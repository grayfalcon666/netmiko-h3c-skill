::: {#707895659 .myid}
[]{#_Toc404793319}[]{#struct_0_85589_x1131_x2075000515}[]{#_Toc279416408}[]{#_Toc257792939}[]{#_Toc168802546}

**SSL \-- SSL服务器端策略配置命令 \-- ciphersuite**

------------------------------------------------------------------------

[**[ciphersuite]{lang="EN-US"}**]{#struct_0_85589_x1131_x633948861}[命令用来配置]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略支持的加密套件。]{style="font-family:宋体"}

[**[undo ciphersuite]{lang="EN-US"}**]{#struct_0_85589_x1131_1127807904}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_85589_x1131_1306836541}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_85589_x1131_x134214628}[模式下：]{style="font-family:宋体"}

[**[ciphersuite]{lang="EN-US"}**[ { **dhe_rsa_aes_128_cbc_sha** \| **dhe_rsa_aes_256_cbc_sha** \| **exp_rsa_des_cbc_sha** \| **exp_rsa_rc2_md5** \| **exp_rsa_rc4_md5** \| **rsa_3des_ede_cbc_sha** \| **rsa_aes_128_cbc_sha** \| **rsa_aes_256_cbc_sha** \| **rsa_des_cbc_sha** \| **rsa_rc4_128_md5** \| **rsa_rc4_128_sha** } \*]{lang="EN-US"}]{#struct_0_85589_x1131_x1148186749}

[**[undo ciphersuite]{lang="EN-US"}**]{#struct_0_85589_x1131_1163179850}

[[FIPS]{lang="EN-US"}]{#struct_0_85589_x1131_282207093}[模式下：]{style="font-family:宋体"}

[**[ciphersuite]{lang="EN-US"}**[ { **dhe_rsa_aes_128_cbc_sha** \| **dhe_rsa_aes_256_cbc_sha** \| **rsa_aes_128_cbc_sha** \| **rsa_aes_256_cbc_sha** } \*]{lang="EN-US"}]{#struct_0_85589_x1131_737093474}

[**[undo ciphersuite]{lang="EN-US"}**]{#struct_0_85589_x1131_x1228345646}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_85589_x1131_1266382613}

[[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_1560755494}[服务器端策略支持所有的加密套件。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_85589_x1131_1127611296}

[[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_x1404590016}[服务器端策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x532381592}

[[network-admin]{lang="EN-US"}]{#struct_0_85589_x1131_x929927763}

[[mdc-admin]{lang="EN-US"}]{#struct_0_85589_x1131_492932380}

[[【参数】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x1518109553}

[**[dhe_rsa_aes_128_cbc_sha]{lang="EN-US"}**]{#struct_0_85589_x1131_1113870462}[：密钥交换算法采用]{style="font-family:宋体"}[DHE RSA]{lang="EN-US"}[、数据加密算法采用]{style="font-family:宋体"}[128]{lang="EN-US"}[位的]{style="font-family:宋体"}[AES]{lang="EN-US"}[、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[算法采用]{style="font-family:宋体"}[SHA]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[dhe_rsa_aes_256_cbc_sha]{lang="EN-US"}**]{#struct_0_85589_x1131_x1940585437}[：密钥交换算法采用]{style="font-family:宋体"}[DHE RSA]{lang="EN-US"}[、数据加密算法采用]{style="font-family:宋体"}[256]{lang="EN-US"}[位的]{style="font-family:宋体"}[AES]{lang="EN-US"}[、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[算法采用]{style="font-family:宋体"}[SHA]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[exp_rsa_des_cbc_sha]{lang="EN-US"}**]{#struct_0_85589_x1131_x1751146993}[：满足出口限制的算法套件。密钥交换算法采用]{style="font-family:宋体"}[RSA]{lang="EN-US"}[、数据加密算法采用]{style="font-family:宋体"}[DES_CBC]{lang="EN-US"}[、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[算法采用]{style="font-family:宋体"}[SHA]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[exp_rsa_rc2_md5]{lang="EN-US"}**]{#struct_0_85589_x1131_1127676832}[：满足出口限制的算法套件。密钥交换算法采用]{style="font-family:宋体"}[RSA]{lang="EN-US"}[、数据加密算法采用]{style="font-family:宋体"}[RC2]{lang="EN-US"}[、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[算法采用]{style="font-family:宋体"}[MD5]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[exp_rsa_rc4_md5]{lang="EN-US"}**]{#struct_0_85589_x1131_905529957}[：满足出口限制的算法套件。密钥交换算法采用]{style="font-family:宋体"}[RSA]{lang="EN-US"}[、数据加密算法采用]{style="font-family:宋体"}[RC4]{lang="EN-US"}[、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[算法采用]{style="font-family:宋体"}[MD5]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[rsa_3des_ede_cbc_sha]{lang="EN-US"}**]{#struct_0_85589_x1131_1843491609}[：密钥交换算法采用]{style="font-family:宋体"}[RSA]{lang="EN-US"}[、数据加密算法采用]{style="font-family:宋体"}[3DES_EDE_CBC]{lang="EN-US"}[、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[算法采用]{style="font-family:宋体"}[SHA]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[rsa_aes_128_cbc_sha]{lang="EN-US"}**]{#struct_0_85589_x1131_x723404819}[：密钥交换算法采用]{style="font-family:宋体"}[RSA]{lang="EN-US"}[、数据加密算法采用]{style="font-family:宋体"}[128]{lang="EN-US"}[位]{style="font-family:宋体"}[AES_CBC]{lang="EN-US"}[、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[算法采用]{style="font-family:宋体"}[SHA]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[rsa_aes_256_cbc_sha]{lang="EN-US"}**]{#struct_0_85589_x1131_26619628}[：密钥交换算法采用]{style="font-family:宋体"}[RSA]{lang="EN-US"}[、数据加密算法采用]{style="font-family:宋体"}[256]{lang="EN-US"}[位]{style="font-family:宋体"}[AES_CBC]{lang="EN-US"}[、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[算法采用]{style="font-family:宋体"}[SHA]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[rsa_des_cbc_sha]{lang="EN-US"}**]{#struct_0_85589_x1131_x1390007077}[：密钥交换算法采用]{style="font-family:宋体"}[RSA]{lang="EN-US"}[、数据加密算法采用]{style="font-family:宋体"}[DES_CBC]{lang="EN-US"}[、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[算法采用]{style="font-family:宋体"}[SHA]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[rsa_rc4_128_md5]{lang="EN-US"}**]{#struct_0_85589_x1131_402187581}[：密钥交换算法采用]{style="font-family:宋体"}[RSA]{lang="EN-US"}[、数据加密算法采用]{style="font-family:宋体"}[128]{lang="EN-US"}[位的]{style="font-family:宋体"}[RC4]{lang="EN-US"}[、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[算法采用]{style="font-family:宋体"}[MD5]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[rsa_rc4_128_sha]{lang="EN-US"}**]{#struct_0_85589_x1131_x1183793243}[：密钥交换算法采用]{style="font-family:宋体"}[RSA]{lang="EN-US"}[、数据加密算法采用]{style="font-family:宋体"}[128]{lang="EN-US"}[位的]{style="font-family:宋体"}[RC4]{lang="EN-US"}[、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[算法采用]{style="font-family:宋体"}[SHA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x879068665}

[[为了提高安全性，]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_1128004512}[协议采用了如下算法：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[数据加密算法：用来对传输的数据进行加密，以保证数据传输的私密性。常用的数据加密算法通常为对称密钥算法，如]{style="font-family:宋体"}]{#struct_0_85589_x1131_x387882637}[DES_CBC]{lang="EN-US"}[、]{style="font-family:宋体"}[3DES_EDE_CBC]{lang="EN-US"}[、]{style="font-family:宋体"}[AES_CBC]{lang="EN-US"}[、]{style="font-family:宋体"}[RC4]{lang="EN-US"}[等。使用对称密钥算法时，要求]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端和]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端具有相同的密钥。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MAC]{lang="EN-US"}]{#struct_0_85589_x1131_916937785}[（]{lang="EN-US" style="font-family:
宋体"}[Message Authentication Code]{lang="EN-US"}[，消息验证码）算法：用来计算数据的]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[值，以防止发送的数据被篡改。常用的]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[算法有]{lang="EN-US" style="font-family:宋体"}[MD5]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[SHA]{lang="EN-US"}[等。]{lang="EN-US" style="font-family:宋体"}[使用]{style="font-family:宋体"}[MAC]{lang="EN-US"}[算法时，要求]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端和]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端具有相同的密钥。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[密钥交换算法：用来实现密钥交换，以保证对称密钥算法、]{style="font-family:宋体"}]{#struct_0_85589_x1131_x269704655}[MAC]{lang="EN-US"}[算法中使用的密钥在]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端和]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端之间安全地传递。常用的密钥交换算法通常为非对称密钥算法，如]{style="font-family:宋体"}[RSA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[通过本命令可以配置]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_x1701252144}[服务器端策略支持的各种算法组合。例如]{style="font-family:宋体"}[，]{style="font-family:宋体"}**[rsa_des_cbc_sha]{lang="FR"}**[表示]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略支持的密钥交换算法为]{style="font-family:宋体"}[RSA]{lang="EN-US"}[、数据加密算法为]{style="font-family:宋体"}[DES_CBC]{lang="EN-US"}[、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[算法为]{style="font-family:宋体"}[SHA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_x2107687149}[服务器接收到]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端发送的客户端加密套件后，将服务器支持的加密套件与]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端支持的加密套件比较。如果]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器支持的加密套件中存在]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端支持的加密套件，则加密套件协商成功；否则，加密套件协商失败。]{style="font-family:宋体"}

[[需要注意的是，如果多次执行本命令，则新的配置覆盖原有配置。]{style="font-family:宋体"}]{#struct_0_85589_x1131_1675343597}

[[【举例】]{style="font-family:黑体"}]{#struct_0_85589_x1131_1966778811}

[[\# ]{lang="EN-US"}]{#struct_0_85589_x1131_2105716372}[指定]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略支持如下加密套件：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[密钥交换算法为]{style="font-family:宋体"}]{#struct_0_85589_x1131_x235405179}[DHE RSA]{lang="EN-US"}[、数据加密算法为]{style="font-family:宋体"}[128]{lang="EN-US"}[位的]{style="font-family:宋体"}[AES]{lang="EN-US"}[、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[算法为]{style="font-family:宋体"}[SHA]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[密钥交换算法为]{style="font-family:宋体"}]{#struct_0_85589_x1131_1128070048}[RSA]{lang="EN-US"}[、数据加密算法为]{style="font-family:宋体"}[128]{lang="EN-US"}[位的]{style="font-family:宋体"}[AES]{lang="EN-US"}[、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[算法为]{style="font-family:宋体"}[SHA]{lang="EN-US"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_85589_x1131_353711076}

[\[Sysname\] ssl server-policy policy1]{lang="EN-US"}

[\[Sysname-ssl-server-policy-policy1\] ciphersuite dhe_rsa_aes_128_cbc_sha rsa_aes_128_cbc_sha]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x1922691981}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ssl server-policy]{lang="EN-US"}**]{#struct_0_85589_x1131_x1835384323}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[prefer-cipher]{lang="EN-US"}**]{#struct_0_85589_x1131_1658474974}
:::

::: {#-1786049235 .myid}
[]{#_Toc404793320}[]{#struct_0_85589_x1131_x1574809057}[]{#_Toc291852148}[]{#_Toc297019335}

**SSL \-- SSL服务器端策略配置命令 \-- client-verify enable**

------------------------------------------------------------------------

[**[client-verify enable]{lang="EN-US"}**]{#struct_0_85589_x1131_x702042672}[命令用来配置]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端要求对]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端进行基于数字证书的身份验证。]{style="font-family:宋体"}**[undo client-verify enable]{lang="EN-US"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_85589_x1131_1825638214}

[**[client-verify enable]{lang="EN-US"}**]{#struct_0_85589_x1131_1127873440}

[**[undo client-verify enable]{lang="EN-US"}**]{#struct_0_85589_x1131_x628846419}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x1773987674}

[[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_809055564}[服务器端不要求对]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端进行基于数字证书的身份验证。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_85589_x1131_1752813502}

[[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_1794426423}[服务器端策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_85589_x1131_838418784}

[[network-admin]{lang="EN-US"}]{#struct_0_85589_x1131_238743279}

[[mdc-admin]{lang="EN-US"}]{#struct_0_85589_x1131_x1414495688}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x560120816}

[[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_1127938976}[通过数字证书实现对对端的身份进行验证。数字证书的详细介绍，请参见"安全配置指导"中的"]{style="font-family:宋体"}[PKI]{lang="EN-US"}["。]{style="font-family:宋体"}

[[如果执行了]{style="font-family:宋体"}**[client-verify enable]{lang="EN-US"}**]{#struct_0_85589_x1131_94820244}[命令，则]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端必须将自己的数字证书提供给服务器，以便服务器对客户端进行基于数字证书的身份验证。只有身份验证通过后，]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端才能访问]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_x1893686077}[服务器端在基于数字证书对]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端进行身份验证时，除了对]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端发送的证书链进行验证，还要检查证书链中的除根]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书外的每个证书是否均未被吊销。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x868730103}

[[\# ]{lang="EN-US"}]{#struct_0_85589_x1131_x1449909913}[配置]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端要求对]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端进行基于数字证书的身份验证。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_85589_x1131_x1993527032}

[\[Sysname\] ssl server-policy policy1]{lang="EN-US"}

[\[Sysname-ssl-server-policy-policy1\] client-verify enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x993591627}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ssl server-policy]{lang="EN-US"}**]{#struct_0_85589_x1131_x1971670679}
:::

::: {#-813227298 .myid}
[]{#_Toc404793321}[]{#struct_0_85589_x1131_306905398}[]{#_Toc291852150}[]{#_Toc297019337}[]{#_Toc291852151}[]{#_Toc297019338}[]{#_Toc291852152}[]{#_Toc297019339}[]{#_Toc291852153}[]{#_Toc297019340}[]{#_Toc291852154}[]{#_Toc297019341}[]{#_Toc291852155}[]{#_Toc297019342}[]{#_Toc291852156}[]{#_Toc297019343}[]{#_Toc291852157}[]{#_Toc297019344}[]{#_Toc291852158}[]{#_Toc297019345}[]{#_Toc291852159}[]{#_Toc297019346}[]{#_Toc291852160}[]{#_Toc297019347}

**SSL \-- SSL服务器端策略配置命令 \-- display ssl server-policy**

------------------------------------------------------------------------

[**[display ssl server-policy]{lang="EN-US"}**]{#struct_0_85589_x1131_1128266656}[命令用来]{style="font-family:
宋体"}[显示]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x1949873425}

[**[display ssl server-policy ]{lang="EN-US"}**[\[ *policy-name* \]]{lang="EN-US"}]{#struct_0_85589_x1131_x775634837}

[[【视图】]{style="font-family:黑体"}]{#struct_0_85589_x1131_1378997547}

[[任意视图]{style="font-family:宋体"}]{#struct_0_85589_x1131_x1023051029}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x46482276}

[[network-admin]{lang="EN-US"}]{#struct_0_85589_x1131_x1560999172}

[[network-operator]{lang="EN-US"}]{#struct_0_85589_x1131_1903696471}

[[mdc-admin]{lang="EN-US"}]{#struct_0_85589_x1131_x1556214569}

[[mdc-operator]{lang="EN-US"}]{#struct_0_85589_x1131_2108762114}

[[【参数】]{style="font-family:黑体"}]{#struct_0_85589_x1131_1128332192}

[*[policy-name]{lang="EN-US"}*]{#struct_0_85589_x1131_x431809230}[：显示指定的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略的信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。如果不指定本参数，则显示所有]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x1015606443}

[[\# ]{lang="EN-US"}]{#struct_0_85589_x1131_x1580920045}[显示名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略的信息。]{style="font-family:宋体"}

[[\<Sysname\> display ssl server-policy policy1]{lang="EN-US"}]{#struct_0_85589_x1131_x1732773177}

[ SSL server policy: policy1]{lang="EN-US"}

[     PKI domain: server-domain]{lang="EN-US"}

[     Ciphersuites:]{lang="EN-US"}

[         DHE_RSA_AES_128_CBC_SHA]{lang="EN-US"}

[         RSA_AES_128_CBC_SHA]{lang="EN-US"}

[     Session cache size: 600]{lang="EN-US"}

[     Caching timeout: 3600 seconds]{lang="EN-US"}

[     Client-verify: enabled]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display ssl server-policy]{lang="EN-US"}]{#struct_0_85589_x1131_x261892869}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1135432039}[[字段]{style="font-family:黑体"}]{#struct_0_85589_x1131_x1136456964}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_85589_x1131_1127742369}

[[SSL server policy]{lang="EN-US"}]{#struct_0_85589_x1131_x1016456005}

[[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_x1410845565}[服务器端策略名]{style="font-family:宋体"}

[[PKI domain]{lang="EN-US"}]{#struct_0_85589_x1131_x1274719197}

[[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_689739685}[服务器端策略使用的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域]{style="font-family:宋体"}

[[Ciphersuites]{lang="EN-US"}]{#struct_0_85589_x1131_x479648834}

[[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_x1301455386}[服务器端策略支持的加密套件]{style="font-family:宋体"}

[[Session cache size]{lang="EN-US"}]{#struct_0_85589_x1131_1127807905}

[[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_1306902077}[服务器端可以缓存的最大会话数目]{style="font-family:宋体"}

[[Caching timeout]{lang="EN-US"}]{#struct_0_85589_x1131_1258989770}

[[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_254235690}[服务器端会话缓存超时时间（单位为秒）]{style="font-family:宋体"}

[[Client-verify]{lang="EN-US"}]{#struct_0_85589_x1131_x1256965744}

[[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_x251183163}[服务器端策略的客户端验证模式，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[disabled]{lang="EN-US"}]{#struct_0_85589_x1131_x1117481937}[：不要求对客户端进行基于数字证书的身份验证]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[enabled]{lang="EN-US"}]{#struct_0_85589_x1131_x1961123797}[：要求对客户端进行基于数字证书的身份验证]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1021747253 .myid}
[]{#_Toc404793322}[]{#struct_0_85589_x1131_1127611297}[]{#_Toc297019349}[]{#_Toc291852162}[]{#_Toc297019350}[]{#_Toc291852164}[]{#_Toc297019352}[]{#_Toc291852165}[]{#_Toc297019353}[]{#_Toc291852166}[]{#_Toc297019354}[]{#_Toc291852167}[]{#_Toc297019355}[]{#_Toc291852168}[]{#_Toc297019356}[]{#_Toc291852169}[]{#_Toc297019357}[]{#_Toc291852170}[]{#_Toc297019358}[]{#_Toc291852171}[]{#_Toc297019359}[]{#_Toc291852172}[]{#_Toc297019360}[]{#_Toc291852173}[]{#_Toc297019361}[]{#_Toc291852174}[]{#_Toc297019362}[]{#_Toc291852175}[]{#_Toc297019363}[]{#_Toc291852176}[]{#_Toc297019364}

**SSL \-- SSL服务器端策略配置命令 \-- pki-domain (SSL server policy view)**

------------------------------------------------------------------------

[**[pki-domain]{lang="EN-US"}**]{#struct_0_85589_x1131_x1404655552}[命令用来配置]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略所使用的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域。]{style="font-family:宋体"}

[**[undo pki-domain]{lang="EN-US"}**]{#struct_0_85589_x1131_673636763}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x2119263964}

[**[pki-domain ]{lang="EN-US"}***[domain-name]{lang="EN-US"}*]{#struct_0_85589_x1131_1783400958}

[**[undo pki-domain]{lang="EN-US"}**]{#struct_0_85589_x1131_x1444907286}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_85589_x1131_1722644387}

[[没有指定]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_x810786503}[服务器端策略所使用的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x287130634}

[[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_1127676833}[服务器端策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_85589_x1131_905464421}

[[network-admin]{lang="EN-US"}]{#struct_0_85589_x1131_x1990299638}

[[mdc-admin]{lang="EN-US"}]{#struct_0_85589_x1131_x686335179}

[[【参数】]{style="font-family:黑体"}]{#struct_0_85589_x1131_1188924328}

[*[domain-name]{lang="EN-US"}*]{#struct_0_85589_x1131_x1103804235}[：]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域的域名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_85589_x1131_621562110}

[[如果通过本命令指定了]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_1163948511}[服务器端策略使用的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域，则引用该服务器端策略的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器将通过该]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域获取服务器端的数字证书。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_85589_x1131_1805757902}

[[\# ]{lang="EN-US"}]{#struct_0_85589_x1131_1128004513}[配置]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略所使用的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域为]{style="font-family:宋体"}[server-domain]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_85589_x1131_x387817101}

[\[Sysname\] ssl server-policy policy1]{lang="EN-US"}

[\[Sysname-ssl-server-policy-policy1\] pki-domain server-domain]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_85589_x1131_495231807}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ssl server-policy]{lang="EN-US"}**]{#struct_0_85589_x1131_1104524480}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pki domain]{lang="EN-US"}**]{#struct_0_85589_x1131_x1420036677}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/PKI]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#-1088603561 .myid}
[]{#_Toc404793323}[]{#struct_0_85589_x1131_x701429221}[]{#_Toc279416453}[]{#_Toc257792949}

**SSL \-- SSL服务器端策略配置命令 \-- session**

------------------------------------------------------------------------

[**[session]{lang="EN-US"}**]{#struct_0_85589_x1131_x1231222058}[命令用来配置]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器上可以缓存的最大会话数目]{style="font-family:宋体"}[和]{style="font-family:宋体"}[SSL]{lang="EN-US"}[会话缓存的超时时间]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo session]{lang="EN-US"}**]{#struct_0_85589_x1131_x1125181468}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x1678491117}

[**[session ]{lang="EN-US"}**[{ ]{lang="EN-US"}**[cachesize ]{lang="EN-US"}***[size ]{lang="EN-US"}*[\| **timeout** *time* } \*]{lang="EN-US"}]{#struct_0_85589_x1131_1128070049}

[**[undo session ]{lang="EN-US"}**[{ ]{lang="EN-US"}**[cachesize ]{lang="EN-US"}**[\| **timeout** } \*]{lang="EN-US"}]{#struct_0_85589_x1131_353645540}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_85589_x1131_792774165}

[[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_x1673359827}[服务器上可以缓存的最大会话数目为]{style="font-family:宋体"}[500]{lang="EN-US"}[个，]{style="font-family:宋体"}[SSL]{lang="EN-US"}[会话缓存的超时时间为]{style="font-family:宋体"}[3600]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_85589_x1131_1549615429}

[[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_212788672}[服务器端策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_85589_x1131_175848739}

[[network-admin]{lang="EN-US"}]{#struct_0_85589_x1131_1005450328}

[[mdc-admin]{lang="EN-US"}]{#struct_0_85589_x1131_x1193401496}

[[【参数】]{style="font-family:黑体"}]{#struct_0_85589_x1131_1127873441}

[**[cachesize ]{lang="EN-US"}***[size]{lang="EN-US"}*]{#struct_0_85589_x1131_x628911955}[：指定]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器上可以缓存的最大会话数目。]{style="font-family:宋体"}*[size]{lang="EN-US"}*[为]{style="font-family:宋体"}[缓存的最大会话数目，取值范围为]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[20480]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[timeout]{lang="EN-US"}**[ *time*]{lang="EN-US"}]{#struct_0_85589_x1131_x1516882216}[：指定]{style="font-family:宋体"}[SSL]{lang="EN-US"}[会话缓存的超时时间。]{style="font-family:宋体"}*[time]{lang="EN-US"}*[为]{style="font-family:宋体"}[会话缓存超时时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x1849854382}

[[通过]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_376611376}[握手协议协商会话参数并建立会话的过程比较复杂。为了简化]{style="font-family:宋体"}[SSL]{lang="EN-US"}[握手过程，]{style="font-family:宋体"}[SSL]{lang="EN-US"}[允许重用已经协商出的会话参数建立会话。为此，]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器上需要保存已有的会话信息。保存的会话信息的数目和保存时间具有一定的限制：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果缓存的会话数目达到最大值，]{lang="EN-US" style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_x1922783224}[将拒绝缓存新协商出的会话。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[会话保存的时间超过设定的时间后，]{lang="EN-US" style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_1002836718}[将删除该会话的信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_85589_x1131_1849993461}

[[\# ]{lang="EN-US"}]{#struct_0_85589_x1131_x1899049450}[配置]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器上可以缓存的最大会话数目为]{style="font-family:宋体"}[600]{lang="EN-US"}[个，]{style="font-family:宋体"}[SSL]{lang="EN-US"}[会话缓存超时时间为]{style="font-family:宋体"}[1800]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_85589_x1131_x1538020824}

[\[Sysname\] ssl server-policy policy1]{lang="EN-US"}

[\[Sysname-ssl-server-policy-policy1\] session cachesize 600 timeout 1800]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_85589_x1131_1203537820}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ssl server-policy]{lang="EN-US"}**]{#struct_0_85589_x1131_x1566736106}
:::

::: {#-866773307 .myid}
[]{#_Toc279163110}[]{#struct_0_85589_x1131_1127938977}[]{#_Toc404793324}[]{#_Toc297019367}

**SSL \-- SSL服务器端策略配置命令 \-- ssl server-policy**

------------------------------------------------------------------------

[**[ssl server-policy]{lang="EN-US"}**]{#struct_0_85589_x1131_94754708}[命令用来创建]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略，并进入]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略视图。]{style="font-family:宋体"}

[**[undo ssl server-policy]{lang="EN-US"}**]{#struct_0_85589_x1131_x709155282}[命令用来删除已创建的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_85589_x1131_2130786269}

[**[ssl server-policy]{lang="EN-US"}**[ *policy-name*]{lang="EN-US"}]{#struct_0_85589_x1131_x1295442101}

[**[undo ssl server-policy]{lang="EN-US"}**[ *policy-name*]{lang="EN-US"}]{#struct_0_85589_x1131_x148760412}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x687337102}

[[设备上不存在任何]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_428384889}[服务器端策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_85589_x1131_1020443688}

[[系统视图]{style="font-family:宋体"}]{#struct_0_85589_x1131_1128266657}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x1949807889}

[[network-admin]{lang="EN-US"}]{#struct_0_85589_x1131_517666310}

[[mdc-admin]{lang="EN-US"}]{#struct_0_85589_x1131_1270192484}

[[【参数】]{style="font-family:黑体"}]{#struct_0_85589_x1131_147856918}

[*[policy-name]{lang="EN-US"}*]{#struct_0_85589_x1131_282204921}[：]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x897564461}

[[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_x1644431244}[服务器端策略视图下可以配置]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器启动时使用的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[参数，如使用的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域、支持的加密套件等。只有与]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[等应用关联后，]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x2109786372}

[[\# ]{lang="EN-US"}]{#struct_0_85589_x1131_1128332193}[创建]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略]{style="font-family:宋体"}[policy1]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_85589_x1131_x431874766}

[\[Sysname\] ssl server-policy policy1]{lang="EN-US"}

[\[Sysname-ssl-server-policy-policy1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_85589_x1131_225513641}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ssl server-policy]{lang="EN-US"}**]{#struct_0_85589_x1131_x1349690228}
:::

::: {#1979822502 .myid}
[]{#_Toc404793326}[]{#struct_0_85589_x1131_27104868}

**SSL \-- SSL客户端策略配置命令 \-- display ssl client-policy**

------------------------------------------------------------------------

[**[display ssl client-policy]{lang="EN-US"}**]{#struct_0_85589_x1131_x29303231}[命令用来显示]{style="font-family:
宋体"}[SSL]{lang="EN-US"}[客户端策略的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_85589_x1131_341326858}

[**[display ssl client-policy ]{lang="EN-US"}**[\[ *policy-name* \] ]{lang="EN-US"}]{#struct_0_85589_x1131_308257089}

[[【视图】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x1601140983}

[[任意视图]{style="font-family:宋体"}]{#struct_0_85589_x1131_1565363270}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x576081472}

[[network-admin]{lang="EN-US"}]{#struct_0_85589_x1131_x1768321794}

[[network-operator]{lang="EN-US"}]{#struct_0_85589_x1131_x1755413002}

[[mdc-admin]{lang="EN-US"}]{#struct_0_85589_x1131_560943047}

[[mdc-operator]{lang="EN-US"}]{#struct_0_85589_x1131_450433904}

[[【参数】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x1715984330}

[*[policy-name]{lang="EN-US"}*]{#struct_0_85589_x1131_x736586920}[：显示指定的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略的信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。如果不指定本参数，则显示所有]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x1601075447}

[[\# ]{lang="EN-US"}]{#struct_0_85589_x1131_x2125925572}[显示名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略的信息。]{style="font-family:宋体"}

[[\<Sysname\> display ssl client-policy policy1]{lang="EN-US"}]{#struct_0_85589_x1131_1841594452}

[ SSL client policy: policy1]{lang="EN-US"}

[     SSL version: SSL 3.0]{lang="EN-US"}

[     PKI domain: client-domain]{lang="EN-US"}

[     Preferred ciphersuite:]{lang="EN-US"}

[         RSA_AES_128_CBC_SHA]{lang="EN-US"}

[     Server-verify: enabled]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display ssl client-policy]{lang="EN-US"}]{#struct_0_85589_x1131_1397846212}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1135811463}[[字段]{style="font-family:黑体"}]{#struct_0_85589_x1131_1041842394}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_85589_x1131_840849823}

[[SSL client policy]{lang="EN-US"}]{#struct_0_85589_x1131_526115302}

[[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_x1601272055}[客户端策略名]{style="font-family:宋体"}

[[SSL version]{lang="EN-US"}]{#struct_0_85589_x1131_x1093149578}

[[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_1154554187}[客户端策略使用的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[协议版本]{style="font-family:宋体"}

[[PKI domain]{lang="EN-US"}]{#struct_0_85589_x1131_517493258}

[[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_207490090}[客户端策略使用的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域]{style="font-family:宋体"}

[[Preferred ciphersuite]{lang="EN-US"}]{#struct_0_85589_x1131_1253254973}

[[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_x806464792}[客户端策略支持的加密套件]{style="font-family:宋体"}

[[Server-verify]{lang="EN-US"}]{#struct_0_85589_x1131_x1601206519}

[[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_x543772484}[客户端策略的服务器端验证模式，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[disabled]{lang="EN-US"}]{#struct_0_85589_x1131_x944822206}[：不要求对]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器进行基于数字证书的身份验证]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[enabled]{lang="EN-US"}]{#struct_0_85589_x1131_x1829820260}[：要求对]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器进行基于数字证书的身份验证]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#210365846 .myid}
[]{#_Toc279416460}[]{#_Toc404793327}[]{#struct_0_85589_x1131_x1499263576}[]{#_Toc279416457}[]{#_Toc257792946}[]{#_Toc168802552}

**SSL \-- SSL客户端策略配置命令 \-- pki-domain (SSL client policy view)**

------------------------------------------------------------------------

[**[pki-domain]{lang="EN-US"}**]{#struct_0_85589_x1131_x849709643}[命令用来配置]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略所使用的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域。]{style="font-family:宋体"}

[**[undo pki-domain]{lang="EN-US"}**]{#struct_0_85589_x1131_x21615904}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x1600878839}

[**[pki-domain ]{lang="EN-US"}***[domain-name]{lang="EN-US"}*]{#struct_0_85589_x1131_2014293625}

[**[undo pki-domain]{lang="EN-US"}**]{#struct_0_85589_x1131_2060163727}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x617241415}

[[没有指定]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_x1567072928}[客户端策略所使用的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_85589_x1131_1347144988}

[[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_1292923203}[客户端策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x67438155}

[[network-admin]{lang="EN-US"}]{#struct_0_85589_x1131_372870557}

[[mdc-admin]{lang="EN-US"}]{#struct_0_85589_x1131_x1600813303}

[[【参数】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x139372962}

[*[domain-name]{lang="EN-US"}*]{#struct_0_85589_x1131_x1500460178}[：]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域的域名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x559269717}

[[如果通过本命令指定了]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_1098261028}[客户端策略使用的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域，则引用该客户端策略的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端将通过该]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域获取客户端的数字证书。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_85589_x1131_1972823122}

[[\# ]{lang="EN-US"}]{#struct_0_85589_x1131_1242015900}[配置]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略所使用的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域为]{style="font-family:宋体"}[client-domain]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_85589_x1131_225502725}

[\[Sysname\] ssl client-policy policy1]{lang="EN-US"}

[\[Sysname-ssl-client-policy-policy1\] pki-domain client-domain]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x168105896}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ssl client-policy]{lang="EN-US"}**]{#struct_0_85589_x1131_x1601009911}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pki domain]{lang="EN-US"}**]{#struct_0_85589_x1131_x57977456}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/PKI]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#-1532955595 .myid}
[]{#_Toc404793328}[]{#struct_0_85589_x1131_831640847}[]{#_Toc279416458}[]{#_Toc257792947}[]{#_Toc168802553}[]{#_Toc140289406}[]{#_Toc138930571}

**SSL \-- SSL客户端策略配置命令 \-- prefer-cipher**

------------------------------------------------------------------------

[**[prefer-cipher]{lang="EN-US"}**]{#struct_0_85589_x1131_x1967865059}[命令用来配置]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略支持的加密套件。]{style="font-family:宋体"}

[**[undo prefer-cipher]{lang="EN-US"}**]{#struct_0_85589_x1131_1067796327}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_85589_x1131_942935823}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_85589_x1131_1818425062}[模式下：]{style="font-family:宋体"}

[**[prefer-cipher]{lang="EN-US"}**[ { **dhe_rsa_aes_128_cbc_sha** \| **dhe_rsa_aes_256_cbc_sha** \| **exp_rsa_des_cbc_sha** \| **exp_rsa_rc2_md5** \| **exp_rsa_rc4_md5** \| **rsa_3des_ede_cbc_sha** \| **rsa_aes_128_cbc_sha** \| **rsa_aes_256_cbc_sha** \| **rsa_des_cbc_sha** \| **rsa_rc4_128_md5** \| **rsa_rc4_128_sha** }]{lang="EN-US"}]{#struct_0_85589_x1131_x2047057296}

[**[undo prefer-cipher]{lang="EN-US"}**]{#struct_0_85589_x1131_x1210722667}

[[FIPS]{lang="EN-US"}]{#struct_0_85589_x1131_x1600944375}[模式下：]{style="font-family:宋体"}

[**[prefer-cipher]{lang="EN-US"}**[ { **dhe_rsa_aes_128_cbc_sha** \| **dhe_rsa_aes_256_cbc_sha** \| **rsa_aes_128_cbc_sha** \| **rsa_aes_256_cbc_sha** }]{lang="EN-US"}]{#struct_0_85589_x1131_921674423}

[**[undo prefer-cipher]{lang="EN-US"}**]{#struct_0_85589_x1131_x179702469}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x2010125354}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_85589_x1131_x1230807002}[模式下：]{style="font-family:宋体"}

[[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_x2072526033}[客户端策略支持的加密套件为]{style="font-family:宋体"}**[rsa_rc4_128_md5]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[FIPS]{lang="EN-US"}]{#struct_0_85589_x1131_x365535129}[模式下：]{style="font-family:宋体"}

[[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_x2014746582}[客户端策略支持的加密套件为]{style="font-family:宋体"}**[rsa_aes_128_cbc_sha]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_85589_x1131_647538616}

[[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_x1600616695}[客户端策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_85589_x1131_1349163705}

[[network-admin]{lang="EN-US"}]{#struct_0_85589_x1131_x427438308}

[[mdc-admin]{lang="EN-US"}]{#struct_0_85589_x1131_x1896503760}

[[【参数】]{style="font-family:黑体"}]{#struct_0_85589_x1131_1239424382}

[**[dhe_rsa_aes_128_cbc_sha]{lang="EN-US"}**]{#struct_0_85589_x1131_x1758838221}[：密钥交换算法采用]{style="font-family:宋体"}[DHE RSA]{lang="EN-US"}[、数据加密算法采用]{style="font-family:宋体"}[128]{lang="EN-US"}[位的]{style="font-family:宋体"}[AES]{lang="EN-US"}[、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[算法采用]{style="font-family:宋体"}[SHA]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[dhe_rsa_aes_256_cbc_sha]{lang="EN-US"}**]{#struct_0_85589_x1131_x1254036537}[：密钥交换算法采用]{style="font-family:宋体"}[DHE RSA]{lang="EN-US"}[、数据加密算法采用]{style="font-family:宋体"}[256]{lang="EN-US"}[位的]{style="font-family:宋体"}[AES]{lang="EN-US"}[、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[算法采用]{style="font-family:宋体"}[SHA]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[exp_rsa_des_cbc_sha]{lang="EN-US"}**]{#struct_0_85589_x1131_x2020944589}[：满足出口限制的算法套件。密钥交换算法采用]{style="font-family:宋体"}[RSA]{lang="EN-US"}[、数据加密算法采用]{style="font-family:宋体"}[DES_CBC]{lang="EN-US"}[、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[算法采用]{style="font-family:宋体"}[SHA]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[exp_rsa_rc2_md5]{lang="EN-US"}**]{#struct_0_85589_x1131_1094820899}[：满足出口限制的算法套件。密钥交换算法采用]{style="font-family:宋体"}[RSA]{lang="EN-US"}[、数据加密算法采用]{style="font-family:宋体"}[RC2]{lang="EN-US"}[、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[算法采用]{style="font-family:宋体"}[MD5]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[exp_rsa_rc4_md5]{lang="EN-US"}**]{#struct_0_85589_x1131_x1600551159}[：满足出口限制的算法套件。密钥交换算法采用]{style="font-family:宋体"}[RSA]{lang="EN-US"}[、数据加密算法采用]{style="font-family:宋体"}[RC4]{lang="EN-US"}[、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[算法采用]{style="font-family:宋体"}[MD5]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[rsa_3des_ede_cbc_sha]{lang="EN-US"}**]{#struct_0_85589_x1131_1093639818}[：密钥交换算法采用]{style="font-family:宋体"}[RSA]{lang="EN-US"}[、数据加密算法采用]{style="font-family:宋体"}[3DES_EDE_CBC]{lang="EN-US"}[、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[算法采用]{style="font-family:宋体"}[SHA]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[rsa_aes_128_cbc_sha]{lang="EN-US"}**]{#struct_0_85589_x1131_x256819465}[：密钥交换算法采用]{style="font-family:宋体"}[RSA]{lang="EN-US"}[、数据加密算法采用]{style="font-family:宋体"}[128]{lang="EN-US"}[位]{style="font-family:宋体"}[AES_CBC]{lang="EN-US"}[、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[算法采用]{style="font-family:宋体"}[SHA]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[rsa_aes_256_cbc_sha]{lang="EN-US"}**]{#struct_0_85589_x1131_x755227832}[：密钥交换算法采用]{style="font-family:宋体"}[RSA]{lang="EN-US"}[、数据加密算法采用]{style="font-family:宋体"}[256]{lang="EN-US"}[位]{style="font-family:宋体"}[AES_CBC]{lang="EN-US"}[、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[算法采用]{style="font-family:宋体"}[SHA]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[rsa_des_cbc_sha]{lang="EN-US"}**]{#struct_0_85589_x1131_1714274728}[：密钥交换算法采用]{style="font-family:宋体"}[RSA]{lang="EN-US"}[、数据加密算法采用]{style="font-family:宋体"}[DES_CBC]{lang="EN-US"}[、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[算法采用]{style="font-family:宋体"}[SHA]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[rsa_rc4_128_md5]{lang="EN-US"}**]{#struct_0_85589_x1131_1389942736}[：密钥交换算法采用]{style="font-family:宋体"}[RSA]{lang="EN-US"}[、数据加密算法采用]{style="font-family:宋体"}[128]{lang="EN-US"}[位的]{style="font-family:宋体"}[RC4]{lang="EN-US"}[、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[算法采用]{style="font-family:宋体"}[MD5]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[rsa_rc4_128_sha]{lang="EN-US"}**]{#struct_0_85589_x1131_x33583852}[：密钥交换算法采用]{style="font-family:宋体"}[RSA]{lang="EN-US"}[、数据加密算法采用]{style="font-family:宋体"}[128]{lang="EN-US"}[位的]{style="font-family:宋体"}[RC4]{lang="EN-US"}[、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[算法采用]{style="font-family:宋体"}[SHA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_85589_x1131_215844849}

[[为了提高安全性，]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_965262821}[协议采用了如下算法：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[数据加密算法：用来对传输的数据进行加密，以保证数据传输的私密性。常用的数据加密算法通常为对称密钥算法，如]{style="font-family:宋体"}]{#struct_0_85589_x1131_773187407}[DES_CBC]{lang="EN-US"}[、]{style="font-family:宋体"}[3DES_EDE_CBC]{lang="EN-US"}[、]{style="font-family:宋体"}[AES_CBC]{lang="EN-US"}[、]{style="font-family:宋体"}[RC4]{lang="EN-US"}[等。使用对称密钥算法时，要求]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端和]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端具有相同的密钥。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MAC]{lang="EN-US"}]{#struct_0_85589_x1131_x1601140982}[（]{lang="EN-US" style="font-family:
宋体"}[Message Authentication Code]{lang="EN-US"}[，消息验证码）算法：用来计算数据的]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[值，以防止发送的数据被篡改。常用的]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[算法有]{lang="EN-US" style="font-family:宋体"}[MD5]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[SHA]{lang="EN-US"}[等。]{lang="EN-US" style="font-family:宋体"}[使用]{style="font-family:宋体"}[MAC]{lang="EN-US"}[算法时，要求]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端和]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端具有相同的密钥。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[密钥交换算法：用来实现密钥交换，以保证对称密钥算法、]{style="font-family:宋体"}]{#struct_0_85589_x1131_x720671}[MAC]{lang="EN-US"}[算法中使用的密钥在]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端和]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端之间安全地传递。常用的密钥交换算法通常为非对称密钥算法，如]{style="font-family:宋体"}[RSA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[通过本命令可以配置]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_892704568}[客户端策略支持的算法组合。例如]{style="font-family:宋体"}[，]{style="font-family:宋体"}**[rsa_des_cbc_sha]{lang="FR"}**[表示]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端支持的密钥交换算法为]{style="font-family:宋体"}[RSA]{lang="EN-US"}[、数据加密算法为]{style="font-family:宋体"}[DES_CBC]{lang="EN-US"}[、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[算法为]{style="font-family:宋体"}[SHA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_296021920}[客户端将本端支持的加密套件发送给]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器，]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器将自己支持的加密套件与]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端支持的加密套件比较。如果]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器支持的加密套件中存在]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端支持的加密套件，则加密套件协商成功；否则，加密套件协商失败。]{style="font-family:宋体"}

[[需要注意的是，如果多次执行本命令，则新的配置覆盖原有配置。]{style="font-family:宋体"}]{#struct_0_85589_x1131_884545228}

[[【举例】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x78875715}

[[\# ]{lang="EN-US"}]{#struct_0_85589_x1131_398631648}[配置]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略支持的加密套件为：密钥交换算法采用]{style="font-family:宋体"}[RSA]{lang="EN-US"}[、数据加密算法采用]{style="font-family:宋体"}[128]{lang="EN-US"}[位]{style="font-family:宋体"}[AES_CBC]{lang="EN-US"}[、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[算法采用]{style="font-family:宋体"}[SHA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_85589_x1131_731273165}

[\[Sysname\] ssl client-policy policy1]{lang="EN-US"}

[\[Sysname-ssl-client-policy-policy1\] prefer-cipher rsa_aes_128_cbc_sha]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x1601075446}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ciphersuite]{lang="EN-US"}**]{#struct_0_85589_x1131_x559841631}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ssl client-policy]{lang="EN-US"}**]{#struct_0_85589_x1131_x1218478476}
:::

::: {#-942620910 .myid}
[]{#_Toc404793329}[]{#struct_0_85589_x1131_x440594196}[]{#_Toc279416459}[]{#_Toc257792948}

**SSL \-- SSL客户端策略配置命令 \-- server-verify enable**

------------------------------------------------------------------------

[**[server-verify enable]{lang="EN-US"}**]{#struct_0_85589_x1131_x1401471284}[命令用来配置客户端需要对服务器端进行基于数字证书的身份验证。]{style="font-family:宋体"}

[**[undo server-verify enable]{lang="EN-US"}**]{#struct_0_85589_x1131_x746526745}[命令用来配置客户端不要求对服务器端进行基于数字证书的身份验证，默认]{style="font-family:
宋体"}[SSL]{lang="EN-US"}[服务器身份合法。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x951495280}

[**[server-verify enable]{lang="EN-US"}**]{#struct_0_85589_x1131_905685898}

[**[undo server-verify enable]{lang="EN-US"}**]{#struct_0_85589_x1131_x2141853583}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_85589_x1131_1238129140}

[[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_x1601272054}[客户端需要对]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端进行基于数字证书的身份验证。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_85589_x1131_472934363}

[[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_x77759347}[客户端策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x1457883393}

[[network-admin]{lang="EN-US"}]{#struct_0_85589_x1131_1756345885}

[[mdc-admin]{lang="EN-US"}]{#struct_0_85589_x1131_x1937973724}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_85589_x1131_2070557895}

[[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_x868651097}[通过数字证书实现对对端的身份进行验证。数字证书的详细介绍，请参见"安全配置指导"中的"]{style="font-family:宋体"}[PKI]{lang="EN-US"}["。]{style="font-family:宋体"}

[[如果执行了]{style="font-family:宋体"}**[server-verify enable]{lang="EN-US"}**]{#struct_0_85589_x1131_x1063479768}[命令，则]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端需要将自己的数字证书提供给客户端，以便客户端对服务器端进行基于数字证书的身份验证。只有身份验证通过后，]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端才会访问该]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x1601206518}

[[\# ]{lang="EN-US"}]{#struct_0_85589_x1131_x2109856425}[配置]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端需要对]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端进行基于数字证书的身份验证。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_85589_x1131_x1718598639}

[\[Sysname\] ssl client-policy policy1]{lang="EN-US"}

[\[Sysname-ssl-client-policy-policy1\] server-verify enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_85589_x1131_425976572}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ssl client-policy]{lang="EN-US"}**]{#struct_0_85589_x1131_x1251423894}
:::

::: {#1659289076 .myid}
[]{#_Toc404793330}[]{#struct_0_85589_x1131_x176487493}[]{#_Toc297019374}

**SSL \-- SSL客户端策略配置命令 \-- ssl client-policy**

------------------------------------------------------------------------

[**[ssl client-policy]{lang="EN-US"}**]{#struct_0_85589_x1131_2011908493}[命令用来创建]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略，并进入]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略视图。]{style="font-family:宋体"}

[**[undo ssl client-policy]{lang="EN-US"}**]{#struct_0_85589_x1131_1133878314}[命令用来删除已创建的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x1057507094}

[**[ssl client-policy]{lang="EN-US"}**[ *policy-name*]{lang="EN-US"}]{#struct_0_85589_x1131_x1600878838}

[**[undo ssl client-policy]{lang="EN-US"}**[ *policy-name*]{lang="EN-US"}]{#struct_0_85589_x1131_x714589730}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_85589_x1131_1021706939}

[[设备上不存在任何]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_x780187060}[客户端策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_85589_x1131_984785461}

[[系统视图]{style="font-family:宋体"}]{#struct_0_85589_x1131_1791725561}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x52120042}

[[network-admin]{lang="EN-US"}]{#struct_0_85589_x1131_x1306853197}

[[mdc-admin]{lang="EN-US"}]{#struct_0_85589_x1131_1080043929}

[[【参数】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x1600813302}

[*[policy-name]{lang="EN-US"}*]{#struct_0_85589_x1131_1426710979}[：]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_85589_x1131_496907142}

[[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_x1255427230}[客户端策略视图下可以配置]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端启动时使用的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[参数，如使用的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域、支持的加密套件等。只有与应用层协议，如]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[（]{style="font-family:宋体"}[Dynamic Domain Name System]{lang="EN-US"}[，动态域名系统），关联后，]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_85589_x1131_1256665529}

[[\# ]{lang="EN-US"}]{#struct_0_85589_x1131_x1100554810}[创建]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略]{style="font-family:宋体"}[policy1]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_85589_x1131_x1648040717}

[\[Sysname\] ssl client-policy policy1]{lang="EN-US"}

[\[Sysname-ssl-client-policy-policy1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x259671323}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ssl client-policy]{lang="EN-US"}**]{#struct_0_85589_x1131_1840152110}
:::

::: {#1902401671 .myid}
[]{#_Toc404793331}[]{#struct_0_85589_x1131_x1601009910}[]{#_Toc297019376}

**SSL \-- SSL客户端策略配置命令 \-- version**

------------------------------------------------------------------------

[**[version]{lang="EN-US"}**]{#struct_0_85589_x1131_x1624061397}[命令用来配置]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略使用的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[协议版本。]{style="font-family:宋体"}

[**[undo version]{lang="EN-US"}**]{#struct_0_85589_x1131_1738406847}[命令恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_85589_x1131_1606101852}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_85589_x1131_1029347432}[模式下：]{style="font-family:宋体"}

[**[version]{lang="EN-US"}**[ { **ssl3.0** \| **tls1.0** }]{lang="EN-US"}]{#struct_0_85589_x1131_x2144682133}

[**[undo version]{lang="EN-US"}**]{#struct_0_85589_x1131_960787050}

[[FIPS]{lang="EN-US"}]{#struct_0_85589_x1131_1817330297}[模式下：]{style="font-family:宋体"}

[**[version tls1.0]{lang="EN-US"}**]{#struct_0_85589_x1131_x1833761471}

[**[undo version]{lang="EN-US"}**]{#struct_0_85589_x1131_x1600944374}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x644409518}

[[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_891235009}[客户端策略使用的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[协议版本为]{style="font-family:宋体"}[TLS 1.0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_85589_x1131_1304305430}

[[SSL]{lang="EN-US"}]{#struct_0_85589_x1131_1161784087}[客户端策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_85589_x1131_1490298319}

[[network-admin]{lang="EN-US"}]{#struct_0_85589_x1131_313635862}

[[mdc-admin]{lang="EN-US"}]{#struct_0_85589_x1131_x1735937778}

[[【参数】]{style="font-family:黑体"}]{#struct_0_85589_x1131_64183575}

[**[ssl3.0]{lang="EN-US"}**]{#struct_0_85589_x1131_1757047067}[：版本为]{style="font-family:宋体"}[SSL 3.0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[tls1.0]{lang="EN-US"}**]{#struct_0_85589_x1131_x1600616694}[：版本为]{style="font-family:宋体"}[TLS 1.0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x1379719650}

[[如果多次执行本命令，则新的配置覆盖原有配置。]{style="font-family:宋体"}]{#struct_0_85589_x1131_292833699}

[[【举例】]{style="font-family:黑体"}]{#struct_0_85589_x1131_x725140083}

[[\# ]{lang="EN-US"}]{#struct_0_85589_x1131_x154664756}[配置]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略使用的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[协议版本为]{style="font-family:宋体"}[TLS 1.0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_85589_x1131_911089762}

[\[Sysname\] ssl client-policy policy1]{lang="EN-US"}

[\[Sysname-ssl-client-policy-policy1\] version tls1.0]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_85589_x1131_2108004434}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ssl client-policy]{lang="EN-US"}**]{#struct_0_85589_x1131_x2087589416}
:::
