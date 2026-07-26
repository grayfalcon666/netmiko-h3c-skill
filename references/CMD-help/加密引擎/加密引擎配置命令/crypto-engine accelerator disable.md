
**加密引擎 \-- 加密引擎配置命令 \-- crypto-engine accelerator disable**

------------------------------------------------------------------------

**[crypto-engine accelerator disable**]命令用来关闭硬件加密引擎。

**[undo crypto-engine accelerator disable**]命令用来开启硬件加密引擎。

【命令】

**[crypto-engine accelerator disable**]

**[undo crypto-engine accelerator disable**]

【缺省情况】

硬件加密引擎处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【使用指导】

加密引擎包括硬件加密引擎和软件加密引擎两种类型。硬件加密引擎可以是集成在CPU上的协处理器或者硬件加密卡；软件加密引擎指设备上的软件加密算法。

开启硬件加密引擎加密功能，是指开启硬件加密引擎来加速加密过程。

当硬件加密引擎加密功能处于开启状态时，设备会优先选择使用硬件加密引擎对数据进行加密处理，如果硬件加密引擎不支持某种加密算法，则设备会使用软件加密引擎进行加密处理；如果硬件加密引擎加密功能关闭，则设备只能使用软件加密引擎进行加密处理。

硬件加密引擎的开启或关闭状态的改变对业务模块的影响由业务模块决定，例如，对于IPsec业务来说，硬件加密引擎状态的改变只对新建立的IPsec SA有影响，已建的IPsec SA仍旧使用之前选择的加密引擎来处理。因此，建议在开启或关闭硬件加密引擎之后，使用**reset ipsec sa**命令将当前已有的IPsec SA删除，使得所有新建立的IPsec SA都将使用新选择的加密引擎处理流程来处理。

硬件加密引擎加密功能仅允许在测试、调试或故障排除的环境下关闭，正常情况下不建议关闭该功能。

【举例】

\# 关闭硬件加密引擎。

\<Sysname\> system-view

Sysname **crypto-engine accelerator disable**

**加密引擎 \-- 加密引擎配置命令 \-- display crypto-engine**

------------------------------------------------------------------------

**[display crypto-engine**]命令用来显示加密引擎的基本信息，包括各个加密引擎的名称、支持的算法能力等信息。

【命令】

**[display crypto-engine**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

若设备没有硬件加密引擎，则只会显示软件加密引擎信息。

【举例】

\# 显示加密引擎的基本信息。

\<Sysname\> display crypto-engine

  Crypto engine name: cavium crypto driver

  Crypto engine state: Enabled

  Crypto engine type: Hardware

  Slot ID: 0

  CPU ID：0

  Crypto engine ID: 0

  Symmetric algorithms: des-ecb 3des-cbc 3des-ecb aes-cbc aes-ecb aes-ctr camellia_cbc sha1 sha2-256 sha2-384 sha2-512 md5-hmac sha1hmac sha2-256-hmac sha2-384-hmac sha2-512-hmac

  Asymmetric algorithms: dh-group1 dh-group2 dh-group5 dh-group14 dh-group24

  Random number generation function: Supported

  Crypto engine name: Software crypto engine

  Crypto engine state: Enabled

  Crypto engine type: Software

  Slot ID: 0

  CPU ID：0

  Crypto engine ID: 1

  Symmetric algorithms: des-cbc des-ecb 3des-ecb aes-ecb sha1 sha2-256 sha1-hmac sha2-256-hmac

  Asymmetric algorithms:

  Random number generation function: Supported

\# 显示加密引擎的基本信息。（设备上无硬件加密引擎的情况）

\<Sysname\> display crypto-engine

  Crypto engine name: Software crypto engine

  Crypto engine state: Enabled

  Crypto engine type: Software

  Slot ID: 0

  CPU ID：0

  Crypto engine ID: 0

  Symmetric algorithms: des-cbc des-ecb 3des-ecb aes-ecb sha1 sha2-256 sha1-hmac sha2-256-hmac

  Asymmetric algorithms:

  Random number generation function: Supported

表1-1 display crypto-engine命令显示信息描述表

字段

描述

Crypto engine name

加密引擎名称

Crypto engine state

加密引擎的状态，对于不同类型的加密引擎状态不同

对于硬件加密引擎，包括以下两种：

·Enabled：已开启

·Disable：关闭

对于软件加密引擎，只包含以下一种：

·Enabled：已开启

Crypto engine type

加密引擎的类型，包括以下两种：

·Hardware：硬件

·Software：软件

Slot ID

加密引擎所在的接口板编号

CPU ID

单板上的CPU编号

Crypto engine ID

加密引擎ID号

Symmetric algorithms

支持的对称加密算法

Asymmetric algorithms

支持的非对称加密算法

Random number generation function

是否支持获取随机数的功能

·Supported：支持

·Not supported：不支持

【相关命令】

·**crypto-engine accelerator disable**

**加密引擎 \-- 加密引擎配置命令 \-- display crypto-engine statistics**

------------------------------------------------------------------------

**[display crypto-engine statistics**]命令用来显示加密引擎的统计信息，包括建立会话的个数，加密引擎处理的报文数等信息。

【命令】

集中式设备：

**[display crypto-engine statistics ** **engine-id** *engine-id* ]

分布式设备---独立运行模式/集中式IRF设备：

**[display crypto-engine statistics** [ **engine-id** *engine*-*id* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备---IRF模式：

**[display crypto-engine statistics** [ **engine-id** *engine*-*id* **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[engine-id*** engine-id*]：显示指定加密引擎的统计信息，*engine-id*为加密引擎ID编号，取值范围与设备的型号有关，请以设备的实际情况为准。

**[slot ***slot-number*]：显示指定单板上的加密引擎统计信息，*slot-number*表示单板所在槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备上的加密引擎统计信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX上的加密引擎统计信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的加密引擎统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：显示指定指定单板的加密引擎统计信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的加密引擎统计信息，*cpu-number*表示单板上的CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

如果未开启硬件加密引擎或者设备上没有硬件加密引擎，则只会显示软件加密引擎的统计信息。

·若不指定任何参数，则显示所有加密引擎统计信息。（集中式设备）

·若不指定任何参数，则显示所有单板的上的加密引擎统计信息。（分布式设备－独立运行模式）

·若不指定任何参数，则显示所有成员设备上的加密引擎统计信息。（集中式IRF设备）（不支持IRF3的设备）

·若不指定任何参数，则显示所有成员设备/PEX上的加密引擎统计信息。（集中式IRF设备）（支持IRF3的设备）

·若不指定任何参数，则显示所有所有单板上的加密引擎统计信息。（分布式设备－IRF模式）

【举例】

\# 显示所有加密引擎统计信息。

\<Sysname\> display crypto-engine statistics

  Submitted sessions: 0

  Failed sessions: 0

  Symmetric operations: 0

  Symmetric errors: 0

  Asymmetric operations: 0

  Asymmetric errors: 0

  Get-random operations: 0

  Get-random errors: 0

\# 显示2号单板上加密引擎号为1的加密引擎统计信息。（分布式设备－独立运行模式）

\<Sysname\> display crypto-engine statistics engine-id 1 slot 2

  Submitted sessions: 0

  Failed sessions: 0

  Symmetric operations: 0

  Symmetric errors: 0

  Asymmetric operations: 0

  Asymmetric errors: 0

  Get-random operations: 0

  Get-random errors: 0

\# 显示2号成员设备上加密引擎号为1的加密引擎统计信息。（集中式IRF设备）

\<Sysname\> display crypto-engine statistics engine-id 1 slot 2

  Submitted sessions: 0

  Failed sessions: 0

  Symmetric operations: 0

  Symmetric errors: 0

  Asymmetric operations: 0

  Asymmetric errors: 0

  Get-random operations: 0

  Get-random errors: 0

\# 显示1号成员设备上2号单板的加密引擎号为1的加密引擎统计信息。（分布式设备－IRF模式）

\<Sysname\> display crypto-engine statistics engine-id 1 chassis 1 slot 2

  Submitted sessions: 0

  Failed sessions: 0

  Symmetric operations: 0

  Symmetric errors: 0

  Asymmetric operations: 0

  Asymmetric errors: 0

  Get-random operations: 0

  Get-random errors: 0

表1-2 display crypto-engine statistics命令显示信息描述表

字段

描述

Submitted sessions

已创建的会话数目

Failed sessions

创建失败的会话数目

Symmetric operations

加密引擎使用对称算法的操作次数

Symmetric errors

加密引擎使用对称算法操作失败的次数

Asymmetric operations

加密引擎使用非对称算法操作的次数

Asymmetric errors

加密引擎使用非对称算法操作失败的次数

Get-random operations

加密引擎获取随机数操作的次数

Get-random errors

加密引擎获取随机数操作失败的次数

【相关命令】

**[reset crypto-engine statistics**]

**加密引擎 \-- 加密引擎配置命令 \-- reset crypto-engine statistics**

------------------------------------------------------------------------

**[reset crypto-engine statistics**]命令用来清除加密引擎的统计计数。

【命令】

集中式设备：

**[reset crypto-engine statistics ** **engine-id** *engine-id* ]

分布式设备---独立运行模式/集中式IRF设备：

**[reset crypto-engine statistics ** **engine-id** *engine***-***id* **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备---IRF模式：

**[reset crypto-engine statistics** [ **engine-id** *engine***-***id* **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[engine-id*** engine-id*]：清除指定加密引擎的统计信息，*engine-id*为加密引擎ID编号，取值范围与设备的型号有关，请以设备的实际情况为准。

**[slot ***slot-number*]：清除指定单板上的加密引擎统计信息，*slot-number*表示单板所在槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：清除指定成员设备上的加密引擎统计信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：清除指定成员设备/PEX上的加密引擎统计信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-numbe*]：清除指定成员设备上指定单板的加密引擎统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-numbe*]：清除指定单板上的加密引擎统计信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：清除指定CPU上的加密引擎统计信息，*cpu-number*表示单板上的CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·若不指定任何参数，则清除所有加密引擎统计信息。（集中式设备）

·若不指定任何参数，则清除所有单板的上的加密引擎统计信息。（分布式设备－独立运行模式）

·若不指定任何参数，则清除所有成员设备上的加密引擎统计信息。（集中式IRF设备）（不支持IRF3的设备）

·若不指定任何参数，则清除所有成员设备/PEX上的加密引擎统计信息。（集中式IRF设备）（支持IRF3的设备）

·若不指定任何参数，则清除所有单板上的加密引擎统计信息。（分布式设备－IRF模式）

【举例】

\# 清除加密引擎的统计信息。

\<Sysname\> reset crypto-engine statistics

【相关命令】

·**display crypto-engine statistics**

