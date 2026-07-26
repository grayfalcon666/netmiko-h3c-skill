::: {#-1924899416 .myid}
[]{#_Toc404800494}[]{#struct_0_x3824_18462_1928185258}[]{#_Toc357517446}[]{#_Toc346023537}

**会话管理 \-- 会话管理Probe命令 \-- display fastforward session table**

------------------------------------------------------------------------

[**[display fastforward session table]{lang="EN-US"}**]{#struct_0_x3824_18462_897046005}[命令用来显示未经过安全业务处理的会话表项。目前，设备上的安全业务包括]{style="font-family:宋体"}[NAT]{lang="EN-US"}[、]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[、连接数限制、]{style="font-family:宋体"}[APR]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x3824_18462_x2033167250}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x3824_18462_x382620118}

[**[display fastforward session table]{lang="EN-US"}**[ { **ipv4** \| **ipv6** } \[ **source-ip** *source-ip* \] \[ **destination-ip** *destination-ip* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x3824_18462_x36092629}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x3824_18462_1353637204}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display fastforward session table]{lang="EN-US"}**[ { **ipv4** \| **ipv6** } \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **source-ip** *source-ip* \] \[ **destination-ip** *destination-ip* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x3824_18462_x1422461806}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x3824_18462_279475369}[模式：]{style="font-family:宋体"}

[**[display fastforward session table]{lang="EN-US"}**[ { **ipv4** \| **ipv6** } \[ ]{lang="EN-US"}]{#struct_0_x3824_18462_x313004492}**[chassis]{lang="SV"}**[ *chassis-number*]{lang="SV"}**[ slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \] \[ **source-ip** *source-ip* \] \[ **destination-ip** *destination-ip* \] \[ **verbose** \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x3824_18462_253207580}

[[Probe]{lang="EN-US"}]{#struct_0_x3824_18462_x2032483950}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x3824_18462_x701309504}

[[network-admin]{lang="EN-US"}]{#struct_0_x3824_18462_x417920365}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x3824_18462_x665267460}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x3824_18462_x2096082728}

[**[ipv4]{lang="EN-US"}**]{#struct_0_x3824_18462_1332558294}[：显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_x3824_18462_1132575065}[：显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-num*]{lang="EN-US"}]{#struct_0_x3824_18462_x236335765}[：显示指定单板上的会话表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。若不指定该参数，则显示所有单板上的会话表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-num*]{lang="EN-US"}]{#struct_0_x3824_18462_x2033232786}[：显示指定成员设备上的会话表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。若不指定该参数，则显示所有成员设备上的会话表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x3824_18462_x667151887}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的会话表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。若不指定该参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的会话表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x3824_18462_2135086024}[：显示指定成员设备的指定单板上的会话表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。若不指定该参数，则显示所有成员设备的所有单板上的会话表项。（分布式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x3824_18462_x263219885}[：]{style="font-family:宋体"}[显示指定单板上的会话表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。若不指定该参数，则显示所有单板上的会话表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x3824_18462_79602194}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的会话表项，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[source-ip]{lang="EN-US"}**[ *source-ip*]{lang="EN-US"}]{#struct_0_x3824_18462_406134630}[：显示指定源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的会话表项。其中，]{style="font-family:宋体"}*[source-ip]{lang="EN-US"}*[表示发起方到响应方会话的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[destination-ip]{lang="EN-US"}**[ *destination-ip*]{lang="EN-US"}]{#struct_0_x3824_18462_911866444}[：显示指定目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的会话表项。其中，]{style="font-family:宋体"}*[destination-ip]{lang="EN-US"}*[表示发起方到响应方会话的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x3824_18462_x791350029}[：显示详细的会话表项。不指定该参数表示显示会话表项的概要信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x3824_18462_x849730079}

[[如果除]{style="font-family:宋体"}**[ipv4]{lang="EN-US"}**]{#struct_0_x3824_18462_x653901306}[、]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[外不指定任何参数，则显示所有未经过安全业务处理的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项。]{style="font-family:宋体"}
:::
