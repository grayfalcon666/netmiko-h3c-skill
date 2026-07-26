
**登录设备 \-- 登录设备调试命令 \-- debugging telnet server**

------------------------------------------------------------------------

【命令】

**[debugging telnet server**]

**[undo debugging telnet server**]

【视图】

用户视图

【缺省级别】

1：监控级

【参数】

无

【描述】

**[debugging telnet server**]命令用来打开Telnet服务端调试信息开关。**undo debugging telnet server**命令用来关闭Telnet服务端调试信息开关。

缺省情况下，Telnet服务端调试信息开关处于关闭状态。

表1-1 debugging telnet server命令输出信息描述表

字段

描述

Successfully opened PTY.

成功打开PTY

Started to execute the login program.

开始执行登录程序

Option negotiation started.

开始选项协商

Started to perform father cycling processing.

进入主循环处理

Failed to receive a message from the network. Reason: *error-info*.

网络侧接收数据失败，错误类型为*error-info*

其中*error-info*的取值为标准出错信息

Failed to read data from PTY. Reason: *error-info*.

PTY侧读取数据失败，错误类型为*error-info*

其中*error-info*的取值为标准出错信息

Failed to add file description to epoll.

向Epoll中添加文件描述符失败

Failed to create socket. Reason: *error-info*.

创建socket失败

其中*error-info*的取值为标准出错信息

Failed to set binary data to the DBM module.

向DBM模块设置二进制数据失败

Failed to open the database.

打开数据库失败

Received the SIGCHLD signal.

接收到SIGCHLD信号

Received the process shutdown signal.

接收到关闭进程信号

Failed to initialize the monitor module.

初始化MONITOR模块失败

Failed to create socket of this type: *domain-code*. Reason: *error-info*.

创建*domain-code*类型的SOCKET失败，错误信息为*error-info*

*[domain-code*]的取值可能为：

·2：IPv4

·10：IPv6

·37：LIPC

*[error-info*]的取值为标准出错信息

Failed to set option *option-name*. Reason: *error-info*.

设置Socket的*option-name*选项失败，错误信息为*error-info*

*[option-name*]的取值可能为：REUSEADDR、REUSEPORT

*[error-info*]的取值为标准出错信息

Failed to bind socket of this type: *domain-code*. Reason: *error-info*.

绑定*domain-code*类型的Socket地址失败，错误信息为*error-info*

*[domain-code*]的取值可能为：

·2：IPv4

·10：IPv6

·37：LIPC

*[error-info*]的取值为标准出错信息

Failed to listen to socket of this type: *domain-code*. Reason: *error-info*.

侦听*domain-code*类型的Socket失败，错误信息为*error-info*

*[domain-code*]的取值可能为：

·2：IPV4

·10：IPV6

·37：LIPC

*[error-info*]的取值为标准出错信息

Failed to accept a connection request from the client. Reason: *error-info*.

接受客户端连接失败，错误类型为*error-info*

*[error-info*]的取值为标准出错信息

Failed to create a child process.

创建子进程失败

Received a connection request.

收到一个连接请求

Received a close request.

收到一个关闭连接请求

Successfully closed the Telnet server.

成功关闭Telnet服务

Successfully opened the Telnet server.

成功打开telnet服务器端

Successfully cleared the user information.

成功清除用户信息

Successfully closed PTY.

成功关闭PTY

Waiting remote response\...

开始等待远程响应

Failed to clear PTY data. Reason: *error-info*.

清除PTY侧数据失败，错误类型为*error-info*

其中*error-info*的取值可能为：write error、success

Failed to write data to network. Reason: *error-info*.

向网络侧写数据失败，错误信息为*error-info*

其中*error-info*的取值为标准出错信息

Sent DO option *option-name*.

发送DO选项，选项名称为：*option-name*

其中*option-name*的取值为RFC规定的标准选项

Sent DONT option *option-name*.

发送DONT选项，选项名称为：*option-name*

其中*option-name*的取值为RFC规定的标准选项

Sent WILL option *option-name*.

发送WILL选项，选项名称为：*option-name*

其中*option-name*的取值为RFC规定的标准选项

Sent WONT option *option-name*.

发送WONT选项，选项名称为：*option-name*

其中*option-name*的取值为RFC规定的标准选项

Received DO option *option-name*.

接收到DO选项，选项名称为：*option-name*

其中*option-name*的取值为RFC规定的标准选项

Received DONT option *option-name*.

接收到DONT选项，选项名称为：*option-name*

其中*option-name*的取值为RFC规定的标准选项

Received WILL option *option-name*.

接收到WILL选项，选项名称为：*option-name*

其中*option-name*的取值为RFC规定的标准选项

Received WONT option *option-name*.

接收到WONT选项，选项名称为：*option-name*

其中*option-name*的取值为RFC规定的标准选项

Sent IAC SB sub-option *suboption-name.*

向对方发送请求*suboption-name*子选项

其中*suboption-name*的取值为RFC规定的标准选项

Sent IAC SB sub-option *suboption-name* IS *option-value.*

向对方发送*suboption-name*应答子选项

其中*suboption-name*的取值为RFC规定的标准选项

Received IAC SB sub-option *suboption-name* SEND.

接收到对方的请求*suboption-name*子选项

其中*suboption-name*的取值为RFC规定的标准选项

Received IAC SB sub-option *suboption-name* IS *option-value.*

接收到对方的应答*suboption-name*子选项

其中*suboption-name*的取值为RFC规定的标准选项

Received IAC *option-name*.

接收到*option-name*选项

其中*option-name*的取值为RFC规定的标准选项

Sent IAC *option-name*.

向对方发送*option-name*选项

其中*option-name*的取值为RFC规定的标准选项

【举例】

\# 设备作为Telnet server，打开Telnet server调试信息开关，使用客户端登录到设备。

\<Sysname\> system-view

Sysname telnet server enable

Sysname quit

\<Sysname\> debugging telnet server

\*Nov 24 16:45:00:280 2010 Sysname TELNETD/7/RUN: Received a connection request.

\*Nov 24 16:45:00:294 2010 Sysname TELNETD/7/RUN: Successfully opened PTY.

\*Nov 24 16:45:00:295 2010 Sysname TELNETD/7/RUN: Option negotiation started.

\*Nov 24 16:45:00:295 2010 Sysname TELNETD/7/FSM: Sent DO TERMINAL TYPE.

\*Nov 24 16:45:00:296 2010 Sysname TELNETD/7/FSM: Sent DO TSPEED.

\*Nov 24 16:45:00:296 2010 Sysname TELNETD/7/FSM: Sent DO XDISPLOC.

\*Nov 24 16:45:00:297 2010 Sysname TELNETD/7/FSM: Sent DO NEW-ENVIRON.

\*Nov 24 16:45:00:304 2010 Sysname TELNETD/7/FSM: Sent DO OLD-ENVIRON.

\*Nov 24 16:45:00:305 2010 Sysname TELNETD/7/RUN: Waiting remote response\...

\*Nov 24 16:45:00:319 2010 Sysname TELNETD/7/FSM: Received WILL TERMINAL TYPE.

\*Nov 24 16:45:00:319 2010 Sysname TELNETD/7/FSM: Received WILL NAWS.

\*Nov 24 16:45:00:320 2010 Sysname TELNETD/7/FSM: Sent DO NAWS.

\*Nov 24 16:45:00:321 2010 Sysname TELNETD/7/RUN: Waiting remote response\...

\*Nov 24 16:45:00:322 2010 Sysname TELNETD/7/FSM: Received WONT TSPEED.

\*Nov 24 16:45:00:323 2010 Sysname TELNETD/7/FSM: Received WONT XDISPLOC.

\*Nov 24 16:45:00:323 2010 Sysname TELNETD/7/FSM: Received WILL NEW-ENVIRON.

\*Nov 24 16:45:00:324 2010 Sysname TELNETD/7/FSM: Received WONT OLD-ENVIRON.

\*Nov 24 16:45:00:324 2010 Sysname TELNETD/7/FSM: Sent IAC SB NEW-ENVIRON SEND .

\*Nov 24 16:45:00:325 2010 Sysname TELNETD/7/FSM: Sent IAC SB TERMINAL-TYPE SEND.

\*Nov 24 16:45:00:326 2010 Sysname TELNETD/7/RUN: Waiting remote response\...

\*Nov 24 16:45:00:337 2010 Sysname TELNETD/7/FSM: Received IAC SB NAWS 0 80(80) 0 26(26).

\*Nov 24 16:45:00:337 2010 Sysname TELNETD/7/RUN: Waiting remote response\...

\*Nov 24 16:45:00:422 2010 Sysname TELNETD/7/FSM: Received IAC SB NEW-ENVIRON IS .

\*Nov 24 16:45:00:422 2010 Sysname TELNETD/7/FSM: Received IAC SB TERMINAL-TYPE IS \"ANSI\".

\*Nov 24 16:45:00:422 2010 Sysname TELNETD/7/FSM: Sent WILL SUPPRESS GO AHEAD.

\*Nov 24 16:45:00:422 2010 Sysname TELNETD/7/FSM: Sent DO ECHO.

\*Nov 24 16:45:00:422 2010 Sysname TELNETD/7/FSM: Sent WILL STATUS.

\*Nov 24 16:45:00:422 2010 Sysname TELNETD/7/FSM: Sent DO LFLOW.

\*Nov 24 16:45:00:422 2010 Sysname TELNETD/7/RUN: Waiting remote response\...

\*Nov 24 16:45:00:422 2010 Sysname TELNETD/7/FSM: Received DO SUPPRESS GO AHEAD.

\*Nov 24 16:45:00:422 2010 Sysname TELNETD/7/RUN: Waiting remote response\...

\*Nov 24 16:45:00:523 2010 Sysname TELNETD/7/FSM: Received WILL ECHO.

\*Nov 24 16:45:00:523 2010 Sysname TELNETD/7/FSM: Received DONT STATUS.

\*Nov 24 16:45:00:523 2010 Sysname TELNETD/7/FSM: Received WONT LFLOW.

\*Nov 24 16:45:00:524 2010 Sysname TELNETD/7/FSM: Received WILL ECHO.

\*Nov 24 16:45:00:524 2010 Sysname TELNETD/7/FSM: Sent DONT ECHO.

\*Nov 24 16:45:00:524 2010 Sysname TELNETD/7/FSM: Sent WILL ECHO.

\*Nov 24 16:45:00:531 2010 Sysname TELNETD/7/RUN: Started to perform father cycling processing.

\*Nov 24 16:45:00:531 2010 Sysname TELNETD/7/RUN: Started to execute the login program.

\*Nov 24 16:45:00:535 2010 Sysname TELNETD/7/FSM: Received WONT ECHO.

\*Nov 24 16:45:00:636 2010 Sysname TELNETD/7/FSM: Received DO ECHO.

**登录设备 \-- 登录设备调试命令 \-- debugging telnet client**

------------------------------------------------------------------------

【命令】

**[debugging telnet client**]

**[undo debugging telnet client**]

【视图】

用户视图

【缺省级别】

1：监控级

【参数】

无

【描述】

**[debugging telnet client**]命令用来打开Telnet客户端调试信息开关。**undo debugging telnet client**命令用来关闭Telnet客户端调试信息开关。

缺省情况下，Telnet服客户端调试信息开关处于关闭状态。

表1-2 debugging telnet client命令输出信息描述表

字段

描述

Failed to receive a message from the network. Reason: *error-info*.

从网络侧获取数据失败，错误信息为*error-type*

其中*error-info*的取值为标准出错信息

Failed to read data from TTY. Reason: *error-info*.

从TTY侧读取数据失败，错误信息为*error-info*

其中*error-info*的取值为标准出错信息

Failed to open database.

打开数据库失败

Failed to use the DBM aware function.

注册DBM感知失败

Failed to bind socket. Reason: *error-info*.

绑定Socket地址失败，错误信息为*error-info*

*[error-info*]的取值为标准出错信息

Pressed Ctrl + K.

按Ctrl + K键

Failed to set option *option-name*. Reason: *error-info*.

设置socket的*option-name*选项失败，错误信息为*error-info*

其中*option-name*的取值可能为：REUSEADDR、REUSEPORT

*[error-info*]的取值为标准出错信息

Failed to create a socket. Reason: *error-info*.

创建Socket失败，错误信息为*error-info*

*[error-info*]的取值为标准出错信息

Option negotiation started.

开始进行选项协商

Failed to write data to TTY. Reason: *error-info*.

向TTY侧写数据失败，错误信息为*error-info*

其中*error-info*的取值为标准出错信息

Failed to write data to network. Reason: *error-info*.

向网络侧写数据失败，错误信息为*error-info*

其中*error-info*的取值为标准出错信息

Sent DO option *option-name*.

发送DO选项，选项名称为：*option-name*

其中*option-name*的取值为RFC规定的标准选项

Sent DONT option *option-name*.

发送DONT选项，选项名称为：*option-name*

其中*option-name*的取值为RFC规定的标准选项

Sent WILL option *option-name*.

发送WILL选项，选项名称为：*option-name*

其中*option-name*的取值为RFC规定的标准选项

Sent WONT option *option-name*.

发送WONT选项，选项名称为：*option-name*

其中*option-name*的取值为RFC规定的标准选项

Received DO option *option-name*.

接收到DO选项，选项名称为：*option-name*

其中*option-name*的取值为RFC规定的标准选项

Received DONT option *option-name*.

接收到DONT选项，选项名称为：*option-name*

其中*option-name*的取值为RFC规定的标准选项

Received WILL option *option-name*.

接收到WILL选项，选项名称为：*option-name*

其中*option-name*的取值为RFC规定的标准选项

Received WONT option *option-name*.

接收到WONT选项，选项名称为：*option-name*

其中*option-name*的取值为RFC规定的标准选项

Sent IAC SB sub-option *suboption-name* SEND.

向对方发送请求*suboption-name*子选项

其中*suboption-name*的取值为RFC规定的标准选项

Sent IAC SB sub-option *suboption-name* IS *option-value.*

向对方发送*suboption-name*应答子选项

其中*suboption-name*的取值为RFC规定的标准选项

Received IAC SB sub-option *suboption-name* SEND.

接收到对方的请求*suboption-name*子选项

其中*suboption-name*的取值为RFC规定的标准选项

Received IAC SB sub-option *suboption-name* IS *option-value.*

接收到对方的应答*suboption-name*子选项

其中*suboption-name*的取值为RFC规定的标准选项

Received IAC *option-name*.

接收到*option-name*选项

其中*option-name*的取值为RFC规定的标准选项

Sent IAC *option-name*.

向对方发送*option-name*选项

其中*option-name*的取值为RFC规定的标准选项

【举例】

\# 打开调试开关，设备作为Telnet客户端，连接到远程服务器。

\<Sysname\> debugging telnet client

\<Sysname\> telnet 1.1.1.1

Trying 1.1.1.1 \...

Press CTRL+K to abort

Connected to 1.1.1.1 \...

\*Nov 24 16:50:27:711 2010 Sysname TELNET/7/RUN: Option negotiation started.

\*Nov 24 16:50:27:714 2010 Sysname TELNET/7/FSM: Sent DO SUPPRESS GO AHEAD.

\*Nov 24 16:50:27:716 2010 Sysname TELNET/7/FSM: Sent WILL TERMINAL TYPE.

\*Nov 24 16:50:27:718 2010 Sysname TELNET/7/FSM: Sent WILL NAWS.

\*Nov 24 16:50:27:719 2010 Sysname TELNET/7/FSM: Sent WILL TSPEED.

\*Nov 24 16:50:27:722 2010 Sysname TELNET/7/FSM: Sent WILL NEW-ENVIRON.

\*Nov 24 16:50:27:724 2010 Sysname TELNET/7/FSM: Sent DO STATUS.

\*Nov 24 16:50:27:726 2010 Sysname TELNET/7/FSM: Received DO TERMINAL TYPE.

\*Nov 24 16:50:27:727 2010 Sysname TELNET/7/FSM: Received DO TSPEED.

\*Nov 24 16:50:27:728 2010 Sysname TELNET/7/FSM: Received DO XDISPLOC.

\*Nov 24 16:50:27:731 2010 Sysname TELNET/7/FSM: Sent WONT XDISPLOC.

\*Nov 24 16:50:27:733 2010 Sysname TELNET/7/FSM: Received DO NEW-ENVIRON.

\*Nov 24 16:50:27:734 2010 Sysname TELNET/7/FSM: Received DO OLD-ENVIRON.

\*Nov 24 16:50:27:735 2010 Sysname TELNET/7/FSM: Sent WONT OLD-ENVIRON.

\*Nov 24 16:50:27:736 2010 Sysname TELNET/7/FSM: Received WILL SUPPRESS GO AHEAD.

\*Nov 24 16:50:27:738 2010 Sysname TELNET/7/FSM: Received DO NAWS.

\*Nov 24 16:50:27:740 2010 Sysname TELNET/7/FSM: Sent IAC SB NAWS 0 80 (80) 0 24 (24).

\*Nov 24 16:50:27:742 2010 Sysname TELNET/7/FSM: Received WILL STATUS.

\*Nov 24 16:50:27:744 2010 Sysname TELNET/7/FSM: Received IAC SB TERMINAL-SPEED SEND.

\*Nov 24 16:50:27:745 2010 Sysname TELNET/7/FSM: Sent IAC SB TERMINAL-SPEED IS 9600,9600.

\*Nov 24 16:50:27:748 2010 Sysname TELNET/7/FSM: Received IAC SB NEW-ENVIRON SEND .

\*Nov 24 16:50:27:753 2010 Sysname TELNET/7/FSM: Sent IAC SB NEW-ENVIRON IS .

\*Nov 24 16:50:27:759 2010 Sysname TELNET/7/FSM: Received IAC SB TERMINAL-TYPE SEND.

\*Nov 24 16:50:27:761 2010 Sysname TELNET/7/FSM: Sent IAC SB TERMINAL-TYPE IS \"VT100\".

\*Nov 24 16:50:27:844 2010 Sysname TELNET/7/FSM: Received DO ECHO.

\*Nov 24 16:50:27:845 2010 Sysname TELNET/7/FSM: Sent WONT ECHO.

\*Nov 24 16:50:27:846 2010 Sysname TELNET/7/FSM: Received DO LFLOW.

\*Nov 24 16:50:27:847 2010 Sysname TELNET/7/FSM: Sent WONT LFLOW.

\*Nov 24 16:50:27:855 2010 Sysname TELNET/7/FSM: Received WILL ECHO.

\*Nov 24 16:50:27:856 2010 Sysname TELNET/7/FSM: Sent DO ECHO.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Copyright (c) 2004-2010 Hangzhou H3C Tech. Co., Ltd. All rights reserved.  \*

\* Without the owner\'s prior written consent,                                 \*

\* no decompiling or reverse-engineering shall be allowed.                    \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

login:

