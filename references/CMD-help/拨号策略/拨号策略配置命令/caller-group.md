
**拨号策略 \-- 拨号策略配置命令 \-- caller-group**

------------------------------------------------------------------------

**[caller-group**]命令用来将用户组绑定到指定的语音实体。

**[undo** **caller-group**]命令用来取消语音实体和用户组的绑定关系。

【命令】

**[caller-group**[ { **deny** \| **permit** } *group-id*]]

**[undo**[ **caller-group** { { **deny** \| **permit** } *group-id* \| **all** }]]

【缺省情况】

语音实体下没有绑定用户组，即允许任意主叫号码呼出/呼入。

【视图】

POTS/VoIP/IVR语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[deny**]：拒绝用户组中的主叫号码呼出/呼入。

**[permit**]：允许用户组中的主叫号码呼出/呼入。

*[group-id*]：绑定用户组ID，取值范围为1～2147483647。

**[all**]：绑定的所有用户组。

【举例】

\# 将用户组绑定到指定的语音实体，允许用户组1中的主叫号码呼出。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 1 voip

Sysname-voice-dial-entity1 caller-group permit 1

【相关命令】

·**subscriber-group**

**拨号策略 \-- 拨号策略配置命令 \-- caller-permit**

------------------------------------------------------------------------

**[caller-permit**]命令用来配置允许呼出/呼入的主叫号码模板。

**[undo** **caller-permit**]命令用来删除允许呼出/呼入的主叫号码模板。

【命令】

**[caller-permit** *caller-string*]

**[undo**[ **caller-permit** { *caller-string* \| **all** }]]

【缺省情况】

没有配置允许呼出/呼入的主叫号码模板，即对呼叫不做任何限制。

【视图】

POTS/VoIP/IVR语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：所有主叫号码模板。

*[caller-string*]：主叫号码模板，为1～31个字符的字符串，号码格式为{ [ +  *string*  \$  }\| \$]，符号说明如下：

·加号"+"：主叫号码模板如果以"+"号开头，"+"号表示整个号码是一个E.164标准号码，如+110022表示110022是符合E.164标准的号码。

·美元符号"\$"：只能放在结尾，表示主叫号码必须全部匹配\$之前的*string*部分。如果配置**caller-permit** \$，表示主叫号码为空。如果主叫号码模板后没有\$字符，则表示允许以此号码开头的主叫号码呼出/呼入，例如配置**caller-permit **20，表示允许以20开头的主叫号码呼出/呼入。

·*string*：由"0-9#＊[.!+%[]()-]"中的字符组合形成的字符串。各符号的含义如表1-1(?-294130838#_Ref148082585)所示。

表1-1 符号含义描述表

符号

含义

0-9

一位数字表示一位号码，0到9之间的数字

\#和＊

表示一位有效号码

.

通配符，可以与任何一位有效号码匹配。如：555. . . . 可以匹配任何以555开头的并有四位附加字符的号码

!

指明符号前的字符串重复零次或一次。如：56!1234可以匹配51234和561234

这些符号不能作为独立号码，之前必须有有效号码或号码串

+

指明符号前的字符串重复一次或多次。如： 9876(54)+可以匹配987654、98765454、9876545454、......等号码

%

指明符号前的字符串重复零次或多次。如：9876(54)%可以匹配9876、987654、98765454、9876545454、......等号码

-

连接符，用于连接两个数字（小的在前，大的在后），表示一个范围。如： 1-9表示从1到9（包括1和9）

符号"-"只能出现在" "中，且连接两端只能为数字，如0-9



表示字符选择范围，如： 1-36表示只可匹配单个字符1、2、3、6中的某一个

符号"  "和"( )"如果嵌套使用，则必须以"( [  )]"形式出现，不允许其它形式，如"   "、" ( ) "等

( )

表示一组字符，如：(123)表示字符串123，它一般与符号"!"、"%"、"+"一起使用，如：408(12)+，可以匹配40812或408121212等字符串，但不能匹配408，即12可连续出现且至少出现一次

![说明](拨号策略命令.files/image001.png)

每一个符号占用一个字符，符号 和( )占用两个字符。

【使用指导】

使用该命令最多可以配置32个允许呼出/呼入的主叫号码。

【举例】

\# 配置语音实体2允许主叫号码为1000和以20开头的主叫号码呼出。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 2 voip

Sysname-voice-dial-entity2 caller-permit 1000\$

Sysname-voice-dial-entity2 caller-permit 20

**拨号策略 \-- 拨号策略配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来配置用户组的描述信息。

**[undo description**]命令用来删除已配置的描述信息。

【命令】

**[description** *text*]

**[undo** **description**]

【缺省情况】

没有配置用户组的描述信息。

【视图】

用户组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：用户组描述字符串，为1～80个字符的字符串，区分大小写。

【举例】

\# 配置用户组10的描述信息为international。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial subscriber-group 10

Sysname-voice-dial-group10 description international

**拨号策略 \-- 拨号策略配置命令 \-- dial-prefix**

------------------------------------------------------------------------

**[dial-prefix**]命令用来配置号码前缀。

**[undo** **dial-prefix**]命令用来删除已配置的号码前缀。

【命令】

**[dial-prefix** *string*]

**[undo** **dial-prefix**]

【缺省情况】

没有配置号码前缀。

【视图】

POTS语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[string*]：号码前缀，为1～31个字符的字符串，由"0～9"、","、"\#"或"\*"中的字符组合形成的字符串。各符号的含义如[表]1-2(?-1356103434#_Ref169498719)所示。

表1-2 参数string中的符号含义

符号

含义

0-9

表示一位号码，可以是0到9之间的数字

,

一个逗号表示停顿500毫秒再发送下一个号码，可以出现在号码的任意位置

\#或\*

表示一位有效号码

【使用指导】

配置号码前缀后，设备以"号码前缀＋拨入号码"作为被叫号码。添加号码前缀后，如果号码总长度超过31位时，设备只发送前31位号码。

【举例】

\# 配置号码前缀为0。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 3 pots

Sysname-voice-dial-entity3 dial-prefix 0

【相关命令】

·**match-template**

**拨号策略 \-- 拨号策略配置命令 \-- dial-program**

------------------------------------------------------------------------

**[dial-program**]命令用来进入语音拨号策略视图。

**[undo** **dial-program**]命令用来删除语音拨号策略视图下的所有配置。

【命令】

**[dial-program**]

**[undo dial-program**]

【视图】

语音视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 进入语音拨号策略视图。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

**拨号策略 \-- 拨号策略配置命令 \-- dot-match**

------------------------------------------------------------------------

**[dot-match**]命令用来配置点号"**.**"的匹配规则。

**[undo** **dot-match**]命令用来恢复缺省情况。

【命令】

**[dot-match**[ { **end-only** \| **left-right** \| **right-left** }]]

**[undo** **dot-match**]

【缺省情况】

点号"**.**"的匹配规则为**end-only**。

【视图】

语音号码变换视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[end-only**]：表示只保留*input-template*中末尾所有点号"**.**"对应的号码。即无论*output-template*的末尾是否有点"**.**"，将*input-template*中末尾所有点号"**.**"对应的号码填充到*output-template*末尾。

**[left-right**]：表示以*output-template*格式中点的个数，从左至右提取*input-template*中点号"**.**"对应的号码。

**[right-left**]：表示以*output-template*格式中点的个数，从右至左提取*input-template*中点号"**.**"对应的号码。

![说明](拨号策略命令.files/image001.png)

上述描述中的*input-template*和*output-template*指的是**rule**命令中的参数。

【使用指导】

此处的"点号"匹配指的是虚号码匹配。虚号码匹配是指与正则表达式中的可变部分（如.+%\![]）进行匹配。例如号码1255与正则表达式进行虚号码匹配，与正则表达式1[23455]匹配的号码为2，与正则表达式125+匹配的号码为5，与正则表达式1..5匹配的号码为25。

需要注意的是，号码始终按照从左到右的顺序进行填充，与**dot-match**设置的参数无关。具体例子可参考命令**rule**中的举例。

【举例】

\# 设置号码变换表20的点号"**.**"匹配规则为**right-left**。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial number-substitute 20

Sysname-voice-dial-substitute20 dot-match right-left

【相关命令】

·**rule**

**拨号策略 \-- 拨号策略配置命令 \-- entity hunt**

------------------------------------------------------------------------

**[entity hunt**]命令用来配置语音实体的选取规则顺序。

**[undo** **entity hunt**]命令用来恢复缺省情况。

【命令】

**[entity hunt ***hunt-number*]

**[undo entity hunt**]

【缺省情况】

语音实体的选取规则顺序为0，即首先采用精确匹配，其次是语音实体优先级，最后是随机选择。

【视图】

语音拨号视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[hunt-number*]：语音实体的选取规则顺序，取值范围为0～7。

0：语音实体的选取规则依次为精确匹配，语音实体的优先级，随机选择。

1：语音实体的选取规则依次为精确匹配，语音实体的优先级，最久不使用。

2：语音实体的选取规则依次为语音实体的优先级，精确匹配，随机选择。

3：语音实体的选取规则依次为语音实体的优先级，精确匹配，最久不使用。

4：语音实体的选取规则依次为最久不使用，精确匹配语，语音实体的优先级。

5：语音实体的选取规则依次为最久不使用，语音实体的优先级，精确匹配。

6：语音实体的选取规则为随机选择。

7：语音实体的选取规则为最久不使用。

表1-3 规则描述

规则

描述

精确匹配

号码串从左至右，匹配的号码位越多，精确度越高，一旦遇到不能唯一匹配的号码，该规则停止

语音实体的优先级

通过**priority**命令可以将语音实体的优先级共分为11级，优先级高的语音实体会被优先匹配

随机选择

随机从符合条件的语音实体中选取一个

最久不使用

选择最长时间没有使用的语音实体

【使用指导】

当号码能匹配多个语音实体时，设备会根据配置的选取规则顺序来选择语音实体。如果应用第一个规则后仍无法区别语音实体的优先级顺序，就应用第二个选取规则，依此类推。

【举例】

\# 配置语音实体的选取规则顺序为3。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity hunt 3

【相关命令】

·**priority**

**拨号策略 \-- 拨号策略配置命令 \-- first-rule**

------------------------------------------------------------------------

**[first-rule**]命令用来配置号码变换表首先使用的号码变换规则ID。

**[undo** **first-rule**]命令用来取消已有配置。

【命令】

**[first-rule** *id*]

**[undo** **first-rule**]

【缺省情况】

没有配置首先使用的号码变换规则ID。

【视图】

语音号码变换视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[id*]：首先使用的号码变换规则ID，取值范围为0～31。

【使用指导】

在匹配号码变换规则时，首先使用**first-rule**命令设置的号码变换规则。如果未配置或匹配首选变换规则失败，则顺序匹配其他号码变换规则。

【举例】

\# 设置号码变换表20首先使用号码变换规则4。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial number-substitute 20

Sysname-voice-dial-substitute20 rule 4 663 3

Sysname-voice-dial-substitute20 first-rule 4

【相关命令】

·**rule**

**拨号策略 \-- 拨号策略配置命令 \-- match-template**

------------------------------------------------------------------------

**[match-template**]命令用来配置用户组的主叫号码模板。

**[undo** **match-template**]命令用来删除已配置的主叫号码模板。

【命令】

**[match-template** *match-string*]

**[undo**[ **match-template** { *match-string* \| **all** }]]

【缺省情况】

用户组下没有配置主叫号码模板。

【视图】

用户组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：所有主叫号码模板。

*[caller-string*]：主叫号码模板，为1～31个字符的字符串，号码格式为{ [ +  *string*  \$  }\| \$]，符号说明如下：

·加号"+"：主叫号码模板如果以"+"号开头，"+"号表示整个号码是一个E.164标准号码，如+110022表示110022是符合E.164标准的号码。

·美元符号"\$"：只能放在结尾，表示主叫号码必须全部匹配\$之前的*string*部分。如果配置**match-template** \$，表示主叫号码为空。如果主叫号码模板后没有\$字符，则表示允许以此号码开头的主叫号码呼出/呼入，例如配置**match-template** 20，表示允许以20开头的主叫号码呼出/呼入。

·*string*：由"0-9#＊[.!+%[]()-]"中的字符组合形成的字符串。各符号的含义如表1-4(?-1681238638#_Ref341709313)所示。

表1-4 符号含义描述表

符号

含义

0-9

一位数字表示一位号码，0到9之间的数字

\#和＊

表示一位有效号码

.

通配符，可以与任何一位有效号码匹配。如：555. . . . 可以匹配任何以555开头的并有四位附加字符的号码

!

指明符号前的字符串重复零次或一次。如：56!1234可以匹配51234和561234

符号"!%+"前的字符串（一位号码或号码串），作为非精确匹配的号码，处理类似"**.**"通配符；这些符号不能作为独立号码，之前必须有有效号码或号码串

+

指明符号前的字符串重复一次或多次。如： 9876(54)+可以匹配987654、98765454、9876545454、......等号码

%

指明符号前的字符串重复零次或多次。如：9876(54)%可以匹配9876、987654、98765454、9876545454、......等号码

-

连接符，用于连接两个数字（小的在前，大的在后），表示一个范围。如： 1-9表示从1到9（包括1和9）

符号"-"只能出现在" "中，且连接两端只能为数字，如0-9



表示字符选择范围，如： 1-36表示只可匹配单个字符1、2、3、6中的某一个

符号"  "和"( )"如果嵌套使用，则必须以"( [  )]"形式出现，不允许其它形式，如"   "、" ( ) "等

( )

表示一组字符，如：(123)表示字符串123，它一般与符号"!"、"%"、"+"一起使用，如：408(12)+，可以匹配40812或408121212等字符串，但不能匹配408，即12可连续出现且至少出现一次

![说明](拨号策略命令.files/image001.png)

每一个符号占用一个字符，符号 和( )占用两个字符。

【举例】

\# 配置用户组2的主叫号码模板为1...，表示允许以1开头的四位主叫号码。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial subscriber-group 2

Sysname-voice-dial-group2 match-template 1...

**拨号策略 \-- 拨号策略配置命令 \-- max-conn**

------------------------------------------------------------------------

**[max-conn**]命令用来配置最大呼叫连接数。

**[undo** **max-conn**]命令用来删除最大呼叫连接数。

【命令】

**[max-conn** *max-number*]

**[undo max-conn**]

【缺省情况】

没有配置最大呼叫连接数，即不对呼叫连接数进行限制。

【视图】

POTS/VoIP/IVR语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[max-number*]：最大呼叫连接数，取值范围为0～120。0表示不允许呼叫。

【举例】

\# 设置语音实体的最大呼叫连接数为5。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 10 voip

Sysname-voice-dial-entity10 max-conn 5

**拨号策略 \-- 拨号策略配置命令 \-- number-match**

------------------------------------------------------------------------

**[number-match**]命令用来配置号码匹配策略。

**[undo** **number-match**]命令用来恢复缺省情况。

【命令】

**[number-match**[ { **longest** \| **shortest** }]]

**[undo** **number-match**]

【缺省情况】

使用最短号码匹配策略。

【视图】

语音拨号策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[longest**]：使用最长号码匹配策略。

**[shortest**]：使用最短号码匹配策略。

【举例】

\# 配置使用最长号码匹配策略。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial number-match longest

【相关命令】

·**terminator**

**拨号策略 \-- 拨号策略配置命令 \-- number-substitute**

------------------------------------------------------------------------

**[number-substitute**]命令用来创建号码变换规则表，并进入语音号码变换视图。

**[undo** **number-substitute**]命令用来删除已配置的号码变换规则表。

【命令】

**[number-substitute** *list-number*]

**[undo**[ **number-substitute** { *list-number* \| **all** }]]

【缺省情况】

不存在号码变换规则表。

【视图】

语音拨号策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[list-number*]：号码变换规则表的序号，取值范围为1～2147483647。

**[all**]：所有号码变换规则表。

【举例】

\# 创建号码变换规则表，并进入语音号码变换视图。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial number-substitute 1

Sysname-voice-dial-substitute1

**拨号策略 \-- 拨号策略配置命令 \-- priority**

------------------------------------------------------------------------

**[priority**]命令用来配置语音实体的优先级。

**[undo** **priority**]命令用来恢复缺省情况。

【命令】

**[priority*** priority-order*]

**[undo** **priority**]

【缺省情况】

优先级别为0。

【视图】

POTS/VoIP/IVR语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[priority-order*]：语音实体的优先级，取值范围为0～10，数值越小表示优先级越高。

【使用指导】

当存在多个相同的号码模板时，优先级高的语音实体会被优先匹配。

【举例】

\# 配置语音实体10的优先级为5。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 10 pots

Sysname-voice-dial-entity10 priority 5

**拨号策略 \-- 拨号策略配置命令 \-- private-line**

------------------------------------------------------------------------

**[private-line**]命令用来配置专线自动振铃功能。

**[undo** **private-line**]命令用来关闭专线自动振铃功能。

【命令】

**[private-line** *string*]

**[undo** **private-line**]

【缺省情况】

没有配置专线自动振铃功能。

【视图】

FXS/FXO/E&M/数字语音用户线视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[string*]：被叫号码，为1～31个字符的字符串，可包含0～9、"＊"和"**\#**"。

【使用指导】

配置专线自动振铃功能后，用户摘机后不需要做任何拨号操作，设备会将*string*作为被叫号码自动拨出。

【举例】

\# 配置专线自动振铃功能。

\<Sysname\> system-view

Sysname subscriber-line 2/1/1

Sysname-subscriber-line2/1/1 private-line 1000

**拨号策略 \-- 拨号策略配置命令 \-- rule**

------------------------------------------------------------------------

**[rule**]命令用来配置号码变换规则。

**[undo** **rule**]命令用来删除号码变换规则。

【命令】

**[rule**[ *id* *input-template output-template* [ **number-type** *input-number-type output-number-type* \| **numbering-plan** *input-numbering-plan output-numbering-plan* ] \*]]

**[undo**[ **rule** { *id* \| **all** }]]

【缺省情况】

没有配置号码变换规则。

【视图】

语音号码变换视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：所有号码变换规则。

*[id*]：号码变换规则ID，取值范围为0～31。

*[input-template*]：号码变换的输入匹配模板，为1～31个字符的字符串，号码格式为 **\^**   +  *string*  \$ ，符号说明如下：

·脱字符"\^"：表示必须从字符串的第一个字符开始匹配。

· 加号"{.ItemStepChar}+{.ItemStepChar}"："{.ItemStepChar}+{.ItemStepChar}"号本身不具备特殊含义，仅表示一位有效号码，以"{.ItemStepChar}+{.ItemStepChar}"号开头的号码是一个{.ItemStepChar}E.164{.ItemStepChar}标准号码。{.ItemStepChar}

·美元符号"\$"：表示必须与号码串的最后一个字符匹配，即用户号码和匹配串进行匹配时，用户号码的最后一个号码必须与匹配串的最后一个字符相匹配。{.ItemStepChar}

·*string*：由"0-9#＊.!%"中的字符组合形成的字符串。各符号的含义如[表]1-5(?1629595628#_Ref354745785)所示。

表1-5 参数*string*中的符号含义

符号

含义

0-9

一位数字表示一位号码，0到9之间的数字

\#和＊

表示一位有效号码

.

通配符，可以与任何一位有效号码匹配。如：555. . . . 可以匹配任何以555开头的并有四位附加字符的号码

!

指明符号前的字符串重复零次或一次。如：56!1234可以匹配51234和561234

这些符号不能作为独立号码，之前必须有有效号码或号码串

%

指明符号前的字符串重复零次或多次。如：54%可以匹配54、5454、......等号码

*[output-template*]：号码变换的输出匹配模板，为1～31个字符的字符串，由"0-9#＊."中的字符组合形成的字符串，首位支持加号"{.ItemStepChar}+{.ItemStepChar}"{.ItemStepChar}。各符号的含义如[表]1-5(?1629595628#_Ref354745785)所示。

**[number-type**]：号码类型。

*[input-number-type*]：输入号码的号码类型。取值范围请参见[表]1-6(?1629595628#_Ref154835875)。

表1-6 输入号码的号码类型

号码类型

描述

abbreviated

缩位号码

any

任意

international

国际号码

national

同一国家但不在本地网络的号码

network

特定服务网络的号码

reserved

扩展保留号码

subscriber

同一个本地网络的号码

unknown

未知号码类型

*[output-number-type*]：输出号码的号码类型。取值范围请参见[表]1-7(?1629595628#_Ref154892305)。

表1-7 输出号码的号码类型

号码类型

描述

abbreviated

缩位号码

international

国际号码

national

同一国家但不在本地网络的号码

network

特定服务网络的号码

reserved

扩展保留号码

subscriber

同一个本地网络的号码

unknown

未知号码类型

**[numbering-plan**]：编码方案。

*[input-numbering-plan*]：输入号码的编码方案。取值范围请参见[表]1-8(?1629595628#_Ref154892345)。

表1-8 输入号码的编码方案

编码方案

描述

any

任意

data

数据编码方案

isdn

ISDN电话编码方案

national

国内编码方案

private

专用编码方案

reserved

扩展保留

telex

用户电报编码方案

unknown

未知编码方案

*[output-numbering-plan*]：输出号码的编码方案。取值范围参见请[表]1-9(?1629595628#_Ref154892367)。

表1-9 输出号码的编码方案

编码方案

描述

data

数据编码方案

isdn

ISDN电话编码方案

national

国内编码方案

private

专用编码方案

reserved

扩展保留

telex

用户电报编码方案

unknown

未知编码方案

【使用指导】

对于参数*input-template*和*output-template*中点号"**.**"分3种情况进行处理：

(1)*output-**template*点号无效

**[dot-match**]命令配置点号的匹配规则为**end-only**时，*output*-*template*中点号无效，只需要将*input-template*参数中末尾所有点号所对应的号码保留至*output-template*中号码的末尾。

例如配置如下规则：

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial number-substitute 1

Sysname-voice-dial-substitute1 dot-match end-only

Sysname-voice-dial-substitute1 rule 0 \^..10\...\$ \...267410.

假设在主叫设备上进行如上配置，并对被叫号码进行变换。主叫拨打电话9810765，匹配输入号码模板后的号码是765，经过号码变换后的号码为267410765。

(2)丢弃*output-**template*中多余的点号

**[dot-match**]命令配置点号的匹配规则**right-left**或**left-right**，并且*output-template*中点号位数大于*input-template*中点号的位数时，取*input-template*中点号对应的全部号码，按从左至右的顺序依次替换*output-template*中的点号，*output-template*中多余的点号会被丢弃。

例如配置如下规则：

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial number-substitute 1

Sysname-voice-dial-substitute1 dot-match right-left

Sysname-voice-dial-substitute1 rule 0 \^..10..\$ ..267410\...

假设在主叫设备上进行如上配置，并对被叫号码进行变换。主叫拨打电话981074，匹配输入号码模板后的号码是9874，所以经过号码变换后的号码为9826741074。

(3)丢弃*input-**template*中多余点号所对应的号码

**[dot-match**]命令配置点号的匹配规则为**right-left**或**left-right**，并且*input-template*中点号位数大于或等于*output-template*中点号位数时，根据*output-template*中点号"**.**"的位数，从*input-template*中点号所对应的号码中按照从右至左/从左至右顺序提取相应位数的号码，依次替换*output-template*中的点号，*input-template*中没有被提取的点号所对应的号码会被丢弃。

例如配置如下规则：

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial number-substitute 1

Sysname-voice-dial-substitute1 dot-match right-left

Sysname-voice-dial-substitute1 rule 0 \^..10\...\$ ..267410..

假设在主叫设备上进行如上配置，并对被叫号码进行变换。主叫拨打电话9810765，匹配输入号码模板后的号码是8765，所以经过号码变换后的号码为8726741065。

【举例】

\# 创建号码变换规则表1，配置号码变换规则0，号码变换的输入匹配模板为\^..01\...\$，号码变换的输出匹配模板为\...1。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial number-substitute 1

Sysname-voice-dial-substitute1 rule 0 \^..01\...\$ \...1

【相关命令】

·**dot-match**

·**first-rule**

·**substitute** (Voice dial-program view)

·**substitute **(Voice entity view/Voice subscriber-line view)

**拨号策略 \-- 拨号策略配置命令 \-- send-number**

------------------------------------------------------------------------

**[send-number**]命令用来配置发送号码的控制方式。

**[undo** **send-number**]命令用来恢复缺省情况。

【命令】

**[send-number**[ { *digit-number* \| **all** \| **truncate** }]]

**[undo** **send-number**]

【缺省情况】

采用**truncate**方式发送号码。

【视图】

POTS语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[digit-number*]：号码发送的长度（从号码末尾依次向前提取），取值范围为0～31。数值不大于被叫号码的位数。

**[all**]：发送全部被叫号码。

**[truncate**]：按号码截断方式发送被叫号码，即当**match-template**命令配置的号码中包含点号"**.**"时，仅发送与号码模板末尾的点号匹配的号码。

【举例】

\# 配置发送全部被叫号码。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 10 pots

Sysname-voice-dial-entity10 send-number all

【相关命令】

·**match-template**

**拨号策略 \-- 拨号策略配置命令 \-- subscriber-group**

------------------------------------------------------------------------

**[subscriber-group**]命令用来创建一个用户组，并进入用户组视图。

**[undo** **subscriber-group**]命令用来删除用户组。

【命令】

**[subscriber-group** *group-id*]

**[undo**[ **subscriber-group** { *group-id* \| **all** }]]

【缺省情况】

没有创建任何用户组。

【视图】

语音拨号视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-id*]：用户组ID，取值范围为1～2147483647。

**[all**]：所有用户组。

【使用指导】

在设备上最多可以创建10个用户组。

【举例】

\# 创建一个用户组，并进入用户组视图。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial subscriber-group 1

Sysname-voice-dial-group1

**拨号策略 \-- 拨号策略配置命令 \-- substitute (Voice entity view/Voice subscriber-line view)**

------------------------------------------------------------------------

**[substitute**]命令用来将号码变换规则表绑定到指定语音实体或语音用户线。

**[undo** **substitute**]命令用来取消绑定关系。

【命令】

**[substitute**[ { **called** \| **calling** } *list-number*]]

**[undo**[ **substitute** { **called** \| **calling** }]]

【缺省情况】

没有绑定号码变换规则表，即不进行号码变换。

【视图】

POTS/VoIP/IVR语音实体视图/语音用户线视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[called**]：对被叫号码应用号码变换。

**[calling**]：对主叫号码应用号码变换。

*[list-number*]：绑定的号码变换规则表的序号，取值范围为1～2147483647。

【举例】

\# 配置将号码变换规则表6绑定到语音实体10，表示对被叫号码应用号码变换。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 10 pots

Sysname-voice-dial-entity10 substitute called 6

\# 配置将号码变换规则表6绑定到语音用户线2/1/1，表示对被叫号码应用号码变换。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice subscriber-line2/1/1

Sysname-voice-line2/1/1 substitute called 6

【相关命令】

·**number-substitute**

·**rule**

**拨号策略 \-- 拨号策略配置命令 \-- substitute (Voice dial-program view)**

------------------------------------------------------------------------

**[substitute**]命令用来将号码变换规则表绑定到入局/出局呼叫的主/被叫号码。

**[undo** **substitute**]命令用来取消绑定关系。

【命令】

**[substitute**[ { **incoming-call** \| **outgoing-call** } { **called** \| **calling** } *list-number*]]

**[undo**[ **substitute** { **incoming-call** \| **outgoing-call** } { **called** \| **calling** } { *list-number* \| **all** }]]

【缺省情况】

没有绑定号码变换规则表，即不进行号码变换。

【视图】

语音拨号策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[incoming-call**]：将号码变换规则表绑定到入局呼叫。

**[outgoing-call**]：将号码变换规则表绑定到出局呼叫。

**[called**]：对被叫号码应用号码变换。

**[calling**]：对主叫号码应用号码变换。

**[all**]：所有的号码变换规则表。

*[list-number*]：绑定的号码变换规则表的序号，取值范围为1～2147483647。

【使用指导】

最多可以绑定32个号码变换规则表。

【举例】

\# 配置将号码变换规则表5绑定到入局呼叫的被叫号码。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial substitute incoming-call called 5

\# 配置将号码变换规则表5、6、8绑定到出局呼叫的被叫号码。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial substitute outgoing-call called 5

Sysname-voice-dial substitute outgoing-call called 6

Sysname-voice-dial substitute outgoing-call called 8

【相关命令】

·**number-substitute**

·**rule**

**拨号策略 \-- 拨号策略配置命令 \-- terminator**

------------------------------------------------------------------------

**[terminator**]命令用来配置拨号终结符。

**[undo** **terminator**]命令用来取消已有配置。

【命令】

**[terminator** *character*]

**[undo** **terminator**]

【缺省情况】

没有配置拨号终结符。

【视图】

语音拨号策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[character*]：拨号终结符，取值范围为数字0～9、"\#"、"＊"。

【使用指导】

·拨号终结符用来表示拨号已经结束，设备接收到这个符号就会根据所拨的号码发起呼叫，即使配置使用最长号码匹配策略，也不会再等待。

·请避免将被叫号码中包含的字符或号码配置为终结符。

【举例】

\# 配置拨号终结符为"\#"。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial terminator \#

