::: {#1485553624 .myid}
[]{#_Toc404796923}[]{#struct_0_21411_x5561_x1622928753}[]{#_Toc331497855}[]{#_Toc291754543}[]{#_Toc221783225}[]{#_Toc136860125}[]{#_Toc99533458}[]{#_Toc11834548}

**RMON \-- RMON配置命令 \-- display rmon alarm**

------------------------------------------------------------------------

[**[display rmon alarm]{lang="EN-US"}**]{#struct_0_21411_x5561_1179668125}[命令用来显示]{style="font-family:宋体"}[RMON]{lang="EN-US"}[告警表项的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x811692053}

[**[display rmon alarm]{lang="EN-US"}**[ \[ *entry*-*number* \]]{lang="EN-US"}]{#struct_0_21411_x5561_899017132}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x1472463428}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21411_x5561_2130676143}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21411_x5561_1431379882}

[[network-admin]{lang="EN-US"}]{#struct_0_21411_x5561_1369851251}

[[network-operator]{lang="EN-US"}]{#struct_0_21411_x5561_x741030046}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21411_x5561_x974385051}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21411_x5561_346841076}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21411_x5561_914181072}

[*[entry]{lang="EN-US"}*[-*number*]{lang="EN-US"}]{#struct_0_21411_x5561_1032807016}[：告警表项的索引号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果不指定索引号，则显示所有告警表项的相关信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21411_x5561_1147385409}

[[\# ]{lang="EN-US"}]{#struct_0_21411_x5561_x110631384}[显示所有]{style="font-family:宋体"}[RMON]{lang="EN-US"}[告警表项的相关信息。]{style="font-family:宋体"}

[]{#_Toc31278552}[]{#_Toc16392686}[]{#_Toc13469795}[]{#_Toc534447534}[]{#_Toc533505417}[[\<Sysname\> display rmon alarm]{lang="EN-US"}]{#struct_0_21411_x5561_2130741679}

[AlarmEntry 1 owned by user1 is VALID.]{lang="EN-US"}

[  Sample type          : absolute]{lang="EN-US"}

[  Sampled variable     : 1.3.6.1.2.1.16.1.1.1.4.1\<etherStatsOctets.1\>]{lang="EN-US"}

[  Sampling interval (in seconds)     : 10]{lang="EN-US"}

[  Rising threshold      : 50(associated with event 1)]{lang="EN-US"}

[  Falling threshold     : 5(associated with event 2)]{lang="EN-US"}

[  Alarm sent upon entry startup  : risingOrFallingAlarm]{lang="EN-US"}

[  Latest value          : 0]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display rmon alarm]{lang="EN-US"}]{#struct_0_21411_x5561_677417957}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x65750352}[[字段]{style="font-family:黑体"}]{#struct_0_21411_x5561_x190972496}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_21411_x5561_1164393821}

[[AlarmEntry *entry*-*number* owned by *owner* is *status*.]{lang="EN-US"}]{#struct_0_21411_x5561_1271968194}

[*[owner]{lang="EN-US"}*]{#struct_0_21411_x5561_2131069359}[创建的告警表项]{style="font-family:宋体"}*[entry]{lang="EN-US"}*[-*number*]{lang="EN-US"}[的当前状态为]{style="font-family:宋体"}*[status]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[entry-number]{lang="EN-US"}*]{#struct_0_21411_x5561_1011628252}[：告警表项，对应]{lang="EN-US" style="font-family:
  宋体"}[MIB]{lang="EN-US"}[节点]{lang="EN-US" style="font-family:宋体"}[alarmIndex]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[owner]{lang="EN-US"}*]{#struct_0_21411_x5561_x2018072138}[：该表项创建者，对应]{lang="EN-US" style="font-family:宋体"}[MIB]{lang="EN-US"}[节点]{lang="EN-US" style="font-family:宋体"}[alarmOwner]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[status]{lang="EN-US"}*]{#struct_0_21411_x5561_1590900975}[：与该索引对应的告警表项的状态（]{lang="EN-US" style="font-family:宋体"}[VALID]{lang="EN-US"}[表示有效，]{lang="EN-US" style="font-family:宋体"}[UNDERCREATION]{lang="EN-US"}[表示无效。处于无效状态的表项使用]{lang="EN-US" style="font-family:宋体"}**[display rmon alarm]{lang="EN-US"}**[命令可以查看到，但使用]{lang="EN-US" style="font-family:
  宋体"}**[display current-configuration]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[display this]{lang="EN-US"}**[看不到对应的]{lang="EN-US" style="font-family:宋体"}**[rmon alarm]{lang="EN-US"}**[配置命令）。命令行配置告警表项时不可配且缺省为]{lang="EN-US" style="font-family:宋体"}[VALID]{lang="EN-US"}[，对应]{lang="EN-US" style="font-family:宋体"}[MIB]{lang="EN-US"}[节点]{lang="EN-US" style="font-family:宋体"}[alarmStatus]{lang="EN-US"}

[[Sample type]{lang="EN-US"}]{#struct_0_21411_x5561_x668379254}

[[采样类型，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_1581772992}[节点]{style="font-family:宋体"}[alarmSampleType]{lang="EN-US"}[，取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[absolute]{lang="EN-US"}]{#struct_0_21411_x5561_1568181729}[：绝对值采样]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delta]{lang="EN-US"}]{#struct_0_21411_x5561_2131134895}[：变化值采样]{lang="EN-US" style="font-family:宋体"}

[[Sampled variable]{lang="EN-US"}]{#struct_0_21411_x5561_1488598484}

[[告警变量，即被监控的]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_1984745983}[节点，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}[节点]{style="font-family:宋体"}[alarmVariable]{lang="EN-US"}

[[Sampling interval]{lang="EN-US"}]{#struct_0_21411_x5561_97238544}

[[采样的时间间隔，单位为秒，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x1759030617}[节点]{style="font-family:宋体"}[alarmInterval]{lang="EN-US"}

[[Rising threshold]{lang="EN-US"}]{#struct_0_21411_x5561_x1501089794}

[[上限阈值（当采样值大于等于该值时引发上限告警），对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x598338281}[节点]{style="font-family:宋体"}[alarmRisingThreshold]{lang="EN-US"}

[[associated with event]{lang="EN-US"}]{#struct_0_21411_x5561_x816742141}

[[告警对应的事件索引，上限事件索引对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x1068439162}[节点]{style="font-family:宋体"}[alarmRisingEventIndex]{lang="EN-US"}[，下限事件索引对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}[节点]{style="font-family:宋体"}[alarmFallingEventIndex]{lang="EN-US"}

[[Falling threshold]{lang="EN-US"}]{#struct_0_21411_x5561_x419619924}

[[下限阈值（当采样值小于等于该值时引发下限告警），对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x525270246}[节点]{style="font-family:宋体"}[alarmFallingThreshold]{lang="EN-US"}

[[Alarm sent upon entry startup]{lang="EN-US"}]{#struct_0_21411_x5561_x598272745}

[[初次触发告警类型：]{style="font-family:宋体"}]{#struct_0_21411_x5561_x40420280}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[risingAlarm]{lang="EN-US"}]{#struct_0_21411_x5561_1304299402}[：表示触发上限告警]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[fallingAlarm]{lang="EN-US"}]{#struct_0_21411_x5561_x829276769}[：表示触发下限告警]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[risingorFallingAlarm]{lang="EN-US"}]{#struct_0_21411_x5561_x2035673222}[：表示触发上限或下限告警]{lang="EN-US" style="font-family:
  宋体"}

[[缺省情况下，触发]{style="font-family:宋体"}[risingorFallingAlarm]{lang="EN-US"}]{#struct_0_21411_x5561_x598469353}[类型告警，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}[节点]{style="font-family:宋体"}[alarmStartupAlarm]{lang="EN-US"}

[[Latest value]{lang="EN-US"}]{#struct_0_21411_x5561_x1191703370}

[[最近一次采样值，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x1340234070}[节点]{style="font-family:宋体"}[alarmValue]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21411_x5561_1644291003}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rmon alarm]{lang="EN-US"}**]{#struct_0_21411_x5561_1708832946}

::: {#-533377582 .myid}
[]{#_Toc404796924}[]{#struct_0_21411_x5561_x1382073937}[]{#_Toc331497856}

**RMON \-- RMON配置命令 \-- display rmon event**

------------------------------------------------------------------------

[**[display rmon event]{lang="EN-US"}**]{#struct_0_21411_x5561_1786013239}[命令用来显示]{style="font-family:宋体"}[RMON]{lang="EN-US"}[事件表项相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x598403817}

[**[display rmon event]{lang="EN-US"}**[ \[ *entry-number* \]]{lang="EN-US"}]{#struct_0_21411_x5561_1856227412}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21411_x5561_330822933}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21411_x5561_1242444954}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21411_x5561_1784705249}

[[network-admin]{lang="EN-US"}]{#struct_0_21411_x5561_x2010857965}

[[network-operator]{lang="EN-US"}]{#struct_0_21411_x5561_x1218170028}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21411_x5561_x1959300758}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21411_x5561_1036711417}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x686776288}

[*[entry-number]{lang="EN-US"}*]{#struct_0_21411_x5561_x598076137}[：事件表项的索引号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果不指定索引号，则显示所有事件表项的相关信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x862908807}

[[显示信息包括：事件表中的事件索引、事件的所有者、对事件的描述、事件引发的动作（日志或告警信息）、最近一次事件发生的时刻（此时间是以系统初始化]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21411_x5561_1780251857}[启动以来的秒数计算的）等。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x1738019757}

[[\# ]{lang="EN-US"}]{#struct_0_21411_x5561_499214129}[显示所有]{style="font-family:宋体"}[RMON]{lang="EN-US"}[事件表项相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display rmon event]{lang="EN-US"}]{#struct_0_21411_x5561_1514131125}

[EventEntry 1 owned by user1 is VALID.]{lang="EN-US"}

[  Description: N/A]{lang="EN-US"}

[  Community: Security]{lang="EN-US"}

[  Take the action log-trap when triggered, last triggered at 0days 00h:02m:27s uptime.]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display rmon event]{lang="EN-US"}]{#struct_0_21411_x5561_406229100}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x64575280}[[字段]{style="font-family:黑体"}]{#struct_0_21411_x5561_x598010601}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_21411_x5561_x1229511360}

[[EventEntry *entry*-*number* owned by *owner* is *status*.]{lang="EN-US"}]{#struct_0_21411_x5561_1698684008}

[*[Owner]{lang="EN-US"}*]{#struct_0_21411_x5561_x2002507050}[创建的事件表项]{style="font-family:宋体"}*[entry]{lang="EN-US"}*[-*number*]{lang="EN-US"}[的当前状态为]{style="font-family:宋体"}*[status]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[entry-number]{lang="EN-US"}*]{#struct_0_21411_x5561_344628721}[：事件表项，对应]{lang="EN-US" style="font-family:
  宋体"}[MIB]{lang="EN-US"}[节点]{lang="EN-US" style="font-family:宋体"}[eventIndex]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[owner]{lang="EN-US"}*]{#struct_0_21411_x5561_x989858806}[：该表项创建者，对应]{lang="EN-US" style="font-family:宋体"}[MIB]{lang="EN-US"}[节点]{lang="EN-US" style="font-family:宋体"}[eventOwner]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[status]{lang="EN-US"}*]{#struct_0_21411_x5561_1353359510}[：与该索引对应的事件表项的状态（]{lang="EN-US" style="font-family:宋体"}[VALID]{lang="EN-US"}[表示有效，]{lang="EN-US" style="font-family:宋体"}[UNDERCREATION]{lang="EN-US"}[表示无效。处于无效状态的表项使用]{lang="EN-US" style="font-family:宋体"}**[display rmon event]{lang="EN-US"}**[命令可以查看到，但使用]{lang="EN-US" style="font-family:
  宋体"}**[display current-configuration]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[display this]{lang="EN-US"}**[看不到对应的]{lang="EN-US" style="font-family:宋体"}**[rmon event]{lang="EN-US"}**[配置命令）。命令行配置]{lang="EN-US" style="font-family:宋体"}[event]{lang="EN-US"}[表项时不可配且默认为]{lang="EN-US" style="font-family:宋体"}[VALID]{lang="EN-US"}[，对应]{lang="EN-US" style="font-family:宋体"}[MIB]{lang="EN-US"}[节点]{lang="EN-US" style="font-family:宋体"}[eventStatus]{lang="EN-US"}

[[Description]{lang="EN-US"}]{#struct_0_21411_x5561_x598207209}

[[该事件表项的描述，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x2023908835}[节点]{style="font-family:宋体"}[eventDescription]{lang="EN-US"}

[[Community]{lang="EN-US"}]{#struct_0_21411_x5561_225072947}

[[接收告警信息的网管站的团体名，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_1209944243}[节点]{style="font-family:宋体"}[eventCommunity]{lang="EN-US"}

[[Take the action *action* when triggered]{lang="EN-US"}]{#struct_0_21411_x5561_x98372301}

[[事件触发时采取的动作：]{style="font-family:宋体"}]{#struct_0_21411_x5561_624808051}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[none]{lang="EN-US"}]{#struct_0_21411_x5561_x598141673}[：表示不采取任何措施]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[log]{lang="EN-US"}]{#struct_0_21411_x5561_351580419}[：表示事件被触发时会记录日志]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[trap]{lang="EN-US"}]{#struct_0_21411_x5561_1566625183}[：表示事件被触发时会生成告警信息发送给设备的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[模块]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[log-trap]{lang="EN-US"}]{#struct_0_21411_x5561_2018351768}[：表示事件被触发时既会记录日志又会生成告警信息发送给设备的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[模块]{style="font-family:宋体"}

[[对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_611484516}[节点]{style="font-family:宋体"}[eventType]{lang="EN-US"}

[[last triggered at]{lang="EN-US"}]{#struct_0_21411_x5561_x1287109001}

[*[time]{lang="EN-US"}*[ uptime]{lang="EN-US"}]{#struct_0_21411_x5561_x597813993}

[[最近一次事件发生的时间（设备启动以来的时间），对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x302462752}[节点]{style="font-family:宋体"}[eventLastTimeSent]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21411_x5561_167512111}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rmon event]{lang="EN-US"}**]{#struct_0_21411_x5561_31506507}

::: {#1141945877 .myid}
[]{#_Toc404796925}[]{#struct_0_21411_x5561_976360724}[]{#_Toc331497857}

**RMON \-- RMON配置命令 \-- display rmon eventlog**

------------------------------------------------------------------------

[**[display rmon eventlog]{lang="EN-US"}**]{#struct_0_21411_x5561_558211434}[命令用来显示事件日志表项的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x1767360330}

[**[display rmon eventlog]{lang="EN-US"}**[ \[ *entry-number* \]]{lang="EN-US"}]{#struct_0_21411_x5561_x597748457}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x1002208910}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21411_x5561_694525416}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21411_x5561_118182821}

[[network-admin]{lang="EN-US"}]{#struct_0_21411_x5561_x1684680303}

[[network-operator]{lang="EN-US"}]{#struct_0_21411_x5561_x2030818035}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21411_x5561_x93819239}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21411_x5561_1005701951}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x365062103}

[*[entry-number]{lang="EN-US"}*]{#struct_0_21411_x5561_x598338280}[：事件表项的索引号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果不指定索引号，则显示所有事件的日志表项的相关信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x816676605}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果使用]{style="font-family:宋体"}]{#struct_0_21411_x5561_67419157}**[rmon]{lang="EN-US"}**[ **event**]{lang="EN-US"}[命令指定某表项的动作包括记录日志，当该事件被触发时，就会在]{style="font-family:宋体"}[RMON]{lang="EN-US"}[事件日志表中记录一条该事件的日志。通过该命令可以显示事件日志表的具体内容：事件表中的事件索引及事件当前的状态、事件产生日志的时刻（此时间是以系统初始化]{style="font-family:宋体"}[/]{lang="EN-US"}[启动以来的秒数计算的）以及事件的描述等。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每个事件最多有]{style="font-family:宋体"}]{#struct_0_21411_x5561_1229313386}[10]{lang="EN-US"}[个日志记录，后续如果再产生日志记录将覆盖最老的。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x1146580532}

[[\# ]{lang="EN-US"}]{#struct_0_21411_x5561_x2113339883}[查看由告警表产生的]{style="font-family:宋体"}[RMON]{lang="EN-US"}[事件]{style="font-family:宋体"}[99]{lang="EN-US"}[的日志。]{style="font-family:宋体"}

[[\<Sysname\> display rmon eventlog 99]{lang="EN-US"}]{#struct_0_21411_x5561_x598272744}

[EventEntry 99 owned by ww is VALID.]{lang="EN-US"}

[  LogEntry 99.1 created at 50days 08h:54m:44s uptime.]{lang="EN-US"}

[  Description: The 1.3.6.1.2.1.16.1.1.1.4.5 defined in alarmEntry 77,]{lang="EN-US"}

[     uprise 16760000 with alarm value 16776314. Alarm sample type is absolute.]{lang="EN-US"}

[  LogEntry 99.2 created at 50days 09h:11m:13s uptime.]{lang="EN-US"}

[  Description: The 1.3.6.1.2.1.16.1.1.1.4.5 defined in alarmEntry 77,]{lang="EN-US"}

[     less than(or =) 20000000 with alarm value 16951648. Alarm sample type is ab]{lang="EN-US"}

[solute.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21411_x5561_x40354744}[查看由扩展告警表产生的]{style="font-family:宋体"}[RMON]{lang="EN-US"}[事件]{style="font-family:宋体"}[99]{lang="EN-US"}[的日志。]{style="font-family:宋体"}

[[\<Sysname\> display rmon eventlog 99]{lang="EN-US"}]{#struct_0_21411_x5561_587747096}

[EventEntry 99 owned by ww is VALID.]{lang="EN-US"}

[  LogEntry 99.3 created at 50days 09h:18m:43s uptime.]{lang="EN-US"}

[  Description: The alarm formula defined in prialarmEntry 777,]{lang="EN-US"}

[     less than(or =) 15000000 with alarm value 14026493. Alarm sample type is ab]{lang="EN-US"}

[solute.]{lang="EN-US"}

[  LogEntry 99.4 created at 50days 09h:23m:28s uptime.]{lang="EN-US"}

[  Description: The alarm formula defined in prialarmEntry 777,]{lang="EN-US"}

[     uprise 17000000 with alarm value 17077846. Alarm sample type is absolute.]{lang="EN-US"}

[]{#struct_0_21411_x5561_1177363597}[]{#_Toc138065899}[]{#_Toc98246492}[]{#_Toc31278554}[]{#_Toc16392688}[]{#_Toc13469797}[]{#_Toc534447536}[[表1-3 ]{lang="EN-US"}[display rmon eventlog]{lang="EN-US"}]{#_Toc533505419}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x37548976}[[字段]{style="font-family:黑体"}]{#struct_0_21411_x5561_910797246}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_21411_x5561_x1104979545}

[[EventEntry *entry*-*number* owned by *owner* is *status*.]{lang="EN-US"}]{#struct_0_21411_x5561_x598469352}

[*[Owner]{lang="EN-US"}*]{#struct_0_21411_x5561_x1191768906}[创建的事件日志表项]{style="font-family:宋体"}*[entry]{lang="EN-US"}*[-*number*]{lang="EN-US"}[的当前状态为]{style="font-family:宋体"}*[status]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[entry-number]{lang="EN-US"}*]{#struct_0_21411_x5561_929067580}[：事件日志表项，对应事件表中]{lang="EN-US" style="font-family:
  宋体"}[MIB]{lang="EN-US"}[节点]{lang="EN-US" style="font-family:宋体"}[logEventIndex]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[owner]{lang="EN-US"}*]{#struct_0_21411_x5561_1232065508}[：该表项创建者，对应事件表中]{lang="EN-US" style="font-family:宋体"}[MIB]{lang="EN-US"}[节点]{lang="EN-US" style="font-family:宋体"}[eventOwner]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[status]{lang="EN-US"}*]{#struct_0_21411_x5561_1411894804}[：与该索引对应的事件日志表项的状态（]{lang="EN-US" style="font-family:宋体"}[VALID]{lang="EN-US"}[表示有效，]{lang="EN-US" style="font-family:宋体"}[UNDERCREATION]{lang="EN-US"}[表示无效。处于无效状态的表项使用]{lang="EN-US" style="font-family:宋体"}**[display rmon eventlog]{lang="EN-US"}**[可以查看到，但使用]{lang="EN-US" style="font-family:
  宋体"}**[display current-configuration]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[display this]{lang="EN-US"}**[看不到对应的]{lang="EN-US" style="font-family:宋体"}**[rmon eventlog]{lang="EN-US"}**[配置命令）。命令行配置]{lang="EN-US" style="font-family:宋体"}[event]{lang="EN-US"}[表项时不可配且默认为]{lang="EN-US" style="font-family:宋体"}[VALID]{lang="EN-US"}[，对应]{lang="EN-US" style="font-family:宋体"}[MIB]{lang="EN-US"}[节点]{lang="EN-US" style="font-family:宋体"}[eventStatus]{lang="EN-US"}

[[LogEntry *entry*-*number* created at *created-time*]{lang="EN-US"}]{#struct_0_21411_x5561_2034226825}

[[uptime.]{lang="EN-US"}]{#struct_0_21411_x5561_x1684529376}

[[日志表项]{style="font-family:宋体"}*[entry]{lang="EN-US"}*[-*number*]{lang="EN-US"}]{#struct_0_21411_x5561_x598403816}[的创建时间为]{style="font-family:宋体"}*[created-time]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[entry-number]{lang="EN-US"}*]{#struct_0_21411_x5561_1856161876}[：日志表项索引号，表示方式为]{lang="EN-US" style="font-family:
  宋体"}[logEventIndex.logIndex]{lang="EN-US"}[，对应]{lang="EN-US" style="font-family:宋体"}[MIB]{lang="EN-US"}[节点]{lang="EN-US" style="font-family:宋体"}[logEventIndex]{lang="EN-US"}[与]{lang="EN-US" style="font-family:宋体"}[logIndex]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[created-time]{lang="EN-US"}*]{#struct_0_21411_x5561_1518383194}[：日志表项的创建时间，对应]{lang="EN-US" style="font-family:
  宋体"}[MIB]{lang="EN-US"}[节点]{lang="EN-US" style="font-family:宋体"}[logTime]{lang="EN-US"}

[[Description]{lang="EN-US"}]{#struct_0_21411_x5561_87795565}

[[该条日志的描述，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_2059919792}[节点]{style="font-family:宋体"}[logDescription]{lang="EN-US"}

[ ]{lang="EN-US"}

[[以上举例表明事件]{style="font-family:宋体"}[99]{lang="EN-US"}]{#struct_0_21411_x5561_1578715003}[产生的告警事件日志，其中告警表产生的事件日志]{style="font-family:宋体"}[2]{lang="EN-US"}[条，扩展告警表产生的事件日志]{style="font-family:宋体"}[2]{lang="EN-US"}[条：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[日志]{style="font-family:宋体"}]{#struct_0_21411_x5561_408130166}[99.1]{lang="EN-US"}[由告警表项]{style="font-family:宋体"}[77]{lang="EN-US"}[触发生成，原因是告警值（]{style="font-family:宋体"}[16776314]{lang="EN-US"}[）超过了上限阈值（]{style="font-family:宋体"}[16760000]{lang="EN-US"}[），采样类型为绝对值采样。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[日志]{style="font-family:宋体"}]{#struct_0_21411_x5561_x598076136}[99.2]{lang="EN-US"}[由告警表项]{style="font-family:宋体"}[77]{lang="EN-US"}[触发生成，原因是告警值（]{style="font-family:宋体"}[16951648]{lang="EN-US"}[）低于下限阈值（]{style="font-family:宋体"}[20000000]{lang="EN-US"}[），采样类型为绝对值采样。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[日志]{style="font-family:宋体"}]{#struct_0_21411_x5561_x862843271}[99.3]{lang="EN-US"}[由扩展告警表项]{style="font-family:宋体"}[777]{lang="EN-US"}[触发生成，原因是告警值（]{style="font-family:宋体"}[14026493]{lang="EN-US"}[）低于下限阈值（]{style="font-family:宋体"}[15000000]{lang="EN-US"}[），采样类型为绝对值采样。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[日志]{style="font-family:宋体"}]{#struct_0_21411_x5561_x656769130}[99.4]{lang="EN-US"}[由扩展告警表项]{style="font-family:宋体"}[777]{lang="EN-US"}[触发生成，原因是告警值（]{style="font-family:宋体"}[17077846]{lang="EN-US"}[）超过上限阈值（]{style="font-family:宋体"}[17000000]{lang="EN-US"}[），采样类型为绝对值采样。]{style="font-family:宋体"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21411_x5561_547955429}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rmon event]{lang="EN-US"}**]{#struct_0_21411_x5561_232126157}

::: {#1718298004 .myid}
[]{#_Toc404796926}[]{#struct_0_21411_x5561_x769549389}[]{#_Toc331497858}[]{#_Toc291754546}[]{#_Toc221783228}[]{#_Toc136860128}[]{#_Toc99533461}[]{#_Toc11834551}

**RMON \-- RMON配置命令 \-- display rmon history**

------------------------------------------------------------------------

[**[display rmon history]{lang="EN-US"}**]{#struct_0_21411_x5561_563278063}[命令用来显示]{style="font-family:宋体"}[RMON]{lang="EN-US"}[历史控制表及历史采样信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x87030598}

[**[display rmon history]{lang="EN-US"}**[ \[ *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_21411_x5561_816144375}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x598010600}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21411_x5561_x1229445824}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x1872797642}

[[network-admin]{lang="EN-US"}]{#struct_0_21411_x5561_x537704101}

[[network-operator]{lang="EN-US"}]{#struct_0_21411_x5561_1199050825}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21411_x5561_x1787537233}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21411_x5561_x1680902453}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21411_x5561_1383492604}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_21411_x5561_1905757624}[：指定接口类型和接口编号。如果未指定本参数，则显示所有接口下配置的历史控制表及历史采样信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x598207208}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在端口创建历史表项之后，系统会按一定的时间周期统计端口的信息，并将这些信息保存到]{style="font-family:宋体"}]{#struct_0_21411_x5561_x2023974371}[etherHistoryEntry]{lang="EN-US"}[表，使用本命令可以显示该表项存储的记录。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[可显示的历史采样信息的数目以及历史采样的间隔可以通过]{style="font-family:宋体"}]{#struct_0_21411_x5561_1309561217}**[rmon history]{lang="EN-US"}**[命令来设置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21411_x5561_108238819}

[[\# ]{lang="EN-US"}]{#struct_0_21411_x5561_x56438090}[显示端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[RMON]{lang="EN-US"}[历史控制表及历史采样信息。]{style="font-family:宋体"}

[[\<Sysname\> display rmon history gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_21411_x5561_x598141672}

[HistoryControlEntry 6 owned by user1 is VALID.]{lang="EN-US"}

[  Sampled interface     : GigabitEthernet 1/0/1 \<ifIndex.117\>]{lang="EN-US"}

[  Sampling interval     : 8(sec) with 3 buckets max]{lang="EN-US"}

[  Sampling record 1 :]{lang="EN-US"}

[    dropevents        : 0         , octets               : 5869]{lang="EN-US"}

[    packets           : 54        , broadcast packets    : 9]{lang="EN-US"}

[    multicast packets : 23        , CRC alignment errors : 0]{lang="EN-US"}

[    undersize packets : 0         , oversize packets     : 0]{lang="EN-US"}

[    fragments         : 0         , jabbers              : 0]{lang="EN-US"}

[    collisions        : 0         , utilization          : 0]{lang="EN-US"}

[  Sampling record 2 :]{lang="EN-US"}

[    dropevents        : 0         , octets               : 5367]{lang="EN-US"}

[    packets           : 55        , broadcast packets    : 1]{lang="EN-US"}

[    multicast packets : 7         , CRC alignment errors : 0]{lang="EN-US"}

[    undersize packets : 0         , oversize packets     : 0]{lang="EN-US"}

[    fragments         : 0         , jabbers              : 0]{lang="EN-US"}

[    collisions        : 0         , utilization          : 0]{lang="EN-US"}

[  Sampling record 3 :]{lang="EN-US"}

[    dropevents        : 0         , octets               : 936]{lang="EN-US"}

[    packets           : 10        , broadcast packets    : 0]{lang="EN-US"}

[    multicast packets : 6         , CRC alignment errors : 0]{lang="EN-US"}

[    undersize packets : 0         , oversize packets     : 0]{lang="EN-US"}

[    fragments         : 0         , jabbers              : 0]{lang="EN-US"}

[    collisions        : 0         , utilization          : 0]{lang="EN-US"}

[HistoryControlEntry 7 owned by user1 is VALID.]{lang="EN-US"}

[  Sampled interface     : GigabitEthernet 1/0/1 \<ifIndex.117\>]{lang="EN-US"}

[  Sampling interval     : 9(sec) with 1 buckets max]{lang="EN-US"}

[  Sampling record 1 :]{lang="EN-US"}

[    dropevents        : 0         , octets               : 1150]{lang="EN-US"}

[    packets           : 12        , broadcast packets    : 0]{lang="EN-US"}

[    multicast packets : 8         , CRC alignment errors : 0]{lang="EN-US"}

[    undersize packets : 0         , oversize packets     : 0]{lang="EN-US"}

[    fragments         : 0         , jabbers              : 0]{lang="EN-US"}

[    collisions        : 0         , utilization          : 0]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display rmon history]{lang="EN-US"}]{#struct_0_21411_x5561_351514883}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x33872752}[[字段]{style="font-family:黑体"}]{#struct_0_21411_x5561_x597813992}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_21411_x5561_x302397216}

[[HistoryControlEntry *entry*-*number* owned by *owner* is *status*.]{lang="EN-US"}]{#struct_0_21411_x5561_x673100077}

[*[Owner]{lang="EN-US"}*]{#struct_0_21411_x5561_534905336}[创建的历史控制表项]{style="font-family:宋体"}*[entry]{lang="EN-US"}*[-*number*]{lang="EN-US"}[的当前状态为]{style="font-family:宋体"}*[status]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[entry-number]{lang="EN-US"}*]{#struct_0_21411_x5561_335920693}[：历史控制表项，对应]{lang="EN-US" style="font-family:
  宋体"}[MIB]{lang="EN-US"}[节点]{lang="EN-US" style="font-family:宋体"}[historyControlIndex]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[owner]{lang="EN-US"}*]{#struct_0_21411_x5561_2020892844}[：该表项的创建者，对应]{lang="EN-US" style="font-family:宋体"}[MIB]{lang="EN-US"}[节点]{lang="EN-US" style="font-family:宋体"}[historyControlOwner]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[status]{lang="EN-US"}*]{#struct_0_21411_x5561_x1213919343}[：与该索引对应的历史控制表项的状态（]{lang="EN-US" style="font-family:宋体"}[VALID]{lang="EN-US"}[表示有效，]{lang="EN-US" style="font-family:宋体"}[UNDERCREATION]{lang="EN-US"}[表示无效。处于无效状态的表项使用]{lang="EN-US" style="font-family:宋体"}**[display rmon history]{lang="EN-US"}**[命令可以查看到，但使用]{lang="EN-US" style="font-family:
  宋体"}**[display current-configuration]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[display this]{lang="EN-US"}**[看不到对应的]{lang="EN-US" style="font-family:宋体"}**[rmon history]{lang="EN-US"}**[配置命令）。命令行配置]{lang="EN-US" style="font-family:宋体"}[HistoryConrtol]{lang="EN-US"}[表项时不可配置且默认为]{lang="EN-US" style="font-family:宋体"}[VALID]{lang="EN-US"}[，对应]{lang="EN-US" style="font-family:宋体"}[MIB]{lang="EN-US"}[节点]{lang="EN-US" style="font-family:宋体"}[historyControlStatus]{lang="EN-US"}

[[Sampled Interface]{lang="EN-US"}]{#struct_0_21411_x5561_x597748456}

[[被统计的接口，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x1002274446}[节点]{style="font-family:宋体"}[historyControlDataSource]{lang="EN-US"}

[[Sampling interval]{lang="EN-US"}]{#struct_0_21411_x5561_1778423872}

[[统计周期，单位为秒，系统会按周期对端口的信息进行统计，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_633776412}[节点]{style="font-family:宋体"}[historyControlInterval]{lang="EN-US"}

[[buckets max]{lang="EN-US"}]{#struct_0_21411_x5561_1342907429}

[[系统最多可保存的统计值的条数]{style="font-family:宋体"}]{#struct_0_21411_x5561_1575484326}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在]{lang="EN-US" style="font-family:宋体"}**[rmon history]{lang="EN-US"}**]{#struct_0_21411_x5561_x598338283}[命令中指定的]{lang="EN-US" style="font-family:宋体"}**[buckets]{lang="EN-US"}**[的值超出了设备实际支持的历史表容量，则此处显示的是设备实际支持的历史表容量]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果当前保存的统计值条数已经到达了系统支持的最大值，则系统会删除最早的记录来保存新的统计值，对应]{style="font-family:宋体"}]{#struct_0_21411_x5561_x816873213}[MIB]{lang="EN-US"}[节点]{style="font-family:宋体"}[historyControlBucketsGranted]{lang="EN-US"}

[[Sampling record ]{lang="EN-US"}]{#struct_0_21411_x5561_x1456638641}

[[历史采样表项索引号，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x1475421432}[节点]{style="font-family:宋体"}[etherHistorySampleIndex]{lang="EN-US"}

[[dropevents]{lang="EN-US"}]{#struct_0_21411_x5561_x987493953}

[[统计周期内检测到的丢包事件次数，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x598272747}[节点]{style="font-family:宋体"}[etherHistoryDropEvents]{lang="EN-US"}

[[octets]{lang="EN-US"}]{#struct_0_21411_x5561_x40551352}

[[统计周期内接收到的字节数，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_479755430}[节点]{style="font-family:宋体"}[etherHistoryOctets]{lang="EN-US"}

[[packets]{lang="EN-US"}]{#struct_0_21411_x5561_x442231240}

[[统计周期内接收到的包数，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_1977058627}[节点]{style="font-family:宋体"}[etherHistoryPkts]{lang="EN-US"}

[[broadcast packets]{lang="EN-US"}]{#struct_0_21411_x5561_x598469355}

[[统计周期内接收到的广播包数，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x1192096586}[节点]{style="font-family:宋体"}[etherHistoryBroadcastPkts]{lang="EN-US"}

[[multicast packets]{lang="EN-US"}]{#struct_0_21411_x5561_x229041170}

[[统计周期内接收到的组播包数，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_1596486924}[节点]{style="font-family:宋体"}[etherHistoryMulticastPkts]{lang="EN-US"}

[[CRC alignment errors]{lang="EN-US"}]{#struct_0_21411_x5561_1274102112}

[[统计周期内接收到的校验错误的包数，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x598403819}[节点]{style="font-family:宋体"} [etherHistoryCRCAlignErrors]{lang="EN-US"}

[[undersize packets]{lang="EN-US"}]{#struct_0_21411_x5561_1857144916}

[[统计周期内接收到的过小的包数，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x865185145}[节点]{style="font-family:宋体"}[etherHistoryUndersizePkts]{lang="EN-US"}

[[oversize packets]{lang="EN-US"}]{#struct_0_21411_x5561_x1139054652}

[[统计周期内接收到的超大的包数，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x598076139}[节点]{style="font-family:宋体"}[etherHistoryOversizePkts]{lang="EN-US"}

[[fragments]{lang="EN-US"}]{#struct_0_21411_x5561_x863564167}

[[统计周期内接收到的过小且校验错误的包数，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_130675603}[节点]{style="font-family:宋体"}[etherHistoryFragments]{lang="EN-US"}

[[jabbers]{lang="EN-US"}]{#struct_0_21411_x5561_1071516866}

[[统计周期内接收到的超大且校验错误的包数，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x598010603}[节点]{style="font-family:宋体"}[etherHistoryJabbers]{lang="EN-US"}[（该字段的支持情况与设备型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}

[[collisions]{lang="EN-US"}]{#struct_0_21411_x5561_x1229380288}

[[统计周期内接收到的冲突的包数，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_1945913516}[节点]{style="font-family:宋体"}[etherHistoryCollisions]{lang="EN-US"}

[[utilization]{lang="EN-US"}]{#struct_0_21411_x5561_489672213}

[[统计周期内的带宽利用率，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x598207211}[节点]{style="font-family:宋体"}[etherHistoryUtilization]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x2024433122}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rmon history]{lang="EN-US"}**]{#struct_0_21411_x5561_x618486131}

::: {#-858458789 .myid}
[]{#_Toc404796927}[]{#struct_0_21411_x5561_914537429}[]{#_Toc331497859}[]{#_Toc291754547}[]{#_Toc221783229}[]{#_Toc136860129}[]{#_Toc99533462}

**RMON \-- RMON配置命令 \-- display rmon prialarm**

------------------------------------------------------------------------

[**[display rmon prialarm]{lang="EN-US"}**]{#struct_0_21411_x5561_x1953198178}[命令用来显示扩展告警表项的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21411_x5561_1236717654}

[**[display rmon prialarm]{lang="EN-US"}**[ \[ *entry-number* \]]{lang="EN-US"}]{#struct_0_21411_x5561_x1609648402}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21411_x5561_1072955852}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21411_x5561_x598141675}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21411_x5561_351973635}

[[network-admin]{lang="EN-US"}]{#struct_0_21411_x5561_1654187518}

[[network-operator]{lang="EN-US"}]{#struct_0_21411_x5561_1458107571}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21411_x5561_961410232}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21411_x5561_1656240601}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21411_x5561_1724589394}

[*[entry-number]{lang="EN-US"}*]{#struct_0_21411_x5561_x166703946}[：扩展告警表项的索引，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果不指定索引号，则显示所有扩展告警表项的相关信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x392724684}

[[\# ]{lang="EN-US"}]{#struct_0_21411_x5561_x597813995}[显示]{style="font-family:宋体"}[RMON]{lang="EN-US"}[所有的扩展告警表项的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display rmon prialarm]{lang="EN-US"}]{#struct_0_21411_x5561_x302855968}

[PrialarmEntry 1 owned by user1 is VALID.]{lang="EN-US"}

[  Sample type          : absolute]{lang="EN-US"}

[  Variable formula      : (.1.3.6.1.2.1.16.1.1.1.6.1\*100/.1.3.6.1.2.1.16.1.1.1.5.1)]{lang="EN-US"}

[  Description           : ifUtilization.GigabitEthernet1/0/1]{lang="EN-US"}

[  Sampling interval (in seconds)     : 10]{lang="EN-US"}

[  Rising threshold      : 80(associated with event 1)]{lang="EN-US"}

[  Falling threshold     : 5(associated with event 2)]{lang="EN-US"}

[  Alarm sent upon entry startup  : risingOrFallingAlarm]{lang="EN-US"}

[  Entry lifetime : forever]{lang="EN-US"}

[  Latest value          : 85]{lang="EN-US"}

[]{#struct_0_21411_x5561_940390635}[[表1-5 ]{lang="EN-US"}[display rmon prialarm]{lang="EN-US"}]{#_Ref331682763}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x39193040}[[字段]{style="font-family:黑体"}]{#struct_0_21411_x5561_x1340462058}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_21411_x5561_364399074}

[[PrialarmEntry *entry*-*number* owned by *owner* is *status*.]{lang="EN-US"}]{#struct_0_21411_x5561_x597748459}

[*[Owner]{lang="EN-US"}*]{#struct_0_21411_x5561_x1002864270}[创建的扩展告警表项]{style="font-family:宋体"}*[entry]{lang="EN-US"}*[-*number*]{lang="EN-US"}[的当前状态为]{style="font-family:宋体"}*[status]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[entry-number]{lang="EN-US"}*]{#struct_0_21411_x5561_x144855579}[：扩展告警表项，对应]{lang="EN-US" style="font-family:
  宋体"}[MIB]{lang="EN-US"}[节点]{lang="EN-US" style="font-family:宋体"}[h]{lang="EN-US"}[h3cRmonExtAlarmIndex]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[owner]{lang="EN-US"}*]{#struct_0_21411_x5561_x1587235842}[：该表项创建者，对应]{lang="EN-US" style="font-family:宋体"}[MIB]{lang="EN-US"}[节点]{lang="EN-US" style="font-family:宋体"}[h]{lang="EN-US"}[h3cRmonExtAlarmOwner]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[status]{lang="EN-US"}*]{#struct_0_21411_x5561_x234952098}[：与该索引对应的扩展告警表项的状态（]{lang="EN-US" style="font-family:宋体"}[VALID]{lang="EN-US"}[表示有效，]{lang="EN-US" style="font-family:宋体"}[UNDERCREATION]{lang="EN-US"}[表示无效。处于无效状态的表项使用]{lang="EN-US" style="font-family:宋体"}**[display rmon prialarm]{lang="EN-US"}**[命令可以查看到，但使用]{lang="EN-US" style="font-family:
  宋体"}**[display current-configuration]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[display this]{lang="EN-US"}**[看不到相应的]{lang="EN-US" style="font-family:宋体"}**[rmon prialarm]{lang="EN-US"}**[配置命令）。命令行配置]{lang="EN-US" style="font-family:宋体"}[prialarm]{lang="EN-US"}[表项时不可配且默认为]{lang="EN-US" style="font-family:宋体"}[VALID]{lang="EN-US"}[，对应]{lang="EN-US" style="font-family:宋体"}[MIB]{lang="EN-US"}[节点]{lang="EN-US" style="font-family:宋体"}[h]{lang="EN-US"}[h3cRmonExtAlarmStatus]{lang="EN-US"}

[[Sample type]{lang="EN-US"}]{#struct_0_21411_x5561_2021641271}

[[采样类型，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x1236231105}[节点]{style="font-family:宋体"}[hh3cRmonExtAlarmSampleType]{lang="EN-US"}[，取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[absolute]{lang="EN-US"}]{#struct_0_21411_x5561_x598338282}[：绝对值采样]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delta]{lang="EN-US"}]{#struct_0_21411_x5561_x816807677}[：变化值采样]{lang="EN-US" style="font-family:宋体"}

[[Variable formula]{lang="EN-US"}]{#struct_0_21411_x5561_1638287289}

[[样本变量的计算公式，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_1446164355}[节点]{style="font-family:宋体"}[hh3cRmonExtAlarmVariable]{lang="EN-US"}

[[Description]{lang="EN-US"}]{#struct_0_21411_x5561_x192319152}

[[扩展告警表项的描述信息，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x598272746}[节点]{style="font-family:宋体"}[hh3cRmonExtAlarmSympol]{lang="EN-US"}

[[Sampling interval]{lang="EN-US"}]{#struct_0_21411_x5561_x40485816}

[[采样间隔，单位为秒，系统会按一定的时间间隔对采样变量进行绝对值采样或者变化值采样，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x1887791428}[节点]{style="font-family:宋体"}[hh3cRmonExtAlarmInterval]{lang="EN-US"}

[[Rising threshold]{lang="EN-US"}]{#struct_0_21411_x5561_x364158059}

[[告警上限，当采样值大于等于该值时引发上限告警，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x1563919386}[节点]{style="font-family:宋体"}[hh3cRmonExtAlarmRisingThreshold]{lang="EN-US"}

[[Falling threshold]{lang="EN-US"}]{#struct_0_21411_x5561_x598469354}

[[告警下限，当采样值小于等于该值时引发下限告警，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x1192162122}[节点]{style="font-family:宋体"}[hh3cRmonExtAlarmFallingThreshold]{lang="EN-US"}

[[associated with event]{lang="EN-US"}]{#struct_0_21411_x5561_x588734537}

[[告警对应的事件索引，上限事件索引对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x1777920139}[节点]{style="font-family:宋体"}[hh3cRmonExtAlarmRisingEvtIndex]{lang="EN-US"}[，下限事件索引对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}[节点]{style="font-family:宋体"}[hh3cRmonExtAlarmFallingEvtIndex]{lang="EN-US"}

[[Alarm sent upon entry startup]{lang="EN-US"}]{#struct_0_21411_x5561_1995390610}

[[初次触发告警类型：]{style="font-family:宋体"}]{#struct_0_21411_x5561_x598403818}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[risingAlarm]{lang="EN-US"}]{#struct_0_21411_x5561_1857079380}[：表示触发上限告警]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[fallingAlarm]{lang="EN-US"}]{#struct_0_21411_x5561_1473467718}[：表示触发下限告警]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[risingorFallingAlarm]{lang="EN-US"}]{#struct_0_21411_x5561_x515146871}[：表示触发上限或下限告警]{lang="EN-US" style="font-family:
  宋体"}

[[缺省情况下，触发]{style="font-family:宋体"}[risingorFallingAlarm]{lang="EN-US"}]{#struct_0_21411_x5561_1224981324}[类型告警，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}[节点]{style="font-family:宋体"}[hh3cRmonExtAlarmStartupAlarm]{lang="EN-US"}

[[Entry lifetime]{lang="EN-US"}]{#struct_0_21411_x5561_x598076138}

[[该扩展告警表项的存活时间，可以是永远存在，也可以是在规定的时间内存在，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x863498631}[节点]{style="font-family:宋体"}[hh3cRmonExtAlarmStatType]{lang="EN-US"}[与]{style="font-family:宋体"}[hh3cRmonExtAlarmStatCycle]{lang="EN-US"}[。]{style="font-family:宋体"}

[[Latest value]{lang="EN-US"}]{#struct_0_21411_x5561_204635245}

[[最近一次采样值，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x714519177}[节点]{style="font-family:宋体"}[hh3cRmonExtAlarmValue]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RMON命令.files/image001.png){#图片 3 width="62" height="25"}]{lang="EN-US"}]{#struct_0_21411_x5561_615776959}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[]{#struct_0_21411_x5561_x598010602}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:KaiTi_GB2312"}1-5]{lang="EN-US"}](?-858458789#_Ref331682763)[中，对于不同的]{style="font-family:KaiTi_GB2312"}[OEM]{lang="EN-US"}[产商，]{style="font-family:KaiTi_GB2312"}[MIB]{lang="EN-US"}[节点前缀不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x1229314752}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rmon prialarm]{lang="EN-US"}**]{#struct_0_21411_x5561_x750729830}

::: {#1991887181 .myid}
[]{#_Toc404796928}[]{#struct_0_21411_x5561_x55500059}[]{#_Toc331497860}[]{#_Toc291754548}[]{#_Toc221783230}[]{#_Toc136860130}[]{#_Toc99533463}

**RMON \-- RMON配置命令 \-- display rmon statistics**

------------------------------------------------------------------------

[**[display rmon statistics]{lang="EN-US"}**]{#struct_0_21411_x5561_x558960227}[命令用来显示]{style="font-family:宋体"}[RMON]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21411_x5561_730591983}

[**[display rmon statistics]{lang="EN-US"}**[ \[ *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_21411_x5561_1972053187}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21411_x5561_1232841114}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21411_x5561_202088311}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x598207210}

[[network-admin]{lang="EN-US"}]{#struct_0_21411_x5561_x2024498658}

[[network-operator]{lang="EN-US"}]{#struct_0_21411_x5561_x2076809132}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21411_x5561_1140533817}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21411_x5561_x1285108071}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x1616562033}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_21411_x5561_x879941228}[：指定接口类型和接口编号。如果未指定本参数，则显示所有接口下配置的统计表及统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21411_x5561_238784071}

[[本命令显示的是从端口创建统计表项到执行显示命令这段时间内端口的统计信息。设备重启时，会清除该统计信息。]{style="font-family:宋体"}]{#struct_0_21411_x5561_x236557846}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x598141674}

[[\# ]{lang="EN-US"}]{#struct_0_21411_x5561_351908099}[显示以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[RMON]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display rmon statistics gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_21411_x5561_1618934955}

[EtherStatsEntry 1 owned by user1 is VALID.]{lang="EN-US"}

[  Interface : GigabitEthernet1/0/1\<ifIndex.3\>]{lang="EN-US"}

[  etherStatsOctets         : 43393306  , etherStatsPkts          : 619825]{lang="EN-US"}

[  etherStatsBroadcastPkts  : 503581    , etherStatsMulticastPkts : 44013]{lang="EN-US"}

[  etherStatsUndersizePkts  : 0         , etherStatsOversizePkts  : 0]{lang="EN-US"}

[  etherStatsFragments      : 0         , etherStatsJabbers       : 0]{lang="EN-US"}

[  etherStatsCRCAlignErrors : 0         , etherStatsCollisions    : 0]{lang="EN-US"}

[  etherStatsDropEvents (insufficient resources): 0]{lang="EN-US"}

[  Incoming packets by size:]{lang="EN-US"}

[  64     : 0         ,  65-127  : 0         ,  128-255  : 0]{lang="EN-US"}

[  256-511: 0         ,  512-1023: 0         ,  1024-1518: 0]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display rmon statistics]{lang="EN-US"}]{#struct_0_21411_x5561_x661989780}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x43856592}[[字段]{style="font-family:黑体"}]{#struct_0_21411_x5561_x1408568973}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_21411_x5561_x597813994}

[[EtherStatsEntry *entry*-*number* owned by *owner* is *status*.]{lang="EN-US"}]{#struct_0_21411_x5561_x302790432}

[*[Owner]{lang="EN-US"}*]{#struct_0_21411_x5561_x1416564344}[创建的统计信息表项]{style="font-family:宋体"}*[entry]{lang="EN-US"}*[-*number*]{lang="EN-US"}[的当前状态为]{style="font-family:宋体"}*[status]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[entry-number]{lang="EN-US"}*]{#struct_0_21411_x5561_1960730312}[：统计信息表项，对应]{lang="EN-US" style="font-family:
  宋体"}[MIB]{lang="EN-US"}[节点]{lang="EN-US" style="font-family:宋体"}[etherStatsIndex]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[owner]{lang="EN-US"}*]{#struct_0_21411_x5561_855790444}[：该表项创建者，对应]{lang="EN-US" style="font-family:宋体"}[MIB]{lang="EN-US"}[节点]{lang="EN-US" style="font-family:宋体"}[etherStatsOwner]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[status]{lang="EN-US"}*]{#struct_0_21411_x5561_x1807454888}[：与该索引对应的统计表项的状态（]{lang="EN-US" style="font-family:宋体"}[VALID]{lang="EN-US"}[表示有效，]{lang="EN-US" style="font-family:宋体"}[UNDERCREATION]{lang="EN-US"}[表示无效。处于无效状态的表项使用]{lang="EN-US" style="font-family:宋体"}**[display rmon statistics]{lang="EN-US"}**[命令可以查看到，但使用]{lang="EN-US" style="font-family:宋体"}**[display current-configuration]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[display this]{lang="EN-US"}**[看不到对应的]{lang="EN-US" style="font-family:宋体"}**[rmon statistics]{lang="EN-US"}**[配置]{lang="EN-US" style="font-family:
  宋体"}[命令）。命令行配置]{lang="EN-US" style="font-family:宋体"}[statistics]{lang="EN-US"}[表项时不可配且默认为]{lang="EN-US" style="font-family:宋体"}[VALID]{lang="EN-US"}[，对应]{lang="EN-US" style="font-family:宋体"}[MIB]{lang="EN-US"}[节点]{lang="EN-US" style="font-family:宋体"}[etherStatsStatus]{lang="EN-US"}

[[Interface]{lang="EN-US"}]{#struct_0_21411_x5561_x597748458}

[[被统计端口，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x1002929806}[节点]{style="font-family:宋体"}[etherStatsDataSource]{lang="EN-US"}

[[etherStatsOctets]{lang="EN-US"}]{#struct_0_21411_x5561_1977710377}

[[统计时间内，端口收到的所有报文的字节数，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x934071123}[节点]{style="font-family:宋体"}[etherStatsOctets]{lang="EN-US"}

[[etherStatsPkts]{lang="EN-US"}]{#struct_0_21411_x5561_906784022}

[[统计时间内，端口收到的所有报文的包数，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x199200162}[节点]{style="font-family:宋体"}[etherStatsPkts]{lang="EN-US"}

[[etherStatsBroadcastPkts]{lang="EN-US"}]{#struct_0_21411_x5561_x598338285}

[[统计时间内，端口收到的所有广播包的数量，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x817004285}[节点]{style="font-family:宋体"}[etherStatsBroadcastPkts]{lang="EN-US"}

[[etherStatsMulticastPkts]{lang="EN-US"}]{#struct_0_21411_x5561_489792541}

[[统计时间内，端口收到的所有组播包的数量，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x68575183}[节点]{style="font-family:宋体"}[etherStatsMulticastPkts]{lang="EN-US"}

[[etherStatsUndersizePkts]{lang="EN-US"}]{#struct_0_21411_x5561_x187647580}

[[统计时间内，端口收到的所有过小包的数量，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x598272749}[节点]{style="font-family:宋体"}[etherStatsUndersizePkts]{lang="EN-US"}

[[etherStatsOversizePkts]{lang="EN-US"}]{#struct_0_21411_x5561_x41206712}

[[统计时间内，端口收到的所有超大包的数量，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_1514554966}[节点]{style="font-family:宋体"}[etherStatsOversizePkts]{lang="EN-US"}

[[etherStatsFragments]{lang="EN-US"}]{#struct_0_21411_x5561_x358557973}

[[统计时间内，端口收到的所有过小且校验错误包的数量，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x1104428496}[节点]{style="font-family:宋体"}[etherStatsFragments]{lang="EN-US"}

[[etherStatsJabbers]{lang="EN-US"}]{#struct_0_21411_x5561_x598469357}

[[统计时间内，端口收到的所有超大且校验错误包的数量，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x1191965514}[节点]{style="font-family:宋体"}[etherStatsJabbers]{lang="EN-US"}

[[etherStatsCRCAlignErrors]{lang="EN-US"}]{#struct_0_21411_x5561_1493797130}

[[统计时间内，端口收到的所有校验错误包的数量，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_154979562}[节点]{style="font-family:宋体"}[etherStatsCRCAlignErrors]{lang="EN-US"}

[[etherStatsCollisions]{lang="EN-US"}]{#struct_0_21411_x5561_578413985}

[[统计时间内，端口收到的所有冲突包的数量，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x598403821}[节点]{style="font-family:宋体"}[etherStatsCollisions]{lang="EN-US"}

[[etherStatsDropEvents]{lang="EN-US"}]{#struct_0_21411_x5561_1856620629}

[[统计时间内，端口收到的所有丢包事件的数量，对应]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_21411_x5561_x1659165491}[节点]{style="font-family:宋体"}[etherStatsDropEvents]{lang="EN-US"}

[[Incoming packets by size:]{lang="EN-US"}]{#struct_0_21411_x5561_x2078302642}

[[64:]{lang="EN-US"}]{#struct_0_21411_x5561_x598076141}

[[65-127:]{lang="EN-US"}]{#struct_0_21411_x5561_x863039886}

[[128-255:]{lang="EN-US"}]{#struct_0_21411_x5561_1000271899}

[[ 256-511:]{lang="EN-US"}]{#struct_0_21411_x5561_639670462}

[[ 512-1023:]{lang="EN-US"}]{#struct_0_21411_x5561_x598010605}

[[1024-1518:]{lang="EN-US"}]{#struct_0_21411_x5561_x1229773504}

[[统计时间内，根据包的长度对接收到的包分区间进行统计。其中：]{style="font-family:宋体"}]{#struct_0_21411_x5561_x607913468}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[64]{lang="EN-US"}]{#struct_0_21411_x5561_1413578025}[字段的信息，对应]{lang="EN-US" style="font-family:宋体"}[MIB]{lang="EN-US"}[节点]{lang="EN-US" style="font-family:宋体"}[etherStatsPkts64Octets]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[65-127]{lang="EN-US"}]{#struct_0_21411_x5561_x598207213}[字段的信息，对应]{lang="EN-US" style="font-family:宋体"}[MIB]{lang="EN-US"}[节点]{lang="EN-US" style="font-family:宋体"}[etherStatsPkts65to127Octets]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[128-255]{lang="EN-US"}]{#struct_0_21411_x5561_x2024564194}[字段的信息，对应]{lang="EN-US" style="font-family:宋体"}[MIB]{lang="EN-US"}[节点]{lang="EN-US" style="font-family:宋体"}[etherStatsPkts128to255Octets]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[256-511]{lang="EN-US"}]{#struct_0_21411_x5561_2145377308}[字段的信息，对应]{lang="EN-US" style="font-family:宋体"}[MIB]{lang="EN-US"}[节点]{lang="EN-US" style="font-family:宋体"}[etherStatsPkts256to511Octets]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[512-1023]{lang="EN-US"}]{#struct_0_21411_x5561_1568665515}[字段的信息，对应]{lang="EN-US" style="font-family:宋体"}[MIB]{lang="EN-US"}[节点]{lang="EN-US" style="font-family:宋体"}[etherStatsPkts512to1023Octets]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1024-1518]{lang="EN-US"}]{#struct_0_21411_x5561_x598141677}[字段的信息，对应]{lang="EN-US" style="font-family:宋体"}[MIB]{lang="EN-US"}[节点]{lang="EN-US" style="font-family:宋体"}[etherStatsPkts1024to1518Octets]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21411_x5561_351842563}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rmon statistics]{lang="EN-US"}**]{#struct_0_21411_x5561_115563254}

::: {#-1846527836 .myid}
[]{#_Toc404796929}[]{#struct_0_21411_x5561_x1434109035}[]{#_Toc331497861}[]{#_Toc308096722}

**RMON \-- RMON配置命令 \-- rmon alarm**

------------------------------------------------------------------------

[**[rmon alarm]{lang="EN-US"}**]{#struct_0_21411_x5561_x689890864}[命令用来创建告警表项。]{style="font-family:宋体"}

[**[undo rmon alarm]{lang="EN-US"}**]{#struct_0_21411_x5561_982861163}[命令用来在告警表中删除指定表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x1638677026}

[**[rmon alarm]{lang="EN-US"}**[ *entry-number alarm-variable sampling-interval* { **absolute** \| **delta** } ]{lang="EN-US"}]{#struct_0_21411_x5561_x750616660}[\[ **startup-alarm** { **falling** \| **rising** \| **rising-falling** } \]]{lang="EN-US"}[ **rising-threshold** *threshold-value1 event-entry1* **falling-threshold** *threshold-value2 event-entry2* \[ **owner** *text* \]]{lang="EN-US"}

[**[undo rmon alarm ]{lang="EN-US"}***[entry-number]{lang="EN-US"}*]{#struct_0_21411_x5561_x790939862}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x597813997}

[[告警表中没有任何表项。]{style="font-family:宋体"}]{#struct_0_21411_x5561_x302724896}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21411_x5561_161334266}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21411_x5561_607132691}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21411_x5561_308466304}

[[network-admin]{lang="EN-US"}]{#struct_0_21411_x5561_x200672613}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21411_x5561_1290799213}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x316850470}

[*[entry]{lang="EN-US"}*[-*number*]{lang="EN-US"}]{#struct_0_21411_x5561_1976292126}[：告警表项的索引号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[alarm]{lang="EN-US"}*[-*variable*]{lang="EN-US"}]{#struct_0_21411_x5561_x597748461}[：告警变量，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，可以是节点]{style="font-family:宋体"}[OID]{lang="EN-US"}[的点分格式（格式为]{style="font-family:宋体"}*[entry.integer.instance]{lang="EN-US"}*[或者*叶子节点名*]{style="font-family:宋体"}*[.instance]{lang="EN-US"}[，]{style="font-family:宋体"}*[如]{style="font-family:宋体"}[1.3.6.1.2.1.2.1.10.1]{lang="EN-US"}[），也可以是节点名（如]{style="font-family:宋体"}[ifInOctets.1]{lang="EN-US"}[）。只有可以解析为]{style="font-family:宋体"}[ASN.1]{lang="EN-US"}[中]{style="font-family:宋体"}[INTEGER]{lang="EN-US"}[（]{style="font-family:宋体"}[INTEGER,INTEGER32,Unsigned32, Counter32,Counter64,Gauge, or TimeTicks]{lang="EN-US"}[）的数据类型的变量能作为告警变量，比如]{style="font-family:宋体"}[etherStatsEntry]{lang="EN-US"}[表项的叶子节点（]{style="font-family:宋体"}[etherStatsOctets]{lang="EN-US"}[、]{style="font-family:宋体"}[etherStatsPkts]{lang="EN-US"}[和]{style="font-family:宋体"}[etherStatsBroadcastPkts]{lang="EN-US"}[等）的实例，]{style="font-family:宋体"}[ifEntry]{lang="EN-US"}[表项的叶子节点（]{style="font-family:宋体"}[ifInOctets]{lang="EN-US"}[、]{style="font-family:宋体"}[ifInUcastPkts]{lang="EN-US"}[和]{style="font-family:宋体"}[ifInNUcastPkts]{lang="EN-US"}[等）的实例。]{style="font-family:宋体"}

[*[sampling]{lang="EN-US"}*[-*interval*]{lang="EN-US"}]{#struct_0_21411_x5561_x1002339983}[：采样间隔时间，取值范围为]{style="font-family:宋体"}[[5]{lang="EN-US" style="color:windowtext;text-decoration:none"}[～]{style="font-family:宋体;color:windowtext;text-decoration:none"}[65535]{lang="EN-US" style="color:windowtext;text-decoration:none"}](#采样间隔时间取值范围)[，单位为秒。]{style="font-family:宋体"}[]{#_Hlt20797756}

[**[absolute]{lang="EN-US"}**]{#struct_0_21411_x5561_x1153557890}[：]{style="font-family:宋体"}[采样类型为绝对值采样，即采样时间到达时直接提取变量的值。]{style="font-family:宋体"}

[**[delta]{lang="EN-US"}**]{#struct_0_21411_x5561_472406561}[：采样类型为变化值采样，即采样时间到达时提取的是变量在采样间隔内的变化值。]{style="font-family:宋体"}

[**[startup-alarm]{lang="EN-US"}**]{#struct_0_21411_x5561_x160710390}[：表示初次采样时，如果达到或超出阈值，触发的告警类型。如果未指定本参数，触发]{style="font-family:宋体"}**[rising-falling]{lang="EN-US"}**[类型告警。]{style="font-family:宋体"}

[**[rising]{lang="EN-US"}**]{#struct_0_21411_x5561_347742576}[：表示只触发上限告警。]{style="font-family:宋体"}

[**[falling]{lang="EN-US"}**]{#struct_0_21411_x5561_1611959004}[：表示只触发下限告警。]{style="font-family:宋体"}

[**[rising-falling]{lang="EN-US"}**]{#struct_0_21411_x5561_x1251462086}[：表示触发上限或下限告警。]{style="font-family:宋体"}

[**[rising-threshold]{lang="EN-US"}**[ *threshold*-*value1* *event*-*entry1*]{lang="EN-US"}]{#struct_0_21411_x5561_x1264822839}[：设置上限参数，]{style="font-family:宋体"}*[threshold]{lang="EN-US"}*[-*value1*]{lang="EN-US"}[表示上限阈值，取值范围为]{style="font-family:宋体"}[-2147483648]{lang="EN-US"}[～]{style="font-family:宋体"}[+2147483647]{lang="EN-US"}[；]{style="font-family:宋体"}*[event]{lang="EN-US"}*[-*entry1*]{lang="EN-US"}[表示上限阈值相应的事件索引号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[（]{style="font-family:宋体"}[0]{lang="EN-US"}[表示没有对应的事件，告警被触发后不会采取任何事件动作）。]{style="font-family:
宋体"}

[**[falling-threshold]{lang="EN-US"}**[ *threshold*-*value2* *event*-*entry2*]{lang="EN-US"}]{#struct_0_21411_x5561_x598338284}[：设置下限参数，]{style="font-family:宋体"}*[threshold]{lang="EN-US"}*[-*value2*]{lang="EN-US"}[表示下限阈值，取值范围为]{style="font-family:宋体"}[-2147483648]{lang="EN-US"}[～]{style="font-family:宋体"}[+2147483647]{lang="EN-US"}[；]{style="font-family:宋体"}*[event]{lang="EN-US"}*[-*entry2*]{lang="EN-US"}[表示下限阈值相应的事件索引号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[（]{style="font-family:宋体"}[0]{lang="EN-US"}[表示没有对应的事件，告警被触发后不会采取任何事件动作）。]{style="font-family:
宋体"}

[**[owner]{lang="EN-US"}***[ text]{lang="EN-US"}*]{#struct_0_21411_x5561_x816938749}[：该表项的创建者，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21411_x5561_1606842326}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令用来设置告警项，以便在出现异常时触发告警事件，再由告警事件来定义具体的处理方式。]{style="font-family:宋体"}]{#struct_0_21411_x5561_1396914605}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户定义了告警表项后，系统会按照定义的时间周期去获取被监视的告警变量的值，并将该值和设定的阈值进行比较，去执行相应的处理过程。]{style="font-family:宋体"}]{#struct_0_21411_x5561_x1360451086}[当采样值大于等于设定的上限]{lang="EN-US" style="font-family:宋体"}*[threshold-value1]{lang="EN-US"}*[，触发事件表中定义的事件]{lang="EN-US" style="font-family:宋体"}*[event-entry1]{lang="EN-US"}*[；采样值小于等于设定的下限]{lang="EN-US" style="font-family:宋体"}*[threshold-value2]{lang="EN-US"}*[，触发事件表中定义的事件]{lang="EN-US" style="font-family:宋体"}*[event-entry2]{lang="EN-US"}*[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在添加告警表项之前，需要通过]{style="font-family:宋体"}]{#struct_0_21411_x5561_398475070}**[rmon event]{lang="EN-US"}**[命令定义好告警表项中引用的事件。否则，虽然会创建告警表项，但是不能触发告警事件。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在新建表项时，指定的告警变量（]{lang="EN-US" style="font-family:宋体"}*[alarm-variable]{lang="EN-US"}*]{#struct_0_21411_x5561_1248358163}[）、采样间隔（]{lang="EN-US" style="font-family:
宋体"}*[sampling-interval]{lang="EN-US"}*[）、采样类型（]{lang="EN-US" style="font-family:宋体"}**[absolute]{lang="EN-US"}**[或]{lang="EN-US" style="font-family:宋体"}**[delta]{lang="EN-US"}**[）、上限阈值（]{lang="EN-US" style="font-family:宋体"}*[threshold-value1]{lang="EN-US"}*[）和下限阈值（]{lang="EN-US" style="font-family:宋体"}*[threshold-value2]{lang="EN-US"}*[）五项参数的值和已经存在的告警表项对应的五项参数值完全相同时，系统将认为这两个表项的配置相同，创建操作失败。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户最多可以定义]{style="font-family:宋体"}]{#struct_0_21411_x5561_x1462245169}[60]{lang="EN-US"}[个告警表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21411_x5561_324282750}

[[\# ]{lang="EN-US"}]{#struct_0_21411_x5561_x598272748}[在告警表中添加表项]{style="font-family:宋体"}[1]{lang="EN-US"}[，对节点]{style="font-family:宋体"}[1.3.6.1.2.1.16.1.1.1.4.1]{lang="EN-US"}[以]{style="font-family:宋体"}[10]{lang="EN-US"}[秒的采样间隔进行绝对值采样，当采样值大于等于]{style="font-family:宋体"}[5000]{lang="EN-US"}[的上限阈值触发事件]{style="font-family:宋体"}[1]{lang="EN-US"}[，小于等于下限阈值]{style="font-family:宋体"}[5]{lang="EN-US"}[时触发事件]{style="font-family:宋体"}[2]{lang="EN-US"}[，创建者为]{style="font-family:宋体"}[user1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21411_x5561_x41141176}

[\[Sysname\] rmon event 1 log]{lang="EN-US"}

[\[Sysname\] rmon event 2 none]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] rmon statistics 1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] quit]{lang="EN-US"}

[\[Sysname\] rmon alarm 1 1.3.6.1.2.1.16.1.1.1.4.1 10 absolute rising-threshold 5000 1 falling-threshold 5 2 owner user1]{lang="EN-US"}

[[1.3.6.1.2.1.16.1.1.1.4]{lang="EN-US"}]{#struct_0_21411_x5561_101146120}[是叶子节点]{style="font-family:宋体"}[etherStatsOctets]{lang="EN-US"}[的]{style="font-family:宋体"}[OID]{lang="EN-US"}[，它表示接口收到报文的统计值（以字节为单位）。以上步骤中也可以使用]{style="font-family:宋体"}[etherStatsOctets.1]{lang="EN-US"}[来代替]{style="font-family:宋体"}[1.3.6.1.2.1.16.1.1.1.4.1]{lang="EN-US"}[参数，]{style="font-family:宋体"}[.1]{lang="EN-US"}[与接口统计表项的编号一致，如果创建的是"]{style="font-family:宋体"}[rmon statistics 5]{lang="EN-US"}["，则对应需要使用]{style="font-family:宋体"}[etherStatsOctets.5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[以上配置步骤实现：对接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}]{#struct_0_21411_x5561_x820146170}[的使用情况进行统计、监控，每]{style="font-family:宋体"}[10]{lang="EN-US"}[秒钟对接口收到报文的总字节数取绝对值，如果接口收到报文的总字节数达到或超过]{style="font-family:宋体"}[5000]{lang="EN-US"}[字节时，就记录日志；当接口收到报文的总字节数小于或等于]{style="font-family:宋体"}[5]{lang="EN-US"}[字节时，不采取任何措施。]{style="font-family:宋体"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21411_x5561_836966298}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display rmon alarm]{lang="EN-US"}**]{#struct_0_21411_x5561_795170385}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rmon event]{lang="EN-US"}**]{#struct_0_21411_x5561_140618994}
:::

::: {#445761214 .myid}
[]{#_Toc404796930}[]{#struct_0_21411_x5561_x448578238}[]{#_Toc331497862}[]{#_Toc308096721}

**RMON \-- RMON配置命令 \-- rmon event**

------------------------------------------------------------------------

[**[rmon event]{lang="EN-US"}**]{#struct_0_21411_x5561_x598469356}[命令用来创建事件表项。]{style="font-family:宋体"}

[**[undo rmon event]{lang="EN-US"}**]{#struct_0_21411_x5561_x1192031050}[命令用来在事件表中删除指定表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x2082622117}

[**[rmon]{lang="EN-US"}**[ **event** *entry*-*number* \[ **description** *string* \] { **log** \| **log-trap** *security-string \|* **none** \| **trap** *security-string* } \[ **owner** *text* \]]{lang="EN-US"}]{#struct_0_21411_x5561_1962934933}

[**[undo rmon event ]{lang="EN-US"}***[entry]{lang="EN-US"}*[-*number*]{lang="EN-US"}]{#struct_0_21411_x5561_x1992874736}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x196719930}

[[事件表中没有任何表项。]{style="font-family:宋体"}]{#struct_0_21411_x5561_1624116440}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x1120580978}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21411_x5561_x1553841855}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x598403820}

[[network-admin]{lang="EN-US"}]{#struct_0_21411_x5561_1856555093}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21411_x5561_731045232}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21411_x5561_1202848131}

[*[entry]{lang="EN-US"}*[-*number*]{lang="EN-US"}]{#struct_0_21411_x5561_x2029205573}[：事件表项的索引号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**[ *string*]{lang="EN-US"}]{#struct_0_21411_x5561_x1227156592}[：事件的描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[log]{lang="EN-US"}**]{#struct_0_21411_x5561_x458971794}[：日志事件。当该事件被触发时，系统会记录日志。]{style="font-family:宋体"}

[**[log-trap]{lang="EN-US"}**]{#struct_0_21411_x5561_x224887204}[：日志和告警事件。当该事件被触发时，系统会同时记录日志和生成告警信息，生成的告警信息将发送到设备的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[模块。通过设置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[中告警信息的发送参数，来决定告警信息输出的相关属性。有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"]{style="font-family:宋体"}[SNMP]{lang="EN-US"}["。]{style="font-family:宋体"}

[*[security]{lang="EN-US"}[-string]{lang="EN-US"}*]{#struct_0_21411_x5561_731745601}[：表示接收告警信息的网管站的团体名，此处支持配置，但配置不生效。为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_21411_x5561_x598076140}[：不产生动作的事件。当该事件被触发时，系统不做处理。]{style="font-family:宋体"}

[**[trap]{lang="FR"}**]{#struct_0_21411_x5561_x862974350}[：告警]{style="font-family:宋体"}[事件。当该事件被触发时，生成告警信息，生成的告警信息将发送到设备的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[模块。通过设置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[中告警信息的发送参数，来决定告警信息输出的相关属性。有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"]{style="font-family:宋体"}[SNMP]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[owner]{lang="EN-US"}***[ text]{lang="EN-US"}*]{#struct_0_21411_x5561_117896210}[：该表项的创建者，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21411_x5561_302193942}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RMON]{lang="EN-US"}]{#struct_0_21411_x5561_x2023603284}[的事件管理定义事件索引号及事件的处理方式包括：记录日志、生成告警信息发送给设备的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[模块、记录日志的同时生成告警信息发送给设备的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[模块或者既不记录日志也生成告警信息发送给设备的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[模块。这样系统就可以对告警表中定义的告警事件进行相应的处理。事件组中定义的事件索引号对应告警组中指定事件索引号。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户最多可以定义]{style="font-family:宋体"}]{#struct_0_21411_x5561_1496763336}[60]{lang="EN-US"}[个事件表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x1630340482}

[[\# ]{lang="EN-US"}]{#struct_0_21411_x5561_352845955}[在事件表中添加索引号为]{style="font-family:宋体"}[10]{lang="EN-US"}[、类型为日志的事件，创建者为]{style="font-family:宋体"}[user1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21411_x5561_x598010604}

[\[Sysname\] rmon event 10 log owner user1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x1229707968}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display rmon event]{lang="EN-US"}**]{#struct_0_21411_x5561_x381922673}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rmon alarm]{lang="EN-US"}**]{#struct_0_21411_x5561_890723348}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rmon prialarm]{lang="EN-US"}**]{#struct_0_21411_x5561_2134296866}
:::

::: {#1774411930 .myid}
[]{#_Toc404796931}[]{#struct_0_21411_x5561_x1913446628}[]{#_Toc331497863}[]{#_Toc308096723}

**RMON \-- RMON配置命令 \-- rmon history**

------------------------------------------------------------------------

[**[rmon history]{lang="EN-US"}**]{#struct_0_21411_x5561_1092900575}[命令用来创建历史控制表项。]{style="font-family:宋体"}

[**[undo rmon history]{lang="EN-US"}**]{#struct_0_21411_x5561_859723657}[命令用来在历史表中删除指定表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x1831642194}

[**[rmon history]{lang="EN-US"}**[ *entry*-*number* **buckets** *number* **interval** *sampling*-*interval* \[ **owner** *text* \]]{lang="EN-US"}]{#struct_0_21411_x5561_x598207212}

[**[undo rmon history]{lang="EN-US"}**[ *entry*-*number*]{lang="EN-US"}]{#struct_0_21411_x5561_x2024629730}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21411_x5561_1147899554}

[[历史控制表中没有任何表项。]{style="font-family:宋体"}]{#struct_0_21411_x5561_225860676}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x847356622}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_21411_x5561_630084941}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21411_x5561_1427972321}

[[network-admin]{lang="EN-US"}]{#struct_0_21411_x5561_x1081730067}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21411_x5561_x1127659462}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x598141676}

[*[entry]{lang="EN-US"}*[-*number*]{lang="EN-US"}]{#struct_0_21411_x5561_351777027}[：历史控制表项的索引号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[buckets]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_21411_x5561_1475935434}[：该历史控制表项对应的历史表容量，即历史表最多可容纳的记录数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，但实际配置如果超过]{style="font-family:宋体"}[50]{lang="EN-US"}[时，会提示取]{style="font-family:宋体"}[50]{lang="EN-US"}[最大配置值。]{style="font-family:宋体"}

[**[interval]{lang="EN-US"}**[ *sampling*-*interval*]{lang="EN-US"}]{#struct_0_21411_x5561_1300402608}[：统计周期，取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[owner]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_21411_x5561_1086667312}[：该表项的创建者，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21411_x5561_822007040}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[创建历史控制表项后，系统会按周期统计当前端口收发报文的情况，并将统计值作为一个实例保存在]{style="font-family:宋体"}]{#struct_0_21411_x5561_x1740485271}[etherHistoryEntry]{lang="EN-US"}[表的叶子节点下。可保存的统计值个数由]{style="font-family:宋体"}**[buckets]{lang="EN-US"}**[ *number*]{lang="EN-US"}[参数决定，当历史表的容量达到最大值时，系统会删除最早的记录来保存新的统计值。统计信息包括端口一个周期内收到的报文总数、广播报文总数和组播报文总数等。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在添加控制历史表项的过程中，如果指定的历史表容量超出了设备实际支持的历史表容量时，新的历史表项会被添加，但该表项对应生效的历史表容量为设备实际支持的历史表容量，可以使用]{style="font-family:宋体"}]{#struct_0_21411_x5561_1193084721}**[display rmon history]{lang="EN-US"}**[命令来查看配置结果。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在创建历史控制表项时，指定的采样间隔（]{style="font-family:宋体"}]{#struct_0_21411_x5561_211823387}**[interval ]{lang="EN-US"}***[sampling-interval]{lang="EN-US"}*[）参数的值和该接口下已经存在的历史控制表项对应的该项参数值相同时，系统将认为这两个表项的配置相同，创建操作失败。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户最多可以定义]{style="font-family:宋体"}]{#struct_0_21411_x5561_x413164916}[100]{lang="EN-US"}[个历史控制表项。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RMON]{lang="EN-US"}]{#struct_0_21411_x5561_x1803925702}[统计功能只能在二]{style="font-family:宋体"}[/]{lang="EN-US"}[三层以太网接口下进行配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x597813996}

[[\# ]{lang="EN-US"}]{#struct_0_21411_x5561_x302659360}[创建索引号为]{style="font-family:宋体"}[1]{lang="EN-US"}[，表容量为]{style="font-family:宋体"}[10]{lang="EN-US"}[，采样时间为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒的历史控制表项，创建者为]{style="font-family:宋体"}[user1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21411_x5561_883231513}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] rmon history 1 buckets 10 interval 5 owner user1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x1471092741}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display rmon history]{lang="EN-US"}**]{#struct_0_21411_x5561_x569207126}
:::

::: {#-881943679 .myid}
[]{#_Toc404796932}[]{#struct_0_21411_x5561_x118992676}[]{#_Toc331497864}[]{#_Toc308096724}

**RMON \-- RMON配置命令 \-- rmon prialarm**

------------------------------------------------------------------------

[**[rmon ]{lang="EN-US"}***[prialarm]{lang="EN-US"}*]{#struct_0_21411_x5561_x382932537}[命令用来创建扩展告警表项。]{style="font-family:宋体"}

[**[undo rmon ]{lang="EN-US"}***[prialarm]{lang="EN-US"}*]{#struct_0_21411_x5561_x1970643944}[命令用来在扩展告警表中删除指定表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x597748460}

[**[rmon prialarm]{lang="EN-US"}**[ *entry-number prialarm-formula prialarm-des sampling-interval* { **absolute** \| **delta** } \[ **startup-alarm** { **falling** \| **rising** \| **rising-falling** } \] **rising-threshold** *threshold-value1 event-entry1* **falling-threshold** *threshold-value2 event-entry2* **entrytype** { **forever** \| **cycle** *cycle-period* } \[ **owner** *text* \]]{lang="EN-US"}]{#struct_0_21411_x5561_x1002405519}

[**[undo rmon prialarm ]{lang="EN-US"}***[entry-number]{lang="EN-US"}*]{#struct_0_21411_x5561_1934413353}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21411_x5561_1689749805}

[[扩展告警表中没有任何表项。]{style="font-family:宋体"}]{#struct_0_21411_x5561_x913094957}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21411_x5561_573219872}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21411_x5561_x1864455983}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21411_x5561_498180563}

[[network-admin]{lang="EN-US"}]{#struct_0_21411_x5561_x836196339}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21411_x5561_1780933850}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21411_x5561_1396834738}

[*[entry]{lang="EN-US"}*[-*number*]{lang="EN-US"}]{#struct_0_21411_x5561_974727698}[：扩展告警表项的索引号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[prialarm-fromula]{lang="EN-US"}*]{#struct_0_21411_x5561_x181754363}[：对告警变量进行计算的告警公式，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串。公式中的告警变量必须以]{style="font-family:宋体"}[OID]{lang="EN-US"}[来表示，]{style="font-family:宋体"}[OID]{lang="EN-US"}[表达式必须以小数点开始，例如]{style="font-family:宋体"}[(.1.3.6.1.2.1.2.1.10.1)\*8]{lang="EN-US"}[；运算公式由用户定义，可以使用加减乘除四种运算方法对告警变量进行运算，该运算公式的结果取值为长整型数，但不支持负数的输入。用户在编写公式的时候需要注意，公式中每一步的运算结果都不能超过长整型的表达范围，否则可能会得出错误的结果。]{style="font-family:宋体"}

[*[prialarm-des]{lang="EN-US"}*]{#struct_0_21411_x5561_x1357637769}[：对该告警的描述，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[*[sampling]{lang="EN-US"}*[-*interval*]{lang="EN-US"}]{#struct_0_21411_x5561_x1883756257}[：采样间隔时间，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[absolute]{lang="EN-US"}**]{#struct_0_21411_x5561_989456500}[：采样类型为绝对值采样，即采样时间到达时直接提取变量的值。]{style="font-family:宋体"}

[**[delta]{lang="EN-US"}**]{#struct_0_21411_x5561_x364325885}[：采样类型为变化值采样，即采样时间到达时提取的是变量在采样间隔内的变化值。]{style="font-family:宋体"}**[startup-alarm]{lang="EN-US"}**[：表示初次采样时，如果达到或超出阈值，触发的告警类型。如果未指定本参数，触发]{style="font-family:宋体"}[rising-falling]{lang="EN-US"}[类型告警。]{style="font-family:宋体"}

[**[rising]{lang="EN-US"}**]{#struct_0_21411_x5561_x1983748110}[：表示只触发上限告警。]{style="font-family:宋体"}

[**[falling]{lang="EN-US"}**]{#struct_0_21411_x5561_1780868314}[：表示只触发下限告警。]{style="font-family:宋体"}

[**[rising-falling]{lang="EN-US"}**]{#struct_0_21411_x5561_x1343630958}[：表示触发上限或下限告警。]{style="font-family:宋体"}

[**[rising-threshold]{lang="EN-US"}**[ *threshold*-*value1* *event*-*entry1*]{lang="EN-US"}]{#struct_0_21411_x5561_1815363439}[：设置超上限参数，]{style="font-family:宋体"}*[threshold]{lang="EN-US"}*[-*value1*]{lang="EN-US"}[表示上限阈值，取值范围为]{style="font-family:宋体"}[-2147483648]{lang="EN-US"}[～]{style="font-family:宋体"}[+2147483647]{lang="EN-US"}[；]{style="font-family:宋体"}*[event]{lang="EN-US"}*[-*entry1*]{lang="EN-US"}[表示上限阈值相应的事件索引号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[（]{style="font-family:宋体"}[0]{lang="EN-US"}[表示没有对应的事件，告警被触发后不会采取任何事件动作）。]{style="font-family:
宋体"}

[**[falling-threshold]{lang="EN-US"}**[ *threshold*-*value2* *event*-*entry2*]{lang="EN-US"}]{#struct_0_21411_x5561_x564942982}[：设置下限参数，]{style="font-family:宋体"}*[threshold]{lang="EN-US"}*[-*value2*]{lang="EN-US"}[表示下限阈值，取值范围为]{style="font-family:宋体"}[-2147483648]{lang="EN-US"}[～]{style="font-family:宋体"}[+2147483647]{lang="EN-US"}[；]{style="font-family:宋体"}*[event]{lang="EN-US"}*[-*entry2*]{lang="EN-US"}[表示下限阈值相应的事件索引号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[（]{style="font-family:宋体"}[0]{lang="EN-US"}[表示没有对应的事件，告警被触发后不会采取任何事件动作）。]{style="font-family:
宋体"}

[**[forever]{lang="EN-US"}**]{#struct_0_21411_x5561_628493030}[：本告警实例存活类型为永久。]{style="font-family:宋体"}

[**[cycle ]{lang="EN-US"}***[cycle]{lang="EN-US"}*[-*period*]{lang="EN-US"}]{#struct_0_21411_x5561_66280084}[：本告警实例的存活时间，单位为秒，取值范围]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[owner]{lang="EN-US"}***[ text]{lang="EN-US"}*]{#struct_0_21411_x5561_x250230762}[：该表项的创建者，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21411_x5561_1245180385}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户定义了扩展告警表项后，系统先对定义的扩展告警公式中的告警变量按照定义的时间间隔进行采样，再将采样值按照定义的运算公式进行计算，最后将计算结果和和设定的阈值进行比较，并执行相应的处理过程。]{style="font-family:宋体"}]{#struct_0_21411_x5561_x1906687057}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在添加扩展告警表项之前，需要通过]{lang="EN-US" style="font-family:宋体"}**[rmon event]{lang="EN-US"}**]{#struct_0_21411_x5561_1780802778}[命令定义好扩展告警表项中引用的事件。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在新建表项时，指定的告警变量公式（]{lang="EN-US" style="font-family:宋体"}*[prialarm-formula]{lang="EN-US"}*]{#struct_0_21411_x5561_1400147258}[）、采样间隔（]{lang="EN-US" style="font-family:
宋体"}*[sampling-interval]{lang="EN-US"}*[）、采样类型（]{lang="EN-US" style="font-family:宋体"}**[absolute]{lang="EN-US"}**[或]{lang="EN-US" style="font-family:宋体"}**[delta]{lang="EN-US"}**[）、上限阈值（]{lang="EN-US" style="font-family:宋体"}*[threshold-value1]{lang="EN-US"}*[）和下限阈值（]{lang="EN-US" style="font-family:宋体"}*[threshold-value2]{lang="EN-US"}*[）五项参数的值和已经存在的扩展告警表项对应的五项参数值完全相同时，系统将认为这两个表项的配置相同，创建操作失败。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户最多可以定义]{style="font-family:宋体"}]{#struct_0_21411_x5561_x1608416863}[50]{lang="EN-US"}[个扩展告警表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21411_x5561_538335181}

[[\# ]{lang="EN-US"}]{#struct_0_21411_x5561_x384050387}[使用扩展告警对接口接收到的广播报文比率进行监控。]{style="font-family:宋体"}

[[在扩展告警表中添加索引号为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_21411_x5561_x144489474}[的表项，对相应告警变量以公式]{style="font-family:宋体"}[(.1.3.6.1.2.1.16.1.1.1.6.1\*100/.1.3.6.1.2.1.16.1.1.1.5.1)]{lang="EN-US"}[运算，对该公式中涉及的变量以]{style="font-family:宋体"}[10]{lang="EN-US"}[秒的采样间隔进行绝对值采样。上限告警值为]{style="font-family:宋体"}[80]{lang="EN-US"}[对应事件]{style="font-family:宋体"}[1]{lang="EN-US"}[（将事件记录在日志表中），下限告警值为]{style="font-family:宋体"}[5]{lang="EN-US"}[对应事件]{style="font-family:宋体"}[2]{lang="EN-US"}[（不需要采取措施），表项的存活时间为永远（]{style="font-family:宋体"}**[forever]{lang="EN-US"}**[），创建者为]{style="font-family:宋体"}*[user1]{lang="EN-US"}*[。（广播报文比率的计算公式为：接口接收到的广播报文总数]{style="font-family:宋体"}[/]{lang="EN-US"}[接口接收到的总报文数，该公式由用户自行定义）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21411_x5561_x1246549306}

[\[Sysname\] rmon event 1 log]{lang="EN-US"}

[\[Sysname\] rmon event 2 none]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] rmon statistics 1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] quit]{lang="EN-US"}

[\[Sysname\] rmon prialarm 1 (.1.3.6.1.2.1.16.1.1.1.6.1\*100/.1.3.6.1.2.1.16.1.1.1.5.1) BroadcastPktsRatioOfEth1/1 10 absolute rising-threshold 80 1 falling-threshold 5 2 entrytype forever owner user1]{lang="EN-US"}

[[1.3.6.1.2.1.16.1.1.1.6.1]{lang="EN-US"}]{#struct_0_21411_x5561_2035513042}[是节点]{style="font-family:宋体"}[etherStatsBroadcastPkts.1]{lang="EN-US"}[的]{style="font-family:宋体"}[OID]{lang="EN-US"}[，]{style="font-family:宋体"}[1.3.6.1.2.1.16.1.1.1.5.1]{lang="EN-US"}[是节点]{style="font-family:宋体"}[etherStatsPkts.1]{lang="EN-US"}[的]{style="font-family:宋体"}[OID]{lang="EN-US"}[。]{style="font-family:宋体"}[.1]{lang="EN-US"}[与接口统计表项的编号一致，如果创建的是"]{style="font-family:宋体"}[rmon statistics 5]{lang="EN-US"}["，则对应需要使用]{style="font-family:宋体"}[.1.3.6.1.2.1.16.1.1.1.6.5]{lang="EN-US"}[和]{style="font-family:宋体"}[.1.3.6.1.2.1.16.1.1.1.5.5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[以上配置步骤实现：对接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}]{#struct_0_21411_x5561_1780737242}[的使用情况进行统计、监控，当广播报文占总报文数的比例大于等于]{style="font-family:宋体"}[80]{lang="EN-US"}[％时将该事件记录到日志表中，比例小于等于]{style="font-family:宋体"}[5]{lang="EN-US"}[％时不采取任何措施。]{style="font-family:宋体"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21411_x5561_574608605}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display rmon prialarm]{lang="EN-US"}**]{#struct_0_21411_x5561_x124029140}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rmon event]{lang="EN-US"}**]{#struct_0_21411_x5561_631118307}
:::

::: {#1556203722 .myid}
[]{#_Toc404796933}[]{#struct_0_21411_x5561_1572833647}[]{#_Toc331497865}[]{#_Toc308096725}

**RMON \-- RMON配置命令 \-- rmon statistics**

------------------------------------------------------------------------

[**[rmon statistics]{lang="EN-US"}**]{#struct_0_21411_x5561_2028120221}[命令用来创建统计表项。]{style="font-family:宋体"}

[**[undo rmon statistics]{lang="EN-US"}**]{#struct_0_21411_x5561_186918652}[命令用来在统计表中删除指定表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21411_x5561_1693978445}

[**[rmon statistics]{lang="EN-US"}**[ *entry*-*number* \[ **owner** *text* \]]{lang="EN-US"}]{#struct_0_21411_x5561_60535473}

[**[undo rmon statistics]{lang="EN-US"}**[ *entry*-*number*]{lang="EN-US"}]{#struct_0_21411_x5561_1780671706}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21411_x5561_978971594}

[[统计表中没有任何表项。]{style="font-family:宋体"}]{#struct_0_21411_x5561_x793846725}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x1370288160}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_21411_x5561_328606610}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21411_x5561_1868388390}

[[network-admin]{lang="EN-US"}]{#struct_0_21411_x5561_2121838352}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21411_x5561_x1855796428}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x1005922314}

[*[entry]{lang="EN-US"}*[-*number*]{lang="EN-US"}]{#struct_0_21411_x5561_1780606170}[：统计表项的索引号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[owner]{lang="EN-US"}***[ text]{lang="EN-US"}*]{#struct_0_21411_x5561_577265760}[：该表项的创建者，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21411_x5561_x95458353}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当需要统计某个以太网端口的累加数据时，需要建立统计表。统计信息包括网络冲突数、]{style="font-family:宋体"}]{#struct_0_21411_x5561_247174296}[CRC]{lang="EN-US"}[校验错误报文数、过小（或超大）的数据报文数、广播、多播的报文数以及接收字节数、接收报文数等。]{style="font-family:宋体"}[设备重启时，会清除该统计信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户可以通过]{lang="EN-US" style="font-family:宋体"}**[display rmon statistics]{lang="EN-US"}**]{#struct_0_21411_x5561_2005340579}[命令来显示统计表项的信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每个接口下只能定义一个统计表项。]{style="font-family:宋体"}]{#struct_0_21411_x5561_x808053053}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户最多可以定义]{style="font-family:宋体"}]{#struct_0_21411_x5561_x1379566626}[100]{lang="EN-US"}[个统计表项。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RMON]{lang="EN-US"}]{#struct_0_21411_x5561_x360388811}[统计功能只能在二]{style="font-family:宋体"}[/]{lang="EN-US"}[三层以太网接口下进行配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21411_x5561_127426374}

[[\# ]{lang="EN-US"}]{#struct_0_21411_x5561_1451796968}[在统计表中添加]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的统计表项，表项的索引号为]{style="font-family:宋体"}[20]{lang="EN-US"}[，创建者为]{style="font-family:宋体"}[user1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21411_x5561_1780540634}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] rmon statistics 20 owner user1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21411_x5561_215381711}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display rmon statistics]{lang="EN-US"}**]{#struct_0_21411_x5561_1064560460}
:::
