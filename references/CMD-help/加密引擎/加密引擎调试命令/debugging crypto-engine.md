<!-- CMD-INDEX
  debugging crypto-engine             | 用户视图             | L5
-->

**加密引擎 \-- 加密引擎调试命令 \-- debugging crypto-engine**

------------------------------------------------------------------------

【命令】

**[debugging crypto-engine**[ { **all** \| **error** \| **event** \| **packet** }]]

**[undo debugging crypto-engine **[{ **all** \| **error** \| **event** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示加密引擎所有调试信息开关。

**[error**]：表示加密引擎错误调试信息开关。

**[event**]：表示加密引擎事件调试信息开关。

**[packet**]：表示加密引擎报文调试信息开关。

【描述】

debugging crypto-engine命令用来打开IPsec调试信息开关。undo debugging crypto-engine命令用来关闭加密引擎调试信息开关。

缺省情况下，加密引擎的调试信息开关处于关闭状态。

表1-1 debugging crypto-engine error命令输出信息描述表

字段

描述

Failed to insert crypto engine, can\'t alloc driver structure.

插入加密引擎失败，无法创建驱动结构

Failed to insert crypto engine, can\'t insert driver struct into driver array.

插入加密引擎失败，无法将驱动结构插入驱动数组

Failed to create new session in driver, driver ID=*driver-id*.

驱动新建会话失败，驱动编号为*driver-id*

Failed to add session to session array.

将会话加入会话数组失败

Failed to allocate session, algorithm ID=*alg-id*.

创建会话失败，算法ID为*alg-id*

Failed to select crypto engine, flag=*flag-id*.

选择加密引擎失败，加密引擎标识为*flag-id*

First algorithm: algorithm ID=*alg-id*, required hash length =*hash-len*, key length=*key-len*.

第一个算法：算法ID为*alg-id*，需要的哈希长度为*hash-len*，密钥长度为*key-len*

Second algorithm: algorithm ID=*alg-id*, required hash length=*hash-len*, key length=*key-len*.

第二个算法：算法ID为*alg-id*，需要的哈希长度为*hash-len*，密钥长度为*key-len*

Can\'t get session during symmetric encryption, session handle=*session-id*.

对称加密过程中找不到会话，会话句柄为*session-id*

Can\'t get driver during symmetric encryption, driver ID=*drv-id*, session handle=*session-id*.

对称加密过程中找不到驱动，驱动ID为*drv-id*会话句柄为*session-id*

Failed to reselect crypto engine, original driver ID=*drv-id*, session handle=*session-id*.

重新选择加密引擎失败，原始驱动ID为*drv-id*会话句柄为*session-id*

Failed to check symmetric Job, driver ID=*drv-id*.

检查对称job失败，驱动ID为*drv-id*

First describer: algorithm ID=*alg-id*, required hash length=*hash-len*, skip length=*skip-len*, process length=*process-len*, inject position=*inject-position*, flag=*flag*, key length=*key-len*.

第一个描述符：算法ID为*alg-id*，需要的哈希长度为*hash-len*，跳过的长度为*skip-len*，处理的长度为*process-len*，插入的位置为*inject-position*，标识为*flag*，密钥长度为*key-len*

Second describer: algorithm ID=*alg-id*, required hash length=*hash-len*, skip length=*skip-len*, process length=*process-len*, inject position=*inject-position*,flag=*flag*, key length=*key-len*.

第二个描述符：算法ID为*alg-id*，需要的哈希长度为*hash-len*，跳过的长度为*skip-len*，处理的长度为*process-len*，插入的位置为*inject-position*，标识为*flag*，密钥长度为*key-len*

Symmetric Job: data type=*type*, input buffer length=*input-buff-len*, output buffer length=*output-buff-len*.

对称Job：数据类型为*type*，输入缓冲区的长度*input-buff-len*， 输出缓冲区的长度为*output-buff-len*

Failed to insert crypto engine, invalid engine flag=*flag*, name=*drv-name*.

插入加密引擎失败，无效的加密引擎标识为*flag*，加密引擎名字为*drv-name*

Failed to remove crypto engine *engine-name*, invalid engine id=*engine-id*.

拔除加密引擎*engine-name*失败，无效的加密引擎ID为*engine-id*、

Failed to register software crypto engine.

注册软件加密引擎失败

表1-2 debugging crypto engine event命令输出信息描述表

字段

描述

New session created on crypto engine(ID =*engine-id*), flag=*flag*.

新会话已成功在加密引擎*engine-id*上创建，标识为*flag*

Crypto engine *engine-name* inserted, driver ID=*driver-id*.

加密引擎*engine-name*插入成功，驱动ID为*driver-id*

Crypto engine(ID =*engine-id*) is removed.

加密引擎*engine-id*已被拔出

First algorithm: algorithm ID=*alg-id*, required hash length=*hash-len*, key length=*key-len*.

第一个算法：算法ID为*alg-id*，需要的哈希长度为*hash-len*，密钥长度为*key-len*

Second algorithm: algorithm ID=*alg-id*, required hash length=*hash-len*, key length=*key-len*.

第二个算法：算法ID为*alg-id*，需要的哈希长度为*hash-len*，密钥长度为*key-len*

表1-3 debugging crypto engine packet命令输出信息描述表

字段

描述

Symmetric encryption: Job doesn\'t contain key, previous crypto engine ID=*engine-id*.

对称加密：任务缺少密钥。之前使用的加密引擎ID为*engine-id*

Symmetric encryption: Reselecting crypto engine failed, previous crypto engine ID=*engine-id*.

对称加密：重新选择加密引擎失败。之前使用的加密引擎ID为*engine-id*

Symmetric encryption: New crypto engine failed to create session, first algorithm ID=*alg-id*, crypto engine ID=*engine-id*.

对称加密：新加密引擎创建会话失败。第一个算法ID为*alg-id*，加密引擎ID为*engine-id*

Symmetric encryption: Reselecting crypto engine successfully, previous crypto engine ID=*old-engine-id*, new crypto engine ID=*new-engine-id*,.

对称加密：重新选择加密引擎成功。之前的加密引擎ID为*old-engine-id*，新加密引擎ID为*new-engine-id*

Symmetric operation finished, driver return= *return-code*, driver ID=*driver-id*, driver flag =*driver-flag*.

对称算法操作完成，驱动返回值为 *return-code*，驱动ID为*driver-id*，驱动标识为*driver-flag*

Job validity check failed, algorithm ID=*alg-id*, base length=*base-len*, mod length=*mod*, exp length=*exp-leng*, out buffer length =*outbuff-len*, flag=*flag*.

任务合法性检查失败：算法ID为*alg-id*，基数长度为*base-length*，模为*mod*，指数长度为*exp-length*，输出缓冲区长度为*outbuff-len*，标识为*flag*

Asymmetric encryption failed: Can't select a crypto engine, algorithm ID=*alg-id*, flag=*flag*.

非对称加密失败：无法选择加密引擎，使用算法ID为*alg，*标识为*flag*

Asymmetric operation finished, base length=*base-len*, mod length=*mod*, exp length=*exp-len*, driver return=*return-code*.

非对称加密完成，基数长度为*base-len*，模为*mod*，指数长度为*exp-len*，驱动返回值为*driver-return*

【举例】

\# 在设备上插入一个硬件加密引擎，并打开加密引擎错误调试信息开关。

\<Sysname\> debugging crypto-engine error

\* Dec 16 14:40:24:162 2012 Sysname CCF/7/Error: -MDC=1;

Failed to insert crypto engine, can\'t allocate driver structure.

*// 插入加密引擎失败，无法分配驱动结构*

**

\# 在设备上配置手工方式的IPsec安全策略mypolicy，并打开加密引擎事件调试信息开关。当将策略mypolicy应用于接口Ethernet1/2上时，会生成IPsec SA，输出如下调试信息。

\<Sysname\> debugging crypto-engine event

\<Sysname\> system-view

Sysname interface ethernet 1/2

Sysname-Ethernet1/2 ipsec policy mypolicy

\*Dec 16 16:44:24:162 2012 Sysname CCF/7/event:

New session created on crypto engine(ID=00), flag=21.

*// 新会话成功在加密引擎0上建立，加密引擎标识为21*

\*Dec 16 16:44:24:162 2012 Sysname Sysname /7/event:

First algorithm: algorithm ID=4, required hash length=0, key length=24.

*// 第一个算法：算法ID为4，需要的哈希长度为0，密钥长度为24*

\*Dec 16 16:44:24:162 2012 Sysname CCF/7/event:

Second algorithm: algorithm ID=17, required hash length=12, key length=20.

*// 第二个算法：算法ID为17，需要的哈希长度为12，密钥长度为20*

\*Dec 16 16:44:24:162 2012 Sysname CCF/7/event:

New session created on crypto engine(ID=0), flag=21.

*// 新会话成功在加密引擎0上建立，加密引擎标识为21*

\*Dec 16 16:44:24:162 2012 Sysname CCF/7/event:

First algorithm: algorithm ID= 17, required hash length=12, key length=20.

*// 第一个算法：算法ID为17，需要的哈希长度为12，密钥长度为20*

\*Dec 16 16:44:24:162 2012 Sysname CCF/7/event:

Second algorithm: algorithm ID=4, required hash length=0, key length=24.

*// 第二个算法：算法ID为4，需要的哈希长度为0，密钥长度为24*

**

\# 在设备上配置IPsec隧道，生成SA并建立CCF会话，打开crypto-engine的报文调试信息开关。当从本机ping对端的时候，输出如下调试信息。

\<Sysname\> debugging crypto-engine packet

Sysname ping -c 1 -a 18.18.18.1 19.19.19.1

PING 19.19.19.1 (19.19.19.1) from 18.18.18.1: 56 data bytes, press CTRL_C to break

56 bytes from 19.19.19.1: icmp_seq=0 ttl=255 time=0.945 ms

\-\-- 19.19.19.1 ping statistics \-\--

1 packet(s) transmitted, 1 packet(s) received, 0.0% packet loss

round-trip min/avg/max/std-dev = 0.945/0.945/0.945/0.000 ms

\*Dec 22 18:59:41:199 2012 Sysname CCF/7/packet:

First describer: algorithm ID=4, required hash length=0, skip length=36, process length=88, inject position36, flag=1, key length=24.

*// 第一个描述符：算法ID为4，需要的哈希长度为0，跳过的长度为36，处理的长度为88，插入的位置为36，标识为1，密钥长度为24*

\*Dec 22 18:59:41:199 2012 Sysname CCF/7/packet:

Second describer: algorithm ID=17, required hash length=12, skip length=20, process length=104, inject position=124, flag=0, key length=20.

*// 第二个描述符：算法ID为17，需要的哈希长度为12，跳过的长度为20，处理的长度104，插入的位置为124，标识为0，密钥长度为20*

\*Dec 22 18:59:41:199 2012 Sysname CCF/7/packet:

Symmetric Job: data type=MBuf, input buffer length=136, output buffer length=136.

*// 对称任务：数据类型为MBuf，输入缓冲区的长度为136，输出缓冲区的长度为136*

\*Dec 22 18:59:41:199 2012 Sysname CCF/7/packet:

Symmetric operation finished, driver return=0, driver ID=0, driver flag=21.

*// 对称操作完成，驱动返回值为0，驱动ID为0，驱动标识为21*

\*Dec 22 18:59:41:199 2012 Sysname CCF/7/packet:

First describer: algorithm ID=17, required hash length=12, skip length=20, process length=104, inject position=124, flag=0, key length=20.

*// 第一个描述符：算法ID为17，需要的哈希长度为12，跳过的长度为20，处理的长度为104，插入的位置为124，标识为0，密钥长度为20*

\*Dec 22 18:59:41:199 2012 Sysname CCF/7/packet:

Second describer: algorithm ID=4, required hash length=0, skip length=36, process length=88, inject position=36, flag=0, key length=24.

*// 第二个描述符：算法ID为4，需要的哈希长度为0，跳过的长度为36，处理的长度为88，插入的位置为36，标识为0，密钥长度为24*

\*Dec 22 18:59:41:199 2012 Sysname CCF/7/packet:

Symmetric Job: data type=MBuf, input buffer length=136, output buffer length=136.

*// 对称任务：数据类型为MBuf，输入缓冲区的长度136，输出缓冲区的长度136*

\*Dec 22 18:59:41:199 2012 Sysname CCF/7/packet:

Symmetric operation finished, driver return=0, driver id=0, driver flag=21.

*// 对称操作完成，驱动返回值为0，驱动ID为0，驱动标识为21*

