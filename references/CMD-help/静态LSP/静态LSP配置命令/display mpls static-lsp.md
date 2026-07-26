
**静态LSP \-- 静态LSP配置命令 \-- display mpls static-lsp**

------------------------------------------------------------------------

**[display mpls static-lsp**]命令用来显示静态LSP的信息。

【命令】

**[display mpls static-lsp** [ **lsp-name** *lsp-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[lsp-name*** lsp-name*]：显示指定静态LSP的信息。*lsp-name*表示静态LSP的名称，为1～15个字符的字符串，区分大小写。如果不指定本参数，则显示所有静态LSP的信息。

【举例】

\# 显示所有静态LSP的信息。

\<Sysname\> display mpls static-lsp

Total: 4

Name            FEC                In/Out Label Nexthop/Out Interface    State

egress123       -/-                16/NULL      -                        Up

ingress123      202.118.224.132/32 NULL/1022    100.100.100.19           Down

transit123      -/-                32/1022      100.100.100.17           Down

transit124      -/-                34/1020      POS2/2/0                 Down

表1-1 display mpls static-lsp命令显示信息描述表

字段

描述

Total

静态LSP的总数

Name

静态LSP的名称

FEC

转发等价类，即IP地址前缀和前缀长度

In/Out Label

入标签值/出标签值

Nexthop/Out Interface

下一跳地址或出接口

·如果配置静态LSP时指定了出接口，则显示为出接口

·如果配置静态LSP时指定了下一跳地址，则显示为下一跳地址

State

静态的LSP状态，取值包括：

·Up：表示静态LSP可用

·Down：表示静态LSP不可用

·Idle：表示静态LSP的入标签不可用

·Dup：表示静态LSP与静态CRLSP或静态PW使用了相同的入标签

**静态LSP \-- 静态LSP配置命令 \-- static-lsp egress**

------------------------------------------------------------------------

**[static-lsp egress**]命令用来配置静态LSP的Egress节点。

**[undo static-lsp egress**]命令用来删除静态LSP的Egress节点配置。

【命令】

**[static-lsp egress ***lsp-name* **in-label** *in-label*]

**[undo static-lsp** **egress** *lsp-name*]

【缺省情况】

设备上不存在任何静态LSP。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[lsp-name*]：静态LSP名称，为1～15个字符的字符串，区分大小写。

**[in-label** *in-label*]：指定入标签值，*in-label*取值范围为16～1023。

【使用指导】

如果为静态LSP指定的入标签与已经存在的静态CRLSP/静态PW的入标签相同，则会导致标签冲突，静态LSP不可用。即使修改静态CRLSP/静态PW的入标签，静态LSP仍不可用，需要手工删除该静态LSP并重新配置。

【举例】

\# 在Egress节点上配置一条名为bj-sh的静态LSP，入标签为233。

\<Sysname\> system-view

Sysname static-lsp egress bj-sh in-label 233

【相关命令】

·**display mpls static-lsp**

**静态LSP \-- 静态LSP配置命令 \-- static-lsp ingress**

------------------------------------------------------------------------

**[static-lsp ingress**]命令用来配置静态LSP的Ingress节点。

**[undo static-lsp ingress**]命令用来删除静态LSP的Ingress节点配置。

【命令】

**[static-lsp******ingress**[ *lsp-name* **destination** *dest-addr* { *mask* \| *mask-length* } { **nexthop** *next-hop-addr* \| **outgoing-interface** *interface-type interface-number* } **out-label** *out-label*]]

**[undo static-lsp******ingress** *lsp-name*]

【缺省情况】

设备上不存在任何静态LSP。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[lsp-name*]：静态LSP名称，为1～15个字符的字符串，区分大小写。

**[destination **]*dest-addr*：指定LSP的目的IP地址。

*[mask*]：目的IP地址掩码。

*[mask-length*]：目的IP地址掩码长度，取值范围为0～32。

**[nexthop*** next-hop-addr*]：指定下一跳地址。

**[outgoing-interface*** interface-type interface-number*]：指定出接口的接口类型和接口编号。指定的接口必须为点到点连接类型的接口。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[out-label ***out-label*]：指定出标签值，*out-label*取值范围为0，3，16～1023。

【使用指导】

·配置静态LSP时，指定的下一跳或出接口必须与路由表中最优路由的下一跳或出接口保持一致。通过静态路由配置路由信息时，如果静态路由指定的是出接口，则静态LSP必须指定相同的出接口；如果静态路由指定的是下一跳，则静态LSP必须指定相同的下一跳。

·静态LSP的出接口上必须使能MPLS能力。

【举例】

\# 为Ingress节点配置一条到目的地址202.25.38.1/24的静态LSP，LSP的名称为bj-sh，下一跳地址为202.55.25.33，出标签为237。

\<Sysname\> system-view

Sysname static-lsp ingress bj-sh destination 202.25.38.1 24 nexthop 202.55.25.33 out-label 237

【相关命令】

·**display mpls static-lsp**

**静态LSP \-- 静态LSP配置命令 \-- static-lsp transit**

------------------------------------------------------------------------

**[static-lsp transit**]命令用来配置静态LSP的Transit节点。

**[undo static-lsp transit**]命令用来删除静态LSP的Transit节点配置。

【命令】

**[static-lsp******transit**[ *lsp-name* **in-label** *in-label* { **nexthop** *next-hop-addr* \| **outgoing-interface** *interface-type interface-number* } **out-label** *out-label*]]

**[undo static-lsp transit ***lsp-name*]

【缺省情况】

设备上不存在任何静态LSP。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[lsp-name*]：静态LSP名称，为1～15个字符的字符串，区分大小写。

**[in-label*** in-label*]：指定入标签值，*in-label*取值范围为16～1023。

**[nexthop*** next-hop-addr*]：指定下一跳地址。

**[outgoing-interface*** interface-type interface-number*]：指定出接口的接口类型和接口编号。指定的接口必须为点到点连接类型的接口。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[out-label*** out-label*]：指定出标签值，*out-label*取值范围为0，3，16～1023。

【使用指导】

静态LSP的出接口上必须使能MPLS能力。

如果为静态LSP指定的入标签与已经存在的静态CRLSP/静态PW的入标签相同，则会导致标签冲突，静态LSP不可用。即使修改静态CRLSP/静态PW的入标签，静态LSP仍不可用，需要手工删除该静态LSP并重新配置。

【举例】

\# 为Transit节点配置一条名为bj-sh的静态LSP，入标签为123，下一跳地址为202.34.114.7，出标签为253。

\<Sysname\> system-view

Sysname static-lsp transit bj-sh in-label 123 nexthop 202.34.114.7 out-label 253

【相关命令】

·**display mpls static-lsp**

