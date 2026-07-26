::: {#835817746 .myid}
[]{#_Toc404796063}[]{#struct_0_32528_11019_x1056877652}[]{#_Toc378323381}

**备份组 \-- 备份组配置命令 \-- bind**

------------------------------------------------------------------------

[**[bind]{lang="EN-US"}**]{#struct_0_32528_11019_1551711065}[命令用来将节点加入备份组。]{style="font-family:宋体"}

[**[undo bind]{lang="EN-US"}**]{#struct_0_32528_11019_2042015758}[命令用来删除备份组内的节点。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_32528_11019_x1926600522}

[[分布式设备－独立运行模式：]{style="font-family:宋体"}]{#struct_0_32528_11019_1444625637}

[**[bind slot ]{lang="EN-US"}***[slot-number ]{lang="EN-US"}***[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*[ { **primary** \| **secondary** }]{lang="EN-US"}]{#struct_0_32528_11019_x78912064}

[**[undo bind slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_32528_11019_x1128577950}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_32528_11019_x1520839052}[模式：]{style="font-family:宋体"}

[**[bind chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number* **cpu** *cpu-number* { **primary** \| **secondary** }]{lang="EN-US"}]{#struct_0_32528_11019_1524099407}

[**[undo bind chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number* **cpu** *cpu-number*]{lang="EN-US"}]{#struct_0_32528_11019_x1254404782}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_32528_11019_x1458697441}

[[备份组下没有任何节点。]{style="font-family:宋体"}]{#struct_0_32528_11019_x1757571150}

[[【视图】]{style="font-family:黑体"}]{#struct_0_32528_11019_1682309974}

[[备份组视图]{style="font-family:宋体"}]{#struct_0_32528_11019_735070040}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_32528_11019_x926479674}

[[network-admin]{lang="EN-US"}]{#struct_0_32528_11019_197925584}

[[mdc-admin]{lang="EN-US"}]{#struct_0_32528_11019_x793930978}

[[【参数】]{style="font-family:黑体"}]{#struct_0_32528_11019_x151640442}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_32528_11019_x5377329}[：]{style="font-family:宋体"}[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_32528_11019_1999629583}[：]{style="font-family:宋体"}[表示单板在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的位置。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_32528_11019_x1925617482}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[primary]{lang="EN-US"}**]{#struct_0_32528_11019_1194778678}[：表示将节点配置成主节点。]{style="font-family:宋体"}

[**[secondary]{lang="EN-US"}**]{#struct_0_32528_11019_x640502917}[：表示将节点配置成备节点。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_32528_11019_x1892014089}

[[每个备份组最多允许有两个节点：一个主节点和一个备节点。主节点处理业务，并将当前数据备份给备节点；备节点接收主节点的备份数据，当主节点故障时，接替主节点处理业务。]{style="font-family:宋体"}]{#struct_0_32528_11019_1305136535}

[[为了保证业务在主、备节点切换后，仍能正常运行，建议将不同单板上的性能相当的两个节点互为备份。]{style="font-family:宋体"}]{#struct_0_32528_11019_1597689964}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_32528_11019_486555377}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不同备份组的主节点不能相同，同一备份组的主节点和备节点不能相同。]{style="font-family:宋体"}]{#struct_0_32528_11019_x586496}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只能将设备上已经存在的节点加入备份组。配置备份组后，对于拔出的节点，也需要使用]{style="font-family:宋体"}]{#struct_0_32528_11019_x1324265629}**[undo]{lang="EN-US"}[ bind]{lang="EN-US"}**[命令将对应节点从备份组中删除。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_32528_11019_x1301299353}

[[\# ]{lang="EN-US"}]{#struct_0_32528_11019_x2115324372}[将]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板配置为备份组]{style="font-family:宋体"}[Group1]{lang="EN-US"}[的主节点。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_32528_11019_1852473422}

[\[Sysname\] failover group Group1]{lang="EN-US"}

[\[Sysname-failover-group-Group1\] bind slot 2 primary]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_32528_11019_591054526}[将成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上的]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板配置为备份组]{style="font-family:宋体"}[Group1]{lang="EN-US"}[的主节点。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_32528_11019_x1925683018}

[\[Sysname\] failover group Group1]{lang="EN-US"}

[\[Sysname-failover-group-Group1\] bind chassis 1 slot 2 primary]{lang="EN-US"}
:::

::: {#-403202552 .myid}
[]{#_Toc404796064}[]{#struct_0_32528_11019_x603747657}[]{#_Toc378323384}

**备份组 \-- 备份组配置命令 \-- display failover group**

------------------------------------------------------------------------

[**[display failover group]{lang="EN-US"}**]{#struct_0_32528_11019_66146136}[命令用来查看备份组的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_32528_11019_1664325292}

[**[display failover group]{lang="EN-US"}**[ \[ *group-name* \]]{lang="EN-US"}]{#struct_0_32528_11019_x903701780}

[[【视图】]{style="font-family:黑体"}]{#struct_0_32528_11019_1564567080}

[[任意视图]{style="font-family:宋体"}]{#struct_0_32528_11019_583172973}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_32528_11019_955790590}

[[network-admin]{lang="EN-US"}]{#struct_0_32528_11019_x285999878}

[[network-operator]{lang="EN-US"}]{#struct_0_32528_11019_x284879603}

[[mdc-admin]{lang="EN-US"}]{#struct_0_32528_11019_855446833}

[[mdc-operator]{lang="EN-US"}]{#struct_0_32528_11019_x1738415346}

[[【参数】]{style="font-family:黑体"}]{#struct_0_32528_11019_1612176336}

[*[group-name]{lang="EN-US"}*]{#struct_0_32528_11019_x1926141769}[：表示备份组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定该参数，将显示所有备份组的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_32528_11019_x727659496}

[[\# ]{lang="EN-US"}]{#struct_0_32528_11019_x1866261739}[查看备份组的信息。]{style="font-family:宋体"}

[[\<Sysname\> display failover group]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_32528_11019_x1588385758}

[[Stateful failover group information:]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_32528_11019_1150313451}

[[ID  Name                            Primary      Secondary    Active Status]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_32528_11019_x383727776}

[[0   123                             1/2.1        1/3.1        Primary]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_32528_11019_343712477}

[[1   aaa                             1/3.1        1/4.1        Secondary]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_32528_11019_254294549}

[[2   bbb                             1/5.1        NA           Initial]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_32528_11019_x1693460429}

[[表1-1 ]{lang="EN-US"}[display failover group]{lang="EN-US"}]{#struct_0_32528_11019_1884677271}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1098408439}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_32528_11019_x2045258502}
:::

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_32528_11019_x2058615830}

[[ID]{lang="EN-US"}]{#struct_0_32528_11019_x1926207305}

[[备份组的编号]{style="font-size:10.0pt;font-family:宋体"}]{#struct_0_32528_11019_x1141847996}

[[Name]{lang="EN-US"}]{#struct_0_32528_11019_373469126}

[[备份组的名称]{style="font-size:10.0pt;font-family:宋体"}]{#struct_0_32528_11019_1569495109}

[[Primary]{lang="EN-US"}]{#struct_0_32528_11019_x1303537074}

[[备份组]{style="font-size:10.0pt;font-family:宋体"}]{#struct_0_32528_11019_366851754}[的主节点，用]{style="font-family:
  宋体"}*[chassis-number]{lang="EN-US"}*[/*slot-number*.*cpu-number*]{lang="EN-US"}[来表示，如果该节点只有一个]{style="font-family:宋体"}[CPU]{lang="EN-US"}[，则不会显示]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[。当取值为]{style="font-family:宋体"}[NA]{lang="EN-US"}[时表示没有配置主节点]{style="font-family:宋体"}

[[Secondary]{lang="EN-US"}]{#struct_0_32528_11019_x1218872337}

[[备份组]{style="font-size:10.0pt;font-family:宋体"}]{#struct_0_32528_11019_941000076}[的备节点，用]{style="font-family:
  宋体"}*[chassis-number]{lang="EN-US"}*[/*slot-number*.*cpu-number*]{lang="EN-US"}[来表示，如果该节点只有一个]{style="font-family:宋体"}[CPU]{lang="EN-US"}[，则不会显示]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[。当取值为]{style="font-family:宋体"}[NA]{lang="EN-US"}[时表示没有配置备节点]{style="font-family:宋体"}

[[Active Status]{lang="EN-US"}]{#struct_0_32528_11019_1661543091}

[[备份组]{style="font-size:10.0pt;font-family:宋体"}]{#struct_0_32528_11019_x1431326464}[的状态：]{style="font-size:
  10.0pt;font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Primary]{lang="EN-US"}]{#struct_0_32528_11019_496687382}[：备份组中主节点处理业务]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Secondary]{lang="EN-US"}]{#struct_0_32528_11019_x1926272841}[：备份组中备节点处理业务]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Initial]{lang="EN-US"}]{#struct_0_32528_11019_922981056}[：备份组中没有任何节点处理业务]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#169468647 .myid}
[]{#_Toc404796065}[]{#struct_0_32528_11019_x1889381770}[]{#_Toc378323380}

**备份组 \-- 备份组配置命令 \-- failover group**

------------------------------------------------------------------------

[**[failover group]{lang="EN-US"}**]{#struct_0_32528_11019_x2015502909}[命令用来创建备份组，并进入备份组视图。]{style="font-family:宋体"}

[**[undo failover group]{lang="EN-US"}**]{#struct_0_32528_11019_1432342202}[命令用来删除指定备份组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_32528_11019_2012151412}

[**[failover group]{lang="EN-US"}***[ group-name]{lang="EN-US"}*]{#struct_0_32528_11019_1817150375}

[**[undo failover group]{lang="EN-US"}***[ group-name]{lang="EN-US"}*]{#struct_0_32528_11019_118359305}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_32528_11019_99287601}

[[未配置任何备份组。]{style="font-family:宋体"}]{#struct_0_32528_11019_x1776409334}

[[【视图】]{style="font-family:黑体"}]{#struct_0_32528_11019_2114876862}

[[系统视图]{style="font-family:宋体"}]{#struct_0_32528_11019_x1926338377}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_32528_11019_x311665665}

[[network-admin]{lang="EN-US"}]{#struct_0_32528_11019_409022642}

[[mdc-admin]{lang="EN-US"}]{#struct_0_32528_11019_x591581916}

[[【参数】]{style="font-family:黑体"}]{#struct_0_32528_11019_1275572585}

[*[group-name]{lang="EN-US"}*]{#struct_0_32528_11019_671161762}[：备份组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_32528_11019_x1049208042}

[[备份组用于实现特定业务（例如]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_32528_11019_x1944352722}[业务）的数据备份，为特定业务的高可靠性运行提供保障。]{style="font-family:宋体"}

[[通过配置多个备份组，可以实现业务的]{style="font-family:宋体"}[1:1]{lang="EN-US"}]{#struct_0_32528_11019_x411407134}[备份、]{style="font-family:宋体"}[1+1]{lang="EN-US"}[备份、]{style="font-family:宋体"}[N:1]{lang="EN-US"}[备份或]{style="font-family:宋体"}[N+1]{lang="EN-US"}[备份。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_32528_11019_1647003449}

[[\# ]{lang="EN-US"}]{#struct_0_32528_11019_850906942}[创建备份组，名称为]{style="font-family:宋体"}[Group1]{lang="EN-US"}[，并进入该备份组的视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_32528_11019_x819964185}

[\[Sysname\] failover group Group1]{lang="EN-US"}

[\[Sysname-failover-group-Group1\]]{lang="EN-US"}
:::
