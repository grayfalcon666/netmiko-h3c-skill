<!-- CMD-INDEX
  tclsh                               | 用户视图             | L6
  tclquit                             | Tcl配置视图          | L46
-->

**Tcl \-- Tcl配置命令 \-- tclsh**

------------------------------------------------------------------------

**[tclsh**]命令用来从用户视图进入Tcl配置视图。

【命令】

**[tclsh**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在用户视图下执行**tclsh**命令，会进入Tcl配置视图。为兼容Comware配置方式，在Tcl配置视图下，用户可以直接输入Tcl脚本命令，也可以输入Comware系统的命令。命令输入完成后，直接回车即可执行。

Tcl配置视图下，支持Tcl8.5版本的所有命令。

对于Comware系统的命令，Tcl配置视图相当于用户视图，配置方式同用户视图下的配置。

【举例】

\# 从用户视图进入Tcl配置视图。

\<Sysname\> tclsh

\<Sysname-tcl\>

【相关命令】

·**tclquit**

**Tcl \-- Tcl配置命令 \-- tclquit**

------------------------------------------------------------------------

**[tclquit**]命令用来从Tcl配置视图退回到用户视图。

【命令】

**[tclquit**]

【视图】

Tcl配置视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·如果在Tcl配置视图下使用了Comware命令进入了子视图，则只能用**quit**命令退回到上一级视图，不能执行**tclquit**命令。

·执行该命令效果等同于在Tcl配置视图下执行**quit**命令。

【举例】

\# 从Tcl配置视图退回到用户视图。

\<Sysname-tcl\> tclquit

\<Sysname\>

【相关命令】

·**tcl****sh**

