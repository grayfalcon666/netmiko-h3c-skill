<!-- CMD-INDEX
  call-normal                         | Call节点视图         | L24
  description                         | Call/Jump/Service节点视图 | L78
  dial-prefix                         | Call节点视图         | L124
  display voice ivr call-info         | 任意视图             | L188
  display voice media-play            | 任意视图             | L268
  display voice media-source          | 任意视图             | L346
  global-input-error                  | IVR管理视图          | L412
  global-timeout                      | IVR管理视图          | L464
  input extension                     | Call节点视图         | L518
  input-error                         | Jump/Call节点视图    | L570
  ivr-root                            | IVR语音实体视图        | L630
  ivr-system                          | 语音视图             | L676
  media-file                          | 语音视图             | L716
  media-play                          | Jump/Call节点视图    | L758
  node                                | IVR管理视图          | L808
  operation                           | Service节点视图      | L862
  select-rule                         | Service节点视图      | L928
  set-media                           | 语音媒体资源管理视图       | L982
  timeout                             | Jump/Call节点视图    | L1030
  user-input                          | Jump节点视图         | L1092
-->

**可定制IVR \-- 可定制IVR配置命令 \-- call-normal**

------------------------------------------------------------------------

**[call-normal**]命令用来配置普通二次呼叫的号码匹配策略。

**[undo**] **call-normal**命令用来取消已有配置。

【命令】

**[call-normal**[ { **length** *number-length* \| **matching** \| **terminator** *character* }]]

**[undo** **call-normal**]

【缺省情况】

没有配置普通二次呼叫的号码匹配策略。

【视图】

Call节点视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[length** *number-length*]：匹配输入号码的长度，取值范围为1～31。

**[matching**]：随时匹配号码，即只要匹配到用户输入的号码，就立即进行二次呼叫。

**[terminator** *character*]：结束符，取值范围为0～9、\*、\#。

【使用指导】

请避免将被叫号码中包含的字符或号码配置为终结符。

【举例】

\# 配置普通二次呼叫，匹配7位长度的用户输入号码。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice ivr-system

Sysname-voice-ivr node 1 call

Sysname-voice-ivr-node1 call-normal length 7

**可定制IVR \-- 可定制IVR配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来配置节点的描述信息。

**[undo** **description**]命令用来删除节点的描述信息。

【命令】

**[description** *text*]

**[undo** **description**]

【缺省情况】

没有配置节点的描述信息。

【视图】

Call/Jump/Service节点视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：节点的描述信息，为1～80个字符的字符串，区分大小写。

【举例】

\# 配置Jump节点的描述信息。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice ivr-system

Sysname-voice-ivr node 1 jump

Sysname-voice-ivr-node1 description first-node

**可定制IVR \-- 可定制IVR配置命令 \-- dial-prefix**

------------------------------------------------------------------------

**[dial-prefix**]命令用来配置号码前缀。

**[undo** **dial-prefix**]命令用来删除已配置的前缀号码。

【命令】

**[dial-prefix** *string*]

**[undo** **dial-prefix**]

【缺省情况】

没有配置号码前缀。

【视图】

Call节点视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[string*]：号码前缀，为1～31个字符的字符串，取值范围为0～9、\*、\#。各符号的含义如[表]1-1(?-1356103434#_Ref169498719)所示。

表1-1 参数string中的符号含义

符号

含义

0-9

表示一位号码，可以是0到9之间的数字

\#或\*

表示一位有效号码

【使用指导】

配置号码前缀后，设备会以"号码前缀＋拨入号码"作为被叫号码。添加号码前缀后，如果号码总长度超过31位时，设备只发送前31位号码。

【举例】

\# 配置号码前缀021。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice ivr-system

Sysname-voice-ivr node 1 call

Sysname-voice-dial-node1 dial-prefix 021

**可定制IVR \-- 可定制IVR配置命令 \-- display voice ivr call-info**

------------------------------------------------------------------------

**[display** **voice** **ivr** **call-info**]命令用来查看IVR呼叫信息。

【命令】

**[display** **voice** **ivr** **call-info**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 查看IVR呼叫信息。

\<Sysname\> display voice ivr call-info

Index  Called-Number    Caller-Number    Entity   Node-Id  Status

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

1      101              100              101      1        PLAY MEDIA

2      406              200              201      3        WAIT INPUT

3      606              300              301      6        CALL

4      806              400              401      9        IDLE

表1-2 display voice ivr call-info命令显示信息描述表

字段

描述

Index

呼叫信息索引

Called-Number

被叫号码

Caller-Number

主叫号码

Entity

被叫号码对应的IVR语音实体号

Node-Id

正在执行的节点号

Status

当前执行所处的状态：

·IDLE：空闲状态

·PLAY MEDIA：播放媒体状态

·WAIT INPUT：等待按键状态

·CALL：呼叫状态

**可定制IVR \-- 可定制IVR配置命令 \-- display voice media-play**

------------------------------------------------------------------------

【命令】

**[display** **voice** **media-play**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 查看放音信息。

\<Sysname\> display voice media-play

Index    Codec       Media-Id    Play-Times       Status        Type

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

1        g729r8       1001           3             play          PSTN:1/0

2        g711alaw     1002           2             stop          IP:100.1.1.1

3        g711ulaw     1003           2             stop          IP:100.1.1.1

4        g723r53      1004           2             stop          IP:100.1.1.1

表1-3 display voice media-play命令显示信息描述表

字段

描述

Index

放音信息索引

Codec

放音编解码类型，包括g729r8、g711alaw、g711ulaw和g723r53四种编解码类型

Media-Id

媒体资源ID

Play-Times

媒体文件总共要播放的次数

Status

当前的放音状态：

·play

·stop

Type

当前的呼叫类型：

·PSTN：从PSTN接入，此例中的1/0表示呼叫从语音用户线1/0接入

·IP：呼叫从对端的IP地址接入

**可定制IVR \-- 可定制IVR配置命令 \-- display voice media-source**

------------------------------------------------------------------------

【命令】

**[display** **voice** **media-source** ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 查看媒体文件的读取信息。

\<Sysname\> display voice media-source

Codec    Media-Id   source        Size (Bytes)   Read-Num  Cache-Num

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

g729r8   1000       cfa0:/wav/g7  69304          1         1

                    29r8/0.wav

表1-4 display voice media-source命令显示信息描述表

字段

描述

Codec

文件使用的编解码类型

Media-Id

媒体资源ID

Source

媒体文件名及存放路径

Size (Bytes)

媒体文件的大小，以字节为单位

Read-Num

此文件对应的读控制块编号

Cache-Num

此文件对应的缓冲区编号

**可定制IVR \-- 可定制IVR配置命令 \-- global-input-error**

------------------------------------------------------------------------

**[global-input-error**]命令用来配置全局IVR用户输入错误的处理策略。

**[undo** **global-input-error**]命令用来恢复缺省情况。

【命令】

**[global-input-error** { **media-play** *media-id* [ *play-times*  \| **repeat** *repeat-times* } \*]]

**[undo** **global-input-error**]

【缺省情况】

输入错误后不播放提示音，输入超过错误3次后结束呼叫。

【视图】

IVR管理视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[media-play*** media-id*]：用户输入错误后，设备播放提示音的媒体资源ID，取值范围为0～2147483647。

*[play-times*]：播放提示音的次数，取值范围为1～255，缺省值为1次。

**[repeat*** repeat-times*]：允许用户输入错误的次数，每次用户输入错误后，设备将重新执行该节点，输入错误次数超过设定的值后将结束呼叫。取值范围为0～255，缺省值为3次。

【举例】

\# 配置全局IVR用户输入错误的处理策略：播放媒体资源ID为10002的提示音2次，输入错误超过5次后结束呼叫。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice ivr-system

Sysname-voice-ivr global-input-error media-play 10002 2 repeat 5

【相关命令】

·**input-error**

**可定制IVR \-- 可定制IVR配置命令 \-- global-timeout**

------------------------------------------------------------------------

**[global**]**-timeout**命令用来配置全局IVR用户输入超时的处理策略。

**[undo**]**global-timeout**命令用来恢复缺省情况。

【命令】

**[global-timeout**[ { **expires** *seconds* \| **media-play** *media-id* [ *play-times* ] \| **repeat** *repeat-times* } \*]]

**[undo global-timeout**]

【缺省情况】

超时时间为10秒，超时次数为3次，输入超时后不播放提示音，超过超时次数后结束呼叫。

【视图】

IVR管理视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[expires** *seconds*]：超时时间，超时后将重新执行该节点，取值范围为1～255，单位为秒。

**[media-play*** media-id*]：用户输入超时后，设备播放提示音的媒体资源ID，取值范围为0～2147483647。

*[play-times*]：播放提示音的次数，取值范围为1～255，缺省值为1次。

**[repeat*** repeat-times*]：允许用户输入超时的次数，每次用户输入超时后，设备将重新执行该节点。超时次数超过设定的值后将结束呼叫。取值范围为0～255。

【举例】

\# 配置全局IVR用户输入超时的处理策略：超时时间为20秒，媒体资源ID为100001，播放提示音1次，超时次数超过2次后结束呼叫。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice ivr-system

Sysname-voice-ivr global-timeout expires 20 media-play 100001 1 repeat 2

【相关命令】

·**timeout**

**可定制IVR \-- 可定制IVR配置命令 \-- input extension**

------------------------------------------------------------------------

**[input**]命令用来配置扩展二次呼叫。

**[undo** **input**]命令用来取消已有配置。

【命令】

**[input ***number ***extension*** extension-number*]

**[undo** **input** *number*]

【缺省情况】

没有配置扩展二次呼叫。

【视图】

Call节点视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：用户输入的号码，为1～31个字符的字符串，取值范围为0～9、\*、\#。

*[extension-number*]：扩展二次呼叫的号码，为1～31个字符的字符串，取值范围为0～9、\*、\#。

【使用指导】

一个Call节点下最多可以配置10条扩展二次呼叫命令。

【举例】

\# 配置扩展二次呼叫，按0表示呼叫号码5000。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice ivr-system

Sysname-voice-ivr node 1 call

Sysname-voice-ivr-node1 input 0 extension 5000

**可定制IVR \-- 可定制IVR配置命令 \-- input-error**

------------------------------------------------------------------------

**[input-error**]命令用来配置节点下用户输入错误的处理策略。

**[undo** **input-error**]命令用来取消已有配置。

【命令】

**[input-error**[ { **end-call** \| **goto-pre-node** \| **goto-node** *node-id* } [ **media-play** *media-id* [ *play-times* ] \| **repeat** *repeat-times* ] \*]]

**[undo** **input-error**]

【缺省情况】

没有配置节点下用户输入错误的处理策略。

【视图】

Jump/Call节点视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[end-call**]：输入错误次数超过设定值后结束呼叫。

**[goto-pre-node**]：输入错误次数超过设定值后返回上一级节点。

**[goto-node** *node-id*]：输入错误次数超过设定值后跳到指定的节点，取值范围为1～256。

**[media-play*** media-id*]：用户输入错误后，设备播放提示音的媒体资源ID，取值范围为0～2147483647。

*[play-times*]：播放提示音的次数，取值范围为1～255，缺省值为1。

**[repeat*** repeat-times*]：允许用户输入错误的次数，每次用户输入错误后，设备将重新执行该节点。当输入错误次数超过设定值后，按配置的处理方式进行处理，取值范围为0～255，缺省值为3。

【举例】

\# 配置节点下用户输入错误的处理策略：播放媒体资源ID为10002的提示音2次，输入错误次数超过5次就结束呼叫。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice ivr-system

Sysname-voice-ivr node 1 jump

Sysname-voice-ivr-node1 input-error end-call media-play 1000 6 repeat 5

【相关命令】

·**global-input-error**

**可定制IVR \-- 可定制IVR配置命令 \-- ivr-root**

------------------------------------------------------------------------

**[ivr-root**]命令用来配置IVR语音实体的根节点，即IVR执行的第一个节点。

**[undo** **ivr-root**]命令用来取消IVR语音实体的根节点。

【命令】

**[ivr-root**] *node-id*

**[undo**] **ivr-root**

【缺省情况】

不存在IVR语音实体的根节点。

【视图】

IVR语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[node-id*]：根节点号，取值范围为1～256。

【举例】

\# 配置IVR语音实体的根节点。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 100 ivr

Sysname-voice-dial-entity100 ivr-root 1

**可定制IVR \-- 可定制IVR配置命令 \-- ivr-system**

------------------------------------------------------------------------

**[ivr-system**]命令用来进入IVR管理视图。

**[undo **]**ivr-system**命令用来删除所有IVR配置。

【命令】

**[ivr-system**]

**[undo **]**ivr-system**

【缺省情况】

没有IVR管理视图。

【视图】

语音视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 进入IVR管理视图。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice ivr-system

Sysname-voice-ivr

**可定制IVR \-- 可定制IVR配置命令 \-- media-file**

------------------------------------------------------------------------

**[media-file**]命令用来进入语音媒体资源管理视图。

【命令】

**[media-file**  { **g711alaw** \| **g711ulaw** \| **g723r53** \| **g729r8** }]

【视图】

语音视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[g711alaw**]：进入g711alaw编码类型视图。

**[g711ulaw**]：进入g711ulaw编码类型视图。

**[g723r53**]：进入g723r53编码类型视图。

**[g729r8**]：进入g729r8编码类型视图。

【举例】

\# 进入编码类型为g729r8的媒体资源管理视图。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice media-file g729r8

Sysname-voice-media-g729r8

**可定制IVR \-- 可定制IVR配置命令 \-- media-play**

------------------------------------------------------------------------

**[media-play**]命令用来配置等待用户按键播放的提示音。

**[undo**] **media-play**命令用来恢复缺省情况。

【命令】

**[media-play** *media-id* [ *play-times*   **force** ]]

**[undo** **media-play**]

【缺省情况】

没有配置等待用户按键播放的提示音。

【视图】

Jump/Call节点视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[media-id*]：表示媒体资源ID，取值范围为0～2147483647。

*[play-times*]：重复播放次数，取值范围为1～255，缺省值为1。

**[force**]：表示进入节点后，播放提示音结束后用户按键才有效。缺省情况为不强制，即表示在提示音播放过程中用户按键有效。

【举例】

\# 配置等待用户按键提示音，且播放提示音结束后用户按键才有效。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice ivr-system

Sysname-voice-ivr node 1 jump

Sysname-voice-ivr-node1 media-play 10000 3 force

**可定制IVR \-- 可定制IVR配置命令 \-- node**

------------------------------------------------------------------------

**[node**]命令用来创建一个IVR节点并进入IVR节点视图。

**[undo** **node**]命令用来删除IVR节点。

【命令】

**[node**[ *node-id* [ **call** \| **jump** \| **service** ]]]

**[undo**[ **node** { *node-id* \| **all** }]]

【缺省情况】

不存在IVR节点。

【视图】

IVR管理视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[node-id*]：表示一个节点号，取值范围为1～256。

**[call**]：表示配置二次呼叫的节点。

**[jump**]：表示配置按键选择跳转的节点。

**[service**]：表示配置立即二次呼叫、跳转、结束呼叫或放音的节点。

**[all**]：所有类型的节点。

【举例】

\# 创建Jump节点。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice ivr-system

Sysname-voice-ivr node 1 jump

Sysname-voice-ivr-node1

**可定制IVR \-- 可定制IVR配置命令 \-- operation**

------------------------------------------------------------------------

**[operation**]命令用来配置节点操作功能。

**[undo** **operation**]命令用来取消已有配置。

【命令】

**[operation**[ *number* { **call-immediate** *call-number* \| **end-call** \| **goto-node** *node-id* \| **goto-pre-node** \| **media-play** *media-id* [ *play-times* ] }]]

**[undo** **operation** *number*]

【缺省情况】

没有配置节点操作功能。

【视图】

Service节点视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：执行ID标识，取值范围为1～3。

**[call-immediate** *call-number*]：立即二次呼叫的号码，为1～31个字符的字符串，取值范围为0～9、\*、\#。

**[end-call**]：结束呼叫。

**[goto-node** *node-id*]：跳到指定节点，取值范围为1～256。

**[goto-pre-node**]：返回上级节点。

**[media-play*** media-id*]：配置播放提示音的媒体资源ID，取值范围为0～2147483647。

*[play-times*]：播放提示音的次数，取值范围为1～255，缺省值为1次。

【使用指导】

当某项执行功能为跳转到其他节点或挂机操作时，将不再执行剩下未执行的功能项。

【举例】

\# 在Service节点配置执行结束呼叫。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice ivr-system

Sysname-voice-ivr node 1 service

Sysname-voice-ivr-node1 operation 1 end-call

【相关命令】

·**select-rule**

**可定制IVR \-- 可定制IVR配置命令 \-- select-rule**

------------------------------------------------------------------------

**[select-rule**]命令用来配置功能执行顺序。

**[undo** **select-rule**]命令用来恢复缺省情况。

【命令】

**[select-rule** *1st-operation 2nd-operation 3rd-operation*]

**[undo** **select-rule** ]

【缺省情况】

功能执行顺序为**select-rule** **1** **2** **3**。

【视图】

Service节点视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[1st-operation*]：第一个执行的操作功能号，取值范围为1～3。

*[2nd-operation*]：第二个执行的操作功能号，取值范围为1～3，此参数不能同*1st-operation*重复。

*[3rd-operation*]：第三个执行的操作功能号，取值范围为1～3，此参数不能同*1st-operation*，*2nd-operation*重复。

【举例】

\# 配置Service节点下功能执行顺序为1，3，2。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice ivr-system

Sysname-voice-ivr node 1 service

Sysname-voice-ivr-node1 select-rule 1 3 2

【相关命令】

·**operation**

**可定制IVR \-- 可定制IVR配置命令 \-- set-media**

------------------------------------------------------------------------

**[set-media**]命令用来配置媒体资源ID与媒体文件的对应关系。

**[undo**] **set-media**命令用来删除已配置的对应关系。

【命令】

**[set-media*** media-id ***file** *filename*]

**[undo**  **set-media** { *media-id* \| **all** }]

【缺省情况】

没有定义媒体资源ID。

【视图】

语音媒体资源管理视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[media-id*]：媒体资源ID，取值范围为0～2147483647。

**[file*** filename*]：媒体文件名。

**[all**]：所有媒体资源ID。

【举例】

\# 配置资源ID 10001对应的媒体文件为cfa0:/g729/ring.wav。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice media-file g729r8

Sysname-voice-media-g729r8 set-media 10001 file cfa0:/g729/ring.wav

**可定制IVR \-- 可定制IVR配置命令 \-- timeout**

------------------------------------------------------------------------

**[timeout**]命令用来配置节点下用户输入超时的处理策略。

**[undo** **timeout**]命令用来删除已有配置。

【命令】

**[timeout**[ { **end-call** \| **goto-pre-node** \| **goto-node** *node-id* } [ **expires** *seconds* \| **media-play** *media-id* [ *play-times* ] \| **repeat** *repeat-times* ] \*]]

**[undo** **timeout**]

【缺省情况】

没有配置节点下用户输入超时的处理策略。

【视图】

Jump/Call节点视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[end-call**]：结束呼叫。

**[goto-pre-node**]：返回上级节点。

**[goto-node** *node-id*]：跳到指定的节点，取值范围为1～256。

**[expires** *seconds*]：超时时间，取值范围为1～255，单位为秒，缺省值为10秒。

**[media-play*** media-id*]：用户输入超时后，设备播放提示音的媒体资源ID，取值范围为0～2147483647。

*[play-times*]：配置播放提示音的次数，取值范围为1～255，缺省值为1次。

**[repeat*** repeat-times*]：允许用户输入超时的次数，每次用户输入错误后，设备将重新执行该节点。当输入超时次数超过设定值后，按配置的处理方式进行处理，取值范围为0～255，缺省为3次。

【举例】

\# 配置节点下用户输入超时的处理策略为输入超时次数超过3次，结束呼叫。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice ivr-system

Sysname-voice-ivr node 1 jump

Sysname-voice-ivr-node1 timeout end-call repeat 3

【相关命令】

·**global-timeout**

**可定制IVR \-- 可定制IVR配置命令 \-- user-input**

------------------------------------------------------------------------

**[user-input**]命令用来配置根据具体输入执行跳转操作。

**[undo**] **user-input**命令用来取消已有配置。

【命令】

**[user-input**[ *character* { **end-call** \| **goto-node** *node-id* \| **goto-pre-node** }]]

**[undo** **user-input** *character*]

【缺省情况】

没有配置跳转操作。

【视图】

Jump节点视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[character*]：用户输入的按键信息，取值范围为0～9、\*、\#。

**[end-call**]：表示结束呼叫。

**[goto-node*** node-id*]：表示跳到指定的节点，取值范围为1～256。

**[goto-pre-node**]：表示返回上级节点。

【使用指导】

在一个Jump节点下最多可以配置12个跳转操作。

【举例】

\# 配置用户按0结束呼叫。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice ivr-system

Sysname-voice-ivr node 1 jump

Sysname-voice-ivr-node1 user-input 0 end-call

