<!-- CMD-INDEX
  display wlan rrm-history ap         | ]                | L23
  display wlan rrm-status ap          | ]                | L159
  adjacency-factor                    | RRM视图            | L413
  calibrate-channel self-decisive     | RRM视图            | L459
  calibrate-power min                 | RRM视图            | L501
  calibrate-power self-decisive       | RRM视图            | L551
  calibrate-power threshold           | RRM视图            | L593
  channel-capability mode             | Radio视图          | L639
  channel-switch mode                 | Radio视图          | L697
  crc-error-threshold                 | RRM视图            | L753
  interference-threshold              | RRM视图            | L799
  power-capability mode               | Radio视图          | L845
  power-constraint mode               | Radio视图          | L903
  rrm                                 | Radio视图          | L979
  tolerance-level                     | RRM视图            | L1011
  spectrum-management                 | Radio视图          | L1061
  wlan calibrate-channel pronto ap all | 系统视图             | L1103
  wlan calibrate-power pronto ap all  | 系统视图             | L1135
  wlan rrm-calibration-interval       | 系统视图             | L1167
-->

**WLAN RRM \-- WLAN RRM配置命令 \-- display wlan rrm-history ap**

------------------------------------------------------------------------

**[display wlan rrm-history ap**]命令用来显示AP的信道和功率调整历史信息。

【命令】

**[display wlan rrm-history ap ***[ap-name *}]

【视图】]

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[all**]：所有AP。

**[name*** ap-name*]：AP名称，为1～63个字符的字符串，不区分大小写。

【使用指导】

该命令显示所有或指定AP上最近3次改变的信道或功率的详细信息。显示输出包括改变时间、触发原因、功率、干扰等参数。

【举例】

\# 显示ap1的RRM历史信息。

\<Sysname\> display wlan rrm-history ap name ap1

                         AP RRM History

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Flags : I - Interference,   P - Packets discarded,    F - Retransmission,

         R - Radar,          C - Coverage,             O - Others

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

                         AP RRM History : ap1

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Radio : 1                                Basic BSSID : 000f-e2ff-7700

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

        Ch  Power Load Util Intf PER Retry Reason  Date         Time

            (dBm) (%)  (%)  (%)  (%) (%)           (yyyy-mm-dd) (hh:mm:ss)

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Before 6   20    24   2    21   11  18    -P\-\-\--  2014-07-07   17:31:50

 After  1   20    9    0    8    0   27    -       -            -

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Before 1   20    54   1    53   11  15    IP\-\-\--  2014-07-08   12:19:50

 After  6   20    10   0    10   3   29    -       -            -

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Before 6   20    29   1    28   21  20    -P\-\-\--  2014-07-08   12:59:50

 After  1   20    30   0    29   2   24    -       -            -

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

表1-1 display wlan rrm-history命令显示信息描述表

字段

描述

Radio

AP的Radio ID

Basic BSSID

基本服务集标识

Ch

Radio的工作信道

Power

Radio的发送功率

Load

信道的负载，以百分比表示

Util

信道的利用率，以百分比显示

Intf

信道检测到的干扰，以百分比表示

PER

信道检测到的误码率，以百分比表示

Retry

信道检测到的重传率，以百分比表示

Reason

信道或功率调整的原因

Date

发生信道或功率调整的日期

Time

发生信道或功率调整的时间

**WLAN RRM \-- WLAN RRM配置命令 \-- display wlan rrm-status ap**

------------------------------------------------------------------------

**[display wlan rrm-status ap**]命令用来显示AP上射频的RRM详细信息。

【命令】

**[display wlan rrm-status ap ***[ap-name *}]

【视图】]

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[all**]：所有AP。

**[name*** ap-name*]：AP名称，为1～63个字符的字符串，不区分大小写。

【使用指导】

在AC设备上，如果信道和功率调整处于关闭状态，则执行此命令时，只会显示AP上Radio的工作信道和功率级别，其它信息如干扰、邻居的数量等不会显示。

【举例】

\# 显示ap1的信道和功率调整详细信息。

\<Sysname\> display wlan rrm-status ap name ap1

                          AP RRM Profile : ap1

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Radio   : 1                              Basic BSSID    : 70f9-6d31-2fe0

 Channel : 157                            Tx Power (dBm) : 18

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

    Ch    Nbrs    Load    Util    Intf    PER    Retry    Radar

                  (%)     (%)     (%)     (%)     (%)

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

    36    0       0       -       0       0      -        -

    40    0       0       -       0       0      -        -

    44    0       0       -       0       0      -        -

    48    0       0       -       0       0      -        -

    52    0       0       -       0       0      -        -

    56    0       0       -       0       0      -        -

    60    0       0       -       0       0      -        -

    64    0       0       -       0       0      -        -

    100   0       0       -       0       0      -        -

    104   0       0       -       0       0      -        -

    108   0       0       -       0       0      -        -

    112   0       0       -       0       0      -        -

    116   0       0       -       0       0      -        -

    132   0       0       -       0       0      -        -

    136   0       0       -       0       0      -        -

    140   0       0       -       0       0      -        -

    149   1       0       -       0       0      -        -

    153   4       0       -       0       0      -        -

    157   0       0       0       0       0      0        -

    161   2       0       -       0       0      -        -

    165   0       0       -       0       0      -        -

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

   Nbr-BasicBSSID   Ch    Intf   SignalStrength   Type

                           (%)    (dBm)

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

   000f-e212-ff01   161   0      -60              Unmanaged

   5866-ba74-e461   153   0      -72              Unmanaged

   70f9-6d30-9020   153   0      -40              Managed

   70f9-6d31-3080   149   0      -54              Managed

   70f9-6d31-34e0   161   0      -59              Managed

   7425-8a86-bbe0   153   0      -48              Unmanaged

   7425-8a86-c720   153   0      -63              Unmanaged

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Radio   : 2                              Basic BSSID    : 70f9-6d31-2ff0

 Channel : 1                              Tx Power (dBm) : 19

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

    Ch    Nbrs    Load    Util    Intf    PER    Retry    Radar

                  (%)     (%)     (%)     (%)     (%)

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

    1     6       4       0       4       0      0        -

    6     4       2       -       2       0      -        -

    11    6       2       -       2       0      -        -

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

   Nbr-BasicBSSID   Ch    Intf   SignalStrength   Type

                           (%)    (dBm)

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

   000f-e212-ff11   1     49     -77              Unmanaged

   0023-89e1-ed00   11    0      -87              Unmanaged

   006a-55f6-ae10   1     57     -88              Unmanaged

   5866-ba64-aa31   1     10     -60              Unmanaged

   5866-ba74-e471   6     0      -76              Unmanaged

   5866-baa9-a610   11    0      -62              Unmanaged

   70f9-6d30-9030   6     0      -63              Managed

   70f9-6d31-3090   1     51     -86              Managed

   70f9-6d31-34f0   6     0      -85              Managed

   7425-8a86-bbf0   6     0      -73              Unmanaged

   7425-8a86-c731   11    0      -93              Unmanaged

   80f6-2ec0-3330   11    0      -76              Unmanaged

   80f6-2ec0-3331   11    0      -73              Unmanaged

   80f6-2edd-d2d0   1     40     -60              Unmanaged

   80f6-2edd-d2d1   1     44     -68              Unmanaged

   80f6-2ede-0b30   11    0      -74              Unmanaged

表1-2 display wlan rrm-status命令显示信息描述表

字段

描述

Radio

AP的Radio ID

Basic BSSID

基本服务集标识

Channel

Radio当前的工作信道

Tx Power

Radio的发送功率

Ch

Radio支持的工作信道

Nbrs

信道中的AP邻居数量

Load

信道的负载，以百分比表示。信道的负载指的是在该信道上，AP发送报文/接收客户端的报文和干扰，这里的干扰指该AP接收到其它AP和客户端发送的错误报文

Util

信道利用率，以百分比显表示。信道利用率指的是在该信道上，AP发送报文/接收客户端的报文

Intf

信道检测到的干扰，以百分比表示

PER

信道检测到的误码率，以百分比表示

Retry

信道检测到的重传率，以百分比表示

Radar

雷达检测状态：

·-表示没有检测到雷达

·Detected表示检测到雷达

Nbr-BasicBSSID

邻居AP的Radio接口的MAC地址

SignalStrength

检测到邻居AP的信号强度，以dBm为单位

Type

AP类型：

·Unmanaged：该AP能探到的非邻居AP

·Managed：该AP能探测到的邻居AP

**WLAN RRM \-- WLAN RRM配置命令 \-- adjacency-factor**

------------------------------------------------------------------------

**[adjacency-factor**]命令用来配置当前Radio所在频段上触发功率调整的最大邻居数和在邻居AP的功率排名中指定AP。

**[undo adjacency-factor**]命令用来恢复缺省情况。

【命令】

**[adjacency-factor ***neighbor*]

**[undo adjacency-factor**]

【缺省情况】

触发功率调整的最大邻居数为3和在邻居AP的功率排名中指定排名第3位的邻居AP，即需要和功率调整门限值进行比较的AP为在所有邻居AP中信号强度排在第3位的邻居AP。

【视图】

RRM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[neighbor*]：触发功率调整的最大邻居数和在邻居AP的功率排名中指定AP，即需要和功率调整门限值进行比较的邻居AP，取值范围为1～16。

【举例】

\# 配置当前Radio所在频段上触发功率调整的最大邻居数为7，需要和功率调整门限值进行比较的AP为在所有邻居AP中信号强度排在第7位的邻居AP。

\<Sysname\> system-view

Sysname wlan ap ap1

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 rrm

Sysname-wlan-ap-ap1-radio-1-rrm adjacency-factor 7

**WLAN RRM \-- WLAN RRM配置命令 \-- calibrate-channel self-decisive**

------------------------------------------------------------------------

**[calibrate-channel self-decisive**]命令用来开启定时触发自动信道调整。

**[undo calibrate-channel self-decisive**]命令用来恢复缺省情况。

【命令】

**[calibrate-channel self-decisive**]

**[undo calibrate-channel self-decisive**]

【缺省情况】

定时触发自动信道调整处于关闭状态。

【视图】

RRM视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 配置定时触发自动信道调整。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 rrm

Sysname-wlan-ap-ap1-radio-1-rrm calibrate-channel self-decisive

**WLAN RRM \-- WLAN RRM配置命令 \-- calibrate-power min**

------------------------------------------------------------------------

**[calibrate-power min**]命令用来配置AP的最小发送功率。

**[undo calibrate-power min**]命令用来恢复缺省情况。

【命令】

**[calibrate-power min ***tx-power*]

**[undo calibrate-power min**]

【缺省情况】

AP的最小发送功率为1dBm。

【视图】

RRM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[tx-power*]：AP的最小发送功率，取值范围为1～20，单位为dBm。

【使用指导】

调整AP功率后（包括手动调整、自动调整），AP的发送功率不能小于**calibrate-power min**命令设置的最小发送功率。该命令主要用来防止调整后的AP功率值过小。

【举例】

\# 配置AP的最小发送功率为10。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 rrm

Sysname-wlan-ap-ap1-radio-1-rrm calibrate-power min 10

**WLAN RRM \-- WLAN RRM配置命令 \-- calibrate-power self-decisive**

------------------------------------------------------------------------

**[calibrate-power self-decisive**]命令用来开启定时触发自动功率调整。

**[undo calibrate-power self-decisive**]命令用来恢复缺省情况。

【命令】

**[calibrate-power self-decisive**]

**[undo calibrate-power self-decisive**]

【缺省情况】

定时触发自动功率调整处于关闭状态。

【视图】

RRM视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 配置定时触发自动功率调整。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 rrm

Sysname-wlan-ap-ap1-radio-1-rrm calibrate-power self-decisive

**WLAN RRM \-- WLAN RRM配置命令 \-- calibrate-power threshold**

------------------------------------------------------------------------

**[calibrate-power threshold**]命令用来配置功率调整门限值。

**[undo calibrate-power threshold**]命令用来恢复缺省情况。

【命令】

**[calibrate-power threshold ***value*]

**[undo calibrate-power threshold**]

【缺省情况】

功率调整门限值为-65dBm。

【视图】

RRM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：功率调整门限值，取值范围为50～90，代表功率范围为-90～-50dBm。

【举例】

\# 配置功率调整门限值为-70dBm。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 rrm

Sysname-wlan-ap-ap1-radio-1-rrm calibrate-power threshold 70

**WLAN RRM \-- WLAN RRM配置命令 \-- channel-capability mode**

------------------------------------------------------------------------

**[channel**]**-capability mode**命令用于配置对客户端信道能力集的检查模式。

**[undo channel-capability mode**]命令用于恢复缺省情况。

【命令】

**[channel-capability mode **]**[none **[\| ]**partial** }

**[undo channel-capability mode**]

【缺省情况】]

不检查客户端信道能力集。

【视图】

Radio视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：完全匹配模式。只有客户端的信道能力集与设备的信道能力集全部匹配，才允许客户端上线，否则，不允许客户端上线。

**[none**]：不检查模式，即不检查客户端的信道能力集。

**[partial**]：部分匹配模式。客户端的信道能力集与设备的信道能力集只要有一个匹配，则允许客户端上线，否则，不允许客户端上线。

【使用指导】

只有在射频工作在5GHz模式下并且开启频谱管理功能，信道能力集检查功能才会生效。

【举例】

\# 配置对客户端信道能力集的检查模式为完全匹配模式。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 spectrum-management enable

Sysname-wlan-ap-ap1-radio-1 channel-capability mode all

【相关命令】

·**spectrum-management**

**WLAN RRM \-- WLAN RRM配置命令 \-- channel-switch mode**

------------------------------------------------------------------------

**[channel-switch**]** mode**命令用于配置信道切换模式。

**[undo channel-switch mode**]命令用于恢复缺省情况。

【命令】

**[channel-switch mode **]**[suspend **}

**[undo channel-switch mode**]

【缺省情况】]

已上线的客户端停止发送帧。

【视图】

Radio视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[continuous**]：信道发生切换期间，已上线的客户端可以继续发送帧。

**[suspend**]：信道发生切换期间，已上线的客户端停止发送帧，直到信道切换完成。

【使用指导】

只有在射频为5GHz模式下并且开启频谱管理功能，信道切换模式才会生效。

【举例】

\# 配置信道发生切换期间，已上线的客户端可以继续发送帧。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 spectrum-management enable

Sysname-wlan-ap-ap1-radio-1 channel-switch mode continuous

【相关命令】

·**spectrum-management**

**WLAN RRM \-- WLAN RRM配置命令 \-- crc-error-threshold**

------------------------------------------------------------------------

**[crc-error-threshold**]命令用来配置CRC错误门限值。

**[undo crc-error-threshold**]命令用来恢复缺省情况。

【命令】

**[crc-error-threshold ***percent*]

**[undo crc-error-threshold**]

【缺省情况】

CRC错误门限值为20。

【视图】

RRM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[percent*]：CRC错误门限值，以百分比表示，取值范围为10～100。

【举例】

\# 配置CRC错误门限值为50。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 rrm

Sysname-wlan-ap-ap1-radio-1-rrm crc-error-threshold 50

**WLAN RRM \-- WLAN RRM配置命令 \-- interference-threshold**

------------------------------------------------------------------------

**[interference-threshold**]命令用来配置信道干扰门限值。

**[undo interference-threshold**]命令用来恢复缺省情况。

【命令】

**[interference-threshold ***percent*]

**[undo interference-threshold**]

【缺省情况】

信道干扰门限值为50。

【视图】

RRM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[percent*]：信道干扰门限，以百分比表示，取值范围为40～100。

【举例】

\# 配置信道干扰门限值为60。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 rrm

Sysname-wlan-ap-ap1-radio-1-rrm interference-threshold 60

**WLAN RRM \-- WLAN RRM配置命令 \-- power-capability mode**

------------------------------------------------------------------------

**[power-capability mode**]命令用于配置对客户端功率能力集的检查模式。

**[undo power-capability mode**]命令用于恢复缺省情况。

【命令】

**[power-capability mode**] **[none **[\| ]**partial **}

**[undo power-capability mode**]

【缺省情况】]

不检查客户端功率能力集。

【视图】

Radio视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：完全匹配模式。只有客户端的功率能力集与设备的功率能力集全部匹配，才允许客户端上线，否则，不允许客户端上线。

**[none**]：不检查模式，即不检查客户端的功率能力集。

**[partial**]：部分匹配模式。客户端的功率能力集与设备的功率能力集只要有一个匹配，则允许客户端上线，否则，不允许客户端上线。

【使用指导】

只有在射频为5GHz模式下并且开启频谱管理功能，功率能力集检查功能才会生效。

【举例】

\# 配置对客户端功率能力集的检查模式为完全匹配模式。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 spectrum-management enable

Sysname-wlan-ap-ap1-radio-1 power-capability mode all

【相关命令】

·**spectrum-management**

**WLAN RRM \-- WLAN RRM配置命令 \-- power-constraint mode**

------------------------------------------------------------------------

**[power-constraint mode**]命令用于配置功率限制模式。

**[undo power-constraint mode**]命令用于恢复缺省情况。

【命令】

**[power-constraint mode **]{ **auto** [ **anpi-interval** *anpi-interval-value*  \| **manual** *power-constraint* }]

**[undo power-constraint mode**]

【缺省情况】

功率限制模式为自动模式。

【视图】

Radio视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[auto**]：配置限制功率模式为自动模式。

**[anpi-interval **]*anpi-interval-value*：指定ANPI差值，取值范围为0～30，单位为dBm。缺省值为10dBm。

**[manual**]*power-constraint*：配置手动限制功率数值，取值范围为0～30，单位为dBm。

【使用指导】

·当配置为手动模式时，设备会通知802.11a客户端将其发送功率降低*power-constraint* dBm。

·当配置为自动模式时，设备会根据接收信道功率参数、平均噪底功率、ANPI差值计算出限制功率值。计算公式：*power-constraint* = 接收信道功率参数RCPI-（平均噪底功率ANPI+*[anpi-interval-value*]）。

·只有在射频为5GHz模式下并且开启频谱管理功能，功率限制功能才会生效。

【举例】

\# 配置5GHz模式下客户端的功率限制模式为手动模式，功率限制值为5dBm。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 spectrum-management enable

Sysname-wlan-ap-ap1-radio-1 power-constraint mode manual 5

\# 配置5GHz模式下客户端的功率限制模式为自动模式，ANPI差值为15dBm。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 spectrum-management enable

Sysname-wlan-ap-ap1-radio-1 power-constraint mode auto apni-interval 15

Sysname-WLAN-Radio1/0/1 power-constraint mode auto apni-interval 15

【项目命令】

·**spectrum-management**

**WLAN RRM \-- WLAN RRM配置命令 \-- rrm**

------------------------------------------------------------------------

**[rrm**]命令用来进入RRM（Radio Resource Management，射频资源管理）视图。

【命令】

**[rrm**]

【视图】

Radio视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 进入RRM视图。

\<Sysname\> system-view

Sysname wlan ap ap1 WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 rrm

**WLAN RRM \-- WLAN RRM配置命令 \-- tolerance-level**

------------------------------------------------------------------------

**[tolerance-level**]命令用来配置容限系数。

**[undo tolerance-level**]命令用来恢复缺省情况。

【命令】

**[tolerance-level ***percent*]

**[undo tolerance-level**]

【缺省情况】

容限系数为20。

【视图】

RRM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[percent*]：容限系数，以百分比表示，取值范围为15～45。

【使用指导】

当CRC错误门限或干扰门限超过门限值时，AC会开始计算信道质量，但只有在新的信道和旧信道的信道质量差超过容限系数时，新的信道才会被应用。

【举例】

\# 配置容限系数为25。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 rrm

Sysname-wlan-ap-ap1-radio-1-rrm tolerance-level 25

**WLAN RRM \-- WLAN RRM配置命令 \-- spectrum-management**

------------------------------------------------------------------------

**[spectrum**]**-management enable**命令用于开启频谱管理功能。

**[spectrum**]**-management disable**命令用于开启频谱管理功能。

**[undo spectrum-management**]命令用于恢复缺省情况。

【命令】

**[spectrum-management ** { **enable** \| **disable** }]

**[undo spectrum-management**]

【缺省情况】

频谱管理功能处于关闭状态。

【视图】

Radio视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 开启频谱管理功能。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 spectrum-management enable

**WLAN RRM \-- WLAN RRM配置命令 \-- wlan calibrate-channel pronto ap all**

------------------------------------------------------------------------

**[wlan calibrate-channel pronto ap all**]命令用来配置手动触发所有AP进行自动信道调整。

【命令】

**[wlan calibrate-channel pronto ap all**]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

执行**wlan calibrate-channel pronto ap all**命令可能会占用较多系统资源，请谨慎使用。

【举例】

\# 配置手动触发所有AP进行自动信道调整。

\<Sysname\> system-view

Sysname wlan calibrate-channel pronto ap all

**WLAN RRM \-- WLAN RRM配置命令 \-- wlan calibrate-power pronto ap all**

------------------------------------------------------------------------

**[wlan calibrate-power pronto ap all**]命令用来配置手动触发所有AP进行自动功率调整。

【命令】

**[wlan calibrate-power pronto ap all**]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

执行**wlan calibrate-power pronto ap all**命令可能会占用较多系统资源，请谨慎使用。

【举例】

\# 配置手动触发所有AP进行自动功率调整。

\<Sysname\> system-view

Sysname wlan calibrate-power pronto ap all

**WLAN RRM \-- WLAN RRM配置命令 \-- wlan rrm-calibration-interval**

------------------------------------------------------------------------

**[wlan rrm-calibration-interval**]命令用来配置信道和功率调整的校准间隔。

**[undo wlan rrm-calibration-interval**]命令用来恢复缺省情况。

【命令】

**[wlan rrm-calibration-interval ***minutes*]

**[undo wlan rrm-calibration-interval**]

【缺省情况】

信道和功率调整的校准间隔是8分钟。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[minutes*]：信道和功率调整的校准间隔，取值范围为3～180，单位为分钟。

【举例】

\# 配置校准间隔为10分钟。

\<Sysname\> system-view

Sysname wlan rrm-calibration-interval 10

