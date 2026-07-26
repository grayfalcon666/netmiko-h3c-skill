
**拨号策略 \-- 拨号策略调试命令 \-- debugging voice dial-plan**

------------------------------------------------------------------------

【命令】

**[debugging voice dial-plan **[{ **all** \| **error** \| **event** }]]

**[undo debugging voice dial-plan **[{ **all** \| **error** \| **event** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示拨号策略所有消息类型的调试信息开关。

**[error**]：表示拨号策略的错误类型的消息调试信息开关。

**[event**]：表示拨号策略的事件类消息调试信息开关。

【描述】

**[debugging voice dial-plan**]命令用来打开拨号策略调试信息开关。**undo debugging voice dial-plan**命令用来关闭拨号策略调试信息开关。

缺省情况下，拨号策略调试信息开关处于关闭状态。

表1-1 debugging voice dial-plan error令输出信息描述表

字段

描述

Failed to allocate memory for *object*.

为*object*分配内存失败。*object*为对象名，包括：

·entity：语音实体号

·regular expression：正则表达式

Failed to send *type* command.

拨号策略向驱动下发*type*命令失败。*type*为下发驱动的命令字类型，包括：

·VOICE_CIOCTL_VOICE_STAR：开启语音功能命令字

·VOICE_CIOCTL_BUSY_TONE_DETECT_START：忙音检测命令字

·VOICE_CIOCTL_BUSY_TONE_DETECT_STOP：停止忙音检测命令字

·VOICE_CIOCTL_BUSY_TONE_PARAM_DOWN：忙音检测数据命令字

·VOICE_CIOCTL_EC_PARAM_DOWN：回波抵消命令字

·VOICE_CIOCTL_DTMF_AMP  DTMF：振幅命令字

·VOICE_CIOCTL_DTMF_TIME：时长命令字

·VOICE_CIOCTL_CPTONE：提示音命令字

·VOICE_CIOCTL_CPTONEAMP：提示音振幅命令字

·VOICE_CIOCTL_FXO_MONITORING：FXO语音用户线检测

Failed to get *type* table when *condition*.

在*condition*条件下获取*type*表单失败。*condition*为获取的时机。*type*为表单的类型，包括：

·entity substitution：语音实体号码变换

·call information：呼叫信息

Failed to get *type* entity from *module*.

从module获取type语音实体失败。module为模块名，type为实体类型

Failed to create socket, errno is *number*.

创建socket失败，错误码是*number*

*[number*]为错误码数值

Failed to send *type object*  to *module*.

向*module*发送*type*类型的*object*失败。*module*为模块名，*type*为消息类型，*object*为待发送的对象

Failed to create *object*  for *module*.

为*module*创建*object*失败。*module*为模块名，*object*为待删除的对象

Failed to set *object*  for *module*.

为*module*设置*object*失败。*module*为模块名，*object*为待删除的对象

Failed to delete *object*  for *module*. 颠三倒四的

为*module*删除*object*失败。*module*为模块名，*object*为待删除的对象

Failed to add *object*  to *module*.

为*module*增加*object*失败。*module*为模块名，*object*为待增加的对象

Failed to flush TLV message.

TLV消息转线性内存失败

Invalid *module* type.

*[module*]类型无效

Invalid *object*.

无效的对象名

The *object*  is empty.

*[object*]为空

*[object*]为对应的对象名

The user number does not exist.

被叫号码不存在

The regular expression is incomplete.

正则式不完整

Unknown voice module ID.

未知的语音模块Id

表1-2 debugging voice dial-plan event令输出信息描述表

字段

描述

 The number template already exists.

号码模版已存在

The number template does not exist.

号码模版不存在

The list of number template is empty.

号码模版列表为空

Remove the bound codec group from this entity first.

请先移除当前实体下绑定的编解码组

DPL \--\> DRV: *command*.

拨号策略下发*command*给驱动

*[command*]为对应的命令字，同上

The current connection number(*number1*) of entity *index* has reached max(*number2*).

语音实体*index*的当前连接数*number1*已达最大值*number2*

*[index*]为当前实体的序号

*[number1*]为当前的连接数

*[number2*]为当前配置的最大连接数

Entity *index* is denied by call permission.

由于配置呼叫限制功能，匹配语音实体*index*的呼叫被拒绝

*[index*]为当前实体的序号

The maximum number(*number*) of entity tags has been reached. The rest of the entities will not be selected.

已取到语音实体序号的最大值*number*，其余的语音实体不会被选中

*[number*]为语音实体序号的最大值

No available entity has been found.

没有找到可用的语音实体

Access service number *number* has been found.

已发现接入服务号码*number*

*[number*]为接入服务号码

Get entity *index* successfully.

成功选中语音实体*index*

Suitable substitution rule has been found.

InputFormat: *format*  \--\> OutputFormat: *format* 

已找到匹配的变换规则:

输入格式: *format*  \>\>  输出格式: *format*

*[format*]为变换规则的格式

The user number has been substituted successfully.

主被叫号码已被成功变换

No suitable substitution rule has been found. The user number has not been substituted

未找到合适的的变换规则。用户号码没有被变换

The user number only matches the first part of the regular expression.

用户号码只匹配正则式的前半部分

The current connected number is 0.

当前已连接的（呼叫）数目为0

Failed to update the information of entity *index*.

更新语音实体*index*的信息失败

External initialization failed in a switch-over between master and standby.

主备倒换期间外部初始化失败

Receive *type* event from interface *name*.

从接口*name*收到*type*事件。*name*为接口名，*type*为事件类型，包括：

·IF_IFMSG_ACTIVE  ACTIVE事件

·IF_IFMSG_DEACTIVE  DEACTIVE事件

·IF_IFMSG_DELETE  DELETE事件

·IF_IFMSG_UP  UP事件

·IF_IFMSG_DOWN  DOWN事件

Sending request for data synchronization to MPU.

向MPU发送数据同步请求

Failed to get *object*.

无法获取*object*。*object*为待获取对象名

There are entities to be matched for the call.

存在可匹配当前呼叫的语音实体

Entity *index* stop keepalive. detection.。

语音实体*index*停止保活探测

*[index*]为当前实体的序号

Entity *index* start keepalive. detection.

语音实体*index*开始保活探测

*[index*]为当前实体的序号

Failed to push message by MPU.

MPU推送数据失败

【举例】

\# 配置语音实体号121、14，两者的号码模版分别为121、14。对于号码变换组1，配置规则，将号码121变换为14。在拨号策略视图下配置全局号码变换规则，绑定号码变换组1，使用其对被叫号码进行变换，打开拨号策略模块的所有调试信息。

\<Sysname\> debugging voice dial-plan all

\<Sysname\>\*Jan 24 10:05:24:679 2014 Sysname DPL/7/DPLDBG:

DPL_EVENT: Number substitution configured under dial-plan view is enabled.

*// 检测到语音用户线或者语音实体视图下有号码变换规则*

\*Jan 24 10:05:24:679 2014 Sysname DPL/7/DPLDBG:

DPL_EVENT: Suitable substitution rule has been found.

           Input format: 121 \--\> output format: 14.

*// 应用规则，将输入的被叫号码121变换为14*

**

\*Jan 24 10:05:24:680 2014 Sysname DPL/7/DPLDBG:

DPL_EVENT: The user number has been substituted successfully.

           Original number is 121, substituted number is 14;

           Original number type is unknown(0x00), substituted number type is unknown(0x00);

           Original numbering plan is unknown(0x00), substituted numbering plan is unknown(0x00).

*// 号码变换详细信息输出*

\*Jan 24 10:05:24:693 2014 Sysname DPL/7/DPLDBG:

DPL_EVENT: Get entity 14 successfully.

*// 号码14成功匹配到语音实体*

