
**帧中继QoS \-- 帧中继QoS配置命令 \-- cir allow**

------------------------------------------------------------------------

**[cir allow**]命令用来配置帧中继虚电路CIR ALLOW（Committed Information Rate ALLOW，允许的承诺信息速率）。

**[undo cir allow**]命令用来恢复缺省情况。

【命令】

**[cir allow**[ [ **inbound** \| **outbound** ] *committed-information-rate*]]

**[undo cir allow**[ [ **inbound** \| **outbound** ]]]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

帧中继类视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[inbound**]：报文入方向所允许的承诺信息速率，本参数仅当接口使能帧中继流量监管时有效。

**[outbound**]：报文出方向所允许的承诺信息速率，本参数仅当接口使能帧中继流量整形时有效。

*[committed-information-rate*]：允许的承诺信息速率，单位为bps。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

允许的承诺信息速率是正常情况下帧中继网络所能提供的发送速率，当网络没有发生拥塞时，它保证用户能够以此速率发送数据。

如果配置时不指定报文方向，则表示同时配置在入方向和出方向上。

【举例】

\# 配置名为test1的帧中继类的CIR ALLOW为64000bps。

\<Sysname\> system-view

Sysname fr class test1

Sysname-fr-class-test1 cir allow 64000

**帧中继QoS \-- 帧中继QoS配置命令 \-- display fr class-map**

------------------------------------------------------------------------

**[display** **fr class-map**]命令用来显示帧中继类与接口以及虚电路的映射关系。

【命令】

**[display**[ **fr** **class-map** [ **fr-class** *class-name* \| **interface** *interface-type interface-number* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[fr-class** *class-name*]：显示指定帧中继类与接口以及虚电路的映射关系。*class-name*表示帧中继类名称，为1～30个字符的字符串，区分大小写。

**[interface** *interface-type interface-number*]：指定接口的类型和编号，可以指定主接口，也可以指定子接口。指定主接口时，显示帧中继类与该主接口及其子接口以及其下的虚电路的映射关系。指定子接口时，显示帧中继类与该子接口及其下的虚电路的映射关系。

【使用指导】

不指定接口和帧中继类名称时，显示所有帧中继类与接口以及虚电路的映射关系。

【举例】

\# 显示接口Serial2/1/0与帧中继类的映射关系。

\<Sysname\> display fr class-map interface serial 2/1/0

Serial2/1/0

  fr-class ts1

  fr dlci 100

    fr-class ts

Serial2/1/0.1

  fr-class ts2

  fr dlci 222

    fr-class ts

\# 显示帧中继类ts与接口的映射关系。

\<Sysname\> display fr class-map fr-class ts

Serial2/1/0

  fr dlci 100

    fr-class ts

Serial2/1/0.1

  fr dlci 222

    fr-class ts

表1-1 display fr class-map命令显示信息描述表

字段

描述

Serial2/1/0

  fr-class ts1

帧中继接口及关联的帧中继类

fr dlci 100

  fr-class ts

帧中继接口下的虚电路及关联的帧中继类

Serial2/1/0.1

  fr-class ts2

帧中继子接口及关联的帧中继类

fr dlci 222

  fr-class ts

帧中继子接口下的虚电路及关联的帧中继类

**帧中继QoS \-- 帧中继QoS配置命令 \-- fr class**

------------------------------------------------------------------------

**[fr class**]命令用来创建帧中继类并进入帧中继类视图。

**[undo fr class**]命令用来删除指定的帧中继类。

【命令】

**[fr class** *class-name*]

**[undo fr class** *class-name*]

【缺省情况】

没有创建帧中继类。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[class-name*]：帧中继类名称，为1～30个字符的字符串，区分大小写。

【使用指导】

·只有将帧中继类同帧中继接口或虚电路相关联，并且使能相应接口的帧中继QoS功能，配置的帧中继类参数才会起作用。

·删除帧中继类时，将释放所有帧中继接口和虚电路与该帧中继类的关联。

【举例】

\# 创建名为test1的帧中继类。

\<Sysname\> system-view

Sysname fr class test1

Sysname-fr-class-test1

【相关命令】

·**fr-class**

**帧中继QoS \-- 帧中继QoS配置命令 \-- fr traffic-shaping**

------------------------------------------------------------------------

**[fr traffic-shaping**]命令用来使能帧中继流量整形功能。

**[undo fr traffic-shaping**]命令用来关闭帧中继流量整形功能。

【命令】

**[fr traffic-shaping**]

**[undo fr traffic-shaping**]

【缺省情况】

帧中继流量整形功能处于关闭状态。

【视图】

帧中继接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

帧中继流量整形功能应用于设备的出接口上，通常应用于帧中继网络的DTE端。

【举例】

\# 在串口Serial2/1/0上使能帧中继流量整形功能。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 fr traffic-shaping

**帧中继QoS \-- 帧中继QoS配置命令 \-- fr-class**

------------------------------------------------------------------------

**[fr-class**]命令用来将帧中继类与当前帧中继接口或虚电路关联起来。

**[undo fr-class**]命令用来取消帧中继类与当前帧中继接口或虚电路的关联。

【命令】

**[fr-class** *class-name*]

**[undo fr-class** *class-name*]

【缺省情况】

帧中继类没有与帧中继接口或虚电路相关联。

【视图】

帧中继接口视图（包括主接口和子接口）/帧中继DLCI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[class-name*]：帧中继类的名称，为1～30个字符的字符串，区分大小写。该帧中继类必须已经存在。

【使用指导】

将一个帧中继类和接口关联起来之后，此接口上的所有虚电路都会继承此帧中继类的帧中继QoS参数。

【举例】

\# 将名为test1的帧中继类与DLCI为200的帧中继虚电路关联起来。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 fr dlci 200

Sysname-Serial2/1/0-fr-dlci-200 fr-class test1

【相关命令】

·**fr class**
