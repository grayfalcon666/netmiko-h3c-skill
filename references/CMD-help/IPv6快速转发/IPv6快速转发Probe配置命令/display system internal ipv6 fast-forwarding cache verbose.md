::: {#2050078931 .myid}
[]{#struct_0_39310_14986_212029450}[]{#_Toc404799089}[]{#_Toc342565517}

**IPv6快速转发 \-- IPv6快速转发Probe配置命令 \-- display system internal ipv6 fast-forwarding cache verbose**

------------------------------------------------------------------------

[**[display system internal ipv6 fast-forwarding cache]{lang="EN-US"}**[ **verbose**]{lang="EN-US"}]{#struct_0_39310_14986_x1811786575}[命令用来显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快转表项的详细内容。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_39310_14986_x1282370090}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_39310_14986_882887532}

[**[display system internal ipv6 fast-forwarding cache ]{lang="EN-US"}**[\[ *ipv6-address* \] **verbose**]{lang="EN-US"}]{#struct_0_39310_14986_x873926498}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_39310_14986_1413070479}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ipv6 fast-forwarding cache ]{lang="EN-US"}**[\[ *ipv6-address* \] **verbose** \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_39310_14986_x2003630806}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_39310_14986_1509938121}[模式：]{style="font-family:宋体"}

[**[display system internal ipv6 fast-forwarding cache]{lang="EN-US"}**[ \[ *ipv6-address* \] **verbose** \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_39310_14986_369550555}

[[【视图】]{style="font-family:黑体"}]{#struct_0_39310_14986_x2071286173}

[[probe]{lang="EN-US"}]{#struct_0_39310_14986_207347177}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_39310_14986_559133806}

[[network-admin]{lang="EN-US"}]{#struct_0_39310_14986_x1050696979}

[[mdc-admin]{lang="EN-US"}]{#struct_0_39310_14986_631007073}

[[【参数】]{style="font-family:黑体"}]{#struct_0_39310_14986_1596647331}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_39310_14986_489475332}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快转表详细信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_39310_14986_x1889933764}[ *slot-number*]{lang="EN-US"}[：]{style="font-family:宋体"}[显示]{style="font-family:宋体"}[指定成员设备]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快转表详细信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示主用主控板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快转表详细信息]{style="font-family:宋体"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_39310_14986_657333364}[：显示指定成员设备的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快转表详细信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快转表详细信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_39310_14986_x668700734}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快转表详细信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快转表详细信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**]{#struct_0_39310_14986_369485019}[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快转表详细信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示全局主用主控板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快转表详细信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**]{#struct_0_39310_14986_772153699}[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：显示指定单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快转表详细信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示全局主用主控板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快转表详细信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_39310_14986_2060182621}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快转表详细信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#795911554 .myid}
[]{#struct_0_39310_14986_1350835250}[]{#_Toc404799090}[]{#_Toc342565518}[]{#_Toc361909662}[]{#_Toc361925244}[]{#_Toc361909663}[]{#_Toc361925245}[]{#_Toc361909664}[]{#_Toc361925246}[]{#_Toc361909665}[]{#_Toc361925247}[]{#_Toc361909666}[]{#_Toc361925248}[]{#_Toc361909667}[]{#_Toc361925249}[]{#_Toc361909668}[]{#_Toc361925250}[]{#_Toc361909669}[]{#_Toc361925251}[]{#_Toc361909670}[]{#_Toc361925252}[]{#_Toc361909671}[]{#_Toc361925253}[]{#_Toc361909672}[]{#_Toc361925254}[]{#_Toc361909673}[]{#_Toc361925255}[]{#_Toc361909674}[]{#_Toc361925256}[]{#_Toc361909675}[]{#_Toc361925257}[]{#_Toc361909676}[]{#_Toc361925258}[]{#_Toc361909677}[]{#_Toc361925259}[]{#_Toc361909678}[]{#_Toc361925260}[]{#_Toc361909679}[]{#_Toc361925261}[]{#_Toc361909680}[]{#_Toc361925262}[]{#_Toc361909681}[]{#_Toc361925263}[]{#_Toc361909682}[]{#_Toc361925264}[]{#_Toc361909770}[]{#_Toc361925352}

**IPv6快速转发 \-- IPv6快速转发Probe配置命令 \-- display system internal ipv6 fast-forwarding service-information**

------------------------------------------------------------------------

[**[display system internal ipv6 fast-forwarding service-information ]{lang="EN-US"}**]{#struct_0_39310_14986_x1311187707}[命令用来显示业务模块向快转模块的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[注册信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_39310_14986_243851153}

[**[display system internal ipv6 fast-forwarding service-information]{lang="EN-US"}**]{#struct_0_39310_14986_436245535}

[[【视图】]{style="font-family:黑体"}]{#struct_0_39310_14986_369288409}

[[probe]{lang="EN-US"}]{#struct_0_39310_14986_1162486055}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_39310_14986_2137001701}

[[network-admin]{lang="EN-US"}]{#struct_0_39310_14986_x65760257}

[[mdc-admin]{lang="EN-US"}]{#struct_0_39310_14986_1378683287}
:::

::: {#-1319190886 .myid}
[]{#struct_0_39310_14986_1765975963}[]{#_Toc404799091}[]{#_Toc342565519}[]{#_Toc361909772}[]{#_Toc361925354}[]{#_Toc361909773}[]{#_Toc361925355}[]{#_Toc361909774}[]{#_Toc361925356}[]{#_Toc361909775}[]{#_Toc361925357}[]{#_Toc361909776}[]{#_Toc361925358}[]{#_Toc361909777}[]{#_Toc361925359}[]{#_Toc361909778}[]{#_Toc361925360}[]{#_Toc361909779}[]{#_Toc361925361}[]{#_Toc361909795}[]{#_Toc361925377}

**IPv6快速转发 \-- IPv6快速转发Probe配置命令 \-- display system internal ipv6 max-ecmp-num**

------------------------------------------------------------------------

[**[display system internal ipv6 max-ecmp-num]{lang="EN-US"}**]{#struct_0_39310_14986_458463665}[命令用来显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[最大等价路由条数配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_39310_14986_x701739923}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_39310_14986_369616089}

[**[display system internal ipv6 max-ecmp-num]{lang="EN-US"}**[ \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_39310_14986_x2126622702}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_39310_14986_1186955441}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ipv6 max-ecmp-num]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] ]{lang="EN-US"}]{#struct_0_39310_14986_x183517866}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_39310_14986_912171678}[模式：]{style="font-family:宋体"}

[**[display system internal ipv6 max-ecmp-num]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_39310_14986_152332377}

[[【视图】]{style="font-family:黑体"}]{#struct_0_39310_14986_1665307092}

[[probe]{lang="EN-US"}]{#struct_0_39310_14986_1421378594}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_39310_14986_1221187796}

[[network-admin]{lang="EN-US"}]{#struct_0_39310_14986_369550553}

[[mdc-admin]{lang="EN-US"}]{#struct_0_39310_14986_x2071286179}

[[【参数】]{style="font-family:黑体"}]{#struct_0_39310_14986_1013916231}

[**[slot]{lang="EN-US"}**]{#struct_0_39310_14986_x1706169037}[ *slot-number*]{lang="EN-US"}[：]{style="font-family:宋体"}[显示]{style="font-family:宋体"}[指定成员设备]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[最大等价路由条数配置信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示主用主控板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[最大等价路由条数配置信息]{style="font-family:宋体"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_39310_14986_1475156837}[ *slot-number*]{lang="EN-US"}[：显示指定成员设备的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[最大等价路由条数配置信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[最大等价路由条数配置信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_39310_14986_x1784445981}[ *slot-number*]{lang="EN-US"}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[最大等价路由条数配置信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[最大等价路由条数配置信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**]{#struct_0_39310_14986_x1383731063}[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[最大等价路由条数配置信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示全局主用主控板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[最大等价路由条数配置信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**]{#struct_0_39310_14986_944437374}[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：显示指定单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[最大等价路由条数配置信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示全局主用主控板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[最大等价路由条数配置信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_39310_14986_x864555678}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[最大等价路由条数配置信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#438053557 .myid}
[]{#struct_0_39310_14986_x1716554435}[]{#_Toc404799092}[]{#_Toc342565520}[]{#_Toc361909797}[]{#_Toc361925379}[]{#_Toc361909798}[]{#_Toc361925380}[]{#_Toc361909799}[]{#_Toc361925381}[]{#_Toc361909800}[]{#_Toc361925382}[]{#_Toc361909801}[]{#_Toc361925383}[]{#_Toc361909802}[]{#_Toc361925384}[]{#_Toc361909803}[]{#_Toc361925385}[]{#_Toc361909804}[]{#_Toc361925386}[]{#_Toc361909814}[]{#_Toc361925396}

**IPv6快速转发 \-- IPv6快速转发Probe配置命令 \-- display system internal ipv6 fast-forwarding statistics**

------------------------------------------------------------------------

[**[display system internal ipv6 fast-forwarding statistics ]{lang="EN-US"}**]{#struct_0_39310_14986_x190395584}[命令用来显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快转的报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_39310_14986_x44727395}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_39310_14986_951884812}

[**[display system internal ipv6 fast-forwarding statistics ]{lang="EN-US"}**]{#struct_0_39310_14986_70109326}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_39310_14986_369878233}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ipv6 fast-forwarding statistics]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_39310_14986_764045080}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_39310_14986_1234970987}[模式：]{style="font-family:宋体"}

[**[display system internal ipv6 fast-forwarding statistics]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_39310_14986_1672418300}

[[【视图】]{style="font-family:黑体"}]{#struct_0_39310_14986_2113834922}

[[probe]{lang="EN-US"}]{#struct_0_39310_14986_55953930}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_39310_14986_322562718}

[[network-admin]{lang="EN-US"}]{#struct_0_39310_14986_x422332675}

[[mdc-admin]{lang="EN-US"}]{#struct_0_39310_14986_x71570892}

[[【参数】]{style="font-family:黑体"}]{#struct_0_39310_14986_369419478}

[**[slot]{lang="EN-US"}**]{#struct_0_39310_14986_x141548929}[ *slot-number*]{lang="EN-US"}[：]{style="font-family:宋体"}[显示]{style="font-family:宋体"}[指定成员设备]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快转的报文统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示主用主控板上的]{style="font-family:宋体"}[快转的报文统计信息]{style="font-family:宋体"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_39310_14986_239252997}[ *slot-number*]{lang="EN-US"}[：显示指定成员设备的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快转的报文统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的快转的报文统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_39310_14986_136450545}[ *slot-number*]{lang="EN-US"}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快转的报文统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的快转的报文统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**]{#struct_0_39310_14986_944714461}[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快转的报文统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示全局主用主控板上的快转的报文统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**]{#struct_0_39310_14986_311663149}[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：显示指定单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快转的报文统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示全局主用主控板上的快转的报文统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_39310_14986_x1429633396}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快转的报文统计信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#1815188409 .myid}
[]{#struct_0_39310_14986_1112560167}[]{#_Toc404799093}[]{#_Toc361909816}[]{#_Toc361925398}[]{#_Toc361909817}[]{#_Toc361925399}[]{#_Toc361909818}[]{#_Toc361925400}[]{#_Toc361909819}[]{#_Toc361925401}[]{#_Toc361909820}[]{#_Toc361925402}[]{#_Toc361909821}[]{#_Toc361925403}[]{#_Toc361909822}[]{#_Toc361925404}[]{#_Toc361909823}[]{#_Toc361925405}[]{#_Toc361909824}[]{#_Toc361925406}[]{#_Toc361909825}[]{#_Toc361925407}[]{#_Toc361909826}[]{#_Toc361925408}

**IPv6快速转发 \-- IPv6快速转发Probe配置命令 \-- reset system internal ipv6 fast-forwarding statistics**

------------------------------------------------------------------------

[**[reset system internal ipv6 fast-forwarding statistics ]{lang="EN-US"}**]{#struct_0_39310_14986_x1143667588}[命令用来清除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快转的报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_39310_14986_x851373584}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_39310_14986_x1231514529}

[**[reset system internal ipv6 fast-forwarding statistics ]{lang="EN-US"}**]{#struct_0_39310_14986_x522605759}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_39310_14986_1304929229}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset system internal ipv6 fast-forwarding statistics]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_39310_14986_369616086}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_39310_14986_x2126622715}[模式：]{style="font-family:宋体"}

[**[reset system internal ipv6 fast-forwarding statistics]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_39310_14986_427375018}

[[【视图】]{style="font-family:黑体"}]{#struct_0_39310_14986_x1527701407}

[[probe]{lang="EN-US"}]{#struct_0_39310_14986_x2054544758}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_39310_14986_1543671367}

[[network-admin]{lang="EN-US"}]{#struct_0_39310_14986_x538986456}

[[mdc-admin]{lang="EN-US"}]{#struct_0_39310_14986_x569116228}

[[【参数】]{style="font-family:黑体"}]{#struct_0_39310_14986_x132326300}

[**[slot]{lang="EN-US"}**]{#struct_0_39310_14986_2096691452}[ *slot-number*]{lang="EN-US"}[：]{style="font-family:宋体"}[清除]{style="font-family:宋体"}[指定成员设备]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快转的报文统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则清除主用主控板上的]{style="font-family:宋体"}[快转的报文统计信息]{style="font-family:宋体"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_39310_14986_369550550}[ *slot-number*]{lang="EN-US"}[：清除指定成员设备的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快转的报文统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则清除]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的快转的报文统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_39310_14986_x266833982}[ *slot-number*]{lang="EN-US"}[：清除指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快转的报文统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则清除]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的快转的报文统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**]{#struct_0_39310_14986_x2071286176}[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：清除指定成员设备上指定单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快转的报文统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则清除全局主用主控板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快转的报文统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**]{#struct_0_39310_14986_x1832917923}[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：清除指定单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快转的报文统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则清除全局主用主控板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快转的报文统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_39310_14986_1050642736}[：清除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快转的报文统计信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[ ]{lang="EN-US"}
:::
