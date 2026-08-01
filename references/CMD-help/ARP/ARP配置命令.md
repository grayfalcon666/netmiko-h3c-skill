<!-- CMD-INDEX
  arp check enable                    | 系统视图             | L36
  arp check log enable                | 系统视图             | L84
  arp max-learning-num                | 二层以太网接口视图/三层以太网接口视图/三层以太网子接口视图/VLAN接口视图/二层聚合接口视图/三层聚合接口视图/三层聚合子接口视图/S通道接口视图/S通道聚合接口视图/三层RPR逻辑接口视图 | L128
  arp max-learning-number             |                  | L204
  arp mode uni                        | VLAN接口视图         | L276
  arp multiport                       | 系统视图             | L322
  arp static                          | 系统视图             | L384
  arp timer aging                     | 系统视图             | L466
  display arp                         | 任意视图             | L516
  display arp ip-address              | 任意视图             | L688
  display arp timer aging             | 任意视图             | L762
  display arp vpn-instance            | 任意视图             | L804
  reset arp                           | 用户视图             | L856
  arp ip-conflict log prompt          | 系统视图             | L928
  arp send-gratuitous-arp             | 三层以太网接口视图/三层以太网子接口视图/三层聚合接口视图/三层聚合子接口视图/三层RPR逻辑接口视图/VLAN接口视图 | L964
  gratuitous-arp-learning enable      | 系统视图             | L1028
  gratuitous-arp-sending enable       | 系统视图             | L1074
  display local-proxy-arp             | 任意视图             | L1116
  display proxy-arp                   | 任意视图             | L1168
  local-proxy-arp enable              | VLAN接口视图/三层以太网接口视图/三层以太网子接口视图/三层聚合接口视图/三层聚合子接口视图/三层RPR逻辑接口视图 | L1220
  proxy-arp enable                    | VLAN接口视图/三层以太网接口视图/三层以太网子接口视图/三层聚合接口视图/三层聚合子接口视图/三层RPR逻辑接口视图 | L1312
  arp snooping enable                 | VLAN视图           | L1384
  display arp snooping                | 任意视图             | L1422
  reset arp snooping                  | 用户视图             | L1544
  arp fast-reply enable               | VLAN视图           | L1586
  arp pnp                             | 三层以太网接口视图/三层以太网子接口视图 | L1626
  display arp pnp                     | 任意视图             | L1674
  arp suppression enable              | 交叉连接视图           | L1762
  arp suppression push interval       | 系统视图             | L1810
  display arp suppression xconnect-group | 任意视图             | L1858
  reset arp suppression xconnect-group | 用户视图             | L1958
  arp route-direct advertise          | L3VE接口视图         | L1994
-->

**ARP \-- ARP配置命令 \-- arp check enable**

------------------------------------------------------------------------

![说明](ARP命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[arp** **check** **enable**]命令用来开启动态ARP表项的检查功能。

**[undo** **arp** **check** **enable**]命令用来关闭动态ARP表项的检查功能。

【命令】

**[arp** **check** **enable**]

**[undo** **arp** **check** **enable**]

【缺省情况】

动态ARP表项的检查功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

动态ARP表项检查功能可以控制设备上是否可以学习ARP报文中的发送端MAC地址为组播MAC的动态ARP表项。

·开启ARP表项的检查功能后，设备上不能学习ARP报文中发送端MAC地址为组播MAC的动态ARP表项，也不能手工添加MAC地址为组播MAC的静态ARP表项。

·关闭ARP表项的检查功能后，设备可以学习以太网源MAC地址为单播MAC且ARP报文中发送端MAC地址为组播MAC的动态ARP表项，也可以手工添加MAC地址为组播MAC的静态ARP表项。

【举例】

\# 开启动态ARP表项的检查功能。

\<Sysname\> system-view

Sysname arp check enable

**ARP \-- ARP配置命令 \-- arp check log enable**

------------------------------------------------------------------------

**[arp check log enable**]命令开启ARP日志信息功能。

**[undo arp check log enable**]命令关闭ARP日志信息功能。

【命令】

**[arp check log enable**]

**[undo arp check log enable**]

【缺省情况】

设备ARP日志信息功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

ARP日志是为了满足网络管理员审计的需要，对处理ARP报文的信息进行的记录，包括设备未使能ARP代理功能时收到目的IP不是设备接口IP地址、VRRP备份组的虚拟IP地址或NAT转化的外部网络地址；收到的ARP报文中源地址和接收接口地址、VRRP备份组中的虚拟IP地址或NAT转换的外部网络地址冲突，且此报文不是ARP请求报文等。

设备生成的ARP日志信息会交给信息中心模块处理，信息中心模块的配置将决定日志信息的发送规则和发送方向。关于信息中心的详细描述请参见"网络管理和监控配置指导"中的"信息中心"。

为了防止设备输出过多的ARP日志信息，一般情况下建议不要打开此功能。

【举例】

\# 开启ARP日志信息功能。

\<Sysname\> system-view

Sysname arp check log enable

**ARP \-- ARP配置命令 \-- arp max-learning-num**

------------------------------------------------------------------------

![说明](ARP命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[arp** **max-learning-num**]命令用来配置接口允许学习动态ARP表项的最大个数。

**[undo** **arp** **max-learning-num**]命令用来恢复缺省情况。

【命令】

**[arp** **max-learning-num** *number*]

**[undo** **arp** **max-learning-num**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

二层以太网接口视图/三层以太网接口视图/三层以太网子接口视图/VLAN接口视图/二层聚合接口视图/三层聚合接口视图/三层聚合子接口视图/S通道接口视图/S通道聚合接口视图/三层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：接口允许学习动态ARP表项的最大个数。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

设备可以通过ARP协议自动生成动态ARP表项。为了防止部分接口下的用户占用过多的ARP资源，可以通过设置接口学习动态ARP表项的最大个数来进行限制。当接口学习动态ARP表项的个数达到所设置的值时，该接口将不再学习动态ARP表项。

当配置接口允许学习动态ARP表项的最大个数为0时，表示禁止接口学习动态ARP表项。

【举例】

\# 配置VLAN接口40上可以学习动态ARP表项的最大个数为500。

\<Sysname\> system-view

Sysname interface vlan-interface 40

Sysname-Vlan-interface40 arp max-learning-num 500

\# 配置接口GigabitEthernet1/0/1上可以学习动态ARP表项的最大个数为1000。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 arp max-learning-num 1000

\# 配置二层聚合接口1上可以学习动态ARP表项的最大个数为1000。

\<Sysname\> system-view

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1 arp max-learning-num 1000

\# 配置三层聚合接口1上可以学习动态ARP表项的最大个数为1000。

\<Sysname\> system-view

Sysname interface route-aggregation 1

Sysname-Route-Aggregation1 arp max-learning-num 1000

**ARP \-- ARP配置命令 \-- arp max-learning-number**

------------------------------------------------------------------------

**[arp max-learning-number**]命令用来配置设备允许学习动态ARP表项的最大个数。

**[undo arp max-learning-number**]命令用来恢复缺省情况。

【命令】

集中式设备:

**[arp max-learning-number ***number*]

**[undo arp max-learning-number**]

分布式设备－独立运行模式/集中式IRF设备:

**[arp max-learning-number ***number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

**[undo arp max-learning-number slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式:

**[arp max-learning-number ***number* **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

**[undo arp max-learning-number chassis ***chassis-number*** slot** *slot-number* [ **cpu** *cpu-number* ]]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：设备允许学习动态ARP表项的最大个数。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[slot*** slot-number*]：设置指定单板学习动态ARP表项的最大个数。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：设置指定成员设备上学习动态ARP表项的最大个数，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：设置指定成员设备/PEX上学习动态ARP表项的最大个数，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：设置指定成员设备上指定单板学习动态ARP表项的最大个数。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：设置指定单板学习动态ARP表项的最大个数。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：设置指定CPU学习动态ARP表项的最大个数。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

设备可以通过ARP协议自动生成动态ARP表项。为了防止用户占用过多的ARP资源，可以通过设置设备学习动态ARP表项的最大个数来进行限制。当设备学习动态ARP表项的个数达到所设置的值时，该设备将不再学习动态ARP表项。

当配置设备允许学习动态ARP表项的最大个数为0时，表示禁止该设备学习动态ARP表项。

【举例】

\# 限制单板1上学习的ARP表项的最大个数为64。

\<Sysname\> system-view

Sysname arp max-learning-number 64 slot 1

**ARP \-- ARP配置命令 \-- arp mode uni**

------------------------------------------------------------------------

**[arp mode uni**]命令用来配置接口为用户侧接口。

**[undo arp mode**]命令用来配置接口为网络侧接口。

【命令】

**[arp mode uni**]

**[undo arp mode**]

【缺省情况】

接口为网络侧接口。

【视图】

VLAN接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当接口连接终端主机时，可以配置接口为用户侧接口。对于这种接口上学到的ARP表项，不再和设备上的路由信息相关联。

当接口连接网络设备时，需要配置接口为网络侧接口。对于这种接口上学到的ARP表项，可以与设备上的路由信息关联，可作为路由信息的下一跳。

通过实际使用情况，正确配置接口的工作模式，可以适当的节省硬件资源。

【举例】

\# 配置VLAN接口2角色为用户侧接口。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 arp mode uni

**ARP \-- ARP配置命令 \-- arp multiport**

------------------------------------------------------------------------

**[arp multiport**]命令用来配置多端口ARP表项。

**[undo** **arp**]命令用来删除ARP表项。

【命令】

**[arp** **multiport** *ip-address mac-address vlan-id* [ **vpn-instance** *vpn-instance-name* ]]

**[undo** **arp** *ip-address* [ *vpn-instance-name* ]]

【缺省情况】

没有配置多端口ARP表项。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：ARP表项的IP地址部分。

*[mac-address*]：ARP表项的MAC地址部分，格式为H-H-H。

*[vlan-id*]：多端口ARP表项所属的VLAN，取值范围为1～4094。

**[vpn-instance*** vpn-instance-name*]：指定多端口ARP表项所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。该VPN实例必须已经存在。如果未指定本参数，则表示多端口ARP表项位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·参数*vlan-id*用于指定多端口ARP表项所对应的VLAN，*vlan-id*必须是用户已经创建好的VLAN的ID。

·当设备多端口ARP表项所对应的VLAN或VLAN接口被删除时，该表项需删除。

·参数*vlan-id*对应的接口IP地址与参数ip-address对应的地址属于同一网段时，多端口ARP配置才能生效。

·必须配置对应的多端口单播/组播MAC地址，多端口ARP表项才能指导转发。

【举例】

\# 配置一条多端口ARP表项，IP地址为202.38.10.2，对应的MAC地址为00e0-fc01-0000，此条ARP表项属于VLAN 10。

\<Sysname\> system-view

Sysname arp multiport 202.38.10.2 00e0-fc01-0000 10

【相关命令】

·**display** **arp** **multiport**

·**reset** **arp**** multiport**

**ARP \-- ARP配置命令 \-- arp static**

------------------------------------------------------------------------

**[arp** **static**]命令用来配置静态ARP表项。

**[undo** **arp**]命令用来删除ARP表项。

【命令】

**[arp**[ **static** *ip-address mac-address* [ *vlan-id* *interface-type interface-number \| interface-type interface-number* *interface-type interface-number* ]  **vpn-instance** *vpn-instance-name* ]]

**[undo** **arp** *ip-address* [ *vpn-instance-name* ]]

【缺省情况】

没有配置静态ARP表项。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：ARP表项的IP地址部分。

*[mac-address*]：ARP表项的MAC地址部分，格式为H-H-H。

*[vlan-id*]：静态ARP表项所属的VLAN，取值范围为1～4094。

*[interface-type interface-number*]：指定接口类型和接口编号。

**[vpn-instance*** vpn-instance-name*]：指定静态ARP表项所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。该VPN实例必须已经存在。如果未指定本参数，则表示静态ARP表项位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

静态ARP表项通过手工配置和维护，不会被老化，不会被动态ARP表项覆盖，可以增加通信的安全性。

静态ARP表项分为短静态ARP表项和长静态ARP表项。一般情况下，ARP动态执行并自动寻求IP地址到以太网MAC地址的解析，无需管理员的介入。当希望设备和指定用户只能使用某个固定的IP地址和MAC地址通信时，可以配置短静态ARP表项，当进一步希望限定这个用户只在某VLAN内的某个特定接口上连接时就可以配置长静态ARP表项。

需要注意的是：

·静态ARP表项在设备正常工作时间一直有效，当某设备ARP表项所对应的VLAN或VLAN接口被删除时，如果是长静态ARP表项则被删除，如果是已经解析的短静态ARP表项则重新变为未解析状态。

·对于已经解析的短静态ARP表项，也会由于外部事件，比如解析到的出接口状态down等原因，恢复到未解析状态。

·对于长静态ARP表项，根据设备的当前状态可能处于有效或无效两种状态。处于无效状态的原因可能是该ARP表项对应的VLAN接口状态down或出接口状态down等原因。处于无效状态的长静态ARP表项不能指导报文转发。、

·如果指定了*vlan-id* *interface-type interface-number*，*vlan-id*用于指定ARP表项所对应的VLAN，*interface-type interface-number*为以太网接口。*vlan-id*所对应的VLAN和VLAN接口必须存在，接口*interface-type interface-number*必须属于此VLAN*，*否则系统均将提示出错。

·当指定了参数*vlan-id*时，*vlan-id*对应的VLAN接口的IP地址必须和*ip-address*属于同一网段。

·如果**undo**命令中没有指定VPN实例，则只删除公网中的ARP表项。

·某些组网环境需要使用参数*interface-type interface-number interface-type interface-number*，比如L2VPN接入L3VPN组网，一个L3VE接口会对应多个L2VE子接口。那么配置长静态ARP表项时，需要通过该参数指定L3VE口和L2VE子接口之间的对应关系。L3VE接口和L2VE子接口的描述和配置请参见"MPLS使用指导"中的"L2VPN接入L3VPN或IP骨干网"。

【举例】

\# 配置一条静态ARP表项，IP地址为202.38.10.2，对应的MAC地址为00e0-fc01-0000，此条ARP表项对应的出接口为属于VLAN 10的接口GigabitEthernet1/0/1。

\<Sysname\> system-view

Sysname arp static 202.38.10.2 00e0-fc01-0000 10 gigabitethernet 1/0/1

\# 配置一条长静态ARP表项，IP地址为1.1.1.1，对应的MAC地址为00e0-fc01-0000，此条ARP表项对应的出接口为VE-L3VPN1下的VE-L2VPN1.1。

\<Sysname\> system-view

Sysname arp static 1.1.1.1 00e0-fc01-0000 ve-l3vpn 1 ve-l2vpn 1.1

【相关命令】

·**display** **arp**

·**reset** **arp**

**ARP \-- ARP配置命令 \-- arp timer aging**

------------------------------------------------------------------------

**[arp** **timer** **aging**]命令用来配置动态ARP表项的老化时间。

**[undo** **arp** **timer** **aging**]命令用来恢复缺省情况。

【命令】

**[arp** **timer** **aging** *aging-time*]

**[undo** **arp** **timer** **aging**]

【缺省情况】

动态ARP表项的老化时间为20分钟。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[aging-time*]：动态ARP表项的老化时间，取值范围为1～1440，单位为分钟。

【使用指导】

为适应网络的变化，ARP表需要不断更新。ARP表中的动态ARP表项并非永远有效，每一条记录都有一个生存周期，到达生存周期仍得不到刷新的记录将被从ARP表中删除，这个生存周期被称作老化时间。如果在到达老化时间前纪录被刷新，则重新计算老化时间。

配置代理ARP功能后，应该减小动态ARP表项的老化时间，以尽快使无效动态ARP表项失效，减少发给设备而设备却不能转发的报文，以尽快删除无效的动态ARP表项。

【举例】

\# 配置动态ARP表项的老化时间为10分钟。

\<Sysname\> system-view

Sysname arp timer aging 10

【相关命令】

·**display** **arp** **timer** **aging**

**ARP \-- ARP配置命令 \-- display arp**

------------------------------------------------------------------------

**[display** **arp**]命令用来显示ARP表项。

【命令】

集中式设备：

**[display**[ **arp** [ [ **all** \| **dynamic** \| **multiport** \| **static** ] \| **vlan** *vlan-id* \| **interface** *interface-type interface-number*   **count** \| **verbose** ]]]

分布式设备－独立运行模式/集中式IRF设备：

**[display**[ **arp** [ [ **all** \| **dynamic** \| **multiport** \| **static** ]  **slot** *slot-number* [ **cpu** *cpu-number*  ] \| **vlan** *vlan-id* \| **interface** *interface-type interface-number*   **count** \| **verbose** ]]]

分布式设备－IRF模式：

**[display**[ **arp** [ [ **all** \| **dynamic** \| **multiport** \| **static** ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ] \| **vlan** *vlan-id* \| **interface** *interface-type interface-number*   **count** \| **verbose** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[all**]：显示所有的ARP表项。

**[dynamic**]：显示动态ARP表项。

**[multiport**]：显示多端口ARP表项。

**[static**]：显示静态ARP表项。

**[slot*** slot-number*]：显示指定单板的ARP表项。*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示主用主控板上的ARP表项。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的ARP表项。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示Master设备上的ARP表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX的ARP表项。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示Master设备上的ARP表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的ARP表项。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示全局主用主控板上的ARP表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的ARP表项。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示全局主用主控板上的ARP表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的ARP表项。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**[vlan*** vlan-id*]：显示指定VLAN的ARP表项，*vlan-id*的取值范围为1～4094。

**[interface*** interface-type interface-number*]：显示指定接口的ARP表项。*interface-type interface-number*用来指定接口类型和接口编号。

**[count**]：显示ARP表项的数目。

**[verbose**]：显示ARP表项的详细信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

使用本命令可以查看静态、动态和多端口ARP表项的具体内容，包括IP地址、MAC地址、VLAN ID、出接口、表项类型以及老化时间等信息。

【举例】

\# 显示所有ARP表项的信息。

\<Sysname\> display arp all

  Type: S-Static   D-Dynamic   O-Openflow   R-Rule   M-Multiport  I-Invalid

IP Address       MAC Address     VLAN     Interface              Aging Type

20.1.1.1         00e0-fc00-0001  N/A      N/A                    N/A   S

193.1.1.70       00e0-fe50-6503  100      GE1/0/1                N/A   IS

192.168.0.115    000d-88f7-9f7d  1        GE1/0/2                18    D

192.168.0.39     0012-a990-2241  1        GE1/0/3                20    D

22.1.1.1         000c-299d-c041  10       N/A                    N/A   M

\# 显示所有ARP表项的详细信息。

\<Sysname\> display arp all verbose

Type: S-Static   D-Dynamic   O-Openflow   R-Rule   M-Multiport  I-Invalid

IP Address       MAC Address     VLAN     Interface              Aging Type

Vpn Instance                   NickNameRb

20.1.1.1         00e0-fc00-0001  N/A      N/A                    N/A   S

test                           0x0001

193.1.1.70       00e0-fe50-6503  100      GE1/0/1                N/A   IS

No Vrf                       0x0000

192.168.0.115    000d-88f7-9f7d  1        GE1/0/2                18    D

No Vrf                       0x0000

192.168.0.39     0012-a990-2241  1        GE1/0/3                20    D

No Vrf                       0x0000

22.1.1.1         000c-299d-c041  10       N/A                    N/A   M

No Vrf                       0x0000

\# 显示所有ARP表项的数目。

\<Sysname\> display arp all count

 Total number of entries : 5

表1-1 display arp命令显示信息描述表

字段

描述

IP Address

ARP表项的IP地址

MAC Address

ARP表项的MAC地址

VLAN

ARP表项所属的VLAN ID（当表项类型为静态表项时，"N/A"表示未解析的短静态ARP表项；如果ARP表项中的接口不属于某个VLAN，也显示"N/A"）

Interface

ARP表项所对应的出接口（当表项类型为静态表项时，"N/A"表示未解析的短静态ARP表项；当表项类型为多端口表项时，"N/A"表示ARP表项不持有端口信息，需要参考对应的多端口MAC地址）

Aging

动态ARP表项的老化时间，单位为分钟（"N/A"表示老化时间不可知或者没有老化时间）

Type

ARP表项类型：动态，用D表示；静态，用S表示；OpenFlow，用O表示；Rule，用R表示；多端口，用M表示；无效，用I表示

Vpn Instance

VPN实例名称，No Vrf表示没有配置相应ARP的VPN实例

NickNameRb

ARP表项的NickName（长度为4的十六进制数字，例如0x012a），关于NickName的详细介绍，请参见"TRILL配置指导"中的"TRILL"

Total number of entries

ARP表项数目

【相关命令】

·**arp** **static**

·**reset** **arp**

**ARP \-- ARP配置命令 \-- display arp ip-address**

------------------------------------------------------------------------

**[display** **arp** *ip-address*]命令用来显示指定IP地址的ARP表项。

【命令】

集中式设备：

**[display** **arp** *ip-address* [ **verbose** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display** **arp** *ip-address* [ **slot** *slot-number* [ **cpu** *cpu-number*  ]  **verbose** ]]

分布式设备－IRF模式：

**[display** **arp** *ip-address* [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]  **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[ip-address*]：显示指定IP地址的ARP表项。

**[slot*** slot-number*]：显示指定单板的ARP表项。*slot-number*表示单板的槽位号。如果未指定本参数，则显示主用主控板上的ARP表项。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的ARP表项。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示Master设备上的ARP表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX的ARP表项。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示Master设备上的ARP表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的ARP表项。*chassis-number*表示设备在IRF中的成员编号。*slot-number*表示单板的槽位号。如果未指定本参数，则显示全局主用主控板上的ARP表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的ARP表项。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号。*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示全局主用主控板上的ARP表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的ARP表项。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**[verbose**]：显示ARP表项的详细信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

用户可以通过本命令查看指定IP地址的ARP表项的具体内容，包括IP地址、MAC地址、VLAN ID、出接口、表项类型以及老化时间等信息。

【举例】

\# 显示IP地址为20.1.1.1的ARP表项的信息。

\<Sysname\> display arp 20.1.1.1

  Type: S-Static   D-Dynamic   O-Openflow   R-Rule   M-Multiport  I-Invalid

IP address       MAC address     VLAN     Interface              Aging Type

20.1.1.1         00e0-fc00-0001  N/A      N/A                    N/A   S

【相关命令】

·**arp** **static**

·**reset** **arp**

**ARP \-- ARP配置命令 \-- display arp timer aging**

------------------------------------------------------------------------

**[display** **arp** **timer** **aging**]命令用来显示动态ARP表项的老化时间。

【命令】

**[display** **arp** **timer** **aging**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

使用本命令可以查看用户配置的动态ARP表项的老化时间。

【举例】

\# 显示动态ARP表项的老化时间。

\<Sysname\> display arp timer aging

Current ARP aging time is 10 minute(s)

以上显示信息表示动态ARP表项的老化时间为10分钟。

【相关命令】

·**arp** **timer** **aging**

**ARP \-- ARP配置命令 \-- display arp vpn-instance**

------------------------------------------------------------------------

**[display** **arp** **vpn-instance**]命令用来显示指定VPN实例的ARP表项。

【命令】

**[display** **arp** **vpn-instance** *vpn-instance-name* [ **count** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[vpn-instance-name*]：表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，不可以包含空格，区分大小写。显示指定VPN实例的ARP表项。

**[count**]：显示ARP表项的数目。

【使用指导】

用户可以通过本命令查看指定VPN实例的ARP表项的具体内容，包括IP地址、MAC地址、VLAN ID、出接口、表项类型以及老化时间等信息。

【举例】

\# 显示VPN实例名为test的ARP表项。

\<Sysname\> display arp vpn-instance test

  Type: S-Static   D-Dynamic   O-Openflow   R-Rule   M-Multiport  I-Invalid

IP address       MAC address     VLAN     Interface              Aging Type

20.1.1.1         00e0-fc00-0001  N/A      N/A                    N/A   S

【相关命令】

·**arp** **static**

·**reset** **arp**

**ARP \-- ARP配置命令 \-- reset arp**

------------------------------------------------------------------------

**[reset** **arp**]命令用来清除ARP表项。

【命令】

集中式设备：

**[reset**[ **arp** { **all** \| **dynamic** \| **interface** *interface-type interface-number* \| **multiport** \| **static** }]]

分布式设备－独立运行模式/集中式IRF设备：

**[reset**[ **arp** { **all** \| **dynamic** \| **interface** *interface-type interface-number* \| **multiport** \| **slot** *slot-number* [ **cpu** *cpu-number* ] \| **static** }]]

分布式设备－IRF模式：

**[reset**[ **arp** { **all** \| **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ] \| **dynamic** \| **interface** *interface-type interface-number* \| **multiport** \| **static** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示清除所有的ARP表项。

**[dynamic**]：表示清除动态ARP表项。

**[multiport**]：表示清除多端口ARP表项。

**[static**]：表示清除静态ARP表项。

**[slot*** slot-number*]：表示清除指定单板的ARP表项。*slot-number*表示单板的槽位号。如果未指定本参数，则清除主用主控板上的ARP表项。（分布式设备－独立运行模式）

**[slot*** slot-number*]：表示清除指定成员设备的ARP表项。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则清除Master设备上的ARP表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：表示清除指定成员设备/PEX的ARP表项。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则清除Master设备上的ARP表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：表示清除指定成员设备上指定单板的ARP表项。*chassis-number*表示设备在IRF中的成员编号。*slot-number*表示单板的槽位号。如果未指定本参数，则清除全局主用主控板上的ARP表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：表示清除指定单板的ARP表项。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号。*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则清除全局主用主控板上的ARP表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示清除指定CPU上的ARP表项。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**[interface** *interface-type interface-number*]：表示清除指定接口的ARP表项。*interface-type interface-number*用来指定接口的类型和编号。

【使用指导】

本命令可以单独清除静态、动态ARP表项和多端口ARP表项，也可以单独清除指定单板、指定接口的ARP表项。

【举例】

\# 清除静态ARP表项。

\<Sysname\> reset arp static

【相关命令】

·**arp** **static**

·**display** **arp**

\

**免费ARP \-- 免费ARP配置命令 \-- arp ip-conflict log prompt**

------------------------------------------------------------------------

**[arp ip-conflict log prompt**]命令用来开启源IP地址冲突提示功能。

**[undo arp ip-conflict log prompt**]命令用来关闭源IP地址冲突提示功能。

【命令】

**[arp ip-conflict log prompt**]

**[undo arp ip-conflict log prompt**]

【缺省情况】

源IP地址冲突提示功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 在设备上开启源IP地址冲突提示功能。

\<Sysname\> system-view

Sysname arp ip-conflict log prompt

**免费ARP \-- 免费ARP配置命令 \-- arp send-gratuitous-arp**

------------------------------------------------------------------------

**[arp** **send-gratuitous-arp**]命令用来在接口上开启定时发送免费ARP功能，并设置发送免费ARP报文的周期。

**[undo** **arp** **send-gratuitous-arp**]命令用来关闭定时发送免费ARP功能。

【命令】

**[arp** **send-gratuitous-arp** [ **interval** *milliseconds* ]]

**[undo** **arp** **send-gratuitous-arp**]

【缺省情况】

定时发送免费ARP功能处于关闭状态。

【视图】

三层以太网接口视图/三层以太网子接口视图/三层聚合接口视图/三层聚合子接口视图/三层RPR逻辑接口视图/VLAN接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interval*** milliseconds*]：发送免费ARP报文的周期，取值范围为200～200000，单位为毫秒，缺省值为2000毫秒。

【使用指导】

配置本命令后，只有当接口链路状态up并且配置IP地址后，此功能才真正生效。

只能为VRRP虚拟IP地址、接口主IP地址和手工配置的从IP地址发送免费ARP。主IP地址可以是手工配置或者通过其他方式获取的，但是从IP地址必须是手工配置的。

如果修改了免费ARP报文的发送周期，则在下一个发送周期才能生效。

如果同时在很多接口下开启本功能，或者每个接口有大量的从IP地址，或者两种情况共存的同时又配置很小的发送时间间隔，那么免费ARP报文的发送频率可能会远远低于用户的预期。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上开启定时发送免费ARP功能，发送免费ARP报文的周期为300毫秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 arp send-gratuitous-arp interval 300

·交换应用

\# 在VLAN接口2上开启定时发送免费ARP功能，发送免费ARP报文的周期为300毫秒。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 arp send-gratuitous-arp interval 300

**免费ARP \-- 免费ARP配置命令 \-- gratuitous-arp-learning enable**

------------------------------------------------------------------------

![说明](ARP命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[gratuitous-arp-learning** **enable**]命令用来开启免费ARP报文的学习功能。

**[undo** **gratuitous-arp-learning** **enable**]命令用来关闭免费ARP报文学习功能。

【命令】

**[gratuitous-arp-learning** **enable**]

**[undo** **gratuitous-arp-learning** **enable**]

【缺省情况】

免费ARP报文的学习功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启免费ARP报文学习功能后，设备会根据收到的免费ARP报文中携带的信息对自身维护的ARP表进行修改（新建或者更新ARP表项）。

关闭免费ARP报文学习功能后，设备不会根据收到的免费ARP报文来新建ARP表项，但是会更新已存在的对应ARP表项。如果用户不希望通过免费ARP报文来新建ARP表项，可以关闭免费ARP报文学习功能，以节省ARP表项资源。

【举例】

\# 开启免费ARP报文的学习功能。

\<Sysname\> system-view

Sysname gratuitous-arp-learning enable

**免费ARP \-- 免费ARP配置命令 \-- gratuitous-arp-sending enable**

------------------------------------------------------------------------

![说明](ARP命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[gratuitous-arp-sending** **enable**]命令用来开启设备收到非同一网段的ARP请求时发送免费ARP报文功能。

**[undo** **gratuitous-arp-sending** **enable**]命令用来恢复缺省情况。

【命令】

**[gratuitous-arp-sending** **enable**]

**[undo** **gratuitous-arp-sending** **enable**]

【缺省情况】

设备收到非同一网段的ARP请求时不发送免费ARP报文。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 关闭设备收到非同一网段的ARP请求时发送免费ARP报文功能。

\<Sysname\> system-view

Sysname undo gratuitous-arp-sending enable

\

**代理ARP \-- 代理ARP配置命令 \-- display local-proxy-arp**

------------------------------------------------------------------------

![说明](ARP命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display** **local-proxy-arp**]命令用来显示本地代理ARP的状态。

【命令】

**[display** **local-proxy-arp** [ **interface** *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface*** interface-type interface-number*]：显示指定接口的本地代理ARP的状态。*interface-type interface-number*指定接口类型和接口编号。

【使用指导】

使用本命令可以查看本地代理ARP是处于开启（enabled）状态还是关闭（disabled）状态。

如果指定接口，则显示指定接口的本地代理ARP的状态；如果不指定接口，则显示所有接口的本地代理ARP的状态。

【举例】

\# 显示VLAN接口2的本地代理ARP状态。

\<Sysname\> display local-proxy-arp interface vlan-interface 2

Interface Vlan-interface2

 Local Proxy ARP status: enabled

【相关命令】

·**local-proxy-arp** **enable**

**代理ARP \-- 代理ARP配置命令 \-- display proxy-arp**

------------------------------------------------------------------------

![说明](ARP命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display** **proxy-arp**]命令用来显示代理ARP的状态。

【命令】

**[display** **proxy-arp** [ **interface** *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface*** interface-type Interface-number*]：显示指定接口的代理ARP的状态。*interface-type interface-number*用来指定接口类型和接口编号。

【使用指导】

使用本命令可以查看代理ARP是处于开启（enabled）状态还是关闭（disabled）状态。

如果指定接口，则显示指定接口的代理ARP的状态；如果不指定接口，则显示所有接口的代理ARP的状态。

【举例】

\# 显示接口GigabitEthernet1/0/1的代理ARP状态。

\<Sysname\> display proxy-arp interface gigabitethernet 1/0/1

Interface GigabitEthernet1/0/1

 Proxy ARP status: disabled

【相关命令】

·**proxy-arp** **enable**

**代理ARP \-- 代理ARP配置命令 \-- local-proxy-arp enable**

------------------------------------------------------------------------

![说明](ARP命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[local-proxy-arp** **enable**]命令用来开启本地代理ARP功能。

**[undo** **local-proxy-arp** **enable**]命令用来关闭本地代理ARP功能。

【命令】

**[local-proxy-arp** **enable** [ **ip-range** *startIP* **to** *endIP* ]]

**[undo** **local-proxy-arp** **enable**]

【缺省情况】

本地代理ARP功能处于关闭状态。

【视图】

VLAN接口视图/三层以太网接口视图/三层以太网子接口视图/三层聚合接口视图/三层聚合子接口视图/三层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip-range** *startIP* **to** *endIP*]：配置对指定IP地址范围进行本地代理ARP。*startIP*表示起始IP地址。*endIP*表示结束IP地址。*startIP*必须小于等于*endIP*。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

如果ARP请求是从一个网络的主机发往同一网段却不在同一物理网络上的另一台主机，那么连接它们的具有代理ARP功能的设备就可以回答该请求，这个过程称作代理ARP（Proxy ARP）。

代理ARP功能屏蔽了分离的物理网络这一事实，使用户使用起来，好像在同一个物理网络上。

代理ARP分为普通代理ARP和本地代理ARP，二者的应用场景有所区别：

·普通代理ARP的应用场景为：想要互通的主机分别连接到设备的不同三层接口上，且这些主机不在同一个广播域中。

·本地代理ARP的应用场景为：想要互通的主机连接到设备的同一个三层接口上，且这些主机不在同一个广播域中。

需要注意的是，配置本地代理ARP功能时，如果配置**ip-range**，则一个接口下只能配置一个IP地址范围。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上开启本地代理ARP功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 local-proxy-arp enable

\# 在接口GigabitEthernet1/0/1上开启本地代理ARP功能，并指定进行ARP代理的IP地址范围。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 local-proxy-arp enable ip-range 1.1.1.1 to 1.1.1.20

·交换应用

\# 在VLAN接口2上开启本地代理ARP功能。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 local-proxy-arp enable

\# 在VLAN接口2上开启本地代理ARP功能，并指定进行ARP代理的IP地址范围。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 local-proxy-arp enable ip-range 1.1.1.1 to 1.1.1.20

【相关命令】

·**display** **local-proxy-arp**

**代理ARP \-- 代理ARP配置命令 \-- proxy-arp enable**

------------------------------------------------------------------------

![说明](ARP命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[proxy-arp** **enable**]命令用来开启代理ARP功能。

**[undo** **proxy-arp** **enable**]命令用来关闭代理ARP功能。

【命令】

**[proxy-arp** **enable**]

**[undo** **proxy-arp** **enable**]

【缺省情况】

代理ARP功能处于关闭状态。

【视图】

VLAN接口视图/三层以太网接口视图/三层以太网子接口视图/三层聚合接口视图/三层聚合子接口视图/三层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

如果ARP请求是从一个网络的主机发往同一网段却不在同一物理网络上的另一台主机，那么连接它们的具有代理ARP功能的设备就可以回答该请求，这个过程称作代理ARP（Proxy ARP）。

代理ARP功能屏蔽了分离的物理网络这一事实，使用户使用起来，好像在同一个物理网络上。

代理ARP分为普通代理ARP和本地代理ARP，二者的应用场景有所区别：

·普通代理ARP的应用场景为：想要互通的主机分别连接到设备的不同三层接口上，且这些主机不在同一个广播域中。

·本地代理ARP的应用场景为：想要互通的主机连接到设备的同一个三层接口上，且这些主机不在同一个广播域中。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上开启代理ARP。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 proxy-arp enable

·交换应用

\# 在接口Vlan-interface2上开启代理ARP。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 proxy-arp enable

【相关命令】

·**display** **proxy-arp**

\

**ARP Snooping \-- ARP Snooping配置命令 \-- arp snooping enable**

------------------------------------------------------------------------

**[arp** **snooping** **enable**]命令用来开启ARP Snooping功能。

**[undo** **arp** **snooping** **enable**]命令用来关闭ARP Snooping功能。

【命令】

**[arp** **snooping** **enable**]

**[undo** **arp** **snooping** **enable**]

【缺省情况】

ARP Snooping功能处于关闭状态。

【视图】

VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 开启VLAN 2下的ARP Snooping功能。

\<Sysname\> system-view

Sysname vlan 2

Sysname-vlan2 arp snooping enable

**ARP Snooping \-- ARP Snooping配置命令 \-- display arp snooping**

------------------------------------------------------------------------

**[display** **arp** **snooping**]命令用来显示ARP Snooping表项。

【命令】

集中式设备：

**[display** **arp** **snooping** [ **vlan** *vlan-id*   **count** ]]

**[display** **arp** **snooping** **ip** *ip-address*]

分布式设备－独立运行模式/集中式IRF设备：

**[display** **arp** **snooping** [ **vlan** *vlan-id*   **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

**[display** **arp** **snooping** **ip** *ip-address* [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display** **arp** **snooping** [ **vlan** *vlan-id*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

**[display** **arp** **snooping** **ip** *ip-address* [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vlan*** vlan-id*]：显示指定VLAN的ARP Snooping表项。*vlan-id*的取值范围为1～4094。

**[count**]：显示当前ARP Snooping表项的计数。

**[ip** *ip-address*]：显示指定IP地址的ARP Snooping表项。

**[slot*** slot-number*]：显示指定单板上的所有ARP Snooping表项。*slot-number*表示单板的槽位号。如果未指定本参数，则显示主用主控板上的ARP Snooping表项。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上的所有ARP Snooping表项。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示Master设备上的ARP Snooping表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的所有ARP Snooping表项。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示Master设备上的ARP Snooping表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板上的所有ARP Snooping表项。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板的槽位号。如果未指定本参数，则显示全局主用主控板上的ARP Snooping表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的所有ARP Snooping表项。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示全局主用主控板上的ARP Snooping表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的所有ARP Snooping表项。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示VLAN 2下的ARP Snooping表项。

\<Sysname\> display arp snooping vlan 2

IP Address   MAC Address    VLAN ID Interface  Aging       Status

3.3.3.3      0003-0003-0003 2       GE1/0/1    20          Valid

3.3.3.4      0004-0004-0004 2       GE1/0/2    5           Invalid

\# 显示当前ARP Snooping表项的计数。

\<Sysname\> display arp snooping count

Total entries: 2

表4-1 display arp snooping命令显示信息描述表

字段

描述

IP Address

ARP Snooping表项的IP地址

MAC Address

ARP Snooping表项的MAC地址

VLAN ID

ARP Snooping表项所属的VLAN ID

Interface

ARP Snooping表项所对应的入接口

Aging

ARP Snooping表项的老化时间，单位为分钟。当显示N/A时，表示当前槽位不是创建ARP Snooping表项的端口所在的槽位

Status

ARP Snooping表项的状态，分为以下三种：

·Valid：有效

·Invalid：无效

·Collision：冲突

Total entries

ARP Snooping表项数目

【相关命令】

·**reset arp snooping**

**ARP Snooping \-- ARP Snooping配置命令 \-- reset arp snooping**

------------------------------------------------------------------------

**[reset** **arp** **snooping**]命令用来清除ARP Snooping表项。

【命令】

**[reset**[ **arp** **snooping** [ **ip** *ip-address* \| **vlan** *vlan-id* ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip*** ip-address*]：清除指定IP地址的ARP Snooping表项。

**[vlan*** vlan-id*]：清除指定VLAN的ARP Snooping表项。*vlan-id*的取值范围为1～4094。

【使用指导】

如果没有指定参数，则清除所有的ARP Snooping表项。

【举例】

\# 清除VLAN 2下的ARP Snooping表项。

\<Sysname\> reset arp snooping vlan 2

【相关命令】

·**display arp snooping**

\

**ARP快速应答 \-- ARP快速应答配置命令 \-- arp fast-reply enable**

------------------------------------------------------------------------

**[arp** **fast-reply** **enable**]命令用来开启ARP快速应答功能。

**[undo** **arp** **fast-reply** **enable**]命令用来关闭ARP快速应答功能。

【命令】

**[arp** **fast-reply** **enable**]

**[undo** **arp** **fast-reply** **enable**]

【缺省情况】

ARP快速应答功能处于关闭状态。

【视图】

VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 开启VLAN 2下的ARP快速应答功能。

\<Sysname\> system-view

Sysname vlan 2

Sysname-vlan2 arp fast-reply enable

\

**即插即用网关 \-- 即插即用网关配置命令 \-- arp pnp**

------------------------------------------------------------------------

**[arp pnp**]命令用来开启即插即用网关功能。

**[undo arp pnp**]命令用来关闭即插即用网关功能。

【命令】

**[arp pnp**]

**[undo arp pnp**]

【缺省情况】

即插即用网关功能处于关闭状态。

【视图】

三层以太网接口视图/三层以太网子接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·目前该功能需要NAT功能一起配合使用。

·开启该功能前，需要在设备上使用**reset arp**命令删除接口下的ARP表项，以防止功能冲突。

·开启该功能后，还需要依赖接口主IP地址及对应掩码生成代理地址池。即如果配置了24位掩码的IP地址则可以生成253个代理地址，且排除接口主IP地址。目前接口下支持代理地址个数最大值与设备型号有关，请以设备实际情况为准。只有接口下存在主IP地址，即插即用功能才能完全生效。

·开启该功能后会导致该接口路由及ARP部分特性（如ARP代理功能）不可使用。

【举例】

\# 开启即插即用网关功能。

\<Sysname\> system-view

sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 arp pnp

**即插即用网关 \-- 即插即用网关配置命令 \-- display arp pnp**

------------------------------------------------------------------------

**[display arp pnp**]命令用来显示接入点在即插即用网关上的信息。

【命令】

**[display arp pnp** [ **interface** *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface** *interface-type interface-number*]：显示指定接口上的接入点在即插即用网关上的信息。*interface-type interface-number*用来指定接口类型和接口编号。如果不指定接口，则显示所有的接入点在即插即用网关上的信息。

【举例】

\# 显示设备上所有的接入点在即插即用网关上的信息。

\<Sysname\> display arp pnp

Total number of entries : 5

Agent IP address   User IP address   MAC address      Interface   Aging

1.1.1.2            20.1.1.1          00e0-fc00-0001   GE1/0/1     10

1.1.1.3            193.1.1.70        00e0-fe50-6503   GE1/0/1     5

2.2.2.2            192.168.0.115     000d-88f7-9f7d   GE1/0/2     11

3.3.3.3            192.168.0.39      0012-a990-2241   GE1/0/3     5

3.3.3.4            22.1.1.1          000c-299d-c041   GE1/0/3     14

\# 显示接口GigabitEthernet1/0/1上的接入点在即插即用网关上的信息。

\<Sysname\> display arp pnp interface gigabitethernet 1/0/1

Total number of entries : 2

Agent IP address   User IP address   MAC address      Interface   Aging

1.1.1.2            20.1.1.1          00e0-fc00-0001   GE1/0/1     10

1.1.1.3            193.1.1.70        00e0-fe50-6503   GE1/0/1     5

表6-1 display arp pnp命令显示信息描述表

字段

描述

Agent IP address

设备分配的代理IP地址

User IP address

用户的IP地址

MAC address

用户的MAC地址

Interface

接入点在即插即用网关上的表项所对应的接口

Aging

表项的老化时间，单位为分钟

\

**ARP泛洪抑制 \-- ARP泛洪抑制配置命令 \-- arp suppression enable**

------------------------------------------------------------------------

**[arp suppression enable**]命令用来开启ARP泛洪抑制功能。

**[undo arp suppression enable**]命令用来关闭ARP泛洪抑制功能。

【命令】

**[arp suppression enable**]

**[undo arp suppression enable**]

【缺省情况】

ARP泛洪抑制功能处于关闭状态。

【视图】

交叉连接视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

配置交叉连接视图时，需要先配置L2VPN功能。

【举例】

\# 开启交叉连接组1，交叉连接2下的ARP泛洪抑制功能。

\<Sysname\> system-view

Sysname xconnect-group 1

Sysname-xcg-1 connection 2

Sysname-xcg-1-2 arp suppression enable

【相关命令】

·**arp suppression push interval**

**ARP泛洪抑制 \-- ARP泛洪抑制配置命令 \-- arp suppression push interval**

------------------------------------------------------------------------

**[arp suppression push interval**]命令配置开启推送ARP泛洪抑制表项功能，并配置推送时间间隔。

**[undo arp suppression push interval**]命令用来关闭设备主动推送ARP泛洪抑制表项的功能。

【命令】

**[arp suppression push interval ***interval*]

**[undo arp suppression push interval**]

【缺省情况】

设备不会主动推送ARP泛洪抑制表项。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：主动推送ARP泛洪抑制表项信息的时间间隔，取值范围为1～1440，单位为分钟**。**

【使用指导】

使用**arp suppression push interval**命令用来设置主动推送ARP泛洪抑制表项信息的时间间隔，如果当前主动推送ARP泛洪抑制表项信息的功能未开启，将会同时开启主动推送功能。

【举例】

\# 开启主动推送ARP泛洪抑制表项功能，将主动推送ARP泛洪抑制表项信息的时间设为2分钟。

\<Sysname\> system-view

Sysname arp suppression push interval 2

【相关命令】

·**arp suppression enable**

**ARP泛洪抑制 \-- ARP泛洪抑制配置命令 \-- display arp suppression xconnect-group**

------------------------------------------------------------------------

**[display arp suppression xconnect-group**]命令用来显示ARP泛洪抑制表项。

【命令】

集中式设备：

**[display** **arp** **suppression xconnect-group** [ **name** *group-name*   **count** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display** **arp** **suppression xconnect-group** [ **name** *group-name*   **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

分布式设备－IRF模式：

**[display** **arp** **suppression xconnect-group** [ **name** *group-name*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name*** group-name*]：交叉连接组的名称，取值为1～31个字符的字符串，不能包含字符"-"，区分大小写。

**[count**]：当前ARP泛洪抑制表项的数目。

**[slot*** slot-number*]：显示指定单板的ARP泛洪抑制表项。*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示主用主控板上的ARP泛洪抑制表项。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的ARP泛洪抑制表项。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示Master设备上的ARP泛洪抑制表项。（集中式IRF设备）（不支持IRF3设备）

**[slot*** slot-number*]：显示指定成员设备/PEX的ARP泛洪抑制表项。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示Master设备上的ARP泛洪抑制表项。（集中式IRF设备）（支持IRF3设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的ARP泛洪抑制表项。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示全局主用主控板上的ARP泛洪抑制表项。（分布式设备－IRF模式）（不支持IRF3设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的ARP泛洪抑制表项。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示全局主用主控板上的ARP泛洪抑制表项。（分布式设备－IRF模式）（支持IRF3设备）

**[cpu** *cpu-number*]：显示指定CPU上的ARP泛洪抑制表项。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示所有交叉连接组下的ARP泛洪抑制表项。

\<Sysname\> display arp suppression xconnect-group

IP address      MAC address     Xconnect-group       Connection           Aging

100.1.1.1       000c-29fe-5a8f  vpna                 svc                  12

100.1.1.2       000c-29fe-5aa3  vpna                 svc                  25

\# 显示当前ARP泛洪抑制表项的计数。

\<Sysname\> display arp suppression xconnect-group count

Total entries: 2

表7-1 display arp suppression xconnect-group命令显示信息描述表

字段

描述

IP address

ARP泛洪抑制表项的IP地址

MAC address

ARP泛洪抑制表项的MAC地址

Xconnect-group

ARP泛洪抑制表项的Xconnect-group名称

Connection

ARP泛洪抑制表项的Connection名称

Aging

ARP泛洪抑制表项的老化时间，单位为分钟

【相关命令】

·**reset arp suppression xconnect-group**

**ARP泛洪抑制 \-- ARP泛洪抑制配置命令 \-- reset arp suppression xconnect-group**

------------------------------------------------------------------------

**[reset arp suppression xconnect-group**]命令用来清除ARP泛洪抑制表项。

【命令】

**[reset arp** **suppression xconnect-group** [ **name** *group-name* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[name*** group-name*]：交叉连接组的名称，取值为1～31个字符的字符串，不能包含字符"-"，区分大小写。

【举例】

\# 清除所有交叉连接组下的ARP泛洪抑制表项。

\<Sysname\> reset arp suppression xconnect-group

【相关命令】

·**display arp suppression xconnect-group**

\

**ARP直连路由通告 \-- ARP直连路由通告配置命令 \-- arp route-direct advertise**

------------------------------------------------------------------------

**[arp route-direct advertise**]命令用来开启ARP直连路由通告功能。

**[undo arp route-direct advertise**]命令用来关闭ARP直连路由通告功能。

【命令】

**[arp route-direct advertise**]

**[undo arp route-direct advertise**]

【缺省情况】

ARP直连路由通告功能处于关闭状态。

【视图】

L3VE接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 在L3VE接口1下开启ARP直连路由通告功能。

\<Sysname\> system-view

Sysname interface ve-l3vpn 1

Sysname-VE-L3VPN1 arp route-direct advertise

