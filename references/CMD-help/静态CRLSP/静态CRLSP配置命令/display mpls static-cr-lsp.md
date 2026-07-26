::: {#1299931629 .myid}
[]{#_Toc333936449}[]{#_Toc317060423}[]{#_Toc67196105}[]{#_Toc67145930}[]{#_Toc59929598}[]{#_Toc50284024}[]{#_Toc404790916}[]{#struct_0_21320_79070_x1528565170}[]{#_Toc333936375}

**静态CRLSP \-- 静态CRLSP配置命令 \-- display mpls static-cr-lsp**

------------------------------------------------------------------------

[**[display mpls static-cr-lsp]{lang="EN-US"}**]{#struct_0_21320_79070_x273246917}[命令用来显示静态]{style="font-family:
宋体"}[CRLSP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21320_79070_432127358}

[**[display mpls static-cr-lsp]{lang="EN-US"}**[ \[ **lsp-name** *lsp-name* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_21320_79070_391085288}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21320_79070_x1655631363}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21320_79070_x571793392}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21320_79070_x1632627432}

[[network-admin]{lang="EN-US"}]{#struct_0_21320_79070_x1469660357}

[[network-operator]{lang="EN-US"}]{#struct_0_21320_79070_x251163519}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21320_79070_x1868786634}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21320_79070_x552435692}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21320_79070_x1177638006}

[**[lsp-name]{lang="EN-US"}***[ lsp-name]{lang="EN-US"}*]{#struct_0_21320_79070_11944325}[：显示指定静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[lsp-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则显示所有静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_21320_79070_1085104054}[：显示静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[的详细信息。如果不指定本参数，则显示静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[的简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21320_79070_1359235524}

[[\# ]{lang="EN-US"}]{#struct_0_21320_79070_x1632692968}[显示静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display mpls static-cr-lsp]{lang="EN-US"}]{#struct_0_21320_79070_x2049024571}

[Name            LSR Type    In/Out Label   Out Interface        State]{lang="EN-US"}

[static-cr-lsp-1 Ingress     Null/20        GE1/0/1               Up]{lang="EN-US"}

[]{#struct_0_21320_79070_1492851300}[[表1-1 ]{lang="EN-US"}[display mpls static-cr-lsp]{lang="EN-US"}]{#_Toc137974527}[命令]{style="font-family:黑体"}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_72885550}[[字段]{style="font-family:黑体"}]{#struct_0_21320_79070_x1001200886}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_21320_79070_x1539984174}

[[Name]{lang="EN-US"}]{#struct_0_21320_79070_x787050140}

[[静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}]{#struct_0_21320_79070_606553089}[的名称]{style="font-family:宋体"}

[[LSR Type]{lang="EN-US"}]{#struct_0_21320_79070_x1607518855}

[[本地节点在静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}]{#struct_0_21320_79070_x1632758504}[中的]{style="font-family:宋体"}[LSR]{lang="EN-US"}[类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ingress]{lang="EN-US"}]{#struct_0_21320_79070_1893029825}[[：表示]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[LSP]{lang="EN-US"}[[的入节点]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Transit]{lang="EN-US"}]{#struct_0_21320_79070_241385276}[[：表示]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[LSP]{lang="EN-US"}[[的中间节点]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Egress]{lang="EN-US"}]{#struct_0_21320_79070_x1586622868}[[：表示]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[LSP]{lang="EN-US"}[[的出节点]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[In/Out Label]{lang="EN-US"}]{#struct_0_21320_79070_1733693462}

[[入标签值]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21320_79070_99387757}[出标签值]{style="font-family:宋体"}

[[Out Interface]{lang="EN-US"}]{#struct_0_21320_79070_x1632299752}

[[出接口]{style="font-family:宋体"}]{#struct_0_21320_79070_x297164251}

[[State]{lang="EN-US"}]{#struct_0_21320_79070_x1893730293}

[[静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}]{#struct_0_21320_79070_x1733735438}[当前的状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_21320_79070_x191144746}[：表示]{lang="EN-US" style="font-family:宋体"}[静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[不可用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_21320_79070_x812451830}[：表示]{lang="EN-US" style="font-family:宋体"}[静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[可用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Idle]{lang="EN-US"}]{#struct_0_21320_79070_1877324348}[：表示静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[的入标签不可用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Dup]{lang="EN-US"}]{#struct_0_21320_79070_1595148178}[：表示静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[与静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[或静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[使用了相同的入标签]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21320_79070_x1632365288}[显示静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display mpls static-cr-lsp verbose]{lang="EN-US"}]{#struct_0_21320_79070_1167677675}

[LSP Name       : Tunnel0]{lang="EN-US"}

[LSR Type       : Ingress]{lang="EN-US"}

[In-Label       : Null]{lang="EN-US"}

[Out-Label      : 60]{lang="EN-US"}

[Out-Interface  : GE1/0/1]{lang="EN-US"}

[Nexthop        : 20.1.1.2]{lang="EN-US"}

[Class Type     : CT0]{lang="EN-US"}

[Bandwidth      : 0 kbps]{lang="EN-US"}

[LSP State      : Up]{lang="EN-US"}

[]{#struct_0_21320_79070_749437888}[[表1-2 ]{lang="EN-US"}[display mpls static-cr-lsp verbose]{lang="EN-US"}]{#_Toc137974528}[命令]{style="font-family:黑体"}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_75056124}[[字段]{style="font-family:黑体"}]{#struct_0_21320_79070_1680579062}

[[描述]{style="font-family:黑体"}]{#struct_0_21320_79070_x330676593}

[[LSP Name]{lang="EN-US"}]{#struct_0_21320_79070_532871590}

[[静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}]{#struct_0_21320_79070_x1632824043}[名称]{style="font-family:宋体"}

[[LSR Type]{lang="EN-US"}]{#struct_0_21320_79070_x318157148}

[[本地节点在静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}]{#struct_0_21320_79070_x1713224015}[中的]{style="font-family:宋体"}[LSR]{lang="EN-US"}[类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ingress]{lang="EN-US"}]{#struct_0_21320_79070_x1716943596}[[：表示]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}]{.TableTextChar}[[的入节点]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Transit]{lang="EN-US"}]{#struct_0_21320_79070_368601411}[[：表示]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}]{.TableTextChar}[[的中间节点]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Egress]{lang="EN-US"}]{#struct_0_21320_79070_x1542766244}[[：表示]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}]{.TableTextChar}[[的出节点]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[In-Label]{lang="EN-US"}]{#struct_0_21320_79070_1277739432}

[[入标签值]{style="font-family:宋体"}]{#struct_0_21320_79070_x1632889579}

[[Out-Label]{lang="EN-US"}]{#struct_0_21320_79070_2027403891}

[[出标签值]{style="font-family:宋体"}]{#struct_0_21320_79070_1885570477}

[[Out-Interface]{lang="EN-US"}]{#struct_0_21320_79070_288650954}

[[出接口名称]{style="font-family:宋体"}]{#struct_0_21320_79070_196754139}

[[Nexthop]{lang="EN-US"}]{#struct_0_21320_79070_482985933}

[[下一跳地址]{style="font-family:宋体"}]{#struct_0_21320_79070_x1632955115}

[[Class Type]{lang="EN-US"}]{#struct_0_21320_79070_x1158886304}

[[静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}]{#struct_0_21320_79070_x1250522694}[流量所属的服务类型，取值包括]{style="font-family:宋体"}[CT0]{lang="EN-US"}[、]{style="font-family:宋体"}[CT1]{lang="EN-US"}[、]{style="font-family:宋体"}[CT2]{lang="EN-US"}[和]{style="font-family:宋体"}[CT3]{lang="EN-US"}

[[Bandwidth]{lang="EN-US"}]{#struct_0_21320_79070_x316865696}

[[静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}]{#struct_0_21320_79070_1957507321}[流量所需的带宽，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}

[[LSP State]{lang="EN-US"}]{#struct_0_21320_79070_x1633020651}

[[静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}]{#struct_0_21320_79070_x928029259}[的状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_21320_79070_x727967262}[：表示]{lang="EN-US" style="font-family:宋体"}[静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[不可用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_21320_79070_1285917983}[：表示]{lang="EN-US" style="font-family:宋体"}[静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[可用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Idle]{lang="EN-US"}]{#struct_0_21320_79070_1877652028}[：表示静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[的入标签不可用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Duplicate]{lang="EN-US"}]{#struct_0_21320_79070_x1139597831}[：表示静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[与静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[或静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[使用了相同的入标签]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21320_79070_x1087777756}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[static-cr-lsp egress]{lang="EN-US"}**]{#struct_0_21320_79070_899520776}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[static-cr-lsp ingress]{lang="EN-US"}**]{#struct_0_21320_79070_x2131564783}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[static-cr-lsp transit]{lang="EN-US"}**]{#struct_0_21320_79070_x1632561899}

::: {#1932635163 .myid}
[]{#_Toc404790917}[]{#struct_0_21320_79070_x1037638582}

**静态CRLSP \-- 静态CRLSP配置命令 \-- static-cr-lsp egress**

------------------------------------------------------------------------

[**[static-cr-lsp egress]{lang="FR"}**]{#struct_0_21320_79070_893363886}[命令用来配置静态]{style="font-family:宋体"}[CRLSP]{lang="FR"}[的]{style="font-family:宋体"}[Egress]{lang="FR"}[节点。]{style="font-family:宋体"}

[**[undo static-cr-lsp egress]{lang="FR"}**]{#struct_0_21320_79070_645845824}[命令用来删除静态]{style="font-family:宋体"}[CRLSP]{lang="FR"}[的]{style="font-family:宋体"}[Egress]{lang="FR"}[节点配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21320_79070_1291365348}

[**[static-cr-lsp egress]{lang="EN-US"}**[ *lsp-name* **in-label** *in-label-value*]{lang="EN-US"}]{#struct_0_21320_79070_1590605469}

[**[undo static-cr-lsp egress]{lang="EN-US"}**[ *lsp-name*]{lang="EN-US"}]{#struct_0_21320_79070_1650112053}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21320_79070_x1399243842}

[[设备上不存在任何静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}]{#struct_0_21320_79070_x324370533}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21320_79070_x1632627435}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21320_79070_902992638}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21320_79070_x1768920685}

[[network-admin]{lang="EN-US"}]{#struct_0_21320_79070_x75951780}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21320_79070_1343013420}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21320_79070_1913573181}

[*[lsp-name]{lang="EN-US"}*]{#struct_0_21320_79070_160343737}[：静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[in-label]{lang="EN-US"}***[ in-label-value]{lang="EN-US"}*]{#struct_0_21320_79070_1252163893}[：指定入标签。本参数的取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21320_79070_1877783100}

[[如果为静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}]{#struct_0_21320_79070_x1893095103}[指定的入标签与已经存在的静态]{style="font-family:宋体"}[LSP/]{lang="EN-US"}[静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[的入标签相同，则会导致标签冲突，静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[不可用。即使修改静态]{style="font-family:宋体"}[LSP/]{lang="EN-US"}[静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[的入标签，静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[仍不可用，需要手工删除该静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[并重新配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21320_79070_x811677926}

[[\# ]{lang="FR"}]{#struct_0_21320_79070_893929336}[在]{style="font-family:宋体"}[Egress]{lang="FR"}[节点上配置一条名称为]{style="font-family:宋体"}[static-te-1]{lang="FR"}[的]{style="font-family:宋体"}[静态]{style="font-family:宋体"}[CRLSP]{lang="FR"}[，]{style="font-family:宋体"}[入标签为]{style="font-family:宋体"}[233]{lang="FR"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="FR"}]{#struct_0_21320_79070_x1632692971}

[\[Sysname\] static-cr-lsp egress static-te-1 in-label 233]{lang="FR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21320_79070_323693960}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}**[display mpls static-cr-lsp]{lang="EN-US"}**]{#struct_0_21320_79070_x85509201}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}**[static-cr-lsp ingress]{lang="FR"}**]{#struct_0_21320_79070_868681838}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}**[static-cr-lsp transit]{lang="FR"}**]{#struct_0_21320_79070_452717858}
:::

::: {#1311817263 .myid}
[]{#_Toc404790918}[]{#struct_0_21320_79070_1819853659}[]{#_Toc333936450}[]{#_Toc317060424}[]{#_Toc67196106}[]{#_Toc67145931}[]{#_Toc59929596}[]{#_Toc50284022}

**静态CRLSP \-- 静态CRLSP配置命令 \-- static-cr-lsp ingress**

------------------------------------------------------------------------

[**[static-cr-lsp ingress]{lang="FR"}**]{#struct_0_21320_79070_x836327857}[命令用来配置静态]{style="font-family:宋体"}[CRLSP]{lang="FR"}[的]{style="font-family:宋体"}[Ingress]{lang="FR"}[节点。]{style="font-family:宋体"}

[**[undo static-cr-lsp ingress]{lang="FR"}**]{#struct_0_21320_79070_644908134}[命令用来删除静态]{style="font-family:宋体"}[CRLSP]{lang="FR"}[的]{style="font-family:宋体"}[Ingress]{lang="FR"}[节点配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21320_79070_1541970664}

[**[static-cr-lsp ingress]{lang="EN-US"}**[ *lsp-name* { **nexthop** *next-hop-addr* \| **outgoing-interface** *interface-type interface-number* } **out-label** *out-label-value* \[ **bandwidth** \[ **ct0** \| **ct1** \| **ct2** \| **ct3** \] *bandwidth-value* \]]{lang="EN-US"}]{#struct_0_21320_79070_x1632758507}

[**[undo static-cr-lsp ingress]{lang="EN-US"}**[ *lsp-name*]{lang="EN-US"}]{#struct_0_21320_79070_1489745298}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21320_79070_763739665}

[[设备上不存在任何静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}]{#struct_0_21320_79070_x692776448}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21320_79070_x734130303}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21320_79070_x1975524849}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21320_79070_x640913167}

[[network-admin]{lang="EN-US"}]{#struct_0_21320_79070_x1930912491}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21320_79070_1816035736}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21320_79070_x1632299755}

[*[lsp-name]{lang="EN-US"}*]{#struct_0_21320_79070_x1056679138}[：静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[nexthop]{lang="EN-US"}**[ *next-hop-addr*]{lang="EN-US"}]{#struct_0_21320_79070_1919987016}[：指定下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[outgoing-interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_21320_79070_1680963738}[：指定出接口的接口类型和接口编号。指定的接口必须为点到点连接类型的接口。]{style="font-family:宋体"}

[**[out-label]{lang="EN-US"}***[ out-label-value]{lang="EN-US"}*]{#struct_0_21320_79070_55771568}[：指定出标签值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[，]{style="font-family:宋体"}[3]{lang="EN-US"}[，]{style="font-family:宋体"}[16]{lang="EN-US"}[～]{style="font-family:宋体"}[1023]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[bandwidth]{lang="EN-US"}**]{#struct_0_21320_79070_1804394601}[：指定静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[流量所属的服务类型和所需的带宽。如果不指定本参数，则静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[流量所需的带宽为]{style="font-family:宋体"}[0]{lang="EN-US"}[；如果指定了本参数，但没有指定任何]{style="font-family:宋体"}[CT]{lang="EN-US"}[，则缺省为]{style="font-family:宋体"}[CT 0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ct0]{lang="EN-US"}**]{#struct_0_21320_79070_x1077741959}[：静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[流量属于]{style="font-family:宋体"}[CT 0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ct1]{lang="EN-US"}**]{#struct_0_21320_79070_826671881}[：静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[流量属于]{style="font-family:宋体"}[CT 1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ct2]{lang="EN-US"}**]{#struct_0_21320_79070_1676593273}[：静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[流量属于]{style="font-family:宋体"}[CT 2]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ct3]{lang="EN-US"}**]{#struct_0_21320_79070_x914380549}[：静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[流量属于]{style="font-family:宋体"}[CT 3]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[bandwidth-value]{lang="EN-US"}*]{#struct_0_21320_79070_x1632365291}[：静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[流量所需的带宽，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21320_79070_x1917501576}

[[在]{style="font-family:宋体"}]{#struct_0_21320_79070_x902469036}[Prestandard DS-TE]{lang="FR"}[模式下]{style="font-family:宋体"}[，]{style="font-family:宋体"}[配置为]{style="font-family:宋体"}[CT 2]{lang="FR"}[和]{style="font-family:宋体"}[CT 3]{lang="FR"}[是无效的]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[隧道不会建立。只有在]{style="font-family:
宋体"}[IETF]{lang="FR"}[模式下]{style="font-family:宋体"}[，]{style="font-family:宋体"}[配置为]{style="font-family:宋体"}[CT 2]{lang="FR"}[和]{style="font-family:宋体"}[CT 3]{lang="FR"}[才有效。]{style="font-family:宋体"}

[[指定的下一跳地址不能是本地设备上的公网]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_21320_79070_x1205794090}[地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21320_79070_x427980707}

[[\# ]{lang="EN-US"}]{#struct_0_21320_79070_1259340221}[在]{style="font-family:宋体"}[Ingress]{lang="EN-US"}[节点上配置一条名称为]{style="font-family:宋体"}[static-te-2]{lang="EN-US"}[的静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[，下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[202.55.25.33]{lang="EN-US"}[，出标签为]{style="font-family:宋体"}[237]{lang="EN-US"}[，流量所属的服务类型为]{style="font-family:宋体"}[CT 0]{lang="EN-US"}[，所需要的带宽为]{style="font-family:宋体"}[20kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21320_79070_x1684789962}

[\[Sysname\] static-cr-lsp ingress static-te-2 nexthop 202.55.25.33 out-label 237 bandwidth ct0 20]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21320_79070_x513695314}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mpls static-cr-lsp]{lang="EN-US"}**]{#struct_0_21320_79070_x1831063376}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[static-cr-lsp egress]{lang="EN-US"}**]{#struct_0_21320_79070_x1632824042}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[static-cr-lsp transit]{lang="EN-US"}**]{#struct_0_21320_79070_x1884241089}
:::

::: {#1611672735 .myid}
[]{#_Toc404790919}[]{#struct_0_21320_79070_1088674308}[]{#_Toc333936451}[]{#_Toc317060425}[]{#_Toc67196107}[]{#_Toc67145932}[]{#_Toc59929597}[]{#_Toc50284023}

**静态CRLSP \-- 静态CRLSP配置命令 \-- static-cr-lsp transit**

------------------------------------------------------------------------

[**[static-cr-lsp transit]{lang="FR"}**]{#struct_0_21320_79070_x912307812}[命令用来配置静态]{style="font-family:宋体"}[CRLSP]{lang="FR"}[的]{style="font-family:宋体"}[Transit]{lang="FR"}[节点。]{style="font-family:宋体"}

[**[undo static-cr-lsp transit]{lang="FR"}**]{#struct_0_21320_79070_x1783609640}[命令用来删除静态]{style="font-family:宋体"}[CRLSP]{lang="FR"}[的]{style="font-family:宋体"}[Transit]{lang="FR"}[节点配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21320_79070_x392113419}

[**[static-cr-lsp]{lang="EN-US"}**[ **transit** *lsp-name* **in-label** *in-label-value* { **nexthop** *next-hop-addr* \| **outgoing-interface** *interface-type interface-number* } **out-label** *out-label-value* \[ **bandwidth** \[ **ct0** \| **ct1** \| **ct2** \| **ct3** \] *bandwidth-value* \]]{lang="EN-US"}]{#struct_0_21320_79070_x1434269742}

[**[undo static-cr-lsp]{lang="EN-US"}**[ **transit** *lsp-name*]{lang="EN-US"}]{#struct_0_21320_79070_x592076052}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21320_79070_x40432013}

[[设备上不存在任何静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}]{#struct_0_21320_79070_x1632889578}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21320_79070_461319950}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21320_79070_1712136189}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21320_79070_x415437261}

[[network-admin]{lang="EN-US"}]{#struct_0_21320_79070_602556222}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21320_79070_2020802250}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21320_79070_x47313006}

[*[lsp-name]{lang="EN-US"}*]{#struct_0_21320_79070_672530934}[：静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[in-label]{lang="EN-US"}**[ *in-label-value*]{lang="EN-US"}]{#struct_0_21320_79070_979447598}[：指定入标签值，取值范围为]{style="font-family:宋体"}[16]{lang="EN-US"}[～]{style="font-family:宋体"}[1023]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[nexthop]{lang="EN-US"}**[ *next-hop-addr*]{lang="EN-US"}]{#struct_0_21320_79070_x696921191}[：指定下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[outgoing-interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_21320_79070_x1632955114}[：指定出接口的接口类型和接口编号。指定的接口必须为点到点连接类型的接口。]{style="font-family:宋体"}

[**[out-label]{lang="EN-US"}**[ *out-label-value*]{lang="EN-US"}]{#struct_0_21320_79070_407197637}[：指定出标签值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[，]{style="font-family:宋体"}[3]{lang="EN-US"}[，]{style="font-family:
宋体"}[16]{lang="EN-US"}[～]{style="font-family:宋体"}[1023]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[bandwidth]{lang="EN-US"}**]{#struct_0_21320_79070_x2081301926}[：指定静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[流量所属的服务类型和流量所需的带宽。如果不指定本参数，则静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[流量所需的带宽为]{style="font-family:宋体"}[0]{lang="EN-US"}[；如果指定了本参数，但没有指定任何]{style="font-family:宋体"}[CT]{lang="EN-US"}[，则缺省为]{style="font-family:宋体"}[CT 0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ct0]{lang="EN-US"}**]{#struct_0_21320_79070_1689040083}[：静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[流量属于]{style="font-family:宋体"}[CT 0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ct1]{lang="EN-US"}**]{#struct_0_21320_79070_x520259735}[：静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[流量属于]{style="font-family:宋体"}[CT 1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ct2]{lang="EN-US"}**]{#struct_0_21320_79070_x1338762713}[：静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[流量属于]{style="font-family:宋体"}[CT 2]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ct3]{lang="EN-US"}**]{#struct_0_21320_79070_1427976660}[：静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[流量属于]{style="font-family:宋体"}[CT 3]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[bandwidth-value]{lang="EN-US"}*]{#struct_0_21320_79070_x1833416315}[：静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[流量所需的带宽，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21320_79070_x231104441}

[[在]{style="font-family:宋体"}]{#struct_0_21320_79070_x1972891744}[Prestandard DS-TE]{lang="FR"}[模式下]{style="font-family:宋体"}[，]{style="font-family:宋体"}[配置为]{style="font-family:宋体"}[CT 2]{lang="FR"}[和]{style="font-family:宋体"}[CT 3]{lang="FR"}[是无效的]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[隧道不会建立。只有在]{style="font-family:
宋体"}[IETF]{lang="FR"}[模式下]{style="font-family:宋体"}[，]{style="font-family:宋体"}[配置为]{style="font-family:宋体"}[CT 2]{lang="FR"}[和]{style="font-family:宋体"}[CT 3]{lang="FR"}[才有效。]{style="font-family:宋体"}

[[指定的下一跳地址不能是本地设备上的公网]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_21320_79070_x1633020650}[地址。]{style="font-family:宋体"}

[[如果为静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}]{#struct_0_21320_79070_1877455419}[指定的入标签与已经存在的静态]{style="font-family:宋体"}[LSP/]{lang="EN-US"}[静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[的入标签相同，则会导致标签冲突，静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[不可用。即使修改静态]{style="font-family:宋体"}[LSP/]{lang="EN-US"}[静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[的入标签，静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[仍不可用，需要手工删除该静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[并重新配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21320_79070_1800854096}

[[\# ]{lang="EN-US"}]{#struct_0_21320_79070_x2021264043}[在]{style="font-family:宋体"}[Transit]{lang="EN-US"}[节点上配置一条名称为]{style="font-family:宋体"}[static-te-3]{lang="EN-US"}[的静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[，入标签为]{style="font-family:宋体"}[123]{lang="EN-US"}[，]{style="font-family:宋体"}[下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，出标签为]{style="font-family:宋体"}[253]{lang="EN-US"}[，流量所属的服务类型为]{style="font-family:宋体"}[CT 0]{lang="EN-US"}[，所需带宽为]{style="font-family:宋体"}[20kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21320_79070_593973301}

[\[Sysname\] static-cr-lsp transit static-te-3 in-label 123 nexthop 1.1.1.1 out-label 253 bandwidth ct0 20]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21320_79070_1386510682}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mpls static-cr-lsp]{lang="EN-US"}**]{#struct_0_21320_79070_x694847785}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[static-cr-lsp egress]{lang="EN-US"}**]{#struct_0_21320_79070_288856907}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[static-cr-lsp ingress]{lang="EN-US"}**]{#struct_0_21320_79070_1973500632}

[ ]{lang="EN-US"}
:::
