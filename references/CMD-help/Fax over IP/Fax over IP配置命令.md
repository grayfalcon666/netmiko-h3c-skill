<!-- CMD-INDEX
  fax cng-switch enable               | POTS/VoIP语音实体视图  | L13
  fax ecm                             | POTS/VoIP语音实体视图  | L55
  fax level                           | POTS/VoIP语音实体视图  | L101
  fax local-train threshold           | POTS/VoIP语音实体视图  | L151
  fax nsf                             | POTS/VoIP语音实体视图  | L205
  fax protocol                        | POTS/VoIP语音实体视图  | L251
  fax rate                            | POTS/VoIP语音实体视图  | L325
  fax train-mode                      | POTS/VoIP语音实体视图  | L397
  modem passthrough                   | POTS/VoIP语音实体视图  | L449
-->

**Fax over IP \-- Fax over IP配置命令 \-- fax cng-switch enable**

------------------------------------------------------------------------

**[fax** **cng-switch** **enable**]命令配置用来开启CNG传真切换。

**[undo** **fax** **cng-switch** **enable**]命令用来恢复缺省情况。

【命令】

**[fax** **cng-switch** **enable**]

**[undo** **fax** **cng-switch** **enable**]

【缺省情况】

CNG传真切换处于关闭状态。

【视图】

POTS/VoIP语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 开启CNG传真切换。

\<sysname\> system-view

sysname voice-setup

sysname-voice dial-program

sysname-voice-dial entity 100 pots

sysname-voice-dial-entity100 fax cng-switch enable

**Fax over IP \-- Fax over IP配置命令 \-- fax ecm**

------------------------------------------------------------------------

**[fax** **ecm**]命令用来配置传真使用ECM方式。

**[undo** **fax** **ecm**]命令用来恢复缺省情况。

【命令】

**[fax** **ecm**]

**[undo** **fax** **ecm**]

【缺省情况】

不使用ECM方式。

【视图】

POTS/VoIP语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

实际配置传真使用ECM方式时，请确认两端传真机都支持ECM方式，并且在发送和接收侧设备上的VoIP语音实体和POTS语音实体下配置ECM方式处于开启状态。

【举例】

\# 配置传真使用ECM方式。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 4 pots

Sysname-voice-dial-entity4 fax ecm

**Fax over IP \-- Fax over IP配置命令 \-- fax level**

------------------------------------------------------------------------

**[fax** **level**]命令用来配置发送载波能量值。

**[undo** **fax** **level**]命令用来恢复缺省情况。

【命令】

**[fax** **level** *level*]

**[undo** **fax** **level**]

【缺省情况】

发送载波能量值为-15dBm。

【视图】

POTS/VoIP语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[level*]：发送载波能量值，即发送电平衰减值，取值范围为-60～-3，单位为dBm。能量值越大表示能量越大，能量值越小表示衰减越大。

【使用指导】

在一般情况下，使用缺省的发送载波能量值即可。在其它配置正确的前提下，如果仍无法成功建立传真时，可尝试调整发送载波能量值。

【举例】

\# 配置发送载波能量值为-20dBm。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 4 pots

Sysname-voice-dial-entity4 fax level -20

**Fax over IP \-- Fax over IP配置命令 \-- fax local-train threshold**

------------------------------------------------------------------------

**[fax** **local-train** **threshold**]命令用来配置本地训练阈值百分比。

**[undo** **fax** **local-train** **threshold**]命令用来恢复缺省情况。

【命令】

**[fax** **local-train** **threshold** *threshold*]

**[undo** **fax** **local-train** **threshold**]

【缺省情况】

本地训练阈值百分比为10。

【视图】

POTS/VoIP语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[threshold*]：本地训练阈值百分比，取值范围为0～100。

【使用指导】

当训练方式为本地训练方式时，**fax** **local-train** **threshold**命令配置的本地训练阈值百分比才能生效。

【举例】

\# 配置本地训练阈值百分比为20。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 10 pots

Sysname-voice-dial-entity10 fax local-train threshold 20

【相关命令】

·**fax** **train****-mode**

**Fax over IP \-- Fax over IP配置命令 \-- fax nsf**

------------------------------------------------------------------------

**[fax** **nsf**]命令用来配置开启非标准能力协商的国家码和厂商码。

**[undo** **fax** **nsf**]命令用来恢复缺省情况。

【命令】

**[fax** **nsf** *value*]

**[undo** **fax** **nsf**]

【缺省情况】

使用非标准能力协商的国家码和厂商码为264833。

【视图】

POTS/VoIP语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[nsf*]：开启非标准能力协商的国家码和厂商码，取值范围为0～0xFFFFFF（两位国家码 + 四位厂商码），其中国家码的设置需要符合T.35标准。取值为000000时，表示使用标准能力协商。

【举例】

\# 配置开启非标准的能力协商的国家码和厂商码为264834。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 10 pots

Sysname-voice-dial-entity10 fax nsf 264834

**Fax over IP \-- Fax over IP配置命令 \-- fax protocol**

------------------------------------------------------------------------

**[fax protocol**]命令用来配置传真协议。

**[undo fax protocol**]命令用来恢复缺省情况。

【命令】

**[fax protocol **[{ **pass-through** { **g711alaw** \| **g711ulaw** } \| **standard-t38** [ **ls-redundancy** *number* [ **hs-redundancy** *number* ] ] }]]

**[undo fax protocol**]

【缺省情况】

使用标准T.38传真协议。

【视图】

POTS/VoIP语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[pass-through**]：开启传真透传方式。

**[g711alaw**]：传真透传方式使用g711alaw编解码。

**[g711μlaw**]：传真透传方式使用g711mlaw编解码。

**[standard-t38**]：使用标准T.38传真协议。

**[ls-redundancy**] *number*：表示低速传输传真数据时的冗余包数，取值范围为0～5，缺省值为0。

**[hs-redundancy**] *number*：表示高速传输传真数据时的冗余包数，取值范围为0～2，缺省值为0。

【使用指导】

·如果配置使用标准T.38传真协议，在出现传真失败或断页情况时，可以通过配置传真冗余包，保证在网络环境较差的情况下传真成功。

·只要在传真发起方设备配置此命令，传真接收方会自动适配传真协议。

【举例】

\# 配置标准T.38传真协议，低速传输传真数据时的冗余包数为4。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 10 pots

Sysname-voice-dial-entity10 fax protocol standard-t38 ls-redundancy 4

\# 配置传真透传方式使用g711alaw编解码。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 10 pots

Sysname-voice-dial-entity10 fax protocol pass-through g711alaw

**Fax over IP \-- Fax over IP配置命令 \-- fax rate**

------------------------------------------------------------------------

**[fax** **rate**]命令用来配置最高传真速率。

**[undo** **fax** **rate**]命令用来恢复缺省情况。

【命令】

**fax**[ **rate** { **2400** \| **4800** \| **7200** \| **9600** \| **12000** \| **14400** \| **disable** \| **voice** }]

**[undo** **fax** **rate**]

【缺省情况】

根据不同的语音编解码协商允许的最高传真速率。

【视图】

POTS/VoIP语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[2400**]：优先使用最高传真速率为2400bps。

**[4800**]：优先使用V.27调制解调标准进行协商，最高传真速率为4800bps。

**[7200**]：优先使用V.29调制解调标准进行协商，最高传真速率为7200bps

**[9600**]：优先使用V.29调制解调标准进行协商，最高传真速率为9600bps。

**[12000**]：优先使用V.17调制解调标准进行协商，最高传真速率为12000bps。

**[14400**]：优先使用V.17调制解调标准进行协商，最高传真速率为14400bps。

**[disable**]：禁止传真功能。

**[voice**]：根据不同的语音编解码协商允许的最高传真速率。

·若使用G.711语音编解码协议，最高传真速率为14400bps，对应调制解调标准为V.17；

·若使用G.723.1 Annex A语音编解码协议，最高传真速率为4800bps，对应调制解调标准为V.27；

·若是用G.726语音编解码协议，最高传真速率为14400bps，对应调制解调标准为V.17；

·若使用G.729语音编解码协议，最高传真速率为7200bps，对应调制解调标准为V.29。

【使用指导】

如果速率配置为除"**disable**"、"**voice**"之外参数，则优先使用该速率对应的调制解调标准进行速率协商，如果协商不成功，就依次递减协商的速率，重新协商。这里配置的速率是允许的最高传真速率，而不是指定使用该速率进行传真。

【举例】

\# 配置优先使用V.29调制解调标准进行速率协商，最高传真速率为9600bps。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 4 pots

Sysname-voice-dial-entity4 fax rate 9600

**Fax over IP \-- Fax over IP配置命令 \-- fax train-mode**

------------------------------------------------------------------------

**[fax**] **train-mode**命令用来配置传真的训练方式。

**[undo**] **fax** **train-mode**命令用来恢复缺省情况。

【命令】

**[fax train-mode ** { **local** \| **ppp** }]

**[undo fax train-mode**]

【缺省情况】

使用端对端训练方式。

【视图】

POTS/VoIP语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[local**]：表示使用本地训练方式。

**[ppp**]：表示使用端对端训练方式。

【举例】

\# 使用本地训练方式。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 10 pots

Sysname-voice-dial-entity10 fax train-mode local

【相关命令】

·**fax** **local-train** **threshold**

**Fax over IP \-- Fax over IP配置命令 \-- modem passthrough**

------------------------------------------------------------------------

**[modem passthrough**]命令用来配置Modem透传的编解码类型和切换方式。

**[undo** **modem passthrough**]命令用来恢复缺省情况。

【命令】

**[modem passthrough** { **nse** [ **payload-type** *number*  \| **protocol** } **codec** { **g711alaw** \| **g711ulaw** }]]

**[undo modem passthrough**]

【缺省情况】

不使用Modem透传。

【视图】

POTS/VoIP语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[nse**]：配置使用NSE方式切换到Modem透传。

**[payload-type **]*number*：NSE方式切换时NSE报文的payload值，取值范围为98～120，缺省值为100。

**[protocol**]：配置使用SIP标准方式切换到Modem透传。

**[codec**]：Modem透传使用的编解码。

**[g711alaw**]：Modem透传时使用g711alaw编解码。

**[g711ulaw**]：Modem透传时使用g711mlaw编解码。

【使用指导】

·配置Modem透传时，需要保证在主被叫设备上配置相同的编解码类型和切换方式。如果使用NSE方式切换到Modem透传，主被叫设备上的payload值也需要保持一致。

·使用NSE方式切换到Modem透传时，静音抑制检测功能和回波抵消功能会自动关闭。

【举例】

\# 配置Modem透传的切换方式为SIP标准方式，编解码类型为g711alaw。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 550 voip

Sysname-voice-dial-entity550 modem passthrough protocol codec g711alaw

\# 配置Modem透传的切换方式为NSE方式，编解码类型为g711alaw。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 550 voip

Sysname-voice-dial-entity550 modem passthrough nse codec g711alaw

