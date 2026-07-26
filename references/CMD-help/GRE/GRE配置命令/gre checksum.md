
**GRE \-- GRE配置命令 \-- gre checksum**

------------------------------------------------------------------------

**[gre checksum**]命令用来开启GRE报文校验和功能。

**[undo gre checksum**]命令用来关闭GRE报文校验和功能。

【命令】

**[gre checksum**]

**[undo gre checksum**]

【缺省情况】

GRE报文校验和功能处于关闭状态。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

通过GRE校验和验证可以检查报文的完整性。

隧道两端可以根据各自的实际应用需要决定是否要开启GRE报文校验和功能。如果发送方开启了GRE报文校验和功能，则会根据GRE头及Payload信息计算校验和，并将包含校验和信息的报文发送给对端。接收方对收到的报文计算校验和，并与报文中的校验和比较，如果一致则对报文进行进一步处理，否则丢弃该报文。

需要注意的是，接收方是否对收到的报文进行校验和验证，取决于报文中是否携带校验和信息，与接收方的配置无关。

【举例】

\# 开启GRE报文校验和功能。

\<Sysname\> system-view

Sysname interface tunnel 2 mode gre

Sysname-Tunnel2 gre checksum

**GRE \-- GRE配置命令 \-- gre key**

------------------------------------------------------------------------

**[gre key**]命令用来设置GRE类型Tunnel接口的GRE Key。

**[undo gre key**]命令用来取消GRE类型Tunnel接口的GRE Key。

【命令】

**[gre key** *key-number*]

**[undo gre key**]

【缺省情况】

没有设置GRE类型Tunnel接口的GRE Key。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[key-number*]：GRE类型Tunnel接口的GRE Key，取值范围为0～4294967295。

【使用指导】

通过设置GRE类型Tunnel接口的GRE Key，可以防止设备接收非法报文。

配置了GRE Key后，发送方会在其发送的报文中携带GRE Key信息。接收方收到报文后将报文中的GRE Key与接收方本地配置的GRE Key进行比较，如果一致则对报文进行进一步处理；否则丢弃该报文。

隧道两端必须设置相同的GRE Key，或者都不设置GRE Key。

【举例】

\# 设置GRE类型Tunnel接口的GRE Key为123。

\<Sysname\> system-view

Sysname interface tunnel 2 mode gre

Sysname-Tunnel2 gre key 123

**GRE \-- GRE配置命令 \-- keepalive**

------------------------------------------------------------------------

**[keepalive**]命令用来开启GRE的keepalive功能，并配置keepalive报文发送周期及最大发送次数。

**[undo keepalive**]命令用来关闭GRE的keepalive功能。

【命令】

**[keepalive ** *interval*  *times*  ]

**[undo keepalive**]

【缺省情况】

GRE的keepalive功能处于关闭状态。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：keepalive报文发送周期，取值范围为1～32767，单位为秒，缺省值为10秒。

*[times*]：keepalive报文的最大传送次数，取值范围为1～255，缺省值为3次。

【使用指导】

开启GRE的keepalive功能后，设备会以*interval*为周期从Tunnel接口发送GRE的keepalive报文。如果连续发送*times*个keepalive报文后，仍然没有收到隧道对端的回应，则把本端Tunnel接口的状态置为down。如果Tunnel接口为down状态时，收到对端回复的keepalive确认报文，则Tunnel接口的状态将转换为up，否则保持down状态。

需要注意的是，不论设备上是否开启了GRE的keepalive功能，设备接收到keepalive报文后，都会对其进行应答。

模式为GRE over IPv6隧道的Tunnel接口不支持本命令。

【举例】

\# 开启GRE的keepalive功能，并配置keepalive报文发送周期为20秒，最大传送次数为5次。

\<Sysname\> system-view

Sysname interface tunnel 2 mode gre

Sysname-Tunnel2 keepalive 20 5
