<!-- CMD-INDEX
  diagnostic bootup level             | 系统视图             | L24
  diagnostic bootup enable test       |                  | L74
  diagnostic event-log size           | 系统视图             | L170
  diagnostic monitor enable           |                  | L214
  diagnostic monitor interval         |                  | L320
  diagnostic ondemand failure         | 用户视图             | L418
  diagnostic ondemand repeating       | 用户视图             | L474
  diagnostic ondemand start           | 用户视图             | L524
  diagnostic ondemand stop            | ]                | L634
  diagnostic simulation               |                  | L712
  display diagnostic bootup           | 任意视图             | L806
  display diagnostic bootup level     | 任意视图             | L906
  display diagnostic content          | 任意视图             | L938
  display diagnostic event-log        | 任意视图             | L1324
  display diagnostic ondemand configuration | 任意视图             | L1380
  display diagnostic result           | 任意视图             | L1424
  display diagnostic result statistics | 任意视图             | L1644
  display diagnostic simulation       | 任意视图             | L1832
  reset diagnostic event-log          | 用户视图             | L1920
  reset diagnostic result             | 用户视图             | L1948
-->

**GOLD \-- GOLD配置命令 \-- diagnostic bootup level**

------------------------------------------------------------------------

**[diagnostic bootup level**]命令用来配置设备下次启动时，是否执行所有启动诊断测试例。

**[undo diagnostic bootup level**]命令用来恢复缺省情况。

【命令】

**[diagnostic bootup level **[{ **bypass** \| **complete** }]]

**[undo diagnostic bootup level**]

【缺省情况】

系统在启动时不执行任何启动测试例。

【视图】

系统视图

【缺省用户角色】

network-admin

【参数】

**[bypass**]：所有测试例均不执行。

**[complete**]：执行所有的测试例。

【使用指导】

启动诊断是在系统启动过程或者板卡插拔时对板卡进行检查，设备将根据检查的结果决定板卡能否运行。启动诊断能够保证板卡基本硬件功能正常后才开始工作。设备支持的启动诊断的具体内容与设备型号有关，请以设备的实际情况为准。

本命令配置后，将在设备下次启动时生效。

【举例】

\# 配置设备下次启动时，执行所有启动诊断测试例。

\<sysname\> system-view

sysname diagnostic bootup level complete

【相关命令】

·**display diagnostic bootup level**

**GOLD \-- GOLD配置命令 \-- diagnostic bootup enable test**

------------------------------------------------------------------------

**[diagnostic bootup enable test**]命令用来配置设备下次启动时，执行指定的启动诊断测试例。

**[undo diagnostic bootup enable test**]命令用来取消执行指定的启动诊断测试例。

【命令】

集中式设备：

**[diagnostic bootup enable test**]*test-name* [ **para** *parameters* ]

**[undo diagnostic bootup enable test**]*test-name* [ **para** *parameters* ]

分布式设备－独立运行模式/集中式IRF设备：

**[diagnostic bootup enable slot **]*slot-number-list* [ **cpu** *cpu-number * **test** ]*test-name* [ **para** *parameters* ]

**[undo diagnostic bootup enable **]**slot ***slot-number-list* \**[cpu***cpu-number * **test** ]*test-name* [ **para** *parameters* ]

分布式设备－IRF模式：

**[diagnostic bootup enable chassis **]*chassis-number ***slot ***slot-number-list* [ **cpu** *cpu-number * **test** ]*test-name* [ **para** *parameters* ]

**[undo diagnostic bootup **]**enablechassis ***chassis-number ***slot***slot-number-list* \**[cpu***cpu-number * **test** ]*test-name* [ **para** *parameters* ]

【缺省情况】

系统在启动时不执行任何启动测试例。

【视图】

系统视图

【缺省用户角色】

network-admin

【参数】

**[slot **]*slot-number-list*：槽位号列表，表示同时使能多个单板的测试例。表示方式为*slot-number-list**=* *[slot-number* \**[to*** slot-number*  }&\<1-7\>]。其中，*slot-number*表示单板所在的槽位号，&\<1-7\>表示前面的参数最多可以输入7次。（分布式设备－独立运行模式）

**[slot **]*slot-number-list*：成员编号列表，表示同时使能多个成员设备的测试例。表示方式为*slot-number-list**=* *[slot-number* \**[to*** slot-number*  }&\<1-7\>]。其中，*slot-number*表示设备在IRF中的成员编号，&\<1-7\>表示前面的参数最多可以输入7次。（集中式IRF设备）（不支持IRF3的设备）

**[slot **]*slot-number-list*：成员编号/PEX虚拟槽位号列表，表示同时使能多个成员设备/PEX的测试例。表示方式为*slot-number-list**=* *[slot-number* \**[to*** slot-number*  }&\<1-7\>]。其中，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号，&\<1-7\>表示前面的参数最多可以输入7次。（集中式IRF设备）（支持IRF3的设备）

**[chassis **]*chassis-number*：表示设备在IRF中的成员编号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **]*chassis-number*：表示设备在IRF中的成员编号或者PEX对应的虚拟框号。（分布式设备－IRF模式）（支持IRF3的设备）

**[slot **]*slot-number-list*：槽位号列表，表示同时使能多个单板的测试例。表示方式为*slot-number-list**=* *[slot-number* \**[to*** slot-number*  }&\<1-7\>]。其中，*slot-number*表示单板所在的槽位号，&\<1-7\>表示前面的参数最多可以输入7次。（分布式设备－IRF模式）（不支持IRF3的设备）

**[slot **]*slot-number-list*：槽位号列表，表示同时使能多个单板/PEX的测试例。表示方式为*slot-number-list**=* *[slot-number* \**[to*** slot-number*  }&\<1-7\>]。其中，*slot-number*表示单板/PEX所在的槽位号，&\<1-7\>表示前面的参数最多可以输入7次。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu**]*cpu-number*：表示指定CPU的编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[test**]* test-name*：表示启动诊断类型的测试例的名称，为1～31个字符的字符串，不区分大小写。具体取值可通过在**test**参数后输入问号，并回车来获取。

**[para**]*parameters*：表示测试例的执行参数，为1～511个字符的字符串，不区分大小写。参数的取值、输入方式以及缺省情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】]

本命令配置后，将在设备下次启动时生效。]

【举例】]

\# ]配置设备下次启动时，执行启动诊断测试例OnlyBootUp，并指定参数为123。（集中式设备）

\<Sysname\> system-view]

sysname diagnostic bootup enable test OnlyBootUp para 123

\# 配置设备下次启动时，执行0号单板上的启动诊断测试例OnlyBootUp，并指定参数为123。（分布式设备－独立运行模式）

\<Sysname\> system-view

sysname diagnostic bootup enable slot 0 test OnlyBootUp para 123

\# 配置设备下次启动时，执行成员设备1上的启动诊断测试例OnlyBootUp，并指定参数为123。（集中式IRF设备）

\<Sysname\> system-view

sysname diagnostic bootup enable slot 1 test OnlyBootUp para 123

\# 配置设备下次启动时，执行1号成员设备的0号单板上的启动诊断测试例OnlyBootUp，并指定参数为123。（分布式设备－IRF模式）

\<Sysname\> system-view

sysname diagnostic bootup enable chassis 1 slot 0 test OnlyBootUp para 123

【相关命令】

·**display diagnostic bootup**

**GOLD \-- GOLD配置命令 \-- diagnostic event-log size**

------------------------------------------------------------------------

**[diagnostic event-log size**]命令用来配置可存储的GOLD日志的最大条数。

**[undo diagnostic event-log size**]命令用来恢复缺省情况。

【命令】

**[diagnostic event-log size **]*[number*]

**[undo diagnostic event-log size**]

【缺省情况】

可存储的GOLD日志的最大条数为512条。

【视图】

系统视图

【缺省用户角色】

network-admin

【参数】

*[number*]：可存储的GOLD日志的最大条数，取值范围为0～1024，单位为条。

【使用指导】

执行该命令时，如果指定的*number*值小于当前已存储的GOLD日志的条数，则系统会自动删除最旧的GOLD日志，直到当前GOLD日志的条数为*number*。

当设备当前已存储的GOLD日志的条数达到最大值，同时还有新的GOLD日志需要存储时，系统会删除最旧的日志来存储新的日志。

【举例】

\# 配置可存储的GOLD日志的最大条数为600条。

\<sysname\> system-view

sysname diagnostic event-log size 600

**GOLD \-- GOLD配置命令 \-- diagnostic monitor enable**

------------------------------------------------------------------------

**[diagnostic monitor enable**]命令用来开启监控诊断功能。

**[undo diagnostic monitor enable**]命令用来关闭监控诊断功能。

【命令】

集中式设备：

**[diagnostic monitor enable** [ **test** ]*test-name* ]

**[undo diagnostic monitor enable** [ **test** ]*test-name* ]

分布式设备－独立运行模式/集中式IRF设备：

**[diagnostic monitor enable** **slot** ]*slot-number-list* \**[cpu***cpu-number *  **test** *test-name* ]

**[undo diagnostic monitor enable slot**]*slot-number-list* \**[cpu***cpu-number *  **test** *test-name* ]

分布式设备－IRF模式：

**[diagnostic monitor enable chassis **]*chassis-number ***slot ***slot-number-list* \**[cpu***cpu-number *  **test** *test-name* ]

**[undo diagnostic monitor enable chassis**]*chassis-number ***slot***slot-number-list* \**[cpu***cpu-number *  **test*** test-name* ]

【缺省情况】

监控诊断测试例缺省是否使能与设备的型号以及版本有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

【参数】

**[slot **]*slot-number-list*：槽位号列表，表示同时使能多个单板的测试例。表示方式为*slot-number-list**=* *[slot-number* \**[to*** slot-number*  }&\<1-7\>]。其中，*slot-number*表示单板所在的槽位号，&\<1-7\>表示前面的参数最多可以输入7次。（分布式设备－独立运行模式）

**[slot **]*slot-number-list*：成员编号列表，表示同时使能多个成员设备的测试例。表示方式为*slot-number-list**=* *[slot-number* \**[to*** slot-number*  }&\<1-7\>]。其中，*slot-number*表示设备在IRF中的成员编号，&\<1-7\>表示前面的参数最多可以输入7次。（集中式IRF设备）（不支持IRF3的设备）

**[slot **]*slot-number-list*：成员编号/PEX虚拟槽位号列表，表示同时使能多个成员设备/PEX的测试例。表示方式为*slot-number-list**=* *[slot-number* \**[to*** slot-number*  }&\<1-7\>]。其中，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号，&\<1-7\>表示前面的参数最多可以输入7次。（集中式IRF设备）（支持IRF3的设备）

**[chassis **]*chassis-number*：表示设备在IRF中的成员编号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **]*chassis-number*：表示设备在IRF中的成员编号或者PEX对应的虚拟框号。（分布式设备－IRF模式）（支持IRF3的设备）

**[slot **]*slot-number-list*：槽位号列表，表示同时使能多个单板的测试例。表示方式为*slot-number-list**=* *[slot-number* \**[to*** slot-number*  }&\<1-7\>]。其中，*slot-number*表示单板所在的槽位号，&\<1-7\>表示前面的参数最多可以输入7次。（分布式设备－IRF模式）（不支持IRF3的设备）

**[slot **]*slot-number-list*：槽位号列表，表示同时使能多个单板/PEX的测试例。表示方式为*slot-number-list**=* *[slot-number* \**[to*** slot-number*  }&\<1-7\>]。其中，*slot-number*表示单板/PEX所在的槽位号，&\<1-7\>表示前面的参数最多可以输入7次。（分布式设备－IRF模式）（支持IRF3的设备）

**[test **]*test-name*：指定测试例的名称，为1～31个字符的字符串，不区分大小写。不指定该参数时，表示使能设备上的所有监控诊断测试例。（集中式设备）

**[test **]*test-name*：指定测试例的名称，为1～31个字符的字符串，不区分大小写。不指定该参数时，表示使能指定单板上的所有监控诊断测试例。（分布式设备－独立运行模式/分布式设备－IRF模式）

**[test **]*test-name*：指定测试例的名称，为1～31个字符的字符串，不区分大小写。不指定该参数时，表示使能指定成员设备上的所有监控诊断测试例。（集中式IRF设备）

**[cpu**]*cpu-number*：表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】]

系统在运行过程中]按照一定的时间间隔定时执行测试例，来检测系统中的硬件故障并记录诊断结果的过程，称为监控诊断。监控诊断只能执行非破坏性的测试例。

破坏性和非破坏性是测试例的一个属性，由开发人员在设计测试例的时候指定。其中：]

·]破坏性测试例在执行过程中会对设备当前正常运行的业务产生影响或导致业务无法运行，如内存耗尽测试例。

·]非破坏性测试例在执行过程中不会对设备当前正常运行的业务产生影响。

对于缺省启动的监控诊断测试例，在设备启动后会自动执行；对于缺省关闭的监控诊断测试例，须使用本命令才能执行。

【举例】

\# 使能测试例HGMonitor。（集中式设备）

\<sysname\> system-view

sysname diagnostic monitor enable test HGMonitor

\# 使能2号单板上的测试例HGMonitor。（分布式设备－独立运行模式）

\<sysname\> system-view

sysname diagnostic monitor enable slot 2 test HGMonitor

\# 使能2号成员设备上的测试例HGMonitor。（集中式IRF设备）

\<sysname\> system-view

sysname diagnostic monitor enable slot 2 test HGMonitor

\# 使能2号成员设备的2号单板上的测试例HGMonitor。（分布式设备－IRF模式）

\<sysname\> system-view

sysname diagnostic monitor enable chassis 2 slot 2 test HGMonitor

【相关命令】

·**diagnostic monitor interval**

**GOLD \-- GOLD配置命令 \-- diagnostic monitor interval**

------------------------------------------------------------------------

**[diagnostic monitor interval**]命令用来配置监控诊断测试例的执行时间间隔。

**[undo diagnostic monitor interval**]命令用来恢复缺省情况。

【命令】

集中式设备：

**[diagnostic monitor interval** [ **test** ]*test-name*  **time** ]*time*

**[undo diagnostic monitor interval** [ **test** ]*test-name* ]

分布式设备－独立运行模式/集中式IRF设备：

**[diagnostic monitor interval slot**]*slot-number-list* \**[cpu***cpu-number *  **test** *test-name*  **time** ]*time*

**[undo diagnostic monitor interval slot**]*slot-number-list *\**[cpu***cpu-number *]** **test** *test-name*

分布式设备－IRF模式：

**[diagnostic monitor interval chassis**]*chassis-number*** slot ***slot-number-list* \**[cpu***cpu-number *  **test** *test-name*  **time** ]*time*

**[undo diagnostic monitor interval chassis**]*chassis-number* **slot** *slot-number-list* \**[cpu***cpu-number *  **test** *test-name* ]

【缺省情况】

监控诊断测试例时间间隔的缺省值与设备的型号以及版本有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

【参数】

**[slot **]*slot-number-list*：槽位号列表，表示同时配置多个单板的测试例的时间间隔。表示方式为*slot-number-list**=* *[slot-number* \**[to*** slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要配置的单板所在的槽位号。&\<1-7\>表示前面的参数最多可以输入7次。（分布式设备－独立运行模式）

**[slot **]*slot-number-list*：成员编号列表，表示同时配置多个成员设备的测试例的时间间隔。表示方式为*slot-number-list**=* *[slot-number* \**[to*** slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要配置的设备在IRF中的成员编号，&\<1-7\>表示前面的参数最多可以输入7次。（集中式IRF设备）（不支持IRF3的设备）

**[slot **]*slot-number-list*：成员编号/PEX虚拟槽位号列表，表示同时配置多个成员设备/PEX的测试例的时间间隔。表示方式为*slot-number-list**=* *[slot-number* \**[to*** slot-number*  }&\<1-7\>]。其中，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号，&\<1-7\>表示前面的参数最多可以输入7次。（集中式IRF设备）（支持IRF3的设备）

**[chassis **]*chassis-number*：表示需要配置测试例时间间隔的设备在IRF中的成员编号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **]*chassis-number*：表示需要配置测试例时间间隔的设备在IRF中的成员编号或者PEX对应的虚拟框号。（分布式设备－IRF模式）（支持IRF3的设备）

**[slot **]*slot-number-list*：槽位号列表，表示同时配置多个单板的测试例的时间间隔。表示方式为*slot-number-list**=* *[slot-number* \**[to*** slot-number*  }&\<1-7\>]。其中，*slot-number*表示单板所在的槽位号。&\<1-7\>表示前面的参数最多可以输入7次。（分布式设备－IRF模式）（不支持IRF3的设备）

**[slot **]*slot-number-list*：槽位号列表，表示同时配置多个单板/PEX的测试例的时间间隔。表示方式为*slot-number-list**=* *[slot-number* \**[to*** slot-number*  }&\<1-7\>]。其中，*slot-number*表示单板/PEX所在的槽位号，&\<1-7\>表示前面的参数最多可以输入7次。（分布式设备－IRF模式）（支持IRF3的设备）

**[test **]*test-name*：指定测试例的名称，为1～31个字符的字符串，不区分大小写。不指定该参数时，表示设备上的所有监控诊断测试例。（集中式设备）

**[test **]*test-name*：指定测试例的名称，为1～31个字符的字符串，不区分大小写。不指定该参数时，表示指定单板上的所有监控诊断测试例。（分布式设备－独立运行模式/分布式设备－IRF模式）

**[test **]*test-name*：指定测试例的名称，为1～31个字符的字符串，不区分大小写。不指定该参数时，表示指定成员设备上的所有监控诊断测试例。（集中式IRF设备）

*[time*]：指定监控诊断测试例的执行时间间隔，格式为hh:mm:ss（小时:分钟:秒）。其中hh取值范围为0～23，mm取值范围为0～59，ss取值范围为0～59。如果要设置成整分，则可以不输入秒；如果要设置成整时，则可以不输入分和秒。比如将*time*参数设置为1表示时间间隔为1小时。

**[cpu**]*cpu-number*：表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】]

使能监控诊断测试例后，测试例会按照一定的时间间隔周期执行，这个时间间隔可用该命令配置。]

用户配置的时间间隔不能小于监控诊断测试例要求的最小值。监控诊断测试例要求的最小值可使用携带]**verbose**参数的**display diagnostic content**命令查看。

【举例】]

\# ]配置测试例HGMonitor的执行时间间隔为1分钟。（集中式设备）

\<sysname\> system-view

sysname diagnostic monitor interval test HGMonitor time 00:01:00

\# 配置1号单板上测试例HGMonitor的时间间隔为1分钟。（分布式设备－独立运行模式/集中式IRF设备）

\<sysname\> system-view

sysname diagnostic monitor interval slot 1 test HGMonitor time 00:01:00

\# 配置2号框中1号单板上测试例HGMonitor的时间间隔为1分钟。（分布式设备－IRF模式）

\<sysname\> system-view

sysname diagnostic monitor interval chassis 2 slot 1 test HGMonitor time 00:01:00

【相关命令】

·**diagnostic monitor enable**

·**display diagnostic content**

**GOLD \-- GOLD配置命令 \-- diagnostic ondemand failure**

------------------------------------------------------------------------

**[diagnostic ondemand failure**]命令用来配置按需诊断测试例的累计失败执行次数的最大值。

**[undo diagnostic ondemand failure**]命令用来恢复缺省情况。

【命令】

**[diagnostic ondemand failure**]*failure-number*

**[undo diagnostic ondemand failure**]

【缺省情况】

不限制按需测试例的累计失败执行次数的最大值。

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

*[failure-number*]：指定失败的次数，取值范围为1～999。

【使用指导】

使用**diagnostic ondemand start**命令启动按需诊断测试例后，这些测试例什么时候终止执行，受三条命令的限制：

·使用**diagnostic ondemand stop**命令可立即停止执行该测试例。

·如果某测试例的执行次数达到**diagnostic ondemand repeating**命令中指定的值，则系统会自动停止执行该测试例。

·如果某测试例的执行次数还未达到**diagnostic ondemand repeating**命令中指定的值，但是测试例在启动后，累计失败的执行次数已达到**diagnostic ondemand failure**命令中指定的值，则系统会自动停止执行该测试例。

本命令可用来修改将要启动的按需诊断测试例的累计失败执行次数的最大值，当前已启动的按需诊断测试例仍使用修改前的值。设备重启后，本命令会恢复到缺省情况，如仍需修改，请重新配置。

【举例】

\# 配置按需诊断测试例的累计失败执行次数的最大值为5次。

\<sysname\> diagnostic ondemand failure 5

【相关命令】

·**diagnostic ondemand repeating**

·**diagno****stic ondemand start**

·**display diagnostic ****ondemand configuration**

**GOLD \-- GOLD配置命令 \-- diagnostic ondemand repeating**

------------------------------------------------------------------------

**[diagnostic ondemand repeating**]命令用来配置按需诊断测试例重复执行的次数。

**[undo diagnostic ondemand repeating**]命令用来恢复缺省情况。

【命令】

**[diagnostic ondemand repeating **]*repeating-number*

**[undo diagnostic ondemand repeating**]

【缺省情况】

按需类型诊断测试例重复执行的次数为1次数，表示执行一次就结束。

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

*[repeating-number*]：表示按需诊断测试例重复执行的次数，取值范围为1～999。

【使用指导】

本命令用来修改将要启动的按需诊断测试例重复执行的次数，当前已启动的按需诊断测试例仍使用修改前的值。设备重启后，本命令会恢复到缺省情况，如仍需修改，请重新配置。

按需诊断测试例重复执行的次数不能比配置的失败次数小，否则，命令执行失败。按需诊断测试例的失败次数可通过**diagnostic ondemand failure**命令配置。

【举例】

\# 配置按需类型测试例重复执行的次数为2。

\<sysname\> diagnostic ondemand repeating 2

【相关命令】

·**diagnostic ondemand failure**

·**diagnostic ondemand start**

·**display diagnostic configuration**

**GOLD \-- GOLD配置命令 \-- diagnostic ondemand start**

------------------------------------------------------------------------

**[diagnostic ondemand start**]命令用来启动按需类型诊断。

【命令】

集中式设备：

**[diagnostic ondemand start test***test-name* } [ **para** *parameters* ]

分布式设备－独立运行模式]/集中式IRF设备：

**[diagnostic ondemand start slot**]* slot-number-list*\**[cpu***cpu-number * **test** *test-name* } [ **para** *parameters *]

分布式设备－]IRF模式：

**[diagnostic ondemand start chassis**]*chassis-number* **slot*** slot-number-list*\**[cpu***cpu-number * **test** *test-name* } [ **para** *parameters *]

【缺省情况】]

所有的按需类型测试例都需要用户手动启动。

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

**[slot **]*slot-number-list*：槽位号列表，表示同时执行多个单板的测试例。表示方式为*slot-number-list**=* *[slot-number* \**[to*** slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要执行的单板所在的槽位号。&\<1-7\>表示前面的参数最多可以输入7次。（分布式设备－独立运行模式）

**[slot **]*slot-number-list*：成员编号列表，表示同时执行多个成员设备的测试例。表示方式为*slot-number-list**=* *[slot-number* \**[to*** slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要执行的设备在IRF中的成员编号，&\<1-7\>表示前面的参数最多可以输入7次。（集中式IRF设备）（不支持IRF3的设备）

**[slot **]*slot-number-list*：成员编号/PEX虚拟槽位号列表，表示同时执行多个成员设备/PEX的测试例。表示方式为*slot-number-list**=* *[slot-number* \**[to*** slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要执行的设备在IRF中的成员编号或者PEX的虚拟槽位号，&\<1-7\>表示前面的参数最多可以输入7次。（集中式IRF设备）（支持IRF3的设备）

**[chassis **]*chassis-number*：表示需要执行测试例的设备在IRF中的成员编号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **]*chassis-number*：表示需要执行测试例的设备在IRF中的成员编号或者PEX对应的虚拟框号。（分布式设备－IRF模式）（支持IRF3的设备）

**[slot **]*slot-number-list*：槽位号列表，表示同时执行多个单板的测试例。表示方式为*slot-number-list**=* *[slot-number* \**[to*** slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要执行的单板所在的槽位号。&\<1-7\>表示前面的参数最多可以输入7次。（分布式设备－IRF模式）（不支持IRF3的设备）

**[slot **]*slot-number-list*：槽位号列表，表示同时执行多个单板/PEX的测试例。表示方式为*slot-number-list**=* *[slot-number* \**[to*** slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要执行的单板/PEX所在的槽位号，&\<1-7\>表示前面的参数最多可以输入7次。（分布式设备－IRF模式）（支持IRF3的设备）

*[test-name*]：指定测试例的名称，为1～31个字符的字符串，不区分大小写。

**[non-disruptive**]：执行所有的非破坏性的测试例。

**[para**]*parameters*：扩展参数，暂时无意义。

**[cpu**]*cpu-number*：表示指定CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】]

在设备维护过程中，用户可以手工启动某些测试例对设备进行诊断，这种诊断称为按需诊断。用于这种诊断的测试例称为按需诊断测试例。]

用户可以通过命令行配置按需诊断测试例重复执行的次数以及累计失败执行次数的最大值。当用户开启某测试例后，测试例在执行过程中，只要达到上述任意条件，则立即自动停止执行。]

【举例】]

\# ]启动破坏性按需诊断测试例PRBS。（集中式设备）

\<sysname\> diagnostic ondemand start test PRBS

Running test PRBS may disrupt system operation. Continue? [Y/N:y]

\# 启动1号单板上破坏性按需诊断测试例PRBS。（分布式设备－独立运行模式）

\<sysname\> diagnostic ondemand start slot 1 test PRBS

Running test PRBS on slot 1 may disrupt system operation. Continue? [Y/N:y]

\# 启动成员设备1上破坏性按需诊断测试例PRBS。（集中式IRF设备）

\<sysname\> diagnostic ondemand start slot 1 test PRBS

Running test PRBS on slot 1 may disrupt system operation. Continue? [Y/N:y]

\# 启动成员设备1的4号单板上破坏性按需诊断测试例PRBS。（分布式设备－IRF模式）

\<sysname\> diagnostic ondemand start chassis 1 slot 4 test PRBS

Running test PRBS on chassis 1 slot 4 may disrupt system operation. Continue? [Y/N:y]

\# 启动非破坏性按需诊断测试例。（集中式设备）

\<sysname\> diagnostic ondemand start test non-disruptive

\# 在1号单板上启动非破坏性按需诊断测试例。（分布式设备－独立运行模式）

\<sysname\> diagnostic ondemand start slot 1 test non-disruptive

\# 在成员设备1上启动非破坏性按需诊断测试例。（集中式IRF设备）

\<sysname\> diagnostic ondemand start slot 1 test non-disruptive

\# 在成员设备1的2号单板上启动非破坏性按需诊断测试例。（分布式设备－IRF模式）

\<sysname\> diagnostic ondemand start chassis 1 slot 2 test non-disruptive

【相关命令】

·**diagnostic ondemand fail****ure**

·**diagnostic ondemand repeating**

**GOLD \-- GOLD配置命令 \-- diagnostic ondemand stop**

------------------------------------------------------------------------

**[diagnostic ondemand stop**]命令用来停止指定按需类型诊断。

【命令】

集中式设备：

**[diagnostic ondemand stop test***test-name* }

分布式设备－独立运行模式]/集中式IRF设备：

**[diagnostic ondemand stop slot**]*slot-number-list*\**[cpu***cpu-number * **test** *test-name* }

分布式设备－]IRF模式：

**[diagnostic ondemand stop chassis**]*chassis-number* **slot*** slot-number-list*\**[cpu***cpu-number * **test** *test-name* }

【视图】]

用户视图

【缺省用户角色】

network-admin

【参数】

**[slot **]*slot-number-list*：槽位号列表，表示同时执行多个单板的测试例。表示方式为*slot-number-list**=* *[slot-number* \**[to*** slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要执行的单板所在的槽位号。&\<1-7\>表示前面的参数最多可以输入7次。（分布式设备－独立运行模式）

**[slot **]*slot-number-list*：成员编号列表，表示同时执行多个成员设备的测试例。表示方式为*slot-number-list**=* *[slot-number* \**[to*** slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要执行的设备在IRF中的成员编号，&\<1-7\>表示前面的参数最多可以输入7次。（集中式IRF设备）（不支持IRF3的设备）

**[slot **]*slot-number-list*：成员编号/PEX虚拟槽位号列表，表示同时执行多个成员设备/PEX的测试例。表示方式为*slot-number-list**=* *[slot-number* \**[to*** slot-number*  }&\<1-7\>]。其中，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号，&\<1-7\>表示前面的参数最多可以输入7次。（集中式IRF设备）（支持IRF3的设备）

**[chassis **]*chassis-number*：表示需要执行测试例的设备在IRF中的成员编号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **]*chassis-number*：表示需要执行测试例的设备在IRF中的成员编号或者PEX对应的虚拟框号。（分布式设备－IRF模式）（支持IRF3的设备）

**[slot **]*slot-number-list*：槽位号列表，表示同时执行多个单板的测试例。表示方式为*slot-number-list**=* *[slot-number* \**[to*** slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要执行的单板所在的槽位号。&\<1-7\>表示前面的参数最多可以输入7次。（分布式设备－IRF模式）（不支持IRF3的设备）

**[slot **]*slot-number-list*：槽位号列表，表示同时执行多个单板/PEX的测试例。表示方式为*slot-number-list**=* *[slot-number* \**[to*** slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要执行的单板/PEX所在的槽位号，&\<1-7\>表示前面的参数最多可以输入7次。（分布式设备－IRF模式）（支持IRF3的设备）

*[test-name*]：指定测试例的名称，为1～31个字符的字符串，不区分大小写。

**[non-disruptive**]：执行所有的非破坏性的测试例。

**[cpu**]*cpu-number*：表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】]

用户可以通过命令行配置按需诊断测试例重复执行的次数以及累计失败执行次数的最大值。当用户开启某测试例后，测试例在执行过程中，只要达到上述任意条件，则立即自动停止执行。]

【举例】]

\# ]手动停止执行非破坏性测试例。（集中式模式）

\<sysname\> diagnostic ondemand stop test non-disruptive]

\# 在1号单板上手动停止执行非破坏性测试例。（分布式设备－独立运行模式/集中式IRF设备）

\<sysname\> diagnostic ondemand stop slot 1 test non-disruptive

\# 在成员设备1上手动停止执行非破坏性测试例。（分布式设备－独立运行模式/集中式IRF设备）

\<sysname\> diagnostic ondemand stop slot 1 test non-disruptive

\# 在成员设备2的1号单板上手动停止执行非破坏性测试例。（分布式设备－IRF模式）

\<sysname\> diagnostic ondemand stop chassis 2 slot 1 test non-disruptive

【相关命令】

·**diagnostic ondemand fail****ure**

·**diagnostic ondemand repeating**

**GOLD \-- GOLD配置命令 \-- diagnostic simulation**

------------------------------------------------------------------------

**[diagnostic simulation**]命令用来设置诊断的执行方式为模拟方式。

**[undo diagnostic simulation**]命令用来恢复缺省情况。

【命令】

集中式设备：

**[diagnostic simulation test**]*test-name*[ { **failure** \| **random-failure** \| **success** }]

**[undo diagnostic simulation test **]*test-name*

分布式设备－独立运行模式/集中式IRF设备：

**[diagnostic simulation slot**]*slot-number-list *\**[cpu***cpu-number *]****test***test-name*[ { **failure** \| **random-failure** \| **success** }]

**[undo diagnostic simulation slot**]*slot-number-list *\**[cpu***cpu-number*  **test** ]*test-name*

分布式设备－IRF模式：

**[diagnostic simulation chassis **]*chassis-number ***slot*** slot-number-list* \**[cpu***cpu-number * **test** ]*test-name*[ { **failure** \| **random-failure** \| **success** }]

**[undo diagnostic simulation chassis **]*chassis-number* **slot** *slot-number-list* \**[cpu***cpu-number * **test** ]*test-name*

【缺省情况】

诊断为非模拟方式。即启动测试例后，系统会真正执行该测试例。

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

**[slot **]*slot-number-list*：槽位号列表，表示同时模拟多个单板的测试例。表示方式为*slot-number-list**=* *[slot-number* \**[to*** slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要模拟的单板所在的槽位号。&\<1-7\>表示前面的参数最多可以输入7次。（分布式设备－独立运行模式）

**[slot **]*slot-number-list*：成员编号列表，表示同时模拟多个成员设备的测试例。表示方式为*slot-number-list**=* *[slot-number* \**[to*** slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要模拟的设备在IRF中的成员编号，&\<1-7\>表示前面的参数最多可以输入7次。（集中式IRF设备）（不支持IRF3的设备）

**[slot **]*slot-number-list*：成员编号/PEX虚拟槽位号列表，表示同时模拟多个成员设备/PEX的测试例。表示方式为*slot-number-list**=* *[slot-number* \**[to*** slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要模拟的设备在IRF中的成员编号或者PEX的虚拟槽位号，&\<1-7\>表示前面的参数最多可以输入7次。（集中式IRF设备）（支持IRF3的设备）

**[chassis **]*chassis-number*：表示需要模拟测试例的设备在IRF中的成员编号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **]*chassis-number*：表示需要模拟测试例的设备在IRF中的成员编号或者PEX对应的虚拟框号。（分布式设备－IRF模式）（支持IRF3的设备）

**[slot **]*slot-number-list*：槽位号列表，表示同时模拟多个单板的测试例。表示方式为*slot-number-list**=* *[slot-number* \**[to*** slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要模拟的单板所在的槽位号。&\<1-7\>表示前面的参数最多可以输入7次。（分布式设备－IRF模式）（不支持IRF3的设备）

**[slot **]*slot-number-list*：槽位号列表，表示同时模拟多个单板/PEX的测试例。表示方式为*slot-number-list**=* *[slot-number* \**[to*** slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要模拟的单板/PEX所在的槽位号，&\<1-7\>表示前面的参数最多可以输入7次。（分布式设备－IRF模式）（支持IRF3的设备）

*[test-name*]：指定进行模拟诊断的测试例名称，为1～31个字符的字符串，不区分大小写。

**[failure**]：假设模拟执行测试例失败，此时将输出测试失败的结果。

**[random-failure**]：表示随机选择模拟执行测试例的结果是成功还是失败。

**[success**]：假设模拟执行测试例成功，此时将输出测试成功的结果。

**[cpu**]*cpu-number*：表示指定CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】]

配置该命令后，当测试例满足执行条件时，在执行测试例的时候就直接生成测试结果，并不真正执行测试例，也不会触发硬件纠正行为。该功能用于判断]GOLD模块框架功能是否正常。

只有监控诊断测试例和按需诊断测试例支持该命令，启动诊断测试例不支持该命令。]

【举例】]

\# ]配置HGMonitor模拟诊断失败。（集中式设备）

\<sysname\> diagnostic simulation test HGMonitor failure

\# 配置1号单板上的HGMonitor模拟诊断失败。（分布式设备－独立运行模式）

\<sysname\> diagnostic simulation slot 1 test HGMonitor failure

\# 配置成员设备1上的HGMonitor模拟诊断失败。（集中式IRF设备）

\<sysname\> diagnostic simulation slot 1 test HGMonitor failure

\# 配置成员设备1的1号单板上的HGMonitor模拟诊断失败。（分布式设备－IRF模式）

\<sysname\> diagnostic simulation chassis 1 slot 1 test HGMonitor failure

【相关命令】

·**display diagnostic simulation**

**GOLD \-- GOLD配置命令 \-- display diagnostic bootup**

------------------------------------------------------------------------

**[display diagnostic bootup**]命令用来显示启动诊断测试例。

【命令】

集中式设备：

**[display diagnostic bootup ** **test** ]*test-name*

分布式设备－独立运行模式/集中式IRF设备：

**[display diagnostic bootup** [ **slot** ]*slot-number* \**[cpu***cpu-number*   **test** *test-name * ]]

分布式设备－IRF模式：

**[display diagnostic bootup ** **chassis** ]*chassis-number * **slot** *slot-number* \**[cpu***cpu-number*   **test** *test-name*  ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

【参数】

**[slot **]*slot-number*：表示单板所在的槽位号。不指定该参数时，显示所有单板上测试例的执行结果。（分布式设备－独立运行模式）

**[slot **]*slot-number*：表示设备在IRF中的成员编号。不指定该参数时，显示所有成员设备上测试例的执行结果。（集中式IRF设备）（不支持IRF3的设备）

**[slot **]*slot-number*：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，显示所有成员设备/PEX上测试例的执行结果。（集中式IRF设备）（支持IRF3的设备）

**[chassis **]*chassis-number*** slot ***slot-number*：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定**chassis**时，显示所有成员设备/虚拟设备上测试例的诊断结果。指定**chassis**不指定**slot**参数时，显示指定成员设备所有单板或者指定虚拟设备所有PEX上测试例的执行结果。（分布式设备－IRF模式）（不支持IRF3的设备）

**[test **]*test-name*：指定测试例的名称，为1～31个字符的字符串，不区分大小写。不指定该参数时，表示设备上的所有测试例。（集中式设备）

**[test **]*test-name*：指定测试例的名称，为1～31个字符的字符串，不区分大小写。不指定该参数时，表示指定单板上的所有测试例。（分布式设备－独立运行模式/分布式设备－IRF模式）

**[test **]*test-name*：指定测试例的名称，为1～31个字符的字符串，不区分大小写。不指定该参数时，表示指定成员设备上的所有测试例。（集中式IRF设备）

**[cpu**]*cpu-number*：表示指定CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示启动诊断测试例OnlyBootUp的信息。（集中式设备）

\<Sysname\> display diagnostic bootup test OnlyBootUp

Test name                : OnlyBootUp

ExtPara                  : 123

State                    : Enabled

\# 显示0号单板上启动诊断测试例OnlyBootUp的信息。（分布式设备－独立运行模式）

\<Sysname\> display diagnostic bootup slot 0

slot 0:

  Test name                : OnlyBootUp

  ExtPara                  : 123

  State                    : Enabled

\# 显示成员设备1上启动诊断测试例的信息。（集中式IRF设备）

\<Sysname\> display diagnostic bootup slot 1

slot 1:

  Test name                : OnlyBootUp

  ExtPara                  : 123

  State                    : Enabled

\# 显示成员设备1的0号单板上启动诊断测试例的信息。（分布式设备－IRF模式）

\<Sysname\> display diagnostic bootup chassis 1 slot 0

Chassis 1 slot 0:

  Test name                : OnlyBootUp

  ExtPara                  : 123

  State                    : Enabled

【相关命令】

·**diagnostic bootup ****enable test**

**GOLD \-- GOLD配置命令 \-- display diagnostic bootup level**

------------------------------------------------------------------------

**[display diagnostic bootup level**]命令用来显示设备本次启动时生效的启动诊断的级别。

【命令】

**[display diagnostic bootup level**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

【举例】

\# 显示设备本次启动时生效的启动诊断的级别。

\<sysname\> display diagnostic bootup level

Current bootup diagnostic level: complete

【相关命令】

·**diagnostic bootup level **

**GOLD \-- GOLD配置命令 \-- display diagnostic content**

------------------------------------------------------------------------

**[display diagnostic content**]命令用来显示测试例的内容。

【命令】

集中式设备：

**[display diagnostic content** [ **verbose** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display diagnostic content** [ **slot** ]*slot-number* \**[cpu***cpu-number*  ]  **verbose** ]

分布式设备－IRF模式：

**[display diagnostic content** **chassis** ]*chassis-number* **slot** *slot-number*\**[cpu***cpu-number*  ]   **verbose**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

【参数】

**[slot **]*slot-number*：表示单板所在的槽位号。不指定时，显示所有板的测试例内容。（分布式设备－独立运行模式）

**[slot **]*slot-number*：表示设备在IRF中的成员编号。不指定时，显示所有设备的测试例内容。（集中式IRF设备）（不支持IRF3的设备）

**[slot **]*slot-number*：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定时，显示所有设备/PEX的测试例内容。（集中式IRF设备）（支持IRF3的设备）

**[chassis **]*chassis-number***** **slot** *slot-number *：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定**chassis**时，显示所有诊断结果。指定**chassis**未指定槽位号时，显示指定设备所有单板的测试例内容。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **]*chassis-number***** **slot** *slot-number *：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定**chassis**时，显示所有诊断结果。指定**chassis**未指定槽位号时，显示指定设备所有单板/PEX的测试例内容。（分布式设备－IRF模式）（支持IRF3的设备）

**[verbose**]：显示测试例的详细信息；不指定该参数时，显示测试例的简要信息。

**[cpu**]*cpu-number*：表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示诊断测试例的简要信息。（集中式设备）

\<sysname\> display diagnostic content

Diagnostic test suite attributes:

#B/\*: Bootup test/NA

#O/\*: Ondemand test/NA

#M/\*: Monitoring test/NA

#D/\*: [Disruptive test/Non-disruptive test]

#P/\*: Per port test[/NA]

#A/I/\*: Monitoring test is active/Monitoring test is inactive/NA

Name                      Attributes              Interval

HGMonitor{.TerminalDisplayChar}\*\*M\*PI{.TerminalDisplayChar}00:00:10{.TerminalDisplayChar}

BoardSteady               B\*\*\*\*\*                  -NA-

\# 显示1号单板上诊断测试例的简要信息。（分布式设备－独立运行模式）

\<sysname\> display diagnostic content slot 1

Diagnostic test suite attributes:

#B/\*: Bootup test/NA

#O/\*: Ondemand test/NA

#M/\*: Monitoring test/NA

#D/\*: Disruptive test/Non-disruptive test

#P/\*: Per port test/NA

#A/I/\*: Monitoring test is active/Monitoring test is inactive/NA

Slot 1 cpu 0:

Name                      Attributes              Interval

HGMonitor{.TerminalDisplayChar}\*\*M\*PI{.TerminalDisplayChar}00:00:10{.TerminalDisplayChar}

BoardSteady               B\*\*\*\*\*                  -NA-

\# 显示成员设备1上诊断测试例的简要信息。（集中式IRF设备）

\<sysname\> display diagnostic content slot 1

Diagnostic test suite attributes:

#B/\*: Bootup test/NA

#O/\*: Ondemand test/NA

#M/\*: Monitoring test/NA

#D/\*: Disruptive test/Non-disruptive test

#P/\*: Per port test/NA

#A/I/\*: Monitoring test is active/Monitoring test is inactive/NA

Slot 1 cpu 0:

Name                      Attributes              Interval

HGMonitor{.TerminalDisplayChar}\*\*M\*PI{.TerminalDisplayChar}00:00:10{.TerminalDisplayChar}

BoardSteady               B\*\*\*\*\*                  -NA-

\# 显示成员设备1的1号单板上诊断测试例的简要信息。（分布式设备－IRF模式）

\<sysname\> display diagnostic content chassis 1 slot 1

Diagnostic test suite attributes:

#B/\*: Bootup test/NA

#O/\*: Ondemand test/NA

#M/\*: Monitoring test/NA

#D/\*: Disruptive test/Non-disruptive test

#P/\*: Per port test/NA

#A/I/\*: Monitoring test is active/Monitoring test is inactive/NA

Chassis 1 slot 1 cpu 0:

Name                      Attributes              Interval

HGMonitor{.TerminalDisplayChar}\*\*M\*PI{.TerminalDisplayChar}00:00:10{.TerminalDisplayChar}

BoardSteady               B\*\*\*\*\*                  -NA-

\# 显示诊断测试例的详细信息。（集中式设备）

\<sysname\> display diagnostic content verbose

Diagnostic test suite attributes:

#B/\*: Bootup test/NA

#O/\*: Ondemand test/NA

#M/\*: Monitoring test/NA

#D/\*: Disruptive test/Non-disruptive test

#P/\*: Per port test/NA

#A/I/\*: Monitoring test is active/Monitoring test is inactive/NA

Test name        : HGMonitor

Test attributes  : \*\*M\*PI

Test interval    : 00:00:10

Min interval     : 00:00:10

Correct-action   : -NA-

Description       : A Real-time test, disabled by default that checks link status between ports.

Test name        : BoardSteady

Test attributes  : B\*\*\*\*\*

Test interval    : -NA-

Min interval     : -NA-

Correct-action   : Offline.

Description       : A bootup test, to check if the board is steady inserted. If the board is not steady inserted, the board will be offline.

\# 显示1号单板上诊断测试例的详细信息。（分布式设备－独立运行模式）

\<sysname\> display diagnostic content slot 1 verbose

Diagnostic test suite attributes:

#B/\*: Bootup test/NA

#O/\*: Ondemand test/NA

#M/\*: Monitoring test/NA

#D/\*: Disruptive test/Non-disruptive test

#P/\*: Per port test/NA

#A/I/\*: Monitoring test is active/Monitoring test is inactive/NA

Slot 1 cpu 0:

Test name        : HGMonitor

Test attributes  : \*\*M\*PI

Test interval    : 00:00:10

Min interval     : 00:00:10

Correct-action   : -NA-

Description       : A Real-time test, disabled by default that checks link status between ports.

Test name        : BoardSteady

Test attributes  : B\*\*\*\*\*

Test interval    : -NA-

Min interval     : -NA-

Correct-action   : Offline.

Description       : A bootup test, to check if the board is steady inserted. If the board is not steady inserted, the board will be offline.

\# 显示成员设备1上诊断测试例的详细信息。（集中式IRF设备）

\<sysname\> display diagnostic content slot 1 verbose

Diagnostic test suite attributes:

#B/\*: Bootup test/NA

#O/\*: Ondemand test/NA

#M/\*: Monitoring test/NA

#D/\*: Disruptive test/Non-disruptive test

#P/\*: Per port test/NA

#A/I/\*: Monitoring test is active/Monitoring test is inactive/NA

slot 1 cpu 0:

Test name        : HGMonitor

Test attributes  : \*\*M\*PI

Test interval    : 00:00:10

Min interval     : 00:00:10

Correct-action   : -NA-

Description      : A real-time test that checks HG channel status, disabled by default.

Test name        : BoardSteady

Test attributes  : B\*\*\*\*\*

Test interval    : -NA-

Min interval     : -NA-

Correct-action   : Offline.

Description       : A bootup test, to check if the board is steady inserted. If the board is not steady inserted, the board will be offline.

\# 显示成员设备1的1号单板上诊断测试例的详细信息。（分布式设备－IRF模式）

\<sysname\> display diagnostic content chassis 1 slot 1 verbose

Diagnostic test suite attributes:

#B/\*: Bootup test/NA

#O/\*: Ondemand test/NA

#M/\*: Monitoring test/NA

#D/\*: Disruptive test/Non-disruptive test

#P/\*: Per port test/NA

#A/I/\*: Monitoring test is active/Monitoring test is inactive/NA

Chassis 1 slot 1 cpu 0:

Test name        : HGMonitor

Test attributes  : \*\*M\*PI

Test interval    : 00:00:10

Min interval     : 00:00:10

Correct-action   : -NA-

Description       : A real-time test that checks HG channel status, disabled by default.

Test name        : BoardSteady

Test attributes  : B\*\*\*\*\*

Test interval    : -NA-

Min interval     : -NA-

Correct-action   : Offline.

Description       : A bootup test, to check if the board is steady inserted. If the board is not steady inserted, the board will be offline.

表1-1 display diagnostic content命令显示信息描述表

字段

描述

B/\*

启动诊断测试例/非启动诊断测试例

O/\*

按需诊断测试例/非按需诊断测试例

M/\*

监控诊断测试例/非监控诊断测试例

D/\*

破坏性测试例/非破坏性测试例

P/\*

端口相关的测试例/不是端口相关的测试例

A/I/\*

使能的监控诊断测试例/未使能的监控诊断测试例/非监控诊断测试例

Slot 1 cpu 0

显示指定CPU上测试例的内容（分布式设备－独立运行模式/集中式IRF设备）

Chassis 1 slot 1 cpu 0

显示指定CPU上测试例的内容（分布式设备－IRF模式）

Test name

测试例的名称

Test attributes

测试例的属性。从左到右依次为是否为启动诊断测试例，是否为按需诊断测试例，是否为监控诊断测试例，是否是破坏性测试例，是否是端口都相关的测试例，是否使能，对于不相关的属性用"\*"表示

Test interval

执行监控测试例的时间间隔，没有时间间隔用"-NA-"表示

Min interval

执行监控测试例允许的最小时间间隔，没有最小时间间隔用"-NA-"表示

Correct-action

测试失败时的触发动作

Description

测试例的描述信息

**GOLD \-- GOLD配置命令 \-- display diagnostic event-log**

------------------------------------------------------------------------

**[display diagnostic event-log**]命令用来显示GOLD日志的信息。

【命令】

**[display diagnostic event-log **[[ **error** \| **info** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

【参数】

**[error**]：显示所有错误相关的GOLD日志信息。

**[info**]**：**显示所有非错误的GOLD日志信息

【使用指导】

不指定**error**和**info**参数时，显示所有GOLD日志的信息。

系统在执行完诊断测试例后，会产生GOLD日志用于记录测试例相关执行情况，日志内容包括测试例的名称、执行时间、执行结果、失败原因等信息。由于所有测试例在执行过程都会产生日志，因此GOLD日志会较多，为了不影响信息中心的性能，GOLD日志独立存储和显示，不会发往信息中心统一处理。

设备重启或主备倒换后，GOLD日志会全部被清除掉。

【举例】

\# 显示所有GOLD日志的信息。（分布式设备－IRF模式）

\<sysname\> display diagnostic event-log

Event: E_INFO, Wed Jan  7 11:39:53:314 2012, -Chassis=4-Slot=2-Cpu=0 TestName-\>SystemMgmtBus, Event_INFO: Result-\>Success.

Event: E_ERROR, Wed Jan  7 11:39:53:314 2012, -Chassis=4-Slot=2-Cpu=0 [TestName-\>SystemMgmtBus, Event_INFO: Result-\>Failure Reason-\>The port 9 is offline.{.TerminalDisplayChar}]

\# 显示所有错误相关的GOLD日志的信息。（分布式设备－IRF模式）

\<sysname\> display diagnostic event-log error

Event: E_ERROR, Wed Jan  7 11:39:53:314 2012, -Chassis=4-Slot=2-Cpu=0 TestName-\>SystemMgmtBus, Event_INFO: Result-\>Failure Reason-\>The port 9 is offline.

\# 显示所有非错误的GOLD日志的信息。（分布式设备－IRF模式）

\<sysname\> display diagnostic event-log info

Event: E_INFO, Wed Jan  7 11:39:53:314 2012, -Chassis=4-Slot=2-Cpu=0 TestName-\>SystemMgmtBus, Event_INFO: Result-\>Success.

**GOLD \-- GOLD配置命令 \-- display diagnostic ondemand configuration**

------------------------------------------------------------------------

**[display diagnostic ondemand configuration**]命令用来显示按需诊断的配置信息。

【命令】

**[display diagnostic ondemand configuration**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

【举例】

\# 配置了重复执行次数与失败次数，显示按需诊断配置信息。

\<sysname\> display diagnostic ondemand configuration

Maximum test-repeating times: 4

Maximum test-failure times: 1

\# 只配置了重复执行次数，显示按需诊断配置信息。

\<sysname\> display diagnostic ondemand configuration

Maximum test-repeating times: 4

Maximum test-failure times: Not configured

【相关命令】

·**diagnostic ondemand fail****ure**

·**diagnostic ondemand repeating**

**GOLD \-- GOLD配置命令 \-- display diagnostic result**

------------------------------------------------------------------------

**[display diagnostic result**]命令用来显示测试例的执行结果。

【命令】

集中式设备：

**[display diagnostic result ** **test** ]*test-name*   **verbose**

分布式设备－独立运行模式/集中式IRF设备：

**[display diagnostic result** [ **slot** ]*slot-number* [ **test** *test-name *\**[cpu***cpu-number*  ] ]  **verbose** ]

分布式设备－IRF模式：

**[display diagnostic result ** **chassis** ]*chassis-number * **slot** *slot-number* \**[cpu***cpu-number*   **test** *test-name*  ]   **verbose**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

【参数】

**[slot **]*slot-number*：表示单板所在的槽位号。不指定该参数时，显示所有单板上测试例的执行结果。（分布式设备－独立运行模式）

**[slot **]*slot-number*：表示设备在IRF中的成员编号。不指定该参数时，显示所有成员设备上测试例的执行结果。（集中式IRF设备）（不支持IRF3的设备）

**[slot **]*slot-number*：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，显示所有成员设备/PEX上测试例的执行结果。（集中式IRF设备）（支持IRF3的设备）

**[chassis **]*chassis-number*** slot ***slot-number*：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定**chassis**时，显示所有成员设备上测试例的诊断结果。指定**chassis**不指定**slot**参数时，显示指定成员设备所有单板上测试例的执行结果。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **]*chassis-number*** slot ***slot-number*：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定**chassis**时，显示所有测试例的诊断结果。指定**chassis**不指定**slot**参数时，显示指定成员设备所有单板/PEX上测试例的执行结果。（分布式设备－IRF模式）（支持IRF3的设备）

**[test **]*test-name*：指定测试例的名称，为1～31个字符的字符串，不区分大小写。不指定该参数时，表示设备上的所有测试例。（集中式设备）

**[test **]*test-name*：指定测试例的名称，为1～31个字符的字符串，不区分大小写。不指定该参数时，表示指定单板上的所有测试例。（分布式设备－独立运行模式/分布式设备－IRF模式）

**[test **]*test-name*：指定测试例的名称，为1～31个字符的字符串，不区分大小写。不指定该参数时，表示指定成员设备上的所有测试例。（集中式IRF设备）

**[verbose**]：显示当前处于使能状态的测试例或者累计执行次数大于0的测试例执行结果的详细信息，不包括统计信息。不指定该参数时，只显示累计执行次数大于0的测试例执行结果的简要信息。

**[cpu**]*cpu-number*：表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示设备中所有测试例的简要诊断结果。（集中式设备）

\<sysname\> display diagnostic result

  Name                    Run count    Failure count    Last result

  HGMonitor               10           3                Failure

  SystemMgmtBus           10           0                Success

\# 显示1号单板上所有测试例的简要诊断结果。（分布式设备－独立运行模式）

\<sysname\> display diagnostic result slot 1

Slot 1 cpu 0：

  Name                    Run count    Failure count    Last result

  HGMonitor               10           3                Failure

  SystemMgmtBus           10           0                Success

\# 显示成员设备1上所有测试例的简要诊断结果。（集中式IRF设备）

\<sysname\> display diagnostic result slot 1

Slot 1 cpu 0：

  Name                    Run count    Failure count    Last result

  HGMonitor               10           3                Failure

  SystemMgmtBus           10           0                Success

\# 显示成员设备1中1号单板上所有测试例的简要诊断结果。（分布式设备－IRF模式）

\<sysname\> display diagnostic result chassis 1 slot 1

Chassis 1 slot 1 cpu 0：

  Name                    Run count    Failure count    Last result

  HGMonitor               10           3                Failure

  SystemMgmtBus           10           0                Success

\# 显示所有测试例的详细诊断结果[（分布式设备－独立运行模式]/集中式IRF设备）

\<sysname\> display diagnostic result verbose

Slot 1 cpu 0:

  Test name                : HGMonitor

  Total run count          : 10

  Total failure count      : 3

  Consecutive failure count: 3

  Last execution time      : Tue Oct 30 10:36:55 2012

  First failure time       : Tue Oct 30 10:36:25 2012

  Last failure time        : Tue Oct 30 10:36:55 2012

  Last pass time           : Tue Oct 30 10:36:15 2012

  Last execution result    : Failure

  Last failure reason      : Failed to send packets.

  Next execution time      : Tue Oct 30 10:37:05 2012

  Port link status : error

  Src-Slot Unit      Port      Dest-Slot

  8        20        3         14

  8        23        5         14

  6        10        3         14

  14       3         13        7

  Test name                : SystemMgmtBus

  Total run count          : 10

  Total failure count      : 0

  Consecutive failure count: 0

  Last execution time      : Tue Oct 30 10:36:55 2012

  First failure time       : -NA-

  Last failure time        : -NA-

  Last pass time           : Tue Oct 30 10:36:55 2012

  Last execution result    : Success

  Last failure reason      : -NA-

  Next execution time      : -NA-

表1-2 display diagnostic result命令显示信息描述表

字段

描述

Slot 1 cpu 0

指定CPU上测试例的执行结果（分布式设备－独立运行模式/集中式IRF设备）

Chassis 1 slot 1 cpu 0：

指定CPU上测试例的执行结果（分布式设备－IRF模式）

Test name

测试例的名称

Total run count

诊断执行的总次数

Total failure count

诊断失败的总次数

Consecutive failure count

连续执行测试例失败的次数

Last execution time

最近一次测试执行的时间

First failure time

第一次诊断失败的时间。如果没有失败的测试例，此字段内容为-NA-

Last failure time

最近一次诊断失败的时间。如果没有失败的测试例，此字段内容为-NA-

Last pass time

最近一次诊断成功的时间。如果没有成功的测试例，此字段内容为-NA-

Last execution result

最近一次诊断结果

Last failure reason

最近一次诊断失败的原因。当用户配置模拟失败时，此字段内容即为Simulated Test；当诊断未失败时，此字段内容即为-NA-

Next execution time

下次诊断执行的时间。如果是监控诊断类型的测试例，下次执行时间为最后一次测试执行时间加上测试例的时间间隔；如果是按需诊断和启动诊断类型的测试例，则此字段的内容为-NA-

**GOLD \-- GOLD配置命令 \-- display diagnostic result statistics**

------------------------------------------------------------------------

**[display diagnostic result statistics**]命令用来显示与报文相关的测试例的统计信息。

【命令】

集中式设备：

**[display diagnostic result** [ **test** ]*test-name * **statistics**]

分布式设备－独立运行模式/集中式IRF设备：

**[display diagnostic result** [ **slot** ]*slot-number* \**[cpu***cpu-number*   **test** *test-name*  ] **statistics**]

分布式设备－IRF模式：

**[display diagnostic result ** **chassis** ]*chassis-number * **slot** *slot-number* \**[cpu***cpu-number*   **test** *test-name*  ]  **statistics**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

【参数】

**[slot **]*slot-number*：表示单板所在的槽位号。不指定该参数时，显示所有单板上与报文相关的测试例的统计信息。（分布式设备－独立运行模式）

**[slot **]*slot-number*：表示设备在IRF中的成员编号。不指定该参数时，显示所有成员设备上与报文相关的测试例的统计信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot **]*slot-number*：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，显示所有成员设备/PEX上测试例的执行结果。（集中式IRF设备）（支持IRF3的设备）

**[chassis **]*chassis-number*** slot ***slot-number*：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定**chassis**时，显示所有成员设备上与报文相关的测试例的统计信息。指定**chassis**不指定**slot**参数时，显示指定成员设备所有单板上与报文相关的测试例的统计信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **]*chassis-number*** slot ***slot-number*：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定**chassis**时，显示与报文相关的所有测试例的统计信息。指定**chassis**不指定**slot**参数时，显示指定成员设备所有单板/PEX上与报文相关的测试例的统计信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[test **]*test-name*：指定测试例的名称，为1～31个字符的字符串，不区分大小写。不指定该参数时，表示设备上的所有测试例。（集中式设备）

**[test **]*test-name*：指定测试例的名称，为1～31个字符的字符串，不区分大小写。不指定该参数时，表示指定单板上的所有测试例。（分布式设备－独立运行模式/分布式设备－IRF模式）

**[test **]*test-name*：指定测试例的名称，为1～31个字符的字符串，不区分大小写。不指定该参数时，表示指定成员设备上的所有测试例。（集中式IRF设备）

**[cpu**]*cpu-number*：表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示设备中PortLoopback执行后的统计结果。（集中式设备）

\<sysname\> display diagnostic result test PortLoopback statistics

  Test name: PortLoopback

  Port    Packets sent    Packets received   Packets lost

  1       0               0                  0

  2       0               0                  0

  3       0               0                  0

  4       4               4                  0

  5       4               4                  0

  6       4               4                  0

  7       4               4                  0

  8       0               0                  0

\# 显示1号单板上的PortLoopback执行后的统计结果。（分布式设备－独立运行模式）

\<sysname\> display diagnostic result slot 1 test PortLoopback statistics

Slot 1 cpu 0:

  Test name: PortLoopback

  Port    Packets sent    Packets received   Packets lost

  1       0               0                  0

  2       0               0                  0

  3       0               0                  0

  4       4               4                  0

  5       4               4                  0

  6       4               4                  0

  7       4               4                  0

  8       0               0                  0

\# 显示成员设备1上的PortLoopback执行后的统计结果。（集中式IRF设备）

\<sysname\> display diagnostic result slot 1 test PortLoopback statistics

Slot 1 cpu 0:

  Test name: PortLoopback

  Port    Packets sent    Packets received   Packets lost

  1       0               0                  0

  2       0               0                  0

  3       0               0                  0

  4       4               4                  0

  5       4               4                  0

  6       4               4                  0

  7       4               4                  0

  8       0               0                  0

\# 显示成员设备1中单板1上的PortLoopback执行后的统计结果。（分布式设备－IRF模式）

\<sysname\> display diagnostic result chassis 1 slot 1 test PortLoopback statistics

Chassis 1 slot 1 cpu 0:

  Test name: PortLoopback

  Port    Packets sent    Packets received   Packets lost

  1       0               0                  0

  2       0               0                  0

  3       0               0                  0

  4       4               4                  0

  5       4               4                  0

  6       4               4                  0

  7       4               4                  0

  8       0               0                  0

表1-3 display diagnostic result statistics命令显示信息描述表

字段

描述

Slot 1 cpu 0

指定CPU上与报文相关的测试例的统计信息（分布式设备－独立运行模式/集中式IRF设备）

Chassis 1 slot 1 cpu 0：

指定CPU上与报文相关的测试例的统计信息（分布式设备－IRF模式）

Test name

测试例的名称

Port

端口号

Packets sent

已发送数据包

Packets received

已接收数据包

Packets lost

丢失的数据包

**GOLD \-- GOLD配置命令 \-- display diagnostic simulation**

------------------------------------------------------------------------

**[display diagnostic simulation**]命令用来显示模拟诊断的配置信息。

【命令】

集中式设备：

**[display diagnostic simulation**]

分布式设备－独立运行模式/集中式IRF设备：

**[display diagnostic simulation ** **slot** ]*slot-number*\**[cpu***cpu-number*  ]

分布式设备－IRF模式：

**[display diagnostic simulation ** **chassis** ]*chassis-number * **slot** *slot-number*\**[cpu***cpu-number*  ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

【参数】

**[slot **]*slot-number*：表示单板所在的槽位号。不指定该参数时，显示所有板的模拟诊断配置。（分布式设备－独立运行模式）

**[slot **]*slot-number*：表示设备在IRF中的成员编号。不指定该参数时，显示所有设备的模拟诊断配置。（集中式IRF设备）（不支持IRF3的设备）

**[slot **]*slot-number*：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，显示所有设备的模拟诊断配置。（集中式IRF设备）（支持IRF3的设备）

**[chassis **]*chassis-number***** **slot** *slot-number *：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定**chassis**时，显示所有设备的模拟诊断配置。指定**chassis**未指定槽位号时，显示指定设备所有板的模拟诊断配置。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **]*chassis-number***** **slot** *slot-number *：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定**chassis**时，显示所有设备的模拟诊断配置。指定**chassis**未指定槽位号时，显示指定设备所有板/PEX的模拟诊断配置。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu**]*cpu-number*：表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

该命令用来显示模拟诊断的配置信息。如果指定的槽号上没有配置模拟诊断，则不显示任何内容。

【举例】

\# 显示设备上配置的模拟诊断配置信息。（集中式设备）

\<sysname\> diagnostic simulation test HGMonitor failure

\<sysname\> display diagnostic simulation

  Name                            Mode

  HGMonitor                       failure

\# 显示1号单板上配置的模拟诊断配置信息。（分布式设备－独立运行模式）

\<sysname\> diagnostic simulation slot 1 test HGMonitor failure

\<sysname\> display diagnostic simulation slot 1

Slot 1 cpu 0:

Name                            Mode

HGMonitor                       failure

\# 显示1号单板上配置的模拟诊断配置信息。（分布式设备－IRF模式）

\<sysname\> diagnostic simulation chassis 1 slot 1 test HGMonitor failure

\<sysname\> display diagnostic simulation chassis 1 slot 1

Chassis 1 slot 1 cpu 0:

  Name                            Mode

  HGMonitor                       failure

【相关命令】

·**diagnostic simulation**

**GOLD \-- GOLD配置命令 \-- reset diagnostic event-log**

------------------------------------------------------------------------

**[reset diagnostic event-log**]命令用来清除GOLD日志。

【命令】

**[reset diagnostic event-log**]

【视图】

用户视图

【缺省用户角色】

network-admin

【举例】

\# 清除GOLD日志。

\<sysname\> reset diagnostic event-log

【相关命令】

·**display diagnostic ****event-log**

**GOLD \-- GOLD配置命令 \-- reset diagnostic result**

------------------------------------------------------------------------

**[reset diagnostic result**]命令用来清除诊断测试结果。

【命令】

集中式设备：

**[reset diagnostic result ** **test** ]*test-name*

分布式设备－独立运行模式/集中式IRF设备：

**[reset diagnostic result ** **slot** ]*slot-number *\**[cpu***cpu-number *]** **test** *test-name*

分布式设备－IRF模式：

**[reset diagnostic result ** **chassis**]* chassis-number*****\**[slot ***slot-number *\**[cpu***cpu-number *  **test** *test-name*  ] ]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

**[slot **]*slot-number*：表示单板所在的槽位号。不指定该参数时，清除所有板的结果。（分布式设备－独立运行模式）

**[slot **]*slot-number*：表示设备在IRF中的成员编号。不指定该参数时，清除所有设备的结果。（集中式-IRF设备）（不支持IRF3的设备）

**[slot **]*slot-number*：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，清除所有设备/PEX的结果。（集中式IRF设备）（支持IRF3的设备）

**[chassis **]*chassis-number***** **slot** *slot-number* ：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定**chassis**时，清除所有设备的结果。指定**chassis**未指定槽位号时，清除指定设备所有板的结果。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **]*chassis-number***** **slot** *slot-number* ：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定**chassis**时，清除所有设备的结果。指定**chassis**未指定槽位号时，清除指定设备所有板/PEX的结果。（分布式设备－IRF模式）（支持IRF3的设备）

**[test **]*test-name*：指定测试例的名称，为1～31个字符的字符串，不区分大小写。不指定该参数时，表示设备上的所有测试例。（集中式设备）

**[test **]*test-name*：指定测试例的名称，为1～31个字符的字符串，不区分大小写。不指定该参数时，表示指定单板上的所有测试例。（分布式设备－独立运行模式/分布式设备－IRF模式）

**[test **]*test-name*：指定测试例的名称，为1～31个字符的字符串，不区分大小写。不指定该参数时，表示指定成员设备上的所有测试例。（集中式IRF设备）

**[cpu**]*cpu-number*：表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

本命令清除测试结果时，不会清除详细诊断结果中的下次诊断执行时间。

【举例】

\# 清除HGMonitor的测试结果。（集中式设备）

\<sysname\> reset diagnostic result test HGMonitor

\# 清除1号单板上HGMonitor的测试结果。（分布式设备－独立运行模式）

\<sysname\> reset diagnostic result slot 1 test HGMonitor

\# 清除成员设备1上HGMonitor的测试结果。（集中式IRF设备）

\<sysname\> reset diagnostic result slot 1 test HGMonitor

\# 清除成员设备1的1号单板上HGMonitor的测试结果。（分布式设备－IRF模式）

\<sysname\> reset diagnostic result chassis 1 slot 1 test HGMonitor

【相关命令】

·**display diagnostic result**
