
**SSL \-- SSL服务器端策略配置命令 \-- ciphersuite**

------------------------------------------------------------------------

**[ciphersuite**]命令用来配置SSL服务器端策略支持的加密套件。

**[undo ciphersuite**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[ciphersuite**[ { **dhe_rsa_aes_128_cbc_sha** \| **dhe_rsa_aes_256_cbc_sha** \| **exp_rsa_des_cbc_sha** \| **exp_rsa_rc2_md5** \| **exp_rsa_rc4_md5** \| **rsa_3des_ede_cbc_sha** \| **rsa_aes_128_cbc_sha** \| **rsa_aes_256_cbc_sha** \| **rsa_des_cbc_sha** \| **rsa_rc4_128_md5** \| **rsa_rc4_128_sha** } \*]]

**[undo ciphersuite**]

FIPS模式下：

**[ciphersuite**[ { **dhe_rsa_aes_128_cbc_sha** \| **dhe_rsa_aes_256_cbc_sha** \| **rsa_aes_128_cbc_sha** \| **rsa_aes_256_cbc_sha** } \*]]

**[undo ciphersuite**]

【缺省情况】

SSL服务器端策略支持所有的加密套件。

【视图】

SSL服务器端策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[dhe_rsa_aes_128_cbc_sha**]：密钥交换算法采用DHE RSA、数据加密算法采用128位的AES、MAC算法采用SHA。

**[dhe_rsa_aes_256_cbc_sha**]：密钥交换算法采用DHE RSA、数据加密算法采用256位的AES、MAC算法采用SHA。

**[exp_rsa_des_cbc_sha**]：满足出口限制的算法套件。密钥交换算法采用RSA、数据加密算法采用DES_CBC、MAC算法采用SHA。

**[exp_rsa_rc2_md5**]：满足出口限制的算法套件。密钥交换算法采用RSA、数据加密算法采用RC2、MAC算法采用MD5。

**[exp_rsa_rc4_md5**]：满足出口限制的算法套件。密钥交换算法采用RSA、数据加密算法采用RC4、MAC算法采用MD5。

**[rsa_3des_ede_cbc_sha**]：密钥交换算法采用RSA、数据加密算法采用3DES_EDE_CBC、MAC算法采用SHA。

**[rsa_aes_128_cbc_sha**]：密钥交换算法采用RSA、数据加密算法采用128位AES_CBC、MAC算法采用SHA。

**[rsa_aes_256_cbc_sha**]：密钥交换算法采用RSA、数据加密算法采用256位AES_CBC、MAC算法采用SHA。

**[rsa_des_cbc_sha**]：密钥交换算法采用RSA、数据加密算法采用DES_CBC、MAC算法采用SHA。

**[rsa_rc4_128_md5**]：密钥交换算法采用RSA、数据加密算法采用128位的RC4、MAC算法采用MD5。

**[rsa_rc4_128_sha**]：密钥交换算法采用RSA、数据加密算法采用128位的RC4、MAC算法采用SHA。

【使用指导】

为了提高安全性，SSL协议采用了如下算法：

·数据加密算法：用来对传输的数据进行加密，以保证数据传输的私密性。常用的数据加密算法通常为对称密钥算法，如DES_CBC、3DES_EDE_CBC、AES_CBC、RC4等。使用对称密钥算法时，要求SSL服务器端和SSL客户端具有相同的密钥。

·MAC（Message Authentication Code，消息验证码）算法：用来计算数据的MAC值，以防止发送的数据被篡改。常用的MAC算法有MD5、SHA等。使用MAC算法时，要求SSL服务器端和SSL客户端具有相同的密钥。

·密钥交换算法：用来实现密钥交换，以保证对称密钥算法、MAC算法中使用的密钥在SSL服务器端和SSL客户端之间安全地传递。常用的密钥交换算法通常为非对称密钥算法，如RSA。

通过本命令可以配置SSL服务器端策略支持的各种算法组合。例如，**rsa_des_cbc_sha**表示SSL服务器端策略支持的密钥交换算法为RSA、数据加密算法为DES_CBC、MAC算法为SHA。

SSL服务器接收到SSL客户端发送的客户端加密套件后，将服务器支持的加密套件与SSL客户端支持的加密套件比较。如果SSL服务器支持的加密套件中存在SSL客户端支持的加密套件，则加密套件协商成功；否则，加密套件协商失败。

需要注意的是，如果多次执行本命令，则新的配置覆盖原有配置。

【举例】

\# 指定SSL服务器端策略支持如下加密套件：

·密钥交换算法为DHE RSA、数据加密算法为128位的AES、MAC算法为SHA

·密钥交换算法为RSA、数据加密算法为128位的AES、MAC算法为SHA

\<Sysname\> system-view

Sysname ssl server-policy policy1

Sysname-ssl-server-policy-policy1 ciphersuite dhe_rsa_aes_128_cbc_sha rsa_aes_128_cbc_sha

【相关命令】

·**display ssl server-policy**

·**prefer-cipher**

**SSL \-- SSL服务器端策略配置命令 \-- client-verify enable**

------------------------------------------------------------------------

**[client-verify enable**]命令用来配置SSL服务器端要求对SSL客户端进行基于数字证书的身份验证。**undo client-verify enable**命令用来恢复缺省情况。

【命令】

**[client-verify enable**]

**[undo client-verify enable**]

【缺省情况】

SSL服务器端不要求对SSL客户端进行基于数字证书的身份验证。

【视图】

SSL服务器端策略视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

SSL通过数字证书实现对对端的身份进行验证。数字证书的详细介绍，请参见"安全配置指导"中的"PKI"。

如果执行了**client-verify enable**命令，则SSL客户端必须将自己的数字证书提供给服务器，以便服务器对客户端进行基于数字证书的身份验证。只有身份验证通过后，SSL客户端才能访问SSL服务器。

SSL服务器端在基于数字证书对SSL客户端进行身份验证时，除了对SSL客户端发送的证书链进行验证，还要检查证书链中的除根CA证书外的每个证书是否均未被吊销。

【举例】

\# 配置SSL服务器端要求对SSL客户端进行基于数字证书的身份验证。

\<Sysname\> system-view

Sysname ssl server-policy policy1

Sysname-ssl-server-policy-policy1 client-verify enable

【相关命令】

·**display ssl server-policy**

**SSL \-- SSL服务器端策略配置命令 \-- display ssl server-policy**

------------------------------------------------------------------------

**[display ssl server-policy**]命令用来显示SSL服务器端策略的信息。

【命令】

**[display ssl server-policy ** *policy-name* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[policy-name*]：显示指定的SSL服务器端策略的信息，为1～31个字符的字符串，不区分大小写。如果不指定本参数，则显示所有SSL服务器端策略的信息。

【举例】

\# 显示名为policy1的SSL服务器端策略的信息。

\<Sysname\> display ssl server-policy policy1

 SSL server policy: policy1

     PKI domain: server-domain

     Ciphersuites:

         DHE_RSA_AES_128_CBC_SHA

         RSA_AES_128_CBC_SHA

     Session cache size: 600

     Caching timeout: 3600 seconds

     Client-verify: enabled

表1-1 display ssl server-policy命令显示信息描述表

字段

描述

SSL server policy

SSL服务器端策略名

PKI domain

SSL服务器端策略使用的PKI域

Ciphersuites

SSL服务器端策略支持的加密套件

Session cache size

SSL服务器端可以缓存的最大会话数目

Caching timeout

SSL服务器端会话缓存超时时间（单位为秒）

Client-verify

SSL服务器端策略的客户端验证模式，取值包括：

·disabled：不要求对客户端进行基于数字证书的身份验证

·enabled：要求对客户端进行基于数字证书的身份验证

**SSL \-- SSL服务器端策略配置命令 \-- pki-domain (SSL server policy view)**

------------------------------------------------------------------------

**[pki-domain**]命令用来配置SSL服务器端策略所使用的PKI域。

**[undo pki-domain**]命令用来恢复缺省情况。

【命令】

**[pki-domain ***domain-name*]

**[undo pki-domain**]

【缺省情况】

没有指定SSL服务器端策略所使用的PKI域。

【视图】

SSL服务器端策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[domain-name*]：PKI域的域名，为1～31个字符的字符串，不区分大小写。

【使用指导】

如果通过本命令指定了SSL服务器端策略使用的PKI域，则引用该服务器端策略的SSL服务器将通过该PKI域获取服务器端的数字证书。

【举例】

\# 配置SSL服务器端策略所使用的PKI域为server-domain。

\<Sysname\> system-view

Sysname ssl server-policy policy1

Sysname-ssl-server-policy-policy1 pki-domain server-domain

【相关命令】

·**display ssl server-policy**

·**pki domain**（安全命令参考/PKI）

**SSL \-- SSL服务器端策略配置命令 \-- session**

------------------------------------------------------------------------

**[session**]命令用来配置SSL服务器上可以缓存的最大会话数目和SSL会话缓存的超时时间。

**[undo session**]命令用来恢复缺省情况。

【命令】

**[session ****[cachesize ***size *[\| **timeout** *time* } \*]]

**[undo session ****[cachesize **[\| **timeout** } \*]]

【缺省情况】]

SSL]服务器上可以缓存的最大会话数目为500个，SSL会话缓存的超时时间为3600秒。

【视图】

SSL服务器端策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cachesize ***size*]：指定SSL服务器上可以缓存的最大会话数目。*size*为缓存的最大会话数目，取值范围为100～20480。

**[timeout** *time*]：指定SSL会话缓存的超时时间。*time*为会话缓存超时时间，取值范围为1～4294967295，单位为秒。

【使用指导】

通过SSL握手协议协商会话参数并建立会话的过程比较复杂。为了简化SSL握手过程，SSL允许重用已经协商出的会话参数建立会话。为此，SSL服务器上需要保存已有的会话信息。保存的会话信息的数目和保存时间具有一定的限制：

·如果缓存的会话数目达到最大值，SSL将拒绝缓存新协商出的会话。

·会话保存的时间超过设定的时间后，SSL将删除该会话的信息。

【举例】

\# 配置SSL服务器上可以缓存的最大会话数目为600个，SSL会话缓存超时时间为1800秒。

\<Sysname\> system-view

Sysname ssl server-policy policy1

Sysname-ssl-server-policy-policy1 session cachesize 600 timeout 1800

【相关命令】

·**display ssl server-policy**

**SSL \-- SSL服务器端策略配置命令 \-- ssl server-policy**

------------------------------------------------------------------------

**[ssl server-policy**]命令用来创建SSL服务器端策略，并进入SSL服务器端策略视图。

**[undo ssl server-policy**]命令用来删除已创建的SSL服务器端策略。

【命令】

**[ssl server-policy** *policy-name*]

**[undo ssl server-policy** *policy-name*]

【缺省情况】

设备上不存在任何SSL服务器端策略。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：SSL服务器端策略名，为1～31个字符的字符串，不区分大小写。

【使用指导】

SSL服务器端策略视图下可以配置SSL服务器启动时使用的SSL参数，如使用的PKI域、支持的加密套件等。只有与HTTPS等应用关联后，SSL服务器端策略才能生效。

【举例】

\# 创建SSL服务器端策略policy1，并进入SSL服务器端策略视图。

\<Sysname\> system-view

Sysname ssl server-policy policy1

Sysname-ssl-server-policy-policy1

【相关命令】

·**display ssl server-policy**

**SSL \-- SSL客户端策略配置命令 \-- display ssl client-policy**

------------------------------------------------------------------------

**[display ssl client-policy**]命令用来显示SSL客户端策略的信息。

【命令】

**[display ssl client-policy ** *policy-name* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[policy-name*]：显示指定的SSL客户端策略的信息，为1～31个字符的字符串，不区分大小写。如果不指定本参数，则显示所有SSL客户端策略的信息。

【举例】

\# 显示名为policy1的SSL客户端策略的信息。

\<Sysname\> display ssl client-policy policy1

 SSL client policy: policy1

     SSL version: SSL 3.0

     PKI domain: client-domain

     Preferred ciphersuite:

         RSA_AES_128_CBC_SHA

     Server-verify: enabled

表1-2 display ssl client-policy命令显示信息描述表

字段

描述

SSL client policy

SSL客户端策略名

SSL version

SSL客户端策略使用的SSL协议版本

PKI domain

SSL客户端策略使用的PKI域

Preferred ciphersuite

SSL客户端策略支持的加密套件

Server-verify

SSL客户端策略的服务器端验证模式，取值包括：

·disabled：不要求对SSL服务器进行基于数字证书的身份验证

·enabled：要求对SSL服务器进行基于数字证书的身份验证

**SSL \-- SSL客户端策略配置命令 \-- pki-domain (SSL client policy view)**

------------------------------------------------------------------------

**[pki-domain**]命令用来配置SSL客户端策略所使用的PKI域。

**[undo pki-domain**]命令用来恢复缺省情况。

【命令】

**[pki-domain ***domain-name*]

**[undo pki-domain**]

【缺省情况】

没有指定SSL客户端策略所使用的PKI域。

【视图】

SSL客户端策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[domain-name*]：PKI域的域名，为1～31个字符的字符串，不区分大小写。

【使用指导】

如果通过本命令指定了SSL客户端策略使用的PKI域，则引用该客户端策略的SSL客户端将通过该PKI域获取客户端的数字证书。

【举例】

\# 配置SSL客户端策略所使用的PKI域为client-domain。

\<Sysname\> system-view

Sysname ssl client-policy policy1

Sysname-ssl-client-policy-policy1 pki-domain client-domain

【相关命令】

·**display ssl client-policy**

·**pki domain**（安全命令参考/PKI）

**SSL \-- SSL客户端策略配置命令 \-- prefer-cipher**

------------------------------------------------------------------------

**[prefer-cipher**]命令用来配置SSL客户端策略支持的加密套件。

**[undo prefer-cipher**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[prefer-cipher**[ { **dhe_rsa_aes_128_cbc_sha** \| **dhe_rsa_aes_256_cbc_sha** \| **exp_rsa_des_cbc_sha** \| **exp_rsa_rc2_md5** \| **exp_rsa_rc4_md5** \| **rsa_3des_ede_cbc_sha** \| **rsa_aes_128_cbc_sha** \| **rsa_aes_256_cbc_sha** \| **rsa_des_cbc_sha** \| **rsa_rc4_128_md5** \| **rsa_rc4_128_sha** }]]

**[undo prefer-cipher**]

FIPS模式下：

**[prefer-cipher**[ { **dhe_rsa_aes_128_cbc_sha** \| **dhe_rsa_aes_256_cbc_sha** \| **rsa_aes_128_cbc_sha** \| **rsa_aes_256_cbc_sha** }]]

**[undo prefer-cipher**]

【缺省情况】

非FIPS模式下：

SSL客户端策略支持的加密套件为**rsa_rc4_128_md5**。

FIPS模式下：

SSL客户端策略支持的加密套件为**rsa_aes_128_cbc_sha**。

【视图】

SSL客户端策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[dhe_rsa_aes_128_cbc_sha**]：密钥交换算法采用DHE RSA、数据加密算法采用128位的AES、MAC算法采用SHA。

**[dhe_rsa_aes_256_cbc_sha**]：密钥交换算法采用DHE RSA、数据加密算法采用256位的AES、MAC算法采用SHA。

**[exp_rsa_des_cbc_sha**]：满足出口限制的算法套件。密钥交换算法采用RSA、数据加密算法采用DES_CBC、MAC算法采用SHA。

**[exp_rsa_rc2_md5**]：满足出口限制的算法套件。密钥交换算法采用RSA、数据加密算法采用RC2、MAC算法采用MD5。

**[exp_rsa_rc4_md5**]：满足出口限制的算法套件。密钥交换算法采用RSA、数据加密算法采用RC4、MAC算法采用MD5。

**[rsa_3des_ede_cbc_sha**]：密钥交换算法采用RSA、数据加密算法采用3DES_EDE_CBC、MAC算法采用SHA。

**[rsa_aes_128_cbc_sha**]：密钥交换算法采用RSA、数据加密算法采用128位AES_CBC、MAC算法采用SHA。

**[rsa_aes_256_cbc_sha**]：密钥交换算法采用RSA、数据加密算法采用256位AES_CBC、MAC算法采用SHA。

**[rsa_des_cbc_sha**]：密钥交换算法采用RSA、数据加密算法采用DES_CBC、MAC算法采用SHA。

**[rsa_rc4_128_md5**]：密钥交换算法采用RSA、数据加密算法采用128位的RC4、MAC算法采用MD5。

**[rsa_rc4_128_sha**]：密钥交换算法采用RSA、数据加密算法采用128位的RC4、MAC算法采用SHA。

【使用指导】

为了提高安全性，SSL协议采用了如下算法：

·数据加密算法：用来对传输的数据进行加密，以保证数据传输的私密性。常用的数据加密算法通常为对称密钥算法，如DES_CBC、3DES_EDE_CBC、AES_CBC、RC4等。使用对称密钥算法时，要求SSL服务器端和SSL客户端具有相同的密钥。

·MAC（Message Authentication Code，消息验证码）算法：用来计算数据的MAC值，以防止发送的数据被篡改。常用的MAC算法有MD5、SHA等。使用MAC算法时，要求SSL服务器端和SSL客户端具有相同的密钥。

·密钥交换算法：用来实现密钥交换，以保证对称密钥算法、MAC算法中使用的密钥在SSL服务器端和SSL客户端之间安全地传递。常用的密钥交换算法通常为非对称密钥算法，如RSA。

通过本命令可以配置SSL客户端策略支持的算法组合。例如，**rsa_des_cbc_sha**表示SSL客户端支持的密钥交换算法为RSA、数据加密算法为DES_CBC、MAC算法为SHA。

SSL客户端将本端支持的加密套件发送给SSL服务器，SSL服务器将自己支持的加密套件与SSL客户端支持的加密套件比较。如果SSL服务器支持的加密套件中存在SSL客户端支持的加密套件，则加密套件协商成功；否则，加密套件协商失败。

需要注意的是，如果多次执行本命令，则新的配置覆盖原有配置。

【举例】

\# 配置SSL客户端策略支持的加密套件为：密钥交换算法采用RSA、数据加密算法采用128位AES_CBC、MAC算法采用SHA。

\<Sysname\> system-view

Sysname ssl client-policy policy1

Sysname-ssl-client-policy-policy1 prefer-cipher rsa_aes_128_cbc_sha

【相关命令】

·**ciphersuite**

·**display ssl client-policy**

**SSL \-- SSL客户端策略配置命令 \-- server-verify enable**

------------------------------------------------------------------------

**[server-verify enable**]命令用来配置客户端需要对服务器端进行基于数字证书的身份验证。

**[undo server-verify enable**]命令用来配置客户端不要求对服务器端进行基于数字证书的身份验证，默认SSL服务器身份合法。

【命令】

**[server-verify enable**]

**[undo server-verify enable**]

【缺省情况】

SSL客户端需要对SSL服务器端进行基于数字证书的身份验证。

【视图】

SSL客户端策略视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

SSL通过数字证书实现对对端的身份进行验证。数字证书的详细介绍，请参见"安全配置指导"中的"PKI"。

如果执行了**server-verify enable**命令，则SSL服务器端需要将自己的数字证书提供给客户端，以便客户端对服务器端进行基于数字证书的身份验证。只有身份验证通过后，SSL客户端才会访问该SSL服务器。

【举例】

\# 配置SSL客户端需要对SSL服务器端进行基于数字证书的身份验证。

\<Sysname\> system-view

Sysname ssl client-policy policy1

Sysname-ssl-client-policy-policy1 server-verify enable

【相关命令】

·**display ssl client-policy**

**SSL \-- SSL客户端策略配置命令 \-- ssl client-policy**

------------------------------------------------------------------------

**[ssl client-policy**]命令用来创建SSL客户端策略，并进入SSL客户端策略视图。

**[undo ssl client-policy**]命令用来删除已创建的SSL客户端策略。

【命令】

**[ssl client-policy** *policy-name*]

**[undo ssl client-policy** *policy-name*]

【缺省情况】

设备上不存在任何SSL客户端策略。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：SSL客户端策略名，为1～31个字符的字符串，不区分大小写。

【使用指导】

SSL客户端策略视图下可以配置SSL客户端启动时使用的SSL参数，如使用的PKI域、支持的加密套件等。只有与应用层协议，如DDNS（Dynamic Domain Name System，动态域名系统），关联后，SSL客户端策略才能生效。

【举例】

\# 创建SSL客户端策略policy1，并进入SSL客户端策略视图。

\<Sysname\> system-view

Sysname ssl client-policy policy1

Sysname-ssl-client-policy-policy1

【相关命令】

·**display ssl client-policy**

**SSL \-- SSL客户端策略配置命令 \-- version**

------------------------------------------------------------------------

**[version**]命令用来配置SSL客户端策略使用的SSL协议版本。

**[undo version**]命令恢复缺省情况。

【命令】

非FIPS模式下：

**[version**[ { **ssl3.0** \| **tls1.0** }]]

**[undo version**]

FIPS模式下：

**[version tls1.0**]

**[undo version**]

【缺省情况】

SSL客户端策略使用的SSL协议版本为TLS 1.0。

【视图】

SSL客户端策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ssl3.0**]：版本为SSL 3.0。

**[tls1.0**]：版本为TLS 1.0。

【使用指导】

如果多次执行本命令，则新的配置覆盖原有配置。

【举例】

\# 配置SSL客户端策略使用的SSL协议版本为TLS 1.0。

\<Sysname\> system-view

Sysname ssl client-policy policy1

Sysname-ssl-client-policy-policy1 version tls1.0

【相关命令】

·**display ssl client-policy**
