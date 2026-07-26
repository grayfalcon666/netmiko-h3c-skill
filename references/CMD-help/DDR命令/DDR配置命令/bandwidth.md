
**DDR命令 \-- DDR配置命令 \-- bandwidth**

------------------------------------------------------------------------

**[bandwidth**]命令用来配置接口的期望带宽。

**[undo bandwidth**]命令用来恢复缺省情况。

【命令】

**[bandwidth** *bandwidth-value*]

**[undo bandwidth**]

【缺省情况】

Dialer接口的期望带宽＝接口的波特率÷1000（kbit/s）。

【视图】

Dialer接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth-value*]：表示接口的期望带宽，取值范围为1～400000000，单位为kbit/s。

【使用指导】

接口的期望带宽会影响链路开销值，具体介绍请参见"三层技术-IP路由配置指导"中的"OSPF"、"OSPFv3"和"IS-IS"。

【举例】

\# 配置接口Dialer1的期望带宽为100kbit/s。

\<Sysname\> system-view

Sysname interface dialer 1

Sysname-Dialer1 bandwidth 100

**DDR命令 \-- DDR配置命令 \-- default**

------------------------------------------------------------------------

**[default**]命令用来恢复当前接口的缺省配置。

【命令】

**[default**]

【视图】

Dialer接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。

您可以在执行**default**命令后通过**display this**命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。

【举例】

\# 将接口Dialer1恢复为缺省配置。

\<Sysname\> system-view

Sysname interface dialer 1

Sysname-Dialer1 default

**DDR命令 \-- DDR配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来设置当前接口的描述信息。

**[undo description**]命令用来恢复缺省情况。

【命令】

**[description** *text*]

**[undo description**]

【缺省情况】

接口的描述信息为"*该接口的接口名* Interface"，比如：Dialer1 Interface。

【视图】

Dialer接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：接口描述信息，为1～255个字符的字符串，区分大小写。

【举例】

\# 设置接口Dialer1的描述信息为"dialer-intf"。

\<Sysname\> system-view

Sysname interface dialer 1

Sysname-Dialer1 description dialer-intf

**DDR命令 \-- DDR配置命令 \-- dialer bundle enable**

------------------------------------------------------------------------

**[dialer bundle enable**]命令用来使能共享DDR。

**[undo dialer bundle enable**]命令用来禁止共享DDR。

【命令】

**[dialer bundle enable**]

**[undo dialer bundle enable**]

【缺省情况】

接口上不使能任何类型的DDR。

【视图】

Dialer接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

DDR分为共享DDR和传统DDR。

用户在使用共享DDR前，必须首先使用**dialer** **bundle** **enable**命令使能共享DDR功能，然后在物理接口下配置**dialer** **bundle-member**将物理接口加入共享DDR中。如果此共享DDR还需要支持入呼叫则还需要在Dialer接口下配置**dialer peer-name**。

在已经使能了传统DDR的Dialer接口上配置**dialer bundle enable**命令，系统会清除原有的传统DDR相关的拨号配置。

在使用**undo dialer bundle enable**命令后，系统将清除拨号接口下的所有DDR配置信息。

【举例】

\# 在接口Dialer1上使能共享DDR。

\<Sysname\> system-view

Sysname interface dialer 1

Sysname-Dialer1 dialer bundle enable

【相关命令】

·**dialer** **bundle-member**

·**dialer circular enable**

·**dialer peer-name**

**DDR命令 \-- DDR配置命令 \-- dialer bundle-member**

------------------------------------------------------------------------

**[dialer bundle-member**]命令用来在共享DDR中，将物理接口加入某个Dialer bundle。

**[undo dialer bundle-member**]命令用来取消该配置。

【命令】

**[dialer bundle-member ***number***** **priority** *priority* ]

**[undo dialer bundle-member** *number*]

【缺省情况】

物理接口不属于任何一个Dialer bundle。

【视图】

物理接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：物理接口所属的Dialer bundle的序号。该序号要与Dialer接口的编号相同。

**[priority*** priority*]：物理接口在该Dialer bundle中的优先级。*priority*取值范围为1～255，缺省值为1。*priority*值越大，优先级越高，优先级高的物理接口会被优先使用，优先级相同时，会轮询选择各物理接口。

【使用指导】

一个物理接口可以是多个Dialer bundle的成员。多次执行本命令可以将一个物理接口加入不同的Dialer bundle。

当Dialer接口不存在时，此命令会创建对应的Dialer接口，并且在Dialer接口上使能共享DDR。

【举例】

\# 设置接口BRI2/4/0属于Dialer bundle1和Dialer bundle2，优先级均为50。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 dialer bundle-member 1 priority 50

Sysname-Bri2/4/0 dialer bundle-member 2 priority 50

【相关命令】

·**dialer bundle enable**

·**interface dialer**

**DDR命令 \-- DDR配置命令 \-- dialer callback-center**

------------------------------------------------------------------------

**[dialer callback-center**]命令用来配置PPP回呼的参照依据。

**[undo dialer callback-center**]命令用来取消该配置。

【命令】

**[dialer callback-center**[ [ **dial-number** \| **user** ] \*]]

**[undo dialer callback-center**]

【缺省情况】

未配置PPP回呼的参照依据，无法进行PPP回呼。

【视图】

拨号接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[dial-number**]：根据配置的本地用户名对应的**authorization-attribute callback-number ***callback-number*命令中的参数*callback-number*确定回呼的拨号串。

**[user**]：根据配置的**dialer route**命令中的参数**user ***hostname*确定回呼的拨号串。

【使用指导】

当设备作为PPP回呼的Server端时，必须配置本命令。

当**user**和**dial-number**两个参数同时被应用时，设备首先尝试按照第一个参数的设置进行回呼，当无法进行回呼时，再尝试应用第二个参数的设置进行回呼。**dialer callback-center**命令不带任何参数与**dialer callback-center** **user dial-number**命令功能相同。

【举例】

\# 配置设备作为PPP回呼的Server端，并且设置回呼方式为**user**，根据**dialer route**命令中配置的用户名对应的拨号串进行回呼。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 ppp callback server

Sysname-Serial2/1/0 dialer callback-center user

Sysname-Serial2/1/0 dialer route ip 1.1.1.2 8810052 user Sysnameb

\# 配置设备作为PPP回呼的Server端，回呼方式为**dial-number**，根据PPP认证中接收的对端用户名查找本地用户表确定回呼的拨号串。

\<Sysname\> system-view

Sysname local-user usera

Sysname-luser-usera password simple usera

Sysname-luser-usera service-type ppp

Sysname-luser-usera authorization-attribute callback-number 8810048

Sysname-luser-usera quit

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 ppp callback server

Sysname-Serial2/1/0 dialer callback-center dial-number

【相关命令】

·**ppp callback**

**DDR命令 \-- DDR配置命令 \-- dialer call-in**

------------------------------------------------------------------------

**[dialer call-in**]命令用来配置允许呼入的ISDN主叫号码，或按照该ISDN主叫号码进行回呼。

**[undo dialer call-in**]命令用来取消该配置。

【命令】

**[dialer call-in** *remote-number* [ **callback** ]]

**[undo dialer call-in** *remote-number*]

【缺省情况】

未配置按照ISDN主叫号码来过滤呼叫。

【视图】

拨号接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[remote-number*]：ISDN主叫号码，为1～30个字符的字符串，不区分大小写，字符"\*"通配任意一个字符。

**[callback**]：如果ISDN主叫号码与参数*remote-number*相匹配，则设备发起回呼。

【使用指导】

**[dialer call-in**]命令用来对ISDN拨入进行预处理，以确定该主叫号码用户是否允许呼入，如果程控交换机没有提供主叫号码则直接拒绝该呼叫。

当**dialer call-in**命令中携带了**callback**参数时，在配置了**dialer call-in**的拨号接口上同时需要配置**dialer route**或者**dialer number**命令，**dialer route**或者**dialer number**命令中的*dial-number*要与**dialer call-in**命令中的*remote-number*一致，以保证进行正确的回呼。

【举例】

\# 设置向ISDN主叫号码为8810152的用户进行回呼。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 dialer route ip 100.1.1.2 8810152

Sysname-Bri2/4/0 dialer call-in 8810152 callback

【相关命令】

·**dialer callback-center**

**DDR命令 \-- DDR配置命令 \-- dialer circular enable**

------------------------------------------------------------------------

**[dialer circular enable**]命令用来使能传统DDR。

**[undo dialer circular enable**]命令用来禁止传统DDR。

【命令】

**[dialer circular enable**]

**[undo dialer circular enable**]

【缺省情况】

接口上不使能任何类型的DDR。

【视图】

拨号接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

DDR分为共享DDR和传统DDR。

用户在使用传统DDR前，必须首先使用**dialer circular enable**命令使能传统DDR功能。

在已经使能了共享DDR的Dialer接口上配置**dialer circular enable**命令，系统会清除原有的共享DDR相关的拨号配置。

在使用**undo dialer circular enable**命令后，系统将清除拨号接口下的所有DDR配置信息。

【举例】

\# 在接口Serial2/1/0上使能传统DDR。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 dialer circular enable

【相关命令】

·**dialer bundle enable**

·**dialer circular-group**

**DDR命令 \-- DDR配置命令 \-- dialer circular-group**

------------------------------------------------------------------------

**[dialer circular-group**]命令用来在传统DDR中，将物理接口加入某个拨号循环组。

**[undo dialer circular-group**]命令用来取消该配置。

【命令】

**[dialer circular-group** *number*]

**[undo dialer circular-group**]

【缺省情况】

物理接口不属于任何一个拨号循环组。

【视图】

物理接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：物理接口所属的拨号循环组的序号。该序号要与Dialer接口的编号相同。

【使用指导】

在传统DDR中，一个物理接口只能属于一个拨号循环组，一个拨号循环组可以包含多个物理接口。当有呼叫从一个拨号循环组上发起时，按照优先级从高到低从属于该拨号循环组的物理接口中选择一个物理接口建立呼叫。

当Dialer接口不存在时，此命令会创建对应的Dialer接口，并且在该Dialer接口上使能传统DDR。

【举例】

\# 将接口Serial2/1/0和Serial2/1/1加入拨号循环组1。

\<Sysname\> system-view

Sysname interface dialer 1

Sysname-Dialer1 quit

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 dialer circular-group 1

Sysname-Serial2/1/0 quit

Sysname interface serial 2/1/1

Sysname-Serial2/1/1 dialer circular-group 1

【相关命令】

·**dialer circular enable**

·**dialer priority**

·**interface dialer**

**DDR命令 \-- DDR配置命令 \-- dialer disconnect**

------------------------------------------------------------------------

**[dialer disconnect**]命令用来拆除拨号链路。

【命令】

**[dialer disconnect** **interface** *interface-type interface-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-type interface-number*]：拆除指定接口的拨号链路。*interface-type interface-number*用来指定接口类型和编号。如果不指定接口，则拆除所有接口的拨号链路。

【举例】

\# 拆除接口Dialer0的拔号链路。

\<Sysname\> dialer disconnect interface dialer 0

**DDR命令 \-- DDR配置命令 \-- dialer flow-interval**

------------------------------------------------------------------------

**[dialer flow-interval**]命令用来配置DDR提供流量统计信息的间隔时间。

**[undo dialer flow-interval**]命令用来恢复缺省情况。

【命令】

**[dialer flow-interval** *interval*]

**[undo dialer flow-interval**]

【缺省情况】

DDR提供流量统计信息的间隔时间为20秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：DDR提供流量统计信息的间隔时间，取值范围为1～1500，单位为秒。

【使用指导】

DDR以用户配置的时间间隔为MP捆绑提供拨号链路上的流量统计信息。

【举例】

\# 配置DDR提供流量统计信息的间隔时间为3秒。

\<Sysname\> system-view

Sysname dialer flow-interval 3

【相关命令】

·**dialer threshold**

**DDR命令 \-- DDR配置命令 \-- dialer number**

------------------------------------------------------------------------

**[dialer number**]命令用来设定呼叫单个对端的拨号串。

**[undo dialer number**]命令用来删除已设定的拨号串。

【命令】

**[dialer number** *dial-number* [ **autodial** ]]

**[undo dialer number**]

【缺省情况】

未配置呼叫对端的拨号串。

【视图】

拨号接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dial-number*]：呼叫对端的拨号串，为1～30个字符的字符串，不区分大小写。

**[autodial**]：表示自动拨号。如果配置了本参数，则路由器每隔一定时间会自动尝试拨号，拨号的时间间隔由命令**dialer timer autodial**设置，缺省的时间间隔为300秒。

【使用指导】

当Dialer接口或者物理接口作为主叫端，需要配置此命令。

需要注意的是：

·对于传统DDR，需要呼叫多个目的地址或拨号串时，可以配置**dialer route**命令来替代**dialer number**。

·对于共享DDR，只能使用**dialer number**命令配置拨号串，且一个Dialer接口只能配置一个拨号串。

【举例】

\# 设定接口Dialer1呼叫对端的拨号串为"11111"。

\<Sysname\> system-view

Sysname interface dialer 1

Sysname-Dialer1 dialer number 11111

【相关命令】

·**dialer route**

·**dialer timer autodial**

**DDR命令 \-- DDR配置命令 \-- dialer peer-name**

------------------------------------------------------------------------

**[dialer peer-name**]命令用来设置共享DDR应用的对端用户名，以便接收呼叫时能认证呼叫请求。

**[undo dialer peer-name**]命令用来删除共享DDR应用的对端用户名。

【命令】

**[dialer peer-name ***username*]

**[undo dialer peer-name ** *username* ]

【缺省情况】

没有配置共享DDR应用的对端用户名。

【视图】

Dialer接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[username*]：对端用户名，为1～80个字符的字符串，不区分大小写，用于PPP认证。

【使用指导】

Dialer接口利用PPP认证得到的对端用户名决定入呼叫时的Dialer接口。

该命令仅在共享DDR中有效。在一个Dialer接口下最多可以配置255个对端用户名。当一个Dialer接口下配置多个对端用户名时，就实现了用一个Dialer接口同时接入多个物理接口的连接。

当共享DDR接口下没有配置对端用户名时，此共享DDR可以支持出呼叫，无法支持入呼叫。当共享DDR接口下配置了对端用户名时，此共享DDR可以支持入呼叫。

【举例】

\# 设置共享DDR应用的对端用户名为routerb。

\<Sysname\> system-view

Sysname interface dialer 1

Sysname-Dialer1 dialer peer-name routerb

**DDR命令 \-- DDR配置命令 \-- dialer priority**

------------------------------------------------------------------------

**[dialer priority**]命令用来配置传统DDR，设置物理接口在其所在的拨号循环组中的优先级。

**[undo dialer priority**]命令用来恢复缺省情况。

【命令】

**[dialer priority** *priority*]

**[undo dialer priority**]

【缺省情况】

物理接口在拨号循环组中的优先级为1。

【视图】

物理接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[priority*]：物理接口在拨号循环组中的优先级，取值范围为1～127，数值越大优先级越高。

【使用指导】

此命令设定物理接口在其所在的拨号循环组中的使用顺序，高优先级的物理接口会被优先使用。优先级相同时，会轮询选择各物理接口。

【举例】

\# 设置接口Serial2/1/0在拨号循环组1中的优先级为5。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 dialer circular-group 1

Sysname-Serial2/1/0 dialer priority 5

【相关命令】

·**dialer circular-group**

**DDR命令 \-- DDR配置命令 \-- dialer queue-length**

------------------------------------------------------------------------

**[dialer queue-length**]命令用来设定拨号接口缓冲队列长度。

**[undo dialer queue-length**]命令用来恢复缺省情况。

【命令】

**[dialer queue-length** *packets*]

**[undo dialer queue-length**]

【缺省情况】

不对报文进行缓存。

【视图】

拨号接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[packets*]：接口缓存的数据报文个数，取值范围为1～100。

【使用指导】

没有为拨号接口配置缓冲队列的情况下，当拨号接口收到一个报文时，如果此时连接还没有成功建立，则这个报文将被丢弃。如果为拨号接口配置了缓冲队列，则在连接成功建立之前报文将被缓存，待连接成功后再发送。

【举例】

\# 设置接口Serial2/1/0的接口缓冲队列长度为10。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 dialer queue-length 10

**DDR命令 \-- DDR配置命令 \-- dialer route**

------------------------------------------------------------------------

**[dialer route**]命令用来配置从一个拨号接口呼叫指定目的地址，或接收对端的呼叫。

**[undo dialer route**]命令用来删除该配置。

【命令】

**[dialer route** **ip** *next-hop-address* [ **mask** *network-mask-length*   **vpn-instance** *vpn-instance-name*  [ *dial-number* [ **autodial** \| **interface** *interface-type interface-number* ] \*   **broadcast** \| **user** *hostname* ] \*]]

**[undo dialer route** *protocol next-hop-address* [ **mask** *network-mask-length*   **vpn-instance** *vpn-instance-name*   *dial-number* ]]

【视图】

拨号接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip**]：网络协议为IP协议。

*[next-hop-address*]：拨号对端的IP地址。

**[mask*** network-mask-length*]：拨号对端IP地址的掩码长度，取值范围为0～32。若不设置该参数则系统默认为32，此时就把*next-hop-address*当成主机地址处理。若用户需要把*next-hop-address*配置成网段地址，则需要指定它的*network-mask-length*。当*next-hop-address*取值为0.0.0.0并且*network-mask-length*取值为0时，表示不限制对端的IP地址，例如**dialer route ip** 0.0.0.0 **mask** 0 8886，表示允许通过8886号码拨叫任何IP地址。

**[vpn-instance** *vpn-instance-name*]：MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。

*[dial-number*]：去往对端的拨号串，为1～30个字符的字符串，不区分大小写。如果配置了此拨号串，则可以进行出方向拨号，否则只能接受入方向拨号。

**[autodial**]：表示自动拨号。如果配置了本参数，则路由器每隔一定时间会自动尝试拨号，拨号的时间间隔由命令**dialer timer autodial**设置，缺省的时间间隔为300秒。

**[interface ***interface-type interface-number*]：使用指定的物理接口拔号。当几个物理接口绑定到一个Dialer口，且这几条拔号链路连接到不同的程控交换机时，需要配置指定拔号号码与物理接口的对应关系。此参数只能在使能传统DDR的Dialer口上配置。

**[broadcast**]：表示可以从本条拨号链路发送广播报文。

**[user*** hostname*]：对端用户名，为1～80个字符的字符串，不区分大小写，用于接收呼叫时进行认证。

【使用指导】

如果需要DDR主动呼叫，则需使用*dial-number*参数来配置拨号串。如果不配置*dial-number*参数，则只能接收对端的呼叫。

如果配置了某个IP地址*next-hop-address*对应的拨号串*dial-number*，那么使用**undo**命令时必须包含*dial-number*参数。

如果使用**user**关键字，则必须配置相关的PPP认证（通过PPP认证获取对端的用户名，然后判断这个用户名和本命令中配置的用户名是否一致，如果一致，才接收呼叫）。

一个拨号接口可以配置多条**dialer route**，对应同一个目的地址也可配置多条**dialer route**命令指定多个拨号串以实现拨号串备份的功能。

【举例】

\# 配置去往192.168.1.0/24网段的数据包都拨叫888066号码建立链路。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 dialer route ip 192.168.1.0 mask 24 888066

\# 配置去往191.168.1.1主机地址的数据包拨叫888065号码建立链路。

Sysname-Serial2/1/0 dialer route ip 191.168.1.1 888065

【相关命令】

·**dialer timer autodial**

**DDR命令 \-- DDR配置命令 \-- dialer threshold**

------------------------------------------------------------------------

**[dialer threshold**]命令用来设定Dialer接口上链路的负载阈值，当Dialer接口的所有链路的流量与可用带宽的比例超过设定的百分比时，启动另一条链路呼叫同一个目的地址。

**[undo dialer threshold**]命令用来恢复缺省情况。

【命令】

**[dialer threshold ***traffic-percentage *[[ **in** \| **in-out** \| **out** ]]]

**[undo dialer threshold**]

【缺省情况】

不启动该功能。

【视图】

Dialer接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[traffic-percentage*]：链路实际流量与带宽的百分比，取值范围为0～99。

**[in**]：计算实际负载时只计算接收的流量。

**[in-out**]：计算实际负载时计算接收和发送流量中较大的一个。

**[out**]：计算实际负载时只计算发送的流量。

【使用指导】

在DDR应用中，可以配置链路的负载阈值。当负载阈值在1～99之间时，MP捆绑根据实际流量百分比适当调节分配的带宽，即如果一条链路的实际流量与带宽的比例超过设定的负载阈值，则系统会自动启用第二条链路，并将两条链路进行MP捆绑；当两条链路的流量与带宽的比例超过设定的负载阈值，系统会启动第三条链路并进行MP捆绑，依此类推，从而确保DDR链路具有合理的负载流量。

相反，若N条（N为大于等于2的整数）链路的流量与N-1条链路带宽的比例小于设定的负载阈值时，系统自动关闭一条链路，以此类推，从而确保DDR链路的利用率保持在合理范围。

目前，本命令只能用于Dialer接口，用于物理接口不生效。另外，本命令须与**ppp mp**命令结合使用。

参数*traffic-percentage*值为0时，在链路由于自动拨号或者报文触发拨号而开始呼叫的时候，将自动启动所有可用的链路进行呼叫，而不依靠流量检测决定呼叫策略，对于已经呼叫建立的链路也不会因为超时而主动拆链，也就是说，**dialer timer idle**命令在配置了**dialer threshold **0之后将会失效。

DDR按照**dialer** **flow-interval**配置的时间间隔来定时进行流量统计。

【举例】

\# 设置接口Dialer1的负载阈值为80%。

\<Sysname\> system-view

Sysname interface dialer 1

Sysname-Dialer1 dialer threshold 80

【相关命令】

·**dialer flow-interval**

·**dialer timer idle**

·**ppp mp**（二层技术-广域网接入命令参考/PPP）

**DDR命令 \-- DDR配置命令 \-- dialer timer autodial**

------------------------------------------------------------------------

**[dialer timer autodial**]命令用来配置DDR自动拨号的间隔时间。

**[undo dialer timer autodial**]命令用来恢复缺省情况。

【命令】

**[dialer timer autodial** *autodial-interval*]

**[undo dialer timer autodial**]

【缺省情况】

DDR自动拨号的间隔时间为300秒。

【视图】

拨号接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[autodial-interval*]：发起下次呼叫尝试的间隔时间，取值范围为1～604800，单位为秒。

【使用指导】

该命令必须与**dialer number**或**dialer route**命令中的关键字**autodial**结合使用。配置该命令后，DDR将每隔*autodial-interval*时间自动尝试拨号一次，直至连接建立。自动拨号功能无需数据包的触发，并且在连接建立后不会因空闲时间超时而自动挂断，即**dialer timer idle**命令配置对其无效。

【举例】

\# 在接口Serial2/1/0上设置DDR自动拨号的间隔时间为60秒。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 dialer timer autodial 60

【相关命令】

·**dialer number**

·**dialer route**

**DDR命令 \-- DDR配置命令 \-- dialer timer compete**

------------------------------------------------------------------------

**[dialer timer compete**]命令用来配置当接口发生呼叫竞争后的链路空闲时间。

**[undo dialer timer compete**]命令用来恢复缺省情况。

【命令】

**[dialer timer compete** *compete-idle*]

**[undo dialer timer compete**]

【缺省情况】

接口发生呼叫竞争后的链路空闲时间为20秒。

【视图】

拨号接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[compete-idle*]：接口发生呼叫竞争后的链路空闲时间，取值范围为0～65535，单位为秒。

【使用指导】

通常一条链路建立后Idle超时定时器将起作用。当DDR开始发起新呼叫时，若所有物理接口都被占用则进入"竞争"状态，此时DDR使用Compete-idle超时定时器取代Idle超时定时器，即链路空闲时间超过Compete-idle超时定时器的时间后将自动断开。

【举例】

\# 在接口Serial2/1/0上设置接口发生呼叫竞争后的链路空闲时间为10秒。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 dialer timer compete 10

**DDR命令 \-- DDR配置命令 \-- dialer timer enable**

------------------------------------------------------------------------

**[dialer timer enable**]命令用来配置接口上当链路断开后进行下次呼叫的间隔时间。

**[undo dialer timer enable**]命令用来恢复缺省情况。

【命令】

**[dialer timer enable** *interval*]

**[undo dialer timer enable**]

【缺省情况】

接口上当链路断开后进行下次呼叫的间隔时间为5秒。

【视图】

拨号接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：当链路断开后进行下次呼叫的间隔时间，取值范围为5～65535，单位为秒。

【使用指导】

当DDR呼叫链路因故障或挂断等原因进入断开状态，必须经过指定时间（即进行下一次呼叫的间隔时间）后才能建立新的拨号连接，从而避免对端程控交换机过载。

需要注意的是：为了使Server端有足够的时间进行回呼，Client端当链路断开后进行下次呼叫的间隔时间应至少比Server端的长10秒。建议Server端使用默认值5秒，Client端配置为15秒。

【举例】

\# 设置当链路断开后进行下次呼叫的间隔时间为15秒。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 dialer timer enable 15

**DDR命令 \-- DDR配置命令 \-- dialer timer idle**

------------------------------------------------------------------------

**[dialer timer idle**]命令用来设定当接口的呼叫建立后，允许链路空闲的时间。

**[undo dialer timer idle**]命令用来恢复缺省情况。

【命令】

**[dialer timer idle**[ *idle* [ **in** \| **in-out** ]]]

**[undo dialer timer idle**]

【缺省情况】

允许链路空闲的时间为120秒，只有出方向的感兴趣报文报文重置定时器。

【视图】

拨号接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[idle*]：允许链路空闲的时间，取值范围为0～65535，单位为秒。

**[in**]：只有入方向的感兴趣报文重置定时器。

**[in-out**]：出方向和入方向的感兴趣报文都重置定时器。

【使用指导】

当一条链路建立后，**dialer timer idle**定时起作用。若在设定的时间内没有感兴趣报文在此链路上传送，则DDR自动挂断链路。

需要注意的是：

·如果配置命令时不指定**in**和**in-out**参数，则表示只有出方向的感兴趣报文重置定时器。

·若**dialer timer idle**设定为0，则相应的链路在建立后，无论是否有感兴趣报文在此链路上传送，链路将永远不被挂断。对于PPPoE Client应用，若**dialer timer idle**设定为0，则将会自动触发拨号保证链接永久在线。

【举例】

\# 设置接口Serial2/1/0允许链路空闲的时间为50秒。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 dialer timer idle 50

**DDR命令 \-- DDR配置命令 \-- dialer timer wait-carrier**

------------------------------------------------------------------------

**[dialer timer wait-carrier**]命令用来设定呼叫建立超时定时器（wait-carrier定时器）的超时时间。

**[undo dialer timer wait-carrier**]命令用来恢复缺省情况。

【命令】

**[dialer timer wait-carrier** *wait-carrier*]

**[undo dialer timer wait-carrier**]

【缺省情况】

呼叫建立超时时间为60秒。

【视图】

拨号接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[wait-carrier*]：呼叫建立超时时间，取值范围为0～65535，单位为秒。

【使用指导】

和某些对端建立DDR呼叫时，从呼叫发起到连接建立的时间长短不一，为了有效控制发起呼叫到呼叫连接建立之间允许等待的时间，可以配置wait-carrier定时器，若在指定时间内呼叫仍未建立，则DDR将终止该呼叫。

【举例】

\# 设置接口Serial2/1/0的呼叫建立超时时间为100秒。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 dialer timer wait-carrier 100

**DDR命令 \-- DDR配置命令 \-- dialer timer warmup**

------------------------------------------------------------------------

![说明](DDR命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[dialer timer warmup**]命令用来设置动态路由备份功能在系统启动后的生效延时。

**[undo dialer timer warmup**]命令用来恢复缺省情况。

【命令】

**[dialer timer warmup** *delay*]

**[undo dialer timer warmup**]

【缺省情况】

动态路由备份功能在系统启动30秒后生效。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[delay*]：动态路由备份功能在系统启动后不生效的时间，取值范围为0～65535，单位为秒。

【使用指导】

配有动态路由备份功能的路由器在启动时，主链路如果在本命令配置的时间内没有协商UP，系统就会触发拨号备份链路；当主链路UP后，系统会切换回主链路。

【举例】

\# 设置动态路由备份功能在系统启动20秒后开始生效。

\<Sysname\> system-view

Sysname dialer timer warmup 20

**DDR命令 \-- DDR配置命令 \-- dialer-group**

------------------------------------------------------------------------

**[dialer-group**]命令用来配置接口关联的拨号访问组，将该接口与拨号控制规则关联起来。

**[undo dialer-group**]命令用来恢复缺省情况。

【命令】

**[dialer-group** *group-number*]

**[undo dialer-group**]

【缺省情况】

接口不与任何拨号访问组相关联。

【视图】

拨号接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-number*]：接口关联的拨号访问组的序号，这个序号由**dialer-group rule**命令设定，取值范围为1～255。

【使用指导】

一个拨号接口只能关联一个拨号访问组，重复配置**dialer-group**命令则会覆盖上一次的配置。

用户必须配置**dialer-group**命令，否则DDR将无法发送报文。

【举例】

\# 配置接口Serial2/1/0关联拨号访问组1。

\<Sysname\> system-view

Sysname dialer-group 1 rule acl 3101

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 dialer-group 1

【相关命令】

·**dialer-group rule**

**DDR命令 \-- DDR配置命令 \-- dialer-group rule**

------------------------------------------------------------------------

**[dialer-group rule**]命令用来创建拨号访问组，并配置拨号控制规则。

**[undo dialer-group rule**]命令用来取消该设置。

【命令】

**[dialer-group**[ *group-number* **rule** { *protocol-name* { **deny** \| **permit** } \| **acl** { *acl-number* \| **name** *acl-name* } }]]

**[undo dialer-group** *group-number* **rule**]

【缺省情况】

不存在拨号访问组。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-number*]：拨号访问组的序号，取值范围为1～255。

*[protocol-name*]：网络协议名，只能为**ip**（表示IP协议）。

**[deny**]：表示禁止相应协议的报文。

**[permit**]：表示允许相应协议的报文。

*[acl-number*]：拨号访问组引用的ACL（Access Control List，访问控制列表）序号，取值范围为2000～3999。

**[name*** acl-name*]：拨号访问组引用的ACL的名称。

【使用指导】

接口的DDR拨号控制规则用于控制接口什么时候发起DDR呼叫。用户需要在DDR呼叫的发起端配置接口的DDR拨号控制规则，在DDR呼叫的接收端不用配置接口的DDR拨号控制规则。

DDR拨号控制规则有如下两种：

·根据协议类型过滤报文：本方法目前只能匹配IP协议报文。

·根据ACL过滤报文：本方法可以对报文进行更精细的区分。

根据匹配DDR拨号控制规则的结果，报文分为两种：

·感兴趣报文：permit的协议报文或者符合ACL的permit条件的报文。

·非感兴趣报文：deny的协议报文或者不符合ACL的permit条件的报文或者没有匹配任何规则的报文。

对上述两种报文的处理方式如下：

·对于感兴趣报文：如果相应链路没有建立，则发起新呼叫建立链路并发送报文；如果相应链路已经建立，DDR将通过该链路发送报文，并重置Idle超时定时器。

·对于非感兴趣报文：如果相应链路没有建立，则不发起呼叫并丢弃此报文；如果相应链路已经建立，DDR将通过此链路发送报文，但是不重置Idle超时定时器。

用户必须配置DDR拨号控制规则，并将拨号接口通过**dialer-group**命令与拨号控制规则关联起来，DDR才能正常拨号。

【举例】

\# 设置拨号访问组1，对IP协议报文进行DDR拨号，并将它与接口Serial2/1/0关联。

\<Sysname\> system-view

Sysname dialer-group 1 rule ip permit

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 dialer-group 1

【相关命令】

·**dialer-group**

**DDR命令 \-- DDR配置命令 \-- display dialer**

------------------------------------------------------------------------

**[display dialer**]命令用来显示接口的DDR信息。

【命令】

**[display dialer** [ **interface** *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface** *interface-type interface-number*]：显示指定接口的DDR信息。*interface-type interface-number*用来指定接口类型和编号。如果不指定接口，则显示所有接口的DDR信息。

【举例】

\# 显示所有接口的DDR信息。

\<Sysname\> display dialer

Dialer0:

  Dialer Route:

    NextHop: 111.111.111.111  Dialer number: 123456789012345678901234567890

    NextHop: 222.222.222.222  Dialer number: 123456789012345678901234567890

  Dialer number:

  Dialer Timers(in seconds):

    Auto-dial: 300       Compete: 20            Enable: 5

    Idle: 120            Wait-for-Carrier: 60

  Total Channels: 1

  Free Channels: 1

表1-1 display dialer命令显示信息描述表

字段

描述

Dialer0

DDR接口，可以是Dialer接口也可以是物理接口

Dialer Route:

  NextHop: 111.111.111.111  Dialer number: 123456789012345678901234567890

在接口上配置的**dialer route**命令指定的对端IP地址，以及对应对端IP地址的拨号串

Dialer number

呼叫单个对端的拨号串

Dialer Timers(in seconds):

  Auto-dial: 300       Compete: 20            Enable: 5

  Idle: 120            Wait-for-Carrier: 60

在接口上配置的拨号定时器设置，单位为秒，包括：

·Auto-dial：**dialer timer autodial**命令设定的DDR自动拨号的间隔时间

·Compete：**dialer timer compete**命令设定的当接口发生呼叫竞争后的空闲时间

·Enable：**dialer timer enable**命令设定的当链路断开后进行下次呼叫的间隔时间

·Idle：**dialer timer idle**命令设定的当接口的呼叫建立后，允许链路空闲的时间

·Wait-for-Carrier：**dialer timer wait-carrier**命令设定的呼叫建立超时定时器（wait-carrier定时器）的超时时间

Total Channels

该接口总共的通道数（通道数指的是物理接口的个数，对于ISDN接口来说，指的是B通道的个数）

Free Channels

空闲的通道数

**DDR命令 \-- DDR配置命令 \-- display interface dialer**

------------------------------------------------------------------------

**[display interface dialer**]命令用来显示Dialer接口的相关信息。

【命令】

**[display interface **[ **dialer** [ *interface-number*    **brief** [ **description** \| **down** ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-number*]：显示指定Dialer接口的信息。*interface-number*表示Dialer接口的编号，取值范围为已创建的Dialer接口的编号。

**[brief**]：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。

**[description**]：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过27个字符，不指定该参数时，只显示描述信息中的前27个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。

**[down**]：显示当前物理状态为down的接口的信息以及down的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。

【使用指导】

·如果不指定**dialer**参数，将显示设备支持的所有接口的相关信息；

·如果指定**dialer**参数，不指定*interface-number*参数，将显示所有已创建的Dialer接口的相关信息。

【举例】

\# 显示接口Dialer1的详细信息。

\<Sysname\> display interface dialer 1

Dialer1

Current state: UP

Line protocol state: UP (spoofing)

Description: Dialer1 Interface

Bandwidth: 64kbps

Maximum Transmit Unit: 1500

Hold timer: 10 seconds, retry times: 5

Internet protocol processing: disabled

Link layer protocol: PPP

LCP: initial

Physical: Dialer, baudrate: 64000 bps

Output queue: (Urgent queuing: Length) 50

Output queue: (Protocol queuing: Length) 500

Output queue: (FIFO queuing: Length) 75

Last clearing of counters: Never

Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

Input: 0 packets, 0 bytes, 0 droped

Output: 0 packets, 0 bytes, 0 droped

\# 显示接口Dialer1的概要信息。

\<Sysname\> display interface dialer 1 brief

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Protocol: (s) - spoofing

Interface            Link Protocol Main IP         Description

Dia1                 UP   UP(s)    \--

\# 显示当前物理状态为down的Dialer接口的信息以及down的原因。

\<Sysname\> display interface dialer brief down

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Interface              Link Cause

Dia1                   ADM  Administratively

表1-2 display interface dialer命令显示信息描述表

字段

描述

Dialer1

Current state

接口当前的物理状态，可能的取值及含义如下：

·UP：该接口的物理状态为开启

·DOWN（Administratively）：表示该接口已经通过**shutdown**命令被关闭，需要通过**undo shutdown**命令开启

Line protocol state

接口的链路层协议状态，可能的状态及含义如下：

·UP：表示数据链路层协议状态为开启

·DOWN：表示数据链路层协议状态为关闭

Description

接口的描述信息

Bandwidth

接口的期望带宽

Maximum Transmit Unit

接口的最大传输单元

Hold timer

该接口发送keepalive报文的周期

retry times

在多少个keepalive周期内没有收到keepalive报文的应答就拆除链路

Internet protocol processing

网络层协议处理状况

Link layer protocol

链路层封装的协议

LCP: initial

LCP（链路控制协议）初始化完成

Physical

接口的物理类型

baudrate

接口的波特率

Output queue: (Urgent queuing : Length)

紧急发送队列的报文统计

Output queue: (Protocol queuing : Length)

协议发送队列的报文统计

Output queue: (FIFO queuing : Length)

先入先出发送队列的报文统计

Last clearing of counters: Never

最后一次清除接口统计信息的时间（Never表示未清除过接口的统计信息）

Last 300 seconds input rate

最近五分钟时间内接口的输入速率

Last 300 seconds output rate

最近五分钟时间内接口的输出速率

Input: 0 packets, 0 bytes, 0 droped

该接口接收的数据报文个数、字节数，以及由于没有接收缓冲而被丢弃的报文个数

Output: 0 packets, 0 bytes, 0 droped

该接口发送的数据报文个数、字节数，以及由于没有发送缓冲而被丢弃的报文个数

Brief information on interface(s) under route mode:

三层接口的概要信息

Link: ADM - administratively down; Stby - standby

·如果某接口的Link属性值为"ADM"，则表示该接口被管理员手工关闭了，需要在该接口下执行**undo shutdown**命令才能恢复接口本身的物理状态

·如果某接口的Link属性值为"Stby"，则表示该接口是一个备份接口，使用**display interface-backup state**命令可以查看该备份接口对应的主接口

Protocol: (s) - spoofing

如果某接口的Protocol属性值中带有"(s)"，则表示该接口的数据链路层协议状态显示为UP，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的

Interface

接口名称缩写

Link

接口物理连接状态，取值可能为：

·UP：表示接口物理上是连通的

·ADM：表示接口被手工关闭了，需要执行**undo shutdown**命令才能打开接口

·Stby：表示该接口是一个备份接口

Protocol

接口数据链路层协议状态，取值可能为：

·UP：表示接口的数据链路层是连通的

·DOWN：表示接口的数据链路层不通

·UP(s)：表示接口的数据链路层协议状态显示为UP，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的

Main IP

接口主IP地址

Description

用户通过**description**命令给接口配置的描述信息。使用**display interface brief**命令，不指定**description**参数时，该字段最多显示27个字符；指定**description**参数时，可显示配置的全部描述信息

Cause

接口物理连接状态为down的原因，取值为Administratively时表示本链路被手工关闭了（配置了**shutdown**命令），需要执行**undo shutdown**命令才能恢复真实的物理状态；取值为Not connected时表示没有物理连接（可能没有插网线或者网线故障）

【相关命令】

·**reset counters interface**

**DDR命令 \-- DDR配置命令 \-- interface dialer**

------------------------------------------------------------------------

**[interface dialer**]命令用创建一个Dialer接口。如果当前已经配置该接口，此命令用来进入该接口视图。

**[undo interface dialer**]命令用来删除一个指定的Dialer接口。

【命令】

**[interface dialer** *number*]

**[undo interface dialer** *number*]

【缺省情况】

未创建Dialer接口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：Dialer接口序号，取值范围为0～1023。

【使用指导】

Dialer接口的波特率恒定为64000bps。

【举例】

\# 创建一个接口Dialer1。

\<Sysname\> system-view

Sysname interface dialer 1

**DDR命令 \-- DDR配置命令 \-- mtu**

------------------------------------------------------------------------

**[mtu**]命令用来设置接口的MTU（Maximum Transmission Unit，最大传输单元）值。

**[undo mtu**]命令用来恢复缺省情况。

【命令】

**[mtu** *size*]

**[undo mtu**]

【缺省情况】

Dialer接口的MTU值为1500字节。

【视图】

Dialer接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size*]：接口的MTU值，单位为字节。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

接口的MTU值影响IP协议报文在该接口上传输时的分片与重组。

【举例】

\# 设置接口Dialer1的MTU值为1200字节。

\<Sysname\> system-view

Sysname interface dialer 1

Sysname-Dialer1 mtu 1200

**DDR命令 \-- DDR配置命令 \-- ppp callback**

------------------------------------------------------------------------

**[ppp callback**]命令用来允许PPP发送或接受回呼请求。

**[undo ppp callback**]命令用来禁止PPP发送或接受PPP回呼请求。

【命令】

**[ppp callback**[ { **client** \| **server** }]]

**[undo ppp callback**[ { **client** \| **server** }]]

【缺省情况】

系统未启动回呼功能。

【视图】

拨号接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在PPP回呼的配置中，需要配置发送呼叫方作为Client端，同时配置接受呼叫方作为Server端。由Client端首先发起呼叫，Server端确认该呼叫是否进行回呼，若需要回呼，Server端则立即挂断该次呼入连接，并根据用户名或回呼字符串等信息向Client端再次发起呼叫。

利用PPP回呼功能可以为PPP Client端节省通信费用。

【举例】

\# 配置接口Serial2/1/0允许接受回呼请求。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 ppp callback server

**DDR命令 \-- DDR配置命令 \-- ppp callback ntstring**

------------------------------------------------------------------------

**[ppp callback ntstring**]命令用来设置从Windows NT Server回呼路由器时所需要的拨号串。

**[undo ppp callback ntstring**]命令用来取消设置的回呼拨号串。

【命令】

**[ppp callback ntstring** *dial-number*]

**[undo ppp callback ntstring**]

【缺省情况】

没有设置Windows NT Server回呼拨号串。

【视图】

拨号接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dial-number*]：从Windows NT Server回呼路由器的拨号串，为1～64个字符的字符串，区分大小写。

【使用指导】

当路由器作为PPP回呼的Client端呼叫作为PPP回呼Server端的Windows NT Server时，如果NT Server需要路由器发送回呼号码，则需要配置此命令。

【举例】

\# 设定从Windows NT Server回呼路由器的拨号串为1234567。

\<Sysname\> system-view

Sysname interface dialer 1

Sysname-Dialer1 ppp callback ntstring 1234567

**DDR命令 \-- DDR配置命令 \-- reset counters interface**

------------------------------------------------------------------------

**[reset counters interface**]命令用来清除Dialer接口的统计信息。

【命令】

**[reset counters interface** [ **dialer** [ *interface-number*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[dialer**]：清除Dialer接口的统计信息。

*[interface-number*]：Dialer接口的编号。取值范围为已创建的Dialer接口的编号。

【使用指导】

在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。

·如果不指定**dialer**和*interface-number*，则清除所有接口的统计信息；

·如果指定**dialer**而不指定*interface-number*，则清除所有Dialer接口的统计信息；

·如果同时指定**dialer**和*interface-number*，则清除指定Dialer接口的统计信息。

【举例】

\# 清除接口Dialer1的统计信息。

\<Sysname\> reset counters interface dialer 1

【相关命令】

·**display interface dialer**

**DDR命令 \-- DDR配置命令 \-- service**

------------------------------------------------------------------------

![说明](DDR命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[service**]命令用来指定转发当前Dialer接口流量的业务处理板。

**[undo service**]命令用来恢复缺省情况。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[service slot*** slot-number*]

**[undo service slot**]

分布式设备－IRF模式：

**[service chassis ***chassis-number*** slot*** slot-number*]

**[undo service chassis**]

【缺省情况】

没有指定转发当前Dialer接口流量的业务处理板。

【视图】

Dialer接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：指定单板所在的槽位号。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：指定设备在IRF中的成员编号。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：指定设备在IRF中的成员编号或者PEX的虚拟槽位号。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：指定成员设备上的指定单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：指定单板。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

【使用指导】

没有通过**service**命令指定Dialer接口流量的业务处理板时，会自动选择主控板作为转发Dialer接口流量的业务处理板。在这种情况下，为了避免主控板处理过多的业务，建议在Dialer接口下通过**service**命令指定转发该接口流量的业务处理板。

【举例】

\# 指定在2号单板处理Dialer1接口的流量。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname interface dialer 1

Sysname-Dialer1 service slot 2

\# 指定在2号成员设备处理Dialer1接口的流量。（集中式IRF设备）

\<Sysname\> system-view

Sysname interface dialer 1

Sysname-Dialer1 service slot 2

\# 指定在2号成员设备的2号单板处理Dialer1接口的流量。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname interface dialer 1

Sysname-Dialer1service chassis2 slot 2

**DDR命令 \-- DDR配置命令 \-- shutdown**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭接口。

**[undo** **shutdown**]命令用来打开接口。

【命令】

**[shutdown**]

**[undo shutdown**]

【缺省情况】

Dialer接口处于打开状态。

【视图】

Dialer接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 关闭接口Dialer1。

\<Sysname\> system-view

Sysname interface dialer 1

Sysname-Dialer1 shutdown

**DDR命令 \-- DDR配置命令 \-- standby routing-group**

------------------------------------------------------------------------

**[standby routing-group**]命令用来在备份接口上启用动态路由备份功能，并配置引用的动态路由备份组。

**[undo standby routing-group**]命令用来在备份接口上关闭动态路由备份功能，或取消引用的动态路由备份组。

【命令】

**[standby routing-group** *group-number*]

**[undo standby routing-group** *group-number*]

【缺省情况】

动态路由备份功能处于关闭状态。

【视图】

拨号接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-number*]：动态路由备份组号，取值范围为1～255。

【使用指导】

·启用动态路由备份功能之前，必须确保备份接口上已经配置了DDR拨号功能。

·每个备份接口上可以同时引用多个动态路由备份组。

【举例】

\# 在BRI2/4/0接口上启用动态路由备份功能，并引用动态路由备份组1。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 standby routing-group 1

**DDR命令 \-- DDR配置命令 \-- standby routing-group rule**

------------------------------------------------------------------------

**[standby routing-group rule**]命令用来创建动态路由备份组，并配置需监控的网段。

**[undo standby routing-group rule**]命令用来删除动态路由备份组，或删除动态路由备份组中的需监控网段。

【命令】

**[standby routing-group ***group-number*** rule**[ **ip** *ip-address* { *mask* \| *mask-length* } [ **vpn-instance** *vpn-instance-name* ]]]

**[undo**[ **standby routing-group** *group-number* **rule** [ **ip** *ip-address* { *mask* \| *mask-length* } ]  **vpn-instance** *vpn-instance-name* ]]

【缺省情况】

没有创建动态路由备份组。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-number*]：动态路由备份组号，取值范围为1～255。

**[ip*** ip-address*]：表示需监控的网段地址。

*[mask*]：网络掩码。

*[mask-length*]：网络掩码的长度，取值范围为0～32。

**[vpn-instance** *vpn-instance-name*]：MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。

【使用指导】

一个动态路由备份组内，最多可配置255个被监控网段。只有到一个动态路由备份组内的所有被监控网段都不存在有效路由{.ItemListChar}时，才认为主链路断开。

【举例】

\# 设置动态路由备份组1，用于监控到达网段20.0.0.0/8和30.0.0.0/8的路由。

\<Sysname\> system-view

Sysname standby routing-group 1 rule ip 20.0.0.1 255.0.0.0

Sysname standby routing-group 1 rule ip 30.0.0.1 255.0.0.0

**DDR命令 \-- DDR配置命令 \-- standby timer routing-disable**

------------------------------------------------------------------------

**[standby timer routing-disable**]命令用来配置主链路接通后断开备份链路的延迟时间。

**[undo standby timer routing-disable**]命令用来恢复缺省情况。

【命令】

**[standby timer routing-disable ***delay*]

**[undo** **standby timer routing-disable**]

【缺省情况】

主链路接通后断开备份链路的延迟时间为20秒。

【视图】

拨号接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[delay*]：主链路接通后断开备份链路的延迟时间，取值范围为0～65535，单位为秒。

【举例】

\# 在接口BRI2/4/0上设置当主链路接通后断开备份链路的延迟时间为5秒。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 standby timer routing-disable 5

**DDR命令 \-- DDR配置命令 \-- timer-hold**

------------------------------------------------------------------------

**[timer-hold**]命令用来配置接口发送keepalive报文的周期。

**[undo timer-hold**]命令用来恢复缺省情况。

【命令】

**[timer-hold** *period*]

**[undo timer-hold**]

【缺省情况】

Dialer接口发送keepalive报文的周期为10秒。

【视图】

Dialer接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[period*]：接口发送keepalive报文的周期，取值范围为0～32767，单位为秒。

【使用指导】

当接口上封装的链路层协议为PPP时，链路层会定期向对端发送keepalive报文。如果在一段时间内无法收到对端发来的keepalive报文，链路层会认为对端故障，上报链路层Down。用户可以通过**timer-hold**命令修改接口发送keepalive报文的周期。

在速率非常低的链路上，参数*period*不能配置过小。因为在低速链路上，大报文可能会需要很长的时间才能传送完毕，这样就会延迟keepalive报文的发送与接收。而接口如果在多个（可以通过**timer-hold retry**命令修改该个数）keepalive周期之后仍然无法收到对端的keepalive报文，它就会认为链路发生故障。如果keepalive报文被延迟的时间超过接口的这个限制，链路就会被认为发生故障而被关闭。

【举例】

\# 配置接口Dialer1发送keepalive报文的周期为1000秒。

\<Sysname\> system-view

Sysname interface dialer 1

Sysname-Dialer1 timer-hold 1000

【相关命令】

·**timer-hold retry**

**DDR命令 \-- DDR配置命令 \-- timer-hold retry**

------------------------------------------------------------------------

**[timer-hold** **retry**]命令用来配置接口在多少个keepalive周期内没有收到keepalive报文的应答就拆除链路。

**[undo timer-hold retry**]命令用来恢复缺省情况。

【命令】

**[timer-hold** **retry** *retry*]

**[undo timer-hold retry**]

【缺省情况】

接口在5个keepalive周期内没有收到keepalive报文的应答就拆除链路。

【视图】

Dialer接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[retry*]：接口在多少个keepalive周期内没有收到keepalive报文的应答就拆除链路，取值范围为1～255。

【使用指导】

当接口上封装的链路层协议为PPP时，链路层会定期（可以通过**timer-hold**命令修改keepalive报文的发送周期）向对端发送keepalive报文。如果在一段时间内无法收到对端发来的keepalive报文，链路层会认为对端故障，上报链路层Down。

用户可以通过**timer-hold retry**命令修改接口在多少个keepalive周期内没有收到keepalive报文的应答就拆除链路。

在速率非常低的链路上，参数*retry*不能配置过小。因为在低速链路上，大报文可能会需要很长的时间才能传送完毕，这样就会延迟keepalive报文的发送与接收。而接口如果在*retry*个keepalive周期之后仍然无法收到对端的keepalive报文，它就会认为链路发生故障。如果keepalive报文被延迟的时间超过接口的这个限制，链路就会被认为发生故障而被关闭。

【举例】

\# 配置接口Dialer1在10个keepalive周期内没有收到keepalive报文的应答就拆除链路。

\<Sysname\> system-view

Sysname interface dialer 1

Sysname-Dialer1 timer-hold retry 10

【相关命令】

·**timer-hold**

