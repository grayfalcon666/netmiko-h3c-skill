<!-- CMD-INDEX
  view                                | Probe视图          | L7
  list                                | Probe视图          | L55
  probe                               | 系统视图             | L99
-->

**Probe基础配置 \-- Probe基础配置命令 \-- view**

------------------------------------------------------------------------

view命令用来查看系统目录（/proc/、/sys/、/var/）下的文件的内容。

【命令】

集中式设备：

**[view ***file-path*]

分布式设备－独立运行模式/集中式IRF设备：

**[view ***file-path * **slot** *slot-number* ]

分布式设备－IRF模式：

**[view ***file-path * **chassis** *chassis-number* **slot** *slot-number* ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[file-path*]：要查看文件的路径，区分大小写。

**[slot **]*slot-number*：查看指定单板系统目录（/proc/、/sys/、/var/）下的文件的内容。*slot-number*表示单板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot **]*slot-number*：查看指定设备系统目录（/proc/、/sys/、/var/）下的文件的内容。*slot-number*表示设备在IRF中的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot **]*slot-number*：查看指定设备/PEX系统目录（/proc/、/sys/、/var/）下的文件的内容。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，表示主设备。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number*** slot***slot-number*：查看指定设备上单板系统目录（/proc/、/sys/、/var/）下的文件的内容。*chassis-numbe*r表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，表示主用主用主控板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**]*chassis-number*** slot***slot-number*：查看单板/PEX系统目录（/proc/、/sys/、/var/）下的文件的内容。*chassis-numbe*r表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定该参数时，表示主用主用主控板。（分布式设备－IRF模式）（支持IRF3的设备）

【使用指导】

执行该命令显示的文件路径中不能包含文件链接。文件链接类似于文件的快捷方式，文件链接指向另一个文件或目录。通过文件链接可以访问到其所指向的文件或目录。

**Probe基础配置 \-- Probe基础配置命令 \-- list**

------------------------------------------------------------------------

**[list**]命令用来查看系统目录（/proc/、/sys/、/var/）下的文件和子目录的相关信息，且文件路径中不能包含文件链接。

【命令】

集中式设备：

**[list ***file-path*]

分布式设备－独立运行模式/集中式IRF设备：

**[list ***file-path * **slot** *slot-number* ]

分布式设备－IRF模式：

**[list ***file-path * **chassis** *chassis-number* **slot** *slot-number* ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[file-path*]：要查看的文件或目录的路径，区分大小写。

**[slot **]*slot-number*：查看指定单板系统目录（/proc/、/sys/、/var/）下的文件和子目录的相关信息。*slot-number*表示单板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot **]*slot-number*：查看指定设备系统目录（/proc/、/sys/、/var/）下的文件和子目录的相关信息。*slot-number*表示设备在IRF中的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot **]*slot-number*：查看指定设备/PEX系统目录（/proc/、/sys/、/var/）下的文件和子目录的相关信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，表示主设备。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number*** slot***slot-number*：查看指定设备上单板系统目录（/proc/、/sys/、/var/）下的文件和子目录的相关信息。*chassis-numbe*r表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**]*chassis-number*** slot***slot-number*：查看单板/PEX系统目录（/proc/、/sys/、/var/）下的文件和子目录的相关信息。*chassis-numbe*r表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）（支持IRF3的设备）

**Probe基础配置 \-- Probe基础配置命令 \-- probe**

------------------------------------------------------------------------

**[probe**]命令用来从系统视图进入Probe视图。

【命令】

**[probe**]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在Probe视图下，用户可以通过命令查看系统的状态和信息，以便对系统故障进行诊断。

