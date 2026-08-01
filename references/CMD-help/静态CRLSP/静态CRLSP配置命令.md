<!-- CMD-INDEX
  display mpls static-cr-lsp          | 任意视图             | L8
  static-cr-lsp egress                | 系统视图             | L174
  static-cr-lsp ingress               | 系统视图             | L228
  static-cr-lsp transit               | 系统视图             | L300
-->

**静态CRLSP \-- 静态CRLSP配置命令 \-- display mpls static-cr-lsp**

------------------------------------------------------------------------

**[display mpls static-cr-lsp**]命令用来显示静态CRLSP信息。

【命令】

**[display mpls static-cr-lsp** [ **lsp-name** *lsp-name*   **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[lsp-name*** lsp-name*]：显示指定静态CRLSP的信息。*lsp-name*表示静态CRLSP的名称，为1～15个字符的字符串，区分大小写。如果不指定本参数，则显示所有静态CRLSP的信息。

**[verbose**]：显示静态CRLSP的详细信息。如果不指定本参数，则显示静态CRLSP的简要信息。

【举例】

\# 显示静态CRLSP的简要信息。

\<Sysname\> display mpls static-cr-lsp

Name            LSR Type    In/Out Label   Out Interface        State

static-cr-lsp-1 Ingress     Null/20        GE1/0/1               Up

表1-1 display mpls static-cr-lsp命令显示信息描述表

字段

描述

Name

静态CRLSP的名称

LSR Type

本地节点在静态CRLSP中的LSR类型，取值包括：

·Ingress：表示{.TableTextChar}LSP的入节点{.TableTextChar}

·Transit：表示{.TableTextChar}LSP的中间节点{.TableTextChar}

·Egress：表示{.TableTextChar}LSP的出节点{.TableTextChar}

In/Out Label

入标签值/出标签值

Out Interface

出接口

State

静态CRLSP当前的状态，取值包括：

·Down：表示静态CRLSP不可用

·Up：表示静态CRLSP可用

·Idle：表示静态CRLSP的入标签不可用

·Dup：表示静态CRLSP与静态LSP或静态PW使用了相同的入标签

\# 显示静态CRLSP的详细信息。

\<Sysname\> display mpls static-cr-lsp verbose

LSP Name       : Tunnel0

LSR Type       : Ingress

In-Label       : Null

Out-Label      : 60

Out-Interface  : GE1/0/1

Nexthop        : 20.1.1.2

Class Type     : CT0

Bandwidth      : 0 kbps

LSP State      : Up

表1-2 display mpls static-cr-lsp verbose命令显示信息描述表

字段

描述

LSP Name

静态CRLSP名称

LSR Type

本地节点在静态CRLSP中的LSR类型，取值包括：

·Ingress：表示LSP{.TableTextChar}的入节点{.TableTextChar}

·Transit：表示LSP{.TableTextChar}的中间节点{.TableTextChar}

·Egress：表示LSP{.TableTextChar}的出节点{.TableTextChar}

In-Label

入标签值

Out-Label

出标签值

Out-Interface

出接口名称

Nexthop

下一跳地址

Class Type

静态CRLSP流量所属的服务类型，取值包括CT0、CT1、CT2和CT3

Bandwidth

静态CRLSP流量所需的带宽，单位为kbps

LSP State

静态CRLSP的状态，取值包括：

·Down：表示静态CRLSP不可用

·Up：表示静态CRLSP可用

·Idle：表示静态CRLSP的入标签不可用

·Duplicate：表示静态CRLSP与静态LSP或静态PW使用了相同的入标签

【相关命令】

·**static-cr-lsp egress**

·**static-cr-lsp ingress**

·**static-cr-lsp transit**

**静态CRLSP \-- 静态CRLSP配置命令 \-- static-cr-lsp egress**

------------------------------------------------------------------------

**[static-cr-lsp egress**]命令用来配置静态CRLSP的Egress节点。

**[undo static-cr-lsp egress**]命令用来删除静态CRLSP的Egress节点配置。

【命令】

**[static-cr-lsp egress** *lsp-name* **in-label** *in-label-value*]

**[undo static-cr-lsp egress** *lsp-name*]

【缺省情况】

设备上不存在任何静态CRLSP。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[lsp-name*]：静态CRLSP的名称，为1～15个字符的字符串，区分大小写。

**[in-label*** in-label-value*]：指定入标签。本参数的取值范围与设备的型号有关，请以设备的实际情况为准。

【使用指导】

如果为静态CRLSP指定的入标签与已经存在的静态LSP/静态PW的入标签相同，则会导致标签冲突，静态CRLSP不可用。即使修改静态LSP/静态PW的入标签，静态CRLSP仍不可用，需要手工删除该静态CRLSP并重新配置。

【举例】

\# 在Egress节点上配置一条名称为static-te-1的静态CRLSP，入标签为233。

\<Sysname\> system-view

Sysname static-cr-lsp egress static-te-1 in-label 233

【相关命令】

·**display mpls static-cr-lsp**

·**static-cr-lsp ingress**

·**static-cr-lsp transit**

**静态CRLSP \-- 静态CRLSP配置命令 \-- static-cr-lsp ingress**

------------------------------------------------------------------------

**[static-cr-lsp ingress**]命令用来配置静态CRLSP的Ingress节点。

**[undo static-cr-lsp ingress**]命令用来删除静态CRLSP的Ingress节点配置。

【命令】

**[static-cr-lsp ingress**[ *lsp-name* { **nexthop** *next-hop-addr* \| **outgoing-interface** *interface-type interface-number* } **out-label** *out-label-value* [ **bandwidth** [ **ct0** \| **ct1** \| **ct2** \| **ct3** ] *bandwidth-value* ]]]

**[undo static-cr-lsp ingress** *lsp-name*]

【缺省情况】

设备上不存在任何静态CRLSP。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[lsp-name*]：静态CRLSP的名称，为1～15个字符的字符串，区分大小写。

**[nexthop** *next-hop-addr*]：指定下一跳IP地址。

**[outgoing-interface*** interface-type interface-number*]：指定出接口的接口类型和接口编号。指定的接口必须为点到点连接类型的接口。

**[out-label*** out-label-value*]：指定出标签值，取值范围为0，3，16～1023。

**[bandwidth**]：指定静态CRLSP流量所属的服务类型和所需的带宽。如果不指定本参数，则静态CRLSP流量所需的带宽为0；如果指定了本参数，但没有指定任何CT，则缺省为CT 0。

**[ct0**]：静态CRLSP流量属于CT 0。

**[ct1**]：静态CRLSP流量属于CT 1。

**[ct2**]：静态CRLSP流量属于CT 2。

**[ct3**]：静态CRLSP流量属于CT 3。

*[bandwidth-value*]：静态CRLSP流量所需的带宽，取值范围为1～4294967295，单位为kbps，缺省值为0。

【使用指导】

在Prestandard DS-TE模式下，配置为CT 2和CT 3是无效的，隧道不会建立。只有在IETF模式下，配置为CT 2和CT 3才有效。

指定的下一跳地址不能是本地设备上的公网IP地址。

【举例】

\# 在Ingress节点上配置一条名称为static-te-2的静态CRLSP，下一跳IP地址为202.55.25.33，出标签为237，流量所属的服务类型为CT 0，所需要的带宽为20kbps。

\<Sysname\> system-view

Sysname static-cr-lsp ingress static-te-2 nexthop 202.55.25.33 out-label 237 bandwidth ct0 20

【相关命令】

·**display mpls static-cr-lsp**

·**static-cr-lsp egress**

·**static-cr-lsp transit**

**静态CRLSP \-- 静态CRLSP配置命令 \-- static-cr-lsp transit**

------------------------------------------------------------------------

**[static-cr-lsp transit**]命令用来配置静态CRLSP的Transit节点。

**[undo static-cr-lsp transit**]命令用来删除静态CRLSP的Transit节点配置。

【命令】

**[static-cr-lsp**[ **transit** *lsp-name* **in-label** *in-label-value* { **nexthop** *next-hop-addr* \| **outgoing-interface** *interface-type interface-number* } **out-label** *out-label-value* [ **bandwidth** [ **ct0** \| **ct1** \| **ct2** \| **ct3** ] *bandwidth-value* ]]]

**[undo static-cr-lsp** **transit** *lsp-name*]

【缺省情况】

设备上不存在任何静态CRLSP。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[lsp-name*]：静态CRLSP的名称，为1～15个字符的字符串，区分大小写。

**[in-label** *in-label-value*]：指定入标签值，取值范围为16～1023。

**[nexthop** *next-hop-addr*]：指定下一跳IP地址。

**[outgoing-interface** *interface-type interface-number*]：指定出接口的接口类型和接口编号。指定的接口必须为点到点连接类型的接口。

**[out-label** *out-label-value*]：指定出标签值，取值范围为0，3，16～1023。

**[bandwidth**]：指定静态CRLSP流量所属的服务类型和流量所需的带宽。如果不指定本参数，则静态CRLSP流量所需的带宽为0；如果指定了本参数，但没有指定任何CT，则缺省为CT 0。

**[ct0**]：静态CRLSP流量属于CT 0。

**[ct1**]：静态CRLSP流量属于CT 1。

**[ct2**]：静态CRLSP流量属于CT 2。

**[ct3**]：静态CRLSP流量属于CT 3。

*[bandwidth-value*]：静态CRLSP流量所需的带宽，取值范围为1～4294967295，单位为kbps，缺省值为0。

【使用指导】

在Prestandard DS-TE模式下，配置为CT 2和CT 3是无效的，隧道不会建立。只有在IETF模式下，配置为CT 2和CT 3才有效。

指定的下一跳地址不能是本地设备上的公网IP地址。

如果为静态CRLSP指定的入标签与已经存在的静态LSP/静态PW的入标签相同，则会导致标签冲突，静态CRLSP不可用。即使修改静态LSP/静态PW的入标签，静态CRLSP仍不可用，需要手工删除该静态CRLSP并重新配置。

【举例】

\# 在Transit节点上配置一条名称为static-te-3的静态CRLSP，入标签为123，下一跳IP地址为1.1.1.1，出标签为253，流量所属的服务类型为CT 0，所需带宽为20kbps。

\<Sysname\> system-view

Sysname static-cr-lsp transit static-te-3 in-label 123 nexthop 1.1.1.1 out-label 253 bandwidth ct0 20

【相关命令】

·**display mpls static-cr-lsp**

·**static-cr-lsp egress**

·**static-cr-lsp ingress**

