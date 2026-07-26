
**HTTPD \-- HTTPD Probe命令 \-- display system internal httpd service**

------------------------------------------------------------------------

**[display system internal httpd service**]命令用来显示HTTPD服务相关信息。

【命令】

**[display system internal httpd service**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

通过本命令可以查看HTTPD服务信息，包括打开的服务端口，注册的URL，内部LIPC端口号等。

本命令仅在Debug版本支持，Release版本不提供。

【举例】

\# 显示HTTPD服务信息。

\<Sysname\> system-view

Sysname probe

Sysname-probe display system internal httpd service

Address family: IPv4

Port: 80

URL: /wnm/

Application family: LIPC

Application address: 0x0

Application port: 10529

Address family: IPv6

Port: 80

URL: /wnm/

Application family: LIPC

Application address: 0x0

Application port: 10529

表1-1 display system internal httpd service命令显示信息描述表

字段

描述

Address family

HTTPD服务的协议族类型，IPv4或者IPv6

Port

HTTPD服务打开的端口号

URL

HTTPD服务访问的目标资源地址

Application family

后台服务的协议族类型，LIPC或者TCP，目前仅支持LIPC

Application address

后台服务的地址，LIPC类型为LIPC地址，TCP类型为IP地址

Application port

后台服务打开的端口号

**HTTPD \-- HTTPD Probe命令 \-- debugging system internal httpd**

------------------------------------------------------------------------

**[debugging system internal httpd**]命令用来打开HTTPD的调试信息开关。

**[undo debugging system internal httpd**]命令用来关闭HTTPD的调试信息开关。

【命令】

**[debugging system internal httpd **[{ **all** \| **event** \| **process** \| **error** }]]

**[undo debugging system internal httpd **[{ **all** \| **event** \| **process** \| **error** }]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]**：**打开HTTPD模块全部调试信息开关。

**[event**]**：**打开HTTPD模块的事件调试信息开关。

**[process**]**：**打开HTTPD模块的处理调试信息开关。

**[error**]**：**打开HTTPD模块的错误调试信息开关。

【举例】

\# 打开HTTPD所有调试信息开关。

\<Sysname\> system-view

Sysname probe

Sysname-probe debugging system internal httpd all

\# 打开HTTPD事件调试信息开关。

\<Sysname\> system-view

Sysname probe

Sysname-probe debugging system internal httpd event

