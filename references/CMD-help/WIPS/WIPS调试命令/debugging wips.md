::: {#-309197258 .myid}
[]{#_Toc404795060}[]{#struct_0_x1926_14152_508482979}

**WIPS \-- WIPS调试命令 \-- debugging wips**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1926_14152_x959433536}

[**[debugging wips]{lang="EN-US"}**[ { **all** \| **classification** \| **countermeasure** \| **detect** \| **event** }]{lang="EN-US"}]{#struct_0_x1926_14152_x28601159}

[**[undo debugging wips]{lang="EN-US"}**[ { **all** \| **classification** \| **countermeasure** \| **detect** \| **event** }]{lang="EN-US"}]{#struct_0_x1926_14152_x89343848}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1926_14152_974422357}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1926_14152_x845550329}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1926_14152_x1253109459}

[[network-admin]{lang="EN-US"}]{#struct_0_x1926_14152_1493692746}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1926_14152_940994353}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1926_14152_x177222081}

[**[all]{lang="EN-US"}**]{#struct_0_x1926_14152_x1306098901}[：表示]{style="font-family:宋体"}[WIPS]{lang="EN-US"}[所有调试信息开关。]{style="font-family:宋体"}

[**[classification]{lang="EN-US"}**]{#struct_0_x1926_14152_x822763473}[：表示]{style="font-family:宋体"}[WIPS]{lang="EN-US"}[的分类调试信息开关。]{style="font-family:宋体"}

[**[countermeasure]{lang="EN-US"}**]{#struct_0_x1926_14152_x1243324597}[：表示]{style="font-family:宋体"}[WIPS]{lang="EN-US"}[的反制调试信息开关。]{style="font-family:宋体"}

[**[detect]{lang="EN-US"}**]{#struct_0_x1926_14152_x675150870}[：表示]{style="font-family:宋体"}[WIPS]{lang="EN-US"}[的检测调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1926_14152_x719846920}[：表示]{style="font-family:宋体"}[WIPS]{lang="EN-US"}[的事件调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1926_14152_x1644184488}

[**[debugging wips]{lang="EN-US"}**]{#struct_0_x1926_14152_x1124651079}[命令用来打开]{style="font-family:宋体"}[WIPS]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging wips]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[WIPS]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[WIPS]{lang="EN-US"}]{#struct_0_x1926_14152_x849621908}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging wips classification]{lang="EN-US"}]{#struct_0_x1926_14152_x808417749}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1413207681}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_x1926_14152_2146717495}
:::

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_x1926_14152_x517541850}

[[Classified *device* (MAC: *mac-address*) in VSD *vsd-name.*]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_x1926_14152_659709413}

[[在名字为]{style="font-family:宋体"}*[vsd-name]{lang="EN-US"}*]{#struct_0_x1926_14152_74190224}[的]{style="font-family:宋体"}[VSD]{lang="EN-US"}[内将]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[的]{style="font-family:宋体"}[device]{lang="EN-US"}[设备进行分类，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AP]{lang="EN-US"}]{#struct_0_x1926_14152_605227884}[：]{style="font-family:宋体"}[AP]{lang="EN-US"}[设备]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[C]{lang="EN-US"}[lient]{lang="EN-US"}]{#struct_0_x1926_14152_x725439450}[：]{style="font-family:
  宋体"}[客户端设备]{lang="EN-US" style="font-family:宋体"}

[[Classified *device* as *type.*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x1926_14152_x1709383428}

[[将]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x1926_14152_x863029071}*[device]{lang="EN-US" style="font-size:9.0pt"}*[设备分类成]{style="font-size:9.0pt;font-family:宋体"}*[type]{lang="EN-US" style="font-size:9.0pt"}*[类型]{style="font-size:9.0pt;
  font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[device]{lang="EN-US"}*]{#struct_0_x1926_14152_x1771900896}[：]{style="font-family:宋体"}[设备类型，包括：]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AP]{lang="EN-US"}]{#struct_0_x1926_14152_x94544342}[：]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[设备]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Client]{lang="EN-US"}]{#struct_0_x1926_14152_x1474585419}[：客户端设备]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[type]{lang="EN-US"}*]{#struct_0_x1926_14152_32195593}[：]{style="font-family:宋体"}[分类的类型，包括：]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Auth]{lang="EN-US"}]{#struct_0_x1926_14152_x1792006808}[：认证的]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Mis(C)]{lang="EN-US"}]{#struct_0_x1926_14152_830942670}[：错误配置的]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Rogue]{lang="EN-US"}]{#struct_0_x1926_14152_x278190523}[：非法的]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Ext]{lang="EN-US"}]{#struct_0_x1926_14152_x1570176518}[：外部的]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Ad-hoc]{lang="EN-US"}]{#struct_0_x1926_14152_x1780560889}[：]{lang="EN-US" style="font-family:宋体"}[ad-hoc]{lang="EN-US"}[网络的]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Auth(P)]{lang="EN-US"}]{#struct_0_x1926_14152_x143299487}[：潜在认证的]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Rogue(P)]{lang="EN-US"}]{#struct_0_x1926_14152_x736613865}[：潜在非法的]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Ext(P)]{lang="EN-US"}]{#struct_0_x1926_14152_1834899313}[：潜在外部的]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Uncate]{lang="EN-US"}]{#struct_0_x1926_14152_1114719311}[：未分类的]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Auth]{lang="EN-US"}]{#struct_0_x1926_14152_661533954}[：授权的客户端]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Unauth]{lang="EN-US"}]{#struct_0_x1926_14152_2001540925}[：未授权的客户端]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Mis(A)]{lang="EN-US"}]{#struct_0_x1926_14152_656545674}[：错误关联的客户端]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Uncate]{lang="EN-US"}]{#struct_0_x1926_14152_1731981568}[：未分类的客户端]{lang="EN-US" style="font-family:宋体"}

[[Failed to classify *device*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x1926_14152_x898261154}

[[分类]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x1926_14152_x546584014}*[device]{lang="EN-US" style="font-size:9.0pt"}*[设备失败]{style="font-size:9.0pt;font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[device]{lang="EN-US"}*]{#struct_0_x1926_14152_1143488193}[为设备类型，包括：]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AP]{lang="EN-US"}]{#struct_0_x1926_14152_2027087921}[：]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[设备]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Client]{lang="EN-US"}]{#struct_0_x1926_14152_1498985158}[：客户端]{lang="EN-US" style="font-family:宋体"}[设备]{lang="EN-US" style="font-family:宋体"}

[[Created reclassify timer.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x1926_14152_2044966236}

[[创建重分类定时器]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x1926_14152_x163415449}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging wips countermeasure]{lang="EN-US"}]{#struct_0_x1926_14152_966813775}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1412320747}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_x1926_14152_x1596874252}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_x1926_14152_544983687}

[[Stopped countermeasure timer.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x1926_14152_x1174506043}

[[停止反制定时器]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x1926_14152_1019499927}

[[Failed to add countermeasure record for sensor *sensor-id* on radio *radio-id.*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x1926_14152_x257411872}

[[当用]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x1926_14152_436764147}[sensor *sensor-id*]{lang="EN-US" style="font-size:9.0pt"}[的]{style="font-size:9.0pt;font-family:宋体"}[radio *radio-id*]{lang="EN-US" style="font-size:9.0pt"}[反制时添加反制记录失败]{style="font-size:
  9.0pt;font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sensor-id]{lang="EN-US"}*]{#struct_0_x1926_14152_1812116521}[：]{style="font-family:宋体"}[sensor]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[radio-id]{lang="EN-US"}*]{#struct_0_x1926_14152_x30020038}[：]{style="font-family:宋体"}[radio]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[Failed to set countermeasure plan for sensor *sensor-id* on radio *radio-id*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x1926_14152_1055191224}

[[通知]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x1926_14152_x852709291}[sensor *sensor-id*]{lang="EN-US" style="font-size:9.0pt"}[的]{style="font-size:9.0pt;font-family:宋体"}[radio *radio-id*]{lang="EN-US" style="font-size:9.0pt"}[执行反制失败]{style="font-size:
  9.0pt;font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sensor-id]{lang="EN-US"}*]{#struct_0_x1926_14152_x1033297166}[：]{style="font-family:宋体"}[sensor]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[radio-id]{lang="EN-US"}*]{#struct_0_x1926_14152_x2070458076}[：]{style="font-family:宋体"}[radio]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[Countermeasure timer expired.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x1926_14152_1189693991}

[[反制定时器超时]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x1926_14152_422511260}

[[Started countermeasure timer.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_x1926_14152_x96245320}

[[启动反制定时器]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x1926_14152_x867598571}

[[Failed to start countermeasure timer]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x1926_14152_1549499472}

[[启动反制定时器失败]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x1926_14152_x1415881533}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging wips detect]{lang="EN-US"}]{#struct_0_x1926_14152_x36230536}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1438867131}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_x1926_14152_2000185328}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_x1926_14152_x2141364723}

[[Received AP *message-type* message from sensor *sensor-id* on radio *radio-id*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x1926_14152_x958000019}

[[从]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x1926_14152_1881534884}[sensor *sensor-id*]{lang="EN-US" style="font-size:9.0pt"}[的]{style="font-size:9.0pt;font-family:宋体"}[radio *radio-id*]{lang="EN-US" style="font-size:9.0pt"}[收到]{style="font-size:
  9.0pt;font-family:宋体"}[AP]{lang="EN-US" style="font-size:9.0pt"}[的]{style="font-size:9.0pt;font-family:宋体"}*[message-type]{lang="EN-US" style="font-size:9.0pt"}*[事件]{style="font-size:9.0pt;
  font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sensor-id]{lang="EN-US"}*]{#struct_0_x1926_14152_x208189117}[：]{style="font-family:宋体"}[se]{lang="EN-US"}[nsor]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[radio-id]{lang="EN-US"}*]{#struct_0_x1926_14152_1825049171}[：]{style="font-family:宋体"}[radio]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[*[message-type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_x1926_14152_1727090008}[的类型包括：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[update]{lang="EN-US"}]{#struct_0_x1926_14152_1469838621}[：]{lang="EN-US" style="font-family:宋体"}[AC]{lang="EN-US"}[收到]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[更新事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="EN-US"}]{#struct_0_x1926_14152_x237326866}[：]{lang="EN-US" style="font-family:宋体"}[AC]{lang="EN-US"}[收到]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[删除事件]{lang="EN-US" style="font-family:宋体"}

[[Received the message for clearing clients associated with AP *mac-address* from sensor *sensor-id* on radio *radio-id*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x1926_14152_x2003175166}

[[从]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x1926_14152_1705613446}[sensor *sensor-id*]{lang="EN-US" style="font-size:9.0pt"}[的]{style="font-size:9.0pt;font-family:宋体"}[radio *radio-id*]{lang="EN-US" style="font-size:9.0pt"}[收到清除]{style="font-size:
  9.0pt;font-family:宋体"}[MAC]{lang="EN-US" style="font-size:9.0pt"}[地址为]{style="font-size:9.0pt;font-family:宋体"}*[mac-address]{lang="EN-US" style="font-size:9.0pt"}*[的]{style="font-size:9.0pt;
  font-family:宋体"}[AP]{lang="EN-US" style="font-size:9.0pt"}[设备下关联的]{style="font-size:9.0pt;font-family:宋体"}[client]{lang="EN-US" style="font-size:9.0pt"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sensor-id]{lang="EN-US"}*]{#struct_0_x1926_14152_x1834307832}[：]{style="font-family:宋体"}[se]{lang="EN-US"}[nsor]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[radio-id]{lang="EN-US"}*]{#struct_0_x1926_14152_x635304327}[：]{style="font-family:宋体"}[radio]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mac-address]{lang="EN-US"}*]{#struct_0_x1926_14152_1380388835}[：]{style="font-family:宋体"}[AP]{lang="EN-US"}[设备的]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}*[ ]{lang="EN-US"}*

[[Received AP status change message from sensor *sensor-id* on radio *radio-id*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x1926_14152_x246295872}

[[从]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x1926_14152_x1595034924}[sensor *sensor-id*]{lang="EN-US" style="font-size:9.0pt"}[的]{style="font-size:9.0pt;font-family:宋体"}[radio *radio-id*]{lang="EN-US" style="font-size:9.0pt"}[收到]{style="font-size:
  9.0pt;font-family:宋体"}[AP]{lang="EN-US" style="font-size:9.0pt"}[状态改变消息]{style="font-size:9.0pt;font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sensor-id]{lang="EN-US"}*]{#struct_0_x1926_14152_x1165623065}[：]{style="font-family:宋体"}[sensor]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[radio-id]{lang="EN-US"}*]{#struct_0_x1926_14152_260050576}[：]{style="font-family:宋体"}[radio]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[Received AP critical memory gate message from sensor *sensor-id*.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_x1926_14152_974347924}

[[从]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x1926_14152_1988196968}[sensor *sensor-id*]{lang="EN-US" style="font-size:9.0pt"}[收到]{style="font-size:9.0pt;font-family:宋体"}[AP]{lang="EN-US" style="font-size:9.0pt"}[三级内存门限消息]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sensor-id]{lang="EN-US"}*]{#struct_0_x1926_14152_155541643}[：]{style="font-family:宋体"}[sensor]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging wips event]{lang="EN-US"}]{#struct_0_x1926_14152_x1710855955}[令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1441868959}[[字段]{style="font-size:10.0pt;font-family:黑体"}]{#struct_0_x1926_14152_x58537459}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_x1926_14152_x702605557}

[[Failed to send IOCTL message to the AP.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x1926_14152_1417754799}

[[给]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x1926_14152_906483497}[AP]{lang="EN-US" style="font-size:9.0pt"}[发送]{style="font-size:9.0pt;font-family:宋体"}[IOCTL]{lang="EN-US" style="font-size:9.0pt"}[消息失败]{style="font-size:9.0pt;font-family:
  宋体"}

[[Failed to create *timer-type* timer.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x1926_14152_x2022226739}

[[创建]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x1926_14152_x1885553103}*[timer-type]{lang="EN-US" style="font-size:9.0pt"}*[类型定时器失败，]{style="font-size:9.0pt;font-family:宋体"}*[timer-type]{lang="EN-US" style="font-size:9.0pt"}*[为定时器的类型，包括：]{style="font-size:9.0pt;
  font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[reclassify]{lang="EN-US"}]{#struct_0_x1926_14152_x2009590199}[：]{lang="EN-US" style="font-family:宋体"}[学习到的设备重新分类定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[memory threshold recover]{lang="EN-US"}]{#struct_0_x1926_14152_1826134517}[：]{lang="EN-US" style="font-family:宋体"}[内存门限恢复定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[scan]{lang="EN-US"}]{#struct_0_x1926_14152_1250976086}[：]{style="font-family:宋体"}[扫描列表定时器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[reconnect to APMGR]{lang="EN-US"}]{#struct_0_x1926_14152_851732560}[：]{lang="EN-US" style="font-family:
  宋体"}[重连]{lang="EN-US" style="font-family:宋体"}[APMGR]{lang="EN-US"}[定时器]{lang="EN-US" style="font-family:宋体"}

[[Created *timer-type* timer.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_x1926_14152_301497567}

[[创建]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x1926_14152_1259166036}*[timer-type]{lang="EN-US" style="font-size:9.0pt"}*[类型定时器，]{style="font-size:9.0pt;font-family:宋体"}*[timer-type]{lang="EN-US" style="font-size:9.0pt"}*[为定时器的类型，包括：]{style="font-size:9.0pt;
  font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[reclassify]{lang="EN-US"}]{#struct_0_x1926_14152_x1256560305}[：]{lang="EN-US" style="font-family:宋体"}[学习到的设备重新分类定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[memory threshold recover]{lang="EN-US"}]{#struct_0_x1926_14152_x1407208356}[：]{lang="EN-US" style="font-family:宋体"}[内存门限恢复定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[scan]{lang="EN-US"}]{#struct_0_x1926_14152_x1565886521}[：]{style="font-family:宋体"}[扫描列表定时器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[reconnect to APMGR]{lang="EN-US"}]{#struct_0_x1926_14152_1311620728}[：]{lang="EN-US" style="font-family:
  宋体"}[重连]{lang="EN-US" style="font-family:宋体"}[APMGR]{lang="EN-US"}[定时器]{lang="EN-US" style="font-family:宋体"}

[*[Timer-type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_x1926_14152_x1534786335}[ timer expired.]{lang="EN-US" style="font-size:9.0pt"}

[*[Timer-type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_x1926_14152_1422849990}[类型定时器超时，]{style="font-size:9.0pt;font-family:
  宋体"}*[Timer-type]{lang="EN-US" style="font-size:9.0pt"}*[为定时器的类型，包括：]{style="font-size:9.0pt;font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Reclassify]{lang="EN-US"}]{#struct_0_x1926_14152_x1237365678}[：学习到的设备重新分类定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Memory threshold recover]{lang="EN-US"}]{#struct_0_x1926_14152_x523615668}[：内存门限恢复定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[scan]{lang="EN-US"}]{#struct_0_x1926_14152_508535754}[：扫描列表定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Reconnect to APMGR]{lang="EN-US"}]{#struct_0_x1926_14152_1341441126}[：重连]{lang="EN-US" style="font-family:
  宋体"}[APMGR]{lang="EN-US"}[定时器]{lang="EN-US" style="font-family:
  宋体"}

[[Deleted*Timer-type* timer.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x1926_14152_x279857169}

[[删除]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x1926_14152_364988936}*[Timer-type]{lang="EN-US" style="font-size:9.0pt"}*[类型定时器，]{style="font-size:9.0pt;font-family:宋体"}*[Timer-type]{lang="EN-US" style="font-size:9.0pt"}*[为定时器的类型，包括：]{style="font-size:9.0pt;
  font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[reclassify]{lang="EN-US"}]{#struct_0_x1926_14152_1755468632}[：学习到的设备重新分类定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[memory threshold recover]{lang="EN-US"}]{#struct_0_x1926_14152_x1935685273}[：内存门限恢复定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[scan]{lang="EN-US"}]{#struct_0_x1926_14152_x1306033365}[：扫描列表定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[reconnect to APMGR]{lang="EN-US"}]{#struct_0_x1926_14152_1412711087}[：重连]{lang="EN-US" style="font-family:
  宋体"}[APMGR]{lang="EN-US"}[定时器]{lang="EN-US" style="font-family:
  宋体"}

[[Failed to recover configuration of key (Type: *type*).]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x1926_14152_x1989636063}

[[DBM]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_x1926_14152_143428025}[恢复类型为]{style="font-size:9.0pt;font-family:宋体"}*[type]{lang="EN-US" style="font-size:9.0pt"}*[的]{style="font-size:9.0pt;
  font-family:宋体"}[key]{lang="EN-US" style="font-size:9.0pt"}[的配置失败]{style="font-size:9.0pt;font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[type]{lang="EN-US"}*]{#struct_0_x1926_14152_323491168}[：]{style="font-family:宋体"}[DBM]{lang="EN-US"}[存储的]{style="font-family:宋体"}[key]{lang="EN-US"}[的类型，取值为数值]{style="font-family:宋体"}

[[Received HA *type* event.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x1926_14152_x1478519073}

[[收到]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x1926_14152_x398261752}[HA *type*]{lang="EN-US" style="font-size:9.0pt"}[类型事件]{style="font-size:9.0pt;font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[type]{lang="EN-US"}*]{#struct_0_x1926_14152_x1466388253}[为]{lang="EN-US" style="font-family:宋体"}[HA]{lang="EN-US"}[事件类型：]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[upgrade]{lang="EN-US"}]{#struct_0_x1926_14152_x1709317892}[：备进程收到]{lang="EN-US" style="font-family:宋体"}[HA]{lang="EN-US"}[模块通知的升级事件]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[stop]{lang="EN-US"}]{#struct_0_x1926_14152_14747980}[：主进程收到]{lang="EN-US" style="font-family:宋体"}[HA]{lang="EN-US"}[模块通知的停止事件]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[degrade]{lang="EN-US"}]{#struct_0_x1926_14152_x320700303}[：主进程收到]{lang="EN-US" style="font-family:宋体"}[HA]{lang="EN-US"}[模块通知的降级事件]{lang="EN-US" style="font-family:宋体"}

[[Failed to process HA upgrade event.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_x1926_14152_776208763}

[[处理]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x1926_14152_x208508287}[HA]{lang="EN-US" style="font-size:9.0pt"}[升级事件失败]{style="font-size:9.0pt;font-family:宋体"}

[[Failed to recover configuration from DBM.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_x1926_14152_687445539}

[[从]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x1926_14152_x1802734376}[DBM]{lang="EN-US" style="font-size:9.0pt"}[中恢复配置失败]{style="font-size:9.0pt;font-family:宋体"}

[[Failed to synchronize data from APMGR.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x1926_14152_x1063320411}

[[从]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x1926_14152_x143233951}[APMGR]{lang="EN-US" style="font-size:9.0pt"}[模块同步获取数据失败]{style="font-size:9.0pt;font-family:宋体"}

[[Processing system memory threshold alert stop event received by WIPS .]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x1926_14152_1722850316}

[[处理]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x1926_14152_1509700312}[WIPS]{lang="EN-US" style="font-size:9.0pt"}[模块收到系统内存门限恢复事件]{style="font-size:9.0pt;font-family:宋体"}

[[Processing system memory threshold event(Level *level*) received by WIPS.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x1926_14152_x811719801}

[[处理]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x1926_14152_x1857617155}[WIPS]{lang="EN-US" style="font-size:9.0pt"}[模块收到系统内存门限事件，级别为]{style="font-size:9.0pt;font-family:宋体"}*[level]{lang="EN-US" style="font-size:9.0pt"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_x1926_14152_1184705582}[：内存门限级别]{style="font-family:宋体"}

[[Finished async get data from APMGR.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x1926_14152_x546518478}

[[完成从]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x1926_14152_313046539}[APMGR]{lang="EN-US" style="font-size:9.0pt"}[异步获取数据]{style="font-size:9.0pt;font-family:宋体"}

[[Processing AP *event-ype* event from APMGR.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x1926_14152_1455736333}

[[处理来自]{style="font-size:9.0pt;font-family:
  宋体"}]{#struct_0_x1926_14152_71788817}[APMGR]{lang="EN-US" style="font-size:9.0pt"}[模块]{style="font-size:9.0pt;font-family:宋体"}[AP]{lang="EN-US" style="font-size:9.0pt"}[的]{style="font-size:9.0pt;font-family:
  宋体"}*[event-type]{lang="EN-US" style="font-size:9.0pt"}*[事件]{style="font-size:9.0pt;font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[event-type]{lang="EN-US"}*]{#struct_0_x1926_14152_x633622543}[：]{style="font-family:宋体"}[APMGR]{lang="EN-US"}[上报]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[的事件类型，包括：]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[down]{lang="EN-US"}]{#struct_0_x1926_14152_692702222}[：]{lang="EN-US" style="font-family:宋体"}[AC]{lang="EN-US"}[收到]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[的下线事件]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[up]{lang="EN-US"}]{#struct_0_x1926_14152_1019565463}[：]{lang="EN-US" style="font-family:宋体"}[AC]{lang="EN-US"}[收到]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[的上线事件]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[delete]{lang="EN-US"}]{#struct_0_x1926_14152_1763074637}[：]{lang="EN-US" style="font-family:宋体"}[AC]{lang="EN-US"}[收到]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[的删除事件]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[create]{lang="EN-US"}]{#struct_0_x1926_14152_1711875642}[：]{lang="EN-US" style="font-family:宋体"}[AC]{lang="EN-US"}[收到]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[的创建事件]{lang="EN-US" style="font-family:宋体"}

[[Processing radio *event-type* event for radio *radio-id* on AP *ap-id* from APMGR.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_x1926_14152_101802481}

[[处理来自]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x1926_14152_1712445328}[APMGR]{lang="EN-US" style="font-size:9.0pt"}[的]{style="font-size:9.0pt;font-family:宋体"}[AP *ap-id*]{lang="EN-US" style="font-size:9.0pt"}[上]{style="font-size:9.0pt;
  font-family:宋体"}[radio *radio-id*]{lang="EN-US" style="font-size:9.0pt"}[的]{style="font-size:9.0pt;font-family:宋体"}*[event-type]{lang="EN-US" style="font-size:9.0pt"}*[事件]{style="font-size:9.0pt;
  font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[event-type]{lang="EN-US"}*]{#struct_0_x1926_14152_x1597087117}[：]{style="font-family:宋体"}[APMGR]{lang="EN-US"}[上报]{lang="EN-US" style="font-family:宋体"}[radio]{lang="EN-US"}[的事件类型，包括：]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[down]{lang="EN-US"}]{#struct_0_x1926_14152_x96179784}[：]{lang="EN-US" style="font-family:宋体"}[AC]{lang="EN-US"}[收到]{lang="EN-US" style="font-family:宋体"}[radio]{lang="EN-US"}[的下线事件]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[up]{lang="EN-US"}]{#struct_0_x1926_14152_88494496}[：]{lang="EN-US" style="font-family:宋体"}[AC]{lang="EN-US"}[收到]{lang="EN-US" style="font-family:宋体"}[radio]{lang="EN-US"}[的上线事件]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[delete]{lang="EN-US"}]{#struct_0_x1926_14152_x904376751}[：]{lang="EN-US" style="font-family:宋体"}[AC]{lang="EN-US"}[收到]{lang="EN-US" style="font-family:宋体"}[radio]{lang="EN-US"}[的删除事件]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[create]{lang="EN-US"}]{#struct_0_x1926_14152_x135669188}[：]{lang="EN-US" style="font-family:宋体"}[AC]{lang="EN-US"}[收到]{lang="EN-US" style="font-family:宋体"}[radio]{lang="EN-US"}[的创建事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ap-id]{lang="EN-US"}*]{#struct_0_x1926_14152_1164776218}[：]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[radio-id]{lang="EN-US"}*]{#struct_0_x1926_14152_1469904157}[：]{style="font-family:宋体"}[radio]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[Failed to async get data from APMGR: error code = *error-code*.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_x1926_14152_494019862}

[[从]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x1926_14152_x1596927156}[APMGR]{lang="EN-US" style="font-size:9.0pt"}[异步获取数据失败，错误码为]{style="font-size:9.0pt;font-family:宋体"}*[error-code]{lang="EN-US" style="font-size:9.0pt"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_x1926_14152_1500147847}[：]{style="font-family:宋体"}[失败的错误码]{lang="EN-US" style="font-family:宋体"}

[[Failed to process APMGR message: error code = *error-code*.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_x1926_14152_260116112}

[[处理]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x1926_14152_210406304}[APMGR]{lang="EN-US" style="font-size:9.0pt"}[的消息失败，错误码为]{style="font-size:9.0pt;font-family:宋体"}*[error-code]{lang="EN-US" style="font-size:9.0pt"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_x1926_14152_1338942162}[：]{style="font-family:宋体"}[失败的错误码]{lang="EN-US" style="font-family:宋体"}

[[Failed to *event-type* AP event: error code = *error-code*.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_x1926_14152_740359468}

[[处理]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x1926_14152_1826200053}[AP]{lang="EN-US" style="font-size:9.0pt"}[的]{style="font-size:9.0pt;font-family:宋体"}*[event-type]{lang="EN-US" style="font-size:9.0pt"}*[ ]{lang="EN-US" style="font-size:9.0pt"}[事件失败，错误码为]{style="font-size:9.0pt;font-family:
  宋体"}*[error-code]{lang="EN-US" style="font-size:9.0pt"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[event-type]{lang="EN-US"}*]{#struct_0_x1926_14152_470823973}[：]{style="font-family:宋体"}[事件类型，包括：]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[register]{lang="EN-US"}]{#struct_0_x1926_14152_190130328}[：]{lang="EN-US" style="font-family:宋体"}[AC]{lang="EN-US"}[上用户态模块注册接收]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[事件]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[unregister]{lang="EN-US"}]{#struct_0_x1926_14152_x1819168918}[：]{lang="EN-US" style="font-family:宋体"}[AC]{lang="EN-US"}[上用户态模块去]{lang="EN-US" style="font-family:宋体"}[注册接收]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_x1926_14152_x1482651449}[：]{style="font-family:宋体"}[失败的错误码]{lang="EN-US" style="font-family:宋体"}

[[Failed to process *event-type* radio event: error code = *error-code*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x1926_14152_1422915526}

[[处理]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x1926_14152_1130157286}[radio]{lang="EN-US" style="font-size:9.0pt"}[的]{style="font-size:9.0pt;font-family:宋体"}*[event-type]{lang="EN-US" style="font-size:9.0pt"}*[ ]{lang="EN-US" style="font-size:9.0pt"}[事件失败，错误码为]{style="font-size:9.0pt;font-family:
  宋体"}*[error-code]{lang="EN-US" style="font-size:9.0pt"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[event-type]{lang="EN-US"}*]{#struct_0_x1926_14152_272217891}[：]{style="font-family:宋体"}[事件类型，包括：]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[register]{lang="EN-US"}]{#struct_0_x1926_14152_x50738218}[：]{lang="EN-US" style="font-family:宋体"}[AC]{lang="EN-US"}[上用户态模块]{lang="EN-US" style="font-family:宋体"}[注册接收]{lang="EN-US" style="font-family:宋体"}[APMGR]{lang="EN-US"}[事件]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[unregister]{lang="EN-US"}]{#struct_0_x1926_14152_x1305967829}[：]{lang="EN-US" style="font-family:宋体"}[AC]{lang="EN-US"}[上用户态模块去]{lang="EN-US" style="font-family:宋体"}[注册接收]{lang="EN-US" style="font-family:宋体"}[APMGR]{lang="EN-US"}[事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_x1926_14152_x1308311734}[：]{style="font-family:宋体"}[失败的错误码]{lang="EN-US" style="font-family:宋体"}

[[Failed to set scan *type* for AP *ap-id* on radio *radio-id*: error code = *error-code*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x1926_14152_x497417538}

[[在]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x1926_14152_x57369919}[AP *ap-id*]{lang="EN-US" style="font-size:9.0pt"}[的]{style="font-size:9.0pt;font-family:宋体"}[radio *radio-id*]{lang="EN-US" style="font-size:9.0pt"}[上设置扫描]{style="font-size:
  9.0pt;font-family:宋体"}*[type]{lang="EN-US" style="font-size:9.0pt"}*[类型失败，错误码为]{style="font-size:9.0pt;font-family:宋体"}*[error-code]{lang="EN-US" style="font-size:9.0pt"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[type]{lang="EN-US"}*]{#struct_0_x1926_14152_x683349674}[：]{style="font-family:宋体"}[设置的类型，包括：]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[filter]{lang="EN-US"}]{#struct_0_x1926_14152_x1709252356}[：]{lang="EN-US" style="font-family:宋体"}[过滤]{lang="EN-US" style="font-family:
  宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[plan]{lang="EN-US"}]{#struct_0_x1926_14152_1024546499}[：]{lang="EN-US" style="font-family:宋体"}[列表]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ap-id]{lang="EN-US"}*]{#struct_0_x1926_14152_x698529264}[：]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[radio-id]{lang="EN-US"}*]{#struct_0_x1926_14152_822545560}[：]{style="font-family:宋体"}[radio]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_x1926_14152_x143168415}[：]{style="font-family:宋体"}[失败的错误码]{lang="EN-US" style="font-family:宋体"}

[[Set scan *type* for AP *ap-id* on radio *radio-id* successfully.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_x1926_14152_848803236}

[[在]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x1926_14152_x382031929}[AP *ap-id*]{lang="EN-US" style="font-size:9.0pt"}[的]{style="font-size:9.0pt;font-family:宋体"}[radio *radio-id*]{lang="EN-US" style="font-size:9.0pt"}[上设置扫描]{style="font-size:
  9.0pt;font-family:宋体"}*[type]{lang="EN-US" style="font-size:9.0pt"}*[类型成功]{style="font-size:9.0pt;font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[type]{lang="EN-US"}*]{#struct_0_x1926_14152_1157019811}[：]{style="font-family:宋体"}[设置的类型，包括：]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[filter]{lang="EN-US"}]{#struct_0_x1926_14152_x546452942}[：过滤]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[plan]{lang="EN-US"}]{#struct_0_x1926_14152_x1153095653}[：列表]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ap-id]{lang="EN-US"}*]{#struct_0_x1926_14152_1756497264}[：]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[radio-id]{lang="EN-US"}*]{#struct_0_x1926_14152_1019630999}[：]{style="font-family:宋体"}[radio]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[Failed to clear scan filter for AP *ap-id* on radio *radio-id*: error code = *error-code*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x1926_14152_2127824106}

[[在]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x1926_14152_184701931}[AP *ap-id*]{lang="EN-US" style="font-size:9.0pt"}[的]{style="font-size:9.0pt;font-family:宋体"}[radio *radio-id*]{lang="EN-US" style="font-size:9.0pt"}[上清除射频的过滤类型失败，错误码为]{style="font-size:
  9.0pt;font-family:宋体"}*[error-code]{lang="EN-US" style="font-size:9.0pt"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ap-id]{lang="EN-US"}*]{#struct_0_x1926_14152_x96114248}[：]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[radio-id]{lang="EN-US"}*]{#struct_0_x1926_14152_69863919}[：]{style="font-family:宋体"}[radio]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_x1926_14152_1662180200}[：]{style="font-family:宋体"}[失败的错误码]{lang="EN-US" style="font-family:宋体"}

[[Failed to stop scan plan for AP *ap-id* on radio *radio-id*: error code = *error-code*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x1926_14152_1469969693}

[[在]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x1926_14152_x1792728463}[AP *ap-id*]{lang="EN-US" style="font-size:9.0pt"}[的]{style="font-size:9.0pt;font-family:宋体"}[radio *radio-id*]{lang="EN-US" style="font-size:9.0pt"}[上停止扫描列表失败，错误码为]{style="font-size:
  9.0pt;font-family:宋体"}*[error-code]{lang="EN-US" style="font-size:9.0pt"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ap-id]{lang="EN-US"}*]{#struct_0_x1926_14152_1120955909}[：]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[radio-id]{lang="EN-US"}*]{#struct_0_x1926_14152_160486632}[：]{style="font-family:宋体"}[radio]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_x1926_14152_260181648}[：]{style="font-family:宋体"}[失败的错误码]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1926_14152_207486766}

[[\# ]{lang="EN-US"}]{#struct_0_x1926_14152_1572826763}[配置]{style="font-family:宋体"}[WIPS]{lang="EN-US"}[，并打开]{style="font-family:宋体"}[WIPS]{lang="EN-US"}[分类调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging wips classification]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x1926_14152_838332326}

[[\*Apr  4 15:49:28:081 2014 Sysname WIPS/7/]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}[ ]{lang="EN-US"}]{#struct_0_x1926_14152_x410641213}[CLASS: -MDC=1; Classify AP as Rogue]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[*[// ]{lang="EN-US"}*]{#struct_0_x1926_14152_1665228355}*[将]{style="font-family:宋体"}[AP]{lang="EN-US"}[分类为]{style="font-family:宋体"}[Rouge AP]{lang="EN-US"}*

[ ]{lang="EN-US" style="font-size:9.0pt;font-family:\"Courier New\""}

[[\# ]{lang="EN-US"}]{#struct_0_x1926_14152_1485352762}[配置]{style="font-family:宋体"}[WIPS]{lang="EN-US"}[，并打开]{style="font-family:宋体"}[WIPS]{lang="EN-US"}[反制调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging wips countermeasure]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x1926_14152_695176797}

[[\*Apr  4 15:53:28:081 2014 Sysname WIPS/7/]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}[ ]{lang="EN-US"}]{#struct_0_x1926_14152_x232991163}[COUNTERMEASURE: -MDC=1; Failed to add countermeasure record for sensor 100 on radio 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[*[// ]{lang="EN-US"}*]{#struct_0_x1926_14152_191589975}*[使用]{style="font-family:宋体"}[sensor ]{lang="EN-US"}[100]{lang="EN-US"}[的]{style="font-family:宋体"}[radio ]{lang="EN-US"}[1]{lang="EN-US"}[对非法设备进行反制时，添加反制记录失败]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1926_14152_x1182256035}[配置]{style="font-family:宋体"}[WIPS]{lang="EN-US"}[，并打开]{style="font-family:宋体"}[WIPS]{lang="EN-US"}[检测调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging wips detect]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x1926_14152_1533297422}

[[\*Apr  4 15:55:28:081 2014 Sysname WIPS/7/]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}[ ]{lang="EN-US"}]{#struct_0_x1926_14152_x2115717239}[DETECT: -MDC=1; Received AP status change message from sensor 100 on radio 1.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[*[// ]{lang="EN-US"}*]{#struct_0_x1926_14152_883422735}*[从]{style="font-family:宋体"}[sensor 100]{lang="EN-US"}[的]{style="font-family:宋体"}[radio 1]{lang="EN-US"}[收到]{style="font-family:宋体"}[AP]{lang="EN-US"}[状态改变消息]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1926_14152_x429338350}[配置]{style="font-family:宋体"}[WIPS]{lang="EN-US"}[，并打开]{style="font-family:宋体"}[WIPS]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging wips event]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x1926_14152_1826265589}

[[\*Apr  4 15:59:28:081 2014 Sysname WIPS/7/]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}[ ]{lang="EN-US"}]{#struct_0_x1926_14152_x328804791}[EVENT: -MDC=1; Process AP down event from APMGR]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[*[// ]{lang="EN-US"}*]{#struct_0_x1926_14152_x912773257}*[处理来自]{style="font-family:宋体"}[APMGR]{lang="EN-US"}[模块的]{style="font-family:宋体"}[AP]{lang="EN-US"}[下线的事件]{style="font-family:宋体"}*

[ ]{lang="EN-US"}
