
**NQA \-- NQA客户端配置命令 \-- advantage-factor**

------------------------------------------------------------------------

**[advantage-factor**]命令用来配置用于计算MOS值和ICPIF值的补偿因子。

**[undo advantage-factor**]命令用来恢复缺省情况。

【命令】

**[advantage-factor ***factor *]

**[undo advantage-factor**]

【缺省情况】

补偿因子取值为0。

【视图】

Voice测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[factor*]：用于计算MOS值和ICPIF值的补偿因子，取值范围为0～20。

【使用指导】

用户对语音质量的评价具有一定的主观性，不同用户对语音质量的容忍程度不同，因此，衡量语音质量时，需要考虑用户的主观因素。对语音质量容忍程度较强的用户，可以通过**advantage-factor**命令配置补偿因子，在计算ICPIF值时将减去该补偿因子，修正ICPIF和MOS值，以便在比较语音质量时综合考虑客观和主观因素。

【举例】

\# 配置语音测试的补偿因子为10。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type voice

Sysname-nqa-admin-test-voice advantage-factor 10

**NQA \-- NQA客户端配置命令 \-- codec-type**

------------------------------------------------------------------------

**[codec-type**]命令用来配置语音测试的编码格式。

**[undo codec-type**]命令用来恢复缺省情况。

【命令】

**[codec-type**[ { **g711a** \| **g711u** \| **g729a** }]]

**[undo codec-type**]

【缺省情况】

语音编码格式为G.711 A律。

【视图】

Voice测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[g711a**]：G.711 A律语音编码格式。

**[g711u**]：G.711 µ律语音编码格式。

**[g729a**]：G.729 A律语音编码格式。

【举例】

\# 配置Voice测试的语音编码格式为G.729 A律。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type voice

Sysname-nqa-admin-test-voice codec-type g729a

**NQA \-- NQA客户端配置命令 \-- data-fill**

------------------------------------------------------------------------

**[data-fill**]命令用来配置发送的探测报文的填充字符串。

**[undo data-fill**]命令用来恢复缺省情况。

【命令】

**[data-fill** *string*]

**[undo** **data-fill**]

【缺省情况】

探测报文的填充内容为十六进制数值00010203040506070809。

【视图】

ICMP-echo/Path-jitter/UDP-echo/UDP-jitter/Voice测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[string*]：探测报文的填充内容，为1～200个字符的字符串，区分大小写。

【使用指导】

·如果探测报文的数据段长度比配置的填充数据长度小，系统在报文封装时以报文的数据段长度为界截取该字符串的前一部分；

·如果探测报文的数据段长度比配置的填充数据长度大，系统在报文封装时用该字符串进行循环填充，直到填满。

例如，配置填充数据为"abcd"，当探测报文数据段长度为3字节时，则取"abc"作为填充数据；当探测报文大小为6字节时，则使用"adcdab"作为填充数据。

·在ICMP-echo测试中，配置的字符串用来填充ICMP Echo消息的数据字段。

·在UDP-echo测试中，由于UDP报文数据字段的前5个字节具有特定用途，所以只用所配置的字符串填充报文中剩余的字节。

·在UDP-jitter测试中，UDP报文数据字段的前68个字节具有特定用途，所以只用所配置的字符串填充报文中剩余的字节。

·在Voice测试中，UDP报文数据字段的前16个字节具有特定用途，所以只用所配置的字符串填充报文中剩余的字节。

·在Path-jitter测试中，由于ICMP探测阶段ICMP报文数据字段的前4个字节具有特定用途，所以只用所配置的字符串填充ICMP报文中剩余的字节。

【举例】

\# 配置ICMP-echo探测报文的填充字符串为abcd。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type icmp-echo

Sysname-nqa-admin-test-icmp-echo data-fill abcd

\# 在TCP类型的NQA模板视图下，配置探测报文的填充字符串为abcd。

\<Sysname\> system-view

Sysname nqa template tcp tcptplt

Sysname-nqatplt-tcp-tcptplt data-fill abcd

**NQA \-- NQA客户端配置命令 \-- data-size**

------------------------------------------------------------------------

**[data-size**]命令用来配置发送的探测报文中的填充内容的大小。

**[undo data-size**]命令用来恢复缺省情况。

【命令】

**[data-size** *size*]

**[undo** **data-size**]

【缺省情况】

缺省情况如 表1-1(?-1912717852#_Ref337469088)所示。

表1-1 探测报文中的填充内容大小的缺省值

测试类型

编码类型

缺省值（字节）

ICMP-echo

-

100

UDP-echo

-

100

UDP-jitter

-

100

UDP-tracert

-

100

Path-jitter

-

100

Voice

G.711 A律

172

Voice

G.711 µ律

172

Voice

G.729 A律

32

【视图】

ICMP-echo/Path-jitter/UDP-echo/UDP-jitter/UDP-tracert/Voice测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size*]：探测报文中的填充内容的大小，单位为字节，ICMP-echo、UDP-echo和UDP-tracert测试类型取值范围为20～8100，UDP-jitter和Path-jitter测试类型取值范围为68～8100，Voice测试类型取值范围为16～1500。

【使用指导】

·对于ICMP-echo和Path-jitter测试，探测报文中填充内容的大小为ICMP Echo消息中数据字段的长度。

·对于UDP-echo、UDP-jitter、UDP-tracert和Voice测试，探测报文中填充内容的大小为UDP报文中数据字段的长度。

【举例】

\# 配置发送的ICMP-echo探测报文中的填充内容的大小为80字节。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type icmp-echo

Sysname-nqa-admin-test-icmp-echo data-size 80

\# 在ICMP类型的NQA模板视图下，配置发送的ICMP-echo探测报文中的填充内容的大小为80字节。

\<Sysname\> system-view

Sysname nqa template icmp icmptplt

Sysname-nqatplt-icmp-icmptplt data-size 80

**NQA \-- NQA客户端配置命令 \-- description (any NQA test type view)**

------------------------------------------------------------------------

**[description**]命令用来对测试组进行简要描述，通常用于描述一个测试组的测试类型或测试目的。**undo description**命令用来删除已配置的描述信息。

【命令】

**[description ***text*]

**[undo description**]

【缺省情况】

未配置描述字符串。

【视图】

任意测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：测试组的描述，为1～200个字符的字符串，区分大小写。

【举例】

\# 配置测试组的描述字符串为icmp-probe。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type icmp-echo

Sysname-nqa-admin-test-icmp-echo description icmp-probe

\# 在ICMP类型的NQA模板视图下，配置描述字符串为icmp-probe。

\<Sysname\> system-view

Sysname nqa template icmp icmptplt

Sysname-nqatplt-icmp-icmptplt description icmp-probe

**NQA \-- NQA客户端配置命令 \-- destination ip**

------------------------------------------------------------------------

**[destination ip**]命令用来配置测试操作中探测报文的目的IP地址。

**[undo destination ip**]命令用来删除已配置的探测报文的目的IP地址。

【命令】

**[destination** **ip** *ip-address*]

**[undo** **destination** **ip**]

【缺省情况】

未配置测试操作中探测报文的目的IP地址。

【视图】

DHCP/DLSw/DNS/ICMP-echo/Path-jitter/SNMP/TCP/UDP-echo/UDP-jitter/UDP-tracert/Voice测试类型视图

DNS/ICMP/RADIUS/TCP/UDP类型的NQA模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：测试操作中探测报文的目的IP地址。

【举例】

\# 配置ICMP-echo测试操作中探测报文的目的IP地址为10.1.1.1。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type icmp-echo

Sysname-nqa-admin-test-icmp-echo destination ip 10.1.1.1

\# 在ICMP类型的NQA模板视图下，配置测试操作中探测报文的目的IP地址为10.1.1.1。

\<Sysname\> system-view

Sysname nqa template icmp icmptplt

Sysname-nqatplt-icmp-icmptplt destination ip 10.1.1.1

**NQA \-- NQA客户端配置命令 \-- destination ipv6**

------------------------------------------------------------------------

**[destination ipv6**]命令用来配置测试操作中探测报文的目的IPv6地址。

**[undo destination ipv6**]命令用来删除已配置的探测报文的目的IPv6地址。

【命令】

**[destination** **ipv6** *ipv6-address*]

**[undo** **destination** **ipv6**]

【缺省情况】

未配置测试操作中探测报文的目的IPv6地址。

【视图】

DNS/ICMP/RADIUS/TCP/UDP类型的NQA模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：测试操作中探测报文的目的IPv6地址，不支持IPv6链路本地地址。

【举例】

\# 在ICMP类型的NQA模板视图下，配置测试操作中探测报文的目的IPv6地址为1::1。

\<Sysname\> system-view

Sysname nqa template icmp icmptplt

Sysname-nqatplt-icmp-icmptplt destination ipv6 1::1

**NQA \-- NQA客户端配置命令 \-- destination port**

------------------------------------------------------------------------

**[destination port**]命令用来配置测试操作的目的端口号。

**[undo destination port**]命令用来删除已配置的目的端口号。

【命令】

**[destination**] **port** *port-number*

**[undo**] **destination** **port**

【缺省情况】

对于UDP-tracert测试，目的端口号缺省为33434；对于其他类型测试，未配置测试操作的目的端口号。

对于各类型的NQA模板，各种操作类型的端口号缺省为DNS（53）、HTTP（80）、FTP（21）、RADIUS（1812）；对于其他模板类型，未配置测试操作的目的端口号。

【视图】

TCP/UDP-echo/UDP-jitter/UDP-tracert/Voice测试类型视图

DNS/RADIUS/TCP/UDP类型的NQA模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-number*]：测试操作的目的端口号，取值范围为1～65535。

【举例】

\# 配置测试操作的目的端口号为9000。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type udp-echo

Sysname-nqa-admin-test-udp-echo destination port 9000

\# 在TCP类型的NQA模板视图下，配置测试操作的目的端口号为9000。

\<Sysname\> system-view

Sysname nqa template tcp tcptplt

Sysname-nqatplt-tcp-tcptplt destination port 9000

**NQA \-- NQA客户端配置命令 \-- display nqa history**

------------------------------------------------------------------------

**[display nqa history**]命令用来显示NQA测试组的历史记录。

【命令】

**[display nqa history** *admin-name* *operation-tag* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[admin-name operation-tag*]：显示指定测试组的历史记录。如果不指定这两个参数，将显示所有测试组的历史记录。其中，*admin-name*为创建NQA测试组的管理员名字，为1～32个字符的字符串，字符串中不能包括"-"，不区分大小写；*operation-tag*为测试操作的标签，为1～32个字符的字符串，字符串中不能包括"-"，不区分大小写。

【使用指导】

**[display nqa history**]命令的显示信息无法反映UDP-jitter，Path-jitter和Voice测试的结果，如果想了解UDP-jitter，Path-jitter和Voice测试的结果，建议通过**display nqa result**命令查看最近一次NQA测试的结果，或通过**display nqa statistics**命令查看NQA测试的统计信息。

【举例】

\# 显示管理员名字为administrator，测试类型标签为tracert的UDP-tracert测试项的历史记录。

\<Sysname\> display nqa history administrator tracert

NQA entry (admin administrator, tag tracert) history records:

Index      TTL  Response  Hop IP          Status          Time

1          2    328       4.1.1.1         Succeeded       2013-09-09 14:46:06.2 

1          2    328       4.1.1.1         Succeeded       2013-09-09 14:46:05.2 

1          2    328       4.1.1.1         Succeeded       2013-09-09 14:46:04.2 

1          1    328       3.1.1.2         Succeeded       2013-09-09 14:46:03.2 

1          1    328       3.1.1.1         Succeeded       2013-09-09 14:46:02.2

1          1    328       3.1.1.1         Succeeded       2013-09-09 14:46:01.2  

\# 查看管理员名字为administrator，测试操作标签为test的NQA测试组的历史记录。

\<Sysname\> display nqa history administrator test

NQA entry (admin administrator, tag test) history records:

  Index      Response     Status           Time

  10         329          Succeeded        2011-04-29 20:54:26.5

  9          344          Succeeded        2011-04-29 20:54:26.2

  8          328          Succeeded        2011-04-29 20:54:25.8

  7          328          Succeeded        2011-04-29 20:54:25.5

  6          328          Succeeded        2011-04-29 20:54:25.1

  5          328          Succeeded        2011-04-29 20:54:24.8

  4          328          Succeeded        2011-04-29 20:54:24.5

  3          328          Succeeded        2011-04-29 20:54:24.1

  2          328          Succeeded        2011-04-29 20:54:23.8

  1          328          Succeeded        2011-04-29 20:54:23.4

表1-2 display nqa history命令显示信息描述表

字段

描述

Index

历史记录的编号，一次UDP-tracert测试中的所有记录此编号一致

TTL

本次探测的TTL值

Response

测试成功时，为测试报文的往返时延；如果测试超时，则为超时时间；不能完成测试时，则为0。单位为毫秒

Hop IP

回复应答的节点IP地址

Status

测试结果的状态值，具体如下：

·Succeeded：测试成功，接收到响应报文

·Unknown error：未知错误

·Internal error：内部错误

·Timeout：请求超时

Time

测试完成时间

**NQA \-- NQA客户端配置命令 \-- display nqa reaction counters**

------------------------------------------------------------------------

**[display nqa reaction counters**]命令用来显示阈值告警组的当前监测结果。

【命令】

**[display nqa reaction counters** \*[admin-name* *operation-tag* [ *item-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[admin-name operation-tag*]：显示指定测试组中阈值告警组的当前监测结果。如果不指定这两个参数，将显示所有测试组中所有阈值告警组的当前监测结果。其中，*admin-name*为创建NQA测试组的管理员名字，为1～32个字符的字符串，字符串中不能包括"-"，不区分大小写；*operation-tag*为测试操作的标签，为1～32个字符的字符串，字符串中不能包括"-"，不区分大小写。

*[item-number*]：显示指定阈值告警组的当前监测结果。如果不指定该参数，将显示所有阈值告警组的当前监测结果。*item-number*为阈值告警组的编号，取值范围为1～10。

【使用指导】

·如果NQA阈值告警组的阈值类型为平均值，或监测对象为Voice测试的ICPIF或MOS值，则显示的监测结果为无效值。

·测试结束后，不会清除监测结果，即测试组启动后，监测结果会不断累加。

【举例】

\# 显示ICMP-echo测试组admin test的所有阈值告警组的当前监测结果。

\<Sysname\> display nqa reaction counters admin test

NQA entry (admin admin, tag test) reaction counters:

  Index  Checked Element  Threshold Type  Checked Num  Over-threshold Num

1      probe-duration   accumulate      12           4

  2      probe-duration   average         -            -

3      probe-duration   consecutive     160          56

  4      probe-fail       accumulate      12           0

  5      probe-fail       consecutive     162          2

表1-3 display nqa reaction counters命令显示信息描述

字段

描述

Index

阈值告警组的编号

Checked Element

监测的对象

Threshold Type

阈值类型

Checked Num

已监测的样本个数

Over-threshold Num

超出阈值的样本个数

表1-4 display nqa reaction counters命令显示字段取值描述

监测对象

阈值类型

监测的样本范围

Checked Num取值

Over-threshold Num取值

probe-duration

accumulate

启动NQA测试组后进行的探测

启动NQA测试组后已完成的探测次数

启动NQA测试组后探测持续时间不在阈值范围内的探测次数

average

-

-

-

consecutive

启动NQA测试组后进行的探测

启动NQA测试组后已完成的探测次数

启动NQA测试组后探测持续时间不在阈值范围内的探测次数

probe-fail

accumulate

启动NQA测试组后进行的探测

启动NQA测试组后已完成的探测次数

启动NQA测试组后失败的探测次数

consecutive

启动NQA测试组后进行的探测

启动NQA测试组后已完成的探测次数

启动NQA测试组后失败的探测次数

RTT

accumulate

启动NQA测试组后发送的报文

启动NQA测试组后已发送的报文个数

启动NQA测试组后往返时间不在阈值范围内的报文个数

average

-

-

-

jitter-DS/jitter-SD

accumulate

启动NQA测试组后发送的报文

启动NQA测试组后已发送的报文个数

启动NQA测试组后单向时延抖动不在阈值范围内的报文个数

average

-

-

-

OWD-DS/OWD-SD

-

启动NQA测试组后发送的报文

启动NQA测试组后已发送的报文个数

启动NQA测试组后单向时延不在阈值范围内的报文个数

packet-loss

accumulate

启动NQA测试组后发送的报文

启动NQA测试组后已发送的报文个数

启动NQA测试组后的丢包数

ICPIF

-

-

-

-

MOS

-

-

-

-

**NQA \-- NQA客户端配置命令 \-- display nqa result**

------------------------------------------------------------------------

**[display nqa result**]命令用来显示最近一次NQA测试的当前结果。

【命令】

**[display nqa result ** *admin-name* *operation-tag* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[admin-name operation-tag*]：显示指定测试组的最近一次测试的当前结果。如果不指定这两个参数，将显示所有测试组的最近一次测试的结果。其中，*admin-name*为创建NQA测试组的管理员名字，为1～32个字符的字符串，字符串中不能包括"-"，不区分大小写；*operation-tag*为测试操作的标签，为1～32个字符的字符串，字符串中不能包括"-"，不区分大小写。

【举例】

\# 显示TCP测试的最近一次测试的当前结果。

\<Sysname\> display nqa result admin test

NQA entry (admin admin, tag test) test results:

    Send operation times: 1              Receive response times: 1

    Min/Max/Average round trip time: 35/35/35

    Square-Sum of round trip time: 1225

    Last succeeded probe time: 2011-05-29 10:50:33.2

  Extended results:

    Packet loss ratio: 0%

    Failures due to timeout: 0

    Failures due to disconnect: 0

    Failures due to no connection: 0

    Failures due to internal error: 0

    Failures due to other errors: 0

\# 显示UDP-jitter测试的最近一次测试的当前结果。

\<Sysname\> display nqa result admin test

NQA entry (admin admin, tag test) test results:

    Send operation times: 10             Receive response times: 10

    Min/Max/Average round trip time: 15/46/26

    Square-Sum of round trip time: 8103

    Last packet received time: 2011-05-29 10:56:38.7

  Extended results:

    Packet loss ratio: 0%

    Failures due to timeout: 0

    Failures due to internal error: 0

    Failures due to other errors: 0

    Packets out of sequence: 0

    Packets arrived late: 0

  UDP-jitter results:

RTT number: 10

    Min positive SD: 8                     Min positive DS: 8

Max positive SD: 18                    Max positive DS: 8

    Positive SD number: 5                  Positive DS number: 2

    Positive SD sum: 75                    Positive DS sum: 32

    Positive SD average: 15                Positive DS average: 16

    Positive SD square-sum: 1189           Positive DS square-sum: 640

Min negative SD: 8                     Min negative DS: 1

    Max negative SD: 24                    Max negative DS: 30

    Negative SD number: 4                  Negative DS number: 7

    Negative SD sum: 56                    Negative DS sum: 99

    Negative SD average: 14                Negative DS average: 14

Negative SD square-sum: 946            Negative DS square-sum: 1495

  One way results:

    Max SD delay: 22                       Max DS delay: 23

Min SD delay: 7                        Min DS delay: 7

Number of SD delay: 10                 Number of DS delay: 10

    Sum of SD delay: 125                   Sum of DS delay: 132

    Square-Sum of SD delay: 1805           Square-Sum of DS delay: 1988

    SD lost packets: 0                     DS lost packets: 0

    Lost packets for unknown reason: 0

\# 显示Voice测试最近一次测试的当前结果。

\<Sysname\> display nqa result admin test

NQA entry (admin admin, tag test) test results:

    Send operation times: 1000           Receive response times: 0

    Min/Max/Average round trip time: 0/0/0

    Square-Sum of round trip time: 0

    Last packet received time: 0-00-00 00:00:00.0

  Extended results:

    Packet loss ratio: 100%

    Failures due to timeout: 1000

    Failures due to internal error: 0

    Failures due to other errors: 0

    Packets out of sequence: 0

    Packets arrived late: 0

  Voice results:

RTT number: 0

    Min positive SD: 0                     Min positive DS: 0

Max positive SD: 0                     Max positive DS: 0

    Positive SD number: 0                  Positive DS number: 0

    Positive SD sum: 0                     Positive DS sum: 0

    Positive SD average: 0                 Positive DS average: 0

    Positive SD square-sum: 0              Positive DS square-sum: 0

Min negative SD: 0                     Min negative DS: 0

    Max negative SD: 0                     Max negative DS: 0

    Negative SD number: 0                  Negative DS number: 0

    Negative SD sum: 0                     Negative DS sum: 0

    Negative SD average: 0                 Negative DS average: 0

Negative SD square-sum: 0              Negative DS square-sum: 0

  One way results:

    Max SD delay: 0                        Max DS delay: 0

Min SD delay: 0                        Min DS delay: 0

Number of SD delay: 0                  Number of DS delay: 0

    Sum of SD delay: 0                     Sum of DS delay: 0

    Square-Sum of SD delay: 0              Square-Sum of DS delay: 0

    SD lost packets: 0                     DS lost packets: 0

    Lost packets for unknown reason: 1000

  Voice scores:

    MOS value: 0.99                        ICPIF value: 87

\# 显示Path-jitter测试正在进行中。

\<Sysname\> display nqa result admin test

Data collecting in progress\...

\# 显示Path-jitter测试没有生成结果。

\<Sysname\> display nqa result admin test

  Path jitter result is not available.

\# 显示Path-jitter测试的最近一次测试的当前结果。

\<Sysname\> display nqa result admin test

NQA entry (admin admin, tag test) test results:

  Hop IP 192.168.40.210

    Basic Results:

      Send operation times: 10

      Receive response times: 10

      Min/Max/Average round trip time: 1/1/1

      Square-Sum of round trip time: 10

    Extended Results:

      Packet loss ratio: 0%

      Failures due to timeout: 0

      Failures due to internal error: 0

      Failures due to other errors: 0

      Packets out of sequence: 0

      Packets arrived late: 0

    Path-Jitter Results:

      Jitter number: 9

        Min/Max/Average jitter: 0/0/0

      Positive jitter number: 0

        Min/Max/Average positive jitter: 0/0/0

        Sum/Square-Sum positive jitter: 0/0

      Negative jitter number: 0

        Min/Max/Average negative jitter: 0/0/0

        Sum/Square-Sum negative jitter: 0/0

  Hop IP 192.168.50.209

    Basic Results:

      Send operation times: 10

      Receive response times: 10

      Min/Max/Average round trip time: 1/1/1

      Square-Sum of round trip time: 10

    Extended Results:

      Packet loss ratio: 0%

      Failures due to timeout: 0

      Failures due to internal error: 0

      Failures due to other errors: 0

      Packets out of sequence: 0

      Packets arrived late: 0

    Path-Jitter Results:

      Jitter number: 9

        Min/Max/Average jitter: 0/0/0

      Positive jitter number: 0

        Min/Max/Average positive jitter: 0/0/0

        Sum/Square-Sum positive jitter: 0/0

      Negative jitter number: 0

        Min/Max/Average negative jitter: 0/0/0

        Sum/Square-Sum negative jitter: 0/0

\# 显示UDP-tracert测试的最近一次测试的当前结果。

\<Sysname\> display nqa result admin test

NQA entry (admin admin, tag test) test results:

    Send operation times: 6              Receive response times: 6

    Min/Max/Average round trip time: 35/35/35

    Square-Sum of round trip time: 1225

    Last succeeded probe time: 2013-09-09 14:23:24.5

  Extended results:

    Packet loss ratio: 0%

    Failures due to timeout: 0

    Failures due to internal error: 0

    Failures due to other errors: 0

  UDP-tracert results: 

    TTL    Hop IP             Time

    1      3.1.1.1            2013-09-09 14:23:24.5

    2      4.1.1.1            2013-09-09 14:23:24.5

表1-5 display nqa result命令显示信息描述

字段

描述

Send operation times

发送的探测报文数

Receive response times

收到的响应报文数

Min/Max/Average round trip time

最小/最大/平均往返时间，单位为毫秒

Square-Sum of round trip time

往返时间平方和

Last succeeded probe time

一次测试中最后一次成功探测的完成时间，如果一次测试中的探测均失败，则该时间显示为全0，UDP-jitter、Path-jitter和Voice测试中无此信息

Last packet received time

一次探测中最后一次成功收到正确响应报文的时间，如果一次探测中没有收到过正确的响应报文，则该时间显示为全0，只在UDP-jitter和Voice测试中存在此信息

Packet loss ratio

平均丢包率

Failures due to timeout

测试过程中超时的次数

Failures due to disconnect

对方强制断开连接的次数

Failures due to no connection

和对方建立连接失败的次数

Failures due to internal error

因内部错误失败的次数

Failures due to other errors

因其它错误失败的次数

Packets out of sequence

报文失序的次数

Packets arrived late

探测超时后，收到的响应报文个数

UDP-jitter results

UDP-jitter测试的结果，只在UDP-jitter测试中存在此信息

Voice results

Voice测试的结果，只在Voice测试中存在此信息

RTT number

收到的响应报文数

Min positive SD

源到目的方向正抖动时延的最小值

Min positive DS

目的到源方向正抖动时延的最小值

Max positive SD

源到目的方向正抖动时延的最大值

Max positive DS

目的到源方向正抖动时延的最大值

Positive SD number

源到目的方向正抖动时延的数目

Positive DS number

目的到源方向正抖动时延的数目

Positive SD sum

源到目的方向正抖动时延之和

Positive DS sum

目的到源方向正抖动时延之和

Positive SD average

源到目的方向正抖动时延的平均值

Positive DS average

目的到源方向正抖动时延的平均值

Positive SD square-sum

源到目的方向正抖动时延的平方和

Positive DS square-sum

目的到源方向正抖动时延的平方和

Min negative SD

源到目的方向负抖动时延的绝对值的最小值

Min negative DS

目的到源方向负抖动时延的绝对值的最小值

Max negative SD

源到目的方向负抖动时延的绝对值的最大值

Max negative DS

目的到源方向负抖动时延的绝对值的最大值

Negative SD number

源到目的方向负抖动时延的数目

Negative DS number

目的到源方向负抖动时延的数目

Negative SD sum

源到目的方向负抖动时延的绝对值之和

Negative DS sum

目的到源方向负抖动时延的绝对值之和

Negative SD average

源到目的方向负抖动时延的绝对值的平均值

Negative DS average

目的到源方向负抖动时延的绝对值的平均值

Negative SD square-sum

源到目的方向负抖动时延的平方和

Negative DS square-sum

目的到源方向负抖动时延的平方和

One way results

单向延迟测试结果，只有UDP-Jitter和Voice类型测试有单向延迟测试结果

Max SD delay

源到目的的最大时延

Max DS delay

目的到源的最大时延

Min SD delay

源到目的的最小时延

Min DS delay

目的到源的最小时延

Number of SD delay

源到目的计算的时延数

Number of DS delay

目的到源计算的时延数

Sum of SD delay

源到目的的时延和

Sum of DS delay

目的到源的时延和

Square-Sum of SD delay

源到目的的时延的平方和

Square-Sum of DS delay

目的到源的时延的平方和

SD lost packets

源到目的方向丢失的报文个数

DS lost packets

目的到源方向丢失的报文个数

Lost packets for unknown reason

不能确定原因丢失的报文个数

Voice scores

语音参数，只在Voice类型测试有此信息

MOS value

为语音计算的MOS值

ICPIF value

为语音计算的ICPIF值

Hop IP

本跳IP地址，只在Path-jitter测试中存在此信息

Path-jitter results

Path-jitter测试的结果，只在Path-jitter测试中存在此信息

Jitter number

计算抖动次数，只在Path-jitter测试中存在此信息

Min/Max/Average jitter

最小/最大/平均抖动时延，单位为毫秒，只在Path-jitter测试中存在此信息

Positive jitter number

正抖动时延的数目，只在Path-jitter测试中存在此信息

Min/Max/Average positive jitter

最小/最大/平均正抖动时延，单位为毫秒，只在Path-jitter测试中存在此信息

Sum/Square-Sum positive jitter

正抖动时延之和/平方和，只在Path-jitter测试中存在此信息

Negative jitter number

负抖动时延的数目，只在Path-jitter测试中存在此信息

Min/Max/Average negative jitter

最小/最大/平均负抖动时延，单位为毫秒，只在Path-jitter测试中存在此信息

Sum/Square-Sum negative jitter

负抖动时延之和/平方和，只在Path-jitter测试中存在此信息

TTL

本次收到的应答报文中的TTL值

Hop IP

回复应答的节点IP地址

Time

收到应答报文的时间

**NQA \-- NQA客户端配置命令 \-- display nqa statistics**

------------------------------------------------------------------------

**[display nqa statistics**]命令用来显示NQA测试的统计信息。

【命令】

**[display nqa statistics** [ *admin-name* *operation-tag* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[admin-name operation-tag*]：显示指定测试组的统计信息。如果不指定这两个参数，将显示所有测试组的统计信息。其中，*admin-name*为创建NQA测试组的管理员名字，为1～32个字符的字符串，字符串中不能包括"-"，不区分大小写；*operation-tag*为测试操作的标签，为1～32个字符的字符串，字符串中不能包括"-"，不区分大小写。

【使用指导】

·测试开始后，如果第一次测试中的所有探测尚未完成，则无法生成统计信息。若此时通过该命令查看统计信息，则显示信息为全0。

·如果配置了阈值告警组，将显示在**statistics interval**命令指定的统计周期内的监测结果。若阈值告警组的阈值类型为平均值，或监测对象为Voice测试的ICPIF或MOS值，则显示的监测结果为无效值。

·UDP-tracert测试类型不支持用该命令显示统计信息。

【举例】

\# 显示TCP测试的统计信息。

\<Sysname\> display nqa statistics admin test

NQA entry (admin admin, tag test) test statistics:

  NO. : 1

    Start time: 2007-01-01 09:30:20.0

    Life time: 2 seconds

    Send operation times: 1              Receive response times: 1

    Min/Max/Average round trip time: 13/13/13

    Square-Sum of round trip time: 169

  Extended results:

    Packet loss ratio: 0%

    Failures due to timeout: 0

    Failures due to disconnect: 0

    Failures due to no connection: 0

    Failures due to internal error: 0

    Failures due to other errors: 0

\# 显示UDP-jitter测试的统计信息。

\<Sysname\> display nqa statistics admin test

NQA entry (admin admin, tag test) test statistics:

  NO. : 1

    Start time: 2007-01-01 09:33:22.3

    Life time: 23 seconds

    Send operation times: 100            Receive response times: 100

    Min/Max/Average round trip time: 1/11/5

    Square-Sum of round trip time: 24360

  Extended results:

    Packet loss ratio: 0%

    Failures due to timeout: 0

    Failures due to internal error: 0

    Failures due to other errors: 0

    Packets out of sequence: 0

    Packets arrived late: 0

  UDP-jitter results:

RTT number: 550

    Min positive SD: 1                     Min positive DS: 1

Max positive SD: 7                     Max positive DS: 1

    Positive SD number: 220                Positive DS number: 97

    Positive SD sum: 283                   Positive DS sum: 287

    Positive SD average: 1                 Positive DS average: 2

    Positive SD square-sum: 709            Positive DS square-sum: 1937

Min negative SD: 2                     Min negative DS: 1

    Max negative SD: 10                    Max negative DS: 1

    Negative SD number: 81                 Negative DS number: 94

    Negative SD sum: 556                   Negative DS sum: 191

    Negative SD average: 6                 Negative DS average: 2

Negative SD square-sum: 4292           Negative DS square-sum: 967

  One way results:

    Max SD delay: 5                        Max DS delay: 5

Min SD delay: 1                        Min DS delay: 1

Number of SD delay: 550                Number of DS delay: 550

    Sum of SD delay: 1475                  Sum of DS delay: 1201

    Square-Sum of SD delay: 5407           Square-Sum of DS delay: 3959

    SD lost packets: 0                     DS lost packets: 0

    Lost packets for unknown reason: 0

  Reaction statistics:

    Index  Checked Element  Threshold Type  Checked Num  Over-threshold Num

    1      jitter-DS        accumulate      90           25

    2      jitter-SD        average         -            -

    3      OWD-DS           -               100          24

    4      OWD-SD           -               100          13

    5      packet-loss      accumulate      0            0

    6      RTT              accumulate      100          52

\# 显示Voice测试的统计信息。

\<Sysname\> display nqa statistics admin test

NQA entry (admin admin, tag test) test statistics:

  NO. : 1

    Start time: 2007-01-01 09:33:45.3

    Life time: 120 seconds

    Send operation times: 10             Receive response times: 10

    Min/Max/Average round trip time: 1/12/7

    Square-Sum of round trip time: 620

  Extended results:

    Packet loss ratio: 0%

    Failures due to timeout: 0

    Failures due to internal error: 0

    Failures due to other errors: 0

    Packets out of sequence: 0

    Packets arrived late: 0

  Voice results:

RTT number: 10

    Min positive SD: 3                     Min positive DS: 1

Max positive SD: 10                    Max positive DS: 1

    Positive SD number: 3                  Positive DS number: 2

    Positive SD sum: 18                    Positive DS sum: 2

    Positive SD average: 6                 Positive DS average: 1

    Positive SD square-sum: 134            Positive DS square-sum: 2

Min negative SD: 3                     Min negative DS: 1

    Max negative SD: 9                     Max negative DS: 1

    Negative SD number: 4                  Negative DS number: 2

    Negative SD sum: 25                    Negative DS sum: 2

    Negative SD average: 6                 Negative DS average: 1

Negative SD square-sum: 187            Negative DS square-sum: 2

  One way results:

    Max SD delay: 0                        Max DS delay: 0

Min SD delay: 0                        Min DS delay: 0

Number of SD delay: 0                  Number of DS delay: 0

    Sum of SD delay: 0                     Sum of DS delay: 0

    Square-Sum of SD delay: 0              Square-Sum of DS delay: 0

    SD lost packets: 0                     DS lost packets: 0

    Lost packets for unknown reason: 0

  Voice scores:

    Max MOS value: 4.40                    Min MOS value: 4.40

    Max ICPIF value: 0                     Min ICPIF value: 0

  Reaction statistics:

    Index  Checked Element  Threshold Type  Checked Num  Over-threshold Num

    1      ICPIF            -               -            -

    2      MOS              -               -            -

\# 显示Path-jitter测试的统计信息。

\<Sysname\> display nqa statistics admin test

NQA entry (admin admin, tag test) test statistics:

  NO. : 1

  Path 1:

  Hop IP 192.168.40.210

    Basic Results:

      Send operation times: 10

      Receive response times: 10

      Min/Max/Average round trip time: 1/1/1

      Square-Sum of round trip time: 10

    Extended Results:

      Packet loss ratio: 0%

      Failures due to timeout: 0

      Failures due to internal error: 0

      Failures due to other errors: 0

      Packets out of sequence: 0

      Packets arrived late: 0

    Path-Jitter Results:

      Jitter number: 9

        Min/Max/Average jitter: 0/0/0

      Positive jitter number: 0

        Min/Max/Average positive jitter: 0/0/0

        Sum/Square-Sum positive jitter: 0/0

      Negative jitter number: 0

        Min/Max/Average negative jitter: 0/0/0

        Sum/Square-Sum negative jitter: 0/0

  Hop IP 192.168.50.209

    Basic Results:

      Send operation times: 10

      Receive response times: 10

      Min/Max/Average round trip time: 1/1/1

      Square-Sum of round trip time: 10

    Extended Results:

      Packet loss ratio: 0%

      Failures due to timeout: 0

      Failures due to internal error: 0

      Failures due to other errors: 0

      Packets out of sequence: 0

      Packets arrived late: 0

    Path-Jitter Results:

      Jitter number: 9

        Min/Max/Average jitter: 0/0/0

      Positive jitter number: 0

        Min/Max/Average positive jitter: 0/0/0

        Sum/Square-Sum positive jitter: 0/0

      Negative jitter number: 0

        Min/Max/Average negative jitter: 0/0/0

        Sum/Square-Sum negative jitter: 0/0

表1-6 display nqa statistics命令显示信息描述

字段

描述

No.

统计组的组号

Start time

测试组启动时间

Life time

测试的持续时间，单位为秒

Send operation times

发送的探测报文数

Receive response times

收到的响应报文数

Min/Max/Average round trip time

最小/最大/平均往返时间，单位为毫秒

Square-Sum of round trip time

往返时间平方和

Packet loss ratio

平均丢包率

Failures due to timeout

测试过程中超时的次数

Failures due to disconnect

对方强制断开连接的次数

Failures due to no connection

和对方建立连接失败的次数

Failures due to internal error

因内部错误失败的次数

Failures due to other errors

因其它错误失败的次数

Packets out of sequence

报文失序的次数

Packets arrived late

迟到报文个数

UDP-jitter results

UDP-jitter测试的结果，只在UDP-jitter测试中存在此信息

Voice results

Voice测试的结果，只在Voice测试中存在此信息

RTT number

收到的响应报文数

Min positive SD

源到目的方向抖动时延为正值的最小值

Min positive DS

目的到源方向抖动时延为正值的最小值

Max positive SD

源到目的方向抖动时延为正值的最大值

Max positive DS

目的到源方向抖动时延为正值的最大值

Positive SD number

源到目的方向抖动时延为正值的数目

Positive DS number

目的到源方向抖动时延为正值的数目

Positive SD sum

源到目的方向抖动时延为正值的和

Positive DS sum

目的到源方向抖动时延为正值的和

Positive SD average

源到目的方向抖动时延为正值的平均值

Positive DS average

目的到源方向抖动时延为正值的平均值

Positive SD square-sum

源到目的方向抖动时延为正值的平方和

Positive DS square-sum

目的到源方向抖动时延为正值的平方和

Min negative SD

源到目的方向抖动时延为负值的最小绝对值

Min negative DS

目的到源方向抖动时延为负值的最小绝对值

Max negative SD

源到目的方向抖动时延为负值的最大绝对值

Max negative DS

目的到源方向抖动时延为负值的最大绝对值

Negative SD number

源到目的方向抖动时延为负值的数目

Negative DS number

目的到源方向抖动时延为负值的数目

Negative SD sum

源到目的方向抖动时延为负值的绝对值和

Negative DS sum

目的到源方向抖动时延为负值的绝对值和

Negative SD average

源到目的方向抖动时延为负值的绝对值的平均值

Negative DS average

目的到源方向抖动时延为负值的绝对值的平均值

Negative SD square-sum

源到目的方向抖动时延为负值的平方和

Negative DS square-sum

目的到源方向抖动时延为负值的平方和

One way results

单向延迟测试结果，只有UDP-Jitter和Voice类型测试有单向延迟测试结果

Max SD delay

源到目的的最大时延

Max DS delay

目的到源的最大时延

Min SD delay

源到目的的最小时延

Min DS delay

目的到源的最小时延

Number of SD delay

源到目的计算的时延数

Number of DS delay

目的到源计算的时延数

Sum of SD delay

源到目的的时延和

Sum of DS delay

目的到源的时延和

Square-Sum of SD delay

源到目的的时延的平方和

Square-Sum of DS delay

目的到源的时延的平方和

SD lost packets

源到目的方向丢失的报文个数

DS lost packets

目的到源方向丢失的报文个数

Lost packets for unknown reason

不能确定原因丢失的报文个数

Voice scores

语音参数，只在voice类型测试有此信息

Max MOS value

最大MOS值

Min MOS value

最小MOS值

Max ICPIF value

最大ICPIF值

Min ICPIF value

最小ICPIF值

Reaction statistics

阈值告警组在统计周期内的监测结果

Index

阈值告警组的编号

Checked Element

监测对象

Threshold Type

阈值类型

Checked Num

已监测的样本个数

Over-threshold Num

超出阈值的样本个数

Path

Path-jitter测试结果的路径序号，只在Path-jitter测试中存在此信息

Hop IP

本跳IP地址，只在Path-jitter测试中存在此信息

Path-jitter results

Path-jitter测试的结果，只在Path-jitter测试中存在此信息

Jitter number

计算抖动次数，只在Path-jitter测试中存在此信息

Min/Max/Average jitter

最小/最大/平均抖动时延，单位为毫秒，只在Path-jitter测试中存在此信息

Positive jitter number

正抖动时延的数目，只在Path-jitter测试中存在此信息

Min/Max/Average positive jitter

最小/最大/平均正抖动时延，单位为毫秒，只在Path-jitter测试中存在此信息

Sum/Square-Sum positive jitter

正抖动时延之和/平方和，只在Path-jitter测试中存在此信息

Negative jitter number

负抖动时延的数目，只在Path-jitter测试中存在此信息

Min/Max/Average negative jitter

最小/最大/平均负抖动时延，单位为毫秒，只在Path-jitter测试中存在此信息

Sum/Square-Sum negative jitter

负抖动时延之和/平方和，只在Path-jitter测试中存在此信息

表1-7 display nqa statistics命令显示阈值告警功能相关字段取值描述

监测对象

阈值类型

监测的样本范围

Checked Num取值

Over-threshold Num取值

probe-duration

accumulate

统计周期内，进行的探测

统计周期内，已完成的探测次数

统计周期内，探测持续时间不在阈值范围内的探测次数

average

-

-

-

consecutive

统计周期内，进行的探测

统计周期内，已完成的探测次数

统计周期内，探测持续时间不在阈值范围内的探测次数

probe-fail

accumulate

统计周期内，进行的探测

统计周期内，已完成的探测次数

统计周期内，失败的探测次数

consecutive

统计周期内，进行的探测

统计周期内，已完成的探测次数

统计周期内，失败的探测次数

RTT

accumulate

统计周期内，发送的报文

统计周期内，已发送的报文个数

统计周期内，往返时间不在阈值范围内的报文个数

average

-

-

-

jitter-DS/jitter-SD

accumulate

统计周期内，发送的报文

统计周期内，已发送的报文个数

统计周期内，单向时延抖动不在阈值范围内的报文个数

average

-

-

-

OWD-DS/OWD-SD

-

统计周期内，发送的报文

统计周期内，已发送的报文个数

统计周期内，单向时延不在阈值范围内的报文个数

packet-loss

accumulate

统计周期内，发送的报文

统计周期内，已发送的报文个数

统计周期内的丢包数

ICPIF

-

-

-

-

MOS

-

-

-

-

【相关命令】

·**statistics interval**

**NQA \-- NQA客户端配置命令 \-- expect data**

------------------------------------------------------------------------

**[expect data**]命令用来配置期望的应答内容。

**[undo expect data**]命令用来恢复缺省情况。

【命令】

**[expect data ***expression * **offset** *number* ]

**[undo expect data**]

【缺省情况】

未配置期望的应答内容。

【视图】

HTTP/TCP/UDP类型的NQA模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[expression*]：期望收到的应答内容，为1～200个字符的字符串，区分大小写。

**[offset** *number*]：所期望的内容在返回报文中的偏移量，取值范围为0～1000，缺省值为0。

【使用指导】

在NQA测试过程中，配置了该命令以后，NQA客户端会检查接收到的测试报文中的应答内容：如果应答内容和该命令配置内容相同，则表示当前NQA目的端设备合法；否则为非法设备。

对于HTTP类型的NQA模板，仅当回应报文中存在Content-Length头域时，进行期望应答内容的检查，否则不做检查。

对于TCP类型的NQA模板，仅当**data-fill**和**expect data**命令都配置时，进行期望应答内容的检查，否则不做检查。

对于UDP类型的NQA模板，由于UDP报文数据字段的前5个字节具有特定用途。缺省情况下，配置**expect data**后从第6个字节开始进行偏移检查。

【举例】

\# 在HTTP类型的NQA模板视图下，配置期望的应答为welcome!。

\<Sysname\> system-view

Sysname nqa template http httptplt

Sysname-nqatplt-http-httptplt expect data welcome!

**NQA \-- NQA客户端配置命令 \-- expect status**

------------------------------------------------------------------------

**[expect status**]命令用来配置期望的应答状态码。

**[undo expect status**]命令用来恢复缺省情况。

【命令】

**[expect status** *status-list*]

**[undo expect status** \*[status-list* ]]

【缺省情况】

未配置期望状态码。

【视图】

HTTP类型的模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[status-list*]：状态码列表，即HTTP模板类型期望收到的状态码范围。表示方式为*status-list* = { *status-num*1 [ to *status-num*2  }&\<1-10\>]，*status-num*取值范围为0～999，*status-num*2的值要大于或等于*status-num*1的值，&\<1-10\>表示前面的参数最多可以重复输入10次。

【使用指导】

HTTP类型的NQA模板支持配置状态码。HTTP报文的状态码是由3位十进制数组成的字段，它包含HTTP服务器的状态信息，用户可以根据该状态码了解HTTP服务器的状态。状态码的第一位规定状态码的类型，后两位编码没有规则。

【举例】

\# 在HTTP类型的NQA模板视图下，配置期望状态码，允许状态码为200、300、400～500。

\<Sysname\> system-view

Sysname nqa template http httptplt

Sysname-nqatplt-http-httptplt expect status 200 300 400 to 500

**NQA \-- NQA客户端配置命令 \-- expect ip**

------------------------------------------------------------------------

**[expect ip**]命令用来配置期望返回的IP地址。

**[undo expect ip**]命令用来取消期望返回的IP地址。

【命令】

**[expect ip **]*ip-address*

**[undo expect ip**]

【缺省情况】

未配置期望返回的IP地址。

【视图】

DNS类型的NQA模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：DNS探测期望返回的IP地址。

【使用指导】

在DNS测试中，NQA客户端通过该命令配置的IP地址与DNS服务器通过域名解析出的IP地址进行比较，若相同，则证明目前测试的DNS服务器合法，否则为非法DNS服务器。

【举例】

\# 在DNS类型的NQA模板视图下，配置期望返回的地址为1.1.1.1。

\<Sysname\> system-view

Sysname nqa template dns dnstplt

Sysname-nqatplt-dns-dnstplt expect ip 1.1.1.1

**NQA \-- NQA客户端配置命令 \-- expect ipv6**

------------------------------------------------------------------------

**[expect ipv6**]命令用来配置期望返回的IPv6地址。

**[undo expect ipv6**]命令用来取消期望返回的IPv6地址配置。

【命令】

**[expect ipv6 ***ipv6-address*]

**[undo expect ipv6**]

【缺省情况】

无期望返回的IPv6地址。

【视图】

DNS类型的NQA模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：DNS探测期望返回的IPv6地址。

【使用指导】

在DNS测试中，NQA客户端通过该命令配置的IPv6地址与DNS服务器通过域名解析出的IPv6地址进行比较，若相同，则证明目前测试的DNS服务器合法，否则为非法DNS服务器。

【举例】

\# 在DNS类型的NQA模板视图下，配置期望返回的IPv6地址为1::1。

\<Sysname\> system-view

Sysname nqa template dns dnstplt

Sysname-nqatplt-dns-dnstplt expect ipv6 1::1

**NQA \-- NQA客户端配置命令 \-- filename**

------------------------------------------------------------------------

**[filename**]命令用来配置FTP服务器和客户端之间传送文件的文件名。

**[undo filename**]命令用来恢复缺省情况。

【命令】

**[filename** *filename*]

**[undo** **filename**]

【缺省情况】

未配置FTP服务器和客户端之间传送文件的文件名。

【视图】

FTP测试类型视图

FTP类型的NQA模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[filename*]：FTP服务器和客户端之间传送文件的文件名，为1～200个字符的字符串，字符串中不能包括"/"，区分大小写。

【举例】

\# 配置FTP服务器和客户端之间要传送文件的文件名为config.txt。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type ftp

Sysname-nqa-admin-test-ftp filename config.txt

\# 在FTP类型的NQA模板视图下，配置FTP服务器和客户端之间要传送文件的文件名为config.txt。

\<Sysname\> system-view

Sysname nqa template ftp ftptplt

Sysname-nqatplt-ftp-ftptplt filename config.txt

**NQA \-- NQA客户端配置命令 \-- frequency**

------------------------------------------------------------------------

**[frequency**]命令用来配置测试组连续两次测试开始时间的时间间隔。

**[undo frequency**]命令用来恢复缺省情况。

【命令】

**[frequency** *interval*]

**[undo** **frequency**]

【缺省情况】

在NQA测试类型视图下，Voice、Path-jitter测试中连续两次测试开始时间的时间间隔为60000毫秒；其他类型的测试中连续两次测试开始时间的时间间隔为0毫秒，即只进行一次测试。

在NQA模板视图下，测试中连续两次测试开始时间的时间间隔为5000毫秒。

【视图】

任意测试类型视图

任意类型的NQA模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：连续两次测试开始时间的时间间隔，取值范围为0～604800000，单位为毫秒。时间间隔为0，表示两次测试的时间间隔为无穷，即只进行一次测试，此时不会生成统计结果。

【使用指导】

通过**nqa** **schedule**命令启动NQA测试组后，每隔*interval*时间启动一次测试。

需要注意的时，如果到达**frequency**指定的时间间隔时，上次测试尚未完成，则不启动新一轮测试。

【举例】

\# 配置连续两次测试开始时间的时间间隔为1000毫秒。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type icmp-echo

Sysname-nqa-admin-test-icmp-echo frequency 1000

\# 在DNS类型的NQA模板视图下，配置连续两次测试开始时间的时间间隔为1000毫秒。

\<Sysname\> system-view

Sysname nqa template dns dnstplt

Sysname-nqatplt-dns-dnstplt frequency 1000

**NQA \-- NQA客户端配置命令 \-- history-record enable**

------------------------------------------------------------------------

**[history-record enable**]命令用来开启NQA测试组的历史记录保存功能。

**[undo** **history-record enable**]命令用来关闭NQA测试组的历史记录保存功能。

【命令】

**[history-record enable**]

**[undo history-record enable**]

【缺省情况】

UDP-tracert测试类型的历史记录保存功能处于开启状态，其他类型的NQA测试组的历史记录保存功能处于关闭状态。

【视图】

DHCP/DLSw/DNS/FTP/HTTP/ICMP-echo/SNMP/TCP/UDP-echo/UDP-tracert测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·如果开启NQA测试组的历史记录保存功能，则系统会记录该NQA测试组的历史信息，通过**display nqa history**命令可以查看该测试组的历史记录信息。

·如果关闭NQA测试组的历史记录保存功能，则系统不会记录该测试组的历史信息，原有的历史记录信息也会被删除。

【举例】

\# 开启NQA测试组的历史记录保存功能。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type icmp-echo

Sysname-nqa-admin-test-icmp-echo history-record enable

【相关命令】

·**display nqa history**

**NQA \-- NQA客户端配置命令 \-- history-record keep-time**

------------------------------------------------------------------------

**[history-record keep-time**]命令用来配置NQA测试组中历史记录的保存时间。

**[undo** **history-record keep-time**]命令用来恢复缺省情况。

【命令】

**[history-record keep-time ***keep-time*]

**[undo history-record keep-time**]

【缺省情况】

NQA测试组中历史记录的保存时间为120分钟。

【视图】

DHCP/DLSw/DNS/FTP/HTTP/ICMP-echo/SNMP/TCP/UDP-echo/UDP-tracert测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[keep-time*]：历史记录的保存时间，取值范围为1～1440，单位为分钟。

【使用指导】

NQA测试结束后，开始计算该测试组中所有历史记录的保存时间。保存时间达到配置的值后，将删除这些记录。

【举例】

\# 配置NQA测试组中历史记录的保存时间为100分钟。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type icmp-echo

Sysname-nqa-admin-test-icmp-echo history-record keep-time 100

**NQA \-- NQA客户端配置命令 \-- history-record number**

------------------------------------------------------------------------

**[history-record number**]命令用来配置在一个测试组中能够保存的最大历史记录个数。

**[undo** **history-record number**]命令用来恢复缺省情况。

【命令】

**[history-record number ***number*]

**[undo history-record number**]

【缺省情况】

一个测试组中能够保存的最大历史记录个数为50。

【视图】

DHCP/DLSw/DNS/FTP/HTTP/ICMP-echo/SNMP/TCP/UDP-echo/UDP-tracert测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：在一个测试组中能够保存的最大历史记录个数，取值范围为0～50。

【使用指导】

如果一个测试组中历史记录个数超过设定的最大数目，则最早的历史记录将会被删除。

【举例】

\# 配置一个测试组中能够保存的最大历史记录数为10个。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type icmp-echo

Sysname-nqa-admin-test-icmp-echo history-record number 10

**NQA \-- NQA客户端配置命令 \-- init-ttl**

------------------------------------------------------------------------

**[init-ttl**]命令用来配置UDP-tracert探测报文的初始跳数。

**[undo init-ttl**]命令用来恢复缺省情况。

【命令】

**[init-ttl ***value*]

**[undo init-ttl**]

【缺省情况】

UDP-tracert探测报文的初始跳数为1。

【视图】

UDP-tracert测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：UDP-tracert探测报文的初始跳数，取值范围1～255。

【举例】

\# 配置UDP-tracert探测报文的初始跳数为5跳。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type udp-tracert

Sysname-nqa-admin-test-udp-tracert init-ttl 5

**NQA \-- NQA客户端配置命令 \-- key**

------------------------------------------------------------------------

**[key**]命令用来设置RADIUS认证使用的共享密钥。

**[undo key**]命令用来取消设置的共享密钥。

【命令】

**[key **[{ **cipher** \| **simple** } *string*]]

**[undo key**]

【缺省情况】

未设置RADIUS认证使用的共享密钥。

【视图】

RADIUS类型的NQA模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cipher**]：表示以密文方式设置RADIUS认证使用的共享密钥。

**[simple**]：表示以明文方式设置RADIUS认证使用的共享密钥。

*[string*]：设置的明文密钥或密文密钥，区分大小写。明文密钥为1～64个字符的字符串；密文密钥为1～117个字符的字符串。

【使用指导】

·必须保证设备上设置的共享密钥与RADIUS服务器上的完全一致。

·以明文或密文方式设置的共享密钥，均以密文的方式保存在配置文件中。

【举例】

\# 设置RADIUS认证使用的共享密钥为明文abc。

\<Sysname\> system-view

Sysname nqa template radius radiustplt

Sysname-nqatplt-radius-radiustplt key simple abc

**NQA \-- NQA客户端配置命令 \-- lsr-path**

------------------------------------------------------------------------

**[lsr-path**]命令用来配置松散路由。

**[undo lsr-path**]命令用来恢复缺省情况。

【命令】

**[lsr-path ***ip-address*&*\<*1*-*8*\>*]

**[undo lsr-path**]

【缺省情况】

未配置松散路由。

【视图】

Path-jitter测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*&*\<*1*-*8*\>*]：松散路由IP地址，&\<1-8\>表示最多可以输入8个IP地址，每个IP地址之间用空格分隔。

【使用指导】

通过本命令配置松散路由，用户只需给出NQA测试报文必须经过的一些"节点"，并不需要给出一条完备的路径，无直接连接的"节点"之间的路由需要路由器寻址功能补充。

Path-jitter测试中，NQA客户端通过tracert过程使用该命令配置的松散路由进行探路，并根据收到ICMP报文计算主要"节点"时延和时延抖动。

【举例】

\# 配置松散路由为10.1.1.20和10.1.2.10两跳。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type path-jitter

Sysname-nqa-admin-test- path-jitter lsr-path 10.1.1.20 10.1.2.10

**NQA \-- NQA客户端配置命令 \-- max-failture**

------------------------------------------------------------------------

**[max-failure**]命令用来配置一次UDP-tracert测试中连续探测失败的最大次数。

**[undo max-failure**]命令用来恢复缺省情况。

【命令】

**[max-failure** *value*]

**[undo max-failure**]

【缺省情况】

一次UDP-tracert测试中连续探测失败的最大次数为5。

【视图】

UDP-tracert测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：表示一次UDP-tracert测试中连续探测失败的最大次数。取值范围0～255。0和255意味着UDP-tracert探测不会因为连续探测失败而停止测试。

【举例】

\# 配置一次UDP-tracert测试中连续探测失败的最大次数为20次。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type udp-tracert

Sysname-nqa-admin-test-udp-tracert max-failure 20

**NQA \-- NQA客户端配置命令 \-- mode**

------------------------------------------------------------------------

**[mode**]命令用来配置FTP测试的数据传输方式。

**[undo mode**]命令用来恢复缺省情况。

【命令】

**[mode **[{ **active** \| **passive** }]]

**[undo** **mode**]

【缺省情况】

FTP测试的数据传输方式为主动方式。

【视图】

FTP测试类型视图

FTP类型的NQA模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[active**]：设置FTP的数据传输方式为主动方式。

**[passive**]：设置FTP的数据传输方式为被动方式。

【使用指导】

FTP的数据传输方式分为：主动方式和被动方式。主动方式是指在建立数据连接时由服务器主动发起连接请求；被动方式是指在建立数据连接时由客户端主动发起连接请求。

【举例】

\# 配置FTP测试的数据传输方式为被动方式。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type ftp

Sysname-nqa-admin-test-ftp mode passive

\# 在FTP类型的NQA模板视图下，配置数据传输方式为被动方式。

\<Sysname\> system-view

Sysname nqa template ftp ftptplt

Sysname-nqatplt-ftp-ftptplt mode passive

**NQA \-- NQA客户端配置命令 \-- next-hop**

------------------------------------------------------------------------

**[next-hop**]命令用来配置探测报文的下一跳IP地址。

**[undo next-hop**]命令用来删除所配置的下一跳IP地址。

【命令】

**[next-hop** *ip-address*]

**[undo** **next-hop**]

【缺省情况】

未配置下一跳IP地址。

【视图】

ICMP-echo测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：探测报文的下一跳IP地址。

【举例】

\# 配置探测报文的下一跳IP地址为10.1.1.1。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type icmp-echo

Sysname-nqa-admin-test-icmp-echo next-hop 10.1.1.1

**NQA \-- NQA客户端配置命令 \-- no-fragment enable**

------------------------------------------------------------------------

**[no-fragment enable**]命令用来开启UDP-tracert探测类型的禁止报文分片功能。

**[undo no-fragment enable**]命令用来关闭UDP-tracert探测类型的禁止报文分片功能。

【命令】

**[no-fragment enable**]

**[undo no-fragment enable**]

【缺省情况】

UDP-tracert测试类型的禁止报文分片功能处于关闭状态。

【视图】

UDP-tracert测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启此功能后，设备发送的IP报文头部的DF（don\'t fragment）字段会被置一，这样报文在转发过程中将无法被分片。通过配置这条命令可以对一条链路的路径MTU值进行测试。

【举例】

\# 开启UDP-tracert探测类型的禁止报文分片功能。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type udp-tracert

Sysname-nqa-admin-test-udp-tracert no-fragment enable

**NQA \-- NQA客户端配置命令 \-- nqa**

------------------------------------------------------------------------

**[nqa**]命令用来创建NQA测试组，并进入NQA测试组视图。

**[undo nqa**]命令用来删除NQA测试组。

【命令】

**[nqa******entry*** admin-name* *operation-tag*]

**[undo nqa**[ { **all** \| **entry** *admin-name* *operation-tag* }]]

【缺省情况】

设备上不存在任何NQA测试组。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[admin-name*]：创建NQA测试组的管理员名字，为1～32个字符的字符串，字符串中不能包括"-"，不区分大小写。

*[operation-tag*]：测试操作的标签，为1～32个字符的字符串，字符串中不能包括"-"，不区分大小写。

**[all**]：所有NQA测试组。

【使用指导】

如果配置了测试组的测试类型，执行**nqa entry**命令进入该测试组时，系统将直接进入测试类型视图。

【举例】

\# 创建一个管理员名为admin，测试操作标签为test的NQA测试组，并进入NQA测试组视图。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test

**NQA \-- NQA客户端配置命令 \-- nqa template**

------------------------------------------------------------------------

**[nqa template**]命令用来创建指定类型NQA模板，并进入NQA模板视图。

**[undo nqa template**]命令用来删除NQA模板。

【命令】

**[nqa template **[{ **dns** \| **ftp** \| **http** \| **icmp** \| **radius** \| **tcp** \| **udp** } *name*]]

**[undo nqa template **[{ **dns** \| **ftp** \| **http** \| **icmp** \| **radius** \| **tcp** \| **udp** } *name*]]

【缺省情况】

设备上不存在任何类型的NQA模板。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[dns**]：配置DNS模板类型。

**[ftp**]：配置FTP模板类型。

**[http**]：配置HTTP模板类型。

**[icmp**]：配置ICMP模板类型。

**[radius**]：配置RADIUS模板类型。

**[tcp**]：配置TCP模板类型。

**[udp**]：配置UDP模板类型。

*[name*]：NQA模板名称，为1～32个字符的字符串，不区分大小写。

【举例】

\# 创建一个类型为icmp名称为icmptplt的模板，并进入NQA模板视图。

\<Sysname\> system-view

Sysname nqa template icmp icmptplt

Sysname-nqatplt-icmp-icmptplt

**NQA \-- NQA客户端配置命令 \-- nqa agent enable**

------------------------------------------------------------------------

**[nqa agent enable**]命令用来开启NQA客户端功能。

**[undo nqa agent enable**]命令用来关闭NQA客户端功能，并停止所有正在进行的测试。

【命令】

**[nqa agent** **enable**]

**[undo nqa agent enable**]

【缺省情况】

NQA客户端功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 开启NQA客户端功能。

\<Sysname\> system-view

Sysname nqa agent enable

【相关命令】

·**nqa server enable**

**NQA \-- NQA客户端配置命令 \-- nqa schedule**

------------------------------------------------------------------------

**[nqa schedule**]命令用来配置测试组的启动时间和持续时间。

**[undo nqa schedule**]命令用来停止该测试组的测试。

【命令】

**[nqa schedule ***admin-name*[ *operation-tag* **start-time** { *hh*:*mm*:*ss* [ *yyyy/mm/dd \| mm/dd/yyyy* ] \| **now** } **lifetime** { *lifetime \|* **forever** }  **recurring** ]]

**[undo nqa schedule***admin-name* *operation-tag*]

【缺省情况】

未配置NQA调度功能。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[admin-name*]：创建NQA测试组的管理员名字，为1～32个字符的字符串，字符串中不能包括"-"，不区分大小写。

*[operation-tag*]：测试操作的标签，为1～32个字符的字符串，字符串中不能包括"-"，不区分大小写。

**[start-time**]：指定测试组的启动时间和日期。

*[hh*:*mm*:*ss*]：测试组的启动时间，小时:分钟:秒。

*[yyyy/mm/dd*]：测试组的启动日期，年:月:日，缺省值为系统的当前日期，年的取值范围为2000～2035。

*[mm/dd/yyyy*]：测试组的启动日期，月:日:年，缺省值为系统的当前日期，年的取值范围为2000～2035。

**[now**]：测试组立即开始测试。

**[lifetime**]：指定测试的持续时间。

*[lifetime*]：测试的持续时间，取值范围为1～2147483647，单位为秒。

**[forever**]：测试组将一直进行测试。

**[recurring**]：指定测试组每天都被调度运行。每天启动测试的时间由start-time参数指定。

【使用指导】

·测试组被调度后不允许进入测试组视图和测试类型视图。

·系统时间在启动时间～启动时间＋持续时间范围内时，测试组进行测试。执行**nqa schedule**命令时，如果系统时间尚未到达启动时间，则到达启动时间后，启动测试；如果系统时间在启动时间～启动时间＋持续时间之间，则立即启动测试；如果系统时间已经超过启动时间＋持续时间，则不会启动测试。通过**display clock**命令可以显示系统的当前时间。

·配置lifetime时间请保证一次测试能够完成，否则无法完成正常的联动操作

【举例】

\# 启动管理员名字为admin，标签为test的测试组进行测试，测试组的启动时间为2008年8月8日以后（包含当天）的每天的08:08:08，测试持续时间为1000秒。

\<Sysname\> system-view

Sysname nqa schedule admin test start-time 08:08:08 2008/08/08 lifetime 1000 recurring

【相关命令】

·**destination ip**

·**display clock**（基础配置命令参考/设备管理）

·**nqa entry **

·**type**

**NQA \-- NQA客户端配置命令 \-- operation (FTP test type view)**

------------------------------------------------------------------------

**[operation**]命令用来配置FTP测试的操作方式。

**[undo operation**]命令用来恢复缺省情况。

【命令】

**[operation **[{ **get** \| **put** }]]

**[undo operation**]

【缺省情况】

FTP测试的操作方式为**get**操作。

【视图】

FTP测试类型视图

FTP类型的模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[get**]：从FTP服务器获取文件。

**[put**]：向FTP服务器传送文件。

【使用指导】

·进行**put**操作时，若配置了**filename**，发送数据前判断**filename**指定的文件是否存在，如果存在则上传该文件，如果不存在则探测失败。

·进行**get**操作时，如果FTP服务器上没有以**url**中所配置的文件名为名字的文件，则测试不会成功。进行**get**操作时，设备上不会保存从服务器获取的文件。

·进行**get、put**操作时，请选用较小的文件进行测试，如果文件较大，可能会因为超时而导致测试失败，或由于占用较多的网络带宽而影响其他业务。

【举例】

\# 配置FTP测试的操作方式为**put**操作。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type ftp

Sysname-nqa-admin-test-ftp operation put

\# 在FTP类型的NQA模板视图下，配置测试的操作方式为**put**操作。

\<Sysname\> system-view

Sysname nqa template ftp ftptplt

Sysname-nqatplt-ftp-ftptplt operation put

**NQA \-- NQA客户端配置命令 \-- operation (HTTP test type view)**

------------------------------------------------------------------------

**[operation**]命令用来配置HTTP测试的操作方式。

**[undo operation**]命令用来恢复缺省情况。

【命令】

**[operation **[{ **get** \| **post** \| **raw** }]]

**[undo operation**]

【缺省情况】

HTTP测试的操作方式为**get**操作。

【视图】

HTTP测试类型视图

HTTP类型的NQA模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[get**]：从HTTP服务器获取数据。

**[post**]：向HTTP服务器提交数据。

**[raw**]：使用原始报文向服务器发送探测报文。

【使用指导】

HTTP测试的操作方式为**get**或**post**时，请求报文内容从url中获取。HTTP测试的操作方式为**raw**时，请求报文为**raw-request**子视图中配置的内容。

【举例】

\# 配置HTTP测试的操作方式为**raw**操作。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type http

Sysname-nqa-admin-test-http operation raw

\# 在HTTP类型的NQA模板视图下，配置测试的操作方式为**raw**操作。

\<Sysname\> system-view

Sysname nqa template http httptplt

Sysname-nqatplt-http-httptplt operation raw

**NQA \-- NQA客户端配置命令 \-- out interface**

------------------------------------------------------------------------

**[out interface**]命令用来指定探测报文的出接口。

**[undo out interface**]命令用来恢复缺省情况。

【命令】

**[out interface** *interface-type interface-number*]

**[undo out interface**]

【缺省情况】

未指定探测报文的出接口。

【视图】

DHCP/ICMP-echo/UDP-tracert测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type interface-number*]：探测报文出接口的接口类型和接口编号。

【使用指导】

·该命令指定的接口必须处于UP状态，否则NQA探测过程将会失败。

·对于ICMP-echo测试类型，如果配置**next-hop**命令，此配置不生效。

【举例】

·路由应用

\# 配置接口GigabitEthernet1/0/1作为UDP-tracert探测报文出接口。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type udp-tracert

Sysname-nqa-admin-test-udp-tracert out interface gigabitethernet 1/0/1

·交换应用

\# 配置VLAN接口2作为UDP-tracert探测报文的出接口。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type udp-tracert

Sysname-nqa-admin-test-udp-tracert out interface vlan-interface 2

**NQA \-- NQA客户端配置命令 \-- password**

------------------------------------------------------------------------

**[password**]命令用来配置FTP或HTTP登录密码。

**[undo password**]命令用来取消已配置的登录密码。

【命令】

**[password****cipher**[ \| ]**simple** } *password*

**[undo password**]

【缺省情况】]

未配置FTP或HTTP的登录密码。

【视图】

FTP/HTTP测试类型视图

FTP/HTTP/RADIUS类型的NQA模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cipher**]：表示以密文形式设置密码。

**[simple**]：表示以明文形式设置密码。

*[password*]：测试使用的密码，区分大小写。FTP或HTTP的登录密码，明文形式输入密码时为1～32个字符的字符串，密文形式输入密码时为1～73个字符的字符串；RADIUS密码，明文形式输入时为1～64个字符的字符串，密文形式输入时为1～117个字符的字符串。

【使用指导】

以明文或密文方式设置的用户密码，均以密文的方式保存在配置文件中。

【举例】

\# 配置录FTP登录密码为ftpuser。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type ftp

Sysname-nqa-admin-test-ftp password simple ftpuser

\# 在FTP类型的NQA模板视图下，配置FTP登录密码为ftpuser。

\<Sysname\> system-view

Sysname nqa template ftp ftptplt

Sysname-nqatplt-ftp-ftptplt password simple ftpuser

【相关命令】

·**operation**

·**username**

**NQA \-- NQA客户端配置命令 \-- probe count**

------------------------------------------------------------------------

**[probe count**]命令用来配置一次NQA测试中探测的次数。

**[undo probe count**]命令用来恢复缺省情况。

【命令】

**[probe count** *times*]

**[undo probe count**]

【缺省情况】

对于UDP-tracert测试类型，对于一个TTL值的节点发送的探测报文次数为3次；其他类型的NQA测试一次NQA测试中的探测次数为1次。

【视图】

DHCP/DNS/DLSw/FTP/HTTP/ICMP-echo/SNMP/TCP/UDP-echo/UDP-jitter/UDP-tracert测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[times*]：对于UDP-tracert测试类型，配置对于一个TTL值的节点发送的探测报文次数，取值范围为1～10；对于其他测试类型，配置的是一次NQA测试中进行探测的次数，取值范围为1～15。

【使用指导】

·对于TCP和DLSw测试，一次探测操作是指建立一次连接；

·对于UDP-jitter和Voice测试，一次探测操作是指连续发送多个探测报文，发送探测报文的个数由**probe packet-number**命令指定；

·对于FTP、HTTP、DHCP和DNS测试，一次探测操作是指完成一次相应的功能，例如上传或下载一个文件，获取一个Web页面，为接口申请一个IP地址，将一个域名解析为IP地址；

·对于ICMP-echo和UDP-echo测试，一次探测操作是指发送一个探测报文；

·对于SNMP测试，一次探测操作是指发送三个SNMP协议报文，分别对应SNMP v1、SNMP v2c和SNMP v3三个版本；

·对于Path-jitter测试，一次探测操作分为两个步骤：首先通过tracert探路获取到达目的地址的路径（最大为64跳）；再根据tracert结果，分别向路径上的每一跳发送多个ICMP-echo探测报文，发送探测报文的个数由用户来设定；

·对于UDP-tracert测试，对目的节点进行的整个Tracert过程称为一次测试，对于一个特定TTL值的节点发送一个探测报文的操作称为一次探测，对于同一个TTL值的节点发送探测报文的次数由**probe count**命令来设定。

对于UDP-tracert测试来说，对于同一个TTL的节点，设备会发送数量为**probe count**命令配置的探测报文，系统在进行第一次探测之后，等待回应；对于其他类型的测试，如果配置的次数大于1，那么系统在进行第一次探测之后，等待回应。如果到达**probe timeout**命令指定的探测超时时间时，仍然没有收到回应，则发起第二次探测。如此反复，直到完成指定次数的探测。

需要注意的是，Voice和Path-jitter测试不支持该命令，一次测试中只能进行一次探测。

【举例】

\# 配置一次ICMP-echo测试中探测的次数为10次。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type icmp-echo

Sysname-nqa-admin-test-icmp-echo probe count 10

**NQA \-- NQA客户端配置命令 \-- probe packet-interval**

------------------------------------------------------------------------

**[probe packet-interval**]命令用来配置测试中发送探测报文的时间间隔。

**[undo probe packet-interval**]命令用来恢复缺省情况。

【命令】

**[probe packet-interval ***packet-interval*]

**[undo probe packet-interval**]

【缺省情况】

测试中发送探测报文的时间间隔为20毫秒。

【视图】

Path-jitter/UDP-jitter/Voice测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[packet-interval*]：测试中发送探测报文的时间间隔，取值范围为10～60000，单位为毫秒。

【举例】

\# 配置UDP-jitter测试中发送探测报文的时间间隔为100毫秒。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type udp-jitter

Sysname-nqa-admin-test-udp-jitter probe packet-interval 100

**NQA \-- NQA客户端配置命令 \-- probe packet-number**

------------------------------------------------------------------------

**[probe packet-number**]命令用来配置一次探测中发送探测报文的个数。

**[undo probe packet-number**]命令用恢复缺省情况。

【命令】

**[probe packet-number ***packet-number*****]

**[undo probe packet-number**]

【缺省情况】

一次UDP-jitter或Path-jitter探测中发送10个探测报文；一次Voice探测中发送1000个探测报文。

【视图】

Path-jitter/UDP-jitter/Voice测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[packet-number*]：一次探测中发送探测报文的个数，对于UDP-jitter和Path-jitter测试，取值范围为10～1000；对于Voice测试，取值范围为10～60000。

【举例】

\# 配置一次UDP-jitter探测中发送100个探测报文。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type udp-jitter

Sysname-nqa-admin-test-udp-jitter probe packet-number 100

**NQA \-- NQA客户端配置命令 \-- probe packet-timeout**

------------------------------------------------------------------------

**[probe packet-timeout**]命令用来配置一次探测中等待响应报文的超时时间。

**[undo probe packet-timeout**]命令用来恢复缺省情况。

【命令】

**[probe packet-timeout*** packet-timeout*]

**[undo probe packet-timeout**]

【缺省情况】

UDP-jitter和Path-jitter测试中等待响应报文的超时时间为3000毫秒；Voice测试中等待响应报文的超时时间为5000毫秒。

【视图】

Path-jitter/UDP-jitter/Voice测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[packet-timeout*]：一次探测中等待响应报文的超时时间，取值范围为10～3600000，单位为毫秒。

【举例】

\# 配置UDP-jitter测试中等待响应报文的超时时间为100毫秒。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type udp-jitter

Sysname-nqa-admin-test-udp-jitter probe packet-timeout 100

**NQA \-- NQA客户端配置命令 \-- probe timeout**

------------------------------------------------------------------------

**[probe timeout**]命令用来配置探测的超时时间。

**[undo probe timeout**]命令用来恢复缺省情况。

【命令】

**[probe timeout** *timeout*]

**[undo probe timeout**]

【缺省情况】

探测的超时时间为3000毫秒。

【视图】

DHCP/DNS/DLSw/FTP/HTTP/ICMP-echo/SNMP/TCP/UDP-echo/UDP-tracert测试类型视图

任意类型的NQA模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[timeout*]：一次探测的超时时间，单位为毫秒。在FTP、HTTP探测中，取值范围为10～86400000；在DHCP、DNS、DLSw、ICMP-echo、SNMP、TCP、UDP-echo和UDP-tracert探测中，取值范围为10～3600000。

【使用指导】

如果NQA探测没有在**probe timeout**命令指定的时间内完成，则认为本次探测超时。

【举例】

\# 配置DHCP探测的超时时间为10000毫秒。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type dhcp

Sysname-nqa-admin-test-dhcp probe timeout 10000

\# 在HTTP类型的NQA模板视图下，配置探测的超时时间为10000毫秒。

\<Sysname\> system-view

Sysname nqa template http httptplt

Sysname-nqatplt-http-httptplt probe timeout 10000

**NQA \-- NQA客户端配置命令 \-- raw-request**

------------------------------------------------------------------------

**[raw-request**]命令用来进入raw-request子视图，并在该子视图下配置HTTP测试请求报文内容。

**[undo** **raw-request**]命令用来删除配置的HTTP测试请求报文内容。

【命令】

**[raw-request**]

**[undo** **raw-request**]

【缺省情况】

没有配置报文内容。

【视图】

HTTP测试类型视图

HTTP类型的NQA模板视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

每次使用**raw-request**命令进入raw-request子视图时，之前在该子视图下配置的HTTP测试请求报文内容会被清除。

【举例】

\# 进入raw-request子视图，并在该子视图下配置HTTP测试请求报文的内容。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type http

Sysname-nqa-admin-test-http raw-request

Sysname-nqa-admin-test-http-raw-request

\# 在HTTP类型的NQA模板视图下，进入raw-request子视图，并在该子视图下配置HTTP测试请求报文的内容。

\<Sysname\> system-view

Sysname nqa template http httptplt

Sysname-nqatplt-http-httptplt raw-request

Sysname-nqatplt-http-httptplt-raw-request

**NQA \-- NQA客户端配置命令 \-- reaction checked-element icpif**

------------------------------------------------------------------------

**[reaction checked-element icpif**]命令用来创建监测Voice测试ICPIF值的阈值告警组。

**[undo reaction**]命令用来删除指定的阈值告警组。

【命令】

**[reaction** *item-number* **checked-element**]**icpif threshold-value***upper-threshold lower-threshold*[ [ **action-type** { **none** \| **trap-only** } ]]

**[undo reaction ***item-number*]

【缺省情况】

未创建监测Voice测试ICPIF值的阈值告警组。

【视图】

Voice测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[item-number*]：阈值告警组编号，取值范围为1～10。

**[threshold-value**]：指定阈值范围。

*[upper-threshold*]：阈值上限，取值范围为1～100。

*[lower-threshold*]：阈值下限，取值范围为1～100，且必须小于等于阈值上限。

**[action-type**]：触发的动作类型，缺省动作类型为**none**。

**[none**]：只在显示信息中记录监测结果，不向网管发送Trap消息。

**[trap-only**]：条件满足时，在显示信息中记录监测结果的同时，向网管发送Trap消息。

【使用指导】

阈值告警组创建后，不能再通过**reaction**命令修改该阈值告警组的内容。若要修改阈值告警组的内容，则需要先通过**undo reaction**命令用来删除阈值告警组，再利用新的参数创建阈值告警组。

【举例】

\# 创建编号为1的阈值告警组，监测每次Voice测试的ICPIF值，阈值上限为50，下限为5。NQA测试组启动前，初始的阈值状态为invalid。每次测试结束后，检查本次测试的ICPIF值，若超出阈值范围，阈值状态置为over-threshold；反之，置为below-threshold。当阈值状态改变时，向网管发送Trap消息。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type voice

Sysname-nqa-admin-test-voice reaction 1 checked-element icpif threshold-value 50 5 action-type trap-only

**NQA \-- NQA客户端配置命令 \-- reaction checked-element { jitter-ds \| jitter-sd }**

------------------------------------------------------------------------

**[reaction checked-element **[{ **jitter-ds** \| **jitter-sd** }]]命令用来创建监测单向时延抖动的阈值告警组。

**[undo reaction**]命令用来删除指定的阈值告警组。

【命令】

**[reaction** *item-number* **checked-element** { **jitter-ds** \| **jitter-sd** } ]**threshold-type **[{ **accumulate** *accumulate-occurrences* \| **average** } **threshold-value** *upper-threshold lower-threshold* [ **action-type** { **none** \| **trap-only** } ]]

**[undo reaction ***item-number*]

【缺省情况】

未创建监测单向时延抖动的阈值告警组。

【视图】

UDP-jitter/Voice测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[item-number*]：阈值告警组编号，取值范围为1～10。

**[jitter-ds**]：监测从目的到源的单向时延抖动。

**[jitter-sd**]：监测从源到目的的单向时延抖动。

**[threshold-type**]：指定阈值类型。

**[accumulate** *accumulate-occurrences*]：每次测试中，累计的单向时延抖动超出阈值的报文个数。对于UDP-jitter测试，取值为1～14999；对于Voice测试，取值范围为1～59999。

**[average**]：每次测试中，单向时延抖动的平均值。

**[threshold-value**]：指定阈值范围。

*[upper-threshold*]：阈值上限，取值范围为0～3600000，单位为毫秒。

*[lower-threshold*]：阈值下限，取值范围为0～3600000，且必须小于等于阈值上限，单位为毫秒。

**[action-type**]：触发的动作类型，缺省动作类型为**none**。

**[none**]：只在显示信息中记录监测结果，不向网管发送Trap消息。

**[trap-only**]：条件满足时，在显示信息中记录监测结果的同时，向网管发送Trap消息。

【使用指导】

·阈值告警组创建后，不能再通过**reaction**命令修改该阈值告警组的内容。若要修改阈值告警组的内容，则需要先通过**undo reaction**命令用来删除阈值告警组，再利用新的参数创建阈值告警组。

·监测的对象是探测成功的报文，探测失败的报文不参与计数。

【举例】

\# 创建编号为1的阈值告警组，监测UDP-jitter探测报文的从目的到源的单向时延抖动，阈值上限为50毫秒，下限为5毫秒。NQA测试组启动前，初始的阈值状态为invalid。每次测试结束后，检查本次测试的平均单向时延抖动，若超出阈值，阈值状态置为over-threshold；反之，置为below-threshold。当阈值状态改变时，向网管发送Trap消息。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type udp-jitter

Sysname-nqa-admin-test-udp-jitter reaction 1 checked-element jitter-ds threshold-type average threshold-value 50 5 action-type trap-only

\# 创建编号为2的阈值告警组，监测UDP-jitter探测报文的从目的到源的单向时延抖动，阈值上限为50毫秒，下限为5毫秒。NQA测试组启动前，初始的阈值状态为invalid。每次测试结束后，检查本次测试中累计的单向时延抖动超出阈值的报文个数，若达到或超过100个，阈值状态置为over-threshold；反之，置为below-threshold。当阈值状态改变时，向网管发送Trap消息。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type udp-jitter

Sysname-nqa-admin-test-udp-jitter reaction 2 checked-element jitter-ds threshold-type accumulate 100 threshold-value 50 5 action-type trap-only

**NQA \-- NQA客户端配置命令 \-- reaction checked-element mos**

------------------------------------------------------------------------

**[reaction checked-element mos**]命令用来创建监测Voice测试MOS值的阈值告警组。

**[undo reaction**]命令用来删除指定的阈值告警组。

【命令】

**[reaction** *item-number* **checked-element**]**mos threshold-value***upper-threshold lower-threshold*[ [ **action-type** { **none** \| **trap-only** } ]]

**[undo reaction ***item-number*]

【缺省情况】

未创建监测Voice测试MOS值的阈值告警组。

【视图】

Voice测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[item-number*]：阈值告警组的编号，取值范围为1～10。

**[threshold-value**]：指定阈值范围。

*[upper-threshold*]：阈值上限，取值范围为1～500。

*[lower-threshold*]：阈值下限，取值范围为1～500，且必须小于等于阈值上限。

**[action-type**]：触发的动作类型，缺省动作类型为**none**。

**[none**]：只在显示信息中记录监测结果，不向网管发送Trap消息。

**[trap-only**]：条件满足时，在显示信息中记录监测结果的同时，向网管发送Trap消息。

【使用指导】

·实际的阈值下限（或阈值上限）为输入的阈值下限/100（或阈值上限/100），即如果输入的阈值下限和阈值上限分别为100、200，则MOS值在1～2之间时，未超出阈值。

·阈值告警组创建后，不能再通过**reaction**命令修改该阈值告警组的内容。若要修改阈值告警组的内容，则需要先通过**undo reaction**命令用来删除阈值告警组，再利用新的参数创建阈值告警组。

【举例】

\# 创建编号为1的阈值告警组，监测每次Voice测试的MOS值，阈值上限为200，下限为100。NQA测试组启动前，初始的阈值状态为invalid。每次测试结束后，检查本次测试的MOS值，若超出阈值范围，阈值状态置为over-threshold；反之，置为below-threshold。当阈值状态改变时，向网管发送Trap消息。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type voice

Sysname-nqa-admin-test-voice reaction 1 checked-element mos threshold-value 200 100 action-type trap-only

**NQA \-- NQA客户端配置命令 \-- reaction checked-element { owd-ds \| owd-sd }**

------------------------------------------------------------------------

**[reaction checked-element **[{ **owd-ds** \| **owd-sd** }]]命令用来创建监测单向时延的阈值告警组。

**[undo reaction**]命令用来删除指定的阈值告警组。

【命令】

**[reaction** *item-number* **checked-element** { **owd-ds** \| **owd-sd** } ]**threshold-value ***upper-threshold lower-threshold*

**[undo reaction ***item-number*]

【缺省情况】

未创建监测单向时延的阈值告警组。

【视图】

UDP-jitter/Voice测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[item-number*]：阈值告警组编号，取值范围为1～10。

**[owd-ds**]：监测每个探测报文的从目的到源的单向时延。

**[owd-sd**]：监测每个探测报文的从源到目的的单向时延。

**[threshold-value**]：指定阈值范围。

*[upper-threshold*]：阈值上限，取值范围为0～3600000，单位为毫秒。

*[lower-threshold*]：阈值下限，取值范围为0～3600000，且必须小于等于阈值上限，单位为毫秒。

【使用指导】

·阈值告警组创建后，不能再通过**reaction**命令修改该阈值告警组的内容。若要修改阈值告警组的内容，则需要先通过**undo reaction**命令用来删除阈值告警组，再利用新的参数创建阈值告警组。

·监测的对象是探测成功的报文，探测失败的报文不参与计数。

·监测单向时延的阈值告警组不支持触发动作，但可以通过相关显示命令**display nqa reaction counters**和**display nqa statistics**显示当前的监测结果。

【举例】

\# 创建编号为1的阈值告警组，监测每个UDP-jitter探测报文的从目的到源的单向时延，阈值上限为50毫秒，下限为5毫秒。NQA测试组启动前，初始的阈值状态为invalid。收到探测报文的应答报文后，计算该探测报文从目的到源的单向时延，若超出阈值范围，阈值状态置为over-threshold；反之，置为below-threshold。。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type udp-jitter

Sysname-nqa-admin-test-udp-jitter reaction 1 checked-element owd-ds threshold-value 50 5

**NQA \-- NQA客户端配置命令 \-- reaction checked-element packet-loss**

------------------------------------------------------------------------

**[reaction checked-element packet-loss**]命令用来创建监测每次测试中丢包数的阈值告警组。

**[undo reaction **]命令用来删除指定的阈值告警组。

【命令】

**[reaction** *item-number* **checked-element**]**packet-loss threshold-type** **accumulate*******accumulate-occurrences *[[ **action-type** { **none** \| **trap-only** } ]]

**[undo reaction ***item-number*]

【缺省情况】

未创建监测每次测试中丢包数的阈值告警组。

【视图】

UDP-jitter/Voice测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[item-number*]：阈值告警组的编号，取值范围为1～10。

**[threshold-type**]：指定阈值类型。

**[accumulate** *accumulate-occurrences*]：每次测试中，累计的丢包数。对于UDP-jitter测试，取值范围为1～15000；对于Voice测试，取值范围为1～60000。

**[action-type**]：触发的动作类型，缺省动作类型为**none**。

**[none**]：只在显示信息中记录监测结果，不向网管发送Trap消息。

**[trap-only**]：条件满足时，在显示信息中记录监测结果的同时，向网管发送Trap消息。

【使用指导】

阈值告警组创建后，不能再通过**reaction**命令修改该阈值告警组的内容。若要修改阈值告警组的内容，则需要先通过**undo reaction**命令用来删除阈值告警组，再利用新的参数创建阈值告警组。

【举例】

\# 创建编号为1的阈值告警组，监测每次UDP-jitter测试的丢包数。NQA测试组启动前，初始的阈值状态为invalid。每次测试结束后，检查本次测试中累计的丢包数，若达到或超过100个，阈值状态置为over-threshold；反之，置为below-threshold。当阈值状态改变时，向网管发送Trap消息。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type udp-jitter

Sysname-nqa-admin-test-udp-jitter reaction 1 checked-element packet-loss threshold-type accumulate 100 action-type trap-only

**NQA \-- NQA客户端配置命令 \-- reaction checked-element probe-duration**

------------------------------------------------------------------------

**[reaction checked-element probe-duration**]命令用来创建监测探测持续时间的阈值告警组。

**[undo reaction**]命令用来删除指定的阈值告警组。

【命令】

**[reaction** *item-number* **checked-element**]**probe-duration threshold-type **[{ **accumulate** *accumulate-occurrences* \| **average** \| **consecutive** *consecutive-occurrences* } **threshold-value** *upper-threshold lower-threshold* [ **action-type** { **none** \| **trap-only** } ]]

**[undo reaction ***item-number*]

【缺省情况】

未创建监测探测持续时间的阈值告警组。

【视图】

DHCP/DLSw/DNS/FTP/HTTP/ICMP-echo/SNMP/TCP/UDP-echo测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[item-number*]：阈值告警组的编号，取值范围为1～10。

**[threshold-type**]：指定阈值类型。

**[accumulate** *accumulate-occurrences*]：每次测试中，累计的探测持续时间超出阈值的探测次数。*accumulate-occurrences*取值范围为1～15。

**[average**]：每次测试中，探测持续时间的平均值。

**[consecutive** *consecutive-occurrences*]：测试组启动后，连续的探测持续时间超出阈值的探测次数。*consecutive-occurrences*取值范围为1～16。

**[threshold-value**]：指定阈值范围。

*[upper-threshold*]：阈值上限，取值范围为0～3600000，单位为毫秒。

*[lower-threshold*]：阈值下限，取值范围为0～3600000，且必须小于等于阈值上限，单位为毫秒。

**[action-type**]：触发的动作类型，缺省动作类型为**none**。

**[none**]：只在显示信息中记录监测结果，不向网管发送Trap消息。

**[trap-only**]：条件满足时，在显示信息中记录监测结果的同时，向网管发送Trap消息。DNS测试不支持发送Trap，DNS测试类型视图下无此参数。

【使用指导】

·阈值告警组创建后，不能再通过**reaction**命令修改该阈值告警组的内容。若要修改阈值告警组的内容，则需要先通过**undo reaction**命令用来删除阈值告警组，再利用新的参数创建阈值告警组。

·监测的对象是成功的探测，失败的探测不参与计数。

【举例】

\# 创建编号为1的阈值告警组，监测ICMP-echo探测的持续时间，阈值上限为50毫秒，下限为5毫秒。NQA测试组启动前，初始的阈值状态为invalid。每次测试结束后，检查本次测试的平均探测持续时间，若超出阈值，阈值状态置为over-threshold；反之，置为below-threshold。当阈值状态改变时，向网管发送Trap消息。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type icmp-echo

Sysname-nqa-admin-test-icmp-echo reaction 1 checked-element probe-duration threshold-type average threshold-value 50 5 action-type trap-only

\# 创建编号为2的阈值告警组，监测ICMP-echo探测的持续时间，阈值上限为50毫秒，下限为5毫秒。NQA测试组启动前，初始的阈值状态为invalid。每次测试结束后，检查本次测试中累计的持续时间超出阈值的探测次数，若达到或超过10次，阈值状态置为over-threshold；反之，置为below-threshold。当阈值状态改变时，向网管发送Trap消息。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type icmp-echo

Sysname-nqa-admin-test-icmp-echo reaction 2 checked-element probe-duration threshold-type accumulate 10 threshold-value 50 5 action-type trap-only

\# 创建编号为3的阈值告警组，监测ICMP-echo探测的持续时间，阈值上限为50毫秒，下限为5毫秒。NQA测试组启动前，初始的阈值状态为invalid。每次探测结束后，检查测试组启动以来连续的持续时间超出阈值的探测次数，若达到或超过10次，阈值状态置为over-threshold；反之，置为below-threshold。当阈值状态改变时，向网管发送Trap消息。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type icmp-echo

Sysname-nqa-admin-test-icmp-echo reaction 3 checked-element probe-duration threshold-type consecutive 10 threshold-value 50 5 action-type trap-only

**NQA \-- NQA客户端配置命令 \-- reaction checked-element probe-fail (for trap)**

------------------------------------------------------------------------

**[reaction checked-element probe-fail**]命令用来创建监测探测失败次数的阈值告警组。

**[undo reaction**]命令用来删除指定的阈值告警组。

【命令】

**[reaction**[ *item-number* **checked-element** **probe-fail** **threshold-type** { **accumulate** *accumulate-occurrences* \| **consecutive** *consecutive-occurrences* } [ **action-type** { **none** \| **trap-only** } ]]]

**[undo reaction ***item-number*]

【缺省情况】

未创建监测探测失败次数的阈值告警组。

【视图】

DHCP/DLSw/DNS/FTP/HTTP/ICMP-echo/SNMP/TCP/UDP-echo测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[item-number*]：阈值告警组编号，取值范围为1～10。

**[threshold-type**]：指定阈值类型。

**[accumulate** *accumulate-occurrences*]：一次测试中，累计的探测失败次数。*accumulate-occurrences*取值范围为1～15。

**[consecutive** *consecutive-occurrences*]：NQA测试组启动以来，连续的探测失败次数。*consecutive-occurrences*取值范围为1～16。

**[action-type**]：触发的动作类型，缺省动作类型为**none**。

**[none**]：只在显示信息中记录监测结果，不向网管发送Trap消息。

**[trap-only**]：条件满足时，在显示信息中记录监测结果的同时，向网管发送Trap消息。DNS测试不支持发送trap，DNS测试类型视图下无此参数。

【使用指导】

阈值告警组创建后，不能再通过**reaction**命令修改该阈值告警组的内容。若要修改阈值告警组的内容，则需要先通过**undo reaction**命令用来删除阈值告警组，再利用新的参数创建阈值告警组。

【举例】

\# 创建编号为1的阈值告警组，监测ICMP-echo探测的失败次数。NQA测试组启动前，初始的阈值状态为invalid。每次测试结束后，检查本次测试中累计的探测失败次数，若达到或超过10次，阈值状态置为over-threshold；反之，置为below-threshold。当阈值状态改变时，向网管发送Trap消息。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type icmp-echo

Sysname-nqa-admin-test-icmp-echo reaction 1 checked-element probe-fail threshold-type accumulate 10 action-type trap-only

\# 创建编号为2的阈值告警组，监测ICMP-echo探测的失败次数。NQA测试组启动前，初始的阈值状态为invalid。每次探测结束后，检查测试组启动以来连续的探测失败次数，若达到或超过10次，阈值状态置为over-threshold；反之，置为below-threshold。当阈值状态改变时，向网管发送Trap消息。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type icmp-echo

Sysname-nqa-admin-test-icmp-echo reaction 2 checked-element probe-fail threshold-type consecutive 10 action-type trap-only

**NQA \-- NQA客户端配置命令 \-- reaction checked-element probe-fail (for trigger)**

------------------------------------------------------------------------

**[reaction checked-element probe-fail**]命令用来建立联动项，对当前所在测试组中的探测进行监测，当连续探测失败次数达到阈值时，就触发其他模块联动。

**[undo reaction**]命令用来删除指定的联动项。

【命令】

**[reaction** *item-number* **checked-element**]**probe-fail threshold-typeconsecutive***consecutive-occurrences* **action-type** **trigger-only**

**[undo reaction ***item-number*]

【缺省情况】

未配置联动项。

【视图】

DHCP/DLSw/DNS/FTP/HTTP/ICMP-echo/SNMP/TCP/UDP-echo测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[item-number*]：联动项序号，取值范围为1～10。

**[threshold-type**]：指定门限类型。

**[consecutive** *consecutive-occurrences*]：NQA测试组启动以来，连续的探测失败次数。*consecutive-occurrences*取值范围为1～16。

**[action-type**]：触发的动作类型。

**[trigger-only**]：条件满足时，触发其它模块联动。

【使用指导】

联动项创建后，不能再通过**reaction**命令修改该联动项的内容。若要修改联动项的内容，则需要先通过**undo reaction**命令用来删除联动项，再利用新的参数创建联动项。

【举例】

\# 建立序号为1的联动项，连续探测失败3次，触发其他模块联动。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type tcp

Sysname-nqa-admin-test-tcp reaction 1 checked-element probe-fail threshold-type consecutive 3 action-type trigger-only

【相关命令】

·**track**（可靠性命令参考/Track）

**NQA \-- NQA客户端配置命令 \-- reaction checked-element rtt**

------------------------------------------------------------------------

**[reaction checked-element rtt**]命令用来创建监测报文往返时延的阈值告警组。

**[undo reaction**]命令用来删除指定的阈值告警组。

【命令】

**[reaction** *item-number* **checked-element**]**rtt threshold-type **[{ **accumulate** *accumulate-occurrences* \| **average** } **threshold-value** *upper-threshold lower-threshold* [ **action-type** { **none** \| **trap-only** } ]]

**[undo reaction ***item-number*]

【缺省情况】

未创建监测报文往返时延的阈值告警组。

【视图】

UDP-jitter/Voice测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[item-number*]：阈值告警组编号，取值范围为1～10。

**[threshold-type**]：指定阈值类型。

**[accumulate** *accumulate-occurrences*]：每次测试中，累计的RTT超出阈值的报文个数。对于UDP-jitter测试，取值范围为1～15000；对于Voice测试，取值范围为1～60000。

**[average**]：每次测试中，报文往返时间的平均值。

**[threshold-value**]：指定阈值范围。

*[upper-threshold*]：阈值上限，取值范围为0～3600000，单位为毫秒。

*[lower-threshold*]：阈值下限，取值范围为0～3600000，且必须小于等于阈值上限，单位为毫秒。

**[action-type**]：触发的动作类型，缺省动作类型为**none**。

**[none**]：只在显示信息中记录监测结果，不向网管发送Trap消息。

**[trap-only**]：条件满足时，在显示信息中记录监测结果的同时，向网管发送Trap消息。

【使用指导】

·阈值告警组创建后，不能再通过**reaction**命令修改该阈值告警组的内容。若要修改阈值告警组的内容，则需要先通过**undo reaction**命令用来删除阈值告警组，再利用新的参数创建阈值告警组。

·监测的对象是探测成功的报文，探测失败的报文不参与计数。

【举例】

\# 创建编号为1的阈值告警组，监测UDP-jitter探测报文的往返时间，阈值上限为50毫秒，下限为5毫秒。NQA测试组启动前，初始的阈值状态为invalid。每次测试结束后，检查本次测试的平均报文往返时间，若超出阈值，阈值状态置为over-threshold；反之，置为below-threshold。当阈值状态改变时，向网管发送Trap消息。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type udp-jitter

Sysname-nqa-admin-test-udp-jitter reaction 1 checked-element rtt threshold-type average threshold-value 50 5 action-type trap-only

\# 创建编号为2的阈值告警组，监测每个UDP-jitter探测报文的往返时间，阈值上限为50毫秒，下限为5毫秒。NQA测试组启动前，初始的阈值状态为invalid。每次测试结束后，检查本次测试中累计的RTT超出阈值的报文个数，若达到或超过100个，阈值状态置为over-threshold；反之，置为below-threshold。当阈值状态改变时，向网管发送Trap消息。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type udp-jitter

Sysname-nqa-admin-test-udp-jitter reaction 1 checked-element rtt threshold-type accumulate 100 threshold-value 50 5 action-type trap-only

**NQA \-- NQA客户端配置命令 \-- reaction trap**

------------------------------------------------------------------------

**[reaction trap**]命令用来配置在指定条件下向网管服务器发送Trap消息。

**[undo reaction trap**]命令用来恢复缺省情况。

【命令】

**[reaction trap **[{ **path-change** \| **probe-failure** *consecutive-probe-failures* \| **test-complete** \| **test-failure** [ *cumulate-probe-failures* ] }]]

**[undo reaction trap **[{ **probe-failure** \| **test-complete** \| **test-failure** }]]

【缺省情况】

不向网管服务器发送Trap消息。

【视图】

DHCP/DLSw/DNS/FTP/HTTP/ICMP-echo/SNMP/TCP/UDP-echo/UDP-jitter/UDP-tracert/Voice测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[path-change**]：当进行UDP-tracert类型测试时，在配置了**frequency**命令后进行连续测试后，如果检测到当前路径相对于上一次测试路径发生变化，则设备发送一次Trap消息。

**[probe-failure ***consecutive-probe-failures*]：每次探测结束后，计算本次NQA测试中探测连续失败的次数，如果连续失败次数大于或等于*consecutive-probe-failures*，则向网管服务器发送探测失败的Trap消息。一次测试中，可能发送多次Trap消息。*consecutive-probe-failures*为一次测试中连续探测失败的次数，取值范围为1～15。

**[test-complete**]：对于非UDP-tracert类型测试，当测试完成时发送测试完成的Trap消息。对于UDP-tracert类型测试，测试出到达目的设备的路径后，发送测试完成的Trap消息。

**[test-failure** *cumulate-probe-failures*]：对于非UDP-tracert类型测试，一次NQA测试结束后，计算本次NQA测试中探测失败的累计次数，如果累计失败次数大于或等于*cumulate-probe-failures*，则向网管服务器发送测试失败的Trap消息。*cumulate-probe-failures*为一次测试中累计探测失败的次数，为必须输入的参数，取值范围为1～15。对于UDP-tracert类型测试，只要未能测试出到达目的地的路径，就发送一次Trap消息。用户不能输入参数*cumulate-probe-failures*。

【使用指导】

UDP-jitter 和Voice测试只支持**reaction trap test-complete**。

UDP-tracert测试支持**reaction trap path-change**，**reaction trap test-complete**和**reaction trap test-failure**。

【举例】

\# 配置ICMP-echo测试中连续探测失败次数大于或等于5次时，发送探测失败的Trap消息。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type icmp-echo

Sysname-nqa-admin-test-icmp-echo reaction trap probe-failure 5

**NQA \-- NQA客户端配置命令 \-- reaction trigger probe-fail**

------------------------------------------------------------------------

**[undo reaction trigger probe-fail**]命令****用来恢复缺省情况。

【命令】

**[reaction trigger probe-fail** *count*]

**[undo reaction trigger probe-fail**]

【缺省情况】

【视图】

任意类型的NQA模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[count*]*：*连续探测失败的次数，取值范围为1～15。

【使用指导】

外部特性调用NQA模板后进行相应的NQA测试，使用此命令可以设定节点失效的连续测试失败次数。

【举例】

\# 在HTTP类型的NQA模板视图下，配置确定节点失效需要连续探测失败5次。当连续探测失败的次数达到5次时，NQA客户端把探测失败的消息发送给外部特性，使外部特性能利用NQA测试的结果进行相应处理。

\<Sysname\> system-view

Sysname nqa template http httptplt

Sysname-nqatplt-http-httptplt reaction trigger probe-fail 5

**NQA \-- NQA客户端配置命令 \-- reaction trigger probe-pass**

------------------------------------------------------------------------

**[undo reaction trigger probe-pass**]命令用来恢复缺省情况。

【命令】

**[reaction trigger probe-pass** *count*]

**[undo reaction trigger probe-pass**]

【缺省情况】

【视图】

任意类型的NQA模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[count*]*：*连续探测成功的次数，取值范围为1～15。

【使用指导】

外部特性调用NQA模板后进行相应的NQA测试，使用此命令可以设定节点有效的连续探测成功次数。

【举例】

\# 在HTTP类型的NQA模板视图下，配置确定节点有效需要连续探测成功5次。当连续探测成功的次数达到5次时，NQA客户端把探测成功的消息发送给外部特性，使外部特性能利用NQA测试的结果进行相应处理。

\<Sysname\> system-view

Sysname nqa template http httptplt

Sysname-nqatplt-http-httptplt reaction trigger probe-pass 5

**NQA \-- NQA客户端配置命令 \-- resolve-target**

------------------------------------------------------------------------

**[resolve-target**]命令用来配置要解析的域名。

**[undo resolve-target**]命令用来恢复缺省情况。

【命令】

**[resolve-target ***domain-name*]

**[undo resolve-target**]

【缺省情况】

没有配置要解析的域名。

【视图】

DNS测试类型视图

DNS类型的NQA模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[domain-name*]：要解析的域名，由"."分隔的字符串组成（如aabbcc.com），每个字符串的长度不超过63个字符，包括"."在内的总长度不超过255个字符，区分大小写。字符串中可以包含字母、数字、"-"及"\_"，不能出现连续"."。

【举例】

\# 配置DNS测试要解析的域名为domain1。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type dns

Sysname-nqa-admin-test-dns resolve-target domain1

\# 在DNS类型的NQA模板视图下，配置测试要解析的域名为domain1。

\<Sysname\> system-view

Sysname nqa template dns dnstplt

Sysname-nqatplt-dns-dnstplt resolve-target domain1

**NQA \-- NQA客户端配置命令 \-- resolve-type**

------------------------------------------------------------------------

**[resolve-type**]命令用来配置域名解析类型。

**[undo resolve-type**]命令用来恢复缺省情况。

【命令】

**[resolve-type **[{ **A** \| **AAAA** }]]

**[undo resolve-type**]

【缺省情况】

域名解析类型为**A**类型。

【视图】

DNS类型的NQA模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

【举例】

\# 在DNS类型的NQA模板视图下，配置测试的域名解析类型为**AAAA**。

\<Sysname\> system-view

Sysname nqa template dns dnstplt

Sysname-nqatplt-dns-dnstplt resolve-type AAAA

**NQA \-- NQA客户端配置命令 \-- route-option bypass-route**

------------------------------------------------------------------------

**[route-option bypass-route**]命令用来启动路由表旁路功能，探测直连目的地的连通情况。

**[undo** **route-option bypass-route**]命令用来关闭路由表旁路功能。

【命令】

**[route-option bypass-route**]

**[undo route-option bypass-route**]

【缺省情况】

路由表旁路功能处于关闭状态。

【视图】

DLSw/DNS/FTP/HTTP/ICMP-echo/SNMP/TCP/UDP-echo/UDP-jitter/UDP-tracert/Voice测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

启动该功能后，将不进行路由查找，而直接将报文发送到直连网络的目的地。

在设备上启动该功能后，设备转发探测报文可以经过的最大跳数为1，**ttl**命令设置的跳数不会生效。

【举例】

\# 启动路由旁路功能。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type icmp-echo

Sysname-nqa-admin-test-icmp-echo route-option bypass-route

**NQA \-- NQA客户端配置命令 \-- source interface**

------------------------------------------------------------------------

**[source interface**]命令用来使用指定接口的IP地址作为测试中探测报文的源IP地址。

**[undo source interface**]命令用来恢复缺省情况。

【命令】

**[source interface** *interface-type interface-number*]

**[undo source interface**]

【缺省情况】

未指定测试中探测报文的源IP地址，以报文发送接口的主IP地址作为探测报文中的源IP地址。

【视图】

ICMP-echo/UDP-tracert测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type interface-number*]：探测报文源接口的接口类型和接口编号。

【使用指导】

·**source ip**命令或**source ipv6**命令和**source interface**命令是互相覆盖的关系，新的配置会覆盖已有配置。

·该命令指定的接口必须处于UP状态，否则探测将会失败。

【举例】

·路由应用

\# 指定接口GigabitEthernet1/0/1的IP地址作为ICMP-echo探测报文的源IP地址。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type icmp-echo

Sysname-nqa-admin-test-icmp-echo source interface gigabitethernet 1/0/1

\# 在ICMP类型的NQA模板视图下，指定接口GigabitEthernet1/0/1的IP地址作为ICMP-echo探测报文的源IP地址。

\<Sysname\> system-view

Sysname nqa template icmp icmptplt

Sysname-nqatplt-icmp-icmptplt source interface gigabitethernet 1/0/1

·交换应用

\# 指定VLAN接口2的IP地址作为ICMP-echo探测报文的源IP地址。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type icmp-echo

Sysname-nqa-admin-test-icmp-echo source interface vlan-interface 2

\# 在ICMP类型的NQA模板视图下，指定VLAN接口2的IP地址作为ICMP-echo探测报文的源IP地址。

\<Sysname\> system-view

Sysname nqa template icmp icmptplt

Sysname-nqatplt-icmp-icmptplt source interface vlan-interface 2

【相关命令】

·**source ip**

**NQA \-- NQA客户端配置命令 \-- source ip**

------------------------------------------------------------------------

**[source ip**]命令用来配置测试操作中探测报文的源IP地址。

**[undo source ip**]命令用来取消已配置的源IP地址，即以报文发送接口的IP地址作为探测报文中的源IP地址。

【命令】

**[source ip ***ip-address*]

**[undo** **source ip**]

【缺省情况】

未配置测试操作中探测报文的源IP地址。

【视图】

DLSw/FTP/HTTP/ICMP-echo/Path-jitter/SNMP/TCP/UDP-echo/DHCP/UDP-jitter/UDP-tracert/Voice测试类型视图

任意类型的NQA模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：测试操作中探测报文的源IP地址。

【使用指导】

·对于ICMP-echo/UDP-tracert测试类型，**source ip**命令和**source interface**命令是互相覆盖的关系，新的配置会覆盖已有配置。

·**source ip**命令配置的源IP地址必须是设备上接口的IP地址，且接口为UP状态，否则测试将会失败。

·对于NQA模板类型来说，当源地址类型和目的地址类型不一致时，以目的地址类型为准，进行该类型的报文探测，此时源地址的配置不生效。

【举例】

\# 配置ICMP-echo探测报文中的源IP地址为10.1.1.1。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type icmp-echo

Sysname-nqa-admin-test-icmp-echo source ip 10.1.1.1

\# 在ICMP类型的NQA模板视图下，配置探测报文中的源IP地址为10.1.1.1。

\<Sysname\> system-view

Sysname nqa template icmp icmptplt

Sysname-nqatplt-icmp-icmptplt source ip 10.1.1.1

【相关命令】

·**source interface**

**NQA \-- NQA客户端配置命令 \-- source ipv6**

------------------------------------------------------------------------

**[source ipv6**]命令用来配置测试操作中探测报文的源IPv6地址。

**[undo source ipv6**]命令用来取消已配置的源IPv6地址，即以报文发送接口的IPv6地址作为探测报文中的源IPv6地址。

【命令】

**[source ipv6 ***ipv6-address*]

**[undo** **source ipv6**]

【缺省情况】

未配置测试操作中探测报文的源IPv6地址。

【视图】

任意类型的NQA模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：测试操作中探测报文的源IPv6地址，不支持IPv6链路本地地址。

【使用指导】

·对于ICMP-echo测试类型，**source ipv6**命令和**source interface**命令是互相覆盖的关系，新的配置会覆盖已有配置。

·**source ipv6**命令配置的源IPv6地址必须是设备上接口的IPv6地址，且接口为up状态，否则测试将会失败。

·对于NQA模板类型来说，当源地址类型和目的地址类型不一致时，以目的地址类型为准，进行该类型的报文探测，此时源地址的配置不生效。

【举例】

\# 在ICMP类型的NQA模板视图下，配置探测报文中的源IPv6地址为1::1。

\<Sysname\> system-view

Sysname nqa template icmp icmptplt

Sysname-nqatplt-icmp-icmptplt source ipv6 1::1

【相关命令】

·**source interface**

**NQA \-- NQA客户端配置命令 \-- source port**

------------------------------------------------------------------------

**[source port**]命令用来配置测试操作中探测报文的源端口号。

**[undo source port**]命令用来取消已配置的源端口号。

【命令】

**[source port **]*port-number*

**[undo**] **source port**

【缺省情况】

未指定源端口号。

【视图】

SNMP/UDP-echo/UDP-jitter/UDP-tracert/Voice测试类型视图

DNS类型的NQA模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-number*]：探测报文的源端口号，取值范围为1～65535。

【举例】

\# 配置探测报文的源端口号为8000。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type udp-echo

Sysname-nqa-admin-test-udp-echo source port 8000

\# 在DNS类型的NQA模板视图下，配置探测报文的源端口号为8000。

\<Sysname\> system-view

Sysname nqa template dns dnstplt

Sysname-nqatplt-dns-dnstplt source port 8000

**NQA \-- NQA客户端配置命令 \-- statistics hold-time**

------------------------------------------------------------------------

**[statistics hold-time**]命令用来配置统计组的保留时间。

**[undo statistics hold-time**]命令用来恢复缺省情况。

【命令】

**[statistics hold-time ***hold-time*]

**[undo statistics hold-time**]

【缺省情况】

统计组的保留时间为120分钟。

【视图】

DHCP/DLSw/DNS/FTP/HTTP/ICMP-echo/Path-jitter/SNMP/TCP/UDP-echo/UDP-jitter/Voice测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[hold-time*]：统计组的保留时间，取值范围为1～1440，单位为分钟。

【使用指导】

统计组具有老化功能。统计组保存一定时间后将被删除，以便记录新的统计组信息。

【举例】

\# 配置统计组的保留时间为3分钟。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type icmp-echo

Sysname-nqa-admin-test-icmp-echo statistics hold-time 3

**NQA \-- NQA客户端配置命令 \-- statistics interval**

------------------------------------------------------------------------

**[statistics interval**]命令用来配置对测试结果进行统计的时间间隔。

**[undo statistics interval**]命令用来恢复缺省情况。

【命令】

**[statistics interval ***interval*]

**[undo statistics interval**]

【缺省情况】

对测试结果进行统计的时间间隔为60分钟。

【视图】

DHCP/DLSw/DNS/FTP/HTTP/ICMP-echo/Path-jitter/SNMP/TCP/UDP-echo/UDP-jitter/Voice测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：对测试结果进行统计的时间间隔，取值范围为1～35791394，单位为分钟。

【使用指导】

NQA将统计时间间隔内完成的NQA测试归为一组，计算该组测试结果的统计值，这些统计值构成一个统计组。通过**display nqa statistics**命令可以显示该统计组的信息。

【举例】

\# 配置对测试结果进行统计的时间间隔为2分钟。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type icmp-echo

Sysname-nqa-admin-test-icmp-echo statistics interval 2

**NQA \-- NQA客户端配置命令 \-- statistics max-group**

------------------------------------------------------------------------

**[statistics max-group**]命令用来配置能够保留的最大统计组个数。

**[undo statistics max-group**]命令用来恢复缺省情况。

【命令】

**[statistics max-group ***number*]

**[undo statistics max-group**]

【缺省情况】

能够保留的最大统计组个数为2。

【视图】

DHCP/DLSw/DNS/FTP/HTTP/ICMP-echo/Path-jitter/SNMP/TCP/UDP-echo/UDP-jitter/Voice测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：能够保留的最大统计组个数，取值范围为0～100。

【使用指导】

当保留的统计组数目达到最大值时，如果形成新的统计组，保存时间最久的统计组将被删除。

需要注意的是，能够保留的最大统计组个数为0时，不进行统计。

【举例】

\# 配置能够保留的最大统计组个数为5。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type icmp-echo

Sysname-nqa-admin-test-icmp-echo statistics max-group 5

**NQA \-- NQA客户端配置命令 \-- target-only**

------------------------------------------------------------------------

**[target-only**]命令用来配置Path-jitter测试中仅针对到达目的地址的完整路径进行探测，不逐跳进行探测。

**[undo target-only**]命令用来恢复缺省情况。

【命令】

**[target-only**]

**[undo target-only**]

【缺省情况】

Path-jitter测试中会逐跳进行探测。

【视图】

Path-jitter测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 配置仅对目的地址探测。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type path-jitter

Sysname-nqa-admin-test- path-jitter target-only

**NQA \-- NQA客户端配置命令 \-- tos**

------------------------------------------------------------------------

**[tos**]命令用来配置NQA探测报文IP报文头中服务类型域的值。

**[undo tos**]命令用来恢复缺省情况。

【命令】

**[tos** *value*]

**[undo** **tos**]

【缺省情况】

NQA探测报文IP报文头中服务类型域的值为0。

【视图】

任意测试类型视图

任意类型的NQA模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：探测报文IP报文头中服务类型域的值，取值范围为0～255。

【举例】

\# 配置探测报文IP报文头中服务类型域的值为1。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type icmp-echo

Sysname-nqa-admin-test-icmp-echo tos 1

\# 在ICMP类型的NQA模板视图下，配置探测报文IP报文头中服务类型域的值为1。

\<Sysname\> system-view

Sysname nqa template icmp icmptplt

Sysname-nqatplt-icmp-icmptplt tos 1

**NQA \-- NQA客户端配置命令 \-- ttl**

------------------------------------------------------------------------

**[ttl**]命令用来配置探测报文在网络中可以经过的最大跳数。

**[undo ttl**]命令用来恢复缺省情况。

【命令】

**[ttl** *value*]

**[undo ttl**]

【缺省情况】

UDP-tracert类型测试报文在网络中可以经过的最大跳数是30跳。其它测试类型下探测报文在网络中可以经过的最大跳数为20跳。

【视图】

DLSw/DNS/FTP/HTTP/ICMP-echo/SNMP/TCP/UDP-echo/UDP-jitter/UDP-tracert/Voice测试类型视图

任意类型的NQA模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：UDP-tracert测试类型表示允许探测报文填充的最大跳数值，其它测试类型表示探测报文在网络中可以经过的最大跳数，取值范围1～255。

【使用指导】

配置**route-option bypass-route**命令后，探测报文在网络中可以经过的最大跳数为1，**ttl**命令不会生效。

配置UDP-tracert类型测试时，如果使用**init-ttl**命令配置的初始跳数值大于此值，测试将无法启动。

【举例】

\# 配置探测报文在网络中可以经过的最大跳数为16跳。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type icmp-echo

Sysname-nqa-admin-test-icmp-echo ttl 16

\# 在ICMP类型的NQA模板视图下，配置探测报文在网络中可以经过的最大跳数为16跳。

\<Sysname\> system-view

Sysname nqa template icmp icmptplt

Sysname-nqatplt-icmp-icmptplt ttl 16

**NQA \-- NQA客户端配置命令 \-- type**

------------------------------------------------------------------------

**[type**]命令用来配置当前测试组的测试类型，并进入测试组测试类型视图。

【命令】

**[type**[ { **dhcp** \| **dlsw** \| **dns** \| **ftp** \| **http** \| **icmp-echo** \| **path-jitter** \| **snmp** \| **tcp** \| **udp-echo** \| **udp-jitter** \| **udp-tracert** \| **voice** }]]

【缺省情况】

没有配置测试类型。

【视图】

NQA测试组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[dhcp**]：测试类型为DHCP。

**[dlsw**]：测试类型为DLSw。

**[dns**]：测试类型为DNS。

**[ftp**]：测试类型为FTP。

**[http**]：测试类型为HTTP。

**[icmp-echo**]：测试类型为ICMP-echo。

**[path-jitter**]：测试类型为Path-jitter。

**[snmp**]：测试类型为SNMP。

**[tcp**]：测试类型为TCP。

**[udp-echo**]：测试类型为UDP-echo。

**[udp-jitter**]：测试类型为UDP-jitter。

**[udp-tracert**]：测试类型为UDP-tracert。

**[voice**]：测试类型为Voice。

【举例】

\# 配置测试组的测试类型为FTP测试，并进入测试组测试类型视图。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type ftp

Sysname-nqa-admin-test-ftp

**NQA \-- NQA客户端配置命令 \-- url**

------------------------------------------------------------------------

**[url**]命令用来配置HTTP和FTP测试访问的网址。

**[undo url**]命令用来取消已配置的测试访问的网址。

【命令】

**[url ***url*]

**[undo url**]

【缺省情况】

没有配置HTTP和FTP测试访问的网址。

【视图】

FTP/HTTP测试类型视图

FTP/HTTP类型的NQA模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[url*]：测试操作访问的目标资源地址，为1～255个字符的字符串，区分大小写。*url*中不允许有字符?。*url*中的主机名部分，由"."分隔的字符串组成（如aabbcc.com），每个字符串的长度不超过63个字符，包括"."在内的总长度不超过255个字符，区分大小写；字符串中可以包含字母、数字、"-"及"\_"，不能出现连续"."。

·HTTP测试类型时，*url*格式为http://*host/resource*或http://*host*:*port*/*resource*。

·FTP测试类型时，*url*格式为ftp://*host*/*filename*或ftp://*host*:*port*/*filename*

*[filename*]取值范围的详细介绍，请参见"基础配置指导"中的"文件系统管理"。

【举例】

\# 配置HTTP测试访问的网址为http://www.company.com/index.html。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type http

Sysname-nqa-admin-test-http url http://www.company.com/index.html(http://www.company.com/index.html)

\# 在HTTP类型的NQA模板视图，配置测试访问的网址为http://www.company.com/index.html。

\<Sysname\> system-view

Sysname nqa template http httptplt

Sysname-nqatplt-http-httptplt url http://www.company.com/index.html(http://www.company.com/index.html)

**NQA \-- NQA客户端配置命令 \-- username**

------------------------------------------------------------------------

**[username**]命令用来配置FTP或HTTP登录用户名。

**[undo username**]命令用来取消已配置的登录用户名。

【命令】

**[username **]*username*

**[undo username**]

【缺省情况】

未配置FTP或HTTP登录用户名。

【视图】

FTP/HTTP测试类型视图

FTP/HTTP/RADIUS类型的NQA模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[username*]：测试使用的用户名，区分大小写。FTP或HTTP登录用户名，为1～32个字符的字符串，区分大小写；RADIUS用户名，为1～253个字符的字符串。

【举例】

\# 配置FTP登录用户名为administrator。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type ftp

Sysname-nqa-admin-test-ftp username administrator

\# 在FTP类型的NQA模板视图下，配置FTP登录用户名为administrator。

\<Sysname\> system-view

Sysname nqa template ftp ftptplt

Sysname-nqatplt-ftp-ftptplt username administrator

【相关命令】

·**operation**

·**password**

**NQA \-- NQA客户端配置命令 \-- version**

------------------------------------------------------------------------

**[version**]命令用来配置HTTP测试所使用的版本。

**[undo version**]命令用来恢复缺省情况。

【命令】

**[version ** { **v1.0** \| **v1.1** } ]

**[undo version**]

【缺省情况】

HTTP测试使用的版本为1.0。

【视图】

HTTP测试类型视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[v1.0**]：HTTP测试使用的版本为1.0。

**[v1**.1]：HTTP测试使用的版本为1.1。

【举例】

\# 配置HTTP测试使用的版本为1.1。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type http

Sysname-nqa-admin-test-http version v1.1

**NQA \-- NQA客户端配置命令 \-- vpn-instance**

------------------------------------------------------------------------

![说明](NQA命令.files/image001.png)

本命令的支持情况与设备的实际情况有关，请以设备的实际情况为准。

**[vpn-instance**]命令用来指定测试操作所属的VPN。

**[undo vpn-instance**]命令用来恢复缺省情况。

【命令】

**[vpn-instance ***vpn-instance-name*]

**[undo vpn-instance**]

【缺省情况】

未指定测试操作所属的VPN，NQA用来测试公网的连通性。

【视图】

任意测试类型视图

任意类型的NQA模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vpn-instance-name*]：MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。

【使用指导】

指定测试操作所属的VPN后，NQA将测试指定VPN内隧道的连通情况。

【举例】

\# 指定测试操作所属的VPN为vpn1。

\<Sysname\> system-view

Sysname nqa entry admin test

Sysname-nqa-admin-test type icmp-echo

Sysname-nqa-admin-test-icmp-echo vpn-instance vpn1

\# 在FTP类型的NQA模板视图下，指定测试操作所属的VPN为vpn1。

\<Sysname\> system-view

Sysname nqa template ftp ftptplt

Sysname-nqatplt-ftp-ftptplt vpn-instance vpn1

**NQA \-- NQA服务器端命令 \-- display nqa server**

------------------------------------------------------------------------

**[display nqa server**]命令用来显示服务器的状态信息。

【命令】

**[display nqa server**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示服务器的状态信息。

\<Sysname\> display nqa server

NQA server status: enabled

TCP connect:

   IP Address          Port      ToS    Vpn-instance

   2.2.2.2             2000      200    -

UDP echo:

   IP Address          Port      ToS    Vpn-instance

   3.3.3.3             3000      255    vpn1

表1-8 display nqa server status命令输出信息描述

字段

描述命令

NQA server status

NQA服务器状态，包括的取值如下：

·Disabled：未启用NQA服务器功能；

·Enabled：启用了NQA服务器功能；

tcp-connect

NQA TCP测试中服务器的状态信息

udp-echo

NQA UDP测试中服务器的状态信息

IP Address

NQA服务器TCP/UDP监听服务的IP地址

Port

NQA服务器TCP/UDP监听服务的端口号

ToS

NQA服务器TCP/UDP监听服务的回应报文携带的ToS值

Vpn-instance

NQA服务器的MPLS L3VPN的VPN实例名称

**NQA \-- NQA服务器端命令 \-- nqa server enable**

------------------------------------------------------------------------

**[nqa server enable**]命令用来开启NQA服务器功能。

**[undo nqa server enable**]命令用来关闭NQA服务器功能。

【命令】

**[nqa server enable**]

**[undo nqa server enable**]

【缺省情况】

NQA服务器功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 开启NQA服务器功能。

\<Sysname\> system-view

Sysname nqa server enable

【相关命令】

·**display nqa server**

·**nqa server tcp-connect**

·**nqa server udp-echo**

**NQA \-- NQA服务器端命令 \-- nqa server tcp-connect**

------------------------------------------------------------------------

**[nqa server tcp-connect**]命令用来在NQA服务器上创建TCP监听服务。

**[undo nqa server tcp-connect**]命令用来删除已建立的TCP监听服务。

【命令】

**[nqa server tcp-connect** *ip-address port-number* [ **vpn-instance** *vpn-instance-name*   **tos** *tos* ]]

**[undo nqa server tcp-connect** *ip-address port-number*]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：NQA服务器TCP监听服务的IP地址。

*[port-number*]：NQA服务器TCP监听服务的端口号，取值范围为1～65535。

**[vpn-instance*** vpn-instance-name*]：MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则表示TCP监听的是公网IP地址。

**[tos*** tos*]：NQA服务器应答报文中的ToS域的值。取值范围为0～255，缺省值为0。

【使用指导】

·只有在测试类型为TCP时，才需在NQA服务器上配置此命令。

·通过本命令可以指定发送应答NQA探测报文（TCP报文）中携带的ToS值。

·所配置的IP地址和端口号必须与NQA客户端的配置一致，且不能与已有的监听服务冲突。

·所配置的IP地址必须是作为服务器的设备上的接口的IP地址，否则配置无效。

·建议不要配置1～1023之间的端口（知名端口），否则可能导致NQA测试失败或该知名端口对应的服务不可用。

【举例】

\# 创建IP地址为169.254.10.2，端口号为9000的TCP监听服务。

\<Sysname\> system-view

Sysname nqa server tcp-connect 169.254.10.2 9000

【相关命令】

·**display nqa server**

·**nqa server enable**

**NQA \-- NQA服务器端命令 \-- nqa server udp-echo**

------------------------------------------------------------------------

**[nqa server udp-echo**]命令用来在NQA服务器上创建UDP监听服务。

**[undo nqa server udp-echo**]命令用来删除已建立的UDP监听服务。

【命令】

**[nqa server udp-echo** *ip-address port-number* [ **vpn-instance** *vpn-instance-name*   **tos** *tos* ]]

**[undo nqa server udp-echo** *ip-address port-number*]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：NQA服务器UDP监听服务的IP地址。

*[port-number*]：NQA服务器UDP监听服务的端口号，取值范围为1～65535。

**[vpn-instance*** vpn-instance-name*]：MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则表示UDP监听的是公网IP地址。

**[tos*** tos*]：NQA服务器应答报文中的ToS域的值。取值范围为0～255，缺省值为0。

【使用指导】

·只有在测试类型为UDP-jitter、UDP-echo或Voice时，才需在NQA服务器上配置此命令。

·通过本命令可以指定发送应答NQA探测报文（UDP报文）中携带的ToS值。

·配置的IP地址和端口号必须与NQA客户端的配置一致，且不能与已有的监听服务冲突。

·所配置的IP地址必须是作为服务器的设备上的接口的IP地址，否则配置无效。

·建议不要配置1～1023之间的端口（知名端口），否则可能导致NQA测试失败或该知名端口对应的服务不可用。

【举例】

\# 创建IP地址为169.254.10.2、端口号为9000的UDP监听服务。

\<Sysname\> system-view

Sysname nqa server udp-echo 169.254.10.2 9000

【相关命令】

·**display nqa server**

·**nqa server enable**
