::: {#-47672824 .myid}
[]{#_Toc86742806}[]{#_Toc80178012}[]{#_Toc80177406}[]{#_Toc404792085}[]{#struct_0_36812_x2234_x1344990334}[]{#_Toc291080246}

**时间段 \-- 时间段配置命令 \-- display time-range**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **time-range**]{lang="EN-US"}]{#struct_0_36812_x2234_x1020575210}[命令用来显示时间段的配置和状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_36812_x2234_x1616192414}

[**[display]{lang="EN-US"}**[ **time-range** { *time-range-name* \| **all** }]{lang="EN-US"}]{#struct_0_36812_x2234_x1220745358}

[[【视图】]{style="font-family:黑体"}]{#struct_0_36812_x2234_450572626}

[[任意视图]{style="font-family:宋体"}]{#struct_0_36812_x2234_1825175683}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_36812_x2234_x431198149}

[[network-admin]{lang="EN-US"}]{#struct_0_36812_x2234_x1026455836}

[[network-operator]{lang="EN-US"}]{#struct_0_36812_x2234_x729360710}

[[mdc-admin]{lang="EN-US"}]{#struct_0_36812_x2234_x2020605675}

[[mdc-operator]{lang="EN-US"}]{#struct_0_36812_x2234_x429762906}

[[【参数】]{style="font-family:黑体"}]{#struct_0_36812_x2234_1430383281}

[*[time-range-name]{lang="EN-US"}*]{#struct_0_36812_x2234_x1781364271}[：显示指定名称时间段的配置和状态信息。]{style="font-family:宋体"}*[time-range-name]{lang="EN-US"}*[表示时间段的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写，必须以英文字母]{style="font-family:宋体"}[a]{lang="EN-US"}[～]{style="font-family:宋体"}[z]{lang="EN-US"}[或]{style="font-family:
宋体"}[A]{lang="EN-US"}[～]{style="font-family:宋体"}[Z]{lang="EN-US"}[开头。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_36812_x2234_x1082707608}[：显示所有时间段的配置和状态信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_36812_x2234_x363707709}

[[\# ]{lang="EN-US"}]{#struct_0_36812_x2234_x727625308}[显示时间段]{style="font-family:宋体"}[t4]{lang="EN-US"}[的配置和状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display time-range t4]{lang="EN-US"}]{#struct_0_36812_x2234_x431263685}

[Current time is 17:12:34 11/23/2010 Tuesday]{lang="EN-US"}

[ ]{lang="EN-US"}

[Time-range : t4 (Inactive)]{lang="EN-US"}

[ 10:00 to 12:00 Mon]{lang="EN-US"}

[ 14:00 to 16:00 Wed]{lang="EN-US"}

[ from 00:00 1/1/2011 to 00:00 1/1/2012]{lang="EN-US"}

[ from 00:00 6/1/2011 to 00:00 7/1/2011]{lang="EN-US"}

[]{#struct_0_36812_x2234_x969189756}[[表1-1 ]{lang="EN-US"}[display time-range]{lang="EN-US"}]{#_Toc138129446}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x229934408}[[字段]{style="font-family:黑体"}]{#struct_0_36812_x2234_747761793}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_36812_x2234_1162633571}

[[Current time]{lang="EN-US"}]{#struct_0_36812_x2234_x165826220}

[[系统当前的时间]{style="font-family:宋体"}]{#struct_0_36812_x2234_x702554772}

[[Time-range]{lang="EN-US"}]{#struct_0_36812_x2234_x431722436}

[[时间段的配置信息，包括：]{style="font-family:宋体"}]{#struct_0_36812_x2234_1368378351}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[时间段的名称]{lang="EN-US" style="font-family:宋体"}]{#struct_0_36812_x2234_1254469396}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[时间段的状态，包括]{lang="EN-US" style="font-family:宋体"}[Active]{lang="EN-US"}]{#struct_0_36812_x2234_165631185}[（生效）和]{lang="EN-US" style="font-family:宋体"}[Inactive]{lang="EN-US"}[（未生效）两种状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[时间段的时间范围]{lang="EN-US" style="font-family:宋体"}]{#struct_0_36812_x2234_604745883}

[ ]{lang="EN-US"}

::: {#1603341627 .myid}
[]{#_Toc404792086}[]{#struct_0_36812_x2234_x1941779800}[]{#_Toc291080268}

**时间段 \-- 时间段配置命令 \-- time-range**

------------------------------------------------------------------------

[**[time-range]{lang="EN-US"}**]{#struct_0_36812_x2234_793970310}[命令用来创建一个时间段，来描述一个特定的时间范围。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **time-range**]{lang="EN-US"}]{#struct_0_36812_x2234_x954306709}[命令用来删除一个时间段。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_36812_x2234_x431787972}

[**[time-range]{lang="EN-US"}**[ *time-range-name* { *start-time* **to** *end-time* *days* \[ **from** *time1* *date1* \] \[ **to** *time2* *date2* \] \| **from** *time1* *date1* \[ **to** *time2* *date2* \] \| **to** *time2* *date2* }]{lang="EN-US"}]{#struct_0_36812_x2234_1781236964}

[**[undo]{lang="EN-US"}**[ **time-range** *time-range-name* \[ *start-time* **to** *end-time* *days* \[ **from** *time1* *date1* \] \[ **to** *time2* *date2* \] \| **from** *time1* *date1* \[ **to** *time2* *date2* \] \| **to** *time2* *date2* \]]{lang="EN-US"}]{#struct_0_36812_x2234_x560832277}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_36812_x2234_x1109718276}

[[不存在任何时间段。]{style="font-family:宋体"}]{#struct_0_36812_x2234_x1706697440}

[[【视图】]{style="font-family:黑体"}]{#struct_0_36812_x2234_x1989561725}

[[系统视图]{style="font-family:宋体"}]{#struct_0_36812_x2234_270592467}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_36812_x2234_x693704570}

[[network-admin]{lang="EN-US"}]{#struct_0_36812_x2234_392951988}

[[mdc-admin]{lang="EN-US"}]{#struct_0_36812_x2234_x431853508}

[[【参数】]{style="font-family:黑体"}]{#struct_0_36812_x2234_606361522}

[*[time-range-name]{lang="EN-US"}*]{#struct_0_36812_x2234_35552294}[：指定时间段的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写，必须以英文字母]{style="font-family:宋体"}[a]{lang="EN-US"}[～]{style="font-family:宋体"}[z]{lang="EN-US"}[或]{style="font-family:
宋体"}[A]{lang="EN-US"}[～]{style="font-family:宋体"}[Z]{lang="EN-US"}[开头。为避免混淆，时间段的名称不允许使用英文单词]{style="font-family:宋体"}[all]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[start-time]{lang="EN-US"}*[ **to** *end-time*]{lang="EN-US"}]{#struct_0_36812_x2234_x511883955}[：指定周期时间段的时间范围。]{style="font-family:宋体"}*[start-time]{lang="EN-US"}*[表示起始时间，格式为]{style="font-family:宋体"}[hh:mm]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[00:00]{lang="EN-US"}[～]{style="font-family:宋体"}[23:59]{lang="EN-US"}[；]{style="font-family:宋体"}*[end-time]{lang="EN-US"}*[表示结束时间，格式为]{style="font-family:宋体"}[hh:mm]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[00:00]{lang="EN-US"}[～]{style="font-family:宋体"}[24:00]{lang="EN-US"}[，且结束时间必须大于起始时间。]{style="font-family:宋体"}

[*[days]{lang="EN-US"}*]{#struct_0_36812_x2234_1853715788}[：指定周期时间段在每周的周几生效。本参数可输入多次，但后输入的值不能与此前输入的值完全重叠（譬如输入]{style="font-family:宋体"}**[6]{lang="EN-US"}**[后不允许再输入]{style="font-family:宋体"}**[sat]{lang="EN-US"}**[，但允许再输入]{style="font-family:宋体"}**[off-day]{lang="EN-US"}**[），系统将取各次输入值的并集作为最终值（譬如依次输入]{style="font-family:宋体"}**[1]{lang="EN-US"}**[、]{style="font-family:宋体"}**[wed]{lang="EN-US"}**[和]{style="font-family:宋体"}**[working-day]{lang="EN-US"}**[之后，最终生效的时间将为每周的工作日）。本参数可输入的形式如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[数字：取值范围为]{style="font-family:宋体"}]{#struct_0_36812_x2234_x967844447}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[6]{lang="EN-US"}[，依次表示周日～周六；]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[周几的英文缩写（从周日到周六依次为]{style="font-family:宋体"}]{#struct_0_36812_x2234_2034627632}**[sun]{lang="EN-US"}**[、]{style="font-family:宋体"}**[mon]{lang="EN-US"}**[、]{style="font-family:宋体"}**[tue]{lang="EN-US"}**[、]{style="font-family:宋体"}**[wed]{lang="EN-US"}**[、]{style="font-family:宋体"}**[thu]{lang="EN-US"}**[、]{style="font-family:宋体"}**[fri]{lang="EN-US"}**[和]{style="font-family:宋体"}**[sat]{lang="EN-US"}**[）；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[工作日（]{lang="EN-US" style="font-family:宋体"}**[working-day]{lang="EN-US"}**]{#struct_0_36812_x2234_1793174282}[）：表示从周一到周五；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[休息日（]{lang="EN-US" style="font-family:宋体"}**[off-day]{lang="EN-US"}**]{#struct_0_36812_x2234_1357720305}[）：表示周六和周日；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每日（]{lang="EN-US" style="font-family:宋体"}**[daily]{lang="EN-US"}**]{#struct_0_36812_x2234_x1296816976}[）：表示一周七天。]{lang="EN-US" style="font-family:宋体"}

[**[from]{lang="EN-US"}**[ *time1* *date1*]{lang="EN-US"}]{#struct_0_36812_x2234_x431919044}[：指定绝对时间段的起始时间。]{style="font-family:宋体"}*[time1]{lang="EN-US"}*[的格式为]{style="font-family:宋体"}[hh:mm]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[00:00]{lang="EN-US"}[～]{style="font-family:宋体"}[23:59]{lang="EN-US"}[。]{style="font-family:宋体"}*[date1]{lang="EN-US"}*[的格式为]{style="font-family:宋体"}[MM/DD/YYYY]{lang="EN-US"}[或]{style="font-family:宋体"}[YYYY/MM/DD]{lang="EN-US"}[。]{style="font-family:宋体"}[MM]{lang="EN-US"}[表示月，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[12]{lang="EN-US"}[；]{style="font-family:宋体"}[DD]{lang="EN-US"}[表示日，取值范围取决于所输入的月份；]{style="font-family:宋体"}[YYYY]{lang="EN-US"}[表示年，取值范围为]{style="font-family:宋体"}[1970]{lang="EN-US"}[～]{style="font-family:宋体"}[2100]{lang="EN-US"}[。若未指定本参数，绝对时间段的起始时间将为系统可表示的最早时间，即]{style="font-family:宋体"}[1970]{lang="EN-US"}[年]{style="font-family:宋体"}[1]{lang="EN-US"}[月]{style="font-family:宋体"}[1]{lang="EN-US"}[日]{style="font-family:
宋体"}[0]{lang="EN-US"}[点]{style="font-family:宋体"}[0]{lang="EN-US"}[分。]{style="font-family:宋体"}

[**[to]{lang="EN-US"}**[ *time2* *date2*]{lang="EN-US"}]{#struct_0_36812_x2234_x1399712975}[：指定绝对时间段的结束时间。]{style="font-family:宋体"}*[time2]{lang="EN-US"}*[的格式为]{style="font-family:宋体"}[hh:mm]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[00:00]{lang="EN-US"}[～]{style="font-family:宋体"}[24:00]{lang="EN-US"}[。]{style="font-family:宋体"}*[date2]{lang="EN-US"}*[的格式为]{style="font-family:宋体"}[MM/DD/YYYY]{lang="EN-US"}[或]{style="font-family:宋体"}[YYYY/MM/DD]{lang="EN-US"}[。]{style="font-family:宋体"}[MM]{lang="EN-US"}[表示月，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[12]{lang="EN-US"}[；]{style="font-family:宋体"}[DD]{lang="EN-US"}[表示日，取值范围取决于所输入的月份；]{style="font-family:宋体"}[YYYY]{lang="EN-US"}[表示年，取值范围为]{style="font-family:宋体"}[1970]{lang="EN-US"}[～]{style="font-family:宋体"}[2100]{lang="EN-US"}[。结束时间必须大于起始时间。若未指定本参数，绝对时间段的结束时间将为系统可表示的最晚时间，即]{style="font-family:宋体"}[2100]{lang="EN-US"}[年]{style="font-family:宋体"}[12]{lang="EN-US"}[月]{style="font-family:宋体"}[31]{lang="EN-US"}[日]{style="font-family:宋体"}[24]{lang="EN-US"}[点]{style="font-family:宋体"}[0]{lang="EN-US"}[分。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_36812_x2234_30576144}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_36812_x2234_x1711455576}**[time-range]{lang="EN-US"}**[命令时，如果指定名称的时间段不存在，则创建一个新的时间段（最多]{style="font-family:宋体"}[1024]{lang="EN-US"}[个）；如果指定名称的时间段已存在，则对旧时间段进行修改，即在其原有内容的基础上叠加新的内容。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_36812_x2234_1515541977}*[start-time]{lang="EN-US"}*[ **to** *end-time* *days*]{lang="EN-US"}[这组参数所创建的时间段为周期时间段，它将以一周为周期循环生效；使用]{style="font-family:
宋体"}**[from]{lang="EN-US"}**[ *time1* *date1*]{lang="EN-US"}[和]{style="font-family:宋体"}**[to]{lang="EN-US"}**[ *time2* *date2*]{lang="EN-US"}[这组参数所创建的时间段为绝对时间段，它将在指定时间范围内生效；而同时使用了上述两组参数所创建的时间段，将取周期时间段和绝对时间段的交集作为生效的时间范围，譬如：创建一个时间段，既定义其在每周一的]{style="font-family:宋体"}[8]{lang="EN-US"}[点到]{style="font-family:宋体"}[12]{lang="EN-US"}[点生效，又定义其在]{style="font-family:宋体"}[2011]{lang="EN-US"}[年全年生效，那么其最终将在]{style="font-family:宋体"}[2011]{lang="EN-US"}[年全年内每周一的]{style="font-family:宋体"}[8]{lang="EN-US"}[点到]{style="font-family:宋体"}[12]{lang="EN-US"}[点生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个时间段内可包含一或多个周期时间段（最多]{style="font-family:宋体"}]{#struct_0_36812_x2234_x710242333}[32]{lang="EN-US"}[个）和绝对时间段（最多]{style="font-family:宋体"}[12]{lang="EN-US"}[个），当包含有多个周期时间段和绝对时间段时，系统将先分别取各周期时间段的并集和各绝对时间段的并集，再取这两个并集的交集作为该时间段最终生效的时间范围。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_36812_x2234_905570499}

[[\# ]{lang="EN-US"}]{#struct_0_36812_x2234_x388337579}[创建名为]{style="font-family:宋体"}[t1]{lang="EN-US"}[的时间段，其时间范围为每周工作日的]{style="font-family:宋体"}[8]{lang="EN-US"}[点到]{style="font-family:宋体"}[18]{lang="EN-US"}[点。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_36812_x2234_x76832159}

[\[Sysname\] time-range t1 08:00 to 18:00 working-day]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_36812_x2234_x431984580}[创建名为]{style="font-family:宋体"}[t2]{lang="EN-US"}[的时间段，其时间范围为]{style="font-family:宋体"}[2011]{lang="EN-US"}[年全年。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_36812_x2234_x182841196}

[\[Sysname\] time-range t2 from 00:00 1/1/2011 to 24:00 12/31/2011]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_36812_x2234_x1464681968}[创建名为]{style="font-family:宋体"}[t3]{lang="EN-US"}[的时间段，其时间范围为]{style="font-family:宋体"}[2011]{lang="EN-US"}[年全年内每周休息日的]{style="font-family:宋体"}[8]{lang="EN-US"}[点到]{style="font-family:宋体"}[12]{lang="EN-US"}[点。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_36812_x2234_703647601}

[\[Sysname\] time-range t3 08:00 to 12:00 off-day from 00:00 1/1/2011 to 24:00 12/31/2011]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_36812_x2234_102764922}[创建名为]{style="font-family:宋体"}[t4]{lang="EN-US"}[的时间段，其时间范围为]{style="font-family:宋体"}[2011]{lang="EN-US"}[年]{style="font-family:宋体"}[1]{lang="EN-US"}[月和]{style="font-family:
宋体"}[6]{lang="EN-US"}[月内每周一的]{style="font-family:宋体"}[10]{lang="EN-US"}[点到]{style="font-family:宋体"}[12]{lang="EN-US"}[点以及每周三的]{style="font-family:宋体"}[14]{lang="EN-US"}[到]{style="font-family:宋体"}[16]{lang="EN-US"}[点。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_36812_x2234_x844411633}

[\[Sysname\] time-range t4 10:00 to 12:00 1 from 00:00 1/1/2011 to 24:00 1/31/2011]{lang="EN-US"}

[\[Sysname\] time-range t4 14:00 to 16:00 3 from 00:00 6/1/2011 to 24:00 6/30/2011]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_36812_x2234_x1256290838}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **time-range**]{lang="EN-US"}]{#struct_0_36812_x2234_x1562598855}
:::
