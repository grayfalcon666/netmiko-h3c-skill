::: {#2025847969 .myid}
[]{#_Toc404795215}[]{#struct_0_73594_93986_x315614614}[]{#_Toc402462254}[]{#_Toc398190396}[]{#_Toc402462253}

**负载均衡 \-- 负载均衡配置命令 \-- ap radio**

------------------------------------------------------------------------

[**[ap radio]{lang="EN-US"}**]{#struct_0_73594_93986_896574794}[命令用来将指定的]{style="font-family:宋体"}[Radio]{lang="EN-US"}[加入到负载均衡组中。]{style="font-family:宋体"}

[**[undo ap]{lang="EN-US"}**]{#struct_0_73594_93986_x1738367605}[命令用来删除负载均衡组中的]{style="font-family:宋体"}[Radio]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73594_93986_1920337115}

[**[ap ]{lang="EN-US"}***[ap-name]{lang="EN-US"}***[ radio]{lang="EN-US"}**[ *radio-number*]{lang="EN-US"}]{#struct_0_73594_93986_x841190364}

[**[undo ap ]{lang="EN-US"}**[{ *ap-name* \[ **radio** *radio-number* \] \| **all** }]{lang="EN-US"}]{#struct_0_73594_93986_x1763569467}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_73594_93986_x522148309}

[[负载均衡组中不存在任何]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_73594_93986_2030151084}[的]{style="font-family:宋体"}[Radio]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73594_93986_2031850406}

[[负载均衡组视图]{style="font-family:宋体"}]{#struct_0_73594_93986_485230482}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73594_93986_1400257921}

[[network-admin]{lang="EN-US"}]{#struct_0_73594_93986_x418217477}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73594_93986_x457881969}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73594_93986_x2066645392}

[*[ap-name]{lang="EN-US"}*]{#struct_0_73594_93986_754600483}[：加入负载均衡组的]{style="font-family:宋体"}[AP]{lang="EN-US"}[名称。为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。加入负载均衡组的]{style="font-family:宋体"}[AP]{lang="EN-US"}[必须已经存在。]{style="font-family:宋体"}

[*[radio-number]{lang="EN-US"}*]{#struct_0_73594_93986_x365144094}[：将]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[radio]{lang="EN-US"}[编号加入负载均衡组。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_73594_93986_1908601638}[：删除负载均衡组中所有的]{style="font-family:宋体"}[Radio]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_73594_93986_x1570924480}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{style="font-family:宋体"}[Radio]{lang="EN-US"}]{#struct_0_73594_93986_x1681971113}[只能加入一个负载均衡组。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除负载均衡组中的]{lang="EN-US" style="font-family:宋体"}[Radio]{lang="EN-US"}]{#struct_0_73594_93986_x1713823531}[时，如果使用]{lang="EN-US" style="font-family:宋体"}**[undo ap]{lang="EN-US"}**[ *ap-name*]{lang="EN-US"}[命令（即不指定]{lang="EN-US" style="font-family:宋体"}**[radio]{lang="EN-US"}***[ radio-number]{lang="EN-US"}*[参数时），表示删除负载均衡组中指定]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[的所有]{lang="EN-US" style="font-family:宋体"}[Radio]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73594_93986_1887692991}

[[\# ]{lang="EN-US"}]{#struct_0_73594_93986_2143194625}[将]{style="font-family:宋体"}[ap1]{lang="EN-US"}[的第]{style="font-family:宋体"}[2]{lang="EN-US"}[个]{style="font-family:宋体"}[Radio]{lang="EN-US"}[加入到]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[10]{lang="EN-US"}[的负载均衡组中。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_73594_93986_2060149894}

[\[Sysname\] wlan load-balance group 10]{lang="EN-US"}

[\[Sysname-wlan-lb-group-10\] ap ap1 radio 2]{lang="EN-US"}
:::

::: {#-1461383778 .myid}
[]{#_Toc404795216}[]{#struct_0_73594_93986_x558033228}[]{#_Toc398190397}[]{#_Toc402462255}

**负载均衡 \-- 负载均衡配置命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_73594_93986_1119458261}[命令用来配置负载均衡组的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_73594_93986_x837310089}[命令用来删除负载均衡组的描述信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73594_93986_x1729043910}

[**[description]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_73594_93986_1075031498}

[**[undo description]{lang="EN-US"}**]{#struct_0_73594_93986_x739983261}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_73594_93986_857233296}

[[负载均衡组没有描述信息。]{style="font-family:宋体"}]{#struct_0_73594_93986_1655191592}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73594_93986_1059958861}

[[负载均衡组视图]{style="font-family:宋体"}]{#struct_0_73594_93986_x40711996}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73594_93986_x1263728052}

[[network-admin]{lang="EN-US"}]{#struct_0_73594_93986_1976518723}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73594_93986_x484894468}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73594_93986_1035343832}

[*[text]{lang="EN-US"}*]{#struct_0_73594_93986_x1308456484}[：负载均衡组的描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73594_93986_1354794921}

[[\# ]{lang="EN-US"}]{#struct_0_73594_93986_x1161014714}[配置负载均衡组]{style="font-family:宋体"}[10]{lang="EN-US"}[的描述信息为]{style="font-family:宋体"}[marketing]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_73594_93986_x995661926}

[\[Sysname\] wlan load-balance group 10]{lang="EN-US"}

[\[Sysname-wlan-lb-group10\] description marketing]{lang="EN-US"}
:::

::: {#134141313 .myid}
[]{#_Toc404795217}[]{#struct_0_73594_93986_x1682853430}[]{#_Toc398190398}[]{#_Toc402462256}

**负载均衡 \-- 负载均衡配置命令 \-- display wlan load-balance group**

------------------------------------------------------------------------

[**[display wlan load-balance group]{lang="EN-US"}**]{#struct_0_73594_93986_1571521878}[命令用来显示负载均衡组的当前配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73594_93986_240828357}

[**[display wlan load-balance group ]{lang="EN-US"}**[{ *group-id* \| **all** }]{lang="EN-US"}]{#struct_0_73594_93986_x604855673}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73594_93986_710293739}

[[任意视图]{style="font-family:宋体"}]{#struct_0_73594_93986_1829267735}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73594_93986_686997380}

[[network-admin]{lang="EN-US"}]{#struct_0_73594_93986_x1888119617}

[[network-operator]{lang="EN-US"}]{#struct_0_73594_93986_619034609}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73594_93986_x2050978409}

[[mdc-operator]{lang="EN-US"}]{#struct_0_73594_93986_x890947708}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73594_93986_x868312283}

[*[group-id]{lang="EN-US"}*]{#struct_0_73594_93986_1291455009}[：负载均衡组的]{style="font-family:宋体"}[ID]{lang="EN-US"}[。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_73594_93986_x754338310}[：显示所有负载均衡组的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73594_93986_x1901684962}

[[\# ]{lang="EN-US"}]{#struct_0_73594_93986_x1432028098}[显示组号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的负载均衡组配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display wlan load-balance group 1]{lang="EN-US"}]{#struct_0_73594_93986_223891519}

[                  WLAN load balance group information]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Group ID                : 1]{lang="EN-US"}

[Description             :]{lang="EN-US"}

[Group members           : ap3-radio2,]{lang="EN-US"}

[                          ap2-radio1,]{lang="EN-US"}

[                          ap1-radio1,]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_73594_93986_x981942207}[显示所有负载均衡组配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display wlan load-balance group all]{lang="EN-US"}]{#struct_0_73594_93986_677904946}

[                  WLAN load balance group information]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Group ID                : 1]{lang="EN-US"}

[Description             :]{lang="EN-US"}

[Group members           : ap3-radio2,]{lang="EN-US"}

[                          ap2-radio1,]{lang="EN-US"}

[                          ap1-radio1,]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Group ID                : 2]{lang="EN-US"}

[Description             : marketing]{lang="EN-US"}

[Group members           : ap3-radio1,]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display wlan load-balance group]{lang="EN-US"}]{#struct_0_73594_93986_1892351504}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_970280539}[[字段]{style="font-family:黑体"}]{#struct_0_73594_93986_x1375935435}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_73594_93986_x1930846170}

[[Group ID]{lang="EN-US"}]{#struct_0_73594_93986_439595389}

[[负载均衡组]{style="font-family:宋体"}]{#struct_0_73594_93986_x1137908601}[ID]{lang="EN-US"}

[[Description]{lang="EN-US"}]{#struct_0_73594_93986_x469296150}

[[负载均衡组描述信息]{style="font-family:宋体"}]{#struct_0_73594_93986_1637932095}

[[Group members]{lang="EN-US"}]{#struct_0_73594_93986_x1494221520}

[[负载均衡组内的]{style="font-family:宋体"}[Radio]{lang="EN-US"}]{#struct_0_73594_93986_x888178995}[列表]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1111672271 .myid}
[]{#_Toc404795218}[]{#struct_0_73594_93986_x1177247864}[]{#_Toc398190402}[]{#_Toc402462257}

**负载均衡 \-- 负载均衡配置命令 \-- wlan load-balance access-denial**

------------------------------------------------------------------------

[**[wlan load-balance access-denial]{lang="EN-US"}**]{#struct_0_73594_93986_1679232588}[命令用来配置拒绝客户端关联请求的最大次数。]{style="font-family:宋体"}

[**[undo wlan load-balance access-denial]{lang="EN-US"}**]{#struct_0_73594_93986_x270000522}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73594_93986_1342898589}

[**[wlan load-balance access-denial]{lang="EN-US"}**[ *access-denial*]{lang="EN-US"}]{#struct_0_73594_93986_713222062}

[**[undo wlan load-balance access-denial]{lang="EN-US"}**]{#struct_0_73594_93986_153025365}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_73594_93986_1566149116}

[[拒绝客户端关联请求的最大次数为]{style="font-family:宋体"}[10]{lang="EN-US"}]{#struct_0_73594_93986_x659217554}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73594_93986_1218101670}

[[系统视图]{style="font-family:宋体"}]{#struct_0_73594_93986_x1858695058}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73594_93986_x597436267}

[[network-admin]{lang="EN-US"}]{#struct_0_73594_93986_887820128}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73594_93986_x1299654081}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73594_93986_1840704360}

[*[access-denial]{lang="EN-US"}*]{#struct_0_73594_93986_x983928561}[：拒绝客户端关联请求的最大次数，取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_73594_93986_1420402801}

[[如果客户端反复向某个]{style="font-family:宋体"}[Radio]{lang="EN-US"}]{#struct_0_73594_93986_x1479861102}[发起关联请求，且]{style="font-family:宋体"}[Radio]{lang="EN-US"}[拒绝客户端关联请求次数达到设定的最大拒绝关联请求次数，那么该]{style="font-family:宋体"}[Radio]{lang="EN-US"}[会认为此时该客户端不能连接到其它任何的]{style="font-family:宋体"}[Radio]{lang="EN-US"}[，在这种情况下，]{style="font-family:宋体"}[ Radio]{lang="EN-US"}[会接受该客户端的关联请求。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73594_93986_x431429036}

[[\# ]{lang="EN-US"}]{#struct_0_73594_93986_x1402400047}[配置设备拒绝客户端关联请求的最大次数为]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_73594_93986_x1083964828}

[\[Sysname\] wlan load-balance access-denial 4]{lang="EN-US"}
:::

::: {#-263865669 .myid}
[]{#_Toc404795219}[]{#struct_0_73594_93986_x792767736}[]{#_Toc398190394}[]{#_Toc402462258}

**负载均衡 \-- 负载均衡配置命令 \-- wlan load-balance enable**

------------------------------------------------------------------------

[**[wlan load-balance enable]{lang="EN-US"}**]{#struct_0_73594_93986_x981886241}[命令用来开启负载均衡功能。]{style="font-family:
宋体"}

[**[undo wlan ]{lang="EN-US"}[load-balance enable]{lang="EN-US"}**]{#struct_0_73594_93986_345976480}[命令用来关闭负载均衡功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73594_93986_1298745926}

[**[wlan load-balance enable]{lang="EN-US"}**]{#struct_0_73594_93986_x562579937}

[**[undo wlan load-balance enable]{lang="EN-US"}**]{#struct_0_73594_93986_274620419}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_73594_93986_x934845267}

[[负载均衡功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_73594_93986_148675598}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73594_93986_x191840752}

[[系统视图]{style="font-family:宋体"}]{#struct_0_73594_93986_1157179044}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73594_93986_x812165837}

[[network-admin]{lang="EN-US"}]{#struct_0_73594_93986_x421974038}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73594_93986_1641885520}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73594_93986_817030398}

[[\# ]{lang="EN-US"}]{#struct_0_73594_93986_x1058159724}[开启负载均衡功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_73594_93986_22426818}

[\[Sysname\] wlan load-balance ]{lang="EN-US"}[enable]{lang="EN-US"}
:::

::: {#1769033631 .myid}
[]{#_Toc404795220}[]{#struct_0_73594_93986_x50091947}[]{#_Toc398190395}[]{#_Toc402462259}

**负载均衡 \-- 负载均衡配置命令 \-- wlan load-balance group**

------------------------------------------------------------------------

[**[wlan load-balance group]{lang="EN-US"}**]{#struct_0_73594_93986_1274415926}[命令用来创建负载均衡组。]{style="font-family:宋体"}

[**[undo wlan load-balance group]{lang="EN-US"}**]{#struct_0_73594_93986_708481622}[命令用来删除指定或所有的负载均衡组。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73594_93986_x1291463522}

[**[wlan load-balance group ]{lang="EN-US"}***[group-id]{lang="EN-US"}*]{#struct_0_73594_93986_x700611069}

[**[undo wlan load-balance group ]{lang="EN-US"}**[{ ]{lang="EN-US"}*[group-id]{lang="EN-US"}***[ \| all ]{lang="EN-US"}**[}]{lang="EN-US"}]{#struct_0_73594_93986_1539532352}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_73594_93986_1370684840}

[[不存在负载均衡组。]{style="font-family:宋体"}]{#struct_0_73594_93986_337970989}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73594_93986_185537326}

[[系统视图]{style="font-family:宋体"}]{#struct_0_73594_93986_x1508128927}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73594_93986_1516037484}

[[network-admin]{lang="EN-US"}]{#struct_0_73594_93986_262896055}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73594_93986_1729242642}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73594_93986_1491606875}

[*[group-id]{lang="EN-US"}*]{#struct_0_73594_93986_x850574950}[：负载均衡组的]{style="font-family:宋体"}[ID]{lang="EN-US"}[。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_73594_93986_x831512573}[：删除所有的负载均衡组。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_73594_93986_x178336851}

[[创建负载均衡组后，]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_73594_93986_1823849925}[将以负载均衡组为单位，在各个组内的]{style="font-family:宋体"}[Radio]{lang="EN-US"}[间进行会话模式、流量模式或带宽模式的负载均衡，没有加入到任何负载均衡组的]{style="font-family:宋体"}[Radio]{lang="EN-US"}[不会参与负载均衡。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73594_93986_x70300595}

[[\# ]{lang="EN-US"}]{#struct_0_73594_93986_1437419833}[创建]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[10]{lang="EN-US"}[的负载均衡组。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_73594_93986_932922581}

[\[Sysname\] wlan load-balance group 10]{lang="EN-US"}

[\[Sysname-wlan-lb-group-10\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_73594_93986_x1364659240}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ap radio]{lang="EN-US"}**]{#struct_0_73594_93986_x1658508966}
:::

::: {#1502206664 .myid}
[]{#_Toc404795221}[]{#struct_0_73594_93986_656758437}[]{#_Toc398190401}[]{#_Toc402462260}

**负载均衡 \-- 负载均衡配置命令 \-- wlan load-balance mode bandwidth**

------------------------------------------------------------------------

[**[wlan load-balance mode bandwidth]{lang="EN-US"}**]{#struct_0_73594_93986_x716175384}[命令用来配置负载均衡模式为带宽模式。]{style="font-family:宋体"}

[**[undo wlan load-balance mode]{lang="EN-US"}**]{#struct_0_73594_93986_x1070911518}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73594_93986_2070865368}

[**[wlan load-balance mode bandwidth ]{lang="EN-US"}***[value]{lang="EN-US"}*[ \[ **gap** *gap-value* \]]{lang="EN-US"}]{#struct_0_73594_93986_1452115285}

[**[undo wlan load-balance mode]{lang="EN-US"}**]{#struct_0_73594_93986_x202711581}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73594_93986_x414489048}

[[系统视图]{style="font-family:宋体"}]{#struct_0_73594_93986_x1388182818}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_73594_93986_1738626368}

[[负载均衡模式为会话模式。]{style="font-family:宋体"}]{#struct_0_73594_93986_2029333404}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73594_93986_183600269}

[[系统视图]{style="font-family:宋体"}]{#struct_0_73594_93986_x841124828}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73594_93986_605568605}

[[network-admin]{lang="EN-US"}]{#struct_0_73594_93986_x1995420991}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73594_93986_177703525}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73594_93986_65639132}

[*[value]{lang="EN-US"}*]{#struct_0_73594_93986_x1543790334}[：带宽门限值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[500]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[Mbps]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[40Mbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[gap-value]{lang="EN-US"}*]{#struct_0_73594_93986_1491624421}[：带宽差值门限值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[200]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[Mbps]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[20Mbps]{lang="EN-US"}[。带宽差值即当前]{style="font-family:宋体"}[Radio]{lang="EN-US"}[上的带宽与同一]{style="font-family:宋体"}[AC]{lang="EN-US"}[内其他]{style="font-family:宋体"}[Radio]{lang="EN-US"}[上的带宽最小者的差值。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_73594_93986_1072835285}

[[当]{style="font-family:宋体"}[Radio]{lang="EN-US"}]{#struct_0_73594_93986_152343000}[上的带宽达到]{style="font-family:宋体"}[/]{lang="EN-US"}[超过带宽门限值并且与同一]{style="font-family:宋体"}[AC]{lang="EN-US"}[内其他]{style="font-family:宋体"}[Radio]{lang="EN-US"}[上的带宽最小者的差值达到]{style="font-family:宋体"}[/]{lang="EN-US"}[超过带宽差值门限值，]{style="font-family:宋体"}[Radio]{lang="EN-US"}[开始运行负载均衡。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73594_93986_x272223397}

[[\# ]{lang="EN-US"}]{#struct_0_73594_93986_1195865711}[配置负载均衡模式为带宽模式，带宽门限值为]{style="font-family:宋体"}[100Mbps]{lang="EN-US"}[，带宽差值门限值为]{style="font-family:宋体"}[20Mbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_73594_93986_x1471629963}

[\[Sysname\] wlan load-balance mode bandwidth 100 gap 20]{lang="EN-US"}
:::

::: {#-26126975 .myid}
[]{#_Toc404795222}[]{#struct_0_73594_93986_675053035}[]{#_Toc398190399}[]{#_Toc402462261}

**负载均衡 \-- 负载均衡配置命令 \-- wlan load-balance mode session**

------------------------------------------------------------------------

[**[wlan load-balance mode session]{lang="EN-US"}**]{#struct_0_73594_93986_1502545603}[命令用来配置负载均衡模式为会话模式。]{style="font-family:
宋体"}

[**[undo wlan load-balance mode]{lang="EN-US"}**]{#struct_0_73594_93986_1887758527}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73594_93986_630182459}

[**[wlan load-balance mode session]{lang="EN-US"}**[ *value* \[ **gap** *gap-value* \]]{lang="EN-US"}]{#struct_0_73594_93986_x899163694}

[**[undo wlan load-balance mode]{lang="EN-US"}**]{#struct_0_73594_93986_1708443594}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_73594_93986_x945312045}

[[负载均衡模式为会话模式。]{style="font-family:宋体"}]{#struct_0_73594_93986_x665442373}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73594_93986_x1285879168}

[[系统视图]{style="font-family:宋体"}]{#struct_0_73594_93986_19558600}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73594_93986_1119688012}

[[network-admin]{lang="EN-US"}]{#struct_0_73594_93986_x1222006342}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73594_93986_x1755724946}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73594_93986_822385705}

[*[value]{lang="EN-US"}*]{#struct_0_73594_93986_x485353220}[：会话门限值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[40]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[20]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[gap-value]{lang="EN-US"}*]{#struct_0_73594_93986_702926832}[：会话差值门限值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[4]{lang="EN-US"}[。会话差值即当前]{style="font-family:宋体"}[Radio]{lang="EN-US"}[上的在线客户端数量与同一]{style="font-family:宋体"}[AC]{lang="EN-US"}[内其他]{style="font-family:宋体"}[Radio]{lang="EN-US"}[上的在线客户端数量最小者的差值。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_73594_93986_x258556174}

[[当]{style="font-family:宋体"}[Radio]{lang="EN-US"}]{#struct_0_73594_93986_291845835}[上的在线客户端数量达到]{style="font-family:宋体"}[/]{lang="EN-US"}[超过会话门限值并且与同一]{style="font-family:宋体"}[AC]{lang="EN-US"}[内其他]{style="font-family:宋体"}[Radio]{lang="EN-US"}[上的在线客户端数量最小者的差值达到]{style="font-family:宋体"}[/]{lang="EN-US"}[超过会话差值门限值，]{style="font-family:宋体"}[Radio]{lang="EN-US"}[开始运行负载均衡。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73594_93986_455515645}

[[\# ]{lang="EN-US"}]{#struct_0_73594_93986_x1702210553}[配置负载均衡模式为会话模式，会话门限值为]{style="font-family:宋体"}[7]{lang="EN-US"}[，会话差值门限值为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_73594_93986_918131613}

[\[Sysname\] wlan load-balance mode session 7 gap 5]{lang="EN-US"}
:::

::: {#-558283673 .myid}
[]{#_Toc404795223}[]{#struct_0_73594_93986_1401847510}[]{#_Toc398190400}[]{#_Toc402462262}

**负载均衡 \-- 负载均衡配置命令 \-- wlan load-balance mode traffic**

------------------------------------------------------------------------

[**[wlan load-balance mode traffic]{lang="EN-US"}**]{#struct_0_73594_93986_750092466}[命令用来配置负载均衡模式为流量模式。]{style="font-family:
宋体"}

[**[undo wlan load-balance ]{lang="EN-US"}[mode]{lang="EN-US"}**]{#struct_0_73594_93986_139058618}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73594_93986_2146255176}

[**[wlan load-balance mode traffic]{lang="EN-US"}**[ *value* \[ **gap** *gap-value* \]]{lang="EN-US"}]{#struct_0_73594_93986_x2084710083}

[**[undo wlan load-balance ]{lang="EN-US"}[mode]{lang="EN-US"}**]{#struct_0_73594_93986_x1338746701}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_73594_93986_x1957360876}

[[负载均衡模式为会话模式。]{style="font-family:宋体"}]{#struct_0_73594_93986_x1121004844}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73594_93986_x2051437161}

[[系统视图]{style="font-family:宋体"}]{#struct_0_73594_93986_x1700086570}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73594_93986_x547450225}

[[network-admin]{lang="EN-US"}]{#struct_0_73594_93986_x397864625}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73594_93986_1435826455}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73594_93986_1107503840}

[*[value]{lang="EN-US"}*]{#struct_0_73594_93986_x367415640}[：流量门限值，该参数表示]{style="font-family:宋体"}[Radio]{lang="EN-US"}[上的数据流量占]{style="font-family:宋体"}[Radio]{lang="EN-US"}[最大支持带宽的百分比数值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[80]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[gap-value]{lang="EN-US"}*]{#struct_0_73594_93986_x551458737}[：流量差值门限值，该参数表示流量差值占]{style="font-family:宋体"}[Radio]{lang="EN-US"}[最大支持带宽的百分比数值，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[40]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[20]{lang="EN-US"}[。流量差值即当前]{style="font-family:宋体"}[Radio]{lang="EN-US"}[上的数据流量与同一]{style="font-family:宋体"}[AC]{lang="EN-US"}[内其他]{style="font-family:宋体"}[Radio]{lang="EN-US"}[上的流数据量最小者的差值。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_73594_93986_x1879533725}

[[当]{style="font-family:宋体"}[Radio]{lang="EN-US"}]{#struct_0_73594_93986_x1520886668}[上的流量达到]{style="font-family:宋体"}[/]{lang="EN-US"}[超过流量门限值并且与同一]{style="font-family:宋体"}[AC]{lang="EN-US"}[内其他]{style="font-family:宋体"}[Radio]{lang="EN-US"}[上的流量最小者的差值达到]{style="font-family:宋体"}[/]{lang="EN-US"}[超过流量差值门限值，]{style="font-family:宋体"}[Radio]{lang="EN-US"}[开始运行负载均衡。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73594_93986_x2049351036}

[[\# ]{lang="EN-US"}]{#struct_0_73594_93986_x939862315}[配置负载均衡模式为流量模式，流量门限值为占]{style="font-family:宋体"}[Radio]{lang="EN-US"}[最大支持带宽的]{style="font-family:宋体"}[25%]{lang="EN-US"}[，流量差值门限值为占]{style="font-family:宋体"}[Radio]{lang="EN-US"}[最大支持带宽的]{style="font-family:宋体"}[20%]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_73594_93986_x2145203124}

[\[Sysname\] wlan load-balance mode traffic 25 gap 20]{lang="EN-US"}
:::

::: {#-280314656 .myid}
[]{#_Toc404795224}[]{#struct_0_73594_93986_x1926769500}[]{#_Toc398190403}[]{#_Toc402462263}

**负载均衡 \-- 负载均衡配置命令 \-- wlan load-balance rssi-threshold**

------------------------------------------------------------------------

[**[wlan load-balance rssi-threshold]{lang="EN-US"}**]{#struct_0_73594_93986_677446194}[命令用来配置负载均衡]{style="font-family:宋体"}[RSSI]{lang="EN-US"}[门限。]{style="font-family:宋体"}

[**[undo wlan load-balance rssi-threshold]{lang="EN-US"}**]{#struct_0_73594_93986_x2126601730}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73594_93986_x124475535}

[**[wlan load-balance rssi-threshold]{lang="EN-US"}**[ *rssi-threshold*]{lang="EN-US"}]{#struct_0_73594_93986_x1301372024}

[**[undo wlan load-balance rssi-threshold]{lang="EN-US"}**]{#struct_0_73594_93986_186642884}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_73594_93986_x1980387732}

[[负载均衡]{style="font-family:宋体"}[RSSI]{lang="EN-US"}]{#struct_0_73594_93986_2000813025}[门限值为]{style="font-family:宋体"}[25]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73594_93986_1018405320}

[[系统视图]{style="font-family:宋体"}]{#struct_0_73594_93986_x582000012}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73594_93986_1781154822}

[[network-admin]{lang="EN-US"}]{#struct_0_73594_93986_x1356969536}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73594_93986_273571628}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73594_93986_371990332}

[*[rssi-threshold]{lang="EN-US"}*]{#struct_0_73594_93986_749772232}[：负载均衡]{style="font-family:宋体"}[RSSI]{lang="EN-US"}[门限值，取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_73594_93986_x888637747}

[[如果]{style="font-family:宋体"}[Radio]{lang="EN-US"}]{#struct_0_73594_93986_401253121}[检测到客户端的]{style="font-family:宋体"}[RSSI]{lang="EN-US"}[值低于设定值，则该]{style="font-family:宋体"}[Radio]{lang="EN-US"}[将判定该客户端没有被检测到。如果只有过载的]{style="font-family:宋体"}[Radio]{lang="EN-US"}[可以检测到某客户端，则即使该]{style="font-family:宋体"}[Radio]{lang="EN-US"}[已经过载，也会通过减少该客户端的]{style="font-family:宋体"}[最大拒绝关联请求次数]{style="font-family:宋体"}[，增大该客户端接入的概率。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73594_93986_x1325565015}

[[\# ]{lang="EN-US"}]{#struct_0_73594_93986_292308990}[配置负载均衡]{style="font-family:宋体"}[RSSI]{lang="EN-US"}[门限值为]{style="font-family:宋体"}[40]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_73594_93986_x252755758}

[\[Sysname\] wlan load-balance rssi-threshold 40]{lang="EN-US"}

[ ]{lang="EN-US"}
:::
