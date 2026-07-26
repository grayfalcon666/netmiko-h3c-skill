::: {#-2134805710 .myid}
[]{#_Toc404800560}[]{#struct_0_x1716_x8563_x2121719517}

**对象组 \-- 对象组Probe配置命令 \-- display system internal object-group**

------------------------------------------------------------------------

[**[display system internal object-group]{lang="EN-US"}**]{#struct_0_x1716_x8563_44197788}[命令用来显示对象组的配置和运行情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1716_x8563_123640226}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1716_x8563_x1616183861}

[**[display system internal object-group]{lang="EN-US"}**[ \[ { { **ip** \| **ipv6** } **address** \| **port** \| **service** } \[ **default** \] \[ **name** *object-group-name* \] \| **name** *object-group-name* \]]{lang="EN-US"}]{#struct_0_x1716_x8563_96605836}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1716_x8563_936288965}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal object-group]{lang="EN-US"}**[ \[ { { **ip \| ipv6** } **address \| port \| service** } \[ **default** \] \[ **name** *object-group-name* \] **\| name** *object-group-name* \] **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1716_x8563_492716578}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1716_x8563_x2038316877}[模式：]{style="font-family:宋体"}

[**[display system internal object-group]{lang="EN-US"}**[ \[ { { **ip \| ipv6** } **address \| port \| service** } \[ **default** \] \[ **name** *object-group-name* \] **\| name** *object-group-name* \] **chassis** *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1716_x8563_1718912723}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1716_x8563_1544231625}

[[Probe]{lang="EN-US"}]{#struct_0_x1716_x8563_2039068848}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1716_x8563_239775094}

[[network-admin]{lang="EN-US"}]{#struct_0_x1716_x8563_x269570809}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1716_x8563_x2122178267}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1716_x8563_1869522184}

[**[ip address]{lang="EN-US"}**]{#struct_0_x1716_x8563_108543079}[：]{style="font-family:宋体"}[指定对象组类型为]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址对象组。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**[ **address**]{lang="EN-US"}]{#struct_0_x1716_x8563_2131392245}[：]{style="font-family:宋体"}[指定对象组类型为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址对象组。]{style="font-family:宋体"}

[**[port]{lang="EN-US"}**]{#struct_0_x1716_x8563_x1722879703}[：]{style="font-family:宋体"}[指定对象组类型为]{style="font-family:宋体"}[端口对象组。]{style="font-family:宋体"}

[**[service]{lang="EN-US"}**]{#struct_0_x1716_x8563_2134442633}[：指定对象组类型为服务对象组。]{style="font-family:宋体"}

[**[default]{lang="EN-US"}**]{#struct_0_x1716_x8563_x1956580777}[：]{style="font-family:宋体"}[指定默认对象组。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}***[ object-group-name]{lang="EN-US"}*]{#struct_0_x1716_x8563_586558111}[：]{style="font-family:宋体"}[指定对象组名称。]{style="font-family:宋体"}*[object-group-name]{lang="EN-US"}*[表示对象组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1716_x8563_833271753}[：显示指定单板上对象组的配置和运行情况，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1716_x8563_x1931554611}[：显示指定成员设备上对象组的配置和运行情况，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1716_x8563_92756216}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上对象组的配置和运行情况，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1716_x8563_x968749437}[：显示指定成员设备指定单板上对象组的配置和运行情况，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1716_x8563_x757419627}[：]{style="font-family:宋体"}[显示指定单板上对象组的配置和运行情况，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[ ]{lang="EN-US"}
:::
