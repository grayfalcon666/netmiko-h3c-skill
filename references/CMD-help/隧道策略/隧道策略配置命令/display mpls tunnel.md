::: {#1282355211 .myid}
[]{#_Toc404791028}[]{#struct_0_13623_x1941_774196204}

**隧道策略 \-- 隧道策略配置命令 \-- display mpls tunnel**

------------------------------------------------------------------------

[**[display mpls tunnel]{lang="EN-US"}**]{#struct_0_13623_x1941_x2143010298}[命令用来显示隧道信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13623_x1941_x687576468}

[**[display mpls tunnel]{lang="EN-US"}**[ { **all** \| **statistics** \| \[ **vpn-instance** *vpn-instance-name* \] **destination** { *tunnel-ipv4-dest* \| *tunnel-ipv6-dest* } }]{lang="EN-US"}]{#struct_0_13623_x1941_x1980665792}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13623_x1941_1219529403}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13623_x1941_x331991873}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13623_x1941_922644056}

[[network-admin]{lang="EN-US"}]{#struct_0_13623_x1941_x1370599166}

[[network-operator]{lang="EN-US"}]{#struct_0_13623_x1941_1222881401}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13623_x1941_1244112755}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13623_x1941_839211654}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13623_x1941_1664506767}

[**[all]{lang="EN-US"}**]{#struct_0_13623_x1941_629149384}[：显示所有隧道的信息。]{style="font-family:宋体"}

[**[statistics]{lang="EN-US"}**]{#struct_0_13623_x1941_x1980731328}[：显示隧道的统计信息。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_13623_x1941_x1560198806}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的隧道信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[字符的字符串，区分大小写。如果没有指定本参数，则显示公网的隧道信息。]{style="font-family:宋体"}

[**[destination]{lang="EN-US"}**]{#struct_0_13623_x1941_85191868}[：显示目的地址为指定地址的隧道的信息。]{style="font-family:宋体"}

[*[tunnel-ipv4-dest]{lang="EN-US"}*]{#struct_0_13623_x1941_923131750}[：显示目的地址为指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址的隧道的信息。]{style="font-family:宋体"}*[tunnel-ipv4-dest]{lang="EN-US"}*[为隧道目的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[tunnel-ipv6-dest]{lang="EN-US"}*]{#struct_0_13623_x1941_x1583557259}[：显示目的地址为指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的隧道的信息。]{style="font-family:宋体"}*[tunnel-ipv6-dest]{lang="EN-US"}*[为隧道目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13623_x1941_x914099375}

[[\# ]{lang="EN-US"}]{#struct_0_13623_x1941_1182925299}[显示所有隧道的信息。]{style="font-family:宋体"}

[[\<Sysname\> display mpls tunnel all]{lang="EN-US"}]{#struct_0_13623_x1941_x1980796864}

[Destination      Type     Tunnel/NHLFE      VPN Instance]{lang="EN-US"}

[2.2.2.2          LSP      NHLFE1024         -]{lang="EN-US"}

[3.3.3.3          CRLSP    Tunnel2           -]{lang="EN-US"}

[3.3.3.3          GRE      Tunnel3           -]{lang="EN-US"}

[4.4.4.4          CRLSP    Tunnel-Bundle0    -]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display mpls tunnel all]{lang="EN-US"}]{#struct_0_13623_x1941_x1745624085}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1938243616}[[字段]{style="font-family:黑体"}]{#struct_0_13623_x1941_1888847190}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13623_x1941_1539494978}

[[Destination]{lang="EN-US"}]{#struct_0_13623_x1941_x990625239}

[[隧道目的地址]{style="font-family:宋体"}]{#struct_0_13623_x1941_x1477278667}

[[Type]{lang="EN-US"}]{#struct_0_13623_x1941_334221763}

[[隧道类型，取值包括]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_13623_x1941_x1980862400}[、]{style="font-family:宋体"}[GRE]{lang="EN-US"}[和]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[（表示]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道）]{style="font-family:宋体"}

[[Tunnel/NHLFE]{lang="EN-US"}]{#struct_0_13623_x1941_x89677436}

[[Tunnel]{lang="EN-US"}]{#struct_0_13623_x1941_1060501682}[隧道、捆绑隧道或]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项]{style="font-family:宋体"}

[[取值为]{style="font-family:宋体"}[NHLFE*number*]{lang="EN-US"}]{#struct_0_13623_x1941_189319116}[时，表示与]{style="font-family:宋体"}[NID]{lang="EN-US"}[为]{style="font-family:宋体"}*[number]{lang="EN-US"}*[的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项对应的]{style="font-family:宋体"}[Ingress LSP]{lang="EN-US"}

[[VPN Instance]{lang="EN-US"}]{#struct_0_13623_x1941_x184949771}

[[VPN]{lang="EN-US"}]{#struct_0_13623_x1941_x1170336499}[实例名称，为"]{style="font-family:宋体"}[-]{lang="EN-US"}["表示公网]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13623_x1941_1841054499}[显示隧道的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display mpls tunnel statistics]{lang="EN-US"}]{#struct_0_13623_x1941_x1979879360}

[LSP  :     1]{lang="EN-US"}

[GRE  :     0]{lang="EN-US"}

[CRLSP:     0]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display mpls tunnel statistics]{lang="EN-US"}]{#struct_0_13623_x1941_566225072}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1944914496}[[字段]{style="font-family:黑体"}]{#struct_0_13623_x1941_411124487}

[[描述]{style="font-family:黑体"}]{#struct_0_13623_x1941_2117190359}

[[LSP]{lang="EN-US"}]{#struct_0_13623_x1941_x608110530}

[[LSP]{lang="EN-US"}]{#struct_0_13623_x1941_1999696095}[隧道的数量]{style="font-family:宋体"}

[[GRE]{lang="EN-US"}]{#struct_0_13623_x1941_x1623768664}

[[GRE]{lang="EN-US"}]{#struct_0_13623_x1941_x1979944896}[隧道的数量]{style="font-family:宋体"}

[[CRLSP]{lang="EN-US"}]{#struct_0_13623_x1941_1327173792}

[[CRLSP]{lang="EN-US"}]{#struct_0_13623_x1941_811176331}[（]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[）隧道的数量]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-702184333 .myid}
[]{#_Toc404791029}[]{#struct_0_13623_x1941_x227753767}

**隧道策略 \-- 隧道策略配置命令 \-- preferred-path**

------------------------------------------------------------------------

[**[preferred-path]{lang="SV"}**]{#struct_0_13623_x1941_1011834698}[命令用来指定到固定目的地址的首选隧道。]{style="font-family:宋体"}

[**[undo preferred-path]{lang="SV"}**]{#struct_0_13623_x1941_x816064880}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13623_x1941_x1452301283}

[**[preferred-path ]{lang="EN-US"}**[{ **tunnel** ]{lang="EN-US"}*[number]{lang="EN-US"}*[ \| ]{lang="EN-US"}**[tunnel-bundle ]{lang="EN-US"}***[number]{lang="EN-US"}*[ }]{lang="EN-US"}]{#struct_0_13623_x1941_x1107182757}

[**[undo preferred-path ]{lang="EN-US"}**[{ **tunnel** ]{lang="EN-US"}*[number]{lang="EN-US"}*[ \| ]{lang="EN-US"}**[tunnel-bundle ]{lang="EN-US"}***[number]{lang="EN-US"}*[ }]{lang="EN-US"}]{#struct_0_13623_x1941_x1927110623}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13623_x1941_x1980403651}

[[未]{style="font-family:宋体"}]{#struct_0_13623_x1941_x73950837}[指定到固定目的地址的首选隧道。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13623_x1941_420382544}

[[隧道策略视图]{style="font-family:宋体"}]{#struct_0_13623_x1941_1888965762}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13623_x1941_1551088980}

[[network-admin]{lang="EN-US"}]{#struct_0_13623_x1941_1242221024}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13623_x1941_1748416689}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13623_x1941_x693008457}

[**[tunnel]{lang="SV"}**]{#struct_0_13623_x1941_49578085}[ *number*]{lang="SV"}[：配置指定的]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道或]{style="font-family:宋体"}[GRE]{lang="EN-US"}[隧道为首选隧道。]{style="font-family:宋体"}*[number]{lang="SV"}*[为]{style="font-family:宋体"}[隧道接口的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[tunnel-bundle ]{lang="EN-US"}**]{#struct_0_13623_x1941_1468207120}*[number]{lang="SV"}*[：配置指定的捆绑隧道为首选隧道。]{style="font-family:宋体"}*[number]{lang="SV"}*[为隧道捆绑接口]{style="font-family:宋体"}[的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13623_x1941_x1359496831}

[[通过本命令配置首选隧道后，]{style="font-family:宋体"}]{#struct_0_13623_x1941_x1980469187}[如果对端]{style="font-family:宋体"}[PE]{lang="SV"}[地址与隧道接口]{style="font-family:宋体"}[/]{lang="SV"}[隧道捆绑接口的目的地址相同，则]{style="font-family:宋体"}[通过该隧道]{style="font-family:宋体"}[/]{lang="EN-US"}[捆绑隧道转发到达该]{style="font-family:宋体"}[PE]{lang="SV"}[的流量。该方式为]{style="font-family:宋体"}[MPLS VPN]{lang="EN-US"}[显式指定了一条]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道、]{style="font-family:宋体"}[GRE]{lang="EN-US"}[隧道或捆绑隧道，选择的隧道是明确的、可以预期的，便于网络流量规划。推荐使用该方式配置隧道策略。]{style="font-family:宋体"}

[[需要注意]{style="font-family:宋体"}]{#struct_0_13623_x1941_369021380}[的是：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="SV" style="font-size:10.0pt;font-family:Symbol"}[如果希望隧道]{style="font-family:宋体"}]{#struct_0_13623_x1941_1757475351}[/]{lang="EN-US"}[捆绑隧道只被特定策略使用]{style="font-family:宋体"}[，]{style="font-family:宋体"}[则不要将同一隧道]{style="font-family:宋体"}[/]{lang="EN-US"}[捆绑隧道指定为多个策略下的]{style="font-family:宋体"}[首选隧道]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在同一个隧道策略下配置的多条首选隧道的目的地址相同，则选择配置的第一条首选隧道，如果第一条首选隧道不可用，则选择下一条首选隧道，以此类推。也就是说到达同一个目的地址只能存在一条首选隧道，不会在多条隧道间进行负载分担。]{style="font-family:宋体"}]{#struct_0_13623_x1941_1940381058}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个隧道策略下最多可以指定]{style="font-family:宋体"}]{#struct_0_13623_x1941_1921235089}[128]{lang="EN-US"}[个首选隧道。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13623_x1941_652006985}

[[\# ]{lang="EN-US"}]{#struct_0_13623_x1941_242560976}[配置隧道策略]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的首选隧道为接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[和]{style="font-family:宋体"}[Tunnel2]{lang="EN-US"}[对应的隧道：优先选择]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[；如果]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[不可用，则选择]{style="font-family:宋体"}[Tunnel2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13623_x1941_2096644374}

[\[Sysname\] tunnel-policy policy1]{lang="EN-US"}

[\[Sysname-tunnel-policy-policy1\] preferred-path tunnel 1]{lang="EN-US"}

[\[Sysname-tunnel-policy-policy1\] preferred-path tunnel 2]{lang="EN-US"}
:::

::: {#-1046323923 .myid}
[]{#_Toc404791030}[]{#struct_0_13623_x1941_563814109}

**隧道策略 \-- 隧道策略配置命令 \-- select-seq load-balance-number**

------------------------------------------------------------------------

[**[select-seq load-balance-number]{lang="EN-US"}**]{#struct_0_13623_x1941_x1980534723}[命令用来配置隧道的选择顺序和]{style="font-family:
宋体"}[负载分担的隧道数目。]{style="font-family:宋体"}

[**[undo select-seq]{lang="EN-US"}**]{#struct_0_13623_x1941_x135296915}[命令用来恢复缺省配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13623_x1941_826669242}

[**[select-seq ]{lang="EN-US"}**[{ **cr-lsp** \| **gre** \| **lsp** } \* **load-balance-number**]{lang="EN-US"}[ *number*]{lang="EN-US"}]{#struct_0_13623_x1941_1177376331}

[**[undo select-seq]{lang="EN-US"}**]{#struct_0_13623_x1941_2045767887}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13623_x1941_x2092568537}

[[按照]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_13623_x1941_x200770139}[隧道－]{style="font-family:宋体"}[\>GRE]{lang="EN-US"}[隧道－]{style="font-family:宋体"}[\>CR-LSP]{lang="EN-US"}[隧道的优先级顺序选择隧道，负载分担的隧道数目为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13623_x1941_1643639176}

[[隧道策略视图]{style="font-family:宋体"}]{#struct_0_13623_x1941_262626561}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13623_x1941_x1980600259}

[[network-admin]{lang="EN-US"}]{#struct_0_13623_x1941_x559221577}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13623_x1941_351567174}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13623_x1941_1964935245}

[**[cr-lsp]{lang="EN-US"}**]{#struct_0_13623_x1941_x187459152}[：]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[隧道。]{style="font-family:宋体"}

[**[gre]{lang="EN-US"}**]{#struct_0_13623_x1941_x889514832}[：]{style="font-family:宋体"}[GRE]{lang="EN-US"}[隧道。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[lsp]{lang="EN-US"}**]{#struct_0_13623_x1941_x38856906}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[隧道。]{style="font-family:宋体"}

[**[load-balance-number]{lang="EN-US"}***[ number]{lang="EN-US"}*]{#struct_0_13623_x1941_1136530576}[：指定负载分担的隧道条数，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13623_x1941_x123792269}

[[在配置隧道选择顺序时，隧道类型越靠近关键字]{style="font-family:宋体"}**[select-seq]{lang="EN-US"}**]{#struct_0_13623_x1941_771484335}[，其优先级越高。并且，只有本命令中列举的隧道类型可以被使用。例如：配置了]{style="font-family:宋体"}**[select-seq lsp gre load-balance-number 3]{lang="EN-US"}**[命令，则优先选择]{style="font-family:宋体"}[LSP]{lang="EN-US"}[；在没有]{style="font-family:宋体"}[LSP]{lang="EN-US"}[或]{style="font-family:宋体"}[LSP]{lang="EN-US"}[不足]{style="font-family:宋体"}[3]{lang="EN-US"}[条的情况下，选用]{style="font-family:宋体"}[GRE]{lang="EN-US"}[隧道；不会选用]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[隧道。]{style="font-family:宋体"}

[[通过本命令配置隧道策略时，选择的隧道具有随机性，不便于网络流量规划。不推荐使用该方式配置隧道策略。]{style="font-family:宋体"}]{#struct_0_13623_x1941_x1980665795}

[[需要注意的是，如果同时配置了本命令和]{style="font-family:宋体"}**[preferred-path]{lang="EN-US"}**]{#struct_0_13623_x1941_816244876}[命令，则优先选择]{style="font-family:宋体"}**[preferred-path]{lang="EN-US"}**[命令指定的隧道，即：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果对端]{lang="EN-US" style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_13623_x1941_253872147}[地址与某条首选隧道的目的地址相同，则采用该隧道]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[捆绑隧道]{style="font-family:宋体"}[转发流量，不会再根据]{lang="EN-US" style="font-family:宋体"}**[select-seq load-balance-number]{lang="EN-US"}**[命令指定的隧道选择顺序和负载分担数目选择隧道。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不存在隧道目的地址与对端]{lang="EN-US" style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_13623_x1941_x2110024730}[地址相同的首选隧道，则根据]{lang="EN-US" style="font-family:宋体"}**[select-seq load-balance-number]{lang="EN-US"}**[命令指定的隧道选择顺序和负载分担数目选择隧道。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13623_x1941_687511121}

[[\# ]{lang="EN-US"}]{#struct_0_13623_x1941_x614686075}[配置隧道策略]{style="font-family:宋体"}[policy1]{lang="EN-US"}[为只能使用]{style="font-family:宋体"}[GRE]{lang="EN-US"}[隧道，负载分担条数为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13623_x1941_2004728855}

[\[Sysname\] tunnel-policy policy1]{lang="EN-US"}

[\[Sysname-tunnel-policy-policy1\] select-seq gre load-balance-number 2]{lang="EN-US"}
:::

::: {#95151371 .myid}
[]{#_Toc404791031}[]{#struct_0_13623_x1941_x1187136475}

**隧道策略 \-- 隧道策略配置命令 \-- tunnel-policy**

------------------------------------------------------------------------

[**[tunnel-policy]{lang="EN-US"}**]{#struct_0_13623_x1941_x1925245971}[命令用来创建隧道策略，并进入隧道策略视图。]{style="font-family:宋体"}

[**[undo tunnel-policy]{lang="EN-US"}**]{#struct_0_13623_x1941_x1980731331}[命令用来删除已创建的隧道策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13623_x1941_362049959}

[**[tunnel-policy]{lang="EN-US"}***[ tunnel-policy-name]{lang="EN-US"}*]{#struct_0_13623_x1941_x910146227}

[**[undo tunnel-policy]{lang="EN-US"}***[ tunnel-policy-name]{lang="EN-US"}*]{#struct_0_13623_x1941_1817754446}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13623_x1941_105371444}

[[设备上不存在任何隧道策略。]{style="font-family:宋体"}]{#struct_0_13623_x1941_x316255672}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13623_x1941_1955213253}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13623_x1941_x1708144763}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13623_x1941_1356139438}

[[network-admin]{lang="EN-US"}]{#struct_0_13623_x1941_x973449938}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13623_x1941_x1980796867}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13623_x1941_983259270}

[*[tunnel-policy-name]{lang="EN-US"}*]{#struct_0_13623_x1941_86186966}[：隧道策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13623_x1941_1759829861}

[[\# ]{lang="EN-US"}]{#struct_0_13623_x1941_893736011}[创建名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的隧道策略，并进入隧道策略视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13623_x1941_9383684}

[\[Sysname\] tunnel-policy policy1]{lang="EN-US"}

[\[Sysname-tunnel-policy-policy1\]]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}
:::
