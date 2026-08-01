<!-- CMD-INDEX
  debugging qcn all                   | 用户视图             | L9
  debugging qcn error                 | 用户视图             | L35
  debugging qcn event                 | 用户视图             | L179
  debugging qcn fsm                   | 用户视图             | L237
  debugging qcn packet                | 用户视图             | L301
-->

**QCN \-- QCN调试命令 \-- debugging qcn all**

------------------------------------------------------------------------

【命令】

**[debugging qcn** **all**]

**[undo debugging qcn** **all**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging qcn all**]命令用来打开QCN所有的调试信息开关。**undo debugging qcn all**命令用来关闭QCN所有的调试信息开关。

缺省情况下，QCN所有的调试信息开关处于关闭状态。

**QCN \-- QCN调试命令 \-- debugging qcn error**

------------------------------------------------------------------------

【命令】

**[debugging qcn** **error**]

**[undo debugging qcn** **error**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging qcn error**]命令用来打开QCN错误调试信息开关。**undo debugging qcn error**命令用来关闭QCN错误调试信息开关。

缺省情况下，QCN错误调试信息开关处于关闭状态。

表1-1 debugging qcn error命令输出信息描述表

字段

描述

Failed to set domain *Cnpv* with alternate priority *AlterPri* to driver.

下发驱动，设置优先级为*Cnpv*、隔离优先级为*AlterPri*的域失败

Failed to delete domain *Cnpv* from driver.

删除驱动中优先级为*Cnpv*的域失败

Failed to set the defense mode in domain *Cnpv* on interface *IfName* to driver.

下发驱动，设置接口名为*IfName*、优先级为*Cnpv*的域的保护模式失败

Failed to set profile *profile_id* to driver.

下发驱动，下发profile ID为*profile_id*的profile失败

Failed to delete profile *profile_id* from driver.

删除驱动中profile ID为*profile_id*的profile失败

Failed to bind domain *Cnpv* with profile *profile_id* on interface *IfName* to driver.

下发驱动，在名为*IfName*的接口上建立优先级为*Cnpv*与profile ID为*profile_id*之间的绑定关系失败

Failed to unbind domain *Cnpv* from profile *profile_id* on interface *IfName* to driver.

下发驱动，在名为*IfName*的接口上解除优先级为*Cnpv*与profile ID为*profile_id*之间的绑定关系失败

Failed to notify map table change to driver globally.

下发驱动，通知全局优先级映射表变化信息失败

Failed to notify map table change on interface *IfName* to driver.

下发驱动，通知接口名为*IfName*优先级映射表变化信息失败

Failed to get cp statistics on interface *IfName* with domain *Cnpv* from driver.

从驱动中获取接口名为*IfName*、优先级为*Cnpv*的域的统计信息失败

Failed to clear cp statistics on interface *IfName* with domain *Cnpv* from driver.

清除驱动中接口名为*IfName*、优先级为*Cnpv*的域的统计信息失败

Failed to get capability of interface *IfName* from driver.

从驱动中获取接口名为*IfName*的能力集失败

Failed to start service on slot *slot_id*, and the error code is *ErrCode.*

ID为*slot_id*的板启动失败，错误码为*ErrCode*

【举例】

\# 启动QCN功能，使能LLDP功能，打开QCN错误调试信息开关。

\<Sysname\> debugging qcn error

\*Apr 24 00:56:38:387 2013 Sysname QCN/7/ERROR: -MDC = 1; Failed to set domain *1* with alternate priority *0* to driver.

*// 下发驱动，设置CNPV为1，隔离优先级为0的域信息失败。*

\*Apr 24 00:56:38:387 2013 Sysname QCN/7/ERROR: -MDC = 1; Failed to delete domain *1* from driver.

*// 删除驱动中CNPV为1的域信息失败。*

\*Apr 24 00:56:38:387 2013 Sysname QCN/7/ERROR: -MDC = 1; Failed to set the defense mode in domain *1 on interface* GigabitEthernet0/1/3 to driver.

*// 下发驱动，设置接口名为GE0/1/3，Cnpv为1的域的保护模式失败。*

\*Apr 24 00:56:38:387 2013 Sysname QCN/7/ERROR: -MDC = 1; Failed to set profile *1* to driver.

*// 下发驱动，设置profile ID为1的profile失败。*

\*Apr 24 00:56:38:387 2013 Sysname QCN/7/ERROR: -MDC = 1; Failed to delete profile *1* from driver.

*// 删除驱动中profile ID为1的profile失败。*

\*Apr 24 00:56:38:387 2013 Sysname QCN/7/ERROR: -MDC = 1; Failed to bind domain *1* with profile *2* on interface *GigabitEthernet0/1/3* to driver.

*// 下发驱动，在接口名为GE0/1/3上建立域1和profile ID为2的profile之间的绑定关系失败。*

\*Apr 24 00:56:38:387 2013 Sysname QCN/7/ERROR: -MDC = 1; Failed to unbind domain *1* with profile *2* on interface *GigabitEthernet0/1/3* to driver.

*// 下发驱动，在接口GE0/1/3上解除域1和profile ID为2的profile之间的绑定关系失败。*

\*Apr 24 00:56:38:387 2013 Sysname QCN/7/ERROR: -MDC = 1; Failed to notify map table change to driver globally.

*// 下发驱动，通知全局优先级映射表变化信息失败。*

\*Apr 24 00:56:38:387 2013 Sysname QCN/7/ERROR: -MDC = 1; Failed to notify map table on interface GigabitEthernet0/1/3 change to driver.

*// 下发驱动，通知接口名为GE0/1/3优先级映射表变化信息失败。*

\*Apr 24 00:56:38:387 2013 Sysname QCN/7/ERROR: -MDC = 1;

Failed to get cp statistics on interface *GigabitEthernet0/1/3* with domain *1* from driver.

*// 从驱动中获取接口名为GE0/1/3上域1的cp点统计信息失败。*

\*Apr 24 00:56:38:387 2013 Sysname QCN/7/ERROR: -MDC = 1; Failed to clear cp statistics on interface *GigabitEthernet0/1/3* with domain *1* from driver.

*// 下发驱动，清除接口名为GE0/1/3上域1的cp点统计信息失败。*

\*Apr 24 00:56:38:387 2013 Sysname QCN/7/ERROR: -MDC = 1; Failed to get capability of interface GigabitEthernet0/1/3 from driver.

*// 从驱动中获取接口名为GE0/1/3的能力集失败。*

\*Apr 24 00:56:38:387 2013 Sysname QCN/7/ERROR: -MDC = 1; Failed to start service on slot 1, and the error code is *0x1.*

*[// Slot ID*]*为1的板启动失败，错误码为0x1。*

**QCN \-- QCN调试命令 \-- debugging qcn event**

------------------------------------------------------------------------

【命令】

**[debugging qcn** **event**]

**[undo debugging qcn** **event**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging qcn event**]命令用来打开QCN事件调试信息开关。**undo debugging qcn event**命令用来关闭QCN事件调试信息开关。

缺省情况下，QCN事件调试信息开关处于关闭状态。

表1-2 debugging qcn event命令输出信息描述表

字段

描述

*[EventType*: Received slot insert event. Service started, SlotID=*slot_id*,]，ErrCode= *ErrCode*.

*[EventType*]事件：收到板插入事件。服务启动，板号为*slot_id*，错误码为*ErrCode。*

*[EventType*]为QCN_SLOTEVT（板事件）

*[EventType:*  Map table has been changed.]

*[EventType*]事件：优先级映射表发生改变。

*[EventType*]为QCN_MAPTBLEVT（MAPTBL表变化事件）

【举例】

\# 启动QCN功能，使能LLDP功能，打开QCN事件调试信息开关。

\<Sysname\> debugging qcn event

\*Apr 24 00:56:38:387 2013 Sysname QCN/7/EVENT: -MDC = 1; QCN_SLOTEVT: Received slot insert event. Service started, SlotID=2, ErrCode=0x0.

*// 板事件：收到板插入事件。服务启动，板号为2，错误码为0x0。*

\*Apr 24 00:56:48:387 2013 Sysname QCN/7/EVENT: -MDC = 1; QCN_MAPTBLEVT: Map table has been changed.

*[// MAPTBL*]*表变化事件：优先级映射表发生改变。*

**QCN \-- QCN调试命令 \-- debugging qcn fsm**

------------------------------------------------------------------------

【命令】

**[debugging qcn fsm ** **interface** *interface-type interface-number* ]

**[undo debugging qcn fsm ** **interface** *interface-type interface-number* ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-type* *interface-number*]：指定接口上的调试信息开关。*interface-type* *interface-number*表示接口类型和接口编号。如果未指定本参数，则打开所有二层以太网接口上的调试信息开关。

【描述】

**[debugging qcn fsm**]命令用来打开QCN状态机调试信息开关。**undo debugging qcn fsm**命令用来关闭QCN状态机调试信息开关。

缺省情况下，QCN状态机调试信息开关处于关闭状态。

表1-3 debugging qcn fsm命令输出信息描述表

字段

描述

Received *EventType* event on interface *IfName* with domain *Cnpv*, and the state machine changed from *defense-mode1* state to *defense-mode2* state.

收到*EventType*事件在接口*IfName*上，域为*Cnpv*，状态机的状态从*defense-mode1*切换到*defense-mode2*

·*EventType*包括IF_DEACTIVE（接口去激活）、IF_ACTIVE（接口激活）、ENABLE（全局使能）、DISABLE（全局去使能）、ISSU（不中断业务升级）、SET\_DOMAIN（加入或修改全局域）、DEL\_DOMAIN（退出全局域）、SET\_PORT\_DOMAIN（接口域配置）、DEL\_PORT\_DOMAIN（删除接口域配置）、LLDP\_NOTIFY（LLDP通知事件）

·*Cnpv*范围为0～7

·*defense-mode*包括disabled、interior、interior-ready、edge

【举例】

\# 启动QCN功能，使能LLDP功能，打开QCN状态机调试信息开关。

\<Sysname\> debugging qcn fsm

\<Sysname\> system-view

Sysname qcn priority 1 auto

\*Apr 24 00:56:38:387 2013 Sysname QCN/7/FSM: -MDC = 1; Received SET_DOMAIN event on interface GigabitEthernet0/1/3 with domain 1, and the state machine changed from disabled state to edge state.

*// 接口GigabitEthernet0/1/3，收到加入或修改全局域事件，CNPV值为1的域，状态机从disabled状态切换到edge状态。*

\*Apr 24 00:56:38:395 2013 Sysname QCN/7/FSM: -MDC = 1; Received SET_DOMAIN event on interface Ten-GigabitEthernet0/2/5 with domain 1, and the state machine changed from disabled state to edge state.

*// 接口Ten-GigabitEthernet0/2/5，收到加入或修改全局域事件，CNPV值为1的域，状态机从disabled状态切换到edge状态。*

**QCN \-- QCN调试命令 \-- debugging qcn packet**

------------------------------------------------------------------------

【命令】

**[debugging qcn packet ** **interface** *interface-type interface-number* ]

**[undo debugging qcn packet ** **interface** *interface-type interface-number* ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-type* *interface-number*]：指定接口上的调试信息开关。*interface-type* *interface-number*表示接口类型和接口编号。如果未指定本参数，则打开所有二层以太网接口上的调试信息开关。

【描述】

**[debugging qcn packet**]命令用来打开QCN报文调试信息开关。**undo debugging qcn packet**命令用来关闭QCN报文调试信息开关。

缺省情况下，QCN报文调试信息开关处于关闭状态。

表1-4 debugging qcn packet命令输出信息描述表

字段

描述

On interface *IfName,* LLDP requested CN TLV information on *AgentType* agent, CNPV indicator is *CnpvIndicator,* and ready indicator is *ReadyIndicator.*

在接口名为*IfName*的接口上，LLDP从QCN模块获取CN TLV字段来组装报文，代理类型为*AgentType*，*CnpvIndicator*表明该接口上的哪些dot1p优先级被配置为CNPV，*ReadyIndicator*表明该接口上哪些优先级已经关闭了remap。AgentType包括nearest-bridge（最近桥代理）、nearest-nontpmr（最近非TPMR桥代理）、nearest-customer（最近客户桥代理）

On interface *IfName,* LLDP notified CN TLV information on *AgentType* agent, CNPV indicator is *CnpvIndicator,* and ready indicator is *ReadyIndicator.*

在接口名为*IfName*的接口上收到对端发来的LLDP报文，通知QCN模块 CN TLV字段，代理类型为*AgentType*，*CnpvIndicator*表明对端设备上的哪些dot1p优先级被配置为CNPV，*ReadyIndicator*表明对端设备上哪些优先级已经关闭了remap。AgentType包括nearest-bridge、nearest-nontpmr、nearest-customer

【举例】

\# 启动QCN功能，使能LLDP功能，在接口上配置允许发布CN TLV，打开QCN报文调试信息开关。

\<Sysname\> debugging qcn packet

\*Apr 24 00:56:38:387 2013 Sysname QCN/7/PACKET: -MDC = 1; On interface GigabitEthernet0/1/3, LLDP requested CN TLV information on nearest-bridge agent, CNPV indicator is 0x2, and ready indicator is 0x0.

*// 在接口GigabitEthernet0/1/3上，LLDP从QCN模块获取CN TLV字段来组装报文，代理类型为最近桥模式，表明设备上哪些dot1p优先级被配置为CNPV的指示器为0x2，表明接口上哪些优先级已经关闭了remap的指示器为0x0。*

\*Apr 24 00:56:38:395 2013 Sysname QCN/7/PACKET: -MDC = 1; On interface Ten-GigabitEthernet0/2/5, LLDP requested CN TLV information on nearest-bridge agent, CNPV indicator is 0x2, and ready indicator is 0x0.

*// 在接口Ten-GigabitEthernet0/2/5上，LLDP从QCN模块获取CN TLV字段来组装报文，代理类型为最近桥模式，表明设备上哪些dot1p优先级被配置为CNPV的指示器为0x2，表明接口上哪些优先级已经关闭了remap的指示器为0x0。*

\# 启动QCN功能，使能LLDP功能，打开QCN报文调试信息开关。

\<Sysname\> debugging qcn packet

\*Apr 24 00:56:38:387 2013 Sysname QCN/7/PACKET: -MDC = 1; On interface GigabitEthernet0/1/3, LLDP notified CN TLV information on nearest-bridge agent, CNPV indicator is 0x2, and ready indicator is 0x0.

*// 在接口GigabitEthernet0/1/3上收到LLDP报文，通知QCN模块CN TLV字段，代理类型为最近桥模式，表明设备上哪些dot1p优先级被配置为CNPV的指示器为0x2，表明接口上哪些优先级已经关闭了remap的指示器为0x0。*

\*Apr 24 00:56:38:395 2013 Sysname QCN/7/PACKET: -MDC = 1; On interface Ten-GigabitEthernet0/2/5, LLDP notified CN TLV information on nearest-bridge agent, CNPV indicator is 0x2, and ready indicator is 0x0.

*// 在接口Ten-GigabitEthernet0/2/5上收到LLDP报文，通知QCN模块CN TLV字段，代理类型为最近桥模式，表明设备上哪些dot1p优先级被配置为CNPV的指示器为0x2，表明接口上哪些优先级已经关闭了remap的指示器为0x0。*
