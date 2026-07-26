
**FTP \-- FTP服务器调试命令 \-- debugging ftp-server**

------------------------------------------------------------------------

**[debugging ftp-server**]命令用来打开FTP服务器的调试信息开关。

**[undo debugging ftp-server**]命令用来关闭FTP服务器的调试信息开关。

【命令】

**[debugging ftp-server**]

**[undo debugging ftp-server**]

【缺省情况】

FTP服务器的调试信息开关处于关闭状态。

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

表1-1 debugging ftp-server命令输出信息描述表

字段

描述

Request received from user *user-name@ip-address* for *ftp-command* *arg*.

收到用户*user-name*@*ip-address*的请求，请求对应的指令为*ftp-command* *arg*

·*user-name*表示登录用户名

·*ip-address*表示登录用户的IP地址

·*ftp-command*表示登录用户执行的FTP指令

·*arg*表示FTP指令中携带的参数

Active data connection to user *user-name*@*ip-address* successfully established.

与用户*user-name*@*ip-address*间的FTP主动数据连接创建成功

Passive data connection to user *user-name*@*ip-address* successfully established.

与用户*user-name*@*ip-address*间的FTP被动数据连接创建成功

Data connection to user *user-name*@*ip-address* closed.

与用户*user-name*@*ip-address*间的FTP数据连接断开

*[number* bytes sent from FTP server to client %s@%s.]

FTP服务器给用户*user-name*@*ip-address*发送了*number*字节的数据

*[number *bytes sent from client %s@%s to FTP server.]

用户*user-name*@*ip-address*给FTP服务器发送了*number*字节的数据

【使用指导】

\# 设备作为FTP服务器，打开设备的FTP服务器调试信息开关。

\<Sysname\> debugging ftp-server

\<Sysname\> system-view

Sysname ftp server enable

Sysname

\*May 12 15:02:05:781 2011 Sysname FTPD/7/Request received from user@192.168.1.44 for [user User.]

\*May 12 15:02:09:570 2011 Sysname FTPD/7/ Request received from user User@192.168.1.44 for [pass \*.]

*// 用户（IP地址为192.168.1.44）登录服务器，使用的用户名为ftp，密码为隐藏显示*

\*May 12 15:10:14:381 2011 Sysname FTPD/7/Request received from user User@192.168.1.44 for pasv .

\*May 12 15:10:14:389 2011 Sysname FTPD/7/Passive data connection to user User@192.168.1.44 successfully established.

\*May 12 15:10:14:401 2011 Sysname FTPD/7/Request received from user User@192.168.1.44 for [list .]

\*May 12 15:10:14:411 2011 Sysname FTPD/7/Data connection to user User@192.168.1.44 closed.

*// 用户（IP地址为192.168.1.44）以被动方式查看服务器当前目录下的文件以及子文件夹*

\*May 12 15:11:16:804 2011 Sysname FTPD/7/Request received from user User@192.168.1.44 for pasv .

\*May 12 15:11:16:813 2011 Sysname FTPD/7/Passive data connection to user User@192.168.1.44 successfully established.

\*May 12 15:11:16:825 2011 Sysname FTPD/7/ Request received from user User@192.168.1.44 for [retr config.cfg.]

\*May 12 15:11:16:834 2011 Sysname FTPD/7/3304 bytes sent from FTP server to client User@192.168.1.44.

\*May 12 15:11:16:834 2011 Sysname FTPD/7/ Data connection to user User@192.168.1.44 closed.

\*Jan  1 06:49:39:431 2011 Sysname FTP/7/REPLY: 226 File successfully transferred.

*// 用户（IP地址为192.168.1.44）以被动方式从服务器上下载文件config.cfg*

\*May 12 15:14:12:967 2011 Sysname FTPD/7/ Request received from user User@192.168.1.44 for pasv .

\*May 12 15:14:12:976 2011 Sysname FTPD/7/ Passive data connection to user User@192.168.1.44 successfully established.

\*May 12 15:14:12:989 2011 Sysname FTPD/7/ Request received from user User@192.168.1.44 for [stor aa.cfg.]

\*May 12 15:14:13:21 2011 Sysname FTPD/7/ FTPD/7/3304 bytes sent from client User@192.168.1.44(mailto:User@192.168.1.44) to FTP server.

\*May 12 15:11:16:834 2011 Sysname FTPD/7/ Data connection to user User@192.168.1.44 closed.

\*Jan  1 06:49:39:431 2011 Sysname FTP/7/REPLY: 226 File successfully transferred.

*// 用户（IP地址为192.168.1.44）以被动方式将一个本地文件上传到服务器，在服务器上存储的名字为aa.cfg*

\*May 12 15:18:19:948 2011 Sysname FTPD/7/ Request received from user User@192.168.1.44 for QUIT .

\*Jan  1 07:17:02:656 2011 Sysname FTP/7/REPLY: 221 Logout.

*// 用户（IP地址为192.168.1.44）退出登录*
