
**CLI \-- CLI命令 \-- alias**

------------------------------------------------------------------------

**[alias**]命令用来给指定的命令或命令字符串配置别名。

**[undo alias**]命令用来取消相应配置。

【命令】

**[alias ***alias command*]

**[undo alias** *alias*]

【缺省情况】

系统为部分常用命令定义了缺省别名，如 表1-1(?1613693525#_Ref396407562)所示。系统定义的缺省别名无法取消。

表1-1 系统定义的缺省别名

缺省别名

命令

**[access-list**]

**[acl**]

**[end**]

**[return**]

**[erase**]

**[delete**]

**[exit**]

**[quit**]

**[hostname**]

**[sysname**]

**[logging**]

**[info-center**]

**[no**]

**[undo**]

**[show**]

**[display**]

**[write**]

**[save**]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[alias*]：表示命令的别名，为1～20个字符的字符串，区分大小写。别名不能是alias也不能包含空格。

*[command*]：表示配置别名的命令，可以为任意字符串。请用户自行保证该命令字符串能够被设备识别并执行，否则执行别名命令时将会失败。

【使用指导】

本命令通常可以在如下情况使用：

·本命令可以为某条命令行配置别名，当执行该命令时可以直接使用别名以简化输入。例如将命令**display ip routing-table**的别名配置为**shiprt**，当需要使用**display ip routing-table**查看设备当前生效的配置时，直接输入**shiprt**即可。

·本命令可以为命令行起始的一个或多个关键字配置别名，使其更符合用户习惯。所有使用该关键字开头的命令行都可以使用指定的别名命令来执行。例如，为**display ip**命令定义的别名为**ship**，在使用所有以**display ip**关键字开头的命令行时，都可以使用**ship**进行配置。例如：

¡输入**ship routing-table**可以执行命令**display ip routing-table**。

¡输入**ship interface**可以执行命令**display ip interface**。

·配置别名时，可以使用\$n表示命令行中的参数或者关键字，这样既可以用别名替代部分关键字来简化输入，又可以根据实际需要指定不同的参数或者关键字，增加了灵活性。\$n最多可以使用9次，n为1～9的整数，表示参数或关键字出现的顺序。比如，将命令**[display ip \$1 \| include \$2]**的别名配置为**shinc**后，如果需要执行**[display ip routing-table \| include Static]**命令来筛选并查看路由表中的所有静态路由信息，可直接执行**shinc** **routing-table Static**；同样如果需要执行**[display ip interface \| include GigabitEthernet0/0/1]**，则可直接执行**shinc interface GigabitEthernet0/0/1**。

【举例】

\# 配置命令**display ip routing-table**的别名为**shiprt**。

\<Sysname\> system-view

Sysname alias shiprt display ip routing-table

Sysname shiprt

Destinations : 12        Routes : 12

Destination/Mask   Proto   Pre Cost        NextHop         Interface

0.0.0.0/32         Direct  0   0           127.0.0.1       InLoop0

3.3.3.3/32         Static  60  0           192.168.1.62    GE0/0

127.0.0.0/8        Direct  0   0           127.0.0.1       InLoop0

127.0.0.0/32       Direct  0   0           127.0.0.1       InLoop0

127.0.0.1/32       Direct  0   0           127.0.0.1       InLoop0

127.255.255.255/32 Direct  0   0           127.0.0.1       InLoop0

169.254.0.0/24     Direct  0   0           169.254.0.188   GE0/0

169.254.0.0/32     Direct  0   0           169.254.0.188   GE0/0

169.254.0.188/32   Direct  0   0           127.0.0.1       InLoop0

169.254.0.255/32   Direct  0   0           169.254.0.188   GE0/0

192.168.57.0/24    RIP     100 1           192.168.1.62    GE0/0

224.0.0.0/4        Direct  0   0           0.0.0.0         NULL0

224.0.0.0/24       Direct  0   0           0.0.0.0         NULL0

255.255.255.255/32 Direct  0   0           127.0.0.1       InLoop0

\# 配置命令**[display ip \$1 \| include \$2]**的别名为**shinc**，同时使用别名命令筛选并查看路由表中的所有静态路由信息。

Sysname alias shinc display ip \$1 \| include \$2

Sysname shinc routing-table Static

3.3.3.3/32         Static  60  0           192.168.1.62    GE0/0

\# 使用别名命令**shinc**筛选并查看路由表中的所有RIP路由信息。

Sysname shinc routing-table RIP

192.168.57.0/24    RIP     100 1           192.168.1.62    GE0/0

【相关命令】

·**display alias**

**CLI \-- CLI命令 \-- display \| { begin \| exclude \| include }**

------------------------------------------------------------------------

[**[display \|]**[ { **begin** \| **exclude** \| **include** }]]命令用来使用正则表达式对显示信息进行过滤。

【命令】

**[display ***command*[ **\|** { **begin** \| **exclude** \| **include** } *regular-expression*]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[command*]：命令关键字，取值可以通过输入?来获得。

**[begin**]：从包含指定正则表达式的行开始显示。

**[exclude**]：只显示不包含指定正则表达式的行。

**[include**]：只显示包含指定正则表达式的行。

*[regular-expression*]：表示正则表达式，为1～256个字符的字符串，区分大小写。

【使用指导】

用**display**命令查看显示信息时，用户可以使用正则表达式来过滤显示信息，以便快速的找到自己关注的信息。关于正则表达式的详细描述请参考"基础配置指导"中的"CLI"。

【举例】

\# 查看包含VLAN的配置。

\<Sysname\> display current-configuration \| include vlan

vlan 1

vlan 999

 port access vlan 999

**CLI \-- CLI命令 \-- display \| by-linenum**

------------------------------------------------------------------------

[**[display \| by-linenum]**]命令用来查看带行号的显示信息。

【命令】

**[display ***command*[ **\|** **by-linenum**]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[command*]：命令关键字，取值可以通过输入?来获得。

【使用指导】

使用本命令时，系统在显示信息的同时会自动在每行显示信息的前面添加行号。以便当显示信息较多时，能够迅速定位到某行信息。

行号占5个字符，通常行号后面接":"。当**by-linenum**和**begin**参数一起使用时，行号后面还可能接"-"，其中":"表示该行符合匹配规则，"-"表示该行不符合匹配规则。

【举例】

\# 显示VLAN 999信息的同时显示行号。

\<Sysname\> display vlan 999 \| by-linenum

    1:  VLAN ID: 999

    2:  VLAN type: Static

    3:  Route interface: Configured

    4:  IP address: 192.168.2.1

    5:  Subnet mask: 255.255.255.0

    6:  Description: For LAN Access

    7:  Name: VLAN 0999

    8:  Tagged ports:   None

    9:  Untagged ports:

   10:     GigabitEthernet1/0/1

\# 查看当前配置，从包含"user-group"字符串的行开始到最后一行配置信息，并同时显示行号。（行号后为":"表示该行包含"user-group"字符串，行号后为"-"表示该行不包含"user-group"字符串。）

\<Sysname\> display current-configuration[ \| by-linenum begin user-group]

  114:  user-group system

  115-  \#

  116-  return

**CLI \-- CLI命令 \-- display \>**

------------------------------------------------------------------------

**[display** **\>**]命令用来将显示信息独立保存到指定文件。

【命令】

**[display** *command* **\>** *filename*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[command*]：命令关键字，取值可以通过输入?来获得。

*[filename*]：文件名称，为1～63个字符的字符串。

【使用指导】

**[display**]命令显示的内容通常是统计信息、功能是否使能以及功能的相关参数配置，这些信息在设备运行过程中会随着时间或者用户的配置而改变。使用本命令可以将当前显示信息保存到指定文件，可供用户随时比对和查看。

执行本命令时，如果*filename*不存在，系统会先创建该文件，再保存；如果*filename*已存在，则会覆盖原文件的内容。

【举例】

\# 将display vlan 1的显示信息保存到指定文件vlan.txt。

\<Sysname\> display vlan 1 \> vlan.txt

查看vlan.txt的内容，验证**display** **\>**命令的执行效果。

\<Sysname\> more vlan.txt

VLAN ID: 1

 VLAN type: Static

 Route interface: Not configured

 Description: VLAN 0001

 Name: VLAN 0001

 Tagged ports:   None

 Untagged ports:

    GigabitEthernet1/0/2

**CLI \-- CLI命令 \-- display \>\>**

------------------------------------------------------------------------

**[display** **\>\>**]命令用来将显示信息以追加方式保存到指定文件。

【命令】

**[display** *command* **\>\>** *filename*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[command*]：命令关键字，取值可以通过输入?来获得。

*[filename*]：文件名称，为1～63个字符的字符串。

【使用指导】

**[display**]命令显示的内容通常是统计信息、功能是否使能以及功能的相关参数配置，这些信息在设备运行过程中会随着时间或者用户的配置而改变。使用本命令可以将当前显示信息保存到指定文件，可供用户随时比对和查看。

执行本命令时，如果*filename*不存在，系统会先创建该文件，再保存。如果*filename*已存在，则新保存的内容会追加到文件*filename*的尾部。

【举例】

\# 将display vlan 999的显示信息以追加方式保存到指定文件vlan.txt。

\<Sysname\> display vlan 999 \>\> vlan.txt

查看vlan.txt的内容，验证**display \>\>**命令的执行效果。

\<Sysname\> more vlan.txt

VLAN ID: 1

 VLAN type: Static

 Route interface: Not configured

 Description: VLAN 0001

 Name: VLAN 0001

 Tagged ports:   None

 Untagged ports:

    GigabitEthernet1/0/2

 VLAN ID: 999

 VLAN type: Static

 Route interface: Configured

 IP address: 192.168.2.1

 Subnet mask: 255.255.255.0

 Description: For LAN Access

 Name: VLAN 0999

 Tagged ports:   None

 Untagged ports:

    GigabitEthernet1/0/1

**CLI \-- CLI命令 \-- display alias**

------------------------------------------------------------------------

**[display alias**]命令用来查看命令别名的相关配置。

【命令】

**[display alias **\*[alias* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[alias*]：表示配置的命令别名。不指定该参数，则显示所有的已配置的命令别名。

【举例】

\# 查看系统中配置的所有命令别名。

\<Sysname\> display alias

Index     Alias                Command key

1         access-list          acl

2         end                  return

3         erase                delete

4         exit                 quit

5         hostname             sysname

6         logging              info-center

7         no                   undo

[8         shinc                display \$1 \| include \$2]

9         show                 display

10        sirt                 display ip routing-table

11        write                save

\# 查看别名命令**shinc**表示的命令字符串。

\<Sysname\> display alias shinc

Alias                Command key

[shinc                display ip \$1 \| include \$2]

表1-2  display alias命令显示信息描述表

字段

描述

Index

索引号

Alias

别名

Command key

命令字符串

【相关命令】

·**alias**

**CLI \-- CLI命令 \-- display history-command**

------------------------------------------------------------------------

**[display history-command**]命令用来显示当前登录用户成功执行的历史命令。

【命令】

**[display history-command**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

用户登录设备后，系统会给每个用户自动分配一个历史命令缓冲区，用于存放用户本次登录用户成功执行的命令行，以便用户查看和调用。历史命令缓存区有大小限制，缺省保存10条命令，用户也可以通过**history-command max-size**命令来修改大小。当数目达到上限时，系统会自动删除最早的记录，来保存最新成功执行的命令。

如果用户退出登录，系统会自动清除该历史命令缓存区的所有记录。

【举例】

\# 显示历史命令缓存区内保存的命令。

\<Sysname\> display history-command

  system-view

  vlan 2

  quit

【相关命令】

·**history-command max-size**（基础配置命令参考/登录设备）

**CLI \-- CLI命令 \-- display history-command all**

------------------------------------------------------------------------

**[display history-command all**]命令用来显示所有登录用户成功执行的历史命令。

【命令】

**[display history-command all**]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

系统中有一个共享历史命令缓冲区，用于存放所有登录用户成功执行的命令行，以便用户查看（不能调用）。历史命令缓存区的大小固定为1024条，不可配置。当数目达到上限时，系统会自动删除最早的记录，来保存最新成功执行的命令。

即便用户退出登录，系统也不会清除共享历史命令缓存区中该用户的历史命令记录。

【举例】

\# 显示所有登录用户成功执行的历史命令。

\<Sysname\> display history-command all

  Date       Time     Terminal   Ip              User

  03/16/2012 20:03:33 vty0       192.168.1.26    \*\*

  Cmd:dis his all

  03/16/2012 20:03:29 vty0       192.168.1.26    \*\*

  Cmd:sys

表1-3 display history-command all命令显示信息描述表

字段

描述

Date

执行命令行的日期

Time

执行命令行的时间

Terminal

执行命令的用户使用的登录用户线

Ip

执行命令的用户使用的登录IP

User

执行命令的用户使用的登录用户名

Cmd

执行的命令（和用户的输入保持一致）

【相关命令】

·**display history-command**

**CLI \-- CLI命令 \-- display hotkey**

------------------------------------------------------------------------

**[display hotkey**]命令用来显示系统支持的快捷键及其含义。

【命令】

**[display hotkey**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示系统支持的快捷键及其含义。

\<Sysname\> display hotkey

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- Hotkeys \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

           -Defined command hotkeys-

CTRL_G display current-configuration

CTRL_L display ip routing-table

CTRL_O undo debugging all

           -Undefined command hotkeys-

CTRL_T NULL

CTRL_U NULL

           -System-reserved hotkeys-

CTRL_A  Move the cursor to the beginning of the line.

CTRL_B  Move the cursor one character to the left.

CTRL_C  Stop the current command.

CTRL_D  Erase the character at the cursor.

CTRL_E  Move the cursor to the end of the line.

CTRL_F  Move the cursor one character to the right.

CTRL_H  Erase the character to the left of the cursor.

CTRL_K  Abort the connection request.

CTRL_N  Display the next command in the history buffer.

CTRL_P  Display the previous command in the history buffer.

CTRL_R  Redisplay the current line.

CTRL_V  Paste text from the clipboard.

CTRL_W  Delete the word to the left of the cursor.

CTRL_X  Delete all characters from the beginning of the line to the cursor.

CTRL_Y  Delete all characters from the cursor to the end of the line.

CTRL_Z  Return to the User View.

CTRL\_  Kill incoming connection or redirect connection.

ESC_B   Move the cursor back one word.

ESC_D   Delete all characters from the cursor to the end of the word.

ESC_F   Move the cursor forward one word.

表1-4 display hotkey命令显示信息描述表

字段

描述

Defined command hotkeys

已定义的快捷键

Undefined command hotkeys

未定义的快捷键

System-reserved hotkeys

系统保留的快捷键。每个保留快捷键的作用请参见[表]1-5(?39677947#_Ref325619217)

表1-5 系统保留的快捷键

快捷键

功能

\<Ctrl+A\>

将光标移动到当前行的开头

\<Ctrl+B\>

将光标向左移动一个字符

\<Ctrl+C\>

停止当前正在执行的功能

\<Ctrl+D\>

删除当前光标所在位置的字符

\<Ctrl+E\>

将光标移动到当前行的末尾

\<Ctrl+F\>

将光标向右移动一个字符

\<Ctrl+H\>

删除光标左侧的一个字符

\<Ctrl+K\>

终止呼出的连接

\<Ctrl+R\>

重新显示当前行信息

\<Ctrl+V\>

粘贴剪贴板的内容

\<Ctrl+W\>

删除光标左侧连续字符串内的所有字符

\<Ctrl+X\>

删除光标左侧所有的字符

\<Ctrl+Y\>

删除光标所在位置及其右侧所有的字符

\<Ctrl+Z\>

退回到用户视图

\<Ctrl+\>

终止当前连接

\<Esc+B\>

将光标移动到左侧连续字符串的首字符处

\<Esc+D\>

删除光标所在位置及其右侧连续字符串内的所有字符

\<Esc+F\>

将光标向右移到下一个连续字符串之前

【相关命令】

·**hotkey**

**CLI \-- CLI命令 \-- hotkey**

------------------------------------------------------------------------

**[hotkey**]命令用来为快捷键指定对应的命令行。

**[undo hotkey**]命令用来恢复缺省情况。

【命令】

**[hotkey **[{ **ctrl_g** \| **ctrl_l** \| **ctrl_o** \| **ctrl_t** \| **ctrl_u** } *command*]]

**[undo hotkey **[{ **ctrl_g** \| **ctrl_l** \| **ctrl_o** \| **ctrl_t** \| **ctrl_u** }]]

【缺省情况】

·\<Ctrl+G\>对应命令**display current-configuration**（显示当前配置）。

·\<Ctrl+L\>对应命令**display ip routing-table**（显示IPv4路由表信息）。

·\<Ctrl+O\>对应命令**undo debugging all**（关闭设备支持的所有功能项的调试开关）。

·\<Ctrl+T\>没有关联任何命令行。

·\<Ctrl+U\>没有关联任何命令行。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ctrl_g**]：表示为快捷键\<Ctrl+G\>指定一条命令。

**[ctrl_l**]：表示为快捷键\<Ctrl+L\>指定一条命令。

**[ctrl_o**]：表示为快捷键\<Ctrl+O\>指定一条命令。

**[ctrl_t**]：表示为快捷键\<Ctrl+T\>指定一条命令。

**[ctrl_u**]：表示为快捷键\<Ctrl+U\>指定一条命令。

*[command*]：快捷键关联的命令行。

【使用指导】

通过快捷键用户可以简便、快捷的操作设备，使用**display hotkey**命令可以查看设备支持的所有快捷键及其含义。

【举例】

\# 指定命令**display tcp status**的快捷键为\<Ctrl+T\>。

\<Sysname\> system-view

Sysname hotkey ctrl_t display tcp status

【相关命令】

·**display hotkey**

**CLI \-- CLI命令 \-- quit**

------------------------------------------------------------------------

**[quit**]命令用来使用户从当前视图退回到上一层视图。

【命令】

**[quit**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

如果当前是用户视图，执行**quit**后，会断开当前连接，退出系统。

【举例】

\# 从接口GigabitEthernet1/0/1视图退回到系统视图，再退回到用户视图。

Sysname-GigabitEthernet1/0/1 quit

Sysname quit

\<Sysname\>

**CLI \-- CLI命令 \-- repeat**

------------------------------------------------------------------------

**[repeat**]命令用来重复执行当前视图下的历史记录命令。

【命令】

**[repeat ** *number* ]  **count** *times*   **delay** *seconds*

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：表示重复执行历史命令的条数，取值范围为1～10，缺省值为1。

**[count ***times*]：表示重复执行历史命令的次数，取值范围为0～4294967295，缺省值为0。如不指定该参数，则历史命令一直重复执行，直到执行用户线视图下设置的终止当前运行任务的快捷键才能停止执行该命令，默认的终止快捷键为\<Ctrl+C\>。关于终止当前执行任务的快捷键的设置，请参见"基础配置"中的"登录设备"。

**[delay ***seconds*]：表示重复执行历史命令的时间间隔，取值范围为0～4294967295，单位为秒，缺省值为1秒。

【使用指导】

需要注意的是：

·重复执行历史命令时，系统将按照历史命令的下发顺序执行。例如，用户在某视图下依次执行命令a、b和c后，再执行**repeat** 3命令，则系统将按照a、b和c的顺序重复执行一次。

·如果用户重复执行的历史命令中存在交互式命令，需要用户手动处理此交互式命令，直到交互式命令执行结束，历史命令才会继续被重复执行。

【举例】

\# 重复执行最近2条历史命令**display cpu**和**display clock**，重复执行3次，时间间隔10秒。

\<Sysname\> repeat 2 count 3 delay 10

\<Sysname\> display cpu

Unit CPU usage:

      33% in last 5 seconds

      32% in last 1 minute

      33% in last 5 minutes

\<Sysname\> display clock

12:20:08 UTC Thu 06/19/2014

\<Sysname\> display cpu

Unit CPU usage:

      33% in last 5 seconds

      32% in last 1 minute

      33% in last 5 minutes

\<Sysname\> display clock

12:20:18 UTC Thu 06/19/2014

\<Sysname\> display cpu

Unit CPU usage:

      33% in last 5 seconds

      32% in last 1 minute

      33% in last 5 minutes

\<Sysname\> display clock

12:20:28 UTC Thu 06/19/2014

【相关命令】

·**display history-command**

·**history-command max-size**

**CLI \-- CLI命令 \-- return**

------------------------------------------------------------------------

**[return**]命令用来从当前视图（非用户视图）直接退回到用户视图。

【命令】

**[return**]

【视图】

除用户视图外的任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

用户也可以使用组合键\<Ctrl+Z\>从当前视图（非用户视图）直接退回到用户视图，效果等同于执行**return**命令。

【举例】

\# 从接口GigabitEthernet1/0/1视图退回到用户视图。

Sysname-GigabitEthernet1/0/1 return

\<Sysname\>

**CLI \-- CLI命令 \-- screen-length disable**

------------------------------------------------------------------------

**[screen-length disable**]命令用来禁用当前用户的分屏显示功能。

**[undo screen-length disable**]命令用来启用当前用户的分屏显示功能。

【命令】

**[screen-length disable**]

**[undo screen-length disable**]

【缺省情况】

用户登录后将遵循用户线下的**screen-length**设置。**screen-length**设置的缺省情况为：允许分屏显示，下一屏显示24行数据。

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

禁止分屏显示时，会一次显示所有信息，如果信息较多，则会连续刷屏，不方便立即查看。

需要注意的是，该配置只对当前用户本次登录有效，用户重新登录后将恢复到缺省情况。

【举例】

\# 禁用当前用户的分屏显示功能。

\<Sysname\> screen-length disable

【相关命令】

·**screen-length**（基础配置命令参考/登录设备）

**CLI \-- CLI命令 \-- system-view**

------------------------------------------------------------------------

**[system-view**]命令用来从用户视图进入系统视图。

【命令】

**[system-view**]

【视图】

用户视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 从用户视图进入系统视图。

\<Sysname\> system-view

System View: return to User View with Ctrl+Z.

Sysname
