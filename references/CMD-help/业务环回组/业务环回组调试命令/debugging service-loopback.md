::: {#1865991273 .myid}
[]{#_Toc174448765}[]{#_Toc404784736}[]{#struct_0_13719_95673_x694961537}

**业务环回组 \-- 业务环回组调试命令 \-- debugging service-loopback**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_13719_95673_x487411217}

[**[debugging service-loopback]{lang="EN-US"}**[ { **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_13719_95673_1360640388}

[**[undo debugging service-loopback]{lang="EN-US"}**[ { **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_13719_95673_219501458}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13719_95673_873864848}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13719_95673_819385169}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13719_95673_1794244252}

[[network-admin]{lang="EN-US"}]{#struct_0_13719_95673_2111736239}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13719_95673_x1419714116}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13719_95673_x1630809002}

[**[all]{lang="EN-US"}**]{#struct_0_13719_95673_2107760795}[：表示业务环回组的所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_13719_95673_1637422913}[：表示业务环回组错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_13719_95673_1992949197}[：表示业务环回组事件调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_13719_95673_x1182122468}

[**[debugging service-loopback]{lang="EN-US"}**]{#struct_0_13719_95673_x397264022}[命令用来打开业务环回组调试信息开关。]{style="font-family:
宋体"}**[undo debugging service-loopback]{lang="EN-US"}**[命令用来关闭业务环回组调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，业务环回组调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_13719_95673_x1712588819}

[[表1-1 ]{lang="EN-US"}[debugging service-loopback error]{lang="EN-US"}]{#struct_0_13719_95673_2111801775}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_89794169}[[字段]{style="font-family:黑体"}]{#struct_0_13719_95673_178160392}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13719_95673_x150273390}

[[Failed to get group information when processing update-group message.]{lang="EN-US"}]{#struct_0_13719_95673_x1961978867}

[[非主用主控板处理主用主控板发来的组数据时读取组信息失败]{style="font-family:宋体"}]{#struct_0_13719_95673_93394942}

[[Failed to send the information of group *GroupID*.]{lang="EN-US"}]{#struct_0_13719_95673_304624598}

[[发送组]{style="font-family:宋体"}*[GroupID]{lang="EN-US"}*]{#struct_0_13719_95673_894033225}[的信息失败]{style="font-family:宋体"}

[[Failed to send the information of the debug switch status.]{lang="EN-US"}]{#struct_0_13719_95673_1930720397}

[[发送调试开关信息失败]{style="font-family:宋体"}]{#struct_0_13719_95673_x617671401}

[[Failed to set driver.]{lang="EN-US"}]{#struct_0_13719_95673_x1564910013}

[[设置内核驱动失败]{style="font-family:宋体"}]{#struct_0_13719_95673_1954210655}

[[Failed to switch over member port type.]{lang="EN-US"}]{#struct_0_13719_95673_1399661910}

[[业务环回组切换成员端口类型失败]{style="font-family:宋体"}]{#struct_0_13719_95673_1611785167}

[[Failed to send sync group data.]{lang="EN-US"}]{#struct_0_13719_95673_x1651416434}

[[发送同步组数据失败]{style="font-family:宋体"}]{#struct_0_13719_95673_x617605865}

[[Failed to create group *GroupID*, which arealdy exists.]{lang="EN-US"}]{#struct_0_13719_95673_x1251594063}

[[创建业务环回组]{style="font-family:宋体"}*[GroupID]{lang="EN-US"}*]{#struct_0_13719_95673_254832943}[失败，因为该组已存在]{style="font-family:宋体"}

[[Failed to mofidy group *GroupID*, which does not exist.]{lang="EN-US"}]{#struct_0_13719_95673_2117685287}

[[修改业务环回组]{style="font-family:宋体"}*[GroupID]{lang="EN-US"}*]{#struct_0_13719_95673_1333352111}[失败，因为该组不存在]{style="font-family:宋体"}

[[Failed to mofidy group *GroupID*, the type of which is invalid.]{lang="EN-US"}]{#struct_0_13719_95673_x617802473}

[[修改业务环回组]{style="font-family:宋体"}*[GroupID]{lang="EN-US"}*]{#struct_0_13719_95673_x9770519}[失败，因为组类型非法]{style="font-family:宋体"}

[[Failed to delete group *GroupID*, which does not exist.]{lang="EN-US"}]{#struct_0_13719_95673_1861725987}

[[删除业务环回组]{style="font-family:宋体"}*[GroupID]{lang="EN-US"}*]{#struct_0_13719_95673_1069521514}[失败，因为该组已不存在]{style="font-family:宋体"}

[[No group can process set-intftype result.]{lang="EN-US"}]{#struct_0_13719_95673_414500805}

[[没有任何组能够处理切换接口类型结果]{style="font-family:宋体"}]{#struct_0_13719_95673_352768936}

[[Failed to switch over interface type when deleting the group.]{lang="EN-US"}]{#struct_0_13719_95673_x617736937}

[[删除业务环回组时切换接口类型失败]{style="font-family:宋体"}]{#struct_0_13719_95673_x2021082126}

[[No group can process set-loopback result.]{lang="EN-US"}]{#struct_0_13719_95673_1668084915}

[[没有任何组能处理设置接口自环结果]{style="font-family:宋体"}]{#struct_0_13719_95673_1455498808}

[[Can't process set-loopback result because of invliad interface indexes.]{lang="EN-US"}]{#struct_0_13719_95673_x617409257}

[[由于接口索引非法而不能处理设置接口自环结果]{style="font-family:宋体"}]{#struct_0_13719_95673_x837549346}

[[No group can process interface-up]{lang="EN-US"}]{#struct_0_13719_95673_1753354933}

[[没有任何组能够处理接口]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_13719_95673_x1304079676}[事件]{style="font-family:宋体"}

[[Can't process interface-up because of invalid group operation flag.]{lang="EN-US"}]{#struct_0_13719_95673_2021251971}

[[由于无效组操作标记而不能处理接口]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_13719_95673_x617343721}[事件]{style="font-family:宋体"}

[[Can't process interface-up for non-operation members.]{lang="EN-US"}]{#struct_0_13719_95673_x1156156280}

[[不能处理非操作成员的接口]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_13719_95673_346184378}[事件]{style="font-family:宋体"}

[[No group can process expiration of wait-up timer.]{lang="EN-US"}]{#struct_0_13719_95673_282306475}

[[没有组能处理等待接口]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_13719_95673_x617540329}[事件定时器超时]{style="font-family:宋体"}

[[Can't process expiration of wait-up timer because of invalid group operation flag.]{lang="EN-US"}]{#struct_0_13719_95673_x795291009}

[[由于无效组操作标记而不能处理等待接口]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_13719_95673_1275769063}[事件定时器超时]{style="font-family:宋体"}

[[Can't process the response message from the slot because the group does not exsit.]{lang="EN-US"}]{#struct_0_13719_95673_x2001265863}

[[由于环回组不存在而不能处理接口板回应消息]{style="font-family:宋体"}]{#struct_0_13719_95673_x617474793}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging service-loopback event]{lang="EN-US"}]{#struct_0_13719_95673_768714001}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_87333759}[[字段]{style="font-family:黑体"}]{#struct_0_13719_95673_x1121559093}

[[描述]{style="font-family:黑体"}]{#struct_0_13719_95673_1729845751}

[[Processing *usMsgType* message succeeded.]{lang="EN-US"}]{#struct_0_13719_95673_x1606626037}

[[处理]{style="font-family:宋体"}*[usMsgType]{lang="EN-US"}*]{#struct_0_13719_95673_x1641186020}[消息成功]{style="font-family:宋体"}

[[Setting driver succeeded.]{lang="EN-US"}]{#struct_0_13719_95673_x1212446118}

[[设置内核驱动成功]{style="font-family:宋体"}]{#struct_0_13719_95673_x617147113}

[[Synchronized group *GroupID* to other slots.]{lang="EN-US"}]{#struct_0_13719_95673_x1978382669}

[[同步业务环回组]{style="font-family:宋体"}*[GroupID]{lang="EN-US"}*]{#struct_0_13719_95673_664111960}[的数据到其它接口板]{style="font-family:宋体"}

[[Processed group *GroupID* set-intftype result.]{lang="EN-US"}]{#struct_0_13719_95673_1947484002}

[[处理业务环回组]{style="font-family:宋体"}*[GroupID]{lang="EN-US"}*]{#struct_0_13719_95673_x1545506586}[切换接口类型结果]{style="font-family:宋体"}

[[Processed port *IFIndex* set-loopback result.]{lang="EN-US"}]{#struct_0_13719_95673_x379343434}

[[处理接口]{style="font-family:宋体"}*[IFIndex]{lang="EN-US"}*]{#struct_0_13719_95673_x577931588}[的自环结果]{style="font-family:宋体"}

[[Processed port *IFIndex* up.]{lang="EN-US"}]{#struct_0_13719_95673_x617081577}

[[处理接口]{style="font-family:宋体"}*[IFIndex]{lang="EN-US"}*]{#struct_0_13719_95673_356605212}[的]{style="font-family:宋体"}[up]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[Processed the wait-up timer expiration of group *GroupID*.]{lang="EN-US"}]{#struct_0_13719_95673_x1874512771}

[[处理业务环回组]{style="font-family:宋体"}*[GroupID]{lang="EN-US"}*]{#struct_0_13719_95673_388169339}[等待接口]{style="font-family:宋体"}[up]{lang="EN-US"}[事件定时器超时]{style="font-family:宋体"}

[[Received a response from slot *SlotID*.]{lang="EN-US"}]{#struct_0_13719_95673_x1374356850}

[[收到接口板]{style="font-family:宋体"}*[SlotID]{lang="EN-US"}*]{#struct_0_13719_95673_x1687738016}[的回应]{style="font-family:宋体"}

[[Received responses from all slots.]{lang="EN-US"}]{#struct_0_13719_95673_x617671400}

[[收到所有接口板回应]{style="font-family:宋体"}]{#struct_0_13719_95673_x1564975549}

[[Processed group *GroupID* sync data.]{lang="EN-US"}]{#struct_0_13719_95673_x643874418}

[[处理业务环回组]{style="font-family:宋体"}*[GroupID]{lang="EN-US"}*]{#struct_0_13719_95673_x2037039258}[同步数据]{style="font-family:宋体"}

[[Completed upgrading backup daemon.]{lang="EN-US"}]{#struct_0_13719_95673_292774485}

[[备用守护进程升级完成]{style="font-family:宋体"}]{#struct_0_13719_95673_x617605864}

[[Received a change type result *ResultType.*]{lang="EN-US"}]{#struct_0_13719_95673_x1251528527}

[[接收切换接口类型结果]{style="font-family:宋体"}]{#struct_0_13719_95673_x1707176155}

[[Received *EventType* interface-event of port *IFIndex*.]{lang="EN-US"}]{#struct_0_13719_95673_x1367282548}

[[接收到接口]{style="font-family:宋体"}*[IFIndex]{lang="EN-US"}*]{#struct_0_13719_95673_1385613679}[的接口事件]{style="font-family:宋体"}*[EventType]{lang="EN-US"}*

[[Adding interface *IFIndex* node to the setLB list succeeded.]{lang="EN-US"}]{#struct_0_13719_95673_x617802472}

[[成功添加接口]{style="font-family:宋体"}*[IFIndex]{lang="EN-US"}*]{#struct_0_13719_95673_x9704983}[节点到设置自环状态并设置自环链表]{style="font-family:宋体"}

[[Processing interface *IFIndex* in setLB list succeeded.]{lang="EN-US"}]{#struct_0_13719_95673_1118469866}

[[从设置接口自环链表中成功处理接口]{style="font-family:宋体"}*[IFIndex]{lang="EN-US"}*]{#struct_0_13719_95673_1102918876}

[[Adding interface *IFIndex* node to pending list succeeded.]{lang="EN-US"}]{#struct_0_13719_95673_x617736936}

[[成功添加接口]{style="font-family:宋体"}*[IFIndex]{lang="EN-US"}*]{#struct_0_13719_95673_x2021147662}[节点到待处理接口事件链表]{style="font-family:宋体"}

[[Processing interface *IFIndex* in pending list succeeded.]{lang="EN-US"}]{#struct_0_13719_95673_663004972}

[[从待处理接口事件链表中成功处理接口]{style="font-family:宋体"}*[IFIndex]{lang="EN-US"}*]{#struct_0_13719_95673_x1127536688}

[[Completed processing pending list interface node *IFIndex.*]{lang="EN-US"}]{#struct_0_13719_95673_x465216778}

[[完成处理待处理接口链表的节点接口]{style="font-family:宋体"}*[IFIndex]{lang="EN-US"}*]{#struct_0_13719_95673_x617409256}

[[Creating thread succeeded.]{lang="EN-US"}]{#struct_0_13719_95673_x837483810}

[[创建线程成功]{style="font-family:宋体"}]{#struct_0_13719_95673_x1755424979}

[[Switch over a dissociating loopback interface *IFIndex*.]{lang="EN-US"}]{#struct_0_13719_95673_1227636312}

[[切换游离口]{style="font-family:宋体"}*[IFIndex]{lang="EN-US"}*]{#struct_0_13719_95673_x617343720}[的接口类型成功]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13719_95673_x1156090744}

[[\# ]{lang="EN-US"}]{#struct_0_13719_95673_x1733580739}[打开业务环回组错误调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging service-loopback error]{lang="EN-US"}]{#struct_0_13719_95673_2068425873}

[\*Nov  3 19:29:12:860 2010 Sysname SLBG/7/Error:]{lang="EN-US"}

[Failed to create wait response timer.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13719_95673_x2001367339}*[创建等待回应定时器失败]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_13719_95673_1997987394}[打开业务环回组事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging service-loopback event]{lang="EN-US"}]{#struct_0_13719_95673_916245546}

[\*Nov  3 19:29:12:860 2010 Sysname SLBG/7/Event:]{lang="EN-US"}

[Received responses from all slots.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13719_95673_x617540328}*[主控板收到其它所有板的回应消息]{style="font-family:宋体"}*
