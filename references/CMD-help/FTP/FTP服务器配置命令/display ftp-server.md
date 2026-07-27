<!-- CMD-INDEX
  display ftp-server                  | 任意视图             | L60
  display ftp-user                    | 任意视图             | L120
  free ftp user                       | 用户视图             | L194
  free ftp user-ip                    | 用户视图             | L228
  free ftp user-ip ipv6               | 用户视图             | L264
  ftp server acl                      | 系统视图             | L300
  ftp server dscp                     | 系统视图             | L354
  ftp server enable                   | 系统视图             | L398
  ftp server ipv6 dscp                | 系统视图             | L434
  ftp server ssl-server-policy        | 系统视图             | L478
  ftp timeout                         | 系统视图             | L528
  append                              | FTP客户端视图         | L572
  ascii                               | FTP客户端视图         | L616
  binary                              | FTP客户端视图         | L660
  bye                                 | FTP客户端视图         | L704
  cd                                  | FTP客户端视图         | L740
  cdup                                | FTP客户端视图         | L806
  close                               | FTP客户端视图         | L852
  debug                               | FTP客户端视图         | L892
  delete                              | FTP客户端视图         | L972
  dir                                 | FTP客户端视图         | L1010
  disconnect                          | FTP客户端视图         | L1106
  display ftp client source           | 任意视图             | L1146
  ftp                                 | 用户视图             | L1180
  ftp client source                   | 系统视图             | L1248
  ftp client ipv6 source              | 系统视图             | L1302
  ftp ipv6                            | 用户视图             | L1356
  get                                 | FTP客户端视图         | L1424
  help                                | FTP客户端视图         | L1524
  lcd                                 | FTP客户端视图         | L1602
  ls                                  | FTP客户端视图         | L1650
  mkdir                               | FTP客户端视图         | L1746
  newer                               | FTP客户端视图         | L1784
  open                                | FTP客户端视图         | L1832
  passive                             | FTP客户端视图         | L1890
  put                                 | FTP客户端视图         | L1938
  pwd                                 | FTP客户端视图         | L2038
  quit                                | FTP客户端视图         | L2074
  reget                               | FTP客户端视图         | L2110
  rename                              | FTP客户端视图         | L2164
  reset                               | FTP客户端视图         | L2228
  restart                             | FTP客户端视图         | L2254
  rhelp                               | FTP客户端视图         | L2310
  rmdir                               | FTP客户端视图         | L2504
  rstatus                             | FTP客户端视图         | L2552
  status                              | FTP客户端视图         | L2738
  system                              | FTP客户端视图         | L2830
  user                                | FTP客户端视图         | L2862
  verbose                             | FTP客户端视图         | L2916
  ?                                   | FTP客户端视图         | L2972
  tftp                                | 用户视图             | L3052
  tftp client source                  | 系统视图             | L3186
  tftp ipv6                           | 用户视图             | L3240
  tftp client ipv6 source             | 系统视图             | L3314
  tftp-server acl                     | 系统视图             | L3368
  tftp-server ipv6 acl                | 系统视图             | L3418
-->

**FTP \-- FTP服务器配置命令 \-- display ftp-server**

------------------------------------------------------------------------

**[display** **ftp-server**]命令用来显示设备作为FTP服务器时的配置和运行情况。

【命令】

**[display** **ftp-server**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示FTP服务器的配置和运行情况。

\<Sysname\> display ftp-server

FTP server is running.

User count:                        1

Idle-timeout timer (in minutes):  30

表1-1 display ftp-server命令显示信息描述表

字段

描述

FTP server is running

FTP服务器功能正在运行中

User count

当前登录的用户数

Idle-timeout timer (in minutes)

FTP连接自动断开前的空闲时间，如果在该时间段内，FTP客户端和FTP服务器之间没有报文交互，该FTP连接会被断开

【相关命令】

·**ftp** **server** **enable**

·**ftp** **timeout**

**FTP \-- FTP服务器配置命令 \-- display ftp-user**

------------------------------------------------------------------------

**[display** **ftp-user**]命令用来显示当前FTP用户的详细情况。

【命令】

**[display** **ftp-user**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示FTP用户详细情况。

\<Sysname\> display ftp-user

UserName     HostIP             Port     HomeDir

root         192.168.20.184     46539    flash:

当登录用户名长度超过10位时，将换行并靠右对齐显示；当登录用户的IP地址长度超过15位时，将换行并靠右对齐显示；当用户根路径长度超过37位时，将换行并靠右对齐显示。形如：

\<Sysname\> display ftp-user

UserName     HostIP             Port     HomeDir

user2        2000:2000:2000:    1499     flash:/user2

             2000:2000:2000:

                  2000:2000

administra   100.100.100.100    10001    flash:/123456789/123456789/123456789/

       tor                               123456789/123456789/123456789/1234567

                                                                  89/123456789

表1-2 display ftp-user命令显示信息描述表

字段

描述

UserName

当前登录的FTP用户名

HostIP

当前登录的FTP用户的IP地址

Port

当前登录的FTP用户使用的端口号

HomeDir

当前登录的FTP用户的授权路径

**FTP \-- FTP服务器配置命令 \-- free ftp user**

------------------------------------------------------------------------

**[free** **ftp** **user**]命令用来强制释放通过指定用户名建立的FTP连接。

【命令】

**[free** **ftp** **user** *username*]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[username*]：用户名。可以使用**display** **ftp-user**命令来查看当前FTP用户的信息。

【举例】

\# 强制释放通过用户名ftpuser建立的FTP连接。

\<Sysname\> free ftp user ftpuser

Are you sure to free FTP connection? [Y/N:y]

\<Sysname\>

**FTP \-- FTP服务器配置命令 \-- free ftp user-ip**

------------------------------------------------------------------------

**[free** **ftp** **user-ip**]命令用来强制释放通过指定IPv4地址建立的FTP连接。

【命令】

**[free** **ftp** **user-ip** *ipv4-address* [ **port** *port* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv4-address*]：待释放的FTP连接的源IP。可以使用**display** **ftp-user**命令来查看当前FTP连接的源IP。

**[port** *por**t*]：待释放的FTP连接的源端口，*port*为源端口的端口号。可以使用**display** **ftp-user**命令来查看当前FTP连接的源端口。

【举例】

\# 强制释放通过IP地址192.168.20.184建立的FTP连接。

\<Sysname\> free ftp user-ip 192.168.20.184

Are you sure to free FTP connection? [Y/N:y]

\<Sysname\>

**FTP \-- FTP服务器配置命令 \-- free ftp user-ip ipv6**

------------------------------------------------------------------------

**[free** **ftp** **user-ip**]命令用来强制释放通过指定IPv6地址建立的FTP连接。

【命令】

**[free** **ftp** **user-ip** **ipv6** *ipv6-address* [ **port** *port* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：待释放的FTP连接的源IP。可以使用**display** **ftp-user**命令来查看当前FTP连接的源IP。

**[port** *por**t*]：待释放的FTP连接的源端口，*port*为源端口的端口号。可以使用**display** **ftp-user**命令来查看当前FTP连接的源端口。

【举例】

\# 强制释放通过IP地址2000::154建立的FTP连接。

\<Sysname\> free ftp user-ip ipv6 2000::154

Are you sure to free FTP connection? [Y/N:y]

\<Sysname\>

**FTP \-- FTP服务器配置命令 \-- ftp server acl**

------------------------------------------------------------------------

**[ftp** **server** **acl**]命令用来使用ACL限制哪些FTP客户端可以访问设备。

**[undo** **ftp** **server** **acl**]命令用来恢复缺省情况。

【命令】

**[ftp** **server** **acl**[ { *acl-number* \| **ipv6** *acl-number6* }]]

**[undo** **ftp** **server** **acl** [ **ipv6** ]]

【缺省情况】

没有使用ACL限制FTP客户端。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl-number*]：表示IPv4访问控制列表号，取值范围为2000～3999。

**[ipv6** *acl-number6*]：表示IPv6访问控制列表号，取值范围为2000～3999。

【使用指导】

通过将FTP服务与ACL关联，可以过滤掉来自某些FTP客户端的FTP请求报文，只允许符合ACL过滤规则的FTP客户端访问设备。该配置只过滤新建立的FTP连接，不会对已建立的FTP连接和操作造成影响。如果多次使用该命令配置FTP服务与ACL关联，FTP服务将只与最后一次配置的ACL关联。

【举例】

\# 配置FTP服务与ACL关联，只允许FTP客户端（1.1.1.1）通过FTP访问本设备。

\<Sysname\> system-view

Sysname acl number 2001

Sysname-acl-basic-2001 rule 0 permit source 1.1.1.1 0

Sysname-acl-basic-2001 rule 1 deny source any

Sysname-acl-basic-2001 quit

Sysname ftp server acl 2001

**FTP \-- FTP服务器配置命令 \-- ftp server dscp**

------------------------------------------------------------------------

**[ftp server dscp**]命令用来配置FTP服务器发送的FTP报文的DSCP优先级。

**[undo ftp server dscp**]命令用来恢复缺省情况。

【命令】

**[ftp server dscp ***dscp-value*]

**[undo ftp server dscp**]

【缺省情况】

FTP服务器发送的FTP报文的DSCP优先级为0。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dscp-value*]：指定设备发送的FTP报文的DSCP优先级，取值范围为0～63。

【使用指导】

DSCP携带在IP报文中的ToS字段，用来体现报文自身的优先等级，决定报文传输的优先程度。

【举例】

\# 配置FTP服务器发送的FTP报文的DSCP优先级为30。

\<Sysname\> system-view

Sysname ftp server dscp 30

**FTP \-- FTP服务器配置命令 \-- ftp server enable**

------------------------------------------------------------------------

**[ftp** **server** **enable**]命令用来开启设备的FTP服务器功能，允许FTP用户登录。

**[undo** **ftp** **server** **enable**]命令用来关闭设备的FTP服务器功能。

【命令】

**[ftp** **server** **enable**]

**[undo** **ftp** **server** **enable**]

【缺省情况】

FTP服务器功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 开启设备的FTP服务器功能。

\<Sysname\> system-view

Sysname ftp server enable

**FTP \-- FTP服务器配置命令 \-- ftp server ipv6 dscp**

------------------------------------------------------------------------

**[ftp server ipv6 dscp**]命令用来配置FTP服务器发送的IPv6 FTP报文的DSCP优先级。

**[undo ftp server ipv6 dscp**]命令用来恢复缺省情况。

【命令】

**[ftp server ipv6 dscp ***dscp-value*]

**[undo ftp server ipv6 dscp**]

【缺省情况】

FTP服务器发送的IPv6 FTP报文的DSCP优先级为0。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dscp-value*]：指定设备发送的IPv6 FTP报文的DSCP优先级，取值范围为0～63。

【使用指导】

DSCP携带在IPv6报文中的Trafic class字段，用来体现报文自身的优先等级，决定报文传输的优先程度。

【举例】

\# 配置FTP服务器发送的IPv6 FTP报文的DSCP优先级为30。

\<Sysname\> system-view

Sysname ftp server ipv6 dscp 30

**FTP \-- FTP服务器配置命令 \-- ftp server ssl-server-policy**

------------------------------------------------------------------------

**[ftp server ssl-server-policy**]命令用来配置FTP服务与SSL服务器端策略关联。

**[undo ftp server ssl-server-policy**]命令用来取消FTP服务与SSL服务器端策略的关联。

【命令】

**[ftp server ssl-server-policy ***policy-name*]

**[undo ftp server ssl-server-policy**]

【缺省情况】

没有配置SSL服务器端策略与FTP服务关联。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：SSL服务器端策略名，为1～31个字符的字符串。

【使用指导】

当支持FTP安全扩展协议的两台设备建立FTP连接时，通过将FTP服务与SSL服务器端策略关联，可以建立一条安全的SSL连接来传输数据，保证FTP传输的安全性。

【举例】

\# 设置FTP服务使用的SSL服务器端策略为myssl。

\<Sysname\> system-view

Sysname ftp server ssl-server-policy myssl

【相关命令】

·**ftp server enable**

·**ssl server-policy**（安全/SSL）

**FTP \-- FTP服务器配置命令 \-- ftp timeout**

------------------------------------------------------------------------

**[ftp** **timeout**]命令用来设置FTP连接自动断开前的空闲时间。

**[undo** **ftp** **timeout**]命令用来恢复缺省情况。

【命令】

**[ftp** **timeout** *minute*]

**[undo** **ftp** **timeout**]

【缺省情况】

FTP连接自动断开前的空闲时间为30分钟。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[minute*]：FTP连接自动断开前的空闲时间，取值范围为1～35791，单位为分钟。

【使用指导】

如果在设置的连接空闲时间到期时，FTP服务器和客户端一直没有信息交互，FTP服务器将认为该连接已失效并断开该连接，从而避免系统资源被持续占用、其它FTP用户的登录受影响。

【举例】

\# 设置FTP连接自动断开前的空闲时间为36分钟。

\<Sysname\> system-view

Sysname ftp timeout 36

**FTP \-- FTP客户端配置命令 \-- append**

------------------------------------------------------------------------

**[append**]命令用来在原文件内容的后面添加新文件的内容。

【命令】

**[append** *localfile* [ *remotefile* ]]

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[localfile*]：待添加的本地文件名称。

*[remotefile*]：被添加的FTP服务器文件名称。

【使用指导】

只有成功登录FTP服务器后才能执行此项操作。

【举例】

\# 将本地a.txt文件内容添加到FTP服务器上的b.txt文件内容的后面。

ftp\> append a.txt b.txt

local: a.txt remote: b.txt

150 Connecting to port 50190

226 File successfully transferred

1657 bytes sent in 0.000736 seconds (2.15 Mbyte/s)

**FTP \-- FTP客户端配置命令 \-- ascii**

------------------------------------------------------------------------

**[ascii**]命令用来设置文件传输的模式为ASCII模式。

【命令】

**[ascii**]

【缺省情况】

文件传输模式为二进制模式。

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有成功登录FTP服务器后才能执行此项操作。

当设备作为FTP服务器时，使用的传输模式由FTP客户端决定。当设备作为FTP客户端时，使用的传输模式用户可通过命令行修改，缺省为二进制模式。

请使用二进制模式传输非文本文件，用ASCII模式传输文本文件。

【举例】

\# 设置数据传输的模式为ASCII模式。

ftp\> ascii

200 TYPE is now ASCII

【相关命令】

·**binary**

**FTP \-- FTP客户端配置命令 \-- binary**

------------------------------------------------------------------------

**[binary**]命令用来设置文件传输的模式为二进制模式（也称为流模式）。

【命令】

**[binary**]

【缺省情况】

文件传输模式为二进制模式。

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有成功登录FTP服务器后才能执行此项操作。

当设备作为FTP服务器时，使用的传输模式由FTP客户端决定。当设备作为FTP客户端时，使用的传输模式用户可通过命令行修改，缺省为二进制模式。

请使用二进制模式传输非文本文件，用ASCII模式传输文本文件。

【举例】

\# 设置文件传输类型为二进制模式。

ftp\> binary

200 TYPE is now 8-bit binary

【相关命令】

·**ascii**

**FTP \-- FTP客户端配置命令 \-- bye**

------------------------------------------------------------------------

**[bye**]命令用来断开与FTP服务器的连接，并退回到用户视图。如果设备与FTP服务器没有建立连接，则直接退回到用户视图。

【命令】

**[bye**]

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 终止与FTP服务器的连接，并退回到用户视图。

ftp\> bye

221-Goodbye. You uploaded 2 and downloaded 2 kbytes.

221 Logout.

\<Sysname\>

【相关命令】

·**quit**

**FTP \-- FTP客户端配置命令 \-- cd**

------------------------------------------------------------------------

**[cd**]命令用来切换FTP服务器上的工作路径，即访问FTP服务器上的另一目录。

【命令】

**[cd**[ { *directory* *\|* **..** \| **/** }]]

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[directory*]：指定目标工作路径。如果指定的工作路径不存在，则执行cd directory后保持当前工作路径不变。格式为*drive*:/*path*。*drive*和*path*参数的详细解释，请参见"基础配置指导"中的"文件系统管理"。如果没有给出*drive*信息，则表示当前工作路径下的文件夹或者子文件夹。

**[..**]：返回上一级目录，功能与**cdup**类似。如果当前工作路径已经是FTP根目录，则执行cd ..后保持当前工作路径不变。

**[/**]：返回FTP根目录。

【使用指导】

只有成功登录FTP服务器后才能执行此项操作。

用户可以访问的目录只能是FTP服务器对用户授权的目录。

【举例】

\# 切换工作路径到当前工作路径的logfile子目录下。

ftp\> cd logfile

250 OK. Current directory is /logfile

\# 切换工作路径到FTP根目录的folder子目录下。

ftp\> cd /folder

250 OK. Current directory is /folder

\# 切换工作路径到当前工作路径的上层目录下。

ftp\> cd ..

250 OK. Current directory is /

\# 切换工作路径到FTP根目录下。

ftp\> cd /

250 OK. Current directory is /

【相关命令】

·**cdup**

·**pwd**

**FTP \-- FTP客户端配置命令 \-- cdup**

------------------------------------------------------------------------

**[cdup**]命令用来退出FTP服务器的当前工作路径，并返回到FTP服务器的上一级目录。如果当前工作路径已经是FTP根目录，则执行该命令后，保持当前工作路径不变。

【命令】

**[cdup**]

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有成功登录FTP服务器后才能执行此项操作。

【举例】

\# 将工作路径改为上一级目录。

ftp\> pwd

257 \"/ftp/subdir\" is your current location

ftp\> cdup

250 OK. Current directory is /ftp

ftp\> pwd

257 \"/ftp\" is your current location

【相关命令】

·**cd**

·**pwd**

**FTP \-- FTP客户端配置命令 \-- close**

------------------------------------------------------------------------

**[close**]命令用来在不退出FTP客户端视图的前提下，断开与FTP服务器的连接。

【命令】

**[close**]

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有成功登录FTP服务器后才能执行此项操作。

【举例】

\# 断开与FTP服务器的连接，并保持在FTP客户端视图。

ftp\> close

221-Goodbye. You uploaded 0 and downloaded 0 kbytes.

221 Logout.

ftp\>

【相关命令】

·**disconnect**

**FTP \-- FTP客户端配置命令 \-- debug**

------------------------------------------------------------------------

**[debug**]命令用来切换FTP客户端调试信息开关状态。

【命令】

**[debug**]

【缺省情况】

FTP客户端调试信息开关处于关闭状态。

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

重复执行该命令，可以打开或者关闭FTP客户端调试信息开关。

【举例】

\# 切换FTP客户端调试信息开关状态。

ftp\> debug

Debugging on (debug=1).

ftp\> debug

Debugging off (debug=0).

\# 设备作为FTP客户端，成功登录后，打开设备的FTP客户端调试信息开关，下载FTP服务器当前工作路径下的a.txt文件。

ftp\> debug

Debugging on (debug=1).

ftp\> get a.txt

local: a.txt remote: a.txt

[\-\--\> EPRT \|2\|8::124\|50198\|]

200 PORT command successful

\-\--\> RETR a.txt

150 Connecting to port 50198

226 File successfully transferred

1569 bytes received in 0.0104 seconds (147.2 kbyte/s)

表1-3 debug命令显示信息描述表

字段

描述

\-\--\> EPRT \|2\|8::124\|50198\|

发出FTP指令，2表示所使用的地址结构协议族（1表示IPv4协议，2表示IPv6协议），8::124表示FTP服务器的IP地址，50198表示FTP服务器端口号

200 PORT command successful

收到的FTP应答码。200表示应答码，FTP应答码由RFC 959规定

\-\--\> RETR a.txt

发出FTP指令，下载文件a.txt

**FTP \-- FTP客户端配置命令 \-- delete**

------------------------------------------------------------------------

**[delete**]命令用来彻底删除FTP服务器上的指定文件。

【命令】

**[delete** *remotefile*]

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[remotefile*]：FTP服务器上的文件的文件名。

【使用指导】

只有成功登录FTP服务器后才能执行此项操作。

用户必须具有删除的权限才能执行该操作。

【举例】

\# 删除文件b.txt。

ftp\> delete b.txt

250 Deleted b.txt

**FTP \-- FTP客户端配置命令 \-- dir**

------------------------------------------------------------------------

**[dir**]命令用来查看FTP服务器当前工作路径下的所有子目录及文件的详细信息。

**[dir** *remotefile*]命令用来查看FTP服务器上指定目录或文件的详细信息。

**[dir** *remotefile* *localfile*]命令用来查看FTP服务器上指定目录或文件的详细信息，并把查看结果（找到的目录或文件的详细信息）保存在本地以*localfile*命名的文件中。

【命令】

**[dir** [ *remotefile* [ *localfile*  ]]]

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[remotefile*]：待查看的FTP服务器上的目录或文件名。

*[localfile*]：用于保存查询信息的本地文件的名称。

【使用指导】

只有成功登录FTP服务器后才能执行此项操作。

在FTP客户端视图下，**dir**命令等同于**ls**命令。

【举例】

\# 显示当前FTP服务器工作路径下的所有文件夹以及文件的信息。

ftp\> dir

150 Connecting to port 50201

-rwxr-xr-x    1 0          0                1481 Jul  7 15:36 a.txt

-rwxr-xr-x    1 0          0                   0 Sep 27  2010 base.bin

drwxr-xr-x    2 0          0                8192 Jul  2 14:33 diagfile

drwxr-xr-x    3 0          0                8192 Jul  7 15:21 ftp

-rwxr-xr-x    1 0          0                   0 Sep 27  2010 kernel.bin

drwxr-xr-x    2 0          0                8192 Jul  5 09:15 logfile

drwxr-xr-x    2 0          0                8192 Jul  2 14:33 seclog

-rwxr-xr-x    1 0          0            40808448 Jul  2 14:33 simware-cmw710-sys

tem-a1801.bin

-rwxr-xr-x    1 0          0                3050 Jul  7 12:26 startup.cfg

-rwxr-xr-x    1 0          0               54674 Jul  4 09:24 startup.mdb

-rwxr-xr-x    1 0          0                1481 Jul  7 12:34 x.cfg

226 11 matches total

\# 查看文件a.txt，并将查询结果保存在s.txt文件中。

ftp\> dir a.txt s.txt

output to local-file: s.txt ? [Y/Ny]

150 Connecting to port 50203

226-Glob: a.txt

查看s.txt文件的内容。

ftp\> bye

221-Goodbye. You uploaded 0 and downloaded 2 kbytes.

221 Logout.

\<Sysname\> more s.txt

-rwxr-xr-x    1 0          0                1481 Jul  7 12:34 a.txt

【相关命令】

·**ls**

**FTP \-- FTP客户端配置命令 \-- disconnect**

------------------------------------------------------------------------

**[disconnect**]命令用来在不退出FTP客户端视图的前提下，断开与FTP服务器的连接。

【命令】

**[disconnect**]

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有成功登录FTP服务器后才能执行此项操作。

【举例】

\# 断开与FTP服务器的连接，保持在FTP客户端视图。

ftp\> disconnect

221-Goodbye. You uploaded 0 and downloaded 0 kbytes.

221 Logout.

ftp\>

【相关命令】

·**close**

**FTP \-- FTP客户端配置命令 \-- display ftp client source**

------------------------------------------------------------------------

**[display** **ftp client source**]命令用来显示设备作为FTP客户端时的源地址的配置。

【命令】

**[display** **ftp client source**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示设备作为FTP客户端时的源地址的配置。

\<Sysname\> display ftp client source

The source IP address of the FTP client is 1.1.1.1.

The source IPv6 address of the FTP client is 2001::1.

**FTP \-- FTP客户端配置命令 \-- ftp**

------------------------------------------------------------------------

**[ftp**]命令用来登录FTP服务器，并进入FTP客户端视图。

【命令】

**[ftp**[ *ftp-server* [ *service-port*   **vpn-instance** *vpn-instance-name*  [ **dscp** *dscp-value* \| **source** { **interface** *interface-type* *interface-number* \| **ip** *source-ip-address* } ] ] \*]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ftp-server*]：FTP服务器的主机名或IP地址。其中，主机名为1～253个字符的字符串，不区分大小写，字符串仅可包含字母、数字、"-"、"\_"或"."。

*[service-port*]：远端设备提供FTP服务的TCP端口号，取值范围为0～65535，缺省值为21。

**[vpn-instance** *vpn-instance-name*]：指定FTP服务器所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示FTP服务器位于公网中。该参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[dscp** *dscp-value*]：指定设备发送的FTP报文中携带的DSCP优先级的取值，取值范围为0～63，缺省值为0。

**[source**[ { **interface** *interface-type* *interface-number* \| **ip** *source-ip-address* }]]：指定建立FTP连接时使用的源地址。其中：

·**interface***interface-type* *interface-number*：表示源接口的接口类型和接口编号。发送FTP协议报文时，设备将使用该接口下配置的主IP地址作为源地址。如果源接口下没有配置主地址，则不能建立连接。

·**ip***source-ip-address*：表示源IP地址。发送FTP协议报文时，设备将使用该IP地址作为源地址。该地址必须是设备上已配置的IP地址，否则不能建立连接。

【使用指导】

该命令仅适用于IPv4组网环境。

如果不指定任何参数，则只进入FTP客户端视图，不登录FTP服务器。

如果指定参数，系统会提示用户输入登录FTP服务器的用户名和密码。如果用户名和密码正确，则登录成功，并进入FTP客户端视图；否则，登录失败。

【举例】

\# 使用FTP方式，从当前设备Sysname登录到设备FTP Server（IP地址为192.168.0.211），并且FTP发送报文的源IP地址为192.168.0.212。

\<Sysname\>ftp 192.168.0.211 source ip 192.168.0.212

Press CTRL+C to abort.

Connected to 192.168.0.211 (192.168.0.211).

220 WFTPD 2.0 service (by Texas Imperial Software) ready for new user

User (192.168.0.211:(none)): abc

331 Give me your password, please

Password:

230 Logged in successfully

Remote system type is MSDOS.

ftp\>

**FTP \-- FTP客户端配置命令 \-- ftp client source**

------------------------------------------------------------------------

**[ftp client source**]命令用来在IPv4组网环境下配置FTP客户端发送的FTP报文的源地址。

**[undo ftp client source**]命令用来恢复缺省情况。

【命令】

**[ftp** **client** **source**[ { **interface** *interface-type interface-number* \| **ip** *source-ip-address* }]]

**[undo** **ftp** **client** **source**]

【缺省情况】

没有配置源地址，使用路由出接口的主IP地址作为设备发送FTP报文的源IP地址。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface*** interface-type interface-number*]：设置FTP传输使用的源接口，包括接口类型和接口编号，此接口下配置的主IP地址即为发送报文的源地址。请使用配置了主IP地址，并且状态为up的接口作为源接口，否则，文件传输失败。

**[ip** *source-ip-address*]：设置当前FTP客户端发送报文所使用的源IP地址。该地址必须是设备上已经配置的IP地址，并且地址所在接口状态为up，否则，文件传输失败。

【使用指导】

·多次执行本命令，最新的配置生效。

·使用本命令指定了源地址后，又在**ftp**命令中指定了源地址，则采用**ftp**命令中指定的源地址进行通信。

·本命令指定的源地址对所有的FTP传输有效，**ftp**命令指定的源地址只对当前的FTP传输有效。

【举例】

\# 配置设备发送FTP报文的源IP地址为192.168.20.222。

\<Sysname\> system-view

Sysname ftp client source ip 192.168.20.222

【相关命令】

·**ftp**

**FTP \-- FTP客户端配置命令 \-- ftp client ipv6 source**

------------------------------------------------------------------------

**[ftp client ipv6 source**]命令用来在IPv6组网环境下配置FTP客户端发送的FTP报文的源地址。

**[undo ftp client ipv6 source**]命令用来恢复缺省情况。

【命令】

**[ftp** **client** **ipv6 source**[ { **interface** *interface-type interface-number* \| **ipv6** *source-ipv6-address* }]]

**[undo** **ftp** **client** **ipv6 source**]

【缺省情况】

没有配置源地址，设备自动选择IPv6 FTP报文的源IPv6地址，具体选择原则请参见RFC 3484。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface*** interface-type interface-number*]：表示源接口的类型和编号，此接口下配置的IPv6地址即为发送报文的源地址。请使用状态为up的接口作为源接口，否则，文件传输失败。

**[ipv6 ***source-ipv6-address*]：设置当前FTP客户端发送报文所使用的源IPv6地址。该地址必须是设备上已经配置的IPv6地址，并且地址所在接口状态为up，否则，文件传输失败。

【使用指导】

·多次执行**ftp client** **ipv6 source**命令，最新的配置生效。

·使用该命令指定了源地址后，又在**ftp ipv6**命令中指定了源地址，则采用**ftp** **ipv6**命令中指定的源地址进行通信。

·本命令指定的源地址对所有的FTP传输有效，**ftp ipv6**命令指定的源地址只对当前的FTP传输有效。

【举例】

\# 配置设备发送的FTP报文的源IPv6地址为2000::1。

\<Sysname\> system－view

Sysname ftp client ipv6 source ipv6 2000::1

【相关命令】

·**ftp ipv6**

**FTP \-- FTP客户端配置命令 \-- ftp ipv6**

------------------------------------------------------------------------

**[ftp** **ipv6**]命令用来登录FTP服务器，并进入FTP客户端视图。

【命令】

**[ftp** **ipv6** [ *ftp-server* [ *service-port*   **vpn-instance** *vpn-instance-name*  [ **dscp** *dscp-value* \| **source** { **ipv6** *source-ipv6-address* \| **interface** *interface-type* *interface-number* } ] \*  **-i** *interface-type interface-number*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ftp-server*]：远端设备的IPv6地址或主机名。其中，主机名为1～253个字符的字符串，不区分大小写，字符串仅可包含字母、数字、"-"、"\_"或"."。

*[service-port*]：远端设备提供FTP服务的TCP端口号，取值范围为0～65535，缺省值为21。

**[dscp** *dscp-value*]：指定设备发送的IPv6 FTP报文中携带的DSCP优先级的取值，取值范围为0～63，缺省值为0。

**[source**[ [ *source-ipv6-address* \| **interface** *interface-type* *interface-number* }]]：指定建立IPv6 FTP连接时使用的源地址。其中：

·]**interface***interface-type* *interface-number*：当前FTP客户端连接所使用的源接口的接口类型和接口编号。此参数主要用于FTP服务器的地址是链路本地地址的情况，而且指定的出接口必需具有链路本地地址。（链路本地地址的介绍和配置请参见"三层技术-IP业务配置指导"中的"IPv6基础"）。

·**ipv6***source-ipv6-address*：当前FTP客户端连接所使用的源IPv6地址。该地址必须是设备上已配置的IPv6地址。

**[vpn-instance** *vpn-instance-name*]：指定目的端所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示目的端位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[-i** *interface-type* *interface-number*]：当前FTP客户端连接所使用的出接口的接口类型和接口编号。此参数主要用于FTP服务器的地址是链路本地地址的情况，而且指定的出接口必需具有链路本地地址。

【使用指导】

该命令仅适用于IPv6组网环境。

如果不指定任何参数，则只进入FTP客户端视图，不登录FTP服务器。

如果指定参数，系统会提示用户输入登录FTP服务器的用户名和密码。如果用户名和密码正确，则登录成功，并进入FTP客户端视图；否则，登录失败。

【举例】

\# 登录到IPv6地址为2000::154的FTP服务器。

\<Sysname\> ftp ipv6 2000::154

Press CTRL+C to abort.

Connected to 2000::154 (2000::154).

220 FTP service ready.

User (2000::154): root

331 Password required for root.

Password:

230 User logged in

Remote system type is H3C

**FTP \-- FTP客户端配置命令 \-- get**

------------------------------------------------------------------------

**[get**]命令用来下载FTP服务器上的文件，并将下载的文件存储在本地。

【命令】

**[get** *remotefile* [ *localfile* ]]

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[remotefile*]：需要下载的文件名称。

*[localfile*]：将文件下载到本地保存时使用的文件名称。

【使用指导】

只有成功登录FTP服务器后才能执行此项操作。

·如果要将文件保存到用户执行**ftp**命令时的当前工作路径，*localfile*只能是文件的名称或者不输入，形如a.cfg。当不使用该参数，将使用源文件名称作为本地文件名称保存。

·如果要将文件保存到用户执行**ftp**命令时的当前工作路径外的其它路径，则*localfile*必须是绝对路径形式，形如flash:/subdirectory/a.cfg，否则，命令执行失败。

【举例】

\# 下载a.txt文件，并以b.txt文件名保存到用户执行**ftp**命令时的当前工作路径。

ftp\> get a.txt b.txt

local: b.txt remote: a.txt

150 Connecting to port 47457

226 File successfully transferred

1569 bytes received in 0.00527 seconds (290.6 kbyte/s)

\# 下载a.txt文件，并以b.txt文件名保存到用户执行**ftp**命令时的当前工作路径的子文件夹test。

ftp\> get a.txt flash:/test/b.txt

local: flash:/test/b.txt remote: a.txt

150 Connecting to port 47457

226 File successfully transferred

1569 bytes received in 0.00527 seconds (290.6 kbyte/s)

\# 下载a.txt文件到备用主控板（所在槽号1）存储介质的根目录下，并以c.txt文件名保存。（分布式设备－独立运行模式）

ftp\> get a.txt slot1#flash:/c.txt

local: slot1#flash:/c.txt remote: a.txt

150 Connecting to port 47460

226 File successfully transferred

1569 bytes received in 0.0564 seconds (27.2 kbyte/s)

\# 下载a.txt文件到成员设备1存储介质的根目录下，并以c.txt文件名保存。（集中式IRF）

ftp\> get a.txt slot1#flash:/c.txt

local: slot1#flash:/c.txt remote: a.txt

150 Connecting to port 47460

226 File successfully transferred

1569 bytes received in 0.0564 seconds (27.2 kbyte/s)

\# 下载a.txt文件到成员设备1的1号主控板存储介质的根目录下，并以c.txt文件名保存。（分布式设备－IRF模式）

ftp\> get a.txt chassis1#slot1#flash:/c.txt

 local: chassis1#slot1#flash:/c.txt remote: a.txt

150 Connecting to port 47460

226 File successfully transferred

1569 bytes received in 0.0564 seconds (27.2 kbyte/s)

【相关命令】

·**put**

**FTP \-- FTP客户端配置命令 \-- help**

------------------------------------------------------------------------

**[help**]命令用来显示所有FTP客户端支持的命令的名字。

**[help** *command-name*]命令用来显示指定命令的帮助信息。

【命令】

**[help** [ *command-name* ]]

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[command-name*]：命令名。

【使用指导】

在FTP客户端视图下，**help**命令等同于**?**命令。

【举例】

\# 显示所有FTP客户端支持的命令的名字。

ftp\> help

Commands may be abbreviated.  Commands are:

\$                dir             mkdir           pwd             status

account          disconnect      mls             quit            struct

append           form            mode            quote           system

ascii            get             modtime         recv            sunique

bell             glob            mput            reget           tenex

binary           hash            newer           rstatus         trace

bye              help            nmap            rhelp           type

case             idle            nlist           rename          user

cd               image           ntrans          reset           umask

cdup             lcd             open            restart         verbose

chmod            ls              passive         rmdir           ?

close            macdef          prompt          runique

cr               mdelete         proxy           send

delete           mdir            sendport        site

debug            mget            put             size

\# 查看**dir**命令的帮助信息

ftp\> help dir

dir              list contents of remote directory

【相关命令】

·**?**

**FTP \-- FTP客户端配置命令 \-- lcd**

------------------------------------------------------------------------

**[lcd**]命令用来显示或切换FTP客户端本地的工作路径。

【命令】

**[lcd **[[ *directory* *\| **/*** ]]]

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[directory*]：表示本设备上的文件夹路径。请注意，存储介质名前面必须带"/"，形如"/flash:/logfile"。

**[/**]：表示本设备的根目录。

【使用指导】

执行**lcd**命令，不指定任何参数时，用来显示FTP客户端本地的当前工作路径。

**[lcd ***directory*]命令用来将FTP客户端本地的工作路径切换到指定路径。

**[lcd /**]命令用来将FTP客户端本地的工作路径切换到本设备的根目录。

【举例】

\# 显示FTP客户端本地的当前工作路径。

ftp\> lcd

Local directory now /flash:

\# 将FTP客户端本地的工作路径切换到flash:/logfile。

ftp\> lcd /flash:/logfile

Local directory now /flash:/logfile

**FTP \-- FTP客户端配置命令 \-- ls**

------------------------------------------------------------------------

**[ls**]命令用来查看FTP服务器当前工作路径下的所有子目录及文件的详细信息。

**[ls** *remotefile*]命令用来查看FTP服务器上指定目录或文件的详细信息。

**[ls** *remotefile* *localfile*]命令用来查看FTP服务器上指定目录或文件的详细信息，并把查看结果（找到的目录或文件的详细信息）保存在本地以*localfile*命名的文件中。

【命令】

**[ls** *remotefile*  *localfile*  ]

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[remotefile*]：待查看的FTP服务器上的目录或文件名。

*[localfile*]：用于保存查询信息的本地文件的名称。

【使用指导】

只有成功登录FTP服务器后才能执行此项操作。

在FTP客户端视图下，**ls**命令等同于**dir**命令。

【举例】

\# 显示当前FTP服务器工作路径下的所有文件夹以及文件的信息。

ftp\> ls

150 Connecting to port 50201

-rwxr-xr-x    1 0          0                1481 Jul  7 15:36 a.txt

-rwxr-xr-x    1 0          0                   0 Sep 27  2010 base.bin

drwxr-xr-x    2 0          0                8192 Jul  2 14:33 diagfile

drwxr-xr-x    3 0          0                8192 Jul  7 15:21 ftp

-rwxr-xr-x    1 0          0                   0 Sep 27  2010 kernel.bin

drwxr-xr-x    2 0          0                8192 Jul  5 09:15 logfile

drwxr-xr-x    2 0          0                8192 Jul  2 14:33 seclog

-rwxr-xr-x    1 0          0            40808448 Jul  2 14:33 simware-cmw710-sys

tem-a1801.bin

-rwxr-xr-x    1 0          0                3050 Jul  7 12:26 startup.cfg

-rwxr-xr-x    1 0          0               54674 Jul  4 09:24 startup.mdb

-rwxr-xr-x    1 0          0                1481 Jul  7 12:34 x.cfg

226 11 matches total

\# 查看文件a.txt，并将查询结果保存在s.txt文件中。

ftp\> ls a.txt s.txt

output to local-file: s.txt ? [Y/Ny]

150 Connecting to port 50203

226-Glob: a.txt

查看s.txt文件的内容。

ftp\> bye

221-Goodbye. You uploaded 0 and downloaded 2 kbytes.

221 Logout.

\<Sysname\> more s.txt

-rwxr-xr-x    1 0          0                1481 Jul  7 12:34 a.txt

【相关命令】

·**dir**

**FTP \-- FTP客户端配置命令 \-- mkdir**

------------------------------------------------------------------------

**[mkdir**]命令用来在FTP服务器上当前工作路径下创建子目录。

【命令】

**[mkdir** *directory*]

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[directory*]：待创建的目录名称。

【使用指导】

只有成功登录FTP服务器后才能执行此项操作。

用户必须具有创建的权限才能执行此项操作。

【举例】

\# 在FTP服务器的当前工作路径下创建子目录newdir。

ftp\> mkdir newdir

257 \"newdir\" : The directory was successfully created

**FTP \-- FTP客户端配置命令 \-- newer**

------------------------------------------------------------------------

**[newer**]命令用来更新本地文件。

【命令】

**[newer** *remotefile* [ *localfile* ]]

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[remotefile*]：目标文件名称。

*[localfile*]：需要更新的本地文件名称。

【使用指导】

只有成功登录FTP服务器后才能执行此项操作。

如果本地文件不存在，一律视为目标文件比本地新，即本地文件需要更新。

如果目标文件不比本地文件新，则不更新本地文件。

【举例】

\# FTP服务器的文件a.txt比本地的要新，更新本地文件。

ftp\> newer a.txt

local: a.txt remote: a.txt

150 Connecting to port 63513

226 File successfully transferred

1573 bytes received in 0.0293 seconds (52.3 kbyte/s)

**FTP \-- FTP客户端配置命令 \-- open**

------------------------------------------------------------------------

**[open**]命令用来在FTP客户端视图下，登录FTP服务器。

【命令】

**[open** *server-address* [ *service-port* ]]

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[server-address*]：FTP服务器的IP地址（IPv4或IPv6地址）或主机名。

*[service-port*]：远端设备提供FTP服务的TCP端口号，取值范围为0～65535，缺省值为21。

【使用指导】

登录时，系统会提示用户输入登录用户名和密码。如果用户名和密码正确，则登录成功；否则，登录失败。

如果当前已经登录到FTP服务器，则不能直接使用**open**命令连接到其他FTP服务器，需要中断与当前FTP服务器的连接后再重新连接。

【举例】

\# 在FTP客户端视图下，登录FTP服务器（IP地址为192.168.40.7）。

\<Sysname\> ftp

ftp\> open 192.168.40.7

Press CTRL+C to abort.

Connected to 192.168.40.7 (192.168.40.7).

220 FTP service ready.

User (192.168.40.7:(none)): root

331 Password required for root.

Password:

230 User logged in.

Remote system type is H3C.

ftp\>

**FTP \-- FTP客户端配置命令 \-- passive**

------------------------------------------------------------------------

**[passive**]命令用来切换FTP数据传输的主被动方式。

【命令】

**[passive**]

【缺省情况】

数据传输的方式为被动方式。

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

数据传输的方式分为主动方式和被动方式：

·主动方式是指在建立数据连接时由FTP服务器主动发起连接请求。

·被动方式是指在建立数据连接时由FTP客户端主动发起连接请求。

重复执行该命令，可以FTP数据传输方式设置为主动方式或者被动方式。

该命令主要与防火墙功能配合使用，用来限制私网用户和公网用户之间建立FTP会话。

【举例】

\# 切换数据传输的主被动方式。

ftp\> passive

Passive mode on.

ftp\> passive

Passive mode off.

**FTP \-- FTP客户端配置命令 \-- put**

------------------------------------------------------------------------

**[put**]命令用来将FTP客户端本地的文件上传到FTP服务器。

【命令】

**[put** *localfile* [ *remotefile* ]]

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[localfile*]：待上传的本地文件名称。

*[remotefile*]：文件上传完成后，在FTP服务器上保存时使用的文件名称。如果用户没有指定FTP服务器上的文件名，则系统缺省认为此文件名与本地文件名相同。

【使用指导】

只有成功登录FTP服务器后才能执行此项操作。

·如果要将用户执行**ftp**命令时的当前工作路径下的某文件上传，*localfile*只能是文件的名称，形如a.cfg。

·如果要将用户执行**ftp**命令时的当前工作路径外的其它文件上传，则*localfile*必须是绝对路径形式，形如flash:/subdirectory/a.cfg，否则，命令执行失败。

【举例】

\# 上传用户执行**ftp**命令时的当前工作路径下的a.txt文件，并以b.txt文件名保存。

ftp\> put a.txt b.txt

local: a.txt remote: b.txt

150 Connecting to port 47461

226 File successfully transferred

1569 bytes sent in 0.000671 seconds (2.23 Mbyte/s)

\# 上传用户执行**ftp**命令时的当前工作路径下子文件夹test下的a.txt文件，并以b.txt文件名保存。

ftp\> put flash:/test/a.txt b.txt

local: flash:/test/a.txt remote: b.txt

150 Connecting to port 47461

226 File successfully transferred

1569 bytes sent in 0.000671 seconds (2.23 Mbyte/s)

\# 上传备用主控板（假设槽位号为1）存储介质根目录下的a.txt文件，并以b.txt文件名保存。（分布式设备－独立运行模式）

ftp\> put slot1#flash:/test/a.txt b.txt

local: slot1#flash:/test/a.txt remote: b.txt

150 Connecting to port 47461

226 File successfully transferred

1569 bytes sent in 0.000671 seconds (2.23 Mbyte/s)

\# 上传成员设备2存储介质根目录下的a.txt文件，并以b.txt文件名保存。（集中式IRF设备）

ftp\> put slot2#flash:/test/a.txt b.txt

local: slot2#flash:/test/a.txt remote: b.txt

150 Connecting to port 47461

226 File successfully transferred

1569 bytes sent in 0.000671 seconds (2.23 Mbyte/s)

\# 上传成员设备1的1号主控板存储介质根目录下的a.txt文件，并以b.txt文件名保存。（分布式设备－IRF模式）

ftp\> put chassis1#slot1#flash:/test/a.txt b.txt

local: chassis1#slot1#flash:/test/a.txt remote: b.txt

150 Connecting to port 47461

226 File successfully transferred

1569 bytes sent in 0.000671 seconds (2.23 Mbyte/s)

【相关命令】

·**get**

**FTP \-- FTP客户端配置命令 \-- pwd**

------------------------------------------------------------------------

**[pwd**]命令用来显示当前用户正在访问的FTP服务器上的路径。

【命令】

**[pwd**]

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有成功登录FTP服务器后才能执行此项操作。

【举例】

\# 显示当前用户正在访问的FTP服务器上的路径。

ftp\> cd subdir

250 OK. Current directory is /subdir

ftp\> pwd

257 \"/subdir\" is your current location

**FTP \-- FTP客户端配置命令 \-- quit**

------------------------------------------------------------------------

**[quit**]命令用来断开与FTP服务器的连接，并退回到用户视图。

【命令】

**[quit**]

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 终止与FTP服务器的连接，并退回到用户视图。

ftp\> quit

221-Goodbye. You uploaded 0 and downloaded 0 kbytes.

221 Logout.

\<Sysname\>

【相关命令】

·**bye**

**FTP \-- FTP客户端配置命令 \-- reget**

------------------------------------------------------------------------

**[reget**]命令用来实现断点续传。

【命令】

**[reget***remotefile* [ *localfile* ]]

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[remotefile*]：目标文件名称。

*[localfile*]：内容保存不完整的本地文件名称。

【使用指导】

只有成功登录FTP服务器后才能执行此项操作。

网络故障或者存储空间不足，可能导致正在进行的下载操作终止，下载的文件内容不完整。当网络故障排除或者存储空间恢复后，可执行**reget**命令继续下载文件剩余的内容。

【举例】

\# 获取因传输中断而不完整的本地文件s.bin的剩余内容。

ftp\> reget s.bin

local: s.bin remote: s.bin

350 Restarting at 1749706

150-Connecting to port 47429

150 38143.3 kbytes to download

226 File successfully transferred

39058742 bytes received in 66.2 seconds (576.1 kbyte/s)

**FTP \-- FTP客户端配置命令 \-- rename**

------------------------------------------------------------------------

**[rename**]命令用来重命名文件。

【命令】

**[rename** \*[oldfilename* *newlfilename* ] ]

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[oldfilename*]：原文件名。

*[newfilename*]：新文件名。

【使用指导】

只有成功登录FTP服务器后才能执行此项操作。

【举例】

\# 将文件a.txt改名为b.txt。

方法一：

ftp\> rename

(from-name) a.txt

(to-name) b.txt

350 RNFR accepted - file exists, ready for destination

250 File successfully renamed or moved

方法二：

ftp\> rename a.txt

(to-name) b.txt

350 RNFR accepted - file exists, ready for destination

250 File successfully renamed or moved

方法三：

ftp\> rename a.txt b.txt

350 RNFR accepted - file exists, ready for destination

250 File successfully renamed or moved

**FTP \-- FTP客户端配置命令 \-- reset**

------------------------------------------------------------------------

**[reset**]命令用来清除缓存中FTP服务器端发送回来的命令应答。

【命令】

**[reset**]

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 清除缓存中FTP服务器端发送回来的命令应答。

ftp\> reset

**FTP \-- FTP客户端配置命令 \-- restart**

------------------------------------------------------------------------

**[restart**]命令用来指定重传点。

【命令】

**[restart** *marker*]

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[marker*]：重传点，从文件首部开始的偏移量，单位为字节。

【使用指导】

只有成功登录FTP服务器后才能执行此项操作。

不同FTP服务器对本命令的支持情况可能不同，请以FTP服务器的实际情况为准。

【举例】

\# 设置重传点的偏移量为2字节，将本地文件h.c（大小82字节）上传。

ftp\> restart 2

restarting at 2. execute get, put or append to initiate transfer

ftp\> put h.c h.c

local: h.c remote: h.c

350 Restart position accepted (2).

150 Ok to send data.

226 File receive OK.

80 bytes sent in 0.000445 seconds (175.6 kbyte/s)

ftp\> dir

150 Here comes the directory listing.

-rw-r\--r\--    1 0        0              80 Jul 18 02:58 h.c

**FTP \-- FTP客户端配置命令 \-- rhelp**

------------------------------------------------------------------------

**[rhelp**]命令用来显示FTP服务器支持的FTP相关协议命令字。

**[rhelp** *protocol*-*command*]命令用来显示FTP服务器支持的FTP相关协议命令字的帮助信息。

【命令】

**[rhelp** [ *protocol*-*command* ]]

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[protocol*-*command*]：FTP协议命令字。

【使用指导】

只有成功登录FTP服务器后才能执行此项操作。

【举例】

\# 查看FTP服务器支持的FTP相关协议命令字。

ftp\> rhelp

214-The following FTP commands are recognized

 USER PASS NOOP QUIT SYST TYPE

 HELP CWD  XCWD PWD  CDUP XCUP

 XPWD LIST NLST MLSD PORT EPRT

 PASV EPSV REST RETR STOR APPE

 DELE MKD  XMKD RMD  XRMD ABOR

 SIZE RNFR RNTO

4 UNIX Type: L8

表1-4 rhelp命令显示信息描述表

字段

描述

214-The following FTP commands are recognized

以下是可用的FTP命令字列表

USER

用户名，对应FTP客户端视图下的xx命令

PASS

用户口令

NOOP

空操作，表示当服务器收到无效命令时，不做任何操作

QUIT

退出

SYST

显示系统参数

TYPE

请求类型

HELP

帮助

CWD

改变当前工作路径

XCWD

扩展命令，含义同CWD

PWD

打印工作路径

CDUP

改变目录到父级目录

XCUP

扩展命令，含义同CDUP

XPWD

扩展命令，含义同PWD

LIST

列出文件

NLST

列出文件简单描述

MLSD

列出文件内容

PORT

主动模式（IPv4）

EPRT

主动模式（IPv6）

PASV

被动模式（IPv4）

EPSV

被动模式（IPv6）

REST

重启动

RETR

下载文件

STOR

上传文件

APPE

追加上传

DELE

删除文件

MKD

创建文件夹

XMKD

扩展命令，含义同MKD

RMD

删除文件夹

XRMD

扩展命令，含义同RMD

ABOR

中断传输

SIZE

获取文件的传输大小

RNFR

需要重命名的文件的原名称

RNTO

需要重命名的文件的新名称

**FTP \-- FTP客户端配置命令 \-- rmdir**

------------------------------------------------------------------------

**[rmdir**]命令用来彻底删除FTP服务器上指定的目录。

【命令】

**[rmdir** *directory*]

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[directory*]：FTP服务器上的目录名。

【使用指导】

只有成功登录FTP服务器后才能执行此项操作。

用户必须具有删除的权限才能执行此项操作。

需要注意的是：

·被删除的目录必须为空目录（即删除目录前，必须先删除该目录下的所有文件及子目录，文件的删除请参见**delete**命令）。

·成功执行**rmdir**命令后，FTP服务器的回收站中原来属于该文件夹的文件会自动被彻底删除。

【举例】

\# 删除空目录subdir1。

ftp\>rmdir subdir1

250 The directory was successfully removed

【相关命令】

·**delete**

**FTP \-- FTP客户端配置命令 \-- rstatus**

------------------------------------------------------------------------

**[rstatus**]命令用来显示FTP服务器的状态。

**[rstatus***remotefile*]命令用来显示FTP服务器上指定目录或文件的详细信息。

【命令】

**[rstatus** \*[remotefile* ]]

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[remotefile*]：待查询的FTP服务器上的目录或文件名。

【使用指导】

只有成功登录FTP服务器后才能执行此项操作。

不同FTP服务器对本命令的支持情况可能不同，请以FTP服务器的实际情况为准。

【举例】

\# 显示FTP服务器状态。

ftp\> rstatus

211-FTP server status:

     Connected to 192.168.20.177

     Logged in as root

     TYPE: ASCII

     No session bandwidth limit

     Session timeout in seconds is 300

     Control connection is plain text

     Data connections will be plain text

     At session startup, client count was 1

     vsFTPd 2.0.6 - secure, fast, stable

211 End of status

表1-5 rstatus命令显示信息描述表

字段

描述

211-FTP server status:

211：FTP命令字；整个字段表示FTP服务器状态信息开始

Connected to 192.168.20.177

连接的FTP客户端IP地址：192.168.20.177

Logged in as root

登入的用户名：root

TYPE: ASCII

文件传输模式：ASCII

No session bandwidth limit

无带宽限制

Session timeout in seconds is 300

超时时间：300，单位为秒

Control connection is plain text

控制连接类型：纯文本

Data connections will be plain text

数据连接类型：纯文本

At session startup, client count was 1

FTP客户端连接数：1

vsFTPd 2.0.6 - secure, fast, stable

FTP版本号：2.0.6；可靠，快速，稳定

211 End of status

FTP服务器状态信息结束

\# 查看文件a.txt。

ftp\> rstatus a.txt

213-Status follows:

-rw-r\--r\--    1 0        0              80 Jul 18 02:58 a.txt

213 End of status

表1-6 rstatus命令显示指定文件信息描述表

字段

描述

213-Status follows:

213：FTP命令字；整个字段表示文件信息开始

-rw-r\--r\--

第一位表示文件类型：

·-：普通文件

·b：块设备文件

·c：字符设备文件

·d：目录

·l：符号连接文件

·p：命名管道文件

·s：socket文件

第二位到第十位分为3组，每组3个字符，分别表示所有者、组和其他用户的访问权限：

·-：没有对应权限

·r：有读权限

·w：有写权限

·x：有执行权限

1

表示文件的连接数

0

文件所有者的名字

0

文件所有者的组名

80

文件大小，单位为字节

Jul 18 02:58

文件最近一次修改的日期和时间

a.txt

文件名

213 End of status

文件信息结束

**FTP \-- FTP客户端配置命令 \-- status**

------------------------------------------------------------------------

**[status**]命令用来显示当前FTP状态。

【命令】

**[status**]

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 显示当前FTP状态。

ftp\> status

Connected to 192.168.1.56.

No proxy connection.

Not using any security mechanism.

Mode: stream; Type: ascii; Form: non-print; Structure: file

Verbose: on; Bell: off; Prompting: on; Globbing: off

Store unique: off; Receive unique: off

Case: off; CR stripping: on

Ntrans: off

Nmap: off

Hash mark printing: off; Use of PORT cmds: on

表1-7 status命令显示信息描述表

字段

描述

Connected to 192.168.1.56.

连接到的FTP服务器IP地址

No proxy connection.

不使用代理连接

Not using any security mechanism.

不使用安全机制

Mode: stream; Type: ascii; Form: non-print; Structure: file

文件传输模式：数据流；类型：ASCII；格式：非打印；组织结构：文件

Verbose: on; Bell: off; Prompting: on; Globbing: off

显示调试信息；操作完成后无蜂鸣提示；多文件操作时不需要每个文件进行确认；不能自动匹配文件名

Store unique: off; Receive unique: off

FTP服务器文件名唯一；本地接收文件名唯一

Case: off; CR stripping: on

不支持一次获取多个文件；文本环境下下载文件时，将"\\r"删除

Ntrans: off

不使用输入输出传输表

Nmap: off

文件名不使用输入输出映射模板

Hash mark printing: off; Use of PORT cmds: on

不以"\#"号结尾；使用"PORT"命令字作为数据传输连接

**FTP \-- FTP客户端配置命令 \-- system**

------------------------------------------------------------------------

**[system**]命令用来显示FTP服务器的系统信息。

【命令】

**[system**]

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有成功登录FTP服务器后才能执行此项操作。

【举例】

\# 显示FTP服务器的系统信息。

ftp\> system

5 UNIX Type: L8

**FTP \-- FTP客户端配置命令 \-- user**

------------------------------------------------------------------------

**[user**]命令用来在成功登录FTP服务器后，使用其他用户身份重新登录当前访问的FTP服务器。

【命令】

**[user** *username* [ *password* ]]

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[username*]：其他的登录用户名。

*[password*]：登录密码。

【使用指导】

只有成功登录FTP服务器后才能执行此项操作。

在使用该命令前，必须事先在FTP服务器上设置相应的用户名和密码，否则将导致登录失败，FTP连接关闭。

【举例】

\# 用户已经登录FTP服务器，现以新身份（用户名ftp，密码123456）重新登录当前FTP服务器。

方法一：

ftp\> user ftp 123456

331 Password required for ftp.

230 User logged in.

方法二：

ftp\> user ftp

331 Password required for ftp.

Password:

230 User logged in.

**FTP \-- FTP客户端配置命令 \-- verbose**

------------------------------------------------------------------------

**[verbose**]命令用来允许或者禁止显示FTP操作过程中的详细信息。

【命令】

**[verbose**]

【缺省情况】

允许显示FTP操作过程中的详细信息。

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本配置只对当前会话生效。当用户重新登录后，本命令将恢复到缺省情况。

【举例】

\# 禁止显示FTP操作过程中的详细信息时，执行get操作。

ftp\> verbose

Verbose mode off.

ftp\> get a.cfg 1.cfg

\# 允许显示FTP操作过程中的详细信息时，执行get操作。

ftp\> verbose

Verbose mode on.

ftp\> get a.cfg 2.cfg

227 Entering Passive Mode (192,168,1,58,68,14)

150-Accepted data connection

150 The computer is your friend. Trust the computer

226 File successfully transferred

3796 bytes received in 0.00762 seconds (486.5 kbyte/s)

**FTP \-- FTP客户端配置命令 \-- ?**

------------------------------------------------------------------------

**[?**]命令用来显示所有FTP客户端支持命令的名字。

**[?** *command-name*]命令用来显示指定命令的帮助信息。

【命令】

**[?** [ *command-name* ]]

【视图】

FTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[command-name*]：命令名。

【使用指导】

在FTP客户端视图下，**?**命令等同于**help**命令。

【举例】

\# 显示FTP客户端支持的所有命令的名字。

ftp\> ?

Commands may be abbreviated.  Commands are:

\$                dir             mkdir           pwd             status

account          disconnect      mls             quit            struct

append           form            mode            quote           system

ascii            get             modtime         recv            sunique

bell             glob            mput            reget           tenex

binary           hash            newer           rstatus         trace

bye              help            nmap            rhelp           type

case             idle            nlist           rename          user

cd               image           ntrans          reset           umask

cdup             lcd             open            restart         verbose

chmod            ls              passive         rmdir           ?

close            macdef          prompt          runique

cr               mdelete         proxy           send

delete           mdir            sendport        site

debug            mget            put             size

\# 查看**dir**命令的帮助信息

ftp\> ? dir

dir              list contents of remote directory

【相关命令】

·**help**

\

**TFTP \-- TFTP配置命令 \-- tftp**

------------------------------------------------------------------------

**[tftp**]命令用来在IPv4组网环境下执行下列操作：

·下载文件：将TFTP服务器上的指定源文件下载到本地。

·上传文件：将本地的指定源文件上传到TFTP服务器。

【命令】

**[tftp ***tftp-server *[{ **get** \| **put** \| **sget** } *source-filename* [ *destination-filename* ] ]] **vpn-instance** *vpn-instance-name*  [ **dscp** *dscp-value* \| **source** { **interface** *interface-type interface-number* \| **ip** *source-ip-address* } ] \*

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[tftp-server*]：TFTP服务器的IP地址或主机名。其中，主机名为1～253个字符的字符串，不区分大小写，字符串仅可包含字母、数字、"-"、"\_"或"."。

**[get**]：执行下载文件操作。执行该操作时，设备直接将文件保存到存储介质中。如果下载前存储介质中已有同名文件，则先删除存储介质中的已有文件，再下载。如果下载失败，将导致已有文件被删除，不可恢复，因此，不安全。

**[put**]：执行上传文件操作。

**[sget**]：执行安全下载文件操作。执行该操作时，设备会先将文件保存到内存，保存成功后，再拷贝到存储介质中，并删除内存中的文件。比**get**方式更加安全。

*[source-filename*]：源文件名，为1～255个字符的字符串，不区分大小写。

*[destination-filename*]：目标文件名，为1～255个字符的字符串，不区分大小写。如果不指定该参数，则使用源文件名作为目标文件名。

**[vpn-instance** *vpn-instance-name*]：指定TFTP服务器所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定该参数，则表示TFTP服务器位于公网中。该参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[dscp** *dscp-value*]：指定设备发送的TFTP报文中携带的DSCP优先级的取值，取值范围为0～63，缺省值为0。

**[source**]：发送的TFTP报文的源IP地址。不指定该参数时，则使用路由出接口的主IP地址作为发送的TFTP报文的源IP地址。

·**interface*** interface-type interface-number*：表示源接口的类型和编号，此接口下配置的主IP地址将作为设备发送的TFTP报文的源IP地址。请使用配置了主IP地址，并且状态为up的接口作为源接口，否则，文件传输失败。

·**ip ***source-ip-address***：**源IP地址，该地址将作为设备发送的TFTP报文的源IP地址。该地址必须是设备上已经配置的IP地址，并且地址所在接口状态为up，否则，文件传输失败。

【使用指导】

·使用**tftp** **client** **source**命令指定了源地址后，又在**tftp**命令中指定了源地址，则采用**tftp**命令中指定的源地址进行通信。

·**tftp** **client** **source**命令指定的源地址对所有的TFTP传输有效，**tftp**命令指定的源地址只对当前的TFTP传输有效。

【举例】

\# 将TFTP服务器上的new.bin文件下载到本地存储设备。TFTP服务器的IP地址为192.168.1.1，下载到本地后以文件名new.bin保存。

\<Sysname\> tftp 192.168.1.1 get new.bin

Press CTRL+C to abort.

   % Total    % Received % Xferd  Average Speed   Time    Time     Time   Current

                                  Dload  Upload   Total   Spent    Left   Speed

100 13.9M  100 13.9M    0     0  1206k      0  0:00:11  0:00:11  \--:\--:\-- 1206k

Writing file\...Done.

\<System\>

表2-1 tftp命令显示信息描述表

字段

描述

%

文件传输的进度百分比

Total

要传输的文件大小，单位为字节

%

下载时已接收文件大小与文件总大小的百分比

Received

下载时已接收的文件大小，单位为字节

%

上传时已发送文件大小与文件总大小的百分比

Xferd

上传时已发送的文件大小，单位为字节

Average Dload

平均下载速度，单位为字节/秒

Speed Upload

平均上传速度，单位为字节/秒

Time Total

文件传输时已花费时间和剩余时间的总和，单位为秒

Time Spent

文件传输时已花费时间，单位为秒

Time Left

完成文件传输，还需要的时间，单位为秒

Current Speed

文件传输时的当前速度，单位为字节/秒

Writing file

正在将文件保存到存储介质中，成功会显示Done，失败显示Failed。执行get和sget操作时会显示该字段

【相关命令】

·**tftp client source**

**TFTP \-- TFTP配置命令 \-- tftp client source**

------------------------------------------------------------------------

**[tftp client source**]命令用来在IPv4组网环境下配置TFTP客户端发送的TFTP报文的源地址。

**[undo tftp client source**]命令用来恢复缺省情况。

【命令】

**[tftp** **client** **source**[ { **interface** *interface-type interface-number* \| **ip** *source-ip-address* }]]

**[undo** **tftp** **client** **source**]

【缺省情况】

没有配置源地址，使用路由出接口的主IP地址作为设备发送TFTP报文的源IP地址。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface*** interface-type interface-number*]：设置TFTP传输使用的源接口，包括接口类型和接口编号，此接口下配置的主IP地址即为发送报文的源地址。请使用配置了主IP地址，并且状态为up的接口作为源接口，否则，文件传输失败。

**[ip** *source-ip-address*]：设置当前TFTP客户端发送报文所使用的源IP地址。该地址必须是设备上已经配置的IP地址，并且地址所在接口状态为up，否则，文件传输失败。

【使用指导】

·多次执行本命令，最新的配置生效。

·使用本命令指定了源地址后，又在**tftp**命令中指定了源地址，则采用**tftp**命令中指定的源地址进行通信。

·本命令指定的源地址对所有的TFTP传输有效，**tftp**命令指定的源地址只对当前的TFTP传输有效。

【举例】

\# 配置设备发送TFTP报文的源IP地址为192.168.20.222。

\<Sysname\> system-view

Sysname tftp client source ip 192.168.20.222

【相关命令】

·**tftp**

**TFTP \-- TFTP配置命令 \-- tftp ipv6**

------------------------------------------------------------------------

**[tftp** **ipv6**]命令用来在IPv6组网环境下执行下列操作：

·下载文件：将TFTP服务器上的指定源文件下载到本地。

·上传文件：将本地的指定源文件上传到TFTP服务器。

【命令】

**[tftp ipv6 ***tftp-server *[ **-i** *interface-type interface-number*  { **get** \| **put** \| **sget** } *source-filename*  *destination-filename*   **vpn-instance** *vpn-instance-name*  [ **dscp** *dscp-value* \| **source** { **interface** *interface-type interface-number* \| **ipv6** *source-ipv6-address* } ] \*]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[tftp-server*]：TFTP服务器的IPv6地址或主机名。其中，主机名为1～253个字符的字符串，不区分大小写，字符串仅可包含字母、数字、"-"、"\_"或"."。

**[-i** *interface-type interface-number*]：表示出接口的接口类型和接口编号。如果指定的TFTP服务器的地址是链路本地地址的情况，则必须指定出接口而且指定的出接口必须具有链路本地地址（链路本地地址的介绍和配置请参见"三层技术-IP业务配置指导"中的"IPv6基础"）。

**[get**]：执行下载文件操作。执行该操作时，设备直接将文件保存到存储介质中。如果下载前存储介质中已有同名文件，则先删除存储介质中的已有文件，再下载。如果下载失败，将导致已有文件被删除，不可恢复，因此，不安全。

**[put**]：执行上传文件操作。

**[sget**]：执行安全下载文件操作。执行该操作时，设备会先将文件保存到内存，保存成功后，再拷贝到存储介质中，并删除内存中的文件。比**get**方式更加安全。

*[source-filename*]：源文件的名称，为1～255个字符的字符串，不区分大小写。

*[destination-filename*]：目的文件的名称，为1～255个字符的字符串，不区分大小写。如果不指定该参数，则目的文件的名称与源文件的名称相同。

**[vpn-instance** *vpn-instance-name*]：指定目的主机所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示目的主机位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[dscp** *dscp-value*]：指定设备发送的IPv6 TFTP报文中携带的DSCP优先级的取值，取值范围为0～63，缺省值为0。

**[source**]：发送的IPv6 TFTP报文的源地址。不指定该参数时，设备自动选择报文的源IPv6地址，具体选择原则请参见RFC 3484。

·**interface*** interface-type interface-number*：表示源接口的类型和编号，此接口下配置的IPv6地址将作为设备发送的TFTP报文的源IPv6地址。请使用状态为up的接口作为源接口，否则，文件传输失败。

·**ipv6 ***source-ipv6-address***：**源IPv6地址，该地址将作为设备发送的TFTP报文的源IPv6地址。该地址必须是设备上已经配置的IPv6地址，并且地址所在接口状态为up，否则，文件传输失败。

【使用指导】

·使用**tftp client ipv6 source**命令指定了源地址后，又在**tftp ipv6**命令中指定了源地址，则采用**tftp** **ipv6**命令中指定的源地址进行通信。

·**tftp client ipv6 source**命令指定的源地址对所有的TFTP传输有效，**tftp ipv6**命令指定的源地址只对当前的TFTP传输有效。

【举例】

\# 将TFTP服务器上的new.bin文件下载到本地存储设备。TFTP服务器的IPv6地址为2001::1，下载到本地之后以文件名new.bin保存。

\<Sysname\> tftp ipv6 2001::1 get new.bin new.bin

Press CTRL+C to abort.

   % Total    % Received % Xferd  Average Speed   Time    Time     Time   Current

                                  Dload  Upload   Total   Spent    Left   Speed

100 13.9M  100 13.9M    0     0  1206k      0  0:00:11  0:00:11  \--:\--:\-- 1206k

Writing file\...Done.

本命令显示信息的详细描述请参见 表2-1(?-1155661038#_Ref300298608)。

**TFTP \-- TFTP配置命令 \-- tftp client ipv6 source**

------------------------------------------------------------------------

**[tftp client ipv6 source**]命令用来在IPv6组网环境下配置TFTP客户端发送的TFTP报文的源地址。

**[undo tftp client ipv6 source**]命令用来恢复缺省情况。

【命令】

**[tftp** **client** **ipv6 source**[ { **interface** *interface-type interface-number* \| **ipv6** *source-ipv6-address* }]]

**[undo** **tftp** **client** **ipv6 source**]

【缺省情况】

没有配置源地址，设备自动选择IPv6 TFTP报文的源IPv6地址，具体选择原则请参见RFC 3484。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface*** interface-type interface-number*]：表示源接口的类型和编号，此接口下配置的IPv6地址即为发送报文的源地址。请使用状态为up的接口作为源接口，否则，文件传输失败。

**[ipv6 ***source-ipv6-address*]：设置当前TFTP客户端发送报文所使用的源IPv6地址。该地址必须是设备上已经配置的IPv6地址，并且地址所在接口状态为up，否则，文件传输失败。

【使用指导】

·多次执行**tftp client ipv6 source**命令，最新的配置生效。

·使用该命令指定了源地址后，又在**tftp ipv6**命令中指定了源地址，则采用**tftp** **ipv6**命令中指定的源地址进行通信。

·本命令指定的源地址对所有的TFTP传输有效，**tftp ipv6**命令指定的源地址只对当前的TFTP传输有效。

【举例】

\# 配置设备发送的TFTP报文的源IPv6地址为2000::1。

\<Sysname\> system－view

Sysname tftp client ipv6 source ipv6 2000::1

【相关命令】

·**tftp ipv6**

**TFTP \-- TFTP配置命令 \-- tftp-server acl**

------------------------------------------------------------------------

**[tftp-server acl**]命令用来在IPv4组网环境下使用ACL限制设备可访问哪些TFTP服务器。

**[undo tftp-server acl**]命令用来恢复缺省情况。

【命令】

**[tftp-server acl** *acl-number*]

**[undo** **tftp-server** **acl**]

【缺省情况】

没有使用ACL对设备可访问的TFTP服务器进行限制。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl-number*]：基本访问控制列表的编号，取值范围为2000～2999。

【使用指导】

用户利用ACL中配置的规则可以允许或禁止设备对网络中特定TFTP服务器的访问。

【举例】

\# 仅允许设备访问IP地址为1.1.1.1的TFTP服务器。

\<Sysname\> System-view

Sysname acl number 2000

Sysname-acl-basic-2000 rule permit source 1.1.1.1 0

Sysname-acl-basic-2000 quit

Sysname tftp-server acl 2000{.TerminalDisplayChar}

**TFTP \-- TFTP配置命令 \-- tftp-server ipv6 acl**

------------------------------------------------------------------------

**[tftp-server ipv6 acl**]命令用来在IPv6组网环境下使用ACL限制设备可访问哪些TFTP服务器。

**[undo tftp-server ipv6 acl**]命令用来恢复缺省情况。

【命令】

**[tftp-server ipv6** **acl** *acl-number*]

**[undo** **tftp-server** **ipv6** **acl**]

【缺省情况】

没有使用ACL对设备可访问的IPv6 TFTP服务器进行限制。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl-number*]：基本访问控制列表的编号，取值范围为2000～2999。

【使用指导】

用户利用ACL中配置的规则可以允许或禁止设备对网络中特定TFTP服务器的访问。

【举例】

\# 仅允许设备访问IP地址为2001::1的TFTP服务器。

\<Sysname\> System-view

Sysname acl ipv6 number 2001

Sysname-acl6-basic-2001 rule permit source 2001::1/128

Sysname-acl6-basic-2001 quit

Sysname tftp-server ipv6 acl 2001

