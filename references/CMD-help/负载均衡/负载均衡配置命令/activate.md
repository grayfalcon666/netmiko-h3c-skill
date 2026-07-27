<!-- CMD-INDEX
  activate                            | 实服务组视图           | L112
  case-insensitive                    | 参数模板视图           | L164
  check all-packet                    | 持续性组视图           | L214
  class                               | 负载均衡策略视图         | L264
  connection-limit (real server view) | 实服务器视图           | L320
  connection-limit (virtual server view) | 虚服务器视图           | L362
  connection-sync enable              | 虚服务器视图           | L404
  content                             | 持续性组视图           | L452
  content maxparse-length             | 参数模板视图           | L512
  cookie                              | 持续性组视图           | L560
  cookie secondary name               | 持续性组视图           | L638
  default server-farm                 | 虚服务器视图           | L686
  default-class action                | 负载均衡策略视图         | L736
  description                         | 负载均衡动作视图/负载均衡类视图/负载均衡策略视图/参数模板视图/实服务器视图/实服务组视图/SNAT地址池视图/持续性组视图/虚服务器视图 | L784
  display loadbalance action          | 任意视图             | L890
  display loadbalance class           | 任意视图             | L1100
  display loadbalance hot-backup statistics | 任意视图             | L1206
  display loadbalance policy          | 任意视图             | L1368
  display loadbalance snat-pool       | 任意视图             | L1452
  display parameter-profile           | 任意视图             | L1544
  display real-server                 | 任意视图             | L1712
  display real-server statistics      | 任意视图             | L1910
  display server-farm                 | 任意视图             | L2096
  display sticky                      | 任意视图             | L2392
  display sticky-group                | 任意视图             | L2610
  display virtual-server              | 任意视图             | L2882
  display virtual-server statistics   | 任意视图             | L3126
  exceed-mss                          | 参数模板视图           | L3312
  fail-action                         | 实服务组视图           | L3360
  forward all                         | 负载均衡动作视图         | L3406
  header                              | 持续性组视图           | L3454
  header delete                       | 负载均衡动作视图         | L3518
  header exceed-length                | 参数模板视图           | L3572
  header insert                       | 负载均衡动作视图         | L3626
  header maxparse-length              | 参数模板视图           | L3690
  header modify per-request           | 参数模板视图           | L3738
  header rewrite                      | 负载均衡动作视图         | L3780
  ip                                  | 持续性组视图           | L3838
  ip address                          | 实服务器视图           | L3900
  ip range                            | SNAT地址池视图        | L3942
  ipv6                                | 持续性组视图           | L3990
  ipv6 address                        | 实服务器视图           | L4052
  ipv6 range                          | SNAT地址池视图        | L4094
  lb-policy                           | 虚服务器视图           | L4142
  loadbalance action                  | 系统视图             | L4190
  loadbalance class                   | 系统视图             | L4234
  loadbalance policy                  | 系统视图             | L4280
  loadbalance snat-pool               | 系统视图             | L4324
  match class                         | 负载均衡类视图          | L4366
  match content                       | 负载均衡类视图          | L4418
  match cookie                        | 负载均衡类视图          | L4476
  match header                        | 负载均衡类视图          | L4530
  match method                        | 负载均衡类视图          | L4584
  match source                        | 负载均衡类视图          | L4660
  match url                           | 负载均衡类视图          | L4716
  parameter                           | 虚服务器视图           | L4766
  parameter-profile                   | 系统视图             | L4814
  payload                             | 持续性组视图           | L4862
  port (real server view)             | 实服务器视图           | L4918
  port (virtual server view)          | 虚服务器视图           | L4968
  predictor                           | 实服务组视图           | L5018
  priority                            | 实服务器视图           | L5078
  probe (real server view)            | 实服务器视图           | L5120
  probe (server farm view)            | 实服务组视图           | L5180
  rate-limit bandwidth (real server view) | 实服务器视图           | L5240
  rate-limit bandwidth (virtual server view) | 虚服务器视图           | L5306
  rate-limit connection (real server view) | 实服务器视图           | L5372
  rate-limit connection (virtual server view) | 虚服务器视图           | L5414
  real-server                         | 系统视图             | L5456
  rebalance per-request               | 参数模板视图           | L5498
  redirect relocation                 | 虚服务器视图           | L5540
  redirect return-code                | 虚服务器视图           | L5590
  reset loadbalance hot-backup statistics | 用户视图             | L5644
  reset real-server statistics        | 用户视图             | L5676
  reset virtual-server statistics     | 用户视图             | L5710
  secondary-cookie delimiters         | 参数模板视图           | L5744
  secondary-cookie start              | 参数模板视图           | L5790
  selected-server                     | 实服务组视图           | L5836
  server-connection reuse             | 参数模板视图           | L5894
  server-farm (LB action view)        | 负载均衡动作视图         | L5940
  server-farm (real server view)      | 实服务器视图           | L5998
  server-farm (system view)           | 系统视图             | L6040
  service enable                      | 虚服务器视图           | L6086
  set ip tos (LB action view)         | 负载均衡动作视图         | L6124
  set ip tos (parameter profile view) | 参数模板视图           | L6166
  shutdown                            | 实服务器视图           | L6212
  slow-online                         | 实服务组视图           | L6250
  slow-shutdown enable                | 实服务器视图           | L6298
  snat-pool                           | 实服务组视图           | L6348
  snmp-agent trap enable loadbalance  | 系统视图             | L6394
  ssl session-id                      | 持续性组视图           | L6434
  ssl url rewrite                     | 负载均衡动作视图         | L6478
  ssl-client-policy (LB action view)  | 负载均衡动作视图         | L6530
  ssl-client-policy (virtual server view) | 虚服务器视图           | L6578
  ssl-server-policy                   | 虚服务器视图           | L6626
  sticky-group                        | 系统视图             | L6674
  sticky-sync enable                  | 虚服务器视图           | L6722
  success-criteria (real server view) | 实服务器视图           | L6766
  success-criteria (server farm view) | 实服务组视图           | L6818
  tcp window-size                     | 参数模板视图           | L6870
  timeout                             | 持续性组视图           | L6916
  transparent enable                  | 实服务组视图           | L6958
  udp per-packet                      | 虚服务器视图           | L7000
  virtual ip address                  | 虚服务器视图           | L7052
  virtual ipv6 address                | 虚服务器视图           | L7098
  virtual-server                      | 系统视图             | L7142
  vpn-instance                        | 虚服务器视图           | L7186
  weight                              | 实服务器视图           | L7228
-->

**负载均衡 \-- 负载均衡配置命令 \-- activate**

------------------------------------------------------------------------

**[activate**]命令用来配置实服务组的可用条件。

**[undo** **activate**]命令用来恢复缺省情况。

【命令】

**[activate** **lower** *lower-percentage* **upper** *upper-percentage*]

**[undo** **activate**]

【缺省情况】

实服务组中只要有一个实服务器可用，该实服务组就被认为可用。

【视图】

实服务组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[lower** *lower-percentage*]：最小可用百分比，取值范围为1～99。当主用实服务组中可用的实服务器数量占实服务器总数量的百分比低于此值时，该实服务组将被认为不可用，从而切换到备用实服务组。

**[upper** *upper-percentage*]：最大可用百分比，取值范围为1～99，且必须大于等于最小可用百分比。当主用实服务组中可用的实服务器数量占实服务器总数量的百分比高于此值时，将从备用实服务组切换回主用实服务组。

【使用指导】

需要注意的是，当虚服务器上未配置备用实服务组时，本配置无效。

【举例】

\# 配置实服务组sf的最小可用百分比为20，最大可用百分比为80。

\<Sysname\> system-view

Sysname server-farm sf

Sysname-sfarm-sf activate lower 20 upper 80

【相关命令】

·**default****server-farm**

**负载均衡 \-- 负载均衡配置命令 \-- case-insensitive**

------------------------------------------------------------------------

**[case-insensitive**]命令用来配置匹配字符串时对大小写不敏感。

**[undo****case-insensitive**]命令用来恢复缺省情况。

【命令】

**[case-insensitive**]

**[undo****case-insensitive**]

【缺省情况】

匹配字符串时对大小写敏感。

【视图】

参数模板视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本命令只在HTTP类型的参数模板视图下支持。

本命令将影响以下内容：

·对于类匹配，影响HTTP首部的取值、HTTP Cookie的名称和取值、URL。

·对于HTTP首部持续性方法，影响首部的取值、URL以及用于生成持续性表项的Key值。

·对于Cookie截取持续性方法，影响Cookie的名称和取值的匹配以及用于生成持续性表项的Key值。

【举例】

\# 在HTTP类型的参数模板pp1中，配置匹配字符串时对大小写不敏感。

\<Sysname\> system-view

Sysname parameter-profile pp1 type http

Sysname-para-http-pp1 case-insensitive

**负载均衡 \-- 负载均衡配置命令 \-- check all-packet**

------------------------------------------------------------------------

**[check** **all-packet**]命令用来配置检查所有报文。

**[undo** **check** **all-packet**]命令用来恢复缺省情况。

【命令】

**[check** **all-packet**]

**[undo****check** **all-packet**]

【缺省情况】

不检查所有报文。

【视图】

持续性组视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本命令只在HTTP Cookie类型的持续性组视图下支持。

需要注意的是：

·当持续性方法为Cookie截取时，本命令用来配置是否从所有HTTP应答报文中截取Cookie。如果未配置本命令，则在一次连接中只从首个应答报文中截取一次Set-Cookie信息，后续应答报文不再截取。

·当持续性方法为Cookie重写时，本命令用来配置是否在所有HTTP应答报文中重写Cookie。如果未配置本命令，则在一次连接中只在首个应答报文中重写Set-Cookie信息，后续应答报文不再重写。

·当持续性方法为Cookie插入时，本命令用来配置是否向所有HTTP应答报文中插入Cookie。如果未配置本命令，则在一次连接中只向首个应答报文中插入Set-Cookie信息，后续应答报文不再插入。

【举例】

\# 在HTTP Cookie类型的持续性组sg3中，配置检查所有报文。

\<Sysname\> system-view

Sysname sticky-group sg3 type http-cookie

Sysname-sticky-http-cookie-sg3 check all-packet

**负载均衡 \-- 负载均衡配置命令 \-- class**

------------------------------------------------------------------------

**[class**]命令用来为负载均衡类指定负载均衡动作。

**[undo** **class**]命令用来删除指定的负载均衡类。

【命令】

**[class** *class-name* [ **insert-before** *before-class-name*  **action** *action-name*]]

**[undo** **class** *class-name*]

【缺省情况】

没有为任何负载均衡类指定负载均衡动作。

【视图】

负载均衡策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[class-name*]：负载均衡类的名称，为1～63个字符的字符串，不区分大小写。

**[insert-before** *before-class-name*]：表示插入到指定的负载均衡类之前（该负载均衡类必须已被当前负载均衡策略引用）。*before-class-name*为1～63个字符的字符串，不区分大小写。

*[action-name*]：负载均衡动作的名称，为1～63个字符的字符串，不区分大小写。

【使用指导】

通过本命令可以为匹配特定负载均衡类的报文指定其执行的负载均衡动作。

需要注意的是：

·不同的负载均衡类可以与同一负载均衡动作组成匹配规则。

·通用类型的负载均衡策略只能引用通用类型的负载均衡类和负载均衡动作，HTTP类型的负载均衡策略则无此限制。

【举例】

\# 在通用类型的负载均衡策略lbp1中，为负载均衡类lbc1指定负载均衡动作为lba1，并将lbc1插入到负载均衡类lbc0之前。

\<Sysname\> system-view

Sysname loadbalance policy lbp1 type generic

Sysname-lbp-generic-lbp1 class lbc1 insert-before lbc0 action lba1

**负载均衡 \-- 负载均衡配置命令 \-- connection-limit (real server view)**

------------------------------------------------------------------------

**[connection-limit**]命令用来配置实服务器所允许的最大连接数。

**[undo**]**connection-limit**命令用来恢复缺省情况。

【命令】

**[connection-limit** **max** *max-number*]

**[undo**] **connection-limit**

【缺省情况】

实服务器所允许的最大连接数为0，即不受限制。

【视图】

实服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[max-number*]：最大连接数，取值范围为0～4294967295，0表示实服务器所允许的最大连接数不受限制。

【举例】

\# 配置实服务器rs所允许的最大连接数为10000。

\<Sysname\> system-view

Sysname real-server rs

Sysname-rserver-rs connection-limit max 10000

**负载均衡 \-- 负载均衡配置命令 \-- connection-limit (virtual server view)**

------------------------------------------------------------------------

**[connection-limit**]命令用来配置虚服务器所允许的最大连接数。

**[undo**]**connection-limit**命令用来恢复缺省情况。

【命令】

**[connection-limit** **max** *max-number*]

**[undo**]**connection-limit**

【缺省情况】

虚服务器所允许的最大连接数为0，即不受限制。

【视图】

虚服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[max-number*]：最大连接数，取值范围为0～4294967295，0表示虚服务器所允许的最大连接数不受限制。

【举例】

\# 配置IP类型的虚服务器vs3所允许的最大连接数为10000。

\<Sysname\>system-view

Sysname virtual-server vs3 type ip

Sysname-vs-ip-vs3 connection-limit max 10000

**负载均衡 \-- 负载均衡配置命令 \-- connection-sync enable**

------------------------------------------------------------------------

![说明](负载均衡命令.files/image001.png)

集中式设备不支持本命令，请以设备的实际情况为准。

****

**[connection-sync** **enable**]命令用来开启虚服务器的会话扩展信息备份功能。

**[undo****connection-sync** **enable**]命令用来关闭虚服务器的会话扩展信息备份功能。

【命令】

**[connection-sync** **enable**]

**[undo****connection-sync** **enable**]

【缺省情况】

虚服务器的会话扩展信息备份功能处于关闭状态。

【视图】

虚服务器视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本命令在HTTP类型的虚服务器视图下不支持。

【举例】

\# 开启IP类型的虚服务器vs3的会话扩展信息备份功能。

\<Sysname\>system-view

Sysname virtual-server vs3 type ip

Sysname-vs-ip-vs3 connection-sync enable

**负载均衡 \-- 负载均衡配置命令 \-- content**

------------------------------------------------------------------------

**[content**]命令用来配置HTTP实体持续性方法。

**[undo****content**]命令用来删除HTTP实体持续性方法。

【命令】

**[content** [ **offset** *offset*   **start** *start-string*  [ **end** *end-string* \| **length** *length* ]]]

**[undo****content**]

【缺省情况】

不存在任何持续性方法。

【视图】

持续性组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[offset** *offset*]：实体基于HTTP报文起始位置的偏移量，取值范围为0～1000，缺省值为0。

**[start** *start-string*]：实体开始标记的正则表达式，即从*offset*起到本标记为开始，为1～127字符的字符串。

**[end** *end-string*]：实体结束标记的正则表达式，即从*start-string*起到本标记为结束，为1～127字符的字符串。

**[length** *length*]：实体的长度，取值范围为0～1000，缺省值为0，表示所有长度。

【使用指导】

本命令只在HTTP实体类型的持续性组视图下支持。

本命令用来根据*offset*、*start-string*、*end-string*及*length*获取生成持续性表项的HTTP实体信息。*start-string*和*end-string*将不计入持续性表项信息中。

需要注意的是：

·HTTP实体持续性只能对实体内的所有内容进行持续性处理，对于chunk及multipart形式的实体内容，HTTP实体持续性不能根据具体内容进行明确的持续性处理。

·快速HTTP类型的虚服务器不支持引用HTTP实体持续性方法。

【举例】

\# 在HTTP实体类型的持续性组sg2中，配置HTTP实体持续性方法为：从HTTP报文起始位置的第30个字节起，以abc为开始、长度为20个字节的HTTP实体来生成持续性表项。

\<Sysname\> system-view

Sysname sticky-group sg2 type http-content

Sysname-sticky-http-content-sg2 content offset 30 start abc length 20

**负载均衡 \-- 负载均衡配置命令 \-- content maxparse-length**

------------------------------------------------------------------------

**[content** **maxparse-length**]命令用来配置HTTP实体的最大解析长度。

**[undo****content** **maxparse-length**]命令用来恢复缺省情况。

【命令】

**[content** **maxparse-length** *length*]

**[undo****content** **maxparse-length**]

【缺省情况】

HTTP实体的最大解析长度为4096。

【视图】

参数模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[length*]：HTTP实体的最大解析长度，取值范围为1～65535。

【使用指导】

本命令只在HTTP类型的参数模板视图下支持。

需要注意的是，快速HTTP类型的虚服务器不支持本功能。

【举例】

\# 在HTTP类型的参数模板pp1中，配置HTTP实体的最大解析长度为8192。

\<Sysname\> system-view

Sysname parameter-profile pp1 type http

Sysname-para-http-pp1 content maxparse-length 8192

**负载均衡 \-- 负载均衡配置命令 \-- cookie**

------------------------------------------------------------------------

**[cookie**]命令用来配置HTTP Cookie持续性方法。

**[undo** **cookie**]命令用来删除HTTP Cookie持续性方法。

【命令】

**[cookie** { **get** **name** *cookie-name* [ **offset** *offset*   **start** *start-string* [ **end** *end-string* \| **length** *length* ] \| { **insert** \| **rewrite** }  **name** *cookie-name*  }]]

**[undo****cookie**[ { **get** \| **insert** \| **rewrite** }]]

【缺省情况】

不存在任何持续性方法。

【视图】

持续性组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[get**]：表示持续性方法为Cookie截取，即在服务器发送的HTTP应答报文中截取Set-Cookie字段用于持续性处理。

*[cookie-name*]：HTTP Cookie的名称，为1～63个字符的字符串，区分大小写。

**[offset** *offset*]：Cookie基于HTTP报文起始位置的偏移量，取值范围为0～1000，缺省值为0。

**[start** *start-string*]：Cookie开始标记的正则表达式，即从*offset*起到本标记为开始，为1～127字符的字符串。

**[end** *end-string*]：Cookie结束标记的正则表达式，即从*start-string*起到本标记为结束，为1～127字符的字符串。

**[length** *length*]：Cookie的长度，取值范围为0～1000，缺省值为0，表示所有长度。

**[insert**]：表示持续性方法为Cookie插入，即在服务器发送的HTTP应答报文中插入Set-Cookie字段用于持续性处理。

**[rewrite**]：表示持续性方法为Cookie重写，即改写服务器发送的HTTP应答报文所携带的Set-Cookie字段用于持续性处理。

**[name** *cookie-name*]：HTTP Cookie的名称，为1～63个字符的字符串，区分大小写，缺省值为X-LB。

【使用指导】

本命令只在HTTP Cookie类型的持续性组视图下支持。

**[cookie** **get**]命令用来根据*offset*、*start-string*、*end-string*及*length*获取生成持续性表项的HTTP Cookie信息。*start-string*和*end-string*将不计入持续性表项信息中。

需要注意的是：

·当持续性方法为Cookie重写时，需要与HTTP服务器配合，即服务器发送的HTTP应答报文中应携带指定名称Cookie的Set-Cookie首部信息；此外，系统仅修改Set-Cookie中Cookie的名称和值，不会修改其它属性（如Expires等）。

·当持续性方法为Cookie插入或Cookie重写时，所配置的持续性老化时间不为会话老化（持续性表项的超时时间为0时），会在对应插入或重写的Value值后加入Expires字段。如果服务器发送的HTTP应答报文也携带此属性，负载均衡模块不会修改服务器所携带的该属性，而是在Value值后新增用户配置的Expires信息。因此在与服务器配合设置Cookie重写持续性方法时，建议服务器对于被负载均衡模块重写的Set-Cookie首部不要携带任何表征超时的属性。

【举例】

\# 在HTTP Cookie类型的持续性组sg3中，配置持续性方法为Cookie截取，即：截取从HTTP报文起始位置的第10个字节起，长度为32个字节的名为user的HTTP Cookie来生成持续性表项。

\<Sysname\> system-view

Sysname sticky-group sg3 type http-cookie

Sysname-sticky-http-cookie-sg3 cookie get name user offset 10 length 32

\# 在HTTP Cookie类型的持续性组sg3中，配置持续性方法为Cookie插入。

\<Sysname\> system-view

Sysname sticky-group sg3 type http-cookie

Sysname-sticky-http-cookie-sg3 cookie insert

**负载均衡 \-- 负载均衡配置命令 \-- cookie secondary name**

------------------------------------------------------------------------

**[cookie** **secondary** **name**]命令用来指定需在URI中查找的Secondary Cookie名称。

**[undo****cookie** **secondary** **name**]命令用来恢复缺省情况。

【命令】

**[cookie** **secondary** **name** *value*]

**[undo** **cookie** **secondary** **name**]

【缺省情况】

未指定需在URI中查找的Secondary Cookie名称。

【视图】

持续性组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：Secondary Cookie的名称，为1～63个Token字符，区分大小写，不包括(、)、\<、\>、@、,、;、:、\、\"、/、、、?、=、[、}、SP（空格符）、HT（水平制表符），以及ASCII码小于或等于31，大于或等于127的字符。

【使用指导】]

本命令只在HTTP Cookie类型的持续性组视图下支持。

需要注意的是，本命令只对Cookie截取持续性方法生效。即：当配置了Cookie截取持续性方法时，如果也配置了本命令，此时系统如果未能在HTPP请求报文首部找到指定名称的Cookie，便会查找出现在URI中的Secondary Cookie。

【举例】

\# 在HTTP Cookie类型的持续性组sg3中，指定需在URI中查找的Secondary Cookie名称为sid。

\<Sysname\> system-view

Sysname sticky-group sg3 type http-cookie

Sysname-sticky-http-cookie-sg3 cookie secondary name sid

**负载均衡 \-- 负载均衡配置命令 \-- default server-farm**

------------------------------------------------------------------------

**[default****server-farm**]命令用来指定默认的实服务组。

**[undo** **default** **server-farm**]命令用来恢复缺省情况。

【命令】

**[default** **server-farm** *server-farm-name* [ **backup** *backup-server-farm-name*   **sticky** *sticky-name* ]]

**[undo** **default** **server-farm**]

【缺省情况】

没有指定默认的实服务组。

【视图】

虚服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[server-farm-name*]：主用实服务组的名称，为1～63个字符的字符串，不区分大小写。

**[backup** *backup-**server-farm-name*]：备用实服务组的名称，为1～63个字符的字符串，不区分大小写。

**[sticky***sticky-name*]：持续性组的名称，为1～63个字符的字符串，不区分大小写。

【使用指导】

当主用实服务组可用（该实服务组存在且有可用的实服务器）时，虚服务器通过主用实服务组进行转发；当主用实服务组不可用而备用实服务组可用时，虚服务器通过备用实服务组进行转发。

【举例】

\# 为IP类型的虚服务器vs3指定默认的主用实服务组为sf，备用实服务组为sfb，持续性组名称为sg1。

\<Sysname\> system-view

Sysname virtual-server vs3 type ip

Sysname-vs-ip-vs3 default server-farm sf backup sfb sticky sg1

**负载均衡 \-- 负载均衡配置命令 \-- default-class action**

------------------------------------------------------------------------

**[default-class** **action**]命令用来配置默认的负载均衡动作。

**[undo** **default-class**]命令用来恢复缺省情况。

【命令】

**[default-class** **action** *action-name*]

**[undo** **default-class**]

【缺省情况】

未指定默认的负载均衡动作。

【视图】

负载均衡策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[action-name*]：负载均衡动作的名称，为1～63个字符的字符串，不区分大小写。

【使用指导】

通过本命令可以为未匹配任何负载均衡类的报文指定其执行的默认动作。

需要注意的是，通用类型的负载均衡策略只能用通用类型的负载均衡动作作为其默认的负载均衡动作，HTTP类型的负载均衡策略则无此限制。

【举例】

\# 在通用类型的负载均衡策略lbp1中，配置默认的负载均衡动作为lba1。

\<Sysname\> system-view

Sysname loadbalance policy lbp1 type generic

Sysname-lbp-generic-lbp1 default-class action lba1

**负载均衡 \-- 负载均衡配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来配置描述信息。

**[undo** **description**]命令用来恢复缺省情况。

【命令】

**[description** *text*]

**[undo** **description**]

【缺省情况】

不存在任何描述信息。

【视图】

负载均衡动作视图/负载均衡类视图/负载均衡策略视图/参数模板视图/实服务器视图/实服务组视图/SNAT地址池视图/持续性组视图/虚服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：描述信息，为1～127个字符的字符串，区分大小写。

【举例】

\# 配置通用类型的负载均衡动作lba1的描述信息为"LB action LBA1"。

\<Sysname\> system-view

Sysname loadbalance action lba1 type generic

Sysname-lba-generic-lba1 description LB action LBA1

\# 配置通用类型的负载均衡类lbc1的描述信息为"LB class LBC1"。

\<Sysname\> system-view

Sysname loadbalance class lbc1 type generic

Sysname-lbc-generic-lbc1 description LB class LBC1

\# 配置通用类型的负载均衡策略lbp1的描述信息为"LB policy LBP1"。

\<Sysname\> system-view

Sysname loadbalance policy lbp1 type generic

Sysname-lbp-generic-lbp1 description LB policy LBP1

\# 配置IP类型的参数模板pp2的描述信息为"Parameter profile PP2"。

\<Sysname\> system-view

Sysname parameter-profile pp2 type ip

Sysname-para-ip-pp2 description Parameter profile PP2

\# 配置实服务器rs的描述信息为"Real server RS"。

\<Sysname\> system-view

Sysname real-server rs

Sysname-rserver-rs description Real server RS

\# 配置实服务组sf的描述信息为"Server farm SF"。

\<Sysname\> system-view

Sysname server-farm sf

Sysname-sfarm-sf description Server farm SF

\# 配置SNAT地址池lbsp的描述信息为"SNAT pool LBSP"。

\<Sysname\> system-view

Sysname loadbalance snat-pool lbsp

Sysname-lbsnat-pool-lbsp description SNAT pool LBSP

\# 配置持续性组sg1的描述信息为"Sticky group SG1"。

\<Sysname\> system-view

Sysname sticky-group sg1 type address-port

Sysname-sticky-address-port-sg1 description Sticky group SG1

\# 配置IP类型的虚服务器vs3的描述信息为"Virtual server VS"。

\<Sysname\> system-view

Sysname virtual-server vs3 type ip

Sysname-vs-ip-vs3 description Virtual server VS

**负载均衡 \-- 负载均衡配置命令 \-- display loadbalance action**

------------------------------------------------------------------------

**[display** **loadbalance** **action**]命令用来显示负载均衡动作的信息。

【命令】

**[display** **loadbalance** **action** [ **name** *action-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[name** *action-name*]：显示指定负载均衡动作的信息。*action-name*为负载均衡动作的名称，为1～63个字符的字符串，不区分大小写。如果未指定本参数，将显示所有负载均衡动作的信息。

【举例】

\# 显示所有负载均衡动作的信息。

\<Sysname\> display loadbalance action

LB action: lba1

  Description:

  Type: Generic

  State: Inactive

  Forward type: Drop

  IP ToS:

LB action: lba2

  Description:

  Type: HTTP

  State: Active

  Forward type: Server farm

  Server farm: sf (in use)

  Backup server farm: sfb

  Sticky: sg3

  IP ToS: 20

  SSL client policy:

  Header delete:

    Name: ww

    Direction: Request

  Header insert:

    Name: aa

    Value: 1234567890123456789012345678901234567890123456789012345678901234567890

    Direction: Both

  Header insert:

    Name: cc

    Value: dd

    Direction: Request

  Header rewrite:

    Name: ee

    Value: dd

    Replacement: ff

    Direction: Response

  SSL URL rewrite:

    Value: 12

    Clear port: 12

    SSL port: 123

表1-1 display loadbalance action命令显示信息描述表

字段

描述

LB action

负载均衡动作的名称

Description

负载均衡动作的描述信息

Type

负载均衡动作的类型，包括：

·Generic：表示通用类型

·HTTP：表示HTTP类型

State

负载均衡动作的状态，包括：

·Active：可用

·Inactive：不可用

Forward type

负载均衡动作中的报文转发模式，包括：

·Drop：丢弃

·Forward：正常转发

·Server farm：通过实服务组指导转发

Server farm

指导转发的主用实服务组名称，(in use)表示该实服务组正被使用。只有当报文转发模式为server farm时才会显示本字段

Backup server farm

指导转发的备用实服务组名称，(in use)表示该实服务组正被使用。只有当报文转发模式为server farm时才会显示本字段

Sticky

指导转发的持续性组名称，只有当报文转发模式为server farm时才会显示本字段

IP ToS

IP报文的ToS字段值

SSL client policy

SSL客户端策略的名称，只有HTTP类型的负载均衡动作才会显示本字段

Header delete

删除HTTP首部的配置，其中：

·Name：HTTP报文首部的名称

·Direction：HTTP报文的方向，包括Both、Request和Response

只有配置了**header** **delete**命令才会显示本字段

Header insert

插入HTTP首部的配置，其中：

·Name：要插入HTTP报文中的首部名称

·Value：要插入HTTP报文中的首部内容

·Direction：HTTP报文的方向，包括Both、Request和Response

只有配置了**header** **insert**命令才会显示本字段

Header rewrite

重写HTTP首部的配置，其中：

·Name：HTTP报文首部的名称

·Value：要被重写的HTTP报文首部的内容

·Replacement：重写后的内容

·Direction：HTTP报文的方向，包括Both、Request和Response

只有配置了**header** **rewrite**命令才会显示本字段

SSL URL rewrite

重写服务器发送的HTTP应答报文Location首部的URL的配置，其中：

·Value：Location首部URL的正则表达式

·Clear port：原HTTP端口号

·SSL port：重写后的SSL端口号

只有配置了**ssl** **url** **rewrite**命令才会显示本字段

**负载均衡 \-- 负载均衡配置命令 \-- display loadbalance class**

------------------------------------------------------------------------

**[display** **loadbalance** **class**]命令用来显示负载均衡类的信息。

【命令】

**[display** **loadbalance** **class** [ **name** *class-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[name** *class-name*]：显示指定负载均衡类的信息。*class-name*为负载均衡类的名称，为1～63个字符的字符串，不区分大小写。如果未指定本参数，将显示所有负载均衡类的信息。

【举例】

\# 显示所有负载均衡类的信息。

\<Sysname\> display loadbalance class

LB class: lbc1

  Description:

  Type: HTTP

  Match type: Match-all

  Match rule:

    match 1 source ip address 1.2.3.0 24

    match 2 source ipv6 address 1::2

    match 3 cookie abc value 123

    match 4 header def value 12

    match 5 method ext xde

    match 6 method rfc CONNECT

    match 7 class cla2

    match 8 url 2q3

LB class: lbc2

  Description:

  Type: Generic

  Match type: Match-any

  Match rule:

    match 1 class cla2

    match 2 source ip address 1.2.23.0 24

    match 3 source ipv6 address 1::12

表1-2 display loadbalance class命令显示信息描述表

字段

描述

LB class

负载均衡类的名称

Description

负载均衡类的描述信息

Type

负载均衡类的类型，包括：

·Generic：表示通用类型

·HTTP：表示HTTP类型

Match type

负载均衡类的匹配类型，包括：

·Match-all：表示需要匹配所有规则才算匹配该类

·Match-any：表示只需匹配任一规则就算匹配该类

Match rule

负载均衡类包含的匹配规则

**负载均衡 \-- 负载均衡配置命令 \-- display loadbalance hot-backup statistics**

------------------------------------------------------------------------

![说明](负载均衡命令.files/image001.png)

集中式设备不支持本命令，请以设备的实际情况为准。

****

**[display** **loadbalance** **hot-backup** **statistics**]命令用来显示负载均衡双机热备的统计信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display** **loadbalance** **hot-backup** **statistics** [ **slot** *slot-number* ]]

分布式设备－IRF模式：

**[display** **loadbalance** **hot-backup** **statistics** **chassis** *chassis-number***slot** *slot-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot**]*slot-number*：显示指定单板上的信息，*slot-number*表示单板所在槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－独立运行模式）

**[slot**]*slot-number*：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示所有成员设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]*slot-number*：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示所有成员设备/PEX上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number* **slot** *slot-number*：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**]*chassis-number* **slot** *slot-number*：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

【举例】

\# 显示负载均衡双机热备的统计信息。

\<Sysname\> display loadbalance hot-backup statistics

Slot 2:

               TryAdd    TryDel    AckDel    AckOK     AckNO     NotSpt

  StiSnd       1         0         0         0         0         0

  StiRcv       0         0         0         0         0         0

  StiSndFail   0         0         0         0         0         0

  StiRcvFail   0         0         0         0         0         0

  MsgSnd       1         0         0         0         0         0

  MsgRcv       0         0         0         0         0         0

  MsgSndFail   0         0         0         0         0         0

  MsgRcvFail   0         0         0         0         0         0

  SesBkTotal : 0

  SesBkFail  : 0

  SesResTotal: 0

  SesResFail : 0

  SesUpdate  : 0

表1-3 display loadbalance hotbackup statistics命令显示信息描述表

字段

描述

TryAdd

持续性表项添加消息

TryDel

持续性表项删除消息

AckDel

持续性表项确认删除消息

AckOK

持续性表项可以删除消息

AckNO

持续性表项不能删除消息

NotSpt

不支持的持续性表项消息

StiSnd

发送条数

StiRcv

接收条数

StiSndFail

发送失败条数

StiRcvFail

接收失败条数

MsgSnd

报文发送次数

MsgRcv

报文接收次数

MsgSndFail

报文发送失败次数

MsgRcvFail

报文发送失败次数

SesBkTotal

会话备份次数

SesBkFail

会话备份失败次数

SesResTotal

会话恢复次数

SesResFail

会话恢复失败次数

SesUpdate

会话更新次数

**负载均衡 \-- 负载均衡配置命令 \-- display loadbalance policy**

------------------------------------------------------------------------

**[display** **loadbalance** **policy**]命令用来显示负载均衡策略的信息。

【命令】

**[display** **loadbalance** **policy** [ **name** *policy-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[name** *policy-name*]：显示指定负载均衡策略的信息。*policy-name*为负载均衡策略的名称，为1～63个字符的字符串，不区分大小写。如果未指定本参数，将显示所有负载均衡策略的信息。

【举例】

\# 显示所有负载均衡策略的信息。

\<Sysname\> display loadbalance policy

LB policy: lbp1

  Description:

  Type: Generic

  Class: lbc1

   Action: lba1

  Default class action: lba0

LB policy: lbp2

  Description:

  Type: HTTP

  Default class action:

表1-4 display loadbalance policy命令显示信息描述表

字段

描述

LB policy

负载均衡策略的名称

Description

负载均衡策略的描述信息

Type

负载均衡策略的类型，包括：

·Generic：表示通用类型

·HTTP：表示HTTP类型

Class

负载均衡策略包含的负载均衡类

Action

负载均衡类对应的负载均衡动作

Default class action

默认的负载均衡动作

**负载均衡 \-- 负载均衡配置命令 \-- display loadbalance snat-pool**

------------------------------------------------------------------------

**[display** **loadbalance** **snat-pool**]命令用来显示SNAT地址池的信息。

【命令】

**[display** **loadbalance** **snat-pool** [ **name** *pool-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[name** *pool-name*]：显示指定SNAT地址池的信息。*pool-name*为SNAT地址池的名称，为1～63个字符的字符串，不区分大小写。如果未指定本参数，将显示所有SNAT地址池的信息。

【举例】

\# 显示所有SNAT地址池的信息。

\<Sysname\> display loadbalance snat-pool

SNAT pool: lbsp1

  Description:

  IPv4 range：

    Start address                       End address

    202.110.10.10                       202.110.10.15

  IPv6 range：

    Start address                       End address

    2002::2                             2002::100

SNAT pool: lbsp2

  Description:

  IPv4 range：

    Start address                       End address

    203.110.10.10                       203.110.10.15

  IPv6 range：

    Start address                       End address

    2003::2                             2003::100

表1-5 display loadbalancesnat-pool命令显示信息描述表

字段

描述

SNAT pool

SNAT地址池的名称

Description

SNAT地址池的描述信息

IPv4 range

IPv4地址段

IPv6 range

IPv6地址段

Start address

起始地址

End address

结束地址

**负载均衡 \-- 负载均衡配置命令 \-- display parameter-profile**

------------------------------------------------------------------------

**[display** **parameter-profile**]命令用来显示参数模板的信息。

【命令】

**[display** **parameter-profile** [ **name** *parameter-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[name** *parameter-name*]：显示指定参数模板的信息。*parameter-name*为参数模板的名称，为1～63个字符的字符串，不区分大小写。如果未指定本参数，将显示所有参数模板的信息。

【举例】

\# 显示所有参数模板的信息。

\<Sysname\> display parameter-profile

Parameter profile: pp1

  Description:

  Type: IP

IP ToS: 20

Parameter profile: pp2

  Description:

  Type: TCP

Exceed MSS: Allow

  TCP window size：65535

Parameter profile: pp3

  Description:

  Type: HTTP

  Rebalance per request: Enabled

  Server connection reuse: Enabled

  Case insensitive: Enabled

Header modify per request: Enabled

Content maximum parse length: 8192

Header maximum parse length: 8192

Secondary cookie delimiters: !@#\$

Secondary cookie start: ?

Header exceed length: Drop

表1-6 display parameter-profile命令显示信息描述表

字段

描述

Parameter profile

参数模板的名称

Description

参数模板的描述信息

Type

参数模板的类型，包括：

·IP：表示IP类型

·HTTP：表示HTTP类型

·TCP：表示TCP类型

IP ToS

发往服务器的IP报文中的ToS字段

Exceed MSS

对客户端发来的HTTP请求报文中超出MSS的数据段的处理方式，包括：

·Allow：表示允许超出MSS的数据段

·Drop：表示丢弃超出MSS的数据段

Rebalance per request

是否开启对每个HTTP请求报文都进行负载均衡的功能，包括：

·Disabled：关闭

·Enabled：开启

Server connection reuse

是否开启允许负载均衡设备与服务器的连接复用的功能，包括：

·Disabled：关闭

·Enabled：开启

Header modify per request

是否开启对每个HTTP请求或应答报文的首部都执行插入、删除或修改操作的功能，包括：

·Disabled：关闭

·Enabled：开启

Case insensitive

是否开启匹配字符串时对大小写不敏感的功能，包括：

·Disabled：关闭

·Enabled：开启

Content maximum parse length

HTTP实体的最大解析长度

Header maximum parse length

HTTP首部的最大解析长度

Secondary cookie delimiters

URL中分隔Secondary Cookie的字符

Secondary cookie start

URL中Secondary Cookie的起始位置标示字符

Header exceed length

当HTTP请求或应答报文首部超出最大长度时的处理方式，包括：

·Continue：表示继续执行负载均衡操作

·Drop：表示停止执行负载均衡操作，丢弃该报文并关闭连接

TCP window size

TCP连接中的本地最大窗口值

**负载均衡 \-- 负载均衡配置命令 \-- display real-server**

------------------------------------------------------------------------

**[display** **real-server**]命令用来显示实服务器的信息。

【命令】

**[display**[ **real-server** [ **brief** \| **name** *real-server-name* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[brief**]：显示实服务器的简要信息。如果未指定本参数，将显示实服务器的详细信息。

**[name** *real-server-name*]：显示指定实服务器的信息。*real-server-name*为实服务器的名称，为1～63个字符的字符串，不区分大小写。如果未指定本参数，将显示所有实服务器的信息。

【举例】

\# 显示所有实服务器的简要信息。

\<Sysname\> display real-server brief

Real server      Address              Port  State          Server farm

rs1              192.168.1.1          0     Active         sf

rs2              192.168.1.2          0     Active         sf

rs3              192.168.1.3          0     Active         sf

\# 显示实服务器rs的详细信息。

\<Sysname\> display real-server name rs

Real server: rs

  Description: Real server RS

  State: Active

  IPv4 address: 1.1.1.1

  IPv6 address: 1001::1

  Port: 8080

  Server farm: sf

  Weight: 150

  Priority: 3

  Slow shutdown: Enabled

  Connection limit: 10000

  Rate limit:

    Connections: 10000

    Bandwidth: 10000 Kbytes/s

    Inbound bandwidth: 5000 Kbytes/s

    Outbound bandwidth: 5000 Kbytes/s

  Probe information:

    Probe success criteria: All

    Probe method      State

    t4                Succeeded

表1-7 display real-server命令显示信息描述表

字段

描述

Real server

实服务器的名称

Address

实服务器的IPv4地址

Port

实服务器的端口号

State

实服务器的状态，包括：

·Active：可用

·Inactive：不可用（由于配置不完全、未被引用或虚服务器尚未开启）

·Probe-failed：健康检测失败

·Ramp：温暖上线的爬升阶段

·Shutdown：关闭

·Standby：温暖上线的准备阶段

Server farm

实服务器所属的实服务组

Description

实服务器的描述信息

IPv4 address

实服务器的IPv4地址

IPv6 address

实服务器的IPv6地址

Weight

实服务器的权值

Priority

实服务器的调用优先级

Slow shutdown

实服务器慢宕功能的状态，包括：

·Disabled：关闭

·Enabled：开启

Connection limit

实服务器所允许的最大连接数

Rate limit

实服务器的速率限制

Connections

实服务器所允许的每秒最大连接数

Bandwidth

实服务器所允许的最大总带宽，单位为千字节/秒

Inbound bandwidth

实服务器所允许的最大入带宽，单位为千字节/秒

Outbound bandwidth

实服务器所允许的最大出带宽，单位为千字节/秒

Probe success criteria

实服务器健康检测的成功条件：

·All：只有全部方法都通过检测才认为健康检测成功

·At least 3：健康检测成功所需通过检测的最少方法数为3

Probe method

健康检测方法所使用的NQA模板名称

State

健康检测方法的状态，包括：

·Failed：健康检测失败

·In progress：正在进行健康检测

·Invalid：健康检测不可用（因其所使用的NQA模板配置不完全），或者实服务器不可用

·Succeeded：健康检测成功

**负载均衡 \-- 负载均衡配置命令 \-- display real-server statistics**

------------------------------------------------------------------------

**[display** **real-server** **statistic**]命令用来显示实服务器的统计信息。

【命令】

集中式设备：

**[display** **real-server** **statistics** [ **name** *real-server-name* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display** **real-server** **statistics** [ **name** *real-server-name*   **slot** *slot-number* ]]

分布式设备－IRF模式：

**[display** **real-server** **statistics** [ **name** *real-server-name*  ]**chassis** *chassis-number***slot** *slot-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[name** *real-server-name*]：显示指定实服务器的统计信息。*real-server-name*为实服务器的名称，为1～63个字符的字符串，不区分大小写。如果未指定本参数，将显示所有实服务器的统计信息。

**[slot**]*slot-number*：显示指定单板上的信息，*slot-number*表示单板所在槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－独立运行模式）

**[slot**]*slot-number*：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示所有成员设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]*slot-number*：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示所有成员设备/PEX上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number* **slot** *slot-number*：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**]*chassis-number* **slot** *slot-number*：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

【举例】

\# 显示实服务器rs的统计信息。

\<Sysname\> display real-server statistics name rs

Real server: rs

  Total connections: 1798

  Active connections: 788

  Max connections: 803

  Connections per second: 157

  Max connections per second: 163

  Server input: 333332 bytes

  Server output: 472054 bytes

  Throughput: 4396 bytes/s

  Inbound throughput: 1214 bytes/s

  Outbound throughput: 3128 bytes/s

  Max throughput: 4564 bytes/s

  Max inbound throughput: 1214 bytes/s

  Max outbound throughput: 3320 bytes/s

  Received packets: 1798

  Sent packets: 0

  Dropped packets: 0

  Received requests: 0

  Dropped requests: 0

  Sent responses: 0

  Dropped responses: 0

表1-8 display real-server statistics命令显示信息描述表

字段

描述

Real server

实服务器的名称

Total connections

总连接数

Active connections

当前活动的连接数

Max connections

最大连接数

Connections per second

每秒连接数

Max connections per second

最大每秒连接数

Server input

从服务器收到的流量，单位为字节

Server output

向服务器发出的流量，单位为字节

Throughput

报文的总吞吐量，单位为字节/秒

Inbound throughput

报文的入吞吐量，单位为字节/秒

Outbound throughput

报文的出吞吐量，单位为字节/秒

Max throughput

报文的最大总吞吐量，单位为字节/秒

Max inbound throughput

报文的最大入吞吐量，单位为字节/秒

Max outbound throughput

报文的最大出吞吐量，单位为字节/秒

Received packets

收到的报文数

Sentpackets

发出的报文数

Dropped packets

丢弃的报文数

Received requests

接收的HTTP请求报文数量，只有七层实服务器才会显示本字段

Dropped requests

丢弃的HTTP请求报文数量，只有七层实服务器才会显示本字段

Sent responses

发出的HTTP应答报文数量，只有七层实服务器才会显示本字段

Dropped responses

丢弃的HTTP应答报文数量，只有七层实服务器才会显示本字段

【相关命令】

·**reset** **real-server** **statistics**

**负载均衡 \-- 负载均衡配置命令 \-- display server-farm**

------------------------------------------------------------------------

**[display** **server-farm**]命令用来显示实服务组的信息。

【命令】

**[display**[ **server-farm** [ **brief** \| **name** *server-farm-name* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[brief**]：显示实服务组的简要信息。如果未指定本参数，将显示实服务组的详细信息。

**[name***server-farm-name*]：显示指定实服务组的信息。*server-farm-name*为实服务组的名称，为1～63个字符的字符串，不区分大小写。如果未指定本参数，将显示所有实服务组的信息。

【举例】

\# 显示所有实服务组的简要信息。

\<Sysname\> display server-farm brief

Predictor: RR - round robin, RD - random, LC - least connection,

           HASH(SIP) - hash address source IP,

           HASH(DIP) - hash address destination IP,

           HASH(SIP-PORT) - hash address source IP-port

NAT/SNAT: Y - enabled, N - disabled

Server farm       Predictor       NAT  SNAT  Total  Active

sf                RR              Y    N     3      3

\# 显示所有实服务组的详细信息。

\<Sysname\> display server-farm

Server farm: sf1

  Description:

  Predictor: Hash address

  NAT: Enbaled

  SNAT pool:

  Failed action: Keep

  Active threshold: Enabled

    Lower: 80

    Upper: 90

  Slow-online: Enabled

  Standby time: 5s

  Ramp-up time: 10s

  Selected server: Enbaled

    Min server: 100

    Max server: 600

  Total real server: 2

  Active real server: 1

  Real server list:

  Name             State         Address              Port  Weight Priority

  rs1              Inactive      1.2.3.4              0     4      100

Server farm: sf2

  Description:

  Predictor: Hash address

  NAT: Enbaled

  SNAT pool:

  Failed action: Keep

  Active threshold: Enabled

    Lower: 80

    Upper: 90

  Slow-online: Enabled

  Standby time: 5s

  Ramp-up time: 10s

  Selected server: Enbaled

    Min server: 100

    Max server: 600

  Total real server: 2

  Active real server: 1

  Real server list:

  Name             State         Address              Port  Weight Priority

  rs2              Inactive      1.2.3.4              0     4      100

                                 1111:2222:3333:4444:

                                 5555:6666:7777:888

  rs3              Inactive      1111:2222:3333:4444: 0     4      100

                                 5555:6666:7777:888

  rs4              Inactive      \--                   0     4      100

表1-9 display server-farm命令显示信息描述表

字段

描述

Server farm

实服务组的名称

Predictor

实服务组的调度算法，包括：

·RR：加权轮转算法

·RD：随机算法

·LC：加权最小连接算法

·HASH(SIP)：根据源IP地址进行的哈希算法

·HASH(DIP)：根据源IP地址和端口号进行的哈希算法

·HASH(SIP-PORT)：根据目的IP地址进行的哈希算法

NAT

实服务组中NAT功能的状态，Y表示开启，N表示关闭

SNAT

实服务组中SNAT功能的状态，Y表示开启，N表示关闭

Total

包含的实服务器数量

Active

活跃的实服务器数量

Description

实服务组的描述信息

Predictor

实服务组的调度算法，包括：

·Round robin：加权轮转算法

·Random：随机算法

·Least connection：加权最小连接算法

·Hash address source IP：根据源IP地址进行的哈希算法

·Hash address source IP-port：根据源IP地址和端口号进行的哈希算法

·Hash address destination IP：根据目的IP地址进行的哈希算法

NAT

实服务组中NAT功能的状态，包括：

·Disabled：关闭

·Enabled：开启

SNAT pool

实服务组引用的SNAT地址池名称

Failed action

实服务组的故障处理方式，包括：

·Keep：保持已有连接

·Reschedule：重定向连接

·Reset：断开已有连接

Active threshold

实服务组可用条件的状态，包括Disabled（关闭）和Enabled（开启）两种。在开启状态下还会显示：

·Lower：最小可用百分比

·Upper：最大可用百分比

Slow-online

实服务组中实服务器温暖上线功能的状态，包括Disabled（关闭）和Enabled（开启）两种。在开启状态下还会显示：

·Standby time：准备时间

·Ramp-up time：爬升时间

Selected server

实服务组中可被调度算法调用的实服务器数量限制功能的状态，包括Disabled（关闭）和Enabled（开启）两种。在开启状态下还会显示：

·Min server：可被调度算法调用的实服务器最小数量

·Max server：可被调度算法调用的实服务器最大数量

Total real server

包含的实服务器数量

Active real server

活跃的实服务器数量

Real server list

实服务器列表

Name

实服务器的名称

State

实服务器的状态，包括：

·Active：可用

·Inactive：不可用（由于配置不完全、未被引用或虚服务器尚未开启）

·Probe-failed：健康检测失败

·Ramp：温暖上线的爬升阶段

·Shutdown：关闭

·Standby：温暖上线的准备阶段

Address

实服务器的IPv4和IPv6地址

Port

实服务器的端口号

Weight

实服务器的权值

Priority

实服务器的调用优先级

**负载均衡 \-- 负载均衡配置命令 \-- display sticky**

------------------------------------------------------------------------

**[display** **sticky**]命令用来显示持续性表项的信息。

【命令】

集中式设备：

**[display**[ **sticky** [ **virtual-server** *virtual-server-name* [ **class** *class-name* \| **default-class** \| **default-server-farm** ] ]]]

分布式设备－独立运行模式/集中式IRF设备：

**[display**[ **sticky** [ **virtual-server** *virtual-server-name* [ **class** *class-name* \| **default-class** \| **default-server-farm** ] ]  **slot** *slot-number* ]]

分布式设备－IRF模式：

**[display**[ **sticky** [ **virtual-server** *virtual-server-name* [ **class** *class-name* \| **default-class** \| **default-server-farm** ] ] ]**chassis** *chassis-number***slot** *slot-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[virtual-server** *virtual-server-name*]：显示指定虚服务器的信息。*virtual-server-name*为虚服务器的名称，为1～63个字符的字符串，不区分大小写。如果未指定本参数，将显示所有虚服务器的信息。

**[class** *class-name*]：显示指定负载均衡类的信息。*class-name*为负载均衡类的名称，为1～63个字符的字符串，不区分大小写。

**[default-class**]：显示默认负载均衡动作的信息。

**[default-server-farm**]：显示默认的实服务组的信息。

**[slot**]*slot-number*：显示指定单板上的信息，*slot-number*表示单板所在槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－独立运行模式）

**[slot**]*slot-number*：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示所有成员设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]*slot-number*：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示所有成员设备/PEX上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number* **slot** *slot-number*：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式IRF设备－IRF模式）（不支持IRF3的设备）

**[chassis**]*chassis-number* **slot** *slot-number*：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式IRF设备－IRF模式）（支持IRF3的设备）

【举例】

\# 显示所有虚服务的持续性表项信息。

\<Sysname\> display sticky

Virtual server name: vs1

  Sticky zone type: Class

  Class name: lbc1

  Sticky group name: sg1

  Sticky method: Source IP and port

  Timeout: 60

Sticky entry                     Real server           Expired time Count

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

192.168.6.206/1566               192.168.6.206/0       53           0

192.168.6.206/1567               192.168.6.206/0       56           0

Virtual server name: vs2

  Sticky zone type: Default class

  Class name:

  Sticky group name: sg2

  Sticky method: HTTP URL

  Timeout: 60

Sticky entry                     Real server           Expired time Count

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

e251273eb74a8ee3f661a7af0915af1  192.168.6.206/0       54           0

                                 2000::100/0

Virtual server name: vs3

  Sticky zone type: Default sever farm

  Class name:

  Sticky group name: sg3

  Sticky method: Both IP and port

  Timeout: 60

Sticky entry                     Real server           Expired time Count

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

192.168.6.206/2606               192.168.6.206/0       57           0

192.168.6.40/80

192.168.6.206/2605               192.168.6.206/0       55           0

192.168.6.40/80

192.168.6.206/2604               192.168.6.206/0       52           0

192.168.6.40/80

表1-10 display sticky命令显示信息描述表

字段

描述

Virtual server name

虚服务器的名称

Sticky zone type

持续性表项的来源，包括：

·Class：由虚服务所引用策略中的类和动作生成

·Default class：由虚服务所引用策略中的默认动作生成

·Default server farm：由虚服务下默认的主用或备用实服务组生成

Class name

如果该持续性由类和动作生成，显示对应负载均衡类的名称；否则显示为空

Sticky group name

生成该持续性表项的持续性组名称

Sticky method

该持续性表项对应的持续性方法，包括：

·Source IP：源IPv4地址持续性方法

·Source IPv6：源IPv6地址持续性方法

·Source IP and port：源IPv4地址＋源端口持续性方法

·Source IPv6 and port：源IPv6地址＋源端口持续性方法

·Destination IP：目的IPv4地址持续性方法

·Destination IPv6：目的IPv6地址持续性方法

·Destination IP and port：目的IPv4地址＋目的端口持续性方法

·Destination IPv6 and port：目的IPv6地址＋目的端口持续性方法

·Both IP：源IPv4地址＋目的IPv4地址持续性方法

·Both IPv6：源IPv6地址＋目的IPv6地址持续性方法

·Both IP and port：源IPv4地址＋源端口＋目的IPv4地址＋目的端口持续性方法

·Both IPv6 and port：源IPv6地址＋源端口＋目的IPv6地址＋目的端口持续性方法

·HTTP URL：基于HTTP URL的持续性方法

·HTTP header name：基于HTTP首部名称的持续性方法

·HTTP version：基于HTTP版本的持续性方法

·HTTP host：基于HTTP主机的持续性方法

·HTTP method：基于HTTP Request-Method的持续性方法

·HTTP content：HTTP实体持续性方法

·HTTP cookie：HTTP Cookie持续性方法

·Payload：HTTP载荷持续性方法

·SSL session ID：SSL持续性方法为基于SSL会话ID

Timeout

持续性表项的超时时间，单位为秒

Sticky entry

持续性表项对应的Key值

Real server

实服务器的IP地址和端口号。对于七层持续性方法，如果实服务器同时配置了IPv4和IPv6地址，则不论该持续性表项由哪种连接生成，都会同时显示这两个地址

Expired time

持续性表项的老化剩余时间，如果引用计数不为0，则显示为配置值

Count

持续性表项的引用计数

**负载均衡 \-- 负载均衡配置命令 \-- display sticky-group**

------------------------------------------------------------------------

**[display** **sticky-group**]命令用来显示持续性组的信息。

【命令】

**[display** **sticky-group** [ **name** *group-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[name** *group-name*]：显示指定持续性组的信息。*group-name*为持续性组的名称，为1～63个字符的字符串，不区分大小写。如果未指定本参数，将显示所有持续性组的信息。

【举例】

\# 显示所有持续性组的信息。

\<Sysname\> display sticky-group

Sticky group: sg1

  Description:

  Timeout: 60

  Sticky group type: Address-port

    Method: Both IP and port

      Mask: 32

Sticky group: sg2

  Description:

  Timeout: 60

  Sticky group type: HTTP header

    Method: HTTP header name

      Name: accept-encoding

      Offset: 4

      Start: gzip

      Length: 10

表1-11 display sticky-group命令显示信息描述表

字段

描述

Sticky group

持续性组的名称

Description

持续性组的描述信息

Timeout

持续性表项的超时时间，单位为秒

Sticky group type

持续性组的类型，包括：

·Address-port：表示地址端口类型

·HTTP content：表示HTTP实体类型

·HTTP cookie：表示HTTP Cookie类型

·HTTP header：表示HTTP首部类型

·Payload：表示HTTP载荷类型

·SSL：表示SSL类型

各类型持续性组的具体内容，请参见 表1-12(?-1867804460#_Ref393378952)

表1-12 各类型持续性组的具体内容

持续性组类型

字段

描述

Address-port

Method

持续性方法，包括：

·Source IP：源IPv4地址持续性方法

·Source IPv6：源IPv6地址持续性方法

·Source IP and port：源IPv4地址＋源端口持续性方法

·Source IPv6 and port：源IPv6地址＋源端口持续性方法

·Destination IP：目的IPv4地址持续性方法

·Destination IPv6：目的IPv6地址持续性方法

·Destination IP and port：目的IPv4地址＋目的端口持续性方法

·Destination IPv6 and port：目的IPv6地址＋目的端口持续性方法

·Both IP：源IPv4地址＋目的IPv4地址持续性方法

·Both IPv6：源IPv6地址＋目的IPv6地址持续性方法

·Both IP and port：源IPv4地址＋源端口＋目的IPv4地址＋目的端口持续性方法

·Both IPv6 and port：源IPv6地址＋源端口＋目的IPv6地址＋目的端口持续性方法

Mask

持续性方法的掩码长度，只有IPv4持续性方法才会显示本字段

Prefix

持续性方法的前缀长度，只有IPv6持续性方法才会显示本字段

HTTP content

Offset

实体基于HTTP报文起始位置的偏移量

Start

实体开始标记的正则表达式

End

实体结束标记的正则表达式，不会与Length字段同时显示

Length

实体的长度，不会与End字段同时显示

HTTP cookie

Method

持续性方法，包括：

·HTTP cookie insert：Cookie截取持续性方法

·HTTP cookie rewrite：Cookie重写持续性方法

·HTTP cookie get：Cookie插入持续性方法

只有指定了HTTP Cookie持续性方法才会显示本字段

Name

HTTP cookie的名称。只有指定了HTTP Cookie持续性方法才会显示本字段

Offset

Cookie基于HTTP报文起始位置的偏移量。只有指定了Cookie插入持续性方法才会显示本字段

Start

Cookie开始标记的正则表达式。只有指定了Cookie插入持续性方法才会显示本字段

End

Cookie结束标记的正则表达式，不会与Length字段同时显示。只有指定了Cookie插入持续性方法才会显示本字段

Length

Cookie的长度，不会与End字段同时显示。只有指定了Cookie插入持续性方法才会显示本字段

Cookie secondary name

需在URI中查找的Secondary Cookie名称。只有指定了Cookie插入持续性方法才会显示本字段

Check all packets

是否开启检查所有报文的功能，包括：

·Disabled：关闭

·Enabled：开启

HTTP header

Method

持续性方法，包括：

·HTTP host：基于HTTP主机的持续性方法

·HTTP header name：基于HTTP首部名称的持续性方法

·HTTP method：基于HTTP Request-Method的持续性方法

·HTTP URL：基于HTTP URL的持续性方法

·HTTP version：基于HTTP版本的持续性方法

只有指定了HTTP首部持续性方法才会显示本字段

Name

HTTP首部的名称。只有指定了基于HTTP首部名称的持续性方法才会显示本字段

Offset

HTTP首部基于HTTP报文起始位置的偏移量。只有指定了基于HTTP主机或HTTP URL的持续性方法才会显示本字段

Start

HTTP首部开始标记的正则表达式。只有指定了基于HTTP主机或HTTP URL的持续性方法才会显示本字段

End

HTTP首部结束标记的正则表达式，不会与Length字段同时显示。只有指定了基于HTTP主机或HTTP URL的持续性方法才会显示本字段

Length

HTTP首部的长度，不会与End字段同时显示。只有指定了基于HTTP主机或HTTP URL的持续性方法才会显示本字段

Payload

Offset

HTTP载荷基于HTTP报文起始位置的偏移量

Start

HTTP载荷开始标记的正则表达式

End

HTTP载荷结束标记的正则表达式，不会与Length字段同时显示

Length

HTTP载荷的长度，不会与End字段同时显示

SSL

Method

持续性方法，包括：

·SSL session ID：基于SSL session ID的SSL持续性方法

只有指定了基于SSL会话ID的SSL持续性方法才会显示本字段

**负载均衡 \-- 负载均衡配置命令 \-- display virtual-server**

------------------------------------------------------------------------

**[display** **virtual-server**]命令用来显示虚服务器的信息。

【命令】

**[display**[ **virtual-server** [ **brief** \| **name** *virtual-server-name* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[brief**]：显示虚服务器的简要信息。如果未指定本参数，将显示虚服务器的详细信息。

**[name** *virtual-server-name*]：显示指定虚服务器的信息。*virtual-server-name*为虚服务器的名称，为1～63个字符的字符串，不区分大小写。如果未指定本参数，将显示所有虚服务器的信息。

【举例】

\# 显示所有虚服务器的简要信息。

\<Sysname\> display virtual-server brief

Virtual server   State    Type      VPN instance     Virtual address     Port

vs1              Inactive IP        vpn1             192.168.21.148/32   80

                                                     1111:2222:3333:4444

                                                     :5555:6666:7777:888

                                                     8/128

vs2              Active   HTTP                       61.159.4.100/32     8080

\# 显示虚服务器vs的详细信息。

\<Sysname\> display virtual-server name vs

Virtual server: vs

  Description: Virtual server VS

  Type: HTTP

  State: Active

  VPN instance: vpn1

  Virtual IPv4 address: 1.1.1.1/32

  Virtual IPv6 address: 1001::1/128

  Port: 8080

  Default server farm: sf (in use)

  Backup server farm: sfb

  Sticky: sg3

  LB policy: lbp2

  HTTP parameter profile: pp1

  UDP per-packet: Enabled

  Connection limit: 10000

  Rate limit:

    Connections: 10000

    Bandwidth: 10000 Kbytes/s

    Inbound bandwidth: 5000 Kbytes/s

    Outbound bandwidth: 5000 Kbytes/s

  SSL server policy: ssl-server

  SSL client policy: ssl-client

  Redirect relocation:

  Redirect return-code: 302

  Sticky synchronization: Disabled

表1-13 display virtual-server命令显示信息描述表

字段

描述

Virtual server

虚服务器的名称

State

虚服务器的状态，包括：

·Active：可用

·Inactive：不可用（由于配置不完全或虚服务器尚未开启）

Type

虚服务器的类型，包括Fast HTTP、HTTP、IP、TCP和UDP

VPN instance

虚服务器所属的VPN实例名称

Virtual address

虚服务器的IPv4地址和掩码

Port

虚服务器的端口号

Description

虚服务器的描述信息

Virtual IPv4 address

虚服务器的IPv4地址和掩码

Virtual IPv6 address

虚服务器的IPv6地址和前缀

Default server farm

默认的主用实服务组名称，(in use)表示该实服务组正被使用

Backup server farm

默认的备用实服务组名称，(in use)表示该实服务组正被使用

Sticky

默认的持续性组名称

LB policy

虚服务器引用的负载均衡策略

HTTP parameter profile

虚服务器引用的HTTP类型参数模板，只有配置了HTTP类型的参数模板才会显示本字段

IP parameter profile

虚服务器引用的IP类型参数模板，只有配置了IP类型的参数模板才会显示本字段

TCP parameter profile

虚服务器引用的TCP类型参数模板，只有配置了TCP类型的参数模板才会显示本字段

UDP per-packet

虚服务器UDP强制负载均衡功能的状态，包括：

·Disabled：关闭

·Enabled：开启

只有UDP类型的虚服务器才会显示本字段

Connection limit

虚服务器所允许的最大连接数

Rate limit

虚服务器的速率限制

Connections

虚服务器所允许的每秒最大连接数

Bandwidth

虚服务器所允许的最大总带宽，单位为千字节/秒

Inbound bandwidth

虚服务器所允许的最大入带宽，单位为千字节/秒

Outbound bandwidth

虚服务器所允许的最大出带宽，单位为千字节/秒

SSL server policy

SSL服务器端策略的名称，只有HTTP类型的虚服务器才会显示本字段

SSL client policy

SSL客户端策略的名称，只有HTTP类型的虚服务器才会显示本字段

Redirect relocation

重定向的URL，只有HTTP类型的虚服务器才会显示本字段

Redirect return-code

重定向报文中的状态码，只有HTTP类型的虚服务器才会显示本字段

Connection synchronization

虚服务器会话扩展信息备份功能的状态，包括：

·Disabled：关闭

·Enabled：开启

HTTP类型的虚服务器不会显示本字段

集中式设备不支持本字段，请以设备的实际情况为准

Sticky synchronization

虚服务器持续性表项备份功能的状态，包括：

·Disabled：关闭

·Enabled：开启

集中式设备不支持本字段，请以设备的实际情况为准

**负载均衡 \-- 负载均衡配置命令 \-- display virtual-server statistics**

------------------------------------------------------------------------

**[display** **virtual-server** **statistics**]命令用来显示虚服务器的统计信息。

【命令】

集中式设备：

**[display** **virtual-server** **statistics** [ **name** *virtual-server-name* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display** **virtual-server** **statistics** [ **name** *virtual-server-name*   **slot** *slot-number* ]]

分布式设备－IRF模式：

**[display** **virtual-server** **statistics** [ **name** *virtual-server-name* ] **chassis** *chassis-number***slot** *slot-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[name** *virtual-server-name*]：显示指定虚服务器的统计信息。*virtual-server-name*为虚服务器的名称，为1～63个字符的字符串，不区分大小写。如果未指定本参数，将显示所有虚服务器的统计信息。

**[slot**]*slot-number*：显示指定单板上的信息，*slot-number*表示单板所在槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－独立运行模式）

**[slot**]*slot-number*：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示所有成员设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]*slot-number*：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示所有成员设备/PEX上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number* **slot** *slot-number*：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**]*chassis-number* **slot** *slot-number*：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

【举例】

\# 显示虚服务器vs的统计信息。

\<Sysname\> display virtual-server statistics name vs

Virtual server: vs

  Total connections: 979

  Active connections: 618

  Max connections: 661

  Connections per second: 146

  Max connections per second: 156

Client input: 333332 bytes

Client output: 472054 bytes

  Throughput: 4088 bytes/s

  Inbound throughput: 1214 bytes/s

  Outbound throughput: 2874 bytes/s

  Max throughput: 4368 bytes/s

  Max inbound throughput: 1214 bytes/s

  Max outbound throughput: 3154 bytes/s

  Received packets: 979

  Sent packets: 0

  Dropped packets: 0

  Received requests: 0

  Dropped requests: 0

  Sent responses: 0

  Dropped responses: 0

表1-14 display virtual-server staistics命令显示信息描述表

字段

描述

Virtual server

虚服务器的名称

Total connections

总连接数

Active connections

当前活动的连接数

Max connections

最大连接数

Connections per second

每秒连接数

Max connections per second

最大每秒连接数

Client input

从客户端收到的流量，单位为字节

Client output

向客户端发出的流量，单位为字节

Throughput

报文的总吞吐量，单位为字节/秒

Inbound throughput

报文的入吞吐量，单位为字节/秒

Outbound throughput

报文的出吞吐量，单位为字节/秒

Max throughput

报文的最大总吞吐量，单位为字节/秒

Max inbound throughput

报文的最大入吞吐量，单位为字节/秒

Max oubound throughput

报文的最大出吞吐量，单位为字节/秒

Received packets

收到的报文数

Sentpackets

发出的报文数（虚服务器发给客户端的）

Dropped packets

丢弃的报文数

Received requests

收到的HTTP请求报文数量，只有HTTP类型的虚服务器才会显示本字段

Dropped requests

丢弃的HTTP请求报文数量，只有HTTP类型的虚服务器才会显示本字段

Sent responses

发出的HTTP应答报文数量，只有HTTP类型的虚服务器才会显示本字段

Dropped responses

丢弃的HTTP应答报文数量，只有HTTP类型的虚服务器才会显示本字段

【相关命令】

·**reset****virtual-server** **statistics**

**负载均衡 \-- 负载均衡配置命令 \-- exceed-mss**

------------------------------------------------------------------------

**[exceed-mss**]命令用来配置对客户端发来的HTTP请求报文中超出MSS的数据段的处理方式。

**[undo****exceed-mss**]命令用来恢复缺省情况。

【命令】

**[exceed-mss**[ { **allow** \| **drop** }]]

**[undo****exceed-mss**]

【缺省情况】

对客户端发来的HTTP请求报文中超出MSS的数据段的处理方式为允许超出MSS的数据段。

【视图】

参数模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[allow**]：允许超出MSS的数据段。

**[drop**]：丢弃超出MSS的数据段。

【使用指导】

本命令只在TCP类型的参数模板视图下支持。

【举例】

\# 在TCP类型的参数模板pp3中，配置对客户端发来的HTTP请求报文中超出MSS的数据段的处理方式为丢弃超出MSS的数据段。

\<Sysname\> system-view

Sysname parameter-profile pp3 type tcp

Sysname-para-tcp-pp3 exceed-mss drop

**负载均衡 \-- 负载均衡配置命令 \-- fail-action**

------------------------------------------------------------------------

**[fail-action**]命令用来配置实服务组的故障处理方式。

**[undo** **fail-action**]命令用来恢复缺省情况。

【命令】

**[fail-action**[ { **keep** \| **reschedule** \| **reset** }]]

**[undo** **fail-action**]

【缺省情况】

实服务组的故障处理方式为保持已有连接。

【视图】

实服务组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[keep**]：保持已有连接，即不主动断开与故障实服务器的连接，连接继续保持还是断开将由协议自身的超时机制决定。

**[reschedule**]：重定向连接，即把连接重定向到实服务组中其它可用的实服务器上。

**[reset**]：断开已有连接，即主动断开与故障实服务器的连接。对于TCP报文，将发送RST报文；对于其它类型的报文，将发送ICMP不可达报文。

【举例】

\# 配置实服务组sf的故障处理方式为重定向连接。

\<Sysname\> system-view

Sysname server-farm sf

Sysname-sfarm-sf fail-action reschedule

**负载均衡 \-- 负载均衡配置命令 \-- forward all**

------------------------------------------------------------------------

**[forward** **all**]命令用来配置报文的转发模式为转发。

**[undo** **forward**]命令用来恢复缺省情况。

【命令】

**[forward** **all**]

**[undo** **forward**]

【缺省情况】

报文的转发模式为丢弃。

【视图】

负载均衡动作视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本命令只在通用类型的负载均衡动作视图下支持。

需要注意的是，本命令与**server-farm**命令互斥，当配置了其中一条后，另一条的配置将被自动取消。

【举例】

\# 在通用类型的负载均衡动作lba1中，配置报文的转发模式为转发。

\<Sysname\> system-view

Sysname loadbalance action lba1 type generic

Sysname-lba-generic-lba1 forward all

【相关命令】

·**server-farm** (LB action view)

**负载均衡 \-- 负载均衡配置命令 \-- header**

------------------------------------------------------------------------

**[header**]命令用来配置HTTP首部持续性方法。

**[undo****header**]命令用来删除HTTP首部持续性方法。

【命令】

**[header**[ { { **host** \| **name** *header-name* \| **url** } [ **offset** *offset* ]  **start** *start-string* [ **end** *end-string* \| **length** *length* ] } \| **request-method** **\|** **version** }]]

**[undo****header**]

【缺省情况】

不存在任何持续性方法。

【视图】

持续性组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[host**]：基于HTTP主机的持续性方法。

**[name**] *header-name*：基于HTTP首部名称的持续性方法，为1～63个字符的字符串。

**[url**]：基于HTTP URL的持续性方法。

**[offset**] *offset*：HTTP首部基于HTTP报文起始位置的偏移量，取值范围为0～1000，缺省值为0。

**[start**] *start-string*：HTTP首部开始标记的正则表达式，即从*offset*起到本标记为开始，为1～127字符的字符串。

**[end**] *end-string*：HTTP首部结束标记的正则表达式，即从*start-string*起到本标记为结束，为1～127字符的字符串。

**[length**] *length*：HTTP首部的长度，取值范围为0～1000，缺省值为0，表示所有长度。

**[request-method**]：基于HTTP Request-Method的持续性方法。

**[version**]：基于HTTP版本的持续性方法。

【使用指导】

本命令只在HTTP首部类型的持续性组视图下支持。

本命令用来根据*offset*、*start-string*、*end-string*及*length*获取生成持续性表项的HTTP首部信息。*start-string*和*end-string*将不计入持续性表项信息中。

【举例】

\# 在HTTP首部类型的持续性组sg4中，配置HTTP首部持续性方法为：基于HTTP主机来生成持续性表项。

\<Sysname\> system-view

Sysname sticky-group sg4 type http-header

Sysname-sticky-http-header-sg4 header host

**负载均衡 \-- 负载均衡配置命令 \-- header delete**

------------------------------------------------------------------------

**[header** **delete**]命令用来删除HTTP首部。

**[undo** **header** **delete**]命令用来取消该配置。

【命令】

**[header**[ **delete** { **both** \| **request** \| **response** } **name** *header-name*]]

**[undo**[ **header** **delete** { **both** \| **request** \| **response** } **name** *header-name*]]

【缺省情况】

不删除HTTP首部。

【视图】

负载均衡动作视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[both**]：请求和应答两个方向的HTTP报文。

**[request**]：请求方向的HTTP报文。

**[response**]：应答方向的HTTP报文。

**[name**] *header-name*：HTTP报文首部的名称，包括标准和自定义的首部，需要与报文中的首部完全匹配。为1～63个字符的字符串，不区分大小写。不包括(、)、\<、\>、@、,、;、:、\、\"、/、、、?、=、[、}、SP（空格符）、HT（水平制表符），以及ASCII码中小于等于31、大于等于127的字符。

【使用指导】]

本命令只在HTTP类型的负载均衡动作视图下支持。

配置了本命令后，如果指定方向的HTTP报文中携带有指定名称的首部，系统会将该首部从报文中删除。

【举例】

\# 在HTTP类型的负载均衡动作lba2中，删除HTTP请求报文中名为host的首部。

\<Sysname\> system-view

Sysname loadbalance action lba2 type http

Sysname-lba-http-lba2 header delete request name host

**负载均衡 \-- 负载均衡配置命令 \-- header exceed-length**

------------------------------------------------------------------------

**[header** **exceed-length**]命令用来配置当HTTP请求或应答报文首部超出最大长度时的处理方式。

**[undo** **header** **exceed-length**]命令用来恢复缺省情况。

【命令】

**[header**[ **exceed-length** { **continue** \| **drop** }]]

**[undo** **header** **exceed-length**]

【缺省情况】

当HTTP请求或应答报文首部超出最大长度时，继续进行负载均衡处理。

【视图】

参数模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[continue**]：继续执行负载均衡操作。

**[drop**]：停止执行负载均衡操作，丢弃该报文并关闭连接。

【使用指导】

本命令只在HTTP类型的参数模板视图下支持。

需要注意的是：

·当HTTP报文首部的长度超过负载均衡的处理能力时，系统将无条件使用**drop**方式处理该报文。

·快速HTTP类型的虚服务器不支持本功能。

【举例】

\# 在HTTP类型的参数模板pp1中，配置当HTTP请求或应答报文首部超出最大长度时的处理方式为：停止执行负载均衡操作，丢弃该报文并关闭连接。

\<Sysname\> system-view

Sysname parameter-profile pp1 type http

Sysname-para-http-pp1 header exceed-length drop

**负载均衡 \-- 负载均衡配置命令 \-- header insert**

------------------------------------------------------------------------

**[header** **insert**]命令用来插入HTTP首部。

**[undo** **header** **insert**]命令用来取消该配置。

【命令】

**[header**[ **insert** { **both** \| **request** \| **response** } **name** *header-name* **value** *value*]]

**[undo**[ **header** **insert** { **both** \| **request** \| **response** } **name** *header-name*]]

【缺省情况】

不插入HTTP首部。

【视图】

负载均衡动作视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[both**]：请求和应答两个方向的HTTP报文。

**[request**]：请求方向的HTTP报文。

**[response**]：应答方向的HTTP报文。

**[name**] *header-name*：要插入HTTP报文中的首部名称，包括标准和自定义的首部。为1～63个字符的字符串，不区分大小写。不包括(、)、\<、\>、@、,、;、:、\、\"、/、、、?、=、[、}、SP（空格符）、HT（水平制表符），以及ASCII码中小于等于31、大于等于127的字符。

**[value**] *value*：要插入HTTP报文中的首部内容，为1～255个字符的字符串，也可以使用以下特定含义的字符串：

·]%is：源IP地址或源IPv6地址。

·%ps：源端口号。

·%id：目的IP地址或目的IPv6地址。

·%pd：目的端口号。

【使用指导】

本命令只在HTTP类型的负载均衡动作视图下支持。

配置了本命令后，系统将在指定方向的HTTP报文中插入指定名称和内容的首部。

【举例】

\# 在HTTP类型的负载均衡动作lba2中，将名为source、内容为源IP和源端口号的首部插入到HTTP请求报文中。

\<Sysname\> system-view

Sysname loadbalance action lba2 type http

Sysname-lba-http-lba2 header insert request name source value %is:%ps

**负载均衡 \-- 负载均衡配置命令 \-- header maxparse-length**

------------------------------------------------------------------------

**[header** **maxparse-length**]命令用来配置HTTP首部的最大解析长度。

**[undo****header** **maxparse-length**]命令用来恢复缺省情况。

【命令】

**[header** **maxparse-length** *length*]

**[undo****header** **maxparse-length**]

【缺省情况】

HTTP首部的最大解析长度为4096。

【视图】

参数模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[length*]：HTTP首部的最大解析长度，取值范围为1～65535。

【使用指导】

本命令只在HTTP类型的参数模板视图下支持。

需要注意的是，快速HTTP类型的虚服务器不支持本功能。

【举例】

\# 在HTTP类型的参数模板pp1中，配置HTTP首部的最大解析长度为8192。

\<Sysname\> system-view

Sysname parameter-profile pp1 type http

Sysname-para-http-pp1 header maxparse-length 8192

**负载均衡 \-- 负载均衡配置命令 \-- header modify per-request**

------------------------------------------------------------------------

**[header** **modify** **per-request**]命令用来配置对每个HTTP请求或应答报文的首部都执行插入、删除或修改操作。

**[undo****header** **modify** **per-request**]命令用来恢复缺省情况。

【命令】

**[header** **modify** **per-request**]

**[undo****header** **modify** **per-request**]

【缺省情况】

只对每个连接的第一个HTTP请求或应答报文的首部执行插入、删除或修改操作。

【视图】

参数模板视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本命令只在HTTP类型的参数模板视图下支持。

【举例】

\# 在HTTP类型的参数模板pp1中，配置对每个HTTP请求或应答报文的首部都执行插入、删除或修改操作。

\<Sysname\> system-view

Sysname parameter-profile pp1 type http

Sysname-para-http-pp1 header modify per-request

**负载均衡 \-- 负载均衡配置命令 \-- header rewrite**

------------------------------------------------------------------------

**[header** **rewrite**]命令用来重写HTTP首部。

**[undo** **header** **rewrite**]命令用来取消该配置。

【命令】

**[header**[ **rewrite** { **both** \| **request** \| **response** } **name** *header-name* **value** *value* **replace** *replace*]]

**[undo**[ **header** **rewrite** { **both** \| **request** \| **response** } **name** *header-name*]]

【缺省情况】

不重写HTTP首部。

【视图】

负载均衡动作视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[both**]：请求和应答两个方向的HTTP报文。

**[request**]：请求方向的HTTP报文。

**[response**]：应答方向的HTTP报文。

**[name**] *header-name*：HTTP报文首部的名称，包括标准和自定义的首部，需要与报文中的首部完全匹配。为1～63个字符的字符串，不区分大小写。不包括(、)、\<、\>、@、,、;、:、\、\"、/、、、?、=、[、}、SP（空格符）、HT（水平制表符），以及ASCII码中小于等于31、大于等于127的字符。

**[value** *value*]：要被重写的HTTP报文首部的内容，为1～127个字符的字符串。

**[replace** *replace*]：重写后的内容，为1～127个字符的字符串。

【使用指导】]

本命令只在HTTP类型的负载均衡动作视图下支持。

配置了本命令后，如果指定方向的HTTP报文中携带有指定名称的首部，系统会将该首部中的内容*value*重写为*replace*。

【举例】

\# 在HTTP类型的负载均衡动作lba2中，将HTTP请求报文名中为host的首部中的内容，由www\\.(h3c)\\.com重写为www.%1.com.cn。

\<Sysname\> system-view

Sysname loadbalance action lba2 type http

Sysname-lba-http-lba2 header rewrite request name host value www\\.(h3c)\\.com replace www.%1.com.cn

**负载均衡 \-- 负载均衡配置命令 \-- ip**

------------------------------------------------------------------------

**[ip**]命令用来配置IPv4持续性方法。

**[undo** **ip**]命令用来删除IPv4持续性方法。

【命令】

**[ip** [ **port**  { **both** \| **destination** \| **source** }  **mask** *mask-length* ]]

**[undo** **ip**]

【缺省情况】

不存在任何持续性方法。

【视图】

持续性组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[port**]：表示持续性方法为IPv4地址＋端口。如果未指定本参数，表示持续性方法为IPv4地址。

**[both**]：当未指定**port**参数时，表示持续性方法为源IPv4地址＋目的IPv4地址；当指定了**port**参数时，表示持续性方法为源IPv4地址＋源端口＋目的IPv4地址＋目的端口。

**[destination**]：当未指定**port**参数时，表示持续性方法为目的IPv4地址；当指定了**port**参数时，表示持续性方法为目的IPv4地址＋目的端口。

**[source**]：当未指定**port**参数时，表示持续性方法为源IPv4地址；当指定了**port**参数时，表示持续性方法为源IPv4地址＋源端口。

**[mask** *mask-length*]：持续性方法的掩码长度，仅对IPv4地址有效。

【举例】

\# 在地址端口类型的持续性组sg1中，配置持续性方法为源IPv4地址。

\<Sysname\> system-view

Sysname sticky-group sg1 type address-port

Sysname-sticky-address-port-sg1 ip source

\# 在地址端口类型的持续性组sg1中，配置持续性方法为源IPv4地址＋源端口。

\<Sysname\> system-view

Sysname sticky-group sg1 type address-port

Sysname-sticky-address-port-sg1 ip port source

【相关命令】

·**sticky-group**

**负载均衡 \-- 负载均衡配置命令 \-- ip address**

------------------------------------------------------------------------

**[ip** **address**]命令用来配置实服务器的IPv4地址。

**[undo** **ip** **address**]命令用来删除实服务器的IPv4地址。

【命令】

**[ip** **address** *ipv4-address*]

**[undo** **ip** **address**]

【缺省情况】

实服务器没有IPv4地址。

【视图】

实服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv4-address*]：IPv4地址，不能为环回地址、组播地址、广播地址和0.X.X.X。

【举例】

\# 配置实服务器rs的IPv4地址为1.1.1.1。

\<Sysname\> system-view

Sysname real-server rs

Sysname-rserver-rs ip address 1.1.1.1

**负载均衡 \-- 负载均衡配置命令 \-- ip range**

------------------------------------------------------------------------

**[ip** **range**]命令用来配置SNAT地址池的IPv4地址范围。

**[undo** **ip** **range**]命令用来恢复缺省情况。

【命令】

**[ip** **range** **start** *start-ipv4-address* **end** *end-ipv4-address*]

**[undo** **ip** **range**]

【缺省情况】

没有配置SNAT地址池的IPv4地址范围。

【视图】

SNAT地址池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[start** *start-ipv4-address*]：起始IPv4地址。

**[end** *end-ipv4-address*]：结束IPv4地址，必须大于等于起始IPv4地址。

【使用指导】

需要注意的是，一个SNAT地址池中最多允许有256个IPv4地址，且不同SNAT地址池中的IPv4地址不允许重叠。

【举例】

\# 配置SNAT地址池lbsp的IPv4地址范围为1.1.1.1～1.1.1.100。

\<Sysname\> system-view

Sysname loadbalance snat-pool lbsp

Sysname-lbsnat-pool-lbsp ip range start 1.1.1.1 end 1.1.1.100

**负载均衡 \-- 负载均衡配置命令 \-- ipv6**

------------------------------------------------------------------------

**[ipv6**]命令用来配置IPv6持续性方法。

**[undo** **ipv6**]命令用来删除IPv6持续性方法。

【命令】

**[ipv6** [ **port**  { **both** \| **destination** \| **source** }  **prefix** *prefix-length* ]]

**[undo** **ipv6**]

【缺省情况】

不存在任何持续性方法。

【视图】

持续性组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[port**]：表示持续性方法为IPv6地址＋端口。如果未指定本参数，表示持续性方法为IPv6地址。

**[both**]：表示持续性方法为源IPv6地址＋目的IPv6地址（未指定**port**参数时），或源IPv6地址＋源端口＋目的IPv6地址＋目的端口（指定**port**参数时）。

**[destination**]：表示持续性方法为目的IPv6地址（未指定**port**参数时），或目的IPv6地址＋目的端口（指定**port**参数时）。

**[source**]：表示持续性方法为源IPv6地址（未指定**port**参数时），或源IPv6地址＋源端口（指定**port**参数时）。

**[prefix** *prefix-length*]：持续性方法的前缀长度，仅对IPv6地址有效。

【举例】

\# 在地址端口类型的持续性组sg1中，配置持续性方法为源IPv6地址。

\<Sysname\> system-view

Sysname sticky-group sg1 type address-port

Sysname-sticky-address-port-sg1 ipv6 source

\# 在地址端口类型的持续性组sg1中，配置持续性方法为源IPv6地址＋源端口。

\<Sysname\> system-view

Sysname sticky-group sg1 type address-port

Sysname-sticky-address-port-sg1 ipv6 port source

【相关命令】

·**sticky-group**

**负载均衡 \-- 负载均衡配置命令 \-- ipv6 address**

------------------------------------------------------------------------

**[ipv6** **address**]命令用来配置实服务器的IPv6地址。

**[undo** **ipv6** **address**]命令用来删除实服务器的IPv6地址。

【命令】

**[ipv6** **address** *ipv6-address*]

**[undo** **ipv6** **address**]

【缺省情况】

实服务器没有IPv6地址。

【视图】

实服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：IPv6地址，不能为环回地址、IPv6组播地址、链路本地地址和全0地址。

【举例】

\# 配置实服务器rs的IPv6地址为1001::1。

\<Sysname\> system-view

Sysname real-server rs

Sysname-rserver-rs ipv6 address 1001::1

**负载均衡 \-- 负载均衡配置命令 \-- ipv6 range**

------------------------------------------------------------------------

**[ip** **range**]命令用来配置SNAT地址池的IPv6地址范围。

**[undo** **ip** **range**]命令用来恢复缺省情况。

【命令】

**[ipv6** **range** **start** *start-ipv6-address* **end** *end-ipv6-address*]

**[undo** **ipv6** **range**]

【缺省情况】

没有配置SNAT地址池的IPv6地址范围。

【视图】

SNAT地址池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[start** *start-ipv6-address*]：起始IPv6地址。

**[end** *end-ipv6-address*]：结束IPv6地址，必须大于等于起始IPv6地址。

【使用指导】

需要注意的是，一个SNAT地址池中最多允许有65536个IPv6地址，且不同SNAT地址池中的IPv6地址不允许重叠。

【举例】

\# 配置SNAT地址池lbsp的IPv6地址范围为1001::1～1001::100。

\<Sysname\> system-view

Sysname loadbalance snat-pool lbsp

Sysname-lbsnat-pool-lbsp ipv6 range start 1001::1 end 1001::100

**负载均衡 \-- 负载均衡配置命令 \-- lb-policy**

------------------------------------------------------------------------

**[lb-policy**]命令用来指定虚服务器引用的负载均衡策略。

**[undo** **lb-poilcy**]命令用来恢复缺省情况。

【命令】

**[lb-policy** *policy-name*]

**[undo** **lb-poilcy**]

【缺省情况】

虚服务器没有引用任何负载均衡策略。

【视图】

虚服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：负载均衡策略的名称，为1～63个字符的字符串，不区分大小写。

【使用指导】

虚服务器引用负载均衡策略，能够细化虚服务器负载均衡的粒度。根据策略中的匹配规则，使命中虚服务器的报文根据不同的报文内容进行不同的负载均衡处理，从而有效地丰富了负载均衡的负载功能。

需要注意的是，虚服务器只能引用与自身类型相关的策略模板，如：快速HTTP和HTTP类型的虚服务器，可以引用通用或HTTP类型的策略模板；IP、TCP和UDP类型的虚服务器，只能引用通用类型的策略模板。

【举例】

\# 指定IP类型的虚服务器vs3引用的负载均衡策略为lbp1。

\<Sysname\> system-view

Sysname virtual-server vs3 type ip

Sysname-vs-ip-vs3 lb-policy lbp1

**负载均衡 \-- 负载均衡配置命令 \-- loadbalance action**

------------------------------------------------------------------------

**[loadbalance** **action**]命令用来创建负载均衡动作，并进入负载均衡动作视图。

**[undo** **loadbalance** **action**]命令用来删除指定的负载均衡动作。

【命令】

**[loadbalance**[ **action** *action-name* [ **type** { **generic** \| **http** } ]]]

**[undo** **loadbalance** **action** *action-name*]

【缺省情况】

不存在任何负载均衡动作。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[action-name*]：负载均衡动作的名称，为1～63个字符的字符串，不区分大小写。

**[type**[ { **generic** \| **http** }]]：负载均衡动作的类型，包括通用和HTTP两种类型。创建负载均衡动作时必须指定本参数；而在进入已创建的负载均衡动作视图时可以不指定本参数，但若要指定本参数，则必须与创建时的类型一致。

【举例】

\# 创建通用类型的负载均衡动作lba1，并进入负载均衡动作视图。

\<Sysname\> system-view

Sysname loadbalance action lba1 type generic

Sysname-lba-generic-lba1

**负载均衡 \-- 负载均衡配置命令 \-- loadbalance class**

------------------------------------------------------------------------

**[loadbalance** **class**]命令用来创建负载均衡类，并进入负载均衡类视图。

**[undo** **loadbalance** **class**]命令用来删除指定的负载均衡类。

【命令】

**[loadbalance**[ **class** *class-name* [ **type** { **generic** **\|** **http** } [ **match-all** \| **match-any** ] ]]]

**[undo** **loadbalance** **class** *class-name*]

【缺省情况】

不存在任何负载均衡类。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[class-name*]：负载均衡类的名称，为1～63个字符的字符串，不区分大小写。

**[type**[ { **generic** **\|** **http** }]]：负载均衡类的类型，包括通用和HTTP两种类型。创建负载均衡类时必须指定本参数；而在进入已创建的负载均衡类视图时可以不指定本参数，但若要指定本参数，则必须与创建时的类型一致。

[[[ **match-all** \| **match-any** ]]]：**match-all**表示需要匹配所有规则才算匹配该类，**match-any**表示只需匹配任一规则就算匹配该类。缺省值为**match-all**。

【举例】

\# 创建通用类型的负载均衡类lbc1，并进入负载均衡类视图。

\<Sysname\> system-view

Sysname loadblance class lbc1 type generic

Sysname-lbc-generic-lbc1

**负载均衡 \-- 负载均衡配置命令 \-- loadbalance policy**

------------------------------------------------------------------------

**[loadbalance** **poliy** ]命令用来创建负载均衡策略，并进入负载均衡策略视图。

**[undo** **loadbalance** **policy**]命令用来删除指定的负载均衡策略。

【命令】

**[loadbalance**[ **policy** *policy-name* [ **type** { **generic** \| **http** } ]]]

**[undo** **loadbalance** **policy** *policy-name*]

【缺省情况】

不存在任何负载均衡策略。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：负载均衡策略的名称，为1～63个字符的字符串，不区分大小写。

**[type**[ { **generic** \| **http** }]]：负载均衡策略的类型，包括通用和HTTP两种类型。创建负载均衡策略时必须指定本参数；而在进入已创建的负载均衡策略视图时可以不指定本参数，但若要指定本参数，则必须与创建时的类型一致。

【举例】

\# 创建通用类型的负载均衡策略lbp1，并进入负载均衡策略视图。

\<Sysname\> system-view

Sysname loadbalance policy lbp1 type generic

Sysname-lbp-generic-lbp1

**负载均衡 \-- 负载均衡配置命令 \-- loadbalance snat-pool**

------------------------------------------------------------------------

**[loadbalance** **snat-pool**]命令用来创建SNAT地址池，并进入SNAT地址池视图。

**[undo** **loadbalance** **snat-pool**]命令用来删除指定的SNAT地址池。

【命令】

**[loadbalance** **snat-pool** *pool-name*]

**[undo** **loadbalance** **snat-pool** *pool-name*]

【缺省情况】

不存在任何SNAT地址池。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[pool-name*]：SNAT地址池的名称，为1～63个字符的字符串，不区分大小写。

【举例】

\# 创建SNAT地址池lbsp，并进入SNAT地址池视图。

\<Sysname\> system-view

Sysname loadbalance snat-pool lbsp

Sysname-lbsnat-pool-lbsp

**负载均衡 \-- 负载均衡配置命令 \-- match class**

------------------------------------------------------------------------

**[match** **class**]命令用来创建嵌套类的匹配规则。

**[undo** **match**]命令用来删除指定的匹配规则。

【命令】

**[match** [ *match-id*  **class** *class-name*]]

**[undo** **match** *match-id*]

【缺省情况】

负载均衡类中不存在任何匹配规则。

【视图】

负载均衡类视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[match-id*]：匹配规则的编号，取值范围为1～65535。如果指定编号的匹配规则不存在，则创建一条新的匹配规则；如果指定编号的匹配规则已存在，则对其进行修改。如果未指定本参数，系统将自动分配一个可用的最小编号。

*[class-name*]：要嵌套的负载均衡类名称，为1～63个字符的字符串，不区分大小写。不允许嵌套当前的负载均衡类。

【使用指导】

需要注意的是：

·如果嵌套的负载均衡类lbc1中已嵌套负载均衡类lbc2，则lbc2在此嵌套中将不会生效。

·一个负载均衡类中最多允许创建65535条匹配规则。

【举例】

\# 在通用类型的负载均衡类lbc1中，创建嵌套类的匹配规则为：嵌套负载均衡类lbc2。

\<Sysname\> system-view

Sysname loadbalance class lbc1 type generic

Sysname-lbc-generic-lbc1 match class lbc2

**负载均衡 \-- 负载均衡配置命令 \-- match content**

------------------------------------------------------------------------

**[match** **content**]命令用来创建HTTP实体类型的匹配规则。

**[undo** **match**]命令用来删除指定的匹配规则。

【命令】

**[match** [ *match-id*  **content** *content*  **offset** *offset* ]]

**[undo** **match** *match-id*]

【缺省情况】

负载均衡类中不存在任何匹配规则。

【视图】

负载均衡类视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[match-id*]：匹配规则的编号，取值范围为1～65535。如果指定编号的匹配规则不存在，则创建一条新的匹配规则；如果指定编号的匹配规则已存在，则对其进行修改。如果未指定本参数，系统将自动分配一个可用的最小编号。

**[content** *content*]：HTTP实体的正则表达式，为1～255个字符的字符串。

**[offset** *offset*]：HTTP实体基于HTTP报文起始位置的偏移量，取值范围为0～1000，缺省值为0。

【使用指导】

本命令只在HTTP类型的负载均衡类视图下支持。

配置了本命令后，如果HTTP报文的实体部分在偏移了*offset*后能够匹配指定的正则表达式，便认为此报文匹配了该规则。

需要注意的是：

·快速HTTP类型的虚服务器不支持本功能。

·一个负载均衡类中最多允许创建65535条匹配规则。

【举例】

\# 在HTTP类型的负载均衡类lbc2中，创建HTTP实体类型的匹配规则为：HTTP报文的实体部分偏移了10之后，包含字符串abc。

\<Sysname\> system-view

Sysname loadbalance class lbc2 type http

Sysname-lbc-http-lbc2 match content abc.\* offset 10

**负载均衡 \-- 负载均衡配置命令 \-- match cookie**

------------------------------------------------------------------------

**[match** **cookie**]命令用来创建HTTP Cookie类型的匹配规则。

**[undo** **match**]命令用来删除指定的匹配规则。

【命令】

**[match** [ *match-id*  **cookie** *cookie-name* **value** *value*]]

**[undo** **match** *match-id*]

【缺省情况】

负载均衡类中不存在任何匹配规则。

【视图】

负载均衡类视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[match-id*]：匹配规则的编号，取值范围为1～65535。如果指定编号的匹配规则不存在，则创建一条新的匹配规则；如果指定编号的匹配规则已存在，则对其进行修改。如果未指定本参数，系统将自动分配一个可用的最小编号。

**[cookie** *cookie-name*]：HTTP报文的Cookie名称，为1～63个字符的字符串，区分大小写。不包括(、)、\<、\>、@、,、;、:、\、\"、/、、、?、=、[、}、SP（空格符）、HT（水平制表符），以及ASCII码中小于等于31、大于等于127的字符。

**[value** *value*]：Cookie值的正则表达式，为1～255个字符的字符串。

【使用指导】]

本命令只在HTTP类型的负载均衡类视图下支持。

配置了本命令后，如果HTTP报文中携带有指定名称的Cookie，且Cookie值匹配了指定的正则表达式，便认为此报文匹配了该规则。

需要注意的是，一个负载均衡类中最多允许创建65535条匹配规则。

【举例】

\# 在HTTP类型的负载均衡类lbc2中，创建HTTP Cookie类型的匹配规则为：名为JSession-id的Cookie，其值中包含字符串abc。

\<Sysname\> system-view

Sysname loadbalance class lbc2 type http

Sysname-lbc-http-lbc2 match cookie JSeesion-id value abc.\*

**负载均衡 \-- 负载均衡配置命令 \-- match header**

------------------------------------------------------------------------

**[match** **header**]命令用来创建HTTP首部类型的匹配规则。

**[undo** **match**]命令用来删除指定的匹配规则。

【命令】

**[match** [ *match-id*  **header** *header-name* **value** *value*]]

**[undo** **match** *match-id*]

【缺省情况】

负载均衡类中不存在任何匹配规则。

【视图】

负载均衡类视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[match-id*]：匹配规则的编号，取值范围为1～65535。如果指定编号的匹配规则不存在，则创建一条新的匹配规则；如果指定编号的匹配规则已存在，则对其进行修改。如果未指定本参数，系统将自动分配一个可用的最小编号。

**[header** *header-name*]：HTTP报文首部的名称，为1～63个字符的字符串，不区分大小写。不包括(、)、\<、\>、@、,、;、:、\、\"、/、、、?、=、[、}、SP（空格符）、HT（水平制表符），以及ASCII码中小于等于31、大于等于127的字符。

**[value** *value*]：首部值的正则表达式，为1～255个字符的字符串。

【使用指导】]

本命令只在HTTP类型的负载均衡类视图下支持。

配置了本命令后，如果HTTP报文中携带有指定名称的首部，且首部值匹配了指定的正则表达式，便认为此报文匹配了该规则。

需要注意的是，一个负载均衡类中最多允许创建65535条匹配规则。

【举例】

\# 在HTTP类型的负载均衡类lbc2中，创建HTTP首部类型的匹配规则为：名为user-agent的HTTP报文首部，其值为abcd。

\<Sysname\> system-view

Sysname loadbalance class lbc2 type http

Sysname-lbc-http-lbc2 match header user-agent value abcd

**负载均衡 \-- 负载均衡配置命令 \-- match method**

------------------------------------------------------------------------

**[match** **method**]命令用来创建匹配报文方法类型的匹配规则。

**[undo** **match**]命令用来删除指定的匹配规则。

【命令】

**[match** [ *match-id*  **method** { **ext** *ext-type* \| **rfc** *rfc-type* }]]

**[undo** **match** *match-id*]

【缺省情况】

负载均衡类中不存在任何匹配规则。

【视图】

负载均衡类视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[match-id*]：匹配规则的编号，取值范围为1～65535。如果指定编号的匹配规则不存在，则创建一条新的匹配规则；如果指定编号的匹配规则已存在，则对其进行修改。如果未指定本参数，系统将自动分配一个可用的最小编号。

**[ext** *ext-type*]：扩展类型，即用户可以输入指定的字符串作为方法名。*ext-type*为1～63个字符，区分大小写。不包括(、)、\<、\>、@、,、;、:、\、\"、/、、、?、=、[、}、SP（空格符）、HT（水平制表符），以及ASCII码中小于等于31、大于等于127的字符。

**[rfc** *rfc-type*]：RFC类型，即对HTTP请求报文中URI所标识资源的执行方法。*rfc-type*包括：

·]**CONNECET**：保留。

·**DELETE**：请求删除URI所标识的资源。

·**GET**：请求获取URI所标识的资源。

·**HEAD**：请求获取URI所标识资源的响应消息首部。

·**OPTIONS**：请求查询服务器支持的功能，即查询与URI所标识资源相关的选项和需求。

·**POST**：在URI所标识的资源后附加新数据。

·**PUT**：请求服务器存储一个资源，并用URI作为其标识。

·**TRACE**：请求服务器回送收到的请求消息，主要用于测试或诊断。

【使用指导】

本命令只在HTTP类型的负载均衡类视图下支持。

需要注意的是，一个负载均衡类中最多允许创建65535条匹配规则。

【举例】

\# 在HTTP类型的负载均衡类lbc2中，创建匹配报文方法类型的匹配规则为扩展类型的user。

\<Sysname\> system-view

Sysname loadbalance class lbc2 type http

Sysname-lbc-http-lbc2 match method ext user

\# 在HTTP类型的负载均衡类lbc2中创建匹配报文方法类型的匹配规则为RFC类型的**CONNECT**。

\<Sysname\> system-view

Sysname loadbalance class lbc2 type http

Sysname-lbc-http-lbc2 match method rfc CONNECT

**负载均衡 \-- 负载均衡配置命令 \-- match source**

------------------------------------------------------------------------

**[match** **source**]命令用来创建源IP地址类型的匹配规则。

**[undo** **match**]命令用来删除指定的匹配规则。

【命令】

**[match** [ *match-id*  **source** { **ip** **address** *ipv4-address* [ *mask-length* \| *mask* ] \| **ipv6** **address** *ipv6-address*  *prefix-length*  }]]

**[undo** **match** *match-id*]

【缺省情况】

负载均衡类中不存在任何匹配规则。

【视图】

负载均衡类视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[match-id*]：匹配规则的编号，取值范围为1～65535。如果指定编号的匹配规则不存在，则创建一条新的匹配规则；如果指定编号的匹配规则已存在，则对其进行修改。如果未指定本参数，系统将自动分配一个可用的最小编号。

**ip** **address** *ipv4-address*：IPv4地址。

*[mask-lengh*]：子网掩码长度，取值范围为0～32，缺省值为32。

*[mask*]：子网掩码，缺省值为255.255.255.255。

**[ipv6** **address** *ipv6-address*]：IPv6地址。

*[prefix-length*]：前缀长度，取值范围为0～128，缺省值为128。

【使用指导】

需要注意的是，一个负载均衡类中最多允许创建65535条匹配规则。

【举例】

\# 在通用类型的负载均衡类lbc1中，创建源IP地址类型的匹配规则为：匹配IPv4地址1.1.1.1/32。

\<Sysname\> system-view

Sysname loadbalance class lbc1 type generic

Sysname-lbc-generic-lbc1 match source ip address 1.1.1.1

**负载均衡 \-- 负载均衡配置命令 \-- match url**

------------------------------------------------------------------------

**[match** **url**]命令用来创建HTTP URL类型的匹配规则。

**[undo** **match**]命令用来在删除指定的匹配规则。

【命令】

**[match** [ *match-id*  **url** *url*]]

**[undo** **match** *match-id*]

【缺省情况】

负载均衡类中不存在任何匹配规则。

【视图】

负载均衡类视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[match-id*]：匹配规则的编号，取值范围为1～65535。如果指定编号的匹配规则不存在，则创建一条新的匹配规则；如果指定编号的匹配规则已存在，则对其进行修改。如果未指定本参数，系统将自动分配一个可用的最小编号。

**[url** *url*]：URL的正则表达式，为1～255个字符的字符串。

【使用指导】

本命令只在HTTP类型的负载均衡类视图下支持。

需要注意的是，一个负载均衡类中最多允许创建65535条匹配规则。

【举例】

\# 在HTTP类型的负载均衡类lbc2中，创建HTTP URL类型的匹配规则为：.\*.html。

\<Sysname\> system-view

Sysname loadbalance class lbc2 type http

Sysname-lbc-http-lbc2 match url .\*.html

**负载均衡 \-- 负载均衡配置命令 \-- parameter**

------------------------------------------------------------------------

**[parameter**]命令用来指定虚服务器引用的参数模板。

**[undo**]**parameter**命令用来恢复缺省情况。

【命令】

**[parameter**]**[ip**[\| **tcp** }]*profile-name*

**[undo**]**parameter****[ip**[\| **tcp** }]

【缺省情况】]

虚服务器没有引用任何参数模板。]

【视图】

虚服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

[[{ **http** \| **ip**\| **tcp** }]]：参数模板的类型，包括HTTP、IP和TCP三种类型。其中，**http**和**tcp**参数只在快速HTTP和HTTP类型的虚服务器视图下支持。

*[profile-name*]：参数模板的名称，为1～63个字符的字符串，不区分大小写。

【使用指导】

参数模板用来对虚服务器上的流量进行比较深入的解析、处理和优化。虚服务器引用了参数模板后，就要根据该参数模板的配置对匹配流量进行相应的处理。

【举例】

\# 指定IP类型的虚服务器vs3引用IP类型的参数模板pp2。

\<Sysname\> system-view

Sysname virtual-server vs3 type ip

Sysname-vs-ip-vs3 parameter ip pp2

**负载均衡 \-- 负载均衡配置命令 \-- parameter-profile**

------------------------------------------------------------------------

**[parameter-profile**]命令用来创建参数模板，并进入参数模板视图。

**[undo****parameter-profile**]命令用来删除指定的参数模板。

【命令】

**[parameter-profile**]*profile-name*[[ **type** { **http** \| **ip** \| **tcp** } ]]

**[undo****parameter-profile** *profile-name*]

【缺省情况】

不存在任何参数模板。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[profile-name*]：参数模板的名称，为1～63个字符的字符串，不区分大小写。

**[type**[ { **http** \| **ip** \| **tcp** }]]：参数模板的类型，包括HTTP、IP和TCP三种类型。创建参数模板时必须指定本参数；而在进入已创建的参数模板视图时可以不指定本参数，但若要指定本参数，则必须与创建时的类型一致。

【使用指导】

通过配置参数模板可以进行一些高级参数的配置。这样，当参数模板被虚服务器引用之后，可以对虚服务器的业务流量进行更深入的解析、处理和优化。

【举例】

\# 创建IP类型的参数模板pp2，并进入参数模板视图。

\<Sysname\> system-view

Sysname parameter-profile pp2 type ip

Sysname-para-ip-pp2

**负载均衡 \-- 负载均衡配置命令 \-- payload**

------------------------------------------------------------------------

**[payload**]命令用于配置HTTP载荷持续性方法。

**[undo****payload**]命令用来删除HTTP载荷持续性方法。

【命令】

**[payload** [ **offset** *offset*   **start** *start-string*  [ **end** *end-string* \| **length** *length* ]]]

**[undo****payload**]

【缺省情况】

不存在任何持续性方法。

【视图】

持续性组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[offset** *offset*]：HTTP载荷基于HTTP报文起始位置的偏移量，取值范围为0～1000，缺省值为0。

**[start** *start-string*]：HTTP载荷开始标记的正则表达式，即从*offset*起到本标记为开始，为1～127个字符的字符串。

**[end** *end-string*]：HTTP载荷结束标记的正则表达式，即从*start-string*起到本标记为结束，为1～127个字符的字符串。

**[length** *length*]：HTTP载荷的长度，取值范围为0～1000，缺省值为0，表示所有长度。

【使用指导】

本命令只在HTTP载荷类型的持续性组视图下支持。

本命令用来根据*offset*、*start-string*、*end-string*及*length*获取生成持续性表项的HTTP载荷信息。*start-string*和*end-string*将不计入持续性表项信息中。

需要注意的是，快速HTTP类型的虚服务器不支持引用HTTP载荷持续性方法。

【举例】

\# 在HTTP载荷类型的持续性组sg5中，配置HTTP载荷持续性方法为：从HTTP报文起始位置的第10个字节起，长度为20个字节HTTP载荷来生成持续性表项。

\<Sysname\> system-view

Sysname sticky-group sg5 type payload

Sysname-sticky-payload-sg5 payload offset 10 length 20

**负载均衡 \-- 负载均衡配置命令 \-- port (real server view)**

------------------------------------------------------------------------

**[port**]命令用来配置实服务器的端口号。

**[undo** **port**]命令用来恢复缺省情况。

【命令】

**[port** *port-number*]

**[undo** **port**]

【缺省情况】

实服务器的端口号为0（表示继续使用原报文携带的端口号）。

【视图】

实服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-number*]：端口号，取值范围为0～65535，0表示继续使用原报文携带的端口号。

【使用指导】

需要注意的是，只有当实服务组开启了NAT功能后，本配置才有效。

【举例】

\# 配置实服务器rs的端口号为8080。

\<Sysname\> system-view

Sysname real-server rs

Sysname-rserver-rs port 8080

【相关命令】

·**transparent** **enable**

**负载均衡 \-- 负载均衡配置命令 \-- port (virtual server view)**

------------------------------------------------------------------------

**[port**]命令用来配置虚服务器的端口号。

**[undo** **port**]命令用来恢复缺省情况。

【命令】

**[port** *port-number*]

**[undo** **port**]

【缺省情况】

IP/TCP/UDP类型虚服务器的端口号为0（表示任意端口号），快速HTTP/HTTP类型虚服务器的端口号为80。

【视图】

虚服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-number*]：端口号。对于IP/TCP/UDP类型的虚服务器，取值范围为0～65535，0表示任意端口号；对于快速HTTP/HTTP类型的虚服务器，取值范围为1～65535。

【使用指导】

需要注意的是，如果虚服务器引用了SSL策略，则必须为其配置一个非缺省端口号（通常用443）。

【举例】

\# 配置IP类型的虚服务器vs3的端口号为8080。

\<Sysname\> system-view

Sysname virtual-server vs3 type ip

Sysname-vs-ip-vs3 port 8080

【相关命令】

·**ssl-server-policy**

**负载均衡 \-- 负载均衡配置命令 \-- predictor**

------------------------------------------------------------------------

**[predictor**]命令用来配置实服务组的调度算法。

**[undo** **predictor**]命令用来恢复缺省情况。

【命令】

**[predictor**[ **hash** **address** { **destination** \| **source** \| **source-ip-port** } [ **mask** *mask-length* ]  **prefix** *prefix-length* ]]

**[predictor**[ { **least-connection** \| **random** \| **round-robin** }]]

**[undo** **predictor**]

【缺省情况】

实服务组的调度算法为加权轮转算法。

【视图】

实服务组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[hash** **address**]：根据IP地址进行的哈希算法。

**[destination**]：根据目的IP地址进行的哈希算法。

**[source**]：根据源IP地址进行的哈希算法。

**[source-ip-port**]：根据源IP地址和端口号进行的哈希算法。

**[mask** *mask-length*]：哈希算法中IPv4地址的掩码长度，取值范围为0～32，缺省值为32。

**[prefix** *prefix-length*]：哈希算法中IPv6地址的前缀长度，取值范围为0～128，缺省值为128。

**[least-connection**]：加权最小连接算法，即总是把新连接分发给加权活动连接数（当前活动连接数/权值）最小的实服务。

**[random**]：随机算法，即把新连接随机分发给每个实服务器。

**[round-robin**]：加权轮转算法，即根据实服务权值的大小把新连接依次分发给每个实服务器，权值越大，分配的新连接越多。

【举例】

\# 配置实服务组sf的调度算法为随机算法。

\<Sysname\> system-view

Sysname server-farm sf

Sysname-sfarm-sf predictor random

**负载均衡 \-- 负载均衡配置命令 \-- priority**

------------------------------------------------------------------------

**[priority**]命令用来配置实服务器的调用优先级。

**[undo**] **priority**命令用来恢复缺省情况。

【命令】

**[priority**] *priority-value*

**[undo**] **priority**

【缺省情况】

实服务器的调用优先级为4。

【视图】

实服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[priority-value*]：优先级，取值范围为1～8。数值越大，越被优先调用。

【举例】

\# 配置实服务器rs的调用优先级为3。

\<Sysname\> system-view

Sysname real-server rs

Sysname-rserver-rs priority 3

**负载均衡 \-- 负载均衡配置命令 \-- probe (real server view)**

------------------------------------------------------------------------

**[probe**]命令用来指定实服务器的健康检测方法。

**[undo** **probe**]命令用来恢复缺省情况。

【命令】

**[probe** *template-name*]

**[undo** **probe** *template-name*]

【缺省情况】

没有指定实服务器的健康检测方法。

【视图】

实服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[template-name*]：健康检测方法所使用的NQA模板名称，为1～32个字符的字符串，不区分大小写。

【使用指导】

需要注意的是：

·请使用**nqa** **template**命令创建健康检测方法所使用的NQA模板，通过健康检测可以对实服务器进行检测，保证其能够提供有效的服务。

·用户既可在实服务组视图下对组内的所有实服务器进行配置，也可在实服务器视图下只对当前实服务器进行配置，后者的配置优先级较高。

【举例】

\# 创建ICMP类型的NQA模板t4，并将其指定为实服务器rs的健康检测方法。

\<Sysname\> system-view

Sysname nqa template icmp t4

Sysname-nqatplt-icmp-t4 quit

Sysname real-server rs

Sysname-rserver-rs probe t4{.TerminalDisplayChar}

【相关命令】

·**nqa** **template**（网络管理和监控命令参考/NQA）

·**success-criteria**(real server view)

**负载均衡 \-- 负载均衡配置命令 \-- probe (server farm view)**

------------------------------------------------------------------------

**[probe**]命令用来指定实服务组的健康检测方法。

**[undo** **probe**]命令用来恢复缺省情况。

【命令】

**[probe** *template-name*]

**[undo** **probe** *template-name*]

【缺省情况】

没有指定实服务组的健康检测方法。

【视图】

实服务组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[template-name*]：健康检测方法所使用的NQA模板名称，为1～32个字符的字符串，不区分大小写。

【使用指导】

需要注意的是：

·请使用**nqa** **template**命令创建健康检测方法所使用的NQA模板，通过健康检测可以对实服务器进行检测，保证其能够提供有效的服务。

·用户既可在实服务组视图下对组内的所有实服务器进行配置，也可在实服务器视图下只对当前实服务器进行配置，后者的配置优先级较高。

【举例】

\# 创建ICMP类型的NQA模板t4，并将其指定为实服务组sf的健康检测方法。

\<Sysname\>system-view

Sysname nqa template icmp t4

Sysname-nqatplt-icmp-t4 quit

Sysname server-farm sf

Sysname-sfarm-sf probe t4{.TerminalDisplayChar}

【相关命令】

·**nqa** **template**（网络管理和监控命令参考/NQA）

·{.TerminalDisplayChar}**success-criteria**(server farm view)

**负载均衡 \-- 负载均衡配置命令 \-- rate-limit bandwidth (real server view)**

------------------------------------------------------------------------

**[rate-limit** **bandwidth**]命令用来配置实服务器所允许的最大带宽。

**[undo** **rate-limit** **bandwidth**]命令用来恢复缺省情况。

【命令】

**[rate-limit**[ **bandwidth** [ **inbound** \| **outbound** ] *bandwidth-value*]]

**[undo**[ **rate-limit** **bandwidth** [ **inbound** \| **outbound** ]]]

【缺省情况】

实服务器所允许的最大总带宽、最大入带宽和最大出带宽均为0千字节/秒，即不受限制。

【视图】

实服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[inbound**]：配置最大入带宽。

**[outbound**]：配置最大出带宽。

*[bandwidth-value*]：最大带宽值，取值范围为0～4294967295，单位为千字节/秒，0千字节/秒表示最大带宽不受限制。

【使用指导】

需要注意的是，如果未指定**inbound**和**outbound**参数，则配置最大总带宽，总带宽等于入带宽与出带宽之和。

【举例】

\# 配置实服务器rs所允许的最大总带宽为1千字节/秒。

\<Sysname\> system-view

Sysname real-server rs

Sysname-rserver-rs rate-limit bandwidth 1

\# 配置实服务器rs所允许的最大入带宽为1千字节/秒。

\<Sysname\> system-view

Sysname real-server rs

Sysname-rserver-rs rate-limit bandwidth inbound 1

\# 配置实服务器rs所允许的最大出带宽为1千字节/秒。

\<Sysname\> system-view

Sysname real-server rs

Sysname-rserver-rs rate-limit bandwidth outbound 1

**负载均衡 \-- 负载均衡配置命令 \-- rate-limit bandwidth (virtual server view)**

------------------------------------------------------------------------

**[rate-limit** **bandwidth**]命令用来配置虚服务器所允许的最大带宽。

**[undo** **rate-limit** **bandwidth**]命令用来恢复缺省情况。

【命令】

**[rate-limit**[ **bandwidth** [ **inbound** \| **outbound** ] *bandwidth-value*]]

**[undo**[ **rate-limit** **bandwidth** [ **inbound** \| **outbound** ]]]

【缺省情况】

虚服务器所允许的最大总带宽、最大入带宽和最大出带宽均为0千字节/秒，即不受限制。

【视图】

虚服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[inbound**]：最大入带宽。

**[outbound**]：最大出带宽。

*[bandwidth-value*]：最大带宽值，取值范围为0～4294967295，单位为千字节/秒，0千字节/秒表示最大带宽不受限制。

【使用指导】

需要注意的是，如果未指定**inbound**和**outbound**参数，则配置最大总带宽，总带宽等于入带宽与出带宽之和。

【举例】

\# 配置IP类型的虚服务器vs3所允许的最大总带宽为1千字节/秒。

\<Sysname\> system-view

Sysname virtual-server vs3 type ip

Sysname-vs-ip-vs3 rate-limit bandwidth 1

\# 配置IP类型的虚服务器vs3所允许的最大入带宽为1千字节/秒。

\<Sysname\> system-view

Sysname virtual-server vs3 type ip

Sysname-vs-ip-vs3 rate-limit bandwidth inbound 1

\# 配置IP类型的虚服务器vs3所允许的最大出带宽为1千字节/秒。

\<Sysname\> system-view

Sysname virtual-server vs3 type ip

Sysname-vs-ip-vs3 rate-limit bandwidth outbound 1

**负载均衡 \-- 负载均衡配置命令 \-- rate-limit connection (real server view)**

------------------------------------------------------------------------

**[rate-limit** **connection**]命令用来配置实服务器所允许的每秒最大连接数。

**[undo** **rate-limit** **connection**]命令用来恢复缺省情况。

【命令】

**[rate-limit** **connection** *connection-number*]

**[undo** **rate-limit** **connection**]

【缺省情况】

实服务器所允许的每秒最大连接数为0，即不受限制。

【视图】

实服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[connection-number*]：每秒最大连接数，取值范围为0～4294967295，0表示实服务器所允许的每秒最大连接数不受限制。

【举例】

\# 配置实服务器rs所允许的每秒最大连接数为10000。

\<Sysname\> system-view

Sysname real-server rs

Sysname-rserver-rs rate-limit connection 10000

**负载均衡 \-- 负载均衡配置命令 \-- rate-limit connection (virtual server view)**

------------------------------------------------------------------------

**[rate-limit** **connection**]命令用来配置虚服务器所允许的每秒最大连接数。

**[undo** **rate-limit** **connection**]命令用来恢复缺省情况。

【命令】

**[rate-limit** **connection** *connection-number*]

**[undo** **rate-limit** **connection**]

【缺省情况】

虚服务器所允许的每秒最大连接数为0，即不受限制。

【视图】

虚服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[connection-number*]：每秒最大连接数，取值范围为0～4294967295，0表示虚服务器所允许的每秒最大连接数不受限制。

【举例】

\# 配置IP类型的虚服务器vs3所允许的每秒最大连接数为10000。

\<Sysname\> system-view

Sysname virtual-server vs3 type ip

Sysname-vs-ip-vs3 rate-limit connection 10000

**负载均衡 \-- 负载均衡配置命令 \-- real-server**

------------------------------------------------------------------------

**[real-server**]命令用来创建实服务器，并进入实服务器视图。

**[undo** **real-server**]命令用来删除指定的实服务器。

【命令】

**[real-server** *real-server-name*]

**[undo** **real-server** *real-server-name*]

【缺省情况】

不存在任何实服务器。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[real-server-name*]：实服务器的名称，为1～63个字符的字符串，不区分大小写。

【举例】

\# 创建实服务器rs，并进入实服务器视图。

\<Sysname\> system-view

Sysname real-server rs

Sysname-rserver-rs

**负载均衡 \-- 负载均衡配置命令 \-- rebalance per-request**

------------------------------------------------------------------------

**[rebalance** **per-request**]命令用来配置对每个HTTP请求报文都进行负载均衡。

**[undo****rebalance** **per-request**]命令用来恢复缺省情况。

【命令】

**[rebalance** **per-request**]

**[undo****rebalance** **per-request**]

【缺省情况】

只对一条连接的第一个HTTP请求报文进行负载均衡，其余请求报文的处理方式与第一个相同。

【视图】

参数模板视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本命令只在HTTP类型的参数模板视图下支持。

【举例】

\# 在HTTP类型的参数模板pp1中，配置对每个HTTP请求报文都进行负载均衡。

\<Sysname\> system-view

Sysname parameter-profile pp1 type http

Sysname-para-http-pp1 rebalance per-request

**负载均衡 \-- 负载均衡配置命令 \-- redirect relocation**

------------------------------------------------------------------------

**[redirect** **relocation**]命令用来开启虚服务器的重定向功能并指定重定向URL。

**[undo** **redirect** **relocation**]命令用来关闭虚服务器的重定向功能。

【命令】

**[redirect** **relocation** *relocation*]

**[undo** **redirect** **relocation**]

【缺省情况】

虚服务器的重定向功能处于关闭状态。

【视图】

虚服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[relocation*]：指定重定向URL，开启了虚服务器的重定向功能后，所有匹配该虚服务器的请求报文都将被重定向到该URL。为1～255个字符的字符串，区分大小写。也可以使用以下特定含义的字符串（各自只允许使用一次）：

·%h：使用客户端请求报文中的主机名。

·%p：使用客户端请求报文中的URL。

【使用指导】

本命令只在HTTP类型的虚服务器视图下支持。

【举例】

\# 开启HTTP类型的虚服务器vs2的重定向功能，并指定重定向URL为客户端请求报文中的主机名和URL。

\<Sysname\> system-view

Sysname virtual-server vs2 type http

Sysname-vs-http-vs2 redirect relocation %h%p

**负载均衡 \-- 负载均衡配置命令 \-- redirect return-code**

------------------------------------------------------------------------

**[redirect** **return-code**]命令用来配置负载均衡设备返回给客户端的重定向报文中的状态码。

**[undo** **redirect** **return-code**]命令用来恢复缺省情况。

【命令】

**[redirect**[ **return-code** [ **301** \| **302** }]]

**[undo** **redirect** **return-code**]

【缺省情况】]

负载均衡设备返回给客户端的重定向报文中的状态码为302。

【视图】

虚服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[301**]：状态码为301，表示永久删除被请求的资源。

**[302**]：状态码为302，表示临时删除被请求的资源。

【使用指导】

本命令只在HTTP类型的虚服务器视图下支持。

需要注意的是，本命令只有在开启了虚服务器的重定向功能后才会生效。

【举例】

\# 在HTTP类型的虚服务器vs2上，配置负载均衡设备返回给客户端的重定向报文中的状态码为301。

\<Sysname\> system-view

Sysname virtual-server vs2 type http

Sysname-vs-http-vs2 redirect return-code 301

【相关命令】

·**redirect** **relocation**

**负载均衡 \-- 负载均衡配置命令 \-- reset loadbalance hot-backup statistics**

------------------------------------------------------------------------

![说明](负载均衡命令.files/image001.png)

集中式设备不支持本命令，请以设备的实际情况为准。

****

**[reset** **loadbalance** **hot-backup** **statistics**]命令用来清除负载均衡双机热备的统计信息。

【命令】

**[reset** **loadbalance** **hot-backup** **statistics**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 清除负载均衡双机热备的统计信息。

\<Sysname\> reset loadbalance hot-backup statistics

**负载均衡 \-- 负载均衡配置命令 \-- reset real-server statistics**

------------------------------------------------------------------------

**[reset** **real-server** **statistics**]命令用来清除实服务器的统计信息。

【命令】

**[reset** **real-server** **statistics** [ *real-server-name* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[real-server-name*]：清除指定实服务器的统计信息。*real-server-name*为实服务器的名称，为1～63个字符的字符串，不区分大小写。如果未指定本参数，将清除所有实服务器的统计信息。

【举例】

\# 清除所有实服务器的统计信息。

\<Sysname\> reset real-server statistics

【相关命令】

·**display** **real-server** **statistics**

**负载均衡 \-- 负载均衡配置命令 \-- reset virtual-server statistics**

------------------------------------------------------------------------

**[reset** **virtual-server** **statistics**]命令用来清除虚服务器的统计信息。

【命令】

**[reset** **virtual-server** **statistics** [ *virtual-server-name* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[virtual-server-name*]：清除指定虚服务器的统计信息。*virtual-server-name*为虚服务器的名称，为1～63个字符的字符串，不区分大小写。如果未指定本参数，将清除所有虚服务器的统计信息。

【举例】

\# 清除所有虚服务器的统计信息。

\<Sysname\> reset virtual-server statistics

【相关命令】

·**display****virtual-server** **statistics**

**负载均衡 \-- 负载均衡配置命令 \-- secondary-cookie delimiters**

------------------------------------------------------------------------

**[secondary-cookie** **delimiters**]命令用来配置URL中分隔Secondary Cookie的字符。

**[undo****secondary-cookie** **delimiters**]命令用来恢复缺省情况。

【命令】

**[secondary-cookie** **delimiters** *text*]

**[undo****secondary-cookie** **delimiters**]

【缺省情况】

URL中分隔Secondary Cookie的字符为"/"、"&"、"\#"或"+"。

【视图】

参数模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：分隔字符，为1～4个字符的字符串，包括：!、\"、\#、;、\<、\>、?、、\、、\^、\`、[\|]、:、@、&、\$、+、\*、\'、(、)、,、/。该字符串中的每个字符都被认为是分隔字符。

【使用指导】

本命令只在HTTP类型的参数模板视图下支持。

【举例】

\# 在HTTP类型的参数模板pp1中，配置URL中分隔Secondary Cookie的字符为"/"、"@"、"\#"或"\$"。

\<Sysname\> system-view

Sysname parameter-profile pp1 type http

Sysname-para-http-pp1 secondary-cookie delimiters !@#\$

**负载均衡 \-- 负载均衡配置命令 \-- secondary-cookie start**

------------------------------------------------------------------------

**[secondary-cookie** **start**]命令用来配置URL中Secondary Cookie的起始位置标示字符。

**[undo****secondary-cookie** **start**]命令用来恢复缺省情况。

【命令】

**[secondary-cookie** **start** *text*]

**[undo****secondary-cookie** **start**]

【缺省情况】

URL中Secondary Cookie的起始位置标示字符为"?"。

【视图】

参数模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：标示字符，为1～2个字符的字符串，包括：!、\"、\#、;、\<、\>、?、、\、、\^、\`、[\|]。

【使用指导】

本命令只在HTTP类型的参数模板视图下支持。

【举例】

\# 在HTTP类型的参数模板pp1中，配置URL中Secondary Cookie的起始位置标示字符为"?"或"!"。

\<Sysname\> system-view

Sysname parameter-profile pp1 type http

Sysname-para-http-pp1 secondary-cookie start ?!

**负载均衡 \-- 负载均衡配置命令 \-- selected-server**

------------------------------------------------------------------------

**[selected-server**]命令用来配置实服务组中可被调度算法调用的实服务器数量限制。

**[undo** **selected-server**]命令用来恢复缺省情况。

【命令】

**[selected-server** **min** *min-number* **max** *max-number*]

**[undo** **selected-server**]

【缺省情况】

实服务组中调用优先级最高的实服务器全部被调度算法调用。

【视图】

实服务组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[min** *min-number*]：可被调度算法调用的实服务器最小数量，取值范围为1～1000。

**[max** *max-number*]：可被调度算法调用的实服务器最大数量，取值范围1～1000，且必须大于等于*min-number*。

【使用指导】

缺省情况下，一个实服务组中调用优先级最高的实服务器全部被调度算法调用。用户通过本命令可以限制可被调度算法调用的实服务器数量：

·如果调用优先级最高的可用实服务器数量大于*max-number*时，则只选用*max-number*个实服务器。

·如果调用优先级最高的可用实服务器数量小于*min-number*时，除了调用全部优先级最高的可用实服务器外，还会调用优先级次高的可用实服务器，直至调用的可用实服务器数量达到*min-number*，或者没有可用的实服务器可调用为止。

【举例】

\# 配置实服务组sf中可被调度算法调用的实服务器最小数量为20，最大数量为30。

\<Sysname\> system-view

Sysname server-farm sf

Sysname-sfarm-sf selected-server min 20 max 30

【相关命令】

·**predictor**

·**priority**

**负载均衡 \-- 负载均衡配置命令 \-- server-connection reuse**

------------------------------------------------------------------------

**[server-connection** **reuse**]命令用来配置允许负载均衡设备与服务器的连接复用。

**[undo****server-connection** **reuse**]命令用来恢复缺省情况。

【命令】

**[server-connection** **reuse**]

**[undo****server-connection** **reuse**]

【缺省情况】

不允许负载均衡设备与服务器的连接复用。

【视图】

参数模板视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本命令只在HTTP类型的参数模板视图下支持。

允许负载均衡设备与服务器的连接复用，即允许负载均衡设备与服务器建立长连接，使多个客户端复用同一条与服务器的连接，以减少客户端与服务器之间打开的连接数。

需要注意的是，快速HTTP类型的虚服务器不支持本功能。

【举例】

\# 在HTTP类型的参数模板pp1中，配置允许负载均衡设备与服务器的连接复用。

\<Sysname\> system-view

Sysname parameter-profile pp1 type http

Sysname-para-http-pp1 server-connection reuse

**负载均衡 \-- 负载均衡配置命令 \-- server-farm (LB action view)**

------------------------------------------------------------------------

**[server-farm**]命令用来指定指导转发的实服务组。

**[undo** **server-farm**]命令用来恢复缺省情况。

【命令】

**[server-farm** *server-farm-name* [ **backup** *backup-server-farm-name*   **sticky** *sticky-name* ]]

**[undo** **server-farm**]

【缺省情况】

没有指定指导转发的实服务组。

【视图】

负载均衡动作视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[server-farm-name*]：主用实服务组的名称，为1～63个字符的字符串。

**[backup** *backup-**server-farm-name*]：备用实服务组的名称，为1～63个字符的字符串。

**[sticky***sticky-name*]：实服务组所对应持续性组的名称，为1～63个字符的字符串。

【使用指导】

需要注意的是：

·本命令与**forward** **all**命令互斥，当配置了其中一条后，另一条的配置将被自动取消。

·当主用实服务组可用（该实服务组存在且有可用的实服务器）时，使用主用实服务组指导转发；当主用实服务组不可用而备用实服务组可用时，使用备用实服务组指导转发。

【举例】

\# 在通用类型的负载均衡动作lba1中，指定指导转发的主用实服务组为sf，备用实服务组为sfb，持续性组为sg1。

\<Sysname\> system-view

Sysname loadbalance action lba1 type generic

Sysname-lba-generic-lba1 server-farm sf backup sfb sticky sg1

【相关命令】

·**forward** **all**

**负载均衡 \-- 负载均衡配置命令 \-- server-farm (real server view)**

------------------------------------------------------------------------

**[server-farm**]命令用来指定实服务器所属的实服务组。

**[undo**] **server-farm**命令用来恢复缺省情况。

【命令】

**[server-farm***server-farm-name*]

**[undo** **server-farm**]

【缺省情况】

实服务器不属于任何实服务组。

【视图】

实服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[server-farm-name*]：实服务组的名称，为1～63个字符的字符串，不区分大小写。可以是尚未创建的实服务组。

【举例】

\# 指定实服务器rs属于实服务组sf。

\<Sysname\> system-view

Sysname real-server rs

Sysname-rserver-rs server-farm sf

**负载均衡 \-- 负载均衡配置命令 \-- server-farm (system view)**

------------------------------------------------------------------------

**[server-farm**]命令用来创建实服务组，并进入实服务组视图。

**[undo** **server-farm**]命令用来删除指定的实服务组。

【命令】

**[server-farm** *server-farm-name*]

**[undo** **server-farm** *server-farm-name*]

【缺省情况】

不存在任何实服务组。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[server-farm-name*]：实服务组的名称，为1～63个字符的字符串，不区分大小写。

【使用指导】

为了便于对多台服务器进行管理，可以依据这些服务器的共有属性划分成不同的组，称为实服务组。比如，可按存储内容的不同划分为歌曲服务器组、视频服务器组或图片服务器组等。

【举例】

\# 创建实服务组sf，并进入实服务组视图。

\<Sysname\> system-view

Sysname server-farm sf

Sysname-sfarm-sf

**负载均衡 \-- 负载均衡配置命令 \-- service enable**

------------------------------------------------------------------------

**[service** **enable**]命令用来开启虚服务器。

**[undo** **service** **enable**]命令用来关闭虚服务器。

【命令】

**[service** **enable**]

**[undo** **service** **enable**]

【缺省情况】

虚服务器处于关闭状态。

【视图】

虚服务器视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 开启IP类型的虚服务器vs3。

\<Sysname\> system-view

Sysname virtual-server vs3 type ip

Sysname-vs-ip-vs3 service enable

**负载均衡 \-- 负载均衡配置命令 \-- set ip tos (LB action view)**

------------------------------------------------------------------------

**[set** **ip** **tos**]命令用来配置发往服务器的IP报文中的ToS字段。

**[undo****set** **ip** **tos**]命令用来恢复缺省情况。

【命令】

**[set** **ip** **tos** *tos-number*]

**[undo****set** **ip** **tos**]

【缺省情况】

不改变发往服务器的IP报文中的ToS字段。

【视图】

负载均衡动作视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[tos-number*]：ToS字段值，取值范围为0～255。

【举例】

\# 在通用类型的负载均衡动作lba1中，配置发往服务器的IP报文中的ToS字段值为20。

\<Sysname\> system-view

Sysname loadbalance action lba1 type generic

Sysname-lba-generic-lba1 set ip tos 20

**负载均衡 \-- 负载均衡配置命令 \-- set ip tos (parameter profile view)**

------------------------------------------------------------------------

**[set** **ip** **tos**]命令用来配置发往客户端的IP报文中的ToS字段。

**[undo****set** **ip** **tos**]命令用来恢复缺省情况。

【命令】

**[set** **ip** **tos** *tos-number*]

**[undo** **set** **ip** **tos**]

【缺省情况】

不改变发往客户端的IP报文中的ToS字段。

【视图】

参数模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[tos-number*]：ToS字段值，取值范围0～255。

【使用指导】

本命令只在IP类型的参数模板视图下支持。

【举例】

\# 在IP类型的参数模板pp2中，配置发往客户端的IP报文中的ToS字段值为20。

\<Sysname\> system-view

Sysname parameter-profile pp2 type ip

Sysname-para-ip-pp2 set ip tos 20

**负载均衡 \-- 负载均衡配置命令 \-- shutdown**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭实服务器。

**[undo** **shutdown**]命令用来开启实服务器。

【命令】

**[shutdown**]

**[undo** **shutdown**]

【缺省情况】

实服务器处于开启状态。

【视图】

实服务器视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 关闭实服务器rs。

\<Sysname\> system-view

Sysname real-server rs

Sysname-rserver-rs shutdown

**负载均衡 \-- 负载均衡配置命令 \-- slow-online**

------------------------------------------------------------------------

**[slow-online**]命令用来在实服务组中开启实服务器温暖上线功能。

**[undo** **slow-online**]命令用来在实服务组中关闭实服务器温暖上线功能。

【命令】

**[slow-online** \**[standby-time** *standby-time* **ramp-up-time** *ramp-up-time* ]]

**[undo** **slow-online**]

【缺省情况】

实服务组中的实服务器温暖上线功能处于关闭状态。

【视图】

实服务组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[standby-time** *standby-time*]：准备时间，取值范围为0～600，单位为秒，缺省为5秒。

**[ramp-up-time** *ramp-up-time*]：爬升时间，取值范围为3～600，单位为秒，缺省为5秒。

【使用指导】

当向实服务组中添加实服务器时，某些新增的实服务器无法立即承担大量业务，此时可以开启温暖上线功能。这样，当实服务器上线后，在准备时间内，负载均衡设备不会向其分配任何业务；准备时间超时后，负载均衡设备在爬升时间内会逐步增加向其分配的业务量；爬升时间超时后，负载均衡设备开始向其正常分配业务。

【举例】

\# 在实服务组sf中开启实服务器温暖上线功能。

\<Sysname\> system-view

Sysname server-farm sf

Sysname-sfarm-sf slow-online

**负载均衡 \-- 负载均衡配置命令 \-- slow-shutdown enable**

------------------------------------------------------------------------

**[slow-shutdown** **enable**]命令用来开启实服务器的慢宕功能。

**[undo** **slow-****shutdown** **enable**]命令用来关闭实服务器的慢宕功能。

【命令】

**[slow-shutdown** **enable**]

**[undo** **slow-shutdown** **enable**]

【缺省情况】

实服务器的慢宕功能处于关闭状态。

【视图】

实服务器视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

通过**shutdown**命令可以立即中断实服务器的已有连接，而慢宕则不会立即中断实服务器的已有连接，而是让其自然老化，并且不再建立新的连接。

本命令需要与**shutdown**命令配合使用，即在开启了慢宕功能之后再关闭实服务器，该实服务器才会开始慢宕。

需要注意的是，本命令不会对之前执行的**shutdown**命令生效。比如：开启慢宕功能并关闭实服务器之后，如果再关闭慢宕功能，则该实服务器将保持慢宕状态，而不会立即中断已有连接。

【举例】

\# 开启实服务器rs的慢宕功能。

\<Sysname\> system-view

Sysname real-server rs

Sysname-rserver-rs slow-shutdown enable

【相关命令】

·**shutdown**

**负载均衡 \-- 负载均衡配置命令 \-- snat-pool**

------------------------------------------------------------------------

**[snat-pool**]命令用来指定实服务组引用的SNAT地址池。

**[undo** **snat-pool**]命令用来恢复缺省情况。

【命令】

**[snat-pool** *pool-name*]

**[undo** **snat-pool**]

【缺省情况】

实服务组没有引用任何SNAT地址池。

【视图】

实服务组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[pool-name*]：SNAT地址池的名称，为1～63个字符的字符串，不区分大小写。

【使用指导】

SNAT地址池是一个地址范围，它被实服务组引用之后，负载均衡设备将把收到报文的源地址修改为SNAT地址池中的地址后再转发出去。

【举例】

\# 指定实服务组sf引用的SNAT地址池为lbsp。

\<Sysname\> system-view

Sysname server-farm sf

Sysname-sfarm-sf snat-pool lbsp

**负载均衡 \-- 负载均衡配置命令 \-- snmp-agent trap enable loadbalance**

------------------------------------------------------------------------

**[snmp-agent** **trap** **enable** **loadbalance**]命令用来开启负载均衡的告警功能。

**[undo** **snmp-agent** **trap** **enable** **loadbalance**]命令用来关闭负载均衡的告警功能。

【命令】

**[snmp-agent** **trap** **enable** **loadbalance**]

**[undo** **snmp-agent** **trap** **enable** **loadbalance**]

【缺省情况】

负载均衡的告警功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启了负载均衡的告警功能之后，负载均衡会生成告警信息，以向网管软件报告本模块的重要事件。该信息将发送至SNMP模块，通过设置SNMP中告警信息的发送参数，来决定告警信息输出的相关属性。有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"SNMP"。

【举例】

\# 关闭负载均衡的告警功能。

\<Sysname\> system-view

Sysname undo snmp-agent trap enable loadbalance

**负载均衡 \-- 负载均衡配置命令 \-- ssl session-id**

------------------------------------------------------------------------

**[ssl** **session-id**]命令用来配置SSL持续性方法为基于SSL会话ID。

**[undo** **ssl** **session-id**]命令用来恢复缺省情况。

【命令】

**[ssl** **session-id**]

**[undo** **ssl** **session-id**]

【缺省情况】

不存在任何持续性方法。

【视图】

持续性组视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本命令只在SSL类型的持续性组视图下支持。

基于SSL会话ID的SSL持续性方法对HTTPS请求报文有效，并且需要指定虚服务器引用的SSL服务器端策略。

【举例】

\# 在SSL类型的持续性组sg6中，指定SSL的持续性方法为基于SSL会话ID。

\<Sysname\> system-view

Sysname sticky-group sg6 type ssl

Sysname-sticky-ssl-sg6 ssl session-id

**负载均衡 \-- 负载均衡配置命令 \-- ssl url rewrite**

------------------------------------------------------------------------

**[ssl** **url** **rewrite**]命令用来重写服务器发送的HTTP应答报文Location首部的URL。

**[undo**]**ssl** **url** **rewrite**命令用来取消该配置。

【命令】

**[ssl**] **url** **rewrite** **location** *location* [ **clearport** *clear-port*   **sslport** *ssl-port* ]

**[undo**]**ssl** **url** **rewrite** **location** *location* [ **clearport** *clear-port* ]

【缺省情况】

不重写服务器发送的HTTP应答报文Location首部的URL。

【视图】

负载均衡动作视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[location**] *location*：Location首部URL的正则表达式，为1～255个字符的字符串。

**[clearport**] *clear-port*：原HTTP端口号，取值范围为1～65535，缺省值为80。

**[sslport**] *ssl-port*：重写后的SSL端口号，取值范围为1～65535，缺省值为443。

【使用指导】

本命令只在HTTP类型的负载均衡动作视图下支持。

配置了本命令后，如果HTTP应答报文Location首部匹配了指定的*location*和*clear-port*，系统会将Location首部的URL由HTTP重写为HTTPS，并将*clear-port*重写为*ssl-port*。

【举例】

\# 在HTTP类型的负载均衡动作lba2中，将服务器发送的HTTP应答报文Location首部的URL，由http://www.ss.com:8080(http://www.ss.com:8080)重写为https://www.ss.com:443(https://www.ss.com:443)。

\<Sysname\> system-view

Sysname loadbalance action lba2 type http

Sysname-lba-http-lba2 ssl url rewrite www.ss.com clearport 8080 sslport 443

**负载均衡 \-- 负载均衡配置命令 \-- ssl-client-policy (LB action view)**

------------------------------------------------------------------------

**[ssl-client-policy**]命令用来引用SSL客户端策略，以便对负载均衡设备（作为SSL客户端）与SSL服务器之间传输的流量进行加密传输。

**[undo** **ssl-client-policy**]命令用来恢复缺省情况。

【命令】

**[ssl-client-policy** *policy-name*]

**[undo** **ssl-client-policy** *policy-name*]

【缺省情况】

没有引用任何SSL客户端策略。

【视图】

负载均衡动作视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：SSL客户端策略的名称，为1～31个字符的字符串，不区分大小写。

【使用指导】

本命令只在HTTP类型的负载均衡动作视图下支持。

需要注意的是，快速HTTP类型的虚服务器不支持本功能。

【举例】

\# 在HTTP类型的负载均衡动作lba2中，引用SSL客户端策略scp。

\<Sysname\> system-view

Sysname loadbalance action lba2 type http

Sysname-lba-http-lba2 ssl-client-policy scp

**负载均衡 \-- 负载均衡配置命令 \-- ssl-client-policy (virtual server view)**

------------------------------------------------------------------------

**[ssl-client-policy**]命令用来指定虚服务器引用的SSL客户端策略，以便对负载均衡设备（作为SSL客户端）与SSL服务器之间传输的流量进行加密传输。

**[undo** **ssl-client-policy**]命令用来恢复缺省情况。

【命令】

**[ssl-client-policy** *policy-name*]

**[undo** **ssl-client-policy** *policy-name*]

【缺省情况】

虚服务器没有引用任何SSL客户端策略。

【视图】

虚服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：SSL客户端策略的名称，为1～31个字符的字符串，不区分大小写。

【使用指导】

本命令只在HTTP类型的虚服务器视图下支持。

需要注意的是，快速HTTP类型的虚服务器不支持本功能。

【举例】

\# 在HTTP类型的虚服务器vs2上，引用SSL客户端策略scp。

\<Sysname\> system-view

Sysname virtual-server vs2 type http

Sysname-vs-http-vs2 ssl-client-policy scp

**负载均衡 \-- 负载均衡配置命令 \-- ssl-server-policy**

------------------------------------------------------------------------

**[ssl-server-policy**]命令用来指定虚服务器引用的SSL服务器端策略，以便对负载均衡设备（作为SSL服务器）与SSL客户端之间传输的流量进行加密传输。

**[undo** **ssl-server-policy**]命令用来恢复缺省情况。

【命令】

**[ssl-server-policy** *policy-name*]

**[undo** **ssl-server-policy**]

【缺省情况】

虚服务器没有引用任何SSL服务器端策略。

【视图】

虚服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[name*]：SSL服务器端策略的名称，为1～31个字符的字符串，不区分大小写。

【使用指导】

本命令只在HTTP类型的虚服务器视图下支持。

需要注意的是，快速HTTP类型的虚服务器不支持本功能。

【举例】

\# 在HTTP类型的虚服务器vs2上，引用SSL服务器端策略ssp。

\<Sysname\> system-view

Sysname virtual-server vs2 type http

Sysname-vs-http-vs2 ssl-server-policy ssp

**负载均衡 \-- 负载均衡配置命令 \-- sticky-group**

------------------------------------------------------------------------

**[sticky-group**]命令用来创建持续性组，并进入持续性组视图。

**[undo** **sticky-group**]命令用来删除指定的持续性组。

【命令】

**[sticky-group**[ *group-name* [ **type** { **address-port** \| **http-content** \| **http-cookie** \| **http-header** \| **payload** \| **ssl** } ]]]

**[undo** **sticky-group** *group-name*]

【缺省情况】

不存在任何持续性组。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-name*]：持续性组的名称，为1～63个字符的字符串，不区分大小写。

**[type**[ { **address-port** \| **http-content** \| **http-cookie** \| **http-header** \| **payload** \| **ssl** }]]：持续性组的类型，包括地址端口、HTTP实体、HTTP Cookie、HTTP首部、HTTP载荷和SSL六种类型。创建持续性组时必须指定本参数；而在进入已创建的持续性组视图时可以不指定本参数，但若要指定本参数，则必须与创建时的类型一致。

【使用指导】

持续性组的作用是根据某种持续性方法将具有一定相关性的会话都分配给同一个实服务器处理。在一个会话中，当其首包通过持续性方法选择了实服务器之后，后续包都会沿用这个选择结果。

【举例】

\# 创建地址端口类型的持续性组sg1，并进入其视图。

\<Sysname\> system-view

Sysname sticky-group sg1 type address-port

Sysname-sticky-address-port-sg1

**负载均衡 \-- 负载均衡配置命令 \-- sticky-sync enable**

------------------------------------------------------------------------

![说明](负载均衡命令.files/image002.png)

集中式设备不支持本命令，请以设备的实际情况为准。

****

**[sticky-sync** **enable**]命令用来开启虚服务器的持续性表项备份功能。

**[undo****sticky-sync** **enable**]命令用来关闭虚服务器的持续性表项备份功能。

【命令】

**[sticky-sync** **enable**]

**[undo****sticky-sync** **enable**]

【缺省情况】

虚服务器的持续性表项备份功能处于关闭状态。

【视图】

虚服务器视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 开启IP类型的虚服务器vs3的持续性表项备份。

\<Sysname\>system-view

Sysname virtual-server vs3 type ip

Sysname-vs-ip-vs3 sticky-sync enable

**负载均衡 \-- 负载均衡配置命令 \-- success-criteria (real server view)**

------------------------------------------------------------------------

**[success-criteria**]命令用来配置实服务器健康检测的成功条件。

**[undo** **success-criteria**]命令用来恢复缺省情况。

【命令】

**[success-criteria**[ { **all** \| **at-least** *min-number* }]]

**[undo** **success-criteria**]

【缺省情况】

只有全部方法都通过检测才认为健康检测成功。

【视图】

实服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：只有全部方法都通过检测才认为健康检测成功。

**[at-least** *min-number*]：健康检测成功所需通过检测的最少方法数，取值范围为1～4294967295。

【使用指导】

需要注意的是：

·当用户指定的最少方法数大于设备上实际存在的方法数量时，系统也将认为健康检测成功。

·用户既可在实服务组视图下对组内的所有实服务器进行配置，也可在实服务器视图下只对当前实服务器进行配置，后者的配置优先级较高。

【举例】

\# 配置实服务器rs的健康检测成功所需通过检测的最少方法数为2个。

\<Sysname\> system-view

Sysname real-server rs

Sysname-rserver-rs success-criteria at-least 2{.TerminalDisplayChar}

**负载均衡 \-- 负载均衡配置命令 \-- success-criteria (server farm view)**

------------------------------------------------------------------------

**[success-criteria**]命令用来配置实服务组健康检测的成功条件。

**[undo** **success-criteria**]命令用来恢复缺省情况。

【命令】

**[success-criteria**[ { **all** \| **at-least** *min-number* }]]

**[undo** **success-criteria**]

【缺省情况】

只有全部方法都通过检测才认为健康检测成功。

【视图】

实服务组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：只有全部方法都通过检测才认为健康检测成功。

**[at-least** *min-number*]：健康检测成功所需通过检测的最少方法数，取值范围为1～4294967295。

【使用指导】

需要注意的是：

·当用户指定的最少方法数大于设备上实际存在的方法数量时，系统也将认为健康检测成功。

·用户既可在实服务组视图下对组内的所有实服务器进行配置，也可在实服务器视图下只对当前实服务器进行配置，后者的配置优先级较高。

【举例】

\# 配置实服务组sf的健康检测成功所需通过检测的最少方法数为2个。

\<Sysname\> system-view

Sysname server-farm sf

Sysname-sfarm-sf success-criteria at-least 2

**负载均衡 \-- 负载均衡配置命令 \-- tcp window-size**

------------------------------------------------------------------------

**[tcp** **window-size**]命令用来配置TCP连接中的本地最大窗口值。

**[undo** **tcp** **window-size**]命令用来恢复缺省情况。

【命令】

**[tcp** **window-size** *size*]

**[undo** **tcp** **window-size**]

【缺省情况】

TCP连接中的本地最大窗口值为65535。

【视图】

参数模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size*]：窗口值，取值范围为8192～65535。

【使用指导】

本命令只在TCP类型的参数模板视图下支持。

【举例】

\# 在TCP类型的参数模板pp3中，配置TCP连接中的本地最大窗口值为8192。

\<Sysname\> system-view

Sysname parameter-profile pp3 type tcp

Sysname-para-tcp-pp3 tcp window-size 8192

**负载均衡 \-- 负载均衡配置命令 \-- timeout**

------------------------------------------------------------------------

**[timeout**]命令用来配置持续性表项的超时时间。

**[undo** **timeout**]命令用来恢复缺省情况。

【命令】

**[timeout** *timeout-value*]

**[undo** **timeout**]

【缺省情况】

对于HTTP Cookie类型的持续性组，持续性表项的超时时间为86400秒；对于其它类型的持续性组，持续性表项的超时时间为60秒。

【视图】

持续性组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[timeout-value*]：超时时间。对于HTTP Cookie类型的持续性组，取值范围为0～31536000，单位为秒；对于其它类型的持续性组，取值范围为10～604800，单位为秒。对于HTTP Cookie类型的持续性组，当其持续性方法为Cookie插入或Cookie重写时，0表示该持续性为会话持续性；当其持续性方法为Cookie截取时，0表示此持续性表项的超时时间为0秒。

【举例】

\# 在地址端口类型的持续性组sg1中，配置持续性表项的超时时间为100秒。

\<Sysname\> system-view

Sysname sticky-group sg1 type address-port

Sysname-sticky-address-port-sg1 timeout 100

**负载均衡 \-- 负载均衡配置命令 \-- transparent enable**

------------------------------------------------------------------------

**[transparent** **enable**]命令用来在实服务组中关闭NAT功能。

**[undo** **transparent** **enable**]命令用来在实服务组中开启NAT功能。

【命令】

**[transparent** **enable**]

**[undo** **transparent** **enable**]

【缺省情况】

实服务组中的NAT功能处于开启状态。

【视图】

实服务组视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

需要注意的是，实服务组被快速HTTP或HTTP类型的虚服务器引用时，即使关闭了NAT功能也将仍按照NAT模式处理。

【举例】

\# 在实服务组sf中关闭NAT功能。

\<Sysname\> system-view

Sysname server-farm sf

Sysname-sfarm-sf transparent enable

**负载均衡 \-- 负载均衡配置命令 \-- udp per-packet**

------------------------------------------------------------------------

**[udp** **per-packet**]命令用来开启虚服务器的UDP强制负载均衡功能。

**[undo** **udp** **per-packet**]命令用来关闭虚服务器的UDP强制负载均衡功能。

【命令】

**[udp** **per-packet**]

**[undo** **udp** **per-packet**]

【缺省情况】

虚服务器的UDP强制负载均衡功能处于关闭状态。

【视图】

虚服务器视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本命令只在UDP类型的虚服务器视图下支持。

当UDP强制负载均衡功能关闭时，匹配虚服务器的流量按照数据流来进行负载均衡，即一个应用的流量会被负载均衡到同一个实服务器上；而当UDP强制负载均衡功能开启后，匹配虚服务器的流量不再按照流来进行负载均衡，而是按照每报文来进行负载均衡。

需要注意的是：

·UDP强制负载均衡功能开启后，虚服务器以及实服务器上与连接数相关的数据将不会被统计。

·UDP强制负载均衡功能开启后，如果引用的实服务组未开启NAT功能，虚服务器以及实服务器上的发出的报文数量将不会被统计。

·UDP强制负载均衡功能开启后，以下配置项仍将生效：虚服务器所引用实服务组上配置的调度算法、虚服务器引用实服务组时所配置的持续性组中的持续性方法。例如，实服务组的调度算法为哈希算法或者持续性方法为源IP地址持续性时，由于同一会话的五元组相同，哈希计算结果和持续性表项匹配结果都是相同的实服务器，因此属于同一会话的UDP报文仍将被送至同一个实服务器进行处理，而无法按照每报文进行负载均衡。

【举例】

\# 开启UDP类型的虚服务器vs5的UDP强制负载均衡功能。

\<Sysname\> system-view

Sysname virtual-server vs5 type udp

Sysname-vs-udp-vs5 udp per-packet

**负载均衡 \-- 负载均衡配置命令 \-- virtual ip address**

------------------------------------------------------------------------

**[virtual** **ip** **address**]命令用来配置虚服务器的IPv4地址（即VSIP）。

**[undo** **virtual** **ip** **address**]命令用来恢复缺省情况。

【命令】

**[virtual**[ **ip** **address** *ipv4-address* [ *mask-length* \| *mask* ]]]

**[undo** **virtual** **ip** **address**]

【缺省情况】

虚服务器没有IPv4地址。

【视图】

虚服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv4-address*]：IPv4地址，不能为环回地址、组播地址、广播地址和0.X.X.X（如果掩码长度不是32，则可以配置0.X.X.X）。

*[mask-lengh*]：子网掩码长度，取值范围为0～32，缺省值为32。本参数在快速HTTP和HTTP类型的虚服务器视图下不支持。

*[mask*]：子网掩码，缺省值为255.255.255.255。本参数在快速HTTP和HTTP类型的虚服务器视图下不支持。

【举例】

\# 配置IP类型的虚服务器vs3的IP地址为1.1.1.1/24。

\<Sysname\> system-view

Sysname virtual-server vs3 type ip

Sysname-vs-ip-vs3 virtual ip address 1.1.1.1 24

**负载均衡 \-- 负载均衡配置命令 \-- virtual ipv6 address**

------------------------------------------------------------------------

**[virtual** **ipv6** **address**]命令用来配置虚服务器的IPv6地址（即VSIP）。

**[undo** **virtual** **ipv6** **address**]命令用来恢复缺省情况。

【命令】

**[virtual** **ipv6** **address** *ipv6-address* [ *prefix-length* ]]

**[undo** **virtual** **ipv6** **address**]

【缺省情况】

虚服务器没有IPv6地址。

【视图】

虚服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：IPv6地址，不能为环回地址、IPv6组播地址、链路本地地址和全0地址（如果前缀长度为0，则可以配置全0地址）。

*[prefix-length*]：前缀长度，取值范围为0～128，缺省值为128。本参数在快速HTTP和HTTP类型的虚服务器视图下不支持。

【举例】

\# 配置IP类型的虚服务器vs3的IPv6地址为1001::1/64。

\<Sysname\> system-view

Sysname virtual-server vs3 type ip

Sysname-vs-ip-vs3 virtual ipv6 address 1001::1 64

**负载均衡 \-- 负载均衡配置命令 \-- virtual-server**

------------------------------------------------------------------------

**[virtual-server**]命令用来创建虚服务器，并进入虚服务器视图。

**[undo** **virtual-server**]命令用来删除指定的虚服务器。

【命令】

**[virtual-server**[ *vritual-server-name* [ **type** { **fast-http** \| **http** \| **ip** \| **tcp** \| **udp** } ]]]

**[undo** **virtual-server** *vritual-server-name*]

【缺省情况】

不存在任何虚服务器。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vritual-server-name*]：虚服务器的名称，为1～63个字符的字符串，不区分大小写。

**[type**[ { **fast-http** \| **http** \| **ip** \| **tcp** \| **udp** }]]：虚服务器的类型，包括快速HTTP、HTTP、IP、TCP和UDP五种类型。创建虚服务器时必须指定本参数；而在进入已创建的虚服务器视图时可以不指定本参数，但若要指定本参数，则必须与创建时的类型一致。

【举例】

\# 创建IP类型的虚服务器vs3，并进入虚服务器视图。

\<Sysname\> system-view

Sysname virtual-server vs3 type ip

Sysname-vs-ip-vs3

**负载均衡 \-- 负载均衡配置命令 \-- vpn-instance**

------------------------------------------------------------------------

**[vpn-instance**]命令用来指定虚服务器所属的VPN。

**[undo** **vpn-instance**]命令来恢复缺省情况。

【命令】

**[vpn-instance** *vpn-instance-name*]

**[undo** **vpn-instance**]

【缺省情况】

虚服务器属于公网。

【视图】

虚服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vpn-instance-name*]：MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。

【举例】

\# 指定IP类型的虚服务器vs3所属的VPN为vpn1。

\<Sysname\>system-view

Sysname virtual-server vs3 type ip

Sysname-vs-ip-vs3 vpn-instance vpn1

**负载均衡 \-- 负载均衡配置命令 \-- weight**

------------------------------------------------------------------------

**[weight**]命令用来配置实服务器的权值，即加权轮转和加权最小连接这两种调度算法所使用的权值。

**[undo** **weight**]命令用来恢复缺省情况。

【命令】

**[weight** *weight-value*]

**[undo** **weight**]

【缺省情况】

实服务器的权值为100。

【视图】

实服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[weight-value*]：权值，取值范围为1～255。在加权轮转和加权最小连接调度时，该数值越大，实服务器越被优先调用。

【举例】

\# 配置实服务器rs的权值为150。

\<Sysname\> system-view

Sysname real-server rs

Sysname-rserver-rs weight 150
