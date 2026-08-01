<!-- CMD-INDEX
  attribute                           | 证书属性组视图          | L47
  ca identifier                       | PKI域视图           | L171
  certificate request entity          | PKI域视图           | L217
  certificate request from            | PKI域视图           | L269
  certificate request mode            | PKI域视图           | L319
  certificate request polling         | PKI域视图           | L393
  certificate request url             | PKI域视图           | L449
  common-name                         | PKI实体视图          | L507
  country                             | PKI实体视图          | L549
  crl check                           | PKI域视图           | L591
  crl url                             | PKI域视图           | L641
  display pki certificate access-control-policy | 任意视图             | L707
  display pki certificate attribute-group | 任意视图             | L801
  display pki certificate domain      | 任意视图             | L951
  display pki certificate request-status | 任意视图             | L1361
  display pki crl                     | 任意视图             | L1483
  fqdn                                | PKI实体视图          | L1651
  ip                                  | PKI实体视图          | L1697
  ldap-server                         | PKI域视图           | L1745
  locality                            | PKI实体视图          | L1815
  organization                        | PKI实体视图          | L1857
  organization-unit                   | PKI实体视图          | L1899
  pki abort-certificate-request       | 系统视图             | L1941
  pki certificate access-control-policy | 系统视图             | L1987
  pki certificate attribute-group     | 系统视图             | L2039
  pki delete-certificate              | 系统视图             | L2093
  pki domain                          | 系统视图             | L2179
  pki entity                          | 系统视图             | L2225
  pki export                          | 系统视图             | L2275
  pki import                          | 系统视图             | L2831
  pki request-certificate             | 系统视图             | L3105
  pki retrieve-certificate            | 系统视图             | L3183
  pki retrieve-crl                    | 系统视图             | L3263
  pki storage                         | 系统视图             | L3315
  pki validate-certificate            | 系统视图             | L3373
  public-key dsa                      | PKI域视图           | L3511
  public-key ecdsa                    | PKI域视图           | L3575
  public-key rsa                      | PKI域视图           | L3641
  root-certificate fingerprint        | PKI域视图           | L3727
  rule                                | 证书访问控制策略视图       | L3803
  source                              | PKI域视图           | L3867
  state                               | PKI实体视图          | L3945
  usage                               | PKI域视图           | L3987
-->

**PKI \-- PKI配置命令 \-- attribute**

------------------------------------------------------------------------

attribute{.commandkeywordsCharChar}命令用来配置属性规则，用于根据证书的颁发者名、主题名以及备用主题名来过滤证书。

**[undo attribute**]命令用来删除证书属性规则。

【命令】

**[attribute**[ *id* { **alt-subject-name** { **fqdn** \| **ip** } \| { **issuer-name** \| **subject-name** } { **dn** \| **fqdn** \| **ip** } } { **ctn** \| **equ** \| **nctn** \| **nequ** } *attribute-value*]]

**[undo** **attribute** *id*]

【缺省情况】

不存在属性规则，即对证书的颁发者名、主题名以及备用主题名没有限制。

【视图】

证书属性组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[id*]：证书属性规则序号，取值范围为1～16。

**[alt-subject-name**]：表示证书备用主题名（Subject Alternative Name）。

**[fqdn**]：指定实体的FQDN。

**[ip**]：指定实体的IP地址。

**[dn**]：指定实体的DN。

**[issuer-name**]：表示证书颁发者名（Issuer Name）。

**[subject-name**]：表示证书主题名（Subject Name）。

**[ctn**]：表示包含操作。

**[equ**]：表示相等操作。

**[nctn**]：表示不包含操作。

**[nequ**]：表示不等操作。

*[attribute-value*]：指定证书属性值，为1～255个字符的字符串，不区分大小写。

【使用指导】

各证书属性中可包含的属性域个数有所不同：

·主题名和颁发者名中均只能包含一个DN，但是均可以同时包含多个FQDN和IP；

·备用主题名中不能包含DN，但是可以同时包含多个FQDN和IP。

不同类型的证书属性域与操作关键字的组合代表了不同的匹配条件，具体如下表所示：

表1-1 对证书属性域的操作涵义

操作

DN

FQDN/IP

**[ctn**]

DN中包含指定的属性值

任意一个FQDN/IP中包含了指定的属性值

**[nctn**]

DN中不包含指定的属性值

所有FQDN/IP中均不包含指定的属性值

**[equ**]

DN等于指定的属性值

任意一个FQDN/IP等于指定的属性值

**[nequ**]

DN不等于指定的属性值

所有FQDN/IP均不等于指定的属性值

如果证书的相应属性中包含了属性规则里指定的属性域，且满足属性规则中定义的匹配条件，则认为该属性与属性规则相匹配。例如：属性规则2中定义，证书的主题名DN中包含字符串abc。如果某证书的主题名的DN中确实包含了字符串abc，则认为该证书的主题名与属性规则2匹配。

只有证书中的相应属性与某属性组中的所有属性规则都匹配上，才认为该证书与此属性组匹配。如果证书中的某属性中没有包含属性规则中指定的属性域，或者不满足属性规则中的匹配条件，则认为该证书与此属性组不匹配。

【举例】

\<Sysname\> system-view

Sysname pki certificate attribute-group mygroup

\# 创建证书属性规则1，定义证书主题名中的DN包含字符串abc。

Sysname-pki-cert-attribute-group-mygroup attribute 1 subject-name dn ctn abc

\# 创建证书属性规则2，定义证书颁发者名中的FQDN不等于字符串abc。

Sysname-pki-cert-attribute-group-mygroup attribute 2 issuer-name fqdn nequ abc

\# 创建证书属性规则3，定义证书主题备用名中的IP地址不等于10.0.0.1。

Sysname-pki-cert-attribute-group-mygroup attribute 3 alt-subject-name ip nequ 10.0.0.1

【相关命令】

·**display pki certificate attribute-group**

·**rule**

**PKI \-- PKI配置命令 \-- ca identifier**

------------------------------------------------------------------------

**[ca identifier**]命令用来指定设备信任的CA的名称。

**[undo ca identifier**]命令用来删除设备信任的CA。

【命令】

**[ca identifier** *name*]

**[undo ca identifier**]

【缺省情况】

未指定设备信任的CA。

【视图】

PKI域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[name*]：设备信任的CA的名称，为1～63个字符的字符串，区分大小写。

【使用指导】

获取CA证书时，必须指定信任的CA的名称，这个名称会被作为SCEP消息的一部分发送给CA服务器。但是一般情况下，CA服务器会忽略收到的SCEP消息中的CA名称的具体内容。但是如果在同一台服务器上配置了两个CA，且它们的URL是相同的，则服务器将根据SCEP消息中的CA名称选择对应的CA。因此，使用此命令指定的CA名称必须与希望获取的CA证书对应的CA名称一致。

【举例】

\# 指定设备信任的CA的名称为new-ca。

\<Sysname\> system-view

Sysname pki domain aaa

Sysname-pki-domain-aaa ca identifier new-ca

**PKI \-- PKI配置命令 \-- certificate request entity**

------------------------------------------------------------------------

**[certificate request entity**]命令用来指定用于申请证书的PKI实体名称。

**[undo** **certificate request entity**]命令用来取消用于申请证书的PKI实体名称。

【命令】

**[certificate request entity** *entity-name*]

**[undo** **certificate request entity**]

【缺省情况】

未指定设备申请证书所使用的PKI实体名称。

【视图】

PKI域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[entity-name*]：用于申请证书的PKI实体的名称，为1～31个字符的字符串，不区分大小写。

【使用指导】

本命令用于在PKI域中指定申请证书的PKI实体。PKI实体描述了申请证书的实体的各种属性（通用名、组织部门、组织、地理区域、省、国家、FQDN、IP），这些属性用于描述PKI实体的身份信息。

一个PKI域中只能指定一个PKI实体名，新配置的PKI实体名会覆盖已有的PKI实体名。

【举例】

\# 指定申请证书的PKI实体的名称为en1。

\<Sysname\> system-view

Sysname pki domain aaa

Sysname-pki-domain-aaa certificate request entity en1

【相关命令】

·**pki entity**

**PKI \-- PKI配置命令 \-- certificate request from**

------------------------------------------------------------------------

**[certificate request from**]命令用来配置证书申请的注册受理机构。

**[undo** **certificate request from**]命令用来删除指定的证书申请注册受理机构。

【命令】

**[certificate request from **[{ **ca** \| **ra** }]]

**[undo certificate request from**]

【缺省情况】

未指定证书申请的注册受理机构。

【视图】

PKI域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ca**]：表示实体从CA申请证书。

**[ra**]：表示实体从RA申请证书。

【使用指导】

选择从CA还是RA申请证书，由CA服务器决定，需要了解CA服务器上由什么机构来受理证书申请。

推荐使用独立运行的RA作为注册受理机构。

【举例】

\# 指定实体从RA申请证书。

\<Sysname\> system-view

Sysname pki domain aaa

Sysname-pki-domain-aaa certificate request from ra

**PKI \-- PKI配置命令 \-- certificate request mode**

------------------------------------------------------------------------

**[certificate request mode**]命令用来配置证书申请方式。

**[undo certificate request mode**]命令用来恢复缺省情况。

【命令】

**[certificate request mode**[ { **auto** [ **password** { **cipher** \| **simple** } *password* ] \| **manual** }]]

**[undo certificate request mode**]

【缺省情况】

证书申请方式为手工方式。

【视图】

PKI域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[auto**]：表示用自动方式申请证书。

**[password**]：指定吊销证书时使用的口令。

**[cipher**]：表示以密文方式设置口令。

**[simple**]：表示以明文方式设置口令。

*[password*]：设置的明文或密文口令，区分大小写。明文口令为1～31个字符的字符串，密文口令为1～73个字符的字符串。

**[manual**]：表示用手工方式申请证书。

【使用指导】

两种申请方式都属于在线申请，具体情况如下：

·如果是自动方式，则设备会在与PKI域关联的应用（例如IKE）需要做身份认证时，自动向证书注册机构发起获取CA证书和申请本地证书的操作。自动方式下，可以指定吊销证书时使用的口令，是否需要指定口令是由CA服务器的策略决定的。

·如果为手工方式，则需要手工完成获取CA证书、申请本地证书的操作。

以明文或密文方式设置的口令，均以密文的方式保存在配置文件中。

【举例】

\# 指定证书申请方式为自动方式。

\<Sysname\> system-view

Sysname pki domain aaa

Sysname-pki-domain-aaa certificate request mode auto

\# 指定证书申请方式为自动方式，并设置吊销证书时使用的口令为明文123456。

\<Sysname\> system-view

Sysname pki domain aaa

Sysname-pki-domain-aaa certificate request mode auto password simple 123456

【相关命令】

·**pki request-certificate**

**PKI \-- PKI配置命令 \-- certificate request polling**

------------------------------------------------------------------------

**[certificate request polling**]命令用来配置证书申请状态的查询周期和最大次数。

**[undo certificate request polling**]命令用来恢复缺省情况。

【命令】

**[certificate request polling **[{ **count** *count* \| **interval** *minutes* }]]

**[undo certificate request polling**[ { **count** \| **interval** }]]

【缺省情况】

证书申请状态的查询周期为20分钟，最多查询50次。

【视图】

PKI域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[count*** count*]：表示证书申请状态的查询次数，取值范围为1～100。

**[interval*** minutes*]：表示证书申请状态的查询周期，取值范围为5～168，单位为分钟。

【使用指导】

设备发送证书申请后，如果CA服务器采用手工方式来签发证书申请，则不会立刻响应设备的申请。这种情况下，设备通过定期向CA服务器发送状态查询消息，能够及时获取到被CA签发的证书。CA签发证书后，设备将通过发送状态查询得到证书，之后停止发送状态查询消息。如果达到最大查询次数时，CA服务器仍未签发证书，则设备停止发送状态查询消息，本次证书申请失败。

如果CA服务器采用自动签发证书的方式，则设备可以立刻得到证书，这种情况下设备不会向CA服务器发送状态查询消息。

【举例】

\# 指定证书申请状态的查询周期为15分钟，最多查询40次。

\<Sysname\> system-view

Sysname pki domain aaa

Sysname-pki-domain-aaa certificate request polling interval 15

Sysname-pki-domain-aaa certificate request polling count 40

【相关命令】

·**display pki certificate request-status**

**PKI \-- PKI配置命令 \-- certificate request url**

------------------------------------------------------------------------

**[certificate request url**]命令用来配置实体通过SCEP进行证书申请的注册受理机构服务器的URL。

**[undo certificate request url**]命令用来删除指定的注册受理机构服务器的URL。

【命令】

**[certificate request url** *url-string* [ **vpn-instance** *vpn-instance-name* ]]

**[undo certificate request url**]

【缺省情况】

未指定注册受理机构服务器的URL。

【视图】

PKI域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[url-string*]：表示证书申请的注册受理机构服务器的URL，为1～511个字符的字符串，区分大小写。

**[vpn-instance*** vpn-instance-name*]：指定注册受理机构服务器所属的VPN。*vpn-instance-name*表示MPLS L3VPN实例名称，为1～31个字符的字符串，区分大小写。若未指定本参数，则表示该注册受理机构服务器属于公网。

【使用指导】

本命令配置的URL内容包括注册受理机构服务器的位置及CGI命令接口脚本位置，格式为http://*server_location/cgi_script_location*。其中，*server_location*是服务器的地址，可以是IPv4地址、 IPv6地址和DNS域名，*cgi_script_location*是注册授权机构（CA或RA ）在服务器主机上的应用程序脚本的路径。

实际可输入的URL长度受命令行允许输入的最大字符数限制。

【举例】

\# 指定实体进行证书申请的注册受理机构服务器的URL为http://169.254.0.100/certsrv/mscep/mscep.dll。

\<Sysname\> system-view

Sysname pki domain aaa

Sysname-pki-domain-aaa certificate request url http://169.254.0.100/certsrv/mscep/mscep.dll

\# 指定实体向VPN中的注册受理机构服务器申请证书，该服务器的URL为http://mytest.net/certsrv/mscep/mscep.dll，所在的MPLS L3VPN的实例名称为vpn1。

\<Sysname\> system-view

Sysname pki domain aaa

Sysname-pki-domain-aaa certificate request url http:// mytest.net /certsrv/mscep/mscep.dll vpn-instance vpn1

**PKI \-- PKI配置命令 \-- common-name**

------------------------------------------------------------------------

**[common-name**]命令用来配置PKI实体的通用名，比如用户名称。

**[undo common-name**]命令用来删除配置的PKI实体的通用名。

【命令】

**[common-name ***common-name-sting*]

**[undo common-name**]

【缺省情况】

未配置PKI实体的通用名。

【视图】

PKI实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[common-name-sting*]：PKI实体的通用名称，为1～63个字符的字符串，区分大小写，不能包含逗号。

【举例】

\# 配置PKI实体en的通用名为test。

\<Sysname\> system-view

Sysname pki entity en

Sysname-pki-entity-en common-name test

**PKI \-- PKI配置命令 \-- country**

------------------------------------------------------------------------

**[country**]命令用来配置PKI实体所属的国家代码。

**[undo country**]命令用来删除配置的PKI实体所属的国家代码。

【命令】

**[country ***country-code-string*]

**[undo country**]

【缺省情况】

未配置PKI实体所属的国家代码。

【视图】

PKI实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[country-code-string*]：PKI实体所属的国家代码，为标准的两字符代码，区分大小写，例如中国为CN。

【举例】

\# 配置PKI实体en所属的国家代码为CN。

\<Sysname\> system-view

Sysname pki entity en

Sysname-pki-entity-en country CN

**PKI \-- PKI配置命令 \-- crl check**

------------------------------------------------------------------------

**[crl check enable**]命令用来使能CRL检查。

**[undo crl check enable**]命令用来禁止CRL检查。

【命令】

**[crl check enable**]

**[undo crl check enable**]

【缺省情况】

CRL检查处于使能状态。

【视图】

PKI域视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

CRL（Certificate Revocation List，证书废除列表）是一个由CA签发的文件，该文件中包含被该CA吊销的所有证书的列表。一个证书有可能在有效期达到之前被CA吊销。使能CRL检查的目的是查看设备上的实体证书或者即将要导入、获取到设备上的实体证书是否已经被CA吊销，若检查结果表明实体证书已被吊销，那么该证书就不被设备信任。

【举例】

\# 禁止CRL检查。

\<Sysname\> system-view

Sysname pki domain aaa

Sysname-pki-domain-aaa undo crl check enable

【相关命令】

·**pki import**

·**pki retrieve-certificate**

·**pki validate-certificate**

**PKI \-- PKI配置命令 \-- crl url**

------------------------------------------------------------------------

**[crl url**]命令用来设置CRL发布点的URL。

**[undo crl url**]命令用来删除CRL发布点的URL。

【命令】

**[crl url ***url-string * **vpn-instance** *vpn-instance-name* ]

**[undo crl url**]

【缺省情况】

未设置CRL发布点的URL。

【视图】

PKI域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[url-string*]：表示CRL发布点的URL，为1～511个字符的字符串，区分大小写。格式为ldap://*server_location*或http://*server_location*，其中*server_location*可以为IP地址和DNS域名。

**[vpn-instance*** vpn-instance-name*]：指定CRL发布点所属的VPN。*vpn-instance-name*表示MPLS L3VPN实例名称，为1～31个字符的字符串，区分大小写。若未指定本参数，则表示该CRL发布点属于公网。

【使用指导】

如果CRL检查处于使能状态，则进行CRL检查之前，需要首先从PKI域指定的CRL发布点获取CRL。若PKI域中未配置CRL发布点的URL时，从该待验证的证书中获取发布点信息：优先获取待验证的证书中记录的发布点，如果待验证的证书中没有记录发布点，则获取CA证书中记录的发布点（若待验证的证书为CA证书，则获取上一级CA证书中记录的发布点）。如果无法通过任何途径得到发布点，则通过SCEP协议获取CRL。

若配置了LDAP格式的CRL发布点URL，则表示要通过LDAP协议获取CRL。若该URL中未携带主机名，则需要根据PKI域中配置的LDAP服务器地址信息来得到完整的LDAP发布点URL。

实际可输入的URL长度受命令行允许输入的最大字符数限制。

【举例】

\# 指定CRL发布点的URL为http://169.254.0.30。

\<Sysname\> system-view

Sysname pki domain aaa

Sysname-pki-domain-aaa crl url http://169.254.0.30

\# 指定CRL发布点的URL为ldap://169.254.0.30，所在的MPLS L3VPN的实例名称为vpn1。

\<Sysname\> system-view

Sysname pki domain 1

Sysname-pki-domain-1 crl url ldap://169.254.0.30 vpn-instance vpn1

【相关命令】

·**ldap-server**

·**pki retrieve-crl**

**PKI \-- PKI配置命令 \-- display pki certificate access-control-policy**

------------------------------------------------------------------------

**[display pki certificate access-control-policy**]命令用来显示证书访问控制策略的配置信息。

【命令】

**[display pki certificate access-control-policy** [ *policy-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[policy-name*]：指定证书访问控制策略名称，为1～31个字符的字符串，不区分大小写。

【使用指导】

若不指定证书访问控制策略的名称，则显示所有证书访问控制策略的配置信息。

【举例】

\# 显示证书访问控制策略mypolicy的配置信息。

\<Sysname\> display pki certificate access-control-policy mypolicy

 Access control policy name: mypolicy

     Rule 1  deny    mygroup1

     Rule 2  permit  mygroup2

\# 显示所有证书属性访问控制策略的配置信息。

\<Sysname\> display pki certificate access-control-policy

 Total PKI certificate access control policies: 2

 Access control policy name: mypolicy1

     Rule 1  deny    mygroup1

     Rule 2  permit  mygroup2

 Access control policy name: mypolicy2

     Rule 1  deny    mygroup3

     Rule 2  permit  mygroup4

表1-2 display pki certificate access-control-policy命令显示信息描述表

字段

描述

Total PKI certificate access control policies

PKI证书访问控制策略的总数

Access control policy name

证书访问控制策略名

Rule *number*

访问控制规则编号

permit

当证书的属性与属性组里定义的属性匹配时，认为该证书有效，通过了访问控制策略的检测

deny

当证书的属性与属性组里定义的属性匹配时，认为该证书无效，未通过访问控制策略的检测

【相关命令】

·**pki certificate access-control-policy**

·**rule**

**PKI \-- PKI配置命令 \-- display pki certificate attribute-group**

------------------------------------------------------------------------

**[display pki certificate attribute-group**]命令用来显示证书属性组的配置信息。

【命令】

**[display pki certificate attribute-group ** *group-name* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[group-name*]：指定证书属性组名，为1～31个字符的字符串，不区分大小写。

【使用指导】

若不指定证书属性组的名字，则显示所有证书属性组的配置信息。

【举例】

\# 显示证书属性组mygroup的信息。

\<Sysname\> display pki certificate attribute-group mygroup

 Attribute group name: mygroup

      Attribute  1 subject-name     dn    ctn   abc

      Attribute  2 issuer-name      fqdn  nctn  app

\# 显示所有证书属性组的信息。

\<Sysname\> display pki certificate attribute-group

 Total PKI certificate attribute groups: 2.

 Attribute group name: mygroup1

      Attribute  1 subject-name     dn    ctn   abc

      Attribute  2 issuer-name      fqdn  nctn  app

Attribute group name: mygroup2

      Attribute  1 subject-name     dn    ctn   def

      Attribute  2 issuer-name      fqdn  nctn  fqd

表1-3 display pki certificate attribute-group命令显示信息描述表

字段

描述

Total PKI certificate attribute groups

PKI证书属性组的总数

Attribute group name

证书属性组名称

Attribute *number*

属性规则编号

subject-name

证书主题名

alt-subject-name

证书备用主题名

issuer-name

证书颁发者名

dn

实体的DN

fqdn

实体的FQDN

ip

实体的IP地址

ctn

表示包含操作

nctn

表示不包含操作

equ

表示等于操作

nequ

表示不等操作

Attribute  1 subject-name     dn    ctn   abc

属性规则内容，包括以下参数：

·alt-subject-name：表示证书备用主题名

·issuer-name：表示证书颁发者名

·subject-name：表示证书主题名

·fqdn：表示实体的FQDN

·ip：表示实体的IP地址

·dn：表示实体的DN

·ctn：表示包含操作

·equ：表示相等操作

·nctn：表示不包含操作

·nequ：表示不等操作

【相关命令】

·**attribute**

·**pki certificate attribute-group**

**PKI \-- PKI配置命令 \-- display pki certificate domain**

------------------------------------------------------------------------

**[display pki certificate domain**]命令用来显示证书的内容。

【命令】

**[display pki certificate**[ **domain** *domain-name* { **ca** \| **local** \| **peer** [ **serial** *serial-num* ] }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[domain-name*]：显示指定证书所在的PKI域的名称，为1～31个字符的字符串，不区分大小写，不能包括"\~"、"\*"、"\"、"[\|]"、":"、"."、"\<"、"\>"、"\""和"\'"。

**[ca**]：显示CA证书。

**[local**]：显示本地证书。

**[peer**]：显示对端证书。

**[serial ***serial-num*]：指定要显示的对端证书的序列号。

【使用指导】

·显示CA证书时，会显示此PKI域中所有CA证书的详细信息，若PKI域中存在RA证书，则同时显示RA证书的详细信息。

·显示本地证书时，会显示此PKI域中所有本地证书的详细信息。

·显示对端证书时，如果不指定序列号，将显示所有对端证书的简要信息；如果指定序列号，将显示该序号对应的指定对端证书的详细信息。

【举例】

\# 显示PKI域aaa中的CA证书。

\<Sysname\> display pki certificate domain aaa ca

Certificate:

    Data:

        Version: 1 (0x0)

Serial Number:

            5c:72:dc:c4:a5:43:cd:f9:32:b9:c1:90:8f:dd:50:f6

        Signature Algorithm: sha1WithRSAEncryption

        Issuer: C=cn, O=docm, OU=rnd, CN=rootca

        Validity

            Not Before: Jan  6 02:51:41 2011 GMT

            Not After : Dec  7 03:12:05 2013 GMT

        Subject: C=cn, O=ccc, OU=ppp, CN=rootca

        Subject Public Key Info:

            Public Key Algorithm: rsaEncryption

                Public-Key: (1024 bit)

Modulus:

                    00:c4:fd:97:2c:51:36:df:4c:ea:e8:c8:70:66:f0:

                    28:98:ec:5a:ee:d7:35:af:86:c4:49:76:6e:dd:40:

                    4a:9e:8d:c0:cb:d9:10:9b:61:eb:0c:e0:22:ce:f6:

                    57:7c:bb:bb:1b:1d:b6:81:ad:90:77:3d:25:21:e6:

                    7e:11:0a:d8:1d:3c:8e:a4:17:1e:8c:38:da:97:f6:

                    6d:be:09:e3:5f:21:c5:a0:6f:27:4b:e3:fb:9f:cd:

                    c1:91:18:ff:16:ee:d8:cf:8c:e3:4c:a3:1b:08:5d:

                    84:7e:11:32:5f:1a:f8:35:25:c0:7e:10:bd:aa:0f:

52:db:7b:cd:5d:2b:66:5a:fb

                Exponent: 65537 (0x10001)

    Signature Algorithm: sha1WithRSAEncryption

        6d:b1:4e:d7:ef:bb:1d:67:53:67:d0:8f:7c:96:1d:2a:03:98:

3b:48:41:08:a4:8f:a9:c1:98:e3:ac:7d:05:54:7c:34:d5:ee:

        09:5a:11:e3:c8:7a:ab:3b:27:d7:62:a7:bb:bc:7e:12:5e:9e:

        4c:1c:4a:9f:d7:89:ca:20:46:de:c5:b3:ce:36:ca:5e:6e:dc:

        e7:c6:fe:3f:c5:38:dd:d5:a3:36:ad:f4:3d:e6:32:7f:48:df:

        07:f0:a2:32:89:86:72:22:cd:ed:e5:0f:95:df:9c:75:71:e7:

        fe:34:c5:a0:64:1c:f0:5c:e4:8f:d3:00:bd:fa:90:b6:64:d8:

        88:a6

\# 显示PKI域aaa中的本地证书。

\<Sysname\> display pki certificate domain aaa local

Certificate:

    Data:

        Version: 3 (0x2)

        Serial Number:

            bc:05:70:1f:0e:da:0d:10:16:1e

        Signature Algorithm: sha256WithRSAEncryption

        Issuer: C=CN, O=sec, OU=software, CN=ipsec

Validity

            Not Before: Jan  7 20:05:44 2011 GMT

            Not After : Jan  7 20:05:44 2012 GMT

        Subject: O=OpenCA Labs, OU=Users, CN=fips fips-sec

        Subject Public Key Info:

            Public Key Algorithm: rsaEncryption

                Public-Key: (1024 bit)

Modulus:

                    00:b2:38:ad:8c:7d:78:38:37:88:ce:cc:97:17:39:

52:e1:99:b3:de:73:8b:ad:a8:04:f9:a1:f9:0d:67:

                    d8:95:e2:26:a4:0b:c2:8c:63:32:5d:38:3e:fd:b7:

                    4a:83:69:0e:3e:24:e4:ab:91:6c:56:51:88:93:9e:

                    12:a4:30:ad:ae:72:57:a7:ba:fb:bc:ac:20:8a:21:

                    46:ea:e8:93:55:f3:41:49:e9:9d:cc:ec:76:13:fd:

a5:8d:cb:5b:45:08:b7:d1:c5:b5:58:89:47:ce:12:

bd:5c:ce:b6:17:2f:e0:fc:c0:3e:b7:c4:99:31:5b:

8a:f0:ea:02:fd:2d:44:7a:67

                Exponent: 65537 (0x10001)

        X509v3 extensions:

            X509v3 Basic Constraints:

                CA:FALSE

            Netscape Cert Type:

                SSL Client, S/MIME

            X509v3 Key Usage:

                Digital Signature, Non Repudiation, Key Encipherment

            X509v3 Extended Key Usage:

                TLS Web Client Authentication, E-mail Protection, Microsoft Smartcardlogin

            Netscape Comment:

                User Certificate of OpenCA Labs

            X509v3 Subject Key Identifier:

                91:95:51:DD:BF:4F:55:FA:E4:C4:D0:10:C2:A1:C2:99:AF:A5:CB:30

            X509v3 Authority Key Identifier:

                keyid:DF:D2:C9:1A:06:1F:BC:61:54:39:FE:12:C4:22:64:EB:57:3B:11:9F

            X509v3 Subject Alternative Name:

                email:fips@ccc.com

            X509v3 Issuer Alternative Name:

                email:pki@openca.org

            Authority Information Access:

                CA Issuers - URI:http://titan/pki/pub/cacert/cacert.crt

                OCSP - URI:http://titan:2560/

                1.3.6.1.5.5.7.48.12 - URI:http://titan:830/

            X509v3 CRL Distribution Points:

                Full Name:

                  URI:http://titan/pki/pub/crl/cacrl.crl

    Signature Algorithm: sha256WithRSAEncryption

        94:ef:56:70:48:66:be:8f:9d:bb:77:0f:c9:f4:65:77:e3:bd:

ea:9a:b8:24:ae:a1:38:2d:f4:ab:e8:0e:93:c2:30:33:c8:ef:

        f5:e9:eb:9d:37:04:6f:99:bd:b2:c0:e9:eb:b1:19:7e:e3:cb:

        95:cd:6c:b8:47:e2:cf:18:8d:99:f4:11:74:b1:1b:86:92:98:

        af:a2:34:f7:1b:15:ee:ea:91:ed:51:17:d0:76:ec:22:4c:56:

        da:d6:d1:3c:f2:43:31:4f:1d:20:c8:c2:c3:4d:e5:92:29:ee:

        43:c6:d7:72:92:e8:13:87:38:9a:9c:cd:54:38:b2:ad:ba:aa:

f9:a4:68:b5:2a:df:9a:31:2f:42:80:0c:0c:d9:6d:b3:ab:0f:

dd:a0:2c:c0:aa:16:81:aa:d9:33:ca:01:75:94:92:44:05:1a:

        65:41:fa:1e:41:b5:8a:cc:2b:09:6e:67:70:c4:ed:b4:bc:28:

        04:50:a6:33:65:6d:49:3c:fc:a8:93:88:53:94:4c:af:23:64:

        cb:af:e3:02:d1:b6:59:5f:95:52:6d:00:00:a0:cb:75:cf:b4:

        50:c5:50:00:65:f4:7d:69:cc:2d:68:a4:13:5c:ef:75:aa:8f:

        3f:ca:fa:eb:4d:d5:5d:27:db:46:c7:f4:7d:3a:b2:fb:a7:c9:

        de:18:9d:c1

\# 显示PKI域aaa中的所有对端证书的简要信息。

\<Sysname\> display pki certificate domain aaa peer

Total peer certificates: 1

Serial Number: 9a0337eb2156ba1f5476e4d754a5a9f7

Subject  Name: CN=sldsslserver

\# 显示PKI域aaa中的一个特定序号的对端证书的详细信息。

\<Sysname\> display pki certificate domain aaa peer serial 9a0337eb2156ba1f5476e4d754a5a9f7

Certificate:

    Data:

        Version: 3 (0x2)

        Serial Number:

            9a:03:37:eb:21:56:ba:1f:54:76:e4:d7:54:a5:a9:f7

Signature Algorithm: sha1WithRSAEncryption

        Issuer: C=cn, O=ccc, OU=sec, CN=ssl

        Validity

            Not Before: Oct 15 01:23:06 2010 GMT

            Not After : Jul 26 06:30:54 2012 GMT

        Subject: CN=sldsslserver

        Subject Public Key Info:

            Public Key Algorithm: rsaEncryption

                Public-Key: (1024 bit)

                Modulus:

                    00:c2:cf:37:76:93:29:5e:cd:0e:77:48:3a:4d:0f:

a6:28:a4:60:f8:31:56:28:7f:81:e3:17:47:78:98:

                    68:03:5b:72:f4:57:d3:bf:c5:30:32:0d:58:72:67:

                    04:06:61:08:3b:e9:ac:53:b9:e7:69:68:1a:23:f2:

                    97:4c:26:14:c2:b5:d9:34:8b:ee:c1:ef:af:1a:f4:

39:da:c5:ae:ab:56:95:b5:be:0e:c3:46:35:c1:52:

29:9c:b7:46:f2:27:80:2d:a4:65:9a:81:78:53:d4:

                    ca:d3:f5:f3:92:54:85:b3:ab:55:a5:03:96:2b:19:

                    8b:a3:4d:b2:17:08:8d:dd:81

                Exponent: 65537 (0x10001)

        X509v3 extensions:

            X509v3 Authority Key Identifier:

keyid:9A:83:29:13:29:D9:62:83:CB:41:D4:75:2E:52:A1:66:38:3C:90:11

            X509v3 Key Usage: critical

                Digital Signature, Non Repudiation, Key Encipherment, Data Encipherment, Key Agreement

            Netscape Cert Type:

                SSL Server

            X509v3 Subject Alternative Name:

                DNS:docm.com

            X509v3 Subject Key Identifier:

                3C:76:95:9B:DD:C2:7F:5F:98:83:B7:C7:A0:F8:99:1E:4B:D7:2F:26

            X509v3 CRL Distribution Points:

                Full Name:

                  URI:http://s03130.ccc.sec.com:447/ssl.crl

    Signature Algorithm: sha1WithRSAEncryption

        61:2d:79:c7:49:16:e3:be:25:bb:8b:70:37:31:32:e5:d3:e3:

        31:2c:2d:c1:f9:bf:50:ad:35:4b:c1:90:8c:65:79:b6:5f:59:

36:24:c7:14:63:44:17:1e:e4:cf:10:69:fc:93:e9:70:53:3c:

        85:aa:40:7e:b5:47:75:0f:f0:b2:da:b4:a5:50:dd:06:4a:d5:

        17:a5:ca:20:19:2c:e9:78:02:bd:19:77:da:07:1a:42:df:72:

        ad:07:7d:e5:16:d6:75:eb:6e:06:58:ee:76:31:63:db:96:a2:

ad:83:b6:bb:ba:4b:79:59:9d:59:6c:77:59:5b:d9:07:33:a8:

f0:a5

表1-4 display pki certificate命令显示信息描述表

字段

描述

Version

证书版本号

Serial Number

证书序列号

Signature Algorithm

签名算法

Issuer

证书颁发者

Validity

证书有效期

Subject

证书所属的实体信息

Subject Public Key Info

证书所属的实体的公钥信息

X509v3 extensions

X.509版本3格式的证书扩展属性

【相关命令】

·**pki domain**

·**pki retrieve-certificate**

**PKI \-- PKI配置命令 \-- display pki certificate request-status**

------------------------------------------------------------------------

**[display pki certificate request-status**]命令用来显示证书的申请状态。

【命令】

**[display pki certificate request-status ** **domain** *domain-name* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[domain ***domain-name*]：指定证书所在的PKI域的名称，为1～31个字符的字符串，不区分大小写，不能包括"\~"、"\*"、"\"、"[\|]"、":"、"."、"\<"、"\>"、"\""和"\'"。

【使用指导】

若不指定PKI域的名称，则显示所有PKI域的证书申请状态。

【举例】

\# 显示PKI域aaa的证书申请状态。

\<Sysname\> display pki certificate request-status domain aaa

Certificate Request Transaction 1

    Domain name: aaa

    Status: Pending

    Key usage: General

    Remain polling attempts: 10

    Next polling attempt after : 1191 seconds

\# 显示所有PKI域的证书申请状态。

\<Sysname\> display pki certificate request-status

Certificate Request Transaction 1

    Domain name: domain1

    Status: Pending

    Key usage: General

    Remain polling attempts: 10

    Next polling attempt after : 1191 seconds

Certificate Request Transaction 2

    Domain name: domain2

    Status: Pending

    Key usage: Signature

    Remain polling attempts: 10

    Next polling attempt after : 188 seconds

表1-1 display pki certificate request命令显示信息描述表

字段

描述

Certificate Request Transaction *number*

证书申请任务的编号，从1开始顺序编号

Domain name

PKI域名

Status

证书申请状态。目前，仅有一种取值Pending，表示等待

Key usage

证书用途，包括以下取值：

·General：表示通用，既可以用于加密也可以用于签名

·Signature：表示用于签名

·Encryption：表示用于加密

Remain polling attempts

剩余的证书申请状态的查询次数

Next polling attempt after

当前到下次查询证书申请状态的时间间隔，单位为秒

【相关命令】

l**certificate request polling**

l**pki domain**

l**pki retrieve-certificate**

**PKI \-- PKI配置命令 \-- display pki crl**

------------------------------------------------------------------------

**[display pki crl domain**]命令用来显示存储在本地的CRL。

【命令】

**[display pki crl** **domain** *domain-name*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[domain** *domain-name*]：指定CRL所在的PKI域的名称，为1～31个字符的字符串，不区分大小写，不能包括"\~"、"\*"、"\"、"[\|]"、":"、"."、"\<"、"\>"、"\""和"\'"。

【使用指导】

用户可以通过该命令查看证书吊销列表，看所需的证书是否已经被吊销。

【举例】

\# 显示存储在本地的CRL。

\<Sysname\> display pki crl domain aaa

Certificate Revocation List (CRL):

        Version 2 (0x1)

        Signature Algorithm: sha1WithRSAEncryption

        Issuer: /C=cn/O=docm/OU=sec/CN=therootca

        Last Update: Apr 28 01:42:13 2011 GMT

        Next Update: NONE

        CRL extensions:

            X509v3 CRL Number:

                6

            X509v3 Authority Key Identifier:

                keyid:49:25:DB:07:3A:C4:8A:C2:B5:A0:64:A5:F1:54:93:69:14:51:11:EF

Revoked Certificates:

    Serial Number: CDE626BF7A44A727B25F9CD81475C004

        Revocation Date: Apr 28 01:37:52 2011 GMT

        CRL entry extensions:

            Invalidity Date:

                Apr 28 01:37:49 2011 GMT

    Serial Number: FCADFA81E1F56F43D3F2D3EF7EB56DE5

        Revocation Date: Apr 28 01:33:28 2011 GMT

        CRL entry extensions:

            Invalidity Date:

                Apr 28 01:33:09 2011 GMT

Signature Algorithm: sha1WithRSAEncryption

        57:ac:00:3e:1e:e2:5f:59:62:04:05:9b:c7:61:58:2a:df:a4:

        5c:e5:c0:14:af:c8:e7:de:cf:2a:0a:31:7d:32:da:be:cd:6a:

        36:b5:83:e8:95:06:bd:b4:c0:36:fe:91:7c:77:d9:00:0f:9e:

        99:03:65:9e:0c:9c:16:22:ef:4a:40:ec:59:40:60:53:4a:fc:

        8e:47:57:23:e0:75:0a:a4:1c:0e:2f:3d:e0:b2:87:4d:61:8a:

4a:cb:cb:37:af:51:bd:53:78:76:a1:16:3d:0b:89:01:91:61:

        52:d0:6f:5c:09:59:15:be:b8:68:65:0c:5d:1b:a1:f8:42:04:

        ba:aa

表1-5 display pki crl domain显示信息描述表

字段

描述

Version

CRL版本号

Signature Algorithm

CA签名该CRL采用的签名算法

Issuer

颁发该CRL的CA证书名称

Last Update

上次更新CRL的时间

Next Update

下次更新CRL的时间

CRL extensions

CRL扩展属性

X509v3 CRL Number

X509版本3格式的CRL序号

X509v3 Authority Key Identifier

X509版本3格式的签发该CRL的CA的标识符

keyid

公钥标识符

一个CA可能有多个密钥对，该字段用于标识CA用哪个密钥对对该CRL进行签名

Revoked Certificates

撤销的证书信息

Serial Number

被吊销证书的序列号

Revocation Date

证书被吊销的日期

CRL entry extensions:

CRL项目扩展属性

Signature Algorithm:

签名算法以及签名数据

【相关命令】

·**pki retrieve-crl**

**PKI \-- PKI配置命令 \-- fqdn**

------------------------------------------------------------------------

**[fqdn**]命令用来配置PKI实体的FQDN。

**[undo fqdn**]命令用来删除配置的PKI实体的FQDN。

【命令】

**[fqdn ***fqdn-name-string*]

**[undo fqdn**]

【缺省情况】

未配置PKI实体的FQDN。

【视图】

PKI实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[fqdn-name-string*]：PKI实体的FQDN，为1～255个字符的字符串，区分大小写。

【使用指导】

FQDN是实体在网络中的唯一标识，由一个主机名和一个域名组成，形式为*hostname*@*domainname*。

【举例】

\# 配置PKI实体en的FQDN为abc@pki.domain.com。

\<Sysname\> system-view

Sysname pki entity en

Sysname-pki-entity-en fqdn abc@pki.domain.com

**PKI \-- PKI配置命令 \-- ip**

------------------------------------------------------------------------

**[ip**]命令用来配置PKI实体的IP地址。

**[undo ip**]命令用来删除配置的PKI实体的IP地址。

【命令】

**[ip **[{ *ip-address* \| **interface** *interface-type interface-number* }]]

**[undo ip**]

【缺省情况】

未配置PKI实体的IP地址。

【视图】

PKI实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：指定PKI实体的IPv4地址。

**[interface ***interface-type interface-numbe*]：指定接口的主IPv4地址作为PKI实体的IPv4地址。*interface-type interface-number*表示接口类型及接口编号。

【使用指导】

通过本命令，可以直接指定PKI实体的IP地址，也可以指定设备上某接口的主IPv4地址作为PKI实体的IP地址。如果指定使用某接口的IP地址，则不要求本配置执行时该接口上已经配置了IP地址，只要设备申请证书时，该接口上配置了IP地址，就可以直接使用该地址作为PKI实体身份的一部分。

【举例】

\# 配置PKI实体en的IP地址为192.168.0.2。

\<Sysname\> system-view

Sysname pki entity en

Sysname-pki-entity-en ip 192.168.0.2

**PKI \-- PKI配置命令 \-- ldap-server**

------------------------------------------------------------------------

**[ldap-server**]命令用来指定LDAP服务器。

**[undo ldap-server**]命令用来删除指定的LDAP服务器。

【命令】

**[ldap-server host** *hostname* [ **port** *port-number*   **vpn-instance** *vpn-instance-name* ]]

**[undo ldap-server**]

【缺省情况】

未指定LDAP服务器。

【视图】

PKI域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[host ***host-name*]：LDAP服务器的主机名，为1～255个字符的字符串，区分大小写，支持IPv4与IPv6地址的表示方法以及DNS域名的表示方法。

**[port** *port-number*]：LDAP服务器的端口号，取值范围为1～65535，缺省值为389。

**[vpn-instance*** vpn-instance-name*]：指定LDAP服务器所属的VPN。*vpn-instance-name*表示MPLS L3VPN实例名称，为1～31个字符的字符串，区分大小写。若未指定本参数，则表示该LDAP服务器属于公网。

【使用指导】

以下两种情况下，需要配置LDAP服务器：

·通过LDAP协议获取本地证书或对端证书时，需要指定LDAP服务器。

·通过LDAP协议获取CRL时，若PKI域中配置的LDAP格式的CRL发布点URL中未携带主机名，则需要根据此处配置的LDAP服务器地址来得到完整的LDAP发布点URL。

在一个PKI域中，只能指定一个LDAP服务器，若重复执行本命令，最新的配置生效。

【举例】

\# 指定LDAP服务器的IP地址为10.0.0.1。

\<Sysname\> system-view

Sysname pki domain aaa

Sysname-pki-domain-aaa ldap-server host 10.0.0.1

\# 指定LDAP服务器，IP地址为10.0.0.11，端口号为333，所在的MPLS L3VPN的实例名称为vpn1。

\<Sysname\> system-view

Sysname pki domain aaa

Sysname-pki-domain-aaa ldap-server host 10.0.0.11 port 333 vpn-instance vpn1

【相关命令】

·**pki retrieve-certificate**

·**pki retrieve-crl**

**PKI \-- PKI配置命令 \-- locality**

------------------------------------------------------------------------

**[locality**]命令用来配置PKI实体所在的地理区域名称，比如城市名称。

**[undo locality**]命令用来删除配置的PKI实体所在的地理区域名称。

【命令】

**[locality ***locality-name*]

**[undo locality**]

【缺省情况】

未配置PKI实体所在的地理区域名称。

【视图】

PKI实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[locality-name*]：PKI实体所在的地理区域的名称，为1～63个字符的字符串，区分大小写，不能包含逗号。

【举例】

\# 配置PKI实体en所在地理区域的名称为pukras。

\<Sysname\> system-view

Sysname pki entity en

Sysname-pki-entity-en locality pukras

**PKI \-- PKI配置命令 \-- organization**

------------------------------------------------------------------------

**[organization**]命令用来配置PKI实体所属组织的名称。

**[undo organization**]命令用来删除配置的PKI实体所属组织的名称。

【命令】

**[organization*** org-name*]

**[undo organization**]

【缺省情况】

未配置PKI实体所属组织名称。

【视图】

PKI实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[org-name*]：PKI实体所属的组织名称，为1～63个字符的字符串，区分大小写，不能包含逗号。

【举例】

\# 配置PKI实体en所属的组织名称为abc。

\<Sysname\> system-view

Sysname pki entity en

Sysname-pki-entity-en organization abc

**PKI \-- PKI配置命令 \-- organization-unit**

------------------------------------------------------------------------

**[organization-unit**]命令用来指定实体所属的组织部门的名称。

**[undo organization-unit**]命令用来删除实体所属的组织部门的名称。

【命令】

**[organization-unit*** org-unit-name*]

**[undo organization-unit**]

【缺省情况】

未配置PKI实体所属组织部门的名称。

【视图】

PKI实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[org-unit-name*]：PKI实体所属组织部门的名称，为1～63个字符的字符串，区分大小写，不能包含逗号。使用该参数可在同一个单位内区分不同部门的PKI实体。

【举例】

\# 配置PKI实体en所属组织部门的名称为rdtest。

\<Sysname\> system-view

Sysname pki entity en

Sysname-pki-entity-en organization-unit rdtest

**PKI \-- PKI配置命令 \-- pki abort-certificate-request**

------------------------------------------------------------------------

**[pki abort-certificate-request**]命令用来停止证书申请过程。

【命令】

**[pki abort-certificate-request**]** domain*** domain-name*

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[domain***domain-name*]：指定证书所在的PKI域的名称，为1～31个字符的字符串，不区分大小写，不能包括"\~"、"\*"、"\"、"[\|]"、":"、"."、"\<"、"\>"、"\""和"\'"。

【使用指导】

用户在证书申请时，可能由于某种原因需要改变证书申请的一些参数，比如通用名、国家代码、FQDN等，而此时证书申请正在运行，为了新的申请不与之前的申请发生冲突，建议先停止之前的申请程序，再进行新的申请。

【举例】

\# 停止证书申请过程。

\<Sysname\> system-view

Sysname pki abort-certificate- request domain 1

The certificate request is in process.

Confirm to abort it? [Y/N:y]

【相关命令】

·**display pki certificate request-status**

·{.TerminalDisplayshading}**pki request-certificate domain**

**PKI \-- PKI配置命令 \-- pki certificate access-control-policy**

------------------------------------------------------------------------

**[pki certificate access-control-policy**]命令用来创建证书访问控制策略，并进入证书访问控制策略视图。如果指定的证书访问控制策略已存在，则直接进入其视图。

**[undo pki certificate access-control-policy**]命令用来删除指定的证书访问控制策略。

【命令】

**[pki certificate access-control-policy ***policy-name*]

**[undo pki certificate access-control-policy ***policy-name*]

【缺省情况】

不存在证书访问控制策略。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：表示证书访问控制策略名称，为1～31个字符的字符串，不区分大小写。

【使用指导】

一个证书访问控制策略中可以定义多个证书属性的访问控制规则。

【举例】

\# 配置一个名称为mypolicy的证书访问控制策略，并进入证书访问控制策略视图。

\<Sysname\> system-view

Sysname pki certificate access-control-policy mypolicy

Sysname-pki-cert-acp-mypolicy

【相关命令】

·**display pki certificate access-control-policy**

·**rule**

**PKI \-- PKI配置命令 \-- pki certificate attribute-group**

------------------------------------------------------------------------

**[pki certificate attribute-group**]命令用来创建证书属性组并进入证书属性组视图。如果指定的证书属性组已存在，则直接进入其视图。

**[undo pki certificate attribute-group**]命令用来删除指定的证书属性组。

【命令】

**[pki certificate attribute-group ***group-name*]

**[undo pki certificate attribute-group** *group-name* ]

【缺省情况】

不存在证书属性组。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-name*]：证书属性组名称，为1～31个字符的字符串，不区分大小写。

【使用指导】

一个证书属性组就是一系列证书属性规则（通过**attribute**命令配置）的集合，这些属性规则定义了对证书的颁发者名、主题名以及备用主题名进行过滤的匹配条件。当证书属性组下没有任何属性规则时，则认为对证书的属性没有任何限制。

【举例】

\# 创建一个名为mygroup的证书属性组，并进入证书属性组视图。

\<Sysname\> system-view

Sysname pki certificate attribute-group mygroup

Sysname-pki-cert-attribute-group-mygroup

【相关命令】

·**attribute**

·**display pki certificate attribute-group**

·**rule**

**PKI \-- PKI配置命令 \-- pki delete-certificate**

------------------------------------------------------------------------

**[pki delete-certificate**]命令用来删除PKI域中的证书。

【命令】

**[pki delete-certificate**[ **domain** *domain*-*name* { **ca** \| **local** \| **peer** [ **serial** *serial-num* ] }]]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[domain ***domain*-*name*]：证书所在的PKI域的名称，为1～31个字符的字符串，不区分大小写，不能包括"\~"、"\*"、"\"、"[\|]"、":"、"."、"\<"、"\>"、"\""和"\'"。

**[ca**]：表示删除CA证书。

**[local**]：表示删除本地证书。

**[peer**]：表示删除对端证书。

**[serial*** serial-num*]：表示通过指定序列号删除一个指定的对端证书。*serial-num*为对端证书的序列号，为1～127个字符的字符串，不区分大小写。在每个CA签发的证书范围内，序列号可以唯一标识一个证书。如果不指定本参数，则表示删除本PKI域中的所有对端证书。

【使用指导】

删除CA证书时将同时删除所在PKI域中的本地证书和所有对端证书，以及CRL。

如果需要删除指定的对端证书，则需要首先通过**display pki certificate**命令查看本域中已有的对端证书的序列号，然后再通过指定序列号的方式删除该对端证书。

【举例】

\# 删除PKI域aaa中的CA证书。

\<Sysname\> system-view

Sysname pki delete-certificate domain aaa ca

Local certificates, peer certificates and CRL will also be deleted while deleting the CA certificate.

Confirm to delete the CA certificate? [Y/N:y]

Sysname

\# 删除PKI域aaa中的本地证书。

\<Sysname\> system-view

Sysname pki delete-certificate domain aaa local

Sysname

\# 删除PKI域aaa中的所有对端证书。

\<Sysname\> system-view

Sysname pki delete-certificate domain aaa peer

Sysname

\# 首先查看PKI域aaa中的对端证书，然后通过指定序列号的方式删除对端证书。

\<Sysname\> system-view

Sysname display pki certificate domain aaa peer

Total peer certificates: 1

Serial Number: 9a0337eb2156ba1f5476e4d754a5a9f7

Subject  Name: CN=abc

Sysname pki delete-certificate domain aaa peer serial 9a0337eb2156ba1f5476e4d754a5a9f7

【相关命令】

·**display pki certificate**

**PKI \-- PKI配置命令 \-- pki domain**

------------------------------------------------------------------------

**[pki domain**]命令用来创建PKI域，并进入PKI域视图。如果指定的PKI域已存在，则直接进入其视图。

**[undo pki domain**]命令用来删除指定的PKI域。

【命令】

**[pki domain ***domain-name*]

**[undo pki domain ***domain-name*]

【缺省情况】

不存在PKI域。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[domain-name*]：PKI域名，为1～31个字符的字符串，不区分大小写，不能包括"\~"、"\*"、"\"、"[\|]"、":"、"."、"\<"、"\>"、"\""和"\'"。

【使用指导】

删除PKI域的同时，会将该域相关的证书和CRL都删除掉，因此请慎重操作。

【举例】

\# 创建PKI域aaa并进入其视图。

\<Sysname\> system-view

Sysname pki domain aaa

Sysname-pki-domain-aaa

**PKI \-- PKI配置命令 \-- pki entity**

------------------------------------------------------------------------

**[pki entity**]命令用来创建PKI实体，并进入PKI实体视图。如果指定的PKI实体已存在，则直接进入其视图。

**[undo pki entity**]命令用来删除指定的PKI实体。

【命令】

**[pki entity ***entity-name*]

**[undo pki entity** *entity-name*]

【缺省情况】

无PKI实体存在。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[entity-name*]：PKI实体的名称，为1～31个字符的字符串，不区分大小写。

【使用指导】

在PKI实体视图下可配置PKI实体的各种属性（通用名、组织部门、组织、地理区域、省、国家、FQDN、IP），这些属性用于描述PKI实体的身份信息。当申请证书时，PKI实体的信息将作为证书中主题（Subjuct）部分的内容。

【举例】

\# 创建名称为en的PKI实体，并进入该实体视图。

\<Sysname\> system-view

Sysname pki entity en

Sysname-pki-entity-en

【相关命令】

·**pki domain**

**PKI \-- PKI配置命令 \-- pki export**

------------------------------------------------------------------------

**[pki export**]命令用来将PKI域中的CA证书、本地证书导出到文件中或终端上。

【命令】

**[pki export**[ **domain** *domain*-*name* **der** { **all** \| **ca** \| **local** } **filename** *filename*]]

**[pki export**[ **domain** *domain*-*name* **p12** { **all** \| **local** } **passphrase** *p12passwordstring* **filename** *filename*]]

**[pki export**[ **domain** *domain*-*name* **pem** { { **all** \| **local** } [ { **3des-cbc** \| **aes-128-cbc** \| **aes-192-cbc** \| **aes-256-cbc** \| **des-cbc** } *pempasswordstring* ] \| **ca** }  **filename** *filename* ]]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[domain ***domain*-*name*]：证书所在的PKI域的名称，为1～31个字符的字符串，不区分大小写，不能包括"\~"、"\*"、"\"、"[\|]"、":"、"."、"\<"、"\>"、"\""和"\'"。

**[der**]：指定证书文件格式为DER编码。

**[p12**]：指定证书文件格式为PKCS12编码。

**[pem**]：指定证书文件格式为PEM编码。

**[all**]：表示导出所有证书，包括PKI域中所有的CA证书和本地证书，但不包括RA证书。

**[ca**]：表示导出CA证书。

**[local**]：表示导出本地证书或者本地证书和其对应私钥。

**[passphrase*** p12passwordstring*]：指定对PKCS12编码格式的本地证书对应的私钥进行加密所采用的口令。

**[3des-cbc**]**：**对本地证书对应的私钥数据采用3DES_CBC算法进行加密。

**[aes-128-cbc**]：对本地证书对应的私钥数据采用128位AES_CBC算法进行加密。

**[aes-192-cbc**]：对本地证书对应的私钥数据采用192位AES_CBC算法进行加密。

**[aes-256-cbc**]：对本地证书对应的私钥数据采用256位AES_CBC算法进行加密。

**[des-cbc**]：对本地证书对应的私钥数据采用DES_CBC算法进行加密。

*[pempasswordstring*]：指定对PEM编码格式的本地证书对应的私钥进行加密所采用的口令。

**[filename ***filename*]：指定保存证书的文件名，不区分大小写。如果不指定本参数，则表示要将证书直接导出到终端上显示，这种方式仅PEM编码格式的证书才支持。

【使用指导】

导出CA证书时，如果PKI域中只有一个CA证书则导出单个CA证书到用户指定的一个文件或终端，如果是一个CA证书链则导出整个CA证书链到用户指定的一个文件或终端。

导出本地证书时，设备上实际保存证书的证书文件名称并不一定是用户指定的名称，它与本地证书的密钥对用途相关，具体的命名规则如下（假设用户指定的文件名为*filename*）：

·如果本地证书的密钥对用途为签名，则证书文件名称为*filename*-signature；

·如果本地证书的密钥对用途为加密，则证书文件名称为*filename*-encryption；

·如果本地证书的密钥对用途为通用（RSA/ECDSA/DSA），则证书文件名称为用户输入的*filename*。

导出本地证书时，如果PKI域中有两个本地证书，则导出结果如下：

·若指定文件名，则将每个本地证书分别导出到一个单独的文件中；

·若不指定文件名，则将所有本地证书一次性全部导出到终端上，并由不同的提示信息进行分割显示。

导出所有证书时，如果PKI域中只有本地证书或者只有CA证书，则导出结果与单独导出相同。如果PKI域中存在本地证书和CA证书，则具体导出结果如下：

·若指定文件名，则将每个本地证书分别导出到一个单独的文件，该本地证书对应的完整CA证书链也会同时导出到该文件中。

·若不指定文件名，则将所有的本地证书及域中的CA证书或者CA证书链一次性全部导出到终端上，并由不同的提示信息进行分割显示。

需要注意的是：

·以PKCS12格式导出所有证书时，PKI域中必须有本地证书，否则会导出失败。

·以PEM格式导出本地证书或者所有证书时，若不指定私钥的加密算法和私钥加密口令，则不会导出本地证书对应的私钥信息。

·以PEM格式导出本地证书或者所有证书时，若指定私钥加密算法和私钥加密口令，且此时本地证书有匹配的私钥，则同时导出本地证书的私钥信息；如果此时本地证书没有匹配的私钥，则导出该本地证书失败。

·导出本地证书时，若当前PKI域中的密钥对配置已被修改，导致本地证书的公钥与该密钥对的公钥部分不匹配，则导出该本地证书失败。

·导出本地证书或者所有证书时，如果PKI域中有两个本地证书，则导出某种密钥用途的本地证书失败并不会影响导出另外一个本地证书。

·指定的文件名中可以带完整路径，当系统中不存在用户所指定路径时，则会导出失败。

【举例】

\# 导出PKI域中的CA证书到DER编码的文件，文件名称为cert-ca.der。

\<Sysname\> system-view

Sysname pki export domain domain1 der ca filename cert-ca.der

\# 导出PKI域中的本地证书到DER编码的文件，文件名称为cert-lo.der。

\<Sysname\> system-view

Sysname pki export domain domain1 der local filename cert-lo.der

\# 导出PKI域中的所有证书到DER编码的文件，文件名称为cert-all.p7b。

\<Sysname\> system-view

Sysname pki export domain domain1 der all filename cert-all.p7b

\# 导出PKI域中的CA证书到PEM编码的文件，文件名称为cacert。

\<Sysname\> system-view

Sysname pki export domain domain1 pem ca filename cacert

\# 导出PKI域中的本地证书及其对应的私钥到PEM编码的文件，指定保护私钥信息的加密算法为DES_CBC、加密口令为111，文件名称为local.pem。

\<Sysname\> system-view

Sysname pki export domain domain1 pem local des-cbc 111 filename local.pem

\# 导出PKI域中所有证书到PEM编码的文件，不指定加密算法和加密口令，不导出本地证书对应的私钥信息，文件名称为all.pem。

\<Sysname\> system-view

Sysname pki export domain domain1 pem all filename all.pem

\# 以PEM格式导出PKI域中本地证书及其对应的私钥到终端，指定保护私钥信息的加密算法为DES_CBC、加密口令为111。

\<Sysname\> system-view

Sysname pki export domain domain1 pem local des-cbc 111

%The signature usage local certificate:

Bag Attributes

    friendlyName:

    localKeyID: 99 0B C2 3B 8B D1 E4 33 42 2B 31 C3 37 C0 1D DF 0D 79 09 1D

subject=/C=CN/O=OpenCA Labs/OU=Users/CN=chktest chktest

issuer=/C=CN/O=OpenCA Labs/OU=software/CN=abcd

\-\-\-\--BEGIN CERTIFICATE\-\-\-\--

MIIEqjCCA5KgAwIBAgILAOhID4rI04kBfYgwDQYJKoZIhvcNAQELBQAwRTELMAkG

A1UEBhMCQ04xFDASBgNVBAoMC09wZW5DQSBMYWJzMREwDwYDVQQLDAhzb2Z0d2Fy

ZTENMAsGA1UEAwwEYWJjZDAeFw0xMTA0MjYxMzMxMjlaFw0xMjA0MjUxMzMxMjla

ME0xCzAJBgNVBAYTAkNOMRQwEgYDVQQKDAtPcGVuQ0EgTGFiczEOMAwGA1UECwwF

VXNlcnMxGDAWBgNVBAMMD2Noa3Rlc3QgY2hrdGVzdDCBnzANBgkqhkiG9w0BAQEF

AAOBjQAwgYkCgYEA54rUZ0Ux2kApceE4ATpQ437CU6ovuHS5eJKZyky8fhMoTHhE

jE2KfBQIzOZSgo2mdgpkccjr9Ek6IUC03ed1lPn0IG/YaAl4Tjgkiv+w1NrlSvAy

cnPaSUko2QbO9sg3ycye1zqpbbqj775ulGpcXyXYD9OY63/Cp5+DRQ92zGsCAwEA

AaOCAhUwggIRMAkGA1UdEwQCMAAwUAYDVR0gBEkwRzAGBgQqAwMEMAYGBCoDAwUw

NQYEKgMDBjAtMCsGCCsGAQUFBwIBFh9odHRwczovL3RpdGFuL3BraS9wdWIvY3Bz

L2Jhc2ljMBEGCWCGSAGG+EIBAQQEAwIFoDALBgNVHQ8EBAMCBsAwKQYDVR0lBCIw

IAYIKwYBBQUHAwIGCCsGAQUFBwMEBgorBgEEAYI3FAICMC4GCWCGSAGG+EIBDQQh

Fh9Vc2VyIENlcnRpZmljYXRlIG9mIE9wZW5DQSBMYWJzMB0GA1UdDgQWBBTPw8FY

ut7Xr2Ct/23zU/ybgU9dQjAfBgNVHSMEGDAWgBQzEQ58yIC54wxodp6JzZvn/gx0

CDAaBgNVHREEEzARgQ9jaGt0ZXN0QGgzYy5jb20wGQYDVR0SBBIwEIEOcGtpQG9w

ZW5jYS5vcmcwgYEGCCsGAQUFBwEBBHUwczAyBggrBgEFBQcwAoYmaHR0cDovL3Rp

dGFuL3BraS9wdWIvY2FjZXJ0L2NhY2VydC5jcnQwHgYIKwYBBQUHMAGGEmh0dHA6

Ly90aXRhbjoyNTYwLzAdBggrBgEFBQcwDIYRaHR0cDovL3RpdGFuOjgzMC8wPAYD

VR0fBDUwMzAxoC+gLYYraHR0cDovLzE5Mi4xNjguNDAuMTI4L3BraS9wdWIvY3Js

L2NhY3JsLmNybDANBgkqhkiG9w0BAQsFAAOCAQEAGcMeSpBJiuRmsJW0iZK5nygB

tgD8c0b+n4v/F36sJjY1fRFSr4gPLIxZhPWhTrqsCd+QMELRCDNHDxvt3/1NEG12

X6BVjLcKXKH/EQe0fnwK+7PegAJ15P56xDeACHz2oysvNQ0Ot6hGylMqaZ8pKUKv

UDS8c+HgIBrhmxvXztI08N1imYHq27Wy9j6NpSS60mMFmI5whzCWfTSHzqlT2DNd

no0id18SZidApfCZL8zoMWEFI163JZSarv+H5Kbb063dxXfbsqX9Noxggh0gD8dK

7X7/rTJuuhTWVof5gxSUJp+aCCdvSKg0lvJY+tJeXoaznrINVw3SuXJ+Ax8GEw==

\-\-\-\--END CERTIFICATE\-\-\-\--

Bag Attributes

    friendlyName:

    localKeyID: 99 0B C2 3B 8B D1 E4 33 42 2B 31 C3 37 C0 1D DF 0D 79 09 1D

Key Attributes: \<No Attributes\>

\-\-\-\--BEGIN ENCRYPTED PRIVATE KEY\-\-\-\--

MIICwzA9BgkqhkiG9w0BBQ0wMDAbBgkqhkiG9w0BBQwwDgQIAbfcE+KoYYoCAggA

MBEGBSsOAwIHBAjB+UsJM07JRQSCAoABqtASbjGTQbdxL3n4wNHmyWLxbvL9v27C

Uu6MjYJDCipVzxHU0rExgn+6cQsK5uK99FPBmy4q9/nnyrooTX8BVlXAjenvgyii

WQLwnIg1IuM8j2aPkQ3wbae1+0RACjSLy1u/PCl5sp6CDxI0b9xz6cxIGxKvUOCc

/gxdgk97XZSW/0qnOSZkhgeqBZuxq6Va8iRyho7RCStVxQaeiAZpq/WoZbcS5CKI

/WXEBQd4AX2UxN0Ld/On7Wc6KFToixROTxWTtf8SEsKGPDfrEKq3fSTW1xokB8nM

bkRtU+fUiY27V/mr1RHO6+yEr+/wGGClBy5YDoD4I9xPkGUkmqx+kfYbMo4yxkSi

JdL+X3uEjHnQ/rvnPSKBEU/URwXHxMX9CdCTSqh/SajnrGuB/E4JhOEnS/H9dIM+

DN6iz1IwPFklbcK9KMGwV1bosymXmuEbYCYmSmhZb5FnR/RIyE804Jz9ifin3g0Q

ZrykfG7LHL7Ga4nh0hpEeEDiHGEMcQU+g0EtfpOLTI8cMJf7kdNWDnI0AYCvBAAM

3CY3BElDVjJq3ioyHSJca8C+3lzcueuAF+lO7Y4Zluq3dqWeuJjE+/1BZJbMmaQA

X6NmXKNzmtTPcMtojf+n3+uju0le0d0QYXQz/wPsV+9IYRYasjzoXE5dhZ5sIPOd

u9x9hhp5Ns23bwyNP135qTNjx9i/CZMKvLKywm3Yg+Bgg8Df4bBrFrsH1U0ifmmp

ir2+OuhlC+GbHOxWNeBCa8iAq91k6FGFJ0OLA2oIvhCnh45tM7BjjKTHk+RZdMiA

0TKSWuOyihrwxdUEWh999GKUpkwDHLZJFd21z/kWspqThodEx8ea

\-\-\-\--END ENCRYPTED PRIVATE KEY\-\-\-\--

\# 以PEM格式导出PKI域中所有证书到终端，指定保护本地证书对应私钥的加密算法为DES_CBC、加密口令为111。

\<Sysname\> system-view

Sysname pki export domain domain1 pem all des-cbc 111

 %The signature usage local certificate:

Bag Attributes

    friendlyName:

    localKeyID: 99 0B C2 3B 8B D1 E4 33 42 2B 31 C3 37 C0 1D DF 0D 79 09 1D

subject=/C=CN/O=OpenCA Labs/OU=Users/CN=chktest chktest

issuer=/C=CN/O=OpenCA Labs/OU=software/CN=abcd

\-\-\-\--BEGIN CERTIFICATE\-\-\-\--

MIIEqjCCA5KgAwIBAgILAOhID4rI04kBfYgwDQYJKoZIhvcNAQELBQAwRTELMAkG

A1UEBhMCQ04xFDASBgNVBAoMC09wZW5DQSBMYWJzMREwDwYDVQQLDAhzb2Z0d2Fy

ZTENMAsGA1UEAwwEYWJjZDAeFw0xMTA0MjYxMzMxMjlaFw0xMjA0MjUxMzMxMjla

ME0xCzAJBgNVBAYTAkNOMRQwEgYDVQQKDAtPcGVuQ0EgTGFiczEOMAwGA1UECwwF

VXNlcnMxGDAWBgNVBAMMD2Noa3Rlc3QgY2hrdGVzdDCBnzANBgkqhkiG9w0BAQEF

AAOBjQAwgYkCgYEA54rUZ0Ux2kApceE4ATpQ437CU6ovuHS5eJKZyky8fhMoTHhE

jE2KfBQIzOZSgo2mdgpkccjr9Ek6IUC03ed1lPn0IG/YaAl4Tjgkiv+w1NrlSvAy

cnPaSUko2QbO9sg3ycye1zqpbbqj775ulGpcXyXYD9OY63/Cp5+DRQ92zGsCAwEA

AaOCAhUwggIRMAkGA1UdEwQCMAAwUAYDVR0gBEkwRzAGBgQqAwMEMAYGBCoDAwUw

NQYEKgMDBjAtMCsGCCsGAQUFBwIBFh9odHRwczovL3RpdGFuL3BraS9wdWIvY3Bz

L2Jhc2ljMBEGCWCGSAGG+EIBAQQEAwIFoDALBgNVHQ8EBAMCBsAwKQYDVR0lBCIw

IAYIKwYBBQUHAwIGCCsGAQUFBwMEBgorBgEEAYI3FAICMC4GCWCGSAGG+EIBDQQh

Fh9Vc2VyIENlcnRpZmljYXRlIG9mIE9wZW5DQSBMYWJzMB0GA1UdDgQWBBTPw8FY

ut7Xr2Ct/23zU/ybgU9dQjAfBgNVHSMEGDAWgBQzEQ58yIC54wxodp6JzZvn/gx0

CDAaBgNVHREEEzARgQ9jaGt0ZXN0QGgzYy5jb20wGQYDVR0SBBIwEIEOcGtpQG9w

ZW5jYS5vcmcwgYEGCCsGAQUFBwEBBHUwczAyBggrBgEFBQcwAoYmaHR0cDovL3Rp

dGFuL3BraS9wdWIvY2FjZXJ0L2NhY2VydC5jcnQwHgYIKwYBBQUHMAGGEmh0dHA6

Ly90aXRhbjoyNTYwLzAdBggrBgEFBQcwDIYRaHR0cDovL3RpdGFuOjgzMC8wPAYD

VR0fBDUwMzAxoC+gLYYraHR0cDovLzE5Mi4xNjguNDAuMTI4L3BraS9wdWIvY3Js

L2NhY3JsLmNybDANBgkqhkiG9w0BAQsFAAOCAQEAGcMeSpBJiuRmsJW0iZK5nygB

tgD8c0b+n4v/F36sJjY1fRFSr4gPLIxZhPWhTrqsCd+QMELRCDNHDxvt3/1NEG12

X6BVjLcKXKH/EQe0fnwK+7PegAJ15P56xDeACHz2oysvNQ0Ot6hGylMqaZ8pKUKv

UDS8c+HgIBrhmxvXztI08N1imYHq27Wy9j6NpSS60mMFmI5whzCWfTSHzqlT2DNd

no0id18SZidApfCZL8zoMWEFI163JZSarv+H5Kbb063dxXfbsqX9Noxggh0gD8dK

7X7/rTJuuhTWVof5gxSUJp+aCCdvSKg0lvJY+tJeXoaznrINVw3SuXJ+Ax8GEw==

\-\-\-\--END CERTIFICATE\-\-\-\--

Bag Attributes: \<No Attributes\>

subject=/C=CN/O=OpenCA Labs/OU=software/CN=abcd

issuer=/C=CN/O=OpenCA Labs/OU=software/CN=abcd

\-\-\-\--BEGIN CERTIFICATE\-\-\-\--

MIIEYTCCA0mgAwIBAgIBFzANBgkqhkiG9w0BAQsFADBFMQswCQYDVQQGEwJDTjEU

MBIGA1UECgwLT3BlbkNBIExhYnMxETAPBgNVBAsMCHNvZnR3YXJlMQ0wCwYDVQQD

DARhYmNkMB4XDTExMDQxODExNDQ0N1oXDTEzMDQxNzExNDQ0N1owRTELMAkGA1UE

BhMCQ04xFDASBgNVBAoMC09wZW5DQSBMYWJzMREwDwYDVQQLDAhzb2Z0d2FyZTEN

MAsGA1UEAwwEYWJjZDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAM1g

vomMF8S4u6q51bOwjKFUBwxyvOy4D897LmOSedaCyDt6Lvp+PBEHfwWBYBpsHhk7

kmnSNhX5dZ6NxunHaARZ2VlcctsYKyvAQapuaThy1tuOcphAB+jQQL9dPoqdk0xp

jvmPDlW+k832Konn9U4dIivS0n+/KMGh0g5UyzHGqUUOo7s9qFuQf5EjQon40TZg

BwUnFYRlvGe7bSQpXjwi8LTyxHPy+dDVjO5CP+rXx5IiToFy1YGWewkyn/WeswDf

Yx7ZludNus5vKWTihgx2Qalgb+sqUMwI/WUET7ghO2dRxPUdUbgIYF0saTndKPYd

4oBgl6M0SMsHhe9nF5UCAwEAAaOCAVowggFWMA8GA1UdEwEB/wQFMAMBAf8wCwYD

VR0PBAQDAgEGMB0GA1UdDgQWBBQzEQ58yIC54wxodp6JzZvn/gx0CDAfBgNVHSME

GDAWgBQzEQ58yIC54wxodp6JzZvn/gx0CDAZBgNVHREEEjAQgQ5wa2lAb3BlbmNh

Lm9yZzAZBgNVHRIEEjAQgQ5wa2lAb3BlbmNhLm9yZzCBgQYIKwYBBQUHAQEEdTBz

MDIGCCsGAQUFBzAChiZodHRwOi8mdcGl0YW4vcGtpL3B1Yi9jYWNlcnQvY2FjZXJ0

LmNydDAeBggrBgEFBQcwAYYSaHR0cDovL3RpdGFuOjI1NjAvMB0GCCsGAQUFBzAM

hhFodHRwOi8mdcGl0YW46ODMwLzA8BgNVHR8ENTAzMDGgL6AthitodHRwOi8vMTky

LjE2OC40MC4xMjgvcGtpL3B1Yi9jcmwvY2FjcmwuY3JsMA0GCSqGSIb3DQEBCwUA

A4IBAQC0q0SSmvQNfa5ELtRKYF62C/Y8QTLbk6lZDTZuIzN15SGKQcbNM970ffCD

Lk1zosyEVE7PLnii3bZ5khcGO3byyXfluAqRyOGVJcudaw7uIQqgv0AJQ+zaQSHi

d4kQf5QWgYkQ55/C5puOmcMRgCbMpR2lYkqXLDjTIAZIHRZ/sTp6c+ie2bFxi/YT

3xYbO0wDMuGOKJJpsyKTKcbG9NdfbDyFgzEYAobyYqAUB3C0/bMfBduwhQWKSoYE

6vZsPGAEisCmAl3dIp49jPgVkixoShraYF1jLsWzJGlzem8QvWYzOqKEDwq3SV0Z

cXK8gzDBcsobcUMkwIYPAmd1kAPX

\-\-\-\--END CERTIFICATE\-\-\-\--

Bag Attributes

    friendlyName:

    localKeyID: 99 0B C2 3B 8B D1 E4 33 42 2B 31 C3 37 C0 1D DF 0D 79 09 1D

Key Attributes: \<No Attributes\>

\-\-\-\--BEGIN ENCRYPTED PRIVATE KEY\-\-\-\--

MIICwzA9BgkqhkiG9w0BBQ0wMDAbBgkqhkiG9w0BBQwwDgQIcUSKSW9GVmICAggA

MBEGBSsOAwIHBAi5QZM+lSYWPASCAoBKDYulE5f2BXL9ZhI9zWAJpx2cShz/9PsW

5Qm106D+xSj1eAzkx/m4Xb4xRU8oOAuzu1DlWfSHKXoaa0OoRSiOEX1eg0eo/2vv

CHCvKHfTJr4gVSSa7i4I+aQ6AItrI6q99WlkN/e/IE5U1UE4ZhcsIiFJG+IvG7S8

f9liWQ2CImy/hjgFCD9nqSLN8wUzP7O2SdLVlUb5z4FR6VISZdgTFE8j7ko2HtUs

HVSg0nm114EwPtPMMbHefcuQ6b82y1M+dWfVxBN9K03lN4tZNfPWwLSRrPvjUzBG

dKtjf3/IFdV7/tUMy9JJSpt4iFt1h7SZPcOoGp1ZW+YUR30I7YnFE+9Yp/46KWT8

bk7j0STRnZX/xMy/9E52uHkLdW1ET3TXralLMYt/4jg4M0jUvoi3GS2Kbo+czsUn

gKgqwYnxVfRSvt8d6GBYrpF2tMFS9LEyngPKXExd+m4mAryuT5PhdFTkb1B190Lp

UIBjk3IXnr7AdrhvyLkH0UuQE95emXBD/K0HlD73cMrtmogL8F4yS5B2hpIr/v5/

eW35+1QMnJ9FtHFnVsLx9wl9lX8iNfsoBhg6FQ/hNSioN7rNBe7wwIRzxPVfEhO8

5ajQxWlidRn5RkzfUo6HuAcq02QTpSXI6wf2bzsVmr5sk+fRaELD/cwL6VjtXO6x

ZBLJcUyAwvScrOtTEK7Q5n0I34gQd4qcF0D1x9yQ4sqvTeU/7Jkm6XCPV05/5uiF

RLCfFAwaJMBdIQ6jDQHnpWT67uNDwdEzaPmuTVMme5Woc5zsqE5DY3hWu4oqFdDz

kPLnbX74IZ0gOLki9eIJkVswnF5HkBCKS50ejlW6TgbMNZ+JPk2w

\-\-\-\--END ENCRYPTED PRIVATE KEY\-\-\-\--

\# 以PEM格式导出PKI域中CA证书到终端。

\<Sysname\> system-view

Sysname pki export domain domain1 pem ca

\-\-\-\--BEGIN CERTIFICATE\-\-\-\--

MIIB+TCCAWICEQDMbgjRKygg3vpGFVY6pa3ZMA0GCSqGSIb3DQEBBQUAMD0xCzAJ

BgNVBAYTAmNuMQwwCgYDVQQKEwNoM2MxETAPBgNVBAsTCGgzYy10ZXN0MQ0wCwYD

VQQDEwQ4MDQzMB4XDTExMDMyMjA0NDQyNFoXDTE0MDMyMzA0MzUyNFowPTELMAkG

A1UEBhMCY24xDDAKBgNVBAoTA2gzYzERMA8GA1UECxMIaDNjLXRlc3QxDTALBgNV

BAMTBDgwNDMwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAOvDAYQhyc++G7h5

eNDzJs22OQjCn/4JqnNKIdKz1BbaJT8/+IueSn9JIsg64Ex2WBeCd/tcmnSW57ag

dCvNIUYXXVOGca2iaSOElqCF4CQfV9zLrBtA7giHD49T+JbxLrrJLmdIQMJ+vYdC

sCxIp3YMAiuCahVLZeXklooqwqIXAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAElm7

W2Lp9Xk4nZVIpVV76CkNe8/C+Id00GCRUUVQFSMvo7Pded76bmYX2KzJSz+DlMqy

TdVrgG9Fp6XTFO80aKJGe6NapsfhJHKS+Q7mL0XpXeMONgK+e3dX7rsDxsY7hF+j

0gwsHrjV7kWvwJvDlhzGW6xbpr4DRmdcao19Cr6o=

\-\-\-\--END CERTIFICATE\-\-\-\--

\# 导出PKI域中CA证书到PEM编码的文件，指定文件名称为cacert。

\<Sysname\> system-view

Sysname pki export domain domain1 pem ca filename cacert

\# 导出PKI域中CA证书（证书链）到终端。

\<Sysname\> system-view

Sysname pki export domain domain1 pem ca

\-\-\-\--BEGIN CERTIFICATE\-\-\-\--

MIIB7jCCAVcCEQCdSVShJFEMifVG8zRRoSsWMA0GCSqGSIb3DQEBBQUAMDcxCzAJ

BgNVBAYTAmNuMQwwCgYDVQQKEwNoM2MxDDAKBgNVBAsTA2gzYzEMMAoGA1UEAxMD

YWNhMB4XDTExMDEwNjAyNTc0NFoXDTEzMTIwMTAzMTMyMFowODELMAkGA1UEBhMC

Y24xDDAKBgNVBAoTA2gzYzEMMAoGA1UECxMDaDNjMQ0wCwYDVQQDEwRhYWNhMIGf

MA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDcuJsWhAJXEDmowGb5z7VDVms54TKi

xnaNJCWvBOrU64ftvpVB7xQekbkjgAS9FjDyXlLQ8IyIsYIp5ebJr8P+n9i9Pl7j

lBx5mi4XeIldyv2OjfNx5oSQ+gWY9/m1R8uv13RS05r3rxPg+7EvKBjmiy0Giddw

vu3Y3WrjBPp6GQIDAQABMA0GCSqGSIb3DQEBBQUAA4GBAJrQddzVQEiy4AcgtzUL

ltkmlmWoz87+jUsgFB+H+xeyiZE4sancf2UwH8kXWqZ5AuReFCCBC2fkvvQvUGnV

cso7JXAhfw8sUFok9eHz2R+GSoEk5BZFzZ8eCmNyGq9ln6mJsO1hAqMpsCW6G2zh

5mus7FTHhywXpJ22/fnHg61m

\-\-\-\--END CERTIFICATE\-\-\-\--

\-\-\-\--BEGIN CERTIFICATE\-\-\-\--

MIIB8DCCAVkCEQD2PBUx/rvslNw9uTrZB3DlMA0GCSqGSIb3DQEBBQUAMDoxCzAJ

BgNVBAYTAmNuMQwwCgYDVQQKEwNoM2MxDDAKBgNVBAsTA2gzYzEPMA0GA1UEAxMG

cm9mdcGNhMB4XDTExMDEwNjAyNTY1OFoXDTEzMTIwNDAzMTMxMFowNzELMAkGA1UE

BhMCY24xDDAKBgNVBAoTA2gzYzEMMAoGA1UECxMDaDNjMQwwCgYDVQQDEwNhY2Ew

gZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAOeklR7DpeEV72N1OLz+dydIDTx0

zVZDdPxF1gQYWSfIBwwFKJEyQ/4y8VIfDIm0EGTM4dsOX/QFwudhl/Czkio3dWLh

Q1y5XCJy68vQKrB82WZ2mah5Nuekus3LSZZBoZKTAOY5MCCMFcULM858dtSq15Sh

xF7tKSeAT7ARlJxTAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEADJQCo6m0RNup0ewa

ItX4XK/tYcJXAQWMA0IuwaWpr+ofqVVgYBPwVpYglhJDOuIZxKdR2pfQOA4f35wM

Vz6kAujLATsEA1GW9ACUWa5PHwVgJk9BDEXhKSJ2e7odmrg/iROhJjc1NMV3pvIs

CuFiCLxRQcMGhCNHlOn4wuydssc=

\-\-\-\--END CERTIFICATE\-\-\-\--

\-\-\-\--BEGIN CERTIFICATE\-\-\-\--

MIIB8jCCAVsCEFxy3MSlQ835MrnBkI/dUPYwDQYJKoZIhvcNAQEFBQAwOjELMAkG

A1UEBhMCY24xDDAKBgNVBAoTA2gzYzEMMAoGA1UECxMDaDNjMQ8wDQYDVQQDEwZy

b290Y2EwHhcNMTEwMTA2MDI1MTQxWhcNMTMxMjA3MDMxMjA1WjA6MQswCQYDVQQG

EwJjbjEMMAoGA1UEChMDaDNjMQwwCgYDVQQLEwNoM2MxDzANBgNVBAMTBnJvb3Rj

YTCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEAxP2XLFE230zq6MhwZvAomOxa

7tc1r4bESXZu3UBKno3Ay9kQm2HrDOAizvZXfLu7Gx22ga2Qdz0lIeZ+EQrYHTyO

pBcejDjal/ZtvgnjXyHFoG8nS+P7n83BkRj/Fu7Yz4zjTKMbCF2EfhEyXxr4NSXA

fhC9qg9S23vNXStmWvsCAwEAATANBgkqhkiG9w0BAQUFAAOBgQBtsU7X77sdZ1Nn

0I98lh0qA5g7SEEIpI+pwZjjrH0FVHw01e4JWhHjyHqrOyfXYqe7vH4SXp5MHEqf

14nKIEbexbPONspebtznxv4/xTjd1aM2rfQ95jJ/SN8H8KIyiYZyIs3t5Q+V35x1

cef+NMWgZBzwXOSP0wC9+pC2ZNiIpg==

\-\-\-\--END CERTIFICATE\-\-\-\--

\# 导出PKI域中的本地证书及其对应的私钥到PKCS12编码的文件，指定保护私钥信息的加密口令为123，文件名称为cert-lo.der。

\<Sysname\> system-view

Sysname pki export domain domain1 p12 local passphrase 123 filename cert-lo.der

\# 导出PKI域中的所有证书到PKCS12编码的文件，指定文件名称为cert-all.p7b。

\<Sysname\> system-view

Sysname pki export domain domain1 p12 all passphrase 123 filename cert-all.p7b

【相关命令】

·**pki domain**

**PKI \-- PKI配置命令 \-- pki import**

------------------------------------------------------------------------

**[pki import**]命令用来将CA证书、本地证书或对端证书导入到指定的PKI域中保存。

【命令】

**[pki import domain ***domain-name*****[{ **der** { **ca** \| **local** \| **peer** } **filename** *filename \|* **p12 local filename** *filename \|* **pem** { **ca** \| **local** \| **peer** } [ **filename** *filename* ] }]]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[domain** *domain*-*name*]：保存证书的PKI域的名称，为1～31个字符的字符串，不区分大小写，不能包括"\~"、"\*"、"\"、"[\|]"、":"、"."、"\<"、"\>"、"\""和"\'"。

**[der**]：指定证书格式为DER编码（包括PKCS#7格式的证书）。

**[p12**]：指定证书格式为PKCS#12编码。

**[pem**]：指定证书格式为PEM编码。

**[ca**]：表示CA证书。

**[local**]：表示本地证书。

**[peer**]：表示对端证书。

**[filename ***filename*]：要导入的证书所在的文件名，不区分大小写。如果不指定本参数，则表示要通过直接在终端上粘贴证书内容的方式导入证书，这种方式仅PEM编码格式的证书才支持。

【使用指导】

如果设备所处的环境中，没有证书的发布点，或者CA服务器不支持通过SCEP协议与设备交互，则可通过此命令将证书导入到设备。另外，当证书对应的密钥对由CA服务器生成时，CA服务器会将证书和对应的密钥对打包成一个文件，使用这样的证书前也需要通过此命令将其导入到设备。只有PKCS#12格式或PEM格式的证书文件中可能包含密钥对。

证书导入之前：

·需要通过FTP、TFTP等协议将证书文件传送到设备的存储介质中。如果设备所处的环境不允许使用FTP、TFTP等协议，则可以直接在终端上粘贴证书的内容，但是粘贴的证书必须是PEM格式的，因为只有PEM编码的证书内容为可打印字符。

·必须存在签发本地证书（或对端证书）的CA证书链才能成功导入本地证书（或对端证书），这里的CA证书链可以是保存在设备上的PKI域中的，也可以是本地证书（或对端证书）中携带的。因此，若设备和本地证书（或对端证书）中都没有CA证书链，则需要首先执行导入CA证书的命令。

导入本地证书或对端证书时：

·如果用户要导入的本地证书（或对端证书）中含有CA证书链，则可以通过导入本地证书（或对端证书）的命令一次性将CA证书和本地证书（或对端证书）均导入到设备。导入的过程中，如果发现签发此本地证书（或对端证书）的CA证书已经存在于设备上的任一PKI域中，则系统会提示用户是否将其进行覆盖。

·如果要导入的本地证书（或对端证书）中不含有CA证书链，但签发此本地证书（或对端证书）的CA证书已经存在于设备上的任一PKI域中，则可以直接导入本地证书（或对端证书）。

导入CA证书时：

·若要导入的CA证书为根CA或者包含了完整的证书链（即含有根证书），则可以导入到设备。

·若要导入的CA证书没有包含完整的证书链（即不含有根证书），但能够与设备上已有的CA证书拼接成完整的证书链，则也可以导入到设备；如果不能与设备上已有的CA证书拼接成完成的证书链，则不能导入到设备。

一些情况下，在证书导入的过程中，需要用户确认或输入相关信息：

·若要导入的证书文件中包含了根证书，且设备上目前还没有任何PKI域中有此根证书，且要导入的PKI域中没有配置**root-certificate fingerprint**，则在导入过程中还需要确认该根证书的指纹信息是否与用户的预期一致。用户需要通过联系CA服务器管理员来获取预期的根证书指纹信息。

·当导入含有密钥对的本地证书时，需要输入口令。用户需要联系CA服务器管理员取得口令的内容。

导入含有密钥对的本地证书时，系统首先会根据查找到的PKI域中已有的密钥对配置来保存该密钥对。若PKI域中已保存了对应的密钥对，则设备会提示用户选择是否覆盖已有的密钥对。若PKI域中没有任何密钥对的配置，则根据密钥对的算法及证书的密钥用途，生成相应的密钥对配置。密钥对的具体保存规则如下：

·如果本地证书携带的密钥对的用途为通用，则依次查找指定PKI域中通用用途、签名用途、加密用途的密钥对配置，并以找到配置中的密钥对名称保存该密钥对；若以上用途的密钥对配置均不存在，则提示用户输入密钥对名称（缺省的密钥对名称为PKI域的名称），并生成相应的密钥对配置。

·如果本地证书携带的密钥对的用途为签名，则依次查找指定PKI域中通用用途、签名用途的密钥对配置，并以找到配置中的密钥对名称保存该密钥对；若以上两种用途的密钥对配置均不存在，则提示用户输入密钥对名称（缺省的密钥对名称为PKI域的名称），并生成相应的密钥对配置。

·如果本地证书携带的密钥对的用途为加密，则查找指定PKI域中加密用途的密钥对配置，并以该配置中的密钥对名称保存密钥对；若加密用途密钥对的配置不存在，则提示用户输入密钥对名称（缺省的密钥对名称为PKI域的名称），并生成相应的密钥对配置。

由于以上过程中系统会自动更新或生成密钥对配置，因此建议用户在进行此类导入操作后，保存配置文件。

【举例】

\# 向PKI域aaa中导入CA证书，证书文件格式为PEM编码，证书文件名称为rootca_pem.cer，证书文件中包含根证书。

\<Sysname\> system-view

Sysname pki import domain aaa pem ca filename rootca_pem.cer

The trusted CA\'s finger print is:

    MD5  fingerprint:FFFF 3EFF FFFF 37FF FFFF 137B FFFF 7535

    SHA1 fingerprint:FFFF FF7F FF2B FFFF 7618 FF4C FFFF 0A7D FFFF FF69

Is the finger print correct?(Y/N):y

Sysname

\# 向PKI域bbb中导入CA证书，证书文件格式为PEM编码，证书文件名称为aca_pem.cer，证书文件中不包含根证书。

\<Sysname\> system-view

Sysname pki import domain bbb pem ca filename aca_pem.cer

Sysname

\# 向PKI域bbb中导入本地证书，证书文件格式为PKCS#12编码，证书文件名称为local-ca.p12，证书文件中包含了密钥对。

\<Sysname\> system-view

Sysname pki import domain bbb p12 local filename local-ca.p12

Please input challenge password:

\*\*\*\*\*\*

Sysname

\# 向PKI域bbb中通过粘贴证书内容的方式导入PEM编码的本地证书。证书中含有密钥对和CA证书链。

\<Sysname\> system-view

Sysname pki import domain bbb pem local

Enter PEM-formatted certificate.

End with a Ctrl+c on a line by itself.

Bag Attributes{.TerminalDisplayshading}

localKeyID: 01 00 00 00{.TerminalDisplayshading}

fri[endlyName: {F7619D96-3AC2-40D4-B6F3-4EAB73DEED73}]{.TerminalDisplayshading}

Microsoft CSP Name: Microsoft Enhanced Cryptographic Provider v1.0{.TerminalDisplayshading}

Key Attributes{.TerminalDisplayshading}

X509v3 Key Usage: 10{.TerminalDisplayshading}

\-\-\-\--BEGIN RSA PRIVATE KEY\-\-\-\--{.TerminalDisplayshading}

Proc-Type: 4,ENCRYPTED{.TerminalDisplayshading}

DEK-Info: DES-EDE3-CBC,8DCE37F0A61A4B8C{.TerminalDisplayshading}

{.TerminalDisplayshading}

k9C3KHY[5S3EtnF5iQymvHYYrVFy5ZdjSasU5y4XFubjdcvmpFHQteMjD0GKX6+xO]{.TerminalDisplayshading}

kuKbvpyCnWsPVg56sL/PDRyrRmqLmtUV3bpyQsFXgnc7p+Snj3CG2Ciow9XApybW{.TerminalDisplayshading}

Ec1TDCD75yuQckpVQdhguTvoPQXf9zHmiGu5jLkySp2k7ec/Mc97Ef+qqpfnHpQp{.TerminalDisplayshading}

GDmMqnFpp59ZzB21OGlbGzlPcsjoT+EGpZg6B1KrPiCyFim95L9dWVwX9sk+U1s2{.TerminalDisplayshading}

+8wqac8jETwwM0UZ1NGJ50JJz1QYIzMbcrw+S5WlPxACTIz1cldlBlb1kpc+7mcX{.TerminalDisplayshading}

4W+MxFzsL88IJ99T72eu4iUNsy26g0BZMAcc1sJA3A4w9RNhfs9hSG43S3hAh5li{.TerminalDisplayshading}

JPp720LfYBlkQHn/MgMCZASWDJ5G0eSXQt9QymHAth4BiT9v7zetnQqf4q8plfd/{.TerminalDisplayshading}

Xqd9zEFlBPpoJFtJqXwxHUCKgw6kJeC4CxHvi9ZCJU/upg9IpiguFPoaDOPia[+Pm]{.TerminalDisplayshading}

GbRqSyy55clVde5GOccGN1DZ94DW7AypazgLpBbrkIYAdjFPRmq+zMOdyqsGMTNj{.TerminalDisplayshading}

jnheI5l784pNOAKuGi0i/uXmRRcfoMh6qAnK6YZGS7rOLC9CfPmy8fgY+/Sl9d9x{.TerminalDisplayshading}

Q00ruO1psxzh9c2YfuaiXFIx0auKl6o5+ZZYn7Rg/xy2Y0awVP+dO925GoAcHO40{.TerminalDisplayshading}

cCl6jA/HsGAU9HkpwKHL35lmBDRLEzQeBFcaGwSm1JvRfE4tkJM7+Uz2Q[HJOfP10]{.TerminalDisplayshading}

0VLqMgxMlpk3TvBWgzHGJDe7TdzFCDPMPhod8pi4P8gGXmQd01PbyQ=={.TerminalDisplayshading}

\-\-\-\--END RSA PRIVATE KEY\-\-\-\--{.TerminalDisplayshading}

Bag Attributes{.TerminalDisplayshading}

localKeyID: 01 00 00 00{.TerminalDisplayshading}

subject=/CN=sldsslserver{.TerminalDisplayshading}

issuer=/C=cn/O={.TerminalDisplayshading}ccc{.TerminalDisplayshading}/OU=sec/CN=ssl{.TerminalDisplayshading}

\-\-\-\--BEGIN CERTIFICATE\-\-\-\--{.TerminalDisplayshading}

MIICjzCCAfigAwIBAgIRAJoDN+shVrofVHbk[11SlqfcwDQYJKoZIhvcNAQEFBQAw]{.TerminalDisplayshading}

NzELMAkGA1UEBhMCY24xDDAKBgNVBAoTA2gzYzEMMAoGA1UECxMDc2VjMQwwCgYD{.TerminalDisplayshading}

VQQDEwNzc2wwHhcNMTAxMDE1MDEyMzA2WhcNMTIwNzI2MDYzMDU0WjAXMRUwEwYD{.TerminalDisplayshading}

VQQDEwxzbGRzc2xzZXJ2ZXIwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMLP{.TerminalDisplayshading}

N3aTKV7NDndIOk0PpiikYPgxVih/geMX[R3iYaANbcvRX07/FMDINWHJnBAZhCDvp]{.TerminalDisplayshading}

rFO552loGiPyl0wmFMK12TSL7sHvrxr0OdrFrqtWlbW+DsNGNcFSKZy3RvIngC2k{.TerminalDisplayshading}

ZZqBeFPUytP185JUhbOrVaUDlisZi6NNshcIjd2BAgMBAAGjgbowgbcwHwYDVR0j{.TerminalDisplayshading}

BBgwFoAUmoMpEynZYoPLQdR1LlKhZjg8kBEwDgYDVR0PAQH/BAQDAgP4MBEGCWCG{.TerminalDisplayshading}

SAGG+EIBAQQEAwIGQDASBgNVHREE[CzAJggdoM2MuY29tMB0GA1UdDgQWBBQ8dpWb]{.TerminalDisplayshading}

3cJ/X5iDt8eg+JkeS9cvJjA+BgNVHR8ENzA1MDOgMaAvhi1odHRwOi8vczAzMTMw{.TerminalDisplayshading}

LmgzYy5odWF3ZWktM2NvbS5jb206NDQ3L3NzbC5jcmwwDQYJKoZIhvcNAQEFBQAD{.TerminalDisplayshading}

gYEAYS15x0kW474lu4twNzEy5dPjMSwtwfm/UK01S8GQjGV5tl9ZNiTHFGNEFx7k{.TerminalDisplayshading}

zxBp/JPpcFM8hapAfrVHdQ/w[stq0pVDdBkrVF6XKIBks6XgCvRl32gcaQt9yrQd9]{.TerminalDisplayshading}

5RbWdetuBljudjFj25airYO2u7pLeVmdWWx3WVvZBzOo8KU={.TerminalDisplayshading}

\-\-\-\--END CERTIFICATE\-\-\-\--{.TerminalDisplayshading}

Bag Attributes: \<Empty Attributes\>{.TerminalDisplayshading}

subject=/C=cn/O={.TerminalDisplayshading}ccc{.TerminalDisplayshading}/OU=sec/CN=ssl{.TerminalDisplayshading}

issuer=/C=cn/O={.TerminalDisplayshading}ccc{.TerminalDisplayshading}/OU=sec/CN=ssl{.TerminalDisplayshading}

\-\-\-\--BEGIN CERTIFICATE\-\-\-\--{.TerminalDisplayshading}

MIIB7DCCAVUCEG+jJTPxxiE67pl2ff0SnOMwDQYJKoZIhvcNAQEFBQAwNzELMAkG{.TerminalDisplayshading}

A1UEBhMCY24xDDAKBgNVBAoTA2gzYzEMMAoGA1UECxMDc2VjMQwwCgYDVQQDEwNz{.TerminalDisplayshading}

c2wwHhcNMDkwNzMxMDY0ODQ2WhcNMTIwNzI5MDYyODU4WjA3MQswCQYDVQQGEwJj{.TerminalDisplayshading}

bjEMMAoGA1UEChMDaDNjMQwwCgYDVQQLEwNzZWMxDDAKBgNVBAMTA3NzbDCBn[zAN]{.TerminalDisplayshading}

BgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEAt8QSMetQ70GONiFh7iJkvGQ8nC15zCF1{.TerminalDisplayshading}

cqC/RcJhE/88LkKyQcu9j+Tz8Bk9Qj2UPaZdrk8fOrgtBsa7lZ+UO3j3l30q84l+{.TerminalDisplayshading}

HjWq8yxVLRQahU3gqJze6pGR2l0s76u6GRyCX/zizGrHKqYlNnxK44NyRZx2klQ2{.TerminalDisplayshading}

tKQAfpXCPIkCAwEAATANBgkqhkiG9w0BAQUFAAOBgQBWsaMgRbBMtYNrr[YCMjY6g]{.TerminalDisplayshading}

c7PBjvajVOKNUMxaDalePmXfKCxl91+PKM7+i8I/zLcoQO+sHbva26a2/C4sNvoJ{.TerminalDisplayshading}

2QZs6GtAOahP6CDqXC5VuNBU6eTKNKjL+mf6uuDeMxrlDNha0iymdrXXVIp5cuIu{.TerminalDisplayshading}

fl7xgArs8Ks6aXDXM1o4DQ=={.TerminalDisplayshading}

\-\-\-\--END CERTIFICATE\-\-\-\--{.TerminalDisplayshading}

{.TerminalDisplayshading}

Please input the password:\*\*\*\*\*\*\*\*

Local certificate already exist, confirm to overwrite it? [Y/N:y]

The PKI domain already has a CA certificate. If it is overwritten, local certificates, peer certificates and CRL of this domain will also be deleted.

Overwrite it? [Y/N:y]

The system is going to save the key pair. You must specify a key pair name, which is a case-insensitive string of 1 to 64 characters. Valid characters include a to z, A to Z, 0 to 9, and hyphens (-).

Please enter the key pair name [default name: bbb:]

The key pair already exists.

Please enter the key pair name:

import-key

【相关命令】

·**display pki certificate**

·**public-key dsa**

·**public-key ecdsa**

·**public-key rsa**

**PKI \-- PKI配置命令 \-- pki request-certificate**

------------------------------------------------------------------------

**[pki request-certificate**]命令用来手工申请本地证书或生成PKCS#10证书申请。

【命令】

**[pki request-certificate**]** domain*** domain-name * **password** *password*  \**pkcs10 **[ **filename** *filename*  ]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[domain***domain-name*]：指定证书申请所属的 PKI域名，为1～31个字符的字符串，不区分大小写，不能包括"\~"、"\*"、"\"、"[\|]"、":"、"."、"\<"、"\>"、"\""和"\'"。

**[password** *password*]：在证书撤销时需要提供的口令，为1～31个字符的字符串，区分大小写。该口令包含在提交给CA的证书申请中，在吊销该证书时，需要提供该口令。

**[pkcs10**]：在终端上显示出BASE64格式的PKCS#10证书申请信息，该信息可用于带外方式（如电话、磁盘、电子邮件等）的证书请求。

**[filename**]* filename*：将PKCS#10格式的证书申请信息保存到本地的文件中。其中，*filename*表示保存证书申请信息的文件名，不区分大小写。

【使用指导】

当SCEP协议不能正常通信时，可以通过执行指定参数**pkcs10**的本命令打印出本地的证书申请信息（BASE64格式），或者通过执行指定**pkcs10 filename*** filename*参数的本命令将证书申请信息直接保存到本地的指定文件中，然后通过带外方式将这些本地证书申请信息发送给CA进行证书申请。指定的文件名中可以带完整路径，当系统中不存在用户所指定路径时，则会保存失败。

此命令不会被保存在配置文件中。

【举例】

\# 在终端上显示PKCS#10格式的证书申请信息。

\<Sysname\> system-view

Sysname pki request-certificate domain aaa pkcs10

\*\*\* Request for [general certificate \*\*\*]{.TerminalDisplayshading}

\-\-\-\--BEGIN {.TerminalDisplayshading}NEW {.TerminalDisplayshading}CERTIFICATE REQUEST\-\-\-\--{.TerminalDisplayshading}

MIIBTDCBtgIBADANMQswCQYDVQQDEwJqajCBnzANBgkqhkiG9w0BAQEFAAOBjQAw{.TerminalDisplayshading}

gYkCgYEAw5Drj8ofs9THA4ezkDcQPBy8pvH1kumampPsJmx8sGG52NFtbrDTnTT5{.TerminalDisplayshading}

ALx3LJijB3d/ndKpcHT/DfbJVDCn5gdw32tBZyCkEwMHZN3ol2z7N{.TerminalDisplayshading}mdc{.TerminalDisplayshading}u5TED6[iN8]{.TerminalDisplayshading}

4m+hfp1QWoV6lty3o9pxAXuQl8peUDcfN6WV3LBXYyl1WCtkLkECAwEAAaAAMA0G{.TerminalDisplayshading}

CSqGSIb3DQEBBAUAA4GBAA8E7BaIdmT6NVCZgv/I/1tqZH3TS4e4H9Qo5NiCKiEw{.TerminalDisplayshading}

R8owVmA0XVtGMbyqBNcDTG0f5NbHrXZQT5+MbFJOnm5K/mn1ro5TJKMTKV46PlCZ{.TerminalDisplayshading}

JUjsugaY02GBY0BVcylpC9iIXLuXNIqjh1MBIqVsa1lQOHS7YMvnop6hX[AQlkM4c]{.TerminalDisplayshading}

\-\-\-\--END {.TerminalDisplayshading}NEW {.TerminalDisplayshading}CERTIFICATE REQUEST\-\-\-\--{.TerminalDisplayshading}

\# 手工申请本地证书。

Sysname pki request-certificate domain openca

Start to request the general certificate \...

......

Certificate requested successfully.

【相关命令】

·**display pki certificate**

**PKI \-- PKI配置命令 \-- pki retrieve-certificate**

------------------------------------------------------------------------

**[pki retrieve-certificate**]命令用来从证书发布服务器上在线获取证书并下载至本地。

【命令】

**[pki retrieve-certificate**[ **domain** *domain-name* { **ca** \| **local** \| **peer** *entity-name* } ]]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[domain** *domain-name*]：指定证书所在的PKI域的名称，为1～31个字符的字符串，不区分大小写，不能包括"\~"、"\*"、"\"、"[\|]"、":"、"."、"\<"、"\>"、"\""和"\'"。

**[ca**]：表示获取CA证书。

**[local**]：表示获取本地证书。

**[peer** *entity-name*]：表示获取对端的证书。其中*entity-name*为对端的实体名，为1～31个字符的字符串，不区分大小写。

【使用指导】

获取CA证书是通过SCEP协议进行的。获取CA证书时，如果本地已有CA证书存在，则该操作将不被允许。这种情况下，若要重新获取CA证书，请先使用**pki delete-certificate**命令删除已有的CA证书与对应的本地证书后，再执行此命令。

获取本地证书和对端证书是通过LDAP协议进行的。获取本地证书或对端证书时，如果本地已有本地证书或对端证书，则该操作是被允许进行的。最终，属于一个PKI实体的同一种公钥算法的本地证书只能存在一个，后者直接覆盖已有的，但对于RSA算法的证书而言，可以存在一个签名用途的证书和一个加密用途的证书。

所有获取到的CA证书、本地证书或对端证书只有通过验证之后才会被保存到本地证书库中。

需要注意的是，此命令不会被保存在配置文件中。

【举例】

\# 从证书发布服务器上获取CA证书。（需要用户确认CA根证书的指纹）

\<Sysname\> system-view

Sysname pki retrieve-certificate domain aaa ca

The trusted CA\'s finger print is:

MD5  fingerprint:5C41 E657 A0D6 ECB4 6BD6 1823 7473 AABC

    SHA1 fingerprint:1616 E7A5 D89A 2A99 9419 1C12 D696 8228 87BC C266

Is the finger print correct?(Y/N):y

Retrieved the certificates successfully.

\# 从证书发布服务器上获取本地证书。

\<Sysname\> system-view

Sysname pki retrieve-certificate domain aaa local

Retrieved the certificates successfully.

\# 从证书发布服务器上获取对端证书。

\<Sysname\> system-view

Sysname pki retrieve-certificate domain aaa peer en1

Retrieved the certificates successfully.

【相关命令】

·**display pki certificate**

·{.TerminalDisplayshading}**pki delete-certificate**

**PKI \-- PKI配置命令 \-- pki retrieve-crl**

------------------------------------------------------------------------

**[pki retrieve-crl**]命令用来获取CRL并下载至本地。

【命令】

**[pki retrieve-crl** **domain** *domain-name* ]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[domain-name*]：指定CRL所属的PKI域的名称，为1～31个字符的字符串，不区分大小写，不能包括"\~"、"\*"、"\"、"[\|]"、":"、"."、"\<"、"\>"、"\""和"\'"。

【使用指导】

获取CRL的目的是为了验证PKI域中的本地证书和对端证书的合法性。若要成功获取CRL，PKI域中必须存在CA证书。

设备支持通过HTTP、LDAP或SCEP协议从CRL发布点上获取CRL，具体采用那种协议，由PKI域中CRL发布点的配置决定：

·若配置的CRL发布点URL格式为HTTP格式，则通过HTTP协议获取CRL。

·若配置的CRL发布点URL格式为LDAP格式，则通过LDAP协议获取CRL。若配置的CRL发布点URL（通过命令**crl url**）中缺少主机名，例如ldap:///CN=8088,OU=test,U=rd,C=cn，则还需要在PKI域中配置LDAP服务器的URL（通过命令**ldap server**）。此时，设备会将配置的LDAP服务器URL和配置的CRL发布点URL中的不完整的LDAP发布点拼装成完整的LDAP发布点，再通过LDAP协议获取CRL。

·若PKI域中没有配置CRL发布点，则设备会依次从本地证书、CA证书中查找CRL的发布点，如果从中查找到了CRL发布点，则通过该发布点获取CRL；否则，通过SCEP协议获取CRL。

【举例】

\# 从CRL发布点上获取CRL。

\<Sysname\> system-view

Sysname pki retrieve-crl domain aaa

Retrieve CRL of the domain aaa successfully.

【相关命令】

·**crl url**

·**ldap server**

**PKI \-- PKI配置命令 \-- pki storage**

------------------------------------------------------------------------

**[pki storage**]命令用来配置证书和CRL的存储路径。

**[undo pki storage**]命令用来恢复缺省情况。

【命令】

**[pki storage **[{ **certificates** \| **crls** } ]*dir-path*]

**[undo pki storage**  { **certificates** \| **crls** }]

【缺省情况】

证书和CRL的存储路径为设备存储介质上的PKI目录。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[certificates**]：指定证书的存储目录。

**[crls**]：指定CRL的存储目录。

*[dir-path*]：存储目录的路径名称，区分大小写，不能以'/'开头，不能包含"../"。*dir-path*可以是绝对路径也可以是相对路径，但必须已经存在。

【使用指导】

*[dir-path*]只能是当前主控板上的路径，不能是其它主控板上的路径。

设备缺省的PKI目录在设备首次成功申请、获取或导入证书时自动创建。

如果需要指定的目录还不存在，需要先使用**mkdir**命令创建这个目录，再使用此命令配存储路径。若修改了证书或CRL的存储目录，则原存储路径下的证书文件（以.cer和.p12为后缀的文件）和CRL文件（以.crl为后缀的文件）将被移动到该路径下保存，且原存储路径下的其它文件不受影响。

【举例】

\# 设置证书的存储路径为flash:/pki-new。

\<Sysname\> system-view

Sysname pki storage certificates flash:/pki-new

\# 设置CRL存储路径为pki-new。

\<Sysname\> system-view

Sysname pki storage crls pki-new

**PKI \-- PKI配置命令 \-- pki validate-certificate**

------------------------------------------------------------------------

**[pki validate-certificate**]命令用来验证证书的有效性。

【命令】

**[pki validate-certificate**[ **domain** *domain-name* { **ca** \| **local** } ]]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[domain** *domain-name*]：指定证书所在的PKI域的名称，为1～31个字符的字符串，不区分大小写，不能包括"\~"、"\*"、"\"、"[\|]"、":"、"."、"\<"、"\>"、"\""和"\'"。

**[ca**]：表示验证CA证书。

**[local**]：表示验证本地证书。

【使用指导】

证书验证的内容包括：证书是否由用户信任的CA签发；证书是否仍在有效期内；如果使能了CRL检查功能，还会验证证书是否被吊销。如果验证证书的时候，PKI域中没有CRL，则会先从本地证书库中查找是否存在CRL，如果找到CRL，则把证书库中保存的CRL加载到该PKI域中，否则，就从CA服务器上获取并保存到本地。

导入证书、申请证书、获取证书以及应用程序使用PKI功能时，都会自动对证书进行验证，因此一般不需要使用此命令进行额外的验证。如果用户希望在没有任何前述操作的情况下单独执行证书的验证，可以使用此命令。

验证CA证书时，会对从当前CA到根CA的整条CA证书链进行CRL检查。

【举例】

\# 验证PKI域aaa中的CA证书的有效性。

\<Sysname\> system-view

Sysname pki validate-certificate domain aaa ca

Verifying certificate\...\...

        Serial Number:

            f6:3c:15:31:fe:bb:ec:94:dc:3d:b9:3a:d9:07:70:e5

        Issuer:

            C=cn

            O=ccc

            OU=ppp

            CN=rootca

        Subject:

            C=cn

            O=abc

            OU=test

            CN=aca

Verify result: OK

Verifying certificate\...\...

        Serial Number:

            5c:72:dc:c4:a5:43:cd:f9:32:b9:c1:90:8f:dd:50:f6

Issuer:

            C=cn

            O=ccc

            OU=ppp

CN=rootca

        Subject:

            C=cn

            O=ccc

            OU=ppp

            CN=rootca

Verify result: OK

\# 验证PKI域aaa中的本地证书的有效性。

\<Sysname\> system-view

Sysname pki validate-certificate domain aaa local

Verifying certificate\...\...

        Serial Number:

            bc:05:70:1f:0e:da:0d:10:16:1e

        Issuer:

            C=CN

            O=sec

            OU=software

            CN=bca

        Subject:

            O=OpenCA Labs

            OU=Users

            CN=fips fips-sec

Verify result: OK

【相关命令】

·**crl check**

·**pki domain**

**PKI \-- PKI配置命令 \-- public-key dsa**

------------------------------------------------------------------------

**[public-key dsa**]命令用来指定证书申请使用的DSA密钥对。

**[undo public-key**]命令用来取消指定的密钥对。

【命令】

**[public-key dsa name*** key-name* [ **length** *key-length* ]]

**[undo public-key**]

【缺省情况】

未指定任何密钥对。

【视图】

PKI域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[name*** key-name*]：密钥对的名称，为1～64个字符的字符串，不区分大小写，只能包含字母、数字和连字符"-"。

**[length*** key-length*]：密钥的长度。非FIPS模式下，*key-length*的取值范围为512～2048，单位为比特，缺省值为1024；FIPS模式下，*key-length*的取值为2048，单位为比特，缺省值为2048。密钥越长，密钥安全性越高，但相关的公钥运算越耗时。

【使用指导】

本命令中引用的密钥对并不要求已经存在，可以通过以下任意一种途径获得：

·通过执行**public-key local create**命令生成。

·通过应用程序认证过程触发生成。例如IKE协商过程中，如果使用数字签名认证方式，则可能会触发生成密钥对。

·通过导入证书（使用**pki import**命令）的方式从外界获得。

一个PKI域中只能同时存在一种算法（RSA、DSA或ECDSA）的密钥对。对于RSA密钥对来说，一个PKI域中只允许单独存在一种用途的RSA密钥对，或同时存在一个用于签名的和一个用于加密的RSA密钥对。因此，在一个PKI域中，除RSA签名密钥对和RSA加密密钥对的配置不会互相覆盖之外，其它类型的新的密钥对配置均会覆盖已有的密钥对配置。

本命令中指定的密钥长度仅对将要由设备生成的密钥对有效。如果执行本命令时，设备上已经存在指定名称的密钥对，则后续通过此命令指定的该密钥对的密钥长度没有意义。如果指定名称的密钥对是通过导入证书的方式获得，则通过本命令指定的密钥长度也没有意义。

【举例】

\# 指定证书申请所使用的DSA密钥对为abc，密钥的长度为2048比特。

\<Sysname\> system-view

Sysname pki domain aaa

Sysname-pki-domain-aaa public-key dsa name abc length 2048

【相关命令】

·**pki import**

·**public-key local create**（安全命令参考/公钥管理）

**PKI \-- PKI配置命令 \-- public-key ecdsa**

------------------------------------------------------------------------

![说明](PKI命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[public-key ecdsa**]命令用来指定证书申请使用的ECDSA密钥对。

**[undo public-key**]命令用来取消指定的密钥对。

【命令】

**[public-key ecdsa name** *key-name*]

**[undo public-key**]

【缺省情况】

未指定任何密钥对。

【视图】

PKI域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[name** *key-name*]：密钥对的名称，为1～64个字符的字符串，不区分大小写，只能包含字母、数字和连字符"-"。

【使用指导】

本命令中引用的密钥对并不要求已经存在，可以通过以下任意一种途径获得：

·通过执行**public-key local create**命令生成。

·通过应用程序认证过程触发生成。例如IKE协商过程中，如果使用数字签名认证方式，则可能会触发生成密钥对。

·通过导入证书（使用**pki import**命令）的方式从外界获得。

一个PKI域中只能同时存在一种算法（RSA、DSA或ECDSA）的密钥对。对于RSA密钥对来说，一个PKI域中只允许单独存在一种用途的RSA密钥对，或同时存在一个用于签名的和一个用于加密的RSA密钥对。因此，在一个PKI域中，除RSA签名密钥对和RSA加密密钥对的配置不会互相覆盖之外，其它类型的新的密钥对配置均会覆盖已有的密钥对配置。

本命令中指定的密钥长度仅对将要由设备生成的密钥对有效。如果执行本命令时，设备上已经存在指定名称的密钥对，则后续通过此命令指定的该密钥对的密钥长度没有意义。如果指定名称的密钥对是通过导入证书的方式获得，则通过本命令指定的密钥长度也没有意义。

【举例】

\# 指定证书申请所使用的ECDSA密钥对为abc。

\<Sysname\> system-view

Sysname pki domain aaa

Sysname-pki-domain-aaa public-key ecdsa name abc

【相关命令】

·**pki import**

·**public-key local create**（安全命令参考/公钥管理）

**PKI \-- PKI配置命令 \-- public-key rsa**

------------------------------------------------------------------------

**[public-key rsa**]命令用来指定证书申请使用的RSA密钥对。

**[undo public-key**]命令用来取消指定的密钥对。

【命令】

**[public-key rsa **[ **encryption name** *encryption-key-name* [ **length** *key-length*  \| **signature name** *signature-key-name*  **length** *key-length*  } \* \| **general name** *key-name*  **length** *key-length*  }]]

**[undo public-key**]

【缺省情况】]

未指定任何密钥对。

【视图】

PKI域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[encryption**]：指定密钥对的用途为加密。

**[name*** encryption-key-name*]：加密密钥对的名称，为1～64个字符的字符串，不区分大小写，只能包含字母、数字和连字符"-"。

**[signature**]：指定密钥对的用途为签名。

**[name*** signature-key-name*]：签名密钥对的名称，为1～64个字符的字符串，不区分大小写，只能包含字母、数字和连字符"-"。

**[general**]：指定密钥对的用途为通用，既可以用于签名也可以用于加密。

**[name ***key-name*]：通用密钥对的名称，为1～64个字符的字符串，不区分大小写，只能包含字母、数字和连字符"-"。

**[length** *key-length*]：密钥的长度。非FIPS模式下，*key-length*的取值范围为512～2048，单位为比特，缺省为1024；FIPS模式下，*key-length*的取值为2048，单位为比特，缺省为2048。密钥越长，密钥安全性越高，但相关的公钥运算越耗时。

【使用指导】

本命令中引用的密钥对并不要求已经存在，可以通过以下任意一种途径获得：

·通过执行**public-key local create**命令生成。

·通过应用程序认证过程触发生成。例如IKE协商过程中，如果使用数字签名认证方式，则可能会触发生成密钥对。

·通过导入证书（使用**pki import**命令）的方式从外界获得。

一个PKI域中只能同时存在一种算法（RSA、DSA或ECDSA）的密钥对。对于RSA密钥对来说，一个PKI域中只允许单独存在一种用途的RSA密钥对，或同时存在一个用于签名的和一个用于加密的RSA密钥对。因此，在一个PKI域中，除RSA签名密钥对和RSA加密密钥对的配置不会互相覆盖之外，其它类型的新的密钥对配置均会覆盖已有的密钥对配置。

分别指定RSA签名密钥对和RSA加密密钥对时，它们的密钥长度可以不相同。

本命令中指定的密钥长度仅对将要由设备生成的密钥对有效。如果执行本命令时，设备上已经存在指定名称的密钥对，则后续通过此命令指定的该密钥对的密钥长度没有意义。如果指定名称的密钥对是通过导入证书的方式获得，则通过本命令指定的密钥长度也没有意义。

【举例】

\# 指定证书申请所使用的RSA密钥对为abc，密钥用途为通用，密钥的长度为2048比特。

\<Sysname\> system-view

Sysname pki domain aaa

Sysname-pki-domain-aaa public-key rsa general name abc length 2048

\# 指定证书申请所使用的加密RSA密钥对为rsa1（密钥的长度为2048比特），签名RSA密钥对为sig1（密钥的长度为2048比特）。

\<Sysname\> system-view

Sysname pki domain aaa

Sysname-pki-domain-aaa public-key rsa encryption name rsa1 length 2048

Sysname-pki-domain-aaa public-key rsa signature name sig1 length 2048

【相关命令】

·**pki import**

·**public-key local create**（安全命令参考/公钥管理）

**PKI \-- PKI配置命令 \-- root-certificate fingerprint**

------------------------------------------------------------------------

**[root-certificate fingerprint**]命令用来配置验证CA根证书时所使用的指纹。

**[undo root-certificate fingerprint**]命令用来取消配置的根证书指纹。

【命令】

非FIPS模式下：

**[root-certificate fingerprint **[{ **md5** \| **sha1** } *string*]]

**[undo root-certificate fingerprint**]

FIPS 模式下：

**[root-certificate fingerprint sha1 ***string*]

**[undo root-certificate fingerprint**]

【缺省情况】

未指定验证CA根证书时使用的指纹。

【视图】

PKI域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[md5**]：使用MD5指纹。

**[sha1**]：使用SHA1指纹。

*[string*]：指定所使用的指纹信息。当选择MD5指纹时，*string*必须为32个字符的字符串，并且以16进制的形式输入；当选择SHA1指纹时，*string*必须为40个字符的字符串，并且以16进制的形式输入。

【使用指导】

当本地证书申请模式为自动方式且PKI域中没有CA证书时，必须通过本命令配置验证CA证书时所使用的指纹。当IKE协商等应用触发设备进行本地证书申请时，设备会自动从CA服务器上获取CA证书，如果获取的CA证书中包含了本地不存在的CA根证书，则设备会验证该CA根证书的指纹。此时，如果设备上没有配置CA根证书指纹或者配置了错误的CA根证书指纹，则本地证书申请失败。

通过**pki import**命令导入CA证书或者通过**pki retrieval**命令获取CA证书时，可以选择是否配置验证CA根证书使用的指纹：如果PKI域中配置了验证CA根证书使用的指纹，则当导入的CA证书文件或者获取的CA证书中包含本地不存在的CA根证书时，直接使用配置的CA根证书指纹进行验证。如果配置了错误的CA根证书指纹，则CA证书导入和CA证书获取均会失败；否则，需要用户来确认该CA证书的CA根证书指纹是否可信。

【举例】

\# 配置验证CA根证书时使用的MD5指纹。（仅非FIPS模式下支持）

\<Sysname\> system-view

Sysname pki domain aaa

Sysname-pki-domain-aaa root-certificate fingerprint md5 12EF53FA355CD23E12EF53FA355CD23E

\# 配置验证CA根证书时使用的SHA1指纹。

\<Sysname\> system-view

Sysname pki domain aaa

Sysname-pki-domain-aaa root-certificate fingerprint sha1 D1526110AAD7527FB093ED7FC037B0B3CDDDAD93

【相关命令】

·**certificate request mode**

·**pki import**

·**pki retrieve-certificate**

**PKI \-- PKI配置命令 \-- rule**

------------------------------------------------------------------------

**[rule**]命令用来配置证书属性的访问控制规则。

**[undo rule**]命令用来删除指定的证书属性访问控制规则。

【命令】

**[rule** [ *id*  { **deny** \| **permit** } *group-nam*]*e*]

**[undo rule ***id*]

【缺省情况】

不存在证书属性的访问控制规则。

【视图】

证书访问控制策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[id*]：证书属性访问控制规则编号，取值范围为1～16，缺省值为当前还未被使用的且合法的最小编号，取值越小优先级越高。

**[deny**]：当证书的属性与所关联的属性组匹配时，认为该证书无效，未通过访问控制策略的检测。

**[permit**]：当证书的属性与所关联的属性组匹配时，认为该证书有效，通过了访问控制策略的检测。

*[group-name*]：规则所关联的证书属性组名称，为1～31个字符的字符串，不区分大小写。

【使用指导】

配置证书属性访问控制规则时，可以关联一个当前并不存在的证书属性组，后续可以通过命令**pki certificate attribute-group**完成相应的配置。

若规则所关联的证书属性组中没有定义任何属性规则（通过命令**attribute**配置），或关联的证书属性组不存在，则认为被检测的证书属性与该属性组匹配。

如果一个访问控制策略中有多个规则，则按照规则编号从小到大的顺序遍历所有规则，一旦证书与某一个规则匹配，则立即结束检测，不再继续匹配其它规则；若遍历完所有规则后，证书没有与任何规则匹配，则认为该证书不能通过访问控制策略的检测。

【举例】

\# 配置一个访问控制规则，要求当证书与证书属性组mygroup匹配时，认为该证书有效，通过了访问控制策略的检测。

\<Sysname\> system-view

Sysname pki certificate access-control-policy mypolicy

Sysname-pki-cert-acp-mypolicy rule 1 permit mygroup

【相关命令】

·**attribute**

·**display pki certificate access-control-policy**

·**pki certificate attribute-group**

**PKI \-- PKI配置命令 \-- source**

------------------------------------------------------------------------

**[source**]命令用来指定PKI操作产生的协议报文使用的源IP地址。

**[undo source**]命令用来取消指定的源IP地址。

【命令】

**[source **[{ **ip** \| **ipv6** } { *ip-address* *\|* **interface** *interface-type interface-number* }]]

**[undo source**]

【缺省情况】

PKI操作产生的协议报文的源IP地址为系统根据路由表项查找到的出接口的地址。

【视图】

PKI域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip **]*ip-address*：指定源IPv4地址。

**[ipv6 **]*ip-address*：指定源IPv6地址。

**[interface **]*interface-type interface-number*：指定该接口的主IPv4地址或接口上最小的IPv6地址为源IP地址。*interface-type interface-number*表示接口类型和接口编号。

【使用指导】

如果希望PKI操作产生的协议报文的源IP地址是一个特定的地址，则需要配置此命令，例如CA服务器上的策略要求仅接受来自指定地址或网段的证书申请。如果该IP地址是动态获取的，则可以指定一个接口，使用该接口上的IP地址作为源地址。

此处指定的源IP地址，必须与CA服务器之间路由可达。

一个PKI域中只能存在一个源IP地址，后配置的生效。

【举例】

\# 指定PKI操作产生的协议报文的源IP地址为111.1.1.8。

\<Sysname\> system-view

Sysname pki domain aaa

Sysname-pki-domain-aaa source ip 111.1.1.8

\# 指定PKI操作产生的协议报文的源IPv6地址为1::8。

\<Sysname\> system-view

Sysname pki domain 1

Sysname-pki-domain-1 source ipv6 1::8

\# 指定PKI操作产生的协议报文的源IP地址为接口GigabitEthernet1/0/1的IP地址。

\<Sysname\> system-view

Sysname pki domain aaa

Sysname-pki-domain-aaa source ip interface gigabitethernet 1/0/1

\# 指定PKI操作产生的协议报文的源IPv6地址为接口GigabitEthernet1/0/1的IPv6地址。

\<Sysname\> system-view

Sysname pki domain 1

Sysname-pki-domain-1 source ipv6 interface gigabitethernet 1/0/1

**PKI \-- PKI配置命令 \-- state**

------------------------------------------------------------------------

**[state**]命令用来配置PKI实体所属的州或省的名称。

**[undo state**]命令用来删除配置的PKI所属的州或省的名称。

【命令】

**[state ***state-name*]

**[undo state**]

【缺省情况】

未配置PKI实体所属的州或省的名称。

【视图】

PKI实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[state-name*]：PKI实体所属的州或省的名称，为1～63个字符的字符串，区分大小写，不能包含逗号。

【举例】

\# 配置PKI实体en所在省为countryA。

\<Sysname\> system-view

Sysname pki entity en

Sysname-pki-entity-en state countryA

**PKI \-- PKI配置命令 \-- usage**

------------------------------------------------------------------------

**[usage**]命令用来指定证书的扩展用途。

**[undo usage**]命令用来删除指定证书的扩展用途。

【命令】

**[usage **[{ **ike** \| **ssl-client** \| **ssl-server** } **\***]]

**[undo usage **[[ **ike** \| **ssl-client** \| **ssl-server** ] **\***]]

【缺省情况】

未指定证书的扩展用途，表示可用于所有用途。

【视图】

PKI域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ike**]：指定证书扩展用途为IKE，即IKE对等体使用的证书。

**[ssl-client**]：指定证书扩展用途为SSL客户端，即SSL客户端使用的证书。

**[ssl-server**]**：**指定证书扩展用途为SSL服务器端，即SSL服务器端使用的证书。

【使用指导】

若不指定任何参数，则**undo usage**命令表示删除所有指定的证书扩展用途，证书的用途由证书的使用者决定，PKI不做任何限定。

证书中携带的扩展用途与CA服务器的策略相关，申请到的证书中的扩展用途可能与此处指定的不完全一致，最终请以CA服务器的实际情况为准。

【举例】

\# 指定证书扩展用途为IKE。

\<Sysname\> system-view

Sysname pki domain aaa

Sysname-pki-domain-aaa usage ike
