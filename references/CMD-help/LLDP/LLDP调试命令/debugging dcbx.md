
**LLDP \-- LLDP调试命令 \-- debugging dcbx**

------------------------------------------------------------------------

【命令】

**[debugging**[ **dcbx** { **all** \| **error** \| **event** } [ **interface** *interface-type interface-number* ]]]

**[undo**[ **debugging** **dcbx** { **all** \| **error** \| **event** } [ **interface** *interface-type interface-number* ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示DCBX的所有调试信息开关。

**[error**]：表示DCBX错误调试信息开关。

**[event**]：表示DCBX事件调试信息开关。

**[interface** *interface-type interface-number*]：打开或关闭指定端口上的相关调试信息开关，*interface-type interface-number*表示端口类型和端口编号。如果未指定该参数，将打开或关闭所有端口上的相关调试信息开关。

【描述】

**[debugging dcbx**]命令用来打开DCBX调试信息开关。**undo debugging dcbx**命令用来关闭DCBX调试信息开关。

缺省情况下，DCBX调试信息开关处于关闭状态。

表1-1 debugging dcbx error命令输出信息描述表

字段

描述

Failed to get local data

获取本地运行参数失败

Failed to parse DCBX Control Sub-TLV

解析DCBX Control Sub-TLV失败

Failed to update remote data by remote TLV(sym)

通过远端TLV更新远端运行参数失败（对称状态机）

Failed to update local data by local configuration(sym)

通过本端配置更新本地运行参数失败（对称状态机）

Failed to update local data by remote TLV(sym)

通过远端TLV更新本端运行参数失败（对称状态机）

Failed to update local data by remote data(Asy)

通过远端数据更新本端运行参数失败（非对称状态机）

Failed to get DCBX data from remote TLV

从远端TLV获取DCBX数据失败

Failed to malloc for getting local DCBX data

获取本地DCBX数据时分配内存失败

Failed to make TLV for buffer overflow

缓冲区溢出时构建TLV失败

Failed to update local data (comm)

更新本地数据失败（普通状态机）

Failed to update remote data by remote TLV(comm)

通过远端TLV失败更新远端运行（普通状态机）

Failed to update remote data by remote TLV(asy)

通过远端TLV失败更新远端运行（非对称状态机）

Failed to update local data for malloc failed

内存申请失败导致更新本端运行参数失败

Failed to get the queue scheduling of local precedence

获取本地优先级队列信息失败

Failed to get local configuration for malloc failed(ETS)

内存分配失败导致获取本地配置失败

Failed to malloc for getting local PDCBX data

获取PDCBX本地数据时内存申请失败

Failed to update local data

更新本地运行参数失败

Failed to get PDCBX CB for making TLV

构造TLV时获取PDCBX控制块失败

Failed to malloc for getting local PFC data

获取本地PFC数据时内存申请失败

Failed to update databy local data(pre)

通过本端数据更新运行参数失败（预标准）

Failed to update remote data by remote TLV(pre)

通过远端TLV更新远端运行参数失败（预标准）

Failed to update local data by remote TLV(pre)

通过远端TLV更新本端运行参数失败（预标准）

PDCBX TLV length is invalid

PDCBX TLV长度非法

The version of received DCBX TLV is not supported

本端不支持收到的DCBX TLV版本

Failed to get PDCBX CB for parsing TLV

解析TLV时获取PDCBX控制块失败

Failed to handle interface-up/interface-down event for no CB found

获取PDCBX控制块失败导致接口up/down事件处理失败

Failed to save remote data TLV

保存远端TLV信息失败

Unknown State Machine Type

无法识别的状态机类型

Failed to update DCBX version

更新DCBX版本失败

Unknown DCBX version TLV received

接收到未知DCBX版本的TLV

DCBX version in TLV is not equal to current version

TLV中的DCBX版本不等于当前的版本

APP data space is not enough

APP的数据空间不足

APP data length is incorrect

APP的数据长度错误

APP data format is incorrect

APP的数据模式错误

APP data is reduplicate

APP的数据信息出现了重复

Protocol ID is illegal

协议ID不合法

App TLV data length is incorrect

APP TLV数据长度错误

App TLV data length is not a multiple of 3

APP TLV数据长度不是3的倍数

The LP is *value*,Dot1p is *value*, LP is incorrect

LP不正确

The scheduling algorithm of queue LP *value* is *algorithm*

LP的队列调度算法

ETS TLV data length is incorrect

ETS TLV长度错误

The priority of ETS TLV is invalid

ETS TLV的优先级无效

The sum of bandwidth of ETS TLV is not 100%

ETS TLV的总带宽不是100％

Failed to get local standard DCBX data

获取本端标准DCBX数据错误

Failed to update *name* standard data for malloc failed

内存申请失败导致更新标准数据失败

Failed to update *name* standard data while updating data

更新数据失败

Failed to update standard local data for malloc failed

内存申请失败导致更新本地标准数据失败

Priority flow control is not in auto mode

PFC没有配置成自动模式

The length of PFC TLV is not enough

PFC TLV的长度不足

PFC TLV length is error

PFC长度错误

PFC capability value is error

PFC能力值错误

Failed to get PFC work mode

获取PFC工作模式失败

The PFC work mode is invalid(work mode = *mode*)

PFC的工作模式无效

Failed to get PFC enabled table

PFC开启表获取失败

表1-2 debugging dcbx event命令输出信息描述表

字段

描述

Local data is not updated(sym)

本地运行参数未更新（对称状态机）

Changed flag is not set(sym)

未设置变动标志位（对称状态机）

Driver is not set by remote TLV(sym)

配置参数已通过远端TLV更新，未设置驱动（对称状态机）

Driver is not set by remote TLV(asy)

未通过远端TLV设置驱动（非对称状态机）

DCBX-data is not set to driver for getting cfg-data failed

获取配置数据失败，未设置驱动

PDCBX version changed to *version*

PDCBX版本切换至*version*

Local peer data changed

本地运行参数改变

Changed flag is not set (std)

未设置变动标志位（标准类型）

Current version is *version*

当前版本类型

Current state machine is *state*

当前状态机类型

DCBX version changed from *version* to *version*

DCBX版本切换

Process DCBX neighbor delete event

处理DCBX邻居删除事件

There is no DCBX TLV in message

消息中无DCBX TLV

The TSA Table of ETS TLV is unknown

ETS TLV中的TSA表不识别

Source data is equal to destination data for ETS Recommendation TLV

ETS RecommendationTLV源数据等于目的数据

Source data is not equal to destination data for ETS Recommendation TLV

ETS RecommendationTLV源数据不等于目的数据

Update local ETS Recommendation TLV successfully

更新本端ETS Recommendation TLV成功

Update remote ETS Recommendation TLV successfully

更新远端ETS Recommendation TLV成功

There is no DCBX ETS Recommendation TLV in message

消息中无DCBX ETS Recommendation TLV

There is no DCBX PFC Configuration TLV in message

消息中无DCBX ETS Configuration TLV

Update local PFC TLV successfully

更新本地PFC TLV成功

Update remote PFC TLV successfully

更新远端PFC TLV成功

【举例】

\# 设备通过端口GigabitEthernet1/0/1与另一台设备相连，在本设备上打开DCBX事件调试信息开关。

\<Sysname\> debugging dcbx event

\*Mar 23 14:38:34:266 2010 Sysname DCBX/7/EVENT: PDCBX version changed to 1.

*[// PDCBX*]*版本切换至1.00版本*

**LLDP \-- LLDP调试命令 \-- debugging lldp**

------------------------------------------------------------------------

【命令】

**[debugging lldp**[ { **all** \| **error** \| **event** \| **fsm** [ **interface** *interface-type interface-number* ] \| **packet** [ **receive** \| **send** ]  **interface** *interface-type interface-number*   **verbose**  }]]

**[undo debugging lldp**[ { **all** \| **error** \| **event** \| **fsm** [ **interface** *interface-type interface-number* ] \| **packet** [ **receive** \| **send** ]  **interface** *interface-type interface-number*  }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示LLDP的所有调试信息开关。

**[error**]：表示LLDP错误调试信息开关。

**[event**]：表示LLDP事件调试信息开关。

**[fsm**]：表示LLDP状态机调试信息开关。

**[packet**]：表示LLDP报文调试信息开关。

**[receive**]：表示LLDP接收报文调试信息开关。

**[send**]：表示LLDP发送报文调试信息开关。

**[interface** *interface-type interface-number*]：打开或关闭指定端口上的相关调试信息开关，*interface-type interface-number*表示端口类型和端口编号。如果未指定该参数，将打开或关闭所有端口上的相关调试信息开关。

**[verbose**]：表示LLDP报文的详细调试信息开关。

【描述】

**[debugging lldp**]命令用来打开LLDP调试信息开关。**undo debugging lldp**命令用来关闭LLDP调试信息开关。

缺省情况下，LLDP调试信息开关处于关闭状态。

表1-3 debugging lldp error命令输出信息描述表

字段

描述

The packet is too short

报文长度过短

The packet is too long

报文长度过长

TLV exceeds end of the frame, type: *type*

TLV长度超过报文物理总长度，TLV的类型为*type*

End TLV length error

End of LLDPDU TLV长度错误

Chassis ID TLV length error

Chassis ID TLV长度错误

Chassis ID TLV MAC length error

Chassis ID TLV子类型为MAC地址的长度错误

Receive repeated chassis ID TLV

收到的报文中含有重复的Chassis ID TLV

Chassis ID TLV subtype error

Chassis ID TLV子类型非法

Port ID TLV length error

Port ID TLV长度错误

Port ID TLV MAC length error

Chassis ID TLV子类型为MAC地址的长度错误

Receive repeated port ID TLV

收到的报文中含有重复的Port ID TLV

Port ID TLV subtype error

Port ID TLV子类型非法

TTL TLV length error

Time to Live TLV长度错误

Receive repeated TTL TLV

收到的报文中含有重复的Time to Live TLV

Receive repeated Port Description TLV

收到的报文中含有重复的Port Description TLV

Receive repeated System Name TLV

收到的报文中含有重复的System Name TLV

Receive repeated System Description TLV

收到的报文中含有重复的System Description TLV

Receive repeated System Capabilities TLV

收到的报文中含有重复的System Capabilities TLV

System Capabilities TLV length error

System Capabilities TLV长度错误

System Capability TLV conflict: Support: 0x%x, Enable: 0x%x

System Capabilities TLV信息错误，支持能力为0x%x与开启能力为0x%x相矛盾

System Capability TLV station-only error: 0x%x

System Capabilities TLV信息错误，表示支持功能的第七位置位，且仍有其它有效置位

Receive repeated Management Address TLV

收到的报文中含有重复的Management Address TLV

Management Address TLV total length error

Management Address TLV总长度错误

Management Address TLV address length error

Management Address TLV管理地址长度错误

Management Address TLV conflict error

Management Address TLV解析出的长度和总长度相矛盾

Management Address TLV OID length error

Management Address TLV OID长度错误

Management Address TLV subtype error

Management Address TLV子类型非法

Management Address TLV if subtype error

Management Address TLV接口子类型非法

Management Address TLV format conflict

Management Address TLV本端封装格式与接收到的封装格式不一致

Management Address TLV IPv4 address error

Management Address TLV IPv4地址错误

Port VLAN ID TLV length error

Port VLAN ID TLV长度错误

Receive repeated Port VLAN ID TLV

收到的报文中含有重复的Port VLAN ID TLV

Port VLAN ID TLV VLAN IDerror

Port VLAN ID TLV的VLAN ID错误

Port And Protocol VLAN ID TLV length error

Port And Protocol VLAN ID TLV长度错误

Port And Protocol VLAN ID TLV VLAN ID error

Port And protocol VLAN ID TLV的VLAN ID错误

Receive repeated Port And Protocol ID VLAN TLV

收到的报文中含有重复的Port And Protocol VLAN ID TLV

VLAN Name TLV length error

VLAN Name TLV长度错误

Vlan Name string length error

VLAN Name TLV的VLAN名称长度错误

Vlan Name TLV VLAN ID error

VLAN Name TLV的VLAN ID错误

Receive repeated VLAN Name TLV

收到的报文中含有重复的VLAN Name TLV

Protocol Identity TLV length error

Protocol Identity TLV长度错误

Receive repeated Protocol Identity TLV

收到的报文中含有重复的Protocol Identity TLV

MAC/ PHY Configuration/Status TLV length error

MAC/PHY Configuration/Status TLV长度错误

Receive repeated MAC/PHY Configuration/Status TLV

收到的报文中含有重复的MAC/PHY Configuration/Status TLV

MAC/PHY Configuration/Status TLV MAU type error

MAC/PHY Configuration/Status TLV中端口支持MAU类型非法

Power via MDI TLV length error

Power via MDI TLV长度错误

Receive repeated power via MDI TLV

收到的报文中含有重复的power via MDI TLV

Power via MDI TLV power pair error

Power via MDI TLV中power pair值错误

Power via MDI TLV power class error

Power via MDI TLV中power class值错误

Power via MDI TLV PD requested power value error

Power via MDI TLV中PD requested power value值错误

Power via MDI TLV PSE allocated power value error

Power via MDI TLV中PSE allocated power value值错误

Link Aggregation TLV length error

Link Aggregation TLV长度错误

Link Aggregation TLV member port ID error

Link Aggregation TLV中聚合成员端口ID错误

Receive repeated Link Aggregation TLV

收到的报文中含有重复的Link Aggregation TLV

Max Frame Size TLV length error

Max Frame Size TLV长度错误

Receive repeated Max Frame Size TLV

收到的报文中含有重复的Max Frame Size TLV

Power Stateful Control TLV or EEE TLV length error

Power Stateful Control TLV或者EEE TLV长度错误

Receive repeated Power Stateful Control or EEE TLV

收到的报文中含有重复的Power Stateful Control TLV或者EEE TLV

Power Stateful Control TLV type error

Power Stateful Control TLV中type信息错误

Power Stateful Control TLV source error

Power Stateful Control TLV中source信息错误

Power Stateful Control TLV priority error

Power Stateful Control TLV中priority信息错误

MED capabilities TLV length error

LLDP-MED Capabilities TLV长度错误

Receive repeated MED capabilities TLV

收到的报文中含有重复的LLDP-MED Capabilities TLV

MED capability TLV cap error

LLDP-MED Capabilities TLV中支持capabilities TLV的未置位

MED capability TLV device type error

LLDP-MED Capabilities TLV中支持pse和pd扩展MDI TLV标志均置位

MED capability TLV MED class error

LLDP-MED Capabilities TLV中表示设备类型的值非法

MED network policy TLV conflict with MED capability

MED capability不支持发送Network policy TLV

MED network policy TLV length error

Network Policy TLV长度错误

Receive repeated Network Policy TLV, type: *type*

收到的报文中含有重复的类型为*type*的Network Policy TLV

Receive repeated Network Policy unknown TLV

收到的报文中含有重复的类型未知的Network Policy TLV

MED power MDI TLV conflict with MED capability

MED capability不支持发送MED power MDI TLV

MED power MDI TLV length error

MED power MDI TLV长度错误

Receive repeated MED power MDI TLV

收到的报文中含有重复的MED power MDI TLV

MED power MDI TLV type error

MED power MDI TLV信息中power type位段非法

MED power MDI TLV PSE(PD) type error

MED power MDI TLV信息中表示power type位段与MED capability中不一致，不同为pse或者pd

MED power MDI TLV PSE source error

MED power MDI TLV信息中表示power source的位段的值非法

MED power MDI TLV PSE(PD) priority error

MED power MDI TLV信息中表示power priority的位段的值非法

MED power MDI TLV power value error

MED power MDI TLV信息中表示power value的位段的值非法

MED location ID TLV length error

Location Identification TLV长度错误

MED location ID TLV LCI length error

Location Identification TLV LCI长度错误

MED location ID TLV format error

Location Identification TLV格式错误

Receive repeated Location ID TLV, format: *format*

收到的报文中含有重复的类型为*format*的Location Identification TLV

MED Location TLV conflict with MED capability

MED capability不支持发送Location Identification TLV

MED Inventory TLV length error

MED inventory TLV长度错误

MED Inventory TLV conflict with MED capability

MED capability不支持发送Inventory TLV

Receive repeated MED Inventory TLV

收到的报文中含有重复的Inventory TLV

Failed to update neighbor information

更新邻居信息失败

No chassis ID TLV

没有Chassis ID TLV

No port ID TLV

没有Port ID TLV

No TTL TLV

没有Time to Live TLV

Dropped neighbor because of too many neighbors

由于邻居过多而丢弃邻居

Failed to get port ID

获取Port ID失败

Failed to create gcb save timer

创建定时保存定时器失败

Failed to create Interface Data

创建接口数据失败

Failed to delete configure data from DBM

主控板删除DBM配置数据失败

Failed to set interface statistic data to DBM

保存接口统计数据到DBM失败

Failed to register interface event

注册接口事件失败

Failed to receive event packet

接收事件报文失败

Failed to create neighbor aging timer

创建邻居老化定时器失败

Failed to send message

发包失败

Failed to refresh timer

刷新定时器失败

Failed to announce timer

通知定时器处理失败

VLAN name string is too long

VLAN名称的长度过长

Failed to send nearest customer packet, because connecting EVB error failed

由于连接EVB失败，不能发送最近客户桥代理类型报文

Failed to send nearest customer packet, because no EVB TLV is enabled

由于未开启EVB TLV，不能发送最近客户桥代理类型报文

Failed to send nearest customer packet, because of no EVB data

由于没有EVB数据，不能发送最近客户桥代理类型报文

Failed to send nearest non-tpmr packet, because of connecting EVB error

由于连接EVB失败，不能发送最近非TPMR代理类型报文

Failed to send nearest non-tpmr packet, because of no enabled EVB TLV

由于未开启EVB TLV，不能发送最近非TPMR代理类型报文

Failed to send nearest non-tpmr packet, because of no EVB data

由于没有EVB数据，不能发送最近非TPMR代理类型报文

CDCP TLV length error

接收的CDCP TLV长度错误

Receive repeated CDCP TLV

收到的报文中含有重复的CDCP TLV

EVB TLV length error

接收的EVB TLV长度错误

Receive repeated EVB TLV

收到的报文中含有重复的EVB TLV

Receive repeated Management VLAN ID TLV

接收到重复的管理VLAN TLV

Management VID TLV length is error

管理VLAN TLV长度错误

Management VID TLV vlan id is error

管理VLAN TLV VLAN ID错误

Received a TLV (port and protocol VLAN ID TLV) that is not supported but enabled.

收到一个不支持但已开启的错误的TLV（Port And Protocol VLAN ID TLV）

CN TLV length error

接收的CN TLV长度错误

CN TLV value error

接收的CN TLV的值错误

Received repeated CN TLV

收到的报文中含有重复的CN TLV

表1-4 debugging lldp event命令输出信息描述表

字段

描述

MED neighbor refresh send shutdown

MED邻居变化，发送shutdown报文

MED neighbor refresh send normal

刷新MED邻居

MED neighbor number changed to zero

MED邻居个数变为零

Board *n* insertion event happened

板*n*插入事件发生

Creation/Deletion/Active/Deactive/Up/Down/Link up/Link down event happened.

接口创建/删除/激活/去激活/up/down事件发生

Reinit/Tx-inter/Tx-delay/Fast send/Polling/Gsave/Nb age/trap timer already exists

重新初始化/发送间隔/发送延迟/快发/轮询/定时保存/Trap定时器已经存在

Update statistic on unsupported port

在不支持的接口上更新接口统计数据

LLDP exit

LLDP去初始化

LLDP received terminal signal

LLDP已经收到终端信号

packet encapsulation format is not matched

接收到的报文封装格式与本端报文封装格式不符合

LLDP/CDP packet2CPU control:

ifIndex: *IfIndex*

value: *value*

result: *result*

接口（接口索引为*IfIndex*）下发协议控制状态（*value*值为开启或者关闭）的结果（*result*）

LLDP get index info Request

LLDP获取下一个数据的当前索引信息

LLDP get index info Response

LLDP获取的下一个数据的索引信息

Syns send data with len *len*

syns向client发送数据长度为*len*的数据

LLDP sent message to EVB, result is *value*

LLDP向EVB发送消息，发送的结果是*value*

LLDP processed EVB message, EVB enable value is *n*, data length is *length*

LLDP处理EVB消息，EVB开启值为*n*，长度为*length*

LLDP processed EVB message and data information is no change

LLDP处理EVB消息，数据信息没有发生变化

LLDP processed EVB message and restarted sending machine

LLDP处理EVB消息并重新启动发送状态机

The max credit is zero

LLDP发包限速令牌桶当前值为0

No end TLV

没有End of LLDPDU TLV

Set EEE TxSystemValue=*n*,RxSystemValue=*n*

向设备设置发送及等待接收来自对端的EEE的时间为*n*，单位为微秒

表1-5 debugging lldp fsm命令输出信息描述表

字段

描述

Receive state machine change from *state1* state to *state2* state

接收状态机由state1迁移至state2，状态包括：

·LLDP_RX_IDLE：表示空闲状态

·LLDP_RX_INIT：表示初始状态

·LLDP_RX_WAIT：表示等待接收状态，包括FRAME_RCVD、NB_AGED、ALLNB_DEL和CDPNB_DEL这四种事件

Send state machine change from *state1* state to *state2* state

发送状态机由*state1*迁移至*state2*，状态包括：

·LLDP_TX_WAIT_PORT：表示等待端口开启

·LLDP_TX_ACTIVE：表示激活状态处理

·LLDP_TX_INIT：表示端口发送初始化

·LLDP_TX_IDLE：表示端口空闲

·LLDP_TX_SHUTDOWN_FRAME：表示发送SHUTDOWN报文

·LLDP_TX_INFO_FRAME：表示发送报文

表1-6 debugging lldp packet命令输出信息描述表

字段

描述

Packet received/sent:

Interface *Interfacename*; Length is *len*

收到/发送报文：接口名为*Interfacename*；长度为*len*

【举例】

\# 设备通过端口GigabitEthernet1/0/1与另一台设备相连，两台设备全局和端口均开启了LLDP功能，在本设备上打开LLDP状态机调试信息开关。

\<Sysname\> debugging lldp fsm

\*Dec 6 10:54:12:978 2011 Sysname LLDP/7/Fsm:Port GigabitEthernet1/0/1 (IfIndex 51314688) nearest-bridge:

    Send state machine change from LLDP_TX_IDLE state to LLDP_TX_INFO_FRAME state

    Send state machine change from LLDP_TX_INFO_FRAME state to LLDP_TX_IDLE state

    Receive state machine change from LLDP_RX_INIT state to LLDP_RX_WAIT state

    Receive state machine change from LLDP_RX_WAIT state to EVT: FRAME_RCVD state

    Receive state machine change from RX_FRAME state to RX_WAIT_FOR_FR AME state

*[// LLDP*]*最近桥代理发送状态机由TX_IDLE状态迁移到LLDP_TX_INFO_FRAME状态，再迁移到LLDP_TX_IDLE状态。接收状态机由LLDP_RX_INIT状态迁移到LLDP_RX_WAIT状态，再切换到EVT: FRAME_RCVD事件，但是状态不迁移*

\# 设备通过GigabitEthernet1/0/1与另一台设备相连，两台设备全局和端口均开启了LLDP功能，在本设备上打开LLDP报文调试信息开关。

\<Sysname\> debugging lldp packet verbose

\<Sysname\> \*Aug  7 09:50:43:493 2012 Sysname LLDP/7/Packet received: -MDC=1;

Interface GigabitEthernet1/0/1 nearest-bridge; Length is 375.

 Chassis type        : MAC address

 Chassis ID          : 0011-2200-0101

 Port ID type        : Interface name

 Port ID             : GigabitEthernet1/0/1

 Time to live        : 120

 Port description    : GigabitEthernet1/0/1 Interface

 System name         : Sysname

 System description  : Sysname Comware Platform Software, Software Version 7.1.034,

                       Alpha 0101

                       Sysname Simware32

                       Copyright (c) 2004-2012 Hangzhou Sysname Tech. Co., Ltd. All

                       rights reserved.

 System capabilities supported : Bridge, Router, Customer Bridge, Service Bridge

 System capabilities enabled   : Bridge, Router, Customer Bridge

 Management address type           : All802

 Management address                : 000c-2919-c860

 Management address interface type : IfIndex

\*Aug  7 09:50:43:493 2012 Sysname LLDP/7/Packet received: -MDC=1;

 Management address interface ID   : Unknown

 Management address OID            : 0

 Port VLAN ID(PVID)  : 1

 DCBX Control info:

  Oper version       : Standard

 DCBX ETS configuration info:

  CBS                : False

  Max TCs            : 8

  CoS     Local priority      Percentage        TSA

   0            7                 16            ETS

   1            6                 16            ETS

   2            5                 17            ETS

   3            4                 17            ETS

   4            3                 17            ETS

   5            2                 17            ETS

   6            1                 0             ETS

   7            0                 0             SP

 DCBX ETS recommendation info:

  CoS     Local priority      Percentage        TSA

\*Aug  7 09:50:43:493 2012 Sysname LLDP/7/Packet received: -MDC=1;

   0            7                 16            ETS

   1            6                 16            ETS

   2            5                 17            ETS

   3            4                 17            ETS

   4            3                 17            ETS

   5            2                 17            ETS

   6            1                 0             ETS

   7            0                 0             SP

 DCBX PFC info:

  P0-0     P1-0     P2-0     P3-1     P4-1     P5-0     P6-0     P7-0

  Number of traffic classes supported: 8

  Value of MBC: 0

 DCBX APP info:

  Selected Field              Protocol ID Priority

  Ethertype                   0x22ca      0x3

 Auto-negotiation supported : No

 Auto-negotiation enabled   : No

 OperMau                    : Speed(0)/Duplex(Unknown)

\*Aug  7 09:50:43:493 2012 Sysname LLDP/7/Packet received: -MDC=1;

 Power port class           : PSE

 PSE power supported        : No

 PSE power enabled          : No

 PSE pairs control ability  : No

 Power pairs                : Signal

 Port power classification  : Class 0

 Power type                 : Type 2 PD

 Power source               : PSE and local

 Power priority             : High

 PD requested power value   : 21.1 w

 PSE allocated power value  : 15.3 w

 Link aggregation supported : Yes

 Link aggregation enabled   : No

 Aggregation port ID        : 0

 Maximum frame size         : 9216

 Transmit Tw                : 100 us

 Receive Tw                 : 90 us

 Fallback Tw                : 90 us

 Echo Transmit Tw           : 0 us

 Echo Receive Tw            : 0 us

\*Aug  7 09:50:48:076 2012 Sysname LLDP/7/Packet sent: -MDC=1;

Interface GigabitEthernet1/0/1 nearest-bridge; Length is 311.

 Chassis type        : MAC address

 Chassis ID          : 0011-2200-0001

 Port ID type        : Interface name

 Port ID             : GigabitEthernet1/0/1

 Time to live        : 120

 Port description    : GigabitEthernet1/0/1 Interface

 System name         : Sysname

 System description  : Sysname Comware Platform Software, Software Version 7.1.034,

                       Alpha 0101

                       Sysname Simware32

                       Copyright (c) 2004-2012 Hangzhou Sysname Tech. Co., Ltd. All

                       rights reserved.

 System capabilities supported : Bridge, Router, Customer Bridge, Service Bridge

 System capabilities enabled   : Bridge, Router, Customer Bridge

 Management address type           : All802

 Management address                : 000c-2990-45fd

 Management address interface type : IfIndex

\*Aug  7 09:50:48:076 2012 Sysname LLDP/7/Packet sent: -MDC=1;

 Management address interface ID   : Unknown

 Management address OID            : 0

 Port VLAN ID(PVID)  : 1

 DCBX Control info:

  Oper version       : Standard

 DCBX PFC info:

  P0-0     P1-0     P2-0     P3-1     P4-0     P5-0     P6-0     P7-0

  Number of traffic classes supported: 8

  Value of MBC: 0

 Auto-negotiation supported : No

 Auto-negotiation enabled   : No

 OperMau                    : Speed(0)/Duplex(Unknown)

 Power port class           : PSE

 PSE power supported        : No

 PSE power enabled          : No

 PSE pairs control ability  : No

 Power pairs                : Signal

 Port power classification  : Class 0

 Power type                 : Type 2 PD

 Power source               : PSE and local

 Power priority             : High

 PD requested power value   : 21.1 w

 PSE allocated power value  : 15.3 w

 Link aggregation supported : Yes

 Link aggregation enabled   : No

 Aggregation port ID        : 0

 Maximum frame size         : 9216

 Transmit Tw                : 100 us

 Receive Tw                 : 90 us

 Fallback Tw                : 90 us

 Echo Transmit Tw           : 0 us

 Echo Receive Tw            : 0 us

*[// LLDP*]*发送报文和接收报文的详细信息*
