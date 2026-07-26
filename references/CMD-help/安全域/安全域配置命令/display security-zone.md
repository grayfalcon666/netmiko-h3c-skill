
**安全域 \-- 安全域配置命令 \-- display security-zone**

------------------------------------------------------------------------

**[display security-zone**]命令用来显示安全域信息，包括缺省安全域和自定义的安全域信息。

【命令】

**[display security-zone**  **name*******zone-name *]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name **]*zone-name*：安全域的名称，为1～31个字符的字符串，不区分大小写。若不指定本参数，则显示所有安全域的信息。

【使用指导】

安全域的显示顺序是先显示缺省安全域信息，再按照安全域名称的字母排序显示自定义的安全域信息。

【举例】

\# 显示安全域myZone的信息。（本举例的支持情况与设备的型号有关，请以设备的实际情况为准）

\<Sysname\> display security-zone name myZone

Name: myZone

Members:

  GigabitEthernet1/0/3

  GigabitEthernet1/0/4

  GigabitEthernet1/1/1 in VLAN 3

  GigabitEthernet1/1/5 in VLAN 7

\# 显示安全区域myZone信息。（本举例的支持情况与设备的型号有关，请以设备的实际情况为准）

\<Sysname\> display security-zone name myZone

Name: myZone

Members:

  GigabitEthernet1/1/1

  GigabitEthernet1/1/2

  VLAN 150-200

\# 显示安全域IPZone的信息。（本举例的支持情况与设备的型号有关，请以设备的实际情况为准）

\<Sysname\> display security-zone name IPZone

Name: IPZone

Members:

  192.168.1.0 255.255.255.0

  192.168.0.0 255.255.0.0 vpn-instance abc

  1001:1002::0 32

表1-1 **display****security-zone**命令输出信息描述

字段

描述

Name

安全域名称

Members

安全域成员，包括以下几种取值：

·三层接口名称

·二层以太网接口名称和所属的VLAN编号

·VLAN编号

·公网中的IP子网

·公网中的IPv6子网

·VPN中的IP子网

·VPN中的IPv6子网

·None，该安全域中没有任何成员

**安全域 \-- 安全域配置命令 \-- display zone-pair security**

------------------------------------------------------------------------

**[display zone-pair security**]命令用来显示已创建的所有域间实例的信息。

【命令】

**[display zone-pair security**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示所有安全域间实例的信息。

\<Sysname\> display **zone-pair security**

 Source zone   Destination zone

 DMZ           Local

 Trust         Local

表1-2 **display****zone-pair security**命令输出信息描述

字段

描述

Source zone

源安全域名称

Destination zone

目的安全域名称

**安全域 \-- 安全域配置命令 \-- import interface**

------------------------------------------------------------------------

**[import **]**interface**命令用来向安全域中添加三层接口成员，包括三层以太网接口、三层以太网子接口和其它三层逻辑接口。

**[undo **]**import interface**命令用来从安全域中移除三层接口成员。

【命令】

**[import**] **interface ** *lay3-interface-type lay3-interface-number*

**[undo import**] **interface ** *lay3-interface-type lay3-interface-number*

【缺省情况】

安全域中不存在任何成员。

【视图】

安全域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[lay3-*]*interface-type lay3-interface-number*：指定添加到安全域的三层接口的接口类型和接口编号。

【使用指导】

可以通过多次执行本命令向同一个安全域添加多个三层接口成员。

需要注意的是：

·一个三层接口只允许加入一个安全域。

·若要修改接口所属安全域，需要首先在相应安全域中使用**undo import**命令将相应接口从原安全域中删除，再使用**import**命令将其加入其它安全域。其中，缺省的安全域Local中不允许添加任何接口，其它缺省的安全域中允许添加接口。

【举例】

\# 向安全域Trust中添加三层以太网接口Ethernet1/1。

\<Sysname\> system-view

Sysname security-zone name trust

Sysname-security-zone-trust import interface ethernet 1/1

**安全域 \-- 安全域配置命令 \-- import interface vlan**

------------------------------------------------------------------------

![说明](安全域命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[import interface vlan**]命令用来向安全域中添加二层接口和VLAN成员。

**[undo **]**import interface vlan**命令用来从安全域中移除二层接口和VLAN成员。

【命令】

**[import interface ***lay2-*]*interface-type lay2-interface-number*** vlan ***vlan-list*

**[undo import interface ***lay2-*]*interface-type lay2-interface-number*** vlan ***vlan-list*

【缺省情况】

安全域中不存在任何成员。

【视图】

安全域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[lay2-*]*interface-type lay2-interface-number*：指定添加到安全域的二层接口的接口类型和接口编号。

**[vlan**]*****vlan-list*：指定接口所属的VLAN列表。VLAN列表表示多个VLAN，表示方式为vlan-list ＝ { *vlan-id1* [ **to** *vlan-id2*  }&\<1-10\>]。其中，*vlan-id1*、*vlan-id2*为已创建的VLAN编号。&\<1-10\>表示前面的参数最多可以输入10次。*vlan-id2*必须大于*vlan-id1*。VLAN ID的取值范围为1～4094。

【使用指导】

可以通过多次执行本命令，向安全域中添加多个二层接口和VLAN成员。

需要注意的是：

·一个二层接口和所属的VLAN只允许加入一个安全域。

·若要修改接口或者VLAN所属安全域，需要首先在相应安全域中使用**undo import**命令将相应接口或者VLAN从原安全域中删除，再使用**import**命令将其加入其它安全域。其中，缺省的安全域Local中不允许添加任何接口或者VLAN，其它缺省的安全域中允许添加接口和VLAN。

【举例】

\# 向安全域Untrust中添加二层以太网接口Ethernet1/1和对应的VLAN 10。

\<Sysname\> system-view

Sysname security-zone name untrust

Sysname-security-zone-untrust import interface ethernet1/1 vlan 10

**安全域 \-- 安全域配置命令 \-- import ip**

------------------------------------------------------------------------

![说明](安全域命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[import ip**]命令用来向安全域中添加IPv4子网成员。

**[undo import ip**]命令用来从安全域中删除IPv4子网成员。

【命令】

**[import ip**[ *ip-address* { *mask-length* \| *mask* } [ **vpn-instance** *vpn-instance-name* ]]]

**[undo import ip**[ *ip-address* { *mask-length* \| *mask* } [ **vpn-instance** *vpn-instance-name* ]]]

【缺省情况】

安全域中不存在任何IPv4子网成员。

【视图】

安全域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：指定子网IPv4地址。

*[mask-length*]：表示子网的掩码长度，即掩码中连续"1"的个数，取值范围为0～32。

*[mask*]：表示IPv4子网相应的子网掩码，为点分十进制格式。

**[vpn-instance** *vpn-instance-name*]：指定子网所属的VPN。*vpn-instance-name*表示设备中存在的MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。不指定该参数时，表示子网位于公网中。

【使用指导】

可以通过多次执行本命令，向安全域中添加多个IPv4子网成员。

需要注意的是：

·完全相同的子网不能添加到不同的安全域中，例如1.1.1.1/24与1.1.1.2/24相同，均对应IPv4子网1.1.1.0/24，不能分别添加到不同安全域。

·如果两个子网的网段有包含关系，例如1.1.1.1/24与1.1.2.2/16，后者包含前者，但系统认为是两个不同子网，可以分别配置到同一安全域或者不同安全域。当配置到不同安全域时，报文最终将匹配掩码最长的子网所在的安全域。如IP地址为1.1.1.3的报文会匹配到1.1.1.1/24所在的安全域。

【举例】

\# 添加地址为192.168.1.0、掩码长度为24的IPv4子网到安全域a。

\<Sysname\> system-view

Sysname security-zone name a

Sysname-security-zone-a import ip 192.168.1.0 24

\# 添加地址为192.168.2.1、掩码为255.255.255.0的IPv4子网到安全域a。

\<Sysname\> system-view

Sysname security-zone name a

Sysname-security-zone-a import ip 192.168.2.1 255.255.255.0

\# 添加地址为192.168.2.1、掩码为255.255.255.0、VPN实例名为abc的IPv4子网到安全域a。

\<Sysname\> system-view

Sysname security-zone name a

Sysname-security-zone-a import ip 192.168.2.1 255.255.255.0 vpn-instance abc

**安全域 \-- 安全域配置命令 \-- import ipv6**

------------------------------------------------------------------------

![说明](安全域命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[import ipv6**]命令用来向安全域中添加IPv6子网成员。

**[undo import ipv6**]命令用来从安全域中删除IPv6子网成员。

【命令】

**[import ipv6** *ipv6-address prefix-length* [ **vpn-instance** *vpn-instance-name* ]]

**[undo import ipv6** *ipv6-address prefix-length* [ **vpn-instance** *vpn-instance-name* ]]

【缺省情况】

安全域中不存在任何IPv6子网成员。

【视图】

安全域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：指定子网IPv6地址。

*[prefix-length*]：指定IPv6地址的前缀长度，取值范围为1～128。

**[vpn-instance** *vpn-instance-name*]：指定子网所属的VPN。*vpn-instance-name*表示设备中存在的MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。不指定该参数时，表示子网位于公网中。

【使用指导】

可以通过多次执行本命令，向安全域中添加多个IPv6子网成员。

需要注意的是：

·完全相同的IPv6子网不能添加到不同的安全域中，例如1:1:1::1/32与1:1:1::2/32相同，均对应IPv6子网1:1::0/32，不能分别添加到不同安全域。

·如果两个子网的网段有包含关系，例如1:1:1::0/48与1:1:1::0/32，后者包含前者，但系统会认为是两个不同子网，可以分别配置到同一安全域或者不同安全域。当配置到不同安全域时，报文最终将匹配前缀最长的子网所在的安全域。如IP地址为1:1:1::2的报文会匹配到1:1:1::0/48所在的安全域。

【举例】

\# 将IPv6子网1001:1002::0/32添加到安全域a。

\<Sysname\> system-view

Sysname security-zone name a

Sysname-security-zone-a import ipv6 1001:1002::1 32

\# 将VPN abc中的IPv6子网1001:1002::0/32添加到安全域a。

\<Sysname\> system-view

Sysname security-zone name a

Sysname-security-zone-a import ipv6 1001:1002::1 32 vpn-instance abc

**安全域 \-- 安全域配置命令 \-- import vlan**

------------------------------------------------------------------------

![说明](安全域命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[import vlan**]命令用来向安全域中添加VLAN成员。

**[undo **]**import vlan**命令用来从安全域中移除VLAN成员。

【命令】

**[import **]**vlan** *vlan-list*

**[undo import **]**vlan** *vlan-list*

【缺省情况】

安全域中不存在任何成员。

【视图】

安全域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan**]*****vlan-list*：指定要加入安全区域的VLAN列表。VLAN列表表示多个VLAN，表示方式为vlan-list ＝ { *vlan-id1* [ **to** *vlan-id2*  }&\<1-10\>]。其中，*vlan-id1*、*vlan-id2*为已创建的VLAN编号。&\<1-10\>表示前面的参数最多可以输入10次。*vlan-id2*必须大于*vlan-id1*。VLAN ID的取值范围为1～4094。属于这些VLAN的所有二层以太网接口均属于该安全域。

【使用指导】

可以通过多次执行本命令，向安全域中添加多个VLAN成员。

需要注意的是：

·一个VLAN只允许加入一个安全域。

·若要修改VLAN所属安全域，需要首先在相应安全域中使用**undo import**命令将相应VLAN从原安全域中删除，再使用**import**命令将其加入其它安全域。其中，缺省的安全域Local中不允许添加任何VLAN，其它缺省的安全域中允许添加VLAN。

【举例】

\# 向安全域Trust中添加VLAN 3、VLAN 5～VLAN 7。

\<Sysname\> system-view

Sysname security-zone name trust

Sysname-security-zone-trust import vlan 3 5 to 7

**安全域 \-- 安全域配置命令 \-- security-zone**

------------------------------------------------------------------------

**[security-zone**]命令用来创建并且进入安全域视图。

**[undo security-zone**]命令用来删除安全域。

【命令】

**[security-zone name**]*****zone-name*

**[undo security-zone**]**name***zone-name*

【缺省情况】

缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[name**]*zone-name*：安全域的名称，为1～31个字符的字符串，不区分大小写，不能包含字符["-"。]

【使用指导】

当首次执行创建安全域或者创建域间策略的命令时，系统会自动创建4个缺省安全域：Local、Trust、DMZ和Untrust。该描述的适用情况与设备的型号有关，请以设备的实际情况为准。

同一个MDC内不同安全域的名称不允许相同，属于不同MDC的安全域的名称可以相同。（支持MDC的设备）

可通过多次执行本命令，创建多个安全域。

删除一个安全域时，以此安全域为源域或目的域的域间实例也会被删除，而且在该域间实例上已经应用的安全策略会被自动解除应用。缺省安全域不能被删除。

【举例】

\# 创建安全域zonetest，并进入该安全域视图。

\<Sysname\> system-view

Sysname security-zone name zonetest

Sysname-security-zone-zonetest

【相关配置】

·**display security-zone**

·**import**

**安全域 \-- 安全域配置命令 \-- zone-pair security**

------------------------------------------------------------------------

**[zone-pair security**]命令用来创建安全域间实例并进入安全域间实例视图。

**[undo **]**zone-pair security**命令用来删除指定的域间实例。

【命令】

**[zone-pair security source**]*****[source-zone-name*****[\| **any** } ]**destination***[destination-zone-name *[\| **any** }]

**[undo zone-pair security source**]*****[source-zone-name*****[\| **any** } ]**destination***[destination-zone-name*****[\| **any** }]

【缺省情况】]

无任何安全域间实例存在]。

【视图】]

系统]视图

【缺省用户角色】

network-admin

【参数】

**[source**]*****source-zone-name*：源安全域的名称，为1～31个字符的字符串，不区分大小写。

**[destination**]*****destination-zone-name*：目的安全域的名称，为1～31个字符的字符串，不区分大小写。

**[any**]：表示任意安全域。

【使用指导】

安全域间实例用于指定安全策略（如ASPF策略、对象策略等）需要检测的业务流的源安全域和目的安全域，它们分别描述了经过网络设备的业务流的首包要进入的安全域和要离开的安全域。在安全域间实例上应用安全策略可实现对指定业务流进行安全策略检查。

需要注意的是：

·创建安全域间实例时指定的源安全域和目的安全域必须是已存在的安全域。

·删除安全域间实例后，在域间实例上已经应用的安全策略将不生效，对应的引用关系同时被取消。

【举例】

\# 创建源安全域Trust到目的安全域Untrust的安全域间实例。

\<Sysname\> system-view

Sysname zone-pair security source trust destination untrust

Sysname-zone-pair-security-Trust-Untrust

【相关命令】

·**display zone-pair security**

**安全域 \-- 安全域配置命令 \-- security-zone intra-zone default permit**

------------------------------------------------------------------------

!(安全域命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[security-zone intra-zone default permit**]命令用来配置同一安全域内接口间报文处理的缺省动作为permit。

**[undo** **security-zone intra-zone default permit**]命令用来恢复缺省情况。

【命令】

**[security-zone intra-zone default permit**]

**[undo** **security-zone intra-zone default permit**]

【缺省情况】

同一安全域内报文过滤的缺省动作为deny。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

对于同一安全域内接口间的报文，若设备上不存在当前域到当前域的域间实例，设备缺省会将其丢弃，可以通过配置安全域内接口间报文处理的缺省动作为permit来允许其通过。

【举例】

\# 配置同一安全域内接口间报文处理的缺省动作为pemit。

\<Sysname\> system-view

Sysname security-zone intra-zone default permit

