::: {#1188054656 .myid}
[]{#_Toc404796930}[]{#struct_0_x1400_15709_1906380415}

**SNMP \-- SNMP配置命令 \-- display snmp-agent community**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **snmp-agent** **community**]{lang="EN-US"}]{#struct_0_x1400_15709_1325868046}[命令用来显示]{style="font-family:宋体"}[SNMPv1]{lang="EN-US"}[或]{style="font-family:宋体"}[SNMPv2c]{lang="EN-US"}[的团体信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_499963828}

[**[display]{lang="EN-US"}**[ **snmp-agent** **community** \[ **read** \| **write** \]]{lang="EN-US"}]{#struct_0_x1400_15709_1520279440}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_974030602}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_x944658852}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1466386837}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x723613523}

[[network-operator]{lang="EN-US"}]{#struct_0_x1400_15709_1897160552}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x2013505389}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1400_15709_x1924870542}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1559224866}

[**[read]{lang="EN-US"}**]{#struct_0_x1400_15709_515827022}[：显示只读访问权限的团体信息。]{style="font-family:宋体"}

[**[write]{lang="EN-US"}**]{#struct_0_x1400_15709_974096138}[：显示读写访问权限的团体信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1373972647}

[[FIPS]{lang="EN-US"}]{#struct_0_x1400_15709_1008267756}[模式下，不支持本命令。]{style="font-family:宋体"}

[[不带参数时，显示所有]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_1631224320}[团体的信息。]{style="font-family:宋体"}

[[用户可以使用]{style="font-family:宋体"}**[snmp-agent]{lang="EN-US"}**[ **community**]{lang="EN-US"}]{#struct_0_x1400_15709_849363694}[命令来创建团体，另外，配置]{style="font-family:宋体"}**[snmp-agent]{lang="EN-US"}**[ **usm-user** { **v1** \| **v2c** }]{lang="EN-US"}[和]{style="font-family:宋体"}**[snmp-agent]{lang="EN-US"}**[ **group** { **v1** \| **v2c** }]{lang="EN-US"}[命令成功创建]{style="font-family:宋体"}[SNMPv1]{lang="EN-US"}[或]{style="font-family:宋体"}[SNMPv2c]{lang="EN-US"}[用户以及相应的组后，系统会自动添加一个新的同名的只读团体名。]{style="font-family:宋体"}**[display]{lang="EN-US"}**[ **snmp-agent** **community**]{lang="EN-US"}[会显示这两种方式创建的团体的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1368546094}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_x1141698860}[显示设备当前所有已配置的团体信息。]{style="font-family:宋体"}

[[\<Sysname\> display snmp-agent community]{lang="EN-US"}]{#struct_0_x1400_15709_973113098}

[   Community name: aa]{lang="EN-US"}

[       Group name: aa]{lang="EN-US"}

[       ACL:2001]{lang="EN-US"}

[       Storage-type: nonVolatile]{lang="EN-US"}

[       Context name: con1]{lang="EN-US"}

[ ]{lang="EN-US"}

[   Community name: bb]{lang="EN-US"}

[       Role name: bb]{lang="EN-US"}

[       Storage-type: nonVolatile]{lang="EN-US"}

[ ]{lang="EN-US"}

[   Community name: userv1]{lang="EN-US"}

[       Group name: testv1]{lang="EN-US"}

[       Storage type: nonVolatile]{lang="EN-US"}

[ ]{lang="EN-US"}

[   Community name: cc]{lang="EN-US"}

[       Group name: cc]{lang="EN-US"}

[       ACL name: testacl]{lang="EN-US"}

[       Storage type: nonVolatile]{lang="EN-US"}

[]{#struct_0_x1400_15709_1039545099}[[表1-1 ]{lang="EN-US"}[display snmp-agent community]{lang="EN-US"}]{#_Ref291745733}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1563467589}[[字段]{style="font-family:黑体"}]{#struct_0_x1400_15709_1893911930}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1730551062}

[[Community name]{lang="EN-US"}]{#struct_0_x1400_15709_x748738585}

[[团体名：]{style="font-family:宋体"}]{#struct_0_x1400_15709_1573041744}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果团体是通过]{lang="EN-US" style="font-family:宋体"}**[snmp-agent]{lang="EN-US"}**[ **community**]{lang="EN-US"}]{#struct_0_x1400_15709_973178634}[命令创建的，则显示的是团体名]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果团体名是通过]{lang="EN-US" style="font-family:宋体"}**[snmp-agent]{lang="EN-US"}**[ **usm-user** { **v1** \| **v2c** }]{lang="EN-US"}]{#struct_0_x1400_15709_1812220327}[命令创建的，则显示的是用户名]{lang="EN-US" style="font-family:宋体"}

[[Group name]{lang="EN-US"}]{#struct_0_x1400_15709_x56228507}

[[组名：]{style="font-family:宋体"}]{#struct_0_x1400_15709_x880842845}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果团体名是通过]{lang="EN-US" style="font-family:宋体"}**[snmp-agent]{lang="EN-US"}**[ **community**]{lang="EN-US"}]{#struct_0_x1400_15709_x194814924}[命令]{lang="EN-US" style="font-family:
  宋体"}[的]{style="font-family:宋体"}[VACM]{lang="EN-US"}[方式]{style="font-family:宋体"}[创建的，则组名和团体名相同]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果团体名是通过]{lang="EN-US" style="font-family:宋体"}**[snmp-agent]{lang="EN-US"}**[ **usm-user** { **v1** \| **v2c** }]{lang="EN-US"}]{#struct_0_x1400_15709_x1822623465}[命令创建的，则显示用户所在的组名]{lang="EN-US" style="font-family:宋体"}

[[Role name]{lang="EN-US"}]{#struct_0_x1400_15709_388967996}

[[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_1950367483}[用户所在团体绑定的角色名：]{style="font-family:宋体"}

[[通过]{style="font-family:宋体"}**[snmp-agent]{lang="EN-US"}**[ **community**]{lang="EN-US"}]{#struct_0_x1400_15709_2083386607}[命令的]{style="font-family:宋体"}[RBAC]{lang="EN-US"}[方式创建的团体名可绑定用户角色]{style="font-family:宋体"}

[[ACL]{lang="EN-US"}]{#struct_0_x1400_15709_973637383}

[[使用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x1400_15709_1822795741}[列表的编号（该字段仅在团体名与]{style="font-family:宋体"}[ACL]{lang="EN-US"}[绑定后显示，不会与]{style="font-family:宋体"}[ACL name]{lang="EN-US"}[同时存在）]{style="font-family:宋体"}

[[ACL name]{lang="EN-US"}]{#struct_0_x1400_15709_1542968247}

[[使用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x1400_15709_x586094710}[列表的名称（该字段仅在团体名与]{style="font-family:宋体"}[ACL]{lang="EN-US"}[名称绑定后显示，不会与]{style="font-family:宋体"}[ACL]{lang="EN-US"}[同时存在）]{style="font-family:宋体"}

[[Storage type]{lang="EN-US"}]{#struct_0_x1400_15709_x1976183374}

[[表示存储方式，分为以下几种：]{style="font-family:宋体"}]{#struct_0_x1400_15709_840927340}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[volatile]{lang="EN-US"}]{#struct_0_x1400_15709_x2135701222}[：重启后信息丢失]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[nonVolatile]{lang="EN-US"}]{#struct_0_x1400_15709_x918766121}[：重启后信息仍保存]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[permanent]{lang="EN-US"}]{#struct_0_x1400_15709_973702919}[：重启后信息仍保存，允许更改，但不许删除]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[readOnly]{lang="EN-US"}]{#struct_0_x1400_15709_1001743080}[：重启后信息仍保存，既不允许更改，也不许删除]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[other]{lang="EN-US"}]{#struct_0_x1400_15709_1795993318}[：其他]{lang="EN-US" style="font-family:宋体"}

[[Context name]{lang="EN-US"}]{#struct_0_x1400_15709_x1843267149}

[[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_973768455}[上下文：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果此团体名配置了对应的上下文映射，则显示对应的上下文]{style="font-family:宋体"}]{#struct_0_x1400_15709_305750033}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果此团体名未配置对应的上下文映射，则不显示该字段]{style="font-family:宋体"}]{#struct_0_x1400_15709_x942924553}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_973833991}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **community**]{lang="EN-US"}]{#struct_0_x1400_15709_x1569627263}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **usm-user** { **v1** \| **v2c** }]{lang="EN-US"}]{#struct_0_x1400_15709_x509108675}

::: {#925430076 .myid}
[]{#_Toc404796931}[]{#struct_0_x1400_15709_1118410163}[]{#_Toc345227791}

**SNMP \-- SNMP配置命令 \-- display snmp-agent context**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **snmp-agent context** ]{lang="EN-US"}]{#struct_0_x1400_15709_x12450657}[命令用来显示指定的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[上下文。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1435375622}

[**[display]{lang="EN-US"}**[ **snmp-agent context** \[ *context-name* \]]{lang="EN-US"}]{#struct_0_x1400_15709_1899941433}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1801657622}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_1100587331}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_973899527}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_109767945}

[[network-operator]{lang="EN-US"}]{#struct_0_x1400_15709_1036336883}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x1419039744}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1400_15709_494775696}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1400_15709_752513944}

[*[context-name]{lang="EN-US"}*]{#struct_0_x1400_15709_x449629263}[：显示指定的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[上下文，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。不指定该参数时，显示设备上所有已创建的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[上下文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_973965063}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_1627337343}[显示设备上所有已创建的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[上下文。]{style="font-family:宋体"}

[[\<Sysname\> display snmp-agent context]{lang="EN-US"}]{#struct_0_x1400_15709_x821051541}

[   trillcontext]{lang="EN-US"}

[   isiscontext]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_75003147}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent context]{lang="EN-US"}**]{#struct_0_x1400_15709_x1740708398}
:::

::: {#-116423928 .myid}
[]{#_Toc404796932}[]{#struct_0_x1400_15709_x1282003563}

**SNMP \-- SNMP配置命令 \-- display snmp-agent group**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **snmp-agent** **group**]{lang="EN-US"}]{#struct_0_x1400_15709_x1568190767}[命令用来显示]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[组信息，包括组名、安全模式、视图、存储方式等。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_974030599}

[**[display]{lang="EN-US"}**[ **snmp-agent** **group** \[ *group-name* \]]{lang="EN-US"}]{#struct_0_x1400_15709_x538639306}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_963580689}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_x1327740307}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1340154243}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_126513487}

[[network-operator]{lang="EN-US"}]{#struct_0_x1400_15709_584001052}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_964637396}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1400_15709_1652419943}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1400_15709_974096135}

[*[group-name]{lang="EN-US"}*]{#struct_0_x1400_15709_x1373972636}[：非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，指定要显示信息的]{style="font-family:宋体"}[SNMPv1]{lang="EN-US"}[、]{style="font-family:宋体"}[SNMPv2c]{lang="EN-US"}[或]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[组名；]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，指定要显示信息的]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[组名。为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。不指定该参数时，显示设备上所有已创建的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[组的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x523512888}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_x643634570}[显示所有]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[组的信息。]{style="font-family:宋体"}

[[\<Sysname\> display snmp-agent group]{lang="EN-US"}]{#struct_0_x1400_15709_x88850650}

[   Group name: groupv3]{lang="EN-US"}

[       Security model: v3 noAuthnoPriv]{lang="EN-US"}

[       Readview: ViewDefault]{lang="EN-US"}

[       Writeview: \<no specified\>]{lang="EN-US"}

[       Notifyview: \<no specified\>]{lang="EN-US"}

[       Storage-type: nonVolatile]{lang="EN-US"}

[       ACL name: testacl]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display snmp-agent group]{lang="EN-US"}]{#struct_0_x1400_15709_973113095}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1592868709}[[字段]{style="font-family:黑体"}]{#struct_0_x1400_15709_1039545094}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1400_15709_1893191034}

[[Group name]{lang="EN-US"}]{#struct_0_x1400_15709_x2140478478}

[[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_92961241}[组名]{style="font-family:宋体"}

[[Security model]{lang="EN-US"}]{#struct_0_x1400_15709_x216261563}

[[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_1789025626}[组配置的安全模式，包括版本信息和安全模式，以空格分隔：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_x1400_15709_973178631}[SNMPv1]{lang="EN-US"}[和]{style="font-family:宋体"}[SNMPv2c]{lang="EN-US"}[版本，认证加密级别只能为]{style="font-family:宋体"}[noAuthNoPriv]{lang="EN-US"}[（无认证无加密）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{lang="EN-US" style="font-family:宋体"}[SNMPv3]{lang="EN-US"}]{#struct_0_x1400_15709_1812220330}[版本，安全模式分为三种：]{lang="EN-US" style="font-family:宋体"}[authPriv]{lang="EN-US"}[（既认证又加密）、]{lang="EN-US" style="font-family:宋体"}[authNoPriv]{lang="EN-US"}[（只认证不加密）、]{lang="EN-US" style="font-family:宋体"}[noAuthNoPriv]{lang="EN-US"}[（不认证不加密）]{lang="EN-US" style="font-family:宋体"}

[[Readview]{lang="EN-US"}]{#struct_0_x1400_15709_x56556188}

[[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_641242567}[组对应的只读的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[视图名]{style="font-family:宋体"}

[[Writeview]{lang="EN-US"}]{#struct_0_x1400_15709_x52280076}

[[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_897909209}[组对应的可写的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[视图名]{style="font-family:宋体"}

[[Notifyview]{lang="EN-US"}]{#struct_0_x1400_15709_973637384}

[[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_1822795748}[组对应的可以发]{style="font-family:宋体"}[Trap]{lang="EN-US"}[和]{style="font-family:宋体"}[Inform]{lang="EN-US"}[信息的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[视图名]{style="font-family:宋体"}

[[Storage-type]{lang="EN-US"}]{#struct_0_x1400_15709_x1976773198}

[[存储方式，分为以下几种：]{style="font-family:宋体"}[volatile]{lang="EN-US"}]{#struct_0_x1400_15709_x2026664603}[、]{style="font-family:宋体"}[nonVolatile]{lang="EN-US"}[、]{style="font-family:宋体"}[permanent]{lang="EN-US"}[、]{style="font-family:宋体"}[readOnly]{lang="EN-US"}[、]{style="font-family:宋体"}[other]{lang="EN-US"}[，具体请参见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-1]{lang="EN-US"}](?1188054656#_Ref291745733)

[[ACL]{lang="EN-US"}]{#struct_0_x1400_15709_585060604}

[[使用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x1400_15709_973702920}[列表的编号（该字段仅在]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[组与]{style="font-family:宋体"}[ACL]{lang="EN-US"}[绑定后显示，不会与]{style="font-family:宋体"}[ACL name]{lang="EN-US"}[同时存在）]{style="font-family:宋体"}

[[ACL name]{lang="EN-US"}]{#struct_0_x1400_15709_1543164856}

[[使用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x1400_15709_x100699827}[列表的名称（该字段仅在]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[组与]{style="font-family:宋体"}[ACL]{lang="EN-US"}[名称绑定后显示，不会与]{style="font-family:宋体"}[ACL]{lang="EN-US"}[同时存在）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1336909089}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **group**]{lang="EN-US"}]{#struct_0_x1400_15709_x1417902615}

::: {#-364242265 .myid}
[]{#_Toc404796933}[]{#struct_0_x1400_15709_1868044785}

**SNMP \-- SNMP配置命令 \-- display snmp-agent local-engineid**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **snmp-agent** **local-engineid**]{lang="EN-US"}]{#struct_0_x1400_15709_x280156624}[命令用来显示本地设备的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1870867867}

[**[display]{lang="EN-US"}**[ **snmp-agent** **local-engineid**]{lang="EN-US"}]{#struct_0_x1400_15709_x373916916}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_224444039}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_973768456}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_305750030}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x942924556}

[[network-operator]{lang="EN-US"}]{#struct_0_x1400_15709_x1304084668}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x1284287302}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1400_15709_571147244}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1041233038}

[[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_x696688211}[实体引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[是]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体的唯一标识，它在一个]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[管理域内是唯一的。]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体引擎是]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体的重要组成部分，完成]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[信息的信息调度、信息处理、安全验证、访问控制等功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_973833992}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_x1569627264}[显示本地设备的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> display snmp-agent local-engineid]{lang="EN-US"}]{#struct_0_x1400_15709_x912393202}

[SNMP local engine ID: 800007DB7F0000013859]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_2117039211}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **local-engineid**]{lang="EN-US"}]{#struct_0_x1400_15709_973965064}[]{#_Toc340753834}
:::

::: {#-11971892 .myid}
[]{#_Toc404796934}[]{#struct_0_x1400_15709_1627337340}

**SNMP \-- SNMP配置命令 \-- display snmp-agent mib-node**

------------------------------------------------------------------------

[**[display snmp-agent mib-node]{lang="EN-US"}**]{#struct_0_x1400_15709_x821248149}[命令用来显示当前]{style="font-family:
宋体"}[SNMP]{lang="EN-US"}[支持的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[节点信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1537890934}

[**[display snmp-agent mib-node ]{lang="EN-US"}**[\[ **details** \| **index-node** \| **trap-node** \| **verbose** \]]{lang="EN-US"}]{#struct_0_x1400_15709_1340760687}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1689863021}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_1050018256}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_165595628}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_974030600}

[[network-operator]{lang="EN-US"}]{#struct_0_x1400_15709_x944658850}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x1466517909}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1400_15709_306071083}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1372212076}

[**[details]{lang="SV"}**]{#struct_0_x1400_15709_982851200}[：]{style="font-family:宋体"} [表示显示]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[支持的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[节点细节信息，包括节点名、]{style="font-family:宋体"}[OID]{lang="EN-US"}[末位、下一个叶子节点名。]{style="font-family:宋体"}

[**[index-node]{lang="SV"}**]{#struct_0_x1400_15709_x2057749861}[：]{style="font-family:宋体"}[显示]{style="font-family:宋体"}[SNMP]{lang="SV"}[支持的]{style="font-family:宋体"}[MIB]{lang="SV"}[表、节点名及索引节点]{style="font-family:宋体"}[OID]{lang="SV"}[。]{style="font-family:宋体"}

[**[trap-node]{lang="EN-US"}**]{#struct_0_x1400_15709_2079303648}[：显示]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[支持的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[告警节点名及对应的]{style="font-family:宋体"}[OID]{lang="EN-US"}[、告警绑定变量节点名及对应的]{style="font-family:宋体"}[OID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[verbose]{lang="SV"}**]{#struct_0_x1400_15709_974096136}[：显示]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[支持的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[节点详细信息，包括节点名、]{style="font-family:宋体"}[OID]{lang="EN-US"}[、节点类型、访问权限、数据类型，对应]{style="font-family:宋体"}[MOR]{lang="EN-US"}[（]{style="font-family:宋体"}[Managed Object Repository]{lang="EN-US"}[，管理对象库）定义、父子兄弟节点信息等。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1373972633}

[[未指定任何参数时，显示]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_x961297320}[支持的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[节点信息，包括节点名、]{style="font-family:宋体"}[OID]{lang="EN-US"}[和节点访问权限。]{style="font-family:宋体"}

[[特性包中可以包含不同的]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_x1400_15709_x337424163}[插件，设备根据加载特性包的不同，支持的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[不相同。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1337331757}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_x219438944}[显示]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[支持]{style="font-family:宋体"}[MIB]{lang="EN-US"}[节点信息。]{style="font-family:宋体"}

[[\<Sysname\> display snmp-agent mib-node]{lang="EN-US"}]{#struct_0_x1400_15709_973113096}

[iso\<1\>(NA)]{lang="EN-US"}

[  \|-std\<1.0\>(NA)]{lang="EN-US"}

[   \|-iso8802\<1.0.8802\>(NA)]{lang="EN-US"}

[    \|-ieee802dot1\<1.0.8802.1\>(NA)]{lang="EN-US"}

[     \|-ieee802dot1mibs\<1.0.8802.1.1\>(NA)]{lang="EN-US"}

[      \|-lldpMIB\<1.0.8802.1.1.2\>(NA)]{lang="EN-US"}

[       \|-lldpNotifications\<1.0.8802.1.1.2.0\>(NA)]{lang="EN-US"}

[        \|-lldpNotificationPrefix\<1.0.8802.1.1.2.0.0\>(NA)]{lang="EN-US"}

[         \|-lldpRemTablesChange\<1.0.8802.1.1.2.0.0.1\>(NA)]{lang="EN-US"}

[       \|-lldpObjects\<1.0.8802.1.1.2.1\>(NA)]{lang="EN-US"}

[        \|-lldpConfiguration\<1.0.8802.1.1.2.1.1\>(NA)]{lang="EN-US"}

[         \|-\*lldpMessageTxInterval\<1.0.8802.1.1.2.1.1.1\>(RW)]{lang="EN-US"}

[         \|-\*lldpMessageTxHoldMultiplier\<1.0.8802.1.1.2.1.1.2\>(RW)]{lang="EN-US"}

[         \|-\*lldpReinitDelay\<1.0.8802.1.1.2.1.1.3\>(RW)]{lang="EN-US"}

[ ]{lang="SV"}

[[表1-3 ]{lang="EN-US"}[display snmp-agent mib-node]{lang="EN-US"}]{#struct_0_x1400_15709_1039545097}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1587440773}[[字段]{style="font-family:黑体"}]{#struct_0_x1400_15709_1892994426}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1400_15709_1365453296}

[[-std]{lang="EN-US"}]{#struct_0_x1400_15709_x443895520}

[[MIB]{lang="EN-US"}]{#struct_0_x1400_15709_x1533823997}[节点名]{style="font-family:宋体"}

[[\<1.0\>]{lang="EN-US"}]{#struct_0_x1400_15709_973178632}

[[MIB]{lang="EN-US"}]{#struct_0_x1400_15709_1812220329}[节点对应的]{style="font-family:宋体"}[OID]{lang="EN-US"}

[[(NA)]{lang="EN-US"}]{#struct_0_x1400_15709_x56097435}

[[MIB]{lang="EN-US"}]{#struct_0_x1400_15709_x1893075953}[节点访问权限，取值为：]{style="font-family:宋体"}

[[NA]{lang="EN-US"}]{#struct_0_x1400_15709_1251661957}[：表示节点不可访问]{style="font-family:宋体"}

[[NF]{lang="EN-US"}]{#struct_0_x1400_15709_x1471565777}[：表示节点支持告警]{style="font-family:宋体"}

[[RO]{lang="EN-US"}]{#struct_0_x1400_15709_509512597}[：表示节点支持只读访问]{style="font-family:宋体"}

[[RW]{lang="EN-US"}]{#struct_0_x1400_15709_973637381}[：表示节点支持读写访问]{style="font-family:宋体"}

[[RC]{lang="EN-US"}]{#struct_0_x1400_15709_1822795743}[：表示节点支持读写创建访问]{style="font-family:宋体"}

[[WO]{lang="EN-US"}]{#struct_0_x1400_15709_x1976052302}[：表示节点支持只写访问]{style="font-family:宋体"}

[[\*]{lang="EN-US"}]{#struct_0_x1400_15709_343281483}

[[表示叶子节点或表节点]{style="font-family:宋体"}]{#struct_0_x1400_15709_897530050}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_x54046991}[显示]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[支持]{style="font-family:宋体"}[MIB]{lang="EN-US"}[节点细节信息。]{style="font-family:宋体"}

[[\<Sysname\> display snmp-agent mib-node details]{lang="EN-US"}]{#struct_0_x1400_15709_973702917}

[iso(1)(lldpMessageTxInterval)]{lang="EN-US"}

[  \|-std(0)(lldpMessageTxInterval)]{lang="EN-US"}

[   \|-iso8802(8802)(lldpMessageTxInterval)]{lang="EN-US"}

[    \|-ieee802dot1(1)(lldpMessageTxInterval)]{lang="EN-US"}

[     \|-ieee802dot1mibs(1)(lldpMessageTxInterval)]{lang="EN-US"}

[      \|-lldpMIB(2)(lldpMessageTxInterval)]{lang="EN-US"}

[       \|-lldpNotifications(0)(lldpMessageTxInterval)]{lang="EN-US"}

[        \|-lldpNotificationPrefix(0)(lldpMessageTxInterval)]{lang="EN-US"}

[         \|-lldpRemTablesChange(1)(NULL)]{lang="EN-US"}

[       \|-lldpObjects(1)(lldpMessageTxInterval)]{lang="EN-US"}

[        \|-lldpConfiguration(1)(lldpMessageTxInterval)]{lang="EN-US"}

[         \|-\*lldpMessageTxInterval(1)(lldpMessageTxHoldMultiplier)]{lang="EN-US"}

[         \|-\*lldpMessageTxHoldMultiplier(2)(lldpReinitDelay)]{lang="EN-US"}

[         \|-\*lldpReinitDelay(3)(lldpTxDelay)]{lang="EN-US"}

[         \|-\*lldpTxDelay(4)(lldpNotificationInterval)]{lang="EN-US"}

[         \|-\*lldpNotificationInterval(5)(lldpPortConfigPortNum)]{lang="EN-US"}

[         \|-lldpPortConfigTable(6)(lldpPortConfigPortNum)]{lang="EN-US"}

[          \|-lldpPortConfigEntry(1)(lldpPortConfigPortNum)]{lang="EN-US"}

[           \|-\*lldpPortConfigPortNum(1)(lldpPortConfigAdminStatus)]{lang="EN-US"}

[           \|-\*lldpPortConfigAdminStatus(2)(lldpPortConfigNotificationEnable)]{lang="EN-US"}

[           \|-\*lldpPortConfigNotificationEnable(3)(lldpPortConfigTLVsTxEnable)]{lang="EN-US"}

[           \|-\*lldpPortConfigTLVsTxEnable(4)(lldpConfigManAddrPortsTxEnable)]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display snmp-agent mib-node details]{lang="EN-US"}]{#struct_0_x1400_15709_973768453}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1587683365}[[字段]{style="font-family:黑体"}]{#struct_0_x1400_15709_305750035}

[[描述]{style="font-family:黑体"}]{#struct_0_x1400_15709_x942924559}

[[-std]{lang="EN-US"}]{#struct_0_x1400_15709_x1303363772}

[[MIB]{lang="EN-US"}]{#struct_0_x1400_15709_x1775256482}[节点名]{style="font-family:宋体"}

[[(0)]{lang="EN-US"}]{#struct_0_x1400_15709_x232137641}

[[MIB]{lang="EN-US"}]{#struct_0_x1400_15709_624526395}[节点对应]{style="font-family:宋体"}[OID]{lang="EN-US"}[末位]{style="font-family:宋体"}

[[(lldpMessageTxInterval)]{lang="EN-US"}]{#struct_0_x1400_15709_973833989}

[[MIB]{lang="EN-US"}]{#struct_0_x1400_15709_386687881}[节点下一个叶子节点名]{style="font-family:宋体"}

[[\*]{lang="EN-US"}]{#struct_0_x1400_15709_x1986878199}

[[表示叶子节点或表节点]{style="font-family:宋体"}]{#struct_0_x1400_15709_x1501893153}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_1529086960}[显示]{style="font-family:宋体"}[SNMP]{lang="SV"}[支持的]{style="font-family:宋体"}[MIB]{lang="SV"}[表名、索引节点名及对应的]{style="font-family:宋体"}[OID]{lang="SV"}[。]{style="font-family:宋体"}

[[\<Sysname\> display snmp-agent mib-node index-node]{lang="EN-US"}]{#struct_0_x1400_15709_973899525}

[Table          \|lldpPortConfigTable]{lang="EN-US"}

[Index          \|\|lldpPortConfigPortNum]{lang="EN-US"}

[OID            \|\|\|  1.0.8802.1.1.2.1.1.6.1.1]{lang="EN-US"}

[ ]{lang="EN-US"}

[Table          \|lldpConfigManAddrTable]{lang="EN-US"}

[Index          \|\|lldpLocManAddrSubtype]{lang="EN-US"}

[OID            \|\|\|  1.0.8802.1.1.2.1.3.8.1.1]{lang="EN-US"}

[Index          \|\|lldpLocManAddr]{lang="EN-US"}

[OID            \|\|\|  1.0.8802.1.1.2.1.3.8.1.2]{lang="EN-US"}

[ ]{lang="EN-US"}

[Table          \|lldpStatsTxPortTable]{lang="EN-US"}

[Index          \|\|lldpStatsTxPortNum]{lang="EN-US"}

[OID            \|\|\|  1.0.8802.1.1.2.1.2.6.1.1]{lang="EN-US"}

[ ]{lang="EN-US"}

[Table          \|lldpStatsRxPortTable]{lang="EN-US"}

[Index          \|\|lldpStatsRxPortNum]{lang="EN-US"}

[OID            \|\|\|  1.0.8802.1.1.2.1.2.7.1.1]{lang="EN-US"}

[ ]{lang="EN-US"}

[Table          \|lldpLocPortTable]{lang="EN-US"}

[Index          \|\|lldpLocPortNum]{lang="EN-US"}

[OID            \|\|\|  1.0.8802.1.1.2.1.3.7.1.1]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display snmp-agent mib-node index-node]{lang="EN-US"}]{#struct_0_x1400_15709_109767943}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1583254693}[[字段]{style="font-family:黑体"}]{#struct_0_x1400_15709_1036336885}

[[描述]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1418646528}

[[Table]{lang="EN-US"}]{#struct_0_x1400_15709_973965061}

[[MIB]{lang="EN-US"}]{#struct_0_x1400_15709_1627337345}[表名]{style="font-family:宋体"}

[[Index]{lang="EN-US"}]{#struct_0_x1400_15709_x820920469}

[[MIB]{lang="EN-US"}]{#struct_0_x1400_15709_x1100873289}[索引节点名]{style="font-family:宋体"}

[[OID]{lang="EN-US"}]{#struct_0_x1400_15709_153224516}

[[MIB]{lang="EN-US"}]{#struct_0_x1400_15709_1833356887}[索引节点对应的]{style="font-family:宋体"}[OID]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_974030597}[显示]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[支持的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[告警节点名及对应的]{style="font-family:宋体"}[OID]{lang="EN-US"}[、告警绑定变量节点名及对应的]{style="font-family:宋体"}[OID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> display snmp-agent mib-node trap-node]{lang="EN-US"}]{#struct_0_x1400_15709_974096133}

[Name          \|lldpRemTablesChange]{lang="SV"}

[OID           \|\|1.0.8802.1.1.2.0.0.1]{lang="SV"}

[Trap Object]{lang="SV"}

[Name          \|\|\|lldpStatsRemTablesInserts]{lang="SV"}

[OID           \|\|\|\|1.0.8802.1.1.2.1.2.2]{lang="SV"}

[Name          \|\|\|lldpStatsRemTablesDeletes]{lang="SV"}

[OID           \|\|\|\|1.0.8802.1.1.2.1.2.3]{lang="SV"}

[Name          \|\|\|lldpStatsRemTablesDrops]{lang="SV"}

[OID           \|\|\|\|1.0.8802.1.1.2.1.2.4]{lang="SV"}

[Name          \|\|\|lldpStatsRemTablesAgeouts]{lang="SV"}

[OID           \|\|\|\|1.0.8802.1.1.2.1.2.5]{lang="SV"}

[ ]{lang="SV"}

[Name          \|lldpXMedTopologyChangeDetected]{lang="SV"}

[OID           \|\|1.0.8802.1.1.2.1.5.4795.0.1]{lang="SV"}

[Trap Object]{lang="SV"}

[Name          \|\|\|lldpRemChassisIdSubtype]{lang="SV"}

[OID           \|\|\|\|1.0.8802.1.1.2.1.4.1.1.4]{lang="SV"}

[Name          \|\|\|lldpRemChassisId]{lang="SV"}

[OID           \|\|\|\|1.0.8802.1.1.2.1.4.1.1.5]{lang="SV"}

[Name          \|\|\|lldpXMedRemDeviceClass]{lang="SV"}

[OID           \|\|\|\|1.0.8802.1.1.2.1.5.4795.1.3.1.1.3]{lang="SV"}

[ ]{lang="SV"}

[Name          \|mplsL3VpnVrfUp]{lang="SV"}

[OID           \|\|1.3.6.1.2.1.10.166.11.0.1]{lang="SV"}

[Trap Object]{lang="SV"}

[Name          \|\|\|mplsL3VpnIfConfRowStatus]{lang="SV"}

[OID           \|\|\|\|1.3.6.1.2.1.10.166.11.1.2.1.1.5]{lang="SV"}

[Name          \|\|\|mplsL3VpnVrfOperStatus]{lang="SV"}

[OID           \|\|\|\|1.3.6.1.2.1.10.166.11.1.2.2.1.6]{lang="SV"}

[[表1-6 ]{lang="EN-US"}[display snmp-agent mib-node trap-node]{lang="EN-US"}]{#struct_0_x1400_15709_x1373972638}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1584977605}[[字段]{style="font-family:黑体"}]{#struct_0_x1400_15709_2123816395}

[[描述]{style="font-family:黑体"}]{#struct_0_x1400_15709_419249450}

[[Name]{lang="SV"}]{#struct_0_x1400_15709_x1342237030}

[[MIB]{lang="EN-US"}]{#struct_0_x1400_15709_1778443261}[告警节点名]{style="font-family:宋体"}

[[OID]{lang="EN-US"}]{#struct_0_x1400_15709_973113093}

[[MIB]{lang="EN-US"}]{#struct_0_x1400_15709_1039545092}[告警节点对应的]{style="font-family:宋体"}[OID]{lang="EN-US"}

[[Trap Object]{lang="SV"}]{#struct_0_x1400_15709_1893322106}

[[MIB]{lang="EN-US"}]{#struct_0_x1400_15709_1354592154}[告警绑定变量节点相关信息（其中]{style="font-family:宋体"}[Name]{lang="EN-US"}[表示告警绑定变量节点名，]{style="font-family:宋体"}[OID]{lang="EN-US"}[表示变量名节点对应的]{style="font-family:宋体"}[OID]{lang="EN-US"}[）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_1530936117}[显示]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[支持的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[节点详细信息，包括节点名、]{style="font-family:宋体"}[OID]{lang="EN-US"}[、节点类型、访问权限、数据类型，对应]{style="font-family:宋体"}[MOR]{lang="EN-US"}[定义、父子兄弟节点信息等。]{style="font-family:宋体"}

[[\<Sysname\> display snmp-agent mib-node verbose]{lang="EN-US"}]{#struct_0_x1400_15709_973702918}

[Name          \|lldpNotificationInterval]{lang="EN-US"}

[OID           \|\|1.0.8802.1.1.2.1.1.5]{lang="EN-US"}

[Properties    \|\|NodeType:   Leaf]{lang="EN-US"}

[              \|\|AccessType: RW]{lang="EN-US"}

[              \|\|DataType:   Integer32]{lang="EN-US"}

[              \|\|MOR:        0x020c1105]{lang="EN-US"}

[Parent        \|\|lldpConfiguration]{lang="EN-US"}

[First child   \|\|]{lang="EN-US"}

[Next leaf     \|\|lldpPortConfigPortNum]{lang="EN-US"}

[Next sibling  \|\|lldpPortConfigTable]{lang="EN-US"}

[Allow         \|\|get/set/getnext]{lang="EN-US"}

[Value range   \|\|  \[5..3600\]]{lang="EN-US"}

[ ]{lang="EN-US"}

[Name          \|lldpPortConfigTable]{lang="EN-US"}

[OID           \|\|1.0.8802.1.1.2.1.1.6]{lang="EN-US"}

[Properties    \|\|NodeType:   Table]{lang="EN-US"}

[              \|\|AccessType: NA]{lang="EN-US"}

[              \|\|DataType:   NA]{lang="EN-US"}

[              \|\|MOR:        0x00000000]{lang="EN-US"}

[Parent        \|\|lldpConfiguration]{lang="EN-US"}

[First child   \|\|lldpPortConfigEntry]{lang="EN-US"}

[Next leaf     \|\|lldpPortConfigPortNum]{lang="EN-US"}

[Next sibling  \|\|lldpConfigManAddrTable]{lang="EN-US"}

[ ]{lang="EN-US"}

[Name          \|lldpPortConfigEntry]{lang="EN-US"}

[OID           \|\|1.0.8802.1.1.2.1.1.6.1]{lang="EN-US"}

[Properties    \|\|NodeType:   Row]{lang="EN-US"}

[              \|\|AccessType: NA]{lang="EN-US"}

[              \|\|DataType:   NA]{lang="EN-US"}

[              \|\|MOR:        0x00000000]{lang="EN-US"}

[Parent        \|\|lldpPortConfigTable]{lang="EN-US"}

[First child   \|\|lldpPortConfigPortNum]{lang="EN-US"}

[Next leaf     \|\|lldpPortConfigPortNum]{lang="EN-US"}

[Next sibling  \|\|]{lang="EN-US"}

[Index         \|\|\[indexImplied:0, indexLength:1\]:]{lang="EN-US"}

[ ]{lang="EN-US"}

[Name          \|lldpPortConfigPortNum]{lang="EN-US"}

[OID           \|\|1.0.8802.1.1.2.1.1.6.1.1]{lang="EN-US"}

[Properties    \|\|NodeType:   Column]{lang="EN-US"}

[              \|\|AccessType: NA]{lang="EN-US"}

[              \|\|DataType:   Integer32]{lang="EN-US"}

[              \|\|MOR:        0x020c1201]{lang="EN-US"}

[Parent        \|\|lldpPortConfigEntry]{lang="EN-US"}

[First child   \|\|]{lang="EN-US"}

[Next leaf     \|\|lldpPortConfigAdminStatus]{lang="EN-US"}

[Next sibling  \|\|lldpPortConfigAdminStatus]{lang="EN-US"}

[Allow         \|\|get/set/getnext]{lang="EN-US"}

[Index         \|\|\[indexImplied:0, indexLength:1\]:]{lang="EN-US"}

[Value range   \|\|  \[1..4096\]]{lang="EN-US"}

[ ]{lang="EN-US"}

[Name          \|lldpPortConfigAdminStatus]{lang="EN-US"}

[OID           \|\|1.0.8802.1.1.2.1.1.6.1.2]{lang="EN-US"}

[Properties    \|\|NodeType:   Column]{lang="EN-US"}

[              \|\|AccessType: RW]{lang="EN-US"}

[              \|\|DataType:   Integer]{lang="EN-US"}

[              \|\|MOR:        0x020c1202]{lang="EN-US"}

[Parent        \|\|lldpPortConfigEntry]{lang="EN-US"}

[First child   \|\|]{lang="EN-US"}

[Next leaf     \|\|lldpPortConfigNotificationEnable]{lang="EN-US"}

[Next sibling  \|\|lldpPortConfigNotificationEnable]{lang="EN-US"}

[Allow         \|\|get/set/getnext]{lang="EN-US"}

[Index         \|\|\[indexImplied:0, indexLength:1\]:]{lang="EN-US"}

[Value range   \|\|]{lang="EN-US"}

[              \|\|  \[\'txOnly\', 1\]]{lang="EN-US"}

[              \|\|  \[\'rxOnly\', 2\]]{lang="EN-US"}

[              \|\|  \[\'txAndRx\', 3\]]{lang="EN-US"}

[              \|\|  \[\'disabled\', 4\]]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display snmp-agent mib-node verbose]{lang="EN-US"}]{#struct_0_x1400_15709_1001743079}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1578172037}[[字段]{style="font-family:黑体"}]{#struct_0_x1400_15709_1796452085}

[[描述]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1992921350}

[[Name]{lang="SV"}]{#struct_0_x1400_15709_1862276411}

[[MIB]{lang="EN-US"}]{#struct_0_x1400_15709_2090078127}[节点名]{style="font-family:宋体"}

[[OID]{lang="EN-US"}]{#struct_0_x1400_15709_973768454}

[[MIB]{lang="EN-US"}]{#struct_0_x1400_15709_305750032}[节点对应的]{style="font-family:宋体"}[OID]{lang="EN-US"}

[[NodeType]{lang="EN-US"}]{#struct_0_x1400_15709_x942924554}

[[MIB]{lang="EN-US"}]{#struct_0_x1400_15709_x1304215740}[节点类型，取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Table]{lang="EN-US"}]{#struct_0_x1400_15709_x1924934482}[：表节点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Row]{lang="EN-US"}]{#struct_0_x1400_15709_x465109517}[：表中行节点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Column]{lang="EN-US"}]{#struct_0_x1400_15709_973833990}[：表中列节点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Leaf]{lang="EN-US"}]{#struct_0_x1400_15709_x1569627262}[：叶子节点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Group]{lang="EN-US"}]{#struct_0_x1400_15709_x2075192616}[：组节点（叶子节点的父节点）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Trapnode]{lang="EN-US"}]{#struct_0_x1400_15709_1614595586}[：告警节点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Other]{lang="EN-US"}]{#struct_0_x1400_15709_x746692006}[：其他类型]{lang="EN-US" style="font-family:宋体"}

[[AccessType]{lang="EN-US"}]{#struct_0_x1400_15709_x2096486311}

[[MIB]{lang="EN-US"}]{#struct_0_x1400_15709_973899526}[节点访问权限，取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NA]{lang="EN-US"}]{#struct_0_x1400_15709_109767946}[：表示节点不可访问]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NF]{lang="EN-US"}]{#struct_0_x1400_15709_1036336882}[：表示节点支持告警]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RO]{lang="EN-US"}]{#struct_0_x1400_15709_x1419105280}[：表示节点支持只读访问]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RW]{lang="EN-US"}]{#struct_0_x1400_15709_x1069564830}[：表示节点支持读写访问]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RC]{lang="EN-US"}]{#struct_0_x1400_15709_973965062}[：表示节点支持读写创建访问]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WO]{lang="EN-US"}]{#struct_0_x1400_15709_1627337342}[：表示节点支持只写访问]{style="font-family:宋体"}

[[DataType]{lang="EN-US"}]{#struct_0_x1400_15709_x821117077}

[[MIB]{lang="EN-US"}]{#struct_0_x1400_15709_2024049717}[节点数据类型，取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Integer]{lang="EN-US"}]{#struct_0_x1400_15709_974030598}[：整数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Integer32]{lang="EN-US"}]{#struct_0_x1400_15709_x538639305}[：]{lang="EN-US" style="font-family:宋体"}[32]{lang="EN-US"}[位整数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unsigned32]{lang="EN-US"}]{#struct_0_x1400_15709_963646225}[：]{lang="EN-US" style="font-family:宋体"}[32]{lang="EN-US"}[位无符号整数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Gauge]{lang="EN-US"}]{#struct_0_x1400_15709_x1888674959}[：可增可减的非负整数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Gauge32]{lang="EN-US"}]{#struct_0_x1400_15709_204444938}[：]{style="font-family:宋体"}[32]{lang="EN-US"}[位可增可减的非负整数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Counter]{lang="EN-US"}]{#struct_0_x1400_15709_974096134}[：可增不可减的非负整数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Counter32]{lang="EN-US"}]{#struct_0_x1400_15709_x1373972635}[：]{lang="EN-US" style="font-family:宋体"}[32]{lang="EN-US"}[位可增不可减的非负整数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Counter64]{lang="EN-US"}]{#struct_0_x1400_15709_x2124096734}[：]{lang="EN-US" style="font-family:宋体"}[64]{lang="EN-US"}[位可增不可减的非负整数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Timeticks]{lang="EN-US"}]{#struct_0_x1400_15709_x182111388}[：用于计时的非负整数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Octstring]{lang="EN-US"}]{#struct_0_x1400_15709_973113094}[：]{lang="EN-US" style="font-family:宋体"}[八进制]{style="font-family:宋体"}[字符串]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OID]{lang="EN-US"}]{#struct_0_x1400_15709_1039545095}[：对象标识符]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPaddress]{lang="EN-US"}]{#struct_0_x1400_15709_1893125498}[：用于]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[规范格式的]{lang="EN-US" style="font-family:宋体"}[32]{lang="EN-US"}[位地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Networkaddress]{lang="EN-US"}]{#struct_0_x1400_15709_922596952}[：网络]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Opaque]{lang="EN-US"}]{#struct_0_x1400_15709_973178630}[：任意数据]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Userdefined]{lang="EN-US"}]{#struct_0_x1400_15709_1812220331}[：用户类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BITS]{lang="EN-US"}]{#struct_0_x1400_15709_x56621724}[：所述位枚举]{lang="EN-US" style="font-family:宋体"}

[[MOR]{lang="EN-US"}]{#struct_0_x1400_15709_1214992602}

[[MIB]{lang="EN-US"}]{#struct_0_x1400_15709_x1399015610}[节点对应的]{style="font-family:宋体"}[MOR]{lang="EN-US"}[定义]{style="font-family:宋体"}

[[Parent]{lang="EN-US"}]{#struct_0_x1400_15709_1738528008}

[[父节点名]{style="font-family:宋体"}]{#struct_0_x1400_15709_1592047951}

[[First child]{lang="EN-US"}]{#struct_0_x1400_15709_x1398950074}

[[第一个子节点名]{style="font-family:宋体"}]{#struct_0_x1400_15709_x359037011}

[[Next leaf]{lang="EN-US"}]{#struct_0_x1400_15709_93700455}

[[下一个叶子节点名]{style="font-family:宋体"}]{#struct_0_x1400_15709_669352963}

[[Next sibling]{lang="EN-US"}]{#struct_0_x1400_15709_x1398884538}

[[右兄弟节点名]{style="font-family:宋体"}]{#struct_0_x1400_15709_2097894707}

[[Allow]{lang="EN-US"}]{#struct_0_x1400_15709_x574349936}

[[允许的操作类型，取值包括如下：]{style="font-family:宋体"}]{#struct_0_x1400_15709_x1398819002}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[get/set/getnext]{lang="EN-US"}]{#struct_0_x1400_15709_x1048318985}[：允许所有操作]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[get]{lang="EN-US"}]{#struct_0_x1400_15709_x1806328}[：只允许]{lang="EN-US" style="font-family:宋体"}[G]{lang="EN-US"}[et]{lang="EN-US"}[操作]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[set]{lang="EN-US"}]{#struct_0_x1400_15709_x1398753466}[：只允许]{lang="EN-US" style="font-family:宋体"}[S]{lang="EN-US"}[et]{lang="EN-US"}[操作]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[getnext]{lang="EN-US"}]{#struct_0_x1400_15709_x1643471245}[：只允许]{lang="EN-US" style="font-family:宋体"}[G]{lang="EN-US"}[et]{lang="EN-US"}[N]{lang="EN-US"}[ext]{lang="EN-US"}[操作]{lang="EN-US" style="font-family:宋体"}

[[Value range]{lang="EN-US"}]{#struct_0_x1400_15709_x1014244198}

[[节点的取值范围]{style="font-family:宋体"}]{#struct_0_x1400_15709_x1398687930}

[[Index]{lang="EN-US"}]{#struct_0_x1400_15709_1621012583}

[[表索引，仅表节点显示此字段]{style="font-family:宋体"}]{#struct_0_x1400_15709_1880366349}

[ ]{lang="EN-US"}

::: {#-643173804 .myid}
[]{#_Toc404796935}[]{#struct_0_x1400_15709_1316905159}

**SNMP \-- SNMP配置命令 \-- display snmp-agent mib-view**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **snmp-agent** **mib-view**]{lang="EN-US"}]{#struct_0_x1400_15709_x1150721580}[命令用来显示]{style="font-family:宋体"}[MIB]{lang="EN-US"}[视图的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1398622394}

[**[display]{lang="EN-US"}**[ **snmp-agent** **mib-view** \[ **exclude** \| **include** \| **viewname** *view-name* \]]{lang="EN-US"}]{#struct_0_x1400_15709_x151283509}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1948675050}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_x806025323}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x65390713}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_848282289}

[[network-operator]{lang="EN-US"}]{#struct_0_x1400_15709_x708532026}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x955119602}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1400_15709_575611459}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1398556858}

[**[exclude]{lang="EN-US"}**]{#struct_0_x1400_15709_x2052629983}[：显示属性为]{style="font-family:宋体"}[exclude]{lang="EN-US"}[的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[视图的信息。]{style="font-family:宋体"}

[**[include]{lang="EN-US"}**]{#struct_0_x1400_15709_x203726754}[：显示属性为]{style="font-family:宋体"}[include]{lang="EN-US"}[的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[视图的信息。]{style="font-family:宋体"}

[**[viewname]{lang="EN-US"}**[ *view-name*]{lang="EN-US"}]{#struct_0_x1400_15709_x425338184}[：显示指定名称]{style="font-family:宋体"}[MIB]{lang="EN-US"}[视图的信息，]{style="font-family:宋体"}*[view-name]{lang="EN-US"}*[为视图的名称。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1782733353}

[[不指定参数时，显示所有]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_x1400_15709_2082436609}[视图的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1244769109}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_x1777939057}[显示设备的所有]{style="font-family:宋体"}[MIB]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> display snmp-agent mib-view]{lang="EN-US"}]{#struct_0_x1400_15709_x1399539898}

[   View name: ViewDefault]{lang="EN-US"}

[       MIB Subtree: iso]{lang="EN-US"}

[       Subtree mask:]{lang="EN-US"}

[       Storage-type: nonVolatile]{lang="EN-US"}

[       View Type: included]{lang="EN-US"}

[       View status: active]{lang="EN-US"}

[ ]{lang="EN-US"}

[   View name: ViewDefault]{lang="EN-US"}

[       MIB Subtree: snmpUsmMIB]{lang="EN-US"}

[       Subtree mask:]{lang="EN-US"}

[       Storage-type: nonVolatile]{lang="EN-US"}

[       View Type: excluded]{lang="EN-US"}

[       View status: active]{lang="EN-US"}

[ ]{lang="EN-US"}

[   View name: ViewDefault]{lang="EN-US"}

[       MIB Subtree: snmpVacmMIB]{lang="EN-US"}

[       Subtree mask:]{lang="EN-US"}

[       Storage-type: nonVolatile]{lang="EN-US"}

[       View Type: excluded]{lang="EN-US"}

[       View status: active]{lang="EN-US"}

[ ]{lang="EN-US"}

[   View name: ViewDefault]{lang="EN-US"}

[       MIB Subtree: snmpModules.18]{lang="EN-US"}

[       Subtree mask:]{lang="EN-US"}

[       Storage-type: nonVolatile]{lang="EN-US"}

[       View Type: excluded]{lang="EN-US"}

[       View status: active]{lang="EN-US"}

[[以上信息表明，设备上当前有四个]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_x1400_15709_x1399474362}[视图，名称均为]{style="font-family:宋体"}[ViewDefault]{lang="EN-US"}[。使用]{style="font-family:宋体"}[ViewDefault]{lang="EN-US"}[视图名限制]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问时，除了]{style="font-family:宋体"}[snmpUsmMIB]{lang="EN-US"}[、]{style="font-family:宋体"}[snmpVacmMIB]{lang="EN-US"}[、]{style="font-family:宋体"}[snmpModules.18]{lang="EN-US"}[子树下的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[对象，]{style="font-family:宋体"}[NMS]{lang="EN-US"}[可以访问]{style="font-family:宋体"}[iso]{lang="EN-US"}[子树下其它所有]{style="font-family:宋体"}[MIB]{lang="EN-US"}[对象。]{style="font-family:宋体"}

[[表1-8 ]{lang="EN-US"}[display snmp-agent mib-view]{lang="EN-US"}]{#struct_0_x1400_15709_x1254314419}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1607848805}[[字段]{style="font-family:黑体"}]{#struct_0_x1400_15709_1303066416}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1400_15709_2085752095}

[[View name]{lang="EN-US"}]{#struct_0_x1400_15709_x2139782765}

[[视图名]{style="font-family:宋体"}]{#struct_0_x1400_15709_x347829867}

[[MIB Subtree]{lang="EN-US"}]{#struct_0_x1400_15709_439561027}

[[MIB]{lang="EN-US"}]{#struct_0_x1400_15709_x1399015609}[视图对应的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[子树]{style="font-family:宋体"}

[[Subtree mask]{lang="EN-US"}]{#struct_0_x1400_15709_x634190523}

[[MIB]{lang="EN-US"}]{#struct_0_x1400_15709_x625417711}[子树的掩码]{style="font-family:宋体"}

[[Storage-type]{lang="EN-US"}]{#struct_0_x1400_15709_436047037}

[[存储方式，分为以下几种：]{style="font-family:宋体"}[volatile]{lang="EN-US"}]{#struct_0_x1400_15709_210386768}[、]{style="font-family:宋体"}[nonVolatile]{lang="EN-US"}[、]{style="font-family:宋体"}[permanent]{lang="EN-US"}[、]{style="font-family:宋体"}[readOnly]{lang="EN-US"}[、]{style="font-family:宋体"}[other]{lang="EN-US"}[，具体请参见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-1]{lang="EN-US"}](?1188054656#_Ref291745733)

[[View Type]{lang="EN-US"}]{#struct_0_x1400_15709_268137530}

[[MIB]{lang="EN-US"}]{#struct_0_x1400_15709_x1398950073}[视图的类型（即该视图与]{style="font-family:宋体"}[MIB]{lang="EN-US"}[子树的关系），包括]{style="font-family:宋体"}[included]{lang="EN-US"}[和]{style="font-family:宋体"}[excluded]{lang="EN-US"}[两种：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[included]{lang="EN-US"}]{#struct_0_x1400_15709_2013615984}[表示当前视图包括该子树的所有节点，即可以访问子树内的所有]{style="font-family:宋体"}[MIB]{lang="EN-US"}[对象]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[excluded]{lang="EN-US"}]{#struct_0_x1400_15709_1831687855}[表示当前视图不包括该子树的任意节点，即子树内的所有]{style="font-family:宋体"}[MIB]{lang="EN-US"}[对象都不能被访问]{style="font-family:宋体"}

[[View status]{lang="EN-US"}]{#struct_0_x1400_15709_647083779}

[[MIB]{lang="EN-US"}]{#struct_0_x1400_15709_1571905418}[视图的状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_x1400_15709_x1398884537}[表示]{lang="EN-US" style="font-family:宋体"}[MIB]{lang="EN-US"}[视图可用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[inactive]{lang="EN-US"}]{#struct_0_x1400_15709_x630988648}[表示]{lang="EN-US" style="font-family:宋体"}[MIB]{lang="EN-US"}[视图不可用]{lang="EN-US" style="font-family:宋体"}

[[在无需删除]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_x1400_15709_x766933045}[视图就可以通过命令行暂时关闭]{style="font-family:宋体"}[MIB]{lang="EN-US"}[视图。对]{style="font-family:宋体"}[MIB]{lang="EN-US"}[视图状态节点执行]{style="font-family:宋体"}[Set]{lang="EN-US"}[操作可以修改]{style="font-family:宋体"}[MIB]{lang="EN-US"}[视图的状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1640857739}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **mib-view**]{lang="EN-US"}]{#struct_0_x1400_15709_1317445256}

::: {#145985246 .myid}
[]{#_Toc404796936}[]{#struct_0_x1400_15709_1216242285}

**SNMP \-- SNMP配置命令 \-- display snmp-agent remote**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **snmp-agent** **remote**]{lang="EN-US"}]{#struct_0_x1400_15709_629677097}[命令用来显示远端]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体的引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_482359838}

[**[display]{lang="EN-US"}**[ **snmp-agent** **remote** \[ *ip-address* \[ **vpn-instance** *vpn-instance-name* \] \| **ipv6** *ipv6-address* \[ **vpn-instance** *vpn-instance-name* \] \]]{lang="EN-US"}]{#struct_0_x1400_15709_x1398819001}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1680564370}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_1580484919}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_329402714}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_184337602}

[[network-operator]{lang="EN-US"}]{#struct_0_x1400_15709_1236043865}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x1967617604}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1400_15709_x141715093}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x138890327}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1400_15709_x1398753465}[：显示指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的远端]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体的引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**[ *ipv6-address*]{lang="EN-US"}]{#struct_0_x1400_15709_1085412110}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的远端]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体的引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x1400_15709_x175141449}[：指定远端]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示远端]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体位于公网中。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x950956707}

[[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_x1821952180}[实体引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[是]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体的唯一标识，它在一个]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[管理域内是唯一的。]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体引擎是]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体的重要组成部分，完成]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[信息的信息调度、信息处理、安全验证、访问控制等功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1554025088}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_x521544191}[显示所有远端]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体的引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> display snmp-agent remote]{lang="EN-US"}]{#struct_0_x1400_15709_x1398687929}

[   Remote engineID: 800063A28000A0FC00580400000001]{lang="EN-US"}

[       IPv4 address: 1.1.1.1]{lang="EN-US"}

[       VPN instance: vpn1]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display snmp-agent remote]{lang="EN-US"}]{#struct_0_x1400_15709_411093466}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1610361189}[[字段]{style="font-family:黑体"}]{#struct_0_x1400_15709_1726333251}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1400_15709_x694119978}

[[Remote engineID]{lang="EN-US"}]{#struct_0_x1400_15709_1142754347}

[[远端]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_x671911667}[实体的引擎，可通过]{style="font-family:宋体"}**[snmp-agent]{lang="EN-US"}**[ **remote**]{lang="EN-US"}[命令配置]{style="font-family:宋体"}

[[IPv4 address]{lang="EN-US"}]{#struct_0_x1400_15709_1448709702}

[[远端]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_x1398622393}[实体的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[如果配置]{style="font-family:宋体"}**[snmp-agent]{lang="EN-US"}**[ **remote**]{lang="EN-US"}]{#struct_0_x1400_15709_x910798396}[命令时绑定的是]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，则显示]{style="font-family:宋体"}[IPv6 address]{lang="EN-US"}

[[VPN instance]{lang="EN-US"}]{#struct_0_x1400_15709_x918521951}

[[远端]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_x705864216}[实体所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。只有配置]{style="font-family:宋体"}**[snmp-agent]{lang="EN-US"}**[ **remote**]{lang="EN-US"}[命令且绑定了]{style="font-family:宋体"}[VPN]{lang="EN-US"}[时，才显示该信息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1470577582}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **remote**]{lang="EN-US"}]{#struct_0_x1400_15709_x1211557952}

::: {#-2060619115 .myid}
[]{#_Toc404796937}[]{#struct_0_x1400_15709_x477846332}

**SNMP \-- SNMP配置命令 \-- display snmp-agent statistics**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **snmp-agent** **statistics**]{lang="EN-US"}]{#struct_0_x1400_15709_x1398556857}[命令用来显示]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[报文的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_320023012}

[**[display]{lang="EN-US"}**[ **snmp-agent** **statistics**]{lang="EN-US"}]{#struct_0_x1400_15709_1653807912}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x677776436}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_x489767360}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1553441500}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_751153137}

[[network-operator]{lang="EN-US"}]{#struct_0_x1400_15709_656045689}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_74707195}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1400_15709_x1399539897}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_594422803}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_74831849}[显示]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[报文的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display snmp-agent statistics]{lang="EN-US"}]{#struct_0_x1400_15709_x1399474361}

[  1684 messages delivered to the SNMP entity.]{lang="EN-US"}

[  5 messages were for an unsupported version.]{lang="EN-US"}

[  0 messages used an unknown SNMP community name.]{lang="EN-US"}

[  0 messages represented an illegal operation for the community supplied.]{lang="EN-US"}

[  0 ASN.1 or BER errors in the process of decoding.]{lang="EN-US"}

[  1679 messages passed from the SNMP entity.]{lang="EN-US"}

[  0 SNMP PDUs had badValue error-status.]{lang="EN-US"}

[  0 SNMP PDUs had genErr error-status.]{lang="EN-US"}

[  0 SNMP PDUs had noSuchName error-status.]{lang="EN-US"}

[  0 SNMP PDUs had tooBig error-status (Maximum packet size 1500).]{lang="EN-US"}

[  16544 MIB objects retrieved successfully.]{lang="EN-US"}

[  2 MIB objects altered successfully.]{lang="EN-US"}

[  7 GetRequest-PDU accepted and processed.]{lang="EN-US"}

[  7 GetNextRequest-PDU accepted and processed.]{lang="EN-US"}

[  1653 GetBulkRequest-PDU accepted and processed.]{lang="EN-US"}

[  1669 GetResponse-PDU accepted and processed.]{lang="EN-US"}

[  2 SetRequest-PDU accepted and processed.]{lang="EN-US"}

[  0 Trap PDUs accepted and processed.]{lang="EN-US"}

[  0 alternate Response Class PDUs dropped silently.]{lang="EN-US"}

[  0 forwarded Confirmed Class PDUs dropped silently.]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[display snmp-agent statistics]{lang="EN-US"}]{#struct_0_x1400_15709_x851029892}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1603695493}[[字段]{style="font-family:黑体"}]{#struct_0_x1400_15709_1862083033}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1015369314}

[[messages delivered to the SNMP entity]{lang="EN-US"}]{#struct_0_x1400_15709_x1683563523}

[[Agent]{lang="EN-US"}]{#struct_0_x1400_15709_x1578358538}[收到的数据报文个数]{style="font-family:宋体"}

[[messages were for an unsupported version]{lang="EN-US"}]{#struct_0_x1400_15709_x1399015612}

[[版本不支持的数据报文个数]{style="font-family:宋体"}]{#struct_0_x1400_15709_575728594}

[[messages used an unknown SNMP community name]{lang="EN-US"}]{#struct_0_x1400_15709_x411447997}

[[使用了非法团体名的数据报文个数]{style="font-family:宋体"}]{#struct_0_x1400_15709_126633791}

[[messages represented an illegal operation for the community supplied]{lang="EN-US"}]{#struct_0_x1400_15709_2003141677}

[[包含了超出团体名权限的操作的数据报文个数]{style="font-family:宋体"}]{#struct_0_x1400_15709_x686519396}

[[ASN.1 or BER errors in the process of decoding]{lang="EN-US"}]{#struct_0_x1400_15709_x1398950076}

[[在解码过程中发生]{style="font-family:宋体"}[ASN.1]{lang="EN-US"}]{#struct_0_x1400_15709_x1521836425}[（]{style="font-family:宋体"}[Abstract Syntax Notation dot one]{lang="EN-US"}[，抽象记法]{style="font-family:宋体"}[1]{lang="EN-US"}[）或]{style="font-family:宋体"}[BER]{lang="EN-US"}[（]{style="font-family:宋体"}[Basic Encoding Rules ]{lang="EN-US"}[，基本编码规则）错误的数据报文个数]{style="font-family:宋体"}

[[messages passed from the SNMP entity]{lang="EN-US"}]{#struct_0_x1400_15709_1257475035}

[[Agent]{lang="EN-US"}]{#struct_0_x1400_15709_872930695}[发送给别的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体的数据报文个数]{style="font-family:宋体"}

[[SNMP PDUs had badValue error-status]{lang="EN-US"}]{#struct_0_x1400_15709_x1255578472}

[[错误类型为]{style="font-family:宋体"}[BadValues]{lang="EN-US"}]{#struct_0_x1400_15709_x1398884540}[的数据报文个数]{style="font-family:宋体"}

[[SNMP PDUs had genErr error-status]{lang="EN-US"}]{#struct_0_x1400_15709_1741992027}

[[genErr]{lang="EN-US"}]{#struct_0_x1400_15709_x2115872390}[错误的数据报文个数]{style="font-family:宋体"}

[[SNMP PDUs had noSuchName error-status]{lang="EN-US"}]{#struct_0_x1400_15709_x2001349175}

[[NoSuchName]{lang="EN-US"}]{#struct_0_x1400_15709_x342418482}[错误的数据报文个数]{style="font-family:宋体"}

[[SNMP PDUs had tooBig error-status]{lang="EN-US"}]{#struct_0_x1400_15709_x1398819004}

[[TooBig]{lang="EN-US"}]{#struct_0_x1400_15709_2083848897}[错误的数据报文个数]{style="font-family:宋体"}

[[MIB objects retrieved successfully]{lang="EN-US"}]{#struct_0_x1400_15709_1165870362}

[[已成功获取的]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_x1400_15709_2045203146}[对象个数]{style="font-family:宋体"}

[[MIB objects altered successfully]{lang="EN-US"}]{#struct_0_x1400_15709_x562969996}

[[已成功修改的]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_x1400_15709_x1398753468}[对象个数]{style="font-family:宋体"}

[[GetRequest-PDU accepted and processed]{lang="EN-US"}]{#struct_0_x1400_15709_1844926997}

[[已接收并处理的]{style="font-family:宋体"}[Get]{lang="EN-US"}]{#struct_0_x1400_15709_1532790550}[请求的个数]{style="font-family:宋体"}

[[GetNextRequest-PDU accepted and processed]{lang="EN-US"}]{#struct_0_x1400_15709_1801131188}

[[已接收并处理的]{style="font-family:宋体"}[GetNext]{lang="EN-US"}]{#struct_0_x1400_15709_x1398687932}[请求的个数]{style="font-family:宋体"}

[[GetBulkRequest-PDU accepted and processed]{lang="EN-US"}]{#struct_0_x1400_15709_x1511155299}

[[已接收并处理的]{style="font-family:宋体"}[GetBulk]{lang="EN-US"}]{#struct_0_x1400_15709_194442027}[请求的个数]{style="font-family:宋体"}

[[GetResponse-PDU accepted and processed]{lang="EN-US"}]{#struct_0_x1400_15709_x663731377}

[[已接收并处理的]{style="font-family:宋体"}[Get]{lang="EN-US"}]{#struct_0_x1400_15709_x1398622396}[响应的个数]{style="font-family:宋体"}

[[SetRequest-PDU accepted and processed]{lang="EN-US"}]{#struct_0_x1400_15709_x1314082923}

[[已接收并处理的]{style="font-family:宋体"}[Set]{lang="EN-US"}]{#struct_0_x1400_15709_1549995444}[请求的个数]{style="font-family:宋体"}

[[Trap PDUs accepted and processed]{lang="EN-US"}]{#struct_0_x1400_15709_196863201}

[[已接收并处理的]{style="font-family:宋体"}[Trap]{lang="EN-US"}]{#struct_0_x1400_15709_x1398556860}[和]{style="font-family:宋体"}[Inform]{lang="EN-US"}[报文的个数]{style="font-family:宋体"}

[[alternate Response Class PDUs dropped silently]{lang="EN-US"}]{#struct_0_x1400_15709_1886303561}

[[被丢弃的响应数据报文个数]{style="font-family:宋体"}]{#struct_0_x1400_15709_x613022984}

[[forwarded Confirmed Class PDUs dropped silently]{lang="EN-US"}]{#struct_0_x1400_15709_650307706}

[[被丢弃的转发数据报文个数]{style="font-family:宋体"}]{#struct_0_x1400_15709_x1399539900}

[ ]{lang="EN-US"}

::: {#-1264282277 .myid}
[]{#_Toc404796938}[]{#struct_0_x1400_15709_x165550835}

**SNMP \-- SNMP配置命令 \-- display snmp-agent sys-info**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **snmp-agent** **sys-info**]{lang="EN-US"}]{#struct_0_x1400_15709_x1827331804}[命令用来显示当前]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[设备的系统信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1655315519}

[**[display]{lang="EN-US"}**[ **snmp-agent** **sys-info** \[ **contact** \| **location** \| **version** \] \*]{lang="EN-US"}]{#struct_0_x1400_15709_x1249714645}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1987435670}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_x666572986}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1399474364}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x447745365}

[[network-operator]{lang="EN-US"}]{#struct_0_x1400_15709_x2117094498}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_1910006034}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1400_15709_x2087719332}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x976952258}

[**[contact]{lang="EN-US"}**]{#struct_0_x1400_15709_x1754338281}[：显示当前设备维护者的联系信息。]{style="font-family:宋体"}

[**[location]{lang="EN-US"}**]{#struct_0_x1400_15709_x1239159997}[：显示当前设备的物理位置信息。]{style="font-family:宋体"}

[**[version]{lang="EN-US"}**]{#struct_0_x1400_15709_x1399015611}[：显示当前设备中运行的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[版本号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x990355347}

[[不指定参数时，显示设备的全部系统信息。]{style="font-family:宋体"}]{#struct_0_x1400_15709_851739545}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_660045028}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_x1348336264}[显示设备系统信息。]{style="font-family:宋体"}

[[\<Sysname\> display snmp-agent sys-info]{lang="EN-US"}]{#struct_0_x1400_15709_x63457391}

[   The contact information of the agent:]{lang="EN-US"}

[           Hangzhou H3C Technologies Co., Ltd.]{lang="EN-US"}

[ ]{lang="EN-US"}

[   The location information of the agent:]{lang="EN-US"}

[           Hangzhou, China]{lang="EN-US"}

[ ]{lang="EN-US"}

[   The SNMP version of the agent:]{lang="EN-US"}

[     SNMPv3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x161261811}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **sys-info**]{lang="EN-US"}]{#struct_0_x1400_15709_x1398950075}
:::

::: {#-887578282 .myid}
[]{#_Toc404796939}[]{#struct_0_x1400_15709_1207046930}

**SNMP \-- SNMP配置命令 \-- display snmp-agent trap queue**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **snmp-agent** **trap** **queue**]{lang="EN-US"}]{#struct_0_x1400_15709_1244007713}[命令用来显示告警信息队列的基本信息，包括队列长度和队列中当前告警信息的数量。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1244265678}

[**[display]{lang="EN-US"}**[ **snmp-agent** **trap** **queue**]{lang="EN-US"}]{#struct_0_x1400_15709_64546376}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1221729236}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_x1023510436}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x928837297}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x1398884539}

[[network-operator]{lang="EN-US"}]{#struct_0_x1400_15709_531810766}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x908826473}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1400_15709_1544280857}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1671906332}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_1799548802}[显示当前告警信息队列的配置及使用情况。]{style="font-family:宋体"}

[[\<Sysname\> display snmp-agent trap queue]{lang="EN-US"}]{#struct_0_x1400_15709_1729803057}

[   Queue size: 100]{lang="EN-US"}

[   Message number: 6]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[display snmp-agent trap queue]{lang="EN-US"}]{#struct_0_x1400_15709_316313773}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1601713381}[[字段]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1398819003}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1400_15709_517764956}

[[Queue size]{lang="EN-US"}]{#struct_0_x1400_15709_x616166568}

[[告警信息队列长度]{style="font-family:宋体"}]{#struct_0_x1400_15709_1117240141}

[[Message number]{lang="EN-US"}]{#struct_0_x1400_15709_x211155605}

[[告警信息队列中当前告警信息的个数]{style="font-family:宋体"}]{#struct_0_x1400_15709_603271147}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1544389105}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **trap** **life**]{lang="EN-US"}]{#struct_0_x1400_15709_x1398753467}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **trap** **queue-size**]{lang="EN-US"}]{#struct_0_x1400_15709_x77387304}

::: {#-791797460 .myid}
[]{#_Toc404796940}[]{#struct_0_x1400_15709_x1259047015}

**SNMP \-- SNMP配置命令 \-- display snmp-agent trap-list**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **snmp-agent** **trap-list**]{lang="EN-US"}]{#struct_0_x1400_15709_x1779260276}[命令用来显示设备当前可以生成告警信息的模块及其告警信息的使能状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1391336326}

[**[display]{lang="EN-US"}**[ **snmp-agent** **trap-list**]{lang="EN-US"}]{#struct_0_x1400_15709_x1355070968}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1632951824}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_359374682}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x786744955}

[[如果一个模块包含多个子模块，只要有任何一个子模块的告警信息是使能的，就显示整个模块是使能的。]{style="font-family:宋体"}]{#struct_0_x1400_15709_x1398687931}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_54928642}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_1582504656}[显示设备当前可以生成告警信息的模块及其告警信息的使能状态。（本命令的显示信息与设备的型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}

[[\<Sysname\> display snmp-agent trap-list]{lang="EN-US"}]{#struct_0_x1400_15709_x570799819}

[   Standard notification is enabled.]{lang="EN-US"}

[ ]{lang="EN-US"}

[   Enabled notifications: 1; Disabled notifications: 0]{lang="EN-US"}

[[以上显示信息中]{style="font-family:宋体"}[enable]{lang="EN-US"}]{#struct_0_x1400_15709_x925374163}[表示允许该模块生成告警信息，]{style="font-family:宋体"}[disable]{lang="EN-US"}[表示不允许该模块生成告警信息。]{style="font-family:宋体"}[enable]{lang="EN-US"}[或者]{style="font-family:宋体"}[disable]{lang="EN-US"}[可以通过命令行配置。]{style="font-family:宋体"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_407776913}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **trap** **enable**]{lang="EN-US"}]{#struct_0_x1400_15709_353961715}
:::

::: {#-2110730190 .myid}
[]{#_Toc404796941}[]{#struct_0_x1400_15709_225685262}

**SNMP \-- SNMP配置命令 \-- display snmp-agent usm-user**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **snmp-agent** **usm-user**]{lang="EN-US"}]{#struct_0_x1400_15709_x1398622395}[命令用来显示]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1717367450}

[**[display]{lang="EN-US"}**[ **snmp-agent** **usm-user** \[ **engineid** *engineid* \| **group** *group-name* \| **username** *user-name* \] \*]{lang="EN-US"}]{#struct_0_x1400_15709_1449770353}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1164229766}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_x1064623454}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_639381712}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_101953741}

[[network-operator]{lang="EN-US"}]{#struct_0_x1400_15709_607877406}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x1398556859}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1400_15709_x486546042}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x597021179}

[**[engineid]{lang="EN-US"}**[ *engineid*]{lang="EN-US"}]{#struct_0_x1400_15709_x658853724}[：显示指定引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[的]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户信息，]{style="font-family:宋体"}*[engineid]{lang="EN-US"}*[表示]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户创建的时候，系统会记录当时设备的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[，如果设备的引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[被修改，则被创建的]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户将暂时无效，只有引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[恢复后，才能继续生效。]{style="font-family:宋体"}

[**[group]{lang="EN-US"}**[ *group-name*]{lang="EN-US"}]{#struct_0_x1400_15709_x1526098627}[：显示属于指定]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[组的]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户信息，区分大小写。]{style="font-family:宋体"}

[**[username]{lang="EN-US"}**[ *user-name*]{lang="EN-US"}]{#struct_0_x1400_15709_760600354}[：显示指定名字的]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户信息，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_200971724}

[[使用]{style="font-family:宋体"}**[snmp-agent]{lang="EN-US"}**[ **usm-user**]{lang="EN-US"}]{#struct_0_x1400_15709_1618048287}[命令可以创建]{style="font-family:宋体"}[SNMPv1/v2c/v3]{lang="EN-US"}[用户，如果创建是的]{style="font-family:宋体"}[SNMPv1/v2c]{lang="EN-US"}[用户，系统自动添加一个新的同名的团体名，并将这个用户当成]{style="font-family:宋体"}[SNMPv1/v2c]{lang="EN-US"}[团体来处理。所以，不能通过]{style="font-family:宋体"}**[display]{lang="EN-US"}**[ **snmp-agent** **usm-user**]{lang="EN-US"}[命令来查看]{style="font-family:宋体"}[SNMPv1/v2c]{lang="EN-US"}[用户的信息，能通过]{style="font-family:宋体"}**[display]{lang="EN-US"}**[ **snmp-agent** **community**]{lang="EN-US"}[查看]{style="font-family:
宋体"}[SNMPv1/v2c]{lang="EN-US"}[用户对应的团体的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1714596340}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_x1399539899}[显示设备上已创建的所有]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户的信息。]{style="font-family:宋体"}

[[\<Sysname\> display snmp-agent usm-user]{lang="EN-US"}]{#struct_0_x1400_15709_1044761497}

[   Username: userv3]{lang="EN-US"}

[   Group name: mygroupv3]{lang="EN-US"}

[       Engine ID: 800063A203000FE240A1A6]{lang="EN-US"}

[       Storage type: nonVolatile]{lang="EN-US"}

[       User status: active]{lang="EN-US"}

[       ACL: 2000]{lang="EN-US"}

[ ]{lang="EN-US"}

[   Username: userv3]{lang="EN-US"}

[   Group name: mygroupv3]{lang="EN-US"}

[       Engine ID: 8000259503000BB3100A508]{lang="EN-US"}

[       Storage type: nonVolatile]{lang="EN-US"}

[       User status: active]{lang="EN-US"}

[       ACL name: testacl]{lang="EN-US"}

[ ]{lang="EN-US"}

[   Username: userv3code]{lang="EN-US"}

[   Role name: groupv3code]{lang="EN-US"}

[              network-operator]{lang="EN-US"}

[       Engine ID: 800063A203000FE240A1A6]{lang="EN-US"}

[       Storage type: nonVolatile]{lang="EN-US"}

[       User status: active]{lang="EN-US"}

[ ]{lang="EN-US"}

[   Username: userv3code]{lang="EN-US"}

[   Role name: snmprole]{lang="EN-US"}

[              network-operator]{lang="EN-US"}

[       Engine ID: 800063A280000002BB0001]{lang="EN-US"}

[       Storage type: nonVolatile]{lang="EN-US"}

[       User status: active]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[display snmp-agent usm-user]{lang="EN-US"}]{#struct_0_x1400_15709_x1389119479}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1601026629}[[字段]{style="font-family:黑体"}]{#struct_0_x1400_15709_1677854023}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1400_15709_x892139924}

[[Username]{lang="EN-US"}]{#struct_0_x1400_15709_x1399474363}

[[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_311769522}[用户的用户名]{style="font-family:宋体"}

[[Group name]{lang="EN-US"}]{#struct_0_x1400_15709_1327848120}

[[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_x1566713934}[用户所在组的组名]{style="font-family:宋体"}

[[Role name]{lang="EN-US"}]{#struct_0_x1400_15709_1954855323}

[[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_x2087527164}[用户的角色名称]{style="font-family:宋体"}

[[Engine ID]{lang="EN-US"}]{#struct_0_x1400_15709_x1970066769}

[[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_x1634843043}[用户创建时使用的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Storage type]{lang="EN-US"}]{#struct_0_x1400_15709_x1399015614}

[[存储方式，分为以下几种：]{style="font-family:宋体"}[volatile]{lang="EN-US"}]{#struct_0_x1400_15709_x587070820}[、]{style="font-family:宋体"}[nonVolatile]{lang="EN-US"}[、]{style="font-family:宋体"}[permanent]{lang="EN-US"}[、]{style="font-family:宋体"}[readOnly]{lang="EN-US"}[、]{style="font-family:宋体"}[other]{lang="EN-US"}[，具体请参见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-1]{lang="EN-US"}](?1188054656#_Ref291745733)

[[User status]{lang="EN-US"}]{#struct_0_x1400_15709_341853191}

[[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_x1286698898}[用户的状态，分为以下几种：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_x1400_15709_1624255902}[：有效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[notInService]{lang="EN-US"}]{#struct_0_x1400_15709_498652752}[：当前不可用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[notReady]{lang="EN-US"}]{#struct_0_x1400_15709_x1398950078}[：未配置完成]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[other]{lang="EN-US"}]{#struct_0_x1400_15709_1966561817}[：其他]{lang="EN-US" style="font-family:宋体"}

[[ACL]{lang="EN-US"}]{#struct_0_x1400_15709_892258245}

[[使用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x1400_15709_144258645}[列表的编号（该字段仅在用户与]{style="font-family:宋体"}[ACL]{lang="EN-US"}[绑定后显示，不会与]{style="font-family:宋体"}[ACL name]{lang="EN-US"}[同时存在）]{style="font-family:宋体"}

[[ACL name]{lang="EN-US"}]{#struct_0_x1400_15709_1543426996}

[[使用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x1400_15709_684689336}[列表的名称（该字段仅在用户与]{style="font-family:宋体"}[ACL]{lang="EN-US"}[名称绑定后显示，不会与]{style="font-family:宋体"}[ACL]{lang="EN-US"}[同时存在）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1106344050}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **usm-user** **v3**]{lang="EN-US"}]{#struct_0_x1400_15709_x330840228}

::: {#143449593 .myid}
[]{#_Toc404796942}[]{#struct_0_x1400_15709_x1398884542}

**SNMP \-- SNMP配置命令 \-- enable snmp trap updown**

------------------------------------------------------------------------

[**[enable]{lang="EN-US"}**[ **snmp** **trap** **updown**]{lang="EN-US"}]{#struct_0_x1400_15709_x1390175855}[命令用来开启接口状态变化的告警功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **enable** **snmp** **trap** **updown**]{lang="EN-US"}]{#struct_0_x1400_15709_1255111872}[命令用来关闭接口状态变化的告警功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1405268058}

[**[enable]{lang="EN-US"}**[ **snmp** **trap** **updown**]{lang="EN-US"}]{#struct_0_x1400_15709_848677127}

[**[undo]{lang="EN-US"}**[ **enable** **snmp** **trap** **updown**]{lang="EN-US"}]{#struct_0_x1400_15709_1346241932}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1407272784}

[[接口状态变化的告警功能处于开启状态。]{style="font-family:宋体"}]{#struct_0_x1400_15709_x332928882}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x786135080}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_x1398819006}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_921049483}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_1393751222}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x1767515030}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x2006303598}

[[需要注意的是，如果要求接口在状态发生改变时生成接口状态变化的告警信息，需要开启全局告警功能并在接口开启接口状态变化的告警功能。接口下开启请使用命令]{style="font-family:宋体"}**[enable]{lang="EN-US"}**[ **snmp** **trap** **updown**]{lang="EN-US"}]{#struct_0_x1400_15709_178013104}[，全局下开启请使用命令]{style="font-family:宋体"}**[snmp-agent]{lang="EN-US"}**[ **trap** **enable** **standard** \[ **linkdown** \| **linkup** \] \*]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1398753470}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_1488631101}[允许发送端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[linkUp/linkDown]{lang="EN-US"}[的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[告警，使用团体名]{style="font-family:宋体"}[public]{lang="EN-US"}[，向]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[的目的主机发送]{style="font-family:宋体"}[Trap]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_x403969077}

[\[Sysname\] snmp-agent trap enable]{lang="EN-US"}

[\[Sysname\] snmp-agent target-host trap address udp-domain 10.1.1.1 params securityname public]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] enable snmp trap updown]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x984347851}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **target-host**]{lang="EN-US"}]{#struct_0_x1400_15709_890872415}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **trap** **enable**]{lang="EN-US"}]{#struct_0_x1400_15709_1518407639}
:::

::: {#-1685889571 .myid}
[]{#_Toc404796943}[]{#struct_0_x1400_15709_x1047824066}

**SNMP \-- SNMP配置命令 \-- snmp-agent**

------------------------------------------------------------------------

[**[snmp-agent]{lang="EN-US"}**]{#struct_0_x1400_15709_x1398687934}[命令用来开启]{style="font-family:宋体"}[SNMP Agent]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp-agent**]{lang="EN-US"}]{#struct_0_x1400_15709_x348355885}[命令用来关闭]{style="font-family:宋体"}[SNMP Agent]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1873916708}

[**[snmp-agent]{lang="EN-US"}**]{#struct_0_x1400_15709_x1297223806}

[**[undo]{lang="EN-US"}**[ **snmp-agent**]{lang="EN-US"}]{#struct_0_x1400_15709_1073445132}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1787391403}

[[SNMP Agent]{lang="EN-US"}]{#struct_0_x1400_15709_909661323}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_605755455}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_637613142}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1398622398}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_1461854599}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x1665456841}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1914075675}

[[执行除]{style="font-family:宋体"}**[snmp-agent]{lang="EN-US"}**[ **calculate-password**]{lang="EN-US"}]{#struct_0_x1400_15709_x613629936}[外任何以]{style="font-family:宋体"}[snmp-agent]{lang="EN-US"}[开头的命令都可以开启]{style="font-family:宋体"}[SNMP Agent]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x559676646}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_x1979959508}[开启设备的]{style="font-family:宋体"}[SNMP Agent]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_x1398556862}

[\[Sysname\] snmp-agent]{lang="EN-US"}
:::

::: {#-251404023 .myid}
[]{#_Toc404796944}[]{#struct_0_x1400_15709_723504147}

**SNMP \-- SNMP配置命令 \-- snmp-agent calculate-password**

------------------------------------------------------------------------

[**[snmp-agent]{lang="EN-US"}**[ **calculate-password**]{lang="EN-US"}]{#struct_0_x1400_15709_x322992389}[命令用来计算用户给定明文密码通过加密算法处理后得到的密文密码所对应摘要。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1345852677}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_x1400_15709_1707157819}[模式下：]{style="font-family:宋体"}

[**[snmp-agent]{lang="EN-US"}**[ **calculate-password** *plain-password* **mode** { **3desmd5** \| **3dessha** \| **md5** \| **sha** } { **local-engineid** \| **specified-engineid** *engineid* }]{lang="EN-US"}]{#struct_0_x1400_15709_1516470682}

[[FIPS]{lang="EN-US"}]{#struct_0_x1400_15709_x2074868568}[模式下：]{style="font-family:宋体"}

[**[snmp-agent]{lang="EN-US"}**[ **calculate-password** *plain-password* **mode** **sha** { **local-engineid** \| **specified-engineid** *engineid* }]{lang="EN-US"}]{#struct_0_x1400_15709_1531215439}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x765145516}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_x1399539902}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_997248579}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_2038476787}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_1891114976}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1238947075}

[*[plain-password]{lang="EN-US"}*]{#struct_0_x1400_15709_x754390094}[：需要被加密的明文密码。]{style="font-family:宋体"}

[**[mode]{lang="EN-US"}**]{#struct_0_x1400_15709_102625854}[：指明使用的认证算法或加密算法。]{style="font-family:宋体"}[AES]{lang="EN-US"}[、]{style="font-family:宋体"}[3DES]{lang="EN-US"}[和]{style="font-family:宋体"}[DES]{lang="EN-US"}[是加密算法，这三个加密算法的安全性由高到低依次是：]{style="font-family:宋体"}[AES]{lang="EN-US"}[、]{style="font-family:宋体"}[3DES]{lang="EN-US"}[、]{style="font-family:宋体"}[DES]{lang="EN-US"}[，安全性高的加密算法实现机制复杂，运算速度慢。对于普通的安全要求，]{style="font-family:宋体"}[DES]{lang="EN-US"}[算法就可以满足需要；]{style="font-family:宋体"} [MD5]{lang="EN-US"}[和]{style="font-family:宋体"}[SHA-1]{lang="EN-US"}[是认证算法，其中]{style="font-family:宋体"}[MD5]{lang="EN-US"}[算法的计算速度比]{style="font-family:宋体"}[SHA-1]{lang="EN-US"}[算法快，而]{style="font-family:宋体"}[SHA-1]{lang="EN-US"}[算法的安全强度比]{style="font-family:宋体"}[MD5]{lang="EN-US"}[算法高。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[3desmd5]{lang="EN-US"}**]{#struct_0_x1400_15709_1954789787}[：用于将明文密码转换为密文密码，此时对应的认证算法必须为]{style="font-family:
宋体"}[MD5]{lang="EN-US"}[，加密协议必须为]{style="font-family:宋体"}[3DES]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[3dessha]{lang="EN-US"}**]{#struct_0_x1400_15709_1380930789}[：用于将明文密码转换为密文密码，此时对应的认证算法必须为]{style="font-family:
宋体"}[SHA-1]{lang="EN-US"}[，加密协议必须为]{style="font-family:宋体"}[3DES]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[md5]{lang="EN-US"}**]{#struct_0_x1400_15709_x869476098}[：用于将明文认证密码转换为密文认证密码，此时对应的认证算法必须为]{style="font-family:
宋体"}[MD5]{lang="EN-US"}[；或者用于将明文加密密码转换为密文加密密码，此时对应的认证算法必须为]{style="font-family:宋体"}[MD5]{lang="EN-US"}[，加密协议可以为]{style="font-family:宋体"}[AES]{lang="EN-US"}[也可以是]{style="font-family:宋体"}[DES]{lang="EN-US"}[（当认证协议为]{style="font-family:宋体"}[MD5]{lang="EN-US"}[时，加密协议不管是]{style="font-family:宋体"}[AES]{lang="EN-US"}[还是]{style="font-family:宋体"}[DES]{lang="EN-US"}[，转换后的结果是一样的）。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sha]{lang="EN-US"}**]{#struct_0_x1400_15709_476830957}[：用于将明文认证密码转换为密文认证密码，此时对应的认证算法必须为]{style="font-family:
宋体"}[SHA-1]{lang="EN-US"}[；或者用于将明文加密密码转换为密文加密密码，此时对应的认证算法必须为]{style="font-family:宋体"}[SHA-1]{lang="EN-US"}[，加密协议可以为]{style="font-family:宋体"}[AES]{lang="EN-US"}[也可以是]{style="font-family:宋体"}[DES]{lang="EN-US"}[（当认证协议为]{style="font-family:宋体"}[SHA-1]{lang="EN-US"}[时，加密协议不管是]{style="font-family:宋体"}[AES]{lang="EN-US"}[还是]{style="font-family:宋体"}[DES]{lang="EN-US"}[，转换后的结果是一样的）。]{style="font-family:宋体"}

[**[local-engineid]{lang="EN-US"}**]{#struct_0_x1400_15709_x1399474366}[：使用本地引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[计算密文密码，引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[的相关描述与配置可参考命令]{style="font-family:宋体"}**[snmp-agent]{lang="EN-US"}**[ **local-engineid**]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[specified-engineid]{lang="EN-US"}**]{#struct_0_x1400_15709_715054049}[：使用用户指定的引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[计算密文密码。]{style="font-family:宋体"}

[*[engineid]{lang="EN-US"}*]{#struct_0_x1400_15709_x792392975}[：引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[，必须为偶数个十六进制数，偶数的取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[。全]{style="font-family:宋体"}[0]{lang="EN-US"}[和全]{style="font-family:宋体"}[F]{lang="EN-US"}[均被认为是无效参数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1694810970}

[[执行本命令前，必须先开启设备的]{style="font-family:宋体"}[SNMP Agent]{lang="EN-US"}]{#struct_0_x1400_15709_x765068937}[功能。]{style="font-family:宋体"}

[[在创建]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}]{#struct_0_x1400_15709_x659719286}[用户时，如果指明认证或者加密密码采用密文形式，则可以借助此命令生成相应的密文密码所对应的摘要。]{style="font-family:宋体"}

[[生成的密码是和引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1400_15709_x41671952}[相关联的，在某一引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[下生成的密码，也只在此引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[下生效。]{style="font-family:宋体"}

[[通过该命令可以得到密文密码对应的摘要，从而在配置用户时使用摘要，避免由于输入明文密码造成的安全隐患，同时由于密码可以解密，摘要不可逆，所以增强了安全性。]{style="font-family:宋体"}]{#struct_0_x1400_15709_x1457293741}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_2006057727}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_x964922052}[使用本地引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[和]{style="font-family:宋体"}[SHA-1]{lang="EN-US"}[认证算法计算明文为]{style="font-family:宋体"}[authkey]{lang="EN-US"}[的加密密码所对应摘要。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_x1399015613}

[\[Sysname\] snmp-agent calculate-password authkey mode sha local-engineid]{lang="EN-US"}

[The encrypted key is: 09659EC5A9AE91BA189E5845E1DDE0CC]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_2141812535}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **local-engineid**]{lang="EN-US"}]{#struct_0_x1400_15709_x513192678}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **usm-user** **v3**]{lang="EN-US"}]{#struct_0_x1400_15709_512485600}
:::

::: {#-673923415 .myid}
[]{#_Toc404796945}[]{#struct_0_x1400_15709_x1678755778}

**SNMP \-- SNMP配置命令 \-- snmp-agent community**

------------------------------------------------------------------------

[**[snmp-agent]{lang="EN-US"}**[ **community**]{lang="EN-US"}]{#struct_0_x1400_15709_x1550934032}[命令用来创建一个新的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[团体，并设置该团体的参数，包括访问权限、配置团体名方式、访问控制列表和可访问的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **community**]{lang="EN-US"}]{#struct_0_x1400_15709_1153445974}[命令用来删除指定的团体。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_694410627}

[[VACM]{lang="EN-US"}]{#struct_0_x1400_15709_1955379611}[方式：]{style="font-family:宋体"}

[**[snmp-agent]{lang="EN-US"}**[ **community** { **read** \| **write** } \[ **simple** \| **cipher** \] *community-name* \[ **mib-view** *view-name* \] \[ **acl** { *acl-number* \| **name** *acl-name* } \| **acl** **ipv6** { *ipv6-acl-number \|* **name** *ipv6-acl-name* } \] \*]{lang="EN-US"}]{#struct_0_x1400_15709_x1398950077}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **community** { **read** \| **write** } \[ **cipher** \] *community-name*]{lang="EN-US"}]{#struct_0_x1400_15709_44247516}

[[RBAC]{lang="EN-US"}]{#struct_0_x1400_15709_573199730}[方式：]{style="font-family:宋体"}

[**[snmp-agent]{lang="EN-US"}**[ **community** \[ **simple** \| **cipher** \] *community-name* **user-role** *role-name* \[ **acl** { *acl-number* \| **name** *acl-name* } \| **acl** **ipv6** { *ipv6-acl-number \|* **name** *ipv6-acl-name* } \] \*]{lang="EN-US"}]{#struct_0_x1400_15709_1955445147}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **community** \[ **cipher** \] *community-name*]{lang="EN-US"}]{#struct_0_x1400_15709_x1305944702}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1886742496}

[[设备上没有配置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_x1252563537}[团体。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1591134784}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_x1091163407}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_673807813}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x378758038}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x1398884541}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1400_15709_175908086}

[**[read]{lang="EN-US"}**]{#struct_0_x1400_15709_x1010162410}[：表示对]{style="font-family:宋体"}[MIB]{lang="EN-US"}[对象的访问权限为只读。]{style="font-family:宋体"}[NMS]{lang="EN-US"}[使用该团体名访问]{style="font-family:宋体"}[Agent]{lang="EN-US"}[时只能执行读操作。]{style="font-family:宋体"}

[**[write]{lang="EN-US"}**]{#struct_0_x1400_15709_x835080799}[：表示对]{style="font-family:宋体"}[MIB]{lang="EN-US"}[对象的访问权限为读写。]{style="font-family:宋体"}[NMS]{lang="EN-US"}[使用该团体名访问]{style="font-family:宋体"}[Agent]{lang="EN-US"}[时可以执行读、写操作。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_x1400_15709_1116266918}[：表示以明文方式配置团体名并以密文方式保存到配置文件中，缺省情况下，表示以明文方式配置团体名，并以明文方式保存到配置文件。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_x1400_15709_x1398819005}[：表示以密文方式配置团体名并以密文方式保存到配置文件中，缺省情况下，表示以明文方式配置团体名，并以明文方式保存到配置文件。]{style="font-family:宋体"}

[*[community-name]{lang="EN-US"}*]{#struct_0_x1400_15709_x645034458}[：设置明文团体名或密文团体名，是限制]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问]{style="font-family:宋体"}[Agent]{lang="EN-US"}[时所使用的团体名。区分大小写，需要转义的字符请加"]{style="font-family:宋体"}[\\]{lang="EN-US"}["后输入。当以明文方式配置时，团体名为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串；当以密文方式配置时，团体名为]{style="font-family:宋体"}[33]{lang="EN-US"}[～]{style="font-family:宋体"}[73]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[**[mib-view]{lang="EN-US"}**[ *view-name*]{lang="EN-US"}]{#struct_0_x1400_15709_x1777910278}[：用来指定]{style="font-family:宋体"}[NMS]{lang="EN-US"}[可以访问的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[对象的范围，]{style="font-family:宋体"}*[view-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MIB]{lang="EN-US"}[视图名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串。不指定参数时，缺省视图为]{style="font-family:宋体"}[ViewDefault]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[user-role]{lang="EN-US"}**[ *role-name*]{lang="EN-US"}]{#struct_0_x1400_15709_1954855330}[：该团体对应的角色名称，]{style="font-family:宋体"}*[role-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[acl]{lang="EN-US"}**[ *acl-number*]{lang="EN-US"}]{#struct_0_x1400_15709_x592068099}[：将团体名与基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[绑定，限制了只有]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址符合条件的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[可以访问]{style="font-family:宋体"}[Agent]{lang="EN-US"}[。]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[表示访问列表号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。当未引用]{style="font-family:宋体"}[ACL]{lang="EN-US"}[或者引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在时，允许所有]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备；当]{style="font-family:宋体"}[ACL]{lang="EN-US"}[为空时，会禁止所有的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备；当引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[非空时，则只有]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中]{style="font-family:宋体"}[permit]{lang="EN-US"}[的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[才能访问设备，其它]{style="font-family:宋体"}[NMS]{lang="EN-US"}[不允许访问设备，以免非法]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备。关于]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的详细描述和介绍请参见"]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{style="font-family:宋体"}[QoS]{lang="EN-US"}[配置指导"中的"]{style="font-family:宋体"}[ACL]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}***[ acl-name]{lang="EN-US"}*]{#struct_0_x1400_15709_x1205146326}[：将团体名与基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[名绑定，]{style="font-family:宋体"}*[acl-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。当未引用]{style="font-family:宋体"}[ACL]{lang="EN-US"}[或者引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在时，允许所有]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备；当]{style="font-family:宋体"}[ACL]{lang="EN-US"}[为空时，会禁止所有的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备；当引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[非空时，则只有]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中]{style="font-family:宋体"}[permit]{lang="EN-US"}[的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[才能访问设备，其它]{style="font-family:宋体"}[NMS]{lang="EN-US"}[不允许访问设备，以免非法]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备。关于]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的详细描述和介绍请参见"]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{style="font-family:宋体"}[QoS]{lang="EN-US"}[配置指导"中的"]{style="font-family:宋体"}[ACL]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[acl]{lang="EN-US"}**[ **ipv6** *ipv6-acl-number*]{lang="EN-US"}]{#struct_0_x1400_15709_x1553432479}[：将团体名与基本]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[绑定，限制了只有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址符合条件的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[可以访问]{style="font-family:宋体"}[Agent]{lang="EN-US"}[。]{style="font-family:宋体"}*[ipv6-acl-number]{lang="EN-US"}*[表示访问列表号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。当未引用]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[或者引用的]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[不存在时，允许所有]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备；当]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[为空时，会禁止]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备；当引用的]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[非空时，则只有]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[中]{style="font-family:宋体"}[permit]{lang="EN-US"}[的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[才能访问设备，其它]{style="font-family:宋体"}[NMS]{lang="EN-US"}[不允许访问设备，以免非法]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}***[ ipv6-acl-name]{lang="EN-US"}*]{#struct_0_x1400_15709_x1205342934}[：将团体名与基本]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[名绑定，]{style="font-family:宋体"}*[acl-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。当未引用]{style="font-family:宋体"}[ACL]{lang="EN-US"}[或者引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在时，允许所有]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备；当]{style="font-family:宋体"}[ACL]{lang="EN-US"}[为空时，会禁止所有的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备；当引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[非空时，则只有]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中]{style="font-family:宋体"}[permit]{lang="EN-US"}[的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[才能访问设备，其它]{style="font-family:宋体"}[NMS]{lang="EN-US"}[不允许访问设备，以免非法]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1649272982}

[[FIPS]{lang="EN-US"}]{#struct_0_x1400_15709_1772793130}[模式下，不支持本命令。]{style="font-family:宋体"}

[[该命令用于]{style="font-family:宋体"}[SNMPv1]{lang="EN-US"}]{#struct_0_x1400_15709_x1398753469}[和]{style="font-family:宋体"}[SNMPv2c]{lang="EN-US"}[组网环境。]{style="font-family:宋体"}

[[系统中可配置的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_1954920866}[团体最多为]{style="font-family:宋体"}[10]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[团体是]{style="font-family:宋体"}[NMS]{lang="EN-US"}]{#struct_0_x1400_15709_x883956358}[和]{style="font-family:宋体"}[Agent]{lang="EN-US"}[的集合，用团体名来标志。团体名相当于密码，团体内的设备通信使用团体名来进行认证。只有]{style="font-family:宋体"}[NMS]{lang="EN-US"}[和]{style="font-family:宋体"}[Agent]{lang="EN-US"}[上配置的团体名相同时，才能互相访问。通常情况下，"]{style="font-family:宋体"}[public]{lang="EN-US"}["被用来作为读权限团体名、"]{style="font-family:宋体"}[private]{lang="EN-US"}["被用来作为写权限团体名。为了增强安全性，网络管理员也可以配置其它团体名。]{style="font-family:宋体"}

[[创建]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_x510057492}[团体时，可以通过两种配置方式来控制团体的访问：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VACM]{lang="EN-US"}]{#struct_0_x1400_15709_x2065086900}[（]{lang="EN-US" style="font-family:宋体"}[View-based Access Control Model]{lang="EN-US"}[，基于视图的访问控制模型）的配置方式，通过]{lang="EN-US" style="font-family:宋体"}**[mib-view]{lang="EN-US"}**[参数限制]{lang="EN-US" style="font-family:宋体"}[NMS]{lang="EN-US"}[可以访问的]{lang="EN-US" style="font-family:宋体"}[Agent]{lang="EN-US"}[上的]{lang="EN-US" style="font-family:宋体"}[MIB]{lang="EN-US"}[对象，名称为]{lang="EN-US" style="font-family:宋体"}*[view-name]{lang="EN-US"}*[的所有]{lang="EN-US" style="font-family:宋体"}[MIB]{lang="EN-US"}[视图都会被访问引用；通过]{lang="EN-US" style="font-family:宋体"}**[read]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[write]{lang="EN-US"}**[参数限制]{lang="EN-US" style="font-family:宋体"}[NMS]{lang="EN-US"}[可以对]{lang="EN-US" style="font-family:宋体"}[Agent]{lang="EN-US"}[执行的操作类型。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RBAC]{lang="EN-US"}]{#struct_0_x1400_15709_1222726384}[（]{lang="EN-US" style="font-family:宋体"}[Role Based Access Control]{lang="EN-US"}[，基于角色的访问控制）的配置方式，通过]{lang="EN-US" style="font-family:宋体"}**[user-role]{lang="EN-US"}**[ *role-name*]{lang="EN-US"}[配置团体的角色。角色定义了]{lang="EN-US" style="font-family:宋体"}[SNMP]{lang="EN-US"}[用户能够访问的]{lang="EN-US" style="font-family:宋体"}[MIB]{lang="EN-US"}[对象以及操作类型（通过]{lang="EN-US" style="font-family:宋体"}**[rule]{lang="EN-US"}**[规则来限定）。]{lang="EN-US" style="font-family:宋体"}[该角色可以是系统中预定义的角色，也可以是用户通过]{style="font-family:宋体"}**[role]{lang="EN-US"}**[命令自定义的角色。有关用户角色的详细信息，请参见"基础配置指导"中的"]{style="font-family:宋体"}[RBAC]{lang="EN-US"}["。]{style="font-family:宋体"}

[[多次使用两种配置方式配置同一团体时，以最后一次的配置方式为准。]{style="font-family:宋体"}]{#struct_0_x1400_15709_860047937}

[[RBAC]{lang="EN-US"}]{#struct_0_x1400_15709_x215198082}[配置方式要求]{style="font-family:宋体"}[NMS]{lang="EN-US"}[在访问]{style="font-family:宋体"}[Agent]{lang="EN-US"}[时，不仅需要授予]{style="font-family:宋体"}[NMS]{lang="EN-US"}[对]{style="font-family:宋体"}[MIB]{lang="EN-US"}[节点的访问权限，还要求团体名]{style="font-family:宋体"}[/]{lang="EN-US"}[用户名所绑定的用户角色具有执行相应操作的权限，而]{style="font-family:宋体"}[VACM]{lang="EN-US"}[方式只需通过]{style="font-family:宋体"}[NMS]{lang="EN-US"}[控制]{style="font-family:宋体"}[MIB]{lang="EN-US"}[节点的访问权限即可，所以推荐使用]{style="font-family:宋体"}[RBAC]{lang="EN-US"}[配置方式，安全性更高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1398687933}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_1217728056}[以明文方式创建]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[团体]{style="font-family:宋体"}[readaccess]{lang="EN-US"}[，并且允许]{style="font-family:宋体"}[NMS]{lang="EN-US"}[使用该团体名对]{style="font-family:宋体"}[Agent]{lang="EN-US"}[进行只读访问。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_x1731155551}

[\[Sysname\] snmp-agent sys-info version v1 v2c]{lang="EN-US"}

[\[Sysname\] snmp-agent community read simple readaccess]{lang="EN-US"}

[[在]{style="font-family:宋体"}[NMS]{lang="EN-US"}]{#struct_0_x1400_15709_1453563104}[上将版本号设置为]{style="font-family:宋体"}[SNMPv1]{lang="EN-US"}[或者]{style="font-family:宋体"}[SNMPv2c]{lang="EN-US"}[，并将只读团体名填写为]{style="font-family:宋体"}[readaccess]{lang="EN-US"}[，建立连接，就可以对设备上缺省视图内的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[对象进行只读操作。]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_x970602851}[以明文方式设置团体名]{style="font-family:宋体"}[writeaccess]{lang="EN-US"}[，并且只允许]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[使用该团体名设置]{style="font-family:宋体"}[Agent MIB]{lang="EN-US"}[对象的值，禁止其它]{style="font-family:宋体"}[NMS]{lang="EN-US"}[使用该团体名执行写操作。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_x1398622397}

[\[Sysname\] acl basic 2001]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2001\] rule permit source 1.1.1.1 0.0.0.0]{lang="EN-US"}

[\[Sysname-acl-]{lang="EN-US"}[ ]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}[ipv4-basic-2001\] rule deny source any]{lang="EN-US"}

[\[Sysname-acl-]{lang="EN-US"}[ ]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}[ipv4-basic-2001\] quit]{lang="EN-US"}

[\[Sysname\] snmp-agent sys-info version v2c]{lang="EN-US"}

[\[Sysname\] snmp-agent community write simple writeaccess acl 2001]{lang="EN-US"}

[[将]{style="font-family:宋体"}[NMS]{lang="EN-US"}]{#struct_0_x1400_15709_1414800432}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址配置为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，版本号指定为]{style="font-family:宋体"}[SNMPv2c]{lang="EN-US"}[，]{style="font-family:宋体"}[Write community]{lang="EN-US"}[选项填写为]{style="font-family:宋体"}[writeaccess]{lang="EN-US"}[，即可以对设备上缺省视图内的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[对象进行读写操作。]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_x1204425430}[以明文方式设置团体名]{style="font-family:宋体"}[writeaccess]{lang="EN-US"}[，并且只允许]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.2]{lang="EN-US"}[的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[使用该团体名设置]{style="font-family:宋体"}[Agent MIB]{lang="EN-US"}[对象的值，禁止其它]{style="font-family:宋体"}[NMS]{lang="EN-US"}[使用该团体名执行写操作。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_x997147325}

[\[Sysname\] acl basic name testacl]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-testacl\] rule permit source 1.1.1.2 0.0.0.0]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-testacl\] rule deny source any]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-testacl\] quit]{lang="EN-US"}

[\[Sysname\] snmp-agent sys-info version v2c]{lang="EN-US"}

[\[Sysname\] snmp-agent community write simple writeaccess acl name 2002]{lang="EN-US"}

[[将]{style="font-family:宋体"}[NMS]{lang="EN-US"}]{#struct_0_x1400_15709_891918907}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址配置为]{style="font-family:宋体"}[1.1.1.2]{lang="EN-US"}[，版本号指定为]{style="font-family:宋体"}[SNMPv2c]{lang="EN-US"}[，]{style="font-family:宋体"}[Write community]{lang="EN-US"}[选项填写为]{style="font-family:宋体"}[writeaccess]{lang="EN-US"}[，即可以对设备上缺省视图内的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[对象进行读写操作。]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_1773143070}[以明文方式创建团体名]{style="font-family:宋体"}[wr-sys-acc]{lang="EN-US"}[，使用该团体名访问设备时只能对]{style="font-family:宋体"}[system]{lang="EN-US"}[（]{style="font-family:宋体"}[OID]{lang="EN-US"}[为]{style="font-family:宋体"}[1.3.6.1.2.1.1]{lang="EN-US"}[）子树下的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[对象执行写操作。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_x1249400441}

[\[Sysname\] snmp-agent sys-info version v1 v2c]{lang="EN-US"}

[\[Sysname\] undo snmp-agent mib-view ViewDefault]{lang="EN-US"}

[\[Sysname\] snmp-agent mib-view included test system]{lang="EN-US"}

[\[Sysname\] snmp-agent community write simple wr-sys-acc mib-view test]{lang="EN-US"}

[[在]{style="font-family:宋体"}[NMS]{lang="EN-US"}]{#struct_0_x1400_15709_943012111}[上将版本号设置为]{style="font-family:宋体"}[SNMPv1]{lang="EN-US"}[或者]{style="font-family:宋体"}[SNMPv2c]{lang="EN-US"}[，并将]{style="font-family:宋体"}[Write community]{lang="EN-US"}[填写为]{style="font-family:宋体"}[wr-sys-acc]{lang="EN-US"}[，建立连接，就可以对设备上]{style="font-family:宋体"}[system]{lang="EN-US"}[视图内的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[对象进行读写操作。]{style="font-family:宋体"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x206979478}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **snmp-agent** **community**]{lang="EN-US"}]{#struct_0_x1400_15709_x336917707}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **mib-view**]{lang="EN-US"}]{#struct_0_x1400_15709_514164007}
:::

::: {#1252009757 .myid}
[]{#_Toc345227790}[]{#_Toc404796946}[]{#struct_0_x1400_15709_x1398556861}

**SNMP \-- SNMP配置命令 \-- snmp-agent community-map**

------------------------------------------------------------------------

[**[snmp-agent community-map]{lang="FR"}**]{#struct_0_x1400_15709_x842579794}[命令用来创建一个团体名到]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[上下文的映射。]{style="font-family:宋体"}

[**[undo snmp-agent community-map]{lang="FR"}**]{#struct_0_x1400_15709_394799787}[命令用来删除一个指定的映射。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1551037229}

[**[snmp-agent community-map]{lang="EN-US"}***[ community-name]{lang="EN-US"}***[ context ]{lang="EN-US"}***[context-name]{lang="EN-US"}*]{#struct_0_x1400_15709_x1399539901}

[**[undo snmp-agent community-map]{lang="EN-US"}***[ community-name]{lang="EN-US"}***[ context ]{lang="EN-US"}***[context-name]{lang="EN-US"}*]{#struct_0_x1400_15709_1400533106}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1227903316}

[[设备上没有团体名到]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_x479792691}[上下文的映射。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1399474365}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_1118338576}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x416503265}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_2061661359}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_167068331}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x146888352}

[*[community-name]{lang="EN-US"}*]{#struct_0_x1400_15709_x1751730523}[：团体名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[*[context-name]{lang="EN-US"}*]{#struct_0_x1400_15709_813629829}[：]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[上下文。为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_167133867}

[[用户配置成功后，使用]{style="font-family:宋体"}[SNMP v1/v2]{lang="EN-US"}]{#struct_0_x1400_15709_x467890094}[版本连接]{style="font-family:宋体"}[SNMP Agent]{lang="EN-US"}[时，]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[插件端所获取的上下文，是此时]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问]{style="font-family:宋体"}[Agent]{lang="EN-US"}[，使用的团体名映射的上下文。如团体名未配置上下文映射，则获取不到。]{style="font-family:宋体"}

[[系统中可配置的映射最多为]{style="font-family:宋体"}[10]{lang="EN-US"}]{#struct_0_x1400_15709_x109633073}[个。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1300923126}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_167199403}[配置一个团体名到]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[上下文的映射。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_x1720318388}

[\[Sysname\] snmp-agent community-map private context trillcontext]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1469860954}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display snmp-agent community]{lang="EN-US"}**]{#struct_0_x1400_15709_167264939}
:::

::: {#1611202802 .myid}
[]{#_Toc404796947}[]{#struct_0_x1400_15709_x607511718}

**SNMP \-- SNMP配置命令 \-- snmp-agent context**

------------------------------------------------------------------------

[**[snmp-agent context]{lang="EN-US"}**]{#struct_0_x1400_15709_x144611876}[命令用来创建一个新的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[上下文。]{style="font-family:宋体"}

[**[undo snmp-agent context]{lang="EN-US"}**]{#struct_0_x1400_15709_409241132}[命令用来删除指定的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[上下文。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x723333231}

[**[snmp-agent context ]{lang="EN-US"}***[context-name]{lang="EN-US"}*]{#struct_0_x1400_15709_x1210360092}

[**[undo snmp-agent context ]{lang="EN-US"}***[context-name]{lang="EN-US"}*]{#struct_0_x1400_15709_437159333}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1092981955}

[[设备上没有配置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_1643832048}[上下文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_167330475}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_901253016}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x935320924}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x1782521292}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x776603284}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1107134621}

[*[context-name]{lang="EN-US"}*]{#struct_0_x1400_15709_773865859}[：]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[上下文，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1139105985}

[[NMS]{lang="EN-US"}]{#struct_0_x1400_15709_167396011}[未配置上下文，或]{style="font-family:宋体"}[NMS]{lang="EN-US"}[与]{style="font-family:宋体"}[Agent]{lang="EN-US"}[配置为相同的上下文时，两者可以连接成功，否则返回超时。]{style="font-family:宋体"}

[[系统中可配置的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_x1793707042}[上下文最多为]{style="font-family:宋体"}[20]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1822049243}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_x87614018}[创建一个新的]{style="font-family:宋体"}[context]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_x751500812}

[\[Sysname\] snmp-agent context trillcontext]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1189350808}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[snmp-agent context]{lang="EN-US"}**]{#struct_0_x1400_15709_167461547}
:::

::: {#-248260569 .myid}
[]{#_Toc404796948}[]{#struct_0_x1400_15709_379294352}

**SNMP \-- SNMP配置命令 \-- snmp-agent group**

------------------------------------------------------------------------

[**[snmp-agent]{lang="EN-US"}**[ **group**]{lang="EN-US"}]{#struct_0_x1400_15709_613019984}[命令用来创建一个]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[组，并设置其访问权限。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **group**]{lang="EN-US"}]{#struct_0_x1400_15709_636757878}[命令用来删除一个指定的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_294490274}

[[SNMPv1]{lang="EN-US"}]{#struct_0_x1400_15709_1272466642}[和]{style="font-family:宋体"}[SNMPv2c]{lang="EN-US"}[版本下的命令格式是：]{style="font-family:宋体"}

[**[snmp-agent]{lang="EN-US"}**[ **group** { **v1** \| **v2c** } *group-name* \[ **read-view** *view-name* \] \[ **write-view** *view-name* \] \[ **notify-view** *view-name* \] \[ **acl** { *acl-number \|* **name** *acl-name* } \| **acl** **ipv6** { *ipv6-acl-number* \| **name** *ipv6-acl-name* } \] \*]{lang="EN-US"}]{#struct_0_x1400_15709_x1156779999}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **group** { **v1** \| **v2c** } *group-name*]{lang="EN-US"}]{#struct_0_x1400_15709_711203472}

[[SNMPv3]{lang="EN-US"}]{#struct_0_x1400_15709_802471433}[版本下的命令格式是：]{style="font-family:宋体"}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_x1400_15709_x540680458}[模式下]{style="font-family:宋体"}[:]{lang="EN-US"}

[**[snmp-agent]{lang="EN-US"}**[ **group** **v3** *group-name* \[ **authentication** \| **privacy** \] \[ **read-view** *read-view* \] \[ **write-view** *write-view* \] \[ **notify-view** *notify-view* \] \[ **acl** { *acl-number \|* **name** *acl-name* } \| **acl** **ipv6** { *ipv6-acl-number* \| **name** *ipv6-acl-name* } \] \*]{lang="EN-US"}]{#struct_0_x1400_15709_167527083}

[[FIPS]{lang="EN-US"}]{#struct_0_x1400_15709_x137395931}[模式下]{style="font-family:宋体"}[:]{lang="EN-US"}

[**[snmp-agent]{lang="EN-US"}**[ **group** **v3** *group-name* { **authentication** \| **privacy** } \[ **read-view** *read-view* \] \[ **write-view** *write-view* \] \[ **notify-view** *notify-view* \] \[ **acl** { *acl-number \|* **name** *acl-name* } \| **acl** **ipv6** { *ipv6-acl-number* \| **name** *ipv6-acl-name* } \] \*]{lang="EN-US"}]{#struct_0_x1400_15709_261200686}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **group** **v3** *group-name* \[ **authentication** \| **privacy** \]]{lang="EN-US"}]{#struct_0_x1400_15709_x714459833}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1035928284}

[[设备上没有配置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_x1764706092}[组。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_783726467}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_x923457300}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x649753411}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_166544043}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_269112138}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1015490761}

[**[v1]{lang="EN-US"}**]{#struct_0_x1400_15709_x274300507}[：]{style="font-family:宋体"}[SNMPv1]{lang="EN-US"}[版本。]{style="font-family:宋体"}

[**[v2c]{lang="EN-US"}**]{#struct_0_x1400_15709_x886963682}[：]{style="font-family:宋体"}[SNMPv2c]{lang="EN-US"}[版本。]{style="font-family:宋体"}

[**[v3]{lang="EN-US"}**]{#struct_0_x1400_15709_1714933948}[：]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[版本。]{style="font-family:宋体"}

[*[group-name]{lang="EN-US"}*]{#struct_0_x1400_15709_1858512432}[：]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[组名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[authentication]{lang="EN-US"}**]{#struct_0_x1400_15709_169753399}[：表示对报文进行认证但不加密。]{style="font-family:宋体"}

[**[privacy]{lang="EN-US"}**]{#struct_0_x1400_15709_x225772993}[：表示对报文进行认证和加密。]{style="font-family:宋体"}

[**[read-view]{lang="EN-US"}**[ *view-name*]{lang="EN-US"}]{#struct_0_x1400_15709_166609579}[：只读视图名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串。缺省值为]{style="font-family:宋体"}[ViewDefault]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[write-view]{lang="EN-US"}**[ *view-name*]{lang="EN-US"}]{#struct_0_x1400_15709_x1085367605}[：读写视图名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串。缺省情况下，未配置读写视图，即]{style="font-family:宋体"}[NMS]{lang="EN-US"}[不能对设备的所有]{style="font-family:宋体"}[MIB]{lang="EN-US"}[对象进行写操作。]{style="font-family:宋体"}

[**[notify-view]{lang="EN-US"}**[ *view-name*]{lang="EN-US"}]{#struct_0_x1400_15709_x1753127067}[：可以发告警信息的视图名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串。缺省情况下，未配置告警信息视图。]{style="font-family:宋体"}

[**[acl]{lang="EN-US"}**[ *acl-number*]{lang="EN-US"}]{#struct_0_x1400_15709_x2035407037}[：将组与基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[绑定，]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[表示访问列表号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。当未引用]{style="font-family:宋体"}[ACL]{lang="EN-US"}[或者引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在时，允许所有]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备；当]{style="font-family:宋体"}[ACL]{lang="EN-US"}[为空时，会禁止所有的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备；当引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[非空时，则只有]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中]{style="font-family:宋体"}[permit]{lang="EN-US"}[的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[才能访问设备，其它]{style="font-family:宋体"}[NMS]{lang="EN-US"}[不允许访问设备，以免非法]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}***[ acl-name]{lang="EN-US"}*]{#struct_0_x1400_15709_x1205211861}[：将团体名与基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[名绑定，]{style="font-family:宋体"}*[acl-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。当未引用]{style="font-family:宋体"}[ACL]{lang="EN-US"}[或者引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在时，允许所有]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备；当]{style="font-family:宋体"}[ACL]{lang="EN-US"}[为空时，会禁止所有的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备；当引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[非空时，则只有]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中]{style="font-family:宋体"}[permit]{lang="EN-US"}[的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[才能访问设备，其它]{style="font-family:宋体"}[NMS]{lang="EN-US"}[不允许访问设备，以免非法]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备。关于]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的详细描述和介绍请参见"]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{style="font-family:宋体"}[QoS]{lang="EN-US"}[配置指导"中的"]{style="font-family:宋体"}[ACL]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[acl]{lang="EN-US"}**[ **ipv6** *ipv6-acl-number*]{lang="EN-US"}]{#struct_0_x1400_15709_296108195}[：将组与基本]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[绑定，]{style="font-family:宋体"}*[ipv6-acl-number]{lang="EN-US"}*[表示访问列表号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。当未引用]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[或者引用的]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[不存在时，允许所有]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备；当]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[为空时，会禁止]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备；当引用的]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[非空时，则只有]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[中]{style="font-family:宋体"}[permit]{lang="EN-US"}[的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[才能访问设备，其它]{style="font-family:宋体"}[NMS]{lang="EN-US"}[不允许访问设备，以免非法]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}***[ ipv6-acl-name]{lang="EN-US"}*]{#struct_0_x1400_15709_x1205146325}[：将团体名与基本]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[名绑定，]{style="font-family:宋体"}*[acl-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。当未引用]{style="font-family:宋体"}[ACL]{lang="EN-US"}[或者引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在时，允许所有]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备；当]{style="font-family:宋体"}[ACL]{lang="EN-US"}[为空时，会禁止所有的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备；当引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[非空时，则只有]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中]{style="font-family:宋体"}[permit]{lang="EN-US"}[的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[才能访问设备，其它]{style="font-family:宋体"}[NMS]{lang="EN-US"}[不允许访问设备，以免非法]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1441416213}

[[FIPS]{lang="EN-US"}]{#struct_0_x1400_15709_x1637517926}[模式下，不支持]{style="font-family:宋体"}[SNMPv1]{lang="EN-US"}[和]{style="font-family:宋体"}[SNMPv2c]{lang="EN-US"}[版本下的本命令。]{style="font-family:宋体"}

[[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_x815001498}[组可以定义安全模式、视图权限等信息，配置在此组内的用户都具有这些公共属性。]{style="font-family:宋体"}

[[系统中可配置的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_167068332}[组最多为]{style="font-family:宋体"}[20]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[当不指定]{style="font-family:宋体"}**[authentication]{lang="EN-US"}**]{#struct_0_x1400_15709_x146888355}[和]{style="font-family:宋体"}**[privacy]{lang="EN-US"}**[时，表示不认证不加密。此时，使用和该组绑定的用户名建立]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[连接时，均不认证不加密。即便用户配置了认证密码]{style="font-family:宋体"}[/]{lang="EN-US"}[加密密码，认证密码]{style="font-family:宋体"}[/]{lang="EN-US"}[加密密码也不生效。]{style="font-family:宋体"}

[[当指定]{style="font-family:宋体"}**[authentication]{lang="EN-US"}**]{#struct_0_x1400_15709_x1751271771}[时，表示认证不加密。此时，使用和该组绑定的用户名建立]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[连接时，均认证不加密。即便用户配置了加密密码，加密密码也不生效。]{style="font-family:宋体"}

[[当指定]{style="font-family:宋体"}**[privacy]{lang="EN-US"}**]{#struct_0_x1400_15709_135821125}[时，表示认证加密。此时，使用和该组绑定的用户名建立]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[连接时，均认证加密。该组内的用户必须配置认证密码和加密密码，否则，不能建立]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1873760069}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_x1367660674}[在运行]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[版本的设备上创建一个]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[组]{style="font-family:宋体"}[group1]{lang="EN-US"}[，采用不认证、不加密方式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_395462718}

[\[Sysname\] snmp-agent group v3 group1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1438903436}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **snmp-agent** **group**]{lang="EN-US"}]{#struct_0_x1400_15709_167133868}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **mib-view**]{lang="EN-US"}]{#struct_0_x1400_15709_x467890103}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **usm-user**]{lang="EN-US"}]{#struct_0_x1400_15709_1846616520}
:::

::: {#937991101 .myid}
[]{#_Toc404796949}[]{#struct_0_x1400_15709_x190019600}

**SNMP \-- SNMP配置命令 \-- snmp-agent local-engineid**

------------------------------------------------------------------------

[**[snmp-agent]{lang="EN-US"}**[ **local-engineid**]{lang="EN-US"}]{#struct_0_x1400_15709_x1135539250}[命令用来设置本地]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体的引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **local-engineid**]{lang="EN-US"}]{#struct_0_x1400_15709_217363932}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x758575277}

[**[snmp-agent]{lang="EN-US"}**[ **local-engineid** *engineid*]{lang="EN-US"}]{#struct_0_x1400_15709_x202003609}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **local-engineid**]{lang="EN-US"}]{#struct_0_x1400_15709_762739683}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1400_15709_167199404}

[[设备引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1400_15709_x1720318385}[为公司的"企业号＋设备信息"。设备信息由各个产品决定，可以是]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址或者自定义的十六进制数字串。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1422806787}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_x52409942}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1255269912}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x1748883294}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_1229177234}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1137721563}

[*[engineid]{lang="EN-US"}*]{#struct_0_x1400_15709_167264940}[：引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[，必须为偶数个十六进制数，偶数的取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[。全]{style="font-family:宋体"}[0]{lang="EN-US"}[和全]{style="font-family:宋体"}[F]{lang="EN-US"}[均被认为是无效参数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_201792337}

[[引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1400_15709_20683139}[有两个作用：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x1400_15709_x1223646852}[NMS]{lang="EN-US"}[管理的所有设备中，每一台设备都需要用一个唯一的引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[来标识]{style="font-family:宋体"}[Agent]{lang="EN-US"}[，缺省情况下每个设备有一个缺省的引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[，网络管理员需要确保管理域内不能有重复的引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SNMPv3]{lang="EN-US"}]{#struct_0_x1400_15709_x1195334706}[版本的用户名、密文密码等都和引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[相关联，如果更改了引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[，则原引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[下配置的用户名、密码失效。]{style="font-family:宋体"}

[[通常情况下，使用设备的缺省引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1400_15709_x520511721}[即可，用户也可以根据网络整体规划给设备配置方便记忆的引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[，比如]{style="font-family:宋体"}[A]{lang="EN-US"}[栋一楼的一号设备可以将它的引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[设置为]{style="font-family:宋体"}[000Af0010001]{lang="EN-US"}[，二号设备可以配置为]{style="font-family:宋体"}[000Af0010002]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1703905835}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_x1698925274}[配置本地设备的引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[123456789A]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_167330476}

[\[Sysname\] snmp-agent local-engineid 123456789A]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_901253015}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **snmp-agent** **local-engineid**]{lang="EN-US"}]{#struct_0_x1400_15709_x935320921}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **usm-user**]{lang="EN-US"}]{#struct_0_x1400_15709_x1782193612}
:::

::: {#-372955629 .myid}
[]{#_Toc404796950}[]{#struct_0_x1400_15709_x393033633}

**SNMP \-- SNMP配置命令 \-- snmp-agent log**

------------------------------------------------------------------------

[**[snmp-agent]{lang="EN-US"}**[ **log**]{lang="EN-US"}]{#struct_0_x1400_15709_492029809}[命令用来开启]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[日志功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **log**]{lang="EN-US"}]{#struct_0_x1400_15709_x167590928}[命令用来关闭]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[日志功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x847306461}

[**[snmp-agent]{lang="EN-US"}**[ **log** { **all** \| **get-operation** \| **set-operation** }]{lang="EN-US"}]{#struct_0_x1400_15709_1014519121}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **log** { **all** \| **get-operation** \| **set-operation** }]{lang="EN-US"}]{#struct_0_x1400_15709_167396012}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1793707039}

[[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_x612130126}[日志功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1355558373}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_x2083420407}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1690895067}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x1831291525}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_1312907335}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1829009560}

[**[all]{lang="EN-US"}**]{#struct_0_x1400_15709_167461548}[：表示]{style="font-family:宋体"}[SNMP Get]{lang="EN-US"}[和]{style="font-family:宋体"}[Set]{lang="EN-US"}[操作的日志开关。]{style="font-family:宋体"}

[**[get-operation]{lang="EN-US"}**]{#struct_0_x1400_15709_379294365}[：表示]{style="font-family:宋体"}[SNMP Get]{lang="EN-US"}[操作的日志开关。]{style="font-family:宋体"}

[**[set-operation]{lang="EN-US"}**]{#struct_0_x1400_15709_x1343295155}[：表示]{style="font-family:宋体"}[SNMP Set]{lang="EN-US"}[操作的日志开关。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x96219878}

[[当打开]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_779385825}[指定的日志开关，]{style="font-family:宋体"}[NMS]{lang="EN-US"}[对]{style="font-family:宋体"}[Agent]{lang="EN-US"}[执行指定的操作时，]{style="font-family:宋体"}[Agent]{lang="EN-US"}[会记录与该操作相关的信息并保存到设备的信息中心。通过设置信息中心的参数，最终决定]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[日志的输出规则（即是否允许输出以及输出方向）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1320969381}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_x1149560410}[打开]{style="font-family:宋体"}[SNMP Get]{lang="EN-US"}[操作的日志开关。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_x103696507}

[\[Sysname\] snmp-agent log get-operation]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_167527084}[打开]{style="font-family:宋体"}[SNMP Set]{lang="EN-US"}[操作的日志开关。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_x714459828}

[\[Sysname\] snmp-agent log set-operation]{lang="EN-US"}
:::

::: {#-986127289 .myid}
[]{#_Toc404796951}[]{#struct_0_x1400_15709_1035600603}

**SNMP \-- SNMP配置命令 \-- snmp-agent mib-view**

------------------------------------------------------------------------

[**[snmp-agent]{lang="EN-US"}**[ **mib-view**]{lang="EN-US"}]{#struct_0_x1400_15709_x1352395559}[命令用来创建或者更新]{style="font-family:宋体"}[MIB]{lang="EN-US"}[视图的信息，以指定]{style="font-family:宋体"}[NMS]{lang="EN-US"}[可以访问的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[对象。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **mib-view**]{lang="EN-US"}]{#struct_0_x1400_15709_1121652360}[命令用来删除指定视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1062069042}

[**[snmp-agent]{lang="EN-US"}**[ **mib-view** { **excluded** \| **included** } *view-name* *oid-tree* \[ **mask** *mask-value* \]]{lang="EN-US"}]{#struct_0_x1400_15709_611322808}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **mib-view** *view-name*]{lang="EN-US"}]{#struct_0_x1400_15709_1957923902}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1400_15709_166544044}

[[设备上已创建了四个视图，视图名均为]{style="font-family:宋体"}[ViewDefault]{lang="EN-US"}]{#struct_0_x1400_15709_269112131}[：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[视图一包含]{style="font-family:宋体"}]{#struct_0_x1400_15709_x1015490768}[MIB]{lang="EN-US"}[子树]{style="font-family:宋体"}[iso]{lang="EN-US"}[；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[视图二不包含子树]{lang="EN-US" style="font-family:宋体"}[snmpUsmMIB]{lang="EN-US"}]{#struct_0_x1400_15709_935553074}[；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[视图三不包含子树]{style="font-family:宋体"}]{#struct_0_x1400_15709_x40353134}[snmpVacmMIB]{lang="EN-US"}[；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[视图四不包含子树]{lang="EN-US" style="font-family:宋体"}[snmpModules.18]{lang="EN-US"}]{#struct_0_x1400_15709_223438306}[。]{lang="EN-US" style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x717521776}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_x215917081}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_367282085}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_166609580}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x1805411630}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x849871271}

[**[excluded]{lang="EN-US"}**]{#struct_0_x1400_15709_382568042}[：表示当前视图不包括该]{style="font-family:宋体"}[MIB]{lang="EN-US"}[子树的任何节点（即禁止访问]{style="font-family:宋体"}[MIB]{lang="EN-US"}[子树的所有节点）。]{style="font-family:宋体"}

[**[included]{lang="EN-US"}**]{#struct_0_x1400_15709_1772366754}[：表示当前视图包括该]{style="font-family:宋体"}[MIB]{lang="EN-US"}[子树的所有节点（即允许访问]{style="font-family:宋体"}[MIB]{lang="EN-US"}[子树的所有节点）。]{style="font-family:宋体"}

[*[view-name]{lang="EN-US"}*]{#struct_0_x1400_15709_671543502}[：视图名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[*[oid-tree]{lang="EN-US"}*]{#struct_0_x1400_15709_1027163274}[：]{style="font-family:宋体"}[MIB]{lang="EN-US"}[子树，用子树根节点的]{style="font-family:宋体"}[OID]{lang="EN-US"}[（如"]{style="font-family:宋体"}[1.3.6.1.2.1.1]{lang="EN-US"}["）或名称（如"]{style="font-family:宋体"}[system]{lang="EN-US"}["）表示。]{style="font-family:宋体"}[OID]{lang="EN-US"}[是由一系列的整数组成，标明节点在]{style="font-family:宋体"}[MIB]{lang="EN-US"}[树中的位置，它能唯一地标识一个]{style="font-family:宋体"}[MIB]{lang="EN-US"}[库中的对象。]{style="font-family:宋体"}

[**[mask]{lang="EN-US"}**[ *mask-value*]{lang="EN-US"}]{#struct_0_x1400_15709_x39284331}[：对象子树的掩码，十六进制数，长度为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[中的偶数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_2062797015}

[[MIB]{lang="EN-US"}]{#struct_0_x1400_15709_167068329}[视图是]{style="font-family:宋体"}[MIB]{lang="EN-US"}[的子集，由视图名和]{style="font-family:宋体"}[MIB]{lang="EN-US"}[子树来唯一确定一个]{style="font-family:宋体"}[MIB]{lang="EN-US"}[视图。视图名相同但包含的子树不同，则认为是不同的视图。除缺省视图外，用户最多可以创建]{style="font-family:宋体"}[16]{lang="EN-US"}[个]{style="font-family:宋体"}[MIB]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[缺省视图可以通过]{style="font-family:宋体"}**[display]{lang="EN-US"}**[ **snmp-agent** **mib-view**]{lang="EN-US"}]{#struct_0_x1400_15709_1809426792}[命令来查看。如果使用缺省视图限制]{style="font-family:
宋体"}[NMS]{lang="EN-US"}[的访问权限时，除了]{style="font-family:
宋体"}[snmpUsmMIB]{lang="EN-US"}[、]{style="font-family:
宋体"}[snmpVacmMIB]{lang="EN-US"}[、]{style="font-family:宋体"}[snmpModules.18]{lang="EN-US"}[子树下的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[对象，]{style="font-family:宋体"}[NMS]{lang="EN-US"}[可以访问]{style="font-family:宋体"}[iso]{lang="EN-US"}[子树下其它所有]{style="font-family:宋体"}[MIB]{lang="EN-US"}[对象。缺省视图可以通过]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **snmp-agent** **mib-view**]{lang="EN-US"}[命令删除，但是删除以后，可能导致不能对]{style="font-family:
宋体"}[Agent]{lang="EN-US"}[的所有]{style="font-family:宋体"}[MIB]{lang="EN-US"}[节点执行读写操作，除非另外手工配置视图。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_573050019}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_x2121268110}[创建并更新]{style="font-family:宋体"}[MIB]{lang="EN-US"}[视图信息，名字为]{style="font-family:宋体"}[mibtest]{lang="EN-US"}[，先创建一个包含]{style="font-family:宋体"}[mib-2]{lang="EN-US"}[子树（]{style="font-family:宋体"}[OID]{lang="EN-US"}[为"]{style="font-family:宋体"}[1.3.6.1]{lang="EN-US"}["）所有对象的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[视图，再更新为不包含"]{style="font-family:宋体"}[system]{lang="EN-US"}["子树]{style="font-family:宋体"}[(OID]{lang="EN-US"}[为"]{style="font-family:宋体"}[1.3.6.1.2.1.1]{lang="EN-US"}["]{style="font-family:宋体"}[)]{lang="EN-US"}[所有对象的]{style="font-family:
宋体"}[MIB]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_806991522}

[\[Sysname\] snmp-agent sys-info version v1]{lang="EN-US"}

[\[Sysname\] snmp-agent mib-view included mibtest 1.3.6.1]{lang="EN-US"}

[\[Sysname\] snmp-agent mib-view excluded mibtest system]{lang="EN-US"}

[\[Sysname\] snmp-agent community read public mib-view mibtest]{lang="EN-US"}

[[以上配置成功后，当]{style="font-family:宋体"}[NMS]{lang="EN-US"}]{#struct_0_x1400_15709_1933882757}[使用]{style="font-family:宋体"}[SNMPv1]{lang="EN-US"}[版本，]{style="font-family:宋体"}[public]{lang="EN-US"}[团体名访问设备时，不能查询]{style="font-family:宋体"}[system]{lang="EN-US"}[子树的所有对象（比如]{style="font-family:宋体"}[sysDescr]{lang="EN-US"}[和]{style="font-family:宋体"}[sysObjectID]{lang="EN-US"}[等节点），可以查询]{style="font-family:宋体"}[mib-2]{lang="EN-US"}[子树下的其它所有对象。]{style="font-family:宋体"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1037630796}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **snmp-agent** **mib-view**]{lang="EN-US"}]{#struct_0_x1400_15709_x1428351776}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **group**]{lang="EN-US"}]{#struct_0_x1400_15709_167133865}
:::

::: {#951936228 .myid}
[]{#_Toc404796952}[]{#struct_0_x1400_15709_x467890092}

**SNMP \-- SNMP配置命令 \-- snmp-agent packet max-size**

------------------------------------------------------------------------

[**[snmp-agent]{lang="EN-US"}**[ **packet** **max-size**]{lang="EN-US"}]{#struct_0_x1400_15709_x109764145}[命令用来设置]{style="font-family:宋体"}[Agent]{lang="EN-US"}[能接收或发送的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[报文的最大长度。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **packet** **max-size**]{lang="EN-US"}]{#struct_0_x1400_15709_1413137389}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1526954393}

[**[snmp-agent]{lang="EN-US"}**[ **packet** **max-size** *byte-count*]{lang="EN-US"}]{#struct_0_x1400_15709_x121937837}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **packet** **max-size**]{lang="EN-US"}]{#struct_0_x1400_15709_x218788575}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x364677225}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1400_15709_328749505}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_167199401}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_x1720318390}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1826025778}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_61199892}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_544285895}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1400_15709_45405757}

[*[byte-count]{lang="EN-US"}*]{#struct_0_x1400_15709_67687848}[：]{style="font-family:宋体"}[Agent]{lang="EN-US"}[能接收]{style="font-family:宋体"}[/]{lang="EN-US"}[发送的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[报文的最大长度，取值范围为]{style="font-family:宋体"}[484]{lang="EN-US"}[～]{style="font-family:宋体"}[17940]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x852290161}

[[设置报文的最大长度是为了防止网络中存在不支持分片的主机，而导致超长数据被丢弃。通常情况下，使用缺省值即可。]{style="font-family:宋体"}]{#struct_0_x1400_15709_167264937}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x607511732}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_x145267234}[设置]{style="font-family:宋体"}[Agent]{lang="EN-US"}[能接收]{style="font-family:宋体"}[/]{lang="EN-US"}[发送的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[报文的最大长度为]{style="font-family:宋体"}[1024]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_x381564510}

[\[Sysname\] snmp-agent packet max-size 1024]{lang="EN-US"}
:::

::: {#-1400347777 .myid}
[]{#_Toc404796953}[]{#struct_0_x1400_15709_1666848568}[]{#_Toc335813544}[]{#_Toc320867961}

**SNMP \-- SNMP配置命令 \-- snmp-agent port**

------------------------------------------------------------------------

[**[snmp-agent port]{lang="EN-US"}**]{#struct_0_x1400_15709_1737928177}[命令用来指定设备上接收]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[报文的本地端口号。]{style="font-family:宋体"}

[**[undo snmp-agent port]{lang="EN-US"}**]{#struct_0_x1400_15709_x561006384}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_428137465}

[**[snmp-agent port ]{lang="EN-US"}***[port-num]{lang="EN-US"}*]{#struct_0_x1400_15709_293024951}

[**[undo snmp-agent port]{lang="EN-US"}**]{#struct_0_x1400_15709_167330473}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1400_15709_901253010}

[[使用]{style="font-family:宋体"}[161]{lang="EN-US"}]{#struct_0_x1400_15709_x935320918}[作为本地端口号接收]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1781734861}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_1321241829}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_811444411}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_1441788087}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x279386043}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1400_15709_167396009}

[*[port-num]{lang="EN-US"}*]{#struct_0_x1400_15709_544945126}[：设备上接收]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[报文的本地端口号。取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[161]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x386226185}

[[用户配置成功后，使用新端口重新连接设备后，可以进行]{style="font-family:宋体"}[Get/Set]{lang="EN-US"}]{#struct_0_x1400_15709_1661545846}[等操作，此时使用]{style="font-family:宋体"}[display current-configurantion]{lang="EN-US"}[命令查看]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[相关配置，此项配置可以显示。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x528723963}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_x747348147}[指定新的端口号。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_2143598048}

[\[Sysname\] snmp-agent port 5555]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_65002580}[恢复默认端口号。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_167461545}

[\[Sysname\] undo snmp-agent port]{lang="EN-US"}
:::

::: {#525610896 .myid}
[]{#_Toc404796954}[]{#struct_0_x1400_15709_379294354}

**SNMP \-- SNMP配置命令 \-- snmp-agent remote**

------------------------------------------------------------------------

[**[snmp-agent]{lang="EN-US"}**[ **remote**]{lang="EN-US"}]{#struct_0_x1400_15709_613019982}[命令用来配置远端]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体的引擎。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **remote**]{lang="EN-US"}]{#struct_0_x1400_15709_636757872}[命令用来取消已配置的远端]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体的引擎。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_294490280}

[**[snmp-agent]{lang="EN-US"}**[ **remote** { *ip-address* \| **ipv6** *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \] **engineid** *engineid*]{lang="EN-US"}]{#struct_0_x1400_15709_1317096662}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **remote** *ip-address*]{lang="EN-US"}]{#struct_0_x1400_15709_1987440225}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x802261264}

[[设备上没有配置远端]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_167527081}[实体的引擎。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x714459831}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_1036059356}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1617577307}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_1936423196}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x1953003207}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x661427755}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1400_15709_x1831317115}[：远端]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**[ *ipv6-address*]{lang="EN-US"}]{#struct_0_x1400_15709_x90726365}[：远端]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x1400_15709_166544041}[：指定远端]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示远端]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体位于公网中。]{style="font-family:宋体"}

[*[engineid]{lang="EN-US"}*]{#struct_0_x1400_15709_269112136}[：引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[，必须为偶数个十六进制数，偶数的取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[。全]{style="font-family:宋体"}[0]{lang="EN-US"}[和全]{style="font-family:宋体"}[F]{lang="EN-US"}[均被认为是无效参数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1015490775}

[[当设备需要向]{style="font-family:宋体"}[NMS]{lang="EN-US"}]{#struct_0_x1400_15709_1695133497}[发送]{style="font-family:宋体"}[SNMPv3 Inform]{lang="EN-US"}[报文时，必须配置该命令，并将]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[配置为]{style="font-family:宋体"}[NMS]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，]{style="font-family:宋体"}*[engineid]{lang="EN-US"}*[配置为]{style="font-family:宋体"}[NMS]{lang="EN-US"}[的引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[。因为协议要求]{style="font-family:宋体"}[SNMPv3 Inform]{lang="EN-US"}[报文中必须携带一个权威引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}[NMS]{lang="EN-US"}[收到该报文后，会用自己的引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[和这个权威引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[比较，如果相同，才能接收。]{style="font-family:宋体"}

[[用户最多可以配置]{style="font-family:宋体"}[20]{lang="EN-US"}]{#struct_0_x1400_15709_1079835315}[个远端]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x268660273}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_x520609401}[配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体的引擎为]{style="font-family:宋体"}[123456789A]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_997464844}

[\[Sysname\] snmp-agent remote 10.1.1.1 engineid 123456789A]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1135717777}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **snmp-agent** **remote**]{lang="EN-US"}]{#struct_0_x1400_15709_166609577}
:::

::: {#1887005227 .myid}
[]{#_Toc404796955}[]{#struct_0_x1400_15709_x1085367591}

**SNMP \-- SNMP配置命令 \-- snmp-agent { inform \| trap } source**

------------------------------------------------------------------------

[**[snmp-agent]{lang="EN-US"}**[ { **inform** \| **trap** } **source**]{lang="EN-US"}]{#struct_0_x1400_15709_571881940}[命令用来指定告警信息中的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp-agent** { **inform** \| **trap** } **source**]{lang="EN-US"}]{#struct_0_x1400_15709_x1620696331}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_220998992}

[**[snmp-agent]{lang="EN-US"}**[ { **inform** \| **trap** } **source** *interface-type* { *interface-number* \| *interface-number*.*subnumber* }]{lang="EN-US"}]{#struct_0_x1400_15709_x542363759}

[**[undo]{lang="EN-US"}**[ **snmp-agent** { **inform** \| **trap** } **source**]{lang="EN-US"}]{#struct_0_x1400_15709_x2097636244}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x280630511}

[[由]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_167068330}[选择路由出接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址作为告警信息源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x146888353}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_x1751664987}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x2129025538}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_1054227570}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_1906111767}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1829463960}

[**[inform]{lang="EN-US"}**]{#struct_0_x1400_15709_1837510047}**[：]{style="font-family:宋体"}**[用来指定]{style="font-family:宋体"}[Inform]{lang="EN-US"}[报文中的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[trap]{lang="EN-US"}**]{#struct_0_x1400_15709_x1729686412}**[：]{style="font-family:宋体"}**[用来指定]{style="font-family:宋体"}[Trap]{lang="EN-US"}[报文中的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[interface-type]{lang="EN-US"}*[ { *interface-number* \| *interface-number*.*subnumber* }]{lang="EN-US"}]{#struct_0_x1400_15709_167133866}[：指定三层接口类型与接口编号。其中]{style="font-family:
宋体"}*[interface-number]{lang="EN-US"}*[为主接口编号；]{style="font-family:宋体"}*[subnumber]{lang="EN-US"}*[为子接口编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x467890093}

[[执行该命令后，系统会使用指定接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1400_15709_x109698609}[地址作为发送出去的告警信息的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。这样，在]{style="font-family:宋体"}[NMS]{lang="EN-US"}[上就可以使用该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址唯一标志]{style="font-family:宋体"}[Agent]{lang="EN-US"}[。即便]{style="font-family:宋体"}[Agent]{lang="EN-US"}[使用不同的出接口发送告警信息，]{style="font-family:宋体"}[NMS]{lang="EN-US"}[都可以使用该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址来过滤]{style="font-family:宋体"}[Agent]{lang="EN-US"}[发送的所有告警信息。]{style="font-family:宋体"}

[[在将某个接口设置为获取告警信息的源地址接口之前需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1400_15709_1380882044}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置的接口已存在，并且配置了合法的]{style="font-family:宋体"}]{#struct_0_x1400_15709_476417336}[IP]{lang="EN-US"}[地址，则该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址将作为告警信息的源地址；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置的接口不存在，则该命令会配置失败；]{style="font-family:宋体"}]{#struct_0_x1400_15709_39885878}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置的接口已存在，但没有配置合法的]{style="font-family:宋体"}]{#struct_0_x1400_15709_x151796407}[IP]{lang="EN-US"}[地址，则该命令不生效，在接口配置了合法]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址后，该命令会自动生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_786642698}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_x92080900}[配置]{style="font-family:宋体"}[Trap]{lang="EN-US"}[报文的源地址为以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的接口主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_167199402}

[\[Sysname\] snmp-agent trap source gigabitethernet 1/0/1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_x1720318387}[配置]{style="font-family:宋体"}[Inform]{lang="EN-US"}[报文的源地址为以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[上的接口主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_260007373}

[\[Sysname\] snmp-agent inform source gigabitethernet 1/0/2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1796055754}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **trap** **enable**]{lang="EN-US"}]{#struct_0_x1400_15709_237545227}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **target-host**]{lang="EN-US"}]{#struct_0_x1400_15709_x1867902401}
:::

::: {#-1366745620 .myid}
[]{#_Toc404796956}[]{#struct_0_x1400_15709_x399440240}

**SNMP \-- SNMP配置命令 \-- snmp-agent sys-info contact**

------------------------------------------------------------------------

[**[snmp-agent]{lang="EN-US"}**[ **sys-info contact**]{lang="EN-US"}]{#struct_0_x1400_15709_167264938}[命令用来配置设备的维护联系信息。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **sys-info** **contact**]{lang="EN-US"}]{#struct_0_x1400_15709_x607511719}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x144546340}

[**[snmp-agent]{lang="EN-US"}**[ **sys-info** **contact** *sys-contact*]{lang="EN-US"}]{#struct_0_x1400_15709_1969902993}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **sys-info** **contact**]{lang="EN-US"}]{#struct_0_x1400_15709_1432108004}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1400_15709_814463444}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1400_15709_1948748469}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_161540179}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_167330474}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_901253017}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x935320923}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x1782062540}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1400_15709_217824427}

[*[sys-contact]{lang="EN-US"}*]{#struct_0_x1400_15709_x1260324181}[：描述系统维护联系信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x24992368}

[[如果设备发生故障，设备维护人员可以利用系统维护联系信息，及时与设备生产厂商取得联系。]{style="font-family:宋体"}]{#struct_0_x1400_15709_2117508384}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x228418153}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_167396010}[配置设备的维护联系信息为]{style="font-family:宋体"}[Dial System Operator \# 27345]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_x1793707041}

[\[Sysname\] snmp-agent sys-info contact Dial System Operator \# 27345]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x255965302}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **snmp-agent** **sys-info**]{lang="EN-US"}]{#struct_0_x1400_15709_x1349604377}
:::

::: {#1213853256 .myid}
[]{#_Toc404796957}[]{#struct_0_x1400_15709_849798789}

**SNMP \-- SNMP配置命令 \-- snmp-agent sys-info location**

------------------------------------------------------------------------

[**[snmp-agent]{lang="EN-US"}**[ **sys-info location**]{lang="EN-US"}]{#struct_0_x1400_15709_262465519}[命令用来配置设备的物理位置信息。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **sys-info** **location**]{lang="EN-US"}]{#struct_0_x1400_15709_2029177286}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1004293525}

[**[snmp-agent]{lang="EN-US"}**[ **sys-info** **location** *sys-location*]{lang="EN-US"}]{#struct_0_x1400_15709_1740025688}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **sys-info** **location**]{lang="EN-US"}]{#struct_0_x1400_15709_167461546}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1400_15709_379294351}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1400_15709_613019985}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_636757877}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_294490275}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1272466641}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x1156714463}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x1554463175}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1400_15709_167527082}

[*[sys-location]{lang="EN-US"}*]{#struct_0_x1400_15709_x714459834}[：设备的物理位置信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1035862748}

[[为便于识别和管理设备，请使用该命令将设备所处的物理位置记录在设备中。]{style="font-family:宋体"}]{#struct_0_x1400_15709_1754463565}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x716388679}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_x1851033812}[配置设备的物理位置信息为]{style="font-family:宋体"}[Room524-row1-3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_x365999162}

[\[Sysname\] snmp-agent sys-info location Room524-row1-3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x413077146}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **snmp-agent** **sys-info**]{lang="EN-US"}]{#struct_0_x1400_15709_1917470288}
:::

::: {#984376935 .myid}
[]{#_Toc404796958}[]{#struct_0_x1400_15709_166544042}

**SNMP \-- SNMP配置命令 \-- snmp-agent sys-info version**

------------------------------------------------------------------------

[**[snmp-agent]{lang="EN-US"}**[ **sys-info version**]{lang="EN-US"}]{#struct_0_x1400_15709_269112137}[命令用来设置系统启用的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[版本号。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **sys-info** **version**]{lang="EN-US"}]{#struct_0_x1400_15709_x1015490774}[命令用来禁止使用指定版本的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1033749858}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_x1400_15709_241375566}[模式下：]{style="font-family:宋体"}

[**[snmp-agent]{lang="EN-US"}**[ **sys-info** **version** { **all** \| { **v1** \| **v2c** \| **v3** } \* }]{lang="EN-US"}]{#struct_0_x1400_15709_1511544412}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **sys-info** **version** { **all** \| { **v1** \| **v2c** \| **v3** } \* }]{lang="EN-US"}]{#struct_0_x1400_15709_x1678256404}

[[FIPS]{lang="EN-US"}]{#struct_0_x1400_15709_567790979}[模式下：]{style="font-family:宋体"}

[**[snmp-agent]{lang="EN-US"}**[ **sys-info** **version** **v3**]{lang="EN-US"}]{#struct_0_x1400_15709_x1208284801}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **sys-info** **version** **v3**]{lang="EN-US"}]{#struct_0_x1400_15709_166609578}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1085367606}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1400_15709_x187043126}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1690251411}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_129628591}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_63944383}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_740074287}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_777396324}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1400_15709_167068327}

[**[all]{lang="EN-US"}**]{#struct_0_x1400_15709_1809426778}[：启用]{style="font-family:宋体"}[SNMPv1]{lang="EN-US"}[、]{style="font-family:宋体"}[SNMPv2c]{lang="EN-US"}[和]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[版本。]{style="font-family:宋体"}

[**[v1]{lang="EN-US"}**]{#struct_0_x1400_15709_573443225}[：启用]{style="font-family:宋体"}[SNMPv1]{lang="EN-US"}[版本。]{style="font-family:宋体"}

[**[v2c]{lang="EN-US"}**]{#struct_0_x1400_15709_1144581589}[：启用]{style="font-family:宋体"}[SNMPv2c]{lang="EN-US"}[版本。]{style="font-family:宋体"}

[**[v3]{lang="EN-US"}**]{#struct_0_x1400_15709_736212950}[：启用]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[版本。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1832973846}

[[FIPS]{lang="EN-US"}]{#struct_0_x1400_15709_1801401860}[模式下，不支持设置]{style="font-family:宋体"}[SNMPv1]{lang="EN-US"}[和]{style="font-family:宋体"}[SNMPv2c]{lang="EN-US"}[版本。]{style="font-family:宋体"}

[[启用指定的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_1933547519}[版本后，设备才能收发该版本的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[报文。只有]{style="font-family:宋体"}[NMS]{lang="EN-US"}[和]{style="font-family:宋体"}[Agent]{lang="EN-US"}[使用的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[版本相同，]{style="font-family:宋体"}[NMS]{lang="EN-US"}[才能和]{style="font-family:宋体"}[Agent]{lang="EN-US"}[建立连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_635942568}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_167133863}[启用]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[版本。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_x467890098}

[\[Sysname\] snmp-agent sys-info version v3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x109370929}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **snmp-agent** **sys-info**]{lang="EN-US"}]{#struct_0_x1400_15709_610660611}
:::

::: {#1084945205 .myid}
[]{#_Toc404796959}[]{#struct_0_x1400_15709_x748556682}[]{#_Toc309201717}

**SNMP \-- SNMP配置命令 \-- snmp-agent target-host**

------------------------------------------------------------------------

[**[snmp-agent]{lang="EN-US"}**[ **target-host**]{lang="EN-US"}]{#struct_0_x1400_15709_x700164716}[命令用来设置接收]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[告警信息的目的主机（能够解析]{style="font-family:宋体"}[Trap]{lang="EN-US"}[和]{style="font-family:宋体"}[Inform]{lang="EN-US"}[报文的设备，通常为]{style="font-family:宋体"}[NMS]{lang="EN-US"}[）的属性。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **target-host**]{lang="EN-US"}]{#struct_0_x1400_15709_x1980841143}[命令用来取消当前设置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_792673506}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_x1400_15709_167199399}[模式下：]{style="font-family:宋体"}

[**[snmp-agent]{lang="EN-US"}**[ **target-host** **inform** **address** **udp-domain** { *ip-address* \| **ipv6** *ipv6-address* } \[ **udp-port** *port-number* \] \[ **vpn-instance** *vpn-instance-name* \] **params** **securityname** *security-string* { **v2c** \| **v3** \[ **authentication** \| **privacy** \] }]{lang="EN-US"}]{#struct_0_x1400_15709_x890066815}

[**[snmp-agent]{lang="EN-US"}**[ **target-host** **trap** **address** **udp-domain** { *ip-address* \| **ipv6** *ipv6-address* } \[ **udp-port** *port-number* \] \[ **vpn-instance** *vpn-instance-name* \] **params** **securityname** *security-string* \[ **v1** \| **v2c** \| **v3** \[ **authentication** \| **privacy** \] \]]{lang="EN-US"}]{#struct_0_x1400_15709_x864547210}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **target-host** { **trap** \| **inform** } **address** **udp-domain** { *ip-address* \| **ipv6** *ipv6-address* } **params** **securityname** *security-string* \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_x1400_15709_1172001123}

[[FIPS]{lang="EN-US"}]{#struct_0_x1400_15709_x420757394}[模式下：]{style="font-family:宋体"}

[**[snmp-agent]{lang="EN-US"}**[ **target-host** **inform** **address** **udp-domain** { *ip-address* \| **ipv6** *ipv6-address* } \[ **udp-port** *port-number* \] \[ **vpn-instance** *vpn-instance-name* \] **params** **securityname** *security-string* **v3** { **authentication** \| **privacy** }]{lang="EN-US"}]{#struct_0_x1400_15709_x1879470871}

[**[snmp-agent]{lang="EN-US"}**[ **target-host** **trap** **address** **udp-domain** { *ip-address* \| **ipv6** *ipv6-address* } \[ **udp-port** *port-number* \] \[ **vpn-instance** *vpn-instance-name* \] **params** **securityname** *security-string* **v3** { **authentication** \| **privacy** }]{lang="EN-US"}]{#struct_0_x1400_15709_x1580631175}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **target-host** { **trap** \| **inform** } **address** **udp-domain** { *ip-address* \| **ipv6** *ipv6-address* } **params** **securityname** *security-string* \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_x1400_15709_x375157891}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1400_15709_110971132}

[[设备上没有设置告警主机。]{style="font-family:宋体"}]{#struct_0_x1400_15709_167264935}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x607511730}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_x145136162}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1534569181}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x932837038}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_1439794503}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1223049806}

[**[inform]{lang="EN-US"}**]{#struct_0_x1400_15709_1628261715}[：配置接收]{style="font-family:宋体"}[Inform]{lang="EN-US"}[报文的目的主机的参数。]{style="font-family:宋体"}

[**[trap]{lang="EN-US"}**]{#struct_0_x1400_15709_x215832387}[：配置接收]{style="font-family:宋体"}[Trap]{lang="EN-US"}[报文的目的主机的参数。]{style="font-family:宋体"}

[**[address]{lang="EN-US"}**]{#struct_0_x1400_15709_167330471}[：指定设备发出的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[信息中的目的地址。]{style="font-family:宋体"}

[**[udp-domain]{lang="EN-US"}**]{#struct_0_x1400_15709_901253012}[：指定使用]{style="font-family:宋体"}[UDP]{lang="EN-US"}[协议来传输]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[告警信息。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1400_15709_39356769}[：接收告警信息的目的主机的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址或主机名，主机名为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[253]{lang="EN-US"}[个字符的字符串，不区分大小写，字符串仅可包含字母、数字、"]{style="font-family:宋体"}[-]{lang="EN-US"}["、"]{style="font-family:宋体"}[\_]{lang="EN-US"}["或"]{style="font-family:宋体"}[.]{lang="EN-US"}["。若使用主机名配置，发送时将获取主机名对应的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，向对应的主机发送告警信息。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**[ *ipv6-address*]{lang="EN-US"}]{#struct_0_x1400_15709_666115048}[：接收告警信息的目的主机的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址或主机名，主机名为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[253]{lang="EN-US"}[个字符的字符串，不区分大小写，字符串仅可包含字母、数字、"]{style="font-family:宋体"}[-]{lang="EN-US"}["、"]{style="font-family:宋体"}[\_]{lang="EN-US"}["或"]{style="font-family:宋体"}[.]{lang="EN-US"}["。若使用主机名配置，发送时将获取主机名对应的]{style="font-family:宋体"}[Ipv6]{lang="EN-US"}[地址，向对应的主机发送告警信息。]{style="font-family:宋体"}

[**[udp-port]{lang="EN-US"}**[ *port-number*]{lang="EN-US"}]{#struct_0_x1400_15709_1686137990}[：指定目的主机上用来接收告警信息的端口号，缺省值为]{style="font-family:宋体"}[162]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x1400_15709_x1502751462}[：指定目的主机所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示目的主机位于公网中。]{style="font-family:宋体"}

[**[params]{lang="EN-US"}**[ **securityname** *security-string*]{lang="EN-US"}]{#struct_0_x1400_15709_x1474974717}[：指定认证的参数，]{style="font-family:宋体"}*[security-string]{lang="EN-US"}*[为]{style="font-family:宋体"}[SNMPv1]{lang="EN-US"}[、]{style="font-family:宋体"}[SNMPv2c]{lang="EN-US"}[的团体名或]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[的用户名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[**[v1]{lang="EN-US"}**]{#struct_0_x1400_15709_1912983975}[：]{style="font-family:宋体"}[SNMPv1]{lang="EN-US"}[版本。]{style="font-family:宋体"}

[**[v2c]{lang="EN-US"}**]{#struct_0_x1400_15709_x1752783312}[：]{style="font-family:宋体"}[SNMPv2c]{lang="EN-US"}[版本。]{style="font-family:宋体"}

[**[v3]{lang="EN-US"}**]{#struct_0_x1400_15709_167396007}[：]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[版本。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication]{lang="EN-US"}**]{#struct_0_x1400_15709_544945124}[：指明对报文进行认证但不加密。认证功能用来验证报文的完整性或报文是否被篡改等，认证密码在创建]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户时配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[privacy]{lang="EN-US"}**]{#struct_0_x1400_15709_x386226187}[：指明对报文进行认证和加密。加密是对报文的数据部分进行加密处理以防信息被窃取，认证密码和加密密码在创建]{style="font-family:
宋体"}[SNMPv3]{lang="EN-US"}[用户时配置。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1661414774}

[[根据实际组网需要，用户可以多次使用该命令配置不同的目的主机的属性，使得设备可以向多个]{style="font-family:宋体"}[NMS]{lang="EN-US"}]{#struct_0_x1400_15709_x1434311246}[发送告警信息。可以配置的目的主机的个数与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不指定]{lang="EN-US" style="font-family:宋体"}**[udp-port]{lang="EN-US"}**[ *port-number*]{lang="EN-US"}]{#struct_0_x1400_15709_x1776692238}[参数时，使用的端口号为]{lang="EN-US" style="font-family:宋体"}[162]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}[162]{lang="EN-US"}[是]{lang="EN-US" style="font-family:宋体"}[SNMP]{lang="EN-US"}[协议规定的]{lang="EN-US" style="font-family:宋体"}[NMS]{lang="EN-US"}[接收告警信息的端口，通常情况下（比如使用]{lang="EN-US" style="font-family:宋体"}[iMC]{lang="EN-US"}[或者]{lang="EN-US" style="font-family:宋体"}[MIB Browser]{lang="EN-US"}[作为]{lang="EN-US" style="font-family:宋体"}[NMS]{lang="EN-US"}[时），使用该缺省值即可。]{lang="EN-US" style="font-family:宋体"}[如果要将该参数修改为其它值，则必须和]{style="font-family:
宋体"}[NMS]{lang="EN-US"}[上的配置保持一致。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不指定]{style="font-family:宋体"}]{#struct_0_x1400_15709_1536674800}**[v1]{lang="EN-US"}**[、]{style="font-family:宋体"}**[v2c]{lang="EN-US"}**[、]{style="font-family:宋体"}**[v3]{lang="EN-US"}**[版本参数时，使用的版本是]{style="font-family:宋体"}[v1]{lang="EN-US"}[。设备配置的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[版本必须和]{style="font-family:宋体"}[NMS]{lang="EN-US"}[上运行的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[版本一致，否则，]{style="font-family:宋体"}[NMS]{lang="EN-US"}[将收不到告警信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不指定]{lang="EN-US" style="font-family:宋体"}**[authentication]{lang="EN-US"}**]{#struct_0_x1400_15709_1230914156}[和]{lang="EN-US" style="font-family:
宋体"}**[privacy]{lang="EN-US"}**[参数时，使用的是不认证不加密的安全级别。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_167461543}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_379294356}[允许向]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[发送]{style="font-family:宋体"}[SNMPv3 Trap]{lang="EN-US"}[报文，用户名为]{style="font-family:宋体"}[public]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_613019980}

[\[Sysname\] snmp-agent trap enable standard]{lang="EN-US"}

[\[Sysname\] snmp-agent target-host trap address udp-domain 10.1.1.1 params securityname public v3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_636757874}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ { **inform** \| **trap** } **source**]{lang="EN-US"}]{#struct_0_x1400_15709_294490278}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **trap** **enable**]{lang="EN-US"}]{#struct_0_x1400_15709_1272466638}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **trap** **life**]{lang="EN-US"}]{#struct_0_x1400_15709_x1156124634}
:::

::: {#-1971955544 .myid}
[]{#_Toc404796960}[]{#struct_0_x1400_15709_439892395}

**SNMP \-- SNMP配置命令 \-- snmp-agent trap enable**

------------------------------------------------------------------------

[**[snmp-agent]{lang="EN-US"}**[ **trap** **enable**]{lang="EN-US"}]{#struct_0_x1400_15709_35513483}[命令用来在全局下开启告警功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **trap** **enable**]{lang="EN-US"}]{#struct_0_x1400_15709_167527079}[命令用来在全局下关闭告警功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x376752831}

[**[snmp-agent]{lang="EN-US"}**[ **trap** **enable** \[ **configuration** \| *protocol* **\|** **standard** \[ **authentication** \| **coldstart** \| **linkdown** \| **linkup** \| **warmstart** \] \* \| **system** \]]{lang="EN-US"}]{#struct_0_x1400_15709_x1971237}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **trap** **enable** \[ **configuration** \| *protocol* **\|** **standard** \[ **authentication** \| **coldstart** \| **linkdown** \| **linkup** \| **warmstart** \] \* \| **system** \]]{lang="EN-US"}]{#struct_0_x1400_15709_1409018260}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1400_15709_166544039}

[[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_1843090256}[配置告警、标准告警和系统告警功能处于开启状态，其他各模块告警功能是否开启请参见各模块手册。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_78332889}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_1924442478}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1913855119}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x651075091}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x198858090}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1400_15709_166609575}

[**[configuration]{lang="EN-US"}**]{#struct_0_x1400_15709_x1085367593}[：]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[配置告警信息。配置该参数后，系统会以]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟为周期，查看周期内当前运行配置或者启动配置是否被修改，以及是否有用户对启动配置文件进行修改，并将最后一次修改形成一条告警输出。]{style="font-family:宋体"}

[*[protocol]{lang="EN-US"}*]{#struct_0_x1400_15709_x590917474}[：开启指定协议模块的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[告警功能。有关此参数的详细介绍，请参见各模块的命令手册。]{style="font-family:宋体"}

[**[standard]{lang="EN-US"}**]{#struct_0_x1400_15709_480090913}[：]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[标准告警信息。包括以下五种：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication]{lang="EN-US"}**]{#struct_0_x1400_15709_1081943826}[：]{lang="EN-US" style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备时认证失败，输出]{lang="EN-US" style="font-family:宋体"}[SNMP]{lang="EN-US"}[认证失败的告警信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[coldstart]{lang="EN-US"}**]{#struct_0_x1400_15709_x1474494034}[：当设备重新启动时，输出设备冷启动告警信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[linkdown]{lang="EN-US"}**]{#struct_0_x1400_15709_449109561}[：当接口的链路]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}[时，输出]{lang="EN-US" style="font-family:宋体"}[linkDown]{lang="EN-US"}[告警信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[linkup]{lang="EN-US"}**]{#struct_0_x1400_15709_x1287609988}[：当接口的链路]{lang="EN-US" style="font-family:宋体"}[up]{lang="EN-US"}[时，输出]{lang="EN-US" style="font-family:宋体"}[linkUp]{lang="EN-US"}[告警信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[warmstart]{lang="EN-US"}**]{#struct_0_x1400_15709_167068328}[：当]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[模块重新启动时，输出热启动告警信息。]{style="font-family:宋体"}

[**[system]{lang="EN-US"}**]{#struct_0_x1400_15709_1809426791}**[：]{style="font-family:宋体"}**[SNMP]{lang="EN-US"}[系统告警信息。配置该参数后，如果系统时间被修改、系统重启或系统主用启动软件包不可用，均会生成告警信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_572853411}

[[开启告警功能，设备就可以向目的主机发送告警信息。具体是发送]{style="font-family:宋体"}[Inform]{lang="EN-US"}]{#struct_0_x1400_15709_x60927789}[报文还是]{style="font-family:宋体"}[Trap]{lang="EN-US"}[报文，以及发往哪个目的主机，请通过]{style="font-family:宋体"}**[snmp-agent]{lang="EN-US"}**[ **target-host**]{lang="EN-US"}[命令来配置。]{style="font-family:宋体"}

[[不指定可选参数时，表示在全局下开启]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1400_15709_x1945153911}[关闭所有可选模块的告警功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x146272522}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_1413162868}[允许发送]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[认证失败的告警信息，使用团体名]{style="font-family:宋体"}[public]{lang="EN-US"}[，向]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[的目的主机发送]{style="font-family:宋体"}[Trap]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_167133864}

[\[Sysname\] snmp-agent target-host trap address udp-domain 10.1.1.1 params securityname public]{lang="EN-US"}

[\[Sysname\] snmp-agent trap enable standard authentication]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x467890091}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **target-host**]{lang="EN-US"}]{#struct_0_x1400_15709_x109829681}
:::

::: {#1045862325 .myid}
[]{#_Toc404796961}[]{#struct_0_x1400_15709_x157611167}

**SNMP \-- SNMP配置命令 \-- snmp-agent trap if-mib link extended**

------------------------------------------------------------------------

[**[snmp-agent]{lang="EN-US"}**[ **trap** **if-mib** **link** **extended**]{lang="EN-US"}]{#struct_0_x1400_15709_792821298}[命令用来对标准格式的]{style="font-family:宋体"}[linkUp]{lang="EN-US"}[或]{style="font-family:宋体"}[linkDown]{lang="EN-US"}[告警信息进行私有扩展。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **trap** **if-mib** **link** **extended**]{lang="EN-US"}]{#struct_0_x1400_15709_1596130134}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1662212238}

[**[snmp-agent]{lang="EN-US"}**[ **trap** **if-mib** **link** **extended**]{lang="EN-US"}]{#struct_0_x1400_15709_x9224894}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **trap** **if-mib** **link** **extended**]{lang="EN-US"}]{#struct_0_x1400_15709_1367358478}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1400_15709_167199400}

[[系统发送的]{style="font-family:宋体"}[linkUp/linkDown]{lang="EN-US"}]{#struct_0_x1400_15709_x1720318389}[告警信息的格式为标准格式，不对其进行私有扩展。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1259022401}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_100968150}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1245091907}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x1091520399}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_913817174}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_120962669}

[[扩展格式的]{style="font-family:宋体"}[linkUp/linkDown]{lang="EN-US"}]{#struct_0_x1400_15709_x2016080667}[告警信息由标准格式的]{style="font-family:宋体"}[linkUp/linkDown]{lang="EN-US"}[告警信息后增加接口描述和接口类型信息构成，使用扩展格式的告警信息有助于网络管理员快速定位问题。]{style="font-family:宋体"}

[[需要注意的是，配置该命令后，设备发送的]{style="font-family:宋体"}[linkUp/linkDown]{lang="EN-US"}]{#struct_0_x1400_15709_167264936}[告警信息为扩展格式的信息。如果]{style="font-family:宋体"}[NMS]{lang="EN-US"}[不支持扩展格式，可能会无法解析信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x607511733}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_x145201698}[对标准格式的]{style="font-family:宋体"}[linkUp/linkDown]{lang="EN-US"}[告警信息进行私有扩展。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_x419920578}

[\[Sysname\] snmp-agent trap if-mib link extended]{lang="EN-US"}
:::

::: {#1502780694 .myid}
[]{#_Toc404796962}[]{#struct_0_x1400_15709_x448670979}[]{#_Toc336007828}

**SNMP \-- SNMP配置命令 \-- snmp-agent trap log**

------------------------------------------------------------------------

[**[snmp-agent]{lang="EN-US"}**[ **trap log**]{lang="EN-US"}]{#struct_0_x1400_15709_x419294831}[命令用来开启]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[告警日志功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **trap log**]{lang="EN-US"}]{#struct_0_x1400_15709_x2095799196}[命令用来关闭]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[告警日志功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_232673638}

[**[snmp-agent]{lang="EN-US"}**[ **trap log**]{lang="EN-US"}]{#struct_0_x1400_15709_167330472}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **trap log**]{lang="EN-US"}]{#struct_0_x1400_15709_901253011}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x935320917}

[[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_x1782324685}[告警日志功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1470923981}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_x1135105917}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1118281711}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_1540381730}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x2003388272}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_167396008}

[[打开]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_544945127}[告警日志开关，]{style="font-family:宋体"}[Agent]{lang="EN-US"}[向]{style="font-family:宋体"}[NMS]{lang="EN-US"}[发送告警时，]{style="font-family:宋体"}[Agent]{lang="EN-US"}[会记录该告警相关的信息并保存到设备的信息中心。通过设置信息中心的参数，最终决定]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[告警日志的输出规则（即是否允许输出以及输出方向）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x386226186}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_1661349238}[打开]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[告警日志开关。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_1726489518}

[\[Sysname\] snmp-agent trap log]{lang="EN-US"}
:::

::: {#-1474156421 .myid}
[]{#_Toc404796963}[]{#struct_0_x1400_15709_1247825103}

**SNMP \-- SNMP配置命令 \-- snmp-agent trap life**

------------------------------------------------------------------------

[**[snmp-agent]{lang="EN-US"}**[ **trap** **life**]{lang="EN-US"}]{#struct_0_x1400_15709_x1596726019}[命令用来设置告警信息的保存时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **trap** **life**]{lang="EN-US"}]{#struct_0_x1400_15709_263226537}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_167461544}

[**[snmp-agent]{lang="EN-US"}**[ **trap** **life** *seconds*]{lang="EN-US"}]{#struct_0_x1400_15709_379294353}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **trap** **life**]{lang="EN-US"}]{#struct_0_x1400_15709_613019983}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1400_15709_636757871}

[[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_294490281}[告警信息的保存时间为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1317096661}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_1987505761}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1155710416}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_2062361777}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_167527080}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x714459832}

[*[seconds]{lang="EN-US"}*]{#struct_0_x1400_15709_1035993820}[：超时时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2592000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1319008115}

[[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_906427729}[模块使用队列来发送告警信息，告警信息进入消息发送队列时会启动一个存活定时器。如果直到定时器超时（即达到]{style="font-family:宋体"}**[snmp-agent]{lang="EN-US"}**[ **trap** **life**]{lang="EN-US"}[命令设置的时间），告警信息还没有被发送出去，系统就会将该告警信息从发送队列中删除。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_669163994}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_1013719178}[设置告警信息的保存时间为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_1391408392}

[\[Sysname\] snmp-agent trap life 60]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_166544040}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **trap** **enable**]{lang="EN-US"}]{#struct_0_x1400_15709_269112135}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **target-host**]{lang="EN-US"}]{#struct_0_x1400_15709_x1015490772}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **trap** **queue-size**]{lang="EN-US"}]{#struct_0_x1400_15709_129049556}
:::

::::: {#-1474636508 .myid}
[]{#_Toc404796964}[]{#struct_0_x1400_15709_x1204884185}[]{#_Toc393286384}

**SNMP \-- SNMP配置命令 \-- snmp-agent trap periodical-interval**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](SNMP命令.files/image001.png){#图片 1 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1400_15709_1817159193}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1400_15709_x1872087748}
:::

[ ]{lang="EN-US"}

[**[snmp-agent trap periodical-interval]{lang="EN-US"}**]{#struct_0_x1400_15709_x311429587}[命令用来配置周期]{style="font-family:宋体"}[Trap]{lang="EN-US"}[发送的时间间隔。]{style="font-family:宋体"}

[**[undo snmp-agent trap periodical-interval]{lang="EN-US"}**]{#struct_0_x1400_15709_4326114}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_945574163}

[**[snmp-agent trap periodical-interval ]{lang="EN-US"}***[interval-time]{lang="EN-US"}*]{#struct_0_x1400_15709_x1205080793}

[**[undo snmp-agent trap periodical-interval]{lang="EN-US"}**]{#struct_0_x1400_15709_x1834250444}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x17932942}

[[周期]{style="font-family:宋体"}[Trap]{lang="EN-US"}]{#struct_0_x1400_15709_x1961432915}[发送的时间间隔为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x760283803}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_349404786}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_472892608}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x1234619307}

[[network-operator]{lang="EN-US"}]{#struct_0_x1400_15709_x1205015257}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x369751008}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1400_15709_x1123838462}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1183593366}

[*[interval-time]{lang="EN-US"}*]{#struct_0_x1400_15709_x479978441}[：周期]{style="font-family:宋体"}[Trap]{lang="EN-US"}[消息发送的时间间隔，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[或者]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_692936200}

[[当设备开启周期]{style="font-family:宋体"}[Trap]{lang="EN-US"}]{#struct_0_x1400_15709_x1490026770}[功能时，设备将在指定的时间间隔内向]{style="font-family:宋体"}[NMS]{lang="EN-US"}[发送周期]{style="font-family:宋体"}[Trap]{lang="EN-US"}[消息，表示当前设备的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[功能运行正常。]{style="font-family:宋体"}

[[需要注意的是，如果周期]{style="font-family:宋体"}[Trap]{lang="EN-US"}]{#struct_0_x1400_15709_2115414818}[的时间间隔设置为]{style="font-family:宋体"}[0]{lang="EN-US"}[秒，则表示关闭周期]{style="font-family:宋体"}[Trap]{lang="EN-US"}[发送功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1637299307}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_x1205211865}[设置周期]{style="font-family:宋体"}[Trap]{lang="EN-US"}[发送的时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_x2064243980}

[\[sysname\] snmp-agent trap periodical-interval 10]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_x2102119647}[关闭周期]{style="font-family:宋体"}[Trap]{lang="EN-US"}[发送功能。]{style="font-family:宋体"}

[[\<sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_x198088838}

[\[sysname\] snmp-agent trap periodical-interval 0]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1365737578}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1400_15709_x87194705}**[target-host]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent trap enable]{lang="EN-US"}**]{#struct_0_x1400_15709_1944996328}
:::::

::: {#-2142649509 .myid}
[]{#_Toc404796965}[]{#struct_0_x1400_15709_27440632}

**SNMP \-- SNMP配置命令 \-- snmp-agent trap queue-size**

------------------------------------------------------------------------

[**[snmp-agent]{lang="EN-US"}**[ **trap** **queue-size**]{lang="EN-US"}]{#struct_0_x1400_15709_187023133}[命令用来设置告警信息发送队列的长度。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **trap** **queue-size**]{lang="EN-US"}]{#struct_0_x1400_15709_x364592981}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_741083747}

[**[snmp-agent]{lang="EN-US"}**[ **trap** **queue-size** *size*]{lang="EN-US"}]{#struct_0_x1400_15709_x1863032509}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **trap** **queue-size**]{lang="EN-US"}]{#struct_0_x1400_15709_166609576}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1085367592}

[[告警信息的发送队列最多可以存储]{style="font-family:宋体"}[100]{lang="EN-US"}]{#struct_0_x1400_15709_2137965881}[条告警信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1675640766}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_x384969502}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x917957358}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x1660598374}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x818717980}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1400_15709_668682083}

[*[size]{lang="EN-US"}*]{#struct_0_x1400_15709_1733152272}[：消息队列中可以存储的告警信息的数目，取值范围]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1657404982}

[[告警信息产生后，会进入告警信息消息队列进行发送，告警信息消息队列的长度决定了队列最多可以存储的告警信息的数目。当告警信息队列达到设定长度后，最新生成的告警信息会进入消息队列，最早产生的告警信息被丢弃。]{style="font-family:宋体"}]{#struct_0_x1400_15709_x1781771736}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_584731057}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_x2125319428}[设置发送告警信息的消息队列最多可以存储]{style="font-family:宋体"}[200]{lang="EN-US"}[条告警信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_5860016}

[\[Sysname\] snmp-agent trap queue-size 200]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1122631469}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **trap** **enable**]{lang="EN-US"}]{#struct_0_x1400_15709_1191815219}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **target-host**]{lang="EN-US"}]{#struct_0_x1400_15709_x435899019}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **trap** **life**]{lang="EN-US"}]{#struct_0_x1400_15709_1733217808}
:::

::: {#-1402084142 .myid}
[]{#_Toc404796966}[]{#struct_0_x1400_15709_x241911925}

**SNMP \-- SNMP配置命令 \-- snmp-agent usm-user { v1 \| v2c }**

------------------------------------------------------------------------

[**[snmp-agent]{lang="EN-US"}**[ **usm-user** { **v1** \| **v2c** }]{lang="EN-US"}]{#struct_0_x1400_15709_x1609660852}[命令用来为]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[组添加新用户。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **usm-user** { **v1** \| **v2c** }]{lang="EN-US"}]{#struct_0_x1400_15709_2025234010}[命令用来删除]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[组的用户。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1840163662}

[**[snmp-agent]{lang="EN-US"}**[ **usm-user** { **v1** \| **v2c** } *user-name* *group-name* \[ **acl** { *acl-number \|* **name** *acl-name* } \| **acl** **ipv6** { *ipv6-acl-number* \| **name** *ipv6-acl-name* } \] \*]{lang="EN-US"}]{#struct_0_x1400_15709_1460159253}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **usm-user** { **v1** \| **v2c** } *user-name* ]{lang="EN-US"}]{#struct_0_x1400_15709_319234933}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1300154794}

[[设备上没有配置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_1088194114}[用户。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1733283344}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_914917883}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1553463658}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x1663062576}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_935989804}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1934563203}

[**[v1]{lang="EN-US"}**]{#struct_0_x1400_15709_990183487}[：表示配置的用户名适用于]{style="font-family:宋体"}[SNMPv1]{lang="EN-US"}[组网环境。]{style="font-family:宋体"}

[**[v2c]{lang="EN-US"}**]{#struct_0_x1400_15709_1325798635}[：表示配置的用户名适用于]{style="font-family:宋体"}[SNMPv2c]{lang="EN-US"}[组网环境。]{style="font-family:宋体"}

[*[user-name]{lang="EN-US"}*]{#struct_0_x1400_15709_1733348880}[：用户名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[*[group-name]{lang="EN-US"}*]{#struct_0_x1400_15709_x291784179}[：该用户对应的组名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[acl]{lang="EN-US"}**[ *acl-number*]{lang="EN-US"}]{#struct_0_x1400_15709_x370870093}[：将用户与基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[绑定，]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[表示访问列表号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。当未引用]{style="font-family:宋体"}[ACL]{lang="EN-US"}[或者引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在时，允许所有]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备；当]{style="font-family:宋体"}[ACL]{lang="EN-US"}[为空时，会禁止所有的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备；当引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[非空时，则只有]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中]{style="font-family:宋体"}[permit]{lang="EN-US"}[的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[才能访问设备，其它]{style="font-family:宋体"}[NMS]{lang="EN-US"}[不允许访问设备，以免非法]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}***[ acl-name]{lang="EN-US"}*]{#struct_0_x1400_15709_x1204425433}[：将团体名与基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[名绑定，]{style="font-family:宋体"}*[acl-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。当未引用]{style="font-family:宋体"}[ACL]{lang="EN-US"}[或者引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在时，允许所有]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备；当]{style="font-family:宋体"}[ACL]{lang="EN-US"}[为空时，会禁止所有的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备；当引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[非空时，则只有]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中]{style="font-family:宋体"}[permit]{lang="EN-US"}[的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[才能访问设备，其它]{style="font-family:宋体"}[NMS]{lang="EN-US"}[不允许访问设备，以免非法]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备。关于]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的详细描述和介绍请参见"]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{style="font-family:宋体"}[QoS]{lang="EN-US"}[配置指导"中的"]{style="font-family:宋体"}[ACL]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[acl]{lang="EN-US"}**[ **ipv6** *ipv6-acl-number*]{lang="EN-US"}]{#struct_0_x1400_15709_x442957046}[：将用户与基本]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[绑定，]{style="font-family:宋体"}*[ipv6-acl-number]{lang="EN-US"}*[表示访问列表号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。当未引用]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[或者引用的]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[不存在时，允许所有]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备；当]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[为空时，会禁止]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备；当引用的]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[非空时，则只有]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[中]{style="font-family:宋体"}[permit]{lang="EN-US"}[的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[才能访问设备，其它]{style="font-family:宋体"}[NMS]{lang="EN-US"}[不允许访问设备，以免非法]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}***[ ipv6-acl-name]{lang="EN-US"}*]{#struct_0_x1400_15709_1731736030}[：将团体名与基本]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[名绑定，]{style="font-family:宋体"}*[acl-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。当未引用]{style="font-family:宋体"}[ACL]{lang="EN-US"}[或者引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在时，允许所有]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备；当]{style="font-family:宋体"}[ACL]{lang="EN-US"}[为空时，会禁止所有的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备；当引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[非空时，则只有]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中]{style="font-family:宋体"}[permit]{lang="EN-US"}[的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[才能访问设备，其它]{style="font-family:宋体"}[NMS]{lang="EN-US"}[不允许访问设备，以免非法]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1880831320}

[[FIPS]{lang="EN-US"}]{#struct_0_x1400_15709_x1573982819}[模式下，不支持本命令。]{style="font-family:宋体"}

[[SNMPv1]{lang="EN-US"}]{#struct_0_x1400_15709_x1459854575}[和]{style="font-family:宋体"}[SNMPv2c]{lang="EN-US"}[组网应用中]{style="font-family:宋体"}[NMS]{lang="EN-US"}[和]{style="font-family:宋体"}[Agent]{lang="EN-US"}[之间使用团体名来认证，]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[组网应用中使用用户名来认证。]{style="font-family:宋体"}

[[设备支持配置]{style="font-family:宋体"}[SNMPv1]{lang="EN-US"}]{#struct_0_x1400_15709_x843450172}[和]{style="font-family:宋体"}[SNMPv2c]{lang="EN-US"}[用户以供习惯用户名配置方式的用户。创建一个]{style="font-family:宋体"}[SNMPv1]{lang="EN-US"}[或]{style="font-family:宋体"}[SNMPv2c]{lang="EN-US"}[用户相当于添加一个新的团体名，其读写属性依赖于用户所在组的读、写、通知视图配置。]{style="font-family:宋体"}

[[要使配置的用户生效，必须先创建]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x1400_15709_x1903685293}[组。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1733414416}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_x677166549}[在]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[组]{style="font-family:宋体"}[readCom]{lang="EN-US"}[里创建]{style="font-family:宋体"}[SNMPv2c]{lang="EN-US"}[用户]{style="font-family:宋体"}[userv2c]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_1468120473}

[\[Sysname\] snmp-agent sys-info version v2c]{lang="EN-US"}

[\[Sysname\] snmp-agent group v2c readCom]{lang="EN-US"}

[\[Sysname\] snmp-agent usm-user v2c userv2c readCom]{lang="EN-US"}

[[如果]{style="font-family:宋体"}[NMS]{lang="EN-US"}]{#struct_0_x1400_15709_x1045408848}[需要访问]{style="font-family:宋体"}[Agent]{lang="EN-US"}[，则应将]{style="font-family:宋体"}[NMS]{lang="EN-US"}[的版本号指定为]{style="font-family:宋体"}[SNMPv2c]{lang="EN-US"}[，]{style="font-family:宋体"}[Read community]{lang="EN-US"}[选项填写为]{style="font-family:宋体"}[userv2c]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_1531069268}[在]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[组]{style="font-family:宋体"}[readCom]{lang="EN-US"}[里创建]{style="font-family:宋体"}[SNMPv2c]{lang="EN-US"}[用户]{style="font-family:宋体"}[userv2c]{lang="EN-US"}[，并且只允许]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[使用该用户名访问]{style="font-family:宋体"}[Agent]{lang="EN-US"}[，禁止其它]{style="font-family:宋体"}[NMS]{lang="EN-US"}[使用该用户名访问。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_1733479952}

[\[Sysname\] acl basic 2001]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2001\] rule permit source 1.1.1.1 0.0.0.0]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2001\] rule deny source any]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2001\] quit]{lang="EN-US"}

[\[Sysname\] snmp-agent sys-info version v2c]{lang="EN-US"}

[\[Sysname\] snmp-agent group v2c readCom]{lang="EN-US"}

[\[Sysname\] snmp-agent usm-user v2c userv2c readCom acl 2001]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_361134223}[在]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[组]{style="font-family:宋体"}[readCom]{lang="EN-US"}[里创建]{style="font-family:宋体"}[SNMPv2c]{lang="EN-US"}[用户]{style="font-family:宋体"}[userv2c]{lang="EN-US"}[，并且只允许]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.2]{lang="EN-US"}[的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[使用该用户名访问]{style="font-family:宋体"}[Agent]{lang="EN-US"}[，禁止其它]{style="font-family:宋体"}[NMS]{lang="EN-US"}[使用该用户名访问。]{style="font-family:宋体"}

[[\[Sysname\] acl basic name testacl]{lang="EN-US"}]{#struct_0_x1400_15709_339350284}

[\[Sysname-acl-ipv4-basic-testacl\] rule permit source 1.1.1.2 0.0.0.0]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-testacl\] rule deny source any]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-testacl\] quit]{lang="EN-US"}

[\[Sysname\] snmp-agent sys-info version v2c]{lang="EN-US"}

[\[Sysname\] snmp-agent group v2c readCom]{lang="EN-US"}

[\[Sysname\] snmp-agent usm-user v2c userv2c readCom acl name testacl]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1651195929}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **group**]{lang="EN-US"}]{#struct_0_x1400_15709_199417324}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **community**]{lang="EN-US"}]{#struct_0_x1400_15709_x143394111}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dispaly snmp-agent]{lang="EN-US"}**[ **community**]{lang="EN-US"}]{#struct_0_x1400_15709_x661111166}
:::

::: {#772646335 .myid}
[]{#_Toc404796967}[]{#struct_0_x1400_15709_x648833703}

**SNMP \-- SNMP配置命令 \-- snmp-agent usm-user v3**

------------------------------------------------------------------------

[**[snmp-agent]{lang="EN-US"}**[ **usm-user** **v3**]{lang="EN-US"}]{#struct_0_x1400_15709_x1671652042}[命令用来创建]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **usm-user** **v3**]{lang="EN-US"}]{#struct_0_x1400_15709_x1138957494}[命令用来删除]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1733545488}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_x1400_15709_887016824}[模式下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VACM]{lang="EN-US"}]{#struct_0_x1400_15709_39029087}[方式：]{lang="EN-US" style="font-family:宋体"}

[**[snmp-agent]{lang="EN-US"}**[ **usm-user** **v3** *user-name* *group-name* \[ **remote** { *ip-address* \| **ipv6** *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \] \] \[ { **cipher** \| **simple** } **authentication-mode** { **md5** \| **sha** } *auth-password* \[ **privacy-mode** { **aes128** \| **3des** \| **des56** } *priv-password* \] \] \[ **acl** { *acl-number \|* **name** *acl-name* } \| **acl** **ipv6** { *ipv6-acl-number* \| **name** *ipv6-acl-name* } \] \*]{lang="EN-US"}]{#struct_0_x1400_15709_x341399077}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **usm-user** **v3** *user-name* { **local** \| **engineid** *engineid-string* \| **remote** { *ip-address* \| **ipv6** *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \] }]{lang="EN-US"}]{#struct_0_x1400_15709_x1910494617}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RBAC]{lang="EN-US"}]{#struct_0_x1400_15709_1641265340}[方式：]{lang="EN-US" style="font-family:宋体"}

[**[snmp-agent]{lang="EN-US"}**[ **usm-user** **v3** *user-name* **user-role** *role-name* \[ **remote** { *ip-address* \| **ipv6** *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \] \] \[ { **cipher** \| **simple** } **authentication-mode** { **md5** \| **sha** } *auth-password* \[ **privacy-mode** { **aes128** \| **3des** **\| des56** } *priv-password* \] \] \[ **acl** { *acl-number \|* **name** *acl-name* } \| **acl** **ipv6** { *ipv6-acl-number* \| **name** *ipv6-acl-name* } \] \*]{lang="EN-US"}]{#struct_0_x1400_15709_2000610890}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **usm-user** **v3** *user-name* { **local** \| **engineid** *engineid-string* \| **remote** { *ip-address* \| **ipv6** *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \] }]{lang="EN-US"}]{#struct_0_x1400_15709_x2076829788}

[[FIPS]{lang="EN-US"}]{#struct_0_x1400_15709_1818122380}[模式下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VACM]{lang="EN-US"}]{#struct_0_x1400_15709_x1352619949}[方式：]{lang="EN-US" style="font-family:宋体"}

[**[snmp-agent]{lang="EN-US"}**[ **usm-user** **v3** *user-name* *group-name* \[ **remote** { *ip-address* \| **ipv6** *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \] \] { **cipher** \| **simple** } **authentication-mode** **sha** *auth-password* \[ **privacy-mode** **aes128** *priv-password* \] \[ **acl** { *acl-number \|* **name** *acl-name* } \| **acl** **ipv6** { *ipv6-acl-number* \| **name** *ipv6-acl-name* } \] \*]{lang="EN-US"}]{#struct_0_x1400_15709_x850388024}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **usm-user** **v3** *user-name* { **local** \| **engineid** *engineid-string* \| **remote** { *ip-address* \| **ipv6** *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \] }]{lang="EN-US"}]{#struct_0_x1400_15709_1063098114}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RBAC]{lang="EN-US"}]{#struct_0_x1400_15709_38963551}[方式：]{style="font-family:宋体"}

[**[snmp-agent]{lang="EN-US"}**[ **usm-user** **v3** *user-name* **user-role** *role-name* \[ **remote** { *ip-address* \| **ipv6** *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \] \] \[ { **cipher** \| **simple** } **authentication-mode**  **sha** *auth-password* \[ **privacy-mode** **aes128** *priv-password* \] \] \[ **acl** { *acl-number \|* **name** *acl-name* } \| **acl** **ipv6** { *ipv6-acl-number* \| **name** *ipv6-acl-name* } \] \*]{lang="EN-US"}]{#struct_0_x1400_15709_1369024126}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **usm-user** **v3** *user-name* { **local** \| **engineid** *engineid-string* \| **remote** { *ip-address* \| **ipv6** *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \] }]{lang="EN-US"}]{#struct_0_x1400_15709_422716986}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1239854835}

[[设备上没有配置]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}]{#struct_0_x1400_15709_1711751592}[用户。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1733611024}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_x1844993989}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x183445480}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_71339001}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x1219492703}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1530599763}

[*[user-name]{lang="EN-US"}*]{#struct_0_x1400_15709_x1343683701}[：用户名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[*[group-name]{lang="EN-US"}*]{#struct_0_x1400_15709_1175856157}[：该用户对应的组名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[user-role]{lang="EN-US"}**[ *role-name*]{lang="EN-US"}]{#struct_0_x1400_15709_x1899265306}[：该用户对应的角色名称，]{style="font-family:宋体"}*[role-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[remote]{lang="EN-US"}**[ { *ip-address* \| **ipv6** *ipv6-address* }]{lang="EN-US"}]{#struct_0_x1400_15709_x2139099228}[：接收]{style="font-family:宋体"}[Inform]{lang="EN-US"}[信息的目的主机的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址或者]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，通常为]{style="font-family:宋体"}[NMS]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址或者]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。当设备需要向目的主机发送]{style="font-family:宋体"}[SNMPv3 Inform]{lang="EN-US"}[报文时，该参数必须配置，还需要使用]{style="font-family:宋体"}**[snmp-agent]{lang="EN-US"}**[ **remote**]{lang="EN-US"}[命令将目的主机的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址或者]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址和引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[绑定。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x1400_15709_1732627984}[：目的主机所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示目的主机位于公网中。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_x1400_15709_1314502415}[：以密文方式设置认证密码和加密密码。当使用]{style="font-family:宋体"}[16]{lang="EN-US"}[进制字符作为密文密码时可以使用]{style="font-family:宋体"}**[snmp-agent]{lang="EN-US"}**[ **calculate-password**]{lang="EN-US"}[命令来计算获得。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_x1400_15709_543759181}[：以明文方式设置认证密码和加密密码。]{style="font-family:宋体"}

[**[authentication-mode]{lang="EN-US"}**]{#struct_0_x1400_15709_560238562}[：指明安全模式为需要认证。]{style="font-family:宋体"}[MD5]{lang="EN-US"}[算法的计算速度比]{style="font-family:宋体"}[SHA]{lang="EN-US"}[算法快，而]{style="font-family:宋体"}[SHA]{lang="EN-US"}[算法的安全强度比]{style="font-family:宋体"}[MD5]{lang="EN-US"}[算法高。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[md5]{lang="EN-US"}**]{#struct_0_x1400_15709_x349152755}[：指定认证协议为]{style="font-family:
宋体"}[MD5]{lang="EN-US"}[。]{style="font-family:宋体"}[MD5]{lang="EN-US"}[的相关内容请参见"安全配置指导"中的"]{style="font-family:宋体"}[IPSec]{lang="EN-US"}["。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sha]{lang="EN-US"}**]{#struct_0_x1400_15709_1136469906}[：指定认证协议为]{style="font-family:
宋体"}[SHA-1]{lang="EN-US"}[。]{style="font-family:宋体"}[SHA]{lang="EN-US"}[的相关内容请参见"安全配置指导"中的"]{style="font-family:宋体"}[IPSec]{lang="EN-US"}["。]{style="font-family:宋体"}

[*[auth-password]{lang="EN-US"}*]{#struct_0_x1400_15709_x497531692}[：设置认证密码，区分大小写，具体如下。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[采用明文设置认证密码时：非]{style="font-family:宋体"}]{#struct_0_x1400_15709_1732693520}[FIPS]{lang="EN-US"}[模式下，认证密码的长度范围是]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符，]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，认证密码的长度范围是]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[字符，密码元素的最少组合类型为]{style="font-family:宋体"}[4]{lang="EN-US"}[（必须包括数字、大写字母、小写字母以及特殊字符）。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[采用密文设置认证密码时：对密文加密密码的要求请参见]{style="font-family:宋体"}]{#struct_0_x1400_15709_124815729}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}1-13]{lang="EN-US"}](?772646335#_Ref316050483)[。]{style="font-family:
宋体"}

[]{#struct_0_x1400_15709_x1002898263}[[表1-13 ]{lang="EN-US"}[密文方式认证密码描述表]{style="font-family:
黑体"}]{#_Ref316050483}

[]{#table_struct_0_1597387429}[[认证算法]{style="font-family:黑体"}]{#struct_0_x1400_15709_x476538905}
:::

[[16]{lang="EN-US"}]{#struct_0_x1400_15709_875912584}[进制格式的认证密码长度]{style="font-family:黑体"}

[[非]{style="font-family:黑体"}[16]{lang="EN-US"}]{#struct_0_x1400_15709_x1791297611}[进制格式的认证密码长度]{style="font-family:黑体"}

[[md5]{lang="EN-US"}]{#struct_0_x1400_15709_x1578091239}

[[32]{lang="EN-US"}]{#struct_0_x1400_15709_1733152273}

[[53]{lang="EN-US"}]{#struct_0_x1400_15709_1657339446}

[[sha]{lang="EN-US"}]{#struct_0_x1400_15709_x1781639820}

[[40]{lang="EN-US"}]{#struct_0_x1400_15709_x1978531456}

[[57]{lang="EN-US"}]{#struct_0_x1400_15709_x1829014774}

[ ]{lang="EN-US"}

[**[privacy-mode]{lang="EN-US"}**]{#struct_0_x1400_15709_2044669034}[：表示安全模式为需要加密。加密算法的安全性由高到低依次是：]{style="font-family:宋体"}[AES]{lang="EN-US"}[、]{style="font-family:宋体"}[3DES]{lang="EN-US"}[、]{style="font-family:宋体"}[DES]{lang="EN-US"}[，安全性高的加密算法实现机制复杂，运算速度慢。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[aes128]{lang="EN-US"}**]{#struct_0_x1400_15709_1733217809}[：指定加密协议为]{lang="EN-US" style="font-family:宋体"}[AES]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[Advanced Encryption Standard]{lang="EN-US"}[，高级加密标准）。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[3des]{lang="EN-US"}**]{#struct_0_x1400_15709_38766943}[：指定加密协议为]{lang="EN-US" style="font-family:宋体"}[3DES]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[Triple Data Encryption Standard]{lang="EN-US"}[，三重数据加密标准）。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[des56]{lang="EN-US"}**]{#struct_0_x1400_15709_x241977461}[：指定加密协议为]{lang="EN-US" style="font-family:宋体"}[DES]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[Data Encryption Standard]{lang="EN-US"}[，数据加密标准）。]{lang="EN-US" style="font-family:宋体"}

[*[priv-password]{lang="EN-US"}*]{#struct_0_x1400_15709_x1999320410}[：设置加密密码，区分大小写，具体如下。明文加密密码的长度范围是]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[；如果选择密文方式，对密文加密密码的要求请参见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-14]{lang="EN-US"}](?772646335#_Ref312070103)[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[采用明文方式设置加密密码时：非]{style="font-family:宋体"}]{#struct_0_x1400_15709_251318869}[FIPS]{lang="EN-US"}[模式下，密码的长度范围是]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符；]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，加密密码的长度范围是]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[字符，密码元素的最少组合类型为]{style="font-family:宋体"}[4]{lang="EN-US"}[（必须包括数字、大写字母、小写字母以及特殊字符）。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[采用密文方式设置加密密码时：对密文加密密码的要求请参见]{style="font-family:宋体"}]{#struct_0_x1400_15709_2033163555}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}1-14]{lang="EN-US"}](?772646335#_Ref312070103)[。]{style="font-family:
宋体"}

[]{#struct_0_x1400_15709_1749751361}[[表1-14 ]{lang="EN-US"}[密文方式加密密码描述表]{style="font-family:
黑体"}]{#_Ref312070103}

[]{#table_struct_0_1355840709}[[认证算法]{style="font-family:黑体"}]{#struct_0_x1400_15709_1196931081}

[[加密算法]{style="font-family:黑体"}]{#struct_0_x1400_15709_1175315187}

[[16]{lang="EN-US"}]{#struct_0_x1400_15709_x1726639373}[进制格式的认证密码长度]{style="font-family:黑体"}

[[非]{style="font-family:黑体"}[16]{lang="EN-US"}]{#struct_0_x1400_15709_x157518107}[进制格式的认证密码长度]{style="font-family:黑体"}

[[md5]{lang="EN-US"}]{#struct_0_x1400_15709_1733283345}

[[aes128]{lang="EN-US"}]{#struct_0_x1400_15709_914983419}[或]{style="font-family:宋体"}[des56]{lang="EN-US"}

[[32]{lang="EN-US"}]{#struct_0_x1400_15709_495292401}

[[53]{lang="EN-US"}]{#struct_0_x1400_15709_x1570816936}

[[3des]{lang="EN-US"}]{#struct_0_x1400_15709_39422303}

[[64]{lang="EN-US"}]{#struct_0_x1400_15709_39356767}

[[73]{lang="EN-US"}]{#struct_0_x1400_15709_38832478}

[[sha]{lang="EN-US"}]{#struct_0_x1400_15709_x1831911357}

[[aes128]{lang="EN-US"}]{#struct_0_x1400_15709_x1007110421}[或]{style="font-family:宋体"}[des56]{lang="EN-US"}

[[40]{lang="EN-US"}]{#struct_0_x1400_15709_1733348881}

[[53]{lang="EN-US"}]{#struct_0_x1400_15709_x291718643}

[[3des]{lang="EN-US"}]{#struct_0_x1400_15709_39029086}

[[80]{lang="EN-US"}]{#struct_0_x1400_15709_38963550}

[[73]{lang="EN-US"}]{#struct_0_x1400_15709_38635870}

[ ]{lang="EN-US"}

[**[acl]{lang="EN-US"}**[ *acl-number*]{lang="EN-US"}]{#struct_0_x1400_15709_x1081638548}[：将用户与基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[绑定，]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[表示访问列表号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。当未引用]{style="font-family:宋体"}[ACL]{lang="EN-US"}[或者引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在时，允许所有]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备；当]{style="font-family:宋体"}[ACL]{lang="EN-US"}[为空时，会禁止所有的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备；当引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[非空时，则只有]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中]{style="font-family:宋体"}[permit]{lang="EN-US"}[的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[才能访问设备，其它]{style="font-family:宋体"}[NMS]{lang="EN-US"}[不允许访问设备，以免非法]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}***[ acl-name]{lang="EN-US"}*]{#struct_0_x1400_15709_361134224}[：将团体名与基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[名绑定，]{style="font-family:宋体"}*[acl-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。当未引用]{style="font-family:宋体"}[ACL]{lang="EN-US"}[或者引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在时，允许所有]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备；当]{style="font-family:宋体"}[ACL]{lang="EN-US"}[为空时，会禁止所有的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备；当引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[非空时，则只有]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中]{style="font-family:宋体"}[permit]{lang="EN-US"}[的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[才能访问设备，其它]{style="font-family:宋体"}[NMS]{lang="EN-US"}[不允许访问设备，以免非法]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备。关于]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的详细描述和介绍请参见"]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{style="font-family:宋体"}[QoS]{lang="EN-US"}[配置指导"中的"]{style="font-family:宋体"}[ACL]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[acl]{lang="EN-US"}**[ **ipv6** *ipv6-acl-number*]{lang="EN-US"}]{#struct_0_x1400_15709_893346218}[：将用户与基本]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[绑定，]{style="font-family:宋体"}*[ipv6-acl-number]{lang="EN-US"}*[表示访问列表号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。当未引用]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[或者引用的]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[不存在时，允许所有]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备；当]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[为空时，会禁止]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备；当引用的]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[非空时，则只有]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[中]{style="font-family:宋体"}[permit]{lang="EN-US"}[的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[才能访问设备，其它]{style="font-family:宋体"}[NMS]{lang="EN-US"}[不允许访问设备，以免非法]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}***[ ipv6-acl-name]{lang="EN-US"}*]{#struct_0_x1400_15709_339350279}[：将团体名与基本]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[名绑定，]{style="font-family:宋体"}*[acl-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。当未引用]{style="font-family:宋体"}[ACL]{lang="EN-US"}[或者引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在时，允许所有]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备；当]{style="font-family:宋体"}[ACL]{lang="EN-US"}[为空时，会禁止所有的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备；当引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[非空时，则只有]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中]{style="font-family:宋体"}[permit]{lang="EN-US"}[的]{style="font-family:宋体"}[NMS]{lang="EN-US"}[才能访问设备，其它]{style="font-family:宋体"}[NMS]{lang="EN-US"}[不允许访问设备，以免非法]{style="font-family:宋体"}[NMS]{lang="EN-US"}[访问设备。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_x1400_15709_636622702}[：表示本地实体引擎。]{style="font-family:宋体"}

[**[engineid]{lang="EN-US"}**[ *engineid-string*]{lang="EN-US"}]{#struct_0_x1400_15709_973235776}[：指定与该用户相关联的引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[字符串，必须为偶数个十六进制数，十六进制数的个数为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[。全]{style="font-family:宋体"}[0]{lang="EN-US"}[和全]{style="font-family:宋体"}[F]{lang="EN-US"}[均被认为是无效参数。由于]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[版本的用户名、密文密码等都和引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[相关联，如果更改了引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[，则原引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[下配置的用户名、密码失效，更改后可以使用该参数将]{style="font-family:宋体"}*[engineid-string]{lang="EN-US"}*[指定为创建该用户时的本地引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x1843341962}

[[SNMPv3]{lang="EN-US"}]{#struct_0_x1400_15709_1733414417}[用户与]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体引擎相关联，缺省情况下，创建的]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户与本地]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体引擎相关联。使用]{style="font-family:宋体"}**[remote]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}[参数创建与远端]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体引擎关联的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[用户。]{style="font-family:宋体"}

[[创建]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}]{#struct_0_x1400_15709_38570334}[用户时，可以通过两种配置方式来控制用户访问的权限：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过]{style="font-family:宋体"}]{#struct_0_x1400_15709_x677232085}[VACM]{lang="EN-US"}[方式配置的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[用户依附于]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[组，创建用户时，请先创建组。否则，用户能够创建成功但是不生效。一个组可以包含多个用户。组定义了用户能够访问的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[对象（通过]{style="font-family:宋体"}[MIB]{lang="EN-US"}[视图来限定）以及是否进行认证和加密等，而认证和加密的具体算法和密码则是在创建用户时定义。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过]{lang="EN-US" style="font-family:宋体"}[RBAC]{lang="EN-US"}]{#struct_0_x1400_15709_1032501057}[方式配置的]{lang="EN-US" style="font-family:宋体"}[SNMP]{lang="EN-US"}[用户依附于用户角色，创建用户时，通过]{lang="EN-US" style="font-family:宋体"}**[user-role]{lang="EN-US"}**[ *role-name*]{lang="EN-US"}[参数配置用户的角色。用户角色定义了]{lang="EN-US" style="font-family:宋体"}[SNMP]{lang="EN-US"}[用户能够访问的]{lang="EN-US" style="font-family:宋体"}[SNMP]{lang="EN-US"}[对象以及操作类型（通过]{lang="EN-US" style="font-family:宋体"}**[rule]{lang="EN-US"}**[规则来限定）。使用]{lang="EN-US" style="font-family:宋体"}[RBAC]{lang="EN-US"}[方式创建]{lang="EN-US" style="font-family:宋体"}[SNMP v3]{lang="EN-US"}[用户后，还可以使用]{lang="EN-US" style="font-family:宋体"}**[snmp-agent]{lang="EN-US"}**[ **usm-user** **v3** **user-role**]{lang="EN-US"}[命令为该用户绑定更多的用户角色，最多可绑定]{lang="EN-US" style="font-family:宋体"}[64]{lang="EN-US"}[个用户角色。]{lang="EN-US" style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1400_15709_x2058884342}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过]{style="font-family:宋体"}]{#struct_0_x1400_15709_38766942}[VACM]{lang="EN-US"}[方式配置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[用户时，当用户名相同，新配置会覆盖旧配置，以最后一次配置为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过]{style="font-family:宋体"}]{#struct_0_x1400_15709_x1258817674}[RBAC]{lang="EN-US"}[方式配置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[用户时，可以多次使用本命令为已创建的]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户添加角色，若未配置其他参数，则其他配置不变，只添加角色；若同时配置其他参数（如认证方式），则为用户添加角色，同时修改其他配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以明文或密文方式设置的密码，均以密文方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_x1400_15709_22303397}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NMS]{lang="EN-US"}]{#struct_0_x1400_15709_x1111411401}[在访问设备时，必须输入明文密码，因此在创建用户时请牢记用户名以及对应的明文密码。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RBAC]{lang="EN-US"}]{#struct_0_x1400_15709_x2025053299}[配置方式要求]{style="font-family:宋体"}[NMS]{lang="EN-US"}[在访问]{style="font-family:宋体"}[Agent]{lang="EN-US"}[时，不仅需要授予]{style="font-family:宋体"}[NMS]{lang="EN-US"}[对]{style="font-family:宋体"}[MIB]{lang="EN-US"}[节点的访问权限，还要求团体名]{style="font-family:宋体"}[/]{lang="EN-US"}[用户名所绑定的用户角色具有执行相应操作的权限，而]{style="font-family:宋体"}[VACM]{lang="EN-US"}[方式只需通过控制]{style="font-family:宋体"}[MIB]{lang="EN-US"}[节点的访问权限即可，所以推荐使用]{style="font-family:宋体"}[RBAC]{lang="EN-US"}[配置方式，安全性更高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_189878481}

[[VACM]{lang="EN-US"}]{#struct_0_x1400_15709_x247677732}[方式：]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_495069881}[为]{style="font-family:宋体"}[v3]{lang="EN-US"}[组]{style="font-family:宋体"}[testGroup]{lang="EN-US"}[加入一个用户]{style="font-family:宋体"}[testUser]{lang="EN-US"}[，安全级别为只认证不加密，认证协议为]{style="font-family:宋体"}[SHA-1]{lang="EN-US"}[，认证密码明文为]{style="font-family:宋体"}[123456TESTplat&!]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_1733479953}

[\[Sysname\] snmp-agent group v3 testGroup authentication]{lang="EN-US"}

[\[Sysname\] snmp-agent usm-user v3 testUser testGroup simple authentication-mode sha 123456TESTplat&!]{lang="EN-US"}

[[在]{style="font-family:宋体"}[NMS]{lang="EN-US"}]{#struct_0_x1400_15709_x1072872240}[上将版本号设置为]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[，并将用户名填写为]{style="font-family:宋体"}[testUser]{lang="EN-US"}[，认证协议设置为]{style="font-family:宋体"}[SHA-1]{lang="EN-US"}[，认证密码填写为]{style="font-family:宋体"}[123456TESTplat&!]{lang="EN-US"}[，建立连接，就可以对设备上缺省视图内的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[对象进行访问了。]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_1572884795}[为]{style="font-family:宋体"}[v3]{lang="EN-US"}[组]{style="font-family:宋体"}[testGroup]{lang="EN-US"}[加入一个用户]{style="font-family:宋体"}[testUser]{lang="EN-US"}[，安全级别为认证和加密，认证协议为]{style="font-family:宋体"}[SHA-1]{lang="EN-US"}[、加密协议为]{style="font-family:宋体"}[AES]{lang="EN-US"}[，认证密码明文为]{style="font-family:宋体"}[123456TESTauth&!]{lang="EN-US"}[，加密密码明文为]{style="font-family:宋体"}[123456TESTencr&!]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_x352778637}

[\[Sysname\] snmp-agent group v3 testGroup privacy]{lang="EN-US"}

[\[Sysname\] snmp-agent usm-user v3 testUser testGroup simple authentication-mode sha 123456TESTauth&! privacy-mode aes128 123456TESTencr&!]{lang="EN-US"}

[[在]{style="font-family:宋体"}[NMS]{lang="EN-US"}]{#struct_0_x1400_15709_81303431}[上将版本号设置为]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[，并将用户名填写为]{style="font-family:宋体"}[testUser]{lang="EN-US"}[，认证协议设置为]{style="font-family:宋体"}[SHA-1]{lang="EN-US"}[，认证密码填写为]{style="font-family:宋体"}[123456TESTauth&!]{lang="EN-US"}[，加密协议设置为]{style="font-family:宋体"}[AES]{lang="EN-US"}[，加密密码填写为]{style="font-family:宋体"}[123456TESTencr&!]{lang="EN-US"}[，建立连接，就可以对设备上缺省视图内的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[对象进行访问了。]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_839678659}[为]{style="font-family:宋体"}[v3]{lang="EN-US"}[组]{style="font-family:宋体"}[testGroup]{lang="EN-US"}[加入一个与]{style="font-family:宋体"}[IP]{lang="EN-US"}[为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[的远端]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体引擎相关联的]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户]{style="font-family:宋体"}[remoteUser]{lang="EN-US"}[，安全级别为认证和加密，认证协议为]{style="font-family:宋体"}[SHA-1]{lang="EN-US"}[、加密协议为]{style="font-family:宋体"}[AES]{lang="EN-US"}[，认证密码明文为]{style="font-family:宋体"}[123456TESTauth&!]{lang="EN-US"}[，加密密码明文为]{style="font-family:宋体"}[123456TESTencr&!]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_x580691104}

[\[Sysname\] snmp-agent remote 10.1.1.1 engineid 123456789A]{lang="EN-US"}

[\[Sysname\] snmp-agent group v3 testGroup privacy]{lang="EN-US"}

[\[Sysname\] snmp-agent usm-user v3 remoteUser testGroup remote 10.1.1.1 simple authentication-mode sha 123456TESTauth&! privacy-mode aes128 123456TESTencr&!]{lang="EN-US"}

[[RBAC]{lang="EN-US"}]{#struct_0_x1400_15709_38701406}[方式：]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_x1622989559}[创建一个新的]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户]{style="font-family:宋体"}[testUser]{lang="EN-US"}[，角色为]{style="font-family:宋体"}[network-operator]{lang="EN-US"}[，安全级别为只认证不加密，认证协议为]{style="font-family:宋体"}[SHA-1]{lang="EN-US"}[，认证密码明文为]{style="font-family:宋体"}[123456TESTplat&!]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_1650834035}

[\[Sysname\] snmp-agent usm-user v3 testUser user-role network-operator simple authentication-mode sha 123456TESTplat&!]{lang="EN-US"}

[[在]{style="font-family:宋体"}[NMS]{lang="EN-US"}]{#struct_0_x1400_15709_1737642399}[上将版本号设置为]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[，并将用户名填写为]{style="font-family:宋体"}[testUser]{lang="EN-US"}[，认证协议设置为]{style="font-family:宋体"}[SHA-1]{lang="EN-US"}[，认证密码填写为]{style="font-family:宋体"}[123456TESTplat&!]{lang="EN-US"}[，建立连接，就可以对设备上所有]{style="font-family:宋体"}[MIB]{lang="EN-US"}[对象进行只读操作。]{style="font-family:宋体"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1733545489}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **snmp-agent** **usm-user**]{lang="EN-US"}]{#struct_0_x1400_15709_887082360}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **group**]{lang="EN-US"}]{#struct_0_x1400_15709_1987691571}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **calculate-password**]{lang="EN-US"}]{#struct_0_x1400_15709_x768349244}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **remote**]{lang="EN-US"}]{#struct_0_x1400_15709_39422302}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **usm-user** **v3** **user-role**]{lang="EN-US"}]{#struct_0_x1400_15709_x853527595}

::: {#1257770587 .myid}
[]{#_Toc404796968}[]{#struct_0_x1400_15709_x1759329738}[]{#_Toc359338927}

**SNMP \-- SNMP配置命令 \-- snmp-agent usm-user v3 user-role**

------------------------------------------------------------------------

[**[snmp-agent]{lang="EN-US"}**[ **usm-user** **v3 user-role**]{lang="EN-US"}]{#struct_0_x1400_15709_1408873321}[命令用来为通过]{style="font-family:宋体"}[RBAC]{lang="EN-US"}[方式创建的]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户添加角色。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **usm-user** **user-role**]{lang="EN-US"}]{#struct_0_x1400_15709_x199709111}[命令用来为]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户删除角色。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_x135328554}

[**[snmp-agent]{lang="EN-US"}**[ **usm-user** **v3** *user-name* **user-role** *role-name*]{lang="EN-US"}]{#struct_0_x1400_15709_372279055}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **usm-user** **v3** *user-name* **user-role** *role-name*]{lang="EN-US"}]{#struct_0_x1400_15709_387984259}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1400_15709_646386762}

[[设备上没有配置通过]{style="font-family:宋体"}[RBAC]{lang="EN-US"}]{#struct_0_x1400_15709_1679714190}[方式创建的]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1400_15709_39356766}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1400_15709_1386159080}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1400_15709_539576078}

[[network-admin]{lang="EN-US"}]{#struct_0_x1400_15709_x1205647288}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1400_15709_477704724}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1226270470}

[*[user-name]{lang="EN-US"}*]{#struct_0_x1400_15709_591148067}[：用户名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[user-role ]{lang="EN-US"}***[role-name]{lang="EN-US"}*]{#struct_0_x1400_15709_1466299562}[：该用户对应的角色名称**，**]{style="font-family:宋体"}*[role-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1400_15709_287253459}

[[一个]{style="font-family:宋体"}[RBAC]{lang="EN-US"}]{#struct_0_x1400_15709_280361740}[方式配置的]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户可配置多个用户角色。用户可以通过本命令来为通过]{style="font-family:宋体"}[RBAC]{lang="EN-US"}[方式创建的]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户添加与删除角色，最多可以配置]{style="font-family:宋体"}[64]{lang="EN-US"}[个有效的用户角色且至少保留一个用户角色。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1400_15709_1368487292}

[[\# ]{lang="EN-US"}]{#struct_0_x1400_15709_1179288460}[已创建]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[用户]{style="font-family:宋体"}[testUser]{lang="EN-US"}[拥有]{style="font-family:宋体"}[network-operato]{lang="EN-US"}[用户角色，现为用户]{style="font-family:宋体"}[testUser]{lang="EN-US"}[添加]{style="font-family:宋体"}[network-admin]{lang="EN-US"}[用户角色。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1400_15709_38898021}

[\[Sysname\] snmp-agent usm-user v3 testUser user-role network-admin]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1400_15709_305495605}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent usm-user v]{lang="EN-US"}**]{#struct_0_x1400_15709_1526357963}**[3]{lang="EN-US"}**

[ ]{lang="EN-US"}
:::
