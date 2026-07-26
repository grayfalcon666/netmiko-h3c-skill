
**DHCP \-- DHCP公共命令 \-- dhcp client-detect**

------------------------------------------------------------------------

**[dhcp client-detect**]命令用来开启DHCP服务器或DHCP中继的下线用户探测功能。

**[undo dhcp client-detect**]命令用来恢复缺省情况。

【命令】

**[dhcp** **client-detect**]

**[undo dhcp client-detect**]

【缺省情况】

DHCP服务器或DHCP中继的用户下线检测功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

DHCP服务器开启该功能后，当设备上的ARP表项老化时，DHCP服务器认为该表项对应的DHCP客户端已经下线，DHCP服务器会删除对应的IP地址租约。

DHCP中继开启该功能后，当设备上的ARP表项老化时，DHCP中继认为该表项对应的DHCP客户端已经下线，DHCP中继会删除对应的用户地址表项，并通过发Release报文通知DHCP服务器删除下线用户的IP地址租约。

【举例】

\# 开启DHCP服务器的用户下线检测功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dhcp client-detect

**DHCP \-- DHCP公共命令 \-- dhcp dscp**

------------------------------------------------------------------------

**[dhcp dscp**]命令用来配置DHCP服务器或DHCP中继发送DHCP报文的DSCP优先级。

**[undo dhcp dscp**]命令用来恢复缺省值。

【命令】

**[dhcp dscp ***dscp-value*]

**[undo dhcp dscp**]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dscp-value*]：DHCP报文的DSCP优先级，取值范围为0～63，缺省值为56。

【使用指导】

DSCP优先级用来体现报文自身的优先等级，决定报文传输的优先程度。配置的DSCP优先级的取值越大，报文的优先级越高。通过本命令可以指定DHCP服务器或DHCP中继发送的DHCP报文中携带的DSCP优先级的取值。

【举例】

\# 配置DHCP服务器或DHCP中继发送的DHCP报文的DSCP优先级为30。

\<Sysname\> system-view

Sysname dhcp dscp 30

**DHCP \-- DHCP公共命令 \-- dhcp enable**

------------------------------------------------------------------------

dhcp enable{.commandkeywordsChar}命令用来开启DHCP服务。

undo dhcp enable{.commandkeywordsChar}命令用来禁止DHCP服务。

【命令】

dhcp enable

undo dhcp enable

【缺省情况】

DHCP服务处于禁止状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有开启DHCP服务后，其它相关的DHCP配置才能生效。

配置DHCP服务器和DHCP中继时，都需要先开启DHCP服务。

【举例】

\# 开启DHCP服务。

\<Sysname\> system-view

Sysname dhcp enable

**DHCP \-- DHCP公共命令 \-- dhcp log enable**

------------------------------------------------------------------------

**[dhcp log enable**]命令用来开启DHCP服务器日志信息功能。

**[undo dhcp log enable**]命令用来关闭DHCP服务器日志信息功能。

【命令】

**[dhcp log enable**]

**[undo dhcp log enable**]

【缺省情况】

DHCP服务器日志信息功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

DHCP服务器日志是为了满足管理员审计需求。设备生成DHCP日志信息会交给信息中心模块处理，信息中心模块的配置将决定日志信息的发送规则和发送方向。关于信息中心的详细描述请参见"网络管理和监控配置指导"中的"信息中心"。

比如大量DHCP客户端发生上下线操作时，DHCP服务器会输出大量日志信息，这可能会降低设备性能，影响DHCP服务器分配IP地址的速度。为了避免该情况的发生，用户可以关闭DHCP服务器日志信息功能，使得DHCP服务器不再输出日志信息。

【举例】

\# 开启DHCP服务器日志信息功能。

\<Sysname\> system-view

Sysname dhcp log enable

**DHCP \-- DHCP公共命令 \-- dhcp rate-limit**

------------------------------------------------------------------------

**[dhcp rate-limit**]命令用来开启DHCP报文限速功能，即限制接口接收DHCP报文的速率。

**[undo dhcp rate-limit**]命令用来恢复缺省情况。

【命令】

**[dhcp rate-limit ***rate*]

**[undo dhcp rate-limit**]

【缺省情况】

DHCP报文限速功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[rate*]：接口接收DHCP报文的最高速率，单位为Kbps。本参数的取值范围与设备的型号有关，请以设备的实际情况为准。

【使用指导】

开启DHCP报文限速功能后，当接口上收到的DHCP报文速率超过用户设定的限速值时，丢弃超过速率限制的DHCP报文。

【举例】

·路由应用

\# 开启DHCP报文限速功能，即限制接口GigabitEthernet1/0/1接收DHCP报文的速率为64Kbps。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dhcp rate-limit 64

·交换应用

\# 开启DHCP报文限速功能，即限制VLAN接口2接收DHCP报文的速率为64Kbps。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 dhcp rate-limit 64

**DHCP \-- DHCP公共命令 \-- dhcp select**

------------------------------------------------------------------------

dhcp select{.commandkeywordsChar}命令用来配置接口工作在DHCP服务器或DHCP中继模式。

undo dhcp select{.commandkeywordsChar}命令用来取消接口工作在DHCP服务器或DHCP中继模式，即接口将丢弃DHCP客户端发来的DHCP报文。

【命令】

**[dhcp select** { **relay** [ **proxy**  \| **server** }]]

**[undo dhcp select**[ { **relay** \| **server** }]]

【缺省情况】

接口工作在DHCP服务器模式，即当接口收到DHCP客户端发来的DHCP报文时，将从DHCP服务器的地址池中分配地址等参数。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

relay{.commandkeywordsChar}：配置接口工作在DHCP中继模式，即当接口收到DHCP客户端发来的DHCP报文时，将报文转发给DHCP服务器，由DHCP服务器为DHCP客户端分配地址等参数。

proxy{.commandkeywordsChar}：配置接口工作在DHCP代理模式，即当接口收到DHCP客户端发来的DHCP报文时，将报文转发给DHCP服务器，由DHCP服务器为DHCP客户端分配地址等参数。当接口收到DHCP服务器发来的应答报文后，把报文中的DHCP服务器地址修改为中继接口地址。

server{.commandkeywordsChar}：配置接口工作在DHCP服务器模式，即当接口收到DHCP客户端发来的DHCP报文时，将从DHCP服务器的地址池中分配地址等参数。

【使用指导】

DHCP服务器和DHCP客户端位于同一个网段时，DHCP客户端可以直接从DHCP服务器获取IP地址等参数；DHCP服务器和DHCP客户端位于不同网段时，需要配置DHCP中继在DHCP客户端和DHCP服务器之间转发报文。

需要注意的是，接口从DHCP服务器模式切换到DHCP中继模式时，设备不会删除IP地址绑定信息，也不会删除相应的授权ARP表项。这些表项可能会与DHCP中继新生成的ARP表项冲突。因此，建议接口从DHCP服务器模式切换到DHCP中继模式时，通过reset dhcp server ip-in-use{.commandkeywordsChar}命令清除已有的IP地址绑定信息。

【举例】

·路由应用

\# 配置接口GigabitEthernet1/0/1工作在DHCP中继模式。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dhcp select relay

·交换应用

\# 配置VLAN接口2工作在DHCP中继模式。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 dhcp select relay

【相关命令】

· reset dhcp server ip-in-use{.commandkeywordsChar}

**DHCP \-- DHCP服务器配置命令 \-- address range**

------------------------------------------------------------------------

address range{.commandkeywordsChar}命令用来配置地址池动态分配的IP地址范围。

undo address range{.commandkeywordsChar}命令用来删除地址池动态分配的IP地址范围。

【命令】

address range {.commandkeywordsChar}*start-ip-address end-ip-address*

undo address range

【缺省情况】

没有配置动态分配的IP地址范围。

【视图】

DHCP地址池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[start-ip-address*]：动态分配范围的起始IP地址。

*[end-ip-address*]：动态分配范围的结束IP地址。

【使用指导】

如果没有通过本命令配置地址池动态分配的IP地址范围，则地址池下network{.commandkeywordsChar}命令指定的网段地址都可以分配给DHCP客户端；如果通过本命令配置了地址池动态分配的IP地址范围，则只能从本命令指定的IP地址范围内选择地址分配给客户端。

需要注意的是：

·配置**address range**命令后，不能再通过**network secondary**命令在地址池中配置从网段。

·如果多次执行本命令，新的配置会覆盖已有配置。

·**address range**命令指定的地址范围应该在**network**命令指定的网段范围内，网段范围外的地址将无法被分配。

【举例】

\# 配置地址池1动态分配的地址范围为192.168.8.1到192.168.8.150。

\<Sysname\> system-view

Sysname dhcp server ip-pool 1

Sysname-dhcp-pool-1 address range 192.168.8.1 192.168.8.150

【相关命令】

·**class**

·**dhcp class**

·**display dhcp server pool**

·**network**

**DHCP \-- DHCP服务器配置命令 \-- bims-server**

------------------------------------------------------------------------

bims-server{.commandkeywordsChar}命令用来配置DHCP地址池为DHCP客户端分配的BIMS服务器IP地址、端口及共享密钥信息。

undo bims-server{.commandkeywordsChar}命令用来删除DHCP地址池为DHCP客户端分配的BIMS服务器信息。

【命令】

[[bims-server ip]{.commandkeywordsChar}* ip-address* [[ port{.commandkeywordsChar} *port-number* ] sharekey{.commandkeywordsChar} { **cipher** \| **simple** } *key*]]

undo bims-server

【缺省情况】

没有配置DHCP地址池为DHCP客户端分配的BIMS服务器信息。

【视图】

DHCP地址池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

ip{.commandkeywordsChar} *ip-address*：指定BIMS服务器的IP地址。

port{.commandkeywordsChar} *port-number*：指定BIMS服务器的端口号。*port-number*为端口号，取值范围为1～65534。

**[cipher**]：以密文形式设置密钥。

**[simple**]：以明文形式设置密钥。

*[key*]：指定BIMS服务器的共享密钥，区分大小写。*key*表示共享密钥，明文形式输入密钥时为1～16个字符的字符串，密文形式输入密钥时为1～53个字符的字符串。DHCP客户端获取到BIMS服务器的信息后，与BIMS服务器通信时，采用共享密钥对传递的消息进行加密，以保证消息传递的安全性。

【使用指导】

如果多次执行该命令，新的配置会覆盖已有配置。

以明文或密文方式设置的密钥，均以密文的方式保存在配置文件中。

【举例】

\# 配置DHCP地址池0为DHCP客户端分配的BIMS服务器的IP地址为1.1.1.1，端口号为80，共享密钥为aabbcc。

\<Sysname\> system-view

Sysname dhcp server ip-pool 0

Sysname-dhcp-pool-0 bims-server ip 1.1.1.1 port 80 sharekey simple aabbcc

【相关命令】

·**display dhcp server pool**

**DHCP \-- DHCP服务器配置命令 \-- bootfile-name**

------------------------------------------------------------------------

bootfile-name{.commandkeywordsChar}命令用来配置DHCP客户端使用的启动文件名或远程启动文件的HTTP形式URL。

undo bootfile-name{.commandkeywordsChar}命令用来删除DHCP客户端使用的启动文件名或远程启动文件的HTTP形式URL。

【命令】

[[bootfile-name]{.commandkeywordsChar}*[ { bootfile-name \| url }]*]

undo bootfile-name

【缺省情况】

没有配置DHCP客户端使用的启动文件名或远程启动文件的HTTP形式URL。

【视图】

DHCP地址池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bootfile-name*]：启动文件名，为1～63个字符的字符串，区分大小写。

*[url*]：远程启动文件的HTTP形式URL，为1～63个字符的字符串，区分大小写。

【使用指导】

如果多次执行该命令，新的配置会覆盖已有配置。

【举例】

\# 配置DHCP地址池0为DHCP客户端分配的启动文件名为boot.cfg。

\<Sysname\> system-view

Sysname dhcp server ip-pool 0

Sysname-dhcp-pool-0 bootfile-name boot.cfg

\# 配置DHCP地址池0为DHCP客户端分配的启动文件的HTTP URL为http://10.1.1.1/boot.cfg。

\<Sysname\> system-view

Sysname dhcp server ip-pool 0

Sysname-dhcp-pool-0 bootfile-name http://10.1.1.1/boot.cfg

【相关命令】

·**display dhcp server pool**

·{.commandkeywordsChar}[n]{.commandkeywordsChar}**ext-serve[r{.commandkeywordsChar}]**

·{.commandkeywordsChar}[tftp-server domain-name]{.commandkeywordsChar}

·{.commandkeywordsChar}[tftp-server ip-address]{.commandkeywordsChar}

**DHCP \-- DHCP服务器配置命令 \-- class option-group**

------------------------------------------------------------------------

**[class option-group**]命令用来配置DHCP地址池下DHCP用户类和DHCP选项组的关联。

**[undo class option-group**]命令用来删除DHCP地址池下DHCP用户类和DHCP选项组的关联。

【命令】

**[class** *class-name* **option-group** *option-group-number*]

**[undo class ***class-name***option-group**]

【缺省情况】

未配置DHCP地址池的DHCP用户类和DHCP选项组的关联。

【视图】

DHCP地址池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[class-name*]：DHCP用户类名称，为1～63个字符的字符串，不区分大小写。

*[option-group-number*]：DHCP选项组编号，取值范围为1～32768。

【使用指导】

DHCP服务器应答DHCP客户端报文时，首先根据配置顺序逐个匹配通过**class option-group**命令指定的DHCP用户类。如果匹配成功，则将该用户类对应的选项组中的选项填充到应答报文中；如果同时匹配多个DHCP用户类，且各用户类对应的选项组中有相同编号的选项，以最先匹配到DHCP用户类对应的选项组中的选项为准。

需要注意的是，对于一个DHCP用户类，在一个DHCP地址池中只能指定一个选项组。如果多次执行该命令为同一个DHCP用户类指定不同的选项组，则新的配置会覆盖已有配置。

【举例】

\# 在DHCP地址池0中，配置DHCP用户类user和DHCP选项组1的关联。

\<Sysname\> system-view

Sysname dhcp server ip-pool 0

Sysname-dhcp-pool-0 class user option-group 1

【相关命令】

·**dhcp option-group ***option-group-number*

**DHCP \-- DHCP服务器配置命令 \-- class range**

------------------------------------------------------------------------

class range{.commandkeywordsChar}命令用来配置DHCP地址池为指定DHCP用户类动态分配的IP地址范围。

undo{.commandkeywordsChar} [class range{.commandkeywordsChar}]命令用来删除为指定DHCP用户类动态分配的IP地址范围。

【命令】

class{.commandkeywordsChar} *class-name* [range{.commandkeywordsChar} *start-ip-address end-ip-address*]

undo class {.commandkeywordsChar}*class-name* **range**

【缺省情况】

没有配置为指定DHCP用户类动态分配的IP地址范围。

【视图】

DHCP地址池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[class-name*]：DHCP用户类名称，为1～63个字符的字符串，不区分大小写。

*[start-ip-address*]：动态分配范围的起始IP地址。

*[end-ip-address*]：动态分配范围的结束IP地址。

【使用指导】

DHCP服务器从地址池中选择地址分配给客户端时，首先根据配置顺序逐个匹配通过**class range**命令指定的DHCP用户类。如果匹配成功，则从为该用户类指定的地址范围内选择地址分配给DHCP客户端；如果该用户类中没有可供分配的地址，则继续匹配下一个用户类；如果所有匹配上的用户类地址范围都没有可供分配的地址，则从公共地址范围中选择地址分配给客户端；如果不匹配任何DHCP用户类，则会从地址池动态分配的IP地址范围（通过**address range**命令配置）中选择地址分配给DHCP客户端；如果**address range**命令指定的地址范围内也没有空闲地址，或者没有配置address range{.commandkeywordsChar}命令，则地址分配失败，即DHCP服务器无法为DHCP客户端分配地址。

通过本配置可以实现将一个地址池下的地址范围划分成多个地址段，分别分配给属于不同DHCP用户类的DHCP客户端。

需要注意的是：

·配置**class**** range**命令后，不能再通过network secondary{.commandkeywordsChar}命令在地址池中配置从网段。

·配置**class**** range**命令后，只能从**class range**命令或**address range**命令指定的地址范围内选择地址分配给客户端。

·一个地址池中只能为一个DHCP用户类指定一个地址范围。如果多次执行本命令为同一个DHCP用户类指定不同的地址范围，则新的配置会覆盖已有配置。

·一个地址池中可以为多个不同的DHCP用户类指定地址范围。

·如果指定的DHCP用户类不存在，则为该用户类指定的地址范围不能分配给任何DHCP客户端。

·**class range**命令指定的地址范围应该在**network**命令指定的主网段范围内，主网段范围外的地址将无法被分配。

【举例】

\# 在地址池1中配置为DHCP用户类user动态分配的地址范围为192.168.8.1到192.168.8.150。

\<Sysname\> system-view

Sysname dhcp server ip-pool 1

Sysname-dhcp-pool-1 class user range 192.168.8.1 192.168.8.150

【相关命令】

·**address range**

·**dhcp class**

· display dhcp server pool{.commandkeywordsChar}

**DHCP \-- DHCP服务器配置命令 \-- dhcp class**

------------------------------------------------------------------------

dhcp class{.commandkeywordsChar}命令用来创建DHCP用户类并进入DHCP用户类视图，如果已经创建了DHCP用户类，则直接进入该用户类视图。

undo dhcp class{.commandkeywordsChar}命令用来删除指定的用户类。

【命令】

dhcp class {.commandkeywordsChar}*class-name*

undo dhcp class{.commandkeywordsChar} *class-name*

【缺省情况】

不存在任何DHCP用户类。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[class-name*]：DHCP用户类的名称，为1～63个字符的字符串，不区分大小写。

【使用指导】

在DHCP用户类视图下，可以通过if-match{.commandkeywordsChar}命令配置DHCP用户类的匹配规则，根据匹配规则判断DHCP客户端属于的DHCP用户类，从而实现灵活的用户分类策略。

【举例】

\# 创建名称为test的DHCP用户类，并进入DHCP用户类视图。

\<Sysname\> system-view

Sysname dhcp class test

Sysname-dhcp-class-test

【相关命令】

·**address range**

·{.commandkeywordsChar}**class**

·{.commandkeywordsChar}[if-match]{.commandkeywordsChar}

**DHCP \-- DHCP服务器配置命令 \-- dhcp option-group**

------------------------------------------------------------------------

**[dhcp option-group**]命令用来创建DHCP选项组并进入DHCP选项组视图，如果已经创建了DHCP选项组，则直接进入该DHCP选项组视图。

**[undo dhcp option-group**]命令用来删除指定的DHCP选项组。

【命令】

**[dhcp option-group** *option-group-number*]

**[undo dhcp option-group ***option-group-number*]

【缺省情况】

设备上未配置DHCP选项组。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[option-group-number*]：DHCP选项组编号，取值范围为0～32768。

【举例】

\# 创建DHCP选项组1并进入该选项组视图。

\<Sysname\> system-view

Sysname dhcp option-group 1

Sysname-dhcp-option-group-1

【相关命令】

·**class** *class-name* **option-group** *option-group-number*

[·**option ***code******[ascii-string ***[\| hex]*** hex-string***[ \| ip-address ]***ip-address*&\<1-8\> }]

**DHCP \-- DHCP服务器配置命令 \-- dhcp server always-broadcast**

------------------------------------------------------------------------

dhcp server always-broadcast]{.commandkeywordsChar}命令用来开启DHCP服务器的广播回应报文功能。

undo dhcp server always-broadcast{.commandkeywordsChar}命令用来恢复缺省情况。

【命令】

dhcp server always-broadcast

undo dhcp server always-broadcast

【缺省情况】

DHCP服务器的广播回应报文功能处于关闭状态。DHCP服务器根据请求报文中的广播标志位来决定以广播还是单播的形式发送应答报文。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启DHCP服务器的广播回应报文功能后，DHCP服务器忽略请求报文中的广播标志位，以广播的形式发送应答报文。

当已经存在IP地址的客户端发出请求报文（即报文中ciaddr字段不为0)时，无论是否开启DHCP服务器的广播回应报文功能，DHCP服务器都会以单播形式将回应报文发送给DHCP客户端（即目的地址为ciaddr）。

当请求报文通过DHCP中继转发到DHCP服务器（即报文中giaddr字段不为0）时，无论是否开启DHCP服务器的广播回应报文功能，DHCP服务器都会以单播形式将回应报文发送给DHCP中继（即目的地址为giaddr）。

【举例】

\# 开启DHCP服务器的广播回应报文功能。

\<Sysname\> system-view

Sysname dhcp server always-broadcast

**DHCP \-- DHCP服务器配置命令 \-- dhcp server apply ip-pool**

------------------------------------------------------------------------

dhcp server apply ip-pool{.commandkeywordsChar}命令用来指定接口引用的地址池。

undo dhcp server apply ip-pool{.commandkeywordsChar}命令用来取消接口引用地址池。

【命令】

dhcp server apply ip-pool {.commandkeywordsChar}*pool-name*

undo dhcp server apply ip-pool

【缺省情况】

接口没有引用任何地址池。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[pool-name*]：DHCP地址池名称，为1～63个字符的字符串，不区分大小写。

【使用指导】

需要注意的是：

·接口上配置了[dhcp server apply ip-pool]{.commandkeywordsChar}命令后，如果接口引用的地址池不存在，则无法为客户端动态分配IP地址。

·如果多次执行本命令，新的配置会覆盖已有配置。

【举例】

·路由应用

\# 配置接口GigabitEthernet1/0/1引用DHCP地址池0。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dhcp server apply ip-pool 0

·交换应用

\# 配置VLAN接口2引用DHCP地址池0。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 dhcp server apply ip-pool 0

【相关命令】

·**dhcp server ip-pool**

**DHCP \-- DHCP服务器配置命令 \-- dhcp server bootp ignore**

------------------------------------------------------------------------

dhcp server bootp ignore{.commandkeywordsChar}命令用来配置DHCP服务器忽略BOOTP请求。

undo dhcp server bootp ignore{.commandkeywordsChar}命令用来恢复缺省情况。

【命令】

dhcp server bootp ignore

undo dhcp server bootp ignore

【缺省情况】

DHCP服务器不会忽略BOOTP请求。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

BOOTP客户端申请到的地址的租约是无限期的。在特殊的组网环境中，可能不希望出现无限期的地址租约。此时，可以通过配置DHCP服务器忽略BOOTP请求报文，避免分配无限期的地址租约。

【举例】

\# 配置DHCP服务器忽略BOOTP请求。

\<Sysname\> system-view

Sysname dhcp server bootp ignore

**DHCP \-- DHCP服务器配置命令 \-- dhcp server bootp reply-rfc-1048**

------------------------------------------------------------------------

dhcp server bootp reply-rfc-1048{.commandkeywordsChar}命令用来开启DHCP服务器回应RFC 1048格式报文功能。

undo dhcp server bootp reply-rfc-1048{.commandkeywordsChar}命令用来关闭DHCP服务器回应RFC 1048格式报文功能。

【命令】

dhcp server bootp reply-rfc-1048

undo dhcp server bootp reply-rfc-1048

【缺省情况】

DHCP服务器回应RFC 1048格式报文功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

有些BOOTP客户端发送的请求报文中，vend字段的格式不符合RFC 1048的要求。对于这种报文，DHCP服务器的缺省处理方法是不解析vend字段内容，将报文中vend字段的内容拷贝到回复报文中的vend字段回应给BOOTP客户端。

开启DHCP服务器的回应RFC 1048格式报文功能后，对于这种格式不符合RFC 1048要求的报文，DHCP服务器会将需要回应的选项以符合RFC 1048要求的格式，封装到回复报文的vend字段，并回应给BOOTP客户端。

需要注意的是，该功能只在客户端通过BOOTP报文申请静态绑定地址时有效。

【举例】

\# 开启DHCP服务器的回应RFC 1048格式报文功能。

\<Sysname\> system-view

Sysname dhcp server bootp reply-rfc-1048

**DHCP \-- DHCP服务器配置命令 \-- dhcp server database filename**

------------------------------------------------------------------------

dhcp server database filename{.commandkeywordsChar}命令用来指定存储DHCP服务器表项的文件名称。

undo dhcp server database filename{.commandkeywordsChar}命令用来删除指定的存储DHCP服务器表项的文件名称。

【命令】

**[dhcp server database filename**[ { *filename \|* **url** *url* [ **username** *username* [ **password** { **cipher** \| **simple** } *key* ] ] }]]

**[undo dhcp server database filename**]

【缺省情况】

未指定存储文件名称。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[filename*]：目标文件名，该配置用于本地存储模式。文件名取值范围的详细介绍，请参见"基础配置指导"中的"文件系统管理"。

**[url*** url*]：配置远程目标文件URL，该配置用于远程文件系统模式。此参数中不能包含用户名和密码，和参数*username*和*key*配合使用。

**[username*** username*]：配置远程目标文件URL时的用户名。

**[cipher**]：表示以密文方式设置用户密码。

**[simple**]：表示以明文方式设置用户密码。

*[key*]：设置的明文密码或密文密码，区分大小写。明文密码为1～32个字符的字符串；密文密码为1～73个字符的字符串。

【使用指导】

以明文或密文方式设置的用户密码，均以密文的方式保存在配置文件中。

·存储DHCP服务器表项时，如果设备中还不存在对应名称的文件，则设备会自动创建该文件。

·执行本命令后，会立即触发一次表项备份。之后，如果未配置**dhcp****server****database****update****interval**命令，若表项发生变化，默认在300秒之后刷新存储文件；若表项未发生变化，则不再刷新存储文件。如果配置了**dhcp server****database****update****interval**命令，若表项发生变化，则到达刷新时间间隔后刷新存储文件；若表项未发生变化，则不再刷新存储文件。

·参数*filename*不支持远程目标文件URL，配置远程目标文件URL请使用*url*、*username*、*key*配合使用。

·频繁擦写本地存储介质可能会影响存储介质寿命，建议使用远程文件系统模式存储DHCP服务器表项文件。

当进行远程存储时，支持FTP和TFTP协议：

·当采用FTP或TFTP协议时，服务器地址支持IPv4形式或IPv6形式，并且支持DNS域名方式。服务器地址为IPv6地址形式时需使用方括号(""和"")引用。配置服务器地址为DNS域名格式时请勿使用方括号引用。

·当采用FTP协议时，URL采用"ftp://服务器地址:端口号/文件路径"的形式，如有用户名和密码请分别使用参数username和参数key进行配置，用户名和密码必须和服务器上的配置一致，如果服务器只对用户名进行认证，则不用输入密码。

·当采用TFTP协议时，URL采用"tftp://服务器地址:端口号/文件路径"的形式。

【举例】

\# 配置存储DHCP服务器表项的文件名为database.dhcp。

\<Sysname\> system-view

Sysname dhcp server database filename database.dhcp

\# 配置远程存储DHCP服务器表项至IP地址为10.1.1.1的FTP服务器工作目录下,用户名为1，密码为1，文件名为database.dhcp。

\<Sysname\> system-view

Sysname dhcp server database filename url ftp://10.1.1.1/database.dhcp username 1 password simple 1

【相关命令】

·**dhcp server database update inte****rval**

·**dhcp server database update now**

·**dhcp server database update ****stop**

**DHCP \-- DHCP服务器配置命令 \-- dhcp server database update interval**

------------------------------------------------------------------------

**[dhcp server database update interval**]命令用来配置刷新DHCP服务器表项存储文件的延迟时间。

**[undo dhcp server database update interval**]命令用来恢复缺省情况。

【命令】

**[dhcp server database update interval ***seconds*]

**[undo dhcp server database update interval**]

【缺省情况】

若DHCP服务器表项不变化，则不刷新表项存储文件；若DHCP服务器表项发生变化，默认在300秒后刷新表项存储文件。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：刷新延迟时间，取值范围为60～864000，单位为秒。

【使用指导】

·若执行该命令配置之前没有使用**dhcp server database filename**命令配置固化文件，DHCP服务器不会在表项发生变化之后定时刷新表项数据到固化文件。

·若执行该命令配置之后通过**dhcp server database filename**命令配置固化文件，则DHCP服务器会在表项发生变化之后刷新表项数据到固化文件，且刷新表项的延迟时间为本命令配置的时间。

·当服务器表项发生变化后，DHCP服务器开始计时，当本命令配置的延迟时间到达后，DHCP服务器会把这个时间段内表项所有的变化信息备份到固化文件中。

【举例】

\# 若DHCP服务器表项发生变化，在10分钟后刷新表项存储文件。

\<Sysname\> system-view

Sysname dhcp server database update interval 600

【相关命令】

·{.commandkeywordsChar}[dhcp server database filename]{.commandkeywordsChar}

·**dhcp server database update now**

·**dhcp server database update stop**

**DHCP \-- DHCP服务器配置命令 \-- dhcp server database update now**

------------------------------------------------------------------------

**[dhcp server database update now**]命令用来将当前DHCP服务器表项保存到用户指定的文件中。

【命令】

**[dhcp server database update now**]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·本命令只用来触发一次DHCP服务器表项的备份。

·如果未通过**dhcp server database filename**命令指定存储表项的文件，则本命令的配置不会生效。

【举例】

\# 将当前的DHCP服务器表项保存到文件中。

\<Sysname\> system-view

Sysname dhcp server database update now

【相关命令】

·{.commandkeywordsChar}[dhcp server database filename]{.commandkeywordsChar}

·**dhcp server database update interval**

·**dhcp server database update stop**

**DHCP \-- DHCP服务器配置命令 \-- dhcp server database update stop**

------------------------------------------------------------------------

**[dhcp server database update stop**]命令用来终止当前的DHCP服务器表项恢复操作。

【命令】

**[dhcp server database update stop**]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·本命令只用来触发一次终止DHCP服务器表项的恢复操作。

·本命令只用来停止设备重启后从固化文件中恢复表项信息的过程，不影响除此之外的其他运行过程。当中断恢复表项信息的过程后，如果DHCP服务器分配了未恢复表项中的地址信息，可能会导致局域网设备地址冲突情况发生。

·从固化文件恢复表项的连接超时的最长时间为60分钟，可以通过本命令立刻终止远程恢复。DHCP服务器从固化文件中恢复表项的过程中，DHCP服务器不会学习新的表项。

【举例】

\# 终止当前的DHCP服务器表项恢复操作。

\<Sysname\> system-view

Sysname dhcp server database update stop

【相关命令】

·**dhcp** **s****erver** **database** **filename**

·**dhcp server database update interval**

·**dhcp server database update now**

**DHCP \-- DHCP服务器配置命令 \-- dhcp server forbidden-ip**

------------------------------------------------------------------------

dhcp server forbidden-ip{.commandkeywordsChar}命令用来配置全局不参与自动分配的IP地址。

undo dhcp server forbidden-ip{.commandkeywordsChar}命令用来取消全局不参与自动分配的IP地址的配置。

【命令】

dhcp server forbidden-ip {.commandkeywordsChar}*start-ip-address*{.commandkeywordsChar}[{.commandkeywordsChar}*end-ip-address*   **vpn-instance** *vpn-instance-name* ]

undo dhcp server forbidden-ip{.commandkeywordsChar} *start-ip-address* [ *end-ip-address*{.commandkeywordsChar}  **vpn-instance** *vpn-instance-name* ]

【缺省情况】

没有配置全局不参与自动分配的IP地址。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[start-ip-address*]：不参与自动分配的起始IP地址。

*[end-ip-address*]：不参与自动分配的结束IP地址，不能小于*start-ip-address*。如果不指定该参数，则表示只有一个不参与自动分配的IP地址，即*start-ip-address*；否则，表示*start-ip-address*到*end-ip-address*之间的IP地址均不能参与自动分配。

**[vpn-instance** *vpn-instance-name*]：指定不参与自动分配的IP地址所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示配置的是公网中不参与自动分配的IP地址。

【使用指导】

某些服务器占用的IP地址（如网关地址、FTP服务器地址），不能分配给DHCP客户端。通过本命令可以避免这些地址参与自动分配。

需要注意的是：

·如果通过[dhcp server forbidden-ip]{.commandkeywordsChar}命令将已经静态绑定的IP地址配置为不参与自动分配的地址，则该地址仍然可以分配给静态绑定的用户。

·执行[undo dhcp server forbidden-ip]{.commandkeywordsChar}命令取消不参与自动分配IP地址的配置时，指定的地址/地址范围必须与执行dhcp server forbidden-ip{.commandkeywordsChar}命令时指定的地址/地址范围保持一致。如果配置不参与自动分配的IP地址为某一地址范围，则只能同时取消该地址范围内所有IP地址的配置，不能单独取消其中某个IP地址的配置。

·多次执行[dhcp server forbidden-ip]{.commandkeywordsChar}命令，可以配置多个不参与自动分配的IP地址段。

【举例】

\# 配置10.110.1.1到10.110.1.63之间的IP地址不参与地址自动分配。

\<Sysname\> system-view

Sysname dhcp server forbidden-ip 10.110.1.1 10.110.1.63

【相关命令】

· forbidden-ip{.commandkeywordsChar}

·**static-bind**

**DHCP \-- DHCP服务器配置命令 \-- dhcp server ip-pool**

------------------------------------------------------------------------

dhcp server ip-pool{.commandkeywordsChar}命令用来创建DHCP地址池并进入DHCP地址池视图。如果已经创建了DHCP地址池，则直接进入该地址池视图。

undo dhcp server ip-pool{.commandkeywordsChar}命令用来删除指定的地址池。

【命令】

dhcp server ip-pool {.commandkeywordsChar}*pool-name*

undo dhcp server ip-pool{.commandkeywordsChar} *pool-name*

【缺省情况】

不存在任何DHCP地址池。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[pool-name*]：DHCP地址池名称，是地址池的唯一标识，为1～63个字符的字符串，不区分大小写。

【使用指导】

在DHCP地址池下，可以配置为DHCP客户端分配的IP地址、网关地址等参数。

【举例】

\# 创建名称为pool1的DHCP地址池。

\<Sysname\> system-view

Sysname dhcp server ip-pool pool1

Sysname-dhcp-pool-pool1

【相关命令】

·**dhcp server apply ip-poo[l{.commandkeywordsChar}]**

·**display dhcp server pool**

**DHCP \-- DHCP服务器配置命令 \-- dhcp server ping packets**

------------------------------------------------------------------------

dhcp server ping packets{.commandkeywordsChar}命令用来配置DHCP服务器发送回显请求报文的最大数目。

undo dhcp server ping packets{.commandkeywordsChar}命令用来恢复缺省情况。

【命令】

dhcp server ping packets{.commandkeywordsChar} *number*

undo dhcp server ping packets

【缺省情况】

DHCP服务器发送回显请求报文的最大数目为1。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：发送回显请求报文的最大数目，取值范围为0～10。0表示DHCP服务器将IP地址分配给DHCP客户端之前，不会通过ping操作探测该地址是否冲突。

【使用指导】

为防止IP地址重复分配导致地址冲突，DHCP服务器为客户端分配地址前，需要先对该地址进行探测。

DHCP服务器的地址探测是通过ping功能实现的，通过检测是否能在指定时间内得到ping响应来判断是否存在地址冲突。DHCP服务器发送目的地址为待分配地址的ICMP回显请求报文。如果在指定时间内收到回显响应报文，则认为存在地址冲突。DHCP服务器从地址池中选择新的IP地址，并重复上述操作。如果在指定时间内没有收到回显响应报文，则继续发送ICMP回显请求报文，直到发送的回显请求报文数目达到本命令配置的最大值。如果仍然没有收到回显响应报文，则将地址分配给客户端，从而确保客户端获得的IP地址唯一。

【举例】

\# 配置DHCP服务器最多发送10个回显请求报文。

\<Sysname\> system-view

Sysname dhcp server ping packets 10

【相关命令】

·**dhcp server ping timeout**

·{.commandkeywordsChar}[display dhcp server conflict]{.commandkeywordsChar}

· reset dhcp server conflict{.commandkeywordsChar}

**DHCP \-- DHCP服务器配置命令 \-- dhcp server ping timeout**

------------------------------------------------------------------------

dhcp server ping timeout{.commandkeywordsChar}命令用来配置DHCP服务器等待回显响应报文的超时时间。

undo dhcp server ping timeout{.commandkeywordsChar}命令用来恢复缺省情况。

【命令】

dhcp server ping timeout {.commandkeywordsChar}*milliseconds*

undo dhcp server ping timeout

【缺省情况】

DHCP服务器等待回显响应报文的超时时间为500毫秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[milliseconds*]：等待回显响应报文的超时时间，取值范围是0～10000，单位为毫秒。0表示DHCP服务器将IP地址分配给DHCP客户端之前，不会通过ping操作探测该地址是否冲突。

【使用指导】

为防止IP地址重复分配导致地址冲突，DHCP服务器为客户端分配地址前，需要先对该地址进行探测。

DHCP服务器的地址探测是通过ping功能实现的，通过检测是否能在指定时间内得到ping响应来判断是否存在地址冲突。DHCP服务器发送目的地址为待分配地址的ICMP回显请求报文。如果在本命令指定的时间内收到回显响应报文，则认为存在地址冲突。DHCP服务器从地址池中选择新的IP地址，并重复上述操作。如果在指定时间内没有收到回显响应报文，则继续发送ICMP回显请求报文，直到发送的回显请求报文数目达到最大值。如果仍然没有收到回显响应报文，则将地址分配给客户端，从而确保客户端获取的IP地址唯一。

【举例】

\# 配置DHCP服务器等待回显响应报文的超时时间为1000毫秒。

\<Sysname\> system-view

Sysname dhcp server ping timeout 1000

【相关命令】

·{.commandkeywordsChar}[dhcp server ping packets]{.commandkeywordsChar}

·{.commandkeywordsChar}[display dhcp server conflict]{.commandkeywordsChar}

· reset dhcp server conflict{.commandkeywordsChar}

**DHCP \-- DHCP服务器配置命令 \-- dhcp server relay information enable**

------------------------------------------------------------------------

dhcp server relay information enable{.commandkeywordsChar}命令用来配置DHCP服务器处理Option 82。

undo dhcp server relay information enable{.commandkeywordsChar}命令用来配置DHCP服务器忽略Option 82。

【命令】

dhcp server relay information enable

undo dhcp server relay information enable

【缺省情况】

DHCP服务器处理Option 82。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当DHCP服务器收到含有Option 82的报文时，如果DHCP服务器处理Option 82，则将请求报文中的Option 82原样复制到应答报文中；如果DHCP服务器忽略Option 82，则不会在应答报文中携带Option 82。

【举例】

\# 配置DHCP服务器忽略Option 82。

\<Sysname\> system-view

Sysname undo dhcp server relay information enable

**DHCP \-- DHCP服务器配置命令 \-- display dhcp server conflict**

------------------------------------------------------------------------

display dhcp server conflict{.commandkeywordsChar}命令用来显示DHCP的地址冲突信息。

【命令】

display dhcp server conflict{.commandkeywordsChar} [[ ip{.commandkeywordsChar} *ip-address* ]  **vpn-instance** *vpn-instance-name* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

ip{.commandkeywordsChar} *ip-address*：显示指定IP地址的地址冲突信息。如果不指定本参数，则显示所有的地址冲突信息。

**[vpn-instance** *vpn-instance-name*]：显示指定VPN内的地址冲突信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示显示的是公网中的地址冲突信息。

【使用指导】

DHCP服务器在下列几种情况下会生成地址冲突信息：

·DHCP服务器在为客户端分配IP地址前，通过ping操作检测到网络中已有主机使用该地址。

·DHCP客户端向DHCP服务器发送Decline报文，报告DHCP服务器为其分配的地址存在冲突。

·DHCP服务器检测到地址池内的可供分配的地址是设备自身的地址。

【举例】

\# 显示所有的地址冲突信息。

\<Sysname\> display dhcp server conflict

IP address          Detect time

4.4.4.1             Apr 25 16:57:20 2007

4.4.4.2             Apr 25 17:00:10 2007

表1-1 display dhcp server conflict命令显示信息描述表

字段

描述

IP address

发生冲突的IP地址

Detect time

检测到冲突的时间

【相关命令】

·{.commandkeywordsChar}[reset dhcp server conflict]{.commandkeywordsChar}

**DHCP \-- DHCP服务器配置命令 \-- display dhcp server database**

------------------------------------------------------------------------

**[display dhcp server database**]命令用来显示DHCP服务器的表项备份信息。

【命令】

**[display dhcp server database**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示DHCP服务器的表项备份信息。

\<Sysname\> display dhcp server database

 File name               :   database.dhcp

 Username                :  

 Password                :  

 Update interval         :   600 seconds

 Latest write time       :   Feb  8 16:09:53 2014

 Status                  :   Last write succeeded.

表1-2 display dhcp server database命令显示信息描述表

字段

描述

File name

存储DHCP服务器表项的文件名称

Username

配置远程目标文件时的用户名

Password

配置远程目标文件时的密码，有配置时显示为"\*\*\*\*\*\*"

Update interval

定期刷新表项存储文件的刷新时间间隔，单位为秒

Latest write time

最近一次写文件的时间

Status

写文件的状态，即写文件是否成功

·Writing：正在写文件{.TableTextChar}

·Last write succeeded.：上一次写文件成功{.TableTextChar}

·Last write failed.：上一次写文件失败{.TableTextChar}

**DHCP \-- DHCP服务器配置命令 \-- display dhcp server expired**

------------------------------------------------------------------------

display dhcp server expired{.commandkeywordsChar}命令用来显示租约过期的地址绑定信息。

【命令】

[[display dhcp server expired ]{.commandkeywordsChar}[ [[ ip{.commandkeywordsChar} *ip-address ]  vpn-instance vpn-instance-name * \| pool{.commandkeywordsChar} *pool-name* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

ip{.commandkeywordsChar} *ip-address*：显示指定IP地址的租约过期地址绑定信息。

**[vpn-instance** *vpn-instance-name*]：显示指定VPN内的租约过期的地址绑定信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示显示的是公网中的租约过期的地址绑定信息。

pool{.commandkeywordsChar} *pool-name*：显示指定地址池中租约过期的地址绑定信息。*pool-name*表示地址池名称，为1～63个字符的字符串，不区分大小写。

【使用指导】

执行本命令时，如果不指定任何参数，则显示所有租约过期的地址绑定信息。

在DHCP地址池的可用地址分配完后，租约过期的地址将被分配给DHCP客户端。

【举例】

\# 显示所有租约过期的地址绑定信息。

\<Sysname\> display dhcp server expired

IP address       Client-identifier/Hardware address    Lease expiration

4.4.4.6          3030-3066-2e65-3230-302e-3130-3234    Apr 25 17:10:47 2007

                 -2d45-7468-6572-6e65-7430-2f31

表1-3 display dhcp server expired命令显示信息描述表

字段

描述

IP address

租约过期的IP地址

Client-identifier/Hardware address

租约过期的客户端ID或MAC地址

Lease expiration

租约过期的时间

【相关命令】

· r{.commandkeywordsChar}**eset dhcp server expired**

**DHCP \-- DHCP服务器配置命令 \-- display dhcp server free-ip**

------------------------------------------------------------------------

display dhcp server free-ip{.commandkeywordsChar}命令用来显示DHCP地址池的空闲地址信息，即尚未分配给DHCP客户端的IP地址信息。

【命令】

[[display dhcp server free-ip ]{.commandkeywordsChar}[[ pool {.commandkeywordsChar}*pool-name*{.commandkeywordsChar}\| vpn-instance {.commandkeywordsChar}vpn-instance-name{.commandkeywordsChar}]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[pool ***pool-name*]：显示指定地址池的空闲地址信息。*pool-name*表示地址池名称，为1～63个字符的字符串，不区分大小写。如果不指定本参数，则显示所有地址池的空闲地址信息。

**[vpn-instance** *vpn-instance-name*]：显示指定VPN内的地址池空闲地址信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示显示的是公网中的地址池空闲地址信息。

【举例】

\# 显示所有DHCP地址池的空闲地址信息。

\<Sysname\> display dhcp server free-ip

Pool name: 1

  Network: 10.0.0.0 mask 255.0.0.0

    IP ranges from 10.0.0.10 to 10.0.0.100

    IP ranges from 10.0.0.105 to 10.0.0.255

  Secondary networks:

    10.1.0.0 mask 255.255.0.0

      IP ranges from 10.1.0.0 to 10.1.0.255

    10.2.0.0 mask 255.255.0.0

      IP Ranges from 10.2.0.0 to 10.2.0.255

Pool name: 2

  Network: 20.1.1.0 mask 255.255.255.0

    IP ranges from 20.1.1.0 to 20.1.1.255

表1-4 display dhcp server free-ip命令显示信息描述表

字段

描述

Pool name

地址池的名称

Network

可分配的地址网段

IP ranges

可分配的地址范围

Secondary networks

可分配的从地址网段

【相关命令】

·{.commandkeywordsChar}[address range]{.commandkeywordsChar}

·{.commandkeywordsChar}[dhcp server ip-pool]{.commandkeywordsChar}

·{.commandkeywordsChar}[network]{.commandkeywordsChar}

**DHCP \-- DHCP服务器配置命令 \-- display dhcp server ip-in-use**

------------------------------------------------------------------------

display dhcp server ip-in-use{.commandkeywordsChar}命令用来显示DHCP地址绑定信息。

【命令】

[[display dhcp server ip-in-use ]{.commandkeywordsChar}[{.commandkeywordsChar}[[ ip{.commandkeywordsChar} *ip-address*{.commandkeywordsChar}]{.commandkeywordsChar} [vpn-instance{.commandkeywordsChar} vpn-instance-name ]{.commandkeywordsChar}\| pool {.commandkeywordsChar}*pool-name* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

ip{.commandkeywordsChar} *ip-address*：显示指定IP地址的地址绑定信息。

**[vpn-instance** *vpn-instance-name*]：显示指定VPN内的DHCP地址绑定信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示显示的是公网中的DHCP地址绑定信息。

pool{.commandkeywordsChar} *pool-name*：显示指定地址池的地址绑定信息。*pool-name*表示地址池名称，为1～63个字符的字符串，不区分大小写。

【使用指导】

执行本命令时，如果不指定任何参数，则显示所有DHCP地址绑定信息。

需要注意的是，如果租约的截止时间超过2100年，则显示为After 2100。

当DHCP服务器作为DHCP客户端的网关设备时，DHCP服务器上记录的该DHCP客户端的地址绑定信息才会提供给其他安全特性（如IP Source Guard）使用。

【举例】

\# 显示所有DHCP地址绑定信息。

\<Sysname\> display dhcp server ip-in-use

IP address       Client identifier/    Lease expiration      Type

                 Hardware address

10.1.1.1         4444-4444-4444        Not used              Static(F)

10.1.1.2         3030-3030-2e30-3030-  May 1 14:02:49 2009   Auto(C)

                 662e-3030-3033-2d45-

7468-6572-6e65-74

10.1.1.3         1111-1111-1111        After 2100            Static(C)

表1-5 display dhcp server ip-in-use命令显示信息描述表

字段

描述

IP address

分配给DHCP客户端的IP地址

Client identifier/Hardware address

客户端ID或客户端的硬件地址

Lease expiration

租约到期时间，取值包括：

·具体的时间值（如May 1 14:02:49 2009）：表示租约在该时间到期

·Not used：表示静态绑定的地址尚未分配给特定客户端

·Unlimited：表示租约为无限长

·After 2100：表示租约过期时间超过2100年

Type

地址绑定的类型，取值包括：

·Static(F)：表示尚未分配给客户端的静态绑定，即静态无效绑定

·Static(O)：服务器从地址池选择静态绑定的IP地址，并发送DHCP-OFFER报文为客户端提供该IP地址后产生该类型的地址绑定信息，即静态临时绑定

·Static(C)：表示已经分配给客户端的静态绑定，即静态正式绑定

·Auto(O)：表示动态绑定的临时租约，即从地址池中动态选择IP地址，并发送DHCP-OFFER报文为客户端提供该IP地址后，产生的租约

·Auto(C)：表示动态绑定的正式租约，即从地址池中动态选择IP地址，并发送DHCP-ACK报文成功将该IP地址分配给客户端后，产生的租约

【相关命令】

·**reset dhcp server ip-in-use**

**DHCP \-- DHCP服务器配置命令 \-- display dhcp server pool**

------------------------------------------------------------------------

display dhcp server pool{.commandkeywordsChar}命令用来显示DHCP地址池的信息。

【命令】

[[display dhcp server pool]{.commandkeywordsChar}[ [{.commandkeywordsChar}*pool-name* \| **vpn-instance** *vpn-instance-name* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[pool-name*]：显示指定地址池的信息。*pool-name*表示地址池名称，为1～63个字符的字符串，不区分大小写。如果不指定本参数，则显示所有地址池的信息。

**[vpn-instance** *vpn-instance-name*]：显示指定VPN内的DHCP地址池信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示显示的是公网中的DHCP地址池信息。

【举例】

\# 显示所有DHCP地址池的信息。

\<Sysname\> display dhcp server pool

Pool name: 0

  Network 20.1.1.0 mask 255.255.255.0

  class a range 20.1.1.50 20.1.1.60

  bootfile-name abc.cfg

  dns-list 20.1.1.66 20.1.1.67 20.1.1.68

  domain-name www.aabbcc.com

  bims-server ip 192.168.0.51 sharekey cipher \$c\$3\$K13OmQPi791YvQoF2Gs1E+65LOU=

  option 2 ip-address 1.1.1.1

  expired 1 2 3 0

Pool name: 1

  Network 20.1.1.0 mask 255.255.255.0

  secondary networks:

20.1.2.0 mask 255.255.255.0

    20.1.3.0 mask 255.255.255.0

  bims-server ip 192.168.0.51 port 50 sharekey cipher \$c\$3\$K13OmQPi791YvQoF2Gs1E+65LOU=

  forbidden-ip 20.1.1.22 20.1.1.36 20.1.1.37

  forbidden-ip 20.1.1.22 20.1.1.23 20.1.1.24

gateway-list 1.1.1.1 2.2.2.2 4.4.4.4

  nbns-list 5.5.5.5 6.6.6.6 7.7.7.7

  netbios-type m-node

  option 2 ip-address 1.1.1.1

  expired 1 0 0 0

Pool name: 2

  Network 20.1.1.0 mask 255.255.255.0

  address range 20.1.1.1 to 20.1.1.15

  class departmentA range 20.1.1.20 to 20.1.1.29

  class departmentB range 20.1.1.30 to 20.1.1.40

  next-server 20.1.1.33

  tftp-server domain-name www.dian.org.cn

  tftp-server ip-address 192.168.0.120

  voice-config ncp-ip 10.1.1.2

  voice-config as-ip 10.1.1.5

  voice-config voice-vlan 3 enable

  voice-config fail-over 10.1.1.1 123\*

  option 2 ip-address 1.1.1.3

  expired 1 0 0 0

Pool name: 3

  static bindings:

    ip-address 10.10.1.2 mask 255.0.0.0

      hardware-address 00e0-00fc-0001 ethernet

    ip-address 10.10.1.3 mask 255.0.0.0

      client-identifier aaaa-bbbb

  expired unlimited

表1-6 display dhcp server pool命令显示信息描述表

字段

描述

Pool name

地址池的名称

Network

可分配的地址网段

secondary networks

可分配的从地址网段

address range

可分配的地址范围

class *class-name* range

为指定DHCP用户类分配的地址范围

static bindings

静态绑定的IP地址、硬件地址或客户端ID

option

自定义的DHCP选项

expired

租约期限，其后数值的单位分别为天、小时、分钟和秒。例如，expired 1 2 3 4表示租约期限为1天2小时3分钟4秒

bootfile-name

为DHCP客户端分配的启动文件名

dns-list

为DHCP客户端分配的DNS服务器地址

domain-name

为DHCP客户端分配的域名后缀

bims-server

为DHCP客户端分配的BIMS服务器信息

forbidden-ip

DHCP地址池中不参与自动分配的IP地址

gateway-list

为DHCP客户端分配的网关地址

nbns-list

为DHCP客户端分配的WINS服务器地址

netbios-type

为DHCP客户端分配的NetBIOS节点类型

next-server

为DHCP客户端分配的下一个提供服务的服务器IP地址

tftp-server domain-name

为DHCP客户端分配的TFTP服务器名

tftp-server ip-address

为DHCP客户端分配的TFTP服务器地址

voice-config ncp-ip

为DHCP客户端分配的网络呼叫处理器的地址

voice-config as-ip

为DHCP客户端分配的备用服务器的地址

voice-config voice-vlan

为DHCP客户端分配的语音VLAN

voice-config fail-over

为DHCP客户端分配的自动故障转移呼叫路由

**DHCP \-- DHCP服务器配置命令 \-- display dhcp server statistics**

------------------------------------------------------------------------

display dhcp server statistics{.commandkeywordsChar}命令用来显示DHCP服务器的统计信息。

【命令】

**[display dhcp server statistics**[ [ **pool** *pool-name* \| **vpn-instance** *vpn-instance-name* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[pool** *pool-name*]：显示指定地址池的统计信息。*pool-name*表示地址池名称，为1～63个字符的字符串，不区分大小写。如果不指定本参数，则显示所有地址池的统计信息。

**[vpn-instance** *vpn-instance-name*]：显示指定VPN内的DHCP服务器的统计信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示显示的是公网中的DHCP服务器的统计信息。

【举例】

\# 显示DHCP服务器的统计信息。

\<Sysname\> display dhcp server statistics

    Pool number:                       1

    Pool utilization:                  0.39%

    Bindings:

      Automatic:                       1

      Manual:                          0

      Expired:                         0

    Conflict:                          1

    Messages received:                10

      DHCPDISCOVER:                    5

      DHCPREQUEST:                     3

      DHCPDECLINE:                     0

      DHCPRELEASE:                     2

      DHCPINFORM:                      0

      BOOTPREQUEST:                    0

    Messages sent:                     6

      DHCPOFFER:                       3

      DHCPACK:                         3

      DHCPNAK:                         0

      BOOTPREPLY:                      0

    Bad Messages:                      0

表1-7 display dhcp server statistics命令显示信息描述表

字段

描述

Pool number

地址池的数目，显示指定地址池的统计信息时无此字段

Pool utilization

地址池利用率

·显示所有DHCP租约统计信息时，表示所有地址池的总体利用率

·显示指定地址池的租约统计信息时，表示该地址池的利用率

Bindings

各种状态的地址绑定数，包括：

·Automatic：动态分配的IP地址绑定数

·Manual：手工绑定的IP地址绑定数

·Expired：租约过期的IP地址绑定数

Conflict

冲突地址的总数，显示指定地址池的统计信息时无此字段

Messages received

DHCP服务器接收到DHCP客户端发送的报文数，包括：

·DHCPDISCOVER

·DHCPREQUEST

·DHCPDECLINE

·DHCPRELEASE

·DHCPINFORM

·BOOTPREQUEST

显示指定地址池的统计信息时无此类字段

Messages sent

DHCP服务器发给DHCP客户端的报文数，包括：

·DHCPOFFER

·DHCPACK

·DHCPNAK

·BOOTPREPLY

显示指定地址池的统计信息时无此类字段

Bad Messages

错误信息数，显示指定地址池的统计信息时无此类字段

【相关命令】

·**reset dhcp server statistics**

**DHCP \-- DHCP服务器配置命令 \-- dns-list**

------------------------------------------------------------------------

dns-list{.commandkeywordsChar}命令用来[配置]DHCP地址池为DHCP客户端分配的DNS服务器地址。

undo dns-list{.commandkeywordsChar}命令用来删除DHCP地址池为DHCP客户端分配的DNS服务器地址。

【命令】

dns-list{.commandkeywordsChar} *ip-address*&\<1-8\>

undo dns-list{.commandkeywordsChar} [ *ip-address*&\<1-8\> ]

【缺省情况】

没有配置DHCP地址池为DHCP客户端分配的DNS服务器地址。

【视图】

DHCP地址池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*&\<1-8\>]：DNS服务器的IP地址。&\<1-8\>表示最多可以输入8个IP地址，每个IP地址之间用空格分隔。

【使用指导】

如果多次执行该命令，新的配置会覆盖已有配置。

执行**undo [dns-list{.commandkeywordsChar}]**命令时，如果没有指定任何参数，则删除DHCP地址池中的所有DNS服务器地址。

【举例】

\# 配置DHCP地址池0为DHCP客户端分配的DNS服务器地址为10.1.1.254。

\<Sysname\> system-view

Sysname dhcp server ip-pool 0

Sysname-dhcp-pool-0 dns-list 10.1.1.254

【相关命令】

·**display dhcp server pool**

**DHCP \-- DHCP服务器配置命令 \-- domain-name**

------------------------------------------------------------------------

domain-name{.commandkeywordsChar}命令用来配置DHCP地址池为DHCP客户端分配的域名。

undo domain-name{.commandkeywordsChar}命令用来删除DHCP地址池为DHCP客户端分配的域名。

【命令】

domain-name{.commandkeywordsChar} *domain-name*

undo domain-name

【缺省情况】

没有配置DHCP地址池为DHCP客户端分配的域名。

【视图】

DHCP地址池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[domain-name*]：DHCP客户端的域名，为1～50个字符的字符串，区分大小写。

【使用指导】

如果多次执行该命令，新的配置会覆盖已有配置。

【举例】

\# 配置DHCP地址池0为DHCP客户端分配的域名为company.com。

\<Sysname\> system-view

Sysname dhcp server ip-pool 0

Sysname-dhcp-pool-0 domain-name company.com

【相关命令】

·**display dhcp server pool**

**DHCP \-- DHCP服务器配置命令 \-- expired**

------------------------------------------------------------------------

expired{.commandkeywordsChar}命令用来配置DHCP地址池中分配的IP地址的租约有效期限。

undo expired{.commandkeywordsChar}命令用来恢复缺省情况。

【命令】

[[expired ]{.commandkeywordsChar}{[ day {.commandkeywordsChar}*day*{.commandkeywordsChar}[ hour{.commandkeywordsChar} *hour*{.commandkeywordsChar}[ minute{.commandkeywordsChar} *minute*  **second** *second*  ] ] \| unlimited {.commandkeywordsChar}}]]

undo expired

【缺省情况】

DHCP地址池中IP地址的租约有效期限为1天。

【视图】

DHCP地址池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

day{.commandkeywordsChar} *day*：指定租约过期的天数，*day*取值范围为0～365。

hour{.commandkeywordsChar} *hour*：指定租约过期的小时数，*hour*取值范围为0～23。

minute{.commandkeywordsChar} *minute*：指定租约过期的分钟数，*minute*取值范围为0～59。

second {.commandkeywordsChar}*second*：指定租约过期的秒数，*second*取值范围为0～59。

unlimited{.commandkeywordsChar}：有效期限为无限长（实际上系统限定约为136年）。

【使用指导】

DHCP服务器从DHCP地址池中选择IP地址分配给DHCP客户端时，会同时将该地址池中IP地址的租约有效期限通知给DHCP客户端。在租约有效期限到达之前，DHCP客户端需要进行续约申请。如果续约成功，则DHCP客户端可以继续使用该IP地址。否则，租约有效期限到达后，DHCP客户端不能再继续使用该IP地址，并且DHCP服务器会将该地址添加到过期租约信息中。

【举例】

\# 配置地址池0的IP地址租约有效期为1天2小时3分4秒。

\<Sysname\> system-view

Sysname dhcp server ip-pool 0

Sysname-dhcp-pool-0 expired day 1 hour 2 minute 3 second 4

【相关命令】

·**display [dhcp server expired{.commandkeywordsChar}]**

·**display dhcp server pool**

· reset dhcp server expired{.commandkeywordsChar}

**DHCP \-- DHCP服务器配置命令 \-- forbidden-ip**

------------------------------------------------------------------------

forbidden-ip{.commandkeywordsChar}命令用来配置指定地址池中不参与自动分配的IP地址。

undo forbidden-ip{.commandkeywordsChar}命令用来取消指定地址池中不参与自动分配的IP地址的配置。

【命令】

forbidden-ip{.commandkeywordsChar}* ip-address*&\<1-8\>

undo forbidden-ip{.commandkeywordsChar} [ *ip-address*&\<1-8\>{.commandkeywordsChar}]

【缺省情况】

没有配置指定地址池中不参与自动分配的IP地址。

【视图】

DHCP地址池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*&\<1-8\>]：地址池中不参与自动分配的IP地址。&\<1-8\>表示最多可以输入8个IP地址，每个IP地址之间用空格分隔。

【使用指导】

·在DHCP地址池视图下通过forbidden-ip{.commandkeywordsChar}命令配置不参与自动分配的IP地址后，只有当前的地址池不能分配这些IP地址，其他地址池仍然可以分配这些IP地址。

·多次执行[forbidden-ip]{.commandkeywordsChar}命令，可以配置多个不参与自动分配的IP地址。每个地址池最多能配置4096个地址。

·执行[undo forbidden-ip]{.commandkeywordsChar}命令时，如果没有指定任何参数，则删除所有不参与自动分配的IP地址。

【举例】

\# 配置DHCP地址池0中不参与自动分配的IP地址为192.168.1.3和192.168.1.10。

\<Sysname\> system-view

Sysname dhcp server ip-pool 0

Sysname-dhcp-pool-0 forbidden-ip 192.168.1.3 192.168.1.10

【相关命令】

· dhcp server forbidden-ip{.commandkeywordsChar}

·**display dhcp server pool**

**DHCP \-- DHCP服务器配置命令 \-- gateway-list**

------------------------------------------------------------------------

gateway-list{.commandkeywordsChar}命令用来配置DHCP服务器为DHCP客户端分配的网关地址。

undo gateway-list{.commandkeywordsChar}命令用来删除DHCP服务器为DHCP客户端分配的网关地址。

【命令】

gateway-list{.commandkeywordsChar}* ip-address*&\<1-8\> [ **export-route** ]

undo gateway-list{.commandkeywordsChar} [ *ip-address*&\<1-8\>   **export-route** ]

【缺省情况】

DHCP地址池、DHCP从网段下均没有配置为DHCP客户端分配的网关地址。

【视图】

DHCP地址池视图/DHCP从网段视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*&\<1-8\>]：网关的IP地址。&\<1-8\>表示最多可以输入8个IP地址，每个IP地址之间用空格分隔。

**[export-route**]：将网关列表信息下发给地址管理，通过应答客户端的ARP请求，即可实现对不同类型的业务流量的引导。

【使用指导】

·DHCP地址池视图下执行gateway-list{.commandkeywordsChar}命令，配置的是为地址池中所有DHCP客户端分配的网关地址。如果用户需要为地址池下某个从网段的DHCP客户端分配其它的网关地址，可以在地址池的从网段视图下执行gateway-list{.commandkeywordsChar}命令。如果在地址池视图和从网段视图下都配置了网关地址，则优先将从网段视图下配置的网关地址分配给从网段的DHCP客户端。

·如果多次执行该命令，新的配置会覆盖已有配置。

·执行[undo gateway-list]{.commandkeywordsChar}命令时，如果没有指定任何参数，则删除所有配置的网关地址。

·网关地址应该和可分配的地址在同一网段。

·执行**gateway-list export-route**命令可以用来发布网关路由，如果多次执行该命令，新的配置会覆盖已有配置。

【举例】

\# 配置DHCP地址池0为DHCP客户端分配的网关地址为10.1.1.1。

\<Sysname\> system-view

Sysname dhcp server ip-pool 0

Sysname-dhcp-pool-0 gateway-list 10.1.1.1

【相关命令】

·**display dhcp server pool**

**DHCP \-- DHCP服务器配置命令 \-- if-match**

------------------------------------------------------------------------

if-match{.commandkeywordsChar}命令用来配置DHCP用户类的匹配规则。

undo if-match{.commandkeywordsChar}命令用来删除DHCP用户类的匹配规则。

【命令】

if-match rule {.commandkeywordsChar}*rule-number*{.commandkeywordsChar}[[ option]{.commandkeywordsChar} *option-code*{.commandkeywordsChar}[[ hex{.commandkeywordsChar} *hex-string*{.commandkeywordsChar} [mask {.commandkeywordsChar}*mask*[ \| offset ]{.commandkeywordsChar}*offset* length{.commandkeywordsChar} *length* ] ] \| **hardware-address** *hardware-address* **mask** *hardware-address-mask* }]]

undo if-match rule {.commandkeywordsChar}*rule-number*

【缺省情况】

没有配置DHCP用户类的匹配规则。

【视图】

DHCP用户类视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

rule {.commandkeywordsChar}*rule-number*：匹配规则编号，取值范围为1～16。编号越小，匹配优先级越高。

option{.commandkeywordsChar}* option-code*：DHCP选项的数值，取值范围为1～254。*option-code*用于指定匹配DHCP客户端时从DHCP报文中获取哪个选项。

hex{.commandkeywordsChar} *hex-string*：指定用来匹配报文中指定选项的内容。*hex-string*为十六进制数串，位数的取值范围为2～256之间的偶数。

mask{.commandkeywordsChar} *mask*：指定与选项内容匹配时使用的掩码。*mask*为十六进制掩码数串，位数的取值范围为2～256之间的偶数。*mask*的长度必须和*hex-string*长度相同。

offset{.commandkeywordsChar} *offset*：指定匹配DHCP客户端时获取选项内容的起始位置。*offset*为选项内容偏移量，取值范围为0～254，单位为字节。如果不指定本参数，则表示从选项值第一字节开始匹配整个选项的内容。

length{.commandkeywordsChar} *length*：指定匹配DHCP客户端时获取选项内容的长度。*length*为选项内容的长度，取值范围为1～128，单位为字节。指定的选项内容长度必须和*hex-string*长度相同。

**[hardware-address** *hardware-address*]：指定匹配规则的硬件地址。*hardware-address*表示客户端的硬件地址，为4～39个字符的字符串，字符串只能包含十六进制数和"-"，且形式为H-H-H，除最后一个H表示2位或4位十六进制数外，其他均表示4位十六进制数。例如：aabb-ccdd-ee为有效的硬件地址，aabb-c-dddd和aabb-cc-dddd为无效的客户端硬件地址。

**[mask ***hardware-address-mask*]：指定匹配规则的硬件地址掩码。长度需要与*hardware-address*保持一致。

【使用指导】

DHCP服务器通过将DHCP客户端发送的报文与本命令配置的规则匹配，来判断DHCP客户端属于的DHCP用户类。DHCP用户类视图下通过多次执行if-match{.commandkeywordsChar}命令，可以配置多条匹配规则。只要任意一条规则匹配成功，就认为该DHCP客户端属于该用户类。

将报文与某一条**if-match option**命令配置的规则匹配的方式为：

·如果规则中只指定了*option-code*参数，则只要报文中包括该选项，就认为匹配成功。否则，匹配失败。

·如果规则中只指定了*option-code*和*hex-string*参数，则报文中指定选项的值开始的字节与*hex-string*相同时，认为匹配成功。否则，匹配失败。

·如果规则中指定了*option-code*、*hex-string*、*offset*和*length*参数，则将指定选项值的第*offset*+1位到*offset*+*length*位的内容与*hex-string*比较，二者相同时，认为匹配成功。否则，匹配失败。

·如果规则中指定了*option-code*、*hex-string*、*mask*参数，则将指定选项值的第1位到*mask*长度-1位的内容与*mask*进行与运算，将结果与*hex-string*与*mask*与运算的结果比较，二者相同时，认为匹配成功。否则，匹配失败。

将报文与某一条**if-match hardware-address**命令配置的规则匹配的方式为：

·匹配硬件地址类型，目前只支持以太类型的硬件地址（即MAC地址）匹配，非以太类型的硬件地址均会匹配失败。

·如果报文中的客户端硬件地址与配置的客户端硬件地址及硬件地址掩码匹配，则认为匹配成功。否则，匹配失败。

·匹配时报文中的客户端硬件地址长度与配置规则中的硬件地址长度一致时才进行匹配，否则直接认为不匹配。如匹配规则为**if-match rule** 1 **hardware-address** 0094-0000 **mask** ffff-0000，需匹配硬件地址长度为4字节的用户；若报文中客户端硬件地址长度为6字节（比如0094-0000-0010），则认为匹配失败。

·匹配硬件地址时，可以配置不连续匹配的硬件地址，如匹配规则为**if-match rule** 1 **hardware-address** 0094-0000-1100 **mask** ffff-0000-ff00，则匹配硬件地址为0094-xxxx-11xx（x代表变量）的报文。

需要注意的是，在同一用户类视图下不同的 if-match{.commandkeywordsChar}命令指定的DHCP选项数值*option-code*可以相同，但是*rule-number*不能相同。多次配置相同匹配规则编号的命令，如果规则类型（包括匹配Option还是匹配硬件地址）相同，新的配置会覆盖已有配置；否则，后配置的命令不生效。同时，不同*rule-number*的匹配规则内容不能完全相同。

【举例】

\# 配置DHCP用户类exam的匹配规则为匹配规则编号1，报文中包含Option 82。

\<Sysname\> system-view

Sysname dhcp class exam

Sysname-dhcp-class-exam if-match rule 1 option 82

\# 配置DHCP用户类exam的匹配规则为匹配规则编号2，报文中包含Option 82，并且该选项的前三个字节为0x13ae92。

\<Sysname\> system-view

Sysname dhcp class exam

Sysname-dhcp-class-exam if-match rule 2 option 82 hex 13ae92 offset 0 length 3

\# 配置DHCP用户类exam的匹配规则为匹配规则编号3，报文中包含Option 82，并且该选项的第四个字节的最高位为1。

\<Sysname\> system-view

Sysname dhcp class exam

Sysname-dhcp-class-exam if-match rule 3 option 82 hex 00000080 mask 00000080

\# 配置DHCP用户类exam的匹配规则编号为4，匹配硬件地址0094-0000-0101，硬件掩码长度为ffff-0000-0000。

\<Sysname\> syatem-view

Sysname dhcp class exam

Sysname-dhcp-class-exam if-match rule 4 hardware-address 0094-0000-0101 mask ffff-0000-0000

【相关命令】

·**dhcp class**

**DHCP \-- DHCP服务器配置命令 \-- ip-in-use threshold**

------------------------------------------------------------------------

**[ip-in-use threshold**]命令用来设置地址池使用率告警门限阈值。

**[undo ip-in-use threshold**]命令用来恢复缺省地址池使用率告警门限阈值。

【命令】

**[ip-in-use threshold ***threshold-value*]

**[undo ip-in-use threshold**]

【缺省情况】

地址池使用率告警门限阈值为100%。

【视图】

DHCP地址池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[threshold-value*]：地址池使用率告警阈值，为百分比形式，比如若设置为80，表示地址池使用率超过80%时，系统会生成告警信息发送给信息中心。取值范围为1～100。

【使用指导】

·执行**ip-in-use threshold**命令设置地址池使用率告警阈值，在地址池中地址使用率超过阈值时，系统会生成告警信息提醒管理员进行地址池规划，避免因为地址池中地址资源耗尽，后续用户不能上线。

·在同一个视图下重复执行此命令，新的配置覆盖原有配置。

系统将告警信息发送给信息中心，通过设置信息中心的参数，最终决定日志信息的输出规则（即是否允许输出以及输出方向）。有关信息中心参数配置请参见"网络管理和监控配置指导"中的"信息中心"。

【举例】

\# 配置地址池p1使用率告警门限阈值为85%。

\<Sysname\> system-view

Sysname dhcp server ip-pool p1

Sysname-dhcp-pool-p1 ip-in-use threshold 85

**DHCP \-- DHCP服务器配置命令 \-- nbns-list**

------------------------------------------------------------------------

nbns-list{.commandkeywordsChar}命令用来配置DHCP地址池为DHCP客户端分配的WINS服务器地址。

undo nbns-list{.commandkeywordsChar}命令用来删除DHCP地址池为DHCP客户端分配的WINS服务器地址。

【命令】

nbns-list{.commandkeywordsChar} *ip-address*&\<1-8\>

undo nbns-list {.commandkeywordsChar}[ *ip-address*&\<1-8\> ]

【缺省情况】

没有配置DHCP地址池为DHCP客户端分配的WINS服务器地址。

【视图】

DHCP地址池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*&\<1-8\>]：WINS服务器的IP地址。&\<1-8\>表示最多可以输入8个IP地址，每个IP地址之间用空格分隔。

【使用指导】

·如果多次执行该命令，新的配置会覆盖已有配置。

·执行undo nbns-list{.commandkeywordsChar}命令时，如果没有指定任何参数，则删除DHCP地址池中的所有WINS服务器地址。

【举例】

\# 配置DHCP地址池0为DHCP客户端分配WINS服务器地址为10.1.1.1。

\<Sysname\> system-view

Sysname dhcp server ip-pool 0

Sysname-dhcp-pool-0 nbns-list 10.1.1.1

【相关命令】

·**display dhcp server pool**

·**netbios-type**

**DHCP \-- DHCP服务器配置命令 \-- netbios-type**

------------------------------------------------------------------------

netbios-type{.commandkeywordsChar}命令用来配置DHCP地址池为DHCP客户端分配的NetBIOS节点类型。

undo netbios-type{.commandkeywordsChar}命令用来删除DHCP地址池为DHCP客户端分配的NetBIOS节点类型。

【命令】

**[netbios-type**[ { **b-node** \| **h-node** \| **m-node** \| **p-node** }]]

undo netbios-type

【缺省情况】

没有配置DHCP地址池为DHCP客户端分配的NetBIOS节点类型。

【视图】

DHCP地址池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

b-node{.commandkeywordsChar}：b类节点，"b"代表广播（broadcast），此类节点采用广播方式获取主机名和IP地址之间的映射。源节点通过发送带有目的节点主机名的广播报文来获取目的节点的IP地址，目的节点收到广播报文后，就将自己的IP地址返回给源节点。

h-node{.commandkeywordsChar}：h类节点，"h"代表混合（hybrid），是具备"端到端"通信机制的b类节点。此类节点首先发送单播报文与WINS服务器通信来获取映射关系，如果没有获取到，再发送广播报文来获取映射关系。

m-node{.commandkeywordsChar}：m类节点，"m"代表混合（mixed），是具有部分广播特性的p类节点。此类节点首先发送广播报文来获取映射关系，如果没有获取到，则再发送单播报文与WINS服务器通信来获取映射关系。

p-node{.commandkeywordsChar}：p类节点，"p"代表端到端（peer-to-peer），即此类节点采用发送单播报文与WINS服务器通信的方式获取映射关系。源节点给WINS服务器发送单播报文，WINS服务器收到单播报文后，返回源节点请求的目的节点名所对应的IP地址。

【使用指导】

如果多次执行该命令，新的配置会覆盖已有配置。

【举例】

\# 配置DHCP地址池0为DHCP客户端分配的NetBIOS节点类型为p类节点。

\<Sysname\> system-view

Sysname dhcp server ip-pool 0

Sysname-dhcp-pool-0 netbios-type p-node

【相关命令】

·**display dhcp server pool**

·**nbns-list**

**DHCP \-- DHCP服务器配置命令 \-- network**

------------------------------------------------------------------------

network{.commandkeywordsChar}命令用来配置DHCP地址池动态分配的IP地址网段。

undo network{.commandkeywordsChar}命令用来删除已经创建的用于动态分配的IP地址网段。

【命令】

[[network]{.commandkeywordsChar}[ *network-address* [ *mask-length*{.commandkeywordsChar}\|[ mask]{.commandkeywordsChar} *mask* ]  **export-route**  [ secondary {.commandkeywordsChar}]]]

[[undo network]{.commandkeywordsChar}[ *network-address*{.commandkeywordsChar}[{.commandkeywordsChar}*mask-length*{.commandkeywordsChar}\|[ mask ]{.commandkeywordsChar}*mask*{.commandkeywordsChar}  secondary {.commandkeywordsChar}]]]

【缺省情况】

没有配置动态分配的IP地址网段，即没有可供分配的IP地址。

【视图】

DHCP地址池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[network-address*]：用于动态分配的网段地址。不指定掩码长度和掩码时，表示采用自然掩码。

*[mask-length*]：IP地址的网络掩码长度，取值范围为1～30。

mask{.commandkeywordsChar} *mask*：IP地址的网络掩码，*mask*为点分十进制形式。

**[export-route**]：将网段信息下发给路由管理，由路由管理发布指定网段信息的路由。引导指定网段的下行数据流量。

secondary{.commandkeywordsChar}：指定配置的网段为从网段。如果不指定本参数，则表示配置的网段为主网段。主网段中的地址分配完之后，DHCP服务器可以在从网段中选择地址分配给DHCP客户端。

【使用指导】

执行本命令时如果指定了 secondary{.commandkeywordsChar}参数，则会进入从网段视图。用户可以在该视图下通过gateway-list{.commandkeywordsChar}命令配置为从网段的DHCP客户端分配的网关地址。

需要注意的是：

·每个DHCP地址池中只能配置一个主网段，如果多次执行network{.commandkeywordsChar}命令配置主网段，则新的配置会覆盖已有配置。

·每个DHCP地址池中最多可以配置32个从网段。

·一个DHCP地址池中各个主、从网段的网络号和掩码不能完全相同。

·在地址池下配置了**address range**或**class**命令后，不能再在该地址池下配置从网段。

·修改或删除network{.commandkeywordsChar}配置，会导致该地址池下现有的已分配地址被删除。

·配置**network export-route**命令可以用来发布网段路由，如果多次执行此命令，则新的配置会覆盖已有配置。

【举例】

\# 配置DHCP地址池0动态分配的主地址网段为192.168.8.0/24，从地址网段为192.168.10.0/24。

\<Sysname\> system-view

Sysname dhcp server ip-pool 0

Sysname-dhcp-pool-0 network 192.168.8.0 mask 255.255.255.0

Sysname-dhcp-pool-0 network 192.168.10.0 mask 255.255.255.0 secondary

Sysname-dhcp-pool-0-secondary

【相关命令】

·**display dhcp server pool**

· gateway-list{.commandkeywordsChar}

**DHCP \-- DHCP服务器配置命令 \-- next-server**

------------------------------------------------------------------------

next-server{.commandkeywordsChar}命令用来配置DHCP地址池为DHCP客户端分配的下一个提供服务的服务器IP地址。

undo next-server{.commandkeywordsChar}命令用来删除DHCP地址池为DHCP客户端分配的下一个提供服务的服务器IP地址。

【命令】

next-server{.commandkeywordsChar} *ip-address*

undo next-server

【缺省情况】

没有配置DHCP地址池为DHCP客户端分配的下一个提供服务的服务器IP地址。

【视图】

DHCP地址池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：下一个提供服务的服务器IP地址。

【使用指导】

为DHCP客户端分配的下一个提供服务的服务器IP地址，是在DHCP客户端启动过程中，在获取到IP地址后，用于获取其他启动数据的服务器地址。例如，TFTP服务器地址。

如果多次执行该命令，新的配置会覆盖已有配置。

【举例】

\# 配置DHCP地址池0为DHCP客户端分配的下一个提供服务的服务器IP地址为10.1.1.254。

\<Sysname\> system-view

Sysname dhcp server ip-pool 0

Sysname-dhcp-pool-0 next-server 10.1.1.254

【相关命令】

·**display dhcp server pool**

**DHCP \-- DHCP服务器配置命令 \-- option**

------------------------------------------------------------------------

option{.commandkeywordsChar}命令用来自定义DHCP选项。

undo option{.commandkeywordsChar}命令用来删除自定义的DHCP选项。

【命令】

[[option]{.commandkeywordsChar} *code* {[ ascii {.commandkeywordsChar}*ascii-string* \| hex {.commandkeywordsChar}*hex-string* \| ip-address{.commandkeywordsChar} *ip-address*&\<1-8\> }]]

undo option{.commandkeywordsChar} *code*

【缺省情况】

没有自定义DHCP选项。

【视图】

DHCP地址池视图/DHCP选项组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[code*]：选项的数值，取值范围为2～254，不包括50～54、56、58、59、61和82。

ascii{.commandkeywordsChar} *ascii-string*：指定选项内容为配置的ASCII字符串。*ascii-string*为1～255个字符的ASCII字符串。

hex{.commandkeywordsChar}* hex-string*：指定选项内容为配置的十六进制数串。*hex-string*为十六进制数串，位数的取值范围为2～256之间的偶数。

ip-address{.commandkeywordsChar} *ip-address*&\<1-8\>：指定选项内容为配置的IP地址。&\<1-8\>表示最多可以输入8个IP地址，每个IP地址之间用空格分隔。

【使用指导】

通过执行本命令，可以配置编号为*code*的DHCP选项内容为指定的ASCII字符串、十六进制数串或IP地址，即采用指定的内容来填充DHCP应答报文中编号为*code*的选项，以便将指定的选项内容分配给客户端。

本命令为DHCP服务器提供了灵活的选项配置方式，使得DHCP服务器可以为DHCP客户端提供更加丰富的选项内容。在以下情况下，可以使用本命令自定义DHCP选项：

·随着DHCP的不断发展，新的DHCP选项会陆续出现。通过自定义DHCP选项，可以方便地添加新的DHCP选项。

·有些选项的内容，RFC中没有统一规定。厂商可以根据需要定义选项的内容，如Option 43。通过自定义DHCP选项，可以为DHCP客户端提供厂商指定的信息。

·设备上只提供了有限的选项配置命令（如gateway-list{.commandkeywordsChar}、**dns-list**命令），对于没有专门命令来配置的DHCP选项，可以通过**option**命令配置选项内容。例如，可以通过**option 4[ ip-address 1.1.1.1{.commandkeywordsChar}]**命令指定为DHCP客户端分配的时间服务器地址为1.1.1.1。

·扩展已有的DHCP选项。当前已提供的方式无法满足用户需求时（比如通过**dns-list**命令最多只能配置8个DNS服务器地址，如果用户需要配置的DNS服务器地址数目大于8，则该命令无法满足需求），可以通过自定义DHCP选项的方式进行扩展。

需要注意的是：

·有些DHCP选项既可以通过专门的命令来配置，也可以通过**option**命令来配置。例如，Option 6（DNS服务器地址选项）既可以通过**dns-list**命令配置，也可以通过**option 6**命令配置。如果同时通过上述两种方式配置了这些选项，则在填充DHCP应答报文的选项时，优先选择专门命令的配置。如果没有通过专门命令来配置，则采用**option**命令配置的内容填充选项。

·如果多次执行本命令，并指定相同的选项数值*code*，则新的配置会覆盖已有配置。

·DHCP服务器在应答DHCP客户端报文时，如果DHCP选项组的选项编号和DHCP地址池选项编号相同且匹配用户类时，以DHCP选项组的选项为准。

【举例】

\# 日志服务器选项的编号为7。在DHCP地址池0中配置为DHCP客户端分配的日志服务器地址为2.2.2.2。

\<Sysname\> system-view

Sysname dhcp server ip-pool 0

Sysname-dhcp-pool-0 option 7 ip-address 2.2.2.2

【相关命令】

·**display dhcp server pool**

**DHCP \-- DHCP服务器配置命令 \-- reset dhcp server conflict**

------------------------------------------------------------------------

reset dhcp server conflict{.commandkeywordsChar}命令用来清除DHCP的地址冲突信息。

【命令】

reset dhcp server conflict {.commandkeywordsChar}[[ ip{.commandkeywordsChar} *ip-address*{.commandkeywordsChar}]  **vpn-instance** *vpn-instance-name* ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

ip{.commandkeywordsChar} *ip-address*：清除指定IP地址的冲突信息。如果不指定本参数，则清除所有地址的冲突信息。

**[vpn-instance** *vpn-instance-name*]：清除指定VPN内的地址冲突信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示清除的是公网中的地址冲突信息。

【使用指导】

出现冲突地址，一般是由于网络配置不合理，动态分配的地址和网络中静态配置的地址冲突而产生的。在合理调整网络配置，不再存在冲突的情况后，原来的冲突地址可能不再冲突，可以被重新分配。此时，通过本命令，清除检测到的冲突地址，则该地址可以被重新分配。

【举例】

\# 清除全部地址冲突信息。

\<Sysname\> reset dhcp server conflict

【相关命令】

·**display dhcp server conflict**

**DHCP \-- DHCP服务器配置命令 \-- reset dhcp server expired**

------------------------------------------------------------------------

reset dhcp server expired{.commandkeywordsChar}命令用来清除租约过期的地址绑定信息。

【命令】

[[reset dhcp server expired ]{.commandkeywordsChar}[{.commandkeywordsChar}[[ ip {.commandkeywordsChar}*ip-address* ]  **vpn-instance** *vpn-instance-name*  \| pool{.commandkeywordsChar} *pool-name*{.commandkeywordsChar}]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

ip{.commandkeywordsChar}* ip-address*：清除指定IP地址的租约过期地址绑定信息。

**[vpn-instance** *vpn-instance-name*]：清除指定VPN内的租约过期的地址绑定信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示清除的是公网中的租约过期的地址绑定信息。

pool{.commandkeywordsChar} *pool-name*：清除指定地址池中租约过期的地址绑定信息。*pool-name*表示地址池名称，为1～63个字符的字符串，不区分大小写。

【使用指导】

执行本命令时，如果不指定任何参数，则清除所有租约过期的地址绑定信息。

【举例】

\# 清除所有租约过期的地址绑定信息。

\<Sysname\> reset dhcp server expired

【相关命令】

·**display dhcp server expired**

**DHCP \-- DHCP服务器配置命令 \-- reset dhcp server ip-in-use**

------------------------------------------------------------------------

reset dhcp server ip-in-use{.commandkeywordsChar}命令用来清除DHCP的正式绑定和临时绑定信息。

【命令】

[[reset dhcp server ip-in-use ]{.commandkeywordsChar}[{.commandkeywordsChar}[[ ip{.commandkeywordsChar} *ip-address*{.commandkeywordsChar}]{.commandkeywordsChar} [vpn-instance{.commandkeywordsChar} vpn-instance-name ]{.commandkeywordsChar}\| pool {.commandkeywordsChar}*pool-name*{.commandkeywordsChar}]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

ip{.commandkeywordsChar}* ip-address*：清除指定IP地址的正式绑定和临时绑定信息。

**[vpn-instance** *vpn-instance-name*]：清除指定VPN内的正式绑定和临时绑定信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示清除的是公网中的正式绑定和临时绑定信息。

pool{.commandkeywordsChar} *pool-name*：清除指定地址池的正式绑定和临时绑定信息。*pool-name*表示地址池名称，为1～63个字符的字符串，不区分大小写。

【使用指导】

执行本命令时，如果不指定任何参数，则清除所有的正式绑定和临时绑定信息。

需要注意的是，清除静态正式绑定信息时，将使该绑定信息变为静态无效绑定。

【举例】

\# 清除地址10.110.1.1的正式绑定和临时绑定信息。

\<Sysname\> reset dhcp server ip-in-use ip 10.110.1.1

【相关命令】

·**display dhcp server [ip-in-use{.commandkeywordsChar}]**

**DHCP \-- DHCP服务器配置命令 \-- reset dhcp server statistics**

------------------------------------------------------------------------

reset dhcp server statistics{.commandkeywordsChar}命令用来清除DHCP服务器的统计信息。

【命令】

reset dhcp server statistics {.commandkeywordsChar}[ [vpn-instance{.commandkeywordsChar} vpn-instance-name ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance** *vpn-instance-name*]：清除指定VPN内的DHCP服务器的统计信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示清除的是公网中的DHCP服务器的统计信息。

【举例】

\# 清除DHCP服务器的统计信息。

\<Sysname\> reset dhcp server statistics

【相关命令】

·**display dhcp server statistics**

**DHCP \-- DHCP服务器配置命令 \-- static-bind**

------------------------------------------------------------------------

static-bind{.commandkeywordsChar}命令用来在DHCP地址池中配置静态地址绑定，以便实现DHCP服务器为客户端ID或硬件地址为指定值的客户端分配固定的IP地址。

undo static-bind{.commandkeywordsChar}命令用来删除DHCP地址池中的静态地址绑定。

【命令】

[[static-bind ip-address]{.commandkeywordsChar}[ *ip-address* [{.commandkeywordsChar}*mask-length*{.commandkeywordsChar}\|[ mask ]{.commandkeywordsChar}*mask*{.commandkeywordsChar}] { client-identifier {.commandkeywordsChar}*client-identifier*{.commandkeywordsChar}\| hardware-address {.commandkeywordsChar}*hardware-address*{.commandkeywordsChar}[ ethernet {.commandkeywordsChar}\| token-ring {.commandkeywordsChar}] }]]

**[undo static-bind ip-address** *ip-address*]

【缺省情况】

没有在DHCP地址池中配置静态地址绑定。

【视图】

DHCP地址池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

ip-address{.commandkeywordsChar}* ip-address*：指定静态绑定的IP地址。不指定掩码长度和掩码时，表示采用自然掩码。

*[mask-length*]：静态绑定IP地址的掩码长度，即掩码中连续"1"的个数，取值范围为1～30。

mask {.commandkeywordsChar}*mask*：指定静态绑定IP地址的掩码，*mask*为点分十进制形式。

client-identifier{.commandkeywordsChar}* client-identifier*：指定静态绑定的客户端ID。*client-identifier*表示客户端ID，为4～254个字符的字符串，字符串中只能包括十六进制数和"-"，且形式为H-H-H...，除最后一个H表示2位或4位十六进制数外，其他均表示4位十六进制数。例如：aabb-cccc-dd为有效的ID，aabb-c-dddd和aabb-cc-dddd为无效客户端ID。

hardware-address{.commandkeywordsChar}* hardware-address*：指定静态绑定的客户端硬件地址。*hardware-address*表示客户端硬件地址，为4～39个字符的字符串，字符串中只能包括十六进制数和"-"，且形式为H-H-H...，除最后一个H表示2位或4位十六进制数外，其他均表示4位十六进制数。例如：aabb-cccc-dd为有效的客户端硬件地址，aabb-c-dddd和aabb-cc-dddd为无效的客户端硬件地址。

ethernet{.commandkeywordsChar}：指定客户端硬件地址类型为以太网，缺省为以太网类型。

token-ring{.commandkeywordsChar}：指定客户端硬件地址类型为令牌环网。

【使用指导】

·静态绑定的IP地址不能是DHCP服务器的接口IP地址，否则会导致IP地址冲突，被绑定的客户端将无法正常获取到IP地址。

·同一地址池下可以配置多个静态地址绑定。所有地址池下配置的静态地址绑定一共不能超过8192个。

·同一地址只能绑定给一个客户端。不允许通过重复执行本命令的方式修改IP地址与客户端的绑定关系。只有删除了某个地址的绑定关系，才能将该地址与其他客户端绑定。

【举例】

\# 在DHCP地址池0中配置：为客户端ID为00aa-aabb的客户端，固定分配IP地址10.1.1.1/24。

\<Sysname\> system-view

Sysname dhcp server ip-pool 0

Sysname-dhcp-pool-0 static-bind ip-address 10.1.1.1 mask 255.255.255.0 client-identifier 00aa-aabb

【相关命令】

·**display dhcp server pool**

**DHCP \-- DHCP服务器配置命令 \-- tftp-server domain-name**

------------------------------------------------------------------------

tftp-server domain-name{.commandkeywordsChar}命令用来配置DHCP地址池为DHCP客户端分配的TFTP服务器域名。

undo tftp-server domain-name{.commandkeywordsChar}命令用来删除DHCP地址池为DHCP客户端分配的TFTP服务器域名。

【命令】

tftp-server domain-name{.commandkeywordsChar}* domain-name*

undo tftp-server domain-name

【缺省情况】

没有配置DHCP地址池为DHCP客户端分配的TFTP服务器域名。

【视图】

DHCP地址池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[domain-name*]：TFTP服务器域名，为1～63个字符的字符串，区分大小写。

【使用指导】

如果多次执行该命令，新的配置会覆盖已有配置。

【举例】

\# 配置DHCP地址池0为DHCP客户端分配的TFTP服务器域名为aaa。

\<Sysname\> system-view

Sysname dhcp server ip-pool 0

Sysname-dhcp-pool-0 tftp-server domain-name aaa

【相关命令】

·{.commandkeywordsChar}**display dhcp server pool**

· tftp-server ip-address{.commandkeywordsChar}

**DHCP \-- DHCP服务器配置命令 \-- tftp-server ip-address**

------------------------------------------------------------------------

tftp-server ip-address{.commandkeywordsChar}命令用来配置DHCP地址池为DHCP客户端分配的TFTP服务器地址。undo tftp-server ip-address{.commandkeywordsChar}命令用来删除DHCP地址池为DHCP客户端分配的TFTP服务器地址。

【命令】

tftp-server ip-address{.commandkeywordsChar}* ip-address*

undo tftp-server ip-address

【缺省情况】

没有配置DHCP地址池为DHCP客户端分配的TFTP服务器地址。

【视图】

DHCP地址池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：TFTP服务器的IP地址。

【使用指导】

如果多次执行该命令，新的配置会覆盖已有配置。

【举例】

\# 配置DHCP地址池0为DHCP客户端分配的TFTP服务器地址为10.1.1.1。

\<Sysname\> system-view

Sysname dhcp server ip-pool 0

Sysname-dhcp-pool-0 tftp-server ip-address 10.1.1.1

【相关命令】

·{.commandkeywordsChar}**display dhcp server pool**

·{.commandkeywordsChar}[tftp-server domain-name]{.commandkeywordsChar}

**DHCP \-- DHCP服务器配置命令 \-- valid class**

------------------------------------------------------------------------

**[valid class**]命令用来配置DHCP白名单包括的用户类名。

**[undo valid class**]命令用来删除DHCP白名单中包括的用户类名。

【命令】

**[valid class ***class-name*&\<1-8\>]

**[undo valid class ***class-name*&\<1-8\>]

【缺省情况】

未配置DHCP白名单包括的用户类。

【视图】

DHCP地址池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[class-name*&\<1-8\>]：DHCP白名单包括的用户类名列表。其中*class-name*为DHCP用户类名，为1～63个字符的字符串，不区分大小写。&\<1-8\>代表最多可以输入8个用户类名，每个用户类名之间用空格分隔。

【使用指导】

在配置了DHCP地址池用户白名单功能后，DHCP服务器才会检查用户是否属于白名单包括的用户类。

【举例】

\# 在DHCP地址池0中配置DHCP白名单包括的用户类名为test1和test2。

\<Sysname\> system-view

Sysname dhcp server ip-pool 0

Sysname-dhcp-pool-0 valid class test1 test2

【相关命令】

·**dhcp class**

·**verify class**

**DHCP \-- DHCP服务器配置命令 \-- verify class**

------------------------------------------------------------------------

**[verify class**]命令用来开启DHCP用户类白名单功能。

**[undo verify class**]命令用来关闭DHCP用户类白名单功能。

【命令】

**[verify class**]

**[undo verify class**]

【缺省情况】

DHCP用户类白名单功能处于关闭状态。

【视图】

DHCP地址池视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在开启了DHCP用户类白名单功能后，DHCP服务器才会检查用户是否属于白名单包括的用户类。

需要注意的是，DHCP用户类白名单功能对获取静态绑定租约的客户端不生效。

【举例】

\# 在DHCP地址池0中开启DHCP用户类白名单功能。

Sysname syatem-view

Sysname dhcp server ip-pool 0

Sysname-dhcp-pool-0 verify class

【相关命令】

·**valid class ***class-name*&\<1-8\>

**DHCP \-- DHCP服务器配置命令 \-- voice-config**

------------------------------------------------------------------------

voice-config{.commandkeywordsChar}命令用来配置DHCP地址池为DHCP客户端分配的Option 184内容。

undo voice-config{.commandkeywordsChar}命令用来删除DHCP地址池为DHCP客户端分配的Option 184内容。

【命令】

[[voice-config ]{.commandkeywordsChar}{[ as-ip{.commandkeywordsChar} *ip-address*{.commandkeywordsChar}\| fail-over {.commandkeywordsChar}*ip-address* *dialer-string*{.commandkeywordsChar}\| ncp-ip{.commandkeywordsChar} *ip-address*{.commandkeywordsChar}\| voice-vlan {.commandkeywordsChar}*vlan-id*{.commandkeywordsChar}{ disable {.commandkeywordsChar}\| enable {.commandkeywordsChar}} }]]

**[undo voice-config**[ [ **as-ip** \| **fail-over** \| **ncp-ip** \| **voice-vlan** ]]]

【缺省情况】

没有配置DHCP地址池为DHCP客户端分配的Option 184内容。

【视图】

DHCP地址池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

as-ip {.commandkeywordsChar}*ip-address*：指定备用服务器的IP地址。

fail-over{.commandkeywordsChar}* ip-address dialer-string*：指定自动故障转移IP地址及呼叫字符串。*dialer-string*为1～39个字符的字符串，字符可以是数字0～9及"\*"。

ncp-ip {.commandkeywordsChar}*ip-address*：指定网络呼叫处理器的IP地址。

voice-vlan {.commandkeywordsChar}*vlan-id*：指定语音VLAN的ID。*vlan-id*取值范围为2～4094。

· disable{.commandkeywordsChar}：指定VLAN处于禁止状态，即DHCP客户端不会将所指定的VLAN ID作为语音VLAN。

· enable{.commandkeywordsChar}：指定VLAN处于开启状态，即DHCP客户端会将所指定的VLAN ID作为语音VLAN。

【使用指导】

如果多次执行本命令，为同一个参数配置不同的值，则新的配置会覆盖已有配置。

【举例】

\# 为DHCP地址池0指定Option 184的内容：网络呼叫处理器的IP地址为10.1.1.1，备用服务器的IP地址为10.2.2.2，语音VLAN的ID为3，为开启状态，自动故障转移IP地址为10.3.3.3，呼叫字符串为99\*。

\<Sysname\> system-view

Sysname dhcp server ip-pool 0

Sysname-dhcp-pool-0 voice-config ncp-ip 10.1.1.1

Sysname-dhcp-pool-0 voice-config as-ip 10.2.2.2

Sysname-dhcp-pool-0 voice-config voice-vlan 3 enable

Sysname-dhcp-pool-0 voice-config fail-over 10.3.3.3 99\*

【相关命令】

·**display dhcp server pool**

**DHCP \-- DHCP服务器配置命令 \-- vpn-instance**

------------------------------------------------------------------------

**[vpn-instance**]命令用来指定DHCP服务器上的地址池所在的VPN信息。

**[undo vpn-instance**]命令用来删除指定的DHCP服务器上的地址池所在的VPN信息。

【命令】

**[vpn-instance** *vpn-instance-name*]

**[undo vpn-instance**]

【缺省情况】

未指定DHCP服务器上的地址池所在的VPN信息。

【视图】

DHCP地址池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vpn-instance-name*]：指定DHCP地址池所属的VPN实例名称。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示地址池属于公网。

【使用指导】

当地址池绑定了VPN实例后，DHCP服务器可以将网络划分成公网和VPN私网。没有配置VPN属性的地址池被划分到公网，配置了VPN属性的地址池被划分到相应的VPN私网，这样，对于处于公网或VPN私网中的客户端，服务器都能够选择合适的地址池来为客户端分配租约并且记录该客户端的状态信息。

DHCP客户端的VPN信息可以从认证模块（如IPoE）获取，也可以从DHCP服务器接收报文的接口配置的VPN信息获取。如果以上两种方式都可获取VPN信息，以从认证模块获取的VPN信息为准。

【举例】

\# 指定DHCP地址池0所在的VPN编号为abc。

\<Sysname\> system-view

Sysname dhcp server ip-pool 0

Sysname-dhcp-pool-0 vpn-instance abc

**DHCP \-- DHCP中继配置命令 \-- dhcp relay check mac-address**

------------------------------------------------------------------------

dhcp relay check mac-address{.commandkeywordsChar}命令用来启用DHCP中继的MAC地址检查功能。

undo dhcp relay check mac-address{.commandkeywordsChar}命令用来关闭DHCP中继的MAC地址检查功能。

【命令】

dhcp relay check mac-address

undo dhcp relay check mac-address

【缺省情况】

DHCP中继的MAC地址检查功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

启用该功能后，DHCP中继检查接收到的DHCP请求报文中的chaddr字段和数据帧的源MAC地址字段是否一致。如果一致，则认为该报文合法，将其转发给DHCP服务器；如果不一致，则丢弃该报文。

需要注意的是：

·只有在接口上配置**dhcp select relay**后，DHCP中继的MAC地址检查功能才会生效。

·由于DHCP中继转发DHCP报文时会修改报文的源MAC地址，所以只能在靠近DHCP客户端的第一跳DHCP中继设备上启用MAC地址检查功能。在非第一跳DHCP中继设备上启用MAC地址检查功能，会使DHCP中继设备错误的丢弃报文，导致客户端地址申请不成功。

【举例】

·路由应用

\# 启用DHCP中继的MAC地址检查功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dhcp relay check mac-address

·交换应用

\# 启用DHCP中继的MAC地址检查功能。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 dhcp relay check mac-address

【相关命令】

·**dhcp select relay**

**DHCP \-- DHCP中继配置命令 \-- dhcp relay check mac-address aging-time**

------------------------------------------------------------------------

**[dhcp relay check mac-address aging-time**]命令用来配置DHCP中继的MAC地址检查表项的老化时间。

**[undo dhcp relay check mac-address aging-time**]命令用来恢复缺省情况。

【命令】

**[dhcp relay check mac-address aging-time** *time*]

**[undo dhcp relay check mac-address aging-time**]

【缺省情况】

MAC地址检查表项的老化时间为30秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

如果未通过**dhcp relay check mac-address**命令启用DHCP中继的MAC地址检查功能，则本命令的配置不会生效。

【参数】

*[time*]：DHCP中继的MAC地址检查表项的老化时间，取值范围为30～600，单位为秒。

【举例】

\# 配置DHCP中继的MAC地址检查表项的老化时间为60秒。

\<Sysname\> system-view

Sysname dhcp relay check mac-address aging-time 60

**DHCP \-- DHCP中继配置命令 \-- dhcp relay client-information record**

------------------------------------------------------------------------

dhcp relay client-information record{.commandkeywordsChar}命令用来开启DHCP中继用户地址表项记录功能。

undo dhcp relay client-information record{.commandkeywordsChar}命令用来关闭DHCP中继用户地址表项记录功能。

【命令】

dhcp relay client-information record

undo dhcp relay client-information record

【缺省情况】

DHCP中继用户地址表项记录功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

关闭DHCP中继用户地址表项记录功能时，会删除DHCP中继上记录的全部地址表项。

当DHCP中继作为DHCP客户端的网关设备时，才会记录此DHCP客户端的地址表项。

【举例】

\# 开启DHCP中继用户地址表项记录功能。

\<Sysname\> system-view

Sysname dhcp relay client-information record

【相关命令】

·**dhcp relay client-information refresh**

·**dhcp relay client-information refresh enable**

**DHCP \-- DHCP中继配置命令 \-- dhcp relay client-information refresh**

------------------------------------------------------------------------

dhcp relay client-information refresh{.commandkeywordsChar}命令用来配置DHCP中继动态用户地址表项的定时刷新周期。

undo dhcp relay client-information refresh{.commandkeywordsChar}命令用来恢复缺省情况。

【命令】

[[dhcp relay client-information refresh ]{.commandkeywordsChar}[[ auto {.commandkeywordsChar}\| interval {.commandkeywordsChar}*interval*{.commandkeywordsChar}]]]

undo dhcp relay client-information refresh

【缺省情况】

定时刷新周期为 auto{.commandkeywordsChar}，即根据表项的数目自动计算刷新时间间隔。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

auto{.commandkeywordsChar}：指定根据表项的数目自动计算刷新时间间隔。表项越多，刷新时间间隔越短，但最短时间间隔不会小于50毫秒。

**[interval*** interval*]：刷新时间间隔，取值范围为1～120，单位为秒。

【使用指导】

如果多次执行该命令，新的配置会覆盖已有配置。

【举例】

\# 配置DHCP中继动态用户地址表项的刷新时间间隔为100秒。

\<Sysname\> system-view

Sysname dhcp relay client-information refresh interval 100

【相关命令】

·**dhcp relay client-information record**

·**dhcp relay client-information refresh enable**

**DHCP \-- DHCP中继配置命令 \-- dhcp relay client-information refresh enable**

------------------------------------------------------------------------

dhcp relay client-information refresh enable{.commandkeywordsChar}命令用来开启DHCP中继动态用户地址表项定时刷新功能。

undo dhcp relay client-information refresh enable{.commandkeywordsChar}命令用来关闭DHCP中继动态用户地址表项定时刷新功能。

【命令】

dhcp relay client-information refresh enable

undo dhcp relay client-information refresh enable

【缺省情况】

DHCP中继动态用户地址表项定时刷新功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

DHCP客户端释放动态获取的IP地址时，会向DHCP服务器单播发送DHCP-RELEASE报文，DHCP中继不会处理该报文的内容。如果此时DHCP中继上记录了该IP地址与MAC地址的绑定关系，则会造成DHCP中继的用户地址表项无法实时刷新。为了解决这个问题，DHCP中继支持动态用户地址表项的定时刷新功能。

DHCP中继动态用户地址表项定时刷新功能开启时，DHCP中继每隔指定时间采用客户端获取到的IP地址和DHCP中继接口的MAC地址向DHCP服务器发送DHCP-REQUEST报文：

·如果DHCP中继接收到DHCP服务器响应的DHCP-ACK报文或在指定时间内没有接收到DHCP服务器的响应报文，则表明这个IP地址已经可以进行分配，DHCP中继会删除动态用户地址表中对应的表项，为了避免地址浪费，DHCP中继收到DHCP-ACK报文后，会发送DHCP-RELEASE报文释放申请到的IP地址。

·如果DHCP中继接收到DHCP服务器响应的DHCP-NAK报文，则表示该IP地址的绑定信息仍然存在，DHCP中继不会删除该IP地址对应的表项。

需要注意的是，关闭DHCP中继动态用户地址表项定时刷新功能时，DHCP中继上记录的用户地址表项不会自动老化。DHCP客户端释放申请到的IP地址后，需要用户执行reset dhcp relay client-information{.commandkeywordsChar}命令删除DHCP中继上对应的用户地址表项。

【举例】

\# 关闭DHCP中继动态用户地址表项定时刷新功能。

\<Sysname\> system-view

Sysname undo dhcp relay client-information refresh enable

【相关命令】

·**dhcp relay client-information record**

·**dhcp relay client-information refresh**

·{.commandkeywordsChar}[reset dhcp relay client-information]{.commandkeywordsChar}

**DHCP \-- DHCP中继配置命令 \-- dhcp relay gateway**

------------------------------------------------------------------------

dhcp relay gateway{.commandkeywordsChar}命令用来配置DHCP中继为DHCP客户端分配的网关地址。

undo dhcp relay gateway{.commandkeywordsChar}命令用来恢复缺省情况。

【命令】

dhcp relay gateway {.commandkeywordsChar}ip-address

undo dhcp relay gateway{.commandkeywordsChar}

【缺省情况】

DHCP中继分配接口下主IP地址作为DHCP客户端的网关地址。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：指定为DHCP客户端分配的网关IP地址。

【使用指导】

·在接口视图下配置此命令后，中继会使用此命令配置的地址作为客户端的网关地址。

·如果多次执行此命令，新的配置会覆盖已有配置。

·配置的网关地址必须属于该命令行所在的接口。

【举例】

·路由应用

\# 在接口GigabitEthernet 1/0/1上配置为DHCP客户端分配的网关地址为10.1.1.1。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dhcp relay gateway 10.1.1.1

·交换应用

\# 在VLAN接口2上配置为DHCP客户端分配的网关地址为10.1.1.1。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 dhcp relay gateway 10.1.1.1

【相关命令】

·**gateway-list**

**DHCP \-- DHCP中继配置命令 \-- dhcp relay information circuit-id**

------------------------------------------------------------------------

dhcp relay information circuit-id{.commandkeywordsChar}命令用来配置Option 82的Circuit ID子选项的填充模式和填充格式。

undo dhcp relay information circuit-id{.commandkeywordsChar}命令用来恢复缺省情况。

【命令】

[[dhcp relay information circuit-id ]{.commandkeywordsChar}{[ bas {.commandkeywordsChar}\| string{.commandkeywordsChar} *circuit-id*{.commandkeywordsChar}\|{.commandkeywordsChar}{ normal {.commandkeywordsChar}\| verbose {.commandkeywordsChar}[ node-identifier {.commandkeywordsChar}{ mac {.commandkeywordsChar}\| sysname {.commandkeywordsChar}\| user-defined{.commandkeywordsChar} *node-identifier*{.commandkeywordsChar}}{.commandkeywordsChar}]  **interface**  }{.commandkeywordsChar}[ format {.commandkeywordsChar}{ ascii {.commandkeywordsChar}\| hex {.commandkeywordsChar}} ] }]]

undo dhcp relay information circuit-id{.commandkeywordsChar}

【缺省情况】

Option 82的Circuit ID子选项的填充模式为Normal，填充格式为hex。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[bas**]：表示支持使用电信格式的填充Circuit子选项。

string{.commandkeywordsChar} *circuit-id*：指定以用户配置的字符串填充Circuit ID子选项。*circuit-id*表示用户配置的用来填充Circuit ID子选项的内容，为3～63个字符的字符串，区分大小写。

normal{.commandkeywordsChar}：指定以Normal模式填充Circuit ID子选项，填充内容为VLAN ID和端口号。

verbose{.commandkeywordsChar}：指定以Verbose模式填充Circuit ID子选项。填充的内容为节点标识、接口信息和接口所在的VLAN编号。节点标识默认以节点的MAC地址构成；接口信息默认由以太网类型（取值固定为"eth"）、框号、槽号、子槽号和接口编号组成。

[[node-identifier ]{.commandkeywordsChar}{[ mac {.commandkeywordsChar}\| sysname {.commandkeywordsChar}\| user-defined{.commandkeywordsChar} *node-identifier* }]]：指定接入节点标识。

· mac{.commandkeywordsChar}：表示以节点的MAC地址作为节点标识。

· sysname{.commandkeywordsChar}：表示以节点的设备名称作为节点标识。设备的系统名称可以通过系统视图下的**sysname**命令配置。不管配置了哪种填充格式，设备的系统名称始终采用ASCII码格式填充。

· user-defined{.commandkeywordsChar}* node-identifier*：表示以指定的字符串作为节点标识，*node-identifier*为1～50个字符的字符串，区分大小写。不管配置了哪种填充格式，指定的字符串始终采用ASCII码格式填充。

**[interface**]：表示以接口名构成接口信息，始终采用ASCII码格式填充。

format{.commandkeywordsChar}：指定Circuit ID子选项的填充格式。

ascii{.commandkeywordsChar}：指定以ASCII码格式填充Circuit ID子选项，即将数值转换为对应的ASCII码填充到Circuit ID子选项。

hex{.commandkeywordsChar}：指定以十六进制数值的格式填充Circuit ID子选项。

【使用指导】

以不同模式填充Circuit ID子选项时，填充格式有所不同：

·以用户配置的字符串填充Circuit ID子选项时，填充格式固定为ASCII码格式；

·以Normal和Verbose模式填充Circuit ID子选项时，填充格式由本命令的配置决定。

需要注意的是：

·如果本命令中未指定填充格式，则对于Normal模式，VLAN ID和端口号均以hex格式填充；对于Verbose模式，节点标识（MAC地址、设备的系统名称或指定的字符串）、以太网类型、框号、槽号、子槽号、接口编号均以ASCII码格式填充，VLAN ID以hex格式填充。

·如果本命令中指定填充格式为**ascii**，则所有内容均以ASCII码格式填充。

·如果本命令中指定填充格式为hex{.commandkeywordsChar}，则对于Normal模式，VLAN ID和端口号均以hex格式填充；对于Verbose模式，设备的节点标识、以太网类型以ASCII码格式填充，其余内容均以hex格式填充。

·如果以设备的系统名称（**sysname**）作为节点标识填充DHCP报文的Option 82，则系统名称中不能包含空格；否则，DHCP中继添加或替换Option 82失败。

·Option 82的Circuit ID子选项信息中无法携带携带接口拆分信息或子接口信息，关于"接口拆分"和"子接口"的详细介绍，请参见"以太网接口配置指导"中的"以太网接口通用配置"。

·如果多次执行该命令，新的配置会覆盖已有配置。

【举例】

·路由应用

\# 配置以Verbose模式填充Option 82的Circuit ID子选项，节点标识为设备的系统名称，填充格式为ASCII码格式。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dhcp relay information enable

Sysname-GigabitEthernet1/0/1 dhcp relay information strategy replace

Sysname-GigabitEthernet1/0/1 dhcp relay information circuit-id verbose node-identifier sysname format ascii

·交换应用

\# 配置以Verbose模式填充Option 82的Circuit ID子选项，节点标识为设备的系统名称，填充格式为ASCII码格式。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 dhcp relay information enable

Sysname-Vlan-interface10 dhcp relay information strategy replace

Sysname-Vlan-interface10 dhcp relay information circuit-id verbose node-identifier sysname format ascii

【相关命令】

·**dhcp relay information enable**

·**dhcp relay information strategy**

·**display dhcp relay information**

**DHCP \-- DHCP中继配置命令 \-- dhcp relay information enable**

------------------------------------------------------------------------

dhcp relay information enable{.commandkeywordsChar}命令用来启用DHCP中继支持Option 82功能。

undo dhcp relay information enable{.commandkeywordsChar}命令用来关闭DHCP中继支持Option 82功能。

【命令】

dhcp relay information enable

undo dhcp relay information enable

【缺省情况】

DHCP中继支持Option 82功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

启用DHCP中继支持Option 82功能后，DHCP中继将向转发给DHCP服务器的请求报文中增加Option 82选项。选项内容由**dhcp relay information circuit-id**命令和**dhcp relay information remote-id**命令决定。如果DHCP中继收到的请求报文中已经包含Option 82选项，则按照**dhcp relay information strategy**命令配置的策略处理请求报文。

关闭DHCP中继支持Option 82功能后，DHCP中继不会向转发给DHCP服务器的请求报文中增加Option 82选项，也不检查收到的请求报文中是否包含Option 82选项。

【举例】

·路由应用

\# 启用DHCP中继支持Option 82功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dhcp relay information enable

·交换应用

\# 启用DHCP中继支持Option 82功能。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 dhcp relay information enable

【相关命令】

·**dhcp relay information circuit-id**

·**dhcp relay information remote-id**

·**dhcp relay information strategy**

·**display dhcp relay information**

**DHCP \-- DHCP中继配置命令 \-- dhcp relay information remote-id**

------------------------------------------------------------------------

dhcp relay information remote-id{.commandkeywordsChar}命令用来配置Option 82的Remote ID子选项的填充模式和填充格式。

undo dhcp relay information remote-id{.commandkeywordsChar}命令用来恢复缺省情况。

【命令】

[[dhcp relay information remote-id ]{.commandkeywordsChar}{[ normal {.commandkeywordsChar}[ format {.commandkeywordsChar}{ ascii {.commandkeywordsChar}\| hex{.commandkeywordsChar} } ] \| string{.commandkeywordsChar} *remote-id* \| sysname {.commandkeywordsChar}}]]

undo dhcp relay information remote-id

【缺省情况】

Option 82的Remote ID子选项的填充模式为Normal、填充格式为hex。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

normal{.commandkeywordsChar}：指定以Normal模式填充Remote ID子选项，填充内容为接收报文接口的MAC地址。

format{.commandkeywordsChar}：指定Remote ID子选项的填充格式。如果没有配置，则以hex格式填充。

ascii{.commandkeywordsChar}：指定以ASCII码格式填充Remote ID子选项，即将数值转换为对应的ASCII码填充到Remote ID子选项。

hex{.commandkeywordsChar}：指定以十六进制数值的格式填充Remote ID子选项。

string{.commandkeywordsChar}* remote-id*：指定以用户配置的字符串填充Remote ID子选项。*remote-id*表示用户配置的用来填充Remote ID子选项的内容，为1～63个字符的字符串，区分大小写。

sysname{.commandkeywordsChar}：指定以设备的系统名称填充Remote ID子选项。设备的系统名称可以通过系统视图下的**sysname**命令配置。

【使用指导】

以用户配置的字符串（**string**）和设备的系统名称（sysname{.commandkeywordsChar}）填充Remote ID子选项时，填充内容固定为ASCII格式；以Normal模式填充Remote ID子选项时，填充内容的格式由本命令配置的填充格式决定。

需要注意的是，如果多次执行本命令，新的配置会覆盖已有配置。

【举例】

·路由应用

\# 配置采用字符串device001填充Option 82的Remote ID子选项。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dhcp relay information enable

Sysname-GigabitEthernet1/0/1 dhcp relay information strategy replace

Sysname-GigabitEthernet1/0/1 dhcp relay information remote-id string device001

·交换应用

\# 配置采用字符串device001填充Option 82的Remote ID子选项。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 dhcp relay information enable

Sysname-Vlan-interface10 dhcp relay information strategy replace

Sysname-Vlan-interface10 dhcp relay information remote-id string device001

【相关命令】

·**dhcp relay information enable**

·**dhcp relay information strategy**

·**display dhcp relay information**

**DHCP \-- DHCP中继配置命令 \-- dhcp relay information strategy**

------------------------------------------------------------------------

dhcp relay information strategy{.commandkeywordsChar}命令用来配置DHCP中继对包含Option 82的请求报文的处理策略。

undo dhcp relay information strategy{.commandkeywordsChar}命令用来恢复缺省情况。

【命令】

**[dhcp relay information strategy**[ { **drop** \| **keep** \| **replace** }]]

undo dhcp relay information strategy

【缺省情况】

DHCP中继对带有Option 82的请求报文的处理策略为**replace**。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

drop{.commandkeywordsChar}：如果报文中带有Option 82，则丢弃该报文。

keep{.commandkeywordsChar}：如果报文中带有Option 82，则保持该报文中的Option 82不变并进行转发。

replace{.commandkeywordsChar}：如果报文中带有Option 82，则按照配置的填充内容和填充格式填充Option 82，用该选项替换报文中原有的Option 82，并进行转发。

【使用指导】

本命令仅对包含Option 82的请求报文有效。

如果启用了DHCP中继支持Option 82功能，则对于接收到的不包含Option 82的请求报文，DHCP中继的处理方式始终为在请求报文中添加Option 82，并转发给DHCP服务器。

DHCP中继对包含Option 82请求报文的处理策略为**replace**时，需要配置Option 82的填充模式和填充格式；处理策略为**keep**或**drop**时，不需要配置Option 82选项的填充模式和填充格式。

【举例】

·路由应用

\# 配置接收到的请求报文中带有Option 82时，DHCP中继保持该报文中的Option 82不变并进行转发。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dhcp relay information enable

Sysname-GigabitEthernet1/0/1 dhcp relay information strategy keep

·交换应用

\# 配置接收到的请求报文中带有Option 82时，DHCP中继保持该报文中的Option 82不变并进行转发。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 dhcp relay information enable

Sysname-Vlan-interface10 dhcp relay information strategy keep

【相关命令】

·**dhcp relay information enable**

·**display dhcp relay information**

**DHCP \-- DHCP中继配置命令 \-- dhcp relay release ip**

------------------------------------------------------------------------

dhcp relay release ip{.commandkeywordsChar}命令用来配置向DHCP服务器请求释放客户端申请到的IP地址。

【命令】

dhcp relay release ip {.commandkeywordsChar}*client-ip* [ [vpn-instance{.commandkeywordsChar} *vpn-instance-name* ]]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[client-ip*]：请求释放的DHCP客户端IP地址。

vpn-instance{.commandkeywordsChar}* vpn-instance-name*：指定需要释放的IP地址所属的VPN。{.MsoCommentReference}*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则表示释放公网IP地址。

【使用指导】

如果DHCP中继上存在客户端IP地址对应的动态用户地址表项，则配置通过DHCP中继释放该客户端IP地址后，DHCP中继会主动向DHCP服务器发送DHCP-RELEASE报文。DHCP服务器收到该报文后，将会释放指定IP地址的绑定信息。DHCP中继也会删除该动态用户地址表项。

【举例】

\# 向DHCP服务器请求释放客户端申请到的IP地址1.1.1.1。

\<Sysname\> system-view

Sysname dhcp relay release ip 1.1.1.1

**DHCP \-- DHCP中继配置命令 \-- dhcp relay server-address**

------------------------------------------------------------------------

dhcp relay server-address{.commandkeywordsChar}命令用来在DHCP中继上指定DHCP服务器的地址。

undo dhcp relay server-address{.commandkeywordsChar}命令用来在DHCP中继上删除指定DHCP服务器的地址。

【命令】

dhcp relay server-address{.commandkeywordsChar} *ip-address*

undo dhcp relay server-address {.commandkeywordsChar}[{.commandkeywordsChar}*ip-address* ]

【缺省情况】

没有在DHCP中继上指定DHCP服务器的地址。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：DHCP服务器的IP地址。DHCP中继将DHCP客户端发送的报文转发到该地址。

【使用指导】

·指定的DHCP服务器IP地址不能与DHCP中继的接口IP地址在同一网段。否则，可能导致客户端无法获得IP地址。

·通过多次执行[dhcp relay server-address]{.commandkeywordsChar}命令可以指定多个DHCP服务器地址。一个接口上最多可以指定8个DHCP服务器地址。DHCP中继接收到DHCP客户端发送的报文后，将其转发给所有的DHCP服务器。

·执行[undo dhcp relay server-address]{.commandkeywordsChar}命令时，如果没有指定*ip-address*参数，则删除接口上的所有DHCP服务器地址。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上为DHCP中继指定DHCP服务器的地址为1.1.1.1。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dhcp relay server-address 1.1.1.1

·交换应用

\# 在VLAN接口10上为DHCP中继指定DHCP服务器的地址为1.1.1.1。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 dhcp relay server-address 1.1.1.1

【相关命令】

·**dhcp select relay**

·**display dhcp relay interface**

**DHCP \-- DHCP中继配置命令 \-- display dhcp relay check mac-address**

------------------------------------------------------------------------

**[display dhcp relay check mac-address**]命令用来显示DHCP中继的MAC地址检查表项。

【命令】

**[display dhcp relay check mac-address**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# DHCP中继的MAC地址检查表项。

\<Sysname\> display dhcp relay check mac-address

Source-MAC        Interface                 Aging-time

23f3-1122-adf1    GE1/0/1                   10

23f3-1122-2230    GE1/0/2                   30

表1-8 display dhcp relay check mac-address命令显示信息描述表

字段

描述

Source MAC

检测到攻击的源MAC地址

Interface

攻击来源的接口

Aging-time

DDOS攻击检测表项剩余时间，单位为秒

**DHCP \-- DHCP中继配置命令 \-- display dhcp relay client-information**

------------------------------------------------------------------------

display dhcp relay client-information{.commandkeywordsChar}命令用来显示DHCP中继的用户地址表项信息。

【命令】

[[display dhcp relay client-information ]{.commandkeywordsChar}[ [interface{.commandkeywordsChar} *interface-type interface-number*{.commandkeywordsChar}\| ip{.commandkeywordsChar} *ip-address*{.commandkeywordsChar} [vpn-instance{.commandkeywordsChar} *vpn-instance-name* ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

interface{.commandkeywordsChar} *interface-type interface-number*：显示指定接口上的用户地址表项信息。*interface-type interface-number*为接口类型和接口编号。

ip{.commandkeywordsChar} *ip-address*：显示指定IP地址的用户地址表项信息。

vpn-instance{.commandkeywordsChar} *vpn-instance-name*：显示指定VPN内指定IP地址的用户地址表项信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名，为1～31个字符的字符串，区分大小写。

【使用指导】

·只有执行**dhcp relay client-information record**命令后，DHCP中继才会记录用户地址表项信息。

·执行本命令时，如果没有指定任何参数，则显示所有DHCP中继的用户地址表项信息。

【举例】

\# 显示所有DHCP中继的用户地址表项信息。

\<Sysname\> display dhcp relay client-information

Total number of client-information items: 2

Total number of dynamic items: 1

Total number of temporary items: 1

IP address       MAC address      Type        Interface            VPN name

10.1.1.1         00e0-0000-0001   Dynamic     GE1/0/1              VPN1

10.1.1.5         00e0-0000-0000   Temporary   Vlan2                VPN2

表1-9 display dhcp relay client-information命令显示信息描述表

字段

描述

Total number of client-information items

用户地址信息条目总数

Total number of dynamic items

动态用户地址条目总数

Total number of temporary items

临时用户地址条目总数

IP address

DHCP客户端的IP地址

MAC address

DHCP客户端的MAC地址

Type

用户地址表项的取值包括：

·Dynamic：动态用户地址表项，接收到DHCP服务器对DHCP客户端REQUEST请求的ACK应答后，创建的用户表项

·Temporary：临时用户地址表项，接收DHCP客户端的REQUEST请求，但未收到DHCP服务器ACK应答时，创建的用户表项

Interface

与DHCP客户端相连的三层接口。如果用户地址表项中没有记录接口，则显示为"N/A"

VPN name

VPN实例名称，如果表项不属于任何VPN，则显示为"N/A"

【相关命令】

·**dhcp relay client-information record**

· reset dhcp relay client-information{.commandkeywordsChar}

**DHCP \-- DHCP中继配置命令 \-- display dhcp relay information**

------------------------------------------------------------------------

display dhcp relay information{.commandkeywordsChar}命令用来显示DHCP中继上的Option 82配置信息。

【命令】

display dhcp relay information{.commandkeywordsChar} [[ interface{.commandkeywordsChar} *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

interface{.commandkeywordsChar}* interface-type interface-number*：显示指定接口上的Option 82配置信息。*interface-type interface-number*为接口类型和接口编号。如果不指定本参数，则显示所有接口上的Option 82配置信息。

【举例】

\# 显示所有接口上的Option 82配置信息。

\<Sysname\> display dhcp relay information

Interface: Vlan-interface100

   Status: Enable

   Strategy: Replace

   Circuit ID Pattern: Verbose

   Remote ID Pattern: Sysname

   Circuit ID format: Undefined

   Remote ID format: ASCII

   Node identifier: aabbcc

Interface: Vlan-interface200

   Status: Enable

   Strategy: Replace

   Circuit ID Pattern: User Defined

   Remote ID Pattern: User Defined

   Circuit ID format: ASCII

   Remote ID format: ASCII

   User defined:

   Circuit ID: vlan100

   Remote ID: device001

表1-10 display dhcp relay information命令显示信息描述表

字段

描述

Interface

接口名

Status

Option 82的状态，取值包括：

·Enable：启用了DHCP中继支持Option 82功能

·Disable：未启用DHCP中继支持Option 82功能

Strategy

对包含Option 82的请求报文的处理策略，取值为Drop、Keep或Replace

Circuit ID Pattern

Circuit ID子选项的填充方式，取值为Verbose、Normal或User Defined

Remote ID Pattern

Remote ID子选项的填充方式，取值为Sysname、Normal或User Defined

Circuit ID format

Circuit ID子选项的填充格式，取值为ASCII、Hex或Undefined

Remote ID format

Remote ID子选项的填充格式，取值为ASCII、Hex或Undefined

Node identifier

接入节点的标识

User defined

用户自定义的子选项内容

Circuit ID

用户自定义的Circuit ID子选项的内容

Remote ID

用户自定义的Remote ID子选项的内容

**DHCP \-- DHCP中继配置命令 \-- display dhcp relay server-address**

------------------------------------------------------------------------

**[display dhcp relay server-address**]命令用来显示接口上指定的DHCP服务器地址信息。

【命令】

**[display dhcp relay server-address** [ **interface** *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface*** interface-type interface-number*]：显示指定接口上的DHCP服务器地址信息。*interface-type interface-number*为接口类型和接口编号。如果不指定本参数，则显示所有接口上的DHCP服务器地址信息。

【举例】

 # 显示所有接口上指定的DHCP服务器地址信息。

\<Sysname\> display dhcp relay server-address

Interface name                 Server IP address

GE1/0/1                        2.2.2.2

表1-11 display dhcp relay server-address命令显示信息描述表

字段

描述

Interface name

接口名

Server IP address

指定的DHCP服务器地址

【相关命令】

· dhcp relay server-address{.commandkeywordsChar}

**DHCP \-- DHCP中继配置命令 \-- display dhcp relay statistics**

------------------------------------------------------------------------

display dhcp relay statistics{.commandkeywordsChar}命令用来显示DHCP中继的相关报文统计信息。

【命令】

display dhcp relay statistics {.commandkeywordsChar}[[ interface{.commandkeywordsChar} *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

interface{.commandkeywordsChar}* interface-type interface-number*：显示指定接口的DHCP中继相关报文统计信息。*interface-type interface-number*为接口类型和接口编号。如果不指定本参数，则显示所有的DHCP中继相关报文统计信息。

【举例】

\# 显示所有的DHCP中继相关报文统计信息。

\<Sysname\> display dhcp relay statistics

DHCP packets dropped:                  0

DHCP packets received from clients:    0

   DHCPDISCOVER:                       0

   DHCPREQUEST:                        0

   DHCPINFORM:                         0

   DHCPRELEASE:                        0

   DHCPDECLINE:                        0

   BOOTPREQUEST:                       0

DHCP packets received from servers:    0

   DHCPOFFER:                          0

   DHCPACK:                            0

   DHCPNAK:                            0

   BOOTPREPLY:                         0

DHCP packets relayed to servers:       0

   DHCPDISCOVER:                       0

   DHCPREQUEST:                        0

   DHCPINFORM:                         0

   DHCPRELEASE:                        0

   DHCPDECLINE:                        0

   BOOTPREQUEST:                       0

DHCP packets relayed to clients:       0

   DHCPOFFER:                          0

   DHCPACK:                            0

   DHCPNAK:                            0

   BOOTPREPLY:                         0

DHCP packets sent to servers:          0

   DHCPDISCOVER:                       0

   DHCPREQUEST:                        0

   DHCPINFORM:                         0

   DHCPRELEASE:                        0

   DHCPDECLINE:                        0

   BOOTPREQUEST:                       0

DHCP packets sent to clients:          0

   DHCPOFFER:                          0

   DHCPACK:                            0

   DHCPNAK:                            0

   BOOTPREPLY:                         0

表1-12 display dhcp relay statistics命令显示信息描述表

字段

描述

DHCP packets dropped

DHCP中继丢掉的报文数

DHCP packets received from clients

DHCP中继从客户端接收的DHCP报文数

DHCP packets received from servers

DHCP中继从服务器接收的DHCP报文数

DHCP packets relayed to servers

DHCP中继转发给服务器的报文数

DHCP packets relayed to clients

DHCP中继转发给客户端的报文数

DHCP packets sent to servers

DHCP中继主动发送给服务器的DHCP报文数，用于实现动态用户地址表项的定时刷新

DHCP packets sent to clients

DHCP中继主动发送给客户端的DHCP报文数（目前设备作为DHCP中继时，不会主动发送DHCP报文给客户端）

【相关命令】

·**reset dhcp relay statistics**

**DHCP \-- DHCP中继配置命令 \-- gateway-list**

------------------------------------------------------------------------

gateway-list{.commandkeywordsChar}命令用来指定匹配该地址池的DHCP客户端所在的网段的地址。

undo gateway-list{.commandkeywordsChar}命令用来删除指定的匹配该地址池的DHCP客户端所在的网段的地址。

【命令】

gateway-list{.commandkeywordsChar}* ip-address*&\<1-8\> [ **export-route** ]

undo gateway-list{.commandkeywordsChar} [ *ip-address*&\<1-8\>   **export-route** ]

【缺省情况】

未指定匹配该地址池的DHCP客户端所在的网段地址。

【视图】

DHCP地址池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*&\<1-8\>]：该地址池的DHCP客户端所在的网段的地址。&\<1-8\>表示最多可以输入8个IP地址，每个IP地址之间用空格分隔。

**[export-route**]：将网关列表信息下发给地址管理，通过应答客户端的ARP请求，即可实现对不同类型的业务流量的引导。

【使用指导】

一台DHCP中继的一个接口下可能连接不同类型的用户，当DHCP中继转发DHCP客户端请求报文给DHCP服务器时，不能再以中继接口的IP地址作为选择地址池的依据。为了解决这个问题，需要使用**gateway-list**命令指定某个类型用户所在的网段，并将该地址添加到转发给DHCP服务器的报文字段中，为DHCP服务器选择地址池提供依据。

【举例】

\# 指定匹配该地址池0的DHCP客户端所在的网段的地址为10.1.1.1。

\<Sysname\> system-view

Sysname dhcp server ip-pool 0

Sysname-dhcp-pool-0 gateway-list 10.1.1.1

**DHCP \-- DHCP中继配置命令 \-- remote-server**

------------------------------------------------------------------------

**[remote-server**]命令用来指定中继地址池对应的DHCP服务器地址。

**[undo remote-server**]命令用来删除为中继地址池指定的DHCP服务器地址。

【命令】

**[remote-server** *ip-address*&\<1-8\>]

**[undo remote-server ** *ip-address*&\<1-8\> ]

【缺省情况】

未指定中继地址池的DHCP服务器的地址。

【视图】

DHCP地址池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*&\<1-8\>]：DHCP服务器的IP地址。&\<1-8\>表示最多可以输入8个不同的IP地址，每个IP地址之间需要用空格分隔。

【使用指导】

·如果多次执行该命令，新的配置会覆盖已有配置。

·执行**undo remote-server**命令时，如果没有指定任何参数，则删除所有配置DHCP服务器地址。

【举例】

\# 配置DHCP地址池0为中继配置的服务器地址为10.1.1.1。

\<Sysname\> system-view

Sysname dhcp server ip-pool 0

Sysname-dhcp-pool-0 remote-server 10.1.1.1

**DHCP \-- DHCP中继配置命令 \-- reset dhcp relay client-information**

------------------------------------------------------------------------

reset dhcp relay client-information{.commandkeywordsChar}命令用来清除DHCP中继的用户地址表项信息。

【命令】

[[reset dhcp relay client-information ]{.commandkeywordsChar}[ [interface{.commandkeywordsChar} *interface-type interface-number*{.commandkeywordsChar}\| ip{.commandkeywordsChar} *ip-address*{.commandkeywordsChar} [vpn-instance{.commandkeywordsChar} *vpn-instance-name* ] ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

interface{.commandkeywordsChar} *interface-type interface-number*：清除指定接口上的DHCP中继的用户地址表项信息。*interface-type interface-number*为接口类型和接口编号。

ip{.commandkeywordsChar} *ip-address*：清除指定IP地址的用户地址表项信息。

vpn-instance{.commandkeywordsChar} *vpn-instance-name*：清除指定VPN内指定IP地址的用户地址表项信息。*vpn-name*表示MPLS L3VPN的VPN实例名，为1～31个字符的字符串，区分大小写。如果不指定本参数，则表示清除公网的用户地址表项信息。

【使用指导】

执行本命令时，如果没有指定任何参数，则清除所有DHCP中继的用户地址表项信息。

【举例】

\# 清除所有DHCP中继的用户地址表项信息。

\<Sysname\> reset dhcp relay client-information

【相关命令】

·**display dhcp relay client-information**

**DHCP \-- DHCP中继配置命令 \-- reset dhcp relay statistics**

------------------------------------------------------------------------

reset dhcp relay statistics{.commandkeywordsChar}命令用来清除DHCP中继的相关报文统计信息。

【命令】

reset dhcp relay statistics {.commandkeywordsChar}[[ interface{.commandkeywordsChar} *interface-type interface-number* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

interface{.commandkeywordsChar}* interface-type interface-number*：清除指定接口的DHCP中继相关报文统计信息。*interface-type interface-number*为接口类型和接口编号。如果不指定本参数，则清除所有的DHCP中继相关报文统计信息。

【举例】

\# 清除所有的DHCP中继相关报文统计信息。

\<Sysname\> reset dhcp relay statistics

【相关命令】

·**display dhcp relay statistics**

**DHCP \-- DHCP客户端配置命令 \-- dhcp client dad enable**

------------------------------------------------------------------------

**[dhcp client dad enable**]命令用来启用地址冲突检查功能。

**[undo** **dhcp client dad enable**]命令用来关闭地址冲突检查功能。

【命令】

**[dhcp client dad enable**]

**[undo dhcp client dad enable**]

【缺省情况】

接口上地址冲突检查功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

DHCP客户端通过发送和接收ARP报文，对DHCP服务器分配的IP地址进行地址冲突检测，如果攻击者仿冒地址拥有者进行ARP应答，就可以欺骗DHCP客户端，导致DHCP客户端无法正常使用分配到的IP地址。在网络中存在上述攻击者时，建议在客户端上关闭地址冲突检查功能。

【举例】

\# 关闭地址冲突检查功能。

\<Sysname\> system-view

Sysname undo dhcp client dad enable

**DHCP \-- DHCP客户端配置命令 \-- dhcp client dscp**

------------------------------------------------------------------------

**[dhcp client dscp**]命令用来配置DHCP客户端发送DHCP报文的DSCP优先级。

**[undo dhcp client dscp**]命令用来恢复缺省值。

【命令】

**[dhcp client dscp ***dscp-value*]

**[undo dhcp client dscp**]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dscp-value*]：DHCP请求报文的DSCP优先级，取值范围为0～63，缺省值为56。

【使用指导】

DSCP优先级用来体现报文自身的优先等级，决定报文传输的优先程度。配置的DSCP优先级的取值越大，报文的优先级越高。通过本命令可以指定DHCP客户端发送的DHCP报文中携带的DSCP优先级的取值。

【举例】

\# 配置DHCP客户端发送的DHCP报文的DSCP优先级为30。

\<Sysname\> system-view

Sysname dhcp client dscp 30

**DHCP \-- DHCP客户端配置命令 \-- dhcp client identifier**

------------------------------------------------------------------------

**[dhcp client identifier**]命令用来配置接口使用指定的客户端ID。

**[undo dhcp client identifier**]命令用来恢复缺省情况。

【命令】

**[dhcp client**[ **identifier** { **ascii** *string* \| **hex** *string* *\|* **mac** *interface-type* *interface-number* }]]

**[undo dhcp client** **identifier**]

【缺省情况】

根据本接口的MAC地址生成DHCP客户端ID。如果本接口没有MAC地址，则获取设备第一个以太接口的MAC地址生成DHCP客户端ID。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ascii ***string*]：使用指定的ASCII字符串作为该接口的客户端ID，为1～63个字符的字符串，区分大小写。

**[hex ***string*]：使用指定的十六进制字符串作为该接口的客户端ID，为4～64个字符的字符串。

**[mac** *interface-type* *interface-number*]：使用指定接口的MAC地址作为客户端ID。*interface-type* *interface-number*表示接口类型和接口编号。

【使用指导】

DHCP客户端ID用来填充DHCP报文Option 61，作为识别DHCP客户端的唯一标识。DHCP服务器可以根据客户端ID为特定的客户端分配特定的IP地址。用户可以通过以下三种方法指定DHCP客户端ID：ASCII字符串、十六进制字符串或使用指定接口的MAC地址作为DHCP客户端ID，以上三种方式都需要由用户保证不同客户端的客户端ID不会相同。

【举例】

·路由应用：

\# 配置接口GigabitEthernet1/0/1使用的客户端ID为接口GigabitEthernet1/0/2的MAC地址。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dhcp client identifier mac gigabitethernet 1/0/2

·交换应用：

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 dhcp client identifier hex FFFFFFFF

【相关命令】

·**display** **dhcp** **client**

**DHCP \-- DHCP客户端配置命令 \-- display dhcp client**

------------------------------------------------------------------------

**[display dhcp****client**]命令用来显示DHCP客户端的相关信息。

【命令】

**[display** **dhcp** **client** [ **verbose**   **interface** *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[verbose**]：显示DHCP客户端的详细信息。

**[interface** *interface-type interface-number*]：显示指定接口的DHCP客户端相关信息。*interface-type interface-number*为接口类型和接口编号。

【使用指导】

如果不指定**interface** *interface-type interface-number*参数，显示所有接口上的DHCP客户端相关信息。

【举例】

\# 显示所有接口的DHCP客户端相关信息。

\<Sysname\> display dhcp client

Vlan-interface10 DHCP client information:

 Current state: BOUND

 Allocated IP: 40.1.1.20 255.255.255.0

 Allocated lease: 259200 seconds, T1: 129600 seconds, T2: 226800 seconds

 DHCP server: 40.1.1.2

\# 显示所有接口的DHCP客户端详细信息。

\<Sysname\> display dhcp client verbose

Vlan-interface10 DHCP client information:

 Current state: BOUND

 Allocated IP: 40.1.1.20 255.255.255.0

 Allocated lease: 259200 seconds, T1: 129600 seconds, T2: 226800 seconds

 Lease from May 21 19:00:29 2012   to   May 31 19:00:29 2012

 DHCP server: 40.1.1.2

 Transaction ID: 0x1c09322d

 Default router: 40.1.1.2

Classless static routes:

   Destination: 1.1.0.1, Mask: 255.0.0.0, NextHop: 192.168.40.16

   Destination: 10.198.122.63, Mask: 255.255.255.255, NextHop: 192.168.40.16

 DNS servers: 44.1.1.11 44.1.1.12

 Domain name: ddd.com

 Boot servers: 200.200.200.200  1.1.1.1

 ACS parameter:

   URL: http://192.168.1.1:7547/acs

   Username: bims

   Password: \*\*\*\*\*\*

 Client ID type: acsii(type value=00)

 Client ID value: 000c.29d3.8659-GE1/0/1

 Client ID (with type) hex: 0030-3030-632e-3239-

                            6433-2e38-3635-392d-

                            4574-6830-2f30-2f32

 T1 will timeout in 1 day 11 hours 58 minutes 52 seconds.

表1-13 display dhcp client命令显示信息描述表

字段

描述

Vlan-interface10 DHCP client information

作为DHCP客户端的接口信息

Current state

DHCP客户端状态机的当前状态，取值包括：

·HALT：停止申请IP地址状态；

·INIT：初始化状态；

·SELECTING：发送DHCP-DISCOVER报文寻找DHCP服务器后，进入该状态，等待DHCP服务器的响应报文；

·REQUESTING：发送DHCP-REQUEST报文请求IP地址后，进入该状态，等待DHCP服务器的响应报文；

·BOUND：接收到DHCP服务器发送的DHCP-ACK报文，成功获取IP地址后，进入该状态；

·RENEWING：T1定时器超时后，进入该状态；

·REBOUNDING：T2定时器超时后，进入该状态。

Allocated IP

DHCP服务器为接口分配的IP地址

Allocated lease

租约时长

T1

DHCP客户端的一半左右租约时间（以秒为单位）

T2

DHCP客户端的7/8租约时间（以秒为单位）

Lease from....to....

租约起止时间

DHCP server

选择的DHCP服务器的地址

Transaction ID

DHCP客户端发起申请时生成的一个随机数，用来唯一标识一次申请过程

Default router

为DHCP客户端指定的网关地址

Classless static routes

为DHCP客户端指定的无分类静态路由

Static routes

为DHCP客户端指定的有分类静态路由

DNS servers

为DHCP客户端指定的DNS服务器地址

Domain name

为DHCP客户端指定的域名后缀

Boot servers

为DHCP客户端指定的PXE引导服务器地址，通过Option 43获取，最多可以获取16个地址

ACS parameter

ACS参数

URL

ACS的URL地址

Username

登录ACS设备使用的用户名

Password

登录ACS设备使用的密码，若存在密码，则显示为"\*\*\*\*\*\*"；若不存在密码，则不显示此项；

Client ID type

DHCP客户端ID的类型，type value表示类型值。类型为ASCII时，type value为00；为MAC address时，type value为01；为Hex时，type value为配置的十六进制数的前两位

Client ID value

DHCP客户端ID的取值

Client ID (with type) hex

DHCP客户端ID的十六进制形式（带类型值字段）

T1 will timeout in 1 day 11 hours 58 minutes 52 seconds.

在多少时间后T1定时器（即一半左右租约时间）将到期

【相关命令】

·**dhcp client** **identifier**

·**ip address dhcp-alloc**

**DHCP \-- DHCP客户端配置命令 \-- ip address dhcp-alloc**

------------------------------------------------------------------------

**[ip** **address** **dhcp-alloc**]命令用来配置接口通过DHCP协议获取IP地址。

**[undo** **ip** **address** **dhcp-alloc**]命令用来取消接口通过DHCP协议获取IP地址。

【命令】

**[ip** **address** **dhcp-alloc**]

**[undo** **ip** **address** **dhcp-alloc**]

【缺省情况】

接口不通过DHCP协议获取IP地址。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

取消接口通过DHCP协议获取IP地址时，DHCP客户端会发送DHCP-RELEASE报文通知DHCP服务器释放租约。如果此时该接口处于down状态，则无法保证报文成功发送。

如果配置子接口通过DHCP协议获取IP地址，在其主接口上执行**shutdown**命令时，DHCP客户端不会发送请求释放子接口IP地址租约的DHCP-RELEASE报文。

【举例】

·路由应用

\# 在GigabitEthernet1/0/1接口上配置接口通过DHCP协议获取IP地址。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ip address dhcp-alloc

·交换应用

\# 在VLAN接口10上配置接口通过DHCP协议获取IP地址。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 ip address dhcp-alloc

【相关命令】

·**display** **dhcp** **client**

**DHCP \-- DHCP Snooping配置命令 \-- dhcp snooping binding database filename**

------------------------------------------------------------------------

**[dhcp** **snooping** **binding** **database** **filename**]命令用来指定存储DHCP Snooping表项的文件名称。

**[undo** **dhcp** **snooping** **binding** **database** **filename**]命令用来恢复缺省情况。

【命令】

**[dhcp**[ **snooping** **binding** **database** **filename** { *filename \|* **url** *url* [ **username** *username* [ **password** { **cipher** \| **simple** } *key* ] ] }]]

**[undo** **dhcp** **snooping** **binding** **database** **filename**]

【缺省情况】

未指定存储文件名称。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[filename*]：目标文件名，该配置用于本地存储模式。文件名取值范围的详细介绍，请参见"基础配置指导"中的"文件系统管理"。

**[url*** url*]：配置远程目标文件URL，该配置用于远程文件系统模式。此参数中不能包含用户名和密码，和参数*username*和*password*配合使用。远程目标文件URL是否支持大小写和是否支持路径格式遵循远程服务器端规格。

**[username*** username*]：配置远程目标文件URL时的用户名。

**[cipher**]：表示以密文方式设置用户密码。

**[simple**]：表示以明文方式设置用户密码。

*[key*]：设置的明文密码或密文密码，区分大小写。明文密码为1～32个字符的字符串；密文密码为1～73个字符的字符串。

【使用指导】

·以明文或密文方式设置的用户密码，均以密文的方式保存在配置文件中。

·存储DHCP Snooping表项时，如果设备中还不存在对应名称的文件，则设备会自动创建该文件。

·执行本命令后，会立即触发一次表项备份。之后，如果未配置**dhcp** **snooping** **binding** **database** **update** **interval**命令，若表项发生变化，默认在300秒之后刷新存储文件；若表项未发生变化，则不再刷新存储文件。如果配置了**dhcp** **snooping** **binding** **database** **update** **interval**命令，若表项发生变化，则到达刷新时间间隔后刷新存储文件；若表项未发生变化，则不再刷新存储文件。

·参数*filename*不支持远程目标文件URL，配置远程目标文件URL请使用*url*、*username*、*key*配合使用。

·频繁擦写本地存储介质可能会影响存储介质寿命，建议使用远程文件系统模式存储DHCP Snooping表项文件。

当进行远程存储时，支持FTP和TFTP协议：

·当采用FTP或TFTP协议时，服务器地址支持IPv4形式或IPv6形式，并且支持DNS域名方式。服务器地址为IPv6地址形式时需使用方括号(""和"")引用。配置服务器地址为DNS域名格式时请勿使用方括号引用。

·当采用FTP协议时，URL采用"ftp://服务器地址:端口号/文件路径"的形式，如有用户名和密码请分别使用参数*username*和参数*key*进行配置，用户名和密码必须和服务器上的配置一致，如果服务器只对用户名进行认证，则不用输入密码。

·当采用TFTP协议时，URL采用"tftp://服务器地址:端口号/文件路径"的形式。

【举例】

\# 配置存储DHCP Snooping表项的文件名为database.dhcp。

\<Sysname\> system-view

Sysname dhcp snooping binding database filename database.dhcp

\# 配置远程存储DHCP Snooping表项至IP地址为1.1.1.1的ftp服务器工作目录下,用户名为1，密码为1，文件名为database.dhcp。

\<Sysname\> system-view

Sysname dhcp snooping binding database filename url ftp://10.1.1.1/database.dhcp username 1 password simple 1

\# 配置远程存储DHCP Snooping表项至IP地址为10.1.1.1的tftp服务器工作目录下，文件名为database.dhcp。

\<Sysname\> system-view

Sysname dhcp snooping binding database filename tftp://10.1.1.1/database.dhcp

【相关命令】

·**dhcp** **snooping** **binding** **database** **update** **interval**

**DHCP \-- DHCP Snooping配置命令 \-- dhcp snooping binding database update interval**

------------------------------------------------------------------------

**[dhcp** **snooping** **binding** **database** **update** **interval**]命令用来配置刷新DHCP Snooping表项存储文件的延迟时间。

**[undo** **dhcp** **snooping** **binding** **database** **update** **interval**]命令用来恢复缺省情况。

【命令】

**[dhcp** **snooping** **binding** **database** **update** **interval** *seconds*]

**[undo** **dhcp** **snooping** **binding** **database** **update** **interval**]

【缺省情况】

若DHCP Snooping表项不变化，则不刷新存储文件；若DHCP Snooping表项发生变化，默认在300秒之后刷新存储文件。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：刷新延迟时间，取值范围为60～864000，单位为秒。

【使用指导】

·执行本命令后，当DHCP Snooping表项发生变化后，DHCP Snooping设备开始计时，当本命令配置的延迟时间到达后，DHCP Snooping会把这个时间段内表项所有的变化信息备份到固化文件中。

·如果未通过**dhcp** **snooping** **binding** **database** **filename**命令指定存储表项的文件，则本命令不会生效。

【举例】

\# 若DHCP Snooping表项发生变化，在10分钟后刷新表项存储文件。

\<Sysname\> system-view

Sysname dhcp snooping binding database update interval 600

【相关命令】

·**dhcp** **snooping** **binding** **database** **filename**

**DHCP \-- DHCP Snooping配置命令 \-- dhcp snooping binding database update now**

------------------------------------------------------------------------

**[dhcp**] **snooping** **binding** **database** **update** **now**命令用来将当前的DHCP Snooping表项保存到用户指定的文件中。

【命令】

**[dhcp** **snooping** **binding** **database** **update** **now**]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·本命令只用来触发一次DHCP Snooping表项的备份。

·如果未通过**dhcp** **snooping** **binding** **database** **filename**命令指定存储表项的文件，则本命令不会生效。

【举例】

\# 将当前的DHCP Snooping表项保存到文件中。

\<Sysname\> system-view

Sysname dhcp snooping binding database update now

【相关命令】

·**dhcp** **snooping** **binding** **database** **filename**

**DHCP \-- DHCP Snooping配置命令 \-- dhcp snooping binding record**

------------------------------------------------------------------------

**[dhcp** **snooping** **binding** **record**]命令用来启用端口的DHCP Snooping表项记录功能。

**[undo** **dhcp** **snooping** **binding** **record**]命令用来关闭端口的DHCP Snooping表项记录功能。

【命令】

**[dhcp** **snooping** **binding** **record**]

**[undo****dhcp** **snooping** **binding** **record**]

【缺省情况】

端口DHCP Snooping表项记录功能处于关闭状态。

【视图】

二层以太网接口视图/二层聚合接口视图/WLAN-BSS接口视图/WLAN-ESS接口视图/S通道接口视图/S通道聚合接口视图/VSI接口视图/VSI聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

用户可在DHCP Snooping设备直接与客户端连接的端口上启用DHCP Snooping表项记录功能。

【举例】

\# 启用端口的DHCP Snooping表项记录功能。

\<Sysname\> system-view

Sysnameinterface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dhcp snooping binding record

**DHCP \-- DHCP Snooping配置命令 \-- dhcp snooping check mac-address**

------------------------------------------------------------------------

**[dhcp** **snooping** **check** **mac-address**]命令用来启用DHCP Snooping的MAC地址检查功能。

**[undo** **dhcp** **snooping** **check** **mac-address**]命令用来关闭DHCP Snooping的MAC地址检查功能。

【命令】

**[dhcp** **snooping** **check** **mac-address**]

**[undo** **dhcp** **snooping** **check** **mac-address**]

【缺省情况】

DHCP Snooping的MAC地址检查功能处于关闭状态。

【视图】

二层以太网接口视图/二层聚合接口视图/WLAN-BSS接口视图/WLAN-ESS接口视图/S通道接口视图/S通道聚合接口视图/VSI接口视图/VSI聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

启用该功能后，DHCP Snooping检查接收到的DHCP请求报文中的chaddr字段和数据帧的源MAC地址字段是否一致。如果一致，则认为该报文合法，将其转发给DHCP服务器；如果不一致，则丢弃该报文。

【举例】

\# 启用DHCP Snooping的MAC地址检查功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dhcp snooping check mac-address

**DHCP \-- DHCP Snooping配置命令 \-- dhcp snooping check request-message**

------------------------------------------------------------------------

**[dhcp snooping check request-message**]命令用来启用DHCP Snooping的DHCP请求方向报文检查功能。

**[undo** **dhcp** **snooping** **check** **request-message**]命令用来关闭DHCP Snooping的DHCP请求方向报文检查功能。

【命令】

**[dhcp** **snooping** **check** **request-message**]

**[undo** **dhcp** **snooping** **check** **request-message**]

【缺省情况】

DHCP Snooping的DHCP请求方向报文检查功能处于关闭状态。

【视图】

二层以太网接口视图/二层聚合接口视图/WLAN-BSS接口视图/WLAN-ESS接口视图/S通道接口视图/S通道聚合接口视图/VSI接口视图/VSI聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本功能用来检查DHCP续约报文、DHCP-DECLINE和DHCP-RELEASE三种DHCP请求方向的报文，以防止非法客户端伪造这三种报文对DHCP服务器进行攻击。

如果启用了该功能，则DHCP Snooping设备接收到上述报文后，检查本地是否存在与接收报文匹配的DHCP Snooping表项。若存在，则接收报文信息与DHCP Snooping表项信息一致时，认为该报文为合法的请求方向报文，将其转发给DHCP服务器；不一致时，认为该报文为伪造的请求方向报文，将其丢弃。若不存在，则认为该报文合法，将其转发给DHCP服务器。

【举例】

\# 启用DHCP Snooping的DHCP请求方向报文检查功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dhcp snooping check request-message

**DHCP \-- DHCP Snooping配置命令 \-- dhcp snooping enable**

------------------------------------------------------------------------

**[dhcp** **snooping** **enable**]命令用来启用DHCP Snooping功能。

**[undo** **dhcp** **snooping** **enable**]命令用来关闭DHCP Snooping功能。

【命令】

**[dhcp** **snooping** **enable**]

**[undo** **dhcp** **snooping** **enable**]

【缺省情况】

DHCP Snooping功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

启用DHCP Snooping功能后，如果不信任端口接收到DHCP服务器发送的报文，将丢弃该报文，以保证客户端从合法的DHCP服务器获取IP地址。此时，设备不会记录DHCP Snooping表项。

在DHCP Snooping功能关闭后，所有端口都可转发DHCP服务器的响应报文，并且不记录DHCP客户端的IP地址、MAC地址和VLAN等信息。

【举例】

\# 启用DHCP Snooping功能。

\<Sysname\> system-view

Sysname dhcp snooping enable

**DHCP \-- DHCP Snooping配置命令 \-- dhcp snooping information circuit-id**

------------------------------------------------------------------------

![说明](DHCP命令.files/image001.png)

本特性的支持情况与设备的型号有关，请以设备的实际情况为准。

**[dhcp** **snooping** **information** **circuit-id**]命令用来配置Option 82的Circuit ID子选项的填充模式和填充格式。

**[undo** **dhcp** **snooping** **information** **circuit-id**]命令用来恢复缺省情况。

【命令】

**[dhcp snooping information circuit-id **{ [ **vlan** *vlan-id*  **string** *circuit-id* \| { **normal** \| **verbose** [ **node-identifier** { **mac** \| **sysname** \| **user-defined** *node-identifier* } ] } [ **format** { **ascii** \| **hex** } ] }]]

**[undo** **dhcp** **snooping** **information** **circuit-id** [ **vlan** *vlan-id* ]]

【缺省情况】

Option 82的Circuit ID子选项的填充模式为Normal，填充格式为hex。

【视图】

二层以太网接口视图/二层聚合接口视图/WLAN-BSS接口视图/WLAN-ESS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan ***vlan-id*]：为从指定VLAN内收到的DHCP报文填充Circuit ID子选项。

**[string** *circuit-id*]：指定以用户配置的字符串填充Circuit ID子选项。*circuit-id*表示用户配置的用来填充Circuit ID子选项的内容，为3～63个字符的字符串，区分大小写。

**[normal**]：指定以Normal模式填充Circuit ID子选项，填充内容为VLAN ID和端口号。

**[verbose**]：指定以Verbose模式填充Circuit ID子选项。

**[node-identifier**[ { **mac** \| **sysname** \| **user-defined** *node-identifier* }]]：指定接入节点的标识。缺省情况下，以节点的MAC地址作为节点标识。

·**mac**：表示以节点的MAC地址作为节点标识。Circuit ID子选项的填充内容为MAC地址、以太网类型（取值固定为"eth"）、框号、槽号、子槽号、接口编号、VLAN ID组成的字符串。

·**sysname**：表示以节点的设备名称作为节点标识。Circuit ID子选项的填充内容为设备的系统名称、以太网类型（取值固定为"eth"）、框号、槽号、子槽号、接口编号、VLAN ID组成的字符串。其中，设备的系统名称可以通过系统视图下的**sysname**命令配置。不管配置了哪种填充格式，设备的系统名称始终采用ASCII码格式填充。

·**user-defined** *node-identifier*：表示以指定的字符串作为节点标识，*node-identifier*为1～50个字符的字符串，区分大小写。Circuit ID子选项的填充内容为指定的字符串、以太网类型（取值固定为"eth"）、框号、槽号、子槽号、接口编号、VLAN ID组成的字符串。不管配置了哪种填充格式，指定的字符串始终采用ASCII码格式填充。

**[format**]：指定Circuit ID子选项的填充格式。

**[ascii**]：指定以ASCII码格式填充Circuit ID子选项，即将数值转换为对应的ASCII码填充到Circuit ID子选项。

**[hex**]：指定以十六进制数值的格式填充Circuit ID子选项。

【使用指导】

以用户配置的字符串填充Circuit ID子选项时，填充格式固定为ASCII码格式。

以Normal和Verbose模式填充Circuit ID子选项时，填充格式由本命令的配置决定。

·如果本命令中未指定填充格式，则对于Normal模式，VLAN ID和端口号均以hex格式填充；对于Verbose模式，节点标识（MAC地址、设备的系统名称或指定的字符串）、以太网类型、框号、槽号、子槽号、接口编号均以ASCII码格式填充，VLAN ID以hex格式填充。

·如果本命令中指定填充格式为**ascii**，则所有内容均以ASCII码格式填充。

·如果本命令中指定填充格式为**hex**，则对于Normal模式，VLAN ID和端口号均以hex格式填充；对于Verbose模式，设备的节点标识、以太网类型以ASCII码格式填充，其余内容均以hex格式填充。

需要注意的是：

·如果多次执行该命令，新的配置会覆盖已有配置。

·如果以设备的系统名称（**sysname**）作为节点标识填充DHCP报文的Option 82，则系统名称中不能包含空格；否则，DHCP Snooping添加或替换Option 82失败

·Option 82的Circuit ID子选项信息中无法携带携带接口拆分信息或子接口信息，关于"接口拆分"和"子接口"的详细介绍，请参见"以太网接口配置指导"中的"以太网接口通用配置"。

【举例】

\# 配置以Verbose模式填充Option 82的Circuit ID子选项，节点标识为设备的系统名称，填充格式为ASCII码格式。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dhcp snooping information enable

Sysname-GigabitEthernet1/0/1 dhcp snooping information strategy replace

Sysname-GigabitEthernet1/0/1 dhcp snooping information circuit-id verbose node-identifier sysname format ascii

【相关命令】

·**dhcp** **snooping** **information** **enable**

·**dhcp** **snooping** **information** **strategy**

·**display dhcp snooping information**

**DHCP \-- DHCP Snooping配置命令 \-- dhcp snooping information enable**

------------------------------------------------------------------------

![说明](DHCP命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[dhcp** **snooping** **information** **enable**]命令用来启用DHCP Snooping支持Option 82功能。

**[undo** **dhcp** **snooping** **information** **enable**]命令用来禁止DHCP Snooping支持Option 82功能。

【命令】

**[dhcp** **snooping** **information** **enable**]

**[undo** **dhcp** **snooping** **information** **enable**]

【缺省情况】

DHCP Snooping支持Option 82功能处于关闭状态。

【视图】

二层以太网接口视图/二层聚合接口视图/WLAN-BSS接口视图/WLAN-ESS接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

启用DHCP Snooping支持Option 82功能后，DHCP Snooping将向转发给DHCP服务器的请求报文中增加Option 82选项。选项内容由**dhcp** **snooping** **information** **circuit-id**和**dhcp** **snooping** **information** **remote-id**决定。如果DHCP Snooping收到的请求报文中已经包含Option 82选项，则按照**dhcp** **snooping** **information** **strategy**配置的策略处理请求报文。

【举例】

\# 启用DHCP Snooping支持Option 82功能。

\<Sysname\> system-view

Sysname interface gigabitethernet1/0/1

Sysname-GigabitEthernet1/0/1 dhcp snooping information enable

【相关命令】

·**dhcp snooping information circuit-id**

·**dhcp** **snooping** **information** **remote-id**

·**dhcp** **snooping** **information** **strategy**

**DHCP \-- DHCP Snooping配置命令 \-- dhcp snooping information remote-id**

------------------------------------------------------------------------

![说明](DHCP命令.files/image001.png)

本特性的支持情况与设备的型号有关，请以设备的实际情况为准。

**[dhcp** **snooping** **information** **remote-id**]命令用来配置Option 82的Remote ID子选项的填充模式和填充格式。

**[undo** **dhcp** **snooping** **information** **remote-id**]命令用来恢复缺省情况。

【命令】

**[dhcp**[ **snooping** **information** **remote-id** { **normal** [ **format** { **ascii** \| **hex** } ] \|  **vlan** *vlan-id*  { **string** *remote-id* \| **sysname** } }]]

**[undo** **dhcp** **snooping** **information** **remote-id** [ **vlan** *vlan-id* ]]

【缺省情况】

Option 82的Remote ID子选项的填充模式为Normal、填充格式为hex。

【视图】

二层以太网接口视图/二层聚合接口视图/WLAN-BSS接口视图/WLAN-ESS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan ***vlan-id*]：为从指定VLAN内收到的DHCP报文填充Remote ID子选项。

**[string** *remote-id*]：指定以用户配置的字符串填充Remote ID子选项。*remote-id*表示用户配置的用来填充Remote ID子选项的内容，为1～63个字符的字符串，区分大小写。

**[sysname**]：指定以设备的系统名称填充Remote ID子选项。设备的系统名称可以通过系统视图下的**sysname**命令配置。

**[normal**]：指定以Normal模式填充Remote ID子选项，填充内容为接收报文接口的MAC地址。

**[format**]：指定Remote ID子选项的填充格式。如果没有配置，则以hex模式填充。

**[ascii**]：指定以ASCII码格式填充Remote ID子选项，即将数值转换为对应的ASCII码填充到Remote ID子选项。

**[hex**]：指定以十六进制数值的格式填充Remote ID子选项。

【使用指导】

以用户配置的字符串（**string**）和设备的系统名称（**sysname**）填充Remote ID子选项时，填充内容固定为ASCII格式；以Normal模式填充Remote ID子选项时，填充内容的格式由本命令配置的填充格式决定。

需要注意的是，如果多次执行本命令，新的配置会覆盖已有配置。

【举例】

\# 配置采用字符串device001填充Option 82的Remote ID子选项。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dhcp snooping information enable

Sysname-GigabitEthernet1/0/1 dhcp snooping information strategy replace

Sysname-GigabitEthernet1/0/1 dhcp snooping information remote-id string device001

【相关命令】

·**dhcp** **snooping** **information** **enable**

·**dhcp** **snooping** **information** **strategy**

·**display** **dhcp** **snooping** **information**

**DHCP \-- DHCP Snooping配置命令 \-- dhcp snooping information strategy**

------------------------------------------------------------------------

![说明](DHCP命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[dhcp** **snooping** **information** **strategy**]命令用来配置DHCP Snooping对包含Option 82的请求报文的处理策略。

**[undo** **dhcp** **snooping** **information** **strategy**]命令用来恢复缺省情况。

【命令】

**[dhcp**[ **snooping** **information** **strategy** { **drop** \| **keep** \| **replace** }]]

**[undo** **dhcp** **snooping** **information** **strategy**]

【缺省情况】

对带有Option 82的请求报文的处理策略为**replace**。

【视图】

二层以太网接口视图/二层聚合接口视图/WLAN-BSS接口视图/WLAN-ESS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[drop**]：如果报文中带有Option 82，则丢弃该报文。

**[keep**]：如果报文中带有Option 82，则保持该报文中的Option 82不变并进行转发。

**[replace**]：如果报文中带有Option 82，则按照配置的填充格式填充Option 82，用该选项替换报文中原有的Option 82，并进行转发。

【使用指导】

本命令仅对包含Option 82的请求报文有效。

如果启用了DHCP Snooping支持Option 82功能，则对于接收到的不包含Option 82的请求报文，DHCP Snooping的处理方式始终为在请求报文中添加Option 82，并将报文转发给DHCP服务器。

DHCP Snooping对包含Option 82请求报文的处理策略为**replace**时，需要配置Option 82的填充模式和填充格式；处理策略为**keep**或**drop**时，不需要配置Option 82选项的填充模式和填充格式。

【举例】

\# 配置DHCP Snooping对带有Option 82的请求报文使用**keep**策略。

\<Sysname\> system-view

Sysname interface gigabitethernet1/0/1

Sysname-GigabitEthernet1/0/1 dhcp snooping information enable

Sysname-GigabitEthernet1/0/1 dhcp snooping information strategy keep

【相关命令】

·**dhcp snooping information circuit-id**

·**dhcp** **snooping** **information** **remote-id**

**DHCP \-- DHCP Snooping配置命令 \-- dhcp snooping max-learning-num**

------------------------------------------------------------------------

**[dhcp snooping max-learning-num**]命令用来配置接口动态学习DHCP Snooping表项的最大数目。

**[undo dhcp snooping max-learning-num**]命令用来恢复缺省情况。

【命令】

**[dhcp snooping max-learning-num ***number*]

**[undo dhcp snooping max-learning-num**]

【缺省情况】

不限制接口动态学习DHCP Snooping表项的最大数目。

【视图】

二层以太网接口视图/二层聚合接口视图/S通道接口视图/S通道聚合接口视图/VSI接口视图/VSI聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：接口动态学习DHCP Snooping表项的最大数目。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【举例】

\# 配置二层以太网接口GigabitEthernet1/0/1动态学习DHCP Snooping表项的最大数目为1000。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dhcp snooping max-learning-num 1000

**DHCP \-- DHCP Snooping配置命令 \-- dhcp snooping rate-limit**

------------------------------------------------------------------------

![说明](DHCP命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[dhcp** **snooping** **rate-limit**]命令用来启用DHCP Snooping的报文限速功能，即限制接口接收DHCP报文的速率。

**[undo** **dhcp** **snooping** **rate-limit**]命令用来关闭DHCP Snooping的报文限速功能。

【命令】

**[dhcp** **snooping** **rate-limit** *rate*]

**[undo** **dhcp** **snooping** **rate-limit**]

【缺省情况】

DHCP Snooping的报文限速功能处于关闭状态，即不限制接口接收DHCP报文的速率。

【视图】

二层以太网接口视图/二层聚合接口视图/S通道接口视图/S通道聚合接口视图/VSI接口视图/VSI聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[rate*]：接口接收DHCP报文的最高速率，单位为Kbps。本参数的取值范围与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·只有启用DHCP Snooping功能后，本命令的配置才会生效。

·如果接口接收到的DHCP报文速率超过了限制，则丢弃超过速率限制的DHCP报文。

·如果二层以太网接口加入了聚合组，则该接口采用对应二层聚合接口下的DHCP报文限速配置。如果二层以太网接口离开聚合组，则该接口采用二层以太网接口下的DHCP报文限速配置。

·对于某些产品来说，由于芯片的限制，限速速率的实际生效值只能是某个数值的整数倍。比如，某产品芯片支持的速率值是8的整数倍，当用户设置的速率值为67时，实际的生效值是64或72。

【举例】

\# 配置二层以太网接口GigabitEthernet1/0/1接收DHCP报文的最高速率为64Kbps。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dhcp snooping rate-limit 64

**DHCP \-- DHCP Snooping配置命令 \-- dhcp snooping trust**

------------------------------------------------------------------------

**[dhcp** **snooping** **trust**]命令用来配置端口为信任端口。

**[undo** **dhcp** **snooping** **trust**]命令用来恢复端口为不信任端口。

【命令】

**[dhcp** **snooping** **trust**]

**[undo** **dhcp** **snooping** **trust**]

【缺省情况】

在启用DHCP Snooping功能后，设备上所有支持DHCP Snooping功能的端口均为不信任端口。

【视图】

二层以太网接口视图/二层聚合接口视图/WLAN-BSS接口视图/WLAN-ESS接口视图/S通道接口/S通道聚合接口/VSI接口/VSI聚合接口

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

指向DHCP服务器方向的端口需要设置为信任端口，其他端口设置为不信任端口，从而保证DHCP客户端只能从合法的DHCP服务器获取IP地址，私自架设的伪DHCP服务器无法为DHCP客户端分配IP地址。

【举例】

\# 配置二层以太网接口GigabitEthernet1/0/1为信任端口。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dhcp snooping trust

【相关命令】

·**display** **dhcp** **snooping** **trust**

**DHCP \-- DHCP Snooping配置命令 \-- display dhcp snooping binding**

------------------------------------------------------------------------

**[display** **dhcp** **snooping** **binding**]命令用来显示DHCP Snooping表项信息。

【命令】

**[display** **dhcp** **snooping** **binding** [ **ip** *ip-address* [ **vlan** *vlan-id*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[ip** *ip-address*]：显示指定IP地址对应的DHCP Snooping表项。

**[vlan ***vlan-id*]：显示指定VLAN内的DHCP Snooping表项。

【使用指导】

执行本命令时，如果不指定任何参数，则显示设备上所有DHCP Snooping表项。

【举例】

\# 显示DHCP Snooping表项信息。

\<Sysname\> display dhcp snooping binding

 2 DHCP snooping entries found

 IP address      MAC address    Lease        VLAN  SVLAN Interface

 =============== ============== ============ ===== ===== =================

 1.1.1.7         0000-0101-0107 16907533     2     3     GE1/0/1

 1.1.1.11        0000-0101-010b 16907537     2     3     GE1/0/3

表1-14 display dhcp snooping binding命令显示信息描述表

字段

描述

DHCP snooping entries found

表项统计计数

IP address

DHCP服务器为DHCP客户端分配的IP地址

MAC address

DHCP客户端的MAC地址

Lease

绑定的租约剩余时间，单位为秒

VLAN

如果DHCP Snooping功能与QinQ功能同时使用，或接收到的DHCP报文带有两层VLAN Tag，则表示外层VLAN Tag；否则，表示与DHCP客户端连接的设备端口所属的VLAN

SVLAN

如果DHCP Snooping功能与QinQ功能同时使用，或接收到的DHCP报文带有两层VLAN Tag，则表示内层VLAN Tag；否则，显示为"N/A"

Interface

与DHCP客户端连接的设备端口

【相关命令】

·**dhcp** **snooping** **enable**

·**reset** **dhcp** **snooping**** binding**

**DHCP \-- DHCP Snooping配置命令 \-- display dhcp snooping binding database**

------------------------------------------------------------------------

**[display** **dhcp** **snooping** **binding** **database**]命令用来显示DHCP Snooping表项备份信息。

【命令】

**[display** **dhcp** **snooping** **binding** **database**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示DHCP Snooping表项备份信息。

\<Sysname\> display dhcp snooping binding database

File name               :   database.dhcp

Username                :  

Password                :  

Update interval         :   600 seconds

Latest write time       :   Feb 27 18:48:04 2012

Status                  :   Last write succeeded.

表1-15 display dhcp snooping binding database命令显示信息描述表

字段

描述

File name

存储DHCP Snooping表项的文件名称

Username

配置远程目标文件时的用户名

Password

配置远程目标文件时的密码，有配置时显示为"\*\*\*\*\*\*"

Update interval

定期刷新表项存储文件的刷新时间间隔，单位为秒

Latest write time

最近一次写文件的时间

Status

写文件的状态，即写文件是否成功

·Writing：正在写文件

·Last write succeeded.：写文件成功

·Last write failed.：写文件失败

**DHCP \-- DHCP Snooping配置命令 \-- display dhcp snooping information**

------------------------------------------------------------------------

**[display** **dhcp snooping** **information**]命令用来显示DHCP Snooping上Option 82的配置信息。

【命令】

**[display**[ **dhcp snooping** **information** { **all** \| **interface** *interface-type* *interface-number* }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[all**]：显示所有二层以太网接口对应的Option 82配置信息。

**[interface** *interface-type* *interface-number*]：显示指定接口对应的Option 82配置信息。*interface-type* *interface-number*为接口类型和接口编号。

【举例】

\# 显示所有接口对应的Option 82配置信息。

\<Sysname\> display dhcp snooping information all

Interface: Bridge-Aggregation1

   Status: Disable

   Strategy: Drop

   Circuit ID:

     Padding format: User Defined

       User defined: abcd

     Format: ASCII

   Remote ID:

     Padding format: Normal

     Format: ASCII

   VLAN 10:

     Circuit ID: abcd

     Remote ID: company

表1-16 display dhcp snooping information命令显示信息描述表

字段

描述

Interface

接口名

Status

Option 82的状态，取值为Enable或Disable

Strategy

对包含Option 82的请求报文的处理策略，取值为Drop、Keep或Replace

Circuit ID

Circuit ID子选项的内容

Padding format

Option 82的填充模式：

·在填充Circuit ID子选项时，取值为Normal、User Defined、Verbose(sysname)、Verbose(MAC)或Verbose(user defined)

·在填充Remote ID子选项时，取值为Normal、Sysname或User Defined

Node identifier

接入节点的标识

User defined

用户自定义的子选项内容

Format

Option 82子选项的填充格式

·在填充Circuit ID子选项时，取值为ASCII、Default或Hex

·在填充Remote ID子选项时，取值为ASCII或Hex

Remote ID

Remote ID子选项的内容

VLAN

为指定VLAN内收到的DHCP报文填充的Circuit ID子选项和Remote ID子选项内容

**DHCP \-- DHCP Snooping配置命令 \-- display dhcp snooping packet statistics**

------------------------------------------------------------------------

**[display** **dhcp** **snooping** **packet** **statistics**]命令用来显示DHCP Snooping设备上的DHCP报文统计信息。

【命令】

集中式设备：

**[display** **dhcp** **snooping** **packet** **statistics**]

分布式设备---独立运行模式/集中式IRF设备：

**[display** **dhcp** **snooping** **packet** **statistics** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备---IRF模式：

**[display** **dhcp** **snooping** **packet** **statistics** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot** *slot-number*]：显示指定单板的DHCP报文统计信息。*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示主用主控板上的DHCP报文统计信息。（分布式设备---独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的DHCP报文统计信息。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示Master设备上的DHCP报文统计信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的DHCP报文统计信息。*slot-number*表示设备在IRF中的成员编号或PEX的虚拟槽位号。如果未指定本参数，则显示Master设备上的DHCP报文统计信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的DHCP报文统计信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示全局主用主控板上的DHCP报文统计信息。（分布式设备---IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的DHCP报文统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示全局主用主控板上的DHCP报文统计信息。（分布式设备---IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的DHCP报文统计信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示DHCP Snooping设备上的DHCP报文统计信息。

\<Sysname\> display dhcp snooping packet statistics

 DHCP packets received                  : 100

 DHCP packets sent                      : 200

 Invalid DHCP packets dropped           : 0

表1-17 display dhcp snooping packet statistics命令显示信息描述表

字段

描述

DHCP packets received

接收的DHCP报文数

DHCP packets sent

发送的DHCP报文数

Invalid DHCP packets dropped

丢弃的无效DHCP报文数

【相关命令】

·**reset dhcp snooping packet statistics**

**DHCP \-- DHCP Snooping配置命令 \-- display dhcp snooping trust**

------------------------------------------------------------------------

**[display** **dhcp** **snooping** **trust**]命令用来显示信任端口信息。

【命令】

**[display** **dhcp** **snooping** **trust**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示信任端口信息。

\<Sysname\> display dhcp snooping trust

 DHCP snooping is enabled.

 Interface                                       Trusted

 =========================                       ============

 GigabitEthernet1/0/1                            Trusted

表1-18 display dhcp snooping trust命令显示信息描述表

字段

描述

DHCP snooping is

DHCP Snooping功能的开启状态，取值包括：

·enable：启用DHCP Snooping功能{.TableTextChar}

·disable：未启用DHCP Snooping功能{.TableTextChar}

Interface

接口名称

Trusted

接口为信任接口

【相关命令】

·**dhcp** **snooping** **trust**

**DHCP \-- DHCP Snooping配置命令 \-- reset dhcp snooping binding**

------------------------------------------------------------------------

**[reset** **dhcp** **snooping binding**]命令用来清除DHCP Snooping表项。

【命令】

**[reset**[ **dhcp** **snooping** **binding** { **all** \| **ip** *ip-address* [ **vlan** *vlan-id* ] }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：清除所有的DHCP Snooping表项。

**[ip** *ip-address*]：清除指定IP地址对应的DHCP Snooping表项。

**[vlan ***vlan-id*]：清除指定VLAN内的DHCP Snooping表项

【使用指导】

对于分布式设备，执行该命令后，将清除所有槽位上对应的DHCP Snooping表项。

【举例】

\# 清除所有的DHCP Snooping表项。

\<Sysname\> reset dhcp snooping binding all

【相关命令】

·**display dhcp snooping binding**

**DHCP \-- DHCP Snooping配置命令 \-- reset dhcp snooping packet statistics**

------------------------------------------------------------------------

**[reset** **dhcp** **snooping** **packet** **statistics**]命令用来清除DHCP Snooping设备上的DHCP报文统计信息。

【命令】

集中式设备：

**[reset** **dhcp** **snooping** **packet** **statistics**]

分布式设备---独立运行模式/集中式IRF设备：

**[reset** **dhcp** **snooping** **packet** **statistics** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备---IRF模式：

**[reset** **dhcp** **snooping** **packet** **statistics** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：清除指定单板的DHCP报文统计信息。*slot-number*为单板所在的槽位号。如果未指定本参数，则清除主用主控板上的DHCP报文统计信息。（分布式设备---独立运行模式）

**[slot** *slot-number*]：清除指定成员设备的DHCP报文统计信息。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则清除Master设备上的DHCP报文统计信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：清除指定成员设备的DHCP报文统计信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则清除Master设备上的DHCP报文统计信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定成员设备上指定单板的DHCP报文统计信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则清除全局主用主控板上的DHCP报文统计信息。（分布式设备---IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定单板的DHCP报文统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则清除全局主用主控板上的DHCP报文统计信息。（分布式设备---IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：清除指定CPU上的DHCP报文统计信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 清除DHCP Snooping设备上的DHCP报文统计信息。

\<Sysname\> reset dhcp snooping packet statistics

【相关命令】

·**display** **dhcp** **snooping** **packet** **statistics**

**DHCP \-- BOOTP客户端配置命令 \-- display bootp client**

------------------------------------------------------------------------

**[display bootp client**]命令用来显示BOOTP客户端的相关信息。

【命令】

**[display** **bootp** **client** [ **interface** *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface** *interface-type interface-number*]：显示指定接口的BOOTP客户端相关信息。*interface-type interface-number*为接口类型和接口编号。

【使用指导】

如果不指定**interface** *interface-type interface-number*参数，则显示所有接口上的BOOTP客户端的相关信息。

【举例】

·路由应用

\# 显示接口GigabitEthernet1/0/1的BOOTP客户端相关信息。

\<Sysname\> display bootp client interface gigabitethernet 1/0/1

GigabitEthernet1/0/1 BOOTP client information:

 Allocated IP: 169.254.0.2 255.255.0.0

 Transaction ID: 0x3d8a7431

 MAC Address: 00e0-fc0a-c3ef

·交换应用

\# 显示VLAN接口10的BOOTP客户端相关信息。

\<Sysname\> display bootp client interface vlan-interface 10

Vlan-interface10 BOOTP client information:

 Allocated IP: 169.254.0.2 255.255.0.0

 Transaction ID: 0x3d8a7431

 MAC Address: 00e0-fc0a-c3ef

表1-19 display bootp client命令显示信息描述表

字段

描述

GigabitEthernet1/0/1 BOOTP client information/Vlan-interface10 BOOTP client information

作为BOOTP客户端的接口信息

Allocated IP

BOOTP服务器为BOOTP客户端分配的IP地址

Transaction ID

BOOTP报文中XID字段值，即BOOTP客户端发送BOOTP请求报文时选择的随机数，用来与BOOTP服务器的响应报文相匹配。如果响应报文的XID字段值与请求报文的XID字段值不相同，则BOOTP客户端丢弃该响应报文

MAC Address

BOOTP客户端的MAC地址

【相关命令】

·**ip address ****bootp-alloc**

**DHCP \-- BOOTP客户端配置命令 \-- ip address bootp-alloc**

------------------------------------------------------------------------

**[ip** **address** **bootp-alloc**]命令用来配置接口通过BOOTP协议获取IP地址。

**[undo** **ip** **address** **bootp-alloc**]命令用来取消接口通过BOOTP协议获取IP地址。

【命令】

**[ip** **address** **bootp-alloc**]

**[undo** **ip** **address** **bootp-alloc**]

【缺省情况】

接口不通过BOOTP协议获取IP地址。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

·路由应用

\# 在GigabitEthernet1/0/1接口上配置接口通过BOOTP协议获取IP地址。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ip address bootp-alloc

·交换应用

\# 在VLAN接口10上配置接口通过BOOTP协议获取IP地址。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 ip address bootp-alloc

【相关命令】

·**display** **bootp** **client**
