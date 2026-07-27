<!-- CMD-INDEX
  allocate context                    | MDC视图            | L29
  allocate interface                  | Context视图        | L89
  allocate vlan                       | Context视图        | L157
  blade-controller-team               | 系统视图             | L231
  capability object-policy-rule maximum | Context视图        | L287
  capability session maximum          | Context视图        | L345
  capability session rate             | Context视图        | L401
  capability throughput               | Context视图        | L457
  context                             | 系统视图             | L519
  context start                       | Context视图        | L591
  description                         | Context视图        | L641
  display blade-controller-team       | 任意视图             | L685
  display context                     | 任意视图             | L803
  display context interface           | 任意视图             | L893
  display context resource            | 任意视图             | L953
  display context vlan                | 任意视图             | L1157
  join mdc                            | Context视图        | L1229
  limit-resource cpu                  | Context视图        | L1287
  limit-resource disk                 |                  | L1333
  limit-resource memory               |                  | L1431
  location blade-controller           |                  | L1527
  location blade-controller-team (Context view) | Context视图        | L1669
  location blade-controller-team (MDC view) | MDC视图            | L1733
  reset blade-controller-team         | 用户视图             | L1801
  switchto context                    | 系统视图             | L1861
-->

**Context \-- Context命令 \-- allocate context**

------------------------------------------------------------------------

![说明](Context命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[allocate context**]命令用来批量指定Context所属的MDC。

**[undo allocate context**]命令用来将Context的所属MDC恢复为缺省MDC。

【命令】

**[allocate** **context** *start-context-id* **to** *end-context-id*]

**[undo allocate** **context** *start-context-id* **to** *end-context-id*]

【缺省情况】

Context属于缺省MDC。

【视图】

MDC视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[start-context-id*]：起始Context的ID。该Context必须是已创建、未启动的Context。

*[end-context-id*]：终止Context的ID。该Context必须是已创建、未启动的Context，且*end-context-id*必须大于等于*start-context-id*。

【使用指导】

·MDC视图下的**allocate context**命令与Context视图下的**join mdc**命令功能相同，都是为Context设置归属MDC。**allocate context**可以为Context批量设置归属MDC，**join mdc**是单个设置归属MDC。

·执行**allcoate context**命令设置归属MDC时，系统会逐个设置。如果某个Context配置失败，则命令会终止执行，该Context之前的Context会加入当前MDC，该Context及其后的Context不会加入当前MDC。

【举例】

\# 指定ID为2到80的Context属于名称为cnt2的MDC。

\<Sysname\> system-view

Sysname mdc cnt2

Sysname-mdc-2-cnt2 allocate context 2 to 80

【相关命令】

·**join mdc**

**Context \-- Context命令 \-- allocate interface**

------------------------------------------------------------------------

**[allocate interface**]命令用来为Context分配接口。

**[undo allocate interface**]命令用来将接口从Context中删除。

【命令】

**[allocate interface** [ *interface-type interface-number* }&\<1-24\> [ **share** ]]

**[undo allocate interface** { *interface-type interface-number* }&\<1-24\>]

**[allocate interface ***interface-type*]*interface-number1* **to** *interface-type interface-number2 * **share** ]

**[undo allocate interface ***interface-type*]*interface-number1* **to** *interface-type interface-number2*

【缺省情况】

设备上的所有接口都属于缺省Context，不属于任何非缺省Context。（集中式防火墙/分布式防火墙/防火墙IRF）

接口不属于任何Context。（防火墙插卡）

【视图】

Context视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

 *interface-type interface-number* }&\<1-24\>：表示给Context分配非连续的接口。*interface-type interface-number*表示接口类型和编号，&\<1-24\>表示前面的参数最多可以输入24次。

*[interface-type*]*interface-number1* **to** *interface-type interface-number2*：表示给Context分配一组连续的接口。其中，*interface-type*表示接口类型，*interface-number1*表示起始接口的编号，*interface-number2*表示结束接口的编号。起始接口和结束接口的类型必须相同，并且处于同一接口板上，否则将配置失败。

**[share**]：表示接口是否共享。不指定该参数表示独占。防火墙插卡上不支持该参数。

【使用指导】

物理接口和逻辑接口均可以独占或共享方式分配给某个Context。

(1)包装防火墙/集中式防火墙IRF

·独占方式分配（不带**share**参数）。使用该方式分配的接口仅归该Context所有、使用。用户登录该Context后，能查看到该接口，并执行接口支持的所有命令。

·共享方式分配（带**share**参数）。使用该方式分配的接口归多个Context所有、使用。在缺省Context内仍然存在该接口，可执行接口支持的所有命令；在分配给的非缺省Context内，会新建同名接口，用户登录这些Context后，能查看到该接口，但只能执行**shutdown**、**description**、以及网络/安全相关的命令。

(2)插卡防火墙

同一接口只能分配给一个Context使用。分配后的接口仍然在Context所属的MDC内，但接口下的安全业务会被清除。请登录Context来配置该接口下的安全业务，接口下的其它命令请在Context所属的MDC下配置。

【举例】

\# 将接口Ethernet1/1和Ethernet1/3以共享的方式分配给context sub1。

\<Sysname\> system-view

Sysname context sub1

Sysname-context-2-sub1 allocate interface ethernet 1/1 ethernet 1/3 share

The interfaces will be shared by contexts. Continue? Y/N:y{.TerminalDisplayChar}

**Context \-- Context命令 \-- allocate vlan**

------------------------------------------------------------------------

![说明](Context命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[allocate vlan**]命令用来为Context分配VLAN**。**

**[undo allocate vlan**]命令用来取消为Context分配的VLAN。

【命令】

**[allocate** **vlan** *vlan-id*&\<1-24\>]

**[undo allocate vlan** *vlan-id*&\<1-24\>]

**[allocate vlan*** vlan-id1* **to** *vlan-id2*]

**[undo allocate vlan ***vlan-id1* **to** *vlan-id2*]

【缺省情况】

没有为Context分配VLAN。

【视图】

Context视图

【缺省用户角色】

network-admin

context-admin

【参数】

*[vlan-id*&\<1-24\>]**：**表示给Context分配非连续的VLAN。*vlan-id*表示VLAN的编号，&\<1-24\>表示前面的参数最多可以输入24次。

*[vlan-id1*** to ***vlan-id2*]**：**表示给Context分配一组连续的VLAN。其中，*vlan-id1*表示起始VLAN的编号，*vlan-id2*表示结束VLAN的编号。

【使用指导】

(1)包装防火墙

创建Context时，通过**vlan-unshared**参数可选择是否和其它Context共享VLAN：

·如果选择和其它Context共享VLAN，则设备上所有Context共享VLAN 1～VLAN 4094。这些VLAN通过**allocate** **vlan**命令分配。如果某VLAN已经分配给某Context，则不能再分配给其它Context。

·如果选择不和其它Context共享VLAN，请登录该Context，并使用**vlan**命令创建VLAN 1～VLAN 4094。Context各自使用和管理VLAN，互不干扰。

(2)防火墙插卡

设备上所有Context共享VLAN 1～VLAN 4094。这些VLAN通过**allocate** **vlan**命令分配。如果某VLAN已经分配给某Context了，则不能再分配给其它Context。

【举例】

\# 将VLAN100分配给context sub1。

\<Sysname\> system-view

Sysname context sub1

Sysname-context-2-sub1 allocate vlan 100

The VLAN will be allocated to context sub1. Continue? Y/N:y

【相关命令】

·**display context vlan**

**Context \-- Context命令 \-- blade-controller-team**

------------------------------------------------------------------------

![说明](Context命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[blade-controller-team**]命令用来创建安全引擎组并进入该安全引擎组视图。

**[undo** **blade-controller-team**]命令用来删除指定的安全引擎组。

【命令】

**[blade-controller-team** *blade-controller-team-name* [ **id** *blade-controller-team-id* ]]

**[undo blade-controller-team**[ { *blade-controller-team-name \|* **id** *blade-controller-team-id* }]]

【缺省情况】

设备上有一个安全引擎组，名字为Default，编号为1。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[blade-controller-team-name*]：安全引擎组的名称，为1～31个字符的字符串，区分大小写。

**[id*** blade-controller-team-id*]：安全引擎组的编号，取值范围为2～256。不指定该参数时，系统会自动分配一个当前空闲的最小编号。

【使用指导】

·缺省安全引擎组不能创建、删除，且不能进入缺省安全引擎组的视图。

·当删除安全引擎组时，如果该组中有进驻的安全引擎，请先用**undo locationblade-controller**命令取消进驻后，再删除该组。

【举例】

\# 创建名为abc的安全引擎组。

\<sysname\> system-view

sysname blade-controller-team abc

sysname-blade-controller-team-3-abc

**Context \-- Context命令 \-- capability object-policy-rule maximum**

------------------------------------------------------------------------

![说明](Context命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[capability object-policy-rule maximum**]命令用来设置Context的对象策略规则总数限制。

**[undo capability object-policy-rule maximum**]命令用来恢复缺省情况。

【命令】

**[capability object-policy-rule maximum ***max-value*]

**[undo capability object-policy-rule maximum**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

Context视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[max-value*]：表示Context内可配置的对象策略规则总数的最大值。

【使用指导】

配置本命令后，该Context已进驻的每个安全引擎上都将获得相同的对象策略规则总数限制。

当规则总数达到最大值时，不能新增规则。

如果当前设置的最大值比之前设置的最大值小，则可能存在最大值比当前存在的规则总数小的情况，但配置仍会成功，多出的规则不会删除，后续不能新增规则。

【举例】

\#{.apple-converted-space}配置Context的安全策略规则数最多为1000条。

\<Sysname\> system-view

Sysname context cnt2

Sysname-context-2-cnt2 capability object-policy-rule maximum 1000

【相关命令】

·**display** **object-policy ip**（安全命令参考/对象策略）

**Context \-- Context命令 \-- capability session maximum**

------------------------------------------------------------------------

![说明](Context命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[capability session maximum**]命令用来设置Context的会话并发数限制。

**[undo capability session maximum**]命令用来恢复缺省情况。

【命令】

**[capability session maximum*** max-number*]

**[undo capability session maximum**]

【缺省情况】

未对该Context允许的会话并发数进行限制，由该Context上各安全引擎当前的内存能力决定。

【视图】

Context视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[max-number*]：允许同时存在的最大会话数目，取值范围为1～4294967295。

【使用指导】

配置本命令后，该Context己进驻的每个安全引擎都将获得相同的会话并发数限制。当安全引擎上的会话总数达到最大数目后，该安全引擎上将不允许新建会话；如果本次设置的数值小于当前安全引擎上的会话总数，则配置可以成功，但不再允许新建会话，且已经创建的会话不会被删除，直到已建立的会话通过老化机制使得会话总数低于配置的最大值后，系统才允许新建会话。

【举例】

\# 配置Context cnt2上的会话并发数为1000000。

\<Sysname\> system-view

Sysname context cnt2

Sysname-context-2-cnt2 capability session maximum 1000000

【相关命令】

·**context**

·**display session statistics**（安全命令参考/会话管理）

**Context \-- Context命令 \-- capability session rate**

------------------------------------------------------------------------

!(Context命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[capability session rate**]命令用来设置Context的会话新建速率限制。

**[undo capability session rate**]命令用来恢复缺省情况。

【命令】

**[capability session rate** *max-value*]

**[undo capablility session rate**]

【缺省情况】

未对该Context允许的会话新建速率进行限制，由该Context上各安全引擎当前的内存能力决定。

【视图】

Context视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[max-value*]：允许的会话新建速率最大值，单位为每秒会话个数。

【使用指导】

配置本命令后，该Context己进驻的每个安全引擎都将获得相同的会话新建速率限制。当安全引擎上的会话新建速率达到最大值后，该安全引擎上将不允许新建会话。

【举例】

\# 配置Context cnt2上的会话新建速率最大值为每秒20000个会话数。

\<Sysname\> system-view

Sysname context cnt2

Sysname-context-2-cnt2 capability session rate 20000

【相关命令】

·**context**

·**display session statistics**（安全命令参考/会话管理）

**Context \-- Context命令 \-- capability throughput**

------------------------------------------------------------------------

![说明](Context命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[capability throughput**]命令用来设置Context的吞吐量限制。

**[undo capability throughput**]命令用来恢复缺省情况。

【命令】

**[capability throughput **[\| **pps**]} *value*

**[undo capability throughput**]

【缺省情况】]

各Context不做吞吐量限制，按实际能力转发。

【视图】

Context视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[kbps**]：表示吞吐量按每秒千比特计算。

**[pps**]：表示吞吐量按每秒报文数计算。

*[value*]：表示吞吐量限制值，取值范围为1000～100000000。

【使用指导】

配置本命令后，该Context已进驻的每个安全引擎上都将获得相同的吞吐量限制。

【举例】

\#{.apple-converted-space}配置Context的吞吐量为100Mbps。

\<Sysname\> system-view

Sysname context cnt2

Sysname-context-2-cnt2 capability throughput kbps 100000

\#{.apple-converted-space}配置Context的吞吐量为10000pps。

\<Sysname\> system-view

Sysname context cnt2

Sysname-context-2-cnt2 capability throughput pps 10000

**Context \-- Context命令 \-- context**

------------------------------------------------------------------------

**[context**]命令用来创建Context并进入Context视图。如果Context已创建，则直接进入Context视图。

**[undo context**]命令用来删除Context。

【命令】

包装防火墙：

**[context **]*context-name*****\****[id ***context-id *]**\**[vlan-unshared****]

**[undo context **]*context-name*

防火墙插卡：

**[context **]*context-name*****\****[id ***context-id *]

**[undo context **]*context-name*

【缺省情况】

设备上存在缺省Context，名称为Admin，编号为1。（包装防火墙）

设备上没有Context。（防火墙插卡）

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[context-name*]：Context的名称，为1～15个字符的字符串，区分大小写。

*[context-id*]：Context的编号，取值范围为1～65279。不指定该参数时，系统会自动给Context分配一个当前空闲的最小编号。

**[vlan-unshared**]：不和其它Context共享VLAN。不指定该参数时，表示和其它Context共享VLAN。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（包装防火墙）

【使用指导】

创建Context时，通过**vlan-unshared**参数可选择是否和其它Context共享VLAN：

·如果选择和其它Context共享VLAN，则设备上所有Context共享VLAN 1～VLAN 4094。这些VLAN通过**allocate** **vlan**命令分配。如果某VLAN已经分配给某Context了，则不能再分配给其它Context。

·如果选择不和其它Context共享VLAN，请登录该Context，并使用**vlan**命令创建VLAN 1～VLAN 4094。Context各自使用和管理VLAN，互不干扰。

【举例】

\# 创建一个名称为test的Context。

\<Sysname\> system-view

Sysname context test

Sysname-context-2-test

\# 创建一个名称为test，ID为2的Context。

\<Sysname\> system-view

Sysname context test id 2

Sysname-context-2-test

**Context \-- Context命令 \-- context start**

------------------------------------------------------------------------

**[context start**]命令用来启动Context。

**[undo context start**]命令用来停止该Context。

【命令】

**[context start**]

**[undo context start**]

【视图】

Context视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

Context创建后需要执行**contextstart**命令，才能完成新Context的初始化，相当于上电启动。启动后，用户可以登录到该Context执行配置。

请先配置Context所属的MDC，再登录该MDC，在这个MDC下使用该命令启动Context。例如，Context cnt2属于MDC test，则必须先通过**switchto mdc test**命令或者Telnet等方式登录到MDC test，才可以启动Context cnt2。

需要注意的是：

·停止Context会导致该Context的业务中断，以及登录该Context的用户自动退出，请谨慎使用。

·停止Context前请保存Context的配置，否则，可能导致Context的当前配置丢失。

【举例】

\# 启动Context cnt2。

\<Sysname\> system-view

Sysname context cnt2

Sysname-context-2-cnt2 context start

It will take some time to start the context\...

Context started successfully.

**Context \-- Context命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来配置Context的描述信息。

【命令】

**[description **]*text*

**[undo description**]

【缺省情况】

缺省Context描述信息为DefaultContext。非缺省Context没有配置描述信息。

【视图】

Context视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：Context的描述信息，为1～255个字符的字符串，区分大小写。

【使用指导】

当设备上配置的Context较多时，用户可以为Context配置特定的描述信息，以便记忆和管理Context。

【举例】

\# 将Context的描述信息配置为test。

\<Sysname\> system-view

Sysname context cnt2

Sysname-context-2-cnt2 description test

**Context \-- Context命令 \-- display blade-controller-team**

------------------------------------------------------------------------

![说明](Context命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display blade-controller-team**]命令用来显示安全引擎组的信息。

【命令】

**[display blade-controller-team**[ [ *blade-controller-team-name* \| **id** *blade-controller-team-id* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[blade-controller-team-name*]：安全引擎组的名称，为1～31个字符的字符串，区分大小写。

**[id*** blade-controller-team-id*]：安全引擎组的编号，取值范围为1～256。

【使用指导】

不指定任何参数时，显示所有安全引擎组的信息。

【举例】

\# 显示安全引擎组的信息。

\<Sysname\> display blade-controller-team

ID          Name

1           abc

2           fff

\# 显示名称为abc的安全引擎组的信息。（集中式设备[/分布式设备－独立运行模式]/集中式IRF设备）

\<Sysname\> display blade-controller-team abc

ID: 2        Name: abc

Slot    CPU    Status

1       1      Absent

\* 1       1      Normal

\*  : Primary blade controller of the team.

\# 显示名称为abc的安全引擎组的信息。（分布式设备－IRF模式）

\<Sysname\> display blade-controller-team abc

ID: 2        Name: abc

Chassis    Slot    CPU    Status

1          1       1      Absent

\* 1          7       1      Normal

\*  : Primary blade controller of the team.

表1-1 display blade-controller-team命令显示信息描述表

字段

描述

ID

安全引擎组的编号

Name

安全引擎组的名称

Chassis

安全引擎所在设备的成员编号（分布式设备－IRF模式）

Slot

安全引擎所在的槽位号

CPU

安全引擎的CPU号

Status

安全引擎的状态：

·Absent：表示该位置没有插入安全引擎

·Fault：表示该节点的单板不能正常启动

·Normal：表示该位置的安全引擎运行正常

\*  : Primary blade controller of the team.

\*表示安全引擎组的主安全引擎

**Context \-- Context命令 \-- display context**

------------------------------------------------------------------------

**[display context**]命令用来显示已经创建的Context的信息，包括编号和状态等。

【命令】

**[display context**  **name** *context-name* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name**]*context-name*：Context的名字，为1～15个字符的字符串，区分大小写。

【使用指导】

(1)包装防火墙

在缺省Context中，可使用**name*** context-name*参数查看指定Context的信息。不指定**name*** context-name*参数时，则显示设备上创建的所有Context的信息。

(2)防火墙插卡

·在缺省MDC下，可使用**name*** context-name*参数查看指定Context的信息；不指定**name*** context-name*参数时，则显示设备上创建的所有Context的信息。

·非缺省MDC下，不能指定**name ***context-name*参数，只能显示属于该MDC的所有Context的信息。

【举例】

\# 显示已经创建的Context的信息。

\<Sysname\> display context

ID     Name          Status           BelongTo        Description

1      cnt1          active           Admin           context1

2      cnt2          inactive         MDC3            context2

3      cnt3          inactive         MDC2            context3

表1-2 display context命令显示信息描述表

字段

描述

ID

Context的编号

Name

Context的名称

Status

Context的状态：

·active：表示Context正常运行

·inactive：表示Context处于未启动状态

·starting：表示Context正在启动

·updating：表示正在将Context加入安全引擎组

·stopping：表示Context正在停止

Belongto

Context所属的MDC的名称（防火墙插卡）

Description

Context描述信息

**Context \-- Context命令 \-- display context interface**

------------------------------------------------------------------------

**[display context interface**]命令用来显示Context的接口列表。

【命令】

**[display context ** **name** *context-name* ] **interface**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name*** context-name*]：Context的名称，为1～15个字符的字符串，区分大小写。

【使用指导】

(1)包装防火墙

在缺省Context中，可使用**name*** context-name*参数查看指定Context的接口列表；不指定**name*** context-name*参数时，则显示设备上创建的所有Context的接口列表。

(2)防火墙插卡

使用该命令：

·在缺省MDC下，可使用**name*** context-name*参数查看指定Context的接口列表；不指定**name*** context-name*参数时，则显示设备上创建的所有Context的接口列表。

·在非缺省MDC下，不能指定**name ***context-name*参数，只能显示属于该MDC的所有Context的接口列表。

【举例】

\# 显示所有Context的接口列表。

\<Sysname\> display context interface

Context stub1\'s interfaces:

  GigabitEthernet0/1/4

Context stub2\'s interfaces:

  FortyGigE0/1/8

【相关命令】

·**allocate interface**

**Context \-- Context命令 \-- display context resource**

------------------------------------------------------------------------

**[display context resource**]命令用来显示Context对CPU/磁盘/内存资源的使用情况。

【命令】

集中式设备：

**[display context **] **name** *context-name*  **resource**[ [ **cpu** \| **disk** \| **memory**]]

分布式设备－独立运行模式/集中式IRF设备：

**[display context **] **name** *context-name*  **resource**[ [ **cpu** \| **disk** \| **memory**]  **slot** *slot-number* **cpu** *cpu-number* ]

分布式设备－IRF模式：

**[display context **] **name** *context-name*  **resource **[[ **cpu** \| **disk** \| **memory** ]  **chassis** *chassis-number* **slot** *slot-number* **cpu** *cpu-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name**] *context-name*：显示指定Context对CPU/磁盘[/内存资源的使用情况。]*context-name*表示Context的名字，为1～15个字符的字符串，区分大小写。不指定该参数时，显示当前MDC下所有Context对CPU/磁盘[/内存资源的使用情况。]

**[cpu**]：显示Context对CPU的使用情况。

**[disk**]：显示Context对磁盘的使用情况。

**[memory**]：显示Context对内存的使用情况。

**[slot**] *slot-number* **cpu** *cpu-number*：显示Context对指定安全引擎的CPU/磁盘/内存资源的使用情况，*slot-number*表示安全引擎所在的槽位号，*cpu-number*表示安全引擎的CPU的编号。不指定该参数时，显示Context对所有安全引擎的CPU/磁盘/内存资源的使用情况。（分布式设备－独立运行模式）

**[slot**] *slot-number* **cpu** *cpu-number*：显示Context对指定成员设备上安全引擎的CPU/磁盘/内存资源的使用情况，*slot-number*表示设备在IRF中的成员编号，*cpu-number*表示安全引擎的CPU的编号。不指定该参数时，显示Context对所有安全引擎的CPU/磁盘/内存资源的使用情况。（集中式IRF设备）

**[chassis**] *chassis-number* **slot** *slot-number* **cpu** *cpu-number*：显示Context对指定成员设备安全引擎的CPU/磁盘/内存资源的使用情况，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示安全引擎所在的槽位号，*cpu-number*表示安全引擎的CPU的编号。不指定该参数时，显示Context对IRF中所有安全引擎的CPU/磁盘/内存资源的使用情况。（分布式设备－IRF模式）

【举例】

\# 显示所有Context对CPU/磁盘/内存资源的使用情况。（集中式设备）

\<Sysname\> display context resource

Memory usage:

Slot 0 CPU 0

Used 120.7MB, Free 375.4MB, Total 496.1MB

  ID   Name        Quota(MB)    Used(MB)    Free(MB)

  1    Admin       496.1        94.9        375.4

  2    cnt2        496.1        25.8        375.4

CPU usage:

Slot 0 CPU 0

  ID   Name        Weight       Usage(%)

  1    Admin       10           3

  2    cnt2        10           0

Disk usage:

Slot 0 CPU 0

flash: Used 0.3MB, Free 462.3MB, Total 462.6MB

  ID   Name        Quota(MB)    Used(MB)    Free(MB)

  1    Admin       416.3        0.3         416

  2    cnt2        46.3         0.0         46.3

\# 显示Context对所有安全引擎上CPU资源的使用情况。（分布式设备/集中式IRF设备）

\<Sysname\> display context resource cpu

CPU usage:

Slot 2 CPU 1:

  ID   Name        Weight       Usage(%)

  1    cnt1        10           24

  2    cnt2        10           0

Slot 3 CPU 1:

  ID   Name        Weight       Usage(%)

  1    cnt3        10           0

  2    cnt4        10           0

\# 显示Context对所有安全引擎上CPU资源的使用情况。（分布式设备－IRF模式）

\<Sysname\> display context resource cpu

CPU usage:

Chassis 1 slot 2 CPU 1:

  ID   Name        Weight       Usage(%)

  1    cnt1        10           24

  2    cnt2        10           0

Chassis 1 slot 3 CPU 1:

  ID   Name        Weight       Usage(%)

  1    cnt3        10           0

  2    cnt4        10           0

表1-3 display context resource命令显示信息描述表

字段

描述

Memory

表示下面显示的是内存的使用情况

CPU

表示下面显示的是CPU的使用情况

Disk

表示下面显示的是磁盘的使用情况

Slot 0 CPU 0

表示Context对指定安全引擎上资源的使用情况（集中式设备）

Slot 2 CPU 1

表示Context对指定安全引擎上资源的使用情况（分布式设备－独立运行模式）

Slot 2 CPU 1

表示Context对指定安全引擎上资源的使用情况（集中式IRF设备）

Chassis 1 slot 2 CPU 1

表示Context对指定安全引擎上资源的使用情况（分布式设备－IRF模式）

Used 238.1MB, Free 249.3MB, Total 487.4MB

内存的使用情况，Used表示内存已使用空间的大小（单位为MB），Free表示当前空闲内存的大小（单位为MB），Total表示整个内存大小（单位为MB）。如果Context没有启动，则Used会显示为0

Cfa0: Used 0MB,  Free 61MB, Total 61MB

Cfa0表示磁盘的名称，Used表示整个磁盘已使用空间的大小（单位为MB），Free表示整个磁盘当前空闲空间的大小（单位为MB），Total表示整个磁盘空间大小（单位为MB）。如果Context没有启动，则Used会显示为0

ID

Context的编号

name

Context的名字

Weight

Context使用CPU的权重值

Usage(%)

Context对CPU的实际占用率，用百分比表示

Quota(MB)

Context使用磁盘/内存的限制值，单位为MB

Used(MB)

Context当前已使用的磁盘/内存空间的大小，单位为MB

Free(MB)

Context还可以使用的磁盘/内存空间的大小，单位为MB

**Context \-- Context命令 \-- display context vlan**

------------------------------------------------------------------------

![说明](Context命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display context vlan**]命令用来显示Context的VLAN列表。

【命令】

**[display context** [ **name** *context-name*  **vlan**]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name** *context-name*]：Context的名称，为1～15个字符的字符串，区分大小写。

【使用指导】

(1)包装防火墙

在缺省Context中，可使用**name** *context-name*参数查看指定Context的VLAN列表；不指定**name** *context-name*参数时，则显示设备上创建的所有Context的VLAN列表。

(2)防火墙插卡

可使用**name** *context-name*参数查看指定Context的VLAN列表；不指定**name** *context-name*参数时，则显示所有属于当前登录MDC的Context的VLAN列表。

【举例】

\# 显示所有Context的VLAN列表。

\<Sysname\> display context vlan

Context stub1\'s VLAN(s):

Context stub2\'s VLAN(s):

  2,4094

Context stub3\'s VLAN(s):

  5,6,800-3000,3400

\# 显示Context sub1的VLAN列表。

\<Sysname\> display context name sub1 vlan

Context stub1\'s VLAN(s):

  5,6,11-23,3400

【相关命令】

·**allocate vlan**

**Context \-- Context命令 \-- join mdc**

------------------------------------------------------------------------

![说明](Context命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[join**]**mdc**命令用来配置Context所属的MDC。

**[undo join**]命令用来恢复缺省情况。

【命令】

**[join**]**mdc ***mdc-name*

**[undo join**]

【缺省情况】

Context属于缺省MDC。

【视图】

Context视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mdc-name*]：指定Context所属的MDC的名称。该Context必须是已创建、未启动的Context。

【使用指导】

MDC视图下的**allocate context**命令与Context视图下的**join mdc**命令功能相同，都是为Context设置归属MDC。**allocate context**可以批量设置归属MDC，**join mdc**是为单个Context设置归属MDC。

配置Context所属的MDC后，MDC才能对外提供安全业务。一个MDC下可以存在多个Context，一个Context只能隶属于一个MDC，使用这个MDC上的物理资源。

【举例】

\# 指定Context（名称为cnt2）归属的MDC（名称为test2）。

\<Sysname\> system-view

Sysname context cnt2

Sysname-context-2-cnt2 join mdc test2

【相关命令】

·**allocate context**

**Context \-- Context命令 \-- limit-resource cpu**

------------------------------------------------------------------------

**[limit-resource cpu**]命令用来配置Context的CPU权重。

**[undo limit-resource cpu**]命令用来恢复缺省情况。

【命令】

**[limit-resource cpu** **weight** *weight-value*]

**[undo limit-resource cpu**]

【缺省情况】

各Context的CPU权重均为10。

【视图】

Context视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[weight ***weight-value*]：表示Context在指定安全引擎上的CPU权重，取值范围为1～10。系统根据Context的权重为Context分配CPU时间。

【使用指导】

进驻到同一安全引擎的Context共享该安全引擎的CPU资源。配置本命令后，Context在己进驻的安全引擎上都将获得相同的CPU权重。

【举例】

\#配置Context的CPU权重为2。

\<Sysname\> system-view

Sysname context cnt2

Sysname-context-2-cnt2 limit-resource cpu weight 2

**Context \-- Context命令 \-- limit-resource disk**

------------------------------------------------------------------------

**[limit-resource disk**]命令用来配置Context可使用的磁盘空间上限（用百分比表示）。

**[undo limit-resource disk**]命令用来恢复缺省情况。

【命令】

集中式设备：

**[limit-resource disk ratio **]*limit-ratio*

**[undo limit-resource disk**]

分布式设备－独立运行模式/集中式IRF设备：

**[limit-resource disk slot** *slot-number* **cpu** *cpu-number* **ratio** *limit-ratio*]

**[undo limit-resource disk slot** *slot-number* **cpu** *cpu-number*]

分布式设备－IRF模式：

**[limit-resource disk chassis*** chassis-number ***slot ***slot-number*** cpu** *cpu-number* **ratio** *limit-ratio*]

**[undo limit-resource disk chassis*** chassis-number ***slot ***slot-number*** cpu** *cpu-number*]

【缺省情况】

Context可以使用物理设备上的所有空闲磁盘空间。（集中式设备）

进驻到同一安全引擎的所有Context共享该安全引擎的所有磁盘空间，每个Context可使用的磁盘空间上限为该安全引擎的空闲磁盘空间值。（分布式设备－独立运行模式/集中式IRF设备[/]分布式设备－IRF模式）

【视图】

Context视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot**] *slot-number* **cpu** *cpu-number*：表示安全引擎所在的位置，其中，*slot-number*表示安全引擎所在的槽位号，*cpu-number*表示安全引擎的CPU的编号。（分布式设备－独立运行模式）

**[slot** *slot-number* **cpu** *cpu-number*]：表示成员设备安全引擎所在的位置，其中，*slot-number*表示安全引擎所在的设备的成员编号，*cpu-number*表示安全引擎的CPU的编号。（集中式IRF设备）

**[chassis*** chassis-number ***slot ***slot-number*** cpu** *cpu-number*]：表示成员设备安全引擎所在的位置，其中，*chassis-number*表示安全引擎所在的设备的成员编号，*slot-number*表示安全引擎所在的槽位号，*cpu-number*表示安全引擎的CPU的编号。（分布式设备－IRF模式）

**[ratio **]*limit-ratio*：表示Context在设备上最多可使用的磁盘空间大小与该设备整个磁盘空间大小的百分比，取值范围为1～100。（集中式设备）

**[ratio **]*limit-ratio*：表示Context在指定安全引擎上最多可使用的磁盘空间大小与该安全引擎整个磁盘空间大小的百分比，取值范围为1～100。

【使用指导】

缺省情况下，所有的Context共享已进驻的安全引擎的所有磁盘空间。只要磁盘物理空间足够，就可以无限制使用。为了防止单个Context过多的占用磁盘而影响其它Context，特别是为防止异常情况下对磁盘的占用，可以为指定的Context配置磁盘上限。

请在Context启动后配置磁盘上限。执行**limit-resource disk**命令前，请使用**display context resource**命令查看Context当前实际已经使用的磁盘空间大小。配置值应大于Context当前实际已经使用的磁盘空间大小，否则，会导致Context申请新的磁盘空间失败，从而无法进行文件夹创建、文件拷贝和保存等操作。

如果设备上有多块磁盘，该命令对所有磁盘生效。

【举例】

\# 配置Context cnt2最多可使用设备磁盘空间的30%。（集中式设备）

\<Sysname\> system-view

Sysname context cnt2

Sysname-context-2-cnt2 limit-resource disk ratio 30

\# 配置Context cnt2最多可使用3号单板上安全引擎磁盘空间的20%。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname context cnt2

Sysname-context-2-cnt2 limit-resource disk slot 3 cpu 1 ratio 20

\# 配置Context cnt2最多可使用2号成员设备上安全引擎磁盘空间的30%。（集中式IRF设备）

\<Sysname\> system-view

Sysname context cnt2

Sysname-context-2-cnt2 limit-resource disk slot 2 cpu 1 ratio 30

\# 配置Context cnt2最多可使用2号成员设备3号单板上安全引擎磁盘空间的30%。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname context cnt2

Sysname-context-2-cnt2 limit-resource disk chassis 2 slot 3 cpu 1 ratio 30

**Context \-- Context命令 \-- limit-resource memory**

------------------------------------------------------------------------

**[limit-resource memory**]命令用来配置Context可使用的内存空间上限（用百分比表示）。

**[undo limit-resource memory**]命令用来恢复到缺省情况。

【命令】

集中式设备：

**[limit-resource **]**memory ratio***limit-ratio*

**[undo limit-resource **]**memory**

分布式设备－独立运行模式/集中式IRF设备：

**[limit-resource **]**memory** **slot** *slot-number* **cpu** *cpu-number* **ratio** *limit-ratio*

**[undo limit-resource **]**memory** **slot** *slot-number* **cpu** *cpu-number*

分布式设备－IRF模式：

**[limit-resource **]**memory** **chassis** *chassis-number* **slot** *slot-number* **cpu** *cpu-number* **ratio** *limit-ratio*

**[undo limit-resource **]**memory** **chassis** *chassis-number* **slot** *slot-number* **cpu** *cpu-number*

【缺省情况】

所有Context共享物理设备上的所有内存空间，每个Context可使用的内存空间上限为空闲内存空间值。（集中式设备）

进驻到同一安全引擎的所有Context共享该安全引擎的所有内存空间，每个Context可使用的内存空间上限为该安全引擎的空闲内存空间值。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【视图】

Context视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot**] *slot-number* **cpu** *cpu-number*：表示安全引擎所在的位置，其中，*slot-number*表示安全引擎所在的槽位号，*cpu-number*表示安全引擎的CPU的编号。（分布式设备－独立运行模式）

**[slot** *slot-number* **cpu** *cpu-number*]：表示成员设备安全引擎所在的位置，其中，*slot-number*表示设备的成员编号，*cpu-number*表示安全引擎的CPU的编号。（集中式IRF设备）

**[chassis*** chassis-number ***slot ***slot-number*** cpu** *cpu-number*]：表示成员设备安全引擎所在的位置，其中，*chassis-number*表示安全引擎所在的设备的成员编号，*slot-number*表示安全引擎所在的槽位号，*cpu-number*表示安全引擎的CPU的编号。（分布式设备－IRF模式）

**[ratio **]*limit-ratio*：表示Context在设备上最多可使用的内存大小与该设备整个内存大小的百分比，取值范围为1～100。（集中式设备）

**[ratio **]*limit-ratio*：表示Context在指定安全引擎上最多可使用的内存大小与该安全引擎整个内存大小的百分比，取值范围为1～100。

【使用指导】

缺省情况下，所有的Context共享使用已进驻的安全引擎的所有内存空间。只要物理内存足够，就可以无限制使用。为了防止单个Context过多的占用内存而影响其它Context，特别是为防止异常情况下对内存的占用，可以为指定的Context配置内存上限。

需要注意的是，请在Context启动后再配置内存上限，并且配置的上限值不应过小，以免Context内业务申请不到内存而引起功能异常。

【举例】

\# 配置Context cnt2最多可使用设备内存的30%。（集中式设备）

\<Sysname\> system-view

Sysname context cnt2

Sysname-context-2-cnt2 limit-resource memory ratio 30

\# 配置Context cnt2最多可使用1号单板安全引擎内存的30%。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname context cnt2

Sysname-context-2-cnt2 limit-resource memory slot 1 cpu 1 ratio 30

\# 配置Context cnt2最多可使用2号成员设备安全引擎内存的30%。（集中式IRF设备）

\<Sysname\> system-view

Sysname context cnt2

Sysname-context-2-cnt2 limit-resource memory slot 2 cpu 1 ratio 30

\# 配置Context cnt2最多可使用2号成员设备1号单板安全引擎内存的30%。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname context cnt2

Sysname-context-2-cnt2 limit-resource memory chassis 2 slot 1 cpu 1 ratio 30

**Context \-- Context命令 \-- location blade-controller**

------------------------------------------------------------------------

![说明](Context命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[location blade-controller**]命令用来将安全引擎加入安全引擎组。

**[undo** **location blade-controller**]命令用来恢复缺省情况。

【命令】

集中式设备/分布式设备－独立运行模式/集中式IRF设备：

**[location blade-controller slot ***slot-number* **cpu** *cpu-number*]

**[undo location blade-controller slot ***slot-number* **cpu** *cpu-number*]

分布式设备－IRF模式：

**[location blade-controller chassis*** chassis-number ***slot ***slot-number* **cpu** *cpu-number*]

**[undo location blade-controller chassis*** chassis-number ***slot ***slot-number* **cpu** *cpu-number*]

【缺省情况】

安全引擎插入时会自动加入缺省安全引擎组。

【视图】

安全引擎组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot*** slot-number*]：表示安全引擎所在的槽位号。（集中式设备[/分布式设备－独立运行模式]）

**[slot*** slot-number*]：表示安全引擎所在设备的成员编号。（集中式IRF设备）

**[chassis ***chassis-number*]：表示安全引擎所在设备的成员编号。（分布式设备－IRF模式）

**[slot*** slot-number*]：表示安全引擎所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：表示安全引擎的CPU编号。

【使用指导】

使用该命令可以：

·将一个已经在位的安全引擎加入安全引擎组，这样的命令会立即生效。

·将一个不在位的安全引擎加入安全引擎组，这样的命令会在安全引擎插入后生效。这样的配置方式称为预配置，能够帮助用户先完成配置，再进行硬件部署。使用该方式配置前，请先规划安全引擎即将插入的位置。因为，如果配置的位置误插入非安全引擎，设备会自动将该命令删除，以后插入安全引擎时，需要重新配置。

需要注意的是：

·一个安全引擎只能属于一个安全引擎组。

·当前，每个安全引擎组中可加入的安全引擎个数没有限制。

·将安全引擎从一个安全引擎组切换到另外一个安全引擎组时，防火墙插卡会自动重启。（防火墙插卡）

【举例】

\# 将安全引擎加入安全引擎组abc。（集中式设备）

\<sysname\> system-view

sysname blade-controller-team abc

Sysname-blade-controller-team-2-abc location blade-controller slot 0 cpu 1

This operation will also reboot the blade controller. Continue? [Y/N:y]

\# 将2号槽位上1号CPU的安全引擎加入安全引擎组abc。（分布式设备－独立运行模式）

\<sysname\> system-view

sysname blade-controller-team abc

Sysname-blade-controller-team-2-abc location blade-controller slot 2 cpu 1

This operation will also reboot the blade controller. Continue? [Y/N:y]

\# 将2号成员设备上1号CPU的安全引擎加入安全引擎组abc。（集中式IRF设备）

\<sysname\> system-view

sysname blade-controller-team abc

Sysname-blade-controller-team-2-abc location blade-controller slot 2 cpu 1

This operation will also reboot the blade controller. Continue? [Y/N:y]

\# 将2号成员设备2号槽位上1号CPU的安全引擎加入安全引擎组abc。（分布式设备－IRF模式）

\<sysname\> system-view

sysname blade-controller-team abc

Sysname-blade-controller-team-2-abc location blade-controller chassis 2 slot 2 cpu 1

This operation will also reboot the blade controller. Continue? [Y/N:y]

\# 将3号槽位上1号CPU的安全引擎（不在位）加入安全引擎组abc。（分布式设备－独立运行模式）

\<sysname\> system-view

sysname blade-controller-team abc

Sysname-blade-controller-team-2-abc location blade-controller slot 3 cpu 1

Operation successed, but the blade controller is absent.

\# 将3号成员设备上1号CPU的安全引擎（不在位）加入安全引擎组abc。（集中式IRF设备）

\<sysname\> system-view

sysname blade-controller-team abc

Sysname-blade-controller-team-2-abc location blade-controller slot 3 cpu 1

Operation successed, but the blade controller is absent.

\# 将2号成员设备3号槽位上1号CPU的安全引擎（不在位）加入安全引擎组abc。（分布式设备－IRF模式）

\<sysname\> system-view

sysname blade-controller-team abc

Sysname-blade-controller-team-2-abc location blade-controller chassis 2 slot 3 cpu 1

Operation successed, but the blade controller is absent.

**Context \-- Context命令 \-- location blade-controller-team (Context view)**

------------------------------------------------------------------------

**[location**]** blade-controller-team**命令用于使Context进驻对应的安全引擎组。

**[undo location**]** blade-controller-team**命令用于将Context从安全引擎组中移除。

【命令】

**[location blade-controller-team**]* team-id*

**[undo location blade-controller-team**]* team-id*

【缺省情况】

缺省Context进驻了所有安全引擎组，非缺省Context没有进驻任何安全引擎组。（包装防火墙）

Context未进驻任何安全引擎组。（防火墙插卡）

【视图】

Context视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[team-id*]：当前已经创建的安全引擎组的编号。

【使用指导】

如果没有进驻安全引擎**，**即使Context已经启动，Context也没有实际运行的环境，无法运行业务。

Context进驻安全引擎组后，才能使用安全引擎组中安全引擎上的资源，包括CPU、磁盘和内存。

Context和安全引擎组的关系如下：

·一个Context只能进驻一个安全引擎组。如果该Context已经进驻一个安全引擎组，请先执行**undo location blade-controller-team**命令退出已进驻的安全引擎组，再配置**location blade-controller-team**命令，进驻其它安全引擎组。

·在不同的Context视图下执行该命令可以使多个Context进驻同一个安全引擎组。最多可以有256个Context进驻到同一个安全引擎组，安全引擎组和Context是一对多的关系。

·安全引擎组中加入新的安全引擎后，安全引擎组上已进驻的Context会自动进驻到新加入的安全引擎上，不需要再次配置。

【举例】

\# 将Context cnt2进驻到安全引擎组2。

\<Sysname\> system-view

Sysname context cnt2

Sysname-context-2-cnt2 location blade-controller-team 2

【相关命令】

·**blade-controller-team**

·**location blade-controller-team** (MDC view)

**Context \-- Context命令 \-- location blade-controller-team (MDC view)**

------------------------------------------------------------------------

![说明](Context命令.files/image001.png)

本命令只有防火墙插卡设备支持。

**[location**]** blade-controller-team**命令用来使MDC进驻对应的安全引擎组。

**[undo location**]** blade-controller-team**命令用来将MDC从安全引擎组中移除。

【命令】

**[location blade-controller-team**]* team-id*

**[undo location blade-controller-team**]* team-id*

【缺省情况】

缺省MDC进驻了所有安全引擎组，非缺省MDC没有进驻任何安全引擎组。

【视图】

MDC视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[team-id*]：当前已经创建的安全引擎组的编号。

【使用指导】

Context从属于MDC，Context必须依附于所属MDC环境。为了使Context能进驻安全引擎，必须先将其所属的MDC进驻到该安全引擎。

MDC和安全引擎组的关系如下：

·多次执行该命令可以使一个MDC进驻多个不同的安全引擎组。

·在不同的MDC视图下执行该命令可以使多个MDC进驻同一个安全引擎组。MDC进驻安全引擎组后，该MDC会进驻引擎组内所有安全引擎。

需要注意的是：

·该命令用于MDC进驻引擎组。要使MDC下的Context进驻安全引擎组，请在对应的Context视图下执行**location blade-controller-team**命令。

·执行**undo** **location** **blade-controller-team**命令时，要求本MDC内不存在任何Context。否则，命令执行失败。

【举例】

\# 使MDC sub1进驻安全引擎组2。

\<Sysname\> system-view

Sysname mdc sub1

Sysname-mdc-2-sub1 location blade-controller-team 2

【相关命令】

·**blade-controller-team**

·**location blade-controller-team** (Context view)

**Context \-- Context命令 \-- reset blade-controller-team**

------------------------------------------------------------------------

![说明](Context命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[reset blade-controller-team**]命令用来清除指定安全引擎组中不在位的安全引擎的数据信息。

【命令】

集中式设备/分布式设备－独立运行模式/集中式IRF设备：

**[reset blade-controller-team** *team-id* **member slot** *slot-number* **cpu** *cpu-number*]

分布式IRF设备：

**[reset blade-controller-team ***team-id ***member chassis*** chassis-number ***slot ***slot-number* **cpu** *cpu-number*]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[team-id*]：安全引擎所属安全引擎组的编号，取值范围为1～256。可使用**display blade-controller-team**命令查看。

**[slot*** slot-number*]：表示安全引擎所在的槽位号。（集中式[/分布式设备－独立运行模式]）

**[slot*** slot-number*]：表示安全引擎所在设备的成员编号。（集中式IRF设备）

**[chassis ***chassis-number ***slot*** slot-number*]：*chassis-number*表示安全引擎所在设备的成员编号，*slot-number*表示安全引擎所在的槽位号。（分布式IRF设备）

**[cpu** *cpu-number*]：表示安全引擎的CPU编号。

【举例】

\# 清除安全引擎组abc中安全引擎（编号为1，所在位置为2号槽位1号CPU）的数据信息。（分布式设备－独立运行模式/集中式IRF设备）

\<sysname\> reset blade-controller-team 1 member slot 2 cpu 1

This operation will cause a short interruption of NAT session. Are you sure? [Y/N:y]

Erasing the controller data successed.

\# 清除安全引擎组abc中安全引擎（编号为1，所在位置为1号成员设备2号槽位1号CPU）的数据信息。（分布式设备－IRF模式）

\<sysname\> reset blade-controller-team 1 member chassis 1 slot 2 cpu 1

This operation will cause a short interruption of NAT session. Are you sure? [Y/N:y]

Erasing the controller data successed.

**Context \-- Context命令 \-- switchto context**

------------------------------------------------------------------------

**[switchto context**]命令用来登录到指定的Context。

【命令】

**[switchto context **]*context-name*

【视图】

系统视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[context-name*]：已启动的Context的名称。

【使用指导】

只要用户和物理设备之间路由可达，就能使用该命令，通过物理设备和Context的内联接口，登录Context。（不支持MDC的设备）

只要用户和MDC之间路由可达，就能使用该命令，通过MDC和Context的内联接口，登录Context。请在Context所属的MDC环境下执行该命令。例如，Context cnt2属于MDC test，则必须先通过**switchto mdc**命令或者Telnet等方式登录到MDC test，再通过**switchto context**命令登录到cnt2。（支持MDC的设备）

【举例】

\# 切换到Context test2。

\<Sysname\> system-view

Sysname switchto context test2

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Copyright (c) 2004-2013 Hangzhou H3C Tech. Co., Ltd. All rights reserved.  \*

\* Without the owner\'s prior written consent,                                 \*

\* no decompiling or reverse-engineering shall be allowed.                    \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\<Context2\>
