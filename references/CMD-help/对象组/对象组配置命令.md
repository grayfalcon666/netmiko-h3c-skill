<!-- CMD-INDEX
  description                         | 对象组视图            | L11
  display object-group                | ]                | L57
  network (IPv4 address object group view) | IPv4地址对象组视图      | L221
  network (IPv6 address object group view) | IPv6地址对象组视图      | L337
  object-group                        | 系统视图             | L445
  port (port object group view)       | 端口对象组视图          | L521
  service(service object group view)  | 服务对象组视图          | L629
-->

**对象组 \-- 对象组配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来配置对象组的描述信息。

**[undo**] **description**命令用来删除对象组的描述信息。

【命令】

**[description**] *text*

**[undo**] **description**

【缺省情况】

对象组没有任何描述信息。

【视图】

对象组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：表示对象组的描述信息，为1～127个字符的字符串，区分大小写。

【使用指导】

无

【举例】

\# 为IP地址对象组配置描述信息。

\<Sysname\> system-view

Sysname object-group ip address ipgroup

Sysname-obj-grp-ip-ipgroup****description This is an IPv4 object-group

**对象组 \-- 对象组配置命令 \-- display object-group**

------------------------------------------------------------------------

**[display object-group**]命令用来显示对象组的内容。

【命令】

**[display object-group**[ [ [**[ip \| ipv6 ]**[} **address \| service \| port** } [ **default**]**  **name** *object-group-name *]****[\| ]**name ***object-group-name *]]

【视图】]

任意]视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[ip address**]：指定对象组类型为IPv4地址对象组。

**[ipv6** **address**]：指定对象组类型为IPv6地址对象组。

**[port**]：指定对象组类型为端口对象组。

**[service**]：指定对象组类型为服务对象组。

**[default**]：指定默认对象组。

**[name**]：指定对象组名称。

*[object-group-name*]：对象组的名称，为1～31个字符的字符串，不区分大小写。

【举例】

\# 显示所有对象组。

\<Sysname\> display object-group

IP address object group obj1: 0 object(in use)

IP address object group obj2: 5 objects(out of use)

0 network host address 1.1.1.1

10 network host name host

20 network subnet 1.1.1.1 255.255.255.0

30 network range 1.1.1.1 1.1.1.2

40 network group-object obj1

Ipv6 address object-group obj3: 0 object(in use)

Ipv6 address object-group obj4: 5 objects(out of use)

0 network host address 1::1:1

10 network host name host

20 network subnet 1::1:0 112

30 network range 1::1:1 1::1:2

40 network group-object obj3

Service object-group obj5: 0 object(in use)

Service object-group obj6: 6 objects(out of use)

0 service 200

10 service tcp source lt 50 destination range 30 40

20 service udp source range 30 40 destination gt 30

30 service icmp 20 20

40 service icmpv6 20 20

50 service group-object obj5

Port object-group obj7: 0 object(in use)

Port object-group obj8: 3 objects(out of use)

0 port lt 20

10 port range 20 30

20 port group-object obj7

\# 显示名字为obj2的对象组。

\<Sysname\> display object-group name obj2

Ip address object-group obj2: 5 objects(out of use)

0 network host address 1.1.1.1

10 network host name host

20 network subnet 1.1.1.1 255.255.255.0

30 network range 1.1.1.1 1.1.1.2

40 network group-object obj1

\# 显示所有IPv4地址对象组。

\<Sysname\> display object-group ip address

Ip address object-group obj1: 0 object(in use)

Ip address object-group obj2: 5 objects(out of use)

0 network host address 1.1.1.1

10 network host name host

20 network subnet 1.1.1.1 255.255.255.0

30 network range 1.1.1.1 1.1.1.2

40 network group-object obj1

\# 显示名字为obj4的IPv6地址对象组。

\<Sysname\> display object-group ipv6 address name obj4

Ipv6 address object-group obj4: 5 objects(out of use)

0 network host address 1::1:1

10 network host name host

20 network subnet 1::1:0 112

30 network range 1::1:1 1::1:2

40 network group-object obj3

表1-1 display object-group命令显示信息描述表

字段

描述

in use

表明此对象组被引用，包括被ACL引用或被对象组嵌套引用

out of use

表明此对象组没有被引用

**对象组 \-- 对象组配置命令 \-- network (IPv4 address object group view)**

------------------------------------------------------------------------

**[network**]命令用来创建一个IPv4地址对象。

**[undo network**]命令用来删除指定的IPv4地址对象。

【命令】

[[ *object-id*  **network** { **host** { **address** *ip-address* *\|* **name** *host-name* } \| **subnet** *ip-address* { *mask-length* \| *mask* } \| **range** *ip-address1* *ip-address2* \| **group-object** *object-group-name* }]]

**[undo network**[ { **host** { **address** *ip-address* *\|* **name** *host-name* } \| **subnet** *ip-address* { *mask-length* \| *mask* } \| **range** *ip-address1* *ip-address2* \| **group-object** *object-group-name* }]]

**[undo** *object-id*]

【缺省情况】

没有配置IPv4地址对象。

【视图】

IPv4地址对象组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[object-id*]：指定对象ID，取值范围为0～4294967294。若未指定本参数，系统将按照步长10从0开始，自动分配一个大于现有最大ID的最小ID。譬如现有对象的最大ID为22，那么自动分配的新ID将是30。

**[host**]：指定主机IPv4地址或主机名称。

**[address ***ip-address*]：指定主机IPv4地址。

**[name ***host-name*]：指定主机名称。*host-name*表示主机名称，为1～60字符，不区分大小写。

**[subnet ***ip-address*[{ *mask-length* \| *mask* }]]：指定子网IPv4地址。*mask-length*表示子网掩码长度，即掩码中连续"1"的个数，取值范围为0～32。*mask*表示接口IP地址相应的子网掩码，为点分十进制格式。

**[range ***ip-address1* *ip-address2*]：指定范围IPv4地址。*ip-address1*表示范围起始IPv4地址。*ip-address2*表示范围结束IPv4地址，仅在**range**参数时有效，和*ip-address1*没有大小限制。

**[group-object ***object-group-name*]：指定引用IPv4地址对象组。*object-group-name*表示IPv4地址对象组名称，为1～31字符，不区分大小写。

【使用指导】

·使用**subnet**关键字，如果指定*mask-length*为32或者*mask*为255.255.255.255，则该配置被视为主机地址对象配置。

·使用**range**关键字，如果指定的*ip-address1*和*ip-address2*相同，则该配置被视为主机地址对象配置。

·如果指定的*ip-address1*和*ip-address2*是一个子网的起始地址和结束地址，则该配置被视为子网地址对象配置。

·如果指定的*ip-address1*比*ip-address2*大，会自动调整范围为 *ip-address2*, *ip-address1* 。

·使用**group-object**关键字，如果指定名称的对象组不存在，则系统会创建此名称的IP地址对象组；如果指定名称的对象组存在，则对象组类型必须为IPv4地址对象组。

·引用的IPv4地址对象组不能形成循环，譬如IP地址对象组a引用IPv4地址对象组b，则IP地址对象组b不能再引用IP地址对象组a。

·引用的IPv4地址对象组最大嵌套层次为5层，譬如IP地址对象组1、2、3、4分别引用IP地址对象组2、3、4、5，则IP地址对象组5不能再引用其他IPv4地址对象组，IP地址对象组1也不能再被其他IP地址对象组引用。

·创建对象时指定ID，如果指定ID的对象不存在，则创建一条新的对象；如果指定ID的对象已存在，则对原对象进行修改。

·新创建或修改的对象不能与已有对象的内容完全相同，否则该命令执行失败，并提示出错。

【举例】

\# 配置地址为192.168.0.1的IPv4主机地址对象。

\<Sysname\> system-view

Sysname object-group ip address ipgroup

Sysname-obj-grp-ip-ipgroup****network host address 192.168.0.1

\# 配置名字为pc3的IPv4主机地址对象。

\<Sysname\> system-view

Sysname object-group ip address ipgroup

Sysname-obj-grp-ip-ipgroup network host name pc3

\# 配置地址为192.167.0.0，掩码长度为24的IPv4子网地址对象。

\<Sysname\> system-view

Sysname object-group ip address ipgroup

Sysname-obj-grp-ip-ipgroup network subnet 192.167.0.0 24

\# 配置地址为192.166.0.0，掩码为255.255.0.0的IPv4子网地址对象。

\<Sysname\> system-view

Sysname object-group ip address ipgroup

Sysname-obj-grp-ip-ipgroup network subnet 192.166.0.0 255.255.0.0

\# 配置地址范围为192.165.0.100到192.165.0.200的IPv4范围地址对象。

\<Sysname\> system-view

Sysname object-group ip address ipgroup

Sysname-obj-grp-ip-ipgroup network range 192.165.0.100 192.165.0.200

\# 配置引用ipgroup2对象组的地址对象。

\<Sysname\> system-view

Sysname object-group ip address ipgroup

Sysname-obj-grp-ip-ipgroup network group-object ipgroup2

**对象组 \-- 对象组配置命令 \-- network (IPv6 address object group view)**

------------------------------------------------------------------------

**[network**]命令用来创建一个IPv6地址对象。

**[undo network**]命令用来删除指定的IPv6地址对象。

【命令】

[[ *object-id*  **network** { **host** { **address** *ipv6-address* *\|* **name** *host-name* } \| **subnet** *ipv6-address* *prefix-length* \| **range** *ipv6-address* *ipv6-address2* \| **group-object** *object-group-name* } ]]

**[undo network**[ { **host** { **address** *ipv6-address* *\|* **name** *host-name* } \| **subnet** *ipv6-address* *prefix-length* \| **range** *ipv6-address1* *ipv6-address2* \| **group-object** *object-group-name* }]]

**[undo** *object-id* ]

【缺省情况】

没有配置IPv6地址对象。

【视图】

IPv6地址对象组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[object-id*]：指定对象ID，取值范围为0～4294967294。若未指定本参数，系统将按照步长10从0开始，自动分配一个大于现有最大ID的最小ID。譬如现有对象的最大ID为22，那么自动分配的新ID将是30。

**[host**]：指定主机IPv6地址或主机名称。

**[address ***ipv6-address*]：指定主机IPv6地址。

**[name ***host-name*]：指定主机名称。*host-name*表示主机名称，为1～60字符，不区分大小写。

**[subnet ***ipv6-address* *prefix-length*]：指定子网IPv6地址。*prefix-length*：指定IPv6地址的前缀长度，取值范围为1～128。

**[range ***ipv6-address1* *ipv6-address2*]：指定范围IPv6地址。*ipv6-address1*表示范围起始IPv6地址。*ipv6-address2*表示范围结束IPv6地址，仅在**range**参数时有效，和*ipv6-address1*没有大小限制。

**[group-object ***object-group-name*]：指定引用IPv6地址对象组。*object-group-name*表示IPv6地址对象组名称，为1～31字符，不区分大小写。

【使用指导】

·使用**subnet**命令，如果指定掩码长度为128，则该配置被视为主机地址对象配置。

·使用**range**命令，如果指定的*ipv6-address1*和*ipv6-address2*相同，则该配置被视为主机地址对象配置。

·如果指定的*ipv6-address1*和*ipv6-address2*是一个子网的起始地址和结束地址，则该配置被视为子网地址对象配置。

·如果指定的*ipv6-address1*比*ipv6-address2*大，会自动调整范围为 *ipv6-address2*,*ipv6-address1 *。

·使用**group-object**命令，如果指定名称的对象组不存在，则系统会创建此名称的IPv6地址对象组；如果指定名称的对象组存在，则对象组类型必须为IPv6地址对象组。

·引用的IPv6地址对象组不能形成循环，譬如IPv6地址对象组a引用IPv6地址对象组b，则IPv6地址对象组b不能再引用IPv6地址对象组a。

·引用的IPv6地址对象组最大嵌套层次为5层，譬如IPv6地址对象组1、2、3、4分别引用IPv6地址对象组2、3、4、5，则IPv6地址对象组5不能再引用其他IPv6地址对象组，IPv6地址对象组1也不能再被其他IPv6地址对象组引用。

·创建对象时指定ID，如果指定ID的对象不存在，则创建一条新的对象；如果指定ID的对象已存在，则对原对象进行修改。

·新创建或修改的对象不能与已有对象的内容完全相同，否则该命令执行失败，并提示出错。

【举例】

\# 配置地址为1::1的IPv6主机地址对象。

\<Sysname\> system-view

Sysname object-group ipv6 address ipv6group

Sysname-obj-grp-ipv6-ipv6group network host address 1::1

\# 配置名字为pc3的IPv6主机地址对象。

\<Sysname\> system-view

Sysname object-group ipv6 address ipv6group

Sysname-obj-grp-ipv6-ipv6group network host name pc3

\# 配置地址为1:1:1::1，前缀长度为24的IPv6子网地址对象。

\<Sysname\> system-view

Sysname object-group ipv6 address ipv6group

Sysname-obj-grp-ipv6-ip v6group network subnet 1:1:1::1 24

\# 配置地址范围为1:1:1::1到1:1:1::100 的IPv6范围地址对象。

\<Sysname\> system-view

Sysname object-group ipv6 address ipv6group

Sysname-obj-grp-ipv6-ipv6group network range 1:1:1::1 1:1:1::100

\# 配置引用ipv6group2对象组的地址对象。

\<Sysname\> system-view

Sysname object-group ipv6 address ipv6group

Sysname-obj-grp-ipv6-ipv6group network group-object ipv6group2

**对象组 \-- 对象组配置命令 \-- object-group**

------------------------------------------------------------------------

**[object-group**]命令用来创建一个对象组，并进入对象组视图。

**[undo object-group**]命令用来删除指定的对象组。

【命令】

**[object-group **[{ { **ip** \| **ipv6** } **address** \| **port** \| **service** } *object-group-name*]]

**[undo object-group **[{ { **ip** \| **ipv6** } **address** \| **port** \| **service** } *object-group-name*]]

【缺省情况】

每种对象组都有一个名称为**any**的默认对象组。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip address**]：指定对象组类型为IP地址对象组。

**[ipv6** **address**]：指定对象组类型为IPv6地址对象组。

**[port**]：指定对象组类型为端口对象组。

**[service**]：指定对象组类型为服务对象组。

*[object-group-name*]：对象组的名称，为1～31个字符的字符串，不区分大小写。

【使用指导】

·使用**object-group**命令时，如果指定名字的对象组不存在，则创建对象组并进入其视图；如果指定名字的对象组存在且类型一致，则直接进入其视图；如果指定名字的对象组存在但类型不一致，命令执行失败，并提示出错。

·使用**undo object-group**命令时，如果指定名字的对象组不存在，处理结束。如果指定名字的对象组存在但类型不一致，则命令执行失败，并提示出错。

·要删除的对象组被ACL、对象策略或者其他对象组引用，命令执行失败，并提示出错。

·系统默认对象组不能被删除。

【举例】

\# 配置名称为ipgroup的IP地址对象组。

\<Sysname\> system-view

Sysname object-group ip address ipgroup

\# 配置名称为ipv6group的IPv6地址对象组。

\<Sysname\> system-view

Sysname object-group ipv6 address ipv6group

\# 配置名称为portgroup的端口对象组。

\<Sysname\> system-view

Sysname object-group port portgroup

\# 配置名称为servicegroup的服务对象组。

\<Sysname\> system-view

Sysname object-group service servicegroup

**对象组 \-- 对象组配置命令 \-- port (port object group view)**

------------------------------------------------------------------------

**[port**]命令用来创建一个端口对象。

**[undo port**]命令用来删除指定的端口对象。

【命令】

[[ *object-id*  **port** { { **eq** \| **lt** \| **gt** } *port \|* **range** *port1 port2* \| **group-object** *object-group-name* }]]

**[undo port **[{ { **eq** \| **lt** \| **gt** } *port \|* **range** *port1 port2* \| **group-object** *object-group-name* }]]

**[undo** *object-id*]

【缺省情况】

没有配置端口对象。

【视图】

端口对象组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[object-id*]：指定对象ID，取值范围为0～4294967294。若未指定本参数，系统将按照步长10从0开始，自动分配一个大于现有最大ID的最小ID。譬如现有对象的最大ID为22，那么自动分配的新ID将是30。

**[eq**]：等于指定的端口号。

**[lt**]：小于指定的端口号。

**[gt**]：大于指定的端口号。

*[port*]：指定端口号，取值范围为0～65535。

**[range ***port1 port2*]：指定端口在两个端口号范围内。*port1*表示起始端口号，取值范围为0～65535。*port2*表示结束端口号，取值范围为0～65535，只在指定**range**参数时有效，和*port1*没有大小关系。

**[group-object**]：指定引用端口对象组。*object-group-name*表示端口对象组名称，为1～31字符，不区分大小写。

【使用指导】

·使用**lt**命令，不能指定*port1*为0；如果指定*port1*为1，则该配置被视为**eq** 0。

·使用**gt**命令，不能指定*port1*为65535；如果指定*port1*为65534，该配置被视为**eq** 65535。

·使用**range**命令，如果指定的*port1*和*port2*相同，则该配置被视为等于指定的端口号。；如果指定*port1*为0，则该配置被视为**lt**配置，譬如配置**range** 0 999，被视为**lt** 1000；如果指定*port2*为65535，则该配置被视为**gt**配置，譬如配置**range** 50001 65535，被视为**gt** 50000。

·如果指定的*port1*比*port2*大，会自动调整范围为\*[port2*, *port1 *]。

·使用**group-object**关键字，如果指定名称的对象组不存在，则系统会创建此名称的端口对象组；如果指定名称的对象组存在，则对象组类型必须为端口对象组。

·引用的端口对象组不能形成循环，譬如端口对象组a引用端口对象组b，则端口对象组b不能再引用端口对象组a；

·引用的端口对象组最大嵌套层次为5层，譬如端口对象组1、2、3、4分别引用端口对象组2、3、4、5，则端口对象组5不能再引用其他端口对象组，端口对象组1也不能再被其他端口对象组引用。

·创建对象时指定ID，如果指定ID的对象不存在，则创建一条新的对象；如果指定ID的对象已存在，则对旧对象进行修改。

·新创建或修改的对象不能与已有对象的内容完全相同，否则该命令执行失败，并提示出错。

【举例】

\# 配置端口号等于100的端口对象。

\<Sysname\> system-view

Sysname object-group port portgroup

Sysname-obj-grp-port-portgroup port eq 100

\# 配置端口号小于20的端口对象。

\<Sysname\> system-view

Sysname object-group port portgroup

Sysname-obj-grp-port-portgroup port lt 20

\# 配置端口号大于60000的端口对象。

\<Sysname\> system-view

Sysname object-group port portgroup

Sysname-obj-grp-port-portgroup port gt 60000

\# 配置端口号范围为1000到2000的端口对象。

\<Sysname\> system-view

Sysname object-group port portgroup

Sysname-obj-grp-port-portgroup port range 1000 2000

\# 配置引用portgroup2对象组的端口对象。

\<Sysname\> system-view

Sysname object-group port portgroup

Sysname-obj-grp-port-portgroup port group-object portgroup2

**对象组 \-- 对象组配置命令 \-- service(service object group view)**

------------------------------------------------------------------------

**[service**]命令用来创建一个服务对象。

**[undo service**]命令用来删除指定的服务对象。

【命令】

[[ *object-id*  **service** { *protocol* [ { **source** { { **eq** \| **lt** \| **gt** } *port \|* **range** *port1 port2* } \| **destination** { { **eq** \| **lt** \| **gt** } *port* *\|* **range** *port1 port2* } } \* \| *icmp-type icmp-code \| icmpv6-type icmpv6-code* ] *\|* **group-object** *object-group-name* }]]

**[undo service **[{ *protocol* [ { **source** { { **eq** \| **lt** \| **gt** } *port \|* **range** *port1 port2* } \| **destination** { { **eq** \| **lt** \| **gt** } *port* *\|* **range** *port1 port2* } } \* \| *icmp-type icmp-code \| icmpv6-type icmpv6-code* ] *\|* **group-object** *object-group-name* }]]

**[undo** *object-id*]

【缺省情况】

没有配置服务对象。

【视图】

服务对象组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[object-id*]：指定对象ID，取值范围为0～4294967294。若未指定本参数，系统将按照步长10从0开始，自动分配一个大于现有最大ID的最小ID。譬如现有对象的最大ID为22，那么自动分配的新ID将是30。

*[protocol*]：协议类型，可输入的形式如下：

·数字：取值范围为0～255；

·名称（括号内为对应的数字）：可选取**tcp**（6）、**udp**（17）、**icmp**（1）或**icmpv6**（58）。

**[source**]：指定源端口。只在*protocol*为**tcp**或**udp**时有效。

**[destination**]：指定目的端口。只在*protocol*为**tcp**或**udp**时有效。

**[eq**]：等于指定的端口号。

**[lt**]**：**小于指定的端口号。

**[gt**]**：**大于指定的端口号。

*[port*]：指定端口号，取值范围为0～65535。

**[range*** port1 port2*]：在指定的两个端口号范围内。*port1*表示端口号1，取值范围为0～65535。*port2*表示端口号2，取值范围为0～65535，只在指定**range**参数时有效，和*port1*没有大小关系。

*[icmp-type*]：ICMP消息类型，取值范围为0～255，只在*protocol*为**icmp**时有效。

*[icmp-code*]：ICMP消息码，取值范围为0～255。

*[icmpv6-type*]：ICMPv6消息类型，取值范围为0～255，只在*protocol*为**icmpv6**时有效。

*[icmpv6-code*]：ICMPv6消息码，取值范围为0～255。

**[group-object**]：指定引用端口对象组。*object-group-name*表示服务对象组名称，为1～31字符，不区分大小写。

【使用指导】

·使用**lt**命令，不能指定*port1*为0；如果指定*port1*为1，则该配置被视为**eq** 0。

·使用**gt**命令，不能指定*port1*为65535；如果指定*port1*为65534，该配置被视为**eq** 65535。

·使用**range**命令，如果指定的*port1*和*port2*相同，则该配置被视为等于指定的端口号；如果指定*port1*为0，则该配置被视为**lt**配置，譬如配置**range** 0 999，被视为**lt** 1000；如果指定*port2*为65535，则该配置被视为**gt**配置，譬如配置**range** 50001 65535，被视为**gt** 50000。

·如果指定的*port1*比*port2*大，会自动调整范围为\*[port2*, *port1 *]。

·使用**group-object**关键字，如果指定名称的对象组不存在，则系统会创建此名称的服务对象组；如果指定名称的对象组存在，则对象组类型必须为服务对象组。

·引用的服务对象组不能形成循环，譬如服务对象组a引用端口对象组b，则服务对象组b不能再引用服务对象组a；

·引用的服务对象组最大嵌套层次为5层，譬如服务对象组1、2、3、4分别引用服务对象组2、3、4、5，则服务对象组5不能再引用其他服务对象组，服务对象组1也不能再被其他服务对象组引用。

·创建对象时指定ID，如果指定ID的对象不存在，则创建一条新的对象；如果指定ID的对象已存在，则对旧对象进行修改。

·新创建或修改的对象不能与已有对象的内容完全相同，否则该命令执行失败，并提示出错。

【举例】

\# 配置协议号等于100的服务对象。

\<Sysname\> system-view

Sysname object-group service servicegroup

Sysname-obj-grp-service-servicegroup service 100

\# 配置指定源端口和目的端口的tcp协议报文的服务对象。

\<Sysname\> system-view

Sysname object-group service servicegroup

Sysname-obj-grp-service-servicegroup****service tcp source eq 100 destination range 10 100

\# 配置icmp协议的服务对象。

\<Sysname\> system-view

Sysname object-group service servicegroup

Sysname-obj-grp-service-servicegroup service icmp 100 150

\# 配置引用servicegroup2对象组的端口对象。

\<Sysname\> system-view

Sysname object-group service servicegroup

Sysname-obj-grp-port-portgroup service group-object servicegroup2
