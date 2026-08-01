<!-- CMD-INDEX
  debugging ssh server                | 用户视图             | L6
  debugging ssh client                | 用户视图             | L1920
-->

**SSH \-- SSH调试命令 \-- debugging ssh server**

------------------------------------------------------------------------

【命令】

**[debugging ssh server**[ { **all** \| **error** \| **event** \| **message** }]]

**[undo debugging ssh server**[ { **all** \| **error** \| **event** \| **message** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：所有类型的调试信息开关。

**[error**]：错误调试信息开关。

**[event**]：事件调试信息开关。

**[message**]：消息调试信息开关。

【描述】

**[debugging ssh server**]命令用来打开SSH服务器的调试信息开关。**undo debugging ssh server**命令用来关闭SSH服务器的调试信息开关。

缺省情况下，SSH服务器调试信息开关处于关闭状态。

表1-1 debugging ssh server error命令输出信息描述表

字段

描述

Failed to get challenge

获取挑战字失败

PAM authentication context not initialized

PAM认证上下文未初始化

Failed to set real user ID:

设置real user id失败

Failed to set effective user ID:

设置effective user id失败

Too many environment variables, expected \<= 1024.

环境变量太多，应该不大于1024

Internal error: PAM authentication succeeded when it should have failed

内部错误，PAM认证成功，原本应该失败

PAM: Initialization requested when PAM is disabled.

PAM未使能的情况下初始化PAM

PAM: Initialization failed

PAM初始化失败

PAM: Failed to set PAM_TTY:

设置PAM_TTY失败

PAM: PAM disabled or failed to initialize

PAM未使能或者初始化失败

PAM: Failed to set PAM_CONV:

设置PAM_CONV失败

Failed to generate RSA authentication challenge.

生成RSA认证挑战字失败

Failed to verify the RSA authentication response: bad challenge length *xx*

验证RSA认证应答报文失败：错误的挑战字长度*xx*

Failed to perform the RSA authentication challenge-response dialog

准备RSA认证挑战交换环境失败

Failed to create new BN.

创建BIGNUM失败

INTERNAL ERROR: authenticated invalid user *xx*

内部错误，非法认证用户*xx*

Access denied for user *xx*

拒绝用户*xx*接入

No authentication context

没有认证上下文

Keyboard interface error

keyboard接口错误

Wrong number of replies

应答报文数目错误

Access denied for user *xx* by PAM account configuration.

PAM计费配置拒绝用户*xx*登录

Failed to sign server host key

对服务器主机密钥进行签名失败

protocol error during kex, no DH_GEX_REQUEST:

密钥计算过程中协议错误，没有收到DH_GEX_REQUEST请求

DH_GEX_REQUEST, bad parameters:

DH_GEX_REQUEST请求中发现参数错误

Bad IP address or host name:

错误的IP地址或主机名

No user or invalid user

无用户名或非法用户名

No session

无会话

Failed to set environment: too many environment vars

设置环境变量失败：太多的环境变量

Too many lines in environment file *xx*

环境变量文件*xx*的行数太多

Insane session id *xx* (max *mm* allocated *nn*)

错误的通道号xx（最大值*mm*，已分配*nn*）

Insane first unused session id *xx* (max *mm*, allocated *nn*).

错误的第一个未使用通道号*xx*（最大值*mm*，已分配*nn*）

Failed to allocate new session

分配新会话失败

No user for session *xx*

会话*xx*没有用户

No channel for session *xx*

会话*xx*没有通道

Session *xx*: no channel *yy*

会话*xx*没有通道*yy*

Bad IP address or host name:

错误的IP地址或主机名

No user or invalid user

无用户名或非法用户名

No session

无会话

Failed to allocate new session

分配新通道号失败

TCP wrapper failed

TCP wrapper失败

Do connection:

发起连接失败

Failed to get host key

获取主机密码失败

Failed to get server key

获取服务器密码失败

TTY name is null.

TTY名字为空

Failed to change owner

改变owner失败

Failed to change mode

改变mode失败

Authentication response too long:

认证应答报文长度过长

Bad authentication reply message type:

错误的认证应答消息类型

Too many identities in authentication reply:

认证应答中存在太多的标识

Bad authentication response:

错误的认证应答

Bad response from authentication agent:

从认证代理接收到错误的应答

Failed to get data from buffer

从buffer中获取数据失败

Bad string length *xx*

错误的字符串长度*xx*

Failed to put null string to buffer

向buffer中存入空串失败

Failed to put BIGNUM to the buffer.

向buffer中存入BIGNUM失败

Failed to get BIGNUM from the buffer.

从buffer中获取BIGNUM失败

Failed to write BIGNUM to the buffer in SSH2 format.

向buffer中以ssh2协议格式写入BIGNUM失败

Failed to get BIGNUM from the buffer in SSH2 format.

从buffer中以ssh2协议格式获取BIGNUM失败

Failed to append space to the buffer:

在buffer后追加空间失败

Failed to append buffer space:

在buffer后追加空间失败

Failed to consume data from the beginning of the buffer.

从buffer头删除数据失败

Failed to consume data from the end of the buffer.

从buffer尾删除数据失败

Failed to get remote hostname.

获取对端主机名失败

Connection from *x.x.x.x* with IP options: *yy*

从IP地址*x.x.x.x*发起的连接，携带IP选项为*yy*

Failed to allocate new channel:

channel分配失败

Cannot happen: SSH_CHANNEL_LARVAL

SSH_CHANNEL_LARVAL类型的channel在不兼容2.0版本的情况下不应该出现

Cannot happen: OUT_DRAIN

SSH_CHANNEL_OUTPUT_DRAINING类型的channel在不兼容1.3版本的情况下不应该出现

Bad channel type *xx*

错误的channel类型*xx*

Bad channel id *xx*

错误的channel ID *xx*

Non-larval channel

channel为空或者非SSH_CHANNEL_LARVAL类型的channel

Channel xx: decode socks4: len *mm* \> have *nn*

channel ID *xx*：socks4解码时，buffer长度*mm*大于实际串长度*nn*

Channel xx: decode socks4a: len *mm* \> have *nn*

channel ID *xx*：socks4a解码时，buffer长度*mm*大于实际串长度*nn*

Unexpected data on control fd

在控制文件描述符上获取到异常数据

Failed to prepare select:

select准备失败

Cannot happen: input state INPUT_WAIT_DRAIN for proto 1.3

在1.3协议中不应该出现输入状态 INPUT_WAIT_DRAIN

Too many forwards

太多的TCP/IP端口转发

Failed to set socket to non-block

设置socket为非阻塞时失败

x11_request_forwarding:

在x11转发请求处理中收到错误的认证数据

Bad 3DES IV length: *xx*

错误的3DES IV长度*xx*

No 3DES context.

没有3DES上下文信息

No AES context.

没有AES上下文信息

Failed to initialize cipher:

初始化加密套件失败

Failed to initialize cipher *xx*

初始化加密套件xx失败

Cipher encrypt failed:

加密失败

Wrong IV length *xx* != *yy*

IV长度错误

Bad cipher *xx*

错误的加密套件编号*xx*

No available ciphers found

没有可用的加密套件

Bad compression level *xx*

错误的压缩等级*xx*

Buffer compress failed:

Buffer压缩失败

Buffer uncompress failed:

Buffer解压缩失败

Detect attack:

检测到CRC32 压缩攻击

Failed to generate DH_key:

生成DH密钥失败

Failed to create BN.

创建BN失败

Failed to generate DH_private_key

生成DH私钥失败

Failed to generate DH_key

生成DH密钥失败

Failed to generate DH_key:

生成DH密钥失败

Failed to generate DH public key.

生成DH公钥失败

Protocol error.

协议错误

Failed to seed PRNG.

设置PRNG的种子失败

Failed to send SSH2_MSG_KEXINIT:

发送SSH2_MSG_KEXINIT消息失败

Received SSH2_MSG_KEXINIT:

发送SSH2_MSG_KEXINIT消息失败：空的交换上下文

Unsupported key exchange:

不支持的密钥交换类型

No matching cipher found:

没有匹配的加密算法

Matching cipher is not supported:

匹配的加密算法不支持

No matching mac found:

没有匹配的摘要算法

Unsupported mac *xx*

不支持的摘要算法*xx*

No matching compress found:

没有匹配的压缩算法

Unsupported compress:

不支持的压缩算法

Failed to negotiate a key exchange method.

密钥交换算法协商失败

Bad kex algorithm:

错误的密钥交换算法

No host_key algorithm

没有主机公钥算法

Bad host_key algorithm:

错误的主机公钥算法

Bad kex md size *xx*

错误的密钥交换模数大小*xx*

Bad host modulus (len *xx*)

错误的主机模数（长度*xx*）

Bad server modulus (len *xx*)

错误的服务器模数（长度*xx*）

Unexpected KEX type *xx*

错误的密钥交换算法类型*xx*

Failed to compute DH key

计算DH密钥失败

Failed to compute BN

计算BN失败

Cannot load hostkey

加载主机密钥失败

Unsupported hostkey type *xx*

不支持的主机密钥类型*xx*

Failed to create RSA key

创建RSA密钥失败

Failed to create DSA key

创建DSA密钥失败

Failed to create key:

创建密钥失败

Failed to free key:

释放key失败

Failed to compare key:

密钥比较失败

Failed to print key finger:

打印密钥指纹失败

Failed to generate rsa_private_key.

生成RSA私有失败

Failed to generate dsa_private_key.

生成DSA私有失败

Failed to generate key:

密钥生成失败

Failed to setup MAC *xx*, length *yy*.

设置摘要算法*xx*失败，长度为*yy*

Failed to initial MAC

初始化摘要算法失败

Failed to compute MAC:

计算摘要失败

Failed to add arguments:

增加参数失败

Failed to replace argument:

替换参数失败

Failed to expend keys:

扩展密钥失败

Bad channel input state:

错误的通道输入状态

Bad channel output state:

错误的通道输出状态

Failed to load cipher \'none\'

载入none加密套件失败

Compression already enabled

已经使能了压缩

Failed to set encrypt key:

设置加密密钥失败

No keys for mode *xx*

模式xx没有密钥

Too many packets with same key

使用同一个密钥发送的包个数太多

Read failed:

读数据失败

Too large packet size:

包过大

Disconnect recursively

重复断连

Write failed:

写数据失败

Write connection closed

连接的写方向已关闭

Failed to ask password:

获取密码失败

Failed to encrypt RSA public key, exponent too small or not odd.

RSA公钥加密失败，指数太小或非偶数

Failed to encrypt RSA public key

RSA公钥加密失败

Failed to decrypt RSA private key

RSA私钥解密失败

Failed to generate RSA additional parameters

生成RSA附加参数失败

Bad signature blob length:

错误的签名blob长度

Failed to verify DSA signature

验证DSA签名失败

Failed to set resource limits:

设置资源限制失败

Failed to malloc memory:

分配内存失败

Failed to free memory

释放内存失败

Failed to allocate memory

分配内存失败

Protocol major versions differ for *xx*

客户端*xx*的协议主版本号不同

Bad protocol version identification \'*yy*\' from *xx*

客户端*xx*的错误协议版本串*yy*

Did not receive identification string from *xx*

没有从IP地址*xx*收到标识串

Failed to write identification string to *xx*

向地址*xx*写入标识串失败

PAM: conversation function passed a null context

交互接口为空

PAM: Failed to set TZ environment:

设置TZ环境变量失败

PAM: initialization failed

PAM初始化失败

PAM: Failed to set pam item *XX*.

设置PAM的*XX*项错误

Failed to verify the RSA authentication response:

验证RSA认证应答失败

Unknown message during authentication:

认证过程中收到未知消息

*[xx*] authentication disabled

不支持认证方法*xx*

Unsupported public key algorithm:

不支持的公钥算法

Unrecognized authentication method name:

未知的认证方法名

Read error from remote host *xx*:

从远端主机*xx*读取数据失败

Wait returned pid *xx*, expected *yy*

返回的PID值*xx*不是期望的*yy*

Stelnet server is disabled or service type is not supported

Stelnet服务器未使能或者服务器类型不支持

No more sessions

没有更多的会话

Unknown packet type received after authentication:

认证通过后收到未知类型的包

Failed to close PTY:

关闭PTY失败

No user for session *xx*

会话（ID为*xx*）中没有用户

Free space insufficient:

无剩余磁盘空间

Failed to get device free space

获取设备剩余磁盘空间失败

Bad message from *xx* local user *yy*

接收到本地用户*yy*从地址*xx*发来的错误消息

Unknown message *XX*

未知消息类型*XX*

Incoming queue grew unexpectedly

输入队列增长异常

Abnormal message length *xx*

消息长度*xx*异常

Read:

读操作

Write:

写操作

Failed to set socket option SO_REUSEPORT:

设置Socket选项SO_REUSEPORT失败

Failed to bind any address

无法绑定任何地址

Failed to run in a new session:

无法在新的会话中运行

All session info slots are busy now!

会话信息满

Failed to start new child:

启动新的子进程失败

Failed to open config server

无法打开配置服务

User *xx* doesn\'t exist!

用户*xx*不存在

Failed to disconnect from controlling tty

从控制TTY断开连接失败

Failed to open /dev/tty:

打开/dev/tty失败

Decodes terminal modes:

解析终端模式

Setting tty modes failed:

设置TTY模式失败

Failed to write authentication data

写认证数据失败

Failed to read authentication response length

读认证应答长度失败

Failed to read authentication response

读认证应答失败

Bad string length *xx*

错误的串长度*xx*

Failed to get peer name:

获取对端主机名失败

Non-public channel *xx*, type *yy*

非公用通道号*xx*，类型*yy*

Failed to set socket options SO_REUSEADDR

设置Socket选项SO_REUSEADDR失败

Channel *xx*: connection failed:

通道号*xx*：连接失败

Use of DES is strongly discouraged due to cryptographic weaknesses

不推荐使用DES算法，因为加密强度弱

Kex protocol error:

密钥交换协议错误

Failed to get key type from name:

依据密钥名称获取密钥类型失败

Failed to get key:

获取密钥失败

Unsupported key type *xx*

不支持的密钥类型*xx*

Failed to sign key:

密钥签名失败

Failed to verify key:

密钥验证失败

Failed to get key by name \'*xx*\'

从密钥名字*xx*获取密钥实体失败

Failed to get evpkey:

获取EVP密钥失败

Failed to read the file descriptor flags(*xx*):

读取文件描述符标识*xx*失败

Failed to set the file descriptor flags(*xx*):

设置文件描述符标识*xx*失败

Failed to get socket option TCP_NODELAY:

设置Socket选项TCP_NODELAY失败

Failed to send message

发送消息失败

Failed to receive message header

接收消息头失败

Failed to receive message:

接收消息失败

Channel *xx*: protocol error for unexpected state *yy*

通道号*xx*：错误的状态*yy*导致协议错误

Channel *xx*: read failed for unexpected input state *yy*

通道号*xx*：错误的输入状态*yy*导致读失败

Channel *xx*: protocol error for unexpected output state *yy*

通道号*xx*：错误的输出状态*yy*导致协议错误

Channel *xx*: write failed

通道号*xx*：写错误

Channel *xx*: write failed for unexpected output state *yy*

通道号*xx*：错误的输出状态*yy*导致写错误

Channel *xx*: no empty buffer

通道号*xx*：无缓存空间

Channel *xx*: internal error for unexpected output state *yy*

通道号*xx*：错误的输出状态*yy*导致内部错误

Channel *xx*: cannot send IEOF for unexpected state *yy*

通道号*xx*：错误的状态*yy*导致无法发送IEOF消息

Channel *xx*: cannot send SSH_MSG_CHANNEL_OUTPUT_CLOSE for unexpected state *yy*

通道号*xx*：错误的状态*yy*导致无法发送消息SSH_MSG_CHANNEL_OUTPUT_CLOSE

Channel *xx*: SSH2_MSG_CHANNEL_CLOSE received twice

通道号*xx*：重复接收到SSH2_MSG_CHANNEL_CLOSE消息

Channel *xx*: write failed for unexpected output state *yy*

通道号*xx*：错误的输出状态*yy*导致写失败

Channel *xx*: cannot send EOF for unexpected input state *yy*

通道号*xx*：错误的输入状态*yy*导致无法发送EOF消息

Channel *xx*: cannot send CLOSE for input state/output state *yy*/*zz*

通道号*xx*：错误的输入状态*xx*/输出状态*yy*导致无法发送关闭消息

Channel *xx*: already sent CLOSE

通道号*xx*：已经发送关闭消息

Channel *xx*: failed to shutdown write:

通道号*xx*：shutdown写失败

Channel *xx*: failed to close write:

通道号*xx*：关闭写失败

Channel *xx*: failed to shutdown read:

通道号*xx*：shutdown读失败

Channel *xx*: failed to close read:

通道号*xx*：关闭读失败

Bad packet length *xx*

错误的包长度*xx*

Failed to set socket option IP_TOS *xx*:

设置Socket选项IP_TOS值*xx*失败

Bad max packet size *xx*

错误的最大包大小*xx*

Failed to ask password:

获取密码失败

Failed to decrypt RSA private key

解密RSA私钥失败

RSA sign failed:

RSA签名失败

Failed to verify RSA:

RSA验证失败

Bad hash length

错误的哈希长度

Bad signature length

错误的签名长度

Failed to decrypt RSA public key:

解密RSA公钥失败

Bad decrypted length *xx*

错误的解密长度*xx*

Hash mismatch

哈希不匹配

Failed to get remote hostname

获取远端主机名失败

Failed to set socket option SO_KEEPALIVE:

设置Socket选项SO_KEEPALIVE失败

Failed to initialize the INOTIFY

初始化INOTIFY失败

Failed to get name info:

获取名称信息失败

Failed to set socket option:

设置Socket选项失败

Failed to change owner *xx* (0 0):

改变owner失败

Failed to change mode *xx* (0666):

改变mode失败

表1-2 debugging ssh server event命令输出信息描述表

字段

描述

PAM: cleanup

清除PAM相关资源

PAM: initializing for \\\"*xx*\\\", service: *yy*

为用户*xx*初始化PAM资源，服务类型为*yy*

PAM: password authentication accepted for *xx*, level: *yy*, workdir: *zz*

*[xx*]用户PAM密码认证通过，级别为*yy*，工作路径为*zz*

PAM: password authentication failed for *xx*

*[xx*]用户PAM密码认证失败

Get default work dir: *xx*, return: *yy*

获取用户的默认工作路径*xx*，返回值*yy*

Sending challenge \'*xx*\'

发送认证挑战字*xx*

Do authentication: invalid user *xx*

认证进行中，非法用户*xx*

Init keyboard interactive device:

初始化键盘交互设备

SSH2 authentication challenge:

SSH2认证挑战信息

Start SSH2 authentication challenge:

开始SSH2认证挑战:

Received *XX*

接收到消息XX，消息类型可包括：SSH2_MSG_USERAUTH_INFO_RESPONSE、SSH2_MSG_SERVICE_REQUEST、SSH2_MSG_USERAUTH_REQUEST、SSH2_MSG_KEXINIT、SSH2_MSG_KEX_DH_GEX_REQUEST、SSH2_MSG_KEX_DH_GEX_REQUEST_OLD、SSH_CMSG_EOF、SSH_CMSG_WINDOW_SIZE

Publickey authentication

公钥认证

Authentication result: *xx*, authentication algorithm: *yy*

认证结果*xx*（0或1），认证算法*yy*

Username: *xx*, service: *yy*, method: *zz*

用户名*xx*，服务类型*yy*，认证方法*zz*

Try method *xx*

尝试认证方法*xx*

Get authentication methods:

获取到认证方法

Connection closed by *xx*

连接被关闭，对方IP地址为*xx*

Exited with status %d

退出，状态为*xx*

Received exit confirmation

接收到退出确认

Received SIGCHLD

接收到SIGCHLD信号

Entering interactive session for SSH2

进入SSH2交互会话阶段

Need rekeying

需要重新密钥协商

Received session request

收到会话请求

Failed to open session, free channel *xx*

打开会话失败，释放通道号*xx*

Received SSH2_MSG_CHANNEL_OPEN:

接收到消息MSG_CHANNEL_OPEN

Received SSH2_MSG_GLOBAL_REQUEST:

接收到消息SSH2_MSG_GLOBAL_REQUEST

Received SSH2_MSG_CHANNEL_REQUEST:

接收到消息SSH2_MSG_GLOBAL_REQUEST

Initiate server message dispatch, compatibility: *xx*/*yy*

初始化服务器消息分发机制，兼容性：*xx*/*yy*，其中*xx*表示是否兼容2.0，*yy*表示是否兼容1.3)

Compression disabled

取消压缩

Received unsupported request:

接收到不支持的请求

Exec command \'*xx*\'

执行命令*xx*

Setup environment: user=*xx*, work directory=*yy*, level=*zz*

设置环境变量：用户*xx*，工作路径*yy*，权限级别*zz*

Session id *xx* unused.

会话*xx*设置为未使用

Session info: used *xx*, next_unused *yy*, session_id *zz*, channel_id *mm*, pid *nn*

会话信息：是否被使用*xx*，下一个未使用session ID *yy* ，会话ID zz，通道号*mm*，进程ID *nn*

Session opened: session *xx*, link with channel *yy*

会话打开成功，会话ID *xx*，关联通道*yy*

Channel request: user *xx*, service type *yy*

通道请求：用户*xx*，服务类型*yy*

Release channel *xx*

释放通道，通道号*xx*

Close session: session *xx*, pid *yy*

关闭会话，会话ID *xx*，进程ID *yy*

Request *xx*: sent status *yy*

请求序列号*xx*，发送状态*yy*

Failed to get full file name from \\\"*xx*\\\"

从*xx*获取全路径文件名失败

Received client version *xx*

接收到客户端版本*xx*

Nothing at all written

未写入任何数据

Old state mode *xx*

旧的状态码*xx*

New state mode *xx*

新的状态码*xx*

Read EOF

读EOF

RSA key re-generation complete, return *xx*

重新生成RSA密钥，返回值*xx*

Client protocol version *x.y*, client software version *zz*

客户端协议版本*x.y*，客户端软件版本*zz*

Hostkey string

主机密钥串

Server listening on *xx* port *yy*

服务器启动监听IP地址*xx*、端口*yy*

Failed to get remote port

获取远端端口号失败

Drop connection *xx*

丢弃连接，其中*xx*为文件描述句柄号

Start new child *xx*.

启动新的子进程，其中*xx*为进程ID

SSH1 key exchange

SSH1协议密钥交换

Sent *xx* bit server key and yy bit host key

发送*xx*位的服务器密钥和*yy*位的主机密钥

Encryption type:

加密套件

Received session key, encryption turned on

接收到会话密钥，启动加密

KEX done

密钥交换结束

Failed to send data to pid *xx*, return *yy*

发送数据到进程*xx*失败，返回值*yy*（-1或成功发送的字节数值）

Failed to get session info by user pid *xx*

依据用户进程*xx*获取会话信息失败

Failed to send session info to SSHD, return *xx*

向SSHD守护进程发送会话信息失败，返回值*yy*（-1或成功发送的字节数值）

Delete user *xx* successfully！

成功删除用户*xx*

Channel *xx*:read_fd *yy* is a TTY

通道号*xx*：读连接*yy*是TTY

Channel *xx*:big output buffer *yy* \> *zz*

通道号*xx*：较大的输出缓存，实际值*yy*\>最大值*zz*

Channel *xx*:request *yy* confirm *zz*

通道号*xx*：请求*yy*、确认*zz*

Channel *xx*:closing

通道号*xx*：关闭中

Channel *xx*:connected to *yy* port *zz*

通道号*xx*：连接到IP地址*yy*、端口*zz*

Channel *xx*:not open

通道号*xx*：未打开

Channel *xx*:input draining

通道号*xx*：输出关闭中

Channel *xx*:Failed to filter

通道号*xx*：停止过滤

Channel *xx*:window *yy* sent adjust *zz*

通道号*xx*：窗口*yy*发送调整量*zz*

Channel *xx*:garbage collecting

通道号*xx*：资源回收中

Channel *xx*:sent extended data *yy*

通道号*xx*：发送扩展数据*yy*字节

Channel *xx*:accepting extended_data after EOF

通道号*xx*：EOF状态后收到了扩展数据

Channel *xx*:received too much extended data *yy* bytes, window_size *zz*

通道号*xx*：接收太多的扩展数据*yy*，窗口大小*zz*

Channel *xx*:received extended data *yy* bytes

通道号*xx*：接收扩展数据*yy*字节

Channel *xx*:FORCE input drain

通道号*xx*：输入强行关闭

Bad cipher *xx* *yy*

错误的加密套件xx 收到的完整的加密套件串列表*yy*

Enabling compatibility mode for protocol 2.0

使能兼容2.0版本

Enabling compatibility mode for protocol 1.3

使能兼容1.3版本

Enabling compression at level *xx*

使能*xx*等级的压缩算法

Compress outgoing: raw data *xx* bytes, compressed *yy* bytes, factor *zz*

压缩输出：原始数据*xx*字节，压缩后为*yy*字节，比例为*zz*

Compress incoming: raw data *xx* bytes, compressed *yy* bytes, factor *zz*

压缩输入：原始数据*xx*字节，压缩后为*yy*字节，比例为*zz*

Installing CRC compensation attack detector

安装CRC补偿攻击探测器

Kex strings(*xx*):

密钥交互串信息，xx取值代表如下涵义：

·0：密钥交换算法串；

·1：服务器端支持的主机公钥算法串；

·2：客户端到服务器端的加密算法串；

·3：服务器端到客户端的加密算法串；

·4：客户端到服务器端的HMAC算法串；

·5：服务器端到客户端的HMAC算法串；

·6：客户端到服务器端的压缩算法串；

·7：服务器端到客户端的压缩算法串；

·8：客户端到服务器端的语言选择串；

·9：服务器端到客户端的语言选择串

Proposal mismatch:

密钥交互串匹配失败

My proposal kex:

我的密钥交互串

Peer proposal kex:

对方的密钥交互串

Kex: *xx*, Encrypt: *yy*, HMAC: *zz*, Compress: *mm*

密钥交换算法*xx*，加密算法*yy*，摘要算法*zz*，压缩算法*mm*

Bad HAMC *xx* *yy*

错误的摘要算法*xx*摘要算法串*yy*

Send message: type *xx*

发送消息：消息类型*xx*

Channel *xx*:input state: *xx* -\> *yy*

通道号*xx*：输入状态由*xx*状态切换到*yy*

Channel *xx*:output state: *xx* -\> *yy*

通道号*xx*：输出状态由*xx*状态切换到*yy*

Channel *xx*:received *XX*

通道号*xx*：接收到消息*XX*

Channel *xx*: read failed

通道号*xx*：读数据失败

Channel *xx*:send *XX*

通道号*xx*：发送消息*XX*

Channel *xx*:write failed

通道号*xx*：写失败

Channel *xx*:mode=*yy*

通道号*xx*：新的模式*yy*（0和1，分别对应MODE_IN或者MODE_OUT）

Expecting packet type *xx*

期望收到包类型*xx*

Remote message:

远端发来的信息

Set max packet size to *xx*

设置最大包大小为*xx*

Read passphrase:

读取密码

Sent message: type *xx*, ID *yy*

发送消息：类型为*xx*，消息ID为*yy*

DSA verify:

DSA验证

RSA verify

RSA验证

Ignoring unsupported tty mode, opcode *xx*

忽略不支持的TTY模式，操作码为*xx*

Found matching *xx* key, key finger is *yy*

找到匹配的*xx*类型的密钥，密钥指纹串为*yy*。其中，可能是RSA、RSA、DSA

Failed to get domain from 'xx'

从用户名xx中获取ISP域名失败

Failed *mm* for xx from yy port zzz ssh2

用户使用*mm*认证方式认证失败，用户名为xx，用户IP为yy，源端口号为zz。

表1-3 debugging ssh server message命令输出信息描述表

字段

描述

Prepare packet*xx*

准备消息消息类型*xx*

Compression: raw_len *xx*, compressed_len *yy*

数据压缩：原始数据大小为*xx*，压缩后数据大小为*yy*

Input: Length before de-compress *xx*, length after de-compress *yy*

输入：解压前数据长度为*xx*，解压后数据长度为*yy*

Received packet type *xx*

接收到消息*xx*

【举例】

\# 打开SSH服务器端的错误调试信息开关。远端用户abc从IP地址为192.168.0.59的客户端上登录本设备，第一次输入密码错误。

\<Sysname\> debugging ssh server error

%Dec 31 17:50:35:219 2009 Sysname SSHS/6/SSHLOG: Failed password for abc from 192.168.0.59 port 2628 ssh2

*// 来自IP地址192.168.0.59、端口2628的用户abc登录设备，密码认证失败（日志信息）*

\# 远端用户第二次输入正确的密码，成功登录本设备。

%Dec 31 17:50:48:996 2009 Sysname SSHS/6/SSHLOG: Accepted password for abc from 192.168.0.59 port 2628 ssh2

*// 来自IP地址192.168.0.59、端口2628的用户abc登录设备，密码认证成功（日志信息）*

\# 远端用户执行quit命令退出。

%Dec 31 17:50:51:874 2009 Sysname SSHS/6/SSHLOG: Protocol dispatch error: type 24, seq 15.

*// 协议消息分发处理失败，消息类型24，请求序号15（日志信息）*

\*Dec 31 17:50:51:879 2009 Sysname SSHS/3/ERROR: Read error from remote host 192.168.0.59: Connection reset by peer

*// 从远端主机192.168.0.59上读取数据错误，对端已关闭连接（调试信息）*

%Dec 31 17:50:51:897 2009 Sysname SSHS/6/SSHLOG: Received signal SIGCHLD! pid = 167.

*// 接收到SIGCHLD信号，PID为167*

\# 打开SSH服务器端的事件调试信息开关。远端用户从192.168.0.58上通过putty客户端登录本设备，用户名为abc、密码为abc。

\<Sysname\> debugging ssh server event

\*Dec 31 17:58:29:819 2009 Sysname SSHS/7/EVENT: Start new child 135.

\*Dec 31 17:58:29:841 2009 Sysname SSHS/6/EVENT: Connection from 192.168.0.58 port 1476

*// 用户从192.168.0.58的1476端口发起连接请求，用户进程ID为135*

\*Dec 31 17:58:29:873 2009 Sysname SSHS/7/EVENT: Client protocol version 2.0, client software version PuTTY_Release_0.60

*// 客户端SSH协议版本号2.0，客户端软件版本信息为PuTTY_Release_0.60*

\*Dec 31 17:58:29:888 2009 Sysname SSHS/7/EVENT: Enabling compatibility mode for protocol 2.0

\*Dec 31 17:58:29:897 2009 Sysname SSHS/7/EVENT: Local version string SSH-2.0-Comware-7

*// 发给客户端的服务器端版本串信息（版本中的Comware-7与产品型号有关，请以设备的实际情况为准）*

\*Dec 31 17:58:29:947 2009 Sysname SSHS/7/EVENT: Hostkey string is : ssh-dss,ssh-rsa

*// 主机公钥串为ssh-dss、ssh-rsa，即支持DSA和RSA公钥算法*

\*Dec 31 17:58:29:988 2009 Sysname SSHS/7/EVENT: Received SSH2_MSG_KEXINIT.

*// 收到SSH2_MSG_KEXINIT消息*

\*Dec 31 17:58:29:993 2009 Sysname SSHS/7/EVENT: My proposal kex:

*// 服务器端的版本协商算法串信息如下*

\*Dec 31 17:58:30:29 2009 Sysname SSHS/7/EVENT: Kex strings(0): diffie-hellman-group-exchange-sha1,diffie-hellman-group14-sha1,diffie-hellman-group1-sha1

*// 密钥交换算法串*

\*Dec 31 17:58:30:35 2009 Sysname SSHS/7/EVENT: Kex strings(1): ssh-dss,ssh-rsa

*// 服务器端支持的主机公钥算法串*

\*Dec 31 17:58:30:43 2009 Sysname SSHS/7/EVENT: Kex strings(2): aes128-cbc,3des-cbc,des-cbc

*// 客户端到服务器端的加密算法串*

\*Dec 31 17:58:30:48 2009 Sysname SSHS/7/EVENT: Kex strings(3): aes128-cbc,3des-cbc,des-cbc

*// 服务器端到客户端的加密算法串*

\*Dec 31 17:58:30:59 2009 Sysname SSHS/7/EVENT: Kex strings(4): hmac-sha1,hmac-sha1-96,hmac-md5,hmac-md5-96

*// 客户端到服务器端的HMAC算法串*

\*Dec 31 17:58:30:67 2009 Sysname SSHS/7/EVENT: Kex strings(5): hmac-sha1,hmac-sha1-96,hmac-md5,hmac-md5-96

*// 服务器端到客户端的HMAC算法串*

\*Dec 31 17:58:30:76 2009 Sysname SSHS/7/EVENT: Kex strings(6): none,zlib,zlib@openssh.com

*// 客户端到服务器端的压缩算法串*

\*Dec 31 17:58:30:82 2009 Sysname SSHS/7/EVENT: Kex strings(7): none,zlib,zlib@openssh.com

*// 服务器端到客户端的压缩算法串*

\*Dec 31 17:58:30:91 2009 Sysname SSHS/7/EVENT: Kex strings(8):

\*Dec 31 17:58:30:96 2009 Sysname SSHS/7/EVENT: Kex strings(9):

**

\*Dec 31 17:58:30:104 2009 Sysname SSHS/7/EVENT: Peer proposal kex:

*// 客户端的版本协商算法串信息如下*

\*Dec 31 17:58:30:111 2009 Sysname SSHS/7/EVENT: Kex strings(0): diffie-hellman-group-exchange-sha256,diffie-hellman-group-exchange-sha1,diffie-hellman-group14-sha1,diffie-hellman-group1-sha1

*// 密钥交换算法串*

\*Dec 31 17:58:30:147 2009 Sysname SSHS/7/EVENT: Kex strings(1): ssh-rsa,ssh-dss

*// 服务器端支持的主机公钥算法串*

\*Dec 31 17:58:30:153 2009 Sysname SSHS/7/EVENT: Kex strings(2): aes256-ctr,aes256-cbc,rijndael-cbc@lysator.liu.se,aes192-ctr,aes192-cbc,aes128-ctr,aes128-cbc,blowfish-ctr,blowfish-cbc,3des-ctr,3des-cbc,arcfour256,arcfour128

*// 服务器端支持的加密算法串*

\*Dec 31 17:58:30:162 2009 Sysname SSHS/7/EVENT: Kex strings(3): aes256-ctr,aes256-cbc,rijndael-cbc@lysator.liu.se,aes192-ctr,aes192-cbc,aes128-ctr,aes128-cbc,blowfish-ctr,blowfish-cbc,3des-ctr,3des-cbc,arcfour256,arcfour128

*// 服务器端到客户端的加密算法串*

\*Dec 31 17:58:30:170 2009 Sysname SSHS/7/EVENT: Kex strings(4): hmac-sha1,hmac-sha1-96,hmac-md5

*// 客户端到服务器端的HMAC算法串*

\*Dec 31 17:58:30:171 2009 Sysname SSHS/7/EVENT: Kex strings(5): hmac-sha1,hmac-sha1-96,hmac-md5

*// 服务器端到客户端的HMAC算法串*

\*Dec 31 17:58:30:172 2009 Sysname SSHS/7/EVENT: Kex strings(6): none,zlib

*// 客户端到服务器端的压缩算法*

\*Dec 31 17:58:30:173 2009 Sysname SSHS/7/EVENT: Kex strings(7): none,zlib

*// 客户端到服务器端的压缩算法*

\*Dec 31 17:58:30:174 2009 Sysname SSHS/7/EVENT: Kex strings(8):

\*Dec 31 17:58:30:243 2009 Sysname SSHS/7/EVENT: Kex strings(9):

\*Dec 31 17:58:30:248 2009 Sysname SSHS/7/EVENT: Kex: client-\>server, Encrypt: aes128-cbc, HMAC: hmac-sha1, Compress: none

*// 协商出来的客户端到服务器端的加密算法、HMAC算法和压缩算法*

\*Dec 31 17:58:30:253 2009 Sysname SSHS/7/EVENT: Kex: server-\>client, Encrypt: aes128-cbc, HMAC: hmac-sha1, Compress: none

*// 协商出来的服务器端到客户端的加密算法、HMAC算法和压缩算法*

\*Dec 31 17:58:30:287 2009 Sysname SSHS/7/EVENT: Received SSH2_MSG_KEX_DH_GEX_REQUEST_OLD.

*// 接收到SSH2_MSG_KEX_DH_GEX_REQUEST_OLD消息*

\*Dec 31 17:58:31:142 2009 Sysname SSHS/7/EVENT: Expecting packet type 32.

\*Dec 31 17:58:33:45 2009 Sysname SSHS/7/EVENT: Set new keys: mode=1

*// 设置协商出来的新的算法（mode=1表示输出方向）*

\*Dec 31 17:58:33:62 2009 Sysname SSHS/7/EVENT: Expecting packet type 21.

\*Dec 31 17:58:33:466 2009 Sysname SSHS/7/EVENT: Set new keys: mode=0

*// 设置协商出来的新的算法（mode=0标识输入方向）*

\*Dec 31 17:58:33:471 2009 Sysname SSHS/7/EVENT: KEX done.

*// 密钥交换结束*

\*Dec 31 17:58:33:479 2009 Sysname SSHS/7/EVENT: Received SSH2_MSG_SERVICE_REQUEST.

\*Dec 31 17:58:34:459 2009 Sysname SSHS/7/EVENT: Received SSH2_MSG_USERAUTH_REQUEST.

\*Dec 31 17:58:34:464 2009 Sysname SSHS/7/EVENT: Username: abc, service: ssh-connection, method: none

*// 接收到用户认证请求消息，消息中的用户名为abc，服务请求串为ssh-connection，认证方法为none（向对方请求对方支持的认证方法列表串）*

\*Dec 31 17:58:34:470 2009 Sysname SSHS/7/EVENT: PAM: initializing for \"abc\", service:login, pure user name:abc, domain:

*[// PAM*]*初始化，PAM服务类型为login，纯用户名为abc，域名为空*

\*Dec 31 17:58:34:509 2009 Sysname SSHS/7/EVENT: Try authentication method none.

*// 尝试none认证类型*

\*Dec 31 17:58:34:520 2009 Sysname SSHS/6/EVENT: Failed none for abc from 192.168.0.58 port 1476 ssh2

*[// none*]*认证尝试失败*

\*Dec 31 17:58:34:525 2009 Sysname SSHS/7/EVENT: Get authentication methods: password

*// 用户还可挑战的认证方法为password认证方法*

\*Dec 31 17:58:35:673 2009 Sysname SSHS/7/EVENT: Received SSH2_MSG_USERAUTH_REQUEST.

\*Dec 31 17:58:35:679 2009 Sysname SSHS/7/EVENT: Username: abc, service: ssh-connection, method: password

\*Dec 31 17:58:35:687 2009 Sysname SSHS/7/EVENT: Try authentication method password.

\*Dec 31 17:58:36:86 2009 Sysname SSHS/7/EVENT: PAM: password authentication accepted for abc, level: 15, workdir:flash:.

*// 用户password认证挑战成功，授权用户角色level-15，授权工作路径为flash:*

%Dec 31 17:58:36:109 2009 Sysname SSHS/6/SSHLOG: Accepted password for abc from 192.168.0.58 port 1476 ssh2

*// 用户abc从192.168.0.58端口1467发起连接请求，password认证通过*

\*Dec 31 17:58:36:139 2009 Sysname SSHS/7/EVENT: Entering interactive session for SSH2.

\*Dec 31 17:58:36:147 2009 Sysname SSHS/7/EVENT: Initiate server message dispatch, compatibility:1/0

*// 初始化消息分发处理，兼容2.0版本，不兼容1.3版本*

\*Dec 31 17:58:36:158 2009 Sysname SSHS/7/EVENT: Received SSH2_MSG_CHANNEL_OPEN: ctype session, rchan 256, win 16384, max 16384

\*Dec 31 17:58:36:173 2009 Sysname SSHS/7/EVENT: Received session request.

\*Dec 31 17:58:36:185 2009 Sysname SSHS/7/EVENT: Channel 0: new [server-session]

\*Dec 31 17:58:36:191 2009 Sysname SSHS/7/EVENT: Session id 0 unused.

\*Dec 31 17:58:36:199 2009 Sysname SSHS/7/EVENT: Session opened: session 0, link with channel 0

*// 接收到SSH2_MSG_CHANNEL_OPEN消息，分配通道号为0，会话ID为0*

\*Dec 31 17:58:36:212 2009 Sysname SSHS/7/EVENT: Received SSH2_MSG_CHANNEL_REQUEST: channel 0, request pty-req, reply 1

\*Dec 31 17:58:36:225 2009 Sysname SSHS/7/EVENT: Channel request: user abc, service type 1

*// 用户abc的配置支持服务类型为1（1表示同时支持Stelnet和SFTP服务；2表示支持Stelnet服务，3表示支持SFTP服务）*

\*Dec 31 17:58:36:288 2009 Sysname SSHS/7/EVENT: Received SSH2_MSG_CHANNEL_REQUEST: channel 0, request shell, reply 1

*// 接收到类型为shell的通道请求消息*

\*Dec 31 17:58:36:298 2009 Sysname SSHS/7/EVENT: Channel request: user abc, service type 1

\*Dec 31 17:58:36:327 2009 Sysname SSHS/7/EVENT: Channel 0: read_fd 33 is a TTY.

\*Dec 31 17:58:36:337 2009 Sysname SSHS/7/EVENT: Setup environment: user=abc, work directory=flash:, level=15

*// 设置用户abc的环境变量：工作路径为flash:，授权等级为15*

\*Dec 31 17:58:36:349 2009 Sysname SSHS/7/EVENT: Get default work dir: /mnt/flash:, return:0

\*Dec 31 17:58:40:87 2009 Sysname SSHS/7/EVENT: Received SIGCHLD.

\*Dec 31 17:58:40:93 2009 Sysname SSHS/7/EVENT: Channel 0: request exit-status confirm 0

\*Dec 31 17:58:40:102 2009 Sysname SSHS/7/EVENT: Release channel 0

\*Dec 31 17:58:40:107 2009 Sysname SSHS/7/EVENT: Channel 0: write failed

\*Dec 31 17:58:40:111 2009 Sysname SSHS/7/EVENT: Channel 0: send EOW

\*Dec 31 17:58:40:115 2009 Sysname SSHS/7/EVENT: Channel 0: output state changed (open -\> closed)

\*Dec 31 17:58:40:125 2009 Sysname SSHS/7/EVENT: Channel 0: read failed

\*Dec 31 17:58:40:129 2009 Sysname SSHS/7/EVENT: Channel 0: input state changed (open -\> drain)

\*Dec 31 17:58:40:134 2009 Sysname SSHS/7/EVENT: Channel 0: send EOF

\*Dec 31 17:58:40:138 2009 Sysname SSHS/7/EVENT: Channel 0: input state changed (drain -\> closed)

\*Dec 31 17:58:40:143 2009 Sysname SSHS/7/EVENT: Channel 0: send SSH2_MSG_CHANNEL_CLOSE

\*Dec 31 17:58:40:173 2009 Sysname SSHS/7/EVENT: Channel 0: received SSH2_MSG_CHANNEL_CLOSE

\*Dec 31 17:58:40:180 2009 Sysname SSHS/7/EVENT: Close session: session 0, pid 0

\*Dec 31 17:58:40:185 2009 Sysname SSHS/7/EVENT: Session id 0 unused.

\*Dec 31 17:58:40:187 2009 Sysname SSHS/7/EVENT: Channel 0: garbage collecting

\*Dec 31 17:58:40:198 2009 Sysname SSHS/7/EVENT: Connection closed by 192.168.0.58

*// 从IP地址192.168.0.58发起的连接被主动关闭*

\*Dec 31 17:58:40:203 2009 Sysname SSHS/7/EVENT: PAM: cleanup

\*Dec 31 17:58:40:205 2009 Sysname SSHS/6/EVENT: Transferred: sent 1928 bytes, received 1624 bytes

*// 传输完成，发送1928字节，接收1624字节*

\*Dec 31 17:58:40:207 2009 Sysname SSHS/6/EVENT: Closing connection to 192.168.0.58 port 1476

*// 关闭与IP地址192.168.0.58、端口1476之间的连接*

\# 打开SSH服务器端的消息调试信息开关。用户从IP地址为192.168.0.59的客户端上登录本设备。登录成功后，用户首先执行了**dir**命令，然后执行**quit**命令退出。

\<Sysname\> debugging ssh server message

\*Dec 31 16:07:05:723 2009 Sysname SSHS/7/MESSAGE: Prepare packet[20.]

*// 准备消息，消息类型为20（以下各消息涵义类似，解释略）*

\*Dec 31 16:07:05:779 2009 Sysname SSHS/7/MESSAGE: Received packet type 20.

*// 接收到消息，消息类型为20（以下各消息涵义类似，解释略）*

\*Dec 31 16:07:05:886 2009 Sysname SSHS/7/MESSAGE: Received packet type 34.

\*Dec 31 16:07:05:887 2009 Sysname SSHS/7/MESSAGE: Prepare packet[31.]

\*Dec 31 16:07:07:444 2009 Sysname SSHS/7/MESSAGE: Received packet type 32.

\*Dec 31 16:07:09:294 2009 Sysname SSHS/7/MESSAGE: Prepare packet[33.]

\*Dec 31 16:07:09:301 2009 Sysname SSHS/7/MESSAGE: Prepare packet[21.]

\*Dec 31 16:07:11:627 2009 Sysname SSHS/7/MESSAGE: Received packet type 21.

\*Dec 31 16:07:11:738 2009 Sysname SSHS/7/MESSAGE: Received packet type 5.

\*Dec 31 16:07:11:741 2009 Sysname SSHS/7/MESSAGE: Prepare packet[6.]

\*Dec 31 16:07:11:840 2009 Sysname SSHS/7/MESSAGE: Received packet type 50.

\*Dec 31 16:07:11:846 2009 Sysname SSHS/7/MESSAGE: Prepare packet[51.]

\*Dec 31 16:07:12:673 2009 Sysname SSHS/7/MESSAGE: Received packet type 50.

\*Dec 31 16:07:12:803 2009 Sysname SSHS/7/MESSAGE: Prepare packet[52.]

\*Dec 31 16:07:12:885 2009 Sysname SSHS/7/MESSAGE: Received packet type 90.

\*Dec 31 16:07:12:887 2009 Sysname SSHS/7/MESSAGE: Prepare packet[91. ]

\*Dec 31 16:07:12:986 2009 Sysname SSHS/7/MESSAGE: Received packet type 98.

\*Dec 31 16:07:12:996 2009 Sysname SSHS/7/MESSAGE:P repare packet[99.]

\*Dec 31 16:07:13:86 2009 Sysname SSHS/7/MESSAGE: Received packet type 98.

\*Dec 31 16:07:13:97 2009 Sysname SSHS/7/MESSAGE: Prepare packet[93.]

\*Dec 31 16:07:13:99 2009 Sysname SSHS/7/MESSAGE: Prepare packet[99.]

\*Dec 31 16:07:14:62 2009 Sysname SSHS/7/MESSAGE: Received packet type 94.

\*Dec 31 16:07:14:268 2009 Sysname SSHS/7/MESSAGE: Received packet type 94.

\*Dec 31 16:07:14:695 2009 Sysname SSHS/7/MESSAGE: Received packet type 94.

\*Dec 31 16:07:14:902 2009 Sysname SSHS/7/MESSAGE: Received packet type 94.

\*Dec 31 16:07:17:99 2009 Sysname SSHS/7/MESSAGE: Received packet type 94.

\*Dec 31 16:07:17:205 2009 Sysname SSHS/7/MESSAGE: Received packet type 94.

\*Dec 31 16:07:17:306 2009 Sysname SSHS/7/MESSAGE: Received packet type 94.

\*Dec 31 16:07:17:508 2009 Sysname SSHS/7/MESSAGE: Received packet type 94.

\*Dec 31 16:07:17:520 2009 Sysname SSHS/7/MESSAGE: Prepare packet[98.]

\*Dec 31 16:07:17:523 2009 Sysname SSHS/7/MESSAGE: Prepare packet[96.]

\*Dec 31 16:07:17:525 2009 Sysname SSHS/7/MESSAGE: Prepare packet[97.]

\*Dec 31 16:07:17:719 2009 Sysname SSHS/7/MESSAGE: Received packet type 24.

\*Dec 31 16:07:17:722 2009 Sysname SSHS/7/MESSAGE: Prepare packet[3.]

**SSH \-- SSH调试命令 \-- debugging ssh client**

------------------------------------------------------------------------

【命令】

**[debugging ssh client**[ { **all** \| **error** \| **event** \| **message** }]]

**[undo debugging ssh client**[ { **all** \| **error** \| **event** \| **message** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：所有类型的调试信息开关。

**[error**]：错误调试信息开关。

**[event**]：事件调试信息开关。

**[message**]：消息调试信息开关。

【描述】

**[debugging ssh client**]命令用来打开SSH客户端调试信息开关。**undo debugging ssh client**命令用来关闭SSH客户端调试信息开关。

缺省情况下，SSH客户端调试信息开关处于关闭状态。

表1-4 debugging ssh client error命令输出信息描述表

字段

描述

The count of global confirm register too much:

全局确认计数太大

Killed by signal *xx*

由于收到信号*xx*，进程终止

Failed to setup session: unknown channel *xx*

建立会话失败，未知通道号*xx*

Cannot decode server_public_key_blob

无法解码服务器公钥

Type mismatch for decoded server_public_key_blob

服务器公钥类型不匹配

Failed to save server public key

保存服务器公钥失败

Failed to verify server host key

验证服务器主机密钥失败

Failed to authenticate server public key

认证服务器公钥失败

DH_GEX group out of range:

DH密钥交换算法的group参数超出范围

Cannot decode server_host_key_blob

无法解码服务器主机密钥

Type mismatch for decoded server_host_key_blob

服务器主机密钥类型不匹配

Outbound message too long *xx*

要发的消息太长

Couldn\'t send packet:

无法发送包

Connection closed

连接已被关闭

Failed to read packet:

读取数据包失败

Received message too long *xx*

接收到的消息太长

ID mismatch (*xx* != *yy*)＝)

ID不匹配(当前ID *xx* 不等于期望ID *yy*)

Expected *XX* packet, got *YY*

期望接收到消息*XX*，却接收到*YY*

Got multiple names (*xx*) from SSH_FXP_REALPATH

从SSH_FXP_REALPATH消息中获取到多个文件名*xx*

Unexpected reply *xx*

接收到非期望的包序列*xx*

Received more data than asked for *xx* \> *yy*

接收到过多数据

Transfer complete, but fail sanity check

传送完成，完整性检查失败

Couldn\'t read from \\\"*xx*\\\":

无法从文件*xx*中读取数据

Unexpected ACK *xx*

非期望的ACK *xx*

Couldn\'t find request for ID *xx*

无法找到ID *xx*对应的请求

Too many data

数据太多

Unknown ls sort type

不认识的ls 排序类型

*[xx*] is not implemented

*[xx*]命令未实现

Couldn\'t initialize connection to server

无法初始化到server的连接

Failed to get current working directory

获取当前工作路径失败

Couldn\'t wait for ssh process:

无法等到SSH进程

No host

未输入目标主机名或IP地址

The public key does not exist

指定的公钥不存在

Failed to get host name:

获取主机名失败

Remote port forwarding failed for listen port *xx*

监听端口*xx*的端口转发失败

Couldn\'t request local forwarding

无法请求本地转发

Compression level must be from 1 (fast) to 9 (slow, best)

压缩等级只能从1到9

·1：压缩速度最快

·9：压缩速度最慢，性能最好

Failed to select, return (*xx*).

select失败，返回值(*xx*)

Couldn\'t resolve hostname *xx*:

无法解析主机名*xx*

Connection timed out during banner exchange

banner交换过程中连接超时

SSH exchange identification:

交换标识

Bad remote protocol version identification:

远端版本标识错误

Protocol major versions differ:

主版本号不同

Couldn\'t wait for child:

等待子进程错误

Server denied authentication request:

服务器拒绝认证请求

Failed to setup authentication context:

设置认证上下文失败

Permission denied (xx).

访问拒绝

Bad message during authentication:

认证过程中接收到错误的消息

No authentication context

No authentication context.

Server returned different OID from expected

服务器返回不同的OID

Failed to sign and send public_key

公钥签名和发送失败

Authentication response too long:

认证应答报文长度过长

Bad authentication reply message type:

错误的认证应答消息类型

Too many identities in authentication reply:

认证应答中存在太多的标识

Bad authentication response:

错误的认证应答

Bad response from authentication agent:

从认证代理接收到错误的应答

Failed to get data from buffer

从buffer中获取数据失败

Bad string length *xx*

错误的字符串长度*xx*

Failed to put null string to buffer

向buffer中存入空串失败

Failed to put BIGNUM to the buffer.

向buffer中存入BIGNUM失败

Failed to get BIGNUM from the buffer.

从buffer中获取BIGNUM失败

Failed to write BIGNUM to the buffer in SSH2 format.

向buffer中以ssh2协议格式写入BIGNUM失败

Failed to get BIGNUM from the buffer in SSH2 format.

从buffer中以ssh2协议格式获取BIGNUM失败

Failed to append space to the buffer:

在buffer后追加空间失败

Failed to append buffer space:

在buffer后追加空间失败

Failed to consume data from the beginning of the buffer.

从buffer头删除数据失败

Failed to consume data from the end of the buffer.

从buffer尾删除数据失败

Failed to get remote hostname.

获取对端主机名失败

Connection from *x.x.x.x* with IP options: *yy*

从IP地址*x.x.x.x*发起的连接，携带IP选项为*yy*

Failed to allocate new channel:

channel分配失败

Cannot happen: SSH_CHANNEL_LARVAL

SSH_CHANNEL_LARVAL类型的channel在不兼容2.0版本的情况下不应该出现

Cannot happen: OUT_DRAIN

SSH_CHANNEL_OUTPUT_DRAINING类型的channel在不兼容1.3版本的情况下不应该出现

Bad channel type *xx*

错误的channel类型*xx*

Bad channel id *xx*

错误的channel ID *xx*

Non-larval channel

channel为空或者非SSH_CHANNEL_LARVAL类型的channel

Channel xx: decode socks4: len *mm* \> have *nn*

channel ID *xx*：socks4解码时，buffer长度*mm*大于实际串长度*nn*

Channel xx: decode socks4a: len *mm* \> have *nn*

channel ID *xx*：socks4a解码时，buffer长度*mm*大于实际串长度*nn*

Unexpected data on control fd

在控制文件描述符上获取到异常数据

Failed to prepare select:

select准备失败

Cannot happen: input state INPUT_WAIT_DRAIN for proto 1.3

在1.3协议中不应该出现输入状态 INPUT_WAIT_DRAIN

Too many forwards

太多的TCP/IP端口转发

Failed to set socket to non-block

设置socket为非阻塞时失败

x11_request_forwarding:

在x11转发请求处理中收到错误的认证数据

Bad 3DES IV length: *xx*

错误的3des IV长度*xx*

No 3DES context.

没有3des上下文信息

No AES context.

没有AES上下文信息

Failed to initialize cipher:

初始化加密套件失败

Failed to initialize cipher *xx*

初始化加密套件xx失败

Cipher encrypt failed:

加密失败

Wrong IV length *xx* != *yy*

IV长度错误

Bad cipher *xx*

错误的加密套件编号*xx*

No available ciphers found

没有可用的加密套件

Bad compression level *xx*

错误的压缩等级*xx*

Buffer compress failed:

Buffer压缩失败

Buffer uncompress failed:

Buffer解压缩失败

Detect attack:

检测到CRC32 压缩攻击

Failed to generate DH_key:

生成DH密钥失败

Failed to create BN.

创建BN失败

Failed to generate DH_private_key

生成DH私钥失败

Failed to generate DH_key

生成DH密钥失败

Failed to generate DH_key:

生成DH密钥失败

Failed to generate DH public key.

生成DH公钥失败

Protocol error.

协议错误

Failed to seed PRNG.

设置PRNG的种子失败

Failed to send SSH2_MSG_KEXINIT:

发送SSH2_MSG_KEXINIT消息失败

Received SSH2_MSG_KEXINIT:

发送SSH2_MSG_KEXINIT消息失败：空的交换上下文

Unsupported key exchange:

不支持的密钥交换类型

No matching cipher found:

没有匹配的加密算法

Matching cipher is not supported:

匹配的加密算法不支持

No matching mac found:

没有匹配的摘要算法

Unsupported mac *xx*

不支持的摘要算法*xx*

No matching compress found:

没有匹配的压缩算法

Unsupported compress:

不支持的压缩算法

Failed to negotiate a key exchange method.

密钥交换算法协商失败

Bad kex algorithm:

错误的密钥交换算法

No host_key algorithm

没有主机公钥算法

Bad host_key algorithm:

错误的主机公钥算法

Bad kex md size *xx*

错误的密钥交换模数大小*xx*

Bad host modulus (len *xx*)

错误的主机模数（长度*xx*）

Bad server modulus (len *xx*)

错误的服务器模数（长度*xx*）

Unexpected KEX type *xx*

错误的密钥交换算法类型*xx*

Failed to compute DH key

计算DH密钥失败

Failed to compute BN

计算BN失败

Cannot load hostkey

加载主机密钥失败

Unsupported hostkey type *xx*

不支持的主机密钥类型*xx*

Failed to create RSA key

创建RSA密钥失败

Failed to create DSA key

创建DSA密钥失败

Failed to create key:

创建密钥失败

Failed to free key:

释放key失败

Failed to compare key:

密钥比较失败

Failed to print key finger:

打印密钥指纹失败

Failed to generate rsa_private_key.

生成RSA私有失败

Failed to generate dsa_private_key.

生成DSA私有失败

Failed to generate key:

密钥生成失败

Failed to setup MAC *xx*, length *yy*.

设置摘要算法*xx*失败，长度为*yy*

Failed to initial MAC

初始化摘要算法失败

Failed to compute MAC:

计算摘要失败

Failed to add arguments:

增加参数失败

Failed to replace argument:

替换参数失败

Failed to expend keys:

扩展密钥失败

Bad channel input state:

错误的通道输入状态

Bad channel output state:

错误的通道输出状态

Failed to load cipher \'none\'

载入none加密套件失败

Compression already enabled

已经使能了压缩

Failed to set encrypt key:

设置加密密钥失败

No keys for mode *xx*

模式xx没有密钥

Too many packets with same key

使用同一个密钥发送的包个数太多

Read failed:

读数据失败

Too large packet size:

包过大

Disconnect recursively

重复断连

Write failed:

写数据失败

Write connection closed

连接的写方向已关闭

Failed to ask password:

获取密码失败

Failed to encrypt RSA public key, exponent too small or not odd.

RSA公钥加密失败，指数太小或非偶数

Failed to encrypt RSA public key

RSA公钥加密失败

Failed to decrypt RSA private key

RSA私钥解密失败

Failed to generate RSA additional parameters

生成RSA附加参数失败

Bad signature blob length:

错误的签名blob长度

Failed to verify DSA signature

验证DSA签名失败

Failed to set resource limits:

设置资源限制失败

Failed to malloc memory:

分配内存失败

Failed to free memory

释放内存失败

Failed to allocate memory

分配内存失败

Failed to connect to *xx* port *yy*:

向地址*xx*端口*yy*发起连接失败

Failed to setup untrusted X11 forwarding:

无法建立非信任的X11转发

Not supported

该命令不支持

Not supported for SSH protocol version 1

SSH协议版本1不支持

Server does not support re-keying

服务器不支持重新密钥协商

Write failed

写错误

Channel *xx*: unknown channel.

通道号*xx*：未知通道

Unexpected channel *xx*

非期望的通道号*xx*

Couldn\'t get handle:

无法获取到句柄

Failed to close file:

关闭文件失败

Couldn\'t read directory:

读文件目录错误

No such file or directory

在执行remove、get、put、ls、rename等操作时，发现不存在该文件，类似的错误信息还包括：

·End of file：文件末尾；

·Permission denied：拒绝访问；

·Bad message：错误消息；

·No connection：连接未建立

·Connection lost：连接已关闭；

·Operation unsupported：不支持的操作

·Unknown status：未知状态；

·Failure：操作失败

Couldn\'t set state on \\\"*xx*\\\":

设置状态错误，文件名*xx*

Process SSH_FXP_REALPATH error:

处理SSH_FXP_REALPATH消息出错

Couldn\'t rename file \\\"*xx*\\\" to \\\"*yy*\\\"

文件重命名错误，旧文件名为*xx*，新文件名为*yy*

Not support symlink operation

不支持符号连接操作

Couldn\'t symlink file \\\"*xx*\\\" to \\\"*yy*\\\"

符号连接错误，旧文件名为*xx*，新文件名为*yy*

Couldn\'t download non-regular file:

无法下载非正则文件：

Couldn\'t open local file \\\"*xx*\\\" for writing:

无法打开本地文件*xx*去写数据

Couldn\'t read from remote file \\\"*xx*\\\":

无法从远端文件*xx*中读数据

Couldn\'t write to \\\"*xx*\\\":

无法向本地文件*xx*中写数据

Couldn\'t set mode on \\\"*xx*\\\":

设置文件*xx*的模式失败

Can\'t set times on \\\"*xx*\\\":

设置文件*xx*的时间错误

\"Couldn\'t open local file \\\"*xx*\\\" for reading:

无法打开本地文件*xx*去读数据

Couldn\'t get state for local file \\\"*xx*\\\":

无法获取本地文件*xx*的状态

*[xx *]is not a regular file

文件*xx*不是正则文件

Couldn\'t write to remote file \\\"*xx*\\\":

无法向远端文件*xx*写数据

Couldn\'t close local file \\\"*xx*\\\":

无法关闭本地文件*xx*

Invalid path.

路径无效

Invalid flag --*xx*

无效标识

File \\\"*xx*\\\" not found

未找到文件*xx*

Multiple files match, but \\\"*xx*\\\" is not a directory.

匹配到多个文件，但*xx*不是一个目录

Failed to get the file status *xx*:

获取*xx*文件信息失败

Skipping non-regular file *xx*.

跳过非正则文件*xx*

You must specify at least one path after a *xx* command.

*[xx*]命令之后，必须至少指定一个路径

You must specify two paths after a *xx* command.

*[xx*]命令之后，必须至少指定两个路径

You must specify a path after a *xx* command.

*[xx*]命令之后，必须指定一个路径

Failed to connect to host *xx* port *yy*

连接到主机*xx*端口*yy*失败

Permission denied, please try again.

拒绝登录，请重试

Failed to sign and send public key:

签名和发送公钥失败

Failed to send and test public key:

发送和测试公钥失败

Unrecognized authentication method name:

无法识别的认证方法名

Setting tty modes failed:

设置TTY模式失败

Failed to write authentication data

写认证数据失败

Failed to read authentication response length

读认证应答长度失败

Failed to read authentication response

读认证应答失败

Bad string length *xx*

错误的串长度*xx*

Failed to get peer name:

获取对端主机名失败

Non-public channel *xx*, type *yy*

非公用通道号*xx*，类型*yy*

Failed to set socket options SO_REUSEADDR

设置Socket选项SO_REUSEADDR失败

Channel *xx*: connection failed:

通道号*xx*：连接失败

Use of DES is strongly discouraged due to cryptographic weaknesses

不推荐使用DES算法，因为加密强度弱

Kex protocol error:

密钥交换协议错误

Failed to get key type from name:

依据密钥名称获取密钥类型失败

Failed to get key:

获取密钥失败

Unsupported key type *xx*

不支持的密钥类型*xx*

Failed to sign key:

密钥签名失败

Failed to verify key:

密钥验证失败

Failed to get key by name \'*xx*\'

从密钥名字*xx*获取密钥实体失败

Failed to get evpkey:

获取EVP密钥失败

Failed to read the file descriptor flags(*xx*):

读取文件描述符标识*xx*失败

Failed to set the file descriptor flags(*xx*):

设置文件描述符标识*xx*失败

Failed to get socket option TCP_NODELAY:

设置Socket选项TCP_NODELAY失败

Failed to send message

发送消息失败

Failed to receive message header

接收消息头失败

Failed to receive message:

接收消息失败

Channel *xx*: protocol error for unexpected state *yy*

通道号*xx*：错误的状态*yy*导致协议错误

Channel *xx*: read failed for unexpected input state *yy*

通道号*xx*：错误的输入状态*yy*导致读失败

Channel *xx*: protocol error for unexpected output state *yy*

通道号*xx*：错误的输出状态*yy*导致协议错误

Channel *xx*: write failed

通道号*xx*：写错误

Channel *xx*: write failed for unexpected output state *yy*

通道号*xx*：错误的输出状态*yy*导致写错误

Channel *xx*: no empty buffer

通道号*xx*：无缓存

Channel *xx*: internal error for unexpected output state *yy*

通道号*xx*：错误的输出状态*yy*导致内部错误

Channel *xx*: cannot send IEOF for unexpected state *yy*

通道号*xx*：错误的状态*yy*导致无法发送IEOF消息

Channel *xx*: cannot send SSH_MSG_CHANNEL_OUTPUT_CLOSE for unexpected state *yy*

通道号*xx*：错误的状态*yy*导致无法发送消息SSH_MSG_CHANNEL_OUTPUT_CLOSE

Channel *xx*: SSH2_MSG_CHANNEL_CLOSE received twice

通道号*xx*：重复接收到SSH2_MSG_CHANNEL_CLOSE消息

Channel *xx*: write failed for unexpected output state *yy*

通道号*xx*：错误的输出状态*yy*导致写失败

Channel *xx*: cannot send EOF for unexpected input state *yy*

通道号*xx*：错误的输入状态*yy*导致无法发送EOF消息

Channel *xx*: cannot send CLOSE for input state/output state *yy*/*zz*

通道号*xx*：错误的输入状态*xx*/输出状态*yy*导致无法发送关闭消息

Channel *xx*: already sent CLOSE

通道号*xx*：已经发送关闭消息

Channel *xx*: failed to shutdown write:

通道号*xx*：shutdown写失败

Channel *xx*: failed to close write:

通道号*xx*：关闭写失败

Channel *xx*: failed to shutdown read:

通道号*xx*：shutdown读失败

Channel *xx*: failed to close read:

通道号*xx*：关闭读失败

Bad packet length *xx*

错误的包长度*xx*

Failed to set socket option IP_TOS *xx*:

设置Socket选项IP_TOS值*xx*失败

Bad max packet size *xx*

错误的最大包大小*xx*

Failed to ask password:

获取密码失败

Failed to decrypt RSA private key

解密RSA私钥失败

RSA sign failed:

RSA签名失败

Failed to verify RSA:

RSA验证失败

Bad hash length

错误的哈希长度

Bad signature length

错误的签名长度

Failed to decrypt RSA public key:

解密RSA公钥失败

Bad decrypted length *xx*

错误的解密长度*xx*

Hash mismatch

哈希不匹配

Failed to get remote hostname

获取远端主机名失败

Failed to set socket option SO_KEEPALIVE:

设置Socket选项SO_KEEPALIVE失败

Failed to initialize the INOTIFY

初始化INOTIFY失败

Failed to get name info:

获取名称信息失败

Failed to set socket option:

设置Socket选项失败

Failed to change owner *xx* (0 0):

改变owner失败

Failed to change mode *xx* (0666):

改变mode失败

表1-5 debugging ssh client event命令输出信息描述表

字段

描述

No x11 authenticate context

无x11认证上下文

*[xx*] request accepted on channel *yy*

通道号*yy*上接受*xx*请求

Forwarding port

端口转发

Entering interactive session.

进入会话交互阶段

Rekeying in progress

rekey进行中

Transfer complete: sent *xx* bytes, received *yy* bytes, in *zz* seconds

传输完成：在*zz*秒内，发送*xx*字节，接收*yy*字节

Bytes per second: sent *xx*, received *yy*

每秒发送*xx*字节，接收*yy*字节

Requesting tunnel unit *xx* in mode *yy*

以*yy*模式请求隧道单元*xx*

request_type *xx*, want_reply *yy*

请求类型*xx*，是否要求应答*yy*

Client key exchange

客户端密钥交换

Couldn\'t get remote file\'s state:

无法获取远端文件的状态,

Remote version:

对方版本串

Server supports extension \\\"*xx*\\\" revision *yy*

服务器支持扩展*xx*、修订*yy*

Unrecognised server extension \\\"*xx*\\\"

无法识别的服务器扩展*xx*

Sent message *XX*:

发送消息*XX*

Received reply: type *xx*, ID *yy*

接收到应答：类型为*xx*，消息ID为*yy*

Received *XX*:

接收到消息*X*X，可能包括：

SSH2_FXP_STATUS、SSH2_MSG_USERAUTH_BANNER、SSH2_MSG_USERAUTH_SUCCESS、SSH2_MSG_USERAUTH_PK_OK、SSH2_MSG_USERAUTH_PASSWD_CHANGEREQ

Received *xx* SSH2_FXP_NAME responses

接收到x个SSH2_FXP_NAME消息应答

Sending SSH2_FXP_REMOVE \\\"*xx*\\\"

发送消息SSH2_FXP_REMOVE，路径为*xx*

Server version does not support lstat operation

服务器版本不支持lstat操作

Process SSH_FXP_REALPATH: filename *xx* -\> *yy*

处理消息SSH_FXP_REALPATH，原来文件名xx-\>真实文件名yy

Sent message *xx*:

发送消息*xx*

Request data: offset *xx* -\> *yy*

请求偏移*xx* -\> *yy*的数据（*xx*为当前序号，*yy*为最大序号）

Received reply: Type *xx*, ID *yy*, Max_req *zz*

接收到应答：消息类型为*xx*，消息ID为*yy*， 最大序列号*zz*

Received data: offset *xx* -\> *yy*

接收到数据偏移*xx* -\> *yy*的数据（*xx*为当前序号，*yy*为最大序号）

Requesting compression at level *xx*

请求压缩等级*xx*

Remote host refused compression

对方不支持压缩

Requesting PTY

请求PTY

Remote host failed or refused to allocate a pseudo tty

对方分配虚拟TTY失败或拒绝分配

Remote host denied X11 forwarding

对方拒绝x11转发

Remote host denied authentication agent forwarding

对方拒绝认证代理转发

Sending command:

发送命令

Open new channel:

打开新的通道

Connecting to *xx* port *yy*

连接到IP地址*xx、*端口号*yy*

Connection established

连接建立

Remote protocol version *x.y*, remote software version *zz*

对方协议版本号*x.y*,对方软件版本号*zz*

Get self version string *xx*

获取到本端版本串*xx*

Local version string *xx*

本端版本串*xx*

Service accepted:

服务器接受服务

Authentication succeeded (*xx*)

认证成功（认证方法名串为*xx*）

Try authentication method *xx*

尝试认证方法*xx*

Passed a different authentication method list *xx*, preferred *yy*.

服务端给出不同的认证方法列表*xx*，首选*yy*

No more authentication methods to try

无其它可尝试的认证方法

Authentication method *xx* is enabled

使能认证方法*xx*

Channel *xx*:request *yy* confirm *zz*

通道号*xx*：请求*yy*、确认*zz*

Channel *xx*:closing

通道号*xx*：关闭中

Channel *xx*:connected to *yy* port *zz*

通道号*xx*：连接到IP地址*yy*、端口*zz*

Channel *xx*:not open

通道号*xx*：未打开

Channel *xx*:input draining

通道号*xx*：输出关闭中

Channel *xx*:Failed to filter

通道号*xx*：停止过滤

Channel *xx*:window *yy* sent adjust *zz*

通道号*xx*：窗口*yy*发送调整量*zz*

Channel *xx*:garbage collecting

通道号*xx*：资源回收中

Channel *xx*:sent extended data *yy*

通道号*xx*：发送扩展数据*yy*字节

Channel *xx*:accepting extended_data after EOF

通道号*xx*：EOF状态后收到了扩展数据

Channel *xx*:received too much extended data *yy* bytes, window_size *zz*

通道号*xx*：接收太多的扩展数据*yy*，窗口大小*zz*

Channel *xx*:received extended data *yy* bytes

通道号*xx*：接收扩展数据*yy*字节

Channel *xx*:FORCE input drain

通道号*xx*：输入强行关闭

Bad cipher *xx* *yy*

错误的加密套件xx 收到的完整的加密套件串列表*yy*

Enabling compatibility mode for protocol 2.0

使能兼容2.0版本

Enabling compatibility mode for protocol 1.3

使能兼容1.3版本

Enabling compression at level *xx*

使能*xx*等级的压缩算法

Compress outgoing: raw data *xx* bytes, compressed *yy* bytes, factor *zz*

压缩输出：原始数据*xx*字节，压缩后为*yy*字节，比例为*zz*

Compress incoming: raw data *xx* bytes, compressed *yy* bytes, factor *zz*

压缩输入：原始数据*xx*字节，压缩后为*yy*字节，比例为*zz*

Installing CRC compensation attack detector

安装CRC补偿攻击探测器

Kex strings(*xx*):

密钥交互串信息，xx取值代表如下涵义：

·0：密钥交换算法串；

·1：服务器端支持的主机公钥算法串；

·2：客户端到服务器端的加密算法串；

·3：服务器端到客户端的加密算法串；

·4：客户端到服务器端的HMAC算法串；

·5：服务器端到客户端的HMAC算法串；

·6：客户端到服务器端的压缩算法串；

·7：服务器端到客户端的压缩算法串；

·8：客户端到服务器端的语言选择串；

·9：服务器端到客户端的语言选择串

Proposal mismatch:

密钥交互串匹配失败

My proposal kex:

我的密钥交互串

Peer proposal kex:

对方的密钥交互串

Kex: *xx*, Encrypt: *yy*, HMAC: *zz*, Compress: *mm*

密钥交换算法*xx*，加密算法*yy*，摘要算法*zz*，压缩算法*mm*

Bad HAMC *xx* *yy*

错误的摘要算法*xx*摘要算法串*yy*

Send message: type *xx*

发送消息：消息类型*xx*

Channel *xx*:input state: *xx* -\> *yy*

通道号*xx*：输入状态由*xx*状态切换到*yy*

Channel *xx*:output state: *xx* -\> *yy*

通道号*xx*：输出状态由*xx*状态切换到*yy*

Channel *xx*:received *XX*

通道号*xx*：接收到消息*XX*

Channel *xx*: read failed

通道号*xx*：读数据失败

Channel *xx*:send *XX*

通道号*xx*：发送消息*XX*

Channel *xx*:write failed

通道号*xx*：写失败

Channel *xx*:mode=*yy*

通道号*xx*：新的模式*yy*（0和1，分别对应MODE_IN或者MODE_OUT）

Expecting packet type *xx*

期望收到包类型*xx*

Remote message:

远端发来的信息

Set max packet size to *xx*

设置最大包大小为*xx*

Read passphrase:

读取密码

Sent message: type *xx*, ID *yy*

发送消息：类型为*xx*，消息ID为*yy*

DSA verify:

DSA验证

RSA verify

RSA验证

Ignoring unsupported tty mode, opcode *xx*

忽略不支持的TTY模式，操作码为*xx*

Processed SSH2_MSG_USERAUTH_PK_OK message successfully, key finger is *xx*

处理SSH2_MSG_USERAUTH_PK消息成功，密钥指纹串为*xx*

表1-6 debugging ssh client message命令输出信息描述表

字段

描述

Prepare packet*xx*

准备消息消息类型*xx*

Compression: raw_len *xx*, compressed_len *yy*

数据压缩：原始数据大小为*xx*，压缩后数据大小为*yy*

Input: Length before de-compress *xx*, length after de-compress *yy*

输入：解压前数据长度为*xx*，解压后数据长度为*yy*

Received packet type *xx*

接收到消息*xx*

【举例】

\# 打开SSH客户端的错误调试信息开关。设备作为SFTP客户端（IP地址为192.168.0.55）登录远端SFTP服务器（IP地址为192.168.0.59），用户名为abc、密码为abc。

\<Sysname\> debugging ssh client error

\<Sysname\> sftp 192.168.0.59

Username: abc

Connecting to 192.168.0.59 port 22.

The server is not authenticated. Continue? [Y/N:y]

Do you want to save the server public key? [Y/N:n]

abc@192.168.0.59\'s password:

\# 将本地temp.c文件上传到远程SFTP服务器。

sftp\> put temp.c

Failed to put file.

sftp\>

\*Dec 31 18:15:06:374 2009 Sysname SSHC/3/ERROR: Failed to get the file status temp.c: No such file or directory

*// 获取文件状态失败；无法找到文件temp.c*

\# 以列表的形式显示/abcdefg目录下的文件及文件夹的详细信息。

sftp\> dir abcdefg

Failed to list files, \"/abcdefg\" not found.

sftp\>

\*Dec 31 18:15:24:786 2009 Sysname SSHC/3/ERROR: Couldn\'t get remote file status: No such file or directory

*// 获取文件状态失败；无法找到指定文件或目录*

\# 打开SSH客户端的事件调试信息开关。设备作为SFTP客户端（IP地址为192.168.0.55）登录远端SFTP服务器（IP地址为192.168.0.59），用户名为abc、密码为abc。

\<Sysname\> debugging ssh client event

\<Sysname\> ssh 192.168.0.59

Username: abc

\*Dec 31 20:46:58:178 2009 Sysname SSHC/7/EVENT: Connecting to 192.168.0.59 port 22.

\*Dec 31 20:46:58:191 2009 Sysname SSHC/7/EVENT: Connection established.

\*Dec 31 20:46:58:242 2009 Sysname SSHC/7/EVENT: Remote protocol version 1.99, remote software version Comware-5.20

*// 对端协议版本号为1.99（即兼容SSH1和SSH2），对端软件版本串为Comware-5.20（版本串内容与实际的对端产品型号有关，请以设备的实际情况为准）*

\*Dec 31 20:46:58:248 2009 Sysname SSHC/7/EVENT: Enabling compatibility mode for protocol 2.0

\*Dec 31 20:46:58:262 2009 Sysname SSHC/7/EVENT: Get self version string Comware-7

*// 获取到本端软件版本串为Comware-7（版本串内容与实际的对端产品型号有关，请以设备的实际情况为准）*

\*Dec 31 20:46:58:278 2009 Sysname SSHC/7/EVENT: Local version string SSH-2.0-Comware-7

\*Dec 31 20:46:58:314 2009 Sysname SSHC/7/EVENT: Received SSH2_MSG_KEXINIT.

\*Dec 31 20:46:58:322 2009 Sysname SSHC/7/EVENT: My proposal kex:

*// 客户端的版本协商算法串信息如下*

\*Dec 31 20:46:58:331 2009 Sysname SSHC/7/EVENT: Kex strings(0): diffie-hellman-group-exchange-sha1,diffie-hellman-group14-sha1,diffie-hellman-group1-sha1

*// 密钥交换算法串*

\*Dec 31 20:46:58:338 2009 Sysname SSHC/7/EVENT: Kex strings(1): ssh-dss,ssh-rsa

*// 服务器端支持的主机公钥算法串*

\*Dec 31 20:46:58:358 2009 Sysname SSHC/7/EVENT: Kex strings(2): aes128-cbc,3des-cbc,des-cbc

*// 客户端到服务器端的加密算法串*

\*Dec 31 20:46:58:369 2009 Sysname SSHC/7/EVENT: Kex strings(3): aes128-cbc,3des-cbc,des-cbc

*// 服务器端到客户端的加密算法串*

\*Dec 31 20:46:58:394 2009 Sysname SSHC/7/EVENT: Kex strings(4): hmac-sha1,hmac-sha1-96,hmac-md5,hmac-md5-96

*// 客户端到服务器端的HMAC算法串*

\*Dec 31 20:46:58:404 2009 Sysname SSHC/7/EVENT: Kex strings(5): hmac-sha1,hmac-sha1-96,hmac-md5,hmac-md5-96

*// 服务器端到客户端的HMAC算法串*

\*Dec 31 20:46:58:421 19692009 Sysname SSHC/7/EVENT: Kex strings(6): none,zlib,zlib@openssh.com

*// 客户端到服务器端的压缩算法串*

\*Dec 31 20:46:58:426 2009 Sysname SSHC/7/EVENT: Kex strings(7): none,zlib,zlib@openssh.com

*// 服务器端到客户端的压缩算法串*

\*Dec 31 20:46:58:440 2009 Sysname SSHC/7/EVENT: Kex strings(8):

\*Dec 31 20:46:58:446 2009 Sysname SSHC/7/EVENT: Kex strings(9):

\*Dec 31 20:46:58:452 2009 Sysname SSHC/7/EVENT: Peer proposal kex:

*// 服务器端的版本协商算法串信息如下*

\*Dec 31 20:46:58:460 2009 Sysname SSHC/7/EVENT: Kex strings(0): diffie-hellman-group-exchange-sha1,diffie-hellman-group14-sha1,diffie-hellman-group1-sha1

*// 密钥交换算法串*

\*Dec 31 20:46:58:463 2009 Sysname SSHC/7/EVENT: Kex strings(1): ssh-dss,ssh-rsa

*// 服务器端支持的主机公钥算法串*

\*Dec 31 20:46:58:468 2009 Sysname SSHC/7/EVENT: Kex strings(2): aes128-cbc,3des-cbc,des-cbc

*// 客户端到服务器端的加密算法串*

\*Dec 31 20:46:58:475 2009 Sysname SSHC/7/EVENT: Kex strings(3): aes128-cbc,3des-cbc,des-cbc

*// 服务器端到客户端的加密算法串*

\*Dec 31 20:46:58:477 2009 Sysname SSHC/7/EVENT: Kex strings(4): hmac-sha1,hmac-sha1-96,hmac-md5,hmac-md5-96

*// 客户端到服务器端的HMAC算法串*

\*Dec 31 20:46:58:480 2009 Sysname SSHC/7/EVENT: Kex strings(5): hmac-sha1,hmac-sha1-96,hmac-md5,hmac-md5-96

*// 服务器端到客户端的HMAC算法串*

\*Dec 31 20:46:58:484 2009 Sysname SSHC/7/EVENT: Kex strings(6): none

*// 客户端到服务器端的压缩算法串*

\*Dec 31 20:46:58:486 2009 Sysname SSHC/7/EVENT: Kex strings(7): none

*// 服务器端到客户端的压缩算法串*

\*Dec 31 20:46:58:494 2009 Sysname SSHC/7/EVENT: Kex strings(8):

\*Dec 31 20:46:58:497 2009 Sysname SSHC/7/EVENT: Kex strings(9):

\*Dec 31 20:46:58:499 2009 Sysname SSHC/7/EVENT: Kex: server-\>client, Encrypt: aes128-cbc, HMAC: hmac-sha1, Compress: none

*// 协商出来的服务器端到客户端的加密算法、HMAC算法和压缩算法*

\*Dec 31 20:46:58:502 2009 Sysname SSHC/7/EVENT: Kex: client-\>server, Encrypt: aes128-cbc, HMAC: hmac-sha1, Compress: none

*// 协商出来的客户端到服务器端的加密算法、HMAC算法和压缩算法*

\*Dec 31 20:46:58:504 2009 Sysname SSHC/7/EVENT: Expecting packet type 31.

\*Dec 31 20:47:01:576 2009 Sysname SSHC/7/EVENT: Expecting packet type 33.

The server is not authenticated. Continue? [Y/N:y]

Do you want to save the server public key? [Y/N:n]

\*Dec 31 20:47:07:612 2009 Sysname SSHC/7/EVENT: DSA verify: signature correct

*// 进行DSA认证，签名正确*

\*Dec 31 20:47:07:634 2009 Sysname SSHC/7/EVENT: Set new keys: mode=1

*// 设置协商出来的新的算法（mode=1表示输出方向）*

\*Dec 31 20:47:07:643 2009 Sysname SSHC/7/EVENT: Expecting packet type 21.

\*Dec 31 20:47:07:649 2009 Sysname SSHC/7/EVENT: Set new keys: mode=0

*// 设置协商出来的新的算法（mode=0表示输入方向）*

\*Dec 31 20:47:07:831 2009 Sysname SSHC/7/EVENT: Service accepted: reply ssh-userauth

\*Dec 31 20:47:07:859 2009 Sysname SSHC/7/EVENT: Received SSH2_MSG_USERAUTH_FAILURE.

\*Dec 31 20:47:07:866 2009 Sysname SSHC/7/EVENT: Authentication methods that can continue to try: password

*// 认证失败，可以继续尝试的认证方法为password认证*

\*Dec 31 20:47:07:871 2009 Sysname SSHC/7/EVENT: Passed a different authentication method list password, preferred publickey,password.

*// 传入了一个不同的认证方法列表password，但支持的认证方法是publickey、password*

\*Dec 31 20:47:07:877 2009 Sysname SSHC/7/EVENT: Authentication method password is enabled.

*[// Password*]*认证被使能*

abc@192.168.0.59\'s password:

\*Dec 31 20:47:09:166 2009 Sysname SSHC/7/EVENT: Try authentication method password.

*// 尝试Password认证*

\*Dec 31 20:47:09:181 2009 Sysname SSHC/7/EVENT: Received SSH2_MSG_USERAUTH_SUCCESS.

\*Dec 31 20:47:09:185 2009 Sysname SSHC/7/EVENT: Authentication succeeded (password).

\*Dec 31 20:47:09:194 2009 Sysname SSHC/7/EVENT: Channel 0: new [client-session]

\*Dec 31 20:47:09:196 2009 Sysname SSHC/7/EVENT: Open new channel: 0.

\*Dec 31 20:47:09:203 2009 Sysname SSHC/7/EVENT: Entering interactive session.

\*Dec 31 20:47:09:249 2009 Sysname SSHC/7/EVENT: Channel 0: request pty-req confirm 1

\*Dec 31 20:47:09:254 2009 Sysname SSHC/7/EVENT: Channel 0: request shell confirm 1

\*Dec 31 20:47:09:272 2009 Sysname SSHC/7/EVENT: PTY allocation request accepted on channel 0

\*Dec 31 20:47:09:377 2009 Sysname SSHC/7/EVENT: shell request accepted on channel 0

*[// Password*]*认证成功，shell请求被接受，分配通道号为0*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Copyright (c) 2004-2010 Hangzhou Sysname Tech. Co., Ltd. All rights reserved.  \*

\* Without the owner\'s prior written consent,                                 \*

\* no decompiling or reverse-engineering shall be allowed.                    \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\<Sysname\>

*// 用户abc成功登录设备*

\# 打开SSH客户端的消息调试信息开关。设备作为SFTP客户端（IP地址为192.168.0.55）登录远端SFTP服务器（IP地址为192.168.0.59），用户名为abc、密码为abc。

\<Sysname\> debugging ssh client message

\<Sysname\> sftp 192.168.0.59

Username: abc

Connecting to 192.168.0.59 port 22.

\*Dec 31 16:11:03:507 2009 Sysname SSHC/7/MESSAGE: Prepare packet[20.]

*// 准备消息，消息类型为20（以下各消息涵义类似，解释略）*

\*Dec 31 16:11:03:510 2009 Sysname SSHC/7/MESSAGE: Received packet type 20.

*// 接收到消息，消息类型为20（以下各消息涵义类似，解释略）*

\*Dec 31 16:11:03:518 2009 Sysname SSHC/7/MESSAGE:Prepare packet34.

\*Dec 31 16:11:03:625 2009 Sysname SSHC/7/MESSAGE: Received packet type 31.

\*Dec 31 16:11:05:218 2009 Sysname SSHC/7/MESSAGE: Prepare packet[32.]

\*Dec 31 16:11:05:466 2009 Sysname SSHC/7/MESSAGE: Received packet type 33.

The server is not authenticated. Continue? [Y/N:y]

Do you want to save the server public key? [Y/N:n]

\*Dec 31 16:11:09:252 2009 Sysname SSHC/7/MESSAGE: Prepare packet[21.]

\*Dec 31 16:11:09:255 2009 Sysname SSHC/7/MESSAGE: Received packet type 21.

\*Dec 31 16:11:09:256 2009 Sysname SSHC/7/MESSAGE: Prepare packet[5.]

\*Dec 31 16:11:09:266 2009 Sysname SSHC/7/MESSAGE: Received packet type 6.

\*Dec 31 16:11:09:282 2009 Sysname SSHC/7/MESSAGE: Prepare packet[50.]

\*Dec 31 16:11:09:287 2009 Sysname SSHC/7/MESSAGE: Received packet type 51.

abc@192.168.0.59\'s password:

\*Dec 31 16:11:11:184 2009 Sysname SSHC/7/MESSAGE: Prepare packet[50.]

\*Dec 31 16:11:11:193 2009 Sysname SSHC/7/MESSAGE: Received packet type 52.

\*Dec 31 16:11:11:194 2009 Sysname SSHC/7/MESSAGE: Prepare packet[90.]

\*Dec 31 16:11:11:197 2009 Sysname SSHC/7/MESSAGE: Received packet type 91.

\*Dec 31 16:11:11:201 2009 Sysname SSHC/7/MESSAGE: Prepare packet[98.]

\*Dec 31 16:11:11:205 2009 Sysname SSHC/7/MESSAGE: Received packet type 99.

\*Dec 31 16:11:11:209 2009 Sysname SSHC/7/MESSAGE: Received packet type 94.sftp\>

\*Dec 31 16:11:11:219 2009 Sysname SSHC/7/MESSAGE: Received packet type 94.

sftp\>

