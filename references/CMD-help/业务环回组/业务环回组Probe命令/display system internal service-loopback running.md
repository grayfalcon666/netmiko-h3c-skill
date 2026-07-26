::: {#-70581985 .myid}
[]{#_Toc404800433}[]{#struct_0_20305_x5074_774932233}[]{#_Toc342816090}

**业务环回组 \-- 业务环回组Probe命令 \-- display system internal service-loopback running**

------------------------------------------------------------------------

[**[display system internal service-loopback running]{lang="EN-US"}**]{#struct_0_20305_x5074_1605714105}[命令用来显示业务环回组的运行数据。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20305_x5074_330626548}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20305_x5074_1430741557}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal service-loopback ]{lang="EN-US"}[running]{lang="EN-US"}**]{#struct_0_20305_x5074_x955473884}**[ group ]{lang="EN-US"}***[group-number]{lang="EN-US"}[ ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20305_x5074_672568512}[模式：]{style="font-family:宋体"}

[**[display system internal service-loopback ]{lang="EN-US"}[running ]{lang="EN-US"}**]{#struct_0_20305_x5074_x2067417243}**[group ]{lang="EN-US"}***[group-number]{lang="EN-US"}***[ chassis]{lang="EN-US"}**[ ]{lang="EN-US"}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*

[[【视图】]{style="font-family:黑体"}]{#struct_0_20305_x5074_1026221117}

[[Probe]{lang="EN-US"}]{#struct_0_20305_x5074_744138940}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20305_x5074_1688421218}

[[network-admin]{lang="EN-US"}]{#struct_0_20305_x5074_775259913}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20305_x5074_x198362303}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20305_x5074_998784142}

[**[group ]{lang="EN-US"}***[group-number]{lang="EN-US"}*]{#struct_0_20305_x5074_1545538207}[：显示指定环回组的信息，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}[ ]{lang="EN-US"}**]{#struct_0_20305_x5074_450291722}*[slot-mumber]{lang="EN-US"}*[：显示指定单板的业务环回组信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}[ ]{lang="EN-US"}**]{#struct_0_20305_x5074_x799184016}*[slot-mumber]{lang="EN-US"}*[：显示指定成员设备的业务环回组信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_20305_x5074_x1387005940}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：表示成员设备上指定单板的业务环回组信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20305_x5074_x1622493680}

[[该命令可以用于了解当前系统指定业务环回组在各板的运行状态和驱动信息，方便定位与驱动配合的问题和分布式环境下各板信息不一致的问题。]{style="font-family:宋体"}]{#struct_0_20305_x5074_775325449}
:::

::: {#974717415 .myid}
[]{#_Toc404800434}[]{#struct_0_20305_x5074_x209677708}[]{#_Toc342816091}[]{#_Toc361304855}[]{#_Toc361304856}[]{#_Toc361304857}[]{#_Toc361304858}[]{#_Toc361304859}[]{#_Toc361304860}[]{#_Toc361304861}[]{#_Toc361304862}[]{#_Toc361304863}[]{#_Toc361304864}[]{#_Toc361304865}[]{#_Toc361304866}[]{#_Toc361304867}[]{#_Toc361304868}[]{#_Toc361304869}[]{#_Toc361304870}[]{#_Toc361304908}

**业务环回组 \-- 业务环回组Probe命令 \-- display system internal service-loopback interface-list**

------------------------------------------------------------------------

[**[display system internal service-loopback interface-list]{lang="EN-US"}**]{#struct_0_20305_x5074_775063306}[命令用来显示接口事件处理队列节点信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20305_x5074_x50484079}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20305_x5074_x2073628178}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal service-loopback interface-list slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_20305_x5074_x1474517072}*[slot-number]{lang="EN-US"}*

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20305_x5074_x89885153}[模式：]{style="font-family:宋体"}

[**[display system internal service-loopback interface-list]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_20305_x5074_x243617265}**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}*[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*

[[【视图】]{style="font-family:黑体"}]{#struct_0_20305_x5074_x1344615797}

[[Probe]{lang="EN-US"}]{#struct_0_20305_x5074_x138632079}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20305_x5074_x1466971124}

[[network-admin]{lang="EN-US"}]{#struct_0_20305_x5074_774866698}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20305_x5074_16805247}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20305_x5074_815741470}

[**[slot]{lang="EN-US"}[ ]{lang="EN-US"}**]{#struct_0_20305_x5074_49834954}*[slot-mumber]{lang="EN-US"}*[：表示指定单板的接口事件队列信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}[ ]{lang="EN-US"}**]{#struct_0_20305_x5074_x103371235}*[slot-mumber]{lang="EN-US"}*[：显示指定成员设备的接口事件队列信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_20305_x5074_x1662884449}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：表示成员设备上指定单板的接口事件队列信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20305_x5074_274798661}

[[该命令用于定位接口事件处理过程中出现的时序问题。]{style="font-family:宋体"}]{#struct_0_20305_x5074_774932234}

[ ]{lang="EN-US"}
:::
