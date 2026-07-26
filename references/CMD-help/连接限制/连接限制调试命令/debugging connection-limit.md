::: {#1617546209 .myid}
[]{#_Toc404793530}[]{#struct_0_18971_61630_x1320374186}

**连接限制 \-- 连接限制调试命令 \-- debugging connection-limit**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_18971_61630_1863637656}

[**[debugging connection-limit]{lang="EN-US"}**]{#struct_0_18971_61630_x841757168}[ { **all** \| **event** \| **error** } \[ **acl** \[ **ipv6** \] *acl-number* \]]{lang="EN-US"}

[**[undo debugging connection-limit ]{lang="EN-US"}**]{#struct_0_18971_61630_1364380264}[{ **all** \| **event** \| **error** }]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18971_61630_x1608756243}

[[用户视图]{style="font-family:宋体"}]{#struct_0_18971_61630_x1453136813}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18971_61630_2105525153}

[[network-admin]{lang="EN-US"}]{#struct_0_18971_61630_x1010278762}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18971_61630_90949011}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18971_61630_x1239362234}

[**[all]{lang="EN-US"}**]{#struct_0_18971_61630_1758710602}[：表示连接数限制的所有调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_18971_61630_x196205393}[：表示连接数限制的事件调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_18971_61630_x841691632}[：表示连接数限制的错误调试信息开关。]{style="font-family:宋体"}

[**[acl]{lang="EN-US"}**]{#struct_0_18971_61630_x1755281880}[：指定仅输出匹配]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则的连接数限制相关的调试信息。若不指定该参数，则表示输出对所有连接数限制的相关调试信息。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_18971_61630_2111637500}[：表示使用]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[进行匹配。若不指定该参数，则表示使用]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}[进行匹配。]{style="font-family:宋体"}

[*[acl-number]{lang="EN-US"}*]{#struct_0_18971_61630_956263809}[：]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。该参数可多次设置，但仅最后一次合法的配置生效。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_18971_61630_x1977103278}

[**[debugging connection-limit]{lang="EN-US"}**]{#struct_0_18971_61630_1680995774}[命令用来打开连接数限制调试信息开关。]{style="font-family:
宋体"}**[undo debugging connection-limit]{lang="EN-US"}**[命令用来关闭连接数限制调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，连接数限制调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_18971_61630_x780747434}

[[表1-1 ]{lang="EN-US"}[debugging connection-limit]{lang="EN-US"}]{#struct_0_18971_61630_194421466}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_610122552}[[字段]{style="font-family:黑体"}]{#struct_0_18971_61630_2063823278}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_18971_61630_x841363952}

[[Connection(*src-ip*/*src-vpn*/*tunnel-id*:*src-port*\--\>*dst-ip*:*dst-port*(*protocol*)) matched limit *limit-id* of policy *policy-number* (*node*).]{lang="FR"}]{#struct_0_18971_61630_x2143314857}

[[连接匹配到连接数限制规则，其中：]{style="font-family:宋体"}]{#struct_0_18971_61630_x1173395511}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[src-ip]{lang="FR"}*]{#struct_0_18971_61630_x60166491}[/*src-vpn*/*tunnel-id*]{lang="FR"}[：源]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[源]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[实例的名称]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[ DS Lite Tunnel ID]{lang="EN-US"}[。若不支持或未配置]{style="font-family:宋体"}*[src-vpn]{lang="FR"}*[、]{style="font-family:宋体"}*[tunnel-id]{lang="FR"}*[参数，则仅显示]{style="font-family:宋体"}*[src-ip]{lang="FR"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[src-port]{lang="EN-US"}*]{#struct_0_18971_61630_x1722235888}[：源端口]{lang="EN-US" style="font-family:宋体"}[号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dst-ip]{lang="EN-US"}*]{#struct_0_18971_61630_524442761}[：目的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dst-port]{lang="EN-US"}*]{#struct_0_18971_61630_x1093276594}[：目的端口]{lang="EN-US" style="font-family:宋体"}[号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[protocol]{lang="EN-US"}*]{#struct_0_18971_61630_x841298416}[：协议名称]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[limit-id]{lang="EN-US"}*]{#struct_0_18971_61630_x215566973}[：连接数限制规则编号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[policy-number]{lang="EN-US"}*]{#struct_0_18971_61630_x774390857}[：连接数限制策略编号]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node]{lang="EN-US"}*]{#struct_0_18971_61630_x1709243848}[：匹配]{lang="EN-US" style="font-family:宋体"}[标识（]{style="font-family:宋体"}[Global]{lang="EN-US"}[表示全局，]{lang="EN-US" style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示具体接口]{lang="EN-US" style="font-family:宋体"}[）]{style="font-family:宋体"}

[[Connection(*src-ip*/*src-vpn*/*tunnel-id*:*src-port*\--\>*dst-ip:dst-port*(*protocol*)) doesn't match policy (*node*).]{lang="FR"}]{#struct_0_18971_61630_1724011169}

[[连接不能匹配连接数限制规则，其中：]{style="font-family:宋体"}]{#struct_0_18971_61630_x163534720}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[src-ip]{lang="FR"}*]{#struct_0_18971_61630_x841495024}[/*src-vpn*/*tunnel-id*]{lang="FR"}[：源]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[源]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[实例的名称]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[ DS Lite Tunnel ID]{lang="EN-US"}[。若不支持或未配置]{style="font-family:宋体"}*[src-vpn]{lang="FR"}*[、]{style="font-family:宋体"}*[tunnel-id]{lang="FR"}*[参数，则仅显示]{style="font-family:宋体"}*[src-ip]{lang="FR"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[src-port]{lang="EN-US"}*]{#struct_0_18971_61630_596030335}[：源端口]{lang="EN-US" style="font-family:宋体"}[号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dst-ip]{lang="EN-US"}*]{#struct_0_18971_61630_449421505}[：目的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dst-port]{lang="EN-US"}*]{#struct_0_18971_61630_x1136418366}[：目的端口]{lang="EN-US" style="font-family:宋体"}[号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[protocol]{lang="EN-US"}*]{#struct_0_18971_61630_x1355358980}[：协议名称]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node]{lang="EN-US"}*]{#struct_0_18971_61630_x1667487422}[：匹配]{lang="EN-US" style="font-family:宋体"}[标识（]{style="font-family:宋体"}[Global]{lang="EN-US"}[表示全局，]{lang="EN-US" style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示具体接口]{lang="EN-US" style="font-family:宋体"}[）]{style="font-family:宋体"}

[[An *protocol-version* statistic node of limit *limit-id* using ACL *acl-number* was created (*node*), parameters:]{lang="EN-US"}]{#struct_0_18971_61630_x841429488}

[*[src-ip]{lang="FR"}*]{#struct_0_18971_61630_x1808979255}[/*src-vpn*/*tunnel-id*\--\>*dst-ip*/*dst-vpn*:*dst-port*(*protocol*)]{lang="FR"}

[[HighThres: *amount-max*,  LowThres: *amount-min*]{lang="EN-US"}]{#struct_0_18971_61630_x741227879}

[[连接数限制规则创建了一个统计节点，其中：]{style="font-family:宋体"}]{#struct_0_18971_61630_1038272927}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[protocol]{lang="EN-US"}[-version]{lang="EN-US"}*]{#struct_0_18971_61630_x841101808}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[协议版本（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[src-ip]{lang="FR"}*]{#struct_0_18971_61630_1369408870}[/*src-vpn*/*tunnel-id*]{lang="FR"}[：源]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[源]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[实例的名称]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[ DS Lite Tunnel ID]{lang="EN-US"}[。若不支持或未配置]{style="font-family:宋体"}*[src-vpn]{lang="FR"}*[、]{style="font-family:宋体"}*[tunnel-id]{lang="FR"}*[参数，则仅显示]{style="font-family:宋体"}*[src-ip]{lang="FR"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[src-port]{lang="EN-US"}*]{#struct_0_18971_61630_1613606509}[：源端口]{lang="EN-US" style="font-family:宋体"}[号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dst-ip]{lang="FR"}*]{#struct_0_18971_61630_971370008}[/*dst-vpn*]{lang="FR"}[：目的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[目的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[实例的名称]{lang="EN-US" style="font-family:宋体"}[。若不支持或未配置]{style="font-family:宋体"}*[dst-vpn]{lang="FR"}*[参数，则仅显示]{style="font-family:宋体"}*[dst-ip]{lang="FR"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dst-vpn]{lang="EN-US"}*]{#struct_0_18971_61630_1169171171}[：目的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[实例的名称]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dst-port]{lang="EN-US"}*]{#struct_0_18971_61630_x841036272}[：目的端口]{lang="EN-US" style="font-family:宋体"}[号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[protocol]{lang="EN-US"}*]{#struct_0_18971_61630_1360155845}[：协议名称]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[limit-id]{lang="EN-US"}*]{#struct_0_18971_61630_1782684344}[：连接数限制规则编号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[acl-number]{lang="FR"}*]{#struct_0_18971_61630_x1887745641}[：规则引用的]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="FR"}[编]{style="font-family:宋体"}[号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node]{lang="EN-US"}*]{#struct_0_18971_61630_1253258573}[：匹配]{lang="EN-US" style="font-family:宋体"}[标识（]{style="font-family:宋体"}[Global]{lang="EN-US"}[表示全局，]{lang="EN-US" style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示具体接口]{lang="EN-US" style="font-family:宋体"}[）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[amount-max]{lang="EN-US"}*]{#struct_0_18971_61630_x841626095}[：]{lang="EN-US" style="font-family:宋体"}[连接数]{style="font-family:宋体"}[上限]{lang="EN-US" style="font-family:宋体"}[值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[amount-min]{lang="EN-US"}*]{#struct_0_18971_61630_971789813}[：]{lang="EN-US" style="font-family:宋体"}[连接数]{style="font-family:宋体"}[下限]{lang="EN-US" style="font-family:宋体"}[值]{style="font-family:宋体"}

[[An *protocol-version* statistic node of limit*limit-id* using ACL *acl-number* was deleted (*node*), parameters:]{lang="EN-US"}]{#struct_0_18971_61630_x262551409}

[*[src-ip]{lang="FR"}*]{#struct_0_18971_61630_686724544}[/*src-vpn*/*tunnel*-*id*\--\>*dst-ip*/dst-vpn:*dst-port*(*protocol*)]{lang="FR"}

[[删除了一个统计节点，其中：]{style="font-family:宋体"}]{#struct_0_18971_61630_x841560559}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[protocol]{lang="EN-US"}[-version]{lang="EN-US"}*]{#struct_0_18971_61630_1349521716}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[协议版本（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[src-ip]{lang="FR"}*]{#struct_0_18971_61630_725989327}[/*src-vpn*/*tunnel-id*]{lang="FR"}[：源]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[源]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[实例的名称]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[ DS Lite Tunnel ID]{lang="EN-US"}[。若不支持或未配置]{style="font-family:宋体"}*[src-vpn]{lang="FR"}*[、]{style="font-family:宋体"}*[tunnel-id]{lang="FR"}*[参数，则仅显示]{style="font-family:宋体"}*[src-ip]{lang="FR"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[src-port]{lang="EN-US"}*]{#struct_0_18971_61630_x1291079997}[：源端口]{lang="EN-US" style="font-family:宋体"}[号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dst-ip]{lang="FR"}*]{#struct_0_18971_61630_x841757167}[/*dst-vpn*]{lang="FR"}[：目的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[目的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[实例的名称]{lang="EN-US" style="font-family:宋体"}[。若不支持或未配置]{style="font-family:宋体"}*[dst-vpn]{lang="FR"}*[参数，则仅显示]{style="font-family:宋体"}*[dst-ip]{lang="FR"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dst-port]{lang="EN-US"}*]{#struct_0_18971_61630_1364314728}[：目的端口]{lang="EN-US" style="font-family:宋体"}[号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[protocol]{lang="EN-US"}*]{#struct_0_18971_61630_x463591843}[：协议名称]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[limit-id]{lang="EN-US"}*]{#struct_0_18971_61630_554276292}[：连接数限制规则编号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[acl-number]{lang="FR"}*]{#struct_0_18971_61630_x841691631}[：规则引用的]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="FR"}[编]{style="font-family:宋体"}[号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node]{lang="EN-US"}*]{#struct_0_18971_61630_x1755347416}[：匹配]{lang="EN-US" style="font-family:宋体"}[标识（]{style="font-family:宋体"}[Global]{lang="EN-US"}[表示全局，]{lang="EN-US" style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示具体接口]{lang="EN-US" style="font-family:宋体"}[）]{style="font-family:宋体"}

[[An *protocol-version*  statistic node of limit *limit-id* using ACL *acl-number* was found (*node*), parameters:]{lang="EN-US"}]{#struct_0_18971_61630_x1218323074}

[*[src-ip]{lang="FR"}*]{#struct_0_18971_61630_x841363951}[/*src-vpn*/*tunnel-id*\--\>*dst-ip*/*dst-vpn*:*dst-port*(*protocol*)]{lang="FR"}

[[找到了一个统计节点，其中：]{style="font-family:宋体"}]{#struct_0_18971_61630_x2143511465}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[protocol]{lang="EN-US"}[-version]{lang="EN-US"}*]{#struct_0_18971_61630_x1947697521}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[协议版本（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[src-ip]{lang="FR"}*]{#struct_0_18971_61630_x1855700280}[/*src-vpn*/*tunnel-id*]{lang="FR"}[：源]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[源]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[实例的名称]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[ DS Lite Tunnel ID]{lang="EN-US"}[。若不支持或未配置]{style="font-family:宋体"}*[src-vpn]{lang="FR"}*[、]{style="font-family:宋体"}*[tunnel-id]{lang="FR"}*[参数，则仅显示]{style="font-family:宋体"}*[src-ip]{lang="FR"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[src-port]{lang="EN-US"}*]{#struct_0_18971_61630_x841298415}[：源端口]{lang="EN-US" style="font-family:宋体"}[号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dst-ip]{lang="FR"}*]{#struct_0_18971_61630_x215632509}[/*dst-vpn*]{lang="FR"}[：目的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[目的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[实例的名称]{lang="EN-US" style="font-family:宋体"}[。若不支持或未配置]{style="font-family:宋体"}*[dst-vpn]{lang="FR"}*[参数，则仅显示]{style="font-family:宋体"}*[dst-ip]{lang="FR"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dst-port]{lang="EN-US"}*]{#struct_0_18971_61630_x799610455}[：目的端口]{lang="EN-US" style="font-family:宋体"}[号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[protocol]{lang="EN-US"}*]{#struct_0_18971_61630_x841495023}[：协议名称]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[limit-id]{lang="EN-US"}*]{#struct_0_18971_61630_596489087}[：连接数限制规则编号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[acl-number]{lang="FR"}*]{#struct_0_18971_61630_x2082258595}[：规则引用的]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="FR"}[编]{style="font-family:宋体"}[号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node]{lang="EN-US"}*]{#struct_0_18971_61630_524497818}[：匹配]{lang="EN-US" style="font-family:宋体"}[标识（]{style="font-family:宋体"}[Global]{lang="EN-US"}[表示全局，]{lang="EN-US" style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示具体接口]{lang="EN-US" style="font-family:宋体"}[）]{style="font-family:宋体"}

[[Increased the count value of *node* *protocol-version* statistic node to *value*.]{lang="EN-US"}]{#struct_0_18971_61630_x841429487}

[[全局或接口下的某个统计节点中的连接计数增加：]{style="font-family:宋体"}]{#struct_0_18971_61630_x1809175863}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[node]{lang="EN-US"}]{#struct_0_18971_61630_1872877898}[：匹配标识（]{lang="EN-US" style="font-family:宋体"}[Global]{lang="EN-US"}[表示全局，]{lang="EN-US" style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示具体接口）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[protocol]{lang="EN-US"}[-version]{lang="EN-US"}*]{#struct_0_18971_61630_x841101807}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[协议版本（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[value]{lang="EN-US"}*]{#struct_0_18971_61630_1368950118}[：更新后的统计节点连接计数]{style="font-family:宋体"}

[[Decreased the count value of *node protocol-version* statistic node to *value*.]{lang="EN-US"}]{#struct_0_18971_61630_1996903078}

[[全局或接口下的的某统计节点中的连接计数减少：]{style="font-family:宋体"}]{#struct_0_18971_61630_x841036271}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node]{lang="EN-US"}*]{#struct_0_18971_61630_1360352453}[：匹配]{lang="EN-US" style="font-family:宋体"}[标识（]{style="font-family:宋体"}[Global]{lang="EN-US"}[表示全局，]{lang="EN-US" style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示具体接口]{lang="EN-US" style="font-family:宋体"}[）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[protocol]{lang="EN-US"}[-version]{lang="EN-US"}*]{#struct_0_18971_61630_x1344717534}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[协议版本（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[value]{lang="EN-US"}*]{#struct_0_18971_61630_x841626098}[：更新后的统计节点连接计数]{style="font-family:宋体"}

[[Failed to create *protocol-version* statistic node of limit *limit-id* (*node*)]{lang="EN-US"}]{#struct_0_18971_61630_972117493}

[[创建统计节点失败，其中：]{style="font-family:宋体"}]{#struct_0_18971_61630_1696300893}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[protocol]{lang="EN-US"}[-version]{lang="EN-US"}*]{#struct_0_18971_61630_x841560562}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[协议版本（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[limit-id]{lang="EN-US"}*]{#struct_0_18971_61630_1350242609}[：连接数限制规则编号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node]{lang="EN-US"}*]{#struct_0_18971_61630_1834695709}[：匹配]{lang="EN-US" style="font-family:宋体"}[标识（]{style="font-family:宋体"}[Global]{lang="EN-US"}[表示全局，]{lang="EN-US" style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示具体接口]{lang="EN-US" style="font-family:宋体"}[）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18971_61630_x803090990}

[[\# ]{lang="EN-US"}]{#struct_0_18971_61630_x841757170}[在设备上配置采用连接限制策略]{style="font-family:宋体"}[0]{lang="EN-US"}[对设备的连接数进行统计与限制，其中规则]{style="font-family:宋体"}[0]{lang="EN-US"}[配置为对来自]{style="font-family:宋体"}[192.168.0.0/24]{lang="EN-US"}[网段的用户连接按源地址的方式进行统计与限制，其连接数上下限阈值分别为]{style="font-family:宋体"}[1000]{lang="EN-US"}[和]{style="font-family:宋体"}[900]{lang="EN-US"}[，并打开连接数限制事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging connection-limit event]{lang="EN-US"}]{#struct_0_18971_61630_1363855977}

[\*Aug 18 21:08:14:237 2011 Sysname CONNLMT/7/PACKET:]{lang="EN-US"}

[ EVENT: Connection(192.168.0.210:1405\--\>2.2.2.2:21(tcp)) matched limit 0 of policy 0 (Global).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_18971_61630_495688144}*[匹配到连接数限制规则的用户连接：协议号为]{style="font-family:宋体"}[6]{lang="EN-US"}[（]{style="font-family:宋体"}[TCP]{lang="EN-US"}[），源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.0.210]{lang="EN-US"}[，目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[，源端口为]{style="font-family:宋体"}[1405]{lang="EN-US"}[，目的端口为]{style="font-family:宋体"}[21]{lang="EN-US"}[，源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址不属于任何]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}*

[[\*Aug 18 21:08:14:237 2011 Sysname CONNLMT/7/PACKET:]{lang="EN-US"}]{#struct_0_18971_61630_x660891129}

[ EVENT: An IPv4 statistic node of limit 0 using ACL 3000 was created (Global), parameters:]{lang="EN-US"}

[ 192.168.0.210\--\> Any:0(Any)]{lang="EN-US"}

[ HighThres: 1000, LowThres: 900]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_18971_61630_x1065773468}*[创建了一个按源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址统计的统计节点，连接数上限为]{style="font-family:宋体"}[1000]{lang="EN-US"}[，连接数下限为]{style="font-family:宋体"}[900]{lang="EN-US"}*

[[\*Aug 18 21:08:14:237 2011 Sysname CONNLMT/7/PACKET:]{lang="EN-US"}]{#struct_0_18971_61630_450735340}

[ EVENT: Increased the count value of Global IPv4 statistic node to 200]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_18971_61630_1351391788}*[增加]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[统计节点的统计值到]{style="font-family:宋体"}[200]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_18971_61630_x841691634}[在设备上配置应用全局连接限制策略]{style="font-family:宋体"}[1]{lang="EN-US"}[对设备的连接数进行统计与限制，打开连接数限制事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging connection-limit error]{lang="EN-US"}]{#struct_0_18971_61630_x1755675096}

[\*Aug 18 21:08:14:237 2011 Sysname CONNLMT/7/PACKET:]{lang="EN-US"}

[ ERROR: Failed to create IPv6 statistic node of limit 5 (Global).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_18971_61630_x1974866871}*[在全局统计表中通过规则]{style="font-family:宋体"}[5]{lang="EN-US"}[创建]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[统计节点失败]{style="font-family:宋体"}*
