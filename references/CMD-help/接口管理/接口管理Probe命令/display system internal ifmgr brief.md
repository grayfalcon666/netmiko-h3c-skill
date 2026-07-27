<!-- CMD-INDEX
  display system internal ifmgr brief | ]                | L14
  display system internal ifmgr down  | Probe视图          | L58
  display system internal ifmgr entry | Probe视图          | L102
  display system internal ifmgr event | Probe视图          | L150
  display system internal ifmgr hotplug | Probe视图          | L198
  display system internal ifmgr index | Probe视图          | L246
  display system internal ifmgr list  | Probe视图          | L294
  display system internal ifmgr mdc   | Probe视图          | L348
  display system internal ifmgr name  | Probe视图          | L396
  display system internal ifmgr type  | Probe视图          | L444
-->

**接口管理 \-- 接口管理Probe命令 \-- display system internal ifmgr brief**

------------------------------------------------------------------------

**[display system internal ifmgr**]**brief**命令用来显示接口基本信息同步的信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display**]**system****internal****ifmgr****brief ***[ para***slot***slot-number*[ **cpu** *cpu-number*  \| **help** }]

分布式设备－]IRF模式：

**[display system internal ifmgr**]**brief*****[para***chassis***chassis-number***slot***slot-number*[ **cpu** *cpu-number*  \| **help** }]

【视图】]

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[para*]：指定显示时的参数，为接口索引值。

**[slot**]* slot-number*：表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]*slot-number*：表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]*slot-number*：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number ***slot***slot-number*：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**]*chassis-number ***slot***slot-number*：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[help**]：显示命令参数的帮助信息，用于指导用户输入合法参数。

**接口管理 \-- 接口管理Probe命令 \-- display system internal ifmgr down**

------------------------------------------------------------------------

**[display system internal ifmgr down**]命令用来显示已注册的down类型。

【命令】

集中式设备：

**[display system internal ifmgr down**]

分布式设备－独立运行模式/集中式IRF设备：

**[display**]**system****internal****ifmgr****down** \**[slot***slot-number* **cpu** *cpu-number* ]

分布式设备－IRF模式：

**[display system internal ifmgr**]**down** \**[chassis***chassis-number***slot***slot-number* **cpu** *cpu-number* ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot**]* slot-number*：表示单板所在的槽位号。不指定该参数时，则表示主用主控板。（分布式设备－独立运行模式）

**[slot**]*slot-number*：表示设备在IRF中的成员编号。不指定该参数时，则表示主设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]*slot-number*：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，则表示主设备。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number ***slot*** slot-number*：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，则表示IRF中的全局主用主控板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**]*chassis-number ***slot***slot-number*：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定该参数时，则表示IRF中的全局主用主控板。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**接口管理 \-- 接口管理Probe命令 \-- display system internal ifmgr entry**

------------------------------------------------------------------------

**[display system internal ifmgr**]**entry**命令用来显示指定接口的数据结构信息。

【命令】

集中式设备：

**[display system internal ifmgr entry**]***[para *[\| **help** }]

分布式设备－独立运行模式]/集中式IRF设备：

**[display**]**system****internal****ifmgr****entry ***[ para* \**[slot***slot-number* **cpu** *cpu-number* ]  \| **help** }]

分布式设备－IRF模式：

**[display system internal ifmgr**]**entry ***[ para* \**[chassis***chassis-number***slot***slot-number* **cpu** *cpu-number* ]  \| **help** }]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[para*]：指定显示时的参数。表示接口名或接口索引，格式为：1\*接口索引，2\*接口名。

**[slot**]* slot-number*：表示单板所在的槽位号。不指定该参数时，则表示主用主控板。（分布式设备－独立运行模式）

**[slot**]*slot-number*：表示设备在IRF中的成员编号。不指定该参数时，则表示主设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]*slot-number*：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，则表示主设备。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number ***slot*** slot-number*：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，则表示IRF中的全局主用主控板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**]*chassis-number ***slot***slot-number*：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定该参数时，则表示IRF中的全局主用主控板。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[help**]：显示命令参数的帮助信息，用于指导用户输入合法参数。

**接口管理 \-- 接口管理Probe命令 \-- display system internal ifmgr event**

------------------------------------------------------------------------

**[display system internal ifmgr event**]命令用来显示接口事件的注册信息，包括哪些模块注册了该事件，以及模块在哪些接口上注册了该事件。

【命令】

集中式设备：

**[display system internal ifmgr event***para *[\| **help** }]

分布式设备－独立运行模式]/集中式IRF设备：

**[display**]**system****internal****ifmgr****event** *[para* \**[slot***slot-number* **cpu** *cpu-number* ]  \| **help** }]

分布式设备－IRF模式：

**[display system internal ifmgr**]**event** *[para* \**[chassis***chassis-number***slot***slot-number* **cpu** *cpu-number* ]  \| **help** }]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[para*]：指定显示时的参数。*para*为事件或接口类型，如果同时指定事件和接口类型，事件和接口中间需用"\*"连接，格式为：*event*\**type*。

**[slot**]*slot-number*：表示单板所在的槽位号。不指定该参数时，则表示主用主控板。（分布式设备－独立运行模式）

**[slot**]*slot-number*：表示设备在IRF中的成员编号。不指定该参数时，则表示主设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]*slot-number*：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，则表示主设备。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number ***slot*** slot-number*：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，则表示IRF中的全局主用主控板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**]*chassis-number ***slot***slot-number*：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定该参数时，则表示IRF中的全局主用主控板。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[help**]：显示命令参数的帮助信息，用于指导用户输入合法参数。

**接口管理 \-- 接口管理Probe命令 \-- display system internal ifmgr hotplug**

------------------------------------------------------------------------

**[display system internal ifmgr**]**hotplug**命令用来显示板或子卡的热插拔信息。

【命令】

集中式设备：

**[display system internal ifmgr**]**hotplug **\*[para *[\| **help** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display**]**system****internal****ifmgr****hotplug** [ \*[para * \**slot***slot-number* **cpu** *cpu-number* ]  \| **help** ]

分布式设备－IRF模式：

**[display system internal ifmgr**]**hotplug** [ \*[para * \**chassis***chassis-number***slot***slot-number* **cpu** *cpu-number* ]  \| **help** ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[para*]：指定显示时的参数。*para*为槽位号或者槽位号和子槽位号（格式为*slot-number\*subslot-number*），用于显示该板或子卡的热插拔信息。不指定该参数以及**help**参数时，显示所有板的热插拔信息；

**[slot**]* slot-number*：表示单板所在的槽位号。不指定该参数时，则表示主用主控板。用于显示*slot-number*单板上记录的热插拔信息。（分布式设备－独立运行模式）

**[slot**]*slot-number*：表示设备在IRF中的成员编号。不指定该参数时，则表示主设备。用于显示*slot-number*成员设备上记录的热插拔信息。（集中式IRF设备）。（不支持IRF3的设备）

**[slot**]*slot-number*：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，则表示主设备。用于显示*slot-number*成员设备/PEX上记录的热插拔信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number ***slot*** slot-number*：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，则表示IRF中的全局主用主控板。用于显示*slot-number*单板上记录的热插拔信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**]*chassis-number ***slot***slot-number*：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定该参数时，则表示IRF中的全局主用主控板。用于显示*slot-number*单板/PEX上记录的热插拔信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[help**]：显示命令参数的帮助信息，用于指导用户输入合法参数。

**接口管理 \-- 接口管理Probe命令 \-- display system internal ifmgr index**

------------------------------------------------------------------------

**[display system internal ifmgr index**]命令用来显示接口索引节点的相关信息。

【命令】

集中式设备：

**[display system internal ifmgr index***para *[\| **help** }]

分布式设备－独立运行模式]/集中式IRF设备：

**[display**]**system****internal****ifmgr****index** *[para* \**[slot***slot-number* **cpu** *cpu-number* ]  \| **help** }]

分布式设备－IRF模式：

**[display system internal ifmgr**]**index** *[para* \**[chassis***chassis-number***slot***slot-number* **cpu** *cpu-number* ]  \| **help** }]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[para*]：指定显示时的参数。为接口索引值的十进制形式。

**[slot**]* slot-number*：表示单板所在的槽位号。不指定该参数时，则表示主用主控板。（分布式设备－独立运行模式）

**[slot**]*slot-number*：表示设备在IRF中的成员编号。不指定该参数时，则表示主设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]*slot-number*：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，则表示主设备。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number ***slot*** slot-number*：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，则表示IRF中的全局主用主控板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**]*chassis-number ***slot***slot-number*：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定该参数时，则表示IRF中的全局主用主控板。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[help**]：显示命令参数的帮助信息，用于指导用户输入合法参数。

**接口管理 \-- 接口管理Probe命令 \-- display system internal ifmgr list**

------------------------------------------------------------------------

**[display system internal ifmgr list**]命令用来显示接口树信息。

【命令】

集中式设备：

**[display system internal ifmgr**]**list** \*[para*[ \| **help** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display**]**system****internal****ifmgr****list** [ \*[para * \**slot***slot-number* **cpu** *cpu-number* ]  \| **help** ]

分布式设备－IRF模式：

**[display system internal ifmgr**]**list** [ \*[para * \**chassis***chassis-number***slot***slot-number* **cpu** *cpu-number* ]  \| **help** ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[para*]：指定显示时的参数。*para*为接口类型对应的数值，该数值可通过**help**参数获取。

**[slot**]*slot-number*：表示单板所在的槽位号。不指定该参数时，则表示主用主控板。（分布式设备－独立运行模式）

**[slot**]*slot-number*：表示设备在IRF中的成员编号。不指定该参数时，则表示主设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]*slot-number*：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，则表示主设备。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number ***slot*** slot-number*：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，则表示IRF中的全局主用主控板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**]*chassis-number ***slot***slot-number*：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定该参数时，则表示IRF中的全局主用主控板。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[help**]：显示命令参数的帮助信息，用于指导用户输入合法参数。

【使用指导】

接口树用于管理设备上存在的接口。树上的节点对应接口，子节点对应接口下创建的子接口，每个节点的信息包括接口的名称和索引。

不指定*para*和**help**参数时，显示所有类型接口的接口树信息。

**接口管理 \-- 接口管理Probe命令 \-- display system internal ifmgr mdc**

------------------------------------------------------------------------

**[display system internal ifmgr mdc**]命令用来显示MDC接口分配相关信息。

【命令】

集中式设备：

**[display system internal ifmgr mdc***para *[\| **help** }]

分布式设备－独立运行模式]/集中式IRF设备：

**[display**]**system****internal****ifmgr****mdc** *[para* \**[slot***slot-number* **cpu** *cpu-number* ]  \| **help** }]

分布式设备－IRF模式：

**[display system internal ifmgr**]**mdc** *[para* \**[chassis***chassis-number***slot***slot-number* **cpu** *cpu-number* ]  \| **help** }]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[para*]：指定显示时的参数。合法参数形式有如下四种：1\**接口所在分组的编号*、2\**接口名*、3\**MDC的编号*、4\**槽位号*。

**[slot**]* slot-number*：表示单板所在的槽位号。不指定该参数时，则表示主用主控板。（分布式设备－独立运行模式）

**[slot**]*slot-number*：表示设备在IRF中的成员编号。不指定该参数时，则表示主设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]*slot-number*：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，则表示主设备。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number ***slot*** slot-number*：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，则表示IRF中的全局主用主控板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**]*chassis-number ***slot***slot-number*：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定该参数时，则表示IRF中的全局主用主控板。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[help**]：显示命令参数的帮助信息，用于指导用户输入合法参数。

**接口管理 \-- 接口管理Probe命令 \-- display system internal ifmgr name**

------------------------------------------------------------------------

**[display system internal ifmgr name**]命令用来显示接口名字解析树信息。该树用于解析接口名字，以及命令行上输入接口名字时的帮助检查。

【命令】

集中式设备：

**[display system internal ifmgr name***para *[\| ]**help** }

分布式设备－独立运行模式]/集中式IRF设备：

**[display**]**system****internal****ifmgr****name** *[ para* \**[slot***slot-number* **cpu** *cpu-number* ]  \| ]**help** }

分布式设备－IRF模式：

**[display system internal ifmgr**]**name*****[para* \**[chassis***chassis-number***slot***slot-number* **cpu** *cpu-number* ]  \| ]**help** }

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[para*]：指定显示时的参数，为接口全名或简名。

**[slot**]* slot-number*：表示单板所在的槽位号。不指定该参数时，则表示主用主控板。（分布式设备－独立运行模式）

**[slot**]*slot-number*：表示设备在IRF中的成员编号。不指定该参数时，则表示主设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]*slot-number*：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，则表示主设备。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number ***slot*** slot-number*：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，则表示IRF中的全局主用主控板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**]*chassis-number ***slot***slot-number*：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定该参数时，则表示IRF中的全局主用主控板。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[help**]：显示命令参数的帮助信息，用于指导用户输入合法参数。

**接口管理 \-- 接口管理Probe命令 \-- display system internal ifmgr type**

------------------------------------------------------------------------

**[display system internal ifmgr type**]命令用来按类型显示接口的信息。

【命令】

集中式设备：

**[display system internal ifmgr type***para *[\| ]**help** }

分布式设备－独立运行模式]/集中式IRF设备：

**[display**]**system****internal****ifmgr****type** *[para* \**[slot***slot-number* **cpu** *cpu-number* ]  \| ]**help** }

分布式设备－IRF模式：

**[display system internal ifmgr**]**type** *[para* \**[chassis***chassis-number***slot***slot-number* **cpu** *cpu-number* ]  \| ]**help** }

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[para*]：指定显示时的参数。*para*为接口类型，为1～127个字符的字符串。

**[slot**]* slot-number*：表示单板所在的槽位号。不指定该参数时，则表示主用主控板。（分布式设备－独立运行模式）

**[slot**]*slot-number*：表示设备在IRF中的成员编号。不指定该参数时，则表示主设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]*slot-number*：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，则表示主设备。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number***slot*** slot-number*：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，则表示IRF中的全局主用主控板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**]*chassis-number ***slot***slot-number*：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定该参数时，则表示IRF中的全局主用主控板。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[help**]：显示命令参数的帮助信息，用于指导用户输入合法参数。

