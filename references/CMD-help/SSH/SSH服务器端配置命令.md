<!-- CMD-INDEX
  display ssh server                  | 任意视图             | L47
  display ssh user-information        | 任意视图             | L205
  scp server enable                   | 系统视图             | L285
  sftp server enable                  | 系统视图             | L325
  sftp server idle-timeout            | 系统视图             | L365
  ssh server acl                      | 系统视图             | L413
  ssh server authentication-retries   | 系统视图             | L475
  ssh server authentication-timeout   | 系统视图             | L531
  ssh server compatible-ssh1x enable  | 系统视图             | L581
  ssh server dscp                     | 系统视图             | L631
  ssh server enable                   | 系统视图             | L675
  ssh server ipv6 acl                 | 系统视图             | L715
  ssh server ipv6 dscp                | 系统视图             | L783
  ssh server rekey-interval           | 系统视图             | L827
  ssh user                            | 系统视图             | L881
  bye                                 | SFTP客户端视图        | L997
  cd                                  | SFTP客户端视图        | L1029
  cdup                                | SFTP客户端视图        | L1073
  delete                              | SFTP客户端视图        | L1115
  dir                                 | SFTP客户端视图        | L1151
  display sftp client source          | 任意视图             | L1217
  display ssh client source           | 任意视图             | L1257
  exit                                | SFTP客户端视图        | L1297
  get                                 | SFTP客户端视图        | L1329
  help                                | SFTP客户端视图        | L1369
  ls                                  | SFTP客户端视图        | L1447
  mkdir                               | SFTP客户端视图        | L1513
  put                                 | SFTP客户端视图        | L1543
  pwd                                 | SFTP客户端视图        | L1583
  quit                                | SFTP客户端视图        | L1613
  remove                              | SFTP客户端视图        | L1645
  rename                              | SFTP客户端视图        | L1681
  rmdir                               | SFTP客户端视图        | L1721
  scp                                 | 用户视图             | L1751
  scp ipv6                            | 用户视图             | L1863
  sftp                                | 用户视图             | L1977
  sftp client ipv6 source             | 系统视图             | L2083
  sftp client source                  | 系统视图             | L2137
  sftp ipv6                           | 用户视图             | L2191
  ssh client ipv6 source              | 系统视图             | L2301
  ssh client source                   | 系统视图             | L2355
  ssh2                                | 用户视图             | L2409
  ssh2 ipv6                           | 用户视图             | L2525
-->

**SSH \-- SSH服务器端配置命令 \-- display ssh server**

------------------------------------------------------------------------

**[display ssh server**]命令用来在SSH服务器端显示该服务器的状态信息或会话信息。

【命令】

**[display ssh server**[ { **session** \| **status** }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[session**]：显示SSH服务器的会话信息。

**[status**]：显示SSH服务器的状态信息。

【举例】

\# 在SSH服务器端显示该服务器的状态信息。

\<Sysname\> display ssh server status

 Stelnet server: Disable

 SSH version : 2.0

 SSH authentication-timeout : 60 second(s)

 SSH server key generating interval : 0 hour(s)

 SSH authentication retries : 3 time(s)

 SFTP server: Disable

 SFTP server Idle-Timeout: 10 minute(s)

 NETCONF server: Disable

 SCP server: Disable

表1-1 display ssh server status命令显示信息描述表

字段

描述

SSH server

Stelnet服务器功能的状态

SSH version

SSH协议版本

SSH服务器兼容SSH1时，协议版本为1.99；SSH服务器不兼容SSH1时，协议版本为2.0

SSH authentication-timeout

认证超时时间

SSH server key generating interval

RSA服务器密钥对的最小更新间隔时间

SSH authentication retries

SSH用户认证尝试的最大次数

SFTP server

SFTP服务器功能的状态

SFTP server Idle-Timeout

SFTP用户连接的空闲超时时间

NETCONF server

NETCONF over SSH服务器功能的状态

SCP server

SCP服务器功能的状态

\# 在SSH服务器端显示该服务器的会话信息。

\<Sysname\> display ssh server session

UserPid   SessID Ver   Encrypt    State          Retries  Serv     Username

 184       0     2.0   aes128-cbc Established    1        Stelnet  abc@123

表1-2 display ssh server session显示信息描述表

字段

描述

UserPid

用户进程PID

SessID

会话ID

Ver

SSH服务器的协议版本

Encrypt

SSH服务器本端使用的加密算法

State

会话状态，包括：

·Init：初始化状态

·Ver-exchange：版本协商

·Keys-exchange：密钥交换

·Auth-request：用户认证

·Serv-request：服务请求

·Established：会话已经建立

·Disconnected：断开会话

Retries

认证失败的次数

Serv

服务类型，包括SCP、SFTP、Stelnet和NETCONF

Username

客户端登录服务器时采用的用户名

**SSH \-- SSH服务器端配置命令 \-- display ssh user-information**

------------------------------------------------------------------------

**[display ssh user-information**]命令用来在SSH服务器端显示SSH用户的信息。

【命令】

**[display ssh user-information** [ *username* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[username*]：SSH用户名，为1～80个字符的字符串，区分大小写。如果没有指定本参数，则显示所有SSH用户的信息。

【使用指导】

本命令仅用来显示SSH服务器端通过**ssh user**命令配置的SSH用户信息。

【举例】

\# 显示所有SSH用户的信息。

\<Sysname\> display ssh user-information

 Total ssh users:2

 Username            Authentication-type  User-public-key-name  Service-type

[ yemx                password             null                  Stelnet\|SFTP]

 test                publickey            pubkey                SFTP

表1-3 display ssh user-information显示信息描述表

字段

描述

Total ssh users

SSH用户的总数

Username

用户名

Authentication-type

认证类型，取值包括password、publickey、password-publickey和any

User-public-key-name

用户公钥名称

如果认证类型为password，则用户公钥名称显示为null

Service-type

服务类型，取值包括SCP、SFTP、Stelnet和NETCONF

若同时显示多种服务类型则表示支持多种服务类型

【相关命令】

·**ssh user**

**SSH \-- SSH服务器端配置命令 \-- scp server enable**

------------------------------------------------------------------------

**[scp server enable**]命令用来使能SCP服务器功能。

**[undo scp server enable**]命令用来关闭SCP服务器功能。

【命令】

**[scp server enable**]

**[undo scp server enable**]

【缺省情况】

SCP服务器功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 使能SCP服务器功能。

\<Sysname\> system-view

Sysname scp server enable

【相关命令】

·**display ssh server**

**SSH \-- SSH服务器端配置命令 \-- sftp server enable**

------------------------------------------------------------------------

**[sftp server enable**]命令用来使能SFTP服务器功能。

**[undo sftp server enable**]命令用来关闭SFTP服务器功能。

【命令】

**[sftp server enable**]

**[undo sftp server enable**]

【缺省情况】

SFTP服务器功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 使能SFTP服务器功能。

\<Sysname\> system-view

Sysname sftp server enable

【相关命令】

·**display** **ssh** **server**

**SSH \-- SSH服务器端配置命令 \-- sftp server idle-timeout**

------------------------------------------------------------------------

**[sftp server idle-timeout**]命令用来在SFTP服务器端设置SFTP用户连接的空闲超时时间。

**[undo sftp server idle-timeout**]命令用来恢复缺省情况。

【命令】

**[sftp server idle-timeout** *time-out-value*]

**[undo sftp server idle-timeout**]

【缺省情况】

SFTP用户连接的空闲超时时间为10分钟。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time-out-value*]：超时时间，取值范围为1～35791，单位为分钟。

【使用指导】

当SFTP用户连接的空闲时间超过设定的阈值后，系统会自动断开此用户的连接，从而有效避免用户长期占用连接而不进行任何操作。若同一时间内并发的SFTP连接数较多，可适当减小该值，及时释放系统资源给新用户接入。

【举例】

\# 设置SFTP用户连接的空闲超时时间为500分钟。

\<Sysname\> system-view

Sysname sftp server idle-timeout 500

【相关命令】

·**display ssh server**

**SSH \-- SSH服务器端配置命令 \-- ssh server acl**

------------------------------------------------------------------------

**[ssh server acl**]命令用来设置对IPv4 SSH客户端的访问控制。

**[undo ssh server acl**]命令用来恢复缺省情况。

【命令】

**[ssh server acl** *acl-number* ]

**[undo **]**ssh server acl**

【缺省情况】

允许所有IPv4 SSH客户端向设备发起SSH访问。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl-number*]：指定ACL的编号，取值范围为2000～4999。

【使用指导】

通过本命令可以过滤IPv4 SSH客户端发起的SSH请求报文，具体实现如下：

·若指定的ACL非空，则只允许匹配ACL **permit**规则的客户端访问设备。

·若指定的ACL不存在，或者ACL中无任何规则，则允许SSH客户端发起SSH访问。

该配置生效后，只会过滤新建立的SSH连接，不会影响已建立的SSH连接。

多次执行本配置后，最新的配置生效。

【举例】

\# 只允许IPv4地址为1.1.1.1的SSH客户端向设备发起SSH访问。

\<Sysname\> system-view

Sysname acl basic 2001

Sysname-acl-ipv4-basic-2001 rule permit source 1.1.1.1 0

Sysname-acl-ipv4-basic-2001 quit

Sysname ssh server acl 2001

【相关命令】

·**display ssh server**

**SSH \-- SSH服务器端配置命令 \-- ssh server authentication-retries**

------------------------------------------------------------------------

**[ssh server authentication-retries**]命令用来设置允许SSH用户认证尝试的最大次数。

**[undo ssh server authentication-retries**]命令用来恢复缺省情况。

【命令】

**[ssh server authentication-retries** *times*]

**[undo ssh server authentication-retries**]

【缺省情况】

允许SSH用户认证尝试的最大次数为3次。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[times*]：指定每个SSH用户认证尝试的最大次数，取值范围为1～5。

【使用指导】

通过本命令可以限制用户尝试登录的次数，防止非法用户对用户名和密码进行恶意地猜测和破解。

需要注意的是：

·该配置不会影响已经登录的SSH用户，仅对新登录的SSH用户生效。

·在any认证方式下，SSH客户端通过publickey和password两种方式进行认证尝试的次数总和（可通过命令**display ssh server session**查看），不能超过**ssh server authentication-retries**命令配置的SSH连接认证尝试的最大次数。

·对于password-publickey认证方式，设备首先对SSH用户进行publickey认证，然后进行password认证，这个过程为一次认证尝试，而不是两次认证尝试。

【举例】

\# 指定允许SSH用户认证尝试的最大次数为4。

\<Sysname\> system-view

Sysname ssh server authentication-retries 4

【相关命令】

·**display ssh server**

**SSH \-- SSH服务器端配置命令 \-- ssh server authentication-timeout**

------------------------------------------------------------------------

**[ssh server authentication-timeout**]命令用来在SSH服务器端设置SSH用户的认证超时时间。

**[undo ssh server authentication-timeout**]命令用来恢复缺省情况。

【命令】

**[ssh server authentication-timeout** *time-out-value*]

**[undo ssh server authentication-timeout**]

【缺省情况】

SSH用户的认证超时时间为60秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time-out-value*]：认证超时时间，取值范围为1～120，单位为秒。

【使用指导】

如果SSH用户在设置的认证超时时间内没有完成认证，SSH服务器就拒绝该用户的连接。

为了防止不法用户建立起TCP连接后，不进行接下来的认证，而占用系统资源，妨碍其它合法用户的正常登录，可以适当调小SSH用户认证超时时间。

【举例】

\# 设置SSH用户认证超时时间为10秒。

\<Sysname\> system-view

Sysname ssh server authentication-timeout 10

【相关命令】

·**display ssh server**

**SSH \-- SSH服务器端配置命令 \-- ssh server compatible-ssh1x enable**

------------------------------------------------------------------------

**[ssh** **server** **compatible**-**ssh1x enable**]命令用来设置SSH服务器兼容SSH1版本的客户端。

**[undo** **ssh** **server** **compatible**-**ssh1x** [ **enable** ]]命令用来恢复缺省情况。

【命令】

**[ssh server compatible-ssh1x enable**]

**[undo ssh server compatible-ssh1x ** **enable** ]

【缺省情况】

SSH服务器不兼容SSH1版本的客户端。

【视图】

系统视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

FIPS模式下，不支持本命令。

该配置不会影响已经登录的SSH用户，仅对新登录的SSH用户生效。

【举例】

\# 配置服务器兼容SSH1版本的客户端。

\<Sysname\> system-view

Sysname ssh server compatible-ssh1x enable

【相关命令】

·**display** **ssh** **server**

**SSH \-- SSH服务器端配置命令 \-- ssh server dscp**

------------------------------------------------------------------------

**[ssh server dscp**]命令用来设置IPv4 SSH服务器向SSH客户端发送的报文的DSCP优先级。

**[undo ssh server dscp**]命令用来恢复缺省情况。

【命令】

**[ssh server dscp ***dscp-value*]

**[undo ssh server dscp**]

【缺省情况】

IPv4 SSH报文的DSCP优先级为48。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dscp-value*]：IPv4 SSH报文的DSCP优先级，取值范围为0～63。取值越大，优先级越高。

【使用指导】

DSCP携带在IP报文中的ToS字段，用来体现报文自身的优先等级，决定报文传输的优先程度。通过本命令可以指定服务器发送的IPv4 SSH报文中携带的DSCP优先级的取值。

【举例】

\# 配置IPv4 SSH服务器向SSH客户端发送的报文的DSCP优先级为30。

\<Sysname\> system-view

Sysname ssh server dscp 30

**SSH \-- SSH服务器端配置命令 \-- ssh server enable**

------------------------------------------------------------------------

**[ssh server enable**]命令用来使能Stelnet服务器功能。

**[undo ssh server enable**]命令用来关闭Stelnet服务器功能。

【命令】

**[ssh server enable**]

**[undo ssh server enable**]

【缺省情况】

Stelnet服务器功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 使能Stelnet服务器功能。

\<Sysname\> system-view

Sysname ssh server enable

【相关命令】

·**display ssh server **

**SSH \-- SSH服务器端配置命令 \-- ssh server ipv6 acl**

------------------------------------------------------------------------

**[ssh server ipv6 acl**]命令用来设置对IPv6 SSH客户端的访问控制。

**[undo ssh server ipv6 acl**]命令用来恢复缺省情况。

【命令】

**[ssh server ipv6 acl** [ **ipv6**  *acl-number*]]

**[undo **]**ssh server ipv6 acl**

【缺省情况】

允许所有IPv6 SSH客户端向设备发起SSH访问。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv6**]：指定IPv6 ACL的编号。若不指定该参数，则表示指定二层ACL。

*[acl-number*]：指定ACL的编号。

·指定**ipv6**关键字时，取值范围为2000～3999。

·不指定**ipv6**关键字时，取值范围为4000～4999。

【使用指导】

通过本命令可以过滤IPv6 SSH客户端发起的SSH请求报文，具体实现如下：

·若指定的ACL非空，则只允许匹配ACL **permit**规则的客户端访问设备。

·若指定的ACL不存在，或者ACL中无任何规则，则允许SSH客户端发起SSH访问。

该配置生效后，只会过滤新建立的SSH连接，不会影响已建立的SSH连接。

多次执行本配置后，最新的配置生效。

【举例】

\# 只允许1::1/64网段内的SSH客户端向设备发起SSH访问。

\<Sysname\> system-view

Sysname acl ipv6 basic 2001

Sysname-acl-ipv6-basic-2001 rule permit source 1::1 64

Sysname-acl-ipv6-basic-2001 quit

Sysname ssh server ipv6 acl ipv6 2001

【相关命令】

·**display ssh server**

**SSH \-- SSH服务器端配置命令 \-- ssh server ipv6 dscp**

------------------------------------------------------------------------

**[ssh server ipv6 dscp**]命令用来设置IPv6 SSH服务器向SSH客户端发送的报文的DSCP优先级。

**[undo ssh server ipv6 dscp**]命令用来恢复缺省情况。

【命令】

**[ssh server ipv6 dscp ***dscp-value*]

**[undo ssh server ipv6 dscp**]

【缺省情况】

IPv6 SSH报文的DSCP优先级为48。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dscp-value*]：IPv6 SSH报文的DSCP优先级，取值范围为0～63。取值越大，优先级越高。

【使用指导】

DSCP携带在IPv6报文中的Trafic class字段，用来体现报文自身的优先等级，决定报文传输的优先程度。通过本命令可以指定服务器发送的SSH报文中携带的DSCP优先级的取值。

【举例】

\# 配置IPv6 SSH服务器向SSH客户端发送的报文的DSCP优先级为30。

\<Sysname\> system-view

Sysname ssh server ipv6 dscp 30

**SSH \-- SSH服务器端配置命令 \-- ssh server rekey-interval**

------------------------------------------------------------------------

**[ssh server rekey-interval**]命令用来设置RSA服务器密钥对的最小更新间隔时间。

**[undo ssh** **server rekey-interval**]命令用来恢复缺省情况。

【命令】

**[ssh server rekey-interval** *hours*]

**[undo ssh server rekey-interval**]

【缺省情况】

RSA服务器密钥对的最小更新间隔时间为0，表示系统不更新RSA服务器密钥对。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[hours*]：服务器密钥对的最小更新间隔时间，取值范围为1～24，单位为小时。

【使用指导】

SSH的核心是密钥对的协商和传输，因此密钥对的管理是非常重要的。通过定时更新服务器密钥对，可以防止对密钥对的恶意猜测和破解，从而提高了SSH连接的安全性。

需要注意的是，本配置仅对SSH客户端版本为SSH1的用户有效。

配置该命令后，从首个SSH1用户登录开始，SSH服务器需要等待后续有新的SSH1用户登录，才会更新当前的RSA服务器密钥对，然后使用新的RSA服务器密钥对与新登录的这个SSH1用户进行密钥对的协商，其中等待的最小时长就为此处配置的最小更新间隔时间。之后，重复此过程，直到下一个新的SSH1用户登录才会再次触发RSA服务器密钥的更新。

FIPS模式下，不支持本命令。

【举例】

\# 设置每3小时更新一次RSA服务器密钥对。

\<Sysname\> system-view

Sysname ssh server rekey-interval 3

【相关命令】

·**display ssh server**

**SSH \-- SSH服务器端配置命令 \-- ssh user**

------------------------------------------------------------------------

**[ssh user**]命令用来创建SSH用户，并指定SSH用户的服务类型和认证方式。

**[undo ssh user**]命令用来删除SSH用户。

【命令】

非FIPS模式下：

**[ssh user ***username*** service-type **[{ **all** \| **netconf** \| **scp** \| **sftp** \| **stelnet** } **authentication-type** { **password** \| { **any** \| **password-publickey** \| **publickey** } **assign** ]**publickey** *keyname* } }

**[undo ssh user** *username*]

FIPS]模式下：

**[ssh user ***username*** service-type **[{ **all** \| **netconf** \| **scp** \| **sftp** \| **stelnet** } **authentication-type** ]**publickey** *keyname* } }

**[undo ssh user** *username*]

【缺省情况】]

不存在任何SSH用户。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[username*]：SSH用户名，为1～80个字符的字符串，区分大小写。若用户名中携带ISP域名，则其形式为*pureusername*@*domain*，其中，*pureusername*为1～55个字符的字符串，*domain*为1～24个字符的字符串。

**[service-type**]：SSH用户的服务类型。包括：

·**all**：包括**scp**、**sftp**、**stelnet**和**netconf**四种服务类型。

·**scp**：服务类型为SCP（Secure Copy的简称）。

·**sftp**：服务类型为SFTP（Secure FTP的简称）。

·**stelnet**：服务类型为Stelnet（Secure Telnet的简称）。

·**netconf**：服务类型为NETCONF over SSH。

**[authentication-type**]：SSH用户的认证方式。包括：

·**password**：强制指定该用户的认证方式为password。该认证方式的加密机制简单，加密速度快，可结合AAA{.ItemStepChar}（Authentication, Authorization, Accounting{.ItemStepChar}，认证、授权、计费）实现对用户认证、授权和计费，但容易受到攻击。{.ItemStepChar}

·**any**：不指定用户的认证方式，用户既可以采用password认证，也可以采用publickey认证。

·**password**-**publickey**：指定客户端版本为SSH2的用户认证方式为必须同时进行password和publickey两种认证，安全性更高；客户端版本为SSH1的用户认证方式为只要进行其中一种认证即可。

·**publickey**：强制指定该用户的认证方式为publickey。该认证方式的加密速度相对较慢，但认证强度高，不易受到暴力猜测密码等攻击方式的影响，而且具有较高的易用性。一次配置成功后，后续认证过程自动完成，不需要用户记忆和输入密码。

**[assign**]：指定用于验证客户端的参数。

·**pki-domain** *domain**-name*：指定验证客户端证书的PKI域。*pkiname*表示PKI域的名称，为1～31个字符的字符串，不区分大小写。服务器端使用保存在该PKI域中的CA证书对客户端证书进行合法性检查，无需提前保存客户端的公钥，能够灵活满足大数量客户端的认证需求。

·**publickey ***keyname*：为SSH客户端的公钥。*keyname*表示已经配置的客户端公钥名称，为1～64个字符的字符串，不区分大小写。服务器端使用提前保存在本地的用户公钥对用户进行合法性检查，如果客户端密钥文件改变，服务器端需要及时更新本地配置。

【使用指导】

如果服务器采用publickey方式认证客户端，则必须通过本配置在设备上创建相应的SSH用户，并需要创建同名的本地用户，用于对SSH用户进行本地授权，包括授权用户角色、工作目录；如果服务器采用password方式认证客户端，则必须将SSH用户的账号信息配置在设备（适用于本地认证）或者远程认证服务器（如RADIUS服务器，适用于远程认证）上，而并不要求通过本配置创建相应的SSH用户。

使用该命令为用户指定公钥或PKI域时，以最后一次指定的公钥或PKI域为准。

新配置的服务类型、认证方式和用户公钥或PKI域，不会影响已经登录的SSH用户，仅对新登录的用户生效。

SCP或SFTP用户登录时使用的工作目录与用户使用的认证方式有关：

·采用publickey或password-publickey认证方式的用户，使用的工作目录为对应的本地用户视图下通过**authorization-attribute**命令设置的工作目录。

·只采用password认证方式的用户，使用的工作目录为通过AAA授权的工作目录。

SSH用户登录时拥有的用户角色与用户使用的认证方式有关：

·采用publickey或password-publickey认证方式的用户，用户角色为对应的本地用户视图下通过**authorization-attribute**命令设置的用户角色。

·采用password认证方式的用户，用户角色为通过AAA授权的用户角色。

【举例】

\# 创建SSH用户user1，配置user1的服务类型为SFTP，认证方式为password-publickey，并指定客户端公钥为key1。

\<Sysname\> system-view

Sysname ssh user user1 service-type sftp authentication-type password-publickey assign publickey key1

\# 创建设备管理类本地用户user1，配置用户密码为明文123456TESTplat&!， 服务类型为SSH，授权工作目录为flash:，授权用户角色为network-admin。

Sysname local-user user1 class manage

Sysname-luser-manage-user1 password simple 123456TESTplat&!

Sysname-luser-manage-user1 service-type ssh

Sysname-luser-manage-user1 authorization-attribute work-directory flash: user-role network-admin

【相关命令】

·**authorization-attribute**（安全命令参考/AAA）

·**display ssh user-information**

·**local-user**（安全命令参考/AAA）

·**pki domain**（安全命令参考/PKI）

**SSH \-- SSH客户端配置命令 \-- bye**

------------------------------------------------------------------------

**[bye**]命令用来终止与远程SFTP服务器的连接，并退回到用户视图。

【命令】

**[bye**]

【视图】

SFTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

该命令功能与**exit**、**quit**相同。

【举例】

\# 终止与远程SFTP服务器的连接。

sftp\> bye

\<Sysname\>

**SSH \-- SSH客户端配置命令 \-- cd**

------------------------------------------------------------------------

**[cd**]命令用来改变远程SFTP服务器上的工作路径。

【命令】

**[cd ** *remote-path* ]

【视图】

SFTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[remote-path*]：目的工作路径的名称。

【使用指导】

命令"cd .."用来返回到上一级目录。

命令"cd /"用来返回到系统的根目录。

【举例】

\# 改变工作路径到new1。

sftp\> cd new1

Current Directory is:/new1

sftp\> pwd

Remote working directory: /new1

sftp\>

**SSH \-- SSH客户端配置命令 \-- cdup**

------------------------------------------------------------------------

**[cdup**]命令用来返回到上一级目录。

【命令】

**[cdup**]

【视图】

SFTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 从当前工作目录/test1返回到上一级目录。

sftp\> cd test1

Current Directory is:/test1

sftp\> pwd

Remote working directory: /test1

sftp\> cdup

Current Directory is:/

sftp\> pwd

Remote working directory: /

sftp\>

**SSH \-- SSH客户端配置命令 \-- delete**

------------------------------------------------------------------------

**[delete**]命令用来删除SFTP服务器上指定的文件。

【命令】

**[delete ***remote-file*]

【视图】

SFTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[remote-file*]：要删除的文件的名称。

【使用指导】

该命令和**remove**功能相同。

【举例】

\# 删除服务器上的文件temp.c。

sftp\> delete temp.c

Removing /temp.c

**SSH \-- SSH客户端配置命令 \-- dir**

------------------------------------------------------------------------

**[dir**]命令用来显示指定目录下文件及文件夹的信息。

【命令】

**[dir**[ [ **-a** \| **-l** ]  *remote-path* ]]

【视图】

SFTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[-a**]：以列表的形式显示指定目录下文件及文件夹的详细信息，其中包括以"."开头的文件及文件夹的详细信息。

**[-l**]：以列表的形式显示指定目录下文件及文件夹的详细信息，但不包括以"."开头的文件及文件夹的详细信息。

*[remote-path*]：查询的目录名。

【使用指导】

如果没有指定**-a**和**-l**参数，则显示指定目录下文件及文件夹的名称。

如果没有指定*remote-path*，则显示当前工作目录下文件及文件夹的信息。

该命令功能与**ls**相同。

【举例】

\# 以列表的形式显示当前工作目录下文件及文件夹的详细信息，其中包括以"."开头的文件及文件夹的详细信息。

sftp\> dir -a

drwxrwxrwx    2 1        1               512 Dec 18 14:12 .

drwxrwxrwx    2 1        1               512 Dec 18 14:12 ..

-rwxrwxrwx    1 1        1               301 Dec 18 14:11 010.pub

-rwxrwxrwx    1 1        1               301 Dec 18 14:12 011.pub

-rwxrwxrwx    1 1        1               301 Dec 18 14:12 012.pub

\# 以列表的形式显示当前工作目录下文件及文件夹的详细信息。

sftp\> dir -l

-rwxrwxrwx    1 1        1               301 Dec 18 14:11 010.pub

-rwxrwxrwx    1 1        1               301 Dec 18 14:12 011.pub

-rwxrwxrwx    1 1        1               301 Dec 18 14:12 012.pu

!(SSH命令.files/image002.png)

以上显示信息的格式与服务器的类型有关，请以实际情况为准。

**SSH \-- SSH客户端配置命令 \-- display sftp client source**

------------------------------------------------------------------------

**[display sftp client source**]命令用来显示SFTP客户端的源IP地址配置。

【命令】

**[display sftp client source**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示SFTP客户端的源IP地址配置。

\<Sysname\> display sftp client source

The source IP address of the SFTP client is 192.168.0.1.

The source IPv6 address of the SFTP client is 2:2::2:2.

【相关命令】

·**sftp client ipv6 source**

·**sftp client source**

**SSH \-- SSH客户端配置命令 \-- display ssh client source**

------------------------------------------------------------------------

**[display ssh client source**]命令用来显示STelnet客户端的源IP地址配置。

【命令】

**[display ssh client source**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示STelnet客户端的源IP地址配置。

\<Sysname\> display ssh client source

The source IP address of the SSH client is 192.168.0.1.

The source IPv6 address of the SSH client is 2:2::2:2.

【相关命令】

·**ssh client ipv6 source**

·**ssh client source**

**SSH \-- SSH客户端配置命令 \-- exit**

------------------------------------------------------------------------

**[exit**]命令用来终止与远程SFTP服务器的连接，并退回到用户视图。

【命令】

**[exit**]

【视图】

SFTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

该命令功能与**bye**，**quit**相同。

【举例】

\# 终止与远程SFTP服务器的连接。

sftp\> exit

\<Sysname\>

**SSH \-- SSH客户端配置命令 \-- get**

------------------------------------------------------------------------

**[get**]命令用来从远程SFTP服务器上下载文件并存储在本地。

【命令】

**[get** *remote-file* [ *local-file* ]]

【视图】

SFTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[remote-file*]：远程SFTP服务器上的文件名。

*[local-file*]：本地文件名。

【使用指导】

如果没有指定本地文件名，则认为本地保存文件的文件名与服务器上的文件名相同。

【举例】

\# 下载远程服务器上的temp1.c文件，并以文件名temp.c在本地保存。

sftp\> get temp1.c temp.c

Fetching /temp1.c to temp.c

/temp.c                                                 100% 1424     1.4KB/s   00:00

**SSH \-- SSH客户端配置命令 \-- help**

------------------------------------------------------------------------

**[help**]命令用来显示SFTP客户端命令的帮助信息。

【命令】

**[help**]

【视图】

SFTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

键入**？**和执行**help**命令的功能相同。

【举例】

\# 查看帮助信息。

sftp\> help

Available commands:

  bye                          Quit sftp

  cd [path                    Change remote directory to \'path\']

  cdup                         Change remote directory to the parent directory

  delete path                  Delete remote file

[  dir [-a\|-l]path            Display remote directory listing]

       -a                        List all filenames

       -l                        List filename including the specific

                                 information of the file

  exit                         Quit sftp

  get remote-path [local-path Download file]

  help                         Display this help text

[  ls [-a\|-l]path             Display remote directory]

       -a                         List all filenames

       -l                         List filename including the specific

                                  information of the file

  mkdir path                   Create remote directory

  put local-path [remote-path Upload file]

  pwd                          Display remote working directory

  quit                         Quit sftp

  rename oldpath newpath       Rename remote file

  remove path                  Delete remote file

  rmdir path                   Delete remote empty directory

  ?                            Synonym for help

**SSH \-- SSH客户端配置命令 \-- ls**

------------------------------------------------------------------------

**[ls**]命令用来显示指定目录下文件及文件夹的信息。

【命令】

**[ls**[ [ **-a** \| **-l** ]  *remote-path* ]]

【视图】

SFTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[-a**]：以列表的形式显示指定目录下文件及文件夹的详细信息，其中包括以"."开头的文件及文件夹的详细信息。

**[-l**]：以列表的形式显示指定目录下文件及文件夹的详细信息，但不包括以"."开头的文件及文件夹的详细信息。

*[remote-path*]：查询的目录名。

【使用指导】

如果没有指定**-a**和**-l**参数，则显示指定目录下文件及文件夹的名称。

如果没有指定*remote-path*，则显示当前工作目录下文件及文件夹的信息。

该命令功能与**dir**相同。

【举例】

\# 以列表的形式显示当前工作目录下文件及文件夹的详细信息，其中包括以"."开头的文件及文件夹的详细信息。

sftp\> ls -a

drwxrwxrwx    2 1        1               512 Dec 18 14:12 .

drwxrwxrwx    2 1        1               512 Dec 18 14:12 ..

-rwxrwxrwx    1 1        1               301 Dec 18 14:11 010.pub

-rwxrwxrwx    1 1        1               301 Dec 18 14:12 011.pub

-rwxrwxrwx    1 1        1               301 Dec 18 14:12 012.pub

\# 以列表的形式显示当前工作目录下文件及文件夹的详细信息。

sftp\> ls -l

-rwxrwxrwx    1 1        1               301 Dec 18 14:11 010.pub

-rwxrwxrwx    1 1        1               301 Dec 18 14:12 011.pub

-rwxrwxrwx    1 1        1               301 Dec 18 14:12 012.pub

![说明](SSH命令.files/image003.png)

以上显示信息的格式与服务器的类型有关，请以实际情况为准。

**SSH \-- SSH客户端配置命令 \-- mkdir**

------------------------------------------------------------------------

**[mkdir**]命令用来在远程SFTP服务器上创建新的目录。

【命令】

**[mkdir** *remote-path*]

【视图】

SFTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[remote-path*]：远程SFTP服务器上的目录名。

【举例】

\# 在远程SFTP服务器上建立目录test。

sftp\> mkdir test

**SSH \-- SSH客户端配置命令 \-- put**

------------------------------------------------------------------------

**[put**]命令用来将本地的文件上传到远程SFTP服务器。

【命令】

**[put** *local-file* [ *remote-file* ]]

【视图】

SFTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[local-file*]：本地的文件名。

*[remote-file*]：远程SFTP服务器上的文件名。

【使用指导】

如果没有指定远程服务器上的文件名，则认为服务器上保存文件的文件名与本地的文件名相同。

【举例】

\# 将本地startup.bak文件上传到远程SFTP服务器，并以startup01.bak文件名保存。

sftp\> put startup.bak startup01.bak

Uploading startup.bak to /startup01.bak

startup01.bak                                   100% 1424     1.4KB/s   00:00

**SSH \-- SSH客户端配置命令 \-- pwd**

------------------------------------------------------------------------

**[pwd**]命令用来显示远程SFTP服务器上的当前工作目录。

【命令】

**[pwd**]

【视图】

SFTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 显示远程SFTP服务器上的当前工作目录。

sftp\> pwd

Remote working directory: /

以上显示信息表示当前的工作目录为根目录。

**SSH \-- SSH客户端配置命令 \-- quit**

------------------------------------------------------------------------

**[quit**]命令用来终止与远程SFTP服务器的连接，并退回到用户视图。

【命令】

**[quit**]

【视图】

SFTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

该命令功能与**bye**，**exit**相同。

【举例】

\# 终止与远程SFTP服务器的连接。

sftp\> quit

\<Sysname\>

**SSH \-- SSH客户端配置命令 \-- remove**

------------------------------------------------------------------------

**[remove**]命令用来删除远程SFTP服务器上指定的文件。

【命令】

**[remove**]*remote-file*

【视图】

SFTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[remote-file*]：要删除的文件的名称。

【使用指导】

该命令和**delete**命令相同。

【举例】

\# 删除远程SFTP服务器上的文件temp.c。

sftp\> remove temp.c

Removing /temp.c

**SSH \-- SSH客户端配置命令 \-- rename**

------------------------------------------------------------------------

**[rename**]命令用来改变远程SFTP服务器上指定的文件或者文件夹的名字。

【命令】

**[rename** *old-name* *new-name*]

【视图】

SFTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[old-name*]：原文件名或者文件夹名。

*[new-name*]：新文件名或者文件夹名。

【举例】

\# 将远程SFTP服务器上的文件temp1.c改名为temp2.c。

sftp\> dir

aa.pub  temp1.c

sftp\> rename temp1.c temp2.c

sftp\> dir

aa.pub  temp2.c

**SSH \-- SSH客户端配置命令 \-- rmdir**

------------------------------------------------------------------------

**[rmdir**]命令用来删除远程SFTP服务器上指定的目录。

【命令】

**[rmdir** *remote-path*]

【视图】

SFTP客户端视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[remote-path*]：远程SFTP服务器上的目录名。

【举例】

\# 删除SFTP服务器上当前工作目录下的temp1目录。

sftp\> rmdir temp1

**SSH \-- SSH客户端配置命令 \-- scp**

------------------------------------------------------------------------

**[scp**]命令用来与远程的SCP服务器建立连接，并进行文件传输。

【命令】

非FIPS模式下：

**[scp** *server* [ *port-number*   **vpn-instance** *vpn-instance-name*  { **put** \| **get** } *source-file-name*  *destination-file-name*  [ **identity-key** { **dsa** \| **rsa** } \| **prefer-compress** **zlib** \| **prefer-ctos-cipher** { **3des** \| **aes128** \| **aes256** \| **des** } \| **prefer-ctos-hmac** { **md5** \| **md5-96** \| **sha1** \| **sha1-96** } \| **prefer-kex** { **dh-group-exchange** \| **dh-group1** \| **dh-group14** } \| **prefer-stoc-cipher** { **3des** \| **aes128** \| **aes256** \| **des** } \| **prefer-stoc-hmac** { **md5** \| **md5-96** \| **sha1** \| **sha1-96** } ] \* [ **publickey** *keyname* \| **source** { **interface** *interface-type interface-number* \| **ip** *ip-address* } ] \*]]

FIPS模式下：

**[scp** *server* [ *port-number*   **vpn-instance** *vpn-instance-name*  { **put** \| **get** } *source-file-name*  *destination-file-name*  [ **identity-keyrsa** \| **prefer-compress** **zlib** \| **prefer-ctos-cipher** { **aes128** \| **aes256** } \| **prefer-ctos-hmac** { **sha1** \| **sha1-96** } \| **prefer-kex** **dh-group14** \| **prefer-stoc-cipher** { **aes128** \| **aes256** } \| **prefer-stoc-hmac** { **sha1** \| **sha1-96** }] \* [ **publickey** *keyname* \| **source** { **interface** *interface-type interface-number* \| **ip** *ip-address* } ] \*]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[server*]：服务器的IPv4地址或主机名称，为1～253个字符的字符串，不区分大小写。

*[port*-*number*]：服务器端口号，取值范围为0～65535，缺省值为22。

**[vpn-instance** *vpn-instance-name*]：服务器所属的VPN。其中，*vpn-instance-name*表示MPLS L3VPN的VPN实例名，为1～31个字符的字符串，区分大小写。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[get**]：指定下载文件操作。

**[put**]：指定上传文件操作。

*[source-file-path*]：源文件路径。

*[destination-file-path*]：目的文件路径。不指定该参数时，表示使用源文件路径作为目的文件名称。

**[identity-key**]：客户端采用的公钥算法，缺省算法为**dsa**。

·**dsa**：公钥算法为DSA。

·**rsa**：公钥算法为RSA。

**[prefer-compress**]：服务器与客户端之间的首选压缩算法，缺省不支持压缩。

**[zlib**]：压缩算法ZLIB。

**[prefer-ctos-cipher**]：客户端到服务器端的首选加密算法，缺省算法为**aes128**。**des**、**3des**、**aes128**、**aes256**算法的安全强度和运算花费时间依次递增。

·**3des**：3DES-CBC加密算法。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

·**aes128**：128位的AES-CBC加密算法。

·**aes256**：256位的AES-CBC加密算法。

·**des**：DES-CBC加密算法。

**[prefer-ctos-hmac**]：客户端到服务器端的首选HMAC算法，缺省算法为**sha1**。**md5**、**sha1**算法的安全强度和运算花费时间依次递增。

·**md5**：HMAC算法HMAC-MD5。

·**md5-96**：HMAC算法HMAC-MD5-96。

·**sha1**：HMAC算法HMAC-SHA1。

·**sha1-96**：HMAC算法HMAC-SHA1-96。

**[prefer-kex**]：密钥交换首选算法。非FIPS模式下，缺省算法为**dh-group-exchange**；FIPS模式下，缺省算法为**dh-group14**。**dh-group1**、**dh-group14**算法的安全强度和运算花费时间依次递增。

·**dh-group-exchange**：密钥交换算法diffie-hellman-group-exchange-sha1。

·**dh-group1**：密钥交换算法diffie-hellman-group1-sha1。

·**dh-group14**：密钥交换算法diffie-hellman-group14-sha1。

**[prefer-stoc-cipher**]：服务器端到客户端的首选加密算法，缺省算法为**aes128**。

**[prefer-stoc-hmac**]：服务器端到客户端的首选HMAC算法，缺省算法为**sha1**。

**[publickey ***keyname*]：指定服务器端的主机公钥，用于验证服务器端的身份。其中，*keyname*表示已经配置的主机公钥名称，为1～64个字符的字符串，不区分大小写。

**[source**]：指定与服务器通信的源IP地址或者源接口。缺省情况下，设备根据路由表项自动选择一个源IPv4地址。为保证客户端与服务器之间的通信不会因为所指定的接口发生故障而中断，通常建议指定Loopback接口作为源接口，或者接口的IP地址作为源地址。

·**interface** *interface-type interface-number*：指定源接口。*interface-type interface-number*为接口类型和接口编号。系统将使用该接口的IPv4地址作为发送报文的源IP地址。

·**ip** *ip-address*：指定源IPv4地址。

【使用指导】

当服务器端采用publickey认证方式认证客户端时，客户端需要读取本地的私钥进行数字签名。由于publickey认证可以采用RSA和DSA两种公钥算法，所以需要用**identity-key**关键字指定客户端采用的公钥算法，才能得到正确的本地私钥数据。

【举例】

\# SCP客户端采用publickey认证方式，登录地址为200.1.1.1的远程SCP服务器，下载名为abc.txt的文件，采用如下连接策略，并指定服务器端的公钥名称为svkey：

·首选密钥交换算法为**dh-group14**；

·服务器到客户端的首选加密算法为**aes128**；

·客户端到服务器的首选HMAC算法为**sha1**；

·服务器到客户端的HMAC算法为**sha1-96**；

·服务器与客户端之间的首选压缩算法为**zlib**；

\<Sysname\> scp 200.1.1.1 get abc.txt prefer-kex dh-group14 prefer-stoc-cipher aes128 prefer-ctos-hmac sha1 prefer-stoc-hmac sha1-96 prefer-compress zlib publickey svkey

**SSH \-- SSH客户端配置命令 \-- scp ipv6**

------------------------------------------------------------------------

**[scp ipv6**]命令用来与远程的IPv6 SCP服务器建立连接，并进行文件传输。

【命令】

非FIPS模式下：

**[scp** **ipv6** *server* [ *port-number*   **vpn-instance** *vpn-instance-name*   **-i** *interface-type interface-number *  { **put** \| **get** } *source-file-name*  *destination-file-name*  [ **identity-key** { **dsa** \| **rsa** } \| **prefer-compress** **zlib** \| **prefer-ctos-cipher** { **3des** \| **aes128** \| **aes256** \| **des** } \| **prefer-ctos-hmac** { **md5** \| **md5-96** \| **sha1** \| **sha1-96** } \| **prefer-kex** { **dh-group-exchange** \| **dh-group1** \| **dh-group14** } \| **prefer-stoc-cipher** { **3des** \| **aes128** \| **aes256** \| **des** } \| **prefer-stoc-hmac** { **md5** \| **md5-96** \| **sha1** \| **sha1-96** } ] \* [ **publickey** *keyname* \| **source** { **interface** *interface-type interface-number* \| **ipv6** *ipv6-address* } ] \*]]

FIPS模式下：

**[scp** **ipv6** *server* [ *port-number*   **vpn-instance** *vpn-instance-name*   **-i** *interface-type interface-number *  { **put** \| **get** } *source-file-name*  *destination-file-name*  [ **identity-key** **rsa** \| **prefer-compress** **zlib** \| **prefer-ctos-cipher** { **aes128** \| **aes256** } \| **prefer-ctos-hmac** { **sha1** \| **sha1-96** } \| **prefer-kex** **dh-group14** \| **prefer-stoc-cipher** { **aes128** \| **aes256** } \| **prefer-stoc-hmac** { **sha1** \| **sha1-96** } ] \* [ **publickey** *keyname* \| **source** { **interface** *interface-type interface-number* \| **ipv6** *ipv6-address* } ] \*]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[server*]：服务器的IPv6地址或主机名称，为1～253个字符的字符串，不区分大小写。

*[port*-*number*]：服务器端口号，取值范围为1～65535，缺省值为22。

**[vpn-instance** *vpn-instance-name*]：服务器所属的VPN。其中，*vpn-instance-name*表示MPLS L3VPN的VPN实例名，为1～31个字符的字符串，区分大小写。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[-i ***interface-type interface-number*]：当前SCP客户端连接所使用的出接口的接口类型和接口编号。此参数用于SCP服务器的地址是链路本地地址的情况，而且指定的出接口必需具有链路本地地址。

**[get**]：指定下载文件操作。

**[put**]：指定上传文件操作。

*[source-file-name*]：源文件路径。

*[destination-file-name*]：目的文件路径。不指定该参数时，表示使用源文件路径作为目的文件名称。

**[identity-key**]：客户端采用的公钥算法，缺省算法为**dsa**。

·**dsa**：公钥算法为DSA。

·**rsa**：公钥算法为RSA。

**[prefer-compress**]：服务器与客户端之间的首选压缩算法，缺省不支持压缩。

**[zlib**]：压缩算法ZLIB。

**[prefer-ctos-cipher**]：客户端到服务器端的首选加密算法，缺省算法为**aes128**。**des**、**3des**、**aes128**、**aes256**算法的安全强度和运算花费时间依次递增。

·**3des**：3DES-CBC加密算法。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

·**aes128**：128位的AES-CBC加密算法。

·**aes****256**：256位的AES-CBC加密算法。

·**des**：DES-CBC加密算法。

**[prefer-ctos-hmac**]：客户端到服务器端的首选HMAC算法，缺省算法为**sha1**。**md5**、**sha1**算法的安全强度和运算花费时间依次递增。

·**md5**：HMAC算法HMAC-MD5。

·**md5-96**：HMAC算法HMAC-MD5-96。

·**sha1**：HMAC算法HMAC-SHA1。

·**sha1-96**：HMAC算法HMAC-SHA1-96。

**[prefer-kex**]：密钥交换首选算法。非FIPS模式下，缺省算法为**dh-group-exchange**；FIPS模式下，缺省算法为**dh-group14**。**dh-group1**、**dh-group14**算法的安全强度和运算花费时间依次递增。

·**dh-group-exchange**：密钥交换算法diffie-hellman-group-exchange-sha1。

·**dh-group1**：密钥交换算法diffie-hellman-group1-sha1。

·**dh-group14**：密钥交换算法diffie-hellman-group14-sha1。

**[prefer-stoc-cipher**]：服务器端到客户端的首选加密算法，缺省算法为**aes128**。

**[prefer-stoc-hmac**]：服务器端到客户端的首选HMAC算法，缺省算法为**sha1**。

**[publickey ***keyname*]：指定服务器端的主机公钥，用于验证服务器端的身份。其中，*keyname*表示已经配置的主机公钥名称，为1～64个字符的字符串，不区分大小写。

**[source**]：指定与服务器通信的源IP地址或者源接口。缺省情况下，设备自动选择一个源IPv6地址。为保证客户端与服务器之间的通信不会因为所指定的接口发生故障而中断，通常建议指定Loopback接口作为源接口，或者接口的IP地址作为源地址。

·**interface** *interface-type interface-number*：指定源接口。*interface-type interface-number*为接口类型和接口编号。系统将使用该接口的IPv6地址作为发送报文的源IP地址。

·**ipv6** *ipv6-address*：指定源IPv6地址。

【使用指导】

当服务器端采用publickey认证方式认证客户端时，客户端需要读取本地的私钥进行数字签名。由于publickey认证可以采用RSA和DSA两种公钥算法，所以需要用**identity-key**关键字指定客户端采用的公钥算法，才能得到正确的本地私钥数据。

【举例】

\# SCP客户端采用publickey认证方式，登录地址为2000::1的远程SCP服务器，下载名为abc.txt的文件，采用如下连接策略，并指定服务器端的公钥名称为svkey：

·首选密钥交换算法为**dh-group14**；

·服务器到客户端的首选加密算法为**aes128**；

·客户端到服务器的首选HMAC算法为**sha1**；

·服务器到客户端的HMAC算法为**sha1-96**；

·服务器与客户端之间的首选压缩算法为**zlib**；

\<Sysname\> scp ipv6 2000::1 get abc.txt prefer-kex dh-group14 prefer-stoc-cipher aes128 prefer-ctos-hmac sha1 prefer-stoc-hmac sha1-96 prefer-compress zlib publickey svkey

**SSH \-- SSH客户端配置命令 \-- sftp**

------------------------------------------------------------------------

**[sftp**]命令用来与远程IPv4 SFTP服务器建立连接，并进入SFTP客户端视图。

【命令】

非FIPS模式下：

**[sftp** *server* [ *port-number*   **vpn-instance** *vpn-instance-name*  [ **identity-key** { **dsa** \| **rsa** } \| **prefer-compress** **zlib** \| **prefer-ctos-cipher** { **3des** \| **aes128** **\|** **aes256** \| **des** } \| **prefer-ctos-hmac** { **md5** \| **md5-96** \| **sha1** \| **sha1-96** } \| **prefer-kex** { **dh-group-exchange** \| **dh-group1** \| **dh-group14** } \| **prefer-stoc-cipher** { **3des** \| **aes128** **\|** **aes256** \| **des** } \| **prefer-stoc-hmac** { **md5** \| **md5-96** \| **sha1** \| **sha1-96** } ] \* [ **dscp** *dscp-value* \| **publickey** *keyname* \| **source** { **interface** *interface-type interface-number* *s* \| **ip** *ip-addres*} ] \*]]

FIPS模式下：

**[sftp** *server* [ *port-number*   **vpn-instance** *vpn-instance-name*  [ **identity-key** **rsa** \| **prefer-compress** **zlib** \| **prefer-ctos-cipher** { **aes128 \|** **aes256** } \| **prefer-ctos-hmac** { **sha1** \| **sha1-96** } \| **prefer-kex** **dh-group14** \| **prefer-stoc-cipher** { **aes128** **\|** **aes256** } \| **prefer-stoc-hmac** { **sha1** \| **sha1-96** } ] \* [ **publickey** *keyname* \| **source** { **interface** *interface-type interface-number* *s* \| **ip** *ip-addres*} ] \*]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[server*]：服务器IPv4地址或主机名称，为1～253个字符的字符串，不区分大小写。

*[port-number*]：服务器端口号，取值范围为1～65535，缺省值为22。

**[vpn-instance** *vpn-instance-name*]：服务器所属的VPN。其中，*vpn-instance-name*表示MPLS L3VPN的VPN实例名，为1～31个字符的字符串，区分大小写。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[identity-key**]：客户端采用的公钥算法，缺省算法为**dsa**。

·**dsa**：公钥算法为DSA。

·**rsa**：公钥算法为RSA。

**[prefer-compress**]：服务器与客户端之间的首选压缩算法，缺省不支持压缩。

**[zlib**]：压缩算法ZLIB。

**[prefer-ctos-cipher**]：客户端到服务器端的首选加密算法，缺省算法为**aes128**。**des**、**3des**、**aes128**、**aes256**算法的安全强度和运算花费时间依次递增。

·**3des**：3DES-CBC加密算法。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

·**aes128**：128位的AES-CBC加密算法。

·**aes256**：256位的AES-CBC加密算法。

·**des**：DES-CBC加密算法。

**[prefer-ctos-hmac**]：客户端到服务器端的首选HMAC算法，缺省算法为**sha1**。**md5**、**sha1**算法的安全强度和运算花费时间依次递增。

·**md5**：HMAC算法HMAC-MD5。

·**md5-96**：HMAC算法HMAC-MD5-96。

·**sha1**：HMAC算法HMAC-SHA1。

·**sha1-96**：HMAC算法HMAC-SHA1-96。

**[prefer-kex**]：密钥交换首选算法。非FIPS模式下，缺省算法为**dh-group-exchange**；FIPS模式下，缺省算法为**dh-group14**。**dh-group1**、**dh-group14**算法的安全强度和运算花费时间依次递增。

·**dh-group-exchange**：密钥交换算法diffie-hellman-group-exchange-sha1。

·**dh-group1**：密钥交换算法diffie-hellman-group1-sha1。

·**dh-group14**：密钥交换算法diffie-hellman-group14-sha1。

**[prefer-stoc-cipher**]：服务器端到客户端的首选加密算法，缺省算法为**aes128**。

**[prefer-stoc-hmac**]：服务器端到客户端的首选HMAC算法，缺省算法为**sha1**。

**[dscp** *dscp-value*]：指定客户端发送的SFTP报文中携带的DSCP优先级，取值范围为0～63，缺省值为48。DSCP携带在IP报文中的ToS字段，用来体现报文自身的优先等级，决定报文传输的优先程度。

**[publickey ***keyname*]：指定服务器端的主机公钥，用于验证服务器端的身份。其中，*keyname*表示已经配置的主机公钥名称，为1～64个字符的字符串，不区分大小写。

**[source**]：指定与服务器通信的源IP地址或者源接口。缺省情况下，设备自动选择一个源IPv4地址。为保证客户端与服务器之间的通信不会因为所指定的接口发生故障而中断，通常建议指定Loopback接口或者Dialer接口作为源接口，或者接口的IP地址作为源地址。

·**interface** *interface-type interface-number*：指定源接口。*interface-type interface-number*为接口类型和接口编号。系统将采用该接口的主IPv4地址作为发送报文的源IP地址。

·**ip** *ip-address*：指定源IPv4地址。

【使用指导】

当服务器端采用publickey认证方式认证客户端时，客户端需要读取本地的私钥进行数字签名。由于publickey认证可以采用RSA和DSA两种公钥算法，所以需要用**identity-key**关键字指定客户端采用的公钥算法，才能得到正确的本地私钥数据。

【举例】

\# SFTP客户端采用publickey认证方式，连接IP地址为10.1.1.2的SFTP服务器，采用如下连接策略，并指定服务器端的公钥名称为svkey：

·首选密钥交换算法为**dh-group14**；

·服务器到客户端的首选加密算法为**aes128**；

·客户端到服务器的首选HMAC算法为**sha1**；

·服务器到客户端的HMAC算法为**sha1-96**；

·服务器与客户端之间的首选压缩算法为**zlib**。

\<Sysname\> sftp 10.1.1.2 prefer-kex dh-group14 prefer-stoc-cipher aes128 prefer-ctos-hmac sha1 prefer-stoc-hmac sha1-96 prefer-compress zlib publickey svkey

**SSH \-- SSH客户端配置命令 \-- sftp client ipv6 source**

------------------------------------------------------------------------

**[sftp** **client** **ipv6** **source**]命令用来配置SFTP客户端发送SFTP报文使用的源IPv6地址。

**[undo sftp client ipv6 source**]命令用来恢复缺省情况。

【命令】

**[sftp client ipv6 source **[{ **interface** *interface-type interface-number* \| **ipv6** *ipv6-address* }]]

**[undo sftp client ipv6 source**]

【缺省情况】

未配置SFTP客户端使用的源IPv6地址，设备自动选择IPv6 SFTP报文的源IPv6地址，具体选择原则请参见RFC 3484。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface ***interface-type interface-number*]：指定接口下与报文目的地址最匹配的IPv6地址作为源地址。*interface-type* *interface-number*表示源接口类型与源接口编号。

**[ipv6*** ipv6-address*]：指定源IPv6地址。

【使用指导】

·多次执行本命令，最新配置生效。

·使用该命令指定了源地址后，若SFTP用户使用**sftp ipv6**命令登录时又指定了源地址，则采用**sftp ipv6**命令中指定的源地址。

·**sftp client ipv6 source**命令指定的源地址对所有的SFTP连接有效，**sftp ipv6**命令指定的源地址只对当前的SFTP连接有效。

【举例】

\# 指定SFTP客户端发送SFTP报文使用的源IPv6地址为2:2::2:2。

\<Sysname\> system-view

Sysname sftp client ipv6 source ipv6 2:2::2:2

【相关命令】

·**display sftp client source**

**SSH \-- SSH客户端配置命令 \-- sftp client source**

------------------------------------------------------------------------

**[sftp** **client** **source**]命令用来配置SFTP客户端发送SFTP报文使用的源IPv4地址。

**[undo sftp client source**]命令用来恢复缺省情况。

【命令】

**[sftp client source **[{ **interface** *interface-type interface-number* \| **ip** *ip-address* }]]

**[undo sftp client source**]

【缺省情况】

未配置SFTP客户端使用的源IPv4地址，SFTP客户端发送SFTP报文使用的源IPv4地址为设备路由指定的SFTP报文出接口的主IP地址。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-type interface-number*]：指定接口的主IP地址作为源地址。*interface-type interface-number*表示源接口类型与源接口编号。

**[ip** *ip-address*]：指定源IP地址。

【使用指导】

·多次执行本命令，最新配置生效。

·使用该命令指定了源地址后，若SFTP用户使用**sftp**命令登录时又指定了源地址，则采用**sftp**命令中指定的源地址。

·**sftp client source**命令指定的源地址对所有的SFTP连接有效，**sftp**命令指定的源地址只对当前的SFTP连接有效。

【举例】

\# 指定SFTP客户端发送SFTP报文使用的源IP地址为192.168.0.1。

\<Sysname\> system-view

Sysname sftp client source ip 192.168.0.1

【相关命令】

·**display sftp client source**

**SSH \-- SSH客户端配置命令 \-- sftp ipv6**

------------------------------------------------------------------------

**[sftp ipv6**]命令用来建立SFTP客户端和与远程IPv6 SFTP服务器建立连接，并进入SFTP客户端视图。

【命令】

非FIPS模式下：

**[sftp ipv6** *server* [ *port-number*   **vpn-instance** *vpn-instance-name*   **-i** *interface-type interface-number*  [ **identity-key** { **dsa** \| **rsa** } \| **prefer-compress** **zlib** \| **prefer-ctos-cipher** { **3des** \| **aes128** \| **aes256** \| **des** } \| **prefer-ctos-hmac** { **md5** \| **md5-96** \| **sha1** \| **sha1-96** } \| **prefer-kex** { **dh-group-exchange** \| **dh-group1** \| **dh-group14** } \| **prefer-stoc-cipher** { **3des** \| **aes128** \| **aes256** \| **des** } \| **prefer-stoc-hmac** { **md5** \| **md5-96** \| **sha1** \| **sha1-96** } ] \* [ **dscp** *dscp-value* \| **publickey** *keyname* \| **source** { **interface** *interface-type interface-number* \| **ipv6** *ipv6-addres*} ] \*]]

FIPS模式下：

**[sftp ipv6** *server* [ *port-number*   **vpn-instance** *vpn-instance-name*   **-i** *interface-type interface-number*  [ **identity-key** **rsa** \| **prefer-compress** **zlib** \| **prefer-ctos-cipher** { **aes128** \| **aes256** } \| **prefer-ctos-hmac** { **sha1** \| **sha1-96** } \| **prefer-kex** **dh-group14** \| **prefer-stoc-cipher** { **aes128** \| **aes256** } \| **prefer-stoc-hmac** { **sha1** \| **sha1-96** } ] \* [ **publickey** *keyname* \| **source** { **interface** *interface-type interface-number* \| **ipv6** *ipv6-addres*} ] \*]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[server*]：服务器的IPv6地址或主机名称，为1～253个字符的字符串，不区分大小写。

*[port*-*number*]：服务器端口号，取值范围为1～65535，缺省值为22。

**[vpn-instance** *vpn-instance-name*]：服务器所属的VPN。其中，*vpn-instance-name*表示MPLS L3VPN的VPN实例名，为1～31个字符的字符串，区分大小写。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[-i ***interface-type interface-number*]：客户端连接服务器时使用的出接口。其中，*interface-type interface-number*表示接口类型和接口编号。本参数仅在客户端所连接的服务器的地址是链路本地地址时使用。指定的出接口必须具有链路本地地址。

**[identity-key**]：客户端采用的公钥算法，缺省算法为**dsa**。

·**dsa**：公钥算法为DSA。

·**rsa**：公钥算法为RSA。

**[prefer-compress**]：服务器与客户端之间的首选压缩算法，缺省不支持压缩。

**[zlib**]：压缩算法ZLIB。

**[prefer-ctos-cipher**]：客户端到服务器端的首选加密算法，缺省算法为**aes128**。**des**、**3des**、**aes128**、**aes256**算法的安全强度和运算花费时间依次递增。

·**3des**：3DES-CBC加密算法。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

·**aes128**：128位的AES-CBC加密算法。

·**aes256**：256位的AES-CBC加密算法。

·**des**：DES-CBC加密算法。

**[prefer-ctos-hmac**]：客户端到服务器端的首选HMAC算法，缺省算法为**sha1**。**md5**、**sha1**算法的安全强度和运算花费时间依次递增。

·**md5**：HMAC算法HMAC-MD5。

·**md5-96**：HMAC算法HMAC-MD5-96。

·**sha1**：HMAC算法HMAC-SHA1。

·**sha1-96**：HMAC算法HMAC-SHA1-96。

**[prefer-kex**]：密钥交换首选算法。非FIPS模式下，缺省算法为**dh-group-exchange**；FIPS模式下，缺省算法为**dh-group14**。**dh-group1**、**dh-group14**算法的安全强度和运算花费时间依次递增。

·**dh-group-exchange**：密钥交换算法diffie-hellman-group-exchange-sha1。

·**dh-group1**：密钥交换算法diffie-hellman-group1-sha1。

·**dh-group14**：密钥交换算法diffie-hellman-group14-sha1。

**[prefer-stoc-cipher**]：服务器端到客户端的首选加密算法，缺省算法为**aes128**。

**[prefer-stoc-hmac**]：服务器端到客户端的首选HMAC算法，缺省算法为**sha1**。

**[dscp** *dscp-value*]：指定客户端发送的IPv6 SFTP报文中携带的DSCP优先级，取值范围为0～63，缺省值为48。DSCP携带在IPv6报文中的Trafic class字段，用来体现报文自身的优先等级，决定报文传输的优先程度。

**[publickey ***keyname*]：指定服务器端的主机公钥，用于验证服务器端的身份。其中，*keyname*表示已经配置的主机公钥名称，为1～64个字符的字符串，不区分大小写。

**[source**]：指定与服务器通信的源IP地址或者源接口。缺省情况下，设备自动选择一个源IPv6地址。为保证客户端与服务器之间的通信不会因为所指定的接口发生故障而中断，通常建议指定Loopback接口或者Dialer接口作为源接口，或者接口的IP地址作为源地址。

·**interface** *interface-type interface-number*：指定源接口。*interface-type interface-number*为接口类型和接口编号。系统将使用该接口的IPv6地址作为发送报文的源IP地址。

·**ipv6** *ipv6-address*：指定源IPv6地址。

【使用指导】

当服务器端采用publickey认证方式认证客户端时，客户端需要读取本地的私钥进行数字签名。由于publickey认证可以采用RSA和DSA两种公钥算法，所以需要用**identity-key**关键字指定客户端采用的公钥算法，才能得到正确的本地私钥数据。

【举例】

\# SFTP客户端采用publickey认证方式，连接IPv6地址为2000::1的SFTP服务器，采用如下连接策略，并指定服务器端的公钥名称为svkey：

·首选密钥交换算法为**dh-group14**；

·服务器到客户端的首选加密算法为**aes128**；

·客户端到服务器的首选HMAC算法为**sha1**；

·服务器到客户端的HMAC算法为**sha1-96**；

·服务器与客户端之间的首选压缩算法为**zlib**。

\<Sysname\> sftp ipv6 2000::1 prefer-kex dh-group14 prefer-stoc-cipher aes128 prefer-ctos-hmac sha1 prefer-stoc-hmac sha1-96 prefer-compress zlib publickey svkey

Username:

**SSH \-- SSH客户端配置命令 \-- ssh client ipv6 source**

------------------------------------------------------------------------

**[ssh** **client** **ipv6** **source**]命令用来为配置Stelnet客户端发送SSH报文使用的源IPv6地址。

**[undo ssh client ipv6 source**]命令用来恢复缺省情况。

【命令】

**[ssh client ipv6 source **[{ **interface** *interface-type interface-number* \| **ipv6** *ipv6-address* }]]

**[undo ssh client ipv6 source**]

【缺省情况】

未配置Stelnet客户端使用的源IPv6地址，设备自动选择IPv6 SSH报文的源IPv6地址，具体选择原则请参见RFC 3484。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface ***interface-type interface-number*]：指定接口下与报文目的地址最匹配的IPv6地址作为源地址。*interface-type interface-number*表示源接口类型与源接口编号。

**[ipv6*** ipv6-address*]：指定源IPv6地址。

【使用指导】

·多次执行本命令，最新配置生效。

·使用该命令指定了源地址后，若SSH用户使用**ssh2 ipv6**命令登录时又指定了源地址，则采用**ssh2 ipv6**命令中指定的源地址。

·**ssh client ipv6 source**命令指定的源地址对所有的IPv6 Stelnet连接有效，**ssh2 ipv6**命令指定的源地址只对当前的Stelnet连接有效。

【举例】

\# 指定Stelnet客户端发送SSH报文使用的源IPv6地址为2:2::2:2。

\<Sysname\> system-view

Sysname ssh client ipv6 source ipv6 2:2::2:2

【相关命令】

·**display ssh client source**

**SSH \-- SSH客户端配置命令 \-- ssh client source**

------------------------------------------------------------------------

**[ssh** **client** **source**]命令用来配置Stelnet客户端发送SSH报文使用的源IPv4地址。

**[undo ssh client source**]命令用来恢复缺省情况。

【命令】

**[ssh client source **[{ **interface** *interface-type interface-number* \| **ip** *ip-address* }]]

**[undo ssh client source**]

【缺省情况】

未配置Stelnet客户端使用的源IPv4地址，Stelnet客户端发送SSH报文使用的源IPv4地址为设备路由指定的SSH报文出接口的主IP地址。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-type interface-number*]：指定接口的主IP地址作为源地址。*interface-type interface-number*表示源接口类型与源接口编号。

**[ip** *ip-address*]：指定源IPv4地址。

【使用指导】

·多次执行本命令，最新配置生效。

·使用该命令指定了源地址后，若SSH用户使用**ssh2**命令登录时又指定了源地址，则采用**ssh2**命令中指定的源地址。

·**ssh client source**命令指定的源地址对所有的Stelnet连接有效，**ssh2**命令指定的源地址只对当前的Stelnet连接有效。

【举例】

\# 指定Stelnet客户端发送SSH报文使用的源IPv4地址为192.168.0.1。

\<Sysname\> system-view

Sysname ssh client source ip 192.168.0.1

【相关命令】

·**display ssh client source**

**SSH \-- SSH客户端配置命令 \-- ssh2**

------------------------------------------------------------------------

**[ssh2**]命令用来建立Stelnet客户端和IPv4 Stelnet服务器端的连接。

【命令】

非FIPS模式下：

**[ssh2** *server* [ *port-number*   **vpn-instance** *vpn-instance-name*  [ **identity-key** { **dsa** \| **rsa** } \| **prefer-compress** **zlib** \| **prefer-ctos-cipher** { **3des** \| **aes128** **\| aes256** \| **des** } \| **prefer-ctos-hmac** { **md5** \| **md5-96** \| **sha1** \| **sha1-96** } \| **prefer-kex** { **dh-group-exchange** \| **dh-group1** \| **dh-group14** } \| **prefer-stoc-cipher** { **3des** \| **aes128** **\| aes256** \| **des** } \| **prefer-stoc-hmac** { **md5** \| **md5-96** \| **sha1** \| **sha1-96** } ] \* [ **dscp** *dscp-value* \| **escape** *character* \| **publickey** *keyname* \| **source** { **interface** *interface-type interface-number* \| **ip** *ip-address* } ] \*]]

FIPS模式下：

**[ssh2** *server* [ *port-number*   **vpn-instance** *vpn-instance-name*  [ **identity-key** **rsa** \| **prefer-compress** **zlib** \| **prefer-ctos-cipher** { **aes128** \| **aes256** } \| **prefer-ctos-hmac** { **sha1** \| **sha1-96** } \| **prefer-kex dh-group14** \| **prefer-stoc-cipher** { **aes128 \| aes256** } \| **prefer-stoc-hmac** { **sha1** \| **sha1-96** } ] \* [ **escape** *character* \| **publickey** *keyname* \| **source** { **interface** *interface-type interface-number* \| **ip** *ip-address* } ] \*]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[server*]：服务器IPv4地址或主机名称，为1～253个字符的字符串，不区分大小写。

*[port*-*number*]：服务器端口号，取值范围为1～65535，缺省值为22。

**[vpn-instance** *vpn-instance-name*]：服务器所属的VPN。其中，*vpn-instance-name*表示MPLS L3VPN的VPN实例名，为1～31个字符的字符串，区分大小写。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[identity-key**]：客户端采用的公钥算法，缺省算法为**dsa**。

·**dsa**：公钥算法为DSA。

·**rsa**：公钥算法为RSA。

**[prefer-compress**]：服务器与客户端之间的首选压缩算法，缺省不支持压缩。

**[zlib**]：压缩算法ZLIB。

**[prefer-ctos-cipher**]：客户端到服务器端的首选加密算法，缺省算法为**aes128**。**des**、**3des**、**aes128**、**aes256**算法的安全强度和运算花费时间依次递增。

·**3des**：3DES-CBC加密算法。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

·**aes128**：128位的AES-CBC加密算法。

·**aes****256**：256位的AES-CBC加密算法。

·**des**：DES-CBC加密算法。

**[prefer-ctos-hmac**]：客户端到服务器端的首选HMAC算法，缺省算法为**sha1**。**md5**、**sha1**算法的安全强度和运算花费时间依次递增。

·**md5**：HMAC算法HMAC-MD5。

·**md5-96**：HMAC算法HMAC-MD5-96。

·**sha1**：HMAC算法HMAC-SHA1。

·**sha1-96**：HMAC算法HMAC-SHA1-96。

**[prefer-kex**]：密钥交换首选算法。非FIPS模式下，缺省算法为**dh-group-exchange**；FIPS模式下，缺省算法为**dh-group14**。**dh-group1**、**dh-group14**算法的安全强度和运算花费时间依次递增。

·**dh-group-exchange**：密钥交换算法diffie-hellman-group-exchange-sha1。

·**dh-group1**：密钥交换算法diffie-hellman-group1-sha1。

·**dh-group14**：密钥交换算法diffie-hellman-group14-sha1。

**[prefer-stoc-cipher**]：服务器端到客户端的首选加密算法，缺省算法为**aes128**。

**[prefer-stoc-hmac**]：服务器端到客户端的首选HMAC算法，缺省算法为**sha1**。

**[dscp** *dscp-value*]：指定客户端发送的SFTP报文中携带的DSCP优先级，取值范围为0～63，缺省值为48。DSCP携带在IP报文中的ToS字段，用来体现报文自身的优先等级，决定报文传输的优先程度。

**[escape*****character*]：指定退出字符，该退出字符与字符.配合使用可以强制断开客户端与服务器连接（该方式通常用于服务器端重启或发生异常的情况下，客户端快速中断当前连接）。*character*为一个字符，区分大小写，缺省为\~，即输入\~.可以强制断开与服务端的连接。

**[publickey ***keyname*]：指定服务器端的主机公钥，用于验证服务器端的身份。其中，*keyname*表示已经配置的主机公钥名称，为1～64个字符的字符串，不区分大小写。

**[source**]：指定与服务器通信的源IP地址或者源接口。缺省情况下，报文源IP地址为根据路由查找的发送报文的出接口的主IP地址。为保证客户端与服务器之间的通信不会因为所指定的接口发生故障而中断，通常建议指定Loopback接口或者Dialer接口作为源接口，或者接口的IP地址作为源地址。

·**interface** *interface-type interface-number*：指定源接口。*interface-type interface-number*为接口类型和接口编号。系统将采用该接口的主IPv4地址作为发送报文的源IP地址。

·**ip** *ip-address*：指定源IPv4地址。

【使用指导】

当服务器端采用publickey认证方式认证客户端时，客户端需要读取本地的私钥进行数字签名。由于publickey认证可以采用RSA和DSA两种公钥算法，所以需要通过**identity-key**关键字指定客户端采用的公钥算法，才能得到正确的本地私钥数据。

关于退出字符的使用，需要注意的是：

·必须在一行中首先输入退出字符和.，该操作才能生效，若该行中曾经输入过其它字符或执行了其它操作（比如退格），则需要重新换行输入才能生效。

·一般情况下，建议使用缺省退出字符，避免退出字符和.的组合与登录用户名相同。

【举例】

\# Stelnet客户端采用publickey认证方式，登录地址为3.3.3.3的远程Stelnet服务器，采用如下连接策略，并指定服务器端的公钥名称为svkey：

·首选密钥交换算法为**dh-group14**；

·服务器到客户端的首选加密算法为**aes128**；

·客户端到服务器的首选HMAC算法为**sha1**；

·服务器到客户端的HMAC算法为**sha1-96**；

·服务器与客户端之间的首选压缩算法为**zlib**；

·输入\$.时强制断开客户端和服务端的连接。

\<Sysname\> ssh2 3.3.3.3 prefer-kex dh-group14 prefer-stoc-cipher aes128 prefer-ctos-hmac sha1 prefer-stoc-hmac sha1-96 prefer-compress zlib publickey svkey escape \$

**SSH \-- SSH客户端配置命令 \-- ssh2 ipv6**

------------------------------------------------------------------------

**[ssh2 ipv6**]命令用来建立Stelnet客户端和IPv6 Stelnet服务器端的连接。

【命令】

非FIPS模式下：

**[ssh2** **ipv6** *server* [ *port-number*   **vpn-instance** *vpn-instance-name*   **-i** *interface-type interface-number*  [ **identity-key** { **dsa** \| **rsa** } \| **prefer-compress** **zlib** \| **prefer-ctos-cipher** { **3des** \| **aes128** **\| aes256** \| **des** } \| **prefer-ctos-hmac** { **md5** \| **md5-96** \| **sha1** \| **sha1-96** } \| **prefer-kex** { **dh-group-exchange** \| **dh-group1** \| **dh-group14** } \| **prefer-stoc-cipher** { **3des** \| **aes128** **\| aes256** \| **des** } \| **prefer-stoc-hmac** { **md5** \| **md5-96** \| **sha1** \| **sha1-96** } ] \* [ **dscp** *dscp-value* \| **escape** *character* \| **publickey** *keyname* \| **source** { **interface** *interface-type interface-number* \| **ipv6** *ipv6-address* } ] \*]]

FIPS模式下：

**[ssh2** **ipv6** *server* [ *port-number*   **vpn-instance** *vpn-instance-name*   **-i** *interface-type interface-number*  [ **identity-key** **rsa** \| **prefer-compress** **zlib** \| **prefer-ctos-cipher** { **aes128 \| aes256** } \| **prefer-ctos-hmac** { **sha1** \| **sha1-96** } \| **prefer-kex dh-group14** \| **prefer-stoc-cipher** { **aes128 \| aes256** } \| **prefer-stoc-hmac** { **sha1** \| **sha1-96** } ] \* [ **escape** *character* \| **publickey** *keyname* \| **source** { **interface** *interface-type interface-number* \| **ipv6** *ipv6-address* } ] \*]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[server*]：服务器的IPv6地址或主机名称，为1～253个字符的字符串，不区分大小写。

*[port*-*number*]：服务器端口号，取值范围为1～65535，缺省值为22。

**[vpn-instance** *vpn-instance-name*]：服务器所属的VPN。其中，*vpn-instance-name*表示MPLS L3VPN的VPN实例名，为1～31个字符的字符串，区分大小写。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[-i ***interface-type interface-number*]：客户端连接服务器时使用的出接口。其中，*interface-type interface-number*表示接口类型和接口编号。本参数仅在客户端所连接的服务器的地址是链路本地地址时使用。指定的出接口必须具有链路本地地址。

**[identity-key**]：客户端采用的公钥算法，缺省算法为**dsa**。

·**dsa**：公钥算法为DSA。

·**rsa**：公钥算法为RSA。

**[prefer-compress**]：服务器与客户端之间的首选压缩算法，缺省不支持压缩。

**[zlib**]：压缩算法ZLIB。

**[prefer-ctos-cipher**]：客户端到服务器端的首选加密算法，缺省算法为**aes128**。**des**、**3des**、**aes128**、**aes256**算法的安全强度和运算花费时间依次递增。

·**3des**：3DES-CBC加密算法。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

·**aes128**：128位的AES-CBC加密算法。

·**aes256**：256位的AES-CBC加密算法。

·**des**：DES-CBC加密算法。

**[prefer-ctos-hmac**]：客户端到服务器端的首选HMAC算法，缺省算法为**sha1**。**md5**、**sha1**算法的安全强度和运算花费时间依次递增。

·**md5**：HMAC算法HMAC-MD5。

·**md5-96**：HMAC算法HMAC-MD5-96。

·**sha1**：HMAC算法HMAC-SHA1。

·**sha1-96**：HMAC算法HMAC-SHA1-96。

**[prefer-kex**]：密钥交换首选算法。非FIPS模式下，缺省算法为**dh-group-exchange**；FIPS模式下，缺省算法为**dh-group14**。**dh-group1**、**dh-group14**算法的安全强度和运算花费时间依次递增。

·**dh-group-exchange**：密钥交换算法diffie-hellman-group-exchange-sha1。

·**dh-group1**：密钥交换算法diffie-hellman-group1-sha1。

·**dh-group14**：密钥交换算法diffie-hellman-group14-sha1。

**[prefer-stoc-cipher**]：服务器端到客户端的首选加密算法，缺省算法为**aes128**。

**[prefer-stoc-hmac**]：服务器端到客户端的首选HMAC算法，缺省算法为**sha1**。

**[dscp** *dscp-value*]：指定客户端发送的IPv6 SSH报文中携带的DSCP优先级，取值范围为0～63，缺省值为48。DSCP携带在IPv6报文中的Trafic class字段，用来体现报文自身的优先等级，决定报文传输的优先程度。

**[escape*****character*]：指定退出字符，该退出字符与字符.配合使用可以强制断开客户端与服务器连接（该方式通常用于服务器端重启或发生异常的情况下，客户端快速中断当前连接）。*character*为一个字符，区分大小写，缺省为\~，即输入\~.可以强制断开与服务端的连接。

**[publickey ***keyname*]：指定服务器端的主机公钥，用于验证服务器端的身份。其中，*keyname*表示已经配置的主机公钥名称，为1～64个字符的字符串，不区分大小写。

**[source**]：指定与服务器通信的源IP地址或者源接口。缺省情况下，设备自动选择一个源IPv6地址。为保证客户端与服务器之间的通信不会因为所指定的接口发生故障而中断，通常建议指定Loopback接口或者Dialer接口作为源接口，或者接口的IP地址作为源地址。

·**interface** *interface-type interface-number*：指定源接口。*interface-type interface-number*为接口类型和接口编号。系统将使用该接口的IPv6地址作为发送报文的源IP地址。

·**ipv6** *ipv6-address*：指定源IPv6地址。

关于退出字符的使用，需要注意的是：

·必须在一行中首先输入退出字符和.，该操作才能生效，若该行中曾经输入过其它字符或执行了其它操作（比如退格），则需要重新换行输入才能生效。

·一般情况下，建议使用缺省退出字符，避免退出字符和.的组合与登录用户名相同。

【使用指导】

当服务器端采用publickey认证方式认证客户端时，客户端需要读取本地的私钥进行数字签名。由于publickey认证可以采用RSA和DSA两种公钥算法，所以需要用**identity-key**关键字指定客户端采用的公钥算法，才能得到正确的本地私钥数据。

【举例】

\# SSH客户端采用publickey认证方式，登录地址为2000::1的远程Stelnet服务器，采用如下连接策略，并指定服务器端的公钥名称为svkey：

·首选密钥交换算法为**dh-group14**；

·服务器到客户端的首选加密算法为**aes128**；

·客户端到服务器的首选HMAC算法为**sha1**；

·服务器到客户端的HMAC算法为**sha1-96**；

·服务器与客户端之间的首选压缩算法为**zlib**；

·输入\~.时强制断开客户端和服务端的连接。

\<Sysname\> ssh2 ipv6 2000::1 prefer-kex dh-group14 prefer-stoc-cipher aes128 prefer-ctos-hmac sha1 prefer-stoc-hmac sha1-96 prefer-compress zlib publickey svkey
