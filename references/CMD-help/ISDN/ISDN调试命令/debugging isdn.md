
**ISDN \-- ISDN调试命令 \-- debugging isdn**

------------------------------------------------------------------------

【命令】

**[debugging isdn****cc**[ \| ]**q921**[ \| ]**q931** } \**[interface***interface-type**interface-number* ]

**[undo debugging isdn****cc**[ \| ]**q921**[ \| ]**q931** } \**[interface***interface-type**interface-number* ]

【视图】]

用户视图]

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cc**]：呼叫控制调试信息开关。

**[q921**]：ISDN的Q921数据链路层协议调试信息开关。

**[q931**]：ISDN的Q931网络层协议调试信息开关。

**[interface*** interface-type interface-number*]：指定接口的调试信息开关。

【描述】

**[debugging isdn**]命令用来打开ISDN的调试信息开关。**undo****debugging isdn**命令用来关闭ISDN的调试信息开关。

缺省情况下，ISDN的调试信息开关处于关闭状态。

如果不指定接口，将打开所有ISDN接口的调试信息开关。

表1-1 debugging isdn cc命令输出信息描述表

字段

描述

CC

ISDN呼叫控制

DVA

语音拨号模块，ISDN承载语音业务时的上层应用（User）

DDR

数据拨号模块，ISDN承载数据业务时的上层应用（User）

ISDN_SETUP_REQ

USER向CC请求发出SETUP呼叫

ISDN_CONN_REQ

USER向CC请求发送CONNECT消息

ISDN_DISC_REQ

USER向CC发送拆链消息给对端

ISDN_DISC_RES

USER向CC发送对之前拆链指示的回应

ISDN_CALLPROC_REQ

USER向CC发送CALL-PROCEEDING消息

ISDN_PROGRESS_REQ

USER向CC发送PROGRESS消息给对端

ISDN_ALERTING_REQ

USER向CC发送ALERTING消息给对端

ISDN_INFORMATION_REQ

USER向CC发送INFORMATION消息给对端

ISDN_FACILITY_REQ

USER向CC发送FACILITY消息给对端

ISDN_SETUP_IND

CC向USER指示接收呼叫

ISDN_CONN_IND

CC向USER指示接收到对端的CONNECT消息

ISDN_CONN_CFM

CC向USER指示接收到对端的CONNECT-ACK消息

ISDN_FACILITY_IND

CC向USER指示接收到对端的FACILITY消息

ISDN_DISC_IND

CC向USER指示接收到对端的拆链消息

ISDN_CALLPROC_IND

CC向USER指示接收到对端的CALL-PROCEEDING消息

ISDN_PROGRESS_IND

CC向USER指示接收到对端的PROGRESS消息

ISDN_ALERTING_IND

CC向USER指示接收到对端的ALERTING消息

CCL3_SETUP_REQ

CC和Q931之间呼叫建立请求的原语

CCL3_DL_ESTABLISH_REQ

CC通知Q931进行二层建链

CCL3_DL_ESTABLISH_CONFIRM

二层报给Q931的消息，会给CC报这个消息

CCL3_PROCEEDING_REQ

发Call Proceeding消息给网络

CCL3_ALERTING_REQ

发Alerting消息给网络

CCL3_PROGRESS_REQ

发Progress消息给网络

CCL3_SETUP_RES

发Connect消息给网络

CCL3_SETUPACK_REQ

发Setup Acknowledge消息给网络

CCL3_SETUPCOMP_REQ

发Connect Acknowledge消息给网络

CCL3_DISCONNECT_REQ

发Disconnect消息给网络

CCL3_RELEASE_REQ

发Release消息给网络

CCL3_RELEASECOM_REQ

发Release Complete消息给网络

CCL3_TIME_OUT_IND

收到网络timeout消息

CCL3_SETUP_IND

收到网络Setup消息

CCL3_PROCEEDING_IND

收到网络Call Proceeding消息

CCL3_ALERTING_IND

收到网络Alerting消息

CCL3_SETUP_COMPLETE_ERR

收到网络setup complete err消息

CCL3_SETUP_CONFIRM_ERR

收到网络setup confirm err消息

CCL3_SETUP_CONFIRM

收到网络setup confirm消息

CCL3_SETUP_COMPLETE

收到网络setup complete消息

CCL3_DISCONNECT_IND

收到网络Disconnect消息

CCL3_RELEASE_IND

收到网络Release消息

CCL3_RELEASE_CONFIRM

收到网络Release Complete消息

CCL3_RELEASE_CFM_ERR

T308二次超时向CC发该原语

CCL3_SETUPACK_IND

收到网络Setup Acknowledge消息

CCL3_PROGRESS_IND

收到网络Progress消息

CCL3_RELEASECOM_IND

收到网络Release Complete消息

CCL3_INFO_IND

收到网络info消息

PRIM_SETUP_CFM

CC向USER指示接收呼叫确认

CC\<-DDR

DDR向CC发送原语

CC-\>Q931

CC向Q931发送原语

CallID

由CC模块分配标识呼叫的唯一性的ID号

PortID

端口ID，即接口索引

CES

连接点标识符

ServiceType

服务类型

Channel

通道编号

IsCompleted

是否发送完全

SN_COM

发送完全信息单元

Cause

原因值信息单元

bearer

承载能力信息单元

chan_id

通路标识信息单元

called_n

被叫号码

szCalledNumProperty

被叫号码（信息单元）属性字段

szCallingNumProperty

主叫号码（信息单元）属性字段

szCalledNum

被叫号码（信息单元）号码信息

szCallingNum

主叫号码（信息单元）号码信息

表1-2 debugging isdn q931命令输出信息描述表

字段

描述

DL_I_Data_Req

Q931向Q921发送报文请求

DL_I_Data_Ind

Q921向Q931上送报文指示

CES

连接点标识符

SETUP

发给程控交换机的呼叫建立请求

cr_length

呼叫参考值长度

cr

呼叫参考值

CS_XX

当前呼叫状态

send_comp

号码发送完全

called_n

被叫号码

Call Reference

呼叫参考值

CALL_PROC

呼叫进行时

ALERTING

振铃原语

prog_ind

呼叫进程指示

CONN

Q931呼叫连接请求消息

CONNECT_ACK

Q931呼叫连接应答消息

date/time

日期/时间

Q931-\>Q921

Q931向Q921发送原语

Q921-\>Q931

Q921向Q931发送原语

T303

Q931 T303定时器

T310

Q931 T310定时器

ISDN L3 timer T303 started

Q931 T303定时器开始运行

ISDN Layer 3 call state change

Q931呼叫状态变化

ISDN L3 timer T303 stopped

Q931 T303定时器停止

ISDN L3 timer T310 started

Q931 T310定时器开始运行

ISDN L3 timer T310 stopped

Q931 T310定时器停止

INFORMATION

SPID自协商时发送的information消息

Spid

消息中含有的SPID信息单元

end_id

SPID协商完成时information消息中携带该信息单元（目前该信息单元没有实际用途）

其它信息单元字段描述请参考表 1-1(http://press.h3c.com/data/infoblade/Comware%20V5平台中文/1.1.05%20二层技术-广域网接入/1.1.05.09%20ISDN/ISDN%20Debug.htm#_Ref155675443)

-

表1-3 debugging Isdn q921命令输出信息描述表

字段

描述

Net Tx

网络侧发送报文

Net Rx

网络侧接收报文

User Tx

用户侧发送报文

User Rx

用户侧接收报文

I

信息帧

UI

无编号信息帧

SABME

Q921建链请求帧

DISC

Q921拆链请求帧

UA

无编号确认帧

REJ

拒绝帧

RR

接收准备好帧

RNR

接收未准备好帧

sapi

服务接入点标识号

tei

终端端点标识符（TEI）值

ns

发送序号

nr

接收序号

p

询问比特位值

c/r

命令/响应比特位值

p/f

询问/结束比特位值

Len

用户侧发送的报文长度和内容

Status

Q921状态

TIMER_RECOVERY

Q921状态机中的链路恢复状态

MULTIPLE_FRAME_ESTABLISHED

多帧建链

Q921_DL_ESTABLISH_REQ

Q921建链请求

Q921_DL_DATA_REQ

Q921需确认消息请求

Q921_DL_RELEASE_REQ

Q921拆链请求

Q921_DL_UNIT_DATA_REQ

Q921未确认的消息请求

Q921_DL_ESTABLISH_IND

Q921建链指示

Q921_DL_ESTABLISH_CFM

Q921建链证实

Q921_DL_DATA_IND

Q921需确认的消息指示

Q921_DL_RELEASE_IND

Q921拆链指示

Q921_DL_RELEASE_CFM

Q921拆链证实

Q921_DL_UNIT_DATA_IND

Q921未确认的消息指示

Q921_LAPD_DATA_REQ

Q921向物理层发送需确认的消息请求

Q921_LAPD_DATA_IND

Q921收到物理层发送的需确认的消息指示

Q921_LAPD_DEACTIVE_IND

Q921收到去激活指示

Q921_LAPD_ACTIVE_IND

Q921收到激活指示

Q921_LAPD_ACTIVING_IND

Q921收到激活中指示

Q921_MDL_TEI_IND

Q921与LME间的TEI分配指示

Q921_MDL_REMOVE_IND

Q921与LME间的TEI移除指示

Q921_MDL_TEI_FAIL_IND

Q921与LME间的TEI分配失败指示

Q921_MDL_TEI_REQ

Q921与LME间的TEI分配请求

Q921_MDL_ERROR_IND

Q921与LME间的错误指示

Q921_MDL_UNIT_DATA_IND

Q921与LME间的未确认消息指示

其它信息单元字段描述请参考表 1-1(http://press.h3c.com/data/infoblade/Comware%20V5平台中文/1.1.05%20二层技术-广域网接入/1.1.05.09%20ISDN/ISDN%20Debug.htm#_Ref155675443)

-

【举例】

\# Router A的配置如下：

\<RouterA\> system-view

RouterA dialer-group 1 rule ip permit

RouterA interface Serial2/3/0:15

RouterA-Serial2/3/0:15 link-protocol ppp

RouterA-Serial2/3/0:15 ip address 3.1.1.19 255.255.255.0

RouterA-Serial2/3/0:15 dialer circular enable

RouterA-Serial2/3/0:15 dialer-group 1

RouterA-Serial2/3/0:15 dialer number 666

RouterA-Serial2/3/0:15 return

\# Router B的配置如下：

\<RouterB\> system-view

RouterB interface Serial2/3/0:15

RouterB-Serial2/3/0:15 link-protocol ppp

RouterB-Serial2/3/0:15 ip address 3.1.31.1 255.255.255.0

RouterB-Serial2/3/0:15 dialer circular enable

RouterB-Serial2/3/0:15 dialer-group 1

RouterB-Serial2/3/0:15 quit

RouterB dialer-group 1 rule ip permit

\# Router A与Router B通过程控交换机相连。打开Router A的数据报文调试开关**debugging isdn cc**、**debugging isdn q921**和**debugging isdn q931**。从Router A ping Router B，调试信息分析如下：

\<RouterA\> debugging isdn cc

\<RouterA\> debugging isdn q921

\<RouterA\> debugging isdn q931

\<RouterA\> ping -t 1 -i Dialer 1 -c 1 3.1.31.1

\*Dec 17 03:45:59:986 2011 RouterA ISDN/7/CC: Serial2/3/0:15

  CC\<-DDR: ISDN_SETUP_REQ

  CallID=0xffff, PortID=0x11505, ServiceType=0x8, Channel=0x0, IsCompleted=0x1, Cause=0x00(No0), szCalledNumProperty=0x1 0x0 0x0, szCalledNum=4021

*[// DDR*]*向CC发送请求，要求建立ISDN连接*

\*Dec 17 03:45:59:986 2011 RouterA ISDN/7/CC: Serial2/3/0:15

  CC-\>Q931: CCL3_SETUP_REQ

  CallID=0xffff, PortID=0x1505, CES=0x1, \*SN_COM=a1, \*bearer= 04 02 88 90, \*chan_id= 18 03 a1 83 81, \*called_n= 70 05 80 34 30 32 31

*[// CC*]*向Q931发送请求，要求网络层建立连接*

\*Dec 17 03:45:59:986 2011 RouterA ISDN/7/Q931: Serial2/3/0:15

  Q931-\>Q921: DL_I_Data_Req, CES=1

  cr_length=2, cr= 02 00 93, SETUP, \*send_comp=a1, \*bearer= 04 02 88 90, \*chan_id= 18 03 a1 83 81, \*called_n= 70 05 80 34 30 32 31

*[// Q931*]*向Q921发送请求，要求建立链路层连接*

\*Dec 17 03:45:59:987 2011 RouterA ISDN/7/Q921: Serial2/3/0:15

  CES=1, Status=MULTIPLE_FRAME_ESTABLISHED

  User Tx: Len=26 00 01 90 90 08 02 00 93 05 A1 04 02 88 90 18 03 A1 83 81 70 05 80 34 30 32 31

  User Tx: sapi=00, tei=00, c/r=0, I, ns=48, nr=48, p=0

*[// Q921*]*向对端发送I帧*

\*Dec 17 03:45:59:988 2011 RouterA ISDN/7/Q931: Serial2/3/0:15

  ISDN L3 timer T303 started, Call Reference=0x0093.

*[// Q931*]*启动定时器*

\*Dec 17 03:45:59:988 2011 RouterA ISDN/7/Q931: Serial2/3/0:15

  ISDN Layer 3 call state change: CS_NULL-\>CS_CALL_INITIATED

\*Dec 17 03:45:59:996 2011 RouterA ISDN/7/Q921: Serial2/3/0:15

  CES=1, Status=MULTIPLE_FRAME_ESTABLISHED

  User Rx: Len=4 00 01 01 92

  User Rx: sapi=00, tei=00, c/r=0, RR, nr=49, p/f=0

*[// Q921*]*收到RR帧*

\*Dec 17 03:46:00:026 2011 RouterA ISDN/7/Q921: Serial2/3/0:15

  CES=1, Status=MULTIPLE_FRAME_ESTABLISHED

  User Rx: Len=14 02 01 90 92 08 02 80 93 02 18 03 A9 83 8F

  User Rx: sapi=00, tei=00, c/r=1, I, ns=48, nr=49, p=0

*[// Q921*]*收到对端发送的I帧*

\*Dec 17 03:46:00:027 2011 RouterA ISDN/7/Q931: Serial2/3/0:15

  Q921-\>Q931: DL_I_Data_Ind, CES=1

  cr_length=2, cr= 02 80 93, CALL_PROC, \*chan_id= 18 03 a9 83 8f

*[// Q921*]*将该I帧上送Q931*

\*Dec 17 03:46:00:027 2011 RouterA ISDN/7/Q931: Serial2/3/0:15

  ISDN L3 timer T303 stopped, Call Reference=0x0093.

\*Dec 17 03:46:00:027 2011 RouterA ISDN/7/Q931: Serial2/3/0:15

  ISDN L3 timer T310 started, Call Reference=0x0093.

\*Dec 17 03:46:00:027 2011 RouterA ISDN/7/Q931: Serial2/3/0:15

  ISDN Layer 3 call state change: CS_CALL_INITIATED-\>CS_OUTGOING_CALL_PROCEEDING

\*Dec 17 03:46:00:028 2011 RouterA ISDN/7/Q921: Serial2/3/0:15

  CES=1, Status=MULTIPLE_FRAME_ESTABLISHED

  User Tx: Len=4 02 01 01 92

  User Tx: sapi=00, tei=00, c/r=1, RR, nr=49, p/f=0

*[// Q921*]*发送RR帧应答*

\*Dec 17 03:46:00:083 2011 RouterA ISDN/7/Q921: Serial2/3/0:15

  CES=1, Status=MULTIPLE_FRAME_ESTABLISHED

  User Rx: Len=13 02 01 92 92 08 02 80 93 01 1E 02 82 81

  User Rx: sapi=00, tei=00, c/r=1, I, ns=49, nr=49, p=0

*[// Q921*]*收到对端发送的I帧*

\*Dec 17 03:46:00:084 2011 RouterA ISDN/7/Q931: Serial2/3/0:15

  Q921-\>Q931: DL_I_Data_Ind, CES=1

  cr_length=2, cr= 02 80 93, ALERTING, \*prog_ind= 1e 02 82 81

*[// Q921*]*将该I帧上送Q931*

\*Dec 17 03:46:00:084 2011 RouterA ISDN/7/Q931: Serial2/3/0:15

  ISDN L3 timer T310 stopped, Call Reference=0x0093.

\*Dec 17 03:46:00:084 2011 RouterA ISDN/7/Q931: Serial2/3/0:15

  ISDN Layer 3 call state change: CS_OUTGOING_CALL_PROCEEDING-\>CS_CALL_DELIVERED

\*Dec 17 03:46:00:085 2011 RouterA ISDN/7/Q921: Serial2/3/0:15

  CES=1, Status=MULTIPLE_FRAME_ESTABLISHED

  User Tx: Len=4 02 01 01 94

  User Tx: sapi=00, tei=00, c/r=1, RR, nr=4A, p/f=0

*[// Q921*]*发送RR帧*

\*Dec 17 03:46:00:089 2011 RouterA ISDN/7/Q921: Serial2/3/0:15

  CES=1, Status=MULTIPLE_FRAME_ESTABLISHED

  User Rx: Len=21 02 01 94 92 08 02 80 93 07 1E 02 82 81 29 06 0C 05 12 0A 21 1C

  User Rx: sapi=00, tei=00, c/r=1, I, ns=4A, nr=49, p=0

*[// Q921*]*收到对端发送的I帧*

\*Dec 17 03:46:00:090 2011 RouterA ISDN/7/Q931: Serial2/3/0:15

  Q921-\>Q931: DL_I_Data_Ind, CES=1

  cr_length=2, cr= 02 80 93, CONN, \*prog_ind= 1e 02 82 81, \*date/time= 29 06 0c 05 12 0a 21 1c

*[// Q921*]*将该I帧上送Q931*

\*Dec 17 03:46:00:090 2011 RouterA ISDN/7/Q931: Serial2/3/0:15

  ISDN Layer 3 call state change: CS_CALL_DELIVERED-\>CS_CONNECT_REQUEST

\*Dec 17 03:46:00:091 2011 RouterA ISDN/7/Q931: Serial2/3/0:15

  Q931-\>Q921: DL_I_Data_Req, CES=1

  cr_length=2, cr= 02 00 93, CONNECT_ACK

*[// Q931*]*下发发送I帧的请求*

\*Dec 17 03:46:00:092 2011 RouterA ISDN/7/Q921: Serial2/3/0:15

  CES=1, Status=MULTIPLE_FRAME_ESTABLISHED

  User Tx: Len=9 00 01 92 96 08 02 00 93 0F

  User Tx: sapi=00, tei=00, c/r=0, I, ns=49, nr=4B, p=0

*[// Q921*]*向对端发送I帧*

\*Dec 17 03:46:00:092 2011 RouterA ISDN/7/Q931: Serial2/3/0:15

  ISDN Layer 3 call state change: CS_CONNECT_REQUEST-\>CS_ACTIVE

\*Dec 17 03:46:00:099 2011 RouterA ISDN/7/Q921: Serial2/3/0:15

  CES=1, Status=MULTIPLE_FRAME_ESTABLISHED

  User Rx: Len=4 00 01 01 94

  User Rx: sapi=00, tei=00, c/r=0, RR, nr=4A, p/f=0

*[// Q921*]*收到RR帧*

\*Dec 17 03:46:10:346 2011 RouterA ISDN/7/Q921: Serial2/3/0:15

  CES=1, Status=MULTIPLE_FRAME_ESTABLISHED

  User Rx: Len=4 02 01 01 95

  User Rx: sapi=00, tei=00, c/r=1, RR, nr=4A, p/f=1

*[// Q921*]*收到RR帧*

\*Dec 17 03:46:10:347 2011 RouterA ISDN/7/Q921: Serial2/3/0:15

  CES=1, Status=MULTIPLE_FRAME_ESTABLISHED

  User Tx: Len=4 02 01 01 97

  User Tx: sapi=00, tei=00, c/r=1, RR, nr=4B, p/f=1

*[// Q921*]*发送RR帧*

\*Dec 17 03:46:20:483 2011 RouterA ISDN/7/Q921: Serial2/3/0:15

  CES=1, Status=MULTIPLE_FRAME_ESTABLISHED

  User Tx: Len=4 00 01 01 97

  User Tx: sapi=00, tei=00, c/r=0, RR, nr=4B, p/f=1

*[// Q921*]*发送RR帧*

\*Dec 17 03:46:20:490 2011 RouterA ISDN/7/Q921: Serial2/3/0:15

  CES=1, Status=TIMER_RECOVERY

  User Rx: Len=4 00 01 01 95

  User Rx: sapi=00, tei=00, c/r=0, RR, nr=4A, p/f=1

*[// Q921*]*收到RR帧*
