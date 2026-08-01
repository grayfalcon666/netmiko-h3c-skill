<!-- CMD-INDEX
  display license                     | 任意视图             | L14
  display license feature             | 任意视图             | L392
  display license device-id           |                  | L600
  license activation-file install     | 系统视图             | L726
  license activation-file uninstall   | 系统视图             | L824
  license activation-key install      | 系统视图             | L938
  license activation-key unistall     | 系统视图             | L1036
  license compress                    | 系统视图             | L1146
  license license-key install         | 系统视图             | L1258
  license license-key uninstall       | 系统视图             | L1354
-->

**License管理 \-- License管理命令 \-- display license**

------------------------------------------------------------------------

**[display license**]命令用来显示License的详细信息。

【命令】

集中式设备/分布式设备－独立运行模式不支持slot：

**[display license **[[ **activation-file** \| **activation-key** \| **license-key** ]]]

分布式设备－独立运行模式支持slot/集中式IRF设备：

**[display license **[[ **activation-file** \| **activation-key** \| **license-key** ]  **slot** *slot-number* ]]

分布式设备－IRF模式不支持slot：

**[display license **[[ **activation-file** \| **activation-key** \| **license-key** ]  **chassis** *chassis-number* ]]

分布式设备－IRF模式支持slot：

**[display license **[[ **activation-file** \| **activation-key** \| **license-key** ]  **chassis** *chassis-number* **slot** *slot-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[activation-file**]：显示设备上已存在的激活文件相关信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[activation-key**]**：**显示设备上已存在的激活码相关信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[license-key**]：显示设备上已存在的授权码相关信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[slot** *slot-number*]：显示指定主控板上安装的License信息。*slot-number*表示主控板所在的槽位号。不指定该参数时，显示设备上所有主控板的License信息。（分布式设备－独立运行模式支持slot/分布式设备－IRF模式）

**[slot** *slot-number*]：显示指定成员设备上安装的License信息。*slot-number*表示设备在IRF中的成员编号。不指定该参数时，显示所有成员设备上的License信息。（集中式IRF设备）

**[chassis ***chassis-number*]：显示指定成员设备上安装的License信息。*chassis-number*表示设备在IRF中的成员编号。不指定该参数时，显示所有成员设备上的License信息。（分布式设备－IRF模式不支持slot）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备的指定主控板上安装的License信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示主控板所在的槽位号。不指定该参数时，显示所有主控板上的License信息。（分布式设备－IRF模式支持slot）

【使用指导】

如果不指定**activation-file**、**activation-key**和**license-key**参数，则显示所有类型License的详细信息。

【举例】

\# 显示设备上所有License的详细信息。（集中式设备/分布式设备－独立运行模式不支持slot）

\<Sysname\> display license

Feature: opt

Feature Description: opt license.

Activation Key: QvkT-%gfS-Xz/4-jR@V-9g%3-79wv-NMFG-kmJ9

Registered at: 2013-02-23 11:36:09

License Type: Days restricted

Time Left (days): 249

Current State: In use

flash:/license/H3CS12500F_2014072009113494375.ak

Feature: LISP EVB evi mdc SPBM TRILL FCoE

Product Description: H3C S12500-F Advanced Data Center License

Registered at: 2014-05-07 15:07:39

License Type: Permanent

Current State: In use

flash:/license/H3CVSR10008vCPU_2014072009113494375.ak

Feature: STANDARD

Product Description: H3C VSR1000  License(Comware V7,STANDARD Edition,8vCPU,Permanent)

Registered at: 2014-07-20 09:13:29

License Type: Permanent

Current State: In use

\# 显示设备上所有License的详细信息。（分布式设备－独立运行模式支持slot）

\<Sysname\> display license

Slot 0:

Feature: opt

Feature Description: opt license.

Activation Key: cyKT-x3vc-W@Ca-n4gn-YB83-rVY3-C8:7-e3pg

Registered at: 2013-02-21 15:26:33

License Type: Trial (days restricted)

Trial Time Left (days): 20

Current State: In use

flash:/license/H3CS12500F_2014072009113494375.ak

Feature: LISP EVB evi mdc SPBM TRILL FCoE

Product Description: H3C S12500-F Advanced Data Center License

Registered at: 2014-05-07 15:07:39

License Type: Permanent

Current State: In use

flash:/license/H3CVSR10008vCPU_2014072009113494375.ak

Feature: STANDARD

Product Description: H3C VSR1000  License(Comware V7,STANDARD Edition,8vCPU,Permanent)

Registered at: 2014-07-20 09:13:29

License Type: Permanent

Current State: In use

\# 显示IRF中所有License的详细信息。（集中式IRF设备）

\<Sysname\> display license

Slot 1:

Feature: opt

Feature Description: opt license.

Activation Key: dyKT-x3vc-W@Ca-n4gn-Yo83-rVY3-C8:7-e3pg

Registered at: 2013-02-21 15:26:33

License Type: Trial (days restricted)

Time Left (days): 20

Current State: In use

flash:/license/H3CS12500F_2014072009113494375.ak

Feature: LISP EVB evi mdc SPBM TRILL FCoE

Product Description: H3C S12500-F Advanced Data Center License

Registered at: 2014-05-07 15:07:39

License Type: Permanent

Current State: In use

flash:/license/H3CVSR10008vCPU_2014072009113494375.ak

Feature: STANDARD

Product Description: H3C VSR1000  License(Comware V7,STANDARD Edition,8vCPU,Permanent)

Registered at: 2014-07-20 09:13:29

License Type: Permanent

Current State: In use

\# 显示IRF中所有License的详细信息。（分布式设备－IRF模式不支持slot）

\<Sysname\> display license

Chassis 2:

Feature: opt

Feature Description: opt license.

Activation Key: cyKT-x3vc-WsCa-n4gn-YB83-rsY3-C8:7-e3pg

Registered at: 2013-02-21 15:26:33

License Type: Trial (days restricted)

Trial Time Left (days): 20

Current State: In use

flash:/license/H3CS12500F_2014072009113494375.ak

Feature: LISP EVB evi mdc SPBM TRILL FCoE

Product Description: H3C S12500-F Advanced Data Center License

Registered at: 2014-05-07 15:07:39

License Type: Permanent

Current State: In use

flash:/license/H3CVSR10008vCPU_2014072009113494375.ak

Feature: STANDARD

Product Description: H3C VSR1000  License(Comware V7,STANDARD Edition,8vCPU,Permanent)

Registered at: 2014-07-20 09:13:29

License Type: Permanent

Current State: In use

\# 显示IRF中所有License的详细信息。（分布式设备－IRF模式支持slot）

\<Sysname\> display license chassis 2 slot 1

Chassis 2 Slot 1：

Feature: opt

Feature Description: opt license.

Activation Key: cydT-x3vc-W@Ca-n4gn-YB83-rVY3-C8:7-e3pg

Registered at: 2013-02-21 15:26:33

License Type: Trial (days restricted)

Trial Time Left (days): 20

Current State: In use

flash:/license/H3CS12500F_2014072009113494375.ak

Feature: LISP EVB evi mdc SPBM TRILL FCoE

Product Description: H3C S12500-F Advanced Data Center License

Registered at: 2014-05-07 15:07:39

License Type: Permanent

Current State: In use

flash:/license/H3CVSR10008vCPU_2014072009113494375.ak

Feature: STANDARD

Product Description: H3C VSR1000  License(Comware V7,STANDARD Edition,8vCPU,Permanent)

Registered at: 2014-07-20 09:13:29

License Type: Permanent

Current State: In use

表1-1  display license{.FigureDescriptionChar}命令显示信息描述表

字段

描述

Chassis *n*

*[n*]号成员设备上的License信息（分布式设备－IRF模式不支持slot）

Slot *n*

*[n*]号主控板上的License信息（分布式设备－独立运行模式支持slot）

*[n*]号成员设备上的License信息（集中式IRF设备）

Chassis *n* slot *m*

*[n*]号成员设备*m*号主控板上的License信息（分布式设备－IRF模式支持slot）

Feature

特性名称

Feature Description

特性的相关描述

Product Description

激活文件产品描述信息

License Key

显示安装的授权码信息

Activation Key

显示安装的激活码信息

Registered at

在设备上的安装时间

License Type

License的类型，取值为：

·NA：无法获取License的类型

·Permanent：永久类型，表示该License永远有效，不会过期

·Days restricted：相对时间类型，表示该License是正式发布的，且有效期是一个相对时间段，比如30天

·Date restricted：绝对时间类型，表示该License是正式发布的，且有效期是一个绝对时间段，比如2013年5月1日到2013年5月30日

·Trial (days restricted)：相对时间类型的试用License，表示该License是相对时间类型的、非正式发布的License

·Trial (date restricted)：绝对时间类型的试用License，表示该License是绝对时间类型的、非正式发布的License

Time Left (days)

正式授权相对时间类型剩余时间

Trial Time Left (days)

临时授权相对时间类型剩余时间

Validity Period

正式授权绝对时间类型过期日期。No limit表示不限制时间

Trial Validity Period

临时授权绝对时间类型过期日期。No limit表示不限制时间

Current State

License当前状态取值为：

·In use：当前License正在使用

·Usable：当前License正在等待使用（当设备同时安装了多个相对时间License，且多个License均支持某一特性时，则只有一个License中的该特性处于In use状态，其它License中的该特性会处于Usable状态。绝对时间License，此状态表示未到启用时间）

·Expired：当前License已过期

·Uninstalled：当前License已卸载

·Unusable：当前License无法使用

·Invalid：不合法的数据，无法使用

Uninstall Key

卸载码

Uninstall Date

卸载日期

**License管理 \-- License管理命令 \-- display license feature**

------------------------------------------------------------------------

**[display license feature**]命令用来显示特性的License摘要信息。

【命令】

**[display license feature**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

License摘要信息包括哪些特性需要安装License，以及已安装的License的简要信息。

【举例】

\# 显示License摘要信息。（集中式设备）（分布式设备－独立运行模式不支持slot）

\<Sysname\> display license feature

Total: 50 Usage: 7

Feature       Licensed     State

OPT           Y            Formal

OSPF          N            -

MPLS          Y            Trail

\# 显示License摘要信息。（分布式设备－独立运行模式支持slot）

\<Sysname\> display license feature

Slot 0:

Total: 50   Usage: 7

Feature       Licensed     State

OPT           Y            Formal

OSPF          N            -

MPLS          Y            Trail

Slot 1:

Total: 50   Usage: 7

Feature       Licensed     State

OPT           Y            Formal

OSPF          N            -

MPLS          Y            Trail

\# 显示License摘要信息。（集中式IRF设备）

\<Sysname\> display license feature

Slot 0:

Total: 50 Usage: 7

Feature       Licensed     State

OPT           Y            Formal

OSPF          N            -

MPLS          Y            Trail

Slot 1:

Total: 50  Usage: 7

Feature       Licensed     State

OPT           Y            Formal

OSPF          N            -

MPLS          Y            Trail

\# 显示License摘要信息。（分布式设备－IRF模式不支持slot）

\<Sysname\> display license feature

Chassis 1:

Total: 50 Usage: 7

Feature       Licensed     State

OPT           Y            Formal

OSPF          N            -

MPLS          Y            Trail

Chassis 2:

Total: 50  Usage: 7

Feature       Licensed     State

OPT           Y            Formal

OSPF          N            -

MPLS          Y            Trail

\# 显示License摘要信息。（分布式设备－IRF模式支持slot）

\<Sysname\> display license feature

Chassis 1 Slot 0:

Total: 50   Usage: 7

Feature       Licensed     State

OPT           Y            Formal

OSPF          N            -

MPLS          Y            Trail

Chassis 2 Slot 1:

Total: 50   Usage: 7

Feature       Licensed     State

OPT           Y            Formal

OSPF          N            -

MPLS          Y            Trail

表1-2 display license feature命令显示信息描述表

字段

描述

Slot *n*

*[n*]号主控板上的License摘要信息（分布式设备－独立运行模式支持slot）

Slot *n*

*[n*]号成员备上的License摘要信息（集中式IRF设备）

Chassis *n*

*[n*]号成员备上的License摘要信息（分布式设备－IRF模式不支持slot）

Chassis *n* Slot *m*

*[n*]号成员设备的*m*号主控板上的License摘要信息（分布式设备－IRF模式支持slot）

Total

设备上一共可安装License的总数目

Usage

设备上已经安装的License总数

Feature

需要License授权才能使用的业务特性的名称

Licensed

是否已经授权

·N表示未授权

·Y表示已授权

State

License的当前状态：

·Formal表示当前已经为该特性安装了正式License，License处于有效状态

·Trail表示当前已经为该特性安装了临时License，License处于有效状态

·-表示当前无有效License，用户如需使用该特性，请安装对应的License

**License管理 \-- License管理命令 \-- display license device-id**

------------------------------------------------------------------------

**[display license device-id**]命令用来显示设备的SN和DID信息。（集中式设备/分布式设备－独立运行模式不支持slot）

**[display license device-id** **slot** *slot-number*]命令用来显示指定主控板的SN和DID信息。（分布式设备－独立运行模式支持slot）

**[display license device-id** **slot** *slot-number*]命令用来显示指定成员设备的SN和DID信息。（集中式IRF设备）

**[display license device-id chassis** *chassis-number*]命令用来显示指定成员设备的SN和DID信息。（分布式设备－IRF模式不支持slot）

**[display license device-id** **chassis** *chassis-number* **slot** *slot-number*]命令用来显示指定成员设备上指定主控板的SN和DID信息。（分布式设备－IRF模式支持slot）

【命令】

集中式设备/分布式设备－独立运行模式不支持slot：

**[display license device-id**]

分布式设备－独立运行模式支持slot/集中式IRF设备：

**[display license device-id** **slot** *slot-number*]

分布式设备－IRF模式不支持slot：

**[display license device-id** **chassis** *chassis-number*]

分布式设备－IRF模式支持slot：

**[display license device-id** **chassis** *chassis-number* **slot** *slot-number*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot** *slot-number*]：表示主控板所在的槽位号。（分布式设备－独立运行模式支持slot）

**[slot** *slot-number*]：表示设备在IRF中的成员编号。（集中式IRF设备）

**[chassis** *chassis-number*]：表示设备在IRF中的成员编号。（分布式设备－IRF模式不支持slot）

**[chassis** *chassis-number* **slot** *slot-number*]：表示IRF中指定成员设备上的指定主控板。（分布式设备－IRF模式支持slot）

【使用指导】

生成License激活码或激活文件需要使用DID和SN，用来表示激活码/激活文件和设备的绑定关系。

DID在执行压缩命令的时候会发生变化。因此，请在申请激活码或激活文件前，查询设备的DID信息。

DID有两种形式：

·字符串形式。在申请激活码或激活文件时，直接在申请页面输入该字符串即可。

·文件形式。在申请激活码或激活文件时，需通过申请页面上传该文件。

不同型号的产品支持的DID形式不同，请以设备的实际情况为准。

【举例】

\# 显示设备的SN和DID信息。（集中式设备/分布式设备－独立运行模式不支持slot）

\<Sysname\> display license device-id

SN: XXXXXXXXXXXXXXXXXXXX

Device ID: XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX

\# 显示主控板1的SN和DID信息。（分布式设备－独立运行模式支持slot）

\<Sysname\> display license device-id slot 1

SN: XXXXXXXXXXXXXXXXXXXX

Device ID: XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX

\# 显示成员设备2的SN和DID信息。（集中式IRF设备）

\<Sysname\> display license device-id slot 2

SN: XXXXXXXXXXXXXXXXXXXX

Device ID: XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX

\# 显示成员设备2的SN和DID信息。（分布式设备－IRF模式不支持slot）

\<Sysname\> display license device-id chassis 2

SN: XXXXXXXXXXXXXXXXXXXX

Device ID: XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX

\# 显示成员设备2的1号主控板的SN和DID信息。（分布式设备－IRF模式支持slot）

\<Sysname\> display license device-id chassis 2 slot 1

SN: XXXXXXXXXXXXXXXXXXXX

Device ID: XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX

表1-3  display license device-id{.FigureDescriptionChar}命令显示信息描述表

字段

描述

SN

序列号信息，用于生成激活码或激活文件

Device ID

设备编号信息，用于生成激活码或激活文件

**License管理 \-- License管理命令 \-- license activation-file install**

------------------------------------------------------------------------

**[license activation-file install**]命令用来安装License的激活文件。

【命令】

集中式设备/分布式设备－独立运行模式不支持slot：

**[license activation-file install** *file-name*]

分布式设备－独立运行模式支持slot/集中式IRF设备：

**[license activation-file install ***file-name*** slot** *slot-number*]

分布式设备－IRF模式不支持slot：

**[license activation-file install ***file-name*** chassis** *chassis-number*]

分布式设备－IRF模式支持slot：

**[license activation-file install ***file-name*** chassis** *chassis-number* **slot** *slot-number*]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[file-name*]：激活文件的全路径，为1～127个字符的字符串，区分大小写。激活文件必须合法、有效，并且保存在设备存储介质上。

**[slot** *slot-number*]：表示给主控板安装License激活文件，主控板安装[激活文件后，即便插入别的设备，也具有运行相应特性的授权。]*slot-number*表示主控板所在的槽位号。（分布式设备－独立运行模式支持slot）

**[slot** *slot-number*]：表示给成员设备安装License激活文件，成员设备安装[激活文件后，即便加入别的]IRF，也具有运行相应特性的授权。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[chassis ***chassis-number*]：表示给成员设备安装License激活文件，成员设备安装[激活文件后，即便加入别的]IRF，也具有运行相应特性的授权。*chassis-number*表示设备在IRF中的成员编号。（分布式设备－IRF模式不支持slot）

**[chassis** *chassis-number* **slot** *slot-number*]：表示给指定成员设备上的指定主控板安装License激活文件，主控板安装[激活文件后，即便插入别的设备，也具有运行相应特性的授权。]*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示主控板所在的槽位号。（分布式设备－IRF模式支持slot）

【使用指导】

激活文件是用户购买的激活受控特性的凭证。激活文件安装到设备上后，对应的特性得到授权，可以正常使用。

【举例】

\# 安装激活文件20130810.ak。（集中式设备）（分布式设备－独立运行模式不支持slot）

\<Sysname\> system-view

Sysname license activation-file install flash:/license/20130810.ak

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

\# 给主控板1安装激活文件20130811.ak。（分布式设备－独立运行模式支持slot）

\<Sysname\> system-view

Sysname license activation-file install flash:/license/20130811.ak slot 1

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

\# 给成员设备2安装激活文件20130812.ak。（集中式IRF设备）

\<Sysname\> system-view

Sysname license activation-file install flash:/license/20130812.ak slot 2

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

\# 给成员设备2安装激活文件20130813.ak。（分布式设备－IRF模式不支持slot）

\<Sysname\> system-view

Sysname license activation-file install flash:/license/20130813.ak chassis 2

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

\# 给成员设备2的1号主控板安装激活文件20130814.ak。（分布式设备－IRF模式支持slot）

\<Sysname\> system-view

Sysname license activation-file install flash:/license/20130814.ak chassis 2 slot 1

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

【相关命令】

·**display license activation-file**

·**license activation-file uninstall**

**License管理 \-- License管理命令 \-- license activation-file uninstall**

------------------------------------------------------------------------

**[license activation-file uninstall**]命令用来卸载License的激活文件。

【命令】

集中式设备/分布式设备－独立运行模式不支持slot：

**[license activation-file uninstall ***file-name*]

分布式设备－独立运行模式支持slot/集中式IRF设备：

**[license activation-file uninstall ***file-name*** slot** *slot-number*]

分布式设备－IRF模式不支持slot：

**[license activation-file uninstall ***file-name*** chassis** *chassis-number*]

分布式设备－IRF模式支持slot：

**[license activation-file uninstall ***file-name*** chassis** *chassis-number* **slot** *slot-number*]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[file-name*]：激活文件的全路径，为1～127个字符的字符串，区分大小写。

**[slot** *slot-number*]：表示给主控板卸载License激活文件，主控板卸载[激活文件后，将不能使用该激活文件包含的特性。]*slot-number*表示主控板所在的槽位号。（分布式设备－独立运行模式支持slot）

**[slot** *slot-number*]：表示给成员设备卸载License激活文件，成员设备卸载[激活文件后，将不能使用该激活文件包含的特性。]*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[chassis ***chassis-number*]：表示给成员设备卸载License激活文件，成员设备卸载[激活文件后，将不能使用该激活文件包含的特性。]*chassis-number*表示设备在IRF中的成员编号。（分布式设备－IRF模式不支持slot）

**[chassis** *chassis-number* **slot** *slot-number*]：表示给指定成员设备上的指定主控板卸载License激活文件，成员设备卸载[激活文件后，将不能使用该激活文件包含的特性。]*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示主控板所在的槽位号。（分布式设备－IRF模式支持slot）

【使用指导】

当用户购买的正式激活文件还没有到期，并且在当前上设备不需要再使用时，可以卸载该激活文件，此时设备会产生一个卸载凭证------卸载文件。用户可以将该卸载凭证和其它设备绑定，获取一个新的激活文件，并在新设备上安装，从而将License从当前设备迁移到其它设备。

需要注意的是：

·激活文件被卸载后，对应的特性将无法获得到被卸载的激活文件的信息，特性无法运行。

·如果卸载的是临时激活文件，则不会产卸载文件；如果卸载的是正式激活文件，则会产卸载文件。

【举例】

\# 卸载正式激活文件flash:/license/20130810.ak。（集中式设备）（分布式设备－独立运行模式不支持slot）

\<Sysname\> system-view

Sysname license activation-file uninstall flash:/license/20130810.ak

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

Uninstall file: flash:/license/20130810.uak

\# 给主控板1卸载正式激活文件flash:/license/20130811.ak。（分布式设备－独立运行模式支持slot）

\<Sysname\> system-view

Sysname license activation-file uninstall flash:/license/20130811.ak slot 1

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

Uninstall file: flash:/license/20130813.uak

\# 给成员设备2卸载正式激活文件flash:/license/20130812.ak。（集中式IRF设备）

\<Sysname\> system-view

Sysname license activation-file uninstall flash:/license/20130812.ak slot 2

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

Uninstall file: flash:/license/20130812.uak

\# 给成员设备2卸载正式激活文件flash:/license/20130813.ak。（分布式设备－IRF模式不支持slot）

\<Sysname\> system-view

Sysname license activation-file uninstall flash:/license/20130813.ak chassis 2

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

Uninstall file: flash:/license/20130813.uak

\# 给成员设备2的1号主控板卸载正式激活文件flash:/license/20130814.ak。（分布式设备－IRF模式支持slot）

\<Sysname\> system-view

Sysname license activation-file uninstall flash:/license/20130814.ak chassis 2 slot 1

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

Uninstall file: flash:/license/20130814.uak

【相关命令】

·**display license activation-file**

·**license activation-file install**

**License管理 \-- License管理命令 \-- license activation-key install**

------------------------------------------------------------------------

**[license activation-key install**]命令用来安装License的激活码。

【命令】

集中式设备/分布式设备－独立运行模式不支持slot：

**[license activation-key install** *activation-key-string*]

分布式设备－独立运行模式支持slot/集中式IRF设备：

**[license activation-key install ***activation-key-string*** slot** *slot-number*]

分布式设备－IRF模式不支持slot：

**[license activation-key install ***activation-key-string*** chassis** *chassis-number*]

分布式设备－IRF模式支持slot：

**[license activation-key install ***activation-key-string*** chassis** *chassis-number* **slot** *slot-number*]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[activation-key-string*]：激活码，格式为XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX，区分大小写，必须是合法、有效的激活码。

**[slot** *slot-number*]：表示给主控板安装激活码，主控板安装激活码后，即便插入别的设备，也具有运行相应特性的授权。*slot-number*表示主控板所在的槽位号。（分布式设备－独立运行模式支持slot）

**[slot** *slot-number*]：表示给成员设备安装激活码，成员设备安装激活码后，即便加入别的IRF，也具有运行相应特性的授权。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[chassis ***chassis-number*]：表示给成员设备安装激活码，成员设备安装激活码后，即便加入别的IRF，也具有运行相应特性的授权。*chassis-number*表示设备在IRF中的成员编号。（分布式设备－IRF模式不支持slot）

**[chassis** *chassis-number* **slot** *slot-number*]：表示给指定成员设备上的指定主控板安装激活码，主控板安装激活码后，即便插入别的设备，也具有运行相应特性的授权。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示主控板所在的槽位号。（分布式设备－IRF模式支持slot）

【使用指导】

激活码是用户购买的激活受控特性的凭证。激活码安装到设备上后，对应的特性得到授权，可以正常使用。

【举例】

\# 安装激活码XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX。（集中式设备）（分布式设备－独立运行模式不支持slot）

\<Sysname\> system-view

Sysname license activation-key install XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

\# 给主控板1安装激活码XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX。（分布式设备－独立运行模式支持slot）

\<Sysname\> system-view

Sysname license activation-key install XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX slot 1

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

\# 给成员设备2安装激活码XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX。（集中式IRF设备）

\<Sysname\> system-view

Sysname license activation-key install XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX slot 2

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

\# 给成员设备2安装激活码XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX。（分布式设备－IRF模式不支持slot）

\<Sysname\> system-view

Sysname license activation-key install XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX chassis 2

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

\# 给成员设备2的1号主控板安装激活码XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX。（分布式设备－IRF模式支持slot）

\<Sysname\> system-view

Sysname license activation-key install XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX chassis 2 slot 1

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

【相关命令】

·**display license activation-key**

·**license activation-key uninstall**

**License管理 \-- License管理命令 \-- license activation-key unistall**

------------------------------------------------------------------------

**[license activation-key uninstall**]命令用来卸载激活码。

【命令】

集中式设备/分布式设备－独立运行模式不支持slot：

**[license activation-key uninstall ***activation-key-string*]

分布式设备－独立运行模式支持slot/集中式IRF设备：

**[license activation-key uninstall ***activation-key-string*** slot** *slot-number*]

分布式设备－IRF模式不支持slot：

**[license activation-key uninstall ***activation-key-string*** chassis** *chassis-number*]

分布式设备－IRF模式支持slot：

**[license activation-key uninstall ***activation-key-string*** chassis** *chassis-number* **slot** *slot-number*]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[activation-key-string*]：要卸载的激活码，格式为xxxx-xxxx-xxxx-xxxx-xxxx-xxxx-xxxx-xxxx，区分大小写。只有设备上已安装且未过期的激活码才可以卸载。

**[slot** *slot-number*]：表示给主控板卸载激活码。*slot-number*表示主控板所在的槽位号。（分布式设备－独立运行模式支持slot）

**[slot** *slot-number*]：表示给成员设备卸载激活码。成员设备卸载激活码后，将失去此激活码的授权信息，特性将无法获取到卸载的激活码的授权信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[chassis ***chassis-number*]：表示给成员设备卸载激活码。成员设备卸载激活码后，成员设备将失去此激活码的授权信息，特性模块将无法再获取到此授权码的授权信息。*chassis-number*表示设备在IRF中的成员编号。（分布式设备－IRF模式不支持slot）

**[chassis** *chassis-number* **slot** *slot-number*]：表示给指定成员设备的指定主控板卸载激活码。成员设备卸载激活码后，成员设备将失去此激活码的授权信息，特性模块将无法再获取到此授权码的授权信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示主控板所在的槽位号。（分布式设备－IRF模式支持slot）

【使用指导】

当用户需要将特性授权信息迁移到其它设备上使用时，可以卸载特性对应的激活码，此时设备会产生一个卸载凭证------卸载码，本设备对应的特性将无法使用。用户可以将授权信息和其他设备绑定，从而将授权信息从一个设备迁移到另一台设备。

如果卸载的是正式激活码，则会产生卸载码；如果卸载的是临时激活码，则不会产生卸载码。

【举例】

\# 卸载正式激活码XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX。（集中式设备/分布式设备－独立运行模式不支持slot）

\<Sysname\> system-view

Sysname license activation-key uninstall XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

Uninstall key: YYYY-YYYY-YYYY-YYYY-YYYY-YYYY-YYYY-YYYY

\# 给主控板1卸载正式激活码XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX。（分布式设备－独立运行模式支持slot）

\<Sysname\> system-view

Sysname license activation-key uninstall XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX slot 1

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

Uninstall key: YYYY-YYYY-YYYY-YYYY-YYYY-YYYY-YYYY-YYYY

\# 给成员设备2卸载正式激活码XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX。（集中式IRF设备）

\<Sysname\> system-view

Sysname license activation-key uninstall XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX slot 2

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

Uninstall key: YYYY-YYYY-YYYY-YYYY-YYYY-YYYY-YYYY-YYYY

\# 给成员设备2卸载正式激活码XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX。（分布式设备－IRF模式不支持slot）

\<Sysname\> system-view

Sysname license activation-key uninstall XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX chassis 2

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

Uninstall key: YYYY-YYYY-YYYY-YYYY-YYYY-YYYY-YYYY-YYYY

\# 给成员设备2的1号主控板卸载正式激活码XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX。（分布式设备－IRF模式支持slot）

\<Sysname\> system-view

Sysname license activation-key uninstall XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX chassis 2 slot 1

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

Uninstall key: YYYY-YYYY-YYYY-YYYY-YYYY-YYYY-YYYY-YYYY

【相关命令】

·**display license activation-key**

·**license activation-key install**

**License管理 \-- License管理命令 \-- license compress**

------------------------------------------------------------------------

**[license compress**]命令用来压缩License存储区。

【命令】

集中式设备/分布式设备－独立运行模式不支持slot：

**[license compress**]

分布式设备－独立运行模式支持slot/集中式IRF设备：

**[license compress slot** *slot-number*]

分布式设备－IRF模式不支持slot：

**[license compress chassis** *chassis-number*]

分布式设备－IRF模式支持slot：

**[license compress chassis** *chassis-number* **slot** *slot-number*]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：表示对指定主控板的License存储区进行压缩，主控板将删除无效的License数据，对License存储区空间进行释放，用于安装新的激活信息。*slot-number*表示主控板所在的槽位号。（分布式设备－独立运行模式支持slot）

**[slot** *slot-number*]：表示对指定成员设备的License存储区进行压缩，成员设备将删除无效的License数据，对License存储区空间进行释放，用于安装新的激活信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[chassis ***chassis-number*]：表示对指定成员设备的License存储区进行压缩，将删除无效的License数据，对License存储区空间进行释放，用于安装新的激活信息。*chassis-number*表示设备在IRF中的成员编号。（分布式设备－IRF模式不支持slot）

**[chassis** *chassis-number* **slot** *slot-number*]：表示对指定成员设备上指定主控板的License存储区进行压缩，将删除无效的License数据，对License存储区空间进行释放，用于安装新的激活信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示主控板所在的槽位号。（分布式设备－IRF模式支持slot）

【使用指导】

License存储区空间是有限的。执行该命令后，系统会自动判断各License的状态，将过期和卸载的License以及相关数据删除。从而释放空间，以便用户安装新的License。

需要注意的是，请在执行该命令前，保存各卸载License的卸载码。因为执行该命令后，卸载码会被删除。

【举例】

\# 压缩License存储区。（集中式设备/分布式设备－独立运行模式不支持slot）

\<Sysname\> system-view

Sysname license compress

This command will delete all data relevant to uninstalled and expired keys/licenses, including Uninstall keys, and create a new device ID for activation keys/files.Make sure you have saved the Uninstall keys so you can apply for a new activation key/file for the unexpired licenses that were covered by the uninstalled activation keys/files.

Are you sure you want to continue? [Y/N: Y]

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

\# 给主控板1压缩License存储区。（分布式设备－独立运行模式支持slot）

\<Sysname\> system-view

Sysname license compress slot 1

This command will delete all data relevant to uninstalled and expired keys/licenses, including Uninstall keys, and create a new device ID for activation keys/files.Make sure you have saved the Uninstall keys so you can apply for a new activation key/file for the unexpired licenses that were covered by the uninstalled activation keys/files.

Are you sure you want to continue? [Y/N: Y]

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

\# 给成员设备2压缩License存储区。（集中式IRF设备）

\<Sysname\> system-view

Sysname license compress slot 2

This command will delete all data relevant to uninstalled and expired keys/licenses, including Uninstall keys, and create a new device ID for activation keys/files.Make sure you have saved the Uninstall keys so you can apply for a new activation key/file for the unexpired licenses that were covered by the uninstalled activation keys/files.

Are you sure you want to continue? [Y/N: Y]

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

\# 给成员设备2压缩License存储区。（分布式设备－IRF模式不支持slot）

\<Sysname\> system-view

Sysname license compress chassis 2

This command will delete all data relevant to uninstalled and expired keys/licenses, including Uninstall keys, and create a new device ID for activation keys/files.Make sure you have saved the Uninstall keys so you can apply for a new activation key/file for the unexpired licenses that were covered by the uninstalled activation keys/files.

Are you sure you want to continue? [Y/N: Y]

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

\# 给成员设备2的1号主控板压缩License存储区。（分布式设备－IRF模式支持slot）

\<Sysname\> system-view

Sysname license compress chassis 2 slot 1

This command will delete all data relevant to uninstalled and expired keys/licenses, including Uninstall keys, and create a new device ID for activation keys/files. Make sure you have saved the Uninstall keys so you can apply for a new activation key/file for the unexpired licenses that were covered by the uninstalled activation keys/files.

Are you sure you want to continue? [Y/N: Y]

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

**License管理 \-- License管理命令 \-- license license-key install**

------------------------------------------------------------------------

**[license license-key install**]命令用来安装授权码。

【命令】

集中式设备/分布式设备－独立运行模式不支持slot：

**[license license-key install** *license-key-string*]

分布式设备－独立运行模式支持slot/集中式IRF设备：

**[license license-key install ***license-key-string*** slot** *slot-number*]

分布式设备－IRF模式不支持slot：

**[license license-key install ***license-key-string*** chassis** *chassis-number*]

分布式设备－IRF模式支持slot：

**[license license-key install ***license-key-string*** chassis** *chassis-number* **slot** *slot-number*]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：表示给主控板安装[授权码，主控板安装授权码后，即便插入别的设备，也具有运行相应特性的授权。]*slot-number*表示主控板所在的槽位号。（分布式设备－独立运行模式支持slot）

**[slot** *slot-number*]：表示给成员设备安装[授权码，成员设备安装授权码后，即便加入别的]IRF，也具有运行相应特性的授权。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[chassis ***chassis-number*]：表示给成员设备安装[授权码，成员设备安装授权码后，即便加入别的]IRF，也具有运行相应特性的授权。*chassis-number*表示设备在IRF中的成员编号。（分布式设备－IRF模式不支持slot）

**[chassis** *chassis-number* **slot** *slot-number*]：表示给指定成员设备上的指定主控板安装[授权码，主控板安装授权码后，即便插入别的设备，也具有运行相应特性的授权。]*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示主控板所在的槽位号。（分布式设备－IRF模式支持slot）

****【使用指导】

授权码是用户购买的激活受控特性的凭证。授权码安装到设备上后，对应的特性得到授权，可以正常使用。授权码没有绑定关系，因此一个授权码可以安装到多台设备上。

【举例】

\# 安装授权码XXXXXXXX-(XXXX-)XXXXXXXX-XXXXXXXX-XXXXXXXX。（集中式设备/分布式设备－独立运行模式不支持slot）

\<Sysname\> system-view

Sysname license license-key install XXXXXXXX-(XXXX-)XXXXXXXX-XXXXXXXX-XXXXXXXX

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

\# 给主控板1安装授权码XXXXXXXX-(XXXX-)XXXXXXXX-XXXXXXXX-XXXXXXXX。（分布式设备－独立运行模式支持slot）

\<Sysname\> system-view

Sysname license license-key install XXXXXXXX-(XXXX-)XXXXXXXX-XXXXXXXX-XXXXXXXX slot 1

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

\# 给成员设备2安装授权码XXXXXXXX-(XXXX-)XXXXXXXX-XXXXXXXX-XXXXXXXX。（集中式IRF设备）

\<Sysname\> system-view

Sysname license license-key install XXXXXXXX-(XXXX-)XXXXXXXX-XXXXXXXX-XXXXXXXX slot 2

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

\# 给成员设备2安装授权码XXXXXXXX-(XXXX-)XXXXXXXX-XXXXXXXX-XXXXXXXX。（分布式设备－IRF模式不支持slot）

\<Sysname\> system-view

Sysname license license-key install XXXXXXXX-(XXXX-)XXXXXXXX-XXXXXXXX-XXXXXXXX chassis 2

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

\# 给成员设备2的1号主控板安装授权码XXXXXXXX-(XXXX-)XXXXXXXX-XXXXXXXX-XXXXXXXX。（分布式设备－IRF模式支持slot）

\<Sysname\> system-view

Sysname license license-key install XXXXXXXX-(XXXX-)XXXXXXXX-XXXXXXXX-XXXXXXXX chassis 2 slot 1

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

【相关命令】

·**display license license-key**

·**license license-key uninstall**

**License管理 \-- License管理命令 \-- license license-key uninstall**

------------------------------------------------------------------------

**[license license-key uninstall**]命令用来卸载授权码。

【命令】

集中式设备/分布式设备－独立运行模式不支持slot：

**[license license-key uninstall ***license-key-string*]

分布式设备－独立运行模式支持slot/集中式IRF设备：

**[license license-key uninstall ***license-key-string*** slot** *slot-number*]

分布式设备－IRF模式不支持slot：

**[license license-key uninstall ***license-key-string*** chassis** *chassis-number*]

分布式设备－IRF模式支持slot：

**[license license-key uninstall ***license-key-string*** chassis** *chassis-number* **slot** *slot-number*]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：表示给主控板卸载[授权码，主控板卸载授权码后，将失去此授权码的授权信息，特性将无法获取到卸载的授权码的授权信息。]*slot-number*表示主控板所在的槽位号。（分布式设备－独立运行模式支持slot）

**[slot** *slot-number*]：表示给成员设备卸载[授权码，成员设备卸载授权码后，将失去此授权码的授权信息，特性将无法获取到卸载的授权码的授权信息。]*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[chassis ***chassis-number*]：表示给成员设备卸载[授权码，成员设备卸载授权码后，成员设备将失去此授权码的授权信息，特性模块将无法再获取到此授权码的授权信息。]*chassis-number*表示设备在IRF中的成员编号。（分布式设备－IRF模式不支持slot）

**[chassis** *chassis-number* **slot** *slot-number*]：表示给指定成员设备上的指定主控板安装激活码，主控板安装激活码后，即便插入别的设备，也具有运行相应特性的授权。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示主控板所在的槽位号。（分布式设备－IRF模式支持slot）

【使用指导】

用户确定不再使用受控特性时，可以将授权码卸载，此时对应的特性将不会得到授权，不能使用。

【举例】

\# 卸载授权码XXXXXXXX-XXXX-XXXXXXXX-XXXXXXXX-XXXXXXXX。（集中式设备/分布式设备－独立运行模式不支持slot）

\<Sysname\> system-view

Sysname license license-key uninstall XXXXXXXX-XXXX-XXXXXXXX-XXXXXXXX-XXXXXXXX

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

\# 给主控板1卸载授权码XXXXXXXX-XXXX-XXXXXXXX-XXXXXXXX-XXXXXXXX。（分布式设备－独立运行模式支持slot）

\<Sysname\> system-view

Sysname license license-key uninstall XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX slot 1

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

\# 给成员设备2卸载授权码XXXXXXXX-XXXX-XXXXXXXX-XXXXXXXX-XXXXXXXX。（集中式IRF设备）

\<Sysname\> system-view

Sysname license license-key uninstall XXXXXXXX-XXXX-XXXXXXXX-XXXXXXXX-XXXXXXXX slot 2

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

\# 给成员设备2卸载授权码XXXXXXXX-XXXX-XXXXXXXX-XXXXXXXX-XXXXXXXX。（分布式设备－IRF模式不支持slot）

\<Sysname\> system-view

Sysname license license-key uninstall XXXXXXXX-XXXX-XXXXXXXX-XXXXXXXX-XXXXXXXX chassis 2

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

\# 给成员设备2的1号主控板卸载授权码XXXXXXXX-XXXX-XXXXXXXX-XXXXXXXX-XXXXXXXX。（分布式设备－IRF模式支持slot）

\<Sysname\> system-view

Sysname license license-key uninstall XXXXXXXX-XXXX-XXXXXXXX-XXXXXXXX-XXXXXXXX chassis 2 slot 1

This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...

【相关命令】

·**display license license-key**

·**license license-key install**

