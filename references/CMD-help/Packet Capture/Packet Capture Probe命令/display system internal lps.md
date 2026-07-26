::: {#1194980479 .myid}
[]{#_Toc404800092}[]{#struct_0_34817_x8824_x1943595819}[]{#_Toc382494461}

**Packet Capture \-- Packet Capture Probe命令 \-- display system internal lps**

------------------------------------------------------------------------

[**[display system internal lps]{lang="EN-US"}**]{#struct_0_34817_x8824_x1778129113}[命令用来显示]{style="font-family:
宋体"}[LPS]{lang="EN-US"}[（]{style="font-family:宋体"}[Linux Packet Socket]{lang="EN-US"}[）信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_34817_x8824_268761747}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_34817_x8824_1998965000}

[**[display system internal lps]{lang="EN-US"}**]{#struct_0_34817_x8824_297252183}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_34817_x8824_509195275}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal lps]{lang="EN-US"}**[ \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_34817_x8824_203316585}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_34817_x8824_1981054983}[模式：]{style="font-family:宋体"}

[**[display system internal lps]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_34817_x8824_1531595222}

[[【视图】]{style="font-family:黑体"}]{#struct_0_34817_x8824_366333298}

[[Probe]{lang="EN-US"}]{#struct_0_34817_x8824_824259622}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_34817_x8824_185573754}

[[network-admin]{lang="EN-US"}]{#struct_0_34817_x8824_x1486424969}

[[mdc-admin ]{lang="EN-US"}]{#struct_0_34817_x8824_x101131121}

[[【参数】]{style="font-family:黑体"}]{#struct_0_34817_x8824_416900472}

[**[lps]{lang="EN-US"}**]{#struct_0_34817_x8824_184684851}[：]{style="font-family:宋体"}[显示]{style="font-family:宋体"}[LPS]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_34817_x8824_x652220507}[：显示指定单板的]{style="font-family:宋体"}[LPS]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板的连接信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_34817_x8824_1611264486}[：显示指定成员设备的]{style="font-family:宋体"}[LPS]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备的连接信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_34817_x8824_136253937}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[LPS]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的连接信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_34817_x8824_x1606625334}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[LPS]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[chassis-numbe]{lang="EN-US"}*[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板的连接信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_34817_x8824_x688119065}[：显示指定单板的]{style="font-family:宋体"}[LPS]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[chassis-numbe]{lang="EN-US"}*[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示所有单板的连接信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}
:::
