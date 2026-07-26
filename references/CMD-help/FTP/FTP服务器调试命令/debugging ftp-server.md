::: {#105205649 .myid}
[]{#_Toc404782374}[]{#struct_0_x2161_x1184_706736584}

**FTP \-- FTP服务器调试命令 \-- debugging ftp-server**

------------------------------------------------------------------------

[**[debugging ]{lang="EN-US"}[ftp-server]{lang="EN-US"}**]{#struct_0_x2161_x1184_x1827307280}[命令用来打开]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器的调试信息开关。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[debugging ftp-server]{lang="EN-US"}**]{#struct_0_x2161_x1184_x1633084064}[命令用来关闭]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器的调试信息开关。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2161_x1184_707353832}

[**[debugging ftp-server]{lang="EN-US"}**]{#struct_0_x2161_x1184_x2119207416}

[**[undo debugging ftp-server]{lang="EN-US"}**]{#struct_0_x2161_x1184_1082059757}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2161_x1184_x1994635464}

[[FTP]{lang="EN-US"}]{#struct_0_x2161_x1184_2034284949}[服务器的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2161_x1184_1484166416}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2161_x1184_x103915382}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2161_x1184_x1671153450}

[[network-admin]{lang="EN-US"}]{#struct_0_x2161_x1184_2125003280}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2161_x1184_261063976}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x2161_x1184_x847369944}

[]{#struct_0_x2161_x1184_x1057609116}[[表1-1 ]{lang="EN-US"}[debugging ftp-server]{lang="EN-US"}]{#_Toc130718927}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x124770177}[[字段]{style="font-family:黑体"}]{#struct_0_x2161_x1184_656299952}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2161_x1184_x1990850898}

[[Request received from user *user-name@ip-address* for \[*ftp-command*\] \[*arg*\].]{lang="EN-US"}]{#struct_0_x2161_x1184_1405757331}

[[收到用户]{style="font-family:宋体"}*[user-name]{lang="EN-US"}*[@*ip-address*]{lang="EN-US"}]{#struct_0_x2161_x1184_1484166415}[的请求，请求对应的指令为]{style="font-family:宋体"}[\[*ftp-command*\] \[*arg*\]]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[user-name]{lang="EN-US"}*]{#struct_0_x2161_x1184_x104111990}[表示]{lang="EN-US" style="font-family:宋体"}[登录用户名]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ip-address]{lang="EN-US"}*]{#struct_0_x2161_x1184_x982817421}[表示]{lang="EN-US" style="font-family:宋体"}[登录用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ftp-command]{lang="EN-US"}*]{#struct_0_x2161_x1184_1396220737}[表示]{lang="EN-US" style="font-family:
  宋体"}[登录用户执行的]{style="font-family:宋体"}[FTP]{lang="EN-US"}[指令]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[arg]{lang="EN-US"}*]{#struct_0_x2161_x1184_x1345365780}[表示]{style="font-family:宋体"}[FTP]{lang="EN-US"}[指令中携带的参数]{style="font-family:宋体"}

[[Active data connection to user *user-name*@*ip-address* successfully established.]{lang="EN-US"}]{#struct_0_x2161_x1184_x922769966}

[[与用户]{style="font-family:宋体"}*[user-name]{lang="EN-US"}*[@*ip-address*]{lang="EN-US"}]{#struct_0_x2161_x1184_x678814996}[间的]{style="font-family:宋体"}[FTP]{lang="EN-US"}[主动数据连接创建成功]{style="font-family:宋体"}

[[Passive data connection to user *user-name*@*ip-address* successfully established.]{lang="EN-US"}]{#struct_0_x2161_x1184_1484166414}

[[与用户]{style="font-family:宋体"}*[user-name]{lang="EN-US"}*[@*ip-address*]{lang="EN-US"}]{#struct_0_x2161_x1184_x104046454}[间的]{style="font-family:宋体"}[FTP]{lang="EN-US"}[被动数据连接创建成功]{style="font-family:宋体"}

[[Data connection to user *user-name*@*ip-address* closed.]{lang="EN-US"}]{#struct_0_x2161_x1184_1698879919}

[[与用户]{style="font-family:宋体"}*[user-name]{lang="EN-US"}*[@*ip-address*]{lang="EN-US"}]{#struct_0_x2161_x1184_784350770}[间的]{style="font-family:宋体"}[FTP]{lang="EN-US"}[数据连接断开]{style="font-family:宋体"}

[*[number]{lang="EN-US"}*[ bytes sent from FTP server to client %s@%s.]{lang="EN-US"}]{#struct_0_x2161_x1184_2019418790}

[[FTP]{lang="EN-US"}]{#struct_0_x2161_x1184_577150457}[服务器给用户]{style="font-family:宋体"}*[user-name]{lang="EN-US"}*[@*ip-address*]{lang="EN-US"}[发送了]{style="font-family:宋体"}*[number]{lang="EN-US"}*[字节的数据]{style="font-family:宋体"}

[*[number ]{lang="EN-US"}*[bytes sent from client %s@%s to FTP server.]{lang="EN-US"}]{#struct_0_x2161_x1184_x723323176}

[[用户]{style="font-family:宋体"}*[user-name]{lang="EN-US"}*[@*ip-address*]{lang="EN-US"}]{#struct_0_x2161_x1184_1484166413}[给]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器发送了]{style="font-family:宋体"}*[number]{lang="EN-US"}*[字节的数据]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2161_x1184_x104243062}

[[\# ]{lang="EN-US"}]{#struct_0_x2161_x1184_1337621535}[设备作为]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器，打开设备的]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ftp-server]{lang="EN-US"}]{#struct_0_x2161_x1184_169254971}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] ftp server enable]{lang="EN-US"}

[\[Sysname\]]{lang="EN-US"}

[\*May 12 15:02:05:781 2011 Sysname FTPD/7/Request received from user@192.168.1.44 for \[user\] \[User\].]{lang="EN-US"}

[\*May 12 15:02:09:570 2011 Sysname FTPD/7/ Request received from user User@192.168.1.44 for \[pass\] \[\*\].]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x2161_x1184_2029010581}*[用户（]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.1.44]{lang="EN-US"}[）登录服务器，使用的用户名为]{style="font-family:宋体"}[ftp]{lang="EN-US"}[，密码为隐藏显示]{style="font-family:宋体"}*

[[\*May 12 15:10:14:381 2011 Sysname FTPD/7/Request received from user User@192.168.1.44 for \[pasv\] \[\].]{lang="EN-US"}]{#struct_0_x2161_x1184_1484166412}

[\*May 12 15:10:14:389 2011 Sysname FTPD/7/Passive data connection to user User@192.168.1.44 successfully established.]{lang="EN-US"}

[\*May 12 15:10:14:401 2011 Sysname FTPD/7/Request received from user User@192.168.1.44 for \[list\] \[\].]{lang="EN-US"}

[\*May 12 15:10:14:411 2011 Sysname FTPD/7/Data connection to user User@192.168.1.44 closed.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x2161_x1184_x104177526}*[用户（]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.1.44]{lang="EN-US"}[）以被动方式查看服务器当前目录下的文件以及子文件夹]{style="font-family:宋体"}*

[[\*May 12 15:11:16:804 2011 Sysname FTPD/7/Request received from user User@192.168.1.44 for \[pasv\] \[\].]{lang="EN-US"}]{#struct_0_x2161_x1184_x1825681746}

[\*May 12 15:11:16:813 2011 Sysname FTPD/7/Passive data connection to user User@192.168.1.44 successfully established.]{lang="EN-US"}

[\*May 12 15:11:16:825 2011 Sysname FTPD/7/ Request received from user User@192.168.1.44 for \[retr\] \[config.cfg\].]{lang="EN-US"}

[\*May 12 15:11:16:834 2011 Sysname FTPD/7/3304 bytes sent from FTP server to client User@192.168.1.44.]{lang="EN-US"}

[\*May 12 15:11:16:834 2011 Sysname FTPD/7/ Data connection to user User@192.168.1.44 closed.]{lang="EN-US"}

[\*Jan  1 06:49:39:431 2011 Sysname FTP/7/REPLY: 226 File successfully transferred.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x2161_x1184_x1935870959}*[用户（]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.1.44]{lang="EN-US"}[）以被动方式从服务器上下载文件]{style="font-family:宋体"}[config.cfg]{lang="EN-US"}*

[[\*May 12 15:14:12:967 2011 Sysname FTPD/7/ Request received from user User@192.168.1.44 for \[pasv\] \[\].]{lang="EN-US"}]{#struct_0_x2161_x1184_915926408}

[\*May 12 15:14:12:976 2011 Sysname FTPD/7/ Passive data connection to user User@192.168.1.44 successfully established.]{lang="EN-US"}

[\*May 12 15:14:12:989 2011 Sysname FTPD/7/ Request received from user User@192.168.1.44 for \[stor\] \[aa.cfg\].]{lang="EN-US"}

[\*May 12 15:14:13:21 2011 Sysname FTPD/7/ FTPD/7/3304 bytes sent from client ]{lang="EN-US"}[[User@192.168.1.44]{lang="EN-US"}](mailto:User@192.168.1.44)[ to FTP server.]{lang="EN-US"}

[\*May 12 15:11:16:834 2011 Sysname FTPD/7/ Data connection to user User@192.168.1.44 closed.]{lang="EN-US"}

[\*Jan  1 06:49:39:431 2011 Sysname FTP/7/REPLY: 226 File successfully transferred.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x2161_x1184_x163549065}*[用户（]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.1.44]{lang="EN-US"}[）以被动方式将一个本地文件上传到服务器，在服务器上存储的名字为]{style="font-family:宋体"}[aa.cfg]{lang="EN-US"}*

[[\*May 12 15:18:19:948 2011 Sysname FTPD/7/ Request received from user User@192.168.1.44 for \[QUIT\] \[\].]{lang="EN-US"}]{#struct_0_x2161_x1184_1813377258}

[[\*Jan  1 07:17:02:656 2011 Sysname FTP/7/REPLY: 221 Logout.]{lang="EN-US"}]{#struct_0_x2161_x1184_x695772137}

[*[// ]{lang="EN-US"}*]{#struct_0_x2161_x1184_713506062}*[用户（]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.1.44]{lang="EN-US"}[）退出登录]{style="font-family:宋体"}*
