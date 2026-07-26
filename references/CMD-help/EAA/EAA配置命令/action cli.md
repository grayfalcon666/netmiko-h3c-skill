
**EAA \-- EAA配置命令 \-- action cli**

------------------------------------------------------------------------

**[action cli**]命令用来配置事件发生时执行指定的命令行。

**[undo action**]命令用来取消指定的操作。

【命令】

**[action ***number ***cli ***command-line*]

**[undo action ***number*]

【缺省情况】

监控策略下未配置任何CLI动作。

【视图】

CLI监控策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：动作序号，取值范围为0～231。

**[cli ***command-line*]：需要执行的命令。该参数可以是命令的不完整形式，比如为命令**display current-configuration**的缩写形式**dis cu**，但需要用户保证其为设备可识别的合法命令，否则，该动作不能成功执行。

【使用指导】

如果配置事件发生时执行指定的命令行为非用户视图下的，则必须先配置进入相应视图的**action cli**，且进视图的**action**的编号应小于执行指定命令的**action**的编号。比如，要使用CLI策略来关闭接口GigabitEthernet1/0/1，则需要配置三条**action**命令，**action** 1 **cli** system-view、**action** 2 **cli** interface gigabitethernet 1/0/1、**action** 3 **cli** shutdown。

同一个监控策略下可以配置多个动作，当监控策略被触发后，系统会按照动作序号从小到大依次执行这些动作。如果用户配置了相同序号的动作，当管理员执行**commit**命令时，新配置的**action**生效。

【举例】

\# 为CLI监控策略test配置动作：当test被触发时，关闭接口GigabitEthernet1/0/1。

\<Sysname\> system-view

Sysname rtm cli-policy test

Sysname-rtm-test action 1 cli system-view

Sysname-rtm-test action 2 cli interface gigabitethernet 1/0/1

Sysname-rtm-test action 3 cli shutdown

**EAA \-- EAA配置命令 \-- action reboot**

------------------------------------------------------------------------

**[action reboot**]命令用来配置事件发生时执行重启操作。

**[undo action**]命令用来取消指定的操作。

【命令】

集中式设备：

**[action ***number*****]**reboot ** **subslot** *subslot-number*

**[undo action ***number*]

分布式设备－独立运行模式/集中式IRF设备：

**[action ***number*****]**reboot ** **slot** *slot-number*  **subslot** *subslot-number*

**[undo action ***number*]

分布式设备－IRF模式：

**[action ***number*****]**reboot ** **chassis** *chassis-number*  **slot** *slot-number* [ **subslot** *subslot-number*  ]

**[undo action ***number*]

【缺省情况】

监控策略下未配置任何重启动作。

【视图】

CLI监控策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：动作序号，取值范围为0～231。

**[chassis **]*chassis-number*：表示设备在IRF中的成员编号。不指定该参数时，表示所有成员设备。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **]*chassis-number*：表示设备在IRF中的成员编号或者PEX对应的虚拟框号。不指定该参数时，表示所有成员设备/虚拟框。（分布式设备－IRF模式）（支持IRF3的设备）

**[slot**] *slot-number*：表示单板所在的槽位号。不指定该参数时，表示所有单板。（分布式设备－独立运行模式）

**[slot**] *slot-number*：表示单板所在的槽位号。不指定该参数时，表示所有单板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[slot**] *slot-number*：表示单板/PEX所在的槽位号。不指定该参数时，表示所有单板/PEX。（分布式设备－IRF模式）（支持IRF3的设备）

**[slot**]* slot-number*：表示设备在IRF中的成员编号。不指定该参数时，表示所有成员设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，表示所有成员设备/PEX。（集中式IRF设备）（不支持IRF3的设备）

**[subslot**] *subslot-number*：子卡所在的子槽位号。不指定该参数时，表示所有子卡。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

使用**action reboot**命令，或者使用**action cli**命令并将*command-line*参数指定为**reboot**命令，均可实现在事件发生时执行重启操作。只是**action reboot**命令会直接执行重启操作，使用**action cli**命令时，用户可以选择是否先保存当前配置，再执行重启操作。

同一个监控策略下可以配置多个动作，当监控策略被触发后，系统会按照动作序号从小到大依次执行这些动作。如果用户配置了相同序号的动作，当管理员执行**commit**命令时，新配置的**action**生效。

【举例】

\# 为CLI监控策略test配置动作：当test被触发时，重启整个设备。（集中式设备[/分布式设备－独立运行模式）]

\<Sysname\> system-view

Sysname rtm cli-policy test

Sysname-rtm-test action 3 reboot

\# 为CLI监控策略test配置动作：当test被触发时，重启成员设备1。（集中式IRF设备）

\<Sysname\> system-view

Sysname rtm cli-policy test

Sysname-rtm-test action 3 reboot slot 1

\# 为CLI监控策略test配置动作：当test被触发时，重启成员设备1。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname rtm cli-policy test

Sysname-rtm-test action 3 reboot chassis 1

**EAA \-- EAA配置命令 \-- action switchover**

------------------------------------------------------------------------

**[action switchover**]命令用来配置事件发生时启动主备倒换。

**[undo action**]命令用来取消指定的操作。

【命令】

**[action ***number*** switchover**]

**[undo action ***number*]

【缺省情况】

监控策略下未配置主备倒换动作。

【视图】

CLI监控策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：动作序号，取值范围为0～231。

【使用指导】

同一个监控策略下可以配置多个动作，当监控策略被触发后，系统会按照动作序号从小到大依次执行这些动作。如果用户配置了相同序号的动作，当管理员执行**commit**命令时，新配置的**action**生效。

即便当前设备不是主备环境（未部署备用主控板或者备用主控板未正常启动），该命令也会执行成功，但不会触发主备倒换动作。

【举例】

\# 为CLI监控策略test配置动作：当test被触发时，执行主备倒换。

\<Sysname\> system-view

Sysname rtm cli-policy test

Sysname-rtm-test action 3 switchover

**EAA \-- EAA配置命令 \-- action syslog**

------------------------------------------------------------------------

**[action syslog**]命令用来配置事件发生时生成一条指定内容的日志。

**[undo action**]命令用来取消指定的操作。

【命令】

**[action ***number ***syslog priority ***level*** facility ***local-number*** msg ***msg-body*]

**[undo action ***number*]

【缺省情况】

监控策略下未配置任何日志动作。

【视图】

CLI监控策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：动作序号，取值范围为0～231。

**[priority ***level*]：生成的日志的优先级，取值范围为0～7。优先级的值越小，优先级越高。

**[facility ***local-number*]：生成日志的设备号，取值范围为local0～local7。主要用于在日志主机端标志不同的日志来源，查找、过滤对应日志源的日志。

**[msg ***msg-body*]：生成的日志的内容。

【使用指导】

事件触发后生成的日志信息会交给信息中心模块处理，信息中心模块的配置将决定日志信息的发送规则和发送方向。关于信息中心的详细描述请参见"网络管理和监控配置指导"中的"信息中心"。

同一个监控策略下可以配置多个动作，当监控策略被触发后，系统会按照动作序号从小到大依次执行这些动作。如果用户配置了相同序号的动作，当管理员执行**commit**命令时，新配置的**action**生效。

【举例】

\# 为CLI监控策略test配置动作：当test被触发时，生成一条优先级为7、设备号为local3、内容为hello的日志。

\<Sysname\> system-view

Sysname rtm cli-policy test

Sysname-rtm-test action 3 syslog priority 7 facility local3 msg hello

**EAA \-- EAA配置命令 \-- commit**

------------------------------------------------------------------------

**[commit**]命令用来启用CLI监控策略。

【命令】

**[commit**]

【缺省情况】

CLI监控策略未被启用。

【视图】

CLI监控策略视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

CLI策略策略创建并配置事件和动作后，并不会立即生效，需要执行**commit**命令才会生效。

【举例】

\# 启用CLI监控策略test。

\<Sysname\> system-view

Sysname rtm cli-policy test

Sysname-rtm-test commit

**EAA \-- EAA配置命令 \-- display rtm environment**

------------------------------------------------------------------------

**[display rtm environment**]命令用来显示用户自定义的EAA环境变量配置。

【命令】

**[display rtm environment** [ *var-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[var-name*]：显示指定名称的环境变量的配置。不指定该参数时，显示所有环境变量的配置。

【举例】

\# 显示用户自定义的所有EAA环境变量配置。

\<Sysname\> display rtm environment

Name             Value

config_cmd       interface m1/0/1

save_cmd         save main force

show_run_cmd     display current-configuration

表1-1 display rtm environment命令信息描述

主要字段

描述

Name

环境变量的名称

Value

环境变量的值

**EAA \-- EAA配置命令 \-- display rtm policy**

------------------------------------------------------------------------

**[display rtm policy**]命令用来显示监控策略的相关信息。

【命令】

**[display rtm policy**[{ **active** \| **registered** [ **verbose** ] }  *policy-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[active**]：显示正在执行的监控策略的相关信息。

**[registered**]：显示已创建的监控策略的相关信息。

*[policy-name*]：显示指定监控策略的相关信息。*policy-name*表示监控策略的名称，不指定该参数时，显示所有正在执行的或者是已创建的监控策略的相关信息。

**[verbose**]：显示监控策略的详细信息。

【举例】

\# 显示所有正在运行的监控策略。

\<Sysname\> display rtm policy active

JID   Type  Event      TimeActive           PolicyName

507   TCL   INTERFACE  Aug 29 14:55:55 2013 test

\# 显示所有监控策略的相关信息。

\<Sysname\> display rtm policy registered

Total number: 1

Type  Event      TimeRegistered       PolicyName

CLI              Aug 29 14:54:50 2013 test

\# 显示所有监控策略的详细信息。

\<Sysname\> display  rtm policy registered verbose

  Total number: 1

   Policy Name: test

   Policy Type: CLI

    Event Type:

TimeRegistered: Aug 29 14:54:50 2013

     User-role: network-operator

                network-admin

表1-2 display rtm policy命令显示信息描述表

主要字段

描述

JID

任务ID，执行**display  rtm policy active**命令时才显示该信息

PolicyName

监控策略的名称

Type

监控策略的类型，其中：

·TCL表示这个策略是通过TCL脚本定义的

·CLI表示这个策略是通过命令行定义的

Policy Type

Event

监控策略触发事件的类型，包括CLI、HOTPLUG、INTERFACE、PROCESS、SNMP、SNMP_NOTIF、SYSLOG七种，具体配置及含义参考相应**event**命令

Event Type

TimeActive

监控策略开始运行的时间

PolicyName

监控策略的名称

TimeRegistered

监控策略的创建时间

Total number

监控策略的总数

User-role

执行监控策略需要的最小用户角色

**EAA \-- EAA配置命令 \-- event cli**

------------------------------------------------------------------------

**[event cli**]命令用来配置命令行事件。

**[undo event**]命令用来取消当前的事件配置。

【命令】

**[event cli ****[skip **  \| **sync** } **mode** { **execute** \| **help** \| **tab** } **pattern** *regular-exp*]]

**[undo event**]

【缺省情况】

未配置任何命令行事件。

【视图】

CLI监控策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[async** \**[skip** ]]：异步监控。如果指定**skip**参数，则表示事件发生时，只执行CLI监控策略中的动作，不执行**event cli**中指定的命令；如果不指定**skip**参数，则表示事件发生时，CLI监控策略和**event cli**中指定的命令同时执行。

**[sync**]：同步监控。只有CLI监控策略执行成功，**event cli**中指定的命令才能执行。

**[execute**]：监控命令行的执行。当用户执行特定命令时，触发CLI监控策略。

**[help**]：监控命令行的"?"帮助。当用户执行特定帮助命令时，触发CLI监控策略。

**[tab**]：监控命令行的Tab补全。当用户执行特定命令并使用Tab键自动补全功能时，触发CLI监控策略。

**[pattern*** regular-exp*]：用于匹配命令行的正则表达式。只要输入的命令行中包含该字符串，则匹配成功，触发策略执行。关于正则表达式的详细描述请参见"基础配置指导"中的"CLI"。

【使用指导】

配置该事件后，当用户输入指定的命令并执行相应动作（执行、帮助或者补全）就会触发策略执行。用户输入命令是否执行、帮助或者补全，以及是否等待CLI监控策略执行成功后再执行、帮助或者补全，由**sync**、**async** \**[skip** ]参数决定。

同一监控策略下，只能配置一个事件。如果多次执行**event**命令配置了不同事件，则最新配置并**commit**的生效。

【举例】

\# 为CLI监控策略test配置异步CLI事件，当用户输入命令中含有dis inter brief字符并执行该命令时触发策略执行，同时跳过命令行执行。

\<Sysname\>system-view

Sysname rtm cli-policy test

Sysname-rmt-test event cli async skip mode execute pattern dis inter brief

\# 为CLI监控策略test配置异步CLI事件，当用户输入的命令中含有dis inter brief字符并使用了\<Tab\>键补全功能时，触发策略执行，同时将\<Tab\>键补全的结果返回给用户。

\<Sysname\> system-view

Sysname rtm cli-policy test

Sysname-rmt-test event cli async mode tab pattern dis inter brief

\# 为CLI监控策略test配置同步CLI事件，当用户输入的命令中含有dis inter brief字符并使用了帮助功能时，触发策略执行。系统等策略执行成功后，返回帮助的结果。

\<Sysname\>system-view

Sysname rtm cli-policy test

Sysname-rmt-test event cli sync mode help pattern dis inter brief

**EAA \-- EAA配置命令 \-- event hotplug**

------------------------------------------------------------------------

**[event hotplug**]命令用来配置板卡热插拔事件。

**[undo event**]命令用来取消当前的事件配置。

【命令】

集中式设备/分布式设备－独立运行模式/集中式IRF设备：

**[event hotplug**]****\**[insert**[ \| ]**remove**  ]**slot** *slot-number* [ **subslot** *subslot-number* ]

**[undo event**]

分布式设备－IRF模式：

**[event hotplug**]****\**[insert**[ \| ]**remove**  ]**chassis** *chassis-number* **slot** *slot-number* [ **subslot** *subslot-number* ]

**[undo event**]

【缺省情况】

未配置任何热插拔事件。

【视图】

CLI监控策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[insert**]：表示监控单板的插入事件。不指定**insert**和**remove**参数时，表示监控单板的插入和拔出事件。

**[remove**]：表示监控单板的拔出事件。不指定**insert**和**remove**参数时，表示监控单板的插入和拔出事件。

**[slot**]* slot-number*：取值为0，无实际意义。（集中式设备）

**[slot**] *slot-number*：表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis**] *chassis-number* **slot** *slot-number*：表示IRF中的指定单板。其中，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**] *chassis-number* **slot** *slot-number*：表示IRF中的指定单板/PEX。其中，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[subslot**] *subslot-number*：子卡所在的子槽位号。不指定该参数时，表示单板上的任一子卡。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

配置该事件后，当用户插入/拔出指定板卡，会触发监控策略执行。

同一监控策略下，只能配置一个事件。如果多次执行**event**命令配置了不同事件，则最新配置并**commit**的生效。

【举例】

\# 为CLI监控策略test配置监控事件：热插拔2号子卡均触发策略执行。（集中式设备）

\<Sysname\> system-view

Sysname rtm cli-policy test

Sysname-rtm-test event hotplug slot 0 subslot 2

\# 为CLI监控策略test配置监控事件：热插拔2号槽位的板卡时触发策略执行。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname rtm cli-policy test

Sysname-rtm-test event hotplug slot 2

\# 为CLI监控策略test配置监控事件：热插拔成员设备2上的子卡时均触发策略执行。（集中式IRF设备）

\<Sysname\> system-view

Sysname rtm cli-policy test

Sysname-rtm-test event hotplug slot 2

\# 为CLI监控策略test配置监控事件：热插拔成员设备1上2号槽位的板卡时触发策略执行。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname rtm cli-policy test

Sysname-rtm-test event hotplug chassis 1 slot 2

**EAA \-- EAA配置命令 \-- event interface**

------------------------------------------------------------------------

**[event interface**]命令用来配置接口事件。

**[undo event**]命令用来取消当前的事件配置。

【命令】

**[event interface***interface-type interface-number* **monitor-obj** *monitor-obj* **start-op** *start-op* **start-val** *start-val* **restart-op** *restart-op* **restart-val** *restart-val* [ **interval** *interval* ]]

**[undo event**]

【缺省情况】

未配置任何接口事件。

【视图】

CLI监控策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type interface-number*]：表示要监控的接口类型和编号。

**[monitor-obj*** monitor-obj*]：表示要监控的对象，具体描述请见[表]1-3(?823272471#_Ref323135376)。

**[start-op ***start-op*]：触发监控策略执行的操作码，取值如[表]1-4(?823272471#_Ref323135406)所示。

**[start-val ***start-val*]：触发监控策略执行的监控对象的值，取值范围为0～4294967295，单位请见[表]1-3(?823272471#_Ref323135376)。

**[restart-op ***restart-op*]：重新开启触发开关的操作码，具体描述请见[表]1-4(?823272471#_Ref323135406)。

**[restart-val ***restart-val*]：重新开启触发开关的监控对象的值，取值范围为0～4294967295，单位请见[表]1-3(?823272471#_Ref323135376)。

**[interval*** interval*]：获取监控对象数据的时间间隔，取值范围为1～4294967295，单位为秒，缺省值为300秒。

表1-3 监控对象说明

监控对象

含义

input-drops

接口接收方向丢弃包的个数

input-errors

接口接收到的错误包的个数

output-drops

接口发送方向丢弃包的个数

output-errors

接口发送出去的错误包的个数

rcv-bps

接口接收速率，单位为比特/秒

rcv-broadcasts

接口接收到的广播包个数

rcv-pps

接口接收速率，单位为包/秒

tx-bps

接口传输速率，单位为比特/秒

tx-pps

接口传输速率，单位为包/秒

表1-4 比较操作符说明

比较操作符

含义

eq

等于

ge

大于等于

gt

大于

le

小于等于

lt

小于

ne

不等于

【使用指导】

接口事件中存在一个触发开关：

(1)配置该事件后，触发开关立即打开。

(2)当指定接口上的指定报文的数目达到**start-op** *start-op* **start-val** *start-val*参数指定的条件时，触发监控策略执行一次（第一次执行），并关闭触发开关，但系统会继续监控接口事件。

(3)当满足**restart-op ***restart-op*** restart-val ***restart-val*参数指定的条件时，才重新开启触发开关。

(4)如果指定接口上的指定报文的数目再次达到**start-op** *start-op* **start-val** *start-val*参数指定的条件时，则再次触发监控策略执行一次（第二次执行），并关闭触发开关，系统继续监控接口事件。

(5)如此循环。

同一监控策略下，只能配置一个事件。如果多次执行**event**命令配置了不同事件，则最新配置并**commit**的生效。

【举例】

\# 为CLI监控策略test配置监控事件：每60秒获取一次GigabitEthernet1/0/1接收到的错误包的个数。当错误包的个数大于1000时触发test执行并关闭触发开关，当错误包的个数小于50时重新开启触发开关，如此循环。

\<Sysname\> system-view

Sysname rtm cli-policy test

Sysname-rtm-test event interface gigabitethernet 1/0/1 monitor-obj input-errors start-op gt start-val 1000 restart-op lt restart-val 50 interval 60

**EAA \-- EAA配置命令 \-- event process**

------------------------------------------------------------------------

**[event process**]命令用来配置进程事件。

**[undo event**]命令用来取消当前的事件配置。

【命令】

集中式设备/分布式设备－独立运行模式/集中式IRF设备：

**[event process **[{ **exception** \| **restart** \| **shutdown** \| **start** } [ **name** *process-name* [ **instance** *instance-id* ] ]  **slot** *slot-number* ]]

**[undo event**]

分布式设备－IRF模式：

**[event process **[{ **exception** \| **restart** \| **shutdown** \| **start** } [ **name** *process-name* [ **instance** *instance-id* ] ]  **chassis** *chassis-number* [ **slot** *slot-number*  ]]]

**[undo event**]

【缺省情况】

未配置任何进程事件。

【视图】

CLI监控策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[exception**]**：**监控进程异常事件。当进程发生异常时，触发CLI监控策略。

**[restart**]：监控进程重启事件。当进程重启时，触发CLI监控策略。

**[shutdown**]：监控进程关闭事件。当进程关闭时，触发CLI监控策略。

**[start**]：监控进程启动事件。当进程启动时，触发CLI监控策略。

**[name*** process-name*]：监控的用户态进程的名称，可以是当前正在运行的进程也可以是没有运行的进程。

**[instance*** instance-id*]**：**监控的用户态进程的实例的编号。不指定该参数时，表示进程下的任意实例异常、重启、关闭、启动都会触发事件，取值范围为0～4294967295。可以是当前不存在的实例号。

**[chassis **]*chassis-number*：表示设备在IRF中的成员编号。不指定该参数时，表示所有成员设备。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **]*chassis-number*：表示设备在IRF中的成员编号或者PEX对应的虚拟框号。不指定该参数时，表示所有成员设备[/虚拟框。（分布式设备－]IRF模式）（支持IRF3的设备）

**[slot**] *slot-number*：表示单板所在的槽位号。不指定该参数时，表示所有单板。（分布式设备－独立运行模式）

**[slot**] *slot-number*：表示单板所在的槽位号。不指定该参数时，表示所有单板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[slot**] *slot-number*：表示单板/PEX所在的槽位号。不指定该参数时，表示所有单板/PEX。（分布式设备－IRF模式）（支持IRF3的设备）

**[slot**]* slot-number*：表示设备在IRF中的成员编号。不指定该参数时，表示所有成员设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，表示所有成员设备[/]PEX。（集中式IRF设备）（支持IRF3的设备）

【使用指导】

配置该事件后，当指定进程异常、关闭、启动或重启时（可以为用户命令行触发的或者系统自动触发的），均触发监控策略执行。

同一监控策略下，只能配置一个事件。如果多次执行**event**命令配置了不同事件，则最新配置并**commit**的生效。

【举例】

\# 为CLI监控策略test配置监控事件：当进程snmpd重启时触发策略执行。

\<Sysname\>system-view

Sysname rtm cli-policy test

Sysname-rtm-test event process restart name snmpd

**EAA \-- EAA配置命令 \-- event snmp oid**

------------------------------------------------------------------------

**[event snmp oid**]命令用来配置SNMP操作事件。

**[undo event**]命令用来取消当前的事件配置。

【命令】

**[event snmp**[ **oid** *oid* **monitor-obj** [\| **next** } **start-op** *start-op* **start-val** *start-val* **restart-op** *restart-op* **restart-val** *restart-val* [ **interval** *interval* ]]]

**[undo event**]

【缺省情况】]

未配置任何SNMP操作事件。

【视图】

CLI监控策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[oid*** oid*]：表示需要监控的MIB对象的OID，为1～256个字符的字符串。

**[monitor-obj**[ { **get \| next** }]]：表示需要监控的SNMP操作。**get**表示SNMP Get操作；**next**表示SNMP Get Next操作。

**[start-op ***start-op*]：触发监控策略执行的操作码，取值如[表]1-4(?823272471#_Ref323135406)所示。

*[start-val*]：触发监控策略执行的值。可以是SNMP模块支持的所有类型，例如，数字、字符串等。因为支持多类型，帮助时统一提示为1～512个字符的字符串。如果该值中包含空格，需要在值的首末添加英文格式的引号，形如"xxx xxx"。

**[restart-op ***op*]：重新开启触发开关的操作码，取值如[表]1-4(?823272471#_Ref323135406)所示。

*[restart-val*]：重新开启触发开关的监控对象的值。可以是SNMP模块支持的所有类型，例如，数字、字符串等。因为支持多类型，帮助时统一提示为1～512个字符的字符串。如果该值中包含空格，需要在值的首末添加英文格式的引号，形如"xxx xxx"。

**[interval ***interval*]：获取监控对象数据的时间间隔，取值范围为1～4294967295，单位为秒，缺省值为300秒。

【使用指导】

SNMP操作事件中存在一个触发开关：

(1)配置该事件后，触发开关立即打开。

(2)此后系统按照用户设定的**interval ***interval*值定时获取设备上某个OID对应节点的值，且该值达到**start-op** *start-op* **start-val** *start-val*参数指定的条件时，触发监控策略执行一次（第一次执行），并关闭触发开关，但系统会继续监控SNMP操作事件。

(3)当满足**restart-op ***restart-op*** restart-val ***restart-val*参数指定的条件时，才重新开启触发开关。

(4)如果用户获取的MIB对象的值再次达到**start-op** *start-op* **start-val** *start-val*参数指定的条件时，则再次触发监控策略执行一次（第二次执行），并关闭触发开关，系统继续监控SNMP操作事件。

(5)如此循环。

同一监控策略下，只能配置一个事件。如果多次执行**event**命令配置了不同事件，则最新配置并**commit**的生效。

【举例】

\# 为CLI监控策略test配置监控事件：系统每5秒检查MIB对象1.3.6.4.9.9.42.1.2.1.6.4的值，当该值等于1时触发执行监控策略并关闭监控开关，当等于2时重新启动监控。

\<Sysname\> system-view

Sysname rtm cli-policy snmp

Sysname-rtm-snmp event snmp oid 1.3.6.4.9.9.42.1.2.1.6.4 monitor-obj get start-op eq start-val 1 restart-op eq restart-val 2 interval 5

**EAA \-- EAA配置命令 \-- event snmp-notification**

------------------------------------------------------------------------

**[event snmp-notification**]命令用来配置SNMP Trap事件。

**[undo event**]命令用来取消当前的事件配置。

【命令】

**[event snmp-notification oid** *oid* **oid-val** *oid-val* **op** *op* [ **drop** ]]

**[undo event**]

【缺省情况】

未配置任何SNMP Trap触发事件。

【视图】

CLI监控策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[oid*** oid*]：Trap信息中携带的MIB对象的OID，为1～256个字符的字符串。

**[oid-val*** oid-val*]：Trap信息中携带的MIB对象的值。可以是SNMP模块支持的所有类型，例如，数字、字符串等。因为支持多类型，帮助时统一提示为1～512个字符的字符串。如果该值中包含空格，需要在值的首末添加英文格式的引号，形如"xxx xxx"。

**[op ***op*]：比较操作码，取值如[表]1-4(?823272471#_Ref323135406)所示。

**[drop**]：表示匹配成功后丢弃该Trap信息。不指定该参数时，表示正常发送。

【使用指导】

配置该事件后，当系统生成一条Trap，且Trap中携带的MIB对象（由*oid*参数指定）的值到达**oid-val*** oid-val ***op*** op*指定的条件时，触发监控策略执行。

同一监控策略下，只能配置一个事件。如果多次执行**event**命令配置了不同事件，则最新配置并**commit**的生效。

【举例】

\# 为CLI监控策略test配置SNMP Trap监控事件：当发生Trap的OID为1.3.6.1.4.1.318.2.8.3，并且其值为UPS:Returned from battery backup power时，触发策略，同时丢弃这个Trap。

\<Sysname\> system-view

Sysname rtm cli-policy snmp-notification

Sysname-rtm-snmp-notification event snmp-notification oid 1.3.6.1.4.1.318.2.8.3 oid-val "UPS:Returned from battery backup power" op eq drop

**EAA \-- EAA配置命令 \-- event syslog**

------------------------------------------------------------------------

**[event syslog**]命令用来配置日志事件。

**[undo event**]命令用来取消当前的事件配置。

【命令】

**[event syslog priority ***level*** msg*** msg ***occurs ***times*** period ***period*]

**[undo event**]

【缺省情况】

未配置任何日志事件。

【视图】

CLI监控策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[priority*** level*]：表示需要匹配的日志的最低优先级，取值范围为0～7或者all。对于数字表示的优先级，值越小，优先级越高。当*level*配置为3时，表示能匹配优先级为0～3的日志；all表示和任意优先级匹配。

**[msg*** msg*]：正则表达式，表示需要匹配的日志的部分或全部，为1～255个字符的字符串。该日志必须为H3C格式的日志，关于日志的详细介绍请参见"网络管理和监控配置指导"中的"信息中心"。

**[occurs ***times*** period ***period*]：表示指定日志在*period*秒内发生了*times*次时触发监控策略执行。*times*的取值范围为1～32，*period*的取值范围为1～4294967295，单位为秒。

【使用指导】

配置该事件后，当系统在指定时间段内生成指定规格的日志信息时触发监控策略执行。为了防止循环触发，RTM模块产生的日志不会触发策略。

同一监控策略下，只能配置一个事件。如果多次执行**event**命令配置了不同事件，则最新配置并**commit**的生效。

【举例】

\# 为CLI监控策略test配置监控事件：当优先级高于或等于3、内容中含有down的日志在6秒内出现过5次时触发执行策略。

\<Sysname\> system-view

Sysname rtm cli-policy syslog

Sysname-rtm-syslog event syslog priority 3 msg down occurs 5 period 6

**EAA \-- EAA配置命令 \-- rtm cli-policy**

------------------------------------------------------------------------

**[rtm cli-policy**]命令用来创建CLI监控策略并进入CLI监控策略视图。

**[undo rtm cli-policy**]命令来删除指定的CLI监控策略。

【命令】

**[rtm cli-policy ***policy-name*]

**[undo rtm cli-policy*** policy-name*]

【缺省情况】

未创建CLI监控策略。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：CLI监控策略的名称。为1～63个字符的字符串，区分大小写。

【使用指导】

使用该命令用来创建CLI监控策略并进入CLI监控策略视图。在该视图下，用户可以通过命令行给CLI监控策略配置触发事件以及需要执行的动作。其中，触发事件只能定义一个，动作可以定义多个。当条件满足、事件被触发时，系统会按照动作序号由小到大顺序执行这些动作。监控动作在后台执行，用户可以通过查看日志信息了解策略的执行结果。

CLI监控策略配置完成后（即配置完触发事件以及需要执行的动作后），必须执行**commit**命令才能启用CLI监控策略，使配置的事件和动作生效。

多次执行该命令可以创建多个CLI监控策略且数量没有限制。请尽量确保同时启用的策略间动作不要冲突，因为当系统同时执行多个策略，且不同策略间动作有冲突时，执行结果是随机的。

如果同为TCL监控策略或者同为CLI监控策略，则策略名不能相同。如果策略类型不同，则名称可以相同。

【举例】

\# 创建CLI监控策略test并进入CLI监控策略视图。

\<Sysname\> system-view

Sysname rtm cli-policy test

【相关命令】

·**commit**

**EAA \-- EAA配置命令 \-- rtm environment**

------------------------------------------------------------------------

**[rtm environment**]命令用来创建监控策略的环境变量。

**[undo rtm environment**]命令来删除指定的环境变量。

【命令】

**[rtm environment ***var-name******var-value*]

**[undo rtm environment ***var-name*]

【缺省情况】

无用户自定义的环境变量，系统中支持一系列内部环境变量，不同事件支持的内部环境变量及其意义有所不同，请参见 表1-5(?417053394#_Ref321835254)。

表1-5 内部环境变量描述表

事件

内部环境变量的名称

描述

CLI

\_cmd

匹配上的命令

SYSLOG

\_syslog_pattern

匹配的日志信息的内容

HOTPLUG

\_slot

发生热插拔的单板所在的槽位号

\_subslot

发生热插拔的子卡所在的子槽位号

INTERFACE

\_ifname

接口的名称

SNMP

\_oid

SNMP操作中携带的OID

\_oid_value

OID对应节点的值

SNMP TRAP

\_oid

SNMP Trap信息中携带的OID

PROCESS

\_process_name

进程的名称

公共环境变量

\_event_id

事件的ID

\_event_type

事件的类型

\_event_type_string

事件类型字符串，用于对事件类型进行详细描述

\_event_time

事件发生的时间

\_event_severity

事件的严重级别

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[var-name*]：环境变量的名称，为1～63个字符的字符串，只能包含数字、字母和下划线，并且不能以下划线开头。

*[var-value*]：环境变量的值。

【使用指导】

在配置监控策略的动作时，我们可以在应该输入参数的地方输入"\$环境变量名"，表示此处需要引用环境变量值。系统在运行监控策略的时候，会自动用环境变量值去替代"\$环境变量名"。

【举例】

\# 设置环境变量if，其值为interface。

\<Sysname\> system-view

Sysname rtm environment if interface

**EAA \-- EAA配置命令 \-- rtm scheduler suspend**

------------------------------------------------------------------------

**[rtm scheduler suspend**]命令用来暂停运行所有的监控策略，包括所有CLI监控策略和TCL监控策略。

**[undo rtm scheduler suspend**]命令用来恢复运行监控策略。

【命令】

**[rtm scheduler suspend**]

**[undo rtm scheduler suspend**]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本命令是用来暂停所有已经配置但还未被触发的策略的，不能暂停处于active状态的策略。

【举例】

\# 暂停所有的监控策略。

\<Sysname\> system-view

Sysname rtm scheduler suspend

**EAA \-- EAA配置命令 \-- rtm tcl-policy**

------------------------------------------------------------------------

**[rtm tcl-policy**]命令用来创建并启用TCL监控策略，并将它和TCL脚本绑定。

**[undo rtm tcl-policy**]命令来删除TCL监控策略。

【命令】

**[rtm tcl-policy*** policy-name tcl-filename*]

**[undo rtm tcl-policy ***policy-name*]

【缺省情况】

未创建TCL监控策略。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：TCL监控策略的名称。为1～63个字符的字符串，区分大小写。

*[tcl-filename*]：TCL脚本文件的名称。文件名区分大小写，扩展名必须为".tcl"，扩展名不区分大小写，且必须为设备存储介质（Flash或者CF卡）上存在的文件。

【使用指导】

使用该命令用来创建并启用一个TCL监控策略，策略的具体内容由绑定的TCL脚本来定义。脚本中会定义策略的触发事件、事件触发时要执行的操作、执行操作需要的角色、策略的运行时间等参数。

TCL监控策略启用后，不允许修改TCL脚本。如需修改，请先停用TCL监控策略，修改后，再启用TCL监控策略。否则，TCL监控策略将不能运行。

TCL监控策略创建后，如果需要绑定另外一个TCL脚本，请先删除该TCL监控策略，再重新创建并绑定。

【举例】

\# 创建并启用TCL监控策略test，并将它和脚本test.tcl绑定。

\<Sysname\> system-view

Sysname rtm tcl-policy test test.tcl

**EAA \-- EAA配置命令 \-- running-time**

------------------------------------------------------------------------

**[running-time**]命令用来配置事件发生时CLI监控策略的运行时间。

**[undo running-time**]命令用来恢复缺省情况。

【命令】

**[running-time*** time*]

**[undo running-time**]

【缺省情况】

CLI监控策略的运行时间为20秒。

【视图】

CLI监控策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：CLI监控策略的运行时间，取值范围为0～31536000，单位为秒。取值为0时，表示策略可以永久运行下去。

【使用指导】

当条件满足，监控策略被触发时，系统会开始计时。当运行时间到，即便策略还没有执行完，也会立即停止执行。该命令用于限制策略的运行时间，以免策略长时间运行占用系统资源。而策略是否会触发以及停止后是否会被再次触发则由**event**配置决定。

【举例】

\# 配置CLI监控策略test的运行时间为60秒。

\<Sysname\> system-view

Sysname rtm cli-policy test

Sysname-rtm-test running-time 60

**EAA \-- EAA配置命令 \-- user-role**

------------------------------------------------------------------------

**[user-role**]命令用来配置执行CLI监控策略时使用的用户角色。

**[undo user-role**]命令用来删除已经配置的指定用户角色。

【命令】

**[user-role ***role-name*]

**[undo user-role ***role-name*]

【缺省情况】

执行CLI监控策略时使用的用户角色为创建该策略的用户的角色。

【视图】

CLI监控策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[role-name*]：执行CLI监控策略时使用的用户角色，为1～63个字符。必须为设备支持的用户角色。

【使用指导】

本命令用来指定执行监控策略的用户角色。用户角色中定义了允许用户操作哪些系统功能以及资源对象，设备支持的每条命令都有缺省用户角色，如果监控策略中指定的用户角色权限比命令行的缺省用户角色的权限小，则不能执行该命令以及该命令后面的所有动作。如果指定的用户角色不存在，则监控策略不能执行。如果给某个监控策略配置了多个用户角色，则使用这些用户角色权限的并集去执行该策略。例如，给某策略配置了用户角色A和B，如果策略中的动作是角色A或者B允许执行的，则策略可以执行；如果策略中存在角色A和B都不能执行的命令，则该命令以及该命令后面的所有动作都不能执行。关于用户角色的详细描述请参见"基础配置指导"中的"RBAC"。

同一监控策略下可配置多个用户角色，最多可以配置64个有效用户角色，超过该上限后，新配置的用户角色即便**commit**也不会生效。

安全日志管理员角色与其它用户角色互斥：为监控策略配置安全日志管理员角色后，系统会自动删除当前配置的其它用户角色；反之亦然。

【举例】

\# 配置执行CLI监控策略test时使用的用户角色为network-admin和admin。

\<Sysname\> system-view

Sysname rtm cli-policy test

Sysname-rtm-test user-role network-admin

Sysname-rtm-test user-role admin
