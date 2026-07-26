
**CWMP \-- CWMP配置命令 \-- cwmp**

------------------------------------------------------------------------

**[cwmp**]命令用来进入CWMP视图。

【命令】

**[cwmp**]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 进入CWMP视图。

\<Sysname\> system-view

Sysname cwmp

【相关命令】

·**cwmp enable**

**CWMP \-- CWMP配置命令 \-- cwmp acs default password**

------------------------------------------------------------------------

**[cwmp acs default password**]命令用来配置CPE连接到ACS的缺省密码。

**[undo cwmp acs default password**]命令用来恢复缺省情况。

【命令】

**[cwmp acs default password ** { **cipher** \| **simple** }] *password*

**[undo cwmp acs default password**]

【缺省情况】

未配置CPE连接到ACS的缺省密码。

【视图】

CWMP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cipher**]：表示以密文方式设置CPE连接到ACS的缺省密码，并以密文形式保存到配置文件。

**[simple**]：表示以明文方式设置CPE连接到ACS的缺省密码，并以密文方式保存到配置文件。

*[password*]：设备向ACS发送连接请求时携带的缺省密码，区分大小写。当以明文方式配置时，为1～255个字符的字符串；以密文方式配置时，为33～373个字符的字符串。

【使用指导】

·当设备和ACS的缺省URL建立CWMP连接且通过用户名和密码进行认证时，会将缺省用户名和该密码发送给ACS，以便ACS对设备的身份进行认证。ACS根据本地配置的用户名和密码验证设备是否合法，如果验证成功，则建立连接，否则，不能建立连接。

·多次使用该命令配置不同的密码时，以最新的配置为准。

·该配置为可选配置，可以只用用户名验证，但ACS和CPE上的配置必须一致。

【举例】

\# 配置CPE连接到ACS的缺省密码为newpsw。

\<Sysname\> system-view

Sysname cwmp

Sysname-cwmp cwmp acs default password simple newpsw

【相关命令】

·**cwmp acs default url**

·**cwmp acs default username**

**CWMP \-- CWMP配置命令 \-- cwmp acs default url**

------------------------------------------------------------------------

**[cwmp acs default url**]命令用来配置CPE连接到ACS的缺省URL。

**[undo cwmp acs default url**]命令用来恢复缺省情况。

【命令】

**[cwmp acs default url ***url*]

**[undo cwmp acs default url**]

【缺省情况】

未配置CPE连接到ACS的缺省URL。

【视图】

CWMP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[url*]：CPE连接到ACS的缺省URL，为8～255个字符的字符串，格式必须为：http://*host*[:*port*/*path*]或者https://*host*[:*port*/*path*]。

【使用指导】

当用户没有为ACS配置URL地址，也没有通过DHCP服务器获取到ACS的URL地址时，设备会尝试和ACS的缺省URL建立CWMP连接。

CWMP建立连接时，使用的用户名和密码必须和ACS上创建的用户名和密码一致，否则，连接建立失败。

一个CPE只能配置一个连接到ACS的URL和缺省URL。多次使用该命令配置不同的URL时，以最新的配置为准。

【举例】

\# 配置CPE连接到ACS的缺省URL为http://www.acs.com:80/acs。

\<Sysname\> system-view

Sysname cwmp

Sysname-cwmp cwmp acs default url http://www.acs.com:80/acs

【相关命令】

·**cwmp acs default password**

·**cwmp acs default username**

**CWMP \-- CWMP配置命令 \-- cwmp acs default username**

------------------------------------------------------------------------

**[cwmp acs default username**]命令用来配置CPE连接到ACS的缺省用户名。

**[undo cwmp acs default username**]命令用来恢复缺省情况。

【命令】

**[cwmp acs default username ***username*]

**[undo cwmp acs default username**]

【缺省情况】

未配置CPE连接到ACS的缺省用户名。

【视图】

CWMP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[username*]：CPE向ACS的缺省URL发送连接请求时携带的用户名，为1～255个字符的字符串，区分大小写。

【使用指导】

当CPE和ACS的缺省URL建立CWMP连接且通过用户名和密码进行认证时，会将该用户名和缺省密码发送给ACS，以便ACS对设备的身份进行认证。ACS根据本地配置的用户名和密码验证设备是否合法，如果验证成功，则建立连接，否则，不能建立连接。

多次使用该命令配置不同的用户名时，以最新的配置为准。

【举例】

\# 配置CPE连接到ACS的缺省用户名为newname。

\<Sysname\> system-view

Sysname cwmp

Sysname-cwmp cwmp acs default username newname

【相关命令】

·**cwmp acs default password**

·**cwmp acs default url**

**CWMP \-- CWMP配置命令 \-- cwmp acs password**

------------------------------------------------------------------------

**[cwmp acs password**]命令用来配置CPE连接到ACS的密码。

**[undo cwmp acs password**]命令用来恢复缺省情况。

【命令】

**[cwmp acs password** { **cipher** \| **simple** } ]*password*

**[undo cwmp acs password**]

【缺省情况】

未配置CPE连接到ACS的密码。

【视图】

CWMP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cipher**]：表示以密文方式设置CPE连接到ACS的密码，并以密文形式保存到配置文件。

**[simple**]：表示以明文方式设置CPE连接到ACS的密码，并以密文方式保存到配置文件。

*[password*]：设备向ACS的URL发送连接请求时携带的密码，区分大小写。当以明文方式配置时，为1～255个字符的字符串；以密文方式配置时，为33～373个字符的字符串。

【使用指导】

·当CPE和ACS的URL建立CWMP连接且通过用户名和密码进行认证时，CPE会将用户名和该密码发送给ACS，以便ACS对设备的身份进行认证。ACS根据本地配置的用户名和密码验证设备是否合法，如果验证成功，则建立连接，否则，不能建立连接。

·多次使用该命令配置密码时，以最新的配置为准。

·该配置为可选配置，可以只用用户名验证，但ACS和CPE上的配置必须一致。

【举例】

\# 配置CPE连接到ACS的密码为newpsw。

\<Sysname\> system-view

Sysname cwmp

Sysname-cwmp cwmp acs password simple newpsw

【相关命令】

·**cwmp acs url**

·**cwmp acs username**

**CWMP \-- CWMP配置命令 \-- cwmp acs url**

------------------------------------------------------------------------

**[cwmp acs url**]命令用来配置CPE连接到ACS的URL。

**[undo cwmp acs url**]命令用来恢复缺省情况。

【命令】

**[cwmp acs url ***url*]

**[undo cwmp acs url**]

【缺省情况】

未配置CPE连接到ACS的URL。

【视图】

CWMP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[url*]：指定CPE连接到ACS的URL，为8～255个字符的字符串，格式必须为：http://*host*[:*port*/*path*]或者https://*host*[:*port*/*path*]。

【使用指导】

配置该命令后，如果有连接需求，则设备会向该命令指定的ACS发起CWMP连接请求。

ACS有三种指定方式，按照优先级从高到底依次为：通过该命令指定，通过DHCP协议从DHCP服务器获取，通过**cwmp acs default url**命令指定。当通过优先级高的方式获取不到URL时，再尝试优先级低的方式。

一个CPE只能配置一个连接到ACS的URL和缺省URL。当多次使用该命令配置不同的URL时，以最新的配置为准。

【举例】

\# 配置CPE连接到ACS的URL为http://www.acs.com:80/acs。

\<Sysname\> system-view

Sysname cwmp

Sysname-cwmp cwmp acs url http://www.acs.com:80/acs

**CWMP \-- CWMP配置命令 \-- cwmp acs username**

------------------------------------------------------------------------

**[cwmp acs username**]命令用来配置CPE连接到ACS的用户名。

**[undo cwmp acs username**]命令用来恢复缺省情况。

【命令】

**[cwmp acs username ***username*]

**[undo cwmp acs username**]

【缺省情况】

未配置CPE连接到ACS的用户名。

【视图】

CWMP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[username*]：CPE向ACS的URL发送连接请求时携带的用户名，为1～255个字符的字符串，区分大小写。

【使用指导】

当CPE和ACS的URL建立CWMP连接且通过用户名和密码进行认证时，会将用户名和该密码发送给ACS，以便ACS对设备的身份进行认证。ACS根据本地配置的用户名和密码验证设备是否合法，如果验证成功，则建立连接，否则，不能建立连接。

当多次使用该命令配置不同的用户名时，以最新的配置为准。

【举例】

\# 配置CPE连接到ACS的用户名为newname。

\<Sysname\> system-view

Sysname cwmp

Sysname-cwmp cwmp acs username newname

【相关命令】

·**cwmp acs password**

**CWMP \-- CWMP配置命令 \-- cwmp cpe connect interface**

------------------------------------------------------------------------

**[cwmp cpe connect interface**]命令用来设置CPE上用于连接ACS的接口。

**[undo cwmp cpe connect interface**]命令用来恢复缺省情况。

【命令】

**[cwmp cpe connect interface ***interface-type interface-number*]

**[undo cwmp cpe connect interface**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

CWMP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type interface-number*]：指定CPE上用于连接ACS的接口类型和编号。

【使用指导】

CWMP连接接口指的是CPE上用于连接ACS的接口。CPE会在Inform报文中携带CWMP连接接口的IP地址，要求ACS通过此IP地址和自己建立连接；相应的，ACS会向该IP地址回复Inform响应报文。

通常情况下，系统会采用一定的机制去自动获取一个CWMP连接接口，但如果获取的CWMP连接接口不是CPE和ACS实际相连的接口时，就会导致CWMP连接建立失败。因此，在这种情况下需要手工指定CWMP连接接口。

【举例】

\# 配置CPE上与ACS连接的接口为GigabitEthernet1/0/1。

\<Sysname\> system-view

Sysname cwmp

Sysname-cwmp cwmp cpe connect interface gigabitethernet 1/0/1

**CWMP \-- CWMP配置命令 \-- cwmp cpe connect retry**

------------------------------------------------------------------------

**[cwmp cpe connect retry**]命令用来配置建立CWMP连接时，连接失败后自动重新连接的次数。

**[undo cwmp cpe connect retry**]命令用来恢复缺省情况。

【命令】

**[cwmp cpe connect retry ***times*]

**[undo cwmp cpe connect retry**]

【缺省情况】

重发次数为无限次，即设备会一直按照一定周期向ACS发送连接请求。

【视图】

CWMP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[times*]：重发次数，取值范围为0～100，0表示不重发。

【使用指导】

当CPE向ACS请求建立连接失败，或者在会话过程中连接异常中止（CPE没有收到表示会话正常结束的报文）时，设备可以自动重新发起连接。

【举例】

\# 配置建立CWMP连接时，连接失败后自动重新连接为5次。

\<Sysname\> system-view

Sysname cwmp

Sysname-cwmp cwmp cpe connect retry 5

**CWMP \-- CWMP配置命令 \-- cwmp cpe inform interval**

------------------------------------------------------------------------

**[cwmp cpe inform interval**]命令用来配置周期发送Inform报文的时间间隔。

**[undo cwmp cpe inform interval**]命令用来恢复缺省情况。

【命令】

**[cwmp cpe inform interval ***seconds*]

**[undo cwmp cpe inform interval**]

【缺省情况】

CPE周期发送Inform报文的时间间隔为600秒。

【视图】

CWMP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：周期发送Inform报文的时间间隔，取值范围为10～86400，单位为秒。

【使用指导】

CPE与ACS之间连接的建立过程需要发送Inform报文。通过设置Inform报文发送参数，可以触发CPE向ACS自动发起连接。

该命令用于设置CPE向ACS发送Inform报文的时间间隔。

只有在配置了**cwmp cpe inform interval enable **命令时，该命令才会生效。

【举例】

\# 配置CPE周期发送Inform报文的时间间隔为3600秒。

\<Sysname\> system-view

Sysname cwmp

Sysname-cwmp cwmp cpe inform interval enable

Sysname-cwmp cwmp cpe inform interval 3600

【相关命令】

·**cwmp cpe inform interval enable**

**CWMP \-- CWMP配置命令 \-- cwmp cpe inform interval enable**

------------------------------------------------------------------------

**[cwmp cpe inform interval enable**]命令用来使能CPE周期发送Inform报文功能。

**[undo cwmp cpe inform interval enable**]命令用来恢复缺省情况。

【命令】

**[cwmp cpe inform interval enable**]

**[undo cwmp cpe inform interval enable**]

【缺省情况】

CPE周期发送Inform报文功能处于关闭状态。

【视图】

CWMP视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

使能CPE周期发送Inform报文功能，当设定的周期达到时，CPE会自动发送Inform报文与ACS建立连接。

【举例】

\# 使能CPE周期发送Inform报文功能。

\<Sysname\> system-view

Sysname cwmp

Sysname-cwmp cwmp cpe inform interval enable

【相关命令】

·**cwmp cpe inform interval**

**CWMP \-- CWMP配置命令 \-- cwmp cpe inform time**

------------------------------------------------------------------------

**[cwmp cpe inform time**]命令用来配置CPE在指定时刻发送一次Inform报文。

**[undo cwmp cpe inform time**]命令用来恢复缺省情况。

【命令】

**[cwmp cpe inform time ***time*]

**[undo cwmp cpe inform time**]

【缺省情况】

没有配置CPE定时发送Inform报文的时间。

【视图】

CWMP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：指定CPE发送一次Inform报文的日期和时间，格式为：*yyyy*-*mm*-*dd*T*hh*:*mm*:*ss*，取值范围为1970-01-01T00:00:00～2035-12-31T23:59:59，该时间必须大于系统当前时间。

【使用指导】

CPE与ACS之间连接的建立过程需要发送Inform报文。通过设置Inform报文发送参数，可以触发CPE向ACS自动发起连接。

【举例】

\# 配置CPE发送Inform报文的日期和时间为2012-12-01T20:00:00。

\<Sysname\> system-view

Sysname cwmp

Sysname-cwmp cwmp cpe inform time 2012-12-01T20:00:00

**CWMP \-- CWMP配置命令 \-- cwmp cpe password**

------------------------------------------------------------------------

**[cwmp cpe password**]命令用来配置ACS连接到CPE时的认证密码。

**[undo cwmp cpe password**]命令用来恢复缺省情况。

【命令】

**[cwmp cpe password** { **cipher** \| **simple** } ]*password*

**[undo cwmp cpe password**]

【缺省情况】

未配置ACS连接到CPE的密码。

【视图】

CWMP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cipher**]：表示以密文方式设置连接到CPE的密码，并以密文形式保存到配置文件。

**[simple**]：表示以明文方式设置连接到CPE的密码，并以密文方式保存到配置文件。

*[password*]：ACS请求连接到CPE时用来认证的密码，区分大小写。当以明文方式配置时，为1～255个字符的字符串；以密文方式配置时，为33～373个字符的字符串。

【使用指导】

·当ACS与CPE建立CWMP连接且通过用户名和密码进行认证时，ACS会将用户名和密码发送给CPE，以便设备对ACS的身份进行认证。设备根据本地配置的用户名和该密码验证ACS是否合法，如果验证成功，则建立连接，否则，不能建立连接。

·多次使用该命令配置不同的密码时，以最新的配置为准。

·该配置为可选配置，可以只用用户名验证，但ACS和CPE上的配置必须一致。

【举例】

\# 配置ACS连接到CPE密码为newpsw。

\<Sysname\> system-view

Sysname cwmp

Sysname-cwmp cwmp cpe password simple newpsw

【相关命令】

·**cwmp cpe username**

**CWMP \-- CWMP配置命令 \-- cwmp cpe provision-code**

------------------------------------------------------------------------

**[cwmp cpe provision-code**]命令用来配置CPE的业务代码。

**[undo cwmp cpe provision-code**]命令用来恢复缺省情况。

【命令】

**[cwmp cpe provision-code ***provision-code*]

**[undo cwmp cpe provision-code**]

【缺省情况】

CPE向ACS发送的Inform报文中携带的业务代码为"PROVISIONCODE"。

【视图】

CWMP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[provision-code*]：设备向ACS发送Inform报文中携带的设备代码。为1～64个字符的字符串，必须为大写字母、数字或者"."。

【使用指导】

当CPE与ACS之间建立连接时，CPE需要在Inform报文中携带provision-code信息，ACS根据此信息可以识别设备定制的业务以及相应的参数，以便更好地管理CPE设备。

多次使用该命令配置设备代码时，以最新的配置为准。

【举例】

\# 配置CPE的业务代码为H3C20130525。

\<Sysname\> system

Sysname cwmp

Sysname-cwmp cwmp cpe provision-code H3C20130525

**CWMP \-- CWMP配置命令 \-- cwmp cpe stun enable**

------------------------------------------------------------------------

**[cwmp cpe stun enable**]命令用来使能CPE的NAT穿越功能。

**[undo cwmp cpe stun enable**]命令用来恢复缺省情况。

【命令】

**[cwmp cpe stun enable**]

**[undo cwmp cpe stun enable**]

【缺省情况】

CPE的NAT穿越功能处于关闭状态。

【视图】

CWMP视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

无论CPE与ACS之间是否存在NAT网关，CPE的主动连接请求都能到达ACS。而当CPE与ACS之间存在NAT网关时，ACS主动发起的连接请求不能到达CPE。此时，可以在设备上开启NAT穿越功能，使得ACS的请求能够穿越网关。本特性的实现遵循RFC 3489定义的STUN（Simple Traversal of User Datagram Protocol (UDP) Through Network Address Translators (NATs)，NAT的UDP简单穿越）。

·CPE在主动给ACS发连接请求的过程中，如果发现与ACS之间存在NAT网关，则会将获取到的经NAT绑定的公网的IP地址和端口号发送给ACS。

·为了保证ACS任意时刻主动发起的连接请求能够穿越NAT网关到达CPE，CPE必须维持NAT网关上的地址映射关系。

有关NAT的详细描述，请参见"三层技术-IP业务配置指导"中的"NAT"。

【举例】

\# 使能CPE的NAT穿越功能。

\<Sysname\> system-view

Sysname cwmp

Sysname-cwmp cwmp cpe stun enable

**CWMP \-- CWMP配置命令 \-- cwmp cpe username**

------------------------------------------------------------------------

**[cwmp cpe username**]命令用来配置ACS连接到CPE时的认证用户名。

**[undo cwmp cpe username**]命令用来恢复缺省情况。

【命令】

**[cwmp cpe username ***username*]

**[undo cwmp cpe username**]

【缺省情况】

未配置ACS连接到CPE的用户名。

【视图】

CWMP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[username*]：ACS请求连接到CPE时的认证用户名，为1～255个字符的字符串，区分大小写。

【使用指导】

当ACS向CPE发送连接请求且通过用户名和密码认证时，ACS会将用户名和密码发送给设备，以便设备对ACS的身份进行认证。设备根据本地配置的用户名和该密码验证ACS是否合法，如果验证成功，则建立连接，否则，不能建立连接。

多次使用该命令配置用户名时，以最新的配置为准。

【举例】

\# 配置ACS连接到CPE的用户名为newname。

\<Sysname\> system-view

Sysname cwmp

Sysname-cwmp cwmp cpe username newname

【相关命令】

·**cwmp cpe password**

**CWMP \-- CWMP配置命令 \-- cwmp cpe wait timeout**

------------------------------------------------------------------------

**[cwmp cpe wait timeout**]命令用来配置CPE无数据传输超时时间。

**[undo cwmp cpe wait timeout**]命令用来恢复缺省情况。

【命令】

**[cwmp cpe wait timeout ***seconds*]

**[undo cwmp cpe wait timeout**]

【缺省情况】

无数据传输超时时间为30秒。

【视图】

CWMP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：无数据传输超时时间，取值范围为30～1800，单位为秒。

【使用指导】

CWMP连接建立后，如果CPE与ACS在无数据传输超时时间内一直没有报文的交互，CPE将认为连接失效，并断开连接。

【举例】

\# 配置CPE无数据传输超时时间为60秒。

\<Sysname\> system-view

Sysname cwmp

Sysname-cwmp cwmp cpe wait timeout 60

**CWMP \-- CWMP配置命令 \-- cwmp enable**

------------------------------------------------------------------------

**[cwmp enable**]命令用来使能CWMP功能。

**[undo cwmp enable**]命令用来关闭CWMP功能。

【命令】

**[cwmp enable**]

**[undo cwmp enable**]

【缺省情况】

CWMP功能处于关闭状态。

【视图】

CWMP视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

使能CWMP后，CWMP的其它配置才能生效。

【举例】

\# 使能CWMP功能。

\<Sysname\> system-view

Sysname cwmp

Sysname-cwmp cwmp enable

【相关命令】

·**cwmp**

**CWMP \-- CWMP配置命令 \-- display cwmp configuration**

------------------------------------------------------------------------

**[display cwmp configuration**]命令用来显示CWMP的当前配置信息。

【命令】

**[display cwmp configuration**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# CWMP使能，显示CWMP的配置信息。

\<sysname\> display cwmp configuration

CWMP state                          : Enabled

ACS URL                             : http://www.acs.com:80/acs

ACS username                        : newname

ACS default URL                     : Null

ACS default username                : defname

Periodic inform                     : Disabled

Inform interval                     : 600s

Inform time                         : None

Wait timeout                        : 30s

Connection retries                  : Unlimited

Source IP interface                 : None

STUN state                          : Disabled

SSL policy name                     : Null

表1-1 display cwmp configuration命令显示信息描述表

字段

描述

CWMP state

CWMP的使能状态：

·Enabled：表示已使能

·Disabled：表示未使能

ACS default URL

CPE连接到ACS的缺省URL，没有配置时显示为Null

ACS default username

CPE连接到ACS的缺省用户名，没有配置时显示为空

ACS URL

CPE连接到ACS的URL，没有配置时显示为Null

ACS username

CPE连接到ACS的用户名，没有配置时显示为空

Periodic inform

周期发送Inform报文的使能情况：

·Enabled：表示已使能

·Disabled：表示未使能

Inform interval

发送Inform报文的周期，没有配置时显示为None

Inform time

定期发送Inform报文的日期和时间，没有配置时显示为None

Wait timeout

无数据传输超时的时间

Connection retries

CWMP连接失败后自动重新连接的次数，没有配置时显示为Unlimited

Source IP interface

CPE上用于连接ACS的接口

STUN state

NAT穿越功能的使能状态：

·Enabled：表示已使能

·Disabled：表示未使能

SSL policy name

连接ACS采用的SSL策略名，没有配置时显示为Null

【相关命令】

·**display cwmp status**

**CWMP \-- CWMP配置命令 \-- display cwmp status**

------------------------------------------------------------------------

**[display cwmp status**]命令用来显示CWMP的当前状态信息。

【命令】

**[display cwmp status**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示CWMP的当前状态信息。

\<sysname\> display cwmp status

CWMP state                                    : Enabled

ACS URL of most recent connection             : http://www.acs.com:80/acs

ACS information source                        : User

ACS username of most recent connection        : newname

Connection status                             : Disconnected

Data transfer status                          : None

Most recent successful connection attempt     : None

Length of time before next connection attempt : 1096832s

表1-2 display cwmp status命令显示信息描述表

字段

描述

CWMP state

CWMP的使能状态：

·Enabled：表示已使能

·Disabled：表示未使能

ACS URL of most recent connection

最近一次CPE使用的连接到ACS的URL，没有配置时显示为Null

ACS information source

CPE获得ACS URL的方式，没有配置ACS URL时显示为None

·User：表示ACS URL为命令行配置或者ACS配置

·DHCP：表示ACS URL为DHCP下发

·Default：表示ACS URL为缺省配置

ACS username of most recent connection

最近一次CPE使用的连接到ACS的用户名，没有配置时显示为空

Connection status

CPE的连接状态，包含：

·Connected：表示连接已建立

·Disconnected：表示没有建立连接

·Waiting response：表示正在等待响应报文

Data transfer status

CPE的数据传输的状态，包含：

·Uploading：表示正在上传数据

·Downloading：表示正在下载数据

·None：表示没有数据在传输

Most recent successful connection attempt

最近一次CPE和ACS成功连接的时间，最近没有成功连接时显示为None

Length of time before next connection attempt

距离下一次发起连接的时间，单位为秒。如果目前没有发起会话需求则显示为None

【相关命令】

·**display cwmp configuration**

**CWMP \-- CWMP配置命令 \-- ssl client-policy**

------------------------------------------------------------------------

**[ssl client-policy**]命令用来配置CWMP引用的SSL客户端策略。

**[undo ssl client-policy**]命令用来删除对该SSL客户端策略的引用。

【命令】

**[ssl client-policy** *policy-name*]

**[undo ssl client-policy**]

【缺省情况】

CWMP没有引用SSL客户端策略。

【视图】

CWMP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：SSL客户端策略名，为1～31个字符的字符串，不区分大小写。

【使用指导】

CWMP是基于HTTP/HTTPS协议的，CWMP报文作为HTTP/HTTPS报文的数据部分封装在HTTP/HTTPS报文中。如果ACS的URL以http://开头，则使用HTTP协议，如果ACS的URL以https://开头，则使用HTTPS协议。

使用HTTPS协议时，为了对ACS身份进行认证，需要配置CWMP引用的SSL客户端策略。关于SSL客户端策略的详细介绍和配置请参见"安全配置指导"中的"SSL"。

【举例】

\# 设置CWMP引用的SSL客户端策略为test。

\<Sysname\> system

Sysname cwmp

Sysname-cwmp ssl client-policy test
