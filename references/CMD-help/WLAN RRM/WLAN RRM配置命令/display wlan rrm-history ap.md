::: {#1339335389 .myid}
[]{#_Toc404795305}[]{#struct_0_x1035_x2319_121683460}

**WLAN RRM \-- WLAN RRM配置命令 \-- display wlan rrm-history ap**

------------------------------------------------------------------------

[**[display wlan rrm-history ap]{lang="EN-US"}**]{#struct_0_x1035_x2319_600102537}[命令用来显示]{style="font-family:
宋体"}[AP]{lang="EN-US"}[的信道和功率调整历史信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x965718677}

[**[display wlan rrm-history ap ]{lang="EN-US"}**[{ **all** \| **name** ]{lang="EN-US"}*[ap-name ]{lang="EN-US"}*[}]{lang="EN-US"}]{#struct_0_x1035_x2319_1005943950}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x1536446931}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1035_x2319_1612781970}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x1345089503}

[[network-admin]{lang="EN-US"}]{#struct_0_x1035_x2319_x1148645997}

[[network-operator]{lang="EN-US"}]{#struct_0_x1035_x2319_x1448467082}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1035_x2319_x2066570389}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1035_x2319_x1808516949}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x1841508668}

[**[all]{lang="EN-US"}**]{#struct_0_x1035_x2319_1342545624}[：所有]{style="font-family:宋体"}[AP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}***[ ap-name]{lang="EN-US"}*]{#struct_0_x1035_x2319_x1165499040}[：]{style="font-family:宋体"}[AP]{lang="EN-US"}[名称，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_1664449095}

[[该命令显示所有或指定]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_x1035_x2319_1096426259}[上最近]{style="font-family:宋体"}[3]{lang="EN-US"}[次改变的信道或功率的详细信息。显示输出包括改变时间、触发原因、功率、干扰等参数]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_1361330522}

[[\# ]{lang="EN-US"}]{#struct_0_x1035_x2319_220156913}[显示]{style="font-family:宋体"}[ap1]{lang="EN-US"}[的]{style="font-family:宋体"}[RRM]{lang="EN-US"}[历史信息。]{style="font-family:宋体"}

[[\<Sysname\> display wlan rrm-history ap name ap1 ]{lang="EN-US"}]{#struct_0_x1035_x2319_x1386337731}

[                         AP RRM History]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Flags : I - Interference,   P - Packets discarded,    F - Retransmission,]{lang="EN-US"}

[         R - Radar,          C - Coverage,             O - Others]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[                         AP RRM History : ap1]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Radio : 1                                Basic BSSID : 000f-e2ff-7700]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[        Ch  Power Load Util Intf PER Retry Reason  Date         Time]{lang="EN-US"}

[            (dBm) (%)  (%)  (%)  (%) (%)           (yyyy-mm-dd) (hh:mm:ss)]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Before 6   20    24   2    21   11  18    -P\-\-\--  2014-07-07   17:31:50]{lang="EN-US"}

[ After  1   20    9    0    8    0   27    -       -            -]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Before 1   20    54   1    53   11  15    IP\-\-\--  2014-07-08   12:19:50]{lang="EN-US"}

[ After  6   20    10   0    10   3   29    -       -            -]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Before 6   20    29   1    28   21  20    -P\-\-\--  2014-07-08   12:59:50]{lang="EN-US"}

[ After  1   20    30   0    29   2   24    -       -            -]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display wlan rrm-history]{lang="EN-US"}]{#struct_0_x1035_x2319_x1377406905}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x202446596}[[字段]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x1358526340}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1035_x2319_1197292282}

[[Radio]{lang="EN-US"}]{#struct_0_x1035_x2319_x1173327951}

[[AP]{lang="EN-US"}]{#struct_0_x1035_x2319_1760663264}[的]{style="font-family:宋体"}[Radio ID]{lang="EN-US"}

[[Basic BSSID]{lang="EN-US"}]{#struct_0_x1035_x2319_1459401044}

[[基本服务集标识]{style="font-family:宋体"}]{#struct_0_x1035_x2319_x635326482}

[[Ch]{lang="EN-US"}]{#struct_0_x1035_x2319_973601043}

[[Radio]{lang="EN-US"}]{#struct_0_x1035_x2319_1400910501}[的工作信道]{style="font-family:宋体"}

[[Power]{lang="EN-US"}]{#struct_0_x1035_x2319_986249728}

[[Radio]{lang="EN-US"}]{#struct_0_x1035_x2319_1698079013}[的发送功率]{style="font-family:宋体"}

[[Load]{lang="EN-US"}]{#struct_0_x1035_x2319_1211973434}

[[信道的负载，以百分比表示]{style="font-family:宋体"}]{#struct_0_x1035_x2319_1032300076}

[[Util]{lang="EN-US"}]{#struct_0_x1035_x2319_744101181}

[[信道的利用率，以百分比显示]{style="font-family:宋体"}]{#struct_0_x1035_x2319_586981098}

[[Intf]{lang="EN-US"}]{#struct_0_x1035_x2319_484458840}

[[信道检测到的干扰，以百分比表示]{style="font-family:宋体"}]{#struct_0_x1035_x2319_1062261710}

[[PER]{lang="EN-US"}]{#struct_0_x1035_x2319_x747386712}

[[信道检测到的误码率，以百分比表示]{style="font-family:宋体"}]{#struct_0_x1035_x2319_x1742633627}

[[Retry]{lang="EN-US"}]{#struct_0_x1035_x2319_1254990738}

[[信道检测到的重传率，以百分比表示]{style="font-family:宋体"}]{#struct_0_x1035_x2319_x1006099479}

[[Reason]{lang="EN-US"}]{#struct_0_x1035_x2319_213507375}

[[信道或功率调整的原因]{style="font-family:宋体"}]{#struct_0_x1035_x2319_x1181385414}

[[Date]{lang="EN-US"}]{#struct_0_x1035_x2319_x57994221}

[[发生信道或功率调整的日期]{style="font-family:宋体"}]{#struct_0_x1035_x2319_x1142625256}

[[Time]{lang="EN-US"}]{#struct_0_x1035_x2319_x1360220834}

[[发生信道或功率调整的时间]{style="font-family:宋体"}]{#struct_0_x1035_x2319_x176549686}

[ ]{lang="EN-US"}

::: {#-1098270818 .myid}
[]{#struct_0_x1035_x2319_x1442060043}[]{#_Toc404795306}

**WLAN RRM \-- WLAN RRM配置命令 \-- display wlan rrm-status ap**

------------------------------------------------------------------------

[**[display wlan rrm-]{lang="EN-US"}[status ap]{lang="EN-US"}**]{#struct_0_x1035_x2319_x934876993}[命令用来显示]{style="font-family:宋体"}[AP]{lang="EN-US"}[上射频的]{style="font-family:宋体"}[RRM]{lang="EN-US"}[详细信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x128120269}

[**[display wlan rrm-]{lang="EN-US"}[status ap ]{lang="EN-US"}**[{ **all** \| **name** ]{lang="EN-US"}*[ap-name ]{lang="EN-US"}*[}]{lang="EN-US"}]{#struct_0_x1035_x2319_x14614321}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_1420074033}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1035_x2319_858349941}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_1385062488}

[[network-admin]{lang="EN-US"}]{#struct_0_x1035_x2319_x1713467852}

[[network-operator]{lang="EN-US"}]{#struct_0_x1035_x2319_279958467}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1035_x2319_x1772347715}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1035_x2319_1038450463}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_1102451861}

[**[all]{lang="EN-US"}**]{#struct_0_x1035_x2319_697014271}[：所有]{style="font-family:宋体"}[AP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}***[ ap-name]{lang="EN-US"}*]{#struct_0_x1035_x2319_1389534255}[：]{style="font-family:宋体"}[AP]{lang="EN-US"}[名称，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x2051323592}

[[在]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_x1035_x2319_29092840}[设备上，如果信道和功率调整处于关闭状态，则执行此命令时，只会显示]{style="font-family:宋体"}[AP]{lang="EN-US"}[上]{style="font-family:宋体"}[Radio]{lang="EN-US"}[的工作信道和功率级别，其它信息如干扰、邻居的数量等不会显示。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x722475466}

[[\# ]{lang="EN-US"}]{#struct_0_x1035_x2319_x1576754292}[显示]{style="font-family:宋体"}[ap1]{lang="EN-US"}[的信道和功率调整详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display wlan rrm-status ap name ap1 ]{lang="EN-US"}]{#struct_0_x1035_x2319_226734841}

[                          AP RRM Profile : ap1]{lang="IT"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="IT"}

[ Radio   : 1                              Basic BSSID    : 70f9-6d31-2fe0]{lang="IT"}

[ Channel : 157                            Tx Power (dBm) : 18]{lang="IT"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="IT"}

[    Ch    Nbrs    Load    Util    Intf    PER    Retry    Radar]{lang="IT"}

[                  (%)     (%)     (%)     (%)     (%)]{lang="IT"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="IT"}

[    36    0       0       -       0       0      -        -]{lang="IT"}

[    40    0       0       -       0       0      -        - ]{lang="IT"}

[    44    0       0       -       0       0      -        -]{lang="IT"}

[    48    0       0       -       0       0      -        -]{lang="IT"}

[    52    0       0       -       0       0      -        -]{lang="IT"}

[    56    0       0       -       0       0      -        -]{lang="IT"}

[    60    0       0       -       0       0      -        -]{lang="IT"}

[    64    0       0       -       0       0      -        -]{lang="IT"}

[    100   0       0       -       0       0      -        -]{lang="IT"}

[    104   0       0       -       0       0      -        -]{lang="IT"}

[    108   0       0       -       0       0      -        -]{lang="IT"}

[    112   0       0       -       0       0      -        -]{lang="IT"}

[    116   0       0       -       0       0      -        -]{lang="IT"}

[    132   0       0       -       0       0      -        -]{lang="IT"}

[    136   0       0       -       0       0      -        -]{lang="IT"}

[    140   0       0       -       0       0      -        -]{lang="IT"}

[    149   1       0       -       0       0      -        -]{lang="IT"}

[    153   4       0       -       0       0      -        -]{lang="IT"}

[    157   0       0       0       0       0      0        -]{lang="IT"}

[    161   2       0       -       0       0      -        -]{lang="IT"}

[    165   0       0       -       0       0      -        -]{lang="IT"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="IT"}

[   Nbr-BasicBSSID   Ch    Intf   SignalStrength   Type]{lang="IT"}

[                           (%)    (dBm)]{lang="IT"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="IT"}

[   000f-e212-ff01   161   0      -60              Unmanaged]{lang="IT"}

[   5866-ba74-e461   153   0      -72              Unmanaged]{lang="IT"}

[   70f9-6d30-9020   153   0      -40              Managed]{lang="IT"}

[   70f9-6d31-3080   149   0      -54              Managed]{lang="IT"}

[   70f9-6d31-34e0   161   0      -59              Managed]{lang="IT"}

[   7425-8a86-bbe0   153   0      -48              Unmanaged]{lang="IT"}

[   7425-8a86-c720   153   0      -63              Unmanaged]{lang="IT"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="IT"}

[ Radio   : 2                              Basic BSSID    : 70f9-6d31-2ff0]{lang="IT"}

[ Channel : 1                              Tx Power (dBm) : 19]{lang="IT"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="IT"}

[    Ch    Nbrs    Load    Util    Intf    PER    Retry    Radar]{lang="IT"}

[                  (%)     (%)     (%)     (%)     (%)]{lang="IT"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="IT"}

[    1     6       4       0       4       0      0        -]{lang="IT"}

[    6     4       2       -       2       0      -        -]{lang="IT"}

[    11    6       2       -       2       0      -        -]{lang="IT"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="IT"}

[   Nbr-BasicBSSID   Ch    Intf   SignalStrength   Type]{lang="IT"}

[                           (%)    (dBm)]{lang="IT"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="IT"}

[   000f-e212-ff11   1     49     -77              Unmanaged]{lang="IT"}

[   0023-89e1-ed00   11    0      -87              Unmanaged]{lang="IT"}

[   006a-55f6-ae10   1     57     -88              Unmanaged]{lang="IT"}

[   5866-ba64-aa31   1     10     -60              Unmanaged]{lang="IT"}

[   5866-ba74-e471   6     0      -76              Unmanaged]{lang="IT"}

[   5866-baa9-a610   11    0      -62              Unmanaged]{lang="IT"}

[   70f9-6d30-9030   6     0      -63              Managed]{lang="IT"}

[   70f9-6d31-3090   1     51     -86              Managed]{lang="IT"}

[   70f9-6d31-34f0   6     0      -85              Managed]{lang="IT"}

[   7425-8a86-bbf0   6     0      -73              Unmanaged]{lang="IT"}

[   7425-8a86-c731   11    0      -93              Unmanaged]{lang="IT"}

[   80f6-2ec0-3330   11    0      -76              Unmanaged]{lang="IT"}

[   80f6-2ec0-3331   11    0      -73              Unmanaged]{lang="IT"}

[   80f6-2edd-d2d0   1     40     -60              Unmanaged]{lang="IT"}

[   80f6-2edd-d2d1   1     44     -68              Unmanaged]{lang="IT"}

[   80f6-2ede-0b30   11    0      -74              Unmanaged]{lang="IT"}

[[表1-2 ]{lang="EN-US"}[display wlan rrm-status]{lang="EN-US"}]{#struct_0_x1035_x2319_x1080516145}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x206876730}[[字段]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x1773637992}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x725185256}

[[Radio]{lang="EN-US"}]{#struct_0_x1035_x2319_656581374}

[[AP]{lang="EN-US"}]{#struct_0_x1035_x2319_2126615843}[的]{style="font-family:宋体"}[Radio ID]{lang="EN-US"}

[[Basic BSSID]{lang="EN-US"}]{#struct_0_x1035_x2319_x1366570540}

[[基本服务集标识]{style="font-family:宋体"}]{#struct_0_x1035_x2319_1405696403}

[[Channel]{lang="EN-US"}]{#struct_0_x1035_x2319_x1897984802}

[[Radio]{lang="EN-US"}]{#struct_0_x1035_x2319_x102512956}[当前的工作信道]{style="font-family:宋体"}

[[Tx Power]{lang="EN-US"}]{#struct_0_x1035_x2319_1792818782}

[[Radio]{lang="EN-US"}]{#struct_0_x1035_x2319_241152724}[的发送功率]{style="font-family:宋体"}

[[Ch]{lang="EN-US"}]{#struct_0_x1035_x2319_65826150}

[[Radio]{lang="EN-US"}]{#struct_0_x1035_x2319_x1676431919}[支持的工作信道]{style="font-family:宋体"}

[[Nbrs]{lang="EN-US"}]{#struct_0_x1035_x2319_476931287}

[[信道中的]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_x1035_x2319_x1453119526}[邻居数量]{style="font-family:宋体"}

[[Load]{lang="EN-US"}]{#struct_0_x1035_x2319_x2029303761}

[[信道的负载，以百分比表示。信道的负载指的是在该信道上，]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_x1035_x2319_1099442776}[发送报文]{style="font-family:宋体"}[/]{lang="EN-US"}[接收客户端的报文和干扰，这里的干扰指该]{style="font-family:宋体"}[AP]{lang="EN-US"}[接收到其它]{style="font-family:宋体"}[AP]{lang="EN-US"}[和客户端发送的错误报文]{style="font-family:宋体"}

[[Util]{lang="EN-US"}]{#struct_0_x1035_x2319_1605332720}

[[信道利用率，以百分比显表示。信道利用率指的是在该信道上，]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_x1035_x2319_x2006238508}[发送报文]{style="font-family:宋体"}[/]{lang="EN-US"}[接收客户端的报文]{style="font-family:宋体"}

[[Intf]{lang="EN-US"}]{#struct_0_x1035_x2319_x936064573}

[[信道检测到的干扰，以百分比表示]{style="font-family:宋体"}]{#struct_0_x1035_x2319_x1956180160}

[[PER]{lang="EN-US"}]{#struct_0_x1035_x2319_x1776854310}

[[信道检测到的误码率，以百分比表示]{style="font-family:宋体"}]{#struct_0_x1035_x2319_x1683754117}

[[Retry]{lang="EN-US"}]{#struct_0_x1035_x2319_x392841767}

[[信道检测到的重传率，以百分比表示]{style="font-family:宋体"}]{#struct_0_x1035_x2319_x1830964724}

[[Radar]{lang="EN-US"}]{#struct_0_x1035_x2319_x534029858}

[[雷达检测状态：]{style="font-family:宋体"}]{#struct_0_x1035_x2319_913248744}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[-]{lang="EN-US"}]{#struct_0_x1035_x2319_1342480088}[表示没有检测到雷达]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol;display:none"}[Detected]{lang="EN-US"}]{#struct_0_x1035_x2319_x1211612326}[表示检测到雷达]{lang="EN-US" style="font-family:宋体"}

[[Nbr-BasicBSSID]{lang="IT"}]{#struct_0_x1035_x2319_624793378}

[[邻居]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_x1035_x2319_x1581731243}[的]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[SignalStrength]{lang="EN-US"}]{#struct_0_x1035_x2319_780563731}

[[检测到邻居]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_x1035_x2319_x1089050866}[的信号强度，以]{style="font-family:宋体"}[dBm]{lang="EN-US"}[为单位]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_x1035_x2319_1928255197}

[[AP]{lang="EN-US"}]{#struct_0_x1035_x2319_x698427832}[类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unmanaged]{lang="EN-US"}]{#struct_0_x1035_x2319_x1386403267}[：该]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[能探到的非邻居]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol;display:none"}[Managed]{lang="EN-US"}]{#struct_0_x1035_x2319_22734433}[：该]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[能探测到的邻居]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#-537948303 .myid}
[]{#_Toc404795307}[]{#struct_0_x1035_x2319_564173192}

**WLAN RRM \-- WLAN RRM配置命令 \-- adjacency-factor**

------------------------------------------------------------------------

[**[adjacency-factor]{lang="EN-US"}**]{#struct_0_x1035_x2319_1747017731}[命令用来配置当前]{style="font-family:宋体"}[Radio]{lang="EN-US"}[所在频段上触发功率调整的最大邻居数和在邻居]{style="font-family:宋体"}[AP]{lang="EN-US"}[的功率排名中指定]{style="font-family:宋体"}[AP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo adjacency-factor]{lang="EN-US"}**]{#struct_0_x1035_x2319_x210802719}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_644016618}

[**[adjacency-factor ]{lang="EN-US"}***[neighbor]{lang="EN-US"}*]{#struct_0_x1035_x2319_1750821462}

[**[undo adjacency-factor]{lang="EN-US"}**]{#struct_0_x1035_x2319_352825203}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_1244533844}

[[触发功率调整的最大邻居数为]{style="font-family:宋体"}[3]{lang="EN-US"}]{#struct_0_x1035_x2319_x117375791}[和在邻居]{style="font-family:宋体"}[AP]{lang="EN-US"}[的功率排名中指定排名第]{style="font-family:宋体"}[3]{lang="EN-US"}[位的邻居]{style="font-family:宋体"}[AP]{lang="EN-US"}[，即需要和功率调整门限值进行比较的]{style="font-family:宋体"}[AP]{lang="EN-US"}[为在所有邻居]{style="font-family:宋体"}[AP]{lang="EN-US"}[中信号强度排在第]{style="font-family:宋体"}[3]{lang="EN-US"}[位的邻居]{style="font-family:宋体"}[AP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_1607515655}

[[RRM]{lang="EN-US"}]{#struct_0_x1035_x2319_223963720}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x987124981}

[[network-admin]{lang="EN-US"}]{#struct_0_x1035_x2319_986184192}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1035_x2319_x1257576711}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_1660865584}

[*[neighbor]{lang="EN-US"}*]{#struct_0_x1035_x2319_180933790}[：触发功率调整的最大邻居数和在邻居]{style="font-family:宋体"}[AP]{lang="EN-US"}[的功率排名中指定]{style="font-family:宋体"}[AP]{lang="EN-US"}[，即需要和功率调整门限值进行比较的邻居]{style="font-family:宋体"}[AP]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x324887319}

[[\# ]{lang="EN-US"}]{#struct_0_x1035_x2319_x1434022592}[配置当前]{style="font-family:宋体"}[Radio]{lang="EN-US"}[所在频段上触发功率调整的最大邻居数为]{style="font-family:宋体"}[7]{lang="EN-US"}[，需要和功率调整门限值进行比较的]{style="font-family:宋体"}[AP]{lang="EN-US"}[为在所有邻居]{style="font-family:宋体"}[AP]{lang="EN-US"}[中信号强度排在第]{style="font-family:宋体"}[7]{lang="EN-US"}[位的邻居]{style="font-family:宋体"}[AP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1035_x2319_x2098478378}

[\[Sysname\] wlan ap ap1]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1\] rrm]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1-rrm\] adjacency-factor 7]{lang="EN-US"}
:::

::: {#763079374 .myid}
[]{#_Toc404795308}[]{#struct_0_x1035_x2319_x219072271}[]{#_Toc392681713}[]{#_Toc392836502}[]{#_Toc397707621}[]{#_Toc399315201}[]{#_Toc392681714}[]{#_Toc392836503}[]{#_Toc397707622}[]{#_Toc399315202}[]{#_Toc354316827}[]{#_Toc354316828}[]{#_Toc354316829}[]{#_Toc354316830}[]{#_Toc354316831}[]{#_Toc354316832}[]{#_Toc354316833}[]{#_Toc354316834}[]{#_Toc354316835}[]{#_Toc354316836}[]{#_Toc354316837}[]{#_Toc354316838}[]{#_Toc354316839}[]{#_Toc354316840}[]{#_Toc354316841}[]{#_Toc354316842}[]{#_Toc354316843}[]{#_Toc354316844}[]{#_Toc354316845}[]{#_Toc167869181}[]{#_Toc167869182}[]{#_Toc167869183}[]{#_Toc167869184}[]{#_Toc167869185}[]{#_Toc167869186}[]{#_Toc167869187}[]{#_Toc167869188}[]{#_Toc167869189}[]{#_Toc167869190}[]{#_Toc167869191}[]{#_Toc167869192}[]{#_Toc167869193}[]{#_Toc167869194}[]{#_Toc167869195}[]{#_Toc167869196}[]{#_Toc167869197}[]{#_Toc167869198}[]{#_Toc167869200}[]{#_Toc167869201}[]{#_Toc167869203}[]{#_Toc167869204}[]{#_Toc167869206}[]{#_Toc167869207}[]{#_Toc167869208}[]{#_Toc167869209}[]{#_Toc167869210}[]{#_Toc167869211}[]{#_Toc167869212}[]{#_Hlt19451604}[]{#_Toc167869213}[]{#_Toc167869214}[]{#_Toc167869215}[]{#_Toc167869216}[]{#_Toc167869217}[]{#_Toc167869218}[]{#_Toc167869219}[]{#_Toc167869220}[]{#_Toc167869221}[]{#_Toc167869223}[]{#_Toc167869224}[]{#_Toc167869225}[]{#_Toc167869226}[]{#_Toc248810082}[]{#_Toc248810083}[]{#_Toc248810084}[]{#_Toc248810085}

**WLAN RRM \-- WLAN RRM配置命令 \-- calibrate-channel self-decisive**

------------------------------------------------------------------------

[**[calibrate-channel self-decisive]{lang="EN-US"}**]{#struct_0_x1035_x2319_923828702}[命令用来开启定时触发自动信道调整。]{style="font-family:宋体"}

[**[undo ]{lang="IT"}[calibrate-channel self-decisive]{lang="EN-US"}**]{#struct_0_x1035_x2319_2018257250}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_200830202}

[**[calibrate-channel self-decisive]{lang="EN-US"}**]{#struct_0_x1035_x2319_x309973614}

[**[undo calibrate-channel self-decisive]{lang="EN-US"}**]{#struct_0_x1035_x2319_x1825538771}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x688299265}

[[定时触发自动信道调整处于关闭状态]{style="font-family:宋体"}]{#struct_0_x1035_x2319_x1385150151}[。]{style="font-family:
宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x824749111}

[[RRM]{lang="EN-US"}]{#struct_0_x1035_x2319_1325406959}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x597013983}

[[network-admin]{lang="EN-US"}]{#struct_0_x1035_x2319_x302463129}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1035_x2319_x1016562487}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_1529511570}

[[\# ]{lang="EN-US"}]{#struct_0_x1035_x2319_481601492}[配置定时触发自动信道调整]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1035_x2319_902546060}

[\[Sysname\] wlan ap ap1 model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1\] rrm]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1-rrm\] calibrate-channel self-decisive]{lang="EN-US"}
:::

::: {#737800111 .myid}
[]{#_Toc404795309}[]{#struct_0_x1035_x2319_1622692100}

**WLAN RRM \-- WLAN RRM配置命令 \-- calibrate-power min**

------------------------------------------------------------------------

[**[calibrate-power min]{lang="EN-US"}**]{#struct_0_x1035_x2319_x1798955821}[命令用来配置]{style="font-family:宋体"}[AP]{lang="EN-US"}[的最小发送功率。]{style="font-family:宋体"}

[**[undo ]{lang="IT"}[calibrate-power min]{lang="EN-US"}**]{#struct_0_x1035_x2319_1262788082}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x1640780149}

[**[calibrate-power min ]{lang="EN-US"}***[tx-power]{lang="EN-US"}*]{#struct_0_x1035_x2319_972929589}

[**[undo calibrate-power min]{lang="EN-US"}**]{#struct_0_x1035_x2319_x176615222}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_477913232}

[[AP]{lang="EN-US"}]{#struct_0_x1035_x2319_655821018}[的最小发送功率为]{style="font-family:宋体"}[1dBm]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x861599919}

[[RRM]{lang="EN-US"}]{#struct_0_x1035_x2319_x1585123095}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x1582433396}

[[network-admin]{lang="EN-US"}]{#struct_0_x1035_x2319_1454511906}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1035_x2319_x1477267501}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_1959622003}

[*[tx-power]{lang="EN-US"}*]{#struct_0_x1035_x2319_1506687897}[：]{style="font-family:宋体"}[AP]{lang="EN-US"}[的最小发送功率，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[dBm]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_2101051777}

[[调整]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_x1035_x2319_21466123}[功率后（包括手动调整、自动调整），]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[发送功率不能小于]{style="font-family:宋体"}**[calibrate-power min]{lang="EN-US"}**[命令设置的最小发送功率。该命令主要用来防止调整后的]{style="font-family:宋体"}[AP]{lang="EN-US"}[功率值过小。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_842549892}

[[\# ]{lang="EN-US"}]{#struct_0_x1035_x2319_971239899}[配置]{style="font-family:宋体"}[AP]{lang="EN-US"}[的最小发送功率为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1035_x2319_1389468719}

[\[Sysname\] wlan ap ap1 model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1\] rrm]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1-rrm\] calibrate-power min 10]{lang="EN-US"}
:::

::: {#947894357 .myid}
[]{#_Toc404795310}[]{#struct_0_x1035_x2319_768332309}

**WLAN RRM \-- WLAN RRM配置命令 \-- calibrate-power self-decisive**

------------------------------------------------------------------------

[**[calibrate-power self-decisive]{lang="EN-US"}**]{#struct_0_x1035_x2319_x934811457}[命令用来开启定时触发自动功率调整。]{style="font-family:
宋体"}

[**[undo ]{lang="IT"}[calibrate-power self-decisive]{lang="EN-US"}**]{#struct_0_x1035_x2319_1950794390}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_129585725}

[**[calibrate-power self-decisive]{lang="EN-US"}**]{#struct_0_x1035_x2319_x998781885}

[**[undo calibrate-power self-decisive]{lang="EN-US"}**]{#struct_0_x1035_x2319_x477056587}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_1605025077}

[[定时触发自动功率调整处于关闭状态]{style="font-family:宋体"}]{#struct_0_x1035_x2319_1109289719}[。]{style="font-family:
宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_1777614238}

[[RRM]{lang="EN-US"}]{#struct_0_x1035_x2319_x1496643793}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_425005297}

[[network-admin]{lang="EN-US"}]{#struct_0_x1035_x2319_x312006957}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1035_x2319_x1648641302}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_361562608}

[[\# ]{lang="EN-US"}]{#struct_0_x1035_x2319_x1481120238}[配置定时触发自动功率调整]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1035_x2319_x1339414636}

[\[Sysname\] wlan ap ap1 model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1\] rrm]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1-rrm\] calibrate-power self-decisive]{lang="EN-US"}
:::

::: {#-460113281 .myid}
[]{#_Toc404795311}[]{#struct_0_x1035_x2319_x1719133850}

**WLAN RRM \-- WLAN RRM配置命令 \-- calibrate-power threshold**

------------------------------------------------------------------------

[**[calibrate-power threshold]{lang="EN-US"}**]{#struct_0_x1035_x2319_190775928}[命令用来配置功率调整门限值。]{style="font-family:
宋体"}

[**[undo ]{lang="IT"}[calibrate-power threshold]{lang="EN-US"}**]{#struct_0_x1035_x2319_x272286476}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x1551581832}

[**[calibrate-power threshold ]{lang="EN-US"}***[value]{lang="EN-US"}*]{#struct_0_x1035_x2319_x621917844}

[**[undo calibrate-power threshold]{lang="EN-US"}**]{#struct_0_x1035_x2319_x437547747}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x1295612761}

[[功率调整门限值为]{style="font-family:宋体"}[-65dBm]{lang="EN-US"}]{#struct_0_x1035_x2319_x1132179325}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x1097691587}

[[RRM]{lang="EN-US"}]{#struct_0_x1035_x2319_x327367105}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x360870820}

[[network-admin]{lang="EN-US"}]{#struct_0_x1035_x2319_1018634698}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1035_x2319_x963324074}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_226669305}

[*[value]{lang="EN-US"}*]{#struct_0_x1035_x2319_x1153391261}[：功率调整门限值，取值范围为]{style="font-family:宋体"}[50]{lang="EN-US"}[～]{style="font-family:宋体"}[90]{lang="EN-US"}[，代表功率范围为]{style="font-family:宋体"}[-90]{lang="EN-US"}[～]{style="font-family:宋体"}[-50dBm]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x842338654}

[[\# ]{lang="EN-US"}]{#struct_0_x1035_x2319_x370690614}[配置功率调整门限值为]{style="font-family:宋体"}[-70dBm]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1035_x2319_x1609825600}

[\[Sysname\] wlan ap ap1 model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1\] rrm]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1-rrm\] calibrate-power threshold 70]{lang="EN-US"}
:::

::: {#-1713084427 .myid}
[]{#_Toc404795312}[]{#struct_0_x1035_x2319_2016608818}[]{#_Toc401841494}[]{#_Toc396742900}[]{#_Toc393118439}

**WLAN RRM \-- WLAN RRM配置命令 \-- channel-capability mode**

------------------------------------------------------------------------

[**[channel]{lang="EN-US"}**]{#struct_0_x1035_x2319_388210111}**[-capability mode]{lang="IT"}**[命令用于配置对客户端信道能力集的检查模式。]{style="font-family:宋体"}

[**[undo channel-capability mode]{lang="IT"}**]{#struct_0_x1035_x2319_x747248787}[命令用于恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_996586875}

[**[channel-capability mode ]{lang="IT"}**]{#struct_0_x1035_x2319_x1336226425}[{ **all** \| ]{lang="IT"}**[none ]{lang="IT"}**[\| ]{lang="IT"}**[partial]{lang="IT"}**[ }]{lang="IT"}

[**[undo channel-capability mode]{lang="IT"}**]{#struct_0_x1035_x2319_x463598297}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x1383564202}

[[不检查客户端信道能力集。]{style="font-family:宋体"}]{#struct_0_x1035_x2319_1910619225}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x1708575458}

[[Radio]{lang="IT"}]{#struct_0_x1035_x2319_x1018612753}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_450524877}

[[network-admin]{lang="IT"}]{#struct_0_x1035_x2319_x551046151}

[[mdc-admin]{lang="IT"}]{#struct_0_x1035_x2319_x1040763393}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_357257173}

[**[all]{lang="IT"}**]{#struct_0_x1035_x2319_x1080838069}[：]{style="font-family:宋体"}[完全匹配模式。只有客户端的信道能力集与设备的信道能力集全部匹配]{style="font-family:宋体"}[，]{style="font-family:宋体"}[才允许客户端上线]{style="font-family:宋体"}[，]{style="font-family:宋体"}[否则]{style="font-family:宋体"}[，]{style="font-family:宋体"}[不允许客户端上线。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_x1035_x2319_x685845017}[：不检查模式，即不检查客户端的信道能力集。]{style="font-family:宋体"}

[**[partial]{lang="IT"}**]{#struct_0_x1035_x2319_x626357131}[：]{style="font-family:宋体"}[部分匹配模式。客户端的信道能力集与设备的信道能力集只要有一个匹配，则允许客户端上线，否则，不允许客户端上线。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x836203400}

[[只有在射频工作在]{style="font-family:宋体"}[5GHz]{lang="EN-US"}]{#struct_0_x1035_x2319_973559436}[模式下并且开启频谱管理功能，信道能力集检查功能才会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_1182818353}

[[\# ]{lang="EN-US"}]{#struct_0_x1035_x2319_x1115559064}[配置对客户端信道能力集的检查模式为完全匹配模式。]{style="font-family:宋体"}

[[\<]{lang="EN-US"}[Sysname]{lang="EN-US"}]{#struct_0_x1035_x2319_1449375788}[\> system-view]{lang="EN-US"}

[[\[Sysname]{lang="EN-US"}]{#struct_0_x1035_x2319_x1526077920}[\] ]{lang="EN-US"}[wlan ap ap1 model WA4620i-ACN]{lang="IT"}

[[\[Sysname-wlan-ap-ap1\] radio 1]{lang="IT"}]{#struct_0_x1035_x2319_x1829915706}

[[\[Sysname-wlan-ap-ap1-radio-1\] spectrum-management enable]{lang="IT"}]{#struct_0_x1035_x2319_724124468}

[[\[Sysname-]{lang="EN-US"}]{#struct_0_x1035_x2319_1106401194}[wlan-ap]{lang="IT"}[-ap1-radio-1]{lang="IT"}[\]]{lang="EN-US"}[ channel-capability mode all]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_820942856}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[spectrum-management]{lang="EN-US"}**]{#struct_0_x1035_x2319_x1248665119}
:::

::: {#-410176918 .myid}
[]{#_Toc404795313}[]{#struct_0_x1035_x2319_916770323}[]{#_Toc401841495}[]{#_Toc396742901}[]{#_Toc393118435}

**WLAN RRM \-- WLAN RRM配置命令 \-- channel-switch mode**

------------------------------------------------------------------------

[**[channel-switch]{lang="EN-US"}**]{#struct_0_x1035_x2319_x803614905}**[ mode]{lang="IT"}**[命令用于配置]{style="font-family:宋体"}[信道切换模式。]{style="font-family:宋体"}

[**[undo channel-switch mode]{lang="IT"}**]{#struct_0_x1035_x2319_x534461424}[命令用于恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_1613324291}

[**[channel-switch mode ]{lang="IT"}**]{#struct_0_x1035_x2319_x965355606}[{ **continuous** \| ]{lang="IT"}**[suspend ]{lang="IT"}**[}]{lang="IT"}

[**[undo channel-switch mode]{lang="IT"}**]{#struct_0_x1035_x2319_2114676714}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_662168093}

[[已上线的客户端停止发送帧。]{style="font-family:宋体"}]{#struct_0_x1035_x2319_x65465035}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x2029784369}

[[Radio]{lang="IT"}]{#struct_0_x1035_x2319_543016284}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x174658262}

[[network-admin]{lang="IT"}]{#struct_0_x1035_x2319_x516137493}

[[mdc-admin]{lang="IT"}]{#struct_0_x1035_x2319_262948523}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_1694616078}

[**[continuous]{lang="IT"}**]{#struct_0_x1035_x2319_47240350}[：]{style="font-family:宋体"}[信道发生切换期间]{style="font-family:宋体"}[，]{style="font-family:宋体"}[已上线的客户端可以继续发送帧。]{style="font-family:宋体"}

[**[suspend]{lang="IT"}**]{#struct_0_x1035_x2319_x310917713}[：]{style="font-family:宋体"}[信道发生切换期间]{style="font-family:宋体"}[，]{style="font-family:宋体"}[已上线的客户端停止发送帧]{style="font-family:宋体"}[，]{style="font-family:宋体"}[直到信道切换完成。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_24987550}

[[只有在射频为]{style="font-family:宋体"}[5GHz]{lang="EN-US"}]{#struct_0_x1035_x2319_x394877343}[模式下并且开启频谱管理功能，信道切换模式才会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x410936512}

[[\# ]{lang="EN-US"}]{#struct_0_x1035_x2319_x1091650503}[配置信道发生切换期间，已上线的客户端可以继续发送帧。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1035_x2319_x1865451495}

[\[Sysname\] ]{lang="EN-US"}[wlan ap ap1 model WA4620i-ACN]{lang="IT"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="IT"}

[\[Sysname-]{lang="EN-US"}[wlan-ap-ap1-radio-1]{lang="IT"}[\] ]{lang="EN-US"}[spectrum-management enable]{lang="IT"}

[\[Sysname-]{lang="EN-US"}[wlan-ap-ap1-radio-1]{lang="IT"}[\] channel-switch mode continuous]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_227237203}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[spectrum-management]{lang="EN-US"}**]{#struct_0_x1035_x2319_1194070298}
:::

::: {#1161513010 .myid}
[]{#_Toc404795314}[]{#struct_0_x1035_x2319_1835653898}

**WLAN RRM \-- WLAN RRM配置命令 \-- crc-error-threshold**

------------------------------------------------------------------------

[**[crc-error-threshold]{lang="EN-US"}**]{#struct_0_x1035_x2319_x805992069}[命令用来配置]{style="font-family:宋体"}[CRC]{lang="EN-US"}[错误门限值]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo crc-error-threshold]{lang="EN-US"}**]{#struct_0_x1035_x2319_129960075}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x1663674266}

[**[crc-error-threshold ]{lang="EN-US"}***[percent]{lang="EN-US"}*]{#struct_0_x1035_x2319_1968042852}

[**[undo crc-error-threshold]{lang="EN-US"}**]{#struct_0_x1035_x2319_x1314833147}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x1901974619}

[[CRC]{lang="EN-US"}]{#struct_0_x1035_x2319_1792753246}[错误门限]{style="font-family:宋体"}[值为]{style="font-family:宋体"}[20]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x580126090}

[[RRM]{lang="EN-US"}]{#struct_0_x1035_x2319_x1614336621}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x1333035513}

[[network-admin]{lang="EN-US"}]{#struct_0_x1035_x2319_63527134}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1035_x2319_x312953193}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x877169350}

[*[percent]{lang="EN-US"}*]{#struct_0_x1035_x2319_472311942}[：]{style="font-family:宋体"}[CRC]{lang="EN-US"}[错误门限值]{style="font-family:宋体"}[，以百分比表示，取值范围]{style="font-family:宋体"}[为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x864471056}

[[\# ]{lang="EN-US"}]{#struct_0_x1035_x2319_x1932421662}[配置]{style="font-family:宋体"}[CRC]{lang="EN-US"}[错误门限值]{style="font-family:宋体"}[为]{style="font-family:宋体"}[50]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1035_x2319_x10944914}

[\[Sysname\] wlan ap ap1 model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1\] rrm]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1-rrm\] crc-error-threshold 50]{lang="EN-US"}
:::

::: {#-1270898104 .myid}
[]{#_Toc404795315}[]{#struct_0_x1035_x2319_x2130113831}

**WLAN RRM \-- WLAN RRM配置命令 \-- interference-threshold**

------------------------------------------------------------------------

[**[interference-threshold]{lang="EN-US"}**]{#struct_0_x1035_x2319_x936130109}[命令用来配置信道干扰门限值。]{style="font-family:宋体"}

[**[undo interference-threshold]{lang="EN-US"}**]{#struct_0_x1035_x2319_x384310768}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_611992719}

[**[interference-threshold ]{lang="EN-US"}***[percent]{lang="EN-US"}*]{#struct_0_x1035_x2319_x1169400615}

[**[undo interference-threshold]{lang="EN-US"}**]{#struct_0_x1035_x2319_x1893673695}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_1606009272}

[[信道]{style="font-family:宋体"}]{#struct_0_x1035_x2319_x997704349}[干扰门限值为]{style="font-family:宋体"}[50]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_495974576}

[[RRM]{lang="EN-US"}]{#struct_0_x1035_x2319_x821048978}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_1227793737}

[[network-admin]{lang="EN-US"}]{#struct_0_x1035_x2319_1003721043}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1035_x2319_x1064003544}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_361316549}

[*[percent]{lang="EN-US"}*]{#struct_0_x1035_x2319_1342414552}[：信道干扰门限，以百分比表示，取值范围为]{style="font-family:宋体"}[40]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x1952943903}

[[\# ]{lang="EN-US"}]{#struct_0_x1035_x2319_x349058943}[配置信道]{style="font-family:宋体"}[干扰门限值为]{style="font-family:
宋体"}[60]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1035_x2319_271824190}

[\[Sysname\] wlan ap ap1 model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1\] rrm]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1-rrm\] interference-threshold 60]{lang="EN-US"}
:::

::: {#-920768496 .myid}
[]{#struct_0_x1035_x2319_x1068504897}[]{#_Toc404795316}[]{#_Toc401841496}[]{#_Toc396742902}[]{#_Toc393118438}

**WLAN RRM \-- WLAN RRM配置命令 \-- power-capability mode**

------------------------------------------------------------------------

[**[power-capability mode]{lang="IT"}**]{#struct_0_x1035_x2319_1778699443}[命令用于配置对客户端功率能力集的检查模式。]{style="font-family:宋体"}

[**[undo power-capability mode]{lang="IT"}**]{#struct_0_x1035_x2319_1130896205}[命令用于恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_853874940}

[**[power-capability mode]{lang="IT"}**]{#struct_0_x1035_x2319_x1749459235}[ { **all** \| ]{lang="IT"}**[none ]{lang="IT"}**[\| ]{lang="IT"}**[partial ]{lang="IT"}**[}]{lang="IT"}

[**[undo power-capability mode]{lang="IT"}**]{#struct_0_x1035_x2319_608684893}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x1041582560}

[[不检查客户端功率能力集。]{style="font-family:宋体"}]{#struct_0_x1035_x2319_x764027419}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_1188384925}

[[Radio]{lang="IT"}]{#struct_0_x1035_x2319_787106307}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x384921571}

[[network-admin]{lang="IT"}]{#struct_0_x1035_x2319_x570181147}

[[mdc-admin]{lang="IT"}]{#struct_0_x1035_x2319_x997880484}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_143664817}

[**[all]{lang="IT"}**]{#struct_0_x1035_x2319_x600524374}[：]{style="font-family:宋体"}[完全匹配模式。只有客户端的功率能力集与设备的功率能力集全部匹配]{style="font-family:宋体"}[，]{style="font-family:宋体"}[才允许客户端上线]{style="font-family:宋体"}[，]{style="font-family:宋体"}[否则]{style="font-family:宋体"}[，]{style="font-family:宋体"}[不允许客户端上线。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_x1035_x2319_x712209001}[：不检查模式，即不检查客户端的功率能力集。]{style="font-family:宋体"}

[**[partial]{lang="IT"}**]{#struct_0_x1035_x2319_x1984298441}[：]{style="font-family:宋体"}[部分匹配模式。客户端的功率能力集与设备的功率能力集只要有一个匹配，则允许客户端上线，否则，不允许客户端上线。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_286737068}

[[只有在]{style="font-family:宋体"}]{#struct_0_x1035_x2319_x464304464}[射频]{style="font-family:宋体"}[为]{style="font-family:宋体"}[5GHz]{lang="IT"}[模式下并且开启频谱管理功能]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[功率能力集检查功能才会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_1947661141}

[[\# ]{lang="EN-US"}]{#struct_0_x1035_x2319_1148893227}[配置对客户端功率能力集的检查模式为完全匹配模式。]{style="font-family:宋体"}

[[\<]{lang="EN-US"}[Sysname]{lang="EN-US"}]{#struct_0_x1035_x2319_1241959989}[\> system-view]{lang="EN-US"}

[[\[Sysname]{lang="EN-US"}]{#struct_0_x1035_x2319_x1261806550}[\] ]{lang="EN-US"}[wlan ap ap1 model WA4620i-ACN]{lang="IT"}

[[\[Sysname-wlan-ap-ap1\] radio 1]{lang="IT"}]{#struct_0_x1035_x2319_1541218654}

[[\[Sysname-wlan-ap-ap1-radio-1\] spectrum-management enable]{lang="IT"}]{#struct_0_x1035_x2319_x854071052}

[[\[Sysname-]{lang="EN-US"}]{#struct_0_x1035_x2319_2016674354}[wlan-ap]{lang="IT"}[-ap1-radio-1]{lang="IT"}[\]]{lang="EN-US"}[ power-capability mode all]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x1996764329}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[spectrum-management]{lang="EN-US"}**]{#struct_0_x1035_x2319_x922829794}
:::

::: {#1518345216 .myid}
[]{#_Toc404795317}[]{#struct_0_x1035_x2319_476191574}[]{#_Toc401841497}[]{#_Toc396742903}[]{#_Toc393118434}

**WLAN RRM \-- WLAN RRM配置命令 \-- power-constraint mode**

------------------------------------------------------------------------

[**[power-constraint mode]{lang="IT"}**]{#struct_0_x1035_x2319_1081771138}[命令用于配置功率限制模式。]{style="font-family:宋体"}

[**[undo power-constraint mode]{lang="IT"}**]{#struct_0_x1035_x2319_x1126437969}[命令]{style="font-family:宋体"}[用于恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_972416643}

[**[power-constraint mode ]{lang="IT"}**]{#struct_0_x1035_x2319_x1344444269}[{ **auto** \[ **anpi-interval** *anpi-interval-value* \] \| **manual** *power-constraint* }]{lang="IT"}

[**[undo power-constraint mode]{lang="IT"}**]{#struct_0_x1035_x2319_x1722896531}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x591643397}

[[功率限制模式为自动模式。]{style="font-family:宋体"}]{#struct_0_x1035_x2319_2057291934}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_450590413}

[[Radio]{lang="EN-US"}]{#struct_0_x1035_x2319_262660108}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x2021876685}

[[network-admin]{lang="EN-US"}]{#struct_0_x1035_x2319_x925228094}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1035_x2319_1137747333}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x472664340}

[**[auto]{lang="EN-US"}**]{#struct_0_x1035_x2319_649778481}[：配置限制功率模式为自动模式。]{style="font-family:宋体"}

[**[anpi-interval ]{lang="IT"}**]{#struct_0_x1035_x2319_x140833652}*[anpi-interval-value]{lang="IT"}*[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[ANPI]{lang="EN-US"}[差值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[dBm]{lang="EN-US"}[。缺省值为]{style="font-family:宋体"}[10dBm]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[manual]{lang="EN-US"}**]{#struct_0_x1035_x2319_x902980302}*[ ]{lang="EN-US"}[power-constraint]{lang="IT"}*[：配置手动限制功率数值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[dBm]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x1548815929}

[[·[              ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;
font-family:Symbol"}[当配置为]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1035_x2319_x2040870281}[手动]{style="font-family:宋体"}[模式时]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[设备会通知]{lang="EN-US" style="font-family:
宋体"}[802.11a]{lang="IT"}[客户端将其发送功率降低]{lang="EN-US" style="font-family:
宋体"}*[power-constraint]{lang="IT"}*[ dBm]{lang="IT"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;
font-family:Symbol"}[当配置为自动模式时]{style="font-family:宋体"}]{#struct_0_x1035_x2319_x1115493528}[，]{style="font-family:宋体"}[设备会根据接收信道功率参数、平均噪底功率、]{style="font-family:宋体"}[ANPI]{lang="EN-US"}[差值计算出限制功率值。计算公式]{style="font-family:宋体"}[：]{style="font-family:宋体"}*[power-constraint]{lang="IT" style="color:black"}*[ = ]{lang="IT"}[接收信道功率参数]{style="font-family:宋体"}[RCPI]{lang="IT"}[-]{lang="IT"}[（]{style="font-family:宋体"}[平均噪底功率]{style="font-family:
宋体"}[ANPI+*[anpi-interval-value]{style="color:black"}*]{lang="IT"}[）]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[只有在]{style="font-family:宋体"}]{#struct_0_x1035_x2319_1165320409}[射频]{style="font-family:宋体"}[为]{style="font-family:宋体"}[5GHz]{lang="IT"}[模式下并且开启频谱管理功能，功率限制功能才会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_485905391}

[[\# ]{lang="EN-US"}]{#struct_0_x1035_x2319_x1829588418}[配置]{style="font-family:宋体"}[5GHz]{lang="EN-US"}[模式下客户端的功率限制模式为手动模式，功率限制值为]{style="font-family:宋体"}[5dBm]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1035_x2319_777159324}

[\[Sysname\] ]{lang="EN-US"}[wlan ap ap1 model WA4620i-ACN]{lang="IT"}

[\[Sysname-]{lang="EN-US"}[wlan-ap-ap1]{lang="IT"}[\] ]{lang="EN-US"}[radio 1]{lang="IT"}

[[\[Sysname-wlan-ap-ap1-radio-1\] spectrum-management enable]{lang="IT"}]{#struct_0_x1035_x2319_x1114206316}

[[\[Sysname-wlan-ap-ap1-radio-1\] power-constraint mode manual 5]{lang="IT"}]{#struct_0_x1035_x2319_881257357}

[[\# ]{lang="EN-US"}]{#struct_0_x1035_x2319_x803618667}[配置]{style="font-family:宋体"}[5GHz]{lang="EN-US"}[模式下客户端的功率限制模式为自动模式，]{style="font-family:宋体"}[ANPI]{lang="IT"}[差值为]{style="font-family:宋体"}[15dBm]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1035_x2319_1746638462}

[\[Sysname\] ]{lang="EN-US"}[wlan ap ap1 model WA4620i-ACN]{lang="IT"}

[\[Sysname-]{lang="EN-US"}[wlan-ap-ap1]{lang="IT"}[\] ]{lang="EN-US"}[radio 1]{lang="IT"}

[[\[Sysname-wlan-ap-ap1-radio-1\] spectrum-management enable]{lang="IT"}]{#struct_0_x1035_x2319_165603429}

[[\[Sysname-wlan-ap-ap1-radio-1\] power-constraint mode auto apni-interval 15]{lang="IT"}]{#struct_0_x1035_x2319_1613389827}

[\[Sysname-WLAN-Radio1/0/1\] power-constraint mode auto apni-interval 15]{lang="EN-US"}

[[【项目命令】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_1751266690}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[spectrum-management]{lang="EN-US"}**]{#struct_0_x1035_x2319_744843689}
:::

::: {#1344609415 .myid}
[]{#_Toc404795318}[]{#struct_0_x1035_x2319_x1645706298}

**WLAN RRM \-- WLAN RRM配置命令 \-- rrm**

------------------------------------------------------------------------

[**[rrm]{lang="EN-US"}**]{#struct_0_x1035_x2319_1592993212}[命令用来进入]{style="font-family:宋体"}[RRM]{lang="EN-US"}[（]{style="font-family:宋体"}[Radio Resource Management]{lang="EN-US"}[，射频资源管理）视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x445515341}

[**[rrm]{lang="EN-US"}**]{#struct_0_x1035_x2319_x1631014046}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x1201533001}

[[Radio]{lang="EN-US"}]{#struct_0_x1035_x2319_x128622574}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x1190270255}

[[network-admin]{lang="EN-US"}]{#struct_0_x1035_x2319_758091264}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1035_x2319_x801606238}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x2015307049}

[[\# ]{lang="EN-US"}]{#struct_0_x1035_x2319_x1386468803}[进入]{style="font-family:宋体"}[RRM]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1035_x2319_x1255788131}

[\[Sysname\] wlan ap ap1 WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1\] rrm]{lang="EN-US"}
:::

::: {#-1221934998 .myid}
[]{#_Toc404795319}[]{#struct_0_x1035_x2319_561811545}

**WLAN RRM \-- WLAN RRM配置命令 \-- tolerance-level**

------------------------------------------------------------------------

[**[tolerance-level]{lang="EN-US"}**]{#struct_0_x1035_x2319_562778573}[命令用来配置容限系数。]{style="font-family:宋体"}

[**[undo tolerance-level]{lang="EN-US"}**]{#struct_0_x1035_x2319_1523500462}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_493302586}

[**[tolerance-level ]{lang="EN-US"}***[percent]{lang="EN-US"}*]{#struct_0_x1035_x2319_x467748597}

[**[undo tolerance-level]{lang="EN-US"}**]{#struct_0_x1035_x2319_753564824}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_2044567362}

[[容限系数为]{style="font-family:宋体"}[20]{lang="EN-US"}]{#struct_0_x1035_x2319_609415283}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_1146507662}

[[RRM]{lang="EN-US"}]{#struct_0_x1035_x2319_x129172442}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_1535175175}

[[network-admin]{lang="EN-US"}]{#struct_0_x1035_x2319_x1790849543}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1035_x2319_986118656}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_292564313}

[*[percent]{lang="EN-US"}*]{#struct_0_x1035_x2319_x1969977999}[：容限系数，以百分比表示，取值范围为]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[45]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x752090579}

[[当]{style="font-family:宋体"}[CRC]{lang="EN-US"}]{#struct_0_x1035_x2319_1407971747}[错误门限或干扰门限超过门限值时，]{style="font-family:宋体"}[AC]{lang="EN-US"}[会开始计算信道质量，但只有在新的信道和旧信道的信道质量差超过容限系数时，新的信道才会被应用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:
黑体"}]{#struct_0_x1035_x2319_2135906}

[[\# ]{lang="EN-US"}]{#struct_0_x1035_x2319_x1012130882}[配置]{style="font-family:宋体"}[容限系数为]{style="font-family:宋体"}[25]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1035_x2319_x426596892}

[\[Sysname\] wlan ap ap1 model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1\] rrm]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1-rrm\] tolerance-level 25]{lang="EN-US"}
:::

::: {#-1714733339 .myid}
[]{#_Toc404795320}[]{#struct_0_x1035_x2319_x1518778055}[]{#_Toc401841500}[]{#_Toc396742906}[]{#_Toc393118433}[]{#_Toc390700022}

**WLAN RRM \-- WLAN RRM配置命令 \-- spectrum-management**

------------------------------------------------------------------------

[**[spectrum]{lang="EN-US"}**]{#struct_0_x1035_x2319_x1451224622}**[-management enable]{lang="IT"}**[命令用于开启频谱管理功能。]{style="font-family:宋体"}

[**[spectrum]{lang="EN-US"}**]{#struct_0_x1035_x2319_x1890580143}**[-management disable]{lang="IT"}**[命令用于开启频谱管理功能。]{style="font-family:宋体"}

[**[undo spectrum-management]{lang="IT"}**]{#struct_0_x1035_x2319_936399129}[命令用于恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_497644580}

[**[spectrum-management ]{lang="IT"}**]{#struct_0_x1035_x2319_x937591207}[{ **enable** \| **disable** }]{lang="IT"}

[**[undo spectrum-management]{lang="IT"}**]{#struct_0_x1035_x2319_x742363687}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x316171159}

[[频谱管理功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x1035_x2319_816471420}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_871317438}

[[Radio]{lang="EN-US"}]{#struct_0_x1035_x2319_758640960}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_1538403530}

[[network-admin]{lang="IT"}]{#struct_0_x1035_x2319_1390250292}

[[mdc-admin]{lang="IT"}]{#struct_0_x1035_x2319_x1714923290}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_1477698376}

[[\# ]{lang="EN-US"}]{#struct_0_x1035_x2319_x1882746906}[开启频谱管理功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1035_x2319_x1068439361}

[\[Sysname\] ]{lang="EN-US"}[wlan ap ap1 model WA4620i-ACN]{lang="IT"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="IT"}

[\[Sysname-]{lang="EN-US"}[wlan-ap-ap1-radio-1]{lang="IT"}[\] spectrum-management enable]{lang="EN-US"}
:::

::: {#665546296 .myid}
[]{#_Toc404795321}[]{#struct_0_x1035_x2319_1273698316}

**WLAN RRM \-- WLAN RRM配置命令 \-- wlan calibrate-channel pronto ap all**

------------------------------------------------------------------------

[**[wlan calibrate-channel pront]{lang="EN-US"}[o ap all]{lang="EN-US"}**]{#struct_0_x1035_x2319_2019135468}[命令用来配置手动触发所有]{style="font-family:宋体"}[AP]{lang="EN-US"}[进行自动信道调整。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_1769100814}

[**[wlan calibrate-channel pronto ap all]{lang="EN-US"}**]{#struct_0_x1035_x2319_1684100011}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_2116056913}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1035_x2319_x1742764699}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x314517987}

[[network-admin]{lang="EN-US"}]{#struct_0_x1035_x2319_177948449}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1035_x2319_x1260910857}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_1511298746}

[[执行]{style="font-family:宋体"}**[wlan calibrate-channel pronto ap all]{lang="EN-US"}**]{#struct_0_x1035_x2319_x1339184574}[命令可能会占用较多系统资源，请谨慎使用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x42958166}

[[\# ]{lang="EN-US"}]{#struct_0_x1035_x2319_x896698922}[配置手动触发所有]{style="font-family:宋体"}[AP]{lang="EN-US"}[进行自动信道调整。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1035_x2319_793411981}

[\[Sysname\] wlan calibrate-channel pronto ap all]{lang="EN-US"}
:::

::: {#-1354065966 .myid}
[]{#_Toc404795322}[]{#struct_0_x1035_x2319_1691364276}

**WLAN RRM \-- WLAN RRM配置命令 \-- wlan calibrate-power pronto ap all**

------------------------------------------------------------------------

[**[wlan calibrate-power pronto ]{lang="EN-US"}[ap all]{lang="EN-US"}**]{#struct_0_x1035_x2319_2094607164}[命令用来配置手动触发所有]{style="font-family:宋体"}[AP]{lang="EN-US"}[进行自动功率调整。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_326156555}

[**[wlan calibrate-power pronto ap all]{lang="EN-US"}**]{#struct_0_x1035_x2319_1192530611}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x1308665845}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1035_x2319_x176680758}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x320994620}

[[network-admin]{lang="EN-US"}]{#struct_0_x1035_x2319_x379506865}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1035_x2319_x1827422716}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x595659107}

[[执行]{style="font-family:宋体"}**[wlan calibrate-power pronto ap all]{lang="EN-US"}**]{#struct_0_x1035_x2319_x1284109069}[命令可能会占用较多系统资源，请谨慎使用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x1394156154}

[[\# ]{lang="EN-US"}]{#struct_0_x1035_x2319_x74086616}[配置手动触发所有]{style="font-family:宋体"}[AP]{lang="EN-US"}[进行自动功率调整。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1035_x2319_1380996653}

[\[Sysname\] wlan calibrate-power pronto ap all]{lang="EN-US"}
:::

::: {#1463506522 .myid}
[]{#_Toc404795323}[]{#struct_0_x1035_x2319_1650286470}

**WLAN RRM \-- WLAN RRM配置命令 \-- wlan rrm-calibration-interval**

------------------------------------------------------------------------

[**[wlan rrm-calibration-interval]{lang="EN-US"}**]{#struct_0_x1035_x2319_x216045133}[命令用来配置信道和功率调整的校准间隔。]{style="font-family:
宋体"}

[**[undo wlan rrm-calibration-interval]{lang="EN-US"}**]{#struct_0_x1035_x2319_x949080181}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_1389403183}

[**[wlan rrm-calibration-interval ]{lang="EN-US"}***[minutes]{lang="EN-US"}*]{#struct_0_x1035_x2319_x1225653669}

[**[undo wlan rrm-calibration-interval]{lang="EN-US"}**]{#struct_0_x1035_x2319_796906862}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_338924908}

[[信道和功率调整的校准间隔是]{style="font-family:宋体"}[8]{lang="EN-US"}]{#struct_0_x1035_x2319_1924873849}[分钟]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x1939959635}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1035_x2319_x1206066729}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_1900072403}

[[network-admin]{lang="EN-US"}]{#struct_0_x1035_x2319_2107325108}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1035_x2319_x743219763}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_425929240}

[*[minutes]{lang="EN-US"}*]{#struct_0_x1035_x2319_290793242}[：信道和功率调整的校准间隔，取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[180]{lang="EN-US"}[，单位为分钟]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1035_x2319_x594596632}

[[\# ]{lang="EN-US"}]{#struct_0_x1035_x2319_581766972}[配置校准间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1035_x2319_1268131106}

[\[Sysname\] wlan rrm-calibration-interval 10]{lang="EN-US"}

[ ]{lang="IT"}
:::
