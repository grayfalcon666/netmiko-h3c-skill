::: {#-822294135 .myid}
[]{#_Toc404798610}[]{#struct_0_94490_16305_x230403679}[]{#_Toc350759431}

**ACL \-- ACL Probe命令 \-- display system internal acl**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **acl**]{lang="EN-US"}]{#struct_0_94490_16305_1914722099}[命令用来显示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的配置和运行情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_94490_16305_421862279}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_94490_16305_315068978}

[**[display]{lang="EN-US"}**[ **system** **internal** **acl** ]{lang="EN-US"}]{#struct_0_94490_16305_517978814}[\[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}**[ipv6]{lang="EN-US"}**[ \| **mac \| user-defined**]{lang="EN-US"}[ \] { ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[acl-number ]{lang="EN-US"}*[\| ]{lang="EN-US" style="font-size:10.0pt;
color:black"}**[name]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[acl-name ]{lang="EN-US"}*[}]{lang="EN-US" style="font-size:10.0pt;color:black"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_94490_16305_x828145714}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **acl** ]{lang="EN-US"}]{#struct_0_94490_16305_x1637768443}[\[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}**[ipv6]{lang="EN-US"}**[ \| **mac \| user-defined** ]{lang="EN-US"}[\] { ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[acl-number ]{lang="EN-US"}*[\| ]{lang="EN-US" style="font-size:10.0pt;color:black"}**[name]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[acl-name ]{lang="EN-US"}*[} { ]{lang="EN-US" style="font-size:10.0pt;color:black"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[slot-number]{lang="EN-US"}*[ }]{lang="EN-US" style="font-size:10.0pt;color:black"}

[[分布式设备－]{style="font-family:宋体"}]{#struct_0_94490_16305_709765489}[IRF]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **acl** ]{lang="EN-US"}]{#struct_0_94490_16305_155455588}[\[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}**[ipv6]{lang="EN-US"}**[ \| **mac \| user-defined**]{lang="EN-US"}[ \] { ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[acl-number ]{lang="EN-US"}*[\| ]{lang="EN-US" style="font-size:10.0pt;
color:black"}**[name]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[acl-name ]{lang="EN-US"}*[} {]{lang="EN-US" style="font-size:10.0pt;color:black"}[ **chassis** ]{lang="EN-US"}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number ]{lang="EN-US"}*[}]{lang="EN-US" style="font-size:10.0pt;color:black"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_94490_16305_x448195309}

[[Probe]{lang="EN-US"}]{#struct_0_94490_16305_x1948273926}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_94490_16305_812338170}

[[network-admin]{lang="EN-US"}]{#struct_0_94490_16305_766362213}

[[mdc-admin]{lang="EN-US"}]{#struct_0_94490_16305_532497179}

[[【参数】]{style="font-family:黑体"}]{#struct_0_94490_16305_x578736274}

[**[ipv6]{lang="EN-US"}**]{#struct_0_94490_16305_x1498443821}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[mac]{lang="EN-US"}**]{#struct_0_94490_16305_x741791740}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[user-defined]{lang="EN-US"}**]{#struct_0_94490_16305_x945256945}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。若未指定以上三种类型，则表示]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[acl-number]{lang="EN-US"}*]{#struct_0_94490_16305_x373506492}[：显示指定编号的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的配置和运行情况。]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围及其代表的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[2000]{lang="EN-US"}]{#struct_0_94490_16305_569032203}[～]{lang="EN-US" style="font-family:宋体"}[2999]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[表示基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[3000]{lang="EN-US"}]{#struct_0_94490_16305_x448129773}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[：]{style="font-family:宋体"}[表示高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[4000]{lang="EN-US"}]{#struct_0_94490_16305_x16635335}[～]{style="font-family:宋体"}[4999]{lang="EN-US"}[：]{style="font-family:宋体"}[表示二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[5000]{lang="EN-US"}]{#struct_0_94490_16305_1504870073}[～]{style="font-family:宋体"}[5999]{lang="EN-US"}[：]{style="font-family:宋体"}[表示用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}**[ *acl-name*]{lang="EN-US"}]{#struct_0_94490_16305_x498720024}[：显示指定名称的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的配置和运行情况。]{style="font-family:宋体"}*[acl-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写，必须以英文字母]{style="font-family:宋体"}[a]{lang="EN-US"}[～]{style="font-family:宋体"}[z]{lang="EN-US"}[或]{style="font-family:
宋体"}[A]{lang="EN-US"}[～]{style="font-family:宋体"}[Z]{lang="EN-US"}[开头。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_94490_16305_129115722}[：]{style="font-family:宋体"}[显示指定单板上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的配置和运行情况]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。若未指定本参数，将显示主控板上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的配置和运行情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_94490_16305_x1534341849}[：]{style="font-family:宋体"}[显示指定成员设备上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的配置和运行情况]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_94490_16305_1433336615}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的配置和运行情况]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_94490_16305_x1917338071}[：显示指定成员设备指定单板上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的配置和运行情况]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_94490_16305_455486473}[：]{style="font-family:宋体"}[显示指定单板上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的配置和运行情况]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[]{#_Toc362015036}[]{#_Toc362015037}[]{#_Toc362015038}[]{#_Toc362015039}[]{#_Toc362015040}[]{#_Toc362015041}[]{#_Toc362015042}[]{#_Toc362015043}[]{#_Toc362015044}[]{#_Toc362015045}[]{#_Toc362015046}[]{#_Toc120681090}[]{#_Toc120681091}[]{#_Toc120681098}[]{#_Toc362015083}[ ]{lang="EN-US"}
:::
