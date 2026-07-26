::: {#-1929069742 .myid}
[]{#_Toc404797052}[]{#struct_0_x1862_90986_x883353933}

**Event MIB \-- Event MIB配置命令 \-- action**

------------------------------------------------------------------------

[**[action]{lang="EN-US"}**]{#struct_0_x1862_90986_x550627658}[命令用来配置事件包含的动作。]{style="font-family:宋体"}

[**[undo action]{lang="EN-US"}**]{#struct_0_x1862_90986_928039570}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x496051036}

[**[action ]{lang="EN-US"}**[{]{lang="EN-US"}**[ notification ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ set ]{lang="EN-US"}**[}]{lang="EN-US"}]{#struct_0_x1862_90986_1108193447}

[**[undo ]{lang="EN-US"}[action ]{lang="EN-US"}**[{]{lang="EN-US"}**[ notification ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ set ]{lang="EN-US"}**[}]{lang="EN-US"}]{#struct_0_x1862_90986_1424273204}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1360752141}

[[该事件没有包含任何动作。]{style="font-family:宋体"}]{#struct_0_x1862_90986_x141517554}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x109852115}

[[Event]{lang="EN-US"}]{#struct_0_x1862_90986_x2086598481}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1915322887}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x324133878}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_1707433633}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_812363469}

[**[notificaton]{lang="EN-US"}**]{#struct_0_x1862_90986_x1930003772}[：指定事件包含告警动作，当对应的事件被触发时，则向网管发送指定的告警信息。]{style="font-family:宋体"}

[**[set]{lang="EN-US"}**]{#struct_0_x1862_90986_1953119161}[：指定事件包含设置动作，当对应的事件被触发时，可以对指定的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[节点的值进行设置。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1116951857}

[[当对应事件被触发后，可以配置的执行动作类型包括]{style="font-family:宋体"}[Set]{lang="EN-US"}]{#struct_0_x1862_90986_x2116711599}[和]{style="font-family:宋体"}[Notification]{lang="EN-US"}[。同一个事件可以配置两种动作。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果动作指定为]{style="font-family:宋体"}]{#struct_0_x1862_90986_614987381}[Set]{lang="EN-US"}[类型，则系统自动生成对应的]{style="font-family:宋体"}[Set]{lang="EN-US"}[表，同时进入]{style="font-family:宋体"}[Action-set]{lang="EN-US"}[视图，进行]{style="font-family:宋体"}[Set]{lang="EN-US"}[表的相关配置。具体配置请参见]{style="font-family:宋体"}[Action-set]{lang="EN-US"}[视图下的配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果动作指定为]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1862_90986_x343625025}[N]{lang="EN-US"}[otification]{lang="EN-US"}[类型，则自动生成相对应]{lang="EN-US" style="font-family:宋体"}[N]{lang="EN-US"}[otification]{lang="EN-US"}[表，同时进入]{lang="EN-US" style="font-family:宋体"}[N]{lang="EN-US"}[otification]{lang="EN-US"}[视图，进行]{lang="EN-US" style="font-family:宋体"}[N]{lang="EN-US"}[otification]{lang="EN-US"}[表的相关配置。具体配置请参见]{lang="EN-US" style="font-family:宋体"}[A]{lang="EN-US"}[ction-notification]{lang="EN-US"}[视图下的配置。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x12078147}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_906196501}[配置用户事件的动作类型为]{style="font-family:宋体"}[Set]{lang="EN-US"}[和]{style="font-family:宋体"}[Notification]{lang="EN-US"}[，设置节点名]{style="font-family:宋体"}[ipForwarding.0]{lang="EN-US"}[的值为]{style="font-family:宋体"}[2]{lang="EN-US"}[，告警类型为]{style="font-family:宋体"}[mteEventSetFailure]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1862_90986_134986181}

[\[Sysname\] snmp mib event owner owner1 name EventA]{lang="EN-US"}

[\[Sysname-event-owner1-EventA\] action notification]{lang="EN-US"}

[\[Sysname-event-owner1-EventA-notification\]]{lang="EN-US"}[ oid ]{lang="EN-US"}[mteEventSetFailure]{lang="EN-US"}[ ]{lang="EN-US"}

[\[Sysname-event-owner1-EventA-notification\] quit]{lang="EN-US"}

[\[Sysname-event-owner1-EventA\] action set]{lang="EN-US"}

[\[Sysname-event-owner1-EventA-set\] ]{lang="EN-US"}[oid ]{lang="EN-US"}[ipForwarding.0]{lang="EN-US"}

[\[Sysname-event-owner1-EventA-set\] value 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_687257448}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event ]{lang="EN-US"}**]{#struct_0_x1862_90986_x2066945759}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[event enable]{lang="EN-US"}**]{#struct_0_x1862_90986_x20053216}
:::

::: {#193474836 .myid}
[]{#_Toc404797053}[]{#struct_0_x1862_90986_490997775}

**Event MIB \-- Event MIB配置命令 \-- comparison**

------------------------------------------------------------------------

[**[comparison]{lang="EN-US"}**]{#struct_0_x1862_90986_x1201968278}[命令用来指定]{style="font-family:宋体"}[Trigger-boolean]{lang="EN-US"}[视图下的检测子类型，表示采样值与参考值之间的比较方式。]{style="font-family:宋体"}

[**[undo comparison]{lang="EN-US"}**]{#struct_0_x1862_90986_578568614}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1528647789}

[**[comparison]{lang="EN-US"}**[ { **equal** \| **greater** \| **greaterOrEqual** \| **less** \| **lessOrEqual** \| **unequal** }]{lang="EN-US"}]{#struct_0_x1862_90986_612171756}

[**[undo comparison]{lang="EN-US"}**]{#struct_0_x1862_90986_x1796104009}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x473717931}

[[采样值与参考值的比较方式为]{style="font-family:宋体"}[unequal]{lang="EN-US"}]{#struct_0_x1862_90986_1862355372}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1445815563}

[[Trigger-boolean]{lang="EN-US"}]{#struct_0_x1862_90986_x2047773179}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_811707691}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x1815017499}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x2125935074}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1700431946}

[**[equal]{lang="EN-US"}**]{#struct_0_x1862_90986_x1950509060}[：采样值与参考值的比较方式为]{style="font-family:宋体"}[equal]{lang="EN-US"}[，即当采样值等于参考值时，满足检测条件。]{style="font-family:宋体"}

[**[greater]{lang="EN-US"}**]{#struct_0_x1862_90986_x1710319219}[：采样值与参考值的比较方式为]{style="font-family:宋体"}[greater]{lang="EN-US"}[，即当采样值大于参考值时，满足检测条件。]{style="font-family:宋体"}

[**[greaterOrEqual]{lang="EN-US"}**]{#struct_0_x1862_90986_x1269049408}[：采样值与参考值的比较方式为]{style="font-family:宋体"}[greaterOrEqual]{lang="EN-US"}[，即当采样值大于等于参考值时，满足检测条件。]{style="font-family:宋体"}

[**[less]{lang="EN-US"}**]{#struct_0_x1862_90986_x75323599}[：采样值与参考值的比较方式为]{style="font-family:宋体"}[less]{lang="EN-US"}[，即当采样值小于参考值时，满足检测条件。]{style="font-family:宋体"}

[**[lessOrEqual]{lang="EN-US"}**]{#struct_0_x1862_90986_265464536}[：采样值与参考值的比较方式为]{style="font-family:宋体"}[lessOrEqual]{lang="EN-US"}[，即当采样值小于等于参考值时，满足检测条件。]{style="font-family:宋体"}

[**[unequal]{lang="EN-US"}**]{#struct_0_x1862_90986_1503515088}[：采样值与参考值的比较方式为]{style="font-family:宋体"}[unequal]{lang="EN-US"}[，即当采样值不等于参考值时，满足检测条件。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x953912185}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[被监控的节点为非首次采样，本次采样值满足条件且上次采样值不满足条件则触发指定事件，也就是说如果连续两次采样均满足条件，只在第一次触发指定事件。]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1862_90986_x1967912512}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[被监控节点为首次采样，只有配置了]{lang="EN-US" style="font-family:宋体"}**[startup enable]{lang="EN-US"}**]{#struct_0_x1862_90986_1671135904}[命令后才会触发指定事件。]{lang="EN-US" style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_293573304}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_520650010}[配置采样值与参考值的比较方式为]{style="font-family:宋体"}[Unequal]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1862_90986_x1844309173}

[\[Sysname\] snmp mib event trigger owner owner1 name triggerA]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA\] test boolean]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA-boolean\] comparison unequal]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_2146537941}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event trigger]{lang="EN-US"}**]{#struct_0_x1862_90986_x468848523}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[test]{lang="EN-US"}**]{#struct_0_x1862_90986_949714162}
:::

::: {#-2123566612 .myid}
[]{#_Toc404797054}[]{#struct_0_x1862_90986_744227321}

**Event MIB \-- Event MIB配置命令 \-- context (Trigger view)**

------------------------------------------------------------------------

[**[context]{lang="EN-US"}**]{#struct_0_x1862_90986_823965042}[命令用来配置监控对象所在的]{style="font-family:宋体;color:black"}[SNMP]{lang="EN-US" style="color:black"}[上下文环境。]{style="font-family:宋体;color:black"}

[**[undo context]{lang="EN-US"}**]{#struct_0_x1862_90986_1744580196}[命令用来恢复缺省情况。]{style="font-family:宋体;color:black"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1143292729}

[**[context ]{lang="EN-US"}***[context-name]{lang="EN-US" style="color:black"}*]{#struct_0_x1862_90986_884562656}

[**[undo context]{lang="EN-US"}**]{#struct_0_x1862_90986_x63659647}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1774971170}

[[没有配置监控对象所在的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x1862_90986_x598360247}[上下文环境。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x445504033}

[[Trigger]{lang="EN-US"}]{#struct_0_x1862_90986_1893154498}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x641455373}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_1994175363}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_1391638113}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1038726034}

[*[context-name]{lang="EN-US" style="color:black"}*]{#struct_0_x1862_90986_710749063}[：指定监控对象所在的]{style="font-family:宋体;color:black"}[SNMP]{lang="EN-US" style="color:black"}[上下文，]{style="font-family:宋体;color:black"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写[。]{style="color:black"}]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x337507971}

[[配置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x1862_90986_1305052326}[上下文用于确定唯一的监控对象的节点实例。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1599879862}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_x841335241}[配置监控对象所在的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[上下文为]{style="font-family:宋体"}[contextname1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1862_90986_957068064}

[\[Sysname\] snmp mib event trigger owner owner1 name triggerA]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA\] context contextname1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1751166360}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event trigger]{lang="EN-US"}**]{#struct_0_x1862_90986_208887229}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[wildcard ]{lang="EN-US"}[context]{lang="EN-US"}**]{#struct_0_x1862_90986_1851097276}
:::

::: {#-536916579 .myid}
[]{#_Toc404797055}[]{#struct_0_x1862_90986_x43125543}

**Event MIB \-- Event MIB配置命令 \-- context (Action-set view)**

------------------------------------------------------------------------

[**[context]{lang="EN-US"}**]{#struct_0_x1862_90986_x541811993}[命令用来配置]{style="font-family:宋体"}[Set]{lang="EN-US"}[对象所处的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[上下文。]{style="font-family:宋体"}

[**[undo context]{lang="EN-US"}**]{#struct_0_x1862_90986_x1966766475}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1385859810}

[**[context ]{lang="EN-US"}**[context-name]{lang="EN-US"}]{#struct_0_x1862_90986_308982950}

[**[undo context]{lang="EN-US"}**]{#struct_0_x1862_90986_x838910645}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1232200436}

[[没有配置]{style="font-family:宋体"}[Set]{lang="EN-US"}]{#struct_0_x1862_90986_x163048102}[对象所处的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[上下文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1040874376}

[[Action-set]{lang="EN-US"}]{#struct_0_x1862_90986_x1494781849}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1834097092}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x525871768}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_1539864180}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x2069657432}

[*[context-name]{lang="EN-US" style="border:none windowtext 1.0pt;
padding:0cm"}*]{#struct_0_x1862_90986_x1100121856}[：指定]{style="font-family:宋体"}[Set]{lang="EN-US"}[对象所处的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[上下文，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写[。]{style="color:black"}]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1320440554}

[[配置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x1862_90986_1745273507}[上下文用于确定唯一的]{style="font-family:宋体"}[Set]{lang="EN-US"}[对象的节点实例。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x453849220}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_x1786174644}[配置]{style="font-family:宋体"}[Set]{lang="EN-US"}[对象所处的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[上下文为]{style="font-family:宋体"}[contextname1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\>system-view]{lang="EN-US"}]{#struct_0_x1862_90986_96166215}

[\[Sysname\] snmp mib event owner owner1 name EventA]{lang="EN-US"}

[\[Sysname-event-owner1-EventA\] action set]{lang="EN-US"}

[\[Sysname-event-owner1-EventA-set\] context contextname1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1520992691}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event owner]{lang="EN-US"}**]{#struct_0_x1862_90986_x1328866315}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[action]{lang="EN-US"}**]{#struct_0_x1862_90986_156256418}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[wildcard context]{lang="EN-US"}**]{#struct_0_x1862_90986_x1240783460}
:::

::: {#2040712116 .myid}
[]{#_Toc404797056}[]{#struct_0_x1862_90986_x1620644807}[]{#_Toc366652168}

**Event MIB \-- Event MIB配置命令 \-- delta falling**

------------------------------------------------------------------------

[**[delta falling]{lang="EN-US"}**]{#struct_0_x1862_90986_24689016}[命令用来配置差值采样类型的下限阈值，并指定采样值小于等于该阈值时对应的触发事件。]{style="font-family:宋体"}

[**[undo delta falling]{lang="EN-US"}**]{#struct_0_x1862_90986_1179760704}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x837864282}

[**[delta]{lang="EN-US"}**[ ]{lang="EN-US"}**[falling]{lang="EN-US"}**[ ]{lang="EN-US"}[{ **event** **owner** *event-owner* **name** *event-name* \| **value** *integer-value* }]{lang="EN-US"}]{#struct_0_x1862_90986_659225923}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[delta]{lang="EN-US"}**[ ]{lang="EN-US"}**[falling]{lang="EN-US"}**[ { **event** \| **value** }]{lang="EN-US"}]{#struct_0_x1862_90986_385818995}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x688436046}

[[下限阈值为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x1862_90986_x147509725}[，且没有指定对应的触发事件。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x132765024}

[[Trigger-threshold]{lang="EN-US"}]{#struct_0_x1862_90986_x229401679}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x734104072}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x1951723616}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_369664188}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x564864055}

[**[event]{lang="EN-US"}**[ ]{lang="EN-US"}**[owner]{lang="EN-US"}***[ event-owner]{lang="EN-US"}*]{#struct_0_x1862_90986_986248240}[：配置差值采样类型下限阈值对应事件的所有者，与]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[表中配置的]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[所有者]{style="font-family:宋体"}[owner]{lang="EN-US"}[相同。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}***[ event-name]{lang="EN-US"}*]{#struct_0_x1862_90986_x210609626}[：配置差值采样类型下限阈值对应的事件名，为]{style="font-family:宋体"}[1\~32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[value]{lang="EN-US"}**[ ]{lang="EN-US"}*[integer-value]{lang="EN-US"}*]{#struct_0_x1862_90986_1391461146}[：差值采样类型的下限阈值，可以配置任意不大于差值采样类型上限阈值的整数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1318853750}

[[采样类型为差值采样时，采样差值小于或达到差值采样类型下限阈值时，将触发对应的事件。]{style="font-family:宋体"}]{#struct_0_x1862_90986_x1814448834}

[[若采样值连续多次小于或达到下限阈值，只会在第一次触发对应的事件，上限和下限对应事件的触发是交替产生的。]{style="font-family:宋体"}]{#struct_0_x1862_90986_x510362565}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1713361536}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_x1950570964}[配置差值采样类型的下限阈值为]{style="font-family:宋体"}[20]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1862_90986_x710690357}

[\[Sysname\] snmp mib event trigger owner owner1 name triggerA]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA\] test threshold]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA-threshold\] delta falling value 20]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_2087834339}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event trigger]{lang="EN-US"}**]{#struct_0_x1862_90986_x1101054888}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[test ]{lang="EN-US"}**]{#struct_0_x1862_90986_x1989721988}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sample]{lang="EN-US"}**]{#struct_0_x1862_90986_1149137270}
:::

::: {#-2078694143 .myid}
[]{#_Toc404797057}[]{#struct_0_x1862_90986_486341811}[]{#_Toc366652169}

**Event MIB \-- Event MIB配置命令 \-- delta rising**

------------------------------------------------------------------------

[**[delta]{lang="EN-US"}**[ ]{lang="EN-US"}**[rising]{lang="EN-US"}**]{#struct_0_x1862_90986_1760205430}[命令用来配置差值采样类型的上升阈值，并指定采样值大于等于该阈值对应的触发事件。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[delta]{lang="EN-US"}**[ ]{lang="EN-US"}**[rising]{lang="EN-US"}**]{#struct_0_x1862_90986_x2035573997}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_480578923}

[**[delta]{lang="EN-US"}**[ ]{lang="EN-US"}**[rising]{lang="EN-US"}**[ ]{lang="EN-US"}[{ **event** **owner** *event-owner* **name** *event-name* \| **value** *integer-value* }]{lang="EN-US"}]{#struct_0_x1862_90986_462497980}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[delta]{lang="EN-US"}**[ ]{lang="EN-US"}**[rising ]{lang="EN-US"}**[{ **event** \| **value** }]{lang="EN-US"}]{#struct_0_x1862_90986_847329030}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x2061414702}

[[上限阈值为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x1862_90986_1015521819}[，且没有指定对应的触发事件。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_2109902824}

[[trigger-threshold]{lang="EN-US"}]{#struct_0_x1862_90986_1797008616}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1536248875}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_639059751}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x1349472515}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x2055045618}

[**[event]{lang="EN-US"}**[ ]{lang="EN-US"}**[owner]{lang="EN-US"}***[ event-owner]{lang="EN-US"}*]{#struct_0_x1862_90986_1688374821}[：配置差值上限阈值事件的所有者，与]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[表中配置的]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[所有者]{style="font-family:宋体"}[owner]{lang="EN-US"}[相同。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}***[ event-name]{lang="EN-US"}*]{#struct_0_x1862_90986_x1741993474}[：配置差值上限阈值的事件，为]{style="font-family:宋体"}[1\~32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[value]{lang="EN-US"}**[ ]{lang="EN-US"}*[integer-value]{lang="EN-US"}*]{#struct_0_x1862_90986_274826274}[：差值上限阈值，可以配置任意不小于差值下限阈值的整数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x333951528}

[[采样类型为差值采样时，采样差值达到或超过上限阈值，将触发对应的事件。]{style="font-family:宋体"}]{#struct_0_x1862_90986_1169321563}

[[若采样值连续多次达到或超过上限阈值，只会在第一次触发对应的事件，上限和下限对应事件的触发是交替产生的。]{style="font-family:宋体"}]{#struct_0_x1862_90986_213305480}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1744254510}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_x550562122}[配置差值采样类型的差值上限阈值为]{style="font-family:宋体"}[50]{lang="EN-US"}[，对应的事件所有者为]{style="font-family:宋体"}[owner1]{lang="EN-US"}[，事件名为]{style="font-family:宋体"}[event1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1862_90986_887556405}

[\[Sysname\] snmp mib event trigger owner owner1 name triggerA]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA\] test threshold]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA-threshold\] delta rising value 50 ]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA-threshold\] delta rising event owner owner1 name event1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x252632910}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event trigger]{lang="EN-US"}**]{#struct_0_x1862_90986_x32306796}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[test ]{lang="EN-US"}**]{#struct_0_x1862_90986_1865714647}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sample]{lang="EN-US"}**]{#struct_0_x1862_90986_x393468453}
:::

::: {#337306014 .myid}
[]{#_Toc404797058}[]{#struct_0_x1862_90986_129728848}

**Event MIB \-- Event MIB配置命令 \-- description (Trigger view)**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_x1862_90986_x678972401}[命令用来配置]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[使用功能的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_x1862_90986_1293872153}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_714174066}

[**[description]{lang="EN-US"}**[ *trigger-description*]{lang="EN-US"}]{#struct_0_x1862_90986_x930010747}

[**[undo description]{lang="EN-US"}**]{#struct_0_x1862_90986_1955848619}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x999634720}

[[没有配置]{style="font-family:宋体"}[Trigger]{lang="EN-US"}]{#struct_0_x1862_90986_1099823313}[使用功能的描述信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x2116646063}

[[Trigger]{lang="EN-US"}]{#struct_0_x1862_90986_1134056129}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1963273191}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_1497805270}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x465980037}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x382393944}

[*[trigger-description]{lang="EN-US"}*]{#struct_0_x1862_90986_x17379342}[：]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[使用功能的描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x70486209}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_x1826813768}[配置所有者为]{style="font-family:宋体"}[owner1]{lang="EN-US"}[名称为]{style="font-family:宋体"}[triggerA]{lang="EN-US"}[的]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[描述信息为"]{style="font-family:宋体"}[triggerA is configured for network management events]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1862_90986_x1235527199}

[\[Sysname\] snmp mib event trigger owner owner1 name triggerA]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA\] description triggerA is configured for network management events]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_20554670}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event trigger]{lang="EN-US"}**]{#struct_0_x1862_90986_x811735878}
:::

::: {#1514726781 .myid}
[]{#_Toc404797059}[]{#struct_0_x1862_90986_107884688}[]{#_Toc366652174}

**Event MIB \-- Event MIB配置命令 \-- description (Event view)**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_x1862_90986_2023944105}[命令用来配置]{style="font-family:宋体"}[Event]{lang="EN-US"}[的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_x1862_90986_x154250326}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_612237292}

[**[description]{lang="EN-US"}**[ *event-description*]{lang="EN-US"}]{#struct_0_x1862_90986_1192689392}

[**[undo description]{lang="EN-US"}**]{#struct_0_x1862_90986_x1305788673}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1519514224}

[[没有任何描述信息。]{style="font-family:宋体"}]{#struct_0_x1862_90986_x108743122}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_247168236}

[[Event]{lang="EN-US"}]{#struct_0_x1862_90986_x403893760}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x188711607}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_481278376}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x393178440}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_123437254}

[*[event-description]{lang="EN-US"}*]{#struct_0_x1862_90986_834862704}[：]{style="font-family:宋体"}[Event]{lang="EN-US"}[的描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x828172774}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_x876221946}[配置拥有者为]{style="font-family:宋体"}[owner1]{lang="EN-US"}[的事件]{style="font-family:宋体"}[EventA]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[EventA is an RMON event]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1862_90986_x713192130}

[\[Sysname\] snmp mib event owner owner1 name EventA]{lang="EN-US"}

[\[Sysname-event-owner1-EventA\] description EventA is an RMON event]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x953846649}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event owner]{lang="EN-US"}**]{#struct_0_x1862_90986_x1581762713}
:::

::: {#1666641580 .myid}
[]{#_Toc404797060}[]{#struct_0_x1862_90986_x2050493951}[]{#_Toc381625450}[]{#_Toc388455465}[]{#_Toc401850357}[]{#_Toc382814748}[]{#_Toc382817236}[]{#_Toc382817732}[]{#_Toc382818226}[]{#_Toc383006324}[]{#_Toc383006820}[]{#_Toc383529499}[]{#_Toc387072148}[]{#_Toc382814749}[]{#_Toc382817237}[]{#_Toc382817733}[]{#_Toc382818227}[]{#_Toc383006325}[]{#_Toc383006821}[]{#_Toc383529500}[]{#_Toc387072149}[]{#_Toc382814750}[]{#_Toc382817238}[]{#_Toc382817734}[]{#_Toc382818228}[]{#_Toc383006326}[]{#_Toc383006822}[]{#_Toc383529501}[]{#_Toc387072150}[]{#_Toc382814751}[]{#_Toc382817239}[]{#_Toc382817735}[]{#_Toc382818229}[]{#_Toc383006327}[]{#_Toc383006823}[]{#_Toc383529502}[]{#_Toc387072151}

**Event MIB \-- Event MIB配置命令 \-- display snmp mib event**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **snmp mib event**]{lang="EN-US"}]{#struct_0_x1862_90986_1718619193}[命令用来显示所有]{style="font-family:宋体"}[Event MIB]{lang="EN-US"}[相关配置及统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1481389352}

[**[display snmp mib event]{lang="EN-US"}**]{#struct_0_x1862_90986_x1395046571}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1639516793}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1862_90986_x1652479160}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1898640918}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x249147606}

[[network-operator]{lang="EN-US"}]{#struct_0_x1862_90986_x218052156}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x1113003906}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1862_90986_475196212}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1117267344}

[[显示所有]{style="font-family:宋体"}[Event MIB]{lang="EN-US"}]{#struct_0_x1862_90986_2139912710}[相关配置信息及统计信息，包括获取触发事件名称、功能描述、动作类型、使能及实体控制状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1775036706}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_x1415384920}[显示设备当前所有的]{style="font-family:宋体"}[Event MIB]{lang="EN-US"}[配置信息和统计信息。]{style="font-family:宋体"}

[[\<Sysname\>display snmp mib event]{lang="EN-US"}]{#struct_0_x1862_90986_208952765}

[TriggerFailures               : 0]{lang="EN-US"}

[EventFailures                 : 0]{lang="EN-US"}

[SampleMinimum                 : 1]{lang="EN-US"}

[SampleInstanceMaximum         : 0]{lang="EN-US"}

[SampleInstance                : 0]{lang="EN-US"}

[SampleInstancesHigh           : 0]{lang="EN-US"}

[SampleInstanceLacks           : 0]{lang="EN-US"}

[Trigger entry triggerA owned by owner1:]{lang="EN-US"}

[  TriggerComment              : triggerA is to monitor the state of the interface]{lang="EN-US"}

[  TriggerTest                 : boolean]{lang="EN-US"}

[  TriggerSampleType           : absoluteValue]{lang="EN-US"}

[  TriggerValueID              : 1.3.6.1.2.1.2.2.1.7.3\<ifAdminStatus.3\>]{lang="EN-US"}

[  TriggerValueIDWildcard      : false]{lang="EN-US"}

[  TriggerTargetTag            : N/A]{lang="EN-US"}

[  TriggerContextName          : context1]{lang="EN-US"}

[  TriggerContextNameWildcard  : true]{lang="EN-US"}

[  TriggerFrequency(in seconds): 600]{lang="EN-US"}

[  TriggerEnabled              : true]{lang="EN-US"}

[  Boolean entry:]{lang="EN-US"}

[   BoolCmp                    : unequal]{lang="EN-US"}

[   BoolValue                  : 1]{lang="EN-US"}

[   BoolStartUp                : true]{lang="EN-US"}

[   BoolObjOwner               : owner1]{lang="EN-US"}

[   BoolObjName                : Objects1]{lang="EN-US"}

[   BoolEvtOwner               : N/A]{lang="EN-US"}

[   BoolEvtName                : N/A]{lang="EN-US"}

[Event entry eventA owned by owner2:]{lang="EN-US"}

[  EvtComment                  : event is to set ifAdminStatus]{lang="EN-US"}

[  EvtAction                   : Notification \| Set]{lang="EN-US"}

[  EvtEnabled                  : true]{lang="EN-US"}

[  Notification entry:]{lang="EN-US"}

[   NotifyOID                  : 1.3.6.1.2.1.88.2.0.1\<mteTriggerFired\>]{lang="EN-US"}

[   NotifyObjOwner             : N/A]{lang="EN-US"}

[   NotifyObjName              : N/A]{lang="EN-US"}

[  Set entry: ]{lang="EN-US"}

[   SetObj                     : 1.3.6.1.2.1.2.2.1.7\<ifAdminStatus\>]{lang="EN-US"}

[   SetObjWildcard             : true]{lang="EN-US"}

[   SetValue                   : 2 ]{lang="EN-US"}

[   SetTargetTag               : N/A]{lang="EN-US"}

[   SetContextName             : context1]{lang="EN-US"}

[   SetContextNameWildcard     : false]{lang="EN-US"}

[Object list objectA owend by owner3:]{lang="EN-US"}

[  ObjIndex                    : 1]{lang="EN-US"}

[  ObjID                       : 1.3.6.1.2.1.2.1.0\<ifNumber.0\>]{lang="EN-US"}

[  ObjIDWildcard               : false]{lang="EN-US"}

[Object list objectA owend by owner3:]{lang="EN-US"}

[  ObjIndex                    : 2]{lang="EN-US"}

[  ObjID                       : 1.3.6.1.2.1.2.2.1.2.0\<ifDescr.0\>]{lang="EN-US"}

[  ObjIDWildcard               : false]{lang="EN-US"}

[[上述显示信息中相关字段解释详见各表显示信息描述表（]{style="font-family:宋体"}]{#struct_0_x1862_90986_x893859608}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}1-1]{lang="EN-US"}](?1325784250#_Ref401909013)[至]{style="font-family:
宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-9]{lang="EN-US"}](?1555338873#_Ref401909035)[）。]{style="font-family:宋体"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x2139550410}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event trigger]{lang="EN-US"}**]{#struct_0_x1862_90986_x1762859456}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event ]{lang="EN-US"}**]{#struct_0_x1862_90986_2104143416}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event object list]{lang="EN-US"}**]{#struct_0_x1862_90986_2102043244}
:::

::: {#1325784250 .myid}
[]{#struct_0_x1862_90986_1452057298}[]{#_Toc404797061}[]{#_Toc388455469}[]{#_Toc388455470}[]{#_Toc388455471}[]{#_Toc388455473}[]{#_Toc388455474}[]{#_Toc388455475}[]{#_Toc388455476}[]{#_Toc388455477}[]{#_Toc388455478}[]{#_Toc388455480}[]{#_Toc388455481}[]{#_Toc388455482}[]{#_Toc388455483}[]{#_Toc388455484}[]{#_Toc388455485}[]{#_Toc388455486}[]{#_Toc388455487}[]{#_Toc388455488}[]{#_Toc388455489}[]{#_Toc388455490}[]{#_Toc388455491}[]{#_Toc388455492}[]{#_Toc388455493}

**Event MIB \-- Event MIB配置命令 \-- display snmp mib event event**

------------------------------------------------------------------------

[**[display snmp mib event event]{lang="EN-US"}**]{#struct_0_x1862_90986_x1357712181}[命令用来显示设备上已创建的]{style="font-family:
宋体"}[Event]{lang="EN-US"}[表信息及其相应的]{style="font-family:
宋体"}[Action]{lang="EN-US"}[表。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x2069591896}

[**[display snmp mib event event ]{lang="EN-US"}**[\[ **owner** *event-owner* **name** *event-name* \]]{lang="EN-US"}]{#struct_0_x1862_90986_1102366348}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x903475905}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1862_90986_1977956457}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_208596871}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_1764345039}

[[network-operator]{lang="EN-US"}]{#struct_0_x1862_90986_x743400718}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_1642860878}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1862_90986_1507541716}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x201353248}

[**[owner]{lang="EN-US"}***[ event-owner ]{lang="EN-US"}***[name]{lang="EN-US"}***[ event-name]{lang="EN-US"}*]{#struct_0_x1862_90986_2034072682}[：指定]{style="font-family:宋体"}[Event]{lang="EN-US"}[所有者及]{style="font-family:宋体"}[Event]{lang="EN-US"}[名称。]{style="font-family:宋体"}[Event]{lang="EN-US"}[所有者为]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户；]{style="font-family:宋体"}[Event]{lang="EN-US"}[名称为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。如不指定本参数，则显示设备上所有已创建的]{style="font-family:宋体"}[Event]{lang="EN-US"}[表及其相应的]{style="font-family:宋体"}[Action]{lang="EN-US"}[表信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1753222712}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_x863867311}[显示已创建的]{style="font-family:宋体"}[Event]{lang="EN-US"}[所有者为]{style="font-family:宋体"}[owner2]{lang="EN-US"}[，]{style="font-family:宋体"}[Event]{lang="EN-US"}[名称为]{style="font-family:宋体"}[eventA]{lang="EN-US"}[的]{style="font-family:宋体"}[Event]{lang="EN-US"}[表项信息及其相应的]{style="font-family:宋体"}[Action]{lang="EN-US"}[表信息。]{style="font-family:宋体"}

[[\<Sysname\>display snmp mib event event owner owner2 name eventA]{lang="EN-US"}]{#struct_0_x1862_90986_659291459}

[Event entry eventA owned by owner2:]{lang="EN-US"}

[EvtComment                  : event is to set ifAdminStatus ]{lang="EN-US"}

[EvtAction                   : Notification \| Set]{lang="EN-US"}

[EvtEnabled                  : true]{lang="EN-US"}

[Notification entry:]{lang="EN-US"}

[NotifyOID                  : 1.3.6.1.2.1.88.2.0.1\<mteTriggerFired\>]{lang="EN-US"}

[NotifyObjOwner             : N/A]{lang="EN-US"}

[NotifyObjName              : N/A]{lang="EN-US"}

[Set entry:]{lang="EN-US"}

[SetObj                     : 1.3.6.1.2.1.2.2.1.7\<ifAdminStatus\>]{lang="EN-US"}

[SetObjWildcard             : true]{lang="EN-US"}

[SetValue                   : 2]{lang="EN-US"}

[SetTargetTag               : N/A]{lang="EN-US"}

[SetContextName             : context1]{lang="EN-US"}

[SetContextNameWildcard     : false]{lang="EN-US"}

[]{#struct_0_x1862_90986_x1610412493}[[表1-1 ]{lang="EN-US"}[Event Entry]{lang="EN-US"}]{#_Ref401909013}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_934145330}[[字段]{style="font-family:黑体"}]{#struct_0_x1862_90986_x429369767}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1862_90986_1440946800}

[[Event entry *eventA* owned by *owner2*]{lang="EN-US"}]{#struct_0_x1862_90986_x2109700339}

[*[owner2]{lang="EN-US"}*]{#struct_0_x1862_90986_x1448886011}[：事件所有者，为]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户]{style="font-family:宋体"}

[*[eventA]{lang="EN-US"}*]{#struct_0_x1862_90986_x1209384480}[：事件名称]{style="font-family:宋体"}

[[EvtComment]{lang="EN-US"}]{#struct_0_x1862_90986_x1704071806}

[[事件信息描述]{style="font-family:宋体"}]{#struct_0_x1862_90986_1593330241}

[[EvtAction]{lang="EN-US"}]{#struct_0_x1862_90986_x810133293}

[[事件动作，有]{style="font-family:宋体"}[Set]{lang="EN-US"}]{#struct_0_x1862_90986_x1713296000}[和]{style="font-family:宋体"}[Notification]{lang="EN-US"}[两种动作]{style="font-family:宋体"}

[[EvtEnabled]{lang="EN-US"}]{#struct_0_x1862_90986_2014556636}

[[事件使能状态]{style="font-family:宋体"}]{#struct_0_x1862_90986_x1466048006}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[Notification Entry]{lang="EN-US"}]{#struct_0_x1862_90986_x217885362}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_927533434}[[字段]{style="font-family:黑体"}]{#struct_0_x1862_90986_x938331920}

[[描述]{style="font-family:黑体"}]{#struct_0_x1862_90986_x986223207}

[[NotifyOID]{lang="EN-US"}]{#struct_0_x1862_90986_755486637}

[[告警]{style="font-family:宋体"}[OID ]{lang="EN-US"}]{#struct_0_x1862_90986_x1288089357}[，]{style="font-family:宋体"}[OID]{lang="EN-US"}[类型为]{style="font-family:宋体"}[Trap]{lang="EN-US"}[节点]{style="font-family:宋体"}

[[NotifyObjOwner]{lang="EN-US"}]{#struct_0_x1862_90986_x2066825879}

[[告警绑定对象所有者，为]{style="font-family:宋体"}[SNMPv3 ]{lang="EN-US"}]{#struct_0_x1862_90986_1541414133}[用户]{style="font-family:宋体"}

[[NotifyObjName]{lang="EN-US"}]{#struct_0_x1862_90986_x1196920600}

[[告警绑定对象组名]{style="font-family:宋体"}]{#struct_0_x1862_90986_x936536196}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[Set Entry]{lang="EN-US"}]{#struct_0_x1862_90986_1015587355}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_929128958}[[字段]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1461421798}

[[描述]{style="font-family:黑体"}]{#struct_0_x1862_90986_1418885956}

[[SetObj]{lang="EN-US"}]{#struct_0_x1862_90986_1020223985}

[[事件设置对象的]{style="font-family:宋体"}[OID]{lang="EN-US"}]{#struct_0_x1862_90986_x425881109}[，]{style="font-family:宋体"}[OID]{lang="EN-US"}[类型为表节点、概念行节点、列节点、叶子节点、叶节点的父节点中的一种]{style="font-family:宋体"}

[[SetObjWildcard]{lang="EN-US"}]{#struct_0_x1862_90986_572356215}

[[设置对象]{style="font-family:宋体"}[OID]{lang="EN-US"}]{#struct_0_x1862_90986_x1605956487}[的通配标识符，取值为：]{style="font-family:宋体"}

[[false]{lang="EN-US"}]{#struct_0_x1862_90986_860272158}[：精确匹配]{lang="EN-US" style="font-family:宋体"}

[[true]{lang="EN-US"}]{#struct_0_x1862_90986_x696798718}[：通配]{lang="EN-US" style="font-family:宋体"}

[[SetValue]{lang="EN-US"}]{#struct_0_x1862_90986_x550496586}

[[设置对象]{style="font-family:宋体"}[OID]{lang="EN-US"}]{#struct_0_x1862_90986_2057451246}[的值]{style="font-family:宋体"}

[[SetTargetTag]{lang="EN-US"}]{#struct_0_x1862_90986_x1340300171}

[[设置对象远程标识符，长度为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x1862_90986_x2101139046}[的字符串表示为]{style="font-family:宋体"}[Local,]{lang="EN-US"}[本项目必须为空]{style="font-family:宋体"}

[[SetContextName]{lang="EN-US"}]{#struct_0_x1862_90986_843751088}

[[事件设置对象上下文环境，缺省情况下位空，本项目必须指定]{style="font-family:宋体"}]{#struct_0_x1862_90986_x988533161}

[[SetContextNameWildcard]{lang="EN-US"}]{#struct_0_x1862_90986_x983052238}

[[事件设置对象的上下文通配标识符，取值为：]{style="font-family:宋体"}]{#struct_0_x1862_90986_1796037329}

[[false]{lang="EN-US"}]{#struct_0_x1862_90986_327798089}[：精确匹配]{lang="EN-US" style="font-family:宋体"}

[[true]{lang="EN-US"}]{#struct_0_x1862_90986_x1429918873}[：通配]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x2116580527}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event]{lang="EN-US"}**]{#struct_0_x1862_90986_x2030067644}

::: {#1347432226 .myid}
[]{#_Toc404797062}[]{#struct_0_x1862_90986_1588714295}

**Event MIB \-- Event MIB配置命令 \-- display snmp mib event object list**

------------------------------------------------------------------------

[**[display snmp mib event object list]{lang="EN-US"}**]{#struct_0_x1862_90986_556550531}[命令用来显示设备上已创建的]{style="font-family:宋体"}[Object]{lang="EN-US"}[表的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1768060366}

[**[display snmp mib event object list ]{lang="EN-US"}**[\[ **owner** *objects-owner* **name** *objects-name* \]]{lang="EN-US"}]{#struct_0_x1862_90986_1284774824}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1103214209}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1862_90986_858322385}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1691738972}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_1019617190}

[[network-operator]{lang="EN-US"}]{#struct_0_x1862_90986_x962823803}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_1527873433}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1862_90986_x897216341}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x451211595}

[**[owner ]{lang="EN-US"}***[objects-owner]{lang="EN-US"}***[ name]{lang="EN-US"}**[ *objects-name*]{lang="EN-US"}]{#struct_0_x1862_90986_x846561981}[：指定对象组所有者及对象组名称。对象组所有者为]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户，对象组名称为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。如不指定本参数，则显示设备上所有已创建的]{style="font-family:宋体"}[Object]{lang="EN-US"}[表的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x579041838}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_612302828}[显示已创建的对象组所有者为]{style="font-family:宋体"}[owner3]{lang="EN-US"}[、对象组名称为]{style="font-family:宋体"}[objectA]{lang="EN-US"}[的]{style="font-family:宋体"}[Object]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[\<Sysname\> display snmp mib event object list owner owner3 name objectA]{lang="EN-US"}]{#struct_0_x1862_90986_x10699973}

[Object list objectA owned by owner3:]{lang="EN-US"}

[ObjIndex                    : 1]{lang="EN-US"}

[ObjID                       : 1.3.6.1.2.1.2.1.0\<ifNumber.0\>]{lang="EN-US"}

[ObjIDWildcard               : false]{lang="EN-US"}

[Object list objectA owned by owner3:]{lang="EN-US"}

[ObjIndex                    : 2]{lang="EN-US"}

[ObjID                       : 1.3.6.1.2.1.2.2.1.2.0\<ifDescr.0\>]{lang="EN-US"}

[ObjIDWildcard               : false]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display snmp mib event object list]{lang="EN-US"}]{#struct_0_x1862_90986_x1993667783}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_923116084}[[字段]{style="font-family:黑体"}]{#struct_0_x1862_90986_x244187165}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1862_90986_844745150}

[[Object list *objectA* owned by *owner3*]{lang="EN-US"}]{#struct_0_x1862_90986_x174993002}

[*[owner3]{lang="EN-US"}*]{#struct_0_x1862_90986_x1352304769}[：绑定对象所有者，为]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户，一级索引]{style="font-family:宋体"}

[*[objectA]{lang="EN-US"}*]{#struct_0_x1862_90986_x1324347293}[：绑定对象名，二级索引]{style="font-family:宋体"}

[[ObjIndex]{lang="EN-US"}]{#struct_0_x1862_90986_x487263285}

[[绑定对象的索引，三级索引]{style="font-family:宋体"}]{#struct_0_x1862_90986_203935653}

[[ObjID]{lang="EN-US"}]{#struct_0_x1862_90986_x953781113}

[[绑定对象的]{style="font-family:宋体"}[OID]{lang="EN-US"}]{#struct_0_x1862_90986_775978514}[，]{style="font-family:宋体"}[OID]{lang="EN-US"}[类型应为表节点、表中行节点、表中列节点、叶子节点、叶节点的父节点中的一种]{style="font-family:宋体"}

[[ObjIDWildcard]{lang="EN-US"}]{#struct_0_x1862_90986_x1342716998}

[[绑定对象]{style="font-family:宋体"}[OID]{lang="EN-US"}]{#struct_0_x1862_90986_x1758824234}[的通配标识符，取值为：]{style="font-family:宋体"}

[[false]{lang="EN-US"}]{#struct_0_x1862_90986_1978762747}[：精确匹配]{lang="EN-US" style="font-family:宋体"}

[[true]{lang="EN-US"}]{#struct_0_x1862_90986_x345760288}[：通配]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_243077497}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event object list]{lang="EN-US"}**]{#struct_0_x1862_90986_x1322240492}

::: {#-159833207 .myid}
[]{#_Toc404797063}[]{#struct_0_x1862_90986_951418504}

**Event MIB \-- Event MIB配置命令 \-- display snmp mib event summary**

------------------------------------------------------------------------

[**[display snmp mib event summary]{lang="EN-US"}**]{#struct_0_x1862_90986_375095522}[命令用来显示]{style="font-family:
宋体"}[Event MIB]{lang="EN-US"}[摘要信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1599941506}

[**[display snmp mib event summary]{lang="EN-US"}**]{#struct_0_x1862_90986_x1167333010}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1743989435}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1862_90986_x1124377566}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1775102242}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_2138381857}

[[network-operator]{lang="EN-US"}]{#struct_0_x1862_90986_451187543}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x113030005}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1862_90986_1598673337}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x2004747624}

[[显示全局配置信息包括]{style="font-family:宋体"}]{#struct_0_x1862_90986_2110230769}[最小采样时间间隔和]{style="font-family:宋体"}[最大采样实例数；及显示相关统计值包括当前采样行实例数、采样行数峰值、达到最大采样行数限制而采样失败的行数、]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[触发失败次数和执行相应]{style="font-family:宋体"}[Event]{lang="EN-US"}[失败次数。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1737750620}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_265622711}[显示]{style="font-family:宋体"}[Event MIB]{lang="EN-US"}[的摘要信息。]{style="font-family:宋体"}

[[\<Sysname\> display snmp mib event summary]{lang="EN-US"}]{#struct_0_x1862_90986_986507279}

[TriggerFailures               : 0]{lang="EN-US"}

[EventFailures                 : 0]{lang="EN-US"}

[SampleMinimum                 : 1]{lang="EN-US"}

[SampleInstanceMaximum         : 0]{lang="EN-US"}

[SampleInstance                : 0]{lang="EN-US"}

[SampleInstancesHigh           : 0]{lang="EN-US"}

[SampleInstanceLacks           : 0]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display snmp mib event summary]{lang="EN-US"}]{#struct_0_x1862_90986_386095761}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_926899410}[[字段]{style="font-family:黑体"}]{#struct_0_x1862_90986_x125011359}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1862_90986_1047622922}

[[TriggerFailures]{lang="EN-US"}]{#struct_0_x1862_90986_209018301}

[[Trigger]{lang="EN-US"}]{#struct_0_x1862_90986_x599396871}[触发测试失败的次数，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[EventFailures]{lang="EN-US"}]{#struct_0_x1862_90986_x916517102}

[[Trigger]{lang="EN-US"}]{#struct_0_x1862_90986_x1672722663}[触发]{style="font-family:宋体"}Notification[或者]{style="font-family:宋体"}Set[动作失败的次数，缺省值为]{style="font-family:宋体"}0

[[SampleMinimum]{lang="EN-US"}]{#struct_0_x1862_90986_x1744119293}

[[系统支持的最小采样时间间隔，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x1862_90986_x1957063610}

[[SampleInstanceMaximum]{lang="EN-US"}]{#struct_0_x1862_90986_x446294232}

[[系统支持的最大采样行数]{style="font-family:宋体"}]{#struct_0_x1862_90986_1740258877}

[[SampleInstance]{lang="EN-US"}]{#struct_0_x1862_90986_1360390386}

[[当前活动状态的采样节点数，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x1862_90986_189420519}

[[SampleInstancesHigh]{lang="EN-US"}]{#struct_0_x1862_90986_1987294903}

[[采样过程中达到的最大采样行数，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x1862_90986_x2069526360}

[[SampleInstanceLacks]{lang="EN-US"}]{#struct_0_x1862_90986_x1671691364}

[[由于超过系统支持的最大采样行数限制而采样失败的次数，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x1862_90986_x1642243261}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x928221854}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display snmp mib event]{lang="EN-US"}**]{#struct_0_x1862_90986_826635596}

::: {#1555338873 .myid}
[]{#_Toc404797064}[]{#struct_0_x1862_90986_827372735}

**Event MIB \-- Event MIB配置命令 \-- display snmp mib event trigger**

------------------------------------------------------------------------

[**[display snmp mib event trigger]{lang="EN-US"}**]{#struct_0_x1862_90986_x1139698289}[命令用来显示设备上已创建的]{style="font-family:
宋体"}[Trigger]{lang="EN-US"}[的相关信息及相应的]{style="font-family:
宋体"}[Test]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x107811653}

[**[display snmp mib event trigger ]{lang="EN-US"}**[\[ **owner** *trigger-owner* **name** *trigger-name* \]]{lang="EN-US"}]{#struct_0_x1862_90986_x1887279492}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_844391521}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1862_90986_x323813196}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1417764788}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_904124200}

[[network-operator]{lang="EN-US"}]{#struct_0_x1862_90986_x1500678038}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_659356995}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1862_90986_1220944108}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x965582771}

[**[owner]{lang="EN-US"}**[ *trigger-owner* **name** *trigger-name*]{lang="EN-US"}]{#struct_0_x1862_90986_201329246}[：显示指定所有者及指定名称的]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[的相关信息，]{style="font-family:宋体"}*[trigger-owner]{lang="EN-US"}*[表示]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[所有者，为]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户；]{style="font-family:宋体"}*[trigger-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。如不指定该参数，则显示设备上已创建的所有]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[及]{style="font-family:宋体"}[Test]{lang="EN-US"}[表的相关信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1393889062}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_909721144}[显示已创建的所有者为]{style="font-family:宋体"}[owner1]{lang="EN-US"}[、名称为]{style="font-family:宋体"}[triggerA]{lang="EN-US"}[的]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[信息及其相应的]{style="font-family:宋体"}[Test]{lang="EN-US"}[表信息。]{style="font-family:宋体"}

[[\<Sysname\> display snmp mib event trigger owner owner1 name triggerA]{lang="EN-US"}]{#struct_0_x1862_90986_x1713230464}

[Trigger entry triggerA owned by owner1: ]{lang="EN-US"}

[  TriggerComment              : triggerA is to monitor the state of the interface]{lang="EN-US"}

[  TriggerTest                 : existence \| boolean \| threshold]{lang="EN-US"}

[  TriggerSampleType           : absoluteValue]{lang="EN-US"}

[  TriggerValueID              : 1.3.6.1.2.1.2.2.1.7.3\<ifAdminStatus.3\>]{lang="EN-US"}

[  TriggerValueIDWildcard      : false]{lang="EN-US"}

[  TriggerTargetTag            : N/A]{lang="EN-US"}

[  TriggerContextName          : context1]{lang="EN-US"}

[  TriggerContextNameWildcard  : true]{lang="EN-US"}

[  TriggerFrequency(in seconds): 600]{lang="EN-US"}

[TriggerObjOwner             : owner1 ]{lang="EN-US"}

[  TriggerObjName              : obj1]{lang="EN-US"}

[  TriggerEnabled              : true]{lang="EN-US"}

[Existence entry:]{lang="EN-US"}

[   ExiTest                    : present \| absent]{lang="EN-US"}

[   ExiStartUp                 : present \| absent]{lang="EN-US"}

[   ExiObjOwner                : owner1]{lang="EN-US"}

[   ExiObjName                 : object1]{lang="EN-US"}

[   ExiEvtOwner                : owner1]{lang="EN-US"}

[   ExiEvtName                 : event1]{lang="EN-US"}

[Boolean entry: ]{lang="EN-US"}

[BoolCmp                    : unequal]{lang="EN-US"}

[BoolValue                  : 1]{lang="EN-US"}

[BoolStartUp                : true ]{lang="EN-US"}

[BoolObjOwner               : owner1]{lang="EN-US"}

[BoolObjName                : Objects1]{lang="EN-US"}

[BoolEvtOwner               : N/A]{lang="EN-US"}

[BoolEvtName                : N/A]{lang="EN-US"}

[Threshold entry:]{lang="EN-US"}

[   ThresStartUp               : falling]{lang="EN-US"}

[   ThresRising                : 40]{lang="EN-US"}

[   ThresFalling               : 20]{lang="EN-US"}

[   ThresDeltaRising           : 40]{lang="EN-US"}

[   ThresDeltaFalling          : 20]{lang="EN-US"}

[   ThresObjOwner              : N/A]{lang="EN-US"}

[   ThresObjName               : N/A]{lang="EN-US"}

[   ThresRisEvtOwner           : owner1]{lang="EN-US"}

[   ThresRisEvtName            : event1]{lang="EN-US"}

[   ThresFalEvtOwner           : owner1]{lang="EN-US"}

[   ThresFalEvtName            : event1]{lang="EN-US"}

[   ThresDeltaRisEvtOwner      : owner1]{lang="EN-US"}

[   ThresDeltaRisEvtName       : event1]{lang="EN-US"}

[   ThresDeltaFalEvtOwner      : owner1]{lang="EN-US"}

[   ThresDeltaFalEvtName       : event1]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[Trigger Entry]{lang="EN-US"}]{#struct_0_x1862_90986_x1990578366}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1220870834}[[字段]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1801172340}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1862_90986_2142141064}

[[Trigger entry *triggerA* owned by *owner1*]{lang="EN-US"}]{#struct_0_x1862_90986_1667869577}

[*[owner1]{lang="EN-US"}*]{#struct_0_x1862_90986_x950918515}[：]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[所有者]{style="font-family:宋体"}

[*[triggerA]{lang="EN-US"}*]{#struct_0_x1862_90986_x1883007033}[：]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[名称]{style="font-family:宋体"}

[[TriggerComment]{lang="EN-US"}]{#struct_0_x1862_90986_1015652891}

[[Trigger]{lang="EN-US"}]{#struct_0_x1862_90986_x624682060}[的功能和使用描述]{style="font-family:宋体"}

[[TriggerTest]{lang="EN-US"}]{#struct_0_x1862_90986_418769617}

[[Trigger]{lang="EN-US"}]{#struct_0_x1862_90986_x2107093910}[触发条件的检测类型，取值分为]{style="font-family:宋体"}[existence]{lang="EN-US"}[、]{style="font-family:宋体"}[boolean]{lang="EN-US"}[和]{style="font-family:宋体"}[threshold]{lang="EN-US"}[三种类型]{style="font-family:宋体"}

[[TriggerSampleType]{lang="EN-US"}]{#struct_0_x1862_90986_1762657783}

[[Trigger]{lang="EN-US"}]{#struct_0_x1862_90986_2102887374}[触发采样类型，取值为：]{style="font-family:宋体"}

[[absoluteValue]{lang="EN-US"}]{#struct_0_x1862_90986_1813214265}[：绝对值采样]{lang="EN-US" style="font-family:宋体"}

[[deltaValue]{lang="EN-US"}]{#struct_0_x1862_90986_x39790635}[：差值采样]{lang="EN-US" style="font-family:宋体"}

[[TriggerValueID]{lang="EN-US"}]{#struct_0_x1862_90986_x1308749891}

[[监控对象]{style="font-family:宋体"}[OID]{lang="EN-US"}]{#struct_0_x1862_90986_x1101133025}[，节点类型限定为表节点、表中行节点、表中列节点、叶子节点、叶节点的父节点的一种]{style="font-family:宋体"}

[[TriggerValueIDWildcard]{lang="EN-US"}]{#struct_0_x1862_90986_x550431050}

[[监控对象]{style="font-family:宋体"}[OID]{lang="EN-US"}]{#struct_0_x1862_90986_1262648818}[通配标识符，取值为：]{style="font-family:宋体"}

[[false]{lang="EN-US"}]{#struct_0_x1862_90986_1133883057}[：精确匹配]{lang="EN-US" style="font-family:宋体"}

[[true]{lang="EN-US"}]{#struct_0_x1862_90986_x264992591}[：通配]{lang="EN-US" style="font-family:宋体"}

[[TriggerTargetTag]{lang="EN-US"}]{#struct_0_x1862_90986_x1047721240}

[[标识监控对象所在的远程系统；]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_x1862_90986_250121922}[表示为]{style="font-family:宋体"}[Local]{lang="EN-US"}[，本项目必须为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[TriggerContextName]{lang="EN-US"}]{#struct_0_x1862_90986_x1089523557}

[[监控对象]{style="font-family:宋体"}[OID]{lang="EN-US"}]{#struct_0_x1862_90986_1751057306}[所处的上下文，缺省情况下为空，但本项目必须指定该参数，不能为空]{style="font-family:宋体"}

[[TriggerContextNameWildcard]{lang="EN-US"}]{#struct_0_x1862_90986_742913235}

[[监控对象]{style="font-family:宋体"}[OID]{lang="EN-US"}]{#struct_0_x1862_90986_x2116514991}[所处的上下文环境的通配标识符，分为精确匹配和通配]{style="font-family:宋体"}

[[TriggerFrequency]{lang="EN-US"}]{#struct_0_x1862_90986_657150369}

[[Trigger]{lang="EN-US"}]{#struct_0_x1862_90986_x1751282864}[采样间隔，此采样间隔应该大于或者等于系统支持的最小采样时间间隔]{style="font-family:宋体"}

[[TriggerObjOwner]{lang="EN-US"}]{#struct_0_x1862_90986_x615238372}

[[Trigger]{lang="EN-US"}]{#struct_0_x1862_90986_52197069}[绑定对象所有者，为]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[[用户]{style="font-size:10.5pt;font-family:宋体"}]{.MsoCommentReference}

[[TriggerObjName]{lang="EN-US"}]{#struct_0_x1862_90986_x1404314079}

[[Trigger]{lang="EN-US"}]{#struct_0_x1862_90986_x514606467}[的绑定对象]{style="font-family:宋体"}

[[TriggerEnabled]{lang="EN-US"}]{#struct_0_x1862_90986_612368364}

[[Trigger]{lang="EN-US"}]{#struct_0_x1862_90986_x27167998}[是否触发使能：]{style="font-family:宋体"}

[[enabled]{lang="EN-US"}]{#struct_0_x1862_90986_x2110658218}[：使能]{lang="EN-US" style="font-family:宋体"}

[[disabled]{lang="EN-US"}]{#struct_0_x1862_90986_x1288552411}[：未使能]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[Existence Entry]{lang="EN-US"}]{#struct_0_x1862_90986_x145542861}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1216545174}[[字段]{style="font-family:黑体"}]{#struct_0_x1862_90986_1593911291}

[[描述]{style="font-family:黑体"}]{#struct_0_x1862_90986_751624945}

[[ExiTest]{lang="EN-US"}]{#struct_0_x1862_90986_x535880802}

[[Existence]{lang="EN-US"}]{#struct_0_x1862_90986_x252583146}[触发条件类型，取值为]{style="font-family:宋体"}[present]{lang="EN-US"}[、]{style="font-family:宋体"}[absent]{lang="EN-US"}[和]{style="font-family:宋体"}[changed]{lang="EN-US"}

[[ExiStartUp]{lang="EN-US"}]{#struct_0_x1862_90986_x1251044195}

[[Existence]{lang="EN-US"}]{#struct_0_x1862_90986_x1645894747}[初始触发条件，取值为]{style="font-family:宋体"}[present]{lang="EN-US"}[、]{style="font-family:宋体"}[absent]{lang="EN-US"}[和]{style="font-family:宋体"}[changed]{lang="EN-US"}

[[ExiObjOwner]{lang="EN-US"}]{#struct_0_x1862_90986_x953715577}

[[Existence]{lang="EN-US"}]{#struct_0_x1862_90986_x799822940}[绑定对象所有者，为]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户]{style="font-family:宋体"}

[[ExiObjName]{lang="EN-US"}]{#struct_0_x1862_90986_x1411236498}

[[Existence]{lang="EN-US"}]{#struct_0_x1862_90986_1174287717}[的绑定对象]{style="font-family:宋体"}

[[ExiEvtOwner]{lang="EN-US"}]{#struct_0_x1862_90986_x594248625}

[[Existence]{lang="EN-US"}]{#struct_0_x1862_90986_x906854232}[触发事件所有者，为]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户]{style="font-family:宋体"}

[[ExiEvtName]{lang="EN-US"}]{#struct_0_x1862_90986_x1047870381}

[[Existence]{lang="EN-US"}]{#struct_0_x1862_90986_956125701}[触发事件名]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[Boolean Entry]{lang="EN-US"}]{#struct_0_x1862_90986_821993939}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1218921004}[[字段]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1524412407}

[[描述]{style="font-family:黑体"}]{#struct_0_x1862_90986_1967401578}

[[BoolCmp]{lang="EN-US"}]{#struct_0_x1862_90986_1775167778}

[[Boolean]{lang="EN-US"}]{#struct_0_x1862_90986_141196275}[比较的类型，取值为：]{style="font-family:宋体"}

[[有]{style="font-family:宋体"}[6]{lang="EN-US"}]{#struct_0_x1862_90986_1669405389}[种比较类型]{style="font-family:宋体"}[equal]{lang="EN-US"}[、]{style="font-family:宋体"}[less]{lang="EN-US"}[、]{style="font-family:宋体"}[lessOrEqual]{lang="EN-US"}[、]{style="font-family:宋体"}[greater]{lang="EN-US"}[、]{style="font-family:宋体"}[greaterOrEqual]{lang="EN-US"}[，默认情况下是]{style="font-family:宋体"}[unequal]{lang="EN-US"}[比较对象]{style="font-family:宋体"}[TriggerValueID]{lang="EN-US"}[与]{style="font-family:宋体"}[BoolValue]{lang="EN-US"}

[[BoolValue]{lang="EN-US"}]{#struct_0_x1862_90986_x831546794}

[[Boolean]{lang="EN-US"}]{#struct_0_x1862_90986_x2134967993}[参考值]{style="font-family:宋体"}

[[BoolStartUp]{lang="EN-US"}]{#struct_0_x1862_90986_x721873668}

[[初始触发条件，取值为]{style="font-family:宋体"}[true]{lang="EN-US"}]{#struct_0_x1862_90986_x1485152342}[和]{style="font-family:宋体"}[false]{lang="EN-US"}

[[BoolObjOwner]{lang="EN-US"}]{#struct_0_x1862_90986_x460070536}

[[Boolean]{lang="EN-US"}]{#struct_0_x1862_90986_x101506975}[触发绑定对象所有者，为]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[[用户]{style="font-size:10.5pt;font-family:宋体"}]{.MsoCommentReference}

[[BoolObjName]{lang="EN-US"}]{#struct_0_x1862_90986_1618860668}

[[Boolean]{lang="EN-US"}]{#struct_0_x1862_90986_209083837}[触发的绑定对象]{style="font-family:宋体"}

[[BoolEvtOwner]{lang="EN-US"}]{#struct_0_x1862_90986_612542035}

[[Boolean]{lang="EN-US"}]{#struct_0_x1862_90986_x1673128484}[触发事件所有者，为]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[[用户]{style="font-size:10.5pt;font-family:宋体"}]{.MsoCommentReference}

[[BoolEvtName]{lang="EN-US"}]{#struct_0_x1862_90986_1619426429}

[[Boolean]{lang="EN-US"}]{#struct_0_x1862_90986_x1376326184}[触发的事件名]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[]{#struct_0_x1862_90986_1094126882}[[表1-9 ]{lang="EN-US"}[Threshold Entry]{lang="EN-US"}]{#_Ref401909035}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1212909410}[[字段]{style="font-family:黑体"}]{#struct_0_x1862_90986_x817413700}

[[描述]{style="font-family:黑体"}]{#struct_0_x1862_90986_x234720052}

[[ThresStartUp]{lang="EN-US"}]{#struct_0_x1862_90986_873194163}

[[初始触发条件，取值为]{style="font-family:宋体"}[rising(1)]{lang="EN-US"}]{#struct_0_x1862_90986_1794161458}[、]{style="font-family:宋体"}[falling(2)]{lang="EN-US"}[和]{style="font-family:宋体"}[ risingOrFalling(3)]{lang="EN-US"}

[[ThresRising]{lang="EN-US"}]{#struct_0_x1862_90986_1226302453}

[[绝对值采样上升阈值]{style="font-family:宋体"}]{#struct_0_x1862_90986_x2069460824}

[[ThresFalling]{lang="EN-US"}]{#struct_0_x1862_90986_895153661}

[[绝对值采样下降阈值]{style="font-family:宋体"}]{#struct_0_x1862_90986_1693090482}

[[ThresDeltaRising]{lang="EN-US"}]{#struct_0_x1862_90986_388651172}

[[差值采样下的上升阈值]{style="font-family:宋体"}]{#struct_0_x1862_90986_937485298}

[[ThresDeltaFalling]{lang="EN-US"}]{#struct_0_x1862_90986_2070035653}

[[差值采样下的下降阈值]{style="font-family:宋体"}]{#struct_0_x1862_90986_x1645181348}

[[ThresObjOwner]{lang="EN-US"}]{#struct_0_x1862_90986_x722194539}

[[阈值触发下绑定对象所有者]{style="font-family:宋体"}]{#struct_0_x1862_90986_x1939263895}

[[ThresObjName]{lang="EN-US"}]{#struct_0_x1862_90986_x2123109920}

[[阈值触发下的绑定对象]{style="font-family:宋体"}]{#struct_0_x1862_90986_659422531}

[[ThresRisEvtOwner]{lang="EN-US"}]{#struct_0_x1862_90986_612276405}

[[Rising]{lang="EN-US"}]{#struct_0_x1862_90986_1192116963}[触发事件所有者，为]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户]{style="font-family:宋体"}

[[ThresRisEvtName]{lang="EN-US"}]{#struct_0_x1862_90986_1041580486}

[[Rising]{lang="EN-US"}]{#struct_0_x1862_90986_x1107934405}[触发事件名]{style="font-family:宋体"}

[[ThresFalEvtOwner]{lang="EN-US"}]{#struct_0_x1862_90986_x1212935187}

[[Falling]{lang="EN-US"}]{#struct_0_x1862_90986_1664043304}[触发事件所有者，为]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户]{style="font-family:宋体"}

[[ThresFalEvtName]{lang="EN-US"}]{#struct_0_x1862_90986_276869532}

[[Falling]{lang="EN-US"}]{#struct_0_x1862_90986_2098826901}[触发事件名]{style="font-family:宋体"}

[[ThresDeltaRisEvtOwner]{lang="EN-US"}]{#struct_0_x1862_90986_x1713164928}

[[DeltaRising]{lang="EN-US"}]{#struct_0_x1862_90986_1935499730}[触发事件所有者，为]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户]{style="font-family:宋体"}

[[ThresDeltaRisEvtName]{lang="EN-US"}]{#struct_0_x1862_90986_x1463532331}

[[DeltaRising]{lang="EN-US"}]{#struct_0_x1862_90986_1614142054}[触发事件名]{style="font-family:宋体"}

[[ThresDeltaFalEvtOwner]{lang="EN-US"}]{#struct_0_x1862_90986_x288023598}

[[DeltaFalling]{lang="EN-US"}]{#struct_0_x1862_90986_2116341602}[触发事件所有者，为]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户]{style="font-family:宋体"}

[[ThresDeltaFalEvtName]{lang="EN-US"}]{#struct_0_x1862_90986_x238582938}

[[DeltaFalling]{lang="EN-US"}]{#struct_0_x1862_90986_x1841050711}[触发事件名]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_525729557}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event trigger]{lang="EN-US"}**]{#struct_0_x1862_90986_1015718427}

::: {#-510798471 .myid}
[]{#_Toc404797065}[]{#struct_0_x1862_90986_x1098077794}[]{#_Toc366652175}[]{#_Toc388455499}[]{#_Toc388455500}[]{#_Toc388455501}[]{#_Toc388455504}[]{#_Toc388455505}[]{#_Toc388455506}[]{#_Toc388455507}[]{#_Toc388455508}[]{#_Toc388455511}[]{#_Toc388455512}[]{#_Toc388455513}[]{#_Toc388455514}[]{#_Toc388455515}[]{#_Toc388455516}[]{#_Toc388455517}[]{#_Toc388455518}[]{#_Toc388455519}[]{#_Toc388455520}[]{#_Toc388455521}[]{#_Toc388455523}

**Event MIB \-- Event MIB配置命令 \-- event enable**

------------------------------------------------------------------------

[**[event enable]{lang="EN-US"}**]{#struct_0_x1862_90986_x418074575}[命令用来使能事件触发功能。]{style="font-family:宋体"}

[**[undo event enable]{lang="EN-US"}**]{#struct_0_x1862_90986_1481679906}[命令用来关闭事件触发功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1014384371}

[**[event enable]{lang="EN-US"}**]{#struct_0_x1862_90986_1263654835}

[**[undo event ]{lang="EN-US"}[enable]{lang="EN-US"}**]{#struct_0_x1862_90986_301999603}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x206510923}

[[事件触发功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x1862_90986_922349889}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1110116909}

[[Event]{lang="EN-US"}]{#struct_0_x1862_90986_682292547}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x427116238}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x1073604706}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_233592626}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_655302165}

[[只有满足]{style="font-family:宋体"}[Test]{lang="EN-US"}]{#struct_0_x1862_90986_x1594977549}[检测条件且使能事件触发功能，才能触发相应的事件。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x550365514}

[[\#]{lang="EN-US"}]{#struct_0_x1862_90986_525773631}[使能事件所有者为]{style="font-family:宋体"}[owner1]{lang="EN-US"}[、名称为]{style="font-family:宋体"}[EventA]{lang="EN-US"}[事件的触发功能]{style="font-family:宋体"}[[。]{style="font-size:8.5pt;font-family:宋体"}]{.TerminalDisplayChar}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1862_90986_x272606957}

[\[Sysname\] snmp mib event owner owner1 name EventA]{lang="EN-US"}

[\[Sysname-event-owner1-EventA\] event enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_39632486}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event]{lang="EN-US"}**]{#struct_0_x1862_90986_x708403469}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[action ]{lang="EN-US"}**]{#struct_0_x1862_90986_1019968716}
:::

::: {#-474241434 .myid}
[]{#_Toc404797066}[]{#struct_0_x1862_90986_566077655}

**Event MIB \-- Event MIB配置命令 \-- event owner (Trigger-boolean view)**

------------------------------------------------------------------------

[**[event ]{lang="EN-US"}**]{#struct_0_x1862_90986_x1041236205}**[owner]{lang="EN-US"}**[命令用来指定在]{style="font-family:宋体"}[Trigger-boolean]{lang="EN-US"}[视图下满足检测条件时触发的]{style="font-family:宋体"}[Event]{lang="EN-US"}[事件。]{style="font-family:宋体"}

[**[undo event]{lang="EN-US"}**]{#struct_0_x1862_90986_x1051500798}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1009338498}

[**[event ]{lang="EN-US"}**]{#struct_0_x1862_90986_x260218223}**[owner ]{lang="EN-US"}***[event-owner]{lang="EN-US"}***[ name ]{lang="EN-US"}***[event-name]{lang="EN-US"}*

[**[undo event]{lang="EN-US"}**]{#struct_0_x1862_90986_2019130312}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_981137474}

[[没有指定任何]{style="font-family:宋体"}[Event]{lang="EN-US"}]{#struct_0_x1862_90986_1634923960}[事件。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x2116449455}

[[Trigger-boolean]{lang="EN-US"}]{#struct_0_x1862_90986_1260457575}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1950253954}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_1687340933}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x1927645295}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1778448782}

[*[event-owner]{lang="EN-US"}*]{#struct_0_x1862_90986_1501859762}[：触发事件的所有者，与]{style="font-family:宋体"}[trigger]{lang="EN-US"}[表中配置的]{style="font-family:宋体"}[trigger]{lang="EN-US"}[所有者]{style="font-family:宋体"}[owner]{lang="EN-US"}[相同。]{style="font-family:宋体"}

[*[event-name]{lang="EN-US"}*]{#struct_0_x1862_90986_109853786}[：触发事件名，为]{style="font-family:宋体"}[1\~32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_377146527}

[[当满足触发条件时，就根据指定的触发事件的所有者和名称在配置的]{style="font-family:宋体"}[Event]{lang="EN-US"}]{#struct_0_x1862_90986_20482780}[表中查找指定的]{style="font-family:宋体"}[Event]{lang="EN-US"}[事件是否存在；若存在，则执行该]{style="font-family:宋体"}[Event]{lang="EN-US"}[事件指定的动作。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_244766862}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_x597828499}[配置在满足检测条件时所触发的]{style="font-family:宋体"}[Event]{lang="EN-US"}[事件。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1862_90986_x1007189543}

[\[Sysname\] snmp mib event trigger owner owner1 name triggerA]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA\] test boolean]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA-boolean\] event owner owner1 name event1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x2145234138}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event trigger]{lang="EN-US"}**]{#struct_0_x1862_90986_612433900}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[test]{lang="EN-US"}**]{#struct_0_x1862_90986_x1712836821}
:::

::: {#1914000894 .myid}
[]{#_Toc404797067}[]{#struct_0_x1862_90986_2147257542}[]{#_Toc366652160}

**Event MIB \-- Event MIB配置命令 \-- event owner (Trigger-existence view)**

------------------------------------------------------------------------

[**[event ]{lang="EN-US"}**]{#struct_0_x1862_90986_684716040}**[owner]{lang="EN-US"}**[命令用来指定在]{style="font-family:宋体"}[Trigger-existence]{lang="EN-US"}[视图下，满足检测条件时触发的]{style="font-family:宋体"}[Event]{lang="EN-US"}[事件。]{style="font-family:宋体"}

[**[undo event]{lang="EN-US"}**]{#struct_0_x1862_90986_198190576}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1120124244}

[**[event ]{lang="EN-US"}**]{#struct_0_x1862_90986_553541977}**[owner ]{lang="EN-US"}***[event-owner]{lang="EN-US"}***[ name ]{lang="EN-US"}***[event-name]{lang="EN-US"}*

[**[undo event]{lang="EN-US"}**]{#struct_0_x1862_90986_2025862366}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x314830957}

[[没有指定任何]{style="font-family:宋体"}[event]{lang="EN-US"}]{#struct_0_x1862_90986_1739969308}[事件。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1969833008}

[[Trigger-existence]{lang="EN-US"}]{#struct_0_x1862_90986_682274965}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1662243134}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x2043417819}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_1268115048}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x953650041}

[*[event-owner]{lang="EN-US"}*]{#struct_0_x1862_90986_1526723279}[：指定触发事件的所有者，与]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[表中配置的]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[所有者]{style="font-family:宋体"}[owner]{lang="EN-US"}[相同。]{style="font-family:宋体"}

[*[event-name]{lang="EN-US"}*]{#struct_0_x1862_90986_x536768184}[：指定触发事件名，为]{style="font-family:宋体"}[1\~32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x803108971}

[[满足触发条件时，就会查找]{style="font-family:宋体"}[Event]{lang="EN-US"}]{#struct_0_x1862_90986_1784911282}[表，根据触发事件的所有者和名称查找配置的]{style="font-family:宋体"}[Event]{lang="EN-US"}[事件是否存在。若存在，则执行该]{style="font-family:宋体"}[Event]{lang="EN-US"}[事件指定的动作。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x48567571}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_x1680896974}[配置]{style="font-family:宋体"}[Trigger-existence]{lang="EN-US"}[子视图下，满足检测条件时所触发的]{style="font-family:宋体"}[Event]{lang="EN-US"}[事件。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1862_90986_x1260460481}

[\[Sysname\] snmp mib event trigger owner owner1 name triggerA]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA\] test existence]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA-existence\] event owner owner1 name event1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1069647265}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event trigger]{lang="EN-US"}**]{#struct_0_x1862_90986_x1206287423}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[test ]{lang="EN-US"}**]{#struct_0_x1862_90986_x1159884906}
:::

::: {#346314332 .myid}
[]{#_Toc404797068}[]{#struct_0_x1862_90986_x2145542035}[]{#_Toc366652170}

**Event MIB \-- Event MIB配置命令 \-- falling**

------------------------------------------------------------------------

[**[falling]{lang="EN-US"}**]{#struct_0_x1862_90986_712642050}[命令用来配置绝对值采样类型的下限阈值，并指定采样值小于等于该阈值时触发的事件。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[falling]{lang="EN-US"}**]{#struct_0_x1862_90986_x1424680586}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1775233314}

[**[falling]{lang="EN-US"}**[ ]{lang="EN-US"}[{ **event** **owner** *event-owner* **name** *event-name* \| **value** *integer-value* }]{lang="EN-US"}]{#struct_0_x1862_90986_1355262436}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[falling]{lang="EN-US"}**[ ]{lang="EN-US"}[{ **event** \| **value** }]{lang="EN-US"}]{#struct_0_x1862_90986_767245338}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_913674031}

[[下限阈值为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x1862_90986_x516017469}[，且未配置对应的触发事件。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_259278417}

[[Trigger-threshold]{lang="EN-US"}]{#struct_0_x1862_90986_x860873089}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1305247839}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x997937324}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_905288483}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_881226038}

[**[event]{lang="EN-US"}**[ ]{lang="EN-US"}**[owner]{lang="EN-US"}***[ event-owner]{lang="EN-US"}*]{#struct_0_x1862_90986_x62054664}[：配置下限阈值对应事件的所有者，与]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[表中配置的]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[所有者]{style="font-family:宋体"}[owner]{lang="EN-US"}[相同。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}***[ event-name]{lang="EN-US"}*]{#struct_0_x1862_90986_734664710}[：配置下限阈值对应的事件名，为]{style="font-family:宋体"}[1\~32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[value]{lang="EN-US"}**[ ]{lang="EN-US"}*[integer-value]{lang="EN-US"}*]{#struct_0_x1862_90986_925360675}[：绝对值采样的下限阈值，可以配置任意不大于上限阈值的整数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_209149373}

[[采样类型为绝对值采样时，采样值小于或达到下限阈值时，将触发对应的事件。]{style="font-family:宋体"}]{#struct_0_x1862_90986_1760751330}

[[若采样值连续多次小于或达到下限阈值，只会在第一次触发对应的事件，上限和下限对应事件的触发是交替产生的。]{style="font-family:宋体"}]{#struct_0_x1862_90986_x1653094398}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_126800557}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_x2098357544}[配置绝对值采样类型的下限阈值为]{style="font-family:宋体"}[20]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1862_90986_x630865883}

[\[Sysname\] snmp mib event trigger owner owner1 name triggerA]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA\] test threshold]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA-threshold\] falling value 20]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_2066848791}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event trigger]{lang="EN-US"}**]{#struct_0_x1862_90986_x1763335820}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[test ]{lang="EN-US"}**]{#struct_0_x1862_90986_x1268877747}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sample]{lang="EN-US"}**]{#struct_0_x1862_90986_x1819012883}
:::

::: {#1318637495 .myid}
[]{#_Toc404797069}[]{#struct_0_x1862_90986_692947528}

**Event MIB \-- Event MIB配置命令 \-- frequency**

------------------------------------------------------------------------

[**[frequency]{lang="EN-US"}**]{#struct_0_x1862_90986_x1869367282}[命令用来配置]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[采样时间间隔。]{style="font-family:宋体"}

[**[undo frequency]{lang="EN-US"}**]{#struct_0_x1862_90986_x26150907}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1618342123}

[**[frequency ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_x1862_90986_x2069395288}

[**[undo frequency ]{lang="EN-US"}**]{#struct_0_x1862_90986_x584131252}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_98482428}

[[采样时间间隔为]{style="font-family:宋体"}[600]{lang="EN-US"}]{#struct_0_x1862_90986_270355405}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x2114983428}

[[Trigger]{lang="EN-US"}]{#struct_0_x1862_90986_x1769323982}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x860328167}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_1081441297}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_1599925136}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x2029275817}

[*[interval]{lang="EN-US"}*]{#struct_0_x1862_90986_392498670}[：表示]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[采样时间间隔，为任意不小于系统支持的最小采样时间间隔的正整数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1572094209}

[[Trigger]{lang="EN-US"}]{#struct_0_x1862_90986_x1925118094}[采样时间间隔必须不小于系统支持的最小采样时间间隔，最小采样时间间隔使用]{style="font-family:宋体"}**[snmp mib event sample minimum]{lang="EN-US"}**[命令配置。]{style="font-family:
宋体"}

[[如果采样节点较多且配置的采样间隔时间过短，可能出现下一次采样时本次采样尚未完成，将导致下一次的采样处理失败，因此请根据实际情况合理配置采样间隔。]{style="font-family:宋体"}]{#struct_0_x1862_90986_x1358486384}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1632110744}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_659488067}[配置]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[采样时间间隔为]{style="font-family:宋体"}[360]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1862_90986_x580043728}

[\[Sysname\] snmp mib event trigger owner owner1 name triggerA]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA\] frequency 360]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x15610004}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event trigger]{lang="EN-US"}**]{#struct_0_x1862_90986_784265730}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event sample minimum]{lang="EN-US"}**]{#struct_0_x1862_90986_1611260451}
:::

::: {#1840225106 .myid}
[]{#_Toc404797070}[]{#struct_0_x1862_90986_362546539}

**Event MIB \-- Event MIB配置命令 \-- object list owner (Trigger view)**

------------------------------------------------------------------------

[**[object list owner]{lang="EN-US"}**]{#struct_0_x1862_90986_x1479619063}[命令用来指定绑定对象组。该]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[触发]{style="font-family:宋体"}[Notification]{lang="EN-US"}[动作发送相应]{style="font-family:宋体"}[Trap]{lang="EN-US"}[时需要添加此绑定对象组中的绑定变量。]{style="font-family:宋体"}

[**[undo object list]{lang="EN-US"}**]{#struct_0_x1862_90986_x386989591}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x671607525}

[**[object list owner ]{lang="EN-US"}***[objects-owner]{lang="EN-US"}***[ name ]{lang="EN-US"}***[objects-name]{lang="EN-US"}*]{#struct_0_x1862_90986_x2076816955}

[**[undo object list]{lang="EN-US"}**]{#struct_0_x1862_90986_1698233131}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1559692516}

[[没有指定绑定对象组。]{style="font-family:宋体"}]{#struct_0_x1862_90986_x1395986934}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x501710286}

[[Trigger]{lang="EN-US"}]{#struct_0_x1862_90986_119140748}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1311822464}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_834049983}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_70547053}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1523764610}

[**[owner]{lang="EN-US"}***[ objects-owner]{lang="EN-US"}*]{#struct_0_x1862_90986_2093441297}[：指定]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[绑定对象组的所有者，与]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[表中配置的]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[所有者相同。]{style="font-family:宋体"}

[**[name ]{lang="EN-US"}***[objects-name]{lang="EN-US"}*]{#struct_0_x1862_90986_1244190734}[：指定]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[绑定对象组名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1984644022}

[[通过指定绑定对象组的所有者和名称来指定一个绑定对象组，每个绑定对象组的成员由]{style="font-family:宋体"}]{#struct_0_x1862_90986_853952922}**[object list owner]{lang="EN-US"}**[命令指定；当]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[触发的事件包含]{style="font-family:宋体"}[notification]{lang="EN-US"}[动作时，发送的]{style="font-family:宋体"}[SNMP Trap]{lang="EN-US"}[报文将携带配置的绑定变量。]{style="font-family:宋体"}

[[发送]{style="font-family:宋体"}[Notification]{lang="EN-US"}]{#struct_0_x1862_90986_177233565}[时需要的绑定对象组可以在三处指定：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}[rigger]{lang="EN-US"}]{#struct_0_x1862_90986_x1253928195}[视图下的]{lang="EN-US" style="font-family:宋体"}**[object list]{lang="EN-US"}[ owner]{lang="EN-US"}**[命令指定]{lang="EN-US" style="font-family:宋体"}[T]{lang="EN-US"}[rigger]{lang="EN-US"}[对应的绑定对象组，表示所有由本]{lang="EN-US" style="font-family:宋体"}[T]{lang="EN-US"}[rigger]{lang="EN-US"}[触发]{lang="EN-US" style="font-family:宋体"}[N]{lang="EN-US"}[otification]{lang="EN-US"}[事件时需要添加的绑定变量；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}[rigger-test]{lang="EN-US"}]{#struct_0_x1862_90986_x552699775}[视图]{lang="EN-US" style="font-family:宋体"}[(]{lang="EN-US"}[T]{lang="EN-US"}[rigger-boolean]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[T]{lang="EN-US"}[rigger-existence]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[T]{lang="EN-US"}[rigger-threshold)]{lang="EN-US"}[下的]{lang="EN-US" style="font-family:宋体"}**[object list]{lang="EN-US"}[ owner]{lang="EN-US"}**[命令，统称为]{lang="EN-US" style="font-family:宋体"}[T]{lang="EN-US"}[rigger-test]{lang="EN-US"}[绑定对象组，表示满足此种检测类型所触发的]{lang="EN-US" style="font-family:宋体"}[N]{lang="EN-US"}[otification]{lang="EN-US"}[事件时需要添加的绑定变量；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N]{lang="EN-US"}[otification]{lang="EN-US"}]{#struct_0_x1862_90986_x471850230}[视图下的]{lang="EN-US" style="font-family:宋体"}**[object list]{lang="EN-US"}**[ owner]{lang="EN-US"}[命令指定]{lang="EN-US" style="font-family:宋体"}[N]{lang="EN-US"}[otification]{lang="EN-US"}[绑定对象组，表示引用此事件发送指定]{lang="EN-US" style="font-family:宋体"}[N]{lang="EN-US"}[otification]{lang="EN-US"}[事件时需要添加的绑定变量。]{lang="EN-US" style="font-family:宋体"}

[[实际配置时可以只在其中的一处指定，二处指定，或者三处同时指定。当多处指定时，绑定变量添加到]{style="font-family:宋体"}[Trap]{lang="EN-US"}]{#struct_0_x1862_90986_799015684}[报文中的顺序，应该为先添加]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[绑定对象组中的变量，再添加]{style="font-family:宋体"}[Test]{lang="EN-US"}[绑定对象组中的变量，最后添加]{style="font-family:宋体"}[Notification]{lang="EN-US"}[绑定对象组中的变量。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1070782406}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_x1169844612}[配置]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[绑定所有者为]{style="font-family:宋体"}[owner1]{lang="EN-US"}[，绑定对象组名称为]{style="font-family:宋体"}[objectA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1862_90986_1417060891}

[\[Sysname\] snmp mib event trigger owner owner1 name triggerA]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA\] object list owner owner1 name objectA]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x700971748}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event trigger]{lang="EN-US"}**]{#struct_0_x1862_90986_x1575655843}
:::

::: {#-968552363 .myid}
[]{#_Toc404797071}[]{#struct_0_x1862_90986_x984562852}[]{#_Toc366652156}[]{#_Toc382814764}[]{#_Toc382817252}[]{#_Toc382817748}[]{#_Toc382818242}[]{#_Toc383006340}[]{#_Toc383006836}[]{#_Toc383529515}[]{#_Toc387072164}[]{#_Toc382814765}[]{#_Toc382817253}[]{#_Toc382817749}[]{#_Toc382818243}[]{#_Toc383006341}[]{#_Toc383006837}[]{#_Toc383529516}[]{#_Toc387072165}[]{#_Toc382814766}[]{#_Toc382817254}[]{#_Toc382817750}[]{#_Toc382818244}[]{#_Toc383006342}[]{#_Toc383006838}[]{#_Toc383529517}[]{#_Toc387072166}[]{#_Toc382814767}[]{#_Toc382817255}[]{#_Toc382817751}[]{#_Toc382818245}[]{#_Toc383006343}[]{#_Toc383006839}[]{#_Toc383529518}[]{#_Toc387072167}[]{#_Toc382814768}[]{#_Toc382817256}[]{#_Toc382817752}[]{#_Toc382818246}[]{#_Toc383006344}[]{#_Toc383006840}[]{#_Toc383529519}[]{#_Toc387072168}[]{#_Toc382814769}[]{#_Toc382817257}[]{#_Toc382817753}[]{#_Toc382818247}[]{#_Toc383006345}[]{#_Toc383006841}[]{#_Toc383529520}[]{#_Toc387072169}[]{#_Toc382814770}[]{#_Toc382817258}[]{#_Toc382817754}[]{#_Toc382818248}[]{#_Toc383006346}[]{#_Toc383006842}[]{#_Toc383529521}[]{#_Toc387072170}[]{#_Toc382814771}[]{#_Toc382817259}[]{#_Toc382817755}[]{#_Toc382818249}[]{#_Toc383006347}[]{#_Toc383006843}[]{#_Toc383529522}[]{#_Toc387072171}[]{#_Toc382814772}[]{#_Toc382817260}[]{#_Toc382817756}[]{#_Toc382818250}[]{#_Toc383006348}[]{#_Toc383006844}[]{#_Toc383529523}[]{#_Toc387072172}[]{#_Toc382814773}[]{#_Toc382817261}[]{#_Toc382817757}[]{#_Toc382818251}[]{#_Toc383006349}[]{#_Toc383006845}[]{#_Toc383529524}[]{#_Toc387072173}[]{#_Toc382814775}[]{#_Toc382817263}[]{#_Toc382817759}[]{#_Toc382818253}[]{#_Toc383006351}[]{#_Toc383006847}[]{#_Toc383529526}[]{#_Toc387072175}[]{#_Toc382814776}[]{#_Toc382817264}[]{#_Toc382817760}[]{#_Toc382818254}[]{#_Toc383006352}[]{#_Toc383006848}[]{#_Toc383529527}[]{#_Toc387072176}[]{#_Toc382814777}[]{#_Toc382817265}[]{#_Toc382817761}[]{#_Toc382818255}[]{#_Toc383006353}[]{#_Toc383006849}[]{#_Toc383529528}[]{#_Toc387072177}[]{#_Toc382814778}[]{#_Toc382817266}[]{#_Toc382817762}[]{#_Toc382818256}[]{#_Toc383006354}[]{#_Toc383006850}[]{#_Toc383529529}[]{#_Toc387072178}[]{#_Toc382814779}[]{#_Toc382817267}[]{#_Toc382817763}[]{#_Toc382818257}[]{#_Toc383006355}[]{#_Toc383006851}[]{#_Toc383529530}[]{#_Toc387072179}[]{#_Toc382814780}[]{#_Toc382817268}[]{#_Toc382817764}[]{#_Toc382818258}[]{#_Toc383006356}[]{#_Toc383006852}[]{#_Toc383529531}[]{#_Toc387072180}[]{#_Toc382814781}[]{#_Toc382817269}[]{#_Toc382817765}[]{#_Toc382818259}[]{#_Toc383006357}[]{#_Toc383006853}[]{#_Toc383529532}[]{#_Toc387072181}[]{#_Toc382814782}[]{#_Toc382817270}[]{#_Toc382817766}[]{#_Toc382818260}[]{#_Toc383006358}[]{#_Toc383006854}[]{#_Toc383529533}[]{#_Toc387072182}[]{#_Toc382814783}[]{#_Toc382817271}[]{#_Toc382817767}[]{#_Toc382818261}[]{#_Toc383006359}[]{#_Toc383006855}[]{#_Toc383529534}[]{#_Toc387072183}[]{#_Toc382814784}[]{#_Toc382817272}[]{#_Toc382817768}[]{#_Toc382818262}[]{#_Toc383006360}[]{#_Toc383006856}[]{#_Toc383529535}[]{#_Toc387072184}[]{#_Toc382814785}[]{#_Toc382817273}[]{#_Toc382817769}[]{#_Toc382818263}[]{#_Toc383006361}[]{#_Toc383006857}[]{#_Toc383529536}[]{#_Toc387072185}[]{#_Toc382814786}[]{#_Toc382817274}[]{#_Toc382817770}[]{#_Toc382818264}[]{#_Toc383006362}[]{#_Toc383006858}[]{#_Toc383529537}[]{#_Toc387072186}[]{#_Toc382814788}[]{#_Toc382817276}[]{#_Toc382817772}[]{#_Toc382818266}[]{#_Toc383006364}[]{#_Toc383006860}[]{#_Toc383529539}[]{#_Toc387072188}[]{#_Toc382814790}[]{#_Toc382817278}[]{#_Toc382817774}[]{#_Toc382818268}[]{#_Toc383006366}[]{#_Toc383006862}[]{#_Toc383529541}[]{#_Toc387072190}[]{#_Toc382814791}[]{#_Toc382817279}[]{#_Toc382817775}[]{#_Toc382818269}[]{#_Toc383006367}[]{#_Toc383006863}[]{#_Toc383529542}[]{#_Toc387072191}[]{#_Toc382814792}[]{#_Toc382817280}[]{#_Toc382817776}[]{#_Toc382818270}[]{#_Toc383006368}[]{#_Toc383006864}[]{#_Toc383529543}[]{#_Toc387072192}[]{#_Toc382814793}[]{#_Toc382817281}[]{#_Toc382817777}[]{#_Toc382818271}[]{#_Toc383006369}[]{#_Toc383006865}[]{#_Toc383529544}[]{#_Toc387072193}[]{#_Toc382814795}[]{#_Toc382817283}[]{#_Toc382817779}[]{#_Toc382818273}[]{#_Toc383006371}[]{#_Toc383006867}[]{#_Toc383529546}[]{#_Toc387072195}[]{#_Toc382814796}[]{#_Toc382817284}[]{#_Toc382817780}[]{#_Toc382818274}[]{#_Toc383006372}[]{#_Toc383006868}[]{#_Toc383529547}[]{#_Toc387072196}[]{#_Toc382814797}[]{#_Toc382817285}[]{#_Toc382817781}[]{#_Toc382818275}[]{#_Toc383006373}[]{#_Toc383006869}[]{#_Toc383529548}[]{#_Toc387072197}[]{#_Toc382814798}[]{#_Toc382817286}[]{#_Toc382817782}[]{#_Toc382818276}[]{#_Toc383006374}[]{#_Toc383006870}[]{#_Toc383529549}[]{#_Toc387072198}[]{#_Toc382814799}[]{#_Toc382817287}[]{#_Toc382817783}[]{#_Toc382818277}[]{#_Toc383006375}[]{#_Toc383006871}[]{#_Toc383529550}[]{#_Toc387072199}[]{#_Toc382814801}[]{#_Toc382817289}[]{#_Toc382817785}[]{#_Toc382818279}[]{#_Toc383006377}[]{#_Toc383006873}[]{#_Toc383529552}[]{#_Toc387072201}[]{#_Toc382814802}[]{#_Toc382817290}[]{#_Toc382817786}[]{#_Toc382818280}[]{#_Toc383006378}[]{#_Toc383006874}[]{#_Toc383529553}[]{#_Toc387072202}[]{#_Toc382814803}[]{#_Toc382817291}[]{#_Toc382817787}[]{#_Toc382818281}[]{#_Toc383006379}[]{#_Toc383006875}[]{#_Toc383529554}[]{#_Toc387072203}[]{#_Toc382814804}[]{#_Toc382817292}[]{#_Toc382817788}[]{#_Toc382818282}[]{#_Toc383006380}[]{#_Toc383006876}[]{#_Toc383529555}[]{#_Toc387072204}[]{#_Toc382814805}[]{#_Toc382817293}[]{#_Toc382817789}[]{#_Toc382818283}[]{#_Toc383006381}[]{#_Toc383006877}[]{#_Toc383529556}[]{#_Toc387072205}[]{#_Toc382814806}[]{#_Toc382817294}[]{#_Toc382817790}[]{#_Toc382818284}[]{#_Toc383006382}[]{#_Toc383006878}[]{#_Toc383529557}[]{#_Toc387072206}[]{#_Toc382814807}[]{#_Toc382817295}[]{#_Toc382817791}[]{#_Toc382818285}[]{#_Toc383006383}[]{#_Toc383006879}[]{#_Toc383529558}[]{#_Toc387072207}[]{#_Toc382814808}[]{#_Toc382817296}[]{#_Toc382817792}[]{#_Toc382818286}[]{#_Toc383006384}[]{#_Toc383006880}[]{#_Toc383529559}[]{#_Toc387072208}[]{#_Toc382814809}[]{#_Toc382817297}[]{#_Toc382817793}[]{#_Toc382818287}[]{#_Toc383006385}[]{#_Toc383006881}[]{#_Toc383529560}[]{#_Toc387072209}[]{#_Toc382814810}[]{#_Toc382817298}[]{#_Toc382817794}[]{#_Toc382818288}[]{#_Toc383006386}[]{#_Toc383006882}[]{#_Toc383529561}[]{#_Toc387072210}[]{#_Toc382814811}[]{#_Toc382817299}[]{#_Toc382817795}[]{#_Toc382818289}[]{#_Toc383006387}[]{#_Toc383006883}[]{#_Toc383529562}[]{#_Toc387072211}[]{#_Toc382814813}[]{#_Toc382817301}[]{#_Toc382817797}[]{#_Toc382818291}[]{#_Toc383006389}[]{#_Toc383006885}[]{#_Toc383529564}[]{#_Toc387072213}[]{#_Toc382814814}[]{#_Toc382817302}[]{#_Toc382817798}[]{#_Toc382818292}[]{#_Toc383006390}[]{#_Toc383006886}[]{#_Toc383529565}[]{#_Toc387072214}[]{#_Toc382814815}[]{#_Toc382817303}[]{#_Toc382817799}[]{#_Toc382818293}[]{#_Toc383006391}[]{#_Toc383006887}[]{#_Toc383529566}[]{#_Toc387072215}[]{#_Toc382814816}[]{#_Toc382817304}[]{#_Toc382817800}[]{#_Toc382818294}[]{#_Toc383006392}[]{#_Toc383006888}[]{#_Toc383529567}[]{#_Toc387072216}[]{#_Toc382814817}[]{#_Toc382817305}[]{#_Toc382817801}[]{#_Toc382818295}[]{#_Toc383006393}[]{#_Toc383006889}[]{#_Toc383529568}[]{#_Toc387072217}[]{#_Toc382814818}[]{#_Toc382817306}[]{#_Toc382817802}[]{#_Toc382818296}[]{#_Toc383006394}[]{#_Toc383006890}[]{#_Toc383529569}[]{#_Toc387072218}[]{#_Toc382814819}[]{#_Toc382817307}[]{#_Toc382817803}[]{#_Toc382818297}[]{#_Toc383006395}[]{#_Toc383006891}[]{#_Toc383529570}[]{#_Toc387072219}[]{#_Toc382814820}[]{#_Toc382817308}[]{#_Toc382817804}[]{#_Toc382818298}[]{#_Toc383006396}[]{#_Toc383006892}[]{#_Toc383529571}[]{#_Toc387072220}[]{#_Toc382814821}[]{#_Toc382817309}[]{#_Toc382817805}[]{#_Toc382818299}[]{#_Toc383006397}[]{#_Toc383006893}[]{#_Toc383529572}[]{#_Toc387072221}[]{#_Toc382814822}[]{#_Toc382817310}[]{#_Toc382817806}[]{#_Toc382818300}[]{#_Toc383006398}[]{#_Toc383006894}[]{#_Toc383529573}[]{#_Toc387072222}[]{#_Toc382814825}[]{#_Toc382817313}[]{#_Toc382817809}[]{#_Toc382818303}[]{#_Toc383006401}[]{#_Toc383006897}[]{#_Toc383529576}[]{#_Toc387072225}[]{#_Toc382814826}[]{#_Toc382817314}[]{#_Toc382817810}[]{#_Toc382818304}[]{#_Toc383006402}[]{#_Toc383006898}[]{#_Toc383529577}[]{#_Toc387072226}[]{#_Toc382814827}[]{#_Toc382817315}[]{#_Toc382817811}[]{#_Toc382818305}[]{#_Toc383006403}[]{#_Toc383006899}[]{#_Toc383529578}[]{#_Toc387072227}[]{#_Toc382814828}[]{#_Toc382817316}[]{#_Toc382817812}[]{#_Toc382818306}[]{#_Toc383006404}[]{#_Toc383006900}[]{#_Toc383529579}[]{#_Toc387072228}[]{#_Toc382814829}[]{#_Toc382817317}[]{#_Toc382817813}[]{#_Toc382818307}[]{#_Toc383006405}[]{#_Toc383006901}[]{#_Toc383529580}[]{#_Toc387072229}[]{#_Toc382814830}[]{#_Toc382817318}[]{#_Toc382817814}[]{#_Toc382818308}[]{#_Toc383006406}[]{#_Toc383006902}[]{#_Toc383529581}[]{#_Toc387072230}[]{#_Toc382814831}[]{#_Toc382817319}[]{#_Toc382817815}[]{#_Toc382818309}[]{#_Toc383006407}[]{#_Toc383006903}[]{#_Toc383529582}[]{#_Toc387072231}[]{#_Toc382814832}[]{#_Toc382817320}[]{#_Toc382817816}[]{#_Toc382818310}[]{#_Toc383006408}[]{#_Toc383006904}[]{#_Toc383529583}[]{#_Toc387072232}[]{#_Toc382814833}[]{#_Toc382817321}[]{#_Toc382817817}[]{#_Toc382818311}[]{#_Toc383006409}[]{#_Toc383006905}[]{#_Toc383529584}[]{#_Toc387072233}[]{#_Toc382814834}[]{#_Toc382817322}[]{#_Toc382817818}[]{#_Toc382818312}[]{#_Toc383006410}[]{#_Toc383006906}[]{#_Toc383529585}[]{#_Toc387072234}[]{#_Toc382814835}[]{#_Toc382817323}[]{#_Toc382817819}[]{#_Toc382818313}[]{#_Toc383006411}[]{#_Toc383006907}[]{#_Toc383529586}[]{#_Toc387072235}[]{#_Toc382814836}[]{#_Toc382817324}[]{#_Toc382817820}[]{#_Toc382818314}[]{#_Toc383006412}[]{#_Toc383006908}[]{#_Toc383529587}[]{#_Toc387072236}[]{#_Toc382814838}[]{#_Toc382817326}[]{#_Toc382817822}[]{#_Toc382818316}[]{#_Toc383006414}[]{#_Toc383006910}[]{#_Toc383529589}[]{#_Toc387072238}[]{#_Toc382814839}[]{#_Toc382817327}[]{#_Toc382817823}[]{#_Toc382818317}[]{#_Toc383006415}[]{#_Toc383006911}[]{#_Toc383529590}[]{#_Toc387072239}[]{#_Toc382814840}[]{#_Toc382817328}[]{#_Toc382817824}[]{#_Toc382818318}[]{#_Toc383006416}[]{#_Toc383006912}[]{#_Toc383529591}[]{#_Toc387072240}[]{#_Toc382814841}[]{#_Toc382817329}[]{#_Toc382817825}[]{#_Toc382818319}[]{#_Toc383006417}[]{#_Toc383006913}[]{#_Toc383529592}[]{#_Toc387072241}[]{#_Toc382814842}[]{#_Toc382817330}[]{#_Toc382817826}[]{#_Toc382818320}[]{#_Toc383006418}[]{#_Toc383006914}[]{#_Toc383529593}[]{#_Toc387072242}[]{#_Toc382814843}[]{#_Toc382817331}[]{#_Toc382817827}[]{#_Toc382818321}[]{#_Toc383006419}[]{#_Toc383006915}[]{#_Toc383529594}[]{#_Toc387072243}[]{#_Toc382814844}[]{#_Toc382817332}[]{#_Toc382817828}[]{#_Toc382818322}[]{#_Toc383006420}[]{#_Toc383006916}[]{#_Toc383529595}[]{#_Toc387072244}[]{#_Toc382814845}[]{#_Toc382817333}[]{#_Toc382817829}[]{#_Toc382818323}[]{#_Toc383006421}[]{#_Toc383006917}[]{#_Toc383529596}[]{#_Toc387072245}[]{#_Toc382814846}[]{#_Toc382817334}[]{#_Toc382817830}[]{#_Toc382818324}[]{#_Toc383006422}[]{#_Toc383006918}[]{#_Toc383529597}[]{#_Toc387072246}[]{#_Toc382814847}[]{#_Toc382817335}[]{#_Toc382817831}[]{#_Toc382818325}[]{#_Toc383006423}[]{#_Toc383006919}[]{#_Toc383529598}[]{#_Toc387072247}[]{#_Toc382814850}[]{#_Toc382817338}[]{#_Toc382817834}[]{#_Toc382818328}[]{#_Toc383006426}[]{#_Toc383006922}[]{#_Toc383529601}[]{#_Toc387072250}[]{#_Toc382814851}[]{#_Toc382817339}[]{#_Toc382817835}[]{#_Toc382818329}[]{#_Toc383006427}[]{#_Toc383006923}[]{#_Toc383529602}[]{#_Toc387072251}[]{#_Toc382814852}[]{#_Toc382817340}[]{#_Toc382817836}[]{#_Toc382818330}[]{#_Toc383006428}[]{#_Toc383006924}[]{#_Toc383529603}[]{#_Toc387072252}[]{#_Toc382814853}[]{#_Toc382817341}[]{#_Toc382817837}[]{#_Toc382818331}[]{#_Toc383006429}[]{#_Toc383006925}[]{#_Toc383529604}[]{#_Toc387072253}[]{#_Toc382814854}[]{#_Toc382817342}[]{#_Toc382817838}[]{#_Toc382818332}[]{#_Toc383006430}[]{#_Toc383006926}[]{#_Toc383529605}[]{#_Toc387072254}[]{#_Toc382814855}[]{#_Toc382817343}[]{#_Toc382817839}[]{#_Toc382818333}[]{#_Toc383006431}[]{#_Toc383006927}[]{#_Toc383529606}[]{#_Toc387072255}[]{#_Toc382814856}[]{#_Toc382817344}[]{#_Toc382817840}[]{#_Toc382818334}[]{#_Toc383006432}[]{#_Toc383006928}[]{#_Toc383529607}[]{#_Toc387072256}[]{#_Toc382814857}[]{#_Toc382817345}[]{#_Toc382817841}[]{#_Toc382818335}[]{#_Toc383006433}[]{#_Toc383006929}[]{#_Toc383529608}[]{#_Toc387072257}[]{#_Toc382814858}[]{#_Toc382817346}[]{#_Toc382817842}[]{#_Toc382818336}[]{#_Toc383006434}[]{#_Toc383006930}[]{#_Toc383529609}[]{#_Toc387072258}[]{#_Toc382814859}[]{#_Toc382817347}[]{#_Toc382817843}[]{#_Toc382818337}[]{#_Toc383006435}[]{#_Toc383006931}[]{#_Toc383529610}[]{#_Toc387072259}[]{#_Toc382814860}[]{#_Toc382817348}[]{#_Toc382817844}[]{#_Toc382818338}[]{#_Toc383006436}[]{#_Toc383006932}[]{#_Toc383529611}[]{#_Toc387072260}[]{#_Toc382814861}[]{#_Toc382817349}[]{#_Toc382817845}[]{#_Toc382818339}[]{#_Toc383006437}[]{#_Toc383006933}[]{#_Toc383529612}[]{#_Toc387072261}[]{#_Toc382814863}[]{#_Toc382817351}[]{#_Toc382817847}[]{#_Toc382818341}[]{#_Toc383006439}[]{#_Toc383006935}[]{#_Toc383529614}[]{#_Toc387072263}[]{#_Toc382814865}[]{#_Toc382817353}[]{#_Toc382817849}[]{#_Toc382818343}[]{#_Toc383006441}[]{#_Toc383006937}[]{#_Toc383529616}[]{#_Toc387072265}[]{#_Toc382814866}[]{#_Toc382817354}[]{#_Toc382817850}[]{#_Toc382818344}[]{#_Toc383006442}[]{#_Toc383006938}[]{#_Toc383529617}[]{#_Toc387072266}[]{#_Toc382814867}[]{#_Toc382817355}[]{#_Toc382817851}[]{#_Toc382818345}[]{#_Toc383006443}[]{#_Toc383006939}[]{#_Toc383529618}[]{#_Toc387072267}[]{#_Toc382814868}[]{#_Toc382817356}[]{#_Toc382817852}[]{#_Toc382818346}[]{#_Toc383006444}[]{#_Toc383006940}[]{#_Toc383529619}[]{#_Toc387072268}[]{#_Toc382814869}[]{#_Toc382817357}[]{#_Toc382817853}[]{#_Toc382818347}[]{#_Toc383006445}[]{#_Toc383006941}[]{#_Toc383529620}[]{#_Toc387072269}[]{#_Toc382814870}[]{#_Toc382817358}[]{#_Toc382817854}[]{#_Toc382818348}[]{#_Toc383006446}[]{#_Toc383006942}[]{#_Toc383529621}[]{#_Toc387072270}[]{#_Toc382814871}[]{#_Toc382817359}[]{#_Toc382817855}[]{#_Toc382818349}[]{#_Toc383006447}[]{#_Toc383006943}[]{#_Toc383529622}[]{#_Toc387072271}[]{#_Toc382814872}[]{#_Toc382817360}[]{#_Toc382817856}[]{#_Toc382818350}[]{#_Toc383006448}[]{#_Toc383006944}[]{#_Toc383529623}[]{#_Toc387072272}[]{#_Toc382814873}[]{#_Toc382817361}[]{#_Toc382817857}[]{#_Toc382818351}[]{#_Toc383006449}[]{#_Toc383006945}[]{#_Toc383529624}[]{#_Toc387072273}[]{#_Toc382814874}[]{#_Toc382817362}[]{#_Toc382817858}[]{#_Toc382818352}[]{#_Toc383006450}[]{#_Toc383006946}[]{#_Toc383529625}[]{#_Toc387072274}[]{#_Toc382814877}[]{#_Toc382817365}[]{#_Toc382817861}[]{#_Toc382818355}[]{#_Toc383006453}[]{#_Toc383006949}[]{#_Toc383529628}[]{#_Toc387072277}[]{#_Toc382814878}[]{#_Toc382817366}[]{#_Toc382817862}[]{#_Toc382818356}[]{#_Toc383006454}[]{#_Toc383006950}[]{#_Toc383529629}[]{#_Toc387072278}[]{#_Toc382814879}[]{#_Toc382817367}[]{#_Toc382817863}[]{#_Toc382818357}[]{#_Toc383006455}[]{#_Toc383006951}[]{#_Toc383529630}[]{#_Toc387072279}[]{#_Toc382814880}[]{#_Toc382817368}[]{#_Toc382817864}[]{#_Toc382818358}[]{#_Toc383006456}[]{#_Toc383006952}[]{#_Toc383529631}[]{#_Toc387072280}[]{#_Toc382814881}[]{#_Toc382817369}[]{#_Toc382817865}[]{#_Toc382818359}[]{#_Toc383006457}[]{#_Toc383006953}[]{#_Toc383529632}[]{#_Toc387072281}[]{#_Toc382814882}[]{#_Toc382817370}[]{#_Toc382817866}[]{#_Toc382818360}[]{#_Toc383006458}[]{#_Toc383006954}[]{#_Toc383529633}[]{#_Toc387072282}[]{#_Toc382814883}[]{#_Toc382817371}[]{#_Toc382817867}[]{#_Toc382818361}[]{#_Toc383006459}[]{#_Toc383006955}[]{#_Toc383529634}[]{#_Toc387072283}[]{#_Toc382814884}[]{#_Toc382817372}[]{#_Toc382817868}[]{#_Toc382818362}[]{#_Toc383006460}[]{#_Toc383006956}[]{#_Toc383529635}[]{#_Toc387072284}[]{#_Toc382814885}[]{#_Toc382817373}[]{#_Toc382817869}[]{#_Toc382818363}[]{#_Toc383006461}[]{#_Toc383006957}[]{#_Toc383529636}[]{#_Toc387072285}[]{#_Toc382814886}[]{#_Toc382817374}[]{#_Toc382817870}[]{#_Toc382818364}[]{#_Toc383006462}[]{#_Toc383006958}[]{#_Toc383529637}[]{#_Toc387072286}[]{#_Toc382814889}[]{#_Toc382817377}[]{#_Toc382817873}[]{#_Toc382818367}[]{#_Toc383006465}[]{#_Toc383006961}[]{#_Toc383529640}[]{#_Toc387072289}[]{#_Toc382814890}[]{#_Toc382817378}[]{#_Toc382817874}[]{#_Toc382818368}[]{#_Toc383006466}[]{#_Toc383006962}[]{#_Toc383529641}[]{#_Toc387072290}[]{#_Toc382814891}[]{#_Toc382817379}[]{#_Toc382817875}[]{#_Toc382818369}[]{#_Toc383006467}[]{#_Toc383006963}[]{#_Toc383529642}[]{#_Toc387072291}[]{#_Toc382814892}[]{#_Toc382817380}[]{#_Toc382817876}[]{#_Toc382818370}[]{#_Toc383006468}[]{#_Toc383006964}[]{#_Toc383529643}[]{#_Toc387072292}[]{#_Toc382814893}[]{#_Toc382817381}[]{#_Toc382817877}[]{#_Toc382818371}[]{#_Toc383006469}[]{#_Toc383006965}[]{#_Toc383529644}[]{#_Toc387072293}[]{#_Toc382814894}[]{#_Toc382817382}[]{#_Toc382817878}[]{#_Toc382818372}[]{#_Toc383006470}[]{#_Toc383006966}[]{#_Toc383529645}[]{#_Toc387072294}[]{#_Toc382814895}[]{#_Toc382817383}[]{#_Toc382817879}[]{#_Toc382818373}[]{#_Toc383006471}[]{#_Toc383006967}[]{#_Toc383529646}[]{#_Toc387072295}[]{#_Toc382814896}[]{#_Toc382817384}[]{#_Toc382817880}[]{#_Toc382818374}[]{#_Toc383006472}[]{#_Toc383006968}[]{#_Toc383529647}[]{#_Toc387072296}[]{#_Toc382814897}[]{#_Toc382817385}[]{#_Toc382817881}[]{#_Toc382818375}[]{#_Toc383006473}[]{#_Toc383006969}[]{#_Toc383529648}[]{#_Toc387072297}[]{#_Toc382814898}[]{#_Toc382817386}[]{#_Toc382817882}[]{#_Toc382818376}[]{#_Toc383006474}[]{#_Toc383006970}[]{#_Toc383529649}[]{#_Toc387072298}[]{#_Toc382814900}[]{#_Toc382817388}[]{#_Toc382817884}[]{#_Toc382818378}[]{#_Toc383006476}[]{#_Toc383006972}[]{#_Toc383529651}[]{#_Toc387072300}[]{#_Toc382814901}[]{#_Toc382817389}[]{#_Toc382817885}[]{#_Toc382818379}[]{#_Toc383006477}[]{#_Toc383006973}[]{#_Toc383529652}[]{#_Toc387072301}[]{#_Toc382814902}[]{#_Toc382817390}[]{#_Toc382817886}[]{#_Toc382818380}[]{#_Toc383006478}[]{#_Toc383006974}[]{#_Toc383529653}[]{#_Toc387072302}[]{#_Toc382814903}[]{#_Toc382817391}[]{#_Toc382817887}[]{#_Toc382818381}[]{#_Toc383006479}[]{#_Toc383006975}[]{#_Toc383529654}[]{#_Toc387072303}[]{#_Toc382814904}[]{#_Toc382817392}[]{#_Toc382817888}[]{#_Toc382818382}[]{#_Toc383006480}[]{#_Toc383006976}[]{#_Toc383529655}[]{#_Toc387072304}[]{#_Toc382814905}[]{#_Toc382817393}[]{#_Toc382817889}[]{#_Toc382818383}[]{#_Toc383006481}[]{#_Toc383006977}[]{#_Toc383529656}[]{#_Toc387072305}[]{#_Toc382814906}[]{#_Toc382817394}[]{#_Toc382817890}[]{#_Toc382818384}[]{#_Toc383006482}[]{#_Toc383006978}[]{#_Toc383529657}[]{#_Toc387072306}[]{#_Toc382814907}[]{#_Toc382817395}[]{#_Toc382817891}[]{#_Toc382818385}[]{#_Toc383006483}[]{#_Toc383006979}[]{#_Toc383529658}[]{#_Toc387072307}[]{#_Toc382814908}[]{#_Toc382817396}[]{#_Toc382817892}[]{#_Toc382818386}[]{#_Toc383006484}[]{#_Toc383006980}[]{#_Toc383529659}[]{#_Toc387072308}[]{#_Toc382814909}[]{#_Toc382817397}[]{#_Toc382817893}[]{#_Toc382818387}[]{#_Toc383006485}[]{#_Toc383006981}[]{#_Toc383529660}[]{#_Toc387072309}[]{#_Toc382814910}[]{#_Toc382817398}[]{#_Toc382817894}[]{#_Toc382818388}[]{#_Toc383006486}[]{#_Toc383006982}[]{#_Toc383529661}[]{#_Toc387072310}[]{#_Toc382814911}[]{#_Toc382817399}[]{#_Toc382817895}[]{#_Toc382818389}[]{#_Toc383006487}[]{#_Toc383006983}[]{#_Toc383529662}[]{#_Toc387072311}[]{#_Toc382814912}[]{#_Toc382817400}[]{#_Toc382817896}[]{#_Toc382818390}[]{#_Toc383006488}[]{#_Toc383006984}[]{#_Toc383529663}[]{#_Toc387072312}[]{#_Toc382814913}[]{#_Toc382817401}[]{#_Toc382817897}[]{#_Toc382818391}[]{#_Toc383006489}[]{#_Toc383006985}[]{#_Toc383529664}[]{#_Toc387072313}[]{#_Toc382814915}[]{#_Toc382817403}[]{#_Toc382817899}[]{#_Toc382818393}[]{#_Toc383006491}[]{#_Toc383006987}[]{#_Toc383529666}[]{#_Toc387072315}[]{#_Toc382814916}[]{#_Toc382817404}[]{#_Toc382817900}[]{#_Toc382818394}[]{#_Toc383006492}[]{#_Toc383006988}[]{#_Toc383529667}[]{#_Toc387072316}[]{#_Toc382814917}[]{#_Toc382817405}[]{#_Toc382817901}[]{#_Toc382818395}[]{#_Toc383006493}[]{#_Toc383006989}[]{#_Toc383529668}[]{#_Toc387072317}[]{#_Toc382814918}[]{#_Toc382817406}[]{#_Toc382817902}[]{#_Toc382818396}[]{#_Toc383006494}[]{#_Toc383006990}[]{#_Toc383529669}[]{#_Toc387072318}[]{#_Toc382814919}[]{#_Toc382817407}[]{#_Toc382817903}[]{#_Toc382818397}[]{#_Toc383006495}[]{#_Toc383006991}[]{#_Toc383529670}[]{#_Toc387072319}[]{#_Toc382814920}[]{#_Toc382817408}[]{#_Toc382817904}[]{#_Toc382818398}[]{#_Toc383006496}[]{#_Toc383006992}[]{#_Toc383529671}[]{#_Toc387072320}[]{#_Toc382814921}[]{#_Toc382817409}[]{#_Toc382817905}[]{#_Toc382818399}[]{#_Toc383006497}[]{#_Toc383006993}[]{#_Toc383529672}[]{#_Toc387072321}[]{#_Toc382814922}[]{#_Toc382817410}[]{#_Toc382817906}[]{#_Toc382818400}[]{#_Toc383006498}[]{#_Toc383006994}[]{#_Toc383529673}[]{#_Toc387072322}[]{#_Toc382814923}[]{#_Toc382817411}[]{#_Toc382817907}[]{#_Toc382818401}[]{#_Toc383006499}[]{#_Toc383006995}[]{#_Toc383529674}[]{#_Toc387072323}[]{#_Toc382814924}[]{#_Toc382817412}[]{#_Toc382817908}[]{#_Toc382818402}[]{#_Toc383006500}[]{#_Toc383006996}[]{#_Toc383529675}[]{#_Toc387072324}[]{#_Toc382814927}[]{#_Toc382817415}[]{#_Toc382817911}[]{#_Toc382818405}[]{#_Toc383006503}[]{#_Toc383006999}[]{#_Toc383529678}[]{#_Toc387072327}[]{#_Toc382814928}[]{#_Toc382817416}[]{#_Toc382817912}[]{#_Toc382818406}[]{#_Toc383006504}[]{#_Toc383007000}[]{#_Toc383529679}[]{#_Toc387072328}[]{#_Toc382814929}[]{#_Toc382817417}[]{#_Toc382817913}[]{#_Toc382818407}[]{#_Toc383006505}[]{#_Toc383007001}[]{#_Toc383529680}[]{#_Toc387072329}[]{#_Toc382814930}[]{#_Toc382817418}[]{#_Toc382817914}[]{#_Toc382818408}[]{#_Toc383006506}[]{#_Toc383007002}[]{#_Toc383529681}[]{#_Toc387072330}[]{#_Toc382814931}[]{#_Toc382817419}[]{#_Toc382817915}[]{#_Toc382818409}[]{#_Toc383006507}[]{#_Toc383007003}[]{#_Toc383529682}[]{#_Toc387072331}[]{#_Toc382814932}[]{#_Toc382817420}[]{#_Toc382817916}[]{#_Toc382818410}[]{#_Toc383006508}[]{#_Toc383007004}[]{#_Toc383529683}[]{#_Toc387072332}[]{#_Toc382814933}[]{#_Toc382817421}[]{#_Toc382817917}[]{#_Toc382818411}[]{#_Toc383006509}[]{#_Toc383007005}[]{#_Toc383529684}[]{#_Toc387072333}[]{#_Toc382814934}[]{#_Toc382817422}[]{#_Toc382817918}[]{#_Toc382818412}[]{#_Toc383006510}[]{#_Toc383007006}[]{#_Toc383529685}[]{#_Toc387072334}[]{#_Toc382814935}[]{#_Toc382817423}[]{#_Toc382817919}[]{#_Toc382818413}[]{#_Toc383006511}[]{#_Toc383007007}[]{#_Toc383529686}[]{#_Toc387072335}[]{#_Toc382814936}[]{#_Toc382817424}[]{#_Toc382817920}[]{#_Toc382818414}[]{#_Toc383006512}[]{#_Toc383007008}[]{#_Toc383529687}[]{#_Toc387072336}[]{#_Toc382814937}[]{#_Toc382817425}[]{#_Toc382817921}[]{#_Toc382818415}[]{#_Toc383006513}[]{#_Toc383007009}[]{#_Toc383529688}[]{#_Toc387072337}[]{#_Toc382814938}[]{#_Toc382817426}[]{#_Toc382817922}[]{#_Toc382818416}[]{#_Toc383006514}[]{#_Toc383007010}[]{#_Toc383529689}[]{#_Toc387072338}[]{#_Toc382814939}[]{#_Toc382817427}[]{#_Toc382817923}[]{#_Toc382818417}[]{#_Toc383006515}[]{#_Toc383007011}[]{#_Toc383529690}[]{#_Toc387072339}[]{#_Toc382814940}[]{#_Toc382817428}[]{#_Toc382817924}[]{#_Toc382818418}[]{#_Toc383006516}[]{#_Toc383007012}[]{#_Toc383529691}[]{#_Toc387072340}[]{#_Toc382814941}[]{#_Toc382817429}[]{#_Toc382817925}[]{#_Toc382818419}[]{#_Toc383006517}[]{#_Toc383007013}[]{#_Toc383529692}[]{#_Toc387072341}[]{#_Toc382814942}[]{#_Toc382817430}[]{#_Toc382817926}[]{#_Toc382818420}[]{#_Toc383006518}[]{#_Toc383007014}[]{#_Toc383529693}[]{#_Toc387072342}[]{#_Toc382814943}[]{#_Toc382817431}[]{#_Toc382817927}[]{#_Toc382818421}[]{#_Toc383006519}[]{#_Toc383007015}[]{#_Toc383529694}[]{#_Toc387072343}[]{#_Toc382814944}[]{#_Toc382817432}[]{#_Toc382817928}[]{#_Toc382818422}[]{#_Toc383006520}[]{#_Toc383007016}[]{#_Toc383529695}[]{#_Toc387072344}[]{#_Toc382814945}[]{#_Toc382817433}[]{#_Toc382817929}[]{#_Toc382818423}[]{#_Toc383006521}[]{#_Toc383007017}[]{#_Toc383529696}[]{#_Toc387072345}[]{#_Toc382814946}[]{#_Toc382817434}[]{#_Toc382817930}[]{#_Toc382818424}[]{#_Toc383006522}[]{#_Toc383007018}[]{#_Toc383529697}[]{#_Toc387072346}[]{#_Toc382814947}[]{#_Toc382817435}[]{#_Toc382817931}[]{#_Toc382818425}[]{#_Toc383006523}[]{#_Toc383007019}[]{#_Toc383529698}[]{#_Toc387072347}[]{#_Toc382814948}[]{#_Toc382817436}[]{#_Toc382817932}[]{#_Toc382818426}[]{#_Toc383006524}[]{#_Toc383007020}[]{#_Toc383529699}[]{#_Toc387072348}[]{#_Toc382814949}[]{#_Toc382817437}[]{#_Toc382817933}[]{#_Toc382818427}[]{#_Toc383006525}[]{#_Toc383007021}[]{#_Toc383529700}[]{#_Toc387072349}[]{#_Toc382814950}[]{#_Toc382817438}[]{#_Toc382817934}[]{#_Toc382818428}[]{#_Toc383006526}[]{#_Toc383007022}[]{#_Toc383529701}[]{#_Toc387072350}[]{#_Toc382814951}[]{#_Toc382817439}[]{#_Toc382817935}[]{#_Toc382818429}[]{#_Toc383006527}[]{#_Toc383007023}[]{#_Toc383529702}[]{#_Toc387072351}[]{#_Toc382814952}[]{#_Toc382817440}[]{#_Toc382817936}[]{#_Toc382818430}[]{#_Toc383006528}[]{#_Toc383007024}[]{#_Toc383529703}[]{#_Toc387072352}[]{#_Toc382814953}[]{#_Toc382817441}[]{#_Toc382817937}[]{#_Toc382818431}[]{#_Toc383006529}[]{#_Toc383007025}[]{#_Toc383529704}[]{#_Toc387072353}[]{#_Toc382814954}[]{#_Toc382817442}[]{#_Toc382817938}[]{#_Toc382818432}[]{#_Toc383006530}[]{#_Toc383007026}[]{#_Toc383529705}[]{#_Toc387072354}[]{#_Toc382814957}[]{#_Toc382817445}[]{#_Toc382817941}[]{#_Toc382818435}[]{#_Toc383006533}[]{#_Toc383007029}[]{#_Toc383529708}[]{#_Toc387072357}[]{#_Toc382814958}[]{#_Toc382817446}[]{#_Toc382817942}[]{#_Toc382818436}[]{#_Toc383006534}[]{#_Toc383007030}[]{#_Toc383529709}[]{#_Toc387072358}[]{#_Toc382814959}[]{#_Toc382817447}[]{#_Toc382817943}[]{#_Toc382818437}[]{#_Toc383006535}[]{#_Toc383007031}[]{#_Toc383529710}[]{#_Toc387072359}[]{#_Toc382814960}[]{#_Toc382817448}[]{#_Toc382817944}[]{#_Toc382818438}[]{#_Toc383006536}[]{#_Toc383007032}[]{#_Toc383529711}[]{#_Toc387072360}[]{#_Toc382814961}[]{#_Toc382817449}[]{#_Toc382817945}[]{#_Toc382818439}[]{#_Toc383006537}[]{#_Toc383007033}[]{#_Toc383529712}[]{#_Toc387072361}[]{#_Toc382814962}[]{#_Toc382817450}[]{#_Toc382817946}[]{#_Toc382818440}[]{#_Toc383006538}[]{#_Toc383007034}[]{#_Toc383529713}[]{#_Toc387072362}[]{#_Toc382814963}[]{#_Toc382817451}[]{#_Toc382817947}[]{#_Toc382818441}[]{#_Toc383006539}[]{#_Toc383007035}[]{#_Toc383529714}[]{#_Toc387072363}[]{#_Toc382814964}[]{#_Toc382817452}[]{#_Toc382817948}[]{#_Toc382818442}[]{#_Toc383006540}[]{#_Toc383007036}[]{#_Toc383529715}[]{#_Toc387072364}[]{#_Toc382814965}[]{#_Toc382817453}[]{#_Toc382817949}[]{#_Toc382818443}[]{#_Toc383006541}[]{#_Toc383007037}[]{#_Toc383529716}[]{#_Toc387072365}[]{#_Toc382814966}[]{#_Toc382817454}[]{#_Toc382817950}[]{#_Toc382818444}[]{#_Toc383006542}[]{#_Toc383007038}[]{#_Toc383529717}[]{#_Toc387072366}[]{#_Toc382814967}[]{#_Toc382817455}[]{#_Toc382817951}[]{#_Toc382818445}[]{#_Toc383006543}[]{#_Toc383007039}[]{#_Toc383529718}[]{#_Toc387072367}[]{#_Toc382814968}[]{#_Toc382817456}[]{#_Toc382817952}[]{#_Toc382818446}[]{#_Toc383006544}[]{#_Toc383007040}[]{#_Toc383529719}[]{#_Toc387072368}[]{#_Toc401850369}

**Event MIB \-- Event MIB配置命令 \-- object list owner (Trigger-boolean view)**

------------------------------------------------------------------------

[**[object list owner]{lang="EN-US"}**]{#struct_0_x1862_90986_133651354}[命令用来指定绑定对象组，表示监控对象值满足]{style="font-family:宋体"}[Boolean]{lang="EN-US"}[检测条件且触发事件为]{style="font-family:宋体"}[Notification]{lang="EN-US"}[时，需要添加此绑定对象组中的绑定变量。]{style="font-family:宋体"}

[**[undo object list]{lang="EN-US"}**]{#struct_0_x1862_90986_x1836021489}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x36441064}

[**[object list owner ]{lang="EN-US"}***[objects-owner]{lang="EN-US"}***[ name ]{lang="EN-US"}***[objects-name]{lang="EN-US"}*]{#struct_0_x1862_90986_x832364216}

[**[undo object list]{lang="EN-US"}**]{#struct_0_x1862_90986_x714862649}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x144119322}

[[没有指定绑定对象组。]{style="font-family:宋体"}]{#struct_0_x1862_90986_x44094916}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x261280992}

[[T]{lang="EN-US"}]{#struct_0_x1862_90986_x341368679}[rigger]{lang="EN-US"}[-boolean]{lang="EN-US"}[视图]{style="font-family:
宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x700860980}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x393416211}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x149023050}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1859019830}

[*[objects-owner]{lang="EN-US"}*]{#struct_0_x1862_90986_x472353922}[：指定]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[绑定对象组的所有者，与]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[表中配置的]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[所有者]{style="font-family:宋体"}[owner]{lang="EN-US"}[相同。]{style="font-family:宋体"}

[*[objects-name]{lang="EN-US"}*]{#struct_0_x1862_90986_x856197445}[：指定]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[绑定对象组名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_358465989}

[[参考]{style="font-family:宋体"}[Trigger]{lang="EN-US"}]{#struct_0_x1862_90986_x1399243027}[视图下的]{style="font-family:宋体"}**[object list]{lang="EN-US"}**[ **owner**]{lang="EN-US"}[命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_79307202}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_x299629421}[配置绑定对象组，指定]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[绑定对象组的所有者为]{style="font-family:宋体"}[owner1]{lang="EN-US"}[，绑定对象组名称为]{style="font-family:宋体"}[objectA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1862_90986_1509887218}

[\[Sysname\] snmp mib event trigger owner owner1 name triggerA]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA\] test boolean]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA-boolean\] object list owner owner1 name objectA]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1099661491}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event trigger]{lang="EN-US"}**]{#struct_0_x1862_90986_1991566295}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[test ]{lang="EN-US"}**]{#struct_0_x1862_90986_1628586313}
:::

::: {#-78134460 .myid}
[]{#_Toc404797072}[]{#struct_0_x1862_90986_915425797}[]{#_Toc366652162}

**Event MIB \-- Event MIB配置命令 \-- object list owner (Trigger-existence view)**

------------------------------------------------------------------------

[**[object list owner]{lang="EN-US"}**]{#struct_0_x1862_90986_x607317345}[命令用来指定绑定对象组，表示监控对象值满足]{style="font-family:宋体"}[Existence]{lang="EN-US"}[检测条件且触发事件为]{style="font-family:宋体"}[Notification]{lang="EN-US"}[时，需要添加此绑定对象组中的绑定变量。]{style="font-family:宋体"}

[**[undo object list]{lang="EN-US"}**]{#struct_0_x1862_90986_x1715106991}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_611862485}

[**[object list owner ]{lang="EN-US"}***[objects-owner]{lang="EN-US"}***[ name ]{lang="EN-US"}***[objects-name]{lang="EN-US"}*]{#struct_0_x1862_90986_1511307491}

[**[undo object list]{lang="EN-US"}**]{#struct_0_x1862_90986_x1283425831}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x428783541}

[[没有指定绑定对象组。]{style="font-family:宋体"}]{#struct_0_x1862_90986_1435197256}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x2018003152}

[[Trigger-existence]{lang="EN-US"}]{#struct_0_x1862_90986_817596492}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x528539099}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x1133045070}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x916797767}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x508213415}

[*[objects-owner]{lang="EN-US"}*]{#struct_0_x1862_90986_1155431461}[：]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[绑定对象组的所有者，与]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[表中配置的]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[所有者]{style="font-family:宋体"}[owner]{lang="EN-US"}[相同。]{style="font-family:宋体"}

[*[objects-name]{lang="EN-US"}*]{#struct_0_x1862_90986_x662654992}[：]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[绑定对象组名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1588524026}

[[参考]{style="font-family:宋体"}[Trigger]{lang="EN-US"}]{#struct_0_x1862_90986_1013776364}[视图下的]{style="font-family:宋体"}**[object list owner]{lang="EN-US"}**[命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_236842496}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_1547639353}[当监控对象值满足]{style="font-family:宋体"}[Trigger-existence]{lang="EN-US"}[测试条件后，系统执行]{style="font-family:宋体"}[Notification]{lang="EN-US"}[动作并发送]{style="font-family:宋体"}[Trap]{lang="EN-US"}[时需要绑定的对象组。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1862_90986_343891203}

[\[Sysname\] snmp mib event trigger owner owner1 name triggerA]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA\] test existence]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA-existence\] object list owner owner1 name objectA]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1541016405}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event trigger]{lang="EN-US"}**]{#struct_0_x1862_90986_1060061353}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[test ]{lang="EN-US"}**]{#struct_0_x1862_90986_x1015101334}
:::

::: {#-593866891 .myid}
[]{#_Toc404797073}[]{#struct_0_x1862_90986_1818414087}

**Event MIB \-- Event MIB配置命令 \-- object list owner (Trigger-threshold view)**

------------------------------------------------------------------------

[**[object]{lang="EN-US"}**[ ]{lang="EN-US"}**[list]{lang="EN-US"}**[ ]{lang="EN-US"}**[owner]{lang="EN-US"}**[ ]{lang="EN-US"}**[name]{lang="EN-US"}**]{#struct_0_x1862_90986_692311829}[命令用来指定绑定对象组，表示监控对象值满足]{style="font-family:宋体"}[Threshold]{lang="EN-US"}[检测条件且触发事件为]{style="font-family:宋体"}[Notification]{lang="EN-US"}[时，需要添加此绑定对象组中的绑定变量。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[object]{lang="EN-US"}**[ ]{lang="EN-US"}**[list]{lang="EN-US"}**]{#struct_0_x1862_90986_484555481}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1141595273}

[**[object]{lang="EN-US"}**[ ]{lang="EN-US"}**[list]{lang="EN-US"}**[ ]{lang="EN-US"}**[owner]{lang="EN-US"}**[ ]{lang="EN-US"}*[objects-owner]{lang="EN-US"}*[ ]{lang="EN-US"}**[name]{lang="EN-US"}**[ ]{lang="EN-US"}*[objects-name]{lang="EN-US"}*]{#struct_0_x1862_90986_226157917}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[object]{lang="EN-US"}**[ ]{lang="EN-US"}**[list]{lang="EN-US"}**]{#struct_0_x1862_90986_x722462926}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x552307577}

[[没有指定绑定对象组。]{style="font-family:宋体"}]{#struct_0_x1862_90986_x382287357}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x70082028}

[[Trigger-threshold]{lang="EN-US"}]{#struct_0_x1862_90986_x1573260819}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_296958263}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_1879584929}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x169539890}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_188215537}

[*[objects-owner]{lang="EN-US"}*]{#struct_0_x1862_90986_1954201181}[：]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[绑定对象组的所有者，与]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[表中配置的]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[所有者]{style="font-family:宋体"}[owner]{lang="EN-US"}[相同。]{style="font-family:宋体"}

[*[objects-name]{lang="EN-US"}*]{#struct_0_x1862_90986_624930992}[：]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[绑定对象组名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1089716445}

[[参考]{style="font-family:宋体"}[Trigger]{lang="EN-US"}]{#struct_0_x1862_90986_x1769312290}[视图下的]{style="font-family:宋体"}**[object list owner]{lang="EN-US"}**[命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x585341165}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_x2118391518}[配置对应的绑定对象组。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1862_90986_1511285106}

[\[Sysname\] snmp mib event trigger owner owner1 name triggerA]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA\] test threshold]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA-threshold\] object list owner owner1 name objectA]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1718656201}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event trigger]{lang="EN-US"}**]{#struct_0_x1862_90986_1878040044}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[test]{lang="EN-US"}**]{#struct_0_x1862_90986_1801598219}
:::

::: {#-542762417 .myid}
[]{#_Toc404797074}[]{#struct_0_x1862_90986_1495779360}[]{#_Toc366652185}

**Event MIB \-- Event MIB配置命令 \-- object list owner (Action-notification view)**

------------------------------------------------------------------------

[**[object list owner]{lang="EN-US"}**]{#struct_0_x1862_90986_x692306209}[命令用来指定绑定对象组，表示触发]{style="font-family:宋体"}[Notification]{lang="EN-US"}[事件时，需要在此绑定对象组中添加的绑定变量。]{style="font-family:宋体"}

[**[undo object list]{lang="EN-US"}**]{#struct_0_x1862_90986_402919193}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1036020968}

[**[object list owner ]{lang="EN-US"}***[objects-owner]{lang="EN-US"}***[ name ]{lang="EN-US"}***[objects-name]{lang="EN-US"}*]{#struct_0_x1862_90986_606942142}

[**[undo object list]{lang="EN-US"}**]{#struct_0_x1862_90986_x1545229728}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x392097872}

[[没有指定绑定对象组。]{style="font-family:宋体"}]{#struct_0_x1862_90986_110860761}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x907247240}

[[Action-notification]{lang="EN-US"}]{#struct_0_x1862_90986_610491837}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_2087562213}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_2038071773}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_325293062}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x60089494}

[*[objects-owner]{lang="EN-US"}*]{#struct_0_x1862_90986_2142946381}[：配置绑定对象的所有者，与对应]{style="font-family:宋体"}[Event]{lang="EN-US"}[配置的]{style="font-family:宋体"}[owner]{lang="EN-US"}[相同。]{style="font-family:宋体"}

[*[objects-name]{lang="EN-US"}*]{#struct_0_x1862_90986_x1828095390}[：配置绑定对象组名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1070055203}

[[本命令用来配置发送]{style="font-family:宋体"}[Notification]{lang="EN-US"}]{#struct_0_x1862_90986_x884567336}[时附加的引用]{style="font-family:宋体"}[Object]{lang="EN-US"}[表中的绑定对象组所包含的绑定变量，若不指定或者指定的绑定对象组为空，则不添加绑定变量。关于发送]{style="font-family:宋体"}[Notification]{lang="EN-US"}[的绑定变量描述请参见]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[视图下的]{style="font-family:宋体"}**[object list owner name]{lang="EN-US"}**[的命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_286827163}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_2078653347}[配置事件所有者为]{style="font-family:宋体"}[owner1 ]{lang="EN-US"}[，事件名为]{style="font-family:宋体"}[EventA]{lang="EN-US"}[，绑定对象组名为]{style="font-family:宋体"}[listA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname\] snmp mib event owner owner1 name EventA]{lang="EN-US"}]{#struct_0_x1862_90986_1692966247}

[\[Sysname-event-owner1-EventA\] action notification]{lang="EN-US"}

[\[Sysname-event-owner1-EventA-notification\] object list owner owner1 name listA]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_415514815}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event owner]{lang="EN-US"}**]{#struct_0_x1862_90986_x1668052824}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[action]{lang="EN-US"}**]{#struct_0_x1862_90986_x610218609}
:::

::: {#-1439075067 .myid}
[]{#_Toc404797075}[]{#struct_0_x1862_90986_x461932846}

**Event MIB \-- Event MIB配置命令 \-- oid (Trigger view)**

------------------------------------------------------------------------

[**[oid]{lang="EN-US"}**]{#struct_0_x1862_90986_x1267201317}[命令用来配置]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[采样的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[节点。]{style="font-family:宋体"}

[**[undo oid]{lang="EN-US"}**]{#struct_0_x1862_90986_x140619193}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x197383414}

[**[oid ]{lang="EN-US"}***[object-identifier]{lang="EN-US"}*]{#struct_0_x1862_90986_16893940}

[**[undo oid ]{lang="EN-US"}**]{#struct_0_x1862_90986_1808939556}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1717713979}

[[OID]{lang="EN-US"}]{#struct_0_x1862_90986_1295951595}[为]{style="font-family:宋体"}[0.0]{lang="EN-US"}[，]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[没有配置]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[采样的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[节点，即没有指定]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[的监控对象。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_175825652}

[[Trigger]{lang="EN-US"}]{#struct_0_x1862_90986_x971085394}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1360830621}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_1060830531}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_175264453}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x939765151}

[*[object-identifier]{lang="EN-US"}*]{#struct_0_x1862_90986_x155149396}[：]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[进行采样的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[节点，即]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[的监控对象。取值为节点]{style="font-family:宋体"}[OID]{lang="EN-US"}[或者节点名称。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1260593724}

[[该命令用来指定]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_x1862_90986_x765873928}[节点作为监控对象，当配置该命令后，该]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[生效时将按指定的采样间隔周期性地获取该监控对象的值用来判定是否满足事件触发条件。]{style="font-family:宋体"}

[[配置的]{style="font-family:宋体"}[OID]{lang="EN-US"}]{#struct_0_x1862_90986_x704938086}[可以是表节点，概念行节点，表中列节点，简单叶子节点，叶节点的父节点中的任意一种。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x301951322}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_660760160}[配置]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[采样的节点值为]{style="font-family:宋体"}[1.3.6.1.2.1.2.2.1.1.3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1862_90986_x2102560295}

[\[Sysname\] snmp mib event trigger owner owner1 name triggerA]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA\] oid 1.3.6.1.2.1.2.2.1.1.3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_234225031}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event trigger]{lang="EN-US"}**]{#struct_0_x1862_90986_x1311756928}
:::

::: {#2085872373 .myid}
[]{#_Toc404797076}[]{#struct_0_x1862_90986_x1050388213}[]{#_Toc401850375}

**Event MIB \-- Event MIB配置命令 \-- oid (Action-set view)**

------------------------------------------------------------------------

[**[oid]{lang="EN-US"}**]{#struct_0_x1862_90986_154787209}[命令用来配置事件]{style="font-family:宋体"}[Set]{lang="EN-US"}[操作对象的]{style="font-family:宋体"}[OID]{lang="EN-US"}[值。]{style="font-family:宋体"}

[**[undo oid]{lang="EN-US"}**]{#struct_0_x1862_90986_x1173136992}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x85585034}

[**[oid ]{lang="EN-US"}***[object-identifier]{lang="EN-US"}*]{#struct_0_x1862_90986_49214217}

[**[undo oid]{lang="EN-US"}**]{#struct_0_x1862_90986_x429352929}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1431824943}

[[OID]{lang="EN-US"}]{#struct_0_x1862_90986_x928169557}[为]{style="font-family:宋体"}[0.0]{lang="EN-US"}[，表示没有指定]{style="font-family:宋体"}[Set]{lang="EN-US"}[操作对象。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1219566149}

[[Action-set]{lang="EN-US"}]{#struct_0_x1862_90986_1621487028}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1069989570}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_45032043}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_1417126427}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1840976326}

[*[object-identifier]{lang="EN-US"}*]{#struct_0_x1862_90986_1276196299}[：]{style="font-family:宋体"}[Set]{lang="EN-US"}[操作对象的]{style="font-family:宋体"}[OID]{lang="EN-US"}[，取值为节点]{style="font-family:宋体"}[OID]{lang="EN-US"}[值或者节点名称。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_129167491}

[[配置的]{style="font-family:宋体"}[OID]{lang="EN-US"}]{#struct_0_x1862_90986_x1888671018}[的值必须为表节点，概念行节点，表中列节点，简单叶子节点，叶节点的父节点中的任意一种。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1100816488}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_x363983840}[设置用户名]{style="font-family:宋体"}[owner1]{lang="EN-US"}[，事件名为]{style="font-family:宋体"}[EventA]{lang="EN-US"}[的]{style="font-family:宋体"}[set]{lang="EN-US"}[对象的]{style="font-family:宋体"}[OID]{lang="EN-US"}[为]{style="font-family:宋体"}[1.3.6.1.2.1.2.2.1.7.3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1862_90986_1651867510}

[\[Sysname\] snmp mib event owner owner1 name EventA]{lang="EN-US"}

[\[Sysname-event-owner1-EventA\] action set]{lang="EN-US"}

[\[Sysname-event-owner1-EventA-set\] oid 1.3.6.1.2.1.2.2.1.7.3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x168037428}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event owner]{lang="EN-US"}**]{#struct_0_x1862_90986_954290335}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[action]{lang="EN-US"}**]{#struct_0_x1862_90986_x1348604370}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[wildcard oid]{lang="EN-US"}**]{#struct_0_x1862_90986_x1072515479}**[ ]{lang="EN-US"}**[(Action-set view)]{lang="EN-US"}
:::

::: {#147911607 .myid}
[]{#_Toc404797077}[]{#struct_0_x1862_90986_x113938048}

**Event MIB \-- Event MIB配置命令 \-- oid (Action-notification view)**

------------------------------------------------------------------------

[**[oid]{lang="EN-US"}**]{#struct_0_x1862_90986_1954183126}[命令用来配置执行]{style="font-family:宋体"}[Notification]{lang="EN-US"}[事件时需要发送的]{style="font-family:宋体"}[Notification]{lang="EN-US"}[的]{style="font-family:宋体"}[OID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo oid]{lang="EN-US"}**]{#struct_0_x1862_90986_x148957514}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_880724653}

[**[oid ]{lang="EN-US"}***[object-identifier]{lang="EN-US"}*]{#struct_0_x1862_90986_x408672530}

[**[undo oid]{lang="EN-US"}**]{#struct_0_x1862_90986_983959659}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1086437021}

[[OID]{lang="EN-US"}]{#struct_0_x1862_90986_706884149}[为]{style="font-family:宋体"}[0.0]{lang="EN-US"}[，]{style="font-family:宋体"}[表示没有指定发送]{style="font-family:宋体"}[Notification]{lang="EN-US"}[的]{style="font-family:宋体"}[OID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1961406432}

[[Action-notification]{lang="EN-US"}]{#struct_0_x1862_90986_x1894117653}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_359041505}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x1886081404}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x44168387}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x595288842}

[*[object-identifier]{lang="EN-US"}*]{#struct_0_x1862_90986_x2067234650}[：指定发送]{style="font-family:宋体"}[Notificaton]{lang="EN-US"}[的]{style="font-family:宋体"}[OID]{lang="EN-US"}[值，此]{style="font-family:宋体"}[OID]{lang="EN-US"}[对应的节点必须为告警节点。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1320366612}

[[本命令用于配置事件类型为]{style="font-family:宋体"}[Notification]{lang="EN-US"}]{#struct_0_x1862_90986_x1715041455}[时需要发送具体]{style="font-family:宋体"}[Notification]{lang="EN-US"}[的]{style="font-family:宋体"}[OID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x2068974520}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_731730526}[设置用户名为]{style="font-family:宋体"}[owner1]{lang="EN-US"}[，事件名为]{style="font-family:宋体"}[EventA]{lang="EN-US"}[发送的]{style="font-family:宋体"}[notificaton]{lang="EN-US"}[的]{style="font-family:宋体"}[OID]{lang="EN-US"}[为]{style="font-family:宋体"}[1.3.6.1.2.1.14.16.2.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1862_90986_1204570385}

[\[Sysname\] snmp mib event owner owner1 name EventA]{lang="EN-US"}

[\[Sysname-event-owner1-EventA\] action notification]{lang="EN-US"}

[\[Sysname-event-owner1-EventA-notification\] oid 1.3.6.1.2.1.14.16.2.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1797661519}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event owner ]{lang="EN-US"}**]{#struct_0_x1862_90986_x1589845040}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[action]{lang="EN-US"}**]{#struct_0_x1862_90986_x1801935597}
:::

::: {#-336967511 .myid}
[]{#_Toc404797078}[]{#struct_0_x1862_90986_1519614303}[]{#_Toc366652171}

**Event MIB \-- Event MIB配置命令 \-- rising**

------------------------------------------------------------------------

[**[rising]{lang="EN-US"}**]{#struct_0_x1862_90986_x1483286706}[命令用来配置绝对值采样类型的上限阈值，并指定采样值大于等于该阈值时触发的事件。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[rising]{lang="EN-US"}**]{#struct_0_x1862_90986_314274111}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x291327981}

[**[rising]{lang="EN-US"}**[ ]{lang="EN-US"}[{ **event** **owner** *event-owner* **name** *event-name* \| **value** *integer-value* }]{lang="EN-US"}]{#struct_0_x1862_90986_x1475831193}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[rising]{lang="EN-US"}**[ ]{lang="EN-US"}[{ **event** \| **value** }]{lang="EN-US"}]{#struct_0_x1862_90986_1013841900}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x500265086}

[[上限阈值为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x1862_90986_x268355650}[，未配置对应的触发事件。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x531929105}

[[Trigger-threshold]{lang="EN-US"}]{#struct_0_x1862_90986_353243956}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x550945445}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x1816613918}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x1099212313}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1559865065}

[**[event]{lang="EN-US"}**[ ]{lang="EN-US"}**[owner]{lang="EN-US"}***[ event-owner]{lang="EN-US"}*]{#struct_0_x1862_90986_1240056497}[：配置上限阈值事件的所有者，与]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[配置的]{style="font-family:宋体"}[owner]{lang="EN-US"}[相同。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}***[ event-name]{lang="EN-US"}*]{#struct_0_x1862_90986_x1221949397}[：配置上限阈值对应的事件名，为]{style="font-family:宋体"}[1\~32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[value]{lang="EN-US"}**[ ]{lang="EN-US"}*[integer-value]{lang="EN-US"}*]{#struct_0_x1862_90986_x948371084}[：绝对值采样的上限阈值，可以配置任意不小于下限阈值的整数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x989559408}

[[采样类型为绝对值采样时，采样值达到或超过上限阈值时，将触发对应的事件。]{style="font-family:宋体"}]{#struct_0_x1862_90986_1787827342}

[[若采样值连续多次达到或超过上限阈值，只会在第一次触发对应的事件，上限和下限对应事件的触发是交替产生的。]{style="font-family:宋体"}]{#struct_0_x1862_90986_x170601410}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x552242041}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_x1187706708}[配置]{style="font-family:宋体"}[threshold]{lang="EN-US"}[测试的上限阈值为]{style="font-family:宋体"}[50]{lang="EN-US"}[，对应的事件所有者为]{style="font-family:宋体"}[owner1]{lang="EN-US"}[，事件名为]{style="font-family:宋体"}[event1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1862_90986_x148747224}

[\[Sysname\] snmp mib event trigger owner owner1 name triggerA]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA\] test threshold]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA-threshold\] rising value 50 ]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA-threshold\] rising event owner owner1 name event1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1069233556}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event trigger]{lang="EN-US"}**]{#struct_0_x1862_90986_224020767}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[test ]{lang="EN-US"}**]{#struct_0_x1862_90986_1132457991}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sample]{lang="EN-US"}**]{#struct_0_x1862_90986_1731704525}
:::

::: {#741856984 .myid}
[]{#_Toc404797079}[]{#struct_0_x1862_90986_x511950261}

**Event MIB \-- Event MIB配置命令 \-- sample**

------------------------------------------------------------------------

[**[sample]{lang="EN-US"}**]{#struct_0_x1862_90986_1431819007}[命令用来配置]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[采样的类型。]{style="font-family:宋体"}

[**[undo sample]{lang="EN-US"}**]{#struct_0_x1862_90986_x1399503792}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x907632774}

[**[sample]{lang="EN-US"}**[ { **absolute** \| **delta** }]{lang="EN-US"}]{#struct_0_x1862_90986_x2118325982}

[**[undo sample]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1862_90986_1985904889}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_115886271}

[[Trigger]{lang="EN-US"}]{#struct_0_x1862_90986_1406876370}[采样类型为绝对值采样。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x436466659}

[[Trigger]{lang="EN-US"}]{#struct_0_x1862_90986_981989728}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x2016700344}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_1751764070}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x2004987332}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_369608610}

[**[absolute]{lang="EN-US"}**]{#struct_0_x1862_90986_x1421067936}[：[采样类型为绝对值采样，即采样时间到达时直接获取监控对象的值。]{style="color:black"}]{style="font-family:宋体"}

[**[delta]{lang="EN-US"}**]{#struct_0_x1862_90986_555840713}[：[采样类型为差值采样，即采样时间到达时获取的是监控对象本次与上次采样的差值。]{style="color:black"}]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1513219158}

[[采样类型为差值采样时，获取本次差值的算法与对应监控对象值类型有关。]{style="font-family:宋体"}]{#struct_0_x1862_90986_610557373}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果监控对象值类型为]{lang="EN-US" style="font-family:宋体"}[UINT]{lang="EN-US"}]{#struct_0_x1862_90986_929140994}[类型，则获取本次差值算法：本次采样值与前一次采样值比较，取两者中的较大值减去较小值，保证差值为正值（即也为]{lang="EN-US" style="font-family:宋体"}[UINT]{lang="EN-US"}[类型）；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果监控对象值类型为]{lang="EN-US" style="font-family:宋体"}[INT]{lang="EN-US"}]{#struct_0_x1862_90986_1292721242}[类型，则获取本次差值算法：当前采样值减去前一次采样值取差值。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1095426997}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_1923105126}[配置]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[采样的类型为绝对值采样。]{style="font-family:宋体"}

[[\<Sysname\>system-view]{lang="EN-US"}]{#struct_0_x1862_90986_x1425549842}

[\[Sysname\] snmp mib event trigger owner owner1 name triggerA]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA\] sample absolute]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1061651762}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event trigger]{lang="EN-US"}**]{#struct_0_x1862_90986_x611071969}
:::

::: {#-235638672 .myid}
[]{#_Toc404797080}[]{#struct_0_x1862_90986_x1177133797}[]{#_Toc382814982}[]{#_Toc382817470}[]{#_Toc382817966}[]{#_Toc382818460}[]{#_Toc383006558}[]{#_Toc383007054}[]{#_Toc383529733}[]{#_Toc387072382}[]{#_Toc382814983}[]{#_Toc382817471}[]{#_Toc382817967}[]{#_Toc382818461}[]{#_Toc383006559}[]{#_Toc383007055}[]{#_Toc383529734}[]{#_Toc387072383}[]{#_Toc382814984}[]{#_Toc382817472}[]{#_Toc382817968}[]{#_Toc382818462}[]{#_Toc383006560}[]{#_Toc383007056}[]{#_Toc383529735}[]{#_Toc387072384}[]{#_Toc382814985}[]{#_Toc382817473}[]{#_Toc382817969}[]{#_Toc382818463}[]{#_Toc383006561}[]{#_Toc383007057}[]{#_Toc383529736}[]{#_Toc387072385}[]{#_Toc382814986}[]{#_Toc382817474}[]{#_Toc382817970}[]{#_Toc382818464}[]{#_Toc383006562}[]{#_Toc383007058}[]{#_Toc383529737}[]{#_Toc387072386}[]{#_Toc382814987}[]{#_Toc382817475}[]{#_Toc382817971}[]{#_Toc382818465}[]{#_Toc383006563}[]{#_Toc383007059}[]{#_Toc383529738}[]{#_Toc387072387}[]{#_Toc382814988}[]{#_Toc382817476}[]{#_Toc382817972}[]{#_Toc382818466}[]{#_Toc383006564}[]{#_Toc383007060}[]{#_Toc383529739}[]{#_Toc387072388}[]{#_Toc382814989}[]{#_Toc382817477}[]{#_Toc382817973}[]{#_Toc382818467}[]{#_Toc383006565}[]{#_Toc383007061}[]{#_Toc383529740}[]{#_Toc387072389}[]{#_Toc382814990}[]{#_Toc382817478}[]{#_Toc382817974}[]{#_Toc382818468}[]{#_Toc383006566}[]{#_Toc383007062}[]{#_Toc383529741}[]{#_Toc387072390}[]{#_Toc382814991}[]{#_Toc382817479}[]{#_Toc382817975}[]{#_Toc382818469}[]{#_Toc383006567}[]{#_Toc383007063}[]{#_Toc383529742}[]{#_Toc387072391}[]{#_Toc382814993}[]{#_Toc382817481}[]{#_Toc382817977}[]{#_Toc382818471}[]{#_Toc383006569}[]{#_Toc383007065}[]{#_Toc383529744}[]{#_Toc387072393}[]{#_Toc382814994}[]{#_Toc382817482}[]{#_Toc382817978}[]{#_Toc382818472}[]{#_Toc383006570}[]{#_Toc383007066}[]{#_Toc383529745}[]{#_Toc387072394}[]{#_Toc382814995}[]{#_Toc382817483}[]{#_Toc382817979}[]{#_Toc382818473}[]{#_Toc383006571}[]{#_Toc383007067}[]{#_Toc383529746}[]{#_Toc387072395}[]{#_Toc382814996}[]{#_Toc382817484}[]{#_Toc382817980}[]{#_Toc382818474}[]{#_Toc383006572}[]{#_Toc383007068}[]{#_Toc383529747}[]{#_Toc387072396}[]{#_Toc382814997}[]{#_Toc382817485}[]{#_Toc382817981}[]{#_Toc382818475}[]{#_Toc383006573}[]{#_Toc383007069}[]{#_Toc383529748}[]{#_Toc387072397}[]{#_Toc382814998}[]{#_Toc382817486}[]{#_Toc382817982}[]{#_Toc382818476}[]{#_Toc383006574}[]{#_Toc383007070}[]{#_Toc383529749}[]{#_Toc387072398}[]{#_Toc382814999}[]{#_Toc382817487}[]{#_Toc382817983}[]{#_Toc382818477}[]{#_Toc383006575}[]{#_Toc383007071}[]{#_Toc383529750}[]{#_Toc387072399}[]{#_Toc382815000}[]{#_Toc382817488}[]{#_Toc382817984}[]{#_Toc382818478}[]{#_Toc383006576}[]{#_Toc383007072}[]{#_Toc383529751}[]{#_Toc387072400}[]{#_Toc382815001}[]{#_Toc382817489}[]{#_Toc382817985}[]{#_Toc382818479}[]{#_Toc383006577}[]{#_Toc383007073}[]{#_Toc383529752}[]{#_Toc387072401}[]{#_Toc382815002}[]{#_Toc382817490}[]{#_Toc382817986}[]{#_Toc382818480}[]{#_Toc383006578}[]{#_Toc383007074}[]{#_Toc383529753}[]{#_Toc387072402}[]{#_Toc382815003}[]{#_Toc382817491}[]{#_Toc382817987}[]{#_Toc382818481}[]{#_Toc383006579}[]{#_Toc383007075}[]{#_Toc383529754}[]{#_Toc387072403}[]{#_Toc382815004}[]{#_Toc382817492}[]{#_Toc382817988}[]{#_Toc382818482}[]{#_Toc383006580}[]{#_Toc383007076}[]{#_Toc383529755}[]{#_Toc387072404}[]{#_Toc382815005}[]{#_Toc382817493}[]{#_Toc382817989}[]{#_Toc382818483}[]{#_Toc383006581}[]{#_Toc383007077}[]{#_Toc383529756}[]{#_Toc387072405}[]{#_Toc382815006}[]{#_Toc382817494}[]{#_Toc382817990}[]{#_Toc382818484}[]{#_Toc383006582}[]{#_Toc383007078}[]{#_Toc383529757}[]{#_Toc387072406}[]{#_Toc382815007}[]{#_Toc382817495}[]{#_Toc382817991}[]{#_Toc382818485}[]{#_Toc383006583}[]{#_Toc383007079}[]{#_Toc383529758}[]{#_Toc387072407}[]{#_Toc382815008}[]{#_Toc382817496}[]{#_Toc382817992}[]{#_Toc382818486}[]{#_Toc383006584}[]{#_Toc383007080}[]{#_Toc383529759}[]{#_Toc387072408}[]{#_Toc382815009}[]{#_Toc382817497}[]{#_Toc382817993}[]{#_Toc382818487}[]{#_Toc383006585}[]{#_Toc383007081}[]{#_Toc383529760}[]{#_Toc387072409}[]{#_Toc401850380}[]{#_Toc382815011}[]{#_Toc382817499}[]{#_Toc382817995}[]{#_Toc382818489}[]{#_Toc383006587}[]{#_Toc383007083}[]{#_Toc383529762}[]{#_Toc387072411}[]{#_Toc382815012}[]{#_Toc382817500}[]{#_Toc382817996}[]{#_Toc382818490}[]{#_Toc383006588}[]{#_Toc383007084}[]{#_Toc383529763}[]{#_Toc387072412}[]{#_Toc382815013}[]{#_Toc382817501}[]{#_Toc382817997}[]{#_Toc382818491}[]{#_Toc383006589}[]{#_Toc383007085}[]{#_Toc383529764}[]{#_Toc387072413}[]{#_Toc382815014}[]{#_Toc382817502}[]{#_Toc382817998}[]{#_Toc382818492}[]{#_Toc383006590}[]{#_Toc383007086}[]{#_Toc383529765}[]{#_Toc387072414}[]{#_Toc382815016}[]{#_Toc382817504}[]{#_Toc382818000}[]{#_Toc382818494}[]{#_Toc383006592}[]{#_Toc383007088}[]{#_Toc383529767}[]{#_Toc387072416}[]{#_Toc382815017}[]{#_Toc382817505}[]{#_Toc382818001}[]{#_Toc382818495}[]{#_Toc383006593}[]{#_Toc383007089}[]{#_Toc383529768}[]{#_Toc387072417}[]{#_Toc382815018}[]{#_Toc382817506}[]{#_Toc382818002}[]{#_Toc382818496}[]{#_Toc383006594}[]{#_Toc383007090}[]{#_Toc383529769}[]{#_Toc387072418}[]{#_Toc382815019}[]{#_Toc382817507}[]{#_Toc382818003}[]{#_Toc382818497}[]{#_Toc383006595}[]{#_Toc383007091}[]{#_Toc383529770}[]{#_Toc387072419}[]{#_Toc382815020}[]{#_Toc382817508}[]{#_Toc382818004}[]{#_Toc382818498}[]{#_Toc383006596}[]{#_Toc383007092}[]{#_Toc383529771}[]{#_Toc387072420}[]{#_Toc382815021}[]{#_Toc382817509}[]{#_Toc382818005}[]{#_Toc382818499}[]{#_Toc383006597}[]{#_Toc383007093}[]{#_Toc383529772}[]{#_Toc387072421}[]{#_Toc382815023}[]{#_Toc382817511}[]{#_Toc382818007}[]{#_Toc382818501}[]{#_Toc383006599}[]{#_Toc383007095}[]{#_Toc383529774}[]{#_Toc387072423}[]{#_Toc382815024}[]{#_Toc382817512}[]{#_Toc382818008}[]{#_Toc382818502}[]{#_Toc383006600}[]{#_Toc383007096}[]{#_Toc383529775}[]{#_Toc387072424}[]{#_Toc382815025}[]{#_Toc382817513}[]{#_Toc382818009}[]{#_Toc382818503}[]{#_Toc383006601}[]{#_Toc383007097}[]{#_Toc383529776}[]{#_Toc387072425}[]{#_Toc382815026}[]{#_Toc382817514}[]{#_Toc382818010}[]{#_Toc382818504}[]{#_Toc383006602}[]{#_Toc383007098}[]{#_Toc383529777}[]{#_Toc387072426}[]{#_Toc382815027}[]{#_Toc382817515}[]{#_Toc382818011}[]{#_Toc382818505}[]{#_Toc383006603}[]{#_Toc383007099}[]{#_Toc383529778}[]{#_Toc387072427}[]{#_Toc382815028}[]{#_Toc382817516}[]{#_Toc382818012}[]{#_Toc382818506}[]{#_Toc383006604}[]{#_Toc383007100}[]{#_Toc383529779}[]{#_Toc387072428}[]{#_Toc382815029}[]{#_Toc382817517}[]{#_Toc382818013}[]{#_Toc382818507}[]{#_Toc383006605}[]{#_Toc383007101}[]{#_Toc383529780}[]{#_Toc387072429}[]{#_Toc382815030}[]{#_Toc382817518}[]{#_Toc382818014}[]{#_Toc382818508}[]{#_Toc383006606}[]{#_Toc383007102}[]{#_Toc383529781}[]{#_Toc387072430}[]{#_Toc382815031}[]{#_Toc382817519}[]{#_Toc382818015}[]{#_Toc382818509}[]{#_Toc383006607}[]{#_Toc383007103}[]{#_Toc383529782}[]{#_Toc387072431}[]{#_Toc382815032}[]{#_Toc382817520}[]{#_Toc382818016}[]{#_Toc382818510}[]{#_Toc383006608}[]{#_Toc383007104}[]{#_Toc383529783}[]{#_Toc387072432}[]{#_Toc382815033}[]{#_Toc382817521}[]{#_Toc382818017}[]{#_Toc382818511}[]{#_Toc383006609}[]{#_Toc383007105}[]{#_Toc383529784}[]{#_Toc387072433}[]{#_Toc382815034}[]{#_Toc382817522}[]{#_Toc382818018}[]{#_Toc382818512}[]{#_Toc383006610}[]{#_Toc383007106}[]{#_Toc383529785}[]{#_Toc387072434}[]{#_Toc382815035}[]{#_Toc382817523}[]{#_Toc382818019}[]{#_Toc382818513}[]{#_Toc383006611}[]{#_Toc383007107}[]{#_Toc383529786}[]{#_Toc387072435}[]{#_Toc382815039}[]{#_Toc382817527}[]{#_Toc382818023}[]{#_Toc382818517}[]{#_Toc383006615}[]{#_Toc383007111}[]{#_Toc383529790}[]{#_Toc387072439}[]{#_Toc382815040}[]{#_Toc382817528}[]{#_Toc382818024}[]{#_Toc382818518}[]{#_Toc383006616}[]{#_Toc383007112}[]{#_Toc383529791}[]{#_Toc387072440}[]{#_Toc382815041}[]{#_Toc382817529}[]{#_Toc382818025}[]{#_Toc382818519}[]{#_Toc383006617}[]{#_Toc383007113}[]{#_Toc383529792}[]{#_Toc387072441}[]{#_Toc382815042}[]{#_Toc382817530}[]{#_Toc382818026}[]{#_Toc382818520}[]{#_Toc383006618}[]{#_Toc383007114}[]{#_Toc383529793}[]{#_Toc387072442}[]{#_Toc382815044}[]{#_Toc382817532}[]{#_Toc382818028}[]{#_Toc382818522}[]{#_Toc383006620}[]{#_Toc383007116}[]{#_Toc383529795}[]{#_Toc387072444}[]{#_Toc382815045}[]{#_Toc382817533}[]{#_Toc382818029}[]{#_Toc382818523}[]{#_Toc383006621}[]{#_Toc383007117}[]{#_Toc383529796}[]{#_Toc387072445}[]{#_Toc382815046}[]{#_Toc382817534}[]{#_Toc382818030}[]{#_Toc382818524}[]{#_Toc383006622}[]{#_Toc383007118}[]{#_Toc383529797}[]{#_Toc387072446}[]{#_Toc382815047}[]{#_Toc382817535}[]{#_Toc382818031}[]{#_Toc382818525}[]{#_Toc383006623}[]{#_Toc383007119}[]{#_Toc383529798}[]{#_Toc387072447}[]{#_Toc382815048}[]{#_Toc382817536}[]{#_Toc382818032}[]{#_Toc382818526}[]{#_Toc383006624}[]{#_Toc383007120}[]{#_Toc383529799}[]{#_Toc387072448}[]{#_Toc382815050}[]{#_Toc382817538}[]{#_Toc382818034}[]{#_Toc382818528}[]{#_Toc383006626}[]{#_Toc383007122}[]{#_Toc383529801}[]{#_Toc387072450}[]{#_Toc382815051}[]{#_Toc382817539}[]{#_Toc382818035}[]{#_Toc382818529}[]{#_Toc383006627}[]{#_Toc383007123}[]{#_Toc383529802}[]{#_Toc387072451}[]{#_Toc382815052}[]{#_Toc382817540}[]{#_Toc382818036}[]{#_Toc382818530}[]{#_Toc383006628}[]{#_Toc383007124}[]{#_Toc383529803}[]{#_Toc387072452}[]{#_Toc382815053}[]{#_Toc382817541}[]{#_Toc382818037}[]{#_Toc382818531}[]{#_Toc383006629}[]{#_Toc383007125}[]{#_Toc383529804}[]{#_Toc387072453}[]{#_Toc382815054}[]{#_Toc382817542}[]{#_Toc382818038}[]{#_Toc382818532}[]{#_Toc383006630}[]{#_Toc383007126}[]{#_Toc383529805}[]{#_Toc387072454}[]{#_Toc382815055}[]{#_Toc382817543}[]{#_Toc382818039}[]{#_Toc382818533}[]{#_Toc383006631}[]{#_Toc383007127}[]{#_Toc383529806}[]{#_Toc387072455}[]{#_Toc382815056}[]{#_Toc382817544}[]{#_Toc382818040}[]{#_Toc382818534}[]{#_Toc383006632}[]{#_Toc383007128}[]{#_Toc383529807}[]{#_Toc387072456}[]{#_Toc382815057}[]{#_Toc382817545}[]{#_Toc382818041}[]{#_Toc382818535}[]{#_Toc383006633}[]{#_Toc383007129}[]{#_Toc383529808}[]{#_Toc387072457}[]{#_Toc382815058}[]{#_Toc382817546}[]{#_Toc382818042}[]{#_Toc382818536}[]{#_Toc383006634}[]{#_Toc383007130}[]{#_Toc383529809}[]{#_Toc387072458}[]{#_Toc382815059}[]{#_Toc382817547}[]{#_Toc382818043}[]{#_Toc382818537}[]{#_Toc383006635}[]{#_Toc383007131}[]{#_Toc383529810}[]{#_Toc387072459}[]{#_Toc382815060}[]{#_Toc382817548}[]{#_Toc382818044}[]{#_Toc382818538}[]{#_Toc383006636}[]{#_Toc383007132}[]{#_Toc383529811}[]{#_Toc387072460}[]{#_Toc382815061}[]{#_Toc382817549}[]{#_Toc382818045}[]{#_Toc382818539}[]{#_Toc383006637}[]{#_Toc383007133}[]{#_Toc383529812}[]{#_Toc387072461}[]{#_Toc382815062}[]{#_Toc382817550}[]{#_Toc382818046}[]{#_Toc382818540}[]{#_Toc383006638}[]{#_Toc383007134}[]{#_Toc383529813}[]{#_Toc387072462}[]{#_Toc382815063}[]{#_Toc382817551}[]{#_Toc382818047}[]{#_Toc382818541}[]{#_Toc383006639}[]{#_Toc383007135}[]{#_Toc383529814}[]{#_Toc387072463}[]{#_Toc382815064}[]{#_Toc382817552}[]{#_Toc382818048}[]{#_Toc382818542}[]{#_Toc383006640}[]{#_Toc383007136}[]{#_Toc383529815}[]{#_Toc387072464}[]{#_Toc382815065}[]{#_Toc382817553}[]{#_Toc382818049}[]{#_Toc382818543}[]{#_Toc383006641}[]{#_Toc383007137}[]{#_Toc383529816}[]{#_Toc387072465}[]{#_Toc382815066}[]{#_Toc382817554}[]{#_Toc382818050}[]{#_Toc382818544}[]{#_Toc383006642}[]{#_Toc383007138}[]{#_Toc383529817}[]{#_Toc387072466}[]{#_Toc382815068}[]{#_Toc382817556}[]{#_Toc382818052}[]{#_Toc382818546}[]{#_Toc383006644}[]{#_Toc383007140}[]{#_Toc383529819}[]{#_Toc387072468}[]{#_Toc382815069}[]{#_Toc382817557}[]{#_Toc382818053}[]{#_Toc382818547}[]{#_Toc383006645}[]{#_Toc383007141}[]{#_Toc383529820}[]{#_Toc387072469}

**Event MIB \-- Event MIB配置命令 \-- snmp mib event owner**

------------------------------------------------------------------------

[**[snmp mib event owner]{lang="EN-US"}**]{#struct_0_x1862_90986_x83970529}[命令用来创建一个]{style="font-family:宋体"}[Event]{lang="EN-US"}[并进入]{style="font-family:宋体"}[Event]{lang="EN-US"}[视图，若]{style="font-family:宋体"}[Event]{lang="EN-US"}[已经存在，则直接进入该]{style="font-family:宋体"}[Event]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo snmp mib event]{lang="EN-US"}**]{#struct_0_x1862_90986_x1511941192}[命令用来删除一个已存在的]{style="font-family:宋体"}[event]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1667987288}

[**[snmp mib event owner ]{lang="EN-US"}***[event-owner]{lang="EN-US"}***[ name]{lang="EN-US"}**[ *event-name* ]{lang="EN-US"}]{#struct_0_x1862_90986_1433117813}

[**[undo snmp mib event owner ]{lang="EN-US"}***[event-owner]{lang="EN-US"}***[ name]{lang="EN-US"}**[ *event-name*]{lang="EN-US"}]{#struct_0_x1862_90986_114603820}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_221046958}

[[不存在任何]{style="font-family:宋体"}[Event]{lang="EN-US"}]{#struct_0_x1862_90986_x190371491}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x401362638}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1862_90986_x1588262962}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x469467527}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x668839549}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x765726330}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_816897285}

[*[event-owner]{lang="EN-US"}*]{#struct_0_x1862_90986_x1813227595}[：事件所有者，应该指定为已存在的]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户。]{style="font-family:宋体"}

[*[event-name]{lang="EN-US"}*]{#struct_0_x1862_90986_x1624216902}[：创建的事件名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1829036717}

[[事件由所有者和事件名唯一识别。进入]{style="font-family:宋体"}[Event]{lang="EN-US"}]{#struct_0_x1862_90986_x2028451159}[视图后可以配置事件描述、事件动作和事件使能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1060896067}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_2076577388}[创建一个事件，其所有者为]{style="font-family:宋体"}[owner1]{lang="EN-US"}[，事件名为]{style="font-family:宋体"}[EventA]{lang="EN-US"}[，并进入该]{style="font-family:宋体"}[Event]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1862_90986_x114069592}

[\[Sysname\] snmp mib event owner owner1 name EventA]{lang="EN-US"}

[\[Sysname-event-owner1-EventA\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1810760173}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event]{lang="EN-US"}**]{#struct_0_x1862_90986_x713161525}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[description]{lang="EN-US"}**]{#struct_0_x1862_90986_1144937856}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[event enable]{lang="EN-US"}**]{#struct_0_x1862_90986_1219885997}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[action ]{lang="EN-US"}**]{#struct_0_x1862_90986_1571643893}
:::

::: {#1479666548 .myid}
[]{#_Toc404797081}[]{#struct_0_x1862_90986_1408412008}[]{#_Toc366652187}

**Event MIB \-- Event MIB配置命令 \-- snmp mib event object list**

------------------------------------------------------------------------

[**[snmp mib event object list]{lang="EN-US"}**]{#struct_0_x1862_90986_x594855376}[命令用来配置事件的绑定对象组的信息。]{style="font-family:宋体"}

[**[undo snmp mib event object list]{lang="EN-US"}**]{#struct_0_x1862_90986_613778552}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x2029539446}

[**[snmp mib event object list]{lang="EN-US"}***[ ]{lang="EN-US"}***[owner ]{lang="EN-US"}***[objects-owner]{lang="EN-US"}***[ name]{lang="EN-US"}**[ *objects-name* *objects-index* **oid** *object-identifier* \[ **wildcard** \]]{lang="EN-US"}]{#struct_0_x1862_90986_x1607609213}

[**[undo snmp mib event object list owner ]{lang="EN-US"}***[objects-owner]{lang="EN-US"}***[ name]{lang="EN-US"}**[ *objects-name* *objects-index*]{lang="EN-US"}]{#struct_0_x1862_90986_x1225102071}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1311691392}

[[没有指定绑定对象组。]{style="font-family:宋体"}]{#struct_0_x1862_90986_x96261433}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x86379537}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1862_90986_x1784059795}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1278331647}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_1591525515}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_99530201}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1486481860}

[**[owner]{lang="EN-US"}***[ objects-owner]{lang="EN-US"}*]{#struct_0_x1862_90986_170243649}[：对象组所有者，应该指定为已存在的]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}***[ objects-name]{lang="EN-US"}*]{#struct_0_x1862_90986_x527168348}[：创建的对象组名，其中组名为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[*[objects-index]{lang="EN-US"}*]{#struct_0_x1862_90986_x2088000088}[：绑定对象表的三级索引，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[oid]{lang="EN-US"}***[ object-identifier]{lang="EN-US"}*]{#struct_0_x1862_90986_x955956241}[：绑定的对象，取值为该对象节点]{style="font-family:宋体"}[OID]{lang="EN-US"}[值或者节点名称。配置的]{style="font-family:宋体"}[OID]{lang="EN-US"}[的值必须为表节点，概念行节点，表中列节点，简单叶子节点，叶节点的父节点中的任意一种。]{style="font-family:宋体"}

[**[wildcard]{lang="EN-US"}**]{#struct_0_x1862_90986_x1311557816}[：表示绑定对象的匹配方式为通配。如未指定该参数，则表示绑定对象的匹配方式为精确匹配。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x114188952}

[[绑定的对象由对象组所有者、对象组名和对象表的三级索引唯一确定，用来配置事件的绑定对象组的信息。]{style="font-family:宋体"}[Event]{lang="EN-US"}]{#struct_0_x1862_90986_1417191963}[事件对应动作为]{style="font-family:宋体"}[Notification]{lang="EN-US"}[，发送相应的]{style="font-family:宋体"}[Trap]{lang="EN-US"}[时可以从该配置的绑定对象组中获取信息。]{style="font-family:宋体"}[Notification]{lang="EN-US"}[绑定的对象组信息是向网管提供其关心的相关数据。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1496936339}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_x1416975674}[配置一个对象列表的信息，其中对象组所有者为]{style="font-family:宋体"}[owner1]{lang="EN-US"}[，创建的对象组名为]{style="font-family:宋体"}[objectA]{lang="EN-US"}[，绑定对象表的三级索引为]{style="font-family:宋体"}[10]{lang="EN-US"}[，绑定对象节点]{style="font-family:宋体"}[OID]{lang="EN-US"}[值为]{style="font-family:宋体"}[1.3.6.1.2.1.2.2.1.1.3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1862_90986_144042160}

[\[Sysname\] snmp mib event object list owner owner1 name objectA 10 oid 1.3.6.1.2.1.2.2.1.1.3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_178829293}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event]{lang="EN-US"}**]{#struct_0_x1862_90986_1194430076}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event trigger]{lang="EN-US"}**]{#struct_0_x1862_90986_x658352090}

[ ]{lang="EN-US"}
:::

::: {#-335437112 .myid}
[]{#_Toc404797082}[]{#struct_0_x1862_90986_10881288}

**Event MIB \-- Event MIB配置命令 \-- snmp mib event sample instance maximum**

------------------------------------------------------------------------

[**[snmp mib event sample instance]{lang="EN-US"}**[ **maximum**]{lang="EN-US"}]{#struct_0_x1862_90986_x114244898}[命令用来设置系统支持的最大监控对象数，即最大采样实例数。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp mib event sample instance** **maximum**]{lang="EN-US"}]{#struct_0_x1862_90986_1872405598}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1845989979}

[**[snmp mib event sample instance]{lang="EN-US"}**[ **maximum** *value*]{lang="EN-US"}]{#struct_0_x1862_90986_x61252571}

[**[undo snmp mib event sample instance]{lang="EN-US"}**[ **maximum**]{lang="EN-US"}]{#struct_0_x1862_90986_x2142687155}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x148891978}

[[最大采样实例数为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x1862_90986_x1934653846}[，表示没有上限。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1901805393}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1862_90986_x672634384}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_505271604}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_1267226894}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_779554727}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1496206537}

[*[value]{lang="EN-US"}*]{#struct_0_x1862_90986_x1698036917}[：系统支持的最大采样实例数，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[或正整数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1521958166}

[[当前活动状态的采样实例数：如果此次多个监控对象属性均为通配，即每个监控对象对应有多个行实例，则当前活动状态的采样实例数为这些通配对象所有行实例的累加值。]{style="font-family:宋体"}*[value]{lang="EN-US"}*]{#struct_0_x1862_90986_1934023099}[值为]{style="font-family:宋体"}[0]{lang="EN-US"}[表示没有上限，无特殊资源限制时应为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[修改此节点不影响已经为活动状态的采样实例，比如修改最大采样行实例数小于活动状态采样实例数，原来处于活动状态的行实例数不会减少，但此时如果出现新的行实例则当前行实例数不会新增；]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1862_90986_x263747155}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[最大采样实例数不变，当前采样实例数小于最大采样实例数，此时如果]{style="font-family:宋体"}]{#struct_0_x1862_90986_x908701279}[Trigger]{lang="EN-US"}[实例有新增，则当前采样实例数会更新，每采样一个实例，当前采样实例数就更新一次，并与配置的最大采样实例数比较，如果更新值刚好达到最大采样实例数，则之后新增的实例就不会再采样。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x806197729}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_x436056402}[设置系统支持的最大采样行数为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1862_90986_x1714975919}

[\[Sysname\] snmp mib event sample instance maximum 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_909295323}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event sample minimum]{lang="EN-US"}**]{#struct_0_x1862_90986_61544908}
:::

::: {#-46089060 .myid}
[]{#_Toc404797083}[]{#struct_0_x1862_90986_x1209330581}

**Event MIB \-- Event MIB配置命令 \-- snmp mib event sample minimum**

------------------------------------------------------------------------

[**[snmp mib event sample minimum]{lang="EN-US"}**]{#struct_0_x1862_90986_x250060553}[命]{style="font-family:宋体"}[令用来配置全局允许的最小采样时间间隔]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo snmp mib event sample minimum]{lang="EN-US"}**]{#struct_0_x1862_90986_1620570528}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_328414014}

[**[snmp mib event sample minimum ]{lang="EN-US"}***[value]{lang="EN-US"}*]{#struct_0_x1862_90986_433483477}

[**[undo snmp mib event sample minimum]{lang="EN-US"}**]{#struct_0_x1862_90986_1044982847}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1011046781}

[[全局允许的最小采样时间间隔为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x1862_90986_x24383917}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_548744002}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1862_90986_x978819340}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_471853452}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_1116914354}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_1013907436}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1009023128}

[*[value]{lang="EN-US"}*]{#struct_0_x1862_90986_862564177}[：]{style="font-family:宋体"}[全局允许的最小采样时间间隔]{style="font-family:宋体"}[，]{style="font-family:宋体"}[单位为秒]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1606336986}

[[为减少持续采样的系统开销，新配置的]{style="font-family:宋体"}[Trigger]{lang="EN-US"}]{#struct_0_x1862_90986_1804471610}[采样时间间隔必须大于等于该值，否则无法成功采样；]{style="font-family:宋体"}

[[修改本节点不影响正在被采样的]{style="font-family:宋体"}[Trigger]{lang="EN-US"}]{#struct_0_x1862_90986_x702703616}[，即使正在被采样的]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[的采样间隔小于新配置的最小采样间隔，也可以正常采样。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_267943144}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_x1821461390}[设置采样的全局最小间隔时间为]{style="font-family:宋体"}[50]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1862_90986_2106272941}

[\[Sysname\] snmp mib event sample minimum 50]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x316133907}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event trigger]{lang="EN-US"}**]{#struct_0_x1862_90986_x1883933623}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[frequency]{lang="EN-US"}**]{#struct_0_x1862_90986_x1715581962}
:::

::: {#316677404 .myid}
[]{#_Toc404797084}[]{#struct_0_x1862_90986_32996504}

**Event MIB \-- Event MIB配置命令 \-- snmp mib event trigger**

------------------------------------------------------------------------

[**[snmp mib event trigger]{lang="EN-US"}**]{#struct_0_x1862_90986_31541424}[命令用来创建一个]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[，并进入该]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[视图。如果]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[已经存在则直接进入视图。]{style="font-family:宋体"}

[**[undo snmp mib event trigger]{lang="EN-US"}**]{#struct_0_x1862_90986_x77780003}[命令用来删除指定]{style="font-family:
宋体"}[Trigger]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x552176505}

[**[snmp mib event trigger owner]{lang="EN-US"}**[ *trigger-owner* **name** *trigger-name*]{lang="EN-US"}]{#struct_0_x1862_90986_x1941227933}

[**[undo snmp mib event trigger owner]{lang="EN-US"}**[ *trigger-owner* **name** *trigger-name*]{lang="EN-US"}]{#struct_0_x1862_90986_x1954647257}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1460640666}

[[不存在任何]{style="font-family:宋体"}[Tigger]{lang="EN-US"}]{#struct_0_x1862_90986_1478841220}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x2075082906}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1862_90986_x1092118706}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1161498883}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_1567600248}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x682142843}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x835101908}

[*[trigger-owner]{lang="EN-US"}*]{#struct_0_x1862_90986_x10195595}[：]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[所有者，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。该]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[所有者需指定为一个已存在的]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户，用于判断对监控对象是否有操作权限。]{style="font-family:宋体"}

[*[trigger-name]{lang="EN-US"}*]{#struct_0_x1862_90986_1201289419}[：]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1895547490}

[[Trigger]{lang="EN-US"}]{#struct_0_x1862_90986_x2118260446}[由所有者和名称唯一确定。进入指定的]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[视图，可以指定监控的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[对象，定时对指定的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[对象进行采样。当获取监控对象所处的状态满足用户配置的事件触发条件时，就会触发相应的事件。]{style="font-family:宋体"}

[[若]{style="font-family:宋体"}[Trigger]{lang="EN-US"}]{#struct_0_x1862_90986_x1214745786}[所有者对该]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[视图下配置的采样节点没有读权限，则采样失败。有关]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户操作权限的详细介绍，请参见"网络管理与监控"中的"]{style="font-family:宋体"}[SNMP]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1381398168}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_x276704581}[配置]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[所有者]{style="font-family:宋体"}[owner1]{lang="EN-US"}[，]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[名称]{style="font-family:宋体"}[triggerA]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1862_90986_1706022166}

[\[Sysname\] snmp mib event trigger owner owner1 name triggerA]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA\] ]{lang="EN-US"}
:::

::: {#321884139 .myid}
[]{#_Toc404797085}[]{#struct_0_x1862_90986_791558841}

**Event MIB \-- Event MIB配置命令 \-- snmp-agent trap enable event-mib**

------------------------------------------------------------------------

[**[snmp-agent trap enable event-mib]{lang="EN-US"}**]{#struct_0_x1862_90986_x789868587}[命令用来使能]{style="font-family:宋体"}[Event MIB]{lang="EN-US"}[的告警功能。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[snmp-agent trap enable event-mib]{lang="EN-US"}**]{#struct_0_x1862_90986_77045917}[命令用来关闭告警功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_723683327}

[**[snmp-agent trap enable event-mib]{lang="EN-US"}**]{#struct_0_x1862_90986_x43617991}

[**[undo snmp-agent trap enable event-mib]{lang="EN-US"}**]{#struct_0_x1862_90986_x565964210}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x2142178285}

[[告警功能处于开启状态。]{style="font-family:宋体"}]{#struct_0_x1862_90986_x1016492482}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x137878474}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1862_90986_610622909}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1160568929}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_858198367}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x834134643}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x434106464}

[[开启]{style="font-family:宋体"}[Event MIB]{lang="EN-US"}]{#struct_0_x1862_90986_327874772}[模块的告警功能后，当配置的监控对象采样失败或者满足触发]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[的条件时会产生告警信息，该告警信息包括]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[触发告警、]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[触发上升阈告警、]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[触发下降阈告警、]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[触发条件检查失败告警、]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[触发事件]{style="font-family:宋体"}[Set]{lang="EN-US"}[动作失败的告警。生成的告警信息将发送到设备的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[模块，通过设置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[中告警信息的发送参数，来决定告警信息输出的相关属性。]{style="font-family:宋体"}

[[有关告警信息的详细介绍，请参见"网络管理与监控"中的"]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x1862_90986_x1185385555}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1623815909}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_x1143813925}[使能]{style="font-family:宋体"}[Event MIB]{lang="EN-US"}[的告警功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1862_90986_x1753317740}

[\[Sysname\] snmp-agent trap enable event-mib]{lang="EN-US"}
:::

::: {#-1767496984 .myid}
[]{#_Toc404797086}[]{#struct_0_x1862_90986_x1130535338}[]{#_Toc401850387}[]{#_Toc382815078}[]{#_Toc382817566}[]{#_Toc382818062}[]{#_Toc382818556}[]{#_Toc383006654}[]{#_Toc383007150}[]{#_Toc383529829}[]{#_Toc387072478}[]{#_Toc382815079}[]{#_Toc382817567}[]{#_Toc382818063}[]{#_Toc382818557}[]{#_Toc383006655}[]{#_Toc383007151}[]{#_Toc383529830}[]{#_Toc387072479}[]{#_Toc382815080}[]{#_Toc382817568}[]{#_Toc382818064}[]{#_Toc382818558}[]{#_Toc383006656}[]{#_Toc383007152}[]{#_Toc383529831}[]{#_Toc387072480}[]{#_Toc382815081}[]{#_Toc382817569}[]{#_Toc382818065}[]{#_Toc382818559}[]{#_Toc383006657}[]{#_Toc383007153}[]{#_Toc383529832}[]{#_Toc387072481}[]{#_Toc382815083}[]{#_Toc382817571}[]{#_Toc382818067}[]{#_Toc382818561}[]{#_Toc383006659}[]{#_Toc383007155}[]{#_Toc383529834}[]{#_Toc387072483}[]{#_Toc382815084}[]{#_Toc382817572}[]{#_Toc382818068}[]{#_Toc382818562}[]{#_Toc383006660}[]{#_Toc383007156}[]{#_Toc383529835}[]{#_Toc387072484}[]{#_Toc382815085}[]{#_Toc382817573}[]{#_Toc382818069}[]{#_Toc382818563}[]{#_Toc383006661}[]{#_Toc383007157}[]{#_Toc383529836}[]{#_Toc387072485}[]{#_Toc382815086}[]{#_Toc382817574}[]{#_Toc382818070}[]{#_Toc382818564}[]{#_Toc383006662}[]{#_Toc383007158}[]{#_Toc383529837}[]{#_Toc387072486}[]{#_Toc382815087}[]{#_Toc382817575}[]{#_Toc382818071}[]{#_Toc382818565}[]{#_Toc383006663}[]{#_Toc383007159}[]{#_Toc383529838}[]{#_Toc387072487}[]{#_Toc382815089}[]{#_Toc382817577}[]{#_Toc382818073}[]{#_Toc382818567}[]{#_Toc383006665}[]{#_Toc383007161}[]{#_Toc383529840}[]{#_Toc387072489}[]{#_Toc382815090}[]{#_Toc382817578}[]{#_Toc382818074}[]{#_Toc382818568}[]{#_Toc383006666}[]{#_Toc383007162}[]{#_Toc383529841}[]{#_Toc387072490}[]{#_Toc382815091}[]{#_Toc382817579}[]{#_Toc382818075}[]{#_Toc382818569}[]{#_Toc383006667}[]{#_Toc383007163}[]{#_Toc383529842}[]{#_Toc387072491}[]{#_Toc382815092}[]{#_Toc382817580}[]{#_Toc382818076}[]{#_Toc382818570}[]{#_Toc383006668}[]{#_Toc383007164}[]{#_Toc383529843}[]{#_Toc387072492}[]{#_Toc382815093}[]{#_Toc382817581}[]{#_Toc382818077}[]{#_Toc382818571}[]{#_Toc383006669}[]{#_Toc383007165}[]{#_Toc383529844}[]{#_Toc387072493}[]{#_Toc382815094}[]{#_Toc382817582}[]{#_Toc382818078}[]{#_Toc382818572}[]{#_Toc383006670}[]{#_Toc383007166}[]{#_Toc383529845}[]{#_Toc387072494}[]{#_Toc382815095}[]{#_Toc382817583}[]{#_Toc382818079}[]{#_Toc382818573}[]{#_Toc383006671}[]{#_Toc383007167}[]{#_Toc383529846}[]{#_Toc387072495}[]{#_Toc382815096}[]{#_Toc382817584}[]{#_Toc382818080}[]{#_Toc382818574}[]{#_Toc383006672}[]{#_Toc383007168}[]{#_Toc383529847}[]{#_Toc387072496}[]{#_Toc382815097}[]{#_Toc382817585}[]{#_Toc382818081}[]{#_Toc382818575}[]{#_Toc383006673}[]{#_Toc383007169}[]{#_Toc383529848}[]{#_Toc387072497}[]{#_Toc382815098}[]{#_Toc382817586}[]{#_Toc382818082}[]{#_Toc382818576}[]{#_Toc383006674}[]{#_Toc383007170}[]{#_Toc383529849}[]{#_Toc387072498}[]{#_Toc382815099}[]{#_Toc382817587}[]{#_Toc382818083}[]{#_Toc382818577}[]{#_Toc383006675}[]{#_Toc383007171}[]{#_Toc383529850}[]{#_Toc387072499}[]{#_Toc382815100}[]{#_Toc382817588}[]{#_Toc382818084}[]{#_Toc382818578}[]{#_Toc383006676}[]{#_Toc383007172}[]{#_Toc383529851}[]{#_Toc387072500}[]{#_Toc382815101}[]{#_Toc382817589}[]{#_Toc382818085}[]{#_Toc382818579}[]{#_Toc383006677}[]{#_Toc383007173}[]{#_Toc383529852}[]{#_Toc387072501}[]{#_Toc382815102}[]{#_Toc382817590}[]{#_Toc382818086}[]{#_Toc382818580}[]{#_Toc383006678}[]{#_Toc383007174}[]{#_Toc383529853}[]{#_Toc387072502}

**Event MIB \-- Event MIB配置命令 \-- startup (Trigger-existence view)**

------------------------------------------------------------------------

[**[startup]{lang="EN-US"}**]{#struct_0_x1862_90986_x1032693262}[命令用来配置首次采样允许触发事件的检测子类型。]{style="font-family:宋体"}

[**[undo startup]{lang="EN-US"}**]{#struct_0_x1862_90986_782574412}[命令用来关闭指定的检测子类型。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1667921752}

[**[startup ]{lang="EN-US"}**[{ **absent** \| **present** }]{lang="EN-US"}]{#struct_0_x1862_90986_x694524366}

[**[undo startup ]{lang="EN-US"}**[{ **absent** \| **present** }]{lang="EN-US"}]{#struct_0_x1862_90986_x884017033}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1651924520}

[[首次采样允许触发事件的检测子类型为]{style="font-family:宋体"}[present]{lang="EN-US"}]{#struct_0_x1862_90986_x77836608}[和]{style="font-family:宋体"}[absent]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x147735081}

[[Trigger-existence]{lang="EN-US"}]{#struct_0_x1862_90986_668644264}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1921355826}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_1801273022}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x1999523953}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1199338527}

[**[absent]{lang="EN-US"}**]{#struct_0_x1862_90986_1826862074}[：首次采样时，如果指定的监控对象不存在，且使用命令]{style="font-family:宋体"}**[type]{lang="EN-US"}**[配置采样检测类型]{style="font-family:宋体"}[Absent]{lang="EN-US"}[，则触发指定的事件。]{style="font-family:宋体"}

[**[present]{lang="EN-US"}**]{#struct_0_x1862_90986_1622678547}[：首次采样时，如果指定的监控对象存在，且使用命令]{style="font-family:宋体"}**[type]{lang="EN-US"}**[配置采样检测类型为]{style="font-family:宋体"}[Present]{lang="EN-US"}[，则触发指定的事件。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_952883313}

[[本命令作为]{style="font-family:宋体"}**[type]{lang="EN-US"}**]{#struct_0_x1862_90986_2012786755}[命令的扩展配置，用于首次采样时，若指定的监控对象满足]{style="font-family:宋体"}**[type]{lang="EN-US"}**[指定的检测类型，判断是否触发指定事件。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_x1862_90986_1060961603}**[type]{lang="EN-US"}**[和]{style="font-family:宋体"}**[startup]{lang="EN-US"}**[均配置为]{style="font-family:宋体"}[Present]{lang="EN-US"}[，如果监控对象为精确匹配，首次采样时监控对象存在则触发指定事件；如果监控对象为通配，首次采样时针对每个通配的对象单独触发指定事件。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_x1862_90986_176539456}**[type]{lang="EN-US"}**[和]{style="font-family:宋体"}**[startup]{lang="EN-US"}**[均配置为]{style="font-family:宋体"}[Absent]{lang="EN-US"}[，如果监控对象为精确匹配，首次采样时监控对象不存在则触发指定事件；如果监控对象为通配，首次采样不会触发事件。]{style="font-family:宋体"}

[[其他情况下，首次采样都不会触发事件。]{style="font-family:宋体"}]{#struct_0_x1862_90986_52766300}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_308290764}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_1487784862}[关闭首次采样允许触发事件的]{style="font-family:宋体"}[Present]{lang="EN-US"}[检测子类型。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1862_90986_x1448064637}

[\[Sysname\] snmp mib event trigger owner owner1 name triggerA]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA\] test existence]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA-existence\] undo startup present ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1699283258}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[type]{lang="EN-US"}**]{#struct_0_x1862_90986_1536490274}
:::

::: {#-418837455 .myid}
[]{#_Toc404797087}[]{#struct_0_x1862_90986_1144788117}

**Event MIB \-- Event MIB配置命令 \-- startup (Trigger-threshold view)**

------------------------------------------------------------------------

[**[startup]{lang="EN-US"}**]{#struct_0_x1862_90986_1893460046}[命令用来配置绝对值采样时首次采样允许触发的告警类型。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[startup]{lang="EN-US"}**]{#struct_0_x1862_90986_553998373}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x2141161557}

[**[startup]{lang="EN-US"}**[ ]{lang="EN-US"}[{ **falling** \| **rising** \| **rising-or-falling** }]{lang="EN-US"}]{#struct_0_x1862_90986_1765140187}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[startup]{lang="EN-US"}**]{#struct_0_x1862_90986_x1311625856}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_621653637}

[[绝对值采样时，首次采样允许触发的告警类型为]{style="font-family:宋体"}**[rising-or-falling]{lang="EN-US"}**]{#struct_0_x1862_90986_1011273738}[，即可以触发上限或下限告警。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x789665901}

[[Trigger-threshold]{lang="EN-US"}]{#struct_0_x1862_90986_x807760846}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1239289471}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_887519463}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_926818588}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_2134685892}

[**[falling]{lang="EN-US"}**]{#struct_0_x1862_90986_x1504329266}[：表示只触发下限告警。]{style="font-family:宋体"}

[**[rising]{lang="EN-US"}**]{#struct_0_x1862_90986_x1342410680}[：表示只触发上限告警。]{style="font-family:宋体"}

[**[rising-or-falling]{lang="EN-US"}**]{#struct_0_x1862_90986_x1845177343}[：表示可以触发上限或下限告警。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1563023549}

[[采样类型为绝对值采样时：]{style="font-family:宋体"}]{#struct_0_x1862_90986_1485681056}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若首次采样允许触发的告警类型配置为]{lang="EN-US" style="font-family:宋体"}**[rising]{lang="EN-US"}**]{#struct_0_x1862_90986_1417257499}[或者]{lang="EN-US" style="font-family:宋体"}**[rising-or-falling]{lang="EN-US"}**[，当首次采样值大于等于配置的上限阈值时，触发上限告警；]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若首次采样允许触发的告警类型配置为]{lang="EN-US" style="font-family:宋体"}**[falling]{lang="EN-US"}**]{#struct_0_x1862_90986_x264209927}[或者]{lang="EN-US" style="font-family:宋体"}**[rising-or-falling]{lang="EN-US"}**[，当首次采样值小于等于配置的下限阈值时，触发下限告警。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若前一次采样过程出错或监控对象不存在，那么此次对此监控对象的采样作为第一次采样来处理。]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1862_90986_x2112294813}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_705001916}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_158874570}[配置绝对值采样时首次采样允许触发的告警类型为触发上限告警。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1862_90986_576634391}

[\[Sysname\] snmp mib event trigger owner owner1 name triggerA]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA\] test threshold]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA-threshold\] startup rising]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x832855878}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event trigger]{lang="EN-US"}**]{#struct_0_x1862_90986_x1051223027}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[test ]{lang="EN-US"}**]{#struct_0_x1862_90986_367955482}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sample]{lang="EN-US"}**]{#struct_0_x1862_90986_1236402003}
:::

::: {#284671227 .myid}
[]{#_Toc404797088}[]{#struct_0_x1862_90986_x1995309619}[]{#_Toc366652157}

**Event MIB \-- Event MIB配置命令 \-- startup enable**

------------------------------------------------------------------------

[**[startup enable]{lang="EN-US"}**]{#struct_0_x1862_90986_x1392118404}[命令用来使能首次采样值满足检测条件时触发相应的事件功能。]{style="font-family:宋体"}

[**[undo startup enable]{lang="EN-US"}**]{#struct_0_x1862_90986_x148826442}[命令用来关闭该功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_127882796}

[**[startup enable]{lang="EN-US"}**]{#struct_0_x1862_90986_1503951628}

[**[undo startup enable]{lang="EN-US"}**]{#struct_0_x1862_90986_x1170892961}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x476910060}

[[首次采样满足检测条件则触发指定事件功能处于使能状态。]{style="font-family:宋体"}]{#struct_0_x1862_90986_427360990}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1840707753}

[[Trigger-boolean]{lang="EN-US"}]{#struct_0_x1862_90986_798593263}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x691440222}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x235330010}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_1655300659}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x2062277322}

[[当监控节点为首次采样时，如果没有使能此功能，即使采样值满足检测条件，也不会触发相应的事件。]{style="font-family:宋体"}]{#struct_0_x1862_90986_1516518000}

[[当监控节点首次采样值满足]{style="font-family:宋体"}[Boolean]{lang="EN-US"}]{#struct_0_x1862_90986_x1714910383}[测试条件时，并且配置了]{style="font-family:宋体"}**[startup enable]{lang="EN-US"}**[命令才会触发相应的事件，否则将不会触发相应的事件。]{style="font-family:宋体"}

[[若前一次采样过程出错或监控对象不存在，那么此次对该监控对象的采样作为第一次采样来处理。]{style="font-family:宋体"}]{#struct_0_x1862_90986_993301573}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x901190755}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_2117726428}[配置首次采样满足检测条件时能够触发相应的事件。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1862_90986_x1756962371}

[\[Sysname\] snmp mib event trigger owner owner1 name triggerA]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA\] test boolean]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA-boolean\] startup enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1252441489}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[comparison]{lang="EN-US"}**]{#struct_0_x1862_90986_1112125434}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[value]{lang="EN-US"}**]{#struct_0_x1862_90986_x347381034}
:::

::: {#-354185609 .myid}
[]{#_Toc404797089}[]{#struct_0_x1862_90986_x1458403957}

**Event MIB \-- Event MIB配置命令 \-- test**

------------------------------------------------------------------------

[**[test ]{lang="EN-US"}**[{ **boolean** \| **existence** \| **threshold** }]{lang="EN-US"}]{#struct_0_x1862_90986_944344822}[命令用来配置]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[触发条件的检测类型，并进入相应的]{style="font-family:宋体"}[Trigger-test]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo test ]{lang="EN-US"}**[{]{lang="EN-US"}**[ boolean ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ existence ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ threshold ]{lang="EN-US"}**[} ]{lang="EN-US"}]{#struct_0_x1862_90986_1013972972}[命令用于取消指定的检测类型。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1059330763}

[**[test]{lang="EN-US"}**[ {]{lang="EN-US"}**[ boolean ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ existence]{lang="EN-US"}**[ \|]{lang="EN-US"}**[ threshold ]{lang="EN-US"}**[}]{lang="EN-US"}**[ ]{lang="EN-US"}**]{#struct_0_x1862_90986_x348117710}

[**[undo test ]{lang="EN-US"}**[{]{lang="EN-US"}**[ boolean ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ existence ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ threshold ]{lang="EN-US"}**[}]{lang="EN-US"}**[ ]{lang="EN-US"}**]{#struct_0_x1862_90986_364562885}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1390681998}

[[没有配置]{style="font-family:宋体"}[trigger]{lang="EN-US"}]{#struct_0_x1862_90986_1708807111}[触发条件的检测类型。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x2141552461}

[[Trigger]{lang="EN-US"}]{#struct_0_x1862_90986_214921405}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1465359196}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x1940683863}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_1388802167}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x60977862}

[**[boolean]{lang="EN-US"}**]{#struct_0_x1862_90986_1197643354}[：]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[触发条件的检测类型为]{style="font-family:宋体"}[Boolean]{lang="EN-US"}[类型，主要用于对监控对象的值与参考值的大小比较等检查条件的设置。]{style="font-family:宋体"}

[**[existence]{lang="EN-US"}**]{#struct_0_x1862_90986_x1931281771}[：]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[触发条件的检测类型为]{style="font-family:宋体"}[Existence]{lang="EN-US"}[类型，主要用于对监控对象存在、消失或者改变等状态的检查条件的设置。]{style="font-family:宋体"}

[**[threshold]{lang="EN-US"}**]{#struct_0_x1862_90986_x552110969}[：]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[触发条件的检测类型为]{style="font-family:宋体"}[Threshold]{lang="EN-US"}[类型，主要用于对监控对象的值是否超过上升阈值或者低于下降阈值等检查条件的设置。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_769782275}

[[用户使用本命令可以配置]{style="font-family:宋体"}[Trigger]{lang="EN-US"}]{#struct_0_x1862_90986_x175417603}[运行的测试类型（]{style="font-family:宋体"}[Existence]{lang="EN-US"}[、]{style="font-family:宋体"}[Boolean]{lang="EN-US"}[、]{style="font-family:宋体"}[Threshold]{lang="EN-US"}[）。且每种类型都有相应的表（]{style="font-family:宋体"}[Existence]{lang="EN-US"}[表、]{style="font-family:宋体"}[Boolean]{lang="EN-US"}[表、]{style="font-family:宋体"}[Threshold]{lang="EN-US"}[表）与之对应，详细设置请参见对应的]{style="font-family:宋体"}[Trigger-boolean]{lang="EN-US"}[视图、]{style="font-family:宋体"}[Trigger-existence]{lang="EN-US"}[视图、]{style="font-family:宋体"}[Trigger-threshold]{lang="EN-US"}[视图下的命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1373419130}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_295127268}[配置]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[触发条件的检测类型为]{style="font-family:宋体"}[Existence]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\>system-view]{lang="EN-US"}]{#struct_0_x1862_90986_x284938464}

[\[Sysname\] snmp mib event trigger owner owner1 name triggerA]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA\] test existence]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1482907535}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event trigger]{lang="EN-US"}**]{#struct_0_x1862_90986_1705253161}
:::

::: {#1509844432 .myid}
[]{#_Toc404797090}[]{#struct_0_x1862_90986_x649416814}[]{#_Toc366652144}[]{#_Toc382815107}[]{#_Toc382817595}[]{#_Toc382818091}[]{#_Toc382818585}[]{#_Toc383006683}[]{#_Toc383007179}[]{#_Toc383529858}[]{#_Toc387072507}[]{#_Toc382815108}[]{#_Toc382817596}[]{#_Toc382818092}[]{#_Toc382818586}[]{#_Toc383006684}[]{#_Toc383007180}[]{#_Toc383529859}[]{#_Toc387072508}[]{#_Toc382815109}[]{#_Toc382817597}[]{#_Toc382818093}[]{#_Toc382818587}[]{#_Toc383006685}[]{#_Toc383007181}[]{#_Toc383529860}[]{#_Toc387072509}[]{#_Toc382815110}[]{#_Toc382817598}[]{#_Toc382818094}[]{#_Toc382818588}[]{#_Toc383006686}[]{#_Toc383007182}[]{#_Toc383529861}[]{#_Toc387072510}[]{#_Toc382815111}[]{#_Toc382817599}[]{#_Toc382818095}[]{#_Toc382818589}[]{#_Toc383006687}[]{#_Toc383007183}[]{#_Toc383529862}[]{#_Toc387072511}[]{#_Toc382815112}[]{#_Toc382817600}[]{#_Toc382818096}[]{#_Toc382818590}[]{#_Toc383006688}[]{#_Toc383007184}[]{#_Toc383529863}[]{#_Toc387072512}[]{#_Toc382815113}[]{#_Toc382817601}[]{#_Toc382818097}[]{#_Toc382818591}[]{#_Toc383006689}[]{#_Toc383007185}[]{#_Toc383529864}[]{#_Toc387072513}[]{#_Toc382815114}[]{#_Toc382817602}[]{#_Toc382818098}[]{#_Toc382818592}[]{#_Toc383006690}[]{#_Toc383007186}[]{#_Toc383529865}[]{#_Toc387072514}[]{#_Toc382815115}[]{#_Toc382817603}[]{#_Toc382818099}[]{#_Toc382818593}[]{#_Toc383006691}[]{#_Toc383007187}[]{#_Toc383529866}[]{#_Toc387072515}[]{#_Toc382815116}[]{#_Toc382817604}[]{#_Toc382818100}[]{#_Toc382818594}[]{#_Toc383006692}[]{#_Toc383007188}[]{#_Toc383529867}[]{#_Toc387072516}[]{#_Toc382815117}[]{#_Toc382817605}[]{#_Toc382818101}[]{#_Toc382818595}[]{#_Toc383006693}[]{#_Toc383007189}[]{#_Toc383529868}[]{#_Toc387072517}[]{#_Toc382815119}[]{#_Toc382817607}[]{#_Toc382818103}[]{#_Toc382818597}[]{#_Toc383006695}[]{#_Toc383007191}[]{#_Toc383529870}[]{#_Toc387072519}[]{#_Toc382815120}[]{#_Toc382817608}[]{#_Toc382818104}[]{#_Toc382818598}[]{#_Toc383006696}[]{#_Toc383007192}[]{#_Toc383529871}[]{#_Toc387072520}[]{#_Toc382815121}[]{#_Toc382817609}[]{#_Toc382818105}[]{#_Toc382818599}[]{#_Toc383006697}[]{#_Toc383007193}[]{#_Toc383529872}[]{#_Toc387072521}[]{#_Toc382815122}[]{#_Toc382817610}[]{#_Toc382818106}[]{#_Toc382818600}[]{#_Toc383006698}[]{#_Toc383007194}[]{#_Toc383529873}[]{#_Toc387072522}[]{#_Toc382815123}[]{#_Toc382817611}[]{#_Toc382818107}[]{#_Toc382818601}[]{#_Toc383006699}[]{#_Toc383007195}[]{#_Toc383529874}[]{#_Toc387072523}[]{#_Toc382815124}[]{#_Toc382817612}[]{#_Toc382818108}[]{#_Toc382818602}[]{#_Toc383006700}[]{#_Toc383007196}[]{#_Toc383529875}[]{#_Toc387072524}[]{#_Toc382815125}[]{#_Toc382817613}[]{#_Toc382818109}[]{#_Toc382818603}[]{#_Toc383006701}[]{#_Toc383007197}[]{#_Toc383529876}[]{#_Toc387072525}[]{#_Toc382815126}[]{#_Toc382817614}[]{#_Toc382818110}[]{#_Toc382818604}[]{#_Toc383006702}[]{#_Toc383007198}[]{#_Toc383529877}[]{#_Toc387072526}[]{#_Toc382815127}[]{#_Toc382817615}[]{#_Toc382818111}[]{#_Toc382818605}[]{#_Toc383006703}[]{#_Toc383007199}[]{#_Toc383529878}[]{#_Toc387072527}[]{#_Toc382815128}[]{#_Toc382817616}[]{#_Toc382818112}[]{#_Toc382818606}[]{#_Toc383006704}[]{#_Toc383007200}[]{#_Toc383529879}[]{#_Toc387072528}[]{#_Toc382815129}[]{#_Toc382817617}[]{#_Toc382818113}[]{#_Toc382818607}[]{#_Toc383006705}[]{#_Toc383007201}[]{#_Toc383529880}[]{#_Toc387072529}[]{#_Toc382815130}[]{#_Toc382817618}[]{#_Toc382818114}[]{#_Toc382818608}[]{#_Toc383006706}[]{#_Toc383007202}[]{#_Toc383529881}[]{#_Toc387072530}[]{#_Toc382815131}[]{#_Toc382817619}[]{#_Toc382818115}[]{#_Toc382818609}[]{#_Toc383006707}[]{#_Toc383007203}[]{#_Toc383529882}[]{#_Toc387072531}[]{#_Toc382815132}[]{#_Toc382817620}[]{#_Toc382818116}[]{#_Toc382818610}[]{#_Toc383006708}[]{#_Toc383007204}[]{#_Toc383529883}[]{#_Toc387072532}[]{#_Toc382815133}[]{#_Toc382817621}[]{#_Toc382818117}[]{#_Toc382818611}[]{#_Toc383006709}[]{#_Toc383007205}[]{#_Toc383529884}[]{#_Toc387072533}[]{#_Toc382815134}[]{#_Toc382817622}[]{#_Toc382818118}[]{#_Toc382818612}[]{#_Toc383006710}[]{#_Toc383007206}[]{#_Toc383529885}[]{#_Toc387072534}[]{#_Toc382815135}[]{#_Toc382817623}[]{#_Toc382818119}[]{#_Toc382818613}[]{#_Toc383006711}[]{#_Toc383007207}[]{#_Toc383529886}[]{#_Toc387072535}[]{#_Toc382815136}[]{#_Toc382817624}[]{#_Toc382818120}[]{#_Toc382818614}[]{#_Toc383006712}[]{#_Toc383007208}[]{#_Toc383529887}[]{#_Toc387072536}[]{#_Toc382815137}[]{#_Toc382817625}[]{#_Toc382818121}[]{#_Toc382818615}[]{#_Toc383006713}[]{#_Toc383007209}[]{#_Toc383529888}[]{#_Toc387072537}[]{#_Toc382815138}[]{#_Toc382817626}[]{#_Toc382818122}[]{#_Toc382818616}[]{#_Toc383006714}[]{#_Toc383007210}[]{#_Toc383529889}[]{#_Toc387072538}[]{#_Toc382815139}[]{#_Toc382817627}[]{#_Toc382818123}[]{#_Toc382818617}[]{#_Toc383006715}[]{#_Toc383007211}[]{#_Toc383529890}[]{#_Toc387072539}[]{#_Toc401850392}

**Event MIB \-- Event MIB配置命令 \-- trigger enable**

------------------------------------------------------------------------

[**[trigger enable]{lang="EN-US"}**]{#struct_0_x1862_90986_x1314237012}[命令用来使能]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[的采样功能。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[trigger enable]{lang="EN-US"}**]{#struct_0_x1862_90986_x941699627}[命令用来关闭]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[采样功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x2118194910}

[**[trigger enable]{lang="EN-US"}**]{#struct_0_x1862_90986_x2030107050}

[**[undo ]{lang="EN-US"}[trigger enable]{lang="EN-US"}**]{#struct_0_x1862_90986_x100295249}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x401262653}

[[Trigger]{lang="EN-US"}]{#struct_0_x1862_90986_x1587673211}[采样功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1512489209}

[[trigger]{lang="EN-US"}]{#struct_0_x1862_90986_1480906593}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_164913034}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x1305852998}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x1158719105}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x976298688}

[[在使能]{style="font-family:宋体"}[Trigger]{lang="EN-US"}]{#struct_0_x1862_90986_1810128125}[采样功能前，需要先检查]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[是否满足可以使能的条件：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[必须指定监控对象；]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1862_90986_x350246436}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[采样时间间隔必须大于等于系统支持的最小采样时间间隔。]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1862_90986_x108251582}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_610688445}

[[\#]{lang="EN-US"}]{#struct_0_x1862_90986_x1177036330}[当前最小采样时间间隔为]{style="font-family:宋体"}[100]{lang="EN-US"}[，使能]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[的采样功能。]{style="font-family:宋体"}

[[\<Sysname\>system-view]{lang="EN-US"}]{#struct_0_x1862_90986_x1241503042}

[\[Sysname\] snmp mib event trigger owner owner1 name triggerA]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA\] oid 1.3.6.1.2.1.2.2.1.1.3 ]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA\] frequency 360]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA\] trigger enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1658338416}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event trigger]{lang="EN-US"}**]{#struct_0_x1862_90986_770556639}
:::

::: {#-1051447130 .myid}
[]{#_Toc404797091}[]{#struct_0_x1862_90986_x673516787}[]{#_Toc366652163}[]{#_Toc388455556}[]{#_Toc388455557}[]{#_Toc388455558}[]{#_Toc388455559}[]{#_Toc388455560}[]{#_Toc388455561}[]{#_Toc388455562}[]{#_Toc388455563}[]{#_Toc388455564}[]{#_Toc388455565}[]{#_Toc388455567}[]{#_Toc388455568}[]{#_Toc388455569}[]{#_Toc388455570}[]{#_Toc388455571}[]{#_Toc388455572}[]{#_Toc388455573}[]{#_Toc388455574}[]{#_Toc388455575}[]{#_Toc388455576}[]{#_Toc388455579}[]{#_Toc388455580}[]{#_Toc388455581}[]{#_Toc388455582}

**Event MIB \-- Event MIB配置命令 \-- type**

------------------------------------------------------------------------

[**[type]{lang="EN-US"}**]{#struct_0_x1862_90986_2064825865}[命令用来指定]{style="font-family:宋体"}[Trigger-existence]{lang="EN-US"}[视图下的检测类型。]{style="font-family:宋体"}

[**[undo type]{lang="EN-US"}**]{#struct_0_x1862_90986_x1630827184}[命令用于取消指定的检测类型。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x675739814}

[**[type ]{lang="EN-US"}**[{ **absent** \| **changed** \|**present** }]{lang="EN-US"}]{#struct_0_x1862_90986_485943597}

[**[undo type ]{lang="EN-US"}**[{ **absent** \|**changed** \|**present** }]{lang="EN-US"}]{#struct_0_x1862_90986_1306904974}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1254427342}

[[默认值为]{style="font-family:宋体"}[Present]{lang="EN-US"}]{#struct_0_x1862_90986_x1667856216}[和]{style="font-family:宋体"}[Absent]{lang="EN-US"}[测试类型。]{style="font-family:宋体"}

[[【视图】]{style="font-family:
黑体"}]{#struct_0_x1862_90986_x84386}

[[Trigger-existence]{lang="EN-US"}]{#struct_0_x1862_90986_x1653941513}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x114395439}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_1422471184}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x70342657}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x550315362}

[**[absent]{lang="EN-US"}**]{#struct_0_x1862_90986_889170746}[：此次]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[监控对象不存在，上一次]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[监控对象存在，将触发指定的事件。首次采样时，若监控对象属性为精确匹配且监控对象不存在，必须同时满足设置命令]{style="font-family:宋体"}**[startup absent]{lang="EN-US"}[，]{style="font-family:宋体"}**[才会触发相应事件。]{style="font-family:宋体"}

[**[changed]{lang="EN-US"}**]{#struct_0_x1862_90986_x2030377272}[：当]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[监控对象的值发生改变时，触发指定事件。如果上一次采样值获取不到则不触发。]{style="font-family:宋体"}

[**[present]{lang="EN-US"}**]{#struct_0_x1862_90986_x802175592}[：此次]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[监控对象存在，上一次]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[监控对象不存在，将触发指定的事件。首次采样时，若监控对象存在，必须同时满足设置命令]{style="font-family:宋体"}**[startup present]{lang="EN-US"}[，]{style="font-family:宋体"}**[才会触发相应事件。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1748355105}

[[对于第一次采样，参考]{style="font-family:宋体"}**[startup]{lang="EN-US"}**]{#struct_0_x1862_90986_x991310979}[命令使用指导。]{style="font-family:宋体"}

[[如果不是第一次采样：]{style="font-family:宋体"}]{#struct_0_x1862_90986_516892107}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当执行]{lang="EN-US" style="font-family:宋体"}**[type present]{lang="EN-US"}**]{#struct_0_x1862_90986_1061027139}[命令时，对于精确匹配，如果此次监控对象存在，前一次监控对象不存在，则触发指定事件；对于通配，获取当前监控对象的集合，将其中的每一个监控对象都与前一次通配到的所有监控对象比较，如果前一次无相同的监控对象，则触发指定事件。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当执行]{lang="EN-US" style="font-family:宋体"}**[type absent]{lang="EN-US"}**]{#struct_0_x1862_90986_x1029667830}[命令时，对于精确匹配，如果此次监控对象不存在，前一次监控对象存在，则触发指定事件；对于通配，获取当前监控对象的集合，将前一次的每一个监控对象都与此次通配到的所有监控对象比较，如果此次无相同的监控对象，则触发指定事件。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当执行]{lang="EN-US" style="font-family:宋体"}**[type changed]{lang="EN-US"}**]{#struct_0_x1862_90986_x286740746}[命令时，对于精确匹配，如果此次与前一次都有相同的监控对象，那么比较之，若其值不同，则触发指定事件；对于通配，获取当前监控对象的集合，将其中的每一个监控对象都与前一次通配到的所有监控对象比较，如果两次都有相同的监控对象，那么比较之，若其值不同，则触发指定事件。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1851278601}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_1442761259}[配置]{style="font-family:宋体"}[Trigger-existence]{lang="EN-US"}[子视图下检测类型为]{style="font-family:宋体"}[Present]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1862_90986_1987164181}

[\[Sysname\] snmp mib event trigger owner owner1 name triggerA]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA\] test existence]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA-existence\] type present]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x430487113}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event trigger]{lang="EN-US"}**]{#struct_0_x1862_90986_x1386117951}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[test]{lang="EN-US"}**]{#struct_0_x1862_90986_x1099014057}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[startup]{lang="EN-US"}**]{#struct_0_x1862_90986_1208780460}
:::

::: {#20535924 .myid}
[]{#_Toc404797092}[]{#struct_0_x1862_90986_x68738161}[]{#_Toc366652158}[]{#_Toc388455584}[]{#_Toc388455585}[]{#_Toc388455586}[]{#_Toc388455587}[]{#_Toc388455588}[]{#_Toc388455589}[]{#_Toc388455590}[]{#_Toc388455591}[]{#_Toc388455592}[]{#_Toc388455593}[]{#_Toc388455594}[]{#_Toc388455597}[]{#_Toc388455598}[]{#_Toc388455599}[]{#_Toc388455600}[]{#_Toc388455601}[]{#_Toc388455602}[]{#_Toc388455603}[]{#_Toc388455604}[]{#_Toc388455605}[]{#_Toc388455606}[]{#_Toc388455607}[]{#_Toc388455608}[]{#_Toc388455609}[]{#_Toc388455610}[]{#_Toc388455611}[]{#_Toc388455612}

**Event MIB \-- Event MIB配置命令 \-- value (Trigger-boolean view)**

------------------------------------------------------------------------

[**[value]{lang="EN-US"}**]{#struct_0_x1862_90986_434354498}[命令用来配置与采样值进行比较的参考值。]{style="font-family:宋体"}

[**[undo value]{lang="EN-US"}**]{#struct_0_x1862_90986_1991007362}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_859884878}

[**[value]{lang="EN-US"}**[ ]{lang="EN-US"}*[integer-value]{lang="EN-US"}*]{#struct_0_x1862_90986_x1311560320}

[**[undo value]{lang="EN-US"}**]{#struct_0_x1862_90986_x656824982}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x943120216}

[[与采样值进行比较的参考值为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x1862_90986_x150794036}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1930174531}

[[Trigger-boolean]{lang="EN-US"}]{#struct_0_x1862_90986_9978511}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x573329004}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_1682499786}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_1864713912}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_51097917}

[*[integer-value]{lang="EN-US"}*]{#struct_0_x1862_90986_1238468683}[：用于跟采样值进行比较的参考值，取值为任意整数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_939571575}

[[根据]{style="font-family:宋体"}**[comparison]{lang="EN-US"}**]{#struct_0_x1862_90986_x1615408086}[命令配置的比较方式，将获取的采样值与]{style="font-family:宋体"}**[value]{lang="EN-US"}**[命令配置的参考值进行比较并确定是否满足检测条件。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x233131060}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_x1341362833}[配置与采样值进行比较使用的参考值为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1862_90986_1417323035}

[\[Sysname\] snmp mib event trigger owner owner1 name triggerA]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA\] test boolean]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA-boolean\] value 5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1835948166}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[comparison]{lang="EN-US"}**]{#struct_0_x1862_90986_884696395}
:::

::: {#2114966226 .myid}
[]{#_Toc404797093}[]{#struct_0_x1862_90986_x1740707346}[]{#_Toc366652180}

**Event MIB \-- Event MIB配置命令 \-- value (Action-set view)**

------------------------------------------------------------------------

[**[value]{lang="EN-US"}**]{#struct_0_x1862_90986_732883255}[命令用来配置]{style="font-family:宋体"}[Set]{lang="EN-US"}[操作对象的值。]{style="font-family:宋体"}

[**[undo value]{lang="EN-US"}**]{#struct_0_x1862_90986_x1346698085}[命令用来恢复缺省情况。]{style="font-family:宋体;color:black"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1635372476}

[**[value]{lang="EN-US"}***[ integer-value]{lang="EN-US"}*]{#struct_0_x1862_90986_x989135244}

[**[undo value]{lang="EN-US"}**]{#struct_0_x1862_90986_1333365610}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_802606648}

[[Set]{lang="EN-US"}]{#struct_0_x1862_90986_x438672325}[操作对象的值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_418892809}

[[Action-set]{lang="EN-US"}]{#struct_0_x1862_90986_x1449608123}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1840107264}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x148760906}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x349367951}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x841627157}

[*[integer-value]{lang="EN-US"}*]{#struct_0_x1862_90986_1362152076}[：]{style="font-family:宋体"}[Set]{lang="EN-US"}[操作对象的值，取值为任意整数。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x311935770}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_x1944964914}[将]{style="font-family:宋体"}[Set]{lang="EN-US"}[操作对象]{style="font-family:宋体"}[1.3.6.1.2.1.2.2.1.7.3]{lang="EN-US"}[的值设置为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname\] snmp mib event owner owner1 name EventA]{lang="EN-US"}]{#struct_0_x1862_90986_x1377471265}

[\[Sysname-event-owner1-EventA\] action set]{lang="EN-US"}

[\[Sysname-event-owner1-EventA-set\] oid 1.3.6.1.2.1.2.2.1.7.3]{lang="EN-US"}

[\[Sysname-event-owner1-EventA-set\] value 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_2051529634}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event owner]{lang="EN-US"}**]{#struct_0_x1862_90986_x1781184275}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[action]{lang="EN-US"}**]{#struct_0_x1862_90986_x1415891678}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oid]{lang="EN-US"}**]{#struct_0_x1862_90986_x1104659475}
:::

::: {#200675496 .myid}
[]{#_Toc404797094}[]{#struct_0_x1862_90986_x1638448204}

**Event MIB \-- Event MIB配置命令 \-- wildcard context (Trigger view)**

------------------------------------------------------------------------

[**[wildcard ]{lang="EN-US"}[context]{lang="EN-US"}**]{#struct_0_x1862_90986_255072443}[命令用来配置监控对象所在的]{style="font-family:宋体;color:black"}[SNMP]{lang="EN-US" style="color:black"}[上下文的匹配方式为通配。]{style="font-family:宋体;
color:black"}

[**[undo]{lang="EN-US"}**[ **wildcard** **context**]{lang="EN-US"}]{#struct_0_x1862_90986_904480263}[命令用来恢复缺省情况。]{style="font-family:
宋体;color:black"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1714844847}

[**[wildcard ]{lang="EN-US"}[context]{lang="EN-US"}**]{#struct_0_x1862_90986_x521871967}

[**[undo wildcard context]{lang="EN-US"}**]{#struct_0_x1862_90986_x1671465356}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1966608900}

[[配置监控对象所在的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x1862_90986_149663410}[上下文的匹配方式为精确匹配。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x100390185}

[[Trigger]{lang="EN-US"}]{#struct_0_x1862_90986_1559949577}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_711873579}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x1557444444}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x733985028}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_147233778}

[[本命令和]{style="font-family:宋体"}**[context]{lang="EN-US"}**]{#struct_0_x1862_90986_x1690600407}[命令配合使用，共同决定监控对象所在的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[上下文：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[精确匹配表示配置为特定的]{lang="EN-US" style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x1862_90986_x732086680}[上下文环境名；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通配表示只指定上下文的前缀，即配置系统中存在的相同前缀的所有上下文环境名。]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1862_90986_x1421870992}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1180982396}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_x1375786367}[配置监控对象所在的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[上下文环境名为]{style="font-family:宋体"}[contextname]{lang="EN-US"}[的匹配方式为通配。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1862_90986_1014038508}

[\[Sysname\] snmp mib event trigger owner owner1 name triggerA]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA\] context contextname]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA\] wildcard context]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_451783165}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event trigger]{lang="EN-US"}**]{#struct_0_x1862_90986_x2026276327}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[context]{lang="EN-US"}**]{#struct_0_x1862_90986_258543040}
:::

::: {#-1806319718 .myid}
[]{#_Toc404797095}[]{#struct_0_x1862_90986_x698193036}[]{#_Toc382815146}[]{#_Toc382817634}[]{#_Toc382818130}[]{#_Toc382818624}[]{#_Toc383006722}[]{#_Toc383007218}[]{#_Toc383529897}[]{#_Toc387072546}[]{#_Toc382815147}[]{#_Toc382817635}[]{#_Toc382818131}[]{#_Toc382818625}[]{#_Toc383006723}[]{#_Toc383007219}[]{#_Toc383529898}[]{#_Toc387072547}[]{#_Toc382815148}[]{#_Toc382817636}[]{#_Toc382818132}[]{#_Toc382818626}[]{#_Toc383006724}[]{#_Toc383007220}[]{#_Toc383529899}[]{#_Toc387072548}[]{#_Toc382815149}[]{#_Toc382817637}[]{#_Toc382818133}[]{#_Toc382818627}[]{#_Toc383006725}[]{#_Toc383007221}[]{#_Toc383529900}[]{#_Toc387072549}[]{#_Toc382815150}[]{#_Toc382817638}[]{#_Toc382818134}[]{#_Toc382818628}[]{#_Toc383006726}[]{#_Toc383007222}[]{#_Toc383529901}[]{#_Toc387072550}[]{#_Toc382815152}[]{#_Toc382817640}[]{#_Toc382818136}[]{#_Toc382818630}[]{#_Toc383006728}[]{#_Toc383007224}[]{#_Toc383529903}[]{#_Toc387072552}[]{#_Toc382815153}[]{#_Toc382817641}[]{#_Toc382818137}[]{#_Toc382818631}[]{#_Toc383006729}[]{#_Toc383007225}[]{#_Toc383529904}[]{#_Toc387072553}[]{#_Toc382815154}[]{#_Toc382817642}[]{#_Toc382818138}[]{#_Toc382818632}[]{#_Toc383006730}[]{#_Toc383007226}[]{#_Toc383529905}[]{#_Toc387072554}[]{#_Toc382815155}[]{#_Toc382817643}[]{#_Toc382818139}[]{#_Toc382818633}[]{#_Toc383006731}[]{#_Toc383007227}[]{#_Toc383529906}[]{#_Toc387072555}[]{#_Toc382815156}[]{#_Toc382817644}[]{#_Toc382818140}[]{#_Toc382818634}[]{#_Toc383006732}[]{#_Toc383007228}[]{#_Toc383529907}[]{#_Toc387072556}[]{#_Toc382815158}[]{#_Toc382817646}[]{#_Toc382818142}[]{#_Toc382818636}[]{#_Toc383006734}[]{#_Toc383007230}[]{#_Toc383529909}[]{#_Toc387072558}[]{#_Toc382815159}[]{#_Toc382817647}[]{#_Toc382818143}[]{#_Toc382818637}[]{#_Toc383006735}[]{#_Toc383007231}[]{#_Toc383529910}[]{#_Toc387072559}[]{#_Toc382815160}[]{#_Toc382817648}[]{#_Toc382818144}[]{#_Toc382818638}[]{#_Toc383006736}[]{#_Toc383007232}[]{#_Toc383529911}[]{#_Toc387072560}[]{#_Toc382815161}[]{#_Toc382817649}[]{#_Toc382818145}[]{#_Toc382818639}[]{#_Toc383006737}[]{#_Toc383007233}[]{#_Toc383529912}[]{#_Toc387072561}[]{#_Toc382815162}[]{#_Toc382817650}[]{#_Toc382818146}[]{#_Toc382818640}[]{#_Toc383006738}[]{#_Toc383007234}[]{#_Toc383529913}[]{#_Toc387072562}[]{#_Toc382815163}[]{#_Toc382817651}[]{#_Toc382818147}[]{#_Toc382818641}[]{#_Toc383006739}[]{#_Toc383007235}[]{#_Toc383529914}[]{#_Toc387072563}[]{#_Toc382815164}[]{#_Toc382817652}[]{#_Toc382818148}[]{#_Toc382818642}[]{#_Toc383006740}[]{#_Toc383007236}[]{#_Toc383529915}[]{#_Toc387072564}[]{#_Toc382815165}[]{#_Toc382817653}[]{#_Toc382818149}[]{#_Toc382818643}[]{#_Toc383006741}[]{#_Toc383007237}[]{#_Toc383529916}[]{#_Toc387072565}[]{#_Toc382815166}[]{#_Toc382817654}[]{#_Toc382818150}[]{#_Toc382818644}[]{#_Toc383006742}[]{#_Toc383007238}[]{#_Toc383529917}[]{#_Toc387072566}[]{#_Toc382815167}[]{#_Toc382817655}[]{#_Toc382818151}[]{#_Toc382818645}[]{#_Toc383006743}[]{#_Toc383007239}[]{#_Toc383529918}[]{#_Toc387072567}[]{#_Toc382815169}[]{#_Toc382817657}[]{#_Toc382818153}[]{#_Toc382818647}[]{#_Toc383006745}[]{#_Toc383007241}[]{#_Toc383529920}[]{#_Toc387072569}[]{#_Toc382815170}[]{#_Toc382817658}[]{#_Toc382818154}[]{#_Toc382818648}[]{#_Toc383006746}[]{#_Toc383007242}[]{#_Toc383529921}[]{#_Toc387072570}[]{#_Toc382815171}[]{#_Toc382817659}[]{#_Toc382818155}[]{#_Toc382818649}[]{#_Toc383006747}[]{#_Toc383007243}[]{#_Toc383529922}[]{#_Toc387072571}[]{#_Toc382815172}[]{#_Toc382817660}[]{#_Toc382818156}[]{#_Toc382818650}[]{#_Toc383006748}[]{#_Toc383007244}[]{#_Toc383529923}[]{#_Toc387072572}[]{#_Toc382815173}[]{#_Toc382817661}[]{#_Toc382818157}[]{#_Toc382818651}[]{#_Toc383006749}[]{#_Toc383007245}[]{#_Toc383529924}[]{#_Toc387072573}[]{#_Toc382815174}[]{#_Toc382817662}[]{#_Toc382818158}[]{#_Toc382818652}[]{#_Toc383006750}[]{#_Toc383007246}[]{#_Toc383529925}[]{#_Toc387072574}[]{#_Toc382815175}[]{#_Toc382817663}[]{#_Toc382818159}[]{#_Toc382818653}[]{#_Toc383006751}[]{#_Toc383007247}[]{#_Toc383529926}[]{#_Toc387072575}[]{#_Toc382815178}[]{#_Toc382817666}[]{#_Toc382818162}[]{#_Toc382818656}[]{#_Toc383006754}[]{#_Toc383007250}[]{#_Toc383529929}[]{#_Toc387072578}[]{#_Toc382815179}[]{#_Toc382817667}[]{#_Toc382818163}[]{#_Toc382818657}[]{#_Toc383006755}[]{#_Toc383007251}[]{#_Toc383529930}[]{#_Toc387072579}[]{#_Toc382815180}[]{#_Toc382817668}[]{#_Toc382818164}[]{#_Toc382818658}[]{#_Toc383006756}[]{#_Toc383007252}[]{#_Toc383529931}[]{#_Toc387072580}[]{#_Toc382815181}[]{#_Toc382817669}[]{#_Toc382818165}[]{#_Toc382818659}[]{#_Toc383006757}[]{#_Toc383007253}[]{#_Toc383529932}[]{#_Toc387072581}[]{#_Toc382815182}[]{#_Toc382817670}[]{#_Toc382818166}[]{#_Toc382818660}[]{#_Toc383006758}[]{#_Toc383007254}[]{#_Toc383529933}[]{#_Toc387072582}[]{#_Toc382815184}[]{#_Toc382817672}[]{#_Toc382818168}[]{#_Toc382818662}[]{#_Toc383006760}[]{#_Toc383007256}[]{#_Toc383529935}[]{#_Toc387072584}[]{#_Toc382815185}[]{#_Toc382817673}[]{#_Toc382818169}[]{#_Toc382818663}[]{#_Toc383006761}[]{#_Toc383007257}[]{#_Toc383529936}[]{#_Toc387072585}[]{#_Toc382815186}[]{#_Toc382817674}[]{#_Toc382818170}[]{#_Toc382818664}[]{#_Toc383006762}[]{#_Toc383007258}[]{#_Toc383529937}[]{#_Toc387072586}[]{#_Toc382815187}[]{#_Toc382817675}[]{#_Toc382818171}[]{#_Toc382818665}[]{#_Toc383006763}[]{#_Toc383007259}[]{#_Toc383529938}[]{#_Toc387072587}[]{#_Toc382815188}[]{#_Toc382817676}[]{#_Toc382818172}[]{#_Toc382818666}[]{#_Toc383006764}[]{#_Toc383007260}[]{#_Toc383529939}[]{#_Toc387072588}[]{#_Toc382815189}[]{#_Toc382817677}[]{#_Toc382818173}[]{#_Toc382818667}[]{#_Toc383006765}[]{#_Toc383007261}[]{#_Toc383529940}[]{#_Toc387072589}[]{#_Toc382815190}[]{#_Toc382817678}[]{#_Toc382818174}[]{#_Toc382818668}[]{#_Toc383006766}[]{#_Toc383007262}[]{#_Toc383529941}[]{#_Toc387072590}[]{#_Toc382815191}[]{#_Toc382817679}[]{#_Toc382818175}[]{#_Toc382818669}[]{#_Toc383006767}[]{#_Toc383007263}[]{#_Toc383529942}[]{#_Toc387072591}[]{#_Toc382815192}[]{#_Toc382817680}[]{#_Toc382818176}[]{#_Toc382818670}[]{#_Toc383006768}[]{#_Toc383007264}[]{#_Toc383529943}[]{#_Toc387072592}[]{#_Toc382815193}[]{#_Toc382817681}[]{#_Toc382818177}[]{#_Toc382818671}[]{#_Toc383006769}[]{#_Toc383007265}[]{#_Toc383529944}[]{#_Toc387072593}[]{#_Toc382815195}[]{#_Toc382817683}[]{#_Toc382818179}[]{#_Toc382818673}[]{#_Toc383006771}[]{#_Toc383007267}[]{#_Toc383529946}[]{#_Toc387072595}[]{#_Toc382815196}[]{#_Toc382817684}[]{#_Toc382818180}[]{#_Toc382818674}[]{#_Toc383006772}[]{#_Toc383007268}[]{#_Toc383529947}[]{#_Toc387072596}[]{#_Toc382815197}[]{#_Toc382817685}[]{#_Toc382818181}[]{#_Toc382818675}[]{#_Toc383006773}[]{#_Toc383007269}[]{#_Toc383529948}[]{#_Toc387072597}[]{#_Toc382815198}[]{#_Toc382817686}[]{#_Toc382818182}[]{#_Toc382818676}[]{#_Toc383006774}[]{#_Toc383007270}[]{#_Toc383529949}[]{#_Toc387072598}[]{#_Toc401850398}[]{#_Toc382815201}[]{#_Toc382817689}[]{#_Toc382818185}[]{#_Toc382818679}[]{#_Toc383006777}[]{#_Toc383007273}[]{#_Toc383529952}[]{#_Toc387072601}[]{#_Toc382815202}[]{#_Toc382817690}[]{#_Toc382818186}[]{#_Toc382818680}[]{#_Toc383006778}[]{#_Toc383007274}[]{#_Toc383529953}[]{#_Toc387072602}[]{#_Toc382815203}[]{#_Toc382817691}[]{#_Toc382818187}[]{#_Toc382818681}[]{#_Toc383006779}[]{#_Toc383007275}[]{#_Toc383529954}[]{#_Toc387072603}[]{#_Toc382815204}[]{#_Toc382817692}[]{#_Toc382818188}[]{#_Toc382818682}[]{#_Toc383006780}[]{#_Toc383007276}[]{#_Toc383529955}[]{#_Toc387072604}[]{#_Toc382815206}[]{#_Toc382817694}[]{#_Toc382818190}[]{#_Toc382818684}[]{#_Toc383006782}[]{#_Toc383007278}[]{#_Toc383529957}[]{#_Toc387072606}[]{#_Toc382815207}[]{#_Toc382817695}[]{#_Toc382818191}[]{#_Toc382818685}[]{#_Toc383006783}[]{#_Toc383007279}[]{#_Toc383529958}[]{#_Toc387072607}[]{#_Toc382815208}[]{#_Toc382817696}[]{#_Toc382818192}[]{#_Toc382818686}[]{#_Toc383006784}[]{#_Toc383007280}[]{#_Toc383529959}[]{#_Toc387072608}[]{#_Toc382815209}[]{#_Toc382817697}[]{#_Toc382818193}[]{#_Toc382818687}[]{#_Toc383006785}[]{#_Toc383007281}[]{#_Toc383529960}[]{#_Toc387072609}[]{#_Toc382815210}[]{#_Toc382817698}[]{#_Toc382818194}[]{#_Toc382818688}[]{#_Toc383006786}[]{#_Toc383007282}[]{#_Toc383529961}[]{#_Toc387072610}[]{#_Toc382815211}[]{#_Toc382817699}[]{#_Toc382818195}[]{#_Toc382818689}[]{#_Toc383006787}[]{#_Toc383007283}[]{#_Toc383529962}[]{#_Toc387072611}[]{#_Toc382815213}[]{#_Toc382817701}[]{#_Toc382818197}[]{#_Toc382818691}[]{#_Toc383006789}[]{#_Toc383007285}[]{#_Toc383529964}[]{#_Toc387072613}[]{#_Toc382815214}[]{#_Toc382817702}[]{#_Toc382818198}[]{#_Toc382818692}[]{#_Toc383006790}[]{#_Toc383007286}[]{#_Toc383529965}[]{#_Toc387072614}[]{#_Toc382815215}[]{#_Toc382817703}[]{#_Toc382818199}[]{#_Toc382818693}[]{#_Toc383006791}[]{#_Toc383007287}[]{#_Toc383529966}[]{#_Toc387072615}[]{#_Toc382815216}[]{#_Toc382817704}[]{#_Toc382818200}[]{#_Toc382818694}[]{#_Toc383006792}[]{#_Toc383007288}[]{#_Toc383529967}[]{#_Toc387072616}[]{#_Toc382815217}[]{#_Toc382817705}[]{#_Toc382818201}[]{#_Toc382818695}[]{#_Toc383006793}[]{#_Toc383007289}[]{#_Toc383529968}[]{#_Toc387072617}[]{#_Toc382815218}[]{#_Toc382817706}[]{#_Toc382818202}[]{#_Toc382818696}[]{#_Toc383006794}[]{#_Toc383007290}[]{#_Toc383529969}[]{#_Toc387072618}[]{#_Toc382815219}[]{#_Toc382817707}[]{#_Toc382818203}[]{#_Toc382818697}[]{#_Toc383006795}[]{#_Toc383007291}[]{#_Toc383529970}[]{#_Toc387072619}[]{#_Toc382815220}[]{#_Toc382817708}[]{#_Toc382818204}[]{#_Toc382818698}[]{#_Toc383006796}[]{#_Toc383007292}[]{#_Toc383529971}[]{#_Toc387072620}[]{#_Toc382815221}[]{#_Toc382817709}[]{#_Toc382818205}[]{#_Toc382818699}[]{#_Toc383006797}[]{#_Toc383007293}[]{#_Toc383529972}[]{#_Toc387072621}[]{#_Toc382815222}[]{#_Toc382817710}[]{#_Toc382818206}[]{#_Toc382818700}[]{#_Toc383006798}[]{#_Toc383007294}[]{#_Toc383529973}[]{#_Toc387072622}[]{#_Toc382815223}[]{#_Toc382817711}[]{#_Toc382818207}[]{#_Toc382818701}[]{#_Toc383006799}[]{#_Toc383007295}[]{#_Toc383529974}[]{#_Toc387072623}[]{#_Toc382815224}[]{#_Toc382817712}[]{#_Toc382818208}[]{#_Toc382818702}[]{#_Toc383006800}[]{#_Toc383007296}[]{#_Toc383529975}[]{#_Toc387072624}[]{#_Toc382815225}[]{#_Toc382817713}[]{#_Toc382818209}[]{#_Toc382818703}[]{#_Toc383006801}[]{#_Toc383007297}[]{#_Toc383529976}[]{#_Toc387072625}

**Event MIB \-- Event MIB配置命令 \-- wildcard context (Action-set view)**

------------------------------------------------------------------------

[**[wildcard ]{lang="EN-US" style="border:none windowtext 1.0pt;padding:0cm"}[context]{lang="EN-US"}**]{#struct_0_x1862_90986_376621009}[命令用来配置]{style="font-family:宋体"}[Set]{lang="EN-US"}[对象所在的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[上下文的匹配方式为通配。]{style="font-family:宋体"}

[**[undo wildcard context]{lang="EN-US"}**]{#struct_0_x1862_90986_x1232385264}[用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x322037231}

[**[wildcard context]{lang="EN-US"}**]{#struct_0_x1862_90986_1025149914}

[**[undo wildcard context]{lang="EN-US"}**]{#struct_0_x1862_90986_x300004043}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1427817190}

[[Set]{lang="EN-US"}]{#struct_0_x1862_90986_x300499388}[对象所处的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[上下文的匹配方式为精确匹配。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x173602083}

[[Action-set]{lang="EN-US"}]{#struct_0_x1862_90986_x552045433}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1549227360}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x1375030008}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_602518595}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1301592108}

[[本命令和]{style="font-family:宋体"}**[context]{lang="EN-US"}**]{#struct_0_x1862_90986_657472017}[命令配合使用，共同决定]{style="font-family:宋体"}[Set]{lang="EN-US"}[对象所在的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[上下文。精确匹配表示配置为特定的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[上下文环境名，而通配有两部分组成，一部分为]{style="font-family:宋体"}[mteEventSetContextName]{lang="EN-US"}[指定的]{style="font-family:宋体"}[contextname]{lang="EN-US"}[，另一部分为由]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[表中]{style="font-family:宋体"}[contextName]{lang="EN-US"}[的通配部分。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x2003298695}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_x1551388934}[配置]{style="font-family:宋体"}[Set]{lang="EN-US"}[对象所处的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[上下文环境名为]{style="font-family:宋体"}[contextname1]{lang="EN-US"}[的匹配方式为通配。]{style="font-family:宋体"}

[[\<Sysname\>system-view]{lang="EN-US"}]{#struct_0_x1862_90986_x478542577}

[\[Sysname\] snmp mib event owner owner1 name EventA]{lang="EN-US"}

[\[Sysname-event-owner1-EventA\] action set]{lang="EN-US"}

[\[Sysname-event-owner1-EventA-set\] context contextname1]{lang="EN-US"}

[\[Sysname-event-owner1-EventA-set\] wildcard context]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x521999463}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event owner]{lang="EN-US"}**]{#struct_0_x1862_90986_1759910701}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[action set]{lang="EN-US"}**]{#struct_0_x1862_90986_x986110999}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[context]{lang="EN-US"}**]{#struct_0_x1862_90986_x385399712}
:::

::: {#-930057038 .myid}
[]{#_Toc404797096}[]{#struct_0_x1862_90986_x159837107}

**Event MIB \-- Event MIB配置命令 \-- wildcard oid (Trigger view)**

------------------------------------------------------------------------

[**[wildcard oid]{lang="EN-US"}**]{#struct_0_x1862_90986_x2118129374}[命令用来配置]{style="font-family:宋体"}[Trigger]{lang="EN-US"}[采样的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[节点的匹配方式为通配。]{style="font-family:宋体"}

[**[undo wildcard oid]{lang="EN-US"}**]{#struct_0_x1862_90986_x970537647}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x183875221}

[**[wildcard oid ]{lang="EN-US"}**]{#struct_0_x1862_90986_x1077769097}

[**[undo wildcard oid]{lang="EN-US"}**]{#struct_0_x1862_90986_x411675772}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1865076559}

[[Trigger]{lang="EN-US"}]{#struct_0_x1862_90986_x2120867894}[采样的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[节点匹配方式为精确匹配。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x2120709980}

[[Trigger]{lang="EN-US"}]{#struct_0_x1862_90986_944285249}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1247377703}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_378141938}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x1729151186}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_858674885}

[[本命令与]{style="font-family:宋体"}**[oid]{lang="EN-US"}**]{#struct_0_x1862_90986_436792348}[命令配合使用，共同决定监控的对象：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当匹配类型为精确匹配时，表示]{lang="EN-US" style="font-family:宋体"}**[oid]{lang="EN-US"}**]{#struct_0_x1862_90986_x1333028023}[命令指定的监控对象为一个具体的实例，比如需要监控接口索引为]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}[的接口描述节点，则配置]{lang="EN-US" style="font-family:宋体"}**[oid]{lang="EN-US"}**[ ifDescr.2]{lang="EN-US"}[，匹配类型配置为精确匹配。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当匹配类型为通配时，表示]{style="font-family:宋体"}]{#struct_0_x1862_90986_610753981}**[oid]{lang="EN-US"}**[命令只指定了监控对象的]{style="font-family:宋体"}[OID]{lang="EN-US"}[前缀，系统中存在的所有]{style="font-family:宋体"}[MIB]{lang="EN-US"}[对象只要前缀与此相同均作为监控对象，比如需要监控所有接口对应的接口描述节点，则配置]{style="font-family:宋体"}**[oid]{lang="EN-US"}**[ ifDescr]{lang="EN-US"}[，并将匹配类型配置为通配。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1150623506}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_1965541118}[配置]{style="font-family:宋体"}[triggerr]{lang="EN-US"}[采样的节点值为]{style="font-family:宋体"}[1.3.6.1.2.1.1.6]{lang="EN-US"}[，采样节点匹配方式为通配。]{style="font-family:宋体"}

[[\<Sysname\>system-view]{lang="EN-US"}]{#struct_0_x1862_90986_595969989}

[\[Sysname\] snmp mib event trigger owner owner1 name triggerA]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA\] oid 1.3.6.1.2.1.1.6 ]{lang="EN-US"}

[\[Sysname-trigger-owner1-triggerA\] wildcard oid ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1839940871}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event trigger]{lang="EN-US"}**]{#struct_0_x1862_90986_384832503}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[oid]{lang="EN-US"}]{#struct_0_x1862_90986_1188879649}
:::

::: {#-459962079 .myid}
[]{#_Toc404797097}[]{#struct_0_x1862_90986_120866353}[]{#_Toc401850401}

**Event MIB \-- Event MIB配置命令 \-- wildcard oid (Action-se view)**

------------------------------------------------------------------------

[**[wildcard oid]{lang="EN-US"}**]{#struct_0_x1862_90986_x449138934}[命令用来配置]{style="font-family:宋体"}[Set]{lang="EN-US"}[操作对象的]{style="font-family:宋体"}[匹配方式为通配]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[wildcard oid]{lang="EN-US"}**]{#struct_0_x1862_90986_330151330}[命令用来恢复缺省情况。]{style="font-family:宋体;color:black"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x509499598}

[**[wildcard oid]{lang="EN-US"}**]{#struct_0_x1862_90986_1104415453}

[**[undo wildcard oid]{lang="EN-US"}**]{#struct_0_x1862_90986_1298229864}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1274724482}

[[Set]{lang="EN-US"}]{#struct_0_x1862_90986_1544243368}[操作对象的]{style="font-family:宋体"}[匹配方式为]{style="font-family:宋体;color:black"}[精确匹配。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1667790680}

[[Action-set]{lang="EN-US"}]{#struct_0_x1862_90986_440806996}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1065146284}

[[network-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x255916699}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1862_90986_x973195435}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1862_90986_1629904844}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S]{lang="EN-US"}[et]{lang="EN-US"}]{#struct_0_x1862_90986_132931664}[对象的]{lang="EN-US" style="font-family:宋体"}[OID]{lang="EN-US"}[属性为通配，表示]{lang="EN-US" style="font-family:宋体"}[S]{lang="EN-US"}[et]{lang="EN-US"}[对象的]{lang="EN-US" style="font-family:宋体"}[OID]{lang="EN-US"}[由两部分组成：一部分为]{lang="EN-US" style="font-family:宋体"}[mteEventSetObject]{lang="EN-US"}[指定的]{lang="EN-US" style="font-family:宋体"}[OID]{lang="EN-US"}[，另一部分为由]{lang="EN-US" style="font-family:宋体"}[Trigger]{lang="EN-US"}[表中监控对象]{lang="EN-US" style="font-family:宋体"}[OID]{lang="EN-US"}[的通配部分；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Set]{lang="EN-US"}]{#struct_0_x1862_90986_x545305911}[对象的]{style="font-family:宋体"}[OID]{lang="EN-US"}[属性为精确匹配：表示]{style="font-family:宋体"}[oid]{lang="EN-US"}[命令指定的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[节点]{style="font-family:宋体"}[OID]{lang="EN-US"}[即为]{style="font-family:宋体"}[Set]{lang="EN-US"}[对象的]{style="font-family:宋体"}[OID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1862_90986_544518970}

[[\# ]{lang="EN-US"}]{#struct_0_x1862_90986_1797016614}[配置用户名]{style="font-family:宋体"}[name1]{lang="EN-US"}[，事件名为]{style="font-family:宋体"}[EventA]{lang="EN-US"}[的]{style="font-family:宋体"}[Set]{lang="EN-US"}[对象]{style="font-family:宋体"}[OID]{lang="EN-US"}[为]{style="font-family:宋体"}[1.3.6.1.2.1.2.2.1.7]{lang="EN-US"}[的匹配方式为通配。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1862_90986_x23182877}

[\[Sysname\] snmp mib event owner owner1 name EventA]{lang="EN-US"}

[\[Sysname-event-owner1-EventA\] action set]{lang="EN-US"}

[\[Sysname-event-owner1-EventA-set\] oid 1.3.6.1.2.1.2.2.1.7]{lang="EN-US"}

[\[Sysname-event-owner1-EventA-set\] wildcard oid]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1862_90986_x1246132244}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp mib event owner]{lang="EN-US"}**]{#struct_0_x1862_90986_104513190}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[action set]{lang="EN-US"}**]{#struct_0_x1862_90986_x934954926}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oid]{lang="EN-US"}**]{#struct_0_x1862_90986_1061092675}
:::
