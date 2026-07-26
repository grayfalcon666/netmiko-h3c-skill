
**RBAC \-- RBAC配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来配置用户角色描述信息。

**[undo description**]用来删除用户角色的描述信息。

【命令】

**[description ***text*]

**[undo description**]

【缺省情况】

未定义用户角色描述信息。

【视图】

用户角色视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：用户角色描述信息，为1～128个字符的字符串，区分大小写。

【使用指导】

描述信息用来方便管理员对用户角色进行管理。

【举例】

\# 为用户角色role1配置描述信息为"labVIP"。

\<Sysname\> system-view

Sysname role name role1

Sysname-role-role1 description labVIP

【相关命令】

·**[display role**]{.ItemStepChar}

·**role**

**RBAC \-- RBAC配置命令 \-- display role**

------------------------------------------------------------------------

**[display role**]命令用来显示用户角色信息。

【命令】

**[display role ** **name** *role-name* ]

【视图】

任意视图

【缺省用户角色】

network-admin

netword-operator

mdc-admin

mdc-operator

【参数】

**[name*** role-name*]：用户角色名称，为1～63个字符的字符串，区分大小写。

【使用指导】

如果不指定用户角色名称，则表示显示所有用户角色的信息，包括系统缺省存在的用户角色的信息。

【举例】

\# 显示用户角色123的信息。

\<Sysname\> display role name 123

Role: 123

  Description: new role

  VLAN policy: deny

  Permitted VLANs: 1 to 5, 7 to 8

  Interface policy: deny

  Permitted interfaces: GigabitEthernet1/0/1 to GigabitEthernet1/0/2, Vlan-interface1 to Vlan-interface20

  VPN instance policy: deny

  Permitted VPN instances: vpn, vpn1, vpn2

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Rule    Perm   Type  Scope         Entity

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  1       permit RWX   feature-group abc

  2       deny   -W-   feature       ldap

  3       permit       command       system ; radius sc \*

  4       permit R\--   xml-element   -

  5       permit RW-   oid           1.2.1

  R:Read W:Write X:Execute

\# 显示所有用户角色的信息。

\<Sysname\> display role

Role: network-admin

  Description: Predefined network admin role has access to all commands on the device

  VLAN policy: permit (default)

  Interface policy: permit (default)

  VPN instance policy: permit (default)

  Security zone policy: permit (default)

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Rule    Perm   Type  Scope         Entity

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  sys-1   permit       command       \*

  sys-2   permit RWX   web-menu      -

  sys-3   permit RWX   xml-element   -

  sys-4   deny         command       display security-logfile summary

  sys-5   deny         command       system-view ; info-center securi

                                     ty-logfile directory \*

  sys-6   deny         command       security-logfile save

  sys-7   permit RW-   oid           1

  R:Read W:Write X:Execute

Role: network-operator

  Description: Predefined network operator role has access to all read commands on the device

  VLAN policy: permit (default)

  Interface policy: permit (default)

  VPN instance policy: permit (default)

  Security zone policy: permit (default)

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Rule    Perm   Type  Scope         Entity

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  sys-1   permit       command       display \*

  sys-2   permit       command       xml

  sys-3   deny         command       display history-command all

  sys-4   deny         command       display exception \*

  sys-5   deny         command       display cpu-usage configuration

                                     \*

  sys-6   deny         command       display kernel exception \*

  sys-7   deny         command       display kernel deadloop \*

  sys-8   deny         command       display kernel starvation \*

  sys-9   deny         command       display kernel reboot \*

  sys-10  deny         command       display memory trace \*

  sys-11  deny         command       display kernel memory \*

  sys-12  permit       command       system-view ; local-user \*

  sys-13  permit       command       system-view ; switchto mdc \*

  sys-14  permit R\--   web-menu      -

  sys-15  permit R\--   xml-element   -

  sys-16  deny         command       display security-logfile summary

  sys-17  deny         command       system-view ; info-center securi

                                     ty-logfile directory \*

  sys-18  deny         command       security-logfile save

  sys-19  permit R\--   oid           1

  R:Read W:Write X:Execute

Role: mdc-admin

  Description: Predefined MDC admin role has access to all commands within an MDC instance

  VLAN policy: permit (default)

  Interface policy: permit (default)

  VPN instance policy: permit (default)

  Security zone policy: permit (default)

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Rule    Perm   Type  Scope         Entity

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  sys-1   permit       command       \*

  sys-2   permit RWX   web-menu      -

  sys-3   permit RWX   xml-element   -

  sys-4   deny   RWX   feature       mdc

  sys-5   permit       command       display mdc \*

  sys-6   permit       command       switchback

  sys-7   deny         command       display security-logfile summary

  sys-8   deny         command       system-view ; info-center securi

                                     ty-logfile directory \*

  sys-9   deny         command       security-logfile save

  sys-10  permit RW-   oid           1

  R:Read W:Write X:Execute

Role: mdc-operator

  Description: Predefined MDC operator role has access to all read commands within an MDC instance

  VLAN policy: permit (default)

  Interface policy: permit (default)

  VPN instance policy: permit (default)

  Security zone policy: permit (default)

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Rule    Perm   Type  Scope         Entity

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  sys-1   permit       command       display \*

  sys-2   permit       command       xml

  sys-3   deny         command       display history-command all

  sys-4   deny         command       display exception \*

  sys-5   deny         command       display cpu-usage configuration

  sys-6   deny         command       display kernel exception \*

  sys-7   deny         command       display kernel deadloop \*

  sys-8   deny         command       display kernel starvation \*

  sys-9   deny         command       display kernel reboot \*

  sys-10  deny         command       display memory trace \*

  sys-11  deny         command       display kernel memory \*

  sys-12  permit       command       system-view ; local-user \*

  sys-13  permit       command       switchback

  sys-14  permit R\--   web-menu      -

  sys-15  permit R\--   xml-element   -

  sys-16  deny         command       display security-logfile summary

  sys-17  deny         command       system-view ; info-center securi

                                     ty-logfile directory \*

  sys-18  deny         command       security-logfile save

  sys-19  permit R\--   oid           1

  R:Read W:Write X:Execute

Role: context-admin

  Description: Predefined Context admin role has access to all commands within a Context

  VLAN policy: permit (default)

  Interface policy: permit (default)

  VPN instance policy: permit (default)

  Security zone policy: permit (default)

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Rule    Perm   Type  Scope         Entity

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  sys-1   permit       command       \*

  sys-2   permit RWX   web-menu      -

  sys-3   permit RWX   xml-element   -

  sys-4   deny   RWX   feature       context

  sys-5   permit R\--   command       display context \*

  sys-5   deny         command       display security-logfile summary

  sys-6   deny         command       system-view ; info-center securi

                                     ty-logfile directory \*

  sys-7   deny         command       security-logfile save

  sys-8   permit RW-   oid           1

  R:Read W:Write X:Execute

Role: context-operator

  Description: Predefined Context operator role has access to all read commands within a Context

  VLAN policy: permit (default)

  Interface policy: permit (default)

  VPN instance policy: permit (default)

  Security zone policy: permit (default)

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Rule    Perm   Type  Scope         Entity

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  sys-1   permit       command       display \*

  sys-2   permit       command       xml

  sys-3   deny         command       display history-command all

  sys-4   permit       command       system-view ; local-user \*

  sys-5   permit R\--   web-menu      -

  sys-6   permit R\--   xml-element   -

  sys-7   deny         command       display security-logfile summary

  sys-8   deny         command       system-view ; info-center securi

                                     ty-logfile directory \*

  sys-9   deny         command       security-logfile save

  sys-10  permit R\--   oid           1

  R:Read W:Write X:Execute

Role: level-0

  Description: Predefined level-0 role

  VLAN policy: permit (default)

  Interface policy: permit (default)

  VPN instance policy: permit (default)

  Security zone policy: permit (default)

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Rule    Perm   Type  Scope         Entity

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  sys-1   permit       command       tracert \*

  sys-2   permit       command       telnet \*

  sys-3   permit       command       ping \*

  sys-4   permit       command       ssh2 \*

  sys-5   permit       command       super \*

  R:Read W:Write X:Execute

Role: level-1

  Description: Predefined level-1 role

  VLAN policy: permit (default)

  Interface policy: permit (default)

  VPN instance policy: permit (default)

  Security zone policy: permit (default)

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Rule    Perm   Type  Scope         Entity

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  sys-1   permit       command       tracert \*

  sys-2   permit       command       telnet \*

  sys-3   permit       command       ping \*

  sys-4   permit       command       ssh2 \*

  sys-5   permit       command       display \*

  sys-6   permit       command       super \*

  sys-7   deny         command       display history-command all

  R:Read W:Write X:Execute

Role: level-2

  Description: Predefined level-2 role

  VLAN policy: permit (default)

  Interface policy: permit (default)

  VPN instance policy: permit (default)

  Security zone policy: permit (default)

Role: level-3

  Description: Predefined level-3 role

  VLAN policy: permit (default)

  Interface policy: permit (default)

  VPN instance policy: permit (default)

  Security zone policy: permit (default)

Role: level-4

  Description: Predefined level-4 role

  VLAN policy: permit (default)

  Interface policy: permit (default)

  VPN instance policy: permit (default)

  Security zone policy: permit (default)

Role: level-5

  Description: Predefined level-5 role

  VLAN policy: permit (default)

  Interface policy: permit (default)

  VPN instance policy: permit (default)

  Security zone policy: permit (default)

Role: level-6

  Description: Predefined level-6 role

  VLAN policy: permit (default)

  Interface policy: permit (default)

  VPN instance policy: permit (default)

  Security zone policy: permit (default)

Role: level-7

  Description: Predefined level-7 role

  VLAN policy: permit (default)

  Interface policy: permit (default)

  VPN instance policy: permit (default)

  Security zone policy: permit (default)

Role: level-8

  Description: Predefined level-8 role

  VLAN policy: permit (default)

  Interface policy: permit (default)

  VPN instance policy: permit (default)

  Security zone policy: permit (default)

Role: level-9

  Description: Predefined leve-9 role

  VLAN policy: permit (default)

  Interface policy: permit (default)

  VPN instance policy: permit (default)

  Security zone policy: permit (default)

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Rule    Perm   Type  Scope         Entity

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  sys-1   permit RWX   feature       -

  sys-2   deny   RWX   feature       device

  sys-3   deny   RWX   feature       filesystem

  sys-4   permit       command       display \*

  sys-5   deny         command       display history-command all

  R:Read W:Write X:Execute

Role: level-10

  Description: Predefined level-10 role

  VLAN policy: permit (default)

  Interface policy: permit (default)

  VPN instance policy: permit (default)

  Security zone policy: permit (default)

Role: level-11

  Description: Predefined level-11 role

  VLAN policy: permit (default)

  Interface policy: permit (default)

  VPN instance policy: permit (default)

  Security zone policy: permit (default)

Role: level-12

  Description: Predefined level-12 role

  VLAN policy: permit (default)

  Interface policy: permit (default)

  VPN instance policy: permit (default)

  Security zone policy: permit (default)

Role: level-13

  Description: Predefined level-13 role

  VLAN policy: permit (default)

  Interface policy: permit (default)

  VPN instance policy: permit (default)

  Security zone policy: permit (default)

Role: level-14

  Description: Predefined level-14 role

  VLAN policy: permit (default)

  Interface policy: permit (default)

  VPN instance policy: permit (default)

  Security zone policy: permit (default)

Role: level-15

  Description: Predefined level-15 role

  VLAN policy: permit (default)

  Interface policy: permit (default)

  VPN instance policy: permit (default)

  Security zone policy: permit (default)

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Rule    Perm   Type  Scope         Entity

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  sys-1   permit       command       \*

  sys-2   permit RWX   web-menu      -

  sys-3   permit RWX   xml-element   -

  sys-4   deny         command       display security-logfile summary

  sys-5   deny         command       system-view ; info-center securi

                                     ty-logfile directory \*

  sys-6   deny         command       security-logfile save

  sys-7   permit RW-   oid           1

  R:Read W:Write X:Execute

Role: 123

  Description: new role

  VLAN policy: deny

  Permitted VLANs: 1 to 5, 7 to 8

  Interface policy: deny

  Permitted interfaces: GigabitEthernet1/0/1 to GigabitEthernet1/0/2, Vlan-interface1 to Vlan-interface20

  VPN instance policy: deny

  Permitted VPN instances: vpn, vpn1, vpn2

  Security zone policy: permit (default)

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Rule    Perm   Type  Scope         Entity

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  1       permit RWX   feature-group abc

  2       deny   -W-   feature       ldap

  3       permit       command       system ; radius sc \*

  4       permit R\--   xml-element   -

  5       permit RW-   oid           1.2.1

  R:Read W:Write X:Execute

Role: security-audit

  Description: Predefined security audit role only has access to commands for th

e security log administrator

  VLAN policy: permit (default)

  Interface policy: permit (default)

  VPN instance policy: permit (default)

  Security zone policy: permit (default)

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Rule    Perm   Type  Scope         Entity

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  sys-1   deny         command       \*

  sys-2   permit       command       display security-logfile summary

  sys-3   permit       command       system-view ; info-center securi

                                     ty-logfile directory \*

  sys-4   permit       command       security-logfile save

  sys-5   permit       command       cd \*

  sys-6   permit       command       copy \*

  sys-7   permit       command       delete \*

  sys-8   permit       command       dir \*

  sys-9   permit       command       mkdir \*

  sys-10  permit       command       more \*

  sys-11  permit       command       move \*

  sys-12  permit       command       rmdir \*

  sys-13  permit       command       pwd

  sys-14  permit       command       rename \*

  sys-15  permit       command       undelete \*

  sys-16  permit       command       ftp \*

  sys-17  permit       command       sftp \*

  sys-18  permit       command       virtual-ftp-append

  sys-19  permit       command       virtual-ftp-ascii

  sys-20  permit       command       virtual-ftp-binary

  sys-21  permit       command       virtual-ftp-bye

  sys-22  permit       command       virtual-ftp-cd

  sys-23  permit       command       virtual-ftp-cdup

  sys-24  permit       command       virtual-ftp-close

  sys-25  permit       command       virtual-ftp-delete

  sys-26  permit       command       virtual-ftp-debug

  sys-27  permit       command       virtual-ftp-dir

  sys-28  permit       command       virtual-ftp-disconnect

  sys-29  permit       command       virtual-ftp-get

  sys-30  permit       command       virtual-ftp-help

  sys-31  permit       command       virtual-ftp-lcd

  sys-32  permit       command       virtual-ftp-ls

  sys-33  permit       command       virtual-ftp-mkdir

  sys-34  permit       command       virtual-ftp-newer

  sys-35  permit       command       virtual-ftp-open

  sys-36  permit       command       virtual-ftp-passive

  sys-37  permit       command       virtual-ftp-put

  sys-38  permit       command       virtual-ftp-pwd

  sys-39  permit       command       virtual-ftp-quit

  sys-40  permit       command       virtual-ftp-reget

  sys-41  permit       command       virtual-ftp-rstatus

  sys-42  permit       command       virtual-ftp-rhelp

  sys-43  permit       command       virtual-ftp-rename

  sys-44  permit       command       virtual-ftp-reset

  sys-45  permit       command       virtual-ftp-restart

  sys-46  permit       command       virtual-ftp-rmdir

  sys-47  permit       command       virtual-ftp-status

  sys-48  permit       command       virtual-ftp-system

  sys-49  permit       command       virtual-ftp-user

  sys-50  permit       command       virtual-ftp-verbose

  sys-51  permit       command       virtual-ftp-remove

  sys-52  permit       command       virtual-ftp-exit

  R:Read W:Write X:Execute

表1-1 display role命令显示信息描述表

字段

描述

Role

用户角色名称，其中系统预定义的用户角色名称分别为network-admin、network-operator、mdc-admin、mdc-operator、context-admin、context-operator、level-*n*（*n*为0～15）、security-audit

Description

用户角色描述信息

VLAN policy

配置的VLAN策略：

·deny：表示除允许操作指定的VLAN外，其它VLAN均不能被用户操作

·permit (default)：表示系统缺省允许用户操作任何VLAN

Permitted VLANs

允许用户操作的VLAN

Interface policy

配置的接口策略：

·deny：表示除允许操作指定的接口外，其它接口均不能被用户操作

·permit (default)：表示系统缺省允许用户操作任何接口

Permitted interfaces

允许用户操作的接口

VPN-instance policy

配置的VPN策略：

·deny：表示除允许操作指定的VPN实例外，其它VPN实例均不能被用户操作

·permit (default)：表示系统缺省允许用户操作任何VPN实例

Permitted VPN instances

允许用户操作的VPN实例

Security zone policy

配置的安全域策略：

·deny：表示除允许操作指定的安全域外，其它安全域均不能被用户操作

·permit (default)：表示系统缺省允许用户操作任何安全域

该显示信息的支持情况与设备的型号有关，请以设备的实际情况为准

Permitted security zones

允许用户操作的安全域

该显示信息的支持情况与设备的型号有关，请以设备的实际情况为准

Rule

用户角色规则编号（系统预定义的权限规则通过sys-n标识）

Perm

对命令行的操作许可：

·permit：允许操作

·deny：禁止操作

Type

命令行类型：

·R：读类型

·W：写类型

·X：执行类型

Scope

用户角色规则的类型：

·command：基于命令行的规则

·feature：基于特性的规则

·feature-group：基于特性组规则

·web-menu：基于Web菜单的规则

·xml-element：基于XML元素的规则

·oid：基于OID元素的规则

Entity

用户角色规则中定义的具体内容（命令特征字符串、特性名称或者特性组名称）

·"-"表示所有特性

·"\*"为通配符，表示0个或多个任意字符

【相关命令】

·**role**

**RBAC \-- RBAC配置命令 \-- display role feature**

------------------------------------------------------------------------

**[display role feature**]命令用来显示特性相关信息。

【命令】

**[display role feature **[[ **name** *feature-name* \| **verbose** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

netword-operator

mdc-admin

mdc-operator

【参数】

**[name ***feature-name*]：显示指定特性的详细信息，*feature-name*表示系统中的特性名称，且所有特性名称中的字母均为小写。

**[verbose**]：显示所有特性的详细信息，即显示特性内包含的所有命令行列表。

【使用指导】

如果不指定任何关键字，则显示系统中所有特性的名称列表。

【举例】

![说明](RBAC命令.files/image001.png)

以下内容中涉及的特性、命令行均为示例，具体的显示信息与设备的实际情况有关，请以设备的实际情况为准。

\# 显示系统中所有特性的名称列表。

\<Sysname\> display role feature

Feature: device          (Device configuration related commands)

Feature: interface       (Interface related commands)

Feature: syslog          (Syslog related commands)

Feature: process         (Process related commands)

......（略）

\# 显示所有特性的详细信息。

\<Sysname\> display role feature verbose

Feature: device          (Device configuration related commands)

  display clock    (R)

  debugging dev    (W)

  display debugging dev    (R)

  display device \*    (R)

  display diagnostic-information    (R)

  display environment \*    (R)

  display fan \*    (R)

  display power \*    (R)

  display rps \*    (R)

  display current-configuration \*    (R)

  display saved-configuration \*    (R)

  display startup    (R)

  display this \*    (R)

  display version    (R)

  clock datetime \*    (W)

  reboot \*    (W)

  save \*    (W)

  startup saved-configuration \*    (W)

  system-view ; temperature-limit \*    (W)

  system-view ; sysname \*    (W)

  system-view ; clock timezone \*    (W)

  system-view ; configuration replace file \*    (W)

  system-view ; user-interface \* ; idle-timeout \*    (W)

Feature: interface       (Interface related commands)

  reset counters interface \*    (W)

  debugging ifnet \*    (W)

  display port-group manual \*    (R)

  display debugging ifnet    (R)

  display interface \*   (R)

......（略）

\# 显示特性aaa的详细信息。

\<Sysname\> display role feature name aaa

Feature: aaa             (AAA related commands)

  system-view ; domain \*    (W)

  system-view ; header \*    (W)

  system-view ; aaa \*    (W)

  display domain \*    (R)

  system-view ; user-group \*    (W)

  system-view ; local-user \*    (W)

  display local-user \*    (R)

  display user-group \*    (R)

  display debugging local-server    (R)

  debugging local-server \*    (W)

  super \*    (X)

  display password-control \*    (R)

  reset password-control \*    (W)

  system-view ; password-control \*    (W)

表1-2 display role feature命令显示信息描述表（以display role feature name aaa的显示字段为例）

字段

描述

Feature

特性名称以及功能简介

system-view ; domain \*

系统视图下以**domain**开头的所有命令，以及ISP域视图下的所有命令

system-view ; header \*

系统视图下以**header**开头的所有命令

system-view ; aaa \*

系统视图下以**aaa**开头的所有命令

display domain \*

用户视图下以**display domain**开头的所有命令

system-view ; user-group \*

系统视图下以**user-group**开头的所有命令，以及用户组视图下的所有命令

system-view ; local-user \*

系统视图下以**local-user**开头的所有命令，以及本地用户视图下的所有命令

display user-group \*

用户视图下以**display user-group**开头的所有命令

display debugging local-server

用户视图下以命令**display debugging local-server**开头的所有命令

debugging local-server \*

用户视图下以**debugging local-server**开头的所有命令

super \*

用户视图下以**super**开头的所有命令

display password-control \*

用户视图下以**display password-control**开头的所有命令

reset password-control \*

用户视图下以**reset password-control**开头的所有命令

system-view ; password-control \*

系统视图下以**password-control**开头的所有命令

(W)

命令行的类型为写命令

(R)

命令行的类型为读命令

(X)

命令行的类型为执行命令

【相关命令】

·**feature**

**RBAC \-- RBAC配置命令 \-- display role feature-group**

------------------------------------------------------------------------

**[display role feature-group**]命令用来显示特性组信息。

【命令】

**[display role feature-group ** **name** *feature-group-name* ]  **verbose**

【视图】

任意视图

【缺省用户角色】

network-admin

netword-operator

mdc-admin

mdc-operator

【参数】

**[name ***feature-group-name*]：显示指定特性组包含的特性名称列表。*feature-group-name*表示特性组名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则表示显示所有特性组的相关信息。

**[verbose**]：显示特性组的详细信息，即显示特性组内的特性所包含的命令行列表。如果不指定本参数，则表示显示特性组中的特性名称列表。

【举例】

![说明](RBAC命令.files/image001.png)

以下内容中涉及的特性、命令行均为示例，具体的显示信息与设备的实际情况有关，请以设备的实际情况为准。

\# 显示所有特性组内的特性名称列表。

\<Sysname\> display role feature-group

Feature group: L2

Feature: igmp-snooping   (IGMP-Snooping related commands)

Feature: mld-snooping    (MLD-Snooping related commands)

Feature: lacp            (LACP related commands)

Feature: stp             (STP related commands)

Feature: lldp            (LLDP related commands)

Feature: dldp            (DLDP related commands)

Feature: cfm             (CFM related commands)

Feature: eoam            (EOAM related commands)

Feature: loopbk-detect   (Loopback-detection related commands)

Feature: vlan            (Virtual LAN related commands)

Feature: evb             (EVB related commands)

Feature group: L3

Feature: route           (Route management related commands)

Feature: ospf            (Open Shortest Path First protocol related commands)

Feature: rip             (Routing Information Protocol related commands)

Feature: isis            (ISIS protocol related commands)

Feature: bgp             (Border Gateway Protocol related commands)

Feature: l3vpn           (Layer 3 Virtual Private Network related commands)

\# 显示所有特性组的详细信息。

\<Sysname\> display role feature-group verbose

Feature group: L2

Feature: igmp-snooping   (IGMP-Snooping related commands)

  system-view ; igmp-snooping    (W)

  system-view ; vlan \* ; igmp-snooping \*    (W)

  system-view ; interface \* ; igmp-snooping \*    (W)

  display igmp-snooping \*    (R)

  reset igmp-snooping \*    (W)

  debugging igmp-snooping \*    (W)

  display debugging igmp-snooping \*    (R)

Feature: mld-snooping    (MLD-Snooping related commands)

  system-view ; mld-snooping    (W)

  system-view ; vlan \* ; mld-snooping \*    (W)

  system-view ; interface \* ; mld-snooping \*    (W)

  display mld-snooping \*    (R)

  reset mld-snooping \*    (W)

  debugging mld-snooping \*    (W)

  display debugging mld-snooping \*    (R)

Feature group: L3

Feature: route           (Route management related commands)

  display ip routing-table \*    (R)

  display ipv6 routing-table \*    (R)

  display router id \*    (R)

  reset ip routing-table statistics \*    (W)

  reset ipv6 routing-table statistics \*    (W)

  debugging rm \*    (W)

  system-view ; ip route-static \*    (W)

  system-view ; ipv6 route-static \*    (W)

  system-view ; router id \*    (W)

  system-view ; delete static-routes \*    (W)

  system-view ; delete ipv6 static-routes \*    (W)

Feature: ospf            (Open Shortest Path First protocol related commands)

  display ospf \*    (R)

  display ospfv3 \*    (R)

  reset ospf \*    (W)

  debugging ospf \*    (W)

  debugging ospfv3 \*    (W)

  system-view ; ospf \*    (W)

  system-view ; interface \* ; ospf \*    (W)

  system-view ; ospfv3 \*    (W)

  system-view ; interface \* ; ospfv3 \*    (W)

Feature: rip             (Routing Information Protocol related commands)

  display rip \*    (R)

  display ripng \*    (R)

  debugging rip \*    (W)

  debugging ripng \*    (W)

  system-view ; rip \*    (W)

  system-view ; interface \* ; rip \*    (W)

  system-view ; ripng \*    (W)

  system-view ; interface \* ; ripng \*    (W)

Feature: isis            (ISIS protocol related commands)

  display isis \*    (R)

  reset isis \*    (W)

  debugging isis \*    (W)

  display debugging isis \*    (R)

  system-view ; isis \*    (W)

  system-view ; interface \* ; isis \*    (W)

Feature: bgp             (Border Gateway Protocol related commands)

  display bgp \*    (R)

  reset bgp \*    (W)

  refresh bgp \*    (W)

  debugging bgp \*    (W)

  system-view ; bgp \*    (W)

Feature: l3vpn           (Layer 3 Virtual Private Network related commands)

  display ip vpn-instance \*    (R)

  system-view ; ip vpn-instance \*    (W)

  system-view ; interface \* ; ip binding vpn-instance \*    (W)

\# 显示特性组L3的特性名称列表。

\<Sysname\> display role feature-group name L3

Feature group: L3

Feature: route           (Route management related commands)

Feature: ospf            (Open Shortest Path First protocol related commands)

Feature: rip             (Routing Information Protocol related commands)

Feature: isis            (ISIS protocol related commands)

Feature: bgp             (Border Gateway Protocol related commands)

Feature: l3vpn           (Layer 3 Virtual Private Network related commands)

表1-3 display role feature-group命令显示信息描述表

字段

描述

Feature group

特性组名称，其中L2和L3为系统预定义的两个特性组

Feature

特性名称以及功能简介

关于特性内具体命令的详细介绍请参考 表1-2(?444522080#_Ref285211276)

【相关命令】

·**feature**

·**role feature-group**

**RBAC \-- RBAC配置命令 \-- feature**

------------------------------------------------------------------------

**[feature**]命令用来向特性组中添加一个特性。

**[undo feature**]命令用来删除特性组中的某个特性。

【命令】

**[feature ***feature-name*]

**[undo feature ***feature-name*]

【缺省情况】

自定义特性组中不包括任何特性。

【视图】

特性组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[feature-name*]：系统支持的特性名称，所有特性名称中的字母均为小写。

【使用指导】

可通过多次执行本命令，向特性组中添加多个特性。

【举例】

\# 向特性组security-features中添加特性AAA和ACL。

\<Sysname\> system-view

Sysname role feature-group name security-features

Sysname-featuregrp-security-features feature aaa

Sysname-featuregrp-security-features feature acl

【相关命令】

·**display role feature**

·**display role feature-group**

·**role feature-group**

**RBAC \-- RBAC配置命令 \-- interface policy deny**

------------------------------------------------------------------------

**[interface policy deny**]命令用来进入接口策略视图。

**[undo interface policy deny**]命令用来恢复缺省情况。

【命令】

**[interface policy deny**]

**[undo interface policy deny**]

【缺省情况】

用户具有操作任何接口的权限。

【视图】

用户角色视图

【用户角色】

network-admin

mdc-admin

【使用指导】

进入接口策略视图后，如果不配置允许操作的接口列表，则用户将没有操作任何接口的权限；如果需要限制或区分用户对接口资源的使用权限，则还应该通过**permit interface**命令配置允许用户操作的接口列表。若接口策略视图中未配置允许操作的接口列表，则表示不允许用户操作所有的接口。对接口的操作指的是创建接口并进入接口视图、删除和应用接口。其中，创建和删除接口，仅针对逻辑接口。

允许修改用户角色的接口策略，但修改后的策略只在被授权该角色的用户重新登录时才会生效。

【举例】

\# 在用户角色role1中，进入接口策略视图，并禁止角色为role1的用户操作任何接口。

\<Sysname\> system-view

Sysname role name role1

Sysname-role-role1 interface policy deny

Sysname-role-role1-ifpolicy quit

\# 在用户角色role1中，进入接口策略视图，允许角色为role1的用户操作接口GigabitEthernet1/0/1到 GigabitEthernet1/0/5。

\<Sysname\> system-view

Sysname role name role1

Sysname-role-role1 interface policy deny

Sysname-role-role1-ifpolicy permit interface gigabitethernet 1/0/1 to gigabitethernet 1/0/5

【相关命令】

·{.ItemStepChar}**[display role**]{.ItemStepChar}

·**permit interface**

·**role**

**RBAC \-- RBAC配置命令 \-- permit interface**

------------------------------------------------------------------------

**[permit interface**]命令用来配置允许用户操作的接口列表。

**[undo permit interface**]命令用来禁止用户操作指定的或所有的接口。

【命令】

**[permit interface ***interface-list*]

**[undo permit interface **]\*[interface-list*****]

【缺省情况】

接口策略视图下未定义允许操作的接口列表，用户没有操作任何接口的权限。

【视图】

接口策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface*** interface-list*]：允许用户操作的接口列表，表示多个接口，表示方式为*interface-lis*t = { *interface-type* *interface-number* [ to *interface-type interface-number*  }&\<1-10\>]。其中，*interface-type*为接口类型，*interface-number*为接口编号。&\<1-10\>表示前面的参数最多可以输入10次。起始接口类型必须和终止接口类型一致，并且终止接口编号必须大于起始接口编号。如果不指定本参数，则表示指定所有接口。

【使用指导】

对接口的操作指的是创建并进入接口视图、删除和应用接口。其中，创建和删除接口，只针对逻辑接口。

可通过多次执行此命令向接口列表中添加允许用户操作的接口。

【举例】

\# 创建用户角色role1并进入其视图。

\<Sysname\> system-view

Sysname role name role1

\# 配置用户角色规则1，允许用户执行进入接口视图以及接口视图下的相关命令。

Sysname-role-role1 rule 1 permit command system-view ; interface \*

\# 配置用户角色规则2，允许用户执行创建VLAN以及进入VLAN视图后的相关命令。

Sysname-role-role1 rule 2 permit command system-view ; vlan \*

\# 配置用户角色role1仅可以对接口GigabitEthernet1/0/1以及 GigabitEthernet1/0/5～ GigabitEthernet1/0/7进行操作。

Sysname-role-role1 interface policy deny

Sysname-role-role1-ifpolicy permit interface gigabitethernet 1/0/1 gigabitethernet 1/0/5 to gigabitethernet 1/0/7

当拥有用户角色role1的用户登录设备后，可以操作接口GigabitEthernet1/0/1以及 GigabitEthernet1/0/5～GigabitEthernet1/0/7，但不能操作其它接口。

配置结果验证如下：

·进入接口GigabitEthernet1/0/1视图。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1

·将接口GigabitEthernet1/0/5加入到VLAN 10。

\<Sysname\> system-view

Sysname vlan 10

Sysname-vlan10 port gigabitethernet 1/0/5

·无法进入接口GigabitEthernet1/0/2视图。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/2

Permission denied.

【相关命令】

·{.ItemStepChar}**[display role**]{.ItemStepChar}

·**interface policy deny**

·**role**

**RBAC \-- RBAC配置命令 \-- permit security-zone**

------------------------------------------------------------------------

![说明](RBAC命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[permit security-zone**]命令用来配置允许用户操作的安全域列表。

**[undo permit security-zone**]命令用来禁止用户操作指定的或所有的安全域实例。

【命令】

**[permit security-zone **]*security-zone-name*&\<1-10\>

**[undo permit security-zone **]\*[security-zone-name*&\<1-10\>****]

【缺省情况】

安全域策略视图下未定义允许操作的安全域列表，用户没有操作任何安全域的权限。

【视图】

安全域策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[security-zone-name*&\<1-10\>]：表示允许用户操作的安全域的名称，为1～31个字符的字符串，区分大小写。&\<1-10\>表示前面的参数最多可以输入10次。如果不指定本参数，则表示指定所有安全域。

【使用指导】

对安全域的"操作"指的是创建安全域并进入其视图、删除和应用安全域。

可通过多次执行此本命令向安全域列表中添加允许用户操作的安全域。

【举例】

\# 创建用户角色role1并进入其视图。

\<Sysname\> system-view

Sysname role name role1

\# 配置用户角色规则1，允许用户执行系统视图下的所有命令以及所有子视图下的命令。

Sysname-role-role1 rule 1 permit command system-view ; \*

\# 配置用户角色role1仅可以对安全域trust和abc进行操作。

Sysname-role-role1 security-zone policy deny

Sysname-role-role1-zonepolicy permit security-zonetrust abc

拥有用户角色role1的用户登录设备后，可以操作安全域abc，但不能操作其它安全域。

配置结果验证如下：

·创建并进入名称为abc的安全域视图。

\<Sysname\> system-view

Sysname security-zone name abc

Sysname-security-zone-abc

·创建源安全域trust到目的安全域abc的域间实例。

\<Sysname\> system-view

Sysname interzone source trust destination abc

Sysname-interzone-Trust-abc

·无法创建名称为local的安全域或进入其视图。

\<Sysname\> system-view

Sysname security-zone name local

Permission denied.

【相关命令】

·{.ItemStepChar}**[display role**]{.ItemStepChar}

·**role**

·**security-zone policy deny**

**RBAC \-- RBAC配置命令 \-- permit vlan**

------------------------------------------------------------------------

**[permit vlan**]命令用来配置允许用户操作的VLAN列表。

**[undo permit vlan**]命令用来禁止用户操作指定的或所有的VLAN。

【命令】

**[permit vlan ***vlan-id-list*]

**[undo permit vlan **] *vlan-id-list*

【缺省情况】

VLAN接口视图下未定义允许操作的VLAN列表，用户没有操作任何VLAN的权限。

【视图】

VLAN策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id-list*]：允许用户操作的VLAN列表，表示方式为*vlan-id-list* = { *vlan-id1* [ to *vlan-id2*  }&\<1-10\>]，*vlan-id*取值范围为1～4094，&\<1-10\>表示前面的参数最多可以重复输入10次。终止VLAN编号必须大于起始VLAN编号。如果不指定本参数，则表示指定所有VLAN。

【使用指导】

对VLAN的操作指的是创建VLAN并进入VLAN视图、删除和应用VLAN。

可通过多次执行此命令向VLAN列表中添加允许用户操作的VLAN。

【举例】

\# 创建用户角色role1并进入其视图。

\<Sysname\> system-view

Sysname role name role1

\# 配置用户角色规则1，允许用户执行进入接口视图以及接口视图下的相关命令。

Sysname-role-role1 rule 1 permit command system-view ; interface \*

\# 配置用户角色规则2，允许用户执行创建VLAN以及进入VLAN视图后的相关命令。

Sysname-role-role1 rule 2 permit command system-view ; vlan \*

\# 配置用户角色role1仅可以操作VLAN 2、VLAN 4、VLAN 50～VLAN 100。

Sysname-role-role1 vlan policy deny

Sysname-role-role1-vlanpolicy permit vlan 2 4 50 to 100

当拥有用户角色role1的用户登录设备后，可以操作VLAN 2、VLAN 4、VLAN 50～VLAN 100，但不能操作其它VLAN。

配置结果验证如下：

·创建并进入VLAN 100视图。

\<Sysname\> system-view

Sysname vlan 100

Sysname-vlan100

·向VLAN 100中添加Access类型的端口GigabitEthernet1/0/1。

\<Sysname\> system-view

Sysname interfacegigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port access vlan 100

·无法创建VLAN 101或进入其视图。

\<Sysname\> system-view

Sysname vlan 101

Permission denied.

【相关命令】

·{.ItemStepChar}**[display role**]{.ItemStepChar}

·**role**

·**vlan policy deny**

**RBAC \-- RBAC配置命令 \-- permit vpn-instance**

------------------------------------------------------------------------

**[permit vpn-instance**]命令用来配置允许用户操作的VPN列表。

**[undo permit vpn-instance**]命令用来禁止用户操作指定的或所有的VPN实例。

【命令】

**[permit vpn-instance **]*vpn-instance-name*&\<1-10\>

**[undo permit vpn-instance **]\*[vpn-instance-name*&\<1-10\>****]

【缺省情况】

VPN策略视图下未定义允许操作的VPN列表，用户没有操作任何VPN的权限。

【视图】

VPN策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vpn-instance-name*&\<1-10\>]：表示允许用户操作的MPLS L3VPN实例的名称，为1～31个字符的字符串，区分大小写。&\<1-10\>表示前面的参数最多可以输入10次。如果不指定本参数，则表示指定所有MPLS L3VPN实例。

【使用指导】

对VPN实例的"操作"指的是创建MPLS L3VPN实例并进入其视图、删除和应用VPN实例。

可通过多次执行此命令向接口列表中添加允许用户操作的VPN实例。

【举例】

\# 创建用户角色role1并进入其视图。

\<Sysname\> system-view

Sysname role name role1

\# 配置用户角色规则1，允许用户执行系统视图下的所有命令以及所有子视图下的命令。

Sysname-role-role1 rule 1 permit command system-view ; \*

\# 配置用户角色role1仅可以对VPN实例vpn1进行操作。

Sysname-role-role1 vpn policy deny

Sysname-role-role1-vpnpolicy permit vpn-instance vpn1

拥有用户角色role1的用户登录设备后，可以操作VPN实例vpn1，但不能操作其它VPN实例。

配置结果验证如下：

·进入名称为vpn1的VPN实例视图。

\<Sysname\> system-view

Sysname ip vpn-instance vpn1

Sysname-vpn-instance-vpn1

·设置RADIUS方案radius1的主计费服务器的IP地址为10.110.1.2，且属于VPN实例vpn1。

\<Sysname\> system-view

Sysname radius scheme radius1

Sysname-radius-radius1 primary accounting 10.110.1.2 vpn-instance vpn1

·无法创建名称为vpn2的VPN实例或进入其视图。

\<Sysname\> system-view

Sysname ip vpn-instance vpn2

Permission denied.

【相关命令】

·{.ItemStepChar}**[display role**]{.ItemStepChar}

·**role**

·**vpn-instance policy deny**

**RBAC \-- RBAC配置命令 \-- role**

------------------------------------------------------------------------

**[role**]命令用来创建用户角色，并进入用户角色视图。

**[undo role**]命令用来删除指定的用户角色。

【命令】

**[role** **name** *role-name*]

**[undo role name*** role-name*]

【缺省情况】

系统预定义的用户角色为network-admin、network-operator、mdc-admin、mdc-operator、context-admin、context-operator、level-*n*（*n*为0～15的整数）、security-audit。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[name*** role-name*]：用户角色名称，*role-name*为1～63个字符的字符串，区分大小写。

【使用指导】

除系统预定义的缺省用户角色之外，系统中最多允许创建64个用户角色。

缺省的用户角色不能被删除，而且其中的network-admin、network-operator、mdc-admin、mdc-operator、context-admin、context-operator、level-15、security-audit这些用户角色内定义的所有权限均不能被修改；用户角色level-0～level-14可以通过自定义规则和资源控制策略调整自身的权限，但这种修改对于**display history-command all**命令不生效，即不能通过添加对应的规则来更改它的缺省执行权限。

【举例】

\# 创建用户角色role1，并进入用户角色视图。

\<Sysname\> system-view

Sysname role name role1

Sysname-role-role1

【相关命令】

·{.ItemStepChar}**[display role**]{.ItemStepChar}

·**interface policy deny**

·**rule**

·**vlan policy deny**

·**vpn-instance policy deny**

**RBAC \-- RBAC配置命令 \-- role default-role enable**

------------------------------------------------------------------------

**[role default-role enable**]命令用来使能缺省用户角色授权功能。

**[undo role default-role enable**]命令用来恢复缺省情况。

【命令】

**[role default-role enable**]

**[undo role default-role enable**]

【缺省情况】

缺省用户角色授权功能处于关闭状态，没有被AAA授权用户角色的用户不能登录设备。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

对于通过AAA认证登录设备的用户，由AAA服务器（远程认证）或设备（本地认证）为其授权对应的用户角色。如果用户没有被授权任何用户角色，将无法成功登录设备。使能该功能后，用户将在没有被授权任何用户角色的情况下，具有一个缺省的用户角色，具体情况如下：（不同设备的具体情况有所不同，请以设备的实际情况为准）

·如果用户登录设备，缺省用户角色为network-operator；

·如果用户登录于缺省MDC，则缺省用户角色为network-operator；

·如果用户登录于非缺省MDC，则缺省用户角色为mdc-operator；

·如果用户登录于缺省Context，则缺省用户角色为context-operator；

·如果用户登录于非缺省Context，则缺省用户角色为context-operator。

若用户通过AAA认证且被授予了具体的用户角色，则用户不具有以上缺省的用户角色。

【举例】

\# 使能缺省用户角色授权功能。

\<Sysname\> system-view

Sysname role default-role enable

【相关命令】

·**role**

**RBAC \-- RBAC配置命令 \-- role feature-group**

------------------------------------------------------------------------

**[role feature-group**]命令用来创建特性组并进入特性组视图。

**[undo role feature-group**]命令用来删除指定的特性组。

【命令】

**[role feature-group name ***feature-group-name*]

**[undo role feature-group name ***feature-group-name*]

【缺省情况】

存在两个特性组，名称分别为L2和L3。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[name ***feature-group-name*]：特性组名称，*feature-group-name*为1～31个字符的字符串，区分大小写。

【使用指导】

除系统预定义的特性组L2和L3之外，系统中最多允许创建64个特性组。

不能修改和删除系统预定义的特性组L2和L3。L2中包含了所有的二层协议相关功能的命令，L3中包含了所有三层协议相关功能的命令。

【举例】

\# 创建特性组security-features。

\<Sysname\> system-view

Sysname role feature-group name security-features

Sysname-featuregrp-security-features

【相关命令】

·**display role feature**

·**display role feature-group**

·**feature**

**RBAC \-- RBAC配置命令 \-- rule**

------------------------------------------------------------------------

**[rule**]命令用来为用户角色创建一条规则。

**[undo rule**]命令用来为用户角色删除一条规则。

【命令】

**[rule**[ *number* { **deny** \| **permit** } { **command** *command-string \|* { **execute** \| **read** \| **write** } \* ]**oid** [ *oid-string*   \| **web-menu** [ *web-string* ] \| **xml-element**  *xml-string*  } }]

**[undo rule**[ { *number* \| **all** }]]

【缺省情况】]

新创建的用户角色中未定义规则，即当前用户角色无任何权限。

【视图】

用户角色视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：权限规则编号，取值范围为1～256。

**[deny**]：禁止执行指定的命令。

**[permit**]：允许执行指定的命令。

**[command ***command-string*]：配置基于命令的规则。*command-string*表示命令特征字符串，为1～128个字符的字符串，区分大小写，可以是特定的一条命令行，也可以是用星号（\*）通配符表示的一批命令，可包含空格、Tab（它们用于分隔关键字、参数以及输入的字符），以及所有可打印字符。

**[execute**]：表示执行类型的命令，即用于执行特定的程序或功能的一类命令，如**ping**命令。

**[read**]：表示读类型的命令，即显示系统配置和维护信息的一类命令，如**display**、**dir**、**more**和**pwd**命令。

**[write**]：表示写类型的命令，即用于对系统进行配置的一类命令，如**ssh server enable**命令。

**[feature ** *feature-name* ]：配置基于特性的规则。*feature-name*表示系统预定义的特性名称，区分大小写。若不指定特性名称，则表示所有特性。

**[feature-group** *feature-group-name*]：配置基于特性组的规则。*feature-group-name*表示特性组名称，为1～31个字符的字符串，区分大小写。

**[oid **]*oid-string* ：配置基于MIB节点OID（Object Identifier，对象标识符）的规则。*oid-string*表示允许操作的OID，为1～255个字符的字符串，不区分大小写。例如：1.3.6.1.4.1.25506.8.35.14.19.1.1。

**[web-menu** [ *web-string* ]]：配置基于Web菜单的规则。*web-string*表示允许操作的Web菜单选项的ID路径，为1～255个字符的字符串，不区分大小写，以"/"为分隔符来分隔不同级别的菜单。合法的*web-string*为通过**display web menu**命令显示的ID路径,例如：M_DEVICE/I_BASIC_INFO/I_reboot；若不指定*web-string*参数，则表示对所有菜单选项生效。

**[xml-element ** *xml-string* ]：配置基于XML元素的规则。*xml-string*表示允许操作的XML元素的XPath，为1～255个字符的字符串，不区分大小写，以"/"为分隔符来分隔不同级别的菜单，例如：Interfaces/Index/Name；若不指定*xml-string*参数，则表示对所有XML元素生效。

**[all**]：指定所有权限规则。

【使用指导】

可为一个用户角色定义以下几种类型的规则：

·禁止或允许执行特定的命令行。

·禁止或允许执行指定或所有特性的某一类或某几类命令。

·禁止或允许执行某个特性组中所有特性的某一类或某几类命令。

·禁止或允许执行指定所有或指定的MIB节点OID。

·禁止或允许执行Web页面中所有菜单选项或某几类菜单选项。

·禁止或允许执行所有XML元素或某几类XML元素。

需要注意的是：

· 执行本命令时，如果指定编号的规则不存在，则表示创建一条新的规则；如果指定编号的规则已存在，则表示对已有的规则进行修改。{.ItemStepChar}修改后的规则对于当前已经在线的用户不生效，对于之后使用该角色登录设备的用户生效。

·{.ItemStepChar}一个用户角色中允许创建多条规则，各规则以创建时指定的编号为唯一标识，被授权该角色的用户可以执行的命令为这些规则定义的可执行命令的并集。若这些规则定义的权限内容有冲突，则规则编号大的有效。例如，规则1允许执行命令A，规则2允许执行命令B，规则3禁止执行命令A，则最终规则2和规则3生效，即禁止执行命令A，允许执行命令B。{.ItemStepChar}

·{.ItemStepChar}[在同时存在系统预定义规则（以]{.ItemStepChar}sys-x{.ItemStepChar}为权限规则编号，{.ItemStepChar}x{.ItemStepChar}为整数值）和自定义规则的用户角色中，若预定义规则定义的权限内容与自定义规则定义的权限内容有冲突，则以自定义规则为准。{.ItemStepChar}

·每个用户角色中最多可以配置256条规则，系统中可以配置的用户角色规则总数不能超过1024。

·访问文件系统的命令，受基于文件系统特性规则以及具体命令规则的双重控制。

·对于需要将输出信息重定向到文件中保存的命令，只有在用户角色被授权了文件系统写权限后才允许执行。

输入命令特征字符串时，需要遵循以下规则：

(1)段（segment）的划分

·若要描述多级视图下的命令，则需要使用分号（;）将命令特征字符串分成多个段，每一个段代表一个或一系列命令，后一个段中的命令是执行前一个段中命令所进入视图下的命令。一个段中可以包含多个星号（\*），每个星号（\*）代表了0个或多个任意字符。例如：命令特征字符串"system ; interface \* ; ip \* ;"代表从系统视图进入到任意接口视图后，以**ip**开头的所有命令。

·除最后一个段外，其余段中的命令应为描述如何进入子视图的命令特征字符串。

·一个段中必须至少出现一个可打印字符，不能全部为空格或Tab。

(2)分号的使用

·在输入命令特征字符串时必须指定该命令所在的视图，进入各视图的命令特征字符串由分号分隔。但是，对于能在任意视图下执行的命令（例如**display**命令）以及用户视图下的命令（例如**dir**命令），在配置包含此类命令的规则时，不需要在规则的命令匹配字符串中指定其所在的视图。

·当最后一个段中的最后一个可见字符为分号时，表示所指的命令范围不再扩展，否则将向子视图中的命令扩展。例如：命令特征字符串"system ; radius scheme \* ;"代表系统视图下以**radius scheme**开头的所有命令；命令特征字符串"system ; radius scheme \* "代表系统视图下以**radius scheme**开头的所有命令，以及进入子视图（RADIUS方案视图）下的所有命令。

(3)星号的使用

·当星号（\*）出现在一个段的首部时，其后面不能再出现其它可打印字符，且该段必须是命令特征字符串的最后一个段。例如：命令特征字符串"system ; \*"就代表了系统视图下的所有命令，以及所有子视图下的命令。

·当星号（\*）出现在一个段的中间时，该段必须是命令特征字符串的最后一个段。例如：命令特征字符串"debugging \* event"就代表了用户视图下所有模块的事件调试信息开关命令。

(4)前缀匹配

·命令关键字与命令特征字符串是采用前缀匹配算法进行匹配的，即只要命令行中关键字的首部若干连续字符或全部字符与规则中定义的关键字相匹配，就认为该命令行与此规则匹配。因此，命令特征字符串中可以包括完整的或部分的命令关键字。例如，若规则"rule 1 deny command dis mpls lsp protocol static asbr"生效，则命令**display mpls lsp protocol static asbr**和命令**display mpls lsp protocol static-cr asbr**都会被禁止执行。

对于基于命令的规则，有以下使用注意事项：

·基于命令的规则只对指定视图下的命令生效。若用户输入的命令在当前视图下不存在而在其父视图下被查找到时，用于控制当前视图下的命令的规则不会对其父视图下的命令执行权限进行控制。例如，定义一条规则"rule 1 deny command system ; interface \* ; \*"禁止用户执行接口视图下的任何命令。当用户在接口视图下输入命令**acl number **3000时，该命令仍然可以成功执行，因为系统在接口视图下搜索不到指定的**acl**命令时，会回溯到系统视图（父视图）下执行，此时该规则对此命令不生效。

·**display**命令中的重定向符（"[\|]"、"\>"、"\>\>"）及其后面的关键字不被作为命令行关键字参与规则的匹配。例如，若规则"rule 1 permit command display debugging"生效，则命令**display debugging \> log**是被允许执行的，其中的关键字**\> log**将被忽略，RBAC只对重定向符前面的命令行**display debugging**进行匹配。但是，如果在规则中配置了重定向符，则RBAC会将其作为普通字符处理。例如，若规则"rule 1 permit command display debugging \> log"生效，则命令**display debugging \> log**将会匹配失败，因为其中的关键字**\> log**被RBAC忽略了，最终是命令**display debugging**与规则进行匹配。因此，配置规则时不要使用重定向符。

进行基于OID的规则的匹配时，遵循以下规则：

·与用户访问的OID形成最长匹配的规则生效。例如用户访问的OID为1.3.6.1.4.1.25506.141.3.0.1，角色中存在"rule 1 permit read write oid 1.3.6"，"rule 2 deny read write oid 1.3.6.1.4.1"和"rule 3 permit read write oid 1.3.6.1.4"，其中rule 2与用户访问的OID形成最长匹配，则认为rule 2与OID匹配，匹配的结果为用户的此访问请求被拒绝。

·对于定义的OID长度相同的规则，规则编号大的生效。例如用户访问的OID为1.3.6.1.4.1.25506.141.3.0.1，角色中存在"rule 1 permit read write oid 1.3.6"，"rule 2 deny read write oid 1.3.6.1.4.1"和"rule 3 permit read write oid 1.3.6.1.4.1"，其中rule 2和rule 3与访问的OID形成最长匹配，则rule 3生效，匹配的结果为用户的访问请求被允许。

【举例】

\# 为用户角色role1创建一条规则，允许用户执行命令**display acl**。

\<Sysname\> system-view

Sysname role name role1

Sysname-role-role1 rule 1 permit command display acl

\# 为用户角色role1添加一条权限规则，允许用户执行所有以**display**开头的命令。

Sysname-role-role1 rule 2 permit command display \*

\# 为用户角色role1添加一条权限规则，允许用户执行系统视图下的**radius scheme aaa**命令，以及使用该命令进入子视图后的所有命令。

Sysname-role-role1 rule 3 permit command system ; radius scheme aaa

\# 为用户角色role1添加一条权限规则，禁止用户执行所有特性中读类型和写类型的命令。

Sysname-role-role1 rule 4 deny read write feature

\# 为用户角色role1添加一条权限规则，禁止用户执行特性aaa中所有读类型的命令。

Sysname-role-role1 rule 5 deny read feature aaa

\# 为用户角色role1添加一条权限规则，允许执行特性组security-features中所有特性的读类型、写类型以及执行类型的命令。

Sysname-role-role1 rule 6 permit read write execute feature-group security-features

\# 为用户角色role1添加一条基于OID的规则，允许对OID为1.1.2的MIB节点进行读、写操作。

Sysname-role-role1 rule 7 permit read write oid 1.1.2

【相关命令】

·{.ItemStepChar}**[display role**]{.ItemStepChar}

·{.ItemStepChar}**[display role feature**]{.ItemStepChar}

·{.ItemStepChar}**[display role feature-group**]{.ItemStepChar}

·**display web menu**(基础配置命令参考/登录设备)

·**role**

**RBAC \-- RBAC配置命令 \-- super**

------------------------------------------------------------------------

**[super**]命令用来使用户从当前角色切换到指定的用户角色。

【命令】

**[super ** *rolename* ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[rolename*]：待切换的用户角色名称，为1～63个字符的字符串，区分大小写，可以是系统中已存在的任意用户角色。若不指定本参数，则表示要从当前用户角色切换到用户角色network-admin。（不支持MDC、Context的设备）。若不指定本参数，则切换到当前缺省的目的用户角色。缺省的目的用户角色由**super default role**命令指定。

【使用指导】

为了保证操作的安全性，通常用户进行用户角色切换时，均需要输入用户角色切换密码。切换到不同的用户角色时，需要输入相应切换密码。如果服务器没有响应或者没有配置用户角色切换密码，则切换操作失败，若还有备份认证方案，则转而进行备份认证。因此，在进行切换操作前，请先保证配置了正确的用户角色切换密码。

需要注意的是：

·若级别切换认证方式为**local**，在设备上未配置切换密码的情况下，对于Console/AUX用户，设备不关心用户是否输入切换密码以及输入切换密码的内容，可允许用户成功切换用户角色。

·若级别切换认证方式为**local scheme**，在设备上未配置切换密码的情况下，对于Console、TTY或VTY用户，则转为远程AAA认证；对于AUX用户，设备不关心用户是否输入切换密码以及输入切换密码的内容，可允许用户成功切换用户角色。

【举例】

\# 将用户角色切换到network-operator。（假设用户当前的角色为network-admin，切换认证方式为local，切换密码已经设置）

\<Sysname\> super network-operator

Password:

User privilege role is network-operator, and only those commands can be used that authorized to the role.

【相关命令】

·**authentication super**（安全命令参考/AAA）

·**super authentication-mode**

·**super password**

**RBAC \-- RBAC配置命令 \-- super authentication-mode**

------------------------------------------------------------------------

**[super authentication-mode**]命令用来设置切换用户角色时使用的认证方式。

**[undo super authentication-mode**]命令用来恢复缺省情况。

【命令】

**[super authentication-mode **[{ **local** \| **scheme** } \*]]

**[undo super authentication-mode**]

【缺省情况】

采用**local**认证方式。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[local**]：使用本地配置的用户角色切换密码进行认证。

**[scheme**]：使用AAA配置进行认证。该方式下，设备将用户角色切换时使用的用户名和密码发送给HWTACACS/RADIUS服务器进行远程验证。

【使用指导】

用户可以选择使用**local**或者**scheme**方式认证，也可以同时选择**local**和**scheme**方式，多选时根据配置顺序依次认证，例如**scheme local**方式，会先进行**scheme**方式认证，如果认证服务器没有响应，则转为采用**local**方式认证。**scheme**认证方式需要与AAA 的认证方案相配合，具体请参考"安全配置指导"中的"AAA"。

【举例】

\# 配置切换用户角色时采用**local**认证方式。

\<Sysname\> system-view

Sysname super authentication-mode local

\# 配置切换用户角色时采用先**scheme**后**local**的认证方式。

\<Sysname\> system-view

Sysname super authentication-mode scheme local

【相关命令】

·**authentication super**（安全命令参考/AAA）

·**super password**

**RBAC \-- RBAC配置命令 \-- super default role**

------------------------------------------------------------------------

**[super default role**]命令用来配置用户角色切换的缺省目的角色。

**[undo super default role**]命令用来恢复缺省情况。

【命令】

**[super default role ***rolename*]

**[undo super default role**]

【缺省情况】

用户角色切换的缺省目的角色为network-admin。（不支持MDC、Context的设备）

对于登录缺省MDC的用户，用户角色切换的缺省目的角色为network-admin；对于登录非缺省MDC的用户，用户角色切换的缺省目的角色为mdc-admin。（支持MDC的设备）

对于登录缺省Context的用户，用户角色切换的缺省目的角色为network-admin；对于登录非缺省Context的用户，用户角色切换的缺省目的角色为context-admin.（支持Context的设备）

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[rolename*]：待切换的用户角色名称，为1～63个字符的字符串，区分大小写，可以是系统中已存在的任意用户角色。

【使用指导】

当执行**super**命令切换用户角色时，或配置用户角色切换的密码时，如不指定目的切换的角色名称，则表示使用**super default role**命令配置的缺省用户角色。

【举例】

\# 配置用户切换角色的缺省目的角色为network-operator。

\<Sysname\> system-view

Sysname super default role network-operator

【相关命令】

·**super**

·**super password**

**RBAC \-- RBAC配置命令 \-- super password**

------------------------------------------------------------------------

**[super password**]命令用来设置用户角色切换的密码。

**[undo super password**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[super password **[ **role** *rolename*  [ { **hash** \| **simple** } *password* ]]]

**[undo super password** [ **role** *rolename* ]]

FIPS模式下：

**[super password ** **role** *rolename* ]

**[undo super password** [ **role** *rolename* ]]

【缺省情况】

未设置用户角色切换密码。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[role*** rolename*]：待切换的用户角色的名称，为1～63个字符的字符串，区分大小写，可以为系统预定义或用户自定义的用户角色。如果不指定角色名称，则表示设置的是切换到用户角色network-admin的密码。（不支持MDC、Context的设备）。如果不指定角色名称，则表示设置的是切换到当前缺省目的用户角色的密码。缺省的目的用户角色由**super default role**命令指定。

**[hash**]：表示以哈希方式设置用户密码。

**[simple**]：表示以明文方式设置用户密码。

*[password*]：设置的明文密码或哈希密码，区分大小写。非FIPS模式下，明文密码为1～63个字符的字符串；哈希密码为1～110个字符的字符串；FIPS模式下，密码为15～63个字符的字符串，密码元素的最少组合类型为4（必须包括数字、大写字母、小写字母以及特殊字符）。

【使用指导】

如果不指定任何参数，则表示以交互式方式设置本地用户密码，涵义与指定**simple**关键字相同。FIPS模式下，只支持交互式方式设置用户角色切换密码。

以明文方式设置的密码，以哈希计算后的密文形式保存在配置文件中，以哈希方式设置的密码将以设置的原始形式保存在配置文件中。

当用户切换认证方式为**local**或包含**local**（**local scheme**、**scheme local**）时，才需要本命令指定的用户角色切换密码。

为保证权限控制更加安全，推荐给不同的用户角色指定不同的切换密码。

【举例】

\# 配置将用户角色切换到network-operator时使用的密码为明文密码123456TESTplat&!。

\<Sysname\> system-view

Sysname super password role network-operator simple 123456TESTplat&!

\# 以交互式方式设置将用户角色切换到network-operator时使用的密码为明文密码123456TESTplat&!。

\<Sysname\> system-view

Sysname super password role network-operator

Password:

Confirm :

Updating user information. Please wait\... \...

【相关命令】

·**super authentication-mode**

·**super default role**

**RBAC \-- RBAC配置命令 \-- security-zone policy deny**

------------------------------------------------------------------------

![说明](RBAC命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[security-zone policy deny**]命令用来进入安全域策略视图。

**[undo security-zone policy deny**]命令用来恢复缺省情况。

【命令】

**[security-zone policy deny**]

**[undo security-zone policy deny**]

【缺省情况】

用户具有操作任何安全域的权限。

【视图】

用户角色视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

进入安全域策略视图后，如果不配置允许操作的安全域列表，则用户将没有操作任何安全域的权限；如果需要限制或区分用户对安全域资源的使用权限，则还应该通过**permit security-zone**命令配置允许用户操作的安全域列表。若安全域策略视图中未配置允许操作的安全域列表，则表示不允许用户操作所有的安全域。对安全域的"操作"指的是创建并进入安全域视图、删除和应用安全域。

允许修改用户角色的安全域策略，但修改后的策略只对被授权该角色的用户重新登录时才会生效。

【举例】

\# 在用户角色role1中，进入安全域策略视图，禁止角色为role1的用户操作任意安全域。

\<Sysname\> system-view

Sysname role name role1

Sysname-role-role1 security-zone policy deny

Sysname-role-role1-zonepolicy quit

\# 在用户角色role1中，进入安全域策略视图，允许角色为role1的用户操作安全域trust和abc。

\<Sysname\> system-view

Sysname role name role1

Sysname-role-role1 security-zone policy deny

Sysname-role-role1-zonepolicy permit security-zone trust abc

【相关命令】

·{.ItemStepChar}**[display role**]{.ItemStepChar}

·**permit security-zone**

·**role**

**RBAC \-- RBAC配置命令 \-- vlan policy deny**

------------------------------------------------------------------------

**[vlan policy deny**]命令用来进入VLAN策略视图。

**[undo vlan policy deny**]命令用来恢复缺省情况。

【命令】

**[vlan policy deny**]

**[undo vlan policy deny**]

【缺省情况】

用户具有操作任何VLAN的权限。

【视图】

用户角色视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

进入VLAN策略视图后，如果不配置允许操作的VLAN列表，则用户将没有操作任何VLAN的权限；如果需要限制或区分用户对VLAN资源的使用权限，则还应该通过**permit vlan**命令配置允许用户操作的VLAN列表。若VLAN策略视图中未配置允许操作的VLAN列表，则表示不允许用户操作所有的VLAN。对VLAN的"操作"指的是创建并进入VLAN视图、删除和应用VLAN。

允许修改用户角色的VLAN策略，但修改后的策略只对被授权该角色的用户重新登录时才会生效。

【举例】

\# 在用户角色role1中，进入VLAN策略视图，禁止角色为role1的用户操作任意VLAN。

\<Sysname\> system-view

Sysname role name role1

Sysname-role-role1 vlan policy deny

Sysname-role-role1-vlanpolicy quit

\# 在用户角色role1中，进入VLAN策略视图，允许角色为role1的用户操作VLAN 50～VLAN 100。

\<Sysname\> system-view

Sysname role name role1

Sysname-role-role1 vlan policy deny

Sysname-role-role1-vlanpolicy permit vlan 50 to 100

【相关命令】

·{.ItemStepChar}**[display role**]{.ItemStepChar}

·**permit vlan**

·**role**

**RBAC \-- RBAC配置命令 \-- vpn-instance policy deny**

------------------------------------------------------------------------

**[vpn-instance policy deny**]命令用来进入VPN策略视图。

**[undo vpn-instance policy deny**]命令用来恢复缺省情况。

【命令】

**[vpn-instance policy deny**]

**[undo vpn-instance policy deny**]

【缺省情况】

用户具有操作任何VPN实例的权限。

【视图】

用户角色视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

进入VPN策略视图后，如果不配置允许操作的VPN列表，则用户将没有操作任何VPN实例的权限；如果需要限制或区分用户对VPN资源的使用权限，则还应该通过**permit vpn-instance**命令配置允许用户操作的VPN列表。若VPN策略视图中未配置允许操作的VPN列表，则表示不允许用户操作所有的VPN实例。对VPN实例的"操作"指的是创建并进入MPLS L3VPN视图、删除和应用VPN实例。

允许修改用户角色的VPN策略，但修改后的策略只对被授权该角色的用户重新登录时才会生效。

【举例】

\# 在用户角色role1中，创建并进入一个VPN策略视图，并禁止角色为role1的用户操作任意VPN实例。

\<Sysname\> system-view

Sysname role name role1

Sysname-role-role1 vpn-instance policy deny

Sysname-role-role1-vpnpolicy quit

\# 在用户角色role1中，创建并进入一个VPN策略视图，允许角色为role1的用户操作VPN实例vpn2。

\<Sysname\> system-view

Sysname role name role1

Sysname-role-role1 vpn-instance policy deny

Sysname-role-role1-vpnpolicy permit vpn-instance vpn2

【相关命令】

·{.ItemStepChar}**[display role**]{.ItemStepChar}

·**permit vpn-instance**

·**role**

