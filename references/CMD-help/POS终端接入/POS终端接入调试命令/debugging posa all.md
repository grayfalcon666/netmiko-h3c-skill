::: {#1006158504 .myid}
[]{#_Toc404785861}[]{#struct_0_88685_x1869_x1506331587}[]{#_Toc212180723}

**POS终端接入 \-- POS终端接入调试命令 \-- debugging posa all**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_88685_x1869_x538926223}

[**[debugging posa all ]{lang="EN-US"}**[\[ **terminal** *terminal-id* \| **app** *app-id* \]]{lang="EN-US"}]{#struct_0_88685_x1869_x158271037}

[**[undo debugging posa all ]{lang="EN-US"}**[\[ **terminal** *terminal-id* \| **app** *app-id* \]]{lang="EN-US"}]{#struct_0_88685_x1869_x980062147}

[[【视图】]{style="font-family:黑体"}]{#struct_0_88685_x1869_x828548404}

[[用户视图]{style="font-family:宋体"}]{#struct_0_88685_x1869_653829649}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_88685_x1869_x567734748}

[[network-admin]{lang="EN-US"}]{#struct_0_88685_x1869_x1461914666}

[[mdc-admin]{lang="EN-US"}]{#struct_0_88685_x1869_652429314}

[[【参数】]{style="font-family:黑体"}]{#struct_0_88685_x1869_1125282797}

[**[terminal]{lang="EN-US"}***[ terminal-id]{lang="EN-US"}*]{#struct_0_88685_x1869_236068175}[：]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[app]{lang="EN-US"}***[ app-id]{lang="EN-US"}*]{#struct_0_88685_x1869_x2139833299}[：应用模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_88685_x1869_1401874077}

[**[debugging posa all]{lang="EN-US"}**]{#struct_0_88685_x1869_x2013792941}[命令用来打开]{style="font-family:宋体"}[POS]{lang="EN-US"}[接入所有调试开关。]{style="font-family:宋体"}**[undo debugging posa all]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[POS]{lang="EN-US"}[接入所有调试开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_88685_x1869_x979865539}[接入所有调试开关处于关闭状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_88685_x1869_x1127718699}

[]{#_Toc212180724}[[\# ]{lang="EN-US"}]{#struct_0_88685_x1869_1626142289}[打开]{style="font-family:宋体"}[POS]{lang="EN-US"}[接入所有调试开关，系统视图下，创建]{style="font-family:宋体"}[TCP]{lang="EN-US"}[接入方式的终端模板]{style="font-family:宋体"}[1]{lang="EN-US"}[，端口为]{style="font-family:宋体"}[3000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<System\> debugging posa all]{lang="EN-US"}]{#struct_0_88685_x1869_1100553454}

[\[System\]\*Aug  7 18:20:48:047 2012 System POSA/7/EVENT: -MDC=1; Recv LIPC message type:]{lang="EN-US"}

[SET, code:ADDTERM, sequence:0, length:13.]{lang="EN-US"}

[\*Aug  7 18:20:48:047 2012 System POSA/7/EVENT: -MDC=1; Terminal 1:Add template.]{lang="EN-US"}

[\*Aug  7 18:20:48:048 2012 System POSA/7/EVENT: -MDC=1; Terminal 1:Enable template.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_88685_x1869_30912169}*[添加终端模板成功]{style="font-family:宋体"}*
:::

::: {#-367986712 .myid}
[]{#_Toc404785862}[]{#struct_0_88685_x1869_989147618}

**POS终端接入 \-- POS终端接入调试命令 \-- debugging posa event**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_88685_x1869_x886284545}

[**[debugging posa event]{lang="EN-US"}**[ \[ **terminal** *terminal-id* \| **app** *app-id* \]]{lang="EN-US"}]{#struct_0_88685_x1869_164042416}

[**[undo debugging posa event]{lang="EN-US"}**[ \[ **terminal** *terminal-id* \| **app** *app-id* \]]{lang="EN-US"}]{#struct_0_88685_x1869_x1524076317}

[[【视图】]{style="font-family:黑体"}]{#struct_0_88685_x1869_x979931075}

[[用户视图]{style="font-family:宋体"}]{#struct_0_88685_x1869_x339702204}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_88685_x1869_x440480788}

[[network-admin]{lang="EN-US"}]{#struct_0_88685_x1869_x228060842}

[[mdc-admin]{lang="EN-US"}]{#struct_0_88685_x1869_1955790960}

[[【参数】]{style="font-family:黑体"}]{#struct_0_88685_x1869_x2049563466}

[**[terminal]{lang="EN-US"}***[ terminal-id]{lang="EN-US"}*]{#struct_0_88685_x1869_826733384}[：终端模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[app]{lang="EN-US"}***[ app-id]{lang="EN-US"}*]{#struct_0_88685_x1869_1181600651}[：应用模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_88685_x1869_x2094237909}

[]{#_Ref203361563}[**[debugging posa event]{lang="EN-US"}**]{#struct_0_88685_x1869_x979734467}[命令用来打开]{style="font-family:宋体"}[POS]{lang="EN-US"}[接入事件调试开关。]{style="font-family:宋体"}**[undo debugging posa event]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[POS]{lang="EN-US"}[接入事件调试开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_88685_x1869_x344992500}[接入事件调试开关处于关闭状态。]{style="font-family:宋体"}

[]{#struct_0_88685_x1869_991897725}[[表1-1 ]{lang="EN-US"}[debugging posa event]{lang="EN-US"}]{#_Ref206212114}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1873363010}[[字段]{style="font-family:黑体"}]{#struct_0_88685_x1869_493852854}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_88685_x1869_x194009833}

[[Added map dest:*a*, src:*b*, app:*n*.]{lang="EN-US"}]{#struct_0_88685_x1869_x976024625}

[[添加]{style="font-family:宋体"}[map]{lang="EN-US"}]{#struct_0_88685_x1869_182309897}[节点，目的地址为]{style="font-family:宋体"}[a]{lang="EN-US"}[，源地址为]{style="font-family:宋体"}[b]{lang="EN-US"}

[[Deleted map dest:*a*, src:*b*.]{lang="EN-US"}]{#struct_0_88685_x1869_1525274813}

[[删除]{style="font-family:宋体"}[map]{lang="EN-US"}]{#struct_0_88685_x1869_x979800003}[节点，目的地址为]{style="font-family:宋体"}[a]{lang="EN-US"}[，源地址为]{style="font-family:宋体"}[b]{lang="EN-US"}

[[Changed app of map(dest:*a*,src:*b*) from *m* to *n*.]{lang="EN-US"}]{#struct_0_88685_x1869_x1912405245}

[[修改]{style="font-family:宋体"}[map]{lang="EN-US"}]{#struct_0_88685_x1869_x763902111}[表，目的地址为]{style="font-family:宋体"}[a]{lang="EN-US"}[，源地址为]{style="font-family:宋体"}[b]{lang="EN-US"}

[[Terminal *n*: Terminal instance m found matching app *n*.]{lang="EN-US"}]{#struct_0_88685_x1869_2140539613}

[[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_615993578}[：终端实例匹配]{style="font-family:宋体"}[map]{lang="EN-US"}[表]{style="font-family:宋体"}

[[App *n*: Sent AM-CID packet.]{lang="EN-US"}]{#struct_0_88685_x1869_x1311981276}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_1525181177}[：发送]{style="font-family:宋体"}[AM-CID]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[App *n*: Received response for AM-CID packet.]{lang="EN-US"}]{#struct_0_88685_x1869_x980258754}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_x1169907861}[：应用实例收到]{style="font-family:宋体"}[AM-CID]{lang="EN-US"}[的回应报文]{style="font-family:宋体"}

[[App *n /* Terminal *n*: Enabled template.]{lang="EN-US"}]{#struct_0_88685_x1869_x519985253}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_x1890897715}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：使能模板]{style="font-family:宋体"}

[[App *n /* Terminal *n*: Disabled template.]{lang="EN-US"}]{#struct_0_88685_x1869_314466278}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_766399064}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：去使能模板]{style="font-family:宋体"}

[[App *n / * Terminal *n*: Add template.]{lang="EN-US"}]{#struct_0_88685_x1869_x980324290}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_x52947202}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：添加模板]{style="font-family:宋体"}

[[App *n /* Terminal *n*: Deleted template.]{lang="EN-US"}]{#struct_0_88685_x1869_2032855695}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_x408239980}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：删除模板]{style="font-family:宋体"}

[[App *n*: Bound app to interface.]{lang="EN-US"}]{#struct_0_88685_x1869_x1072690645}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_x980127682}[：应用模板与接口绑定]{style="font-family:宋体"}

[[App n:Unbound app from interface.]{lang="EN-US"}]{#struct_0_88685_x1869_748593712}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_295615656}[：取消应用模板与接口的绑定]{style="font-family:宋体"}

[[App *n /* Terminal *n*: Failed to add template, The template ID has existed.]{lang="EN-US"}]{#struct_0_88685_x1869_890133639}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_x263969007}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：由于模板已存在，导致添加模板失败]{style="font-family:宋体"}

[[App *n /* Terminal *n*: Failed to bind interface,The interface has been bounded.]{lang="EN-US"}]{#struct_0_88685_x1869_x980193218}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_x797978675}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：由于接口已被绑定，导致绑定接口失败]{style="font-family:宋体"}

[[App *n*: Changed source IP from *p* to *q*.]{lang="EN-US"}]{#struct_0_88685_x1869_x1553694290}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_1467876371}[：修改源]{style="font-family:宋体"}[IP]{lang="EN-US"}

[[App *n*: Changed source port from *m* to *n*.]{lang="EN-US"}]{#struct_0_88685_x1869_679218795}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_x979996610}[：修改源端口]{style="font-family:宋体"}

[[App *n*: Changed app IP from *p* to *q*]{lang="EN-US"}]{#struct_0_88685_x1869_1213054599}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_x1885874296}[：修改前置机]{style="font-family:宋体"}[IP]{lang="EN-US"}

[[App *n*: Changed app port from *m* to *n*.]{lang="EN-US"}]{#struct_0_88685_x1869_595015309}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_x980062146}[：修改前置机端口]{style="font-family:宋体"}

[[App *n*: Changed hello interval from *m* to *n*.]{lang="EN-US"}]{#struct_0_88685_x1869_x828613940}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_245194607}[：修改]{style="font-family:宋体"}[Hello]{lang="EN-US"}[间隔时间]{style="font-family:宋体"}

[[App *n*: Changed hello switch from *m* to *n*.]{lang="EN-US"}]{#struct_0_88685_x1869_1504467870}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_x979865538}[：修改握手功能使能开关]{style="font-family:宋体"}

[[App *n*: Changed sending caller-number switch from *m* to *n*.\"]{lang="EN-US"}]{#struct_0_88685_x1869_x1127784235}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_x254441126}[：修改主叫号码使能开关]{style="font-family:宋体"}

[[App *n*:Changed mode to temporary.]{lang="EN-US"}]{#struct_0_88685_x1869_187661808}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_859410421}[：修改连接方式为短连接]{style="font-family:宋体"}

[[App *n*: Changed mode to permanent.]{lang="EN-US"}]{#struct_0_88685_x1869_x979931074}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_x339636668}[：修改连接方式为长连接]{style="font-family:宋体"}

[[App *n*:Changed TCP keepalive interval and number from (*m*, *n*) to (*m*, *n*).]{lang="EN-US"}]{#struct_0_88685_x1869_753793441}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_x1522980336}[：修改保活报文发送的时间间隔和次数]{style="font-family:宋体"}

[[App *n*: Changed app link-time from *p* to *q*.]{lang="EN-US"}]{#struct_0_88685_x1869_x979734466}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_x344926964}[：修改连接请求超时时间]{style="font-family:宋体"}

[[App *n*:Changed quiet time from *p* to *q*.]{lang="EN-US"}]{#struct_0_88685_x1869_684217867}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_x979800002}[：修改静默时间]{style="font-family:宋体"}

[[App *n /* Terminal *n*: Changed description from *p* to *q*.]{lang="EN-US"}]{#struct_0_88685_x1869_x1912470781}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_1034195405}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：修改描述信息]{style="font-family:宋体"}

[[App *n*:Changed backup app form *p* to *q*.]{lang="EN-US"}]{#struct_0_88685_x1869_997379573}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_x980258757}[：修改备份]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用]{style="font-family:宋体"}

[[App *n*: Changed TPDU-change-strategy source.]{lang="EN-US"}]{#struct_0_88685_x1869_x1169842325}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_1916246506}[：修改]{style="font-family:宋体"}[TPDU]{lang="EN-US"}[源地址]{style="font-family:宋体"}

[[App *n*: Changed TPDU-change-strategy destination.]{lang="EN-US"}]{#struct_0_88685_x1869_1811738269}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_x980324293}[：修改]{style="font-family:宋体"}[TPDU]{lang="EN-US"}[目的地址]{style="font-family:宋体"}

[[App *n /* Terminal *n*: Created instance *m*.]{lang="EN-US"}]{#struct_0_88685_x1869_x52750594}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_x144858261}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：创建实例]{style="font-family:宋体"}*[m]{lang="EN-US"}*

[[App *n /* Terminal *n*: Deleted instance *m*.]{lang="EN-US"}]{#struct_0_88685_x1869_x980127685}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_748266032}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：删除实例]{style="font-family:宋体"}*[m]{lang="EN-US"}*

[[App *n /* Terminal *n*: Reset instance *m*]{lang="EN-US"}]{#struct_0_88685_x1869_418274504}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_x980193221}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：重置实例]{style="font-family:宋体"}*[m]{lang="EN-US"}*

[[App *n*: Reset the socket keepalive for instance *m*.]{lang="EN-US"}]{#struct_0_88685_x1869_x797519926}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_361434260}[：重置实例]{style="font-family:宋体"}*[m]{lang="EN-US"}*[保活]{style="font-family:宋体"}[socket]{lang="EN-US"}

[[Terminal *n*: Accepted a new connecting request.]{lang="EN-US"}]{#struct_0_88685_x1869_90903307}

[[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_x979996613}[：获取新的连接请求]{style="font-family:宋体"}

[[App *n*: Connect to app.]{lang="EN-US"}]{#struct_0_88685_x1869_1213120135}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_x666565371}[：连接到]{style="font-family:宋体"}[app]{lang="EN-US"}

[[App *n /* Terminal *n*: Instance *m* received epollout event.]{lang="EN-US"}]{#struct_0_88685_x1869_x980062149}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_x828417332}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：实例]{style="font-family:宋体"}*[m]{lang="EN-US"}*[收到]{style="font-family:宋体"}[epollout]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[App *n /* Terminal *n*: Instance *m* link error.]{lang="EN-US"}]{#struct_0_88685_x1869_303008958}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_x979865541}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：实例]{style="font-family:宋体"}*[m]{lang="EN-US"}*[收到]{style="font-family:宋体"}[epollup]{lang="EN-US"}[或]{style="font-family:宋体"}[epollerr]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[App *n /* Terminal *n*: Instance *m* received packet.]{lang="EN-US"}]{#struct_0_88685_x1869_x1128242992}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_x2044469649}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：实例]{style="font-family:宋体"}*[m]{lang="EN-US"}*[报文]{style="font-family:宋体"}

[[App *n /* Terminal *n*: Instance *m* sent packet.]{lang="EN-US"}]{#struct_0_88685_x1869_x979931077}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_x339833276}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：实例]{style="font-family:宋体"}*[m]{lang="EN-US"}*[发送报文]{style="font-family:宋体"}

[[App *n /* Terminal *n*: Instance link peer closed.]{lang="EN-US"}]{#struct_0_88685_x1869_1114527663}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_x979734469}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：连接已关闭]{style="font-family:宋体"}

[[App *n /* Terminal *n*: Received a completed packet, length=*m*.]{lang="EN-US"}]{#struct_0_88685_x1869_x344599284}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_1753885354}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：接收到长度为]{style="font-family:宋体"}*[m]{lang="EN-US"}*[的完整报文]{style="font-family:宋体"}

[[Failed to get terminal instance by handle(*n*).]{lang="EN-US"}]{#struct_0_88685_x1869_x979800005}

[[通过]{style="font-family:宋体"}[handle(*n*)]{lang="EN-US"}]{#struct_0_88685_x1869_x1912012029}[获取终端实例失败]{style="font-family:宋体"}

[[App *n /* Terminal *n*: Interface *ifname*: event=*type*.]{lang="EN-US"}]{#struct_0_88685_x1869_x980258756}

[[应用]{style="font-size:9.0pt;font-family:宋体"}]{#struct_0_88685_x1869_x1169776789}*[n]{lang="EN-US" style="font-size:9.0pt"}*[ / ]{lang="EN-US" style="font-size:9.0pt"}[终端]{style="font-size:9.0pt;font-family:宋体"}*[n]{lang="EN-US" style="font-size:9.0pt"}*[：接口名：事件。]{style="font-size:9.0pt;
  font-family:宋体"}[(]{lang="EN-US" style="font-size:9.0pt"}[其中]{style="font-size:9.0pt;font-family:宋体"}*[type]{lang="EN-US" style="font-size:9.0pt"}*[包括：]{style="font-size:9.0pt;
  font-family:宋体"}[insert]{lang="EN-US" style="font-size:9.0pt"}[、]{style="font-size:9.0pt;font-family:宋体"}[remove]{lang="EN-US" style="font-size:9.0pt"}[、]{style="font-size:9.0pt;font-family:
  宋体"}[up]{lang="EN-US" style="font-size:9.0pt"}[、]{style="font-size:9.0pt;font-family:宋体"}[down]{lang="EN-US" style="font-size:9.0pt"}[、]{style="font-size:9.0pt;font-family:
  宋体"}[delete]{lang="EN-US" style="font-size:9.0pt"}[、]{style="font-size:9.0pt;font-family:宋体"}[create]{lang="EN-US" style="font-size:9.0pt"}[、]{style="font-size:9.0pt;font-family:
  宋体"}[deactive)]{lang="EN-US" style="font-size:9.0pt"}

[[App *n /* Terminal *n*:Interface *ifname* TTY event=*type*.]{lang="EN-US"}]{#struct_0_88685_x1869_x1152705881}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*[ / ]{lang="EN-US"}]{#struct_0_88685_x1869_x980324292}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：收到接口]{style="font-family:宋体"}[(*ifname*)]{lang="EN-US"}[的]{style="font-family:宋体"}[tty]{lang="EN-US"}[事件。]{style="font-family:宋体"}[(]{lang="EN-US"}[其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[包括：]{style="font-family:宋体"}[ready]{lang="EN-US"}[、]{style="font-family:宋体"}[release)]{lang="EN-US"}

[[Connected to TTYM.]{lang="EN-US"}]{#struct_0_88685_x1869_x52816130}

[[连接到]{style="font-family:宋体"}[TTYM]{lang="EN-US"}]{#struct_0_88685_x1869_478442863}

[[App *n /* Terminal *n*: Registered interface *ifname* to with TTYM.]{lang="EN-US"}]{#struct_0_88685_x1869_x980127684}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*[ / ]{lang="EN-US"}]{#struct_0_88685_x1869_748200496}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：向]{style="font-family:宋体"}[ttym]{lang="EN-US"}[注册接口]{style="font-family:宋体"}[(*ifname*)]{lang="EN-US"}

[[App *n /* Terminal *n*: Unregistered interface *ifname* with TTYM.]{lang="EN-US"}]{#struct_0_88685_x1869_x980193220}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*[ / ]{lang="EN-US"}]{#struct_0_88685_x1869_x797454390}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：向]{style="font-family:宋体"}[ttym]{lang="EN-US"}[撤销注册接口]{style="font-family:宋体"}[(*ifname*)]{lang="EN-US"}

[[App *n /* Terminal *n*: Got control TTY device for interface *ifname*.]{lang="EN-US"}]{#struct_0_88685_x1869_x441190247}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*[ / ]{lang="EN-US"}]{#struct_0_88685_x1869_x979996612}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：接口]{style="font-family:宋体"}[(*ifname)*]{lang="EN-US"}[获取]{style="font-family:宋体"}[tty]{lang="EN-US"}[设备控制权]{style="font-family:宋体"}

[[App *n /* Terminal *n*: Released control over TTY device for interface *ifname*.]{lang="EN-US"}]{#struct_0_88685_x1869_1213185671}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*[ / ]{lang="EN-US"}]{#struct_0_88685_x1869_x980062148}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：接口]{style="font-family:宋体"}[(*ifname)*]{lang="EN-US"}[放弃]{style="font-family:宋体"}[tty]{lang="EN-US"}[设备控制权]{style="font-family:宋体"}

[[App *n /* Terminal *n*: Opened device *s*.]{lang="EN-US"}]{#struct_0_88685_x1869_x828482868}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*[ / ]{lang="EN-US"}]{#struct_0_88685_x1869_x516953452}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：打开设备]{style="font-family:宋体"}[(*s*)]{lang="EN-US"}

[[Batch backup for configurations started.]{lang="EN-US"}]{#struct_0_88685_x1869_x979865540}

[[批备数据开始]{style="font-family:宋体"}]{#struct_0_88685_x1869_x1128308528}

[[Batch backup for configurations ended.]{lang="EN-US"}]{#struct_0_88685_x1869_x979931076}

[[批备数据结束]{style="font-family:宋体"}]{#struct_0_88685_x1869_x339767740}

[[Batched up app *n* configuration.]{lang="EN-US"}]{#struct_0_88685_x1869_x979734468}

[[批备]{style="font-family:宋体"}[app *n*]{lang="EN-US"}]{#struct_0_88685_x1869_x344533748}[配置]{style="font-family:宋体"}

[[Batched up terminal *n* configuration.]{lang="EN-US"}]{#struct_0_88685_x1869_x945120104}

[[批备]{style="font-family:宋体"}[terminal *n*]{lang="EN-US"}]{#struct_0_88685_x1869_x979800004}[配置]{style="font-family:宋体"}

[[Batched up terminal *n* description.]{lang="EN-US"}]{#struct_0_88685_x1869_x1912077565}

[[批备]{style="font-family:宋体"}[terminal *n*]{lang="EN-US"}]{#struct_0_88685_x1869_585825188}[描述信息]{style="font-family:宋体"}

[[Batched up global FCM configuration.]{lang="EN-US"}]{#struct_0_88685_x1869_887857084}

[[批备]{style="font-family:宋体"}[FCM]{lang="EN-US"}]{#struct_0_88685_x1869_585759652}[全局配置]{style="font-family:宋体"}

[[Batched up FCM negotiation and threshold configuration for interface *ifname*.]{lang="EN-US"}]{#struct_0_88685_x1869_2513102}

[[为接口]{style="font-family:宋体"}[(*ifname*)]{lang="EN-US"}]{#struct_0_88685_x1869_x1006236720}[批备]{style="font-family:宋体"}[FCM]{lang="EN-US"}[协商和临界值配置]{style="font-family:宋体"}

[[Batched up map (DST=*a*, SRC=*b*) configuration.]{lang="EN-US"}]{#struct_0_88685_x1869_585956260}

[[批备]{style="font-family:宋体"}[map]{lang="EN-US"}]{#struct_0_88685_x1869_1319775036}[配置，目的地址为]{style="font-family:宋体"}*[a]{lang="EN-US"}*[，源地址为]{style="font-family:宋体"}*[b]{lang="EN-US"}*

[[Batched up trap configuration.]{lang="EN-US"}]{#struct_0_88685_x1869_585890724}

[[批备]{style="font-family:宋体"}[trap]{lang="EN-US"}]{#struct_0_88685_x1869_x210771259}[配置]{style="font-family:宋体"}

[[Batched up caller-IP *n* configuration.]{lang="EN-US"}]{#struct_0_88685_x1869_586087332}

[[批备]{style="font-family:宋体"}[caller-IP *n*]{lang="EN-US"}]{#struct_0_88685_x1869_648388403}[配置]{style="font-family:宋体"}

[[Batched up caller-id *s* configuration.]{lang="EN-US"}]{#struct_0_88685_x1869_586021796}

[[批备]{style="font-family:宋体"}[caller-id *s*]{lang="EN-US"}]{#struct_0_88685_x1869_1839952705}[配置]{style="font-family:宋体"}

[[Batched up posa server configuration.]{lang="EN-US"}]{#struct_0_88685_x1869_586218404}

[[批备]{style="font-family:宋体"}[posa]{lang="EN-US"}]{#struct_0_88685_x1869_1716851985}[服务配置]{style="font-family:宋体"}

[[Receiving batch backup configurations finished.]{lang="EN-US"}]{#struct_0_88685_x1869_586152868}

[[批备完成]{style="font-family:宋体"}]{#struct_0_88685_x1869_x852713907}

[[Sent batch backup request.]{lang="EN-US"}]{#struct_0_88685_x1869_586349476}

[[发送批备请求]{style="font-family:宋体"}]{#struct_0_88685_x1869_546706878}

[[Received LIPC message type=*a*, code=*b*, sequence=*c*, length=*d*.]{lang="EN-US"}]{#struct_0_88685_x1869_363699704}

[[收到]{style="font-family:宋体"}[LIPC]{lang="EN-US"}]{#struct_0_88685_x1869_586283940}[消息，类型：]{style="font-family:宋体"}*[a]{lang="EN-US"}*[，操作：]{style="font-family:宋体"}*[b]{lang="EN-US"}*[，序列：]{style="font-family:宋体"}*[c]{lang="EN-US"}*[，长度：]{style="font-family:宋体"}*[d]{lang="EN-US"}*

[[LIPC connected.]{lang="EN-US"}]{#struct_0_88685_x1869_979767587}

[[LIPC]{lang="EN-US"}]{#struct_0_88685_x1869_585825189}[已连接]{style="font-family:宋体"}

[[LIPC disconnected.]{lang="EN-US"}]{#struct_0_88685_x1869_887857083}

[[LIPC]{lang="EN-US"}]{#struct_0_88685_x1869_585759653}[断开]{style="font-family:宋体"}

[[Terminal *n*: Caller number was *s*.]{lang="EN-US"}]{#struct_0_88685_x1869_2513103}

[[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_585956261}[：主叫号码是]{style="font-family:宋体"}*[s]{lang="EN-US"}*

[[App *n /* Terminal *n*: Waited to send packet.]{lang="EN-US"}]{#struct_0_88685_x1869_1319775037}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*[ / ]{lang="EN-US"}]{#struct_0_88685_x1869_585890725}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：由于当前发送缓存区已存在数据，所以延迟发送当前报文]{style="font-family:宋体"}

[[Kernel received FCM event: *n*, for interface ]{lang="EN-US"}*[ifname]{lang="EN-US"}*]{#struct_0_88685_x1869_586087333}

[[内核收到]{style="font-family:宋体"}]{#struct_0_88685_x1869_648388402}[fcm]{lang="EN-US"}[接口]{style="font-family:宋体"}*[ifname]{lang="EN-US"}*[的事件]{style="font-family:宋体"}*[n]{lang="EN-US"}*

[[Kernel published the event to POSA daemon.]{lang="EN-US"}]{#struct_0_88685_x1869_586021797}

[[内核把事件传到]{style="font-family:宋体"}]{#struct_0_88685_x1869_1839952704}[posa]{lang="EN-US"}[后台进程]{style="font-family:宋体"}

[[Kernel got interface ]{lang="EN-US"}*[ifname]{lang="EN-US"}*]{#struct_0_88685_x1869_586218405}[ statistics and returned *m*]{lang="EN-US"}

[[内核获取接口]{style="font-family:宋体"}]{#struct_0_88685_x1869_1716851986}*[ifname]{lang="EN-US"}*[的统计，返回]{style="font-family:宋体"}*[m]{lang="EN-US"}*

[[Kernel hung up the interface ]{lang="EN-US"}*[ifname]{lang="EN-US"}*]{#struct_0_88685_x1869_586152869}[ POS and returned *m*]{lang="EN-US"}

[[内核挂起接口]{style="font-family:宋体"}*[ifname]{lang="EN-US"}*]{#struct_0_88685_x1869_x852713906}[下的]{style="font-family:宋体"}[pos]{lang="EN-US"}[机，返回]{style="font-family:宋体"}*[m]{lang="EN-US"}*

[[Kernel got the interface ]{lang="EN-US"}*[ifname]{lang="EN-US"}*]{#struct_0_88685_x1869_586349477}[ s POS calling number and returned *m*]{lang="EN-US"}

[[内核获取接口]{style="font-family:宋体"}*[ifname]{lang="EN-US"}*]{#struct_0_88685_x1869_546706877}[下的]{style="font-family:宋体"}[pos]{lang="EN-US"}[机，主机号码返回值]{style="font-family:宋体"}*[m]{lang="EN-US"}*

[[Kernel set the interface ]{lang="EN-US"}*[ifname]{lang="EN-US"}*]{#struct_0_88685_x1869_586283941}[ para (cmd=n value=d) and returned *m*]{lang="EN-US"}

[[内核设置接口]{style="font-family:宋体"}*[ifname]{lang="EN-US"}*]{#struct_0_88685_x1869_979767586}[值参数（命令字：]{style="font-family:宋体"}[n]{lang="EN-US"}[，值：]{style="font-family:宋体"}[d]{lang="EN-US"}[），返回]{style="font-family:宋体"}*[m]{lang="EN-US"}*

[[Kernel set the FCM timer parameter (answer-time=a, trade-time=b) and returned *m*]{lang="EN-US"}]{#struct_0_88685_x1869_585825186}

[[内核设置]{style="font-family:宋体"}]{#struct_0_88685_x1869_585759650}[fcm]{lang="EN-US"}[定时器参数，返回]{style="font-family:宋体"}*[m]{lang="EN-US"}*

[[Added TPDU-replace entry: terminal*=*]{lang="EN-US"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_788518265}[, destination=]{lang="EN-US"}*[0xaaaa]{lang="EN-US"}*[ to , des-code=]{lang="EN-US"}*[0xbbbb]{lang="EN-US"}*[.]{lang="EN-US"}

[[添加]{style="font-family:宋体"}]{#struct_0_88685_x1869_x777565676}[TPDU-replace]{lang="EN-US"}[配置：将终端为]{style="font-family:宋体"}*[n]{lang="EN-US"}*[且目的地址为]{style="font-family:宋体"}*[0xaaaa]{lang="EN-US"}*[的报文的目的地址]{style="font-family:宋体"}[替换为]{style="font-family:宋体"}*[0xbbbb]{lang="EN-US"}*

[[Updated TPDU-replace entry (terminal=]{lang="EN-US"}*[ n]{lang="EN-US"}*]{#struct_0_88685_x1869_1144683089}[, destination=]{lang="EN-US"}*[0xaaaa]{lang="EN-US"}*[)]{lang="EN-US"}[ changed des-code from ]{lang="EN-US"}*[0xbbbb]{lang="EN-US"}*[ to ]{lang="EN-US"}*[0xcccc]{lang="EN-US"}*[.]{lang="EN-US"}

[[修改]{style="font-family:宋体"}]{#struct_0_88685_x1869_765054721}[TPDU-replace]{lang="EN-US"}[配置：将终端为]{style="font-family:宋体"}*[n]{lang="EN-US"}*[且目的地址为]{style="font-family:宋体"}*[0xaaaa]{lang="EN-US"}*[的对应的替换目的地址由]{style="font-family:宋体"}*[0xbbbb]{lang="EN-US"}*[修改为]{style="font-family:宋体"}*[0xcccc]{lang="EN-US"}*

[[Deleted TPDU-replace enty: terminal=]{lang="EN-US"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_x421400852}[, destination=]{lang="EN-US"}*[0xaaaa]{lang="EN-US"}*[.]{lang="EN-US"}

[[删除]{style="font-family:宋体"}]{#struct_0_88685_x1869_x1987484793}[TPDU-replace]{lang="EN-US"}[配置：将终端为]{style="font-family:宋体"}*[n]{lang="EN-US"}*[且目的地址为]{style="font-family:宋体"}[0xaaaa]{lang="EN-US"}[的替换配置删除]{style="font-family:宋体"}

[[Terminal *n*]{lang="EN-US"}]{#struct_0_88685_x1869_295006597}[: Replaced des-code from ]{lang="EN-US"}*[0xaaaa]{lang="EN-US"}*[ to ]{lang="EN-US"}*[0xbbbb]{lang="EN-US"}*[.]{lang="EN-US"}

[[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_741398562}[：将报文的目的地址由]{style="font-family:宋体"}*[0xaaaa]{lang="EN-US"}*[替换为]{style="font-family:宋体"}*[0xbbbb]{lang="EN-US"}*

[[Terminal *n*]{lang="EN-US"}]{#struct_0_88685_x1869_x824685379}[: Failed to match TPDU-replace table with destination ]{lang="EN-US"}*[0xaaaa]{lang="EN-US"}*[.]{lang="EN-US"}

[[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_x1715428406}[：由于找不到对应的替换策略而替换地址失败]{style="font-family:宋体"}

[[Batched up TPDU-replace configuration: terminal=*n*, destination=*0xaaaa*, des-code=*0xbbbb*.]{lang="EN-US"}]{#struct_0_88685_x1869_1904197976}

[[批备]{style="font-family:宋体"}[posa ]{lang="EN-US"}]{#struct_0_88685_x1869_338114035}[TPDU]{lang="EN-US"}[-replace]{lang="EN-US"}[配置]{style="font-family:
  宋体"}

[[Started to close allTCP terminal listen ports.]{lang="EN-US"}]{#struct_0_88685_x1869_x1227969906}

[[开始关闭所有]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_88685_x1869_788452729}[终端的监听端口]{style="font-family:宋体"}

[[Started to open all TCP terminal listen ports.]{lang="EN-US"}]{#struct_0_88685_x1869_x2041988317}

[[开始打开所有]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_88685_x1869_x777631212}[终端的监听端口]{style="font-family:宋体"}

[[Batched up posa auto-stop service configuration.]{lang="EN-US"}]{#struct_0_88685_x1869_1278900817}

[[批备]{style="font-family:宋体"}[posa]{lang="EN-US"}]{#struct_0_88685_x1869_x1595067423}[自动关闭终端服务的配置]{style="font-family:宋体"}

[[App *n*]{lang="EN-US"}]{#struct_0_88685_x1869_x287183124}[: Changed auto-connect interval from ]{lang="EN-US"}*[a]{lang="EN-US"}*[ to ]{lang="EN-US"}*[b]{lang="EN-US"}*[ minutes.]{lang="EN-US"}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_x1853267065}[：将自动连接时长由]{style="font-family:宋体"}*[a]{lang="EN-US"}*[分钟修改为]{style="font-family:宋体"}*[b]{lang="EN-US"}*[分钟]{style="font-family:宋体"}

[[App *n*]{lang="EN-US"}]{#struct_0_88685_x1869_x299281134}[: Enabled auto-connect.]{lang="EN-US"}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_875616290}[：开启自动连接功能]{style="font-family:宋体"}

[[App *n*]{lang="EN-US"}]{#struct_0_88685_x1869_x690467651}[: Disabled auto-connect.]{lang="EN-US"}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_184326852}[：关闭自动连接功能]{style="font-family:宋体"}

[[App *n*]{lang="EN-US"}]{#struct_0_88685_x1869_2038415704}[: ]{lang="EN-US"}[Started auto-connect to server(IP: *x.x.x.x*, port: *a*).]{lang="EN-US"}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_x1987526121}[：开始自动向前置机（]{style="font-family:宋体"}[IP]{lang="EN-US"}[为]{style="font-family:宋体"}*[x.x.x.x]{lang="EN-US"}*[，端口为]{style="font-family:宋体"}*[a]{lang="EN-US"}*[）发起连接]{style="font-family:宋体"}

[[Terminal *n*]{lang="EN-US"}]{#struct_0_88685_x1869_472331763}[:]{lang="EN-US"}[ ]{lang="EN-US"}[Changed idle time from ]{lang="EN-US"}*[a]{lang="EN-US"}*[ to]{lang="EN-US"}*[ b]{lang="EN-US"}*[ minute(s).]{lang="EN-US"}

[[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_x1093752178}[：将空闲时间由]{style="font-family:宋体"}*[a]{lang="EN-US"}*[分钟修改为]{style="font-family:宋体"}*[b]{lang="EN-US"}*[分钟]{style="font-family:宋体"}

[[Terminal *n*]{lang="EN-US"}]{#struct_0_88685_x1869_232605698}[:]{lang="EN-US"}[ ]{lang="EN-US"}[Instance ]{lang="EN-US"}*[m]{lang="EN-US"}*[ cleared idle-time count.]{lang="EN-US"}

[[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_922670457}[：实例]{style="font-family:宋体"}*[m]{lang="EN-US"}*[将空闲计数器重置为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[Terminal *n*: Instance *m* has ]{lang="EN-US"}]{#struct_0_88685_x1869_1958918556}[successfully got trade]{lang="EN-US"}[ number *o*.]{lang="EN-US"}

[[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_1958984092}[：实例]{style="font-family:宋体"}*[m]{lang="EN-US"}*[成功获取到交易号]{style="font-family:宋体"}*[o]{lang="EN-US"}*

[[Terminal *n*: Instance *m*]{lang="EN-US"}]{#struct_0_88685_x1869_1958787484}[ released trade number ]{lang="EN-US"}*[o]{lang="EN-US"}*[.]{lang="EN-US"}

[[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_x788466581}[：实例]{style="font-family:宋体"}*[m]{lang="EN-US"}*[释放交易号]{style="font-family:宋体"}*[o]{lang="EN-US"}*

[[Changed the concurrent trades limit for each TCP connection from ]{lang="EN-US"}*[m]{lang="EN-US"}*]{#struct_0_88685_x1869_1958853020}[ to ]{lang="EN-US"}*[n]{lang="EN-US"}*[.]{lang="EN-US"}

[[将每条]{style="font-family:宋体"}]{#struct_0_88685_x1869_1959704988}[TCP]{lang="EN-US"}[连接的并发交易数上限值从]{style="font-family:宋体"}*[m]{lang="EN-US"}*[修改为]{style="font-family:宋体"}*[n]{lang="EN-US"}*

[[Changed the trade timeout from *m* to *n*]{lang="EN-US"}[ seconds.]{lang="EN-US"}]{#struct_0_88685_x1869_x469413316}

[[将每笔交易的超时时间从]{style="font-family:宋体"}*[m]{lang="EN-US"}*]{#struct_0_88685_x1869_1959770524}[秒]{style="font-family:宋体"}[修改为]{style="font-family:宋体"}*[n]{lang="EN-US"}*[秒]{style="font-family:宋体"}

[[Changed the TCP terminal ]{lang="EN-US"}[concurrent ]{lang="EN-US"}]{#struct_0_88685_x1869_x438819662}[connections threshold from *m* to *n*]{lang="EN-US"}[.]{lang="EN-US"}

[[将]{style="font-family:宋体"}]{#struct_0_88685_x1869_1959180699}[TCP]{lang="EN-US"}[接入方式的终端的并发连接数阈值从]{style="font-family:宋体"}*[m]{lang="EN-US"}*[修改为]{style="font-family:宋体"}*[n]{lang="EN-US"}*

[[Changed the FCM terminal ]{lang="EN-US"}[concurrent ]{lang="EN-US"}]{#struct_0_88685_x1869_1959246235}[connections threshold from *m* to *n*]{lang="EN-US"}[.]{lang="EN-US"}

[[将]{style="font-family:宋体"}]{#struct_0_88685_x1869_x447845970}[FCM]{lang="EN-US"}[接入方式的终端的并发连接数阈值从]{style="font-family:宋体"}*[m]{lang="EN-US"}*[修改为]{style="font-family:宋体"}*[n]{lang="EN-US"}*

[[Batch]{lang="EN-US"}]{#struct_0_88685_x1869_1959049627}[ ]{lang="EN-US" style="font-size:10.5pt"}[ed up the TCP terminal concurrent connections threshold configuration.]{lang="EN-US"}

[[备份]{style="font-family:宋体"}]{#struct_0_88685_x1869_x96905904}[TCP]{lang="EN-US"}[接入方式的终端并发连接数阈值的配置到接口板]{style="font-family:宋体"}

[[Batch]{lang="EN-US"}]{#struct_0_88685_x1869_1959115163}[ ]{lang="EN-US" style="font-size:10.5pt"}[ed up the FCM terminal concurrent connections threshold configuration.]{lang="EN-US"}

[[备份]{style="font-family:宋体"}]{#struct_0_88685_x1869_x431104531}[FCM]{lang="EN-US"}[接入方式终端并发连接数阈值的配置到接口板]{style="font-family:宋体"}

[[Batch]{lang="EN-US"}]{#struct_0_88685_x1869_1958918555}[ ]{lang="EN-US" style="font-size:10.5pt"}[ed up the concurrent trades limit for each TCP connection configuration.]{lang="EN-US"}

[[备份]{style="font-family:宋体"}]{#struct_0_88685_x1869_1958984091}[TCP]{lang="EN-US"}[连接并发交易数上限的配置到接口板]{style="font-family:宋体"}

[[Batch]{lang="EN-US"}]{#struct_0_88685_x1869_x427273849}[ ]{lang="EN-US" style="font-size:10.5pt"}[ed up the trade timeout configuration.]{lang="EN-US"}

[[备份交易超时时间的配置到接口板]{style="font-family:宋体"}]{#struct_0_88685_x1869_1958787483}

[[Backed up the TCP connection maximum number.]{lang="EN-US"}]{#struct_0_88685_x1869_1961532945}

[[备份]{style="font-family:宋体"}]{#struct_0_88685_x1869_1273576539}[TCP]{lang="EN-US"}[终端的连接数最大值]{style="font-family:宋体"}

[[Enabled a license.]{lang="EN-US"}]{#struct_0_88685_x1869_x1566773243}

[[使能一个]{style="font-family:宋体"}]{#struct_0_88685_x1869_x1930149824}[License]{lang="EN-US"}

[[Disabled a license.]{lang="EN-US"}]{#struct_0_88685_x1869_x46103582}

[[去使能一个]{style="font-family:宋体"}]{#struct_0_88685_x1869_798733531}[License]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:
黑体"}]{#struct_0_88685_x1869_2513104}

[[\#]{lang="EN-US"}]{#struct_0_88685_x1869_x1812805774}[打开事件调试信息开关，删除]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<System\> debugging posa event]{lang="EN-US"}]{#struct_0_88685_x1869_712919590}

[\[System\]\*Aug  7 17:40:21:819 2012 System POSA/7/EVENT: -MDC=1; Recv LIPC message type:]{lang="EN-US"}

[SET, code:DELAPP, sequence:0, length:2.]{lang="EN-US"}

[\*Aug  7 17:40:21:819 2012 System POSA/7/EVENT: -MDC=1; App 2:Disable template.]{lang="EN-US"}

[\*Aug  7 17:40:21:819 2012 System POSA/7/EVENT: -MDC=1; App 2:Delete template.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_88685_x1869_719240298}*[删除应用模板]{style="font-family:宋体"}[2]{lang="EN-US"}*

::: {#349841430 .myid}
[]{#_Toc212180725}[]{#_Toc404785863}[]{#struct_0_88685_x1869_x1280879355}

**POS终端接入 \-- POS终端接入调试命令 \-- debugging posa timer**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_88685_x1869_66809178}

[**[debugging posa timer]{lang="EN-US"}**[ \[ **terminal** *terminal-id* \| **app** *app-id* \]]{lang="EN-US"}]{#struct_0_88685_x1869_x339229528}

[**[undo debugging posa timer]{lang="EN-US"}**[ \[ **terminal** *terminal-id* \| **app** *app-id* \]]{lang="EN-US"}]{#struct_0_88685_x1869_1124274732}

[[【视图】]{style="font-family:黑体"}]{#struct_0_88685_x1869_x117415501}

[[用户视图]{style="font-family:宋体"}]{#struct_0_88685_x1869_585956258}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_88685_x1869_x1401214156}

[[network-admin]{lang="EN-US"}]{#struct_0_88685_x1869_x1718365330}

[[mdc-admin]{lang="EN-US"}]{#struct_0_88685_x1869_1717157335}

[[【参数】]{style="font-family:黑体"}]{#struct_0_88685_x1869_1702525345}

[**[terminal]{lang="EN-US"}***[ terminal-id]{lang="EN-US"}*]{#struct_0_88685_x1869_x1734120887}[：终端模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[app]{lang="EN-US"}***[ app-id]{lang="EN-US"}*]{#struct_0_88685_x1869_1115200583}[：应用模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_88685_x1869_294258015}

[**[debugging posa timer]{lang="EN-US"}**]{#struct_0_88685_x1869_1802450811}[命令用来打开定时器操作调试开关。]{style="font-family:宋体"}**[undo debugging posa timer]{lang="EN-US"}**[命令用来关闭定时器调试开关。]{style="font-family:宋体"}

[[缺省情况下，定时器调试开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_88685_x1869_x1313791131}

[[表1-2 ]{lang="EN-US"}[debugging posa timer]{lang="EN-US"}]{#struct_0_88685_x1869_585890722}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1855313658}[[字段]{style="font-family:黑体"}]{#struct_0_88685_x1869_x210771257}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_88685_x1869_1793613346}

[[App *n /* Terminal *n*: Failed to create *type* timer, key=*m*.]{lang="EN-US"}]{#struct_0_88685_x1869_1402600085}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*[ / ]{lang="EN-US"}]{#struct_0_88685_x1869_x563469392}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：创建]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型定时器失败。]{style="font-family:宋体"}*[type]{lang="EN-US"}*[和]{style="font-family:宋体"}*[key]{lang="EN-US"}*[取值及对应关系如下：]{style="font-family:宋体"}

[*[type]{lang="EN-US"}*]{#struct_0_88685_x1869_x1171132145}[：]{style="font-family:宋体"}*[key]{lang="EN-US"}*

[[app connecting]{lang="EN-US"}]{#struct_0_88685_x1869_x1379808187}[：应用实例]{style="font-family:宋体"}

[[quiet]{lang="EN-US"}]{#struct_0_88685_x1869_x2078314004}[：]{style="font-family:宋体"}[AppID ]{lang="EN-US"}

[[hello period]{lang="EN-US"}]{#struct_0_88685_x1869_586087330}[：]{style="font-family:宋体"}[AppID]{lang="EN-US"}

[[hello probe]{lang="EN-US"}]{#struct_0_88685_x1869_648388401}[：]{style="font-family:宋体"}[AppID]{lang="EN-US"}

[[app flush statistics]{lang="EN-US"}]{#struct_0_88685_x1869_785263970}[：无效值]{style="font-family:宋体"}

[[terminal flush statistics]{lang="EN-US"}]{#struct_0_88685_x1869_541735586}[：无效值]{style="font-family:宋体"}

[[caller-ID flush statistics]{lang="EN-US"}]{#struct_0_88685_x1869_x1100852709}[：无效值]{style="font-family:
  宋体"}

[[caller-IP flush statistics]{lang="EN-US"}]{#struct_0_88685_x1869_x708195451}[：无效值]{style="font-family:
  宋体"}

[[terminal idle]{lang="EN-US"}]{#struct_0_88685_x1869_586021794}[：终端实例]{style="font-family:宋体"}

[[lipc connecting]{lang="EN-US"}]{#struct_0_88685_x1869_1839952707}[：无效值]{style="font-family:宋体"}

[[resend]{lang="EN-US"}]{#struct_0_88685_x1869_1597046058}[：应用实例或终端实例]{style="font-family:宋体"}

[[TTYM connect]{lang="EN-US"}]{#struct_0_88685_x1869_1280786919}[：无效值]{style="font-family:宋体"}

[[app wait AM-CID response]{lang="EN-US"}]{#struct_0_88685_x1869_x473669560}[：应用实例]{style="font-family:宋体"}

[[app auto-connect]{lang="EN-US"}]{#struct_0_88685_x1869_x1853332601}[：应用模板]{style="font-family:宋体"}

[[trade]{lang="EN-US"}]{#struct_0_88685_x1869_1959770523}[：交易号]{style="font-family:宋体"}

[[App *n /* Terminal *n*:Created *type* timer, key=*m*.]{lang="EN-US"}]{#struct_0_88685_x1869_318040400}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*[ / ]{lang="EN-US"}]{#struct_0_88685_x1869_586218402}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：创建]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型定时器]{style="font-family:宋体"}[.( *type*]{lang="EN-US"}[类型及]{style="font-family:宋体"}*[key]{lang="EN-US"}*[取值同上]{style="font-family:宋体"}[)]{lang="EN-US"}

[[App *n /* Terminal *n*: Triggered *type* timer, key=*m*.]{lang="EN-US"}]{#struct_0_88685_x1869_1716851987}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*[ / ]{lang="EN-US"}]{#struct_0_88685_x1869_x1009086583}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：触发]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型定时器]{style="font-family:宋体"}[.( *type*]{lang="EN-US"}[类型及]{style="font-family:宋体"}*[key]{lang="EN-US"}*[取值同上]{style="font-family:宋体"}[)]{lang="EN-US"}

[[App *n /* Terminal *n*: Deleted *type* timer, key=*m*.]{lang="EN-US"}]{#struct_0_88685_x1869_2021413736}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*[ / ]{lang="EN-US"}]{#struct_0_88685_x1869_1124763063}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：删除]{style="font-family:宋体"}*[ype]{lang="EN-US"}*[类型定时器]{style="font-family:宋体"}[.( *type*]{lang="EN-US"}[类型及]{style="font-family:宋体"}*[key]{lang="EN-US"}*[取值同上]{style="font-family:宋体"}[)]{lang="EN-US"}

[[App *n /* Terminal *n*: Reset *type* timer interval from *p* to *q*, key=*m*.]{lang="EN-US"}]{#struct_0_88685_x1869_x909405866}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*[ / ]{lang="EN-US"}]{#struct_0_88685_x1869_586152866}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：刷新]{style="font-family:宋体"}[t*ype*]{lang="EN-US"}[类型定时器，修改时间间隔。]{style="font-family:宋体"}[(*type*]{lang="EN-US"}[类型及]{style="font-family:宋体"}*[key]{lang="EN-US"}*[取值同上]{style="font-family:宋体"}[)]{lang="EN-US"}

[[ ]{lang="EN-US"}]{#struct_0_88685_x1869_x852713897}[【举例】]{style="font-family:黑体"}

[[\# ]{lang="EN-US"}]{#struct_0_88685_x1869_x162687772}[打开定时器调试信息开关，存在]{style="font-family:宋体"}[tcp]{lang="EN-US"}[类型的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板]{style="font-family:宋体"}[2]{lang="EN-US"}[，在应用视图下配置静默定时器时间。]{style="font-family:宋体"}

[[\<System\> debugging posa timer]{lang="EN-US"}]{#struct_0_88685_x1869_x1768205884}

[\*Aug  7 17:54:40:786 2012 System POSA/7/TIMER: -MDC=1; App 2:Trigger hello period t]{lang="EN-US"}

[imer, key:2.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_88685_x1869_x2002225653}*[静默定时器时间已更改，]{style="font-family:宋体"}[hello]{lang="EN-US"}[定时器已触发]{style="font-family:宋体"}*

::: {#1977969791 .myid}
[]{#_Toc404785864}[]{#struct_0_88685_x1869_777859108}

**POS终端接入 \-- POS终端接入调试命令 \-- debugging posa error**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_88685_x1869_x2041928102}

[**[debugging posa error]{lang="EN-US"}**[ \[ **terminal** *terminal-id* \| **app** *app-id* \]]{lang="EN-US"}]{#struct_0_88685_x1869_350987493}

[**[undo debugging posa error]{lang="EN-US"}**[ \[ **terminal** *terminal-id* \| **app** *app-id* \]]{lang="EN-US"}]{#struct_0_88685_x1869_x1626280854}

[[【视图】]{style="font-family:黑体"}]{#struct_0_88685_x1869_586349474}

[[用户视图]{style="font-family:宋体"}]{#struct_0_88685_x1869_546706876}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_88685_x1869_363699694}

[[network-admin]{lang="EN-US"}]{#struct_0_88685_x1869_479535703}

[[mdc-admin]{lang="EN-US"}]{#struct_0_88685_x1869_x1880704988}

[[【参数】]{style="font-family:黑体"}]{#struct_0_88685_x1869_1455191926}

[**[terminal]{lang="EN-US"}***[ terminal-id]{lang="EN-US"}*]{#struct_0_88685_x1869_x1092898731}[：终端模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[app]{lang="EN-US"}***[ app-id]{lang="EN-US"}*]{#struct_0_88685_x1869_1943503128}[：应用模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_88685_x1869_x544682346}

[**[debugging posa error]{lang="EN-US"}**]{#struct_0_88685_x1869_x300275619}[命令用来打开]{style="font-family:宋体"}[POS]{lang="EN-US"}[接入错误调试开关。]{style="font-family:宋体"}**[undo debugging posa error]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[POS]{lang="EN-US"}[接入错误调试开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_88685_x1869_586283938}[接入错误调试开关处于关闭状态。]{style="font-family:宋体"}

[]{#struct_0_88685_x1869_170463515}[[表1-3 ]{lang="EN-US"}[debugging posa error]{lang="EN-US"}]{#_Ref203361573}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1861670450}[[字段]{style="font-family:黑体"}]{#struct_0_88685_x1869_x1854313813}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_88685_x1869_x1410001592}

[[App *n*:Failed to trigger hello issue, A previous issue exist.]{lang="EN-US"}]{#struct_0_88685_x1869_x435903412}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_708728724}[：]{style="font-family:宋体"}[Hello]{lang="EN-US"}[已存在]{style="font-family:宋体"}

[[Maximum number of maps has been reached.]{lang="EN-US"}]{#struct_0_88685_x1869_x1504920705}

[[Map]{lang="EN-US"}]{#struct_0_88685_x1869_585825187}[表项已达到最大值]{style="font-family:宋体"}

[[Failed to match map.]{lang="EN-US"}]{#struct_0_88685_x1869_887857069}

[[匹配]{style="font-family:宋体"}[map]{lang="EN-US"}]{#struct_0_88685_x1869_653741634}[表失败]{style="font-family:宋体"}

[[Failed to set data(CMD:*n*) to kernel.]{lang="EN-US"}]{#struct_0_88685_x1869_1974144375}

[[向内核设置数据失败]{style="font-family:宋体"}]{#struct_0_88685_x1869_712968023}

[[App *n /* Terminal *n*:]{lang="EN-US"}]{#struct_0_88685_x1869_1509759285}[ ]{lang="EN-US" style="font-size:10.5pt"}[AM-CID response packet total length was wrong.]{lang="EN-US"}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_319700227}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：应答]{style="font-family:宋体"}[AM-CID]{lang="EN-US"}[报文总长度错误]{style="font-family:宋体"}

[[App *n /* Terminal *n*:]{lang="EN-US"}]{#struct_0_88685_x1869_585759651}[ ]{lang="EN-US" style="font-size:
  10.5pt"}[AM-CID response packet data length was wrong.]{lang="EN-US"}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_2513105}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：应答]{style="font-family:宋体"}[AM-CID]{lang="EN-US"}[报文数据长度错误]{style="font-family:宋体"}

[[App *n /* Terminal *n*: AM-CID response packet data length was wrong.]{lang="EN-US"}]{#struct_0_88685_x1869_x246721833}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_754157071}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：应答]{style="font-family:宋体"}[AM-CID]{lang="EN-US"}[报文数据代码错误]{style="font-family:宋体"}

[[App *n /* Terminal *n*: AM-CID response packet caller number length was wrong.]{lang="EN-US"}]{#struct_0_88685_x1869_760293835}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_x1920290777}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：应答]{style="font-family:宋体"}[AM-CID]{lang="EN-US"}[报文数据主叫号码长度错误]{style="font-family:宋体"}

[[App *n /* Terminal *n*: AM-CID response packet caller number was wrong.]{lang="EN-US"}]{#struct_0_88685_x1869_585956259}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_x1401214155}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：应答]{style="font-family:宋体"}[AM-CID]{lang="EN-US"}[报文数据主叫号码错误]{style="font-family:宋体"}

[[App *n /* Terminal *n*: AM-CID response packet CRC was wrong.]{lang="EN-US"}]{#struct_0_88685_x1869_x2121649857}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_x21420960}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：应答]{style="font-family:宋体"}[AM-CID]{lang="EN-US"}[报文数据]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验错误]{style="font-family:宋体"}

[[App *n /* Terminal *n*: Maximum number of instances has been reached.]{lang="EN-US"}]{#struct_0_88685_x1869_x842137032}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_585890723}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：实例数达到最大值]{style="font-family:宋体"}

[[Terminal *n*: Maximum number of TCP connections has been reached.]{lang="EN-US"}]{#struct_0_88685_x1869_1558313954}

[[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_x7769987}[：]{style="font-family:宋体"}[TCP]{lang="EN-US"}[终端的连接数达到最大值]{style="font-family:宋体"}

[[Terminal *n*: Failed to accept socket error code=*m*.]{lang="EN-US"}]{#struct_0_88685_x1869_x210771256}

[[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_1793547810}[：]{style="font-family:宋体"}[accept   socket]{lang="EN-US"}[连接失败，错误码是]{style="font-family:宋体"}*[m]{lang="EN-US"}*

[[Terminal *n*: Failed to listen socket error code=*m*]{lang="EN-US"}]{#struct_0_88685_x1869_622447779}

[[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_x448159419}[：监听]{style="font-family:宋体"}[socket]{lang="EN-US"}[连接失败，错误码是]{style="font-family:宋体"}*[m]{lang="EN-US"}*

[[App n / Terminal n: Failed to set socket option.]{lang="EN-US"}]{#struct_0_88685_x1869_586087331}

[[应用]{style="font-family:宋体"}[n / ]{lang="EN-US"}]{#struct_0_88685_x1869_648388400}[终端]{style="font-family:宋体"}[n]{lang="EN-US"}[：设置]{style="font-family:宋体"}[socket]{lang="EN-US"}[选项失败]{style="font-family:宋体"}

[[App *n*: Failed to get app instance for terminal.]{lang="EN-US"}]{#struct_0_88685_x1869_785263969}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_x1796916583}[：为终端获取应用实例失败]{style="font-family:宋体"}

[[App *n /* Terminal *n*: Failed to bind socket, error code=*m*.]{lang="EN-US"}]{#struct_0_88685_x1869_263361673}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_586021795}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：绑定]{style="font-family:宋体"}[socket]{lang="EN-US"}[失败，错误码是]{style="font-family:宋体"}*[m]{lang="EN-US"}*

[[App *n*: Failed to connect to app, error code=*m*.]{lang="EN-US"}]{#struct_0_88685_x1869_1839952706}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_1596980522}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：连接到]{style="font-family:宋体"}[app]{lang="EN-US"}[失败，错误码是]{style="font-family:宋体"}*[m]{lang="EN-US"}*

[[App *n /* Terminal *n*: Failed to send packet, error code=*m*]{lang="EN-US"}]{#struct_0_88685_x1869_x1889511545}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_586218403}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：发送报文失败，错误码是]{style="font-family:宋体"}*[m]{lang="EN-US"}*

[[App *n /* Terminal *n*: Received incompleted packet received length=*a*,]{lang="EN-US"}]{#struct_0_88685_x1869_1716851988}[ ]{lang="EN-US" style="font-size:10.5pt"}[expected length=*b*.]{lang="EN-US"}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_x1009152119}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：接受了长度为]{style="font-family:宋体"}*[a]{lang="EN-US"}*[不完整的报文，实际长度应为]{style="font-family:宋体"}*[b]{lang="EN-US"}*

[[Terminal *n*: Failed to send to peer for *m* times.]{lang="EN-US"}]{#struct_0_88685_x1869_102088035}

[*[m]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_88685_x1869_1108095707}[次重传失败]{style="font-size:9.0pt;font-family:宋体"}

[[App *n*: Failed to distribute app packet.]{lang="EN-US"}]{#struct_0_88685_x1869_586152867}

[[分发]{style="font-family:宋体"}[app]{lang="EN-US"}]{#struct_0_88685_x1869_x852713896}[报文失败]{style="font-family:宋体"}

[[App *n /* Terminal *n*: Invalid packet length(*m*).]{lang="EN-US"}]{#struct_0_88685_x1869_x162753308}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_968785720}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：报文长度]{style="font-family:宋体"}[(*m*)]{lang="EN-US"}[错误]{style="font-family:宋体"}

[[App *n /* Terminal *n*: NO-HEAD-FCM packet checking failed. Invalid packet length (*m*).]{lang="EN-US"}]{#struct_0_88685_x1869_586349475}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_546706875}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：检查无头]{style="font-family:宋体"}[FCM]{lang="EN-US"}[报文时报文长度]{style="font-family:宋体"}[(*m*)]{lang="EN-US"}[错误]{style="font-family:宋体"}

[[App *n /* Terminal *n*: FCM packet checking failed. Invalid packet length (*m*).]{lang="EN-US"}]{#struct_0_88685_x1869_363699691}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_586283939}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：检查]{style="font-family:宋体"}[FCM]{lang="EN-US"}[报文时报文长度]{style="font-family:宋体"}[(*m*)]{lang="EN-US"}[错误]{style="font-family:宋体"}

[[App *n /* Terminal *n*: Flow packet checking failed. Invalid STX*(m)*.]{lang="EN-US"}]{#struct_0_88685_x1869_170463514}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_x1854313814}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：检查异步报文时其特定域]{style="font-family:宋体"}[STX*(m)*]{lang="EN-US"}[错误]{style="font-family:宋体"}

[[App *n /* Terminal *n*: Flow packet checking failed. Invalid TPDU-ID*(m)*.]{lang="EN-US"}]{#struct_0_88685_x1869_156082349}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_585825184}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：检查异步报文时其]{style="font-family:宋体"}[TPDU ID*(m)*]{lang="EN-US"}[错误]{style="font-family:宋体"}

[[App *n /* Terminal *n*: Flow packet checking failed. Invalid ETX(*m*).]{lang="EN-US"}]{#struct_0_88685_x1869_887857072}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_x1302573491}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：检查异步报文时其特定域]{style="font-family:宋体"}[ETX*(m)*]{lang="EN-US"}[错误]{style="font-family:宋体"}

[[App *n /* Terminal *n*: Flow packet checking failed. Invalid CRC(*p)*, should be *q*.]{lang="EN-US"}]{#struct_0_88685_x1869_x362918030}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_585759648}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：检查异步报文时其特定域]{style="font-family:宋体"}[CRC*(p)*]{lang="EN-US"}[错误，正确的]{style="font-family:宋体"}[CRC]{lang="EN-US"}[是]{style="font-family:宋体"}[(*q)*]{lang="EN-US"}

[[Failed to get private data for interface *ifname*.]{lang="EN-US"}]{#struct_0_88685_x1869_x1953802040}

[[获取接口（]{style="font-family:宋体"}*[ifname]{lang="EN-US"}*]{#struct_0_88685_x1869_1109957136}[）私有数据块失败]{style="font-family:宋体"}

[[App *n /* Terminal *n*: Failed to set non-block mode, error code=*m*.]{lang="EN-US"}]{#struct_0_88685_x1869_x1326874477}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_585956256}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：设置连接为非阻塞失败，错误码为]{style="font-family:宋体"}*[m]{lang="EN-US"}*

[[TTYM was lost.]{lang="EN-US"}]{#struct_0_88685_x1869_x1401214146}

[[断开与]{style="font-family:宋体"}[TTYM]{lang="EN-US"}]{#struct_0_88685_x1869_x1718430866}[连接]{style="font-family:宋体"}

[[Terminal *n*: Failed to enable nontcp terminal because instance has already existed]{lang="EN-US"}]{#struct_0_88685_x1869_585890720}

[[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_x210771255}[：由于实例已经存在，导致使能非]{style="font-family:宋体"}[tcp]{lang="EN-US"}[类型终端失败]{style="font-family:宋体"}

[[App *n /* Terminal *n*: Failed to register interface *ifname* to TTYM.]{lang="EN-US"}]{#struct_0_88685_x1869_1793482274}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_x2096533775}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：向]{style="font-family:宋体"}[ttym]{lang="EN-US"}[注册接口]{style="font-family:宋体"}[(*ifname*)]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[App *n /* Terminal *n*: Failed to unregister interface *ifname* toTTYM ]{lang="EN-US"}]{#struct_0_88685_x1869_586087328}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_x1690263767}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：撤销向]{style="font-family:宋体"}[ttym]{lang="EN-US"}[注册接口]{style="font-family:宋体"}[(*ifname*)]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[App *n /* Terminal *n*: Failed to put TTY device for interface *ifname*.]{lang="EN-US"}]{#struct_0_88685_x1869_600963799}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_586021792}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：接口]{style="font-family:宋体"}[(*ifname)*]{lang="EN-US"}[放弃]{style="font-family:宋体"}[tty]{lang="EN-US"}[设备控制权失败]{style="font-family:宋体"}

[[App *n /* Terminal *n*: Failed to read data from interface or socket.]{lang="EN-US"}]{#struct_0_88685_x1869_1839952709}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_1597177130}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：从接口或]{style="font-family:宋体"}[socket]{lang="EN-US"}[中读取数据失败]{style="font-family:宋体"}

[[Failed to connect to TTYM]{lang="EN-US"}]{#struct_0_88685_x1869_586218400}

[[连接到]{style="font-family:宋体"}[TTYM]{lang="EN-US"}]{#struct_0_88685_x1869_1716851989}[失败]{style="font-family:宋体"}

[[App *n /* Terminal *n*:Failed to get TTY device for interface *ifname*.]{lang="EN-US"}]{#struct_0_88685_x1869_x1009217655}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_586152864}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：接口]{style="font-family:宋体"}[(*ifname)*]{lang="EN-US"}[获取]{style="font-family:宋体"}[tty]{lang="EN-US"}[设备控制权失败]{style="font-family:宋体"}

[[App *n /* Terminal *n*: Failed to open device *s* error code=*m*.]{lang="EN-US"}]{#struct_0_88685_x1869_x852713895}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_x162818844}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：打开设备]{style="font-family:宋体"}[(*s*)]{lang="EN-US"}[失败，错误码为]{style="font-family:宋体"}*[m]{lang="EN-US"}*

[[App *n*: Failed to create more instance. Source port is set.]{lang="EN-US"}]{#struct_0_88685_x1869_586349472}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_546706874}[：由于配置了源端口的模板只允许一个实例，导致创建其他实例失败]{style="font-family:宋体"}

[[Failed to add fd:*n* to epoll.]{lang="EN-US"}]{#struct_0_88685_x1869_363699692}

[[添加]{style="font-family:宋体"}[fd(*n*)]{lang="EN-US"}]{#struct_0_88685_x1869_586283936}[到]{style="font-family:宋体"}[epoll]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[App *n /* Terminal *n*: Failed to get *s* attribute, error code=*m*.]{lang="EN-US"}]{#struct_0_88685_x1869_170463521}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_x280335697}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：获取]{style="font-family:宋体"}[tty]{lang="EN-US"}[设备]{style="font-family:宋体"}[(*s)*]{lang="EN-US"}[失败，错误码为]{style="font-family:宋体"}*[m]{lang="EN-US"}*

[[App *n /* Terminal *n*: Failed to set *s* attribute, error code=*m*.]{lang="EN-US"}]{#struct_0_88685_x1869_585825185}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_887857071}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：设置]{style="font-family:宋体"}[tty]{lang="EN-US"}[设备]{style="font-family:宋体"}[(*s)*]{lang="EN-US"}[失败，错误码为]{style="font-family:宋体"}*[m]{lang="EN-US"}*

[[App *n /* Terminal *n*: Failed to get instance for tty event.]{lang="EN-US"}]{#struct_0_88685_x1869_x1302573494}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_585759649}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：处理]{style="font-family:宋体"}[tty]{lang="EN-US"}[事件获取实例失败]{style="font-family:宋体"}

[[App *n /* Terminal *n*: Failed to get fd for tty event.]{lang="EN-US"}]{#struct_0_88685_x1869_x1953802039}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_585956257}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：处理]{style="font-family:宋体"}[tty]{lang="EN-US"}[事件获取句柄失败]{style="font-family:宋体"}

[[App *n /* Terminal *n*: Failed to recevie data due to buffer overflow.]{lang="EN-US"}]{#struct_0_88685_x1869_x1401214145}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_x2121715393}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：由于接受缓冲满，无法读取新的报文]{style="font-family:宋体"}

[[App *n /* Terminal *n*: Failed to send data due to buffer overflow.]{lang="EN-US"}]{#struct_0_88685_x1869_585890721}

[[应用]{style="font-family:宋体"}*[n / ]{lang="EN-US"}*]{#struct_0_88685_x1869_x210771254}[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[：由于发送缓存满，无法发送新的报文]{style="font-family:宋体"}

[[Failed to send Lipc message.]{lang="EN-US"}]{#struct_0_88685_x1869_1278769745}

[[发送]{style="font-family:宋体"}[LIPC]{lang="EN-US"}]{#struct_0_88685_x1869_x287314196}[消息失败]{style="font-family:宋体"}

[[Recevied invalid Lipc message.]{lang="EN-US"}]{#struct_0_88685_x1869_x856549634}

[[收到无效的]{style="font-family:宋体"}[LIPC]{lang="EN-US"}]{#struct_0_88685_x1869_x1853398137}[消息]{style="font-family:宋体"}

[[App *n* : Socket (fd: *n*) received epoll event,event=*a*, error code=*b*.]{lang="EN-US"}]{#struct_0_88685_x1869_x1401421156}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_875485218}[：]{style="font-family:宋体"}[socket *n* ]{lang="EN-US"}[接收到]{style="font-family:宋体"}[epoll]{lang="EN-US"}[事件]{style="font-family:宋体"}*[a]{lang="EN-US"}*[，错误码为]{style="font-family:宋体"}*[b]{lang="EN-US"}*

[[App *n*: Instance *m* keep was down.]{lang="EN-US"}]{#struct_0_88685_x1869_x690598723}

[[应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_x592346833}[：实例]{style="font-family:宋体"}*[m]{lang="EN-US"}*[报文保活失败]{style="font-family:宋体"}

[[Terminal *n*: Number of concurrent trades for instance *m* exceeded the limit *o*.]{lang="EN-US"}]{#struct_0_88685_x1869_1958853026}

[[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_1959704994}[：实例]{style="font-family:宋体"}*[m]{lang="EN-US"}*[的并发交易数超过上限值]{style="font-family:宋体"}*[o]{lang="EN-US"}*

[[Failed to allocate trade resources.]{lang="EN-US"}]{#struct_0_88685_x1869_x469675459}

[[分配交易资源失败]{style="font-family:宋体"}]{#struct_0_88685_x1869_1959770530}

[[Terminal *n*: Instance *m* failed to get a trade number due to trade resource allocation error.]{lang="EN-US"}]{#struct_0_88685_x1869_x438557517}

[[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_1959180705}[：实例]{style="font-family:宋体"}*[m]{lang="EN-US"}*[获取交易号失败，原因是交易资源申请失败]{style="font-family:宋体"}

[[Terminal *n*: Instance *m* failed to get a trade number because no idle trade number was left.]{lang="EN-US"}]{#struct_0_88685_x1869_x38394638}

[[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_1959246241}[：实例]{style="font-family:宋体"}*[m]{lang="EN-US"}*[获取交易号失败，原因是无空闲交易号]{style="font-family:宋体"}

[[Terminal *n*: Instance *m* failed to create timer for trade *o*.]{lang="EN-US"}]{#struct_0_88685_x1869_x447583819}

[[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_1959049633}[：实例]{style="font-family:宋体"}*[m]{lang="EN-US"}*[为交易]{style="font-family:宋体"}*[o]{lang="EN-US"}*[创建定时器失败]{style="font-family:宋体"}

[[Trade number *o* has already been released.]{lang="EN-US"}]{#struct_0_88685_x1869_x96643761}

[[交易号]{style="font-family:宋体"}*[o]{lang="EN-US"}*]{#struct_0_88685_x1869_1959115169}[已经被释放]{style="font-family:宋体"}

[[Terminal *n*: FCM packet checking failed. Invalid TPDU-ID*(m)*.]{lang="EN-US"}]{#struct_0_88685_x1869_x430711315}

[[终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_88685_x1869_1958918561}[：检查]{style="font-family:宋体"}[FCM]{lang="EN-US"}[报文时其]{style="font-family:宋体"}[TPDU ID*(m)*]{lang="EN-US"}[错误]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_88685_x1869_1793416738}

[[\# ]{lang="EN-US"}]{#struct_0_88685_x1869_x1367785119}[打开错误调试信息开关，在没有配置匹配的]{style="font-family:宋体"}[map]{lang="EN-US"}[表情况下，发起一次交易。]{style="font-family:宋体"}

[[\<System\> debugging posa error]{lang="EN-US"}]{#struct_0_88685_x1869_x1759750952}

[\*Aug  7 18:09:38:603 2012 System POSA/7/ERROR: -MDC=1; Failed to match map.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_88685_x1869_586087329}*[显示匹配]{style="font-family:宋体"}[map]{lang="EN-US"}[表失败]{style="font-family:宋体"}*

::: {#-1125272813 .myid}
[]{#_Toc404785865}[]{#struct_0_88685_x1869_x1690263768}[]{#_Toc212180726}[]{#_Toc200170329}[]{#_Toc194748104}[]{#_Toc193529372}

**POS终端接入 \-- POS终端接入调试命令 \-- debugging posa packet**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_88685_x1869_197679272}

[**[debugging posa packet]{lang="EN-US"}**[ \[ **receive** \| **send** \] \[ **terminal** *terminal-id* \| **app** *app-id* \]]{lang="EN-US"}]{#struct_0_88685_x1869_1372331486}

[**[undo debugging posa packet]{lang="EN-US"}**[ \[ **receive** \| **send** \] \[ **terminal** *terminal-id* \| **app** *app-id* \]]{lang="EN-US"}]{#struct_0_88685_x1869_617398407}

[[【视图】]{style="font-family:黑体"}]{#struct_0_88685_x1869_x1236276586}

[[用户视图]{style="font-family:宋体"}]{#struct_0_88685_x1869_x1519906639}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_88685_x1869_965776572}

[[network-admin]{lang="EN-US"}]{#struct_0_88685_x1869_1412627406}

[[mdc-admin]{lang="EN-US"}]{#struct_0_88685_x1869_x1594394242}

[[【参数】]{style="font-family:黑体"}]{#struct_0_88685_x1869_x515409649}

[**[receive]{lang="EN-US"}**]{#struct_0_88685_x1869_586021793}[：表示接收报文的调试信息开关。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_88685_x1869_1839952708}[：表示发送报文的调试信息开关。]{style="font-family:宋体"}

[**[terminal]{lang="EN-US"}***[ terminal-id]{lang="EN-US"}*]{#struct_0_88685_x1869_1597111594}[：终端]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[app]{lang="EN-US"}***[ app-id]{lang="EN-US"}*]{#struct_0_88685_x1869_x1434000407}[：应用]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_88685_x1869_x725810422}

[**[debugging posa packet]{lang="EN-US"}**]{#struct_0_88685_x1869_611975645}[命令用来打开]{style="font-family:宋体"}[POS]{lang="EN-US"}[接入报文调试开关，可以使用]{style="font-family:宋体"}**[receive]{lang="EN-US"}**[、]{style="font-family:宋体"}**[send]{lang="EN-US"}**[参数来控制打开特定方向的报文调试开关；使用]{style="font-family:宋体"}**[terminal]{lang="EN-US"}**[、]{style="font-family:宋体"}**[app]{lang="EN-US"}**[参数来控制打开某个终端模板或应用模板的报文调试开关。]{style="font-family:宋体"}

[**[undo debugging posa packet]{lang="EN-US"}**]{#struct_0_88685_x1869_x1176645686}[命令用来关闭]{style="font-family:
宋体"}[POS]{lang="EN-US"}[接入报文调试开关，可以使用]{style="font-family:宋体"}**[receive]{lang="EN-US"}**[、]{style="font-family:宋体"}**[send]{lang="EN-US"}**[、]{style="font-family:宋体"}**[terminal]{lang="EN-US"}**[、]{style="font-family:宋体"}**[app]{lang="EN-US"}**[参数来控制关闭某个终端或应用模板特定方向的报文调试开关。]{style="font-family:宋体"}

[[POS]{lang="EN-US"}]{#struct_0_88685_x1869_239609135}[报文特定域：]{style="font-family:宋体"}[STX ]{lang="EN-US"}[、]{style="font-family:宋体"}[PktLen(]{lang="EN-US"}[报文包长]{style="font-family:宋体"}[)]{lang="EN-US"}[、]{style="font-family:宋体"}[ID]{lang="EN-US"}[（传输协议数据单元]{style="font-family:宋体"}[ID]{lang="EN-US"}[，即]{style="font-family:宋体"}[TPDU  ID]{lang="EN-US"}[）、]{style="font-family:宋体"}[DST]{lang="EN-US"}[（]{style="font-family:宋体"}[TPDU ]{lang="EN-US"}[目的地址）、]{style="font-family:宋体"}[SRC]{lang="EN-US"}[（]{style="font-family:宋体"}[TPDU ]{lang="EN-US"}[源地址）、]{style="font-family:宋体"}[EXT]{lang="EN-US"}[、]{style="font-family:宋体"}[CRC]{lang="EN-US"}[（校验和）。]{style="font-family:宋体"}

[[当接收到的报文不完整时，无报文数据的域显示为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_88685_x1869_x561916010}[。当本次收到的报文数据大于]{style="font-family:宋体"}[32]{lang="EN-US"}[字节时，只显示前]{style="font-family:宋体"}[32]{lang="EN-US"}[字节的报文内容。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_88685_x1869_x1916609207}[接入报文调试开关处于关闭状态。]{style="font-family:宋体"}

[]{#struct_0_88685_x1869_586218401}[[表1-4 ]{lang="EN-US"}[debugging posa packet]{lang="EN-US"}]{#_Ref203361581}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1839479482}[[字段]{style="font-family:黑体"}]{#struct_0_88685_x1869_1716851990}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_88685_x1869_x1008627830}

[[Received *m* bytes from flow terminal *n*.]{lang="EN-US"}]{#struct_0_88685_x1869_566660905}

[[STX PktLen(a) ID(b) DST(c) SRC(d) ETX CRC(e)]{lang="EN-US"}]{#struct_0_88685_x1869_1352209237}

[[Total length:x offset:y]{lang="EN-US"}[, partial data as follows:]{lang="EN-US"}]{#struct_0_88685_x1869_x1880730227}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[从]{style="font-family:宋体"}]{#struct_0_88685_x1869_132610307}[flow]{lang="EN-US"}[类型的终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[收到]{style="font-family:宋体"}*[m]{lang="EN-US"}*[字节]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STX PktLen*(a)* ID(*b*) DST(*c*) SRC(*d*) ETX *CRC*(*e*)]{lang="EN-US"}]{#struct_0_88685_x1869_586152865}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[报文长度：]{style="font-family:宋体"}]{#struct_0_88685_x1869_x852713894}*[x]{lang="EN-US"}*[ ]{lang="EN-US"}[偏移量：]{style="font-family:宋体"}*[y]{lang="EN-US"}*[，部分报文内容如下：]{style="font-family:宋体"}

[[Received *m* bytes from tcp terminal *n*.]{lang="EN-US"}]{#struct_0_88685_x1869_x162884380}

[[PktLen(a) ID(b) DST(c) SRC(d)]{lang="EN-US"}]{#struct_0_88685_x1869_x600116164}

[[Total length:x, offset: y]{lang="EN-US"}[, partial data as follows:]{lang="EN-US"}]{#struct_0_88685_x1869_x1769481710}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[从]{style="font-family:宋体"}]{#struct_0_88685_x1869_1975847027}[tcp]{lang="EN-US"}[类型的终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[收到]{style="font-family:宋体"}*[m]{lang="EN-US"}*[字节]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PktLen(*a*) ID(*b*) DST(*c*) SRC(*d*)]{lang="EN-US"}]{#struct_0_88685_x1869_586349473}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[报文长度：]{style="font-family:宋体"}]{#struct_0_88685_x1869_546706873}*[x]{lang="EN-US"}*[ ]{lang="EN-US"}[偏移量：]{style="font-family:宋体"}*[y]{lang="EN-US"}*[，部分报文内容如下：]{style="font-family:宋体"}

[[Received *m* bytes from ]{lang="EN-US"}[fcm ]{lang="EN-US"}]{#struct_0_88685_x1869_363699697}[terminal *n*.]{lang="EN-US"}

[[ID(a) DST(b) SRC(c)]{lang="EN-US"}]{#struct_0_88685_x1869_479535700}

[[Total length:x, offset: y]{lang="EN-US"}[, partial data as follows:]{lang="EN-US"}]{#struct_0_88685_x1869_x1880704987}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[从]{style="font-family:宋体"}]{#struct_0_88685_x1869_x2080260483}[fcm]{lang="EN-US"}[类型的终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[收到]{style="font-family:宋体"}*[m]{lang="EN-US"}*[字节]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ID(*a*) DST(*b*) SRC(*c*)]{lang="EN-US"}]{#struct_0_88685_x1869_586283937}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[报文长度：]{style="font-family:宋体"}]{#struct_0_88685_x1869_170463520}*[x]{lang="EN-US"}*[ ]{lang="EN-US"}[偏移量：]{style="font-family:宋体"}*[y]{lang="EN-US"}*[，部分报文内容如下：]{style="font-family:宋体"}

[[Received *m* bytes from ]{lang="EN-US"}[fcm ]{lang="EN-US"}]{#struct_0_88685_x1869_x280335698}[terminal *n*.]{lang="EN-US"}

[[No head]{lang="EN-US"}]{#struct_0_88685_x1869_1480297369}

[[Total length:x, offset: y]{lang="EN-US"}[, partial data as follows:]{lang="EN-US"}]{#struct_0_88685_x1869_x1037380217}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[从]{style="font-family:宋体"}]{#struct_0_88685_x1869_x759856961}[fcm]{lang="EN-US"}[类型的终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[收到]{style="font-family:宋体"}*[m]{lang="EN-US"}*[字节]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[无头报文]{lang="EN-US" style="font-family:宋体"}]{#struct_0_88685_x1869_x2143058167}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[报文长度：]{style="font-family:宋体"}]{#struct_0_88685_x1869_223161478}*[x]{lang="EN-US"}*[ ]{lang="EN-US"}[偏移量：]{style="font-family:宋体"}*[y]{lang="EN-US"}*[，部分报文内容如下：]{style="font-family:宋体"}

[[Received *m* bytes from ]{lang="EN-US"}[flow ]{lang="EN-US"}]{#struct_0_88685_x1869_364852840}[terminal *n*.]{lang="EN-US"}

[[Transparent packet]{lang="EN-US"}]{#struct_0_88685_x1869_x544153456}

[[Total length:x, offset: y]{lang="EN-US"}[, partial data as follows:]{lang="EN-US"}]{#struct_0_88685_x1869_x2143123703}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[从]{style="font-family:宋体"}]{#struct_0_88685_x1869_271643823}[flow]{lang="EN-US"}[类型的终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[收到]{style="font-family:宋体"}*[m]{lang="EN-US"}*[字节]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[透传报文]{lang="EN-US" style="font-family:宋体"}]{#struct_0_88685_x1869_1652792828}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[报文长度：]{style="font-family:宋体"}]{#struct_0_88685_x1869_1618492279}*[x]{lang="EN-US"}*[ ]{lang="EN-US"}[偏移量：]{style="font-family:宋体"}*[y]{lang="EN-US"}*[，部分报文内容如下：]{style="font-family:宋体"}

[[Received *m* bytes from ]{lang="EN-US"}[fcm ]{lang="EN-US"}]{#struct_0_88685_x1869_168893289}[terminal *n*.]{lang="EN-US"}

[[Transparent packet]{lang="EN-US"}]{#struct_0_88685_x1869_x2142927095}

[[Total length:x, offset: y]{lang="EN-US"}[, partial data as follows:]{lang="EN-US"}]{#struct_0_88685_x1869_525940933}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[从]{style="font-family:宋体"}]{#struct_0_88685_x1869_x2095561521}[fcm]{lang="EN-US"}[类型的终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*[收到]{style="font-family:宋体"}*[m]{lang="EN-US"}*[字节]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[透传报文]{lang="EN-US" style="font-family:宋体"}]{#struct_0_88685_x1869_197605844}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[报文长度：]{style="font-family:宋体"}]{#struct_0_88685_x1869_1401327667}*[x]{lang="EN-US"}*[ ]{lang="EN-US"}[偏移量：]{style="font-family:宋体"}*[y]{lang="EN-US"}*[，部分报文内容如下：]{style="font-family:宋体"}

[[Received *m* bytes from flow application *n*.]{lang="EN-US"}]{#struct_0_88685_x1869_x2142992631}

[[STX PktLen(a) ID(b) DST(c) SRC(d) ETX CRC(e)]{lang="EN-US"}]{#struct_0_88685_x1869_x358051704}

[[Total length:x, offset: y]{lang="EN-US"}]{#struct_0_88685_x1869_x291930870}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[从]{style="font-family:宋体"}]{#struct_0_88685_x1869_x1868028283}[flow]{lang="EN-US"}[类型的应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*[收到]{style="font-family:宋体"}*[m]{lang="EN-US"}*[字节]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STX PktLen(*a*) ID(*b*) DST(*c*) SRC(*d*) ETX CRC(*e*)]{lang="EN-US"}]{#struct_0_88685_x1869_x2142796023}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[报文长度：]{style="font-family:宋体"}]{#struct_0_88685_x1869_282360260}*[x ]{lang="EN-US"}*[偏移量：]{style="font-family:宋体"}*[y]{lang="EN-US"}*[ ]{lang="EN-US"}[，部分报文内容如下：]{style="font-family:宋体"}

[[Received *m* bytes from tcp application *n*.]{lang="EN-US"}]{#struct_0_88685_x1869_x2027220777}

[[PktLen(a) ID(b) DST(c) SRC(d)]{lang="EN-US"}]{#struct_0_88685_x1869_x1346501798}

[[Total length:x, offset: y]{lang="EN-US"}[, partial data as follows:]{lang="EN-US"}]{#struct_0_88685_x1869_x2142861559}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[从]{style="font-family:宋体"}]{#struct_0_88685_x1869_x2094889408}[tcp]{lang="EN-US"}[类型的应用]{style="font-family:宋体"}[n]{lang="EN-US"}[收到]{style="font-family:宋体"}[m]{lang="EN-US"}[字节]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PktLen(*a*) ID(*b*) DST(*c*) SRC(*d*)]{lang="EN-US"}]{#struct_0_88685_x1869_645675415}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[报文长度：]{style="font-family:宋体"}]{#struct_0_88685_x1869_732443668}*[x ]{lang="EN-US"}*[偏移量：]{style="font-family:宋体"}*[y]{lang="EN-US"}*[，部分报文内容如下：]{style="font-family:宋体"}

[[Received *m* bytes from tcp application *n*.]{lang="EN-US"}]{#struct_0_88685_x1869_x2142664951}

[[Transparent packet]{lang="EN-US"}]{#struct_0_88685_x1869_x2127877356}

[[Total length:x, offset: y]{lang="EN-US"}[, partial data as follows:]{lang="EN-US"}]{#struct_0_88685_x1869_x648996243}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[从]{style="font-family:宋体"}]{#struct_0_88685_x1869_270030348}[tcp]{lang="EN-US"}[类型的应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*[收到]{style="font-family:宋体"}*[m]{lang="EN-US"}*[字节]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[透传报文]{lang="EN-US" style="font-family:宋体"}]{#struct_0_88685_x1869_x2142730487}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[报文长度：]{style="font-family:宋体"}]{#struct_0_88685_x1869_1961110002}*[x ]{lang="EN-US"}*[偏移量：]{style="font-family:宋体"}*[y]{lang="EN-US"}*[，部分报文内容如下：]{style="font-family:宋体"}

[[Sent *m* bytes to flow terminal *n*.]{lang="EN-US"}]{#struct_0_88685_x1869_x320580691}

[[STX PktLen(a) ID(b) DST(c) SRC(d) ETX CRC(e)]{lang="EN-US"}]{#struct_0_88685_x1869_x2142533879}

[[Total length:x, offset: y]{lang="EN-US"}[, partial data as follows:]{lang="EN-US"}]{#struct_0_88685_x1869_1284302224}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[发送]{style="font-family:宋体"}]{#struct_0_88685_x1869_856723041}*[m]{lang="EN-US"}*[字节到]{style="font-family:宋体"}[flow]{lang="EN-US"}[类型的终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STX PktLen(]{lang="EN-US"}*[a]{lang="EN-US"}*]{#struct_0_88685_x1869_x1065980523}[) ID(]{lang="EN-US"}*[b]{lang="EN-US"}*[) DST(*c*) SRC(*d*) ETX CRC(*e*)]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[报文长度：]{style="font-family:宋体"}]{#struct_0_88685_x1869_x2142599415}*[x ]{lang="EN-US"}*[偏移量：]{style="font-family:宋体"}*[y]{lang="EN-US"}*[，部分报文内容如下：]{style="font-family:宋体"}

[[Sent *m* bytes to tcp terminal *n*.]{lang="EN-US"}]{#struct_0_88685_x1869_x2005418466}

[[PktLen(a) ID(b) DST(c) SRC(d)]{lang="EN-US"}]{#struct_0_88685_x1869_x31321711}

[[Total length:x, offset: y]{lang="EN-US"}[, partial data as follows:]{lang="EN-US"}]{#struct_0_88685_x1869_x2143058166}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[发送]{style="font-family:宋体"}]{#struct_0_88685_x1869_x1342922463}*[m]{lang="EN-US"}*[字节到]{style="font-family:宋体"}[tcp]{lang="EN-US"}[类型的终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PktLen(*a*) ID(*b*) DST(*c*) SRC(*d*)]{lang="EN-US"}]{#struct_0_88685_x1869_995184793}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[报文长度：]{style="font-family:宋体"}]{#struct_0_88685_x1869_x237300891}*[x]{lang="EN-US"}*[ ]{lang="EN-US"}[偏移量：]{style="font-family:宋体"}*[y]{lang="EN-US"}*[，部分报文内容如下：]{style="font-family:宋体"}

[[Sent *m* bytes to ]{lang="EN-US"}[fcm ]{lang="EN-US"}]{#struct_0_88685_x1869_x2143123702}[terminal *n*.]{lang="EN-US"}

[[ID(a) DST(b) SRC(c)]{lang="EN-US"}]{#struct_0_88685_x1869_1837727764}

[[Total length:x, offset: y]{lang="EN-US"}[, partial data as follows:]{lang="EN-US"}]{#struct_0_88685_x1869_x527452433}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[发送]{style="font-family:宋体"}]{#struct_0_88685_x1869_x2142927094}*[m]{lang="EN-US"}*[字节到]{style="font-family:宋体"}[fcm]{lang="EN-US"}[类型的终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ID(*a*) DST(*b*) SRC(*c*)]{lang="EN-US"}]{#struct_0_88685_x1869_2092024874}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[报文长度：]{style="font-family:宋体"}]{#struct_0_88685_x1869_77733535}*[x ]{lang="EN-US"}*[偏移量：]{style="font-family:宋体"}*[y]{lang="EN-US"}*[，部分报文内容如下：]{style="font-family:宋体"}

[[Sent *m* bytes to ]{lang="EN-US"}[fcm ]{lang="EN-US"}]{#struct_0_88685_x1869_x2142992630}[terminal *n*.]{lang="EN-US"}

[[No head]{lang="EN-US"}]{#struct_0_88685_x1869_x1924135645}

[[Total length:x, offset: y]{lang="EN-US"}[, partial data as follows:]{lang="EN-US"}]{#struct_0_88685_x1869_177554684}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[发送]{style="font-family:宋体"}]{#struct_0_88685_x1869_x2142796022}*[m]{lang="EN-US"}*[字节到]{style="font-family:宋体"}[fcm]{lang="EN-US"}[类型的终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[无头报文]{lang="EN-US" style="font-family:宋体"}]{#struct_0_88685_x1869_x1283723681}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[报文长度：]{style="font-family:宋体"}]{#struct_0_88685_x1869_x698005431}*[x ]{lang="EN-US"}*[偏移量：]{style="font-family:宋体"}*[y]{lang="EN-US"}*[，部分报文内容如下：]{style="font-family:宋体"}

[[Sent *m* bytes to ]{lang="EN-US"}[flow ]{lang="EN-US"}]{#struct_0_88685_x1869_x2142861558}[terminal *n*.]{lang="EN-US"}

[[Transparent packet]{lang="EN-US"}]{#struct_0_88685_x1869_x528805467}

[[Total length:x, offset: y]{lang="EN-US"}[, partial data as follows:]{lang="EN-US"}]{#struct_0_88685_x1869_x283335672}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[发送]{style="font-family:宋体"}]{#struct_0_88685_x1869_x2142664950}*[m]{lang="EN-US"}*[字节到]{style="font-family:宋体"}[flow]{lang="EN-US"}[类型的终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[透传报文]{lang="EN-US" style="font-family:宋体"}]{#struct_0_88685_x1869_x561793415}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[报文长度：]{style="font-family:宋体"}]{#struct_0_88685_x1869_x2142730486}*[x ]{lang="EN-US"}*[偏移量：]{style="font-family:宋体"}*[y]{lang="EN-US"}*[，部分报文内容如下：]{style="font-family:宋体"}

[[Sent *m* bytes to ]{lang="EN-US"}[fcm ]{lang="EN-US"}]{#struct_0_88685_x1869_395026061}[terminal *n*.]{lang="EN-US"}

[[Transparent packet]{lang="EN-US"}]{#struct_0_88685_x1869_x668656564}

[[Total length:x, offset: y]{lang="EN-US"}[, partial data as follows:]{lang="EN-US"}]{#struct_0_88685_x1869_x2142533878}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[发送]{style="font-family:宋体"}]{#struct_0_88685_x1869_x281781717}*[m]{lang="EN-US"}*[字节到]{style="font-family:宋体"}[fcm]{lang="EN-US"}[类型的终端]{style="font-family:宋体"}*[n]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[透传报文]{lang="EN-US" style="font-family:宋体"}]{#struct_0_88685_x1869_x1654015575}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[报文长度：]{style="font-family:宋体"}]{#struct_0_88685_x1869_x2142599414}*[x ]{lang="EN-US"}*[偏移量：]{style="font-family:宋体"}*[y]{lang="EN-US"}*[，部分报文内容如下：]{style="font-family:宋体"}

[[Sent *m* bytes to flow application *n*.]{lang="EN-US"}]{#struct_0_88685_x1869_723464889}

[[STX PktLen(a) ID(b) DST(c) SRC(d) ETX CRC(e)]{lang="EN-US"}]{#struct_0_88685_x1869_x315908290}

[[Total length:x, offset: y]{lang="EN-US"}[, partial data as follows:]{lang="EN-US"}]{#struct_0_88685_x1869_x2143058169}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[发送]{style="font-family:宋体"}]{#struct_0_88685_x1869_673500172}*[m]{lang="EN-US"}*[字节到]{style="font-family:宋体"}[flow]{lang="EN-US"}[类型的应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STX PktLen(]{lang="EN-US"}*[a]{lang="EN-US"}*]{#struct_0_88685_x1869_1529053944}[) ID(]{lang="EN-US"}*[b]{lang="EN-US"}*[) DST(]{lang="EN-US"}*[c]{lang="EN-US"}*[) SRC(]{lang="EN-US"}*[d]{lang="EN-US"}*[) ETX CRC(]{lang="EN-US"}*[e]{lang="EN-US"}*[)]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[报文长度：]{style="font-family:宋体"}]{#struct_0_88685_x1869_x2143123705}*[x ]{lang="EN-US"}*[偏移量：]{style="font-family:宋体"}*[y]{lang="EN-US"}*[，部分报文内容如下：]{style="font-family:宋体"}

[[Sent *m* bytes to tcp application *n*.]{lang="EN-US"}]{#struct_0_88685_x1869_1078212877}

[[PktLen(a) ID(b) DST(c) SRC(d)]{lang="EN-US"}]{#struct_0_88685_x1869_x2142927097}

[[Total length:x, offset: y]{lang="EN-US"}[, partial data as follows:]{lang="EN-US"}]{#struct_0_88685_x1869_1688740347}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[发送]{style="font-family:宋体"}]{#struct_0_88685_x1869_652310284}*[m]{lang="EN-US"}*[字节到]{style="font-family:宋体"}[tcp]{lang="EN-US"}[类型的应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PktLen(]{lang="EN-US"}*[a]{lang="EN-US"}*]{#struct_0_88685_x1869_x2142992633}[) ID(]{lang="EN-US"}*[b]{lang="EN-US"}*[) DST(]{lang="EN-US"}*[c]{lang="EN-US"}*[) SRC(]{lang="EN-US"}*[d]{lang="EN-US"}*[)]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[报文长度：]{style="font-family:宋体"}]{#struct_0_88685_x1869_804747710}[x ]{lang="EN-US"}[偏移量：]{style="font-family:宋体"}[y]{lang="EN-US"}[，部分报文内容如下：]{style="font-family:宋体"}

[[Sent *m* bytes to tcp application *n*.]{lang="EN-US"}]{#struct_0_88685_x1869_x2142796025}

[[Transparent packet]{lang="EN-US"}]{#struct_0_88685_x1869_1088929314}

[[Total length:x, offset: y]{lang="EN-US"}[, partial data as follows:]{lang="EN-US"}]{#struct_0_88685_x1869_x854833649}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[发送]{style="font-family:宋体"}]{#struct_0_88685_x1869_x2142861561}*[m]{lang="EN-US"}*[字节到]{style="font-family:宋体"}[tcp]{lang="EN-US"}[类型的应用]{style="font-family:宋体"}*[n]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[透传报文]{lang="EN-US" style="font-family:宋体"}]{#struct_0_88685_x1869_x1738462440}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[报文长度：]{style="font-family:宋体"}]{#struct_0_88685_x1869_x2142664953}*[x ]{lang="EN-US"}*[偏移量：]{style="font-family:宋体"}*[y]{lang="EN-US"}*[，部分报文内容如下：]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_88685_x1869_x965077942}

[[\# ]{lang="EN-US"}]{#struct_0_88685_x1869_x1733209959}[打开接受报文调试开关，发送一次完整报文。]{style="font-family:宋体"}

[[\<System\>debugging posa packet receive]{lang="EN-US"}]{#struct_0_88685_x1869_1450746555}

[\[System\]\*Aug  7 18:15:58:136 2012 System POSA/7/PKTRECEIVE: -MDC=1; Received 9 bytes f]{lang="EN-US"}

[rom tcp terminal 1.]{lang="EN-US"}

[PktLen(0x0007) ID(0x60) DST(0x1111) SRC(0x2222)]{lang="EN-US"}

[Total length: 9 Offset: 0, partial data as follows:]{lang="EN-US"}

[0x000:  00 07 60 11 11 22 22 aa bb]{lang="EN-US"}

[*[// ]{lang="PT-BR"}*]{#struct_0_88685_x1869_x1997182701}*[收到]{style="font-family:宋体"}[9]{lang="EN-US"}[字节的报文]{style="font-family:宋体"}[，]{style="font-family:宋体"}[报文的]{style="font-family:宋体"}[TPDU ID]{lang="PT-BR"}[为]{style="font-family:宋体"}[0x60]{lang="PT-BR"}[，]{style="font-family:宋体"}[目的地址为]{style="font-family:宋体"}[0x2222]{lang="PT-BR"}[，]{style="font-family:宋体"}[源地址为]{style="font-family:宋体"}[0x1111]{lang="PT-BR"}[，报文长度为]{style="font-family:宋体"}[9]{lang="PT-BR"}[字节，偏移量为]{style="font-family:宋体"}[0]{lang="PT-BR"}*
