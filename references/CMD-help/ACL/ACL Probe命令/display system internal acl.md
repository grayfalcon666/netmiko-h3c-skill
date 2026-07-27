<!-- CMD-INDEX
  display system internal acl         | ]                | L5
-->

**ACL \-- ACL Probe命令 \-- display system internal acl**

------------------------------------------------------------------------

**[display** **system** **internal** **acl**]命令用来显示ACL的配置和运行情况。

【命令】

集中式设备：

**[display** **system** **internal** **acl** ]\**[ipv6**[ \| **mac \| user-defined**]  *acl-number *[\| ]**name***acl-name *}

分布式设备－独立运行模式]/集中式IRF设备：

**[display** **system** **internal** **acl** ]\**[ipv6**[ \| **mac \| user-defined** ] *acl-number *[\| ]**name***acl-name *} **[slot***slot-number* }

分布式设备－]IRF模式：

**[display** **system** **internal** **acl** ]\**[ipv6**[ \| **mac \| user-defined**]  *acl-number *[\| ]**name***acl-name *} [ **chassis** *chassis-number***slot***slot-number *}

【视图】]

Probe]视图

【缺省用户角色】]

network-admin

mdc-admin

【参数】

**[ipv6**]：指定ACL类型为IPv6 ACL。

**[mac**]：指定ACL类型为二层ACL。

**[user-defined**]：指定ACL类型为用户自定义ACL。若未指定以上三种类型，则表示IPv4 ACL。

*[acl-number*]：显示指定编号的ACL的配置和运行情况。*acl-number*表示ACL的编号，取值范围及其代表的ACL类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：

·2000～2999：表示基本ACL。

·3000～3999：表示高级ACL。

·4000～4999：表示二层ACL。

·5000～5999：表示用户自定义ACL。

**[name** *acl-name*]：显示指定名称的ACL的配置和运行情况。*acl-name*表示ACL的名称，为1～63个字符的字符串，不区分大小写，必须以英文字母a～z或A～Z开头。

**[slot** *slot-number*]：显示指定单板上ACL的配置和运行情况，*slot-number*表示单板所在的槽位号。若未指定本参数，将显示主控板上ACL的配置和运行情况。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上ACL的配置和运行情况，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上ACL的配置和运行情况，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上ACL的配置和运行情况，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上ACL的配置和运行情况，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

