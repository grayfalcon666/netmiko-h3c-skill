::: {#-1510030404 .myid}
[]{#_Toc404782590}[]{#struct_0_x2076_x8851_x214370052}

**软件升级 \-- 软件升级配置命令 \-- boot-loader file**

------------------------------------------------------------------------

[**[boot-loader file]{lang="EN-US"}**]{#struct_0_x2076_x8851_1145098817}[命令用来指定设备下次启动时使用的软件包]{style="font-family:宋体"}[/]{lang="EN-US" style="font-family:宋体"}[IPE]{lang="EN-US"}[文件（以下简称下次启动软件包]{style="font-family:宋体"}[/]{lang="EN-US" style="font-family:
宋体"}[IPE]{lang="EN-US"}[文件）。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x1196758867}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2076_x8851_607553286}

[**[boot-loader file boot ]{lang="EN-US"}***[boot-package ]{lang="EN-US"}***[system]{lang="EN-US"}**[ *system-package* \[ **feature** *feature-package*&\<1-30\> \] { **backup** \| **main** }]{lang="EN-US"}]{#struct_0_x2076_x8851_859242477}

[**[boot-loader file]{lang="EN-US"}***[ ipe-filename ]{lang="EN-US"}*[{ **backup** \| **main** }]{lang="EN-US"}]{#struct_0_x2076_x8851_x1221573574}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2076_x8851_x612435684}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[boot-loader file boot ]{lang="EN-US"}***[boot-package ]{lang="EN-US"}***[system]{lang="EN-US"}**[ *system-package* \[ **feature** *feature-package*&\<1-30\> \] ]{lang="EN-US"}]{#struct_0_x2076_x8851_x184995723}[{ ]{lang="EN-US"}**[all]{lang="EN-US"}**[ \| **slot** *slot-number* \[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}[ \] } { **backup** \| **main** }]{lang="EN-US"}

[**[boot-loader file]{lang="EN-US"}***[ ipe-filename ]{lang="EN-US"}*]{#struct_0_x2076_x8851_1496484948}[{ ]{lang="EN-US"}**[all]{lang="EN-US"}**[ \| **slot** *slot-number* \[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}[ \] } { **backup** \| **main** }]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_x8851_x1648547183}[模式：]{style="font-family:宋体"}

[**[boot-loader file boot ]{lang="EN-US"}***[boot-package ]{lang="EN-US"}***[system]{lang="EN-US"}**[ *system-package* \[ **feature** *feature-package*&\<1-30\> \] ]{lang="EN-US"}]{#struct_0_x2076_x8851_1649708371}[{ ]{lang="EN-US"}**[all]{lang="EN-US"}**[ \| **chassis** *chassis-number* **slot** *slot-number* \[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}[ \] } { **backup** \| **main** }]{lang="EN-US"}

[**[boot-loader file]{lang="EN-US"}***[ ipe-filename]{lang="EN-US"}***[ ]{lang="EN-US"}**]{#struct_0_x2076_x8851_x953030587}[{ ]{lang="EN-US"}**[all]{lang="EN-US"}**[ \| **chassis** *chassis-number* **slot** *slot-number* \[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}[ \] } { **backup** \| **main** }]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x36245091}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2076_x8851_607487750}

[[【缺省用户角色】]{style="font-family:
黑体"}]{#struct_0_x2076_x8851_1007505}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_x8851_162683697}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x802797144}

[**[boot ]{lang="EN-US"}***[boot-package]{lang="EN-US"}*]{#struct_0_x2076_x8851_x2118430894}[：]{style="font-family:宋体"}[Boot]{lang="EN-US"}[包的名称，]{style="font-family:宋体"}[以]{style="font-family:宋体;color:black"}[.bin]{lang="EN-US" style="color:black"}[作为后缀名]{style="font-family:宋体;
color:black"}[，从]{style="font-family:宋体"}[flash]{lang="EN-US"}[、]{style="font-family:宋体"}[cf]{lang="EN-US"}[、]{style="font-family:宋体"}[usb]{lang="EN-US"}[开始最多可输入]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符，不区分大小写。]{style="font-family:宋体"}

[**[system]{lang="EN-US"}**[ *system-package*]{lang="EN-US"}]{#struct_0_x2076_x8851_1165330677}[：]{style="font-family:宋体"}[System]{lang="EN-US"}[包的名称，]{style="font-family:宋体"}[以]{style="font-family:宋体;color:black"}[.bin]{lang="EN-US" style="color:black"}[作为后缀名]{style="font-family:宋体;
color:black"}[，从]{style="font-family:宋体"}[flash]{lang="EN-US"}[、]{style="font-family:宋体"}[cf]{lang="EN-US"}[、]{style="font-family:宋体"}[usb]{lang="EN-US"}[开始最多可输入]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符，不区分大小写。]{style="font-family:宋体"}

[**[feature]{lang="EN-US"}**[ *feature-package*]{lang="EN-US"}]{#struct_0_x2076_x8851_862409710}[：]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包的名称，]{style="font-family:宋体"}[以]{style="font-family:宋体;color:black"}[.bin]{lang="EN-US" style="color:black"}[作为后缀名]{style="font-family:宋体;
color:black"}[，从]{style="font-family:宋体"}[flash]{lang="EN-US"}[、]{style="font-family:宋体"}[cf]{lang="EN-US"}[、]{style="font-family:宋体"}[usb]{lang="EN-US"}[开始最多可输入]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符，不区分大小写。]{style="font-family:宋体"}*[feature-package]{lang="EN-US"}*[&\<1-30\>]{lang="EN-US"}[表示]{style="font-family:宋体"}[前面的参数最多可以输入]{style="font-family:宋体"}[30]{lang="EN-US"}[次。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[ipe-filename]{lang="EN-US"}*]{#struct_0_x2076_x8851_x1128933171}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[IPE]{lang="EN-US"}[（]{style="font-family:宋体"}[Image Package Envelope]{lang="EN-US"}[，复合软件包套件）文件的名称，]{style="font-family:宋体"}[以]{style="font-family:宋体;
color:black"}[.ipe]{lang="EN-US" style="color:black"}[作为后缀名]{style="font-family:宋体;color:black"}[，从]{style="font-family:宋体"}[flash]{lang="EN-US"}[、]{style="font-family:宋体"}[cf]{lang="EN-US"}[、]{style="font-family:宋体"}[usb]{lang="EN-US"}[开始最多可输入]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符，不区分大小写。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x2076_x8851_x389348356}[：用来升级整个系统。当用户获取的]{style="font-family:宋体"}[IPE]{lang="EN-US"}[包中包含]{style="font-family:宋体"}[IRF]{lang="EN-US"}[系统升级需要的所有软件包时，使用这样的]{style="font-family:宋体"}[IPE]{lang="EN-US"}[包，并指定]{style="font-family:宋体"}**[all]{lang="EN-US"}**[参数，执行一次]{style="font-family:宋体"}**[boot-loader file]{lang="EN-US"}**[命令，就能指定系统中所有硬件下次启动时使用的软件包]{style="font-family:宋体"}[/]{lang="EN-US" style="font-family:宋体"}[IPE]{lang="EN-US"}[文件。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2076_x8851_66339301}[：表示待升级的主控板所在的槽位号。（分布式设备－独立运行模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2076_x8851_x647655204}[：表示待升级的主控板所在的槽位号，或者待升级的本地有存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的虚拟槽位号。（分布式设备－独立运行模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2076_x8851_607422214}[：表示待升级的成员设备的编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2076_x8851_x647655201}[：表示待升级的成员设备的编号，或者待升级的本地有存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**]{#struct_0_x2076_x8851_1537646518}[ *cpu-number*]{lang="EN-US"}[：表示待升级的安全引擎的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数专用于升级防火墙插卡上的安全引擎，其它单板以及防火墙插卡上其它]{style="font-family:宋体"}[CPU]{lang="EN-US"}[升级时，不需要指定该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2076_x8851_x353894278}[：表示待升级的成员设备上的指定主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2076_x8851_76657598}[：表示待升级的成员设备上的指定主控板的槽位号，或者待升级的本地有存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的虚拟槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[backup]{lang="EN-US"}**]{#struct_0_x2076_x8851_x1836900194}[：指定该软件包为备用启动软件]{style="font-family:宋体"}[包，并将该软件包的名称添加到备用启动软件包列表。]{style="font-family:宋体"}[备用启动软件包用于主用启动软件包不可用或异常情况时，引导设备启动]{style="font-family:
宋体"}[。]{style="font-family:宋体"}

[**[main]{lang="EN-US"}**]{#struct_0_x2076_x8851_284183312}[：指定该软件包为主用启动软件包]{style="font-family:宋体"}[，并将该软件包的名称添加到主用启动软件包列表。]{style="font-family:宋体"}[主用启动软件包用于引导设备启动。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x602226252}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[集中式设备]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2076_x8851_843438578}

[[请先查看软件包版本发布说明书，如果软件包需要]{style="font-family:宋体"}[License]{lang="EN-US"}]{#struct_0_x2076_x8851_x1627658234}[才能运行，且设备当前没有对应的有效的]{style="font-family:宋体"}[License]{lang="EN-US"}[时，需安装对应的]{style="font-family:宋体"}[License]{lang="EN-US"}[，再执行该命令。否则：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{lang="EN-US" style="font-family:宋体"}**[boot-loader file boot ]{lang="EN-US"}***[boot-package ]{lang="EN-US"}***[system]{lang="EN-US"}**[ *system-package* \[ **feature** *feature-package*&\<1-30\> \] { **backup** \| **main** }]{lang="EN-US"}]{#struct_0_x2076_x8851_1797150861}[命令，只要指定某个的软件包当前没有有效的]{lang="EN-US" style="font-family:宋体"}[License]{lang="EN-US"}[，就会导致整条命令配置失败。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{lang="EN-US" style="font-family:宋体"}**[boot-loader file]{lang="EN-US"}***[ ipe-filename ]{lang="EN-US"}*[{ **backup** \| **main** }]{lang="EN-US"}]{#struct_0_x2076_x8851_1483495571}[命令，只有当前没有有效的]{lang="EN-US" style="font-family:宋体"}[License]{lang="EN-US"}[的软件包配置失败，其它软件包会配置成功。]{lang="EN-US" style="font-family:宋体"}

[[当配置该命令时，命令中指定的软件包]{style="font-family:宋体"}]{#struct_0_x2076_x8851_607356678}[/]{lang="EN-US" style="font-family:宋体"}[IPE]{lang="EN-US"}[文件必须放在设备存储介质主分区的根目录下，]{style="font-family:宋体"}[文件名中]{style="font-family:
宋体;color:black"}[必须包含]{style="font-family:宋体"}[存储介质的名称，形如]{style="font-family:宋体"}[flash:/xx.bin]{lang="EN-US"}[（]{style="font-family:宋体"}[flash:/xx.ipe]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[成功执行该命令后，系统会用命令中指定的软件包替换现有的软件包列表。如果命令行中没有指定]{style="font-family:宋体"}[Feature]{lang="EN-US"}]{#struct_0_x2076_x8851_x901266172}[包，则更新后的软件包列表中不会有]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包。]{style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x1815686569}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x655828497}[PEX]{lang="EN-US"}[设备，只有本地有存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备才能使用该命令来配置下次启动软件包。对于本地无存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备]{style="font-family:宋体"}[，则不能通过该命令来升级]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备]{style="font-family:宋体"}[，请使用]{style="font-family:宋体"}**[boot-loader pex file]{lang="EN-US"}**[命令]{style="font-family:宋体"}[。]{style="font-family:宋体"}[对于本地有存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备，如果同时配置了]{style="font-family:宋体"}**[boot-loader file]{lang="EN-US"}**[和]{style="font-family:宋体"}**[boot-loader pex]{lang="EN-US"}**[命令，则]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备启动时优先使用下次启动软件包。在启动过程中，如果发现下次启动软件包和父设备的版本不兼容，再使用加载软件包。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于防火墙插卡上的安全引擎，如果同时配置了]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x389741572}**[boot-loader file]{lang="EN-US"}**[和]{style="font-family:宋体"}**[boot-loader blade]{lang="EN-US"}**[命令，则安全引擎启动时优先使用下次启动软件包。在启动过程中，如果发现下次启动软件包和主用主控板的版本不兼容，再使用加载软件包。]{style="font-family:宋体"}[（分布式设备－独立运行模式）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[请先查看软件包版本发布说明书，如果软件包需要]{style="font-family:宋体"}]{#struct_0_x2076_x8851_1406668166}[License]{lang="EN-US"}[才能运行，且设备当前没有对应的有效的]{style="font-family:宋体"}[License]{lang="EN-US"}[时，需安装对应的]{style="font-family:宋体"}[License]{lang="EN-US"}[，再执行该命令。否则，当使用软件包配置该命令时，只要指定的某个软件包当前没有有效的]{style="font-family:宋体"}[License]{lang="EN-US"}[，则会导致整条命令配置失败；当使用]{style="font-family:宋体"}[IPE]{lang="EN-US"}[文件配置该命令时，只有当前没有有效的]{style="font-family:宋体"}[License]{lang="EN-US"}[的软件包配置失败，其它软件包会配置成功。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当配置该命令时，命令中指定的软件包]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x1622947718}[/]{lang="EN-US" style="font-family:宋体"}[IPE]{lang="EN-US"}[文件必须放在存储介质主分区的根目录下，]{style="font-family:宋体"}[文件名中]{style="font-family:宋体;
color:black"}[必须包含]{style="font-family:宋体"}[存储介质的名称]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[系统会自动检查指定单板上对应路径下是否存在同名文件，如果不存在，则直接]{style="font-family:宋体"}]{#struct_0_x2076_x8851_1169704224}[从指定路径拷贝一份并设置为下次启动软件包；如果存在，则提示用户是否从指定路径拷贝一份并设置为下次启动软件包]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[成功执行该命令后，系统会用命令中指定的软件包替换现有的软件包列表。如果命令行中没有指定]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x1003543079}[Feature]{lang="EN-US"}[包，则更新后的软件包列表中不会有]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x93762471}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_x1765165242}[指定设备下次启动时所用的主用启动文件为]{style="font-family:宋体"}[flash:/all.ipe]{lang="EN-US"}[。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> boot-loader file flash:/all.ipe main]{lang="EN-US"}]{#struct_0_x2076_x8851_664817774}

[Verifying the IPE file and the images\...\...\...\...Done.]{lang="EN-US"}

[Images in IPE:]{lang="EN-US"}

[  boot.bin]{lang="EN-US"}

[  system.bin]{lang="EN-US"}

[This command will set the main startup software images. Continue? \[Y/N\]:Y]{lang="EN-US"}

[Add images to the device.]{lang="EN-US"}

[File flash:/boot.bin already exists on the device.]{lang="EN-US"}

[File flash:/system.bin already exists on the device.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Decompressing file boot.bin to flash:/boot.bin\...\...\...\...\...\...\...\...Done.]{lang="EN-US"}

[Decompressing file system.bin to flash:/system.bin\...\...\...\...\...\...\...\...\...\....Done.]{lang="EN-US"}

[The images that have passed all examinations will be used as the main startup software images at the next reboot on the device..]{lang="EN-US"}[]{#struct_0_x2076_x8851_307224300}

[\# ]{lang="EN-US"}[指定设备下次启动时所用的主用启动文件为]{style="font-family:宋体"}[flash:/boot.bin]{lang="EN-US"}[和]{style="font-family:宋体"}[flash:/system.bin]{lang="EN-US"}[。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> boot-loader file boot flash:/boot.bin system flash:/system.bin main]{lang="EN-US"}]{#struct_0_x2076_x8851_664883310}

[This command will set the main startup software images. Continue? \[Y/N\]:y]{lang="EN-US"}

[The images that have passed all examinations will be used as the main startup]{lang="EN-US"}

[software images at the next reboot on the device.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_x523783491}[指定]{style="font-family:宋体"}[0]{lang="EN-US"}[号板下次启动时所用的主用启动文件为]{style="font-family:宋体"}[flash:/all.ipe]{lang="EN-US"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> boot-loader file flash:/all.ipe slot 0 main]{lang="EN-US"}]{#struct_0_x2076_x8851_665473134}

[Verifying the IPE file and the images\...\...\...\...Done.]{lang="EN-US"}

[Images in IPE:]{lang="EN-US"}

[  boot.bin]{lang="EN-US"}

[  system.bin]{lang="EN-US"}

[This command will set the main startup software images. Continue? \[Y/N\]:Y]{lang="EN-US"}

[Add images to target slot.]{lang="EN-US"}

[File flash:/boot.bin already exists on slot 0.]{lang="EN-US"}

[File flash:/system.bin already exists on slot 0.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Decompressing file boot.bin to flash:/boot.bin\...\...\...\...\...\...\...\...Done.]{lang="EN-US"}

[Decompressing file system.bin to flash:/system.bin\...\...\...\...\...\...\...\...\...\....Done.]{lang="EN-US"}

[The images that have passed all examinations will be used as the main startup software images at the next reboot on slot 0.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_665538670}[指定成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[下次启动时所用的主用启动文件为]{style="font-family:宋体"}[flash:/all.ipe]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> boot-loader file flash:/all.ipe slot 1 main]{lang="EN-US"}]{#struct_0_x2076_x8851_679693126}

[Verifying the IPE file and the images\...\...\...\...Done.]{lang="EN-US"}

[Images in IPE:]{lang="EN-US"}

[  boot.bin]{lang="EN-US"}

[  system.bin]{lang="EN-US"}

[This command will set the main startup software images. Continue? \[Y/N\]:Y]{lang="EN-US"}

[Add images to target slot.]{lang="EN-US"}

[File flash:/boot.bin already exists on slot 1.]{lang="EN-US"}

[File flash:/system.bin already exists on slot 1.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Decompressing file boot.bin to flash:/boot.bin\...\...\...\...\...\...\...\...Done.]{lang="EN-US"}

[Decompressing file system.bin to flash:/system.bin\...\...\...\...\...\...\...\...\...\....Done.]{lang="EN-US"}

[The images that have passed all examinations will be used as the main startup software images at the next reboot on slot 1.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_664948845}[指定成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[0]{lang="EN-US"}[号单板下次启动时所用的主用启动文件为]{style="font-family:
宋体"}[flash:/all.ipe]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> boot-loader file flash:/all.ipe chassis 1 slot 0 main]{lang="EN-US"}]{#struct_0_x2076_x8851_665014381}

[Verifying the IPE file and the images\...\...\...\...Done.]{lang="EN-US"}

[Images in IPE:]{lang="EN-US"}

[  boot.bin]{lang="EN-US"}

[  system.bin]{lang="EN-US"}

[This command will set the main startup software images. Continue? \[Y/N\]:Y]{lang="EN-US"}

[Add images to target slot.]{lang="EN-US"}

[File flash:/boot.bin already exists on chassis 1 slot 0.]{lang="EN-US"}

[File flash:/system.bin already exists on chassis 1 slot 0.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Decompressing file boot.bin to flash:/boot.bin\...\...\...\...\...\...\...\...Done.]{lang="EN-US"}

[Decompressing file system.bin to flash:/system.bin\...\...\...\...\...\...\...\...\...\....Done.]{lang="EN-US"}

[The images that have passed all examinations will be used as the main startup software images at the next reboot on chassis 1 slot 0.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x1716500330}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[boot-loader blade]{lang="EN-US"}**]{#struct_0_x2076_x8851_x389413889}**[ file]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[boot-loader pex]{lang="EN-US"}**]{#struct_0_x2076_x8851_x1029992234}**[ file]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display boot-loader]{lang="EN-US"}**]{#struct_0_x2076_x8851_1902171023}
:::

::::: {#-545330068 .myid}
[]{#_Toc404782591}[]{#struct_0_x2076_x8851_x1658728361}[]{#_Toc368057762}

**软件升级 \-- 软件升级配置命令 \-- boot-loader blade file**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](软件升级命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_x8851_x24787866}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x2076_x8851_x389741569}
:::

**[ ]{lang="EN-US"}**

[**[boot-loader blade file]{lang="EN-US"}**]{#struct_0_x2076_x8851_x819545690}[命令用来配置安全引擎的加载软件包]{style="font-family:宋体"}[/]{lang="EN-US" style="font-family:宋体"}[IPE]{lang="EN-US"}[文件。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x1647759272}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2076_x8851_x389807105}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[**[boot-loader blade ]{lang="EN-US"}***[blade-model]{lang="EN-US"}***[ file boot ]{lang="EN-US"}***[boot-package ]{lang="EN-US"}***[system]{lang="EN-US"}**[ *system-package* \[ **feature** *feature-package*&\<1-30\> \]]{lang="EN-US"}]{#struct_0_x2076_x8851_1100063551}

[**[boot-loader blade ]{lang="EN-US"}***[blade-model]{lang="EN-US"}***[ file ipe ]{lang="EN-US"}***[ipe-filename]{lang="EN-US"}*]{#struct_0_x2076_x8851_x1914392750}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_618248008}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x389610497}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x1224784589}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_x8851_x255011919}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x389676033}

[**[blade ]{lang="EN-US"}***[blade-model]{lang="EN-US"}*]{#struct_0_x2076_x8851_707538527}[：设备支持的]{style="font-family:宋体"}[安全引擎的型号，该参数必须完整输入，不区分大小写。]{style="font-family:宋体"}[可输入]{style="font-family:宋体"}**[boot-loader blade ]{lang="EN-US"}[？]{style="font-family:宋体"}**[，来获取该参数的取值]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[boot ]{lang="EN-US"}***[boot-package]{lang="EN-US"}*]{#struct_0_x2076_x8851_1189705972}[：]{style="font-family:宋体"}[安全引擎加载的]{style="font-family:宋体"}[Boot]{lang="EN-US"}[包的名称，]{style="font-family:宋体"}[以]{style="font-family:宋体;color:black"}[.bin]{lang="EN-US" style="color:black"}[作为后缀名]{style="font-family:宋体;color:black"}[，从]{style="font-family:宋体"}[flash]{lang="EN-US"}[、]{style="font-family:宋体"}[cf]{lang="EN-US"}[、]{style="font-family:宋体"}[usb]{lang="EN-US"}[开始最多可输入]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符，不区分大小写。]{style="font-family:宋体"}

[**[system]{lang="EN-US"}**[ *system-package*]{lang="EN-US"}]{#struct_0_x2076_x8851_x360464865}[：]{style="font-family:宋体"}[安全引擎加载的]{style="font-family:宋体"}[System]{lang="EN-US"}[包的名称，]{style="font-family:宋体"}[以]{style="font-family:宋体;color:black"}[.bin]{lang="EN-US" style="color:black"}[作为后缀名]{style="font-family:宋体;color:black"}[，从]{style="font-family:宋体"}[flash]{lang="EN-US"}[、]{style="font-family:宋体"}[cf]{lang="EN-US"}[、]{style="font-family:宋体"}[usb]{lang="EN-US"}[开始最多可输入]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符，不区分大小写。]{style="font-family:宋体"}

[**[feature]{lang="EN-US"}**[ *feature-package*]{lang="EN-US"}]{#struct_0_x2076_x8851_x390003713}[：]{style="font-family:宋体"}[安全引擎加载的]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包的名称，]{style="font-family:宋体"}[以]{style="font-family:宋体;color:black"}[.bin]{lang="EN-US" style="color:black"}[作为后缀名]{style="font-family:宋体;color:black"}[，从]{style="font-family:宋体"}[flash]{lang="EN-US"}[、]{style="font-family:宋体"}[cf]{lang="EN-US"}[、]{style="font-family:宋体"}[usb]{lang="EN-US"}[开始最多可输入]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符，不区分大小写。]{style="font-family:宋体"}[{ *feature-package* }&\<1-30\>]{lang="EN-US"}[表示]{style="font-family:宋体"}[前面的参数最多可以输入]{style="font-family:宋体"}[30]{lang="EN-US"}[次。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ipe ]{lang="EN-US"}***[ipe-filename]{lang="EN-US"}*]{#struct_0_x2076_x8851_260360047}[：]{style="font-family:宋体"}[表示加载的]{style="font-family:宋体"}[IPE]{lang="EN-US"}[（]{style="font-family:宋体"}[Image Package Envelope]{lang="EN-US"}[，复合软件包套件）文件名，]{style="font-family:宋体"}[以]{style="font-family:宋体;color:black"}[.ipe]{lang="EN-US" style="color:black"}[作为后缀名]{style="font-family:宋体;color:black"}[，从]{style="font-family:宋体"}[flash]{lang="EN-US"}[、]{style="font-family:宋体"}[cf]{lang="EN-US"}[、]{style="font-family:宋体"}[usb]{lang="EN-US"}[开始最多可输入]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x503378998}

[[请在设备启动完成、稳定运行后再配置该命令。如果配置该命令后，加入新的主控板，需要重新配置该命令，以免新加入的主控板上没有加载软件包，影响安全引擎启动。]{style="font-family:宋体"}]{#struct_0_x2076_x8851_800364015}

[[配置该命令后，系统会将指定软件包备份到所有主控板。安全引擎只使用当前主用主控板上的软件包作为加载软件包。（分布式设备－独立运行模式）]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x1844101834}

[[成功执行该命令后，系统会用命令中指定的软件包替换命令行中指定型号的安全引擎现有的加载软件包列表。如果命令行中没有指定]{style="font-family:宋体"}[Feature]{lang="EN-US"}]{#struct_0_x2076_x8851_x389479426}[包，则更新后的加载软件包列表中不会有]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包。]{style="font-family:宋体"}

[[当配置该命令时，命令中指定的软件包]{style="font-family:宋体"}]{#struct_0_x2076_x8851_1153045679}[/]{lang="EN-US" style="font-family:宋体"}[IPE]{lang="EN-US"}[文件必须放在存储介质主分区的根目录下，文件名中必须包含存储介质的名称。]{style="font-family:宋体"}

[[关于加载软件包的详细介绍以及下次启动软件包]{style="font-family:宋体"}[/IPE]{lang="EN-US"}]{#struct_0_x2076_x8851_650632719}[文件和加载软件包]{style="font-family:宋体"}[/IPE]{lang="EN-US"}[文件的关系，请参见"基础配置指导"中的"软件升级"。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x389544962}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_1812540495}[指定型号为]{style="font-family:宋体"}[Blade-m9k]{lang="EN-US"}[的安全引擎向主控板加载时所用的加载文件为]{style="font-family:宋体"}[slot2.1#flash:/m9000_fw.ipe]{lang="EN-US"}[。（分布式设备---独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> boot-loader blade Blade-m9k file ipe slot2.1#cfa0:/m9000_fw.ipe]{lang="EN-US"}]{#struct_0_x2076_x8851_x1795720048}

[Verifying the IPE file and the images\...\...\...\...\...\...\...\...\....Done.]{lang="EN-US"}

[File flash:/blade3fwm9k-cmw710-boot-a0002.bin already exists on slot 5.]{lang="EN-US"}

[File flash:/blade3fwm9k-cmw710-system-a0002.bin already exists on slot 5.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Decompressing file blade3fwm9k-cmw710-boot-a0002.bin to flash:/blade3fwm9k-cmw710-boot-a0002.bin\...\...\...\...\...\.....Done.]{lang="EN-US"}

[Decompressing file blade3fwm9k-cmw710-system-a0002.bin to flash:/blade3fwm9k-cmw710-system-a0002.bin\...\...\...\...\...\...\...\...\...\...Done.]{lang="EN-US"}

[File flash:/blade3fwm9k-cmw710-boot-a0002.bin already exists on slot 4.]{lang="EN-US"}

[File flash:/blade3fwm9k-cmw710-system-a0002.bin already exists on slot 4.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Copying file flash:/blade3fwm9k-cmw710-boot-a0002.bin to slot4#flash:/blade3fwm9k-cmw710-boot-a0002.bin\...\...\...\...\...\...\...\...\...\...\....Done.]{lang="EN-US"}

[Copying file flash:/blade3fwm9k-cmw710-system-a0002.bin to slot4#flash:/blade3fwm9k-cmw710-system-a0002.bin\...\...\...\...\...\...\...\...\...\.....Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_x390003714}[指定型号为]{style="font-family:宋体"}[Blade-m9k]{lang="EN-US"}[的安全引擎向主控板加载时所用的文件为]{style="font-family:宋体"}[slot2.1#flash:/blade3fwm9k-cmw710-boot-a0002.bin]{lang="EN-US"}[和]{style="font-family:宋体"}[slot2.1#flash:/blade3fwm9k-cmw710-system-a0002.bin]{lang="EN-US"}[。（分布式设备---独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> boot-loader blade Blade-m9k file boot slot2.1#cfa0:/blade3fwm9k-cmw710-boot-a0002.bin system slot2.1#cfa0:/blade3fwm9k-cmw710-system-a0002.bin]{lang="EN-US"}]{#struct_0_x2076_x8851_x1795588976}

[File flash:/blade3fwm9k-cmw710-boot-a0002.bin already exists on slot 4.]{lang="EN-US"}

[File flash:/blade3fwm9k-cmw710-system-a0002.bin already exists on slot 4.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:]{lang="EN-US"}

[File flash:/blade3fwm9k-cmw710-boot-a0002.bin already exists on slot 5.]{lang="EN-US"}

[File flash:/blade3fwm9k-cmw710-system-a0002.bin already exists on slot 5.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:]{lang="EN-US"}

[\<maintest\>boot-loader blade Blade-m9k file boot slot2.1#cfa0:/blade3fwm9k-cmw710-boot-a0002.bin system slot2.1#cfa0:/blade3fwm9k-cmw710-system-a0002.bin]{lang="EN-US"}

[File flash:/blade3fwm9k-cmw710-boot-a0002.bin already exists on chassis 1 slot 4.]{lang="EN-US"}

[File flash:/blade3fwm9k-cmw710-system-a0002.bin already exists on chassis 1 slot 4.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Copying file cfa0:/blade3fwm9k-cmw710-boot-a0002.bin to slot4#flash:/blade3fwm9k-cmw710-boot-a0002.bin\...\...\...\...\...\...Done.]{lang="EN-US"}

[Copying file cfa0:/blade3fwm9k-cmw710-system-a0002.bin to slot4#flash:/blade3fwm9k-cmw710-system-a0002.bin\...\...\...\...\...\...\...\....Done.]{lang="EN-US"}

[File flash:/blade3fwm9k-cmw710-boot-a0002.bin already exists on slot 5.]{lang="EN-US"}

[File flash:/blade3fwm9k-cmw710-system-a0002.bin already exists on slot 5.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Copying file cfa0:/blade3fwm9k-cmw710-boot-a0002.bin to flash:/blade3fwm9k-cmw710-boot-a0002.bin\...\...\...\...\.....Done.]{lang="EN-US"}

[Copying file cfa0:/blade3fwm9k-cmw710-system-a0002.bin to flash:/blade3fwm9k-cmw710-system-a0002.bin\...\...\...\...\...\...\...\...\....Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_x819152474}[指定型号为]{style="font-family:宋体"}[Blade-m9k]{lang="EN-US"}[的安全引擎向主控板加载时所用的文件为]{style="font-family:宋体"}[flash:/m9000_fw.ipe]{lang="EN-US"}[。（分布式设备---]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> boot-loader blade Blade-m9k file ipe flash:/m9000_fw.ipe]{lang="EN-US"}]{#struct_0_x2076_x8851_x1796113263}

[Verifying the IPE file and the images\...\...\...\...\...\....Done.]{lang="EN-US"}

[File flash:/blade3fwm9k-cmw710-boot-a0002.bin already exists on chassis 1 slot 5.]{lang="EN-US"}

[File flash:/blade3fwm9k-cmw710-system-a0002.bin already exists on chassis 1 slot 5.]{lang="EN-US"}

[File flash:/blade3fwm9k-cmw710-devkit-a0002.bin already exists on chassis 1 slot 5.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:N]{lang="EN-US"}

[File flash:/blade3fwm9k-cmw710-boot-a0002.bin already exists on chassis 1 slot 4.]{lang="EN-US"}

[File flash:/blade3fwm9k-cmw710-system-a0002.bin already exists on chassis 1 slot 4.]{lang="EN-US"}

[File flash:/blade3fwm9k-cmw710-devkit-a0002.bin already exists on chassis 1 slot 4.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Copying file flash:/blade3fwm9k-cmw710-boot-a0002.bin to chassis1#slot4#flash:/blade3fwm9k-cmw710-boot-a0002.bin\...\...\...\...\...\...\...\...\....Done.]{lang="EN-US"}

[Copying file flash:/blade3fwm9k-cmw710-system-a0002.bin to chassis1#slot4#flash:/blade3fwm9k-cmw710-system-a0002.bin\...\...\...\...\...\.....Done.]{lang="EN-US"}

[Copying file flash:/blade3fwm9k-cmw710-devkit-a0002.bin to chassis1#slot4#flash:/blade3fwm9k-cmw710-devkit-a0002.bin\...\...\...\...\...\....Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_x390069247}[指定型号为]{style="font-family:宋体"}[Blade-m9k]{lang="EN-US"}[的安全引擎向主控板加载时所用的文件为]{style="font-family:宋体"}[flash:/ blade3fwm9k-cmw710-boot-a0002.bin]{lang="EN-US"}[和]{style="font-family:宋体"}[flash:/ blade3fwm9k-cmw710-system-a0002.bin]{lang="EN-US"}[。（分布式设备---]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> boot-loader blade Blade-m9k file boot flash:/blade3fwm9k-cmw710-boot-a0002.bin system flash:/blade3fwm9k-cmw710-system-a0002.bin]{lang="EN-US"}]{#struct_0_x2076_x8851_x1795982191}

[File flash:/blade3fwm9k-cmw710-boot-a0002.bin already exists on chassis 1 slot 4.]{lang="EN-US"}

[File flash:/blade3fwm9k-cmw710-system-a0002.bin already exists on chassis 1 slot 4.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Copying file flash:/blade3fwm9k-cmw710-boot-a0002.bin to chassis1#slot4#flash:/blade3fwm9k-cmw710-boot-a0002.bin\...\...\...\...\...\...\...\...Done.]{lang="EN-US"}

[Copying file flash:/blade3fwm9k-cmw710-system-a0002.bin to chassis1#slot4#flash:/blade3fwm9k-cmw710-system-a0002.bin\...\...\...\...\...\...\....Done.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_1071650617}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display boot-loader ]{lang="EN-US"}**]{#struct_0_x2076_x8851_302986436}**[blade]{lang="EN-US"}**
:::::

::::: {#2112542094 .myid}
[]{#_Toc404782592}[]{#struct_0_x2076_x8851_x1029992231}[]{#_Toc360431289}

**软件升级 \-- 软件升级配置命令 \-- boot-loader pex file**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](软件升级命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_x8851_x412253660}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x2076_x8851_768373796}
:::

**[ ]{lang="EN-US"}**

[**[boot-loader pex file]{lang="EN-US"}**]{#struct_0_x2076_x8851_x1029992232}[命令用来配置]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的加载软件包]{style="font-family:宋体"}[/]{lang="EN-US" style="font-family:宋体"}[IPE]{lang="EN-US"}[文件。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x8969133}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2076_x8851_x1029992229}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[**[boot-loader pex ]{lang="EN-US"}***[pex-model]{lang="EN-US"}***[ file boot ]{lang="EN-US"}***[boot-package ]{lang="EN-US"}***[system]{lang="EN-US"}**[ *system-package* \[ **feature** *feature-package*&\<1-30\> \]]{lang="EN-US"}]{#struct_0_x2076_x8851_x768418484}

[**[boot-loader pex ]{lang="EN-US"}***[pex-model]{lang="EN-US"}***[ file]{lang="EN-US"}***[ ]{lang="EN-US"}***[ipe ]{lang="EN-US"}***[ipe-filename]{lang="EN-US"}*]{#struct_0_x2076_x8851_x1756005261}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x1029992227}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2076_x8851_394380930}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_594629471}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_x8851_x1029992228}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_797665457}

[**[pex ]{lang="EN-US"}***[pex-model]{lang="EN-US"}*]{#struct_0_x2076_x8851_x1029992225}[：设备支持的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的型号，该参数必须完整输入，不区分大小写。]{style="font-family:宋体"}[可输入]{style="font-family:
宋体"}**[boot-loader pex ]{lang="EN-US"}[？]{style="font-family:宋体"}**[，回车，来获取该参数的取值]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[boot ]{lang="EN-US"}***[boot-package]{lang="EN-US"}*]{#struct_0_x2076_x8851_1557180344}[：]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备将加载的]{style="font-family:宋体"}[Boot]{lang="EN-US"}[包的名称，]{style="font-family:宋体"}[以]{style="font-family:宋体;color:black"}[.bin]{lang="EN-US" style="color:black"}[作为后缀名]{style="font-family:宋体;
color:black"}[，从]{style="font-family:宋体"}[flash]{lang="EN-US"}[、]{style="font-family:宋体"}[cf]{lang="EN-US"}[、]{style="font-family:宋体"}[usb]{lang="EN-US"}[开始最多可输入]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符，不区分大小写。]{style="font-family:宋体"}

[**[system]{lang="EN-US"}**[ *system-package*]{lang="EN-US"}]{#struct_0_x2076_x8851_x1458887435}[：]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备将加载的]{style="font-family:宋体"}[System]{lang="EN-US"}[包的名称，]{style="font-family:宋体"}[以]{style="font-family:宋体;color:black"}[.bin]{lang="EN-US" style="color:black"}[作为后缀名]{style="font-family:宋体;
color:black"}[，从]{style="font-family:宋体"}[flash]{lang="EN-US"}[、]{style="font-family:宋体"}[cf]{lang="EN-US"}[、]{style="font-family:宋体"}[usb]{lang="EN-US"}[开始最多可输入]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符，不区分大小写。]{style="font-family:宋体"}

[**[feature]{lang="EN-US"}**[ *feature-package*]{lang="EN-US"}]{#struct_0_x2076_x8851_x1029992226}[：]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备将加载的]{style="font-family:宋体"}[feature]{lang="EN-US"}[包的名称，]{style="font-family:宋体"}[以]{style="font-family:宋体;color:black"}[.bin]{lang="EN-US" style="color:black"}[作为后缀名]{style="font-family:宋体;
color:black"}[，从]{style="font-family:宋体"}[flash]{lang="EN-US"}[、]{style="font-family:宋体"}[cf]{lang="EN-US"}[、]{style="font-family:宋体"}[usb]{lang="EN-US"}[开始最多可输入]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符，不区分大小写。]{style="font-family:宋体"}*[feature-package]{lang="EN-US"}*[&\<1-30\>]{lang="EN-US"}[表示]{style="font-family:宋体"}[前面的参数最多可以输入]{style="font-family:宋体"}[30]{lang="EN-US"}[次。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ipe ]{lang="EN-US"}***[ipe-filename]{lang="EN-US"}*]{#struct_0_x2076_x8851_1960464871}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备将加载的]{style="font-family:宋体"}[IPE]{lang="EN-US"}[（]{style="font-family:宋体"}[Image Package Envelope]{lang="EN-US"}[，复合软件包套件）文件的名称，]{style="font-family:宋体"}[以]{style="font-family:宋体;color:black"}[.ipe]{lang="EN-US" style="color:black"}[作为后缀名]{style="font-family:宋体;color:black"}[，从]{style="font-family:宋体"}[flash]{lang="EN-US"}[、]{style="font-family:宋体"}[cf]{lang="EN-US"}[、]{style="font-family:宋体"}[usb]{lang="EN-US"}[开始最多可输入]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x585458680}

[[如果配置该命令后，加入新的主控板，需要重新配置该命令，以免主备倒换后，影响]{style="font-family:宋体"}[PEX]{lang="EN-US"}]{#struct_0_x2076_x8851_665538669}[设备启动。]{style="font-family:宋体"}

[[配置该命令后，系统会将指定软件包备份到所有主控板。]{style="font-family:宋体"}[PEX]{lang="EN-US"}]{#struct_0_x2076_x8851_664948844}[设备只使用当前主用主控板上的软件包作为加载软件包。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[成功执行该命令后，系统会用命令中指定的软件包替换命令行中指定型号的]{style="font-family:宋体"}[PEX]{lang="EN-US"}]{#struct_0_x2076_x8851_218221120}[设备现有的加载软件包列表。如果命令行中没有指定]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包，则更新后的加载软件包列表中不会有]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包。]{style="font-family:宋体"}

[[关于该命令请注意，当配置该命令时，命令中指定的软件包]{style="font-family:宋体"}]{#struct_0_x2076_x8851_877715274}[（]{style="font-family:宋体"}[IPE]{lang="EN-US"}[文件）必须放在存储介质主分区的根目录下，文件名中必须包含存储介质的名称。]{style="font-family:宋体"}

[[关于加载软件包的详细介绍以及下次启动软件包]{style="font-family:宋体"}]{#struct_0_x2076_x8851_1706135766}[/]{lang="EN-US" style="font-family:宋体"}[IPE]{lang="EN-US"}[文件和加载软件包]{style="font-family:宋体"}[/]{lang="EN-US" style="font-family:宋体"}[IPE]{lang="EN-US"}[文件的关系，请参见"基础配置指导"中的"软件升级"。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_1706135773}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_665014379}[将型号为]{style="font-family:宋体"}[PEX-S5120HI]{lang="EN-US"}[的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的加载软件包配置为]{style="font-family:宋体"}[flash:/all.ipe]{lang="EN-US"}[。（分布式设备---独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> boot-loader pex PEX-S5120HI file ipe flash:/all.ipe]{lang="EN-US"}]{#struct_0_x2076_x8851_665079915}

[Verifying the IPE file and the images\...\...\...\...Done.]{lang="EN-US"}

[File flash:/rpu-s5120hi-boot.bin already exists on slot 0.]{lang="EN-US"}

[File flash:/rpu-s5120hi-system.bin already exists on slot 0.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Decompressing file rpu-s5120hi-boot.bin to flash:/rpu-s5120hi-boot.bin\...\...\...\...\...\...\...Done.]{lang="EN-US"}

[Decompressing file rpu-s5120hi-system.bin to flash:/rpu-s5120hi-system.bin\...\...\...\...\...\...\...\...\...\...\...\... Done.]{lang="EN-US"}

[File flash:/rpu-s5120hi-boot.bin already exists on slot 1.]{lang="EN-US"}

[File flash:/rpu-s5120hi-system.bin already exists on slot 1.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Copying file flash:/rpu-s5120hi-boot.bin to slot1#flash:/rpu-s5120hi-boot.bin\...\...\...\...\...\...\...\....Done.]{lang="EN-US"}

[Copying file flash:/rpu-s5120hi-system.bin to slot1#flash:/rpu-s5120hi-system.bin\...\...\...\...\...\...\...\...\...\...\...\...\...\.....Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_665145451}[将型号为]{style="font-family:宋体"}[PEX-S5120HI]{lang="EN-US"}[的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的加载软件包配置为]{style="font-family:宋体"}[flash:/boot.bin]{lang="EN-US"}[和]{style="font-family:宋体"}[flash:/system.bin]{lang="EN-US"}[。（分布式设备---独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> boot-loader pex PEX-S5120HI file boot flash:/boot.bin system flash:/system.bin]{lang="EN-US"}]{#struct_0_x2076_x8851_664686699}

[File flash:/boot.bin already exists on slot 1.]{lang="EN-US"}

[File flash:/system.bin already exists on slot 1.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:y]{lang="EN-US"}

[Copying file flash:/boot.bin to slot1#flash:/boot.bin\...\...\...\...\...\...\...\....Done.]{lang="EN-US"}

[Copying file flash:/system.bin to slot1#flash:/system.bin\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_664752235}[将型号为]{style="font-family:宋体"}[PEX-S5120HI]{lang="EN-US"}[的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的加载软件包配置为]{style="font-family:宋体"}[flash:/all.ipe]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> boot-loader pex PEX-S5120HI file ipe flash:/all.ipe]{lang="EN-US"}]{#struct_0_x2076_x8851_664817771}

[Verifying the IPE file and the images\...\...\...\...Done.]{lang="EN-US"}

[File flash:/rpu-s5120hi-boot.bin already exists on slot 1.]{lang="EN-US"}

[File flash:/rpu-s5120hi-system.bin already exists on slot 1.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Decompressing file rpu-s5120hi-boot.bin to flash:/rpu-s5120hi-boot.bin\...\...\...\...\...\...\...Done.]{lang="EN-US"}

[Decompressing file rpu-s5120hi-system.bin to flash:/rpu-s5120hi-system.bin\...\...\...\...\...\...\...\...\...\...\...\...\...\..... Done.]{lang="EN-US"}

[File flash:/rpu-s5120hi-boot.bin already exists on slot 2.]{lang="EN-US"}

[File flash:/rpu-s5120hi-system.bin already exists on slot 2.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Copying file flash:/rpu-s5120hi-boot.bin to slot2#flash:/rpu-s5120hi-boot.bin\...\...\...\...\...\...\...\....Done.]{lang="EN-US"}

[Copying file flash:/rpu-s5120hi-system.bin to slot2#flash:/rpu-s5120hi-system.bin\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_664883307}[将型号为]{style="font-family:宋体"}[PEX-S5120HI]{lang="EN-US"}[的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的加载软件包配置为]{style="font-family:宋体"}[flash:/boot.bin]{lang="EN-US"}[和]{style="font-family:宋体"}[flash:/system.bin]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> boot-loader pex PEX-S5120HI file boot flash:/boot.bin system flash:/system.bin]{lang="EN-US"}]{#struct_0_x2076_x8851_665473131}

[File flash:/boot.bin already exists on slot 2.]{lang="EN-US"}

[File flash:/system.bin already exists on slot 2.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Copying file flash:/boot.bin to slot2#flash:/boot.bin\...\...\...\...\...\...\...\....Done.]{lang="EN-US"}

[Copying file flash:/system.bin to slot2#flash:/system.bin\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_665538667}[将型号为]{style="font-family:宋体"}[PEX-S5120HI]{lang="EN-US"}[的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的加载软件包配置为]{style="font-family:宋体"}[flash:/all.ipe]{lang="EN-US"}[。（分布式设备---]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> boot-loader pex PEX-S5120HI file ipe flash:/all.ipe]{lang="EN-US"}]{#struct_0_x2076_x8851_664948842}

[Verifying the IPE file and the images\...\...\...\...Done.]{lang="EN-US"}

[File flash:/rpu-s5120hi-boot.bin already exists on chassis 1 slot 1.]{lang="EN-US"}

[File flash:/rpu-s5120hi-system.bin already exists on chassis 1 slot 1.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Decompressing file rpu-s5120hi-boot.bin to flash:/rpu-s5120hi-boot.bin\...\...\...\...\...\...\...Done.]{lang="EN-US"}

[Decompressing file rpu-s5120hi-system.bin to flash:/rpu-s5120hi-system.bin\...\...\...\...\...\...\...\...\...\...\...\...\...\..... Done.]{lang="EN-US"}

[File flash:/rpu-s5120hi-boot.bin already exists on chassis 1 slot 2.]{lang="EN-US"}

[File flash:/rpu-s5120hi-system.bin already exists on chassis 1 slot 2.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Copying file flash:/rpu-s5120hi-boot.bin to chassis1#slot2#flash:/rpu-s5120hi-boot.bin\...\...\...\...\...\...\...\....Done.]{lang="EN-US"}

[Copying file flash:/rpu-s5120hi-system.bin to chassis1#slot2#flash:/rpu-s5120hi-system.bin\...\...\...\...\...\...\...\...\...\...\...\...\...Done.]{lang="EN-US"}

[File flash:/rpu-s5120hi-boot.bin already exists on chassis 2 slot 2.]{lang="EN-US"}

[File flash:/rpu-s5120hi-system.bin already exists on chassis 2 slot 2.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Copying file flash:/rpu-s5120hi-boot.bin to chassis2#slot2#flash:/rpu-s5120hi-boot.bin\...\...\...\...\...\...\...\....Done.]{lang="EN-US"}

[Copying file flash:/rpu-s5120hi-system.bin to chassis2#slot2#flash:/rpu-s5120hi-system.bin\...\...\...\...\...\...\...\...\...\...\...\...Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_665014378}[将型号为]{style="font-family:宋体"}[PEX-S5120HI]{lang="EN-US"}[的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的加载软件包配置为]{style="font-family:宋体"}[flash:/boot.bin]{lang="EN-US"}[和]{style="font-family:宋体"}[flash:/system.bin]{lang="EN-US"}[。（分布式设备---]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> boot-loader pex PEX-S5120HI file boot flash:/boot.bin system flash:/system.bin]{lang="EN-US"}]{#struct_0_x2076_x8851_665145450}

[File flash:/boot.bin already exists on chassis 1 slot 2.]{lang="EN-US"}

[File flash:/system.bin already exists on chassis 1 slot 2.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Copying file flash:/boot.bin to chassis1#slot2#flash:/boot.bin\...\...\...\...\...\...\...\....Done.]{lang="EN-US"}

[Copying file flash:/system.bin to chassis1#slot2#flash:/system.bin\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...Done.]{lang="EN-US"}

[File flash:/boot.bin already exists chassis 2 slot 2.]{lang="EN-US"}

[File flash:/system.bin already exists chassis 2 slot 2.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Copying file flash:/boot.bin to chassis2#slot2#flash:/boot.bin\...\...\...\...\...\...\...\....Done.]{lang="EN-US"}

[Copying file flash:/system.bin to chassis2#slot2#flash:/system.bin\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\....Done.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x1173319121}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[boot-loader ]{lang="EN-US"}**]{#struct_0_x2076_x8851_x632516388}**[file]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display boot-loader]{lang="EN-US"}**]{#struct_0_x2076_x8851_1872427333}**[ pex]{lang="EN-US"}**
:::::

::::: {#451505726 .myid}
[]{#_Toc404782593}[]{#struct_0_x2076_x8851_x1558472604}[]{#_Toc311032813}[]{#_Toc311032814}

**软件升级 \-- 软件升级配置命令 \-- boot-loader update**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[**[![说明](软件升级命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}**]{#struct_0_x2076_x8851_x1487579602}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x2076_x8851_666149935}
:::

**[ ]{lang="EN-US"}**

[**[boot-loader update]{lang="EN-US"}**]{#struct_0_x2076_x8851_x638581472}[命令用来将备用主控板的软件版本与主用主控板的当前软件版本进行同步。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[boot-loader update]{lang="EN-US"}**]{#struct_0_x2076_x8851_x2067632675}[命令用来将从设备的软件版本与主设备的当前软件版本进行同步。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[boot-loader update]{lang="EN-US"}**]{#struct_0_x2076_x8851_819325709}[命令用来将全局备用主控板的软件版本与全局主用主控板的当前软件版本进行同步。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x1765230778}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2076_x8851_x949235278}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[boot-loader update]{lang="EN-US"}**[ { **all** \| **slot** *slot-number* }]{lang="EN-US"}]{#struct_0_x2076_x8851_x2141474092}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_x8851_1262873648}[模式：]{style="font-family:宋体"}

[**[boot-loader update]{lang="EN-US"}**[ { **all** \| **chassis** *chassis-number* **slot** *slot-number* }]{lang="EN-US"}]{#struct_0_x2076_x8851_x2059882343}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x1132011825}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x1880392126}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_496501271}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_x8851_184952832}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x30480375}

[**[all]{lang="EN-US"}**]{#struct_0_x2076_x8851_1176080226}[：表示同步升级所有备用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x2076_x8851_1176014690}[：表示同步升级所有备设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x2076_x8851_x323614870}[：表示同步升级所有全局备用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2076_x8851_x1765296314}[：表示待升级的备用主控板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2076_x8851_1984779340}[：表示待升级的成员设备的编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2076_x8851_x1431157032}[：表示待升级的全局备用主控板所在位置。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示全局备用主控板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_485024021}

[[本命令用于备用主控板和主用主控板软件版本不一致时，刷新备用主控板的软件版本，使其和主用主控板的软件版本相同。]{style="font-family:宋体"}]{#struct_0_x2076_x8851_301469777}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x1864273531}

[[请先查看软件包版本发布说明书，如果软件包需要]{style="font-family:宋体"}[License]{lang="EN-US"}]{#struct_0_x2076_x8851_x2071233777}[才能运行，且设备当前没有对应的有效的]{style="font-family:宋体"}[License]{lang="EN-US"}[时，需安装对应的]{style="font-family:宋体"}[License]{lang="EN-US"}[，再执行该命令。否则，会导致命令执行失败。]{style="font-family:宋体"}

[[通过该命令指定备用主控板的下次启动软件包时，系统会进行如下处理：]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x1531784294}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果主用主控板当前是使用主用启动软件包列表启动的，则将其主用下次启动软件包列表中的软件包拷贝到备用主控板的对应目录下，并设置为备用主控板的主用下次启动软件包。如果这些软件包中有任一软件包不存在或者不可用，则命令执行失败。]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x773943175}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果主用主控板当前是使用备用启动软件包列表启动的，则将其备用下次启动软件包列表中的软件包拷贝到备用主控板的对应目录下，并设置为备用主控板的主用下次启动软件包。如果这些软件包中有任一软件包不存在或者不可用，则命令执行失败。]{style="font-family:宋体"}]{#struct_0_x2076_x8851_707229563}

[[如果主用主控板刚安装了补丁或者进行了]{style="font-family:宋体"}[ISSU]{lang="EN-US"}]{#struct_0_x2076_x8851_x1764837562}[升级，在执行]{style="font-family:宋体"}**[boot-loader update]{lang="EN-US"}**[命令前，请执行]{style="font-family:宋体"}**[install commit]{lang="EN-US"}**[命令刷新主用主控板的下次启动软件包列表。否则，可能导致备用主控板升级后与主用主控板的版本不一致。]{style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[集中式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_x8851_1580502387}[设备]{lang="EN-US" style="font-family:宋体"}

[[请先查看软件包版本发布说明书，如果软件包需要]{style="font-family:宋体"}[License]{lang="EN-US"}]{#struct_0_x2076_x8851_x1988260448}[才能运行，且设备当前没有对应的有效的]{style="font-family:宋体"}[License]{lang="EN-US"}[时，需安装对应的]{style="font-family:宋体"}[License]{lang="EN-US"}[，再执行该命令。否则，会导致命令执行失败。]{style="font-family:宋体"}

[[通过该命令指定从设备的下次启动软件包时，系统会进行如下处理：]{style="font-family:宋体"}]{#struct_0_x2076_x8851_20137924}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果主设备当前是使用主用启动软件包列表启动的，则将其主用下次启动软件包列表中的软件包拷贝到从设备的对应目录下，并设置为从设备的主用下次启动软件包。如果这些软件包中有任一软件包不存在或者不可用，则命令执行失败。]{style="font-family:宋体"}]{#struct_0_x2076_x8851_1009257426}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果主设备当前是使用备用启动软件包列表启动的，则将其备用下次启动软件包列表中的软件包拷贝到从设备的对应目录下，并设置为从设备的主用下次启动软件包。如果这些软件包中有任一软件包不存在或者不可用，则命令执行失败。]{style="font-family:宋体"}]{#struct_0_x2076_x8851_461734395}

[[如果主用主控板刚安装了补丁或者进行了]{style="font-family:宋体"}[ISSU]{lang="EN-US"}]{#struct_0_x2076_x8851_1517130286}[升级，在执行]{style="font-family:宋体"}**[boot-loader update]{lang="EN-US"}**[命令前，请执行]{style="font-family:宋体"}**[install commit]{lang="EN-US"}**[命令刷新主用主控板的下次启动软件包列表。否则，可能导致备用主控板升级后与主用主控板的版本不一致。]{style="font-family:宋体"}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设]{style="font-family:宋体"}]{#struct_0_x2076_x8851_1465844989}[备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[请先查看软件包版本发布说明书，如果软件包需要]{style="font-family:宋体"}[License]{lang="EN-US"}]{#struct_0_x2076_x8851_x1892670152}[才能运行，且设备当前没有对应的有效的]{style="font-family:宋体"}[License]{lang="EN-US"}[时，需安装对应的]{style="font-family:宋体"}[License]{lang="EN-US"}[，再执行该命令。否则，会导致命令执行失败。]{style="font-family:宋体"}

[[通过该命令指定全局备用主控板的下次启动软件包时，系统会进行如下处理：]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x1764903098}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果全局主用主控板当前是使用主用启动软件包列表启动的，则将其主用下次启动软件包列表中的软件包拷贝到全局备用主控板的对应目录下，并设置为全局备用主控板的主用下次启动软件包。如果这些软件包中有任一软件包不存在或者不可用，则命令执行失败。]{style="font-family:宋体"}]{#struct_0_x2076_x8851_207921939}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果全局主用主控板当前是使用备用启动软件包列表启动的，则将其备用下次启动软件包列表中的软件包拷贝到全局备用主控板的对应目录下，并设置为全局备用主控板的主用下次启动软件包。如果这些软件包中有任一软件包不存在或者不可用，则命令执行失败。]{style="font-family:宋体"}]{#struct_0_x2076_x8851_1349521114}

[[如果主用主控板刚安装了补丁或者进行了]{style="font-family:宋体"}[ISSU]{lang="EN-US"}]{#struct_0_x2076_x8851_1108457423}[升级，在执行]{style="font-family:宋体"}**[boot-loader update]{lang="EN-US"}**[命令前，请执行]{style="font-family:宋体"}**[install commit]{lang="EN-US"}**[命令刷新主用主控板的下次启动软件包列表。否则，可能导致备用主控板升级后与主用主控板的版本不一致。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x536706759}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_x1187251838}[将]{style="font-family:宋体"}[1]{lang="EN-US"}[号槽位的备用主控板上的软件版本与主用主控板的软件版本同步。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> boot-loader update slot 1]{lang="EN-US"}]{#struct_0_x2076_x8851_643121458}

[This command will update the specified standby MPU. Continue? \[Y/N\]:y]{lang="EN-US"}

[Updating. Please wait\...]{lang="EN-US"}

[Copying main startup software images to slot 1. Please wait\...]{lang="EN-US"}

[Done.]{lang="EN-US"}

[Setting copied images as main startup software images for slot 1\...]{lang="EN-US"}

[Done.]{lang="EN-US"}

[Successfully updated the startup software images of slot 1.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_x1764968634}[将成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[上的软件版本与主设备的软件版本同步。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> boot-loader update slot 2]{lang="EN-US"}]{#struct_0_x2076_x8851_x799996833}

[This command will update the specified standby MPU. Continue? \[Y/N\]:y]{lang="EN-US"}

[Updating. Please wait\...]{lang="EN-US"}

[Copying main startup software images to slot 2. Please wait\...]{lang="EN-US"}

[Done.]{lang="EN-US"}

[Setting copied images as main startup software images for slot 2\...]{lang="EN-US"}

[Done.]{lang="EN-US"}

[Successfully updated the startup software images of slot 2.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_x1026879552}[将成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板上的软件版本与全局主用主控板同步。（分布式设备－]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> boot-loader update chassis 1 slot 1]{lang="EN-US"}]{#struct_0_x2076_x8851_80266943}

[This command will update the specified standby MPU. Continue? \[Y/N\]:y]{lang="EN-US"}

[Updating. Please wait\...]{lang="EN-US"}

[Copying main startup software images to chassis 1 slot 1. Please wait\...]{lang="EN-US"}

[Done.]{lang="EN-US"}

[Setting copied images as main startup software images for chassis 1 slot 1\...]{lang="EN-US"}

[Done.]{lang="EN-US"}

[Successfully updated the startup software images of chassis 1 slot 1.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x31960450}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display boot-loader]{lang="EN-US"}**]{#struct_0_x2076_x8851_x1765034170}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[install commit]{lang="EN-US"}**]{#struct_0_x2076_x8851_x1132628344}[（基本配置命令参考]{lang="EN-US" style="font-family:宋体"}[/ISSU]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}
:::::

::::: {#-1149834701 .myid}
[]{#_Toc404782594}[]{#struct_0_x2076_x8851_x926890969}[]{#_Toc304986340}[]{#_Toc262216952}[]{#_Toc262048105}[]{#_Toc206560257}

**软件升级 \-- 软件升级配置命令 \-- bootrom backup**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](软件升级命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_x8851_1089274330}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x2076_x8851_253512221}
:::

[ ]{lang="EN-US"}

[**[bootrom backup]{lang="EN-US"}**]{#struct_0_x2076_x8851_x1448152721}[命令用来将]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序从]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[的]{style="font-family:宋体"}[Normal]{lang="EN-US"}[区备份到]{style="font-family:宋体"}[Backup]{lang="EN-US"}[区。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_627851242}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2076_x8851_1567358961}

[**[bootrom backup ]{lang="EN-US"}**[\[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number ]{lang="EN-US"}*[\] ]{lang="EN-US"}[\[ **subslot** *subslot-number-list* \] \[ **all** \| **part** \]]{lang="EN-US"}]{#struct_0_x2076_x8851_x1463636200}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2076_x8851_x1764575418}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[bootrom backup]{lang="EN-US"}**[ **slot** *slot-number-list* \[ **cpu** *cpu-number* \] \[ **subslot** *subslot-number-list* \] \[ **all** \| **part** \]]{lang="EN-US"}]{#struct_0_x2076_x8851_1379837966}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_x8851_1683847948}[模式：]{style="font-family:宋体"}

[**[bootrom backup]{lang="EN-US"}**[ **chassis** *chassis-number* **slot** *slot-number-list* \[ **cpu** *cpu-number* \] \[ **subslot** *subslot-number-list* \] \[ **all** \| **part** \]]{lang="EN-US"}]{#struct_0_x2076_x8851_x1630809026}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_138261255}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x1965060619}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_1754285863}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_x8851_2115034701}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x1294808304}

[**[slot ]{lang="EN-US"}***[slot-number-list]{lang="EN-US"}*]{#struct_0_x2076_x8851_x1122116898}[：槽位号列表，表示同时备份多个单板的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ *=* { *slot-number* \[ **to** *slot-number* \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要备份的单板所在的槽位号。]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number-list]{lang="EN-US"}*]{#struct_0_x2076_x8851_x1764640954}[：成员编号列表，表示同时备份多个成员设备的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ *=* { *slot-number* \[ **to** *slot-number* \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要备份的设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number-list]{lang="EN-US"}*]{#struct_0_x2076_x8851_1486794277}[：成员编号]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[虚拟槽位号列表，表示同时备份多个成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ *=* { *slot-number* \[ **to** *slot-number* \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要备份的设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_x2076_x8851_x1569196950}[：表示需要备份]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序的设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_x2076_x8851_920734084}[：表示需要备份]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序的设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number-list]{lang="EN-US"}*]{#struct_0_x2076_x8851_1343096032}[：槽位号列表，表示同时备份多个单板的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ *=* { *slot-number* \[ **to** *slot-number* \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要备份的单板所在的槽位号。]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number-list]{lang="EN-US"}*]{#struct_0_x2076_x8851_1890078804}[：槽位号列表，表示同时备份多个单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ *=* { *slot-number* \[ **to** *slot-number* \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要备份的单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[subslot ]{lang="EN-US"}***[subslot-number-list]{lang="EN-US"}*]{#struct_0_x2076_x8851_374048821}[：子槽位号列表，表示同时备份多个子卡的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。表示方式为]{style="font-family:宋体"}*[subslot-number-list]{lang="EN-US"}*[ *=* { *subslot-number* \[ **to** *subslot-number* \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[subslot-number]{lang="EN-US"}*[表示需要备份的子卡所在的子槽位号。]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。不使用该参数时，表示备份的是单板的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x2076_x8851_x1760042832}[：操作]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序的全部内容。不指定]{style="font-family:宋体"}**[all]{lang="EN-US"}**[和]{style="font-family:宋体"}**[part]{lang="EN-US"}**[参数时，默认使用]{style="font-family:宋体"}**[all]{lang="EN-US"}**[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[part]{lang="EN-US"}**]{#struct_0_x2076_x8851_1299122753}[：只操作]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序的扩展段（]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序分为两部分：基本段和扩展段，基本段提供]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[菜单的基本操作项，扩展段提供更多的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[菜单操作项）。不指定]{style="font-family:宋体"}**[all]{lang="EN-US"}**[和]{style="font-family:宋体"}**[part]{lang="EN-US"}**[参数时，默认使用]{style="font-family:宋体"}**[all]{lang="EN-US"}**[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number]{lang="EN-US"}*]{#struct_0_x2076_x8851_1176080225}[：备份指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_1475768157}

[[Boot ROM]{lang="EN-US"}]{#struct_0_x2076_x8851_x1744597037}[分为]{style="font-family:宋体"}[Normal]{lang="EN-US"}[区和]{style="font-family:宋体"}[Backup]{lang="EN-US"}[区。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_x2076_x8851_150939352}[区用于存放]{lang="EN-US" style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。设备启动时，会自动读取]{lang="EN-US" style="font-family:宋体"}[Normal]{lang="EN-US"}[区的]{lang="EN-US" style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。]{lang="EN-US" style="font-family:宋体"}[如果]{style="font-family:宋体"}[Normal]{lang="EN-US"}[区的]{lang="EN-US" style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序]{lang="EN-US" style="font-family:宋体"}[不可用，再自动读取]{style="font-family:宋体"}[Backup]{lang="EN-US"}[区的]{lang="EN-US" style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backup]{lang="EN-US"}]{#struct_0_x2076_x8851_x1765099705}[区用于存放]{lang="EN-US" style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序的副本。如果在设备运行过程中，]{lang="EN-US" style="font-family:宋体"}[Normal]{lang="EN-US"}[区的]{lang="EN-US" style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序被损坏或者需要版本回退，可以使用]{lang="EN-US" style="font-family:宋体"}**[bootrom restore]{lang="EN-US"}**[命令将]{lang="EN-US" style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序从]{lang="EN-US" style="font-family:宋体"}[Backup]{lang="EN-US"}[区恢复到]{lang="EN-US" style="font-family:宋体"}[Normal]{lang="EN-US"}[区。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x2140092181}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_x339177397}[将]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序从]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[的]{style="font-family:宋体"}[Normal]{lang="EN-US"}[区备份到]{style="font-family:宋体"}[Backup]{lang="EN-US"}[区。]{style="font-family:宋体"}

[[\<Sysname\> bootrom backup all]{lang="EN-US"}]{#struct_0_x2076_x8851_754353208}

[Now backing up the Boot ROM, please wait\...]{lang="EN-US"}

[\...\...Done.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x1717354354}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[bootrom restore]{lang="EN-US"}**]{#struct_0_x2076_x8851_x1743372357}
:::::

::::: {#1266183364 .myid}
[]{#_Toc404782595}[]{#struct_0_x2076_x8851_x242100928}

**软件升级 \-- 软件升级配置命令 \-- bootrom read**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](软件升级命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_x8851_x176287543}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x2076_x8851_x1765165241}
:::

[ ]{lang="EN-US"}

[**[bootrom read]{lang="EN-US"}**]{#struct_0_x2076_x8851_1012383025}[命令用来将]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序从]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[的]{style="font-family:宋体"}[Normal]{lang="EN-US"}[区读取到]{style="font-family:宋体"}[Flash]{lang="EN-US"}[中。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_1412474745}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2076_x8851_730388233}

[**[bootrom read]{lang="EN-US"}***[ ]{lang="EN-US"}*[\[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number ]{lang="EN-US"}*[\] ]{lang="EN-US"}[\[ **subslot** *subslot-number-list* \] \[ **all** \| **part** \]]{lang="EN-US"}]{#struct_0_x2076_x8851_544547379}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2076_x8851_301776562}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[bootrom read]{lang="EN-US"}***[ ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number-list ]{lang="EN-US"}*[\[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number ]{lang="EN-US"}*[\] ]{lang="EN-US"}[\[ **subslot** *subslot-number-list* \] \[ **all** \| **part** \]]{lang="EN-US"}]{#struct_0_x2076_x8851_779442837}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_x8851_507943269}[模式：]{style="font-family:宋体"}

[**[bootrom read]{lang="EN-US"}**[ **chassis** *chassis-number* **slot** *slot-number-list* \[ **cpu** *cpu-number* \] \[ **subslot** *subslot-number-list* \] \[ **all** \| **part** \]]{lang="EN-US"}]{#struct_0_x2076_x8851_x1422848588}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x1765230777}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x1352519805}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x1351184479}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_x8851_x1765518291}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x824452310}

[**[slot ]{lang="EN-US"}***[slot-number-list]{lang="EN-US"}*]{#struct_0_x2076_x8851_x974919027}[：槽位号列表，表示同时读取多个单板的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ *=* { *slot-number* \[ **to** *slot-number* \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要读取的单板所在的槽位号。]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number-list]{lang="EN-US"}*]{#struct_0_x2076_x8851_1944971631}[：成员编号列表，表示同时读取多个成员设备的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ *=* { *slot-number* \[ **to** *slot-number* \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要读取的设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number-list]{lang="EN-US"}*]{#struct_0_x2076_x8851_1083509750}[：成员编号]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[虚拟槽位号列表，表示同时读取多个成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ *=* { *slot-number* \[ **to** *slot-number* \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要读取的设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_x2076_x8851_x1472874679}[：表示需要读取]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序的设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_x2076_x8851_x818067825}[：表示需要读取]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序的设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number-list]{lang="EN-US"}*]{#struct_0_x2076_x8851_x856334584}[：槽位号列表，表示同时读取多个单板的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ *=* { *slot-number* \[ **to** *slot-number* \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要读取的单板所在的槽位号。]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number-list]{lang="EN-US"}*]{#struct_0_x2076_x8851_x482574191}[：槽位号列表，表示同时读取多个单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ *=* { *slot-number* \[ **to** *slot-number* \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要备份的单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[subslot ]{lang="EN-US"}***[subslot-number-list]{lang="EN-US"}*]{#struct_0_x2076_x8851_x2022301756}[：子槽位号列表，表示同时读取多个子卡的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。表示方式为]{style="font-family:宋体"}*[subslot-number-list]{lang="EN-US"}*[ *=* { *subslot-number* \[ **to** *subslot-number* \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[subslot-number]{lang="EN-US"}*[表示需要读取的子卡所在的子槽位号。]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。不使用该参数时，表示读取的是单板的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x2076_x8851_x1765296313}[：操作]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序的全部内容。不指定]{style="font-family:宋体"}**[all]{lang="EN-US"}**[和]{style="font-family:宋体"}**[part]{lang="EN-US"}**[参数时，默认使用]{style="font-family:宋体"}**[all]{lang="EN-US"}**[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[part]{lang="EN-US"}**]{#struct_0_x2076_x8851_x387873655}[：只操作]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序的扩展段。不指定]{style="font-family:宋体"}**[all]{lang="EN-US"}**[和]{style="font-family:宋体"}**[part]{lang="EN-US"}**[参数时，默认使用]{style="font-family:宋体"}**[all]{lang="EN-US"}**[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number]{lang="EN-US"}*]{#struct_0_x2076_x8851_1176276836}[：读取指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x634138418}

[[成功执行]{style="font-family:宋体"}**[bootrom read]{lang="EN-US"}**]{#struct_0_x2076_x8851_1706198758}[命令后，系统会自动生成]{style="font-family:宋体"}[basicbtm.bin]{lang="EN-US"}[和]{style="font-family:宋体"}[extendbtm.bin]{lang="EN-US"}[文件并保存到]{style="font-family:宋体"}[Flash]{lang="EN-US"}[中。其中，]{style="font-family:宋体"}[basicbtm.bin]{lang="EN-US"}[存储了]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序的基本段，]{style="font-family:宋体"}[extendbtm.bin]{lang="EN-US"}[存储了]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序的扩展段。如果在设备运行过程中，]{style="font-family:宋体"}[Normal]{lang="EN-US"}[区的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序被损坏或者需要版本回退，可以使用]{style="font-family:宋体"}**[bootrom update]{lang="EN-US"}**[命令重新加载之前生成的]{style="font-family:宋体"}[basicbtm.bin]{lang="EN-US"}[和]{style="font-family:宋体"}[extendbtm.bin]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x822753115}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_1868848973}[读取]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。]{style="font-family:宋体"}

[[\<Sysname\> bootrom read all]{lang="EN-US"}]{#struct_0_x2076_x8851_x285495823}

[  Now reading the Boot ROM, please wait\...]{lang="EN-US"}

[\...\...\...Done.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x1898607629}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[bootrom ]{lang="EN-US"}**]{#struct_0_x2076_x8851_x1764837561}**[update]{lang="EN-US"}**
:::::

::::: {#1661569207 .myid}
[]{#_Toc404782596}[]{#struct_0_x2076_x8851_1177217860}

**软件升级 \-- 软件升级配置命令 \-- bootrom restore**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](软件升级命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_x8851_x723354542}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x2076_x8851_x31641946}
:::

[ ]{lang="EN-US"}

[**[bootrom restore]{lang="EN-US"}**]{#struct_0_x2076_x8851_x403963168}[命令用来将]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序从]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[的]{style="font-family:宋体"}[Backup]{lang="EN-US"}[区恢复到]{style="font-family:宋体"}[Normal]{lang="EN-US"}[区。。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x547914458}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2076_x8851_1180843841}

[**[bootrom]{lang="EN-US"}**[ **restore** \[ **cpu** *cpu-number* \] \[ **subslot** *subslot-number-list* \] \[ **all** \| **part** \]]{lang="EN-US"}]{#struct_0_x2076_x8851_1827144147}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2076_x8851_878731609}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[bootrom]{lang="EN-US"}**[ **restore** **slot** *slot-number-list* \[ **cpu** *cpu-number* \] \[ **subslot** *subslot-number-list* \] \[ **all** \| **part** \]]{lang="EN-US"}]{#struct_0_x2076_x8851_x1764903097}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_x8851_967436826}[模式：]{style="font-family:宋体"}

[**[bootrom restore]{lang="EN-US"}**[ **chassis** *chassis-number* **slot** *slot-number-list* \[ **cpu** *cpu-number* \] \[ **subslot** *subslot-number-list* \] \[ **all** \| **part** \]]{lang="EN-US"}]{#struct_0_x2076_x8851_x709841317}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_1766352513}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x1269023453}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x1051017824}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_x8851_x1637519630}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_1686632849}

[**[slot ]{lang="EN-US"}***[slot-number-list]{lang="EN-US"}*]{#struct_0_x2076_x8851_x306409995}[：槽位号列表，表示同时恢复多个单板的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ *=* { *slot-number* \[ **to** *slot-number* \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要恢复的单板所在的槽位号。]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number-list]{lang="EN-US"}*]{#struct_0_x2076_x8851_x494859556}[：成员编号列表，表示同时恢复多个成员设备的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ *=* { *slot-number* \[ **to** *slot-number* \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要恢复的设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number-list]{lang="EN-US"}*]{#struct_0_x2076_x8851_x1645373605}[：成员编号]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[虚拟槽位号列表，表示同时恢复多个成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ *=* { *slot-number* \[ **to** *slot-number* \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要恢复的设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_x2076_x8851_x1764968633}[：表示需要恢复]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序的设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_x2076_x8851_x739582756}[：表示需要恢复]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序的设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number-list]{lang="EN-US"}*]{#struct_0_x2076_x8851_1572656162}[：槽位号列表，表示同时恢复多个单板的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ *=* { *slot-number* \[ **to** *slot-number* \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要恢复的单板所在的槽位号。]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number-list]{lang="EN-US"}*]{#struct_0_x2076_x8851_x1598319438}[：槽位号列表，表示同时恢复多个单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ *=* { *slot-number* \[ **to** *slot-number* \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要恢复的单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[subslot ]{lang="EN-US"}***[subslot-number-list]{lang="EN-US"}*]{#struct_0_x2076_x8851_1218572384}[：子槽位号列表，表示同时恢复多个子卡的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。表示方式为]{style="font-family:宋体"}*[subslot-number-list]{lang="EN-US"}*[ *=* { *subslot-number* \[ **to** *subslot-number* \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[subslot-number]{lang="EN-US"}*[表示需要恢复的子卡所在的子槽位号。]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。不使用该参数时，表示不恢复子卡。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x2076_x8851_x1490347180}[：操作]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序的全部内容。不指定]{style="font-family:宋体"}**[all]{lang="EN-US"}**[和]{style="font-family:宋体"}**[part]{lang="EN-US"}**[参数时，默认使用]{style="font-family:宋体"}**[all]{lang="EN-US"}**[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[part]{lang="EN-US"}**]{#struct_0_x2076_x8851_x1766089938}[：只操作]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序的扩展段。不指定]{style="font-family:宋体"}**[all]{lang="EN-US"}**[和]{style="font-family:宋体"}**[part]{lang="EN-US"}**[参数时，默认使用]{style="font-family:宋体"}**[all]{lang="EN-US"}**[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number]{lang="EN-US"}*]{#struct_0_x2076_x8851_1176735587}[：恢复指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x883249868}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_97260549}[恢复]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。]{style="font-family:宋体"}

[[\<Sysname\> bootrom restore all]{lang="EN-US"}]{#struct_0_x2076_x8851_x1962847585}

[  This command will restore the Boot ROM file, Continue? \[Y/N\]:y]{lang="EN-US"}

[  Now restoring the Boot ROM, please wait\...]{lang="EN-US"}

[\...\...Done.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x1765034169}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[bootrom backup]{lang="EN-US"}**]{#struct_0_x2076_x8851_1239959115}
:::::

::: {#370838168 .myid}
[]{#_Toc404782597}[]{#struct_0_x2076_x8851_2091664434}

**软件升级 \-- 软件升级配置命令 \-- bootrom update**

------------------------------------------------------------------------

[**[bootrom update]{lang="EN-US"}**]{#struct_0_x2076_x8851_1349459673}[命令用来加载]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x867279678}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2076_x8851_1910960222}

[**[bootrom update]{lang="EN-US"}**[ **file** *file-url* \[ **cpu** *cpu-number* \] \[ **subslot** *subslot-number-list* \] \[ **all** \| **part** \]]{lang="EN-US"}]{#struct_0_x2076_x8851_657654780}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2076_x8851_x544711229}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[bootrom update]{lang="EN-US"}**[ **file** *file-url* **slot** *slot-number-list* \[ **cpu** *cpu-number* \] \[ **subslot** *subslot-number-list* \] \[ **all** \| **part** \]]{lang="EN-US"}]{#struct_0_x2076_x8851_1270842889}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_x8851_x605938371}[模式：]{style="font-family:宋体"}

[**[bootrom update]{lang="EN-US"}**[ **file** *file-url* **chassis** *chassis-number* **slot** *slot-number-list* \[ **cpu** *cpu-number* \] \[ **subslot** *subslot-number-list* \] \[ **all** \| **part** \]]{lang="EN-US"}]{#struct_0_x2076_x8851_x1764575417}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_620323079}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x1589377492}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_590793384}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_x8851_133340480}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_1612333611}

[**[file]{lang="EN-US"}**[ *file-url*]{lang="EN-US"}]{#struct_0_x2076_x8851_621389685}[：]{style="font-family:宋体"}[Flash]{lang="EN-US"}[中包含]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序的文件，]{style="font-family:宋体"}*[file-url]{lang="EN-US"}*[表示用于]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序升级的文件的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number-list]{lang="EN-US"}*]{#struct_0_x2076_x8851_1282724315}[：槽位号列表，表示同时升级多个单板的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ *=* { *slot-number* \[ **to** *slot-number* \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要升级的单板所在的槽位号。]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number-list]{lang="EN-US"}*]{#struct_0_x2076_x8851_x1405007490}[：成员编号列表，表示同时升级多个成员设备的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ *=* { *slot-number* \[ **to** *slot-number* \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要升级的设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number-list]{lang="EN-US"}*]{#struct_0_x2076_x8851_x1242154614}[：成员编号]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[虚拟槽位号列表，表示同时升级多个成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ *=* { *slot-number* \[ **to** *slot-number* \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要升级的设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_x2076_x8851_x1764640953}[：表示需要升级]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序的设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_x2076_x8851_x208410364}[：表示需要升级]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序的设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number-list]{lang="EN-US"}*]{#struct_0_x2076_x8851_x1165912423}[：槽位号列表，表示同时升级多个单板的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ *=* { *slot-number* \[ **to** *slot-number* \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要升级的单板所在的槽位号。]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number-list]{lang="EN-US"}*]{#struct_0_x2076_x8851_x1627197080}[：槽位号列表，表示同时升级多个单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ *=* { *slot-number* \[ **to** *slot-number* \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要升级的单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[subslot ]{lang="EN-US"}***[subslot-number-list]{lang="EN-US"}*]{#struct_0_x2076_x8851_x1154759208}[：子槽位号列表，表示同时升级多个子卡的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。表示方式为]{style="font-family:宋体"}*[subslot-number-list]{lang="EN-US"}*[ *=* { *subslot-number* \[ **to** *subslot-number* \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[subslot-number]{lang="EN-US"}*[表示需要升级的子卡所在的子槽位号。]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。不使用该参数时，表示不升级子卡。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x2076_x8851_1994503588}[：操作]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序的全部内容。不指定]{style="font-family:宋体"}**[all]{lang="EN-US"}**[和]{style="font-family:宋体"}**[part]{lang="EN-US"}**[参数时，默认使用]{style="font-family:宋体"}**[all]{lang="EN-US"}**[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[part]{lang="EN-US"}**]{#struct_0_x2076_x8851_x948831679}[：只操作]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序的扩展段。不指定]{style="font-family:宋体"}**[all]{lang="EN-US"}**[和]{style="font-family:宋体"}**[part]{lang="EN-US"}**[参数时，默认使用]{style="font-family:宋体"}**[all]{lang="EN-US"}**[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number]{lang="EN-US"}*]{#struct_0_x2076_x8851_1176014691}[：更新指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x2129295766}

[[Boot ROM]{lang="EN-US"}]{#struct_0_x2076_x8851_1118969077}[程序通过]{style="font-family:宋体"}[Boot]{lang="EN-US"}[包（]{style="font-family:宋体"}[\*.bin]{lang="EN-US"}[）发布，产品会将需要升级的单板的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序集成到]{style="font-family:宋体"}[Boot]{lang="EN-US"}[包中。此时，可是使用]{style="font-family:宋体"}**[bootrom update]{lang="EN-US"}**[命令，将升级文件指定为]{style="font-family:宋体"}[Boot]{lang="EN-US"}[包，系统会根据单板的型号自动将相应的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序加载到]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[中；也可以在升级]{style="font-family:宋体"}[Boot]{lang="EN-US"}[包的同时完成]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序的加载。]{style="font-family:宋体"}

[[执行该命令后，设备会将]{style="font-family:宋体"}[Flash]{lang="EN-US"}]{#struct_0_x2076_x8851_x426363842}[中的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序加载到]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[的]{style="font-family:宋体"}[Normal]{lang="EN-US"}[区。设备启动时，会直接使用]{style="font-family:宋体"}[Normal]{lang="EN-US"}[区的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。因此，如果]{style="font-family:宋体"}[Flash]{lang="EN-US"}[空间不足，]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序加载完成之后，]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[文件可以删除。]{style="font-family:宋体"}

[[加载后，要使新的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}]{#struct_0_x2076_x8851_2056871628}[程序生效，需要重启设备。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x599153937}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_x1765099708}[使用]{style="font-family:宋体"}[a.bin]{lang="EN-US"}[文件升级设备的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序。]{style="font-family:宋体"}

[[\<Sysname\> bootrom update file a.bin]{lang="EN-US"}]{#struct_0_x2076_x8851_2107820948}

[   This command will update the Boot ROM file on the specified board(s), Continue? \[Y/N\]:y]{lang="EN-US"}

[   Now updating the Boot ROM, please wait\...]{lang="EN-US"}

[\...\...\...\....Done.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_26613349}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[boot-loader file]{lang="EN-US"}**]{#struct_0_x2076_x8851_1728910871}
:::

::::: {#-917895862 .myid}
[]{#_Toc404782598}[]{#struct_0_x2076_x8851_1458582205}[]{#_Toc304986341}[]{#_Toc262216953}[]{#_Toc262048106}[]{#_Toc206560258}[]{#_Toc136403365}[]{#_Toc98563138}[]{#_Toc182048949}[]{#_Toc182120798}[]{#_Toc130782577}[]{#_Toc130786976}[]{#_Toc130782581}[]{#_Toc130786980}

**软件升级 \-- 软件升级配置命令 \-- bootrom-update security-check enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](软件升级命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_x8851_x259245256}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x2076_x8851_1850583771}
:::

[ ]{lang="EN-US"}

[**[bootrom-update security-check enable]{lang="EN-US"}**]{#struct_0_x2076_x8851_x1993488744}[命令用来开启]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序合法性检查功能。]{style="font-family:宋体"}

[**[undo bootrom-update security-check enable]{lang="EN-US"}**]{#struct_0_x2076_x8851_x1765165244}[命令用来关闭]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[程序合法性检查功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_1771897912}

[**[bootrom-update security-check enable]{lang="EN-US"}**]{#struct_0_x2076_x8851_1254849286}

[**[undo bootrom-update security-check enable]{lang="EN-US"}**]{#struct_0_x2076_x8851_2117882958}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_147197547}

[[Boot ROM]{lang="EN-US"}]{#struct_0_x2076_x8851_x754544204}[程序合法性检查功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_1670062077}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_x8851_659168835}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_1268487460}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_x8851_x1765230780}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x593463670}

[[如果使能了该功能，则在升级]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}]{#struct_0_x2076_x8851_372885594}[程序时，设备会先检查]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[文件的合法性：包括]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[文件是否有效以及是否和硬件匹配等。检查通过后，才会升级。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x101987296}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_x9351263}[启动]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[升级时的合法性检查功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_x8851_x1716839779}

[\[Sysname\] bootrom-update security-check enable]{lang="EN-US"}
:::::

::: {#-1577922449 .myid}
[]{#_Toc404782599}[]{#struct_0_x2076_x8851_x1566381861}

**软件升级 \-- 软件升级配置命令 \-- display boot-loader**

------------------------------------------------------------------------

[**[display boot-loader]{lang="EN-US"}**]{#struct_0_x2076_x8851_1996603100}[命令用来显示]{style="font-family:宋体"}[本次启动和下次启动所采用的启动软件包的名称]{style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x1446249830}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x1765296316}

[**[display boot-loader]{lang="EN-US"}**]{#struct_0_x2076_x8851_x1147388542}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2076_x8851_x1029046800}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display boot-loader ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ ]{lang="EN-US"}]{#struct_0_x2076_x8851_x431046932}**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}[ \] \]]{lang="EN-US"}

[[分布式设备]{style="font-family:宋体"}]{#struct_0_x2076_x8851_247396474}[－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模]{style="font-family:宋体"}[式：]{style="font-family:宋体"}

[**[display boot-loader ]{lang="EN-US"}**[\[ **chassis** *chassis-number* \[ **slot** *slot-number* \[ ]{lang="EN-US"}]{#struct_0_x2076_x8851_1048312229}**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}[ \] \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x1256301883}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2076_x8851_1945206783}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_110004334}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_x8851_x1539592365}

[[network-operator]{lang="EN-US"}]{#struct_0_x2076_x8851_x1764837564}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_417702973}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2076_x8851_x985528688}[：表示主控板所在的槽位号。不指定该参数时，表示设备上的所有主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2076_x8851_114663419}[：表示成员设备的编号。不指定该参数时，表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有成员设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2076_x8851_x504467153}[：表示指定成员设备上的指定主控板。]{style="font-family:宋体"}**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*[表示主控板所在的槽位号。不指定该参数时，表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**]{#struct_0_x2076_x8851_1176670054}[ *cpu-number*]{lang="EN-US"}[：表示安全引擎的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数专用于显示安全引擎]{style="font-family:宋体"}[本次启动和下次启动所采用的启动软件包的名称]{style="font-family:宋体"}[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x1707704150}

[[使用该命令可显示父设备、]{style="font-family:宋体"}[PEX]{lang="EN-US"}]{#struct_0_x2076_x8851_x1955736716}[设备和安全引擎本次启动和下次启动所采用的启动软件包的名称。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于本地有存储介质的]{style="font-family:宋体"}]{#struct_0_x2076_x8851_1176407910}[PEX]{lang="EN-US"}[设备，会显示本次启动和下次启动所采用的启动软件包的名称。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于本地无存储介质的]{style="font-family:宋体"}]{#struct_0_x2076_x8851_2073918345}[PEX]{lang="EN-US"}[设备，只显示本次启动软件包的名称。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于安全引擎，会显示本次启动和下次启动所采用的启动软件包的名称。]{style="font-family:宋体"}]{#struct_0_x2076_x8851_1176080230}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_1443385143}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_1992025636}[显示本次启动和下次启动所采用的启动软件包的名称（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（]{style="font-family:宋体"}[集中式设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display boot-loader]{lang="EN-US"}]{#struct_0_x2076_x8851_x1196575998}

[Software images on the device:]{lang="EN-US"}

[Current software images:]{lang="EN-US"}

[  flash:/simware-cmw710-boot-a1701.bin]{lang="EN-US"}

[  flash:/simware-cmw710-system-a1701.bin]{lang="EN-US"}

[Main startup software images:]{lang="EN-US"}

[  flash:/simware-cmw710-boot-a1701.bin]{lang="EN-US"}

[  flash:/simware-cmw710-system-a1701.bin]{lang="EN-US"}

[  flash:/simware-cmw710-ssh-a1701.bin]{lang="EN-US"}

[Backup startup software images:]{lang="EN-US"}

[  flash:/simware-cmw710-boot-a1701.bin]{lang="EN-US"}

[  flash:/simware-cmw710-system-a1701.bin]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_x1962796247}[显示本次启动和下次启动所采用的启动软件包的名称（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display boot-loader]{lang="EN-US"}]{#struct_0_x2076_x8851_13343119}

[Software images on slot 0:]{lang="EN-US"}

[Current software images:]{lang="EN-US"}

[  flash:/simware-cmw710-boot-a1701.bin]{lang="EN-US"}

[  flash:/simware-cmw710-system-a1701.bin]{lang="EN-US"}

[Main startup software images:]{lang="EN-US"}

[  flash:/simware-cmw710-boot-a1701.bin]{lang="EN-US"}

[  flash:/simware-cmw710-system-a1701.bin]{lang="EN-US"}

[  flash:/simware-cmw710-ssh-a1701.bin]{lang="EN-US"}

[Backup startup software images:]{lang="EN-US"}

[  flash:/simware-cmw710-boot-a1701.bin]{lang="EN-US"}

[  flash:/simware-cmw710-system-a1701.bin]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_1155581854}[显示本次启动和下次启动所采用的启动软件包的名称（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（分布式设]{style="font-family:宋体"}[备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display boot-loader]{lang="EN-US"}]{#struct_0_x2076_x8851_x1552740822}

[Software images on chassis 0 slot 1:]{lang="EN-US"}

[Current software images:]{lang="EN-US"}

[  flash:/simware-cmw710-boot-a1701.bin]{lang="EN-US"}

[  flash:/simware-cmw710-system-a1701.bin]{lang="EN-US"}

[Main startup software images:]{lang="EN-US"}

[  flash:/simware-cmw710-boot-a1701.bin]{lang="EN-US"}

[  flash:/simware-cmw710-system-a1701.bin]{lang="EN-US"}

[  flash:/simware-cmw710-ssh-a1701.bin]{lang="EN-US"}

[Backup startup software images:]{lang="EN-US"}

[  flash:/simware-cmw710-boot-a1701.bin]{lang="EN-US"}

[  flash:/simware-cmw710-system-a1701.bin]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_x141685744}[显示本次启动和下次启动所采用的启动软件包的名称（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display boot-loader]{lang="EN-US"}]{#struct_0_x2076_x8851_x141030384}

[Software images on slot 1:]{lang="EN-US"}

[Current software images:]{lang="EN-US"}

[  flash:/s5820v2_5830v2-cmw710-boot-d2402.bin]{lang="EN-US"}

[  flash:/s5820v2_5830v2-cmw710-systemt-d2402.bin]{lang="EN-US"}

[Main startup software images:]{lang="EN-US"}

[  flash:/s5820v2_5830v2-cmw710-boot-d2402.bin]{lang="EN-US"}

[  flash:/s5820v2_5830v2-cmw710-systemt-d2402.bin]{lang="EN-US"}

[Backup startup software images:]{lang="EN-US"}

[  flash:/s5820v2_5830v2-cmw710-boot-d2402.bin]{lang="EN-US"}

[  flash:/s5820v2_5830v2-cmw710-systemt-d2402.bin]{lang="EN-US"}

[Software images on slot 101:]{lang="EN-US"}

[Current software images:]{lang="EN-US"}

[  flash:/rpu-s5800-boot-d2402.bin]{lang="EN-US"}

[  flash:/rpu-s5800-boot-systemt-d2402.bin]{lang="EN-US"}

[Main startup software images:]{lang="EN-US"}

[  flash:/rpu-s5800-boot-boot-d2402.bin]{lang="EN-US"}

[  flash:/rpu-s5800-boot-systemt-d2402.bin]{lang="EN-US"}

[Backup startup software images:]{lang="EN-US"}

[  flash:/rpu-s5800-boot-boot-d2402.bin]{lang="EN-US"}

[  flash:/rpu-s5800-boot-systemt-d2402.bin]{lang="EN-US"}

[Software images on slot 105:]{lang="EN-US"}

[Current software images:]{lang="EN-US"}

[  flash:/rpu-s5120hi-boot.bin]{lang="EN-US"}

[  flash:/rpu-s5120hi-system.bin]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_x141554673}[显示本次启动和下次启动所采用的启动软件包的名称（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display boot-loader]{lang="EN-US"}]{#struct_0_x2076_x8851_x141882353}

[Software images on chassis 0 slot 1:]{lang="EN-US"}

[Current software images:]{lang="EN-US"}

[  flash:/s10500-cmw710-boot-a0046.bin]{lang="EN-US"}

[  flash:/s10500-cmw710-system-a0046.bin]{lang="EN-US"}

[Main startup software images:]{lang="EN-US"}

[  flash:/s10500-cmw710-boot-a0046.bin]{lang="EN-US"}

[  flash:/s10500-cmw710-system-a0046.bin]{lang="EN-US"}

[Backup startup software images:]{lang="EN-US"}

[  flash:/s10500-cmw710-boot-a0046.bin]{lang="EN-US"}

[  flash:/s10500-cmw710-system-a0046.bin]{lang="EN-US"}

[Software images on chassis 5 slot 1:]{lang="EN-US"}

[Current software images:]{lang="EN-US"}

[  flash:/rpu-s5800-boot-d2402.bin]{lang="EN-US"}

[  flash:/rpu-s5800-systemt-d2402.bin]{lang="EN-US"}

[Main startup software images:]{lang="EN-US"}

[  flash:/rpu-s5800-boot-d2402.bin]{lang="EN-US"}

[  flash:/rpu-s5800-systemt-d2402.bin]{lang="EN-US"}

[Backup startup software images:]{lang="EN-US"}

[  flash:/rpu-s5800-boot-d2402.bin]{lang="EN-US"}

[  flash:/rpu-s5800-systemt-d2402.bin]{lang="EN-US"}

[Software images on chassis 5 slot 10:]{lang="EN-US"}

[Current software images:]{lang="EN-US"}

[  flash:/rpu-s5120hi-boot.bin]{lang="EN-US"}

[  flash:/rpu-s5120hi-systemt.bin]{lang="EN-US"}

[]{#struct_0_x2076_x8851_1259018962}[[表1-1 ]{lang="EN-US"}[display boot-loader]{lang="EN-US"}]{#_Ref291745733}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x858923894}[[字段]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x1764640956}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x406397536}

[[Software images on the device]{lang="EN-US"}]{#struct_0_x2076_x8851_x1641460011}

[[启动软件包的相关信息（集中式设备）]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x1377419367}

[[Software images on slot ]{lang="EN-US"}]{#struct_0_x2076_x8851_x2077853273}*[n]{lang="EN-US" style="font-size:10.5pt"}*

[[位于槽位]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_x2076_x8851_1894843433}[上的某主控板的启动软件包的相关信息（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[成员编号为]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_x2076_x8851_1209989589}[的某成员设备的启动软件包的相关信息（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[Software images on chassis *m* slot *n*]{lang="EN-US"}]{#struct_0_x2076_x8851_1462189118}

[[某主控板的启动软件包的相关信息，该主控板位于成员设备]{style="font-family:宋体"}*[m]{lang="EN-US"}*]{#struct_0_x2076_x8851_x1765099707}[的]{style="font-family:宋体"}*[n]{lang="EN-US"}*[号槽位上（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Current software images]{lang="EN-US"}]{#struct_0_x2076_x8851_x977292767}

[[最近一次启动使用的启动软件包列表]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x518657267}

[[Main startup software images]{lang="EN-US"}]{#struct_0_x2076_x8851_x281131141}

[[主用下次启动软件包列表]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x1252345602}

[[Backup startup software images]{lang="EN-US"}]{#struct_0_x2076_x8851_x754062714}

[[备用下次启动软件包列表]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x1765165243}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x150416389}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[boot-loader file]{lang="EN-US"}**]{#struct_0_x2076_x8851_x1554958609}

::::: {#-479590437 .myid}
[]{#_Toc404782600}[]{#struct_0_x2076_x8851_1176473445}[]{#_Toc368057763}

**软件升级 \-- 软件升级配置命令 \-- display boot-loader blade**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](软件升级命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_x8851_x229570575}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x2076_x8851_x1894448836}
:::

[ ]{lang="EN-US"}

[**[display]{lang="EN-US"}**[ **boot-loader blade**]{lang="EN-US"}]{#struct_0_x2076_x8851_1176407909}[命令用来显示安全引擎的加载]{style="font-family:宋体"}[软件包列表]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_2073459594}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2076_x8851_x1200948140}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[**[display boot-loader blade ]{lang="EN-US"}**[\[ *blade-model* \]]{lang="EN-US"}]{#struct_0_x2076_x8851_1176014693}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x323549334}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x1552278841}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x1552344377}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_x8851_x1552147769}

[[network-operator]{lang="EN-US"}]{#struct_0_x2076_x8851_x911980323}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x1552213305}

[*[blade-model]{lang="EN-US"}*]{#struct_0_x2076_x8851_x1552540985}[：设备支持的]{style="font-family:宋体"}[安全引擎的型号，该参数必须完整输入，不区分大小写。]{style="font-family:宋体"}[可输入]{style="font-family:
宋体"}**[boot-loader blade ]{lang="EN-US"}[？]{style="font-family:宋体"}**[，来获取该参数的取值。不指定该参数时，表示设备支持的所有型号的安全引擎。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_1362088343}

[[加载]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x1552606521}[软件包列表中记录了加载软件包存储的位置、]{style="font-family:宋体"}[安全引擎的型号、加载启动软件包的名称。当安全引擎需要使用加载软件包启动时，就会根据该列表去当前主用主控板加载这些软件包。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x1552409913}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_x1123820871}[查看所有安全引擎在所有主控板上的加载]{style="font-family:宋体"}[软件包列表。]{style="font-family:宋体"}

[[\<Sysname\> display boot-loader blade Blade-m9k]{lang="EN-US"}]{#struct_0_x2076_x8851_x1552475449}

[Startup software image files for BLADEs to load from the parent device:]{lang="EN-US"}

[Blade model: Blade-m9k]{lang="EN-US"}

[  flash:/blade3fwm9k-cmw710-boot-a0002.bin]{lang="EN-US"}

[  flash:/blade3fwm9k-cmw710-system-a0002.bin]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display boot-loader blade]{lang="EN-US"}]{#struct_0_x2076_x8851_x229636111}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1191799044}[[字段]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x229439503}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x2076_x8851_1199184587}

[[Startup software image files for BLADEs to load from the parent device]{lang="EN-US"}]{#struct_0_x2076_x8851_x229505039}

[[安全引擎的加载软件包列表]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x229963790}

[[Blade model]{lang="EN-US"}]{#struct_0_x2076_x8851_x230029326}

[[安全引擎的型号]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x78442002}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

::: {#-832293142 .myid}
[]{#_Toc404782601}[]{#struct_0_x2076_x8851_939299030}[]{#_Toc360431297}[]{#_Toc358447386}

**软件升级 \-- 软件升级配置命令 \-- display boot-loader pex**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **boot-loader pex**]{lang="EN-US"}]{#struct_0_x2076_x8851_1631418270}[命令用来显示]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的加载]{style="font-family:宋体"}[软件包列表]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_939299033}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2076_x8851_x141685745}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[**[display boot-loader pex]{lang="EN-US"}**[ \[ *pex-model* \]]{lang="EN-US"}]{#struct_0_x2076_x8851_x141095921}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_939299034}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2076_x8851_1631418274}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_939299037}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_x8851_1631418273}

[[network-operator]{lang="EN-US"}]{#struct_0_x2076_x8851_939299036}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_1631418272}

[*[pex-model]{lang="EN-US"}*]{#struct_0_x2076_x8851_939299039}[：设备支持的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的型号，该参数必须完整输入，不区分大小写。]{style="font-family:宋体"}[可输入]{style="font-family:
宋体"}**[boot-loader pex ]{lang="EN-US"}[？]{style="font-family:宋体"}**[，回车，来获取该参数的取值。不指定该参数时，表示所有型号的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x1193775199}

[[加载]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x1017016106}[软件包列表中记录了加载软件包存储的位置、]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的型号、加载启动软件包的名称。当]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备需要使用加载软件包启动时，就会根据该列表去当前主用主控板加载这些软件包。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x790490672}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_x141423602}[查看所有]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备在所有主控板上的加载]{style="font-family:宋体"}[软件包列表。]{style="font-family:宋体"}

[[\<Sysname\> display boot-loader pex]{lang="EN-US"}]{#struct_0_x2076_x8851_x141751282}

[Startup software image files for PEXs to load from the parent device: ]{lang="EN-US"}

[PEX model: PEX-S5120HI]{lang="EN-US"}

[  flash:/rpu-s5120hi-boot.bin]{lang="EN-US"}

[  flash:/rpu-s5120hi-system.bin]{lang="EN-US"}

[ ]{lang="EN-US"}

[PEX model: PEX-S5820]{lang="EN-US"}

[  flash:/boot.bin]{lang="EN-US"}

[  flash:/system.bin]{lang="EN-US"}
:::

::::: {#1312183348 .myid}
[]{#_Toc404782602}[]{#struct_0_x2076_x8851_990275738}

**软件升级 \-- 软件升级配置命令 \-- firmware update**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](软件升级命令.files/image001.png){#图片 12 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_x8851_x1976918166}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x2076_x8851_x1354911659}
:::

[ ]{lang="EN-US"}

[**[firmware update]{lang="EN-US"}**]{#struct_0_x2076_x8851_x817620723}[命令用来升级]{style="font-family:宋体"}[CPLD]{lang="EN-US"}[、]{style="font-family:宋体"}[FPGA]{lang="EN-US"}[等固件。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x648621347}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x148841163}

[**[firmware update]{lang="EN-US"}**[ \[ **subslot** *subslot-number* \] { **cpld** *cpld-number* \| **cpu** *cpu-number* \| **fpga** *fpga-number* \| **module** *module-number* } **file** *filename*]{lang="EN-US"}]{#struct_0_x2076_x8851_845383275}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2076_x8851_2130728561}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[firmware update slot]{lang="EN-US"}**[ *slot-number* \[ **subslot** *subslot-number* \] { **cpld** *cpld-number* \| **cpu** *cpu-number* \| **fpga** *fpga-number* \| **module** *module-number* } **file** *filename*]{lang="EN-US"}]{#struct_0_x2076_x8851_x2093961895}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_x8851_x2105156299}[模式：]{style="font-family:宋体"}

[**[firmware update chassis ]{lang="EN-US"}***[chass-number]{lang="EN-US"}*[ **slot** *slot-number* \[ **subslot** *subslot-number* \] { **cpld** *cpld-number* \| **cpu** *cpu-number* \| **fpga** *fpga-number* \| **module** *module-number* } **file** *filename*]{lang="EN-US"}]{#struct_0_x2076_x8851_x90780597}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_1280915690}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2076_x8851_1476509019}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_233495861}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_x8851_1401138216}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_684902564}

[**[chassis ]{lang="EN-US"}***[chass-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x2076_x8851_1590544508}[：]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chass-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x2076_x8851_1083378678}[：]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x2076_x8851_x1722819275}[：表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x2076_x8851_1274367810}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x2076_x8851_x1222782276}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[subslot]{lang="EN-US"}**[ *subslot-number*]{lang="EN-US"}]{#struct_0_x2076_x8851_x469795790}[：子卡所在的子槽位号。不指定该参数时，表示单板上的所有子卡。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[cpld]{lang="EN-US"}**[ *cpld-number*]{lang="EN-US"}]{#struct_0_x2076_x8851_x1473288073}[：表示需要升级]{style="font-family:宋体"}[CPLD]{lang="EN-US"}[（]{style="font-family:宋体"}[Complex Programmable Logical Device ]{lang="EN-US"}[复杂可编程逻辑器件），]{style="font-family:宋体"}*[cpld-number]{lang="EN-US"}*[表示固件的编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[fpga]{lang="EN-US"}**[ *fpga-number*]{lang="EN-US"}]{#struct_0_x2076_x8851_615832885}[：表示需要升级]{style="font-family:宋体"}[FPGA]{lang="EN-US"}[（]{style="font-family:宋体"}[Field Programmable Gate Array ]{lang="EN-US"}[现场可编程门阵列），]{style="font-family:宋体"}*[fpga-number]{lang="EN-US"}*[表示固件的编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x2076_x8851_x1022710844}[：表示需要升级]{style="font-family:宋体"}[CPU]{lang="EN-US"}[，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[module]{lang="EN-US"}**[ *module-number*]{lang="EN-US"}]{#struct_0_x2076_x8851_237959736}[：表示需要升级指定模块（如]{style="font-family:宋体"}[3G Modem]{lang="EN-US"}[模块等），]{style="font-family:宋体"}*[module-number]{lang="EN-US"}*[表示模块的编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[file]{lang="EN-US"}**[ *filename*]{lang="EN-US"}]{#struct_0_x2076_x8851_525037490}[：升级文件的名称。不同固件升级文件的后缀可能不同，文件名从]{style="font-family:宋体"}[flash]{lang="EN-US"}[、]{style="font-family:宋体"}[cf]{lang="EN-US"}[、]{style="font-family:宋体"}[usb]{lang="EN-US"}[开始最多可输入]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x1340482251}

[[固件升级后需要对其所在的板卡进行下电后重新上电才能生效，对板卡下电的方式有：切断外部电源、插拔板卡、使用]{style="font-family:宋体"}**[power-supply off]{lang="EN-US"}**]{#struct_0_x2076_x8851_1305224085}[和]{style="font-family:宋体"}**[power-supply]{lang="EN-US"}**[ **on**]{lang="EN-US"}[命令等方式，请根据板卡的实际支持情况，选择下电方式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x1552288112}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_334645588}[升级]{style="font-family:宋体"}[1]{lang="EN-US"}[号]{style="font-family:宋体"}[CPLD]{lang="EN-US"}[。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> firmware update cpld 1 file package.bin]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x2076_x8851_998169909}

[[Updating firmware for CPLD on the specified card or subcard. Continue?\[Y/N\]:y]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x2076_x8851_1174430866}

[[Updating the firmware...]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x2076_x8851_x1293929343}

[[Please power cycle the card or subcard to activate the firmware.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x2076_x8851_x958145227}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_732211965}[升级位于]{style="font-family:宋体"}[1]{lang="EN-US"}[号槽位的]{style="font-family:宋体"}[1]{lang="EN-US"}[号]{style="font-family:宋体"}[CPLD]{lang="EN-US"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> firmware update slot 1 cpld 1 file package.bin]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x2076_x8851_1784951723}

[[Updating firmware for CPLD on the specified card or subcard. Continue?\[Y/N\]:y]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x2076_x8851_x1246827801}

[[Updating the firmware...]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x2076_x8851_250628334}

[[Please power cycle the card or subcard to activate the firmware.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x2076_x8851_1380506933}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_x666411004}[升级位于成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上的]{style="font-family:宋体"}[1]{lang="EN-US"}[号]{style="font-family:宋体"}[CPLD]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> firmware update slot 1 cpld 1 file package.bin]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x2076_x8851_1709282782}

[[Updating firmware for CPLD on the specified card or subcard. Continue?\[Y/N\]:y]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x2076_x8851_1430600429}

[[Updating the firmware...]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x2076_x8851_x573500201}

[[Please power cycle the card or subcard to activate the firmware.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x2076_x8851_x575808203}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_761880106}[升级位于成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上]{style="font-family:宋体"}[1]{lang="EN-US"}[号槽位的]{style="font-family:
宋体"}[1]{lang="EN-US"}[号]{style="font-family:宋体"}[CPLD]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> firmware update chassis 1 slot 1 cpld 1 file package.bin]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x2076_x8851_x1000310771}

[[Updating firmware for CPLD on the specified card or subcard. Continue?\[Y/N\]:y]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x2076_x8851_x1714925104}

[[Updating the firmware...]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x2076_x8851_x45018919}

[[Please power cycle the card or subcard to activate the firmware.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x2076_x8851_x146070980}
:::::

::::: {#-1952982264 .myid}
[]{#_Toc404782603}[]{#struct_0_x2076_x8851_1875920698}

**软件升级 \-- 软件升级配置命令 \-- reset boot-loader blade**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](软件升级命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_x8851_x1425198103}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x2076_x8851_1876117306}
:::

[ ]{lang="EN-US"}

[**[reset boot-loader blade]{lang="EN-US"}**]{#struct_0_x2076_x8851_402095087}[命令用来清除安全引擎的加载软件包配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_1928207761}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2076_x8851_x677855351}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[**[reset boot-loader blade ]{lang="EN-US"}***[blade-model]{lang="EN-US"}*]{#struct_0_x2076_x8851_x2046926640}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_175148769}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2076_x8851_1876051770}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_1964818545}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_x8851_x2116833808}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x947037409}

[*[blade-model]{lang="EN-US"}*]{#struct_0_x2076_x8851_x754464413}[：设备支持的安全引擎的型号，该参数必须完整输入，不区分大小写。可输入]{style="font-family:宋体"}**[reset boot-loader blade ]{lang="EN-US"}[？]{style="font-family:宋体"}**[，来获取该参数的取值。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x247134453}

[[请在设备启动完成、稳定运行后再配置该命令。]{style="font-family:宋体"}]{#struct_0_x2076_x8851_1541684828}

[[执行该命令后，设备会清空对应的加载软件包列表，不会将加载软件包从设备上删除。]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x405442267}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x283113422}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_1875658554}[清除指定型号为]{style="font-family:宋体"}[Blade-m9k]{lang="EN-US"}[的安全引擎的加载软件包配置。]{style="font-family:宋体"}

[[\<Sysname\> reset boot-loader blade Blade-m9k]{lang="EN-US"}]{#struct_0_x2076_x8851_x205680664}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_1761341862}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[boot-loader blade file]{lang="EN-US"}**]{#struct_0_x2076_x8851_x55392117}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display boot-loader blade]{lang="EN-US"}**]{#struct_0_x2076_x8851_1875855162}
:::::

::::: {#-847967977 .myid}
[]{#_Toc404782604}[]{#struct_0_x2076_x8851_x1017540138}

**软件升级 \-- 软件升级配置命令 \-- reset boot-loader pex**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](软件升级命令.files/image001.png){#图片 4 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_x8851_x1214375477}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x2076_x8851_1875789626}
:::

[ ]{lang="EN-US"}

[**[reset boot-loader pex]{lang="EN-US"}**]{#struct_0_x2076_x8851_1876510522}[命令用来清除]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的加载软件包配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_25179234}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2076_x8851_1567135533}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[**[reset boot-loader pex]{lang="EN-US"}**[ *pex-model*]{lang="EN-US"}]{#struct_0_x2076_x8851_1876444986}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_43321079}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2076_x8851_1543415529}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_1875986237}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_x8851_1319694209}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_982243151}

[*[pex-model]{lang="EN-US"}*]{#struct_0_x2076_x8851_x55655010}[：设备支持的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的型号，该参数必须完整输入，不区分大小写。可输入]{style="font-family:宋体"}**[boot-loader pex ]{lang="EN-US"}[？]{style="font-family:宋体"}**[，回车，来获取该参数的取值。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_1875920701}

[[请在设备启动完成、稳定运行后再配置该命令。]{style="font-family:宋体"}]{#struct_0_x2076_x8851_530527200}

[[执行该命令后，设备会清空对应的加载软件包列表，不会将加载软件包从设备上删除。]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x742184462}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x258195876}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_x2091799814}[清除指定型号为]{style="font-family:宋体"}[PEX-S5820V2]{lang="EN-US"}[的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的加载软件包配置。]{style="font-family:宋体"}

[[\<Sysname\> reset boot-loader pex PEX-S5820V2]{lang="EN-US"}]{#struct_0_x2076_x8851_1876117309}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_402815983}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[boot-loader pex file]{lang="EN-US"}**]{#struct_0_x2076_x8851_883505136}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
line-height:125%;font-family:Symbol"}**[display boot-loader pex]{lang="EN-US"}**]{#struct_0_x2076_x8851_1897642507}
:::::

::::: {#158683708 .myid}
[]{#_Toc404782605}[]{#struct_0_x2076_x8851_669733255}[]{#_Toc329856491}[]{#_Toc366671106}[]{#_Toc366671107}[]{#_Toc366671108}[]{#_Toc366671109}[]{#_Toc366671110}[]{#_Toc366671111}[]{#_Toc366671112}[]{#_Toc366671113}[]{#_Toc366671114}[]{#_Toc366671115}[]{#_Toc366671116}[]{#_Toc366671117}[]{#_Toc366671118}[]{#_Toc366671119}[]{#_Toc366671120}[]{#_Toc366671121}[]{#_Toc366671122}[]{#_Toc366671123}[]{#_Toc366671124}[]{#_Toc366671125}[]{#_Toc366671126}[]{#_Toc366671127}[]{#_Toc366671128}[]{#_Toc366671129}[]{#_Toc366671130}[]{#_Toc366671131}[]{#_Toc366671132}[]{#_Toc366671133}[]{#_Toc366671134}[]{#_Toc366671135}[]{#_Toc366671136}[]{#_Toc366671137}[]{#_Toc366671138}[]{#_Toc366671139}[]{#_Toc366671140}[]{#_Toc366671141}[]{#_Toc366671142}[]{#_Toc366671143}[]{#_Toc366671144}[]{#_Toc366671145}[]{#_Toc366671146}[]{#_Toc366671147}[]{#_Toc366671148}[]{#_Toc366671149}

**软件升级 \-- 软件升级配置命令 \-- version auto-update enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](软件升级命令.files/image002.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_x2076_x8851_209080659}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[该命令只在分布式设备－独立运行模式下支持。]{style="font-family:楷体_GB2312"}]{#struct_0_x2076_x8851_1751397475}
:::

**[ ]{lang="EN-US"}**

[**[version auto-update enable]{lang="EN-US"}**]{#struct_0_x2076_x8851_1958999287}[命令用来使能备用主控板自动加载主用主控板当前启动软件包的功能。]{style="font-family:宋体;color:black"}

[**[undo version auto-update enable]{lang="EN-US"}**]{#struct_0_x2076_x8851_x854371281}[命令用来[取消备用主控板自动加载主用主控板启动软件的功能。]{style="color:black"}]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x1890812523}

[**[version auto-update enable]{lang="EN-US"}**]{#struct_0_x2076_x8851_x1765230779}

[**[undo version auto-update enable]{lang="EN-US"}**]{#struct_0_x2076_x8851_1779648077}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_1094553575}

[[当启动过程中，当[备用主控板发现自己版本和主用主控板版本不一致时，会自动加载主用主控板的当前启动软件包]{style="color:black"}。]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x1245382092}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_1653867468}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x327748655}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x375282096}

[[network-admin]{lang="EN-US" style="font-size:10.0pt"}]{#struct_0_x2076_x8851_2024467210}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_878555977}

[[配置]{style="font-family:宋体;color:black"}**[undo version check ignore]{lang="EN-US"}**]{#struct_0_x2076_x8851_x437559177}[和]{style="font-family:
宋体"}**[version auto-update enable]{lang="EN-US"}**[命令后，在设备启动过程中，当[备用主控板发现自己当前启动软件包版本和主用主控板的当前启动软件包版本不一致时，会自动拷贝主用主控板的当前启动软件包列表中的所有软件包，设置为自己的主用下次启动软件包，并自动重启。这样，能够使得备用主控板启动后，和主用主控板启动软件包的版本一致。]{style="color:black"}]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x1765296315}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_418695399}[使能备用主控板自动加载主用主控板当前启动软件包的功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_x8851_668789890}

[\[Sysname\] version auto-update enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_1984083484}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[version check ignore]{lang="EN-US"}**]{#struct_0_x2076_x8851_883360463}
:::::

::::: {#-2041729362 .myid}
[]{#_Toc404782606}[]{#struct_0_x2076_x8851_83319801}[]{#_Toc329856490}

**软件升级 \-- 软件升级配置命令 \-- version check ignore**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](软件升级命令.files/image002.png){#图片 11 width="63" height="25"}]{lang="EN-US"}]{#struct_0_x2076_x8851_x1492122066}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[该命令只在分布式设备－独立运行模式下支持。]{style="font-family:楷体_GB2312"}]{#struct_0_x2076_x8851_x1914703931}
:::

**[ ]{lang="EN-US"}**

[**[version check ignore]{lang="EN-US"}**]{#struct_0_x2076_x8851_756390520}[命令用来忽略对备用主控板进行启动软件包版本一致性检查，即不检查备用主控板的版本是否与主用主控板的启动软件包版本一致。]{style="font-family:宋体;color:black"}

[**[undo version check ignore]{lang="EN-US"}**]{#struct_0_x2076_x8851_x461864395}[命令用来使能对备用主控板进行启动软件包版本一致性检查。]{style="font-family:宋体;color:black"}

[[需要注意的是，系统运行时，如果备用主控板的启动软件包版本和主用主控板的启动软件包版本不一致，可能会造成系统故障。]{style="font-family:宋体;color:black"}]{#struct_0_x2076_x8851_x1764837563}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_14418446}

[**[version check ignore]{lang="EN-US"}**]{#struct_0_x2076_x8851_850092453}

[**[undo version check ignore]{lang="EN-US"}**]{#struct_0_x2076_x8851_x1434906360}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x1776370688}

[[备用主控板启动软件包版本一致性检查功能处于使能状态。]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x2130728882}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x1669234814}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_x8851_477539330}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_1377670271}

[[network-admin]{lang="EN-US" style="font-size:10.0pt"}]{#struct_0_x2076_x8851_x1764903099}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_1774005880}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果[忽略对备用主控板进行]{style="color:black"}启动软件包[版本一致性检查]{style="color:black"}，当备用主控板和主用主控板启动软件包版本不一致时，备用主控板仍然使用不一致的版本启动，可能会造成设备功能问题。]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x2123525425}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果[使能对备用主控板进行]{style="color:black"}启动软件包[版本一致性检查]{style="color:black"}，当备用主控板和主用主控板启动软件包版本不一致时，备用主控板会停留在启动阶段，不能正常启动。]{style="font-family:宋体"}]{#struct_0_x2076_x8851_1090402570}

[[建议用户不要忽略启动软件包版本一致性检查。]{style="font-family:宋体"}]{#struct_0_x2076_x8851_x571052304}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x590681392}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_x8851_2021175764}[使能对备用主控板进行版本一致性检查。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_x8851_1918224679}

[\[Sysname\] undo version check ignore]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_x8851_x665856044}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[version auto-update enable]{lang="EN-US"}**]{#struct_0_x2076_x8851_x1300767387}
:::::
