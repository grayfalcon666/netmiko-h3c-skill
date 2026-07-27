<!-- CMD-INDEX
  debugging ntp-service               | 用户视图             | L6
  debugging sntp                      | 用户视图             | L568
-->

**NTP \-- NTP调试命令 \-- debugging ntp-service**

------------------------------------------------------------------------

【命令】

**[debugging ntp-service **[{ **acl** \| **adjustment** \| **all** \| **authentication** \| **event** \| **filter** \| **packet** \| **parameter** \| **refclock** \| **selection** \| **synchronization** \| **validity** }]]

**[undo debugging ntp-service **[{ **acl** \| **adjustment** \| **all** \| **authentication** \| **event** \| **filter** \| **packet** \| **parameter** \| **refclock** \| **selection** \| **synchronization** \| **validity** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[acl**]：表示NTP访问控制调试信息开关。

**[adjustment**]：表示NTP时钟调节调试信息开关。

**[all**]：表示NTP的所有调试信息开关。

**[authentication**]：表示NTP身份验证调试信息开关。

**[event**]：表示NTP事件调试信息开关。

**[filter**]：表示NTP时钟过滤调试信息开关。

**[packet**]：表示NTP报文调试信息开关。

**[parameter**]：表示NTP时钟参数调试信息开关。

**[refclock**]：表示NTP参考时钟调试信息开关。

**[selection**]：表示NTP时钟选择调试信息开关。

**[synchronization**]：表示NTP时间同步调试信息开关。

**[validity**]：表示NTP远程主机的身份验证调试信息开关。

【描述】

**[debugging ntp-service**]命令用来打开NTP的调试信息开关。

**[undo debugging ntp-service**]命令用来关闭NTP的调试信息开关。

缺省情况下，NTP调试信息开关处于关闭状态。

表1-1 debugging ntp-service acl命令输出信息描述表

字段

描述

Access restrict: *right*.

对端设备对本地NTP服务的访问控制权限，*right*取值包括：

·0x0000：表示拒绝访问

·0x0001：表示具有**query**权限，只允许对本地NTP服务进行控制查询

·0x0002：表示具有**synchronization**权限，只允许对端设备与本地设备的时间同步，但不能进行控制查询

·0x0004：表示具有**server**权限，可以对本地NTP服务进行时间请求和控制查询，但本地时间不会与对端设备同步

·0x0008：表示具有**peer**权限，既可以对本地NTP服务进行时间请求和控制查询，本地时间又可以与对端设备同步

表1-2 debugging ntp-service adjustment命令输出信息描述表

字段

描述

System huff size *size* min delay *delay1* huffpuff *delay2*

huff-n\'-puff滤波器的阶数为*size*，最小延迟为*delay1*，过滤后的时延为*delay2*

Adjust local clock

调整本地时钟

offset: *string*

时钟偏移为*string*

jitter: *string*

时钟偏移均方根为*string*

freq: *string*

时钟频率为*string*

stab: *string*

频率稳定度为*string*

poll: *string*

轮询间隔为*string*

Reset clock state

重置时钟状态

time count difference: *string*

时间计数差为*string*

state *state1*-\> *state2*

时钟状态从*state1*变为*state2*

*[state*]取值包括：

·0：unspecified ，未定义

·1：freq not set ，频率未设定

·2：freq set ，频率已设定

·3：spike detect ，检测到大的频率跳变

·4：freq mode ，频率已确定

·5：clock sync，时钟已同步

count *string*

计数器的值为*string*

One-off system time adjustment failed. Error: *error-code*

一次性调整系统时钟失败，错误码为*error-code*

Frequency error: *p1* PPM exceeds tolerance *p2* PPM

当前时钟频率*p1*超出了频率阈值*p2*

Failed to adjust system time

调整系统时间失败

表1-3 debugging ntp-service authentication命令输出信息描述表

字段

描述

Authentication failed

认证失败

auth flag *flag*

认证标志为*flag*

authenticate key ID *id*

认证密钥编号为*id*

packet key ID *id*

收到的NTP报文中的密钥编号为*id*

MAC length *length*

MAC长度为*length*

Received a packet at *time*, from *ip-address*, mode *mode*, key ID *id*, length *length*, authentication result *result*

在时间*time*，从*ip-address*接收到带有认证信息的NTP报文，工作模式为*mode*，密钥ID为*id*，报文长度为*length*，认证结果为*result*

Invalid private packet for bad length *length*

私有报文无效，原因：报文长度错误，报文长度为*length*

Invalid private packet, xmit/rcv timestamp delta *p1* \> *p2*

私有报文无效，原因：发送时间戳和接收时间戳的差值*p1*大于阈值*p2*

表1-4 debugging ntp-service event命令输出信息描述表

字段

描述

Clear peer at *time*

在时间*time*清除与对端设备的连接

next sent time *time*

下一次发送报文的时间为*time*

session ID *id*

会话ID为*id*

refid *string*

参考时钟ID为*string*

Sending control packet with error code *code* to *ip-address*

向*ip-address*发送携带错误码*code*的控制报文

Reading status, session ID *id*

读取ID为*id*的会话的状态

Event at *time*: *event*

在时间*time*发生事件*event*

Quit from the process on receiving the signal *signal*

接收到信令*signal*后，退出NTP进程

表1-5 debugging ntp-service filter命令输出信息描述表

字段

描述

Clock filter: old sample, current *count1*, filter epoch *count2*, peer epoch *count3*

时钟过滤：样本太老，当前时间计数为*count1*，样本时间计数为*count2*，参考时间计数为*count3*

表1-6 debugging ntp-service packet命令输出信息描述表

字段

描述

packet to *ip-address*

向*ip-address*发送NTP报文

count: *count*

控制报文中数据的个数为*count*

RMEOP: *operation*

控制报文中的操作码为*operation*

seq: *sequence*

控制报文中的请求序号为*sequence*

status: *status*

控制报文中的状态字为*sequence*

session ID: *id*

控制报文中的连接ID为*id*

offset: *offset*

控制报文数据偏移量为*offset*

auth_seq: *code*

私有报文中的消息验证码为*code*

impl: *code*

私有报文中的操作码为*code*

req: *code*

私有报文中的请求码为*code*

err_nitems: *code*

私有报文的错误码或数据项的数目为*code*

itemsize: *size*

每一个数据项的大小为*size*

length: *length*

发送报文的长度为*length*

leap: *leap*

报文中的告警信息为*leap*

version: *version*

报文中的协议版本号为*version*

mode: *mode*

报文中的工作模式为*mode*

vrfindex: *index*

收到或发送报文的VPN索引为*index*

stratum: *stratum*

报文中的层数为*stratum*

poll: *poll*

报文中的轮询间隔为*poll*

precision: *precision*

报文中的精度为*precision*

rdel: *delay*

报文中的根延时为*delay*

rdsp: *disper*

报文中的根离差为*disper*

refid: *id*

报文中参考时钟的标识为*id*

当参考时钟为本地时钟时，本字段的取值和本地时钟层数有关：本地时钟层数为1时，为LOCL；本地时钟层数为其它值时，为本地时钟的IP地址

当参考时钟为网络中其它设备的时钟时，本字段为该设备的IP地址

reftime: *string*

报文中的参考时间戳为*string*

orgtime: *string*

报文中的启始时间戳为*string*

rectime: *string*

报文中的接收时间戳为*string*

xmttime: *string*

报文中的发送时间戳为*string*

inptime: *string*

处理报文的时间戳为*string*

packet from *ip-address1* to *ip-address2* on *interface-name*

从接口*interface-name*接收到源IP地址为*ip-address1*、目的IP地址为*ip-address2*的报文

Invalid private packet for wrong item size, received *size1*, should be *size2* or *size3*

私有报文无效，原因：数据项大小错误，接收到的数据项大小为*size1*，应为*size2*（IPv4报文）或*size3*（IPv6报文）

Invalid private packet for not enough data

私有报文无效，原因：数据不完整

Sending request packet to *ip-address*, sequence number *number,* error code *code*

向*ip-address*发送请求报文，序列号为*number*，错误码为*code*

Flushing packet, *number* items

发送*number*个报文

Failed to send packet because too many data, length *length*

由于数据过多，发送报文失败，报文长度为*length*

Failed to set socket option, level *level*, option *option*, error code: *code*

设置socket选项失败，socket选项等级为*level*，socket选项为*option*，错误码为*code*

Failed to get VRF index VPN name *vpn-name*

获取VPN实例*vpn-name*的索引失败

表1-7 debugging ntp-service parameter命令输出信息描述表

字段

描述

Clock filter param

时钟过滤参数

number *number*

时间服务器的个数为*number*

offset *string*

时钟偏差为*string*

delay *string*

双向延迟为*string*

dispersion *string*

离差为*string*

jitter *string*

时钟偏移均方根为*string*

burst *string*

一个时钟脉冲中的数据包个数

表1-8 debugging ntp-service refclock命令输出信息描述表

字段

描述

Select PPS peer *ip-address* offset *offset*, jitter *jitter*

选取PPS类型的时钟*ip-address *作为参考时钟，时钟偏移量为*offset*，时钟偏移量的均方根为*jitter*

Reference clock sent a packet to *ip-address* at *time*

参考时钟在时间*time*向*ip-address*发送报文

Reference clock received a packet from *ip-address* at *time*

参考时钟在时间*time*从*ip-address*接收到报文

表1-9 debugging ntp-service selection命令输出信息描述表

字段

描述

Combine offset *offset*, jitter *jitter*

合并时钟：系统当前时钟偏移量为*offset*，当前时钟偏移量的均方根为*jitter*

Drop peer *ip-address*, select jitter *jitter2*, jitter *jitter3*

丢弃时钟*ip-address*，根据所有peer的jitter计算出的综合jitter为*jitter2*，当前peer连接的jitter为*jitter3*

Survivor *ip-address*, distance *distance*

最终优选的时钟为*ip-address*，时钟举例为*distance*

endpoint *p1*, *p2*

时钟选择算法的终点结构体，*p1*为终点偏移量，*p2*为步进

Clock update at *time*, sample *sample*, session ID *id*, offset *offset*

在时间*time*更新时钟，时钟样本为*sample*，会话ID为*id*，当前时钟偏移量为*offset*

peer *ip-address*, flash *code*, flags *flag*, reach *reach*, root distance *distance*

地址为*ip-address*的时间服务器的可达性，与该时间服务器连接的错误码为*code*，会话标识为*flag*，可达性为*reach*，根同步距离为*distance*

peer *ip-address*, offset *offset*, low *low*, high *high*, flags *flag*

地址为*ip-address*的时间服务器的连接信息：时钟偏移量为*offset*，插值算法的最小阈值为*low*，插值算法的最大阈值为*high*，会话标识为*flag*

set large distance peer *ip-address*, root distance *distance*

保存同步距离过大的时间服务器*ip-address*，同步距离为*distance*

select large distance syspeer *ip-address*

选择同步距离过大的时间服务器*ip-address*作为参考时钟

表1-10 debugging ntp-service synchronization命令输出信息描述表

字段

描述

Synchronized to peer *address*

本地设备的时间与地址为*address*的peer的时间同步

表1-11 debugging ntp-service validity命令输出信息描述表

字段

描述

The packet from *ip-address string* the validity tests *result*

从*ip-address*接收到的报文通过（pass）或未通过（failed）合法性检查，检查结果为*result*

【举例】

\# 网络中有两台设备Device A和Device B，Device A的接口GigabitEthernet1/0/1地址为192.168.0.19，Device B的接口GigabitEthernet1/0/1地址为192.168.0.13，它们之间可以相互ping通。Device B使用本地时钟作为参考时钟，时钟层数为2。在Device A上打开NTP报文调试信息开关。Device A通过客户端/服务器模式与Device B的时间同步时，Device A上打印如下调试信息。

\<DeviceA\> debugging ntp-service packet

\<DeviceA\> system-view

DeviceA ntp-service unicast-server 192.168.0.13 version 3

\*Jan 25 19:58:23:206 2012 H3C NTP/7/PACKET_SEND:

 packet to 192.168.0.13, length: 48

 leap: 3, version: 3, mode: 3, vrfindex: 0

 stratum: 16, poll: 6, precision: 2\^-10

 rdel: 0.000, rdsp: 0.092, refid: INIT

 reftime: d2cadcdc.350d4fcd  Wed, Jan 25 2012 19:56:12.207

 orgtime: 00000000.00000000  Thu, Feb  7 2036  6:28:16.000

 rectime: 00000000.00000000  Thu, Feb  7 2036  6:28:16.000

 xmttime: d2cadd5f.3469b5b7  Wed, Jan 25 2012 19:58:23.204

*[// NTP*]*模块向Device B发送NTP时间同步报文：报文的目的地址是192.168.0.13；报文长度为48字节；本地时钟告警位取值为3；本地NTP协议版本号为3；工作模式为3；报文出端口所在的VPN索引为0（即公网）；本地时钟层数为16；轮询间隔为64秒；时钟精度为2的10次方分之一秒级别；本地根延迟为0.000；根离差为0.092；参考时钟ID为0.0.0.0，表明没有参考时钟；后续的信息分别是参考时间戳、起始时间戳、接收时间戳和发送时间戳*

\*Jan 25 19:49:45:403 2012 H3C NTP/7/PACKET_RECV:

 packet from 192.168.0.13 to 192.168.0.19 on GigabitEthernet1/0/1

 leap: 0, version: 3, mode: 4, vrfindex: 0

 stratum:  2, poll: 6, precision: 2\^-18

 rdel: 0.000, rdsp: 10.941, refid: 127.127.1.0

 reftime: d2cadbe0.1a74d163  Wed, Jan 25 2012 19:52:00.103

 orgtime: d2cadb59.6569818c  Wed, Jan 25 2012 19:49:45.396

 rectime: d2cadc0e.f2d6a9c5  Wed, Jan 25 2012 19:52:46.948

 xmttime: d2cadc0e.f2e12620  Wed, Jan 25 2012 19:52:46.948

 inptime: 59dbcad2.f6985367  Fri, Oct 10 1947 19:15:30.963

*[// Device A*]*收到Device B发过来的NTP响应报文：对端的IP地址是192.168.0.13，本端的IP地址是192.168.0.19，报文入接口是GigabitEthernet1/0/1；对端的告警位为0，表示处于已同步状态；对端NTP的协议版本号为3；工作模式为4；对端报文的出接口属于的VPN索引为0；对端时钟的层数为2；轮询间隔为64秒；精度为2的18次方分之一秒级别；对端的根延迟为0.000；根离差为10.941；对端的参考时钟ID为127.127.1.0，即本地时钟；后续的信息分别是参考时间戳、起始时间戳、接收时间戳、发送时间戳和本地处理该报文的时间戳*

![说明](NTP%20Debug.files/image001.png)

实际上，上述的报文交互过程会进行多次，此处仅给出前两个报文的信息。

\

**SNTP \-- SNTP调试命令 \-- debugging sntp**

------------------------------------------------------------------------

【命令】

**[debugging sntp**[ { **adjustment** \| **all** \| **packet** \| **selection** }]]

**[undo debugging sntp **[{ **adjustment** \| **all** \| **packet** \| **selection** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[adjustment**]：表示SNTP时钟调节调试信息开关。

**[all**]：表示SNTP的所有调试信息开关。

**[packet**]：表示SNTP报文调试信息开关。

**[selection**]：表示NTP时钟选择调试信息开关。

【描述】

**[debugging sntp**]命令用来打开SNTP的调试信息开关。**undo debugging sntp**命令用来关闭SNTP的调试信息开关。

缺省情况下，SNTP的调试信息开关处于关闭状态。

表2-1 debugging sntp adjustment命令输出信息描述表

字段

描述

System huff size *size* min delay *delay1* huffpuff *delay2*

huff-n\'-puff滤波器的阶数为*size*，最小延迟为*delay1*，过滤后的时延为*delay2*

Adjust local clock

调整本地时钟

offset: *string*

时钟偏移为*string*

jitter: *string*

时钟偏移量的均方根为*string*

freq: *string*

时钟频率为*string*

stab: *string*

频率稳定度为*string*

poll: *string*

轮询间隔为*string*

Reset clock state

重置时钟状态

time count difference: *string*

时间计数差为*string*

state *state1*-\> *state2*

时钟状态从*state1*变为*state2*

*[state*]取值包括：

·0：unspecified ，未定义

·1：freq not set ，频率未设定

·2：freq set ，频率已设定

·3：spike detect ，检测到大的频率跳变

·4：freq mode ，频率已确定

·5：clock sync，时钟已同步

count *string*

计数器的值为*string*

One-off system time adjustment failed. Error: *error-code*

一次性调整系统时钟失败，错误码为*error-code*

Frequency error: *p1* PPM exceeds tolerance *p2* PPM

当前时钟频率*p1*超出了频率阈值*p2*

Failed to adjust system time.

调整系统时间失败

表2-2 debugging sntp packet 命令信息描述表

字段

描述

packet to *ip-address*

向*ip-address*发送NTP报文

count: *count*

控制报文中数据的个数为*count*

RMEOP: *operation*

控制报文中的操作码为*operation*

seq: *sequence*

控制报文中的请求序号为*sequence*

status: *status*

控制报文中的状态字为*sequence*

session ID: *id*

控制报文中的连接ID为*id*

offset: *offset*

控制报文数据偏移量为*offset*

auth_seq: *code*

私有报文中的消息验证码为*code*

impl: *code*

私有报文中的操作码为*code*

req: *code*

私有报文中的请求码为*code*

err_nitems: *code*

私有报文的错误码或数据项的数目为*code*

itemsize: *size*

每一个数据项的大小为*size*

length: *length*

发送报文的长度为*length*

leap: *leap*

报文中的告警信息为*leap*

version: *version*

报文中的协议版本号为*version*

mode: *mode*

报文中的工作模式为*mode*

vrfindex: *index*

收到或发送报文的VPN索引为*index*

stratum: *stratum*

报文中的层数为*stratum*

poll: *poll*

报文中的轮询间隔为*poll*

precision: *precision*

报文中的精度为*precision*

rdel: *delay*

报文中的根延时为*delay*

rdsp: *disper*

报文中的根离差为*disper*

refid: *id*

报文中参考时钟的标识为*id*

当参考时钟为本地时钟时，本字段的取值和本地时钟层数有关：本地时钟层数为1时，为LOCL；本地时钟层数为其它值时，为本地时钟的IP地址

当参考时钟为网络中其它设备的时钟时，本字段为该设备的IP地址

reftime: *string*

报文中的参考时间戳为*string*

orgtime: *string*

报文中的启始时间戳为*string*

rectime: *string*

报文中的接收时间戳为*string*

xmttime: *string*

报文中的发送时间戳为*string*

inptime: *string*

处理报文的时间戳为*string*

packet from *ip-address1* to *ip-address2* on *interface-name*

从接口*interface-name*接收到源IP地址为*ip-address1*、目的IP地址为*ip-address2*的报文

Invalid private packet for wrong item size, received *size1*, should be *size2* or *size3*

私有报文无效，原因：数据项大小错误，接收到的数据项大小为*size1*，应为*size2*（IPv4报文）或*size3*（IPv6报文）

Invalid private packet for not enough data

私有报文无效，原因：数据不完整

Sending request packet to *ip-address*, sequence number *number,* error code *code*

向*ip-address*发送请求报文，序列号为*number*，错误码为*code*

Flushing packet, *number* items

发送*number*个报文

Failed to send packet because too many data, length *length*

由于数据过多，发送报文失败，报文长度为*length *

Failed to set socket option, level *level*, option *option*, error code *code*

设置socket选项失败，socket选项等级为*level*，socket选项为*option*，错误码为*code*

Failed to get VRF index, VPN name *vpn-name*

获取VPN实例*vpn-name*的索引失败

表2-3 debugging sntp selection 命令描述表

字段

描述

Select peer *ip-address*, offset *offset*

选取*ip-address *作为参考时钟，时钟偏移量为*offset*

【举例】

\# 网络中有两台设备Device A和Device B，Device A的接口GigabitEthernet1/0/1地址为192.168.0.19，Device B的接口GigabitEthernet1/0/1地址为192.168.0.13，它们之间可以相互ping通。Device B使用本地时钟作为参考时钟，时钟层数为2。在Device A上打开SNTP报文调试开关。Device A作为SNTP客户端，通过客户端/服务器模式与Device B的时间同步时，Device A上打印如下调试信息。

\<DeviceA\> debugging sntp all

\<DeviceA\> system-view

DeviceA sntp unicast-server 192.168.0.13 version 3

\*Jan 25 20:05:11:765 2012 H3C SNTP/7/PACKET_SEND:

 packet to 192.168.0.13, length: 48

 leap: 0, version: 3, mode: 3, vrfindex: 0

 stratum:  3, poll: 6, precision: 2\^-10

 rdel: 0.000, rdsp: 0.946, refid: 192.168.0.13

 reftime: d2cadeb7.c4631f0b  Wed, Jan 25 2012 20:04:07.767

 orgtime: d2cadf61.b1c7abfb  Wed, Jan 25 2012 20:06:57.694

 rectime: 00000000.00000000  Thu, Feb  7 2036  6:28:16.000

 xmttime: d2cadef7.c384ff1a  Wed, Jan 25 2012 20:05:11.763

*[// SNTP*]*模块向Device B发送SNTP时间同步报文：报文的目的地址是192.168.0.13；报文长度为48字节；本地时钟告警位取值为3；本地SNTP协议版本号为3；工作模式为3；报文出端口所在的VPN索引为0（即公网）；本地时钟层数为3；轮询间隔为64秒；时钟精度为2的10次方分之一秒级别；本地根延迟为0.000；根离差为0.946；参考时钟的ID为192.168.0.13，表明向192.168.0.13同步；后续的信息分别是参考时间戳、起始时间戳、接收时间戳和发送时间戳*

\*Jan 25 20:05:11:770 2012 H3C SNTP/7/PACKET_RECV:

 packet from 192.168.0.13 to 192.168.0.19 on GigabitEthernet1/0/1

 leap: 0, version: 3, mode: 4, vrfindex: 0

 stratum:  2, poll: 6, precision: 2\^-18

 rdel: 0.000, rdsp: 10.925, refid: 127.127.1.0

 reftime: d2cadfe9.1a93d102  Wed, Jan 25 2012 20:09:13.103

 orgtime: d2cadef7.c384ff1a  Wed, Jan 25 2012 20:05:11.763

 rectime: d2cae015.9b3b85e8  Wed, Jan 25 2012 20:09:57.606

 xmttime: d2cae015.9b45ae5f  Wed, Jan 25 2012 20:09:57.606

 inptime: f7decad2.7a58fac4  Sun, Oct 12 2031 15:14:26.477

*[// Device A*]*收到Device B发过来的NTP响应报文：对端的IP地址是192.168.0.13，本端的IP地址是192.168.0.19，报文入接口是GigabitEthernet1/0/1；对端的告警位为0，表示处于已同步状态；对端NTP的协议版本号为3；工作模式为4；对端报文的出接口属于的VPN索引为0；对端时钟的层数为2；轮询间隔为64秒；精度为2的18次方分之一秒级别；对端的根延迟为0.000；根离差为10.925；对端的参考时钟ID为127.127.1.0，即本地时钟；后续的信息分别是参考时间戳、起始时间戳、接收时间戳、发送时间戳和本地处理该报文的时间戳*
