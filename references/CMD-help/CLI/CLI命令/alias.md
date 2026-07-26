::: {#1613693525 .myid}
[]{#_Toc404782160}[]{#struct_0_16211_x1303_x1593943514}[]{#_Toc389227637}[]{#_Toc389226357}

**CLI \-- CLI命令 \-- alias**

------------------------------------------------------------------------

[**[alias]{lang="EN-US"}**]{#struct_0_16211_x1303_x272379418}[命令用来给指定的命令或命令字符串配置别名。]{style="font-family:宋体"}

[**[undo alias]{lang="EN-US"}**]{#struct_0_16211_x1303_474867884}[命令用来取消相应配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16211_x1303_1520620660}

[**[alias ]{lang="EN-US"}***[alias command]{lang="EN-US"}*]{#struct_0_16211_x1303_1829254039}

[**[undo alias]{lang="EN-US"}**[ *alias*]{lang="EN-US"}]{#struct_0_16211_x1303_x1594009050}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16211_x1303_709280922}

[[系统为部分常用命令定义了缺省别名，如]{style="font-family:宋体"}]{#struct_0_16211_x1303_x1994144149}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-1]{lang="EN-US"}](?1613693525#_Ref396407562)[所示。系统定义的缺省别名无法取消。]{style="font-family:宋体"}

[]{#struct_0_16211_x1303_x1200436268}[[表1-1 ]{lang="EN-US"}[系统定义的缺省别名]{style="font-family:
黑体"}]{#_Ref396407562}

[]{#table_struct_0_x729345212}[[缺省别名]{style="font-family:黑体"}]{#struct_0_16211_x1303_1491519083}
:::

[[命令]{style="font-family:黑体"}]{#struct_0_16211_x1303_724319903}

[**[access-list]{lang="EN-US"}**]{#struct_0_16211_x1303_x1429191769}

[**[acl]{lang="EN-US"}**]{#struct_0_16211_x1303_x847133077}

[**[end]{lang="EN-US"}**]{#struct_0_16211_x1303_x1753965525}

[**[return]{lang="EN-US"}**]{#struct_0_16211_x1303_x1603912954}

[**[erase]{lang="EN-US"}**]{#struct_0_16211_x1303_x1933957460}

[**[delete]{lang="EN-US"}**]{#struct_0_16211_x1303_x2141355190}

[**[exit]{lang="EN-US"}**]{#struct_0_16211_x1303_2019485021}

[**[quit]{lang="EN-US"}**]{#struct_0_16211_x1303_352402182}

[**[hostname]{lang="EN-US"}**]{#struct_0_16211_x1303_413245430}

[**[sysname]{lang="EN-US"}**]{#struct_0_16211_x1303_915615280}

[**[logging]{lang="EN-US"}**]{#struct_0_16211_x1303_x1986249978}

[**[info-center]{lang="EN-US"}**]{#struct_0_16211_x1303_x1467000957}

[**[no]{lang="EN-US"}**]{#struct_0_16211_x1303_x29934842}

[**[undo]{lang="EN-US"}**]{#struct_0_16211_x1303_x72253202}

[**[show]{lang="EN-US"}**]{#struct_0_16211_x1303_x44832144}

[**[display]{lang="EN-US"}**]{#struct_0_16211_x1303_x839238906}

[**[write]{lang="EN-US"}**]{#struct_0_16211_x1303_x1588820279}

[**[save]{lang="EN-US"}**]{#struct_0_16211_x1303_1117076230}

[ ]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x2046885054}

[[系统视图]{style="font-family:宋体"}]{#struct_0_16211_x1303_333188161}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16211_x1303_2070976149}

[[network-admin]{lang="EN-US"}]{#struct_0_16211_x1303_1429201627}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16211_x1303_x876697413}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x1593550298}

[*[alias]{lang="EN-US"}*]{#struct_0_16211_x1303_1248552940}[：表示命令的别名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[个字符的字符串，区分大小写。别名不能是]{style="font-family:宋体"}[alias]{lang="EN-US"}[也不能包含空格。]{style="font-family:宋体"}

[*[command]{lang="EN-US"}*]{#struct_0_16211_x1303_x1451861511}[：表示配置别名的命令，可以为任意字符串。请用户自行保证该命令字符串能够被设备识别并执行，否则执行别名命令时将会失败。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16211_x1303_887911629}

[[本命令通常可以在如下情况使用：]{style="font-family:宋体"}]{#struct_0_16211_x1303_x1221575930}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[本命令可以为某条命令行配置别名，当执行该命令时可以直接使用别名以简化输入。例如将命令]{style="font-family:宋体"}**[display ip routing-table]{lang="EN-US"}**]{#struct_0_16211_x1303_x1778201724}[的别名配置为]{style="font-family:
宋体"}**[shiprt]{lang="EN-US"}**[，当需要使用]{style="font-family:
宋体"}**[display ip routing-table]{lang="EN-US"}**[查看设备当前生效的配置时，直接输入]{style="font-family:宋体"}**[shiprt]{lang="EN-US"}**[即可。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[本命令可以为命令行起始的一个或多个关键字配置别名，使其更符合用户习惯。所有使用该关键字开头的命令行都可以使用指定的别名命令来执行。例如，为]{style="font-family:宋体"}**[display ip]{lang="EN-US"}**]{#struct_0_16211_x1303_x1429878116}[命令定义的别名为]{style="font-family:宋体"}**[ship]{lang="EN-US"}**[，在使用所有以]{style="font-family:宋体"}**[display ip]{lang="EN-US"}**[关键字开头的命令行时，都可以使用]{style="font-family:宋体"}**[ship]{lang="EN-US"}**[进行配置。例如：]{style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[输入]{style="font-family:宋体"}]{#struct_0_16211_x1303_1457164146}**[ship routing-table]{lang="EN-US"}**[可以执行命令]{style="font-family:宋体"}**[display ip routing-table]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[输入]{style="font-family:宋体"}]{#struct_0_16211_x1303_1131172490}**[ship interface]{lang="EN-US"}**[可以执行命令]{style="font-family:宋体"}**[display ip interface]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置别名时，可以使用]{style="font-family:宋体"}]{#struct_0_16211_x1303_734739206}[\$n]{lang="EN-US"}[表示命令行中的参数或者关键字，这样既可以用别名替代部分关键字来简化输入，又可以根据实际需要指定不同的参数或者关键字，增加了灵活性。]{style="font-family:宋体"}[\$n]{lang="EN-US"}[最多可以使用]{style="font-family:宋体"}[9]{lang="EN-US"}[次，]{style="font-family:宋体"}[n]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[9]{lang="EN-US"}[的整数，表示参数或关键字出现的顺序。比如，将命令]{style="font-family:宋体"}**[display ip \$1 \| include \$2]{lang="EN-US"}**[的别名配置为]{style="font-family:宋体"}**[shinc]{lang="EN-US"}**[后]{style="font-family:宋体"}[，如果需要执行]{style="font-family:宋体"}**[display ip routing-table \| include Static]{lang="EN-US"}**[命令来筛选并查看路由表中的所有静态路由信息，可直接执行]{style="font-family:宋体"}**[shinc]{lang="EN-US"}**[ **routing-table Static**]{lang="EN-US"}[；同样如果需要执行]{style="font-family:宋体"}**[display ip interface \| include GigabitEthernet0/0/1]{lang="EN-US"}**[，则可直接执行]{style="font-family:宋体"}**[shinc interface GigabitEthernet0/0/1]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x1720045062}

[[\# ]{lang="EN-US"}]{#struct_0_16211_x1303_x1253730898}[配置命令]{style="font-family:宋体"}**[display ip routing-table]{lang="EN-US"}**[的别名为]{style="font-family:宋体"}**[shiprt]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16211_x1303_x1593615834}

[\[Sysname\] alias shiprt display ip routing-table]{lang="EN-US"}

[\[Sysname\] shiprt]{lang="EN-US"}

[Destinations : 12        Routes : 12]{lang="EN-US"}

[Destination/Mask   Proto   Pre Cost        NextHop         Interface ]{lang="EN-US"}

[0.0.0.0/32         Direct  0   0           127.0.0.1       InLoop0 ]{lang="EN-US"}

[3.3.3.3/32         Static  60  0           192.168.1.62    GE0/0 ]{lang="EN-US"}

[127.0.0.0/8        Direct  0   0           127.0.0.1       InLoop0 ]{lang="EN-US"}

[127.0.0.0/32       Direct  0   0           127.0.0.1       InLoop0 ]{lang="EN-US"}

[127.0.0.1/32       Direct  0   0           127.0.0.1       InLoop0 ]{lang="EN-US"}

[127.255.255.255/32 Direct  0   0           127.0.0.1       InLoop0 ]{lang="EN-US"}

[169.254.0.0/24     Direct  0   0           169.254.0.188   GE0/0 ]{lang="EN-US"}

[169.254.0.0/32     Direct  0   0           169.254.0.188   GE0/0 ]{lang="EN-US"}

[169.254.0.188/32   Direct  0   0           127.0.0.1       InLoop0 ]{lang="EN-US"}

[169.254.0.255/32   Direct  0   0           169.254.0.188   GE0/0 ]{lang="EN-US"}

[192.168.57.0/24    RIP     100 1           192.168.1.62    GE0/0 ]{lang="EN-US"}

[224.0.0.0/4        Direct  0   0           0.0.0.0         NULL0 ]{lang="EN-US"}

[224.0.0.0/24       Direct  0   0           0.0.0.0         NULL0 ]{lang="EN-US"}

[255.255.255.255/32 Direct  0   0           127.0.0.1       InLoop0 ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16211_x1303_x961825422}[配置命令]{style="font-family:宋体"}**[display ip \$1 \| include \$2]{lang="EN-US"}**[的别名为]{style="font-family:宋体"}**[shinc]{lang="EN-US"}**[，同时使用别名命令筛选并查看路由表中的所有静态路由信息。]{style="font-family:宋体"}

[[\[Sysname\] alias shinc display ip \$1 \| include \$2]{lang="EN-US"}]{#struct_0_16211_x1303_x323458863}

[\[Sysname\] shinc routing-table Static]{lang="EN-US"}

[3.3.3.3/32         Static  60  0           192.168.1.62    GE0/0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16211_x1303_x1596018783}[使用别名命令]{style="font-family:宋体"}**[shinc]{lang="EN-US"}**[筛选并查看路由表中的所有]{style="font-family:宋体"}[RIP]{lang="EN-US"}[路由信息。]{style="font-family:宋体"}

[[\[Sysname\] shinc routing-table RIP]{lang="EN-US"}]{#struct_0_16211_x1303_1999460413}

[192.168.57.0/24    RIP     100 1           192.168.1.62    GE0/0]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x1299536330}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display alias]{lang="EN-US"}**]{#struct_0_16211_x1303_x1594074585}

::: {#-2066564194 .myid}
[]{#_Toc404782161}[]{#struct_0_16211_x1303_x994239422}[]{#_Toc404069384}[]{#_Toc404069385}[]{#_Toc404069386}[]{#_Toc404069387}[]{#_Toc404069388}[]{#_Toc404069389}[]{#_Toc404069390}[]{#_Toc404069391}[]{#_Toc404069392}[]{#_Toc404069393}[]{#_Toc404069394}[]{#_Toc404069395}[]{#_Toc404069396}[]{#_Toc404069397}[]{#_Toc404069398}[]{#_Toc404069399}[]{#_Toc404069400}[]{#_Toc404069401}[]{#_Toc404069402}[]{#_Toc404069403}[]{#_Toc404069404}[]{#_Toc404069405}[]{#_Toc404069406}[]{#_Toc404069407}[]{#_Toc404069408}[]{#_Toc404069409}[]{#_Toc404069410}[]{#_Toc404069411}[]{#_Toc404069412}[]{#_Toc404069413}[]{#_Toc404069414}[]{#_Toc404069415}[]{#_Toc404069416}[]{#_Toc404069429}[]{#_Toc404069430}[]{#_Toc404069431}[]{#_Toc389752924}[]{#_Toc389752925}[]{#_Toc389752926}[]{#_Toc389752927}[]{#_Toc389752928}[]{#_Toc389752929}[]{#_Toc389752930}[]{#_Toc389752931}[]{#_Toc389752932}[]{#_Toc389752933}[]{#_Toc389752934}[]{#_Toc389752935}[]{#_Toc389752936}[]{#_Toc389752937}[]{#_Toc389752938}[]{#_Toc389752939}[]{#_Toc389752940}[]{#_Toc389752941}[]{#_Toc389752942}[]{#_Toc389752943}[]{#_Toc389752944}[]{#_Toc389752945}[]{#_Toc389752946}[]{#_Toc389752947}[]{#_Toc389752948}[]{#_Toc389752949}[]{#_Toc389752950}[]{#_Toc389752951}[]{#_Toc389752952}[]{#_Toc389752953}[]{#_Toc389752954}[]{#_Toc389752955}[]{#_Toc389752956}[]{#_Toc389752957}[]{#_Toc389752958}[]{#_Toc389752959}[]{#_Toc389752960}[]{#_Toc389752961}[]{#_Toc389752962}[]{#_Toc389752963}[]{#_Toc389752964}[]{#_Toc389752965}[]{#_Toc389752966}[]{#_Toc389752967}[]{#_Toc389752968}[]{#_Toc389752969}[]{#_Toc389752970}[]{#_Toc389752971}

**CLI \-- CLI命令 \-- display \| { begin \| exclude \| include }**

------------------------------------------------------------------------

[**[display \|]{lang="EN-US"}**[ { **begin** \| **exclude** \| **include** }]{lang="EN-US"}]{#struct_0_16211_x1303_1819741198}[命令用来使用正则表达式对显示信息进行过滤。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x1635217374}

[**[display ]{lang="EN-US"}***[command]{lang="EN-US"}*[ **\|** { **begin** \| **exclude** \| **include** } *regular-expression*]{lang="EN-US"}]{#struct_0_16211_x1303_1477678354}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x1861251096}

[[任意视图]{style="font-family:宋体"}]{#struct_0_16211_x1303_1805248592}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16211_x1303_45140219}

[[network-admin]{lang="EN-US"}]{#struct_0_16211_x1303_x1042841558}

[[network-operator]{lang="EN-US"}]{#struct_0_16211_x1303_x959112960}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16211_x1303_694880458}

[[mdc-operator]{lang="EN-US"}]{#struct_0_16211_x1303_x171485979}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16211_x1303_492724309}

[*[command]{lang="EN-US"}*]{#struct_0_16211_x1303_1477678353}[：命令关键字，取值可以通过输入]{style="font-family:宋体"}[?]{lang="EN-US"}[来获得。]{style="font-family:宋体"}

[**[begin]{lang="EN-US"}**]{#struct_0_16211_x1303_x1861578776}[：从包含指定正则表达式的行开始显示。]{style="font-family:宋体"}

[**[exclude]{lang="EN-US"}**]{#struct_0_16211_x1303_1304144577}[：只显示不包含指定正则表达式的行。]{style="font-family:宋体"}

[**[include]{lang="EN-US"}**]{#struct_0_16211_x1303_780138042}[：只显示包含指定正则表达式的行。]{style="font-family:宋体"}

[*[regular-expression]{lang="EN-US"}*]{#struct_0_16211_x1303_x10221055}[：表示正则表达式，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16211_x1303_1081209019}

[[用]{style="font-family:宋体"}**[display]{lang="EN-US"}**]{#struct_0_16211_x1303_869877622}[命令查看显示信息时，用户可以使用正则表达式来过滤显示信息，以便快速的找到自己关注的信息。关于正则表达式的详细描述请参考"基础配置指导"中的"]{style="font-family:宋体"}[CLI]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16211_x1303_783440742}

[[\# ]{lang="EN-US"}]{#struct_0_16211_x1303_x1616667426}[查看包含]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的配置。]{style="font-family:宋体"}

[[\<Sysname\> display current-configuration \| include vlan]{lang="EN-US"}]{#struct_0_16211_x1303_1477678352}

[vlan 1]{lang="NL-BE"}

[vlan 999]{lang="NL-BE"}

[ port access vlan 999]{lang="NL-BE"}
:::

::: {#-1062601475 .myid}
[]{#_Toc404782162}[]{#struct_0_16211_x1303_x1861644312}

**CLI \-- CLI命令 \-- display \| by-linenum**

------------------------------------------------------------------------

[**[display \| by-linenum]{lang="EN-US"}**]{#struct_0_16211_x1303_2060858536}[命令用来查看带行号的显示信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x184966802}

[**[display ]{lang="EN-US"}***[command]{lang="EN-US"}*[ **\|** **by-linenum**]{lang="EN-US"}]{#struct_0_16211_x1303_1963798149}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16211_x1303_1563864727}

[[任意视图]{style="font-family:宋体"}]{#struct_0_16211_x1303_x453696207}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16211_x1303_1365522217}

[[network-admin]{lang="EN-US"}]{#struct_0_16211_x1303_1477678351}

[[network-operator]{lang="EN-US"}]{#struct_0_16211_x1303_x1861447704}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16211_x1303_848228422}

[[mdc-operator]{lang="EN-US"}]{#struct_0_16211_x1303_383607723}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x1742033211}

[*[command]{lang="EN-US"}*]{#struct_0_16211_x1303_x1872917300}[：命令关键字，取值可以通过输入]{style="font-family:宋体"}[?]{lang="EN-US"}[来获得。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x516918676}

[[使用本命令时，系统在显示信息的同时会自动在每行显示信息的前面添加行号。以便当显示信息较多时，能够迅速定位到某行信息。]{style="font-family:宋体"}]{#struct_0_16211_x1303_x1731627050}

[[行号占]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_16211_x1303_1743708867}[个字符，通常行号后面接"]{style="font-family:宋体"}[:]{lang="EN-US"}["。当]{style="font-family:宋体"}**[by-linenum]{lang="EN-US"}**[和]{style="font-family:宋体"}**[begin]{lang="EN-US"}**[参数一起使用时，行号后面还可能接"]{style="font-family:宋体"}[-]{lang="EN-US"}["，其中"]{style="font-family:宋体"}[:]{lang="EN-US"}["表示该行符合匹配规则，"]{style="font-family:宋体"}[-]{lang="EN-US"}["表示该行不符合匹配规则。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16211_x1303_1477678350}

[[\# ]{lang="EN-US"}]{#struct_0_16211_x1303_x1861513240}[显示]{style="font-family:宋体"}[VLAN 999]{lang="EN-US"}[信息的同时显示行号。]{style="font-family:宋体"}

[[\<Sysname\> display vlan 999 \| by-linenum]{lang="EN-US"}]{#struct_0_16211_x1303_x1949863284}

[    1:  VLAN ID: 999]{lang="EN-US"}

[    2:  VLAN type: Static]{lang="EN-US"}

[    3:  Route interface: Configured]{lang="EN-US"}

[    4:  IP address: 192.168.2.1]{lang="EN-US"}

[    5:  Subnet mask: 255.255.255.0]{lang="EN-US"}

[    6:  Description: For LAN Access]{lang="EN-US"}

[    7:  Name: VLAN 0999]{lang="EN-US"}

[    8:  Tagged ports:   None]{lang="EN-US"}

[    9:  Untagged ports:]{lang="EN-US"}

[   10:     GigabitEthernet1/0/1]{lang="EN-US"}

[[\# ]{lang="NL-BE"}]{#struct_0_16211_x1303_x701074117}[查看]{style="font-family:宋体"}[当前配置]{style="font-family:宋体"}[，从包含"]{style="font-family:宋体"}[user-group]{lang="NL-BE"}["字符串的行开始到最后一行配置信息，并同时显示行号。（行号后为"]{style="font-family:宋体"}[:]{lang="NL-BE"}["表示该行包含"]{style="font-family:宋体"}[user-group]{lang="NL-BE"}["字符串，行号后为"]{style="font-family:宋体"}[-]{lang="NL-BE"}["表示该行不包含"]{style="font-family:宋体"}[user-group]{lang="NL-BE"}["字符串。）]{style="font-family:宋体"}

[[\<Sysname\> display ]{lang="NL-BE"}[current-configuration]{lang="EN-US"}]{#struct_0_16211_x1303_x429931798}[ \| by-linenum begin user-group]{lang="NL-BE"}

[  114:  user-group system]{lang="NL-BE"}

[  115-  \#]{lang="NL-BE"}

[[  116-  return]{lang="NL-BE"}]{#struct_0_16211_x1303_1477678349}
:::

::: {#1801766413 .myid}
[]{#_Toc404782163}[]{#struct_0_16211_x1303_x1861971991}

**CLI \-- CLI命令 \-- display \>**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **\>**]{lang="EN-US"}]{#struct_0_16211_x1303_x1831175550}[命令用来将显示信息独立保存到指定文件。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16211_x1303_1821866630}

[**[display]{lang="EN-US"}**[ *command* **\>** *filename*]{lang="EN-US"}]{#struct_0_16211_x1303_x1104328285}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16211_x1303_1454258537}

[[任意视图]{style="font-family:宋体"}]{#struct_0_16211_x1303_x384906712}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16211_x1303_1780756102}

[[network-admin]{lang="EN-US"}]{#struct_0_16211_x1303_564224070}

[[network-operator]{lang="EN-US"}]{#struct_0_16211_x1303_1477678348}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16211_x1303_x1862037527}

[[mdc-operator]{lang="EN-US"}]{#struct_0_16211_x1303_x1784675165}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16211_x1303_1530522727}

[*[command]{lang="EN-US"}*]{#struct_0_16211_x1303_x1954808401}[：命令关键字，取值可以通过输入]{style="font-family:宋体"}[?]{lang="EN-US"}[来获得。]{style="font-family:宋体"}

[*[filename]{lang="EN-US"}*]{#struct_0_16211_x1303_x280287782}[：文件名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x1657757167}

[**[display]{lang="EN-US"}**]{#struct_0_16211_x1303_1561674178}[命令显示的内容通常是统计信息、功能是否使能以及功能的相关参数配置，这些信息在设备运行过程中会随着时间或者用户的配置而改变。使用本命令可以将当前显示信息保存到指定文件，可供用户随时比对和查看。]{style="font-family:宋体"}

[[执行本命令时，如果]{style="font-family:宋体"}*[filename]{lang="EN-US"}*]{#struct_0_16211_x1303_x1110628880}[不存在，系统会先创建该文件，再保存；如果]{style="font-family:宋体"}*[filename]{lang="EN-US"}*[已存在，则会覆盖原文件的内容。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x94137067}

[[\# ]{lang="EN-US"}]{#struct_0_16211_x1303_x426110732}[将]{style="font-family:宋体"}[display vlan 1]{lang="EN-US"}[的显示信息保存到指定文件]{style="font-family:宋体"}[vlan.txt]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> display vlan 1 \> vlan.txt]{lang="EN-US"}]{#struct_0_16211_x1303_x1121124140}

[[查看]{style="font-family:宋体"}[vlan.txt]{lang="EN-US"}]{#struct_0_16211_x1303_758683318}[的内容，验证]{style="font-family:宋体"}**[display]{lang="EN-US"}**[ **\>**]{lang="EN-US"}[命令的执行效果。]{style="font-family:宋体"}

[[\<Sysname\> more vlan.txt]{lang="EN-US"}]{#struct_0_16211_x1303_1925638736}

[VLAN ID: 1]{lang="EN-US"}

[ VLAN type: Static]{lang="EN-US"}

[ Route interface: Not configured]{lang="EN-US"}

[ Description: VLAN 0001]{lang="EN-US"}

[ Name: VLAN 0001]{lang="EN-US"}

[ Tagged ports:   None]{lang="EN-US"}

[ Untagged ports:]{lang="EN-US"}

[    GigabitEthernet1/0/2]{lang="EN-US"}
:::

::: {#1802608593 .myid}
[]{#_Toc404782164}[]{#struct_0_16211_x1303_x51455885}[]{#_Toc255981043}[]{#_Toc255995942}[]{#_Toc255995976}

**CLI \-- CLI命令 \-- display \>\>**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **\>\>**]{lang="EN-US"}]{#struct_0_16211_x1303_x370968744}[命令用来将显示信息以追加方式保存到指定文件。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x94137068}

[**[display]{lang="EN-US"}**[ *command* **\>\>** *filename*]{lang="EN-US"}]{#struct_0_16211_x1303_x426110731}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x1121189676}

[[任意视图]{style="font-family:宋体"}]{#struct_0_16211_x1303_555363035}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x1971579689}

[[network-admin]{lang="EN-US"}]{#struct_0_16211_x1303_x640941770}

[[network-operator]{lang="EN-US"}]{#struct_0_16211_x1303_x1904114102}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16211_x1303_1348132944}

[[mdc-operator]{lang="EN-US"}]{#struct_0_16211_x1303_x1661904251}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x94137069}

[*[command]{lang="EN-US"}*]{#struct_0_16211_x1303_x426110730}[：命令关键字，取值可以通过输入]{style="font-family:宋体"}[?]{lang="EN-US"}[来获得。]{style="font-family:宋体"}

[*[filename]{lang="EN-US"}*]{#struct_0_16211_x1303_x1121255212}[：文件名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x352858480}

[**[display]{lang="EN-US"}**]{#struct_0_16211_x1303_x297035795}[命令显示的内容通常是统计信息、功能是否使能以及功能的相关参数配置，这些信息在设备运行过程中会随着时间或者用户的配置而改变。使用本命令可以将当前显示信息保存到指定文件，可供用户随时比对和查看。]{style="font-family:宋体"}

[[执行本命令时，如果]{style="font-family:宋体"}*[filename]{lang="EN-US"}*]{#struct_0_16211_x1303_870482697}[不存在，系统会先创建该文件，再保存。如果]{style="font-family:宋体"}*[filename]{lang="EN-US"}*[已存在，则新保存的内容会追加到文件]{style="font-family:宋体"}*[filename]{lang="EN-US"}*[的尾部。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16211_x1303_1316759477}

[[\# ]{lang="EN-US"}]{#struct_0_16211_x1303_x396282616}[将]{style="font-family:宋体"}[display vlan 999]{lang="EN-US"}[的显示信息以追加方式保存到指定文件]{style="font-family:宋体"}[vlan.txt]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> display vlan 999 \>\> vlan.txt]{lang="EN-US"}]{#struct_0_16211_x1303_x564118452}

[[查看]{style="font-family:宋体"}[vlan.txt]{lang="EN-US"}]{#struct_0_16211_x1303_x94137070}[的内容，验证]{style="font-family:宋体"}**[display \>\>]{lang="EN-US"}**[命令的执行效果。]{style="font-family:宋体"}

[[\<Sysname\> more vlan.txt]{lang="EN-US"}]{#struct_0_16211_x1303_1530204397}

[VLAN ID: 1]{lang="EN-US"}

[ VLAN type: Static]{lang="EN-US"}

[ Route interface: Not configured]{lang="EN-US"}

[ Description: VLAN 0001]{lang="EN-US"}

[ Name: VLAN 0001]{lang="EN-US"}

[ Tagged ports:   None]{lang="EN-US"}

[ Untagged ports:]{lang="EN-US"}

[    GigabitEthernet1/0/2]{lang="EN-US"}

[ ]{lang="EN-US"}

[ VLAN ID: 999]{lang="EN-US"}

[ VLAN type: Static]{lang="EN-US"}

[ Route interface: Configured]{lang="EN-US"}

[ IP address: 192.168.2.1]{lang="EN-US"}

[ Subnet mask: 255.255.255.0]{lang="EN-US"}

[ Description: For LAN Access]{lang="EN-US"}

[ Name: VLAN 0999]{lang="EN-US"}

[ Tagged ports:   None]{lang="EN-US"}

[ Untagged ports:]{lang="EN-US"}

[    GigabitEthernet1/0/1]{lang="EN-US"}
:::

::: {#-1985717589 .myid}
[]{#_Toc404782165}[]{#struct_0_16211_x1303_x1249449023}

**CLI \-- CLI命令 \-- display alias**

------------------------------------------------------------------------

[**[display alias]{lang="EN-US"}**]{#struct_0_16211_x1303_1282224113}[命令用来查看命令别名的相关配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16211_x1303_1479434332}

[**[display alias ]{lang="EN-US"}**[\[ ]{lang="EN-US"}*[alias]{lang="EN-US"}*[ \]]{lang="EN-US"}]{#struct_0_16211_x1303_x2120677648}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x1086817829}

[[任意视图]{style="font-family:宋体"}]{#struct_0_16211_x1303_772138763}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16211_x1303_516138334}

[[network-admin]{lang="EN-US"}]{#struct_0_16211_x1303_1096720576}

[[network-operator]{lang="EN-US"}]{#struct_0_16211_x1303_x1374463917}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16211_x1303_1298131539}

[[mdc-operator]{lang="EN-US"}]{#struct_0_16211_x1303_x876616718}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x86649609}

[*[alias]{lang="EN-US"}*]{#struct_0_16211_x1303_x877601555}[：表示配置的命令别名。不指定该参数，则显示所有的已配置的命令别名。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16211_x1303_457281065}

[[\# ]{lang="EN-US"}]{#struct_0_16211_x1303_x703586666}[查看系统中配置的所有命令别名。]{style="font-family:宋体"}

[[\<Sysname\> display alias]{lang="EN-US"}]{#struct_0_16211_x1303_x1652733550}

[Index     Alias                Command key]{lang="EN-US"}

[1         access-list          acl]{lang="EN-US"}

[2         end                  return]{lang="EN-US"}

[3         erase                delete]{lang="EN-US"}

[4         exit                 quit]{lang="EN-US"}

[5         hostname             sysname]{lang="EN-US"}

[6         logging              info-center]{lang="EN-US"}

[7         no                   undo]{lang="EN-US"}

[8         shinc                display \$1 \| include \$2]{lang="EN-US"}

[9         show                 display]{lang="EN-US"}

[10        sirt                 display ip routing-table]{lang="EN-US"}

[11        write                save]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16211_x1303_x1249936038}[查看别名命令]{style="font-family:宋体"}**[shinc]{lang="EN-US"}**[表示的命令字符串。]{style="font-family:宋体"}

[[\<Sysname\> display alias shinc]{lang="EN-US"}]{#struct_0_16211_x1303_1164593031}

[Alias                Command key]{lang="EN-US"}

[shinc                display ip \$1 \| include \$2]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[ display alias]{lang="EN-US"}]{#struct_0_16211_x1303_x1493651207}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x259911323}[[字段]{style="font-family:黑体"}]{#struct_0_16211_x1303_363689085}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16211_x1303_x696317139}

[[Index]{lang="EN-US"}]{#struct_0_16211_x1303_164010619}

[[索引号]{style="font-family:宋体"}]{#struct_0_16211_x1303_x1202394856}

[[Alias]{lang="EN-US"}]{#struct_0_16211_x1303_x1226161292}

[[别名]{style="font-family:宋体"}]{#struct_0_16211_x1303_719984981}

[[Command key]{lang="EN-US"}]{#struct_0_16211_x1303_x574150981}

[[命令字符串]{style="font-family:宋体"}]{#struct_0_16211_x1303_763363827}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x846098960}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[alias]{lang="EN-US"}**]{#struct_0_16211_x1303_1377875264}

::: {#-599367759 .myid}
[]{#_Toc404782166}[]{#struct_0_16211_x1303_1882746650}[]{#_Toc291753303}[]{#_Toc389752976}[]{#_Toc389752977}[]{#_Toc389752978}[]{#_Toc389752979}[]{#_Toc389752980}[]{#_Toc389752981}[]{#_Toc389752982}[]{#_Toc389752983}[]{#_Toc389752984}[]{#_Toc389752985}[]{#_Toc389752986}[]{#_Toc389752987}[]{#_Toc389752988}[]{#_Toc389752989}[]{#_Toc389752990}[]{#_Toc389752991}[]{#_Toc389752992}[]{#_Toc389752993}[]{#_Toc389752994}[]{#_Toc389753010}[]{#_Toc389753011}[]{#_Toc389753012}[]{#_Toc389753013}

**CLI \-- CLI命令 \-- display history-command**

------------------------------------------------------------------------

[**[display history-command]{lang="EN-US"}**]{#struct_0_16211_x1303_x749051828}[命令用来显示当前登录用户成功执行的历史命令。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16211_x1303_387155206}

[**[display history-command]{lang="EN-US"}**]{#struct_0_16211_x1303_x1944512994}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x1922620234}

[[任意视图]{style="font-family:宋体"}]{#struct_0_16211_x1303_x94137075}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16211_x1303_1530204402}

[[network-admin]{lang="EN-US"}]{#struct_0_16211_x1303_1185497840}

[[network-operator]{lang="EN-US"}]{#struct_0_16211_x1303_1162269883}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16211_x1303_x495246391}

[[mdc-operator]{lang="EN-US"}]{#struct_0_16211_x1303_x733081936}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x1394774762}

[[用户登录设备后，系统会给每个用户自动分配一个历史命令缓冲区，用于存放用户本次登录用户成功执行的命令行，以便用户查看和调用。历史命令缓存区有大小限制，缺省保存]{style="font-family:宋体"}[10]{lang="EN-US"}]{#struct_0_16211_x1303_x1256346130}[条命令，用户也可以通过]{style="font-family:宋体"}**[history-command max-size]{lang="EN-US"}**[命令来修改大小。当数目达到上限时，系统会自动删除最早的记录，来保存最新成功执行的命令。]{style="font-family:宋体"}

[[如果用户退出登录，系统会自动清除该历史命令缓存区的所有记录。]{style="font-family:宋体"}]{#struct_0_16211_x1303_1976238649}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x94137076}

[[\# ]{lang="EN-US"}]{#struct_0_16211_x1303_1530204403}[显示历史命令缓存区内保存的命令。]{style="font-family:宋体"}

[[\<Sysname\> display history-command]{lang="EN-US"}]{#struct_0_16211_x1303_1185563376}

[  system-view]{lang="EN-US"}

[  vlan 2]{lang="EN-US"}

[  quit]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x1570569681}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[history-command max-size]{lang="EN-US"}**]{#struct_0_16211_x1303_x1015376942}[（基础配置命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[登录设备）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#-1573173420 .myid}
[]{#_Toc404782167}[]{#struct_0_16211_x1303_x718354844}

**CLI \-- CLI命令 \-- display history-command all**

------------------------------------------------------------------------

[**[display history-command all]{lang="EN-US"}**]{#struct_0_16211_x1303_1068737731}[命令用来显示所有登录用户成功执行的历史命令。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x1178303573}

[**[display history-command all]{lang="EN-US"}**]{#struct_0_16211_x1303_x2050452203}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16211_x1303_986907426}

[[任意视图]{style="font-family:宋体"}]{#struct_0_16211_x1303_x306232378}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16211_x1303_1453393795}

[[network-admin]{lang="EN-US"}]{#struct_0_16211_x1303_x611858596}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16211_x1303_x241928629}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x2050452204}

[[系统中有一个共享历史命令缓冲区，用于存放所有登录用户成功执行的命令行，以便用户查看（不能调用）。历史命令缓存区的大小固定为]{style="font-family:宋体"}[1024]{lang="EN-US"}]{#struct_0_16211_x1303_x1385745569}[条，不可配置。当数目达到上限时，系统会自动删除最早的记录，来保存最新成功执行的命令。]{style="font-family:宋体"}

[[即便用户退出登录，系统也不会清除共享历史命令缓存区中该用户的历史命令记录。]{style="font-family:宋体"}]{#struct_0_16211_x1303_2015932241}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16211_x1303_1291324961}

[[\# ]{lang="EN-US"}]{#struct_0_16211_x1303_x1879102662}[显示所有登录用户成功执行的历史命令。]{style="font-family:宋体"}

[[\<Sysname\> display history-command all]{lang="EN-US"}]{#struct_0_16211_x1303_659532031}

[  Date       Time     Terminal   Ip              User]{lang="EN-US"}

[  03/16/2012 20:03:33 vty0       192.168.1.26    \*\*]{lang="EN-US"}

[  Cmd:dis his all]{lang="EN-US"}

[ ]{lang="EN-US"}

[  03/16/2012 20:03:29 vty0       192.168.1.26    \*\*]{lang="EN-US"}

[  Cmd:sys]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display history-command all]{lang="EN-US"}]{#struct_0_16211_x1303_x2113062267}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x108172810}[[字段]{style="font-family:黑体"}]{#struct_0_16211_x1303_x2050452205}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16211_x1303_180338372}

[[Date]{lang="EN-US"}]{#struct_0_16211_x1303_632008564}

[[执行命令行的日期]{style="font-family:宋体"}]{#struct_0_16211_x1303_x1944471418}

[[Time]{lang="EN-US"}]{#struct_0_16211_x1303_x631283139}

[[执行命令行的时间]{style="font-family:宋体"}]{#struct_0_16211_x1303_1198020234}

[[Terminal]{lang="EN-US"}]{#struct_0_16211_x1303_x168863570}

[[执行命令的用户使用的登录用户线]{style="font-family:宋体"}]{#struct_0_16211_x1303_x2050452206}

[[Ip]{lang="EN-US"}]{#struct_0_16211_x1303_1746422313}

[[执行命令的用户使用的登录]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_16211_x1303_609049116}

[[User]{lang="EN-US"}]{#struct_0_16211_x1303_x1390754289}

[[执行命令的用户使用的登录用户名]{style="font-family:宋体"}]{#struct_0_16211_x1303_x213588968}

[[Cmd]{lang="EN-US"}]{#struct_0_16211_x1303_x1860995240}

[[执行的命令（和用户的输入保持一致）]{style="font-family:宋体"}]{#struct_0_16211_x1303_x2050452207}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x982461042}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display history-command]{lang="EN-US"}**]{#struct_0_16211_x1303_991934857}

::: {#39677947 .myid}
[]{#_Toc404782168}[]{#struct_0_16211_x1303_477022247}[]{#_Toc296419235}

**CLI \-- CLI命令 \-- display hotkey**

------------------------------------------------------------------------

[**[display hotkey]{lang="EN-US"}**]{#struct_0_16211_x1303_x335804044}[命令用来显示系统支持的快捷键及其含义。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x882110297}

[**[display hotkey]{lang="EN-US"}**]{#struct_0_16211_x1303_x1134345120}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x919156967}

[[任意视图]{style="font-family:宋体"}]{#struct_0_16211_x1303_x2050452208}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16211_x1303_227392539}

[[network-admin]{lang="EN-US"}]{#struct_0_16211_x1303_1992459525}

[[network-operator]{lang="EN-US"}]{#struct_0_16211_x1303_x1944764744}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16211_x1303_x1364691747}

[[mdc-operator]{lang="EN-US"}]{#struct_0_16211_x1303_368780798}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16211_x1303_1952172880}

[[\# ]{lang="EN-US"}]{#struct_0_16211_x1303_x1945027660}[显示系统支持的快捷键及其含义。]{style="font-family:宋体"}

[[\<Sysname\> display hotkey]{lang="EN-US"}]{#struct_0_16211_x1303_x2050452210}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- Hotkeys \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[           -Defined command hotkeys-]{lang="EN-US"}

[CTRL_G display current-configuration]{lang="EN-US"}

[CTRL_L display ip routing-table]{lang="EN-US"}

[CTRL_O undo debugging all]{lang="EN-US"}

[ ]{lang="EN-US"}

[           -Undefined command hotkeys-]{lang="EN-US"}

[CTRL_T NULL]{lang="EN-US"}

[CTRL_U NULL]{lang="EN-US"}

[ ]{lang="EN-US"}

[           -System-reserved hotkeys-]{lang="EN-US"}

[CTRL_A  Move the cursor to the beginning of the line.]{lang="EN-US"}

[CTRL_B  Move the cursor one character to the left.]{lang="EN-US"}

[CTRL_C  Stop the current command.]{lang="EN-US"}

[CTRL_D  Erase the character at the cursor.]{lang="EN-US"}

[CTRL_E  Move the cursor to the end of the line.]{lang="EN-US"}

[CTRL_F  Move the cursor one character to the right.]{lang="EN-US"}

[CTRL_H  Erase the character to the left of the cursor.]{lang="EN-US"}

[CTRL_K  Abort the connection request.]{lang="EN-US"}

[CTRL_N  Display the next command in the history buffer.]{lang="EN-US"}

[CTRL_P  Display the previous command in the history buffer.]{lang="EN-US"}

[CTRL_R  Redisplay the current line.]{lang="EN-US"}

[CTRL_V  Paste text from the clipboard.]{lang="EN-US"}

[CTRL_W  Delete the word to the left of the cursor.]{lang="EN-US"}

[CTRL_X  Delete all characters from the beginning of the line to the cursor.]{lang="EN-US"}

[CTRL_Y  Delete all characters from the cursor to the end of the line.]{lang="EN-US"}

[CTRL_Z  Return to the User View.]{lang="EN-US"}

[CTRL\_\]  Kill incoming connection or redirect connection.]{lang="EN-US"}

[ESC_B   Move the cursor back one word.]{lang="EN-US"}

[ESC_D   Delete all characters from the cursor to the end of the word.]{lang="EN-US"}

[ESC_F   Move the cursor forward one word.]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display hotkey]{lang="EN-US"}]{#struct_0_16211_x1303_583557363}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x112021216}[[字段]{style="font-family:黑体"}]{#struct_0_16211_x1303_1864464662}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16211_x1303_x1959189070}

[[Defined command hotkeys]{lang="EN-US"}]{#struct_0_16211_x1303_x571909378}

[[已定义的快捷键]{style="font-family:宋体"}]{#struct_0_16211_x1303_x545658515}

[[Undefined command hotkeys]{lang="EN-US"}]{#struct_0_16211_x1303_x2050452211}

[[未定义的快捷键]{style="font-family:宋体"}]{#struct_0_16211_x1303_x2145325992}

[[System-reserved hotkeys]{lang="EN-US"}]{#struct_0_16211_x1303_1038254168}

[]{#struct_0_16211_x1303_1879458547}[[系统保留的快捷键]{style="font-family:宋体"}]{#_Ref300394622}[。每个保留快捷键的作用请参见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-5]{lang="EN-US"}](?39677947#_Ref325619217)

[ ]{lang="EN-US"}

[]{#struct_0_16211_x1303_x868970585}[[表1-5 ]{lang="EN-US"}[系统保留的快捷键]{style="font-family:
黑体"}]{#_Ref325619217}

[]{#table_struct_0_x112493708}[[快捷键]{style="font-family:黑体"}]{#struct_0_16211_x1303_2073698737}

[[功能]{style="font-family:黑体"}]{#struct_0_16211_x1303_x1368620049}

[[\<Ctrl+A\>]{lang="EN-US"}]{#struct_0_16211_x1303_x2050452212}

[[将光标移动到当前行的开头]{style="font-family:宋体"}]{#struct_0_16211_x1303_x579242051}

[[\<Ctrl+B\>]{lang="EN-US"}]{#struct_0_16211_x1303_x1521751281}

[[将光标向左移动一个字符]{style="font-family:宋体"}]{#struct_0_16211_x1303_x823964077}

[[\<Ctrl+C\>]{lang="EN-US"}]{#struct_0_16211_x1303_x1617219764}

[[停止当前正在执行的功能]{style="font-family:宋体"}]{#struct_0_16211_x1303_x866638042}

[[\<Ctrl+D\>]{lang="EN-US"}]{#struct_0_16211_x1303_288199957}

[[删除当前光标所在位置的字符]{style="font-family:宋体"}]{#struct_0_16211_x1303_x1714800284}

[[\<Ctrl+E\>]{lang="EN-US"}]{#struct_0_16211_x1303_x425262874}

[[将光标移动到当前行的末尾]{style="font-family:宋体"}]{#struct_0_16211_x1303_x155653659}

[[\<Ctrl+F\>]{lang="EN-US"}]{#struct_0_16211_x1303_x1455581955}

[[将光标向右移动一个字符]{style="font-family:宋体"}]{#struct_0_16211_x1303_1218933123}

[[\<Ctrl+H\>]{lang="EN-US"}]{#struct_0_16211_x1303_288199956}

[[删除光标左侧的一个字符]{style="font-family:宋体"}]{#struct_0_16211_x1303_x1714800283}

[[\<Ctrl+K\>]{lang="EN-US"}]{#struct_0_16211_x1303_1497051427}

[[终止呼出的连接]{style="font-family:宋体"}]{#struct_0_16211_x1303_1127605268}

[[\<Ctrl+R\>]{lang="EN-US"}]{#struct_0_16211_x1303_570217927}

[[重新显示当前行信息]{style="font-family:宋体"}]{#struct_0_16211_x1303_288199955}

[[\<Ctrl+V\>]{lang="EN-US"}]{#struct_0_16211_x1303_x1714800282}

[[粘贴剪贴板的内容]{style="font-family:宋体"}]{#struct_0_16211_x1303_x1231831928}

[[\<Ctrl+W\>]{lang="EN-US"}]{#struct_0_16211_x1303_1428047512}

[[删除光标左侧连续字符串内的所有字符]{style="font-family:宋体"}]{#struct_0_16211_x1303_x858210492}

[[\<Ctrl+X\>]{lang="EN-US"}]{#struct_0_16211_x1303_288199954}

[[删除光标左侧所有的字符]{style="font-family:宋体"}]{#struct_0_16211_x1303_x1714800281}

[[\<Ctrl+Y\>]{lang="EN-US"}]{#struct_0_16211_x1303_334252013}

[[删除光标所在位置及其右侧所有的字符]{style="font-family:宋体"}]{#struct_0_16211_x1303_1136343996}

[[\<Ctrl+Z\>]{lang="EN-US"}]{#struct_0_16211_x1303_288199953}

[[退回到用户视图]{style="font-family:宋体"}]{#struct_0_16211_x1303_x1714800280}

[[\<Ctrl+\]\>]{lang="EN-US"}]{#struct_0_16211_x1303_1900335954}

[[终止当前连接]{style="font-family:宋体"}]{#struct_0_16211_x1303_1315662609}

[[\<Esc+B\>]{lang="EN-US"}]{#struct_0_16211_x1303_1713642413}

[[将光标移动到左侧连续字符串的首字符处]{style="font-family:宋体"}]{#struct_0_16211_x1303_288199952}

[[\<Esc+D\>]{lang="EN-US"}]{#struct_0_16211_x1303_x1714800279}

[[删除光标所在位置及其右侧连续字符串内的所有字符]{style="font-family:宋体"}]{#struct_0_16211_x1303_x22306027}

[[\<Esc+F\>]{lang="EN-US"}]{#struct_0_16211_x1303_x308543375}

[[将光标向右移到下一个连续字符串之前]{style="font-family:宋体"}]{#struct_0_16211_x1303_288199951}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x1013212251}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hotkey]{lang="EN-US"}**]{#struct_0_16211_x1303_600392074}

::: {#1990966527 .myid}
[]{#_Toc404782169}[]{#struct_0_16211_x1303_x1457453296}[]{#_Toc54432786}

**CLI \-- CLI命令 \-- hotkey**

------------------------------------------------------------------------

[**[hotkey]{lang="EN-US"}**]{#struct_0_16211_x1303_1133347820}[命令用来为快捷键指定对应的命令行。]{style="font-family:宋体"}

[**[undo hotkey]{lang="EN-US"}**]{#struct_0_16211_x1303_183482223}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x2008482486}

[**[hotkey ]{lang="EN-US"}**[{ **ctrl_g** \| **ctrl_l** \| **ctrl_o** \| **ctrl_t** \| **ctrl_u** } *command*]{lang="EN-US"}]{#struct_0_16211_x1303_288199948}

[**[undo hotkey ]{lang="EN-US"}**[{ **ctrl_g** \| **ctrl_l** \| **ctrl_o** \| **ctrl_t** \| **ctrl_u** }]{lang="EN-US"}]{#struct_0_16211_x1303_623851875}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x1013212252}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[\<]{lang="EN-US"}[Ctrl+G\>]{lang="EN-US"}]{#struct_0_16211_x1303_1003676601}[对应命令]{lang="EN-US" style="font-family:宋体"}**[display current-configuration]{lang="EN-US"}**[（显示当前配置）。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[\<]{lang="EN-US"}[Ctrl+L\>]{lang="EN-US"}]{#struct_0_16211_x1303_2036534494}[对应命令]{lang="EN-US" style="font-family:宋体"}**[display ip routing-table]{lang="EN-US"}**[（显示]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由表信息）。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[\<]{lang="EN-US"}[Ctrl+O\>]{lang="EN-US"}]{#struct_0_16211_x1303_x287492536}[对应命令]{lang="EN-US" style="font-family:宋体"}**[undo debugging all]{lang="EN-US"}**[（关闭设备支持的所有功能项的调试开关）。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[\<Ctrl+T\>]{lang="EN-US"}]{#struct_0_16211_x1303_x831956043}[没有关联任何命令行。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[\<Ctrl+U\>]{lang="EN-US"}]{#struct_0_16211_x1303_590739902}[没有关联任何命令行。]{style="font-family:
宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16211_x1303_135998590}

[[系统视图]{style="font-family:宋体"}]{#struct_0_16211_x1303_x1668115179}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x143960805}

[[network-admin]{lang="EN-US"}]{#struct_0_16211_x1303_x1801449037}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16211_x1303_1982197835}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16211_x1303_649123107}

[**[ctrl_g]{lang="EN-US"}**]{#struct_0_16211_x1303_1077069390}[：表示为快捷键]{style="font-family:宋体"}[\<Ctrl+G\>]{lang="EN-US"}[指定一条命令。]{style="font-family:宋体"}

[**[ctrl_l]{lang="EN-US"}**]{#struct_0_16211_x1303_x25224309}[：表示为快捷键]{style="font-family:宋体"}[\<Ctrl+L\>]{lang="EN-US"}[指定一条命令。]{style="font-family:宋体"}

[**[ctrl_o]{lang="EN-US"}**]{#struct_0_16211_x1303_710382605}[：表示为快捷键]{style="font-family:宋体"}[\<Ctrl+O\>]{lang="EN-US"}[指定一条命令。]{style="font-family:宋体"}

[**[ctrl_t]{lang="EN-US"}**]{#struct_0_16211_x1303_1460532389}[：表示为快捷键]{style="font-family:宋体"}[\<Ctrl+T\>]{lang="EN-US"}[指定一条命令。]{style="font-family:宋体"}

[**[ctrl_u]{lang="EN-US"}**]{#struct_0_16211_x1303_x1668115180}[：表示为快捷键]{style="font-family:宋体"}[\<Ctrl+U\>]{lang="EN-US"}[指定一条命令。]{style="font-family:宋体"}

[*[command]{lang="EN-US"}*]{#struct_0_16211_x1303_x1354666354}[：快捷键关联的命令行。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x552384482}

[[通过快捷键用户可以简便、快捷的操作设备，使用]{style="font-family:宋体"}**[display hotkey]{lang="EN-US"}**]{#struct_0_16211_x1303_1147346899}[命令可以查看设备支持的所有快捷键及其含义。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x1699641264}

[[\# ]{lang="EN-US"}]{#struct_0_16211_x1303_x1921967976}[指定命令]{style="font-family:宋体"}**[display tcp status]{lang="EN-US"}**[的快捷键为]{style="font-family:宋体"}[\<Ctrl+T\>]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16211_x1303_208362884}

[\[Sysname\] hotkey ctrl_t display tcp status]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16211_x1303_1167509087}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display hotkey]{lang="EN-US"}**]{#struct_0_16211_x1303_x1936973068}
:::

::: {#-1159706084 .myid}
[]{#_Toc404782170}[]{#struct_0_16211_x1303_x1668115181}[]{#_Toc291753306}

**CLI \-- CLI命令 \-- quit**

------------------------------------------------------------------------

[**[quit]{lang="EN-US"}**]{#struct_0_16211_x1303_211417587}[命令用来使用户从当前视图退回到上一层视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x857975283}

[**[quit]{lang="EN-US"}**]{#struct_0_16211_x1303_1130212335}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x915603824}

[[任意视图]{style="font-family:宋体"}]{#struct_0_16211_x1303_1237939468}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x1214757837}

[[network-admin]{lang="EN-US"}]{#struct_0_16211_x1303_x70105211}

[[network-operator]{lang="EN-US"}]{#struct_0_16211_x1303_x1668115182}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16211_x1303_x191866940}

[[mdc-operator]{lang="EN-US"}]{#struct_0_16211_x1303_1177423835}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16211_x1303_1256499487}

[[如果当前是用户视图，执行]{style="font-family:宋体"}**[quit]{lang="EN-US"}**]{#struct_0_16211_x1303_x772647726}[后，会断开当前连接，退出系统。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x2046080571}

[[\# ]{lang="EN-US"}]{#struct_0_16211_x1303_616786453}[从接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[视图退回到系统视图，再退回到用户视图。]{style="font-family:宋体"}

[[\[Sysname-GigabitEthernet1/0/1\] quit]{lang="EN-US"}]{#struct_0_16211_x1303_x800060994}

[\[Sysname\] quit]{lang="EN-US"}

[\<Sysname\>]{lang="EN-US"}
:::

::: {#2044914397 .myid}
[]{#_Toc404782171}[]{#struct_0_16211_x1303_x1594271198}[]{#_Toc389227713}[]{#_Toc389226359}

**CLI \-- CLI命令 \-- repeat**

------------------------------------------------------------------------

[**[repeat]{lang="EN-US"}**]{#struct_0_16211_x1303_1683183700}[命令用来重复执行当前视图下的历史记录命令。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x1593812446}

[**[repeat ]{lang="EN-US"}**[\[ *number* \] \[ **count** *times* \] \[ **delay** *seconds* \]]{lang="EN-US"}]{#struct_0_16211_x1303_x749166940}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16211_x1303_415323428}

[[任意视图]{style="font-family:宋体"}]{#struct_0_16211_x1303_x1673052708}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x1941463275}

[[network-admin]{lang="EN-US"}]{#struct_0_16211_x1303_2035607790}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16211_x1303_1007397636}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x527859231}

[*[number]{lang="EN-US"}*]{#struct_0_16211_x1303_x1325655215}[：表示重复执行历史命令的条数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[count ]{lang="EN-US"}***[times]{lang="EN-US"}*]{#struct_0_16211_x1303_x1525083539}[：表示重复执行历史命令的次数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。如不指定该参数，则历史命令一直重复执行，直到执行用户线视图下设置的终止当前运行任务的快捷键才能停止执行该命令，默认的终止快捷键为]{style="font-family:宋体"}[\<Ctrl+C\>]{lang="EN-US"}[。关于终止当前执行任务的快捷键的设置，请参见"基础配置"中的"登录设备"。]{style="font-family:宋体"}

[**[delay ]{lang="EN-US"}***[seconds]{lang="EN-US"}*]{#struct_0_16211_x1303_27187179}[：表示重复执行历史命令的时间间隔，取值范围为]{style="font-family:
宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x254973533}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_16211_x1303_1622666964}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重复执行历史命令时，系统将按照历史命令的下发顺序执行。例如，用户在某视图下依次执行命令]{style="font-family:宋体"}]{#struct_0_16211_x1303_x1658079638}[a]{lang="EN-US"}[、]{style="font-family:宋体"}[b]{lang="EN-US"}[和]{style="font-family:宋体"}[c]{lang="EN-US"}[后，再执行]{style="font-family:
宋体"}**[repeat]{lang="EN-US"}**[ 3]{lang="EN-US"}[命令，则系统将按照]{style="font-family:宋体"}[a]{lang="EN-US"}[、]{style="font-family:宋体"}[b]{lang="EN-US"}[和]{style="font-family:
宋体"}[c]{lang="EN-US"}[的顺序重复执行一次。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果用户重复执行的历史命令中存在交互式命令，需要用户手动处理此交互式命令，直到交互式命令执行结束，历史命令才会继续被重复执行。]{style="font-family:宋体"}]{#struct_0_16211_x1303_1881750279}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x236762973}

[[\# ]{lang="EN-US"}]{#struct_0_16211_x1303_x1190605845}[重复执行最近]{style="font-family:宋体"}[2]{lang="EN-US"}[条历史命令]{style="font-family:宋体"}**[display cpu]{lang="EN-US"}**[和]{style="font-family:宋体"}**[display clock]{lang="EN-US"}**[，重复执行]{style="font-family:宋体"}[3]{lang="EN-US"}[次，时间间隔]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> repeat 2 count 3 delay 10]{lang="EN-US"}]{#struct_0_16211_x1303_x1593943518}

[\<Sysname\> display cpu]{lang="EN-US"}

[Unit CPU usage:]{lang="EN-US"}

[      33% in last 5 seconds]{lang="EN-US"}

[      32% in last 1 minute]{lang="EN-US"}

[      33% in last 5 minutes]{lang="EN-US"}

[                                                                                ]{lang="EN-US"}

[\<Sysname\> display clock]{lang="EN-US"}

[12:20:08 UTC Thu 06/19/2014]{lang="EN-US"}

[\<Sysname\> display cpu]{lang="EN-US"}

[Unit CPU usage:]{lang="EN-US"}

[      33% in last 5 seconds]{lang="EN-US"}

[      32% in last 1 minute]{lang="EN-US"}

[      33% in last 5 minutes]{lang="EN-US"}

[                                                                                ]{lang="EN-US"}

[\<Sysname\> display clock]{lang="EN-US"}

[12:20:18 UTC Thu 06/19/2014]{lang="EN-US"}

[\<Sysname\> display cpu]{lang="EN-US"}

[Unit CPU usage:]{lang="EN-US"}

[      33% in last 5 seconds]{lang="EN-US"}

[      32% in last 1 minute]{lang="EN-US"}

[      33% in last 5 minutes]{lang="EN-US"}

[                                                                                ]{lang="EN-US"}

[\<Sysname\> display clock ]{lang="EN-US"}

[12:20:28 UTC Thu 06/19/2014 ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x1885517526}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display history-command]{lang="EN-US"}**]{#struct_0_16211_x1303_x1596018782}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[history-command max-size]{lang="EN-US"}**]{#struct_0_16211_x1303_433376472}
:::

::: {#-1160069800 .myid}
[]{#_Toc404782172}[]{#struct_0_16211_x1303_748154997}[]{#_Toc291753307}[]{#_Toc137951601}[]{#_Toc89225284}[]{#_Toc396481066}[]{#_Toc396481067}[]{#_Toc389753020}[]{#_Toc298254747}[]{#_Toc298254749}[]{#_Toc298254751}

**CLI \-- CLI命令 \-- return**

------------------------------------------------------------------------

[**[return]{lang="EN-US"}**]{#struct_0_16211_x1303_x1668115183}[命令用来从当前视图（非用户视图）直接退回到用户视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16211_x1303_1374217001}

[**[return]{lang="EN-US"}**]{#struct_0_16211_x1303_847674448}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x769777423}

[[除用户视图外的任意视图]{style="font-family:宋体"}]{#struct_0_16211_x1303_1295471009}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16211_x1303_1753867150}

[[network-admin]{lang="EN-US"}]{#struct_0_16211_x1303_622392272}

[[network-operator]{lang="EN-US"}]{#struct_0_16211_x1303_x711065546}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16211_x1303_1673211781}

[[mdc-operator]{lang="EN-US"}]{#struct_0_16211_x1303_x1668115184}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16211_x1303_614702114}

[[用户也可以使用组合键]{style="font-family:宋体"}[\<Ctrl+Z\>]{lang="EN-US"}]{#struct_0_16211_x1303_658873064}[从当前视图（非用户视图）直接退回到用户视图，效果等同于执行]{style="font-family:宋体"}**[return]{lang="EN-US"}**[命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16211_x1303_1766938849}

[[\# ]{lang="EN-US"}]{#struct_0_16211_x1303_1172090320}[从接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[视图退回到用户视图。]{style="font-family:宋体"}

[[\[Sysname-GigabitEthernet1/0/1\] return]{lang="EN-US"}]{#struct_0_16211_x1303_x1628097271}

[\<Sysname\>]{lang="EN-US"}
:::

::: {#1769150750 .myid}
[]{#_Toc137951602}[]{#_Toc89225285}[]{#_Toc404782173}[]{#struct_0_16211_x1303_91434681}[]{#_Toc291753308}[]{#_Toc168299375}

**CLI \-- CLI命令 \-- screen-length disable**

------------------------------------------------------------------------

[**[screen-length disable]{lang="EN-US"}**]{#struct_0_16211_x1303_1845287381}[命令用来禁用当前用户的分屏显示功能。]{style="font-family:宋体"}

[**[undo screen-length disable]{lang="EN-US"}**]{#struct_0_16211_x1303_x1668115185}[命令用来启用当前用户的分屏显示功能。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x2114181241}

[**[screen-length disable]{lang="EN-US"}**]{#struct_0_16211_x1303_1601264547}

[**[undo screen-length disable]{lang="EN-US"}**]{#struct_0_16211_x1303_x954337637}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x518471186}

[[用户登录后将遵循用户线下的]{style="font-family:宋体"}**[screen-length]{lang="EN-US"}**]{#struct_0_16211_x1303_1281187337}[设置。]{style="font-family:宋体"}**[screen-length]{lang="EN-US"}**[设置的缺省情况为：允许分屏显示，下一屏显示]{style="font-family:宋体"}[24]{lang="EN-US"}[行数据。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16211_x1303_273470755}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16211_x1303_x417748306}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x295602280}

[[network-admin]{lang="EN-US"}]{#struct_0_16211_x1303_x585876167}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16211_x1303_x1668115186}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16211_x1303_1777501528}

[[禁止分屏显示时，会一次显示所有信息，如果信息较多，则会连续刷屏，不方便立即查看。]{style="font-family:宋体"}]{#struct_0_16211_x1303_x675823670}

[[需要注意的是，该配置只对当前用户本次登录有效，用户重新登录后将恢复到缺省情况。]{style="font-family:宋体"}]{#struct_0_16211_x1303_388134812}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16211_x1303_587844021}

[[\# ]{lang="EN-US"}]{#struct_0_16211_x1303_1420567686}[禁用当前用户的分屏显示功能。]{style="font-family:宋体"}

[[\<Sysname\> screen-length disable]{lang="EN-US"}]{#struct_0_16211_x1303_x689455446}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16211_x1303_x527397900}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[screen-length]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_16211_x1303_999525499}[（基础配置命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[登录设备）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#1057508062 .myid}
[]{#_Toc404782174}[]{#struct_0_16211_x1303_x1668115187}[]{#_Toc291753312}[]{#_Toc326154684}[]{#_Toc326226362}[]{#_Toc326154685}[]{#_Toc326226363}[]{#_Toc326154686}[]{#_Toc326226364}[]{#_Toc326154687}[]{#_Toc326226365}[]{#_Toc326154688}[]{#_Toc326226366}[]{#_Toc326154689}[]{#_Toc326226367}[]{#_Toc326154690}[]{#_Toc326226368}[]{#_Toc326154691}[]{#_Toc326226369}[]{#_Toc326154692}[]{#_Toc326226370}[]{#_Toc326154693}[]{#_Toc326226371}[]{#_Toc326154694}[]{#_Toc326226372}[]{#_Toc326154695}[]{#_Toc326226373}[]{#_Toc326154696}[]{#_Toc326226374}[]{#_Toc326154697}[]{#_Toc326226375}[]{#_Toc326154698}[]{#_Toc326226376}[]{#_Toc326154699}[]{#_Toc326226377}[]{#_Toc326154700}[]{#_Toc326226378}[]{#_Toc326154701}[]{#_Toc326226379}[]{#_Toc326154702}[]{#_Toc326226380}[]{#_Toc326154703}[]{#_Toc326226381}[]{#_Toc326154704}[]{#_Toc326226382}[]{#_Toc326154705}[]{#_Toc326226383}[]{#_Toc326154706}[]{#_Toc326226384}[]{#_Toc326154707}[]{#_Toc326226385}[]{#_Toc326154708}[]{#_Toc326226386}[]{#_Toc326154709}[]{#_Toc326226387}[]{#_Toc326154710}[]{#_Toc326226388}[]{#_Toc326154711}[]{#_Toc326226389}[]{#_Toc326154712}[]{#_Toc326226390}[]{#_Toc326154713}[]{#_Toc326226391}[]{#_Toc326154714}[]{#_Toc326226392}[]{#_Toc326154715}[]{#_Toc326226393}[]{#_Toc326154716}[]{#_Toc326226394}[]{#_Toc326154717}[]{#_Toc326226395}[]{#_Toc326154718}[]{#_Toc326226396}[]{#_Toc326154719}[]{#_Toc326226397}[]{#_Toc326154720}[]{#_Toc326226398}[]{#_Toc326154721}[]{#_Toc326226399}[]{#_Toc326154722}[]{#_Toc326226400}[]{#_Toc326154723}[]{#_Toc326226401}[]{#_Toc326154724}[]{#_Toc326226402}[]{#_Toc326154725}[]{#_Toc326226403}[]{#_Toc326154726}[]{#_Toc326226404}[]{#_Toc326154727}[]{#_Toc326226405}[]{#_Toc326154728}[]{#_Toc326226406}[]{#_Toc326154729}[]{#_Toc326226407}[]{#_Toc326154730}[]{#_Toc326226408}[]{#_Toc326154731}[]{#_Toc326226409}[]{#_Toc326154732}[]{#_Toc326226410}[]{#_Toc326154733}[]{#_Toc326226411}[]{#_Toc326154734}[]{#_Toc326226412}[]{#_Toc326154735}[]{#_Toc326226413}[]{#_Toc326154736}[]{#_Toc326226414}[]{#_Toc326154737}[]{#_Toc326226415}[]{#_Toc326154738}[]{#_Toc326226416}[]{#_Toc326154739}[]{#_Toc326226417}[]{#_Toc326154740}[]{#_Toc326226418}[]{#_Toc326154741}[]{#_Toc326226419}[]{#_Toc326154742}[]{#_Toc326226420}[]{#_Toc326154743}[]{#_Toc326226421}[]{#_Toc326154744}[]{#_Toc326226422}[]{#_Toc326154745}[]{#_Toc326226423}[]{#_Toc326154746}[]{#_Toc326226424}[]{#_Toc326154747}[]{#_Toc326226425}[]{#_Toc326154748}[]{#_Toc326226426}[]{#_Toc326154749}[]{#_Toc326226427}[]{#_Toc326154750}[]{#_Toc326226428}[]{#_Toc326154751}[]{#_Toc326226429}[]{#_Toc326154752}[]{#_Toc326226430}[]{#_Toc326154753}[]{#_Toc326226431}[]{#_Toc326154754}[]{#_Toc326226432}[]{#_Toc326154755}[]{#_Toc326226433}[]{#_Toc326154756}[]{#_Toc326226434}[]{#_Toc326154757}[]{#_Toc326226435}[]{#_Toc326154758}[]{#_Toc326226436}[]{#_Toc326154759}[]{#_Toc326226437}[]{#_Toc326154760}[]{#_Toc326226438}[]{#_Toc326154761}[]{#_Toc326226439}[]{#_Toc326154762}[]{#_Toc326226440}[]{#_Toc326154763}[]{#_Toc326226441}

**CLI \-- CLI命令 \-- system-view**

------------------------------------------------------------------------

[**[system-view]{lang="EN-US"}**]{#struct_0_16211_x1303_x951381827}[命令用来从用户视图进入系统视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16211_x1303_1317764495}

[**[system-view]{lang="EN-US"}**]{#struct_0_16211_x1303_x736045271}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16211_x1303_255761062}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16211_x1303_133634259}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16211_x1303_903675501}

[[network-admin]{lang="EN-US"}]{#struct_0_16211_x1303_510389180}

[[network-operator]{lang="EN-US"}]{#struct_0_16211_x1303_1473480217}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16211_x1303_x1668115188}

[[mdc-operator]{lang="EN-US"}]{#struct_0_16211_x1303_x1710896714}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16211_x1303_23626690}

[[\# ]{lang="EN-US"}]{#struct_0_16211_x1303_834999155}[从用户视图进入系统视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16211_x1303_325767972}

[System View: return to User View with Ctrl+Z.]{lang="EN-US"}

[\[Sysname\]]{lang="EN-US"}
:::
