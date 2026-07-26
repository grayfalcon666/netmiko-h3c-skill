::: {#1184612688 .myid}
[]{#_Toc404794421}[]{#struct_0_x2079_20553_2136389931}

**语音用户线 \-- 模拟语音用户线 \-- area**

------------------------------------------------------------------------

[**[area]{lang="EN-US"}**]{#struct_0_x2079_20553_x510838731}[命令用来配置检测忙音的类型。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **area**]{lang="EN-US"}]{#struct_0_x2079_20553_1809020923}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1321870316}

[**[area]{lang="EN-US"}**[ { **custom** \| **europe** \| **north-america** }]{lang="EN-US"}]{#struct_0_x2079_20553_1940730583}

[**[undo]{lang="EN-US"}**[ **area**]{lang="EN-US"}]{#struct_0_x2079_20553_755712877}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1842302908}

[[使用符合欧洲标准的忙音参数。]{style="font-family:宋体"}]{#struct_0_x2079_20553_1134361509}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1171628195}

[[语音视图]{style="font-family:宋体"}]{#struct_0_x2079_20553_2089979892}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x508872350}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1160841388}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1220098201}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1201472459}

[**[custom]{lang="EN-US"}**]{#struct_0_x2079_20553_932308218}[：用户自定义的忙音类型。]{style="font-family:宋体"}

[**[europe]{lang="EN-US"}**]{#struct_0_x2079_20553_x1324795226}[：符合欧洲标准的忙音。]{style="font-family:宋体"}

[**[north-america]{lang="EN-US"}**]{#struct_0_x2079_20553_1134295973}[：符合北美标准的忙音。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_828165719}

[[此命令对设备上的所有模拟]{style="font-family:宋体"}[FXO]{lang="EN-US"}]{#struct_0_x2079_20553_x101519725}[语音用户线都生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_386730676}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_696256133}[配置符合北美标准的忙音。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_314747418}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] area north-america]{lang="EN-US"}
:::

::: {#514421303 .myid}
[]{#_Toc404794422}[]{#struct_0_x2079_20553_x111449756}

**语音用户线 \-- 模拟语音用户线 \-- busytone-detect auto**

------------------------------------------------------------------------

[**[busytone-detect auto]{lang="EN-US"}**]{#struct_0_x2079_20553_525009629}[命令用来配置自动忙音检测。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1134230437}

[**[busytone-detect]{lang="EN-US"}**[ **auto** *index line-number*]{lang="EN-US"}]{#struct_0_x2079_20553_1564677466}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1341621184}

[[语音视图]{style="font-family:宋体"}]{#struct_0_x2079_20553_x292964297}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1845950719}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x488422736}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1145873483}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x872187907}

[*[index]{lang="EN-US"}*]{#struct_0_x2079_20553_x2034022141}[：忙音参数的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[。设备最多可以记录]{style="font-family:宋体"}[4]{lang="EN-US"}[种忙音。]{style="font-family:宋体"}

[*[line-number]{lang="EN-US"}*]{#struct_0_x2079_20553_1134164901}[：检测忙音的]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x718585200}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[busytone-detect auto]{lang="EN-US"}**]{#struct_0_x2079_20553_753610830}[命令只对]{lang="EN-US" style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线有效。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}**[busytone-detect]{lang="EN-US"}**[ **auto**]{lang="EN-US"}]{#struct_0_x2079_20553_x436625331}[命令成功检测忙音后，设备会自动计算出忙音参数，然后会自动使用]{lang="EN-US" style="font-family:宋体"}**[busytone-detect]{lang="EN-US"}**[ **custom**]{lang="EN-US"}[命令记录检测到的忙音参数，]{lang="EN-US" style="font-family:宋体"}[并自动执行]{style="font-family:
宋体"}**[area]{lang="EN-US"}**[ **custom**]{lang="EN-US"}[命令使这些忙音参数生效。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1343841333}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x522980501}[在]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线]{style="font-family:宋体"}[2/2/1]{lang="EN-US"}[上开启自动忙音检测，并将检测到的忙音参数标识到编号]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_1134099365}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] busytone-detect auto 0 2/2/1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_362169694}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[area custom]{lang="EN-US"}**]{#struct_0_x2079_20553_x1226096019}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[busytone-detect custom]{lang="EN-US"}**]{#struct_0_x2079_20553_x1648516559}
:::

::: {#708443932 .myid}
[]{#_Toc404794423}[]{#struct_0_x2079_20553_x1564489294}

**语音用户线 \-- 模拟语音用户线 \-- busytone-detect custom**

------------------------------------------------------------------------

[**[busytone-detect custom]{lang="EN-US"}**]{#struct_0_x2079_20553_x473889381}[命令用来配置自定义忙音参数。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **busytone-detect custom**]{lang="EN-US"}]{#struct_0_x2079_20553_x856954472}[命令用来删除忙音参数。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x70442883}

[**[busytone-detect]{lang="EN-US"}**[ **custom** *area-number index argu f1 f2 p1 p2 p3 p4 p5 p6 p7* ]{lang="EN-US"}]{#struct_0_x2079_20553_x1828481476}

[**[undo busytone-detect]{lang="EN-US"}**[ **custom** *index*]{lang="EN-US"}]{#struct_0_x2079_20553_1134033829}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1998883256}

[[不存在忙音参数，设备用于检测忙音的标准]{style="font-family:宋体"}]{#struct_0_x2079_20553_743242199}[和]{style="font-family:
宋体"}**[area]{lang="EN-US"}**[命令的设置有关。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1468561907}

[[语音视图]{style="font-family:宋体"}]{#struct_0_x2079_20553_x396063576}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1315322003}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_89674016}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1383184751}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1234875964}

[*[area-number]{lang="EN-US"}*]{#struct_0_x2079_20553_1133968293}[：区域号，目前为保留参数，规定设置为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[index]{lang="EN-US"}*]{#struct_0_x2079_20553_1287960789}[：忙音参数的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[。设备最多可以记录]{style="font-family:宋体"}[4]{lang="EN-US"}[种忙音。]{style="font-family:宋体"}

[*[argu]{lang="EN-US"}*]{#struct_0_x2079_20553_x36145581}[：目前为保留参数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[f1]{lang="EN-US"}*]{#struct_0_x2079_20553_x1727436726}[：频率参数]{style="font-family:宋体"}[1]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[50]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[Hz]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[f2]{lang="EN-US"}*]{#struct_0_x2079_20553_x428599049}[：频率参数]{style="font-family:宋体"}[2]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[50]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[Hz]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[p1]{lang="EN-US"}*]{#struct_0_x2079_20553_x940434768}[：信号振幅参数]{style="font-family:宋体"}[1]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[50]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[p2]{lang="EN-US"}*]{#struct_0_x2079_20553_x1951514904}[：信号振幅参数]{style="font-family:宋体"}[2]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[50]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[p3]{lang="EN-US"}*]{#struct_0_x2079_20553_104896704}[：单音持续时间长度，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[*[p4]{lang="EN-US"}*]{#struct_0_x2079_20553_x484312148}[：单音持续时间长度的误差范围，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[500]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[*[p5]{lang="EN-US"}*]{#struct_0_x2079_20553_1133902757}[：静音持续时间长度，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[*[p6]{lang="EN-US"}*]{#struct_0_x2079_20553_524877103}[：静音持续时间长度的误差范围，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[500]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[*[p7]{lang="EN-US"}*]{#struct_0_x2079_20553_x1422809065}[：单音和静音持续时间长度的差值区间，即]{style="font-family:宋体"}*[p3]{lang="EN-US"}*[和]{style="font-family:宋体"}*[p5]{lang="EN-US"}*[差的绝对值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[500]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1070982866}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[busytone-detect custom]{lang="EN-US"}**]{#struct_0_x2079_20553_x1182427528}[命令只对]{lang="EN-US" style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线有效。系统可以记录]{lang="EN-US" style="font-family:宋体"}[4]{lang="EN-US"}[种忙音特性，由]{lang="EN-US" style="font-family:宋体"}*[index]{lang="EN-US"}*[参数来标记。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{lang="EN-US" style="font-family:宋体"}**[busytone-detect]{lang="EN-US"}**[ **custom**]{lang="EN-US"}]{#struct_0_x2079_20553_1588073}[命令设置的自定义忙音参数，在配置]{lang="EN-US" style="font-family:宋体"}**[area]{lang="EN-US"}**[ **custom**]{lang="EN-US"}[命令后才能生效。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1500443418}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x231166261}[自定义忙音参数，并将检测到的忙音参数标识到编号]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_332593364}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] busytone-detect custom 2 1 99 450 450 8000 8000 800 300 500 500 500]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1134885797}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[area]{lang="EN-US"}**]{#struct_0_x2079_20553_x1548628717}
:::

::: {#1829205606 .myid}
[]{#_Toc404794424}[]{#struct_0_x2079_20553_2011620706}[]{#_Toc296158434}[]{#_Toc296159749}[]{#_Toc296158436}[]{#_Toc296159751}[]{#_Toc296158437}[]{#_Toc296159752}[]{#_Toc296158438}[]{#_Toc296159753}[]{#_Toc296158439}[]{#_Toc296159754}[]{#_Toc296158440}[]{#_Toc296159755}[]{#_Toc296158441}[]{#_Toc296159756}[]{#_Toc296158442}[]{#_Toc296159757}[]{#_Toc296158443}[]{#_Toc296159758}[]{#_Toc296158444}[]{#_Toc296159759}[]{#_Toc296158445}[]{#_Toc296159760}[]{#_Toc296158446}[]{#_Toc296159761}[]{#_Toc296158447}[]{#_Toc296159762}[]{#_Toc296158448}[]{#_Toc296159763}[]{#_Toc296158449}[]{#_Toc296159764}[]{#_Toc296158450}[]{#_Toc296159765}[]{#_Toc296158451}[]{#_Toc296159766}[]{#_Toc296158452}[]{#_Toc296159767}[]{#_Toc296158453}[]{#_Toc296159768}[]{#_Toc296158454}[]{#_Toc296159769}[]{#_Toc296158455}[]{#_Toc296159770}[]{#_Toc296158456}[]{#_Toc296159771}[]{#_Toc296158457}[]{#_Toc296159772}[]{#_Toc296158458}[]{#_Toc296159773}[]{#_Toc296158459}[]{#_Toc296159774}[]{#_Toc296158460}[]{#_Toc296159775}[]{#_Toc296158461}[]{#_Toc296159776}[]{#_Toc296158462}[]{#_Toc296159777}[]{#_Toc296158463}[]{#_Toc296159778}[]{#_Toc296158464}[]{#_Toc296159779}[]{#_Toc296158465}[]{#_Toc296159780}[]{#_Toc296158469}[]{#_Toc296159784}[]{#_Toc296158476}[]{#_Toc296159791}[]{#_Toc296158477}[]{#_Toc296159792}[]{#_Toc296158478}[]{#_Toc296159793}[]{#_Toc296158487}[]{#_Toc296159802}[]{#_Toc296158488}[]{#_Toc296159803}[]{#_Toc296158534}[]{#_Toc296159849}[]{#_Toc296158536}[]{#_Toc296159851}[]{#_Toc296158537}[]{#_Toc296159852}[]{#_Toc296158538}[]{#_Toc296159853}[]{#_Toc296158539}[]{#_Toc296159854}[]{#_Toc296158540}[]{#_Toc296159855}[]{#_Toc296158541}[]{#_Toc296159856}[]{#_Toc296158542}[]{#_Toc296159857}[]{#_Toc296158543}[]{#_Toc296159858}[]{#_Toc296158544}[]{#_Toc296159859}[]{#_Toc296158545}[]{#_Toc296159860}[]{#_Toc296158546}[]{#_Toc296159861}[]{#_Toc296158547}[]{#_Toc296159862}[]{#_Toc296158548}[]{#_Toc296159863}[]{#_Toc296158549}[]{#_Toc296159864}[]{#_Toc296158550}[]{#_Toc296159865}[]{#_Toc296158551}[]{#_Toc296159866}[]{#_Toc296158552}[]{#_Toc296159867}[]{#_Toc296158553}[]{#_Toc296159868}[]{#_Toc296158554}[]{#_Toc296159869}[]{#_Toc296158556}[]{#_Toc296159871}[]{#_Toc296158557}[]{#_Toc296159872}[]{#_Toc296158562}[]{#_Toc296159877}[]{#_Toc296158584}[]{#_Toc296159899}[]{#_Toc296158586}[]{#_Toc296159901}[]{#_Toc296158587}[]{#_Toc296159902}[]{#_Toc296158588}[]{#_Toc296159903}[]{#_Toc296158589}[]{#_Toc296159904}[]{#_Toc296158590}[]{#_Toc296159905}[]{#_Toc296158591}[]{#_Toc296159906}[]{#_Toc296158592}[]{#_Toc296159907}[]{#_Toc296158593}[]{#_Toc296159908}[]{#_Toc296158594}[]{#_Toc296159909}[]{#_Toc296158595}[]{#_Toc296159910}[]{#_Toc296158596}[]{#_Toc296159911}[]{#_Toc296158597}[]{#_Toc296159912}[]{#_Toc296158598}[]{#_Toc296159913}[]{#_Toc296158599}[]{#_Toc296159914}[]{#_Toc296158600}[]{#_Toc296159915}[]{#_Toc296158601}[]{#_Toc296159916}[]{#_Toc296158602}[]{#_Toc296159917}[]{#_Toc296158603}[]{#_Toc296159918}[]{#_Toc296158604}[]{#_Toc296159919}[]{#_Toc296158605}[]{#_Toc296159920}[]{#_Toc296158606}[]{#_Toc296159921}[]{#_Toc296158607}[]{#_Toc296159922}[]{#_Toc296158608}[]{#_Toc296159923}[]{#_Toc296158609}[]{#_Toc296159924}[]{#_Toc296158610}[]{#_Toc296159925}[]{#_Toc296158611}[]{#_Toc296159926}[]{#_Toc296158612}[]{#_Toc296159927}[]{#_Toc296158613}[]{#_Toc296159928}[]{#_Toc296158614}[]{#_Toc296159929}[]{#_Toc296158615}[]{#_Toc296159930}[]{#_Toc296158625}[]{#_Toc296159940}[]{#_Toc296158626}[]{#_Toc296159941}[]{#_Toc296158648}[]{#_Toc296159963}

**语音用户线 \-- 模拟语音用户线 \-- busytone-detect period**

------------------------------------------------------------------------

[**[busytone-detect period]{lang="EN-US"}**]{#struct_0_x2079_20553_x1182402330}[命令用来配置检测忙音的周期数。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **busytone-detect period**]{lang="EN-US"}]{#struct_0_x2079_20553_x1038571895}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1021500201}

[**[busytone-detect period ]{lang="EN-US"}***[value]{lang="EN-US"}*]{#struct_0_x2079_20553_1416898931}

[**[undo busytone-detect period]{lang="EN-US"}**]{#struct_0_x2079_20553_x1872320266}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_678139910}

[[检测忙音的周期数为]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_x2079_20553_1134820261}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_424023065}

[[FXO]{lang="EN-US"}]{#struct_0_x2079_20553_1898458906}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_129545041}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_949639208}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1645441622}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_357105998}

[*[value]{lang="EN-US"}*]{#struct_0_x2079_20553_1840452377}[：忙音检测的周期数]{style="font-family:宋体"}[，周期数越多，检测时间越长。]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[12]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_177035801}

[[通过调整忙音检测的周期数，可以增加忙音检测的时间，提高忙音检测的准确性，这对由于忙音数据不准确导致误挂机能够一定程度上进行改善，但是可能会使挂不断的情形加剧。因此使用该命令调整忙音检测的周期数，一定要在进行多次测试，确认使用的参数能够保证正常挂机后方可采用。]{style="font-family:宋体"}]{#struct_0_x2079_20553_1134361506}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1172480163}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x2004142975}[设置检测忙音的周期数为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x1015931817}

[\[Sysname\] subscriber-line 2/2/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/2/1\] busytone-detect period 3]{lang="EN-US"}
:::

::: {#1697859936 .myid}
[]{#_Toc404794425}[]{#struct_0_x2079_20553_93735078}

**语音用户线 \-- 模拟语音用户线 \-- busytone-hookon**

------------------------------------------------------------------------

[**[busytone-hookon delay-timer]{lang="EN-US"}**]{#struct_0_x2079_20553_x219648714}[命令用来配置]{style="font-family:
宋体"}[FXO]{lang="EN-US"}[语音用户线检测到忙音到挂机前的延时时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **busytone-hookon delay-timer**]{lang="EN-US"}]{#struct_0_x2079_20553_427521974}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1105594071}

[**[busytone-hookon delay-timer ]{lang="EN-US"}***[value]{lang="EN-US"}*]{#struct_0_x2079_20553_1134295970}

[**[undo busytone-hookon delay-timer]{lang="EN-US"}**]{#struct_0_x2079_20553_828100183}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x448526955}

[[延时时间为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x2079_20553_380786066}[秒，即]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线检测到忙音后立即挂机。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_380508666}

[[FXO]{lang="EN-US"}]{#struct_0_x2079_20553_x695139176}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1217000405}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1764858271}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1478387673}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1134230434}

[*[value]{lang="EN-US"}*]{#struct_0_x2079_20553_1564874074}[：]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线检测到忙音到挂机前的延时时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_980362550}

[[通常]{style="font-family:宋体"}[FXO]{lang="EN-US"}]{#struct_0_x2079_20553_186157143}[语音用户线检测到线路忙音后，会自动挂机，完成线路拆除。当]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线作为语音网关接入端与]{style="font-family:宋体"}[IPPhone]{lang="EN-US"}[配合使用时，由于]{style="font-family:宋体"}[IPPhone]{lang="EN-US"}[收到拆线消息后不会播放提示音，]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线检测到忙音就立即挂机，由于此忙音持续时间较短，使用]{style="font-family:宋体"}[IPPhone]{lang="EN-US"}[的用户容易忽略忙音，误认为是线路异常导致的挂机。通过配置忙音检测挂机延迟时间，]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线检测到忙音后，会延迟一段时间再挂机拆线，此时]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线接收到的忙音会继续传到]{style="font-family:宋体"}[IPPhone]{lang="EN-US"}[，使得]{style="font-family:宋体"}[IPPhone]{lang="EN-US"}[用户可以用较长时间识别到忙音。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1843578819}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_1134164898}[配置]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线检测到忙音到挂机前的延时时间为]{style="font-family:宋体"}[3]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_1237140105}

[\[Sysname\] subscriber-line 2/2/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/2/1\] busytone-hookon delay-timer 3]{lang="EN-US"}
:::

::: {#-577270684 .myid}
[]{#_Toc404794426}[]{#struct_0_x2079_20553_x426830596}

**语音用户线 \-- 模拟语音用户线 \-- calling-name**

------------------------------------------------------------------------

[**[calling-name]{lang="EN-US"}**]{#struct_0_x2079_20553_x1508310557}[命令用来配置主叫用户名。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **calling-name**]{lang="EN-US"}]{#struct_0_x2079_20553_1995188965}[命令用来删除主叫用户名。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_711373752}

[**[calling-name]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_x2079_20553_x1540530317}

[**[undo calling-name]{lang="EN-US"}**]{#struct_0_x2079_20553_76063305}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1134099362}

[[没有配置主叫用户名。]{style="font-family:宋体"}]{#struct_0_x2079_20553_362104158}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x840916992}

[[FXS]{lang="EN-US"}]{#struct_0_x2079_20553_1007703578}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x495866123}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1119612959}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_149091998}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_750468635}

[*[text]{lang="EN-US"}*]{#struct_0_x2079_20553_x1701449104}[：主叫用户名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[50]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1134033826}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[主叫信息中的主叫用户名只能通过复合格式发送。]{style="font-family:宋体"}]{#struct_0_x2079_20553_1999604152}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[此命令在主叫侧设备上生效。]{style="font-family:宋体"}]{#struct_0_x2079_20553_1475685074}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_518492815}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_23183500}[配置主叫用户名为]{style="font-family:宋体"}[tony]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_1746990340}

[\[Sysname\] subscriber-line 2/1/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/1/1\] calling-name tony]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1787183794}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cid display]{lang="EN-US"}**]{#struct_0_x2079_20553_1055589038}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cid send]{lang="EN-US"}**]{#struct_0_x2079_20553_x875998038}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cid type]{lang="EN-US"}**]{#struct_0_x2079_20553_1133968290}
:::

::: {#-798614504 .myid}
[]{#_Toc404794427}[]{#struct_0_x2079_20553_1287764181}

**语音用户线 \-- 模拟语音用户线 \-- cable**

------------------------------------------------------------------------

[**[cable]{lang="EN-US"}**]{#struct_0_x2079_20553_x859027083}[命令用来配置线缆类型。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **cable**]{lang="EN-US"}]{#struct_0_x2079_20553_948158816}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x208015335}

[**[cable]{lang="EN-US"}**[ { **2-wire** \| **4-wire** }]{lang="EN-US"}]{#struct_0_x2079_20553_x867616890}

[**[undo]{lang="PT-BR"}**]{#struct_0_x2079_20553_1419500847}[ **cable**]{lang="PT-BR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x107608962}

[[线缆类型为四线。]{style="font-family:宋体"}]{#struct_0_x2079_20553_378902142}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1133902754}

[[E&M]{lang="EN-US"}]{#struct_0_x2079_20553_524942639}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x215976021}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1203127242}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_436053526}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1377401351}

[**[2-wire]{lang="EN-US"}**]{#struct_0_x2079_20553_x58804726}[：线缆类型为二线。二线方式提供全双工语音传输，语音信号在两根线中双向传输。]{style="font-family:宋体"}

[**[4-wire]{lang="EN-US"}**]{#struct_0_x2079_20553_2134811092}[：线缆类型为四线。四线方式相当于单工方式，每两根线负责一个方向的语音信号的传输。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1134885794}

[[在呼叫两端设备上需要配置相同的]{style="font-family:宋体"}[E&M]{lang="EN-US"}]{#struct_0_x2079_20553_x1548563181}[线缆类型，如果配置的线缆不一致，用户将只能获取单向的语音服务。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1859581482}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_1399613737}[配置使用的线缆类型为二线。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x1473840489}

[\[Sysname\] subscriber-line 2/3/1]{lang="EN-US"}

[\[Sysname-sub scriber-line2/3/1\] cable 2-wire]{lang="EN-US"}
:::

::: {#2042640370 .myid}
[]{#_Toc404794428}[]{#struct_0_x2079_20553_1075194308}

**语音用户线 \-- 模拟语音用户线 \-- cid display**

------------------------------------------------------------------------

[**[cid]{lang="EN-US"}**[ **display**]{lang="EN-US"}]{#struct_0_x2079_20553_1581582164}[命令用来开启主叫信息（包括主叫号码和主叫用户名）显示功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **cid** **display**]{lang="EN-US"}]{#struct_0_x2079_20553_x1227780714}[命令用来取消主叫信息显示功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x31647017}

[**[cid]{lang="EN-US"}**[ **display**]{lang="EN-US"}]{#struct_0_x2079_20553_1134820258}

[**[undo]{lang="EN-US"}**[ **cid** **display**]{lang="EN-US"}]{#struct_0_x2079_20553_423433238}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x303503049}

[[主叫信息显示功能处于开启状态。]{style="font-family:宋体"}]{#struct_0_x2079_20553_1719434412}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x438642931}

[[FXS]{lang="EN-US"}]{#struct_0_x2079_20553_x1958425592}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1864797136}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x545163370}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x663053268}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1134361507}

[[此命令在被叫侧设备上生效。]{style="font-family:宋体"}]{#struct_0_x2079_20553_1172545699}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x824143298}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x589472097}[关闭主叫信息显示功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x1752147012}

[\[Sysname\] subscriber-line 2/1/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/1/1\] undo cid display]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_746719883}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[calling-name]{lang="EN-US"}**]{#struct_0_x2079_20553_1064277330}
:::

::: {#-1235416693 .myid}
[]{#_Toc404794429}[]{#struct_0_x2079_20553_1134295971}[]{#_Toc316549745}[]{#_Toc295912507}[]{#_Toc263260013}[]{#_Toc135295454}[]{#_Toc130097097}[]{#_Toc129160819}[]{#_Toc95385402}[]{#_Toc54499264}

**语音用户线 \-- 模拟语音用户线 \-- cid receive**

------------------------------------------------------------------------

[**[cid]{lang="EN-US"}**[ **receive**]{lang="EN-US"}]{#struct_0_x2079_20553_828034647}[命令用来开启接收主叫信息功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **cid** **receive**]{lang="EN-US"}]{#struct_0_x2079_20553_x2042594669}[命令用来关闭接收主叫信息功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x709895103}

[**[cid]{lang="EN-US"}**[ **receive**]{lang="EN-US"}]{#struct_0_x2079_20553_x566413076}

[**[undo]{lang="EN-US"}**[ **cid** **receive**]{lang="EN-US"}]{#struct_0_x2079_20553_x1494122725}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_813917447}

[[主叫信息接收功能处于开启状态。]{style="font-family:宋体"}]{#struct_0_x2079_20553_x648061860}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x160660222}

[[FXO]{lang="EN-US"}]{#struct_0_x2079_20553_1134230435}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1564808538}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1395502574}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1543270095}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x546749424}

[[为了保证主叫信息识别及显示功能能够正常运行，建议将]{style="font-family:宋体"}**[cid]{lang="EN-US"}**[ **receive**]{lang="EN-US"}]{#struct_0_x2079_20553_x1238291743}[命令保持在开启状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x869407026}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x1084075645}[开启接收主叫信息功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_1134164899}

[\[Sysname\] subscriber-line 2/2/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/2/1\] cid receive]{lang="EN-US"}
:::

::: {#-1162371013 .myid}
[]{#_Toc404794430}[]{#struct_0_x2079_20553_1237205641}[]{#_Toc316549746}[]{#_Toc295912508}[]{#_Toc263260014}

**语音用户线 \-- 模拟语音用户线 \-- cid ring**

------------------------------------------------------------------------

[**[cid]{lang="EN-US"}**[ **ring**]{lang="EN-US"}]{#struct_0_x2079_20553_14208602}[命令用来配置检测]{style="font-family:宋体"}[CID]{lang="EN-US"}[的时间和]{style="font-family:宋体"}[CID]{lang="EN-US"}[检测完毕后的振铃次数。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **cid** **ring**]{lang="EN-US"}]{#struct_0_x2079_20553_x1621089253}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_155593863}

[**[cid]{lang="EN-US"}**[ **ring** { **0** \| **1** \| **2** } \[ *times* \]]{lang="EN-US"}]{#struct_0_x2079_20553_x1774532414}

[**[undo]{lang="EN-US"}**[ **cid** **ring**]{lang="EN-US"}]{#struct_0_x2079_20553_1727243326}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1284018672}

[[在第一声和第二声振铃间进行检测]{style="font-family:宋体"}[CID]{lang="EN-US"}]{#struct_0_x2079_20553_x1869426017}[，]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线完成]{style="font-family:宋体"}[CID]{lang="EN-US"}[检测后会立即摘机应答，即缺省情况下的命令为]{style="font-family:宋体"}**[cid]{lang="EN-US"}**[ **ring** **1** **0**]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1134099363}

[[FXO]{lang="EN-US"}]{#struct_0_x2079_20553_362038622}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1473397192}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x920486870}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1078007847}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x693076974}

[**[0]{lang="EN-US"}**]{#struct_0_x2079_20553_1241779829}[：表示振铃前进行]{style="font-family:宋体"}[CID]{lang="EN-US"}[检测。]{style="font-family:宋体"}

[**[1]{lang="EN-US"}**]{#struct_0_x2079_20553_1080122602}[：表示第一声和第二声振铃间进行]{style="font-family:宋体"}[CID]{lang="EN-US"}[检测。]{style="font-family:宋体"}

[**[2]{lang="EN-US"}**]{#struct_0_x2079_20553_x305230307}[：表示第二声和第三声振铃间进行]{style="font-family:宋体"}[CID]{lang="EN-US"}[检测。]{style="font-family:宋体"}

[*[times]{lang="EN-US"}*]{#struct_0_x2079_20553_1134033827}[：]{style="font-family:宋体"}[CID]{lang="EN-US"}[检测完毕后到]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线摘机前的振铃次数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[5]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。取值越大，]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线的摘机应答时间越长。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1999538616}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_756790067}[配置振铃前进行]{style="font-family:宋体"}[CID]{lang="EN-US"}[检测，]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线完成]{style="font-family:宋体"}[CID]{lang="EN-US"}[检测后会立即摘机应答。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x1450493137}

[\[Sysname\] subscriber-line 2/2/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/2/1\] cid ring 0]{lang="EN-US"}
:::

::: {#1175494716 .myid}
[]{#_Toc404794431}[]{#struct_0_x2079_20553_x63864957}[]{#_Toc316549747}[]{#_Toc295912509}[]{#_Toc263260015}[]{#_Toc135295455}[]{#_Toc130097098}[]{#_Toc129160820}[]{#_Toc95385403}

**语音用户线 \-- 模拟语音用户线 \-- cid send**

------------------------------------------------------------------------

[**[cid]{lang="EN-US"}**[ **send**]{lang="EN-US"}]{#struct_0_x2079_20553_656216852}[命令用来开启向对端发送主叫信息。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **cid** **send**]{lang="EN-US"}]{#struct_0_x2079_20553_x392326901}[命令用来禁止向对端发送主叫信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_900861690}

[**[cid]{lang="EN-US"}**[ **send**]{lang="EN-US"}]{#struct_0_x2079_20553_1590831750}

[**[undo]{lang="EN-US"}**[ **cid** **send**]{lang="EN-US"}]{#struct_0_x2079_20553_1133968291}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1287829717}

[[向对端发送主叫信息。]{style="font-family:宋体"}]{#struct_0_x2079_20553_x1950202324}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1194146014}

[[FXS/FXO]{lang="EN-US"}]{#struct_0_x2079_20553_827103622}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_131926576}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x531668166}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1204648018}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_879964725}

[[为了保证主叫信息识别及显示功能能够正常运行，建议将]{style="font-family:宋体"}**[cid]{lang="EN-US"}**[ **send**]{lang="EN-US"}]{#struct_0_x2079_20553_1133902755}[命令保持在开启状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_525008175}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x1506566291}[开启向对端发送主叫信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x1683813997}

[\[Sysname\] subscriber-line 2/1/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/1/1\] cid send]{lang="EN-US"}
:::

::: {#-1229324101 .myid}
[]{#_Toc404794432}[]{#struct_0_x2079_20553_832865405}

**语音用户线 \-- 模拟语音用户线 \-- cid type**

------------------------------------------------------------------------

[**[cid type]{lang="EN-US"}**]{#struct_0_x2079_20553_x2101118272}[命令用来配置发送主叫信息时所采用的消息格式。]{style="font-family:宋体"}

[**[undo cid type]{lang="EN-US"}**]{#struct_0_x2079_20553_695250596}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_800243642}

[**[cid]{lang="EN-US"}**[ **type** { **complex** \| **simple** }]{lang="EN-US"}]{#struct_0_x2079_20553_1134885795}

[**[undo]{lang="EN-US"}**[ **cid** **type**]{lang="EN-US"}]{#struct_0_x2079_20553_x1548497645}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1636962774}

[[发送主叫信息时采用复合格式。]{style="font-family:宋体"}]{#struct_0_x2079_20553_x509245594}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1190185025}

[[FXS]{lang="EN-US"}]{#struct_0_x2079_20553_x1257994159}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x560059016}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_487649315}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_2005505320}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1134820259}

[**[complex]{lang="EN-US"}**]{#struct_0_x2079_20553_423498774}[：主叫信息采用复合格式。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_x2079_20553_x322133766}[：主叫信息采用简单格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_629694112}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当对端设备只能支持两种格式中的一种时，需要在主叫侧设备调整本端语音用户线发送主叫信息的格式，以保证双方设备采用一致的格式。]{style="font-family:宋体"}]{#struct_0_x2079_20553_x723663054}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[主叫信息中的主叫用户名只能通过复合格式发送。]{style="font-family:宋体"}]{#struct_0_x2079_20553_x836804753}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[此命令在被叫侧设备上生效。]{style="font-family:宋体"}]{#struct_0_x2079_20553_x1360129882}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1927827539}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x487080386}[配置使用简单格式发送主叫信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_1134361504}

[\[Sysname\] subscriber-line 2/1/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/1/1\] cid type simple]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1172349091}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[call-name]{lang="EN-US"}**]{#struct_0_x2079_20553_1170807728}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cid display]{lang="EN-US"}**]{#struct_0_x2079_20553_1652390664}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cid send]{lang="EN-US"}**]{#struct_0_x2079_20553_x366402251}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cid standard-type]{lang="EN-US"}**]{#struct_0_x2079_20553_603589245}
:::

::: {#962221642 .myid}
[]{#_Toc404794433}[]{#struct_0_x2079_20553_x590028335}

**语音用户线 \-- 模拟语音用户线 \-- cid standard-type**

------------------------------------------------------------------------

[**[cid standard-type]{lang="EN-US"}**]{#struct_0_x2079_20553_127238251}[命令用来配置发送主叫信息的标准模式。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[cid standard-type]{lang="EN-US"}**]{#struct_0_x2079_20553_1134295968}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_828624472}

[**[cid]{lang="EN-US"}**[ **standard-type** { **bellcore** \| **brazil** }]{lang="EN-US"}]{#struct_0_x2079_20553_x121085013}

[**[undo]{lang="EN-US"}**[ **cid** **standard-type**]{lang="EN-US"}]{#struct_0_x2079_20553_132358818}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x2131372003}

[[使用]{style="font-family:宋体"}**[bellcore]{lang="EN-US"}**]{#struct_0_x2079_20553_x796559467}[标准模式发送主叫信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1144261784}

[[FXS]{lang="EN-US"}]{#struct_0_x2079_20553_366524587}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1265397235}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1134230432}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1564480858}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1389384516}

[**[bellcore]{lang="EN-US"}**]{#struct_0_x2079_20553_x1247917566}[：使用通用地区标准（包括中国、北美等大多数地区），表示按]{style="font-family:宋体"}[FSK]{lang="EN-US"}[（]{style="font-family:宋体"}[Frequency Shift Keying]{lang="EN-US"}[，频移键控）方式发送主叫信息。]{style="font-family:宋体"}

[**[brazil]{lang="EN-US"}**]{#struct_0_x2079_20553_863016902}[：使用巴西标准，表示按]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[（]{style="font-family:宋体"}[Dual Tone Multi-Frequency]{lang="EN-US"}[，双音多频）方式发送主叫信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1980129025}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[此命令在被叫侧设备上生效，被叫设备会根据指定的标准模式封装主叫信息，并发送给被叫话机。]{style="font-family:宋体"}]{#struct_0_x2079_20553_376260372}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{lang="EN-US" style="font-family:宋体"}**[bellcore]{lang="EN-US"}**]{#struct_0_x2079_20553_x212752034}[标准模式时，]{lang="EN-US" style="font-family:宋体"}**[cid type]{lang="EN-US"}**[命令设置消息格式才能生效。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x290199155}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_1134164896}[配置使用巴西标准模式发送主叫信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_1238057609}

[\[Sysname\] subscriber-line 2/1/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/1/1\] cid standard-type brazil]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_981055306}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cid type]{lang="EN-US"}**]{#struct_0_x2079_20553_1653916883}
:::

::: {#1260174227 .myid}
[]{#_Toc404794434}[]{#struct_0_x2079_20553_92563535}

**语音用户线 \-- 模拟语音用户线 \-- cptone**

------------------------------------------------------------------------

[**[cptone]{lang="EN-US"}**]{#struct_0_x2079_20553_x198133650}[命令用来设置提示音的模式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **cptone**]{lang="EN-US"}]{#struct_0_x2079_20553_x536361010}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1931645515}

[**[cptone]{lang="EN-US"}**[ { **country-type** *locale \|* **custom** { **busy-tone** \| **congestion-tone** \| **dial-tone** \| **ringback-tone** \| **special-dial-tone** \| **waiting-tone** } *comb freq1 freq2 time1 time2 time3 time4* }]{lang="EN-US"}]{#struct_0_x2079_20553_1134099360}

[**[undo cptone]{lang="EN-US"}**]{#struct_0_x2079_20553_361973086}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x246547253}

[[提示音的国家模式为中国。]{style="font-family:宋体"}]{#struct_0_x2079_20553_x835270099}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x2008751640}

[[语音视图]{style="font-family:宋体"}]{#struct_0_x2079_20553_1690103228}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1388971330}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1091421496}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_599253909}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1134033824}

[**[country-type]{lang="EN-US"}**[ *locale*]{lang="EN-US"}]{#struct_0_x2079_20553_1999735224}[：将提示音设置为指定的国家或地区模式。目前支持以下提示音的国家模式。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[提示音对应的国家模式]{style="font-family:黑体"}]{#struct_0_x2079_20553_1474541087}

[]{#table_struct_0_234873019}[[提示音模式]{style="font-family:黑体"}]{#struct_0_x2079_20553_1736425425}
:::

[[国家名]{style="font-family:黑体"}]{#struct_0_x2079_20553_642698641}

[[AR]{lang="EN-US"}]{#struct_0_x2079_20553_x728486453}

[[Argentina ]{lang="EN-US"}]{#struct_0_x2079_20553_x1974331354}[阿根廷]{style="font-family:宋体"}

[[AU]{lang="EN-US"}]{#struct_0_x2079_20553_1133968288}

[[Australia ]{lang="EN-US"}]{#struct_0_x2079_20553_1287239892}[澳大利亚]{style="font-family:宋体"}

[[AT]{lang="EN-US"}]{#struct_0_x2079_20553_x1232124050}

[[Austria ]{lang="EN-US"}]{#struct_0_x2079_20553_x1582580579}[奥地利]{style="font-family:宋体"}

[[BE]{lang="EN-US"}]{#struct_0_x2079_20553_x830810274}

[[Belgium ]{lang="EN-US"}]{#struct_0_x2079_20553_595387156}[比利时]{style="font-family:宋体"}

[[BR]{lang="EN-US"}]{#struct_0_x2079_20553_1133902752}

[[Brazil ]{lang="EN-US"}]{#struct_0_x2079_20553_524549423}[巴西]{style="font-family:宋体"}

[[BG]{lang="EN-US"}]{#struct_0_x2079_20553_x1894817557}

[[Bulgaria ]{lang="EN-US"}]{#struct_0_x2079_20553_x1977370766}[保加利亚]{style="font-family:宋体"}

[[CA]{lang="EN-US"}]{#struct_0_x2079_20553_712156176}

[[Canada ]{lang="EN-US"}]{#struct_0_x2079_20553_1134885792}[加拿大]{style="font-family:宋体"}

[[CL]{lang="EN-US"}]{#struct_0_x2079_20553_x1548956397}

[[Chile ]{lang="EN-US"}]{#struct_0_x2079_20553_x1886886361}[智利]{style="font-family:宋体"}

[[CN]{lang="EN-US"}]{#struct_0_x2079_20553_472606983}

[[China ]{lang="EN-US"}]{#struct_0_x2079_20553_877213776}[中国]{style="font-family:宋体"}

[[HR]{lang="EN-US"}]{#struct_0_x2079_20553_1134820256}

[[Croatia ]{lang="EN-US"}]{#struct_0_x2079_20553_423826454}[克罗地亚]{style="font-family:宋体"}

[[CU]{lang="EN-US"}]{#struct_0_x2079_20553_975777266}

[[Cuba ]{lang="EN-US"}]{#struct_0_x2079_20553_x1184867941}[古巴]{style="font-family:宋体"}

[[CY]{lang="EN-US"}]{#struct_0_x2079_20553_1801333702}

[[Cyprus ]{lang="EN-US"}]{#struct_0_x2079_20553_1134361505}[塞浦路斯]{style="font-family:宋体"}

[[CZ]{lang="EN-US"}]{#struct_0_x2079_20553_1172414627}

[[Czech Republic ]{lang="EN-US"}]{#struct_0_x2079_20553_1906771697}[捷克]{style="font-family:宋体"}

[[DK]{lang="EN-US"}]{#struct_0_x2079_20553_123836445}

[[Denmark ]{lang="EN-US"}]{#struct_0_x2079_20553_1134295969}[丹麦]{style="font-family:宋体"}

[[EG]{lang="EN-US"}]{#struct_0_x2079_20553_828558936}

[[Egypt ]{lang="EN-US"}]{#struct_0_x2079_20553_x713465737}[埃及]{style="font-family:宋体"}

[[FI]{lang="EN-US"}]{#struct_0_x2079_20553_x1206898576}

[[Finland ]{lang="EN-US"}]{#struct_0_x2079_20553_1134230433}[芬兰]{style="font-family:宋体"}

[[FR]{lang="EN-US"}]{#struct_0_x2079_20553_1564415322}

[[France ]{lang="EN-US"}]{#struct_0_x2079_20553_1357486672}[法国]{style="font-family:宋体"}

[[DE]{lang="EN-US"}]{#struct_0_x2079_20553_1071081704}

[[Germany ]{lang="EN-US"}]{#struct_0_x2079_20553_1134164897}[德国]{style="font-family:宋体"}

[[GH]{lang="EN-US"}]{#struct_0_x2079_20553_1238123145}

[[Ghana ]{lang="EN-US"}]{#struct_0_x2079_20553_x1783002725}[加纳]{style="font-family:宋体"}

[[GR]{lang="EN-US"}]{#struct_0_x2079_20553_1487893797}

[[Greece ]{lang="EN-US"}]{#struct_0_x2079_20553_1134099361}[希腊]{style="font-family:宋体"}

[[HK]{lang="EN-US"}]{#struct_0_x2079_20553_361907550}

[[Hong Kong China ]{lang="EN-US"}]{#struct_0_x2079_20553_x978888077}[中国香港]{style="font-family:宋体"}

[[HU]{lang="EN-US"}]{#struct_0_x2079_20553_1134033825}

[[Hungary ]{lang="EN-US"}]{#struct_0_x2079_20553_1999669688}[匈牙利]{style="font-family:宋体"}

[[IS]{lang="EN-US"}]{#struct_0_x2079_20553_x1982382336}

[[Iceland ]{lang="EN-US"}]{#struct_0_x2079_20553_x726455881}[冰岛]{style="font-family:宋体"}

[[IN]{lang="EN-US"}]{#struct_0_x2079_20553_1133968289}

[[India ]{lang="EN-US"}]{#struct_0_x2079_20553_1287305428}[印度]{style="font-family:宋体"}

[[ID]{lang="EN-US"}]{#struct_0_x2079_20553_x847266146}

[[Indonesia ]{lang="EN-US"}]{#struct_0_x2079_20553_1133902753}[印度尼西亚]{style="font-family:宋体"}

[[IR]{lang="EN-US"}]{#struct_0_x2079_20553_524614959}

[[Iran ]{lang="EN-US"}]{#struct_0_x2079_20553_1432177711}[伊朗]{style="font-family:宋体"}

[[IE]{lang="EN-US"}]{#struct_0_x2079_20553_1134885793}

[[Ireland ]{lang="EN-US"}]{#struct_0_x2079_20553_x1548890861}[爱尔兰]{style="font-family:宋体"}

[[IEU]{lang="EN-US"}]{#struct_0_x2079_20553_725818312}

[[Ireland]{lang="EN-US"}]{#struct_0_x2079_20553_x120935011}[（]{style="font-family:宋体"}[UK style]{lang="EN-US"}[）]{style="font-family:宋体"} [爱尔兰（英国模式）]{style="font-family:宋体"}

[[IL]{lang="EN-US"}]{#struct_0_x2079_20553_1134820257}

[[Israel ]{lang="EN-US"}]{#struct_0_x2079_20553_423891990}[以色列]{style="font-family:宋体"}

[[IT]{lang="EN-US"}]{#struct_0_x2079_20553_x1065734388}

[[Italy ]{lang="EN-US"}]{#struct_0_x2079_20553_x1594521847}[意大利]{style="font-family:宋体"}

[[JP]{lang="EN-US"}]{#struct_0_x2079_20553_x325524247}

[[Japan ]{lang="EN-US"}]{#struct_0_x2079_20553_x1808650543}[日本]{style="font-family:宋体"}

[[JO]{lang="EN-US"}]{#struct_0_x2079_20553_x1594587383}

[[Jordan ]{lang="EN-US"}]{#struct_0_x2079_20553_x1845016072}[约旦]{style="font-family:宋体"}

[[KE]{lang="EN-US"}]{#struct_0_x2079_20553_x1644030687}

[[Kenya ]{lang="EN-US"}]{#struct_0_x2079_20553_x1594652919}[肯尼亚]{style="font-family:宋体"}

[[KR]{lang="EN-US"}]{#struct_0_x2079_20553_x1737821257}

[[Korea Republic ]{lang="EN-US"}]{#struct_0_x2079_20553_1238998116}[韩国]{style="font-family:宋体"}

[[LB]{lang="EN-US"}]{#struct_0_x2079_20553_x1594718455}

[[Lebanon ]{lang="EN-US"}]{#struct_0_x2079_20553_x1143193292}[黎巴嫩]{style="font-family:宋体"}

[[LU]{lang="EN-US"}]{#struct_0_x2079_20553_x949817694}

[[Luxembourg ]{lang="EN-US"}]{#struct_0_x2079_20553_x1594783991}[卢森堡]{style="font-family:宋体"}

[[MO]{lang="EN-US"}]{#struct_0_x2079_20553_x1213517004}

[[Macau ]{lang="EN-US"}]{#struct_0_x2079_20553_x1594849527}[澳门]{style="font-family:宋体"}

[[MY]{lang="EN-US"}]{#struct_0_x2079_20553_496655786}

[[Malaysia ]{lang="EN-US"}]{#struct_0_x2079_20553_81882927}[马来西亚]{style="font-family:宋体"}

[[MX]{lang="EN-US"}]{#struct_0_x2079_20553_x1594915063}

[[Mexico ]{lang="EN-US"}]{#struct_0_x2079_20553_x577677318}[墨西哥]{style="font-family:宋体"}

[[NP]{lang="EN-US"}]{#struct_0_x2079_20553_x951760440}

[[Nepal ]{lang="EN-US"}]{#struct_0_x2079_20553_x1594980599}[尼泊尔]{style="font-family:宋体"}

[[NL]{lang="EN-US"}]{#struct_0_x2079_20553_x736372728}

[[Netherlands ]{lang="EN-US"}]{#struct_0_x2079_20553_x1593997559}[荷兰]{style="font-family:宋体"}

[[NZ]{lang="EN-US"}]{#struct_0_x2079_20553_88522680}

[[New Zealand ]{lang="EN-US"}]{#struct_0_x2079_20553_430226167}[新西兰]{style="font-family:宋体"}

[[NG]{lang="EN-US"}]{#struct_0_x2079_20553_x1594063095}

[[Nigeria ]{lang="EN-US"}]{#struct_0_x2079_20553_x1532872985}[尼日利亚]{style="font-family:宋体"}

[[NO]{lang="EN-US"}]{#struct_0_x2079_20553_x1594521846}

[[Norway ]{lang="EN-US"}]{#struct_0_x2079_20553_1240559694}[挪威]{style="font-family:宋体"}

[[PK]{lang="EN-US"}]{#struct_0_x2079_20553_x1594587382}

[[Pakistan ]{lang="EN-US"}]{#struct_0_x2079_20553_x278932131}[巴基斯坦]{style="font-family:宋体"}

[[PA]{lang="EN-US"}]{#struct_0_x2079_20553_379055129}

[[Panama ]{lang="EN-US"}]{#struct_0_x2079_20553_x1594652918}[巴拿马]{style="font-family:宋体"}

[[PH]{lang="EN-US"}]{#struct_0_x2079_20553_991062098}

[[Philippines ]{lang="EN-US"}]{#struct_0_x2079_20553_x1594718454}[菲律宾]{style="font-family:宋体"}

[[PL]{lang="EN-US"}]{#struct_0_x2079_20553_1585690063}

[[Poland ]{lang="EN-US"}]{#struct_0_x2079_20553_x1594783990}[波兰]{style="font-family:宋体"}

[[PT]{lang="EN-US"}]{#struct_0_x2079_20553_352566937}

[[Portugal ]{lang="EN-US"}]{#struct_0_x2079_20553_1135166745}[葡萄牙]{style="font-family:宋体"}

[[RU]{lang="EN-US"}]{#struct_0_x2079_20553_x1594849526}

[[Russian Federation ]{lang="EN-US"}]{#struct_0_x2079_20553_2062739727}[俄罗斯]{style="font-family:宋体"}

[[SA]{lang="EN-US"}]{#struct_0_x2079_20553_x1594915062}

[[Saudi Arabia ]{lang="EN-US"}]{#struct_0_x2079_20553_x2143761259}[沙特阿拉伯]{style="font-family:宋体"}

[[SG]{lang="EN-US"}]{#struct_0_x2079_20553_x1594980598}

[[Singapore ]{lang="EN-US"}]{#struct_0_x2079_20553_829711213}[新加坡]{style="font-family:宋体"}

[[SK]{lang="EN-US"}]{#struct_0_x2079_20553_x1593997558}

[[Slovakia ]{lang="EN-US"}]{#struct_0_x2079_20553_x1477561261}[斯洛伐克]{style="font-family:宋体"}

[[SI]{lang="EN-US"}]{#struct_0_x2079_20553_x1594063094}

[[Slovenia ]{lang="EN-US"}]{#struct_0_x2079_20553_33210956}[斯洛文尼亚]{style="font-family:宋体"}

[[ZA]{lang="EN-US"}]{#struct_0_x2079_20553_x1594521849}

[[South Africa ]{lang="EN-US"}]{#struct_0_x2079_20553_124814447}[南非]{style="font-family:宋体"}

[[ES]{lang="EN-US"}]{#struct_0_x2079_20553_x1594587385}

[[Spain ]{lang="EN-US"}]{#struct_0_x2079_20553_1643382170}[西班牙]{style="font-family:宋体"}

[[SE]{lang="EN-US"}]{#struct_0_x2079_20553_x1594652921}

[[Sweden ]{lang="EN-US"}]{#struct_0_x2079_20553_x2093986081}[瑞典]{style="font-family:宋体"}

[[CH]{lang="EN-US"}]{#struct_0_x2079_20553_x1594718457}

[[Switzerland ]{lang="EN-US"}]{#struct_0_x2079_20553_19606122}[瑞士]{style="font-family:宋体"}

[[TH]{lang="EN-US"}]{#struct_0_x2079_20553_x1594783993}

[[Thailand ]{lang="EN-US"}]{#struct_0_x2079_20553_1918650878}[泰国]{style="font-family:宋体"}

[[TR]{lang="EN-US"}]{#struct_0_x2079_20553_x1594849529}

[[Turkey ]{lang="EN-US"}]{#struct_0_x2079_20553_46317092}[土耳其]{style="font-family:宋体"}

[[GB]{lang="EN-US"}]{#struct_0_x2079_20553_x1594915065}

[[United Kingdom ]{lang="EN-US"}]{#struct_0_x2079_20553_585122096}[英国]{style="font-family:宋体"}

[[US]{lang="EN-US"}]{#struct_0_x2079_20553_x1594980601}

[[United States ]{lang="EN-US"}]{#struct_0_x2079_20553_x1093061837}[美国]{style="font-family:宋体"}

[[UY]{lang="EN-US"}]{#struct_0_x2079_20553_x1593997561}

[[Uruguay ]{lang="EN-US"}]{#struct_0_x2079_20553_x267511072}[乌拉圭]{style="font-family:宋体"}

[[ZW]{lang="EN-US"}]{#struct_0_x2079_20553_x1594063097}

[[Zimbabwe ]{lang="EN-US"}]{#struct_0_x2079_20553_x370073571}[津巴布韦]{style="font-family:宋体"}

**[ ]{lang="EN-US"}**

[**[custom]{lang="EN-US"}**]{#struct_0_x2079_20553_x435194317}[：自定义模式。]{style="font-family:宋体"}

[**[busy-tone]{lang="EN-US"}**]{#struct_0_x2079_20553_1504448421}[：忙音。]{style="font-family:宋体"}

[**[congestion-tone]{lang="EN-US"}**]{#struct_0_x2079_20553_x1594521848}[：拥塞音。]{style="font-family:宋体"}

[**[dial-tone]{lang="EN-US"}**]{#struct_0_x2079_20553_1690898388}[：拨号音。]{style="font-family:宋体"}

[**[ringback-tone]{lang="EN-US"}**]{#struct_0_x2079_20553_171881172}[：回铃音。]{style="font-family:宋体"}

[**[special-dial-tone]{lang="EN-US"}**]{#struct_0_x2079_20553_x20607101}[：特殊拨号音。]{style="font-family:宋体"}

[**[waiting-tone]{lang="EN-US"}**]{#struct_0_x2079_20553_x1456249576}[：呼叫等待音。]{style="font-family:宋体"}

[*[comb]{lang="EN-US"}*]{#struct_0_x2079_20553_x224111279}[：组合方式，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}[0]{lang="EN-US"}[表示两个频率的叠加，]{style="font-family:
宋体"}[1]{lang="EN-US"}[表示两个频率的调制，]{style="font-family:宋体"}[2]{lang="EN-US"}[表示两个频率的交替。]{style="font-family:宋体"}

[*[freq1 freq2]{lang="EN-US"}*]{#struct_0_x2079_20553_1909093739}[：两个单频音的频率值，单位为]{style="font-family:宋体"}[Hz]{lang="EN-US"}[。频率的取值范围与选择的组合方式相关，如果为叠加方式或交替方式，则两个单频音频率的取值范围为]{style="font-family:宋体"}[300]{lang="EN-US"}[～]{style="font-family:宋体"}[3400]{lang="EN-US"}[；如果为调制方式，则两个单频音频率的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[3400]{lang="EN-US"}[，并要求两个单频音频率的和与差的绝对值必须在]{style="font-family:宋体"}[300]{lang="EN-US"}[～]{style="font-family:宋体"}[3400]{lang="EN-US"}[范围之间。]{style="font-family:宋体"}

[*[time1]{lang="EN-US"}*]{#struct_0_x2079_20553_789491536}[：第一个通断比的通时间的长度，取值范围为]{style="font-family:宋体"}[30]{lang="EN-US"}[～]{style="font-family:宋体"}[8192]{lang="EN-US"}[，单位为毫秒。如果是持续播放，需要将此参数设置为]{style="font-family:宋体"}[8192]{lang="EN-US"}[，在这种情况下，后三个参数取值只能为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[time2]{lang="EN-US"}*]{#struct_0_x2079_20553_1607114207}[：第一个通断比的断时间的长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[或]{style="font-family:宋体"}[30]{lang="EN-US"}[～]{style="font-family:宋体"}[8191]{lang="EN-US"}[，单位为毫秒。如果]{style="font-family:宋体"}*[time1]{lang="EN-US"}*[为]{style="font-family:宋体"}[0]{lang="EN-US"}[，那么该参数只能设置为]{style="font-family:
宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[time3]{lang="EN-US"}*]{#struct_0_x2079_20553_x1594587384}[：第二个通断比的通时间的长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[或]{style="font-family:宋体"}[30]{lang="EN-US"}[～]{style="font-family:宋体"}[8191]{lang="EN-US"}[，单位为毫秒。如果]{style="font-family:宋体"}*[time1]{lang="EN-US"}*[为]{style="font-family:宋体"}[0]{lang="EN-US"}[，那么该参数只能设置为]{style="font-family:
宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[time4]{lang="EN-US"}*]{#struct_0_x2079_20553_x1085501185}[：第二个通断比的断时间的长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[或]{style="font-family:宋体"}[30]{lang="EN-US"}[～]{style="font-family:宋体"}[8191]{lang="EN-US"}[，单位为毫秒。如果]{style="font-family:宋体"}*[time1]{lang="EN-US"}*[为]{style="font-family:宋体"}[0]{lang="EN-US"}[，那么该参数只能设置为]{style="font-family:
宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_2008373102}

[**[cptone]{lang="EN-US"}**]{#struct_0_x2079_20553_450601515}[命令用来设置提示音的国家]{style="font-family:宋体"}[/]{lang="EN-US"}[地区模式。用户也可以使用]{style="font-family:宋体"}**[custom]{lang="EN-US"}**[参数设置自定义模式，定制提示音参数。该设置只对本设备播放的提示音有效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1439476248}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x2145099757}[配置提示音的国家模式为美国。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x831805474}

[\[sysname\] voice-setup]{lang="EN-US"}

[\[sysname-voice\] cptone country-type us]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_231709709}[配置自定义模式，设置组合方式为]{style="font-family:宋体"}[0]{lang="EN-US"}[，两个单频音的频率值为]{style="font-family:宋体"}[425]{lang="EN-US"}[，通断时间均为]{style="font-family:宋体"}[350]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x1594652920}

[\[sysname\] voice-setup]{lang="EN-US"}

[\[sysname-voice\] cptone custom busy-tone 0 425 425 350 350 350 350]{lang="EN-US"}

::: {#-1750664576 .myid}
[]{#_Toc404794435}[]{#struct_0_x2079_20553_634897274}

**语音用户线 \-- 模拟语音用户线 \-- cptone tone-type**

------------------------------------------------------------------------

[**[cptone]{lang="EN-US"}**[ **tone-type**]{lang="EN-US"}]{#struct_0_x2079_20553_x33342010}[命令用来配置提示音的幅度值。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **cptone** **tone-type**]{lang="EN-US"}]{#struct_0_x2079_20553_x1170677101}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1052360250}

[**[cptone tone-type]{lang="EN-US"}**[ { **all** \| **busy-tone** \| **congestion-tone** \| **dial-tone** \| **ringback-tone** \| **special-dial-tone** \| **waiting-tone** } **amplitude** *value*]{lang="EN-US"}]{#struct_0_x2079_20553_831006001}

[**[undo cptone tone-type]{lang="EN-US"}**[ { **all** \| **busy-tone** \| **congestion-tone** \| **dial-tone** \| **ringback-tone** \| **special-dial-tone** \| **waiting-tone** } **amplitude**]{lang="EN-US"}]{#struct_0_x2079_20553_407183023}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1072570011}

[[忙音和拥塞音类型的幅度值为]{style="font-family:宋体"}[1000]{lang="EN-US"}]{#struct_0_x2079_20553_x1594718456}[，拨号音和特殊拨号音类型的幅度值为]{style="font-family:宋体"}[400]{lang="EN-US"}[，回铃音和呼叫等待音类型的幅度值为]{style="font-family:宋体"}[600]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1546477819}

[[语音视图]{style="font-family:宋体"}]{#struct_0_x2079_20553_x204807164}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1782992821}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1042707178}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_56050376}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1102606714}

[**[all]{lang="EN-US"}**]{#struct_0_x2079_20553_x1663038243}[：所有类型的提示音。]{style="font-family:宋体"}

[**[busy-tone]{lang="EN-US"}**]{#struct_0_x2079_20553_514006993}[：忙音。]{style="font-family:宋体"}

[**[congestion-tone]{lang="EN-US"}**]{#struct_0_x2079_20553_x1594783992}[：拥塞音。]{style="font-family:宋体"}

[**[dial-tone]{lang="EN-US"}**]{#struct_0_x2079_20553_x810232477}[：拨号音。]{style="font-family:宋体"}

[**[ringback-tone]{lang="EN-US"}**]{#struct_0_x2079_20553_x671291202}[：回铃音。]{style="font-family:宋体"}

[**[special-dial-tone]{lang="EN-US"}**]{#struct_0_x2079_20553_x2096591551}[：特殊拨号音。]{style="font-family:宋体"}

[**[waiting-tone]{lang="EN-US"}**]{#struct_0_x2079_20553_x1072922106}[：呼叫等待音。]{style="font-family:宋体"}

[**[amplitude]{lang="EN-US"}***[ value]{lang="EN-US"}*]{#struct_0_x2079_20553_x1740564129}[：配置提示音幅度，取值范围为]{style="font-family:宋体"}[200]{lang="EN-US"}[～]{style="font-family:宋体"}[1500]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x319171104}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_1817075071}[配置忙音的电平幅度为]{style="font-family:宋体"}[1200]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x1594849528}

[\[sysname\] voice-setup]{lang="EN-US"}

[\[sysname-voice\] cptone tone-type busy-tone amplitude 1200]{lang="EN-US"}
:::

::: {#-1713937643 .myid}
[]{#_Toc404794436}[]{#struct_0_x2079_20553_1612401033}

**语音用户线 \-- 模拟语音用户线 \-- cng-on**

------------------------------------------------------------------------

[**[cng-on]{lang="EN-US"}**]{#struct_0_x2079_20553_x2130735096}[命令用来开启舒适噪音功能。]{style="font-family:宋体"}

[**[undo cng-on]{lang="EN-US"}**]{#struct_0_x2079_20553_x150954417}[命令用来关闭舒适噪音功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1173561475}

[**[cng-on]{lang="EN-US"}**]{#struct_0_x2079_20553_x1214660668}

[**[undo]{lang="EN-US"}**[ **cng-on**]{lang="EN-US"}]{#struct_0_x2079_20553_x370720207}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x827981150}

[[舒适噪音功能处于开启状态。]{style="font-family:宋体"}]{#struct_0_x2079_20553_1662547541}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1594915064}

[[FXS/FXO/E&M]{lang="EN-US"}]{#struct_0_x2079_20553_x980961845}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x804996634}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_2054085372}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1908789648}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1198441216}

[[使用该命令可以产生适当的背景噪音以填充通话过程中的静音间隙。如果关闭舒适噪音功能，那么通话中的静音间隙可能会使通话者感到不安。]{style="font-family:宋体"}]{#struct_0_x2079_20553_x471748394}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1893573165}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_1595654579}[关闭舒适噪音功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x1594980600}

[\[Sysname\] subscriber-line 2/1/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/1/1\] undo cng-on]{lang="EN-US"}
:::

::: {#1948332219 .myid}
[]{#_Toc404794437}[]{#struct_0_x2079_20553_473022104}[]{#_Toc329007815}[]{#_Toc309912009}

**语音用户线 \-- 模拟语音用户线 \-- default**

------------------------------------------------------------------------

[**[default]{lang="EN-US"}**]{#struct_0_x2079_20553_1396804538}[命令用来恢复当前语音用户线的缺省配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_602024466}

[**[default]{lang="EN-US"}**]{#struct_0_x2079_20553_x17218641}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1622164065}

[[FXS/FXO/E&M]{lang="EN-US"}]{#struct_0_x2079_20553_1239552486}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1389036106}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1593997560}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1833595013}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1920616866}

[[语音用户线下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。]{style="font-family:宋体"}]{#struct_0_x2079_20553_1063144034}

[[您可以在执行]{style="font-family:宋体"}**[default]{lang="EN-US"}**]{#struct_0_x2079_20553_1976051224}[命令后通过]{style="font-family:宋体"}**[display this]{lang="EN-US"}**[命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1350778770}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x1958397849}[将语音用户线]{style="font-family:宋体"}[2/2/1]{lang="EN-US"}[恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x2065676835}

[\[Sysname\] subscriber-line 2/1/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/1/1\] default]{lang="EN-US"}
:::

::: {#1663943886 .myid}
[]{#_Toc404794438}[]{#struct_0_x2079_20553_x1594063096}[]{#_Toc318291919}[]{#_Toc263260021}

**语音用户线 \-- 模拟语音用户线 \-- delay hold**

------------------------------------------------------------------------

[**[delay]{lang="EN-US"}**[ **hold**]{lang="EN-US"}]{#struct_0_x2079_20553_1196010370}[命令用来配置延时启动时，占用信号的持续时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **delay** **hold**]{lang="EN-US"}]{#struct_0_x2079_20553_x1969006414}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1589720986}

[**[delay]{lang="EN-US"}**[ **hold** *milliseconds*]{lang="EN-US"}]{#struct_0_x2079_20553_1009348788}

[**[undo]{lang="EN-US"}**[ **delay** **hold**]{lang="EN-US"}]{#struct_0_x2079_20553_x732903203}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1077586030}

[[占用信号的持续时间为]{style="font-family:宋体"}[400]{lang="EN-US"}]{#struct_0_x2079_20553_x1445113047}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1092241516}

[[E&M]{lang="EN-US"}]{#struct_0_x2079_20553_x1594521851}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_480979271}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1725749739}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1193133747}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1695221055}

[*[milliseconds]{lang="EN-US"}*]{#struct_0_x2079_20553_x65498235}[：延时启动方式时，占用信号的持续时间，取值范围为]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[5000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1074268594}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x1114009496}[配置在延时启动方式时，占用信号的持续时间为]{style="font-family:宋体"}[500]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x1594587387}

[\[Sysname\] subscriber-line 2/3/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/3/1\] signal delay]{lang="EN-US"}

[\[Sysname-subscriber-line2/3/1\] delay hold 500]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_480582756}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[signal]{lang="EN-US"}**]{#struct_0_x2079_20553_x708875446}
:::

::: {#-2113137212 .myid}
[]{#_Toc404794439}[]{#struct_0_x2079_20553_195442920}

**语音用户线 \-- 模拟语音用户线 \-- delay rising**

------------------------------------------------------------------------

[**[delay]{lang="EN-US"}**[ **rising**]{lang="EN-US"}]{#struct_0_x2079_20553_x1732422454}[命令用来配置延时启动时，被叫侧检测到占用信号到发送占用信号前的延时时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **delay** **rising**]{lang="EN-US"}]{#struct_0_x2079_20553_x185069516}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x381676600}

[**[delay]{lang="EN-US"}**[ **rising** *milliseconds*]{lang="EN-US"}]{#struct_0_x2079_20553_x1076285854}

[**[undo]{lang="EN-US"}**[ **delay** **rising**]{lang="EN-US"}]{#struct_0_x2079_20553_409436388}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1594652923}

[[被叫侧检测到占用信号到发送占用信号前的延时时间为]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_x2079_20553_x931186667}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_18217172}

[[E&M]{lang="EN-US"}]{#struct_0_x2079_20553_1517465479}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_695165552}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1687994205}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_798771382}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1611732854}

[*[milliseconds]{lang="EN-US"}*]{#struct_0_x2079_20553_1658009199}[：延时启动方式时，被叫侧检测到占用信号到发送占用信号前的延时时间，取值范围为]{style="font-family:宋体"}[20]{lang="EN-US"}[～]{style="font-family:宋体"}[2000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1594718459}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_469944816}[配置在延时启动方式时，被叫侧检测到占用信号到发送占用信号前的延时时间为]{style="font-family:宋体"}[700]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x1914396837}

[\[Sysname\] subscriber-line 2/3/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/3/1\] signal delay]{lang="EN-US"}

[\[Sysname-subscriber-line2/3/1\] delay rising 700]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1556699514}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[signal]{lang="EN-US"}**]{#struct_0_x2079_20553_1210799372}
:::

::: {#-9215474 .myid}
[]{#_Toc404794440}[]{#struct_0_x2079_20553_179975432}[]{#_Toc318291917}[]{#_Toc263260023}

**语音用户线 \-- 模拟语音用户线 \-- delay send-dtmf**

------------------------------------------------------------------------

[**[delay]{lang="EN-US"}**[ **send-dtmf**]{lang="EN-US"}]{#struct_0_x2079_20553_920529589}[命令用来配置在立即启动方式时，主叫侧发送号码前的延迟时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **delay** **send-dtmf**]{lang="EN-US"}]{#struct_0_x2079_20553_x156727102}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1594783995}

[**[delay]{lang="EN-US"}**[ **send-dtmf** *milliseconds*]{lang="EN-US"}]{#struct_0_x2079_20553_1112081824}

[**[undo]{lang="EN-US"}**[ **delay** **send-dtmf**]{lang="EN-US"}]{#struct_0_x2079_20553_836210828}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1454192476}

[[主叫侧发送号码前的延迟时间为]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_x2079_20553_x1761151737}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x522378511}

[[E&M]{lang="EN-US"}]{#struct_0_x2079_20553_881501677}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1744959513}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1756476467}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1594849531}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x309847732}

[*[milliseconds]{lang="EN-US"}*]{#struct_0_x2079_20553_x1828040776}[：立即启动方式时，主叫侧发送号码前的延迟时间，取值范围为]{style="font-family:宋体"}[50]{lang="EN-US"}[～]{style="font-family:宋体"}[5000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x265394710}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_899019600}[配置在立即启动方式下，主叫侧发送号码前的延迟时间为]{style="font-family:宋体"}[3000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_484531083}

[\[Sysname\] subscriber-line 2/3/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/3/1\] signal immediate]{lang="EN-US"}

[\[Sysname-subscriber-line2/3/1\] delay send-dtmf 3000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x819122511}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[signal]{lang="EN-US"}**]{#struct_0_x2079_20553_x831133467}
:::

::: {#-902017584 .myid}
[]{#_Toc404794441}[]{#struct_0_x2079_20553_x1594915067}

**语音用户线 \-- 模拟语音用户线 \-- delay send-wink**

------------------------------------------------------------------------

[**[delay]{lang="EN-US"}**[ **send-wink**]{lang="EN-US"}]{#struct_0_x2079_20553_1747921510}[命令用来配置闪断启动时，被叫侧检测到占用信号到发送闪断信号前的延迟时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **delay** **send-wink**]{lang="EN-US"}]{#struct_0_x2079_20553_x539510968}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1351213689}

[**[delay]{lang="EN-US"}**[ **send-wink** *milliseconds*]{lang="EN-US"}]{#struct_0_x2079_20553_640403322}

[**[undo]{lang="EN-US"}**[ **delay** **send-wink**]{lang="EN-US"}]{#struct_0_x2079_20553_883069388}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x2101173499}

[[被叫侧检测到占用信号到发送闪断信号前的延迟时间为]{style="font-family:宋体"}[200]{lang="EN-US"}]{#struct_0_x2079_20553_234554783}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1868558446}

[[E&M]{lang="EN-US"}]{#struct_0_x2079_20553_x1594980603}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_2039106045}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1499012863}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1282436989}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x187211732}

[*[milliseconds]{lang="EN-US"}*]{#struct_0_x2079_20553_x1671644960}[：闪断启动方式时，被叫]{style="font-family:宋体"}[侧检测到占用信号到发送闪断信号前的延迟时间，取值范围为]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[5000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_957159634}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_1709772329}[配置在闪断启动方式下，被叫侧检测到占用信号到发送闪断信号前的延迟时间为]{style="font-family:宋体"}[700]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x1593997563}

[\[Sysname\] subscriber-line 2/3/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/3/1\] signal wink]{lang="EN-US"}

[\[Sysname-subscriber-line2/3/1\] delay send-wink 700]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_895288342}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[signal]{lang="EN-US"}**]{#struct_0_x2079_20553_406381007}
:::

::: {#-2091914529 .myid}
[]{#_Toc404794442}[]{#struct_0_x2079_20553_x341623460}[]{#_Toc316549750}[]{#_Toc295912522}[]{#_Toc263260027}[]{#_Toc135295464}

**语音用户线 \-- 模拟语音用户线 \-- delay start-dial**

------------------------------------------------------------------------

[**[delay]{lang="EN-US"}**[ **start-dial**]{lang="EN-US"}]{#struct_0_x2079_20553_118463735}[命令用来配置延时拨号的时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **delay** **start-dial**]{lang="EN-US"}]{#struct_0_x2079_20553_x408365828}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1431816182}

[**[delay]{lang="EN-US"}**[ **start-dial** *seconds*]{lang="EN-US"}]{#struct_0_x2079_20553_x224001790}

[**[undo]{lang="EN-US"}**[ **delay** **start-dial**]{lang="EN-US"}]{#struct_0_x2079_20553_719942918}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1594063099}

[[延时拨号的时间为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x2079_20553_1148956203}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_490833677}

[[FXS/FXO]{lang="EN-US"}]{#struct_0_x2079_20553_x793577481}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1387160920}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1748326886}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1732761552}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_256824181}

[*[seconds]{lang="EN-US"}*]{#struct_0_x2079_20553_x517489758}[：延时拨号的时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1594521850}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_2047063212}[配置延时拨号时间为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_1648149179}

[\[Sysname\] subscriber-line 2/1/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/1/1\] delay start-dial 5]{lang="EN-US"}
:::

::: {#-348645211 .myid}
[]{#_Toc404794443}[]{#struct_0_x2079_20553_999972142}

**语音用户线 \-- 模拟语音用户线 \-- delay wink-hold**

------------------------------------------------------------------------

[**[delay]{lang="EN-US"}**[ **wink-hold**]{lang="EN-US"}]{#struct_0_x2079_20553_x1997209157}[命令用来配置闪断启动方式时，被叫侧发送闪断信号的持续时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **delay** **wink-hold**]{lang="EN-US"}]{#struct_0_x2079_20553_x223093005}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x341025211}

[**[delay]{lang="EN-US"}**[ **wink-hold** *milliseconds*]{lang="EN-US"}]{#struct_0_x2079_20553_102740632}

[**[undo]{lang="EN-US"}**[ **delay** **wink-hold**]{lang="EN-US"}]{#struct_0_x2079_20553_x1594587386}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_2046666697}

[[被叫侧发送闪断信号的持续时间为]{style="font-family:宋体"}[500]{lang="EN-US"}]{#struct_0_x2079_20553_1633647598}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x62802160}

[[E&M]{lang="EN-US"}]{#struct_0_x2079_20553_1728476430}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x2009052632}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_935134307}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1034151274}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x2109890460}

[*[milliseconds]{lang="EN-US"}*]{#struct_0_x2079_20553_x1594652922}[：闪断启动方式时，被叫侧发送闪断信号的持续时间，取值范围为]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[3000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1797696688}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x6667864}[配置在闪断启动方式时，被叫侧发送闪断信号的持续时间为]{style="font-family:宋体"}[700]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x1046938068}

[\[Sysname\] subscriber-line 2/3/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/3/1\] signal wink]{lang="EN-US"}

[\[Sysname-subscriber-line2/3/1\] delay wink-hold 700]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_212755058}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[signal]{lang="EN-US"}**]{#struct_0_x2079_20553_1727473530}
:::

::: {#265704851 .myid}
[]{#_Toc404794444}[]{#struct_0_x2079_20553_892703023}

**语音用户线 \-- 模拟语音用户线 \-- delay wink-rising**

------------------------------------------------------------------------

[**[delay]{lang="EN-US"}**[ **wink-rising**]{lang="EN-US"}]{#struct_0_x2079_20553_668224872}[命令用来配置闪断启动时，主叫侧发送占用信号后等待闪断信号的最大持续时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **delay** **wink-rising**]{lang="EN-US"}]{#struct_0_x2079_20553_x1594718458}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1096139125}

[**[delay]{lang="EN-US"}**[ **wink-rising** *milliseconds*]{lang="EN-US"}]{#struct_0_x2079_20553_1174560712}

[**[undo]{lang="EN-US"}**[ **delay** **wink-rising**]{lang="EN-US"}]{#struct_0_x2079_20553_x1340853147}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1573333107}

[[主叫侧发送占用信号后等待闪断信号的最大持续时间为]{style="font-family:宋体"}[2000]{lang="EN-US"}]{#struct_0_x2079_20553_855812548}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x422971463}

[[E&M]{lang="EN-US"}]{#struct_0_x2079_20553_1120958034}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x696592496}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1594783994}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1616801531}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x776317345}

[*[milliseconds]{lang="EN-US"}*]{#struct_0_x2079_20553_x743749312}[：闪断启动方式时，主叫侧发送占用信号后等待闪断信号的最大持续时间，取值范围为]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[5000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x340710686}

[[如果在该时间内，主叫侧没有收到被叫侧发送的闪断信号，则此次建立呼叫失败。]{style="font-family:宋体"}]{#struct_0_x2079_20553_1678578041}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_539529095}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_389171174}[配置在闪断启动方式时，主叫侧发送占用信号后等待闪断信号的最大持续时间为]{style="font-family:宋体"}[2000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x1594849530}

[\[Sysname\] subscriber-line 2/3/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/3/1\] signal wink]{lang="EN-US"}

[\[Sysname-subscriber-line2/3/1\] delay wink-rising 2000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1256236209}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[signal]{lang="EN-US"}**]{#struct_0_x2079_20553_2045209009}
:::

::: {#-1461383778 .myid}
[]{#_Toc404794445}[]{#struct_0_x2079_20553_x1000976250}[]{#_Toc329265664}

**语音用户线 \-- 模拟语音用户线 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_x2079_20553_x1469719454}[命令用来配置语音用户线的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_x2079_20553_x994692574}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1799109938}

[**[description]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_x2079_20553_966278939}

[**[undo description]{lang="EN-US"}**]{#struct_0_x2079_20553_x774618804}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1594915066}

[[语音用户线的描述信息为"*该接口的接口名*]{style="font-family:宋体"}[ Interface]{lang="EN-US"}]{#struct_0_x2079_20553_181837569}["，比如：]{style="font-family:宋体"}[Subscriber-line1/0 Interface]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1097425682}

[[FXS/FXO/E&M]{lang="EN-US"}]{#struct_0_x2079_20553_x949373438}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x2133287851}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1586584392}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1250211519}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1979004483}

[*[text]{lang="EN-US"}*]{#struct_0_x2079_20553_x351467669}[：语音用户线描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[80]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1594980602}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x689777310}[配置语音用户线]{style="font-family:宋体"}[1/0]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[pstn]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_1417323228}

[\[Sysname\] subscriber-line 2/1/1]{lang="EN-US"}

[\[Sysname-Subscriber-line2/1/1\] description pstn]{lang="EN-US"}
:::

::: {#-1554523002 .myid}
[]{#_Toc404794446}[]{#struct_0_x2079_20553_2077534073}

**语音用户线 \-- 模拟语音用户线 \-- disconnect lcfo**

------------------------------------------------------------------------

[**[disconnect lcfo]{lang="EN-US"}**]{#struct_0_x2079_20553_x476906730}[命令用来配置发送挂机脉冲信号。]{style="font-family:宋体"}

[**[undo disconnect lcfo]{lang="EN-US"}**]{#struct_0_x2079_20553_x1186480507}[命令用来禁止发送挂机脉冲信号。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1099866180}

[**[disconnect lcfo]{lang="EN-US"}**]{#struct_0_x2079_20553_14368995}

[**[undo disconnect lcfo]{lang="EN-US"}**]{#struct_0_x2079_20553_x1593997562}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x670795599}

[[禁止发送挂机脉冲信号，即直接向对端设备播放忙音。]{style="font-family:宋体"}]{#struct_0_x2079_20553_636313721}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_837183010}

[[FXS]{lang="EN-US"}]{#struct_0_x2079_20553_x2005250152}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_671810534}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1223146221}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1531320419}

[[【使用指导】]{style="font-family:
黑体"}]{#struct_0_x2079_20553_4134204}

[[FXS]{lang="EN-US"}]{#struct_0_x2079_20553_x1594063098}[语音用户线可以发送]{style="font-family:宋体"}[LCFO]{lang="EN-US"}[（]{style="font-family:宋体"}[Loop Current Feed Open]{lang="EN-US"}[，脉冲挂机信号）通知对端设备拆线。此功能主要在北美地区使用。挂机脉冲信号的时长可以通过命令]{style="font-family:宋体"}**[timer disconnect-pulse]{lang="EN-US"}**[设置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1579927152}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x117828901}[配置发送挂机脉冲信号。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_1687386105}

[\[Sysname\] subscriber-line 2/1/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/1/1\] disconnect lcfo]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1968136394}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer disconnect-pulse]{lang="EN-US"}**]{#struct_0_x2079_20553_1451036488}
:::

::: {#232120452 .myid}
[]{#_Toc404794447}[]{#struct_0_x2079_20553_728459623}

**语音用户线 \-- 模拟语音用户线 \-- display voice subscriber-line**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **voice subscriber-line**]{lang="EN-US"}]{#struct_0_x2079_20553_x1131198846}[命令用来显示模拟语音用户线信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_327792454}

[**[display]{lang="EN-US"}**[ **voice subscriber-line** *line-number*]{lang="EN-US"}]{#struct_0_x2079_20553_579599822}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x262561333}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2079_20553_x117008961}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1683060367}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x75597961}

[[network-operator]{lang="EN-US"}]{#struct_0_x2079_20553_x368499927}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1580134665}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2079_20553_x1605219900}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_327726918}

[*[line-number]{lang="EN-US"}*]{#struct_0_x2079_20553_219878104}[：语音用户线号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1755043702}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_78563135}[显示模拟语音用户线信息。]{style="font-family:宋体"}

[[\<Sysname\> display voice subscriber-line 2/3/1]{lang="EN-US"}]{#struct_0_x2079_20553_x178342212}

[Current information:]{lang="EN-US"}[ ]{lang="EN-US"}[subscriber-line2/3/1]{lang="EN-US"}

[    ]{lang="NO-BOK"}[Type: E&M]{lang="EN-US"}

[    ]{lang="NO-BOK"}[Status: Up]{lang="EN-US"}

[    Call status: Idle]{lang="NO-BOK"}

[[表1-2 ]{lang="EN-US"}[display voice subscriber-line]{lang="EN-US"}]{#struct_0_x2079_20553_1874848597}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_247113531}[[字段]{style="font-family:黑体"}]{#struct_0_x2079_20553_x612331730}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2079_20553_327661382}

[[Current information]{lang="EN-US"}]{#struct_0_x2079_20553_1770692964}

[[当前语音用户线的信息]{style="font-family:宋体"}]{#struct_0_x2079_20553_1256857076}

[[Type]{lang="EN-US"}]{#struct_0_x2079_20553_x1078922287}

[[模拟语音用户线的类型：]{style="font-family:宋体"}]{#struct_0_x2079_20553_988843811}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FXS]{lang="EN-US"}]{#struct_0_x2079_20553_1594093501}[：模拟]{style="font-family:宋体"}[FXS]{lang="EN-US"}[语音用户线]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FXO]{lang="EN-US"}]{#struct_0_x2079_20553_327595846}[：模拟]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E&M]{lang="EN-US"}]{#struct_0_x2079_20553_1487177356}[：模拟]{style="font-family:宋体"}[E&M]{lang="EN-US"}[语音用户线]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_x2079_20553_188798249}

[[语音用户线的状态：]{style="font-family:宋体"}]{#struct_0_x2079_20553_x2110419682}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_x2079_20553_925281859}[：语音用户线处于]{style="font-family:宋体"}[Down]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_x2079_20553_x2046826384}[：语音用户线处于]{style="font-family:宋体"}[Up]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down(Administratively)]{lang="EN-US"}]{#struct_0_x2079_20553_327530310}[：语音用户线表示已经通过]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，即管理状态为关闭]{style="font-family:宋体"}

[[Call Status]{lang="EN-US"}]{#struct_0_x2079_20553_1475453119}

[[FXS]{lang="EN-US"}]{#struct_0_x2079_20553_1342023965}[语音用户线的呼叫状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Idle]{lang="EN-US"}]{#struct_0_x2079_20553_1176031041}[：空闲状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Receiving number]{lang="EN-US"}]{#struct_0_x2079_20553_327464774}[：接收号码状态]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ringing]{lang="EN-US"}]{#struct_0_x2079_20553_x521899054}[：振铃状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Listening to ringback tone]{lang="EN-US"}]{#struct_0_x2079_20553_x1770710197}[：主叫设备处于听回铃音状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Playing busytone]{lang="EN-US"}]{#struct_0_x2079_20553_1343353136}[：播放忙音状态]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Talking]{lang="EN-US"}]{#struct_0_x2079_20553_x1180971167}[：通话状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Releasing]{lang="EN-US"}]{#struct_0_x2079_20553_327399238}[：拆线状态]{lang="EN-US" style="font-family:宋体"}

[[FXO]{lang="EN-US"}]{#struct_0_x2079_20553_x755886948}[语音用户线的呼叫状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Idle]{lang="EN-US"}]{#struct_0_x2079_20553_2125739878}[：空闲状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Receiving number]{lang="EN-US"}]{#struct_0_x2079_20553_1835221176}[：接收号码状态]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ringing]{lang="EN-US"}]{#struct_0_x2079_20553_1514709187}[：振铃状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Listening to ringback tone]{lang="EN-US"}]{#struct_0_x2079_20553_327333702}[：主叫设备处于听回铃音状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Playing busytone]{lang="EN-US"}]{#struct_0_x2079_20553_1583444777}[：播放忙音状态]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Talking]{lang="EN-US"}]{#struct_0_x2079_20553_x1351530152}[：通话状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Releasing]{lang="EN-US"}]{#struct_0_x2079_20553_x466194558}[：拆线状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Bound and off-hook]{lang="EN-US"}]{#struct_0_x2079_20553_240579370}[：]{lang="EN-US" style="font-family:
  宋体"}[FXO]{lang="EN-US"}[语音用户线已经被绑定，并处于强制摘机状态]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Bound and on-hook]{lang="EN-US"}]{#struct_0_x2079_20553_328316742}[：]{lang="EN-US" style="font-family:
  宋体"}[FXO]{lang="EN-US"}[语音用户线已经被绑定，并处于强制挂机状态]{lang="EN-US" style="font-family:
  宋体"}

[[E&M]{lang="EN-US"}]{#struct_0_x2079_20553_x1023226716}[语音用户线的呼叫状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Idle]{lang="EN-US"}]{#struct_0_x2079_20553_1583118201}[：空闲状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Sending number]{lang="EN-US"}]{#struct_0_x2079_20553_1820316282}[：发送号码状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ringing]{lang="EN-US"}]{#struct_0_x2079_20553_328251206}[：振铃状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Listening to ringback tone]{lang="EN-US"}]{#struct_0_x2079_20553_970032669}[：主叫设备处于听回铃音状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Playing busytone]{lang="EN-US"}]{#struct_0_x2079_20553_x1175114927}[：播放忙音状态]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Talking]{lang="EN-US"}]{#struct_0_x2079_20553_1737683825}[：通话状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Releasing]{lang="EN-US"}]{#struct_0_x2079_20553_327792455}[：拆线状态]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-355308413 .myid}
[]{#struct_0_x2079_20553_579599823}[]{#_Toc404794448}[]{#_Toc135295477}

**语音用户线 \-- 模拟语音用户线 \-- dtmf amplitude**

------------------------------------------------------------------------

[**[dtmf]{lang="EN-US"}**[ **amplitude**]{lang="EN-US"}]{#struct_0_x2079_20553_x262561334}[命令用来配置]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号的幅值。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **dtmf** **amplitude**]{lang="EN-US"}]{#struct_0_x2079_20553_x117074497}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x609115108}

[**[dtmf]{lang="EN-US"}**[ **amplitude** *value*]{lang="EN-US"}]{#struct_0_x2079_20553_x368887835}

[**[undo]{lang="EN-US"}**[ **dtmf** **amplitude**]{lang="EN-US"}]{#struct_0_x2079_20553_x1203809786}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_619245901}

[[DTMF]{lang="EN-US"}]{#struct_0_x2079_20553_327726919}[信号的幅值为]{style="font-family:宋体"}[-9.0dBm]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_219878103}

[[语音视图]{style="font-family:宋体"}]{#struct_0_x2079_20553_1755043699}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1877293256}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_911177660}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_2103577602}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_264795485}

[*[value]{lang="EN-US"}*]{#struct_0_x2079_20553_x739548260}[：]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号的幅值，取值范围为]{style="font-family:宋体"}[-9.0]{lang="EN-US"}[～]{style="font-family:宋体"}[-7.0]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[dBm]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1541437615}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_327661383}[配置]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号的幅值为]{style="font-family:宋体"}[-8.0dBm]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_1770692963}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dtmf amplitude -8.0]{lang="EN-US"}
:::

::::: {#1338905256 .myid}
[]{#_Toc404794449}[]{#struct_0_x2079_20553_1256398324}[]{#_Toc316549751}[]{#_Toc295912526}[]{#_Toc263260031}[]{#_Toc135295478}[]{#_Toc130097126}[]{#_Toc129160846}[]{#_Toc115163579}

**语音用户线 \-- 模拟语音用户线 \-- dtmf sensitivity-level**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](语音用户线命令.files/image001.png){#图片 16 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2079_20553_x382350834}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[该命令的支持情况与实际使用的板卡有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2079_20553_397231244}
:::

[ ]{lang="EN-US"}

[**[dtmf]{lang="EN-US"}**[ **sensitivity-level**]{lang="EN-US"}]{#struct_0_x2079_20553_864097622}[命令用来配置检测]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号的敏感度等级。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **dtmf** **sensitivity-level**]{lang="EN-US"}]{#struct_0_x2079_20553_x1102077211}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_327595847}

[**[dtmf]{lang="EN-US"}**[ **sensitivity-level** { **high** \| **low** \| **medium** \[ **frequency-tolerance** *value* \] }]{lang="EN-US"}]{#struct_0_x2079_20553_1487177357}

[**[undo]{lang="EN-US"}**[ **dtmf** **sensitivity-level**]{lang="EN-US"}]{#struct_0_x2079_20553_188863785}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_737727740}

[[检测]{style="font-family:宋体"}[DTMF]{lang="EN-US"}]{#struct_0_x2079_20553_1140220486}[信号的敏感度为低级。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x2080357360}

[[FXS/FXO]{lang="EN-US"}]{#struct_0_x2079_20553_1503980631}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_369894083}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1525829408}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_327530311}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1475453120}

[**[high]{lang="EN-US"}**]{#struct_0_x2079_20553_1342482720}[：检测]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号的敏感度为高级，可靠性较低，使用此模式可能出现]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号误检的情况。]{style="font-family:宋体"}

[**[low]{lang="EN-US"}**]{#struct_0_x2079_20553_x418620898}[：检测]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号的敏感度为低级，可靠性较高，使用此模式可能出现]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号漏检的情况。]{style="font-family:宋体"}

[**[medium]{lang="EN-US"}**]{#struct_0_x2079_20553_x894971162}[：检测]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号的敏感度为中级。]{style="font-family:宋体"}

[**[frequency-tolerance]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x2079_20553_x346115607}[：允许的绝对频率偏差，取值范围为]{style="font-family:宋体"}[1.0]{lang="EN-US"}[～]{style="font-family:宋体"}[5.0]{lang="EN-US"}[，单位百分比，缺省值为]{style="font-family:宋体"}[2]{lang="EN-US"}[。取值越大，误检概率越大。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_884191994}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x608208899}[配置检测]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号的敏感度为高级。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_327464775}

[\[Sysname\] subscriber-line 2/1/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/1/1\] dtmf sensitivity-level high]{lang="EN-US"}
:::::

::: {#1217866863 .myid}
[]{#struct_0_x2079_20553_x521899055}[]{#_Toc404794450}

**语音用户线 \-- 模拟语音用户线 \-- dtmf time**

------------------------------------------------------------------------

[**[dtmf]{lang="EN-US"}**[ **time**]{lang="EN-US"}]{#struct_0_x2079_20553_x1770775733}[命令用来配置发送]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号的相关时间参数。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **dtmf** **time**]{lang="EN-US"}]{#struct_0_x2079_20553_x259748432}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1819580295}

[**[dtmf]{lang="EN-US"}**[ **time** { **interval** \| **persist** } *milliseconds*]{lang="EN-US"}]{#struct_0_x2079_20553_x455736181}

[**[undo]{lang="EN-US"}**[ **dtmf** **time** { **interval** \| **persist** }]{lang="EN-US"}]{#struct_0_x2079_20553_x310429934}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1161952549}

[[发送]{style="font-family:宋体"}[DTMF]{lang="EN-US"}]{#struct_0_x2079_20553_327399239}[信号的持续时间和发送间隔时间都为]{style="font-family:宋体"}[120]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x755886947}

[[语音视图]{style="font-family:宋体"}]{#struct_0_x2079_20553_2126198630}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1245367251}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x314835729}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1045942028}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x563996280}

[**[persist]{lang="EN-US"}**]{#struct_0_x2079_20553_x2046370478}[：发送]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号的持续时间。]{style="font-family:宋体"}

[**[interval]{lang="EN-US"}**]{#struct_0_x2079_20553_x2042939214}[：发送]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号的间隔时间。]{style="font-family:宋体"}

[*[milliseconds]{lang="EN-US"}*]{#struct_0_x2079_20553_327333703}[：指定时间，取值范围为]{style="font-family:宋体"}[50]{lang="EN-US"}[～]{style="font-family:宋体"}[500]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1583444778}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x1352251048}[配置发送]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号的持续时间为]{style="font-family:宋体"}[200]{lang="EN-US"}[毫秒，发送间隔为]{style="font-family:宋体"}[300]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_2053098894}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dtmf time persist 200]{lang="EN-US"}

[\[Sysname-voice\] dtmf time interval 300]{lang="EN-US"}
:::

::: {#1886217264 .myid}
[]{#_Toc404794451}[]{#struct_0_x2079_20553_52936033}

**语音用户线 \-- 模拟语音用户线 \-- dtmf threshold analog**

------------------------------------------------------------------------

[**[dtmf]{lang="EN-US"}**[ **threshold analog**]{lang="EN-US"}]{#struct_0_x2079_20553_1640032929}[命令用来配置检测]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号的阈值参数。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **dtmf** **threshold analog**]{lang="EN-US"}]{#struct_0_x2079_20553_x1889969503}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_178311106}

[**[dtmf]{lang="EN-US"}**[ **threshold** **analog** *index* *value*]{lang="EN-US"}]{#struct_0_x2079_20553_328316743}

[**[undo dtmf threshold analog ]{lang="EN-US"}***[index]{lang="EN-US"}*]{#struct_0_x2079_20553_x1023226715}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_17034260}

[[按照序号从]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x2079_20553_1247214943}[到]{style="font-family:宋体"}[12]{lang="EN-US"}[的顺序，阈值参数分别为]{style="font-family:宋体"}[{1400]{lang="EN-US"}[，]{style="font-family:宋体"}[458]{lang="EN-US"}[，]{style="font-family:宋体"}[-9]{lang="EN-US"}[，]{style="font-family:宋体"}[-9]{lang="EN-US"}[，]{style="font-family:宋体"}[-9]{lang="EN-US"}[，]{style="font-family:宋体"}[-9]{lang="EN-US"}[，]{style="font-family:宋体"}[-3]{lang="EN-US"}[，]{style="font-family:宋体"}[-12]{lang="EN-US"}[，]{style="font-family:宋体"}[-12]{lang="EN-US"}[，]{style="font-family:宋体"}[30]{lang="EN-US"}[，]{style="font-family:宋体"}[300]{lang="EN-US"}[，]{style="font-family:宋体"}[3200]{lang="EN-US"}[，]{style="font-family:宋体"}[375}]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1492480432}

[[FXS/FXO/E&M]{lang="EN-US"}]{#struct_0_x2079_20553_x1788323798}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_309673711}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_588367082}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_328251207}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_970032670}

[*[index]{lang="EN-US"}*]{#struct_0_x2079_20553_1163537226}[：阈值的索引号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[12]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[value]{lang="EN-US"}*]{#struct_0_x2079_20553_987661156}[：检测]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号的阈值参数，取值范围与索引号]{style="font-family:宋体"}*[index]{lang="EN-US"}*[的取值有关，具体参数的取值范围和含义请参见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}1-3]{lang="EN-US"}](?1886217264#_Ref149023135)[。]{style="font-family:
宋体"}

[[DTMF]{lang="EN-US"}]{#struct_0_x2079_20553_1590091212}[信号检测是通过输入的]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号在]{style="font-family:宋体"}[4]{lang="EN-US"}[个行频率和]{style="font-family:宋体"}[4]{lang="EN-US"}[个列频率上的能量，以及它们的二倍频上的能量来判断]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号的有效性。为了方便描述，标识输入信号在行频组上的最大能量值为]{style="font-family:宋体"}[ROWMAX]{lang="EN-US"}[，其对应的二倍频能量为]{style="font-family:宋体"}[ROW2nd]{lang="EN-US"}[，在列频率组上的能量最大值为]{style="font-family:宋体"}[COLMAX]{lang="EN-US"}[，其对应的二倍频能量为]{style="font-family:宋体"}[COL2nd]{lang="EN-US"}[。]{style="font-family:宋体"}

[]{#struct_0_x2079_20553_x315169774}[[表1-3 ]{lang="EN-US"}[检测]{style="font-family:
黑体"}[DTMF]{lang="EN-US"}]{#_Ref149023135}[信号的阈值参数]{style="font-family:黑体"}

[]{#table_struct_0_242792827}[[索引号]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1834155438}
:::

[[含义]{style="font-family:黑体"}]{#struct_0_x2079_20553_1895641054}

[[取值范围]{style="font-family:黑体"}]{#struct_0_x2079_20553_327792452}

[[说明]{style="font-family:黑体"}]{#struct_0_x2079_20553_579599820}

[[0]{lang="EN-US"}]{#struct_0_x2079_20553_x262561335}

[[与]{style="font-family:宋体"}[DTMF]{lang="EN-US"}]{#struct_0_x2079_20553_x117140033}[信号强度有关。输入信号要被识别为]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号必须满足（]{style="font-family:宋体"}[ROWMAX+COLMAX]{lang="EN-US"}[）]{style="font-family:宋体"}[\>]{lang="EN-US"}[索引号]{style="font-family:宋体"}[0]{lang="EN-US"}[对应的阈值，否则视为信号强度不足]{style="font-family:宋体"}

[[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x2079_20553_2127352345}[～]{style="font-family:宋体"}[4999]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1400]{lang="EN-US"}

[[取值越大，检测可靠性越高，但灵敏度会下降]{style="font-family:宋体"}]{#struct_0_x2079_20553_x1023733778}

[[1]{lang="EN-US"}]{#struct_0_x2079_20553_327726916}

[[与]{style="font-family:宋体"}[DTMF]{lang="EN-US"}]{#struct_0_x2079_20553_219878094}[信号之间的停顿有关。一个]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号在被检测到之后，只有满足]{style="font-family:宋体"}[max]{lang="EN-US"}[（]{style="font-family:宋体"}[ROWMAX]{lang="EN-US"}[，]{style="font-family:宋体"}[COLMAX]{lang="EN-US"}[）]{style="font-family:宋体"}[\<]{lang="EN-US"}[索引号]{style="font-family:宋体"}[1]{lang="EN-US"}[对应的阈值时，才能认为这个]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号已经停止]{style="font-family:宋体"}

[[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x2079_20553_x238007279}[～]{style="font-family:宋体"}[4999]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[458]{lang="EN-US"}

[[取值越小，检测可靠性越高，但灵敏度会下降]{style="font-family:宋体"}]{#struct_0_x2079_20553_1755218907}

[[2]{lang="EN-US"}]{#struct_0_x2079_20553_1652345386}

[[当]{style="font-family:宋体"}[COLMAX\<ROWMAX]{lang="EN-US"}]{#struct_0_x2079_20553_2003951140}[时，输入信号要被识别为]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号，必须满足]{style="font-family:宋体"}[10]{lang="EN-US"}[×（]{style="font-family:宋体"}[COLMAX/ROWMAX]{lang="EN-US"}[）]{style="font-family:宋体"}[\>]{lang="EN-US"}[索引号]{style="font-family:宋体"}[2]{lang="EN-US"}[对应的阈值]{style="font-family:宋体"}

[[取值范围为]{style="font-family:宋体"}[-18]{lang="EN-US"}]{#struct_0_x2079_20553_327661380}[～]{style="font-family:宋体"}[-3]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[dB]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[-9]{lang="EN-US"}

[[取值越大，检测可靠性越高，但灵敏度会下降]{style="font-family:宋体"}]{#struct_0_x2079_20553_1770692962}

[[3]{lang="EN-US"}]{#struct_0_x2079_20553_1256463860}

[[当]{style="font-family:宋体"}[COLMAX\>=ROWMAX]{lang="EN-US"}]{#struct_0_x2079_20553_x275921222}[时，输入信号要被识别为]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号，必须满足]{style="font-family:宋体"}[10]{lang="EN-US"}[×（]{style="font-family:宋体"}[ROWMAX/COLMAX]{lang="EN-US"}[）]{style="font-family:宋体"}[\>]{lang="EN-US"}[索引号]{style="font-family:宋体"}[3]{lang="EN-US"}[对应的阈值]{style="font-family:宋体"}

[[取值范围为]{style="font-family:宋体"}[-18]{lang="EN-US"}]{#struct_0_x2079_20553_x1253994937}[～]{style="font-family:宋体"}[-3]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[dB]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[-9]{lang="EN-US"}

[[取值越小，检测可靠性越高，但灵敏度会下降]{style="font-family:宋体"}]{#struct_0_x2079_20553_327595844}

[[4]{lang="EN-US"}]{#struct_0_x2079_20553_1487177354}

[[行频率组里的能量次大者与]{style="font-family:宋体"}[ROWMAX]{lang="EN-US"}]{#struct_0_x2079_20553_188929321}[的比值的上限。输入信号要被识别为]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号，其对应的比值必须小于此门限]{style="font-family:宋体"}

[[取值范围为]{style="font-family:宋体"}[-18]{lang="EN-US"}]{#struct_0_x2079_20553_x1929247976}[～]{style="font-family:宋体"}[-3]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[dB]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[-9]{lang="EN-US"}

[[取值越小，检测可靠性越高，但灵敏度会下降]{style="font-family:宋体"}]{#struct_0_x2079_20553_1922997254}

[[5]{lang="EN-US"}]{#struct_0_x2079_20553_327530308}

[[列频率组里的能量次大者与]{style="font-family:宋体"}[COLMAX]{lang="EN-US"}]{#struct_0_x2079_20553_x480862009}[的比值的上限。输入信号要被识别为]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号，其对应的比值必须小于此门限]{style="font-family:宋体"}

[[取值范围为]{style="font-family:宋体"}[-18]{lang="EN-US"}]{#struct_0_x2079_20553_564223032}[～]{style="font-family:宋体"}[-3]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[dB]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[-9]{lang="EN-US"}

[[取值越小，检测可靠性越高，但灵敏度会下降]{style="font-family:宋体"}]{#struct_0_x2079_20553_1453798161}

[[6]{lang="EN-US"}]{#struct_0_x2079_20553_327464772}

[[（]{style="font-family:宋体"}[ROW2nd/ROWMAX]{lang="EN-US"}]{#struct_0_x2079_20553_x521899056}[）比值的上限。输入信号要被识别为]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号，必须满足（]{style="font-family:宋体"}[ROW2nd/ROWMAX]{lang="EN-US"}[）]{style="font-family:宋体"}[\<]{lang="EN-US"}[索引号]{style="font-family:宋体"}[6]{lang="EN-US"}[对应的阈值]{style="font-family:宋体"}

[[取值范围为]{style="font-family:宋体"}[-18]{lang="EN-US"}]{#struct_0_x2079_20553_x1770579125}[～]{style="font-family:宋体"}[-3]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[dB]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[-3]{lang="EN-US"}

[[取值越小，检测可靠性越高，但灵敏度会下降]{style="font-family:宋体"}]{#struct_0_x2079_20553_1617971540}

[[7]{lang="EN-US"}]{#struct_0_x2079_20553_391352166}

[[（]{style="font-family:宋体"}[COL2nd/COLMAX]{lang="EN-US"}]{#struct_0_x2079_20553_327399236}[）比值的上限。输入信号要被识别为]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号，其对应的比值必须小于此门限]{style="font-family:宋体"}

[[取值范围为]{style="font-family:宋体"}[-18]{lang="EN-US"}]{#struct_0_x2079_20553_x755886950}[～]{style="font-family:宋体"}[-3]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[dB]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[-12]{lang="EN-US"}

[[取值越小，检测可靠性越高，但灵敏度会下降]{style="font-family:宋体"}]{#struct_0_x2079_20553_2126264167}

[[8]{lang="EN-US"}]{#struct_0_x2079_20553_x225028949}

[[两个额外指定的频点上（由索引号]{style="font-family:宋体"}[9]{lang="EN-US"}]{#struct_0_x2079_20553_327333700}[、]{style="font-family:宋体"}[10]{lang="EN-US"}[指定）的能量最大者与]{style="font-family:宋体"}[max]{lang="EN-US"}[（]{style="font-family:宋体"}[ROWMAX]{lang="EN-US"}[，]{style="font-family:宋体"}[COLMAX]{lang="EN-US"}[）的比值的上限。输入信号要被识别为]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号，其对应的比值必须小于此门限]{style="font-family:宋体"}

[[取值范围为]{style="font-family:宋体"}[-18]{lang="EN-US"}]{#struct_0_x2079_20553_1583444779}[～]{style="font-family:宋体"}[-3]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[dB]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[-12]{lang="EN-US"}

[[取值越小，检测可靠性越高，但灵敏度会下降]{style="font-family:宋体"}]{#struct_0_x2079_20553_x1352185512}

[[9]{lang="EN-US"}]{#struct_0_x2079_20553_328316740}

[[DTMF]{lang="EN-US"}]{#struct_0_x2079_20553_x1023226718}[信号持续时间的下限。输入信号要被识别为]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号，输入信号持续的时间必须大于此门限]{style="font-family:宋体"}

[[取值范围为]{style="font-family:宋体"}[30]{lang="EN-US"}]{#struct_0_x2079_20553_776549147}[～]{style="font-family:宋体"}[150]{lang="EN-US"}[，单位为毫秒，缺省值为]{style="font-family:宋体"}[30]{lang="EN-US"}[毫秒]{style="font-family:宋体"}

[[取值越大，检测可靠性越高，但灵敏度会下降]{style="font-family:宋体"}]{#struct_0_x2079_20553_x1500271113}

[[10]{lang="EN-US"}]{#struct_0_x2079_20553_328251204}

[[额外指定的第一个检测频点的频率。这个频率需要选择为距离行、列频率组]{style="font-family:宋体"}[100Hz]{lang="EN-US"}]{#struct_0_x2079_20553_970032667}[之外的频率值]{style="font-family:宋体"}

[[取值范围为]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_x2079_20553_x1175114933}[～]{style="font-family:宋体"}[3400]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[Hz]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[300Hz]{lang="EN-US"}

[[-]{lang="EN-US"}]{#struct_0_x2079_20553_x231750179}

[[11]{lang="EN-US"}]{#struct_0_x2079_20553_327792453}

[[额外指定的第二个检测频点的频率。这个频率需要选择为距离行、列频率组]{style="font-family:宋体"}[100Hz]{lang="EN-US"}]{#struct_0_x2079_20553_579599821}[之外的频率值]{style="font-family:宋体"}

[[取值范围为]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_x2079_20553_x262561336}[～]{style="font-family:宋体"}[3400]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[Hz]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[3200Hz]{lang="EN-US"}

[[-]{lang="EN-US"}]{#struct_0_x2079_20553_327726917}

[[12]{lang="EN-US"}]{#struct_0_x2079_20553_219878093}

[[DTMF]{lang="EN-US"}]{#struct_0_x2079_20553_x238007282}[信号幅度的下限。输入信号要被识别为]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号，其平均幅度必须大于此值]{style="font-family:宋体"}

[[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x2079_20553_327661381}[～]{style="font-family:宋体"}[700]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[375]{lang="EN-US"}

[[取值越大，检测可靠性越高，但灵敏度会下降]{style="font-family:宋体"}]{#struct_0_x2079_20553_1770692961}

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1256529396}

[[通过配置]{style="font-family:宋体"}**[dtmf]{lang="EN-US"}**[ **threshold**]{lang="EN-US"}]{#struct_0_x2079_20553_1207260340}[命令的参数可以精确调整设备对]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号检测的灵敏度和可靠性。该命令主要供专业人员在]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号检测功能失效时使用，一般情况下使用缺省值即可。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1826151376}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x1427147657}[配置检测]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号敏感度阈值的索引号]{style="font-family:宋体"}[9]{lang="EN-US"}[，此索引号对应的阈值参数为]{style="font-family:宋体"}[40]{lang="EN-US"}[，即输入信号持续的时间大于]{style="font-family:宋体"}[40]{lang="EN-US"}[毫秒，此信号才能被识别为]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_327595845}

[\[Sysname\] subscriber-line 2/1/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/1/1\] dtmf threshold analog 9 40]{lang="EN-US"}

::: {#732202118 .myid}
[]{#struct_0_x2079_20553_1487177355}[]{#_Toc404794452}

**语音用户线 \-- 模拟语音用户线 \-- echo-canceler**

------------------------------------------------------------------------

[**[echo-canceler]{lang="EN-US"}**]{#struct_0_x2079_20553_188994857}[命令用来配置回波抵消的参数。]{style="font-family:宋体"}

[**[undo echo-canceler]{lang="EN-US"}**]{#struct_0_x2079_20553_1224593782}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1863291158}

[**[echo-canceler]{lang="EN-US"}**[ { **convergence-rate** *value* \| **max-amplitude** *value* \| **mix-proportion-ratio** *value* \| **talk-threshold** *value* }]{lang="EN-US"}]{#struct_0_x2079_20553_568182956}

[**[undo]{lang="EN-US"}**[ **echo-canceler** { **convergence-rate** \| **max-amplitude** \| **mix-proportion-ratio** \| **talk-threshold** }]{lang="EN-US"}]{#struct_0_x2079_20553_1635071174}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_605659270}

[[舒适噪声幅度的收敛速度的值为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x2079_20553_x993190511}[，舒适噪声的最大幅度的值为]{style="font-family:宋体"}[256]{lang="EN-US"}[，噪声的混合比例控制因子的值为]{style="font-family:宋体"}[100]{lang="EN-US"}[，双向通话判断阈值的值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_327530309}

[[语音视图]{style="font-family:宋体"}]{#struct_0_x2079_20553_x480862008}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_564288568}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1270033520}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_996892588}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1703953988}

[**[convergence-rate]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x2079_20553_x299406127}[：舒适噪声幅度的收敛速度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[511]{lang="EN-US"}[。取值越大，噪声的收敛速度越快。]{style="font-family:宋体"}

[**[max-amplitude]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x2079_20553_x115077283}[：舒适噪声的最大幅度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[2048]{lang="EN-US"}[。取值越大，噪声的最大幅度越大。取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[表示系统只做非线性处理而不加舒适噪声。]{style="font-family:宋体"}

[**[mix-proportion-ratio]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x2079_20553_673662540}[：噪声的混合比例控制因子，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[3000]{lang="EN-US"}[。取值越大，噪声与语音混合时噪声的比例越大。]{style="font-family:宋体"}

[**[talk-threshold]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x2079_20553_327464773}[：双向通话判断阈值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x521899057}

[[开启]{style="font-family:宋体"}**[echo-canceler]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_x1770644661}[命令后，设置的回波抵消参数才能生效。]{style="font-family:宋体"}

[**[convergence-rate]{lang="EN-US"}**]{#struct_0_x2079_20553_x1690653578}[和]{style="font-family:宋体"}**[max-amplitude]{lang="EN-US"}**[参数必须在开启]{style="font-family:宋体"}**[cng-on]{lang="EN-US"}**[命令下才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1775905259}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_572756403}[配置舒适噪声幅度的收敛速度为]{style="font-family:宋体"}[50]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_2074824917}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] echo-canceler convergence-rate 50]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x716965397}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cng-on]{lang="EN-US"}**]{#struct_0_x2079_20553_327399237}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[echo-canceler enable]{lang="EN-US"}**]{#struct_0_x2079_20553_x755886949}
:::

::: {#1211179221 .myid}
[]{#_Toc404794453}[]{#struct_0_x2079_20553_2125805414}

**语音用户线 \-- 模拟语音用户线 \-- echo-canceler delay**

------------------------------------------------------------------------

[**[echo-canceler delay]{lang="EN-US"}**]{#struct_0_x2079_20553_1450231943}[命令用来配置回波延时时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **echo-canceler delay**]{lang="EN-US"}]{#struct_0_x2079_20553_x2017611588}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1311477178}

[**[echo-canceler]{lang="EN-US"}**[ **delay** *milliseconds*]{lang="EN-US"}]{#struct_0_x2079_20553_x1196988151}

[**[undo]{lang="EN-US"}**[ **echo-canceler** **delay**]{lang="EN-US"}]{#struct_0_x2079_20553_x690201630}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_327333701}

[[回波延时时间为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x2079_20553_1583444780}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1351726751}

[[FXS/FXO/E&M]{lang="EN-US"}]{#struct_0_x2079_20553_x1527331502}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_467921491}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1110904144}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_328316741}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1023226717}

[*[milliseconds]{lang="EN-US"}*]{#struct_0_x2079_20553_x1145765154}[：回波延时时间，即用户从发出声音到听到回声的时间间隔，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1556515186}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_2074598766}[开启回波抵消功能，并配置回波延时时间为]{style="font-family:宋体"}[24]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x1502575661}

[\[Sysname\] subscriber-line 2/1/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/1/1\] echo-canceler enable]{lang="EN-US"}

[\[Sysname-subscriber-line2/1/1\] echo-canceler delay 24]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x257868230}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[echo-canceler enable]{lang="EN-US"}**]{#struct_0_x2079_20553_328251205}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[echo-canceler tail-length]{lang="EN-US"}**]{#struct_0_x2079_20553_970032668}
:::

::: {#2147218820 .myid}
[]{#_Toc404794454}[]{#struct_0_x2079_20553_x1175114926}[]{#_Toc316549753}[]{#_Toc295912529}[]{#_Toc263260034}

**语音用户线 \-- 模拟语音用户线 \-- echo-canceler enable**

------------------------------------------------------------------------

[**[echo-canceler enable]{lang="EN-US"}**]{#struct_0_x2079_20553_x991199530}[命令用来开启回波抵消功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **echo-canceler enable**]{lang="EN-US"}]{#struct_0_x2079_20553_x1786704850}[命令用来关闭回波抵消功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1341510554}

[**[echo-canceler]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_506413872}

[**[undo]{lang="EN-US"}**[ **echo-canceler** **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_1502584271}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1911485871}

[[回波抵消功能处于开启状态。]{style="font-family:宋体"}]{#struct_0_x2079_20553_327792450}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_579599818}

[[FXS/FXO/E&M]{lang="EN-US"}]{#struct_0_x2079_20553_1311416769}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x374084139}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_447140872}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1624669102}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_421219600}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_2028067063}[开启回波抵消功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_327726914}

[\[Sysname\] subscriber-line 2/1/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/1/1\] echo-canceler enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_219878092}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[echo-canceler delay]{lang="EN-US"}**]{#struct_0_x2079_20553_x238007281}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[echo-canceler tail-length]{lang="EN-US"}**]{#struct_0_x2079_20553_1755743190}
:::

::: {#-1198544127 .myid}
[]{#_Toc404794455}[]{#struct_0_x2079_20553_x1068579099}

**语音用户线 \-- 模拟语音用户线 \-- echo-canceler tail-length**

------------------------------------------------------------------------

[**[echo-canceler tail-length]{lang="EN-US"}**]{#struct_0_x2079_20553_x942720784}[命令用来配置回波抵消窗口大小。]{style="font-family:
宋体"}

[**[undo]{lang="EN-US"}**[ **echo-canceler tail-length**]{lang="EN-US"}]{#struct_0_x2079_20553_1403720057}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_216343438}

[**[echo-canceler]{lang="EN-US"}**[ **tail-length** *milliseconds*]{lang="EN-US"}]{#struct_0_x2079_20553_327661378}

[**[undo]{lang="EN-US"}**[ **echo-canceler** **tail-length**]{lang="EN-US"}]{#struct_0_x2079_20553_x1804230310}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x420548991}

[[回波抵消窗长]{style="font-family:宋体"}]{#struct_0_x2079_20553_60859930}[为]{style="font-family:宋体"}[128]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_196538940}

[[FXS/FXO/E&M]{lang="EN-US"}]{#struct_0_x2079_20553_x924376142}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1168971717}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x586365119}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1132563374}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_327595842}

[*[milliseconds]{lang="EN-US"}*]{#struct_0_x2079_20553_1487177352}[：回波抵消窗口大小。取值范围为]{style="font-family:宋体"}[32]{lang="EN-US"}[、]{style="font-family:宋体"}[48]{lang="EN-US"}[、]{style="font-family:宋体"}[64]{lang="EN-US"}[、]{style="font-family:宋体"}[80]{lang="EN-US"}[、]{style="font-family:宋体"}[96]{lang="EN-US"}[、]{style="font-family:宋体"}[112]{lang="EN-US"}[、]{style="font-family:宋体"}[128]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_188536105}

[[回波抵消窗口是指回波抵消能够消除回波的最大范围。增大回波抵消窗长，可以有效消除多路径回波。]{style="font-family:宋体"}]{#struct_0_x2079_20553_x2047087571}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_215116272}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_1171795703}[开启回波抵消功能，并配置回波抵消窗口大小为]{style="font-family:宋体"}[32]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_1632866935}

[\[Sysname\] subscriber-line 2/1/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/1/1\] echo-canceler enable]{lang="EN-US"}

[\[Sysname-subscriber-line2/1/1\] echo-canceler tail-length 32]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_327530306}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[echo-canceler delay]{lang="EN-US"}**]{#struct_0_x2079_20553_x480862023}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[echo-canceler enable]{lang="EN-US"}**]{#struct_0_x2079_20553_564878394}
:::

::: {#1944961636 .myid}
[]{#_Toc404794456}[]{#struct_0_x2079_20553_981778145}[]{#_Toc316549755}[]{#_Toc295912536}[]{#_Toc263260058}[]{#_Toc157310651}[]{#_Toc339548870}[]{#_Toc339548871}[]{#_Toc339548872}[]{#_Toc339548873}[]{#_Toc339548874}[]{#_Toc339548875}[]{#_Toc339548876}[]{#_Toc339548877}[]{#_Toc339548878}[]{#_Toc339548879}[]{#_Toc339548880}[]{#_Toc339548881}[]{#_Toc339548882}[]{#_Toc339548883}[]{#_Toc339548884}[]{#_Toc339548885}[]{#_Toc339548886}[]{#_Toc339548887}[]{#_Toc339548888}[]{#_Toc339548889}[]{#_Toc339548890}[]{#_Toc339548891}[]{#_Toc339548892}[]{#_Toc339548893}[]{#_Toc339548894}[]{#_Toc339548895}

**语音用户线 \-- 模拟语音用户线 \-- hookoff-mode delay bind**

------------------------------------------------------------------------

[**[hookoff-mode]{lang="EN-US"}**[ **delay** **bind**]{lang="EN-US"}]{#struct_0_x2079_20553_x631787978}[命令用来配置同该]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线绑定的]{style="font-family:宋体"}[FXS]{lang="EN-US"}[语音用户线。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **hookoff-mode** **delay** **bind**]{lang="EN-US"}]{#struct_0_x2079_20553_1638106341}[命令用来取消]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线同]{style="font-family:宋体"}[FXS]{lang="EN-US"}[语音用户线的绑定关系。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x2052117559}

[**[hookoff-mode]{lang="EN-US"}**[ **delay** **bind** *fxs-subscriber* \[ **ring-immediately** \]]{lang="EN-US"}]{#struct_0_x2079_20553_x1619103361}

[**[undo]{lang="EN-US"}**[ **hookoff-mode**]{lang="EN-US"}]{#struct_0_x2079_20553_x1032694146}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_327464770}

[[没有绑定]{style="font-family:宋体"}[FXS]{lang="EN-US"}]{#struct_0_x2079_20553_x521899058}[语音用户线。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1770972341}

[[FXO]{lang="EN-US"}]{#struct_0_x2079_20553_488863466}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_790246815}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1593266605}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1126418804}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1674769361}

[*[fxs-subscriber]{lang="EN-US"}*]{#struct_0_x2079_20553_327399234}[：同当前]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线绑定的]{style="font-family:宋体"}[FXS]{lang="EN-US"}[语音用户线号。]{style="font-family:宋体"}

[**[ring-immediately]{lang="EN-US"}**]{#struct_0_x2079_20553_x755886952}[：采用立即振铃方式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_2126395239}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hookoff-mode delay bind]{lang="EN-US"}**]{#struct_0_x2079_20553_528206060}[命令所绑定的]{lang="EN-US" style="font-family:宋体"}[FXS]{lang="EN-US"}[语音用户线必须与]{lang="EN-US" style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线在同一台设备上。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{style="font-family:宋体"}]{#struct_0_x2079_20553_1744004718}**[ring-immediately]{lang="EN-US"}**[参数可提高]{style="font-family:宋体"}[FXO]{lang="EN-US"}[与绑定]{style="font-family:宋体"}[FXS]{lang="EN-US"}[语音用户线的振铃同步速度，但对于使用来电显示的被叫话机，在收到呼叫后的第二声振铃后才能显示主叫号码。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x816615062}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_1660498098}[配置]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线的摘机方式为延时摘机，并同]{style="font-family:宋体"}[FXS]{lang="EN-US"}[语音用户线]{style="font-family:宋体"}[2/1/1]{lang="EN-US"}[绑定。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_2100342392}

[\[Sysname\] subscriber-line 2/2/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/2/1\] hookoff-mode delay bind 2/1/1]{lang="EN-US"}
:::

::: {#-1901890465 .myid}
[]{#_Toc404794457}[]{#struct_0_x2079_20553_327333698}[]{#_Toc316549754}[]{#_Toc295912535}[]{#_Toc263260057}[]{#_Toc150660459}[]{#_Toc135295486}[]{#_Toc130097135}[]{#_Toc129160855}

**语音用户线 \-- 模拟语音用户线 \-- hookoff-mode**

------------------------------------------------------------------------

[**[hookoff-mode]{lang="EN-US"}**]{#struct_0_x2079_20553_444327886}[命令用来配置]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线的摘机方式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **hookoff-mode**]{lang="EN-US"}]{#struct_0_x2079_20553_x1513565197}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1416896445}

[**[hookoff-mode]{lang="EN-US"}**[ { **delay** \| **immediate** }]{lang="EN-US"}]{#struct_0_x2079_20553_x1110119081}

[**[undo]{lang="EN-US"}**[ **hookoff-mode**]{lang="EN-US"}]{#struct_0_x2079_20553_1262768244}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1245860201}

[[FXO]{lang="EN-US"}]{#struct_0_x2079_20553_1216948375}[语音用户线使用立即摘机方式摘机。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_192391385}

[[FXO]{lang="EN-US"}]{#struct_0_x2079_20553_328316738}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x213922662}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_891283910}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1283280883}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1371240364}

[**[delay]{lang="EN-US"}**]{#struct_0_x2079_20553_x1604897461}[：]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线使用延时摘机方式摘机。]{style="font-family:宋体"}

[**[immediate]{lang="EN-US"}**]{#struct_0_x2079_20553_362819127}[：]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线使用立即摘机方式摘机。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1821270062}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x1000709185}[配置]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线摘机模式为延时摘机。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_328251202}

[\[Sysname\] subscriber-line 2/2/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/2/1\] hookoff-mode delay]{lang="EN-US"}
:::

::: {#471155723 .myid}
[]{#_Toc404794458}[]{#struct_0_x2079_20553_970032673}[]{#_Toc316549756}[]{#_Toc295912537}[]{#_Toc263260059}[]{#_Toc135295487}[]{#_Toc130097136}[]{#_Toc129160856}

**语音用户线 \-- 模拟语音用户线 \-- hookoff-time**

------------------------------------------------------------------------

[**[hookoff-time]{lang="EN-US"}**]{#struct_0_x2079_20553_1163537223}[命令用来配置强制挂机功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **hookoff-time**]{lang="EN-US"}]{#struct_0_x2079_20553_987333476}[命令用来关闭强制挂机功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1829053852}

[**[hookoff-time]{lang="EN-US"}**[ *time*]{lang="EN-US"}]{#struct_0_x2079_20553_x1317957196}

[**[undo]{lang="EN-US"}**[ **hookoff-time**]{lang="EN-US"}]{#struct_0_x2079_20553_x122315241}

[[【缺省情况】]{style="font-family:
黑体"}]{#struct_0_x2079_20553_9413418}

[[强制挂机功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x2079_20553_327792451}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_579599819}

[[FXO]{lang="EN-US"}]{#struct_0_x2079_20553_1311416768}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x374018603}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_114121923}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1368695416}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1399108062}

[*[time]{lang="EN-US"}*]{#struct_0_x2079_20553_494580664}[：强制挂机的时间，此时间从]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线摘机开始计算，取值范围为]{style="font-family:宋体"}[60]{lang="EN-US"}[～]{style="font-family:宋体"}[36000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_327726915}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[某些国家的]{style="font-family:宋体"}]{#struct_0_x2079_20553_219878091}[PBX]{lang="EN-US"}[交换机不播放忙音或放忙音持续时间较短会造成设备无法检测到忙音]{style="font-family:宋体"}[。如果传输链路上存在杂音，可能导致配置的静音检测自动挂机功能也无法解决]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户无法挂机的问题，这种情况下可以考虑使用强制挂机功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置强制挂机功能后，在此时间超时后，即使用户正在通话中，设备也会自动拆线。]{style="font-family:宋体"}]{#struct_0_x2079_20553_x238007284}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令对单板上的所有]{style="font-family:宋体"}]{#struct_0_x2079_20553_1756070870}[FXO]{lang="EN-US"}[语音用户线生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1187371753}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_1678604346}[配置强制挂机的时间为]{style="font-family:宋体"}[500]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_871565100}

[\[Sysname\] subscriber-line 2/2/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/2/1\] hookoff-time 500]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1302746640}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[silence-detect threshold]{lang="EN-US"}**]{#struct_0_x2079_20553_327661379}
:::

::: {#48154999 .myid}
[]{#_Toc404794459}[]{#struct_0_x2079_20553_x1804230311}

**语音用户线 \-- 模拟语音用户线 \-- impedance**

------------------------------------------------------------------------

[**[impedance]{lang="PT-BR"}**]{#struct_0_x2079_20553_x1986632932}[命令用来配置电气阻抗]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo]{lang="PT-BR"}**]{#struct_0_x2079_20553_x1958412744}[ **impedance**]{lang="PT-BR"}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_378771915}

[**[impedance]{lang="PT-BR"}**]{#struct_0_x2079_20553_x1308148008}[ { *country-name* \| **r550** \| **r600** \| **r650** \| **r700** \| **r750** \| **r800** \| **r850** \| **r900** \| **r950** }]{lang="PT-BR"}

[**[undo impedance]{lang="PT-BR"}**]{#struct_0_x2079_20553_958937940}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1019635039}

[[电气阻抗]{style="font-family:宋体"}]{#struct_0_x2079_20553_x1761123663}[是中国的]{style="font-family:宋体"}[阻抗匹配值]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_327595843}

[[FXS/FXO]{lang="PT-BR"}]{#struct_0_x2079_20553_1487177353}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_188601641}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_945381543}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_964361371}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_327464771}

[*[country-name]{lang="PT-BR"}*]{#struct_0_x2079_20553_x521899059}[：]{style="font-family:宋体"}[国家名称]{style="font-family:宋体"}[，]{style="font-family:宋体"}[不同的国家有自己的电气阻抗值，]{style="font-family:宋体"}[配置国家名称可以直接]{style="font-family:宋体"}[索引相应国家的电气阻抗值。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[australia]{lang="PT-BR"}**]{#struct_0_x2079_20553_x1771037877}[：]{lang="EN-US" style="font-family:宋体"}[澳大利亚。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[austria]{lang="PT-BR"}**]{#struct_0_x2079_20553_x316920044}[：]{lang="EN-US" style="font-family:宋体"}[奥地利。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[belgium-long]{lang="PT-BR"}**]{#struct_0_x2079_20553_1204736766}[：]{lang="EN-US" style="font-family:宋体"}[比利时]{lang="EN-US" style="font-family:宋体"}[（]{lang="EN-US" style="font-family:宋体"}[长]{lang="EN-US" style="font-family:
宋体"}[）]{lang="EN-US" style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[belgium-short]{lang="PT-BR"}**]{#struct_0_x2079_20553_x561640251}[：]{lang="EN-US" style="font-family:宋体"}[比利时]{lang="EN-US" style="font-family:宋体"}[（]{lang="EN-US" style="font-family:宋体"}[短]{lang="EN-US" style="font-family:
宋体"}[）]{lang="EN-US" style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[brazil]{lang="PT-BR"}**]{#struct_0_x2079_20553_x712629878}[：]{lang="EN-US" style="font-family:宋体"}[巴西。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[china]{lang="PT-BR"}**]{#struct_0_x2079_20553_777454366}[：]{lang="EN-US" style="font-family:宋体"}[中华人民共和国。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[czech-republic]{lang="PT-BR"}**]{#struct_0_x2079_20553_327399235}[：]{lang="EN-US" style="font-family:宋体"}[捷克斯洛伐克。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[denmark]{lang="PT-BR"}**]{#struct_0_x2079_20553_x755886951}[：]{lang="EN-US" style="font-family:宋体"}[丹麦。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[etsi-harmanized]{lang="PT-BR"}**]{#struct_0_x2079_20553_2126329703}[：]{lang="EN-US" style="font-family:宋体"}[欧洲电信标准化协会。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[finland]{lang="PT-BR"}**]{#struct_0_x2079_20553_2046115887}[：]{lang="EN-US" style="font-family:宋体"}[芬兰。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[france]{lang="PT-BR"}**]{#struct_0_x2079_20553_x1434920661}[：]{lang="EN-US" style="font-family:宋体"}[法国。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[german-swiss]{lang="PT-BR"}**]{#struct_0_x2079_20553_339818356}[：]{lang="EN-US" style="font-family:宋体"}[德国及瑞士。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[greece]{lang="PT-BR"}**]{#struct_0_x2079_20553_2023486017}[：]{lang="EN-US" style="font-family:宋体"}[希腊。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[hungary]{lang="PT-BR"}**]{#struct_0_x2079_20553_x956023122}[：]{lang="EN-US" style="font-family:宋体"}[匈牙利。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[india]{lang="PT-BR"}**]{#struct_0_x2079_20553_x265710634}[：]{lang="EN-US" style="font-family:宋体"}[印度。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[italy]{lang="PT-BR"}**]{#struct_0_x2079_20553_327333699}[：]{lang="EN-US" style="font-family:宋体"}[意大利。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[japan]{lang="PT-BR"}**]{#struct_0_x2079_20553_444327887}[：]{lang="EN-US" style="font-family:宋体"}[日本。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[korea]{lang="PT-BR"}**]{#struct_0_x2079_20553_x1513565196}[：]{lang="EN-US" style="font-family:宋体"}[韩国。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[mexico]{lang="PT-BR"}**]{#struct_0_x2079_20553_x1311986910}[：]{lang="EN-US" style="font-family:宋体"}[墨西哥。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[netherlands]{lang="PT-BR"}**]{#struct_0_x2079_20553_x1829720238}[：]{lang="EN-US" style="font-family:宋体"}[荷兰。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[new-zealand]{lang="PT-BR"}**]{#struct_0_x2079_20553_1635474874}[：新西兰。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[norway]{lang="PT-BR"}**]{#struct_0_x2079_20553_x1849202480}[：]{lang="EN-US" style="font-family:宋体"}[挪威。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[portugal]{lang="PT-BR"}**]{#struct_0_x2079_20553_x1246028388}[：]{lang="EN-US" style="font-family:宋体"}[葡萄牙。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[slovakia]{lang="PT-BR"}**]{#struct_0_x2079_20553_x182118234}[：]{lang="EN-US" style="font-family:宋体"}[斯洛伐克。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[spain]{lang="PT-BR"}**]{#struct_0_x2079_20553_2086772622}[：]{lang="EN-US" style="font-family:宋体"}[西班牙。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[sweden]{lang="PT-BR"}**]{#struct_0_x2079_20553_328316739}[：]{lang="EN-US" style="font-family:宋体"}[瑞典。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[u.k]{lang="PT-BR"}**]{#struct_0_x2079_20553_x213922661}[．：]{lang="EN-US" style="font-family:宋体"}[英国。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[us-loaded-line]{lang="PT-BR"}**]{#struct_0_x2079_20553_891349446}[：]{lang="EN-US" style="font-family:宋体"}[美国标准]{lang="EN-US" style="font-family:
宋体"}[1]{lang="PT-BR"}[。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[us-non-loaded]{lang="PT-BR"}**]{#struct_0_x2079_20553_909570224}[：]{lang="EN-US" style="font-family:宋体"}[美国标准]{lang="EN-US" style="font-family:宋体"}[2]{lang="PT-BR"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[us-special-service]{lang="PT-BR"}**]{#struct_0_x2079_20553_x446264030}[：]{lang="EN-US" style="font-family:宋体"}[美国标准]{lang="EN-US" style="font-family:
宋体"}[3]{lang="PT-BR"}[。]{lang="EN-US" style="font-family:
宋体"}

[**[r550]{lang="PT-BR"}**]{#struct_0_x2079_20553_1381449277}[：]{style="font-family:宋体"}[550]{lang="PT-BR"}[欧姆实阻抗。]{style="font-family:宋体"}

[**[r600]{lang="PT-BR"}**]{#struct_0_x2079_20553_908871342}[：]{style="font-family:宋体"}[600]{lang="PT-BR"}[欧姆实阻抗。]{style="font-family:宋体"}

[**[r650]{lang="PT-BR"}**]{#struct_0_x2079_20553_x84336512}[：]{style="font-family:宋体"}[650]{lang="PT-BR"}[欧姆实阻抗。]{style="font-family:宋体"}

[**[r700]{lang="PT-BR"}**]{#struct_0_x2079_20553_328251203}[：]{style="font-family:宋体"}[700]{lang="PT-BR"}[欧姆实阻抗。]{style="font-family:宋体"}

[**[r750]{lang="PT-BR"}**]{#struct_0_x2079_20553_970032674}[：]{style="font-family:宋体"}[750]{lang="PT-BR"}[欧姆实阻抗。]{style="font-family:宋体"}

[**[r800]{lang="PT-BR"}**]{#struct_0_x2079_20553_1163537230}[：]{style="font-family:宋体"}[800]{lang="PT-BR"}[欧姆实阻抗。]{style="font-family:宋体"}

[**[r850]{lang="PT-BR"}**]{#struct_0_x2079_20553_987530085}[：]{style="font-family:宋体"}[850]{lang="PT-BR"}[欧姆实阻抗。]{style="font-family:宋体"}

[**[r900]{lang="PT-BR"}**]{#struct_0_x2079_20553_200364847}[：]{style="font-family:宋体"}[900]{lang="PT-BR"}[欧姆实阻抗。]{style="font-family:宋体"}

[**[r950]{lang="PT-BR"}**]{#struct_0_x2079_20553_1615445126}[：]{style="font-family:宋体"}[950]{lang="PT-BR"}[欧姆实阻抗。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1083022733}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[电气阻抗的配置必须符合国家的要求。在配置电气阻抗值时，用户可以通过输入国家名称]{style="font-family:宋体"}]{#struct_0_x2079_20553_x425381774}[直接]{style="font-family:宋体"}[索引相应国家的电气阻抗值。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在呼叫两端设备上需要配置相同的电气阻抗值。]{style="font-family:宋体"}]{#struct_0_x2079_20553_1719694745}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1893876395}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x997900062}[配置电气阻抗为]{style="font-family:宋体"}[600]{lang="EN-US"}[欧姆实阻抗。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_890644100}

[\[Sysnamee\] subscriber-line 2/2/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/2/1\] impedance r600 ]{lang="EN-US"}
:::

::: {#-501408057 .myid}
[]{#_Toc404794460}[]{#struct_0_x2079_20553_x520411919}

**语音用户线 \-- 模拟语音用户线 \-- monitor enable**

------------------------------------------------------------------------

[**[monitor enable]{lang="EN-US"}**]{#struct_0_x2079_20553_x2085718541}[命令用来开启所有]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线的在线检测功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **monitor enable**]{lang="EN-US"}]{#struct_0_x2079_20553_x1246281265}[命令用来关闭所有]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线的在线检测功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1662297690}

[**[monitor enable]{lang="EN-US"}**]{#struct_0_x2079_20553_x30112701}

[**[undo monitor enable]{lang="EN-US"}**]{#struct_0_x2079_20553_x524726607}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1563158460}

[[在线检测功能处于开启状态。]{style="font-family:宋体"}]{#struct_0_x2079_20553_2041657265}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1045672022}

[[语音视图]{style="font-family:宋体"}]{#struct_0_x2079_20553_x968467876}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x552578682}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x53242039}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1324096869}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1735394538}

[[在线检测功能处于开启状态时，设备会检测]{style="font-family:宋体"}[FXO]{lang="EN-US"}]{#struct_0_x2079_20553_1807701755}[语音用户线的物理状态。关闭该功能，设备不会检测]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线的物理状态，]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线的物理状态一直为]{style="font-family:宋体"}[Up]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_286157135}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_651934732}[关闭所有]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线的在线检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x1068213351}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] undo monitor enable]{lang="EN-US"}
:::

::: {#-58070653 .myid}
[]{#_Toc404794461}[]{#struct_0_x2079_20553_x1028017750}

**语音用户线 \-- 模拟语音用户线 \-- nlp-on**

------------------------------------------------------------------------

[**[nlp-on]{lang="EN-US"}**]{#struct_0_x2079_20553_x1586246193}[命令用来开启回波抵消的非线性功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **nlp-on**]{lang="EN-US"}]{#struct_0_x2079_20553_186724436}[命令用来关闭回波抵消的非线性功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_289482364}

[**[nlp-on]{lang="EN-US"}**]{#struct_0_x2079_20553_833219927}

[**[undo]{lang="EN-US"}**[ **nlp-on**]{lang="EN-US"}]{#struct_0_x2079_20553_1893810859}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x957392984}

[[回波抵消的非线性功能处于开启状态。]{style="font-family:宋体"}]{#struct_0_x2079_20553_114362618}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1798993926}

[[FXS/FXO/E&M]{lang="EN-US"}]{#struct_0_x2079_20553_1750113278}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x429013211}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1049255492}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_703391294}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1893745323}

[[只有开启]{style="font-family:宋体"}**[echo-canceler]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_1728951839}[命令后，非线性功能才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x114579628}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x916192583}[关闭回波抵消的非线性功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x487528228}

[\[Sysname\] subscriber-line 2/2/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/2/1\] undo nlp-on]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1726701583}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[echo-canceler enable]{lang="EN-US"}**]{#struct_0_x2079_20553_1514156390}
:::

::: {#228681441 .myid}
[]{#_Toc404794462}[]{#struct_0_x2079_20553_x374739406}

**语音用户线 \-- 模拟语音用户线 \-- open-trunk**

------------------------------------------------------------------------

[**[open-trunk]{lang="EN-US"}**]{#struct_0_x2079_20553_1893679787}[命令用来开启]{style="font-family:宋体"}[E&M]{lang="EN-US"}[无信令模式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **open-trunk**]{lang="EN-US"}]{#struct_0_x2079_20553_x186302720}[命令用来关闭]{style="font-family:宋体"}[E&M]{lang="EN-US"}[无信令模式。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_630217557}

[**[open-trunk]{lang="EN-US"}**[ { **caller** \[ **monitor** *interval* \] \| **called** }]{lang="EN-US"}]{#struct_0_x2079_20553_1702317324}

[**[undo]{lang="EN-US"}**[ **open-trunk**]{lang="EN-US"}]{#struct_0_x2079_20553_1395950043}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x13084790}

[[E&M]{lang="EN-US"}]{#struct_0_x2079_20553_1467188550}[无信令模式处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_721268442}

[[E&M]{lang="EN-US"}]{#struct_0_x2079_20553_x1870938905}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1893614251}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1780274478}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1862847865}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x726375233}

[**[caller]{lang="EN-US"}**]{#struct_0_x2079_20553_106013506}[：开启主叫侧设备的]{style="font-family:宋体"}[E&M]{lang="EN-US"}[无信令模式。]{style="font-family:宋体"}

[**[monitor]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_x2079_20553_x638215498}[：]{style="font-family:宋体"}[监控时间，取值范围为]{style="font-family:宋体"}[60]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[，单位为秒。如果被叫在此时间内没有摘机应答，主叫侧会在监控时间超时后，重新向被叫发起呼叫。配置]{style="font-family:宋体"}**[monitor]{lang="EN-US"}**[参数后，监控定时器就开始计时。]{style="font-family:宋体"}

[**[called]{lang="EN-US"}**]{#struct_0_x2079_20553_x76309790}[：开启被叫侧设备的]{style="font-family:宋体"}[E&M]{lang="EN-US"}[无信令模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1382633628}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置本命令之前，需要在主被叫侧设备上将]{style="font-family:宋体"}]{#struct_0_x2079_20553_1893548715}[E&M]{lang="EN-US"}[信令设置在立即启动模式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在主叫侧设备上配置]{lang="EN-US" style="font-family:宋体"}**[open-trunk caller ]{lang="EN-US"}**[\[ **monitor** *interval* \]]{lang="EN-US"}]{#struct_0_x2079_20553_x1754418381}[命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在被叫侧设备上配置]{lang="EN-US" style="font-family:宋体"}**[open-trunk called]{lang="EN-US"}**]{#struct_0_x2079_20553_x962405556}[命令。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E&M]{lang="EN-US"}]{#struct_0_x2079_20553_1494640718}[无信令模式需要结合专线自动振铃功能使用时，在主叫侧设备上需要配置]{style="font-family:宋体"}**[private-line]{lang="EN-US"}**[命令。关于专线自动振铃功能请参见"语音配置指导"中的"拨号策略"。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1996970090}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_106583951}[开启主叫侧设备的]{style="font-family:宋体"}[E&M]{lang="EN-US"}[无信令模式，监控时间为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_720511622}

[\[Sysname\] subscriber-line 2/3/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/3/1\] open-trunk caller monitor 120]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x2119437443}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[private-line]{lang="EN-US"}**]{#struct_0_x2079_20553_1893483179}[（语音命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[拨号策略）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[signal]{lang="EN-US"}**]{#struct_0_x2079_20553_x1353647531}
:::

::: {#-334263399 .myid}
[]{#_Toc404794463}[]{#struct_0_x2079_20553_x539585124}[]{#_Toc318291925}[]{#_Toc318291281}[]{#_Toc234202113}

**语音用户线 \-- 模拟语音用户线 \-- passthrough**

------------------------------------------------------------------------

[**[passthrough]{lang="EN-US"}**]{#struct_0_x2079_20553_x955671698}[命令用来开启]{style="font-family:宋体"}[E&M]{lang="EN-US"}[透传模拟控制信号。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **passthrough**]{lang="EN-US"}]{#struct_0_x2079_20553_216497719}[命令用来关闭]{style="font-family:宋体"}[E&M]{lang="EN-US"}[透传模拟控制信号。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1110280650}

[**[passthrough]{lang="PT-BR"}**]{#struct_0_x2079_20553_x1322654176}

[**[undo]{lang="PT-BR"}**]{#struct_0_x2079_20553_175283536}[ **passthrough**]{lang="PT-BR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1775492359}

[[E&M]{lang="EN-US"}]{#struct_0_x2079_20553_1893417643}[透传模拟控制信号功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x612184896}

[[E&M]{lang="EN-US"}]{#struct_0_x2079_20553_1370596476}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x2034175999}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_135179534}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x2113086035}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x588609324}

[[在主叫侧和被叫侧设备上都需要配置该命令。]{style="font-family:宋体"}]{#struct_0_x2079_20553_x1346300692}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_627089246}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_1894400683}[开启]{style="font-family:宋体"}[E&M]{lang="EN-US"}[透传模拟控制信号。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_430921777}

[\[Sysname\] subscriber-line 2/3/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/3/1\] passthrough]{lang="EN-US"}
:::

::::: {#-1875552419 .myid}
[]{#_Toc404794464}[]{#struct_0_x2079_20553_x1502727793}

**语音用户线 \-- 模拟语音用户线 \-- pcm-passthrough**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](语音用户线命令.files/image001.png){#图片 1 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2079_20553_x1215229492}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2079_20553_1084008026}
:::

[ ]{lang="EN-US"}

[**[pcm-passthrough]{lang="EN-US"}**]{#struct_0_x2079_20553_63356148}[命令用来开启]{style="font-family:宋体"}[PCM]{lang="EN-US"}[透传功能。]{style="font-family:宋体"}

[**[undo pcm-passthrough]{lang="EN-US"}**]{#struct_0_x2079_20553_1822568967}[命令用来关闭]{style="font-family:宋体"}[PCM]{lang="EN-US"}[透传功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1089918991}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2079_20553_x1268264580}

[**[pcm-passthrough subslot ]{lang="EN-US"}**]{#struct_0_x2079_20553_2112098925}*[subslot-number]{lang="EN-US"}*

[**[undo pcm-passthrough subslot ]{lang="EN-US"}**]{#struct_0_x2079_20553_1958583678}*[subslot-number]{lang="EN-US"}*

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2079_20553_1154008728}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[pcm-passthrough slot ]{lang="EN-US"}**]{#struct_0_x2079_20553_x698627605}*[slot-number]{lang="EN-US"}***[ subslot ]{lang="EN-US"}***[subslot-number]{lang="EN-US"}*

[**[undo pcm-passthrough slot ]{lang="EN-US"}**]{#struct_0_x2079_20553_1576835841}*[slot-number]{lang="EN-US"}***[ subslot ]{lang="EN-US"}***[subslot-number]{lang="EN-US"}*

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2079_20553_1985670449}[模式：]{style="font-family:宋体"}

[**[pcm-passthrough chassis ]{lang="EN-US"}**]{#struct_0_x2079_20553_82933548}*[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}***[ subslot ]{lang="EN-US"}***[subslot-number]{lang="EN-US"}*

[**[undo pcm-passthrough chassis ]{lang="EN-US"}**]{#struct_0_x2079_20553_458824742}*[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}***[ subslot ]{lang="EN-US"}***[subslot-number]{lang="EN-US"}*

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1752481919}

[[PCM]{lang="EN-US"}]{#struct_0_x2079_20553_x2079084558}[透传功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1986941296}

[[语音视图]{style="font-family:宋体"}]{#struct_0_x2079_20553_383228888}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_86749495}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_50138279}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_268593527}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x743212906}

[**[subslot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x2079_20553_x1438374027}*[subslot-number]{lang="EN-US"}*[：开启指定子卡的]{style="font-family:宋体"}[PCM]{lang="EN-US"}[透传功能。]{style="font-family:宋体"}*[subslot-number]{lang="EN-US"}*[表示子卡所在的子槽位号。（集中式设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x2079_20553_x1196276031}*[slot-number]{lang="EN-US"}***[ subslot ]{lang="EN-US"}***[subslot-number]{lang="EN-US"}*[：开启指定单板上的指定子卡的]{style="font-family:宋体"}[PCM]{lang="EN-US"}[透传功能。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号，]{style="font-family:宋体"}*[subslot-number]{lang="EN-US"}*[表示子卡所在的子槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x2079_20553_x943103600}*[slot-number]{lang="EN-US"}***[ subslot ]{lang="EN-US"}***[subslot-number]{lang="EN-US"}*[：开启指定成员设备上的指定子卡的]{style="font-family:宋体"}[PCM]{lang="EN-US"}[透传功能。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[subslot-number]{lang="EN-US"}*[表示子卡所在的子槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_x2079_20553_x2119197648}*[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}***[ subslot ]{lang="EN-US"}***[subslot-number]{lang="EN-US"}*[：开启指定成员设备指定单板上指定子槽位号的]{style="font-family:宋体"}[PCM]{lang="EN-US"}[透传功能。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示指定单板所在的槽位号，]{style="font-family:宋体"}*[subslot-number]{lang="EN-US"}*[表示子卡所在的子槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1774936402}

[[开启]{style="font-family:宋体"}[PCM]{lang="EN-US"}]{#struct_0_x2079_20553_x243339391}[透传功能后，转换后的]{style="font-family:宋体"}[PCM]{lang="EN-US"}[信号将直接传输，不支持编解码、回波抵消功能，不再进行其他信号处理工作，从而降低了传输时延。建议对于信号传输时延较为敏感的系统（例如：空管系统）开启该功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_165423721}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x2000095978}[在语音视图下开启槽位]{style="font-family:宋体"}[3]{lang="EN-US"}[上的]{style="font-family:宋体"}[EM]{lang="EN-US"}[卡的]{style="font-family:宋体"}[PCM]{lang="EN-US"}[透传功能。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_822871035}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] pcm-passthrough subslot 3]{lang="EN-US"}

[This command will reboot the card in the specified subslot. Continue? \[Y/N\]: Y]{lang="EN-US"}
:::::

::: {#-542505514 .myid}
[]{#_Toc404794465}[]{#struct_0_x2079_20553_x1842123519}

**语音用户线 \-- 模拟语音用户线 \-- plc-mode**

------------------------------------------------------------------------

[**[plc-mode]{lang="EN-US"}**]{#struct_0_x2079_20553_102036267}[命令用来配置丢包补偿方式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **plc-mode**]{lang="EN-US"}]{#struct_0_x2079_20553_x828105416}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_707830533}

[**[plc-mode]{lang="EN-US"}**[ { **general** \| **specific** }]{lang="EN-US"}]{#struct_0_x2079_20553_x1432127248}

[**[undo]{lang="EN-US"}**[ **plc-mode**]{lang="EN-US"}]{#struct_0_x2079_20553_x986755011}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1894335147}

[[使用语音网关特有方式补偿丢失的语音包。]{style="font-family:宋体"}]{#struct_0_x2079_20553_1986377373}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1120130405}

[[FXS/FXO]{lang="EN-US"}]{#struct_0_x2079_20553_x1804061759}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1217260605}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1478207891}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1112188353}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x418600477}

[**[general]{lang="EN-US"}**]{#struct_0_x2079_20553_1893876396}[：使用通用的丢帧补偿算法重构丢失的语音包，适用于出现零散丢包的情况。]{style="font-family:宋体"}

[**[specific]{lang="EN-US"}**]{#struct_0_x2079_20553_x998096670}[：使用语音网关特有方式补偿丢失的语音包，适用于出现连续丢包的情况。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_739970676}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x710662254}[配置使用通用的丢帧补偿算法重构丢失的语音包。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x1444157011}

[\[Sysname\] subscriber-line 2/1/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/1/1\] plc-mode general]{lang="EN-US"}
:::

::: {#-1725270079 .myid}
[]{#_Toc404794466}[]{#struct_0_x2079_20553_x41795735}[]{#_Toc316549759}[]{#_Toc295912542}[]{#_Toc263260064}[]{#_Toc135295497}[]{#_Toc130097146}[]{#_Toc129160866}[]{#_Toc47776207}

**语音用户线 \-- 模拟语音用户线 \-- receive gain**

------------------------------------------------------------------------

[**[receive]{lang="EN-US"}**[ **gain**]{lang="EN-US"}]{#struct_0_x2079_20553_2075936666}[命令用来配置输入方向的增益值。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **receive** **gain**]{lang="EN-US"}]{#struct_0_x2079_20553_1565319897}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1893810860}

[**[receive]{lang="EN-US"}**[ **gain** *value*]{lang="EN-US"}]{#struct_0_x2079_20553_x957982805}

[**[undo]{lang="EN-US"}**[ **receive** **gain**]{lang="EN-US"}]{#struct_0_x2079_20553_x1843918408}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_477583681}

[[输入方向的增益值为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x2079_20553_x1752442308}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_339592746}

[[FXS/FXO/E&M]{lang="EN-US"}]{#struct_0_x2079_20553_x824065115}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1361010014}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1893745324}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1728886303}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_746670497}

[*[value]{lang="EN-US"}*]{#struct_0_x2079_20553_x2037773336}[：输入方向的增益值，取值范围为]{style="font-family:宋体"}[-14.0]{lang="EN-US"}[～]{style="font-family:宋体"}[13.9]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[dB]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_2050595084}

[[当从线路上接收到的语音信号衰减较大时，可以使用该命令适当增大输入增益来放大信号。]{style="font-family:宋体"}]{#struct_0_x2079_20553_x585248348}

[[调整增益大小可能会导致语音呼叫失败。建议不要随意调整增益大小，如果确实有需要，请在技术人员指导下进行。]{style="font-family:宋体"}]{#struct_0_x2079_20553_528654187}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x437855375}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x1696031731}[配置输入方向的增益值为]{style="font-family:宋体"}[3.5dB]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_1893679788}

[\[Sysname\] subscriber-line 2/1/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/1/1\] receive gain 3.5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x186499328}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[transmit]{lang="EN-US"}**[ **gain**]{lang="EN-US"}]{#struct_0_x2079_20553_x917105489}
:::

::::: {#1575792361 .myid}
[]{#_Toc404794467}[]{#struct_0_x2079_20553_1464152035}[]{#_Toc316549760}[]{#_Toc295912546}[]{#_Toc263260068}

**语音用户线 \-- 模拟语音用户线 \-- ring-detect debounce**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](语音用户线命令.files/image002.jpg){#图片 13 border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x2079_20553_26885346}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[该命令的支持情况与实际使用的板卡有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2079_20553_x121423421}
:::

[ ]{lang="EN-US"}

[**[ring-detect]{lang="EN-US"}**[ **debounce**]{lang="EN-US"}]{#struct_0_x2079_20553_x1417126101}[命令用来配置检测振铃的防抖动时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ring-detect** **debounce**]{lang="EN-US"}]{#struct_0_x2079_20553_377698194}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1893614252}

[**[ring-detect]{lang="EN-US"}**[ **debounce** *value*]{lang="EN-US"}]{#struct_0_x2079_20553_x1780208942}

[**[undo]{lang="EN-US"}**[ **ring-detect** **debounce**]{lang="EN-US"}]{#struct_0_x2079_20553_912702361}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x999313608}

[[检测振铃的防抖动时间为]{style="font-family:宋体"}[10]{lang="EN-US"}]{#struct_0_x2079_20553_1512359923}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1029950078}

[[FXO]{lang="EN-US"}]{#struct_0_x2079_20553_1630292167}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x763101548}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_176788823}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1893548716}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1754483917}

[]{#struct_0_x2079_20553_x2060211639}[]{#_Toc121809775}[]{#_Toc112125402}[]{#_Toc33603418}*[value]{lang="EN-US"}*[：检测振铃的防抖动时间，取值范围为]{style="font-family:宋体"}[4]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x933334720}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过调整]{style="font-family:宋体"}]{#struct_0_x2079_20553_1833045960}**[debounce]{lang="EN-US"}**[时间，可以检测不同频率和波形的振铃信号。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[请不要在通话中修改振铃检测的防抖动时间。]{style="font-family:宋体"}]{#struct_0_x2079_20553_1684327962}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[建议设置防抖动时间值不要小于]{style="font-family:宋体"}]{#struct_0_x2079_20553_x1768630937}[8]{lang="EN-US"}[，因为如果该值过小，在线路有干扰时，可能出现振铃误检。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在某一单板上的某个]{style="font-family:宋体"}]{#struct_0_x2079_20553_x1360908246}[FXO]{lang="EN-US"}[语音用户线视图下配置该命令，则对该单板上所有]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线均生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1893483180}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x1353057696}[配置检测振铃的防抖动时间为]{style="font-family:宋体"}[15]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x273793081}

[\[sysname\] subscriber-line 2/2/1]{lang="EN-US"}

[\[sysname-subscriber-line2/2/1\] ring-detect debounce 15]{lang="EN-US"}
:::::

::::: {#-1425060184 .myid}
[]{#_Toc404794468}[]{#struct_0_x2079_20553_x764774587}[]{#_Toc316549761}[]{#_Toc295912547}[]{#_Toc263260069}

**语音用户线 \-- 模拟语音用户线 \-- ring-detect frequency**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](语音用户线命令.files/image002.jpg){#图片 14 border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x2079_20553_x378342438}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[该命令的支持情况与实际使用的板卡有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2079_20553_1366682455}
:::

**[ ]{lang="EN-US"}**

[**[ring-detect]{lang="EN-US"}**[ **frequency**]{lang="EN-US"}]{#struct_0_x2079_20553_968899771}[命令用来配置检测振铃的频率。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ring-detect** **frequency**]{lang="EN-US"}]{#struct_0_x2079_20553_x542903246}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1893417644}

[**[ring-detect]{lang="EN-US"}**[ **frequency** *value*]{lang="EN-US"}]{#struct_0_x2079_20553_x612643648}

[**[undo]{lang="EN-US"}**[ **ring-detect** **frequency**]{lang="EN-US"}]{#struct_0_x2079_20553_627143953}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1337328242}

[[检测振铃的频率为]{style="font-family:宋体"}[40Hz]{lang="EN-US"}]{#struct_0_x2079_20553_x1053238071}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x13517577}

[[FXO]{lang="EN-US"}]{#struct_0_x2079_20553_x374826236}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1099055450}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1894400684}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_431380529}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_669011076}

[*[value]{lang="EN-US"}*]{#struct_0_x2079_20553_x219792696}[：检测振铃的频率，取值范围为]{style="font-family:宋体"}[30]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[，步长为]{style="font-family:宋体"}[10]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[Hz]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1236855187}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x1590047468}[配置检测振铃的频率为]{style="font-family:宋体"}[100Hz]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x1326102370}

[\[sysname\] subscriber-line 2/2/1]{lang="EN-US"}

[\[sysname-subscriber-line2/2/1\] ring-detect frequency 100]{lang="EN-US"}
:::::

::: {#-1747263384 .myid}
[]{#_Toc404794469}[]{#struct_0_x2079_20553_x1053706717}[]{#_Toc316549762}[]{#_Toc295912548}[]{#_Toc263260070}[]{#_Toc135295503}[]{#_Toc130097151}[]{#_Toc129160872}[]{#_Toc89229000}

**语音用户线 \-- 模拟语音用户线 \-- send-busytone enable**

------------------------------------------------------------------------

[**[send-busytone enable]{lang="EN-US"}**]{#struct_0_x2079_20553_1894335148}[命令用来开启忙音发送功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **send-busytone enable**]{lang="EN-US"}]{#struct_0_x2079_20553_1986705053}[命令用来关闭忙音发送功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x437731811}

[**[send-busytone]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_572223004}

[**[undo]{lang="EN-US"}**[ **send-busytone** **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_x1207622887}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x367655823}

[[忙音发送功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x2079_20553_2133354635}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x640404084}

[[FXO]{lang="EN-US"}]{#struct_0_x2079_20553_430784233}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1893876393}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x997768990}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x279084679}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x414329852}

[[如果]{style="font-family:宋体"}[PBX]{lang="EN-US"}]{#struct_0_x2079_20553_1397359230}[交换机不发送忙音，可以配置]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线发送忙音。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1082408800}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_390976022}[开启发送忙音功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x1988158583}

[\[Sysname\] subscriber-line 2/2/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/2/1\] send-busytone enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1893810857}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[send-busytone time]{lang="EN-US"}**]{#struct_0_x2079_20553_x958048344}
:::

::: {#1866838260 .myid}
[]{#_Toc404794470}[]{#struct_0_x2079_20553_x108292487}

**语音用户线 \-- 模拟语音用户线 \-- send-busytone time**

------------------------------------------------------------------------

[**[send-busytone time]{lang="EN-US"}**]{#struct_0_x2079_20553_x1304623230}[命令用来配置忙音发送的时长。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **send-busytone time**]{lang="EN-US"}]{#struct_0_x2079_20553_x1179269668}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1700235078}

[**[send-busytone]{lang="EN-US"}**[ **time** *seconds*]{lang="EN-US"}]{#struct_0_x2079_20553_x434083019}

[**[undo]{lang="EN-US"}**[ **send-busytone** **time** ]{lang="EN-US"}]{#struct_0_x2079_20553_x864004535}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_772731597}

[[忙音发送的时长为]{style="font-family:宋体"}[3]{lang="EN-US"}]{#struct_0_x2079_20553_1893745321}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1729082911}

[[FXO]{lang="EN-US"}]{#struct_0_x2079_20553_1090526486}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x588037816}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x256400937}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1664086666}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1733030029}

[**[time]{lang="EN-US"}***[ seconds]{lang="EN-US"}*]{#struct_0_x2079_20553_1787357239}[：忙音发送的时长，取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x2135960222}

[[只有开启]{style="font-family:宋体"}**[send-busytone enable]{lang="EN-US"}**]{#struct_0_x2079_20553_1893679785}[命令后，]{style="font-family:宋体"}**[send-busytone time]{lang="EN-US"}**[命令的设置才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x186171648}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x2121877250}[开启发送忙音功能，发送忙音的时长为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x1455565468}

[\[Sysname\] subscriber-line 2/2/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/2/1\] send-busytone enable]{lang="EN-US"}

[\[Sysname-subscriber-line2/2/1\] send-busytone time 5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x2018204299}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[send-busytone enable]{lang="EN-US"}**]{#struct_0_x2079_20553_x2044866730}
:::

::: {#1170655049 .myid}
[]{#_Toc404794471}[]{#struct_0_x2079_20553_x387666290}

**语音用户线 \-- 模拟语音用户线 \-- shutdown**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_x2079_20553_1893614249}[命令用来关闭语音用户线。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[shutdown]{lang="EN-US"}**]{#struct_0_x2079_20553_x1779750189}[命令用来开启语音用户线。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_872877333}

[**[shutdown]{lang="EN-US"}**]{#struct_0_x2079_20553_1470409525}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_x2079_20553_x1885398254}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_320728081}

[[语音用户线处于开启状态。]{style="font-family:宋体"}]{#struct_0_x2079_20553_x1886905563}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_98341403}

[[FXS/FXO/E&M]{lang="EN-US"}]{#struct_0_x2079_20553_x1714420153}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1893548713}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1754287309}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1063831471}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_278814503}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x775048811}[关闭语音用户线。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x1301062461}

[\[Sysname\] subscriber-line 2/1/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/1/1\] shutdown]{lang="EN-US"}
:::

::: {#-401775381 .myid}
[]{#_Toc404794472}[]{#struct_0_x2079_20553_1893483177}

**语音用户线 \-- 模拟语音用户线 \-- signal**

------------------------------------------------------------------------

[**[signal]{lang="EN-US"}**]{#struct_0_x2079_20553_x1352992171}[命令用来配置]{style="font-family:宋体"}[E&M]{lang="EN-US"}[信令的启动方式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **signal**]{lang="EN-US"}]{#struct_0_x2079_20553_877816244}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1056978920}

[**[signal]{lang="EN-US"}**[ { **delay** \| **immediate** \| **wink** }]{lang="EN-US"}]{#struct_0_x2079_20553_x2147235648}

[**[undo]{lang="PT-BR"}**]{#struct_0_x2079_20553_x1069524234}[ **signal**]{lang="PT-BR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_494547247}

[[采用立即启动方式。]{style="font-family:宋体"}]{#struct_0_x2079_20553_93668900}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1002814209}

[[E&M]{lang="EN-US"}]{#struct_0_x2079_20553_1893417641}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x612315968}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1002582054}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1457505778}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_717261796}

[**[delay]{lang="EN-US"}**]{#struct_0_x2079_20553_1533043040}[：延时启动方式。]{style="font-family:宋体"}

[**[immediate]{lang="EN-US"}**]{#struct_0_x2079_20553_x524711495}[：立即启动方式。]{style="font-family:宋体"}

[**[wink]{lang="EN-US"}**]{#struct_0_x2079_20553_x1595574756}[：闪断启动方式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1422746473}

[[在呼叫两端设备上需要配置相同的]{style="font-family:宋体"}[E&M]{lang="EN-US"}]{#struct_0_x2079_20553_1894400681}[信令启动方式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_431052849}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x9923308}[配置]{style="font-family:宋体"}[E&M]{lang="EN-US"}[信令的启动方式为延时启动方式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_1657620327}

[\[Sysname\] subscriber-line 2/3/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/3/1\] signal delay]{lang="EN-US"}
:::

::: {#-1556032784 .myid}
[]{#_Toc404794473}[]{#struct_0_x2079_20553_x1364122420}

**语音用户线 \-- 模拟语音用户线 \-- silence-detect threshold**

------------------------------------------------------------------------

[**[silence-detect threshold]{lang="EN-US"}**]{#struct_0_x2079_20553_1886272121}[命令用来设置静音检测自动挂机功能。]{style="font-family:
宋体"}

[**[undo]{lang="EN-US"}**[ **silence-detect threshold**]{lang="EN-US"}]{#struct_0_x2079_20553_183996028}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x765389828}

[**[silence-detect threshold]{lang="EN-US"}**[ *threshold* **time** *time-length*]{lang="EN-US"}]{#struct_0_x2079_20553_1894335145}

[**[undo]{lang="EN-US"}**[ **silence-detect**]{lang="EN-US"}]{#struct_0_x2079_20553_1986508445}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x788409869}

[[静音阈值为]{style="font-family:宋体"}[20]{lang="EN-US"}]{#struct_0_x2079_20553_x1915153230}[，静音时长为]{style="font-family:宋体"}[7200]{lang="EN-US"}[秒（即]{style="font-family:宋体"}[2]{lang="EN-US"}[个小时）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1923777414}

[[FXO]{lang="EN-US"}]{#struct_0_x2079_20553_x1454981403}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_2017179131}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1914579069}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x793692999}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1893876394}

[*[threshold]{lang="EN-US"}*]{#struct_0_x2079_20553_x997965598}[：静音阈值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[200]{lang="EN-US"}[。当]{style="font-family:宋体"}[PBX]{lang="EN-US"}[交换机发来的信号小于此值时，将被判定为静音。]{style="font-family:宋体"}

[*[time-length]{lang="EN-US"}*]{#struct_0_x2079_20553_1675330660}[：静音时长，取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[7200]{lang="EN-US"}[，单位为秒。当检测到的静音时长超过该值时，]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线会自动挂机。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1952199979}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当设备没有正常检测到忙音或]{style="font-family:宋体"}]{#struct_0_x2079_20553_x797289166}[PBX]{lang="EN-US"}[交换机不播放忙音的情况下，可以通过静音检测自动挂机实现挂机。其基本原理就是当静音（如果音量小于所配置的阈值，即为静音）持续的时间超过配置的静音时长，]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线会自动挂机。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通常情况下不需要使用此项功能，如果误配置很可能导致误挂机。]{style="font-family:宋体"}]{#struct_0_x2079_20553_x1144517623}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果确实需要配置此功能，建议配置时，多测试几组参数，找到一组既不会导致误挂机又可以在呼叫结束后快速释放]{style="font-family:宋体"}]{#struct_0_x2079_20553_1202076308}[FXO]{lang="EN-US"}[语音用户线资源的参数。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x838464224}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_1893810858}[设置静音阈值为]{style="font-family:宋体"}[20]{lang="EN-US"}[，静音时长为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x957458520}

[\[Sysname\] subscriber-line 2/2/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/2/1\] silence-detect threshold 20 time 100]{lang="EN-US"}
:::

::: {#-667747949 .myid}
[]{#_Toc404794474}[]{#struct_0_x2079_20553_x684746909}[]{#_Toc136487931}[]{#_Toc136504493}[]{#_Toc87442432}[]{#_Toc87787072}[]{#_Toc87851935}[]{#_Toc87852714}[]{#_Toc87853495}[]{#_Toc87867534}[]{#_Toc87442434}[]{#_Toc87787074}[]{#_Toc87851937}[]{#_Toc87852716}[]{#_Toc87853497}[]{#_Toc87867536}[]{#_Toc87442435}[]{#_Toc87787075}[]{#_Toc87851938}[]{#_Toc87852717}[]{#_Toc87853498}[]{#_Toc87867537}[]{#_Toc87442436}[]{#_Toc87787076}[]{#_Toc87851939}[]{#_Toc87852718}[]{#_Toc87853499}[]{#_Toc87867538}[]{#_Toc87442437}[]{#_Toc87787077}[]{#_Toc87851940}[]{#_Toc87852719}[]{#_Toc87853500}[]{#_Toc87867539}[]{#_Toc87442438}[]{#_Toc87787078}[]{#_Toc87851941}[]{#_Toc87852720}[]{#_Toc87853501}[]{#_Toc87867540}[]{#_Toc87442439}[]{#_Toc87787079}[]{#_Toc87851942}[]{#_Toc87852721}[]{#_Toc87853502}[]{#_Toc87867541}[]{#_Toc87442440}[]{#_Toc87787080}[]{#_Toc87851943}[]{#_Toc87852722}[]{#_Toc87853503}[]{#_Toc87867542}[]{#_Toc87442441}[]{#_Toc87787081}[]{#_Toc87851944}[]{#_Toc87852723}[]{#_Toc87853504}[]{#_Toc87867543}[]{#_Toc87442442}[]{#_Toc87787082}[]{#_Toc87851945}[]{#_Toc87852724}[]{#_Toc87853505}[]{#_Toc87867544}[]{#_Toc87442443}[]{#_Toc87787083}[]{#_Toc87851946}[]{#_Toc87852725}[]{#_Toc87853506}[]{#_Toc87867545}[]{#_Toc87442444}[]{#_Toc87787084}[]{#_Toc87851947}[]{#_Toc87852726}[]{#_Toc87853507}[]{#_Toc87867546}[]{#_Toc87442445}[]{#_Toc87787085}[]{#_Toc87851948}[]{#_Toc87852727}[]{#_Toc87853508}[]{#_Toc87867547}[]{#_Toc87442446}[]{#_Toc87787086}[]{#_Toc87851949}[]{#_Toc87852728}[]{#_Toc87853509}[]{#_Toc87867548}

**语音用户线 \-- 模拟语音用户线 \-- slic-gain**

------------------------------------------------------------------------

[**[slic-gain]{lang="EN-US"}**]{#struct_0_x2079_20553_x198693310}[命令用来配置]{style="font-family:宋体"}[slic]{lang="EN-US"}[芯片的输出增益。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **slic-gain**]{lang="EN-US"}]{#struct_0_x2079_20553_x1749628779}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1170912105}

[**[slic-gain]{lang="EN-US"}**[ { **0** \| **1** }]{lang="EN-US"}]{#struct_0_x2079_20553_x1097917162}

[**[undo]{lang="EN-US"}**[ **slic-gain**]{lang="EN-US"}]{#struct_0_x2079_20553_648012860}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1893745322}

[[输出增益为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x2079_20553_1729017375}[，即]{style="font-family:宋体"}[slic]{lang="EN-US"}[芯片的输出增益值为]{style="font-family:宋体"}[0.8dB]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_323272523}

[[E&M]{lang="EN-US"}]{#struct_0_x2079_20553_225232308}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_723368484}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1804806143}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x308147172}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1847374165}

[**[0]{lang="EN-US"}**]{#struct_0_x2079_20553_x1698840009}[：设置]{style="font-family:宋体"}[slic]{lang="EN-US"}[芯片的输出增益值为]{style="font-family:宋体"}[0.8dB]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[1]{lang="EN-US"}**]{#struct_0_x2079_20553_1893679786}[：设置]{style="font-family:宋体"}[slic]{lang="EN-US"}[芯片的输出增益值为]{style="font-family:宋体"}[2.1dB]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x186368256}

[[通过此命令，可以调整信号增益的大小。]{style="font-family:宋体"}]{#struct_0_x2079_20553_x1670471754}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x397157358}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_262249018}[配置输出增益为]{style="font-family:宋体"}[1]{lang="EN-US"}[，即]{style="font-family:宋体"}[slic]{lang="EN-US"}[芯片的输出增益值为]{style="font-family:宋体"}[2.1dB]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_1332160474}

[\[Sysname\] subscriber-line 2/3/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/3/1\] slic-gain 1]{lang="EN-US"}
:::

::: {#265850974 .myid}
[]{#_Toc404794475}[]{#struct_0_x2079_20553_x368634625}[]{#_Toc295912552}[]{#_Toc263260074}[]{#_Toc135295509}[]{#_Toc130097157}[]{#_Toc129160878}[]{#_Ref128814385}[]{#_Ref128814379}[]{#_Toc47776220}

**语音用户线 \-- 模拟语音用户线 \-- subscriber-line**

------------------------------------------------------------------------

[**[subscriber-line]{lang="EN-US"}**]{#struct_0_x2079_20553_824046576}[命令用来进入模拟语音用户线视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1893614250}

[**[subscriber-line]{lang="EN-US"}**[ *line-number*]{lang="EN-US"}]{#struct_0_x2079_20553_x1780340014}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1739358492}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2079_20553_201009452}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_344836882}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1892605897}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_2143401539}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_886353015}

[*[line-number]{lang="EN-US"}*]{#struct_0_x2079_20553_2112122123}[：语音用户线号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1893548714}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x1754352845}[进入语音用户线视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x1958921653}

[\[Sysname\] subscriber-line 2/1/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/1/1\]]{lang="EN-US"}
:::

::: {#1706952915 .myid}
[]{#_Toc404794476}[]{#struct_0_x2079_20553_221446040}[]{#_Toc316549765}[]{#_Toc295912553}[]{#_Toc263260075}[]{#_Toc135295511}[]{#_Toc130097159}[]{#_Toc129160880}

**语音用户线 \-- 模拟语音用户线 \-- timer dial-interval**

------------------------------------------------------------------------

[**[timer]{lang="EN-US"}**[ **dial-interval**]{lang="EN-US"}]{#struct_0_x2079_20553_1908537640}[命令用来配置等待用户拨下一位号码的超时时间。]{style="font-family:宋体"}

[**[undo timer dial-interval]{lang="EN-US"}**]{#struct_0_x2079_20553_x402292460}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1785005956}

[**[timer dial-interval]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}]{#struct_0_x2079_20553_x418267523}

[**[undo timer dial-interval]{lang="EN-US"}**]{#struct_0_x2079_20553_1893483178}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1353581995}

[[等待用户拨下一位号码的超时时间为]{style="font-family:宋体"}[10]{lang="EN-US"}]{#struct_0_x2079_20553_864780784}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_815732579}

[[FXS/FXO/E&M]{lang="EN-US"}]{#struct_0_x2079_20553_1622407163}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1378369858}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x2050441235}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x963806913}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x434643607}

[*[seconds]{lang="EN-US"}*]{#struct_0_x2079_20553_1893417642}[：拨下一位号码的超时时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x612250432}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户每拨一位号码，此定时器就会重启。如果定时器超时，但是用户还没有进行拨号，用户将被提示拨号超时。]{style="font-family:宋体"}]{#struct_0_x2079_20553_x160116231}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[此时间不包括用户从摘机到拨第一位号码的超时时间，用户从摘机到拨第一位号码的超时时间由]{style="font-family:宋体"}]{#struct_0_x2079_20553_1497422946}**[timer]{lang="EN-US"}**[ **first-dial**]{lang="EN-US"}[命令决定。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1656918289}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_1435129048}[配置等待用户拨下一位号码的超时时间为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x866171587}

[\[Sysname\] subscriber-line 2/1/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/1/1\] timer dial-interval 5]{lang="EN-US"}
:::

::: {#1491196330 .myid}
[]{#_Toc404794477}[]{#struct_0_x2079_20553_1438750036}[]{#_Toc324163432}

**语音用户线 \-- 模拟语音用户线 \-- timer disconnect-pulse**

------------------------------------------------------------------------

[**[timer disconnect-pulse]{lang="EN-US"}**]{#struct_0_x2079_20553_1894400682}[命令用来配置挂机脉冲信号时长。]{style="font-family:宋体"}

[**[undo timer disconnect-pulse]{lang="EN-US"}**]{#struct_0_x2079_20553_430987313}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_513906915}

[**[timer disconnect-pulse ]{lang="EN-US"}***[value]{lang="EN-US"}*]{#struct_0_x2079_20553_2028024911}

[**[undo timer disconnect-pulse]{lang="EN-US"}**]{#struct_0_x2079_20553_2111657204}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_133721473}

[[挂机脉冲信号时长为]{style="font-family:宋体"}[750]{lang="EN-US"}]{#struct_0_x2079_20553_189416174}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_31056887}

[[FXS]{lang="EN-US"}]{#struct_0_x2079_20553_x470632251}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1894335146}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1986311837}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_4713523}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_555390711}

[*[value]{lang="EN-US"}*]{#struct_0_x2079_20553_781247175}[：挂机脉冲时长。取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1500]{lang="EN-US"}[，步长为]{style="font-family:宋体"}[30]{lang="EN-US"}[，单位为毫秒]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_741504539}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x561493641}[配置挂机脉冲信号时长为]{style="font-family:宋体"}[90]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x1910931688}

[\[Sysname\] subscriber-line 2/1/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/1/1\] timer disconnect-pulse 90]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1893876391}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[disconnect lcfo]{lang="EN-US"}**]{#struct_0_x2079_20553_x997637918}
:::

::: {#-502968179 .myid}
[]{#_Toc404794478}[]{#struct_0_x2079_20553_x1477731583}[]{#_Toc316549766}[]{#_Toc295912554}[]{#_Toc263260076}[]{#_Toc135295512}[]{#_Toc130097160}[]{#_Toc129160881}

**语音用户线 \-- 模拟语音用户线 \-- timer first-dial**

------------------------------------------------------------------------

[**[timer]{lang="EN-US"}**[ **first-dial**]{lang="EN-US"}]{#struct_0_x2079_20553_x1009138662}[命令用来配置用户从摘机到拨第一位号码的超时时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **timer** **first-dial**]{lang="EN-US"}]{#struct_0_x2079_20553_543008493}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1346031188}

[**[timer]{lang="EN-US"}**[ **first-dial** *seconds*]{lang="EN-US"}]{#struct_0_x2079_20553_1684946952}

[**[undo]{lang="EN-US"}**[ **timer** **first-dial**]{lang="EN-US"}]{#struct_0_x2079_20553_x197959805}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1175778025}

[[从摘机到拨第一位号码的等待时间为]{style="font-family:宋体"}[10]{lang="EN-US"}]{#struct_0_x2079_20553_1363120492}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1893810855}

[[FXS/FXO]{lang="EN-US"}]{#struct_0_x2079_20553_x958179416}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1256971708}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1379657156}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_167738311}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1440459203}

[*[seconds]{lang="EN-US"}*]{#struct_0_x2079_20553_1314020549}[：用户从摘机到拨第一位号码的超时时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x253819607}

[[如果用户在摘机后的该时间内没有拨号，则将被提示拨号超时。]{style="font-family:宋体"}]{#struct_0_x2079_20553_x889248950}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1893745319}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_1728558622}[配置用户从摘机到拨第一位号码的时间间隔为]{style="font-family:宋体"}[15]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x868165610}

[\[Sysname\] subscriber-line 2/1/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/1/1\] timer first-dial 15]{lang="EN-US"}
:::

::: {#852340665 .myid}
[]{#_Toc404794479}[]{#struct_0_x2079_20553_106063817}[]{#_Toc316549767}[]{#_Toc295912555}[]{#_Toc263260095}

**语音用户线 \-- 模拟语音用户线 \-- timer hookflash-detect**

------------------------------------------------------------------------

[**[timer]{lang="EN-US"}**[ **hookflash-detect**]{lang="EN-US"}]{#struct_0_x2079_20553_584691371}[命令用来配置拍叉的时间范围，即设备会将检测到的挂机（挂机时长应该在指定时间范围内）判定为拍叉。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **timer** **hookflash-detect**]{lang="EN-US"}]{#struct_0_x2079_20553_950779185}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_487306822}

[**[timer]{lang="EN-US"}**[ **hookflash-detect** *hookflash-range*]{lang="EN-US"}]{#struct_0_x2079_20553_710376234}

[**[undo]{lang="EN-US"}**[ **timer** **hookflash-detect**]{lang="EN-US"}]{#struct_0_x2079_20553_700260453}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x676209749}

[[拍叉的时间范围为]{style="font-family:宋体"}[50]{lang="EN-US"}]{#struct_0_x2079_20553_1893679783}[～]{style="font-family:宋体"}[180]{lang="EN-US"}[毫秒，即设备会将检测到的挂机（挂机时长应该在]{style="font-family:宋体"}[50]{lang="EN-US"}[～]{style="font-family:宋体"}[180]{lang="EN-US"}[毫秒）判定为拍叉。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x186040576}

[[FXS]{lang="EN-US"}]{#struct_0_x2079_20553_1401635843}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x823170389}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x2006515507}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_2026210956}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_782706458}

[*[hookflash-range]{lang="EN-US"}*]{#struct_0_x2079_20553_111233014}[：拍叉的时间范围，取值范围为]{style="font-family:宋体"}[50]{lang="EN-US"}[～]{style="font-family:宋体"}[1200]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1893614247}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x1780405549}[配置拍叉的时间范围为]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[200]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x712596950}

[\[Sysname\] subscriber-line 2/1/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/1/1\] timer hookflash-detect 100-200]{lang="EN-US"}
:::

::: {#688589695 .myid}
[]{#_Toc404794480}[]{#struct_0_x2079_20553_x1923630154}[]{#_Toc316549768}[]{#_Toc295912556}[]{#_Toc263260096}[]{#_Toc152832582}

**语音用户线 \-- 模拟语音用户线 \-- timer hookoff-interval**

------------------------------------------------------------------------

[**[timer]{lang="EN-US"}**[ **hookoff-interval**]{lang="EN-US"}]{#struct_0_x2079_20553_x1788102351}[命令用来配置从挂机到摘机的时长。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **timer** **hookoff-interval**]{lang="EN-US"}]{#struct_0_x2079_20553_x487503760}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1391054898}

[**[timer]{lang="EN-US"}**[ **hookoff-interval** *milliseconds*]{lang="EN-US"}]{#struct_0_x2079_20553_247278352}

[**[undo]{lang="EN-US"}**[ **timer** **hookoff-interval**]{lang="EN-US"}]{#struct_0_x2079_20553_1893548711}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1754156237}

[[从挂机到摘机的时长为]{style="font-family:宋体"}[500]{lang="EN-US"}]{#struct_0_x2079_20553_x1336204421}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1520315077}

[[FXO]{lang="EN-US"}]{#struct_0_x2079_20553_x926296526}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x2073487490}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1237429591}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1722173636}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x2000973422}

[*[milliseconds]{lang="EN-US"}*]{#struct_0_x2079_20553_1893483175}[：从挂机到摘机的时长。取值范围为]{style="font-family:宋体"}[500]{lang="EN-US"}[～]{style="font-family:宋体"}[4000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1352861099}

[[FXO]{lang="EN-US"}]{#struct_0_x2079_20553_325077540}[语音用户线在与]{style="font-family:宋体"}[FXS]{lang="EN-US"}[语音用户线绑定模式下，]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线同]{style="font-family:宋体"}[FXS]{lang="EN-US"}[语音用户线摘挂机状态一致。]{style="font-family:宋体"}[FXS]{lang="EN-US"}[语音用户线摘机后，同其绑定的]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线在摘机之前，必须先进行挂机操作，然后再次进行摘机。此命令设置的参数即为从挂机到摘机的时长。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1478371925}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_370075895}[配置从挂机到摘机的时长为]{style="font-family:宋体"}[600]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x31866779}

[\[Sysname\] subscriber-line 2/2/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/2/1\] timer hookoff-interval 600]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1434142593}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hookoff-mode delay bind]{lang="EN-US"}**]{#struct_0_x2079_20553_705887787}
:::

::: {#1468319565 .myid}
[]{#_Toc404794481}[]{#struct_0_x2079_20553_1893417639}[]{#_Toc316549769}[]{#_Toc295912557}[]{#_Toc263260097}[]{#_Toc135295513}[]{#_Toc130097161}[]{#_Toc129160882}

**语音用户线 \-- 模拟语音用户线 \-- timer ring-back**

------------------------------------------------------------------------

[**[timer]{lang="EN-US"}**[ **ring-back**]{lang="EN-US"}]{#struct_0_x2079_20553_x611791675}[命令用来配置设备发送回铃音的最大时长。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **timer** **ring-back**]{lang="EN-US"}]{#struct_0_x2079_20553_x2014355931}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1038377436}

[**[timer ring-back ]{lang="EN-US"}***[seconds]{lang="EN-US"}*]{#struct_0_x2079_20553_1500821360}

[**[undo timer ring-back]{lang="EN-US"}**]{#struct_0_x2079_20553_x646146174}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1875815131}

[[发送回铃音的最大时长为]{style="font-family:宋体"}[60]{lang="EN-US"}]{#struct_0_x2079_20553_787676760}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1187946045}

[[FXS/FXO/E&M]{lang="EN-US"}]{#struct_0_x2079_20553_1894400679}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_431577126}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x621970450}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1225719369}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_851553191}

[*[seconds]{lang="EN-US"}*]{#struct_0_x2079_20553_x720066098}[：设备发送回铃音的最大时长，取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[120]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1646597942}

[[为了避免主叫用户长时间向被叫发起呼叫，如果被叫用户在该时间内没有摘机应答，主叫用户将被提示呼叫结束。]{style="font-family:宋体"}]{#struct_0_x2079_20553_x702546905}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1894335143}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_1986115229}[配置设备发送回铃音的最大时长为]{style="font-family:宋体"}[8]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x52838824}

[\[Sysname\] subscriber-line 2/1/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/1/1\] timer ring-back 8]{lang="EN-US"}
:::

::: {#-1481248895 .myid}
[]{#_Toc404794482}[]{#struct_0_x2079_20553_31827434}

**语音用户线 \-- 模拟语音用户线 \-- timer wait-digit**

------------------------------------------------------------------------

[**[timer]{lang="EN-US"}**[ **wait-digit**]{lang="EN-US"}]{#struct_0_x2079_20553_x1626082597}[命令用来配置被叫侧设备等待接收第一位号码的最大时长。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **timer** **wait-digit**]{lang="EN-US"}]{#struct_0_x2079_20553_1275396029}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_263057614}

[**[timer wait-digit]{lang="EN-US"}**[ { *seconds* \| **infinity** }]{lang="EN-US"}]{#struct_0_x2079_20553_1235820426}

[**[undo timer wait-digit]{lang="FR"}**]{#struct_0_x2079_20553_1893876392}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x997834526}

[[被叫侧设备等待接收第一位号码的最大时长为]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_x2079_20553_119535895}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_184333301}

[[E&M]{lang="EN-US"}]{#struct_0_x2079_20553_2004209503}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1883386010}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_441147596}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1284066937}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_73949353}

[*[seconds]{lang="EN-US"}*]{#struct_0_x2079_20553_1893810856}[：被叫侧设备等待接收第一位号码的最大时长，取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[infinity]{lang="FR"}**]{#struct_0_x2079_20553_x958113880}[：没有时间限制。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x479357907}

[[如果被叫侧设备在该时间内没有接收到第一位号码，被叫侧设备会播放忙音。]{style="font-family:宋体"}]{#struct_0_x2079_20553_1768245541}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1695914776}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_1040656886}[配置被叫侧设备等待接收第一位号码的最大时长为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x1843165190}

[\[Sysname\] subscriber-line 2/3/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/3/1\] timer wait-digit 10]{lang="EN-US"}
:::

::: {#-1657627290 .myid}
[]{#_Toc404794483}[]{#struct_0_x2079_20553_1818635473}[]{#_Toc316549770}[]{#_Toc295912559}[]{#_Toc263260099}[]{#_Toc135295515}[]{#_Toc130097163}[]{#_Toc129160884}[]{#_Toc47776227}

**语音用户线 \-- 模拟语音用户线 \-- transmit gain**

------------------------------------------------------------------------

[**[transmit]{lang="EN-US"}**[ **gain**]{lang="EN-US"}]{#struct_0_x2079_20553_1893745320}[命令用来配置输出端的增益值。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **transmit** **gain**]{lang="EN-US"}]{#struct_0_x2079_20553_1729148447}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_303028380}

[**[transmit]{lang="EN-US"}**[ **gain** *value*]{lang="EN-US"}]{#struct_0_x2079_20553_1655275762}

[**[undo]{lang="EN-US"}**[ **transmit** **gain**]{lang="EN-US"}]{#struct_0_x2079_20553_x854860211}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_831582988}

[[输出方向的增益值为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x2079_20553_2111066091}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1803689517}

[[FXS/FXO/E&M]{lang="EN-US"}]{#struct_0_x2079_20553_454328118}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1893679784}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x186237184}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_240951825}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_2092088423}

[*[value]{lang="EN-US"}*]{#struct_0_x2079_20553_x1852856490}[：输出方向的增益值，取值范围为]{style="font-family:宋体"}[-14.0]{lang="EN-US"}[～]{style="font-family:宋体"}[13.9]{lang="EN-US"}[，单位是]{style="font-family:宋体"}[dB]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x191955209}

[[当输出到线路上语音信号电平需要减小时，可以使用本命令适当减小输出增益值以适应输出线路信号要求。]{style="font-family:宋体"}]{#struct_0_x2079_20553_x443513765}

[[调整增益大小可能会导致语音呼叫失败。建议不要随意调整增益大小，如果确实有需要，请在技术人员指导下进行。]{style="font-family:宋体"}]{#struct_0_x2079_20553_x735732586}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1893614248}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x1779815725}[配置输出方向的增益值为]{style="font-family:宋体"}[-6.7dB]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_842795327}

[\[Sysname\] subscriber-line 2/1/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/1/1\] transmit gain -6.7]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x303846298}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[receive]{lang="EN-US"}**[ **gain**]{lang="EN-US"}]{#struct_0_x2079_20553_942398243}
:::

::: {#-1051447130 .myid}
[]{#_Toc404794484}[]{#struct_0_x2079_20553_1845574662}

**语音用户线 \-- 模拟语音用户线 \-- type**

------------------------------------------------------------------------

[**[type]{lang="EN-US"}**]{#struct_0_x2079_20553_x478318399}[命令用来配置]{style="font-family:宋体"}[E&M]{lang="EN-US"}[信号类型。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **type**]{lang="EN-US"}]{#struct_0_x2079_20553_x1669898929}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1893548712}

[**[type]{lang="EN-US"}**[ { **1** \| **2** \| **3** \| **5** }]{lang="EN-US"}]{#struct_0_x2079_20553_x1754221773}

[**[undo type]{lang="EN-US"}**]{#struct_0_x2079_20553_1103755797}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x915445111}

[[信号类型为类型]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_x2079_20553_x384683923}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_255119503}

[[E&M]{lang="EN-US"}]{#struct_0_x2079_20553_x299511514}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x478563988}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x961775869}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1893483176}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1352926635}

[**[1]{lang="EN-US"}**]{#struct_0_x2079_20553_785684382}[：]{style="font-family:宋体"}[E&M]{lang="EN-US"}[信号类型为类型]{style="font-family:宋体"}[I]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[2]{lang="EN-US"}**]{#struct_0_x2079_20553_361082560}[：]{style="font-family:宋体"}[E&M]{lang="EN-US"}[信号类型为类型]{style="font-family:宋体"}[II]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[3]{lang="EN-US"}**]{#struct_0_x2079_20553_x1218815733}[：]{style="font-family:宋体"}[E&M]{lang="EN-US"}[信号类型为类型]{style="font-family:宋体"}[III]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[5]{lang="EN-US"}**]{#struct_0_x2079_20553_1952135766}[：]{style="font-family:宋体"}[E&M]{lang="EN-US"}[信号类型为类型]{style="font-family:宋体"}[V]{lang="EN-US"}[。。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1950604781}

[[在呼叫两端设备上需要配置相同的]{style="font-family:宋体"}[E&M]{lang="EN-US"}]{#struct_0_x2079_20553_x654355861}[信号类型。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1980978374}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_1893417640}[配置信号类型为类型]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x612381504}

[\[Sysname\] subscriber-line 2/3/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/3/1\] type 3]{lang="EN-US"}

[ ]{lang="EN-US"}
:::

[\
]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}

::: {.Section3 style="layout-grid:15.75pt"}
:::

::: {#-981775860 .myid}
[]{#_Toc404794486}[]{#struct_0_x2079_20553_727139636}[]{#_Toc316027045}[]{#_Toc37216690}

**语音用户线 \-- 数字语音用户线 \-- ani**

------------------------------------------------------------------------

[**[ani]{lang="EN-US"}**]{#struct_0_x2079_20553_2066601668}[命令用来配置入局端向出局端请求主叫组号码信息（业务类别信息和主叫号码）。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ani**]{lang="EN-US"}]{#struct_0_x2079_20553_x1008681942}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x485439444}

[**[ani]{lang="EN-US"}**[ { **all** \| **ka** }]{lang="EN-US"}]{#struct_0_x2079_20553_1878594737}

[**[undo ani]{lang="EN-US"}**]{#struct_0_x2079_20553_1894400680}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_431118385}

[[入局端不向出局端请求主叫组号码信息。]{style="font-family:宋体"}]{#struct_0_x2079_20553_43487723}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_671763013}

[[R2]{lang="EN-US"}]{#struct_0_x2079_20553_x640424326}[信令视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1903673629}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_713354563}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_929215470}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x879867646}

[**[all]{lang="EN-US"}**]{#struct_0_x2079_20553_1894335144}[：要求出局端发送主叫业务类别信息与主叫号码。]{style="font-family:宋体"}

[**[ka]{lang="EN-US"}**]{#struct_0_x2079_20553_1986442909}[：要求出局端只发送主叫业务类别信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1557688904}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x480639547}[配置入局端向出局端请求主叫组号码信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="DA"}]{#struct_0_x2079_20553_1368265971}

[\[Sysname\] controller e1 2/4/1]{lang="DA"}

[\[Sysname-E1 2/4/1\] timeslot-set 0 timeslot-list 1-31 signal r2]{lang="DA"}

[\[Sysname-E1 2/4/1\] cas 0]{lang="DA"}

[\[Sysname-cas 2/4/1:0\] ani all]{lang="DA"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x6579434}

[[·[              ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}**[ani-]{lang="EN-US"}[digit]{lang="EN-US"}**]{#struct_0_x2079_20553_1004647936}
:::

::: {#-768370976 .myid}
[]{#_Toc404794487}[]{#struct_0_x2079_20553_x835006960}[]{#_Toc316027046}[]{#_Toc37216691}

**语音用户线 \-- 数字语音用户线 \-- ani-digit**

------------------------------------------------------------------------

[**[ani-]{lang="EN-US"}[digit]{lang="EN-US"}**]{#struct_0_x2079_20553_1555363959}[命令用来配置请求主叫组号码信息之前需要收集的被叫号位数。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ani-digit**]{lang="EN-US"}]{#struct_0_x2079_20553_1860945765}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1047304622}

[**[ani-]{lang="EN-US"}[digit]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_x2079_20553_1299476879}

[**[undo]{lang="EN-US"}**[ **ani-digit**]{lang="EN-US"}]{#struct_0_x2079_20553_x549174948}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1746222682}

[[请求主叫组号码信息之前需要收集的被叫号位数为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x2079_20553_x964994343}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x564857839}

[[R2]{lang="EN-US"}]{#struct_0_x2079_20553_x835072496}[信令视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x81212708}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x45529427}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x733601932}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1411813832}

[*[number]{lang="EN-US"}*]{#struct_0_x2079_20553_x337510151}[：收集的号码位数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x634068359}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当入局端收集的号码个数小于该值时，入局端将等待接收下一个号码直到超时，在等待过程中不会向出局端请求主叫号码信息；入局端收集的号码个数等于或超过该值后，会向出局端请求主叫组号码信息。]{style="font-family:宋体"}]{#struct_0_x2079_20553_x1386510717}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有开启]{lang="EN-US" style="font-family:宋体"}**[ani all]{lang="EN-US"}**]{#struct_0_x2079_20553_x970808145}[命令后，]{lang="EN-US" style="font-family:宋体"}**[ani-]{lang="EN-US"}[digit]{lang="EN-US"}**[命令的设置才能生效。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x835138032}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x1645639961}[配置入局端收到]{style="font-family:宋体"}[3]{lang="EN-US"}[位号码后，向出局端请求主叫组号码信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="DA"}]{#struct_0_x2079_20553_x274170389}

[\[Sysname\] controller e1 2/4/1]{lang="DA"}

[\[Sysname-E1 2/4/1\] timeslot-set 0 timeslot-list 1-31 signal r2]{lang="DA"}

[\[Sysname-E1 2/4/1\] cas 0]{lang="DA"}

[\[Sysname-cas 2/4/1:0\] ani all]{lang="DA"}

[\[Sysname-cas 2/4/1:0\] ani-digit 3]{lang="DA"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x2041118220}

[[·[              ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}**[ani]{lang="EN-US"}**]{#struct_0_x2079_20553_x337654583}
:::

::: {#-777018785 .myid}
[]{#_Toc404794488}[]{#struct_0_x2079_20553_579145841}[]{#_Toc316027036}

**语音用户线 \-- 数字语音用户线 \-- answer enable**

------------------------------------------------------------------------

[**[answer]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_x1971084459}[命令用来配置出局端要求入局端必须发送应答信号。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **answer** **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_x835203568}[命令用来配置出局端不强制要求入局端发送应答信号。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x848341370}

[**[answer]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_1170441615}

[**[undo]{lang="EN-US"}**[ **answer** **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_111984615}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1546513750}

[[出局端要求入局端发送应答信号。]{style="font-family:宋体"}]{#struct_0_x2079_20553_x51589486}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1938512502}

[[R2]{lang="EN-US"}]{#struct_0_x2079_20553_1420943568}[信令视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_65573004}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x835269104}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1863717422}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1446673494}

[[若出局端不要求入局端发送应答信号，那么双方可以直接进入通话状态。如果配置]{style="font-family:宋体"}**[answer]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_18213042}[命令，那么只有在出局端接收到应答信号后，双方才能进入通话状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1920684474}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_680157483}[配置出局端不强制要求入局端发送应答信号。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="DA"}]{#struct_0_x2079_20553_1522587657}

[\[Sysname\] controller e1 2/4/1]{lang="DA"}

[\[Sysname-E1 2/4/1\] timeslot-set 0 timeslot-list 1-31 signal r2]{lang="DA"}

[\[Sysname-E1 2/4/1\] cas 0]{lang="DA"}

[\[Sysname-cas 2/4/1:0\] undo answer enable]{lang="DA"}
:::

::: {#61066128 .myid}
[]{#_Toc404794489}[]{#struct_0_x2079_20553_x835334640}[]{#_Toc313548820}[]{#_Toc294166675}[]{#_Toc262031003}[]{#_Toc135295490}[]{#_Toc130097139}[]{#_Toc129160859}[]{#_Toc47776198}

**语音用户线 \-- 数字语音用户线 \-- callmode**

------------------------------------------------------------------------

[**[callmode]{lang="EN-US"}**]{#struct_0_x2079_20553_1114640330}[命令用来配置呼叫接续模式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **callmode**]{lang="EN-US"}]{#struct_0_x2079_20553_x1263008544}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1463546868}

[**[callmode]{lang="EN-US"}**[ { **segment** \| **terminal** }]{lang="EN-US"}]{#struct_0_x2079_20553_1341066949}

[**[undo]{lang="EN-US"}**[ **callmode**]{lang="EN-US"}]{#struct_0_x2079_20553_558794808}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1544830842}

[[呼叫接续模式为端到端方式。]{style="font-family:宋体"}]{#struct_0_x2079_20553_833612347}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_118137699}

[[R2]{lang="EN-US"}]{#struct_0_x2079_20553_x835400176}[信令视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x47324520}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x102277202}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x519221615}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x657892000}

[**[segment]{lang="EN-US"}**]{#struct_0_x2079_20553_172952022}[：采用段到段方式。]{style="font-family:宋体"}

[**[terminal]{lang="EN-US"}**]{#struct_0_x2079_20553_1094529854}[：采用端到端方式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x770228588}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_487480572}[配置使用段到段的呼叫接续模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="DA"}]{#struct_0_x2079_20553_x835465712}

[\[Sysname\] controller e1 2/4/1]{lang="DA"}

[\[Sysname-E1 2/4/1\] timeslot-set 0 timeslot-list 1-31 signal r2]{lang="DA"}

[\[Sysname-E1 2/4/1\] cas 0]{lang="DA"}

[\[Sysname-cas 2/4/1:0\] callmode segment]{lang="DA"}
:::

::: {#-175403416 .myid}
[]{#_Toc404794490}[]{#struct_0_x2079_20553_329292683}[]{#_Toc316027025}

**语音用户线 \-- 数字语音用户线 \-- cas**

------------------------------------------------------------------------

[**[cas]{lang="EN-US"}**]{#struct_0_x2079_20553_x1222559683}[命令用来进入]{style="font-family:宋体"}[R2]{lang="EN-US"}[信令视图。]{style="font-family:宋体"}

[**[undo cas]{lang="EN-US"}**]{#struct_0_x2079_20553_x1363142335}[命令用来删除指定的]{style="font-family:宋体"}[R2]{lang="EN-US"}[信令视图及其该视图下的相关配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1973666606}

[**[cas]{lang="EN-US"}**[ *ts-set-number*]{lang="EN-US"}]{#struct_0_x2079_20553_820834407}

[**[undo cas ]{lang="EN-US"}***[ts-set-number]{lang="EN-US"}*]{#struct_0_x2079_20553_x1267920831}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x834482672}

[[E1]{lang="EN-US"}]{#struct_0_x2079_20553_x1225471026}[语音]{style="font-family:宋体"}[/T1]{lang="EN-US"}[语音接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1501032371}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x941072822}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1562060598}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x33467452}

[*[ts-set-number]{lang="EN-US"}*]{#struct_0_x2079_20553_1435963495}[：时隙组的编号，]{style="font-family:宋体"}[E1]{lang="EN-US"}[语音接口的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[，]{style="font-family:宋体"}[T1]{lang="EN-US"}[语音接口的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[23]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_713394328}

[[在进入时隙组的]{style="font-family:宋体"}[R2]{lang="EN-US"}]{#struct_0_x2079_20553_x642027247}[信令视图前，需要使用]{style="font-family:宋体"}**[timeslot-set]{lang="EN-US"}**[命令创建时隙组。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x834548208}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_1474004812}[进入]{style="font-family:宋体"}[5]{lang="EN-US"}[号时隙组的]{style="font-family:宋体"}[R2]{lang="EN-US"}[信令视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_957745010}

[\[Sysname\] controller e1 ]{lang="EN-US"}[2/4/1]{lang="DA"}

[\[Sysname-E1 2/4/1\]]{lang="DA"}[ timeslot-set 5 timeslot-list 1-31 signal r2]{lang="DA"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] cas 5]{lang="EN-US"}

[\[Sysname-cas ]{lang="EN-US"}[2/4/1]{lang="DA"}[:5\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1331670486}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timeslot-set]{lang="EN-US"}**]{#struct_0_x2079_20553_1428216566}
:::

::: {#12283302 .myid}
[]{#_Toc404794491}[]{#struct_0_x2079_20553_697715438}[]{#_Toc316027038}[]{#_Toc61260441}

**语音用户线 \-- 数字语音用户线 \-- clear-forward-ack enable**

------------------------------------------------------------------------

[**[clear-forward-ack]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_1381493141}[命令用来配置出局端主动拆线时，入局端必须发送后向拆线信号给予回应。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **clear-forward-ack** **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_x835006959}[用来配置出局端主动拆线时，入局端不发送后向拆线信号给予回应。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1555822708}

[**[clear-forward-ack enable]{lang="EN-US"}**]{#struct_0_x2079_20553_x1332462894}

[**[undo clear-forward-ack enable]{lang="EN-US"}**]{#struct_0_x2079_20553_1833947864}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_890549797}

[[出局端主动拆线时，入局端不发送后向拆线信号给予回应。]{style="font-family:宋体"}]{#struct_0_x2079_20553_1101765339}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1172804973}

[[R2]{lang="EN-US"}]{#struct_0_x2079_20553_x101401267}[信令视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1154783741}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x835072495}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x81016100}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1484759681}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_1954758511}[配置出局端主动拆线时，入局端必须发送后向拆线信号给予回应。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_175098249}

[\[Sysname\] controller e1 ]{lang="EN-US"}[2/4/1]{lang="DA"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] timeslot-set 0 timeslot-list 1-31 signal r2]{lang="EN-US"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] cas 0]{lang="EN-US"}

[\[Sysname-cas ]{lang="EN-US"}[2/4/1]{lang="DA"}[:0\] clear-forward-ack enable]{lang="EN-US"}
:::

::: {#-1533389649 .myid}
[]{#_Toc404794492}[]{#struct_0_x2079_20553_1937521338}[]{#_Toc316027055}

**语音用户线 \-- 数字语音用户线 \-- display voice subscriber-line**

------------------------------------------------------------------------

[**[display voice subscriber-line]{lang="EN-US"}**]{#struct_0_x2079_20553_1199153116}[命令用来显示数字语音用户线信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x835138031}

[[E1]{lang="EN-US"}]{#struct_0_x2079_20553_x1645443353}[或]{style="font-family:宋体"}[T1]{lang="EN-US"}[语音接口生成的数字语音用户线：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **voice subscriber-line** *line-number*]{lang="EN-US"}]{#struct_0_x2079_20553_x2104062800}[：]{style="font-family:宋体"}[{ *ts-set-number* \| *ts-set-number.sub-timeslot* \| **15** \| **23** }]{lang="EN-US"}

[[BSV]{lang="EN-US"}]{#struct_0_x2079_20553_x247417044}[语音接口生成的数字语音用户线：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **voice subscriber-line** *line-number.subnumber*]{lang="EN-US"}]{#struct_0_x2079_20553_x426784181}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x320524521}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2079_20553_x1936183605}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_346982513}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1079078682}

[[network-operator]{lang="EN-US"}]{#struct_0_x2079_20553_x835203567}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x848800122}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2079_20553_x1169681964}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x423327325}

[*[line-number]{lang="EN-US"}*]{#struct_0_x2079_20553_x1221030818}[：]{style="font-family:宋体"}[E1/T1]{lang="EN-US"}[语音接口编号。]{style="font-family:宋体"}

[*[ts-set-number]{lang="EN-US"}*]{#struct_0_x2079_20553_1209222807}[：时隙组编号。]{style="font-family:宋体"}

[*[sub-timeslot]{lang="EN-US"}*]{#struct_0_x2079_20553_1868184310}[：表示指定的时隙。]{style="font-family:宋体"}

[*[subnumber]{lang="EN-US"}*]{#struct_0_x2079_20553_508700186}[：语音用户线的子接口，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[15]{lang="EN-US"}**]{#struct_0_x2079_20553_x738731257}[：将]{style="font-family:宋体"}[E1]{lang="EN-US"}[语音接口的时隙捆绑为]{style="font-family:宋体"}[ISDN PRI]{lang="EN-US"}[组后，系统生成的编号。]{style="font-family:宋体"}

[**[23]{lang="EN-US"}**]{#struct_0_x2079_20553_x835269103}[：将]{style="font-family:宋体"}[T1]{lang="EN-US"}[语音接口的时隙捆绑为]{style="font-family:宋体"}[ISDN PRI]{lang="EN-US"}[组后，系统生成的编号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1864045102}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x1564894509}[显示]{style="font-family:宋体"}[E1]{lang="EN-US"}[语音接口生成的数字语音用户线信息。]{style="font-family:宋体"}

[[\<Sysname\> display voice subscriber-line ]{lang="EN-US"}]{#struct_0_x2079_20553_x835334639}[2/4/1]{lang="DA"}[:0]{lang="EN-US"}

[Current information]{lang="EN-US"}[        ]{lang="NO-BOK"}[subscriber-line]{lang="EN-US"}[2/4/1]{lang="DA"}[:0]{lang="EN-US"}

[    ]{lang="NO-BOK"}[Type: R2]{lang="EN-US"}

[    ]{lang="NO-BOK"}[Status: Up]{lang="EN-US"}

[    Call status:]{lang="NO-BOK"}

[        TS 1: Idle]{lang="NO-BOK"}

[        TS 2: Idle]{lang="NO-BOK"}

[        TS 3: Idle]{lang="NO-BOK"}

[        TS 4: Idle]{lang="NO-BOK"}

[        TS 5: Idle]{lang="NO-BOK"}

[        TS 6: Idle]{lang="NO-BOK"}

[        TS 7: Idle]{lang="NO-BOK"}

[        TS 8: Idle]{lang="NO-BOK"}

[        TS 9: Idle]{lang="NO-BOK"}

[        TS 10: Idle]{lang="NO-BOK"}

[        TS 11: Idle]{lang="NO-BOK"}

[        TS 12: Idle]{lang="NO-BOK"}

[        TS 13: Idle]{lang="NO-BOK"}

[        TS 14: Idle]{lang="NO-BOK"}

[        TS 15: Idle]{lang="NO-BOK"}

[        TS 17: Idle]{lang="NO-BOK"}

[        TS 18: Idle]{lang="NO-BOK"}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_1115230153}[显示]{style="font-family:宋体"}[BSV]{lang="EN-US"}[语音接口生成的数字语音用户线信息。]{style="font-family:宋体"}

[[\<Sysname\> ]{lang="EN-US"}]{#struct_0_x2079_20553_x472578710}[display voice subscriber-line ]{lang="NO-BOK"}[2/5/1]{lang="DA"}

[  Current information : subscriber-line]{lang="NO-BOK"}[2/5/1]{lang="DA"}

[      Type: ISDN]{lang="NO-BOK"}

[      Status: Up]{lang="NO-BOK"}

[      Call status:]{lang="NO-BOK"}

[        TS 0: Idle]{lang="NO-BOK"}

[        TS 1: Idle]{lang="NO-BOK"}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_1496210825}[显示]{style="font-family:宋体"}[BSV]{lang="EN-US"}[语音接口生成的数字语音用户线子接口信息。]{style="font-family:宋体"}

[[\<Sysname\> ]{lang="EN-US"}]{#struct_0_x2079_20553_x835400175}[display voice subscriber-line ]{lang="NO-BOK"}[2/5/1]{lang="DA"}[.1]{lang="NO-BOK"}

[  Current information : subscriber-line]{lang="NO-BOK"}[2/5/1]{lang="DA"}[.1]{lang="NO-BOK"}

[      Type: ISDN]{lang="NO-BOK"}

[      Status: Up]{lang="NO-BOK"}

[      Call status: Idle]{lang="NO-BOK"}

[]{#struct_0_x2079_20553_x47258984}[]{#_Toc37211929}[]{#_Toc37216704}[]{#_Toc129160935}[]{#_Toc61260452}[]{#_Toc121809773}[]{#_Toc112125400}[]{#_Toc38788028}[表1-4 ]{lang="EN-US"}[display voice subscriber-line]{lang="EN-US"}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_266979483}[[字段]{style="font-family:黑体"}]{#struct_0_x2079_20553_x446109455}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1037751749}

[[Current information]{lang="EN-US"}]{#struct_0_x2079_20553_312917279}

[[当前语音用户线的信息]{style="font-family:宋体"}]{#struct_0_x2079_20553_x419949458}

[[Type]{lang="EN-US"}]{#struct_0_x2079_20553_x470744260}

[[语音用户线使用的信令类型：]{style="font-family:宋体"}]{#struct_0_x2079_20553_x835465711}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[R2]{lang="EN-US"}]{#struct_0_x2079_20553_329096075}[：使用]{lang="EN-US" style="font-family:宋体"}[R2]{lang="EN-US"}[信令进行呼叫]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISDN]{lang="EN-US"}]{#struct_0_x2079_20553_59199241}[：使用]{lang="EN-US" style="font-family:宋体"}[ISDN]{lang="EN-US"}[信令进行呼叫]{lang="EN-US" style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_x2079_20553_x1757558967}

[[语音用户线的状态：]{style="font-family:宋体"}]{#struct_0_x2079_20553_529408933}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_x2079_20553_x1738658249}[：语音用户线处于]{style="font-family:宋体"}[Up]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_x2079_20553_x834482671}[：语音用户线处于]{style="font-family:宋体"}[Down]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down(Administratively)]{lang="EN-US"}]{#struct_0_x2079_20553_x1225405490}[：语音用户线表示已经通过]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，即管理状态为关闭]{style="font-family:宋体"}

[[TS]{lang="EN-US"}]{#struct_0_x2079_20553_x467358418}

[[时隙组中的时隙]{style="font-family:宋体"}]{#struct_0_x2079_20553_x1205371892}

[[Call Status]{lang="EN-US"}]{#struct_0_x2079_20553_x834548207}

[[使用]{style="font-family:宋体"}[R2]{lang="EN-US"}]{#struct_0_x2079_20553_1474070348}[信令进行呼叫，会出现以下几种呼叫状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Idle]{lang="EN-US"}]{#struct_0_x2079_20553_2119709963}[：空闲状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Seize]{lang="EN-US"}]{#struct_0_x2079_20553_x447862584}[：占用状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Seize Ack]{lang="EN-US"}]{#struct_0_x2079_20553_225192100}[：占用确认状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Talking]{lang="EN-US"}]{#struct_0_x2079_20553_x835006962}[：通话状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Releasing]{lang="EN-US"}]{#struct_0_x2079_20553_1555232887}[：拆线状态]{lang="EN-US" style="font-family:宋体"}

[[使用]{style="font-family:宋体"}[ISDN]{lang="EN-US"}]{#struct_0_x2079_20553_x1676461036}[信令进行呼叫，会出现以下几种呼叫状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Idle]{lang="EN-US"}]{#struct_0_x2079_20553_1431179978}[：空闲状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Call in]{lang="EN-US"}]{#struct_0_x2079_20553_x969194180}[：呼入状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Call out]{lang="EN-US"}]{#struct_0_x2079_20553_x835072498}[：呼出状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ring]{lang="EN-US"}]{#struct_0_x2079_20553_x81343780}[：振铃状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ringback tone]{lang="EN-US"}]{#struct_0_x2079_20553_x788707528}[：回铃音状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Talking]{lang="EN-US"}]{#struct_0_x2079_20553_x351558949}[：通话状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Releasing]{lang="EN-US"}]{#struct_0_x2079_20553_x835138034}[：拆线状态]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-426367985 .myid}
[]{#_Toc404794493}[]{#struct_0_x2079_20553_x1645246745}[]{#_Toc316027041}[]{#_Toc137986355}

**语音用户线 \-- 数字语音用户线 \-- dl-bits**

------------------------------------------------------------------------

[**[dl-bits]{lang="EN-US"}**]{#struct_0_x2079_20553_639345534}[命令用来配置线路信号的比特值。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **dl-bits**]{lang="EN-US"}]{#struct_0_x2079_20553_891066489}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1839263969}

[**[dl-bits ]{lang="EN-US"}**[{ **answer** \| **blocking** \| **clear-back** \| **clear-forward** \| **idle** \| **release-guard** \| **seizing** \| **seizing-ack** } { **receive** \| **transmit** } *ABCD*]{lang="EN-US"}]{#struct_0_x2079_20553_770214394}

[**[undo dl-bits ]{lang="EN-US"}**[{ **answer** \| **blocking** \| **clear-back** \| **clear-forward** \| **idle \| release-guard** \| **seizing** \| **seizing-ack** } { **receive** \| **transmit** }]{lang="EN-US"}]{#struct_0_x2079_20553_1447925165}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1748245280}

[[线路信号的比特值使用]{style="font-family:宋体"}[ITU-T]{lang="EN-US"}]{#struct_0_x2079_20553_x835203570}[标准。具体缺省值如下表所示。]{style="font-family:宋体"}

[[表1-5 ]{lang="EN-US"}[线路信号的缺省值]{style="font-family:黑体"}]{#struct_0_x2079_20553_x848865659}

[]{#table_struct_0_262654683}[[信号]{style="font-family:黑体"}]{#struct_0_x2079_20553_31568892}
:::

[**[rx-bits]{lang="EN-US"}**]{#struct_0_x2079_20553_x1402452665}[[ ]{lang="EN-US"}]{.TableTextChar}*[ABCD]{lang="EN-US"}*[缺省值]{style="font-family:
   黑体"}

[**[tx-bits]{lang="EN-US"}**]{#struct_0_x2079_20553_2100784213}[[ ]{lang="EN-US"}]{.TableTextChar}*[ABCD]{lang="EN-US"}*[缺省值]{style="font-family:
   黑体"}

[[answer]{lang="EN-US"}]{#struct_0_x2079_20553_1170663861}[（应答）]{style="font-family:宋体"}

[[0101]{lang="EN-US"}]{#struct_0_x2079_20553_x835269106}

[[0101]{lang="EN-US"}]{#struct_0_x2079_20553_1863848494}

[[blocking]{lang="EN-US"}]{#struct_0_x2079_20553_556445171}[（闭塞）]{style="font-family:宋体"}

[[1101]{lang="EN-US"}]{#struct_0_x2079_20553_x193873945}

[[1101]{lang="EN-US"}]{#struct_0_x2079_20553_679004372}

[[clear-back]{lang="EN-US"}]{#struct_0_x2079_20553_x37102252}[（后向拆线）]{style="font-family:宋体"}

[[1101]{lang="EN-US"}]{#struct_0_x2079_20553_x835334642}

[[1101]{lang="EN-US"}]{#struct_0_x2079_20553_1114509258}

[[clear-forward]{lang="EN-US"}]{#struct_0_x2079_20553_x1671220036}[（前向拆线）]{style="font-family:宋体"}

[[1001]{lang="EN-US"}]{#struct_0_x2079_20553_1539150625}

[[1001]{lang="EN-US"}]{#struct_0_x2079_20553_1786516733}

[[idle]{lang="EN-US"}]{#struct_0_x2079_20553_x1773903867}[（空闲）]{style="font-family:宋体"}

[[1001]{lang="EN-US"}]{#struct_0_x2079_20553_x835400178}

[[1001]{lang="EN-US"}]{#struct_0_x2079_20553_x46931304}

[[seizing]{lang="EN-US"}]{#struct_0_x2079_20553_103251640}[（占用）]{style="font-family:宋体"}

[[0001]{lang="EN-US"}]{#struct_0_x2079_20553_x1184486590}

[[0001]{lang="EN-US"}]{#struct_0_x2079_20553_x1631656183}

[[seizing-ack]{lang="EN-US"}]{#struct_0_x2079_20553_x835465714}[（占用确认）]{style="font-family:宋体"}

[[1101]{lang="EN-US"}]{#struct_0_x2079_20553_328899467}

[[1101]{lang="EN-US"}]{#struct_0_x2079_20553_132792380}

[[release-guard]{lang="EN-US"}]{#struct_0_x2079_20553_1525649546}[（释放监护）]{style="font-family:宋体"}

[[1001]{lang="EN-US"}]{#struct_0_x2079_20553_1516457228}

[[1001]{lang="EN-US"}]{#struct_0_x2079_20553_x834482674}

[ ]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1225077810}

[[R2]{lang="EN-US"}]{#struct_0_x2079_20553_x2030973961}[信令视图]{style="font-family:宋体"}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1278038258}

[**[answer]{lang="EN-US"}**]{#struct_0_x2079_20553_433426482}[：应答信号。]{style="font-family:宋体"}

[**[blocking]{lang="EN-US"}**]{#struct_0_x2079_20553_1100426736}[：闭塞信号。]{style="font-family:宋体"}

[**[clear-back]{lang="EN-US"}**]{#struct_0_x2079_20553_1603407005}[：后向拆线信号。]{style="font-family:宋体"}

[**[clear-forward]{lang="EN-US"}**]{#struct_0_x2079_20553_x325484234}[：前向拆线信号。]{style="font-family:宋体"}

[**[idle]{lang="EN-US"}**]{#struct_0_x2079_20553_x834548210}[：空闲信号。]{style="font-family:宋体"}

[**[seizing]{lang="EN-US"}**]{#struct_0_x2079_20553_1474529101}[：占用信号。]{style="font-family:宋体"}

[**[seizing-ack]{lang="EN-US"}**]{#struct_0_x2079_20553_x589227279}[：占用确认信号。]{style="font-family:宋体"}

[**[release-guard]{lang="EN-US"}**]{#struct_0_x2079_20553_x613113325}[：后向释放监护信号。]{style="font-family:宋体"}

[**[receive]{lang="EN-US"}**]{#struct_0_x2079_20553_x937855926}[：接收信号。]{style="font-family:宋体"}

[**[transmit]{lang="EN-US"}**]{#struct_0_x2079_20553_775724050}[：发送信号。]{style="font-family:宋体"}

[*[ABCD]{lang="EN-US"}*]{#struct_0_x2079_20553_x1971909816}[：线路信号的比特值，每位的取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[或]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1487199812}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1396488425}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x835006961}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1555298423}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_2117585448}[配置接收的空闲信号的比特值为]{style="font-family:宋体"}[1101]{lang="EN-US"}[，发送的空闲信号的比特值为]{style="font-family:宋体"}[1011]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_951342748}

[\[Sysname\] controller e1 ]{lang="EN-US"}[2/4/1]{lang="DA"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] timeslot-set 0 timeslot-list 1-31 signal r2]{lang="EN-US"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] cas 0]{lang="EN-US"}

[\[Sysname-cas ]{lang="EN-US"}[2/4/1]{lang="DA"}[:0\] dl-bits idle receive 1101]{lang="EN-US"}

[\[Sysname-cas ]{lang="EN-US"}[2/4/1]{lang="DA"}[:0\] dl-bits idle transmit 1011]{lang="EN-US"}

::: {#-484764389 .myid}
[]{#_Toc404794494}[]{#struct_0_x2079_20553_514823899}[]{#_Toc316027031}[]{#_Toc294166672}[]{#_Toc262031000}[]{#_Toc135295484}[]{#_Toc130097133}[]{#_Toc129160853}[]{#_Toc47776192}

**语音用户线 \-- 数字语音用户线 \-- dtmf enable**

------------------------------------------------------------------------

[**[dtmf]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_9820147}[命令用来配置采用]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[方式发送]{style="font-family:宋体"}[/]{lang="EN-US"}[接收号码。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **dtmf** **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_x235360143}[用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x835072497}

[**[dtmf]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_x81147172}

[**[undo]{lang="EN-US"}**[ **dtmf** **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_875388420}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x2086113995}

[[采用多频互控方式发送]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2079_20553_1931702214}[接收号码信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1203700239}

[[R2]{lang="EN-US"}]{#struct_0_x2079_20553_803659047}[信令视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_2025926236}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x835138033}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1645574425}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1421878050}

[[R2]{lang="EN-US"}]{#struct_0_x2079_20553_x1272923563}[协议规定可以使用两种方式发送或接收号码。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MFC]{lang="EN-US"}]{#struct_0_x2079_20553_x168837992}[（]{style="font-family:宋体"}[Multi-Frequency Compelled]{lang="EN-US"}[，多频互控）方式，出局端和入局端之间通过记发器信令来传递号码信息（包括主叫号码、线路信息以及计费业务等信息），整个记发器交互过程由两端交替四个节拍来完成信息交互。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DTMF]{lang="EN-US"}]{#struct_0_x2079_20553_1292390924}[方式：出局端仅将被叫号码一位一位地发送给入局端，不需要入局端回复任何确认信号。]{style="font-family:宋体"}

[[DTMF]{lang="EN-US"}]{#struct_0_x2079_20553_x66955054}[方式方式相对于]{style="font-family:宋体"}[MFC]{lang="EN-US"}[方式而言，双方接续的速度要快，但传递的信息较少。]{style="font-family:宋体"}

[[在呼叫两端设备上应配置相同的方式发送]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2079_20553_1564090664}[接收号码，否则无法建立呼叫。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x991603759}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x835203569}[配置采用]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[方式发送]{style="font-family:宋体"}[/]{lang="EN-US"}[接收号码。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x848406906}

[\[Sysname\] controller e1 ]{lang="EN-US"}[2/4/1]{lang="DA"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] timeslot-set 0 timeslot-list 1-31 signal r2]{lang="EN-US"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] cas 0]{lang="EN-US"}

[\[Sysname-cas ]{lang="EN-US"}[2/4/1]{lang="DA"}[:0\] dtmf enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1166497196}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer]{lang="EN-US"}**[ **dtmf-delay**]{lang="EN-US"}]{#struct_0_x2079_20553_x856128628}
:::

::: {#683172444 .myid}
[]{#_Toc404794495}[]{#struct_0_x2079_20553_x1302882596}[]{#_Toc316027048}[]{#_Toc61260455}

**语音用户线 \-- 数字语音用户线 \-- final-callednum enable**

------------------------------------------------------------------------

[**[final-callednum]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_1563257559}[命令用来配置出局端发送被叫号码后，必须给入局端发送号码终结信号。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **final-callednum** **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_x485850033}[命令用来配置出局端发送被叫号码后，不会向入局端发送号码终结信号。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x835269105}

[**[final-callednum]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_1863651886}

[**[undo]{lang="EN-US"}**[ **final-callednum** **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_1352452141}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1287207763}

[[出局端发送被叫号码后，不会向入局端发送号码终结信号。]{style="font-family:宋体"}]{#struct_0_x2079_20553_x435497593}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_320439497}

[[R2]{lang="EN-US"}]{#struct_0_x2079_20553_x1330975378}[信令视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1767872344}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x835334641}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1114705866}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x848207205}

[[一些国家的]{style="font-family:宋体"}[R2]{lang="EN-US"}]{#struct_0_x2079_20553_x354891355}[记发器信令，会在发送完被叫号码后再发送号码终结信号，以表示被叫号码已经发送完毕，在这种情况下可使用]{style="font-family:宋体"}**[final-callednum]{lang="EN-US"}**[命令来适配这种信令交互方式。当入局端收到号码终结信号后，将不再请求被叫号码。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x417563027}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x1826655061}[配置出局端发送被叫号码后，必须给入局端发送号码终结信号。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_676593631}

[\[Sysname\] controller e1 ]{lang="EN-US"}[2/4/1]{lang="DA"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] timeslot-set 0 timeslot-list 1-31 signal r2]{lang="EN-US"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] cas 0]{lang="EN-US"}

[\[Sysname-cas ]{lang="EN-US"}[2/4/1]{lang="DA"}[:0\] final-callednum enable]{lang="EN-US"}
:::

::: {#-1857735484 .myid}
[]{#_Toc404794496}[]{#struct_0_x2079_20553_811594384}[]{#_Toc316027047}[]{#_Toc61260457}

**语音用户线 \-- 数字语音用户线 \-- group-b enable**

------------------------------------------------------------------------

[**[group-b]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_x835400177}[命令用来配置使用]{style="font-family:宋体"}[B]{lang="EN-US"}[组阶段信号完成记发器交互过程。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **group-b** **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_x47390056}[命令用来取消使用]{style="font-family:宋体"}[B]{lang="EN-US"}[组阶段信号完成记发器交互过程。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x899284258}

[**[group-b]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_128382954}

[**[undo]{lang="EN-US"}**[ **group-b** **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_x577288655}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x523412223}

[[使用]{style="font-family:宋体"}[B]{lang="EN-US"}]{#struct_0_x2079_20553_502917775}[组阶段信号完成记发器交互过程。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_188788255}

[[R2]{lang="EN-US"}]{#struct_0_x2079_20553_x835465713}[信令视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_329227147}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x61088949}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1467482982}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_239221894}

[[由于一些国家]{style="font-family:宋体"}[R2]{lang="EN-US"}]{#struct_0_x2079_20553_x619206898}[记发器信令不支持]{style="font-family:宋体"}[B]{lang="EN-US"}[组阶段信号交互过程，在这种情况下，可以使用]{style="font-family:宋体"}**[undo group-b]{lang="EN-US"}**[命令来禁止]{style="font-family:宋体"}[B]{lang="EN-US"}[组交互过程。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_913423145}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x1163215283}[配置使用]{style="font-family:宋体"}[B]{lang="EN-US"}[组信号完成记发器交互过程。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x834482673}

[\[Sysname\] controller e1 ]{lang="EN-US"}[2/4/1]{lang="DA"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] timeslot-set 0 timeslot-list 1-31 signal r2]{lang="EN-US"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] cas 0]{lang="EN-US"}

[\[Sysname-cas ]{lang="EN-US"}[2/4/1]{lang="DA"}[:0\] group-b enable]{lang="EN-US"}
:::

::: {#-1502834408 .myid}
[]{#_Toc404794497}[]{#struct_0_x2079_20553_x1225536562}[]{#_Toc316027054}[]{#_Toc61260458}

**语音用户线 \-- 数字语音用户线 \-- line**

------------------------------------------------------------------------

[**[line]{lang="EN-US"}**]{#struct_0_x2079_20553_655229610}[命令用来将数字语音用户线绑定到指定的语音实体。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **line**]{lang="EN-US"}]{#struct_0_x2079_20553_x1205974105}[命令用来取消]{style="font-family:宋体"}[POTS]{lang="EN-US"}[语音实体与数字语音用户线之间的绑定关系。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1496551905}

[**[line]{lang="EN-US"}**[ *line-number*:\[ *ts-set-number* \| **15** \| **23** \]]{lang="EN-US"}]{#struct_0_x2079_20553_1065643334}

[**[undo]{lang="EN-US"}**[ **line**]{lang="EN-US"}]{#struct_0_x2079_20553_1853600088}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1741628631}

[[POTS]{lang="EN-US"}]{#struct_0_x2079_20553_x834548209}[语音实体与数字语音用户线没有绑定关系。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1473939276}

[[POTS]{lang="EN-US"}]{#struct_0_x2079_20553_1498618480}[语音实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x989219941}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1750209543}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1242606189}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1035525347}

[*[line-number]{lang="EN-US"}*]{#struct_0_x2079_20553_x924070547}[：]{style="font-family:宋体"}[E1/T1]{lang="EN-US"}[语音接口编号。]{style="font-family:宋体"}

[*[ts-set-number]{lang="EN-US"}*]{#struct_0_x2079_20553_x1198849936}[：时隙组的编号。]{style="font-family:宋体"}

[**[15]{lang="EN-US"}**]{#struct_0_x2079_20553_x835006964}[：将]{style="font-family:宋体"}[E1]{lang="EN-US"}[语音接口的时隙捆绑为]{style="font-family:宋体"}[ISDN PRI]{lang="EN-US"}[组后，系统生成的编号。]{style="font-family:宋体"}

[**[23]{lang="EN-US"}**]{#struct_0_x2079_20553_1555626103}[：将]{style="font-family:宋体"}[T1]{lang="EN-US"}[语音接口的时隙捆绑为]{style="font-family:宋体"}[ISDN PRI]{lang="EN-US"}[组后，系统生成的编号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x509384404}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x1613184116}[将数字语音用户线绑定到指定的语音实体]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_362312627}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 10 pots]{lang="EN-US"}

[\[Sysname-voice-dial-entity10\] line ]{lang="EN-US"}[2/4/1]{lang="DA"}[:1]{lang="EN-US"}
:::

::: {#-355565768 .myid}
[]{#_Toc404794498}[]{#struct_0_x2079_20553_x1748155903}[]{#_Toc316027039}

**语音用户线 \-- 数字语音用户线 \-- metering enable**

------------------------------------------------------------------------

[**[metering]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_167163067}[命令用来配置开启计次信号处理功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **metering** **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_x835072500}[命令用来关闭计次信号的处理功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1875495653}

[**[metering]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_x1800826289}

[**[undo]{lang="EN-US"}**[ **metering** **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_267514608}

[[【缺省情况】]{style="font-family:
黑体"}]{#struct_0_x2079_20553_1827790}

[[计次信号处理功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x2079_20553_x863362014}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1306462746}

[[R2]{lang="EN-US"}]{#struct_0_x2079_20553_x2062271956}[信令视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x835138036}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1645377817}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1856959404}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x117353433}

[[如果出局端支持计次信号，在入局端需要开启]{style="font-family:宋体"}**[metering]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_1759736942}[命令，入局端]{style="font-family:宋体"}[主动结束呼叫时会发送强拆信号替代后向拆线信号，表明入局端已主动拆线结束呼叫。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1728014601}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_751591795}[开启计次信号处理功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x835203572}

[\[Sysname\] controller e1 ]{lang="EN-US"}[2/4/1]{lang="DA"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] timeslot-set 0 timeslot-list 1-31 signal r2]{lang="EN-US"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] cas 0]{lang="EN-US"}

[\[Sysname-cas ]{lang="EN-US"}[2/4/1]{lang="DA"}[:0\] metering enable]{lang="EN-US"}
:::

::: {#1985170617 .myid}
[]{#_Toc404794499}[]{#struct_0_x2079_20553_x848996731}[]{#_Toc316027027}[]{#_Toc294166660}[]{#_Toc262030988}

**语音用户线 \-- 数字语音用户线 \-- mode**

------------------------------------------------------------------------

[**[mode]{lang="EN-US"}**]{#struct_0_x2079_20553_x1486268912}[命令用来配置]{style="font-family:宋体"}[R2]{lang="EN-US"}[信令标准。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **mode**]{lang="EN-US"}]{#struct_0_x2079_20553_80126768}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_256958309}

[**[mode]{lang="FR"}**]{#struct_0_x2079_20553_x125983433}[ *zone-name* \[ **default-standard** \]]{lang="FR"}

[**[undo]{lang="FR"}**]{#struct_0_x2079_20553_626024333}[ **mode**]{lang="FR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x835269108}

[[使用]{style="font-family:宋体"}[ITU-T]{lang="EN-US"}]{#struct_0_x2079_20553_1863455278}[标准。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_530225740}

[[R2]{lang="EN-US"}]{#struct_0_x2079_20553_x1794805511}[信令视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:
黑体"}]{#struct_0_x2079_20553_5523438}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1073428357}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x335770049}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1440604850}

[*[zone-name]{lang="FR"}*]{#struct_0_x2079_20553_x955551453}[：国家或地区名称。取值如下：]{style="font-family:宋体"}

[**[argentina]{lang="EN-US"}**]{#struct_0_x2079_20553_x835334644}[：使用阿根廷的]{style="font-family:宋体"}[R2]{lang="EN-US"}[信令标准。]{style="font-family:宋体"}

[**[australia]{lang="EN-US"}**]{#struct_0_x2079_20553_1114902474}[：使用澳大利亚的]{style="font-family:宋体"}[R2]{lang="EN-US"}[信令标准。]{style="font-family:宋体"}

[**[bengal]{lang="EN-US"}**]{#struct_0_x2079_20553_686430923}[：使用孟加拉国的]{style="font-family:宋体"}[R2]{lang="EN-US"}[信令标准。]{style="font-family:宋体"}

[**[brazil]{lang="EN-US"}**]{#struct_0_x2079_20553_1632044392}[：使用巴西的]{style="font-family:宋体"}[R2]{lang="EN-US"}[信令标准。]{style="font-family:宋体"}

[**[china]{lang="EN-US"}**]{#struct_0_x2079_20553_719930023}[：使用中国的]{style="font-family:宋体"}[R2]{lang="EN-US"}[信令标准。]{style="font-family:宋体"}

[**[custom]{lang="EN-US"}**]{#struct_0_x2079_20553_1372602053}[：使用用户自定义的]{style="font-family:宋体"}[R2]{lang="EN-US"}[信令模式。]{style="font-family:宋体"}

[**[hongkong]{lang="EN-US"}**]{#struct_0_x2079_20553_989797878}[：使用香港的]{style="font-family:宋体"}[R2]{lang="EN-US"}[信令标准。]{style="font-family:宋体"}

[**[india]{lang="EN-US"}**]{#struct_0_x2079_20553_1545982654}[：使用印度的]{style="font-family:宋体"}[R2]{lang="EN-US"}[信令标准。]{style="font-family:宋体"}

[**[indonesia]{lang="EN-US"}**]{#struct_0_x2079_20553_x835400180}[：使用印度尼西亚的]{style="font-family:宋体"}[R2]{lang="EN-US"}[信令标准。]{style="font-family:宋体"}

[**[itu-t]{lang="EN-US"}**]{#struct_0_x2079_20553_x47455589}[：使用]{style="font-family:宋体"}[ITU-T]{lang="EN-US"}[制定的]{style="font-family:宋体"}[R2]{lang="EN-US"}[信令标准。]{style="font-family:宋体"}

[**[korea]{lang="EN-US"}**]{#struct_0_x2079_20553_x1763352518}[：使用韩国的]{style="font-family:宋体"}[R2]{lang="EN-US"}[信令标准。]{style="font-family:宋体"}

[**[malaysia]{lang="EN-US"}**]{#struct_0_x2079_20553_2076809144}[：使用马来西亚的]{style="font-family:宋体"}[R2]{lang="EN-US"}[信令标准。]{style="font-family:宋体"}

[**[mexico]{lang="EN-US"}**]{#struct_0_x2079_20553_x31322609}[：使用墨西哥的]{style="font-family:宋体"}[R2]{lang="EN-US"}[信令标准。]{style="font-family:宋体"}

[**[newzealand]{lang="EN-US"}**]{#struct_0_x2079_20553_x1681867992}[：使用新西兰的]{style="font-family:宋体"}[R2]{lang="EN-US"}[信令标准。]{style="font-family:宋体"}

[**[singapore]{lang="EN-US"}**]{#struct_0_x2079_20553_1684249955}[：使用新加坡的]{style="font-family:宋体"}[R2]{lang="EN-US"}[信令标准。]{style="font-family:宋体"}

[**[thailand]{lang="EN-US"}**]{#struct_0_x2079_20553_1011959675}[：使用泰国的]{style="font-family:宋体"}[R2]{lang="EN-US"}[信令标准。]{style="font-family:宋体"}

[**[default-standard]{lang="EN-US"}**]{#struct_0_x2079_20553_x1222822850}[：按照配置的国家标准初始]{style="font-family:宋体"}[R2]{lang="EN-US"}[信令标准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x835465716}

[[由于不同国家和地区可能有各自的]{style="font-family:宋体"}[R2]{lang="EN-US"}]{#struct_0_x2079_20553_329030539}[信令标准，为了能和不同国家或地区的设备进行]{style="font-family:宋体"}[R2]{lang="EN-US"}[信令互通，需要适配国家和地区模式。如果采用]{style="font-family:宋体"}**[custom]{lang="EN-US"}**[模式，用户可以自行设定]{style="font-family:宋体"}[R2]{lang="EN-US"}[信令中的特定信令交互流程和信号值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_424914340}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_1722202583}[配置采用新加坡的]{style="font-family:宋体"}[R2]{lang="EN-US"}[信令标准。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_1538989391}

[\[Sysname\] controller e1 ]{lang="EN-US"}[2/4/1]{lang="DA"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] timeslot-set 0 timeslot-list 1-31 signal r2]{lang="EN-US"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] cas 0]{lang="EN-US"}

[\[Sysname-cas ]{lang="EN-US"}[2/4/1]{lang="DA"}[:0\] mode singapore]{lang="EN-US"}
:::

::: {#1343495305 .myid}
[]{#_Toc404794500}[]{#struct_0_x2079_20553_942490679}

**语音用户线 \-- 数字语音用户线 \-- pcm**

------------------------------------------------------------------------

[**[pcm]{lang="EN-US"}**]{#struct_0_x2079_20553_977365396}[命令用来配置信号量化时使用的对数压扩律。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **pcm**]{lang="EN-US"}]{#struct_0_x2079_20553_x834482676}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1225208882}

[**[pcm]{lang="EN-US"}**[ { **a-law** \| **u-law** }]{lang="EN-US"}]{#struct_0_x2079_20553_x948845572}

[**[undo]{lang="EN-US"}**[ **pcm**]{lang="EN-US"}]{#struct_0_x2079_20553_x1747405826}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_467266117}

[[E1]{lang="EN-US"}]{#struct_0_x2079_20553_x629298129}[语音接口的缺省值为]{style="font-family:宋体"}[a-law]{lang="EN-US"}[，]{style="font-family:宋体"}[T1]{lang="EN-US"}[语音接口的缺省值为]{style="font-family:宋体"}[u-law]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1070684789}

[[数字语音用户线视图]{style="font-family:宋体"}]{#struct_0_x2079_20553_669852130}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x780417593}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x834548212}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1474398029}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x213348268}

[**[a-law]{lang="EN-US"}**]{#struct_0_x2079_20553_1633318682}[：对数压扩律]{style="font-family:宋体"}[A]{lang="EN-US"}[律，中国、欧洲、非洲和南美等国家使用。]{style="font-family:宋体"}

[**[u-law]{lang="EN-US"}**]{#struct_0_x2079_20553_1836169741}[：对数压扩律]{style="font-family:宋体"}[µ]{lang="EN-US"}[律，美国使用。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1417919171}

[[使用对数压扩律对信号进行非均匀量化，可以减少噪声，提高信噪比，保证语音质量。]{style="font-family:宋体"}]{#struct_0_x2079_20553_592142201}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1412172949}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x835006963}[配置信号量化时使用]{style="font-family:宋体"}[µ]{lang="EN-US"}[律进行压扩。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_1555167351}

[\[Sysname\] subscriber-line ]{lang="EN-US"}[2/4/1]{lang="DA"}[:0]{lang="EN-US"}

[\[Sysname-subscriber-line]{lang="EN-US"}[2/4/1]{lang="DA"}[:0\] pcm u-law]{lang="EN-US"}
:::

::: {#-1799870332 .myid}
[]{#_Toc404794501}[]{#struct_0_x2079_20553_1447556279}[]{#_Toc316027037}

**语音用户线 \-- 数字语音用户线 \-- re-answer enable**

------------------------------------------------------------------------

[**[re-answer]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_622167948}[命令用来配置出局端开启再应答功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **re-answer** **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_2128621216}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1580360643}

[**[re-answer]{lang="EN-US"}**[ **enable** ]{lang="EN-US"}]{#struct_0_x2079_20553_1985671587}

[**[undo]{lang="EN-US"}**[ **re-answer** **enable** ]{lang="EN-US"}]{#struct_0_x2079_20553_473295827}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x835072499}

[[出局端的再应答功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x2079_20553_x81278244}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x385291898}

[[R2]{lang="EN-US"}]{#struct_0_x2079_20553_x141707046}[信令视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1295267226}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1817555964}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1626694221}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1881891119}

[[一些国家的]{style="font-family:宋体"}[R2]{lang="EN-US"}]{#struct_0_x2079_20553_x593302780}[信令需要支持再应答功能。再应答功能是指，当入局端发出后向拆线信号后，出局端不立即拆线，而是继续保持呼叫状态。如果出局端在一定时间内收到入局端发送的应答线路信号，则继续呼叫通话过程，否则就在超时后拆除呼叫。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x835138035}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x1645181209}[配置出局端支持再应答功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_843627257}

[\[Sysname\] controller e1 ]{lang="EN-US"}[2/4/1]{lang="DA"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] timeslot-set 0 timeslot-list 1-31 signal r2]{lang="EN-US"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] cas 0]{lang="EN-US"}

[\[Sysname-cas ]{lang="EN-US"}[2/4/1]{lang="DA"}[:0\] re-answer enable]{lang="EN-US"}
:::

::: {#-2141350785 .myid}
[]{#_Toc404794502}[]{#struct_0_x2079_20553_968562715}[]{#_Toc316027050}[]{#_Toc61260462}

**语音用户线 \-- 数字语音用户线 \-- register-value**

------------------------------------------------------------------------

[**[register-value]{lang="EN-US"}**]{#struct_0_x2079_20553_159380133}[命令用来配置记发器信令的信号值。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **register-value**]{lang="EN-US"}]{#struct_0_x2079_20553_x1583750388}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1150511085}

[**[register-value]{lang="EN-US"}**[ { **billingcategory** \| **callcreate-in-groupa** \| **callingcategory** \| **congestion** \| **demand-refused** \| **digit-end** \| **null-number** \| **req-billingcategory** \| **req-callednum-and-switchgroupa** \| **req-callingcategory** \| **req-currentcallednum-in-groupc** \| **req-currentdigit** \| **req-firstcallednum-in-groupc** \| **req-firstcallingnum** \| **req-firstdigit** \| **req-lastfirstdigit** \| **req-lastseconddigit** \| **req-lastthirddigit** \| **req-nextcallednum** \| **req-nextcallingnum** \| **req-switch-groupb** \| **subscriber-abnormal** \| **subscriber-busy** \| **subscriber-charge** \| **subscriber-idle** } *value*]{lang="EN-US"}]{#struct_0_x2079_20553_x835203571}

[**[undo]{lang="EN-US"}**[ **register-value** { **billingcategory** \| **callcreate-in-groupa** \| **callingcategory** \| **congestion** \| **demand-refused** \| **digit-end** \| **null-number** \| **req-billingcategory** \| **req-callednum-and-switchgroupa** \| **req-callingcategory** \| **req-currentcallednum-in-groupc** \| **req-currentdigit** \| **req-firstcallednum-in-groupc** \| **req-firstcallingnum** \| **req-firstdigit** \| **req-nextcallednum** \| **req-nextcallingnum** \| **req-lastfirstdigit** \| **req-lastseconddigit** \| **req-lastthirddigit** \| **req-nextcallednum** \| **req-nextcallingnum** \| **req-specialsignal** \| **req-switch-groupb** \| **subscriber-abnormal** \| **subscriber-busy** \| **subscriber-charge** \| **subscriber-idle** }]{lang="EN-US"}]{#struct_0_x2079_20553_x848931195}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1561691735}

[[记发器信令的信号]{style="font-family:宋体"}]{#struct_0_x2079_20553_x1117665245}[缺省]{style="font-family:宋体"}[值]{style="font-family:宋体"}[和]{style="font-family:宋体"}[R2]{lang="EN-US"}[信令标准（使用]{style="font-family:宋体"}**[mode]{lang="EN-US"}**[命令设置）]{style="font-family:宋体"}[有关。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_945094224}

[[R2]{lang="EN-US"}]{#struct_0_x2079_20553_x1631233328}[信令视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_264135690}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_486898447}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x835269107}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1863782958}

[**[billingcategory]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x2079_20553_1761361062}[：计费业务类别信号值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。用于配置]{style="font-family:宋体"}[R2]{lang="EN-US"}[信令的]{style="font-family:宋体"}[KA]{lang="EN-US"}[信号，该信号提供本次呼叫的计费种类（定期、立即、免费等）和用户等级（普通、优先）两种信息。]{style="font-family:宋体"}

[**[callcreate-in-groupa]{lang="EN-US"}***[ value]{lang="EN-US"}*]{#struct_0_x2079_20553_1463077003}[：直接建立呼叫信号的信号值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[callingcategory]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x2079_20553_1298433033}[：主叫业务类别信号值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。用于配置]{style="font-family:宋体"}[R2]{lang="EN-US"}[信令中的]{style="font-family:宋体"}[KD]{lang="EN-US"}[信号，即呼叫业务类别，用于标识是否能插入或强拆市话，或能否被插入或强拆市话。]{style="font-family:宋体"}

[**[congestion]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x2079_20553_682228313}[：拥塞信号值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[demand-refused]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x2079_20553_1891267561}[：请求被拒绝信号值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[digit-end]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x2079_20553_x88158836}[：号码结束信号值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[null-number]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x2079_20553_996122613}[：空号信号值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[req-billingcategory]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x2079_20553_x835334643}[：请求计费业务类别信号值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[req-callednum-and-switchgroupa]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x2079_20553_1114574794}[：请求后一位被叫号码并且转到]{style="font-family:宋体"}[A]{lang="EN-US"}[组阶段的信号值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[req-callingcategory]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x2079_20553_1824970487}[：请求主叫业务类别信号值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[req-currentcallednum-in-groupc]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x2079_20553_963064513}[：在]{style="font-family:宋体"}[C]{lang="EN-US"}[组状态下请求当前位被叫号码的信号值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[req-currentdigit]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x2079_20553_1632627576}[：请求当前号码信号值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[req-firstcallednum-in-groupc]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x2079_20553_x1998014718}[：在]{style="font-family:宋体"}[C]{lang="EN-US"}[组状态下请求第一位被叫号码的信号值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[req-firstcallingnum]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x2079_20553_x1059761468}[：开始请求主叫号码信号值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[req-firstdigit]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x2079_20553_x1866760531}[：请求第一位号码信号值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[req-lastfirstdigit]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x2079_20553_x835400179}[：请求前一位号码信号值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[req-lastseconddigit]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x2079_20553_x46996840}[：请求前二位号码信号值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[req-lastthirddigit]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x2079_20553_x612205359}[：请求前三位号码信号值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[req-nextcallednum]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x2079_20553_x1378734136}[：请求后一位被叫号码信号值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[req-nextcallingnum]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x2079_20553_x1648737549}[：请求后一位主叫号码信号值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[req-switch-groupb]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x2079_20553_x1976313432}[：请求切换到]{style="font-family:宋体"}[B]{lang="EN-US"}[组信号值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[subscriber-abnormal]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x2079_20553_x1830452538}[：表示用户线异常的信号值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[subscriber-busy]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x2079_20553_x1732301071}[：被叫用户线忙信号值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[subscriber-charge]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x2079_20553_729761609}[：表示用户线空闲（并需要计费）的信号值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[subscriber-idle]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x2079_20553_x835465715}[：被叫用户线空闲信号值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。用于配置]{style="font-family:宋体"}[R2]{lang="EN-US"}[信令中的]{style="font-family:宋体"}[KB]{lang="EN-US"}[信号，即被叫用户线状态（如空闲等）。实际应用时必须确保两端的]{style="font-family:宋体"}[KB]{lang="EN-US"}[值相同，否则即便被叫空闲，呼叫也可能无法正常建立。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_328833931}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[记发器信令主要用于本端通过发送指定的请求信号，从而让对端发送相应的响应信号。]{style="font-family:宋体"}]{#struct_0_x2079_20553_x990167469}[例如在入局端配置]{lang="EN-US" style="font-family:宋体"}**[register-value]{lang="EN-US"}**[ **callingcategory** *value*]{lang="EN-US"}[，入局端发送指定信号来请求出局端发送主叫业务类别。当配置信号值为]{lang="EN-US" style="font-family:宋体"}[16]{lang="EN-US"}[时，表明不存在相应信号功能。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如无特殊需要，请使用缺省值。]{style="font-family:宋体"}]{#struct_0_x2079_20553_1263901239}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1862584127}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x242539117}[在出局端配置请求主叫业务类别信号值为]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_145959587}

[\[Sysname\] controller e1 ]{lang="EN-US"}[2/4/1]{lang="DA"}

[\[Sysname-E1 ]{lang="DA"}[2/4/1]{lang="DA"}[\] timeslot-set 0 timeslot-list 1-31 signal r2]{lang="DA"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] cas 0]{lang="EN-US"}

[\[Sysname-cas ]{lang="EN-US"}[2/4/1]{lang="DA"}[:0\] register-value req-callingcategory 7]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x834482675}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mode]{lang="EN-US"}**]{#struct_0_x2079_20553_x1225143346}
:::

::: {#1589070697 .myid}
[]{#_Toc404794503}[]{#struct_0_x2079_20553_458716787}

**语音用户线 \-- 数字语音用户线 \-- renew**

------------------------------------------------------------------------

[**[renew]{lang="EN-US"}**]{#struct_0_x2079_20553_x58212387}[命令用来配置]{style="font-family:宋体"}[C]{lang="EN-US"}[、]{style="font-family:宋体"}[D]{lang="EN-US"}[信号位的比特值。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **renew**]{lang="EN-US"}]{#struct_0_x2079_20553_1819201480}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x54161212}

[**[renew]{lang="EN-US"}**[ *ABCD*]{lang="EN-US"}]{#struct_0_x2079_20553_x33150889}

[**[undo]{lang="EN-US"}**[ **renew**]{lang="EN-US"}]{#struct_0_x2079_20553_x268597419}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1005146467}

[[缺省值和]{style="font-family:宋体"}[R2]{lang="EN-US"}]{#struct_0_x2079_20553_x834548211}[信令标准（使用]{style="font-family:宋体"}**[mode]{lang="EN-US"}**[命令设置）有关。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1474463565}

[[R2]{lang="EN-US"}]{#struct_0_x2079_20553_1703389468}[信令视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x560054911}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1249440460}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_159269712}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x459748093}

[*[ABCD]{lang="EN-US"}*]{#struct_0_x2079_20553_x1836476531}[：表示]{style="font-family:宋体"}[A]{lang="EN-US"}[、]{style="font-family:宋体"}[B]{lang="EN-US"}[、]{style="font-family:宋体"}[C]{lang="EN-US"}[、]{style="font-family:
宋体"}[D]{lang="EN-US"}[信号位的比特值，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[或]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_731076981}

[[在]{style="font-family:宋体"}[R2]{lang="EN-US"}]{#struct_0_x2079_20553_800135960}[信令中，]{style="font-family:宋体"}[A]{lang="EN-US"}[和]{style="font-family:宋体"}[B]{lang="EN-US"}[用来传输有效信息，具体的传输信号和设定值无关；]{style="font-family:
宋体"}[C]{lang="EN-US"}[和]{style="font-family:宋体"}[D]{lang="EN-US"}[不传输有效信息，此命令只对]{style="font-family:
宋体"}[C]{lang="EN-US"}[和]{style="font-family:宋体"}[D]{lang="EN-US"}[有意义。]{style="font-family:宋体"}

[[通过此命令可以使]{style="font-family:宋体"}[C]{lang="EN-US"}]{#struct_0_x2079_20553_x1363257529}[、]{style="font-family:宋体"}[D]{lang="EN-US"}[两位的取值适配于各国的线路信令的编码规范，例如对于中国]{style="font-family:
宋体"}[R2]{lang="EN-US"}[信令，]{style="font-family:宋体"}[C]{lang="EN-US"}[、]{style="font-family:宋体"}[D]{lang="EN-US"}[两位是固定取值为]{style="font-family:
宋体"}[1]{lang="EN-US"}[、]{style="font-family:宋体"}[1]{lang="EN-US"}[。但是对于其它大多数国家而言，]{style="font-family:宋体"}[C]{lang="EN-US"}[、]{style="font-family:宋体"}[D]{lang="EN-US"}[位取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[、]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x439336337}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x749668097}[配置]{style="font-family:宋体"}[C]{lang="EN-US"}[和]{style="font-family:宋体"}[D]{lang="EN-US"}[信号位的比特值都为]{style="font-family:
宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_773961328}

[\[Sysname\] controller e1 ]{lang="EN-US"}[2/4/1]{lang="DA"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] timeslot-set 0 timeslot-list 1-31 signal r2]{lang="EN-US"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] cas 0]{lang="EN-US"}

[\[Sysname-cas ]{lang="EN-US"}[2/4/1]{lang="DA"}[:0\] renew 0011]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_834563841}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mode]{lang="EN-US"}**]{#struct_0_x2079_20553_968229366}
:::

::: {#1018102883 .myid}
[]{#_Toc404794504}[]{#struct_0_x2079_20553_731011445}

**语音用户线 \-- 数字语音用户线 \-- reverse**

------------------------------------------------------------------------

[**[reverse]{lang="EN-US"}**]{#struct_0_x2079_20553_1961606633}[命令用来配置线路信号的反转功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **reverse**]{lang="EN-US"}]{#struct_0_x2079_20553_x1511715031}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x730370495}

[**[reverse]{lang="EN-US"}**[ *ABCD*]{lang="EN-US"}]{#struct_0_x2079_20553_x944053688}

[**[undo]{lang="EN-US"}**[ **reverse**]{lang="EN-US"}]{#struct_0_x2079_20553_1654496199}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x866227981}

[[ABCD]{lang="EN-US"}]{#struct_0_x2079_20553_x1661382441}[取值为]{style="font-family:宋体"}[0000]{lang="EN-US"}[，即不启动反转功能。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_730945909}

[[R2]{lang="EN-US"}]{#struct_0_x2079_20553_80945898}[信令视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1169149887}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1969008829}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x2042581258}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1450624785}

[*[ABCD]{lang="EN-US"}*]{#struct_0_x2079_20553_1991796420}[：表示各信号位是否进行反转，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[或]{style="font-family:宋体"}[1]{lang="EN-US"}[，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[时表示该位需要被反转。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_504906116}

[[使用该命令可以在线路信令发送之前和接收之后对]{style="font-family:宋体"}[ABCD]{lang="EN-US"}]{#struct_0_x2079_20553_1449437035}[位进行反转变换，当某位取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[时表示该位需要被反转，即将]{style="font-family:宋体"}[0]{lang="EN-US"}[变为]{style="font-family:宋体"}[1]{lang="EN-US"}[或将]{style="font-family:宋体"}[1]{lang="EN-US"}[变为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_730880373}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x1036937522}[反转]{style="font-family:宋体"}[B]{lang="EN-US"}[和]{style="font-family:宋体"}[D]{lang="EN-US"}[信号位的比特值。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x330324269}

[\[Sysname\] controller e1 ]{lang="EN-US"}[2/4/1]{lang="DA"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] timeslot-set 0 timeslot-list 1-31 signal r2]{lang="EN-US"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] cas 0]{lang="EN-US"}

[\[Sysname-cas ]{lang="EN-US"}[2/4/1]{lang="DA"}[:0\] reverse 0101]{lang="EN-US"}
:::

::: {#-217957211 .myid}
[]{#_Toc404794505}[]{#struct_0_x2079_20553_1706954700}[]{#_Toc316027053}[]{#_Toc61260468}

**语音用户线 \-- 数字语音用户线 \-- select-mode**

------------------------------------------------------------------------

[**[select-mode]{lang="EN-US"}**]{#struct_0_x2079_20553_1123284270}[命令用来配置选路模式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **select-mode**]{lang="EN-US"}]{#struct_0_x2079_20553_1583964599}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x965523267}

[**[select-mode]{lang="EN-US"}**[ { **max** \| **maxpoll** \| **min** \| **minpoll** }]{lang="EN-US"}]{#struct_0_x2079_20553_730814837}

[**[undo]{lang="EN-US"}**[ **select-mode**]{lang="EN-US"}]{#struct_0_x2079_20553_x1473466596}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x2078337242}

[[选路模式为最小选路模式。]{style="font-family:宋体"}]{#struct_0_x2079_20553_x239068241}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1041922429}

[[R2]{lang="EN-US"}]{#struct_0_x2079_20553_x1733444013}[信令视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_631638732}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1951179878}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_730749301}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x2062117660}

[**[max]{lang="EN-US"}**]{#struct_0_x2079_20553_629948737}[：最大选路模式，即从当前可用的时隙中选取编号最大的时隙。]{style="font-family:宋体"}

[**[maxpoll]{lang="EN-US"}**]{#struct_0_x2079_20553_1812574022}[：最大循环选路模式，第一次使用时从当前可用的时隙中选取编号最大的时隙，下一次使用时，按从大到小的顺序依次选择编号比其小且可用的时隙。例如在]{style="font-family:宋体"}[32]{lang="EN-US"}[个时隙中，编号为]{style="font-family:宋体"}[31]{lang="EN-US"}[的时隙和编号为]{style="font-family:宋体"}[29]{lang="EN-US"}[的时隙不可用，则第一次选路时选择编号为]{style="font-family:宋体"}[30]{lang="EN-US"}[的时隙，第二次选路时选择编号为]{style="font-family:宋体"}[28]{lang="EN-US"}[的时隙。]{style="font-family:宋体"}

[**[min]{lang="EN-US"}**]{#struct_0_x2079_20553_x452274452}[：最小选路模式，即从当前可用的时隙中选取编号最小的时隙。]{style="font-family:宋体"}

[**[minpoll]{lang="EN-US"}**]{#struct_0_x2079_20553_1383014262}[：最小循环选路模式，第一次使用时从当前可用的时隙中选编号最小的时隙，下一次使用时，按从小到大的顺序依次选择编号比其大且可用的时隙。例如在]{style="font-family:宋体"}[32]{lang="EN-US"}[个时隙中，编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的时隙和编号为]{style="font-family:宋体"}[3]{lang="EN-US"}[的时隙不可用，则第一次选路时选择编号为]{style="font-family:宋体"}[2]{lang="EN-US"}[的时隙，第二次选路时选择编号为]{style="font-family:宋体"}[4]{lang="EN-US"}[的时隙。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_349850084}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_1659916428}[配置使用最大循环选路模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_730683765}

[\[Sysname\] controller e1 ]{lang="EN-US"}[2/4/1]{lang="DA"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] timeslot-set 0 timeslot-list 1-31 signal r2]{lang="EN-US"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] cas 0]{lang="EN-US"}

[\[Sysname-cas ]{lang="EN-US"}[2/4/1]{lang="DA"}[:0\] select-mode maxpoll]{lang="EN-US"}
:::

::: {#-1437680541 .myid}
[]{#_Toc404794506}[]{#struct_0_x2079_20553_639461696}[]{#_Toc316027040}[]{#_Toc61260467}

**语音用户线 \-- 数字语音用户线 \-- seizure-ack enable**

------------------------------------------------------------------------

[**[seizure-ack]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_1167598386}[命令用来配置出局端要求入局端必须发送占用确认信号。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **seizure-ack** **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_1179627097}[命令用来配置出局端不要求入局端必须发送占用确认信号。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1644004397}

[**[seizure-ack]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_125124433}

[**[undo]{lang="EN-US"}**[ **seizure-ack** **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_836391652}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_731601269}

[[出局端要求入局端发送占用确认信号。]{style="font-family:宋体"}]{#struct_0_x2079_20553_1188233840}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1998848797}

[[R2]{lang="EN-US"}]{#struct_0_x2079_20553_1533391572}[信令视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_731535733}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1793499176}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_961321747}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_579704716}

[[通常情况下，入局端接收到出局端发来的占用信号后会发送占用确认信号。但是有一些国家的]{style="font-family:宋体"}[R2]{lang="EN-US"}]{#struct_0_x2079_20553_345553985}[线路信令编码方案中允许不发送占用确认信号，在这种情况下可使用]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **seizure-ack enable**]{lang="EN-US"}[命令来适配这种信令编码方案。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1615613230}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x1861507312}[配置出局端不要求入局端必须发送占用确认信号。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_731076982}

[\[Sysname\] controller e1 ]{lang="EN-US"}[2/4/1]{lang="DA"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] timeslot-set 0 timeslot-list 1-31 signal r2]{lang="EN-US"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] cas 0]{lang="EN-US"}

[\[Sysname-cas ]{lang="EN-US"}[2/4/1]{lang="DA"}[:0\] undo seizure-ack enable]{lang="EN-US"}
:::

::: {#1136504486 .myid}
[]{#_Toc404794507}[]{#struct_0_x2079_20553_800135957}[]{#_Toc316027029}[]{#_Toc37216715}

**语音用户线 \-- 数字语音用户线 \-- send ringbusy enable**

------------------------------------------------------------------------

[**[send]{lang="EN-US"}**[ **ringbusy** **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_210720584}[命令用来配置入局端向出局端发送忙音信号。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **send** **ringbusy** **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_x1177133526}[命令用来禁止入局端向出局端发送忙音信号。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1482834306}

[**[send]{lang="EN-US"}**[ **ringbusy** **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_x1559017258}

[**[undo]{lang="EN-US"}**[ **send** **ringbusy** **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_x757877883}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_733070039}

[[入局端向出局端发送忙音信号。]{style="font-family:宋体"}]{#struct_0_x2079_20553_2076834505}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_731011446}

[[R2]{lang="EN-US"}]{#struct_0_x2079_20553_1961606634}[信令视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1511387351}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_328151721}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1666855641}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1788312000}

[[如果出局端设备需要播放忙音，可以在入局端设备上执行]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **send** **ringbusy** **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_x221252967}[命令，取消入局端向出局端发送忙音信号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1392241126}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_730945910}[配置入局端向出局端发送忙音信号。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_2037261043}

[\[Sysname\] controller e1 ]{lang="EN-US"}[2/4/1]{lang="DA"}

[\[Sysname-E1 ]{lang="DA"}[2/4/1]{lang="DA"}[\] timeslot-set 0 timeslot-list 1-31 signal r2]{lang="DA"}

[\[Sysname-E1 ]{lang="DA"}[2/4/1]{lang="DA"}[\] cas 0]{lang="DA"}

[\[Sysname-cas ]{lang="DA"}[2/4/1]{lang="DA"}[:0\] send ringbusy enable]{lang="DA"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x678259783}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer]{lang="EN-US"}**]{#struct_0_x2079_20553_x1002182559}
:::

::: {#-1345320708 .myid}
[]{#_Toc404794508}[]{#struct_0_x2079_20553_x38812591}[]{#_Toc316027049}

**语音用户线 \-- 数字语音用户线 \-- special-character**

------------------------------------------------------------------------

[**[special-character]{lang="EN-US"}**]{#struct_0_x2079_20553_x912225425}[命令用来配置特殊字符的记发器信号编码。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **special-character**]{lang="EN-US"}]{#struct_0_x2079_20553_148123594}[命令用来删除已配置的特殊字符的记发器信号编码。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_730880374}

[**[special-character]{lang="EN-US"}**[ *character* *number*]{lang="EN-US"}]{#struct_0_x2079_20553_x1036937515}

[**[undo]{lang="EN-US"}**[ **special-character** *character* *number*]{lang="EN-US"}]{#struct_0_x2079_20553_x1090035764}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_58714629}

[[没有配置特殊字符的记发器信号编码。]{style="font-family:宋体"}]{#struct_0_x2079_20553_1897664000}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x879678761}

[[R2]{lang="EN-US"}]{#struct_0_x2079_20553_x489267733}[信令视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_788832790}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1220756644}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_730814838}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1473466587}

[*[character]{lang="EN-US"}*]{#struct_0_x2079_20553_650480577}[：特殊字符，取值为"]{style="font-family:宋体"}[\#]{lang="EN-US"}[＊]{style="font-family:宋体"}[ABCD]{lang="EN-US"}["中的任意一个字符。]{style="font-family:宋体"}

[*[number]{lang="EN-US"}*]{#struct_0_x2079_20553_x1322758540}[：记发器信号的编码，取值范围为]{style="font-family:宋体"}[11]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x459033578}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[由于一些国家]{lang="EN-US" style="font-family:宋体"}[R2]{lang="EN-US"}]{#struct_0_x2079_20553_x612068399}[信令的记发器前向]{lang="EN-US" style="font-family:宋体"}[I]{lang="EN-US"}[组信号可能会支持如"]{lang="EN-US" style="font-family:宋体"}[\#]{lang="EN-US"}["、"＊"等特殊字符，在这种情况下，可以使用]{lang="EN-US" style="font-family:宋体"}**[special-character]{lang="EN-US"}**[命令为这些特殊字符进行编码。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不同的特殊字符请使用不同的编码。]{style="font-family:宋体"}]{#struct_0_x2079_20553_x607291767}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x160668332}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x6325077}[配置特殊字符]{style="font-family:宋体"}["#"]{lang="EN-US"}[的记发器信号编码为]{style="font-family:宋体"}[11]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_730749302}

[\[Sysname\] controller e1 ]{lang="EN-US"}[2/4/1]{lang="DA"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] timeslot-set 0 timeslot-list 1-31 signal r2]{lang="EN-US"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] cas 0]{lang="EN-US"}

[\[Sysname-cas ]{lang="EN-US"}[2/4/1]{lang="DA"}[:0\] special-character \# 11]{lang="EN-US"}
:::

::: {#-17086221 .myid}
[]{#_Toc404794509}[]{#struct_0_x2079_20553_x2062117661}

**语音用户线 \-- 数字语音用户线 \-- subscriber-line**

------------------------------------------------------------------------

[**[subscriber-line]{lang="EN-US"}**]{#struct_0_x2079_20553_x2098934618}[命令用来进入数字音用户线视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1640668494}

[**[subscriber-line]{lang="EN-US"}**[ *line-number*]{lang="EN-US"}]{#struct_0_x2079_20553_457016891}[：]{style="font-family:宋体"}[{ *ts-set-number* \| **15** \| **23** }]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x120816949}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2079_20553_730683766}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_639461695}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1167598389}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1179692633}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1650909704}

[*[line-number]{lang="EN-US"}*]{#struct_0_x2079_20553_x380670979}[：]{style="font-family:宋体"}[E1/T1]{lang="EN-US"}[语音接口编号。]{style="font-family:宋体"}

[*[ts-set-number]{lang="EN-US"}*]{#struct_0_x2079_20553_x1832041171}[：时隙组编号。]{style="font-family:宋体"}

[**[15]{lang="EN-US"}**]{#struct_0_x2079_20553_x1951386487}[：将]{style="font-family:宋体"}[E1]{lang="EN-US"}[语音接口的时隙捆绑为]{style="font-family:宋体"}[ISDN PRI]{lang="EN-US"}[组后，系统生成的编号。]{style="font-family:宋体"}

[**[23]{lang="EN-US"}**]{#struct_0_x2079_20553_x204133931}[：将]{style="font-family:宋体"}[T1]{lang="EN-US"}[语音接口的时隙捆绑为]{style="font-family:宋体"}[ISDN PRI]{lang="EN-US"}[组后，系统生成的编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_730618230}

[[在]{style="font-family:宋体"}[E1/T1]{lang="EN-US"}]{#struct_0_x2079_20553_1443111183}[语音接口上创建时隙组后，系统会根据当前]{style="font-family:宋体"}[E1]{lang="EN-US"}[语音接口编号和时隙组的组号生成该时隙组对应的数字语音用户线，语音用户线号为"]{style="font-family:宋体"}[E1]{lang="EN-US"}[语音接口号]{style="font-family:宋体"}[:]{lang="EN-US"}[时隙组号"。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[E1]{lang="EN-US"}]{#struct_0_x2079_20553_44611658}[语音接口上配置]{style="font-family:宋体"}[ISDN PRI]{lang="EN-US"}[组后，系统会根据当前]{style="font-family:宋体"}[PRI]{lang="EN-US"}[接口所在]{style="font-family:宋体"}[E1]{lang="EN-US"}[语音接口的编号生成该]{style="font-family:宋体"}[PRI]{lang="EN-US"}[组对应的数字语音用户线，语音用户线号为"]{style="font-family:宋体"}[E1]{lang="EN-US"}[语音接口号]{style="font-family:宋体"}[:**15**]{lang="EN-US"}["。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[T1]{lang="EN-US"}]{#struct_0_x2079_20553_x1789228430}[语音接口上配置]{style="font-family:宋体"}[ISDN PRI]{lang="EN-US"}[组后，系统会根据当前]{style="font-family:宋体"}[PRI]{lang="EN-US"}[接口所在]{style="font-family:宋体"}[T1]{lang="EN-US"}[语音接口的编号生成该]{style="font-family:宋体"}[PRI]{lang="EN-US"}[组对应的数字语音用户线，语音用户线号为"]{style="font-family:宋体"}[T1]{lang="EN-US"}[语音接口号]{style="font-family:宋体"}[:**23**]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x531962969}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x1927754709}[进入数字语音用户线]{style="font-family:宋体"}[2/4/1]{lang="DA"}[:15]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_360559622}

[\[Sysname\]]{lang="EN-US"}[ subscriber-line ]{lang="EN-US"}[2/4/1]{lang="DA"}[:15]{lang="EN-US"}

[\[Sysname-subscriber-line]{lang="EN-US"}[2/4/1]{lang="DA"}[:15\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1872758016}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timeslot-set]{lang="EN-US"}**]{#struct_0_x2079_20553_731601270}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ pri-set]{lang="EN-US"}**]{#struct_0_x2079_20553_x768081303}
:::

::: {#507753927 .myid}
[]{#_Toc404794510}[]{#struct_0_x2079_20553_x221276934}[]{#_Toc325038121}

**语音用户线 \-- 数字语音用户线 \-- tdm-clock**

------------------------------------------------------------------------

[**[tdm-clock]{lang="EN-US"}**]{#struct_0_x2079_20553_x928442499}[命令用来配置]{style="font-family:宋体"}[TDM]{lang="EN-US"}[时钟源。]{style="font-family:宋体"}

[**[undo tdm-clock]{lang="EN-US"}**]{#struct_0_x2079_20553_1250421397}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x717049863}

[**[tdm-clock]{lang="EN-US"}**[ { **internal** \| **line** \[ **primary** \] }]{lang="EN-US"}]{#struct_0_x2079_20553_856097267}

[**[undo tdm-clock]{lang="EN-US"}**]{#struct_0_x2079_20553_x1864214600}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_731535734}

[[E1]{lang="EN-US"}]{#struct_0_x2079_20553_x1793499171}[语音、]{style="font-family:宋体"}[T1]{lang="EN-US"}[语音接口的]{style="font-family:宋体"}[TDM]{lang="EN-US"}[时钟源为]{style="font-family:宋体"}**[internal]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1364606274}

[[E1]{lang="EN-US"}]{#struct_0_x2079_20553_1896943397}[语音]{style="font-family:宋体"}[/T1]{lang="EN-US"}[语音接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x861144642}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1823601449}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x81483723}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x157923395}

[**[internal]{lang="EN-US"}**]{#struct_0_x2079_20553_x742157018}[：]{style="font-family:宋体"}[TDM]{lang="EN-US"}[时钟源为设备内部晶振]{style="font-family:宋体"}[TDM]{lang="EN-US"}[时钟方式，即]{style="font-family:宋体"}[E1]{lang="EN-US"}[或]{style="font-family:宋体"}[T1]{lang="EN-US"}[语音接口从设备内部时钟源获取时钟信息。]{style="font-family:宋体"}**[internal]{lang="EN-US"}**[相当于主时钟模式。]{style="font-family:宋体"}

[**[line]{lang="EN-US"}**]{#struct_0_x2079_20553_731076979}[：]{style="font-family:宋体"}[TDM]{lang="EN-US"}[时钟源为提取线路]{style="font-family:宋体"}[TDM]{lang="EN-US"}[时钟方式，即通过线路获取对端设备的时钟。]{style="font-family:宋体"}**[line]{lang="EN-US"}**[相当于从时钟模式。]{style="font-family:宋体"}

[**[line primary]{lang="EN-US"}**]{#struct_0_x2079_20553_x773842160}[：]{style="font-family:宋体"}[TDM]{lang="EN-US"}[时钟源为优先提取线路]{style="font-family:宋体"}[TDM]{lang="EN-US"}[时钟方式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x859182026}

[[语音]{style="font-family:宋体"}[E1]{lang="EN-US"}]{#struct_0_x2079_20553_1729366222}[、]{style="font-family:宋体"}[T1]{lang="EN-US"}[接口之间进行]{style="font-family:宋体"}[TDM]{lang="EN-US"}[时隙交换时，需要保证不同语音]{style="font-family:宋体"}[E1]{lang="EN-US"}[、]{style="font-family:宋体"}[T1]{lang="EN-US"}[接口在进行]{style="font-family:宋体"}[TDM]{lang="EN-US"}[交换时时钟同步，否则会导致交换数据时出现滑帧、误码等错误。]{style="font-family:宋体"}

[[在设备上插入语音]{style="font-family:宋体"}[E1]{lang="EN-US"}]{#struct_0_x2079_20553_x80196918}[、]{style="font-family:宋体"}[T1]{lang="EN-US"}[板卡后，所有]{style="font-family:宋体"}[SIC]{lang="EN-US"}[语音]{style="font-family:宋体"}[E1]{lang="EN-US"}[或]{style="font-family:宋体"}[SIC]{lang="EN-US"}[语音]{style="font-family:宋体"}[T1]{lang="EN-US"}[板卡合起来是一个子系统，各]{style="font-family:宋体"}[HMIM]{lang="EN-US"}[语音]{style="font-family:宋体"}[E1]{lang="EN-US"}[或]{style="font-family:宋体"}[T1]{lang="EN-US"}[语音板卡是一个单独的子系统。各系统根据命令行接口时钟模式参数的设置情况确定]{style="font-family:宋体"}[TDM]{lang="EN-US"}[时钟源标准：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果子系统所有接口参数均设为]{style="font-family:宋体"}]{#struct_0_x2079_20553_1470630722}**[line]{lang="EN-US"}**[时，子系统采用接口号最小的接口时钟为标准进行]{style="font-family:宋体"}[TDM]{lang="EN-US"}[时隙交换；如果接口号最小的接口]{style="font-family:宋体"}[down]{lang="EN-US"}[掉，子系统则采用接口号次小的接口时钟为标准进行]{style="font-family:宋体"}[TDM]{lang="EN-US"}[时隙交换，依此类推；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果子系统有一个接口设置为]{lang="EN-US" style="font-family:宋体"}**[line primary]{lang="EN-US"}**]{#struct_0_x2079_20553_811218115}[，而其它接口分别为]{lang="EN-US" style="font-family:宋体"}**[line]{lang="EN-US"}**[或]{lang="EN-US" style="font-family:宋体"}**[internal]{lang="EN-US"}**[时，则子系统采用设置为]{lang="EN-US" style="font-family:宋体"}**[line primary]{lang="EN-US"}**[的接口时钟为标准进行]{lang="EN-US" style="font-family:宋体"}[TDM]{lang="EN-US"}[时隙交换；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果子系统的一个接口设置为]{style="font-family:宋体"}]{#struct_0_x2079_20553_405842485}**[line]{lang="EN-US"}**[，其余接口设置为]{style="font-family:宋体"}**[internal]{lang="EN-US"}**[，则子系统采用设置为]{style="font-family:宋体"}**[line]{lang="EN-US"}**[的接口时钟为标准进行]{style="font-family:宋体"}[TDM]{lang="EN-US"}[时隙交换；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每个子系统仅允许一个接口设置为]{lang="EN-US" style="font-family:宋体"}**[line primary]{lang="EN-US"}**]{#struct_0_x2079_20553_731011443}[。]{lang="EN-US" style="font-family:宋体"}

[[本端设备上的子系统确定]{style="font-family:宋体"}[TDM]{lang="EN-US"}]{#struct_0_x2079_20553_1961606639}[时钟原标准后，一定要与对端设备的时钟源匹配。例如如果本端设备的子系统使用]{style="font-family:宋体"}**[line]{lang="EN-US"}**[方式，那么对端设备应该使用]{style="font-family:宋体"}**[internal]{lang="EN-US"}**[方式。如果本端设备的子系统使用]{style="font-family:宋体"}**[internal]{lang="EN-US"}**[方式，那么对端设备应该使用]{style="font-family:宋体"}**[line]{lang="EN-US"}**[方式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1511059671}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_380915279}[配置]{style="font-family:宋体"}[E1]{lang="EN-US"}[语音接口的]{style="font-family:宋体"}[TDM]{lang="EN-US"}[时钟为]{style="font-family:宋体"}**[line]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x1751698932}

[\[Sysname\] controller e1 ]{lang="EN-US"}[2/4/1]{lang="DA"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] tdm-clock line]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x1395191932}[配置]{style="font-family:宋体"}[T1]{lang="EN-US"}[语音接口的]{style="font-family:宋体"}[TDM]{lang="EN-US"}[时钟为]{style="font-family:宋体"}**[line]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x1095488715}

[\[Sysname\] controller T1 ]{lang="EN-US"}[2/4/1]{lang="DA"}

[\[Sysname-T1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] tdm-clock line]{lang="EN-US"}
:::

::: {#-1113860339 .myid}
[]{#struct_0_x2079_20553_730945907}[]{#_Toc294166664}[]{#_Toc262030992}[]{#_Toc135295472}[]{#_Toc404794511}[]{#_Toc316027030}

**语音用户线 \-- 数字语音用户线 \-- timer**

------------------------------------------------------------------------

[**[timer]{lang="EN-US"}**]{#struct_0_x2079_20553_80945900}[命令用来配置播放信号音的超时时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **timer**]{lang="EN-US"}]{#struct_0_x2079_20553_x849589836}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1907698337}

[**[timer]{lang="EN-US"}**[ { **ringback** \| **ringbusy** } *time*]{lang="EN-US"}]{#struct_0_x2079_20553_x1017526147}

[**[undo]{lang="EN-US"}**[ **timer** { **ringback** \| **ringbusy** } ]{lang="EN-US"}]{#struct_0_x2079_20553_x1309801636}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1984531995}

[[播放回铃音的超时时间为]{style="font-family:宋体"}[60000]{lang="EN-US"}]{#struct_0_x2079_20553_x1610988291}[毫秒，播放忙音的超时时间为]{style="font-family:宋体"}[30000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_730880371}

[[R2]{lang="EN-US"}]{#struct_0_x2079_20553_x1036937520}[信令视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1493123683}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_2109951453}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x915502410}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1965615433}

[**[ringback]{lang="EN-US"}**[ *time*]{lang="EN-US"}]{#struct_0_x2079_20553_1739102862}[：播放回铃音的超时时间，取值范围为]{style="font-family:宋体"}[1000]{lang="EN-US"}[～]{style="font-family:宋体"}[90000]{lang="EN-US"}[，单位是毫秒。]{style="font-family:宋体"}

[**[ringbusy]{lang="EN-US"}**[ *time*]{lang="EN-US"}]{#struct_0_x2079_20553_420937271}[：播放忙音的超时时间，取值范围是]{style="font-family:宋体"}[1000]{lang="EN-US"}[～]{style="font-family:宋体"}[90000]{lang="EN-US"}[，单位是毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1903109521}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer]{lang="EN-US"}**[ **ringback**]{lang="EN-US"}]{#struct_0_x2079_20553_730814835}[和]{lang="EN-US" style="font-family:宋体"}**[timer]{lang="EN-US"}**[ **ringbusy**]{lang="EN-US"}[命令对入局端生效。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有开启]{lang="EN-US" style="font-family:宋体"}**[send ringbusy enable]{lang="EN-US"}**]{#struct_0_x2079_20553_x1473466598}[命令后，]{lang="EN-US" style="font-family:宋体"}**[timer ringbusy]{lang="EN-US"}**[命令的设置才能生效。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x559307468}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x802438652}[配置播放回铃音的超时时间为]{style="font-family:宋体"}[10000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_193566269}

[\[Sysname\] controller e1 ]{lang="EN-US"}[2/4/1]{lang="DA"}

[\[Sysname-E1 ]{lang="DA"}[2/4/1]{lang="DA"}[\] timeslot-set 0 timeslot-list 1-31 signal r2]{lang="DA"}

[\[Sysname-E1 ]{lang="FR"}[2/4/1]{lang="DA"}[\] cas 0]{lang="FR"}

[\[Sysname-cas ]{lang="EN-US"}[2/4/1]{lang="DA"}[:0\]]{lang="EN-US"}[ timer ringback 10000]{lang="EN-US"}
:::

::: {#1706405583 .myid}
[]{#_Toc404794512}[]{#struct_0_x2079_20553_95092246}[]{#_Toc316027044}[]{#_Toc243369651}

**语音用户线 \-- 数字语音用户线 \-- timer dl**

------------------------------------------------------------------------

[**[timer]{lang="EN-US"}**[ **dl**]{lang="EN-US"}]{#struct_0_x2079_20553_x1129060477}[命令用来配置线路信号的超时时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **timer** **dl**]{lang="EN-US"}]{#struct_0_x2079_20553_730749299}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1305337791}

[**[timer]{lang="EN-US"}**[ **dl** { **answer** \| **clear-back** \| **clear-forward** \| **re-answer** \| **release-guard** \| **seizing** } *time*]{lang="EN-US"}]{#struct_0_x2079_20553_x380080152}

[**[undo]{lang="EN-US"}**[ **timer** **dl** { **answer** \| **clear-back** \| **clear-forward** \| **re-answer** \| **release-guard** \| **seizing** }]{lang="EN-US"}]{#struct_0_x2079_20553_x317242367}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1881872193}

[[线路信号超时时间的缺省值如下：]{style="font-family:宋体"}]{#struct_0_x2079_20553_730519643}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[等待应答信号（]{style="font-family:宋体"}]{#struct_0_x2079_20553_x1968508034}**[answer]{lang="EN-US"}**[）的超时时间为]{style="font-family:宋体"}[60000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[后向拆线信号（]{lang="EN-US" style="font-family:宋体"}**[clear-back]{lang="EN-US"}**]{#struct_0_x2079_20553_269731977}[）的超时时间为]{lang="EN-US" style="font-family:宋体"}[10000]{lang="EN-US"}[毫秒。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[前向拆线信号（]{lang="EN-US" style="font-family:宋体"}**[clear-forward]{lang="EN-US"}**]{#struct_0_x2079_20553_x2099891692}[）的超时时间为]{lang="EN-US" style="font-family:
宋体"}[10000]{lang="EN-US"}[毫秒。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[再应答信号（]{lang="EN-US" style="font-family:宋体"}**[re-answer]{lang="EN-US"}**]{#struct_0_x2079_20553_730683763}[）的超时时间为]{lang="EN-US" style="font-family:宋体"}[1000]{lang="EN-US"}[毫秒。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[后向释放信号（]{lang="EN-US" style="font-family:宋体"}**[release-guard]{lang="EN-US"}**]{#struct_0_x2079_20553_639461690}[）的超时时间为]{lang="EN-US" style="font-family:
宋体"}[10000]{lang="EN-US"}[毫秒。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[占用信号（]{style="font-family:宋体"}]{#struct_0_x2079_20553_1167598392}**[seizure]{lang="EN-US"}**[）的超时时间为]{style="font-family:宋体"}[1000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1179364954}

[[R2]{lang="EN-US"}]{#struct_0_x2079_20553_x895547501}[信令视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1981061793}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1212748796}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1783002602}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_730618227}

[**[answer]{lang="EN-US"}**[ *time*]{lang="EN-US"}]{#struct_0_x2079_20553_x895540978}[：等待应答信号的超时时间。对于入局端，入局端发送占用确认信号后，入局端应在该时间内回复应答信号。如果入局端没有在该时间内发送应答信号，入局端就拆线。对于出局端，入局端发送应答信号后，出局端开启定时器。出局端应该在该时间内收到应答信号，否则出局端将进行拆线处理。取值范围为]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[120000]{lang="EN-US"}[，单位为毫秒。该参数对出局端和入局端均生效。]{style="font-family:宋体"}

[**[clear-back]{lang="EN-US"}**[ *time*]{lang="EN-US"}]{#struct_0_x2079_20553_1252664841}[：后向拆线信号的超时时间。入局端发送后向拆线信号后，入局端应在该时间间隔内收到出局端回复的前向信号，否则入局端将进行拆线处理。取值范围为]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[60000]{lang="EN-US"}[，单位为毫秒。该参数对入局端生效。]{style="font-family:宋体"}

[**[clear-forward]{lang="EN-US"}**[ *time*]{lang="EN-US"}]{#struct_0_x2079_20553_754537055}[：前向拆线信号的超时时间。出局端发送前向拆线信号后，入局端应在该时间内回复相应的线路信号（如后向拆线或释放监护信号），否则出局端将进行拆线处理。取值范围为]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[60000]{lang="EN-US"}[，单位为毫秒。该参数对出局端生效。]{style="font-family:宋体"}

[**[re-answer]{lang="EN-US"}**[ *time*]{lang="EN-US"}]{#struct_0_x2079_20553_x1852102159}[：再应答信号的超时时间。出局端收到后向拆线信号后，应当在该时间间隔内再次发送应答信号，否则出局端将进行拆线处理。取值范围为]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[60000]{lang="EN-US"}[，单位为毫秒。该参数对出局端生效。]{style="font-family:宋体"}

[**[release-guard]{lang="EN-US"}**[ *time*]{lang="EN-US"}]{#struct_0_x2079_20553_x882548490}[：后向释放信号的超时时间。出局端发送前向拆线信号后，入局端应当在该时间间隔内发送释放监护信号，否则出局端将进行拆线处理。取值范围为]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[60000]{lang="EN-US"}[，单位为毫秒。该参数对出局端生效。]{style="font-family:宋体"}

[**[seizing]{lang="EN-US"}**[ *time*]{lang="EN-US"}]{#struct_0_x2079_20553_1644535804}[：占用信号的超时时间。出局端发送占用信号后，入局端应当在该时间内回复占用确认信号或应答信号，否则出局端将进行拆线处理。取值范围为]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[5000]{lang="EN-US"}[，单位为毫秒。该参数对出局端生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x2126256799}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x373306193}[配置占用信号的超时时间为]{style="font-family:宋体"}[300]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_731601267}

[\[Sysname\] controller e1 ]{lang="EN-US"}[2/4/1]{lang="DA"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] timeslot-set 0 timeslot-list 1-31 signal r2]{lang="EN-US"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] cas 0]{lang="EN-US"}

[\[Sysname-cas ]{lang="EN-US"}[2/4/1]{lang="DA"}[:0\] timer dl seize 300]{lang="EN-US"}
:::

::: {#1470814718 .myid}
[]{#_Toc404794513}[]{#struct_0_x2079_20553_1188233834}[]{#_Toc294166674}[]{#_Toc262031002}[]{#_Toc135295489}[]{#_Toc130097138}[]{#_Toc129160858}[]{#_Toc47776197}[]{#_Toc316027032}

**语音用户线 \-- 数字语音用户线 \-- timer dtmf-delay**

------------------------------------------------------------------------

[**[timer]{lang="EN-US"}**[ **dtmf-delay**]{lang="EN-US"}]{#struct_0_x2079_20553_1999110934}[命令用来配置出局端收到占用确认信号到发送]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号前的延时时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **timer** **dtmf-delay**]{lang="EN-US"}]{#struct_0_x2079_20553_681859213}[命令用来恢复发送]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号的时间间隔为缺省值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x441123422}

[**[timer]{lang="EN-US"}**[ **dtmf-delay** *time*]{lang="EN-US"}]{#struct_0_x2079_20553_185637934}

[**[undo]{lang="EN-US"}**[ **timer** **dtmf-delay**]{lang="EN-US"}]{#struct_0_x2079_20553_731535731}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1793499174}

[[发送]{style="font-family:宋体"}[DTMF]{lang="EN-US"}]{#struct_0_x2079_20553_2124121161}[信号的延时时间为]{style="font-family:宋体"}[50]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_274963347}

[[R2]{lang="EN-US"}]{#struct_0_x2079_20553_1229112064}[信令视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1919017735}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x599347084}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x849241482}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x766671553}

[*[time]{lang="EN-US"}*]{#struct_0_x2079_20553_731076980}[：发送]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号的延时时间，取值范围为]{style="font-family:宋体"}[50]{lang="EN-US"}[～]{style="font-family:宋体"}[10000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_800135959}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[正常情况下，出局端接收到占用确认信号后，可以立刻发送]{style="font-family:宋体"}]{#struct_0_x2079_20553_210720590}[DTMF]{lang="EN-US"}[信号。有时为了配合对端]{style="font-family:宋体"}[PBX]{lang="EN-US"}[交换机的收号，需要在出局端设备上配置此命令，从而在指定的延时时间后，出局端才开始发送]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有开启]{lang="EN-US" style="font-family:宋体"}**[dtmf]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_779181614}[命令后，]{lang="EN-US" style="font-family:宋体"}**[timer]{lang="EN-US"}**[ **dtmf-delay**]{lang="EN-US"}[命令的设置才能生效。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x2017384088}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x1159710282}[配置出局端收到占用确认信号到发送]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号前的延时时间为]{style="font-family:宋体"}[800]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_731011444}

[\[Sysname\] controller e1 ]{lang="EN-US"}[2/4/1]{lang="DA"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] timeslot-set 0 timeslot-list 1-31 signal r2]{lang="EN-US"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] cas 0]{lang="EN-US"}

[\[Sysname-cas ]{lang="EN-US"}[2/4/1]{lang="DA"}[:0\] dtmf enable]{lang="EN-US"}

[\[Sysname-cas ]{lang="EN-US"}[2/4/1]{lang="DA"}[:0\] timer dtmf-delay 800]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1961606632}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dtmf]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x2079_20553_x1511780567}
:::

::: {#2128992037 .myid}
[]{#_Toc404794514}[]{#struct_0_x2079_20553_1080040413}[]{#_Toc316027052}[]{#_Toc61260476}

**语音用户线 \-- 数字语音用户线 \-- timer group-b**

------------------------------------------------------------------------

[**[timer]{lang="EN-US"}**[ **group-b**]{lang="EN-US"}]{#struct_0_x2079_20553_1235253105}[命令用来配置]{style="font-family:宋体"}[B]{lang="EN-US"}[组信号交互的超时时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **timer** **group-b**]{lang="EN-US"}]{#struct_0_x2079_20553_2032372216}[命令用来恢复情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x2021265108}

[**[timer]{lang="EN-US"}**[ **group-b** *time*]{lang="EN-US"}]{#struct_0_x2079_20553_412766943}

[**[undo]{lang="EN-US"}**[ **timer** **group-b**]{lang="EN-US"}]{#struct_0_x2079_20553_x1432209127}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_730945908}

[[B]{lang="EN-US"}]{#struct_0_x2079_20553_80945899}[组信号交互的超时时间为]{style="font-family:宋体"}[30000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1169502273}

[[R2]{lang="EN-US"}]{#struct_0_x2079_20553_2128297050}[信令视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1906291327}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1718130885}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1254161155}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1264471012}

[**[group-b]{lang="EN-US"}**[ *time*]{lang="EN-US"}]{#struct_0_x2079_20553_x247703693}[：]{style="font-family:宋体"}[B]{lang="EN-US"}[组信号交互的超时时间，取值范围为]{style="font-family:
宋体"}[100]{lang="EN-US"}[～]{style="font-family:
宋体"}[90000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_730880372}

[[该命令对入局端生效。入局端转到]{style="font-family:宋体"}[B]{lang="EN-US"}]{#struct_0_x2079_20553_x1036937521}[组交互阶段后，应当在该时间间隔内完成]{style="font-family:宋体"}[B]{lang="EN-US"}[组交互过程，否则呼叫建立失败。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1235759672}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_416564478}[配置]{style="font-family:宋体"}[B]{lang="EN-US"}[组信号交互的超时时间为]{style="font-family:宋体"}[10000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_730814836}

[\[Sysname\] controller e1 ]{lang="EN-US"}[2/4/1]{lang="DA"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] timeslot-set 0 timeslot-list 1-31 signal r2]{lang="EN-US"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] cas 0]{lang="EN-US"}

[\[Sysname-cas ]{lang="EN-US"}[2/4/1]{lang="DA"}[:0\] timer group-b 10000]{lang="EN-US"}
:::

::: {#600266426 .myid}
[]{#_Toc404794515}[]{#struct_0_x2079_20553_x1473466597}[]{#_Toc316027051}[]{#_Toc61260475}

**语音用户线 \-- 数字语音用户线 \-- timer register-pulse**

------------------------------------------------------------------------

[**[timer]{lang="EN-US"}**[ **register-pulse**]{lang="EN-US"}]{#struct_0_x2079_20553_650546113}[命令用来配置记发器脉冲信号的持续时长。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **timer** **register-pulse**]{lang="EN-US"}]{#struct_0_x2079_20553_678918680}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1967538881}

[**[timer]{lang="EN-US"}**[ **register-pulse** *time*]{lang="EN-US"}]{#struct_0_x2079_20553_1660005977}

[**[undo]{lang="PT-BR"}**]{#struct_0_x2079_20553_x252011815}[ **timer** **register-pulse**]{lang="PT-BR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_730749300}

[[记发器脉冲信号持续时长为]{style="font-family:宋体"}[150]{lang="EN-US"}]{#struct_0_x2079_20553_x2062117659}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1742507650}

[[R2]{lang="EN-US"}]{#struct_0_x2079_20553_1891291816}[信令视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_357491795}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1515352703}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x769254383}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_511177477}

[*[time]{lang="EN-US"}*]{#struct_0_x2079_20553_927713075}[：记发器脉冲信号的持续时长，取值范围为]{style="font-family:宋体"}[50]{lang="EN-US"}[～]{style="font-family:宋体"}[3000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_730683764}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_639461697}[配置记发器脉冲信号的持续时长为]{style="font-family:宋体"}[300]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_1167598387}

[\[Sysname\] controller e1 ]{lang="EN-US"}[2/4/1]{lang="DA"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] timeslot-set 0 timeslot-list 1-31 signal r2]{lang="EN-US"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] cas 0]{lang="EN-US"}

[\[Sysname-cas ]{lang="EN-US"}[2/4/1]{lang="DA"}[:0\] timer register-pulse 300]{lang="EN-US"}
:::

::: {#2024420871 .myid}
[]{#_Toc404794516}[]{#struct_0_x2079_20553_1179561561}[]{#_Toc325038122}

**语音用户线 \-- 数字语音用户线 \-- timeslot-set**

------------------------------------------------------------------------

[**[timeslot-set]{lang="EN-US"}**]{#struct_0_x2079_20553_345685955}[命令用来创建时隙组。]{style="font-family:宋体"}

[**[undo timeslot-set]{lang="EN-US"}**]{#struct_0_x2079_20553_1450068831}[命令用来删除时隙组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1260467734}

[**[timeslot-set]{lang="EN-US"}**[ *ts-set-number* **timeslot-list** *timeslots-list* **signal** **r2**]{lang="EN-US"}]{#struct_0_x2079_20553_730618228}

[**[undo]{lang="EN-US"}**[ **timeslot-set** *ts-set-number*]{lang="EN-US"}]{#struct_0_x2079_20553_x895540969}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1252599304}

[[没有创建时隙组。]{style="font-family:宋体"}]{#struct_0_x2079_20553_648172715}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x242108750}

[[E1]{lang="EN-US"}]{#struct_0_x2079_20553_1327478176}[语音]{style="font-family:宋体"}[/T1]{lang="EN-US"}[语音接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1577002959}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x998760466}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x63756730}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_731601268}

[*[ts-set-number]{lang="EN-US"}*]{#struct_0_x2079_20553_1188233841}[：时隙组的标识号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[timeslots-list]{lang="EN-US"}*]{#struct_0_x2079_20553_1998783261}[：时隙范围。表示方式包括单个数字、由逗号"，"分割开的两个数字、由连字号"]{style="font-family:宋体"}[-]{lang="EN-US"}["分隔开的一对数字，或组合形式（如]{style="font-family:宋体"}[1-14]{lang="EN-US"}[，]{style="font-family:宋体"}[15]{lang="EN-US"}[，]{style="font-family:宋体"}[17-31]{lang="EN-US"}[）。其中]{style="font-family:宋体"}[E1]{lang="EN-US"}[语音接口的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[，]{style="font-family:宋体"}[T1]{lang="EN-US"}[语音接口的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[24]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[signal]{lang="EN-US"}**]{#struct_0_x2079_20553_743176833}[：时隙组实用的信令。]{style="font-family:宋体"}

[**[r2]{lang="EN-US"}**]{#struct_0_x2079_20553_x624189529}[：指定信令方式为]{style="font-family:宋体"}[R2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1148852809}

[[成功创建时隙组后，才能使用]{style="font-family:宋体"}**[subscriber-line]{lang="EN-US"}**]{#struct_0_x2079_20553_433543576}[命令进入数字语音用户线，配置和语音相关的属性。]{style="font-family:宋体"}

[[  ]{lang="EN-US"}]{#struct_0_x2079_20553_x517555817}[【举例】]{style="font-family:黑体"}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_731535732}[创建时隙组，组号为]{style="font-family:宋体"}[5]{lang="EN-US"}[，时隙包括]{style="font-family:宋体"}[TS1]{lang="EN-US"}[～]{style="font-family:宋体"}[TS31]{lang="EN-US"}[，信令为]{style="font-family:宋体"}[R2]{lang="EN-US"}[信令。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x1793499177}

[\[Sysname\] controller e1 ]{lang="EN-US"}[2/4/1]{lang="DA"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] timeslot-set 5 timeslot-list 1-31 signal r2]{lang="EN-US"}
:::

::: {#-779340462 .myid}
[]{#_Toc404794517}[]{#struct_0_x2079_20553_x1767561608}

**语音用户线 \-- 数字语音用户线 \-- trunk-direction**

------------------------------------------------------------------------

[**[trunk-direction]{lang="EN-US"}**]{#struct_0_x2079_20553_329176806}[命令用来配置中继方向。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **trunk-direction**]{lang="EN-US"}]{#struct_0_x2079_20553_x704664712}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_84329488}

[**[trunk-direction]{lang="EN-US"}**[ **timeslots** *timeslots-list* { **dual** \| **in** \| **out** }]{lang="EN-US"}]{#struct_0_x2079_20553_x839996666}

[**[undo]{lang="EN-US"}**[ **trunk-direction** **timeslots** *timeslots-list*]{lang="EN-US"}]{#struct_0_x2079_20553_1635449276}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_731076977}

[[中继方向为双向中继。]{style="font-family:宋体"}]{#struct_0_x2079_20553_x773842158}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x858657739}

[[R2]{lang="EN-US"}]{#struct_0_x2079_20553_1358348939}[信令视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_1180224015}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x166245857}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1577687132}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_439044635}

[*[timeslots-list]{lang="EN-US"}*]{#struct_0_x2079_20553_731011441}[：指定了中继时隙的范围，表示方式包括单个数字、由逗号"，"分割开的两个数字、由连字号"]{style="font-family:宋体"}[-]{lang="EN-US"}["分隔开的一对数字，或组合形式（如]{style="font-family:宋体"}[1-14]{lang="EN-US"}[，]{style="font-family:宋体"}[15]{lang="EN-US"}[，]{style="font-family:宋体"}[17-31]{lang="EN-US"}[）。其中]{style="font-family:宋体"}[E1]{lang="EN-US"}[语音接口的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[，]{style="font-family:宋体"}[T1]{lang="EN-US"}[语音接口的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[24]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[dual]{lang="EN-US"}**]{#struct_0_x2079_20553_1961606637}[：双向中继，表示允许接收呼入或发起呼出。]{style="font-family:宋体"}

[**[in]{lang="EN-US"}**]{#struct_0_x2079_20553_x1511452887}[：入中继，表示只允许接收呼入。]{style="font-family:宋体"}

[**[out]{lang="EN-US"}**]{#struct_0_x2079_20553_2031969559}[：出中继，表示只允许发起呼出。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2079_20553_66664329}

[[为了使得]{style="font-family:宋体"}[R2]{lang="EN-US"}]{#struct_0_x2079_20553_967781468}[信令通信正常，必须确保中继的两端一端为出一端为入。如果两端都采用双向中继，则需要使用]{style="font-family:宋体"}**[select-mode]{lang="EN-US"}**[命令调整中继选路的策略，避免通信双方争抢时隙。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x2046679558}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_x1112590159}[配置中继方向为双向中继。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_730945905}

[\[Sysname\] controller e1 ]{lang="EN-US"}[2/4/1]{lang="DA"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] timeslot-set 0 timeslot-list 1-31 signal r2]{lang="EN-US"}

[\[Sysname-E1 ]{lang="EN-US"}[2/4/1]{lang="DA"}[\] cas 0]{lang="EN-US"}

[\[Sysname-cas ]{lang="EN-US"}[2/4/1]{lang="DA"}[:0\] trunk-direction timeslots 1-31 dual]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_80945902}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[select-mode]{lang="EN-US"}**]{#struct_0_x2079_20553_x1231926860}
:::

::: {#-839403572 .myid}
[]{#_Toc404794518}[]{#struct_0_x2079_20553_x1331905356}[]{#_Toc316027034}[]{#_Toc294166678}[]{#_Toc262031006}[]{#_Toc135295498}[]{#_Toc133476846}[]{#_Toc130098015}[]{#_Toc129160947}

**语音用户线 \-- 数字语音用户线 \-- ts**

------------------------------------------------------------------------

[**[ts]{lang="EN-US"}**]{#struct_0_x2079_20553_x1909165822}[命令用来对指定时隙进行维护操作。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x2079159281}

[**[ts]{lang="EN-US"}**[ { **block** \| **open** \| **query** \| **reset** } **timeslots** *timeslots-list*]{lang="EN-US"}]{#struct_0_x2079_20553_1733160349}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1850731265}

[[R2]{lang="EN-US"}]{#struct_0_x2079_20553_730880369}[信令视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_919377608}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_1012948882}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x155604770}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2079_20553_2081366112}

[**[block]{lang="EN-US"}**]{#struct_0_x2079_20553_1604080515}[：闭塞指定时隙，即人为的将线路设为不可用。]{style="font-family:宋体"}

[**[open]{lang="EN-US"}**]{#struct_0_x2079_20553_x1653660694}[：打开指定时隙，为闭塞操作的逆过程，重新将时隙设为可用。]{style="font-family:宋体"}

[**[query]{lang="EN-US"}**]{#struct_0_x2079_20553_x2077754525}[：查询指定时隙，实时显示线路的忙闲状态、打开或闭塞状态。]{style="font-family:宋体"}

[**[reset]{lang="EN-US"}**]{#struct_0_x2079_20553_1232912326}[：复位指定时隙。通常当进行人工闭塞或打开时隙时，若时隙的状态不能正常恢复，则需要执行复位操作。或者是由于其它原因导致时隙不能自动正确复位时，也需要对时隙进行人工复位。]{style="font-family:宋体"}

[**[timeslots]{lang="EN-US"}***[ timeslots-list]{lang="EN-US"}*]{#struct_0_x2079_20553_730814833}[：指定了一个时隙范围，表示方式包括单个数字、由逗号"，"分割开的两个数字、由连字号"]{style="font-family:宋体"}[-]{lang="EN-US"}["分割开的一对数字，或组合形式（如]{style="font-family:宋体"}[1-14]{lang="EN-US"}[，]{style="font-family:宋体"}[15]{lang="EN-US"}[，]{style="font-family:宋体"}[17-31]{lang="EN-US"}[）。其中]{style="font-family:宋体"}[E1]{lang="EN-US"}[语音接口的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[，]{style="font-family:宋体"}[T1]{lang="EN-US"}[语音接口的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[24]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1473466592}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_247261586}[复位]{style="font-family:宋体"}[0]{lang="EN-US"}[号时隙组中的]{style="font-family:宋体"}[TS1]{lang="EN-US"}[～]{style="font-family:宋体"}[TS15]{lang="EN-US"}[时隙。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_1193854873}

[\[Sysname\] controller e1 2/4/1]{lang="EN-US"}

[\[Sysname-E1 2/4/1\] timeslot-set 0 timeslot-list 1-31 signal r2]{lang="EN-US"}

[\[Sysname-E1 2/4/1\] cas 0]{lang="EN-US"}

[\[Sysname-cas 2/4/1:0\] ts reset timeslots 1-15]{lang="EN-US"}
:::

::: {#1322163795 .myid}
[]{#_Toc404794519}[]{#struct_0_x2079_20553_641083926}[]{#_Toc401757460}

**语音用户线 \-- 数字语音用户线 \-- voice call disc-pi-off**

------------------------------------------------------------------------

[**[voice call disc-pi-off]{lang="EN-US"}**]{#struct_0_x2079_20553_2007701731}[命令用来配置设备收到]{style="font-family:宋体"}[PI]{lang="EN-US"}[（]{style="font-family:宋体"}[Progress Indicator]{lang="EN-US"}[，进展指示语）为]{style="font-family:宋体"}[8]{lang="EN-US"}[的]{style="font-family:宋体"}[DISCONNECT]{lang="EN-US"}[消息时，按照标准的]{style="font-family:宋体"}[DISCONNECT]{lang="EN-US"}[消息进行处理（释放资源，]{style="font-family:宋体"}[B]{lang="EN-US"}[通道为开启状态则关闭]{style="font-family:宋体"}[B]{lang="EN-US"}[通道）。]{style="font-family:宋体"}

[**[undo voice call disc-pi-off]{lang="EN-US"}**]{#struct_0_x2079_20553_285051878}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x2052473469}

[**[voice call disc-pi-off]{lang="EN-US"}**]{#struct_0_x2079_20553_x2085406778}

[**[undo voice call disc-pi-off]{lang="EN-US"}**]{#struct_0_x2079_20553_x160939185}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x1187712652}

[[设备收到]{style="font-family:宋体"}[PI]{lang="EN-US"}]{#struct_0_x2079_20553_x1182027958}[为]{style="font-family:宋体"}[8]{lang="EN-US"}[的]{style="font-family:
宋体"}[DISCONNECT]{lang="EN-US"}[消息时，用户侧]{style="font-family:宋体"}[B]{lang="EN-US"}[通道若为开启状态则保持]{style="font-family:宋体"}[B]{lang="EN-US"}[通道，若为关闭状态则重新建立]{style="font-family:宋体"}[B]{lang="EN-US"}[通道，用以接收带内信号音，并进入拆线指示状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2079_20553_10697573}

[[语音视图]{style="font-family:宋体"}]{#struct_0_x2079_20553_356349003}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2079_20553_x858502196}

[[network-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1028257475}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2079_20553_x1387449151}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2079_20553_55249591}

[[\# ]{lang="EN-US"}]{#struct_0_x2079_20553_419314955}[配置设备收到]{style="font-family:宋体"}[PI]{lang="EN-US"}[为]{style="font-family:宋体"}[8]{lang="EN-US"}[的]{style="font-family:
宋体"}[DISCONNECT]{lang="EN-US"}[消息时，按照标准的]{style="font-family:宋体"}[DISCONNECT]{lang="EN-US"}[消息进行处理。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2079_20553_x516150831}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice call disc-pi-off]{lang="EN-US"}

[ ]{lang="EN-US"}
:::
