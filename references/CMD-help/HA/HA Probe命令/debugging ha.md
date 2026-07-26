
**HA \-- HA Probe命令 \-- debugging ha**

------------------------------------------------------------------------

**[debugging ha**]命令用来打开HA各子模块的调试信息开关。

**[undo debugging ha**]命令用来关闭HA各子模块的调试信息开关。

【命令】

**[debugging ha **** all **[\|]** config**[ \|]** fsm**[ \| ]**policy**[ \|]** standby**[ \|]** sync **}

**[undo debugging ha****all **[\| ]**config **[\|]** fsm **[\|]** policy **[\| ]**standby **[\| ]**sync **}

【缺省情况】]

HA]各子模块的调试信息开关处于关闭状态。

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：HA所有模块的信息。

**[config**]：config子模块的信息。

**[fsm**]：FSM子模块的信息。

**[policy**]：policy子模块的信息。

**[standby**]：备份HA模块的信息。

**[sync**]：sync子模块的信息。

【举例】

\# 打开HA FSM子模块的调试开关。

\<Sysname\> debugging ha fsm

**HA \-- HA Probe命令 \-- display system internal ha service**

------------------------------------------------------------------------

**[display system internal ha service**]命令用来显示某个业务进程的HA统计信息，包括业务注册的基本信息、各控制消息接收处理统计、各数据的发送统计和接收统计等。

【命令】

**[display system internal ha service ***socket*]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[socket*]：所要查询的业务进程的socket，可通过**display system internal ha service-group** *sg-name*查询。

**HA \-- HA Probe命令 \-- display system internal ha service-group**

------------------------------------------------------------------------

**[display system internal ha service-group**]命令用来显示当前到HA模块注册的所有SG信息，包括SG的名称、SG的状态、SU的个数等信息。

【命令】

**[display system internal ha service-group** \*[ name*]****\*[instance***** ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[name*]：SG的名称。不指定该参数时，显示所有SG的信息。

*[instance*]：SG实例的名称（如果有实例）。

**HA \-- HA Probe命令 \-- display system internal ha statistics**

------------------------------------------------------------------------

**[display system internal ha statistics**]命令用来显示HA各子模块的统计信息。

【命令】

**[display system internal ha statistics****submodule ****[fsm **[\| ]**service **[} \| ]**summary** }

【视图】]

Probe]视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[submodule**]：HA子模块的信息。

**[fsm**]：FSM子模块的信息。

**[service**]：service子模块的信息。

**[summary**]：全局统计信息。

