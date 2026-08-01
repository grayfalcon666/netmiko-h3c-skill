<!-- CMD-INDEX
  buffer apply                        | 系统视图             | L11
  buffer queue guaranteed             |                  | L49
  buffer queue shared                 | 系统视图             | L147
  buffer total-shared                 | 系统视图             | L237
  burst-mode enable                   | 系统视图             | L325
  display buffer                      | 任意视图             | L371
  display buffer usage                | 任意视图             | L547
-->

**数据缓冲区 \-- 数据缓冲区配置命令 \-- buffer apply**

------------------------------------------------------------------------

**[buffer apply**]命令用来应用用户对数据缓冲区所做的配置。

**[undo buffer apply**]命令用来取消数据缓冲区配置的应用。

【命令】

**[buffer apply**]

**[undo buffer apply**]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

用户对数据缓冲区进行配置后，必须使用**buffer apply**命令进行应用，这些配置才能生效。

配置被应用后就不能被修改，需要先取消应用，再修改、应用，新的配置才能生效。

【举例】

\# 应用用户对数据缓冲区所做的配置。

\<Sysname\> system-view

Sysname buffer apply

**数据缓冲区 \-- 数据缓冲区配置命令 \-- buffer queue guaranteed**

------------------------------------------------------------------------

![说明](数据缓冲区命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[buffer queue** **guaranteed**]命令用来配置指定队列最多可使用的固定区域的大小。

**[undo** **buffer** **queue** **guaranteed**]命令用来恢复缺省情况。

【命令】

集中式设备/分布式设备－独立运行模式/集中式IRF设备：

**[buffer **[{ **ingress** \| **egress** } [ **slot** *slot-number* ] { **cell** \| **packet** } **queue** *queue-id* **guaranteed** { **ratio** *ratio-value* \| *size-value* }]]

**[undo buffer **[{ **ingress** \| **egress** } [ **slot** *slot-number* ] { **cell** \| **packet** } **queue** *queue-id* **guaranteed**]]

分布式设备－IRF模式：

**[buffer **[{ **ingress** \| **egress** } [ **chassis** *chassis-number* **slot** *slot-number* ] { **cell** \| **packet** } **queue** *queue-id* **guaranteed** { **ratio** *ratio-value* \| *size-value* }]]

**[undo buffer **[{ **ingress** \| **egress** } [ **chassis** *chassis-number* **slot** *slot-number* ] { **cell** \| **packet** } **queue** *queue-id* **guaranteed**]]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ingress**]：表示对接收数据缓冲区进行配置。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[egress**]：表示对发送数据缓冲区进行配置。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[slot ***slot-number*]：取值只能为1，表示配置当前设备的数据缓冲区。（集中式设备）

**[slot ***slot-number*]：表示接口板所在的槽位号。不指定该参数时，表示配置所有接口板。（分布式设备－独立运行模式）

**[slot ***slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示配置所有成员设备。（集中式IRF设备）

**[chassis*** chassis-number ***slot ***slot-number*]：表示IRF中指定成员设备上的指定接口板。不指定该参数时，表示配置IRF的所有接口板。（分布式设备－IRF模式）

**[cell**]：配置队列最多可使用的cell资源中固定区域的大小。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[packet**]：配置队列最多可使用的packet资源中固定区域的大小。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[queue-id*]：需要配置的队列编号，取值范围为0～7。

**[ratio ***ratio-value*]：队列最多可使用的缓存大小占整个接口板cell或packet固定区域的大小的百分比。该参数的支持情况以及取值范围与设备的型号有关，请以设备的实际情况为准。

*[size-value*]：队列最多可使用的字节数。该参数的支持情况以及取值范围与设备的型号有关，请以设备的实际情况为准。

【使用指导】

缺省情况下，所有队列均分固定区域，但用户也可以使用该命令调整指定队列最多可使用的固定区域的大小，其它未配置的队列则均分剩余的固定区域。

配置该命令后，系统就与给队列预留指定大小的空间，即便该队列没有报文存储需求，其他队列也不能抢占。所有队列所配置的固定区域大小之和，不应超过可配置的总固定区域大小，否则配置失败。

【举例】

*[\# *]配置队列0最多可使用的cell固定区域的大小为整个cell固定缓冲区大小的20%。（集中式设备）

*[\<Sysname\>* system-view]

Sysname buffer egress cell queue 0 guaranteed ratio 20

\# 配置2号接口板的队列0最多可使用的cell固定区域的大小为该接口板cell固定缓冲区大小的15%。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname buffer egress slot 2 cell queue 0 guaranteed ratio 15

\# 配置成员设备2的队列0最多可使用的cell固定区域的大小为该成员设备cell固定缓冲区大小的15%。（集中式IRF设备）

\<Sysname\> system-view

Sysname buffer egress slot 2 cell queue 0 guaranteed ratio 15

\# 配置成员设备2上的2号接口板的队列0最多可使用的cell固定区域的大小为该接口板cell固定缓冲区大小的15%。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname buffer egress chassis 2 slot 2 cell queue 0 guaranteed ratio 15

**数据缓冲区 \-- 数据缓冲区配置命令 \-- buffer queue shared**

------------------------------------------------------------------------

**[buffer queue shared**]命令用来配置指定队列最多可使用的共享区域的大小。

**[undo** **buffer queue shared**]命令用来恢复缺省情况。

【命令】

集中式设备/分布式设备－独立运行模式/集中式IRF设备：

**[buffer **[{ **ingress** \| **egress** } [ **slot** *slot-number* ] { **cell** \| **packet** } **queue** *queue-id* **shared** { **ratio** *ratio-value* \| *size-value* }]]

**[undo buffer **[{ **ingress** \| **egress** } [ **slot** *slot-number* ] { **cell** \| **packet** } **queue** *queue-id* **shared**]]

分布式设备－IRF模式：

**[buffer **[{ **ingress** \| **egress** } [ **chassis** *chassis-number* **slot** *slot-number* ] { **cell** \| **packet** } **queue** *queue-id* **shared** { **ratio** *ratio-value* \| *size-value* }]]

**[undo buffer **[{ **ingress** \| **egress** } [ **chassis** *chassis-number* **slot** *slot-number* ] { **cell** \| **packet** } **queue** *queue-id* **shared**]]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ingress**]**：**表示对接收数据缓冲区进行配置。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[egress**]**：**表示对发送数据缓冲区进行配置。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[slot ***slot-number*]：取值只能为1，表示配置当前设备的数据缓冲区。（集中式设备）

**[slot ***slot-number*]：表示接口板所在的槽位号。不指定该参数时，表示配置所有接口板。（分布式设备－独立运行模式）

**[slot ***slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示配置所有成员设备。（集中式IRF设备）

**[chassis*** chassis-number ***slot ***slot-number*]：表示IRF中指定成员设备上的指定接口板。不指定该参数时，表示配置IRF的所有接口板。（分布式设备－IRF模式）

**[cell**]：配置队列在cell资源中的最大共享缓存区的大小。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[packet**]：配置队列在packet资源中的最大共享缓存区的大小。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[queue-id*]：需要配置的队列编号，取值范围为0～7。

**[ratio ***ratio-value*]：队列的最大共享缓存占用比，以百分数形式表示。该参数的支持情况以及取值范围与设备的型号有关，请以设备的实际情况为准。

*[size-value*]：队列的最大共享缓存占用字节数。参数的支持情况以及取值范围与设备的型号有关，请以设备的实际情况为准。

【使用指导】

缺省情况下，所有队列均分共享区域，但用户也可以调整指定队列最多可使用的共享区域的大小，其它未配置的队列最多可使用的共享区域的大小仍遵循缺省值。最终，各队列最多可使用的共享区域的大小将由芯片根据**buffer shared**配置，以及实际需要收发报文的数量决定。

【举例】

\# 配置队列0在cell资源中的最大共享缓存占用比为10%。（集中式设备）

\<Sysname\> system-view

Sysname buffer egress cell queue 0 shared ratio 10

\# 配置2号接口板的队列0在该设备cell资源中的最大共享缓存占用比为5%。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname buffer egress slot 2 cell queue 0 shared ratio 5

\# 配置成员设备2的队列0在该设备cell资源中的最大共享缓存占用比为5%。（集中式IRF设备）

\<Sysname\> system-view

Sysname buffer egress slot 2 cell queue 0 shared ratio 5

\# 配置成员设备2上的2号接口板的队列0在该设备cell资源中的最大共享缓存占用比为5%。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname buffer egress chassis 2 slot 2 cell queue 0 shared ratio 5

**数据缓冲区 \-- 数据缓冲区配置命令 \-- buffer total-shared**

------------------------------------------------------------------------

**[buffer total-shared**]命令用来配置数据缓冲区中共享区域的大小。

**[undo** **buffer total-shared**]命令用来恢复缺省情况。

【命令】

集中式设备/分布式设备－独立运行模式/集中式IRF设备：

**[buffer **[{ **ingress** \| **egress** } [ **slot** *slot-number* ] { **cell** \| **packet** } **total-shared** { **ratio** *ratio-value* \| *size-value* }]]

**[undo buffer **[{ **ingress** \| **egress** } [ **slot** *slot-number* ] { **cell** \| **packet** } **total-shared**]]

分布式设备－IRF模式：

**[buffer **[{ **ingress** \| **egress** } [ **chassis** *chassis-number* **slot** *slot-number* ] { **cell** \| **packet** } **total-shared** { **ratio** *ratio-value* \| *size-value* }]]

**[undo buffer **[{ **ingress** \| **egress** } [ **chassis** *chassis-number* **slot** *slot-number* ] { **cell** \| **packet** } **total-shared**]]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ingress**]：表示对接收数据缓冲区进行配置。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[egress**]：表示对发送数据缓冲区进行配置。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[slot ***slot-number*]：取值只能为1，表示配置当前设备的数据缓冲区。（集中式设备）

**[slot ***slot-number*]：表示接口板所在的槽位号。不指定该参数时，表示配置所有接口板。（分布式设备－独立运行模式）

**[slot ***slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示配置所有成员设备。（集中式IRF设备）

**[chassis*** chassis-number ***slot ***slot-number*]：表示IRF中指定成员设备上的指定接口板。不指定该参数时，表示配置IRF的所有接口板。（分布式设备－IRF模式）

**[cell**]：配置cell资源中的共享缓存区的大小。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[packet**]：配置packet资源中的共享缓存区的大小。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ratio ***ratio-value*]：缓冲区中共享区域所占的比例，以百分数形式表示。该参数的支持情况以及取值范围与设备的型号有关，请以设备的实际情况为准。

*[size-value*]：缓冲区中共享区域所占的字节数。该参数的支持情况以及取值范围与设备的型号有关，请以设备的实际情况为准。

【使用指导】

接口卡上整个数据缓冲区的大小是固定的，用户配置共享区域的大小后，其余部分将自动成为固定区域。

【举例】

\# 配置当前设备cell资源中的共享区域所占比例为50%。（集中式设备）

\<Sysname\> system-view

Sysname buffer egress cell total-shared ratio 50

\# 配置2号接口板的cell资源中共享区域所占比例为65%。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname buffer egress slot 2 cell total-shared ratio 65

\# 配置成员设备2的cell资源中共享区域所占比例为65%。（集中式IRF设备）

\<Sysname\> system-view

Sysname buffer egress slot 2 cell total-shared ratio 65

\# 配置成员设备2上的2号接口板的cell资源中共享区域所占比例为65%。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname buffer egress chassis 2 slot 2 cell total-shared ratio 65

**数据缓冲区 \-- 数据缓冲区配置命令 \-- burst-mode enable**

------------------------------------------------------------------------

**[burst-mode enable**]命令用来开启Burst功能。

**[undo burst-mode enable**]命令用来关闭Burst功能。

【命令】

**[burst-mode enable**]

**[undo burst-mode enable**]

【缺省情况】

Burst功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在下列情况下，Burst功能可以提供更好的报文缓存功能和流量转发性能：

·广播或者组播报文流量密集，瞬间突发大流量的网络环境中；

·报文从高速链路进入设备，由低速链路转发出去；或者报文从相同速率的多个接口同时进入设备，由一个相同速率的接口转发出去。

用户可以通过开启Burst功能，降低设备在上述特定环境中的报文丢包率，提高对报文的处理能力。

【举例】

\# 开启Burst功能。

\<Sysname\> system-view

Sysname burst-mode enable

**数据缓冲区 \-- 数据缓冲区配置命令 \-- display buffer**

------------------------------------------------------------------------

**[display buffer**]命令显示数据缓冲区的大小。

【命令】

集中式设备/分布式设备－独立运行模式/集中式IRF设备：

**[display buffer ** **slot** *slot-number* ]  **queue** [ *queue-id*  ]

分布式设备－IRF模式：

**[display buffer ** **chassis** *chassis-number* **slot** *slot-number* ]  **queue** [ *queue-id*  ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot*** slot-number*]：取值只能为1，暂无意义。（集中式设备）

**[slot*** slot-number*]：表示接口板所在的槽位号。不指定该参数时，表示所有接口板。（分布式设备－独立运行模式）

**[slot*** slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示所有成员设备。（集中式IRF设备）

**[chassis** *chassis-number* **slot** *slot-number*]：表示IRF中指定成员设备上的指定接口板。不指定该参数时，表示IRF中的所有接口板。（分布式设备－IRF模式）

**[queue** *queue-id*]：表示队列的编号，取值范围为0～7。如果不指定*queue-id*，表示所有队列。

【使用指导】

**[display buffer**]命令不带**queue**关键字时，显示共享区域的大小。

**[display buffer**]命令带**queue**关键字时，显示队列最多可使用的固定区域的大小以及队列最多可使用的共享区域的大小。其中，指定*queue-id*时，显示指定队列的相关信息，不指定*queue-id*时，显示所有队列的相关信息。

【举例】

\# 显示数据缓冲区的大小。（不同型号的设备显示信息不同，请以设备的实际情况为准）（集中式设备/分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display buffer

Slot      Type          In(Total-shared)        Eg(Total-shared)

1         packet        24                      36

1         cell          50                      \--

          In: Size of the receiving buffer

          Eg: Size of the sending buffer

Total-shared: Size of the shared buffer for all ports

      Shared: Size of the maximum shared buffer per port

        Unit: Ratio

\<Sysname\> display buffer queue

Slot      Queue          Type       In(Guaranteed , Shared)     Eg(Guaranteed , Shared)

1         0-7            packet     256 , 128                   256 , 128

1         0-1,3-4,6-7    cell       256 , 128                   256 , 128

1         2,5            cell       512 , 128                   \-- , \--

        In: Size of the receiving buffer

        Eg: Size of the sending buffer

Guaranteed: Size of the minimum guaranteed buffer per queue

    Shared: Size of the maximum shared buffer per queue

      Unit: Byte

\# 显示成员设备1上2号接口板数据缓冲区的大小。（不同型号的设备显示信息不同，请以设备的实际情况为准）（分布式设备－IRF模式）

\<Sysname\> display buffer chassis 1 slot 2

Slot      Type          In(Total-shared , Shared)        Eg(Total-shared , Shared)

1/2       packet        24 , 2                           36 , 2

1/2       cell          50 , 25                          \-- , \--

          In: Size of the receiving buffer

          Eg: Size of the sending buffer

Total-shared: Size of the shared buffer for all ports

      Shared: Size of the maximum shared buffer per port

        Unit: Ratio

\<Sysname\> display buffer chassis 1 slot 2 queue

Slot      Queue          Type       In(Guaranteed , Shared)     Eg(Guaranteed , Shared)

1/2       0-7            packet     256 , 128                   256 , 128

1/2       0-1,3-4,6-7    cell       256 , 128                   256 , 128

1/2       2,5            cell       512 , 128                   \-- , \--

        In: Size of the receiving buffer

        Eg: Size of the sending buffer

Guaranteed: Size of the minimum guaranteed buffer per queue

    Shared: Size of the maximum shared buffer per queue

      Unit: Byte

表1-1 display buffer命令显示信息描述表

字段

描述

Slot

取值固定为1（集中式设备）

表示接口板所在的槽位号（分布式设备－独立运行模式）

表示设备在IRF中的成员编号（集中式IRF设备）

表示接口板所在的槽位号，其中第一维为设备在IRF中的成员编号，第二维为接口板在成员设备上的槽位号（分布式设备－IRF模式）

Type

缓冲区类型，包括packet资源和cell资源

Queue

队列ID，范围为0～7

In

Ingress，入方向的数据缓冲区配置

Eg

Egress，出方向的数据缓冲区配置

(Total-shared)

共享区域的大小。如果显示为"\--"字符串，则表示设备不支持该缓冲区

(Guaranteed , Shared)

Guaranteed表示最多可使用的固定区域的大小。如果显示为"\--"字符串，则表示设备不支持该数据缓冲区

Shared对应表示最多可使用的共享区域的大小。如果显示为"\--"字符串，则表示设备不支持该数据缓冲区

Unit

数据缓冲区的单位，为%或byte

**数据缓冲区 \-- 数据缓冲区配置命令 \-- display buffer usage**

------------------------------------------------------------------------

**[display buffer usage**]命令用来显示数据缓冲区的使用率。

【命令】

集中式设备/分布式设备－独立运行模式/集中式IRF设备：

**[display buffer** **usage** [ **slot** *slot-number* ]]

分布式设备－IRF模式：

**[display buffer** **usage** [ **chassis** *chassis-number* **slot** *slot-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot*** slot-number*]：取值只能为1，表示显示当前设备的数据缓冲区的使用率。（集中式设备）

**[slot*** slot-number*]：表示接口板所在的槽位号。不指定该参数时，表示所有接口板。（分布式设备－独立运行模式）

**[slot*** slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示所有成员设备。（集中式IRF设备）

**[chassis** *chassis-number* **slot** *slot-number*]：表示IRF中指定成员设备上的指定接口板。不指定该参数时，表示IRF中的所有接口板。（分布式设备－IRF模式）

【举例】

\# 显示数据缓冲区的使用率。（不同型号的设备显示信息不同，请以设备的实际情况为准）

\<Sysname\> display buffer usage

Egress total-shared cell buffer usage for slot 1:

         4% in last 5 seconds

        16% in last 1 minute

        14% in last 5 minutes

