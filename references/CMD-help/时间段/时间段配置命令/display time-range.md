<!-- CMD-INDEX
  display time-range                  | 任意视图             | L6
  time-range                          | 系统视图             | L74
-->

**时间段 \-- 时间段配置命令 \-- display time-range**

------------------------------------------------------------------------

**[display** **time-range**]命令用来显示时间段的配置和状态信息。

【命令】

**[display**[ **time-range** { *time-range-name* \| **all** }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[time-range-name*]：显示指定名称时间段的配置和状态信息。*time-range-name*表示时间段的名称，为1～32个字符的字符串，不区分大小写，必须以英文字母a～z或A～Z开头。

**[all**]：显示所有时间段的配置和状态信息。

【举例】

\# 显示时间段t4的配置和状态信息。

\<Sysname\> display time-range t4

Current time is 17:12:34 11/23/2010 Tuesday

Time-range : t4 (Inactive)

 10:00 to 12:00 Mon

 14:00 to 16:00 Wed

 from 00:00 1/1/2011 to 00:00 1/1/2012

 from 00:00 6/1/2011 to 00:00 7/1/2011

表1-1 display time-range命令显示信息描述表

字段

描述

Current time

系统当前的时间

Time-range

时间段的配置信息，包括：

·时间段的名称

·时间段的状态，包括Active（生效）和Inactive（未生效）两种状态

·时间段的时间范围

**时间段 \-- 时间段配置命令 \-- time-range**

------------------------------------------------------------------------

**[time-range**]命令用来创建一个时间段，来描述一个特定的时间范围。

**[undo** **time-range**]命令用来删除一个时间段。

【命令】

**[time-range** *time-range-name* { *start-time* **to** *end-time* *days* [ **from** *time1* *date1*   **to** *time2* *date2*  \| **from** *time1* *date1*  **to** *time2* *date2*  \| **to** *time2* *date2* }]]

**[undo** **time-range** *time-range-name* [ *start-time* **to** *end-time* *days* [ **from** *time1* *date1*   **to** *time2* *date2*  \| **from** *time1* *date1*  **to** *time2* *date2*  \| **to** *time2* *date2* ]]]

【缺省情况】

不存在任何时间段。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time-range-name*]：指定时间段的名称，为1～32个字符的字符串，不区分大小写，必须以英文字母a～z或A～Z开头。为避免混淆，时间段的名称不允许使用英文单词all。

*[start-time* **to** *end-time*]：指定周期时间段的时间范围。*start-time*表示起始时间，格式为hh:mm，取值范围为00:00～23:59；*end-time*表示结束时间，格式为hh:mm，取值范围为00:00～24:00，且结束时间必须大于起始时间。

*[days*]：指定周期时间段在每周的周几生效。本参数可输入多次，但后输入的值不能与此前输入的值完全重叠（譬如输入**6**后不允许再输入**sat**，但允许再输入**off-day**），系统将取各次输入值的并集作为最终值（譬如依次输入**1**、**wed**和**working-day**之后，最终生效的时间将为每周的工作日）。本参数可输入的形式如下：

·数字：取值范围为0～6，依次表示周日～周六；

·周几的英文缩写（从周日到周六依次为**sun**、**mon**、**tue**、**wed**、**thu**、**fri**和**sat**）；

·工作日（**working-day**）：表示从周一到周五；

·休息日（**off-day**）：表示周六和周日；

·每日（**daily**）：表示一周七天。

**[from** *time1* *date1*]：指定绝对时间段的起始时间。*time1*的格式为hh:mm，取值范围为00:00～23:59。*date1*的格式为MM/DD/YYYY或YYYY/MM/DD。MM表示月，取值范围为1～12；DD表示日，取值范围取决于所输入的月份；YYYY表示年，取值范围为1970～2100。若未指定本参数，绝对时间段的起始时间将为系统可表示的最早时间，即1970年1月1日0点0分。

**[to** *time2* *date2*]：指定绝对时间段的结束时间。*time2*的格式为hh:mm，取值范围为00:00～24:00。*date2*的格式为MM/DD/YYYY或YYYY/MM/DD。MM表示月，取值范围为1～12；DD表示日，取值范围取决于所输入的月份；YYYY表示年，取值范围为1970～2100。结束时间必须大于起始时间。若未指定本参数，绝对时间段的结束时间将为系统可表示的最晚时间，即2100年12月31日24点0分。

【使用指导】

·使用**time-range**命令时，如果指定名称的时间段不存在，则创建一个新的时间段（最多1024个）；如果指定名称的时间段已存在，则对旧时间段进行修改，即在其原有内容的基础上叠加新的内容。

·使用*start-time* **to** *end-time* *days*这组参数所创建的时间段为周期时间段，它将以一周为周期循环生效；使用**from** *time1* *date1*和**to** *time2* *date2*这组参数所创建的时间段为绝对时间段，它将在指定时间范围内生效；而同时使用了上述两组参数所创建的时间段，将取周期时间段和绝对时间段的交集作为生效的时间范围，譬如：创建一个时间段，既定义其在每周一的8点到12点生效，又定义其在2011年全年生效，那么其最终将在2011年全年内每周一的8点到12点生效。

·一个时间段内可包含一或多个周期时间段（最多32个）和绝对时间段（最多12个），当包含有多个周期时间段和绝对时间段时，系统将先分别取各周期时间段的并集和各绝对时间段的并集，再取这两个并集的交集作为该时间段最终生效的时间范围。

【举例】

\# 创建名为t1的时间段，其时间范围为每周工作日的8点到18点。

\<Sysname\> system-view

Sysname time-range t1 08:00 to 18:00 working-day

\# 创建名为t2的时间段，其时间范围为2011年全年。

\<Sysname\> system-view

Sysname time-range t2 from 00:00 1/1/2011 to 24:00 12/31/2011

\# 创建名为t3的时间段，其时间范围为2011年全年内每周休息日的8点到12点。

\<Sysname\> system-view

Sysname time-range t3 08:00 to 12:00 off-day from 00:00 1/1/2011 to 24:00 12/31/2011

\# 创建名为t4的时间段，其时间范围为2011年1月和6月内每周一的10点到12点以及每周三的14到16点。

\<Sysname\> system-view

Sysname time-range t4 10:00 to 12:00 1 from 00:00 1/1/2011 to 24:00 1/31/2011

Sysname time-range t4 14:00 to 16:00 3 from 00:00 6/1/2011 to 24:00 6/30/2011

【相关命令】

·**display** **time-range**
