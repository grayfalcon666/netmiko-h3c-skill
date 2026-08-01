<!-- CMD-INDEX
  action                              | Event视图          | L50
  comparison                          | Trigger-boolean视图 | L118
  context (Trigger view)              | Trigger视图        | L184
  context (Action-set view)           | Action-set视图     | L236
  delta falling                       | Trigger-threshold视图 | L292
  delta rising                        | trigger-threshold视图 | L354
  description (Trigger view)          | Trigger视图        | L418
  description (Event view)            | Event视图          | L464
  display snmp mib event              | 任意视图             | L510
  display snmp mib event event        | 任意视图             | L652
  display snmp mib event object list  | 任意视图             | L800
  display snmp mib event summary      | 任意视图             | L882
  display snmp mib event trigger      | 任意视图             | L968
  event enable                        | Event视图          | L1298
  event owner (Trigger-boolean view)  | Trigger-boolean视图 | L1346
  event owner (Trigger-existence view) | Trigger-existence视图 | L1402
  falling                             | Trigger-threshold视图 | L1458
  frequency                           | Trigger视图        | L1520
  object list owner (Trigger view)    | Trigger视图        | L1574
  object list owner (Trigger-boolean view) | Trigger-boolean视图 | L1636
  object list owner (Trigger-existence view) | Trigger-existence视图 | L1692
  object list owner (Trigger-threshold view) | Trigger-threshold视图 | L1748
  object list owner (Action-notification view) | Action-notification视图 | L1804
  oid (Trigger view)                  | Trigger视图        | L1858
  oid (Action-set view)               | Action-set视图     | L1910
  oid (Action-notification view)      | Action-notification视图 | L1966
  rising                              | Trigger-threshold视图 | L2020
  sample                              | Trigger视图        | L2084
  snmp mib event owner                | 系统视图             | L2140
  snmp mib event object list          | 系统视图             | L2198
  snmp mib event sample instance maximum | 系统视图             | L2256
  snmp mib event sample minimum       | 系统视图             | L2308
  snmp mib event trigger              | 系统视图             | L2360
  snmp-agent trap enable event-mib    | 系统视图             | L2410
  startup (Trigger-existence view)    | Trigger-existence视图 | L2452
  startup (Trigger-threshold view)    | Trigger-threshold视图 | L2512
  startup enable                      | Trigger-boolean视图 | L2578
  test                                | Trigger视图        | L2632
  trigger enable                      | trigger视图        | L2686
  type                                | Trigger-existence视图 | L2740
  value (Trigger-boolean view)        | Trigger-boolean视图 | L2808
  value (Action-set view)             | Action-set视图     | L2860
  wildcard context (Trigger view)     | Trigger视图        | L2912
  wildcard context (Action-set view)  | Action-set视图     | L2966
  wildcard oid (Trigger view)         | Trigger视图        | L3020
  wildcard oid (Action-se view)       | Action-set视图     | L3074
-->

**Event MIB \-- Event MIB配置命令 \-- action**

------------------------------------------------------------------------

**[action**]命令用来配置事件包含的动作。

**[undo action**]命令用来恢复缺省情况。

【命令】

**[action ****[ notification **[\|]** set **}]

**[undo action ****[ notification **[\|]** set **}]

【缺省情况】]

该事件没有包含任何动作。]

【视图】

Event视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[notificaton**]：指定事件包含告警动作，当对应的事件被触发时，则向网管发送指定的告警信息。

**[set**]：指定事件包含设置动作，当对应的事件被触发时，可以对指定的MIB节点的值进行设置。

【使用指导】

当对应事件被触发后，可以配置的执行动作类型包括Set和Notification。同一个事件可以配置两种动作。

·如果动作指定为Set类型，则系统自动生成对应的Set表，同时进入Action-set视图，进行Set表的相关配置。具体配置请参见Action-set视图下的配置。

·如果动作指定为Notification类型，则自动生成相对应Notification表，同时进入Notification视图，进行Notification表的相关配置。具体配置请参见Action-notification视图下的配置。

【举例】

\# 配置用户事件的动作类型为Set和Notification，设置节点名ipForwarding.0的值为2，告警类型为mteEventSetFailure。

\<Sysname\> system-view

Sysname snmp mib event owner owner1 name EventA

Sysname-event-owner1-EventA action notification

Sysname-event-owner1-EventA-notification oid mteEventSetFailure

Sysname-event-owner1-EventA-notification quit

Sysname-event-owner1-EventA action set

Sysname-event-owner1-EventA-set oid ipForwarding.0

Sysname-event-owner1-EventA-set value 2

【相关命令】

·**snmp mib event **

·**event enable**

**Event MIB \-- Event MIB配置命令 \-- comparison**

------------------------------------------------------------------------

**[comparison**]命令用来指定Trigger-boolean视图下的检测子类型，表示采样值与参考值之间的比较方式。

**[undo comparison**]命令用来恢复缺省情况。

【命令】

**[comparison**[ { **equal** \| **greater** \| **greaterOrEqual** \| **less** \| **lessOrEqual** \| **unequal** }]]

**[undo comparison**]

【缺省情况】

采样值与参考值的比较方式为unequal。

【视图】

Trigger-boolean视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[equal**]：采样值与参考值的比较方式为equal，即当采样值等于参考值时，满足检测条件。

**[greater**]：采样值与参考值的比较方式为greater，即当采样值大于参考值时，满足检测条件。

**[greaterOrEqual**]：采样值与参考值的比较方式为greaterOrEqual，即当采样值大于等于参考值时，满足检测条件。

**[less**]：采样值与参考值的比较方式为less，即当采样值小于参考值时，满足检测条件。

**[lessOrEqual**]：采样值与参考值的比较方式为lessOrEqual，即当采样值小于等于参考值时，满足检测条件。

**[unequal**]：采样值与参考值的比较方式为unequal，即当采样值不等于参考值时，满足检测条件。

【使用指导】

·被监控的节点为非首次采样，本次采样值满足条件且上次采样值不满足条件则触发指定事件，也就是说如果连续两次采样均满足条件，只在第一次触发指定事件。

·被监控节点为首次采样，只有配置了**startup enable**命令后才会触发指定事件。

【举例】

\# 配置采样值与参考值的比较方式为Unequal。

\<Sysname\> system-view

Sysname snmp mib event trigger owner owner1 name triggerA

Sysname-trigger-owner1-triggerA test boolean

Sysname-trigger-owner1-triggerA-boolean comparison unequal

【相关命令】

·**snmp mib event trigger**

·**test**

**Event MIB \-- Event MIB配置命令 \-- context (Trigger view)**

------------------------------------------------------------------------

**[context**]命令用来配置监控对象所在的SNMP上下文环境。

**[undo context**]命令用来恢复缺省情况。

【命令】

**[context ***context-name*]

**[undo context**]

【缺省情况】

没有配置监控对象所在的SNMP上下文环境。

【视图】

Trigger视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[context-name*]：指定监控对象所在的SNMP上下文，为1～32个字符的字符串，区分大小写[。]

【使用指导】

配置SNMP上下文用于确定唯一的监控对象的节点实例。

【举例】

\# 配置监控对象所在的SNMP上下文为contextname1。

\<Sysname\> system-view

Sysname snmp mib event trigger owner owner1 name triggerA

Sysname-trigger-owner1-triggerA context contextname1

【相关命令】

·**snmp mib event trigger**

·**wildcard context**

**Event MIB \-- Event MIB配置命令 \-- context (Action-set view)**

------------------------------------------------------------------------

**[context**]命令用来配置Set对象所处的SNMP上下文。

**[undo context**]命令用来恢复缺省情况。

【命令】

**[context **context-name]

**[undo context**]

【缺省情况】

没有配置Set对象所处的SNMP上下文。

【视图】

Action-set视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[context-name*]：指定Set对象所处的SNMP上下文，为1～32个字符的字符串，区分大小写[。]

【使用指导】

配置SNMP上下文用于确定唯一的Set对象的节点实例。

【举例】

\# 配置Set对象所处的SNMP上下文为contextname1。

\<Sysname\>system-view

Sysname snmp mib event owner owner1 name EventA

Sysname-event-owner1-EventA action set

Sysname-event-owner1-EventA-set context contextname1

【相关命令】

·**snmp mib event owner**

·**action**

·**wildcard context**

**Event MIB \-- Event MIB配置命令 \-- delta falling**

------------------------------------------------------------------------

**[delta falling**]命令用来配置差值采样类型的下限阈值，并指定采样值小于等于该阈值时对应的触发事件。

**[undo delta falling**]命令用来恢复缺省情况。

【命令】

**[delta****falling**[{ **event** **owner** *event-owner* **name** *event-name* \| **value** *integer-value* }]]

**[undo****delta****falling**[ { **event** \| **value** }]]

【缺省情况】

下限阈值为0，且没有指定对应的触发事件。

【视图】

Trigger-threshold视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[event****owner*** event-owner*]：配置差值采样类型下限阈值对应事件的所有者，与Trigger表中配置的Trigger所有者owner相同。

**[name*** event-name*]：配置差值采样类型下限阈值对应的事件名，为1\~32个字符的字符串，区分大小写。

**[value***integer-value*]：差值采样类型的下限阈值，可以配置任意不大于差值采样类型上限阈值的整数。

【使用指导】

采样类型为差值采样时，采样差值小于或达到差值采样类型下限阈值时，将触发对应的事件。

若采样值连续多次小于或达到下限阈值，只会在第一次触发对应的事件，上限和下限对应事件的触发是交替产生的。

【举例】

\# 配置差值采样类型的下限阈值为20。

\<Sysname\> system-view

Sysname snmp mib event trigger owner owner1 name triggerA

Sysname-trigger-owner1-triggerA test threshold

Sysname-trigger-owner1-triggerA-threshold delta falling value 20

【相关命令】

·**snmp mib event trigger**

·**test **

·**sample**

**Event MIB \-- Event MIB配置命令 \-- delta rising**

------------------------------------------------------------------------

**[delta****rising**]命令用来配置差值采样类型的上升阈值，并指定采样值大于等于该阈值对应的触发事件。

**[undo****delta****rising**]命令用来恢复缺省情况。

【命令】

**[delta****rising**[{ **event** **owner** *event-owner* **name** *event-name* \| **value** *integer-value* }]]

**[undo****delta****rising **[{ **event** \| **value** }]]

【缺省情况】

上限阈值为0，且没有指定对应的触发事件。

【视图】

trigger-threshold视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[event****owner*** event-owner*]：配置差值上限阈值事件的所有者，与Trigger表中配置的Trigger所有者owner相同。

**[name*** event-name*]：配置差值上限阈值的事件，为1\~32个字符的字符串，区分大小写。

**[value***integer-value*]：差值上限阈值，可以配置任意不小于差值下限阈值的整数。

【使用指导】

采样类型为差值采样时，采样差值达到或超过上限阈值，将触发对应的事件。

若采样值连续多次达到或超过上限阈值，只会在第一次触发对应的事件，上限和下限对应事件的触发是交替产生的。

【举例】

\# 配置差值采样类型的差值上限阈值为50，对应的事件所有者为owner1，事件名为event1。

\<Sysname\> system-view

Sysname snmp mib event trigger owner owner1 name triggerA

Sysname-trigger-owner1-triggerA test threshold

Sysname-trigger-owner1-triggerA-threshold delta rising value 50

Sysname-trigger-owner1-triggerA-threshold delta rising event owner owner1 name event1

【相关命令】

·**snmp mib event trigger**

·**test **

·**sample**

**Event MIB \-- Event MIB配置命令 \-- description (Trigger view)**

------------------------------------------------------------------------

**[description**]命令用来配置Trigger使用功能的描述信息。

**[undo description**]命令用来恢复缺省情况。

【命令】

**[description** *trigger-description*]

**[undo description**]

【缺省情况】

没有配置Trigger使用功能的描述信息。

【视图】

Trigger视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[trigger-description*]：Trigger使用功能的描述信息，为1～255个字符的字符串，区分大小写。

【举例】

\# 配置所有者为owner1名称为triggerA的Trigger描述信息为"triggerA is configured for network management events"。

\<Sysname\> system-view

Sysname snmp mib event trigger owner owner1 name triggerA

Sysname-trigger-owner1-triggerA description triggerA is configured for network management events

【相关命令】

·**snmp mib event trigger**

**Event MIB \-- Event MIB配置命令 \-- description (Event view)**

------------------------------------------------------------------------

**[description**]命令用来配置Event的描述信息。

**[undo description**]命令用来恢复缺省情况。

【命令】

**[description** *event-description*]

**[undo description**]

【缺省情况】

没有任何描述信息。

【视图】

Event视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[event-description*]：Event的描述信息，为1～255个字符的字符串，区分大小写。

【举例】

\# 配置拥有者为owner1的事件EventA的描述信息为"EventA is an RMON event"。

\<Sysname\> system-view

Sysname snmp mib event owner owner1 name EventA

Sysname-event-owner1-EventA description EventA is an RMON event

【相关命令】

·**snmp mib event owner**

**Event MIB \-- Event MIB配置命令 \-- display snmp mib event**

------------------------------------------------------------------------

**[display** **snmp mib event**]命令用来显示所有Event MIB相关配置及统计信息。

【命令】

**[display snmp mib event**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

显示所有Event MIB相关配置信息及统计信息，包括获取触发事件名称、功能描述、动作类型、使能及实体控制状态。

【举例】

\# 显示设备当前所有的Event MIB配置信息和统计信息。

\<Sysname\>display snmp mib event

TriggerFailures               : 0

EventFailures                 : 0

SampleMinimum                 : 1

SampleInstanceMaximum         : 0

SampleInstance                : 0

SampleInstancesHigh           : 0

SampleInstanceLacks           : 0

Trigger entry triggerA owned by owner1:

  TriggerComment              : triggerA is to monitor the state of the interface

  TriggerTest                 : boolean

  TriggerSampleType           : absoluteValue

  TriggerValueID              : 1.3.6.1.2.1.2.2.1.7.3\<ifAdminStatus.3\>

  TriggerValueIDWildcard      : false

  TriggerTargetTag            : N/A

  TriggerContextName          : context1

  TriggerContextNameWildcard  : true

  TriggerFrequency(in seconds): 600

  TriggerEnabled              : true

  Boolean entry:

   BoolCmp                    : unequal

   BoolValue                  : 1

   BoolStartUp                : true

   BoolObjOwner               : owner1

   BoolObjName                : Objects1

   BoolEvtOwner               : N/A

   BoolEvtName                : N/A

Event entry eventA owned by owner2:

  EvtComment                  : event is to set ifAdminStatus

[  EvtAction                   : Notification \| Set]

  EvtEnabled                  : true

  Notification entry:

   NotifyOID                  : 1.3.6.1.2.1.88.2.0.1\<mteTriggerFired\>

   NotifyObjOwner             : N/A

   NotifyObjName              : N/A

  Set entry:

   SetObj                     : 1.3.6.1.2.1.2.2.1.7\<ifAdminStatus\>

   SetObjWildcard             : true

   SetValue                   : 2

   SetTargetTag               : N/A

   SetContextName             : context1

   SetContextNameWildcard     : false

Object list objectA owend by owner3:

  ObjIndex                    : 1

  ObjID                       : 1.3.6.1.2.1.2.1.0\<ifNumber.0\>

  ObjIDWildcard               : false

Object list objectA owend by owner3:

  ObjIndex                    : 2

  ObjID                       : 1.3.6.1.2.1.2.2.1.2.0\<ifDescr.0\>

  ObjIDWildcard               : false

上述显示信息中相关字段解释详见各表显示信息描述表（ 表1-1(?1325784250#_Ref401909013)至[表]1-9(?1555338873#_Ref401909035)）。

【相关命令】

·**snmp mib event trigger**

·**snmp mib event **

·**snmp mib event object list**

**Event MIB \-- Event MIB配置命令 \-- display snmp mib event event**

------------------------------------------------------------------------

**[display snmp mib event event**]命令用来显示设备上已创建的Event表信息及其相应的Action表。

【命令】

**[display snmp mib event event ** **owner** *event-owner* **name** *event-name* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[owner*** event-owner ***name*** event-name*]：指定Event所有者及Event名称。Event所有者为SNMPv3用户；Event名称为1～32个字符的字符串，区分大小写。如不指定本参数，则显示设备上所有已创建的Event表及其相应的Action表信息。

【举例】

\# 显示已创建的Event所有者为owner2，Event名称为eventA的Event表项信息及其相应的Action表信息。

\<Sysname\>display snmp mib event event owner owner2 name eventA

Event entry eventA owned by owner2:

EvtComment                  : event is to set ifAdminStatus

[EvtAction                   : Notification \| Set]

EvtEnabled                  : true

Notification entry:

NotifyOID                  : 1.3.6.1.2.1.88.2.0.1\<mteTriggerFired\>

NotifyObjOwner             : N/A

NotifyObjName              : N/A

Set entry:

SetObj                     : 1.3.6.1.2.1.2.2.1.7\<ifAdminStatus\>

SetObjWildcard             : true

SetValue                   : 2

SetTargetTag               : N/A

SetContextName             : context1

SetContextNameWildcard     : false

表1-1 Event Entry显示信息描述表

字段

描述

Event entry *eventA* owned by *owner2*

*[owner2*]：事件所有者，为SNMPv3用户

*[eventA*]：事件名称

EvtComment

事件信息描述

EvtAction

事件动作，有Set和Notification两种动作

EvtEnabled

事件使能状态

表1-2 Notification Entry显示信息描述表

字段

描述

NotifyOID

告警OID ，OID类型为Trap节点

NotifyObjOwner

告警绑定对象所有者，为SNMPv3 用户

NotifyObjName

告警绑定对象组名

表1-3 Set Entry显示信息描述表

字段

描述

SetObj

事件设置对象的OID，OID类型为表节点、概念行节点、列节点、叶子节点、叶节点的父节点中的一种

SetObjWildcard

设置对象OID的通配标识符，取值为：

false：精确匹配

true：通配

SetValue

设置对象OID的值

SetTargetTag

设置对象远程标识符，长度为0的字符串表示为Local,本项目必须为空

SetContextName

事件设置对象上下文环境，缺省情况下位空，本项目必须指定

SetContextNameWildcard

事件设置对象的上下文通配标识符，取值为：

false：精确匹配

true：通配

【相关命令】

·**snmp mib event**

**Event MIB \-- Event MIB配置命令 \-- display snmp mib event object list**

------------------------------------------------------------------------

**[display snmp mib event object list**]命令用来显示设备上已创建的Object表的相关信息。

【命令】

**[display snmp mib event object list ** **owner** *objects-owner* **name** *objects-name* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[owner ***objects-owner*** name** *objects-name*]：指定对象组所有者及对象组名称。对象组所有者为SNMPv3用户，对象组名称为1～32个字符的字符串，区分大小写。如不指定本参数，则显示设备上所有已创建的Object表的信息。

【举例】

\# 显示已创建的对象组所有者为owner3、对象组名称为objectA的Object表项信息。

\<Sysname\> display snmp mib event object list owner owner3 name objectA

Object list objectA owned by owner3:

ObjIndex                    : 1

ObjID                       : 1.3.6.1.2.1.2.1.0\<ifNumber.0\>

ObjIDWildcard               : false

Object list objectA owned by owner3:

ObjIndex                    : 2

ObjID                       : 1.3.6.1.2.1.2.2.1.2.0\<ifDescr.0\>

ObjIDWildcard               : false

表1-4 display snmp mib event object list显示信息描述表

字段

描述

Object list *objectA* owned by *owner3*

*[owner3*]：绑定对象所有者，为SNMPv3用户，一级索引

*[objectA*]：绑定对象名，二级索引

ObjIndex

绑定对象的索引，三级索引

ObjID

绑定对象的OID，OID类型应为表节点、表中行节点、表中列节点、叶子节点、叶节点的父节点中的一种

ObjIDWildcard

绑定对象OID的通配标识符，取值为：

false：精确匹配

true：通配

【相关命令】

·**snmp mib event object list**

**Event MIB \-- Event MIB配置命令 \-- display snmp mib event summary**

------------------------------------------------------------------------

**[display snmp mib event summary**]命令用来显示Event MIB摘要信息。

【命令】

**[display snmp mib event summary**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

显示全局配置信息包括最小采样时间间隔和最大采样实例数；及显示相关统计值包括当前采样行实例数、采样行数峰值、达到最大采样行数限制而采样失败的行数、Trigger触发失败次数和执行相应Event失败次数。

【举例】

\# 显示Event MIB的摘要信息。

\<Sysname\> display snmp mib event summary

TriggerFailures               : 0

EventFailures                 : 0

SampleMinimum                 : 1

SampleInstanceMaximum         : 0

SampleInstance                : 0

SampleInstancesHigh           : 0

SampleInstanceLacks           : 0

表1-5 display snmp mib event summary显示信息描述表

字段

描述

TriggerFailures

Trigger触发测试失败的次数，缺省值为0

EventFailures

Trigger触发Notification或者Set动作失败的次数，缺省值为0

SampleMinimum

系统支持的最小采样时间间隔，缺省值为1

SampleInstanceMaximum

系统支持的最大采样行数

SampleInstance

当前活动状态的采样节点数，缺省值为0

SampleInstancesHigh

采样过程中达到的最大采样行数，缺省值为0

SampleInstanceLacks

由于超过系统支持的最大采样行数限制而采样失败的次数，缺省值为0

【相关命令】

·**display snmp mib event**

**Event MIB \-- Event MIB配置命令 \-- display snmp mib event trigger**

------------------------------------------------------------------------

**[display snmp mib event trigger**]命令用来显示设备上已创建的Trigger的相关信息及相应的Test表项信息。

【命令】

**[display snmp mib event trigger ** **owner** *trigger-owner* **name** *trigger-name* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[owner** *trigger-owner* **name** *trigger-name*]：显示指定所有者及指定名称的Trigger的相关信息，*trigger-owner*表示Trigger所有者，为SNMPv3用户；*trigger-name*表示Trigger名称，为1～32个字符的字符串，区分大小写。如不指定该参数，则显示设备上已创建的所有Trigger及Test表的相关信息。

【举例】

\# 显示已创建的所有者为owner1、名称为triggerA的Trigger信息及其相应的Test表信息。

\<Sysname\> display snmp mib event trigger owner owner1 name triggerA

Trigger entry triggerA owned by owner1:

  TriggerComment              : triggerA is to monitor the state of the interface

[  TriggerTest                 : existence \| boolean \| threshold]

  TriggerSampleType           : absoluteValue

  TriggerValueID              : 1.3.6.1.2.1.2.2.1.7.3\<ifAdminStatus.3\>

  TriggerValueIDWildcard      : false

  TriggerTargetTag            : N/A

  TriggerContextName          : context1

  TriggerContextNameWildcard  : true

  TriggerFrequency(in seconds): 600

TriggerObjOwner             : owner1

  TriggerObjName              : obj1

  TriggerEnabled              : true

Existence entry:

[   ExiTest                    : present \| absent]

[   ExiStartUp                 : present \| absent]

   ExiObjOwner                : owner1

   ExiObjName                 : object1

   ExiEvtOwner                : owner1

   ExiEvtName                 : event1

Boolean entry:

BoolCmp                    : unequal

BoolValue                  : 1

BoolStartUp                : true

BoolObjOwner               : owner1

BoolObjName                : Objects1

BoolEvtOwner               : N/A

BoolEvtName                : N/A

Threshold entry:

   ThresStartUp               : falling

   ThresRising                : 40

   ThresFalling               : 20

   ThresDeltaRising           : 40

   ThresDeltaFalling          : 20

   ThresObjOwner              : N/A

   ThresObjName               : N/A

   ThresRisEvtOwner           : owner1

   ThresRisEvtName            : event1

   ThresFalEvtOwner           : owner1

   ThresFalEvtName            : event1

   ThresDeltaRisEvtOwner      : owner1

   ThresDeltaRisEvtName       : event1

   ThresDeltaFalEvtOwner      : owner1

   ThresDeltaFalEvtName       : event1

表1-6 Trigger Entry显示信息描述表

字段

描述

Trigger entry *triggerA* owned by *owner1*

*[owner1*]：Trigger所有者

*[triggerA*]：Trigger名称

TriggerComment

Trigger的功能和使用描述

TriggerTest

Trigger触发条件的检测类型，取值分为existence、boolean和threshold三种类型

TriggerSampleType

Trigger触发采样类型，取值为：

absoluteValue：绝对值采样

deltaValue：差值采样

TriggerValueID

监控对象OID，节点类型限定为表节点、表中行节点、表中列节点、叶子节点、叶节点的父节点的一种

TriggerValueIDWildcard

监控对象OID通配标识符，取值为：

false：精确匹配

true：通配

TriggerTargetTag

标识监控对象所在的远程系统；N/A表示为Local，本项目必须为N/A

TriggerContextName

监控对象OID所处的上下文，缺省情况下为空，但本项目必须指定该参数，不能为空

TriggerContextNameWildcard

监控对象OID所处的上下文环境的通配标识符，分为精确匹配和通配

TriggerFrequency

Trigger采样间隔，此采样间隔应该大于或者等于系统支持的最小采样时间间隔

TriggerObjOwner

Trigger绑定对象所有者，为SNMPv3用户{.MsoCommentReference}

TriggerObjName

Trigger的绑定对象

TriggerEnabled

Trigger是否触发使能：

enabled：使能

disabled：未使能

表1-7 Existence Entry显示信息描述表

字段

描述

ExiTest

Existence触发条件类型，取值为present、absent和changed

ExiStartUp

Existence初始触发条件，取值为present、absent和changed

ExiObjOwner

Existence绑定对象所有者，为SNMPv3用户

ExiObjName

Existence的绑定对象

ExiEvtOwner

Existence触发事件所有者，为SNMPv3用户

ExiEvtName

Existence触发事件名

表1-8 Boolean Entry显示信息描述表

字段

描述

BoolCmp

Boolean比较的类型，取值为：

有6种比较类型equal、less、lessOrEqual、greater、greaterOrEqual，默认情况下是unequal比较对象TriggerValueID与BoolValue

BoolValue

Boolean参考值

BoolStartUp

初始触发条件，取值为true和false

BoolObjOwner

Boolean触发绑定对象所有者，为SNMPv3用户{.MsoCommentReference}

BoolObjName

Boolean触发的绑定对象

BoolEvtOwner

Boolean触发事件所有者，为SNMPv3用户{.MsoCommentReference}

BoolEvtName

Boolean触发的事件名

表1-9 Threshold Entry显示信息描述表

字段

描述

ThresStartUp

初始触发条件，取值为rising(1)、falling(2)和 risingOrFalling(3)

ThresRising

绝对值采样上升阈值

ThresFalling

绝对值采样下降阈值

ThresDeltaRising

差值采样下的上升阈值

ThresDeltaFalling

差值采样下的下降阈值

ThresObjOwner

阈值触发下绑定对象所有者

ThresObjName

阈值触发下的绑定对象

ThresRisEvtOwner

Rising触发事件所有者，为SNMPv3用户

ThresRisEvtName

Rising触发事件名

ThresFalEvtOwner

Falling触发事件所有者，为SNMPv3用户

ThresFalEvtName

Falling触发事件名

ThresDeltaRisEvtOwner

DeltaRising触发事件所有者，为SNMPv3用户

ThresDeltaRisEvtName

DeltaRising触发事件名

ThresDeltaFalEvtOwner

DeltaFalling触发事件所有者，为SNMPv3用户

ThresDeltaFalEvtName

DeltaFalling触发事件名

【相关命令】

·**snmp mib event trigger**

**Event MIB \-- Event MIB配置命令 \-- event enable**

------------------------------------------------------------------------

**[event enable**]命令用来使能事件触发功能。

**[undo event enable**]命令用来关闭事件触发功能。

【命令】

**[event enable**]

**[undo event enable**]

【缺省情况】

事件触发功能处于关闭状态。

【视图】

Event视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有满足Test检测条件且使能事件触发功能，才能触发相应的事件。

【举例】

\#使能事件所有者为owner1、名称为EventA事件的触发功能。{.TerminalDisplayChar}

\<Sysname\> system-view

Sysname snmp mib event owner owner1 name EventA

Sysname-event-owner1-EventA event enable

【相关命令】

·**snmp mib event**

·**action **

**Event MIB \-- Event MIB配置命令 \-- event owner (Trigger-boolean view)**

------------------------------------------------------------------------

**[event **]**owner**命令用来指定在Trigger-boolean视图下满足检测条件时触发的Event事件。

**[undo event**]命令用来恢复缺省情况。

【命令】

**[event **]**owner ***event-owner*** name ***event-name*

**[undo event**]

【缺省情况】

没有指定任何Event事件。

【视图】

Trigger-boolean视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[event-owner*]：触发事件的所有者，与trigger表中配置的trigger所有者owner相同。

*[event-name*]：触发事件名，为1\~32个字符的字符串，区分大小写。

【使用指导】

当满足触发条件时，就根据指定的触发事件的所有者和名称在配置的Event表中查找指定的Event事件是否存在；若存在，则执行该Event事件指定的动作。

【举例】

\# 配置在满足检测条件时所触发的Event事件。

\<Sysname\> system-view

Sysname snmp mib event trigger owner owner1 name triggerA

Sysname-trigger-owner1-triggerA test boolean

Sysname-trigger-owner1-triggerA-boolean event owner owner1 name event1

【相关命令】

·**snmp mib event trigger**

·**test**

**Event MIB \-- Event MIB配置命令 \-- event owner (Trigger-existence view)**

------------------------------------------------------------------------

**[event **]**owner**命令用来指定在Trigger-existence视图下，满足检测条件时触发的Event事件。

**[undo event**]命令用来恢复缺省情况。

【命令】

**[event **]**owner ***event-owner*** name ***event-name*

**[undo event**]

【缺省情况】

没有指定任何event事件。

【视图】

Trigger-existence视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[event-owner*]：指定触发事件的所有者，与Trigger表中配置的Trigger所有者owner相同。

*[event-name*]：指定触发事件名，为1\~32个字符的字符串，区分大小写。

【使用指导】

满足触发条件时，就会查找Event表，根据触发事件的所有者和名称查找配置的Event事件是否存在。若存在，则执行该Event事件指定的动作。

【举例】

\# 配置Trigger-existence子视图下，满足检测条件时所触发的Event事件。

\<Sysname\> system-view

Sysname snmp mib event trigger owner owner1 name triggerA

Sysname-trigger-owner1-triggerA test existence

Sysname-trigger-owner1-triggerA-existence event owner owner1 name event1

【相关命令】

·**snmp mib event trigger**

·**test **

**Event MIB \-- Event MIB配置命令 \-- falling**

------------------------------------------------------------------------

**[falling**]命令用来配置绝对值采样类型的下限阈值，并指定采样值小于等于该阈值时触发的事件。

**[undo****falling**]命令用来恢复缺省情况。

【命令】

**[falling**[{ **event** **owner** *event-owner* **name** *event-name* \| **value** *integer-value* }]]

**[undo****falling**[{ **event** \| **value** }]]

【缺省情况】

下限阈值为0，且未配置对应的触发事件。

【视图】

Trigger-threshold视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[event****owner*** event-owner*]：配置下限阈值对应事件的所有者，与Trigger表中配置的Trigger所有者owner相同。

**[name*** event-name*]：配置下限阈值对应的事件名，为1\~32个字符的字符串，区分大小写。

**[value***integer-value*]：绝对值采样的下限阈值，可以配置任意不大于上限阈值的整数。

【使用指导】

采样类型为绝对值采样时，采样值小于或达到下限阈值时，将触发对应的事件。

若采样值连续多次小于或达到下限阈值，只会在第一次触发对应的事件，上限和下限对应事件的触发是交替产生的。

【举例】

\# 配置绝对值采样类型的下限阈值为20。

\<Sysname\> system-view

Sysname snmp mib event trigger owner owner1 name triggerA

Sysname-trigger-owner1-triggerA test threshold

Sysname-trigger-owner1-triggerA-threshold falling value 20

【相关命令】

·**snmp mib event trigger**

·**test **

·**sample**

**Event MIB \-- Event MIB配置命令 \-- frequency**

------------------------------------------------------------------------

**[frequency**]命令用来配置Trigger采样时间间隔。

**[undo frequency**]命令用来恢复缺省情况。

【命令】

**[frequency ***interval*]

**[undo frequency **]

【缺省情况】

采样时间间隔为600秒。

【视图】

Trigger视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示Trigger采样时间间隔，为任意不小于系统支持的最小采样时间间隔的正整数，取值范围为1～4294967295，单位为秒。

【使用指导】

Trigger采样时间间隔必须不小于系统支持的最小采样时间间隔，最小采样时间间隔使用**snmp mib event sample minimum**命令配置。

如果采样节点较多且配置的采样间隔时间过短，可能出现下一次采样时本次采样尚未完成，将导致下一次的采样处理失败，因此请根据实际情况合理配置采样间隔。

【举例】

\# 配置Trigger采样时间间隔为360秒。

\<Sysname\> system-view

Sysname snmp mib event trigger owner owner1 name triggerA

Sysname-trigger-owner1-triggerA frequency 360

【相关命令】

·**snmp mib event trigger**

·**snmp mib event sample minimum**

**Event MIB \-- Event MIB配置命令 \-- object list owner (Trigger view)**

------------------------------------------------------------------------

**[object list owner**]命令用来指定绑定对象组。该Trigger触发Notification动作发送相应Trap时需要添加此绑定对象组中的绑定变量。

**[undo object list**]命令用来恢复缺省情况。

【命令】

**[object list owner ***objects-owner*** name ***objects-name*]

**[undo object list**]

【缺省情况】

没有指定绑定对象组。

【视图】

Trigger视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[owner*** objects-owner*]：指定Trigger绑定对象组的所有者，与Trigger表中配置的Trigger所有者相同。

**[name ***objects-name*]：指定Trigger绑定对象组名称，为1～32个字符的字符串，区分大小写。

【使用指导】

通过指定绑定对象组的所有者和名称来指定一个绑定对象组，每个绑定对象组的成员由**object list owner**命令指定；当Trigger触发的事件包含notification动作时，发送的SNMP Trap报文将携带配置的绑定变量。

发送Notification时需要的绑定对象组可以在三处指定：

·Trigger视图下的**object list owner**命令指定Trigger对应的绑定对象组，表示所有由本Trigger触发Notification事件时需要添加的绑定变量；

·Trigger-test视图(Trigger-boolean、Trigger-existence、Trigger-threshold)下的**object list owner**命令，统称为Trigger-test绑定对象组，表示满足此种检测类型所触发的Notification事件时需要添加的绑定变量；

·Notification视图下的**object list** owner命令指定Notification绑定对象组，表示引用此事件发送指定Notification事件时需要添加的绑定变量。

实际配置时可以只在其中的一处指定，二处指定，或者三处同时指定。当多处指定时，绑定变量添加到Trap报文中的顺序，应该为先添加Trigger绑定对象组中的变量，再添加Test绑定对象组中的变量，最后添加Notification绑定对象组中的变量。

【举例】

\# 配置Trigger绑定所有者为owner1，绑定对象组名称为objectA。

\<Sysname\> system-view

Sysname snmp mib event trigger owner owner1 name triggerA

Sysname-trigger-owner1-triggerA object list owner owner1 name objectA

【相关命令】

·**snmp mib event trigger**

**Event MIB \-- Event MIB配置命令 \-- object list owner (Trigger-boolean view)**

------------------------------------------------------------------------

**[object list owner**]命令用来指定绑定对象组，表示监控对象值满足Boolean检测条件且触发事件为Notification时，需要添加此绑定对象组中的绑定变量。

**[undo object list**]命令用来恢复缺省情况。

【命令】

**[object list owner ***objects-owner*** name ***objects-name*]

**[undo object list**]

【缺省情况】

没有指定绑定对象组。

【视图】

Trigger-boolean视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[objects-owner*]：指定Trigger绑定对象组的所有者，与Trigger表中配置的Trigger所有者owner相同。

*[objects-name*]：指定Trigger绑定对象组名称，为1～32个字符的字符串，区分大小写。

【使用指导】

参考Trigger视图下的**object list** **owner**命令。

【举例】

\# 配置绑定对象组，指定Trigger绑定对象组的所有者为owner1，绑定对象组名称为objectA。

\<Sysname\> system-view

Sysname snmp mib event trigger owner owner1 name triggerA

Sysname-trigger-owner1-triggerA test boolean

Sysname-trigger-owner1-triggerA-boolean object list owner owner1 name objectA

【相关命令】

·**snmp mib event trigger**

·**test **

**Event MIB \-- Event MIB配置命令 \-- object list owner (Trigger-existence view)**

------------------------------------------------------------------------

**[object list owner**]命令用来指定绑定对象组，表示监控对象值满足Existence检测条件且触发事件为Notification时，需要添加此绑定对象组中的绑定变量。

**[undo object list**]命令用来恢复缺省情况。

【命令】

**[object list owner ***objects-owner*** name ***objects-name*]

**[undo object list**]

【缺省情况】

没有指定绑定对象组。

【视图】

Trigger-existence视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[objects-owner*]：Trigger绑定对象组的所有者，与Trigger表中配置的Trigger所有者owner相同。

*[objects-name*]：Trigger绑定对象组名称，为1～32个字符的字符串，区分大小写。

【使用指导】

参考Trigger视图下的**object list owner**命令。

【举例】

\# 当监控对象值满足Trigger-existence测试条件后，系统执行Notification动作并发送Trap时需要绑定的对象组。

\<Sysname\> system-view

Sysname snmp mib event trigger owner owner1 name triggerA

Sysname-trigger-owner1-triggerA test existence

Sysname-trigger-owner1-triggerA-existence object list owner owner1 name objectA

【相关命令】

·**snmp mib event trigger**

·**test **

**Event MIB \-- Event MIB配置命令 \-- object list owner (Trigger-threshold view)**

------------------------------------------------------------------------

**[object****list****owner****name**]命令用来指定绑定对象组，表示监控对象值满足Threshold检测条件且触发事件为Notification时，需要添加此绑定对象组中的绑定变量。

**[undo****object****list**]命令用来恢复缺省情况。

【命令】

**[object****list****owner***objects-owner***name***objects-name*]

**[undo****object****list**]

【缺省情况】

没有指定绑定对象组。

【视图】

Trigger-threshold视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[objects-owner*]：Trigger绑定对象组的所有者，与Trigger表中配置的Trigger所有者owner相同。

*[objects-name*]：Trigger绑定对象组名称，为1～32个字符的字符串，区分大小写。

【使用指导】

参考Trigger视图下的**object list owner**命令。

【举例】

\# 配置对应的绑定对象组。

\<Sysname\> system-view

Sysname snmp mib event trigger owner owner1 name triggerA

Sysname-trigger-owner1-triggerA test threshold

Sysname-trigger-owner1-triggerA-threshold object list owner owner1 name objectA

【相关命令】

·**snmp mib event trigger**

·**test**

**Event MIB \-- Event MIB配置命令 \-- object list owner (Action-notification view)**

------------------------------------------------------------------------

**[object list owner**]命令用来指定绑定对象组，表示触发Notification事件时，需要在此绑定对象组中添加的绑定变量。

**[undo object list**]命令用来恢复缺省情况。

【命令】

**[object list owner ***objects-owner*** name ***objects-name*]

**[undo object list**]

【缺省情况】

没有指定绑定对象组。

【视图】

Action-notification视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[objects-owner*]：配置绑定对象的所有者，与对应Event配置的owner相同。

*[objects-name*]：配置绑定对象组名，为1～32个字符的字符串，区分大小写。

【使用指导】

本命令用来配置发送Notification时附加的引用Object表中的绑定对象组所包含的绑定变量，若不指定或者指定的绑定对象组为空，则不添加绑定变量。关于发送Notification的绑定变量描述请参见Trigger视图下的**object list owner name**的命令。

【举例】

\# 配置事件所有者为owner1 ，事件名为EventA，绑定对象组名为listA。

Sysname snmp mib event owner owner1 name EventA

Sysname-event-owner1-EventA action notification

Sysname-event-owner1-EventA-notification object list owner owner1 name listA

【相关命令】

·**snmp mib event owner**

·**action**

**Event MIB \-- Event MIB配置命令 \-- oid (Trigger view)**

------------------------------------------------------------------------

**[oid**]命令用来配置Trigger采样的MIB节点。

**[undo oid**]命令用来恢复缺省情况。

【命令】

**[oid ***object-identifier*]

**[undo oid **]

【缺省情况】

OID为0.0，表示没有配置Trigger采样的MIB节点，即没有指定Trigger的监控对象。

【视图】

Trigger视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[object-identifier*]：Trigger进行采样的MIB节点，即Trigger的监控对象。取值为节点OID或者节点名称。

【使用指导】

该命令用来指定MIB节点作为监控对象，当配置该命令后，该Trigger生效时将按指定的采样间隔周期性地获取该监控对象的值用来判定是否满足事件触发条件。

配置的OID可以是表节点，概念行节点，表中列节点，简单叶子节点，叶节点的父节点中的任意一种。

【举例】

\# 配置Trigger采样的节点值为1.3.6.1.2.1.2.2.1.1.3。

\<Sysname\> system-view

Sysname snmp mib event trigger owner owner1 name triggerA

Sysname-trigger-owner1-triggerA oid 1.3.6.1.2.1.2.2.1.1.3

【相关命令】

·**snmp mib event trigger**

**Event MIB \-- Event MIB配置命令 \-- oid (Action-set view)**

------------------------------------------------------------------------

**[oid**]命令用来配置事件Set操作对象的OID值。

**[undo oid**]命令用来恢复缺省情况。

【命令】

**[oid ***object-identifier*]

**[undo oid**]

【缺省情况】

OID为0.0，表示没有指定Set操作对象。

【视图】

Action-set视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[object-identifier*]：Set操作对象的OID，取值为节点OID值或者节点名称。

【使用指导】

配置的OID的值必须为表节点，概念行节点，表中列节点，简单叶子节点，叶节点的父节点中的任意一种。

【举例】

\# 设置用户名owner1，事件名为EventA的set对象的OID为1.3.6.1.2.1.2.2.1.7.3。

\<Sysname\> system-view

Sysname snmp mib event owner owner1 name EventA

Sysname-event-owner1-EventA action set

Sysname-event-owner1-EventA-set oid 1.3.6.1.2.1.2.2.1.7.3

【相关命令】

·**snmp mib event owner**

·**action**

·**wildcard oid******(Action-set view)

**Event MIB \-- Event MIB配置命令 \-- oid (Action-notification view)**

------------------------------------------------------------------------

**[oid**]命令用来配置执行Notification事件时需要发送的Notification的OID。

**[undo oid**]命令用来恢复缺省情况。

【命令】

**[oid ***object-identifier*]

**[undo oid**]

【缺省情况】

OID为0.0，表示没有指定发送Notification的OID。

【视图】

Action-notification视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[object-identifier*]：指定发送Notificaton的OID值，此OID对应的节点必须为告警节点。

【使用指导】

本命令用于配置事件类型为Notification时需要发送具体Notification的OID。

【举例】

\# 设置用户名为owner1，事件名为EventA发送的notificaton的OID为1.3.6.1.2.1.14.16.2.1。

\<Sysname\> system-view

Sysname snmp mib event owner owner1 name EventA

Sysname-event-owner1-EventA action notification

Sysname-event-owner1-EventA-notification oid 1.3.6.1.2.1.14.16.2.1

【相关命令】

·**snmp mib event owner **

·**action**

**Event MIB \-- Event MIB配置命令 \-- rising**

------------------------------------------------------------------------

**[rising**]命令用来配置绝对值采样类型的上限阈值，并指定采样值大于等于该阈值时触发的事件。

**[undo****rising**]命令用来恢复缺省情况。

【命令】

**[rising**[{ **event** **owner** *event-owner* **name** *event-name* \| **value** *integer-value* }]]

**[undo****rising**[{ **event** \| **value** }]]

【缺省情况】

上限阈值为0，未配置对应的触发事件。

【视图】

Trigger-threshold视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[event****owner*** event-owner*]：配置上限阈值事件的所有者，与Trigger配置的owner相同。

**[name*** event-name*]：配置上限阈值对应的事件名，为1\~32个字符的字符串，区分大小写。

**[value***integer-value*]：绝对值采样的上限阈值，可以配置任意不小于下限阈值的整数。

【使用指导】

采样类型为绝对值采样时，采样值达到或超过上限阈值时，将触发对应的事件。

若采样值连续多次达到或超过上限阈值，只会在第一次触发对应的事件，上限和下限对应事件的触发是交替产生的。

【举例】

\# 配置threshold测试的上限阈值为50，对应的事件所有者为owner1，事件名为event1。

\<Sysname\> system-view

Sysname snmp mib event trigger owner owner1 name triggerA

Sysname-trigger-owner1-triggerA test threshold

Sysname-trigger-owner1-triggerA-threshold rising value 50

Sysname-trigger-owner1-triggerA-threshold rising event owner owner1 name event1

【相关命令】

·**snmp mib event trigger**

·**test **

·**sample**

**Event MIB \-- Event MIB配置命令 \-- sample**

------------------------------------------------------------------------

**[sample**]命令用来配置Trigger采样的类型。

**[undo sample**]命令用来恢复缺省情况。

【命令】

**[sample**[ { **absolute** \| **delta** }]]

**[undo sample**]

【缺省情况】

Trigger采样类型为绝对值采样。

【视图】

Trigger视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[absolute**]：[采样类型为绝对值采样，即采样时间到达时直接获取监控对象的值。]

**[delta**]：[采样类型为差值采样，即采样时间到达时获取的是监控对象本次与上次采样的差值。]

【使用指导】

采样类型为差值采样时，获取本次差值的算法与对应监控对象值类型有关。

·如果监控对象值类型为UINT类型，则获取本次差值算法：本次采样值与前一次采样值比较，取两者中的较大值减去较小值，保证差值为正值（即也为UINT类型）；

·如果监控对象值类型为INT类型，则获取本次差值算法：当前采样值减去前一次采样值取差值。

【举例】

\# 配置Trigger采样的类型为绝对值采样。

\<Sysname\>system-view

Sysname snmp mib event trigger owner owner1 name triggerA

Sysname-trigger-owner1-triggerA sample absolute

【相关命令】

·**snmp mib event trigger**

**Event MIB \-- Event MIB配置命令 \-- snmp mib event owner**

------------------------------------------------------------------------

**[snmp mib event owner**]命令用来创建一个Event并进入Event视图，若Event已经存在，则直接进入该Event视图。

**[undo snmp mib event**]命令用来删除一个已存在的event。

【命令】

**[snmp mib event owner ***event-owner*** name** *event-name* ]

**[undo snmp mib event owner ***event-owner*** name** *event-name*]

【缺省情况】

不存在任何Event。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[event-owner*]：事件所有者，应该指定为已存在的SNMPv3用户。

*[event-name*]：创建的事件名，为1～32个字符的字符串，区分大小写。

【使用指导】

事件由所有者和事件名唯一识别。进入Event视图后可以配置事件描述、事件动作和事件使能。

【举例】

\# 创建一个事件，其所有者为owner1，事件名为EventA，并进入该Event视图。

\<Sysname\> system-view

Sysname snmp mib event owner owner1 name EventA

Sysname-event-owner1-EventA

【相关命令】

·**snmp mib event**

·**description**

·**event enable**

·**action **

**Event MIB \-- Event MIB配置命令 \-- snmp mib event object list**

------------------------------------------------------------------------

**[snmp mib event object list**]命令用来配置事件的绑定对象组的信息。

**[undo snmp mib event object list**]命令用来恢复缺省情况。

【命令】

**[snmp mib event object list******owner ***objects-owner*** name** *objects-name* *objects-index* **oid** *object-identifier* [ **wildcard** ]]

**[undo snmp mib event object list owner ***objects-owner*** name** *objects-name* *objects-index*]

【缺省情况】

没有指定绑定对象组。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[owner*** objects-owner*]：对象组所有者，应该指定为已存在的SNMPv3用户。

**[name*** objects-name*]：创建的对象组名，其中组名为1～32个字符的字符串，区分大小写。

*[objects-index*]：绑定对象表的三级索引，取值范围为1～4294967295。

**[oid*** object-identifier*]：绑定的对象，取值为该对象节点OID值或者节点名称。配置的OID的值必须为表节点，概念行节点，表中列节点，简单叶子节点，叶节点的父节点中的任意一种。

**[wildcard**]：表示绑定对象的匹配方式为通配。如未指定该参数，则表示绑定对象的匹配方式为精确匹配。

【使用指导】

绑定的对象由对象组所有者、对象组名和对象表的三级索引唯一确定，用来配置事件的绑定对象组的信息。Event事件对应动作为Notification，发送相应的Trap时可以从该配置的绑定对象组中获取信息。Notification绑定的对象组信息是向网管提供其关心的相关数据。

【举例】

\# 配置一个对象列表的信息，其中对象组所有者为owner1，创建的对象组名为objectA，绑定对象表的三级索引为10，绑定对象节点OID值为1.3.6.1.2.1.2.2.1.1.3。

\<Sysname\> system-view

Sysname snmp mib event object list owner owner1 name objectA 10 oid 1.3.6.1.2.1.2.2.1.1.3

【相关命令】

·**snmp mib event**

·**snmp mib event trigger**

**Event MIB \-- Event MIB配置命令 \-- snmp mib event sample instance maximum**

------------------------------------------------------------------------

**[snmp mib event sample instance** **maximum**]命令用来设置系统支持的最大监控对象数，即最大采样实例数。

**[undo** **snmp mib event sample instance** **maximum**]命令用来恢复缺省情况。

【命令】

**[snmp mib event sample instance** **maximum** *value*]

**[undo snmp mib event sample instance** **maximum**]

【缺省情况】

最大采样实例数为0，表示没有上限。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：系统支持的最大采样实例数，取值为0或正整数。

【使用指导】

当前活动状态的采样实例数：如果此次多个监控对象属性均为通配，即每个监控对象对应有多个行实例，则当前活动状态的采样实例数为这些通配对象所有行实例的累加值。*value*值为0表示没有上限，无特殊资源限制时应为0。

·修改此节点不影响已经为活动状态的采样实例，比如修改最大采样行实例数小于活动状态采样实例数，原来处于活动状态的行实例数不会减少，但此时如果出现新的行实例则当前行实例数不会新增；

·最大采样实例数不变，当前采样实例数小于最大采样实例数，此时如果Trigger实例有新增，则当前采样实例数会更新，每采样一个实例，当前采样实例数就更新一次，并与配置的最大采样实例数比较，如果更新值刚好达到最大采样实例数，则之后新增的实例就不会再采样。

【举例】

\# 设置系统支持的最大采样行数为10。

\<Sysname\> system-view

Sysname snmp mib event sample instance maximum 10

【相关命令】

·**snmp mib event sample minimum**

**Event MIB \-- Event MIB配置命令 \-- snmp mib event sample minimum**

------------------------------------------------------------------------

**[snmp mib event sample minimum**]命令用来配置全局允许的最小采样时间间隔。

**[undo snmp mib event sample minimum**]命令用来恢复缺省情况。

【命令】

**[snmp mib event sample minimum ***value*]

**[undo snmp mib event sample minimum**]

【缺省情况】

全局允许的最小采样时间间隔为1秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：全局允许的最小采样时间间隔，单位为秒。

【使用指导】

为减少持续采样的系统开销，新配置的Trigger采样时间间隔必须大于等于该值，否则无法成功采样；

修改本节点不影响正在被采样的Trigger，即使正在被采样的Trigger的采样间隔小于新配置的最小采样间隔，也可以正常采样。

【举例】

\# 设置采样的全局最小间隔时间为50秒。

\<Sysname\> system-view

Sysname snmp mib event sample minimum 50

【相关命令】

·**snmp mib event trigger**

·**frequency**

**Event MIB \-- Event MIB配置命令 \-- snmp mib event trigger**

------------------------------------------------------------------------

**[snmp mib event trigger**]命令用来创建一个Trigger，并进入该Trigger视图。如果Trigger已经存在则直接进入视图。

**[undo snmp mib event trigger**]命令用来删除指定Trigger。

【命令】

**[snmp mib event trigger owner** *trigger-owner* **name** *trigger-name*]

**[undo snmp mib event trigger owner** *trigger-owner* **name** *trigger-name*]

【缺省情况】

不存在任何Tigger。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[trigger-owner*]：Trigger所有者，为1～32个字符的字符串，区分大小写。该Trigger所有者需指定为一个已存在的SNMPv3用户，用于判断对监控对象是否有操作权限。

*[trigger-name*]：Trigger名称，为1～32个字符的字符串，区分大小写。

【使用指导】

Trigger由所有者和名称唯一确定。进入指定的Trigger视图，可以指定监控的MIB对象，定时对指定的MIB对象进行采样。当获取监控对象所处的状态满足用户配置的事件触发条件时，就会触发相应的事件。

若Trigger所有者对该Trigger视图下配置的采样节点没有读权限，则采样失败。有关SNMPv3用户操作权限的详细介绍，请参见"网络管理与监控"中的"SNMP"。

【举例】

\# 配置Trigger所有者owner1，Trigger名称triggerA，并进入Trigger视图。

\<Sysname\> system-view

Sysname snmp mib event trigger owner owner1 name triggerA

Sysname-trigger-owner1-triggerA

**Event MIB \-- Event MIB配置命令 \-- snmp-agent trap enable event-mib**

------------------------------------------------------------------------

**[snmp-agent trap enable event-mib**]命令用来使能Event MIB的告警功能。

**[undo snmp-agent trap enable event-mib**]命令用来关闭告警功能。

【命令】

**[snmp-agent trap enable event-mib**]

**[undo snmp-agent trap enable event-mib**]

【缺省情况】

告警功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启Event MIB模块的告警功能后，当配置的监控对象采样失败或者满足触发Trigger的条件时会产生告警信息，该告警信息包括Trigger触发告警、Trigger触发上升阈告警、Trigger触发下降阈告警、Trigger触发条件检查失败告警、Trigger触发事件Set动作失败的告警。生成的告警信息将发送到设备的SNMP模块，通过设置SNMP中告警信息的发送参数，来决定告警信息输出的相关属性。

有关告警信息的详细介绍，请参见"网络管理与监控"中的"SNMP"。

【举例】

\# 使能Event MIB的告警功能。

\<Sysname\> system-view

Sysname snmp-agent trap enable event-mib

**Event MIB \-- Event MIB配置命令 \-- startup (Trigger-existence view)**

------------------------------------------------------------------------

**[startup**]命令用来配置首次采样允许触发事件的检测子类型。

**[undo startup**]命令用来关闭指定的检测子类型。

【命令】

**[startup **[{ **absent** \| **present** }]]

**[undo startup **[{ **absent** \| **present** }]]

【缺省情况】

首次采样允许触发事件的检测子类型为present和absent。

【视图】

Trigger-existence视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[absent**]：首次采样时，如果指定的监控对象不存在，且使用命令**type**配置采样检测类型Absent，则触发指定的事件。

**[present**]：首次采样时，如果指定的监控对象存在，且使用命令**type**配置采样检测类型为Present，则触发指定的事件。

【使用指导】

本命令作为**type**命令的扩展配置，用于首次采样时，若指定的监控对象满足**type**指定的检测类型，判断是否触发指定事件。

·当**type**和**startup**均配置为Present，如果监控对象为精确匹配，首次采样时监控对象存在则触发指定事件；如果监控对象为通配，首次采样时针对每个通配的对象单独触发指定事件。

·当**type**和**startup**均配置为Absent，如果监控对象为精确匹配，首次采样时监控对象不存在则触发指定事件；如果监控对象为通配，首次采样不会触发事件。

其他情况下，首次采样都不会触发事件。

【举例】

\# 关闭首次采样允许触发事件的Present检测子类型。

\<Sysname\> system-view

Sysname snmp mib event trigger owner owner1 name triggerA

Sysname-trigger-owner1-triggerA test existence

Sysname-trigger-owner1-triggerA-existence undo startup present

【相关命令】

·**type**

**Event MIB \-- Event MIB配置命令 \-- startup (Trigger-threshold view)**

------------------------------------------------------------------------

**[startup**]命令用来配置绝对值采样时首次采样允许触发的告警类型。

**[undo****startup**]命令用来恢复缺省情况。

【命令】

**[startup**[{ **falling** \| **rising** \| **rising-or-falling** }]]

**[undo****startup**]

【缺省情况】

绝对值采样时，首次采样允许触发的告警类型为**rising-or-falling**，即可以触发上限或下限告警。

【视图】

Trigger-threshold视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[falling**]：表示只触发下限告警。

**[rising**]：表示只触发上限告警。

**[rising-or-falling**]：表示可以触发上限或下限告警。

【使用指导】

采样类型为绝对值采样时：

·若首次采样允许触发的告警类型配置为**rising**或者**rising-or-falling**，当首次采样值大于等于配置的上限阈值时，触发上限告警；

·若首次采样允许触发的告警类型配置为**falling**或者**rising-or-falling**，当首次采样值小于等于配置的下限阈值时，触发下限告警。

·若前一次采样过程出错或监控对象不存在，那么此次对此监控对象的采样作为第一次采样来处理。

【举例】

\# 配置绝对值采样时首次采样允许触发的告警类型为触发上限告警。

\<Sysname\> system-view

Sysname snmp mib event trigger owner owner1 name triggerA

Sysname-trigger-owner1-triggerA test threshold

Sysname-trigger-owner1-triggerA-threshold startup rising

【相关命令】

·**snmp mib event trigger**

·**test **

·**sample**

**Event MIB \-- Event MIB配置命令 \-- startup enable**

------------------------------------------------------------------------

**[startup enable**]命令用来使能首次采样值满足检测条件时触发相应的事件功能。

**[undo startup enable**]命令用来关闭该功能。

【命令】

**[startup enable**]

**[undo startup enable**]

【缺省情况】

首次采样满足检测条件则触发指定事件功能处于使能状态。

【视图】

Trigger-boolean视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当监控节点为首次采样时，如果没有使能此功能，即使采样值满足检测条件，也不会触发相应的事件。

当监控节点首次采样值满足Boolean测试条件时，并且配置了**startup enable**命令才会触发相应的事件，否则将不会触发相应的事件。

若前一次采样过程出错或监控对象不存在，那么此次对该监控对象的采样作为第一次采样来处理。

【举例】

\# 配置首次采样满足检测条件时能够触发相应的事件。

\<Sysname\> system-view

Sysname snmp mib event trigger owner owner1 name triggerA

Sysname-trigger-owner1-triggerA test boolean

Sysname-trigger-owner1-triggerA-boolean startup enable

【相关命令】

·**comparison**

·**value**

**Event MIB \-- Event MIB配置命令 \-- test**

------------------------------------------------------------------------

**[test **[{ **boolean** \| **existence** \| **threshold** }]]命令用来配置Trigger触发条件的检测类型，并进入相应的Trigger-test视图。

**[undo test ****[ boolean **[\|]** existence **[\|]** threshold **} ]命令用于取消指定的检测类型。

【命令】]

**[test** **[ boolean **[\|]** existence**[ \|]** threshold **}****]

**[undo test ****[ boolean **[\|]** existence **[\|]** threshold **}****]

【缺省情况】]

没有配置]trigger触发条件的检测类型。

【视图】

Trigger视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[boolean**]：Trigger触发条件的检测类型为Boolean类型，主要用于对监控对象的值与参考值的大小比较等检查条件的设置。

**[existence**]：Trigger触发条件的检测类型为Existence类型，主要用于对监控对象存在、消失或者改变等状态的检查条件的设置。

**[threshold**]：Trigger触发条件的检测类型为Threshold类型，主要用于对监控对象的值是否超过上升阈值或者低于下降阈值等检查条件的设置。

【使用指导】

用户使用本命令可以配置Trigger运行的测试类型（Existence、Boolean、Threshold）。且每种类型都有相应的表（Existence表、Boolean表、Threshold表）与之对应，详细设置请参见对应的Trigger-boolean视图、Trigger-existence视图、Trigger-threshold视图下的命令。

【举例】

\# 配置Trigger触发条件的检测类型为Existence。

\<Sysname\>system-view

Sysname snmp mib event trigger owner owner1 name triggerA

Sysname-trigger-owner1-triggerA test existence

【相关命令】

·**snmp mib event trigger**

**Event MIB \-- Event MIB配置命令 \-- trigger enable**

------------------------------------------------------------------------

**[trigger enable**]命令用来使能Trigger的采样功能。

**[undo trigger enable**]命令用来关闭Trigger采样功能。

【命令】

**[trigger enable**]

**[undo trigger enable**]

【缺省情况】

Trigger采样功能处于关闭状态。

【视图】

trigger视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在使能Trigger采样功能前，需要先检查Trigger是否满足可以使能的条件：

·必须指定监控对象；

·采样时间间隔必须大于等于系统支持的最小采样时间间隔。

【举例】

\#当前最小采样时间间隔为100，使能Trigger的采样功能。

\<Sysname\>system-view

Sysname snmp mib event trigger owner owner1 name triggerA

Sysname-trigger-owner1-triggerA oid 1.3.6.1.2.1.2.2.1.1.3

Sysname-trigger-owner1-triggerA frequency 360

Sysname-trigger-owner1-triggerA trigger enable

【相关命令】

·**snmp mib event trigger**

**Event MIB \-- Event MIB配置命令 \-- type**

------------------------------------------------------------------------

**[type**]命令用来指定Trigger-existence视图下的检测类型。

**[undo type**]命令用于取消指定的检测类型。

【命令】

**[type **[{ **absent** \| **changed** \|**present** }]]

**[undo type **[{ **absent** \|**changed** \|**present** }]]

【缺省情况】

默认值为Present和Absent测试类型。

【视图】

Trigger-existence视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[absent**]：此次Trigger监控对象不存在，上一次Trigger监控对象存在，将触发指定的事件。首次采样时，若监控对象属性为精确匹配且监控对象不存在，必须同时满足设置命令**startup absent，**才会触发相应事件。

**[changed**]：当Trigger监控对象的值发生改变时，触发指定事件。如果上一次采样值获取不到则不触发。

**[present**]：此次Trigger监控对象存在，上一次Trigger监控对象不存在，将触发指定的事件。首次采样时，若监控对象存在，必须同时满足设置命令**startup present，**才会触发相应事件。

【使用指导】

对于第一次采样，参考**startup**命令使用指导。

如果不是第一次采样：

·当执行**type present**命令时，对于精确匹配，如果此次监控对象存在，前一次监控对象不存在，则触发指定事件；对于通配，获取当前监控对象的集合，将其中的每一个监控对象都与前一次通配到的所有监控对象比较，如果前一次无相同的监控对象，则触发指定事件。

·当执行**type absent**命令时，对于精确匹配，如果此次监控对象不存在，前一次监控对象存在，则触发指定事件；对于通配，获取当前监控对象的集合，将前一次的每一个监控对象都与此次通配到的所有监控对象比较，如果此次无相同的监控对象，则触发指定事件。

·当执行**type changed**命令时，对于精确匹配，如果此次与前一次都有相同的监控对象，那么比较之，若其值不同，则触发指定事件；对于通配，获取当前监控对象的集合，将其中的每一个监控对象都与前一次通配到的所有监控对象比较，如果两次都有相同的监控对象，那么比较之，若其值不同，则触发指定事件。

【举例】

\# 配置Trigger-existence子视图下检测类型为Present。

\<Sysname\> system-view

Sysname snmp mib event trigger owner owner1 name triggerA

Sysname-trigger-owner1-triggerA test existence

Sysname-trigger-owner1-triggerA-existence type present

【相关命令】

·**snmp mib event trigger**

·**test**

·**startup**

**Event MIB \-- Event MIB配置命令 \-- value (Trigger-boolean view)**

------------------------------------------------------------------------

**[value**]命令用来配置与采样值进行比较的参考值。

**[undo value**]命令用来恢复缺省情况。

【命令】

**[value***integer-value*]

**[undo value**]

【缺省情况】

与采样值进行比较的参考值为0。

【视图】

Trigger-boolean视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[integer-value*]：用于跟采样值进行比较的参考值，取值为任意整数。

【使用指导】

根据**comparison**命令配置的比较方式，将获取的采样值与**value**命令配置的参考值进行比较并确定是否满足检测条件。

【举例】

\# 配置与采样值进行比较使用的参考值为5。

\<Sysname\> system-view

Sysname snmp mib event trigger owner owner1 name triggerA

Sysname-trigger-owner1-triggerA test boolean

Sysname-trigger-owner1-triggerA-boolean value 5

【相关命令】

·**comparison**

**Event MIB \-- Event MIB配置命令 \-- value (Action-set view)**

------------------------------------------------------------------------

**[value**]命令用来配置Set操作对象的值。

**[undo value**]命令用来恢复缺省情况。

【命令】

**[value*** integer-value*]

**[undo value**]

【缺省情况】

Set操作对象的值为0。

【视图】

Action-set视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[integer-value*]：Set操作对象的值，取值为任意整数。

【举例】

\# 将Set操作对象1.3.6.1.2.1.2.2.1.7.3的值设置为2。

Sysname snmp mib event owner owner1 name EventA

Sysname-event-owner1-EventA action set

Sysname-event-owner1-EventA-set oid 1.3.6.1.2.1.2.2.1.7.3

Sysname-event-owner1-EventA-set value 2

【相关命令】

·**snmp mib event owner**

·**action**

·**oid**

**Event MIB \-- Event MIB配置命令 \-- wildcard context (Trigger view)**

------------------------------------------------------------------------

**[wildcard context**]命令用来配置监控对象所在的SNMP上下文的匹配方式为通配。

**[undo** **wildcard** **context**]命令用来恢复缺省情况。

【命令】

**[wildcard context**]

**[undo wildcard context**]

【缺省情况】

配置监控对象所在的SNMP上下文的匹配方式为精确匹配。

【视图】

Trigger视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本命令和**context**命令配合使用，共同决定监控对象所在的SNMP上下文：

·精确匹配表示配置为特定的SNMP上下文环境名；

·通配表示只指定上下文的前缀，即配置系统中存在的相同前缀的所有上下文环境名。

【举例】

\# 配置监控对象所在的SNMP上下文环境名为contextname的匹配方式为通配。

\<Sysname\> system-view

Sysname snmp mib event trigger owner owner1 name triggerA

Sysname-trigger-owner1-triggerA context contextname

Sysname-trigger-owner1-triggerA wildcard context

【相关命令】

·**snmp mib event trigger**

·**context**

**Event MIB \-- Event MIB配置命令 \-- wildcard context (Action-set view)**

------------------------------------------------------------------------

**[wildcard context**]命令用来配置Set对象所在的SNMP上下文的匹配方式为通配。

**[undo wildcard context**]用来恢复缺省情况。

【命令】

**[wildcard context**]

**[undo wildcard context**]

【缺省情况】

Set对象所处的SNMP上下文的匹配方式为精确匹配。

【视图】

Action-set视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本命令和**context**命令配合使用，共同决定Set对象所在的SNMP上下文。精确匹配表示配置为特定的SNMP上下文环境名，而通配有两部分组成，一部分为mteEventSetContextName指定的contextname，另一部分为由Trigger表中contextName的通配部分。

【举例】

\# 配置Set对象所处的SNMP上下文环境名为contextname1的匹配方式为通配。

\<Sysname\>system-view

Sysname snmp mib event owner owner1 name EventA

Sysname-event-owner1-EventA action set

Sysname-event-owner1-EventA-set context contextname1

Sysname-event-owner1-EventA-set wildcard context

【相关命令】

·**snmp mib event owner**

·**action set**

·**context**

**Event MIB \-- Event MIB配置命令 \-- wildcard oid (Trigger view)**

------------------------------------------------------------------------

**[wildcard oid**]命令用来配置Trigger采样的MIB节点的匹配方式为通配。

**[undo wildcard oid**]命令用来恢复缺省情况。

【命令】

**[wildcard oid **]

**[undo wildcard oid**]

【缺省情况】

Trigger采样的MIB节点匹配方式为精确匹配。

【视图】

Trigger视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本命令与**oid**命令配合使用，共同决定监控的对象：

·当匹配类型为精确匹配时，表示**oid**命令指定的监控对象为一个具体的实例，比如需要监控接口索引为2的接口描述节点，则配置**oid** ifDescr.2，匹配类型配置为精确匹配。

·当匹配类型为通配时，表示**oid**命令只指定了监控对象的OID前缀，系统中存在的所有MIB对象只要前缀与此相同均作为监控对象，比如需要监控所有接口对应的接口描述节点，则配置**oid** ifDescr，并将匹配类型配置为通配。

【举例】

\# 配置triggerr采样的节点值为1.3.6.1.2.1.1.6，采样节点匹配方式为通配。

\<Sysname\>system-view

Sysname snmp mib event trigger owner owner1 name triggerA

Sysname-trigger-owner1-triggerA oid 1.3.6.1.2.1.1.6

Sysname-trigger-owner1-triggerA wildcard oid

【相关命令】

·**snmp mib event trigger**

·oid

**Event MIB \-- Event MIB配置命令 \-- wildcard oid (Action-se view)**

------------------------------------------------------------------------

**[wildcard oid**]命令用来配置Set操作对象的匹配方式为通配。

**[undo wildcard oid**]命令用来恢复缺省情况。

【命令】

**[wildcard oid**]

**[undo wildcard oid**]

【缺省情况】

Set操作对象的匹配方式为精确匹配。

【视图】

Action-set视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·Set对象的OID属性为通配，表示Set对象的OID由两部分组成：一部分为mteEventSetObject指定的OID，另一部分为由Trigger表中监控对象OID的通配部分；

·Set对象的OID属性为精确匹配：表示oid命令指定的MIB节点OID即为Set对象的OID。

【举例】

\# 配置用户名name1，事件名为EventA的Set对象OID为1.3.6.1.2.1.2.2.1.7的匹配方式为通配。

\<Sysname\> system-view

Sysname snmp mib event owner owner1 name EventA

Sysname-event-owner1-EventA action set

Sysname-event-owner1-EventA-set oid 1.3.6.1.2.1.2.2.1.7

Sysname-event-owner1-EventA-set wildcard oid

【相关命令】

·**snmp mib event owner**

·**action set**

·**oid**
