::: {#159028826 .myid}
[]{#_Toc404796166}[]{#struct_0_x1184_x1007_x1974402618}

**Track \-- Track调试命令 \-- debugging track**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1184_x1007_1544549791}

[**[debugging track]{lang="EN-US"}**]{#struct_0_x1184_x1007_x1015129742}

[**[undo debugging track]{lang="EN-US"}**]{#struct_0_x1184_x1007_39888203}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1184_x1007_678061931}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1184_x1007_1399466120}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1184_x1007_x320847519}

[[network-admin]{lang="EN-US"}]{#struct_0_x1184_x1007_1967951168}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1184_x1007_865781570}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1184_x1007_1401813146}

[**[debugging track]{lang="EN-US"}**]{#struct_0_x1184_x1007_x821121461}[命令用来打开]{style="font-family:宋体"}[Track]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[**[undo debugging track]{lang="EN-US"}**]{#struct_0_x1184_x1007_x1014933134}[命令用来关闭]{style="font-family:宋体"}[Track]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_x1184_x1007_229370603}[的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging track]{lang="EN-US"}]{#struct_0_x1184_x1007_1086469444}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1012931191}[[字段]{style="font-family:黑体"}]{#struct_0_x1184_x1007_1641236141}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1184_x1007_2010941561}

[[The state of track entry *entry-number* changed from *state1* to *state2*.]{lang="EN-US"}]{#struct_0_x1184_x1007_x405110086}

[[Track]{lang="EN-US"}]{#struct_0_x1184_x1007_486994135}[项]{style="font-family:宋体"}*[entry-number]{lang="EN-US"}*[的状态从]{style="font-family:宋体"}*[state1]{lang="EN-US"}*[转变为]{style="font-family:宋体"}*[state2]{lang="EN-US"}*

[[状态取值包括：]{style="font-family:宋体"}]{#struct_0_x1184_x1007_2055516694}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NotReady]{lang="EN-US"}]{#struct_0_x1184_x1007_x1014998670}[：表示无效值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Positive]{lang="EN-US"}]{#struct_0_x1184_x1007_x1946350292}[：表示状态正常]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Negative]{lang="EN-US"}]{#struct_0_x1184_x1007_x679645923}[：表示状态异常]{lang="EN-US" style="font-family:宋体"}

[[Notified application process *process-id* in slot *slot-number* that the state of track entry *entry-number* had changed to *state1*.]{lang="EN-US"}]{#struct_0_x1184_x1007_464871567}

[[通知应用进程]{style="font-family:宋体"}*[process-id]{lang="EN-US"}*]{#struct_0_x1184_x1007_x881602199}[，]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}*[entry-number]{lang="EN-US"}*[的状态变为]{style="font-family:宋体"}*[state1]{lang="EN-US"}*[，进程所在的板的板号为]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*

[[Track entry *entry-number* registered with the NQA (*owner-tag*) reaction (*item-number*).]{lang="EN-US"}]{#struct_0_x1184_x1007_x212771843}

[[Track]{lang="EN-US"}]{#struct_0_x1184_x1007_x1014802062}[项]{style="font-family:宋体"}*[entry-number]{lang="EN-US"}*[向]{style="font-family:宋体"}[NQA]{lang="EN-US"}[注册联动]{style="font-family:宋体"}

[[Track entry *entry-number* deregistered with the NQA (*owner-tag*) reaction (*item-number*).]{lang="EN-US"}]{#struct_0_x1184_x1007_599295945}

[[Track]{lang="EN-US"}]{#struct_0_x1184_x1007_8727852}[项]{style="font-family:宋体"}*[entry-number]{lang="EN-US"}*[取消与]{style="font-family:宋体"}[NQA]{lang="EN-US"}[的联动注册]{style="font-family:宋体"}

[[Received the notification that the state of NQA (*owner-tag*) reaction (*item-number*) had changed to *state*.]{lang="EN-US"}]{#struct_0_x1184_x1007_263982634}

[[接收到]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_x1184_x1007_x884531721}[联动项状态转变的通知]{style="font-family:宋体"}

[[Received the notification that the BFD session state had changed to *state*.]{lang="EN-US"}]{#struct_0_x1184_x1007_x98191004}

[[BFD info: ]{lang="EN-US"}]{#struct_0_x1184_x1007_x1014867598}

[[Session mode: *session-mode*]{lang="EN-US"}]{#struct_0_x1184_x1007_180310884}

[[Outgoing interface: *interface-name*]{lang="EN-US"}]{#struct_0_x1184_x1007_x168179545}

[[VPN instance: *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x1184_x1007_x560140160}

[[Remote IP: *remote-ip*]{lang="EN-US"}]{#struct_0_x1184_x1007_459612350}

[[Local IP: *local-ip*]{lang="EN-US"}]{#struct_0_x1184_x1007_x1014670990}

[[接收到]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_x1184_x1007_2143018315}[会话状态改变的通知，状态转到]{style="font-family:宋体"}*[state]{lang="EN-US"}*

[[BFD]{lang="EN-US"}]{#struct_0_x1184_x1007_1655954478}[会话信息为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[会话模式为]{lang="EN-US" style="font-family:宋体"}*[session-mode]{lang="EN-US"}*]{#struct_0_x1184_x1007_x469610110}[，取值为]{lang="EN-US" style="font-family:宋体"}[echo]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[control]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[出接口名为]{lang="EN-US" style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1184_x1007_x1833164411}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[出接口绑定的]{lang="EN-US" style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x1184_x1007_x1014736526}[实例为]{lang="EN-US" style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[，如果出接口没有绑定]{lang="EN-US" style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，则打印"]{lang="EN-US" style="font-family:宋体"}[-]{lang="EN-US"}["]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对端]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1184_x1007_1806619685}[地址为]{lang="EN-US" style="font-family:宋体"}*[remote-ip]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本地]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1184_x1007_696663331}[地址为]{lang="EN-US" style="font-family:宋体"}*[local-ip]{lang="EN-US"}*

[[Notified the BFD module to create a BFD session.]{lang="EN-US"}]{#struct_0_x1184_x1007_2019594995}

[[BFD info: ]{lang="EN-US"}]{#struct_0_x1184_x1007_x1014539918}

[[Session mode: *session-mode*]{lang="EN-US"}]{#struct_0_x1184_x1007_x36347337}

[[Outgoing interface: *interface-name*]{lang="EN-US"}]{#struct_0_x1184_x1007_476544794}

[[VPN instance: *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x1184_x1007_1626632077}

[[Remote IP: *remote-ip*]{lang="EN-US"}]{#struct_0_x1184_x1007_x1014605454}

[[Local IP: *local-ip*]{lang="EN-US"}]{#struct_0_x1184_x1007_x1938699221}

[[Track]{lang="EN-US"}]{#struct_0_x1184_x1007_x393395410}[模块通知]{style="font-family:宋体"}[BFD]{lang="EN-US"}[模块创建]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话]{style="font-family:宋体"}

[[BFD]{lang="EN-US"}]{#struct_0_x1184_x1007_56853398}[会话信息为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[会话模式为]{lang="EN-US" style="font-family:宋体"}*[session-mode]{lang="EN-US"}*]{#struct_0_x1184_x1007_907250098}[，取值为]{lang="EN-US" style="font-family:宋体"}[echo]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[control]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[出接口名为]{lang="EN-US" style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1184_x1007_985485956}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[出接口绑定的]{lang="EN-US" style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x1184_x1007_1952216036}[实例为]{lang="EN-US" style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[，如果出接口没有绑定]{lang="EN-US" style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，则打印"]{lang="EN-US" style="font-family:宋体"}[-]{lang="EN-US"}["]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对端]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1184_x1007_1556310446}[地址为]{lang="EN-US" style="font-family:宋体"}*[remote-ip]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本地]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1184_x1007_907184562}[地址为]{lang="EN-US" style="font-family:宋体"}*[local-ip]{lang="EN-US"}*

[[Notified BFD module to delete a BFD session.]{lang="EN-US"}]{#struct_0_x1184_x1007_x101863062}

[[BFD info: ]{lang="EN-US"}]{#struct_0_x1184_x1007_1590656329}

[[Session mode: *session-mode*]{lang="EN-US"}]{#struct_0_x1184_x1007_1643331998}

[[Outgoing interface: *interface-name*]{lang="EN-US"}]{#struct_0_x1184_x1007_907381170}

[[VPN instance: *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x1184_x1007_572120828}

[[Remote IP: *remote-ip*]{lang="EN-US"}]{#struct_0_x1184_x1007_53659645}

[[Local IP: *local-ip*]{lang="EN-US"}]{#struct_0_x1184_x1007_907315634}

[[Track]{lang="EN-US"}]{#struct_0_x1184_x1007_1721110166}[模块通知]{style="font-family:宋体"}[BFD]{lang="EN-US"}[模块删除]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话]{style="font-family:宋体"}

[[BFD]{lang="EN-US"}]{#struct_0_x1184_x1007_1268331462}[会话信息为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[会话模式为]{lang="EN-US" style="font-family:宋体"}*[session-mode]{lang="EN-US"}*]{#struct_0_x1184_x1007_1832896648}[，取值为]{lang="EN-US" style="font-family:宋体"}[echo]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[control]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[出接口名为]{lang="EN-US" style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1184_x1007_907512242}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[出接口绑定的]{lang="EN-US" style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x1184_x1007_x1143849948}[实例为]{lang="EN-US" style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[，如果出接口没有绑定]{lang="EN-US" style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，则打印"]{lang="EN-US" style="font-family:宋体"}[-]{lang="EN-US"}["]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对端]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1184_x1007_193012202}[地址为]{lang="EN-US" style="font-family:宋体"}*[remote-ip]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本地]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1184_x1007_907446706}[地址为]{lang="EN-US" style="font-family:宋体"}*[local-ip]{lang="EN-US"}*

[[Received the notification that application process *process-id* in slot *slot-number* had registered with track entry *entry-number*.]{lang="EN-US"}]{#struct_0_x1184_x1007_1190500656}

[[收到应用进程]{lang="EN-US" style="font-family:
  宋体"}*[process-id]{lang="EN-US"}*]{#struct_0_x1184_x1007_1956075527}[向]{lang="EN-US" style="font-family:宋体"}[track]{lang="EN-US"}[项]{lang="EN-US" style="font-family:宋体"}*[entry-number]{lang="EN-US"}*[注册联动的通知]{lang="EN-US" style="font-family:宋体"}[，]{style="font-family:
  宋体"}[[该进程所在板的板号为]{lang="EN-US" style="font-family:
  宋体"}[slot-number]{lang="EN-US"}]{.TableTextChar}

[[Received the notification that application process *process-id* in slot *slot-number* had deregistered with track entry *entry-number*.]{lang="EN-US"}]{#struct_0_x1184_x1007_907643314}

[[收到应用进程]{style="font-family:宋体"}*[process-id]{lang="EN-US"}*]{#struct_0_x1184_x1007_1482147522}[取消与]{style="font-family:宋体"}[track]{lang="EN-US"}[项]{style="font-family:宋体"}*[entry-number]{lang="EN-US"}*[注册联动的通知，[[该进程所在板的板号为]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*]{.TableTextChar}]{style="font-family:宋体"}

[[Created delay timer for track entry *entry-number*. Delay time: *time*, State: *state*]{lang="EN-US"}]{#struct_0_x1184_x1007_x1124674270}

[[为]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_x1184_x1007_x1107700245}[项]{style="font-family:宋体"}*[entry-number]{lang="EN-US"}*[创建延迟定时器，延迟时间为]{style="font-family:宋体"}*[time]{lang="EN-US"}*[，单位为秒，待通知的状态为]{style="font-family:宋体"}*[state]{lang="EN-US"}*

[[Delay timer for track entry *entry-number* expired.]{lang="EN-US"}]{#struct_0_x1184_x1007_907577778}

[[Track]{lang="EN-US"}]{#struct_0_x1184_x1007_785029565}[项]{style="font-family:宋体"}*[entry-number]{lang="EN-US"}*[的延迟定时器超时]{style="font-family:宋体"}

[[Deleted the delay timer for track entry *entry-number*.]{lang="EN-US"}]{#struct_0_x1184_x1007_907774386}

[[删除]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_x1184_x1007_1450362703}[项]{style="font-family:宋体"}*[entry-number]{lang="EN-US"}*[的延迟定时器]{style="font-family:宋体"}

[[Track *entry-number* registered with the CFD CC (service instance *service-id*, MEP *mep-id*).]{lang="EN-US"}]{#struct_0_x1184_x1007_x58377218}

[[Track]{lang="EN-US"}]{#struct_0_x1184_x1007_907708850}[项]{style="font-family:宋体"}[entry-number]{lang="EN-US"}[关联到]{style="font-family:宋体"}[CFD]{lang="EN-US"}[连续性检测功能（服务实例为]{style="font-family:宋体"}*[service-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[MEP]{lang="EN-US"}[为]{style="font-family:宋体"}*[mep-id]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Track *entry-number* deregistered with the CFD CC (service instance *service-id*, MEP *mep-id*).]{lang="EN-US"}]{#struct_0_x1184_x1007_x1981108809}

[[Track]{lang="EN-US"}]{#struct_0_x1184_x1007_x1632701170}[项]{style="font-family:宋体"}[entry-number]{lang="EN-US"}[与]{style="font-family:宋体"}[CFD]{lang="EN-US"}[连续性检测功能（服务实例为]{style="font-family:宋体"}*[service-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[MEP]{lang="EN-US"}[为]{style="font-family:宋体"}*[mep-id]{lang="EN-US"}*[）解除关联]{style="font-family:宋体"}

[[Received the notification that the state of CFD CC (service instance *service-id,* MEP *mep-id*) had changed to *state*.]{lang="EN-US"}]{#struct_0_x1184_x1007_907250099}

[[收到]{style="font-family:宋体"}[CFD]{lang="EN-US"}]{#struct_0_x1184_x1007_985485957}[服务实例]{style="font-family:宋体"}*[service-id]{lang="EN-US"}*[, MEP *mep-id* ]{lang="EN-US"}[的状态变化为]{style="font-family:宋体"}*[state]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1184_x1007_1952216035}

[[\# ]{lang="EN-US"}]{#struct_0_x1184_x1007_1556113838}[打开]{style="font-family:宋体"}[Track]{lang="EN-US"}[的调试信息开关。配置]{style="font-family:宋体"}[Track]{lang="EN-US"}[模块监测接口物理状态，并将监测结果通知给]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[模块。查看此时设备上打印的调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging track]{lang="EN-US"}]{#struct_0_x1184_x1007_x629946591}

[[\# ]{lang="EN-US"}]{#struct_0_x1184_x1007_966858893}[创建]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[，监测接口]{style="font-family:
宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的物理状态。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1184_x1007_907184563}

[\[Sysname\] track 1 interface gigabitethernet 1/0/1]{lang="EN-US"}

[\*May 28 13:19:26:421 2011 Sysname TRACK/7/debug: -MDC=1; The state of track entry 1 changed from NotReady to Positive.]{lang="EN-US"}

[*[// Track]{lang="EN-US"}*]{#struct_0_x1184_x1007_x101863063}*[项]{style="font-family:宋体"}[1]{lang="EN-US"}[的状态从]{style="font-family:宋体"}[NotReady]{lang="EN-US"}[转变为]{style="font-family:宋体"}[Positive]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1184_x1007_1590721865}[创建]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[，并关联]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[\[Sysname\] interface gigabitethernet 1/0/2]{lang="EN-US"}]{#struct_0_x1184_x1007_x1436097622}

[\[Sysname-GigabitEthernet1/0/2\] vrrp vrid 1 priority 110]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/2\] vrrp vrid 1 virtual ip 10.1.1.1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/2\] vrrp vrid 1 track 1 reduced 30]{lang="EN-US"}

[\*May 28 13:21:35:376 2011 Sysname TRACK/7/debug: -MDC=1; Received the notification that application process 952 had registered with track entry 1.]{lang="EN-US"}

*[// Track]{lang="EN-US" style="font-size:10.5pt;
font-family:\"Arial\",\"sans-serif\""}[模块接收到]{style="font-size:
10.5pt;font-family:宋体"}[VRRP]{lang="EN-US" style="font-size:
10.5pt;font-family:\"Arial\",\"sans-serif\""}[向]{style="font-size:10.5pt;font-family:宋体"}[Track]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}[项]{style="font-size:10.5pt;font-family:宋体"}[1]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}[注册联动的通知。]{style="font-size:10.5pt;font-family:宋体"}*

[\*May 28 13:21:35:376 2011 Sysname TRACK/7/debug: -MDC=1; Notified application process 952 in slot 1 that the state of track entry 1 had changed to Positive.]{lang="EN-US"}

[*[// Track]{lang="EN-US"}*]{#struct_0_x1184_x1007_1667280448}*[模块通知]{style="font-family:宋体"}[VRRP]{lang="EN-US"}*[：]{style="font-family:宋体"}*[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[的状态为]{style="font-family:宋体"}[Positive]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1184_x1007_x1022077935}[改变接口状态。]{style="font-family:宋体"}

[[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x1184_x1007_x1109449824}

[[\[Sysname-GigabitEthernet1/0/1\] shutdown]{lang="EN-US"}]{#struct_0_x1184_x1007_907381171}

[\*May 28 13:25:24:427 2011 Sysname TRACK/7/debug: -MDC=1; The state of track entry 1 changed from Positive to Negative.]{lang="EN-US"}

[*[// Track]{lang="EN-US"}*]{#struct_0_x1184_x1007_572120827}*[项]{style="font-family:宋体"}[1]{lang="EN-US"}[的状态为从]{style="font-family:宋体"}[Positive]{lang="EN-US"}[转变为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[，表示监测的接口物理状态变为]{style="font-family:宋体"}[down]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*May 28 13:25:24:427 2011 Sysname TRACK/7/debug: -MDC=1; Notified application process 952 in slot 1 that the state of track entry 1 had changed to Negative.]{lang="EN-US"}]{#struct_0_x1184_x1007_53659632}

[*[// Track]{lang="EN-US"}*]{#struct_0_x1184_x1007_x506814123}*[模块通知]{style="font-family:宋体"}[VRRP]{lang="EN-US"}*[：]{style="font-family:宋体"}*[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[的状态变为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[。]{style="font-family:宋体"}*
