::: {#-1618505991 .myid}
[]{#_Toc404795330}[]{#struct_0_18628_x5113_x1060518542}[]{#_Toc347412450}

**接口备份 \-- 接口备份调试命令 \-- debugging interface-backup**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_18628_x5113_1395087306}

[**[debugging ]{lang="EN-US"}[interface-backup]{lang="EN-US"}**[ { **event** \| **track** }]{lang="EN-US"}]{#struct_0_18628_x5113_740478280}

[**[undo debugging ]{lang="EN-US"}[interface-backup]{lang="EN-US"}**[ { **event** \| **track** }]{lang="EN-US"}]{#struct_0_18628_x5113_1287004265}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18628_x5113_1101875684}

[[用户视图]{style="font-family:宋体"}]{#struct_0_18628_x5113_395012593}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18628_x5113_536794476}

[[network-admin]{lang="EN-US"}]{#struct_0_18628_x5113_x1312156633}

[[vd-admin]{lang="EN-US"}]{#struct_0_18628_x5113_x998812092}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18628_x5113_x455787142}

[**[event]{lang="EN-US"}**]{#struct_0_18628_x5113_1238221419}[：表示接口备份事件调试信息开关。]{style="font-family:宋体"}

[**[track]{lang="EN-US"}**]{#struct_0_18628_x5113_x1754947391}[：表示接口备份]{style="font-family:宋体"}[Track]{lang="EN-US"}[项调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_18628_x5113_1133227357}

[**[debugging interface-backup]{lang="EN-US"}**]{#struct_0_18628_x5113_x995248241}[命令用来打开接口备份调试信息开关。]{style="font-family:
宋体"}

[**[undo debugging interface-backup]{lang="EN-US"}**]{#struct_0_18628_x5113_191940872}[命令用来关闭接口备份调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，接口备份调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_18628_x5113_868002171}

[[表1-1 ]{lang="EN-US"}[debugging interface-backup event]{lang="EN-US"}]{#struct_0_18628_x5113_1207305620}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x509430689}[[字段]{style="font-family:黑体"}]{#struct_0_18628_x5113_511666966}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_18628_x5113_118957350}

[[Deactivated the primary interface *interface-name.*]{lang="EN-US"}]{#struct_0_18628_x5113_x1857420748}

[[去激活主接口]{style="font-family:宋体"}]{#struct_0_18628_x5113_1230888234}

[[Deleted the primary interface *interface-name.*]{lang="EN-US"}]{#struct_0_18628_x5113_290306284}

[[删除主接口]{style="font-family:宋体"}]{#struct_0_18628_x5113_x1901318601}

[[Deactivated the backup interface *interface-name*.]{lang="EN-US"}]{#struct_0_18628_x5113_x2003664393}

[[去激活备份接口]{style="font-family:宋体"}]{#struct_0_18628_x5113_338710618}

[[Deleted the backup interface *interface-name*.]{lang="EN-US"}]{#struct_0_18628_x5113_2064603135}

[[删除备份接口]{style="font-family:宋体"}]{#struct_0_18628_x5113_1078699357}

[[Activated the backup interface *interface-name*.]{lang="EN-US"}]{#struct_0_18628_x5113_191875336}

[[激活备份接口]{style="font-family:宋体"}]{#struct_0_18628_x5113_502572793}

[[Activated the primary interface *interface-name*.]{lang="EN-US"}]{#struct_0_18628_x5113_x1817596181}

[[激活主接口]{style="font-family:宋体"}]{#struct_0_18628_x5113_x788319395}

[[Primary interface *interface-name* came up.]{lang="EN-US"}]{#struct_0_18628_x5113_x1494936478}

[[主接口链路]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_18628_x5113_149370352}

[[Backup interface *interface-name* came up.]{lang="EN-US"}]{#struct_0_18628_x5113_x1389757827}

[[备份接口链路]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_18628_x5113_623782341}

[[Primary interface *interface-name* went down.]{lang="EN-US"}]{#struct_0_18628_x5113_x408785606}

[[主接口链路]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_18628_x5113_159004812}

[[Backup interface *interface-name* went down.]{lang="EN-US"}]{#struct_0_18628_x5113_191809800}

[[备份接口链路]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_18628_x5113_x1474844163}

[[Bandwidth of primary interface *interface-name* changed.]{lang="EN-US"}]{#struct_0_18628_x5113_91331602}

[[主接口带宽发生变化]{style="font-family:宋体"}]{#struct_0_18628_x5113_736691783}

[[Added a backup interface for primary interface *interface-name.*]{lang="EN-US"}]{#struct_0_18628_x5113_x553948305}

[[在主接口上添加一个备份接口]{style="font-family:宋体"}]{#struct_0_18628_x5113_x1605396539}

[[Deleted a backup interface from primary interface *interface-name.*]{lang="EN-US"}]{#struct_0_18628_x5113_867881713}

[[在主接口上删除一个备份接口]{style="font-family:宋体"}]{#struct_0_18628_x5113_x313026913}

[[Enabled load balancing of primary interface *interface-name*.]{lang="EN-US"}]{#struct_0_18628_x5113_191744264}

[[启动主接口的负载分担模式]{style="font-family:宋体"}]{#struct_0_18628_x5113_316218215}

[[Disabled load balancing of primary interface *interface-name*.]{lang="EN-US"}]{#struct_0_18628_x5113_2146579558}

[[停止主接口的负载分担模式]{style="font-family:宋体"}]{#struct_0_18628_x5113_1366773998}

[[Changed the priority of backup interface *interface-name*.]{lang="EN-US"}]{#struct_0_18628_x5113_x538136267}

[[修改备份接口的优先级]{style="font-family:宋体"}]{#struct_0_18628_x5113_x165283625}

[[Changed the UP_DELAY timer interval of interface *Interface-name*.]{lang="EN-US"}]{#struct_0_18628_x5113_444104305}

[[修改接口的]{style="font-family:宋体"}[UP_DELAY]{lang="EN-US"}]{#struct_0_18628_x5113_960018997}[定时器参数]{style="font-family:宋体"}

[[Changed the DOWN_DELAY timer interval of interface *Interface-name*.]{lang="EN-US"}]{#struct_0_18628_x5113_191678728}

[[修改接口的]{style="font-family:宋体"}[DOWN_DELAY]{lang="EN-US"}]{#struct_0_18628_x5113_684226903}[定时器参数]{style="font-family:宋体"}

[[Changed the flow check interval of primary interface *interface-name*.]{lang="EN-US"}]{#struct_0_18628_x5113_x1566556287}

[[修改主接口的流量检测间隔]{style="font-family:宋体"}]{#struct_0_18628_x5113_x600837817}

[[DOWN_DELAY timer on primary interface *interface-name* expired. ]{lang="EN-US"}]{#struct_0_18628_x5113_1391415223}

[[主接口]{style="font-family:宋体"}[DOWN_DELAY]{lang="EN-US"}]{#struct_0_18628_x5113_x578243076}[定时器超时]{style="font-family:宋体"}

[[DOWN_DELAY timer on backup interface *interface-name* expired.]{lang="EN-US"}]{#struct_0_18628_x5113_x739608974}

[[备份接口]{style="font-family:宋体"}[DOWN_DELAY]{lang="EN-US"}]{#struct_0_18628_x5113_191613192}[定时器超时]{style="font-family:宋体"}

[[UP_DELAY timer on backup interface *interface-name* expired.]{lang="EN-US"}]{#struct_0_18628_x5113_x66744215}

[[备份接口]{style="font-family:宋体"}[UP_DELAY]{lang="EN-US"}]{#struct_0_18628_x5113_x1403647362}[定时器超时]{style="font-family:宋体"}

[[UP_DELAY timer on primary interface *interface-name* expired.]{lang="EN-US"}]{#struct_0_18628_x5113_558400747}

[[主接口]{style="font-family:宋体"}[UP_DELAY]{lang="EN-US"}]{#struct_0_18628_x5113_x1887648707}[定时器超时]{style="font-family:宋体"}

[[Load balancing timer on primary interface *interface-name* expired.]{lang="EN-US"}]{#struct_0_18628_x5113_x1019481872}

[[主接口上的负载分担定时器超时]{style="font-family:宋体"}]{#struct_0_18628_x5113_x120141810}

[[Traffic amount reached the upper limit of primary interface *interface-name*, and it is required to activate a backup interface.]{lang="EN-US"}]{#struct_0_18628_x5113_191547656}

[[主接口的流量达到了主接口下配置的阈值上限，需要启用一个备份接口]{style="font-family:宋体"}]{#struct_0_18628_x5113_1949232597}

[[Total traffic amount reached the lower limit of primary interface *interface-name*, and it is required to deactivate a backup interface.]{lang="EN-US"}]{#struct_0_18628_x5113_1396267737}

[[主接口和备份接口的流量总和小于主接口下配置的阈值下限，需要关闭一个备份接口]{style="font-family:宋体"}]{#struct_0_18628_x5113_1392692615}

[[Interface *interface-name* transitioned from *state1* to *state2.*]{lang="EN-US"}]{#struct_0_18628_x5113_1660972852}

[[接口状态由]{style="font-family:宋体"}*[state1]{lang="EN-US"}*]{#struct_0_18628_x5113_2118859741}[迁移到]{style="font-family:宋体"}*[state2]{lang="EN-US"}*[，可能的状态如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INVALID]{lang="EN-US"}]{#struct_0_18628_x5113_191482120}[：初始]{style="font-family:宋体"}[无效]{lang="EN-US" style="font-family:宋体"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STANDBY]{lang="EN-US"}]{#struct_0_18628_x5113_x1524002942}[：备用]{lang="EN-US" style="font-family:宋体"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_18628_x5113_1357962091}[：]{lang="EN-US" style="font-family:宋体"}[UP]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_18628_x5113_270285501}[：]{lang="EN-US" style="font-family:宋体"}[DOWN]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP_DELAY]{lang="EN-US"}]{#struct_0_18628_x5113_x170107642}[：延时]{lang="EN-US" style="font-family:宋体"}[UP]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN_DELAY]{lang="EN-US"}]{#struct_0_18628_x5113_192465160}[：延时]{lang="EN-US" style="font-family:宋体"}[DOWN]{lang="EN-US"}[状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging interface-backup track]{lang="EN-US"}]{#struct_0_18628_x5113_x1197955015}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x519339385}[[字段]{style="font-family:黑体"}]{#struct_0_18628_x5113_1473594323}

[[描述]{style="font-family:黑体"}]{#struct_0_18628_x5113_263325390}

[[Track add: Interface *interface-name* was associated with track entry *number*.]{lang="EN-US"}]{#struct_0_18628_x5113_x31687438}

[[配置了一个关联]{style="font-family:宋体"}[track]{lang="EN-US"}]{#struct_0_18628_x5113_1959962005}[项的备份接口]{style="font-family:宋体"}

[[Track modify: Track entry *number* associated with interface *interface-name* transitioned to *state*.]{lang="EN-US"}]{#struct_0_18628_x5113_1498167988}

[[Track]{lang="EN-US"}]{#struct_0_18628_x5113_x1855533791}[项]{style="font-family:宋体"}*[number]{lang="EN-US"}*[的状态变为]{style="font-family:宋体"}*[state]{lang="EN-US"}*[，可能的状态如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Positive]{lang="EN-US"}]{#struct_0_18628_x5113_22670948}[：]{style="font-family:宋体"}[Track]{lang="EN-US"}[项跟踪的主链路正常]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N]{lang="EN-US"}[egative]{lang="EN-US"}]{#struct_0_18628_x5113_x652339686}[：]{style="font-family:
  宋体"}[Track]{lang="EN-US"}[项跟踪的主链路故障]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not ready]{lang="EN-US"}]{#struct_0_18628_x5113_1576084092}[：]{style="font-family:宋体"}[Track]{lang="EN-US"}[项未生效]{style="font-family:宋体"}

[[Track delete: Association between interface *interface-name* and track entry *number* was removed.]{lang="EN-US"}]{#struct_0_18628_x5113_x1773467797}

[[删除接口与]{style="font-family:宋体"}[track]{lang="EN-US"}]{#struct_0_18628_x5113_x412637650}[项的关联]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18628_x5113_192399624}

[[\# ]{lang="EN-US"}]{#struct_0_18628_x5113_x1017165433}[打开接口备份的事件调试信息开关，当在主接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[下添加一个备份接口]{style="font-family:宋体"}[GigabitEthernet1/0/4]{lang="EN-US"}[时，将输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging interface-backup event]{lang="EN-US"}]{#struct_0_18628_x5113_505565399}

[\<Sysname\> terminal monitor]{lang="EN-US"}

[\<Sysname\> terminal  debugging]{lang="EN-US"}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/2\] backup interface gigabitethernet 1/0/4]{lang="EN-US"}

[\*Feb 27 21:12:49:639 2013 Sysname IB/7/EVENT: -MDC=1; Added a backup interface for primary interface GigabitEthernet1/0/2.]{lang="EN-US"}

[\*Feb 27 21:12:49:640 2013 Sysname IB/7/EVENT: -MDC=1; Interface GigabitEthernet1/0/2 transitioned from INVALID to UP.]{lang="EN-US"}

[\*Feb 27 21:12:49:640 2013 Sysname IB/7/EVENT: -MDC=1; Interface GigabitEthernet1/0/4 transitioned from INVALID to UP.]{lang="EN-US"}

[\*Feb 27 21:12:49:650 2013 Sysname IB/7/EVENT: -MDC=1; Interface GigabitEthernet1/0/4 transitioned from UP to STANDBY.]{lang="EN-US"}

[\*Feb 27 21:12:49:650 2013 Sysname IB/7/EVENT: -MDC=1; Backup interface GigabitEthernet1/0/4 went down.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_18628_x5113_x1960921351}*[主接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[下添加了一个备份接口，由于主接口当前处于]{style="font-family:宋体"}[UP]{lang="EN-US"}[状态，备份接口]{style="font-family:宋体"}[GigabitEthernet1/0/4]{lang="EN-US"}[直接被]{style="font-family:宋体"}[shutdown]{lang="EN-US"}[，当前备份接口处于]{style="font-family:宋体"}[STANDBY]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_18628_x5113_x1064758019}[配置主备接口的切换延时为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒，当将主接口]{style="font-family:宋体"}[shutdown]{lang="EN-US"}[时，将输出如下调试信息。]{style="font-family:宋体"}

[[\[Sysname-GigabitEthernet1/0/2\] backup timer delay 10 10]{lang="EN-US"}]{#struct_0_18628_x5113_x1087354782}

[\[Sysname-GigabitEthernet1/0/2\] shutdown]{lang="EN-US"}

[\*Feb 27 21:15:42:912 2013 Sysname IB/7/EVENT: -MDC=1; Primary interface GigabitEthernet1/0/2 went down.]{lang="EN-US"}

[\*Feb 27 21:15:42:913 2013 Sysname IB/7/EVENT: -MDC=1; Interface GigabitEthernet1/0/2 transitioned from UP to DOWN_DELAY.]{lang="EN-US"}

[%Feb 27 21:15:42:914 2013 Sysname IFNET/3/PHY_UPDOWN: -MDC=1; GigabitEthernet1/0/2 link status is down.]{lang="EN-US"}

[%Feb 27 21:15:42:915 2013 Sysname IFNET/5/LINK_UPDOWN: -MDC=1; Line protocol on the interface GigabitEthernet1/0/2 is down.]{lang="EN-US"}

[\*Feb 27 21:15:53:914 2013 Sysname IB/7/EVENT: -MDC=1; DOWN_DELAY timer on primary interface GigabitEthernet1/0/2 expired.]{lang="EN-US"}

[\*Feb 27 21:15:53:914 2013 Sysname IB/7/EVENT: -MDC=1; Interface GigabitEthernet1/0/2 transitioned from DOWN_DELAY to DOWN.]{lang="EN-US"}

[\*Feb 27 21:15:54:136 2013 Sysname IB/7/EVENT: -MDC=1; Interface GigabitEthernet1/0/4 transitioned from STANDBY to UP_DELAY.]{lang="EN-US"}

[\*Feb 27 21:15:55:474 2013 Sysname IB/7/EVENT: -MDC=1; Backup interface GigabitEthernet1/0/4 came up.]{lang="EN-US"}

[%Feb 27 21:15:55:475 2013 Sysname IFNET/3/PHY_UPDOWN: -MDC=1; GigabitEthernet1/0/4 link status is up.]{lang="EN-US"}

[%Feb 27 21:15:55:475 2013 Sysname IFNET/5/LINK_UPDOWN: -MDC=1; Line protocol on the interface GigabitEthernet1/0/4 is up.]{lang="EN-US"}

[\*Feb 27 21:16:03:914 2013 Sysname IB/7/EVENT: -MDC=1; UP_DELAY timer on backup interface GigabitEthernet1/0/4 expired.]{lang="EN-US"}

[\*Feb 27 21:16:03:914 2013 Sysname IB/7/EVENT: -MDC=1; Interface GigabitEthernet1/0/4 transitioned from UP_DELAY to UP.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_18628_x5113_135529510}*[主接口报链路]{style="font-family:宋体"}[down]{lang="EN-US"}[事件，主接口的状态由]{style="font-family:宋体"}[UP]{lang="EN-US"}[切换到]{style="font-family:宋体"}[DOWN_DELAY]{lang="EN-US"}[，待主接口的]{style="font-family:宋体"}[DOWN_DELAY]{lang="EN-US"}[定时器超时后，主接口的状态由]{style="font-family:宋体"}[DOWN_DELAY]{lang="EN-US"}[切换到]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[，备份接口由]{style="font-family:宋体"}[STANDBY]{lang="EN-US"}[切换到]{style="font-family:宋体"}[UP_DELAY]{lang="EN-US"}[，待备份接口上的]{style="font-family:宋体"}[UPDELAY]{lang="EN-US"}[定时器超时后，备份接口状态由]{style="font-family:宋体"}[UP_DELAY]{lang="EN-US"}[切换到]{style="font-family:宋体"}[UP]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18628_x5113_191940871}[打开]{style="font-family:宋体"}[接口备份的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项调试信息开关，配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/4]{lang="EN-US"}[与]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[关联时，]{style="font-family:宋体"}[将输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging standby track]{lang="EN-US"}]{#struct_0_18628_x5113_868002168}

[\<Sysname\> terminal monitor]{lang="EN-US"}

[\<Sysname\> terminal debugging]{lang="EN-US"}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/4]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/4\] backup track 1]{lang="EN-US"}

[\*Feb 27 21:20:46:614 2013 Sysname IB/7/TRACK: -MDC=1; Track add: Interface GigabitEthernet1/0/4 was associated with track entry 1.]{lang="EN-US"}

[\*Feb 27 21:20:46:616 2013 Sysname IB/7/TRACK: -MDC=1; Track modify: Track entry 1 associated with interface GigabitEthernet1/0/4 transitioned to Not ready.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_18628_x5113_x1131346531}*[添加一个关联]{style="font-family:宋体"}[Track]{lang="EN-US"}[的备份接口，由于]{style="font-family:宋体"}[Track]{lang="EN-US"}[项当前未建立，]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的状态为]{style="font-family:宋体"}[Not ready]{lang="EN-US"}[，此时备份接口的链路状态保持原始状态不变]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_18628_x5113_1943550767}[配置]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[跟踪的主链路为接口]{style="font-family:
宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[时，将输出如下调试信息。]{style="font-family:宋体"}

[[\[Sysname-GigabitEthernet1/0/4\] quit]{lang="EN-US"}]{#struct_0_18628_x5113_x1733672147}

[\[Sysname\] track 1 interface GigabitEthernet1/0/2]{lang="EN-US"}

[\*Feb 27 21:37:00:144 2013 Sysname IB/7/TRACK: -MDC=1; Track modify: Track entry 1 associated with interface GigabitEthernet1/0/4 transitioned to Positive.]{lang="EN-US"}

[%Feb 27 21:37:00:153 2013 Sysname IFNET/3/PHY_UPDOWN: -MDC=1; GigabitEthernet1/0/4 link status is down.]{lang="EN-US"}

[%Feb 27 21:37:00:154 2013 Sysname IFNET/5/LINK_UPDOWN: -MDC=1; Line protocol on the interface GigabitEthernet1/0/4 is down.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_18628_x5113_x388704962}*[新创建]{style="font-family:宋体"}[Track]{lang="EN-US"}[项关联时，由于]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[跟踪的主接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[处于]{style="font-family:宋体"}[UP]{lang="EN-US"}[状态，]{style="font-family:宋体"}[Track]{lang="EN-US"}[状态变为]{style="font-family:宋体"}[positive]{lang="EN-US"}[，此时需要将备份接口]{style="font-family:宋体"}[GigabitEthernet1/0/4 shutdown]{lang="EN-US"}[，备份接口状态转换为]{style="font-family:
宋体"}[STANDBY]{lang="EN-US"}[状态]{style="font-family:宋体"}*
