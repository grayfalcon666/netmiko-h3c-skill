
**RMON \-- RMON配置命令 \-- display rmon alarm**

------------------------------------------------------------------------

**[display rmon alarm**]命令用来显示RMON告警表项的相关信息。

【命令】

**[display rmon alarm** [ *entry*-*number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[entry*-*number*]：告警表项的索引号，取值范围为1～65535。如果不指定索引号，则显示所有告警表项的相关信息。

【举例】

\# 显示所有RMON告警表项的相关信息。

\<Sysname\> display rmon alarm

AlarmEntry 1 owned by user1 is VALID.

  Sample type          : absolute

  Sampled variable     : 1.3.6.1.2.1.16.1.1.1.4.1\<etherStatsOctets.1\>

  Sampling interval (in seconds)     : 10

  Rising threshold      : 50(associated with event 1)

  Falling threshold     : 5(associated with event 2)

  Alarm sent upon entry startup  : risingOrFallingAlarm

  Latest value          : 0

表1-1 display rmon alarm命令显示信息描述表

字段

描述

AlarmEntry *entry*-*number* owned by *owner* is *status*.

*[owner*]创建的告警表项*entry*-*number*的当前状态为*status*

·*entry-number*：告警表项，对应MIB节点alarmIndex

·*owner*：该表项创建者，对应MIB节点alarmOwner

·*status*：与该索引对应的告警表项的状态（VALID表示有效，UNDERCREATION表示无效。处于无效状态的表项使用**display rmon alarm**命令可以查看到，但使用**display current-configuration**和**display this**看不到对应的**rmon alarm**配置命令）。命令行配置告警表项时不可配且缺省为VALID，对应MIB节点alarmStatus

Sample type

采样类型，对应MIB节点alarmSampleType，取值为：

·absolute：绝对值采样

·delta：变化值采样

Sampled variable

告警变量，即被监控的MIB节点，对应MIB节点alarmVariable

Sampling interval

采样的时间间隔，单位为秒，对应MIB节点alarmInterval

Rising threshold

上限阈值（当采样值大于等于该值时引发上限告警），对应MIB节点alarmRisingThreshold

associated with event

告警对应的事件索引，上限事件索引对应MIB节点alarmRisingEventIndex，下限事件索引对应MIB节点alarmFallingEventIndex

Falling threshold

下限阈值（当采样值小于等于该值时引发下限告警），对应MIB节点alarmFallingThreshold

Alarm sent upon entry startup

初次触发告警类型：

·risingAlarm：表示触发上限告警

·fallingAlarm：表示触发下限告警

·risingorFallingAlarm：表示触发上限或下限告警

缺省情况下，触发risingorFallingAlarm类型告警，对应MIB节点alarmStartupAlarm

Latest value

最近一次采样值，对应MIB节点alarmValue

【相关命令】

·**rmon alarm**

**RMON \-- RMON配置命令 \-- display rmon event**

------------------------------------------------------------------------

**[display rmon event**]命令用来显示RMON事件表项相关信息。

【命令】

**[display rmon event** [ *entry-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[entry-number*]：事件表项的索引号，取值范围为1～65535。如果不指定索引号，则显示所有事件表项的相关信息。

【使用指导】

显示信息包括：事件表中的事件索引、事件的所有者、对事件的描述、事件引发的动作（日志或告警信息）、最近一次事件发生的时刻（此时间是以系统初始化/启动以来的秒数计算的）等。

【举例】

\# 显示所有RMON事件表项相关信息。

\<Sysname\> display rmon event

EventEntry 1 owned by user1 is VALID.

  Description: N/A

  Community: Security

  Take the action log-trap when triggered, last triggered at 0days 00h:02m:27s uptime.

表1-2 display rmon event命令显示信息描述表

字段

描述

EventEntry *entry*-*number* owned by *owner* is *status*.

*[Owner*]创建的事件表项*entry*-*number*的当前状态为*status*

·*entry-number*：事件表项，对应MIB节点eventIndex

·*owner*：该表项创建者，对应MIB节点eventOwner

·*status*：与该索引对应的事件表项的状态（VALID表示有效，UNDERCREATION表示无效。处于无效状态的表项使用**display rmon event**命令可以查看到，但使用**display current-configuration**和**display this**看不到对应的**rmon event**配置命令）。命令行配置event表项时不可配且默认为VALID，对应MIB节点eventStatus

Description

该事件表项的描述，对应MIB节点eventDescription

Community

接收告警信息的网管站的团体名，对应MIB节点eventCommunity

Take the action *action* when triggered

事件触发时采取的动作：

·none：表示不采取任何措施

·log：表示事件被触发时会记录日志

·trap：表示事件被触发时会生成告警信息发送给设备的SNMP模块

·log-trap：表示事件被触发时既会记录日志又会生成告警信息发送给设备的SNMP模块

对应MIB节点eventType

last triggered at

*[time* uptime]

最近一次事件发生的时间（设备启动以来的时间），对应MIB节点eventLastTimeSent

【相关命令】

·**rmon event**

**RMON \-- RMON配置命令 \-- display rmon eventlog**

------------------------------------------------------------------------

**[display rmon eventlog**]命令用来显示事件日志表项的相关信息。

【命令】

**[display rmon eventlog** [ *entry-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[entry-number*]：事件表项的索引号，取值范围为1～65535。如果不指定索引号，则显示所有事件的日志表项的相关信息。

【使用指导】

·如果使用**rmon** **event**命令指定某表项的动作包括记录日志，当该事件被触发时，就会在RMON事件日志表中记录一条该事件的日志。通过该命令可以显示事件日志表的具体内容：事件表中的事件索引及事件当前的状态、事件产生日志的时刻（此时间是以系统初始化/启动以来的秒数计算的）以及事件的描述等。

·每个事件最多有10个日志记录，后续如果再产生日志记录将覆盖最老的。

【举例】

\# 查看由告警表产生的RMON事件99的日志。

\<Sysname\> display rmon eventlog 99

EventEntry 99 owned by ww is VALID.

  LogEntry 99.1 created at 50days 08h:54m:44s uptime.

  Description: The 1.3.6.1.2.1.16.1.1.1.4.5 defined in alarmEntry 77,

     uprise 16760000 with alarm value 16776314. Alarm sample type is absolute.

  LogEntry 99.2 created at 50days 09h:11m:13s uptime.

  Description: The 1.3.6.1.2.1.16.1.1.1.4.5 defined in alarmEntry 77,

     less than(or =) 20000000 with alarm value 16951648. Alarm sample type is ab

solute.

\# 查看由扩展告警表产生的RMON事件99的日志。

\<Sysname\> display rmon eventlog 99

EventEntry 99 owned by ww is VALID.

  LogEntry 99.3 created at 50days 09h:18m:43s uptime.

  Description: The alarm formula defined in prialarmEntry 777,

     less than(or =) 15000000 with alarm value 14026493. Alarm sample type is ab

solute.

  LogEntry 99.4 created at 50days 09h:23m:28s uptime.

  Description: The alarm formula defined in prialarmEntry 777,

     uprise 17000000 with alarm value 17077846. Alarm sample type is absolute.

表1-3 display rmon eventlog命令显示信息描述表

字段

描述

EventEntry *entry*-*number* owned by *owner* is *status*.

*[Owner*]创建的事件日志表项*entry*-*number*的当前状态为*status*

·*entry-number*：事件日志表项，对应事件表中MIB节点logEventIndex

·*owner*：该表项创建者，对应事件表中MIB节点eventOwner

·*status*：与该索引对应的事件日志表项的状态（VALID表示有效，UNDERCREATION表示无效。处于无效状态的表项使用**display rmon eventlog**可以查看到，但使用**display current-configuration**和**display this**看不到对应的**rmon eventlog**配置命令）。命令行配置event表项时不可配且默认为VALID，对应MIB节点eventStatus

LogEntry *entry*-*number* created at *created-time*

uptime.

日志表项*entry*-*number*的创建时间为*created-time*

·*entry-number*：日志表项索引号，表示方式为logEventIndex.logIndex，对应MIB节点logEventIndex与logIndex

·*created-time*：日志表项的创建时间，对应MIB节点logTime

Description

该条日志的描述，对应MIB节点logDescription

以上举例表明事件99产生的告警事件日志，其中告警表产生的事件日志2条，扩展告警表产生的事件日志2条：

·日志99.1由告警表项77触发生成，原因是告警值（16776314）超过了上限阈值（16760000），采样类型为绝对值采样。

·日志99.2由告警表项77触发生成，原因是告警值（16951648）低于下限阈值（20000000），采样类型为绝对值采样。

·日志99.3由扩展告警表项777触发生成，原因是告警值（14026493）低于下限阈值（15000000），采样类型为绝对值采样。

·日志99.4由扩展告警表项777触发生成，原因是告警值（17077846）超过上限阈值（17000000），采样类型为绝对值采样。

【相关命令】

·**rmon event**

**RMON \-- RMON配置命令 \-- display rmon history**

------------------------------------------------------------------------

**[display rmon history**]命令用来显示RMON历史控制表及历史采样信息。

【命令】

**[display rmon history** [ *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：指定接口类型和接口编号。如果未指定本参数，则显示所有接口下配置的历史控制表及历史采样信息。

【使用指导】

·在端口创建历史表项之后，系统会按一定的时间周期统计端口的信息，并将这些信息保存到etherHistoryEntry表，使用本命令可以显示该表项存储的记录。

·可显示的历史采样信息的数目以及历史采样的间隔可以通过**rmon history**命令来设置。

【举例】

\# 显示端口GigabitEthernet1/0/1的RMON历史控制表及历史采样信息。

\<Sysname\> display rmon history gigabitethernet 1/0/1

HistoryControlEntry 6 owned by user1 is VALID.

  Sampled interface     : GigabitEthernet 1/0/1 \<ifIndex.117\>

  Sampling interval     : 8(sec) with 3 buckets max

  Sampling record 1 :

    dropevents        : 0         , octets               : 5869

    packets           : 54        , broadcast packets    : 9

    multicast packets : 23        , CRC alignment errors : 0

    undersize packets : 0         , oversize packets     : 0

    fragments         : 0         , jabbers              : 0

    collisions        : 0         , utilization          : 0

  Sampling record 2 :

    dropevents        : 0         , octets               : 5367

    packets           : 55        , broadcast packets    : 1

    multicast packets : 7         , CRC alignment errors : 0

    undersize packets : 0         , oversize packets     : 0

    fragments         : 0         , jabbers              : 0

    collisions        : 0         , utilization          : 0

  Sampling record 3 :

    dropevents        : 0         , octets               : 936

    packets           : 10        , broadcast packets    : 0

    multicast packets : 6         , CRC alignment errors : 0

    undersize packets : 0         , oversize packets     : 0

    fragments         : 0         , jabbers              : 0

    collisions        : 0         , utilization          : 0

HistoryControlEntry 7 owned by user1 is VALID.

  Sampled interface     : GigabitEthernet 1/0/1 \<ifIndex.117\>

  Sampling interval     : 9(sec) with 1 buckets max

  Sampling record 1 :

    dropevents        : 0         , octets               : 1150

    packets           : 12        , broadcast packets    : 0

    multicast packets : 8         , CRC alignment errors : 0

    undersize packets : 0         , oversize packets     : 0

    fragments         : 0         , jabbers              : 0

    collisions        : 0         , utilization          : 0

表1-4 display rmon history命令显示信息描述表

字段

描述

HistoryControlEntry *entry*-*number* owned by *owner* is *status*.

*[Owner*]创建的历史控制表项*entry*-*number*的当前状态为*status*

·*entry-number*：历史控制表项，对应MIB节点historyControlIndex

·*owner*：该表项的创建者，对应MIB节点historyControlOwner

·*status*：与该索引对应的历史控制表项的状态（VALID表示有效，UNDERCREATION表示无效。处于无效状态的表项使用**display rmon history**命令可以查看到，但使用**display current-configuration**和**display this**看不到对应的**rmon history**配置命令）。命令行配置HistoryConrtol表项时不可配置且默认为VALID，对应MIB节点historyControlStatus

Sampled Interface

被统计的接口，对应MIB节点historyControlDataSource

Sampling interval

统计周期，单位为秒，系统会按周期对端口的信息进行统计，对应MIB节点historyControlInterval

buckets max

系统最多可保存的统计值的条数

·如果在**rmon history**命令中指定的**buckets**的值超出了设备实际支持的历史表容量，则此处显示的是设备实际支持的历史表容量

·如果当前保存的统计值条数已经到达了系统支持的最大值，则系统会删除最早的记录来保存新的统计值，对应MIB节点historyControlBucketsGranted

Sampling record

历史采样表项索引号，对应MIB节点etherHistorySampleIndex

dropevents

统计周期内检测到的丢包事件次数，对应MIB节点etherHistoryDropEvents

octets

统计周期内接收到的字节数，对应MIB节点etherHistoryOctets

packets

统计周期内接收到的包数，对应MIB节点etherHistoryPkts

broadcast packets

统计周期内接收到的广播包数，对应MIB节点etherHistoryBroadcastPkts

multicast packets

统计周期内接收到的组播包数，对应MIB节点etherHistoryMulticastPkts

CRC alignment errors

统计周期内接收到的校验错误的包数，对应MIB节点 etherHistoryCRCAlignErrors

undersize packets

统计周期内接收到的过小的包数，对应MIB节点etherHistoryUndersizePkts

oversize packets

统计周期内接收到的超大的包数，对应MIB节点etherHistoryOversizePkts

fragments

统计周期内接收到的过小且校验错误的包数，对应MIB节点etherHistoryFragments

jabbers

统计周期内接收到的超大且校验错误的包数，对应MIB节点etherHistoryJabbers（该字段的支持情况与设备型号有关，请以设备的实际情况为准）

collisions

统计周期内接收到的冲突的包数，对应MIB节点etherHistoryCollisions

utilization

统计周期内的带宽利用率，对应MIB节点etherHistoryUtilization

【相关命令】

·**rmon history**

**RMON \-- RMON配置命令 \-- display rmon prialarm**

------------------------------------------------------------------------

**[display rmon prialarm**]命令用来显示扩展告警表项的相关信息。

【命令】

**[display rmon prialarm** [ *entry-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[entry-number*]：扩展告警表项的索引，取值范围为1～65535。如果不指定索引号，则显示所有扩展告警表项的相关信息。

【举例】

\# 显示RMON所有的扩展告警表项的相关信息。

\<Sysname\> display rmon prialarm

PrialarmEntry 1 owned by user1 is VALID.

  Sample type          : absolute

  Variable formula      : (.1.3.6.1.2.1.16.1.1.1.6.1\*100/.1.3.6.1.2.1.16.1.1.1.5.1)

  Description           : ifUtilization.GigabitEthernet1/0/1

  Sampling interval (in seconds)     : 10

  Rising threshold      : 80(associated with event 1)

  Falling threshold     : 5(associated with event 2)

  Alarm sent upon entry startup  : risingOrFallingAlarm

  Entry lifetime : forever

  Latest value          : 85

表1-5 display rmon prialarm命令显示信息描述表

字段

描述

PrialarmEntry *entry*-*number* owned by *owner* is *status*.

*[Owner*]创建的扩展告警表项*entry*-*number*的当前状态为*status*

·*entry-number*：扩展告警表项，对应MIB节点hh3cRmonExtAlarmIndex

·*owner*：该表项创建者，对应MIB节点hh3cRmonExtAlarmOwner

·*status*：与该索引对应的扩展告警表项的状态（VALID表示有效，UNDERCREATION表示无效。处于无效状态的表项使用**display rmon prialarm**命令可以查看到，但使用**display current-configuration**和**display this**看不到相应的**rmon prialarm**配置命令）。命令行配置prialarm表项时不可配且默认为VALID，对应MIB节点hh3cRmonExtAlarmStatus

Sample type

采样类型，对应MIB节点hh3cRmonExtAlarmSampleType，取值为：

·absolute：绝对值采样

·delta：变化值采样

Variable formula

样本变量的计算公式，对应MIB节点hh3cRmonExtAlarmVariable

Description

扩展告警表项的描述信息，对应MIB节点hh3cRmonExtAlarmSympol

Sampling interval

采样间隔，单位为秒，系统会按一定的时间间隔对采样变量进行绝对值采样或者变化值采样，对应MIB节点hh3cRmonExtAlarmInterval

Rising threshold

告警上限，当采样值大于等于该值时引发上限告警，对应MIB节点hh3cRmonExtAlarmRisingThreshold

Falling threshold

告警下限，当采样值小于等于该值时引发下限告警，对应MIB节点hh3cRmonExtAlarmFallingThreshold

associated with event

告警对应的事件索引，上限事件索引对应MIB节点hh3cRmonExtAlarmRisingEvtIndex，下限事件索引对应MIB节点hh3cRmonExtAlarmFallingEvtIndex

Alarm sent upon entry startup

初次触发告警类型：

·risingAlarm：表示触发上限告警

·fallingAlarm：表示触发下限告警

·risingorFallingAlarm：表示触发上限或下限告警

缺省情况下，触发risingorFallingAlarm类型告警，对应MIB节点hh3cRmonExtAlarmStartupAlarm

Entry lifetime

该扩展告警表项的存活时间，可以是永远存在，也可以是在规定的时间内存在，对应MIB节点hh3cRmonExtAlarmStatType与hh3cRmonExtAlarmStatCycle。

Latest value

最近一次采样值，对应MIB节点hh3cRmonExtAlarmValue

![说明](RMON命令.files/image001.png)

[表]1-5(?-858458789#_Ref331682763)中，对于不同的OEM产商，MIB节点前缀不同，请以设备的实际情况为准。

【相关命令】

·**rmon prialarm**

**RMON \-- RMON配置命令 \-- display rmon statistics**

------------------------------------------------------------------------

**[display rmon statistics**]命令用来显示RMON统计信息。

【命令】

**[display rmon statistics** [ *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：指定接口类型和接口编号。如果未指定本参数，则显示所有接口下配置的统计表及统计信息。

【使用指导】

本命令显示的是从端口创建统计表项到执行显示命令这段时间内端口的统计信息。设备重启时，会清除该统计信息。

【举例】

\# 显示以太网接口GigabitEthernet1/0/1的RMON统计信息。

\<Sysname\> display rmon statistics gigabitethernet 1/0/1

EtherStatsEntry 1 owned by user1 is VALID.

  Interface : GigabitEthernet1/0/1\<ifIndex.3\>

  etherStatsOctets         : 43393306  , etherStatsPkts          : 619825

  etherStatsBroadcastPkts  : 503581    , etherStatsMulticastPkts : 44013

  etherStatsUndersizePkts  : 0         , etherStatsOversizePkts  : 0

  etherStatsFragments      : 0         , etherStatsJabbers       : 0

  etherStatsCRCAlignErrors : 0         , etherStatsCollisions    : 0

  etherStatsDropEvents (insufficient resources): 0

  Incoming packets by size:

  64     : 0         ,  65-127  : 0         ,  128-255  : 0

  256-511: 0         ,  512-1023: 0         ,  1024-1518: 0

表1-6 display rmon statistics命令显示信息描述表

字段

描述

EtherStatsEntry *entry*-*number* owned by *owner* is *status*.

*[Owner*]创建的统计信息表项*entry*-*number*的当前状态为*status*

·*entry-number*：统计信息表项，对应MIB节点etherStatsIndex

·*owner*：该表项创建者，对应MIB节点etherStatsOwner

·*status*：与该索引对应的统计表项的状态（VALID表示有效，UNDERCREATION表示无效。处于无效状态的表项使用**display rmon statistics**命令可以查看到，但使用**display current-configuration**和**display this**看不到对应的**rmon statistics**配置命令）。命令行配置statistics表项时不可配且默认为VALID，对应MIB节点etherStatsStatus

Interface

被统计端口，对应MIB节点etherStatsDataSource

etherStatsOctets

统计时间内，端口收到的所有报文的字节数，对应MIB节点etherStatsOctets

etherStatsPkts

统计时间内，端口收到的所有报文的包数，对应MIB节点etherStatsPkts

etherStatsBroadcastPkts

统计时间内，端口收到的所有广播包的数量，对应MIB节点etherStatsBroadcastPkts

etherStatsMulticastPkts

统计时间内，端口收到的所有组播包的数量，对应MIB节点etherStatsMulticastPkts

etherStatsUndersizePkts

统计时间内，端口收到的所有过小包的数量，对应MIB节点etherStatsUndersizePkts

etherStatsOversizePkts

统计时间内，端口收到的所有超大包的数量，对应MIB节点etherStatsOversizePkts

etherStatsFragments

统计时间内，端口收到的所有过小且校验错误包的数量，对应MIB节点etherStatsFragments

etherStatsJabbers

统计时间内，端口收到的所有超大且校验错误包的数量，对应MIB节点etherStatsJabbers

etherStatsCRCAlignErrors

统计时间内，端口收到的所有校验错误包的数量，对应MIB节点etherStatsCRCAlignErrors

etherStatsCollisions

统计时间内，端口收到的所有冲突包的数量，对应MIB节点etherStatsCollisions

etherStatsDropEvents

统计时间内，端口收到的所有丢包事件的数量，对应MIB节点etherStatsDropEvents

Incoming packets by size:

64:

65-127:

128-255:

 256-511:

 512-1023:

1024-1518:

统计时间内，根据包的长度对接收到的包分区间进行统计。其中：

·64字段的信息，对应MIB节点etherStatsPkts64Octets

·65-127字段的信息，对应MIB节点etherStatsPkts65to127Octets

·128-255字段的信息，对应MIB节点etherStatsPkts128to255Octets

·256-511字段的信息，对应MIB节点etherStatsPkts256to511Octets

·512-1023字段的信息，对应MIB节点etherStatsPkts512to1023Octets

·1024-1518字段的信息，对应MIB节点etherStatsPkts1024to1518Octets

【相关命令】

·**rmon statistics**

**RMON \-- RMON配置命令 \-- rmon alarm**

------------------------------------------------------------------------

**[rmon alarm**]命令用来创建告警表项。

**[undo rmon alarm**]命令用来在告警表中删除指定表项。

【命令】

**[rmon alarm**[ *entry-number alarm-variable sampling-interval* { **absolute** \| **delta** } ] [ **startup-alarm** { **falling** \| **rising** \| **rising-falling** } ]] **rising-threshold** *threshold-value1 event-entry1* **falling-threshold** *threshold-value2 event-entry2* [ **owner** *text* ]

**[undo rmon alarm ***entry-number*]

【缺省情况】

告警表中没有任何表项。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[entry*-*number*]：告警表项的索引号，取值范围为1～65535。

*[alarm*-*variable*]：告警变量，为1～255个字符的字符串，可以是节点OID的点分格式（格式为*entry.integer.instance*或者*叶子节点名**.instance，*如1.3.6.1.2.1.2.1.10.1），也可以是节点名（如ifInOctets.1）。只有可以解析为ASN.1中INTEGER（INTEGER,INTEGER32,Unsigned32, Counter32,Counter64,Gauge, or TimeTicks）的数据类型的变量能作为告警变量，比如etherStatsEntry表项的叶子节点（etherStatsOctets、etherStatsPkts和etherStatsBroadcastPkts等）的实例，ifEntry表项的叶子节点（ifInOctets、ifInUcastPkts和ifInNUcastPkts等）的实例。

*[sampling*-*interval*]：采样间隔时间，取值范围为5～[65535](#采样间隔时间取值范围)，单位为秒。

**[absolute**]：采样类型为绝对值采样，即采样时间到达时直接提取变量的值。

**[delta**]：采样类型为变化值采样，即采样时间到达时提取的是变量在采样间隔内的变化值。

**[startup-alarm**]：表示初次采样时，如果达到或超出阈值，触发的告警类型。如果未指定本参数，触发**rising-falling**类型告警。

**[rising**]：表示只触发上限告警。

**[falling**]：表示只触发下限告警。

**[rising-falling**]：表示触发上限或下限告警。

**[rising-threshold** *threshold*-*value1* *event*-*entry1*]：设置上限参数，*threshold*-*value1*表示上限阈值，取值范围为-2147483648～+2147483647；*event*-*entry1*表示上限阈值相应的事件索引号，取值范围为0～65535（0表示没有对应的事件，告警被触发后不会采取任何事件动作）。

**[falling-threshold** *threshold*-*value2* *event*-*entry2*]：设置下限参数，*threshold*-*value2*表示下限阈值，取值范围为-2147483648～+2147483647；*event*-*entry2*表示下限阈值相应的事件索引号，取值范围为0～65535（0表示没有对应的事件，告警被触发后不会采取任何事件动作）。

**[owner*** text*]：该表项的创建者，为1～127个字符的字符串，区分大小写。

【使用指导】

·本命令用来设置告警项，以便在出现异常时触发告警事件，再由告警事件来定义具体的处理方式。

·用户定义了告警表项后，系统会按照定义的时间周期去获取被监视的告警变量的值，并将该值和设定的阈值进行比较，去执行相应的处理过程。当采样值大于等于设定的上限*threshold-value1*，触发事件表中定义的事件*event-entry1*；采样值小于等于设定的下限*threshold-value2*，触发事件表中定义的事件*event-entry2*。

·在添加告警表项之前，需要通过**rmon event**命令定义好告警表项中引用的事件。否则，虽然会创建告警表项，但是不能触发告警事件。

·如果在新建表项时，指定的告警变量（*alarm-variable*）、采样间隔（*sampling-interval*）、采样类型（**absolute**或**delta**）、上限阈值（*threshold-value1*）和下限阈值（*threshold-value2*）五项参数的值和已经存在的告警表项对应的五项参数值完全相同时，系统将认为这两个表项的配置相同，创建操作失败。

·用户最多可以定义60个告警表项。

【举例】

\# 在告警表中添加表项1，对节点1.3.6.1.2.1.16.1.1.1.4.1以10秒的采样间隔进行绝对值采样，当采样值大于等于5000的上限阈值触发事件1，小于等于下限阈值5时触发事件2，创建者为user1。

\<Sysname\> system-view

Sysname rmon event 1 log

Sysname rmon event 2 none

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 rmon statistics 1

Sysname-GigabitEthernet1/0/1 quit

Sysname rmon alarm 1 1.3.6.1.2.1.16.1.1.1.4.1 10 absolute rising-threshold 5000 1 falling-threshold 5 2 owner user1

1.3.6.1.2.1.16.1.1.1.4是叶子节点etherStatsOctets的OID，它表示接口收到报文的统计值（以字节为单位）。以上步骤中也可以使用etherStatsOctets.1来代替1.3.6.1.2.1.16.1.1.1.4.1参数，.1与接口统计表项的编号一致，如果创建的是"rmon statistics 5"，则对应需要使用etherStatsOctets.5。

以上配置步骤实现：对接口GigabitEthernet1/0/1的使用情况进行统计、监控，每10秒钟对接口收到报文的总字节数取绝对值，如果接口收到报文的总字节数达到或超过5000字节时，就记录日志；当接口收到报文的总字节数小于或等于5字节时，不采取任何措施。

【相关命令】

·**display rmon alarm**

·**rmon event**

**RMON \-- RMON配置命令 \-- rmon event**

------------------------------------------------------------------------

**[rmon event**]命令用来创建事件表项。

**[undo rmon event**]命令用来在事件表中删除指定表项。

【命令】

**[rmon** **event** *entry*-*number* [ **description** *string*  { **log** \| **log-trap** *security-string \|* **none** \| **trap** *security-string* }  **owner** *text* ]]

**[undo rmon event ***entry*-*number*]

【缺省情况】

事件表中没有任何表项。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[entry*-*number*]：事件表项的索引号，取值范围为1～65535。

**[description** *string*]：事件的描述信息，为1～127个字符的字符串，区分大小写。

**[log**]：日志事件。当该事件被触发时，系统会记录日志。

**[log-trap**]：日志和告警事件。当该事件被触发时，系统会同时记录日志和生成告警信息，生成的告警信息将发送到设备的SNMP模块。通过设置SNMP中告警信息的发送参数，来决定告警信息输出的相关属性。有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"SNMP"。

*[security-string*]：表示接收告警信息的网管站的团体名，此处支持配置，但配置不生效。为1～127个字符的字符串，区分大小写。

**[none**]：不产生动作的事件。当该事件被触发时，系统不做处理。

**[trap**]：告警事件。当该事件被触发时，生成告警信息，生成的告警信息将发送到设备的SNMP模块。通过设置SNMP中告警信息的发送参数，来决定告警信息输出的相关属性。有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"SNMP"。

**[owner*** text*]：该表项的创建者，为1～127个字符的字符串，区分大小写。

【使用指导】

·RMON的事件管理定义事件索引号及事件的处理方式包括：记录日志、生成告警信息发送给设备的SNMP模块、记录日志的同时生成告警信息发送给设备的SNMP模块或者既不记录日志也生成告警信息发送给设备的SNMP模块。这样系统就可以对告警表中定义的告警事件进行相应的处理。事件组中定义的事件索引号对应告警组中指定事件索引号。

·用户最多可以定义60个事件表项。

【举例】

\# 在事件表中添加索引号为10、类型为日志的事件，创建者为user1。

\<Sysname\> system-view

Sysname rmon event 10 log owner user1

【相关命令】

·**display rmon event**

·**rmon alarm**

·**rmon prialarm**

**RMON \-- RMON配置命令 \-- rmon history**

------------------------------------------------------------------------

**[rmon history**]命令用来创建历史控制表项。

**[undo rmon history**]命令用来在历史表中删除指定表项。

【命令】

**[rmon history** *entry*-*number* **buckets** *number* **interval** *sampling*-*interval* [ **owner** *text* ]]

**[undo rmon history** *entry*-*number*]

【缺省情况】

历史控制表中没有任何表项。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[entry*-*number*]：历史控制表项的索引号，取值范围为1～65535。

**[buckets** *number*]：该历史控制表项对应的历史表容量，即历史表最多可容纳的记录数，取值范围为1～65535，但实际配置如果超过50时，会提示取50最大配置值。

**[interval** *sampling*-*interval*]：统计周期，取值范围为5～3600，单位为秒。

**[owner** *text*]：该表项的创建者，为1～127个字符的字符串，区分大小写。

【使用指导】

·创建历史控制表项后，系统会按周期统计当前端口收发报文的情况，并将统计值作为一个实例保存在etherHistoryEntry表的叶子节点下。可保存的统计值个数由**buckets** *number*参数决定，当历史表的容量达到最大值时，系统会删除最早的记录来保存新的统计值。统计信息包括端口一个周期内收到的报文总数、广播报文总数和组播报文总数等。

·在添加控制历史表项的过程中，如果指定的历史表容量超出了设备实际支持的历史表容量时，新的历史表项会被添加，但该表项对应生效的历史表容量为设备实际支持的历史表容量，可以使用**display rmon history**命令来查看配置结果。

·如果在创建历史控制表项时，指定的采样间隔（**interval ***sampling-interval*）参数的值和该接口下已经存在的历史控制表项对应的该项参数值相同时，系统将认为这两个表项的配置相同，创建操作失败。

·用户最多可以定义100个历史控制表项。

·RMON统计功能只能在二/三层以太网接口下进行配置。

【举例】

\# 创建索引号为1，表容量为10，采样时间为5秒的历史控制表项，创建者为user1。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 rmon history 1 buckets 10 interval 5 owner user1

【相关命令】

·**display rmon history**

**RMON \-- RMON配置命令 \-- rmon prialarm**

------------------------------------------------------------------------

**[rmon ***prialarm*]命令用来创建扩展告警表项。

**[undo rmon ***prialarm*]命令用来在扩展告警表中删除指定表项。

【命令】

**[rmon prialarm**[ *entry-number prialarm-formula prialarm-des sampling-interval* { **absolute** \| **delta** } [ **startup-alarm** { **falling** \| **rising** \| **rising-falling** } ] **rising-threshold** *threshold-value1 event-entry1* **falling-threshold** *threshold-value2 event-entry2* **entrytype** { **forever** \| **cycle** *cycle-period* }  **owner** *text* ]]

**[undo rmon prialarm ***entry-number*]

【缺省情况】

扩展告警表中没有任何表项。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[entry*-*number*]：扩展告警表项的索引号，取值范围为1～65535。

*[prialarm-fromula*]：对告警变量进行计算的告警公式，为1～255个字符的字符串。公式中的告警变量必须以OID来表示，OID表达式必须以小数点开始，例如(.1.3.6.1.2.1.2.1.10.1)\*8；运算公式由用户定义，可以使用加减乘除四种运算方法对告警变量进行运算，该运算公式的结果取值为长整型数，但不支持负数的输入。用户在编写公式的时候需要注意，公式中每一步的运算结果都不能超过长整型的表达范围，否则可能会得出错误的结果。

*[prialarm-des*]：对该告警的描述，为1～127个字符的字符串，区分大小写。

*[sampling*-*interval*]：采样间隔时间，取值范围为10～65535，单位为秒。

**[absolute**]：采样类型为绝对值采样，即采样时间到达时直接提取变量的值。

**[delta**]：采样类型为变化值采样，即采样时间到达时提取的是变量在采样间隔内的变化值。**startup-alarm**：表示初次采样时，如果达到或超出阈值，触发的告警类型。如果未指定本参数，触发rising-falling类型告警。

**[rising**]：表示只触发上限告警。

**[falling**]：表示只触发下限告警。

**[rising-falling**]：表示触发上限或下限告警。

**[rising-threshold** *threshold*-*value1* *event*-*entry1*]：设置超上限参数，*threshold*-*value1*表示上限阈值，取值范围为-2147483648～+2147483647；*event*-*entry1*表示上限阈值相应的事件索引号，取值范围为0～65535（0表示没有对应的事件，告警被触发后不会采取任何事件动作）。

**[falling-threshold** *threshold*-*value2* *event*-*entry2*]：设置下限参数，*threshold*-*value2*表示下限阈值，取值范围为-2147483648～+2147483647；*event*-*entry2*表示下限阈值相应的事件索引号，取值范围为0～65535（0表示没有对应的事件，告警被触发后不会采取任何事件动作）。

**[forever**]：本告警实例存活类型为永久。

**[cycle ***cycle*-*period*]：本告警实例的存活时间，单位为秒，取值范围0～4294967。

**[owner*** text*]：该表项的创建者，为1～127个字符的字符串，区分大小写。

【使用指导】

·用户定义了扩展告警表项后，系统先对定义的扩展告警公式中的告警变量按照定义的时间间隔进行采样，再将采样值按照定义的运算公式进行计算，最后将计算结果和和设定的阈值进行比较，并执行相应的处理过程。

·在添加扩展告警表项之前，需要通过**rmon event**命令定义好扩展告警表项中引用的事件。

·如果在新建表项时，指定的告警变量公式（*prialarm-formula*）、采样间隔（*sampling-interval*）、采样类型（**absolute**或**delta**）、上限阈值（*threshold-value1*）和下限阈值（*threshold-value2*）五项参数的值和已经存在的扩展告警表项对应的五项参数值完全相同时，系统将认为这两个表项的配置相同，创建操作失败。

·用户最多可以定义50个扩展告警表项。

【举例】

\# 使用扩展告警对接口接收到的广播报文比率进行监控。

在扩展告警表中添加索引号为1的表项，对相应告警变量以公式(.1.3.6.1.2.1.16.1.1.1.6.1\*100/.1.3.6.1.2.1.16.1.1.1.5.1)运算，对该公式中涉及的变量以10秒的采样间隔进行绝对值采样。上限告警值为80对应事件1（将事件记录在日志表中），下限告警值为5对应事件2（不需要采取措施），表项的存活时间为永远（**forever**），创建者为*user1*。（广播报文比率的计算公式为：接口接收到的广播报文总数/接口接收到的总报文数，该公式由用户自行定义）

\<Sysname\> system-view

Sysname rmon event 1 log

Sysname rmon event 2 none

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 rmon statistics 1

Sysname-GigabitEthernet1/0/1 quit

Sysname rmon prialarm 1 (.1.3.6.1.2.1.16.1.1.1.6.1\*100/.1.3.6.1.2.1.16.1.1.1.5.1) BroadcastPktsRatioOfEth1/1 10 absolute rising-threshold 80 1 falling-threshold 5 2 entrytype forever owner user1

1.3.6.1.2.1.16.1.1.1.6.1是节点etherStatsBroadcastPkts.1的OID，1.3.6.1.2.1.16.1.1.1.5.1是节点etherStatsPkts.1的OID。.1与接口统计表项的编号一致，如果创建的是"rmon statistics 5"，则对应需要使用.1.3.6.1.2.1.16.1.1.1.6.5和.1.3.6.1.2.1.16.1.1.1.5.5。

以上配置步骤实现：对接口GigabitEthernet1/0/1的使用情况进行统计、监控，当广播报文占总报文数的比例大于等于80％时将该事件记录到日志表中，比例小于等于5％时不采取任何措施。

【相关命令】

·**display rmon prialarm**

·**rmon event**

**RMON \-- RMON配置命令 \-- rmon statistics**

------------------------------------------------------------------------

**[rmon statistics**]命令用来创建统计表项。

**[undo rmon statistics**]命令用来在统计表中删除指定表项。

【命令】

**[rmon statistics** *entry*-*number* [ **owner** *text* ]]

**[undo rmon statistics** *entry*-*number*]

【缺省情况】

统计表中没有任何表项。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[entry*-*number*]：统计表项的索引号，取值范围为1～65535。

**[owner*** text*]：该表项的创建者，为1～127个字符的字符串，区分大小写。

【使用指导】

·当需要统计某个以太网端口的累加数据时，需要建立统计表。统计信息包括网络冲突数、CRC校验错误报文数、过小（或超大）的数据报文数、广播、多播的报文数以及接收字节数、接收报文数等。设备重启时，会清除该统计信息。

·用户可以通过**display rmon statistics**命令来显示统计表项的信息。

·每个接口下只能定义一个统计表项。

·用户最多可以定义100个统计表项。

·RMON统计功能只能在二/三层以太网接口下进行配置。

【举例】

\# 在统计表中添加GigabitEthernet1/0/1的统计表项，表项的索引号为20，创建者为user1。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 rmon statistics 20 owner user1

【相关命令】

·**display rmon statistics**
