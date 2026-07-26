::: {#-1461383778 .myid}
[]{#_Toc404782242}[]{#struct_0_x1979_37509_x100625136}[]{#_Toc285213496}

**RBAC \-- RBAC配置命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_x1979_37509_x1947846488}[命令用来配置用户角色描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_x1979_37509_940529497}[用来删除用户角色的描述信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1072032735}

[**[description ]{lang="EN-US"}***[text]{lang="EN-US"}*]{#struct_0_x1979_37509_1394993731}

[**[undo description]{lang="EN-US"}**]{#struct_0_x1979_37509_x1991509580}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1979_37509_517809488}

[[未定义用户角色描述信息。]{style="font-family:宋体"}]{#struct_0_x1979_37509_640546423}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1097213872}

[[用户角色视图]{style="font-family:宋体"}]{#struct_0_x1979_37509_139977795}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x100625137}

[[network-admin]{lang="EN-US"}]{#struct_0_x1979_37509_x1947780952}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1979_37509_x1481048844}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1369126628}

[*[text]{lang="EN-US"}*]{#struct_0_x1979_37509_994481660}[：用户角色描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1979_37509_901031620}

[[描述信息用来方便管理员对用户角色进行管理。]{style="font-family:宋体"}]{#struct_0_x1979_37509_1538002054}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1750073771}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_x136022298}[为用户角色]{style="font-family:宋体"}[role1]{lang="EN-US"}[配置描述信息为"]{style="font-family:宋体"}[labVIP]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1979_37509_x100625138}

[\[Sysname\] role name role1]{lang="EN-US"}

[\[Sysname-role-role1\] description labVIP]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1948239704}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[**[display role]{lang="EN-US"}**]{.ItemStepChar}]{#struct_0_x1979_37509_x595740142}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[role]{lang="EN-US"}**]{#struct_0_x1979_37509_1806902859}
:::

::: {#654469937 .myid}
[]{#_Toc404782243}[]{#struct_0_x1979_37509_x1938343534}[]{#_Toc285213497}

**RBAC \-- RBAC配置命令 \-- display role**

------------------------------------------------------------------------

[**[display role]{lang="EN-US"}**]{#struct_0_x1979_37509_x845445811}[命令用来显示用户角色信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x427773060}

[**[display role ]{lang="EN-US"}**[\[ **name** *role-name* \]]{lang="EN-US"}]{#struct_0_x1979_37509_73097034}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x100625139}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1979_37509_x1948174168}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1030331716}

[[network-admin]{lang="EN-US"}]{#struct_0_x1979_37509_1928254267}

[[netword-operator]{lang="EN-US"}]{#struct_0_x1979_37509_x1853333064}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1979_37509_438603854}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1979_37509_902086035}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1979_37509_1112429171}

[**[name]{lang="EN-US"}***[ role-name]{lang="EN-US"}*]{#struct_0_x1979_37509_x100625140}[：用户角色名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1947715409}

[[如果不指定用户角色名称，则表示显示所有用户角色的信息，包括系统缺省存在的用户角色的信息。]{style="font-family:宋体"}]{#struct_0_x1979_37509_679468487}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x274264982}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_x860171199}[显示用户角色]{style="font-family:宋体"}[123]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[\<Sysname\> display role name 123]{lang="EN-US"}]{#struct_0_x1979_37509_x2056940267}

[Role: 123]{lang="EN-US"}

[  Description: new role]{lang="EN-US"}

[  VLAN policy: deny]{lang="EN-US"}

[  Permitted VLANs: 1 to 5, 7 to 8]{lang="EN-US"}

[  Interface policy: deny]{lang="EN-US"}

[  Permitted interfaces: GigabitEthernet1/0/1 to GigabitEthernet1/0/2, Vlan-interface1 to Vlan-interface20]{lang="EN-US"}

[  VPN instance policy: deny]{lang="EN-US"}

[  Permitted VPN instances: vpn, vpn1, vpn2]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  Rule    Perm   Type  Scope         Entity]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  1       permit RWX   feature-group abc]{lang="EN-US"}

[  2       deny   -W-   feature       ldap]{lang="EN-US"}

[  3       permit       command       system ; radius sc \*]{lang="EN-US"}

[  4       permit R\--   xml-element   -]{lang="EN-US"}

[  5       permit RW-   oid           1.2.1]{lang="EN-US"}

[  R:Read W:Write X:Execute]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_2023854379}[显示所有用户角色的信息。]{style="font-family:宋体"}

[[\<Sysname\> display role]{lang="EN-US"}]{#struct_0_x1979_37509_x2056940274}

[Role: network-admin]{lang="EN-US"}

[  Description: Predefined network admin role has access to all commands on the device]{lang="EN-US"}

[  VLAN policy: permit (default)]{lang="EN-US"}

[  Interface policy: permit (default)]{lang="EN-US"}

[  VPN instance policy: permit (default)]{lang="EN-US"}

[  Security zone policy: permit (default)]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  Rule    Perm   Type  Scope         Entity]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  sys-1   permit       command       \*]{lang="EN-US"}

[  sys-2   permit RWX   web-menu      -]{lang="EN-US"}

[  sys-3   permit RWX   xml-element   -]{lang="EN-US"}

[  sys-4   deny         command       display security-logfile summary]{lang="EN-US"}

[  sys-5   deny         command       system-view ; info-center securi]{lang="EN-US"}

[                                     ty-logfile directory \*]{lang="EN-US"}

[  sys-6   deny         command       security-logfile save]{lang="EN-US"}

[  sys-7   permit RW-   oid           1]{lang="EN-US"}

[  R:Read W:Write X:Execute]{lang="EN-US"}

[ ]{lang="EN-US"}

[Role: network-operator]{lang="EN-US"}

[  Description: Predefined network operator role has access to all read commands on the device]{lang="EN-US"}

[  VLAN policy: permit (default)]{lang="EN-US"}

[  Interface policy: permit (default)]{lang="EN-US"}

[  VPN instance policy: permit (default)]{lang="EN-US"}

[  Security zone policy: permit (default)]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  Rule    Perm   Type  Scope         Entity]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  sys-1   permit       command       display \*]{lang="EN-US"}

[  sys-2   permit       command       xml]{lang="EN-US"}

[  sys-3   deny         command       display history-command all]{lang="EN-US"}

[  sys-4   deny         command       display exception \*]{lang="EN-US"}

[  sys-5   deny         command       display cpu-usage configuration]{lang="EN-US"}

[                                     \*]{lang="EN-US"}

[  sys-6   deny         command       display kernel exception \*]{lang="EN-US"}

[  sys-7   deny         command       display kernel deadloop \*]{lang="EN-US"}

[  sys-8   deny         command       display kernel starvation \*]{lang="EN-US"}

[  sys-9   deny         command       display kernel reboot \*]{lang="EN-US"}

[  sys-10  deny         command       display memory trace \*]{lang="EN-US"}

[  sys-11  deny         command       display kernel memory \*]{lang="EN-US"}

[  sys-12  permit       command       system-view ; local-user \*]{lang="EN-US"}

[  sys-13  permit       command       system-view ; switchto mdc \*]{lang="EN-US"}

[  sys-14  permit R\--   web-menu      -]{lang="EN-US"}

[  sys-15  permit R\--   xml-element   -]{lang="EN-US"}

[  sys-16  deny         command       display security-logfile summary]{lang="EN-US"}

[  sys-17  deny         command       system-view ; info-center securi]{lang="EN-US"}

[                                     ty-logfile directory \*]{lang="EN-US"}

[  sys-18  deny         command       security-logfile save]{lang="EN-US"}

[  sys-19  permit R\--   oid           1]{lang="EN-US"}

[  R:Read W:Write X:Execute]{lang="EN-US"}

[ ]{lang="EN-US"}

[Role: mdc-admin]{lang="EN-US"}

[  Description: Predefined MDC admin role has access to all commands within an MDC instance]{lang="EN-US"}

[  VLAN policy: permit (default)]{lang="EN-US"}

[  Interface policy: permit (default)]{lang="EN-US"}

[  VPN instance policy: permit (default)]{lang="EN-US"}

[  Security zone policy: permit (default)]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  Rule    Perm   Type  Scope         Entity]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  sys-1   permit       command       \*]{lang="EN-US"}

[  sys-2   permit RWX   web-menu      -]{lang="EN-US"}

[  sys-3   permit RWX   xml-element   -]{lang="EN-US"}

[  sys-4   deny   RWX   feature       mdc]{lang="EN-US"}

[  sys-5   permit       command       display mdc \*]{lang="EN-US"}

[  sys-6   permit       command       switchback]{lang="EN-US"}

[  sys-7   deny         command       display security-logfile summary]{lang="EN-US"}

[  sys-8   deny         command       system-view ; info-center securi]{lang="EN-US"}

[                                     ty-logfile directory \*]{lang="EN-US"}

[  sys-9   deny         command       security-logfile save]{lang="EN-US"}

[  sys-10  permit RW-   oid           1]{lang="EN-US"}

[ ]{lang="EN-US"}

[  R:Read W:Write X:Execute]{lang="EN-US"}

[ ]{lang="EN-US"}

[Role: mdc-operator]{lang="EN-US"}

[  Description: Predefined MDC operator role has access to all read commands within an MDC instance]{lang="EN-US"}

[  VLAN policy: permit (default)]{lang="EN-US"}

[  Interface policy: permit (default)]{lang="EN-US"}

[  VPN instance policy: permit (default)]{lang="EN-US"}

[  Security zone policy: permit (default)]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  Rule    Perm   Type  Scope         Entity]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  sys-1   permit       command       display \*]{lang="EN-US"}

[  sys-2   permit       command       xml]{lang="EN-US"}

[  sys-3   deny         command       display history-command all]{lang="EN-US"}

[  sys-4   deny         command       display exception \*]{lang="EN-US"}

[  sys-5   deny         command       display cpu-usage configuration]{lang="EN-US"}

[                                     ]{lang="EN-US"}

[  sys-6   deny         command       display kernel exception \*]{lang="EN-US"}

[  sys-7   deny         command       display kernel deadloop \*]{lang="EN-US"}

[  sys-8   deny         command       display kernel starvation \*]{lang="EN-US"}

[  sys-9   deny         command       display kernel reboot \*]{lang="EN-US"}

[  sys-10  deny         command       display memory trace \*]{lang="EN-US"}

[  sys-11  deny         command       display kernel memory \*]{lang="EN-US"}

[  sys-12  permit       command       system-view ; local-user \*]{lang="EN-US"}

[  sys-13  permit       command       switchback]{lang="EN-US"}

[  sys-14  permit R\--   web-menu      -]{lang="EN-US"}

[  sys-15  permit R\--   xml-element   -]{lang="EN-US"}

[  sys-16  deny         command       display security-logfile summary]{lang="EN-US"}

[  sys-17  deny         command       system-view ; info-center securi]{lang="EN-US"}

[                                     ty-logfile directory \*]{lang="EN-US"}

[  sys-18  deny         command       security-logfile save]{lang="EN-US"}

[  sys-19  permit R\--   oid           1]{lang="EN-US"}

[  R:Read W:Write X:Execute]{lang="EN-US"}

[ ]{lang="EN-US"}

[Role: context-admin]{lang="EN-US"}

[  Description: Predefined Context admin role has access to all commands within a Context]{lang="EN-US"}

[  VLAN policy: permit (default)]{lang="EN-US"}

[  Interface policy: permit (default)]{lang="EN-US"}

[  VPN instance policy: permit (default)]{lang="EN-US"}

[  Security zone policy: permit (default)]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  Rule    Perm   Type  Scope         Entity]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  sys-1   permit       command       \*]{lang="EN-US"}

[  sys-2   permit RWX   web-menu      -]{lang="EN-US"}

[  sys-3   permit RWX   xml-element   -]{lang="EN-US"}

[  sys-4   deny   RWX   feature       context]{lang="EN-US"}

[  sys-5   permit R\--   command       display context \*]{lang="EN-US"}

[  sys-5   deny         command       display security-logfile summary]{lang="EN-US"}

[  sys-6   deny         command       system-view ; info-center securi]{lang="EN-US"}

[                                     ty-logfile directory \*]{lang="EN-US"}

[  sys-7   deny         command       security-logfile save]{lang="EN-US"}

[  sys-8   permit RW-   oid           1]{lang="EN-US"}

[ ]{lang="EN-US"}

[  R:Read W:Write X:Execute]{lang="EN-US"}

[ ]{lang="EN-US"}

[Role: context-operator]{lang="EN-US"}

[  Description: Predefined Context operator role has access to all read commands within a Context]{lang="EN-US"}

[  VLAN policy: permit (default)]{lang="EN-US"}

[  Interface policy: permit (default)]{lang="EN-US"}

[  VPN instance policy: permit (default)]{lang="EN-US"}

[  Security zone policy: permit (default)]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  Rule    Perm   Type  Scope         Entity]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  sys-1   permit       command       display \*]{lang="EN-US"}

[  sys-2   permit       command       xml]{lang="EN-US"}

[  sys-3   deny         command       display history-command all]{lang="EN-US"}

[  sys-4   permit       command       system-view ; local-user \*]{lang="EN-US"}

[  sys-5   permit R\--   web-menu      -]{lang="EN-US"}

[  sys-6   permit R\--   xml-element   -]{lang="EN-US"}

[  sys-7   deny         command       display security-logfile summary]{lang="EN-US"}

[  sys-8   deny         command       system-view ; info-center securi]{lang="EN-US"}

[                                     ty-logfile directory \*]{lang="EN-US"}

[  sys-9   deny         command       security-logfile save]{lang="EN-US"}

[  sys-10  permit R\--   oid           1]{lang="EN-US"}

[  R:Read W:Write X:Execute]{lang="EN-US"}

[ ]{lang="EN-US"}

[Role: level-0]{lang="EN-US"}

[  Description: Predefined level-0 role]{lang="EN-US"}

[  VLAN policy: permit (default)]{lang="EN-US"}

[  Interface policy: permit (default)]{lang="EN-US"}

[  VPN instance policy: permit (default)]{lang="EN-US"}

[  Security zone policy: permit (default)]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  Rule    Perm   Type  Scope         Entity]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  sys-1   permit       command       tracert \*]{lang="EN-US"}

[  sys-2   permit       command       telnet \*]{lang="EN-US"}

[  sys-3   permit       command       ping \*]{lang="EN-US"}

[  sys-4   permit       command       ssh2 \*]{lang="EN-US"}

[  sys-5   permit       command       super \*]{lang="EN-US"}

[  R:Read W:Write X:Execute]{lang="EN-US"}

[ ]{lang="EN-US"}

[Role: level-1]{lang="EN-US"}

[  Description: Predefined level-1 role]{lang="EN-US"}

[  VLAN policy: permit (default)]{lang="EN-US"}

[  Interface policy: permit (default)]{lang="EN-US"}

[  VPN instance policy: permit (default)]{lang="EN-US"}

[  Security zone policy: permit (default)]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  Rule    Perm   Type  Scope         Entity]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  sys-1   permit       command       tracert \*]{lang="EN-US"}

[  sys-2   permit       command       telnet \*]{lang="EN-US"}

[  sys-3   permit       command       ping \*]{lang="EN-US"}

[  sys-4   permit       command       ssh2 \*]{lang="EN-US"}

[  sys-5   permit       command       display \*]{lang="EN-US"}

[  sys-6   permit       command       super \*]{lang="EN-US"}

[  sys-7   deny         command       display history-command all]{lang="EN-US"}

[  R:Read W:Write X:Execute]{lang="EN-US"}

[ ]{lang="EN-US"}

[Role: level-2]{lang="EN-US"}

[  Description: Predefined level-2 role]{lang="EN-US"}

[  VLAN policy: permit (default)]{lang="EN-US"}

[  Interface policy: permit (default)]{lang="EN-US"}

[  VPN instance policy: permit (default)]{lang="EN-US"}

[  Security zone policy: permit (default)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Role: level-3]{lang="EN-US"}

[  Description: Predefined level-3 role]{lang="EN-US"}

[  VLAN policy: permit (default)]{lang="EN-US"}

[  Interface policy: permit (default)]{lang="EN-US"}

[  VPN instance policy: permit (default)]{lang="EN-US"}

[  Security zone policy: permit (default)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Role: level-4]{lang="EN-US"}

[  Description: Predefined level-4 role]{lang="EN-US"}

[  VLAN policy: permit (default)]{lang="EN-US"}

[  Interface policy: permit (default)]{lang="EN-US"}

[  VPN instance policy: permit (default)]{lang="EN-US"}

[  Security zone policy: permit (default)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Role: level-5]{lang="EN-US"}

[  Description: Predefined level-5 role]{lang="EN-US"}

[  VLAN policy: permit (default)]{lang="EN-US"}

[  Interface policy: permit (default)]{lang="EN-US"}

[  VPN instance policy: permit (default)]{lang="EN-US"}

[  Security zone policy: permit (default)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Role: level-6]{lang="EN-US"}

[  Description: Predefined level-6 role]{lang="EN-US"}

[  VLAN policy: permit (default)]{lang="EN-US"}

[  Interface policy: permit (default)]{lang="EN-US"}

[  VPN instance policy: permit (default)]{lang="EN-US"}

[  Security zone policy: permit (default)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Role: level-7]{lang="EN-US"}

[  Description: Predefined level-7 role]{lang="EN-US"}

[  VLAN policy: permit (default)]{lang="EN-US"}

[  Interface policy: permit (default)]{lang="EN-US"}

[  VPN instance policy: permit (default)]{lang="EN-US"}

[  Security zone policy: permit (default)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Role: level-8]{lang="EN-US"}

[  Description: Predefined level-8 role]{lang="EN-US"}

[  VLAN policy: permit (default)]{lang="EN-US"}

[  Interface policy: permit (default)]{lang="EN-US"}

[  VPN instance policy: permit (default)]{lang="EN-US"}

[  Security zone policy: permit (default)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Role: level-9]{lang="EN-US"}

[  Description: Predefined leve-9 role]{lang="EN-US"}

[  VLAN policy: permit (default)]{lang="EN-US"}

[  Interface policy: permit (default)]{lang="EN-US"}

[  VPN instance policy: permit (default)]{lang="EN-US"}

[  Security zone policy: permit (default)]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  Rule    Perm   Type  Scope         Entity]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  sys-1   permit RWX   feature       -]{lang="EN-US"}

[  sys-2   deny   RWX   feature       device]{lang="EN-US"}

[  sys-3   deny   RWX   feature       filesystem]{lang="EN-US"}

[  sys-4   permit       command       display \*]{lang="EN-US"}

[  sys-5   deny         command       display history-command all]{lang="EN-US"}

[  R:Read W:Write X:Execute]{lang="EN-US"}

[ ]{lang="EN-US"}

[Role: level-10]{lang="EN-US"}

[  Description: Predefined level-10 role]{lang="EN-US"}

[  VLAN policy: permit (default)]{lang="EN-US"}

[  Interface policy: permit (default)]{lang="EN-US"}

[  VPN instance policy: permit (default)]{lang="EN-US"}

[  Security zone policy: permit (default)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Role: level-11]{lang="EN-US"}

[  Description: Predefined level-11 role]{lang="EN-US"}

[  VLAN policy: permit (default)]{lang="EN-US"}

[  Interface policy: permit (default)]{lang="EN-US"}

[  VPN instance policy: permit (default)]{lang="EN-US"}

[  Security zone policy: permit (default)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Role: level-12]{lang="EN-US"}

[  Description: Predefined level-12 role]{lang="EN-US"}

[  VLAN policy: permit (default)]{lang="EN-US"}

[  Interface policy: permit (default)]{lang="EN-US"}

[  VPN instance policy: permit (default)]{lang="EN-US"}

[  Security zone policy: permit (default)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Role: level-13]{lang="EN-US"}

[  Description: Predefined level-13 role]{lang="EN-US"}

[  VLAN policy: permit (default)]{lang="EN-US"}

[  Interface policy: permit (default)]{lang="EN-US"}

[  VPN instance policy: permit (default)]{lang="EN-US"}

[  Security zone policy: permit (default)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Role: level-14]{lang="EN-US"}

[  Description: Predefined level-14 role]{lang="EN-US"}

[  VLAN policy: permit (default)]{lang="EN-US"}

[  Interface policy: permit (default)]{lang="EN-US"}

[  VPN instance policy: permit (default)]{lang="EN-US"}

[  Security zone policy: permit (default)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Role: level-15]{lang="EN-US"}

[  Description: Predefined level-15 role]{lang="EN-US"}

[  VLAN policy: permit (default)]{lang="EN-US"}

[  Interface policy: permit (default)]{lang="EN-US"}

[  VPN instance policy: permit (default)]{lang="EN-US"}

[  Security zone policy: permit (default)]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  Rule    Perm   Type  Scope         Entity]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  sys-1   permit       command       \*]{lang="EN-US"}

[  sys-2   permit RWX   web-menu      -]{lang="EN-US"}

[  sys-3   permit RWX   xml-element   -]{lang="EN-US"}

[  sys-4   deny         command       display security-logfile summary]{lang="EN-US"}

[  sys-5   deny         command       system-view ; info-center securi]{lang="EN-US"}

[                                     ty-logfile directory \*]{lang="EN-US"}

[  sys-6   deny         command       security-logfile save]{lang="EN-US"}

[  sys-7   permit RW-   oid           1]{lang="EN-US"}

[  R:Read W:Write X:Execute]{lang="EN-US"}

[ ]{lang="EN-US"}

[Role: 123]{lang="EN-US"}

[  Description: new role]{lang="EN-US"}

[  VLAN policy: deny]{lang="EN-US"}

[  Permitted VLANs: 1 to 5, 7 to 8]{lang="EN-US"}

[  Interface policy: deny]{lang="EN-US"}

[  Permitted interfaces: GigabitEthernet1/0/1 to GigabitEthernet1/0/2, Vlan-interface1 to Vlan-interface20]{lang="EN-US"}

[  VPN instance policy: deny]{lang="EN-US"}

[  Permitted VPN instances: vpn, vpn1, vpn2]{lang="EN-US"}

[  Security zone policy: permit (default)]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  Rule    Perm   Type  Scope         Entity]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  1       permit RWX   feature-group abc]{lang="EN-US"}

[  2       deny   -W-   feature       ldap]{lang="EN-US"}

[  3       permit       command       system ; radius sc \*]{lang="EN-US"}

[  4       permit R\--   xml-element   -]{lang="EN-US"}

[  5       permit RW-   oid           1.2.1]{lang="EN-US"}

[  R:Read W:Write X:Execute]{lang="EN-US"}

[ ]{lang="EN-US"}

[Role: security-audit]{lang="EN-US"}

[  Description: Predefined security audit role only has access to commands for th]{lang="EN-US"}

[e security log administrator]{lang="EN-US"}

[  VLAN policy: permit (default)]{lang="EN-US"}

[  Interface policy: permit (default)]{lang="EN-US"}

[  VPN instance policy: permit (default)]{lang="EN-US"}

[  Security zone policy: permit (default)]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  Rule    Perm   Type  Scope         Entity]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  sys-1   deny         command       \*]{lang="EN-US"}

[  sys-2   permit       command       display security-logfile summary]{lang="EN-US"}

[  sys-3   permit       command       system-view ; info-center securi]{lang="EN-US"}

[                                     ty-logfile directory \*]{lang="EN-US"}

[  sys-4   permit       command       security-logfile save]{lang="EN-US"}

[  sys-5   permit       command       cd \*]{lang="EN-US"}

[  sys-6   permit       command       copy \*]{lang="EN-US"}

[  sys-7   permit       command       delete \*]{lang="EN-US"}

[  sys-8   permit       command       dir \*]{lang="EN-US"}

[  sys-9   permit       command       mkdir \*]{lang="EN-US"}

[  sys-10  permit       command       more \*]{lang="EN-US"}

[  sys-11  permit       command       move \*]{lang="EN-US"}

[  sys-12  permit       command       rmdir \*]{lang="EN-US"}

[  sys-13  permit       command       pwd]{lang="EN-US"}

[  sys-14  permit       command       rename \*]{lang="EN-US"}

[  sys-15  permit       command       undelete \*]{lang="EN-US"}

[  sys-16  permit       command       ftp \*]{lang="EN-US"}

[  sys-17  permit       command       sftp \*]{lang="EN-US"}

[  sys-18  permit       command       virtual-ftp-append]{lang="EN-US"}

[  sys-19  permit       command       virtual-ftp-ascii]{lang="EN-US"}

[  sys-20  permit       command       virtual-ftp-binary]{lang="EN-US"}

[  sys-21  permit       command       virtual-ftp-bye]{lang="EN-US"}

[  sys-22  permit       command       virtual-ftp-cd]{lang="EN-US"}

[  sys-23  permit       command       virtual-ftp-cdup]{lang="EN-US"}

[  sys-24  permit       command       virtual-ftp-close]{lang="EN-US"}

[  sys-25  permit       command       virtual-ftp-delete]{lang="EN-US"}

[  sys-26  permit       command       virtual-ftp-debug]{lang="EN-US"}

[  sys-27  permit       command       virtual-ftp-dir]{lang="EN-US"}

[  sys-28  permit       command       virtual-ftp-disconnect]{lang="EN-US"}

[  sys-29  permit       command       virtual-ftp-get]{lang="EN-US"}

[  sys-30  permit       command       virtual-ftp-help]{lang="EN-US"}

[  sys-31  permit       command       virtual-ftp-lcd]{lang="EN-US"}

[  sys-32  permit       command       virtual-ftp-ls]{lang="EN-US"}

[  sys-33  permit       command       virtual-ftp-mkdir]{lang="EN-US"}

[  sys-34  permit       command       virtual-ftp-newer]{lang="EN-US"}

[  sys-35  permit       command       virtual-ftp-open]{lang="EN-US"}

[  sys-36  permit       command       virtual-ftp-passive]{lang="EN-US"}

[  sys-37  permit       command       virtual-ftp-put]{lang="EN-US"}

[  sys-38  permit       command       virtual-ftp-pwd]{lang="EN-US"}

[  sys-39  permit       command       virtual-ftp-quit]{lang="EN-US"}

[  sys-40  permit       command       virtual-ftp-reget]{lang="EN-US"}

[  sys-41  permit       command       virtual-ftp-rstatus]{lang="EN-US"}

[  sys-42  permit       command       virtual-ftp-rhelp]{lang="EN-US"}

[  sys-43  permit       command       virtual-ftp-rename]{lang="EN-US"}

[  sys-44  permit       command       virtual-ftp-reset]{lang="EN-US"}

[  sys-45  permit       command       virtual-ftp-restart]{lang="EN-US"}

[  sys-46  permit       command       virtual-ftp-rmdir]{lang="EN-US"}

[  sys-47  permit       command       virtual-ftp-status]{lang="EN-US"}

[  sys-48  permit       command       virtual-ftp-system]{lang="EN-US"}

[  sys-49  permit       command       virtual-ftp-user]{lang="EN-US"}

[  sys-50  permit       command       virtual-ftp-verbose]{lang="EN-US"}

[  sys-51  permit       command       virtual-ftp-remove]{lang="EN-US"}

[  sys-52  permit       command       virtual-ftp-exit]{lang="EN-US"}

[  R:Read W:Write X:Execute]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display role]{lang="EN-US"}]{#struct_0_x1979_37509_457835974}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_369669503}[[字段]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1072429459}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1979_37509_x2056940275}

[[Role]{lang="EN-US"}]{#struct_0_x1979_37509_x1108247967}

[[用户角色名称，其中系统预定义的用户角色名称分别为]{style="font-family:宋体"}[network-admin]{lang="EN-US"}]{#struct_0_x1979_37509_x594205322}[、]{style="font-family:宋体"}[network-operator]{lang="EN-US"}[、]{style="font-family:宋体"}[mdc-admin]{lang="EN-US"}[、]{style="font-family:宋体"}[mdc-operator]{lang="EN-US"}[、]{style="font-family:宋体"}[context-admin]{lang="EN-US"}[、]{style="font-family:宋体"}[context-operator]{lang="EN-US"}[、]{style="font-family:宋体"}[level-*n*]{lang="EN-US"}[（]{style="font-family:宋体"}*[n]{lang="EN-US"}*[为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[）、]{style="font-family:宋体"}[security-audit]{lang="EN-US"}

[[Description]{lang="EN-US"}]{#struct_0_x1979_37509_610960209}

[[用户角色描述信息]{style="font-family:宋体"}]{#struct_0_x1979_37509_264248322}

[[VLAN policy]{lang="EN-US"}]{#struct_0_x1979_37509_657441595}

[[配置的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1979_37509_x2056940276}[策略：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deny]{lang="EN-US"}]{#struct_0_x1979_37509_x704963440}[：表示除允许操作指定的]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[外，其它]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[均不能被用户操作]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[permit (default)]{lang="EN-US"}]{#struct_0_x1979_37509_1663597863}[：表示系统缺省允许用户操作任何]{lang="EN-US" style="font-family:
  宋体"}[VLAN ]{lang="EN-US"}

[[Permitted VLANs]{lang="EN-US"}]{#struct_0_x1979_37509_x393182365}

[[允许用户操作的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1979_37509_111230054}

[[Interface policy]{lang="EN-US"}]{#struct_0_x1979_37509_x1907620540}

[[配置的接口策略：]{style="font-family:宋体"}]{#struct_0_x1979_37509_281711893}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deny]{lang="EN-US"}]{#struct_0_x1979_37509_x1901421288}[：表示除允许操作指定的接口外，其它接口均不能被用户操作]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[permit (default)]{lang="EN-US"}]{#struct_0_x1979_37509_x2146078589}[：表示系统缺省允许用户操作任何接口]{lang="EN-US" style="font-family:
  宋体"}

[[Permitted interfaces]{lang="EN-US"}]{#struct_0_x1979_37509_1667368555}

[[允许用户操作的接口]{style="font-family:宋体"}]{#struct_0_x1979_37509_615296793}

[[VPN-instance policy]{lang="EN-US"}]{#struct_0_x1979_37509_281711892}

[[配置的]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x1979_37509_x1901421287}[策略：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deny]{lang="EN-US"}]{#struct_0_x1979_37509_x223764288}[：表示除允许操作指定的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例外，其它]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例均不能被用户操作]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[permit (default)]{lang="EN-US"}]{#struct_0_x1979_37509_1664495383}[：表示系统缺省允许用户操作任何]{lang="EN-US" style="font-family:
  宋体"}[VPN]{lang="EN-US"}[实例]{lang="EN-US" style="font-family:宋体"}

[[Permitted VPN instances]{lang="EN-US"}]{#struct_0_x1979_37509_1413454422}

[[允许用户操作的]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x1979_37509_281711891}[实例]{style="font-family:宋体"}

[[Security zone policy]{lang="EN-US"}]{#struct_0_x1979_37509_1817328033}

[[配置的安全域策略：]{style="font-family:宋体"}]{#struct_0_x1979_37509_1817262497}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deny]{lang="EN-US"}]{#struct_0_x1979_37509_902765608}[：表示除允许操作指定的安全域外，其它安全域均不能被用户操作]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[permit (default)]{lang="EN-US"}]{#struct_0_x1979_37509_1817459105}[：表示系统缺省允许用户操作任何]{lang="EN-US" style="font-family:
  宋体"}[安全域]{style="font-family:宋体"}

[[该显示信息的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_x1979_37509_1817393569}

[[Permitted security zones]{lang="EN-US"}]{#struct_0_x1979_37509_1817590177}

[[允许用户操作的安全域]{style="font-family:宋体"}]{#struct_0_x1979_37509_526255229}

[[该显示信息的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_x1979_37509_1817524641}

[[Rule]{lang="EN-US"}]{#struct_0_x1979_37509_x1901421286}

[[用户角色规则编号（系统预定义的权限规则通过]{style="font-family:宋体"}[sys-n]{lang="EN-US"}]{#struct_0_x1979_37509_1342319653}[标识）]{style="font-family:宋体"}

[[Perm]{lang="EN-US"}]{#struct_0_x1979_37509_1501388137}

[[对命令行的操作许可：]{style="font-family:宋体"}]{#struct_0_x1979_37509_281711890}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[permit]{lang="EN-US"}]{#struct_0_x1979_37509_x1901421285}[：允许操作]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deny]{lang="EN-US"}]{#struct_0_x1979_37509_x1386563702}[：禁止操作]{lang="EN-US" style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_x1979_37509_1508949243}

[[命令行类型：]{style="font-family:宋体"}]{#struct_0_x1979_37509_x1222886343}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[R]{lang="EN-US"}]{#struct_0_x1979_37509_281711889}[：读类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[W]{lang="EN-US"}]{#struct_0_x1979_37509_437230882}[：写类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[X]{lang="EN-US"}]{#struct_0_x1979_37509_x2061927669}[：执行类型]{lang="EN-US" style="font-family:宋体"}

[[Scope]{lang="EN-US"}]{#struct_0_x1979_37509_1271405602}

[[用户角色规则的类型：]{style="font-family:宋体"}]{#struct_0_x1979_37509_281711888}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[command]{lang="EN-US"}]{#struct_0_x1979_37509_437230883}[：基于命令行的规则]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[feature]{lang="EN-US"}]{#struct_0_x1979_37509_x2061927670}[：基于特性的规则]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[feature-group]{lang="EN-US"}]{#struct_0_x1979_37509_281711887}[：基于特性组规则]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[web-menu]{lang="EN-US"}]{#struct_0_x1979_37509_437230868}[：基于]{lang="EN-US" style="font-family:宋体"}[Web]{lang="EN-US"}[菜单的]{style="font-family:宋体"}[规则]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[xml-element]{lang="EN-US"}]{#struct_0_x1979_37509_x914916587}[：基于]{lang="EN-US" style="font-family:宋体"}[XML]{lang="EN-US"}[元素的]{style="font-family:宋体"}[规则]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[oid]{lang="EN-US"}]{#struct_0_x1979_37509_438912262}[：基于]{style="font-family:宋体"}[OID]{lang="EN-US"}[元素的规则]{style="font-family:宋体"}

[[Entity]{lang="EN-US"}]{#struct_0_x1979_37509_1553251392}

[[用户角色规则中定义的具体内容（命令特征字符串、特性名称或者特性组名称）]{style="font-family:宋体"}]{#struct_0_x1979_37509_281711886}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}["]{lang="EN-US" style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_x1979_37509_437230869}["表示所有特性]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}["]{style="font-family:宋体"}]{#struct_0_x1979_37509_x914916588}[\*]{lang="EN-US"}["为通配符，表示]{style="font-family:宋体"}[0]{lang="EN-US"}[个或多个任意字符]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_1553448000}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[role]{lang="EN-US"}**]{#struct_0_x1979_37509_1115277668}

::::: {#444522080 .myid}
[]{#_Toc404782244}[]{#struct_0_x1979_37509_281711885}[]{#_Toc285213498}

**RBAC \-- RBAC配置命令 \-- display role feature**

------------------------------------------------------------------------

[**[display role feature]{lang="EN-US"}**]{#struct_0_x1979_37509_437230870}[命令用来显示特性相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_1423735565}

[**[display role feature ]{lang="EN-US"}**[\[ **name** *feature-name* \| **verbose** \]]{lang="EN-US"}]{#struct_0_x1979_37509_x1238706764}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1979_37509_931978078}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1979_37509_x150002988}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x369948569}

[[network-admin]{lang="EN-US"}]{#struct_0_x1979_37509_1284078795}

[[netword-operator]{lang="EN-US"}]{#struct_0_x1979_37509_281711884}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1979_37509_437230871}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1979_37509_1423735564}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1238772300}

[**[name ]{lang="EN-US"}***[feature-name]{lang="EN-US"}*]{#struct_0_x1979_37509_x1805398893}[：显示指定特性的详细信息，]{style="font-family:宋体"}*[feature-name]{lang="EN-US"}*[表示系统中的特性名称，且所有特性名称中的字母均为小写。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1979_37509_x1238349332}[：显示所有特性的详细信息，即显示特性内包含的所有命令行列表。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x153901908}

[[如果不指定任何关键字，则显示系统中所有特性的名称列表。]{style="font-family:宋体"}]{#struct_0_x1979_37509_x1266581933}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1979_37509_659913206}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RBAC命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1979_37509_x1674603243}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[以下内容中涉及的特性、命令行均为示例，具体的显示信息与设备的实际情况有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1979_37509_1004707107}
:::

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_1925546330}[显示系统中所有特性的名称列表。]{style="font-family:宋体"}

[[\<Sysname\> display role feature]{lang="EN-US"}]{#struct_0_x1979_37509_1946765830}

[Feature: device          (Device configuration related commands)]{lang="EN-US"}

[Feature: interface       (Interface related commands)]{lang="EN-US"}

[Feature: syslog          (Syslog related commands)]{lang="EN-US"}

[Feature: process         (Process related commands)]{lang="EN-US"}

[......（略）]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_x1151474265}[显示所有特性的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display role feature verbose]{lang="EN-US"}]{#struct_0_x1979_37509_x1674603245}

[Feature: device          (Device configuration related commands)]{lang="EN-US"}

[  display clock    (R)]{lang="EN-US"}

[  debugging dev    (W)]{lang="EN-US"}

[  display debugging dev    (R)]{lang="EN-US"}

[  display device \*    (R)]{lang="EN-US"}

[  display diagnostic-information    (R)]{lang="EN-US"}

[  display environment \*    (R)]{lang="EN-US"}

[  display fan \*    (R)]{lang="EN-US"}

[  display power \*    (R)]{lang="EN-US"}

[  display rps \*    (R)]{lang="EN-US"}

[  display current-configuration \*    (R)]{lang="EN-US"}

[  display saved-configuration \*    (R)]{lang="EN-US"}

[  display startup    (R)]{lang="EN-US"}

[  display this \*    (R)]{lang="EN-US"}

[  display version    (R)]{lang="EN-US"}

[  clock datetime \*    (W)]{lang="EN-US"}

[  reboot \*    (W)]{lang="EN-US"}

[  save \*    (W)]{lang="EN-US"}

[  startup saved-configuration \*    (W)]{lang="EN-US"}

[  system-view ; temperature-limit \*    (W)]{lang="EN-US"}

[  system-view ; sysname \*    (W)]{lang="EN-US"}

[  system-view ; clock timezone \*    (W)]{lang="EN-US"}

[  system-view ; configuration replace file \*    (W)]{lang="EN-US"}

[  system-view ; user-interface \* ; idle-timeout \*    (W)]{lang="EN-US"}

[Feature: interface       (Interface related commands)]{lang="EN-US"}

[  reset counters interface \*    (W)]{lang="EN-US"}

[  debugging ifnet \*    (W)]{lang="EN-US"}

[  display port-group manual \*    (R)]{lang="EN-US"}

[  display debugging ifnet    (R)]{lang="EN-US"}

[  display interface \*   (R)]{lang="EN-US"}

[......（略）]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_1811276161}[显示特性]{style="font-family:宋体"}[aaa]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display role feature name aaa]{lang="EN-US"}]{#struct_0_x1979_37509_x1674603246}

[Feature: aaa             (AAA related commands)]{lang="EN-US"}

[  system-view ; domain \*    (W)]{lang="EN-US"}

[  system-view ; header \*    (W)]{lang="EN-US"}

[  system-view ; aaa \*    (W)]{lang="EN-US"}

[  display domain \*    (R)]{lang="EN-US"}

[  system-view ; user-group \*    (W)]{lang="EN-US"}

[  system-view ; local-user \*    (W)]{lang="EN-US"}

[  display local-user \*    (R)]{lang="EN-US"}

[  display user-group \*    (R)]{lang="EN-US"}

[  display debugging local-server    (R)]{lang="EN-US"}

[  debugging local-server \*    (W)]{lang="EN-US"}

[  super \*    (X)]{lang="EN-US"}

[  display password-control \*    (R)]{lang="EN-US"}

[  reset password-control \*    (W)]{lang="EN-US"}

[  system-view ; password-control \*    (W)]{lang="EN-US"}

[]{#struct_0_x1979_37509_245192220}[[表1-2 ]{lang="EN-US"}[display role feature]{lang="EN-US"}]{#_Ref285211276}[命令显示信息描述表（以]{style="font-family:黑体"}[display role feature name aaa]{lang="EN-US"}[的显示字段为例）]{style="font-family:黑体"}

[]{#table_struct_0_401794011}[[字段]{style="font-family:黑体"}]{#struct_0_x1979_37509_x95539695}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1244055925}

[[Feature]{lang="EN-US"}]{#struct_0_x1979_37509_x1902092722}

[[特性名称以及功能简介]{style="font-family:宋体"}]{#struct_0_x1979_37509_x2079088688}

[[system-view ; domain \*]{lang="EN-US"}]{#struct_0_x1979_37509_700624525}

[[系统视图下以]{style="font-family:宋体"}**[domain]{lang="EN-US"}**]{#struct_0_x1979_37509_x1674603247}[开头的所有命令，以及]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域视图下的所有命令]{style="font-family:宋体"}

[[system-view ; header \*]{lang="EN-US"}]{#struct_0_x1979_37509_x1320891721}

[[系统视图下以]{style="font-family:宋体"}**[header]{lang="EN-US"}**]{#struct_0_x1979_37509_x1798398209}[开头的所有命令]{style="font-family:宋体"}

[[system-view ; aaa \*]{lang="EN-US"}]{#struct_0_x1979_37509_1593893632}

[[系统视图下以]{style="font-family:宋体"}**[aaa]{lang="EN-US"}**]{#struct_0_x1979_37509_x1674603248}[开头的所有命令]{style="font-family:宋体"}

[[display domain \*]{lang="EN-US"}]{#struct_0_x1979_37509_1051761274}

[[用户视图下以]{style="font-family:宋体"}**[display domain]{lang="EN-US"}**]{#struct_0_x1979_37509_x1381912548}[开头的所有命令]{style="font-family:宋体"}

[[system-view ; user-group \*]{lang="EN-US"}]{#struct_0_x1979_37509_1567193339}

[[系统视图下以]{style="font-family:宋体"}**[user-group]{lang="EN-US"}**]{#struct_0_x1979_37509_848212350}[开头的所有命令，以及用户组视图下的所有命令]{style="font-family:宋体"}

[[system-view ; local-user \*]{lang="EN-US"}]{#struct_0_x1979_37509_828710015}

[[系统视图下以]{style="font-family:宋体"}**[local-user]{lang="EN-US"}**]{#struct_0_x1979_37509_x1674603249}[开头的所有命令，以及本地用户视图下的所有命令]{style="font-family:宋体"}

[[display user-group \*]{lang="EN-US"}]{#struct_0_x1979_37509_x514322667}

[[用户视图下以]{style="font-family:宋体"}**[display user-group]{lang="EN-US"}**]{#struct_0_x1979_37509_23128351}[开头的所有命令]{style="font-family:宋体"}

[[display debugging local-server]{lang="EN-US"}]{#struct_0_x1979_37509_x1746644272}

[[用户视图下以命令]{style="font-family:宋体"}**[display debugging local-server]{lang="EN-US"}**]{#struct_0_x1979_37509_x1948150062}[开头的所有命令]{style="font-family:宋体"}

[[debugging local-server \*]{lang="EN-US"}]{#struct_0_x1979_37509_x1674603250}

[[用户视图下以]{style="font-family:宋体"}**[debugging local-server]{lang="EN-US"}**]{#struct_0_x1979_37509_1408057170}[开头的所有命令]{style="font-family:宋体"}

[[super \*]{lang="EN-US"}]{#struct_0_x1979_37509_x1782480448}

[[用户视图下以]{style="font-family:宋体"}**[super]{lang="EN-US"}**]{#struct_0_x1979_37509_x1674603251}[开头的所有命令]{style="font-family:宋体"}

[[display password-control \*]{lang="EN-US"}]{#struct_0_x1979_37509_x158026771}

[[用户视图下以]{style="font-family:宋体"}**[display password-control]{lang="EN-US"}**]{#struct_0_x1979_37509_x906873344}[开头的所有命令]{style="font-family:宋体"}

[[reset password-control \*]{lang="EN-US"}]{#struct_0_x1979_37509_x1674603252}

[[用户视图下以]{style="font-family:宋体"}**[reset password-control]{lang="EN-US"}**]{#struct_0_x1979_37509_x1724110712}[开头的所有命令]{style="font-family:宋体"}

[[system-view ; password-control \*]{lang="EN-US"}]{#struct_0_x1979_37509_x865299179}

[[系统视图下以]{style="font-family:宋体"}**[password-control]{lang="EN-US"}**]{#struct_0_x1979_37509_479785054}[开头的所有命令]{style="font-family:宋体"}

[[(W)]{lang="EN-US"}]{#struct_0_x1979_37509_1144799805}

[[命令行的类型为写命令]{style="font-family:宋体"}]{#struct_0_x1979_37509_747986152}

[[(R)]{lang="EN-US"}]{#struct_0_x1979_37509_x865299180}

[[命令行的类型为读命令]{style="font-family:宋体"}]{#struct_0_x1979_37509_480243805}

[[(X)]{lang="EN-US"}]{#struct_0_x1979_37509_574993480}

[[命令行的类型为执行命令]{style="font-family:宋体"}]{#struct_0_x1979_37509_x368550050}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x341237462}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[feature]{lang="EN-US"}**]{#struct_0_x1979_37509_x865299181}

::::: {#-7848027 .myid}
[]{#_Toc404782245}[]{#struct_0_x1979_37509_480309341}[]{#_Toc285213499}

**RBAC \-- RBAC配置命令 \-- display role feature-group**

------------------------------------------------------------------------

[**[display role feature-group]{lang="EN-US"}**]{#struct_0_x1979_37509_x939812275}[命令用来显示特性组信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_199674954}

[**[display role feature-group ]{lang="EN-US"}**[\[ **name** *feature-group-name* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x1979_37509_119488221}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1979_37509_2072931950}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1979_37509_x1746619747}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1979_37509_371418867}

[[network-admin]{lang="EN-US"}]{#struct_0_x1979_37509_1408803156}

[[netword-operator]{lang="EN-US"}]{#struct_0_x1979_37509_x865299182}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1979_37509_480374877}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1979_37509_x603802587}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1979_37509_1636108471}

[**[name ]{lang="EN-US"}***[feature-group-name]{lang="EN-US"}*]{#struct_0_x1979_37509_1972156888}[：显示指定特性组包含的特性名称列表。]{style="font-family:宋体"}*[feature-group-name]{lang="EN-US"}*[表示特性组名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则表示显示所有特性组的相关信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1979_37509_x1875971966}[：显示特性组的详细信息，即显示特性组内的特性所包含的命令行列表。如果不指定本参数，则表示显示特性组中的特性名称列表。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1979_37509_461286195}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RBAC命令.files/image001.png){#图片 2 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1979_37509_x1311671783}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[以下内容中涉及的特性、命令行均为示例，具体的显示信息与设备的实际情况有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1979_37509_x865299183}
:::

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_480440413}[显示所有特性组内的特性名称列表。]{style="font-family:宋体"}

[[\<Sysname\> display role feature-group]{lang="EN-US"}]{#struct_0_x1979_37509_x865299184}

[Feature group: L2]{lang="EN-US"}

[Feature: igmp-snooping   (IGMP-Snooping related commands)]{lang="EN-US"}

[Feature: mld-snooping    (MLD-Snooping related commands)]{lang="EN-US"}

[Feature: lacp            (LACP related commands)]{lang="EN-US"}

[Feature: stp             (STP related commands)]{lang="EN-US"}

[Feature: lldp            (LLDP related commands)]{lang="EN-US"}

[Feature: dldp            (DLDP related commands)]{lang="EN-US"}

[Feature: cfm             (CFM related commands)]{lang="EN-US"}

[Feature: eoam            (EOAM related commands)]{lang="EN-US"}

[Feature: loopbk-detect   (Loopback-detection related commands)]{lang="EN-US"}

[Feature: vlan            (Virtual LAN related commands)]{lang="EN-US"}

[Feature: evb             (EVB related commands)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Feature group: L3]{lang="EN-US"}

[Feature: route           (Route management related commands)]{lang="EN-US"}

[Feature: ospf            (Open Shortest Path First protocol related commands)]{lang="EN-US"}

[Feature: rip             (Routing Information Protocol related commands)]{lang="EN-US"}

[Feature: isis            (ISIS protocol related commands)]{lang="EN-US"}

[Feature: bgp             (Border Gateway Protocol related commands)]{lang="EN-US"}

[Feature: l3vpn           (Layer 3 Virtual Private Network related commands)]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_479981661}[显示所有特性组的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display role feature-group verbose]{lang="EN-US"}]{#struct_0_x1979_37509_x865299186}

[Feature group: L2]{lang="EN-US"}

[Feature: igmp-snooping   (IGMP-Snooping related commands)]{lang="EN-US"}

[  system-view ; igmp-snooping    (W)]{lang="EN-US"}

[  system-view ; vlan \* ; igmp-snooping \*    (W)]{lang="EN-US"}

[  system-view ; interface \* ; igmp-snooping \*    (W)]{lang="EN-US"}

[  display igmp-snooping \*    (R)]{lang="EN-US"}

[  reset igmp-snooping \*    (W)]{lang="EN-US"}

[  debugging igmp-snooping \*    (W)]{lang="EN-US"}

[  display debugging igmp-snooping \*    (R)]{lang="EN-US"}

[Feature: mld-snooping    (MLD-Snooping related commands)]{lang="EN-US"}

[  system-view ; mld-snooping    (W)]{lang="EN-US"}

[  system-view ; vlan \* ; mld-snooping \*    (W)]{lang="EN-US"}

[  system-view ; interface \* ; mld-snooping \*    (W)]{lang="EN-US"}

[  display mld-snooping \*    (R)]{lang="EN-US"}

[  reset mld-snooping \*    (W)]{lang="EN-US"}

[  debugging mld-snooping \*    (W)]{lang="EN-US"}

[  display debugging mld-snooping \*    (R)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Feature group: L3]{lang="EN-US"}

[Feature: route           (Route management related commands)]{lang="EN-US"}

[  display ip routing-table \*    (R)]{lang="EN-US"}

[  display ipv6 routing-table \*    (R)]{lang="EN-US"}

[  display router id \*    (R)]{lang="EN-US"}

[  reset ip routing-table statistics \*    (W)]{lang="EN-US"}

[  reset ipv6 routing-table statistics \*    (W)]{lang="EN-US"}

[  debugging rm \*    (W)]{lang="EN-US"}

[  system-view ; ip route-static \*    (W)]{lang="EN-US"}

[  system-view ; ipv6 route-static \*    (W)]{lang="EN-US"}

[  system-view ; router id \*    (W)]{lang="EN-US"}

[  system-view ; delete static-routes \*    (W)]{lang="EN-US"}

[  system-view ; delete ipv6 static-routes \*    (W)]{lang="EN-US"}

[Feature: ospf            (Open Shortest Path First protocol related commands)]{lang="EN-US"}

[  display ospf \*    (R)]{lang="EN-US"}

[  display ospfv3 \*    (R)]{lang="EN-US"}

[  reset ospf \*    (W)]{lang="EN-US"}

[  debugging ospf \*    (W)]{lang="EN-US"}

[  debugging ospfv3 \*    (W)]{lang="EN-US"}

[  system-view ; ospf \*    (W)]{lang="EN-US"}

[  system-view ; interface \* ; ospf \*    (W)]{lang="EN-US"}

[  system-view ; ospfv3 \*    (W)]{lang="EN-US"}

[  system-view ; interface \* ; ospfv3 \*    (W)]{lang="EN-US"}

[Feature: rip             (Routing Information Protocol related commands)]{lang="EN-US"}

[  display rip \*    (R)]{lang="EN-US"}

[  display ripng \*    (R)]{lang="EN-US"}

[  debugging rip \*    (W)]{lang="EN-US"}

[  debugging ripng \*    (W)]{lang="EN-US"}

[  system-view ; rip \*    (W)]{lang="EN-US"}

[  system-view ; interface \* ; rip \*    (W)]{lang="EN-US"}

[  system-view ; ripng \*    (W)]{lang="EN-US"}

[  system-view ; interface \* ; ripng \*    (W)]{lang="EN-US"}

[Feature: isis            (ISIS protocol related commands)]{lang="EN-US"}

[  display isis \*    (R)]{lang="EN-US"}

[  reset isis \*    (W)]{lang="EN-US"}

[  debugging isis \*    (W)]{lang="EN-US"}

[  display debugging isis \*    (R)]{lang="EN-US"}

[  system-view ; isis \*    (W)]{lang="EN-US"}

[  system-view ; interface \* ; isis \*    (W)]{lang="EN-US"}

[Feature: bgp             (Border Gateway Protocol related commands)]{lang="EN-US"}

[  display bgp \*    (R)]{lang="EN-US"}

[  reset bgp \*    (W)]{lang="EN-US"}

[  refresh bgp \*    (W)]{lang="EN-US"}

[  debugging bgp \*    (W)]{lang="EN-US"}

[  system-view ; bgp \*    (W)]{lang="EN-US"}

[Feature: l3vpn           (Layer 3 Virtual Private Network related commands)]{lang="EN-US"}

[  display ip vpn-instance \*    (R)]{lang="EN-US"}

[  system-view ; ip vpn-instance \*    (W)]{lang="EN-US"}

[  system-view ; interface \* ; ip binding vpn-instance \*    (W)]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_480112733}[显示特性组]{style="font-family:宋体"}[L3]{lang="EN-US"}[的特性名称列表。]{style="font-family:宋体"}

[[\<Sysname\> display role feature-group name L3]{lang="EN-US"}]{#struct_0_x1979_37509_x865299187}

[Feature group: L3]{lang="EN-US"}

[Feature: route           (Route management related commands)]{lang="EN-US"}

[Feature: ospf            (Open Shortest Path First protocol related commands)]{lang="EN-US"}

[Feature: rip             (Routing Information Protocol related commands)]{lang="EN-US"}

[Feature: isis            (ISIS protocol related commands)]{lang="EN-US"}

[Feature: bgp             (Border Gateway Protocol related commands)]{lang="EN-US"}

[Feature: l3vpn           (Layer 3 Virtual Private Network related commands)]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display role feature-group]{lang="EN-US"}]{#struct_0_x1979_37509_480178269}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_389129265}[[字段]{style="font-family:黑体"}]{#struct_0_x1979_37509_x790682099}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1979_37509_1528773945}

[[Feature group]{lang="EN-US"}]{#struct_0_x1979_37509_x745041589}

[[特性组名称，其中]{style="font-family:宋体"}[L2]{lang="EN-US"}]{#struct_0_x1979_37509_718308604}[和]{style="font-family:宋体"}[L3]{lang="EN-US"}[为系统预定义的两个特性组]{style="font-family:宋体"}

[[Feature]{lang="EN-US"}]{#struct_0_x1979_37509_x865299188}

[[特性名称以及功能简介]{style="font-family:宋体"}]{#struct_0_x1979_37509_479719517}

[[关于特性内具体命令的详细介绍请参考]{style="font-family:宋体"}]{#struct_0_x1979_37509_1532141848}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-2]{lang="EN-US"}](?444522080#_Ref285211276)

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_293576804}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[feature]{lang="EN-US"}**]{#struct_0_x1979_37509_x1858491049}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[role feature-group]{lang="EN-US"}**]{#struct_0_x1979_37509_1499292666}

::: {#321417343 .myid}
[]{#_Toc404782246}[]{#struct_0_x1979_37509_x646352965}[]{#_Toc285213500}[]{#_Toc301724426}[]{#_Toc301787485}

**RBAC \-- RBAC配置命令 \-- feature**

------------------------------------------------------------------------

[**[feature]{lang="EN-US"}**]{#struct_0_x1979_37509_x1081530416}[命令用来向特性组中添加一个特性。]{style="font-family:宋体"}

[**[undo feature]{lang="EN-US"}**]{#struct_0_x1979_37509_1473352981}[命令用来删除特性组中的某个特性。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x2020663720}

[**[feature ]{lang="EN-US"}***[feature-name]{lang="EN-US"}*]{#struct_0_x1979_37509_x755585630}

[**[undo feature ]{lang="EN-US"}***[feature-name]{lang="EN-US"}*]{#struct_0_x1979_37509_1280224099}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x99595753}

[[自定义特性组中不包括任何特性。]{style="font-family:宋体"}]{#struct_0_x1979_37509_1770232612}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x721215873}

[[特性组视图]{style="font-family:宋体"}]{#struct_0_x1979_37509_x1814388001}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1979_37509_1855678664}

[[network-admin]{lang="EN-US"}]{#struct_0_x1979_37509_1473352980}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1979_37509_x2020729256}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1985775887}

[*[feature-name]{lang="EN-US"}*]{#struct_0_x1979_37509_1140250301}[：系统支持的特性名称，所有特性名称中的字母均为小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1979_37509_621364248}

[[可通过多次执行本命令，向特性组中添加多个特性。]{style="font-family:宋体"}]{#struct_0_x1979_37509_1257635132}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1457267259}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_462166608}[向特性组]{style="font-family:宋体"}[security-features]{lang="EN-US"}[中添加特性]{style="font-family:宋体"}[AAA]{lang="EN-US"}[和]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1979_37509_1473352979}

[\[Sysname\] role feature-group name security-features]{lang="EN-US"}

[\[Sysname-featuregrp-security-features\] feature aaa]{lang="EN-US"}

[\[Sysname-featuregrp-security-features\] feature acl]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x2021188001}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display role feature]{lang="EN-US"}**]{#struct_0_x1979_37509_1438738765}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display role feature-group]{lang="EN-US"}**]{#struct_0_x1979_37509_x1161512552}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[role feature-group]{lang="EN-US"}**]{#struct_0_x1979_37509_419516626}
:::

::: {#1734184062 .myid}
[]{#_Toc404782247}[]{#struct_0_x1979_37509_1665215613}[]{#_Toc285213501}

**RBAC \-- RBAC配置命令 \-- interface policy deny**

------------------------------------------------------------------------

[**[interface policy deny]{lang="EN-US"}**]{#struct_0_x1979_37509_1403362069}[命令用来进入接口策略视图。]{style="font-family:宋体"}

[**[undo interface policy deny]{lang="EN-US"}**]{#struct_0_x1979_37509_x938198315}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_1473352978}

[**[interface policy deny]{lang="EN-US"}**]{#struct_0_x1979_37509_x2021253537}

[**[undo interface policy deny]{lang="EN-US"}**]{#struct_0_x1979_37509_1276070533}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x625658616}

[[用户具有操作任何接口的权限。]{style="font-family:宋体"}]{#struct_0_x1979_37509_1573561970}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1820868667}

[[用户角色视图]{style="font-family:宋体"}]{#struct_0_x1979_37509_1379859470}

[[【用户角色】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x2103043439}

[[network-admin]{lang="EN-US"}]{#struct_0_x1979_37509_1709086336}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1979_37509_1473352977}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x2020794785}

[[进入接口策略视图后，如果不配置允许操作的接口列表，则用户将没有操作任何接口的权限；如果需要限制或区分用户对接口资源的使用权限，则还应该通过]{style="font-family:宋体"}**[permit interface]{lang="EN-US"}**]{#struct_0_x1979_37509_x1850757522}[命令配置允许用户操作的接口列表。若接口策略视图中未配置允许操作的接口列表，则表示不允许用户操作所有的接口。对接口的操作指的是创建接口并进入接口视图、删除和应用接口。其中，创建和删除接口，仅针对逻辑接口。]{style="font-family:宋体"}

[[允许修改用户角色的接口策略，但修改后的策略只在被授权该角色的用户重新登录时才会生效。]{style="font-family:宋体"}]{#struct_0_x1979_37509_x1214966402}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1979_37509_683902605}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_1993084509}[在用户角色]{style="font-family:宋体"}[role1]{lang="EN-US"}[中，进入接口策略视图，并禁止角色为]{style="font-family:宋体"}[role1]{lang="EN-US"}[的用户操作任何接口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1979_37509_1123691289}

[\[Sysname\] role name role1]{lang="EN-US"}

[\[Sysname-role-role1\] interface policy deny]{lang="EN-US"}

[\[Sysname-role-role1-ifpolicy\] quit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_1473352976}[在用户角色]{style="font-family:宋体"}[role1]{lang="EN-US"}[中，进入接口策略视图，允许角色为]{style="font-family:宋体"}[role1]{lang="EN-US"}[的用户操作接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[到]{style="font-family:宋体"} [GigabitEthernet1/0/5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1979_37509_x2020860321}

[\[Sysname\] role name role1]{lang="EN-US"}

[\[Sysname-role-role1\] interface policy deny]{lang="EN-US"}

[\[Sysname-role-role1-ifpolicy\] permit interface gigabitethernet 1/0/1 to gigabitethernet 1/0/5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_1199454475}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}]{.ItemStepChar}[**[display role]{lang="EN-US"}**]{.ItemStepChar}]{#struct_0_x1979_37509_x1755960686}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[permit interface]{lang="EN-US"}**]{#struct_0_x1979_37509_1117133574}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[role]{lang="EN-US"}**]{#struct_0_x1979_37509_x565729480}
:::

::: {#-414838793 .myid}
[]{#_Toc404782248}[]{#struct_0_x1979_37509_x1721437903}[]{#_Toc285213502}

**RBAC \-- RBAC配置命令 \-- permit interface**

------------------------------------------------------------------------

[**[permit interface]{lang="EN-US"}**]{#struct_0_x1979_37509_x965642724}[命令用来配置允许用户操作的接口列表。]{style="font-family:宋体"}

[**[undo permit interface]{lang="EN-US"}**]{#struct_0_x1979_37509_1473352975}[命令用来禁止用户操作指定的或所有的接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x2020925857}

[**[permit interface ]{lang="EN-US"}***[interface-list]{lang="EN-US"}*]{#struct_0_x1979_37509_x968228276}

[**[undo permit interface ]{lang="EN-US"}**]{#struct_0_x1979_37509_x439714877}[\[ ]{lang="DA"}*[interface-list]{lang="EN-US"}***[ ]{lang="EN-US"}**[\]]{lang="DA"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1979_37509_1578307657}

[[接口策略视图下未定义允许操作的接口列表，用户没有操作任何接口的权限。]{style="font-family:宋体"}]{#struct_0_x1979_37509_429882419}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1979_37509_646911143}

[[接口策略视图]{style="font-family:宋体"}]{#struct_0_x1979_37509_x1824216450}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x188547462}

[[network-admin]{lang="EN-US"}]{#struct_0_x1979_37509_1473352974}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1979_37509_x2020991393}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1369270360}

[**[interface]{lang="EN-US"}***[ interface-list]{lang="EN-US"}*]{#struct_0_x1979_37509_1425160626}[：允许用户操作的接口列表，表示多个接口，表示方式为]{style="font-family:宋体"}*[interface-lis]{lang="EN-US"}*[t = { *interface-type* *interface-number* \[ to *interface-type interface-number* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[为接口类型，]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[为接口编号。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。起始接口类型必须和终止接口类型一致，并且终止接口编号必须大于起始接口编号。如果不指定本参数，则表示指定所有接口。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1979_37509_1358050239}

[[对接口的操作指的是创建并进入接口视图、删除和应用接口。其中，创建和删除接口，只针对逻辑接口。]{style="font-family:宋体"}]{#struct_0_x1979_37509_862135570}

[[可通过多次执行此命令向接口列表中添加允许用户操作的接口。]{style="font-family:宋体"}]{#struct_0_x1979_37509_1512959992}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1029884863}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_1473352973}[创建用户角色]{style="font-family:宋体"}[role1]{lang="EN-US"}[并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1979_37509_x2020532641}

[\[Sysname\] role name role1]{lang="EN-US"}

[[\# ]{lang="FR"}]{#struct_0_x1979_37509_1079062797}[配置用户角色规则]{style="font-family:宋体"}[1]{lang="EN-US"}[，允许用户执行进入接口视图以及接口视图下的相关命令。]{style="font-family:宋体"}

[[\[Sysname-role-role1\] rule 1 permit command system-view ; interface \*]{lang="EN-US"}]{#struct_0_x1979_37509_525606452}

[[\# ]{lang="FR"}]{#struct_0_x1979_37509_1624719779}[配置用户角色规则]{style="font-family:宋体"}[2]{lang="EN-US"}[，允许用户执行创建]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[以及进入]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图后的相关命令。]{style="font-family:宋体"}

[[\[Sysname-role-role1\] rule 2 permit command system-view ; vlan \*]{lang="EN-US"}]{#struct_0_x1979_37509_789269738}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_958509716}[配置用户角色]{style="font-family:宋体"}[role1]{lang="EN-US"}[仅可以对接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[以及]{style="font-family:宋体"} [GigabitEthernet1/0/5]{lang="EN-US"}[～]{style="font-family:宋体"} [GigabitEthernet1/0/7]{lang="EN-US"}[进行操作。]{style="font-family:宋体"}

[[\[Sysname-role-role1\] interface policy deny]{lang="EN-US"}]{#struct_0_x1979_37509_68547280}

[\[Sysname-role-role1-ifpolicy\] permit interface gigabitethernet 1/0/1 gigabitethernet 1/0/5 to gigabitethernet 1/0/7]{lang="EN-US"}

[[当拥有用户角色]{style="font-family:宋体"}[role1]{lang="EN-US"}]{#struct_0_x1979_37509_1473352972}[的用户登录设备后，可以操作接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[以及]{style="font-family:宋体"} [GigabitEthernet1/0/5]{lang="EN-US"}[～]{style="font-family:宋体"}[GigabitEthernet1/0/7]{lang="EN-US"}[，但不能操作其它接口。]{style="font-family:宋体"}

[[配置结果验证如下：]{style="font-family:宋体"}]{#struct_0_x1979_37509_x2020598177}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[进入接口]{lang="EN-US" style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}]{#struct_0_x1979_37509_1812841786}[视图。]{lang="EN-US" style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1979_37509_742231946}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[将接口]{lang="EN-US" style="font-family:宋体"}[GigabitEthernet1/0/5]{lang="EN-US"}]{#struct_0_x1979_37509_1473983342}[加入到]{lang="EN-US" style="font-family:
宋体"}[VLAN 10]{lang="FR"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1979_37509_662022271}

[\[Sysname\] vlan 10]{lang="EN-US"}

[\[Sysname-vlan10\] port gigabitethernet 1/0/5]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[无法进入接口]{lang="EN-US" style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}]{#struct_0_x1979_37509_1099628365}[视图。]{lang="EN-US" style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1979_37509_x98462443}

[\[Sysname\] interface gigabitethernet 1/0/2]{lang="EN-US"}

[Permission denied.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_1632769941}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}]{.ItemStepChar}[**[display role]{lang="EN-US"}**]{.ItemStepChar}]{#struct_0_x1979_37509_x1234680590}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[interface policy deny]{lang="EN-US"}**]{#struct_0_x1979_37509_x1892618972}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[role]{lang="EN-US"}**]{#struct_0_x1979_37509_454628501}
:::

::::: {#-1953547838 .myid}
[]{#_Toc404782249}[]{#struct_0_x1979_37509_x911424247}

**RBAC \-- RBAC配置命令 \-- permit security-zone**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RBAC命令.files/image002.png){border="0" width="62" height="26"}]{lang="EN-US"}]{#struct_0_x1979_37509_x911489783}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1979_37509_1046741730}
:::

[ ]{lang="EN-US"}

[**[permit security-zone]{lang="EN-US"}**]{#struct_0_x1979_37509_1604171795}[命令用来配置允许用户操作的]{style="font-family:宋体"}[安全域]{style="font-family:宋体"}[列表。]{style="font-family:宋体"}

[**[undo permit security-zone]{lang="EN-US"}**]{#struct_0_x1979_37509_x911293175}[命令用来禁止用户操作指定的或所有的]{style="font-family:
宋体"}[安全域]{style="font-family:宋体"}[实例。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x87657437}

[**[permit security-zone ]{lang="FR"}**]{#struct_0_x1979_37509_1954272463}*[security-zone-name]{lang="FR"}*[&\<1-10\>]{lang="FR"}

[**[undo permit security-zone ]{lang="EN-US"}**]{#struct_0_x1979_37509_x911358711}[\[ ]{lang="DA"}*[security-zone-name]{lang="FR"}*[&\<1-10\>]{lang="FR"}**[ ]{lang="FR"}**[\]]{lang="DA"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x541165803}

[[安全域]{style="font-family:宋体"}]{#struct_0_x1979_37509_x1934249223}[策略视图下未定义允许操作的]{style="font-family:宋体"}[安全域]{style="font-family:宋体"}[列表，用户没有操作任何]{style="font-family:宋体"}[安全域]{style="font-family:宋体"}[的权限。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x911817464}

[[安全域]{style="font-family:宋体"}]{#struct_0_x1979_37509_x500283462}[策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x263029730}

[[network-admin]{lang="EN-US"}]{#struct_0_x1979_37509_x911883000}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1979_37509_x2046200496}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x979389021}

[*[security-zone-name]{lang="EN-US"}*[&\<1-10\>]{lang="EN-US"}]{#struct_0_x1979_37509_x911686392}[：表示允许用户操作的]{style="font-family:宋体"}[安全域]{style="font-family:宋体"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。如果不指定本参数，则表示指定所有]{style="font-family:宋体"}[安全域]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1979_37509_1051835420}

[[对]{style="font-family:宋体"}]{#struct_0_x1979_37509_x552674044}[安全域]{style="font-family:宋体"}[的"操作"指的是创建]{style="font-family:宋体"}[安全域]{style="font-family:宋体"}[并进入其视图、删除和应用]{style="font-family:宋体"}[安全域]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[可通过多次执行此本命令向安全域列表中添加允许用户操作的]{style="font-family:宋体"}]{#struct_0_x1979_37509_1942626402}[安全域]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x911751928}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_x478781913}[创建用户角色]{style="font-family:宋体"}[role1]{lang="EN-US"}[并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1979_37509_x911555320}

[\[Sysname\] role name role1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_x535941043}[配置用户角色规则]{style="font-family:宋体"}[1]{lang="EN-US"}[，允许用户执行系统视图下的所有命令以及所有子视图下的命令。]{style="font-family:宋体"}

[[\[Sysname-role-role1\] rule 1 permit command system-view ; \*]{lang="EN-US"}]{#struct_0_x1979_37509_x1419809192}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_618964379}[配置用户角色]{style="font-family:宋体"}[role1]{lang="EN-US"}[仅可以对安全域]{style="font-family:宋体"}[trust]{lang="EN-US"}[和]{style="font-family:宋体"}[abc]{lang="EN-US"}[进行操作。]{style="font-family:宋体"}

[[\[Sysname-role-role1\] ]{lang="EN-US"}]{#struct_0_x1979_37509_x911620856}[security-zone]{lang="FR"}[ policy deny]{lang="EN-US"}

[\[Sysname-role-role1-zonepolicy\] permit ]{lang="EN-US"}[security-zone]{lang="FR"}[ ]{lang="FR"}[trust abc]{lang="EN-US"}

[[拥有用户角色]{style="font-family:宋体"}[role1]{lang="EN-US"}]{#struct_0_x1979_37509_303026914}[的用户登录设备后，可以操作安全域]{style="font-family:宋体"}[abc]{lang="EN-US"}[，但不能操作其它安全域。]{style="font-family:宋体"}

[[配置结果验证如下：]{style="font-family:宋体"}]{#struct_0_x1979_37509_x911424248}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[创建并进入名称为]{style="font-family:宋体"}]{#struct_0_x1979_37509_245998861}[abc]{lang="EN-US"}[的安全域视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1979_37509_2047261726}

[\[Sysname\] security-zone name abc]{lang="EN-US"}

[\[Sysname-security-zone-abc\] ]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[创建源安全域]{style="font-family:宋体;color:black"}]{#struct_0_x1979_37509_x911489784}[trust]{lang="EN-US" style="color:black"}[到目的安全域]{style="font-family:宋体;
color:black"}[abc]{lang="EN-US" style="color:black"}[的域间实例]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1979_37509_1047069410}

[\[Sysname\] interzone source trust destination abc]{lang="EN-US"}

[\[Sysname-interzone-Trust-abc\] ]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[无法创建名称为]{style="font-family:宋体"}]{#struct_0_x1979_37509_x1510253240}[local]{lang="EN-US"}[的安全域或进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1979_37509_x911293176}

[\[Sysname\] security-zone name local]{lang="EN-US"}

[Permission denied.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x87460829}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}]{.ItemStepChar}[**[display role]{lang="EN-US"}**]{.ItemStepChar}]{#struct_0_x1979_37509_207117808}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[role]{lang="EN-US"}**]{#struct_0_x1979_37509_x911358712}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[security-zone]{lang="EN-US"}[ policy deny]{lang="EN-US"}**]{#struct_0_x1979_37509_x540969195}
:::::

::: {#849005739 .myid}
[]{#_Toc404782250}[]{#struct_0_x1979_37509_x419180222}[]{#_Toc285213503}

**RBAC \-- RBAC配置命令 \-- permit vlan**

------------------------------------------------------------------------

[**[permit vlan]{lang="EN-US"}**]{#struct_0_x1979_37509_x1277898216}[命令用来配置允许用户操作的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表。]{style="font-family:宋体"}

[**[undo permit vlan]{lang="EN-US"}**]{#struct_0_x1979_37509_723499230}[命令用来禁止用户操作指定的或所有的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x98462444}

[**[permit vlan ]{lang="EN-US"}***[vlan-id-list]{lang="EN-US"}*]{#struct_0_x1979_37509_1632769948}

[**[undo permit vlan ]{lang="DA"}**]{#struct_0_x1979_37509_x1235139342}[\[ *vlan-id-list* \]]{lang="DA"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1979_37509_1703936676}

[[VLAN]{lang="EN-US"}]{#struct_0_x1979_37509_1403194365}[接口视图下未定义允许操作的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，用户没有操作任何]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的权限。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x193530311}

[[VLAN]{lang="EN-US"}]{#struct_0_x1979_37509_1431643655}[策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x964851345}

[[network-admin]{lang="EN-US"}]{#struct_0_x1979_37509_x185821601}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1979_37509_x98462445}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1979_37509_1632769947}

[*[vlan-id-list]{lang="EN-US"}*]{#struct_0_x1979_37509_x1234549518}[：允许用户操作的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示方式为]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id1* \[ to *vlan-id2* \] }&\<1-10\>]{lang="EN-US"}[，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[，]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以重复输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。终止]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号必须大于起始]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号。如果不指定本参数，则表示指定所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1979_37509_1352282680}

[[对]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1979_37509_x1453310955}[的操作指的是创建]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[并进入]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图、删除和应用]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[可通过多次执行此命令向]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1979_37509_x501039922}[列表中添加允许用户操作的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1041757710}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_1844243634}[创建用户角色]{style="font-family:宋体"}[role1]{lang="EN-US"}[并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1979_37509_x98462446}

[\[Sysname\] role name role1]{lang="EN-US"}

[[\# ]{lang="FR"}]{#struct_0_x1979_37509_1632769946}[配置用户角色规则]{style="font-family:宋体"}[1]{lang="EN-US"}[，允许用户执行进入接口视图以及接口视图下的相关命令。]{style="font-family:宋体"}

[[\[Sysname-role-role1\] rule 1 permit command system-view ; interface \*]{lang="EN-US"}]{#struct_0_x1979_37509_x1234483982}

[[\# ]{lang="FR"}]{#struct_0_x1979_37509_1637876722}[配置用户角色规则]{style="font-family:宋体"}[2]{lang="EN-US"}[，允许用户执行创建]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[以及进入]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图后的相关命令。]{style="font-family:宋体"}

[[\[Sysname-role-role1\] rule 2 permit command system-view ; vlan \*]{lang="EN-US"}]{#struct_0_x1979_37509_1292905182}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_1078310239}[配置用户角色]{style="font-family:宋体"}[role1]{lang="EN-US"}[仅可以操作]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[、]{style="font-family:宋体"}[VLAN 4]{lang="EN-US"}[、]{style="font-family:宋体"}[VLAN 50]{lang="EN-US"}[～]{style="font-family:宋体"}[VLAN 100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname-role-role1\] vlan policy deny]{lang="EN-US"}]{#struct_0_x1979_37509_928134445}

[\[Sysname-role-role1-vlanpolicy\] permit vlan 2 4 50 to 100]{lang="EN-US"}

[[当拥有用户角色]{style="font-family:宋体"}[role1]{lang="EN-US"}]{#struct_0_x1979_37509_x95787002}[的用户登录设备后，可以操作]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[、]{style="font-family:宋体"}[VLAN 4]{lang="EN-US"}[、]{style="font-family:宋体"}[VLAN 50]{lang="EN-US"}[～]{style="font-family:宋体"}[VLAN 100]{lang="EN-US"}[，但不能操作其它]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[配置结果验证如下：]{style="font-family:宋体"}]{#struct_0_x1979_37509_x98462447}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[创建并进入]{style="font-family:宋体"}]{#struct_0_x1979_37509_1632769945}[VLAN 100]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="DA"}]{#struct_0_x1979_37509_x1234418446}

[\[]{lang="DA"}[Sysname]{lang="EN-US"}[\] vlan 100]{lang="DA"}

[\[]{lang="DA"}[Sysname]{lang="EN-US"}[-vlan100\]]{lang="DA"}

[[·[              ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[向]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1979_37509_x2089183318}[VLAN 100]{lang="DA"}[中添加]{lang="EN-US" style="font-family:宋体"}[Access]{lang="DA"}[类型的端口]{lang="EN-US" style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="DA"}]{#struct_0_x1979_37509_1629698551}

[\[]{lang="DA"}[Sysname]{lang="EN-US"}[\] interface]{lang="DA"}[ ]{lang="DA"}[gigabitethernet 1/0/1]{lang="EN-US"}

[\[]{lang="DA"}[Sysname]{lang="EN-US"}[-]{lang="DA"}[GigabitEthernet1/0/1]{lang="EN-US"}[\] port access vlan 100]{lang="DA"}

[[·[              ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[无法创建]{style="font-family:宋体"}]{#struct_0_x1979_37509_x1834821518}[VLAN 101]{lang="DA"}[或进入其]{style="font-family:宋体"}[视图。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1979_37509_x1619236752}

[\[Sysname\] vlan 101]{lang="EN-US"}

[Permission denied.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x98462448}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}]{.ItemStepChar}[**[display role]{lang="EN-US"}**]{.ItemStepChar}]{#struct_0_x1979_37509_1632769952}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[role]{lang="EN-US"}**]{#struct_0_x1979_37509_x1234746127}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vlan policy deny]{lang="EN-US"}**]{#struct_0_x1979_37509_x2038562313}
:::

::: {#-2002014661 .myid}
[]{#_Toc404782251}[]{#struct_0_x1979_37509_413421885}[]{#_Toc285213504}

**RBAC \-- RBAC配置命令 \-- permit vpn-instance**

------------------------------------------------------------------------

[**[permit vpn-instance]{lang="EN-US"}**]{#struct_0_x1979_37509_x376462025}[命令用来配置允许用户操作的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[列表。]{style="font-family:宋体"}

[**[undo permit vpn-instance]{lang="EN-US"}**]{#struct_0_x1979_37509_1529801655}[命令用来禁止用户操作指定的或所有的]{style="font-family:
宋体"}[VPN]{lang="EN-US"}[实例。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1086216329}

[**[permit vpn-instance ]{lang="FR"}**]{#struct_0_x1979_37509_927917824}*[vpn-instance-name]{lang="FR"}*[&\<1-10\>]{lang="FR"}

[**[undo permit vpn-instance ]{lang="EN-US"}**]{#struct_0_x1979_37509_x98462449}[\[ ]{lang="DA"}*[vpn-instance-name]{lang="FR"}*[&\<1-10\>]{lang="FR"}**[ ]{lang="FR"}**[\]]{lang="DA"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1979_37509_1632769951}

[[VPN]{lang="EN-US"}]{#struct_0_x1979_37509_x1234680591}[策略视图下未定义允许操作的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[列表，用户没有操作任何]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的权限。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x326535031}

[[VPN]{lang="EN-US"}]{#struct_0_x1979_37509_15573863}[策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x551200331}

[[network-admin]{lang="EN-US"}]{#struct_0_x1979_37509_x1473646107}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1979_37509_x1953642169}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1979_37509_1055807194}

[*[vpn-instance-name]{lang="EN-US"}*[&\<1-10\>]{lang="EN-US"}]{#struct_0_x1979_37509_x98462450}[：表示允许用户操作的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[实例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。如果不指定本参数，则表示指定所有]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[实例。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x323545192}

[[对]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x1979_37509_x2055101583}[实例的"操作"指的是创建]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[实例并进入其视图、删除和应用]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。]{style="font-family:宋体"}

[[可通过多次执行此命令向接口列表中添加允许用户操作的]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x1979_37509_413441657}[实例。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1557784727}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_x1690523670}[创建用户角色]{style="font-family:宋体"}[role1]{lang="EN-US"}[并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1979_37509_406903237}

[\[Sysname\] role name role1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_x5822470}[配置用户角色规则]{style="font-family:宋体"}[1]{lang="EN-US"}[，允许用户执行系统视图下的所有命令以及所有子视图下的命令。]{style="font-family:宋体"}

[[\[Sysname-role-role1\] rule 1 permit command system-view ; \*]{lang="EN-US"}]{#struct_0_x1979_37509_x98462451}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_x323545193}[配置用户角色]{style="font-family:宋体"}[role1]{lang="EN-US"}[仅可以对]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[进行操作。]{style="font-family:宋体"}

[[\[Sysname-role-role1\] vpn policy deny]{lang="EN-US"}]{#struct_0_x1979_37509_x2055036047}

[\[Sysname-role-role1-vpnpolicy\] permit vpn-instance vpn1]{lang="EN-US"}

[[拥有用户角色]{style="font-family:宋体"}[role1]{lang="EN-US"}]{#struct_0_x1979_37509_1307235331}[的用户登录设备后，可以操作]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[，但不能操作其它]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。]{style="font-family:宋体"}

[[配置结果验证如下：]{style="font-family:宋体"}]{#struct_0_x1979_37509_x1282839760}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[进入名称为]{style="font-family:宋体"}]{#struct_0_x1979_37509_x901321903}[vpn1]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1979_37509_x610376292}

[\[Sysname\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-vpn-instance-vpn1\]]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设置]{style="font-family:宋体"}]{#struct_0_x1979_37509_1121827720}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[radius1]{lang="EN-US"}[的主计费服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.110.1.2]{lang="EN-US"}[，且属于]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1979_37509_x98462452}

[\[Sysname\] radius scheme radius1]{lang="EN-US"}

[\[Sysname-radius-radius1\] primary accounting 10.110.1.2 vpn-instance vpn1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[无法创建名称为]{style="font-family:宋体"}]{#struct_0_x1979_37509_x323545194}[vpn2]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例或进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1979_37509_x2055494799}

[\[Sysname\] ip vpn-instance vpn2]{lang="EN-US"}

[Permission denied.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_961505330}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}]{.ItemStepChar}[**[display role]{lang="EN-US"}**]{.ItemStepChar}]{#struct_0_x1979_37509_104514779}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[role]{lang="EN-US"}**]{#struct_0_x1979_37509_x1753482071}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vpn-instance policy deny]{lang="EN-US"}**]{#struct_0_x1979_37509_x1031695593}
:::

::: {#1628940268 .myid}
[]{#_Toc404782252}[]{#struct_0_x1979_37509_x2054777579}[]{#_Toc285213505}

**RBAC \-- RBAC配置命令 \-- role**

------------------------------------------------------------------------

[**[role]{lang="EN-US"}**]{#struct_0_x1979_37509_1676884079}[命令用来创建用户角色，并进入用户角色视图。]{style="font-family:宋体"}

[**[undo role]{lang="EN-US"}**]{#struct_0_x1979_37509_x1706883471}[命令用来删除指定的用户角色。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_1494681689}

[**[role]{lang="EN-US"}**[ **name** *role-name*]{lang="EN-US"}]{#struct_0_x1979_37509_1192092632}

[**[undo role name]{lang="EN-US"}***[ role-name]{lang="EN-US"}*]{#struct_0_x1979_37509_1802071928}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x544040825}

[[系统预定义的用户角色为]{style="font-family:宋体"}[network-admin]{lang="EN-US"}]{#struct_0_x1979_37509_1704792171}[、]{style="font-family:宋体"}[network-operator]{lang="EN-US"}[、]{style="font-family:宋体"}[mdc-admin]{lang="EN-US"}[、]{style="font-family:宋体"}[mdc-operator]{lang="EN-US"}[、]{style="font-family:宋体"}[context-admin]{lang="EN-US"}[、]{style="font-family:宋体"}[context-operator]{lang="EN-US"}[、]{style="font-family:宋体"}[level-*n*]{lang="EN-US"}[（]{style="font-family:宋体"}*[n]{lang="EN-US"}*[为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:
宋体"}[15]{lang="EN-US"}[的整数）、]{style="font-family:宋体"}[security-audit]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1979_37509_538851915}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1979_37509_x2054777580}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1979_37509_466047458}

[[network-admin]{lang="EN-US"}]{#struct_0_x1979_37509_2090930608}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1979_37509_x2136126749}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1080708882}

[**[name]{lang="EN-US"}***[ role-name]{lang="EN-US"}*]{#struct_0_x1979_37509_x1297185059}[：用户角色名称，]{style="font-family:宋体"}*[role-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1259220015}

[[除系统预定义的缺省用户角色之外，系统中最多允许创建]{style="font-family:宋体"}[64]{lang="EN-US"}]{#struct_0_x1979_37509_x1596229306}[个用户角色。]{style="font-family:宋体"}

[[缺省的用户角色不能被删除，而且其中的]{style="font-family:宋体"}[network-admin]{lang="EN-US"}]{#struct_0_x1979_37509_189034629}[、]{style="font-family:宋体"}[network-operator]{lang="EN-US"}[、]{style="font-family:宋体"}[mdc-admin]{lang="EN-US"}[、]{style="font-family:宋体"}[mdc-operator]{lang="EN-US"}[、]{style="font-family:宋体"}[context-admin]{lang="EN-US"}[、]{style="font-family:宋体"}[context-operator]{lang="EN-US"}[、]{style="font-family:宋体"}[level-15]{lang="EN-US"}[、]{style="font-family:宋体"}[security-audit]{lang="EN-US"}[这些用户角色内定义的所有权限均不能被修改；用户角色]{style="font-family:宋体"}[level-0]{lang="EN-US"}[～]{style="font-family:宋体"}[level-14]{lang="EN-US"}[可以通过自定义规则和资源控制策略调整自身的权限，但这种修改对于]{style="font-family:宋体"}**[display history-command all]{lang="EN-US"}**[命令不生效，即不能通过添加对应的规则来更改它的缺省执行权限。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x2054777581}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_2032131399}[创建用户角色]{style="font-family:宋体"}[role1]{lang="EN-US"}[，并进入用户角色视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1979_37509_729256869}

[\[Sysname\] role name role1]{lang="EN-US"}

[\[Sysname-role-role1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1603233355}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}]{.ItemStepChar}[**[display role]{lang="EN-US"}**]{.ItemStepChar}]{#struct_0_x1979_37509_406301495}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[interface policy deny]{lang="EN-US"}**]{#struct_0_x1979_37509_x1884024526}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rule]{lang="EN-US"}**]{#struct_0_x1979_37509_x1028393346}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vlan policy deny]{lang="EN-US"}**]{#struct_0_x1979_37509_1848332809}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vpn-instance policy deny]{lang="EN-US"}**]{#struct_0_x1979_37509_x2054777582}
:::

::: {#-1270710712 .myid}
[]{#_Toc404782253}[]{#struct_0_x1979_37509_1628846872}[]{#_Toc285213506}

**RBAC \-- RBAC配置命令 \-- role default-role enable**

------------------------------------------------------------------------

[**[role default-role enable]{lang="EN-US"}**]{#struct_0_x1979_37509_520767912}[命令用来使能缺省用户角色授权功能。]{style="font-family:
宋体"}

[**[undo role default-role enable]{lang="EN-US"}**]{#struct_0_x1979_37509_1640312093}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_1591761593}

[**[role default-role enable]{lang="EN-US"}**]{#struct_0_x1979_37509_2077418423}

[**[undo role default-role enable]{lang="EN-US"}**]{#struct_0_x1979_37509_376144948}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1979_37509_349772680}

[[缺省用户角色授权功能处于关闭状态，没有被]{style="font-family:宋体"}[AAA]{lang="EN-US"}]{#struct_0_x1979_37509_x1290651260}[授权用户角色的用户不能登录设备。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x2054777583}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1979_37509_x1100036483}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x115452092}

[[network-admin]{lang="EN-US"}]{#struct_0_x1979_37509_690612590}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1979_37509_2119847179}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1178637250}

[[对于通过]{style="font-family:宋体"}[AAA]{lang="EN-US"}]{#struct_0_x1979_37509_x1111545058}[认证登录设备的用户，由]{style="font-family:宋体"}[AAA]{lang="EN-US"}[服务器（远程认证）或设备（本地认证）为其授权对应的用户角色。如果用户没有被授权任何用户角色，将无法成功登录设备。使能该功能后，用户将在没有被授权任何用户角色的情况下，具有一个缺省的用户角色，具体情况如下：（不同设备的具体情况有所不同，请以设备的实际情况为准）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果用户登录设备，缺省用户角色为]{lang="EN-US" style="font-family:宋体"}[network-operator]{lang="EN-US"}]{#struct_0_x1979_37509_x464248385}[；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果用户登录于缺省]{lang="EN-US" style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_x1979_37509_x2054777584}[，则缺省用户角色为]{lang="EN-US" style="font-family:宋体"}[network-operator]{lang="EN-US"}[；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果用户登录于非缺省]{lang="EN-US" style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_x1979_37509_x1503321010}[，则缺省用户角色为]{lang="EN-US" style="font-family:宋体"}[mdc-operator]{lang="EN-US"}[；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果用户登录于缺省]{lang="EN-US" style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_x1979_37509_2005192806}[，则缺省用户角色为]{lang="EN-US" style="font-family:宋体"}[context]{lang="EN-US"}[-operator]{lang="EN-US"}[；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果用户登录于非缺省]{lang="EN-US" style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_x1979_37509_2005258342}[，则缺省用户角色为]{lang="EN-US" style="font-family:宋体"}[context]{lang="EN-US"}[-operator]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[若用户通过]{style="font-family:宋体"}[AAA]{lang="EN-US"}]{#struct_0_x1979_37509_x1607158717}[认证且被授予了具体的用户角色，则用户不具有以上缺省的用户角色。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1979_37509_1144763995}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_1587072723}[使能缺省用户角色授权功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1979_37509_x1541173699}

[\[Sysname\] role default-role enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_332391217}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[role]{lang="EN-US"}**]{#struct_0_x1979_37509_x1309666444}
:::

::: {#-1927973318 .myid}
[]{#_Toc404782254}[]{#struct_0_x1979_37509_2024264675}[]{#_Toc285213507}

**RBAC \-- RBAC配置命令 \-- role feature-group**

------------------------------------------------------------------------

[**[role feature-group]{lang="EN-US"}**]{#struct_0_x1979_37509_x2054777585}[命令用来创建特性组并进入特性组视图。]{style="font-family:宋体"}

[**[undo role feature-group]{lang="EN-US"}**]{#struct_0_x1979_37509_62762931}[命令用来删除指定的特性组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_1080203518}

[**[role feature-group name ]{lang="EN-US"}***[feature-group-name]{lang="EN-US"}*]{#struct_0_x1979_37509_853345048}

[**[undo role feature-group name ]{lang="EN-US"}***[feature-group-name]{lang="EN-US"}*]{#struct_0_x1979_37509_1800744503}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x452135435}

[[存在两个特性组，名称分别为]{style="font-family:宋体"}[L2]{lang="EN-US"}]{#struct_0_x1979_37509_x1354585346}[和]{style="font-family:宋体"}[L3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x74784742}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1979_37509_x1696740660}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x2054777586}

[[network-admin]{lang="EN-US"}]{#struct_0_x1979_37509_x340521596}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1979_37509_x1459452461}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1979_37509_1757989679}

[**[name ]{lang="EN-US"}***[feature-group-name]{lang="EN-US"}*]{#struct_0_x1979_37509_1935365163}[：特性组名称，]{style="font-family:宋体"}*[feature-group-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1020867019}

[[除系统预定义的特性组]{style="font-family:宋体"}[L2]{lang="EN-US"}]{#struct_0_x1979_37509_1622466018}[和]{style="font-family:宋体"}[L3]{lang="EN-US"}[之外，系统中最多允许创建]{style="font-family:宋体"}[64]{lang="EN-US"}[个特性组。]{style="font-family:宋体"}

[[不能修改和删除系统预定义的特性组]{style="font-family:宋体"}[L2]{lang="EN-US"}]{#struct_0_x1979_37509_x2138551770}[和]{style="font-family:宋体"}[L3]{lang="EN-US"}[。]{style="font-family:宋体"}[L2]{lang="EN-US"}[中包含了所有的二层协议相关功能的命令，]{style="font-family:宋体"}[L3]{lang="EN-US"}[中包含了所有三层协议相关功能的命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x2054777587}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_1225562345}[创建特性组]{style="font-family:宋体"}[security-features]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1979_37509_x449110929}

[\[Sysname\] role feature-group name security-features]{lang="EN-US"}

[\[Sysname-featuregrp-security-features\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x21950263}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display role feature]{lang="EN-US"}**]{#struct_0_x1979_37509_1252911431}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display role feature-group]{lang="EN-US"}**]{#struct_0_x1979_37509_1118351182}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[feature]{lang="EN-US"}**]{#struct_0_x1979_37509_1545048229}
:::

::: {#1629595628 .myid}
[]{#_Toc404782255}[]{#struct_0_x1979_37509_460974255}[]{#_Toc285213508}

**RBAC \-- RBAC配置命令 \-- rule**

------------------------------------------------------------------------

[**[rule]{lang="EN-US"}**]{#struct_0_x1979_37509_x2054777588}[命令用来为用户角色创建一条规则。]{style="font-family:宋体"}

[**[undo rule]{lang="EN-US"}**]{#struct_0_x1979_37509_109817098}[命令用来为用户角色删除一条规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x21735290}

[**[rule]{lang="EN-US"}**[ *number* { **deny** \| **permit** } { **command** *command-string \|* { **execute** \| **read** \| **write** } \* { **feature** \[ *feature-name* \] \| **feature-group** *feature-group-name* \| ]{lang="EN-US"}]{#struct_0_x1979_37509_221374726}**[oid]{lang="EN-US"}**[ \[ *oid-string* \] ]{lang="EN-US"}[\| **web-menu** \[ *web-string* \] \| **xml-element** \[ *xml-string* \] } }]{lang="EN-US"}

[**[undo rule]{lang="EN-US"}**[ { *number* \| **all** }]{lang="EN-US"}]{#struct_0_x1979_37509_x292655834}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1979_37509_1494189109}

[[新创建的用户角色中未定义规则，即当前用户角色无任何权限。]{style="font-family:宋体"}]{#struct_0_x1979_37509_x1502789861}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1979_37509_752038531}

[[用户角色视图]{style="font-family:宋体"}]{#struct_0_x1979_37509_1016118310}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1979_37509_283874581}

[[network-admin]{lang="EN-US"}]{#struct_0_x1979_37509_x1157578381}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1979_37509_929283909}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1979_37509_356015553}

[*[number]{lang="EN-US"}*]{#struct_0_x1979_37509_449155630}[：权限规则编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[deny]{lang="EN-US"}**]{#struct_0_x1979_37509_x1269551869}[：禁止执行指定的命令。]{style="font-family:宋体"}

[**[permit]{lang="EN-US"}**]{#struct_0_x1979_37509_x1181785763}[：允许执行指定的命令。]{style="font-family:宋体"}

[**[command ]{lang="EN-US"}***[command-string]{lang="EN-US"}*]{#struct_0_x1979_37509_x470257181}[：配置基于命令的规则。]{style="font-family:宋体"}*[command-string]{lang="EN-US"}*[表示命令特征字符串，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[个字符的字符串，区分大小写，可以是特定的一条命令行，也可以是用星号（]{style="font-family:宋体"}[\*]{lang="EN-US"}[）通配符表示的一批命令，可包含空格、]{style="font-family:宋体"}[Tab]{lang="EN-US"}[（它们用于分隔关键字、参数以及输入的字符），以及所有可打印字符。]{style="font-family:宋体"}

[**[execute]{lang="EN-US"}**]{#struct_0_x1979_37509_x1564063524}[：表示执行类型的命令，即]{style="font-family:宋体"}[用于执行特定的程序或功能]{style="font-family:宋体"}[的一类命令，如]{style="font-family:宋体"}**[ping]{lang="EN-US"}**[命令。]{style="font-family:宋体"}

[**[read]{lang="EN-US"}**]{#struct_0_x1979_37509_283874580}[：表示读类型的命令，即显示系统配置和维护信息的一类命令，如]{style="font-family:宋体"}**[display]{lang="EN-US"}**[、]{style="font-family:宋体"}**[dir]{lang="EN-US"}**[、]{style="font-family:宋体"}**[more]{lang="EN-US"}**[和]{style="font-family:宋体"}**[pwd]{lang="EN-US"}**[命令。]{style="font-family:宋体"}

[**[write]{lang="EN-US"}**]{#struct_0_x1979_37509_x1157578380}[：表示写类型的命令，即用于对系统进行配置的一类命令，如]{style="font-family:宋体"}**[ssh server enable]{lang="EN-US"}**[命令。]{style="font-family:宋体"}

[**[feature ]{lang="EN-US"}**[\[ *feature-name* \]]{lang="EN-US"}]{#struct_0_x1979_37509_x1799599446}[：配置基于特性的规则。]{style="font-family:宋体"}*[feature-name]{lang="EN-US"}*[表示系统预定义的特性名称，区分大小写。若不指定特性名称，则表示所有特性。]{style="font-family:宋体"}

[**[feature-group]{lang="EN-US"}**[ *feature-group-name*]{lang="EN-US"}]{#struct_0_x1979_37509_955030484}[：配置基于特性组的规则。]{style="font-family:宋体"}*[feature-group-name]{lang="EN-US"}*[表示特性组名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[oid ]{lang="EN-US"}**]{#struct_0_x1979_37509_2004602981}[\[*oid-string* \]]{lang="EN-US"}[：配置基]{style="font-family:宋体"}[于]{style="font-family:宋体"}[MIB]{lang="EN-US"}[节点]{style="font-family:宋体"}[OID]{lang="EN-US"}[（]{style="font-family:宋体"}[Object Identifier]{lang="EN-US"}[，对象标识符）]{style="font-family:宋体"}[的规]{style="font-family:宋体"}[则。]{style="font-family:宋体"}*[oid-string]{lang="EN-US"}*[表示允许操作的]{style="font-family:宋体"}[OID]{lang="EN-US"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，不区分大小写。例如：]{style="font-family:宋体"}[1.3.6.1.4.1.25506.8.35.14.19.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[web-menu]{lang="EN-US"}**[ \[ *web-string* \]]{lang="EN-US"}]{#struct_0_x1979_37509_135491795}[：配置基于]{style="font-family:宋体"}[Web]{lang="EN-US"}[菜单的规则。]{style="font-family:宋体"}*[web-string]{lang="EN-US"}*[表示允许操作的]{style="font-family:宋体"}[Web]{lang="EN-US"}[菜单选项的]{style="font-family:宋体"}[ID]{lang="EN-US"}[路径，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，不区分大小写，以"]{style="font-family:宋体"}[/]{lang="EN-US"}["为分隔符来分隔不同级别的菜单。]{style="font-family:宋体"}[合法的]{style="font-family:宋体"}*[web-string]{lang="EN-US"}*[为通过]{style="font-family:宋体"}**[display web menu]{lang="EN-US"}**[命令显示的]{style="font-family:宋体"}[ID]{lang="EN-US"}[路径]{style="font-family:宋体"}[,]{lang="EN-US"}[例如：]{style="font-family:宋体"}[M_DEVICE/I_BASIC_INFO/I_reboot]{lang="EN-US"}[；]{style="font-family:宋体"}[若不指定]{style="font-family:宋体"}*[web-string]{lang="EN-US"}*[参数，则表示]{style="font-family:宋体"}[对所有菜单选项生效。]{style="font-family:宋体"}

[**[xml-element ]{lang="EN-US"}**[\[ *xml-string* \]]{lang="EN-US"}]{#struct_0_x1979_37509_x741411918}[：]{style="font-family:宋体"}[配置基于]{style="font-family:宋体"}[XML]{lang="EN-US"}[元素的规则。]{style="font-family:宋体"}*[xml-string]{lang="EN-US"}*[表示允许操作的]{style="font-family:宋体"}[XML]{lang="EN-US"}[元素的]{style="font-family:宋体"}[XPath]{lang="EN-US"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，不区分大小写，以"]{style="font-family:宋体"}[/]{lang="EN-US"}["为分隔符来分隔不同级别的菜单，例如：]{style="font-family:宋体"}[Interfaces/Index/Name]{lang="EN-US"}[；若不指定]{style="font-family:宋体"}*[xml-string]{lang="EN-US"}*[参数]{style="font-family:宋体"}[，则表示对]{style="font-family:宋体"}[所有]{style="font-family:宋体"}[XML]{lang="EN-US"}[元素生效。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x1979_37509_x2109045271}[：指定所有权限规则。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1961608168}

[[可为一个用户角色定义以下几种类型的规则：]{style="font-family:宋体"}]{#struct_0_x1979_37509_x2044857065}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[禁止或允许执行特定的命令行。]{style="font-family:宋体"}]{#struct_0_x1979_37509_283874579}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[禁止或允许执行指定或所有特性的某一类或某几类命令。]{style="font-family:宋体"}]{#struct_0_x1979_37509_x1495285397}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[禁止或允许执行某个特性组中所有特性的某一类或某几类命令。]{style="font-family:宋体"}]{#struct_0_x1979_37509_1848442078}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[禁止或允许执行指定所有或指定的]{style="font-family:宋体"}]{#struct_0_x1979_37509_330043416}[MIB]{lang="EN-US"}[节点]{style="font-family:宋体"}[OID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[禁止或允许执行]{style="font-family:宋体"}]{#struct_0_x1979_37509_x383100391}[Web]{lang="EN-US"}[页面中所有菜单选项或某几类菜单选项。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[禁止或允许执行所有]{style="font-family:宋体"}]{#struct_0_x1979_37509_x12893088}[XML]{lang="EN-US"}[元素或某几类]{style="font-family:宋体"}[XML]{lang="EN-US"}[元素。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1979_37509_1892221381}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[[执行本命令时，如果指定编号的规则不存在，则表示创建一条新的规则；如果指定编号的规则已存在，则表示对已有的规则进行修改。]{style="font-family:宋体"}]{.ItemStepChar}]{#struct_0_x1979_37509_x231283636}[修改后的规则对于当前已经在线的用户不生效，对于之后使用该角色登录设备的用户生效。]{style="font-family:宋体"}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}]{.ItemStepChar}[一个用户角色中允许创建多条规则，各规则以创建时指定的编号为唯一标识，被授权该角色的用户可以执行的命令为这些规则定义的可执行命令的并集。若这些规则定义的权限内容有冲突，则规则编号大的有效。例如，规则]{style="font-family:宋体"}]{#struct_0_x1979_37509_x847882615}[1]{lang="EN-US"}[允许执行命令]{style="font-family:宋体"}[A]{lang="EN-US"}[，规则]{style="font-family:宋体"}[2]{lang="EN-US"}[允许执行命令]{style="font-family:宋体"}[B]{lang="EN-US"}[，规则]{style="font-family:宋体"}[3]{lang="EN-US"}[禁止执行命令]{style="font-family:宋体"}[A]{lang="EN-US"}[，则最终规则]{style="font-family:宋体"}[2]{lang="EN-US"}[和规则]{style="font-family:宋体"}[3]{lang="EN-US"}[生效，即禁止执行命令]{style="font-family:宋体"}[A]{lang="EN-US"}[，允许执行命令]{style="font-family:宋体"}[B]{lang="EN-US"}[[。]{style="font-family:宋体"}]{.ItemStepChar}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}]{.ItemStepChar}[[在同时存在系统预定义规则（以]{style="font-family:宋体"}]{.ItemStepChar}]{#struct_0_x1979_37509_x2062299667}[[sys-x]{lang="EN-US"}]{.ItemStepChar}[[为权限规则编号，]{style="font-family:宋体"}]{.ItemStepChar}[[x]{lang="EN-US"}]{.ItemStepChar}[[为整数值）和自定义规则的用户角色中，若预定义规则定义的权限内容与自定义规则定义的权限内容有冲突，则以自定义规则为准。]{style="font-family:宋体"}]{.ItemStepChar}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每个用户角色中最多可以配置]{style="font-family:宋体"}]{#struct_0_x1979_37509_x1319622501}[256]{lang="EN-US"}[条规则，系统中可以配置的用户角色规则总数不能超过]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[访问文件系统的命令，受基于文件系统特性规则以及具体命令规则的双重控制。]{style="font-family:宋体"}]{#struct_0_x1979_37509_283874578}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于需要将输出信息重定向到文件中保存的命令，只有在用户角色被授权了文件系统写权限后才允许执行。]{style="font-family:宋体"}]{#struct_0_x1979_37509_x1495285396}

[[输入命令特征字符串时，需要遵循以下规则：]{style="font-family:宋体"}]{#struct_0_x1979_37509_282358137}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[段（]{lang="EN-US" style="font-family:宋体"}[segment]{lang="EN-US"}]{#struct_0_x1979_37509_747805726}[）的划分]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若要描述多级视图下的命令，则需要使用分号（]{style="font-family:宋体"}]{#struct_0_x1979_37509_1412326026}[;]{lang="EN-US"}[）将命令特征字符串分成多个段，每一个段代表一个或一系列命令，后一个段中的命令是执行前一个段中命令所进入视图下的命令。一个段中可以包含多个星号（]{style="font-family:宋体"}[\*]{lang="EN-US"}[），每个星号（]{style="font-family:宋体"}[\*]{lang="EN-US"}[）代表了]{style="font-family:宋体"}[0]{lang="EN-US"}[个或多个任意字符。]{style="font-family:宋体"}[例如：命令特征字符串"]{lang="EN-US" style="font-family:
宋体"}[system ; interface \* ; ip \* ;]{lang="EN-US"}["]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}[代表从系统视图进入到任意接口视图后，以]{lang="EN-US" style="font-family:宋体"}**[ip]{lang="EN-US"}**[开头的所有命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[除最后一个段外，其余段中的命令应为描述如何进入子视图的命令特征字符串。]{style="font-family:宋体"}]{#struct_0_x1979_37509_1899163264}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个段中必须至少出现一个可打印字符，不能全部为空格或]{style="font-family:宋体"}]{#struct_0_x1979_37509_283874577}[Tab]{lang="EN-US"}[。]{style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分号的使用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1979_37509_x1495285383}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在输入命令特征字符串时必须指定该命令所在的视图，进入各视图的命令特征字符串由分号分隔。但是，对于能在任意视图下执行的命令（例如]{style="font-family:宋体"}]{#struct_0_x1979_37509_x477222286}**[display]{lang="EN-US"}**[命令）以及用户视图下的命令（例如]{style="font-family:宋体"}**[dir]{lang="EN-US"}**[命令），在配置包含此类命令的规则时，不需要在规则的命令匹配字符串中指定其所在的视图。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当最后一个段中的最后一个可见字符为分号时，表示所指的命令范围不再扩展，否则将向子视图中的命令扩展。例如：命令特征字符串"]{style="font-family:宋体"}]{#struct_0_x1979_37509_1989405451}[system ; radius scheme \* ;]{lang="EN-US"}["代表系统视图下以]{style="font-family:宋体"}**[radius scheme]{lang="EN-US"}**[开头的所有命令；命令特征字符串"]{style="font-family:宋体"}[system ; radius scheme \* ]{lang="EN-US"}["代表系统视图下以]{style="font-family:宋体"}**[radius scheme]{lang="EN-US"}**[开头的所有命令，以及进入子视图（]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案视图）下的所有命令。]{style="font-family:宋体"}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[星号的使用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1979_37509_179813872}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当星号（]{style="font-family:宋体"}]{#struct_0_x1979_37509_606974903}[\*]{lang="EN-US"}[）出现在一个段的首部时，其后面不能再出现其它可打印字符，且该段必须是命令特征字符串的最后一个段。]{style="font-family:宋体"}[例如：命令特征字符串"]{lang="EN-US" style="font-family:宋体"}[system ; \*]{lang="EN-US"}["就代表了系统视图下的所有命令，以及所有子视图下的命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当星号（]{style="font-family:宋体"}]{#struct_0_x1979_37509_x1141111548}[\*]{lang="EN-US"}[）出现在一个段的中间时，该段必须是命令特征字符串的最后一个段。]{style="font-family:宋体"}[例如：命令特征字符串"]{lang="EN-US" style="font-family:宋体"}[debugging \* event]{lang="EN-US"}["就代表了用户视图下所有模块的事件调试信息开关命令。]{lang="EN-US" style="font-family:宋体"}

[[(4)[      ]{style="font:7.0pt "}]{lang="EN-US"}[前缀匹配]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1979_37509_x894014907}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[命令关键字与命令特征字符串是采用前缀匹配算法进行匹配的，即只要命令行中关键字的首部若干连续字符或全部字符与规则中定义的关键字相匹配，就认为该命令行与此规则匹配。因此，命令特征字符串中可以包括完整的或部分的命令关键字。例如，若规则"]{style="font-family:宋体"}]{#struct_0_x1979_37509_x1105004627}[rule 1 deny command dis mpls lsp protocol static asbr]{lang="EN-US"}["生效，则命令]{style="font-family:宋体"}**[display mpls lsp protocol static asbr]{lang="EN-US"}**[和命令]{style="font-family:宋体"}**[display mpls lsp protocol static-cr asbr]{lang="EN-US"}**[都会被禁止执行。]{style="font-family:宋体"}

[[对于基于命令的规则，有以下使用注意事项：]{style="font-family:宋体"}]{#struct_0_x1979_37509_283874576}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[基于命令的规则只对指定视图下的命令生效。若用户输入的命令在当前视图下不存在而在其父视图下被查找到时，用于控制当前视图下的命令的规则不会对其父视图下的命令执行权限进行控制。例如，定义一条规则"]{style="font-family:宋体"}]{#struct_0_x1979_37509_x1495285382}[rule 1 deny command system ; interface \* ; \*]{lang="EN-US"}["禁止用户执行接口视图下的任何命令。当用户在接口视图下输入命令]{style="font-family:宋体"}**[acl number ]{lang="EN-US"}**[3000]{lang="EN-US"}[时，该命令仍然可以成功执行，因为系统在接口视图下搜索不到指定的]{style="font-family:宋体"}**[acl]{lang="EN-US"}**[命令时，会回溯到系统视图（父视图）下执行，此时该规则对此命令不生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**]{#struct_0_x1979_37509_x2043306227}[命令中的重定向符（"]{style="font-family:
宋体"}[\|]{lang="EN-US"}["、"]{style="font-family:宋体"}[\>]{lang="EN-US"}["、"]{style="font-family:宋体"}[\>\>]{lang="EN-US"}["）及其后面的关键字不被作为命令行关键字参与规则的匹配。例如，若规则"]{style="font-family:宋体"}[rule 1 permit command display debugging]{lang="EN-US"}["生效，则命令]{style="font-family:宋体"}**[display debugging \> log]{lang="EN-US"}**[是被允许执行的，其中的关键字]{style="font-family:宋体"}**[\> log]{lang="EN-US"}**[将被忽略，]{style="font-family:宋体"}[RBAC]{lang="EN-US"}[只对重定向符前面的命令行]{style="font-family:宋体"}**[display debugging]{lang="EN-US"}**[进行匹配。但是，如果在规则中配置了重定向符，则]{style="font-family:宋体"}[RBAC]{lang="EN-US"}[会将其作为普通字符处理。例如，若规则"]{style="font-family:宋体"}[rule 1 permit command display debugging \> log]{lang="EN-US"}["生效，则命令]{style="font-family:宋体"}**[display debugging \> log]{lang="EN-US"}**[将会匹配失败，因为其中的关键字]{style="font-family:宋体"}**[\> log]{lang="EN-US"}**[被]{style="font-family:宋体"}[RBAC]{lang="EN-US"}[忽略了，最终是命令]{style="font-family:宋体"}**[display debugging]{lang="EN-US"}**[与规则进行匹配。因此，]{style="font-family:宋体"}[配置规则时不要使用重定向符。]{lang="EN-US" style="font-family:宋体"}

[[进行基于]{style="font-family:宋体"}]{#struct_0_x1979_37509_2004799589}[OID]{lang="EN-US"}[的规则的匹配时，遵循以下规则：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[与用户访问的]{style="font-family:宋体"}]{#struct_0_x1979_37509_1864839349}[OID]{lang="EN-US"}[形成最长匹配的规则生效。例如用户访问的]{style="font-family:宋体"}[OID]{lang="EN-US"}[为]{style="font-family:宋体"}[1.3.6.1.4.1.25506.141.3.0.1]{lang="EN-US"}[，角色中存在"]{style="font-family:宋体"}[rule 1 permit read write oid 1.3.6]{lang="EN-US"}["，"]{style="font-family:宋体"}[rule 2 deny read write oid 1.3.6.1.4.1]{lang="EN-US"}["和"]{style="font-family:宋体"}[rule 3 permit read write oid 1.3.6.1.4]{lang="EN-US"}["，其中]{style="font-family:
宋体"}[rule 2]{lang="EN-US"}[与用户访问的]{style="font-family:宋体"}[OID]{lang="EN-US"}[形成最长匹配，则认为]{style="font-family:宋体"}[rule 2]{lang="EN-US"}[与]{style="font-family:宋体"}[OID]{lang="EN-US"}[匹配，匹配的结果为用户的此访问请求被拒绝。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于定义的]{style="font-family:宋体"}]{#struct_0_x1979_37509_x324787573}[OID]{lang="EN-US"}[长度相同的规则，规则编号大的生效。例如用户访问的]{style="font-family:宋体"}[OID]{lang="EN-US"}[为]{style="font-family:宋体"}[1.3.6.1.4.1.25506.141.3.0.1]{lang="EN-US"}[，角色中存在"]{style="font-family:宋体"}[rule 1 permit read write oid 1.3.6]{lang="EN-US"}["，"]{style="font-family:宋体"}[rule 2 deny read write oid 1.3.6.1.4.1]{lang="EN-US"}["和"]{style="font-family:宋体"}[rule 3 permit read write oid 1.3.6.1.4.1]{lang="EN-US"}["，其中]{style="font-family:宋体"}[rule 2]{lang="EN-US"}[和]{style="font-family:宋体"}[rule 3]{lang="EN-US"}[与访问的]{style="font-family:宋体"}[OID]{lang="EN-US"}[形成最长匹配，则]{style="font-family:宋体"}[rule 3]{lang="EN-US"}[生效，匹配的结果为用户的访问请求被允许。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1979_37509_317603939}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_139989785}[为用户角色]{style="font-family:宋体"}[role1]{lang="EN-US"}[创建一条规则，允许用户执行命令]{style="font-family:宋体"}**[display acl]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1979_37509_791333955}

[\[Sysname\] role name role1]{lang="EN-US"}

[\[Sysname-role-role1\] rule 1 permit command display acl]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_x1845355648}[为用户角色]{style="font-family:宋体"}[role1]{lang="EN-US"}[添加一条权限规则，允许用户执行所有以]{style="font-family:宋体"}**[display]{lang="EN-US"}**[开头的命令。]{style="font-family:宋体"}

[[\[Sysname-role-role1\] rule 2 permit command display \*]{lang="EN-US"}]{#struct_0_x1979_37509_1776758717}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_283874575}[为用户角色]{style="font-family:宋体"}[role1]{lang="EN-US"}[添加一条权限规则，允许用户执行系统视图下的]{style="font-family:宋体"}**[radius scheme aaa]{lang="EN-US"}**[命令，以及使用该命令进入子视图后的所有命令。]{style="font-family:宋体"}

[[\[Sysname-role-role1\] rule 3 permit command system ; radius scheme aaa]{lang="EN-US"}]{#struct_0_x1979_37509_x1495285385}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_685577128}[为用户角色]{style="font-family:宋体"}[role1]{lang="EN-US"}[添加一条权限规则，禁止用户执行所有特性中读类型和写类型的命令。]{style="font-family:宋体"}

[[\[Sysname-role-role1\] rule 4 deny read write feature]{lang="EN-US"}]{#struct_0_x1979_37509_x345337374}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_1425132013}[为用户角色]{style="font-family:宋体"}[role1]{lang="EN-US"}[添加一条权限规则，禁止用户执行特性]{style="font-family:宋体"}[aaa]{lang="EN-US"}[中所有读类型的命令。]{style="font-family:宋体"}

[[\[Sysname-role-role1\] rule 5 deny read feature aaa]{lang="EN-US"}]{#struct_0_x1979_37509_1362697464}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_x341343295}[为用户角色]{style="font-family:宋体"}[role1]{lang="EN-US"}[添加一条权限规则，允许执行特性组]{style="font-family:宋体"}[security-features]{lang="EN-US"}[中所有特性的读类型、写类型以及执行类型的命令。]{style="font-family:宋体"}

[[\[Sysname-role-role1\] rule 6 permit read write execute feature-group security-features]{lang="EN-US"}]{#struct_0_x1979_37509_1278254171}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_2005192805}[为用户角色]{style="font-family:宋体"}[role1]{lang="EN-US"}[添加一条基于]{style="font-family:宋体"}[OID]{lang="EN-US"}[的规则，允许对]{style="font-family:宋体"}[OID]{lang="EN-US"}[为]{style="font-family:宋体"}[1.1.2]{lang="EN-US"}[的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[节点进行读、写操作。]{style="font-family:宋体"}

[[\[Sysname-role-role1\] rule 7 permit read write oid 1.1.2]{lang="EN-US"}]{#struct_0_x1979_37509_x1937560110}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_1528891318}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}]{.ItemStepChar}[**[display role]{lang="EN-US"}**]{.ItemStepChar}]{#struct_0_x1979_37509_283874574}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}]{.ItemStepChar}[**[display role feature]{lang="EN-US"}**]{.ItemStepChar}]{#struct_0_x1979_37509_x1495285384}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}]{.ItemStepChar}[**[display role feature-group]{lang="EN-US"}**]{.ItemStepChar}]{#struct_0_x1979_37509_x880506813}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display web menu]{lang="EN-US"}**]{#struct_0_x1979_37509_2137468418}[(]{lang="EN-US"}[基础配置命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[登录设备]{style="font-family:宋体"}[)]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[role]{lang="EN-US"}**]{#struct_0_x1979_37509_1440460279}
:::

::: {#2074012427 .myid}
[]{#_Toc285213509}[]{#_Toc404782256}[]{#struct_0_x1979_37509_x1774173361}[]{#_Toc320537173}[]{#_Toc320518508}[]{#_Toc300678539}

**RBAC \-- RBAC配置命令 \-- super**

------------------------------------------------------------------------

[**[super]{lang="EN-US"}**]{#struct_0_x1979_37509_640186318}[命令用来]{style="font-family:宋体"}[使用户从当前角色切换到指定的用户角色]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x818310454}

[**[super ]{lang="EN-US"}**[\[ *rolename* \]]{lang="EN-US"}]{#struct_0_x1979_37509_283874573}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1495285387}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1979_37509_1848376542}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1132296109}

[[network-admin]{lang="EN-US"}]{#struct_0_x1979_37509_x1437537355}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1979_37509_2115969521}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x2082592874}

[*[rolename]{lang="EN-US"}*]{#struct_0_x1979_37509_x1801111024}[：待切换的用户角色名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写，可以是系统中已存在的任意用户角色。若不指定本参数，则表示要从当前用户角色切换到用户角色]{style="font-family:宋体"}[network-admin]{lang="EN-US"}[。（不支持]{style="font-family:宋体"}[MDC]{lang="EN-US"}[、]{style="font-family:宋体"}[Context]{lang="EN-US"}[的设备）。若不指定本参数，则切换到当前缺省的目的用户角色。缺省的目的用户角色由]{style="font-family:宋体"}**[super default role]{lang="EN-US"}**[命令指定。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1979_37509_283874572}

[[为了保证操作的安全性，通常用户进行用户角色切换时，均需要输入用户角色切换密码。切换到不同的用户角色时，需要输入相应切换密码。如果服务器没有响应或者没有配置用户角色切换密码，则切换操作失败，若还有备份认证方案，则转而进行备份认证。因此，在进行切换操作前，请先保证配置了正确的用户角色切换密码。]{style="font-family:宋体"}]{#struct_0_x1979_37509_x1495285386}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1979_37509_x2061971987}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若级别切换认证方式为]{style="font-family:宋体"}]{#struct_0_x1979_37509_1893570652}**[local]{lang="EN-US"}**[，在设备上未配置切换密码的情况下，对于]{style="font-family:宋体"}[Console/AUX]{lang="EN-US"}[用户，设备不关心用户是否输入切换密码以及输入切换密码的内容，可允许用户成功切换用户角色。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若级别切换认证方式为]{style="font-family:宋体"}]{#struct_0_x1979_37509_942692359}**[local scheme]{lang="EN-US"}**[，在设备上未配置切换密码的情况下，对于]{style="font-family:宋体"}[Console]{lang="EN-US"}[、]{style="font-family:宋体"}[TTY]{lang="EN-US"}[或]{style="font-family:宋体"}[VTY]{lang="EN-US"}[用户，则转为远程]{style="font-family:宋体"}[AAA]{lang="EN-US"}[认证；对于]{style="font-family:宋体"}[AUX]{lang="EN-US"}[用户，设备不关心用户是否输入切换密码以及输入切换密码的内容，可允许用户成功切换用户角色。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1979_37509_282292601}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_x1228522273}[将用户角色切换到]{style="font-family:宋体"}[network-operator]{lang="EN-US"}[。（假设用户当前的角色为]{style="font-family:宋体"}[network-admin]{lang="EN-US"}[，切换认证方式为]{style="font-family:宋体"}[local]{lang="EN-US"}[，切换密码已经设置）]{style="font-family:宋体"}

[[\<Sysname\> super network-operator]{lang="EN-US"}]{#struct_0_x1979_37509_1302606432}

[Password:]{lang="EN-US"}

[User privilege role is network-operator, and only those commands can be used that authorized to the role.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x231928613}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication super]{lang="EN-US"}**]{#struct_0_x1979_37509_1095469009}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/AAA]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[super authentication-mode]{lang="EN-US"}**]{#struct_0_x1979_37509_x1672440555}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[super password]{lang="EN-US"}**]{#struct_0_x1979_37509_1176199100}
:::

::: {#-1307615536 .myid}
[]{#_Toc404782257}[]{#struct_0_x1979_37509_x265020555}[]{#_Toc320537174}[]{#_Toc320518509}[]{#_Toc300678540}

**RBAC \-- RBAC配置命令 \-- super authentication-mode**

------------------------------------------------------------------------

[**[super authentication-mode]{lang="EN-US"}**]{#struct_0_x1979_37509_x1785061285}[命令用来设置切换用户角色时使用的认证方式]{style="font-family:
宋体"}[。]{style="font-family:宋体"}

[**[undo super authentication-mode]{lang="EN-US"}**]{#struct_0_x1979_37509_574882872}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_1193727555}

[**[super authentication-mode ]{lang="EN-US"}**[{ **local** \| **scheme** } \*]{lang="EN-US"}]{#struct_0_x1979_37509_1018809580}

[**[undo super authentication-mode]{lang="EN-US"}**]{#struct_0_x1979_37509_1361261666}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1979_37509_1390069931}

[[采用]{style="font-family:宋体"}**[local]{lang="EN-US"}**]{#struct_0_x1979_37509_x1672440556}[认证方式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x389884841}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1979_37509_x910551082}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1689100821}

[[network-admin]{lang="EN-US"}]{#struct_0_x1979_37509_x1999219065}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1979_37509_1363259513}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1979_37509_107619280}

[**[local]{lang="EN-US"}**]{#struct_0_x1979_37509_330047006}[：使用本地配置的用户角色切换密码进行认证。]{style="font-family:宋体"}

[**[scheme]{lang="EN-US"}**]{#struct_0_x1979_37509_x898950162}[：使用]{style="font-family:宋体"}[AAA]{lang="EN-US"}[配置进行认证。该方式下，]{style="font-family:宋体"}[设备将用户角色切换时使用的用户名和密码发送给]{style="font-family:宋体"}[HWTACACS/RADIUS]{lang="EN-US"}[服务器进行远程验证。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1672440557}

[[用户可以选择使用]{style="font-family:宋体"}**[local]{lang="EN-US"}**]{#struct_0_x1979_37509_x1955968782}[或者]{style="font-family:宋体"}**[scheme]{lang="EN-US"}**[方式认证，也可以同时选择]{style="font-family:宋体"}**[local]{lang="EN-US"}**[和]{style="font-family:宋体"}**[scheme]{lang="EN-US"}**[方式，多选时根据配置顺序依次认证，例如]{style="font-family:宋体"}**[scheme local]{lang="EN-US"}**[方式，会先进行]{style="font-family:宋体"}**[scheme]{lang="EN-US"}**[方式认证，如果认证服务器没有响应，则转为采用]{style="font-family:宋体"}**[local]{lang="EN-US"}**[方式认证。]{style="font-family:宋体"}**[scheme]{lang="EN-US"}**[认证方式需要与]{style="font-family:宋体"}[AAA ]{lang="EN-US"}[的认证方案相配合，具体请参考"安全配置指导"中的"]{style="font-family:宋体"}[AAA]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1979_37509_1898315809}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_2047653537}[配置切换用户角色时采用]{style="font-family:宋体"}**[local]{lang="EN-US"}**[认证方式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1979_37509_x1070218501}

[\[Sysname\] super authentication-mode local]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_2103757925}[配置切换用户角色时采用先]{style="font-family:宋体"}**[scheme]{lang="EN-US"}**[后]{style="font-family:宋体"}**[local]{lang="EN-US"}**[的]{style="font-family:宋体"}[认证方式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1979_37509_304903453}

[\[Sysname\] super authentication-mode scheme local]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x63936283}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication super]{lang="EN-US"}**]{#struct_0_x1979_37509_640404356}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/AAA]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[super password]{lang="EN-US"}**]{#struct_0_x1979_37509_x1672440558}
:::

::: {#-941848615 .myid}
[]{#_Toc404782258}[]{#struct_0_x1979_37509_x452037423}[]{#_Toc375921060}[]{#_Toc373390834}

**RBAC \-- RBAC配置命令 \-- super default role**

------------------------------------------------------------------------

[**[super default role]{lang="EN-US"}**]{#struct_0_x1979_37509_1777713514}[命令用来配置用户角色切换的缺省目的角色。]{style="font-family:宋体"}

[**[undo super default role]{lang="EN-US"}**]{#struct_0_x1979_37509_x451971887}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_731610715}

[**[super default role ]{lang="EN-US"}***[rolename]{lang="EN-US"}*]{#struct_0_x1979_37509_1978753048}

[**[undo super default role]{lang="EN-US"}**]{#struct_0_x1979_37509_27502917}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1764712362}

[[用户角色切换的缺省目的角色为]{style="font-family:宋体"}[network-admin]{lang="EN-US"}]{#struct_0_x1979_37509_569004007}[。（不支持]{style="font-family:宋体"}[MDC]{lang="EN-US"}[、]{style="font-family:宋体"}[Context]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[对于登录缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_x1979_37509_x451119919}[的用户，用户角色切换的缺省目的角色为]{style="font-family:宋体"}[network-admin]{lang="EN-US"}[；对于登录非缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的用户，用户角色切换的缺省目的角色为]{style="font-family:宋体"}[mdc-admin]{lang="EN-US"}[。（支持]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[对于登录缺省]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_x1979_37509_x1255792060}[的用户，用户角色切换的缺省目的角色为]{style="font-family:宋体"}[network-admin]{lang="EN-US"}[；对于登录非缺省]{style="font-family:宋体"}[Context]{lang="EN-US"}[的用户，用户角色切换的缺省目的角色为]{style="font-family:宋体"}[context-admin.]{lang="EN-US"}[（支持]{style="font-family:宋体"}[Context]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1979_37509_2092760312}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1979_37509_1993690124}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1963829143}

[[network-admin]{lang="EN-US"}]{#struct_0_x1979_37509_1175584438}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1979_37509_x451054383}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1979_37509_712253233}

[*[rolename]{lang="EN-US" style="color:black"}*]{#struct_0_x1979_37509_x1181941008}[：]{style="font-family:
宋体;color:black"}[待切换的用户角色名称]{style="font-family:宋体"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写，可以是系统中已存在的任意用户角色。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1979_37509_1918902719}

[[当执行]{style="font-family:宋体"}**[super]{lang="EN-US"}**]{#struct_0_x1979_37509_x1819927863}[命令切换用户角色时，或配置用户角色切换的密码时，如不指定目的切换的角色名称，则表示使用]{style="font-family:宋体"}**[super default role]{lang="EN-US"}**[命令配置的缺省用户角色。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x451644208}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_x1242750881}[配置用户切换角色的缺省目的角色为]{style="font-family:宋体"}[network-operator]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1979_37509_1082929161}

[\[Sysname\] super default role network-operator]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1606466032}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[super]{lang="EN-US"}**]{#struct_0_x1979_37509_x1471111633}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[super password]{lang="EN-US"}**]{#struct_0_x1979_37509_681771259}
:::

::: {#912350306 .myid}
[]{#_Toc404782259}[]{#struct_0_x1979_37509_772914573}[]{#_Toc320537175}[]{#_Toc320518510}[]{#_Toc300678541}

**RBAC \-- RBAC配置命令 \-- super password**

------------------------------------------------------------------------

[**[super password]{lang="EN-US"}**]{#struct_0_x1979_37509_x1609843610}[命令用来设置用户角色切换的密码]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo super password]{lang="EN-US"}**]{#struct_0_x1979_37509_1285614336}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x741979751}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_x1979_37509_x617272544}[模式下：]{style="font-family:宋体"}

[**[super password ]{lang="EN-US"}**[\[ **role** *rolename* \] \[ { **hash** \| **simple** } *password* \]]{lang="EN-US"}]{#struct_0_x1979_37509_1957161152}

[**[undo super password]{lang="EN-US"}**[ \[ **role** *rolename* \]]{lang="EN-US"}]{#struct_0_x1979_37509_1290121308}

[[FIPS]{lang="EN-US"}]{#struct_0_x1979_37509_x1672440559}[模式下：]{style="font-family:宋体"}

[**[super password ]{lang="EN-US"}**[\[ **role** *rolename* \]]{lang="EN-US"}]{#struct_0_x1979_37509_x793169368}

[**[undo super password]{lang="EN-US"}**[ \[ **role** *rolename* \]]{lang="EN-US"}]{#struct_0_x1979_37509_x2099377108}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1979_37509_1264859346}

[[未设置用户角色切换密码。]{style="font-family:宋体"}]{#struct_0_x1979_37509_x976674165}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1979_37509_1369298223}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1979_37509_444837684}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1949863154}

[[network-admin]{lang="EN-US"}]{#struct_0_x1979_37509_x701270722}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1979_37509_x1672440560}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1979_37509_416487605}

[**[role]{lang="EN-US"}***[ rolename]{lang="EN-US"}*]{#struct_0_x1979_37509_x1882851072}[：待切换的用户角色的名称，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写，可以为系统预定义或用户自定义的用户角色。如果不指定角色名称，则表示设置的是切换到用户角色]{style="font-family:宋体"}[network-admin]{lang="EN-US"}[的密码。（不支持]{style="font-family:宋体"}[MDC]{lang="EN-US"}[、]{style="font-family:宋体"}[Context]{lang="EN-US"}[的设备）。如果不指定角色名称，则表示设置的是切换到当前缺省目的用户角色的密码。缺省的目的用户角色由]{style="font-family:宋体"}**[super default role]{lang="EN-US"}**[命令指定。]{style="font-family:宋体"}

[**[hash]{lang="EN-US"}**]{#struct_0_x1979_37509_x713383638}[：表示以哈希方式设置用户密码。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_x1979_37509_1974695047}[：表示以明文方式设置用户密码。]{style="font-family:宋体"}

[*[password]{lang="EN-US"}*]{#struct_0_x1979_37509_349147794}[：设置的明文密码或哈希密码，区分大小写。]{style="font-family:宋体"}[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}[明文密码为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串；哈希密码为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[110]{lang="EN-US"}[个字符的字符串]{style="font-family:宋体"}[；]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，密码为]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，]{style="font-family:宋体"}[密码元素的最少组合类型为]{style="font-family:宋体"}[4]{lang="EN-US"}[（必须包括数字、大写字母、小写字母以及特殊字符）]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1619475122}

[[如果不指定任何参数，则表示以交互式方式设置本地用户密码，涵义与指定]{style="font-family:宋体"}**[simple]{lang="EN-US"}**]{#struct_0_x1979_37509_1770695970}[关键字相同。]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，只支持交互式方式设置]{style="font-family:宋体"}[用户角色切换]{style="font-family:宋体"}[密码。]{style="font-family:宋体"}

[[以明文方式设置的密码，以哈希计算后的密文形式保存在配置文件中，以哈希方式设置的密码将以设置的原始形式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_x1979_37509_x309489008}

[[当用户切换认证方式为]{style="font-family:宋体"}**[local]{lang="EN-US"}**]{#struct_0_x1979_37509_x1672440561}[或包含]{style="font-family:宋体"}**[local]{lang="EN-US"}**[（]{style="font-family:宋体"}**[local scheme]{lang="EN-US"}**[、]{style="font-family:宋体"}**[scheme local]{lang="EN-US"}**[）时，才需要本命令指定的]{style="font-family:宋体"}[用户角色切换]{style="font-family:宋体"}[密码。]{style="font-family:宋体"}

[[为保证权限控制更加安全，推荐给不同的用户角色指定不同的切换密码。]{style="font-family:宋体"}]{#struct_0_x1979_37509_x1149596336}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1979_37509_609885433}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_396496543}[配置将用户角色切换到]{style="font-family:宋体"}[network-operator]{lang="EN-US"}[时使用的密码为明文密码]{style="font-family:宋体"}[123456TESTplat&!]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1979_37509_951816493}

[\[Sysname\] super password role network-operator simple 123456TESTplat&!]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_x721816198}[以交互式方式设置将用户角色切换到]{style="font-family:宋体"}[network-operator]{lang="EN-US"}[时使用的密码为明文密码]{style="font-family:宋体"}[123456TESTplat&!]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1979_37509_x1672440563}

[\[Sysname\] super password role network-operator]{lang="EN-US"}

[Password:]{lang="EN-US"}

[Confirm :]{lang="EN-US"}

[Updating user information. Please wait\... \...]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_13203078}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[super authentication-mode]{lang="EN-US"}**]{#struct_0_x1979_37509_x1672440564}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[super default role]{lang="EN-US"}**]{#struct_0_x1979_37509_x452037424}
:::

::::: {#1502976409 .myid}
[]{#_Toc404782260}[]{#struct_0_x1979_37509_x911686396}

**RBAC \-- RBAC配置命令 \-- security-zone policy deny**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RBAC命令.files/image002.png){#图片 1 border="0" width="62" height="26"}]{lang="EN-US"}]{#struct_0_x1979_37509_x911751932}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1979_37509_x478126552}
:::

[ ]{lang="EN-US"}

[**[security-zone policy deny]{lang="EN-US"}**]{#struct_0_x1979_37509_x911555324}[命令用来进入安全域策略视图。]{style="font-family:
宋体"}

[**[undo security-zone policy deny]{lang="EN-US"}**]{#struct_0_x1979_37509_x536203187}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x911620860}

[**[security-zone policy deny]{lang="EN-US"}**]{#struct_0_x1979_37509_303157985}

[**[undo security-zone policy deny]{lang="EN-US"}**]{#struct_0_x1979_37509_1639202104}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x911424252}

[[用户具有操作任何安全域的权限。]{style="font-family:宋体"}]{#struct_0_x1979_37509_245605644}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x911489788}

[[用户角色视图]{style="font-family:宋体"}]{#struct_0_x1979_37509_1046282978}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x677029149}

[[network-admin]{lang="EN-US"}]{#struct_0_x1979_37509_x911293180}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1979_37509_x87854046}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1979_37509_1038221922}

[[进入安全域策略视图后，如果不配置允许操作的安全域列表，则用户将没有操作任何安全域的权限；如果需要限制或区分用户对安全域资源的使用权限，则还应该通过]{style="font-family:宋体"}**[permit security-zone]{lang="EN-US"}**]{#struct_0_x1979_37509_x911358716}[命令配置允许用户操作的安全域列表。若安全域策略视图中未配置允许操作的安全域列表，则表示不允许用户操作所有的安全域。对安全域的"操作"指的是创建并进入安全域视图、删除和应用安全域。]{style="font-family:宋体"}

[[允许修改用户角色的安全域策略，但修改后的策略只对被授权该角色的用户重新登录时才会生效。]{style="font-family:宋体"}]{#struct_0_x1979_37509_x541231339}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1979_37509_654266478}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_x1697033546}[在用户角色]{style="font-family:宋体"}[role1]{lang="EN-US"}[中，进入安全域策略视图，禁止角色为]{style="font-family:宋体"}[role1]{lang="EN-US"}[的用户操作任意安全域。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1979_37509_654200942}

[\[Sysname\] role name role1]{lang="EN-US"}

[\[Sysname-role-role1\] security-zone policy deny]{lang="EN-US"}

[\[Sysname-role-role1-zonepolicy\] quit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_979713985}[在用户角色]{style="font-family:宋体"}[role1]{lang="EN-US"}[中，进入安全域策略视图，允许角色为]{style="font-family:宋体"}[role1]{lang="EN-US"}[的用户操作安全域]{style="font-family:宋体"}[trust]{lang="EN-US"}[和]{style="font-family:宋体"}[abc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1979_37509_654397550}

[\[Sysname\] role name role1]{lang="EN-US"}

[\[Sysname-role-role1\] security-zone policy deny]{lang="EN-US"}

[\[Sysname-role-role1-zonepolicy\] permit security-zone trust abc]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1716598490}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}]{.ItemStepChar}[**[display role]{lang="EN-US"}**]{.ItemStepChar}]{#struct_0_x1979_37509_x1495944573}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[permit security-zone]{lang="EN-US"}**]{#struct_0_x1979_37509_654332014}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[role]{lang="EN-US"}**]{#struct_0_x1979_37509_1403921841}
:::::

::: {#125460501 .myid}
[]{#_Toc404782261}[]{#struct_0_x1979_37509_x1552880863}

**RBAC \-- RBAC配置命令 \-- vlan policy deny**

------------------------------------------------------------------------

[**[vlan policy deny]{lang="EN-US"}**]{#struct_0_x1979_37509_808047794}[命令用来进入]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[策略视图。]{style="font-family:宋体"}

[**[undo vlan policy deny]{lang="EN-US"}**]{#struct_0_x1979_37509_x1894125980}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1961620148}

[**[vlan policy deny]{lang="EN-US"}**]{#struct_0_x1979_37509_1461183777}

[**[undo vlan policy deny]{lang="EN-US"}**]{#struct_0_x1979_37509_x863136491}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1979_37509_115006556}

[[用户具有操作任何]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1979_37509_791076368}[的权限。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1979_37509_299273473}

[[用户角色视图]{style="font-family:宋体"}]{#struct_0_x1979_37509_x436527494}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x2137553748}

[[network-admin]{lang="EN-US"}]{#struct_0_x1979_37509_x1717747415}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1979_37509_x863136492}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1979_37509_114809948}

[[进入]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1979_37509_x1915593407}[策略视图后，如果不配置允许操作的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，则用户将没有操作任何]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的权限；如果需要限制或区分用户对]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[资源的使用权限，则还应该通过]{style="font-family:宋体"}**[permit vlan]{lang="EN-US"}**[命令配置允许用户操作的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表。若]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[策略视图中未配置允许操作的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，则表示不允许用户操作所有的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。对]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的"操作"指的是创建并进入]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图、删除和应用]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[允许修改用户角色的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1979_37509_1142249815}[策略，但修改后的策略只对被授权该角色的用户重新登录时才会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1979_37509_494820746}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_x944052204}[在用户角色]{style="font-family:宋体"}[role1]{lang="EN-US"}[中，进入]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[策略视图，禁止角色为]{style="font-family:宋体"}[role1]{lang="EN-US"}[的用户操作任意]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1979_37509_x1838799052}

[\[Sysname\] role name role1]{lang="EN-US"}

[\[Sysname-role-role1\] vlan policy deny]{lang="EN-US"}

[\[Sysname-role-role1-vlanpolicy\] quit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_x863136493}[在用户角色]{style="font-family:宋体"}[role1]{lang="EN-US"}[中，进入]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[策略视图，允许角色为]{style="font-family:宋体"}[role1]{lang="EN-US"}[的用户操作]{style="font-family:宋体"}[VLAN 50]{lang="EN-US"}[～]{style="font-family:宋体"}[VLAN 100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1979_37509_114875484}

[\[Sysname\] role name role1]{lang="EN-US"}

[\[Sysname-role-role1\] vlan policy deny]{lang="EN-US"}

[\[Sysname-role-role1-vlanpolicy\] permit vlan 50 to 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x728665843}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}]{.ItemStepChar}[**[display role]{lang="EN-US"}**]{.ItemStepChar}]{#struct_0_x1979_37509_1848943564}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[permit vlan]{lang="EN-US"}**]{#struct_0_x1979_37509_x374944234}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[role]{lang="EN-US"}**]{#struct_0_x1979_37509_2046219599}
:::

::: {#-119084857 .myid}
[]{#_Toc404782262}[]{#struct_0_x1979_37509_1584222351}[]{#_Toc285213510}

**RBAC \-- RBAC配置命令 \-- vpn-instance policy deny**

------------------------------------------------------------------------

[**[vpn-instance policy deny]{lang="EN-US"}**]{#struct_0_x1979_37509_x1447981438}[命令用来进入]{style="font-family:
宋体"}[VPN]{lang="EN-US"}[策略视图。]{style="font-family:宋体"}

[**[undo vpn-instance policy deny]{lang="EN-US"}**]{#struct_0_x1979_37509_x863136494}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_115203164}

[**[vpn-instance policy deny]{lang="EN-US"}**]{#struct_0_x1979_37509_1434628218}

[**[undo vpn-instance policy deny]{lang="EN-US"}**]{#struct_0_x1979_37509_696367536}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x2019787742}

[[用户具有操作任何]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x1979_37509_217565185}[实例的权限。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1979_37509_1044100146}

[[用户角色视图]{style="font-family:宋体"}]{#struct_0_x1979_37509_1764246459}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x863136495}

[[network-admin]{lang="EN-US"}]{#struct_0_x1979_37509_115268700}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1979_37509_x1690897262}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1979_37509_1928634860}

[[进入]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x1979_37509_69427500}[策略视图后，如果不配置允许操作的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[列表，则用户将没有操作任何]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的权限；如果需要限制或区分用户对]{style="font-family:宋体"}[VPN]{lang="EN-US"}[资源的使用权限，则还应该通过]{style="font-family:宋体"}**[permit vpn-instance]{lang="EN-US"}**[命令配置允许用户操作的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[列表。若]{style="font-family:宋体"}[VPN]{lang="EN-US"}[策略视图中未配置允许操作的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[列表，则表示不允许用户操作所有的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。对]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的"操作"指的是创建并进入]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[视图、删除和应用]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。]{style="font-family:宋体"}

[[允许修改用户角色的]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x1979_37509_x1236258003}[策略，但修改后的策略只对被授权该角色的用户重新登录时才会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x1108010453}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_1125333774}[在用户角色]{style="font-family:宋体"}[role1]{lang="EN-US"}[中，创建并进入一个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[策略视图，并禁止角色为]{style="font-family:宋体"}[role1]{lang="EN-US"}[的用户操作任意]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1979_37509_x863136496}

[\[Sysname\] role name role1]{lang="EN-US"}

[\[Sysname-role-role1\] vpn-instance policy deny]{lang="EN-US"}

[\[Sysname-role-role1-vpnpolicy\] quit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1979_37509_115072092}[在用户角色]{style="font-family:宋体"}[role1]{lang="EN-US"}[中，创建并进入一个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[策略视图，允许角色为]{style="font-family:宋体"}[role1]{lang="EN-US"}[的用户操作]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[vpn2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1979_37509_794567858}

[\[Sysname\] role name role1]{lang="EN-US"}

[\[Sysname-role-role1\] vpn-instance policy deny]{lang="EN-US"}

[\[Sysname-role-role1-vpnpolicy\] permit vpn-instance vpn2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1979_37509_x725955078}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}]{.ItemStepChar}[**[display role]{lang="EN-US"}**]{.ItemStepChar}]{#struct_0_x1979_37509_243639272}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[permit vpn-instance]{lang="EN-US"}**]{#struct_0_x1979_37509_1329262895}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[role]{lang="EN-US"}**]{#struct_0_x1979_37509_x593027761}

[ ]{lang="EN-US"}
:::
