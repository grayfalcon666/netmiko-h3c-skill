<!-- CMD-INDEX
  debugging rmon                      | 用户视图             | L5
-->

**RMON \-- RMON调试命令 \-- debugging rmon**

------------------------------------------------------------------------

【命令】

**[debugging rmon**[ { **all** \| **error** \| **event** }]]

**[undo debugging rmon **[{ **all** \| **error** \| **event** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示RMON所有调试信息开关。

**[error**]：表示RMON错误调试信息开关。

**[event**]：表示RMON事件调试信息开关。

【描述】

**[debugging rmon**]命令用来打开RMON调试信息开关。**undo debugging rmon**命令用来关闭RMON调试信息开关。

缺省情况下，RMON调试信息开关处于关闭状态。

表1-1 debugging rmon error命令输出信息描述表

字段

描述

*[modulename* entry *index*: failed to create aging timer]

模块创建表项的老化定时器失败

*[modulename*]：模块名，可取Hist、Event、Prialarm、Usrhist、Stats

*[index*]：表项索引

*[modulename* entry *index*: failed to sample on slot *slotid*]

模块采样失败

*[modulename*]：模块名，可取Hist、Stats

*[index*]：表项的索引

*[slotid*]：采样所在槽号

*[modulename* module: failed to init]

模块初始化失败

*[modulename*]：模块名，可取Alarm、Stats、Usrhist、Event、Hist、Prialarm、Dbm、Epoll、Timer

*[modulename* module: failed to recover]

模块配置恢复失败

*[modulename*]：模块名，可取Alarm、Event、Stats、Hist、Prialarm、Usrhist

*[modulename* entry *index*: calloc failed]

模块创建表项时分配内存失败

*[modulename*]：模块名，可取Event、Stats、Hist、Prialarm、Alarm、Usrhist

*[index*]：表项索引

*[modulename* entry *index*: failed to create sampling timer]

模块创建表项的采样定时器失败

*[modulename*]：模块名，可取Hist、Prialarm、Alarm、Usrhist

*[index*]：表项的索引

*[modulename* sample entry *index*- *sampleindex*: calloc failed]

模块创建采样数据表项时分配内存失败

*[modulename*]：模块名，可取Hist

*[index*]：表项的索引

*[sampleindex*]：采样索引

*[modulename* entry *index*: sampling failed]

表项定时采样失败

*[Modulename*]：模块名，可取Alarm、Prialarm

*[Index*]：表项索引

*[modulename *module: illegal OID type ]

模块创建或修改表项时OID类型非法

*[modulename*]：模块名，可取Alarm、Prialarm

Prialarm module: failed to process *state-name* parse state

扩展告警表解析表达式时处理状态失败

*[state-name*]：状态名称，可以取OID、INIT、NUM、SCAN、OPERATOR、FINISH

Prialarm module: failed to calloc OID memory

扩展告警表解析表达式时分配oid内存失败

*[modulename* module: illegal NUM characters]

表达式中含有非法格式的数字字符

*[Modulename*]：模块名，可取Prialarm

Prialarm module: illegal bracket

扩展告警表的表达式含有非法的括号

Prialarm module: zero divider

用户将0作为除数下发给扩展告警表的表达式

Prialarm module: fail to calloc exp-stack

扩展告警表创建表达式栈失败

Prialarm module: exp-stack overflow

扩展告警表表达式栈溢出

Log entry *index --logIndex*: calloc failed

创建事件日志表项时分配内存失败

*[index*]：事件表项的索引

*[logindex*]：日志表项的索引

Usrhist entry *index*: failed to calloc OID

用户历史控制表项采样时获取采样OID时分配内存失败

*[index*]：用户历史控制表项的索引

Object entry *index-objectindex*: *calloc failed*

创建索引为*index*的用户历史控制表项的第*objectindex*个用户历史对象表项时分配内存失败

*[index*]：用户历史控制表项的索引

*[objectindex*]：用户历史对象表项的索引

Usrhist sample *entry index-sampleindex-objectindex*: calloc failed

创建索引为*index*的用户历史控制表项的第*objectindex*个用户历史对象表项的第*sampleindex*个用户历史数据表项时分配内存失败

*[index*]：用户历史控制表项的索引

*[sampleindex*]：用户历史数据表采样次数

*[objectindex*]：用户历史对象表项的索引

Sync module: failed to get global slot

获取全局槽号失败

Sync module: failed to register epoll

Sync模块注册epoll失败

表1-2 debugging rmon event命令输出信息描述表

字段

描述

*[modulename* entry *index*: set same configuration]

对表项下发了相同配置

*[modulename*]：模块名，可取Alarm、Event、Stats、Hist、Prialarm、Usrhist

*[index*]：表项索引

*[modulename* entry *index*: aging timer started]

表项开始老化

*[modulename*]： 统计表模块名，可取Event、Stats、Hist、Prialarm、Usrhist

*[index*]：统计表项索引

*[modulename* entry *index*: the entry has been valid]

表项已经处于激活状态

*[modulename*]：模块名，可取Alarm、Event、Stats、Hist、Prialarm、Usrhist

*[index*]：表项索引

*[modulename* entry *index*: start sampling ]

表项触发采样

*[modulename*]：模块名，可取Alarm、Hist、Prialarm、Usrhist

*[index*]：表项索引

*[modulename* entry *index*: the entry does not exist or different sample-id]

表项不存在或采样标记sample Id不一致

*[modulename*]： 模块名，可取Alarm、Hist、Prialarm、Usrhist

*[index*]：表项索引

*[modulename* entry *index*: created no-loop timer-id *timerid*]

模块创建一个非循环定时器

*[modulename*]：模块名，可取Alarm、Hist、Prialarm、Usrhist

*[timerid*]：非循环定时器ID

Alarm entry *index*: sample reverse or first sample

索引为*index*的告警表项采样翻转或第一次采样

*[index*]：告警表项索引

*[modulename* entry *index*: set to valid]

表项被配置为生效状态

*[modulename*]：模块名，可取Alarm、Prialarm

*[index*]：表项的索引

Usrhist sample entry *index-sampleindex-objectindex*: sample reverse

用户历史表采样数据发生反转

*[Index*]：用户历史控制表项索引

*[Sampleindex*]：用户历史数据表采样次数

*[Objectindex*]：用户历史对象表项索引

Failed to start daemon in chass-id *chassid* slot-id *slotid*

启动框号为*chassid*槽号为*slotid*上的rmon进程失败

*[chassid*]：框号

*[slotid*]：槽号

Interface *interfacename* activated

*[interfacename*]的接口激活

Interface *interfacename* deactivated

*[interfacename*]的接口去激活

Interface *interfacename* deleted

*[interfacename*]的接口删除

Timer id is invalid

删除一个无效的定时器

*[timerType* timer has *timerCount* timer instances]

拥有*timerCount*个*timetype*类型的定时器

*[Timetype*]：老化定时器(0)，OID采样定时器(1)，驱动采样定时器(2)

*[timerCount*]：定时器个数

SYNC module accepted new connection(GSlot=*gSlotNo*,Slot=*SlotNo*,Socket=*socketId*)

LLIPC模块接受来自全局槽号为*gSlotNo*，局部槽号为*SlotNo*的*socketId*的连接请求

*[gSlotNo*]：全局槽号

*[SlotNo*]：局部槽号

*[socketId*]：连接的socket id

【举例】

\# 打开RMON事件调试信息开关，配置历史组。

\<Sysname\> debugging rmon event

*[//*]*新创建历史表项，系统输出相应调试信息*

Sysname rmon alarm 1 1.3.6.1.2.1.6.3.0 5 absolute rising-threshold 100 1 falling-threshold 20 1

\*Jun 30 16:53:29:403 2012 H3C RMON/7/EVENT: Alarm entry index 1: set to valid

*[//*]*新创建历史控制表项后，对监控接口进行开始第一次采样，输出相应调试信息*

Sysname-Ethernet1/0/2 rmon history 1 buckets 5 interval 5 owner h3c

\*Jun 30 16:53:29:403 2012 H3C RMON/7/EVENT:Hist entry index 1: start sampling

