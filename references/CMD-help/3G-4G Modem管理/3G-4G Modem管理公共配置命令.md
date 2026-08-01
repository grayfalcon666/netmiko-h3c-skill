<!-- CMD-INDEX
  controller cellular                 | 系统视图             | L35
  description                         | Cellular接口视图     | L69
  display cellular                    | 任意视图             | L111
  display controller cellular         | 任意视图             | L1337
  dm-port open                        | Cellular接口视图     | L1495
  mode                                | Cellular接口视图     | L1541
  modem reboot                        | Cellular接口视图     | L1605
  modem response                      | Cellular接口视图     | L1639
  pin modify                          | Cellular接口视图     | L1689
  pin unlock                          | Cellular接口视图     | L1751
  pin verification enable             | Cellular接口视图     | L1817
  pin verify                          | Cellular接口视图     | L1881
  plmn search                         | Cellular接口视图     | L1941
  plmn select                         | Cellular接口视图     | L2035
  profile create                      | Cellular接口视图     | L2091
  profile delete                      | Cellular接口视图     | L2161
  profile main                        | Cellular接口视图     | L2201
  reset counters controller cellular  | 用户视图             | L2255
  sendat                              | Cellular接口视图     | L2297
  shutdown                            | Cellular接口视图     | L2363
  serial-set                          | Cellular接口视图     | L2401
  bandwidth                           | 以太网通道接口视图        | L2443
  default                             | 以太网通道接口视图        | L2489
  description                         | 以太网通道接口视图        | L2525
  display interface eth-channel       | 任意视图             | L2573
  eth-channel                         | Cellular接口视图     | L2823
  interface eth-channel               | 系统视图             | L2865
  ip address cellular-alloc           | 以太网通道接口视图        | L2899
  mtu                                 | 以太网通道接口视图        | L2949
  reset counters interface            | 用户视图             | L2991
  shutdown                            | 以太网通道接口视图        | L3033
-->

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- controller cellular**

------------------------------------------------------------------------

**[controller cellular**]命令用来进入Cellular接口视图。

【命令】

**[controller cellular** *cellular-number*]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[cellular-number*]：Cellular接口的编号。

【举例】

\# 进入接口Cellular2/4/0的视图。

\<Sysname\> system-view

Sysname controller cellular 2/4/0

Sysname-Cellular 2/4/0

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来设置当前接口的描述信息。

**[undo description**]命令用来恢复缺省情况。

【命令】

**[description** *text*]

**[undo description**]

【缺省情况】

接口的描述信息为"*该接口的接口名* Interface"，比如：Cellular2/4/0 Interface。

【视图】

Cellular接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：接口描述信息，为1～255个字符的字符串，区分大小写。

【举例】

\# 设置接口Cellular2/4/0的描述信息为"Cellular-intf"。

\<Sysname\> system-view

Sysname controller cellular 2/4/0

Sysname-Cellular2/4/0 description Cellular-intf

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- display cellular**

------------------------------------------------------------------------

**[display** **cellular**]命令用来显示3G/4G Modem的呼叫连接信息。

【命令】

**[display cellular** [ *interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-number*]：显示指定Cellular接口的3G/4G Modem呼叫连接信息。如果不指定本参数，则显示所有在位Modem对应Cellular接口的3G/4G Modem呼叫连接信息。

【使用指导】

对于不同厂家生产的3G/4G Modem，此命令显示的内容和格式可能略有区别。

【举例】

\# 显示3G Modem的呼叫连接信息（WCDMA网络）。

\<Sysname\> display cellular 2/4/0

Cellular2/4/0:

  Hardware Information:

    Model: E176G

    Modem Firmware Version: 11.604.09.00.00

    Hardware Version: CD25TCPU

    International Mobile Subscriber Identity (IMSI): 460029010431055

    International Mobile Equipment Identity (IMEI): 353871020138548

    Factory Serial Number (FSN):  DK9RAA1871500602

    Modem Status: Online

  Profile Information:

    Profile 1: Active

      PDP Type: IPv4, Header Compression: Off

      Data Compression: Off

      Access Point Name (APN): 001

      Packet Session Status: Inactive

  Modem Setup Information:

    Diagnostics Monitor: Close

  Network Information:

    Current Service Status: Service available

    Current Service: Combined

    Packet Service: Attached

    Packet Session Status: Inactive

    Current Roaming Status: Roaming

    Network Selection Mode: Manual

    Network Connection Mode: WCDMA precedence

    Current Network Connection: HSDPA and HSUPA

    Mobile Country Code (MCC): 460

    Mobile Network Code (MNC): 00

    Location Area Code (LAC): 4318

    Cell ID: 25381

  Radio Information:

    Current Band: ANY

    Current RSSI: -51 dBm

  Modem Security Information:

    PIN Verification: Disabled

    PIN Status: Ready

    Number of Retries remaining: 3

    SIM Status: OK

表1-1 display cellular命令显示信息描述表（WCDMA网络）

字段

描述

Hardware Information

硬件信息

Model

3G Modem名称

Modem Firmware Version

3G Modem的软件版本号

Hardware Version

3G Modem的硬件版本号

International Mobile Subscriber Identity (IMSI)

SIM卡的IMSI号码串

International Mobile Equipment Identity (IMEI)

3G Modem的IMEI串号

Factory Serial Number (FSN)

3G Modem的产品序列号

Modem Status

3G Modem的状态：

·Online：3G Modem处于上电状态

·Offline：3G Modem处于下电状态或省电模式，cellular接口功能不可用

Profile Information

3G Modem的参数模板信息

Profile 1

3G Modem的PDP设置状态：

·Active：已经配置参数模板

·Undefined：还未配置参数模板

PDP Type

PDP类型，只有Profile 1: Active时，才显示该信息：

·IPv4：PDP协议类型为IPv4

·IPv6：PDP协议类型为IPv6

·PPP：PDP协议类型为PPP透传

Header Compression

PDP头压缩模式：

·On：使能PDP头压缩

·Off：禁止PDP头压缩

Data Compression

PDP数据压缩模式：

·On：使能PDP数据压缩

·Off：禁止PDP数据压缩

Access Point Name (APN)

接入点名称

Packet Session Status

PDP的激活状态：

·Active：处于激活状态，3G Modem正在进行PPP传输

·Inactive：处于非激活状态，3G Modem接口的物理状态为Down

Modem Setup Information

Modem安装状态

Diagnostics Monitor

诊断口监控状态

·Open：诊断监控打开

·Close：诊断监控关闭

Network Information

网络信息

Current Service Status

3G Modem的服务状态：

·Service available：提供有效服务

·Emergency：提供有限制服务，Cellular接口功能不可用

·No service：无法提供服务，Cellular接口功能不可用

·Low power：处于省电模式，Cellular接口功能不可用

Current Service

当前服务类型：

·Circuit-switched：仅CS域服务

·Packet-switched：仅PS域服务

·Combined：CS和PS域服务都有效

·Invalid：服务无效

Packet Service

3G Modem PS域附着状态：

·Detached：分离状态，Cellular接口功能不可用

·Attached：连接状态

Current Roaming Status

漫游状态：

·Roaming：漫游状态

·Home：本地状态

Network Selection Mode

网络选择模式：

·Manual：手动选择

·Automatic：自动选择

Network Connection Mode

网络连接模式：

·WCDMA only：仅连接WCDMA网络

·WCDMA precedence：优先连接WCDMA网络

·GSM only：仅连接GSM网络

·GSM precedence：优先连接GSM网络

Current Network Connection

当前网络连接：

·No Service：无服务

·GSM：GSM网络

·GPRS：GPRS网络

·EDGE：EDGE网络

·WCDMA：WCDMA网络

·HSDPA：HSDPA网络

·HSUPA：HSUPA网络

·HSDPA and HSUPA：HSDPA和HSUPA网络

·HSPA+：HSPA+网络

·Unknown：未知网络

Mobile Country Code (MCC)

移动国家码，搜索到网络后才能显示该信息。例如：中国大陆的国家码为460

Mobile Network Code (MNC)

运营商网络代码，成功注册到网络后才能显示该信息。例如：中国移动GSM网络代码为00

Location Area Code (LAC)

位置码信息，成功注册到网络后才能显示该信息

Cell ID

小区信息，成功注册到网络后才能显示该信息

Current Band

当前频带选择模式：

·GSM：选择GSM网络频带

·WCDMA：选择WCDMA网络频带

·ANY：选择任意频带

·AUTO：自动选择频带

Current RSSI

当前信号质量：

·信号质量的取值范围为-110dBm ～ -51dBm

·Unknown：无信号，Cellular接口功能不可用

Modem Security Information

Modem安全信息

PIN Verification

PIN认证状态：

·Disabled：未使能PIN认证

·Enabled：使能了PIN认证

PIN Status

·Ready：SIM卡状态正常

·PIN Requirement：SIM卡有PIN认证请求，需要用户配置**pin verify**命令

·PUK Requirement：SIM卡有PUK认证请求，需要用户配置**pin unlock**命令

Number of Retries remaining

PIN或PUK剩余尝试次数

SIM Status

SIM卡状态：

·OK：SIM卡状态正常

·Network Reject：SIM卡被拒绝接入网络，Cellular接口功能不可用

·Not Insert：未插入SIM卡，Cellular接口功能不可用

\# 显示3G Modem的呼叫连接信息（TD-SCDMA网络）。

\<Sysname\> display cellular 2/4/0

Cellular2/4/0:

  Hardware Information:

    Model: ET128

    Modem Firmware Version: 11.101.01.08.00

    Hardware Version:  CS31TCPU

    International Mobile Subscriber Identity (IMSI): 460079011105842

    International Mobile Equipment Identity (IMEI): 860039002369111

    Factory Serial Number (FSN):  GQ4CAB1942911350

    Modem Status: Online

  Profile Information:

    Profile 1: Active

      PDP Type: IPv4

      Header Compression: Off

      Data Compression: Off

      Access Point Name (APN): cmnet

      Packet Session Status: Active

  Network Information:

    Current Service Status: Service available

    Network Selection Mode: Automatic

    Network Connection Mode: TD-SCDMA precedence

    Current Network Connection: HSDPA

    Mobile Network Name: CHINA MOBILE

    Downstream Bandwidth: 2800000 bps

  Radio Information:

    Current RSSI: -75 dBm

  Modem Security Information:

    PIN Verification: Disabled

    PIN Status: Ready

    Number of Retries remaining: 3

    SIM Status: OK

表1-2 display cellular命令显示信息描述表（TD-SCDMA网络）

字段

描述

Hardware Information

硬件信息

Model

3G Modem名称

Modem Firmware Version

3G Modem的软件版本号

Hardware Version

3G Modem的硬件版本号

International Mobile Subscriber Identity (IMSI)

SIM卡的IMSI号码串

International Mobile Equipment Identity (IMEI)

3G Modem的IMEI串号

Factory Serial Number (FSN)

3G Modem的产品序列号

Modem Status

3G Modem的状态：

·Online：3G Modem处于上电状态

·Offline：3G Modem处于下电状态或省电模式，cellular接口功能不可用

Profile Information

3G Modem的参数模板信息

Profile 1

3G Modem的PDP设置状态：

·Active：已经配置参数模板

·Undefined：还未配置参数模板

PDP Type

PDP类型，只有Profile 1: Active时，才显示该信息：

·IPv4：PDP协议类型为IPv4

·IPv6：PDP协议类型为IPv6

·PPP：PDP协议类型为PPP透传

Header Compression

PDP头压缩模式：

·On：使能PDP头压缩

·Off：禁止PDP头压缩

Data Compression

PDP数据压缩模式：

·On：使能PDP数据压缩

·Off：禁止PDP数据压缩

Access Point Name (APN)

接入点名称

Packet Session Status

PDP的激活状态：

·Active：处于激活状态，3G Modem正在进行PPP传输

·Inactive：处于非激活状态，3G Modem接口的物理状态为Down

Network Information

网络信息

Current Service Status

3G Modem的服务状态：

·Service available：提供有效服务

·Emergency：提供有限制服务，Cellular接口功能不可用

·No service：无法提供服务，Cellular接口功能不可用

·Low power：处于省电模式，Cellular接口功能不可用

Network Selection Mode

网络选择模式：

·Manual：手动选择

·Automatic：自动选择

Network Connection Mode

网络连接模式：

·TD-SCDMA only：仅连接TD-SCDMA网络

·TD-SCDMA precedence：优先连接TD-SCDMA网络

·GSM only：仅连接GSM网络

·GSM precedence：优先连接GSM网络

Current Network Connection

当前网络连接：

·No Service：无服务

·GSM：GSM网络

·GPRS：GPRS网络

·EDGE：EDGE网络

·TD-SCDMA：TD-SCDMA网络

·HSDPA：HSDPA网络

·Unknown：未知网络

Mobile Network Name

移动网络名称

Downstream Bandwidth

下行理论带宽，单位为bps

Radio Information

无线电通信信息

Current RSSI

当前信号质量：

·信号质量的取值范围为-110dBm ～ -51dBm

·Unknown：无信号，Cellular接口功能不可用

Modem Security Information

Modem安全信息

PIN Verification

PIN认证状态：

·Disabled：未使能PIN认证

·Enabled：使能了PIN认证

PIN Status

PIN状态：

·Ready：SIM卡状态正常

·PIN Requirement：SIM卡有PIN认证请求，需要用户配置**pin verify**命令

·PUK Requirement：SIM卡有PUK认证请求，需要用户配置**pin unlock**命令

Number of Retries remaining

PIN或PUK剩余尝试次数

SIM Status

SIM卡状态：

·OK：SIM卡状态正常

·Network Reject：SIM卡被拒绝接入网络，Cellular接口功能不可用

·Not Insert：未插入SIM卡，Cellular接口功能不可用

\# 显示3G Modem的呼叫连接信息（CDMA网络）。

\<Sysname\> display cellular 2/4/0

Cellular2/4/0:

  Hardware Information:

    Model: EC169

    Manufacturer: HUAWEI TECHNOLOGIES CO.

    Modem Firmware Version: 11.002.03.01.45

    Hardware Version:  CE62TCPUVer A

    Electronic Serial Number (ESN): c1836f2d

    Preferred Roaming List (PRL) Version: 0

    International Mobile Subscriber Identity (IMSI): 460036101433925

    Modem Status: Online

  Network Information:

    Current Service Status: Service available

    Current Roaming Status: Home

    Network Connection Mode: Manual

    Current Network Connection: 1xRTT/EVDO HYBRID

    Downstream Bandwidth: 3100000 bps

  Radio Information:

    Current RSSI(1xRTT): -93 dBm

    Current RSSI(EVDO): -75 dBm

    Current Voltage: 3336 mV

  Modem Security Information:

    PIN Verification: Disabled

    PIN Status: Ready

    Number of Retries remaining: 3

    UIM Status: OK

表1-3 display cellular命令显示信息描述表（CDMA网络）

字段

描述

Hardware Information

硬件信息

Model

3G Modem名称

Manufacturer

设备生产商

Modem Firmware Version

3G Modem的软件版本号

Hardware Version

3G Modem的硬件版本号

Electronic Serial Number (ESN)

3G Modem的产品序列号

Preferred Roaming List (PRL) Version

首选漫游列表版本

International Mobile Subscriber Identity (IMSI)

UIM卡的IMSI号码串

Modem Status

3G Modem的状态：

·Online：3G Modem处于上电状态

·Offline：3G Modem处于下电状态或省电模式，cellular接口功能不可用

Network Information

网络信息

Current Service Status

3G Modem的服务状态：

·Service available：提供有效服务

·Emergency：提供有限制服务，Cellular接口功能不可用

·No service：无法提供服务，Cellular接口功能不可用

·Low power：处于省电模式，Cellular接口功能不可用

Current Roaming Status

漫游状态：

·Roaming：漫游状态

·Home：本地状态

Network Selection Mode

网络选择模式：

·Manual：手动选择

·Automatic：自动选择

Current Network Connection

当前网络连接：

·No Service：无服务

·1xRTT/EVDO HYBRID：1xRTT和EVDO网络

·EVDO：EVDO网络

·1xRTT：1xRTT网络

·Unknown：未知网络

Downstream Bandwidth

下行理论带宽，单位为bps

Radio Information

无线电通信信息

Current RSSI (1xRTT)

当前1xRTT网络信号质量：

·信号质量的取值范围为-125dBm ～ -75dBm

·Unknown：无信号

Current RSSI (EVDO)

当前EVDO网络信号质量：

·信号质量的取值范围为-120dBm ～ -60dBm

·Unknown：无信号

Current Voltage

UIM卡电压值，单位为mV

Modem Security Information

Modem安全信息

PIN Verification

PIN认证状态：

·Disabled：未使能PIN认证

·Enabled：使能了PIN认证

PIN Status

·Ready：UIM卡状态正常

·PIN Requirement：UIM卡有PIN认证请求，需要用户配置**pin verify**命令

·PUK Requirement：UIM卡有PUK认证请求，需要用户配置**pin unlock**命令

Number of Retries remaining

PIN或PUK剩余尝试次数

UIM Status

UIM卡状态：

·OK：SIM卡状态正常

·Network Reject：SIM卡被拒绝接入网络，Cellular接口功能不可用

·Not Insert：未插入SIM卡，Cellular接口功能不可用

\# 显示4G Modem的呼叫连接信息（LTE网络）。

\<Sysname\> display cellular 0/0

Cellular0/0:

  Hardware Information:

    Model: MC7750

    Manufacturer: Sierra Wireless, Incorporated

    Modem Firmware Version: SWI9600M_03.05.10.06

    Hardware Version: 10

    International Mobile Equipment Identity (IMEI): 990000560327506

    Modem Status: Online

  Profile Information:

    Profile index: 1

      PDP Type: IPv4

      Header Compression: Off

      Data Compression: Off

      Access Point Name (APN): vzwinternet

  Network Information:

    Current Service Status: Service available

    Current Roaming Status: Roaming

    Current Data Bearer Technology: Unknown

    Network Selection Mode: Manual

    Mobile Country Code (MCC): 460

    Mobile Network Code (MNC): 00

    Location Area Code (LAC): 4318

    Cell ID: 25381

  Radio Information:

    Technology Preference: LTE only

    Technology Selected: LTE

  LTE related info:

    Current RSSI: -79 dBm

    Current RSRQ: -9 dB

    Current RSRP: -106 dBm

    Current SNR: 5 dB

    Tx Power: -3276 dBm

  Modem Security Information:

    PIN Verification: Disabled

    PIN Status: Ready

    SIM Status: OK

表1-4 display cellular命令显示信息描述表（LTE网络）

字段

描述

Hardware Information

硬件信息

Model

Modem名称

Manufacturer

设备生产商

Modem Firmware Version

Modem的软件版本号

Hardware Version

Modem的硬件版本号

International Mobile Equipment Identity (IMEI)

Modem的IMEI串号

Modem Status

Modem的状态：

·Online：Modem处于上电状态

·Offline：Modem处于下电状态或省电模式，Cellular接口功能不可用

Profile Information

Modem的参数模板信息

Profile index

Modem的参数模板索引

PDP Type

PDP类型，只有Profile 1 = Active时，才显示该信息：

·IPv4：PDP协议类型为IPv4

·IPv6：PDP协议类型为IPv6

·PPP：PDP协议类型为PPP透传

Header Compression

PDP头压缩模式：

·On：使能PDP头压缩

·Off：禁止PDP头压缩

Data Compression

PDP数据压缩模式：

·On：使能PDP数据压缩

·Off：禁止PDP数据压缩

Access Point Name

接入点名称

Network Information

网络信息

Current Service Status

Modem的服务状态：

·Limited：服务受限，Cellular接口功能不可用

·Service available：提供有效服务

·Emergency：提供有限制服务，Cellular接口功能不可用

·No service：无法提供服务，Cellular接口功能不可用

·Low power：处于省电模式，Cellular接口功能不可用

Current Roaming Status

漫游状态：

·Roaming：漫游状态

·Home：本地状态

Current Data Bearer Technology

当前载波制式，包括：

·CDMA2000 1X

·CDMA2000 HRPD (1xEV-DO)

·GSM

·UMTS

·CDMA2000 HRPD (1xEV-DO RevA)

·EDGE

·HSDPA and WCDMA

·WCDMA and HSUPA

·HSDPA and HSUPA

·LTE

·CDMA2000 EHRPD

·HSDPA+ and WCDMA

·HSDPA+ and HSUPA

·DC_HSDPA+ and WCDMA

·DC_HSDPA+ and HSUPA

·HSDPA+ and 64QAM

·HSDPA+, 64QAM and HSUPA

·TDSCDMA

·TDSCDMA and HSDPA

·Unknown

Network Selection Mode

网络选择模式：

·Manual：手动选择

·Automatic：自动选择

Mobile Country Code

移动国家码，搜索到网络后才能显示该信息。例如：中国大陆的国家码为460

Mobile Network Code

运营商网络代码，成功注册到网络后才能显示该信息。例如：中国移动GSM网络代码为00

Location Area Code

位置码信息，成功注册到网络后才能显示该信息

Cell ID

小区信息，成功注册到网络后才能显示该信息

Radio Information

无线电通信信息

Technology Preference

网络优先连接选择：

·AUTO：自动选择连接网络

·GSM only：仅连接GSM网络

·GSM precedence：优先连接GSM网络

·WCDMA only：仅连接WCDMA网络

·WCDMA precedence：优先连接WCDMA网络

·TD-SCDMA only：仅连接TD-SCDMA网络

·TD-SCDMA precedence：优先连接TD-SCDMA网络

·EVDO：仅连接CDMA-EVDO网络

·1x RTT：仅连接CDMA-1x RTT网络

·1xRTT/EVDO HYBRID：同时连接CDMA-EVDO和CDMA-1x RTT网络

·LTE only：仅连接LTE网络

Technology Selected

当前选择的网络：

·GSM：连接GSM网络

·WCDMA：连接WCDMA网络

·TD-SCDMA：连接TD-SCDMA网络

·EVDO：连接CDMA-EVDO网络

·1x RTT：连接CDMA-1x RTT网络

·1xRTT/EVDO HYBRID：同时连接CDMA-EVDO和CDMA-1x RTT网络

·LTE：连接LTE网络

LTE related info

LTE网络相关信息

Current RSSI

当前信号质量：

·信号质量的取值范围为-110dBm～-51dBm

·Unknown：无信号，Cellular接口功能不可用

Current RSRQ

当前参考信号接收质量

Current RSRP

当前参考信号接收功率

Current SNR

当前信噪比

Tx Power

发送功率

Modem Security Information

Modem安全信息

PIN Verification

PIN认证状态：

·Disabled：未使能PIN认证

·Enabled：使能了PIN认证

·Unknown：当前PIN码状态未知

PIN Status

·Ready：SIM卡状态正常

·PIN Requirement：SIM卡有PIN认证请求，需要用户配置**pin verify**命令

·PUK Requirement：SIM卡有PUK认真请求，需要用户配置**pin unlock**命令

SIM Status

SIM卡状态：

·OK：SIM卡状态正常

·Network Reject：SIM卡被拒绝接入网络，Cellular接口功能不可用

·Not Inserted：未插入SIM卡，Cellular接口功能不可用

·Not Initialized：当前SIM卡状态未知

【相关命令】

·**mode cdma**

·**mode td-scdma**

·**mode wcdma**

·**pin modify**

·**pin unlock**

·**pin verification**** enable**

·**pin verify**

·**plmn select**

·**profile create**

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- display controller cellular**

------------------------------------------------------------------------

**[display controller cellular**]命令用来显示Cellular接口的相关信息。

【命令】

**[display controller** [ **cellular** [ *interface-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-number*]：Cellular接口的编号。

【使用指导】

·如果不指定**cellular**参数，将显示设备支持的所有接口的相关信息；

·如果指定**cellular**参数，不指定*interface-number*参数，将显示所有已创建的Cellular接口的相关信息。

·USB 3G/4G Modem模块热插拔后，相关统计信息会被清零。

【举例】

\# 显示接口Cellular2/4/0的相关信息。

\<Sysname\> display controller cellular 2/4/0

Cellular2/4/0

Current state: UP

Description: Cellular2/4/0 Interface

Modem status: Present

DM port status: Disabled

Capability:

  1 Control channel, 1 PPP channel

Control channel 0 traffic statistics:

  TX: 0 packets, 0 errors

  RX: 0 packets, 0 errors

PPP channel 0 traffic statistics:

  TX: 0 packets, 0 errors

  RX: 0 packets, 0 errors

表1-5 display controller cellular命令显示信息描述表

字段

描述

Cellular2/4/0

Current state

接口当前的物理状态和管理状态，可能的取值及含义如下：

·AdministrativelyDOWN：表示该接口已经通过**shutdown**命令被关闭，即管理状态为关闭

·DOWN：表示该接口的管理状态为开启，但物理状态为关闭（可能因为没有物理连线或者线路故障）

·UP：该接口的管理状态和物理状态均为开启

Description

Cellular接口的描述信息

Modem status

USB 3G/4G Modem模块的在位状态：

·Present：表示在位

·Absent：表示不在位

DM port status

DM功能的状态：

·Enabled：表示DM功能处于打开状态

·Disabled：表示DM功能处于关闭状态

Capability:

  1 Control channel, 1 PPP channel

Cellular接口支持的通道类型及数量：

·1 Control channel：支持1个控制通道

·1 PPP channel：支持1个异步串口子通道

·1 ETH channel：支持1个以太网子通道

Control channel 0 traffic statistics:

  TX: 0 packets, 0 errors

  RX: 0 packets, 0 errors

Control channel的报文收发统计信息：

·发送完成的报文数量，发送错误的报文数量

·接收的报文数量，接收错误的报文数量

PPP channel 0 traffic statistics

  TX: 0 packets, 0 errors

  RX: 0 packets, 0 errors

PPP channel的报文收发统计信息：

·发送完成的报文数量，发送错误的报文数量

·接收的报文数量，接收错误的报文数量

ETH channel 0 traffic statistics

  TX: 0 packets, 0 errors

  RX: 0 packets, 0 errors

ETH channel的报文收发统计信息：

·发送完成的报文数量，发送错误的报文数量

·接收的报文数量，接收错误的报文数量

【相关命令】

·**reset counters controller****cellular**

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- dm-port open**

------------------------------------------------------------------------

**[dm-port open**]命令用来打开3G/4G Modem的DM功能。

**[undo** **dm-port open**]命令用来关闭3G/4G Modem的DM功能。

【命令】

**[dm-port open**]

**[undo dm-port open**]

【缺省情况】

本命令的缺省情况与3G/4G Modem设备的型号有关，请以设备的实际情况为准。

【视图】

Cellular接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本命令用于在3G/4G Modem上打开或关闭DM功能。

DM（Diagnostic and Monitoring，诊断和监控），指某些类型的3G/4G Modem支持通过3G/4G Modem上的调试信息输出接口输出调试信息功能，用于连接第三方的调试工具（如高通QXDM软件）进行诊断和监控。

不同型号的3G/4G Modem对于DM功能的支持情况不同，具体使用请参考相应的3G/4G Modem用户手册。

【举例】

\# 打开3G/4G Modem的DM功能。

\<Sysname\> system-view

Sysname controller cellular 2/4/0

Sysname-Cellular2/4/0 dm-port open

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- mode**

------------------------------------------------------------------------

**[mode**]命令用来选择网络连接方式。

【命令】

**[mode**[ { **1xrtt** \| **auto** \| **evdo** \| **gsm** \| **gsm-precedence** \| **hybrid** \| **lte** \| **td** \| **td-precedence** \| **wcdma** \| **wcdma-precedence** }]]

【缺省情况】

本命令的缺省情况与3G/4G Modem设备的型号有关，请以设备的实际情况为准。

【视图】

Cellular接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[1xrtt**]：设置3G/4G Modem只选择CDMA-1x RTT网络。

**[auto**]：设置3G/4G Modem自动选择网络。

**[evdo**]：设置3G/4G Modem只选择CDMA-EVDO网络。

**[gsm**]：设置3G/4G Modem只选择GSM网络。

**[gsm-preference**]：设置3G/4G Modem优先选择GSM网络。

**[hybrid**]：设置3G/4G Modem同时选择CDMA-EVDO和CDMA-1x RTT网络。

**[lte**]：设置3G/4G Modem只选择LTE网络。

**[td**]：设置3G/4G Modem只选择TD-SCDMA网络。

**[td-preference**]：设置3G/4G Modem优先选择TD-SCDMA网络。

**[wcdma**]：设置3G/4G Modem只选择WCDMA网络。

**[wcdma-preference**]：设置3G/4G Modem优先选择WCDMA网络。

【使用指导】

本命令用于在3G/4G Modem上选择网络连接方式。

本命令中各参数的支持情况与3G/4G Modem设备的型号有关，请以设备的实际情况为准。

【举例】

\# 设置4G Modem只选择LTE网络。

\<Sysname\> system-view

Sysname controller cellular 2/4/0

Sysname-Cellular2/4/0 mode lte

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- modem reboot**

------------------------------------------------------------------------

**[modem reboot**]命令用来手动重启3G/4G Modem。

【命令】

**[modem reboot**]

【视图】

Cellular接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

3G/4G Modem在运行过程中能够自动检测异常，并实施自动重启。如果无法自动重启，用户可以通过本命令手动重启3G/4G Modem。

【举例】

\# 手动重启3G/4G Modem。

\<Sysname\> system-view

Sysname controller cellular 2/4/0

Sysname-Cellular2/4/0 modem reboot

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- modem response**

------------------------------------------------------------------------

**[modem response**]命令用来配置系统向3G/4G Modem下发配置指令后，等待其回复的时间间隔，以及3G/4G Modem连续不响应系统配置指令（配置指令失败或配置指令响应超时）次数的阈值，达到系统配置的阈值后，自动重启3G/4G Modem。

**[undo modem response**]命令用来恢复缺省情况。

【命令】

**[modem response timer** *time* **auto-recovery** *threshold*]

**[undo modem response**]

【缺省情况】

系统等待3G/4G Modem回复的时间间隔为10秒，3G/4G Modem连续不响应系统配置指令次数的阈值为3次。

【视图】

Cellular接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[timer** *time*]：系统向3G/4G Modem下发配置指令后，等待其回复的时间间隔。若在该时间内系统没收到3G/4G Modem的回复，则认为3G/4G Modem不响应系统配置指令。*time*的取值范围为1～300，单位为秒。

**[auto-recovery** *threshold*]：3G/4G Modem连续不响应系统配置指令次数的阈值，达到阈值后系统自动重启3G/4G Modem。取值范围为0～10。当*threshold*配置为0时，关闭自动重启功能。

【使用指导】

3G/4G无线网络的不稳定运行或应用环境变化可能导致3G/4G Modem功能故障，无法自动拨号并连接网络。设备提供自动重启3G/4G Modem功能，尽可能减少需要用户手工重启3G/4G Modem的情况。

开启自动重启3G/4G Modem功能后，如果连续多次下发配置指令失败或配置指令响应超时，系统将自动重启3G/4G Modem。为避免因配置错误引起的多次拨号失败，而导致的反复自动重启3G/4G Modem的情况，系统仅在上次自动重启3G/4G Modem后有过至少一次拨号成功记录，并且多次发配置指令失败或配置指令响应超时的情况下才会自动重启3G/4G Modem。

【举例】

\# 配置系统向3G/4G Modem下发配置指令时，等待其回复的时间间隔为20秒，配置3G/4G Modem模块连续4次不响应系统配置指令，则自动重启。

\<Sysname\> system-view

Sysname controller cellular 2/4/0

Sysname-Cellular2/4/0 modem response timer 20 auto-recovery 4

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- pin modify**

------------------------------------------------------------------------

**[pin modify**]命令用来修改SIM/UIM卡的PIN码，修改后的PIN码保存在SIM/UIM卡上。

【命令】

**[pin modify** *current-pin new-pin*]

【视图】

Cellular接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[current-pin*]：插在3G/4G Modem上的SIM/UIM卡的PIN码，由4～8位数字组成。

*[new-pin*]：用户重新设置的PIN码，由4～8位数字组成。

【使用指导】

本命令用于在3G/4G Modem上修改SIM/UIM卡的PIN码。

需要注意的是：

·如果开启了3G/4G Modem的PIN码认证功能，修改PIN码后，需要配置**pin verify**命令以保持和修改后的PIN码一致。

·如果连续多次修改PIN码失败，会导致SIM/UIM卡被锁。

·如果SIM/UIM卡被锁，必须先通过**pin unlock**命令来解锁。

·部分3G/4G Modem必须在启用PIN码认证，并且PIN码认证通过后才可以修改PIN码。

【举例】

\# 修改SIM/UIM卡的PIN码。

\<Sysname\> system-view

Sysname controller cellular 2/4/0

Sysname-Cellular2/4/0 pin modify 1234 4321

PIN will be changed to "4321". Continue? [Y/N:y]

PIN has been changed successfully.

【相关命令】

·**pin unlock**

·**pin verification**** enable**

·**pin verify**

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- pin unlock**

------------------------------------------------------------------------

**[pin unlock**]命令用来对3G/4G Modem上的SIM/UIM卡进行PIN码解锁。

【命令】

**[pin unlock** *puk new-pin*]

【视图】

Cellular接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[puk*]：插在3G/4G Modem上的SIM/UIM卡的PUK码，由网络提供商提供，由4～8位数字组成。

*[new-pin*]：用户重新设置的PIN码，由4～8位数字组成。重新设置的PIN码保存在SIM/UIM卡上。

【使用指导】

本命令用于在3G/4G Modem上对SIM/UIM卡进行PIN码解锁。下列情况可能导致SIM/UIM卡PIN码被锁住：

·连续多次修改PIN码失败。

·连续多次开启或关闭3G/4G Modem的PIN码认证功能失败。

·连续多次PIN码认证失败。

如果PIN码被锁住，需要用户使用PUK码将PIN码解锁，否则3G/4G Modem的数据通信功能不可用。

需要注意的是：

·如果开启了3G/4G Modem的PIN码认证功能，解锁PIN码后，需要配置**pin** **verify**命令以保持和重新设置的PIN码一致。

·如果连续多次解锁失败，可能会导致SIM/UIM卡被永久锁定，无法使用。

·如果SIM/UIM卡被永久锁定，请联系SIM/UIM卡的运营商为SIM/UIM卡解锁。

【举例】

\# 使用PUK码解锁PIN码。

\<Sysname\> system-view

Sysname controller cellular 2/4/0

Sysname-Cellular2/4/0 pin unlock 87654321 1234

PIN will be unlocked and changed to "1234". Continue? [Y/N:y]

PIN has been unlocked and changed successfully.

【相关命令】

·**pin modify**

·**pin verification**** enable**

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- pin verification enable**

------------------------------------------------------------------------

**[pin verification enable**]命令用来开启3G/4G Modem的PIN码认证功能。

**[undo pin verification enable**]命令用来关闭3G/4G Modem的PIN码认证功能。

【命令】

**[pin verification enable** [ *pin* ]]

**[undo pin verification enable** [ *pin* ]]

【缺省情况】

本命令的缺省情况与3G/4G Modem设备的型号有关，请以设备的实际情况为准。

【视图】

Cellular接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[pin*]：插在3G/4G Modem上的SIM/UIM卡的PIN码，由4～8位数字组成。

【使用指导】

本命令用于在3G/4G Modem上开启或关闭{.MsoCommentReference}PIN码认证功能。

·如果开启了3G/4G Modem的PIN码认证功能，当3G/4G Modem插入或3G/4G Modem重启时，会使用**pin** **verify**命令配置的PIN码进行认证，否则3G/4G Modem的数据通信功能不可用。重启3G/4G Modem的途径包括：重启设备、使用**modem reboot**命令重启3G/4G Modem、热拔插USB 3G/4G Modem。对于SIC-3G/4G-CDMA模块，只有设备冷启动后，才需要重新进行PIN码认证。

·如果关闭了3G/4G Modem的PIN码认证功能，不需要进行PIN码认证就可以进行3G/4G Modem数据通信。

如果开启了3G/4G Modem的PIN码认证功能，需要通过**pin** **verify**命令将PIN码保存在设备上，在需要认证时，自动完成PIN码认证。

需要注意的是：

·开启或关闭3G/4G Modem的PIN码认证功能时，可能要求输入当前的PIN码。该要求与3G/4G Modem设备的型号有关，请以设备的实际情况为准。如果连续多次开启或关闭{.MsoCommentReference}3G/4G Modem的PIN码认证功能失败，可能会导致SIM/UIM卡被锁。如果SIM/UIM卡被锁，可以通过**pin** **unlock**命令来解锁。

·部分3G/4G Modem在启用PIN码认证功能后，必须PIN码认证通过后才可以关闭PIN码认证功能。

【举例】

\# 开启PIN码认证功能。

\<Sysname\> system-view

Sysname controller cellular 2/4/0

Sysname-Cellular2/4/0 pin verification enable 1234

【相关命令】

·**pin unlock**

·**pin verify**

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- pin verify**

------------------------------------------------------------------------

**[pin verify**]命令用来配置3G/4G Modem进行认证的PIN码。

**[undo pin verify**]命令用来恢复缺省情况。

【命令】

**[pin verify**[ { **cipher** *ciphered-pin* \| **simple** *pin* }]]

**[undo pin verify**]

【缺省情况】

未配置3G/4G Modem进行认证的PIN码。

【视图】

Cellular接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cipher**]：表示以密文形式输入密码。

*[ciphered-pin*]：插在3G/4G Modem上的SIM/UIM卡的密文PIN码，由37～41个字符的字符串组成。

**[simple**]：表示以明文形式输入密码。

*[pin*]：插在3G/4G Modem上的SIM/UIM卡的明文PIN码，由4～8位数字组成。

【使用指导】

开启了3G/4G Modem的PIN码认证功能后，当3G/4G Modem插入或重启时，需要通过**pin** **verify**命令输入PIN码进行认证，如果输入的PIN码正确，则PIN码认证通过，否则，PIN码认证失败。如果连续多次PIN码认证失败，可能会导致SIM/UIM卡被锁。如果SIM/UIM卡被锁，可以通过**pin** **unlock**命令来解锁。

用户可以在需要PIN码认证时配置**pin** **verify**命令，也可以提前配置**pin** **verify**命令，只要配置一次**pin** **verify**命令，PIN码就会保存在设备上，在需要认证时，自动完成PIN码认证。

【举例】

#  配置3G/4G Modem进行认证的PIN码。

\<Sysname\> system-view

Sysname controller cellular 2/4/0

Sysname-Cellular2/4/0 pin verify simple 1234

【相关命令】

·**pin unlock**

·**pin verification****enable**

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- plmn search**

------------------------------------------------------------------------

**[plmn search**]命令用来搜索移动网络。

【命令】

**[plmn search**]

【视图】

Cellular接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本命令用于触发3G/4G Modem搜索移动网络。

搜索移动网络需要等待几分钟，完成搜索后，命令行会给出提示，显示搜索到的移动网络。

3G/4G Modem使用时，需要在PLMN（Public Land Mobile Network，公共陆地移动网络）进行选择接入的移动网络。如果用户需要手工指定接入的移动网络，则需要先搜索移动网络，获取当前区域内有信号的移动网络列表。

【举例】

\# 搜索移动网络。

\<Sysname\> system-view

Sysname controller cellular 2/4/0

Sysname-Cellular2/4/0 plmn search

PLMN search done.

Available PLMNs:

PLMN No.     MCC    MNC    Status     Type

01           460    00     Current    GSM

02           460    00     Available  UTRAN

03           460    01     Forbidden  GSM

表1-6 plmn search命令显示信息描述表

字段

描述

PLMN No

序号

MCC

移动国家编码

MNC

移动网络编码，表示运营商，比如：

·00、02、07：表示移动

·01：表示联通

·03：表示电信

Status

移动网络的状态，其取值及含义如下：

·Current：表示当前正在使用的网络

·Available：表示网络可达

·Forbidden：表示网络被禁止使用

Type

搜索到的移动网络类型

【相关命令】

·**display cellular**

·**plmn select**

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- plmn select**

------------------------------------------------------------------------

**[plmn select**]命令用来配置选择移动网络的方式。

【命令】

**[plmn select****auto**[\| **manual** *mcc mnc* }]

【缺省情况】]

本命令的缺省情况与3G/4G Modem设备的型号有关，请以设备的实际情况为准。

【视图】

Cellular接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[auto**]：表示自动选择PLMN（Public Land Mobile Network，公共地带移动网络）。

**[manual**]：表示人工指定PLMN。

*[mcc*]：MCC（Mobile Country Code，移动国家编码），取值范围为0～65535。

*[mnc*]：MNC（Mobile Network Code，移动网络编码），取值范围为0～65535。

【使用指导】

本命令用于在3G/4G Modem上配置选择移动网络的方式。

当配置选择移动网络的方式为人工指定时，需要先通过**plmn search**命令搜索移动网络。

【举例】

\# 配置选择移动网络的方式为人工指定。

\<Sysname\> system-view

Sysname controller cellular 2/4/0

Sysname-Cellular2/4/0 plmn select manual 65524 65524

【相关命令】

·**display cellular**

·**plmn search**

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- profile create**

------------------------------------------------------------------------

**[profile create**]命令用来创建3G/4G Modem的参数模板。

【命令】

**[profile create*** profile-number *[{ **dynamic** \| **static** *apn* } **authentication-mode** { **none** \| { **chap** \| **pap** } **user** *username* [ **password** *password* ] }]]

【缺省情况】

本命令的缺省情况与3G/4G Modem设备的型号有关，请以设备的实际情况为准。

【视图】

Cellular接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[profile-number*]：3G/4G Modem的参数模板编号。不同型号的3G/4G Modem设备支持的取值范围不同，请以设备的实际情况为准。

**[dynamic**]：由运营商根据接入用户动态分配接入点。

**[static*** apn*]：指定的由运营商提供的接入点名称，为1～100个字符的字符串，是否大小写敏感和运营商有关。

**[authentication-mode**]：认证方式。

**[none**]：不认证。

**[chap**]：认证方式为CHAP。

**[pap**]：认证方式为PAP。

**[user*** username*]：认证用户名，由运营商提供。为1～32个字符的字符串，区分大小写。

**[password*** password*]：认证密码，由运营商提供。为1～32个字符的字符串，区分大小写。

【使用指导】

本命令用于在3G/4G Modem上创建参数模板。

参数模板可以配置接入点和认证方式，3G/4G Modem会根据配置的接入点和认证方式，来和对应的服务商进行认证：

·当选用None方式时，不需要输入用户名和密码。

·当选用CHAP或PAP方式时，需要根据运营商的要求，选择配置用户名和密码，其中*username*字段是必选的，而*password*字段是可选的。

【举例】

\# 创建3G/4G Modem的参数模板1，指定的接入点名称为cmnet，认证方式采用PAP。

\<Sysname\> system-view

Sysname controller cellular 2/4/0

Sysname-Cellular2/4/0 profile create 1 static cmnet authentication-mode pap user abc password abc

【相关命令】

·**display cellular**

·**profile delete**

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- profile delete**

------------------------------------------------------------------------

**[profile delete**]命令用来删除3G/4G Modem的参数模板。

【命令】

**[profile delete** *profile-number*]

【视图】

Cellular接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[profile-number*]：3G/4G Modem的参数模板编号。不同型号的3G/4G Modem设备支持的取值范围不同，请以设备的实际情况为准。

【举例】

\# 删除3G/4G Modem的参数模板1。

\<Sysname\> system-view

Sysname controller cellular 2/4/0

Sysname-Cellular2/4/0 profile delete 1

【相关命令】

·**display cellular**

·**profile**** create**

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- profile main**

------------------------------------------------------------------------

**[profile main**]命令用来配置3G/4G Modem拨号使用的主备参数模板。

**[undo profile main**]命令用来恢复缺省情况。

【命令】

**[profile main **]*main-profile-number ***backup***backup-profile-number*

**[undo profile main**]

【缺省情况】

3G/4G Modem使用参数模板1进行拨号。

【视图】

Cellular接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[main-profile-numbe*]：主参数模板索引。不同型号的3G/4G Modem设备支持的取值范围不同，请以设备的实际情况为准。

**[backup**]*backup-profile-number*：备份参数模板索引。不同型号的3G/4G Modem设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

配置**profile main**命令后，3G/4G Modem每次拨号都优先选择主参数模板，如果主参数模板拨号失败，将使用备份参数模板进行拨号。无论备份参数模板拨号是否成功，下次拨号时都使用主参数模板拨号。

需要注意的是：

·使用的主备参数模板的用户名和密码必须配成一样的。

·本命令的配置会在下次拨号时生效，不会影响当前的拨号结果。

【举例】

\# 配置3G/4G Modem拨号使用主参数模板1，备份参数模板2。

\<Sysname\> system-view

Sysname controller cellular 2/4/0

Sysname-Cellular2/4/0 profile main 1 backup 2

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- reset counters controller cellular**

------------------------------------------------------------------------

**[reset counters controller cellular**]命令用来清除Cellular接口的统计信息。

【命令】

**[reset counters controller** **cellular** [ *interface-number* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-number*]：Cellular接口的编号。

【使用指导】

在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。

·如果不指定*interface-number*，则清除所有Cellular接口的统计信息；

·如果指定*interface-number*，则清除指定Cellular接口的统计信息。

【举例】

\# 清除接口Cellular2/4/0的统计信息。

\<Sysname\> reset counters controller cellular 2/4/0

【相关命令】

·**display controller cellular**

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- sendat**

------------------------------------------------------------------------

**[sendat**]命令用来手工向3G/4G Modem发送配置指令。

【命令】

**[sendat** *at-string*]

【视图】

Cellular接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[at-string*]：配置指令字符串，为1～300个字符的字符串。该字符串的内容格式不同产品有所区别，可能是AT指令（"+++"和"A/"以及任意以AT开头的字符串，AT指令的详细解释请参见"二层技术-广域网接入命令参考/Modem管理"中的命令**sendat**），也可能是CNS格式的报文（样例请参见[表]1-7(?-361739400#_Ref329768282)）\_Ref310583627(#_Ref310583627)。本参数的具体格式与设备的型号有关，请以设备的实际情况为准。

表1-7 CNS格式报文举例

指令

说明

**[CNS***n*]

控制CNS心跳检测开关

·*n = *00000500000000000000，打开CNS心跳检测开关

·*n = *00000800000000000000，关闭CNS心跳检测开关

【使用指导】

**[sendat**]命令不检查配置指令的合法性，直接将用户输入的字符串送至3G/4G Modem（遇到小写字母自动转化为大写字母）。

需要注意的是：

·**sendat**命令一次只能配置一条配置指令。

·通过配置指令配置3G/4G Modem后，3G/4G Modem的工作状态会被改变，有可能导致3G/4G Modem的状态混乱从而影响到拨号等基本功能。请在专业人员的指导下慎重使用此功能。

【举例】

\# 向3G/4G Modem发送拨号指令，呼叫号码169。

\<Sysname\> system-view

Sysname controller cellular 2/4/0

Sysname-Cellular2/4/0 sendat ATD169

\# 向3G/4G Modem发送打开CNS心跳检测开关的指令。

\<Sysname\> system-view

Sysname controller cellular 2/4/0

Sysname-Cellular2/4/0 sendat cns00000500000000000000

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- shutdown**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭Cellular接口。

**[undo** **shutdown**]命令用来打开Cellular接口。

【命令】

**[shutdown**]

**[undo shutdown**]

【缺省情况】

Cellular接口处于打开状态。

【视图】

Cellular接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 关闭接口Cellular2/4/0。

\<Sysname\> system-view

Sysname interface cellular 2/4/0

Sysname-Cellular2/4/0 shutdown

**3G/4G Modem管理 \-- 3G Modem管理专用配置命令 \-- serial-set**

------------------------------------------------------------------------

**[serial-set**]命令用来将Cellular接口通道化出同/异步串口。

**[undo serial-set**]命令用来将Cellular接口通道化出的同/异步串口删除。

【命令】

**[serial-set** *set-number*]

**[undo serial-set** *set-number*]

【视图】

Cellular接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[set-number*]：通道化出的串口的编号。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。

【使用指导】

Cellular接口在配置该命令后通道化出一个Serial接口，接口名是**serial** *cellular-number*:*set-number*。

【举例】

\# 将接口Cellular2/4/0通道化出一个Serial接口。

\<Sysname\> system-view

Sysname controller cellular 2/4/0

Sysname-Cellular2/4/0 serial-set 0

**3G/4G Modem管理 \-- 4G Modem管理专用配置命令 \-- bandwidth**

------------------------------------------------------------------------

**[bandwidth**]命令用来配置接口的期望带宽。

**[undo bandwidth**]命令用来恢复缺省情况。

【命令】

**[bandwidth**]*bandwidth-value*

**[undo bandwidth**]

【缺省情况】

接口的期望带宽＝接口的波特率÷1000（kbit/s）。

【视图】

以太网通道接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth-value*]：表示接口的期望带宽，取值范围为1～400000000，单位为kbit/s。

【使用指导】

接口的期望带宽会影响链路开销值，具体介绍请参见"三层技术-IP路由配置指导"中的"OSPF"OSPFv3"和"IS-IS"。

【举例】

\# 设置以太网通道接口Eth-channel2/4/0:0的期望带宽为1000kbit/s。

\<Sysname\> system-view

Sysname interface eth-channel 2/4/0:0

Sysname-Eth-channel2/4/0:0 bandwidth 1000

**3G/4G Modem管理 \-- 4G Modem管理专用配置命令 \-- default**

------------------------------------------------------------------------

**[default**]命令用来恢复当前接口的缺省配置。

【命令】

**[default**]

【视图】

以太网通道接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。

您可以在执行**default**命令后通过**display this**命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。

【举例】

\# 将以太网通道接口Eth-channel2/4/0:0恢复为缺省配置。

\<Sysname\> system-view

Sysname interface eth-channel 2/4/0:0

Sysname-Eth-channel2/4/0:0 default

**3G/4G Modem管理 \-- 4G Modem管理专用配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来设置当前接口的描述信息。

**[undo description**]命令用来恢复缺省情况。

【命令】

**[description** *text*]

**[undo description**]

【缺省情况】

接口的描述信息为"*该接口的接口名* Interface"，比如"Echannel2/4/0:0 Interface"。

【视图】

以太网通道接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：接口描述信息，为1～255个字符的字符串，区分大小写。

【使用指导】

可以根据需要修改接口的描述。

修改后的描述信息会在**display interface**显示的接口信息中体现。

【举例】

\# 设置以太网通道接口Eth-channel2/4/0:0的描述信息为"Echannel-interface"。

\<Sysname\> system-view

Sysname interface eth-channel 2/4/0:0

Sysname-Eth-channel2/4/0:0 description Echannel-interface

**3G/4G Modem管理 \-- 4G Modem管理专用配置命令 \-- display interface eth-channel**

------------------------------------------------------------------------

**[display interface eth-channel**]命令用来显示以太网通道接口的相关信息。

【命令】

**[display interface** [ **eth-channel** [ *channel-id*    **brief** [ **description** \| **down** ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[channel-id*]：以太网通道接口的编号。

**[brief**]：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。

**[description**]：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过27个字符，不指定该参数时，只显示描述信息中的前27个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。

**[down**]：显示当前物理状态为down的接口的信息以及down的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。

【使用指导】

·如果不指定**eth-channel**参数，将显示设备支持的所有接口的相关信息；

·如果指定**eth-channel**参数，不指定*channel-id*参数，将显示所有已通道化的以太网通道接口的相关信息。

【举例】

\# 显示以太网通道接口Eth-channel2/4/0:0的详细信息。

\<Sysname\> display interface eth-channel 2/4/0:0

Echannel2/4/0:0

Current state: DOWN

Line protocol state: DOWN

Description: Echannel2/4/0:0 Interface

Bandwidth: 100000kbps

Maximum Transmit Unit: 1500

Internet protocol processing: disabled

IP Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: 000c-2963-b75d

IPv6 Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: 000c-2963-b75d

Output queue - Urgent queuing: Size/Length/Discards 0/100/0

Output queue - Protocol queuing: Size/Length/Discards 0/500/0

Output queue - FIFO queuing: Size/Length/Discards 0/75/0

Last link flapping: Never

Last clearing of counters: Never

Last 300 seconds input rate 0.00 bytes/sec, 0.00 packets/sec

Last 300 seconds output rate 0.00 bytes/sec, 0.00 packets/sec

Input: 0 packets, 0 bytes, 0 buffers

Output:0 packets, 0 bytes

\# 显示以太网通道接口Eth-channel2/4/0:0的概要信息。

\<Sysname\> display interface eth-channel 2/4/0:0 brief

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Protocol: (s) - spoofing

Interface            Link Protocol Main IP         Description

Echannel2/4/0:0      UP   UP(s)    192.168.80.239

\# 显示当前物理状态为down的以太网通道接口的信息以及down的原因。

\<Sysname\> display interface eth-channel brief down

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Interface            Link Cause

Echannel2/4/0:0      ADM  Administratively

表1-8 display interface eth-channel命令显示信息描述表

字段

描述

Current state

接口当前的物理状态和管理状态，可能的取值及含义如下：

·Administratively DOWN：表示该接口已经通过**shutdown**命令被关闭，即管理状态为关闭

·DOWN：表示该接口的管理状态为开启，但物理状态为关闭（可能因为没有物理连线或者线路故障）

·UP：该接口的管理状态和物理状态均为开启

Line protocol state

接口的链路层协议状态，由链路层经过参数协商决定，取值为：

·UP：表示数据链路层协议状态为开启

·DOWN：表示数据链路层协议状态为关闭

·UP(spoofing)：表示该接口的数据链路层协议状态为开启，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立

Description

接口的描述信息

Bandwidth

接口的期望带宽

Maximum Transmit Unit

接口允许通过的最大传输单元

Internet protocol processing: disabled

接口当前不能处理IP报文

Internet Address is 192.168.1.200/24 Primary

接口的主IP地址，此IP地址由运营商自动分配

IP Packet Frame Type，Hardware Address

IP报文发送帧格式，硬件地址

IPv6 Packet Frame Type，Hardware Address

IPv6报文发送帧格式，硬件地址

Output queue - Urgent queuing: Size/Length/Discards

输出队列的紧急队列中当前的消息数/最大可容纳的消息数/已丢弃的消息数。该显示信息的支持情况与设备的型号有关，请以设备的实际情况为准

Output queue - Protocol queuing: Size/Length/Discards

输出队列的协议队列中当前的消息数/最大可容纳的消息数/已丢弃的消息数。该显示信息的支持情况与设备的型号有关，请以设备的实际情况为准

Output queue - FIFO queuing: Size/Length/Discards

输出队列的先进先出队列中当前的消息数/最大可容纳的消息数/已丢弃的消息数。该显示信息与用户的配置有关，当配置为CBQ、WFQ等队列时则显示为CBQ/WFQ等队列的消息数。该显示信息的支持情况与设备的型号有关，请以设备的实际情况为准

Last link flapping

接口最近一次物理状态改变到现在的时长。Never表示接口从设备启动后一直处于down状态（没有改变过）

Last clearing of counters

最近一次使用**reset counters interface**命令清除接口下的统计信息的时间。如果从设备启动一直没有执行**reset counters interface**命令清除过该接口下的统计信息，则显示Never

Last 300 seconds input rate

最近300秒钟的平均输入速率：bytes/sec表示平均每秒输入的字节数，bits/sec表示平均每秒输入的比特数，packets/sec表示平均每秒输入的包数

Last 300 seconds output rate

最近300秒钟的平均输出速率：bytes/sec表示平均每秒输出的字节数，bits/sec表示平均每秒输出的比特数，packets/sec表示平均每秒输出的包数

Input: 0 packets, 0 bytes, 0 buffers

输入报文：报文数，字节数，缓存单元的个数

Output:0 packets, 0 bytes

输出报文：报文数，字节数

Brief information on interface(s) under route mode:

三层模式下（route）接口的概要信息，即三层接口的概要信息

Link: ADM - administratively down; Stby - standby

·如果某接口的Link属性值为"ADM"，则表示该接口被管理员手工关闭了，需要在该接口下执行**undo shutdown**命令才能恢复接口本身的物理状态

·如果某接口的Link属性值为"Stby"，则表示该接口是一个备份接口，使用**display interface-backup state**命令可以查看该备份接口对应的主接口

Protocol: (s) - spoofing

如果某接口的Protocol属性值中带有"(s)"，则表示该接口的数据链路层协议状态显示为UP，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的

Interface

接口名称缩写

Iink

接口物理连接状态，取值可能为：

·UP：表示接口物理上是连通的

·DOWN：表示接口物理上不通

·ADM：表示接口被手工关闭了，需要执行**undo shutdown**命令才能打开接口

·Stby：表示该接口是一个备份接口

Protocol

接口数据链路层协议状态，取值可能为：

·UP：表示接口的数据链路层是连通的

·DOWN：表示接口的数据链路层不通

·UP(s)：表示接口的数据链路层协议状态显示为UP，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的

Main IP

接口主IP地址

Description

用户通过**description**命令给接口配置的描述信息。使用**display interface brief**命令，不指定**description**参数时，该字段最多显示27个字符；指定**description**参数时，可显示配置的全部描述信息

Cause

接口物理连接状态为down的原因，取值为Administratively时表示本链路被手工关闭了（配置了**shutdown**命令），需要执行**undo shutdown**命令才能恢复真实的物理状态

**3G/4G Modem管理 \-- 4G Modem管理专用配置命令 \-- eth-channel**

------------------------------------------------------------------------

**[eth-channel**]命令用来将Cellular接口通道化出以太网通道接口。

**[undo eth-channel**]命令用来将Cellular接口通道化出的以太网通道接口删除。

【命令】

**[eth-channel ***channel-number*]

**[undo eth-channel ***channel-number*]

【视图】

Cellular接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[channel-number*]：通道化出的以太网通道接口编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

Cellular接口在配置该命令后通道化出一个以太网通道接口，接口名是**eth-channel** *cellular-number*:*channel-number*。

【举例】

\# 将接口Cellular2/4/0通道化出一个以太网通道接口。

\<Sysname\> system-view

Sysname controller cellular 2/4/0

Sysname-Cellular2/4/0 eth-channel 0

**3G/4G Modem管理 \-- 4G Modem管理专用配置命令 \-- interface eth-channel**

------------------------------------------------------------------------

**[interface eth-channel**]命令用来进入以太网通道接口视图。

【命令】

**[interface eth-channel** *interface-number*]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-number*]：以太网通道接口的编号。

【举例】

\# 进入以太网通道接口Eth-channel2/4/0:0的视图。

\<Sysname\> system-view

Sysname interface eth-channel 2/4/0:0

Sysname-Eth-channel2/4/0:0

**3G/4G Modem管理 \-- 4G Modem管理专用配置命令 \-- ip address cellular-alloc**

------------------------------------------------------------------------

**[ip address cellular-alloc**]命令用来配置接口通过Modem私有协议获取IP地址。

**[undo ip address cellular-alloc**]命令用来恢复缺省情况。

【命令】

**[ip address cellular-alloc**]

**[undo ip address cellular-alloc**]

【缺省情况】

接口不通过Modem私有协议获取IP地址。

【视图】

以太网通道接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

**[ip address cellular-alloc**]与**ip address dhcp-alloc**命令用于设置接口以何种方式从Modem获取接口IP地址，Modem的IP地址由运营商自动分配。

其中，**ip address cellular-alloc**命令是配置接口采用Modem私有协议获取IP地址，而**ip address dhcp-alloc**命令是配置接口采用标准DHCP协议获取IP地址。

【举例】

\# 为接口Cellular2/4/0创建以太网通道接口，并采用Modem私有协议获取运营商自动分配的IP地址。

\<Sysname\> system-view

Sysname controller cellular 2/4/0

Sysname-Cellular2/4/0 eth-channel 0

Sysname-Cellular2/4/0 quit

Sysname interface eth-channel 2/4/0:0

Sysname-Eth-channel2/4/0:0 ip address cellular-alloc

**3G/4G Modem管理 \-- 4G Modem管理专用配置命令 \-- mtu**

------------------------------------------------------------------------

**[mtu**]命令用来配置接口的MTU（Maximum Transmission Unit，最大传输单元）值。

**[undo mtu**]命令用来恢复缺省情况。

【命令】

**[mtu** *size*]

**[undo mtu**]

【缺省情况】

接口的MTU值为1500字节。

【视图】

以太网通道接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size*]：接口的MTU值，单位为字节。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【举例】

\# 配置以太网通道接口Eth-channel2/4/0:0的MTU值为1430字节。

\<Sysname\> system-view

Sysname interface eth-channel 2/4/0:0

Sysname-Eth-channel2/4/0:0 mtu 1430

**3G/4G Modem管理 \-- 4G Modem管理专用配置命令 \-- reset counters interface**

------------------------------------------------------------------------

**[reset counters interface**]命令用来清除以太网通道接口的统计信息。

【命令】

**[reset counters interface ** **eth-channel**  *channel-id*  ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[eth-channel**]：清除以太网通道接口的统计信息。

*[channel-id*]：以太网通道接口的编号。

【使用指导】

在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。

·如果不指定**eth-channel**和*channel-id*，则清除所有接口的统计信息；

·如果指定**eth-channel**而不指定*channel-id*，则清除所有以太网通道接口的统计信息；

·如果同时指定**eth-channel**和*channel-id*，则清除指定以太网通道接口的统计信息。

【举例】

\# 清除以太网通道接口Eth-channel2/4/0:0的统计信息。

\<Sysname\> reset counters interface eth-channel 2/4/0:0

**3G/4G Modem管理 \-- 4G Modem管理专用配置命令 \-- shutdown**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭以太网通道接口。

**[undo** **shutdown**]命令用来打开以太网通道接口。

【命令】

**[shutdown**]

**[undo shutdown**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

以太网通道接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 关闭以太网通道接口Eth-channel2/4/0:0。

\<Sysname\> system-view

Sysname interface eth-channel 2/4/0:0

Sysname-Eth-channel2/4/0:0 shutdown

