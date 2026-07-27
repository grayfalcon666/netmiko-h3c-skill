<!-- CMD-INDEX
  ah authentication-algorithm         | IPsec安全提议视图      | L89
  description                         | IPsec安全策略视图/IPsec安全策略模板视图/IPsec安全框架视图 | L147
  display ipsec { ipv6-policy \| policy } | 任意视图             | L193
  display ipsec { ipv6-policy-template \| policy-template } | 任意视图             | L627
  display ipsec profile               | 任意视图             | L797
  display ipsec sa                    | 任意视图             | L953
  display ipsec statistics            | 任意视图             | L1369
  display ipsec transform-set         | 任意视图             | L1549
  display ipsec tunnel                | 任意视图             | L1655
  encapsulation-mode                  | IPsec安全提议视图      | L1899
  esp authentication-algorithm        | IPsec安全提议视图      | L1957
  esp encryption-algorithm            |                  | L2019
  ike-profile                         | IPsec安全策略视图/IPsec安全策略模板视图 | L2095
  ipsec anti-replay check             | 系统视图             | L2147
  ipsec anti-replay window            | 系统视图             | L2195
  ipsec decrypt-check enable          | 系统视图             | L2245
  ipsec logging packet enable         | 系统视图             | L2285
  ipsec df-bit                        | 接口视图             | L2325
  ipsec global-df-bit                 | 系统视图             | L2385
  ipsec apply                         | 接口视图             | L2441
  ipsec { ipv6-policy \| policy }     | 系统视图             | L2499
  ipsec { ipv6-policy \| policy } isakmp template | 系统视图             | L2577
  ipsec { ipv6-policy \| policy } local-address | 系统视图             | L2637
  ipsec { ipv6-policy-template \| policy-template } | 系统视图             | L2701
  ipsec profile                       | 系统视图             | L2767
  ipsec redundancy enable             | 系统视图             | L2833
  ipsec sa global-duration            | 系统视图             | L2881
  ipsec sa idle-time                  | 系统视图             | L2941
  ipsec transform-set                 | 系统视图             | L2993
  local-address                       | IPsec安全策略视图/IPsec安全策略模板视图 | L3043
  pfs                                 | IPsec安全提议视图      | L3097
  protocol                            | IPsec安全提议视图      | L3163
  qos pre-classify                    | IPsec安全策略视图/IPsec安全策略模板视图 | L3213
  redundancy replay-interval          | IPsec安全策略视图/IPsec安全策略模板视图 | L3255
  remote-address                      | IPsec安全策略视图/IPsec安全策略模板视图 | L3317
  reset ipsec sa                      | 用户视图             | L3403
  reset ipsec statistics              | 用户视图             | L3493
  reverse-route dynamic               | IPsec安全策略视图/IPsec安全策略模板视图 | L3527
  reverse-route preference            | IPsec安全策略视图/IPsec安全策略模板视图 | L3599
  reverse-route tag                   | IPsec安全策略视图/IPsec安全策略模板视图 | L3651
  sa duration                         | IPsec安全策略视图/IPsec安全策略模板视图/IPsec安全框架视图 | L3703
  sa hex-key authentication           | IPsec安全策略视图/IPsec安全框架视图 | L3767
  sa hex-key encryption               | IPsec安全策略视图/IPsec安全框架视图 | L3843
  sa idle-time                        | IPsec安全策略视图/IPsec安全策略模板视图/IPsec安全框架视图 | L3917
  sa spi                              | IPsec安全策略视图/IPsec安全框架视图 | L3971
  sa string-key                       | IPsec安全策略视图/IPsec安全框架视图 | L4041
  security acl                        | IPsec安全策略视图/IPsec安全策略模板视图 | L4133
  snmp-agent trap enable ipsec        | 系统视图             | L4225
  transform-set                       | IPsec安全策略视图/IPsec安全策略模板视图/IPsec安全框架视图 | L4299
  tunnel protection ipsec             | Tunnel接口视图       | L4361
  authentication-algorithm            | IKE提议视图          | L4417
  authentication-method               | IKE提议视图          | L4473
  certificate domain                  | IKE profile视图    | L4539
  dh                                  |                  | L4601
  display ike proposal                | 任意视图             | L4673
  display ike sa                      | 任意视图             | L4783
  dpd                                 | IKE profile视图    | L5091
  encryption-algorithm                |                  | L5151
  exchange-mode                       | IKE profile视图    | L5223
  ike dpd                             | 系统视图             | L5283
  ike identity                        | 系统视图             | L5347
  ike invalid-spi-recovery enable     | 系统视图             | L5407
  ike keepalive interval              | 系统视图             | L5451
  ike keepalive timeout               | 系统视图             | L5505
  ike keychain                        | 系统视图             | L5557
  ike limit                           | 系统视图             | L5611
  ike nat-keepalive                   | 系统视图             | L5669
  ike profile                         | 系统视图             | L5719
  ike proposal                        | 系统视图             | L5761
  ike signature-identity from-certificate | 系统视图             | L5823
  inside-vpn                          | IKE profile视图    | L5871
  keychain                            | IKE profile视图    | L5917
  local-identity                      | IKE profile视图    | L5967
  match local address (IKE keychain view) | IKE keychain视图   | L6033
  match local address (IKE profile view) | IKE profile视图    | L6089
  match remote                        | IKE profile视图    | L6145
  pre-shared-key                      | IKE keychain视图   | L6221
  priority (IKE keychain view)        | IKE keychain视图   | L6303
  priority (IKE profile view)         | IKE-Profile视图    | L6349
  proposal                            | IKE profile视图    | L6395
  reset ike sa                        | 用户视图             | L6445
  reset ike statistics                | 用户视图             | L6513
  sa duration                         | IKE提议视图          | L6543
  snmp-agent trap enable ike          | 系统视图             | L6595
  tunnel protection                   | Tunnel接口视图       | L6683
-->

**IPsec \-- IPsec配置命令 \-- ah authentication-algorithm**

------------------------------------------------------------------------

**[ah authentication-algorithm**]命令用来配置AH协议采用的认证算法。

**[undo ah authentication-algorithm**]命令用来删除所有指定的AH协议采用的认证算法。

【命令】

非FIPS模式下：

**[ah authentication-algorithm **[{ **md5** \| **sha1** } \*]]

**[undo ah authentication-algorithm**]

FIPS模式下：

**[ah authentication-algorithm sha1**]

**[undo ah authentication-algorithm**]

【缺省情况】

AH协议没有采用任何认证算法。

【视图】

IPsec安全提议视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[md5**]：采用HMAC-MD5认证算法，密钥长度128比特。

**[sha1**]：采用HMAC-SHA1认证算法，密钥长度160比特。

【使用指导】

非FIPS模式下，每个IPsec安全提议中均可以配置多个AH认证算法，其优先级为配置顺序。

对于手工方式以及IKEv1（第1版本的IKE协议）协商方式的IPsec安全策略，IPsec安全提议中配置顺序首位的AH认证算法生效。为保证成功建立IPsec隧道，隧道两端指定的IPsec安全提议中配置的首个AH认证算法需要一致。

【举例】

\# 配置IPsec安全提议采用的AH认证算法为HMAC-SHA1算法，密钥长度为160比特。

\<Sysname\> system-view

Sysname ipsec transform-set tran1

Sysname-ipsec-transform-set-tran1 ah authentication-algorithm sha1

**IPsec \-- IPsec配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来配置IPsec安全策略/IPsec安全策略模板/IPsec安全框架的描述信息。

**[undo description**]命令用来恢复缺省情况。

【命令】

**[description ***text*]

**[undo description**]

【缺省情况】

无描述信息。

【视图】

IPsec安全策略视图/IPsec安全策略模板视图/IPsec安全框架视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：IPsec安全策略/IPsec安全策略模板/IPsec安全框架的描述信息，为1～80个字符的字符串，区分大小写。

【使用指导】

当系统中存在多个IPsec安全策略/IPsec安全策略模板/IPsec安全框架时，可通过配置相应的描述信息来有效区分不同的安全策略。

【举例】

\# 配置序号为1的IPsec安全策略policy1的描述信息为CenterToA。

\<Sysname\> system-view

Sysname ipsec policy policy1 1 isakmp

Sysname-ipsec-policy-isakmp-policy1-1 description CenterToA

**IPsec \-- IPsec配置命令 \-- display ipsec { ipv6-policy \| policy }**

------------------------------------------------------------------------

**[display ipsec **[{ **ipv6-policy** \| **policy** }]]命令用来显示IPsec安全策略的信息。

【命令】

**[display**[ **ipsec** { **ipv6-policy** \| **policy** } [ *policy-name* [ *seq-number* ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[ipv6-policy**]：显示IPv6 IPsec安全策略的信息。

**[policy**]：显示IPv4 IPsec安全策略的信息。

*[policy-name*]：IPsec安全策略的名称，为1～63个字符的字符串，不区分大小写。

*[seq-number*]：IPsec安全策略表项的顺序号，取值范围为1～65535。

【使用指导】

·如果不指定任何参数，则显示所有IPsec安全策略的信息。

·如果指定了*policy-name*和*seq-number*，则显示指定的IPsec安全策略表项的信息；如果指定了*policy-name*而没有指定*seq-number*，则显示所有名称相同的IPsec安全策略表项的信息。

【举例】

\# 显示所有IPv4 IPsec安全策略的信息。

\<Sysname\> display ipsec policy

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

IPsec Policy: mypolicy

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Sequence number: 1

  Mode: manual

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  The policy configuration is incomplete:

           ACL not specified

           Incomplete transform-set configuration

  Description: This is my first IPv4 manual policy

  Security data flow:

  Remote address: 2.5.2.1

  Transform set: transform

  Inbound AH setting:

    AH SPI: 1200 (0x000004b0)

    AH string-key: \*\*\*\*\*\*

    AH authentication hex key:

  Inbound ESP setting:

    ESP SPI: 1400 (0x00000578)

    ESP string-key:

    ESP encryption hex key:

    ESP authentication hex key:

  Outbound AH setting:

    AH SPI: 1300 (0x00000514)

    AH string-key: \*\*\*\*\*\*

    AH authentication hex key:

  Outbound ESP setting:

    ESP SPI: 1500 (0x000005dc)

    ESP string-key: \*\*\*\*\*\*

    ESP encryption hex key:

    ESP authentication hex key:

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Sequence number: 2

  Mode: isakmp

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  The policy configuration is incomplete:

           Remote-address not set

           ACL not specified

           Transform-set not set

  Description: This is my first IPv4 Isakmp policy

  Security data flow:

  Selector mode: standard

  Local address:

  Remote address:

  Transform set:

  IKE profile:

  SA duration(time based):

  SA duration(traffic based):

  SA idle time:

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

IPsec Policy: mycompletepolicy

Interface: LoopBack2

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Sequence number: 1

  Mode: manual

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Description: This is my complete policy

  Security data flow: 3100

  Remote address: 2.2.2.2

  Transform set: completetransform

  Inbound AH setting:

    AH SPI: 5000 (0x00001388)

    AH string-key: \*\*\*\*\*\*

    AH authentication hex key:

  Inbound ESP setting:

    ESP SPI: 7000 (0x00001b58)

    ESP string-key: \*\*\*\*\*\*

    ESP encryption hex key:

    ESP authentication hex key:

  Outbound AH setting:

    AH SPI: 6000 (0x00001770)

    AH string-key: \*\*\*\*\*\*

    AH authentication hex key:

  Outbound ESP setting:

    ESP SPI: 8000 (0x00001f40)

    ESP string-key: \*\*\*\*\*\*

    ESP encryption hex key:

    ESP authentication hex key:

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Sequence number: 2

  Mode: isakmp

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Description: This is my complete policy

  Security data flow: 3200

  Selector mode: standard

  Local address:

  Remote address: 5.3.6.9

  Transform set:  completetransform

  IKE profile:

  SA duration(time based):

  SA duration(traffic based):

  SA idle time:

\# 显示所有IPv6 IPsec安全策略的详细信息。

\<Sysname\> display ipsec ipv6-policy

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

IPsec Policy: mypolicy

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Sequence number: 1

  Mode: manual

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Description: This is my first IPv6 policy

  Security data flow: 3600

  Remote address: 1000::2

  Transform set: mytransform

  Inbound AH setting:

    AH SPI: 1235 (0x000004d3)

    AH string-key: \*\*\*\*\*\*

    AH authentication hex key:

  Inbound ESP setting:

    ESP SPI: 1236 (0x000004d4)

    ESP string-key: \*\*\*\*\*\*

    ESP encryption hex key:

    ESP authentication hex key:

  Outbound AH setting:

    AH SPI: 1237 (0x000004d5)

    AH string-key: \*\*\*\*\*\*

    AH authentication hex key:

  Outbound ESP setting:

    ESP SPI: 1238 (0x000004d6)

    ESP string-key: \*\*\*\*\*\*

    ESP encryption hex key:

    ESP authentication hex key:

表1-1  display ipsec { ipv6-policy \| policy }命令显示信息描述表

字段

描述

IPsec Policy

IPsec安全策略的名称

Interface

应用了IPsec安全策略的接口名称

Sequence number

IPsec安全策略表项的顺序号

Mode

IPsec安全策略采用的协商方式

·mannul：手工方式

·isakmp：IKE协商方式

·template：策略模板方式

The policy configuration is incomplete

IPsec安全策略配置不完整，可能的原因包括：

·ACL未配置

·IPsec安全提议未配置

·ACL中没有**permit**规则

·IPsec安全提议配置不完整

·IPsec隧道对端IP地址未指定

·IPsec SA的SPI和密钥与IPsec安全策略的SPI和密钥不匹配

Description

IPsec安全策略的描述信息

Security data flow

IPsec安全策略引用的ACL

Selector mode

IPsec安全策略的数据流保护方式

·standard：标准方式

·aggregation：聚合方式

·per-host：主机方式

Local address

IPsec隧道的本端IP地址（仅IKE协商方式的IPsec安全策略下存在）

Remote address

IPsec隧道的对端IP地址或主机名

Transform set

IPsec安全策略引用的IPsec安全提议的名字

IKE profile

IPsec安全策略引用的IKE Profile的名称

SA duration(time based)

基于时间的IPsec SA生命周期，单位为秒

SA duration(traffic based)

基于流量的IPsec SA生命周期，单位为千字节

SA idle time

IPsec SA的空闲超时时间，单位为秒

Inbound AH setting

入方向采用的AH协议的相关设置

outbound AH setting

出方向采用的AH协议的相关设置

AH SPI

AH协议的SPI

AH string-key

AH协议的字符类型的密钥（若配置，则显示为\*\*\*\*\*\*）

AH authentication hex key

AH协议的十六进制密钥（若配置，则显示为\*\*\*\*\*\*）

Inbound ESP setting

入方向采用的ESP协议的相关设置

outbound ESP setting

出方向采用的ESP协议的相关设置

ESP SPI

ESP协议的SPI

ESP string-key

ESP协议的字符类型的密钥（若配置，则显示为\*\*\*\*\*\*）

ESP encryption hex key

ESP协议的十六进制加密密钥（若配置，则显示为\*\*\*\*\*\*）

ESP authentication hex key

ESP协议的十六进制认证密钥（若配置，则显示为\*\*\*\*\*\*）

【相关命令】

[·**ipsec**[ { **ipv6-policy** \| **policy** }]]

**IPsec \-- IPsec配置命令 \-- display ipsec { ipv6-policy-template \| policy-template }**

------------------------------------------------------------------------

**[display ipsec**[ { **ipv6-policy-template** \| **policy-template** }]]命令用来显示IPsec安全策略模板的信息。

【命令】

**[display**[ **ipsec** { **ipv6-policy-template** \| **policy-template** } [ *template-name* [ *seq-number* ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[ipv6-policy-template**]：显示IPv6 IPsec安全策略模板的信息。

**[policy-template**]：显示IPv4 IPsec安全策略模板的信息。

*[template-name*]：指定IPsec安全策略模板的名称，为1～63个字符的字符串，不区分大小写。

*[seq-number*]：指定IPsec安全策略模板表项的顺序号，取值范围为1～65535。

【使用指导】

·如果不指定任何参数，则显示所有IPsec安全策略模板的信息。

·如果指定了*template-name*和*seq-number*，则显示指定的IPsec安全策略模板表项的信息；如果指定了*template-name*而没有指定*seq-number*，则显示所有名称相同的IPsec安全策略模板表项的信息。

【举例】

\# 显示所有IPv4 IPsec安全策略模板的信息。

\<Sysname\> display ipsec policy-template

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

IPsec Policy Template: template

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Sequence number: 1

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

    Description: This is policy template

    Security data flow :

    Selector mode: standard

    Local address:

    IKE profile:  None

    Remote address: 162.105.10.2

    Transform set:  testprop

    IPsec SA local duration(time based): 3600 seconds

    IPsec SA local duration(traffic based): 1843200 kilobytes

\# 显示所有IPv6 IPsec安全策略模板的详细信息。

\<Sysname\> display ipsec ipv6-policy-template

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

IPsec Policy Template: template6

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Sequence number: 1

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

    Description: This is policy template

    Security data flow :

    Selector mode: standard

    Local address:

    IKE profile:  None

    Remote address: 200::1/64

    Transform set: testprop

    IPsec SA local duration(time based): 3600 seconds

    IPsec SA local duration(traffic based): 1843200 kilobytes

表1-2  display ipsec { ipv6-policy-template \| policy-template }命令显示信息描述表

字段

描述

IPsec Policy Template

IPsec安全策略模板名称

Sequence number

IPsec安全策略模板表项的序号

Description

IPsec安全策略模板的描述信息

Security data flow

IPsec安全策略模板引用的ACL

Selector mode

IPsec安全策略模板的数据流保护方式

·standard：标准方式

·aggregation：聚合方式

·per-host：主机方式

Local address

IPsec隧道的本端IP地址

IKE profile

IPsec安全策略模板引用的IKE profile名称

Remote address

IPsec隧道的对端IP地址

Transform set

IPsec安全策略模板引用的安全提议的名字

IPsec SA local duration(time based)

基于时间的IPsec SA生命周期，单位为秒

IPsec SA local duration(traffic based)

基于流量的IPsec SA生命周期，单位为千字节

【相关命令】

[·**ipsec **[{ **ipv6-policy** \| **policy** } **isakmp template**]]

**IPsec \-- IPsec配置命令 \-- display ipsec profile**

------------------------------------------------------------------------

**[display ipsec profile**]命令用来显示IPsec安全框架的信息。

【命令】

**[display ipsec profile** [ *profile-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[profile-name*]：指定IPsec安全框架的名称，为1～63个字符的字符串，不区分大小写。

【使用指导】

如果没有指定任何参数，则显示所有IPsec安全框架的配置信息。

【举例】

\# 显示所有IPsec安全框架的配置信息。

\<Sysname\> display ipsec profile

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

IPsec profile: profile

Mode: manual

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Description:

  Transform set: prop1

  Inbound AH setting:

    AH SPI: 12345 (0x00003039)

    AH string-key:

    AH authentication hex key: \*\*\*\*\*\*

  Inbound ESP setting:

    ESP SPI: 23456 (0x00005ba0)

    ESP string-key:

    ESP encryption hex-key: \*\*\*\*\*\*

    ESP authentication hex-key: \*\*\*\*\*\*

  Outbound AH setting:

    AH SPI: 12345 (0x00003039)

    AH string-key:

    AH authentication hex key: \*\*\*\*\*\*

  Outbound ESP setting:

    ESP SPI: 23456 (0x00005ba0)

    ESP string-key:

    ESP encryption hex key: \*\*\*\*\*\*

    ESP authentication hex key: \*\*\*\*\*\*

表1-3 display ipsec profile命令显示信息描述表

字段

描述

IPsec profile

IPsec安全框架的名称

Mode

IPsec安全框架采用的协商方式，目前仅支持手工方式（mannul）

Description

IPsec安全框架的描述信息

Transform set

IPsec安全策略引用的IPsec安全提议的名字

Inbound AH setting

入方向采用的AH协议的相关设置

outbound AH setting

出方向采用的AH协议的相关设置

AH SPI

AH协议的SPI

AH string-key

AH协议的字符类型的密钥

AH authentication hex key

AH协议的十六进制密钥

Inbound ESP setting

入方向采用的ESP协议的相关设置

outbound ESP setting

出方向采用的ESP协议的相关设置

ESP SPI

ESP协议的SPI

ESP string-key

ESP协议的字符类型的密钥

ESP encryption hex key

ESP协议的十六进制加密密钥

ESP authentication hex key

ESP协议的十六进制认证密钥

【相关命令】

·**ipsec p****rofile**

**IPsec \-- IPsec配置命令 \-- display ipsec sa**

------------------------------------------------------------------------

**[display** **ipsec** **sa**]命令用来显示IPsec SA的相关信息。

【命令】

**[display**[ **ipsec** **sa** [ **brief** \| **count** \| **interface** *interface-type interface-number* \| { **ipv6-policy** \| **policy** } *policy-name* [ *seq-number* ] \| **profile** *profile-name* \| **remote**  **ipv6**  *ip-address* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[brief**]：显示所有的IPsec SA的简要信息。

**[count**]：显示IPsec SA的个数。

**[interface ***interface-type interface-number*]：显示指定接口下的IPsec SA的详细信息。*interface-type interface-number*表示接口类型和接口编号。

**[ipv6-policy**]：显示由指定IPv6 IPsec安全策略创建的IPsec SA的详细信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[policy**]：显示由指定IPv4 IPsec安全策略创建的IPsec SA的详细信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[policy-name*]：IPsec安全策略的名字，为1～63个字符的字符串，不区分大小写。

*[seq-number*]：IPsec安全策略的顺序号，取值范围为1～65535。

**[profile**]：显示由指定IPsec安全框架创建的IPsec SA的详细信息。

*[profile-name*]：IPsec安全框架的名字，为1～63个字符的字符串，不区分大小写。

**[remote*** ip-address*]：显示指定对端IP地址的IPsec SA的详细信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ipv6**]：显示指定IPv6对端地址的IPsec SA的详细信息。若不指定本参数，则表示显示指定IPv4对端地址的IPsec SA的详细信息。

【使用指导】

如果不指定任何参数，则显示所有IPsec SA的详细信息。

【举例】

\# 显示IPsec SA的简要信息。

\<Sysname\> display ipsec sa brief

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Interface/Global   Dst Address      SPI         Protocol  Status

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

GE1/0/1            10.1.1.1         400         ESP       Active

GE1/0/1            255.255.255.255  4294967295  ESP       Active

GE1/0/1            100::1/64        500         AH        Active

Global             \--               600         ESP       Active

表1-4 display ipsec sa brief命令显示信息描述表

字段

描述

Interface/Global

IPsec SA属于的接口或是全局（全局IPsec SA由IPsec安全框架生成）

Dst Address

IPsec隧道对端的IP地址

IPsec安全框架生成的SA中，该值无意义，显示为"\--"

SPI

IPsec SA的SPI

Protocol

IPsec采用的安全协议

Status

IPsec SA的状态：主用（Active）、备用（Backup）

·多机备份环境下，取值为Active表示主用、取值为Standby表示备用

·单机运行环境下，仅为Active，表示SA处于可用状态

\# 显示IPsec SA的个数。

\<Sysname\> display ipsec sa count

Total IPsec SAs count：4

\# 显示所有IPsec SA的详细信息。

\<Sysname\> display ipsec sa

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Interface: GigabitEthernet1/0/1

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  IPsec policy: r2

  Sequence number: 1

  Mode: ISAKMP

  Flow table status：Active

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

    Tunnel id: 3

    Encapsulation mode: tunnel

    Perfect Forward Secrecy:

    Inside VRF: vp1

    Path MTU: 1443

    Tunnel:

        local  address: 2.2.2.2

        remote address: 1.1.1.2

    Flow:

    sour addr: 192.168.2.0/255.255.255.0  port: 0  protocol: ip

    dest addr: 192.168.1.0/255.255.255.0  port: 0  protocol: ip

    Inbound ESP SAs

      SPI: 3564837569 (0xd47b1ac1)

      Connection ID： 1

      Transform set: ESP-ENCRYPT-AES-CBC-128 ESP-AUTH-SHA1

      SA duration (kilobytes/sec): 4294967295/604800

      SA remaining duration (kilobytes/sec): 1843200/2686

      Max received sequence-number: 5

      Anti-replay check enable: Y

      Anti-replay window size: 32

      UDP encapsulation used for NAT traversal: N

      Status: Active

    Outbound ESP SAs

      SPI: 801701189 (0x2fc8fd45)

      Connection ID： 2

      Transform set: ESP-ENCRYPT-AES-CBC-128 ESP-AUTH-SHA1

      SA duration (kilobytes/sec): 4294967295/604800

      SA remaining duration (kilobytes/sec): 1843200/2686

Max sent sequence-number: 6

      UDP encapsulation used for NAT traversal: N

      Status: Active

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Global IPsec SA

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  IPsec profile: profile

  Mode: Manual

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

    Encapsulation mode: transport

    Inbound AH SAs

      SPI: 1234563 (0x0012d683)

      Connection ID： 9

      Transform set: AH-SHA1

      No duration limit for this SA

    Outbound AH SAs

      SPI: 1234563 (0x002d683)

      Connection ID： 10

      Transform set: AH-SHA1

      No duration limit for this SA

表1-5 display ipsec sa命令显示信息描述表

字段

描述

Interface

IPsec SA所在的接口

Global IPsec SA

全局IPsec SA

IPsec policy

采用的IPsec安全策略名

IPsec profile

采用的IPsec安全框架名

Sequence number

IPsec安全策略表项顺序号

Mode

IPsec安全策略采用的协商方式

·Mannul：手工方式

·ISAKMP：IKE协商方式

·Template：IKE模板方式

Flow table status

IPsec下发引流规则的状态，包括以下取值：

·Inactive：引流规则下发失败

·Active：引流规则下发成功

该字段的显示与设备的型号有关，请以设备的实际情况为准

Tunnel id

IPsec隧道的ID号

Encapsulation mode

采用的报文封装模式，有两种：传输（transport）和隧道（tunnel）模式

Perfect Forward Secrecy

此IPsec安全策略发起协商时使用完善的前向安全（PFS）特性，取值包括：

·768-bit Diffie-Hellman组（**dh-group1**）

·1024-bit Diffie-Hellman组（**dh-group2**）

·1536-bit Diffie-Hellman组（**dh-group5**）

·2048-bit Diffie-Hellman组（**dh-group14**）

·2048-bit和256_bit子群Diffie-Hellman组（**dh-group24**）

Inside VRF

被保护数据所属的VRF实例名称

Path MTU

IPsec SA的路径MTU值

Tunnel

IPsec隧道的端点地址信息

local address

IPsec隧道的本端IP地址

remote address

IPsec隧道的对端IP地址

Flow

受保护的数据流信息

sour addr

数据流的源IP地址

dest addr

数据流的目的IP地址

port

端口号

protocol

协议类型，取值包括：

·ip：IPv4协议

·ipv6：IPv6协议

Inbound ESP SAs

入方向的ESP协议的IPsec SA信息

Outbound ESP SAs

出方向的ESP协议的IPsec SA信息

Inbound AH SAs

入方向的AH协议的IPsec SA信息

Outbound AH SAs

出方向的AH协议的IPsec SA信息

SPI

IPsec SA的SPI

Connection ID

IPsec SA标识

Transform set

IPsec安全提议所采用的安全协议及算法

SA duration (kilobytes/sec)

IPsec SA生存时间，单位为千字节或者秒

SA remaining duration (kilobytes/sec)

剩余的IPsec SA生存时间，单位为千字节或者秒

Max received sequence-number

入方向接收到的报文最大序列号

Max sent sequence-number

出方向发送的报文最大序列号

Anti-replay check enable

抗重放检测功能是否使能

Anti-replay window size

抗重放窗口宽度

UDP encapsulation used for NAT traversal

此IPsec SA是否使用NAT穿越功能

Status

IPsec SA的状态：

·多机备份环境下，取值为Active表示主用、取值为Standby表示备用

·单机运行环境下，取值仅为Active，表示SA处于可用状态

No duration limit for this SA

手工方式创建的IPsec SA无生命周期

【相关命令】

·**ipsec sa global-duration**

·**reset ipsec sa**

**IPsec \-- IPsec配置命令 \-- display ipsec statistics**

------------------------------------------------------------------------

**[display** **ipsec** **statistics**]命令用来显示IPsec处理的报文的统计信息。

【命令】

**[display ipsec statistics ** **tunnel-id** *tunnel-id* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[tunnel-id ***tunnel-id*]：显示指定IPsec隧道处理的报文统计信息。其中，*tunnel-id*为隧道的ID号，取值范围与设备的型号有关，请以设备的实际情况为准。通过**display ipsec tunnel brief**可以查看到已建立的IPsec隧道的ID号。

【使用指导】

如果不指定任何参数，则显示IPsec处理的所有报文的统计信息。

【举例】

\# 显示所有IPsec处理的报文统计信息。

\<Sysname\> display ipsec statistics

  IPsec packet statistics:

    Received/sent packets: 47/64

    Received/sent bytes: 3948/5208

    Dropped packets (received/sent): 0/45

    Dropped packets statistics

      No available SA: 0

      Wrong SA: 0

      Invalid length: 0

      Authentication failure: 0

      Encapsulation failure: 0

      Decapsulation failure: 0

      Replayed packets: 0

      ACL check failure: 45

      MTU check failure: 0

      Loopback limit exceeded: 0

      Crypto speed limit exceeded: 0

\# 显示ID为1的IPsec隧道处理的报文统计信息。

\<Sysname\> display ipsec statistics tunnel-id 1

  IPsec packet statistics:

    Received/sent packets: 5124/8231

    Received/sent bytes: 52348/64356

    Dropped packets (received/sent): 0/0

    Dropped packets statistics

      No available SA: 0

      Wrong SA: 0

      Invalid length: 0

      Authentication failure: 0

      Encapsulation failure: 0

      Decapsulation failure: 0

      Replayed packets: 0

      ACL check failure: 0

      MTU check failure: 0

      Loopback limit exceeded: 0

      Crypto speed limit exceeded: 0

表1-6 display ipsec statistics命令显示信息描述表

字段

描述

IPsec packet statistics

IPsec处理的报文统计信息

Received/sent packets

接收/发送的受安全保护的数据包的数目

Received/sent bytes

接收/发送的受安全保护的字节数目

Dropped packets (received/sent)

被设备丢弃了的受安全保护的数据包的数目（接收/发送）

Dropped packets statistics

被丢弃的数据包的详细信息

No available SA

因为找不到IPsec SA而被丢弃的数据包的数目

Wrong SA

因为IPsec SA错误而被丢弃的数据包的数目

Invalid length

因为数据包长度不正确而被丢弃的数据包的数目

Authentication failure

因为认证失败而被丢弃的数据包的数目

Encapsulation failure

因为加封装失败而被丢弃的数据包的数目

Decapsulation failure

因为解封装失败而被丢弃的数据包的数目

Replayed packets

被丢弃的重放的数据包的数目

ACL check failure

因为ACL检测失败而被丢弃的数据包的数目

MTU check failure

因为MTU检测失败而被丢弃的数据包的数目

Loopback limit exceeded

因为本机处理的次数超过限制而被丢弃的数据包的数目

Crypto speed limit exceeded

因为加密速度的限制而被丢弃的数据包的数目

【相关命令】

·**reset ipsec statistics**

**IPsec \-- IPsec配置命令 \-- display ipsec transform-set**

------------------------------------------------------------------------

**[display ipsec transform-set**]命令用来显示IPsec安全提议的信息。

【命令】

**[display** **ipsec transform-set** [ *transform-set-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[transform-set-name*]：指定IPsec安全提议的名字，为1～63个字符的字符串，不区分大小写。

【使用指导】

如果没有指定IPsec安全提议的名字，则显示所有IPsec安全提议的信息。

【举例】

\# 显示所有IPsec安全提议的信息。

\<Sysname\> display ipsec transform-set

IPsec transform set: mytransform

  State: incomplete

  Encapsulation mode: tunnel

  Transform: ESP

IPsec transform set: completeTransform

  State: complete

  Encapsulation mode: transport

  Transform: AH-ESP

  AH protocol:

    Integrity: SHA1

  ESP protocol:

    Integrity: SHA1

    Encryption: AES-CBC-128

表1-7 display ipsec transform-set命令显示信息描述表

字段

描述

IPsec transform set

IPsec安全提议的名字

State

IPsec安全提议是否完整

Encapsulation mode

IPsec安全提议采用的封装模式，包括两种：传输（transport）和隧道（tunnel）模式

Transform

IPsec安全提议采用的安全协议，包括三种：AH协议、ESP协议、AH-ESP（先采用ESP协议，再采用AH协议）

AH protocol

AH协议相关配置

ESP protocol

ESP协议相关配置

Integrity

安全协议采用的认证算法

Encryption

安全协议采用的加密算法

【相关命令】

·**ipsec transform-set**

**IPsec \-- IPsec配置命令 \-- display ipsec tunnel**

------------------------------------------------------------------------

**[display** **ipsec** **tunnel**]命令用来显示IPsec隧道的信息。

【命令】

**[display ipsec tunnel **[{ **brief** \| **count** \| **tunnel-id** *tunnel-id* }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[brief**]：显示IPsec隧道的简要信息。

**[count**]：显示IPsec隧道的个数。

**[tunnel-id ***tunnel-id*]：显示指定的IPsec隧道的详细信息。其中，*tunnel-id*为隧道的ID号，取值范围与设备的型号有关，请以设备的实际情况为准。

【使用指导】

IPsec通过在特定通信方之间（例如两个安全网关之间）建立"通道"，来保护通信方之间传输的用户数据，该通道通常称为IPsec隧道。

【举例】

\# 显示所有IPsec隧道的简要信息。

\<Sysname\> display ipsec tunnel brief

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Tunn-id   Src Address     Dst Address     Inbound SPI   Outbound SPI  Status

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

0         \--              \--              1000          2000          Active

                                          3000          4000

1         1.2.3.1         2.2.2.2         5000          6000          Active

                                          7000          8000

表1-8 display ipsec tunnel brief命令显示信息描述表

字段

描述

Tunn-id

IPsec隧道的ID号

Src Address

IPsec隧道的源地址

在IPsec Profile生成的SA中，该值无意义，显示为"\--"

Dst Address

IPsec隧道的目的地址

在IPsec Profile生成的SA中，该值无意义，显示为"\--"

Inbound SPI

IPsec隧道中生效的入方向SPI

如果该隧道使用了两种安全协议，则会分为两行分别显示两个入方向的SPI

Outbound SPI

IPsec隧道中生效的出方向SPI

如果该隧道使用了两种安全协议，则会分为两行分别显示两个入方向的SPI

Status

IPsec SA的状态：

·多机备份环境下，取值为Active表示主用、取值为Standby表示备用

·单机运行环境下，取值仅为Active，表示SA处于可用状态

\# 显示IPsec隧道的数目。

\<Sysname\> display ipsec tunnel count

Total IPsec Tunnel Count: 2

\# 显示所有IPsec隧道的详细信息。

\<Sysname\> display ipsec tunnel

Tunnel ID: 0

Status: active

Perfect forward secrecy:

SA\'s SPI:

    outbound:  2000        (0x000007d0)   [AH]

    inbound:   1000        (0x000003e8)   [AH]

    outbound:  4000        (0x00000fa0)   [ESP]

    inbound:   3000        (0x00000bb8)   [ESP]

Tunnel:

    local  address:

    remote address:

Flow:

Tunnel ID: 1

Status: Active

Perfect forward secrecy:

SA\'s SPI:

    outbound:  6000        (0x00001770)   [AH]

    inbound:   5000        (0x00001388)   [AH]

    outbound:  8000        (0x00001f40)   [ESP]

    inbound:   7000        (0x00001b58)   [ESP]

Tunnel:

    local  address: 1.2.3.1

    remote address: 2.2.2.2

Flow:

    as defined in ACL 3100

\# 显示ID号为1的IPsec隧道的详细信息。

\<Sysname\> display ipsec tunnel tunnel-id 1

Tunnel ID: 1

Status: Active

Perfect forward secrecy:

SA\'s SPI:

    outbound:  6000        (0x00001770)   [AH]

    inbound:   5000        (0x00001388)   [AH]

    outbound:  8000        (0x00001f40)   [ESP]

    inbound:   7000        (0x00001b58)   [ESP]

Tunnel:

    local  address: 1.2.3.1

    remote address: 2.2.2.2

Flow:

    as defined in ACL 3100

表1-9 display ipsec tunnel命令显示信息描述表

字段

描述

Tunnel ID

IPsec隧道的ID，用来唯一地标识一个IPsec隧道

Status

IPsec隧道的状态：

·多机备份环境下，取值为Active表示主用、取值为Standby表示备用

·单机运行环境下，取值仅为Active，表示隧道处于可用状态

Perfect Forward Secrecy

此IPsec安全策略发起协商时使用完善的前向安全（PFS）特性，取值包括：

·768-bit Diffie-Hellman组（**dh-group1**）

·1024-bit Diffie-Hellman组（**dh-group2**）

·1536-bit Diffie-Hellman组（**dh-group5**）

·2048-bit Diffie-Hellman组（**dh-group14**）

·2048-bit和256_bit子群Diffie-Hellman组（**dh-group24**）

SA\'s SPI

出方向和入方向的IPsec SA的SPI

Tunnel

IPsec隧道的端点地址信息

local  address

IPsec隧道的本端IP地址

remote address

IPsec隧道的对端IP地址

Flow

IPsec隧道保护的数据流，包括源地址、目的地址、源端口、目的端口、协议

as defined in ACL 3001

手工方式建立的IPsec隧道所保护的数据流的范围，例如IPsec隧道保护ACL 3001中定义的所有数据流

**IPsec \-- IPsec配置命令 \-- encapsulation-mode**

------------------------------------------------------------------------

**[encapsulation-mode**]命令用来配置安全协议对报文的封装模式。

**[undo encapsulation-mode**]命令用来恢复缺省情况。

【命令】

**[encapsulation-mode**[ { **transport** \| **tunnel** }]]

**[undo encapsulation-mode**]

【缺省情况】

使用隧道模式对IP报文进行封装。

【视图】

IPsec安全提议视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[transport**]：采用传输模式。

**[tunnel**]：采用隧道模式。

【使用指导】

传输模式下的安全协议主要用于保护上层协议报文，仅传输层数据被用来计算安全协议头，生成的安全协议头以及加密的用户数据（仅针对ESP封装）被放置在原IP头后面。若要求端到端的安全保障，即数据包进行安全传输的起点和终点为数据包的实际起点和终点时，才能使用传输模式。

隧道模式下的安全协议用于保护整个IP数据包，用户的整个IP数据包都被用来计算安全协议头，生成的安全协议头以及加密的用户数据（仅针对ESP封装）被封装在一个新的IP数据包中。这种模式下，封装后的IP数据包有内外两个IP头，其中的内部IP头为原有的IP头，外部IP头由提供安全服务的设备添加。在安全保护由设备提供的情况下，数据包进行安全传输的起点或终点不为数据包的实际起点和终点时（例如安全网关后的主机），则必须使用隧道模式。隧道模式用于保护两个安全网关之间的数据传输。

在IPsec隧道的两端，IPsec安全提议所采用的封装模式要一致。

IPsec profile要引用的IPsec安全提议所采用的封装模式必须为传输模式[。]

【举例】

\# 指定IPsec安全提议tran1采用传输模式对IP报文进行封装。

\<Sysname\> system-view

Sysname ipsec transform-set tran1

Sysname-ipsec-transform-set-tran1 encapsulation-mode transport

【相关命令】

·**ipsec ****transform-set**

**IPsec \-- IPsec配置命令 \-- esp authentication-algorithm**

------------------------------------------------------------------------

**[esp authentication-algorithm**]命令用来配置ESP协议采用的认证算法。

**[undo esp authentication-algorithm**]命令用来删除所有指定的ESP协议采用的认证算法。

【命令】

非FIPS模式下：

**[esp authentication-algorithm **[{ **md5** \| **sha1** } \*]]

**[undo esp authentication-algorithm**]

FIPS模式下：

**[esp authentication-algorithm sha1**]

**[undo esp authentication-algorithm**]

【缺省情况】

ESP协议没有采用任何认证算法。

【视图】

IPsec安全提议视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[md5**]：采用HMAC-MD5认证算法，密钥长度128比特。

**[sha1**]：采用HMAC-SHA1认证算法，密钥长度160比特。

【使用指导】

非FIPS模式下，每个IPsec安全提议中均可以配置多个ESP认证算法，其优先级为配置顺序。

对于手工方式以及IKEv1（第1版本的IKE协议）协商方式的IPsec安全策略，IPsec安全提议中配置顺序首位的ESP认证算法生效。为保证成功建立IPsec隧道，隧道两端指定的IPsec安全提议中配置的首个ESP认证算法需要一致。

【举例】

\# 配置IPsec安全提议采用的ESP认证算法为HMAC-SHA1算法，密钥长度为160比特。

\<Sysname\> system-view

Sysname ipsec transform-set tran1

Sysname-ipsec-transform-set-tran1 esp authentication-algorithm sha1

【相关命令】

·**ipsec ****transform-set**

**IPsec \-- IPsec配置命令 \-- esp encryption-algorithm**

------------------------------------------------------------------------

**[esp encryption-algorithm**]命令用来配置ESP协议采用的加密算法。

**[undo esp encryption-algorithm**]命令用来删除所有指定的ESP协议采用的加密算法。

【命令】

低加密版本中：

**[esp encryption-algorithm des-cbc**]

**[undo esp encryption-algorithm**]

高加密版本-非FIPS模式下：

**[esp encryption-algorithm **[{ **3des-cbc** \| **aes-cbc-128** \| **aes-cbc-192** \| **aes-cbc-256** \| **des-cbc** \| **null** } \*]]

**[undo esp encryption-algorithm.**]

高加密版本-FIPS模式下：

**[esp encryption-algorithm **[{ **aes-cbc-128** \| **aes-cbc-192** \| **aes-cbc-256** }\*]]

**[undo esp encryption-algorithm**]

【缺省情况】

ESP协议没有采用任何加密算法。

【视图】

IPsec安全提议视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[3des-cbc**]：采用CBC模式的3DES算法，密钥长度为168比特[。]

**[aes-cbc-128**]：采用CBC模式的AES算法，密钥长度为128比特[。]

**[aes-cbc-192**]：采用CBC模式的AES算法，密钥长度为192比特[。]

**[aes-cbc-256**]：采用CBC模式的AES算法，密钥长度为256比特[。]

**[des-cbc**]：采用CBC模式的DES算法，密钥长度为64比特[。]

**[null**]：采用NULL加密算法，表示不进行加密。

【描述】

每个IPsec安全提议中均可以配置多个ESP加密算法，其优先级为配置顺序。

对于手工方式以及IKEv1（第1版本的IKE协议）协商方式的IPsec安全策略，IPsec安全提议中配置顺序首位的ESP加密算法生效。为保证成功建立IPsec隧道，隧道两端指定的IPsec安全提议中配置的首个ESP加密算法需要一致。

【举例】

\# 配置IPsec安全提议采用的ESP加密算法为CBC模式的AES算法，密钥长度为128比特。

\<Sysname\> system-view

Sysname ipsec transform-set tran1

Sysname-ipsec-transform-set-tran1 esp encryption-algorithm aes-cbc-128

【相关命令】

·**ipsec ****transform-set**

**IPsec \-- IPsec配置命令 \-- ike-profile**

------------------------------------------------------------------------

**[ike-profile**]命令用来指定IPsec安全策略/IPsec安全策略模板引用的IKE profile。

**[undo ike-profile**]命令用来取消在IPsec安全策略/安全策略模板中引用IKE profile。

【命令】

**[ike-profile ***profile-name*]

**[undo ike-profile**]

【缺省情况】

IPsec安全策略/IPsec安全策略模板没有引用任何IKE profile。若系统视图下配置了IKE profile，则使用系统视图下配置的IKE profile进行性协商，否则使用全局的IKE参数进行协商。

【视图】

IPsec安全策略视图/IPsec安全策略模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[profile-name*]：IKE profile的名称，为1～63个字符的字符串，不区分大小写。

【使用指导】

IPsec安全策略、IPsec安全策略模板引用的IKE profile中定义了用于IKE协商的相关参数。

一个IPsec安全策略视图或一个IPsec安全策略模板视图下只能引用一个IKE profile。

【举例】

\# 指定IPsec安全策略policy1中引用的IKE profile为profile1。

\<Sysname\> system-view

Sysname ipsec policy policy1 10 isakmp

Sysname-ipsec-policy-isakmp-policy1-10 ike-profile profile1

【相关命令】

·**ike profile**（安全命令参考/IKE）

**IPsec \-- IPsec配置命令 \-- ipsec anti-replay check**

------------------------------------------------------------------------

**[ipsec anti-replay check**]命令用来开启IPsec抗重放检测功能。

**[undo ipsec anti-replay check**]用来关闭IPsec抗重放检测功能。

【命令】

**[ipsec anti-replay check**]

**[undo ipsec anti-replay check**]

【缺省情况】

IPsec抗重放检测功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

对重放报文的解封装无意义，并且解封装过程涉及密码学运算，会消耗设备大量的资源，导致业务可用性下降，造成了拒绝服务攻击。通过使能IPsec抗重放检测功能，将检测到的重放报文在解封装处理之前丢弃，可以降低设备资源的消耗。

在某些特定环境下，业务数据报文的接收顺序可能与正常的顺序差别较大，虽然并非有意的重放攻击，但会被抗重放检测认为是重放报文，导致业务数据报文被丢弃，影响业务的正常运行。因此，这种情况下就可以通过关闭IPsec抗重放检测功能来避免业务数据报文的错误丢弃，也可以通过适当地增大抗重放窗口的宽度，来适应业务正常运行的需要。

只有IKE协商的IPsec SA才能够支持抗重放检测，手工方式生成的IPsec SA不支持抗重放检测。因此该功能使能与否对手工方式生成的IPsec SA没有影响。

【举例】

\# 开启IPsec抗重放检测功能。

\<Sysname\> system-view

Sysname ipsec anti-replay check

【相关命令】

·**ipsec anti-replay window**

**IPsec \-- IPsec配置命令 \-- ipsec anti-replay window**

------------------------------------------------------------------------

**[ipsec anti-replay window**]命令用来配置IPsec抗重放窗口的宽度。

**[undo ipsec anti-replay window**]命令用来恢复缺省情况。

【命令】

**[ipsec anti-replay window ***width*]

**[undo ipsec anti-replay window**]

【缺省情况】

IPsec抗重放窗口的宽度为64。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[width*]：IPsec抗重放窗口的宽度，可取的值为64、128、256、512、1024，单位为报文个数。

【描述】

修改后的抗重放窗口宽度仅对新协商成功的IPsec SA生效。

在某些特定环境下，业务数据报文的接收顺序可能与正常的顺序差别较大，虽然并非有意的重放攻击，但会被抗重放检测认为是重放报文，导致业务数据报文被丢弃，影响业务的正常运行。因此，这种情况下就可以通过关闭IPsec抗重放检测功能来避免业务数据报文的错误丢弃，也可以通过适当地增大抗重放窗口的宽度，来适应业务正常运行的需要。

【举例】

\# 配置IPsec抗重放窗口的宽度为128。

\<Sysname\> system-view

Sysname ipsec anti-replay window 128

【相关命令】

·**ipsec anti-replay check**

**IPsec \-- IPsec配置命令 \-- ipsec decrypt-check enable**

------------------------------------------------------------------------

**[ipsec decrypt-check enable**]命令用来开启解封装后IPsec报文的ACL检查功能。

**[undo ipsec decrypt-check**]命令用来关闭解封装后IPsec报文的ACL检查功能。

【命令】

**[ipsec decrypt-check enable**]

**[undo ipsec decrypt-check enable**]

【缺省情况】

解封装后IPsec报文的ACL检查功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在隧道模式下，接口入方向上解封装的IPsec报文的内部IP头有可能不在当前IPsec安全策略引用的ACL的保护范围内，如网络中一些恶意伪造的攻击报文就可能有此问题，所以设备需要重新检查解封装后的报文的IP头是否在ACL保护范围内。使能该功能后可以保证ACL检查不通过的报文被丢弃，从而提高网络安全性。

【举例】

\# 开启解封装后IPsec报文的ACL检查功能。

\<Sysname\> system-view

Sysname ipsec decrypt-check enable

**IPsec \-- IPsec配置命令 \-- ipsec logging packet enable**

------------------------------------------------------------------------

**[ipsec logging packet enable**]命令用来开启IPsec报文日志记录功能。

**[undo ipsec logging packet enable**]命令用来关闭IPsec报文日志记录功能。

【命令】

**[ipsec logging packet enable**]

**[undo ipsec logging packet enable**]

【缺省情况】

IPsec报文日志记录功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启IPsec报文日志记录功能后，设备会在丢弃IPsec报文的情况下，例如入方向找不到对应的IPsec SA，AH/ESP认证失败或ESP加密失败等时，输出相应的日志信息，该日志信息内容主要包括报文的源和目的IP地址、报文的SPI值、报文的序列号信息，以及设备丢包的原因。

【举例】

\# 开启IPsec报文日志记录功能。

\<Sysname\> system-view

Sysname ipsec logging packet enable

**IPsec \-- IPsec配置命令 \-- ipsec df-bit**

------------------------------------------------------------------------

**[ipsec df-bit**]命令用来为当前接口设置IPsec封装后外层IP头的DF位。

**[undo ipsec df-bit**]命令用来恢复缺省情况。

【命令】

**[ipsec df-bit **[{ **clear** \| **copy** \| **set** }]]

**[undo ipsec df-bit**]

【缺省情况】

接口下未设置IPsec封装后外层IP头的DF位，采用全局设置的DF位。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[clear**]：表示清除外层IP头的DF位，IPsec封装后的报文可被分片。

**[copy**]：表示外层IP头的DF位从原始报文IP头中拷贝。

**[set**]：表示设置外层IP头的DF位，IPsec封装后的报文不能分片。

【使用指导】

该功能仅在IPsec的封装模式为隧道模式时有效（因为传输模式不会增加新的IP头，因此对于传输模式无影响）。

该功能用于设置IPsec隧道模式封装后的外层IP头的DF位，原始报文IP头的DF位不会被修改。

如果有多个接口应用了共享源接口安全策略，则这些接口上必须使用相同的DF位设置。

转发报文时对报文进行分片、重组，可能会导致报文的转发延时较大。若设置了封装后IPsec报文的DF位，则不允许对IPsec报文进行分片，可以避免引入分片延时。这种情况下，要求IPsec报文转发路径上各个接口的MTU大于IPsec报文长度，否则，会导致IPsec报文被丢弃。如果无法保证转发路径上各个接口的MTU大于IPsec报文长度，则建议清除DF位。

【举例】

\# 在接口GigabitEthernet1/0/2上设置IPsec封装后外层IP头的DF位。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/2

Sysname-GigabitEthernet1/0/2 ipsec df-bit set

【相关命令】

·**ipsec global-df-bit**

**IPsec \-- IPsec配置命令 \-- ipsec global-df-bit**

------------------------------------------------------------------------

**[ipsec global-df-bit**]命令用来为所有接口设置IPsec封装后外层IP头的DF位。

**[undo ipsec global-df-bit**]命令用来恢复缺省情况。

【命令】

**[ipsec global-df-bit**[ { **clear** \| **copy** \| **set** }]]

**[undo ipsec global-df-bit**]

【缺省情况】

IPsec封装后外层IP头的DF位从原始报文IP头中拷贝。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[clear**]：表示清除外层IP头的DF位，IPsec封装后的报文可被分片。

**[copy**]：表示外层IP头的DF位从原始报文IP头中拷贝。

**[set**]：表示设置外层IP头的DF位，IPsec封装后的报文不能分片。

【使用指导】

该功能仅在IPsec的封装模式为隧道模式时有效（因为传输模式不会增加新的IP头，因此对于传输模式无影响）。

该功能用于设置IPsec隧道模式封装后的外层IP头的DF位，原始报文IP头的DF位不会被修改。

转发报文时对报文进行分片、重组，可能会导致报文的转发延时较大。若设置了封装后IPsec报文的DF位，则不允许对IPsec报文进行分片，可以避免引入分片延时。这种情况下，要求IPsec报文转发路径上各个接口的MTU大于IPsec报文长度，否则，会导致IPsec报文被丢弃。如果无法保证转发路径上各个接口的MTU大于IPsec报文长度，则建议清除DF位。

【举例】

\# 为所有接口设置IPsec封装后外层IP头的DF位。

\<Sysname\> system-view

Sysname ipsec global-df-bit set

【相关命令】

·**ipsec df-bit**

**IPsec \-- IPsec配置命令 \-- ipsec apply**

------------------------------------------------------------------------

**[ipsec** **apply**]命令用来在接口上应用IPsec安全策略。

**[undo ipsec apply**]命令用来从接口上取消应用的IPsec安全策略。

【命令】

**[ipsec**[ **apply** { **ipv6-policy** \| **policy** } *policy-name*]]

**[undo**[ **ipsec** **apply** { **ipv6-policy** \| **policy** }]]

【缺省情况】

接口上没有应用任何IPsec安全策略。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv6-policy**]：指定IPv6 IPsec安全策略。

**[policy**]：指定IPv4 IPsec安全策略。

*[policy-name*]：IPsec安全策略的名字，为1～63个字符的字符串，不区分大小写。

【使用指导】

一个接口下只能应用一个IPsec安全策略。

IKE方式的IPsec安全策略可以应用到多个接口上，但建议只应用到一个接口上；手工方式的IPsec安全策略只能应用到一个接口上。

【举例】

\# 在接口GigabitEthernet1/0/2上应用名为policy1的IPsec安全策略。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/2

Sysname-GigabitEthernet1/0/2 ipsec apply policy policy1

【相关命令】

·**display****ipsec**[ { **ipv6-policy** \| **policy** }]

[·**ipsec**[ { **ipv6-policy** \| **policy** }]]

**IPsec \-- IPsec配置命令 \-- ipsec { ipv6-policy \| policy }**

------------------------------------------------------------------------

**[ipsec **[{ **ipv6-policy** \| **policy** }]]命令用来创建一条IPsec安全策略，并进入IPsec安全策略视图。

**[undo**[ **ipsec** { **ipv6-policy** \| **policy** }]]命令用来删除指定的IPsec安全策略。

【命令】

**[ipsec**[ { **ipv6-policy** \| **policy** } *policy-name* *seq-number* [ **isakmp** \| **manual** ]]]

**[undo**[ **ipsec** { **ipv6-policy** \| **policy** } *policy-name* [ *seq-number* ]]]

【缺省情况】

不存在任何IPsec安全策略。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv6-policy**]：指定IPv6 IPsec安全策略。

**[policy**]：指定IPv4 IPsec安全策略。

*[policy-name*]：IPsec安全策略的名字，为1～63个字符的字符串，不区分大小写。

*[seq-number*]：IPsec安全策略的顺序号，取值范围为1～65535。

**[isakmp**]：指定通过IKE协商建立IPsec SA。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[manual**]：指定用手工方式建立IPsec SA。

【使用指导】

·创建IPsec安全策略时，必须指定协商方式（**isakmp**或**manual**）。进入已创建的IPsec安全策略时，可以不指定协商方式。

·不能修改已创建的IPsec安全策略的协商方式。

·一个IPsec安全策略是若干具有相同名字、不同顺序号的IPsec安全策略表项的集合。在同一个IPsec安全策略中，顺序号越小的IPsec安全策略表项优先级越高。

·对于**undo**命令，携带*seq-number*参数时表示删除一个IPsec安全策略表项，不携带该参数时表示删除指定IPsec安全策略的所有表项。

·IPv4 IPsec安全策略和IPv6 IPsec安全策略名称可以相同。

【举例】

\# 创建一个名字为policy1、顺序号为100、采用IKE方式协商IPsec SA的IPsec安全策略，并进入IPsec安全策略视图。

\<Sysname\> system-view

Sysname ipsec policy policy1 100 isakmp

Sysname-ipsec-policy-isakmp-policy1-100

\# 创建一个名字为policy1、顺序号为101、采用手工方式建立IPsec SA的IPsec安全策略，并进入IPsec安全策略视图。

\<Sysname\> system-view

Sysname ipsec policy policy1 101 manual

Sysname-ipsec-policy-manual-policy1-101

【相关命令】

[·**display ipsec **[{ **ipv6-policy** \| **policy** }]]

·**ipsec apply**

**IPsec \-- IPsec配置命令 \-- ipsec { ipv6-policy \| policy } isakmp template**

------------------------------------------------------------------------

**[ipsec**[ { **ipv6-policy** \| **policy** } **isakmp template**]]命令用来引用IPsec安全策略模板创建一条IKE协商方式的IPsec安全策略。

**[undo**[ **ipsec** { **ipv6-policy** \| **policy** }]]命令用来删除指定的IPsec安全策略。

【命令】

**[ipsec**[ { **ipv6-policy** \| **policy** } *policy-name* *seq-number* **isakmp template** *template-name*]]

**[undo**[ **ipsec** { **ipv6-policy** \| **policy** } *policy-name* [ *seq-number* ]]]

【缺省情况】

没有任何IPsec安全策略存在。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv6-policy**]：指定IPv6 IPsec安全策略。

**[policy**]：指定IPv4 IPsec安全策略。

*[policy-name*]：IPsec安全策略的名字，为1～63个字符的字符串，不区分大小写。

*[seq-number*]：IPsec安全策略的顺序号，取值范围为1～65535，值越小优先级越高。

**[isakmp template*** template-name*]：指定被引用的IPsec安全策略模板。*template-name*表示IPsec安全策略模板的名字，为1～63个字符的字符串，不区分大小写。

【使用指导】

·不携带*seq-number*参数的**undo**命令用来删除一个安全策略。

·应用了该类IPsec安全策略的接口不能发起协商，仅可以响应远端设备的协商请求。由于IPsec安全策略模板中未定义的可选参数由发起方来决定，而响应方会接受发起方的建议，因此这种方式创建的IPsec安全策略适用于通信对端（例如对端的IP地址）未知的情况下，允许这些对端设备向本端设备主动发起协商。

【举例】

\# 引用IPsec策略模板temp1，创建名字为policy2、顺序号为200的IPsec安全策略。

\<Sysname\> system-view

Sysname ipsec policy policy2 200 isakmp template temp1

【相关命令】

[·**display ipsec **[{ **ipv6-policy** \| **policy** }]]

[·**ipsec**[ { **ipv6-policy-template** \| **policy-template** }]]

**IPsec \-- IPsec配置命令 \-- ipsec { ipv6-policy \| policy } local-address**

------------------------------------------------------------------------

**[ipsec**[ { **ipv6-policy** \| **policy** } **local-address**]]命令用来配置IPsec安全策略为共享源接口IPsec安全策略，即将指定的IPsec安全策略与一个源接口进行绑定。

**[undo ipsec **[{ **ipv6-policy** \| **policy** } **local-address**]]命令用来取消IPsec安全策略为共享源接口IPsec安全策略。

【命令】

**[ipsec**[ { **ipv6-policy** \| **policy** } *policy-name* **local-address** *interface-type interface-number*]]

**[undo**[ **ipsec** { **ipv6-policy** \| **policy** } *policy-name* **local-address**]]

【缺省情况】

IPsec安全策略不是共享源接口IPsec安全策略。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv6-policy**]：指定IPv6 IPsec安全策略。

**[policy**]：指定IPv4 IPsec安全策略。

*[policy-name*]：共享该接口IP地址的IPsec安全策略的名字，为1～63个字符的字符串，不区分大小写。

**[local-address*** interface-type interface-number*]：指定的共享源接口的名称。*interface-type interface-nunmber*为接口类型和接口编号。

【使用指导】

在不同的接口上应用安全策略时，各个接口将分别协商生成IPsec SA。如果两个互为备份的接口上都引用了IPsec安全策略，并采用相同的安全策略，则在主备链路切换时，接口状态的变化会触发重新进行IKE协商，从而导致IPsec业务流的暂时中断。通过将一个IPsec安全策略与一个源接口绑定，使之成为共享源接口IPsec安全策略，可以实现多个应用该共享源接口IPsec安全策略的出接口共享同一个指定的源接口（称为共享源接口）协商出的IPsec SA。只要该源接口的状态不变化，各接口上IPsec业务就不会中断。

·当非共享源接口IPsec安全策略应用于业务接口，并已经生成IPsec SA时，如果将该安全策略配置为共享源接口安全策略，则已经生成的IPsec SA将被删除。

·只有IKE协商方式的IPsec安全策略才能配置为IPsec共享源接口安全策略，手工方式的IPsec安全策略不能配置为共享源接口IPsec安全策略。

l一个IPsec安全策略只能与一个源接口绑定，新配置将覆盖旧配置。

·一个源接口可以同时与多个IPsec安全策略绑定。

·推荐使用状态较为稳定的接口作为共享源接口，例如Loopback接口。

【举例】

\# 配置IPsec安全策略map为共享源接口安全策略，共享源接口为Loopback11。

\<Sysname\> system-view

Sysname ipsec policy map local-address loopback 11

【相关命令】

[·**ipsec **[{ **ipv6-policy** \| **policy** }]]

**IPsec \-- IPsec配置命令 \-- ipsec { ipv6-policy-template \| policy-template }**

------------------------------------------------------------------------

**[ipsec**[ { **ipv6-policy-template** \| **policy-template** }]]命令用来创建一个IPsec安全策略模板，并进入IPsec安全策略模板视图。

**[undo**[ **ipsec** { **ipv6-policy-template** \| **policy-template** }]]命令用来删除指定的IPsec安全策略模板。

【命令】

**[ipsec**[ { **ipv6-policy-template** \| **policy-template** } *template-name* *seq-number*]]

**[undo**[ **ipsec** { **ipv6-policy-template** \| **policy-template** } *template-name* [ *seq-number* ]]]

【缺省情况】

不存在任何IPsec安全策略模板。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv6-policy-template**]：指定IPv6 IPsec安全策略模板。

**[policy-template**]：指定IPv4 IPsec安全策略模板。

*[template-name*]：IPsec安全策略模板的名字，为1～63个字符的字符串，不区分大小写。

*[seq-number*]：IPsec安全策略模板表项的顺序号，取值范围为1～65535，值越小优先级越高。

【使用指导】

IPsec安全策略模板与直接配置的IKE协商方式的IPsec安全策略中可配置的参数类似，但是配置较为简单，除了IPsec安全提议和IKE对等体之外的其它参数均为可选。

·携带*seq-number*参数的**undo**命令用来删除一个IPsec安全策略模板表项。

·一个IPsec安全策略模板是若干具有相同名字、不同顺序号的IPsec安全策略模板表项的集合。

·IPv4 IPsec安全策略模板和IPv6 IPsec安全策略模板名称可以相同。

【举例】

\# 创建一个名字为template1、顺序号为100的IPsec安全策略模板，并进入IPsec安全策略模板视图。

\<Sysname\> system-view

Sysname ipsec policy-template template1 100

Sysname-ipsec-policy-template-template1-100

【相关命令】

[·**display ipsec ****-template**[ \| **policy**]**-template** }

[·**ipsec **[{ **ipv6-policy** \| **policy** }]]

[·**ipsec**[ { **ipv6**-**policy** \| **policy** } **isakmp** **template**]]

**IPsec \-- IPsec配置命令 \-- ipsec profile**

------------------------------------------------------------------------

**[ipsec profile**]命令用来创建一个IPsec安全框架，并进入IPsec安全框架视图。

**[undo ipsec profile**]命令用来删除指定的IPsec安全框架。

【命令】]

**[ipsec profile ***profile-name*[ [ **manual** \| **isakmp** ]]]

**[undo** **ipsec** **profile** *profile-name*]

【缺省情况】

没有任何IPsec安全框架存在。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[profile-name*]：IPsec安全框架的名字，为1～63个字符的字符串，不区分大小写。

**[manual**]：手工方式的IPsec安全框架。

**[isakmp**]：指定通过IKE协商建立安全联盟。

【使用指导】

·创建IPsec安全框架时，必须指定协商方式（**manual**或**isakmp**）；进入已创建的IPsec安全框架时，可以不指定协商方式。

·手工方式IPsec profile专门用于为应用协议配置IPsec安全策略，它相当于一个手工方式创建的IPsec安全策略，其中的应用协议可包括但不限于OSPFv3、IPv6 BGP、RIPng。

·IKE协商方式IPsec profile用于为应用协议模块自动协商生成安全联盟，不限制对端的地址，不需要进行ACL匹配，且适用于IPv4和IPv6应用协议，其中的应用协议模块包括但是不限于ADVPN等。

【举例】

\# 配置名字为profile1的IPsec安全框架，通过手工配置建立安全联盟。

\<Sysname\> system-view

Sysname ipsec profile profile1 manual

Sysname-ipsec-profile---manual-profile1

\# 配置名字为profile1的IPsec安全框架，通过IKE协商建立安全联盟。

\<Sysname\> system-view

Sysname ipsec profile profile1 isakmp

Sysname-ipsec-profile-isakmp-profile1

【相关命令】

·**display ipsec ****profile**

**IPsec \-- IPsec配置命令 \-- ipsec redundancy enable**

------------------------------------------------------------------------

![说明](IPsec命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ipsec redundancy enable**]命令用来使能IPsec冗余备份功能。

**[undo ipsec redundancy enable**]命令用来恢复缺省情况。

【命令】

**[ipsec redundancy enable**]

**[undo**]**ipsec redundancy enable **

【缺省情况】

IPsec冗余备份功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

使能冗余备份功能后，系统会根据命令**redundancy replay-interval**指定的备份间隔对系统中的所有IPsec SA进行抗重放窗口值和序列号的备份，当发生主备切换时，可以保证主备IPsec流量不中断和抗重放保护不间断。

【举例】

\# 使能IPsec冗余备份功能。

\<Sysname\> system-view

Sysname ipsec redundancy enable

【相关命令】

·**redundancy replay-interval**

**IPsec \-- IPsec配置命令 \-- ipsec sa global-duration**

------------------------------------------------------------------------

**[ipsec sa global-duration**]命令用来配置全局的IPsec SA生存时间。

**[undo ipsec sa global-duration**]命令用来恢复缺省情况。

【命令】

**[ipsec sa global-duration**[ { **time-based** *seconds* \| **traffic-based** *kilobytes* }]]

**[undo ipsec sa global-duration**[ { **time-based** \| **traffic-based** }]]

【缺省情况】

IPsec SA基于时间的生存时间为3600秒，基于流量的生存时间为1843200千字节。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[time-based*** seconds*]：指定基于时间的全局生存时间，取值范围为180～604800，单位为秒。

**[traffic-based*** kilobytes*]：指定基于流量的全局生存时间，取值范围为2560～4294967295，单位为千字节。如果流量达到此值，则生存时间到期。

【使用指导】

IPsec安全策略/IPsec安全策略模板视图下也可配置IPsec SA的生存时间，若IPsec安全策略/IPsec安全策略模板视图和全局都配置了IPsec SA的生存时间，则优先采用IPsec安全策略/IPsec安全策略模板视图下的配置值与对端协商。

IKE为IPsec协商建立IPsec SA时，采用本地配置的生存时间和对端提议的IPsec SA生存时间中较小的一个。

可同时存在基于时间和基于流量两种方式的IPsec SA生存时间，只要IPsec SA的生存时间到达指定的时间或流量时，该IPsec SA就会失效。IPsec SA失效前，IKE将为IPsec对等体协商建立新的IPsec SA，这样，在旧的IPsec SA失效前新的IPsec SA就已经准备好。在新的IPsec SA开始协商而没有协商好之前，继续使用旧的IPsec SA保护通信。在新的IPsec SA协商好之后，则立即采用新的IPsec SA保护通信。

【举例】

\# 配置全局的IPsec SA生存时间为两个小时，即7200秒。

\<Sysname\> system-view

Sysname ipsec sa global-duration time-based 7200

\# 配置全局的IPsec SA生存时间为10M字节，即传输10240千字节的流量后，当前的IPsec SA过期。

Sysname ipsec sa global-duration traffic-based 10240

【相关命令】

·**display ipsec sa**

·**sa duration**

**IPsec \-- IPsec配置命令 \-- ipsec sa idle-time**

------------------------------------------------------------------------

**[ipsec sa idle-time**]命令用来开启全局的IPsec SA空闲超时功能，并配置全局IPsec SA空闲超时时间。在指定超时时间内没有流量匹配的IPsec SA即被删除。

**[undo ipsec sa idle-time**]命令用来恢复缺省情况。

【命令】

**[ipsec sa idle-time **]*seconds*

**[undo ipsec sa idle-time**]

【缺省情况】

全局的IPsec SA空闲超时功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：IPsec SA的空闲超时时间，取值范围为60～86400，单位为秒。

【使用指导】

此功能只适用于IKE协商出的IPsec SA。

IPsec安全策略/IPsec安全策略模板/IPsec安全框架视图下也可配置IPsec SA的空闲超时时间，若IPsec安全策略/IPsec安全策略模板/IPsec安全框架视图和全局都配置了IPsec SA的空闲超时时间，则优先采用IPsec安全策略/IPsec安全策略模板/IPsec安全框架视图下的配置值。

【举例】

\# 配置全局IPsec SA的空闲超时时间为600秒。

\<Sysname\> system-view

Sysname ipsec sa idle-time 600

【相关命令】

·**display ipsec sa**

·**sa idle-time**

**IPsec \-- IPsec配置命令 \-- ipsec transform-set**

------------------------------------------------------------------------

**[ipsec transform-set**]命令用来创建IPsec安全提议，并进入IPsec安全提议视图。

**[undo ipsec  transform-set**]命令用来删除指定的IPsec安全提议。

【命令】

**[ipsec transform-set ***transform-set-name*]

**[undo ipsec transform-set ***transform-set-name*]

【缺省情况】

没有任何IPsec安全提议存在。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[t*]*ransform-set-name*：IPsec安全提议的名字，为1\~63个字符的字符串，不区分大小写。

【使用指导】

IPsec安全提议是IPsec安全策略的一个组成部分，它用于保存IPsec需要使用的安全协议、加密/认证算法以及封装模式，为IPsec协商SA提供各种安全参数。

【举例】

\# 创建名为tran1的IPsec安全提议，并进入IPsec安全提议视图。

\<Sysname\> system-view

Sysname ipsec transform-set tran1

Sysname-transform-set-tran1

【相关命令】

·**display ipsec transform-set**

**IPsec \-- IPsec配置命令 \-- local-address**

------------------------------------------------------------------------

**[local-address**]命令用来配置IPsec隧道的本端IP地址。

**[undo local-address**]命令用来恢复缺省情况。

【命令】

**[local-address**[ { *ipv4-address* \| **ipv6** *ipv6-address* }]]

**[undo local-address**]

【缺省情况】

IPsec隧道的本端IPv4地址为应用IPsec安全策略的接口的主IPv4地址，本端IPv6地址为应用IPsec安全策略的接口的第一个IPv6地址。

【视图】

IPsec安全策略视图/IPsec安全策略模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv4-address*]：IPsec隧道的本端IPv4地址。

**[ipv6** *ipv6-address*]：IPsec隧道的本端IPv6地址。

【使用指导】

采用IKE协商方式的IPsec安全策略上，发起方的IPsec隧道的对端IP地址必须与响应方的IPsec隧道本端IP地址一致。

在VRRP组网环境中，必须指定IPsec隧道本端的IP地址为应用IPsec安全策略的接口所在备份组的虚拟IP地址。

【举例】

\# 配置IPsec隧道的本端IP地址为1.1.1.1。

\<Sysname\> system-view

Sysname ipsec policy map 1 isakmp

Sysname-ipsec-policy-isakmp-map-1 local-address 1.1.1.1

【相关命令】

·**remote-address**

**IPsec \-- IPsec配置命令 \-- pfs**

------------------------------------------------------------------------

**[pfs**]命令用来配置在使用此安全提议发起IKE协商时使用PFS（Perfect Forward Secrecy，完善的前向安全）特性。

**[undo pfs**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[pfs **[{ **dh-group1** \| **dh-group2** \| **dh-group5** \| **dh-group14** \| **dh-group24** }]]

**[undo pfs**]

FIPS模式下：

**[pfs dh-group14**]

**[undo pfs**]

【缺省情况】

使用IPsec安全策略发起IKE协商时不使用PFS特性。

【视图】

IPsec安全提议视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[dh-group1**]：采用768-bit Diffie-Hellman组。

**[dh-group2**]：采用1024-bit Diffie-Hellman组[。]

**[dh-group5**]：采用1536-bit Diffie-Hellman组。

**[dh-group14**]：采用2048-bit Diffie-Hellman组[。]

**[dh-group24**]：采用2048-bit和256_bit子群Diffie-Hellman组[。]

【使用指导】

2048-bit和256-bit子群Diffie-Hellman组（**dh-group24**）、2048-bit Diffie-Hellman组（**dh-group14**）、1536-bit Diffie-Hellman组（**dh-group5**）、1024-bit Diffie-Hellman组（**dh-group2**）、768-bit Diffie-Hellman组（**dh-group1**）算法的强度，即安全性和需要计算的时间依次递减。

发起方的PFS强度必须大于或等于响应方的PFS强度，否则IKE协商会失败。

不配置PFS特性的一端，按照对端的PFS特性要求进行IKE协商。

【举例】

\# 配置IPsec安全提议使用PFS特性，并采用2048-bit Diffie-Hellman组。

\<Sysname\> system-view

Sysname ipsec transform-set tran1

Sysname-ipsec-transform-set-tran1 pfs dh-group14

**IPsec \-- IPsec配置命令 \-- protocol**

------------------------------------------------------------------------

**[protocol**]命令用来配置IPsec安全提议采用的安全协议。

**[undo protocol**]命令用来恢复缺省情况。

【命令】

**[protocol **[{ **ah** \| **ah-esp** \| **esp** }]]

**[undo protocol**]

【缺省情况】

使用ESP安全协议。

【视图】

IPsec安全提议视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ah**]：采用AH协议对报文进行保护。

**[ah-esp**]：先用ESP协议对报文进行保护，再用AH协议对报文进行保护。

**[esp**]：采用ESP协议对报文进行保护。

【使用指导】

在IPsec隧道的两端，IPsec安全[提议所采用的安全协议必须一致。]

【举例】

\# 配置IPsec安全提议采用AH协议。

\<Sysname\> system-view

Sysname ipsec transform-set tran1

Sysname-ipsec-transform-set-tran1 protocol ah

**IPsec \-- IPsec配置命令 \-- qos pre-classify**

------------------------------------------------------------------------

**[qos pre-classify**]命令用来开启QoS预分类功能。

**[undo**] **qos pre-classify**命令用来恢复缺省情况。

【命令】

**[qos pre-classify**]

**[undo**] **qos pre-classify**

【缺省情况】

QoS预分类功能处于关闭状态，即QoS使用IPsec封装后报文的外层IP头信息来对报文进行分类。

【视图】

IPsec安全策略视图/IPsec安全策略模板视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

QoS预分类功能是指，QoS基于被封装报文的原始IP头信息对报文进行分类。

【举例】

\# 在IPsec安全策略中开启QoS预分类功能。

\<Sysname\> system-view

Sysname ipsec policy policy1 100 manual

Sysname-ipsec-policy-manual-policy1-100 qos pre-classify

**IPsec \-- IPsec配置命令 \-- redundancy replay-interval**

------------------------------------------------------------------------

![说明](IPsec命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[redundancy replay-interval**]命令用来配置抗重放窗口和序号的同步间隔。

**[undo **]redundancy{.SC132527}** replay-interval**命令用来恢复缺省情况。

【命令】

redundancy{.SC132527}** replay-interval inbound ***inbound-interval*** outbound ***outbound-interval*

**[undo **]redundancy{.SC132527}** replay-interval**

【缺省情况】

同步入方向抗重放窗口的报文间隔为1000，同步出方向IPsec SA抗重放序号的报文间隔为100000。

【视图】

IPsec安全策略视图/IPsec安全策略模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[inbound ***inbound-interval*]：同步入方向IPsec SA抗重放窗口左侧值的报文间隔，取值范围为0～1000，单位为报文个数，取值为0，表示不同步防重放窗口。

**[outbound ***outbound-interval*]：同步出方向IPsec SA抗重放序号的报文间隔，取值范围为1000～100000，单位为报文个数。

【使用指导】

IPsec冗余备份功能处于开启状态时，抗重放序号同步间隔的配置才会生效。

调小同步的报文间隔，可以增加主备间保持抗重放窗口和序号一致的精度，但同时对转发性能会有一定影响。

【举例】

\# 配置同步入方向抗重放窗口的报文间隔为800，同步出方向抗重放序号的报文间隔为50000。

\<Sysname\> system-view

Sysname ipsec policy test 1

sysname-ipsec-policy-test-1****redundancy relay-interval inbound 800 outbound 50000

【相关命令】

·**ipsec anti-replay check**

·**ipsec anti-replay window**

·**ipsec redundancy enable**

**IPsec \-- IPsec配置命令 \-- remote-address**

------------------------------------------------------------------------

**[remote-address**]命令用来指定IPsec隧道的对端IP地址。

**[undo remote-address**]命令用来恢复缺省情况。

【命令】

**[remote-address **]{ [ **ipv6**  *host-name* \| *ipv4-address* \| **ipv6** *ipv6-address* }]

**[undo**] **remote-address** { [ **ipv6**  *host-name* \| *ipv4-address* \| **ipv6** *ipv6-address* }]

【缺省情况】

未指定IPsec隧道的对端IP地址。

【视图】

IPsec安全策略视图/IPsec安全策略模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv6**]：指定IPv6 IPsec隧道的对端地址或主机名称。如果不指定该参数，则表示指定IPv4 IPsec隧道的对端地址或主机名称。

*[hostname*]：IPsec隧道的对端主机名，为1～255个字符的字符串，不区分大小写。该主机名可被DNS服务器解析为IP地址。

*[ipv4-address*]：IPsec隧道的对端IPv4地址。

*[ipv6-address*]：IPsec隧道的对端IPv6地址。

【使用指导】

IKE协商发起方必须配置IPsec隧道的对端IP地址，对于使用IPsec安全策略模板的响应方可选配。

手工方式的IPsec安全策略不支持域名解析，因此只能指定IP地址类型的对端IP地址。

对于主机名方式的对端地址，地址更新的查询过程有所不同。

·若此处指定对端主机名由DNS服务器来解析，则本端按照DNS服务器通知的域名解析有效期，在该有效期超时之后向DNS服务器查询主机名对应的最新的IP地址。

·若此处指定对端主机名由本地配置的静态域名解析（通过**ip host**命令配置）来解析，则更改此主机名对应的IP地址之后，需要在IPsec安全策略或IPsec安全策略模板中重新配置**remote-address**，才能使得本端解析到更新后的对端IP地址。

例如，本端已经存在一条静态域名解析配置，它指定了主机名test对应的IP地址为1.1.1.1。若先后执行以下配置：

\# 在IPsec安全策略policy1中指定IPsec隧道的对端主机名为test。

Sysname ipsec policy policy1 1 isakmp

Sysname-ipsec-policy-isakmp-policy1-1 remote-address test

\# 更改主机名test对应的IP地址为2.2.2.2。

Sysname ip host test 2.2.2.2

则，需要在IPsec安全策略policy1中重新指定对端主机名，使得本端可以根据更新后的本地域名解析配置得到最新的对端IP地址2.2.2.2，否则仍会解析为原来的IP地址1.1.1.1。

\# 重新指定IPsec隧道的对端主机名为test。

Sysname ipsec policy policy1 1 isakmp

Sysname -ipsec-policy-isakmp-policy1-1 remote-address test

【举例】

\# 指定IPsec隧道的对端IPv4地址为10.1.1.2。

\<Sysname\> system-view

Sysname ipsec policy policy1 10 manual

Sysname-ipsec-policy-manual-policy1-10 remote-addresss 10.1.1.2

【相关命令】

·**ip host**（三层技术-IP业务/域名解析）

·**local-address**

**IPsec \-- IPsec配置命令 \-- reset ipsec sa**

------------------------------------------------------------------------

**[reset ipsec sa**]命令用来清除已经建立的IPsec SA。

【命令】

**[reset**[ **ipsec** **sa** [ { **ipv6-policy** \| **policy** } *policy-name* [ *seq-number* ] \| **profile** *policy-name* \| **remote** { *ipv4-address* \| **ipv6** *ipv6-address* } \| **spi** { *ipv4-address* \| **ipv6** *ipv6-address* } { **ah** \| **esp** } *spi-num* ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

[[{ **ipv6-policy** \| **policy** } *policy-name* [ *seq-number* ]]]：表示根据IPsec安全策略名称清除IPsec SA。

·**ipv6-policy**：IPv6 IPsec安全策略。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

·**policy**：IPv4 IPsec安全策略。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

·*policy-name*：IPsec安全策略的名字，为1～63个字符的字符串，不区分大小写。

·*seq-number*：IPsec安全策略表项的顺序号，取值范围为1～65535。如果不指定该参数，则表示指定名字为*policy-name*的安全策略中所有安全策略表项。

**[profile*** profile-name*]：表示根据IPsec安全框架名称清除IPsec SA。*profile-name*表示IPsec安全框架的名字，为1～63个字符的字符串，不区分大小写。

**[remote**]：表示根据对端IP地址清除IPsec SA。

·*ipv4-address*：对端的IPv4地址。

·**ipv6*** ipv6-address*：对端的IPv6地址。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[spi **[{ *ipv4-address* \| **ipv6** *ipv6-address* } { **ah** \| **esp** } *spi-num*]]：表示根据SA的三元组信息（对端IP地址、安全协议、安全参数索引）清除IPsec SA。

·*ipv4-address*：对端的IPv4地址。

·**ipv6*** ipv6-address*：对端的IPv6地址。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

·**ah**：AH协议。

·**esp**：ESP协议。

·*spi-num*：安全参数索引，取值范围为256～4294967295。

【使用指导】

如果不指定任何参数，则清除所有的IPsec SA。

如果指定了一个IPsec SA的三元组信息，则将清除符合该三元组的某一个方向的IPsec SA以及对应的另外一个方向的IPsec SA。若是同时采用了两种安全协议，则还会清除另外一个协议的出方向和入方向的IPsec SA。

对于出方向IPsec SA，三元组是它的唯一标识；对于入方向IPsec SA，SPI是它的唯一标识。因此，若是希望通过指定出方向的三元组信息来清除IPsec SA，则需要准确指定三元组信息（其中，IPsec安全框架生成的SA由于没有地址信息，所以地址信息可以任意）；若是希望通过指定入方向的三元组信息来清除IPsec SA，则只需要准确指定SPI值即可，另外两个信息可以任意。

通过手工建立的IPsec SA被清除后，系统会立即根据对应的手工IPsec安全策略建立新的IPsec SA。

通过IKE协商建立的IPsec SA被清除后，系统会在有报文需要进行IPsec保护时触发协商新的IPsec SA。

【举例】

\# 清除所有IPsec SA。

\<Sysname\> reset ipsec sa

\# 清除SPI为123、对端地址为10.1.1.2、安全协议为AH的出方向和入方向的IPsec SA。

\<Sysname\> reset ipsec sa spi 10.1.1.2 ah 123

\# 清除IPsec对端地址为10.1.1.2的所有IPsec SA。

\<Sysname\> reset ipsec sa remote 10.1.1.2

\# 清除IPsec安全策略名字为policy1、顺序号为10的所有IPsec SA。

\<Sysname\> reset ipsec sa policy policy1 10

\# 清除IPsec安全策略policy1中的所有IPsec SA。

\<Sysname\> reset ipsec sa policy policy1

【相关命令】

·**display ipsec sa**

**IPsec \-- IPsec配置命令 \-- reset ipsec statistics**

------------------------------------------------------------------------

**[reset** **ipsec** **statistics**]命令用来清除IPsec的报文统计信息。

【命令】

**[reset ipsec statistics ** **tunnel-id** *tunnel-id*]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[tunnel-id ***tunnel-id*]：清除指定IPsec隧道的报文统计信息。其中，*tunnel-id*为隧道的ID号，取值范围与设备的型号有关，请以设备的实际情况为准。如果未指定任何参数，则清除IPsec的所有报文统计信息。

【举例】

\# 清除IPsec的所有报文统计信息。

\<Sysname\> reset ipsec statistics

【相关命令】

·**display ipsec statistics**

**IPsec \-- IPsec配置命令 \-- reverse-route dynamic**

------------------------------------------------------------------------

**[reverse-route dynamic**]命令用来开启IPsec反向路由注入功能。

**[undo reverse-route dynamic**]命令用来关闭IPsec反向路由注入功能。

【命令】

**[reverse-route** **dynamic**]

**[undo reverse-route** **dynamic**]

【缺省情况】

IPsec反向路由注入功能处于关闭状态。

【视图】

IPsec安全策略视图/IPsec安全策略模板视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在企业中心侧网关设备上的某安全策略视图/安全策略模板视图下开启IPsec反向路由注入功能后，设备会根据协商的IPsec SA自动生成一条静态路由，该路由的目的地址为受保护的对端私网，下一跳地址为IPsec隧道的对端地址。

需要注意的是：

l开启反向路由注入功能时，会删除本策略协商出的所有IPsec SA。当有新的流量触发生成IPsec SA时，根据新协商的IPsec生成路由信息。

l关闭反向路由注入功能时，会删除本策略协商出的所有IPsec SA。

l生成的静态路由随IPsec SA的创建而创建，随IPsec SA的删除而删除。

l需要查看生成的路由信息时，可以通过**display ip routing-table**命令查看。

【举例】

\# 开启IPsec反向路由注入功能，根据协商成功的IPsec SA动态生成静态路由，目的地址为受保护的对端私网网段3.0.0.0/24，下一跳地址为对端隧道地址1.1.1.2。

\<Sysname\> system-view

Sysname ipsec policy 1 1 isakmp

Sysname-ipsec-policy-isakmp-1-1 reverse-route dynamic

Sysname-ipsec-policy-isakmp-1-1 quit

\# 隧道两端的IPsec SA协商成功后，可查看到生成如下静态路由（其它显示信息略）。

Sysname display ip routing-table

\...

Destination/Mask    Proto  Pre  Cost         NextHop         Interface

3.0.0.0/24          Static 60   0            1.1.1.2         Eth1/1

【相关命令】

l**display ip routing-table**（三层技术-IP路由命令参考/IP路由基础）

l**ipsec policy**

·**ipsec policy-template**

**IPsec \-- IPsec配置命令 \-- reverse-route preference**

------------------------------------------------------------------------

**[reverse-route preference**]命令用来设置IPsec反向路由注入功能生成的静态路由的优先级。

**[undo reverse-route preference**]命令用来恢复缺省情况。

【命令】

**[reverse-route preference** *number*]

**[undo reverse-route preference**]

【缺省情况】

IPsec反向路由注入功能生成的静态路由的优先级为60。

【视图】

IPsec安全策略视图/IPsec安全策略模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：静态路由的优先级，取值范围为1～255。该值越小，优先级越高。

【使用指导】

若对静态路由优先级进行修改，会删除本策略协商生成的所有IPsec SA和根据这些IPsec SA生成的静态路由。

【举例】

\# 配置IPsec反向路由注入功能生成的静态路由的优先级为100。

\<Sysname\> system-view

Sysname ipsec policy 1 1 isakmp

Sysname-ipsec-policy-isakmp-1-1 reverse-route preference 100

【相关命令】

l**ipsec policy**

·**ipsec policy-template**

**IPsec \-- IPsec配置命令 \-- reverse-route tag**

------------------------------------------------------------------------

**[reverse-route tag**]命令用来设置IPsec反向路由注入功能生成的静态路由的Tag值，该值用于标识静态路由，以便在路由策略中根据Tag值对路由进行灵活的控制。

**[undo reverse-route tag**]命令用来恢复缺省情况。

【命令】

**[reverse-route tag ***tag-value*]

**[undo reverse-route tag**]

【缺省情况】

IPsec反向路由注入功能生成的静态路由的Tag值为0。

【视图】

IPsec安全策略视图/IPsec安全策略模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[tag-value*]：静态路由的Tag值，取值范围为1～4294967295。

【使用指导】

若对静态路由Tag值进行修改，则会删除本策略协商生成的所有IPsec SA和根据这些IPsec SA生成的静态路由。

【举例】

\# 配置IPsec反向路由注入功能生成的静态路由的Tag值为50。

\<Sysname\>system-view

Sysname ipsec policy 1 1 isakmp

Sysname-ipsec-policy-isakmp-1-1 reverse-route tag 50

【相关命令】

l**ipsec policy**

·**ipsec policy-template**

**IPsec \-- IPsec配置命令 \-- sa duration**

------------------------------------------------------------------------

**[sa** **duration**]命令用来配置IPsec SA的生存时间。

**[undo** **sa** **duration**]命令用来删除配置的IPsec SA生存时间。

【命令】

**[sa duration** { **time-based** *seconds* \| **traffic-based** *kilobytes* }]

**[undo sa duration**[ { **time-based** \| **traffic-based** }]]

【缺省情况】

IPsec安全策略和IPsec安全策略模板的IPsec SA生存时间均为当前全局的IPsec SA生存时间。

【视图】

IPsec安全策略视图/IPsec安全策略模板视图/IPsec安全框架视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[time-based*** seconds*]：指定基于时间的生存时间，取值范围为180～604800，单位为秒。

**[traffic-based*** kilobytes*]：指定基于流量的生存时间，取值范围为2560～4294967295，单位为千字节。

【使用指导】

当IKE协商IPsec SA时，如果采用的IPsec安全策略下未配置IPsec SA的生存时间，将采用全局的IPsec SA生存时间（通过命令**ipsec sa global-duration**设置）与对端协商。如果IPsec安全策略/IPsec安全策略模板下配置了IPsec SA的生存时间，则优先使用IPsec安全策略/IPsec安全策略模板下的配置值与对端协商。

IKE为IPsec协商建立IPsec SA时，采用本地配置的生存时间和对端提议的IPsec SA生存时间中较小的一个。

【举例】

\# 配置IPsec安全策略policy1的IPsec SA生存时间为两个小时，即7200秒。

\<Sysname\> system-view

Sysname ipsec policy policy1 100 isakmp

Sysname-ipsec-policy-isakmp-policy1-100 sa duration time-based 7200

\# 配置IPsec安全策略policy1的IPsec SA生存时间为20M字节，即传输20480千字节的流量后，当前的IPsec SA就过期。

\<Sysname\> system-view

Sysname ipsec policy policy1 100 isakmp

Sysname-ipsec-policy-isakmp-policy1-100 sa duration traffic-based 20480

【相关命令】

·**display ipsec sa**

·**ipsec sa global-duration**

**IPsec \-- IPsec配置命令 \-- sa hex-key authentication**

------------------------------------------------------------------------

**[sa hex-key authentication**]命令用来为手工创建的IPsec SA配置十六进制形式的认证密钥。

**[undo sa hex-key authentication**]命令用来删除为IPsec SA配置的十六进制形式的认证密钥。

【命令】

**[sa hex-key**[ **authentication** { **inbound** \| **outbound** } { **ah** \| **esp** } { **cipher** \| **simple** } *key-value*]]

**[undo sa hex-key**[ **authentication** { **inbound** \| **outbound** } { **ah** \| **esp** }]]

【缺省情况】

未配置IPsec SA使用的认证密钥。

【视图】

IPsec安全策略视图/IPsec安全框架视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[inbound**]：指定入方向IPsec SA使用的认证密钥。

**[outbound**]：指定出方向IPsec SA使用的认证密钥。

**[ah**]：指定AH协议。

**[esp**]：指定ESP协议。

**[cipher ***key-value*]：表示以密文形式设置认证密钥。*key-value*为1～85个字符的字符串，区分大小写。

**[simple ***key-value*]：表示以明文形式设置认证密钥。*key-value*为十六进制格式的字符串，不区分大小写。对于不同的算法，密钥长度不同：HMAC-MD5算法，密钥长度为16个字节；HMAC-SHA1算法，密钥长度为20个字节。

【使用指导】

此命令仅用于手工方式的IPsec安全策略及IPsec安全框架。

·必须分别配置**inbound**和**outbound**两个方向的IPsec SA参数。

·在IPsec隧道的两端设置的IPsec SA参数必须是完全匹配的。本端的入方向IPsec SA的认证密钥必须和对端的出方向IPsec SA的认证密钥一致；本端的出方向IPsec SA的认证密钥必须和对端的入方向IPsec SA的认证密钥一致。

·对于要应用于IPv6路由协议的IPsec安全框架，还必须保证本端出方向SA的密钥和本端入方向SA的密钥一致。

·如果先后以不同的方式输入了密钥，则最后设定的密钥有效。

·在IPsec隧道的两端，应当以相同的方式输入密钥。如果一端以字符串方式输入密钥，另一端以十六进制方式输入密钥，则不能建立IPsec隧道。

·以明文或密文方式设置的认证密钥，均以密文的方式保存在配置文件中。

【举例】

\# 配置采用AH协议的入方向IPsec SA的认证密钥为明文0x112233445566778899aabbccddeeff00；出方向IPsec SA的认证密钥为明文0xaabbccddeeff001100aabbccddeeff00。

\<Sysname\> system-view

Sysname ipsec policy policy1 100 manual

Sysname-ipsec-policy-manual-policy1-100 sa hex-key authentication inbound ah simple 112233445566778899aabbccddeeff00

Sysname-ipsec-policy-manual-policy1-100 sa hex-key authentication outbound ah simple aabbccddeeff001100aabbccddeeff00

【相关命令】

·**display ipsec sa**

·**sa string-key**

**IPsec \-- IPsec配置命令 \-- sa hex-key encryption**

------------------------------------------------------------------------

**[sa hex-key encryption**]命令用来为手工创建的IPsec SA配置十六进制形式的加密密钥。

**[undo sa hex-key encryption**]命令用来删除为IPsec SA配置的十六进制形式的加密密钥。

【命令】

**[sa hex-key encryption**[ { **inbound** \| **outbound** } **esp** { **cipher** \| **simple** } *key-value*]]

**[undo sa hex-key  encryption**[ { **inbound** \| **outbound** } **esp**]]

【缺省情况】

未配置IPsec SA使用的加密密钥。

【视图】

IPsec安全策略视图/IPsec安全框架视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[inbound**]：指定入方向IPsec SA使用的加密密钥。

**[outbound**]：指定出方向IPsec SA使用的加密密钥。

**[esp**]：指定ESP协议。

**[cipher ***key-value*]：表示以密文形式设置加密密钥。*key-value*为1～117个字符的字符串，区分大小写。

**[simple ***key-value*]：表示以明文形式设置加密密钥。*key-value*为16进制格式的字符串，不区分大小写。对于不同的算法，密钥长度不同：DES-CBC算法，密钥长度为8个字节；3DES-CBC算法，密钥长度为24个字节；AES128-CBC算法，密钥长度为16字节；AES192-CBC算法，密钥长度为24字节；AES256-CBC算法，密钥长度为32字节。

【使用指导】

此命令仅用于手工方式的IPsec安全策略及IPsec安全框架。

·必须分别配置**inbound**和**outbound**两个方向的IPsec SA参数。

·在IPsec隧道的两端设置的IPsec SA参数必须是完全匹配的。本端的入方向IPsec SA的加密密钥必须和对端的出方向IPsec SA的加密密钥一致；本端的出方向IPsec SA的加密密钥必须和对端的入方向IPsec SA的加密密钥一致。

·对于要应用于IPv6路由协议的IPsec安全框架，还必须保证本端出方向SA的密钥和本端入方向SA的密钥一致。

·如果先后以不同的方式输入了密钥，则最后设定的密钥有效。

·在IPsec隧道的两端，应当以相同的方式输入密钥。如果一端以字符串方式输入密钥，另一端以十六进制方式输入密钥，则不能建立IPsec隧道。

·以明文或密文方式设置的加密密钥，均以密文的方式保存在配置文件中。

【举例】

\# 配置采用ESP协议的入方向IPsec SA的加密算法的密钥为明文0x1234567890abcdef；出方向IPsec SA的加密算法的密钥为明文0xabcdefabcdef1234。

\<Sysname\> system-view

Sysname ipsec policy policy1 100 manual

Sysname-ipsec-policy-manual-policy1-100 sa hex-key encryption inbound esp simple 1234567890abcdef

Sysname-ipsec-policy-manual-policy1-100 sa hex-key encryption outbound esp simple abcdefabcdef1234

【相关命令】

·**display ipsec sa**

·**sa string-key**

**IPsec \-- IPsec配置命令 \-- sa idle-time**

------------------------------------------------------------------------

**[sa idle-time**]命令用来配置IPsec SA的空闲超时时间。在指定的超时时间内，没有流量使用的IPsec SA将被删除。

**[undo sa idle-time**]命令用来恢复缺省情况。

【命令】

**[sa idle-time** *seconds*]

**[undo sa idle-time**]

【缺省情况】

IPsec安全策略和IPsec安全策略模板下的IPsec SA空闲超时时间为当前全局的IPsec SA空闲超时时间。

【视图】

IPsec安全策略视图/IPsec安全策略模板视图/IPsec安全框架视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：IPsec SA的空闲超时时间，取值范围为60～86400，单位为秒。

【使用指导】

此功能只适用于IKE协商出的IPsec SA，且只有通过**ipsec sa idle-time**命令开启空闲超时功能后，本功能才会生效。

如果IPsec安全策略/IPsec安全策略模板/IPsec安全框架视图下没有配置IPsec SA 空闲超时时间，将采用全局的IPsec SA空闲超时时间（通过命令**ipsec sa idle-time**设置）决定IPsec SA是否空闲并进行删除。如果IPsec安全策略/IPsec安全策略模板/IPsec安全框架视图下配置了IPsec SA 空闲超时时间，则优先使用IPsec安全策略/IPsec安全策略模板/IPsec安全框架视图下的配置值。

【举例】

\# 配置IPsec安全策略的IPsec SA的空闲超时时间为600秒。

\<Sysname\> system-view

Sysname ipsec policy map 100 isakmp

Sysname-ipsec-policy-isakmp-map-100 sa idle-time 600

【相关命令】

·**display ipsec sa**

·**ipsec sa idle-time**

**IPsec \-- IPsec配置命令 \-- sa spi**

------------------------------------------------------------------------

**[sa** **spi**]命令用来配置IPsec SA的SPI。

**[undo** **sa** **spi**]命令用来删除指定的IPsec SA的SPI。

【命令】

**[sa**[ **spi** { **inbound** \| **outbound** } { **ah** \| **esp** } *spi-number*]]

**[undo sa spi**[ { **inbound** \| **outbound** } { **ah** \| **esp** }]]

【缺省情况】

不存在IPsec SA的SPI。

【视图】

IPsec安全策略视图/IPsec安全框架视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[inbound**]：指定入方向IPsec SA的SPI。

**[outbound**]：指定出方向IPsec SA的SPI。

**[ah**]：指定AH协议。

**[esp**]：指定ESP协议。

*[spi-number*]：IPsec SA的安全参数索引，取值范围为256～4294967295。

【使用指导】

此命令仅用于手工方式的IPsec安全策略以及IPsec安全框架。对于IKE协商方式的IPsec安全策略，IKE将自动协商IPsec SA的参数并创建IPsec SA，不需要手工设置IPsec SA的参数。

·必须分别配置**inbound**和**outbound**两个方向IPsec SA的参数，且保证每一个方向上的IPsec SA的唯一性：对于出方向IPsec SA，必须保证三元组（对端IP地址、安全协议、SPI）唯一；对于入方向IPsec SA，必须保证SPI唯一。

·在IPsec隧道的两端设置的IPsec SA参数必须是完全匹配的。本端的入方向IPsec SA的SPI必须和对端的出方向IPsec SA的SPI一样；本端的出方向IPsec SA的SPI必须和对端的入方向IPsec SA的SPI一样。

在配置应用于IPv6路由协议的IPsec安全框架时，还需要注意的是：

·本端出方向IPsec SA的SPI必须和本端入方向IPsec SA的SPI保持一致；

·同一个范围内的、所有设备上的IPsec SA的SPI均要保持一致。该范围与协议相关：对于OSPF，是OSPF邻居之间或邻居所在的区域；对于RIPng，是RIPng直连邻居之间或邻居所在的进程；对于BGP，是BGP邻居之间或邻居所在的一个组。

【举例】

\# 配置入方向IPsec SA的SPI为10000，出方向IPsec SA的SPI为20000。

\<Sysname\> system-view

Sysname ipsec policy policy1 100 manual

Sysname-ipsec-policy-manual-policy1-100 sa spi inbound ah 10000

Sysname-ipsec-policy-manual-policy1-100 sa spi outbound ah 20000

【相关命令】

·**display ipsec sa**

**IPsec \-- IPsec配置命令 \-- sa string-key**

------------------------------------------------------------------------

**[sa** **string-key**]命令用来为手工创建的IPsec SA配置字符串形式的密钥。

**[undo** **sa** **string-key**]命令用来删除为指定的IPsec SA配置的字符串形式的密钥。

【命令】

**[sa string-key**[ { **inbound** \| **outbound** } { **ah** \| **esp** } { **cipher** \| **simple** } *key-value*]]

**[undo sa string-key**[ { **inbound** \| **outbound** } { **ah** \| **esp** }]]

【缺省情况】

未配置IPsec SA使用的密钥。

【视图】

IPsec安全策略视图/IPsec安全框架视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[inbound**]：指定入方向IPsec SA的密钥。

**[outbound**]：指定出方向IPsec SA的密钥。

**[ah**]：指定AH协议。

**[esp**]：指定ESP协议。

**[cipher**]：表示以密文形式设置密码。

**[simple**]：表示以明文形式设置密码。

*[key-value*]：设置的明文密钥或密文密钥，区分大小写。明文密钥为1～255个字符的字符串；密文密钥为1～373个字符的字符串。对于不同的算法，系统会根据输入的字符串自动生成符合算法要求的密钥。对于ESP协议，系统会自动地同时生成认证算法的密钥和加密算法的密钥。

【使用指导】

此命令仅用于手工方式的IPsec安全策略及IPsec安全框架。

·必须分别配置**inbound**和**outbound**两个方向IPsec SA的参数。

·在IPsec隧道的两端设置的IPsec SA参数必须是完全匹配的。本端入方向IPsec SA的密钥必须和对端出方向IPsec SA的密钥一样；本端出方向IPsec SA的密钥必须和对端入方向IPsec SA的密钥一样。

·如果先后以不同的方式输入了密钥，则最后设定的密钥有效。

·在IPsec隧道的两端，应当以相同的方式输入密钥。如果一端以字符串方式输入密钥，另一端以十六进制方式输入密钥，则不能正确地建立IPsec隧道。

·以明文或密文方式设置的密钥，均以密文的方式保存在配置文件中。

在配置应用于IPv6路由协议的IPsec安全框架时，还需要注意的是：

·本端出方向IPsec SA的密钥必须和本端入方向IPsec SA的密钥保持一致；

·同一个范围内的，所有设备上的IPsec SA的密钥均要保持一致。该范围内容与协议相关：对于OSPF，是OSPF邻居之间或邻居所在的区域；对于RIPng，是RIPng直连邻居之间或邻居所在的进程；对于BGP，是BGP邻居之间或邻居所在的一个组。

【举例】

\# 配置采用AH协议的入方向IPsec SA的密钥为明文字符串abcdef；出方向IPsec SA的密钥为明文字符串efcdab。

\<Sysname\> system-view

Sysname ipsec policy policy1 100 manual

Sysname-ipsec-policy-manual-policy1-100 sa string-key inbound ah simple abcdef

Sysname-ipsec-policy-manual-policy1-100 sa string-key outbound ah simple efcdab

\# 在要应用于IPv6路由协议的安全策略中，配置采用AH协议的入方向IPsec SA的密钥为明文字符串abcdef；出方向IPsec SA的密钥为明文字符串abcdef。

\<Sysname\> system-view

Sysname ipsec policy policy1 100 manual

Sysname-ipsec-policy-manual-policy1-100 sa string-key inbound ah simple abcdef

Sysname-ipsec-policy-manual-policy1-100 sa string-key outbound ah simple abcdef

【相关命令】

·**display ipsec sa**

·**sa ****hex-key**

**IPsec \-- IPsec配置命令 \-- security acl**

------------------------------------------------------------------------

**[security** **acl**]命令用来指定IPsec安全策略/IPsec安全策略模板引用的ACL。

**[undo** **security** **acl**]命令用来取消IPsec安全策略/IPsec安全策略模板引用的ACL。

【命令】

**[security** **acl** [ **ipv6**  { *acl-number* \| **name** *acl-name* } [ **aggregation** \| **per-host** ]]]

**[undo security acl**]

【缺省情况】

IPsec安全策略/IPsec安全策略模板没有引用任何ACL。

【视图】

IPsec安全策略视图/IPsec安全策略模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv6**]：指定IPv6 ACL。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[acl-number*]：ACL编号，取值范围为3000～3999。

**[name ***acl-name*]：ACL名称，为1～63个字符的字符串，不区分大小写。

**[aggregation**]：指定IPsec安全策略的数据流保护方式为聚合方式。不支持对IPv6数据流采用该保护方式。

**[per-host**]：指定IPsec安全策略的数据流保护方式为主机方式。

【使用指导】

对于IKE协商方式的IPsec安全策略，数据流的保护方式包括以下几种：

·标准方式：一条隧道保护一条数据流。ACL中的每一个规则对应的数据流都会由一条单独创建的隧道来保护。不指定**aggregation**和**per-host**参数的情况下，缺省采用此方式。

·聚合方式：一条隧道保护ACL中定义的所有数据流。ACL中的所有规则对应的数据流只会由一条创建的隧道来保护。对于聚合方式和标准方式都支持的设备，聚合方式仅用于和老版本的设备互通。

·主机方式：一条隧道保护一条主机到主机的数据流。ACL中的每一个规则对应的不同主机之间的数据流，都会由一条单独创建的隧道来保护。这种方式下，受保护的网段之间存在多条数据流的情况下，将会消耗更多的系统资源。

需要注意的是：

·手工方式的IPsec安全策略缺省使用聚合方式，且仅支持聚合方式；

·IKE协商方式的IPsec安全策略中可以通过配置来选择不同的保护方式。

【举例】

\# 配置IPsec安全策略引用IPv4高级ACL 3001。

\<Sysname\> system-view

Sysname acl advanced 3001

Sysname-acl-ipv4-adv-3001 rule permit tcp source 10.1.1.0 0.0.0.255 destination 10.1.2.0 0.0.0.255

Sysname-acl-ipv4-adv-3001 quit

Sysname ipsec policy policy1 100 manual

Sysname-ipsec-policy-manual-policy1-100 security acl 3001

\# 配置IPsec安全策略引用IPv4高级ACL 3002，并设置数据流保护方式为聚合方式。

\<Sysname\> system-view

Sysname acl advanced 3002

Sysname-acl-ipv4-adv-3002 rule 0 permit ip source 10.1.2.1 0.0.0.255 destination 10.1.2.2 0.0.0.255

Sysname-acl-ipv4-adv-3002 rule 1 permit ip source 10.1.3.1 0.0.0.255 destination 10.1.3.2 0.0.0.255

Sysname ipsec policy policy2 1 isakmp

Sysname-ipsec-policy-isakmp-policy2-1 security acl 3002 aggregation

【相关命令】

·**display ipsec sa**

·**display ipsec tunnel**

**IPsec \-- IPsec配置命令 \-- snmp-agent trap enable ipsec**

------------------------------------------------------------------------

**[snmp-agent  trap enable ipsec**]命令用来开启IPsec告警功能。

**[undo snmp-agent** **trap** **enable** **ipsec**]命令用来关闭指定的IPsec告警功能。

【命令】

**[snmp-agent**[ **trap** **enable** **ipsec** [ **auth-failure** \| **decrypt-failure** \| **encrypt-failure** \| **global** \| **invalid-sa-failure** \| **no-sa-failure** \| **policy-add** \| **policy-attach** \| **policy-delete** \| **policy-detach tunnel-start** \| **tunnel-stop**] \*]]

**[undo snmp-agent**[ **trap** **enable** **ipsec** [ **auth-failure** \| **decrypt-failure** \| **encrypt-failure** \| **global** \| **invalid-sa-failure** \| **no-sa-failure** \| **policy-add** \| **policy-attach** \| **policy-delete** \| **policy-detach tunnel-start** \| **tunnel-stop**] \*]]

【缺省情况】

IPsec的所有告警功能均处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[auth-failure**]：表示认证失败时的告警功能。

**[decrypt-failure**]：表示解密失败时的告警功能。

**[encrypt-failure**]：表示加密失败时的告警功能。

**[global**]**：**表示全局告警功能。

**[invalid-sa-failure**]：表示无效SA的告警功能。

**[no-sa-failure**]：表示无法查找到SA时的告警功能。

**[policy-add**]：表示添加IPsec安全策略时的告警功能。

**[policy-attach**]：表示将IPsec安全策略应用到接口时的告警功能。

**[policy-delete**]：表示删除IPsec安全策略时的告警功能。

**[policy-detach**]：表示将IPsec 安全策略从接口下删除时的告警功能。

**[tunnel-start**]：表示创建IPsec隧道时的告警功能。

**[tunnel-stop**]：表示删除IPsec隧道时的告警功能。

【使用指导】

如果不指定任何参数，则表示开启或关闭所有类型的IPsec 告警功能。

如果希望生成并输出某种类型的IPsec告警信息，则需要保证IPsec的全局告警功能以及相应类型的告警功能均处于开启状态。

【举例】

希望设备在创建IPsec隧道时生成并发送告警信息，需要开启以下告警功能：

\# 开启全局IPsec Trap告警。

\<Sysname\> system-view

Sysname snmp-agent trap enable ipsec global

\# 开启创建IPsec隧道时的告警功能。

Sysname snmp-agent trap enable ipsec tunnel-start

**IPsec \-- IPsec配置命令 \-- transform-set**

------------------------------------------------------------------------

**[transform-set**]命令用来指定IPsec安全策略/IPsec安全策略模板/IPsec安全框架所引用的IPsec安全提议。

**[undo transform-set**]命令用来取消IPsec安全策略/IPsec安全策略模板/IPsec安全框架引用的IPsec安全提议。

【命令】

**[transform-set ***transform-set-name*&\<1-6\>]

**[undo** **transform-set** [ *transform-set-name* ]]

【缺省情况】

IPsec安全策略/IPsec安全策略模板/IPsec安全框架没有引用任何IPsec安全提议。

【视图】

IPsec安全策略视图/IPsec安全策略模板视图/IPsec安全框架视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[transform-set-name*&\<1-6\>]：IPsec安全提议的名字，为1～63个字符的字符串，不区分大小写。&\<1-6\>表示前面的参数最多可以输入6次。

【使用指导】

·对于手工方式的IPsec安全策略，只能引用一个IPsec安全提议。改变IPsec安全策略引用的IPsec安全提议时，新配置的IPsec安全提议将覆盖旧的IPsec安全提议。

·对于IKE协商方式的IPsec安全策略，一条IPsec安全策略最多可以引用六个IPsec安全提议。IKE协商过程中，IKE将会在隧道两端配置的IPsec安全策略中查找能够完全匹配的IPsec安全提议。如果IKE在两端找不到完全匹配的IPsec安全提议，则SA不能协商成功，需要被保护的报文将被丢弃。

·若不指定任何参数，则**undo transform-set**命令表示删除所有引用的IPsec安全提议。

【举例】

\# 配置IPsec安全策略引用名字为prop1的IPsec安全提议。

\<Sysname\> system-view

Sysname ipsec transform-set prop1

Sysname-ipsec-transform-set-prop1 quit

Sysname ipsec policy policy1 100 manual

Sysname-ipsec-policy-manual-policy1-100 transform-set prop1

【相关命令】

[·**ipsec **[{ **ipv6-policy** \| **policy** }]]

·**ipsec profile**

·**ipsec transform-set**

**IPsec \-- IPsec配置命令 \-- tunnel protection ipsec**

------------------------------------------------------------------------

**[tunnel protection ipsec**]命令用来在隧道接口上应用IPsec安全框架。

**[undo tunnel protection ipsec**]命令用来删除指定的IPsec安全框架的应用。

【命令】

**[tunnel protection ipsec profile ***profile-name*]

**[undo tunnel protection ipsec profile**]

【缺省情况】

Tunnel接口下没有引用任何的IPsec安全框架。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[profile ***profile-name*]：指定使用的IPsec安全框架，且必须为IKE协商方式的IPsec安全框架。其中，*profile-name*为IPsec安全框架的名字，为1～63个字符的字符串，不区分大小写。

【使用指导】

在隧道接口上应用IPsec安全框架后，隧道两端会通过IKE协商建立IPsec隧道对隧道接口上传输的数据流进行IPsec保护。目前，仅支持对ADVPN隧道报文进行IPsec保护。

【举例】

\# 配置使用IPsec安全框架prf1来保护接口Tunnel1的报文。

\<Sysname\> system-view

Sysname interface tunnel 1 mode advpn gre

Sysname-Tunnel1 tunnel protection ipsec profile prf1

【相关命令】

l**interface tunnel**（IP业务命令参考/隧道）

l**display interface tunnel**（IP业务命令参考/隧道）

·**ipsec profile**

\

**IKE \-- IKE配置命令 \-- authentication-algorithm**

------------------------------------------------------------------------

**[authentication-algorithm**]命令用来指定一个供IKE提议使用的认证算法。

**[undo authentication-algorithm**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[authentication-algorithm**[ { **md5** \| **sha** }]]

**[undo** **authentication-algorithm**]

FIPS模式下：

**[authentication-algorithm ** **sha**]

**[undo** **authentication-algorithm**]

【缺省情况】

IKE提议使用的认证算法为HMAC-SHA1。

【视图】

IKE提议视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[md5**]：指定认证算法为HMAC-MD5。

**[sha**]：指定认证算法为HMAC-SHA1。

【举例】

\# 指定IKE提议1的认证算法为HMAC-SHA1。

\<Sysname\> system-view

Sysname ike proposal 1

Sysname-ike-proposal-1 authentication-algorithm sha

【相关命令】

·**display ike proposal**

**IKE \-- IKE配置命令 \-- authentication-method**

------------------------------------------------------------------------

**[authentication-method**]命令用来指定一个供IKE提议使用的认证方法。

**[undo authentication-method**]命令用来恢复缺省情况。

【命令】

**[authentication-method**[ { **dsa-signature** \| **pre-share** \| **rsa-signature** }]]

**[undo authentication-method**]

【缺省情况】

IKE提议使用预共享密钥的认证方法。

【视图】

IKE提议视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[dsa-signature**]：指定认证方法为DSA数字签名方法。

**[pre-share**]：指定认证方法为预共享密钥方法。

**[rsa-signature**]：指定认证方法为RSA数字签名方法。

【使用指导】

认证方法分为预共享密钥认证和数字签名认证（包括RSA数字签名认证和DSA数字签名认证）。预共享密钥认证机制简单、不需要证书，常在小型组网环境中使用；数字签名认证安全性更高，常在"中心---分支"模式的组网环境中使用。例如，在"中心---分支"组网中使用预共享密钥认证进行IKE协商时，中心侧可能需要为每个分支配置一个预共享密钥，当分支很多时，配置会很复杂，而使用数字签名认证时中心只需配置一个PKI域。

需要注意的是：

·协商双方必须有匹配的认证方法。

·如果指定认证方法为RSA数字签名方法或者DSA数字签名方法，则还必须保证对端从CA（证书认证机构）获得数字证书。

·如果指定认证方法为预共享密钥方法，必须使用**pre-shared-key**命令在两端配置相同的预共享密钥。

【举例】

\# 指定IKE提议1的认证方法为预共享密钥。

\<Sysname\> system-view

Sysname ike proposal 1

Sysname-ike-proposal-1 authentication-method pre-share

【相关命令】

l**display ike proposal**

l**ike keychain**

l**pre-shared-key**

**IKE \-- IKE配置命令 \-- certificate domain**

------------------------------------------------------------------------

**[certificate domain**]命令用来指定IKE协商采用数字签名认证时使用的PKI域。

**[undo certificate domain**]命令用来取消配置IKE协商时使用的PKI域。

【命令】

**[certificate domain ***domain-name*]

**[undo certificate domain ***domain-name*]

【缺省情况】

未指定用于IKE协商的PKI域。

【视图】

IKE profile视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[domain-name*]：PKI域的名称，为1～31个字符的字符串，不区分大小写。

【使用指导】

可通过多次执行本命令指定多个PKI域。如果在IKE profile中指定了PKI域，则使用指定的PKI域发送本端证书请求、验证对端证书请求、发送本端证书、验证对端证书、进行数字签名。如果IKE profile中没有指定PKI域，则使用设备上配置的PKI域进行以上证书相关的操作。

一个IKE profile中最多可以引用六个PKI域。

IKE可以通过PKI自动获取CA证书、自动申请证书，对这种情况，有几点需要说明：

·对于发起方：若在IKE profile中指定了PKI域，且PKI域中的证书申请为自动申请方式，则发起方会自动获取CA证书；若在IKE profile中没有指定PKI域，则发起方不会自动获取CA证书，需要手动获取CA证书。

·对于响应方：第一阶段采用主模式的IKE协商时，响应方不会自动获取CA证书，需要手动获取CA证书；第一阶段采用野蛮模式的IKE协商时，若响应方找到了匹配的IKE profile并且IKE profile下指定了PKI域，且PKI域中的证书申请为自动申请方式，则会自动获取CA证书；否则，响应方不会自动获取CA证书，需要手动获取CA证书。

·在IKE协商过程中先自动获取CA证书，再自动申请证书。若CA证书存在，则不获取CA证书，直接自动申请证书。

【举例】

\# 在IKE profile 1中指定IKE协商时使用的PKI域。

\<Sysname\> system-view

Sysname ike profile 1

Sysname-ike-profile-1 certificate domain abc

【相关命令】

l**authentication-method**

·**pki domain**（安全命令参考/PKI）

**IKE \-- IKE配置命令 \-- dh**

------------------------------------------------------------------------

**[dh**]命令用来配置IKE阶段1密钥协商时所使用的DH密钥交换参数。

**[undo** **dh**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[dh **[{ **group1** \| **group14** \| **group2** \| **group24** \| **group5** }]]

**[undo dh**]

FIPS模式下：

**[dh group14**]

**[undo dh**]

【缺省情况】

非FIPS模式下：

IKE提议使用的DH密钥交换参数为**group1**，即768-bit的Diffie-Hellman group。

FIPS模式下：

IKE提议使用的DH密钥交换参数为**group14**，即2048-bit的Diffie-Hellman group。

【视图】

IKE提议视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[group1**]：指定阶段1密钥协商时采用768-bit的Diffie-Hellman group。

**[group14**]：指定阶段1密钥协商时采用2048-bit的Diffie-Hellman group。

**[group2**]：指定阶段1密钥协商时采用1024-bit的Diffie-Hellman group。

**[group24**]：指定阶段1密钥协商时采用含256-bit的sub-group的2048-bit Diffie-Hellman group。

**[group5**]：指定阶段1密钥协商时采用1536-bit的Diffie-Hellman group。

【使用指导】

**[group1**]提供了最低的安全性，但是处理速度最快。**group24**提供了最高的安全性，但是处理速度最慢。其它的Diffie-Hellman group随着其位数的增加提供更高的安全性，但是处理速度会相应减慢。请根据实际组网环境中对安全性和性能的要求选择合适的Diffie-Hellman group。

【举例】

\# 指定IKE提议1使用2048-bit的Diffie-Hellman group。

\<Sysname\> system-view

Sysname ike proposal 1

Sysname-ike-proposal-1 dh group14

【相关命令】

l**display ike proposal**

**IKE \-- IKE配置命令 \-- display ike proposal**

------------------------------------------------------------------------

**[display** **ike** **proposal**]命令用来显示所有IKE提议的配置信息。

【命令】

**[display ike proposal**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

IKE提议按照优先级的先后顺序显示。如果没有配置任何IKE提议，则只显示缺省的IKE提议。

【举例】

\# 显示IKE提议的配置信息。

\<Sysname\> display ike proposal

 Priority Authentication Authentication Encryption  Diffie-Hellman Duration

              method       algorithm    algorithm       group      (seconds)

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 1        RSA-SIG            MD5        DES-CBC     Group 1        5000

 11       PRE-SHARED-KEY     MD5        DES-CBC     Group 1        50000

 default  PRE-SHARED-KEY     SHA1       DES-CBC     Group 1        86400

表2-1 display ike proposal命令显示信息描述表

字段

描述

Priority

IKE提议的优先级

Authentication method

IKE提议使用的认证方法，包括：

·PRE-SHARED-KEY：预共享密钥

·RSA-SIG：RSA签名

·DSA-SIG：DSA签名

Authentication algorithm

IKE提议使用的认证算法，包括：

·MD5：HMAC-MD5算法

·SHA1：HMAC-SHA1算法

Encryption algorithm

IKE提议使用的加密算法，包括：

·3DES-CBC：168位CBC模式的3DES算法

·AES-CBC-128：128位CBC模式的AES算法

·AES-CBC-192：192位CBC模式的AES算法

·AES-CBC-256：256位CBC模式的AES算法

·DES-CBC：56位CBC模式的DES算法

Diffie-Hellman group

IKE阶段1密钥协商时所使用的DH密钥交换参数，包括：

·Group 1：DH group1

·Group 2：DH group2

·Group 5：DH group5

·Group 14：DH group14

·Group 24：DH group24

Duration (seconds)

IKE提议中指定的IKE SA存活时间，单位为秒

【相关命令】

·**ike** **proposal**

**IKE \-- IKE配置命令 \-- display ike sa**

------------------------------------------------------------------------

![说明](IPsec命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display** **ike** **sa**]命令用来显示当前IKE SA的信息。

【命令】

**[display ike sa**[[ **verbose** [ **connection-id** *connection-id* \| **remote-address** [ **ipv6** ] *remote-address*  **vpn-instance** *vpn-name*  ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[verbose**]：显示当前IKE SA的详细信息。

**[connection-id*** connection-id*]：按照连接标识符显示IKE SA的详细信息，取值范围为1～2000000000。

**[remote-address**]：显示指定对端IP地址的IKE SA的详细信息。

**[ipv6**]：指定IPv6地址。

*[remote-address*]：对端的IP地址。

**[vpn-instance** *vpn-name*]：显示指定VPN内的IKE SA的详细信息，*vpn-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定该参数，则表示显示的IKE SA属于公网。

【使用指导】

若不指定任何参数，则显示当前所有IKE SA的摘要信息。

【举例】

\# 显示当前所有IKE SA的摘要信息。

\<Sysname\> display ike sa

    Connection-ID  Remote          Flag        DOI

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

      1            202.38.0.2      RD          IPSEC

Flags:

RD\--READY ST\--STAYALIVE RL\--REPLACED FD---FADING

表2-2 display ike sa命令显示信息描述表

字段

描述

Connection-ID

IKE SA的标识符

Remote

此IKE SA的对端的IP地址

Flags

IKE SA的状态，包括：

·RD（READY）：表示此IKE SA已建立成功

·ST（STAYALIVE）：表示此端是隧道协商发起方

·RL（REPLACED）：表示此IKE SA已经被新的IKE SA代替，一段时间后将被删除

·FD（FADING）：表示此IKE SA正在接近超时时间，目前还在使用，但即将被删除

·Unknown：表示IKE协商的状态未知

DOI

IKE SA所属解释域，包括：

·IPSEC：表示此IKE SA使用的DOI为IPSEC DOI

\# 显示当前IKE SA的详细信息。

\<Sysname\> display ike sa verbose

    \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

    Connection ID: 2

    Outside VPN: 1

    Inside VPN: 1

    Profile: prof1

    Transmitting entity: Initiator

    \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

    Local IP: 4.4.4.4

    Local ID type: IPV4_ADDR

    Local ID: 4.4.4.4

    Remote IP: 4.4.4.5

    Remote ID type: IPV4_ADDR

    Remote ID: 4.4.4.5

    Authentication-method: PRE-SHARED-KEY

    Authentication-algorithm: SHA1

    Encryption-algorithm: AES-CBC-128

    Life duration(sec): 86400

    Remaining key duration(sec): 86379

    Exchange-mode: Main

    Diffie-Hellman group: Group 1

    NAT traversal: Not detected

\# 显示目的地址为4.4.4.5的IKE SA的详细信息。

\<Sysname\> display ike sa verbose remote-address 4.4.4.5

    \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

    Connection ID: 2

    Outside VPN: 1

    Inside VPN: 1

    Profile: prof1

    Transmitting entity: Initiator

    \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

    Local IP: 4.4.4.4

    Local ID type: IPV4_ADDR

    Local ID: 4.4.4.4

    Remote IP: 4.4.4.5

    Remote ID type: IPV4_ADDR

    Remote ID: 4.4.4.5

    Authentication-method: PRE-SHARED-KEY

    Authentication-algorithm: SHA1

    Encryption-algorithm: AES-CBC-128

    Life duration(sec): 86400

    Remaining key duration(sec): 86379

    Exchange-mode: Main

    Diffie-Hellman group: Group 1

    NAT traversal: Not detected

表2-3 display ike sa verbose命令显示信息描述表

字段

描述

Connection ID

IKE SA的标识符

Outside VPN

接收报文的接口所属的MPLS L3VPN的VPN实例名称

Inside VPN

被保护数据所属的MPLS L3VPN的VPN实例名称

Profile

IKE SA协商过程中匹配到的IKE profile的名称，如果协商过程中没有匹配到任何profile，则该字段不会显示任何KE profile名称

Transmitting entity

IKE协商中的实体角色，包括：

·Initiator：发起方

·Responder：响应方

Local IP

本端安全网关的IP地址

Local ID type

本端安全网关的身份信息类型

Local ID

本端安全网关的身份信息

Remote IP

对端安全网关的IP地址

Remote ID type

对端安全网关的身份信息类型

Remote ID

对端安全网关的身份信息

Authentication-method

IKE提议使用的认证方法，包括：

·PRE-SHARED-KEY：预共享密钥

·RSA-SIG：RSA签名

·DSA-SIG：DSA签名

Authentication-algorithm

IKE提议使用的认证算法，包括：

·MD5：HMAC-MD5算法

·SHA1：HMAC-SHA1算法

Encryption-algorithm

IKE提议使用的加密算法，包括：

·3DES-CBC：168位CBC模式的3DES算法

·AES-CBC-128：128位CBC模式的AES算法

·AES-CBC-192：192位CBC模式的AES算法

·AES-CBC-256：256位CBC模式的AES算法

·DES-CBC：56位CBC模式的DES算法

Life duration(sec)

IKE SA的存活时间，单位为秒

Remaining key duration(sec)

IKE SA的剩余存活时间，单位为秒

Exchange-mode

IKE第一阶段的协商模式，包括：

·Main：主模式

·Aggressive： 野蛮模式

Diffie-Hellman group

IKE第一阶段密钥协商时所使用的DH密钥交换参数，包括：

·Group 1：DH group1

·Group 2：DH group2

·Group 5：DH group5

·Group 14：DH group14

·Group 24：DH group24

NAT traversal

是否检测到协商双方之间存在NAT网关设备

**IKE \-- IKE配置命令 \-- dpd**

------------------------------------------------------------------------

**[dpd**]命令用来配置IKE DPD功能。

**[undo dpd**]命令用来关闭IKE DPD功能。

【命令】

**[dpd interval ***interval-seconds *[ **retry** *seconds*  { **on-demand** \| **periodic** }]]

**[undo dpd interval**]

【缺省情况】

IKE DPD功能处于关闭状态。

【视图】

IKE profile视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interval ***interval-seconds*]：指定触发IKE DPD探测的时间间隔，取值范围为1～300，单位为秒。对于按需探测模式，指定经过多长时间没有从对端收到IPsec报文，则触发一次DPD探测；对于定时探测模式，指触发一次DPD探测的时间间隔。

**[retry*** seconds*]：指定DPD报文的重传时间间隔，取值范围为1～60，单位为秒。缺省情况下，DPD报文的重传时间间隔为5秒。

**[on-demand**]：指定按需探测模式，根据流量来探测对端是否存活，在本端发送用户报文时，如果发现当前距离最后一次收到对端报文的时间超过指定的触发IKE DPD探测的时间间隔，则触发DPD探测。

**[periodic**]：指定定时探测模式，按照触发IKE DPD探测的时间间隔定时探测对端是否存活。

【使用指导】

IKE DPD有两种模式：按需探测模式和定时探测模式。一般若无特别要求，建议使用按需探测模式，在此模式下，仅在本端需要发送报文时，才会触发探测；如果需要尽快地检测出对端的状态，则可以使用定时探测模式。在定时探测模式下工作，会消耗更多的带宽和计算资源，因此当设备与大量的IKE对端通信时，应优先考虑使用按需探测模式。

如果IKE profile视图下和系统视图下都配置了IKE DPD功能，则IKE profile视图下的DPD配置生效，如果IKE profile视图下没有配置IKE DPD功能，则采用系统视图下的DPD配置。

建议配置的**interval**时间大于**retry**时间，使得直到当前DPD探测结束才可以触发下一次DPD探测，在重传DPD报文过程中不会触发新的DPD探测。

【举例】

\# 为IKE profile 1配置IKE DPD功能，指定若10秒内没有从对端收到IPsec报文，则触发IKE DPD探测，DPD请求报文的重传时间间隔为5秒，探测模式为按需探测。

\<Sysname\> system-view

Sysname ike profile 1

Sysname-ike-profile-1 dpd interval 10 retry 5 on-demand

【相关命令】

l**ike dpd**

**IKE \-- IKE配置命令 \-- encryption-algorithm**

------------------------------------------------------------------------

**[encryption-algorithm**]命令用来指定一个供IKE提议使用的加密算法。

**[undo** **encryption-algorithm**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[encryption-algorithm**[ { **3des-cbc** \| **aes-cbc-128** \| **aes-cbc-192** \| **aes-cbc-256** \| **des-cbc** }]]

**[undo encryption-algorithm**]

FIPS模式下：

**[encryption-algorithm**[ { **aes-cbc-128** \| **aes-cbc-192** \| **aes-cbc-256** }]]

**[undo encryption-algorithm**]

【缺省情况】

非FIPS模式下：

IKE提议使用的加密算法为**des-cbc**，即CBC模式的56-bit DES加密算法。

FIPS模式下：

IKE提议使用的加密算法为**aes-cbc-128**，即CBC模式的AES算法，AES算法采用128比特的密钥进行加密。

【视图】

IKE提议视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[3des-cbc**]：指定IKE安全提议采用的加密算法为CBC模式的3DES算法，3DES算法采用168比特的密钥进行加密。

**[aes-cbc-128**]：指定IKE安全提议采用的加密算法为CBC模式的AES算法，AES算法采用128比特的密钥进行加密。

**[aes-cbc-192**]：指定IKE安全提议采用的加密算法为CBC模式的AES算法，AES算法采用192比特的密钥进行加密。

**[aes-cbc-256**]：指定IKE安全提议采用的加密算法为CBC模式的AES算法，AES算法采用256比特的密钥进行加密。

**[des-cbc**]：指定IKE安全提议采用的加密算法为CBC模式的DES算法，DES算法采用56比特的密钥进行加密。

【使用指导】

算法强度从低到高依次为**des-cbc**、**3des-cbc**、**aes-cbc-128**、**aes-cbc-192**、**aes-cbc-256**，算法强度越高，安全性越好，计算量越大。请根据实际组网环境中对安全性和性能的要求选择适当强度的算法。

【举例】

\# 指定IKE提议1的加密算法为128比特的CBC模式的AES。

\<Sysname\> system-view

Sysname ike proposal 1

Sysname-ike-proposal-1 encryption-algorithm aes-cbc-128

【相关命令】

l**display ike proposal**

**IKE \-- IKE配置命令 \-- exchange-mode**

------------------------------------------------------------------------

**[exchange-mode**]命令用来选择IKE第一阶段的协商模式。

**[undo exchange-mode**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[exchange-mode **[{ **aggressive** \| **main** }]]

**[undo exchange-mode**]

FIPS模式下：

**[exchange-mode main**]

**[undo exchange-mode**]

【缺省情况】

IKE第一阶段的协商模式为主模式。

【视图】

IKE profile视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[aggressive**]：野蛮模式。

**[main**]：主模式。

【使用指导】

当本端的IP地址为自动获取（如本端用户为拨号方式，IP地址为动态分配），且采用预共享密钥认证方式时，建议将本端的协商模式配置为野蛮模式。

【举例】

\# 配置IKE第一阶段协商使用主模式。

\<Sysname\> system-view

Sysname ike profile 1

Sysname-ike-profile-1 exchange-mode main

【相关命令】

·**display ike proposal**

**IKE \-- IKE配置命令 \-- ike dpd**

------------------------------------------------------------------------

![说明](IPsec命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[ike dpd**]命令用来配置全局IKE DPD功能。

**[undo ike dpd**]命令用来关闭全局IKE DPD功能。

【命令】

**[ike dpd interval ***interval-seconds *[ **retry** *seconds*  { **on-demand** \| **periodic** }]]

**[undo ike dpd interval**]

【缺省情况】

全局IKE DPD功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interval ***interval-seconds*]：指定触发IKE DPD探测的时间间隔，取值范围为1～300，单位为秒。对于按需探测模式，指定经过多长时间没有从对端收到IPsec报文，则触发一次DPD探测；对于定时探测模式，指触发一次DPD探测的时间间隔。

**[retry*** seconds*]：指定DPD报文的重传时间间隔，取值范围为1～60，单位为秒，缺省值为5秒。

**[on-demand**]：指定按需探测模式，根据流量来探测对端是否存活，在本端发送IPsec报文时，如果发现当前距离最后一次收到对端报文的时间超过指定的触发IKE DPD探测的时间间隔（即通过*interval-seconds*指定的时间），则触发DPD探测。

**[periodic**]：指定定时探测模式，按照触发IKE DPD探测的时间间隔（即通过*interval-seconds*指定的时间）定时探测对端是否存活。

【使用指导】

IKE DPD有两种模式：按需探测模式和定时探测模式。一般若无特别要求，建议使用按需探测模式，在此模式下，仅在本端需要发送报文时，才会触发探测；如果需要尽快地检测出对端的状态，则可以使用定时探测模式。在定时探测模式下工作，会消耗更多的带宽和计算资源，因此当设备与大量的IKE对端通信时，应优先考虑使用按需探测模式。

如果IKE profile视图下和系统视图下都配置了DPD探测功能，则IKE profile视图下的DPD配置生效，如果IKE profile视图下没有配置DPD探测功能，则采用系统视图下的DPD配置。

建议配置的**interval**大于**retry**，使得直到当前DPD探测结束才可以触发下一次DPD探测，在重传DPD报文的过程中不触发新的DPD探测。

【举例】

\# 配置流量触发IKE DPD探测间隔时间为10秒，重传时间间隔为5秒，探测模式为按需探测。

\<Sysname\> system-view

Sysname ike dpd interval 10 retry 5 on-demand

【相关命令】

·**dpd**

**IKE \-- IKE配置命令 \-- ike identity**

------------------------------------------------------------------------

**[ike identity**]命令用来配置本端身份信息，用于在IKE认证协商阶段向对端标识自己的身份。

**[undo** **ike identity**]命令用来删除配置的本端身份信息，并恢复为默认身份。

【命令】

**[ike identity **[{ **address** { *ipv4-address \|* **ipv6** *ipv6-address* } \| **dn** \| **fqdn** [ *fqdn-name* ] \| **user-fqdn**  *user-fqdn-name*  }]]

**[undo ike identity**]

【缺省情况】

使用IP地址标识本端的身份，该IP地址为IPsec安全策略或IPsec安全策略模板应用的接口IP地址。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[address**[ { *ipv4-address* \| **ipv6** *ipv6-address* }]]：指定标识本端身份的IP地址，其中*ipv4-address*为标识本端身份的IPv4地址，*ipv6-address*为标识本端身份的IPv6地址。

**[dn**]：使用从数字证书中获得的DN名作为本端身份。

**[fqdn** *fqdn-name*]：指定标识本端身份的FQDN名称，*fqdn-name*表示FQDN名称，为1～255个字符的字符串，区分大小写，例如www.test.com。不指定*fqdn-name*时，则设备将使用**sysname**命令配置的设备的名称作为本端FQDN类型的身份。

**[user-fqdn ***user-fqdn-name*]：指定标识本端身份的User FQDN名称，*user-fqdn-name*表示User FQDN名称，为1～255个字符的字符串，区分大小写，例如adc@test.com。不指定*user-fqdn-name*时，则设备将使用**sysname**命令配置的设备的名称作为本端user FQDN类型的身份。

【使用指导】

本命令用于全局配置IKE对等体的本端身份，适用于所有IKE SA的协商，而IKE profile下的**local-identity**为局部配置身份，仅适用于使用本IKE profile的IKE SA的协商。

如果本端的认证方式为数字签名方式，则本端可以配置任何类型的身份信息；如果本端的认证方式为预共享密钥方式，则只能配置除DN之外的其它类型的身份信息。

如果希望在采用数字签名认证时，总是从证书中的主题字段取得本端身份，则可以通过**ike signature-identity from-certificate**命令实现。如果没有配置**ike signature-identity from-certificate**，并且IPsec安全策略或IPsec安全策略模板下指定的IKE profile中配置了本端身份（由**local-identity**命令指定），则使用IKE profile中配置的本端身份；若IPsec安全策略或IPsec安全策略模板下未指定IKE profile或IKE profile下没有配置本端身份，则使用全局配置的本端身份（由**ike identity**命令指定）。

【举例】

\# 指定使用IP地址2.2.2.2标识本端身份。

\<sysname\> system-view

sysname ike identity address 2.2.2.2

【相关命令】

l**local-identity**

·**ike signature-identity from-certificate**

**IKE \-- IKE配置命令 \-- ike invalid-spi-recovery enable**

------------------------------------------------------------------------

**[ike invalid-spi-recovery enable**]命令用来使能针对无效IPsec SPI的IKE SA恢复功能。

**[undo ike invalid-spi-recovery enable**]命令用来恢复缺省情况。

【命令】

**[ike invalid-spi-recovery enable**]

**[undo ike invalid-spi-recovery enable**]

【缺省情况】

针对无效IPsec SPI的IKE SA恢复功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当IPsec隧道一端的安全网关出现问题（例如安全网关重启）导致本端IPsec SA丢失时，会造成IPsec流量黑洞现象：一端（接收端）的IPsec SA已经完全丢失，而另一端（发送端）还持有对应的IPsec SA且不断地向对端发送报文，当接收端收到发送端使用此IPsec SA封装的IPsec报文时，就会因为找不到对应的SA而持续丢弃报文，形成流量黑洞。该现象造成IPsec通信链路长时间得不到恢复（只有等到发送端旧的IPsec SA生命周期超时，并重建IPsec SA后，两端的IPsec流量才能得以恢复），因此需要采取有效的IPsec SA恢复手段来快速恢复中断的IPsec通信链路。

SA由SPI唯一标识，接收方根据IPsec报文中的SPI在SA数据库中查找对应的IPsec SA，若接收方找不到处理该报文的IPsec SA，则认为此报文的SPI无效。如果接收端当前存在IKE SA，则会向对端发送删除对应IPsec SA的通知消息，发送端IKE接收到此通知消息后，就会立即删除此无效SPI对应的IPsec SA。之后，当发送端需要继续向接收端发送报文时，就会触发两端重建IPsec SA，使得中断的IPsec通信链路得以恢复；如果接收端当前不存在IKE SA，就不会触发本端向对端发送删除IPsec SA的通知消息，接受端将默认丢弃无效SPI的IPsec 报文，使得链路无法恢复。后一种情况下，如果使能了IPsec无效SPI恢复IKE SA功能，就会触发本端与对端协商新的IKE SA并发送删除消息给对端，从而使链路恢复正常。

由于使能此功能后，若攻击者伪造大量源IP地址不同但目的IP地址相同的无效SPI报文发给设备，会导致设备因忙于与无效对端协商建立IKE SA而面临受到DoS（Denial of Sevice）攻击的风险，通常情况下，建议关闭针对无效IPsec SPI的IKE SA恢复功能。

【举例】

\# 使能IPsec无效SPI恢复IKE SA功能。

\<Sysname\> system-view

Sysname ike invalid-spi-recovery enable

**IKE \-- IKE配置命令 \-- ike keepalive interval**

------------------------------------------------------------------------

![说明](IPsec命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ike keepalive interval**]命令用来配置通过IKE SA向对端发送IKE Keepalive报文的时间间隔。

**[undo ike  keepalive interval**]命令用来恢复缺省情况。

【命令】

**[ike keepalive interval** *seconds*]

**[undo ike keepalive interval**]

【缺省情况】

不向对端发送IKE Keepalive报文。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：指定向对端发送IKE SA的Keepalive报文的时间间隔，取值范围为20～28800，单位为秒。

【使用指导】

当有检测对方IKE SA和IPsec SA是否存活的需求时，通常建议配置IKE DPD，不建议配置IKE Keepalive功能。仅当对方不支持IKE DPD特性，但支持IKE Keepalive功能时，才考虑配置IKE Keepalive功能。

本端配置的IKE Keepalive报文的等待超时时间要大于对端发送的时间间隔。由于网络中一般不会出现超过三次的报文丢失，所以，本端的超时时间可以配置为对端配置的发送IKE Keepalive报文的时间间隔的三倍。

【举例】

\# 配置本端向对端发送Keepalive报文的时间间隔为200秒。

\<Sysname\> system-view

Sysname ike keepalive interval 200

【相关命令】

·**ike keepalive timeout**

**IKE \-- IKE配置命令 \-- ike keepalive timeout**

------------------------------------------------------------------------

![说明](IPsec命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ike keepalive timeout**]命令用来配置本端等待对端发送IKE Keepalive报文的超时时间。超过该时间之后，本端的IKE SA将会被删除。

**[undo ike keepalive timeout**]命令用来恢复缺省情况。

【命令】

**[ike keepalive timeout*** seconds*]

**[undo ike keepalive timeout**]

【缺省情况】

永不超时。无论是否收到对端的IKE Keepalive报文，本端IKE SA仅按照协商出来的老化时间进行老化。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：指定本端等待对端发送IKE Keepalive报文的超时时间，取值范围为20～28800，单位为秒。

【使用指导】

本端配置的等待对端发送IKE Keepalive报文的超时时间要大于对端发送IKE Keepalive报文的时间间隔。由于网络中一般不会出现超过三次的报文丢失，所以，本端的超时时间可以配置为对端配置的发送IKE Keepalive报文的时间间隔的三倍。

【举例】

\# 配置本端等待对端发送IKE Keepalive报文的超时时间为20秒。

\<Sysname\> system-view

Sysname ike keepalive timeout 20

【相关命令】

·**ike keepalive interval**

**IKE \-- IKE配置命令 \-- ike keychain**

------------------------------------------------------------------------

**[ike keychain**]命令用来创建并进入一个IKE keychain视图，该视图用于配置IKE对等体的密钥信息。

**[undo ike keychain**]命令用来删除指定的IKE keychain以及IKE对等体的密钥信息。

【命令】

**[ike keychain** *keychain-name* [ **vpn-instance** *vpn-name* ]]

**[undo** **ike keychain** *keychain-name* [ **vpn-instance** *vpn-name* ]]

【缺省情况】

不存在IKE keychain。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[keychain-name*]：IKE keychain的名字，为1～63个字符的字符串，不区分大小写。

**[vpn-instance** *vpn-name*]：指定IKE keychain所属的VPN。*vpn-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定该参数，则表示IKE keychain属于公网。

【使用指导】

在IKE需要通过预共享密钥方式进行认证时，需要创建并指定IKE keychain。

【举例】

\# 创建IKE keychain key1并进入IKE keychain视图。

\<Sysname\> system-view

Sysname ike keychain key1

Sysname-ike-keychain-key1

【相关命令】

l**authentication-method**

l**pre-shared-key**

**IKE \-- IKE配置命令 \-- ike limit**

------------------------------------------------------------------------

![说明](IPsec命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ike limit**]命令用来配置对本端IKE SA数目的限制。

**[undo ike limit**]命令用来恢复缺省情况。

【命令】

**[ike limit**[ { **max-negotiating-sa** *negotiation-limit* \| **max-sa** *sa-limit* }]]

**[undo ike limit **[{ **max-negotiating-sa** \| **max-sa** }]]

【缺省情况】

不限制IKE SA数目。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[max-negotiating-sa** *negotiation-limit*]：指定允许同时处于协商状态的IKE SA和IPsec SA的最大总和数，取值范围与设备的型号有关，请以设备的实际情况为准。

**[max-sa** *sa-limit*]：指定允许建立的IKE SA的最大数，取值范围与设备的型号有关，请以设备的实际情况为准。

【使用指导】

可以通过**max-negotiating-sa**参数设置允许同时协商更多的IKE SA，以充分利用设备处理能力，以便在设备有较强处理能力的情况下得到更高的新建性能；可以通过该参数设置允许同时协商更少的IKE SA，以避免产生大量不能完成协商的IKE SA，以便在设备处理能力较弱时保证一定的新建性能。

可以通过**max-sa**参数设置允许建立更多的IKE SA，以便在设备有充足内存的情况下得到更高的并发性能；可以通过该参数设置允许建立更少的IKE SA，以便在设备没有充足的内存的情况下，使IKE不过多占用系统内存。

【举例】

\# 配置本端允许同时处于协商状态的IKE SA和IPsec SA的最大总和数为200。

\<Sysname\> system-view

Sysname ike limit max-negotiating-sa 200

\# 配置本端允许成功建立的IKE SA的最大数为5000。

\<Sysname\> system-view

Sysname ike limit max-sa 5000

**IKE \-- IKE配置命令 \-- ike nat-keepalive**

------------------------------------------------------------------------

![说明](IPsec命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ike nat-keepalive**]命令用来配置向对端发送NAT Keepalive报文的时间间隔。

**[undo ike nat-keepalive**]命令用来恢复缺省情况。

【命令】

**[ike nat-keepalive **]*seconds*

**[undo ike nat-keepalive**]

【缺省情况】

向对端发送NAT Keepalive报文的时间间隔为20秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：指定向对端发送NAT Keepalive报文的时间间隔，取值范围为5～300，单位为秒。

【使用指导】

该命令仅对位于NAT之后的设备（即该设备位于NAT设备连接的私网侧）有意义。NAT之后的IKE网关设备需要定时向NAT之外的IKE网关设备发送NAT Keepalive报文，以便维持NAT设备上对应的IPsec流量的会话存活，从而让NAT之外的设备可以访问NAT之后的设备。

因此，需要确保该命令配置的时间小于NAT设备上会话表项的存活时间。关于如何查看NAT表项的存活时间，请参见"三层技术-IP业务命令参考"中的"NAT"。

【举例】

\# 配置向对端发送NAT Keepalive报文的时间间隔为5秒。

\<Sysname\> system-view

Sysname ike nat-keepalive 5

**IKE \-- IKE配置命令 \-- ike profile**

------------------------------------------------------------------------

**[ike profile**]命令用来创建一个IKE profile，并进入IKE profile视图。

**[undo** **ike profile**]命令用来删除指定的IKE profile。

【命令】

**[ike profile ***profile-name*]

**[undo ike profile ***profile-name*]

【缺省情况】

不存在IKE profile。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[profile-name*]：IKE profile名称，为1～63个字符的字符串，不区分大小写。

【举例】

\# 创建IKE profile 1，并进入其视图。

\<Sysname\> system-view

Sysname ike profile 1

Sysname-ike-profile-1

**IKE \-- IKE配置命令 \-- ike proposal**

------------------------------------------------------------------------

**[ike** **proposal**]命令用来创建IKE提议，并进入IKE提议视图。

**[undo** **ike** **proposal**]命令用来删除一个IKE提议。

【命令】

**[ike** **proposal** *proposal-number*]

**[undo** **ike** **proposal** *proposal-number*]

【缺省情况】

系统提供一条缺省的IKE提议，此缺省的IKE提议具有最低的优先级。缺省的提议的参数不可修改，其参数包括：

l加密算法：非FIPS模式下使用DES-CBC，FIPS模式下使用AES-CBC-128

l认证算法：HMAC-SHA1

l认证方法：预共享密钥

lDH密钥交换参数：非FIPS模式使用group1，FIPS模式下使用group14

lIKE SA存活时间：86400秒

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[proposal-number*]：IKE提议序号，取值范围为1～65535。该序号同时表示优先级，数值越小，优先级越高。

【使用指导】

在进行IKE协商的时候，协商发起方会将自己的IKE提议发送给对端，由对端进行匹配。若发起方使用的IPsec安全策略中没有引用IKE profile，则会将当前系统中所有的IKE提议发送给对端；否则，发起方会将引用的IKE profle中的所有IKE提议发送给对端。

响应方则以对端发送的IKE提议优先级从高到低的顺序与本端所有的IKE提议进行匹配，一旦找到匹配项则停止匹配并使用匹配的提议，否则继续查找其它的IKE提议。如果本端配置中没有和对端匹配的IKE提议，则使用系统缺省的IKE提议进行匹配。

【举例】

\# 创建IKE提议1，并进入IKE提议视图。

\<Sysname\> system-view

Sysname ike proposal 1

Sysname-ike-proposal-1

【相关命令】

·**display ike proposal**

**IKE \-- IKE配置命令 \-- ike signature-identity from-certificate**

------------------------------------------------------------------------

**[ike signature-identity from-certificate**]命令用来配置当使用数字签名认证方式时，本端的身份总是从本端证书的主题字段中获得，不论**local-identity**或**ike identity**如何配置。

**[undo** **ike signature-identity from-certificate**]命令用来恢复缺省的情况。

【命令】

**[ike signature-identity from-certificate**]

**[undo** **ike signature-identity from-certificate**]

【缺省情况】

当使用数字签名认证方式时，本端身份信息由**local-identity**或**ike identity**命令指定。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在采用IPsec野蛮协商模式以及数字签名认证方式的情况下，与仅支持使用DN类型身份进行数字签名认证的ComwareV5设备互通时需要配置本命令。

如果没有配置**ike signature-identity from-certificate**，并且IPsec安全策略或IPsec安全策略模板下指定的IKE profile中配置了本端身份（由**local-identity**命令指定），则使用IKE profile中配置的本端身份；若IPsec安全策略或IPsec安全策略模板下未指定IKE profile或IKE profile下没有配置本端身份，则使用全局配置的本端身份（由**ike identity**命令指定）。

【举例】

\# 在采用数字签名认证时，指定总从本端证书中的主题字段取得本端身份。

\<Sysname\> system-view

sysname ike signature-identity from-certificate

【相关命令】

l**local-identity**

l**ike identity**

**IKE \-- IKE配置命令 \-- inside-vpn**

------------------------------------------------------------------------

**[inside-vpn**]命令用来指定内部VPN实例。

**[undo** **inside-vpn** ]命令用来取消指定的内部VPN实例。

【命令】

**[inside-vpn** **vpn-instance** *vpn-name*]

**[undo inside-vpn**]

【缺省情况】

IKE profile未指定内部VPN实例，设备在收到IPsec报文的接口所属的VPN中查找路由。

【视图】

IKE profile视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-name*]：保护的数据属于指定的VPN。*vpn-name*为MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。

【使用指导】

当IPsec解封装后得到的报文需要继续转发到不同的VPN中去时，设备需要知道在哪个MPLS L3VPN实例中查找相应的路由。缺省情况下，设备在与外网相同的VPN中查找路由。如果不希望在与外网相同的VPN中查找路由去转发解封装后的报文，则可以通过此命令指定一个内部VPN实例，指定设备通过查找该内部VPN实例中的路由来转发解封装后的报文。

【举例】

\# 在IKE profile prof1中指定内部VPN实例为vpn1。

\<Sysname\> system-view

Sysname ike profile prof1

Sysname-ike-profile-prof1 inside-vpn vpn-instance vpn1

**IKE \-- IKE配置命令 \-- keychain**

------------------------------------------------------------------------

**[keychain**]命令用来指定采用预共享密钥认证时使用的IKE keychain。

**[undo** **keychain**]命令用取消指定的IKE keychain。

【命令】

**[keychain ***keychain-name*]

**[undo keychain ***keychain-name*]

【缺省情况】

未指定IKE keychain。

【视图】

IKE profile视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[keychain-name*]：指定配置的IKE keychain名称，为1～63个字符的字符串，不区分大小写。

【使用指导】

一个IKE profile中最多可以指定六个IKE keychain，先配置的IKE keychain优先级高。

【举例】

\# 在IKE profile 1中指定名称为abc的配置的IKE keychain。

\<Sysname\> system-view

Sysname ike profile 1

Sysname-ike-profile-1 keychain abc

【相关命令】

·**ike keychain**

**IKE \-- IKE配置命令 \-- local-identity**

------------------------------------------------------------------------

**[local-identity**]命令用来配置本端身份信息，用于在IKE认证协商阶段向对端标识自己的身份。

**[undo** **local-identity**]命令用来删除配置的本端身份信息。

【命令】

**[local-identity **[{ **address** { *ipv4-address \|* **ipv6** *ipv6-address* } \| **dn** \| **fqdn** [ *fqdn-name* ] \| **user-fqdn**  *user-fqdn-name*  }]]

**[undo local-identity**]

【缺省情况】

未配置本端身份信息。此时使用系统视图下通过**ike identity**命令配置的身份信息作为本端身份信息。若两者都没有配置，则使用IP地址标识本端的身份，该IP地址为IPsec安全策略或IPsec安全策略模板应用的接口的IP地址。

【视图】

IKE profile视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[address**[ { *ipv4-address* \| **ipv6** *ipv6-address* }]]：指定标识本端身份的IP地址，其中*ipv4-address*为标识本端身份的IPv4地址，*ipv6-address*为标识本端身份的IPv6地址。

**[dn**]：使用从本端数字证书中获得的DN名作为本端身份。

**[fqdn** *fqdn-name*]：指定标识本端身份的FQDN名称，*fqdn-name*为1～255个字符的字符串，区分大小写，例如www.test.com。不指定*fqdn-name*时，则设备将使用**sysname**命令配置的设备的名称作为本端FQDN类型的身份。

**[user-fqdn ***user-fqdn-name*]：指定标识本端身份的user FQDN名称，*user-fqdn-name*为1～255个字符的字符串，区分大小写，例如adc@test.com。不指定*user-fqdn-name*时，则设备将使用**sysname**命令配置的设备的名称作为本端user FQDN类型的身份。

【使用指导】

如果本端的认证方式为数字签名方式，则本端可以配置任何类型的身份信息；如果本端的认证方式为预共享密钥方式，则只能配置除DN之外的其它类型的身份信息。

如果本端的认证方式为数字签名方式，且配置的本端身份为IP地址，但这个IP地址与本端证书中的IP地址不同，则设备将使用FQDN类型的本端身份标识，该标识为使用**sysname**命令配置的设备名称。

响应方使用发起方的身份信息查找本地的IKE profile，通过与**match remote**命令中指定的发起方身份信息进行匹配，可查找到本端要采用的IKE profile。

一个IKE profile中只能配置一条本端身份信息。

IKE profile下的本端身份信息优先级高于系统视图下通过**ike identity**命令配置的本端身份信息。如果IKE profile下未配置本端身份信息，则使用系统视图下配置的本端身份信息。

【举例】

\# 指定使用IP地址2.2.2.2标识本端身份。

\<Sysname\> system-view

Sysname ike profile prof1

Sysname-ike-profile-prof1 local-identity address 2.2.2.2

【相关命令】

l**match remote**

·{.TerminalDisplayshading}**ike identity**

**IKE \-- IKE配置命令 \-- match local address (IKE keychain view)**

------------------------------------------------------------------------

**[match local address**]命令用来限制IKE keychain的使用范围，即IKE keychain只能用于指定地址或指定接口的地址上的IKE协商。

**[undo match local address**]命令用来取消对IKE keychain使用范围的限制。

【命令】

**[match local address **[{ *interface-type interface-number* \| { *ipv4-address* \| **ipv6** *ipv6-address* } [ **vpn-instance** *vpn-name* ] }]]

**[undo match local address**]

【缺省情况】

未限制IKE keychain的使用范围。

【视图】

IKE keychain视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type interface-number*]：本端接口名称。可以是任意的三层接口。

*[ipv4-address*]：本端接口的IPv4地址。

**[ipv6** *ipv6-address*]：本端接口的IPv6地址。

**[vpn-instance** *vpn-name*]：指定接口地址所属的VPN。*vpn-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定该参数，则表示接口地址属于公网。

【使用指导】

此命令用于限制IKE keychain只能用于指定地址或指定接口的地址上的协商，这里的地址指的是IPsec安全策略/IPsec安全策略模板下配置的本端地址（通过命令**local-address**配置），若本端地址没有配置，则为引用IPsec安全策略的接口的IP地址。

一个IKE profile中最多可以指定六个IKE keychain，先配置的IKE keychain优先级高。若希望本端在匹配某些IKE keychain的时候，不按照配置的优先级来查找，则可以通过本命令来指定这类IKE keychain的使用范围。例如，IKE keychain A中的预共享密钥的匹配地址范围大（2.2.0.0/16），IKE keychain B中的预共享密钥的匹配地址范围小（2.2.2.0/24），IKE keychain A先于IKE keychain B配置。若希望本端IP地址为2.2.2.2的接口上使用IKE keychain B，但是按照配置顺序匹配，依据本端IP地址2.2.2.2总会匹配到预共享密钥地址范围大的IKE keychain A，而找不到期望的IKE keychain B。这中情况下，可以通过配置IKE keychainB在指定地址2.2.2.2的接口上使用，使其找到正确的预共享密钥。

【举例】

\# 创建IKE keychain，名称为key1。

\<Sysname\> system-view

Sysname ike keychain key1

\# 限制IKE keychain key1只能在名称为vpn1的VPN实例中IP地址为2.2.2.2的接口上使用。

sysname-ike-keychain-key1 match local address 2.2.2.2 vpn-instance vpn1

**IKE \-- IKE配置命令 \-- match local address (IKE profile view)**

------------------------------------------------------------------------

**[match local address**]命令用来限制IKE profile的使用范围，即IKE profile只能用于指定地址或指定接口的地址上的IKE协商。

**[undo match local address**]命令用来取消对IKE profile使用范围的限制。

【命令】

**[match local address **[{ *interface-type interface-number* \| { *ipv4-address* \| **ipv6** *ipv6-address* } [ **vpn-instance** *vpn-name* ] }]]

**[undo match** **local address**]

【缺省情况】

未限制IKE profile的使用范围。

【视图】

IKE profile视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type interface-number*]：本端接口名称。可以是任意三层接口。

*[ipv4-address*]：本端接口IPv4地址。

**[ipv6** *ipv6-address*]：本端接口IPv6地址。

**[vpn-instance** *vpn-name*]：指定接口地址所属的VPN。*vpn-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定该参数，则表示接口地址属于公网。

【使用指导】

此命令用于限制IKE profile只能用于指定地址或指定接口的地址上的协商，这里的地址指的是IPsec安全策略/IPsec安全策略模板下配置的本端地址（通过命令**local-address**配置），若本端地址没有配置，则为引用IPsec安全策略的接口的IP地址。

先配置的IKE profile优先级高，若希望本端在匹配某些IKE profile的时候，不按照配置的优先级来查找，则可以通过本命令来指定这类IKE profile的使用范围。例如，IKE profile A中的match remote地址范围大（match remote identity address range 2.2.2.1 2.2.2.100），IKE profile B中的match remote地址范围小（match remote identity address range 2.2.2.1 2.2.2.10），IKE profile A先于IKE profile B配置。若希望本端IP地址为2.2.2.2的接口上使用IKE profile B，但是按照配置顺序匹配，依据本端IP地址2.2.2.2总会匹配到预共享密钥地址范围大的IKE profile A，而找不到期望的IKE profile B。这种情况下，可以通过配置IKE profile B在指定地址2.2.2.2的接口上使用，使其找到正确的IKE profile。

【举例】

\# 创建IKE profile，名称为prof1。

\<Sysname\> system-view

Sysname ike profile prof1

\# 限制IKE profile prof1 只能在名称为vpn1的VPN中IP地址为2.2.2.2的接口上使用。

sysname-ike-profile-prof1 match local address 2.2.2.2 vpn-instance vpn1

**IKE \-- IKE配置命令 \-- match remote**

------------------------------------------------------------------------

**[match remote**]命令用来配置一条用于匹配对端身份的规则。

**[undo match remote**]命令用来删除一条用于匹配对端身份的规则。

【命令】

**[match remote **[{ **certificate** *policy-name* \| **identity** { **address** { { *ipv4-address* [ *mask \| mask-length* ] \| **range** *low-ipv4-address high-ipv4-address* } \| **ipv6** { *ipv6-address*  *prefix-length*  \| **range** *low-ipv6-address high-ipv6-address* } }  **vpn-instance** *vpn-name*  \| **fqdn** *fqdn-name* \| **user-fqdn** *user-fqdn-name* } }]]

**[undo**[ **match remote** { **certificate** *policy-name* \| **identity** { **address** { { *ipv4-address* [ *mask \| mask-length* ] \| **range** *low-ipv4-address high-ipv4-address* } \| **ipv6** { *ipv6-address*  *prefix-length*  \| **range** *low-ipv6-address high-ipv6-address* } }  **vpn-instance** *vpn-name*  \| **fqdn** *fqdn-name* \| **user-fqdn** *user-fqdn-name* } }]]

【缺省情况】

未配置任何用于匹配对端身份的规则。

【视图】

IKE profile视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[certificate ***policy-name*]：基于对端数字证书中的信息匹配IKE profile。其中，*policy-name*是证书访问控制策略的名称，为1～31个字符的字符串。本参数用于响应方根据收到的发起方证书中的DN字段来过滤使用的IKE profile。

**[identity**]：基于指定的对端身份信息匹配IKE profile。本参数用于响应方根据发起方通过**local-identity**命令配置的身份信息来选择使用的IKE profile。

[·**address**[ *ipv4-address* [ *mask* \| *mask-length* ]]]：对端IPv4地址或IPv4网段。其中，*ipv4-address*为IPv4地址，*mask*为子网掩码，*mask-length*为子网掩码长度，取值范围为0～32。

·**address range ***low-ipv4-address high-ipv4-address*：对端IPv4地址范围。其中*low-ipv4-address*为起始IPv4地址，*high-ipv4-address*为结束IPv4地址。结束地址必须大于起始地址。

·**address** **ipv6** *ipv6-address* [ *prefix-length*  ]：对端IPv6地址或IPv6网段。其中，*ipv6-address*为IPv6地址，*prefix-length*为IPv6前缀，取值范围为0～128。

·**address** **ipv6 range** *low-ipv6-address high-ipv6-address*：对端IPv6地址范围。其中*low-ipv6-address*为起始IPv6地址，*high-ipv6-address*为结束IPv6地址。结束地址必须大于起始地址。

·**fqdn** *fqdn-name*：对端FQDN名称，为1～255个字符的字符串，区分大小写，例如www.test.com。

·**user-fqdn** *user-fqdn-name*：对端User FQDN名称，为1～255个字符的字符串，区分大小写，例如abc@test.com。

**[vpn-instance** *vpn-name*]：指定对端地址所属的MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定该参数，则表示对端地址属于公网。

【使用指导】

响应方根据发起发的身份信息通过本配置查找IKE profile并验证对端身份，发起方根据响应方的身份信息通过本配置验证对端身份。

协商双方都必须配置至少一个**match remote**规则，当对端的身份与IKE profile中配置的**match remote**规则匹配时，则使用此IKE profile中的信息与对端完成认证。为了使得每个对端能够匹配到唯一的IKE profile，不建议在两个或两个以上IKE profile中配置相同的**match remote**规则，否则能够匹配到哪个IKE profile是不可预知的。

**[match remote**]规则可以配置多个，并同时都有效，其匹配优先级为配置顺序。

【举例】

\# 创建IKE profile，名称为prof1。

\<Sysname\> system-view

Sysname ike profile prof1

\# 指定需要匹配对端身份类型为FQDN，取值为www.test.com。

Sysname-ike-profile-prof1 match remote identity fqdn www.test.com

\# 指定需要匹配对端身份类型为IP地址，取值为10.1.1.1。

Sysname-ike-profile-prof1 match remote identity address 10.1.1.1

【相关命令】

·**local-identity**

**IKE \-- IKE配置命令 \-- pre-shared-key**

------------------------------------------------------------------------

**[pre-shared-key**]命令用来配置预共享密钥。

**[undo pre-shared-key**]命令用来取消配置的预共享密钥。

【命令】

**[pre-shared-key **[{ **address** { *ipv4-address* [ *mask \| mask-length* ] \| **ipv6** *ipv6-address*  *prefix-length*  } \| **hostname** *host-name* } **key** { **cipher** *cipher-key* \| **simple** *simple-key* } ]]

**[undo pre-shared-key **[{ **address** { *ipv4-address* [ *mask \| mask-length* ] \| **ipv6** *ipv6-address*  *prefix-length*  } \| **hostname** *host-name* } ]]

【缺省情况】

未配置预共享密钥。

【视图】

IKE keychain视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[address**]：对端的地址。

*[ipv4-address*]：对端的IPv4地址。

*[mask*]：对端的IPv4地址掩码，缺省值为255.255.255.255。

*[mask-length*]：对端的IPv4地址掩码长度，取值范围为0～32，缺省值为32。

**[ipv6**]：指定对端的IPv6地址。

*[ipv6-address*]：对端的IPv6地址。

*[prefix-length*]：对端的IPv6地址前缀长度，取值范围为0～128，缺省值为128。

**[hostname ***host-name*]：对端主机名。取值范围为1～255，区分大小写。

**[key**]：设置的预共享密钥。

**[simple**]：表示以明文方式设置预共享密钥。

*[simple-key*]：设置的明文密钥。非FIPS模式下，为1～128个字符的字符串，区分大小写；FIPS模式下，为15～128个字符的字符串，区分大小写，密码元素的最少组合类型为4（必须包括数字、大写字母、小写字母以及特殊字符）。

**[cipher**]：表示以密文方式设置预共享密钥。

*[cipher-key*]：设置密文密钥。非FIPS模式下，为1～201个字符的字符串，区分大小写；FIPS模式下，为15～201个字符的字符串，区分大小写。

【使用指导】

配置预共享密钥的同时，还通过参数**address**和**hostname**指定了使用该预共享密钥的匹配条件，即与哪些IP地址或哪些主机名的对端协商时，才可以使用该预共享密钥。

IKE协商双方必须配置了相同的预共享密钥，预共享密钥类型的身份认证才会成功。

以明文或密文方式设置的共享密钥，均以密文的方式保存在配置文件中。

【举例】

\# 创建IKE keychain key1并进入IKE keychain视图。

\<Sysname\> system-view

Sysname ike keychain key1

\# 配置与地址为1.1.1.2的对端使用的预共享密钥为明文的123456TESTplat&!。

Sysname-ike-keychain-key1 pre-shared-key address 1.1.1.2 255.255.255.255 key simple 123456TESTplat&!

【相关命令】

l**authentication-method**

l**keychain**

**IKE \-- IKE配置命令 \-- priority (IKE keychain view)**

------------------------------------------------------------------------

**[priority**]命令用来指定IKE keychain的优先级。

**[undo** **priority**]命令用来恢复缺省情况。

【命令】

**[priority** *number*]

**[undo priority**]

【缺省情况】

IKE keychain的优先级为100。

【视图】

IKE keychain视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[priority** *number*]：IKE keychain优先级，取值范围为1～65535。该数值越小，优先级越高。

【使用指导】

配置了**match local address**的IKE keychain，优先级高于所有未配置**match local address**的IKE keychain。即IKE keychain的使用优先级首先决定于其中是否配置了**match local address**，其次取决于它的优先级。

【举例】

\# 指定IKE keychain key1的优先级为10。

\<Sysname\> system-view

Sysname ike keychain key1

Sysname-ike-keychain-key1 priority 10

**IKE \-- IKE配置命令 \-- priority (IKE profile view)**

------------------------------------------------------------------------

**[priority**]命令用来指定IKE profile的优先级。

**[undo** **priority** ]命令用来恢复缺省情况。

【命令】

**[priority** *number*]

**[undo priority**]

【缺省情况】

IKE profile的优先级为100。

【视图】

IKE-Profile视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[priority** *number*]：IKE profile优先级号，取值范围为1～65535。该数值越小，优先级越高。

【使用指导】

配置了**match local address**的IKE profile，优先级高于所有未配置**match local address**的IKE profile。即IKE profile的匹配优先级首先决定于其中是否配置了**match local address**，其次决定于它的优先级。

【举例】

\# 指定在IKE profile prof1的优先级为10。

\<Sysname\> system-view

Sysname ike profile prof1

Sysname-ike-profile-prof1 priority 10

**IKE \-- IKE配置命令 \-- proposal**

------------------------------------------------------------------------

**[proposal**]命令用来配置IKE profile引用的IKE提议。

**[undo** **proposal** ]命令用来取消所有引用的IKE提议。

【命令】

**[proposal** *proposal-number*&\<1-6\>]

**[undo proposal**]

【缺省情况】

IKE profile未引用任何IKE提议，使用系统视图下配置的IKE提议进行IKE协商。

【视图】

IKE profile视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[proposal-number*&\<1-6\>]：IKE提议序号，取值范围为1～65535。该序号在IKE profile中与优先级无关，先配置的IKE提议优先级高。&\<1-6\>表示前面的参数最多可以输入6次。

【使用指导】

IKE协商过程中，对于发起方，如果使用的IPsec安全策略下指定了IKE profile，则使用IKE profile中引用的IKE提议进行协商；对于响应方，则使用系统视图下配置的IKE提议与对端发送的IKE提议进行匹配。

【举例】

\# 设置IKE profile prof1引用序号为10的IKE安全提议。

\<Sysname\> system-view

Sysname ike profile prof1

Sysname-ike-profile-prof1 proposal 10

【相关命令】

·**ike proposal**

**IKE \-- IKE配置命令 \-- reset ike sa**

------------------------------------------------------------------------

**[reset** **ike** **sa**]命令用来清除IKE SA。

【命令】

**[reset** **ike** **sa** [ **connection-id** *connection-id* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[connection-id*** connection-id*]：清除指定连接ID的IKE SA，取值范围为1～2000000000。

【使用指导】

删除IKE SA时，会向对端发送删除通知消息。

【举例】

\# 查看当前的IKE SA。

\<Sysname\> display ike sa

    Total IKE SAs:  2

    Connection-ID  Remote            Flag        DOI

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

[      1            202.38.0.2      RD\|ST       IPSEC]

[      2            202.38.0.3      RD\|ST       IPSEC]

Flags:

RD\--READY ST\--STAYALIVE RL\--REPLACED FD---FADING TO---TIMEOUT

\# 清除连接ID号为2 的IKE SA。

\<Sysname\> reset ike sa 2

\# 查看当前的IKE SA。

\<Sysname\> display ike sa

Total IKE SAs:  1

    Connection-ID  Remote            Flag        DOI

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

[      1            202.38.0.2      RD\|ST       IPSEC]

Flags:

RD\--READY ST\--STAYALIVE RL\--REPLACED FD---FADING TO---TIMEOUT

**IKE \-- IKE配置命令 \-- reset ike statistics**

------------------------------------------------------------------------

**[reset ike statistics**]命令用于清除IKE的MIB统计信息。

【命令】

**[reset ike statistics**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 清除IKE的MIB统计信息。

\<Sysname\> reset ike statistics

【相关命令】

·**snmp-agent trap enable ike**

**IKE \-- IKE配置命令 \-- sa duration**

------------------------------------------------------------------------

**[sa** **duration**]命令用来指定一个IKE提议的IKE SA存活时间，超时后IKE SA将自动更新。

**[undo** **sa** **duration**]命令用来恢复缺省情况。

【命令】

**[sa duration** *seconds*]

**[undo sa duration**]

【缺省情况】

IKE提议的IKE SA存活时间为86400秒。

【视图】

IKE提议视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：指定IKE SA存活时间，取值范围为60～604800，单位为秒。

【使用指导】

在指定的IKE SA存活时间超时前，设备会提前协商另一个IKE SA来替换旧的IKE SA。在新的IKE SA还没有协商完之前，依然使用旧的IKE SA；在新的IKE SA建立后，将立即使用新的IKE SA，而旧的IKE SA在存活时间超时后，将被自动清除。

如果协商双方配置了不同的IKE SA存活时间，则时间较短的存活时间生效。

【举例】

\# 指定IKE提议1的IKE SA存活时间600秒（10分钟）。

\<Sysname\> system-view

Sysname ike proposal 1

Sysname-ike-proposal-1 sa duration 600

【相关命令】

·{.TerminalDisplayshading}**display ike proposal**

**IKE \-- IKE配置命令 \-- snmp-agent trap enable ike**

------------------------------------------------------------------------

**[snmp-agent trap enable ike**]命令用来开启IKE的告警功能。

**[undo snmp-agent** **trap** **enable** **ike**]命令用来关闭指定的IKE告警功能。

【命令】

**[snmp-agent trap enable** **ike** \**[attr**]**-not-support**[ \| **auth-failure** \| **cert**]**-type-unsupport**[ \| ]**cert-unavailable **[\| ]**decrypt-failure**[ \| **encrypt-failure** \| **global** \| **invalid-cert-auth**  \|]** invalid-cookie**[ \| **invalid-id**  \|]** invalid-proposal**[ \|]**invalid-protocol**[ \| ]**invalid-sign**[ \| ]**no-sa-failure **[\|  **proposal-add** \| **proposal--delete** \| **tunnel-start** \| **tunnel-stop** \| **unsupport**]**-exch-type ** \*]

**[undo snmp-agent trap enable** **ike** \**[attr**]**-not-support**[ \| **auth-failure** \| **cert**]**-type-unsupport**[ \| ]**cert-unavailable **[\| ]**decrypt-failure**[ \| **encrypt-failure** \| **global** \| **invalid-cert-auth**  \|]** invalid-cookie**[ \| **invalid-id**  \|]** invalid-proposal**[ \|]**invalid-protocol**[ \| ]**invalid-sign**[ \| ]**no-sa-failure **[\|  **proposal-add** \| **proposal--delete** \| **tunnel-start** \| **tunnel-stop** \| **unsupport**]**-exch-type ** \*]

【缺省情况】

IKE的所有告警功能均处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[attr-not-support**]：表示属性参数不支持时的告警功能。

**[auth-failure**]：表示认证失败时的告警功能。

**[cert**]**-type-unsupport**：表示证书类型不支持时的告警功能。

**[cert-unavailable**]：表示无法获取证书时的告警功能。

**[decrypt-failure**]：表示解密失败时的告警功能。

**[encrypt-failure**]：表示加密失败时的告警功能。

**[global**]：表示全局告警功能。

**[invalid-cert-auth**]：表示证书认证无效时的告警功能。

**[invalid-cookie**]：表示cookie无效时的告警功能。

**[invalid-id**]：表示身份信息无效时的告警功能。

**[invalid-proposal**]：表示IKE提议无效时的告警功能。

**[invalid**]**-protocol**：表示安全协议无效时的告警功能。

**[invalid**]**-sign**：表示证书签名无效时的告警功能。

**[no-sa-failure**]：表示无法查到SA时的告警功能。

**[proposal-add**]：表示添加IKE提议时的告警功能。

**[proposal-delete**]：表示删除IKE提议时的告警功能。

**[tunnel-start**]：表示创建IKE隧道时的告警功能。

**[tunnel-stop**]：表示删除IKE隧道时的告警功能。

**[unsupport-exch-type**]：表示协商类型不支持时的告警功能。

【使用指导】

如果不指定任何参数，则表示开启或关闭所有类型的IKE告警功能。

如果希望生成并输出某种类型的IKE告警信息，则需要保证IKE的全局告警功能以及相应类型的告警功能均处于开启状态。

【举例】

希望设备在创建IKE隧道时生成并发送告警信息，需要开启以下告警功能：

\# 开启全局IKE告警功能。

\<Sysname\> system-view

Sysname snmp-agent trap enable ike global

\# 开启创建IKE 隧道时的告警功能。

Sysname snmp-agent trap enable ike tunnel-start

**IKE \-- IKE配置命令 \-- tunnel protection**

------------------------------------------------------------------------

**[tunnel protection**]命令用来在隧道接口上应用IPsec安全框架。

**[undo tunnel protection**]命令用来删除指定的IPsec安全框架的应用。

【命令】

**[tunnel protection ipsec profile ***profile-name*]

**[undo tunnel protection**]

【缺省情况】

Tunnel接口下没有引用任何的IPsec安全框架。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[profile-name*]：指定使用的IPsec安全框架，且必须为IKE协商方式的IPsec安全框架。其中，*profile-name*为IPsec安全框架的名字，为1～63个字符的字符串，不区分大小写。

【使用指导】

在隧道接口上应用IPsec安全框架后，隧道两端会通过IKE协商建立IPsec隧道对隧道接口上传输的数据流进行IPsec保护。目前，仅支持对ADVPN隧道报文进行IPsec保护。

【举例】

\# 配置使用IPsec安全框架prf1来保护接口Tunnel1的报文。

\<Sysname\> system-view

Sysname interface tunnel 1 mode advpn gre

Sysname-Tunnel1tunnel protection ipsec profile prf1

【相关命令】

l**interface tunnel**（IP业务命令参考/隧道）

l**display interface tunnel**（IP业务命令参考/隧道）

·**ipsec profile**
