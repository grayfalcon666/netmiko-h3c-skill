::: {#-13705271 .myid}
[]{#_Toc404795464}[]{#struct_0_x1112_41438_158417578}[]{#_Toc129683607}

**以太网OAM \-- 以太网OAM配置命令 \-- display oam**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **oam**]{lang="EN-US"}]{#struct_0_x1112_41438_1242283601}[命令用来显示以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[连接的信息，包括连接状态、以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[报文头部信息和以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_181325693}

[**[display]{lang="EN-US"}**[ **oam** { **local** \| **remote** } \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x1112_41438_x402788710}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1725797982}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1112_41438_1857666795}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x413636300}

[[network-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x39732203}

[[network-operator]{lang="EN-US"}]{#struct_0_x1112_41438_158483114}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x1474303224}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1112_41438_167314184}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1112_41438_577355856}

[**[local]{lang="EN-US"}**]{#struct_0_x1112_41438_x1618837611}[：显示本端信息。]{style="font-family:宋体"}

[**[remote]{lang="EN-US"}**]{#struct_0_x1112_41438_x1214218621}[：显示远端信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x1112_41438_1212829861}[：显示指定接口上的信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。如果未指定本参数，将显示所有接口上的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1280783456}

[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_x1644428677}[显示所有接口上以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[连接的本端信息。]{style="font-family:宋体"}

[[\<Sysname\> display oam local]{lang="EN-US"}]{#struct_0_x1112_41438_158548650}

[\-\-\-\-\-\-\-\-\-\-- \[GigabitEthernet1/0/1\] \-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Enable status     : Enable]{lang="EN-US"}

[ Loopback status   : No loopback]{lang="EN-US"}

[ Link status       : UP]{lang="EN-US"}

[ OAM mode          : Active]{lang="EN-US"}

[ PDU               : ANY]{lang="EN-US"}

[ Mux action        : FWD]{lang="EN-US"}

[ Par action        : FWD]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_x1893507037}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[连接的本端信息。]{style="font-family:宋体"}

[[\<Sysname\> display oam local interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_x1112_41438_158614186}

[ Enable status     : Enable]{lang="EN-US"}

[ Loopback status   : No loopback]{lang="EN-US"}

[ Link status       : UP]{lang="EN-US"}

[ OAM mode          : Active]{lang="EN-US"}

[ PDU               : ANY]{lang="EN-US"}

[ Mux action        : FWD]{lang="EN-US"}

[ Par action        : FWD]{lang="EN-US"}

[ Flags]{lang="EN-US"}

[   Link fault        : Not occurred]{lang="EN-US"}

[   Dying gasp        : Not occurred]{lang="EN-US"}

[   Critical event    : Not occurred]{lang="EN-US"}

[   Local evaluating  : COMPLETE]{lang="EN-US"}

[   Remote evaluating : COMPLETE]{lang="EN-US"}

[ Packets statistics]{lang="EN-US"}

[   Packet type                      Sent                   Received]{lang="EN-US"}

[   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[   OAMPDU                           100                    80]{lang="EN-US"}

[   OAMInformation                   64                     60]{lang="EN-US"}

[   OAMEventNotification             36                     20]{lang="EN-US"}

[   OAMUniqueEventNotification       36                     10]{lang="EN-US"}

[   OAMDuplicateEventNotification    0                      10]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display oam local]{lang="EN-US"}]{#struct_0_x1112_41438_x773067789}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_409376132}[[字段]{style="font-family:黑体"}]{#struct_0_x1112_41438_x891205479}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1112_41438_x870284467}

[[GigabitEthernet1/0/1]{lang="EN-US"}]{#struct_0_x1112_41438_1985270851}

[[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}]{#struct_0_x1112_41438_2084403127}[上的信息]{style="font-family:宋体"}

[[Enable status]{lang="EN-US"}]{#struct_0_x1112_41438_158155434}

[[本端的以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x1112_41438_x1624815306}[状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enable]{lang="EN-US"}]{#struct_0_x1112_41438_x384298949}[：表示已使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disable]{lang="EN-US"}]{#struct_0_x1112_41438_x1672241300}[：表示未使能]{lang="EN-US" style="font-family:宋体"}

[[Loopback status]{lang="EN-US"}]{#struct_0_x1112_41438_563746999}

[[以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x1112_41438_x1536805680}[远端环回状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No loopback]{lang="EN-US"}]{#struct_0_x1112_41438_158220970}[：表示尚未建立远端环回]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Remote loopback]{lang="EN-US"}]{#struct_0_x1112_41438_1812154230}[：表示远端环回的主控端]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Local loopback]{lang="EN-US"}]{#struct_0_x1112_41438_x67577999}[：表示远端环回的被控端]{lang="EN-US" style="font-family:宋体"}

[[Link status]{lang="EN-US"}]{#struct_0_x1112_41438_x1843271371}

[[链路状态：]{style="font-family:宋体"}]{#struct_0_x1112_41438_678358857}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x1112_41438_506508362}[：表示链路]{lang="EN-US" style="font-family:宋体"}[up]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x1112_41438_158286506}[：表示链路]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}

[[OAM mode]{lang="EN-US"}]{#struct_0_x1112_41438_x1744323210}

[[本端以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x1112_41438_x2137201848}[的连接模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_x1112_41438_611077169}[：表示主动模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Passive]{lang="EN-US"}]{#struct_0_x1112_41438_958165493}[：表示被动模式]{lang="EN-US" style="font-family:宋体"}

[[PDU]{lang="EN-US"}]{#struct_0_x1112_41438_158352042}

[[本端对]{style="font-family:宋体"}[OAMPDU]{lang="EN-US"}]{#struct_0_x1112_41438_x963807536}[的处理方式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RX_INFO]{lang="EN-US"}]{#struct_0_x1112_41438_293491206}[：表示只接收]{lang="EN-US" style="font-family:宋体"}[Information OAMPDU]{lang="EN-US"}[，不允许发送任何]{lang="EN-US" style="font-family:宋体"}[OAMPDU]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LF_INFO]{lang="EN-US"}]{#struct_0_x1112_41438_x1833766783}[：表示只发送不带]{lang="EN-US" style="font-family:宋体"}[Information TLV]{lang="EN-US"}[且链路错误标志位已被置位的]{lang="EN-US" style="font-family:宋体"}[Information OAMPDU]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INFO]{lang="EN-US"}]{#struct_0_x1112_41438_x1818964218}[：表示只收发]{lang="EN-US" style="font-family:宋体"}[Information OAMPDU]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ANY]{lang="EN-US"}]{#struct_0_x1112_41438_158941866}[：表示可收发所有]{lang="EN-US" style="font-family:宋体"}[OAMPDU]{lang="EN-US"}

[[Mux action]{lang="EN-US"}]{#struct_0_x1112_41438_x1339895277}

[[本端发送器的工作方式：]{style="font-family:宋体"}]{#struct_0_x1112_41438_x1156848473}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FWD]{lang="EN-US"}]{#struct_0_x1112_41438_x377299414}[：表示发送方向为]{lang="EN-US" style="font-family:宋体"}[FORWARDING]{lang="EN-US"}[，允许发送任何报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DISCARD]{lang="EN-US"}]{#struct_0_x1112_41438_159007402}[：表示发送方向为]{lang="EN-US" style="font-family:宋体"}[DISCARDING]{lang="EN-US"}[，只允许发送]{lang="EN-US" style="font-family:宋体"}[OAMPDU]{lang="EN-US"}

[[Par action]{lang="EN-US"}]{#struct_0_x1112_41438_855780122}

[[本端接收器的工作方式：]{style="font-family:宋体"}]{#struct_0_x1112_41438_x1828402424}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FWD]{lang="EN-US"}]{#struct_0_x1112_41438_x71611569}[：表示接收方向为]{lang="EN-US" style="font-family:宋体"}[FORWARDING]{lang="EN-US"}[，允许接收任何报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DISCARD]{lang="EN-US"}]{#struct_0_x1112_41438_158417575}[：表示接收方向为]{lang="EN-US" style="font-family:宋体"}[DISCARDING]{lang="EN-US"}[，只允许接收]{lang="EN-US" style="font-family:宋体"}[OAMPDU]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LB]{lang="EN-US"}]{#struct_0_x1112_41438_1242283612}[：表示接收方向处于环回状态，收到的所有非]{style="font-family:宋体"}[OAMPDU]{lang="EN-US"}[都将按原路返回]{style="font-family:宋体"}

[[Flags]{lang="EN-US"}]{#struct_0_x1112_41438_181522300}

[[以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x1112_41438_x1319327850}[报文中的本端标识域]{style="font-family:宋体"}

[[Link fault]{lang="EN-US"}]{#struct_0_x1112_41438_158483111}

[[是否发生链路故障：]{style="font-family:宋体"}]{#struct_0_x1112_41438_x1474303227}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Occurred]{lang="EN-US"}]{#struct_0_x1112_41438_1733398125}[：表示已发生]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not occurred]{lang="EN-US"}]{#struct_0_x1112_41438_x1081296365}[：表示未发生]{lang="EN-US" style="font-family:宋体"}

[[Dying gasp]{lang="EN-US"}]{#struct_0_x1112_41438_158548647}

[[是否发生致命故障：]{style="font-family:宋体"}]{#struct_0_x1112_41438_445145122}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Occurred]{lang="EN-US"}]{#struct_0_x1112_41438_x1646486539}[：表示已发生]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not occurred]{lang="EN-US"}]{#struct_0_x1112_41438_707378015}[：表示未发生]{lang="EN-US" style="font-family:宋体"}

[[Critical event]{lang="EN-US"}]{#struct_0_x1112_41438_158614183}

[[是否发生紧急事件：]{style="font-family:宋体"}]{#struct_0_x1112_41438_x773067794}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Occurred]{lang="EN-US"}]{#struct_0_x1112_41438_x891008870}[：表示已发生]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not occurred]{lang="EN-US"}]{#struct_0_x1112_41438_158155431}[：表示未发生]{lang="EN-US" style="font-family:宋体"}

[[Local evaluating]{lang="EN-US"}]{#struct_0_x1112_41438_x1624815303}

[[本端对远端配置的协商过程：]{style="font-family:宋体"}]{#struct_0_x1112_41438_375215938}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[COMPLETE]{lang="EN-US"}]{#struct_0_x1112_41438_158026932}[：表示协商已完成]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NOTCOMPLETE]{lang="EN-US"}]{#struct_0_x1112_41438_158220967}[：表示协商未完成]{lang="EN-US" style="font-family:宋体"}

[[Remote evaluating]{lang="EN-US"}]{#struct_0_x1112_41438_x526497927}

[[远端对本端配置的协商过程：]{style="font-family:宋体"}]{#struct_0_x1112_41438_1833929918}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[COMPLETE]{lang="EN-US"}]{#struct_0_x1112_41438_158286503}[：表示协商已完成]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NOTCOMPLETE]{lang="EN-US"}]{#struct_0_x1112_41438_x1744323213}[：表示协商未完成]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RESERVED]{lang="EN-US"}]{#struct_0_x1112_41438_x571117907}[：表示此字段为保留值，协商未完成]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UNSATISFIED]{lang="EN-US"}]{#struct_0_x1112_41438_158352039}[：表示远端对本端的配置不满意，协商未完成]{lang="EN-US" style="font-family:宋体"}

[[Packets statistics]{lang="EN-US"}]{#struct_0_x1112_41438_x154503467}

[[各种以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x1112_41438_1687786651}[报文的发送和接收数量]{style="font-family:宋体"}

[[Packet type]{lang="EN-US"}]{#struct_0_x1112_41438_158941863}

[[报文类型]{style="font-family:宋体"}]{#struct_0_x1112_41438_x1339895272}

[[Sent]{lang="EN-US"}]{#struct_0_x1112_41438_x397333586}

[[发送的报文数量]{style="font-family:宋体"}]{#struct_0_x1112_41438_1836697595}

[[Received]{lang="EN-US"}]{#struct_0_x1112_41438_159007399}

[[收到的报文数量]{style="font-family:宋体"}]{#struct_0_x1112_41438_x257230124}

[[OAMPDU]{lang="EN-US"}]{#struct_0_x1112_41438_x698158619}

[[以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x1112_41438_158417576}[报文]{style="font-family:宋体"}

[[OAMInformation]{lang="EN-US"}]{#struct_0_x1112_41438_1242283615}

[[以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x1112_41438_158483112}[信息报文]{style="font-family:宋体"}

[[OAMEventNotification]{lang="EN-US"}]{#struct_0_x1112_41438_x1474303226}

[[以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x1112_41438_x995485230}[事件通知报文]{style="font-family:宋体"}

[[OAMUniqueEventNotification]{lang="EN-US"}]{#struct_0_x1112_41438_158548648}

[[以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x1112_41438_445145131}[一次性发送或接收的事件报文]{style="font-family:宋体"}

[[OAMDuplicateEventNotification]{lang="EN-US"}]{#struct_0_x1112_41438_309828600}

[[以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x1112_41438_158614184}[重复发送或接收的事件报文]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_x773067791}[显示所有接口上以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[连接的远端信息。]{style="font-family:宋体"}

[[\<Sysname\> display oam remote]{lang="EN-US"}]{#struct_0_x1112_41438_x890681190}

[\-\-\-\-\-\-\-\-\-\-- \[GigabitEthernet1/0/1\] \-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ OAM mode          : Active]{lang="EN-US"}

[ MAC address       : 3822-d6a2-a800]{lang="EN-US"}

[ ]{lang="EN-US"}[MTU size          : 1500]{lang="FR"}

[ Mux action        : FWD]{lang="FR"}

[ Par action        : FWD]{lang="FR"}

[[\# ]{lang="FR"}]{#struct_0_x1112_41438_x859721261}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="FR"}[上以太网]{style="font-family:宋体"}[OAM]{lang="FR"}[连接的远端信息。]{style="font-family:宋体"}

[]{#_Toc98246493}[[\<Sysname\> display oam remote interface gigabitethernet 1/0/1]{lang="FR"}]{#struct_0_x1112_41438_158155432}

[ OAM mode          : Active]{lang="FR"}

[ ]{lang="FR"}[MAC address       : 3822-d6a2-a800]{lang="EN-US"}

[ ]{lang="EN-US"}[MTU size          : 1500]{lang="FR"}

[ Mux action        : FWD]{lang="FR"}

[ Par action        : FWD]{lang="FR"}

[ ]{lang="FR"}[Configuration]{lang="EN-US"}

[   Unidirectional    : Not supported]{lang="EN-US"}

[   Remote loopback   : Supported]{lang="EN-US"}

[   Link events       : Supported]{lang="EN-US"}

[   MIB retrieval     : Not supported]{lang="EN-US"}

[ Flags]{lang="EN-US"}

[   Link fault        : Not occurred]{lang="EN-US"}

[   Dying gasp        : Not occurred]{lang="EN-US"}

[   Critical event    : Not occurred]{lang="EN-US"}

[   Local evaluating  : COMPLETE]{lang="EN-US"}

[   Remote evaluating : COMPLETE]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display oam remote]{lang="EN-US"}]{#struct_0_x1112_41438_x1624815300}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_435927430}[[字段]{style="font-family:黑体"}]{#struct_0_x1112_41438_778500465}

[[描述]{style="font-family:黑体"}]{#struct_0_x1112_41438_1864839260}

[[GigabitEthernet1/0/1]{lang="EN-US"}]{#struct_0_x1112_41438_158220968}

[[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}]{#struct_0_x1112_41438_x526497938}[上的信息]{style="font-family:宋体"}

[[OAM mode]{lang="EN-US"}]{#struct_0_x1112_41438_1833602239}

[[远端的以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x1112_41438_x1490616820}[连接模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_x1112_41438_242411982}[：表示主动模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Passive]{lang="EN-US"}]{#struct_0_x1112_41438_977092719}[：表示被动模式]{lang="EN-US" style="font-family:宋体"}

[[MAC address]{lang="EN-US"}]{#struct_0_x1112_41438_158286504}

[[远端的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1112_41438_x1744323212}[地址]{style="font-family:宋体"}

[[MTU size]{lang="EN-US"}]{#struct_0_x1112_41438_994966034}

[[以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x1112_41438_x596483784}[实体间传送的报文最大长度，单位为字节]{style="font-family:宋体"}

[[Mux action]{lang="FR"}]{#struct_0_x1112_41438_x1104033701}

[[远端发送器的工作方式]{style="font-family:宋体"}]{#struct_0_x1112_41438_378421607}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FWD]{lang="EN-US"}]{#struct_0_x1112_41438_158352040}[：表示发送方向为]{lang="EN-US" style="font-family:宋体"}[FORWARDING]{lang="EN-US"}[，允许发送任何报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DISCARD]{lang="EN-US"}]{#struct_0_x1112_41438_x963807538}[：表示发送方向为]{lang="EN-US" style="font-family:宋体"}[DISCARDING]{lang="EN-US"}[，只允许发送]{lang="EN-US" style="font-family:宋体"}[OAMPDU]{lang="EN-US"}

[[Par action]{lang="FR"}]{#struct_0_x1112_41438_293884422}

[[远端接收器的工作方式：]{style="font-family:宋体"}]{#struct_0_x1112_41438_x550161112}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FWD]{lang="EN-US"}]{#struct_0_x1112_41438_x678527639}[：表示接收方向为]{lang="EN-US" style="font-family:宋体"}[FORWARDING]{lang="EN-US"}[，允许接收任何报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DISCARD]{lang="EN-US"}]{#struct_0_x1112_41438_158941864}[：表示接收方向为]{lang="EN-US" style="font-family:宋体"}[DISCARDING]{lang="EN-US"}[，只允许接收]{lang="EN-US" style="font-family:宋体"}[OAMPDU]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LB]{lang="EN-US"}]{#struct_0_x1112_41438_x1339895279}[：表示接收方向处于环回状态，收到的所有非]{style="font-family:宋体"}[OAMPDU]{lang="EN-US"}[都将按原路返回]{style="font-family:宋体"}

[[Configuration]{lang="FR"}]{#struct_0_x1112_41438_1975319409}

[[远端以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x1112_41438_x801170505}[实体的配置信息]{style="font-family:宋体"}

[[Unidirectional]{lang="EN-US"}]{#struct_0_x1112_41438_1920921823}

[[是否支持单向传输：]{style="font-family:宋体"}]{#struct_0_x1112_41438_159007400}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Supported]{lang="EN-US"}]{#struct_0_x1112_41438_855780120}[：表示支持]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not supported]{lang="EN-US"}]{#struct_0_x1112_41438_x1828402426}[：表示不支持]{lang="EN-US" style="font-family:宋体"}

[[Remote loopback]{lang="EN-US"}]{#struct_0_x1112_41438_1091187845}

[[是否支持远端环回：]{style="font-family:宋体"}]{#struct_0_x1112_41438_984206637}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Supported]{lang="EN-US"}]{#struct_0_x1112_41438_1724501520}[：表示支持]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not supported]{lang="EN-US"}]{#struct_0_x1112_41438_607037401}[：表示不支持]{lang="EN-US" style="font-family:宋体"}

[[Link events]{lang="EN-US"}]{#struct_0_x1112_41438_x2071795382}

[[是否支持一般链路事件：]{style="font-family:宋体"}]{#struct_0_x1112_41438_41981959}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Supported]{lang="EN-US"}]{#struct_0_x1112_41438_1724567056}[：表示支持]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not supported]{lang="EN-US"}]{#struct_0_x1112_41438_616218268}[：表示不支持]{lang="EN-US" style="font-family:宋体"}

[[MIB retrieval]{lang="EN-US"}]{#struct_0_x1112_41438_x574415068}

[[是否支持获取]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_x1112_41438_x457285547}[变量：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Supported]{lang="EN-US"}]{#struct_0_x1112_41438_1724632592}[：表示支持]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not supported]{lang="EN-US"}]{#struct_0_x1112_41438_x969597732}[：表示不支持]{lang="EN-US" style="font-family:宋体"}

[[Flags]{lang="EN-US"}]{#struct_0_x1112_41438_299454817}

[[以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x1112_41438_1815914360}[报文中的远端标识域]{style="font-family:宋体"}

[[Link fault]{lang="EN-US"}]{#struct_0_x1112_41438_1724698128}

[[是否发生链路故障：]{style="font-family:宋体"}]{#struct_0_x1112_41438_1775097971}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Occurred]{lang="EN-US"}]{#struct_0_x1112_41438_1790475284}[：表示已发生]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not occurred]{lang="EN-US"}]{#struct_0_x1112_41438_1724239376}[：表示未发生]{lang="EN-US" style="font-family:宋体"}

[[Dying gasp]{lang="EN-US"}]{#struct_0_x1112_41438_x194032233}

[[是否发生致命故障：]{style="font-family:宋体"}]{#struct_0_x1112_41438_2091138060}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Occurred]{lang="EN-US"}]{#struct_0_x1112_41438_x560814355}[：表示已发生]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not occurred]{lang="EN-US"}]{#struct_0_x1112_41438_1724304912}[：表示未发生]{lang="EN-US" style="font-family:宋体"}

[[Critical event]{lang="EN-US"}]{#struct_0_x1112_41438_1848598933}

[[是否发生紧急事件：]{style="font-family:宋体"}]{#struct_0_x1112_41438_739895306}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Occurred]{lang="EN-US"}]{#struct_0_x1112_41438_1724370448}[：表示已发生]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not occurred]{lang="EN-US"}]{#struct_0_x1112_41438_x183290874}[：表示未发生]{lang="EN-US" style="font-family:宋体"}

[[Local evaluating]{lang="EN-US"}]{#struct_0_x1112_41438_1298023489}

[[本端对远端配置的协商过程：]{style="font-family:宋体"}]{#struct_0_x1112_41438_x81200428}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[COMPLETE]{lang="EN-US"}]{#struct_0_x1112_41438_1724435984}[：表示协商已完成]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NOTCOMPLETE]{lang="EN-US"}]{#struct_0_x1112_41438_271963538}[：表示协商未完成]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RESERVED]{lang="EN-US"}]{#struct_0_x1112_41438_x63285586}[：表示此字段为保留值，协商未完成]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UNSATISFIED]{lang="EN-US"}]{#struct_0_x1112_41438_1725025808}[：表示本端对远端的配置不满意，协商未完成]{lang="EN-US" style="font-family:宋体"}

[[Remote evaluating]{lang="EN-US"}]{#struct_0_x1112_41438_x1276062194}

[[远端对本端配置的协商过程：]{style="font-family:宋体"}]{#struct_0_x1112_41438_688013251}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[COMPLETE]{lang="EN-US"}]{#struct_0_x1112_41438_1725091344}[：表示协商已完成]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NOTCOMPLETE]{lang="EN-US"}]{#struct_0_x1112_41438_637577342}[：表示协商未完成]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UNSATISFIED]{lang="EN-US"}]{#struct_0_x1112_41438_76188440}[：表示本端对远端的配置不满意，协商未完成]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x224606442}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset]{lang="EN-US"}**[ **oam**]{lang="EN-US"}]{#struct_0_x1112_41438_x832956312}

::: {#-1981072478 .myid}
[]{#_Toc404795465}[]{#struct_0_x1112_41438_1724501521}[]{#_Toc129683608}

**以太网OAM \-- 以太网OAM配置命令 \-- display oam configuration**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **oam** **configuration**]{lang="EN-US"}]{#struct_0_x1112_41438_607102937}[命令用来显示以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[的配置信息，包括各一般链路事件的检测窗口和检测阈值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x58393074}

[**[display]{lang="EN-US"}**[ **oam** **configuration** \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x1112_41438_607995210}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1112_41438_911475039}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1112_41438_x1268309291}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1730057989}

[[network-admin]{lang="EN-US"}]{#struct_0_x1112_41438_1037285185}

[[network-operator]{lang="EN-US"}]{#struct_0_x1112_41438_x1051734450}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1112_41438_1724567057}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1112_41438_616283804}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1691643277}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x1112_41438_x1786398241}[：显示指定接口上的信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。如果未指定本参数，将显示全局以及未采用缺省配置的接口上的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1135492578}

[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_1151663562}[显示全局以及未采用缺省配置的接口上的以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display oam configuration]{lang="EN-US"}]{#struct_0_x1112_41438_1724632593}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- \[Global\] \-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="NO-BOK"}

[ OAM timers]{lang="NO-BOK"}

[   Hello timer        : 1000 milliseconds]{lang="NO-BOK"}

[   Keepalive timer    : 5000 milliseconds]{lang="EN-US"}

[ Link monitoring]{lang="EN-US"}

[   Errored symbol period]{lang="EN-US"}

[     Window           : 100 x 1000000 symbols]{lang="EN-US"}

[     Threshold        : 1 error symbols]{lang="EN-US"}

[   Errored frame]{lang="EN-US"}

[     Window           : 10 x 100 milliseconds]{lang="EN-US"}

[     Threshold        : 1 error frames]{lang="EN-US"}

[   Errored frame period]{lang="EN-US"}

[     Window           : 1000 x 10000 frames]{lang="EN-US"}

[     Threshold        : 1 error frames]{lang="EN-US"}

[   Errored frame seconds]{lang="EN-US"}

[     Window           : 600 x 100 milliseconds]{lang="EN-US"}

[     Threshold        : 1 error seconds]{lang="EN-US"}

[ ]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-- \[GigabitEthernet1/0/1\] \-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ OAM timers]{lang="NO-BOK"}

[   Hello timer        : 500 milliseconds]{lang="NO-BOK"}

[   Keepalive timer    : 5000 milliseconds]{lang="NO-BOK"}

[ ]{lang="NO-BOK"}[Link monitoring]{lang="EN-US"}

[   Errored symbol period]{lang="EN-US"}

[     Window           : 100 x 1000000 symbols]{lang="EN-US"}

[     Threshold        : 1 error symbols]{lang="EN-US"}

[   Errored frame]{lang="EN-US"}

[     Window           : 10 x 100 milliseconds]{lang="EN-US"}

[     Threshold        : 1 error frames]{lang="EN-US"}

[   Errored frame period]{lang="EN-US"}

[     Window           : 1000 x 10000 frames]{lang="EN-US"}

[     Threshold        : 1 error frames]{lang="EN-US"}

[   Errored frame seconds]{lang="EN-US"}

[     Window           : 600 x 100 milliseconds]{lang="EN-US"}

[     Threshold        : 1 error seconds]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display oam configuration]{lang="EN-US"}]{#struct_0_x1112_41438_1724698129}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_424902936}[[字段]{style="font-family:黑体"}]{#struct_0_x1112_41438_1775032435}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1784865217}

[[Global]{lang="NO-BOK"}]{#struct_0_x1112_41438_x69067995}

[[全局信息]{style="font-family:宋体"}]{#struct_0_x1112_41438_620694776}

[[GigabitEthernet1/0/1]{lang="EN-US"}]{#struct_0_x1112_41438_x1109236513}

[[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}]{#struct_0_x1112_41438_x110536562}[上的信息]{style="font-family:宋体"}

[[OAM timers]{lang="EN-US"}]{#struct_0_x1112_41438_1724239377}

[[以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x1112_41438_x194097769}[连接检测定时器]{style="font-family:宋体"}

[[Hello timer]{lang="EN-US"}]{#struct_0_x1112_41438_475240922}

[[以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x1112_41438_2125152464}[握手报文的发送间隔]{style="font-family:宋体"}

[[Keepalive timer]{lang="EN-US"}]{#struct_0_x1112_41438_x2100752338}

[[以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x1112_41438_2098872356}[连接的超时时间]{style="font-family:宋体"}

[[Link monitoring]{lang="EN-US"}]{#struct_0_x1112_41438_1724304913}

[[一般链路事件的检测窗口和检测阈值]{style="font-family:宋体"}]{#struct_0_x1112_41438_1848664469}

[[Errored symbol period]{lang="EN-US"}]{#struct_0_x1112_41438_1980002594}

[[错误信号事件]{style="font-family:宋体"}]{#struct_0_x1112_41438_x1589080525}

[[Errored frame]{lang="EN-US"}]{#struct_0_x1112_41438_1153631739}

[[错误帧事件]{style="font-family:宋体"}]{#struct_0_x1112_41438_1724370449}

[[Errored frame period]{lang="EN-US"}]{#struct_0_x1112_41438_x183356410}

[[错误帧周期事件]{style="font-family:宋体"}]{#struct_0_x1112_41438_468266432}

[[Errored frame seconds]{lang="EN-US"}]{#struct_0_x1112_41438_x1685178978}

[[错误帧秒事件]{style="font-family:宋体"}]{#struct_0_x1112_41438_451754676}

[[Window]{lang="EN-US"}]{#struct_0_x1112_41438_1724435985}

[[检测窗口]{style="font-family:宋体"}]{#struct_0_x1112_41438_271898002}

[[Threshold]{lang="EN-US"}]{#struct_0_x1112_41438_1536096088}

[[检测阈值]{style="font-family:宋体"}]{#struct_0_x1112_41438_x400610340}

[ ]{lang="EN-US"}

::: {#108458142 .myid}
[]{#_Toc404795466}[]{#struct_0_x1112_41438_1123348904}[]{#_Toc129683609}

**以太网OAM \-- 以太网OAM配置命令 \-- display oam critical-event**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **oam** **critical-event**]{lang="EN-US"}]{#struct_0_x1112_41438_788519131}[命令用来显示以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[的紧急链路事件统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1725025809}

[**[display]{lang="EN-US"}**[ **oam** **critical-event** \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x1112_41438_x1275996658}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x540433966}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1112_41438_767597752}

[[【缺省用户角色】]{style="font-family:
黑体"}]{#struct_0_x1112_41438_418670}

[[network-admin]{lang="EN-US"}]{#struct_0_x1112_41438_1512006809}

[[network-operator]{lang="EN-US"}]{#struct_0_x1112_41438_165080666}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x577935252}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1112_41438_215834799}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1725091345}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x1112_41438_637511806}[：显示指定接口上的信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。如果未指定本参数，将显示所有接口上的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1112_41438_517042763}

[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_x684561521}[显示所有接口上以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[紧急链路事件的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display oam critical-event]{lang="EN-US"}]{#struct_0_x1112_41438_x628704921}

[\-\-\-\-\-\-\-\-\-\-- \[GigabitEthernet1/0/1\] \-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Local link status   : UP]{lang="EN-US"}

[ Event statistics]{lang="EN-US"}

[   Link fault        : Not occurred]{lang="EN-US"}

[   Dying gasp        : Not occurred]{lang="EN-US"}

[   Critical event    : Not occurred]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display oam critical-event]{lang="EN-US"}]{#struct_0_x1112_41438_1687760652}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_420749574}[[字段]{style="font-family:黑体"}]{#struct_0_x1112_41438_2033743627}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1112_41438_1724501518}

[[GigabitEthernet1/0/1]{lang="EN-US"}]{#struct_0_x1112_41438_607561686}

[[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}]{#struct_0_x1112_41438_x1105800712}[上的信息]{style="font-family:宋体"}

[[Local link status]{lang="EN-US"}]{#struct_0_x1112_41438_x1479950884}

[[本端的链路状态：]{style="font-family:宋体"}]{#struct_0_x1112_41438_x1633194646}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x1112_41438_x78589945}[：表示链路]{lang="EN-US" style="font-family:宋体"}[up]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x1112_41438_1724567054}[：表示链路]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}

[[Event statistics]{lang="EN-US"}]{#struct_0_x1112_41438_616349340}

[[紧急链路事件的统计信息]{style="font-family:宋体"}]{#struct_0_x1112_41438_x211643500}

[[Link fault]{lang="EN-US"}]{#struct_0_x1112_41438_x1308920562}

[[是否发生链路故障：]{style="font-family:宋体"}]{#struct_0_x1112_41438_1799871779}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Occurred]{lang="EN-US"}]{#struct_0_x1112_41438_x607526128}[：表示已发生]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not occurred]{lang="EN-US"}]{#struct_0_x1112_41438_1724632590}[：表示未发生]{lang="EN-US" style="font-family:宋体"}

[[Dying gasp]{lang="EN-US"}]{#struct_0_x1112_41438_x969728804}

[[是否发生致命故障：]{style="font-family:宋体"}]{#struct_0_x1112_41438_x2039120753}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Occurred]{lang="EN-US"}]{#struct_0_x1112_41438_719204652}[：表示已发生]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not occurred]{lang="EN-US"}]{#struct_0_x1112_41438_1800743003}[：表示未发生]{lang="EN-US" style="font-family:宋体"}

[[Critical event]{lang="EN-US"}]{#struct_0_x1112_41438_1509338862}

[[是否发生紧急事件：]{style="font-family:宋体"}]{#struct_0_x1112_41438_1724698126}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Occurred]{lang="EN-US"}]{#struct_0_x1112_41438_1775753331}[：表示已发生]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not occurred]{lang="EN-US"}]{#struct_0_x1112_41438_1352706365}[：表示未发生]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#80402374 .myid}
[]{#_Toc404795467}[]{#struct_0_x1112_41438_x657954540}[]{#_Toc129683610}

**以太网OAM \-- 以太网OAM配置命令 \-- display oam link-event**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **oam** **link-event**]{lang="EN-US"}]{#struct_0_x1112_41438_225648765}[命令用来显示以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[的一般链路事件统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_58714324}

[**[display]{lang="EN-US"}**[ **oam** **link-event** { **local** \| **remote** } \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x1112_41438_1724239374}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x194163305}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1112_41438_1699137489}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1553937120}

[[network-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x143177820}

[[network-operator]{lang="EN-US"}]{#struct_0_x1112_41438_1727318466}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x293087012}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1112_41438_x1656448549}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1112_41438_31077140}

[**[local]{lang="EN-US"}**]{#struct_0_x1112_41438_1724304910}[：显示本端统计信息。]{style="font-family:宋体"}

[**[remote]{lang="EN-US"}**]{#struct_0_x1112_41438_1848467861}[：显示远端统计信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x1112_41438_1545665609}[：显示指定接口上的信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。如果未指定本参数，将显示所有接口上的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1277027778}

[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_x1366197229}[显示所有接口上以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[一般链路事件的本端统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display oam link-event local]{lang="EN-US"}]{#struct_0_x1112_41438_1724370446}

[\-\-\-\-\-\-\-\-\-\-- \[GigabitEthernet1/0/1\] \-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Link status: UP]{lang="EN-US"}

[ OAM local errored frame event]{lang="EN-US"}

[   Event time stamp        : 49582 x 100 milliseconds]{lang="EN-US"}

[   Errored frame window    : 10 x 100 milliseconds]{lang="EN-US"}

[   Errored frame threshold : 1 error frames]{lang="EN-US"}

[   Errored frame           : 1 error frames]{lang="EN-US"}

[   Error running total     : 6 error frames]{lang="EN-US"}

[   Event running total     : 6 events]{lang="EN-US"}

[ OAM local errored frame period event]{lang="EN-US"}

[   Event time stamp                : 16382 x 100 milliseconds]{lang="EN-US"}

[   Errored frame period window     : 10000000 frames]{lang="EN-US"}

[   Errored frame period threshold  : 1 error frames]{lang="EN-US"}

[   Errored frame period            : 1 error frames]{lang="EN-US"}

[   Error running total             : 5 error frames]{lang="EN-US"}

[   Event running total             : 5 events]{lang="EN-US"}

[ OAM local errored frame seconds summary event]{lang="EN-US"}

[   Event time stamp                : 50022 x 100 milliseconds]{lang="EN-US"}

[   Errored frame seconds window    : 600 x 100 milliseconds]{lang="EN-US"}

[   Errored frame seconds threshold : 1 error seconds]{lang="EN-US"}

[   Errored frame seconds           : 1 error seconds]{lang="EN-US"}

[   Error running total             : 1 error seconds]{lang="EN-US"}

[   Event running total             : 1 events]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_x182897658}[显示所有接口上以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[一般链路事件的远端统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display oam link-event remote]{lang="EN-US"}]{#struct_0_x1112_41438_1724435982}

[\-\-\-\-\-\-\-\-\-\-- \[GigabitEthernet1/0/1\] \-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Link status: UP]{lang="EN-US"}

[ OAM remote errored symbol event]{lang="EN-US"}

[   Event time stamp         : 35498 x 100 milliseconds]{lang="EN-US"}

[   Errored symbol window    : 100000000  symbols]{lang="EN-US"}

[   Errored symbol threshold : 1 error symbols]{lang="EN-US"}

[   Errored symbol           : 1 error symbols]{lang="EN-US"}

[   Error running total      : 4 error symbols]{lang="EN-US"}

[   Event running total      : 4 events]{lang="EN-US"}

[ OAM remote errored frame event]{lang="EN-US"}

[   Event time stamp        : 49582 x 100 milliseconds]{lang="EN-US"}

[   Errored frame window    : 10 x 100 milliseconds]{lang="EN-US"}

[   Errored frame threshold : 1 error frames]{lang="EN-US"}

[   Errored frame           : 1 error frames]{lang="EN-US"}

[   Error running total     : 6 error frames]{lang="EN-US"}

[   Event running total     : 6 events]{lang="EN-US"}

[ OAM remote errored frame period event]{lang="EN-US"}

[   Event time stamp                : 16382 x 100 milliseconds]{lang="EN-US"}

[   Errored frame period window     : 10000000 frames]{lang="EN-US"}

[   Errored frame period threshold  : 1 error frames]{lang="EN-US"}

[   Errored frame period            : 1 error frames]{lang="EN-US"}

[   Error running total             : 5 error frames]{lang="EN-US"}

[   Event running total             : 5 events]{lang="EN-US"}

[ OAM remote errored frame seconds summary event]{lang="EN-US"}

[   Event time stamp                : 50022 x 100 milliseconds]{lang="EN-US"}

[   Errored frame seconds window    : 600 x 100 milliseconds]{lang="EN-US"}

[   Errored frame seconds threshold : 1 error seconds]{lang="EN-US"}

[   Errored frame seconds           : 1 error seconds]{lang="EN-US"}

[   Error running total             : 1 error seconds]{lang="EN-US"}

[   Event running total             : 1 events]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display oam link-event]{lang="EN-US"}]{#struct_0_x1112_41438_271832466}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_423093380}[[字段]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1601910166}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1038741576}

[[GigabitEthernet1/0/1]{lang="EN-US"}]{#struct_0_x1112_41438_1725025806}

[[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}]{#struct_0_x1112_41438_x1276455410}[上的信息]{style="font-family:宋体"}

[[Link status]{lang="EN-US"}]{#struct_0_x1112_41438_2103193849}

[[链路状态：]{style="font-family:宋体"}]{#struct_0_x1112_41438_310092393}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x1112_41438_1621337513}[：表示链路]{lang="EN-US" style="font-family:宋体"}[up]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x1112_41438_x2006728858}[：表示链路]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}

[[OAM remote errored symbol event]{lang="EN-US"}]{#struct_0_x1112_41438_1725091342}

[[远端产生的错误信号事件信息（只有产生了错误信号事件才会显示）：]{style="font-family:宋体"}]{#struct_0_x1112_41438_637184126}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Event time stamp]{lang="EN-US"}]{#struct_0_x1112_41438_x1998019603}[：表示错误信号事件的发生时间]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Errored symbol window]{lang="EN-US"}]{#struct_0_x1112_41438_552496184}[：表示错误信号事件的检测窗口]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Errored symbol threshold]{lang="EN-US"}]{#struct_0_x1112_41438_421893739}[：表示错误信号事件的检测阈值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Errored symbol]{lang="EN-US"}]{#struct_0_x1112_41438_x1884200085}[：表示]{lang="EN-US" style="font-family:宋体"}[最近一次错误]{style="font-family:宋体"}[信号]{lang="EN-US" style="font-family:宋体"}[事件中错误信号的]{style="font-family:宋体"}[数量]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Error running total]{lang="EN-US"}]{#struct_0_x1112_41438_530306612}[：表示错误信号的总数量]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Event running total]{lang="EN-US"}]{#struct_0_x1112_41438_1724501519}[：表示错误信号事件的总数量]{lang="EN-US" style="font-family:
  宋体"}

[[OAM local/remote errored frame event]{lang="EN-US"}]{#struct_0_x1112_41438_607627222}

[[本端]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1112_41438_x2048917388}[远端产生的错误帧事件信息（只有产生了错误帧事件才会显示）：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Event time stamp]{lang="EN-US"}]{#struct_0_x1112_41438_x1470860629}[：表示错误帧事件的发生时间]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Errored frame window]{lang="EN-US"}]{#struct_0_x1112_41438_1356863813}[：表示错误帧事件的检测窗口]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Errored frame threshold]{lang="EN-US"}]{#struct_0_x1112_41438_1724567055}[：表示错误帧事件的检测阈值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Errored frame]{lang="EN-US"}]{#struct_0_x1112_41438_616414876}[：表示最近一次错误帧事件中错误帧的数量]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Error running total]{lang="EN-US"}]{#struct_0_x1112_41438_1286312208}[：表示错误帧的总数量]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Event running total]{lang="EN-US"}]{#struct_0_x1112_41438_1886359135}[：表示错误帧事件的总数量]{lang="EN-US" style="font-family:
  宋体"}

[[OAM local/remote errored frame period event]{lang="EN-US"}]{#struct_0_x1112_41438_x573028517}

[[本端]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1112_41438_1724632591}[远端产生的错误帧周期事件信息（只有产生了错误帧周期事件才会显示）：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Event time stamp]{lang="EN-US"}]{#struct_0_x1112_41438_x969794340}[：表示错误帧周期事件的发生时间]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Errored frame period window]{lang="EN-US"}]{#struct_0_x1112_41438_1467282383}[：表示错误帧周期事件的检测窗口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Errored frame period threshold]{lang="EN-US"}]{#struct_0_x1112_41438_x1672528580}[：表示错误帧周期事件的检测阈值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Errored frame period]{lang="EN-US"}]{#struct_0_x1112_41438_x357544289}[：表示]{lang="EN-US" style="font-family:
  宋体"}[最近一次错误帧周期事件中错误帧的]{style="font-family:宋体"}[数量]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Error running total]{lang="EN-US"}]{#struct_0_x1112_41438_1724698127}[：表示错误帧周期的总数量]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Event running total]{lang="EN-US"}]{#struct_0_x1112_41438_1775687795}[：表示错误帧周期事件的总数量]{lang="EN-US" style="font-family:
  宋体"}

[[OAM local/remote errored frame seconds summary event]{lang="EN-US"}]{#struct_0_x1112_41438_178093012}

[[本端]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1112_41438_x595167668}[远端产生的错误帧秒事件信息（只有产生了错误帧秒事件才会显示）：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Event time stamp]{lang="EN-US"}]{#struct_0_x1112_41438_x564553158}[：表示错误帧秒事件的发生时间]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Errored frame second]{lang="EN-US"}]{#struct_0_x1112_41438_1724239375}[s]{lang="EN-US"}[ window]{lang="EN-US"}[：表示错误帧秒事件的检测窗口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Errored frame second]{lang="EN-US"}]{#struct_0_x1112_41438_x194228841}[s]{lang="EN-US"}[ threshold]{lang="EN-US"}[：表示错误帧秒事件的检测阈值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Errored frame second]{lang="EN-US"}]{#struct_0_x1112_41438_1757315239}[s]{lang="EN-US"}[：表示]{lang="EN-US" style="font-family:宋体"}[最近一次错误帧秒事件中错误帧的]{style="font-family:宋体"}[数量]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Error running total]{lang="EN-US"}]{#struct_0_x1112_41438_x4530647}[：表示错误帧秒的总数量]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Event running total]{lang="EN-US"}]{#struct_0_x1112_41438_1724304911}[：表示错误帧秒事件的总数量]{lang="EN-US" style="font-family:
  宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1848533397}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset]{lang="EN-US"}**[ **oam**]{lang="EN-US"}]{#struct_0_x1112_41438_16436897}

::: {#-1928468887 .myid}
[]{#_Toc404795468}[]{#struct_0_x1112_41438_654527882}[]{#_Toc129683613}

**以太网OAM \-- 以太网OAM配置命令 \-- oam enable**

------------------------------------------------------------------------

[**[oam]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x1112_41438_x1451242776}[命令用来使能以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **oam** **enable**]{lang="EN-US"}]{#struct_0_x1112_41438_x1696902012}[命令用来关闭以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x615980607}

[**[oam]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x1112_41438_x1521888511}

[**[undo]{lang="EN-US"}**[ **oam** **enable**]{lang="EN-US"}]{#struct_0_x1112_41438_1126576807}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1724370447}

[[以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x1112_41438_x182963194}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1672466621}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1112_41438_x1424887770}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1674491388}

[[network-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x771440657}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x332987773}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1561033438}

[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_x63790427}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1112_41438_1724435983}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] oam enable]{lang="EN-US"}
:::

::: {#-576625541 .myid}
[]{#_Toc404795469}[]{#struct_0_x1112_41438_271766930}

**以太网OAM \-- 以太网OAM配置命令 \-- oam errored-frame threshold**

------------------------------------------------------------------------

[**[oam]{lang="EN-US"}**[ **errored-frame** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_893069602}[命令用来在接口上配置错误帧事件的检测阈值。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **oam** **errored-frame** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_x382646994}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x390451607}

[**[oam]{lang="EN-US"}**[ **errored-frame** **threshold** *threshold-value*]{lang="EN-US"}]{#struct_0_x1112_41438_x913329782}

[**[undo]{lang="EN-US"}**[ **oam** **errored-frame** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_2066416257}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1015413906}

[[接口采用全局值。]{style="font-family:宋体"}]{#struct_0_x1112_41438_x1200811626}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1725025807}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1112_41438_x1276389874}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1594102126}

[[network-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x1759990321}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x919626793}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1675934748}

[*[threshold-value]{lang="EN-US"}*]{#struct_0_x1112_41438_1938622031}[：表示错误帧事件的检测阈值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x964493812}

[[接口值只对当前接口有效，但配置优先级高于全局值。]{style="font-family:宋体"}]{#struct_0_x1112_41438_1810595604}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x272932269}

[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_1725091343}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置错误帧事件的检测阈值为]{style="font-family:宋体"}[100]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1112_41438_637118590}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] oam errored-frame threshold 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_346256626}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display oam configuration]{lang="EN-US"}**]{#struct_0_x1112_41438_x1833171121}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display oam link-event]{lang="EN-US"}**]{#struct_0_x1112_41438_791277383}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oam]{lang="EN-US"}**[ **global** **errored-frame** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_182553864}
:::

::: {#2011015490 .myid}
[]{#_Toc404795470}[]{#struct_0_x1112_41438_x1803495407}[]{#_Toc129683614}

**以太网OAM \-- 以太网OAM配置命令 \-- oam errored-frame window**

------------------------------------------------------------------------

[**[oam]{lang="EN-US"}**[ **errored-frame** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_55539514}[命令用来在接口上配置错误帧事件的检测窗口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **oam** **errored-frame** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_1724501516}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_606906326}

[**[oam]{lang="EN-US"}**[ **errored-frame** **window** *window-value*]{lang="EN-US"}]{#struct_0_x1112_41438_755930134}

[**[undo]{lang="EN-US"}**[ **oam** **errored-frame** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_1490654866}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x464966959}

[[接口采用全局值。]{style="font-family:宋体"}]{#struct_0_x1112_41438_x1135878840}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x482880046}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1112_41438_1967080810}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1112_41438_2027246539}

[[network-admin]{lang="EN-US"}]{#struct_0_x1112_41438_780221926}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1112_41438_1724567052}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1112_41438_616480412}

[*[window-value]{lang="EN-US"}*]{#struct_0_x1112_41438_x700511811}[：表示错误帧事件的检测窗口，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[，步长为]{style="font-family:宋体"}[10]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:
黑体"}]{#struct_0_x1112_41438_9659868}

[[接口值只对当前接口有效，但配置优先级高于全局值。]{style="font-family:宋体"}]{#struct_0_x1112_41438_x1388332260}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1112_41438_950134053}

[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_940458513}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置错误帧事件的检测窗口为]{style="font-family:宋体"}[2000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1112_41438_x1512601483}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] oam errored-frame window 20]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_44060505}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **configuration**]{lang="EN-US"}]{#struct_0_x1112_41438_1724632588}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **link-event**]{lang="EN-US"}]{#struct_0_x1112_41438_x969204517}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oam]{lang="EN-US"}**[ **global** **errored-frame** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_301134605}
:::

::: {#-1793419803 .myid}
[]{#_Toc404795471}[]{#struct_0_x1112_41438_x1601444491}

**以太网OAM \-- 以太网OAM配置命令 \-- oam errored-frame-period threshold**

------------------------------------------------------------------------

[**[oam]{lang="EN-US"}**[ **errored-frame-period** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_x1032424065}[命令用来在接口上配置错误帧周期事件的检测阈值。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **oam** **errored-frame-period** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_x697308212}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x561544950}

[**[oam]{lang="EN-US"}**[ **errored-frame-period** **threshold** *threshold-value*]{lang="EN-US"}]{#struct_0_x1112_41438_1657533331}

[**[undo]{lang="EN-US"}**[ **oam** **errored-frame-period** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_x962345315}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1724698124}

[[接口采用全局值。]{style="font-family:宋体"}]{#struct_0_x1112_41438_1775884403}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x594082198}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1112_41438_209796099}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x220312870}

[[network-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x1339102668}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x771878549}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1112_41438_875126310}

[*[threshold-value]{lang="EN-US"}*]{#struct_0_x1112_41438_x1611603702}[：表示错误帧周期事件的检测阈值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1724239372}

[[接口值只对当前接口有效，但配置优先级高于全局值。]{style="font-family:宋体"}]{#struct_0_x1112_41438_x194294377}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x692848664}

[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_x1872330290}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置错误帧周期事件的检测阈值为]{style="font-family:宋体"}[100]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1112_41438_x1150786953}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] oam errored-frame-period threshold 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1484651747}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **configuration**]{lang="EN-US"}]{#struct_0_x1112_41438_x874648633}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **link-event**]{lang="EN-US"}]{#struct_0_x1112_41438_961895910}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oam]{lang="EN-US"}**[ **global** **errored-frame-period** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_1724304908}
:::

::: {#1804190451 .myid}
[]{#_Toc404795472}[]{#struct_0_x1112_41438_1848992150}

**以太网OAM \-- 以太网OAM配置命令 \-- oam errored-frame-period window**

------------------------------------------------------------------------

[**[oam]{lang="EN-US"}**[ **errored-frame-period** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_1986287998}[命令用来在接口上配置错误帧周期事件的检测窗口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **oam** **errored-frame-period** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_x774384260}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1769657507}

[**[oam]{lang="EN-US"}**[ **errored-frame-period** **window** *window-value*]{lang="EN-US"}]{#struct_0_x1112_41438_x1039367226}

[**[undo]{lang="EN-US"}**[ **oam** **errored-frame-period** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_356447050}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1758874573}

[[接口采用全局值。]{style="font-family:宋体"}]{#struct_0_x1112_41438_188502435}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1724370444}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1112_41438_x183028730}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1112_41438_542547759}

[[network-admin]{lang="EN-US"}]{#struct_0_x1112_41438_201764540}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1112_41438_1166104247}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1909270045}

[*[window-value]{lang="EN-US"}*]{#struct_0_x1112_41438_1925129264}[：表示错误帧周期事件的检测窗口，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[10000]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x45986506}

[[接口值只对当前接口有效，但配置优先级高于全局值。]{style="font-family:宋体"}]{#struct_0_x1112_41438_1335471108}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1724435980}

[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_271701394}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置错误帧周期事件的检测窗口为]{style="font-family:宋体"}[20000000]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1112_41438_1296538318}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] oam errored-frame-period window 2000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_2044900147}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **configuration**]{lang="EN-US"}]{#struct_0_x1112_41438_1764177416}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **link-event**]{lang="EN-US"}]{#struct_0_x1112_41438_1174766568}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oam]{lang="EN-US"}**[ **global** **errored-frame-period** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_x1765740466}
:::

::: {#-281529413 .myid}
[]{#_Toc404795473}[]{#struct_0_x1112_41438_x413475458}

**以太网OAM \-- 以太网OAM配置命令 \-- oam errored-frame-seconds threshold**

------------------------------------------------------------------------

[**[oam]{lang="EN-US"}**[ **errored-frame-seconds** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_1725025804}[命令用来在接口上配置错误帧秒事件的检测阈值。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **oam** **errored-frame-seconds** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_x1276324338}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1936224959}

[**[oam]{lang="EN-US"}**[ **errored-frame-seconds** **threshold** *threshold-value*]{lang="EN-US"}]{#struct_0_x1112_41438_542631404}

[**[undo]{lang="EN-US"}**[ **oam** **errored-frame-seconds** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_1658474647}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1112_41438_2000310812}

[[接口采用全局值。]{style="font-family:宋体"}]{#struct_0_x1112_41438_x2076698939}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1112_41438_676423831}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1112_41438_95588651}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1725091340}

[[network-admin]{lang="EN-US"}]{#struct_0_x1112_41438_637315198}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x1687772530}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1429575186}

[*[threshold-value]{lang="EN-US"}*]{#struct_0_x1112_41438_x860760716}[：表示错误帧秒事件的检测阈值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[900]{lang="EN-US"}[，单位为次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1112_41438_283648360}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在数量上，错误帧秒事件的检测阈值不应大于其检测窗口值（换算成秒），否则将不会产生错误帧秒事件。]{style="font-family:宋体"}]{#struct_0_x1112_41438_1376353721}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口值只对当前接口有效，但配置优先级高于全局值。]{style="font-family:宋体"}]{#struct_0_x1112_41438_x2010797625}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x2128368017}

[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_1724501517}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置错误帧秒事件的检测阈值为]{style="font-family:宋体"}[100]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1112_41438_606971862}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] oam errored-frame-seconds threshold 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_53448810}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **configuration**]{lang="EN-US"}]{#struct_0_x1112_41438_1740679208}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **link-event**]{lang="EN-US"}]{#struct_0_x1112_41438_936926470}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oam]{lang="EN-US"}**[ **errored-frame-seconds** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_46285826}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oam]{lang="EN-US"}**[ **global** **errored-frame-seconds** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_173477049}
:::

::: {#-107589351 .myid}
[]{#_Toc404795474}[]{#struct_0_x1112_41438_1120146624}

**以太网OAM \-- 以太网OAM配置命令 \-- oam errored-frame-seconds window**

------------------------------------------------------------------------

[**[oam]{lang="EN-US"}**[ **errored-frame-seconds** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_1724567053}[命令用来在接口上配置错误帧秒事件的检测窗口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **oam** **errored-frame-seconds** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_616545948}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1454242418}

[**[oam]{lang="EN-US"}**[ **errored-frame-seconds** **window** *window-value*]{lang="EN-US"}]{#struct_0_x1112_41438_x2147109494}

[**[undo]{lang="EN-US"}**[ **oam** **errored-frame-seconds** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_x1130113823}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1869691298}

[[接口采用全局值。]{style="font-family:宋体"}]{#struct_0_x1112_41438_127846444}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1571289365}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1112_41438_x667578246}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1724632589}

[[network-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x969270053}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1112_41438_1078272157}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1112_41438_504110722}

[*[window-value]{lang="EN-US"}*]{#struct_0_x1112_41438_x706417750}[：表示错误帧秒事件的检测窗口，取值范围为]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[9000]{lang="EN-US"}[，步长为]{style="font-family:宋体"}[10]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1599058121}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在数量上，错误帧秒事件的检测阈值不应大于其检测窗口值（换算成秒），否则将不会产生错误帧秒事件。]{style="font-family:宋体"}]{#struct_0_x1112_41438_1401704254}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口值只对当前接口有效，但配置优先级高于全局值。]{style="font-family:宋体"}]{#struct_0_x1112_41438_x1634208262}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1995366785}

[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_1724698125}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置错误帧秒事件的检测窗口为]{style="font-family:宋体"}[10000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1112_41438_1775818867}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] oam errored-frame-seconds window 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1298755796}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **configuration**]{lang="EN-US"}]{#struct_0_x1112_41438_766694243}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **link-event**]{lang="EN-US"}]{#struct_0_x1112_41438_915678305}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oam]{lang="EN-US"}**[ **errored-frame-seconds** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_1170269420}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oam]{lang="EN-US"}**[ **global** **errored-frame-seconds** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_142613460}
:::

::: {#1956788938 .myid}
[]{#_Toc404795475}[]{#struct_0_x1112_41438_x1493802667}

**以太网OAM \-- 以太网OAM配置命令 \-- oam errored-symbol-period threshold**

------------------------------------------------------------------------

[**[oam]{lang="EN-US"}**[ **errored-symbol-period** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_1724239373}[命令用来在接口上配置错误信号事件的检测阈值。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **oam** **errored-symbol-period** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_x194359913}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1347750994}

[**[oam]{lang="EN-US"}**[ **errored-symbol-period** **threshold** *threshold-value*]{lang="EN-US"}]{#struct_0_x1112_41438_x682015890}

[**[undo]{lang="EN-US"}**[ **oam** **errored-symbol-period** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_1076464389}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1453983479}

[[接口采用全局值。]{style="font-family:宋体"}]{#struct_0_x1112_41438_2103952924}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x454546200}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1112_41438_876820168}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1724304909}

[[network-admin]{lang="EN-US"}]{#struct_0_x1112_41438_1849057686}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1112_41438_427031751}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1112_41438_2101307115}

[*[threshold-value]{lang="EN-US"}*]{#struct_0_x1112_41438_1582134422}[：表示错误信号事件的检测阈值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x954906176}

[[接口值只对当前接口有效，但配置优先级高于全局值。]{style="font-family:宋体"}]{#struct_0_x1112_41438_x134531257}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1983737310}

[]{#_Toc129683622}[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_228316387}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置错误信号事件的检测阈值为]{style="font-family:宋体"}[100]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1112_41438_1724370445}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] oam errored-symbol-period threshold 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x183094266}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **configuration**]{lang="EN-US"}]{#struct_0_x1112_41438_475797104}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **link-event**]{lang="EN-US"}]{#struct_0_x1112_41438_x1603954139}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oam]{lang="EN-US"}**[ **global** **errored-symbol-period** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_1754832655}
:::

::: {#1836161897 .myid}
[]{#_Toc404795476}[]{#struct_0_x1112_41438_x699516201}

**以太网OAM \-- 以太网OAM配置命令 \-- oam errored-symbol-period window**

------------------------------------------------------------------------

[**[oam]{lang="EN-US"}**[ **errored-symbol-period** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_x1976824005}[命令用来在接口上配置错误信号事件的检测窗口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **oam** **errored-symbol-period** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_1682654134}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1724435981}

[**[oam]{lang="EN-US"}**[ **errored-symbol-period** **window** *window-value*]{lang="EN-US"}]{#struct_0_x1112_41438_271635858}

[**[undo]{lang="EN-US"}**[ **oam** **errored-symbol-period** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_74489056}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x863513205}

[[接口采用全局值。]{style="font-family:宋体"}]{#struct_0_x1112_41438_x624656650}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1494280088}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1112_41438_775641807}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1112_41438_710127481}

[[network-admin]{lang="EN-US"}]{#struct_0_x1112_41438_1725025805}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x1276258802}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1538333235}

[*[window-value]{lang="EN-US"}*]{#struct_0_x1112_41438_x568423979}[：表示错误信号事件的检测窗口，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[1000000]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1312653541}

[[接口值只对当前接口有效，但配置优先级高于全局值。]{style="font-family:宋体"}]{#struct_0_x1112_41438_x235454597}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1112_41438_2037387310}

[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_x271472091}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置错误信号事件的检测值为]{style="font-family:宋体"}[200000000]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1112_41438_1725091341}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] oam errored-symbol-period window 200]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_637249662}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **configuration**]{lang="EN-US"}]{#struct_0_x1112_41438_x1384721758}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **link-event**]{lang="EN-US"}]{#struct_0_x1112_41438_1487085831}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oam]{lang="EN-US"}**[ **global** **errored-symbol-period** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_1280884346}
:::

::: {#-463138958 .myid}
[]{#_Toc404795477}[]{#struct_0_x1112_41438_1836075226}

**以太网OAM \-- 以太网OAM配置命令 \-- oam global errored-frame threshold**

------------------------------------------------------------------------

[**[oam]{lang="EN-US"}**[ **global** **errored-frame** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_1392889366}[命令用来全局配置错误帧事件的检测阈值。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **oam** **global** **errored-frame** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_x1448001992}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x312498752}

[**[oam]{lang="EN-US"}**[ **global** **errored-frame** **threshold** *threshold-value*]{lang="EN-US"}]{#struct_0_x1112_41438_x1004381835}

[**[undo]{lang="EN-US"}**[ **oam** **global** **errored-frame** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_1889048428}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x733293924}

[[错误帧事件检测阈值的全局值为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x1112_41438_x237939063}[次。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x449375441}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1112_41438_430813984}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1112_41438_813311989}

[[network-admin]{lang="EN-US"}]{#struct_0_x1112_41438_1705860871}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x1412422936}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1004316299}

[*[threshold-value]{lang="EN-US"}*]{#struct_0_x1112_41438_1918559939}[：表示错误帧事件的检测阈值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x359123778}

[[全局值对所有接口都有效，但配置优先级低于接口值。]{style="font-family:宋体"}]{#struct_0_x1112_41438_x294742992}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x951436005}

[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_2076653287}[全局配置错误帧事件的检测阈值为]{style="font-family:宋体"}[100]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1112_41438_x479093413}

[\[Sysname\] oam global errored-frame threshold 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x538413515}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **configuration**]{lang="EN-US"}]{#struct_0_x1112_41438_1383552814}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **link-event**]{lang="EN-US"}]{#struct_0_x1112_41438_x1004250763}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oam]{lang="EN-US"}**[ **errored-frame** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_x961644380}
:::

::: {#649023895 .myid}
[]{#_Toc129683623}[]{#_Toc404795478}[]{#struct_0_x1112_41438_39973882}

**以太网OAM \-- 以太网OAM配置命令 \-- oam global errored-frame window**

------------------------------------------------------------------------

[**[oam]{lang="EN-US"}**[ **global** **errored-frame** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_x526539819}[命令用来全局配置错误帧事件的检测窗口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **oam** **global** **errored-frame** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_1034492586}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_963444181}

[**[oam]{lang="EN-US"}**[ **global** **errored-frame** **window** *window-value*]{lang="EN-US"}]{#struct_0_x1112_41438_625786276}

[**[undo]{lang="EN-US"}**[ **oam** **global** **errored-frame** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_1277501276}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1754677308}

[[错误帧事件检测窗口的全局值为]{style="font-family:宋体"}[1000]{lang="EN-US"}]{#struct_0_x1112_41438_x1004185227}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x711556964}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1112_41438_x1813857351}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1112_41438_519175999}

[[network-admin]{lang="EN-US"}]{#struct_0_x1112_41438_1214852822}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x1551623447}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1819643969}

[*[window-value]{lang="EN-US"}*]{#struct_0_x1112_41438_x2113873294}[：表示错误帧事件的检测窗口，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[，步长为]{style="font-family:宋体"}[10]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1112_41438_101909278}

[[全局值对所有接口都有效，但配置优先级低于接口值。]{style="font-family:宋体"}]{#struct_0_x1112_41438_x1004643979}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1112_41438_394241299}

[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_x909159783}[全局配置错误帧事件的检测窗口配置为]{style="font-family:宋体"}[2000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1112_41438_x2009658806}

[\[Sysname\] oam global errored-frame window 20]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x235284771}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **configuration**]{lang="EN-US"}]{#struct_0_x1112_41438_x1881600130}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **link-event**]{lang="EN-US"}]{#struct_0_x1112_41438_1281891513}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oam]{lang="EN-US"}**[ **errored-frame** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_x2038764796}
:::

::: {#-524286167 .myid}
[]{#_Toc404795479}[]{#struct_0_x1112_41438_x1004578443}

**以太网OAM \-- 以太网OAM配置命令 \-- oam global errored-frame-period threshold**

------------------------------------------------------------------------

[**[oam]{lang="EN-US"}**[ **global** **errored-frame-period** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_x1597031655}[命令用来全局配置错误帧周期事件的检测阈值。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **oam** **global** **errored-frame-period** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_x750461}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_751607601}

[**[oam]{lang="EN-US"}**[ **global** **errored-frame-period** **threshold** *threshold-value*]{lang="EN-US"}]{#struct_0_x1112_41438_x2057906987}

[**[undo]{lang="EN-US"}**[ **oam** **global** **errored-frame-period** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_1429326931}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x904312112}

[[错误帧周期事件检测阈值的全局值为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x1112_41438_1453787084}[次。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x985992085}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1112_41438_x1004512907}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1820952142}

[[network-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x1127998477}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x1035294695}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1419226936}

[*[threshold-value]{lang="EN-US"}*]{#struct_0_x1112_41438_x1287459174}[：表示错误帧周期事件的检测阈值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1923213776}

[[全局值对所有接口都有效，但配置优先级低于接口值。]{style="font-family:宋体"}]{#struct_0_x1112_41438_x1847488012}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1837024956}

[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_x1004447371}[全局配置错误帧周期事件的检测阈值为]{style="font-family:宋体"}[100]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1112_41438_1280920037}

[\[Sysname\] oam global errored-frame-period threshold 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1870427722}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **configuration**]{lang="EN-US"}]{#struct_0_x1112_41438_x1941013620}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **link-event**]{lang="EN-US"}]{#struct_0_x1112_41438_283506322}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oam]{lang="EN-US"}**[ **errored-frame-period** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_1097628983}
:::

::: {#1647370698 .myid}
[]{#_Toc404795480}[]{#struct_0_x1112_41438_x564677733}

**以太网OAM \-- 以太网OAM配置命令 \-- oam global errored-frame-period window**

------------------------------------------------------------------------

[**[oam]{lang="EN-US"}**[ **global** **errored-frame-period** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_x997371455}[命令用来全局配置错误帧周期事件的检测窗口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **oam** **global** **errored-frame-period** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_x1003857547}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_2012170927}

[**[oam]{lang="EN-US"}**[ **global** **errored-frame-period** **window** *window-value*]{lang="EN-US"}]{#struct_0_x1112_41438_1820260417}

[**[undo]{lang="EN-US"}**[ **oam** **global** **errored-frame-period** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_x1108069343}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x48032390}

[[错误帧周期事件检测窗口的全局值为]{style="font-family:宋体"}[10000000]{lang="EN-US"}]{#struct_0_x1112_41438_x203763730}[次。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x30966547}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1112_41438_1283471532}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x228463734}

[[network-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x1003792011}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x110657184}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1306019714}

[*[window-value]{lang="EN-US"}*]{#struct_0_x1112_41438_x2120401572}[：表示错误帧周期事件的检测窗口，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[10000]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1291600625}

[[全局值对所有接口都有效，但配置优先级低于接口值。]{style="font-family:宋体"}]{#struct_0_x1112_41438_1528194489}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1260937548}

[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_1962902246}[全局配置错误帧周期事件的检测窗口为]{style="font-family:宋体"}[20000000]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1112_41438_x1004381834}

[\[Sysname\] oam global errored-frame-period window 2000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_322964487}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **configuration**]{lang="EN-US"}]{#struct_0_x1112_41438_406870329}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **link-event**]{lang="EN-US"}]{#struct_0_x1112_41438_x779772682}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oam]{lang="EN-US"}**[ **errored-frame-period** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_x2072646689}
:::

::: {#1044132000 .myid}
[]{#_Toc129683624}[]{#_Toc404795481}[]{#struct_0_x1112_41438_1570374197}

**以太网OAM \-- 以太网OAM配置命令 \-- oam global errored-frame-seconds threshold**

------------------------------------------------------------------------

[**[oam]{lang="EN-US"}**[ **global** **errored-frame-seconds** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_x207747188}[命令用来全局配置错误帧秒事件的检测阈值。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **oam** **global** **errored-frame-seconds** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_x1850912930}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1968672220}

[**[oam]{lang="EN-US"}**[ **global** **errored-frame-seconds** **threshold** *threshold-value*]{lang="EN-US"}]{#struct_0_x1112_41438_x1004316298}

[**[undo]{lang="EN-US"}**[ **oam** **global** **errored-frame-seconds** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_x810323416}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1112_41438_888632428}

[[错误帧秒事件检测阈值的全局值为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x1112_41438_1719362512}[次。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1979573232}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1112_41438_x1224814107}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x6681536}

[[network-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x1956405163}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1112_41438_1387347169}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1004250762}

[*[threshold-value]{lang="EN-US"}*]{#struct_0_x1112_41438_604439561}[：表示错误帧秒事件的检测阈值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[900]{lang="EN-US"}[，单位为次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1112_41438_192792540}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在数量上，错误帧秒事件的检测阈值不应大于其检测窗口值（换算成秒），否则将不会产生错误帧秒事件。]{style="font-family:宋体"}]{#struct_0_x1112_41438_691328232}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[全局值对所有接口都有效，但配置优先级低于接口值。]{style="font-family:宋体"}]{#struct_0_x1112_41438_x1767375322}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x126281182}

[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_520910153}[全局配置错误帧秒事件的检测阈值配置为]{style="font-family:宋体"}[100]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1112_41438_1119651681}

[\[Sysname\] oam global errored-frame-seconds threshold 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x392130480}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **configuration**]{lang="EN-US"}]{#struct_0_x1112_41438_x1004185226}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **link-event**]{lang="EN-US"}]{#struct_0_x1112_41438_2017326391}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oam]{lang="EN-US"}**[ **errored-frame-seconds** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_783278398}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oam]{lang="EN-US"}**[ **global** **errored-frame-seconds** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_503082851}
:::

::: {#963476194 .myid}
[]{#_Toc404795482}[]{#struct_0_x1112_41438_x1896044666}

**以太网OAM \-- 以太网OAM配置命令 \-- oam global errored-frame-seconds window**

------------------------------------------------------------------------

[**[oam]{lang="EN-US"}**[ **global** **errored-frame-seconds** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_x871995987}[命令用来全局配置错误帧秒事件的检测窗口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **oam** **global** **errored-frame-seconds** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_1238261949}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1424842554}

[**[oam]{lang="EN-US"}**[ **global** **errored-frame-seconds** **window** *window-value*]{lang="EN-US"}]{#struct_0_x1112_41438_661506474}

[**[undo]{lang="EN-US"}**[ **oam** **global** **errored-frame-seconds** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_x1004643978}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1171842642}

[[错误帧秒事件检测窗口的全局值为]{style="font-family:宋体"}[60000]{lang="EN-US"}]{#struct_0_x1112_41438_1795117558}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1112_41438_848416043}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1112_41438_x1270247141}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1891142226}

[[network-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x1681693468}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1112_41438_765091305}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1004578442}

[*[window-value]{lang="EN-US"}*]{#struct_0_x1112_41438_x30947714}[：表示错误帧秒事件的检测窗口，取值范围为]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[9000]{lang="EN-US"}[，步长为]{style="font-family:宋体"}[10]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1455468745}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在数量上，错误帧秒事件的检测阈值不应大于其检测窗口值（换算成秒），否则将不会产生错误帧秒事件。]{style="font-family:宋体"}]{#struct_0_x1112_41438_x492133685}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[全局值对所有接口都有效，但配置优先级低于接口值。]{style="font-family:宋体"}]{#struct_0_x1112_41438_x985544759}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1112_41438_445978428}

[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_130104831}[全局配置错误帧秒事件的检测窗口为]{style="font-family:宋体"}[10000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1112_41438_x1708537663}

[\[Sysname\] oam global errored-frame-seconds window 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x683378904}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **configuration**]{lang="EN-US"}]{#struct_0_x1112_41438_x1004512906}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **link-event**]{lang="EN-US"}]{#struct_0_x1112_41438_x907931213}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oam]{lang="EN-US"}**[ **errored-frame-seconds** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_x614701469}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oam]{lang="EN-US"}**[ **global** **errored-frame-seconds** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_x1097900506}
:::

::: {#-884061978 .myid}
[]{#_Toc404795483}[]{#struct_0_x1112_41438_1832236413}

**以太网OAM \-- 以太网OAM配置命令 \-- oam global errored-symbol-period threshold**

------------------------------------------------------------------------

[**[oam]{lang="EN-US"}**[ **global** **errored-symbol-period** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_x686085082}[命令用来全局配置错误信号事件的检测阈值。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **oam** **global** **errored-symbol-period** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_x1175024892}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_957084914}

[**[oam]{lang="EN-US"}**[ **global** **errored-symbol-period** **threshold** *threshold-value*]{lang="EN-US"}]{#struct_0_x1112_41438_x1324664281}

[**[undo]{lang="EN-US"}**[ **oam** **global** **errored-symbol-period** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_x1004447370}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x285163904}

[[错误信号事件检测阈值的全局值为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x1112_41438_879087564}[次。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1106170130}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1112_41438_x1918884918}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1112_41438_176130913}

[[network-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x1215552594}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x339940974}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1508172531}

[*[threshold-value]{lang="EN-US"}*]{#struct_0_x1112_41438_x1003857546}[：表示错误信号事件的检测阈值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x716712428}

[[全局值对所有接口都有效，但配置优先级低于接口值。]{style="font-family:宋体"}]{#struct_0_x1112_41438_519891335}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1731270450}

[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_x1407807984}[全局配置错误信号事件的检测阈值为]{style="font-family:宋体"}[100]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1112_41438_1143705239}

[\[Sysname\] oam global errored-symbol-period threshold 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x247601753}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **configuration**]{lang="EN-US"}]{#struct_0_x1112_41438_x422214098}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **link-event**]{lang="EN-US"}]{#struct_0_x1112_41438_x1003792010}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oam]{lang="EN-US"}**[ **errored-symbol-period** **threshold**]{lang="EN-US"}]{#struct_0_x1112_41438_1455426757}
:::

::: {#821643370 .myid}
[]{#_Toc404795484}[]{#struct_0_x1112_41438_838363366}

**以太网OAM \-- 以太网OAM配置命令 \-- oam global errored-symbol-period window**

------------------------------------------------------------------------

[**[oam]{lang="EN-US"}**[ **global** **errored-symbol-period** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_351869988}[命令用来全局配置错误信号事件的检测窗口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **oam** **global** **errored-symbol-period** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_798764313}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1191253972}

[**[oam]{lang="EN-US"}**[ **global** **errored-symbol-period** **window** *window-value*]{lang="EN-US"}]{#struct_0_x1112_41438_x2030645621}

[**[undo]{lang="EN-US"}**[ **oam** **global** **errored-symbol-period** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_630606078}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x902756755}

[[错误信号事件检测窗口的全局值为]{style="font-family:宋体"}[100000000]{lang="EN-US"}]{#struct_0_x1112_41438_x1004381837}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1243119454}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1112_41438_1056222739}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x979813350}

[[network-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x1137739879}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1112_41438_2143872613}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1059435240}

[*[window-value]{lang="EN-US"}*]{#struct_0_x1112_41438_1229402710}[：表示错误信号事件的检测窗口，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[1000000]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x343270255}

[[全局值对所有接口都有效，但配置优先级低于接口值。]{style="font-family:宋体"}]{#struct_0_x1112_41438_x1004316301}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1562919402}

[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_x18144665}[全局配置错误信号事件的检测窗口为]{style="font-family:宋体"}[200000000]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1112_41438_x943313373}

[\[Sysname\] oam global errored-symbol-period window 200]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x925459367}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **configuration**]{lang="EN-US"}]{#struct_0_x1112_41438_1901533905}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **link-event**]{lang="EN-US"}]{#struct_0_x1112_41438_x1771131220}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oam]{lang="EN-US"}**[ **errored-symbol-period** **window**]{lang="EN-US"}]{#struct_0_x1112_41438_x367167967}
:::

::: {#-1066992626 .myid}
[]{#_Toc404795485}[]{#struct_0_x1112_41438_959926520}

**以太网OAM \-- 以太网OAM配置命令 \-- oam global timer hello**

------------------------------------------------------------------------

[**[oam]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1112_41438_x1004250765}**[global]{lang="NO-BOK"}**[ **timer**]{lang="NO-BOK"}[ ]{lang="NO-BOK"}**[hello]{lang="EN-US"}**[命令用来全局配置以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[握手报文的发送间隔。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **oam** **global** **timer** **hello**]{lang="EN-US"}]{#struct_0_x1112_41438_x1768213434}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1257280708}

[**[oam]{lang="NO-BOK"}**]{#struct_0_x1112_41438_x1863965357}[ **global** **timer** **hello** *interval*]{lang="NO-BOK"}

[**[undo]{lang="NO-BOK"}**]{#struct_0_x1112_41438_980237899}[ **oam** **global** **timer** **hello**]{lang="NO-BOK"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1375659766}

[[以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x1112_41438_899226444}[握手报文发送间隔的全局值为]{style="font-family:宋体"}[1000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1130972384}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1112_41438_x920388302}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1004185229}

[[network-admin]{lang="EN-US"}]{#struct_0_x1112_41438_95012090}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x1388761462}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1245101368}

[*[interval]{lang="NO-BOK"}*]{#struct_0_x1112_41438_838776916}[：表示以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[握手报文的发送间隔，单位为毫秒，步长为]{style="font-family:宋体"}[100]{lang="EN-US"}[，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1016176459}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[由于本端]{style="font-family:宋体"}]{#struct_0_x1112_41438_487107917}[OAM]{lang="EN-US"}[实体在连接超时后将老化与远端]{style="font-family:宋体"}[OAM]{lang="EN-US"}[实体的连接关系，导致]{style="font-family:宋体"}[OAM]{lang="EN-US"}[连接中断，因此连接超时时间必须大于握手报文发送间隔（建议为五倍或以上），否则将导致以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[连接不稳定。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[全局值对所有接口都有效，但配置优先级低于接口值。]{style="font-family:宋体"}]{#struct_0_x1112_41438_54527628}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1653484449}

[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_x1004643981}[全局配置以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[握手报文的发送间隔为]{style="font-family:宋体"}[600]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NO-BOK"}]{#struct_0_x1112_41438_749488619}

[\[Sysname\] oam global timer hello 600]{lang="NO-BOK"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1546114724}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **configuration**]{lang="EN-US"}]{#struct_0_x1112_41438_x780028402}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oam]{lang="NO-BOK"}**]{#struct_0_x1112_41438_245407533}[ **timer** **hello**]{lang="NO-BOK"}
:::

::: {#1492456160 .myid}
[]{#_Toc404795486}[]{#struct_0_x1112_41438_1644089740}

**以太网OAM \-- 以太网OAM配置命令 \-- oam global timer keepalive**

------------------------------------------------------------------------

[**[oam]{lang="EN-US"}**[ **global** **timer** **keepalive**]{lang="EN-US"}]{#struct_0_x1112_41438_484793676}[命令用来全局配置以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[连接的超时时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **oam** **global** **timer** **keepalive**]{lang="EN-US"}]{#struct_0_x1112_41438_x1705414170}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1004578445}

[**[oam]{lang="EN-US"}**[ **global** **timer** **keepalive** *interval*]{lang="EN-US"}]{#struct_0_x1112_41438_x434232241}

[**[undo]{lang="EN-US"}**[ **oam** **global** **timer** **keepalive**]{lang="EN-US"}]{#struct_0_x1112_41438_1500433187}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1433424174}

[[以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x1112_41438_221829437}[连接超时时间的全局值为]{style="font-family:宋体"}[5000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1985858249}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1112_41438_x659959402}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1179770070}

[[network-admin]{lang="EN-US"}]{#struct_0_x1112_41438_1674398441}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x1004512909}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1370613448}

[*[interval]{lang="NO-BOK"}*]{#struct_0_x1112_41438_1517398364}[：表示以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[连接的超时时间，单位为毫秒，步长为]{style="font-family:宋体"}[100]{lang="EN-US"}[，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x535975391}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[由于本端]{style="font-family:宋体"}]{#struct_0_x1112_41438_x1408787465}[OAM]{lang="EN-US"}[实体在连接超时后将老化与远端]{style="font-family:宋体"}[OAM]{lang="EN-US"}[实体的连接关系，导致]{style="font-family:宋体"}[OAM]{lang="EN-US"}[连接中断，因此连接超时时间必须大于握手报文发送间隔（建议为五倍或以上），否则将导致以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[连接不稳定。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[全局值对所有接口都有效，但配置优先级低于接口值。]{style="font-family:宋体"}]{#struct_0_x1112_41438_1565987912}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1757446880}

[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_x824481550}[全局配置以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[连接的超时时间为]{style="font-family:宋体"}[6000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1112_41438_x1004447373}

[\[Sysname\] ]{lang="EN-US"}[oam global]{lang="NO-BOK"}[ ]{lang="NO-BOK"}[timer keepalive 6000]{lang="NO-BOK"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1851247845}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **configuration**]{lang="EN-US"}]{#struct_0_x1112_41438_x581737250}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oam]{lang="EN-US"}**[ **timer** **keepalive**]{lang="EN-US"}]{#struct_0_x1112_41438_x2020433184}
:::

::: {#1000385863 .myid}
[]{#_Toc404795487}[]{#struct_0_x1112_41438_188475911}

**以太网OAM \-- 以太网OAM配置命令 \-- oam mode**

------------------------------------------------------------------------

[**[oam]{lang="EN-US"}**[ **mode**]{lang="EN-US"}]{#struct_0_x1112_41438_x842185003}[命令用来配置以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[的连接模式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **oam** **mode**]{lang="EN-US"}]{#struct_0_x1112_41438_73511674}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x2122128302}

[**[oam]{lang="FR"}**]{#struct_0_x1112_41438_x1766817847}[ **mode** { **active** \| **passive** }]{lang="FR"}

[**[undo]{lang="EN-US"}**[ **oam** **mode**]{lang="EN-US"}]{#struct_0_x1112_41438_x1003857549}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1112_41438_493141153}

[[以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x1112_41438_9604096}[连接模式为主动模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1112_41438_150863435}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1112_41438_346682896}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x428956412}

[[network-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x1632561016}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1112_41438_527921079}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x767744948}

[**[active]{lang="EN-US"}**]{#struct_0_x1112_41438_1065087958}[：表示主动模式。]{style="font-family:宋体"}

[**[passive]{lang="EN-US"}**]{#struct_0_x1112_41438_x1003792013}[：表示被动模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1273456598}

[[不允许在已使能以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x1112_41438_x1701128913}[功能的接口上更改以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[的连接模式。如需更改，请先关闭该接口上的以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x131830239}

[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_1430119192}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上先关闭以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[功能，再配置以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[的连接模式为被动模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1112_41438_154813746}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] undo oam enable]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] oam mode passive]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1729102667}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oam]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x1112_41438_x1004381836}
:::

::: {#672022086 .myid}
[]{#_Toc404795488}[]{#struct_0_x1112_41438_1485763901}

**以太网OAM \-- 以太网OAM配置命令 \-- oam remote-failure action**

------------------------------------------------------------------------

[**[oam]{lang="EN-US"}**[ **remote-failure action**]{lang="EN-US"}]{#struct_0_x1112_41438_745210486}[命令用来配置接口收到远端以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[事件时的响应动作。]{style="font-family:宋体"}

[**[undo oam]{lang="EN-US"}**[ **remote-failure action**]{lang="EN-US"}]{#struct_0_x1112_41438_613038334}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_636185490}

[**[oam]{lang="EN-US"}**[ **remote-failure** { **connection-expired** \| **critical-event** \| **dying-gasp** \| **link-fault** } **action** **error-link-down**]{lang="EN-US"}]{#struct_0_x1112_41438_1794967995}

[**[undo]{lang="EN-US"}**[ **oam** **remote-failure** { **connection-expired** \| **critical-event** \| **dying-gasp** \| **link-fault** } **action** **error-link-down**]{lang="EN-US"}]{#struct_0_x1112_41438_x1860907993}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1112_41438_2063735886}

[[接口收到远端以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x1112_41438_x1116697045}[事件时仅记录日志。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1004316300}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1112_41438_x1165963953}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1112_41438_895852612}

[[network-admin]{lang="EN-US"}]{#struct_0_x1112_41438_738689717}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1112_41438_77380806}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1112_41438_309331096}

[**[connection-expired]{lang="EN-US"}**]{#struct_0_x1112_41438_495538116}[：表示以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[连接超时。]{style="font-family:宋体"}

[**[critical-event]{lang="EN-US"}**]{#struct_0_x1112_41438_1046977358}[：表示紧急事件。]{style="font-family:宋体"}

[**[dying-gasp]{lang="EN-US"}**]{#struct_0_x1112_41438_1640233901}[：表示致命故障。]{style="font-family:宋体"}

[**[link-fault]{lang="EN-US"}**]{#struct_0_x1112_41438_x1004250764}[：表示链路故障。]{style="font-family:宋体"}

[**[error-link-down]{lang="EN-US"}**]{#struct_0_x1112_41438_x202129493}[：表示断开]{style="font-family:宋体"}[OAM]{lang="EN-US"}[连接，并设置接口的链路层状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1904151115}

[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_1043503207}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收到远端致命故障时的响应动作为断开]{style="font-family:宋体"}[OAM]{lang="EN-US"}[连接，并设置该接口的链路层状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1112_41438_1125502616}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] oam remote-failure dying-gasp action error-link-down]{lang="EN-US"}
:::

::: {#-1964257071 .myid}
[]{#_Toc404795489}[]{#struct_0_x1112_41438_x1703011212}

**以太网OAM \-- 以太网OAM配置命令 \-- oam remote-loopback**

------------------------------------------------------------------------

[**[oam]{lang="EN-US"}**[ **remote-loopback** **start**]{lang="EN-US"}]{#struct_0_x1112_41438_x785905536}[命令用来使能当前接口的以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[远端环回功能。]{style="font-family:宋体"}

[**[oam]{lang="EN-US"}**[ **remote-loopback** **stop**]{lang="EN-US"}]{#struct_0_x1112_41438_1875741782}[命令用来关闭当前接口的以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[远端环回功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1004185228}

[**[oam]{lang="EN-US"}**[ **remote-loopback** **start**]{lang="EN-US"}]{#struct_0_x1112_41438_x1471071851}

[**[oam]{lang="EN-US"}**[ **remote-loopback** **stop**]{lang="EN-US"}]{#struct_0_x1112_41438_x1596802483}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1367257019}

[[以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x1112_41438_x439401746}[远端环回功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1220832764}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1112_41438_1385962516}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1112_41438_243502358}

[[network-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x1637253843}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x1004643980}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x816595322}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有当接口上的以太网]{style="font-family:宋体"}]{#struct_0_x1112_41438_103821389}[OAM]{lang="EN-US"}[连接已建立完成，且以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[的连接模式为主动模式时，才允许在该接口上使能以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[远端环回功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户既可在用户视图或系统视图下使能指定接口的以太网]{style="font-family:宋体"}]{#struct_0_x1112_41438_1839892975}[OAM]{lang="EN-US"}[远端环回功能，也可在接口视图下使能当前接口的以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[远端环回功能，三者的配置效果相同。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x760939186}

[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_x1624379021}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[的连接模式为主动模式并使能其以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[功能，然后在该接口视图下使能其以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[远端环回功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1112_41438_1786186381}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] oam mode active]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] oam enable]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] oam remote-loopback start]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1004578444}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oam]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x1112_41438_1131851700}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oam]{lang="EN-US"}**[ **mode**]{lang="EN-US"}]{#struct_0_x1112_41438_x119496840}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oam]{lang="EN-US"}**[ **remote-loopback** **interface**]{lang="EN-US"}]{#struct_0_x1112_41438_1107672023}
:::

::: {#-1254044710 .myid}
[]{#_Toc404795490}[]{#struct_0_x1112_41438_x341558672}

**以太网OAM \-- 以太网OAM配置命令 \-- oam remote-loopback interface**

------------------------------------------------------------------------

[**[oam]{lang="EN-US"}**[ **remote-loopback** **start** **interface**]{lang="EN-US"}]{#struct_0_x1112_41438_x702564854}[命令用来使能指定接口的以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[远端环回功能。]{style="font-family:宋体"}

[**[oam]{lang="EN-US"}**[ **remote-loopback** **stop** **interface**]{lang="EN-US"}]{#struct_0_x1112_41438_x138951759}[命令用来关闭指定接口的以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[远端环回功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_116026970}

[**[oam]{lang="EN-US"}**[ **remote-loopback** **start** **interface** *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x1112_41438_1954620369}

[**[oam]{lang="EN-US"}**[ **remote-loopback** **stop** **interface** *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x1112_41438_x1004512908}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1358269907}

[[以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x1112_41438_1867573975}[远端环回功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x526929675}

[[用户视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1112_41438_x577889492}[系统视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1425074584}

[[network-admin]{lang="EN-US"}]{#struct_0_x1112_41438_604266860}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x884553213}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x73543631}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1112_41438_x1004447372}[：表示接口类型和接口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1112_41438_877635510}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有当接口上的以太网]{style="font-family:宋体"}]{#struct_0_x1112_41438_1998302401}[OAM]{lang="EN-US"}[连接已建立完成，且以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[的连接模式为主动模式时，才允许在该接口上使能以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[远端环回功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户既可在用户视图或系统视图下使能指定接口的以太网]{style="font-family:宋体"}]{#struct_0_x1112_41438_x1222545510}[OAM]{lang="EN-US"}[远端环回功能，也可在接口视图下使能当前接口的以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[远端环回功能，三者的配置效果相同。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1112_41438_90279094}

[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_x1617412473}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[的连接模式为主动模式并使能其以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[功能，然后在系统视图下使能该接口的以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[远端环回功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1112_41438_x430287008}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] oam mode active]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] oam enable]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] quit]{lang="EN-US"}

[\[Sysname\] oam remote-loopback start interface gigabitethernet 1/0/1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1003857548}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oam]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x1112_41438_2059225094}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oam]{lang="EN-US"}**[ **mode**]{lang="EN-US"}]{#struct_0_x1112_41438_1615712592}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oam]{lang="EN-US"}**[ **remote-loopback**]{lang="EN-US"}]{#struct_0_x1112_41438_x1089070188}
:::

::: {#2116219960 .myid}
[]{#_Toc404795491}[]{#struct_0_x1112_41438_690895058}

**以太网OAM \-- 以太网OAM配置命令 \-- oam remote-loopback reject-request**

------------------------------------------------------------------------

[**[oam]{lang="EN-US"}**[ **remote-loopback** **reject-request**]{lang="EN-US"}]{#struct_0_x1112_41438_x1587017980}[命令用来配置接口拒绝远端发起的以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[远端环回。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **oam** **remote-loopback** **reject-request**]{lang="EN-US"}]{#struct_0_x1112_41438_908714891}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1876168572}

[**[oam]{lang="EN-US"}**[ **remote-loopback** **reject-request**]{lang="EN-US"}]{#struct_0_x1112_41438_x61081625}

[**[undo]{lang="EN-US"}**[ **oam** **remote-loopback** **reject-request**]{lang="EN-US"}]{#struct_0_x1112_41438_x1003792012}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1112_41438_292627343}

[[接口不拒绝远端发起的以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x1112_41438_619283693}[远端环回。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1046881641}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1112_41438_x743196819}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1408740057}

[[network-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x877642042}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x1144525829}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1418153805}

[[在执行]{style="font-family:宋体"}**[oam remote-loopback reject-request]{lang="EN-US"}**]{#struct_0_x1112_41438_x1004381839}[命令时若接口已处于环回状态，则该配置将从下次环回开始时生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x436550400}

[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_1765335668}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[拒绝远端发起的以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[远端环回。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1112_41438_1185520375}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] oam remote-loopback reject-request]{lang="EN-US"}
:::

::: {#-1795407457 .myid}
[]{#_Toc404795492}[]{#struct_0_x1112_41438_1166374602}[]{#_Toc232931916}

**以太网OAM \-- 以太网OAM配置命令 \-- oam timer hello**

------------------------------------------------------------------------

[**[oam]{lang="EN-US"}**[ **timer** **hello**]{lang="EN-US"}]{#struct_0_x1112_41438_x1632033189}[命令用来在接口上配置以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[握手报文的发送间隔。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **oam** **timer** **hello**]{lang="EN-US"}]{#struct_0_x1112_41438_x1306929018}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x751754940}

[**[oam]{lang="NO-BOK"}**]{#struct_0_x1112_41438_x1571676093}[ **timer** **hello** *interval*]{lang="NO-BOK"}

[**[undo]{lang="NO-BOK"}**]{#struct_0_x1112_41438_x1004316303}[ **oam** **timer** **hello**]{lang="NO-BOK"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1112_41438_400119988}

[[接口采用全局值。]{style="font-family:宋体"}]{#struct_0_x1112_41438_1776035841}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1866493221}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1112_41438_752008926}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1359295438}

[[network-admin]{lang="EN-US"}]{#struct_0_x1112_41438_480501321}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x1071670707}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1112_41438_2077333598}

[*[interval]{lang="NO-BOK"}*]{#struct_0_x1112_41438_x1004250767}[：表示以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[握手报文的发送间隔，单位为毫秒，步长为]{style="font-family:宋体"}[100]{lang="EN-US"}[，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1363954448}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[由于本端]{style="font-family:宋体"}]{#struct_0_x1112_41438_x1896078059}[OAM]{lang="EN-US"}[实体在连接超时后将老化与远端]{style="font-family:宋体"}[OAM]{lang="EN-US"}[实体的连接关系，导致]{style="font-family:宋体"}[OAM]{lang="EN-US"}[连接中断，因此连接超时时间必须大于握手报文发送间隔（建议为五倍或以上），否则将导致以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[连接不稳定。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口值只对当前接口有效，但配置优先级高于全局值。]{style="font-family:宋体"}]{#struct_0_x1112_41438_x1295477567}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1112_41438_621053165}

[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_1038185019}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[握手报文的发送间隔为]{style="font-family:宋体"}[600]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1112_41438_1101254134}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] oam timer hello 600]{lang="NO-BOK"}

[[【相关命令】]{style="font-family:
黑体"}]{#struct_0_x1112_41438_456341}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **configuration**]{lang="EN-US"}]{#struct_0_x1112_41438_x1004185231}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oam]{lang="EN-US"}**[ **global** **timer** **hello**]{lang="EN-US"}]{#struct_0_x1112_41438_451176914}
:::

::: {#218381349 .myid}
[]{#_Toc404795493}[]{#struct_0_x1112_41438_640753863}

**以太网OAM \-- 以太网OAM配置命令 \-- oam timer keepalive**

------------------------------------------------------------------------

[**[oam]{lang="EN-US"}**[ **timer** **keepalive**]{lang="EN-US"}]{#struct_0_x1112_41438_x39671179}[命令用来在接口上配置以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[连接的超时时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **oam** **timer** **keepalive**]{lang="EN-US"}]{#struct_0_x1112_41438_220049846}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1114915645}

[**[oam]{lang="EN-US"}**[ **timer** **keepalive** *interval*]{lang="EN-US"}]{#struct_0_x1112_41438_x1614905614}

[**[undo]{lang="EN-US"}**[ **oam** **timer** **keepalive**]{lang="EN-US"}]{#struct_0_x1112_41438_512400679}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1053047213}

[[接口采用全局值。]{style="font-family:宋体"}]{#struct_0_x1112_41438_x1004643983}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1912288033}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1112_41438_1685432892}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1112_41438_210406848}

[[network-admin]{lang="EN-US"}]{#struct_0_x1112_41438_893762617}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1112_41438_x1144765133}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1172237068}

[*[interval]{lang="NO-BOK"}*]{#struct_0_x1112_41438_x747122994}[：表示以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[连接的超时时间，单位为毫秒，步长为]{style="font-family:宋体"}[100]{lang="EN-US"}[，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x2136922229}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[由于本端]{style="font-family:宋体"}]{#struct_0_x1112_41438_x1004578447}[OAM]{lang="EN-US"}[实体在连接超时后将老化与远端]{style="font-family:宋体"}[OAM]{lang="EN-US"}[实体的连接关系，导致]{style="font-family:宋体"}[OAM]{lang="EN-US"}[连接中断，因此连接超时时间必须大于握手报文发送间隔（建议为五倍或以上），否则将导致以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[连接不稳定。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口值只对当前接口有效，但配置优先级高于全局值。]{style="font-family:宋体"}]{#struct_0_x1112_41438_728567173}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1112_41438_422564194}

[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_x801860550}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[连接的超时时间为]{style="font-family:宋体"}[6000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1112_41438_1914761697}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] oam timer keepalive 6000]{lang="NO-BOK"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x770666462}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **configuration**]{lang="EN-US"}]{#struct_0_x1112_41438_1977859684}

[[·[              ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:10.0pt;font-family:Symbol"}**[oam]{lang="EN-US"}**[ **global** **timer** **keepalive**]{lang="EN-US"}]{#struct_0_x1112_41438_1842616980}
:::

::: {#763873786 .myid}
[]{#_Toc404795494}[]{#struct_0_x1112_41438_x1004512911}

**以太网OAM \-- 以太网OAM配置命令 \-- reset oam**

------------------------------------------------------------------------

[**[reset]{lang="EN-US"}**[ **oam**]{lang="EN-US"}]{#struct_0_x1112_41438_1014317552}[命令用来清除以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[的报文和一般链路事件统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1465550368}

[**[reset]{lang="EN-US"}**[ **oam** \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x1112_41438_954197025}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x431332663}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1112_41438_1748749166}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1112_41438_773872865}

[[network-admin]{lang="EN-US"}]{#struct_0_x1112_41438_441360290}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1112_41438_785844146}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1112_41438_x1004447375}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x1112_41438_x688448431}[：清除指定接口上的信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。如果未指定本参数，将清除所有接口上的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1869651988}

[[\# ]{lang="EN-US"}]{#struct_0_x1112_41438_x1088698323}[清除所有接口上以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[的报文和一般链路事件统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset oam]{lang="EN-US"}]{#struct_0_x1112_41438_691443984}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1112_41438_1978013533}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam**]{lang="EN-US"}]{#struct_0_x1112_41438_1608624547}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **oam** **link-event**]{lang="EN-US"}]{#struct_0_x1112_41438_36238863}
:::
