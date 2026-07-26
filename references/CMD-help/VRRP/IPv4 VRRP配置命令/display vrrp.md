::: {#1121431443 .myid}
[]{#_Toc404795926}[]{#struct_0_18718_x1832_x468903680}[]{#_Toc211671357}[]{#_Toc99954750}[]{#_Toc91670449}

**VRRP \-- IPv4 VRRP配置命令 \-- display vrrp**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **vrrp**]{lang="EN-US"}]{#struct_0_18718_x1832_x1826783358}[命令用来显示]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组的状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x691568006}

[**[display]{lang="EN-US"}**[ **vrrp** \[ **interface** *interface-type interface-number* \[ **vrid** *virtual-router-id* \] \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_18718_x1832_x969572051}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x2053764512}

[[任意视图]{style="font-family:宋体"}]{#struct_0_18718_x1832_x945353730}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18718_x1832_865049685}

[[network-admin]{lang="EN-US"}]{#struct_0_18718_x1832_1772545238}

[[network-operator]{lang="EN-US"}]{#struct_0_18718_x1832_x487747019}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18718_x1832_x1379556641}

[[mdc-operator]{lang="EN-US"}]{#struct_0_18718_x1832_1027710546}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1949053827}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_18718_x1832_156749629}[：显示指定接口的]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组状态信息。其中，]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}[为接口类型和接口编号。]{style="font-family:宋体"}

[**[vrid]{lang="EN-US"}***[ virtual-router-id]{lang="EN-US"}*]{#struct_0_18718_x1832_x1511846158}[：显示指定]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组的状态信息。其中，]{style="font-family:宋体"}*[virtual-router-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_18718_x1832_x479377148}[：显示]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组状态的详细信息。如果不指定本参数，则显示]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组状态的简要信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18718_x1832_234113321}

[[如果不指定接口名和备份组号，则显示该路由器上所有]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_1772479702}[备份组的状态信息；如果只指定接口名，不指定备份组号，则显示该接口上的所有]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组的状态信息；如果同时指定接口名和备份组号，则显示该接口上指定]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组的状态信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1604576497}

[]{#_Toc99954751}[]{#_Toc34483419}[]{#_Toc33425588}[]{#_Toc31785777}[]{#_Toc99954527}[[\# VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x1739066425}[工作在标准协议模式时，显示全部]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display vrrp]{lang="EN-US"}]{#struct_0_18718_x1832_1788347578}

[IPv4 Virtual Router Information:]{lang="EN-US"}

[ Running Mode      : Standard]{lang="EN-US"}

[ Total number of virtual routers : 1]{lang="EN-US"}

[ Interface          VRID  State        Running Adver   Auth     Virtual]{lang="EN-US"}

[                                       Pri     Timer   Type        IP ]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ GE1/0/1            1     Master       150     100     Simple   1.1.1.1]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display vrrp]{lang="EN-US"}]{#struct_0_18718_x1832_x360196762}[命令显示信息描述表（标准协议模式）]{style="font-family:黑体"}

[]{#table_struct_0_x1837178345}[[字段]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1381573539}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_18718_x1832_1772414166}

[[Running Mode]{lang="EN-US"}]{#struct_0_18718_x1832_x95615252}

[[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x1079244594}[的工作模式，取值为]{style="font-family:宋体"}[Standard]{lang="EN-US"}[（标准协议模式）]{style="font-family:宋体"}

[[Total number of virtual routers]{lang="EN-US"}]{#struct_0_18718_x1832_1196164584}

[[备份组的数目]{style="font-family:宋体"}]{#struct_0_18718_x1832_741223154}

[[Interface]{lang="EN-US"}]{#struct_0_18718_x1832_x419399994}

[[备份组所在接口名]{style="font-family:宋体"}]{#struct_0_18718_x1832_x542571902}

[[VRID]{lang="EN-US"}]{#struct_0_18718_x1832_1772348630}

[[虚拟路由器号（即备份组号）]{style="font-family:宋体"}]{#struct_0_18718_x1832_x1205890994}

[[State]{lang="EN-US"}]{#struct_0_18718_x1832_1355569874}

[[当前路由器在备份组中的状态，取值为]{style="font-family:宋体"}[Master]{lang="EN-US"}]{#struct_0_18718_x1832_1558467750}[，]{style="font-family:宋体"}[Backup]{lang="EN-US"}[，]{style="font-family:宋体"}[Initialize]{lang="EN-US"}[或]{style="font-family:宋体"}[Inactive]{lang="EN-US"}

[[Running Pri]{lang="EN-US"}]{#struct_0_18718_x1832_382334028}

[[路由器的运行优先级，即路由器当前的优先级。配置监视指定]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_18718_x1832_331623173}[项后，路由器的优先级会根据]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的状态改变]{style="font-family:宋体"}

[[Adver Timer]{lang="EN-US"}]{#struct_0_18718_x1832_1772807382}

[[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x1273005299}[通告报文发送时间间隔，单位为厘秒]{style="font-family:宋体"}

[[Auth Type]{lang="EN-US"}]{#struct_0_18718_x1832_1210642760}

[[认证类型，包括：]{style="font-family:宋体"}]{#struct_0_18718_x1832_635968423}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[None]{lang="EN-US"}]{#struct_0_18718_x1832_63058937}[：无认证]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Simple]{lang="EN-US"}]{#struct_0_18718_x1832_1772741846}[：简单字符认证]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MD5]{lang="EN-US"}]{#struct_0_18718_x1832_x430194682}[：]{lang="EN-US" style="font-family:宋体"}[MD5]{lang="EN-US"}[认证]{lang="EN-US" style="font-family:宋体"}

[[Virtual IP]{lang="EN-US"}]{#struct_0_18718_x1832_993857436}

[[备份组的虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_18718_x1832_1790664750}[地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_1877748435}[工作在标准协议模式时，显示全部]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display vrrp verbose]{lang="EN-US"}]{#struct_0_18718_x1832_1772283095}

[IPv4 Virtual Router Information:]{lang="EN-US"}

[ Running Mode      : Standard]{lang="EN-US"}

[ Total number of virtual routers : 2]{lang="EN-US"}

[   Interface GigabitEthernet1/0/1]{lang="EN-US"}

[     VRID           : 1                    Adver Timer  : 100]{lang="EN-US"}

[     Admin Status   : Up                   State        : Master]{lang="EN-US"}

[     Config Pri     : 150                  Running Pri  : 150]{lang="EN-US"}

[     Preempt Mode   : Yes                  Delay Time   : 5]{lang="EN-US"}

[     Auth Type      : Simple               Key          : \*\*\*\*\*\*]{lang="EN-US"}

[     Virtual IP     : 1.1.1.1]{lang="EN-US"}

[     ]{lang="EN-US"}[Virtual MAC    : 0000-5e00-0101]{lang="PT-BR"}

[     Master IP      : 1.1.1.2]{lang="PT-BR"}

[   ]{lang="PT-BR"}[VRRP Track Information:]{lang="EN-US"}

[     Track Object   : 1                    State : Positive   Pri Reduced : 50]{lang="EN-US"}

[   Interface GigabitEthernet1/0/1]{lang="EN-US"}

[     VRID           : 11                   Adver Timer  : 100]{lang="EN-US"}

[     Admin Status   : Up                   State        : Backup]{lang="EN-US"}

[     Config Pri     : 80                   Running Pri  : 80]{lang="EN-US"}

[     Preempt Mode   : Yes                  Delay Time   : 0]{lang="EN-US"}

[     Become Master  : 2370ms left]{lang="EN-US"}

[     Auth Type      : None]{lang="EN-US"}

[     Virtual IP     : 1.1.1.11]{lang="EN-US"}

[     ]{lang="EN-US"}[Virtual MAC    : 0000-5e00-010b]{lang="PT-BR"}

[     Master IP      : 1.1.1.12]{lang="PT-BR"}

[[表1-2 ]{lang="EN-US"}[display vrrp verbose]{lang="EN-US"}]{#struct_0_18718_x1832_x2007651876}[命令显示信息描述表（标准协议模式）]{style="font-family:黑体"}

[]{#table_struct_0_x1842122741}[[字段]{style="font-family:黑体"}]{#struct_0_18718_x1832_1772217559}

[[描述]{style="font-family:黑体"}]{#struct_0_18718_x1832_1868921940}

[[Running Mode]{lang="EN-US"}]{#struct_0_18718_x1832_x1492924604}

[[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_33741045}[的工作模式，取值为]{style="font-family:宋体"}[Standard]{lang="EN-US"}[（标准协议模式）]{style="font-family:宋体"}

[[Total number of virtual routers]{lang="EN-US"}]{#struct_0_18718_x1832_1167914869}

[[备份组的数目]{style="font-family:宋体"}]{#struct_0_18718_x1832_x461822701}

[[Interface]{lang="EN-US"}]{#struct_0_18718_x1832_1772152023}

[[备份组所在接口名]{style="font-family:宋体"}]{#struct_0_18718_x1832_691019295}

[[VRID]{lang="EN-US"}]{#struct_0_18718_x1832_708967948}

[[虚拟路由器号（即备份组号）]{style="font-family:宋体"}]{#struct_0_18718_x1832_1493249153}

[[Adver Timer]{lang="EN-US"}]{#struct_0_18718_x1832_x1336262785}

[[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_279726176}[通告报文发送时间间隔，单位为厘秒]{style="font-family:宋体"}

[[Admin Status]{lang="EN-US"}]{#struct_0_18718_x1832_1772086487}

[[管理状态，包括]{style="font-family:宋体"}[Up]{lang="EN-US"}]{#struct_0_18718_x1832_x2012680032}[和]{style="font-family:宋体"}[Down]{lang="EN-US"}[两种状态]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_18718_x1832_x182532353}

[[当前路由器在备份组中的状态，取值为]{style="font-family:宋体"}[Master]{lang="EN-US"}]{#struct_0_18718_x1832_x672244838}[，]{style="font-family:宋体"}[Backup]{lang="EN-US"}[，]{style="font-family:宋体"}[Initialize]{lang="EN-US"}[或]{style="font-family:宋体"}[Inactive]{lang="EN-US"}

[[Config Pri]{lang="EN-US"}]{#struct_0_18718_x1832_555471943}

[[路由器的配置优先级，即通过]{style="font-family:宋体"}**[vrrp vrid priority]{lang="EN-US"}**]{#struct_0_18718_x1832_x1379121939}[命令指定的路由器优先级]{style="font-family:宋体"}

[[Running Pri]{lang="EN-US"}]{#struct_0_18718_x1832_1772545239}

[[路由器的运行优先级，即路由器当前的优先级，配置监视指定]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_18718_x1832_x487681483}[项后，路由器的优先级会根据]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的状态改变]{style="font-family:宋体"}

[[Preempt Mode]{lang="EN-US"}]{#struct_0_18718_x1832_956086735}

[[抢占模式，取值包括：]{style="font-family:宋体"}]{#struct_0_18718_x1832_2000790173}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Yes]{lang="EN-US"}]{#struct_0_18718_x1832_1774065487}[：路由器工作在抢占模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No]{lang="EN-US"}]{#struct_0_18718_x1832_150901455}[：路由器工作在非抢占模式]{style="font-family:宋体"}

[[Delay Time]{lang="EN-US"}]{#struct_0_18718_x1832_1772479703}

[[抢占延迟时间，单位为厘秒]{style="font-family:宋体"}]{#struct_0_18718_x1832_x1604642033}

[[Become Master]{lang="EN-US"}]{#struct_0_18718_x1832_1835896016}

[[切换到]{style="font-family:宋体"}[Master]{lang="EN-US"}]{#struct_0_18718_x1832_1151937244}[状态需要等待的时间，单位为毫秒，只有处于]{style="font-family:宋体"}[Backup]{lang="EN-US"}[状态时才会显示此信息]{style="font-family:宋体"}

[[Auth Type]{lang="EN-US"}]{#struct_0_18718_x1832_x773655631}

[[认证类型，包括：]{style="font-family:宋体"}]{#struct_0_18718_x1832_1772414167}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[None]{lang="EN-US"}]{#struct_0_18718_x1832_x95680788}[：无认证]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Simple]{lang="EN-US"}]{#struct_0_18718_x1832_2129314520}[：简单字符认证]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MD5]{lang="EN-US"}]{#struct_0_18718_x1832_7558226}[：]{lang="EN-US" style="font-family:宋体"}[MD5]{lang="EN-US"}[认证]{lang="EN-US" style="font-family:宋体"}

[[Key]{lang="EN-US"}]{#struct_0_18718_x1832_x1074177814}

[[认证字，无认证时不显示此信息]{style="font-family:宋体"}]{#struct_0_18718_x1832_1772348631}

[[Virtual IP]{lang="EN-US"}]{#struct_0_18718_x1832_x1205825458}

[[备份组的虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_18718_x1832_x1361635252}[地址]{style="font-family:宋体"}

[[Virtual MAC]{lang="EN-US"}]{#struct_0_18718_x1832_x979931265}

[[备份组虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_18718_x1832_1772807383}[地址对应的虚拟]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。只在路由器为]{style="font-family:宋体"}[Master]{lang="EN-US"}[状态时，才会显示此信息]{style="font-family:宋体"}

[[Master IP]{lang="EN-US"}]{#struct_0_18718_x1832_x1272939763}

[[处于]{style="font-family:宋体"}[Master]{lang="EN-US"}]{#struct_0_18718_x1832_38142491}[状态的路由器所对应接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[VRRP Track Information]{lang="EN-US"}]{#struct_0_18718_x1832_872555873}

[[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x995560962}[备份组监视的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项信息。执行]{style="font-family:宋体"}**[vrrp vrid track]{lang="EN-US"}**[命令后，才会显示此信息]{style="font-family:宋体"}

[[Track Object]{lang="EN-US"}]{#struct_0_18718_x1832_1772741847}

[[监视的]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_18718_x1832_x430129146}[项]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_18718_x1832_152244809}

[[Track]{lang="EN-US"}]{#struct_0_18718_x1832_x693512132}[项的状态，]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的状态可包括]{style="font-family:宋体"}[Negative]{lang="EN-US"}[、]{style="font-family:宋体"}[Positive]{lang="EN-US"}[和]{style="font-family:宋体"}[NotReady]{lang="EN-US"}

[[Pri Reduced]{lang="EN-US"}]{#struct_0_18718_x1832_x956600257}

[[监视的]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_18718_x1832_1665397454}[项状态为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，优先级降低的数额]{style="font-family:宋体"}

[[Switchover]{lang="EN-US"}]{#struct_0_18718_x1832_x2126543826}

[[快速切换。显示此信息时表示当监视的]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_18718_x1832_x956665793}[项变为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[状态时，]{style="font-family:宋体"}[Backup]{lang="EN-US"}[路由器会马上抢占成为]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x290083893}[工作在负载均衡模式时，显示全部]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display vrrp]{lang="EN-US"}]{#struct_0_18718_x1832_2026686311}

[IPv4 Virtual Router Information:]{lang="EN-US"}

[ Running Mode      : Load Balance]{lang="EN-US"}

[ Total number of virtual routers : 1]{lang="EN-US"}

[ Interface          VRID  State        Running Address             Active]{lang="EN-US"}

[                                       Pri]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ GE1/0/1            1     Master       150     1.1.1.1             Local]{lang="EN-US"}

[ \-\-\-\--              VF 1  Active       255     000f-e2ff-0011      Local]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display vrrp]{lang="EN-US"}]{#struct_0_18718_x1832_1516387948}[命令显示信息描述表（负载均衡模式）]{style="font-family:黑体"}

[]{#table_struct_0_x1820276865}[[字段]{style="font-family:黑体"}]{#struct_0_18718_x1832_285702630}

[[描述]{style="font-family:黑体"}]{#struct_0_18718_x1832_361061614}

[[Running Mode]{lang="EN-US"}]{#struct_0_18718_x1832_x956731329}

[[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_1281785363}[的工作模式，取值为]{style="font-family:宋体"}[Load Balance]{lang="EN-US"}[（负载均衡模式）]{style="font-family:宋体"}

[[Total number of virtual routers]{lang="EN-US"}]{#struct_0_18718_x1832_1436007966}

[[备份组的数目]{style="font-family:宋体"}]{#struct_0_18718_x1832_x2088716464}

[[Interface]{lang="EN-US"}]{#struct_0_18718_x1832_x131204254}

[[备份组所在接口名]{style="font-family:宋体"}]{#struct_0_18718_x1832_x892596352}

[[VRID]{lang="EN-US"}]{#struct_0_18718_x1832_x956796865}

[[虚拟路由器号（即备份组号）]{style="font-family:宋体"}*[number]{lang="EN-US"}*]{#struct_0_18718_x1832_579614472}[或虚拟转发器编号]{style="font-family:宋体"}[VF *number*]{lang="EN-US"}

[[State]{lang="EN-US"}]{#struct_0_18718_x1832_687610359}

[[对于虚拟备份组（]{style="font-family:宋体"}[VRID]{lang="EN-US"}]{#struct_0_18718_x1832_x1544254525}[为]{style="font-family:宋体"}*[number]{lang="EN-US"}*[），该字段表示当前路由器在备份组中的状态，取值为]{style="font-family:宋体"}[Master]{lang="EN-US"}[，]{style="font-family:宋体"}[Backup]{lang="EN-US"}[，]{style="font-family:宋体"}[Initialize]{lang="EN-US"}[或]{style="font-family:宋体"}[Inactive]{lang="EN-US"}

[[对于虚拟转发器（]{style="font-family:宋体"}[VRID]{lang="EN-US"}]{#struct_0_18718_x1832_1005157487}[为]{style="font-family:宋体"}[VF *number*]{lang="EN-US"}[），该字段表示虚拟转发器的状态，取值为]{style="font-family:宋体"}[Active]{lang="EN-US"}[、]{style="font-family:宋体"}[Listening]{lang="EN-US"}[或]{style="font-family:宋体"}[Initialize]{lang="EN-US"}

[[Running Pri]{lang="EN-US"}]{#struct_0_18718_x1832_1125286292}

[[对于虚拟备份组（]{style="font-family:宋体"}[VRID]{lang="EN-US"}]{#struct_0_18718_x1832_x956338113}[为]{style="font-family:宋体"}*[number]{lang="EN-US"}*[），该字段表示路由器的运行优先级，即路由器当前的优先级，配置监视指定]{style="font-family:宋体"}[Track]{lang="EN-US"}[项后，路由器的优先级会根据]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的状态改变]{style="font-family:宋体"}

[[对于虚拟转发器（]{style="font-family:宋体"}[VRID]{lang="EN-US"}]{#struct_0_18718_x1832_x311060735}[为]{style="font-family:宋体"}[VF *number*]{lang="EN-US"}[），该字段表示虚拟转发器的运行优先级，配置监视指定]{style="font-family:宋体"}[Track]{lang="EN-US"}[项后，虚拟转发器的优先级会根据]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的状态改变]{style="font-family:宋体"}

[[Address]{lang="EN-US"}]{#struct_0_18718_x1832_x1526345286}

[[对于虚拟备份组（]{style="font-family:宋体"}[VRID]{lang="EN-US"}]{#struct_0_18718_x1832_263645516}[为]{style="font-family:宋体"}*[number]{lang="EN-US"}*[），该字段表示备份组的虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[对于虚拟转发器（]{style="font-family:宋体"}[VRID]{lang="EN-US"}]{#struct_0_18718_x1832_x1856847336}[为]{style="font-family:宋体"}[VF *number*]{lang="EN-US"}[），该字段表示虚拟转发器的虚拟]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Active]{lang="EN-US"}]{#struct_0_18718_x1832_x956403649}

[[对于虚拟备份组（]{style="font-family:宋体"}[VRID]{lang="EN-US"}]{#struct_0_18718_x1832_x1461218116}[为]{style="font-family:宋体"}*[number]{lang="EN-US"}*[），该字段表示]{style="font-family:宋体"}[Master]{lang="EN-US"}[的接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，当前路由器为]{style="font-family:宋体"}[Master]{lang="EN-US"}[时，显示为]{style="font-family:宋体"}[local]{lang="EN-US"}

[[对于虚拟转发器（]{style="font-family:宋体"}[VRID]{lang="EN-US"}]{#struct_0_18718_x1832_x2008201207}[为]{style="font-family:宋体"}[VF *number*]{lang="EN-US"}[），该字段表示]{style="font-family:宋体"}[AVF]{lang="EN-US"}[的接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，当前虚拟转发器为]{style="font-family:宋体"}[AVF]{lang="EN-US"}[时，显示为]{style="font-family:宋体"}[local]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x40222392}[工作在负载均衡模式时，显示全部]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display vrrp verbose]{lang="EN-US"}]{#struct_0_18718_x1832_x956075969}

[IPv4 Virtual Router Information:]{lang="EN-US"}

[ Running Mode      : Load Balance]{lang="EN-US"}

[ Total number of virtual routers : 2]{lang="EN-US"}

[   Interface GigabitEthernet1/0/1]{lang="EN-US"}

[     VRID           : 1                    Adver Timer  : 100]{lang="EN-US"}

[     Admin Status   : Up                   State        : Master]{lang="EN-US"}

[     Config Pri     : 150                  Running Pri  : 150]{lang="EN-US"}

[     Preempt Mode   : Yes                  Delay Time   : 5]{lang="EN-US"}

[     Auth Type      : None]{lang="EN-US"}

[     Virtual IP     : 10.1.1.1]{lang="EN-US"}

[                      10.1.1.2]{lang="EN-US"}

[                      10.1.1.3]{lang="EN-US"}

[     Member IP List : 10.1.1.10 (Local, Master)]{lang="EN-US"}

[                      10.1.1.20 (Backup)]{lang="EN-US"}

[   VRRP Track Information:]{lang="EN-US"}

[     Track Object   : 1                    State : Positive   Pri Reduced : 50]{lang="EN-US"}

[   Forwarder Information: 2 Forwarders 1 Active]{lang="EN-US"}

[     Config Weight  : 255]{lang="EN-US"}

[     Running Weight : 255]{lang="EN-US"}

[    Forwarder 01]{lang="EN-US"}

[     State          : Active]{lang="EN-US"}

[     Virtual MAC    : 000f-e2ff-0011 (Owner)]{lang="EN-US"}

[     Owner ID       : 0000-5e01-1101]{lang="EN-US"}

[     Priority       : 255]{lang="EN-US"}

[     Active         : local]{lang="EN-US"}

[    Forwarder 02]{lang="EN-US"}

[     State          : Listening]{lang="EN-US"}

[     Virtual MAC    : 000f-e2ff-0012 (Learnt)]{lang="EN-US"}

[     Owner ID       : 0000-5e01-1103]{lang="EN-US"}

[     Priority       : 127]{lang="EN-US"}

[     Active         : 10.1.1.20]{lang="EN-US"}

[   Forwarder Weight Track Information:]{lang="EN-US"}

[     Track Object   : 1          State : Positive   Weight Reduced : 250]{lang="EN-US"}

[   Interface GigabitEthernet1/0/1]{lang="EN-US"}

[     VRID           : 11                   Adver Timer  : 100]{lang="EN-US"}

[     Admin Status   : Up                   State        : Backup]{lang="EN-US"}

[     Config Pri     : 80                   Running Pri  : 80]{lang="EN-US"}

[     Preempt Mode   : Yes                  Delay Time   : 0]{lang="EN-US"}

[     Become Master  : 2370ms left]{lang="EN-US"}

[     Auth Type      : None]{lang="EN-US"}

[     Virtual IP     : 10.1.1.11]{lang="EN-US"}

[                    : 10.1.1.12]{lang="EN-US"}

[                    : 10.1.1.13]{lang="EN-US"}

[     Member IP List : 10.1.1.10 (Local, Backup)]{lang="EN-US"}

[                      10.1.1.15 (Master)]{lang="EN-US"}

[   Forwarder Information: 2 Forwarders 1 Active]{lang="EN-US"}

[     Config Weight  : 255]{lang="EN-US"}

[     Running Weight : 255]{lang="EN-US"}

[    Forwarder 01]{lang="EN-US"}

[     State          : Active]{lang="EN-US"}

[     Virtual MAC    : 000f-e2ff-40b1 (Learnt)]{lang="EN-US"}

[     Owner ID       : 0000-5e01-1103]{lang="EN-US"}

[     Priority       : 127]{lang="EN-US"}

[     Active         : 10.1.1.15]{lang="EN-US"}

[    Forwarder 02]{lang="EN-US"}

[     State          : Listening]{lang="EN-US"}

[     Virtual MAC    : 000f-e2ff-40b2 (Owner)]{lang="EN-US"}

[     Owner ID       : 0000-5e01-1101]{lang="EN-US"}

[     Priority       : 255]{lang="EN-US"}

[     Active         : local]{lang="EN-US"}

[]{#struct_0_18718_x1832_1331866268}[]{#_Hlt13643166}[表1-4 ]{lang="EN-US"}[display vrrp verbose]{lang="EN-US"}[命令显示信息描述表（负载均衡模式）]{style="font-family:黑体"}

[]{#table_struct_0_x1823430137}[[字段]{style="font-family:黑体"}]{#struct_0_18718_x1832_131017443}

[[描述]{style="font-family:黑体"}]{#struct_0_18718_x1832_1965938545}

[[Running Mode]{lang="EN-US"}]{#struct_0_18718_x1832_x1710838319}

[[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x1700403275}[的工作模式，取值为]{style="font-family:宋体"}[Load Balance]{lang="EN-US"}[（负载均衡模式）]{style="font-family:宋体"}

[[Total number of virtual routers]{lang="EN-US"}]{#struct_0_18718_x1832_x1952090979}

[[备份组的数目]{style="font-family:宋体"}]{#struct_0_18718_x1832_x956141505}

[[Interface]{lang="EN-US"}]{#struct_0_18718_x1832_1650556267}

[[备份组所在接口名]{style="font-family:宋体"}]{#struct_0_18718_x1832_196700361}

[[VRID]{lang="EN-US"}]{#struct_0_18718_x1832_x1066552932}

[[虚拟路由器号（即备份组号）]{style="font-family:宋体"}]{#struct_0_18718_x1832_x508135192}

[[Adver Timer]{lang="EN-US"}]{#struct_0_18718_x1832_x838256676}

[[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x956600256}[通告报文发送时间间隔，单位为厘秒]{style="font-family:宋体"}

[[Admin Status]{lang="EN-US"}]{#struct_0_18718_x1832_1665331918}

[[管理状态，包括]{style="font-family:宋体"}[Up]{lang="EN-US"}]{#struct_0_18718_x1832_x1638414200}[和]{style="font-family:宋体"}[Down]{lang="EN-US"}[两种状态]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_18718_x1832_x47646218}

[[当前路由器在备份组中的状态，取值为]{style="font-family:宋体"}[Master]{lang="EN-US"}]{#struct_0_18718_x1832_x362943555}[，]{style="font-family:宋体"}[Backup]{lang="EN-US"}[，]{style="font-family:宋体"}[Initialize]{lang="EN-US"}[或]{style="font-family:宋体"}[Inactive]{lang="EN-US"}

[[Config Pri]{lang="EN-US"}]{#struct_0_18718_x1832_x956665792}

[[路由器的配置优先级，即通过]{style="font-family:宋体"}**[vrrp vrid priority]{lang="EN-US"}**]{#struct_0_18718_x1832_x290149429}[命令指定的路由器优先级]{style="font-family:宋体"}

[[Running Pri]{lang="EN-US"}]{#struct_0_18718_x1832_x687993811}

[[路由器的运行优先级，即路由器当前的优先级，配置监视指定]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_18718_x1832_1951191218}[项后，路由器的优先级会根据]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的状态改变]{style="font-family:宋体"}

[[Preempt Mode]{lang="EN-US"}]{#struct_0_18718_x1832_x1064193960}

[[抢占模式，取值包括：]{style="font-family:宋体"}]{#struct_0_18718_x1832_x956731328}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Yes]{lang="EN-US"}]{#struct_0_18718_x1832_1281850899}[：路由器工作在抢占模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No]{lang="EN-US"}]{#struct_0_18718_x1832_1110603377}[：路由器工作在非抢占模式]{style="font-family:宋体"}

[[Delay Time]{lang="EN-US"}]{#struct_0_18718_x1832_x1386436853}

[[抢占延迟时间，单位为厘秒]{style="font-family:宋体"}]{#struct_0_18718_x1832_x87336572}

[[Become Master]{lang="EN-US"}]{#struct_0_18718_x1832_x956796864}

[[切换到]{style="font-family:宋体"}[Master]{lang="EN-US"}]{#struct_0_18718_x1832_579680008}[状态需要等待的时间，单位为毫秒，只有处于]{style="font-family:宋体"}[Backup]{lang="EN-US"}[状态时才会显示此信息]{style="font-family:宋体"}

[[Auth Type]{lang="EN-US"}]{#struct_0_18718_x1832_x820033992}

[[认证类型，包括：]{style="font-family:宋体"}]{#struct_0_18718_x1832_75587132}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[None]{lang="EN-US"}]{#struct_0_18718_x1832_x956338112}[：无认证]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Simple]{lang="EN-US"}]{#struct_0_18718_x1832_x310995199}[：简单字符认证]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MD5]{lang="EN-US"}]{#struct_0_18718_x1832_x1975766820}[：]{lang="EN-US" style="font-family:宋体"}[MD5]{lang="EN-US"}[认证]{lang="EN-US" style="font-family:宋体"}

[[Key]{lang="EN-US"}]{#struct_0_18718_x1832_726865648}

[[认证字，无认证时不显示此信息]{style="font-family:宋体"}]{#struct_0_18718_x1832_x956403648}

[[Virtual IP]{lang="EN-US"}]{#struct_0_18718_x1832_x1461283652}

[[备份组的虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_18718_x1832_x1075101485}[地址列表]{style="font-family:宋体"}

[[Member IP List]{lang="EN-US"}]{#struct_0_18718_x1832_x573917886}

[[备份组中成员设备的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_18718_x1832_x956469184}[地址列表：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Local]{lang="EN-US"}]{#struct_0_18718_x1832_1244799694}[：表示本地设备的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Master]{lang="EN-US"}]{#struct_0_18718_x1832_x1563861791}[：表示处于]{lang="EN-US" style="font-family:宋体"}[Master]{lang="EN-US"}[状态的成员设备的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backup]{lang="EN-US"}]{#struct_0_18718_x1832_x316697506}[：表示处于]{style="font-family:宋体"}[Backup]{lang="EN-US"}[状态的成员设备的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[VRRP Track Information]{lang="EN-US"}]{#struct_0_18718_x1832_x956534720}

[[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x1845682180}[备份组监视的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项信息，执行]{style="font-family:宋体"}**[vrrp vrid track]{lang="EN-US"}**[命令后，才会显示此信息]{style="font-family:宋体"}

[[Track Object]{lang="EN-US"}]{#struct_0_18718_x1832_x125379259}

[[监视的]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_18718_x1832_x555738513}[项]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_18718_x1832_x956075968}

[[Track]{lang="EN-US"}]{#struct_0_18718_x1832_1331931804}[项的状态，]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的状态包括]{style="font-family:宋体"}[Negative]{lang="EN-US"}[、]{style="font-family:宋体"}[Positive]{lang="EN-US"}[和]{style="font-family:宋体"}[NotReady]{lang="EN-US"}

[[Pri Reduced]{lang="EN-US"}]{#struct_0_18718_x1832_933470041}

[[监视的]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_18718_x1832_x956141504}[项状态为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，优先级降低的数额，执行]{style="font-family:宋体"}**[vrrp vrid track]{lang="EN-US"}**[命令后，才会显示此信息]{style="font-family:宋体"}

[[Switchover]{lang="EN-US"}]{#struct_0_18718_x1832_1650490731}

[[快速切换，显示此信息时表示当监视的]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_18718_x1832_940123279}[项变为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[状态时，]{style="font-family:宋体"}[Backup]{lang="EN-US"}[路由器会马上抢占成为]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器]{style="font-family:宋体"}

[[Forwarder Information: 2 Forwarders 1 Active]{lang="EN-US"}]{#struct_0_18718_x1832_358963333}

[[虚拟转发器信息：路由器的虚拟转发器数目为]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_18718_x1832_x956600259}[，处于]{style="font-family:宋体"}[Active]{lang="EN-US"}[状态的虚拟转发器数目为]{style="font-family:宋体"}[1]{lang="EN-US"}

[[Config Weight]{lang="EN-US"}]{#struct_0_18718_x1832_1665790670}

[[虚拟转发器的配置权重，取值为]{style="font-family:宋体"}[255]{lang="EN-US"}]{#struct_0_18718_x1832_628708195}

[[Running Weight]{lang="EN-US"}]{#struct_0_18718_x1832_x956665795}

[[虚拟转发器的运行权重，即虚拟转发器当前的权重，配置监视指定]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_18718_x1832_x289952821}[项后，虚拟转发器的权重会根据]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的状态改变]{style="font-family:宋体"}

[[Forwarder 01]{lang="EN-US"}]{#struct_0_18718_x1832_112417815}

[[虚拟转发器]{style="font-family:宋体"}[01]{lang="EN-US"}]{#struct_0_18718_x1832_x2111711074}[的信息]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_18718_x1832_x956731331}

[[虚拟转发器的状态，取值为]{style="font-family:宋体"}[Active]{lang="EN-US"}]{#struct_0_18718_x1832_1281261076}[、]{style="font-family:宋体"}[Listening]{lang="EN-US"}[或]{style="font-family:宋体"}[Initialize]{lang="EN-US"}

[[Virtual MAC]{lang="EN-US"}]{#struct_0_18718_x1832_1079241808}

[[虚拟转发器的虚拟]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_18718_x1832_x956796867}[地址]{style="font-family:宋体"}

[[Owner ID]{lang="EN-US"}]{#struct_0_18718_x1832_579745544}

[[虚拟转发器拥有者的接口实际]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_18718_x1832_x1214798335}[地址]{style="font-family:宋体"}

[[Priority]{lang="EN-US"}]{#struct_0_18718_x1832_968871812}

[[虚拟转发器的优先级，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_18718_x1832_x956338115}[～]{style="font-family:宋体"}[255]{lang="EN-US"}

[[Active]{lang="EN-US"}]{#struct_0_18718_x1832_x310667519}

[[AVF]{lang="EN-US"}]{#struct_0_18718_x1832_417744761}[的接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，当前转发器为]{style="font-family:宋体"}[AVF]{lang="EN-US"}[时，显示为]{style="font-family:宋体"}[local]{lang="EN-US"}

[[Forwarder Weight Track Configuration]{lang="EN-US"}]{#struct_0_18718_x1832_x956403651}

[[虚拟转发器权重监视配置信息。执行]{style="font-family:宋体"}**[vrrp vrid weight]{lang="EN-US"}**[ **track**]{lang="EN-US"}]{#struct_0_18718_x1832_x1461742405}[命令后，才会显示此信息]{style="font-family:宋体"}

[[Track Object]{lang="EN-US"}]{#struct_0_18718_x1832_x1970752938}

[[权重监视的]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_18718_x1832_x956469187}[项。执行]{style="font-family:宋体"}**[vrrp vrid weight]{lang="EN-US"}**[ **track**]{lang="EN-US"}[命令后，才会显示此信息]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_18718_x1832_1244996302}

[[Track]{lang="EN-US"}]{#struct_0_18718_x1832_2026145549}[项的状态，]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的状态包括]{style="font-family:宋体"}[Negative]{lang="EN-US"}[、]{style="font-family:宋体"}[Positive]{lang="EN-US"}[和]{style="font-family:宋体"}[NotReady ]{lang="EN-US"}

[[Weight Reduced]{lang="EN-US"}]{#struct_0_18718_x1832_x956534723}

[[监视的]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_18718_x1832_x1845878788}[项状态为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，权重降低的数额。执行]{style="font-family:宋体"}**[vrrp vrid weight]{lang="EN-US"}**[ **track**]{lang="EN-US"}[命令后，才会显示此信息]{style="font-family:
  宋体"}

[ ]{lang="EN-US"}

::: {#-1250607015 .myid}
[]{#_Toc404795927}[]{#struct_0_18718_x1832_x510320696}[]{#_Toc211671358}

**VRRP \-- IPv4 VRRP配置命令 \-- display vrrp statistics**

------------------------------------------------------------------------

[**[display vrrp statistics]{lang="EN-US"}**]{#struct_0_18718_x1832_x879046062}[命令用来显示]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1779154235}

[**[display vrrp]{lang="EN-US"}**[ **statistics** \[ **interface** *interface-type interface-number* \[ **vrid** *virtual-router-id* \] \]]{lang="EN-US"}]{#struct_0_18718_x1832_x956075971}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1332390555}

[[任意视图]{style="font-family:宋体"}]{#struct_0_18718_x1832_1943541051}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1345210421}

[[network-admin]{lang="EN-US"}]{#struct_0_18718_x1832_x266510349}

[[network-operator]{lang="EN-US"}]{#struct_0_18718_x1832_1986666793}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18718_x1832_x847814547}

[[mdc-operator]{lang="EN-US"}]{#struct_0_18718_x1832_x154976414}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18718_x1832_2079930189}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_18718_x1832_x248502475}[：显示指定接口的]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组统计信息。其中，]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}[为接口类型和接口编号。]{style="font-family:宋体"}

[**[vrid ]{lang="EN-US"}***[virtual-router-id]{lang="EN-US"}*]{#struct_0_18718_x1832_x956141507}[：显示指定备份组的]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[统计信息。其中，]{style="font-family:宋体"}*[virtual-router-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1650425195}

[[如果不输入接口名和备份组号，则显示该路由器上所有]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_1348787598}[备份组的统计信息；如果只输入接口名，不输入备份组号，则显示该接口上的所有]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组的统计信息；如果同时输入接口名和备份组号，则显示该接口上指定]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18718_x1832_736492647}

[[\# VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x1258752304}[工作在标准协议模式时，显示所有]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display vrrp statistics]{lang="EN-US"}]{#struct_0_18718_x1832_x956600258}

[ Interface               : GigabitEthernet1/0/1]{lang="EN-US"}

[ VRID                    : 1]{lang="EN-US"}

[ CheckSum Errors         : 0          Version Errors                : 0]{lang="EN-US"}

[ Invalid Pkts Rcvd  :      0          Unexpected Pkts Rcvd          : 0]{lang="EN-US"}

[ IP TTL Errors           : 0          Advertisement Interval Errors : 0]{lang="EN-US"}

[ Invalid Auth Type       : 0          Auth Failures                 : 0]{lang="EN-US"}

[ Packet Length Errors    : 0          Auth Type Mismatch            : 0]{lang="EN-US"}

[ Become Master           : 1          Address List Errors           : 0]{lang="EN-US"}

[ Adver Rcvd              : 0          Priority Zero Pkts Rcvd       : 0]{lang="EN-US"}

[ Adver Sent              : 807        Priority Zero Pkts Sent       : 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Global statistics]{lang="EN-US"}

[ CheckSum Errors         : 0]{lang="EN-US"}

[ Version Errors          : 0]{lang="EN-US"}

[ VRID Errors             : 0]{lang="EN-US"}

[[\# VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_1665725134}[工作在负载均衡模式时，显示全部]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display vrrp statistics]{lang="EN-US"}]{#struct_0_18718_x1832_x2076140946}

[ Interface               : GigabitEthernet1/0/1]{lang="EN-US"}

[ VRID                    : 1]{lang="EN-US"}

[ CheckSum Errors         : 0          Version Errors                : 0]{lang="EN-US"}

[ Invalid Pkts Rcvd       : 0          Unexpected Pkts Rcvd          : 0]{lang="EN-US"}

[ IP TTL Errors           : 0          Advertisement Interval Errors : 0]{lang="EN-US"}

[ Invalid Auth Type       : 0          Auth Failures                 : 0]{lang="EN-US"}

[ Packet Length Errors    : 0          Auth Type Mismatch            : 0]{lang="EN-US"}

[ Become Master           : 39         Address List Errors           : 0]{lang="EN-US"}

[ Become AVF              : 13         Packet Option Errors          : 0]{lang="EN-US"}

[ Adver Rcvd              : 2562       Priority Zero Pkts Rcvd       : 1 ]{lang="EN-US"}

[ Adver Sent              : 16373      Priority Zero Pkts Sent       : 49]{lang="EN-US"}

[ Request Rcvd            : 2          Reply Rcvd                    : 10]{lang="EN-US"}

[ Request Sent            : 12         Reply Sent                    : 2 ]{lang="EN-US"}

[ Release Rcvd            : 0          VF Priority Zero Pkts Rcvd    : 1 ]{lang="EN-US"}

[ Release Sent            : 0          VF Priority Zero Pkts Sent    : 11]{lang="EN-US"}

[ Redirect Timer Expires  : 1          Time-out Timer Expires        : 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Global statistics]{lang="EN-US"}

[ CheckSum Errors         : 0]{lang="EN-US"}

[ Version Errors          : 0]{lang="EN-US"}

[ VRID Errors             : 0]{lang="EN-US"}

[]{#struct_0_18718_x1832_x956665794}[[表1-5 ]{lang="EN-US"}[display vrrp statistics]{lang="EN-US"}]{#_Toc138047854}[显示]{style="font-family:黑体"}[信息描述表（标准协议模式）]{style="font-family:黑体"}

[]{#table_struct_0_x1796042897}[[字段]{style="font-family:黑体"}]{#struct_0_18718_x1832_x290018357}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_18718_x1832_473268324}

[[Interface]{lang="EN-US"}]{#struct_0_18718_x1832_x1063619204}

[[备份组所在接口]{style="font-family:宋体"}]{#struct_0_18718_x1832_109342494}

[[VRID]{lang="EN-US"}]{#struct_0_18718_x1832_x1480316271}

[[备份组号]{style="font-family:宋体"}]{#struct_0_18718_x1832_x888316301}

[[CheckSum Errors]{lang="EN-US"}]{#struct_0_18718_x1832_x956731330}

[[校验和错误的报文数]{style="font-family:宋体"}]{#struct_0_18718_x1832_1281326612}

[[Version Errors]{lang="EN-US"}]{#struct_0_18718_x1832_x860266292}

[[版本号错误的报文数]{style="font-family:宋体"}]{#struct_0_18718_x1832_x2096636869}

[[Invalid Pkts Rcvd]{lang="EN-US"}]{#struct_0_18718_x1832_834983701}

[[接收到报文类型错误的报文数]{style="font-family:宋体"}]{#struct_0_18718_x1832_x956796866}

[[Unexpected Pkts Rcvd]{lang="EN-US"}]{#struct_0_18718_x1832_579811080}

[[接收到未期望的报文数]{style="font-family:宋体"}]{#struct_0_18718_x1832_1305233289}

[[Advertisement Interval Errors]{lang="EN-US"}]{#struct_0_18718_x1832_x1935167607}

[[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x1506094452}[通告报文发送时间间隔错误的报文数]{style="font-family:宋体"}

[[IP TTL Errors]{lang="EN-US"}]{#struct_0_18718_x1832_381974867}

[[TTL]{lang="EN-US"}]{#struct_0_18718_x1832_x956338114}[错误的报文数]{style="font-family:宋体"}

[[Auth Failures]{lang="EN-US"}]{#struct_0_18718_x1832_x310601983}

[[认证失败的报文数]{style="font-family:宋体"}]{#struct_0_18718_x1832_x1513398708}

[[Invalid Auth Type]{lang="EN-US"}]{#struct_0_18718_x1832_211039317}

[[认证类型无效的报文数]{style="font-family:宋体"}]{#struct_0_18718_x1832_x1026909651}

[[Auth Type Mismatch]{lang="EN-US"}]{#struct_0_18718_x1832_x956403650}

[[认证类型不匹配的报文数]{style="font-family:宋体"}]{#struct_0_18718_x1832_x1461807941}

[[Packet Length Errors]{lang="EN-US"}]{#struct_0_18718_x1832_x885611349}

[[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_308328907}[报文长度错误的报文数]{style="font-family:宋体"}

[[Address List Errors]{lang="EN-US"}]{#struct_0_18718_x1832_x956469186}

[[备份组虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_18718_x1832_1244930766}[地址列表错误的报文数]{style="font-family:宋体"}

[[Become Master]{lang="EN-US"}]{#struct_0_18718_x1832_2005877425}

[[成为]{style="font-family:宋体"}[Master]{lang="EN-US"}]{#struct_0_18718_x1832_1120302132}[路由器的次数]{style="font-family:宋体"}

[[Priority Zero Pkts Rcvd]{lang="EN-US"}]{#struct_0_18718_x1832_x956534722}

[[收到的优先级为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_18718_x1832_x1845813252}[的]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文的数目]{style="font-family:宋体"}

[[Adver Rcvd]{lang="EN-US"}]{#struct_0_18718_x1832_x1259530977}

[[收到的]{style="font-family:宋体"}[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x1232743010}[通告报文的数目]{style="font-family:宋体"}

[[Priority Zero Pkts Sent]{lang="EN-US"}]{#struct_0_18718_x1832_197037243}

[[发送的优先级为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_18718_x1832_x956075970}[的]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文的数目]{style="font-family:宋体"}

[[Adver Sent]{lang="EN-US"}]{#struct_0_18718_x1832_1332456091}

[[发送的]{style="font-family:宋体"}[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x769119384}[通告报文的数目]{style="font-family:宋体"}

[[Global statistics]{lang="EN-US"}]{#struct_0_18718_x1832_565244027}

[[所有备份组的全局统计信息]{style="font-family:宋体"}]{#struct_0_18718_x1832_x956141506}

[[CheckSum Errors]{lang="EN-US"}]{#struct_0_18718_x1832_1650359659}

[[校验和错误的报文总数]{style="font-family:宋体"}]{#struct_0_18718_x1832_547116403}

[[Version Errors]{lang="EN-US"}]{#struct_0_18718_x1832_x1558120881}

[[版本号错误的报文总数]{style="font-family:宋体"}]{#struct_0_18718_x1832_x956600261}

[[VRID Errors]{lang="EN-US"}]{#struct_0_18718_x1832_1665266381}

[[备份组号错误的报文总数]{style="font-family:宋体"}]{#struct_0_18718_x1832_1043926951}

[ ]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display vrrp statistics]{lang="EN-US"}]{#struct_0_18718_x1832_1170835218}[显示信息描述表（负载均衡模式）]{style="font-family:黑体"}

[]{#table_struct_0_x1805792995}[[字段]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1086418481}

[[描述]{style="font-family:黑体"}]{#struct_0_18718_x1832_x956665797}

[[Interface]{lang="EN-US"}]{#struct_0_18718_x1832_x289821749}

[[备份组所在接口]{style="font-family:宋体"}]{#struct_0_18718_x1832_x231884283}

[[VRID]{lang="EN-US"}]{#struct_0_18718_x1832_x843050829}

[[备份组号]{style="font-family:宋体"}]{#struct_0_18718_x1832_x1093922708}

[[CheckSum Errors]{lang="EN-US"}]{#struct_0_18718_x1832_x929156325}

[[校验和错误的报文数]{style="font-family:宋体"}]{#struct_0_18718_x1832_x956731333}

[[Version Errors]{lang="EN-US"}]{#struct_0_18718_x1832_1281130004}

[[版本号错误的报文数]{style="font-family:宋体"}]{#struct_0_18718_x1832_x1642891437}

[[Invalid Pkts Rcvd]{lang="EN-US"}]{#struct_0_18718_x1832_x1109900201}

[[接收到报文类型错误的报文数]{style="font-family:宋体"}]{#struct_0_18718_x1832_x1889657812}

[[Unexpected Pkts Rcvd]{lang="EN-US"}]{#struct_0_18718_x1832_102801977}

[[接收到未期望的报文数]{style="font-family:宋体"}]{#struct_0_18718_x1832_x956796869}

[[Advertisement Interval Errors]{lang="EN-US"}]{#struct_0_18718_x1832_578828040}

[[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_2021680815}[通告报文发送时间间隔错误的报文数]{style="font-family:宋体"}

[[IP TTL Errors]{lang="EN-US"}]{#struct_0_18718_x1832_x1590220894}

[[TTL]{lang="EN-US"}]{#struct_0_18718_x1832_x36993500}[错误的报文数]{style="font-family:宋体"}

[[Auth Failures]{lang="EN-US"}]{#struct_0_18718_x1832_x956338117}

[[认证错误的报文数]{style="font-family:宋体"}]{#struct_0_18718_x1832_x310798591}

[[Invalid Auth Type]{lang="EN-US"}]{#struct_0_18718_x1832_x1980401759}

[[认证类型无效的报文数]{style="font-family:宋体"}]{#struct_0_18718_x1832_x697961294}

[[Auth Type Mismatch]{lang="EN-US"}]{#struct_0_18718_x1832_1373876725}

[[认证类型不匹配的报文数]{style="font-family:宋体"}]{#struct_0_18718_x1832_x956403653}

[[Packet Length Errors]{lang="EN-US"}]{#struct_0_18718_x1832_x1461873477}

[[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_879939867}[报文长度错误的报文数]{style="font-family:宋体"}

[[Address List Errors]{lang="EN-US"}]{#struct_0_18718_x1832_x161362495}

[[虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_18718_x1832_x956469189}[地址列表错误的报文数]{style="font-family:宋体"}

[[Become Master]{lang="EN-US"}]{#struct_0_18718_x1832_1245127374}

[[成为]{style="font-family:宋体"}[Master]{lang="EN-US"}]{#struct_0_18718_x1832_1650457779}[路由器的次数]{style="font-family:宋体"}

[[Redirect Timer Expires]{lang="EN-US"}]{#struct_0_18718_x1832_x958860210}

[[Redirect Timer]{lang="EN-US"}]{#struct_0_18718_x1832_x956534725}[超时的次数]{style="font-family:宋体"}

[[Become AVF]{lang="EN-US"}]{#struct_0_18718_x1832_x1845485572}

[[成为]{style="font-family:宋体"}[AVF]{lang="EN-US"}]{#struct_0_18718_x1832_96061055}[的次数]{style="font-family:宋体"}

[[Time-out Timer Expires]{lang="EN-US"}]{#struct_0_18718_x1832_x589669347}

[[Time-out Timer]{lang="EN-US"}]{#struct_0_18718_x1832_x956075973}[超时的次数]{style="font-family:宋体"}

[[Adver Rcvd]{lang="EN-US"}]{#struct_0_18718_x1832_1332259483}

[[收到的]{style="font-family:宋体"}[Advertisement]{lang="EN-US"}]{#struct_0_18718_x1832_1551189394}[报文的数目]{style="font-family:宋体"}

[[Request Rcvd]{lang="EN-US"}]{#struct_0_18718_x1832_424760613}

[[收到的]{style="font-family:宋体"}[Request]{lang="EN-US"}]{#struct_0_18718_x1832_x956141509}[报文的数目]{style="font-family:宋体"}

[[Adver Sent]{lang="EN-US"}]{#struct_0_18718_x1832_1650294123}

[[发送的]{style="font-family:宋体"}[Advertisement]{lang="EN-US"}]{#struct_0_18718_x1832_x238595356}[报文的数目]{style="font-family:宋体"}

[[Request Sent]{lang="EN-US"}]{#struct_0_18718_x1832_x1382507662}

[[发送的]{style="font-family:宋体"}[Request]{lang="EN-US"}]{#struct_0_18718_x1832_x956600260}[报文的数目]{style="font-family:宋体"}

[[Reply Rcvd]{lang="EN-US"}]{#struct_0_18718_x1832_1665200845}

[[收到的]{style="font-family:宋体"}[Reply]{lang="EN-US"}]{#struct_0_18718_x1832_x2030742511}[报文的数目]{style="font-family:宋体"}

[[Release Rcvd]{lang="EN-US"}]{#struct_0_18718_x1832_x956665796}

[[收到的]{style="font-family:宋体"}[Release]{lang="EN-US"}]{#struct_0_18718_x1832_x289887285}[报文的数目]{style="font-family:宋体"}

[[Reply Sent]{lang="EN-US"}]{#struct_0_18718_x1832_x281566393}

[[发送的]{style="font-family:宋体"}[Reply]{lang="EN-US"}]{#struct_0_18718_x1832_1851993610}[报文的数目]{style="font-family:宋体"}

[[Release Sent]{lang="EN-US"}]{#struct_0_18718_x1832_x956731332}

[[发送的]{style="font-family:宋体"}[Release]{lang="EN-US"}]{#struct_0_18718_x1832_1281195540}[报文的数目]{style="font-family:宋体"}

[[Priority Zero Pkts Rcvd]{lang="EN-US"}]{#struct_0_18718_x1832_286899806}

[[收到的路由器优先级为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_18718_x1832_x956796868}[的]{style="font-family:宋体"}[Advertisement]{lang="EN-US"}[报文的数目]{style="font-family:宋体"}

[[VF Priority Zero Pkts Rcvd]{lang="PT-BR"}]{#struct_0_18718_x1832_578893576}

[[收到的虚拟转发器优先级为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_18718_x1832_418753643}[的]{style="font-family:宋体"}[Advertisement]{lang="EN-US"}[报文的数目]{style="font-family:宋体"}

[[Priority Zero Pkts Sent]{lang="EN-US"}]{#struct_0_18718_x1832_x956338116}

[[发送的路由器优先级为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_18718_x1832_x310733055}[的]{style="font-family:宋体"}[Advertisement]{lang="EN-US"}[报文的数目]{style="font-family:宋体"}

[[VF Priority Zero Pkts Sent]{lang="EN-US"}]{#struct_0_18718_x1832_798258412}

[[发送的虚拟转发器优先级为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_18718_x1832_x956403652}[的]{style="font-family:宋体"}[Advertisement]{lang="EN-US"}[报文的数目]{style="font-family:宋体"}

[[Packet Option Errors]{lang="EN-US"}]{#struct_0_18718_x1832_x1461939013}

[[报文状态选项错误的次数]{style="font-family:宋体"}]{#struct_0_18718_x1832_x321797257}

[[Global statistics]{lang="EN-US"}]{#struct_0_18718_x1832_x956469188}

[[所有备份组的全局统计信息]{style="font-family:宋体"}]{#struct_0_18718_x1832_1245061838}

[[CheckSum Errors]{lang="EN-US"}]{#struct_0_18718_x1832_1262467186}

[[校验和错误的报文总数]{style="font-family:宋体"}]{#struct_0_18718_x1832_x956534724}

[[Version Errors]{lang="EN-US"}]{#struct_0_18718_x1832_x1845420036}

[[版本号错误的报文总数]{style="font-family:宋体"}]{#struct_0_18718_x1832_x81201572}

[[VRID Errors]{lang="EN-US"}]{#struct_0_18718_x1832_x956075972}

[[备份组号错误的报文总数]{style="font-family:宋体"}]{#struct_0_18718_x1832_1332325019}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x371798472}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset vrrp statistics]{lang="EN-US"}**]{#struct_0_18718_x1832_x799580727}

::: {#-68005434 .myid}
[]{#_Toc404795928}[]{#struct_0_18718_x1832_x2138561017}[]{#_Toc211671359}

**VRRP \-- IPv4 VRRP配置命令 \-- reset vrrp statistics**

------------------------------------------------------------------------

[**[reset vrrp statistics]{lang="EN-US"}**]{#struct_0_18718_x1832_1879631845}[命令用来清除]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x956141508}

[**[reset vrrp statistics ]{lang="EN-US"}**[\[ **interface** *interface-type interface-number* \[ **vrid** *virtual-router-id* \] \]]{lang="EN-US"}]{#struct_0_18718_x1832_1650228587}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1699727906}

[[用户视图]{style="font-family:宋体"}]{#struct_0_18718_x1832_x1596470042}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18718_x1832_17484425}

[[network-admin]{lang="EN-US"}]{#struct_0_18718_x1832_280447711}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18718_x1832_x1881705025}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18718_x1832_917362097}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_18718_x1832_1181700710}[：清除指定接口的]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组统计信息。其中，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。]{style="font-family:
宋体"}

[**[vrid ]{lang="EN-US"}***[virtual-router-id]{lang="EN-US"}*]{#struct_0_18718_x1832_x137988334}[：清除指定备份组的]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[统计信息。其中，]{style="font-family:宋体"}*[virtual-router-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18718_x1832_609483684}

[[在清除]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x818535070}[备份组统计信息时，如果不输入接口名和备份组号，则清除该路由器上所有]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组的统计信息；如果只输入接口名，不输入备份组号，则清除该接口上所有]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组的统计信息；如果同时输入接口名和备份组号，则清除该接口上指定]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x2040844206}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_x1744406209}[清除所有接口上所有]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组的]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset vrrp statistics]{lang="EN-US"}]{#struct_0_18718_x1832_109552405}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1639503245}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display vrrp]{lang="EN-US"}**[ **statistics**]{lang="EN-US"}]{#struct_0_18718_x1832_2065967337}
:::

::: {#315017389 .myid}
[]{#_Toc404795929}[]{#struct_0_18718_x1832_x120031684}[]{#_Toc342919155}

**VRRP \-- IPv4 VRRP配置命令 \-- snmp-agent trap enable vrrp**

------------------------------------------------------------------------

[**[snmp-agent]{lang="EN-US"}**[ **trap** **enable vrrp**]{lang="EN-US"}]{#struct_0_18718_x1832_609418148}[命令用来在全局下开启]{style="font-family:
宋体"}[VRRP]{lang="EN-US"}[告警功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **trap** **enable vrrp**]{lang="EN-US"}]{#struct_0_18718_x1832_1863632436}[命令用来在全局下关闭]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[告警功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_2084453565}

[**[snmp-agent]{lang="EN-US"}**[ **trap** **enable** **vrrp** \[ **auth-failure** \| **new-master** \]]{lang="EN-US"}]{#struct_0_18718_x1832_x1386547496}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **trap** **enable** **vrrp** \[ **auth-failure** \| **new-master** \]]{lang="EN-US"}]{#struct_0_18718_x1832_x1967674104}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1091061028}

[[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x1068608802}[的告警功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1302648188}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18718_x1832_960444973}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18718_x1832_609352612}

[[network-admin]{lang="EN-US"}]{#struct_0_18718_x1832_x1113775209}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18718_x1832_797312455}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18718_x1832_2008083915}

[**[auth-failure]{lang="EN-US"}**]{#struct_0_18718_x1832_1977983695}[：配置该参数后，当]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[备份组中的设备收到的]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文中的认证类型或认证字与本地不匹配时，会产生]{style="font-family:宋体"}[RFC2787]{lang="EN-US"}[规定的告警信息。]{style="font-family:宋体"}

[**[new-master]{lang="EN-US"}**]{#struct_0_18718_x1832_x910907260}[：配置该参数后，当备份组中设备从]{style="font-family:宋体"}[Initialize]{lang="EN-US"}[或]{style="font-family:宋体"}[Backup]{lang="EN-US"}[状态升级为]{style="font-family:宋体"}[Master]{lang="EN-US"}[状态时，会产生]{style="font-family:宋体"}[RFC2787]{lang="EN-US"}[规定的告警信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x904247401}

[[开启告警功能后，设备就可以向目的主机发送告警信息。具体是发送]{style="font-family:宋体"}[Inform]{lang="EN-US"}]{#struct_0_18718_x1832_630673041}[报文还是]{style="font-family:宋体"}[Trap]{lang="EN-US"}[报文，以及发往哪个目的主机，请通过]{style="font-family:宋体"}**[snmp-agent]{lang="EN-US"}**[ **target-host**]{lang="EN-US"}[命令来配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18718_x1832_660407645}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_609287076}[当]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[备份组中的设备收到的]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文中的认证类型或认证字与本地不匹配时，发送]{style="font-family:宋体"}[RFC2787]{lang="EN-US"}[规定的告警信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_1227897902}

[\[Sysname\] snmp-agent trap enable vrrp auth-failure]{lang="EN-US"}
:::

::: {#-366581484 .myid}
[]{#_Toc404795930}[]{#struct_0_18718_x1832_1354153533}[]{#_Toc211671361}

**VRRP \-- IPv4 VRRP配置命令 \-- vrrp check-ttl enable**

------------------------------------------------------------------------

[**[vrrp check-ttl enable]{lang="EN-US"}**]{#struct_0_18718_x1832_x409352416}[命令用来使能对]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[报文]{style="font-family:宋体"}[TTL]{lang="EN-US"}[域的检查。]{style="font-family:宋体"}

[**[undo vrrp check-ttl enable]{lang="EN-US"}**]{#struct_0_18718_x1832_x566491188}[命令用来禁止对]{style="font-family:
宋体"}[IPv4 VRRP]{lang="EN-US"}[报文的]{style="font-family:
宋体"}[TTL]{lang="EN-US"}[域的检查。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x333867546}

[**[vrrp check-ttl enable]{lang="EN-US"}**]{#struct_0_18718_x1832_9209154}

[**[undo vrrp check-ttl enable]{lang="EN-US"}**]{#struct_0_18718_x1832_x150214782}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18718_x1832_609745828}

[[检查]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x143092268}[报文的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[域。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1836374222}

[[接口视图]{style="font-family:宋体"}]{#struct_0_18718_x1832_x1440193406}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18718_x1832_103841664}

[[network-admin]{lang="EN-US"}]{#struct_0_18718_x1832_x433181859}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18718_x1832_1255042418}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18718_x1832_964443098}

[[Master]{lang="EN-US"}]{#struct_0_18718_x1832_x190095119}[路由器定时发送]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文，来通告它的存在。该报文以组播的形式在本网段内传播，不能被路由器转发，因此报文中的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值不会改变。]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器在发送]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文时，将报文中的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值设置为]{style="font-family:宋体"}[255]{lang="EN-US"}[。如果配置备份组里的路由器检查]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[域，则]{style="font-family:宋体"}[Backup]{lang="EN-US"}[路由器接收到]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值小于]{style="font-family:宋体"}[255]{lang="EN-US"}[的]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文时，将丢弃该报文，从而有效防止来自其他网段的攻击。]{style="font-family:宋体"}

[[不同厂商的设备实现可能不同，在与其他厂商设备互通时，检查]{style="font-family:宋体"}[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_609680292}[报文的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[域可能导致错误地丢弃报文，这时可以通过]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **vrrp** **check-ttl** **enable**]{lang="EN-US"}[命令禁止检查]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[域。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x535538948}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18718_x1832_2082178895}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_375768511}[禁止检查]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[域。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_x1940793910}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] undo vrrp check-ttl enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18718_x1832_1402189398}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_923876663}[禁止检查]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[域。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_609614756}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] undo vrrp check-ttl enable]{lang="EN-US"}
:::

::: {#927450648 .myid}
[]{#_Toc211671360}[]{#_Toc404795931}[]{#struct_0_18718_x1832_1346547556}

**VRRP \-- IPv4 VRRP配置命令 \-- vrrp dot1q**

------------------------------------------------------------------------

[**[vrrp dot1q]{lang="NO-BOK"}**]{#struct_0_18718_x1832_1693056041}[命令用来配置]{style="font-family:宋体"}[IPv4 VRRP]{lang="NO-BOK"}[的控制]{style="font-family:宋体"}[VLAN]{lang="NO-BOK"}[。]{style="font-family:宋体"}

[**[undo vrrp dot1q]{lang="NO-BOK"}**]{#struct_0_18718_x1832_810828262}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1684056959}

[**[vrrp dot1q vid ]{lang="NO-BOK"}***[vlan-id]{lang="EN-US"}*]{#struct_0_18718_x1832_1048813430}**[ ]{lang="EN-US"}**[\[ **secondary-dot1q** *secondary-*]{lang="NO-BOK"}*[vlan-id ]{lang="EN-US"}*[\]]{lang="EN-US"}

[**[undo vrrp dot1q]{lang="EN-US"}**]{#struct_0_18718_x1832_1090702900}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1335726314}

[[没有指定]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_1087281190}[的控制]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，即]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[终结支持广播]{style="font-family:宋体"}[/]{lang="EN-US"}[组播功能后，]{style="font-family:宋体"}[Master]{lang="EN-US"}[在所有模糊终结的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内发送]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18718_x1832_609549220}

[[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18718_x1832_x461418130}[三层聚合子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18718_x1832_704150637}

[[network-admin]{lang="EN-US"}]{#struct_0_18718_x1832_x1478988270}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18718_x1832_x506778856}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1403742625}

[**[vid ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_18718_x1832_x1772464975}[：指定]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[的控制]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[（外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[）的编号，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[secondary-dot1q ]{lang="EN-US"}***[secondary-]{lang="EN-US"}[vlan-id]{lang="EN-US"}*]{#struct_0_18718_x1832_347574035}[：指定内层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，]{style="font-family:宋体"}*[secondary-]{lang="EN-US"}[vlan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1005179731}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重复执行本命令，新的配置将覆盖原有配置。]{style="font-family:宋体"}]{#struct_0_18718_x1832_610007972}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有在三层以太网子接口、三层聚合子接口和三层]{style="font-family:宋体"}]{#struct_0_18718_x1832_x783081510}[RPR]{lang="EN-US"}[逻辑接口下执行本命令才会生效；在其他接口视图下也可以执行本命令，但不会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x700204895}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_x387398876}[配置]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[的控制]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[（外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[）]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[2]{lang="EN-US"}[，内层]{style="font-family:
宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_99786680}

[\[Sysname\] interface gigabitethernet 1/0/1.2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.2\] vrrp dot1q vid 2 secondary-dot1q 100]{lang="EN-US"}
:::

::: {#1853925949 .myid}
[]{#_Toc404795932}[]{#struct_0_18718_x1832_562987352}[]{#_Toc337719113}

**VRRP \-- IPv4 VRRP配置命令 \-- vrrp dscp**

------------------------------------------------------------------------

[**[vrrp dscp]{lang="EN-US"}**]{#struct_0_18718_x1832_1729789766}[命令用来配置]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[**[undo vrrp dscp]{lang="EN-US"}**]{#struct_0_18718_x1832_1100958955}[命令用来恢复缺省值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_609942436}

[**[vrrp dscp ]{lang="EN-US"}***[dscp-value]{lang="EN-US"}*]{#struct_0_18718_x1832_1565003030}

[**[undo vrrp dscp]{lang="EN-US"}**]{#struct_0_18718_x1832_x971394657}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1350839153}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18718_x1832_x828906566}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1480398977}

[[network-admin]{lang="EN-US"}]{#struct_0_18718_x1832_x2137468228}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18718_x1832_540414577}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1104324151}

[*[dscp-value]{lang="EN-US"}*]{#struct_0_18718_x1832_609483685}[：]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[48]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x818535069}

[[DSCP]{lang="EN-US" style="font-size:10.0pt;color:black"}]{#struct_0_18718_x1832_x2040254383}[用来体现报文自身的优先等级，决定报文传输的优先程度。配置的]{style="font-family:
宋体"}[DSCP]{lang="EN-US"}[优先级的取值越大，报文的优先级越高。通过本命令可以指定发送的]{style="font-family:宋体"}[VRRP]{lang="EN-US" style="font-size:10.0pt;color:black"}[报文中携带的]{style="font-family:宋体"}[DSCP]{lang="EN-US" style="font-size:10.0pt;color:black"}[优先级的取值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x936937540}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_783189283}[配置]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_1411704272}

[\[Sysname\] vrrp dscp 30]{lang="EN-US"}
:::

::::: {#-2139109788 .myid}
[]{#_Toc404795933}[]{#struct_0_18718_x1832_x330115273}[]{#_Toc270693099}[]{#_Toc280174807}[]{#_Toc280177514}[]{#_Toc280281395}[]{#_Toc270693100}[]{#_Toc280174808}[]{#_Toc280177515}[]{#_Toc280281396}[]{#_Toc270693102}[]{#_Toc280174810}[]{#_Toc280177517}[]{#_Toc280281398}[]{#_Toc270693103}[]{#_Toc280174811}[]{#_Toc280177518}[]{#_Toc280281399}[]{#_Toc270693104}[]{#_Toc280174812}[]{#_Toc280177519}[]{#_Toc280281400}[]{#_Toc270693105}[]{#_Toc280174813}[]{#_Toc280177520}[]{#_Toc280281401}[]{#_Toc270693106}[]{#_Toc280174814}[]{#_Toc280177521}[]{#_Toc280281402}[]{#_Toc270693107}[]{#_Toc280174815}[]{#_Toc280177522}[]{#_Toc280281403}[]{#_Toc270693108}[]{#_Toc280174816}[]{#_Toc280177523}[]{#_Toc280281404}[]{#_Toc270693109}[]{#_Toc280174817}[]{#_Toc280177524}[]{#_Toc280281405}[]{#_Toc270693110}[]{#_Toc280174818}[]{#_Toc280177525}[]{#_Toc280281406}[]{#_Toc270693111}[]{#_Toc280174819}[]{#_Toc280177526}[]{#_Toc280281407}[]{#_Toc270693112}[]{#_Toc280174820}[]{#_Toc280177527}[]{#_Toc280281408}[]{#_Toc270693113}[]{#_Toc280174821}[]{#_Toc280177528}[]{#_Toc280281409}[]{#_Toc270693114}[]{#_Toc280174822}[]{#_Toc280177529}[]{#_Toc280281410}[]{#_Toc270693115}[]{#_Toc280174823}[]{#_Toc280177530}[]{#_Toc280281411}[]{#_Toc270693116}[]{#_Toc280174824}[]{#_Toc280177531}[]{#_Toc280281412}[]{#_Toc270693117}[]{#_Toc280174825}[]{#_Toc280177532}[]{#_Toc280281413}[]{#_Toc270693118}[]{#_Toc280174826}[]{#_Toc280177533}[]{#_Toc280281414}[]{#_Toc270693119}[]{#_Toc280174827}[]{#_Toc280177534}[]{#_Toc280281415}[]{#_Toc270693120}[]{#_Toc280174828}[]{#_Toc280177535}[]{#_Toc280281416}[]{#_Toc270693121}[]{#_Toc280174829}[]{#_Toc280177536}[]{#_Toc280281417}

**VRRP \-- IPv4 VRRP配置命令 \-- vrrp mode**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VRRP命令.files/image002.png){#图片 2 width="62" height="27"}]{lang="EN-US"}]{#struct_0_18718_x1832_x1024746748}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_18718_x1832_609418149}
:::

[ ]{lang="EN-US"}

[**[vrrp mode]{lang="EN-US"}**]{#struct_0_18718_x1832_1863632435}[命令用来配置]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[的工作模式。]{style="font-family:宋体"}

[**[undo vrrp mode]{lang="EN-US"}**]{#struct_0_18718_x1832_2084650173}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_577530678}

[**[vrrp mode load-balance ]{lang="EN-US"}**[\[ **version-8** \]]{lang="EN-US"}]{#struct_0_18718_x1832_x1408245809}

[**[undo vrrp mode]{lang="EN-US"}**]{#struct_0_18718_x1832_1058393308}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x358889629}

[[IPv4 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_2001347404}[工作在标准协议模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18718_x1832_609352613}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18718_x1832_x1113775210}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1125067382}

[[network-admin]{lang="EN-US"}]{#struct_0_18718_x1832_960733242}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18718_x1832_x1310435108}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18718_x1832_2088976098}

[**[load-balance]{lang="EN-US"}**]{#struct_0_18718_x1832_263541461}[：指定]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[工作在负载均衡模式。]{style="font-family:宋体"}

[**[version-8]{lang="EN-US"}**]{#struct_0_18718_x1832_x171612696}[：发送的协议报文携带的版本号为]{style="font-family:宋体"}[8]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18718_x1832_187971248}

[[创建]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x1299112492}[备份组后，仍然可以修改]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[的工作模式。修改]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[的工作模式后，路由器上所有的]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组都会工作在该模式。]{style="font-family:宋体"}

[[只有接口配置的]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x2127927832}[使用的版本为]{style="font-family:宋体"}[VRRPv2]{lang="EN-US"}[时，指定]{style="font-family:宋体"}**[version-8]{lang="EN-US"}**[参数才会生效。若备份组满足以下所有条件时，需要配置]{style="font-family:宋体"}**[version-8]{lang="EN-US"}**[参数：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[备份组中存在使用]{style="font-family:宋体"}]{#struct_0_18718_x1832_1573552281}[ComwareV5]{lang="EN-US"}[版本软件的路由器；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[备份组中所有路由器的]{style="font-family:宋体"}]{#struct_0_18718_x1832_1250762145}[IPv4 VRRP]{lang="EN-US"}[均需要工作在负载均衡模式；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[备份组中所有路由器的]{style="font-family:宋体"}]{#struct_0_18718_x1832_1222327166}[IPv4 VRRP]{lang="EN-US"}[使用的版本均要配置为]{style="font-family:宋体"}[VRRPv2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18718_x1832_609287077}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_1227897903}[配置]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[工作在负载均衡模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_1354219069}

[\[Sysname\] vrrp mode load-balance]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x2001644142}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **vrrp**]{lang="EN-US"}]{#struct_0_18718_x1832_815179571}
:::::

::: {#751203685 .myid}
[]{#_Toc211671362}[]{#_Toc404795934}[]{#struct_0_18718_x1832_1559951247}

**VRRP \-- IPv4 VRRP配置命令 \-- vrrp version**

------------------------------------------------------------------------

[**[vrrp version]{lang="EN-US"}**]{#struct_0_18718_x1832_x459886766}[命令用来配置接口下]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[使用的版本。]{style="font-family:宋体"}

[**[undo vrrp version]{lang="EN-US"}**]{#struct_0_18718_x1832_155400041}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_609745829}

[**[vrrp version ]{lang="EN-US"}***[version-number]{lang="EN-US"}*]{#struct_0_18718_x1832_x143092267}

[**[undo vrrp version]{lang="EN-US"}**]{#struct_0_18718_x1832_x1836570830}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x2080212138}

[[IPv4 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_2025156929}[使用的版本为]{style="font-family:宋体"}[VRRPv3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x255181370}

[[接口视图]{style="font-family:宋体"}]{#struct_0_18718_x1832_963149158}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x723534437}

[[network-admin]{lang="EN-US"}]{#struct_0_18718_x1832_x1985270067}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18718_x1832_609680293}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x535538947}

[*[version-number]{lang="EN-US"}*]{#struct_0_18718_x1832_2081195855}[：]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[协议的版本号，取值为]{style="font-family:宋体"}[2]{lang="EN-US"}[或]{style="font-family:宋体"}[3]{lang="EN-US"}[，其中]{style="font-family:宋体"}[2]{lang="EN-US"}[表示使用]{style="font-family:宋体"}[VRRPv2]{lang="EN-US"}[版本（]{style="font-family:宋体"}[RFC 3768]{lang="EN-US"}[），]{style="font-family:宋体"}[3]{lang="EN-US"}[表示使用]{style="font-family:宋体"}[VRRPv3]{lang="EN-US"}[版本（]{style="font-family:宋体"}[RFC 5798]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18718_x1832_2003415442}

[[IPv4 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_2028625648}[备份组中的所有路由器上配置的]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[版本必须一致。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x174929452}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18718_x1832_x2078676626}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_1381502467}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[使用的版本为]{style="font-family:宋体"}[VRRPv2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_609614757}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] vrrp version 2]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18718_x1832_1346547555}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_1692990505}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[10]{lang="EN-US"}[上]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[使用的版本为]{style="font-family:宋体"}[VRRPv2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_413882245}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] vrrp version 2]{lang="EN-US"}
:::

::: {#-1983040082 .myid}
[]{#_Toc404795935}[]{#struct_0_18718_x1832_1343633548}[]{#_Toc211671368}[]{#_Toc99954757}[]{#_Toc34483424}[]{#_Toc33425593}[]{#_Toc31785778}

**VRRP \-- IPv4 VRRP配置命令 \-- vrrp vrid**

------------------------------------------------------------------------

[**[vrrp vrid]{lang="EN-US"}**]{#struct_0_18718_x1832_x428880139}[命令用来创建]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组，并配置]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组的虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，或为一个已经存在的]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组添加一个虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo vrrp vrid]{lang="EN-US"}**]{#struct_0_18718_x1832_x1692335651}[命令用来删除一个已经存在的]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组的所有配置，或删除已经存在的]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组中的虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1928757927}

[**[vrrp vrid]{lang="EN-US"}**[ ]{lang="EN-US"}*[virtual-router-id]{lang="EN-US"}***[ virtual-ip]{lang="EN-US"}**[ *virtual-address*]{lang="EN-US"}]{#struct_0_18718_x1832_609352608}

[**[undo vrrp vrid]{lang="EN-US"}**[ *virtual-router-id* \[ **virtual-ip** \[ *virtual-address* \] \]]{lang="EN-US"}]{#struct_0_18718_x1832_1224876945}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x794474074}

[[未创建]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_1223424151}[备份组。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x283746069}

[[接口视图]{style="font-family:宋体"}]{#struct_0_18718_x1832_x222548415}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1120164334}

[[network-admin]{lang="EN-US"}]{#struct_0_18718_x1832_x1775531859}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18718_x1832_1996375634}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18718_x1832_609287072}

[*[virtual-router-id]{lang="EN-US"}*]{#struct_0_18718_x1832_1227897906}[：]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[v]{lang="EN-US"}**]{#struct_0_18718_x1832_1354415677}**[irtual]{lang="EN-US"}[-ip]{lang="EN-US"}***[ ]{lang="EN-US"}[virtual-address]{lang="EN-US"}*[：备份组的虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。不能为全零地址]{style="font-family:宋体"}[(0.0.0.0)]{lang="EN-US"}[、广播地址]{style="font-family:宋体"}[(255.255.255.255)]{lang="EN-US"}[、环回地址、非]{style="font-family:宋体"}[A/B/C]{lang="EN-US"}[类地址和其它非法]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[(]{lang="EN-US"}[如]{style="font-family:宋体"}[0.0.0.1)]{lang="EN-US"}[。删除]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组中的虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址时，如果不指定]{style="font-family:宋体"}*[virtual-address]{lang="EN-US"}*[参数，则表示删除该备份组中的所有虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x7086717}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重复执行本命令，可以为]{style="font-family:宋体"}]{#struct_0_18718_x1832_59279170}[IPv4 VRRP]{lang="EN-US"}[备份组配置多个虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，但每个备份组最多只能配置]{style="font-family:宋体"}[16]{lang="EN-US"}[个虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果没有为备份组配置虚拟]{style="font-family:宋体"}]{#struct_0_18718_x1832_1931980541}[IP]{lang="EN-US"}[地址，但是为备份组进行了其他配置（如优先级、抢占方式等），则该备份组会存在于设备上，并处于]{style="font-family:宋体"}[Inactive]{lang="EN-US"}[状态，此时备份组不起作用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[建议将备份组的虚拟]{style="font-family:宋体"}]{#struct_0_18718_x1832_x1540090888}[IP]{lang="EN-US"}[地址和备份组中设备下行接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址配置为同一网段，否则可能导致局域网内的主机无法访问外部网络。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv4 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x467389501}[工作在负载均衡模式时，要求备份组的虚拟]{style="font-family:
宋体"}[IP]{lang="EN-US"}[地址和接口的]{style="font-family:
宋体"}[IP]{lang="EN-US"}[地址不能相同。否则，]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[负载均衡功能将无法正常工作。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x844894042}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18718_x1832_609745824}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_x143092272}[创建]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[，配置]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[的虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.10.10.10]{lang="EN-US"}[。为]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[添加一个虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[10.10.10.11]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_x1836767439}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] vrrp vrid 1 virtual-ip 10.10.10.10]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] vrrp vrid 1 virtual-ip 10.10.10.11]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18718_x1832_x879225852}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_x580690007}[创建]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[，配置]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[的虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.10.10.10]{lang="EN-US"}[。为]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[添加一个虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[10.10.10.11]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_1491748139}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] vrrp vrid 1 virtual-ip 10.10.10.10]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] vrrp vrid 1 virtual-ip 10.10.10.11]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1124447095}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **vrrp**]{lang="EN-US"}]{#struct_0_18718_x1832_609680288}
:::

::: {#1316738116 .myid}
[]{#_Toc404795936}[]{#struct_0_18718_x1832_2067130339}[]{#_Toc197333719}[]{#_Toc197943244}[]{#_Toc198389981}[]{#_Toc197333720}[]{#_Toc197943245}[]{#_Toc198389982}[]{#_Toc197333721}[]{#_Toc197943246}[]{#_Toc198389983}[]{#_Toc197333722}[]{#_Toc197943247}[]{#_Toc198389984}[]{#_Toc197333723}[]{#_Toc197943248}[]{#_Toc198389985}[]{#_Toc197333724}[]{#_Toc197943249}[]{#_Toc198389986}[]{#_Toc197333725}[]{#_Toc197943250}[]{#_Toc198389987}[]{#_Toc197333726}[]{#_Toc197943251}[]{#_Toc198389988}[]{#_Toc197333727}[]{#_Toc197943252}[]{#_Toc198389989}[]{#_Toc197333728}[]{#_Toc197943253}[]{#_Toc198389990}[]{#_Toc197333729}[]{#_Toc197943254}[]{#_Toc198389991}[]{#_Toc197333730}[]{#_Toc197943255}[]{#_Toc198389992}[]{#_Toc197333731}[]{#_Toc197943256}[]{#_Toc198389993}[]{#_Toc197333732}[]{#_Toc197943257}[]{#_Toc198389994}[]{#_Toc197333733}[]{#_Toc197943258}[]{#_Toc198389995}[]{#_Toc197333734}[]{#_Toc197943259}[]{#_Toc198389996}[]{#_Toc197333735}[]{#_Toc197943260}[]{#_Toc198389997}[]{#_Toc197333736}[]{#_Toc197943261}[]{#_Toc198389998}[]{#_Toc197333737}[]{#_Toc197943262}[]{#_Toc198389999}[]{#_Toc197333738}[]{#_Toc197943263}[]{#_Toc198390000}[]{#_Toc194230961}[]{#_Toc195410171}[]{#_Toc194230962}[]{#_Toc195410172}[]{#_Toc194230965}[]{#_Toc195410175}[]{#_Toc194230966}[]{#_Toc195410176}[]{#_Toc194230967}[]{#_Toc195410177}[]{#_Toc194230968}[]{#_Toc195410178}[]{#_Toc194230969}[]{#_Toc195410179}[]{#_Toc194230970}[]{#_Toc195410180}[]{#_Toc194230971}[]{#_Toc195410181}[]{#_Toc194230972}[]{#_Toc195410182}[]{#_Toc194230973}[]{#_Toc195410183}[]{#_Toc194230974}[]{#_Toc195410184}[]{#_Toc194230975}[]{#_Toc195410185}[]{#_Toc194230976}[]{#_Toc195410186}[]{#_Toc194230977}[]{#_Toc195410187}[]{#_Toc194230978}[]{#_Toc195410188}[]{#_Toc194230979}[]{#_Toc195410189}[]{#_Toc194230981}[]{#_Toc195410191}[]{#_Toc197333742}[]{#_Toc197943267}[]{#_Toc198390004}[]{#_Toc197333745}[]{#_Toc197943270}[]{#_Toc198390007}[]{#_Toc197333746}[]{#_Toc197943271}[]{#_Toc198390008}[]{#_Toc197333747}[]{#_Toc197943272}[]{#_Toc198390009}[]{#_Toc197333748}[]{#_Toc197943273}[]{#_Toc198390010}[]{#_Toc197333749}[]{#_Toc197943274}[]{#_Toc198390011}[]{#_Toc197333750}[]{#_Toc197943275}[]{#_Toc198390012}[]{#_Toc197333751}[]{#_Toc197943276}[]{#_Toc198390013}[]{#_Toc197333752}[]{#_Toc197943277}[]{#_Toc198390014}[]{#_Toc197333753}[]{#_Toc197943278}[]{#_Toc198390015}[]{#_Toc197333754}[]{#_Toc197943279}[]{#_Toc198390016}[]{#_Toc197333755}[]{#_Toc197943280}[]{#_Toc198390017}[]{#_Toc197333756}[]{#_Toc197943281}[]{#_Toc198390018}[]{#_Toc197333758}[]{#_Toc197943283}[]{#_Toc198390020}[]{#_Toc197333759}[]{#_Toc197943284}[]{#_Toc198390021}[]{#_Toc197333760}[]{#_Toc197943285}[]{#_Toc198390022}[]{#_Toc197333761}[]{#_Toc197943286}[]{#_Toc198390023}[]{#_Toc197333764}[]{#_Toc197943289}[]{#_Toc198390026}

**VRRP \-- IPv4 VRRP配置命令 \-- vrrp vrid authentication-mode**

------------------------------------------------------------------------

[**[vrrp vrid authentication-mode]{lang="EN-US"}**]{#struct_0_18718_x1832_1762084583}[命令用来配置备份组发送和接收]{style="font-family:
宋体"}[IPv4 VRRP]{lang="EN-US"}[报文的认证方式和认证字。]{style="font-family:宋体"}

[**[undo vrrp vrid authentication-mode]{lang="EN-US"}**]{#struct_0_18718_x1832_x2140527057}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1696604601}

[**[vrrp vrid]{lang="EN-US"}**[ *virtual-router-id* **authentication-mode** { **md5** \| **simple** } { **cipher** \| **plain** } *key*]{lang="EN-US"}]{#struct_0_18718_x1832_609549221}

[**[undo vrrp vrid]{lang="EN-US"}**[ *virtual-router-id* **authentication-mode**]{lang="EN-US"}]{#struct_0_18718_x1832_x461418129}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18718_x1832_703691886}

[[备份组发送和接收]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_105423188}[报文时不进行认证。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18718_x1832_760852656}

[[接口视图]{style="font-family:宋体"}]{#struct_0_18718_x1832_x1129254128}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1737932435}

[[network-admin]{lang="EN-US"}]{#struct_0_18718_x1832_62307107}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18718_x1832_1261110386}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18718_x1832_610007973}

[*[virtual-router-id]{lang="EN-US"}*]{#struct_0_18718_x1832_x783081509}[：]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[md5]{lang="EN-US"}**]{#struct_0_18718_x1832_x700663648}[：表示使用]{style="font-family:宋体"}[MD5]{lang="EN-US"}[算法进行认证。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_18718_x1832_x784171764}[：表示使用简单字符进行认证。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_18718_x1832_x1251231489}[：表示以密文方式设置认证字。]{style="font-family:宋体"}

[**[plain]{lang="EN-US"}**]{#struct_0_18718_x1832_1696089755}[：表示以明文方式设置认证字。]{style="font-family:宋体"}

[*[key]{lang="EN-US"}*]{#struct_0_18718_x1832_x230473922}[：认证字，区分大小写。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[采用]{style="font-family:宋体"}]{#struct_0_18718_x1832_x429566160}**[md5]{lang="EN-US"}**[认证方式，当使用]{style="font-family:宋体"}**[cipher]{lang="EN-US"}**[参数时，]{style="font-family:宋体"}*[key]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[41]{lang="EN-US"}[个字符的密文认证字；当使用]{style="font-family:宋体"}**[plain]{lang="EN-US"}**[参数时，]{style="font-family:宋体"}*[key]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8]{lang="EN-US"}[个字符的明文认证字。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[采用]{style="font-family:宋体"}]{#struct_0_18718_x1832_1870010373}**[simple]{lang="EN-US"}**[认证方式，当使用]{style="font-family:宋体"}**[cipher]{lang="EN-US"}**[参数时，]{style="font-family:宋体"}*[key]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[41]{lang="EN-US"}[个字符的密文认证字；当使用]{style="font-family:宋体"}**[plain]{lang="EN-US"}**[参数时，]{style="font-family:宋体"}*[key]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8]{lang="EN-US"}[个字符的明文认证字。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1925106420}

[[为了防止非法用户构造报文攻击备份组，]{style="font-family:宋体"}[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_609942437}[通过在]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[报文中增加认证字的方式，验证接收到的]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[报文。]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[提供了两种认证方式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[simple]{lang="EN-US"}**]{#struct_0_18718_x1832_1565003031}[：简单字符认证。发送]{style="font-family:
宋体"}[VRRP]{lang="EN-US"}[报文的路由器将认证字填入到]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[报文中，而收到]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[报文的路由器会将收到的]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[报文中的认证字和本地配置的认证字进行比较。如果认证字相同，则认为接收到的报文是真实、合法的]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[报文；否则认为接收到的报文是一个非法报文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[md5]{lang="EN-US"}**]{#struct_0_18718_x1832_x971329121}[：]{lang="EN-US" style="font-family:宋体"}[MD5]{lang="EN-US"}[认证。发送]{lang="EN-US" style="font-family:宋体"}[VRRP]{lang="EN-US"}[报文的路由器利用认证字和]{lang="EN-US" style="font-family:宋体"}[MD5]{lang="EN-US"}[算法对]{lang="EN-US" style="font-family:宋体"}[VRRP]{lang="EN-US"}[报文进行摘要运算，运算结果保存在]{lang="EN-US" style="font-family:宋体"}[Authentication Header]{lang="EN-US"}[（认证头）中。]{lang="EN-US" style="font-family:宋体"}[收到]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[报文的路由器会利用认证字和]{style="font-family:宋体"}[MD5]{lang="EN-US"}[算法进行同样的运算，并将运算结果与认证头的内容进行比较。如果相同，则认为接收到的报文是真实、合法的]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[报文；否则认为接收到的报文是一个非法报文。]{style="font-family:宋体"}

[[MD5]{lang="EN-US"}]{#struct_0_18718_x1832_x143202131}[认证比简单字符认证更安全，但是]{style="font-family:宋体"}[MD5]{lang="EN-US"}[认证需要进行额外的运算，占用的系统资源较多。]{style="font-family:宋体"}

[[以明文或密文方式设置的验证字，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_18718_x1832_525477747}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_18718_x1832_x576265098}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个接口上的不同备份组可以设置不同的认证方式和认证字；加入同一备份组的成员需要设置相同的认证方式和认证字。]{style="font-family:宋体"}]{#struct_0_18718_x1832_x171221082}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{lang="EN-US" style="font-family:宋体"}[VRRPv3]{lang="EN-US"}]{#struct_0_18718_x1832_2056293690}[版本的]{lang="EN-US" style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[不支持认证。使用]{lang="EN-US" style="font-family:宋体"}[VRRPv3]{lang="EN-US"}[版本时，此配置不会生效。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1766802810}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18718_x1832_609483682}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_x818535064}[设置]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[发送和接收]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[报文的认证方式为]{style="font-family:宋体"}**[simple]{lang="EN-US"}**[，认证字为]{style="font-family:宋体"}[Sysname]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_x2040582063}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] vrrp vrid 1 authentication-mode simple plain Sysname]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18718_x1832_2035962402}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_x584585081}[设置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[上备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[发送和接收]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[报文的认证方式为]{style="font-family:宋体"}**[simple]{lang="EN-US"}**[，认证字为]{style="font-family:宋体"}[Sysname]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_x1509913639}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] vrrp vrid 1 authentication-mode simple plain Sysname]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1737307573}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **vrrp**]{lang="EN-US"}]{#struct_0_18718_x1832_1624781121}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vrrp]{lang="EN-US"}**[ **version**]{lang="EN-US"}]{#struct_0_18718_x1832_609418146}
:::

::: {#546376843 .myid}
[]{#_Toc404795937}[]{#struct_0_18718_x1832_1863632430}[]{#_Toc211671363}[]{#_Toc99954753}[]{#_Toc34483420}[]{#_Toc33425589}[]{#_Toc31785779}

**VRRP \-- IPv4 VRRP配置命令 \-- vrrp vrid preempt-mode**

------------------------------------------------------------------------

[**[vrrp vrid preempt-mode]{lang="EN-US"}**]{#struct_0_18718_x1832_2084322493}[命令用来设置]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组中的路由器工作在抢占方式，并配置抢占延迟时间。]{style="font-family:宋体"}

[**[undo vrrp vrid preempt-mode]{lang="EN-US"}**]{#struct_0_18718_x1832_2141946143}[命令用来取消抢占方式，即设置]{style="font-family:
宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组中的路由器工作在非抢占方式。]{style="font-family:宋体"}

[**[undo vrrp vrid preempt-mode delay]{lang="EN-US"}**]{#struct_0_18718_x1832_x2076673434}[命令用来恢复抢占延迟时间为缺省值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x183032687}

[**[vrrp vrid ]{lang="EN-US"}***[virtual-router-id]{lang="EN-US"}***[ preempt-mode]{lang="EN-US"}**[ \[ **delay** *delay-value* \]]{lang="EN-US"}]{#struct_0_18718_x1832_2068339400}

[**[undo]{lang="EN-US"}**[ **vrrp vrid** *virtual-router-id* **preempt-mode** \[ **delay** \]]{lang="EN-US"}]{#struct_0_18718_x1832_1610618475}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18718_x1832_609352610}

[[IPv4 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x1113775207}[备份组中的路由器工作在抢占方式下，抢占延迟时间为]{style="font-family:宋体"}[0]{lang="EN-US"}[厘秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1247651149}

[[接口视图]{style="font-family:宋体"}]{#struct_0_18718_x1832_714651691}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1094020620}

[[network-admin]{lang="EN-US"}]{#struct_0_18718_x1832_x68659025}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18718_x1832_x1547025203}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x2050288998}

[*[virtual-router-id]{lang="EN-US"}*]{#struct_0_18718_x1832_x1694651071}[：]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[delay]{lang="EN-US"}***[ delay-value]{lang="EN-US"}*]{#struct_0_18718_x1832_609287074}[：抢占延迟时间。]{style="font-family:宋体"}*[delay-value]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[180000]{lang="EN-US"}[，单位为厘秒，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[厘秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1227897900}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果备份组中的路由器工作在非抢占方式下，则只要]{style="font-family:宋体"}]{#struct_0_18718_x1832_1354284605}[Master]{lang="EN-US"}[路由器没有出现故障，]{style="font-family:宋体"}[Backup]{lang="EN-US"}[路由器即使随后被配置了更高的优先级也不会成为]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器。非抢占方式可以避免频繁地切换]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果备份组中的路由器工作在抢占方式下，它一旦发现自己的优先级比当前的]{style="font-family:宋体"}]{#struct_0_18718_x1832_x1583328537}[Master]{lang="EN-US"}[路由器的优先级高，就会对外发送]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文。导致备份组内路由器重新选举]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器，并最终取代原有的]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器。相应地，原来的]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器将会变成]{style="font-family:宋体"}[Backup]{lang="EN-US"}[路由器。抢占方式可以确保承担转发任务的]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器始终是备份组中优先级最高的设备。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为了避免备份组内的成员频繁进行主备状态转换，让]{style="font-family:宋体"}]{#struct_0_18718_x1832_x1619925883}[Backup]{lang="EN-US"}[路由器有足够的时间搜集必要的信息（如路由信息），]{style="font-family:宋体"}[Backup]{lang="EN-US"}[路由器接收到优先级低于本地优先级的通告报文后，不会立即抢占成为]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器，而是等待一定时间后，才会重新选举新的]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18718_x1832_633950131}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18718_x1832_1915716149}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_1190391294}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[工作在抢占方式，抢占延迟时间为]{style="font-family:宋体"}[5000]{lang="EN-US"}[厘秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_609745826}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] vrrp vrid 1 preempt-mode delay 5000]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18718_x1832_x143092270}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_x1836898511}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[工作在抢占方式，抢占延迟时间为]{style="font-family:宋体"}[5000]{lang="EN-US"}[厘秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_259076990}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] vrrp vrid 1 preempt-mode delay 5000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_551498393}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **vrrp**]{lang="EN-US"}]{#struct_0_18718_x1832_1990956361}
:::

::: {#-1200911630 .myid}
[]{#_Toc404795938}[]{#struct_0_18718_x1832_x1877000002}[]{#_Toc211671364}[]{#_Toc99954754}[]{#_Toc34483421}[]{#_Toc33425590}[]{#_Toc31785780}

**VRRP \-- IPv4 VRRP配置命令 \-- vrrp vrid priority**

------------------------------------------------------------------------

[**[vrrp vrid priority]{lang="EN-US"}**]{#struct_0_18718_x1832_397715651}[命令用来设置路由器在]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组中的优先级。]{style="font-family:宋体"}

[**[undo vrrp vrid priority]{lang="EN-US"}**]{#struct_0_18718_x1832_609680290}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x535538950}

[**[vrrp vrid]{lang="EN-US"}***[ virtual-router-id]{lang="EN-US"}*[ **priority** *priority-value*]{lang="EN-US"}]{#struct_0_18718_x1832_2081654606}

[**[undo vrrp vrid]{lang="EN-US"}**[ *virtual-router-id* **priority**]{lang="EN-US"}]{#struct_0_18718_x1832_430783903}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x530110735}

[[路由器在]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_1165877776}[备份组中的优先级为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18718_x1832_436962054}

[[接口视图]{style="font-family:宋体"}]{#struct_0_18718_x1832_1624653707}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1604096366}

[[network-admin]{lang="EN-US"}]{#struct_0_18718_x1832_x1631580891}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18718_x1832_609614754}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1346547558}

[*[virtual-router-id]{lang="EN-US"}*]{#struct_0_18718_x1832_1692662825}[：]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[priority-value]{lang="EN-US"}*]{#struct_0_18718_x1832_473329458}[：优先级的值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[254]{lang="EN-US"}[，该值越大表明优先级越高。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1297362421}

[[优先级决定了路由器在备份组中的地位。优先级越高，越有可能成为]{style="font-family:宋体"}[Master]{lang="EN-US"}]{#struct_0_18718_x1832_x1469485156}[路由器。优先级]{style="font-family:宋体"}[0]{lang="EN-US"}[是系统保留为特殊用途来使用的，]{style="font-family:宋体"}[255]{lang="EN-US"}[则是系统保留给]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址拥有者的。]{style="font-family:宋体"}

[[路由器为]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_18718_x1832_969741358}[地址拥有者时，其运行优先级始终为]{style="font-family:宋体"}[255]{lang="EN-US"}[，表明只要其工作正常，则为]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1770854391}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18718_x1832_x752482701}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_609549218}[设置路由器在]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[中的优先级为]{style="font-family:宋体"}[150]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_1112559990}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] vrrp vrid 1 priority 150]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18718_x1832_x761842488}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_x856421627}[设置交换机在]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[中的优先级为]{style="font-family:宋体"}[150]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_x93225488}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] vrrp vrid 1 priority 150]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1461981053}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **vrrp**]{lang="EN-US"}]{#struct_0_18718_x1832_1811203909}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vrrp]{lang="EN-US"}**[ **vrid** **track**]{lang="EN-US"}]{#struct_0_18718_x1832_x1426282602}
:::

::: {#1078263294 .myid}
[]{#_Toc404795939}[]{#struct_0_18718_x1832_610007970}

**VRRP \-- IPv4 VRRP配置命令 \-- vrrp vrid shutdown**

------------------------------------------------------------------------

[**[vrrp vrid ]{lang="EN-US"}[shutdown]{lang="EN-US"}**]{#struct_0_18718_x1832_x783081512}[命令用来关闭指定的]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组。]{style="font-family:宋体"}

[**[undo vrrp vrid shutdown]{lang="EN-US"}**]{#struct_0_18718_x1832_x700073823}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1163887644}

[**[vrrp vrid]{lang="EN-US"}***[ virtual-router-id]{lang="EN-US"}*[ **shutdown**]{lang="EN-US"}]{#struct_0_18718_x1832_x1239775014}

[**[undo vrrp vrid]{lang="EN-US"}**[ *virtual-router-id* **shutdown**]{lang="EN-US"}]{#struct_0_18718_x1832_x505546233}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1832573561}

[[IPv4 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_1242859789}[备份组处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x248685495}

[[接口视图]{style="font-family:宋体"}]{#struct_0_18718_x1832_609942434}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1565003028}

[[network-admin]{lang="EN-US"}]{#struct_0_18718_x1832_x970870370}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18718_x1832_x2141650176}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1875747071}

[*[virtual-router-id]{lang="EN-US"}*]{#struct_0_18718_x1832_x1815512140}[：]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x887882152}

[[关闭]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_607280179}[备份组功能通常用于暂时禁用备份组，但还需要再次启用该备份组的场景。关闭备份组后，该备份组的状态为]{style="font-family:宋体"}[Initialize]{lang="EN-US"}[，并且该备份组所有已存在的配置保持不变。在关闭状态下还可以对备份组进行配置。备份组再次被开启后，基于最新的配置，从]{style="font-family:宋体"}[Initialize]{lang="EN-US"}[状态重新开始运行。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18718_x1832_609483683}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18718_x1832_x818535063}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_x2040909743}[关闭]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_x468250041}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] vrrp vrid 1 shutdown]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18718_x1832_x269803362}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_x1709211753}[关闭]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_784241828}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] vrrp vrid 1 shutdown]{lang="EN-US"}
:::

::: {#2022749639 .myid}
[]{#_Toc404795940}[]{#struct_0_18718_x1832_609418147}

**VRRP \-- IPv4 VRRP配置命令 \-- vrrp vrid source-interface**

------------------------------------------------------------------------

[**[vrrp vrid source-interface]{lang="EN-US"}**]{#struct_0_18718_x1832_1863632429}[命令用来为]{style="font-family:
宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组指定源接口，该源接口用来代替]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组所在接口进行该备份组]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[报文的收发。]{style="font-family:宋体"}

[**[undo vrrp vrid source-interface]{lang="EN-US"}**]{#struct_0_18718_x1832_2084912318}[命令用来取消当前指定的源接口，]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[报文通过]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组所在接口进行收发。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x959676303}

[**[vrrp vrid]{lang="EN-US"}**[ *virtual-router-id* **source-interface** *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_18718_x1832_1514813225}

[**[undo vrrp vrid ]{lang="EN-US"}***[virtual-router-id]{lang="EN-US"}*[ **source-interface**]{lang="EN-US"}]{#struct_0_18718_x1832_813082189}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18718_x1832_304331530}

[[没有指定备份组的源接口，]{style="font-family:宋体"}[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_1917967650}[报文通过]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组所在接口进行收发。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x85886818}

[[接口视图]{style="font-family:宋体"}]{#struct_0_18718_x1832_609352611}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1113775208}

[[network-admin]{lang="EN-US"}]{#struct_0_18718_x1832_x768771486}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18718_x1832_1317836297}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1532039846}

[*[virtual-router-id]{lang="EN-US"}*]{#struct_0_18718_x1832_x414050531}[：]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_18718_x1832_x176369222}[：源接口的接口类型和接口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18718_x1832_2093082797}

[[因组网要求或网络故障，导致同一个]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_1228169967}[备份组中的设备不能通过备份组所在接口进行]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[协议报文交互时，可以使用本命令将其他能进行报文交互的接口设置为备份组源接口，用来代替备份组所在接口进行该备份组]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[报文的收发。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18718_x1832_609287075}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18718_x1832_1227897901}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_1354350141}[设置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上备份组的源接口为接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_x1577179856}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] vrrp vrid 10 source-interface gigabitethernet 1/0/2]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{style="font-family:宋体"}]{#struct_0_18718_x1832_x744931571}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_313951818}[设置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[10]{lang="EN-US"}[上备份组的源接口为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[20]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_464105934}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] vrrp vrid 10 source-interface vlan-interface 20]{lang="EN-US"}
:::

::: {#-1414685441 .myid}
[]{#_Toc404795941}[]{#struct_0_18718_x1832_382158913}[]{#_Toc211671365}[]{#_Toc99954755}[]{#_Toc34483422}[]{#_Toc33425591}[]{#_Toc31785781}

**VRRP \-- IPv4 VRRP配置命令 \-- vrrp vrid timer advertise**

------------------------------------------------------------------------

[**[vrrp vrid timer advertise]{lang="EN-US"}**]{#struct_0_18718_x1832_609745827}[命令用来设置]{style="font-family:
宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组中的]{style="font-family:
宋体"}[Master]{lang="EN-US"}[路由器发送]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文的时间间隔。]{style="font-family:宋体"}

[**[undo vrrp vrid timer advertise]{lang="EN-US"}**]{#struct_0_18718_x1832_x143092269}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1836439758}

[**[vrrp vrid ]{lang="EN-US"}***[virtual-router-id]{lang="EN-US"}***[ timer advertise ]{lang="EN-US"}***[adver-interval]{lang="EN-US"}*]{#struct_0_18718_x1832_764234219}

[**[undo vrrp vrid ]{lang="EN-US"}***[virtual-router-id]{lang="EN-US"}***[ timer advertise]{lang="EN-US"}**]{#struct_0_18718_x1832_x89177921}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1881738454}

[[IPv4 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x2125344194}[备份组中]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器发送]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文的时间间隔为]{style="font-family:宋体"}[100]{lang="EN-US"}[厘秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1982686872}

[[接口视图]{style="font-family:宋体"}]{#struct_0_18718_x1832_2133064734}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1327183409}

[[network-admin]{lang="EN-US"}]{#struct_0_18718_x1832_609680291}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18718_x1832_x535538949}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18718_x1832_2082113359}

[*[virtual-router-id]{lang="EN-US"}*]{#struct_0_18718_x1832_x2028800528}[：]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[adver-interval]{lang="EN-US"}*]{#struct_0_18718_x1832_271926250}[：备份组中的]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器发送]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文的间隔时间，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[4095]{lang="EN-US"}[，单位为厘秒。使用]{style="font-family:宋体"}[VRRPv2]{lang="EN-US"}[版本时，该参数的实际生效值只能是]{style="font-family:宋体"}[100]{lang="EN-US"}[的整倍数，例如，配置该参数取值在]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[、]{style="font-family:宋体"}[101]{lang="EN-US"}[～]{style="font-family:宋体"}[200]{lang="EN-US"}[、]{style="font-family:宋体"}[4001]{lang="EN-US"}[～]{style="font-family:宋体"}[4095]{lang="EN-US"}[范围内时，实际生效值分别为]{style="font-family:宋体"}[100]{lang="EN-US"}[、]{style="font-family:宋体"}[200]{lang="EN-US"}[、]{style="font-family:宋体"}[4100]{lang="EN-US"}[；使用]{style="font-family:宋体"}[VRRPv3]{lang="EN-US"}[版本时，该参数的实际生效值与所配置数值相同。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1976299733}

[[IPv4 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_695580550}[备份组中的]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器会定时发送]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文，通知备份组内的路由器自己工作正常。]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文的发送时间间隔为本命令配置的值。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_18718_x1832_x531250803}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[建议配置]{style="font-family:宋体"}]{#struct_0_18718_x1832_x762060304}[VRRP]{lang="EN-US"}[通告报文的发送间隔大于]{style="font-family:宋体"}[100]{lang="EN-US"}[厘秒，否则会对系统的稳定性产生影响。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_18718_x1832_609614755}[VRRPv2]{lang="EN-US"}[版本时，]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组中的所有路由器必须配置相同的]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文时间间隔。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_18718_x1832_1346547557}[VRRPv3]{lang="EN-US"}[版本时，]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组中的路由器上配置的]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文时间间隔可以不同。]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器根据自身配置的报文时间间隔定时发送通告报文，并在通告报文中携带]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器上配置的时间间隔；]{style="font-family:宋体"}[Backup]{lang="EN-US"}[路由器接收到]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器发送的通告报文后，记录报文中携带的]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器通告报文时间间隔，如果在]{style="font-family:宋体"}[3]{lang="EN-US"}[×记录的时间间隔＋]{style="font-family:宋体"}[Skew_Time]{lang="EN-US"}[内没有收到]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器发送的]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文，则认为]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器出现故障，重新选举]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[网络流量过大可能会导致]{style="font-family:宋体"}]{#struct_0_18718_x1832_1693121577}[Backup]{lang="EN-US"}[路由器在指定时间内没有收到]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器的]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文，从而发生状态转换。可以通过将]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文的发送时间间隔延长的办法来解决该问题。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x362683401}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18718_x1832_1632599895}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_691291323}[设置]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器发送]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文的间隔时间为]{style="font-family:宋体"}[500]{lang="EN-US"}[厘秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_2098563699}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] vrrp vrid 1 timer advertise 500]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18718_x1832_x337056139}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_609549219}[设置]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器发送]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文的间隔时间为]{style="font-family:宋体"}[500]{lang="EN-US"}[厘秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_1112559991}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] vrrp vrid 1 timer advertise 500]{lang="DA"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x761908024}

[[·[              ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **vrrp**]{lang="EN-US"}]{#struct_0_18718_x1832_x1602913070}
:::

::::: {#1216770826 .myid}
[]{#_Toc99954756}[]{#_Toc34483423}[]{#_Toc33425592}[]{#_Toc31785782}[]{#_Toc404795942}[]{#struct_0_18718_x1832_257882318}[]{#_Toc211671366}[]{#_Toc270693131}[]{#_Toc280174841}[]{#_Toc280177548}[]{#_Toc280281428}[]{#_Toc270693132}[]{#_Toc280174842}[]{#_Toc280177549}[]{#_Toc280281429}[]{#_Toc270693135}[]{#_Toc280174845}[]{#_Toc280177552}[]{#_Toc280281432}[]{#_Toc270693136}[]{#_Toc280174846}[]{#_Toc280177553}[]{#_Toc280281433}[]{#_Toc270693137}[]{#_Toc280174847}[]{#_Toc280177554}[]{#_Toc280281434}[]{#_Toc270693138}[]{#_Toc280174848}[]{#_Toc280177555}[]{#_Toc280281435}[]{#_Toc270693139}[]{#_Toc280174849}[]{#_Toc280177556}[]{#_Toc280281436}[]{#_Toc270693140}[]{#_Toc280174850}[]{#_Toc280177557}[]{#_Toc280281437}[]{#_Toc270693141}[]{#_Toc280174851}[]{#_Toc280177558}[]{#_Toc280281438}[]{#_Toc270693142}[]{#_Toc280174852}[]{#_Toc280177559}[]{#_Toc280281439}[]{#_Toc270693143}[]{#_Toc280174853}[]{#_Toc280177560}[]{#_Toc280281440}[]{#_Toc270693144}[]{#_Toc280174854}[]{#_Toc280177561}[]{#_Toc280281441}[]{#_Toc270693145}[]{#_Toc280174855}[]{#_Toc280177562}[]{#_Toc280281442}[]{#_Toc270693146}[]{#_Toc280174856}[]{#_Toc280177563}[]{#_Toc280281443}[]{#_Toc270693147}[]{#_Toc280174857}[]{#_Toc280177564}[]{#_Toc280281444}[]{#_Toc270693148}[]{#_Toc280174858}[]{#_Toc280177565}[]{#_Toc280281445}[]{#_Toc270693149}[]{#_Toc280174859}[]{#_Toc280177566}[]{#_Toc280281446}[]{#_Toc270693150}[]{#_Toc280174860}[]{#_Toc280177567}[]{#_Toc280281447}[]{#_Toc270693151}[]{#_Toc280174861}[]{#_Toc280177568}[]{#_Toc280281448}[]{#_Toc270693152}[]{#_Toc280174862}[]{#_Toc280177569}[]{#_Toc280281449}[]{#_Toc270693153}[]{#_Toc280174863}[]{#_Toc280177570}[]{#_Toc280281450}[]{#_Toc270693154}[]{#_Toc280174864}[]{#_Toc280177571}[]{#_Toc280281451}[]{#_Toc270693155}[]{#_Toc280174865}[]{#_Toc280177572}[]{#_Toc280281452}[]{#_Toc270693157}[]{#_Toc280174867}[]{#_Toc280177574}[]{#_Toc280281454}[]{#_Toc270693158}[]{#_Toc280174868}[]{#_Toc280177575}[]{#_Toc280281455}[]{#_Toc270693160}[]{#_Toc280174870}[]{#_Toc280177577}[]{#_Toc280281457}[]{#_Toc270693161}[]{#_Toc280174871}[]{#_Toc280177578}[]{#_Toc280281458}[]{#_Toc270693163}[]{#_Toc280174873}[]{#_Toc280177580}[]{#_Toc280281460}[]{#_Toc270693164}[]{#_Toc280174874}[]{#_Toc280177581}[]{#_Toc280281461}[]{#_Toc270693165}[]{#_Toc280174875}[]{#_Toc280177582}[]{#_Toc280281462}

**VRRP \-- IPv4 VRRP配置命令 \-- vrrp vrid track**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VRRP命令.files/image002.png){#图片 3 width="62" height="27"}]{lang="EN-US"}]{#struct_0_18718_x1832_1591450544}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_18718_x1832_500717604}
:::

**[ ]{lang="EN-US"}**

[**[vrrp vrid track]{lang="EN-US"}**]{#struct_0_18718_x1832_x2104230919}[命令用来配置监视指定的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项，即当]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的状态为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，立即将虚拟转发器切换为]{style="font-family:宋体"}[Active]{lang="EN-US"}[状态、降低路由器的优先级、立即切换成为]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器或降低本地虚拟转发器权重值。]{style="font-family:宋体"}

[**[undo vrrp vrid track]{lang="EN-US"}**]{#struct_0_18718_x1832_672065089}[命令用来取消监视指定的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_610007971}

[**[vrrp vrid]{lang="EN-US"}**[ *virtual-router-id* **track** *track-entry-number* { **forwarder-switchover** **member-ip** *ip-address* \| **priority reduced** \[ *priority-reduced* \] \| **switchover** \| **weight reduced** \[ *weight-reduced* \] }]{lang="EN-US"}]{#struct_0_18718_x1832_x783081511}

[**[undo vrrp vrid]{lang="EN-US"}**[ *virtual-router-id* **track** \[ *track-entry-number* \] \[ **forwarder-switchover** \| **priority reduced** \| **switchover** \| **weight reduced** \]]{lang="EN-US"}]{#struct_0_18718_x1832_x700139359}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x447215028}

[[没有指定被监视的]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_18718_x1832_592491225}[项。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18718_x1832_774900488}

[[接口视图]{style="font-family:宋体"}]{#struct_0_18718_x1832_x362063893}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18718_x1832_889421352}

[[network-admin]{lang="EN-US"}]{#struct_0_18718_x1832_x734260055}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18718_x1832_609942435}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1565003029}

[*[virtual-router-id]{lang="EN-US"}*]{#struct_0_18718_x1832_x970804834}[：]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[track-entry-number]{lang="EN-US"}*]{#struct_0_18718_x1832_993711472}[：被监视的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项序号，]{style="font-family:宋体"}*[track-entry-number]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[forwarder-switchover]{lang="EN-US"}**[ **member-ip** *ip-address*]{lang="EN-US"}]{#struct_0_18718_x1832_x556684730}[：虚拟转发器快速切换模式。当监视的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项状态变为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，如果本地设备上有处于]{style="font-family:宋体"}[Listening]{lang="EN-US"}[状态的虚拟转发器，且其对应的]{style="font-family:宋体"}[AVF]{lang="EN-US"}[地址为]{style="font-family:宋体"}**[member-ip]{lang="EN-US"}**[，则马上将该虚拟转发器切换到]{style="font-family:宋体"}[Active]{lang="EN-US"}[状态。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为备份组中成员设备的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。可以通过]{style="font-family:宋体"}**[display vrrp verbose]{lang="EN-US"}**[命令查看备份组中包含的成员设备。]{style="font-family:宋体"}

[**[priority reduced]{lang="EN-US"}**[ \[ *priority-reduced* \]]{lang="EN-US"}]{#struct_0_18718_x1832_1638408285}[：当监视的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项状态变为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，降低本地路由器在备份组中的优先级。优先级降低的数值为]{style="font-family:宋体"}*[priority-reduced]{lang="EN-US"}*[，]{style="font-family:宋体"}*[priority-reduced]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[switchover]{lang="EN-US"}**]{#struct_0_18718_x1832_1908592851}[：切换模式，当监视的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的状态变为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，如果本路由器在备份组中处于]{style="font-family:宋体"}[Backup]{lang="EN-US"}[状态，则马上切换成为]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器。]{style="font-family:宋体"}

[**[weight reduced ]{lang="EN-US"}**[\[ *weight-reduced* \]]{lang="EN-US"}]{#struct_0_18718_x1832_1422965110}[：当监视的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项状态变为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，当前路由器上属于指定]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[组的所有虚拟转发器的权重都降低指定的数值。权重降低的数值为]{style="font-family:宋体"}*[weight-reduced]{lang="EN-US"}*[，]{style="font-family:宋体"}*[weight-reduced]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1527462414}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_18718_x1832_609483680}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在执行本配置之前，需要先在接口上创建备份组并配置虚拟]{style="font-family:宋体"}]{#struct_0_18718_x1832_1017293382}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}**[undo vrrp vrid track]{lang="EN-US"}**]{#struct_0_18718_x1832_8955790}[命令时如果没有指定]{lang="EN-US" style="font-family:宋体"}*[track-entry-number]{lang="EN-US"}*[参数，则删除该备份组与所有]{lang="EN-US" style="font-family:宋体"}[Track]{lang="EN-US"}[项的关联。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有]{style="font-family:宋体"}]{#struct_0_18718_x1832_x115993062}[VRRP]{lang="EN-US"}[工作在负载均衡模式时，执行]{style="font-family:宋体"}**[forwarder-switchover]{lang="EN-US"}**[ **member-ip** *ip-address*]{lang="EN-US"}[或]{style="font-family:
宋体"}**[weight reduced ]{lang="EN-US"}**[\[ *weight-reduced* \]]{lang="EN-US"}[才会生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[虚拟转发器的权重值为]{style="font-family:宋体"}]{#struct_0_18718_x1832_x2046921429}[255]{lang="EN-US"}[，虚拟转发器的失效下限为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[由于]{style="font-family:宋体"}]{#struct_0_18718_x1832_x2064007392}[VF Owner]{lang="EN-US"}[的权重高于或等于失效下限时，它的优先级始终为]{style="font-family:宋体"}[255]{lang="EN-US"}[，不会根据虚拟转发器的权重改变。当监视的上行接口出现故障时，配置的权重降低数额需保证]{style="font-family:宋体"}[VF Owner]{lang="EN-US"}[的权重低于失效下限，即权重降低的数额大于]{style="font-family:宋体"}[245]{lang="EN-US"}[，其他的虚拟转发器才能接替]{style="font-family:宋体"}[VF Owner]{lang="EN-US"}[成为]{style="font-family:宋体"}[AVF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由器在某个备份组中作为]{style="font-family:宋体"}]{#struct_0_18718_x1832_x818535066}[IP]{lang="EN-US"}[地址拥有者时，]{style="font-family:宋体"}[如果在该路由器上执行]{lang="EN-US" style="font-family:宋体"}**[vrrp vrid track priority reduced]{lang="EN-US"}**[或]{lang="EN-US" style="font-family:宋体"}**[vrrp vrid track switchover]{lang="EN-US"}**[命令，]{lang="EN-US" style="font-family:宋体"}[则该配置不会生效。该路由器不再作为]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址拥有者后，之前的配置才会生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[被监视的]{style="font-family:宋体"}]{#struct_0_18718_x1832_x2040713135}[Track]{lang="EN-US"}[项的状态由]{style="font-family:宋体"}[Negative]{lang="EN-US"}[变为]{style="font-family:宋体"}[Positive]{lang="EN-US"}[或]{style="font-family:宋体"}[NotReady]{lang="EN-US"}[后，对应的路由器优先级会自动恢复、对应虚拟转发器的权重会自动恢复、故障恢复后的原]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器会重新抢占为]{style="font-family:宋体"}[Master]{lang="EN-US"}[状态、故障恢复后的原]{style="font-family:宋体"}[AVF]{lang="EN-US"}[会重新抢占为]{style="font-family:宋体"}[Active]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[被监视的]{style="font-family:宋体"}]{#struct_0_18718_x1832_x875598184}[Track]{lang="EN-US"}[项可以是未创建的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项。]{style="font-family:宋体"}[可以通过]{lang="EN-US" style="font-family:宋体"}**[vrrp vrid track]{lang="EN-US"}**[命令指定监视的]{lang="EN-US" style="font-family:宋体"}[Track]{lang="EN-US"}[项后，再通过]{lang="EN-US" style="font-family:宋体"}**[track]{lang="EN-US"}**[命令创建该]{lang="EN-US" style="font-family:宋体"}[Track]{lang="EN-US"}[项。]{lang="EN-US" style="font-family:宋体"}

[[Track]{lang="EN-US"}]{#struct_0_18718_x1832_x944939632}[项的详细介绍请参见"可靠性配置指导"中的"]{style="font-family:宋体"}[Track]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1110168795}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18718_x1832_1343880516}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_x2001714483}[在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上配置监视]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[，当]{style="font-family:
宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[状态为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[的优先级降低]{style="font-family:宋体"}[50]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_194533420}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] vrrp vrid 1 track 1 priority reduced 50]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_x939021754}[在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上配置虚拟转发器监视]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[，当]{style="font-family:
宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[状态为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，如果本地设备上]{style="font-family:宋体"}[AVF]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.1.3]{lang="EN-US"}[的虚拟转发器处于]{style="font-family:宋体"}[Listening]{lang="EN-US"}[状态，则马上将该虚拟转发器切换到]{style="font-family:宋体"}[Active]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_1796435215}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] vrrp vrid 1 track 1 forwarder-switchover member-ip 10.1.1.3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_x848316934}[在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上配置虚拟转发器权重监视]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[，当]{style="font-family:
宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[状态为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[所有虚拟转发器的权重都降低]{style="font-family:宋体"}[50]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> sysname-view]{lang="EN-US"}]{#struct_0_18718_x1832_1172460878}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] vrrp vrid 1 track 1 weight reduced 50]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18718_x1832_609418144}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_1863632432}[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[上配置监视]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[，当]{style="font-family:
宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[状态为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[上备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[的优先级降低]{style="font-family:宋体"}[50]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_2084191421}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] vrrp vrid 1 track 1 priority reduced 50]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_634956358}[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[上配置虚拟转发器监视]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[，当]{style="font-family:
宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[状态为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，如果本地设备上]{style="font-family:宋体"}[AVF]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.1.3]{lang="EN-US"}[的虚拟转发器处于]{style="font-family:宋体"}[Listening]{lang="EN-US"}[状态，则马上将该虚拟转发器切换到]{style="font-family:宋体"}[Active]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_x813256471}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] vrrp vrid 1 track 1 forwarder-switchover member-ip 10.1.1.3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_x63980758}[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[上配置虚拟转发器权重监视]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[，当]{style="font-family:
宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[状态为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[上]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[所有虚拟转发器的权重都降低]{style="font-family:宋体"}[50]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> sysname-view]{lang="EN-US"}]{#struct_0_18718_x1832_x469793459}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] vrrp vrid 1 track 1 weight reduced 50]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1723653929}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **vrrp**]{lang="EN-US"}]{#struct_0_18718_x1832_x403795604}
:::::

::: {#605393404 .myid}
[]{#_Toc404795944}[]{#struct_0_18718_x1832_x1817059611}[]{#_Toc211671370}[]{#_Toc128898004}

**VRRP \-- IPv6 VRRP配置命令 \-- display vrrp ipv6**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **vrrp ipv6**]{lang="EN-US"}]{#struct_0_18718_x1832_1339555774}[命令用来显示]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组的状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1168847508}

[**[display]{lang="EN-US"}**[ **vrrp ipv6** \[ **interface** *interface-type interface-number* \[ **vrid** *virtual-router-id* \] \] \[ **verbose** \] ]{lang="EN-US"}]{#struct_0_18718_x1832_1293981532}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x98245910}

[[任意视图]{style="font-family:宋体"}]{#struct_0_18718_x1832_609483681}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x818535065}

[[network-admin]{lang="EN-US"}]{#struct_0_18718_x1832_x2040516527}

[[network-operator]{lang="EN-US"}]{#struct_0_18718_x1832_1850246494}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18718_x1832_724396456}

[[mdc-operator]{lang="EN-US"}]{#struct_0_18718_x1832_186865867}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1002131797}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_18718_x1832_x259700716}[：显示指定接口的]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组状态信息。其中，]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}[为接口类型和接口编号。]{style="font-family:宋体"}

[**[vrid ]{lang="EN-US"}***[virtual-router-id]{lang="EN-US"}*]{#struct_0_18718_x1832_x484052307}[：显示指定]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组的状态信息。其中，]{style="font-family:宋体"}*[virtual-router-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_18718_x1832_609418145}[：显示]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组状态的详细信息。如果不指定本参数，则显示]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组状态的简要信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1863632431}

[[如果不指定接口名和备份组号，则显示该路由器上所有]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_2084388029}[备份组的状态信息；如果只指定接口名，不指定备份组号，则显示该接口上的所有]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组的状态信息；如果同时指定接口名和备份组号，则显示该接口上指定]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组的状态信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x2123709064}

[[\# VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x1380395935}[工作在标准协议模式时，显示全部]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display vrrp ipv6]{lang="EN-US"}]{#struct_0_18718_x1832_609352609}

[IPv6 Virtual Router Information:]{lang="EN-US"}

[ Running Mode      : Standard]{lang="EN-US"}

[ Total number of virtual routers : 1]{lang="EN-US"}

[ Interface          VRID  State        Running Adver   Auth     Virtual]{lang="EN-US"}

[                                       Pri     Timer   Type        IP]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ GE1/0/1            1     Master       150     100     None     FE80::1]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display vrrp ipv6]{lang="EN-US"}]{#struct_0_18718_x1832_1224876944}[命令显示信息描述表（标准协议模式）]{style="font-family:黑体"}

[]{#table_struct_0_x1780470139}[[字段]{style="font-family:黑体"}]{#struct_0_18718_x1832_x794539610}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_18718_x1832_496831633}

[[Running Mode]{lang="EN-US"}]{#struct_0_18718_x1832_1445395017}

[[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_308405801}[的工作模式，取值为]{style="font-family:宋体"}[Standard]{lang="EN-US"}[（标准协议模式）]{style="font-family:宋体"}

[[Total number of virtual routers]{lang="EN-US"}]{#struct_0_18718_x1832_x2116498921}

[[备份组的数目]{style="font-family:宋体"}]{#struct_0_18718_x1832_609287073}

[[Interface]{lang="EN-US"}]{#struct_0_18718_x1832_1227897907}

[[备份组所在接口名]{style="font-family:宋体"}]{#struct_0_18718_x1832_1354481213}

[[VRID]{lang="EN-US"}]{#struct_0_18718_x1832_1543548913}

[[虚拟路由器号（即备份组号）]{style="font-family:宋体"}]{#struct_0_18718_x1832_238217225}

[[State]{lang="EN-US"}]{#struct_0_18718_x1832_1142587733}

[[当前路由器在备份组中的状态，取值为]{style="font-family:宋体"}[Master]{lang="EN-US"}]{#struct_0_18718_x1832_609745825}[，]{style="font-family:宋体"}[Backup]{lang="EN-US"}[，]{style="font-family:宋体"}[Initialize]{lang="EN-US"}[或]{style="font-family:宋体"}[Inactive]{lang="EN-US"}

[[Running Pri]{lang="EN-US"}]{#struct_0_18718_x1832_x143092271}

[[路由器的运行优先级，即路由器当前的优先级。配置监视指定]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_18718_x1832_x1836964047}[项后，路由器的优先级会根据]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的状态改变]{style="font-family:宋体"}

[[Adver Timer]{lang="EN-US"}]{#struct_0_18718_x1832_x130613962}

[[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x496609422}[通告报文发送时间间隔，单位为厘秒]{style="font-family:宋体"}

[[Auth Type]{lang="EN-US"}]{#struct_0_18718_x1832_609680289}

[[认证类型，取值只能是]{style="font-family:宋体"}[None]{lang="EN-US"}]{#struct_0_18718_x1832_1420776179}[，表示无认证]{style="font-family:宋体"}

[[Virtual IP]{lang="EN-US"}]{#struct_0_18718_x1832_64440912}

[[备份组的虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_18718_x1832_1360439247}[地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_234496775}[工作在标准协议模式时，显示全部]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display vrrp ipv6 verbose]{lang="EN-US"}]{#struct_0_18718_x1832_609614753}

[IPv6 Virtual Router Information:]{lang="EN-US"}

[ Running Mode      : Standard]{lang="EN-US"}

[ Total number of virtual routers : 2]{lang="EN-US"}

[   Interface GigabitEthernet1/0/1]{lang="EN-US"}

[     VRID           : 1                    Adver Timer  : 100]{lang="EN-US"}

[     Admin Status   : Up                   State        : Master]{lang="EN-US"}

[     Config Pri     : 150                  Running Pri  : 150]{lang="EN-US"}

[     Preempt Mode   : Yes                  Delay Time   : 10]{lang="EN-US"}

[     Auth Type      : None]{lang="EN-US"}

[     Virtual IP     : FE80::1]{lang="EN-US"}

[     Virtual MAC    : 0000-5e00-0201]{lang="EN-US"}

[     Master IP      : FE80::2]{lang="EN-US"}

[   VRRP Track Information:]{lang="EN-US"}

[     Track Object   : 1                    State : Positive   Pri Reduced : 50]{lang="EN-US"}

[   Interface GigabitEthernet1/0/1]{lang="EN-US"}

[     VRID           : 11                   Adver Timer  : 100]{lang="EN-US"}

[     Admin Status   : Up                   State        : Backup]{lang="EN-US"}

[     Config Pri     : 80                   Running Pri  : 80]{lang="EN-US"}

[     Preempt Mode   : Yes                  Delay Time   : 0]{lang="EN-US"}

[     Become Master  : 2450ms left]{lang="EN-US"}

[     Auth Type      : None]{lang="EN-US"}

[     Virtual IP     : FE80::11]{lang="EN-US"}

[     Virtual MAC    : 0000-5e00-020b]{lang="EN-US"}

[     Master IP      : FE80::12]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display vrrp ipv6 verbose]{lang="EN-US"}]{#struct_0_18718_x1832_1346547551}[命令显示信息描述表（标准协议模式）]{style="font-family:黑体"}

[]{#table_struct_0_x1785900201}[[字段]{style="font-family:黑体"}]{#struct_0_18718_x1832_1693252649}

[[描述]{style="font-family:黑体"}]{#struct_0_18718_x1832_609549217}

[[Running Mode]{lang="EN-US"}]{#struct_0_18718_x1832_1112559989}

[[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x761383737}[的工作模式，取值为]{style="font-family:宋体"}[Standard]{lang="EN-US"}[（标准协议模式）]{style="font-family:宋体"}

[[Total number of virtual routers]{lang="EN-US"}]{#struct_0_18718_x1832_x58491184}

[[备份组的数目]{style="font-family:宋体"}]{#struct_0_18718_x1832_x1051674139}

[[Interface]{lang="EN-US"}]{#struct_0_18718_x1832_610007969}

[[备份组所在接口名]{style="font-family:宋体"}]{#struct_0_18718_x1832_1173233633}

[[VRID]{lang="EN-US"}]{#struct_0_18718_x1832_x432428575}

[[虚拟路由器号（即备份组号）]{style="font-family:宋体"}]{#struct_0_18718_x1832_x1910929552}

[[Adver Timer]{lang="EN-US"}]{#struct_0_18718_x1832_798948909}

[[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x1716966206}[通告报文发送时间间隔，单位为厘秒]{style="font-family:宋体"}

[[Admin Status]{lang="EN-US"}]{#struct_0_18718_x1832_609942433}

[[管理状态，包括]{style="font-family:宋体"}[Up]{lang="EN-US"}]{#struct_0_18718_x1832_1565003027}[和]{style="font-family:宋体"}[Down]{lang="EN-US"}[两种状态]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_18718_x1832_x971722338}

[[当前路由器在备份组中的状态，取值为]{style="font-family:宋体"}[Master]{lang="EN-US"}]{#struct_0_18718_x1832_192539611}[，]{style="font-family:宋体"}[Backup]{lang="EN-US"}[，]{style="font-family:宋体"}[Initialize]{lang="EN-US"}[或]{style="font-family:宋体"}[Inactive]{lang="EN-US"}

[[Config Pri]{lang="EN-US"}]{#struct_0_18718_x1832_1589267150}

[[路由器的配置优先级，即通过]{style="font-family:宋体"}**[vrrp ipv6 vrid priority]{lang="EN-US"}**]{#struct_0_18718_x1832_x2119399671}[命令指定的路由器优先级]{style="font-family:宋体"}

[[Running Pri]{lang="EN-US"}]{#struct_0_18718_x1832_209621391}

[[路由器的运行优先级，即路由器当前的优先级，配置监视指定]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_18718_x1832_1032711706}[项后，路由器的优先级会根据]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的状态改变]{style="font-family:宋体"}

[[Preempt Mode]{lang="EN-US"}]{#struct_0_18718_x1832_x30760929}

[[抢占模式，取值包括：]{style="font-family:宋体"}]{#struct_0_18718_x1832_x905966818}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Yes]{lang="EN-US"}]{#struct_0_18718_x1832_x2119465207}[：路由器工作在抢占模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No]{lang="EN-US"}]{#struct_0_18718_x1832_x2124617788}[：路由器工作在非抢占模式]{style="font-family:宋体"}

[[Become Master]{lang="EN-US"}]{#struct_0_18718_x1832_x803706160}

[[切换到]{style="font-family:宋体"}[Master]{lang="EN-US"}]{#struct_0_18718_x1832_x174073159}[状态需要等待的时间，单位为毫秒，只有处于]{style="font-family:宋体"}[Backup]{lang="EN-US"}[状态时才会显示此信息]{style="font-family:宋体"}

[[Delay Time]{lang="EN-US"}]{#struct_0_18718_x1832_999650865}

[[抢占延迟时间，单位为厘秒]{style="font-family:宋体"}]{#struct_0_18718_x1832_x2119530743}

[[Auth Type]{lang="EN-US"}]{#struct_0_18718_x1832_x759736180}

[[认证类型，取值只能是]{style="font-family:宋体"}[None]{lang="EN-US"}]{#struct_0_18718_x1832_198522641}[，表示无认证]{style="font-family:宋体"}

[[Virtual IP]{lang="EN-US"}]{#struct_0_18718_x1832_1253990633}

[[备份组的虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_18718_x1832_1465852905}[地址]{style="font-family:宋体"}

[[Virtual MAC]{lang="EN-US"}]{#struct_0_18718_x1832_x2119596279}

[[备份组虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_18718_x1832_x1097077573}[地址对应的虚拟]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。只在路由器为]{style="font-family:宋体"}[Master]{lang="EN-US"}[状态时，才会显示此信息]{style="font-family:宋体"}

[[Master IP]{lang="EN-US"}]{#struct_0_18718_x1832_1148664629}

[[处于]{style="font-family:宋体"}[Master]{lang="EN-US"}]{#struct_0_18718_x1832_899117350}[状态的路由器所对应接口的链路本地地址]{style="font-family:宋体"}

[[VRRP Track Information]{lang="EN-US"}]{#struct_0_18718_x1832_x2119137527}

[[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_1976314618}[备份组监视的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项信息。执行]{style="font-family:宋体"}**[vrrp ipv6 vrid track]{lang="EN-US"}**[命令后，才会显示此信息]{style="font-family:宋体"}

[[Track Object]{lang="EN-US"}]{#struct_0_18718_x1832_180750231}

[[监视的]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_18718_x1832_1951676946}[项]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_18718_x1832_x2119203063}

[[Track]{lang="EN-US"}]{#struct_0_18718_x1832_1306211064}[项的状态，]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的状态可包括]{style="font-family:宋体"}[Negative]{lang="EN-US"}[、]{style="font-family:宋体"}[Positive]{lang="EN-US"}[和]{style="font-family:宋体"}[NotReady]{lang="EN-US"}

[[Pri Reduced]{lang="EN-US"}]{#struct_0_18718_x1832_x1667327799}

[[监视的]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_18718_x1832_2058428203}[项状态为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，优先级降低的数额]{style="font-family:宋体"}

[[Switchover]{lang="EN-US"}]{#struct_0_18718_x1832_x2119268599}

[[快速切换，显示此信息时表示当监视的]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_18718_x1832_x1260222647}[项变为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[状态时，]{style="font-family:宋体"}[Backup]{lang="EN-US"}[路由器会马上抢占成为]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_1412206277}[工作在负载均衡模式时，显示全部]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display vrrp ipv6]{lang="EN-US"}]{#struct_0_18718_x1832_x2009469282}

[IPv6 Virtual Router Information:]{lang="EN-US"}

[ Running Mode      : Load Balance]{lang="EN-US"}

[ Total number of virtual routers : 1]{lang="EN-US"}

[ Interface          VRID  State        Running Address             Active]{lang="EN-US"}

[                                       Pri]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ GE1/0/1            1     Master       150     FE80::1             Local]{lang="EN-US"}

[ \-\-\-\--              VF 1  Active       255     000f-e2ff-4011      Local]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display vrrp ipv6]{lang="EN-US"}]{#struct_0_18718_x1832_x829962826}[命令显示信息描述表（负载均衡模式）]{style="font-family:黑体"}

[]{#table_struct_0_x1787881955}[[字段]{style="font-family:黑体"}]{#struct_0_18718_x1832_239266545}

[[描述]{style="font-family:黑体"}]{#struct_0_18718_x1832_x2119334135}

[[Running Mode]{lang="EN-US"}]{#struct_0_18718_x1832_x1017310156}

[[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x1060105776}[的工作模式，取值为]{style="font-family:宋体"}[Load Balance]{lang="EN-US"}[（负载均衡模式）]{style="font-family:宋体"}

[[Total number of virtual routers]{lang="EN-US"}]{#struct_0_18718_x1832_x1075554651}

[[备份组的数目]{style="font-family:宋体"}]{#struct_0_18718_x1832_x1168839395}

[[Interface]{lang="EN-US"}]{#struct_0_18718_x1832_x823407284}

[[备份组所在接口名]{style="font-family:宋体"}]{#struct_0_18718_x1832_x2118875383}

[[VRID]{lang="EN-US"}]{#struct_0_18718_x1832_x660768611}

[[虚拟路由器号（即备份组号）]{style="font-family:宋体"}*[number]{lang="EN-US"}*]{#struct_0_18718_x1832_983989389}[或虚拟转发器编号]{style="font-family:宋体"}[VF *number*]{lang="EN-US"}

[[State]{lang="EN-US"}]{#struct_0_18718_x1832_x1152014275}

[[对于虚拟备份组（]{style="font-family:宋体"}[VRID]{lang="EN-US"}]{#struct_0_18718_x1832_1588976665}[为]{style="font-family:宋体"}*[number]{lang="EN-US"}*[），该字段表示当前路由器在备份组中的状态，取值为]{style="font-family:宋体"}[Master]{lang="EN-US"}[，]{style="font-family:宋体"}[Backup]{lang="EN-US"}[，]{style="font-family:宋体"}[Initialize]{lang="EN-US"}[或]{style="font-family:宋体"}[Inactive]{lang="EN-US"}

[[对于虚拟转发器（]{style="font-family:宋体"}[VRID]{lang="EN-US"}]{#struct_0_18718_x1832_x1357422714}[为]{style="font-family:宋体"}[VF *number*]{lang="EN-US"}[），该字段表示虚拟转发器的状态，取值为]{style="font-family:宋体"}[Active]{lang="EN-US"}[、]{style="font-family:宋体"}[Listening]{lang="EN-US"}[或]{style="font-family:宋体"}[Initialize]{lang="EN-US"}

[[Running Pri]{lang="EN-US"}]{#struct_0_18718_x1832_x2118940919}

[[对于虚拟备份组（]{style="font-family:宋体"}[VRID]{lang="EN-US"}]{#struct_0_18718_x1832_1658296168}[为]{style="font-family:宋体"}*[number]{lang="EN-US"}*[），该字段表示路由器的运行优先级，即路由器当前的优先级，配置监视指定]{style="font-family:宋体"}[Track]{lang="EN-US"}[项后，路由器的优先级会根据]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的状态改变]{style="font-family:宋体"}

[[对于虚拟转发器（]{style="font-family:宋体"}[VRID]{lang="EN-US"}]{#struct_0_18718_x1832_x431694}[为]{style="font-family:宋体"}[VF *number*]{lang="EN-US"}[），该字段表示虚拟转发器的运行优先级，即虚拟转发器当前的优先级，配置监视指定]{style="font-family:宋体"}[Track]{lang="EN-US"}[项后，虚拟转发器的优先级会根据]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的状态改变]{style="font-family:宋体"}

[[Address]{lang="EN-US"}]{#struct_0_18718_x1832_1581724012}

[[对于虚拟备份组（]{style="font-family:宋体"}[VRID]{lang="EN-US"}]{#struct_0_18718_x1832_332614011}[为]{style="font-family:宋体"}*[number]{lang="EN-US"}*[），该字段表示备份组的虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[对于虚拟转发器（]{style="font-family:宋体"}[VRID]{lang="EN-US"}]{#struct_0_18718_x1832_1967205184}[为]{style="font-family:宋体"}[VF *number*]{lang="EN-US"}[），该字段表示虚拟转发器的虚拟]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Active]{lang="EN-US"}]{#struct_0_18718_x1832_x2119399670}

[[对于虚拟备份组（]{style="font-family:宋体"}[VRID]{lang="EN-US"}]{#struct_0_18718_x1832_x1356462550}[为]{style="font-family:宋体"}*[number]{lang="EN-US"}*[），该字段表示]{style="font-family:宋体"}[Master]{lang="EN-US"}[的接口的链路本地地址，当前路由器为]{style="font-family:宋体"}[Master]{lang="EN-US"}[时，显示为]{style="font-family:宋体"}[local]{lang="EN-US"}

[[对于虚拟转发器（]{style="font-family:宋体"}[VRID]{lang="EN-US"}]{#struct_0_18718_x1832_x1991042354}[为]{style="font-family:宋体"}[VF *number*]{lang="EN-US"}[），该字段表示]{style="font-family:宋体"}[AVF]{lang="EN-US"}[的接口的链路本地地址，当前虚拟转发器为]{style="font-family:宋体"}[AVF]{lang="EN-US"}[时，显示为]{style="font-family:宋体"}[local]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_1538098250}[工作在负载均衡模式时，显示全部]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display vrrp ipv6 verbose]{lang="EN-US"}]{#struct_0_18718_x1832_x2119530742}

[IPv6 Virtual Router Information:]{lang="EN-US"}

[ Running Mode      : Load Balance]{lang="EN-US"}

[ Total number of virtual routers : 2]{lang="EN-US"}

[   Interface GigabitEthernet1/0/1]{lang="EN-US"}

[     VRID           : 1                    Adver Timer  : 100]{lang="EN-US"}

[     Admin Status   : Up                   State        : Master]{lang="EN-US"}

[     Config Pri     : 150                  Running Pri  : 150]{lang="EN-US"}

[     Preempt Mode   : Yes                  Delay Time   : 5]{lang="EN-US"}

[     Auth Type      : None]{lang="EN-US"}

[     Virtual IP     : FE80::10]{lang="EN-US"}

[     Member IP List : FE80::3 (Local, Master)]{lang="EN-US"}

[                      FE80::2 (Backup)]{lang="EN-US"}

[     Master IP      : FE80::3]{lang="EN-US"}

[   VRRP Track Information:]{lang="EN-US"}

[     Track Object   : 1                    State : Positive   Pri Reduced : 50]{lang="EN-US"}

[   Forwarder Information: 2 Forwarders 1 Active]{lang="EN-US"}

[     Config Weight  : 255]{lang="EN-US"}

[     Running Weight : 255]{lang="EN-US"}

[    Forwarder 01]{lang="EN-US"}

[     State          : Active]{lang="EN-US"}

[     Virtual MAC    : 000f-e2ff-4011 (Owner)]{lang="EN-US"}

[     Owner ID       : 0000-5e01-1101]{lang="EN-US"}

[     Priority       : 255]{lang="EN-US"}

[     Active         : local]{lang="EN-US"}

[    Forwarder 02]{lang="EN-US"}

[     State          : Listening]{lang="EN-US"}

[     Virtual MAC    : 000f-e2ff-4012 (Learnt)]{lang="EN-US"}

[     Owner ID       : 0000-5e01-1103]{lang="EN-US"}

[     Priority       : 127]{lang="EN-US"}

[     Active         : FE80::2]{lang="EN-US"}

[   Forwarder Weight Track Information:]{lang="EN-US"}

[     Track Object   : 1          State : Positive   Weight Reduced : 250]{lang="EN-US"}

[   Interface GigabitEthernet1/0/1]{lang="EN-US"}

[     VRID           : 11                   Adver Timer  : 100]{lang="EN-US"}

[     Admin Status   : Up                   State        : Backup]{lang="EN-US"}

[     Config Pri     : 80                   Running Pri  : 80]{lang="EN-US"}

[     Preempt Mode   : Yes                  Delay Time   : 0]{lang="EN-US"}

[     Become Master  : 2450ms left]{lang="EN-US"}

[     Auth Type      : None]{lang="EN-US"}

[     Virtual IP     : FE80::11]{lang="EN-US"}

[     Member IP List : FE80::3 (Local, Backup)]{lang="EN-US"}

[                      FE80::2 (Master)]{lang="EN-US"}

[     Master IP      : FE80::2]{lang="EN-US"}

[   Forwarder Information: 2 Forwarders 1 Active]{lang="EN-US"}

[     Config Weight  : 255]{lang="EN-US"}

[     Running Weight : 255]{lang="EN-US"}

[    Forwarder 01]{lang="EN-US"}

[     State          : Active]{lang="EN-US"}

[     Virtual MAC    : 000f-e2ff-40b1 (Learnt)]{lang="EN-US"}

[     Owner ID       : 0000-5e01-1103]{lang="EN-US"}

[     Priority       : 127]{lang="EN-US"}

[     Active         : FE80::2]{lang="EN-US"}

[    Forwarder 02]{lang="EN-US"}

[     State          : Listening]{lang="EN-US"}

[     Virtual MAC    : 000f-e2ff-40b2 (Owner)]{lang="EN-US"}

[     Owner ID       : 0000-5e01-1101]{lang="EN-US"}

[     Priority       : 255]{lang="EN-US"}

[     Active         : local]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[display vrrp ipv6 verbose]{lang="EN-US"}]{#struct_0_18718_x1832_1969147175}[命令显示信息描述表（负载均衡模式）]{style="font-family:黑体"}

[]{#table_struct_0_x1791035227}[[字段]{style="font-family:黑体"}]{#struct_0_18718_x1832_x2119596278}

[[描述]{style="font-family:黑体"}]{#struct_0_18718_x1832_1631805782}

[[Running Mode]{lang="EN-US"}]{#struct_0_18718_x1832_1646578963}

[[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_441706504}[的工作模式，取值为]{style="font-family:宋体"}[Load Balance]{lang="EN-US"}[（负载均衡模式）]{style="font-family:宋体"}

[[Total number of virtual routers]{lang="EN-US"}]{#struct_0_18718_x1832_1658277359}

[[备份组的数目]{style="font-family:宋体"}]{#struct_0_18718_x1832_1211561242}

[[Interface]{lang="EN-US"}]{#struct_0_18718_x1832_x2119137526}

[[备份组所在接口名]{style="font-family:宋体"}]{#struct_0_18718_x1832_410230677}

[[VRID]{lang="EN-US"}]{#struct_0_18718_x1832_x1666451465}

[[虚拟路由器号（即备份组号）]{style="font-family:宋体"}]{#struct_0_18718_x1832_1080842414}

[[Adver Timer]{lang="EN-US"}]{#struct_0_18718_x1832_72387891}

[[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x2119203062}[通告报文发送时间间隔，单位为厘秒]{style="font-family:宋体"}

[[Admin Status]{lang="EN-US"}]{#struct_0_18718_x1832_x1422672291}

[[管理状态，包括]{style="font-family:宋体"}[Up]{lang="EN-US"}]{#struct_0_18718_x1832_129248975}[和]{style="font-family:宋体"}[Down]{lang="EN-US"}[两种状态]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_18718_x1832_x2006434127}

[[当前路由器在备份组中的状态，取值为]{style="font-family:宋体"}[Master]{lang="EN-US"}]{#struct_0_18718_x1832_475220222}[，]{style="font-family:宋体"}[Backup]{lang="EN-US"}[，]{style="font-family:宋体"}[Initialize]{lang="EN-US"}[或]{style="font-family:宋体"}[Inactive]{lang="EN-US"}

[[Config Pri]{lang="EN-US"}]{#struct_0_18718_x1832_x2119268598}

[[路由器的配置优先级，即通过]{style="font-family:宋体"}**[vrrp ipv6 vrid priority]{lang="EN-US"}**]{#struct_0_18718_x1832_305861294}[命令指定的路由器优先级]{style="font-family:宋体"}

[[Running Pri]{lang="EN-US"}]{#struct_0_18718_x1832_4535199}

[[路由器的运行优先级，即路由器当前的优先级，配置监视指定]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_18718_x1832_2063742199}[项后，路由器的优先级会根据]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的状态改变]{style="font-family:宋体"}

[[Preempt Mode]{lang="EN-US"}]{#struct_0_18718_x1832_x1524682663}

[[抢占模式，取值包括：]{style="font-family:宋体"}]{#struct_0_18718_x1832_x2119334134}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Yes]{lang="EN-US"}]{#struct_0_18718_x1832_1711573199}[：路由器工作在抢占模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No]{lang="EN-US"}]{#struct_0_18718_x1832_x1048664393}[：路由器工作在非抢占模式]{style="font-family:宋体"}

[[Delay Time]{lang="EN-US"}]{#struct_0_18718_x1832_x306753219}

[[抢占延迟时间，单位为厘秒]{style="font-family:宋体"}]{#struct_0_18718_x1832_x2118875382}

[[Become Master]{lang="EN-US"}]{#struct_0_18718_x1832_2068114744}

[[切换到]{style="font-family:宋体"}[Master]{lang="EN-US"}]{#struct_0_18718_x1832_x771024558}[状态需要等待的时间，单位为毫秒，只有处于]{style="font-family:宋体"}[Backup]{lang="EN-US"}[状态时才会显示此信息]{style="font-family:宋体"}

[[Auth Type]{lang="EN-US"}]{#struct_0_18718_x1832_x723987453}

[[认证类型，取值只能是]{style="font-family:宋体"}[None]{lang="EN-US"}]{#struct_0_18718_x1832_x2118940918}[，表示无认证]{style="font-family:宋体"}

[[Virtual IP]{lang="EN-US"}]{#struct_0_18718_x1832_x1070587187}

[[备份组的虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_18718_x1832_x2070279398}[地址列表]{style="font-family:宋体"}

[[Member IP List]{lang="EN-US"}]{#struct_0_18718_x1832_99462180}

[[备份组中成员设备的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_18718_x1832_x344204837}[地址列表：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Local]{lang="EN-US"}]{#struct_0_18718_x1832_x2119399673}[：表示本地设备的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Master]{lang="EN-US"}]{#struct_0_18718_x1832_1372420805}[：表示处于]{lang="EN-US" style="font-family:宋体"}[Master]{lang="EN-US"}[状态的成员设备的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backup]{lang="EN-US"}]{#struct_0_18718_x1832_x1707068285}[：表示处于]{style="font-family:宋体"}[Backup]{lang="EN-US"}[状态的成员设备的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[VRRP Track Information]{lang="EN-US"}]{#struct_0_18718_x1832_x1517353858}

[[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x2119465209}[备份组监视的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项信息，执行]{style="font-family:宋体"}**[vrrp ipv6 vrid track]{lang="EN-US"}**[命令后，才会显示此信息]{style="font-family:宋体"}

[[Track Object]{lang="EN-US"}]{#struct_0_18718_x1832_x1674279094}

[[监视的]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_18718_x1832_x1455563527}[项，执行]{style="font-family:宋体"}**[vrrp ipv6 vrid track]{lang="EN-US"}**[命令后，才会显示此信息]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_18718_x1832_x540308477}

[[Track]{lang="EN-US"}]{#struct_0_18718_x1832_x2119530745}[项的状态，]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的状态包括]{style="font-family:宋体"}[Negative]{lang="EN-US"}[、]{style="font-family:宋体"}[Positive]{lang="EN-US"}[和]{style="font-family:宋体"}[NotReady]{lang="EN-US"}

[[Pri Reduced]{lang="EN-US"}]{#struct_0_18718_x1832_x1566305234}

[[监视的]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_18718_x1832_x925234207}[项状态为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，优先级降低的数额，执行]{style="font-family:宋体"}**[vrrp ipv6 vrid track]{lang="EN-US"}**[命令后，才会显示此信息]{style="font-family:宋体"}

[[Switchover]{lang="EN-US"}]{#struct_0_18718_x1832_x1159385526}

[[快速切换，显示此信息时表示当监视的]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_18718_x1832_x2119596281}[项变为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[状态时，]{style="font-family:宋体"}[Backup]{lang="EN-US"}[路由器会马上抢占成为]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器]{style="font-family:宋体"}

[[Forwarder Information: 2 Forwarders 1 Active]{lang="EN-US"}]{#struct_0_18718_x1832_x739995245}

[[虚拟转发器信息：路由器的虚拟转发器数目为]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_18718_x1832_1657576428}[，处于]{style="font-family:宋体"}[Active]{lang="EN-US"}[状态的虚拟转发器数目为]{style="font-family:宋体"}[1]{lang="EN-US"}

[[Config Weight]{lang="EN-US"}]{#struct_0_18718_x1832_1405315277}

[[虚拟转发器的配置权重，取值为]{style="font-family:宋体"}[255]{lang="EN-US"}]{#struct_0_18718_x1832_x2119137529}

[[Running Weight]{lang="EN-US"}]{#struct_0_18718_x1832_1169745564}

[[虚拟转发器的运行权重，即虚拟转发器当前的权重，配置监视指定]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_18718_x1832_x1769497992}[项后，虚拟转发器的权重会根据]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的状态改变]{style="font-family:宋体"}

[[Forwarder 01]{lang="EN-US"}]{#struct_0_18718_x1832_x2119203065}

[[虚拟转发器]{style="font-family:宋体"}[01]{lang="EN-US"}]{#struct_0_18718_x1832_143411650}[的信息]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_18718_x1832_x1629148218}

[[虚拟转发器的状态，取值为]{style="font-family:宋体"}[Active]{lang="EN-US"}]{#struct_0_18718_x1832_x2119268601}[、]{style="font-family:宋体"}[Listening]{lang="EN-US"}[或]{style="font-family:宋体"}[Initialize]{lang="EN-US"}

[[Virtual MAC]{lang="EN-US"}]{#struct_0_18718_x1832_x903402466}

[[虚拟转发器的虚拟]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_18718_x1832_394004530}[地址]{style="font-family:宋体"}

[[Owner ID]{lang="EN-US"}]{#struct_0_18718_x1832_1529666947}

[[虚拟转发器拥有者的接口实际]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_18718_x1832_x2119334137}[地址]{style="font-family:宋体"}

[[Priority]{lang="EN-US"}]{#struct_0_18718_x1832_2114857726}

[[虚拟转发器的优先级，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_18718_x1832_x2070909895}[～]{style="font-family:宋体"}[255]{lang="EN-US"}

[[Active]{lang="EN-US"}]{#struct_0_18718_x1832_x2118875385}

[[AVF]{lang="EN-US"}]{#struct_0_18718_x1832_x1823568025}[的接口的链路本地地址，当前转发器为]{style="font-family:宋体"}[AVF]{lang="EN-US"}[时，显示为]{style="font-family:宋体"}[local]{lang="EN-US"}

[[Forwarder Weight Track Configuration]{lang="EN-US"}]{#struct_0_18718_x1832_x2118940921}

[[虚拟转发器权重监视配置信息。执行]{style="font-family:宋体"}**[vrrp ipv6 vrid weight]{lang="EN-US"}**[ **track**]{lang="EN-US"}]{#struct_0_18718_x1832_2014329920}[命令后，才会显示此信息]{style="font-family:宋体"}

[[Track Object]{lang="EN-US"}]{#struct_0_18718_x1832_x273602496}

[[权重监视的]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_18718_x1832_x2119399672}[项。执行]{style="font-family:宋体"}**[vrrp ipv6 vrid weight]{lang="EN-US"}**[ **track**]{lang="EN-US"}[命令后，才会显示此信息]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_18718_x1832_x193663136}

[[Track]{lang="EN-US"}]{#struct_0_18718_x1832_x2079537005}[项的状态，]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的状态包括]{style="font-family:宋体"}[Negative]{lang="EN-US"}[、]{style="font-family:宋体"}[Positive]{lang="EN-US"}[和]{style="font-family:宋体"}[NotReady]{lang="EN-US"}

[[Weight Reduced]{lang="EN-US"}]{#struct_0_18718_x1832_x2119465208}

[[监视的]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_18718_x1832_x108195153}[项状态为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，权重降低的数额。执行]{style="font-family:宋体"}**[vrrp ipv6 vrid weight]{lang="EN-US"}**[ **track**]{lang="EN-US"}[命令后，才会显示此信息]{style="font-family:
  宋体"}

[ ]{lang="EN-US"}

::: {#1947501270 .myid}
[]{#_Toc404795945}[]{#struct_0_18718_x1832_x574212125}[]{#_Toc211671371}[]{#_Toc128898005}

**VRRP \-- IPv6 VRRP配置命令 \-- display vrrp ipv6 statistics**

------------------------------------------------------------------------

[**[display vrrp ipv6 statistics]{lang="EN-US"}**]{#struct_0_18718_x1832_x848368880}[命令用来显示]{style="font-family:
宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组的统计信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1633503795}

[**[display vrrp ipv6]{lang="EN-US"}***[ ]{lang="EN-US"}***[statistics]{lang="EN-US"}***[ ]{lang="EN-US"}*[\[ **interface** *interface-type interface-number* \[ **vrid** *virtual-router-id* \] \]]{lang="EN-US"}]{#struct_0_18718_x1832_x2119530744}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1162578121}

[[任意视图]{style="font-family:宋体"}]{#struct_0_18718_x1832_637251151}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1333419487}

[[network-admin]{lang="EN-US"}]{#struct_0_18718_x1832_1588110351}

[[network-operator]{lang="EN-US"}]{#struct_0_18718_x1832_569866069}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18718_x1832_x1146206105}

[[mdc-operator]{lang="EN-US"}]{#struct_0_18718_x1832_333531550}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x2119596280}

[**[interfac]{lang="EN-US"}[e]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_18718_x1832_1988888110}[：显示指定接口的]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组的统计信息。其中，]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}[为接口类型和接口编号。]{style="font-family:宋体"}

[**[vrid]{lang="EN-US"}**[ *virtual-router-id*]{lang="EN-US"}]{#struct_0_18718_x1832_1400623505}[：显示指定备份组号的]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组统计信息，其中，]{style="font-family:宋体"}*[virtual-router-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1990480115}

[[如果不输入接口名和备份组号，则显示该路由器上所有]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x1301444792}[备份组的统计信息；如果只输入接口名，不输入备份组号，则显示该接口上的所有]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组的统计信息；如果同时输入接口名和备份组号，则显示该接口上指定]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1228242598}

[[\# VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x1135403697}[工作在标准协议模式时，显示所有]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display vrrp ipv6 statistics]{lang="EN-US"}]{#struct_0_18718_x1832_x2119137528}

[ Interface               : GigabitEthernet1/0/1]{lang="EN-US"}

[ VRID                    : 1]{lang="EN-US"}

[ CheckSum Errors         : 0          Version Errors                : 0]{lang="EN-US"}

[ Invalid Pkts Rcvd       : 0          Unexpected Pkts Rcvd          : 0]{lang="EN-US"}

[ Hop Limit Errors        : 0          Advertisement Interval Errors : 0]{lang="EN-US"}

[ Invalid Auth Type       : 0          Auth Failures                 : 0]{lang="EN-US"}

[ Packet Length Errors    : 0          Auth Type Mismatch            : 0]{lang="EN-US"}

[ Become Master           : 1          Address List Errors           : 0]{lang="EN-US"}

[ Adver Rcvd              : 0          Priority Zero Pkts Rcvd       : 0]{lang="EN-US"}

[ Adver Sent              : 425        Priority Zero Pkts Sent       : 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Global statistics]{lang="EN-US"}

[ CheckSum Errors         : 0]{lang="EN-US"}

[ Version Errors          : 0]{lang="EN-US"}

[ VRID Errors             : 0]{lang="EN-US"}

[[\# VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x396338377}[工作在负载均衡模式时，显示全部]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display vrrp ipv6 statistics]{lang="EN-US"}]{#struct_0_18718_x1832_x2119203064}

[ Interface               : GigabitEthernet1/0/1]{lang="EN-US"}

[ VRID                    : 1]{lang="EN-US"}

[ CheckSum Errors         : 0          Version Errors                : 0]{lang="EN-US"}

[ Invalid Pkts Rcvd       : 0          Unexpected Pkts Rcvd          : 0]{lang="EN-US"}

[ Hop Limit Errors        : 0          Advertisement Interval Errors : 0]{lang="EN-US"}

[ Invalid Auth Type       : 0          Auth Failures                 : 0]{lang="EN-US"}

[ Packet Length Errors    : 0          Auth Type Mismatch            : 0]{lang="EN-US"}

[ Become Master           : 39         Address List Errors           : 0]{lang="EN-US"}

[ Become AVF              : 13         Packet Option Errors          : 0]{lang="EN-US"}

[ Adver Rcvd              : 2562       Priority Zero Pkts Rcvd       : 1 ]{lang="EN-US"}

[ Adver Sent              : 16373      Priority Zero Pkts Sent       : 49]{lang="EN-US"}

[ Request Rcvd            : 2          Reply Rcvd                    : 10]{lang="EN-US"}

[ Request Sent            : 12         Reply Sent                    : 2 ]{lang="EN-US"}

[ Release Rcvd            : 0          VF Priority Zero Pkts Rcvd    : 1 ]{lang="EN-US"}

[ Release Sent            : 0          VF Priority Zero Pkts Sent    : 11]{lang="EN-US"}

[ Redirect Timer Expires  : 1          Time-out Timer Expires        : 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Global statistics]{lang="EN-US"}

[ CheckSum Errors         : 0]{lang="EN-US"}

[ Version Errors          : 0]{lang="EN-US"}

[ VRID Errors             : 0]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[display vrrp ipv6 statistics]{lang="EN-US"}]{#struct_0_18718_x1832_1709495591}[显示信息描述表（标准协议模式）]{style="font-family:黑体"}

[]{#table_struct_0_x1772828417}[[字段]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1330943371}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1300559440}

[[Interface]{lang="EN-US"}]{#struct_0_18718_x1832_x2119268600}

[[备份组所在接口]{style="font-family:宋体"}]{#struct_0_18718_x1832_662681475}

[[VRID]{lang="EN-US"}]{#struct_0_18718_x1832_706430201}

[[备份组号]{style="font-family:宋体"}]{#struct_0_18718_x1832_302785308}

[[CheckSum Errors]{lang="EN-US"}]{#struct_0_18718_x1832_346654655}

[[校验和错误的报文数]{style="font-family:宋体"}]{#struct_0_18718_x1832_1427703630}

[[Version Errors]{lang="EN-US"}]{#struct_0_18718_x1832_x2119334136}

[[版本号错误的报文数]{style="font-family:宋体"}]{#struct_0_18718_x1832_548773785}

[[Invalid Pkts Rcvd]{lang="EN-US"}]{#struct_0_18718_x1832_136430819}

[[接收到报文类型错误的报文数]{style="font-family:宋体"}]{#struct_0_18718_x1832_769896208}

[[Unexpected Pkts Rcvd]{lang="EN-US"}]{#struct_0_18718_x1832_x1161996591}

[[接收到未期望的报文数]{style="font-family:宋体"}]{#struct_0_18718_x1832_x2118875384}

[[Advertisement Interval Errors]{lang="EN-US"}]{#struct_0_18718_x1832_905315330}

[[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x1081678551}[通告报文发送时间间隔错误的报文数]{style="font-family:宋体"}

[[Hop Limit Errors]{lang="EN-US"}]{#struct_0_18718_x1832_x1593552551}

[[跳数限制错误的报文数]{style="font-family:宋体"}]{#struct_0_18718_x1832_x2105127300}

[[Auth Failures]{lang="EN-US"}]{#struct_0_18718_x1832_x2118940920}

[[认证失败的报文数]{style="font-family:宋体"}]{#struct_0_18718_x1832_x714553435}

[[Invalid Auth Type]{lang="EN-US"}]{#struct_0_18718_x1832_1810789549}

[[认证类型无效的报文数]{style="font-family:宋体"}]{#struct_0_18718_x1832_472003845}

[[Auth Type Mismatch]{lang="EN-US"}]{#struct_0_18718_x1832_x1883847761}

[[认证类型不匹配的报文数]{style="font-family:宋体"}]{#struct_0_18718_x1832_1514812626}

[[Packet Length Errors]{lang="EN-US"}]{#struct_0_18718_x1832_x2119399675}

[[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x2115977437}[报文长度错误的报文数]{style="font-family:宋体"}

[[Address List Errors]{lang="EN-US"}]{#struct_0_18718_x1832_1038198161}

[[备份组虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_18718_x1832_258259414}[地址列表错误的报文数]{style="font-family:宋体"}

[[Become Master]{lang="EN-US"}]{#struct_0_18718_x1832_x2119465211}

[[成为]{style="font-family:宋体"}[Master]{lang="EN-US"}]{#struct_0_18718_x1832_x1318114270}[路由器的次数]{style="font-family:宋体"}

[[Priority Zero Pkts Rcvd]{lang="EN-US"}]{#struct_0_18718_x1832_x1698704081}

[[收到的优先级为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_18718_x1832_x1365158242}[的]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文的数目]{style="font-family:宋体"}

[[Adver Rcvd]{lang="EN-US"}]{#struct_0_18718_x1832_x2119530747}

[[收到的]{style="font-family:宋体"}[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_1565862648}[通告报文的数目]{style="font-family:宋体"}

[[Priority Zero Pkts Sent]{lang="EN-US"}]{#struct_0_18718_x1832_1754151933}

[[发送的优先级为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_18718_x1832_x1841254313}[的]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文的数目]{style="font-family:宋体"}

[[Adver Sent]{lang="EN-US"}]{#struct_0_18718_x1832_x2119596283}

[[发送的]{style="font-family:宋体"}[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_422804169}[通告报文的数目]{style="font-family:宋体"}

[[Global statistics]{lang="EN-US"}]{#struct_0_18718_x1832_2000982913}

[[所有备份组的全局统计信息]{style="font-family:宋体"}]{#struct_0_18718_x1832_x916443927}

[[CheckSum Errors]{lang="EN-US"}]{#struct_0_18718_x1832_x2119137531}

[[校验和错误的报文总数]{style="font-family:宋体"}]{#struct_0_18718_x1832_813580740}

[[Version Errors]{lang="EN-US"}]{#struct_0_18718_x1832_x1544171045}

[[版本号错误的报文总数]{style="font-family:宋体"}]{#struct_0_18718_x1832_2034831694}

[[VRID Errors]{lang="EN-US"}]{#struct_0_18718_x1832_x2119203067}

[[备份组号错误的报文总数]{style="font-family:宋体"}]{#struct_0_18718_x1832_x1019387764}

[ ]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[display vrrp ipv6 statistics]{lang="EN-US"}]{#struct_0_18718_x1832_961285215}[显示信息描述表（负载均衡模式）]{style="font-family:黑体"}

[]{#table_struct_0_x1776255011}[[字段]{style="font-family:黑体"}]{#struct_0_18718_x1832_1781611139}

[[描述]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1755845687}

[[Interface]{lang="EN-US"}]{#struct_0_18718_x1832_x2119268603}

[[备份组所在接口]{style="font-family:宋体"}]{#struct_0_18718_x1832_259396948}

[[VRID]{lang="EN-US"}]{#struct_0_18718_x1832_1558655335}

[[备份组号]{style="font-family:宋体"}]{#struct_0_18718_x1832_x1995645498}

[[CheckSum Errors]{lang="EN-US"}]{#struct_0_18718_x1832_500848415}

[[校验和错误的报文数]{style="font-family:宋体"}]{#struct_0_18718_x1832_1204807129}

[[Version Errors]{lang="EN-US"}]{#struct_0_18718_x1832_x2119334139}

[[版本号错误的报文数]{style="font-family:宋体"}]{#struct_0_18718_x1832_1308288672}

[[Invalid Pkts Rcvd]{lang="EN-US"}]{#struct_0_18718_x1832_x304494331}

[[接收到报文类型错误的报文数]{style="font-family:宋体"}]{#struct_0_18718_x1832_x397098033}

[[Unexpected Pkts Rcvd]{lang="EN-US"}]{#struct_0_18718_x1832_x125403030}

[[接收到未期望的报文数]{style="font-family:宋体"}]{#struct_0_18718_x1832_x2118875387}

[[Advertisement Interval Errors]{lang="EN-US"}]{#struct_0_18718_x1832_1308599857}

[[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_800930999}[通告报文发送时间间隔错误的报文数]{style="font-family:宋体"}

[[Hop Limit Errors]{lang="EN-US"}]{#struct_0_18718_x1832_x382314674}

[[跳数限制错误的报文数]{style="font-family:宋体"}]{#struct_0_18718_x1832_x434301188}

[[Auth Failures]{lang="EN-US"}]{#struct_0_18718_x1832_x2118940923}

[[认证错误的报文数]{style="font-family:宋体"}]{#struct_0_18718_x1832_851530506}

[[Invalid Auth Type]{lang="EN-US"}]{#struct_0_18718_x1832_1176403169}

[[认证类型无效的报文数]{style="font-family:宋体"}]{#struct_0_18718_x1832_1277208860}

[[Auth Type Mismatch]{lang="EN-US"}]{#struct_0_18718_x1832_x2119399674}

[[认证类型不匹配的报文数]{style="font-family:宋体"}]{#struct_0_18718_x1832_612905918}

[[Packet Length Errors]{lang="EN-US"}]{#struct_0_18718_x1832_1880371158}

[[VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x1023218643}[报文长度错误的报文数]{style="font-family:宋体"}

[[Address List Errors]{lang="EN-US"}]{#struct_0_18718_x1832_920803416}

[[虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_18718_x1832_x2119465210}[地址列表错误的报文数]{style="font-family:宋体"}

[[Become Master]{lang="EN-US"}]{#struct_0_18718_x1832_247969671}

[[成为]{style="font-family:宋体"}[Master]{lang="EN-US"}]{#struct_0_18718_x1832_x1734351765}[路由器的次数]{style="font-family:宋体"}

[[Redirect Timer Expires]{lang="EN-US"}]{#struct_0_18718_x1832_x332215553}

[[Redirect Timer]{lang="EN-US"}]{#struct_0_18718_x1832_x2119530746}[超时的次数]{style="font-family:宋体"}

[[Become AVF]{lang="EN-US"}]{#struct_0_18718_x1832_x221293}

[[成为]{style="font-family:宋体"}[AVF]{lang="EN-US"}]{#struct_0_18718_x1832_x2090565526}[的次数]{style="font-family:宋体"}

[[Time-out Timer Expires]{lang="EN-US"}]{#struct_0_18718_x1832_x26349058}

[[Time-out Timer]{lang="EN-US"}]{#struct_0_18718_x1832_x2119596282}[超时的次数]{style="font-family:宋体"}

[[Adver Rcvd]{lang="EN-US"}]{#struct_0_18718_x1832_x1143279772}

[[收到的]{style="font-family:宋体"}[Advertisement]{lang="EN-US"}]{#struct_0_18718_x1832_x1613894567}[报文的数目]{style="font-family:宋体"}

[[Request Rcvd]{lang="EN-US"}]{#struct_0_18718_x1832_x831437663}

[[收到的]{style="font-family:宋体"}[Request]{lang="EN-US"}]{#struct_0_18718_x1832_x2119137530}[报文的数目]{style="font-family:宋体"}

[[Adver Sent]{lang="EN-US"}]{#struct_0_18718_x1832_x752503201}

[[发送的]{style="font-family:宋体"}[Advertisement]{lang="EN-US"}]{#struct_0_18718_x1832_609326232}[报文的数目]{style="font-family:宋体"}

[[Request Sent]{lang="EN-US"}]{#struct_0_18718_x1832_464605614}

[[发送的]{style="font-family:宋体"}[Request]{lang="EN-US"}]{#struct_0_18718_x1832_x2119203066}[报文的数目]{style="font-family:宋体"}

[[Reply Rcvd]{lang="EN-US"}]{#struct_0_18718_x1832_546696177}

[[收到的]{style="font-family:宋体"}[Reply]{lang="EN-US"}]{#struct_0_18718_x1832_1046197847}[报文的数目]{style="font-family:宋体"}

[[Release Rcvd]{lang="EN-US"}]{#struct_0_18718_x1832_1679948980}

[[收到的]{style="font-family:宋体"}[Release]{lang="EN-US"}]{#struct_0_18718_x1832_x2119268602}[报文的数目]{style="font-family:宋体"}

[[Reply Sent]{lang="EN-US"}]{#struct_0_18718_x1832_1825480889}

[[发送的]{style="font-family:宋体"}[Reply]{lang="EN-US"}]{#struct_0_18718_x1832_x525388956}[报文的数目]{style="font-family:宋体"}

[[Release Sent]{lang="EN-US"}]{#struct_0_18718_x1832_755738089}

[[发送的]{style="font-family:宋体"}[Release]{lang="EN-US"}]{#struct_0_18718_x1832_x2119334138}[报文的数目]{style="font-family:宋体"}

[[Priority Zero Pkts Rcvd]{lang="EN-US"}]{#struct_0_18718_x1832_x257795269}

[[收到的路由器优先级为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_18718_x1832_477866915}[的]{style="font-family:宋体"}[Advertisement]{lang="EN-US"}[报文的数目]{style="font-family:宋体"}

[[VF Priority Zero Pkts Rcvd]{lang="PT-BR"}]{#struct_0_18718_x1832_x2118875386}

[[收到的虚拟转发器优先级为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_18718_x1832_x257484084}[的]{style="font-family:宋体"}[Advertisement]{lang="EN-US"}[报文的数目]{style="font-family:宋体"}

[[Priority Zero Pkts Sent]{lang="EN-US"}]{#struct_0_18718_x1832_x704176091}

[[发送的路由器优先级为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_18718_x1832_497605131}[的]{style="font-family:宋体"}[Advertisement]{lang="EN-US"}[报文的数目]{style="font-family:宋体"}

[[VF Priority Zero Pkts Sent]{lang="EN-US"}]{#struct_0_18718_x1832_x2118940922}

[[发送的虚拟转发器优先级为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_18718_x1832_x1877352849}[的]{style="font-family:宋体"}[Advertisement]{lang="EN-US"}[报文的数目]{style="font-family:宋体"}

[[Packet Option Errors]{lang="EN-US"}]{#struct_0_18718_x1832_x1231736827}

[[报文状态选项错误的次数]{style="font-family:宋体"}]{#struct_0_18718_x1832_x197085370}

[[Global statistics]{lang="EN-US"}]{#struct_0_18718_x1832_1548714767}

[[所有备份组的全局统计信息]{style="font-family:宋体"}]{#struct_0_18718_x1832_x1344442110}

[[CheckSum Errors]{lang="EN-US"}]{#struct_0_18718_x1832_290756087}

[[校验和错误的报文总数]{style="font-family:宋体"}]{#struct_0_18718_x1832_x197150906}

[[Version Errors]{lang="EN-US"}]{#struct_0_18718_x1832_x429120094}

[[版本号错误的报文总数]{style="font-family:宋体"}]{#struct_0_18718_x1832_x197216442}

[[VRID Errors]{lang="EN-US"}]{#struct_0_18718_x1832_787222197}

[[备份组号错误的报文总数]{style="font-family:宋体"}]{#struct_0_18718_x1832_x1245993303}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x752753107}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset vrrp ipv6 statistics]{lang="EN-US"}**]{#struct_0_18718_x1832_x197281978}

::: {#-964681241 .myid}
[]{#_Toc404795946}[]{#struct_0_18718_x1832_1135325409}[]{#_Toc211671372}[]{#_Toc128898006}[]{#_Toc211761214}[]{#_Toc211761284}

**VRRP \-- IPv6 VRRP配置命令 \-- reset vrrp ipv6 statistics**

------------------------------------------------------------------------

[**[reset vrrp ipv6 statistics]{lang="EN-US"}**]{#struct_0_18718_x1832_1595002423}[命令用来清除]{style="font-family:
宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组的统计信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x556109960}

[**[reset vrrp ipv6 statistics ]{lang="EN-US"}**[\[ **interface** *interface-type interface-number* \[ **vrid** *virtual-router-id* \] \]]{lang="EN-US"}]{#struct_0_18718_x1832_x1061412288}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1582360124}

[[用户视图]{style="font-family:宋体"}]{#struct_0_18718_x1832_x162302062}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x171767265}

[[network-admin]{lang="EN-US"}]{#struct_0_18718_x1832_x196823226}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18718_x1832_401131738}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1980865370}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_18718_x1832_44409225}[：清除指定接口的]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组统计信息。其中，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。]{style="font-family:宋体"}

[**[vrid]{lang="EN-US"}**[ *virtual-router-id*]{lang="EN-US"}]{#struct_0_18718_x1832_x1110160841}[：清除指定备份组的]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[统计信息。其中，]{style="font-family:宋体"}*[virtual-router-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x2051986733}

[[在清除]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x1669931549}[备份组统计信息时，如果不输入接口名和备份组号，则清除该路由器上所有]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组的统计信息；如果只输入接口名，不输入备份组号，则清除该接口上所有]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组的统计信息；如果同时输入接口名和备份组号，则清除该接口上指定]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18718_x1832_91907312}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_x207235780}[清除所有接口上所有备份组的]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset vrrp ipv6 statistics]{lang="EN-US"}]{#struct_0_18718_x1832_x196888762}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1571651121}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display vrrp ipv6]{lang="EN-US"}***[ ]{lang="EN-US"}***[statistics]{lang="EN-US"}**]{#struct_0_18718_x1832_x357454809}
:::

::: {#-45803940 .myid}
[]{#_Toc404795947}[]{#struct_0_18718_x1832_x38541940}

**VRRP \-- IPv6 VRRP配置命令 \-- vrrp ipv6 dot1q**

------------------------------------------------------------------------

[**[vrrp ipv6 dot1q]{lang="EN-US"}**]{#struct_0_18718_x1832_1812862125}[命令用来配置]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[的控制]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo vrrp ipv6 dot1q]{lang="EN-US"}**]{#struct_0_18718_x1832_x38476404}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_223614837}

[**[vrrp ipv6 dot1q vid ]{lang="NO-BOK"}***[vlan-id]{lang="EN-US"}*]{#struct_0_18718_x1832_x92754678}**[ ]{lang="EN-US"}**[\[ **secondary-dot1q** *secondary-*]{lang="NO-BOK"}*[vlan-id ]{lang="EN-US"}*[\]]{lang="EN-US"}

[**[undo vrrp ipv6 dot1q]{lang="EN-US"}**]{#struct_0_18718_x1832_686233611}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18718_x1832_903868741}

[[没有指定]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_1495782575}[的控制]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，即]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[终结支持广播]{style="font-family:宋体"}[/]{lang="EN-US"}[组播功能后，]{style="font-family:宋体"}[Master]{lang="EN-US"}[在所有模糊终结的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内发送]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[通告报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1586130717}

[[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18718_x1832_1505064785}[三层聚合子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1425602125}

[[network-admin]{lang="EN-US"}]{#struct_0_18718_x1832_x969859886}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18718_x1832_x38410868}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x2080202873}

[**[vid ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_18718_x1832_1689391682}[：指定]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[的控制]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[（外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[）的编号，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[secondary-dot1q ]{lang="EN-US"}***[secondary-]{lang="EN-US"}[vlan-id]{lang="EN-US"}*]{#struct_0_18718_x1832_1800203303}[：指定内层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，]{style="font-family:宋体"}*[secondary-]{lang="EN-US"}[vlan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x822759535}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重复执行本命令，新的配置将覆盖原有配置。]{style="font-family:宋体"}]{#struct_0_18718_x1832_297605873}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有在三层以太网子接口、三层聚合子接口和三层]{style="font-family:宋体"}]{#struct_0_18718_x1832_x172653647}[RPR]{lang="EN-US"}[逻辑接口视图下执行本命令才会生效；在其他接口视图下也可以执行本命令，但不会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1994098848}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_x824484829}[配置]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[的控制]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[（外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[）]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[2]{lang="EN-US"}[，内层]{style="font-family:
宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_x38345332}

[\[Sysname\] interface gigabitethernet 1/0/1.2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.2\] vrrp ipv6 dot1q vid 2 secondary-dot1q 100]{lang="EN-US"}
:::

::: {#1196483640 .myid}
[]{#_Toc404795948}[]{#struct_0_18718_x1832_634134557}[]{#_Toc337719114}

**VRRP \-- IPv6 VRRP配置命令 \-- vrrp ipv6 dscp**

------------------------------------------------------------------------

[**[vrrp ipv6 dscp]{lang="EN-US"}**]{#struct_0_18718_x1832_921815010}[命令用来配置]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[发送报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[**[undo vrrp ipv6 dscp]{lang="EN-US"}**]{#struct_0_18718_x1832_51258126}[命令用来恢复缺省值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1902244659}

[**[vrrp ipv6 dscp ]{lang="EN-US"}***[dscp-value]{lang="EN-US"}*]{#struct_0_18718_x1832_x294925523}

[**[undo vrrp ipv6 dscp]{lang="EN-US"}**]{#struct_0_18718_x1832_2114749529}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1806903492}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18718_x1832_x196954298}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1990199041}

[[network-admin]{lang="EN-US"}]{#struct_0_18718_x1832_512901572}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18718_x1832_x1175141107}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1268625458}

[*[dscp-value]{lang="EN-US"}*]{#struct_0_18718_x1832_x135095668}[：]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[56]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1950325414}

[[DSCP]{lang="EN-US" style="font-size:10.0pt;color:black"}]{#struct_0_18718_x1832_x1040589266}[用来体现报文自身的优先等级，决定报文传输的优先程度。配置的]{style="font-family:
宋体"}[DSCP]{lang="EN-US"}[优先级的取值越大，报文的优先级越高。通过本命令可以指定发送的]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[报文中携带的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级的取值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1257376685}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_x197019834}[配置]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_x1166537777}

[\[Sysname\] vrrp ipv6 dscp 30]{lang="EN-US"}
:::

::::: {#1986854308 .myid}
[]{#_Toc211671373}[]{#_Toc128898007}[]{#_Toc404795949}[]{#struct_0_18718_x1832_x1533561280}

**VRRP \-- IPv6 VRRP配置命令 \-- vrrp ipv6 mode**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VRRP命令.files/image002.png){#图片 7 width="62" height="27"}]{lang="EN-US"}]{#struct_0_18718_x1832_x437873575}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_18718_x1832_1406228399}
:::

[ ]{lang="EN-US"}

[**[vrrp ipv6 mode]{lang="EN-US"}**]{#struct_0_18718_x1832_x1249195781}[命令用来配置]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[的工作模式。]{style="font-family:宋体"}

[**[undo vrrp ipv6 mode]{lang="EN-US"}**]{#struct_0_18718_x1832_1592851831}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1170742516}

[**[vrrp ipv6 mode load-balance]{lang="EN-US"}**]{#struct_0_18718_x1832_x167959550}

[**[undo vrrp ipv6 mode]{lang="EN-US"}**]{#struct_0_18718_x1832_x196561082}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1173205363}

[[IPv6 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_1924174620}[工作在标准协议模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1949998765}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18718_x1832_1567387804}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1167490005}

[[network-admin]{lang="EN-US"}]{#struct_0_18718_x1832_1130765496}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18718_x1832_x1261711956}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x176223305}

[**[load-balance]{lang="EN-US"}**]{#struct_0_18718_x1832_x196626618}[：指定]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[工作在负载均衡模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1924927388}

[[IPv6 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x774259162}[工作在负载均衡模式时，要求备份组虚拟]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址和接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址不能相同。否则，负载均衡功能将无法正常工作。]{style="font-family:宋体"}

[[创建]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x950409117}[备份组后，仍然可以修改工作模式。修改工作模式后，路由器上所有的]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组都会工作在该模式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18718_x1832_445719237}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_1888626292}[配置]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[工作在负载均衡模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_386949229}

[\[Sysname\] vrrp ipv6 mode load-balance]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1438763781}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **vrrp ipv6**]{lang="EN-US"}]{#struct_0_18718_x1832_1319245827}
:::::

::: {#1276752216 .myid}
[]{#_Toc404795950}[]{#struct_0_18718_x1832_x670970813}[]{#_Toc211671379}[]{#_Toc128898014}[]{#_Toc270693174}[]{#_Toc280174924}[]{#_Toc280177631}[]{#_Toc280281511}[]{#_Toc270693175}[]{#_Toc280174925}[]{#_Toc280177632}[]{#_Toc280281512}[]{#_Toc270693177}[]{#_Toc280174927}[]{#_Toc280177634}[]{#_Toc280281514}[]{#_Toc270693178}[]{#_Toc280174928}[]{#_Toc280177635}[]{#_Toc280281515}[]{#_Toc270693179}[]{#_Toc280174929}[]{#_Toc280177636}[]{#_Toc280281516}[]{#_Toc270693180}[]{#_Toc280174930}[]{#_Toc280177637}[]{#_Toc280281517}[]{#_Toc270693181}[]{#_Toc280174931}[]{#_Toc280177638}[]{#_Toc280281518}[]{#_Toc270693182}[]{#_Toc280174932}[]{#_Toc280177639}[]{#_Toc280281519}[]{#_Toc270693183}[]{#_Toc280174933}[]{#_Toc280177640}[]{#_Toc280281520}[]{#_Toc270693184}[]{#_Toc280174934}[]{#_Toc280177641}[]{#_Toc280281521}[]{#_Toc270693185}[]{#_Toc280174935}[]{#_Toc280177642}[]{#_Toc280281522}[]{#_Toc270693186}[]{#_Toc280174936}[]{#_Toc280177643}[]{#_Toc280281523}[]{#_Toc270693187}[]{#_Toc280174937}[]{#_Toc280177644}[]{#_Toc280281524}[]{#_Toc270693188}[]{#_Toc280174938}[]{#_Toc280177645}[]{#_Toc280281525}[]{#_Toc270693189}[]{#_Toc280174939}[]{#_Toc280177646}[]{#_Toc280281526}[]{#_Toc270693190}[]{#_Toc280174940}[]{#_Toc280177647}[]{#_Toc280281527}[]{#_Toc270693191}[]{#_Toc280174941}[]{#_Toc280177648}[]{#_Toc280281528}[]{#_Toc270693192}[]{#_Toc280174942}[]{#_Toc280177649}[]{#_Toc280281529}[]{#_Toc270693193}[]{#_Toc280174943}[]{#_Toc280177650}[]{#_Toc280281530}[]{#_Toc270693194}[]{#_Toc280174944}[]{#_Toc280177651}[]{#_Toc280281531}[]{#_Toc270693195}[]{#_Toc280174945}[]{#_Toc280177652}[]{#_Toc280281532}[]{#_Toc270693196}[]{#_Toc280174946}[]{#_Toc280177653}[]{#_Toc280281533}[]{#_Toc270693199}[]{#_Toc280174949}[]{#_Toc280177656}[]{#_Toc280281536}[]{#_Toc270693200}[]{#_Toc280174950}[]{#_Toc280177657}[]{#_Toc280281537}[]{#_Toc270693201}[]{#_Toc280174951}[]{#_Toc280177658}[]{#_Toc280281538}[]{#_Toc270693202}[]{#_Toc280174952}[]{#_Toc280177659}[]{#_Toc280281539}[]{#_Toc270693203}[]{#_Toc280174953}[]{#_Toc280177660}[]{#_Toc280281540}[]{#_Toc270693204}[]{#_Toc280174954}[]{#_Toc280177661}[]{#_Toc280281541}[]{#_Toc270693205}[]{#_Toc280174955}[]{#_Toc280177662}[]{#_Toc280281542}[]{#_Toc270693206}[]{#_Toc280174956}[]{#_Toc280177663}[]{#_Toc280281543}[]{#_Toc270693207}[]{#_Toc280174957}[]{#_Toc280177664}[]{#_Toc280281544}[]{#_Toc270693208}[]{#_Toc280174958}[]{#_Toc280177665}[]{#_Toc280281545}[]{#_Toc270693209}[]{#_Toc280174959}[]{#_Toc280177666}[]{#_Toc280281546}[]{#_Toc270693210}[]{#_Toc280174960}[]{#_Toc280177667}[]{#_Toc280281547}[]{#_Toc270693211}[]{#_Toc280174961}[]{#_Toc280177668}[]{#_Toc280281548}[]{#_Toc270693212}[]{#_Toc280174962}[]{#_Toc280177669}[]{#_Toc280281549}[]{#_Toc270693213}[]{#_Toc280174963}[]{#_Toc280177670}[]{#_Toc280281550}[]{#_Toc270693214}[]{#_Toc280174964}[]{#_Toc280177671}[]{#_Toc280281551}[]{#_Toc270693215}[]{#_Toc280174965}[]{#_Toc280177672}[]{#_Toc280281552}[]{#_Toc270693216}[]{#_Toc280174966}[]{#_Toc280177673}[]{#_Toc280281553}[]{#_Toc270693217}[]{#_Toc280174967}[]{#_Toc280177674}[]{#_Toc280281554}[]{#_Toc270693218}[]{#_Toc280174968}[]{#_Toc280177675}[]{#_Toc280281555}[]{#_Toc270693219}[]{#_Toc280174969}[]{#_Toc280177676}[]{#_Toc280281556}[]{#_Toc270693220}[]{#_Toc280174970}[]{#_Toc280177677}[]{#_Toc280281557}[]{#_Toc270693222}[]{#_Toc280174972}[]{#_Toc280177679}[]{#_Toc280281559}[]{#_Toc270693223}[]{#_Toc280174973}[]{#_Toc280177680}[]{#_Toc280281560}[]{#_Toc270693224}[]{#_Toc280174974}[]{#_Toc280177681}[]{#_Toc280281561}[]{#_Toc270693225}[]{#_Toc280174975}[]{#_Toc280177682}[]{#_Toc280281562}[]{#_Toc270693226}[]{#_Toc280174976}[]{#_Toc280177683}[]{#_Toc280281563}[]{#_Toc270693228}[]{#_Toc280174978}[]{#_Toc280177685}[]{#_Toc280281565}[]{#_Toc270693229}[]{#_Toc280174979}[]{#_Toc280177686}[]{#_Toc280281566}[]{#_Toc270693230}[]{#_Toc280174980}[]{#_Toc280177687}[]{#_Toc280281567}[]{#_Toc197333777}[]{#_Toc197943302}[]{#_Toc198390039}[]{#_Toc197333778}[]{#_Toc197943303}[]{#_Toc198390040}[]{#_Toc197333780}[]{#_Toc197943305}[]{#_Toc198390042}[]{#_Toc197333781}[]{#_Toc197943306}[]{#_Toc198390043}[]{#_Toc197333782}[]{#_Toc197943307}[]{#_Toc198390044}[]{#_Toc197333783}[]{#_Toc197943308}[]{#_Toc198390045}[]{#_Toc197333784}[]{#_Toc197943309}[]{#_Toc198390046}[]{#_Toc197333785}[]{#_Toc197943310}[]{#_Toc198390047}[]{#_Toc197333786}[]{#_Toc197943311}[]{#_Toc198390048}[]{#_Toc197333787}[]{#_Toc197943312}[]{#_Toc198390049}[]{#_Toc197333788}[]{#_Toc197943313}[]{#_Toc198390050}[]{#_Toc197333789}[]{#_Toc197943314}[]{#_Toc198390051}[]{#_Toc197333790}[]{#_Toc197943315}[]{#_Toc198390052}[]{#_Toc197333791}[]{#_Toc197943316}[]{#_Toc198390053}[]{#_Toc197333792}[]{#_Toc197943317}[]{#_Toc198390054}[]{#_Toc197333793}[]{#_Toc197943318}[]{#_Toc198390055}[]{#_Toc197333794}[]{#_Toc197943319}[]{#_Toc198390056}[]{#_Toc197333795}[]{#_Toc197943320}[]{#_Toc198390057}[]{#_Toc197333796}[]{#_Toc197943321}[]{#_Toc198390058}[]{#_Toc194230995}[]{#_Toc195410205}[]{#_Toc194230996}[]{#_Toc195410206}[]{#_Toc194230999}[]{#_Toc195410209}[]{#_Toc194231000}[]{#_Toc195410210}[]{#_Toc194231001}[]{#_Toc195410211}[]{#_Toc194231002}[]{#_Toc195410212}[]{#_Toc194231003}[]{#_Toc195410213}[]{#_Toc194231004}[]{#_Toc195410214}[]{#_Toc194231005}[]{#_Toc195410215}[]{#_Toc194231006}[]{#_Toc195410216}[]{#_Toc194231007}[]{#_Toc195410217}[]{#_Toc194231008}[]{#_Toc195410218}[]{#_Toc194231009}[]{#_Toc195410219}[]{#_Toc194231010}[]{#_Toc195410220}[]{#_Toc194231011}[]{#_Toc195410221}[]{#_Toc194231012}[]{#_Toc195410222}[]{#_Toc194231013}[]{#_Toc195410223}[]{#_Toc194231015}[]{#_Toc195410225}

**VRRP \-- IPv6 VRRP配置命令 \-- vrrp ipv6 vrid**

------------------------------------------------------------------------

[**[vrrp ipv6 vrid]{lang="DA"}**]{#struct_0_18718_x1832_x2034892062}[命令用来创建]{style="font-family:宋体"}[IPv6 VRRP]{lang="DA"}[备份组]{style="font-family:宋体"}[，]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[IPv6 VRRP]{lang="DA"}[备份组的虚拟]{style="font-family:宋体"}[IPv6]{lang="DA"}[地址]{style="font-family:宋体"}[，]{style="font-family:宋体"}[或为一个已经存在的]{style="font-family:宋体"}[IPv6 VRRP]{lang="DA"}[备份组添加一个虚拟]{style="font-family:宋体"}[IPv6]{lang="DA"}[地址。]{style="font-family:宋体"}

[**[undo vrrp ipv6 vrid]{lang="DA"}**]{#struct_0_18718_x1832_702751728}[命令用来删除一个已经存在的]{style="font-family:宋体"}[IPv6 VRRP]{lang="DA"}[备份组的所有配置，或删除已经存在的]{style="font-family:宋体"}[IPv6 VRRP]{lang="DA"}[备份组中的虚拟]{style="font-family:宋体"}[IPv6]{lang="DA"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1942332708}

[**[vrrp ipv6 vrid]{lang="EN-US"}**[ ]{lang="EN-US"}*[virtual-router-id]{lang="EN-US"}***[ virtual-ip]{lang="EN-US"}***[ virtual-address]{lang="EN-US"}*[ \[ **link-local** \]]{lang="EN-US"}]{#struct_0_18718_x1832_243751619}

[**[undo vrrp ipv6 vrid]{lang="EN-US"}***[ virtual-router-id ]{lang="EN-US"}*[\[ **virtual-ip** \[ *virtual-address* \[ **link-local** \] \] \]]{lang="EN-US"}]{#struct_0_18718_x1832_x1724375170}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1114665322}

[[没有创建]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x196561084}[备份组。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1173336435}

[[接口视图]{style="font-family:宋体"}]{#struct_0_18718_x1832_709816527}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x382559016}

[[network-admin]{lang="EN-US"}]{#struct_0_18718_x1832_4134031}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18718_x1832_1582927904}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x2103061477}

[*[virtual-router-id]{lang="EN-US"}*]{#struct_0_18718_x1832_1273554692}[：]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[virtual-ip]{lang="EN-US"}***[ virtual-address]{lang="EN-US"}*]{#struct_0_18718_x1832_x777255207}[：备份组的虚拟]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。删除]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组中的虚拟]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址时，如果不指定]{style="font-family:宋体"}*[virtual-address]{lang="EN-US"}*[参数，则表示删除该备份组中的所有虚拟]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[link-local]{lang="EN-US"}**]{#struct_0_18718_x1832_x196626620}[：虚拟]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为链路本地地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1925451675}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重复执行本命令，可以为备份组配置多个虚拟]{style="font-family:宋体"}]{#struct_0_18718_x1832_353544180}[IPv6]{lang="EN-US"}[地址，但每个备份组最多只能配置]{style="font-family:宋体"}[16]{lang="EN-US"}[个虚拟]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[备份组的第一个虚拟]{style="font-family:宋体"}]{#struct_0_18718_x1832_1342740609}[IPv6]{lang="EN-US"}[地址必须是链路本地地址，链路本地地址必须最后删除。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{style="font-family:宋体"}]{#struct_0_18718_x1832_x1568980107}[VRRP]{lang="EN-US"}[备份组中只允许有一个链路本地地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果没有为备份组配置虚拟]{style="font-family:宋体"}]{#struct_0_18718_x1832_x1023432629}[IPv6]{lang="EN-US"}[地址，但是为备份组进行了其他配置（如优先级、抢占方式等），则该备份组会存在于设备上，并处于]{style="font-family:宋体"}[Inactive]{lang="EN-US"}[状态，此时备份组不起作用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[建议将备份组的虚拟]{style="font-family:宋体"}]{#struct_0_18718_x1832_1370412656}[IPv6]{lang="EN-US"}[地址和接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址配置为同一网段，否则可能导致局域网内的主机无法访问外部网络。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x431940172}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18718_x1832_x1355422989}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_x197085371}[创建]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[，配置]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[的虚拟]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[fe80::10]{lang="EN-US"}[。为]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[添加一个虚拟]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}[1::10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_1548780303}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] vrrp ipv6 vrid 1 virtual-ip fe80::10 link-local]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] vrrp ipv6 vrid 1 virtual-ip 1::10]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18718_x1832_1728725876}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_1864095142}[创建]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[，配置]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[的虚拟]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[fe80::10]{lang="EN-US"}[。为]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[添加一个虚拟]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}[1::10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_x1534420265}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] vrrp ipv6 vrid 1 virtual-ip fe80::10 link-local]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] vrrp ipv6 vrid 1 virtual-ip 1::10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x371459155}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display vrrp ipv6]{lang="EN-US"}**]{#struct_0_18718_x1832_x783292145}
:::

::: {#1094442734 .myid}
[]{#_Toc404795951}[]{#struct_0_18718_x1832_x197085369}[]{#_Toc211671375}[]{#_Toc128898010}

**VRRP \-- IPv6 VRRP配置命令 \-- vrrp ipv6 vrid preempt-mode**

------------------------------------------------------------------------

[**[vrrp ipv6 vrid preempt-mode]{lang="EN-US"}**]{#struct_0_18718_x1832_1549304592}[命令用来配置]{style="font-family:
宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组中的路由器工作在抢占方式，并配置抢占延迟时间。]{style="font-family:
宋体"}

[**[undo vrrp ipv6 vrid preempt-mode]{lang="EN-US"}**]{#struct_0_18718_x1832_x554012285}[命令用来取消抢占方式，即配置]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组中的路由器工作在非抢占方式。]{style="font-family:宋体"}

[**[undo vrrp ipv6 vrid preempt-mode delay]{lang="EN-US"}**]{#struct_0_18718_x1832_x1317664666}[命令用来恢复抢占延迟时间为缺省值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_696248941}

[**[vrrp ipv6 vrid]{lang="EN-US"}**[ *virtual-router-id* **preempt-mode** \[ **delay** *delay-value* \]]{lang="EN-US"}]{#struct_0_18718_x1832_789448071}

[**[undo vrrp ipv6 vrid]{lang="EN-US"}**[ *virtual-router-id* **preempt-mode** \[ **delay** \]]{lang="EN-US"}]{#struct_0_18718_x1832_x1504756158}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1344247734}

[[IPv6 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_1603781521}[备份组中的路由器工作在抢占方式，抢占延迟时间为]{style="font-family:宋体"}[0]{lang="EN-US"}[厘秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x197150905}

[[接口视图]{style="font-family:宋体"}]{#struct_0_18718_x1832_x429316702}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1481447361}

[[network-admin]{lang="EN-US"}]{#struct_0_18718_x1832_156292285}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18718_x1832_x1985266723}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18718_x1832_64356385}

[*[virtual-router-id]{lang="EN-US"}*]{#struct_0_18718_x1832_166832459}[：]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[delay]{lang="EN-US"}***[ delay-value]{lang="EN-US"}*]{#struct_0_18718_x1832_x813423023}[：抢占延迟时间。]{style="font-family:宋体"}*[delay-value]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[180000]{lang="EN-US"}[，单位为厘秒，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[厘秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x197216441}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果备份组中的路由器工作在非抢占方式下，则只要]{style="font-family:宋体"}]{#struct_0_18718_x1832_787025589}[Master]{lang="EN-US"}[路由器没有出现故障，]{style="font-family:宋体"}[Backup]{lang="EN-US"}[路由器即使随后被配置了更高的优先级也不会成为]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器。非抢占方式可以避免频繁地切换]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果备份组中的路由器工作在抢占方式下，它一旦发现自己的优先级比当前的]{style="font-family:宋体"}]{#struct_0_18718_x1832_x1528989417}[Master]{lang="EN-US"}[路由器的优先级高，就会对外发送]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文。导致备份组内路由器重新选举]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器，并最终取代原有的]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器。相应地，原来的]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器将会变成]{style="font-family:宋体"}[Backup]{lang="EN-US"}[路由器。抢占方式可以确保承担转发任务的]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器始终是备份组中优先级最高的路由器。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为了避免备份组内的成员频繁进行主备状态转换，让]{style="font-family:宋体"}]{#struct_0_18718_x1832_x2145968925}[Backup]{lang="EN-US"}[路由器有足够的时间搜集必要的信息（如路由信息），]{style="font-family:宋体"}[Backup]{lang="EN-US"}[路由器接收到优先级低于本地优先级的通告报文后，不会立即抢占成为]{style="font-family:宋体"}[Master]{lang="EN-US"}[，而是等待一定时间后，才会重新选举新的]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1789591061}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18718_x1832_2001005415}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_233594481}[配置路由器工作于抢占方式，抢占延迟时间为]{style="font-family:宋体"}[5000]{lang="EN-US"}[厘秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_1888761060}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] vrrp ipv6 vrid 10 preempt-mode delay 5000]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18718_x1832_x1966281806}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_x197281977}[配置交换机工作于抢占方式，抢占延迟时间为]{style="font-family:宋体"}[5000]{lang="EN-US"}[厘秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_1134997729}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] vrrp ipv6 vrid 10 preempt-mode delay 5000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x391924191}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **vrrp ipv6**]{lang="EN-US"}]{#struct_0_18718_x1832_x568067841}
:::

::: {#1588827321 .myid}
[]{#_Toc404795952}[]{#struct_0_18718_x1832_x1316532072}[]{#_Toc211671376}[]{#_Toc128898011}

**VRRP \-- IPv6 VRRP配置命令 \-- vrrp ipv6 vrid priority**

------------------------------------------------------------------------

[**[vrrp ipv6 vrid priority]{lang="EN-US"}**]{#struct_0_18718_x1832_x1630745065}[命令用来设置路由器在]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组中的优先级。]{style="font-family:宋体"}

[**[undo vrrp ipv6 vrid priority]{lang="EN-US"}**]{#struct_0_18718_x1832_345940662}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1780063889}

[**[vrrp ipv6 vrid ]{lang="EN-US"}***[virtual-router-id]{lang="EN-US"}*[ **priority** *priority-value*]{lang="EN-US"}]{#struct_0_18718_x1832_x196823225}

[**[undo vrrp ipv6 vrid]{lang="EN-US"}**[ *virtual-router-id* **priority**]{lang="EN-US"}]{#struct_0_18718_x1832_401066202}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x420411468}

[[路由器在]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_848393721}[备份组中的优先级为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1984163826}

[[接口视图]{style="font-family:宋体"}]{#struct_0_18718_x1832_x1432157514}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x677906501}

[[network-admin]{lang="EN-US"}]{#struct_0_18718_x1832_1455668869}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18718_x1832_58575265}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x902932173}

[*[virtual-router-id]{lang="EN-US"}*]{#struct_0_18718_x1832_x196888761}[：]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[priority-value]{lang="EN-US"}*]{#struct_0_18718_x1832_x1571454513}[：优先级的值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[254]{lang="EN-US"}[，该值越大表明优先级越高。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1122974995}

[[优先级决定路由器在备份组中的地位。优先级越高，越有可能成为]{style="font-family:宋体"}[Master]{lang="EN-US"}]{#struct_0_18718_x1832_x1886548425}[路由器。优先级]{style="font-family:宋体"}[0]{lang="EN-US"}[是系统保留为特殊用途来使用的，]{style="font-family:宋体"}[255]{lang="EN-US"}[则是系统保留给]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址拥有者的。]{style="font-family:宋体"}

[[路由器为]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_18718_x1832_2102134750}[地址拥有者时，其运行优先级始终为]{style="font-family:宋体"}[255]{lang="EN-US"}[，表明只要其工作正常，则为]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x502535825}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18718_x1832_x1545127861}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_1343695144}[设置路由器在]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[中的优先级为]{style="font-family:宋体"}[150]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_x196954297}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] vrrp ipv6 vrid 1 priority 150]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18718_x1832_x1990919937}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_x1796695971}[设置交换机在]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[中的优先级为]{style="font-family:宋体"}[150]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_x1318568469}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] vrrp ipv6 vrid 1 priority 150]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x795820063}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **vrrp ipv6**]{lang="EN-US"}]{#struct_0_18718_x1832_x305060186}
:::

::: {#22151509 .myid}
[]{#_Toc404795953}[]{#struct_0_18718_x1832_x1912606602}

**VRRP \-- IPv6 VRRP配置命令 \-- vrrp ipv6 vrid shutdown**

------------------------------------------------------------------------

[**[vrrp ipv6 vrid ]{lang="EN-US"}[shutdown]{lang="EN-US"}**]{#struct_0_18718_x1832_1567898616}[命令用来关闭指定的]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组。]{style="font-family:宋体"}

[**[undo vrrp ipv6 vrid shutdown]{lang="EN-US"}**]{#struct_0_18718_x1832_x1825264148}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x197019833}

[**[vrrp ipv6 vrid]{lang="EN-US"}***[ virtual-router-id]{lang="EN-US"}*[ **shutdown**]{lang="EN-US"}]{#struct_0_18718_x1832_x1166734385}

[**[undo vrrp ipv6 vrid]{lang="EN-US"}**[ *virtual-router-id* **shutdown**]{lang="EN-US"}]{#struct_0_18718_x1832_2005323014}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1958829526}

[[IPv6 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_1701880260}[备份组处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:
黑体"}]{#struct_0_18718_x1832_205543}

[[接口视图]{style="font-family:宋体"}]{#struct_0_18718_x1832_677728441}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1858999894}

[[network-admin]{lang="EN-US"}]{#struct_0_18718_x1832_x1691786919}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18718_x1832_x196561081}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1173139827}

[*[virtual-router-id]{lang="EN-US"}*]{#struct_0_18718_x1832_432085875}[：]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[备份组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18718_x1832_370917962}

[[关闭]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x608488263}[备份组功能通常用于暂时禁用备份组，但还需要再次启用该备份组的场景。关闭备份组后，该备份组的状态为]{style="font-family:宋体"}[Initialize]{lang="EN-US"}[，并且该备份组所有已存在的配置保持不变。在关闭状态下还可以对备份组进行配置。备份组再次被开启后，基于最新的配置，从]{style="font-family:宋体"}[Initialize]{lang="EN-US"}[状态重新开始运行。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18718_x1832_378115647}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18718_x1832_x1756014593}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_x1398618938}[关闭]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_x196626617}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] vrrp ipv6 vrid 1 shutdown]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18718_x1832_1925386140}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_1588284105}[关闭]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_x1034532321}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] vrrp ipv6 vrid 1 shutdown]{lang="EN-US"}
:::

::: {#560038332 .myid}
[]{#_Toc404795954}[]{#struct_0_18718_x1832_1646080500}[]{#_Toc211671377}[]{#_Toc128898012}

**VRRP \-- IPv6 VRRP配置命令 \-- vrrp ipv6 vrid timer advertise**

------------------------------------------------------------------------

[**[vrrp ipv6 vrid timer advertise]{lang="EN-US"}**]{#struct_0_18718_x1832_x1950202923}[命令用来配置]{style="font-family:
宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组中]{style="font-family:
宋体"}[Master]{lang="EN-US"}[路由器发送]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文的时间间隔。]{style="font-family:宋体"}

[**[undo vrrp ipv6 vrid timer advertise]{lang="EN-US"}**]{#struct_0_18718_x1832_1534737331}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1420970267}

[**[vrrp ipv6 vrid]{lang="EN-US"}**[ *virtual-router-id* **timer advertise** *adver-interval*]{lang="EN-US"}]{#struct_0_18718_x1832_x784251557}

[**[undo vrrp ipv6 vrid]{lang="EN-US"}**[ *virtual-router-id* **timer advertise**]{lang="EN-US"}]{#struct_0_18718_x1832_x197085372}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1548583695}

[[IPv6 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_191352478}[备份组中]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器发送]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文的时间间隔为]{style="font-family:宋体"}[100]{lang="EN-US"}[厘秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1822238986}

[[接口视图]{style="font-family:宋体"}]{#struct_0_18718_x1832_x266009441}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1889538017}

[[network-admin]{lang="EN-US"}]{#struct_0_18718_x1832_x942769590}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18718_x1832_x196859155}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1150481103}

[*[virtual-router-id]{lang="EN-US"}*]{#struct_0_18718_x1832_x197150908}[：]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[adver-interval]{lang="EN-US"}*]{#struct_0_18718_x1832_x428464734}[：]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组中的]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器发送]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文的间隔时间，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[4095]{lang="EN-US"}[，单位为厘秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x841208083}

[[IPv6 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_525383036}[备份组中的]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器会定时发送]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文，通知备份组内的路由器自己工作正常。]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文的发送时间间隔为本命令配置的值。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_18718_x1832_x1614736733}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[建议配置]{style="font-family:宋体"}]{#struct_0_18718_x1832_1790416080}[VRRP]{lang="EN-US"}[通告报文的发送间隔大于]{style="font-family:宋体"}[100]{lang="EN-US"}[厘秒，否则会对系统的稳定性产生影响。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv6 VRRP]{lang="EN-US"}]{#struct_0_18718_x1832_x463781530}[备份组中的路由器上配置的]{style="font-family:
宋体"}[VRRP]{lang="EN-US"}[通告报文时间间隔可以不同。]{style="font-family:
宋体"}[Master]{lang="EN-US"}[路由器根据自身配置的报文时间间隔定时发送通告报文，并在通告报文中携带]{style="font-family:
宋体"}[Master]{lang="EN-US"}[路由器上配置的时间间隔；]{style="font-family:宋体"}[Backup]{lang="EN-US"}[路由器接收到]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器发送的通告报文后，记录报文中携带的]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器通告报文时间间隔，如果在]{style="font-family:宋体"}[3]{lang="EN-US"}[×记录的时间间隔＋]{style="font-family:宋体"}[Skew_Time]{lang="EN-US"}[内没有收到]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器发送的]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文，则认为]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器出现故障，重新选举]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[网络流量过大可能会导致]{style="font-family:宋体"}]{#struct_0_18718_x1832_505189893}[Backup]{lang="EN-US"}[路由器在指定时间内没有收到]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器的]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文，从而发生状态转换。可以通过将]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文的发送时间间隔延长的办法来解决该问题。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1742780286}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18718_x1832_x197216444}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_787353269}[设置]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器发送]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文的间隔时间为]{style="font-family:宋体"}[500]{lang="EN-US"}[厘秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_x1290075107}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] vrrp ipv6 vrid 1 timer advertise 500]{lang="NO-BOK"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18718_x1832_897877026}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_1212960391}[设置]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器发送]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[通告报文的间隔时间为]{style="font-family:宋体"}[500]{lang="EN-US"}[厘秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_x694811641}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] vrrp ipv6 vrid 1 timer advertise 500]{lang="NO-BOK"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1071559177}

[[·[              ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **vrrp ipv6**]{lang="EN-US"}]{#struct_0_18718_x1832_x443475220}
:::

::::: {#-1588654424 .myid}
[]{#_Toc128898013}[]{#_Toc404795955}[]{#struct_0_18718_x1832_x197281980}[]{#_Toc270693236}[]{#_Toc280174986}[]{#_Toc280177693}[]{#_Toc280281573}[]{#_Toc270693237}[]{#_Toc280174987}[]{#_Toc280177694}[]{#_Toc280281574}[]{#_Toc270693240}[]{#_Toc280174990}[]{#_Toc280177697}[]{#_Toc280281577}[]{#_Toc270693241}[]{#_Toc280174991}[]{#_Toc280177698}[]{#_Toc280281578}[]{#_Toc270693242}[]{#_Toc280174992}[]{#_Toc280177699}[]{#_Toc280281579}[]{#_Toc270693243}[]{#_Toc280174993}[]{#_Toc280177700}[]{#_Toc280281580}[]{#_Toc270693244}[]{#_Toc280174994}[]{#_Toc280177701}[]{#_Toc280281581}[]{#_Toc270693245}[]{#_Toc280174995}[]{#_Toc280177702}[]{#_Toc280281582}[]{#_Toc270693246}[]{#_Toc280174996}[]{#_Toc280177703}[]{#_Toc280281583}[]{#_Toc270693247}[]{#_Toc280174997}[]{#_Toc280177704}[]{#_Toc280281584}[]{#_Toc270693248}[]{#_Toc280174998}[]{#_Toc280177705}[]{#_Toc280281585}[]{#_Toc270693249}[]{#_Toc280174999}[]{#_Toc280177706}[]{#_Toc280281586}[]{#_Toc270693250}[]{#_Toc280175000}[]{#_Toc280177707}[]{#_Toc280281587}[]{#_Toc270693251}[]{#_Toc280175001}[]{#_Toc280177708}[]{#_Toc280281588}[]{#_Toc270693252}[]{#_Toc280175002}[]{#_Toc280177709}[]{#_Toc280281589}[]{#_Toc270693253}[]{#_Toc280175003}[]{#_Toc280177710}[]{#_Toc280281590}[]{#_Toc270693254}[]{#_Toc280175004}[]{#_Toc280177711}[]{#_Toc280281591}[]{#_Toc270693255}[]{#_Toc280175005}[]{#_Toc280177712}[]{#_Toc280281592}[]{#_Toc270693256}[]{#_Toc280175006}[]{#_Toc280177713}[]{#_Toc280281593}[]{#_Toc270693257}[]{#_Toc280175007}[]{#_Toc280177714}[]{#_Toc280281594}[]{#_Toc270693258}[]{#_Toc280175008}[]{#_Toc280177715}[]{#_Toc280281595}[]{#_Toc270693259}[]{#_Toc280175009}[]{#_Toc280177716}[]{#_Toc280281596}[]{#_Toc270693260}[]{#_Toc280175010}[]{#_Toc280177717}[]{#_Toc280281597}[]{#_Toc270693262}[]{#_Toc280175012}[]{#_Toc280177719}[]{#_Toc280281599}[]{#_Toc270693263}[]{#_Toc280175013}[]{#_Toc280177720}[]{#_Toc280281600}[]{#_Toc270693265}[]{#_Toc280175015}[]{#_Toc280177722}[]{#_Toc280281602}[]{#_Toc270693266}[]{#_Toc280175016}[]{#_Toc280177723}[]{#_Toc280281603}[]{#_Toc270693268}[]{#_Toc280175018}[]{#_Toc280177725}[]{#_Toc280281605}[]{#_Toc270693269}[]{#_Toc280175019}[]{#_Toc280177726}[]{#_Toc280281606}[]{#_Toc270693270}[]{#_Toc280175020}[]{#_Toc280177727}[]{#_Toc280281607}

**VRRP \-- IPv6 VRRP配置命令 \-- vrrp ipv6 vrid track**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VRRP命令.files/image002.png){#图片 8 width="62" height="27"}]{lang="EN-US"}]{#struct_0_18718_x1832_1134801120}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_18718_x1832_411737978}
:::

[ ]{lang="EN-US"}

[**[vrrp ipv6 vrid track]{lang="EN-US"}**]{#struct_0_18718_x1832_563093576}[命令用来配置监视指定的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项，即当]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的状态为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，立即将虚拟转发器切换为]{style="font-family:宋体"}[Active]{lang="EN-US"}[状态、降低路由器的优先级、立即切换成为]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器或降低本地虚拟转发器权重值。]{style="font-family:宋体"}

[**[undo vrrp ipv6 vrid track]{lang="EN-US"}**]{#struct_0_18718_x1832_483441670}[命令用来取消监视指定的]{style="font-family:
宋体"}[Track]{lang="EN-US"}[项。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1224272026}

[**[vrrp ipv6 vrid]{lang="EN-US"}**[ *virtual-router-id* **track** *track-entry-number* { **forwarder-switchover** **member-ip** *ipv6-address* \| **priority reduced** \[ *priority-reduced* \] \| **switchover** \| **weight reduced** \[ *weight-reduced* \] }]{lang="EN-US"}]{#struct_0_18718_x1832_x1621684116}

[**[undo vrrp ipv6 vrid]{lang="EN-US"}**[ *virtual-router-id* **track** \[ *track-entry-number* \] \[ **forwarder-switchover** \| **priority reduced** \| **switchover** \| **weight reduced** \]]{lang="EN-US"}]{#struct_0_18718_x1832_508851089}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18718_x1832_643589836}

[[没有指定被监视的]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_18718_x1832_x196823228}[项。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18718_x1832_400738522}

[[接口视图]{style="font-family:宋体"}]{#struct_0_18718_x1832_1398625741}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18718_x1832_850769464}

[[network-admin]{lang="EN-US"}]{#struct_0_18718_x1832_1702629304}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18718_x1832_591412506}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1183928781}

[*[virtual-router-id]{lang="EN-US"}*]{#struct_0_18718_x1832_542626171}[：]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[track-entry-number]{lang="EN-US"}*]{#struct_0_18718_x1832_x196888764}[：被监视的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项序号，]{style="font-family:宋体"}*[track-entry-number]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[forwarder-switchover]{lang="EN-US"}**[ **member-ip** *ipv6-address*]{lang="EN-US"}]{#struct_0_18718_x1832_x2122768674}[：虚拟转发器快速切换模式。当监视的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项状态变为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，如果本地设备上有处于]{style="font-family:宋体"}[Listening]{lang="EN-US"}[状态的虚拟转发器，且其对应的]{style="font-family:宋体"}[AVF]{lang="EN-US"}[地址为]{style="font-family:宋体"}**[member-ip]{lang="EN-US"}**[，则马上将该虚拟转发器切换到]{style="font-family:宋体"}[Active]{lang="EN-US"}[状态。]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[为备份组中成员设备的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。可以通过]{style="font-family:宋体"}**[display vrrp verbose]{lang="EN-US"}**[命令查看备份组中包含的成员设备。]{style="font-family:宋体"}

[**[priority reduced]{lang="EN-US"}**[ \[ *priority-reduced* \]]{lang="EN-US"}]{#struct_0_18718_x1832_x1172535064}[：当监视的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项状态变为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，降低本地路由器在备份组中的优先级。优先级降低的数值为]{style="font-family:宋体"}*[priority-reduced]{lang="EN-US"}*[，]{style="font-family:宋体"}*[priority-reduced]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[switchover]{lang="EN-US"}**]{#struct_0_18718_x1832_x1871193677}[：切换模式，当监视的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的状态变为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，如果本路由器在备份组中处于]{style="font-family:宋体"}[Backup]{lang="EN-US"}[状态，则马上切换成为]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器。]{style="font-family:宋体"}

[**[weight reduced ]{lang="EN-US"}**[\[ *weight-reduced* \]]{lang="EN-US"}]{#struct_0_18718_x1832_x548790562}[：当监视的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项状态变为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，当前路由器上属于指定]{style="font-family:宋体"}[IPv4 VRRP]{lang="EN-US"}[组的所有虚拟转发器的权重都降低指定的数值。权重降低的数值为]{style="font-family:宋体"}*[weight-reduced]{lang="EN-US"}*[，]{style="font-family:宋体"}*[weight-reduced]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1827863949}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_18718_x1832_1059921093}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在执行本配置之前，需要先在接口上创建备份组并配置虚拟]{style="font-family:宋体"}]{#struct_0_18718_x1832_1348604274}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}**[undo vrrp ]{lang="EN-US"}**]{#struct_0_18718_x1832_1526100257}**[ipv6 ]{lang="EN-US"}[vrid track]{lang="EN-US"}**[命令时如果没有指定]{lang="EN-US" style="font-family:宋体"}*[track-entry-number]{lang="EN-US"}*[参数，则删除该备份组与所有]{lang="EN-US" style="font-family:
宋体"}[Track]{lang="EN-US"}[项的关联。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有]{style="font-family:宋体"}]{#struct_0_18718_x1832_x137677885}[VRRP]{lang="EN-US"}[工作在负载均衡模式时，执行]{style="font-family:宋体"}**[forwarder-switchover]{lang="EN-US"}**[ **member-ip** *ip*]{lang="EN-US"}*[v6]{lang="EN-US"}[-address]{lang="EN-US"}*[或]{style="font-family:宋体"}**[weight reduced ]{lang="EN-US"}**[\[ *weight-reduced* \]]{lang="EN-US"}[才会生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[虚拟转发器的权重值为]{style="font-family:宋体"}]{#struct_0_18718_x1832_x519600884}[255]{lang="EN-US"}[，虚拟转发器的失效下限为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[由于]{style="font-family:宋体"}]{#struct_0_18718_x1832_x317205786}[VF Owner]{lang="EN-US"}[的权重高于或等于失效下限时，它的优先级始终为]{style="font-family:宋体"}[255]{lang="EN-US"}[，不会根据虚拟转发器的权重改变。当监视的上行接口出现故障时，配置的权重降低数额需保证]{style="font-family:宋体"}[VF Owner]{lang="EN-US"}[的权重低于失效下限，即权重降低的数额大于]{style="font-family:宋体"}[245]{lang="EN-US"}[，其他的虚拟转发器才能接替]{style="font-family:宋体"}[VF Owner]{lang="EN-US"}[成为]{style="font-family:宋体"}[AVF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由器在某个备份组中作为]{style="font-family:宋体"}]{#struct_0_18718_x1832_x353849512}[IP]{lang="EN-US"}[地址拥有者时，]{style="font-family:宋体"}[如果在该路由器上执行]{lang="EN-US" style="font-family:宋体"}**[vrrp ]{lang="EN-US"}[ipv6 ]{lang="EN-US"}[vrid track priority reduced]{lang="EN-US"}**[或]{lang="EN-US" style="font-family:宋体"}**[vrrp ]{lang="EN-US"}[ipv6 ]{lang="EN-US"}[vrid track switchover]{lang="EN-US"}**[命令，]{lang="EN-US" style="font-family:宋体"}[则该配置不会生效。该路由器不再作为]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址拥有者后，之前的配置才会生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[被监视的]{style="font-family:宋体"}]{#struct_0_18718_x1832_1250239305}[Track]{lang="EN-US"}[项的状态由]{style="font-family:宋体"}[Negative]{lang="EN-US"}[变为]{style="font-family:宋体"}[Positive]{lang="EN-US"}[或]{style="font-family:宋体"}[NotReady]{lang="EN-US"}[后，对应的路由器优先级会自动恢复、对应虚拟转发器的权重会自动恢复、故障恢复后的原]{style="font-family:宋体"}[Master]{lang="EN-US"}[路由器会重新抢占为]{style="font-family:宋体"}[Master]{lang="EN-US"}[状态、故障恢复后的原]{style="font-family:宋体"}[AVF]{lang="EN-US"}[会重新抢占为]{style="font-family:宋体"}[Active]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[被监视的]{style="font-family:宋体"}]{#struct_0_18718_x1832_x196954300}[Track]{lang="EN-US"}[项可以是未创建的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项。]{style="font-family:宋体"}[可以通过]{lang="EN-US" style="font-family:宋体"}**[vrrp ipv6 vrid track]{lang="EN-US"}**[命令指定监视的]{lang="EN-US" style="font-family:
宋体"}[Track]{lang="EN-US"}[项后，再通过]{lang="EN-US" style="font-family:宋体"}**[track]{lang="EN-US"}**[命令创建该]{lang="EN-US" style="font-family:宋体"}[Track]{lang="EN-US"}[项。]{lang="EN-US" style="font-family:宋体"}

[[Track]{lang="EN-US"}]{#struct_0_18718_x1832_347928822}[项的详细介绍请参见"可靠性配置指导"中的"]{style="font-family:宋体"}[Track]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18718_x1832_1817151341}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18718_x1832_1684181103}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_x1429804051}[在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上配置监视]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[，当]{style="font-family:
宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[状态为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[的优先级降低]{style="font-family:宋体"}[50]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_496912329}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] vrrp ipv6 vrid 1 track 1 priority reduced 50]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_1789861598}[在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上配置虚拟转发器监视]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[，当]{style="font-family:
宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[状态为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，如果本地设备上]{style="font-family:宋体"}[AVF]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1::3]{lang="EN-US"}[的虚拟转发器处于]{style="font-family:宋体"}[Listening]{lang="EN-US"}[状态，则马上将该虚拟转发器切换到]{style="font-family:宋体"}[Active]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_x931127586}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] vrrp ipv6 vrid 1 track 1 forwarder-switchover member-ip 1::3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_x1149991881}[在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上配置虚拟转发器权重监视]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[，当]{style="font-family:
宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[状态为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[所有虚拟转发器的权重都降低]{style="font-family:宋体"}[50]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> sysname-view]{lang="EN-US"}]{#struct_0_18718_x1832_x830500451}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] vrrp ipv6 vrid 1 track 1 weight reduced 50]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18718_x1832_1065196608}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_248778575}[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[上配置监视]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[，当]{style="font-family:
宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[状态为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[上]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[的优先级降低]{style="font-family:宋体"}[50]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_x197019836}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] vrrp ipv6 vrid 1 track 1 priority reduced 50]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_206889593}[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[上配置虚拟转发器监视]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[，当]{style="font-family:
宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[状态为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，如果本地设备上]{style="font-family:宋体"}[AVF]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1::3]{lang="EN-US"}[的虚拟转发器处于]{style="font-family:宋体"}[Listening]{lang="EN-US"}[状态，则马上将该虚拟转发器切换到]{style="font-family:宋体"}[Active]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18718_x1832_1407524574}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] vrrp ipv6 vrid 1 track 1 forwarder-switchover member-ip 1::3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18718_x1832_x25889362}[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[上配置虚拟转发器权重监视]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[，当]{style="font-family:
宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[状态为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[上]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[所有虚拟转发器的权重都降低]{style="font-family:宋体"}[50]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> sysname-view]{lang="EN-US"}]{#struct_0_18718_x1832_690525502}

[\[Sysname\] interface vlan-interface2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] vrrp ipv6 vrid 1 track 1 weight reduced 50]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18718_x1832_x1166406705}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **vrrp ipv6**]{lang="EN-US"}]{#struct_0_18718_x1832_1597887749}
:::::
