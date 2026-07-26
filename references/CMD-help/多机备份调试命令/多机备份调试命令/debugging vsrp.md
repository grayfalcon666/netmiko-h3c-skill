::: {#-1786217777 .myid}
[]{#_Toc404795981}[]{#struct_0_x6987_95089_1025468949}[]{#_Toc154894621}

**多机备份调试命令 \-- 多机备份调试命令 \-- debugging vsrp**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6987_95089_1262475312}

[**[debugging vsrp]{lang="EN-US"}**]{#struct_0_x6987_95089_x2088068530}

[**[undo debugging vsrp]{lang="EN-US"}**]{#struct_0_x6987_95089_1629925128}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6987_95089_x1001073431}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x6987_95089_613110104}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6987_95089_x1681620322}

[[network-admin]{lang="EN-US"}]{#struct_0_x6987_95089_1612170077}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6987_95089_608961802}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x6987_95089_x457985043}

[**[debugging vsrp]{lang="EN-US"}**]{#struct_0_x6987_95089_712420323}[命令用来打开多机备份调试信息开关。]{style="font-family:宋体"}**[undo debugging vsrp]{lang="EN-US"}**[命令用来关闭多机备份调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，多机备份调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x6987_95089_x1290766358}

[[表1-1 ]{lang="EN-US"}[debugging vsrp]{lang="EN-US"}]{#struct_0_x6987_95089_x1107738296}[命令输出信息列表]{style="font-family:黑体"}

[]{#table_struct_0_946214777}[[字段]{style="font-family:黑体"}]{#struct_0_x6987_95089_902143832}
:::

[[含义]{style="font-family:黑体"}]{#struct_0_x6987_95089_x1649150498}

[[The node with backup ID *backup-id* was deleted from the retransmission list: data length*: data-length*, list node total number: *total-num*, VSRP peer name*: peer-name*.]{lang="EN-US"}]{#struct_0_x6987_95089_x999347403}

[[删除重传链中编号为]{style="font-family:宋体"}*[backup-id]{lang="EN-US"}*]{#struct_0_x6987_95089_x848520609}[结点，该结点数据长度为]{style="font-family:宋体"}*[data-length]{lang="EN-US"}*[，该重传链结点个数为]{style="font-family:宋体"}*[node-num]{lang="EN-US"}*[，该重传链所属的]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[对端名为：]{style="font-family:宋体"}*[peer-name]{lang="EN-US"}*

[[The node with backup ID *backup-id* was refreshed in the retransmission list: data length: *data-length*, list node total number: *total-num*, VSRP peer name: *peer-name*.]{lang="EN-US"}]{#struct_0_x6987_95089_x364113617}

[[更新重传链中编号为]{style="font-family:宋体"}*[backup-id]{lang="EN-US"}*]{#struct_0_x6987_95089_x540614992}[结点，该结点数据长度为]{style="font-family:宋体"}*[data-length]{lang="EN-US"}*[，该重传链结点个数为]{style="font-family:宋体"}*[node-num]{lang="EN-US"}*[，该重传链所属的]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[对端名为：]{style="font-family:宋体"}*[peer-name]{lang="EN-US"}*

[[The status of VSRP instance name *instance-name* changed to *new-status*.]{lang="EN-US"}]{#struct_0_x6987_95089_1167081260}

[[VSRP]{lang="EN-US"}]{#struct_0_x6987_95089_x1980577683}[实例]{style="font-family:宋体"}*[instance-name]{lang="EN-US"}*[的状态变化为]{style="font-family:宋体"}*[new-status]{lang="EN-US"}*[，状态取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Master]{lang="EN-US"}]{#struct_0_x6987_95089_x565663654}[：表示主]{lang="EN-US" style="font-family:宋体"}[用设备]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backup]{lang="EN-US"}]{#struct_0_x6987_95089_188317531}[：表示备用设备]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_x6987_95089_1586871899}[：表示]{lang="EN-US" style="font-family:宋体"}[设备]{style="font-family:宋体"}[不可用]{lang="EN-US" style="font-family:宋体"}

[[The TCP connection status of VSRP peer *peer-name* changed, new TCP connection status: *tcp-status*.]{lang="EN-US"}]{#struct_0_x6987_95089_x137330465}

[[VSRP]{lang="EN-US"}]{#struct_0_x6987_95089_1087234616}[对端]{style="font-family:宋体"}*[peer-name]{lang="EN-US"}*[的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[状态变为]{style="font-family:宋体"}*[tcp-status]{lang="EN-US"}*[，取值包含：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disconnected]{lang="EN-US"}]{#struct_0_x6987_95089_473516575}[：连接已断开]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Connected]{lang="EN-US"}]{#struct_0_x6987_95089_x809518932}[：连接已建立]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6987_95089_1688835610}

[[\# ]{lang="EN-US"}]{#struct_0_x6987_95089_x1698185871}[刷新多机备份对端]{style="font-family:宋体"}[pname]{lang="EN-US"}[内]{style="font-family:宋体"}[Backup ID]{lang="EN-US"}[为]{style="font-family:宋体"}[207]{lang="EN-US"}[的重传链结点。]{style="font-family:宋体"}

[[\<Sysname\> debugging vsrp]{lang="EN-US"}]{#struct_0_x6987_95089_x97839410}

[\<Sysname\> \*May 25 10:26:08:418 2013 Sysname VSRP/7/DEBUG: -MDC=1; The node with backup ID 207 was refreshed in the retransmission list, data length: 20, list node total number: 1024, VSRP peer name: pname.]{lang="EN-US"}

[[\# VSRP ]{lang="EN-US"}]{#struct_0_x6987_95089_1986188426}[对端]{style="font-family:宋体"}[pname]{lang="EN-US"}[的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[状态由]{style="font-family:宋体"}[Connetced]{lang="EN-US"}[变成]{style="font-family:宋体"}[Disconnected]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> debugging vsrp]{lang="EN-US"}]{#struct_0_x6987_95089_x1703414406}

[\<Sysname\> \*May 25 09:06:11:953 2013 H3C VSRP/7/DEBUG: -MDC=1; The TCP connection status of]{lang="EN-US"}

[ VSRP peer pname changed, new TCP connection status: Disconnected.]{lang="EN-US"}

[[\# VSRP ]{lang="EN-US"}]{#struct_0_x6987_95089_x2094540050}[实例]{style="font-family:宋体"}[aaa]{lang="EN-US"}[的状态变成]{style="font-family:宋体"}[Down]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> debugging vsrp]{lang="EN-US"}]{#struct_0_x6987_95089_x1784758657}

[\<Sysname\> \*May 25 09:11:44:649 2013 H3C VSRP/7/DEBUG: -MDC=1; The status of VSRP ]{lang="EN-US"}

[instance name aaa changed to Down.]{lang="EN-US"}

::: {#1708650339 .myid}
[]{#_Toc404795983}[]{#struct_0_x6987_95089_x67632394}[]{#_Toc375317953}[]{#_Toc359232863}[]{#_Toc357684241}[]{#_Toc353278231}

**多机备份调试命令 \-- PPPoE支持多机备份功能调试命令 \-- debugging ppp vsrp**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6987_95089_x1121338980}

[**[debugging ppp vsrp]{lang="EN-US"}**]{#struct_0_x6987_95089_x6179469}

[**[undo debugging ppp vsrp]{lang="EN-US"}**]{#struct_0_x6987_95089_x2010784485}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6987_95089_x1571645828}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x6987_95089_x890585706}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6987_95089_x1120880228}

[[network-admin]{lang="EN-US"}]{#struct_0_x6987_95089_x1556070068}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6987_95089_1470811442}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6987_95089_425574248}

[**[debugging ppp vsrp]{lang="EN-US"}**]{#struct_0_x6987_95089_x1120945764}[命令用来打开]{style="font-family:宋体"}[PPP]{lang="EN-US"}[的多机备份调试信息开关。]{style="font-family:宋体"}**[undo debugging ppp vsrp]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[PPP]{lang="EN-US"}[的多机备份调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x6987_95089_2086246559}[的多机备份调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-2 ]{lang="EN-US"}[debugging ppp vsrp]{lang="EN-US"}]{#struct_0_x6987_95089_x1519889438}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1708102976}[[字段]{style="font-family:黑体"}]{#struct_0_x6987_95089_x1121011300}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6987_95089_x1490958993}

[[Received a bind VSRP event: interface=*interface-name*, VSRP instance=*vsrp-instance-name*.]{lang="EN-US"}]{#struct_0_x6987_95089_x1121076836}

[[PPP]{lang="EN-US"}]{#struct_0_x6987_95089_x565110340}[收到接口绑定事件，接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[绑定的多机备份实例名为]{style="font-family:宋体"}*[vsrp-instance-name]{lang="EN-US"}*

[[Received an unbind VSRP event: interface=*interface-name*, VSRP instance=*vsrp-instance-name*.]{lang="EN-US"}]{#struct_0_x6987_95089_x1120618084}

[[PPP]{lang="EN-US"}]{#struct_0_x6987_95089_1678570147}[收到接口去绑定事件，接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[去绑定的多机备份实例名为]{style="font-family:宋体"}*[vsrp-instance-name]{lang="EN-US"}*

[[Received a VSRP status event: VSRP instance=*vsrp-instance-name*, from *OldStatus* to *NewStatus.*]{lang="EN-US"}]{#struct_0_x6987_95089_x1120683620}

[[PPP]{lang="EN-US"}]{#struct_0_x6987_95089_x1588271584}[收到实例]{style="font-family:宋体"}*[vsrp-instance-name]{lang="EN-US"}*[状态变化事件，其中]{style="font-family:宋体"}*[OldStatus]{lang="EN-US"}*[和]{style="font-family:宋体"}*[NewStatus]{lang="EN-US"}*[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Master]{lang="IT"}]{#struct_0_x6987_95089_x1012693400}[：]{lang="EN-US" style="font-family:宋体"}[实例状态为主]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backup]{lang="IT"}]{#struct_0_x6987_95089_x1121142373}[：实例状态为备]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="IT"}]{#struct_0_x6987_95089_674517499}[：实例状态为不运行]{style="font-family:宋体"}

[[Received a VSRP mode event: VSRP instance=*vsrp-instance-name*, from *OldMode* to *NewMode.*]{lang="EN-US"}]{#struct_0_x6987_95089_x1121207909}

[[PPP]{lang="EN-US"}]{#struct_0_x6987_95089_x1124745193}[收到实例]{style="font-family:宋体"}*[vsrp-instance-name]{lang="EN-US"}*[备份模式变化事件信息，其中]{style="font-family:宋体"}*[OldMode]{lang="EN-US"}*[和]{style="font-family:宋体"}*[NewMode]{lang="EN-US"}*[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hot]{lang="IT"}]{#struct_0_x6987_95089_x1121273445}[：]{lang="EN-US" style="font-family:宋体"}[热备份]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Warm]{lang="EN-US"}]{#struct_0_x6987_95089_1498451547}[：]{lang="EN-US" style="font-family:宋体"}[温备份]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_x6987_95089_x1121338981}[：未知备份模式]{style="font-family:宋体"}

[[Received a VSRP NAS IP event: VSRP instance=*vsrp-instance-name*, from *OldAddr* to *NewAddr.*]{lang="EN-US"}]{#struct_0_x6987_95089_1559904472}

[[PPP]{lang="EN-US"}]{#struct_0_x6987_95089_x1120880229}[收到实例]{style="font-family:宋体"}*[vsrp-instance-name]{lang="EN-US"}*[ NAS IP]{lang="EN-US"}[地址从]{style="font-family:宋体"}*[OldAddr]{lang="EN-US"}*[变为]{style="font-family:宋体"}*[NewAddr]{lang="EN-US"}*[事件信息]{style="font-family:宋体"}

[[Received a VSRP NAS port event: VSRP instance=*vsrp-instance-name*, from *OldNasPortName to NewNasPortName.*]{lang="EN-US"}]{#struct_0_x6987_95089_x1120945765}

[[PPP]{lang="EN-US"}]{#struct_0_x6987_95089_520162618}[收到实例]{style="font-family:宋体"}*[vsrp-instance-name]{lang="EN-US"}*[ NAS]{lang="EN-US"}[端口从]{style="font-family:宋体"}*[OldNasPortName]{lang="EN-US"}*[变为]{style="font-family:宋体"}*[NewNasPortName]{lang="EN-US"}*[事件信息，]{style="font-family:宋体"}[NAS]{lang="EN-US"}[端口名为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示未知]{style="font-family:宋体"}[NAS]{lang="EN-US"}[端口]{style="font-family:宋体"}

[[Received a VSRP NAS ID event: VSRP instance=*vsrp-instance-name*, from *OldNasSysName to NewNasSysName.*]{lang="EN-US"}]{#struct_0_x6987_95089_x1121011301}

[[PPP]{lang="EN-US"}]{#struct_0_x6987_95089_75124948}[收到实例]{style="font-family:宋体"}*[vsrp-instance-name]{lang="EN-US"}*[ NAS ID]{lang="EN-US"}[从]{style="font-family:宋体"}*[OldNasSysName]{lang="EN-US"}*[变为]{style="font-family:宋体"}*[NewNasSysName]{lang="EN-US"}*[事件信息，]{style="font-family:宋体"}[NAS ID]{lang="EN-US"}[为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示未知]{style="font-family:宋体"}[NAS ID]{lang="EN-US"}

[[Received a VA up event: VA interface=*interface-name.*]{lang="EN-US"}]{#struct_0_x6987_95089_x1121076837}

[[PPP]{lang="EN-US"}]{#struct_0_x6987_95089_1000973601}[收到]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口]{style="font-family:宋体"}[up]{lang="EN-US"}[事件信息]{style="font-family:宋体"}

[[Received a VA down event: VA interface=*interface-name.*]{lang="EN-US"}]{#struct_0_x6987_95089_x1120618085}

[[PPP]{lang="EN-US"}]{#struct_0_x6987_95089_x1050313208}[收到]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口]{style="font-family:宋体"}[down]{lang="EN-US"}[事件信息]{style="font-family:宋体"}

[[Succeeded to *operate* session node for VSRP instance *vsrp-instance-name*: session ID=*id*, service VLAN=*number*, customer VLAN=*number*, MAC address=*mac-addr*.]{lang="EN-US"}]{#struct_0_x6987_95089_x1120683621}

[[对多机备份实例下的会话操作成功，其中]{style="font-family:宋体"}*[number]{lang="EN-US"}*]{#struct_0_x6987_95089_1140611771}[为]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，取值为]{style="font-family:宋体"}[65535]{lang="EN-US"}[时表示不带]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}

[*[operate]{lang="EN-US"}*]{#struct_0_x6987_95089_x1121142366}[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[c]{lang="EN-US"}[reate]{lang="EN-US"}]{#struct_0_x6987_95089_271298508}[：]{lang="EN-US" style="font-family:宋体"}[创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[d]{lang="EN-US"}[elete]{lang="EN-US"}]{#struct_0_x6987_95089_x1121207902}[：]{lang="EN-US" style="font-family:宋体"}[删除]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[u]{lang="EN-US"}[p]{lang="EN-US"}]{#struct_0_x6987_95089_x1077691026}[d]{lang="EN-US"}[ate]{lang="EN-US"}[：更新]{style="font-family:宋体"}

[[Failed to *operate* session node for VSRP instance *vsrp-instance-name*: session ID=*id*, service VLAN=*number*, customer VLAN=*number*, MAC address=*mac-addr*.]{lang="EN-US"}]{#struct_0_x6987_95089_x1121273438}

[[对多机备份实例下的会话操作失败，其中]{style="font-family:宋体"}*[number]{lang="EN-US"}*]{#struct_0_x6987_95089_x1680311750}[为]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，取值为]{style="font-family:宋体"}[65535]{lang="EN-US"}[时表示不带]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}

[*[operate]{lang="EN-US"}*]{#struct_0_x6987_95089_x1121338974}[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[c]{lang="EN-US"}[reate]{lang="EN-US"}]{#struct_0_x6987_95089_x1974958113}[：]{lang="EN-US" style="font-family:宋体"}[创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[d]{lang="EN-US"}[elete]{lang="EN-US"}]{#struct_0_x6987_95089_x1120880222}[：]{lang="EN-US" style="font-family:宋体"}[删除]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[u]{lang="EN-US"}[p]{lang="EN-US"}]{#struct_0_x6987_95089_1932328174}[d]{lang="EN-US"}[ate]{lang="EN-US"}[：更新]{style="font-family:宋体"}

[[Sent *operate* PPP session message to *Device*: session ID=*id*, service VLAN=*number*, customer VLAN=*number*, MAC address=*mac-addr*.]{lang="EN-US"}]{#struct_0_x6987_95089_x1120945758}

[[发送]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x6987_95089_x1121011294}[会话的]{style="font-family:宋体"}*[operate]{lang="EN-US"}*[消息给]{style="font-family:宋体"}*[Device]{lang="EN-US"}*[，其中]{style="font-family:宋体"}*[number]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，取值为]{style="font-family:宋体"}[65535]{lang="EN-US"}[时表示不带]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}

[*[operate]{lang="EN-US"}*]{#struct_0_x6987_95089_477950722}[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[c]{lang="EN-US"}[reate]{lang="EN-US"}]{#struct_0_x6987_95089_x1121076830}[：]{lang="EN-US" style="font-family:宋体"}[创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[d]{lang="EN-US"}[elete]{lang="EN-US"}]{#struct_0_x6987_95089_x1371679394}[：]{lang="EN-US" style="font-family:宋体"}[删除]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[u]{lang="EN-US"}[p]{lang="EN-US"}]{#struct_0_x6987_95089_x1120618078}[d]{lang="EN-US"}[ate]{lang="EN-US"}[：更新]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[update coa of]{lang="EN-US"}]{#struct_0_x6987_95089_66415079}[：更新授权信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[update flow of]{lang="EN-US"}]{#struct_0_x6987_95089_x1120683614}[：更新流量信息]{style="font-family:宋体"}

[*[Device]{lang="EN-US"}*]{#struct_0_x6987_95089_381031348}[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[primary d]{lang="EN-US"}[evice]{lang="EN-US"}]{#struct_0_x6987_95089_x1121142367}[：]{lang="EN-US" style="font-family:宋体"}[主设备]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[b]{lang="EN-US"}[ackup]{lang="EN-US"}]{#struct_0_x6987_95089_x1294785433}[ d]{lang="EN-US"}[evice]{lang="EN-US"}[：备设备]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[m]{lang="EN-US"}[aster]{lang="EN-US"}]{#struct_0_x6987_95089_x1121207903}[ b]{lang="EN-US"}[oard]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[主控板]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IO b]{lang="EN-US"}[oard]{lang="EN-US"}]{#struct_0_x6987_95089_1651192329}[：接口板]{style="font-family:
  宋体"}

[[Failed to recover PPP session on VA interface *interface-name* of VSRP instance *vsrp-instance-name*: session ID=*id*, service VLAN=*number*, customer VLAN=*number*, MAC address=*mac-addr*.]{lang="EN-US"}]{#struct_0_x6987_95089_x1121273439}

[[PPP]{lang="EN-US"}]{#struct_0_x6987_95089_x114227809}[模块恢复]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[下指定会话失败，其中]{style="font-family:宋体"}*[number]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，取值为]{style="font-family:宋体"}[65535]{lang="EN-US"}[时表示不带]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}

[[Failed to allocate memory to *operate* PPP session: session ID=*id*, service VLAN=*number*, customer VLAN=*number*, MAC address=*mac-addr*.]{lang="EN-US"}]{#struct_0_x6987_95089_x1121338975}

[*[operate]{lang="EN-US"}*[ PPP]{lang="EN-US"}]{#struct_0_x6987_95089_x408874172}[会话时分配内存失败，其中]{style="font-family:宋体"}*[number]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，取值为]{style="font-family:宋体"}[65535]{lang="EN-US"}[时表示不带]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}

[*[operate]{lang="EN-US"}*]{#struct_0_x6987_95089_x1120880223}[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[c]{lang="EN-US"}[reate]{lang="EN-US"}]{#struct_0_x6987_95089_366244233}[：]{lang="EN-US" style="font-family:宋体"}[创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[update]{lang="EN-US"}]{#struct_0_x6987_95089_x1120945759}[：更新]{style="font-family:宋体"}

[[Primary thread *Result* to send *operate* session to worker thread: VA interface=*interface-name*, session ID=*id*, service VLAN=*number*, customer VLAN=*number*, MAC address=*mac-addr*.]{lang="EN-US"}]{#struct_0_x6987_95089_2133104118}

[[PPP]{lang="EN-US"}]{#struct_0_x6987_95089_x1121011295}[发送]{style="font-family:宋体"}*[operate]{lang="EN-US"}*[指定会话成功或失败信息，其中]{style="font-family:宋体"}*[number]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，取值为]{style="font-family:宋体"}[65535]{lang="EN-US"}[时表示不带]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[operate]{lang="EN-US"}*]{#struct_0_x6987_95089_2044034663}[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[c]{lang="EN-US"}[reate]{lang="EN-US"}]{#struct_0_x6987_95089_x1121076831}[：]{lang="EN-US" style="font-family:宋体"}[创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[u]{lang="EN-US"}[p]{lang="EN-US"}]{#struct_0_x6987_95089_194404547}[d]{lang="EN-US"}[ate]{lang="EN-US"}[：更新]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[d]{lang="EN-US"}[elete]{lang="EN-US"}]{#struct_0_x6987_95089_x1120618079}[：删除]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[activate]{lang="EN-US"}]{#struct_0_x6987_95089_x1120683615}[：激活]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deactivate]{lang="EN-US"}]{#struct_0_x6987_95089_x1185052593}[：去激活]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[update coa of]{lang="EN-US"}]{#struct_0_x6987_95089_36866401}[：更新授权信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[update flow of]{lang="EN-US"}]{#struct_0_x6987_95089_440625013}[：更新流量信息]{style="font-family:宋体"}

[*[Result]{lang="EN-US"}*]{#struct_0_x6987_95089_36931937}[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[succe]{lang="EN-US"}]{#struct_0_x6987_95089_x1899369762}[eded]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[failed]{lang="EN-US"}]{#struct_0_x6987_95089_36735329}[：失败]{style="font-family:宋体"}

[[VSRP *vsrp-instance-name*: Establishing TCP channel timed out.]{lang="EN-US"}]{#struct_0_x6987_95089_2137853507}

[[PPP]{lang="EN-US"}]{#struct_0_x6987_95089_36800865}[备份]{style="font-family:宋体"}[TCP]{lang="EN-US"}[通道重连超时]{style="font-family:宋体"}

[[VSRP *vsrp-instance-name*: Successfully established VSRP TCP channel.]{lang="EN-US"}]{#struct_0_x6987_95089_34623657}

[[多机备份的备份]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x6987_95089_36604257}[通道建立成功]{style="font-family:宋体"}

[[VSRP *vsrp-instance-name*: Failed to establish VSRP TCP channel.]{lang="EN-US"}]{#struct_0_x6987_95089_143428312}

[[多机备份的备份]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x6987_95089_36669793}[通道建立失败]{style="font-family:宋体"}

[[VSRP *vsrp-instance-name*: Destroyed VSRP TCP channel.]{lang="EN-US"}]{#struct_0_x6987_95089_x205384823}

[[销毁多机备份的备份]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x6987_95089_36473185}[通道]{style="font-family:宋体"}

[[VSRP *vsrp-instance-name*: Received a repeated VA up event.]{lang="EN-US"}]{#struct_0_x6987_95089_1609750702}

[[重复收到]{style="font-family:宋体"}[VA up]{lang="EN-US"}]{#struct_0_x6987_95089_36538721}[事件]{style="font-family:宋体"}

[[Received a backup end event: VSRP instance=*vsrp-instance-name*..]{lang="EN-US"}]{#struct_0_x6987_95089_1624189908}

[[PPP]{lang="EN-US"}]{#struct_0_x6987_95089_37390689}[收到]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[通知的备份结束事件]{style="font-family:宋体"}

[[Primary device sent a smooth start message to backup device: VSRP instance=*vsrp-instance-name*.]{lang="EN-US"}]{#struct_0_x6987_95089_1786358260}

[[主设备发送平滑开始消息给备设备]{style="font-family:宋体"}]{#struct_0_x6987_95089_37456225}

[[Backup device received a smooth start message: VSRP instance=*vsrp-instance-name*.]{lang="EN-US"}]{#struct_0_x6987_95089_36866400}

[[备设备接收到主设备发送的平滑开始消息]{style="font-family:宋体"}]{#struct_0_x6987_95089_x1898027147}

[[Primary device sent a smooth end message to backup device: VSRP instance=*vsrp-instance-name*.]{lang="EN-US"}]{#struct_0_x6987_95089_36931936}

[[主设备发送平滑结束消息给备设备]{style="font-family:宋体"}]{#struct_0_x6987_95089_439282398}

[[Backup device received a smooth end message: VSRP instance=*vsrp-instance-name*.]{lang="EN-US"}]{#struct_0_x6987_95089_36735328}

[[备设备接收到主设备发送的平滑结束消息]{style="font-family:宋体"}]{#struct_0_x6987_95089_181538371}

[[Sent a backup end message to new primary device: VSRP instance=*vsrp-instance-name*.]{lang="EN-US"}]{#struct_0_x6987_95089_36800864}

[[备设备发送备份结束消息到新主设备]{style="font-family:宋体"}]{#struct_0_x6987_95089_1990938793}

[[New primary device received a backup end message: VSRP instance=*vsrp-instance-name*.]{lang="EN-US"}]{#struct_0_x6987_95089_36604256}

[[新主设备接收到备设备发送的备份结束消息]{style="font-family:宋体"}]{#struct_0_x6987_95089_2099743448}

[[Sent a batch deleting message to backup device: VSRP instance=*vsrp-instance-name*.]{lang="EN-US"}]{#struct_0_x6987_95089_36669792}

[[主设备发送批量会话删除消息到备设备]{style="font-family:宋体"}]{#struct_0_x6987_95089_36473184}

[[Received a batch deleting message: VSRP instance=*vsrp-instance-name*.]{lang="EN-US"}]{#struct_0_x6987_95089_x346564434}

[[备设备收到主设备发送的批量会话删除消息]{style="font-family:宋体"}]{#struct_0_x6987_95089_36538720}

[[Backup device sent a smooth request message to primary device: VSRP instance=*vsrp-instance-name*.]{lang="EN-US"}]{#struct_0_x6987_95089_x332125228}

[[备设备发送平滑请求消息到主设备]{style="font-family:宋体"}]{#struct_0_x6987_95089_37390688}

[[VSRP *vsrp-instance-name* started to allow access.]{lang="EN-US"}]{#struct_0_x6987_95089_37456224}

[[多机备份实例]{style="font-family:宋体"}*[vsrp-instance-name]{lang="EN-US"}*]{#struct_0_x6987_95089_x610579805}[允许用户上线]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6987_95089_734003898}

[[\# ]{lang="EN-US"}]{#struct_0_x6987_95089_x306720976}[打开]{style="font-family:宋体"}[PPP]{lang="EN-US"}[的多机备份调试信息开关。]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[协商通过后会创建会话，系统将输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging ppp vsrp]{lang="EN-US"}]{#struct_0_x6987_95089_36866399}

[\*Jun 10 15:16:33:398 2013 Sysname PPP/7/VSRP: -MDC=1;Succeeded to create session node for VSRP instance 1: session ID=1, service VLAN=65535, customer VLAN=65535, MAC address=0050-56c0-0009.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6987_95089_1283864376}*[在多机备份实例]{style="font-family:宋体"}[1]{lang="EN-US"}[中成功创建了]{style="font-family:宋体"}[SID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0050-56c0-0009]{lang="EN-US"}[且不带]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}[的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[会话]{style="font-family:宋体"}*

::: {#-790114913 .myid}
[]{#_Toc404795984}[]{#struct_0_x6987_95089_x1777252133}[]{#_Toc375317954}[]{#_Toc357684242}[]{#_Toc353278228}

**多机备份调试命令 \-- PPPoE支持多机备份功能调试命令 \-- debugging pppoe-server vsrp**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6987_95089_1961906481}

[**[debugging pppoe-server vsrp]{lang="EN-US"}**]{#struct_0_x6987_95089_x1893921201}

[**[undo debugging pppoe-server vsrp]{lang="EN-US"}**]{#struct_0_x6987_95089_36931935}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6987_95089_x1517032738}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x6987_95089_1710651491}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6987_95089_908955728}

[[network-admin]{lang="EN-US"}]{#struct_0_x6987_95089_x131337536}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6987_95089_x1651538844}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6987_95089_36735327}

[**[debugging pppoe-server vsrp]{lang="EN-US"}**]{#struct_0_x6987_95089_x245428669}[命令用来打开]{style="font-family:
宋体"}[PPPoE Server]{lang="EN-US"}[的多机备份调试信息开关。]{style="font-family:
宋体"}**[undo debugging pppoe-server vsrp]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[的多机备份调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}]{#struct_0_x6987_95089_1573697068}[的多机备份调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-3 ]{lang="EN-US"}[debugging pppoe-server vsrp]{lang="EN-US"}]{#struct_0_x6987_95089_1205500869}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1866447160}[[字段]{style="font-family:黑体"}]{#struct_0_x6987_95089_x898555071}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6987_95089_36800863}

[[VSRP *vsrp-instance-name*: Primary device MPU created a backup session.]{lang="EN-US"}]{#struct_0_x6987_95089_416960681}

[[主设备主控板创建备份会话]{style="font-family:宋体"}]{#struct_0_x6987_95089_36604255}

[[VSRP *vsrp-instance-name*: MPU deleted a backup session.]{lang="EN-US"}]{#struct_0_x6987_95089_525765336}

[[主控板删除备份会话]{style="font-family:宋体"}]{#struct_0_x6987_95089_x688867580}

[[VSRP *vsrp-instance-name*: Destroyed VSRP TCP channel.]{lang="EN-US"}]{#struct_0_x6987_95089_36669791}

[[销毁多机备份]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x6987_95089_x587721847}[通道]{style="font-family:宋体"}

[[VSRP *vsrp-instance-name*: Established VSRP TCP channel.]{lang="EN-US"}]{#struct_0_x6987_95089_36473183}

[[创建多机备份]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x6987_95089_1992087726}[通道]{style="font-family:宋体"}

[[VSRP *vsrp-instance-name*: Failed to establish VSRP TCP channel.]{lang="EN-US"}]{#struct_0_x6987_95089_x21115574}

[[多机备份功能备份]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x6987_95089_36538719}[通道创建失败]{style="font-family:宋体"}

[[VSRP *vsrp-instance-name*: Deleted a session by command.]{lang="EN-US"}]{#struct_0_x6987_95089_x1471242129}

[[命令行执行导致的会话删除]{style="font-family:宋体"}]{#struct_0_x6987_95089_37390687}

[[VSRP *vsrp-instance-name*: VSRP channel changed.]{lang="EN-US"}]{#struct_0_x6987_95089_x125326860}

[[注册多机备份服务后]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}]{#struct_0_x6987_95089_1889146823}[接收到多机备份通知的通道变化事件信息]{style="font-family:宋体"}

[[VSRP *vsrp-instance-name*: VSRP backup mode changed from O*ldMode* to N*ewMode*.]{lang="EN-US"}]{#struct_0_x6987_95089_37456223}

[[多机备份功能备份模式变化，其中]{style="font-family:宋体"}*[OldMode]{lang="EN-US"}*]{#struct_0_x6987_95089_963398307}[和]{style="font-family:宋体"}*[NewMode]{lang="EN-US"}*[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hot]{lang="IT"}]{#struct_0_x6987_95089_36866398}[：]{lang="EN-US" style="font-family:宋体"}[热备份]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Warm]{lang="IT"}]{#struct_0_x6987_95089_x1054787784}[：]{lang="EN-US" style="font-family:宋体"}[温备份]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_x6987_95089_x1190559585}[：未知备份模式]{style="font-family:宋体"}

[[VSRP *vsrp-instance-name*: VSRP status changed from O*ldStatus* to N*ewStatus*.]{lang="EN-US"}]{#struct_0_x6987_95089_36931934}

[[多机备份状态变化，其中]{style="font-family:宋体"}*[OldStatus]{lang="EN-US"}*]{#struct_0_x6987_95089_821619422}[和]{style="font-family:宋体"}*[NewStatus]{lang="EN-US"}*[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Master]{lang="IT"}]{#struct_0_x6987_95089_36735326}[：]{style="font-family:宋体"}[实例状态为主]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backup]{lang="EN-US"}]{#struct_0_x6987_95089_2093223491}[：实例状态为备]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_x6987_95089_36800862}[：实例状态为不运行]{style="font-family:宋体"}

[[VSRP *vsrp-instance-name*: Received a VSRP *event* event.]{lang="EN-US"}]{#struct_0_x6987_95089_x1921691479}

[[PPPoE Server]{lang="EN-US"}]{#struct_0_x6987_95089_x1478170887}[响应]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[事件信息，其中]{style="font-family:宋体"}*[event]{lang="EN-US"}*[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[status]{lang="EN-US"}]{#struct_0_x6987_95089_36604254}[：]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例状态事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[backup mode]{lang="EN-US"}]{#struct_0_x6987_95089_x1812886824}[：]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例备份模式事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[traffic backup interval]{lang="EN-US"}]{#struct_0_x6987_95089_36669790}[：]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例流量备份间隔事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[traffic backup threshold]{lang="EN-US"}]{#struct_0_x6987_95089_1368593289}[：]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例流量备份阈值事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[virtual MAC]{lang="EN-US"}]{#struct_0_x6987_95089_36473182}[：]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例虚]{style="font-family:宋体"}[MAC]{lang="EN-US"}[事件]{style="font-family:宋体"}[peer info]{lang="EN-US"}[：多机备份实例数据通道所需信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[status over]{lang="EN-US"}]{#struct_0_x6987_95089_35772590}[：多机备份实例状态结束事件]{style="font-family:宋体"}

[[VSRP *vsrp-instance-name*: Primary device MPU deleted a backup session.]{lang="EN-US"}]{#struct_0_x6987_95089_36538718}

[[主设备主控板删除备份会话]{style="font-family:宋体"}]{#struct_0_x6987_95089_867410031}

[[VSRP *vsrp-instance-name*: Primary device MPU updated a backup session.]{lang="EN-US"}]{#struct_0_x6987_95089_1972063919}

[[主设备主控板更新备份会话]{style="font-family:宋体"}]{#struct_0_x6987_95089_37390686}

[[VSRP *vsrp-instance-name*: Backup device MPU deleted a backup session.]{lang="EN-US"}]{#struct_0_x6987_95089_x2081641996}

[[备设备主控板删除备份会话]{style="font-family:宋体"}]{#struct_0_x6987_95089_37456222}

[[VSRP *vsrp-instance-name*: Backup device MPU failed to recover a session.]{lang="EN-US"}]{#struct_0_x6987_95089_x992916829}

[[备设备主控板恢复会话失败]{style="font-family:宋体"}]{#struct_0_x6987_95089_x792850498}

[[VSRP *vsrp-instance-name*: Backup device MPU failed to create a backup session.]{lang="EN-US"}]{#struct_0_x6987_95089_36866405}

[[备设备主控板创建备份会话失败]{style="font-family:宋体"}]{#struct_0_x6987_95089_1205299061}

[[VSRP *vsrp-instance-name*: Primary device sent a smooth start message to backup device.]{lang="EN-US"}]{#struct_0_x6987_95089_36931941}

[[主设备向备设备发送平滑开始消息]{style="font-family:宋体"}]{#struct_0_x6987_95089_x359392485}

[[VSRP *vsrp-instance-name*: Primary device sent a smooth end message to backup device.]{lang="EN-US"}]{#struct_0_x6987_95089_36735333}

[[主设备向备设备发送平滑结束消息]{style="font-family:宋体"}]{#struct_0_x6987_95089_555981224}

[[VSRP *vsrp-instance-name*: Backup device received a smooth start message.]{lang="EN-US"}]{#struct_0_x6987_95089_1098262890}

[[备设备收到主设备的平滑开始消息]{style="font-family:宋体"}]{#struct_0_x6987_95089_36800869}

[[VSRP *vsrp-instance-name*: Backup device received a smooth end message.]{lang="EN-US"}]{#struct_0_x6987_95089_x730050391}

[[备设备收到主设备的平滑结束消息]{style="font-family:宋体"}]{#struct_0_x6987_95089_36604261}

[[VSRP *vsrp-instance-name*: New primary device received a real backup end message.]{lang="EN-US"}]{#struct_0_x6987_95089_x275644557}

[[新的主设备收到实时备份结束消息]{style="font-family:宋体"}]{#struct_0_x6987_95089_36669797}

[[VSRP *vsrp-instance-name*: Backup device sent a smooth request message to primary device.]{lang="EN-US"}]{#struct_0_x6987_95089_559289225}

[[备设备向主设备发送平滑请求消息]{style="font-family:宋体"}]{#struct_0_x6987_95089_36473189}

[[VSRP *vsrp-instance-name*: Primary device sent a backup session creating message to backup device.]{lang="EN-US"}]{#struct_0_x6987_95089_x391194450}

[[主设备向备设备发送创建备份会话消息]{style="font-family:宋体"}]{#struct_0_x6987_95089_988608523}

[[VSRP *vsrp-instance-name*: Primary device sent a backup session deleting message to backup device.]{lang="EN-US"}]{#struct_0_x6987_95089_36538725}

[[主设备向备设备发送删除备份会话消息]{style="font-family:宋体"}]{#struct_0_x6987_95089_x1906103340}

[[VSRP *vsrp-instance-name*: Primary device sent a backup session batch deleting message to backup device.]{lang="EN-US"}]{#struct_0_x6987_95089_37390693}

[[主设备向备设备发送批量删除备份会话消息]{style="font-family:宋体"}]{#struct_0_x6987_95089_x2089536167}

[[VSRP *vsrp-instance-name*: Failed to create VSRP CB due to lack of memory space.]{lang="EN-US"}]{#struct_0_x6987_95089_37456229}

[[申请内存失败导致创建]{style="font-family:宋体"}[VSRP]{lang="EN-US"}]{#struct_0_x6987_95089_x948286813}[控制块失败]{style="font-family:宋体"}

[[VSRP *vsrp-instance-name*: Failed to create VSRP CB due to the failure to add VSRP data.]{lang="EN-US"}]{#struct_0_x6987_95089_36866404}

[[添加]{style="font-family:宋体"}[VSRP]{lang="EN-US"}]{#struct_0_x6987_95089_x1133353099}[数据失败导致创建]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[控制块失败]{style="font-family:宋体"}

[[VSRP *vsrp-instance-name*: Failed to create VSRP CB due to VSRP initialization failure.]{lang="EN-US"}]{#struct_0_x6987_95089_x210383861}

[[初始化]{style="font-family:宋体"}[VSRP]{lang="EN-US"}]{#struct_0_x6987_95089_36931940}[控制块失败导致创建]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[控制块失败]{style="font-family:宋体"}

[[VSRP *vsrp-instance-name*: Virtual MAC changed from *oldMacAddr* to *newMacAddr.*]{lang="EN-US"}]{#struct_0_x6987_95089_1979259675}

[[虚]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x6987_95089_36735332}[从]{style="font-family:宋体"}*[oldMacAddr]{lang="EN-US"}*[变为]{style="font-family:宋体"}[n*ewMacAddr*]{lang="EN-US"}

[[VSRP *vsrp-instance-name*: Sent a backup end message to primary device.]{lang="EN-US"}]{#struct_0_x6987_95089_x1400333912}

[[备设备向主设备发送备份结束消息]{style="font-family:宋体"}]{#struct_0_x6987_95089_36800868}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6987_95089_1226264745}

[*[\# ]{lang="EN-US"}*]{#struct_0_x6987_95089_988242362}[打开]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[的多机备份备份调试信息]{style="font-family:宋体"}[开关，接口绑定多机备份实例，主设备和备设备]{style="font-family:宋体"}[TCP]{lang="EN-US"}[通道已建立。默认]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[60032]{lang="EN-US"}[，如果将]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号改为]{style="font-family:宋体"}[100]{lang="EN-US"}[，系统将输出下列调试信息。]{style="font-family:宋体"}

[[\<master\> debugging pppoe-server vsrp]{lang="EN-US"}]{#struct_0_x6987_95089_x340385795}

[\<master\> system-view ]{lang="EN-US"}

[\[master\] pppoe-server vsrp-port 100]{lang="EN-US"}

[\[master\]\*Jun 17 18:25:47:287 2013 master PPPOES/7/VSRP: -MDC=1; VSRP master: Destroyed VSRP TCP channel.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6987_95089_115323685}*[本端通道号与对端通道号不一致，销毁多机备份的备份]{style="font-family:宋体"}[TCP]{lang="EN-US"}[通道]{style="font-family:宋体"}*

::: {#1387777905 .myid}
[]{#_Toc404795986}[]{#struct_0_x6987_95089_1680670579}[]{#_Toc374109538}[]{#_Toc365362554}

**多机备份调试命令 \-- L2TP支持多机备份功能调试命令 \-- debugging l2tp vsrp**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6987_95089_x1129941206}

[**[debugging l2tp]{lang="EN-US"}**]{#struct_0_x6987_95089_387494067}**[ vsrp]{lang="EN-US"}**[ ]{lang="EN-US"}[{]{lang="EN-US"}[ **error** ]{lang="EN-US"}[\|]{lang="EN-US"}[ **event** ]{lang="EN-US"}[}]{lang="EN-US"}

[**[undo debugging l2tp]{lang="EN-US"}**]{#struct_0_x6987_95089_1319381861}**[ vsrp]{lang="EN-US"}**[ ]{lang="EN-US"}[{]{lang="EN-US"}[ **error** ]{lang="EN-US"}[\|]{lang="EN-US"}[ **event** ]{lang="EN-US"}[}]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6987_95089_1374654635}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x6987_95089_x1489959122}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6987_95089_x1950293506}

[[network-admin]{lang="EN-US"}]{#struct_0_x6987_95089_492400467}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6987_95089_x1946661780}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6987_95089_1012441775}

[**[error]{lang="EN-US"}**]{#struct_0_x6987_95089_244748291}[：表示]{style="font-family:宋体"}[L2TP VSRP]{lang="EN-US"}[的错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x6987_95089_36669796}[：表示]{style="font-family:宋体"}[L2TP VSRP]{lang="EN-US"}[的事件调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x6987_95089_x1779362935}

[**[debugging l2tp vsrp]{lang="EN-US"}**]{#struct_0_x6987_95089_86544428}[命令用来打开]{style="font-family:宋体"}[L2TP VSRP]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging l2tp vsrp**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[L2TP VSRP]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}]{#struct_0_x6987_95089_1917070563}[L2TP VSRP]{lang="EN-US"}[的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-4 ]{lang="EN-US"}[debugging l2tp vsrp error]{lang="EN-US"}]{#struct_0_x6987_95089_x472185557}[命令]{style="font-family:黑体"}[输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1824307784}[[字段]{style="font-family:黑体"}]{#struct_0_x6987_95089_1040474058}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6987_95089_36473188}

[[Failed to create VSRP channel.]{lang="EN-US"}]{#struct_0_x6987_95089_1947457710}

[[数据备份通道创建失败]{style="font-family:宋体"}]{#struct_0_x6987_95089_36538724}

[[Failed to create L2TP VSRP reconcile PPP timer.]{lang="EN-US"}]{#struct_0_x6987_95089_432548820}

[[创建]{style="font-family:宋体"}[L2TP VSRP]{lang="EN-US"}]{#struct_0_x6987_95089_37390692}[与]{style="font-family:宋体"}[PPP]{lang="EN-US"}[平滑定时器失败]{style="font-family:宋体"}

[[Received a PULL_REQUEST packet in wrong status.]{lang="EN-US"}]{#struct_0_x6987_95089_249115993}

[[在错误的状态收到同步信息请求报文]{style="font-family:宋体"}]{#struct_0_x6987_95089_1160786517}

[[Received a BEGIN_RECONCILE or END_RECONCILE packet in wrong status.]{lang="EN-US"}]{#struct_0_x6987_95089_37456228}

[[在错误的状态收到平滑开始或平滑结束报文]{style="font-family:宋体"}]{#struct_0_x6987_95089_1390365347}

[[Received a REAL_TIME_TUNNEL packet in wrong status.]{lang="EN-US"}]{#struct_0_x6987_95089_1602950342}

[[在错误的状态收到实时隧道信息报文]{style="font-family:宋体"}]{#struct_0_x6987_95089_2021597894}

[[Received a too short *message-type* packet.]{lang="EN-US"}]{#struct_0_x6987_95089_1603015878}

[[收到]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*]{#struct_0_x6987_95089_x693212425}[类型的报文，报文长度太短。报文类型包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_x6987_95089_x759022518}[：本端备份组状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_x6987_95089_1602819270}[：同步信息请求]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_x6987_95089_x1535427493}[：平滑开始]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_x6987_95089_1602884806}[：平滑结束]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_x6987_95089_66647373}[：添加隧道]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5]{lang="EN-US"}]{#struct_0_x6987_95089_1602688198}[：实时隧道信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6]{lang="EN-US"}]{#struct_0_x6987_95089_1964886152}[：删除隧道]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[7]{lang="EN-US"}]{#struct_0_x6987_95089_1602753734}[：添加会话]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[8]{lang="EN-US"}]{#struct_0_x6987_95089_x1471566102}[：删除会话]{style="font-family:宋体"}

[[Received a *message-type* packet that had failed to pass the check.]{lang="EN-US"}]{#struct_0_x6987_95089_1602557126}

[[收到]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*]{#struct_0_x6987_95089_1236238617}[类型的报文，报文未通过检测。报文类型包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_x6987_95089_1602622662}[：本端备份组状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_x6987_95089_2048146027}[：同步信息请求]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_x6987_95089_1603474630}[：平滑开始]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_x6987_95089_x1497958956}[：平滑结束]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_x6987_95089_255463256}[：添加隧道]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5]{lang="EN-US"}]{#struct_0_x6987_95089_1603540166}[：实时隧道信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6]{lang="EN-US"}]{#struct_0_x6987_95089_2043487044}[：删除隧道]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[7]{lang="EN-US"}]{#struct_0_x6987_95089_1602950341}[：添加会话]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[8]{lang="EN-US"}]{#struct_0_x6987_95089_2021794502}[：删除会话]{style="font-family:宋体"}

[[Received a packet with a wrong local tunnel ID.]{lang="EN-US"}]{#struct_0_x6987_95089_1603015877}

[[收到报文携带错误的本地隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x6987_95089_x694064393}

[[Received a packet with a wrong group ID.]{lang="EN-US"}]{#struct_0_x6987_95089_1602819269}

[[收到报文携带错误的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}]{#struct_0_x6987_95089_x1534837670}[组]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Failed to add a tunnel after receiving the packet.]{lang="EN-US"}]{#struct_0_x6987_95089_1602884805}

[[收到报文后添加隧道失败]{style="font-family:宋体"}]{#struct_0_x6987_95089_66450765}

[[Received a packet with a wrong local session ID.]{lang="EN-US"}]{#struct_0_x6987_95089_1602688197}

[[收到报文携带错误的本地会话]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x6987_95089_1965213832}

[[VSRP service registration failed.]{lang="EN-US"}]{#struct_0_x6987_95089_1602753733}

[[VSRP]{lang="EN-US"}]{#struct_0_x6987_95089_x1471893782}[服务注册失败]{style="font-family:宋体"}

[[Failed to create the VSRP retransmit timer.]{lang="EN-US"}]{#struct_0_x6987_95089_1602557125}

[[重传定时器创建失败]{style="font-family:宋体"}]{#struct_0_x6987_95089_1236435225}

[ ]{lang="EN-US"}

[]{#struct_0_x6987_95089_1602622661}[[表1-5 ]{lang="EN-US"}[debugging l2tp ]{lang="EN-US"}]{#_Ref155675443}[vsrp event]{lang="EN-US"}[命令]{style="font-family:黑体"}[输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1785354904}[[字段]{style="font-family:黑体"}]{#struct_0_x6987_95089_2048211563}

[[描述]{style="font-family:黑体"}]{#struct_0_x6987_95089_297380776}

[[PPPLogStatus]{lang="EN-US"}]{#struct_0_x6987_95089_1603474629}

[[PPP]{lang="EN-US"}]{#struct_0_x6987_95089_x1498417709}[用户登录状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L]{lang="EN-US"}[ogged in]{lang="EN-US"}]{#struct_0_x6987_95089_1603540165}[：已登录]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L]{lang="EN-US"}[ogged out]{lang="EN-US"}]{#struct_0_x6987_95089_2043290436}[：已退出]{style="font-family:宋体"}

[[VSRPName]{lang="EN-US"}]{#struct_0_x6987_95089_1602950340}

[[VSRP]{lang="EN-US"}]{#struct_0_x6987_95089_2021728966}[实例名]{style="font-family:宋体"}

[[LocalVSRPStatus]{lang="EN-US"}]{#struct_0_x6987_95089_1603015876}

[[本端]{style="font-family:宋体"}[VSRP]{lang="EN-US"}]{#struct_0_x6987_95089_x694129929}[状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Master]{lang="EN-US"}]{#struct_0_x6987_95089_1602819268}[/Up]{lang="EN-US"}[：主]{style="font-family:宋体"}[/]{lang="EN-US"}[开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backup]{lang="EN-US"}]{#struct_0_x6987_95089_x1534903206}[/Up]{lang="EN-US"}[：备]{style="font-family:宋体"}[/]{lang="EN-US"}[开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Master]{lang="EN-US"}]{#struct_0_x6987_95089_136555986}[/]{lang="EN-US"}[Down]{lang="EN-US"}[：主]{style="font-family:宋体"}[/]{lang="EN-US"}[关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backup]{lang="EN-US"}]{#struct_0_x6987_95089_1602884804}[/]{lang="EN-US"}[Down]{lang="EN-US"}[：备]{style="font-family:宋体"}[/]{lang="EN-US"}[关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Error]{lang="EN-US"}]{#struct_0_x6987_95089_66516301}[：错误]{style="font-family:宋体"}

[[RemoteVSRPStatus]{lang="EN-US"}]{#struct_0_x6987_95089_1602688196}

[[对端]{style="font-family:宋体"}[VSRP]{lang="EN-US"}]{#struct_0_x6987_95089_1965279368}[状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Master]{lang="EN-US"}]{#struct_0_x6987_95089_1602753732}[：主]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backup]{lang="EN-US"}]{#struct_0_x6987_95089_x1471959318}[：备]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Error]{lang="EN-US"}]{#struct_0_x6987_95089_1602557124}[：错误]{style="font-family:宋体"}

[[VSRPBackupMode]{lang="EN-US"}]{#struct_0_x6987_95089_1236369689}

[[VSRP]{lang="EN-US"}]{#struct_0_x6987_95089_1602622660}[备份模式，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hot]{lang="EN-US"}]{#struct_0_x6987_95089_2048277099}[：热备]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Warm]{lang="EN-US"}]{#struct_0_x6987_95089_1603474628}[：温备]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Error]{lang="EN-US"}]{#struct_0_x6987_95089_x1498483245}[：错误]{style="font-family:宋体"}

[[VSRPChannelStatus]{lang="EN-US"}]{#struct_0_x6987_95089_1603540164}

[[数据备份通道状态，包括：]{style="font-family:宋体"}]{#struct_0_x6987_95089_2043355972}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Connected]{lang="EN-US"}]{#struct_0_x6987_95089_1602950339}[：已连接]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disconnected]{lang="EN-US"}]{#struct_0_x6987_95089_1603015875}[：已断开]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Error]{lang="EN-US"}]{#struct_0_x6987_95089_x693933321}[：错误]{style="font-family:宋体"}

[[NeedReconcilePeer]{lang="EN-US"}]{#struct_0_x6987_95089_1602819267}

[[是否需要平滑]{style="font-family:宋体"}]{#struct_0_x6987_95089_x1535755174}

[[IsSwitching]{lang="EN-US"}]{#struct_0_x6987_95089_1602884803}

[[是否正在切换]{style="font-family:宋体"}]{#struct_0_x6987_95089_66843981}

[[VRFIndexLocal]{lang="EN-US"}]{#struct_0_x6987_95089_1602688195}

[[本端]{style="font-family:宋体"}[VRF]{lang="EN-US"}]{#struct_0_x6987_95089_1965082760}[索引]{style="font-family:宋体"}

[[VRFIndexPeer]{lang="EN-US"}]{#struct_0_x6987_95089_1602753731}

[[对端]{style="font-family:宋体"}[VRF]{lang="EN-US"}]{#struct_0_x6987_95089_x1471762710}[索引]{style="font-family:宋体"}

[[InstanceID]{lang="EN-US"}]{#struct_0_x6987_95089_1602557123}

[[VSRP]{lang="EN-US"}]{#struct_0_x6987_95089_1236042009}[实例]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[LocalAddr]{lang="EN-US"}]{#struct_0_x6987_95089_1602622659}

[[本端]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x6987_95089_2048735854}[地址]{style="font-family:宋体"}

[[PeerAddr]{lang="EN-US"}]{#struct_0_x6987_95089_1603474627}

[[对端]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x6987_95089_x1498024493}[地址]{style="font-family:宋体"}

[[LocalTunnelID]{lang="EN-US"}]{#struct_0_x6987_95089_1603540163}

[[本端隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x6987_95089_2043159364}

[[RemoteTunnelID]{lang="EN-US"}]{#struct_0_x6987_95089_1602950346}

[[对端隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x6987_95089_2021860038}

[[Updated Ns and Nr to remote peer.]{lang="EN-US"}]{#struct_0_x6987_95089_1603015882}

[[通知备用设备更新发送报文的序号（]{style="font-family:宋体"}[Ns]{lang="EN-US"}]{#struct_0_x6987_95089_1602819274}[）和期望接收到的下一个控制报文中]{style="font-family:宋体"}[Ns]{lang="EN-US"}[字段的值（]{style="font-family:宋体"}[Nr]{lang="EN-US"}[）]{style="font-family:宋体"}

[[SendMessageType]{lang="EN-US"}]{#struct_0_x6987_95089_x1535689637}

[[发送信息类型，包括：]{style="font-family:宋体"}]{#struct_0_x6987_95089_1602884810}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L2TPV2_VSRP_MSG_TYPE_LOCAL_STATUS]{lang="EN-US"}]{#struct_0_x6987_95089_66778446}[：表示]{style="font-family:宋体"}[本端备份组状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L2TPV2_VSRP_MSG_TYPE_PULL_REQUEST]{lang="EN-US"}]{#struct_0_x6987_95089_1602688202}[：表示同步]{style="font-family:宋体"}[信息请求]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L2TPV2_VSRP_MSG_TYPE_BEGIN_RECONCILE]{lang="EN-US"}]{#struct_0_x6987_95089_9226367}[：表示]{style="font-family:宋体"}[平滑开始]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L2TPV2_VSRP_MSG_TYPE_END_RECONCILE]{lang="EN-US"}]{#struct_0_x6987_95089_1602622666}[：表示]{style="font-family:宋体"}[平滑结束]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L2TPV2_VSRP_MSG_TYPE_ADD_TUNNEL]{lang="EN-US"}]{#struct_0_x6987_95089_2047883883}[：表示]{style="font-family:
  宋体"}[添加隧道]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L2TPV2_VSRP_MSG_TYPE_REAL_TIME_TUNNEL]{lang="EN-US"}]{#struct_0_x6987_95089_1603474634}[：表示]{style="font-family:宋体"}[实时隧道信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L2TPV2_VSRP_MSG_TYPE_DELETE_TUNNEL]{lang="EN-US"}]{#struct_0_x6987_95089_1603540170}[：表示]{style="font-family:宋体"}[删除隧道]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L2TPV2_VSRP_MSG_TYPE_ADD_SESSION]{lang="EN-US"}]{#struct_0_x6987_95089_1602950345}[：表示]{style="font-family:
  宋体"}[添加会话]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L2TPV2_VSRP_MSG_TYPE_DELETE_SESSION]{lang="EN-US"}]{#struct_0_x6987_95089_2022056646}[：表示]{style="font-family:宋体"}[删除会话]{lang="EN-US" style="font-family:宋体"}

[[RecvMessageType]{lang="EN-US"}]{#struct_0_x6987_95089_1603015881}

[[接收信息类型，包括：]{style="font-family:宋体"}]{#struct_0_x6987_95089_x693671192}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L2TPV2_VSRP_MSG_TYPE_LOCAL_STATUS]{lang="EN-US"}]{#struct_0_x6987_95089_1602819273}[：表示]{style="font-family:宋体"}[本端备份组状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L2TPV2_VSRP_MSG_TYPE_PULL_REQUEST]{lang="EN-US"}]{#struct_0_x6987_95089_1602884809}[：表示同步]{style="font-family:宋体"}[信息请求]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L2TPV2_VSRP_MSG_TYPE_BEGIN_RECONCILE]{lang="EN-US"}]{#struct_0_x6987_95089_66188621}[：表示]{style="font-family:宋体"}[平滑开始]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L2TPV2_VSRP_MSG_TYPE_END_RECONCILE]{lang="EN-US"}]{#struct_0_x6987_95089_1602688201}[：表示]{style="font-family:宋体"}[平滑结束]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L2TPV2_VSRP_MSG_TYPE_ADD_TUNNEL]{lang="EN-US"}]{#struct_0_x6987_95089_9029759}[：表示]{style="font-family:
  宋体"}[添加隧道]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L2TPV2_VSRP_MSG_TYPE_REAL_TIME_TUNNEL]{lang="EN-US"}]{#struct_0_x6987_95089_1602753737}[：表示]{style="font-family:宋体"}[实时隧道信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L2TPV2_VSRP_MSG_TYPE_DELETE_TUNNEL]{lang="EN-US"}]{#struct_0_x6987_95089_x1471631638}[：表示]{style="font-family:宋体"}[删除隧道]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L2TPV2_VSRP_MSG_TYPE_ADD_SESSION]{lang="EN-US"}]{#struct_0_x6987_95089_1602557129}[：表示]{style="font-family:
  宋体"}[添加会话]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L2TPV2_VSRP_MSG_TYPE_DELETE_SESSION]{lang="EN-US"}]{#struct_0_x6987_95089_1235648793}[：表示删除会话]{lang="EN-US" style="font-family:宋体"}

[[MessageDataLen]{lang="EN-US"}]{#struct_0_x6987_95089_1602622665}

[[信息长度]{style="font-family:宋体"}]{#struct_0_x6987_95089_1603474633}

[[MessageInfo]{lang="EN-US"}]{#struct_0_x6987_95089_x1497762348}

[[信息内容]{style="font-family:宋体"}]{#struct_0_x6987_95089_1603540169}

[[VSRP_EVENT_STATUS]{lang="EN-US"}]{#struct_0_x6987_95089_2042504004}

[[VSRP]{lang="EN-US"}]{#struct_0_x6987_95089_1199665815}[实例状态事件，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Master]{lang="EN-US"}]{#struct_0_x6987_95089_1199731351}[：切换为主用设备]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backup]{lang="EN-US"}]{#struct_0_x6987_95089_601088950}[：切换为备用设备]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_x6987_95089_1199534743}[：主用和备用设备皆不可用]{style="font-family:宋体"}

[[VSRP_EVENT_BACKUPMODE]{lang="EN-US"}]{#struct_0_x6987_95089_595798642}

[[VSRP]{lang="EN-US"}]{#struct_0_x6987_95089_1199600279}[实例备份方式事件，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hot]{lang="EN-US"}]{#struct_0_x6987_95089_1375295588}[：切换为热备模式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Warm]{lang="EN-US"}]{#struct_0_x6987_95089_1199403671}[：切换为温备模式]{style="font-family:宋体"}

[[VSRP_EVENT_PEERINFO]{lang="EN-US"}]{#struct_0_x6987_95089_1199469207}

[[VSRP]{lang="EN-US"}]{#struct_0_x6987_95089_x1713226058}[实例数据通道所需信息，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VRFIndexLocal]{lang="EN-US"}]{#struct_0_x6987_95089_1199272599}[：表示]{style="font-family:宋体"}[本端]{lang="EN-US" style="font-family:宋体"}[VRF]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VRFIndexPeer]{lang="EN-US"}]{#struct_0_x6987_95089_1012035504}[：表示对端]{style="font-family:宋体"}[VRF]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[InstanceID]{lang="EN-US"}]{#struct_0_x6987_95089_1199338135}[：表示]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LocalAddr]{lang="EN-US"}]{#struct_0_x6987_95089_1200190103}[：表示]{style="font-family:宋体"}[本端]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PeerAddr]{lang="EN-US"}]{#struct_0_x6987_95089_1200255639}[：表示对]{style="font-family:宋体"}[端]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[VSRP_EVENT_STATUS_OVER]{lang="EN-US"}]{#struct_0_x6987_95089_x1085773008}

[[VSRP]{lang="EN-US"}]{#struct_0_x6987_95089_1199665814}[实例状态结束事件，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Over]{lang="EN-US"}]{#struct_0_x6987_95089_1199731350}[：切换已结束]{lang="EN-US" style="font-family:宋体"}

[[Updated a backup tunnel.]{lang="EN-US"}]{#struct_0_x6987_95089_601154486}

[[更新备份隧道]{style="font-family:宋体"}]{#struct_0_x6987_95089_1199534742}

[[Added a source IP.]{lang="EN-US"}]{#struct_0_x6987_95089_1199600278}

[[源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x6987_95089_1375230052}[生成路由：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VPNID]{lang="EN-US"}]{#struct_0_x6987_95089_1199403670}[：表示]{style="font-family:宋体"}[生成路由所属]{lang="EN-US" style="font-family:宋体"}[VPN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPAddress]{lang="EN-US"}]{#struct_0_x6987_95089_1014364757}[：表示]{style="font-family:宋体"}[源]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Result]{lang="EN-US"}]{#struct_0_x6987_95089_1199469206}[：表示]{style="font-family:宋体"}[路由添加结果]{lang="EN-US" style="font-family:宋体"}

[[Deleted a source IP.]{lang="EN-US"}]{#struct_0_x6987_95089_1199272598}

[[删除源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x6987_95089_1199338134}[路由：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VPNID]{lang="EN-US"}]{#struct_0_x6987_95089_x1703234565}[：表示删除路由所属]{style="font-family:宋体"}[VPN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPAddress]{lang="EN-US"}]{#struct_0_x6987_95089_1200190102}[：表示]{style="font-family:宋体"}[源]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[R]{lang="EN-US"}[esult]{lang="EN-US"}]{#struct_0_x6987_95089_1631003595}[：表示]{style="font-family:
  宋体"}[路由删除结果]{lang="EN-US" style="font-family:宋体"}

[[Notified remote peer of adding a tunnel.]{lang="EN-US"}]{#struct_0_x6987_95089_1200255638}

[[通知备用设备添加隧道]{style="font-family:宋体"}]{#struct_0_x6987_95089_1199665813}

[[Notified remote peer of deleting a tunnel.]{lang="EN-US"}]{#struct_0_x6987_95089_1199731349}

[[通知备用设备删除隧道]{style="font-family:宋体"}]{#struct_0_x6987_95089_600564661}

[[Notified remote peer of adding a session.]{lang="EN-US"}]{#struct_0_x6987_95089_1199534741}

[[通知备用设备添加会话]{style="font-family:宋体"}]{#struct_0_x6987_95089_1199600277}

[[Notified remote peer of deleting a session.]{lang="EN-US"}]{#struct_0_x6987_95089_1199403669}

[[通知备用设备删除会话]{style="font-family:宋体"}]{#struct_0_x6987_95089_1013906006}

[[LocalSessionID]{lang="EN-US"}]{#struct_0_x6987_95089_1199469205}

[[会话本端]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x6987_95089_1199272597}

[[RemoteSessionID]{lang="EN-US"}]{#struct_0_x6987_95089_1011118000}

[[会话对端]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x6987_95089_1199338133}

[[PPPUserID]{lang="EN-US"}]{#struct_0_x6987_95089_x1703693317}

[[PPP]{lang="EN-US"}]{#struct_0_x6987_95089_1200190101}[用户]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}[12]{lang="EN-US"}[个字节，由]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[模块告知]{style="font-family:宋体"}[L2TP]{lang="EN-US"}

[[IfName]{lang="EN-US"}]{#struct_0_x6987_95089_1200255637}

[[接口名]{style="font-family:宋体"}]{#struct_0_x6987_95089_x1086690512}

[[Slot]{lang="EN-US"}]{#struct_0_x6987_95089_1199665812}

[[槽位号]{style="font-family:宋体"}]{#struct_0_x6987_95089_1199731348}

[[Deleted an old session after receiving a L2TPV2_VSRP_MSG_TYPE_END_RECONCILE packet.]{lang="EN-US"}]{#struct_0_x6987_95089_1199534740}

[[备用设备平滑结束删除旧的会话]{style="font-family:宋体"}]{#struct_0_x6987_95089_595995250}

[[Deleted an old tunnel after receiving a L2TPV2_VSRP_MSG_TYPE_END_RECONCILE packet.]{lang="EN-US"}]{#struct_0_x6987_95089_1199600276}

[[备用设备平滑结束删除旧的隧道]{style="font-family:宋体"}]{#struct_0_x6987_95089_1199403668}

[[Deleted an old tunnel due to conflicts.]{lang="EN-US"}]{#struct_0_x6987_95089_1199469204}

[[备用设备运行信息冲突，删除旧的隧道]{style="font-family:宋体"}]{#struct_0_x6987_95089_1199272596}

[[Updated a backup tunnel.]{lang="EN-US"}]{#struct_0_x6987_95089_1011183536}

[[备用设备更新一条备份隧道]{style="font-family:宋体"}]{#struct_0_x6987_95089_1199338132}

[[Deleted a backup tunnel.]{lang="EN-US"}]{#struct_0_x6987_95089_1200190100}

[[备用设备删除一条备份隧道]{style="font-family:宋体"}]{#struct_0_x6987_95089_1631134667}

[[Created a backup tunnel.]{lang="EN-US"}]{#struct_0_x6987_95089_1200255636}

[[备用设备添加一条备份隧道]{style="font-family:宋体"}]{#struct_0_x6987_95089_1199665819}

[[Associated the PPP user info with the session.]{lang="EN-US"}]{#struct_0_x6987_95089_1199731355}

[[将]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x6987_95089_601351094}[用户信息和会话关联]{style="font-family:宋体"}

[[Session changed to unassociated state.]{lang="EN-US"}]{#struct_0_x6987_95089_1199534747}

[[会话变为未关联状态]{style="font-family:宋体"}]{#struct_0_x6987_95089_1199600283}

[[Deleted unassociated sessions upon timeout.]{lang="EN-US"}]{#struct_0_x6987_95089_1375688819}

[[因为超时删除未关联上接口索引的会话]{style="font-family:宋体"}]{#struct_0_x6987_95089_1199403675}

[[Deleted exceeded sessions.]{lang="EN-US"}]{#struct_0_x6987_95089_1199469211}

[[会话下驱动过程中，删除超出热备规格范围的会话]{style="font-family:宋体"}]{#struct_0_x6987_95089_1199272603}

[[Deleted exceeded tunnels.]{lang="EN-US"}]{#struct_0_x6987_95089_x562597959}

[[隧道下驱动过程中，删除超出热备规格范围的隧道]{style="font-family:宋体"}]{#struct_0_x6987_95089_1199338139}

[[Deleted a session from driver.]{lang="EN-US"}]{#struct_0_x6987_95089_1200190107}

[[驱动删除会话]{style="font-family:宋体"}]{#struct_0_x6987_95089_1631331275}

[[Added a tunnel to driver.]{lang="EN-US"}]{#struct_0_x6987_95089_1200255643}

[[通知驱动添加隧道]{style="font-family:宋体"}]{#struct_0_x6987_95089_1199665818}

[[Deleted a tunnel to driver.]{lang="EN-US"}]{#struct_0_x6987_95089_2114631227}

[[通知驱动删除隧道]{style="font-family:宋体"}]{#struct_0_x6987_95089_1199731354}

[[VSRP channel closed.]{lang="EN-US"}]{#struct_0_x6987_95089_1199534746}

[[数据备份通道关闭]{style="font-family:宋体"}]{#struct_0_x6987_95089_1199600282}

[[Created a VSRP channel.]{lang="EN-US"}]{#struct_0_x6987_95089_1375623283}

[[创建数据备份通道]{style="font-family:宋体"}]{#struct_0_x6987_95089_1199403674}

[[VSRP channel connected.]{lang="EN-US"}]{#struct_0_x6987_95089_1199469210}

[[数据备份通道连接成功]{style="font-family:宋体"}]{#struct_0_x6987_95089_1199272602}

[[VSRP channel disconnected.]{lang="EN-US"}]{#struct_0_x6987_95089_x562532423}

[[数据备份通道断开成功]{style="font-family:宋体"}]{#struct_0_x6987_95089_1199338138}

[]{#_Toc130718928}[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6987_95089_x1704020997}

[[\# ]{lang="EN-US"}]{#struct_0_x6987_95089_772381766}[主用]{style="font-family:宋体"}[LAC]{lang="EN-US"}[设备]{style="font-family:宋体"}[上打开]{style="font-family:宋体"}[L2TP VSRP]{lang="EN-US"}[的事件和错误调试信息开关。当主用]{style="font-family:宋体"}[LAC]{lang="EN-US"}[设备]{style="font-family:宋体"}[新建]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道和会话时，打印如下调试信息。]{style="font-family:宋体"}

[[\<LAC1\> debugging l2tp vsrp event]{lang="EN-US"}]{#struct_0_x6987_95089_1200190106}

[\<LAC1\> debugging l2tp vsrp error]{lang="EN-US"}

[%Aug 22 11:37:08:345 2013 LAC1 L2TPV2/1/VSRP: -MDC=1;]{lang="EN-US"}

[ PPPLogStatus: Logged in]{lang="EN-US"}

[ VSRPName: msr_a]{lang="EN-US"}

[ LocalVSRPStatus: Master/Up]{lang="EN-US"}

[ RemoteVSRPStatus: Backup]{lang="EN-US"}

[ VSRPBackupMode: Hot]{lang="EN-US"}

[ VSRPChannelStatus: Connected]{lang="EN-US"}

[ NeedReconcilePeer: No]{lang="EN-US"}

[ IsSwitching: No]{lang="EN-US"}

[ VRFIndexLocal: 0]{lang="EN-US"}

[ VRFIndexPeer: 0]{lang="EN-US"}

[ InstanceID: 5]{lang="EN-US"}

[ LocalAddr: 2.2.2.1]{lang="EN-US"}

[ PeerAddr: 2.2.2.2]{lang="EN-US"}

[ IfName: Virtual-Access0]{lang="EN-US"}

[ VSRPName: msr_a]{lang="EN-US"}

[ PPPUserID: 0001ffffffff000c2988aac6]{lang="EN-US"}

[*[// PPP]{lang="EN-US"}*]{#struct_0_x6987_95089_1631265739}*[用户上线。]{style="font-family:宋体"}*

[[\*Aug 22 11:37:08:348 2013 LAC1 L2TPV2/7/VSRP: -MDC=1;]{lang="EN-US"}]{#struct_0_x6987_95089_1658834516}

[ VSRPName: msr_a]{lang="EN-US"}

[ LocalVSRPStatus: Master/Up]{lang="EN-US"}

[ RemoteVSRPStatus: Backup]{lang="EN-US"}

[ VSRPBackupMode: Hot]{lang="EN-US"}

[ VSRPChannelStatus: Connected]{lang="EN-US"}

[ NeedReconcilePeer: No]{lang="EN-US"}

[ IsSwitching: No]{lang="EN-US"}

[ VRFIndexLocal: 0]{lang="EN-US"}

[ VRFIndexPeer: 0]{lang="EN-US"}

[ InstanceID: 5]{lang="EN-US"}

[ LocalAddr: 2.2.2.1]{lang="EN-US"}

[ PeerAddr: 2.2.2.2]{lang="EN-US"}

[ LocalTunnelID: 65127]{lang="EN-US"}

[ RemoteTunnelID: 1]{lang="EN-US"}

[ LocalIPAddr: 5.6.7.8]{lang="EN-US"}

[ RemoteIPAddr: 2.2.2.5]{lang="EN-US"}

[ Notified remote peer of adding a tunnel.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6987_95089_418140573}*[主用]{style="font-family:宋体"}[LAC]{lang="EN-US"}[设备通知备用]{style="font-family:宋体"}[LAC]{lang="EN-US"}[设备添加]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道，隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[65127]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Aug 22 11:37:08:348 2013 LAC1 L2TPV2/7/VSRP: -MDC=1;]{lang="EN-US"}]{#struct_0_x6987_95089_1200255642}

[ VSRPName: msr_a]{lang="EN-US"}

[ LocalVSRPStatus: Master/Up]{lang="EN-US"}

[ RemoteVSRPStatus: Backup]{lang="EN-US"}

[ VSRPBackupMode: Hot]{lang="EN-US"}

[ VSRPChannelStatus: Connected]{lang="EN-US"}

[ NeedReconcilePeer: No]{lang="EN-US"}

[ IsSwitching: No]{lang="EN-US"}

[ VRFIndexLocal: 0]{lang="EN-US"}

[ VRFIndexPeer: 0]{lang="EN-US"}

[ InstanceID: 5]{lang="EN-US"}

[ LocalAddr: 2.2.2.1]{lang="EN-US"}

[ PeerAddr: 2.2.2.2]{lang="EN-US"}

[ SendMessageType: L2TPV2_VSRP_MSG_TYPE_ADD_TUNNEL]{lang="EN-US"}

[ MessageDataLen: 696]{lang="EN-US"}

[ MessageInfo: 04 00 02 b4 02 02 02 05 00 00 00 00 00 00 00 00 00 01 fe 67 00 01 06 a5 ff ff 00 02 00 01 6c 6e 73 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6987_95089_x1086493897}*[主用]{style="font-family:宋体"}[LAC]{lang="EN-US"}[设备向备用]{style="font-family:宋体"}[LAC]{lang="EN-US"}[设备发送实时隧道消息。]{style="font-family:宋体"}*

[[\*Aug 22 11:37:08:349 2013 LAC1 L2TPV2/7/VSRP: -MDC=1;]{lang="EN-US"}]{#struct_0_x6987_95089_x433011095}

[ VSRPName: msr_a]{lang="EN-US"}

[ LocalVSRPStatus: Master/Up]{lang="EN-US"}

[ RemoteVSRPStatus: Backup]{lang="EN-US"}

[ VSRPBackupMode: Hot]{lang="EN-US"}

[ VSRPChannelStatus: Connected]{lang="EN-US"}

[ NeedReconcilePeer: No]{lang="EN-US"}

[ IsSwitching: No]{lang="EN-US"}

[ VRFIndexLocal: 0]{lang="EN-US"}

[ VRFIndexPeer: 0]{lang="EN-US"}

[ InstanceID: 5]{lang="EN-US"}

[ LocalAddr: 2.2.2.1]{lang="EN-US"}

[ PeerAddr: 2.2.2.2]{lang="EN-US"}

[ LocalTunnelID: 65127]{lang="EN-US"}

[ RemoteTunnelID: 1]{lang="EN-US"}

[ LocalIPAddr: 5.6.7.8]{lang="EN-US"}

[ RemoteIPAddr: 2.2.2.5]{lang="EN-US"}

[ Added a tunnel to driver.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6987_95089_x1488098037}*[主用]{style="font-family:宋体"}[LAC]{lang="EN-US"}[设备通知驱动添加隧道]{style="font-family:宋体"}*[。]{style="font-family:宋体"}

[[\*Aug 22 11:37:08:351 2013 LAC1 L2TPV2/7/VSRP: -MDC=1;]{lang="EN-US"}]{#struct_0_x6987_95089_x1529217540}

[ VSRPName: msr_a]{lang="EN-US"}

[ LocalVSRPStatus: Master/Up]{lang="EN-US"}

[ RemoteVSRPStatus: Backup]{lang="EN-US"}

[ VSRPBackupMode: Hot]{lang="EN-US"}

[ VSRPChannelStatus: Connected]{lang="EN-US"}

[ NeedReconcilePeer: No]{lang="EN-US"}

[ IsSwitching: No]{lang="EN-US"}

[ VRFIndexLocal: 0]{lang="EN-US"}

[ VRFIndexPeer: 0]{lang="EN-US"}

[ InstanceID: 5]{lang="EN-US"}

[ LocalAddr: 2.2.2.1]{lang="EN-US"}

[ PeerAddr: 2.2.2.2]{lang="EN-US"}

[ IfName: Virtual-Access0]{lang="EN-US"}

[ Slot: 65535]{lang="EN-US"}

[ LocalTunnelID: 65127]{lang="EN-US"}

[ LocalSessionID: 545]{lang="EN-US"}

[ RemoteSessionID: 618]{lang="EN-US"}

[ PPPUserID: 0001ffffffff000c2988aac6]{lang="EN-US"}

[ Added a session to driver.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6987_95089_1622270913}*[主用]{style="font-family:宋体"}[LAC]{lang="EN-US"}[设备通知驱动添加会话。]{style="font-family:宋体"}*

[[\*Aug 22 11:37:08:351 2013 LAC1 L2TPV2/7/VSRP: -MDC=1;]{lang="EN-US"}]{#struct_0_x6987_95089_x1529152004}

[ VSRPName: msr_a]{lang="EN-US"}

[ LocalVSRPStatus: Master/Up]{lang="EN-US"}

[ RemoteVSRPStatus: Backup]{lang="EN-US"}

[ VSRPBackupMode: Hot]{lang="EN-US"}

[ VSRPChannelStatus: Connected]{lang="EN-US"}

[ NeedReconcilePeer: No]{lang="EN-US"}

[ IsSwitching: No]{lang="EN-US"}

[ VRFIndexLocal: 0]{lang="EN-US"}

[ VRFIndexPeer: 0]{lang="EN-US"}

[ InstanceID: 5]{lang="EN-US"}

[ LocalAddr: 2.2.2.1]{lang="EN-US"}

[ PeerAddr: 2.2.2.2]{lang="EN-US"}

[ LocalTunnelID: 65127]{lang="EN-US"}

[ RemoteTunnelID: 1]{lang="EN-US"}

[ LocalIPAddr: 5.6.7.8]{lang="EN-US"}

[ RemoteIPAddr: 2.2.2.5]{lang="EN-US"}

[ Updated Ns and Nr to remote peer.]{lang="EN-US"}

[*[//]{lang="EN-US"}*]{#struct_0_x6987_95089_x550768276}*[主用]{style="font-family:宋体"}[LAC]{lang="EN-US"}[设备通知备用]{style="font-family:宋体"}[LAC]{lang="EN-US"}[设备更新]{style="font-family:宋体"}[Ns]{lang="EN-US"}[和]{style="font-family:宋体"}[Nr]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Aug 22 11:37:08:351 2013 LAC1 L2TPV2/7/VSRP: -MDC=1;]{lang="EN-US"}]{#struct_0_x6987_95089_x314665084}

[ VSRPName: msr_a]{lang="EN-US"}

[ LocalVSRPStatus: Master/Up]{lang="EN-US"}

[ RemoteVSRPStatus: Backup]{lang="EN-US"}

[ VSRPBackupMode: Hot]{lang="EN-US"}

[ VSRPChannelStatus: Connected]{lang="EN-US"}

[ NeedReconcilePeer: No]{lang="EN-US"}

[ IsSwitching: No]{lang="EN-US"}

[ VRFIndexLocal: 0]{lang="EN-US"}

[ VRFIndexPeer: 0]{lang="EN-US"}

[ InstanceID: 5]{lang="EN-US"}

[ LocalAddr: 2.2.2.1]{lang="EN-US"}

[ PeerAddr: 2.2.2.2]{lang="EN-US"}

[ SendMessageType: L2TPV2_VSRP_MSG_TYPE_REAL_TIME_TUNNEL]{lang="EN-US"}

[ MessageDataLen: 10]{lang="EN-US"}

[ MessageInfo: 05 00 00 06 fe 67 00 03 00 02]{lang="EN-US"}

[*[//]{lang="EN-US"}*]{#struct_0_x6987_95089_542847160}*[主用]{style="font-family:宋体"}[LAC]{lang="EN-US"}[设备发送流控更新消息到备用]{style="font-family:宋体"}[LAC]{lang="EN-US"}[设备。]{style="font-family:宋体"}*

[[\*Aug 22 11:37:08:352 2013 LAC1 L2TPV2/7/VSRP: -MDC=1;]{lang="EN-US"}]{#struct_0_x6987_95089_x1529348612}

[ VSRPName: msr_a]{lang="EN-US"}

[ LocalVSRPStatus: Master/Up]{lang="EN-US"}

[ RemoteVSRPStatus: Backup]{lang="EN-US"}

[ VSRPBackupMode: Hot]{lang="EN-US"}

[ VSRPChannelStatus: Connected]{lang="EN-US"}

[ NeedReconcilePeer: No]{lang="EN-US"}

[ IsSwitching: No]{lang="EN-US"}

[ VRFIndexLocal: 0]{lang="EN-US"}

[ VRFIndexPeer: 0]{lang="EN-US"}

[ InstanceID: 5]{lang="EN-US"}

[ LocalAddr: 2.2.2.1]{lang="EN-US"}

[ PeerAddr: 2.2.2.2]{lang="EN-US"}

[ IfName: Virtual-Access0]{lang="EN-US"}

[ Slot: 65535]{lang="EN-US"}

[ LocalTunnelID: 65127]{lang="EN-US"}

[ LocalSessionID: 545]{lang="EN-US"}

[ RemoteSessionID: 618]{lang="EN-US"}

[ PPPUserID: 0001ffffffff000c2988aac6]{lang="EN-US"}

[ Notified remote peer of adding a session.]{lang="EN-US"}

[*[//]{lang="EN-US"}*]{#struct_0_x6987_95089_x1035813929}*[主用]{style="font-family:宋体"}[LAC]{lang="EN-US"}[设备通知备用]{style="font-family:宋体"}[LAC]{lang="EN-US"}[设备添加会话，本端会话]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[545]{lang="EN-US"}[，远端会话]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[618]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Aug 22 11:37:08:352 2013 LAC1 L2TPV2/7/VSRP: -MDC=1;]{lang="EN-US"}]{#struct_0_x6987_95089_1851319979}

[ VSRPName: msr_a]{lang="EN-US"}

[ LocalVSRPStatus: Master/Up]{lang="EN-US"}

[ RemoteVSRPStatus: Backup]{lang="EN-US"}

[ VSRPBackupMode: Hot]{lang="EN-US"}

[ VSRPChannelStatus: Connected]{lang="EN-US"}

[ NeedReconcilePeer: No]{lang="EN-US"}

[ IsSwitching: No]{lang="EN-US"}

[ VRFIndexLocal: 0]{lang="EN-US"}

[ VRFIndexPeer: 0]{lang="EN-US"}

[ InstanceID: 5]{lang="EN-US"}

[ LocalAddr: 2.2.2.1]{lang="EN-US"}

[ PeerAddr: 2.2.2.2]{lang="EN-US"}

[ SendMessageType: L2TPV2_VSRP_MSG_TYPE_ADD_SESSION]{lang="EN-US"}

[ MessageDataLen: 176]{lang="EN-US"}

[ MessageInfo: 07 00 00 ac 00 00 00 00 00 00 00 00 ff ff fe 67 02 21 02 6a 00 00 00 00 00 00 00 00 ff ff ff ff 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 0c 29 88 aa c6 00 00]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6987_95089_x465414800}*[主用]{style="font-family:宋体"}[LAC]{lang="EN-US"}[设备向备用]{style="font-family:宋体"}[LAC]{lang="EN-US"}[设备发送实时会话备份消息。]{style="font-family:宋体"}*

[ ]{lang="EN-US"}
