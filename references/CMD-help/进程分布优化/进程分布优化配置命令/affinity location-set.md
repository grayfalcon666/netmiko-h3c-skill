::: {#1718519777 .myid}
[]{#_Toc404796278}[]{#struct_0_52320_18393_1565828875}

**进程分布优化 \-- 进程分布优化配置命令 \-- affinity location-set**

------------------------------------------------------------------------

[**[affinity location-set]{lang="EN-US"}**]{#struct_0_52320_18393_1845931506}[命令用来设置进程对于节点位置的偏好。]{style="font-family:宋体"}

[**[undo affinity location-set]{lang="EN-US"}**]{#struct_0_52320_18393_1861990218}[命令用来取消设置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_52320_18393_x1359753711}

[**[affinity location-set ]{lang="EN-US"}**[{ **slot** *slot-number* \[ **cpu** *cpu-number* \] }&\<1-5\> { **attract** *strength* \| **default** \| **none** \| **repulse** *strength* }]{lang="EN-US"}]{#struct_0_52320_18393_x151806381}

[**[undo affinity location-set ]{lang="EN-US"}**[{ **slot** *slot-number* \[ **cpu** *cpu-number* \] }&\<1-5\>]{lang="EN-US"}]{#struct_0_52320_18393_x381601933}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_52320_18393_1301330372}[模式：]{style="font-family:宋体"}

[**[affinity location-set ]{lang="EN-US"}**[{ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] }&\<1-5\> { **attract** *strength* \| **default** \| **none** \| **repulse** *strength* }]{lang="EN-US"}]{#struct_0_52320_18393_x2080824308}

[**[undo affinity location-set ]{lang="EN-US"}**[{ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] }&\<1-5\>]{lang="EN-US"}]{#struct_0_52320_18393_x154848622}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_52320_18393_1249417191}

[[系统未配置进程对节点位置的偏好。]{style="font-family:宋体"}]{#struct_0_52320_18393_2127428690}

[[【视图】]{style="font-family:黑体"}]{#struct_0_52320_18393_x236663628}

[[分布策略视图]{style="font-family:宋体"}]{#struct_0_52320_18393_713906030}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_52320_18393_x1359819247}

[[network-admin]{lang="EN-US"}]{#struct_0_52320_18393_x190416412}

[[mdc-admin]{lang="EN-US"}]{#struct_0_52320_18393_x800125094}

[[【参数】]{style="font-family:黑体"}]{#struct_0_52320_18393_705443807}

[[{ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] }&\<1-5\>]{lang="EN-US"}]{#struct_0_52320_18393_205949767}[：表示当前进程在指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上运行的偏好。其中：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[chassis]{lang="EN-US"}***[ chassis-number]{lang="EN-US"}*]{#struct_0_52320_18393_56355030}[：表示设备在]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{lang="EN-US" style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式设备－]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{lang="EN-US" style="font-family:宋体"}[）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_52320_18393_x185763462}[：暂无意义，取值始终为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[。（集中式设备）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_52320_18393_1150144624}[：表示单板所在的槽位号。（分布式设备－独立运行模式]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_52320_18393_797528708}[：表示设备在]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cpu]{lang="EN-US"}***[ cpu-number]{lang="EN-US"}*]{#struct_0_52320_18393_x1998233010}[：表示]{lang="EN-US" style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。如果单板上存在多个]{lang="EN-US" style="font-family:宋体"}[CPU]{lang="EN-US"}[（比如主]{lang="EN-US" style="font-family:宋体"}[CPU]{lang="EN-US"}[、辅助]{lang="EN-US" style="font-family:宋体"}[CPU]{lang="EN-US"}[等），需要使用该参数指定]{lang="EN-US" style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。如果不指定该参数，则表示主]{lang="EN-US" style="font-family:宋体"}[CPU]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[&\<1-5\>]{lang="EN-US"}]{#struct_0_52320_18393_x1086330967}[：表示前面的参数最多可以输入]{lang="EN-US" style="font-family:宋体"}[5]{lang="EN-US"}[次。]{lang="EN-US" style="font-family:宋体"}

[**[attract ]{lang="EN-US"}***[strength]{lang="EN-US"}*]{#struct_0_52320_18393_x1359360495}[：正向偏好程度，表示希望运行在该位置。]{style="font-family:宋体"}*[strength]{lang="EN-US"}*[表示]{style="font-family:宋体"}[偏好程度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100000]{lang="EN-US"}[。值越大表示进程运行在该位置的可能性越大。]{style="font-family:宋体"}

[**[default]{lang="EN-US"}**]{#struct_0_52320_18393_1818416099}[：缺省偏好，]{style="font-family:宋体"}[取值为正向偏好]{style="font-family:宋体"}[200]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_52320_18393_x469832226}[：设置偏好为]{style="font-family:宋体"}[0]{lang="EN-US"}[，即主进程对具体节点没有偏好，主进程的运行位置由系统来决定。]{style="font-family:宋体"}

[**[repulse]{lang="EN-US"}**[ ]{lang="EN-US"}*[strength]{lang="EN-US"}*]{#struct_0_52320_18393_2045905664}[：反向偏好程度，表示不希望运行在该位置。]{style="font-family:宋体"}*[strength]{lang="EN-US"}*[表示]{style="font-family:宋体"}[偏好程度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100000]{lang="EN-US"}[。值越大表示进程运行在该位置的可能性越小。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_52320_18393_1760024629}

[[\# ]{lang="EN-US"}]{#struct_0_52320_18393_x855562695}[设置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对于]{style="font-family:宋体"}[3]{lang="EN-US"}[号槽位的正向偏好为]{style="font-family:宋体"}[500]{lang="EN-US"}[。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_52320_18393_1981876541}

[\[Sysname\] placement program bgp]{lang="EN-US"}

[\[Sysname-program-bgp\] affinity location-set slot 3 attract 500]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_52320_18393_1137663908}[设置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对于]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[3]{lang="EN-US"}[号槽位的正向偏好为]{style="font-family:宋体"}[500]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_52320_18393_x1359426031}

[\[Sysname\] placement program bgp]{lang="EN-US"}

[\[Sysname-program-bgp\] affinity location-set chassis 1 slot 3 attract 500]{lang="EN-US"}
:::

::: {#-984750666 .myid}
[]{#_Toc404796279}[]{#struct_0_52320_18393_x1525037505}

**进程分布优化 \-- 进程分布优化配置命令 \-- affinity location-type**

------------------------------------------------------------------------

[**[affinity location-type]{lang="EN-US"}**]{#struct_0_52320_18393_1141017672}[命令用来设置进程对于位置类型的偏好。]{style="font-family:宋体"}

[**[undo affinity location-type]{lang="EN-US"}**]{#struct_0_52320_18393_x1683948332}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_52320_18393_x2086272755}

[**[affinity location-type]{lang="EN-US"}**[ { **current** \| **paired** \| **primary** } { **attract** *strength* \| **default** \| **none** \| **repulse** *strength* }]{lang="EN-US"}]{#struct_0_52320_18393_2146509966}

[**[undo affinity location-type]{lang="EN-US"}**[ { **current** \| **paired** \| **primary** }]{lang="EN-US"}]{#struct_0_52320_18393_x916958995}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_52320_18393_x1286768669}

[[系统未配置进程对位置类型的偏好。]{style="font-family:宋体"}]{#struct_0_52320_18393_x983052844}

[[【视图】]{style="font-family:黑体"}]{#struct_0_52320_18393_x1359884786}

[[分布策略视图]{style="font-family:宋体"}]{#struct_0_52320_18393_x210182023}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_52320_18393_x564270878}

[[network-admin]{lang="EN-US"}]{#struct_0_52320_18393_1419583644}

[[mdc-admin]{lang="EN-US"}]{#struct_0_52320_18393_x1639405907}

[[【参数】]{style="font-family:黑体"}]{#struct_0_52320_18393_106446782}

[**[current]{lang="EN-US"}**]{#struct_0_52320_18393_x480017529}[：用来设置对主控进程当前运行位置的偏好。主控进程当前运行位置可以通过]{style="font-family:宋体"}**[display placement program]{lang="EN-US"}**[命令查看。]{style="font-family:宋体"}

[**[paired]{lang="EN-US"}**]{#struct_0_52320_18393_x1403477543}[：用来设置对所有备份进程当前运行位置的偏好。]{style="font-family:宋体"}

[**[primary]{lang="EN-US"}**]{#struct_0_52320_18393_1978341453}[：用来设置对主用主控板的偏好。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[primary]{lang="EN-US"}**]{#struct_0_52320_18393_x1901543284}[：用来设置对主设备的偏好。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[primary]{lang="EN-US"}**]{#struct_0_52320_18393_x1359950322}[：用来设置对全局主用主控板的偏好。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[attract ]{lang="EN-US"}***[strength]{lang="EN-US"}*]{#struct_0_52320_18393_x1596779790}[：正向偏好程度，表示希望运行在该位置。]{style="font-family:宋体"}*[strength]{lang="EN-US"}*[表示]{style="font-family:宋体"}[偏好程度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100000]{lang="EN-US"}[。值越大表示进程运行在该位置类型的可能性越大。]{style="font-family:宋体"}

[**[default]{lang="EN-US"}**]{#struct_0_52320_18393_241742784}[：缺省偏好，]{style="font-family:宋体"}[取值为正向偏好]{style="font-family:宋体"}[200]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_52320_18393_2016177599}[：设置偏好为]{style="font-family:宋体"}[0]{lang="EN-US"}[，即主进程对位置类型没有偏好，主进程的运行位置由系统来决定。]{style="font-family:宋体"}

[**[repulse]{lang="EN-US"}**[ ]{lang="EN-US"}*[strength]{lang="EN-US"}*]{#struct_0_52320_18393_x1210290971}[：反向偏好程度，表示不希望运行在该位置。]{style="font-family:宋体"}*[strength]{lang="EN-US"}*[表示]{style="font-family:宋体"}[偏好程度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100000]{lang="EN-US"}[。值越大表示进程运行在该位置类型的可能性越小。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_52320_18393_1882258474}

[[\# ]{lang="EN-US"}]{#struct_0_52320_18393_1649070813}[设置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对于当前位置的正向偏好为]{style="font-family:宋体"}[500]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_52320_18393_x2107358250}

[\[Sysname\] placement program bgp]{lang="EN-US"}

[\[Sysname-program-bgp\] affinity location-type current attract 500]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_52320_18393_x1360015858}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[affinity location-set]{lang="EN-US"}**]{#struct_0_52320_18393_113288064}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[affinity program]{lang="EN-US"}**]{#struct_0_52320_18393_131404823}
:::

::: {#323014987 .myid}
[]{#_Toc404796280}[]{#struct_0_52320_18393_920955390}

**进程分布优化 \-- 进程分布优化配置命令 \-- affinity program**

------------------------------------------------------------------------

[**[affinity program]{lang="EN-US"}**]{#struct_0_52320_18393_x2050569004}[命令用来设置本进程和其它进程运行在同一位置的偏好。]{style="font-family:宋体"}

[**[undo affinity program]{lang="EN-US"}**]{#struct_0_52320_18393_1953625260}[命令用来取消设置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_52320_18393_393797058}

[**[affinity program]{lang="EN-US"}**[ *program-name* { **attract** *strength* \| **default** \| **none** \| **repulse** *strength* }]{lang="EN-US"}]{#struct_0_52320_18393_x757462150}

[**[undo affinity program ]{lang="EN-US"}***[program-name]{lang="EN-US"}*]{#struct_0_52320_18393_1917454679}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_52320_18393_x1360081394}

[[进程未配置和其它进程运行在同一位置的偏好。]{style="font-family:宋体"}]{#struct_0_52320_18393_x810617344}

[[【视图】]{style="font-family:黑体"}]{#struct_0_52320_18393_1650280318}

[[分布策略视图]{style="font-family:宋体"}]{#struct_0_52320_18393_1697850707}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_52320_18393_993023908}

[[network-admin]{lang="EN-US"}]{#struct_0_52320_18393_x1605475542}

[[mdc-admin]{lang="EN-US"}]{#struct_0_52320_18393_1400351906}

[[【参数】]{style="font-family:黑体"}]{#struct_0_52320_18393_x1581213528}

[*[program-name]{lang="EN-US"}*]{#struct_0_52320_18393_21904897}[：为当前设备上正在运行的进程的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，不区分大小写。用户可以通过]{style="font-family:宋体"}**[display placement program all]{lang="EN-US"}**[命令查看设备上正在运行的进程。]{style="font-family:宋体"}

[**[attract ]{lang="EN-US"}***[strength]{lang="EN-US"}*]{#struct_0_52320_18393_1009921824}[：正向偏好程度，表示希望运行在该位置。]{style="font-family:宋体"}*[strength]{lang="EN-US"}*[表示]{style="font-family:宋体"}[偏好程度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100000]{lang="EN-US"}[。值越大表示进程运行于同一位置的可能性越大。]{style="font-family:宋体"}

[**[default]{lang="EN-US"}**]{#struct_0_52320_18393_x1359622642}[：缺省偏好，]{style="font-family:宋体"}[取值为正向偏好]{style="font-family:宋体"}[200]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_52320_18393_581259678}[：设置偏好为]{style="font-family:宋体"}[0]{lang="EN-US"}[，即主进程对于是否和其它其它进程运行在同一位置没有偏好，主进程的运行位置由系统来决定。]{style="font-family:宋体"}

[**[repulse]{lang="EN-US"}**[ ]{lang="EN-US"}*[strength]{lang="EN-US"}*]{#struct_0_52320_18393_368500148}[：反向偏好程度，表示不希望运行在该位置。]{style="font-family:宋体"}*[strength]{lang="EN-US"}*[表示]{style="font-family:宋体"}[偏好程度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100000]{lang="EN-US"}[。值越大表示进程运行于同一位置的可能性越小。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_52320_18393_2095571858}

[[该配置方式以其它进程通过进程分布策略计算出来的预测位置为参照物，配置的是本进程和其它进程运行在同一位置的偏好。]{style="font-family:宋体"}]{#struct_0_52320_18393_359585719}

[[【举例】]{style="font-family:黑体"}]{#struct_0_52320_18393_235651926}

[[\# ]{lang="EN-US"}]{#struct_0_52320_18393_x1350940430}[设置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[和]{style="font-family:宋体"}[BGP]{lang="EN-US"}[运行于同一位置的偏好为反向]{style="font-family:宋体"}[200]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_52320_18393_x1455683157}

[\[Sysname\] placement program ospf]{lang="EN-US"}

[\[Sysname-program-ospf\] affinity program bgp repulse 200]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_52320_18393_x200308667}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[affinity location-set]{lang="EN-US"}**]{#struct_0_52320_18393_x1359688178}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[affinity location-type]{lang="EN-US"}**]{#struct_0_52320_18393_x1722758731}
:::

::: {#11231021 .myid}
[]{#_Toc404796281}[]{#struct_0_52320_18393_x1475765059}

**进程分布优化 \-- 进程分布优化配置命令 \-- affinity self**

------------------------------------------------------------------------

[**[affinity self]{lang="EN-US"}**]{#struct_0_52320_18393_2032736780}[命令用来设置本进程所有实例运行于同一位置的偏好。]{style="font-family:宋体"}

[**[undo affinity self]{lang="EN-US"}**]{#struct_0_52320_18393_1531125565}[命令用来取消设置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_52320_18393_1201720826}

[**[affinity self]{lang="EN-US"}**[ { **attract** *strength* \| **default** \| **none** \| **repulse** *strength* }]{lang="EN-US"}]{#struct_0_52320_18393_x1429068917}

[**[undo affinity self]{lang="EN-US"}**]{#struct_0_52320_18393_x1235680986}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_52320_18393_x1086115479}

[[进程未配置所有实例运行于同一位置的偏好。]{style="font-family:宋体"}]{#struct_0_52320_18393_x1359753714}

[[【视图】]{style="font-family:黑体"}]{#struct_0_52320_18393_x911321268}

[[分布策略视图]{style="font-family:宋体"}]{#struct_0_52320_18393_x513516121}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_52320_18393_132758453}

[[network-admin]{lang="EN-US"}]{#struct_0_52320_18393_x747347760}

[[mdc-admin]{lang="EN-US"}]{#struct_0_52320_18393_x119617025}

[[【参数】]{style="font-family:黑体"}]{#struct_0_52320_18393_1161906040}

[**[attract ]{lang="EN-US"}***[strength]{lang="EN-US"}*]{#struct_0_52320_18393_x1624764853}[：正向偏好程度，表示希望运行在该位置。]{style="font-family:宋体"}*[strength]{lang="EN-US"}*[表示]{style="font-family:宋体"}[偏好程度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100000]{lang="EN-US"}[。值越大表示进程运行于同一位置的可能性越大。]{style="font-family:宋体"}

[**[default]{lang="EN-US"}**]{#struct_0_52320_18393_71706970}[：缺省偏好，]{style="font-family:宋体"}[取值为正向偏好]{style="font-family:宋体"}[200]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_52320_18393_x1359819250}[：设置偏好为]{style="font-family:宋体"}[0]{lang="EN-US"}[，即进程对]{style="font-family:宋体"}[所有实例是否运行于同一位置没有偏好，运行位置由系统来决定。]{style="font-family:宋体"}

[**[repulse]{lang="EN-US"}**[ ]{lang="EN-US"}*[strength]{lang="EN-US"}*]{#struct_0_52320_18393_x2112665177}[：反向偏好程度，表示不希望运行在该位置。]{style="font-family:宋体"}*[strength]{lang="EN-US"}*[表示]{style="font-family:宋体"}[偏好程度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100000]{lang="EN-US"}[。值越大表示进程运行于同一位置的可能性越小。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_52320_18393_x2120751426}

[[该配置用以决定一个进程的多个实例是否运行于同一个位置上，如果进程只有一个实例，则该配置不会产生作用。]{style="font-family:宋体"}]{#struct_0_52320_18393_1493606553}

[[本命令在进程的分布策略视图和进程任意实例的分布策略视图下配置效果相同，均对所有实例生效。多次配置该命令，最新配置生效。]{style="font-family:宋体"}]{#struct_0_52320_18393_x627293796}

[[进程是否包含多个实例可以通过]{style="font-family:宋体"}**[display placement program all]{lang="EN-US"}**]{#struct_0_52320_18393_719740543}[命令查看。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_52320_18393_x775775215}

[[\# ]{lang="EN-US"}]{#struct_0_52320_18393_554590321}[设置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[进程所有实例运行于同一位置的偏好为反向]{style="font-family:宋体"}[200]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_52320_18393_x1359360498}

[\[Sysname\] placement program bgp]{lang="EN-US"}

[\[Sysname-program-bgp\] affinity self repulse 200]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_52320_18393_x1360805950}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[affinity location-set]{lang="EN-US"}**]{#struct_0_52320_18393_1756178834}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[affinity location-type]{lang="EN-US"}**]{#struct_0_52320_18393_x831403574}
:::

::: {#-294899052 .myid}
[]{#_Toc404796282}[]{#struct_0_52320_18393_1381455667}[]{#_Toc353350575}

**进程分布优化 \-- 进程分布优化配置命令 \-- display ha service-group**

------------------------------------------------------------------------

[**[display ha service-group]{lang="EN-US"}**]{#struct_0_52320_18393_x1475166733}[命令用来显示服务组的当前位置和状态等信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_52320_18393_x1317052819}

[**[display ha service-group ]{lang="EN-US"}**[{ *program-name* \[ **instance** *instance-name* \] \| **all** }]{lang="EN-US"}]{#struct_0_52320_18393_x8985307}

[[【视图】]{style="font-family:黑体"}]{#struct_0_52320_18393_1223509865}

[[任意视图]{style="font-family:宋体"}]{#struct_0_52320_18393_1637239978}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_52320_18393_x1359426034}

[[network-admin]{lang="EN-US"}]{#struct_0_52320_18393_x765522618}

[[network-operator]{lang="EN-US"}]{#struct_0_52320_18393_1595148889}

[[mdc-admin]{lang="EN-US"}]{#struct_0_52320_18393_x2035305555}

[[mdc-operator]{lang="EN-US"}]{#struct_0_52320_18393_x1123788942}

[[【参数】]{style="font-family:黑体"}]{#struct_0_52320_18393_x1285030536}

[*[program-name]{lang="EN-US"}*]{#struct_0_52320_18393_1483592982}[：为当前设备上正在运行的服务组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_52320_18393_2020052385}[：表示当前设备上运行的所有服务组。]{style="font-family:宋体"}

[**[instance ]{lang="EN-US"}***[instance-name]{lang="EN-US"}*]{#struct_0_52320_18393_x2013982579}[：表示实例名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，不区分大小写。一个服务组是否存在多个实例，由系统软件决定。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_52320_18393_x1359884785}

[[\# ]{lang="EN-US"}]{#struct_0_52320_18393_193102504}[显示所有服务组主控进程的位置和状态信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display ha service-group all]{lang="EN-US"}]{#struct_0_52320_18393_793824792}

[Service Group                     Current Location      State]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ospf                              0/0                   Realtime Backup]{lang="EN-US"}

[bgp                               1/0                   Batch Backup]{lang="EN-US"}

[isis                              0/0                   Stopping]{lang="EN-US"}

[rip                               1/0                   Realtime Backup]{lang="EN-US"}

[ripng                             1/0                   Upgrading]{lang="EN-US"}

[staticroute                       1/0                   Batch Backup]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_52320_18393_2134089092}[显示指定服务组主控进程的位置和状态信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display ha service-group staticroute]{lang="EN-US"}]{#struct_0_52320_18393_x1359950321}

[Service Group                     Current Location      State]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[staticroute                       1/0 (Active)          Batch Backup]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Detailed information about services of the program:]{lang="EN-US"}

[  Service           PID    Type      Location   State]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  ifm               200    Standby   0/0        Realtime Backup]{lang="EN-US"}

[  staticroute       200    Standby   0/0        Batch Backup]{lang="EN-US"}

[  ifm               200    Active    1/0        Realtime Backup]{lang="EN-US"}

[  staticroute       200    Active    1/0        Batch Backup]{lang="EN-US"}

[[以上显示信息表明（以]{style="font-family:宋体"}[staticroute]{lang="EN-US"}]{#struct_0_52320_18393_x30695849}[为例），服务组]{style="font-family:宋体"}[staticroute]{lang="EN-US"}[的主控进程当前运行于]{style="font-family:宋体"}[1]{lang="EN-US"}[号槽位单板的]{style="font-family:宋体"}[0]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上，当前状态是批量备份状态。服务组]{style="font-family:宋体"}[staticroute]{lang="EN-US"}[的备用进程当前运行于]{style="font-family:宋体"}[0]{lang="EN-US"}[号槽位单板的]{style="font-family:宋体"}[0]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上。服务组]{style="font-family:宋体"}[staticroute]{lang="EN-US"}[下有]{style="font-family:宋体"}[ifm]{lang="EN-US"}[和]{style="font-family:宋体"}[staticroute]{lang="EN-US"}[两个服务，]{style="font-family:宋体"}[PID]{lang="EN-US"}[分别是]{style="font-family:宋体"}[200]{lang="EN-US"}[和]{style="font-family:宋体"}[200]{lang="EN-US"}[，]{style="font-family:宋体"}[ifm]{lang="EN-US"}[当前状态是实时备份状态，]{style="font-family:宋体"}[staticroute]{lang="EN-US"}[当前状态是批量备份状态。]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_52320_18393_1029609128}[显示所有服务组主控进程的位置和状态信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display ha service-group all]{lang="EN-US"}]{#struct_0_52320_18393_2103594255}

[Service Group                     Current Location      State]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ospf                              1/0/0                 Realtime Backup]{lang="EN-US"}

[bgp                               1/1/0                 Batch Backup]{lang="EN-US"}

[isis                              1/1/0                 Stopping]{lang="EN-US"}

[rip                               1/0/0                 Realtime Backup]{lang="EN-US"}

[ripng                             2/0/0                 Upgrading]{lang="EN-US"}

[staticroute                       1/0/0                 Batch Backup]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_52320_18393_x2078610949}[显示指定进程主备身份及当前状态。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\>display ha service-group staticroute]{lang="EN-US"}]{#struct_0_52320_18393_x1360015857}

[Service Group                     Current Location      State]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[staticroute                       1/0/0 (Active)        Batch Backup]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Detailed information about services of the program:]{lang="EN-US"}

[  Service           PID    Type      Location   State]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  ifm               200    Active    1/0/0      Realtime Backup]{lang="EN-US"}

[  staticroute       200    Active    1/0/0      Batch Backup]{lang="EN-US"}

[  ifm               200    Standby   1/1/0      Realtime Backup]{lang="EN-US"}

[  staticroute       200    Standby   1/1/0      Batch Backup]{lang="EN-US"}

[  ifm               200    Standby   2/0/0      Realtime Backup]{lang="EN-US"}

[  staticroute       200    Standby   2/0/0      Batch Backup]{lang="EN-US"}

[[以上显示信息表明（以]{style="font-family:宋体"}[staticroute]{lang="EN-US"}]{#struct_0_52320_18393_x1903134571}[为例），服务组]{style="font-family:宋体"}[staticroute]{lang="EN-US"}[的主控进程当前运行于设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[0]{lang="EN-US"}[号槽位单板的]{style="font-family:
宋体"}[0]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上，当前状态是批量备份状态。服务组]{style="font-family:宋体"}[staticroute]{lang="EN-US"}[的备用进程当前运行于设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[1]{lang="EN-US"}[号槽位单板的]{style="font-family:宋体"}[0]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上和设备]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[0]{lang="EN-US"}[号槽位单板的]{style="font-family:
宋体"}[0]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上。服务组]{style="font-family:宋体"}[staticroute]{lang="EN-US"}[下有]{style="font-family:宋体"}[ifm]{lang="EN-US"}[和]{style="font-family:宋体"}[staticroute]{lang="EN-US"}[两个服务，]{style="font-family:宋体"}[PID]{lang="EN-US"}[分别是]{style="font-family:宋体"}[200]{lang="EN-US"}[和]{style="font-family:宋体"}[200]{lang="EN-US"}[，]{style="font-family:宋体"}[ifm]{lang="EN-US"}[当前状态是实时备份状态，]{style="font-family:宋体"}[staticroute]{lang="EN-US"}[当前状态是批量备份状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[display ha service-group]{lang="EN-US"}]{#struct_0_52320_18393_2034070062}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1833606636}[[字段]{style="font-family:黑体"}]{#struct_0_52320_18393_996608160}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_52320_18393_x702028305}

[[Service Group]{lang="EN-US"}]{#struct_0_52320_18393_x2137418411}

[[服务组的名称]{style="font-family:宋体"}]{#struct_0_52320_18393_x1360081393}

[[Type]{lang="EN-US"}]{#struct_0_52320_18393_x407332817}

[[进程的主备身份，取值为：]{style="font-family:宋体"}]{#struct_0_52320_18393_1116276684}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_52320_18393_x644026731}[：表示服务组主控进程]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Standby]{lang="EN-US"}]{#struct_0_52320_18393_x1765911350}[：表示服务组备用进程]{lang="EN-US" style="font-family:宋体"}

[[Service]{lang="EN-US"}]{#struct_0_52320_18393_x472291696}

[[服务组内的服务的名称]{style="font-family:宋体"}]{#struct_0_52320_18393_1058639161}

[[State]{lang="EN-US"}]{#struct_0_52320_18393_x1359622641}

[[进程的状态：]{style="font-family:宋体"}]{#struct_0_52320_18393_x984824263}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Realtime Backup]{lang="EN-US"}]{#struct_0_52320_18393_482809816}[：实时备份状态]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Batch Backup]{lang="EN-US"}]{#struct_0_52320_18393_x508378193}[：批量备份状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stopping]{lang="EN-US"}]{#struct_0_52320_18393_x1232955921}[：停止状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Degrading]{lang="EN-US"}]{#struct_0_52320_18393_523513864}[：降级状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Upgrading]{lang="EN-US"}]{#struct_0_52320_18393_x1359688177}[：升级状态]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#394205137 .myid}
[]{#_Toc404796283}[]{#struct_0_52320_18393_x1319474204}

**进程分布优化 \-- 进程分布优化配置命令 \-- display placement location**

------------------------------------------------------------------------

[**[display placement location]{lang="EN-US"}**]{#struct_0_52320_18393_550367914}[命令用来显示具体位置上正在运行的进程信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_52320_18393_765209890}

[**[display placement location ]{lang="EN-US"}**[{ **all** \| **slot** *slot-number* \[ **cpu** *cpu-number* \] }]{lang="EN-US"}]{#struct_0_52320_18393_1180676194}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_52320_18393_994533485}[模式：]{style="font-family:宋体"}

[**[display placement location ]{lang="EN-US"}**[{ **all** \| **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] }]{lang="EN-US"}]{#struct_0_52320_18393_940478354}

[[【视图】]{style="font-family:黑体"}]{#struct_0_52320_18393_58641658}

[[任意视图]{style="font-family:宋体"}]{#struct_0_52320_18393_x1359753713}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_52320_18393_1010993033}

[[network-admin]{lang="EN-US"}]{#struct_0_52320_18393_1142662700}

[[network-operator]{lang="EN-US"}]{#struct_0_52320_18393_x262907298}

[[mdc-admin]{lang="EN-US"}]{#struct_0_52320_18393_1036734959}

[[mdc-operator]{lang="EN-US"}]{#struct_0_52320_18393_x243580333}

[[【参数】]{style="font-family:黑体"}]{#struct_0_52320_18393_1355682094}

[**[all]{lang="EN-US"}**]{#struct_0_52320_18393_x18924640}[：表示当前设备上运行的所有进程。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_52320_18393_75771262}[：暂无意义，取值始终为]{style="font-family:宋体"}[0]{lang="EN-US"}[。（集中式设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_52320_18393_x1359819249}[：表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_52320_18393_259922282}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_52320_18393_1075667637}[：表示指定成员设备上的指定单板。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，表示所有主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}***[ cpu-number]{lang="EN-US"}*]{#struct_0_52320_18393_x1170506807}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号，该参数的取值范围与设备的型号有关，请以设备的实际情况为准。如果单板上存在多个]{style="font-family:宋体"}[CPU]{lang="EN-US"}[（比如主]{style="font-family:宋体"}[CPU]{lang="EN-US"}[、辅助]{style="font-family:宋体"}[CPU]{lang="EN-US"}[等），需要使用该参数指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。如果不指定该参数，则表示主]{style="font-family:宋体"}[CPU]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_52320_18393_2137844384}

[[\# ]{lang="EN-US"}]{#struct_0_52320_18393_1093219630}[显示设备上正在运行的进程信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display placement location slot 0]{lang="EN-US"}]{#struct_0_52320_18393_x1359360497}

[Program(s) placed at location: 0/0]{lang="EN-US"}

[  l3vpn]{lang="EN-US"}

[  lsm]{lang="EN-US"}

[  aaa]{lang="EN-US"}

[  lauth]{lang="EN-US"}

[  track]{lang="EN-US"}

[  bfd]{lang="EN-US"}

[  rm6]{lang="EN-US"}

[  rm]{lang="EN-US"}

[  rpm]{lang="EN-US"}

[  usr6]{lang="EN-US"}

[  ipaddr]{lang="EN-US"}

[  ip6addr]{lang="EN-US"}

[  slsp]{lang="EN-US"}

[  usr]{lang="EN-US"}

[  ethbase]{lang="EN-US"}

[  ip6base]{lang="EN-US"}

[  ipbase]{lang="EN-US"}

[  eth ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_52320_18393_655616685}[显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号槽单板上正在运行的进程信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display placement location slot 1]{lang="EN-US"}]{#struct_0_52320_18393_x1359426033}

[Program(s) placed at location: 1/0]{lang="EN-US"}

[  l3vpn]{lang="EN-US"}

[  lsm]{lang="EN-US"}

[  aaa]{lang="EN-US"}

[  lauth]{lang="EN-US"}

[  track]{lang="EN-US"}

[  bfd]{lang="EN-US"}

[  rm6]{lang="EN-US"}

[  rm]{lang="EN-US"}

[  rpm]{lang="EN-US"}

[  usr6]{lang="EN-US"}

[  ipaddr]{lang="EN-US"}

[  ip6addr]{lang="EN-US"}

[  slsp]{lang="EN-US"}

[  usr]{lang="EN-US"}

[  ethbase]{lang="EN-US"}

[  ip6base]{lang="EN-US"}

[  ipbase]{lang="EN-US"}

[  eth ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_52320_18393_1607130377}[显示成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[0]{lang="EN-US"}[号槽位单板上正在运行的进程信息。（分布式设备－]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display placement location chassis 1 slot 0]{lang="EN-US"}]{#struct_0_52320_18393_x1359884788}

[Program(s) placed at location: 1/0/0]{lang="EN-US"}

[  l3vpn]{lang="EN-US"}

[  lsm]{lang="EN-US"}

[  aaa]{lang="EN-US"}

[  lauth]{lang="EN-US"}

[  track]{lang="EN-US"}

[  bfd]{lang="EN-US"}

[  rm6]{lang="EN-US"}

[  rm]{lang="EN-US"}

[  rpm]{lang="EN-US"}

[  usr6]{lang="EN-US"}

[  ipaddr]{lang="EN-US"}

[  ip6addr]{lang="EN-US"}

[  slsp]{lang="EN-US"}

[  usr]{lang="EN-US"}

[  ethbase]{lang="EN-US"}

[  ip6base]{lang="EN-US"}

[  ipbase]{lang="EN-US"}

[  eth]{lang="EN-US"}
:::

::: {#1733442622 .myid}
[]{#_Toc404796284}[]{#struct_0_52320_18393_952617391}

**进程分布优化 \-- 进程分布优化配置命令 \-- display placement policy**

------------------------------------------------------------------------

[**[display placement policy]{lang="EN-US"}**]{#struct_0_52320_18393_x105992296}[命令用来显示进程的分布策略。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_52320_18393_x239400806}

[**[display placement policy program ]{lang="EN-US"}**[{ *program-name* \| **all** \| **default** }]{lang="EN-US"}]{#struct_0_52320_18393_x246357357}

[[【视图】]{style="font-family:黑体"}]{#struct_0_52320_18393_1500957163}

[[任意视图]{style="font-family:宋体"}]{#struct_0_52320_18393_897024153}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_52320_18393_x963192262}

[[network-admin]{lang="EN-US"}]{#struct_0_52320_18393_744950257}

[[network-operator]{lang="EN-US"}]{#struct_0_52320_18393_x1359950324}

[[mdc-admin]{lang="EN-US"}]{#struct_0_52320_18393_x790210736}

[[mdc-operator]{lang="EN-US"}]{#struct_0_52320_18393_x434821759}

[[【参数】]{style="font-family:黑体"}]{#struct_0_52320_18393_714501751}

[*[program-name]{lang="EN-US"}*]{#struct_0_52320_18393_1955849032}[：显示指定进程的分布策略，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_52320_18393_x580234169}[：显示所有配置的进程分布策略。]{style="font-family:宋体"}

[**[default]{lang="EN-US"}**]{#struct_0_52320_18393_1881216685}[：显示用户配置的缺省分布策略的信息。如果没有通过]{style="font-family:宋体"}**[placement program default]{lang="EN-US"}**[配置，则没有显示信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_52320_18393_x220110622}

[[只有为进程成功配置分布策略后，才会输出相应的显示信息。]{style="font-family:宋体"}]{#struct_0_52320_18393_x2119696173}

[[【举例】]{style="font-family:黑体"}]{#struct_0_52320_18393_428178124}

[[\# ]{lang="EN-US"}]{#struct_0_52320_18393_x1360015860}[显示缺省分布策略的信息。]{style="font-family:宋体"}

[[\<Sysname\> display placement policy program default]{lang="EN-US"}]{#struct_0_52320_18393_469321816}

[Program: \[default\]                                : source]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  affinity location-set slot 0 cpu 0 attract      : system \[default\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_52320_18393_1240440589}[显示]{style="font-family:宋体"}[aaa]{lang="EN-US"}[进程的分布策略。]{style="font-family:宋体"}

[[\<Sysname\> display placement policy program aaa]{lang="EN-US"}]{#struct_0_52320_18393_312951642}

[Program: aaa                                      : source]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  affinity location-set slot 0 cpu 7 attract      : system aaa]{lang="EN-US"}

[   100]{lang="EN-US"}

[  affinity location-set slot 0 cpu 1 attract      : system aaa]{lang="EN-US"}

[   100]{lang="EN-US"}

[  affinity location-set slot 0 cpu 0 attract      : system \[default\]]{lang="EN-US"}

[   100]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display placement policy]{lang="EN-US"}]{#struct_0_52320_18393_x784907633}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1835185742}[[字段]{style="font-family:黑体"}]{#struct_0_52320_18393_x1360081396}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_52320_18393_352182070}

[[Program]{lang="EN-US"}]{#struct_0_52320_18393_1036134901}

[[进程的名称以及进程的分布策略]{style="font-family:宋体"}]{#struct_0_52320_18393_x243055984}

[[source]{lang="EN-US"}]{#struct_0_52320_18393_618246801}

[[进程分布策略的来源，其中：]{style="font-family:宋体"}[system \[default\]]{lang="EN-US"}]{#struct_0_52320_18393_1703064722}[表示采用系统缺省分布策略，该策略是通过]{style="font-family:宋体"}**[placement program default]{lang="EN-US"}**[命令进入缺省分布策略视图后再配置的；]{style="font-family:宋体"}[system aaa]{lang="EN-US"}[表示采用]{style="font-family:宋体"}[AAA]{lang="EN-US"}[进程分布策略，该策略是通过]{style="font-family:宋体"}**[placement program ]{lang="EN-US"}***[program-name]{lang="EN-US"}*[命令进入]{style="font-family:宋体"}[AAA]{lang="EN-US"}[的分布策略视图后再配置的]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-270320695 .myid}
[]{#_Toc404796285}[]{#struct_0_52320_18393_218232407}

**进程分布优化 \-- 进程分布优化配置命令 \-- display placement program**

------------------------------------------------------------------------

[**[display placement program]{lang="EN-US"}**]{#struct_0_52320_18393_x1359622644}[命令用来显示主控进程的当前运行位置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_52320_18393_x225309376}

[**[display placement program]{lang="EN-US"}**[ { *program-name* \| **all** }]{lang="EN-US"}]{#struct_0_52320_18393_1478236785}

[[【视图】]{style="font-family:黑体"}]{#struct_0_52320_18393_1406005475}

[[任意视图]{style="font-family:宋体"}]{#struct_0_52320_18393_1496279798}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_52320_18393_x62046349}

[[network-admin]{lang="EN-US"}]{#struct_0_52320_18393_1880842033}

[[network-operator]{lang="EN-US"}]{#struct_0_52320_18393_1334676789}

[[mdc-admin]{lang="EN-US"}]{#struct_0_52320_18393_x2080166997}

[[mdc-operator]{lang="EN-US"}]{#struct_0_52320_18393_1579515231}

[[【参数】]{style="font-family:黑体"}]{#struct_0_52320_18393_x1359688180}

[*[program-name]{lang="EN-US"}*]{#struct_0_52320_18393_x2079972131}[：为当前设备上正在运行的进程的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_52320_18393_x1091314262}[：表示当前设备上运行的所有进程。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_52320_18393_803267475}

[[\# ]{lang="EN-US"}]{#struct_0_52320_18393_360733691}[显示]{style="font-family:宋体"}[AAA]{lang="EN-US"}[主控进程的当前运行位置。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display placement program aaa]{lang="EN-US"}]{#struct_0_52320_18393_970523707}

[Program                           Placed at location]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[aaa                               0/0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_52320_18393_x276783225}[显示]{style="font-family:宋体"}[AAA]{lang="EN-US"}[主控进程的当前运行位置。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display placement program aaa]{lang="EN-US"}]{#struct_0_52320_18393_x1359753716}

[Program                          Placed at Location]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[aaa                              1/0/0]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display placement program]{lang="EN-US"}]{#struct_0_52320_18393_251478146}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1829963195}[[字段]{style="font-family:黑体"}]{#struct_0_52320_18393_x1185840145}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_52320_18393_x1119810045}

[[Program]{lang="EN-US"}]{#struct_0_52320_18393_2016968529}

[[进程的名称]{style="font-family:宋体"}]{#struct_0_52320_18393_713923633}

[[Placed at location]{lang="EN-US"}]{#struct_0_52320_18393_x668265954}

[[主进程运行的位置]{style="font-family:宋体"}]{#struct_0_52320_18393_x73439323}

[[当显示为]{style="font-family:宋体"}[NA]{lang="EN-US"}]{#struct_0_52320_18393_x1359819252}[时表示该业务当前没有主进程（没有主进程的原因可能为：业务异常；主进程正在启动；主进程被关闭等）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1686608450 .myid}
[]{#_Toc404796286}[]{#struct_0_52320_18393_x949865763}

**进程分布优化 \-- 进程分布优化配置命令 \-- display placement reoptimize**

------------------------------------------------------------------------

[**[display placement reoptimize]{lang="EN-US"}**]{#struct_0_52320_18393_x960842753}[命令用来显示进程分布优化后的预测位置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_52320_18393_1241058041}

[**[display placement reoptimize program ]{lang="EN-US"}**[{ *program-name* \[ **instance** *instance-name* \] \| **all** }]{lang="EN-US"}]{#struct_0_52320_18393_x123213646}

[[【视图】]{style="font-family:黑体"}]{#struct_0_52320_18393_x12689789}

[[任意视图]{style="font-family:宋体"}]{#struct_0_52320_18393_x220099256}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_52320_18393_1713052130}

[[network-admin]{lang="EN-US"}]{#struct_0_52320_18393_x1359360500}

[[network-operator]{lang="EN-US"}]{#struct_0_52320_18393_x1716446485}

[[mdc-admin]{lang="EN-US"}]{#struct_0_52320_18393_x1943538519}

[[mdc-operator]{lang="EN-US"}]{#struct_0_52320_18393_x1596994218}

[[【参数】]{style="font-family:黑体"}]{#struct_0_52320_18393_x1343933201}

[*[program-name]{lang="EN-US"}*]{#struct_0_52320_18393_x443060315}[：为当前设备上正在运行的、支持进程优化配置的进程的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[instance ]{lang="EN-US"}***[instance-name]{lang="EN-US"}*]{#struct_0_52320_18393_1234702441}[：表示实例名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，不区分大小写。一个进程是否存在多个实例，由系统软件决定。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_52320_18393_x1498546700}[：表示当前设备上运行的、支持进程优化配置的所有进程。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_52320_18393_x1912431468}

[[\# ]{lang="EN-US"}]{#struct_0_52320_18393_x190496345}[显示分布优化后所有进程的预测位置。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display placement reoptimize program all]{lang="EN-US"}]{#struct_0_52320_18393_x1359426036}

[Predicted changes to the placement]{lang="EN-US"}

[Program                           Current location       New location]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[rm6                               1/0                    1/0]{lang="EN-US"}

[rm                                1/0                    1/0]{lang="EN-US"}

[rpm                               1/0                    1/0]{lang="EN-US"}

[usr                               1/0                    1/0]{lang="EN-US"}

[usr6                              1/0                    1/0]{lang="EN-US"}

[bgp                               1/0                    1/0]{lang="EN-US"}

[pim                               1/0                    1/0]{lang="EN-US"}

[igmp                              1/0                    1/0   ]{lang="EN-US"}

[[以上显示信息中，]{style="font-family:宋体"}[Program]{lang="EN-US"}]{#struct_0_52320_18393_x1928322032}[表示进程的名称，]{style="font-family:宋体"}[Current location]{lang="EN-US"}[表示主进程当前运行的位置，]{style="font-family:宋体"}[New location]{lang="EN-US"}[表示分布优化后，主进程将运行的位置。]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_52320_18393_x508231782}[显示分布优化后所有进程的预测位置。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display placement reoptimize program all]{lang="EN-US"}]{#struct_0_52320_18393_x1359884787}

[Predicted changes to the placement]{lang="EN-US"}

[Program                           Current location       New location]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[rm6                               1/0/0                  1/0/0]{lang="EN-US"}

[rm                                1/0/0                  1/0/0]{lang="EN-US"}

[rpm                               1/0/0                  1/0/0]{lang="EN-US"}

[usr                               1/0/0                  1/0/0]{lang="EN-US"}

[usr6                              1/0/0                  1/0/0]{lang="EN-US"}

[bgp                               1/0/0                  1/0/0]{lang="EN-US"}

[pim                               1/0/0                  1/0/0]{lang="EN-US"}

[igmp                              1/0/0                  1/0/0]{lang="EN-US"}

[[以上显示信息中，]{style="font-family:宋体"}[Program]{lang="EN-US"}]{#struct_0_52320_18393_1355901918}[表示进程的名称，]{style="font-family:宋体"}[Current location]{lang="EN-US"}[表示主进程当前运行的位置，]{style="font-family:宋体"}[New location]{lang="EN-US"}[表示分布优化后，主进程将运行的位置。]{style="font-family:宋体"}
:::

::: {#279713620 .myid}
[]{#_Toc404796287}[]{#struct_0_52320_18393_x1141526704}

**进程分布优化 \-- 进程分布优化配置命令 \-- placement program**

------------------------------------------------------------------------

[**[placement program]{lang="EN-US"}**]{#struct_0_52320_18393_x2132360124}[命令用来进入指定进程的分布策略视图。]{style="font-family:宋体"}

[**[undo placement program]{lang="EN-US"}**]{#struct_0_52320_18393_x2132899603}[命令用来删除指定进程的分布策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_52320_18393_1599699390}

[**[placement program ]{lang="EN-US"}**[{ *program-name* \[ **instance** *instance-name* \] \| **default** }]{lang="EN-US"}]{#struct_0_52320_18393_x60080384}

[**[undo placement program]{lang="EN-US"}**[ { *program-name* \[ **instance** *instance-name* \] \| **default** }]{lang="EN-US"}]{#struct_0_52320_18393_x940081850}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_52320_18393_x1359950323}

[[所有进程均未配置分布策略。所有进程的主控进程都在主用主控板上运行。（分布式设备－独立运行模式）]{style="font-family:宋体"}]{#struct_0_52320_18393_1132103565}

[[【视图】]{style="font-family:黑体"}]{#struct_0_52320_18393_542411161}

[[系统视图]{style="font-family:宋体"}]{#struct_0_52320_18393_x1762420903}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_52320_18393_1101330789}

[[network-admin]{lang="EN-US"}]{#struct_0_52320_18393_1600136197}

[[mdc-admin]{lang="EN-US"}]{#struct_0_52320_18393_x1764422409}

[[【参数】]{style="font-family:黑体"}]{#struct_0_52320_18393_1640119922}

[*[program-name]{lang="EN-US"}*]{#struct_0_52320_18393_x1941021397}[：用来进入指定进程的分布策略视图。]{style="font-family:宋体"}*[program-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[当前设备上正在运行的进程的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[instance ]{lang="EN-US"}***[instance-name]{lang="EN-US"}*]{#struct_0_52320_18393_x1360015859}[：用来进入指定进程指定实例的分布策略视图。]{style="font-family:宋体"}*[instance-name]{lang="EN-US"}*[表示实例名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，不区分大小写。一个进程是否存在多个实例，由系统软件决定。]{style="font-family:宋体"}

[**[default]{lang="EN-US"}**]{#struct_0_52320_18393_x1452795877}[：用来进入缺省分布策略视图。进入该视图后，配置的是所有进程（所有实例）的缺省分布策略。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_52320_18393_x334069826}

[[为了提高系统的可靠性，系统在运行过程中会对进程进行]{style="font-family:宋体"}[1:N]{lang="EN-US"}]{#struct_0_52320_18393_1056641518}[备份。当启动某个业务时，系统会自动同时为该业务运行一个主控进程和多个备份进程。]{style="font-family:宋体"}

[[对于一些业务，其主控进程只能运行在主用主控板，这样的进程不支持进程分布优化配置（配置时会提示失败）。当主控进程异常时，系统会自动重启该主控进程。备份进程主要用于主备倒换和]{style="font-family:宋体"}[ISSU]{lang="EN-US"}]{#struct_0_52320_18393_1363521587}[升级环境。]{style="font-family:宋体"}

[[另一些业务，其主控进程可以运行在主用主控板上，也可以运行在备用主控板上。当主控进程异常时，需要从备份进程中选举一个新的主控进程，从而保证业务不受影响。在众多的备份进程中到底选用哪个作为新的主控进程，由该进程的分布策略决定。]{style="font-family:宋体"}]{#struct_0_52320_18393_457099212}

[[分布策略的内容包括]{style="font-family:宋体"}**[affinity location-type]{lang="EN-US"}**]{#struct_0_52320_18393_x1399846926}[、]{style="font-family:宋体"}**[affinity location-set]{lang="EN-US"}**[、]{style="font-family:宋体"}**[affinity program]{lang="EN-US"}[和]{style="font-family:宋体"}[affinity self]{lang="EN-US"}**[，这些命令从不同角度表达了用户对进程在某个位置运行的期望。]{style="font-family:宋体"}

[[一个进程对应一个分布策略，所有的]{style="font-family:宋体"}**[affinity]{lang="EN-US"}**]{#struct_0_52320_18393_2025172272}[命令可以同时设置。系统将根据用户的配置按照一定的算法，最后决定主控进程的预测位置（可以通过]{style="font-family:宋体"}**[display placement reoptimize]{lang="EN-US"}**[命令查看）。当发生主备倒换时，该位置的进程就能当选为主控进程，其它位置的进程则均为备份进程。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_52320_18393_2021789741}

[[\# ]{lang="EN-US"}]{#struct_0_52320_18393_x1360081395}[进入]{style="font-family:宋体"}[BGP]{lang="EN-US"}[分布策略视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_52320_18393_755466597}

[\[Sysname\] placement program bgp]{lang="EN-US"}

[\[Sysname-program-bgp\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_52320_18393_293782364}[进入缺省分布策略视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_52320_18393_x356418511}

[\[Sysname\] placement program default]{lang="EN-US"}

[\[Sysname-program-default\]]{lang="EN-US"}
:::

::: {#1926012602 .myid}
[]{#_Toc404796288}[]{#struct_0_52320_18393_x197159072}

**进程分布优化 \-- 进程分布优化配置命令 \-- placement reoptimize**

------------------------------------------------------------------------

[**[placement reoptimize]{lang="EN-US"}**]{#struct_0_52320_18393_1590299690}[命令用来优化进程运行位置，使进程分布策略生效。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_52320_18393_x1436205196}

[**[placement reoptimize]{lang="EN-US"}**]{#struct_0_52320_18393_1605269474}

[[【视图】]{style="font-family:黑体"}]{#struct_0_52320_18393_x1359622643}

[[系统视图]{style="font-family:宋体"}]{#struct_0_52320_18393_2147343619}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_52320_18393_678478358}

[[network-admin]{lang="EN-US"}]{#struct_0_52320_18393_x2000034750}

[[mdc-admin]{lang="EN-US"}]{#struct_0_52320_18393_x1082147727}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_52320_18393_x520616739}

[[执行该命令后，系统会根据当前硬件的在位情况、主进程的运行位置和状态、分布策略的配置来综合计算主进程的新位置，并将该位置上的进程当选为主控进程，其它位置上的进程均为备份进程。如果新当选的主进程和原主进程不同，则会触发进程的主备倒换。因为只是主备进程间角色的转换，进程不需要重启，所以进程的主备倒换不会造成业务中断。]{style="font-family:宋体"}]{#struct_0_52320_18393_x1300096926}

[[执行此命令时请保持系统的稳定性，不建议在执行此命令的过程中进行任务涉及进程重启的操作。]{style="font-family:宋体"}]{#struct_0_52320_18393_x1850189838}

[[【举例】]{style="font-family:黑体"}]{#struct_0_52320_18393_x297011734}

[[\# ]{lang="EN-US"}]{#struct_0_52320_18393_x1458982745}[手工进行进程分布优化。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_52320_18393_x1359688179}

[\[Sysname\] placement reoptimize]{lang="EN-US"}

[Predicted changes to the placement]{lang="EN-US"}

[Program                           Current location       New location]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[syslog                            0/0                    0/0]{lang="EN-US"}

[l3vpn                             0/0                    0/0]{lang="EN-US"}

[aaa                               0/0                    0/0]{lang="EN-US"}

[lauth                             0/0                    0/0]{lang="EN-US"}

[lsm                               0/0                    0/0]{lang="EN-US"}

[ip6addr                           0/0                    0/0]{lang="EN-US"}

[ip6base                           0/0                    0/0]{lang="EN-US"}

[rm                                0/0                    0/0]{lang="EN-US"}

[ipcfg                             0/0                    0/0]{lang="EN-US"}

[acl                               0/0                    0/0]{lang="EN-US"}

[tunnel                            0/0                    0/0]{lang="EN-US"}

[lagg                              0/0                    0/0]{lang="EN-US"}

[qos                               0/0                    0/0]{lang="EN-US"}

[ipcim                             0/0                    0/0]{lang="EN-US"}

[ipbase                            0/0                    0/0]{lang="EN-US"}

[eth                               0/0                    0/0]{lang="EN-US"}

[ipen                              0/0                    0/0]{lang="EN-US"}

[Continue? \[y/n\]:y]{lang="EN-US"}

[Re-optimization of the placement start. You will be notified on completion]{lang="EN-US"}

[Re-optimization of the placement complete. Use \'display placement\' to view the new placement]{lang="EN-US"}
:::
