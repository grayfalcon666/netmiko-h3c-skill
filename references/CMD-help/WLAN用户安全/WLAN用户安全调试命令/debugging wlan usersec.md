::: {#513843506 .myid}
[]{#_Toc404794920}[]{#struct_0_59269_x7909_x67820725}[]{#_Toc363740041}[]{#_Toc174161344}[]{#_Toc366658786}[]{#_Toc366658522}[]{#_Toc366658548}[]{#_Toc366658573}[]{#_Toc366658585}[]{#_Toc366658597}[]{#_Toc366658624}[]{#_Toc366658787}[]{#_Toc366658523}[]{#_Toc366658549}[]{#_Toc366658574}[]{#_Toc366658586}[]{#_Toc366658598}[]{#_Toc366658625}[]{#_Toc366658788}[]{#_Toc366658524}[]{#_Toc366658550}[]{#_Toc366658575}[]{#_Toc366658587}[]{#_Toc366658599}[]{#_Toc366658626}[]{#_Toc366658789}[]{#_Toc366658525}[]{#_Toc366658551}[]{#_Toc366658576}[]{#_Toc366658588}[]{#_Toc366658600}[]{#_Toc366658627}[]{#_Toc366658790}[]{#_Toc366658526}[]{#_Toc366658552}[]{#_Toc366658577}[]{#_Toc366658589}[]{#_Toc366658601}[]{#_Toc366658628}[]{#_Toc366658791}[]{#_Toc366658590}[]{#_Toc366658602}[]{#_Toc366658629}[]{#_Toc366658792}[]{#_Toc366658793}

**WLAN用户安全 \-- WLAN用户安全调试命令 \-- debugging wlan usersec**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_59269_x7909_672023164}

[**[debugging]{lang="EN-US"}**[ **wlan** **usersec** { **all** \| **error** \| **event** \| **fsm** \| **timer** \| **packet** { **receive** \| **send** } \[ **verbose** \] }]{lang="EN-US"}]{#struct_0_59269_x7909_106465975}

[**[undo]{lang="EN-US"}**[ **debugging** **wlan** **usersec** { **all** \| **error** \| **event** \| **fsm** \| **timer** \| **packet** { **receive** \| **send** } \[ **verbose** \] }]{lang="EN-US"}]{#struct_0_59269_x7909_x67820728}

[[【视图】]{style="font-family:黑体"}]{#struct_0_59269_x7909_1258768603}

[[用户视图]{style="font-family:宋体"}]{#struct_0_59269_x7909_657246600}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_59269_x7909_x1112681921}

[[network-admin]{lang="EN-US"}]{#struct_0_59269_x7909_1531796214}

[[mdc-admin]{lang="EN-US"}]{#struct_0_59269_x7909_1815836444}

[[【参数】]{style="font-family:黑体"}]{#struct_0_59269_x7909_1865015014}

[**[all]{lang="EN-US"}**]{#struct_0_59269_x7909_1188207314}[：表示]{style="font-family:宋体"}[usersec]{lang="EN-US"}[所有类型调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_59269_x7909_458741124}[：表示]{style="font-family:宋体"}[usersec]{lang="EN-US"}[错误类型调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_59269_x7909_1147131793}[：表示]{style="font-family:宋体"}[usersec]{lang="EN-US"}[事件类型调试信息开关。]{style="font-family:宋体"}

[**[timer]{lang="EN-US"}**]{#struct_0_59269_x7909_x491538357}[：表示]{style="font-family:宋体"}[usersec]{lang="EN-US"}[定时器调试信息开关。]{style="font-family:宋体"}

[**[fsm]{lang="EN-US"}**]{#struct_0_59269_x7909_1492025651}[：表示]{style="font-family:宋体"}[usersec]{lang="EN-US"}[状态机调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_59269_x7909_x1789938047}[：表示]{style="font-family:宋体"}[usersec]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[receive]{lang="EN-US"}**]{#struct_0_59269_x7909_672023165}[：表示]{style="font-family:宋体"}[usersec]{lang="EN-US"}[报文接收调试信息开关。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_59269_x7909_106465974}[：表示]{style="font-family:宋体"}[usersec]{lang="EN-US"}[报文发送调试信息开关。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_59269_x7909_x67820727}[：表示]{style="font-family:宋体"}[usersec]{lang="EN-US"}[报文的详细调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_59269_x7909_1258768606}

[**[debugging wlan usersec]{lang="EN-US"}**]{#struct_0_59269_x7909_657049992}[命令用来打开]{style="font-family:宋体"}[usersec]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging wlan usersec]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[usersec]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[usersec]{lang="EN-US"}]{#struct_0_59269_x7909_1412824360}[模块调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging wlan usersec error]{lang="EN-US"}]{#struct_0_59269_x7909_1488115343}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x794287659}[[字段]{style="font-family:黑体"}]{#struct_0_59269_x7909_1543749214}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_59269_x7909_x2136843034}

 

[[No security info in the client.]{lang="EN-US"}]{#struct_0_59269_x7909_x2033215032}

[[客户端中没有安全信息]{style="font-family:宋体"}]{#struct_0_59269_x7909_1183638455}

[[No security info in BSS *BSSID*.]{lang="EN-US"}]{#struct_0_59269_x7909_x1037577645}

[[BSS *BSSID*]{lang="EN-US"}]{#struct_0_59269_x7909_x1290001300}[中没有安全信息]{style="font-family:宋体"}

[[No security info in service template *STName*.]{lang="EN-US"}]{#struct_0_59269_x7909_x1869173658}

[[ST *STName*]{lang="EN-US"}]{#struct_0_59269_x7909_672023166}[中没有安全信息]{style="font-family:宋体"}

[[BSS *BSSID* doesn\'t support shared-key authentication.]{lang="EN-US"}]{#struct_0_59269_x7909_106465977}

[[BSS]{lang="EN-US"}]{#struct_0_59269_x7909_x67820730}[不支持]{style="font-family:宋体"}[shared-key]{lang="EN-US"}[认证算法]{style="font-family:宋体"}

[[Failed to process the 1st shared-key authentication frame: *Reason*.]{lang="EN-US"}]{#struct_0_59269_x7909_x697546525}

[[因为]{style="font-family:宋体"}*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_x1754788035}[，处理第]{style="font-family:宋体"}[1]{lang="EN-US"}[条]{style="font-family:宋体"}[shared-key]{lang="EN-US"}[认证报文]{style="font-family:宋体"}[失败]{style="font-family:宋体"}

[*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_x2020294388}[取值如下：]{style="font-family:宋体"}

[[Invalid transmission sequence number *TransNum*]{lang="EN-US"}]{#struct_0_59269_x7909_1695377259}[：传输序列号]{style="font-family:宋体"}*[TransNum]{lang="EN-US"}*[无效]{style="font-family:宋体"}

[[Failed to process the 3rd shared-key authentication frame: *Reason*.]{lang="EN-US"}]{#struct_0_59269_x7909_672023167}

[[因为]{style="font-family:宋体"}*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_106465976}[，处理第]{style="font-family:宋体"}[3]{lang="EN-US"}[条]{style="font-family:宋体"}[shared-key]{lang="EN-US"}[认证报文失败]{style="font-family:宋体"}

[*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_x67820729}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid challenge text]{lang="EN-US"}]{#struct_0_59269_x7909_1258768604}[：挑战码无效]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid transmission sequence number *TransNum*]{lang="EN-US"}]{#struct_0_59269_x7909_657181064}[：传输序列号]{style="font-family:KaiTi_GB2312"}*[TransNum]{lang="EN-US"}*[无效]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid challenge text length *ChlgTxtLength*]{lang="EN-US"}]{#struct_0_59269_x7909_x187361139}[：挑战码长度]{style="font-family:KaiTi_GB2312"}*[ChlgTxtLength]{lang="EN-US"}*[无效]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unencrypted frame]{lang="EN-US"}]{#struct_0_59269_x7909_x523192025}[：报文未加密]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Non-existent challenge IE or unsuccessful challenge IE decoding]{lang="EN-US"}]{#struct_0_59269_x7909_672023168}[：]{style="font-family:KaiTi_GB2312"} [挑战]{style="font-family:KaiTi_GB2312"}[IE]{lang="EN-US"}[不存在或者解析挑战]{style="font-family:KaiTi_GB2312"}[IE]{lang="EN-US"}[不正确]{style="font-family:KaiTi_GB2312"}

[[Failed to send the response for the unsuccessful shared-key authentication to the client.]{lang="EN-US"}]{#struct_0_59269_x7909_106465979}

[[向客户端发送]{style="font-family:宋体"}[shared-key]{lang="EN-US"}]{#struct_0_59269_x7909_x67820716}[认证失败回应报文失败]{style="font-family:宋体"}

[[Failed to send the response for the successful shared-key authentication to the client.]{lang="EN-US"}]{#struct_0_59269_x7909_x315209507}

[[向客户端发送]{style="font-family:宋体"}[shared-key]{lang="EN-US"}]{#struct_0_59269_x7909_2074346040}[认证成功回应报文失败]{style="font-family:宋体"}

[[Failed to send the *MsgType* message to the down-link device.]{lang="EN-US"}]{#struct_0_59269_x7909_x368123007}

[[下发]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*]{#struct_0_59269_x7909_x751468910}[消息失败]{style="font-family:宋体"}

[*[MsgType]{lang="EN-US"}*]{#struct_0_59269_x7909_672023169}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L2 authentication result]{lang="EN-US"}]{#struct_0_59269_x7909_106465978}[：二层认证结果]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L2 authorization result]{lang="EN-US"}]{#struct_0_59269_x7909_x67820715}[：二层授权结果]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L3 authentication result]{lang="EN-US"}]{#struct_0_59269_x7909_x315209504}[：三层认证结果]{style="font-family:KaiTi_GB2312"}

[[Failed to send the *MsgType* message to the up-link device.]{lang="EN-US"}]{#struct_0_59269_x7909_2074149432}

[[上报]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*]{#struct_0_59269_x7909_1861501560}[类型消息失败]{style="font-family:宋体"}

[*[MsgType]{lang="EN-US"}*]{#struct_0_59269_x7909_x487405634}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[starting L2 authentication]{lang="EN-US"}]{#struct_0_59269_x7909_x1372091406}[：开始二层认证]{style="font-family:
  KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[starting L3 authentication]{lang="EN-US"}]{#struct_0_59269_x7909_x1985826632}[：开始三层认证]{style="font-family:
  KaiTi_GB2312"}

[[Invalid sent session key length *SendKeyLen* or invalid received session key length *RecvKeyLen*.]{lang="EN-US"}]{#struct_0_59269_x7909_x696779015}

[[Send session key]{lang="EN-US"}]{#struct_0_59269_x7909_1861501561}[长度]{style="font-family:宋体"}*[SendKeyLen]{lang="EN-US"}*[或者]{style="font-family:宋体"}[received session key]{lang="EN-US"}[长度]{style="font-family:宋体"}*[RecvKeyLen]{lang="EN-US"}*[不合法]{style="font-family:宋体"}

[[Failed to send 4-way handshake message 3: *Reason.*]{lang="EN-US"}]{#struct_0_59269_x7909_x487471170}

[[因为]{style="font-family:宋体"}*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_x591808118}[，发送四次握手]{style="font-family:宋体"}[message3]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_907117009}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unsuccessful IE encoding]{lang="EN-US"}]{#struct_0_59269_x7909_1861501562}[：解析]{style="font-family:KaiTi_GB2312"}[IE]{lang="EN-US"}[失败]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unsuccessful GTK KDE obtaining]{lang="EN-US"}]{#struct_0_59269_x7909_x487536706}[：获取]{style="font-family:
  KaiTi_GB2312"}[GTK KDE]{lang="EN-US"}[失败]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unsuccessful key data encrypting]{lang="EN-US"}]{#struct_0_59269_x7909_981020161}[：加密]{style="font-family:
  KaiTi_GB2312"}[key data]{lang="EN-US"}[失败]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unsuccessful EAPOL-Key frame constructing]{lang="EN-US"}]{#struct_0_59269_x7909_1676193363}[：构造]{style="font-family:KaiTi_GB2312"}[EAPOL-Key]{lang="EN-US"}[报文失败]{style="font-family:KaiTi_GB2312"}

[[Failed to send group handshake message 1: *Reason*.]{lang="EN-US"}]{#struct_0_59269_x7909_1424271752}

[[因为]{style="font-family:宋体"}*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_579381440}[，发送]{style="font-family:宋体"}[组播握手]{style="font-family:宋体"}[message1]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_1861501563}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unsuccessful key data encrypting]{lang="EN-US"}]{#struct_0_59269_x7909_x487602242}[：加密]{style="font-family:
  KaiTi_GB2312"}[key data]{lang="EN-US"}[失败]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unsuccessful EAPOL-Key frame constructing]{lang="EN-US"}]{#struct_0_59269_x7909_1765366778}[：构造]{style="font-family:KaiTi_GB2312"}[EAPOL-key]{lang="EN-US"}[报文失败]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unsuccessful GTK KDE obtaining]{lang="EN-US"}]{#struct_0_59269_x7909_1566117777}[：获取]{style="font-family:
  KaiTi_GB2312"}[GTK KDE]{lang="EN-US"}[失败]{style="font-family:KaiTi_GB2312"}

[[Failed to process 4-way handshake message 2: *Reason.*]{lang="EN-US"}]{#struct_0_59269_x7909_22119406}

[[因为]{style="font-family:宋体"}*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_753136894}[，处理四次握手]{style="font-family:宋体"}[message2]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_1861501564}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unsuccessful PTK generating]{lang="EN-US"}]{#struct_0_59269_x7909_x487143490}[：产生]{style="font-family:
  KaiTi_GB2312"}[PTK]{lang="EN-US"}[失败]{style="font-family:
  KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid descriptor type]{lang="EN-US"}]{#struct_0_59269_x7909_x174272571}[：]{style="font-family:KaiTi_GB2312"}[descriptor type]{lang="EN-US"}[无效]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid replay counter]{lang="EN-US"}]{#struct_0_59269_x7909_197716748}[：]{style="font-family:KaiTi_GB2312"}[replay counter ]{lang="EN-US"}[无效]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid Key IV]{lang="EN-US"}]{#struct_0_59269_x7909_1861501565}[：]{style="font-family:KaiTi_GB2312"}[KeyIV]{lang="EN-US"}[无效]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid key data length *KeyDataLength*]{lang="EN-US"}]{#struct_0_59269_x7909_x487209026}[：]{style="font-family:KaiTi_GB2312"}[key data]{lang="EN-US"}[长度]{style="font-family:KaiTi_GB2312"}*[KeyDataLength]{lang="EN-US"}*[无效]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid MIC]{lang="EN-US"}]{#struct_0_59269_x7909_1387926537}[：]{style="font-family:KaiTi_GB2312"}[MIC]{lang="EN-US"}[无效]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unsuccessful frame decoding]{lang="EN-US"}]{#struct_0_59269_x7909_1298423680}[：解析报文失败]{style="font-family:
  KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unsuccessful IE decoding]{lang="EN-US"}]{#struct_0_59269_x7909_1861501566}[：解析]{style="font-family:KaiTi_GB2312"}[IE]{lang="EN-US"}[失败]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid IE]{lang="EN-US"}]{#struct_0_59269_x7909_x487274562}[：]{style="font-family:KaiTi_GB2312"}[IE]{lang="EN-US"}[无效]{style="font-family:KaiTi_GB2312"}

[[Failed to process 4-way handshake message 4: *Reason.*]{lang="EN-US"}]{#struct_0_59269_x7909_x1759897938}

[[因为]{style="font-family:宋体"}*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_339397662}[，处理四次握手]{style="font-family:宋体"}[message4]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_1861501567}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid descriptor type]{lang="EN-US"}]{#struct_0_59269_x7909_x487340098}[：]{style="font-family:KaiTi_GB2312"}[descriptor type]{lang="EN-US"}[无效]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid replay counter]{lang="EN-US"}]{#struct_0_59269_x7909_x976206702}[：]{style="font-family:KaiTi_GB2312"}[replay counter ]{lang="EN-US"}[无效]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid Key IV]{lang="EN-US"}]{#struct_0_59269_x7909_x615465601}[：]{style="font-family:KaiTi_GB2312"}[KeyIV]{lang="EN-US"}[无效]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid key data length *KeyDataLength*]{lang="EN-US"}]{#struct_0_59269_x7909_1861501568}[：]{style="font-family:KaiTi_GB2312"}[key data]{lang="EN-US"}[长度]{style="font-family:KaiTi_GB2312"}*[KeyDataLength]{lang="EN-US"}*[无效]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid MIC]{lang="EN-US"}]{#struct_0_59269_x7909_x486881346}[：]{style="font-family:KaiTi_GB2312"}[MIC]{lang="EN-US"}[无效]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unsuccessful frame decoding]{lang="EN-US"}]{#struct_0_59269_x7909_x637421051}[：解析报文失败]{style="font-family:
  KaiTi_GB2312"}

[[Failed to process group handshake message 2: *Reason.*]{lang="EN-US"}]{#struct_0_59269_x7909_1861501569}

[[因为]{style="font-family:宋体"}*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_x486946882}[，处理组播握手]{style="font-family:宋体"}[message2]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_x2126369139}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid descriptor type]{lang="EN-US"}]{#struct_0_59269_x7909_x94813576}[：]{style="font-family:KaiTi_GB2312"}[descriptor type]{lang="EN-US"}[无效]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid replay counter]{lang="EN-US"}]{#struct_0_59269_x7909_x2117750028}[：]{style="font-family:KaiTi_GB2312"}[replay counter ]{lang="EN-US"}[无效]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid Key IV]{lang="EN-US"}]{#struct_0_59269_x7909_1933459754}[：]{style="font-family:KaiTi_GB2312"}[KeyIV]{lang="EN-US"}[无效]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid key data length *KeyDataLength*]{lang="EN-US"}]{#struct_0_59269_x7909_x94813575}[：]{style="font-family:KaiTi_GB2312"}[key data]{lang="EN-US"}[长度]{style="font-family:KaiTi_GB2312"}*[KeyDataLength]{lang="EN-US"}*[无效]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid MIC]{lang="EN-US"}]{#struct_0_59269_x7909_x2117750025}[：]{style="font-family:KaiTi_GB2312"}[MIC]{lang="EN-US"}[无效]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unsuccessful frame decoding]{lang="EN-US"}]{#struct_0_59269_x7909_1886405587}[：解析报文失败]{style="font-family:
  KaiTi_GB2312"}

[[Failed to process the 4-way handshake request: *Reason.*]{lang="EN-US"}]{#struct_0_59269_x7909_x1419461123}

[[因为]{style="font-family:宋体"}*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_x94813574}[，处理四次握手]{style="font-family:宋体"}[request]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_x2117750026}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid replay counter]{lang="EN-US"}]{#struct_0_59269_x7909_1483121060}[：]{style="font-family:KaiTi_GB2312"}[replay counter ]{lang="EN-US"}[无效]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid MIC]{lang="EN-US"}]{#struct_0_59269_x7909_x94813573}[：]{style="font-family:KaiTi_GB2312"}[MIC]{lang="EN-US"}[无效]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unsuccessful frame decoding]{lang="EN-US"}]{#struct_0_59269_x7909_x2117750023}[：解析报文失败]{style="font-family:
  KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[The current client hasn\'t finished key negotiation or 4-way handshake]{lang="EN-US"}]{#struct_0_59269_x7909_723606173}[：当前客户端还未完成密钥协商或者四次握手]{style="font-family:KaiTi_GB2312"}

[[Failed to process the MIC failure report: *Reason.*]{lang="EN-US"}]{#struct_0_59269_x7909_x94813572}

[[因为]{style="font-family:宋体"}*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_x2117750024}[，处理]{style="font-family:宋体"}[MIC]{lang="EN-US"}[错误报告报文失败]{style="font-family:宋体"}

[*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_320321646}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid replay counter]{lang="EN-US"}]{#struct_0_59269_x7909_x2004876198}[：]{style="font-family:KaiTi_GB2312"}[replay counter ]{lang="EN-US"}[无效]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unsuccessful frame decoding]{lang="EN-US"}]{#struct_0_59269_x7909_x94813571}[：解析报文失败]{style="font-family:
  KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid RSC]{lang="EN-US"}]{#struct_0_59269_x7909_x2117750021}[：]{style="font-family:KaiTi_GB2312"}[RSC]{lang="EN-US"}[无效]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[The current client hasn\'t finished key negotiation]{lang="EN-US"}]{#struct_0_59269_x7909_x94813570}[：当前客户端未完成密钥协商]{style="font-family:KaiTi_GB2312"}

[[BSS *BSSID* failed to process the time-based GTK rekey.]{lang="EN-US"}]{#struct_0_59269_x7909_x2117750022}

[[BSS ]{lang="EN-US"}*[BSSID]{lang="EN-US"}*]{#struct_0_59269_x7909_x842477768}[处理基于时间更新]{style="font-family:宋体"}[GTK]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[BSS *BSSID* failed to process the packet-based GTK rekey.]{lang="EN-US"}]{#struct_0_59269_x7909_844876365}

[[BSS ]{lang="EN-US"}*[BSSID]{lang="EN-US"}*]{#struct_0_59269_x7909_x94813569}[处理基于报文更新]{style="font-family:宋体"}[GTK]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[BSS *BSSID* failed to process the stationoff-based GTK rekey.]{lang="EN-US"}]{#struct_0_59269_x7909_x161434893}

[[BSS ]{lang="EN-US"}*[BSSID]{lang="EN-US"}*]{#struct_0_59269_x7909_x24185929}[处理基于客户端下线更新]{style="font-family:宋体"}[GTK]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to send the add mobile message.]{lang="EN-US"}]{#struct_0_59269_x7909_x1305990324}

[[发送]{style="font-family:宋体"}[add mobile]{lang="EN-US"}]{#struct_0_59269_x7909_x94813568}[消息失败]{style="font-family:宋体"}

[[BSS *BSSID* failed to send the update WLAN message.]{lang="EN-US"}]{#struct_0_59269_x7909_x161434894}

[[BSS ]{lang="EN-US"}*[BSSID]{lang="EN-US"}*]{#struct_0_59269_x7909_x23727177}[发送]{style="font-family:宋体"}[update wlan]{lang="EN-US"}[消息失败]{style="font-family:宋体"}

[[Failed to add security TLV data to the add mobile message.]{lang="EN-US"}]{#struct_0_59269_x7909_x94813567}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[添加安全]{lang="EN-US" style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_59269_x7909_x161434891}[数据]{lang="EN-US" style="font-family:宋体"}[至]{style="font-family:宋体"}[add ]{lang="EN-US"}[mobile]{lang="EN-US"}[类型消息失败]{lang="EN-US" style="font-family:宋体"}

[[BSS *BSSID* failed to add security TLV data to the add WLAN message.]{lang="EN-US"}]{#struct_0_59269_x7909_x24054857}

[[添加安全]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_59269_x7909_x2051128712}[数据至]{style="font-family:宋体"}[add wlan ]{lang="EN-US"}[类型消息失败]{style="font-family:宋体"}

[[Failed to get security TLV data from the add mobile message.]{lang="EN-US"}]{#struct_0_59269_x7909_1230302182}

[[从]{style="font-family:宋体"}[add mobile]{lang="EN-US"}]{#struct_0_59269_x7909_x459932052}[消息中获取安全]{style="font-family:宋体"}[TLV]{lang="EN-US"}[数据失败]{style="font-family:宋体"}

[[Failed to get security TLV data from the add WLAN message.]{lang="EN-US"}]{#struct_0_59269_x7909_x2051128711}

[[从]{style="font-family:宋体"}[add wlan]{lang="EN-US"}]{#struct_0_59269_x7909_x1498581173}[消息中获取安全]{style="font-family:宋体"}[TLV]{lang="EN-US"}[数据失败]{style="font-family:宋体"}

[[Failed to fill the add mobile message: *Reason*.]{lang="EN-US"}]{#struct_0_59269_x7909_x1031787755}

[[因为]{style="font-family:宋体"}*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_x2051128710}[，填充]{style="font-family:宋体"}[add mobile]{lang="EN-US"}[消息失败]{style="font-family:宋体"}

[*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_67502768}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[U]{lang="EN-US"}[nsuccessful ]{lang="EN-US"}]{#struct_0_59269_x7909_x951166773}[WEP]{lang="EN-US"}[ key]{lang="EN-US"}[ decrypting]{lang="EN-US"}[：]{style="font-family:宋体"}[解密]{lang="EN-US" style="font-family:宋体"}[wep key]{lang="EN-US"}[失败]{lang="EN-US" style="font-family:宋体"}

[[BSS *BSSID* failed to fill the add WLAN message: *Reason*.]{lang="EN-US"}]{#struct_0_59269_x7909_x2051128709}

[[因为]{style="font-family:宋体"}*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_x1142416349}[，填充]{style="font-family:宋体"}[add wlan]{lang="EN-US"}[消息失败]{style="font-family:宋体"}

[*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_535360907}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[U]{lang="EN-US"}[nsuccessful GTK decrypting]{lang="EN-US"}]{#struct_0_59269_x7909_x2051128708}[：]{style="font-family:宋体"}[解密]{lang="EN-US" style="font-family:宋体"}[GTK]{lang="EN-US"}[失败]{lang="EN-US" style="font-family:宋体"}

[[Failed to process the add mobile message: *Reason*.]{lang="EN-US"}]{#struct_0_59269_x7909_423667592}

[[因为]{style="font-family:宋体"}*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_1181268441}[，处理]{style="font-family:宋体"}[add mobile]{lang="EN-US"}[消息失败]{style="font-family:宋体"}

[*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_x2051128707}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unsuccessful]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_59269_x7909_1633521173}[WEP]{lang="EN-US"}[ key]{lang="EN-US"}[ ]{lang="EN-US"}[encrypting]{lang="EN-US"}[：]{style="font-family:宋体"}[加密]{lang="EN-US" style="font-family:宋体"}[wep key]{lang="EN-US"}[失败]{lang="EN-US" style="font-family:宋体"}

[[BSS *BSSID* failed to process the add WLAN message: *Reason*.]{lang="EN-US"}]{#struct_0_59269_x7909_331325401}

[[因为]{style="font-family:宋体"}*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_x2051128706}[，处理]{style="font-family:宋体"}[add wlan]{lang="EN-US"}[消息失败]{style="font-family:宋体"}

[*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_x1095362182}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unsuccessful]{lang="EN-US"}[ GTK encrypting]{lang="EN-US"}]{#struct_0_59269_x7909_x2051128705}[：]{style="font-family:宋体"}[加密]{lang="EN-US" style="font-family:宋体"}[GTK]{lang="EN-US"}[失败]{lang="EN-US" style="font-family:宋体"}

[[Failed to fill security driver information for the client.]{lang="EN-US"}]{#struct_0_59269_x7909_470721759}

[[客户端填充安全驱动信息失败]{style="font-family:宋体"}]{#struct_0_59269_x7909_x2051128704}

[[Failed to fill security driver information for BSS *BSSID*.]{lang="EN-US"}]{#struct_0_59269_x7909_2036805700}

[[BSS ]{lang="EN-US"}*[BSSID]{lang="EN-US"}*]{#struct_0_59269_x7909_x2051128703}[填充安全驱动信息失败]{style="font-family:宋体"}

[[Failed to process the (re)association request without security IE: *Reason*.]{lang="EN-US"}]{#struct_0_59269_x7909_x335847295}

[[因为]{style="font-family:宋体"}*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_x2057665203}[，处理不带安全]{style="font-family:宋体"}[IE]{lang="EN-US"}[的]{style="font-family:宋体"}[(]{lang="EN-US"}[重]{style="font-family:宋体"}[)]{lang="EN-US"}[关联请求失败]{style="font-family:宋体"}

[*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_287523448}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[I]{lang="EN-US"}[nvalid security mode ]{lang="EN-US"}]{#struct_0_59269_x7909_522844856}[of the client]{lang="EN-US"}[：]{style="font-family:宋体"}[客户端]{lang="EN-US" style="font-family:宋体"}[的安全模式无效]{style="font-family:宋体"}

[[Failed to process the reassociation request without security IE: *Reason*.]{lang="EN-US"}]{#struct_0_59269_x7909_x1945647042}

[[因为]{style="font-family:宋体"}*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_287523449}[，处理不带安全]{style="font-family:宋体"}[IE]{lang="EN-US"}[的重关联请求失败]{style="font-family:宋体"}

[*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_522844857}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Security IE already exists in the client]{lang="EN-US"}]{#struct_0_59269_x7909_287523450}[：]{style="font-family:宋体"}[客户端结构下已存在]{lang="EN-US" style="font-family:宋体"}[IE]{lang="EN-US"}

[[Failed to process the association request without security IE: *Reason*.]{lang="EN-US"}]{#struct_0_59269_x7909_x1815807312}

[[因为]{style="font-family:宋体"}*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_x361560495}[，处理不带安全]{style="font-family:宋体"}[IE]{lang="EN-US"}[的关联请求失败]{style="font-family:宋体"}

[*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_287523451}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No WEP key exists]{lang="EN-US"}]{#struct_0_59269_x7909_x1815807311}[：]{style="font-family:KaiTi_GB2312"}[Wep key ]{lang="EN-US"}[不存在]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[The shared-key client failed to save the WEP key]{lang="EN-US"}]{#struct_0_59269_x7909_41724032}[：]{style="font-family:KaiTi_GB2312"}[shared-key]{lang="EN-US"}[模式下客户端填充]{style="font-family:KaiTi_GB2312"}[wep key]{lang="EN-US"}[失败]{style="font-family:KaiTi_GB2312"}

[[Failed to process the (re)association request with security IE: *Reason*.]{lang="EN-US"}]{#struct_0_59269_x7909_287523452}

[[因为]{style="font-family:宋体"}*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_x1815807314}[，处理带安全]{style="font-family:宋体"}[IE]{lang="EN-US"}[的]{style="font-family:宋体"}[(]{lang="EN-US"}[重]{style="font-family:宋体"}[)]{lang="EN-US"}[关联请求失败]{style="font-family:宋体"}

[*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_287523453}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid security IE]{lang="EN-US"}]{#struct_0_59269_x7909_x1815807313}[：安全]{style="font-family:KaiTi_GB2312"}[IE]{lang="EN-US"}[无效]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[The client doesn\'t use open system authentication]{lang="EN-US"}]{#struct_0_59269_x7909_1204523446}[：客户端链路认证方式不是]{style="font-family:KaiTi_GB2312"}[open-system]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[The BSS is configured with no cipher suite]{lang="EN-US"}]{#struct_0_59269_x7909_287523454}[：]{style="font-family:KaiTi_GB2312"}[BSS]{lang="EN-US"}[下未配置加密套件]{style="font-family:KaiTi_GB2312"}

[[Failed to process the (re)association request with RSN IE: *Reason*.]{lang="EN-US"}]{#struct_0_59269_x7909_x1815807316}

[[因为]{style="font-family:宋体"}*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_1607807973}[，处理带]{style="font-family:宋体"}[RSNIE]{lang="EN-US"}[的]{style="font-family:宋体"}[(]{lang="EN-US"}[重]{style="font-family:宋体"}[)]{lang="EN-US"}[关联请求失败]{style="font-family:宋体"}

[*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_287523455}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}[he security mode ]{lang="EN-US"}]{#struct_0_59269_x7909_x1815807315}[for the BSS ]{lang="EN-US"}[is not RSN]{lang="EN-US"}[：]{style="font-family:宋体"}[BSS]{lang="EN-US"}[下安全模式不是]{lang="EN-US" style="font-family:宋体"}[RSN]{lang="EN-US"}

[[Failed to process the reassociation request with RSN IE: *Reason*.]{lang="EN-US"}]{#struct_0_59269_x7909_2011092500}

[[因为]{style="font-family:宋体"}*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_287523456}[，处理带]{style="font-family:宋体"}[RSNIE]{lang="EN-US"}[的重关联请求失败]{style="font-family:宋体"}

[*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_x1815807318}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid capability field in the frame]{lang="EN-US"}]{#struct_0_59269_x7909_287523457}[：报文中的]{style="font-family:KaiTi_GB2312"}[capability]{lang="EN-US"}[字段无效]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid cipher suite or AKM mode in the frame]{lang="EN-US"}]{#struct_0_59269_x7909_x1815807317}[：报文中的]{style="font-family:KaiTi_GB2312"}[cipher suite ]{lang="EN-US"}[或者]{style="font-family:KaiTi_GB2312"}[AMK]{lang="EN-US"}[无效]{style="font-family:KaiTi_GB2312"}

[[Failed to process the (re)association request with WPA IE: *Reason*.]{lang="EN-US"}]{#struct_0_59269_x7909_x1668791688}

[[因为]{style="font-family:宋体"}*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_663147405}[，处理带]{style="font-family:宋体"}[WPAIE]{lang="EN-US"}[的]{style="font-family:宋体"}[(]{lang="EN-US"}[重]{style="font-family:宋体"}[)]{lang="EN-US"}[关联请求失败]{style="font-family:宋体"}

[*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_x1481628608}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[The security mode for the BSS is not WPA]{lang="EN-US"}]{#struct_0_59269_x7909_x1668791687}[：]{style="font-family:宋体"}[BSS]{lang="EN-US"}[中安全模式不是]{style="font-family:宋体"}[WPA]{lang="EN-US"}

[[Failed to process the reassociation request with WPA IE: *Reason*.]{lang="EN-US"}]{#struct_0_59269_x7909_710201572}

[[因为]{style="font-family:宋体"}*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_x1668791686}[，处理带]{style="font-family:宋体"}[WPAIE]{lang="EN-US"}[的重关联请求失败]{style="font-family:宋体"}

[*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_x855882369}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[I]{lang="EN-US"}[nvalid IE in ]{lang="EN-US"}]{#struct_0_59269_x7909_x1093531179}[the ]{lang="EN-US"}[frame]{lang="EN-US"}[：]{style="font-family:宋体"}[报文中的]{lang="EN-US" style="font-family:宋体"}[IE]{lang="EN-US"}[无效]{lang="EN-US" style="font-family:宋体"}

[[Failed to select a unicast cipher suite for the client.]{lang="EN-US"}]{#struct_0_59269_x7909_x1668791685}

[[客户端选择单播加密套件失败]{style="font-family:宋体"}]{#struct_0_59269_x7909_x452597842}

[[Failed to select an AKM mode for the client.]{lang="EN-US"}]{#struct_0_59269_x7909_1000260145}

[[客户端选择]{style="font-family:宋体"}[AKM]{lang="EN-US"}]{#struct_0_59269_x7909_x1668791684}[模式失败]{style="font-family:宋体"}

[[Invalid element ID in the RSN IE.]{lang="EN-US"}]{#struct_0_59269_x7909_x2018681783}

[[RSN IE]{lang="EN-US"}]{#struct_0_59269_x7909_x1668791683}[中]{style="font-family:宋体"}[element ID]{lang="EN-US"}[无效]{style="font-family:宋体"}

[[Invalid version in the RSN IE.]{lang="EN-US"}]{#struct_0_59269_x7909_x1259166896}

[[RSN IE]{lang="EN-US"}]{#struct_0_59269_x7909_x1799203143}[中版本无效]{style="font-family:宋体"}

[[Invalid group cipher suite in the security IE.]{lang="EN-US"}]{#struct_0_59269_x7909_x1668791682}

[[安全]{style="font-family:宋体"}[IE]{lang="EN-US"}]{#struct_0_59269_x7909_1469716459}[中组播加密套件无效]{style="font-family:宋体"}

[[Invalid unicast cipher suite in the security IE.]{lang="EN-US"}]{#struct_0_59269_x7909_x1668791681}

[[安全]{style="font-family:宋体"}[IE]{lang="EN-US"}]{#struct_0_59269_x7909_1873000986}[中单播加密套件无效]{style="font-family:宋体"}

[[Invalid element ID in the WPA IE.]{lang="EN-US"}]{#struct_0_59269_x7909_1885877503}

[[WPA IE]{lang="EN-US"}]{#struct_0_59269_x7909_x1668791680}[中]{style="font-family:宋体"}[element ID]{lang="EN-US"}[无效]{style="font-family:宋体"}

[[Invalid OUI in the WPA IE.]{lang="EN-US"}]{#struct_0_59269_x7909_306917045}

[[WPA IE]{lang="EN-US"}]{#struct_0_59269_x7909_x1668791679}[中]{style="font-family:宋体"}[OUI]{lang="EN-US"}[无效]{style="font-family:宋体"}

[[Invalid OUI type in the WPA IE.]{lang="EN-US"}]{#struct_0_59269_x7909_x2066718990}

[[WPA IE]{lang="EN-US"}]{#struct_0_59269_x7909_x1661582798}[中]{style="font-family:宋体"}[OUI]{lang="EN-US"}[类型无效]{style="font-family:宋体"}

[[Invalid version in the WPA IE.]{lang="EN-US"}]{#struct_0_59269_x7909_669860472}

[[WPA IE]{lang="EN-US"}]{#struct_0_59269_x7909_x789902225}[中版本无效]{style="font-family:宋体"}

[[Failed to get security info for roaming clients.]{lang="EN-US"}]{#struct_0_59269_x7909_669860473}

[[获取漫游用户迁移安全信息失败]{style="font-family:宋体"}]{#struct_0_59269_x7909_x789902226}

[[BSS *BSSID* failed to inherit PMK from service template *STName*: *Reason*.]{lang="EN-US"}]{#struct_0_59269_x7909_669860474}

[[因为]{style="font-family:宋体"}*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_x789902231}[，]{style="font-family:宋体"}[ BSS]{lang="EN-US"}*[ BSSID]{lang="EN-US"}*[从服务模板]{style="font-family:宋体"}*[STName]{lang="EN-US"}*[继承]{style="font-family:宋体"}[PMK]{lang="EN-US"}[失败]{style="font-family:宋体"}

[*[Reason]{lang="EN-US"}*]{#struct_0_59269_x7909_669860475}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unsuccessful PSK decoding]{lang="EN-US"}]{#struct_0_59269_x7909_x789902232}[：解析]{style="font-family:KaiTi_GB2312"}[PSK]{lang="EN-US"}[失败]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[The PSK was not converted to PMK]{lang="EN-US"}]{#struct_0_59269_x7909_669860476}[：把]{style="font-family:
  KaiTi_GB2312"}[PSK]{lang="EN-US"}[转成]{style="font-family:
  KaiTi_GB2312"}[PMK]{lang="EN-US"}[失败]{style="font-family:
  KaiTi_GB2312"}

[[BSS *BSSID* failed to inherit the group cipher suite from service template *STName*.]{lang="EN-US"}]{#struct_0_59269_x7909_x789902229}

[[BSS]{lang="EN-US"}*[ BSSID]{lang="EN-US"}*]{#struct_0_59269_x7909_669860477}[从服务模板]{style="font-family:宋体"}*[STName]{lang="EN-US"}*[中继承]{style="font-family:宋体"}[组播加密套件失败]{style="font-family:宋体"}

[[BSS *BSSID* failed to inherit the WEP key configuration from service template *STName*.]{lang="EN-US"}]{#struct_0_59269_x7909_x789902230}

[[BSS]{lang="EN-US"}*[ BSSID]{lang="EN-US"}*]{#struct_0_59269_x7909_x1519231975}[从服务模板]{style="font-family:宋体"}*[STName]{lang="EN-US"}*[中继承]{style="font-family:宋体"}[wep key]{lang="EN-US"}[配置失败]{style="font-family:宋体"}

[[Failed to deactivate the security information in the client.]{lang="EN-US"}]{#struct_0_59269_x7909_669860478}

[[去激活客户端中的安全信息失败]{style="font-family:宋体"}]{#struct_0_59269_x7909_x789902235}

[[Failed to initialize PMF info in service template ]{lang="EN-US"}*[STName]{lang="EN-US"}*[: Failed to allocate memory]{lang="EN-US"}[.]{lang="EN-US"}]{#struct_0_59269_x7909_x668481085}

[[由于申请内存空间失败，初始化服务模板]{style="font-family:宋体"}*[STName]{lang="EN-US"}*]{#struct_0_59269_x7909_1610063576}[中]{style="font-family:宋体"}[PMF]{lang="EN-US"}[信息失败。]{style="font-family:宋体"}

[[\[]{lang="EN-US"}[APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID*\] Failed to initialize PMF info in BSS: Failed to allocate memory.]{lang="EN-US"}]{#struct_0_59269_x7909_x1118819779}

[[APID]{lang="EN-US"}]{#struct_0_59269_x7909_1608775345}[为]{style="font-family:宋体"}*[APID]{lang="EN-US"}*[，]{style="font-family:宋体"}[RadioID]{lang="EN-US"}[为]{style="font-family:宋体"}*[RadioID]{lang="EN-US"}*[，]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，由于申请内存空间失败，初始化]{style="font-family:宋体"}[BSS]{lang="EN-US"}[中]{style="font-family:宋体"}[PMF]{lang="EN-US"}[信息失败。]{style="font-family:宋体"}

[[\[MAC: *UserMAC*, ]{lang="EN-US"}[APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID*\] Failed to initialize PMF info in client: Failed to allocate memory.]{lang="EN-US"}]{#struct_0_59269_x7909_1253767680}

[[用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_59269_x7909_x441387925}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[ ]{lang="EN-US"}[，]{style="font-family:宋体"}[APID]{lang="EN-US"}[为]{style="font-family:宋体"}*[APID]{lang="EN-US"}*[，]{style="font-family:宋体"}[RadioID]{lang="EN-US"}[为]{style="font-family:宋体"}*[RadioID]{lang="EN-US"}*[，]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，由于申请内存空间失败，初始化客户端中]{style="font-family:宋体"}[PMF]{lang="EN-US"}[信息失败。]{style="font-family:宋体"}

[[\[]{lang="EN-US"}[APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID*\] Failed to add PMF TLV to the add wlan message.]{lang="EN-US"}]{#struct_0_59269_x7909_x1475115675}

[[APID]{lang="EN-US"}]{#struct_0_59269_x7909_411024649}[为]{style="font-family:宋体"}*[APID]{lang="EN-US"}*[，]{style="font-family:宋体"}[RadioID]{lang="EN-US"}[为]{style="font-family:宋体"}*[RadioID]{lang="EN-US"}*[，]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，向]{style="font-family:宋体"}[add wlan]{lang="EN-US"}[消息中追加]{style="font-family:宋体"}[PMF TLV]{lang="EN-US"}[数据失败。]{style="font-family:宋体"}

[[\[]{lang="EN-US"}[APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID*\] Failed to add PMF TLV to the update wlan message.]{lang="EN-US"}]{#struct_0_59269_x7909_90968266}

[[APID]{lang="EN-US"}]{#struct_0_59269_x7909_1657052207}[为]{style="font-family:宋体"}*[APID]{lang="EN-US"}*[，]{style="font-family:宋体"}[RadioID]{lang="EN-US"}[为]{style="font-family:宋体"}*[RadioID]{lang="EN-US"}*[，]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，向]{style="font-family:宋体"}[update wlan]{lang="EN-US"}[消息中追加]{style="font-family:宋体"}[PMF TLV]{lang="EN-US"}[数据失败。]{style="font-family:宋体"}

[[\[MAC: *UserMAC*, ]{lang="EN-US"}[APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID*\] Failed to add PMF TLV to the add mobile message.]{lang="EN-US"}]{#struct_0_59269_x7909_x185320486}

[[用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_59269_x7909_x1071831148}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[ ]{lang="EN-US"}[，]{style="font-family:宋体"}[APID]{lang="EN-US"}[为]{style="font-family:宋体"}*[APID]{lang="EN-US"}*[，]{style="font-family:宋体"}[RadioID]{lang="EN-US"}[为]{style="font-family:宋体"}*[RadioID]{lang="EN-US"}*[，]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，向]{style="font-family:宋体"}[add mobile]{lang="EN-US"}[消息中追加]{style="font-family:宋体"}[PMF TLV]{lang="EN-US"}[数据失败。]{style="font-family:宋体"}

[[\[MAC: *UserMAC*, ]{lang="EN-US"}[APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID*\] Failed to send SA query response.]{lang="EN-US"}]{#struct_0_59269_x7909_x1935092151}

[[用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_59269_x7909_494252793}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[ ]{lang="EN-US"}[，]{style="font-family:宋体"}[APID]{lang="EN-US"}[为]{style="font-family:宋体"}*[APID]{lang="EN-US"}*[，]{style="font-family:宋体"}[RadioID]{lang="EN-US"}[为]{style="font-family:宋体"}*[RadioID]{lang="EN-US"}*[，]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，发送安全关联询问应答报文失败。]{style="font-family:宋体"}

[[\[MAC: *UserMAC*, ]{lang="EN-US"}[APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID*\] Invalid SA query transaction ID.]{lang="EN-US"}]{#struct_0_59269_x7909_2060336734}

[[用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_59269_x7909_x1013448117}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[ ]{lang="EN-US"}[，]{style="font-family:宋体"}[APID]{lang="EN-US"}[为]{style="font-family:宋体"}*[APID]{lang="EN-US"}*[，]{style="font-family:宋体"}[RadioID]{lang="EN-US"}[为]{style="font-family:宋体"}*[RadioID]{lang="EN-US"}*[，]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，安全关联询问应答中的]{style="font-family:宋体"}[transaction ID]{lang="EN-US"}[是无效的。]{style="font-family:宋体"}

[[\[MAC: *UserMAC*, ]{lang="EN-US"}[APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID*\] Failed to send SA query request.]{lang="EN-US"}]{#struct_0_59269_x7909_x668546621}

[[用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_59269_x7909_1930747080}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[ ]{lang="EN-US"}[，]{style="font-family:宋体"}[APID]{lang="EN-US"}[为]{style="font-family:宋体"}*[APID]{lang="EN-US"}*[，]{style="font-family:宋体"}[RadioID]{lang="EN-US"}[为]{style="font-family:宋体"}*[RadioID]{lang="EN-US"}*[，]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，发送安全关联询问请求报文失败。]{style="font-family:宋体"}

[[The security IE must be RSN and the cipher suite must be CCMP when PMF is enabled.]{lang="EN-US"}]{#struct_0_59269_x7909_1609998040}

[[若配置]{style="font-family:宋体"}[PMF]{lang="EN-US"}]{#struct_0_59269_x7909_x1118885315}[开关，安全]{style="font-family:宋体"}[IE]{lang="EN-US"}[必须配置为]{style="font-family:宋体"}[RSN]{lang="EN-US"}[并且加密套件必须配置为]{style="font-family:宋体"}[CCMP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[Failed to update IGTK for BSS *BSSID*: Failed to generate IGTK.]{lang="EN-US"}]{#struct_0_59269_x7909_x271283782}

[[由于生成]{style="font-family:宋体"}[IGTK]{lang="EN-US"}]{#struct_0_59269_x7909_1387985408}[失败，]{style="font-family:宋体"}[BSS *BSSID*]{lang="EN-US"}[更新]{style="font-family:宋体"}[IGTK]{lang="EN-US"}[失败。]{style="font-family:宋体"}

[[\[MAC: *UserMAC*, ]{lang="EN-US"}[APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID*\] PMF negotiation failed: Invalid client security mode or security IE when PMF status is mandatory. ]{lang="EN-US"}]{#struct_0_59269_x7909_x1073300142}

[[用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_59269_x7909_x1340897947}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[APID]{lang="EN-US"}[为]{style="font-family:宋体"}*[APID]{lang="EN-US"}*[，]{style="font-family:宋体"}[RadioID]{lang="EN-US"}[为]{style="font-family:宋体"}*[RadioID]{lang="EN-US"}*[，]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[。当]{style="font-family:宋体"}[PMF]{lang="EN-US"}[为强制状态时，客户端的安全模式或者安全]{style="font-family:宋体"}[IE]{lang="EN-US"}[信息非法。]{style="font-family:宋体"}

[[\[MAC: *UserMAC*, ]{lang="EN-US"}[APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID*\] PMF negotiation failed: Unmatched PMF capabilities.]{lang="EN-US"}]{#struct_0_59269_x7909_225185994}

[[用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_59269_x7909_x1120188471}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[ ]{lang="EN-US"}[，]{style="font-family:宋体"}[APID]{lang="EN-US"}[为]{style="font-family:宋体"}*[APID]{lang="EN-US"}*[，]{style="font-family:宋体"}[RadioID]{lang="EN-US"}[为]{style="font-family:宋体"}*[RadioID]{lang="EN-US"}*[，]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[。]{style="font-family:宋体"}[PMF]{lang="EN-US"}[协商过程中，客户端关联报文中]{style="font-family:宋体"}[RSN capability]{lang="EN-US"}[携带的]{style="font-family:宋体"}[MFPC/MFPR]{lang="EN-US"}[两位与]{style="font-family:宋体"}[BSS]{lang="EN-US"}[的]{style="font-family:宋体"}[PMF status]{lang="EN-US"}[不匹配，导致]{style="font-family:宋体"}[PMF]{lang="EN-US"}[协商失败。]{style="font-family:宋体"}

[[\[MAC: *UserMAC*, ]{lang="EN-US"}[APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID*\] PMF negotiation failed: PMF is disabled in the BSS.]{lang="EN-US"}]{#struct_0_59269_x7909_1791269935}

[[用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_59269_x7909_781139834}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[ ]{lang="EN-US"}[，]{style="font-family:宋体"}[APID]{lang="EN-US"}[为]{style="font-family:宋体"}*[APID]{lang="EN-US"}*[，]{style="font-family:宋体"}[RadioID]{lang="EN-US"}[为]{style="font-family:宋体"}*[RadioID]{lang="EN-US"}*[，]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[。]{style="font-family:宋体"}[BSS]{lang="EN-US"}[的]{style="font-family:宋体"}[PMF]{lang="EN-US"}[开关为关闭状态，客户端关联报文中携带的]{style="font-family:宋体"}[MFPR]{lang="EN-US"}[位为]{style="font-family:宋体"}[1]{lang="EN-US"}[，即要求]{style="font-family:宋体"}[PMF]{lang="EN-US"}[能力。此时]{style="font-family:宋体"}[PMF]{lang="EN-US"}[协商失败。]{style="font-family:宋体"}

[[\[MAC: *UserMAC*, ]{lang="EN-US"}[APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID*\] Failed to send (re)association response.]{lang="EN-US"}]{#struct_0_59269_x7909_x937613420}

[[用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_59269_x7909_628470521}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[APID]{lang="EN-US"}[为]{style="font-family:宋体"}*[APID]{lang="EN-US"}*[，]{style="font-family:宋体"}[RadioID]{lang="EN-US"}[为]{style="font-family:宋体"}*[RadioID]{lang="EN-US"}*[，]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[。发送（重）关联响应失败。]{style="font-family:宋体"}

[[\[MAC: *UserMAC*, APID: ]{lang="EN-US"}*[APID]{lang="EN-US"}*[, Radio ID: ]{lang="EN-US"}*[RadioID]{lang="EN-US"}*[, BSSID: ]{lang="EN-US"}*[BSSID]{lang="EN-US"}*[\] Failed to negotiate the group management cipher suite: Unmatched group management cipher suite in RSN IE.]{lang="EN-US"}]{#struct_0_59269_x7909_x1519345684}

[[用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_59269_x7909_x2100412834}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[APID]{lang="EN-US"}[为]{style="font-family:宋体"}*[APID]{lang="EN-US"}*[，]{style="font-family:宋体"}[RadioID]{lang="EN-US"}[为]{style="font-family:宋体"}*[RadioID]{lang="EN-US"}*[，]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，由于]{style="font-family:宋体"}[RSN IE]{lang="EN-US"}[中的组加密套件不匹配，协商组加密套件失败。]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging wlan usersec event]{lang="EN-US"}]{#struct_0_59269_x7909_x1519428583}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x779721597}[[字段]{style="font-family:黑体"}]{#struct_0_59269_x7909_x709029161}

[[描述]{style="font-family:黑体"}]{#struct_0_59269_x7909_669860479}

[[Started processing the shared-key authentication frame: Transmission number=*TransNum*.]{lang="EN-US"}]{#struct_0_59269_x7909_x789902236}

[[开始处理]{style="font-family:宋体"}[shared-key]{lang="EN-US"}]{#struct_0_59269_x7909_x1519363047}[认证报文，且传输序列号为]{style="font-family:宋体"}*[TransNum]{lang="EN-US"}*[. ]{lang="EN-US"}

[[Filled challenge IE successfully.]{lang="EN-US"}]{#struct_0_59269_x7909_626335874}

[[填充挑战]{style="font-family:宋体"}[IE]{lang="EN-US"}]{#struct_0_59269_x7909_1489408208}[成功]{style="font-family:宋体"}

[[Processed the 1st shared-key authentication frame successfully.]{lang="EN-US"}]{#struct_0_59269_x7909_x359607786}

[[处理第]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_59269_x7909_1678819990}[条]{style="font-family:宋体"}[shared-key]{lang="EN-US"}[认证报文成功]{style="font-family:宋体"}

[[Processed the 3rd shared-key authentication frame successfully.]{lang="EN-US"}]{#struct_0_59269_x7909_1665604244}

[[处理第]{style="font-family:宋体"}[3]{lang="EN-US"}]{#struct_0_59269_x7909_x2088360463}[条]{style="font-family:宋体"}[shared-key]{lang="EN-US"}[认证报文成功]{style="font-family:宋体"}

[[Started user authentication.]{lang="EN-US"}]{#struct_0_59269_x7909_x1188540104}

[[开始用户认证]{style="font-family:宋体"}]{#struct_0_59269_x7909_448305673}

[[Started L3 authentication.]{lang="EN-US"}]{#struct_0_59269_x7909_669860480}

[[开始三层认证]{style="font-family:宋体"}]{#struct_0_59269_x7909_x452195219}

[[Started L2 authentication.]{lang="EN-US"}]{#struct_0_59269_x7909_x219763968}

[[开始二层认证]{style="font-family:宋体"}]{#struct_0_59269_x7909_x1903594259}

[[Started key negotiation: Key negotiation status= *KeyNegoStatus*, security mode=*SecMode*.]{lang="EN-US"}]{#struct_0_59269_x7909_x1066997983}

[[为]{style="font-family:宋体"}*[KeyNegoStatus]{lang="EN-US"}*]{#struct_0_59269_x7909_x184343495}[开始密钥协商，且安全模式为]{style="font-family:宋体"}*[SecMode]{lang="EN-US"}*

[*[SecMode]{lang="EN-US"}*]{#struct_0_59269_x7909_361484279}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_59269_x7909_x1865412099}[：]{style="font-family:KaiTi_GB2312"}[WPA ]{lang="EN-US"}[，]{style="font-family:KaiTi_GB2312"}[Wi-Fi protected Access Wi-Fi]{lang="EN-US"}[防护访问]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_59269_x7909_x598910593}[：]{style="font-family:KaiTi_GB2312"}[RSN ]{lang="EN-US"}[，]{style="font-family:KaiTi_GB2312"}[Robust Security Network ]{lang="EN-US"}[固安网络]{style="font-family:KaiTi_GB2312"}

[*[KeyNegoStatus]{lang="EN-US"}*]{#struct_0_59269_x7909_669860481}[取值取下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_59269_x7909_x452195220}[：]{style="font-family:KaiTi_GB2312"}[Normal]{lang="EN-US"}[，正常上线]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_59269_x7909_x220353795}[：]{style="font-family:KaiTi_GB2312"}[Reauth]{lang="EN-US"}[，重认证]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_59269_x7909_x193044783}[：]{style="font-family:KaiTi_GB2312"}[Request]{lang="EN-US"}[，请求]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_59269_x7909_220329893}[：]{style="font-family:KaiTi_GB2312"}[Rekey]{lang="EN-US"}[，密钥更新]{style="font-family:KaiTi_GB2312"}

[[Started GTK negotiation: Key negotiation status= *KeyNegoStatus*, security mode=*SecMode*.]{lang="EN-US"}]{#struct_0_59269_x7909_1128512510}

[[为]{style="font-family:宋体"}*[KeyNegoStatus]{lang="EN-US"}*]{#struct_0_59269_x7909_x1200677772}[开始组播密钥协商，且安全模式为]{style="font-family:宋体"}*[SecMode]{lang="EN-US"}*

[*[SecMode]{lang="EN-US"}*]{#struct_0_59269_x7909_1386013169}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_59269_x7909_1859338872}[：]{style="font-family:KaiTi_GB2312"}[WPA ]{lang="EN-US"}[，]{style="font-family:KaiTi_GB2312"}[Wi-Fi protected Access Wi-Fi]{lang="EN-US"}[防护访问]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_59269_x7909_467257867}[：]{style="font-family:KaiTi_GB2312"}[RSN ]{lang="EN-US"}[，]{style="font-family:KaiTi_GB2312"}[Robust Security Network ]{lang="EN-US"}[固安网络]{style="font-family:KaiTi_GB2312"}

[*[KeyNegoStatus]{lang="EN-US"}*]{#struct_0_59269_x7909_x975471787}[取值取下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_59269_x7909_1890553324}[：]{style="font-family:KaiTi_GB2312"}[Normal]{lang="EN-US"}[，正常上线]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_59269_x7909_1870789175}[：]{style="font-family:KaiTi_GB2312"}[Reauth]{lang="EN-US"}[，重认证]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_59269_x7909_x321971398}[：]{style="font-family:KaiTi_GB2312"}[Request]{lang="EN-US"}[，请求]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_59269_x7909_373716577}[：]{style="font-family:KaiTi_GB2312"}[Rekey]{lang="EN-US"}[，密钥更新]{style="font-family:KaiTi_GB2312"}

[[Started processing L2 authentication: Result=*L2AuthResult*, Authentication status=*AuthenticationStatus.*]{lang="EN-US"}]{#struct_0_59269_x7909_1859338873}

[[开始处理]{style="font-family:宋体"}*[ReasonStatus]{lang="EN-US"}*]{#struct_0_59269_x7909_467323403}[二层认证的结果]{style="font-family:宋体"}*[L2AuthResult]{lang="EN-US"}*

[*[L2AuthResult]{lang="EN-US"}*]{#struct_0_59269_x7909_x1430916434}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_59269_x7909_x1037386690}[：]{style="font-family:KaiTi_GB2312"}[success]{lang="EN-US"}[，成功]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_59269_x7909_x1431445876}[：]{style="font-family:KaiTi_GB2312"}[failed-offline]{lang="EN-US"}[，失败下线]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_59269_x7909_1800843858}[：]{style="font-family:KaiTi_GB2312"}[failed-online]{lang="EN-US"}[，失败不下线]{style="font-family:KaiTi_GB2312"}

[*[AuthenticationStatus]{lang="EN-US"}*]{#struct_0_59269_x7909_x20337078}[取值如下：]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_59269_x7909_1859338874}[：]{style="font-family:KaiTi_GB2312"}[Normal]{lang="EN-US"}[，正常上线]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_59269_x7909_467651083}[：]{style="font-family:KaiTi_GB2312"}[Reauth]{lang="EN-US"}[，重认证]{style="font-family:KaiTi_GB2312"}

[[Started processing L3 authentication: Result=*L3AuthResult.*]{lang="EN-US"}]{#struct_0_59269_x7909_x1243668439}

[[开始处理三层认证结果]{style="font-family:宋体"}*[L3AuthResult]{lang="EN-US"}*]{#struct_0_59269_x7909_x1637495501}

[*[L3AuthResult]{lang="EN-US"}*]{#struct_0_59269_x7909_x350540205}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_59269_x7909_x532549014}[：]{style="font-family:KaiTi_GB2312"}[success]{lang="EN-US"}[，成功]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_59269_x7909_x2115038545}[：]{style="font-family:KaiTi_GB2312"}[ failed]{lang="EN-US"}[，失败]{style="font-family:KaiTi_GB2312"}

[[Started processing L2 authorization: VLAN ID=*VLANID*.]{lang="EN-US"}]{#struct_0_59269_x7909_1859338875}

[[开始处理]{style="font-family:宋体"}]{#struct_0_59269_x7909_467716619}[授权结果：]{style="font-family:宋体"}[VLANID=]{lang="EN-US"}*[ VLANID.]{lang="EN-US"}*

[[Started processing key negotiation: Result=*KeyNegoResult.* ]{lang="EN-US"}]{#struct_0_59269_x7909_x2064721075}

[[开始处理密钥协商成功的结果]{style="font-family:宋体"}*[KeyNegoResult]{lang="EN-US"}*]{#struct_0_59269_x7909_x593779353}

[*[KeyNegoResult]{lang="EN-US"}*]{#struct_0_59269_x7909_x1930425129}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[success]{lang="EN-US"}]{#struct_0_59269_x7909_1859338876}[：成功]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[discard packet]{lang="EN-US"}]{#struct_0_59269_x7909_467520011}[：丢弃报文]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[failed]{lang="EN-US"}]{#struct_0_59269_x7909_x1538908092}[：失败]{style="font-family:KaiTi_GB2312"}

[[Finished user authentication: Result=*UserAuthResult*]{lang="EN-US"}]{#struct_0_59269_x7909_x1519133720}

[[用户认证结束，认证结果]{style="font-family:宋体"}*[UserAuthResult]{lang="EN-US"}*]{#struct_0_59269_x7909_1482150857}

[*[UserAuthResult]{lang="EN-US"}*]{#struct_0_59269_x7909_468285272}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[success]{lang="EN-US"}]{#struct_0_59269_x7909_1859338877}[：成功]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[failed with reasoncode *ReasonCode*]{lang="EN-US"}]{#struct_0_59269_x7909_467585547}[：失败，原因为]{style="font-family:KaiTi_GB2312"}*[ReasonCode]{lang="EN-US"}*

[[AP *APID* received a *MsgType* message: CMD=*CMDValue*, length=*Len*.]{lang="EN-US"}]{#struct_0_59269_x7909_1171946601}

[[AP *APID*]{lang="EN-US"}]{#struct_0_59269_x7909_x711725182}[接收到一个]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[类型消息，且]{style="font-family:宋体"}[CMD]{lang="EN-US"}[的值为]{style="font-family:宋体"}*[CMDValue]{lang="EN-US"}*[，消息长度为]{style="font-family:宋体"}*[Len]{lang="EN-US"}*

[*[MsgType]{lang="EN-US"}*]{#struct_0_59269_x7909_x1841876840}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[up]{lang="EN-US"}]{#struct_0_59269_x7909_1859338878}[：上报的]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[down]{lang="EN-US"}]{#struct_0_59269_x7909_467913227}[：下发的]{style="font-family:KaiTi_GB2312"}

[[Processed *MsgType* successfully.]{lang="EN-US"}]{#struct_0_59269_x7909_x1077737257}

[[处理]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*]{#struct_0_59269_x7909_x1078668217}[类型报文成功]{style="font-family:宋体"}

[*[MsgType]{lang="EN-US"}*]{#struct_0_59269_x7909_x539601945}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4-way handshake message 2]{lang="EN-US"}]{#struct_0_59269_x7909_1859338879}[：四次握手]{style="font-family:KaiTi_GB2312"}[message 2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4-way handshake message 4]{lang="EN-US"}]{#struct_0_59269_x7909_467978763}[：四次握手]{style="font-family:KaiTi_GB2312"}[message 4]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[group handshake message 2]{lang="EN-US"}]{#struct_0_59269_x7909_2025482094}[：组播握手]{style="font-family:KaiTi_GB2312"}[message 2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4-way handshake request]{lang="EN-US"}]{#struct_0_59269_x7909_1637552402}[：四次握手请求]{style="font-family:KaiTi_GB2312"}

[[Times of resending the *MsgType* reached the limit: Maximum resending times=*MaxResndTimes*.]{lang="EN-US"}]{#struct_0_59269_x7909_1859338880}

[[重发]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*]{#struct_0_59269_x7909_467388932}[类型报文的次数达到最大值]{style="font-family:宋体"}*[MaxResndTimes]{lang="EN-US"}*

[*[MsgType]{lang="EN-US"}*]{#struct_0_59269_x7909_x996473558}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4-way handshake message 1]{lang="EN-US"}]{#struct_0_59269_x7909_x682309545}[：四次握手]{style="font-family:KaiTi_GB2312"}[message 1]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4-way handshake message 3]{lang="EN-US"}]{#struct_0_59269_x7909_1859338881}[：四次握手]{style="font-family:KaiTi_GB2312"}[message 3]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[group handshake message 1]{lang="EN-US"}]{#struct_0_59269_x7909_467454468}[：组播握手]{style="font-family:KaiTi_GB2312"}[message 1]{lang="EN-US"}

[[Started packet-based GTK rekey for BSS *BSSID*.]{lang="EN-US"}]{#struct_0_59269_x7909_x1562643830}

[[开始为]{style="font-family:宋体"}[BSS ]{lang="EN-US"}*[BSSID]{lang="EN-US"}*]{#struct_0_59269_x7909_1874663583}[处理基于报文更新]{style="font-family:宋体"}[GTK]{lang="EN-US"}

[[Started stationoff-based GTK rekey for BSS *BSSID*: Client MAC address=*StaMac*.]{lang="EN-US"}]{#struct_0_59269_x7909_x1825986200}

[[开始为]{style="font-family:宋体"}[BSS]{lang="EN-US"}*[ BSSID]{lang="EN-US"}*]{#struct_0_59269_x7909_x96976264}[处理基于客户端]{style="font-family:宋体"} *[StaMac]{lang="EN-US"}*[下线更新]{style="font-family:宋体"}[GTK]{lang="EN-US"}

[[Updated GTK for BSS *BSSID*.]{lang="EN-US"}]{#struct_0_59269_x7909_1857948313}

[[BSS]{lang="EN-US"}*[ BSSID]{lang="EN-US"}*]{#struct_0_59269_x7909_x94844733}[更新]{style="font-family:宋体"}[GTK]{lang="EN-US"}[成功]{style="font-family:宋体"}

[[Filled security information in the add mobile message successfully.]{lang="EN-US"}]{#struct_0_59269_x7909_1768278600}

[[向]{style="font-family:宋体"}[add mobile]{lang="EN-US"}]{#struct_0_59269_x7909_x96976263}[消息中填充安全信息成功]{style="font-family:宋体"}

[[BSS *BSSID* filled security information in the *MsgType* message successfully.]{lang="EN-US"}]{#struct_0_59269_x7909_1857948320}

[[BSS *BSSID*]{lang="EN-US"}]{#struct_0_59269_x7909_x94648128}[向]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[类型消息中填充安全信息成功]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[取值如下]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add WLAN]{lang="EN-US"}]{#struct_0_59269_x7909_x1184397839}[：加入]{style="font-family:KaiTi_GB2312"}[WLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[update WLAN]{lang="EN-US"}]{#struct_0_59269_x7909_x96976262}[：更新]{style="font-family:KaiTi_GB2312"}[WLAN]{lang="EN-US"}

[[Processed security information in the add mobile message successfully.]{lang="EN-US"}]{#struct_0_59269_x7909_1857948319}

[[处理]{style="font-family:宋体"}[add mobile]{lang="EN-US"}]{#struct_0_59269_x7909_x95237949}[消息中的安全信息成功]{style="font-family:宋体"}

[[BSS *BSSID* processed security information in the *MsgType* message successfully.]{lang="EN-US"}]{#struct_0_59269_x7909_1901601390}

[[BSS *BSSID* ]{lang="EN-US"}]{#struct_0_59269_x7909_x96976261}[处理]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[类型消息中的安全信息成功]{style="font-family:宋体"}*[MsgType ]{lang="EN-US"}*[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add WLAN]{lang="EN-US"}]{#struct_0_59269_x7909_1857948318}[：加入]{style="font-family:KaiTi_GB2312"}[WLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[update WLAN]{lang="EN-US"}]{#struct_0_59269_x7909_x95172413}[：更新]{style="font-family:KaiTi_GB2312"}[WLAN]{lang="EN-US"}

[[Filled security info about clients in the driver successfully.]{lang="EN-US"}]{#struct_0_59269_x7909_901718083}

[[客户端填充安全驱动信息成功]{style="font-family:宋体"}]{#struct_0_59269_x7909_x96976260}

[[Filled security info about BSS *BSSID* in the driver successfully.]{lang="EN-US"}]{#struct_0_59269_x7909_1857948317}

[[BSS *BSSID* ]{lang="EN-US"}]{#struct_0_59269_x7909_x95106877}[填充安全驱动信息成功]{style="font-family:宋体"}

[[Filled security info about clients in the kernel successfully.]{lang="EN-US"}]{#struct_0_59269_x7909_x1102408070}

[[填充客户端安全信息到内核成功]{style="font-family:宋体"}]{#struct_0_59269_x7909_x96976259}

[[Filled security info about BSS *BSSID* in the kernel successfully.]{lang="EN-US"}]{#struct_0_59269_x7909_x863040858}

[[填充]{style="font-family:宋体"}[BSS]{lang="EN-US"}]{#struct_0_59269_x7909_x1381621669}[安全信息到内核成功]{style="font-family:宋体"}

[[The clear-type client processed the (re)association request without security IE successfully.]{lang="EN-US"}]{#struct_0_59269_x7909_x96976258}

[[clear]{lang="EN-US"}]{#struct_0_59269_x7909_x863040859}[模式下的客户端处理不带安全]{style="font-family:宋体"}[IE]{lang="EN-US"}[的]{style="font-family:宋体"}[(]{lang="EN-US"}[重]{style="font-family:宋体"}[)]{lang="EN-US"}[关联请求成功]{style="font-family:宋体"}

[[The shared-key client processed the (re)association request without security IE successfully.]{lang="EN-US"}]{#struct_0_59269_x7909_x1381687205}

[[shared-key]{lang="EN-US"}]{#struct_0_59269_x7909_x96976257}[模式下的客户端处理不带安全]{style="font-family:宋体"}[IE]{lang="EN-US"}[的]{style="font-family:宋体"}[(]{lang="EN-US"}[重]{style="font-family:宋体"}[)]{lang="EN-US"}[关联请求成功]{style="font-family:宋体"}

[[Selected unicast cipher suite *PCipherSuite* for the client.]{lang="EN-US"}]{#struct_0_59269_x7909_x863040868}

[[客户端选择单播加密套件]{style="font-family:宋体"}*[PCipherSuite]{lang="EN-US"}*]{#struct_0_59269_x7909_x1381621666}[成功]{style="font-family:宋体"}

[*[PCipherSuite]{lang="EN-US"}*]{#struct_0_59269_x7909_x1281773945}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_59269_x7909_x96976256}[：]{style="font-family:KaiTi_GB2312"}[TKIP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_59269_x7909_x863040869}[：]{style="font-family:KaiTi_GB2312"}[CCMP]{lang="EN-US"}

[[Selected AKM mode *AkmMode* for the client.]{lang="EN-US"}]{#struct_0_59269_x7909_x1381687202}

[[客户端选择]{style="font-family:宋体"}[AKM]{lang="EN-US"}]{#struct_0_59269_x7909_x96976255}[模式]{style="font-family:宋体"}*[AkmMode]{lang="EN-US"}*[成功]{style="font-family:宋体"}

[*[AkmMode]{lang="EN-US"}*]{#struct_0_59269_x7909_x863040870}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_59269_x7909_x1381097379}[：]{style="font-family:KaiTi_GB2312"}[DOT1X]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_59269_x7909_1716779658}[：]{style="font-family:KaiTi_GB2312"}[PSK]{lang="EN-US"}

[[Processed the (re)association request with RSN IE successfully.]{lang="EN-US"}]{#struct_0_59269_x7909_x2053291400}

[[处理带]{style="font-family:宋体"}[RSN IE]{lang="EN-US"}]{#struct_0_59269_x7909_433619300}[的关联请求成功]{style="font-family:宋体"}

[[Processed the (re)association request with WPA IE successfully.]{lang="EN-US"}]{#struct_0_59269_x7909_x661687214}

[[处理带]{style="font-family:宋体"}[WPA IE]{lang="EN-US"}]{#struct_0_59269_x7909_x2053291399}[的关联请求成功]{style="font-family:宋体"}

[[Processed (re)association request with security IE successfully. The client is not allowed to go online: TKIP countermeasure is active.]{lang="EN-US"}]{#struct_0_59269_x7909_1642883056}

[[处理带安全]{style="font-family:宋体"}[IE]{lang="EN-US"}]{#struct_0_59269_x7909_x2053291398}[的关联请求成功，但是由于]{style="font-family:宋体"}[TKIP]{lang="EN-US"}[反制处于激活状态所以不允许客户端上线。]{style="font-family:宋体"}

[[Got the security info for roaming clients.]{lang="EN-US"}]{#struct_0_59269_x7909_76799115}

[[获取漫游用户迁移安全信息成功]{style="font-family:宋体"}]{#struct_0_59269_x7909_144355314}

[[Recovered the security info (length: *Lengh*) for roaming clients.]{lang="EN-US"}]{#struct_0_59269_x7909_x2053291397}

[[恢复漫游用户迁移安全信息]{style="font-family:宋体"}[(]{lang="EN-US"}]{#struct_0_59269_x7909_x1489284826}[长度：消息长度]{style="font-family:宋体"}[)]{lang="EN-US"}[成功]{style="font-family:宋体"}

[[BSS *BSSID* inherited security information from service template *STName*.]{lang="EN-US"}]{#struct_0_59269_x7909_46625286}

[[BSS]{lang="EN-US"}*[ BSSID]{lang="EN-US"}*]{#struct_0_59269_x7909_2016452247}[从服务模板]{style="font-family:宋体"}*[STName]{lang="EN-US"}*[继承安全信息成功]{style="font-family:宋体"}

[[Initialized security information in BSS *BSSID*.]{lang="EN-US"}]{#struct_0_59269_x7909_x2053291396}

[[初始化]{style="font-family:宋体"}[BSS]{lang="EN-US"}*[ BSSID]{lang="EN-US"}*]{#struct_0_59269_x7909_1239598529}[中安全信息成功]{style="font-family:宋体"}

[[Deleted security information in BSS *BSSID*.]{lang="EN-US"}]{#struct_0_59269_x7909_x246957746}

[[删除]{style="font-family:宋体"}[BSS]{lang="EN-US"}*[ BSSID]{lang="EN-US"}*]{#struct_0_59269_x7909_x2053291395}[中安全信息成功]{style="font-family:宋体"}

[[Initialized security information in the client.]{lang="EN-US"}]{#struct_0_59269_x7909_x326485412}

[[初始化客户端中的安全信息成功]{style="font-family:宋体"}]{#struct_0_59269_x7909_773825414}

[[Deleted security information in the client.]{lang="EN-US"}]{#struct_0_59269_x7909_x2053291394}

[[删除客户端中的安全信息成功]{style="font-family:宋体"}]{#struct_0_59269_x7909_x1892569353}

[[Initialized security information in service template *STName*.]{lang="EN-US"}]{#struct_0_59269_x7909_556846779}

[[初始化服务模板]{style="font-family:宋体"}*[STName]{lang="EN-US"}*]{#struct_0_59269_x7909_x2053291393}[中的安全信息成功]{style="font-family:宋体"}

[[Deleted security information in service template *STName*.]{lang="EN-US"}]{#struct_0_59269_x7909_836314002}

[[删除服务模板]{style="font-family:宋体"}*[STName]{lang="EN-US"}*]{#struct_0_59269_x7909_x687641226}[中的安全信息成功]{style="font-family:宋体"}

[[Deactivated security information in the client.]{lang="EN-US"}]{#struct_0_59269_x7909_x2053291392}

[[去激活客户端中的安全信息成功]{style="font-family:宋体"}]{#struct_0_59269_x7909_x729769939}

[[Initialized ]{lang="EN-US"}[PMF information in service template *STName*.]{lang="EN-US"}]{#struct_0_59269_x7909_x534394429}

[[初始化服务模板]{style="font-family:宋体"}*[STName]{lang="EN-US"}*]{#struct_0_59269_x7909_1744150232}[中]{style="font-family:宋体"}[PMF]{lang="EN-US"}[信息成功。]{style="font-family:宋体"}

[[Deleted ]{lang="EN-US"}[PMF information in service template *STName*.]{lang="EN-US"}]{#struct_0_59269_x7909_x1607908425}

[[删除服务模板]{style="font-family:宋体"}*[STName]{lang="EN-US"}*]{#struct_0_59269_x7909_x984733123}[中]{style="font-family:宋体"}[PMF]{lang="EN-US"}[信息成功。]{style="font-family:宋体"}

[[\[]{lang="EN-US"}[APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID*\] Failed to get PMF info in BSS: PMF info does not exist in the BSS.]{lang="EN-US"}]{#struct_0_59269_x7909_x1849044876}

[[APID]{lang="EN-US"}]{#struct_0_59269_x7909_x554146346}[为]{style="font-family:宋体"}*[APID]{lang="EN-US"}*[，]{style="font-family:宋体"}[RadioID]{lang="EN-US"}[为]{style="font-family:宋体"}*[RadioID]{lang="EN-US"}*[，]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，由于]{style="font-family:宋体"}[BSS]{lang="EN-US"}[中]{style="font-family:宋体"}[pmf]{lang="EN-US"}[信息不存在，获取]{style="font-family:宋体"}[pmf]{lang="EN-US"}[信息失败]{style="font-family:宋体"}

[[\[]{lang="EN-US"}[APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID*\] Initialized PMF information in BSS.]{lang="EN-US"}]{#struct_0_59269_x7909_1387854336}

[[APID]{lang="EN-US"}]{#struct_0_59269_x7909_x1444329257}[为]{style="font-family:宋体"}*[APID]{lang="EN-US"}*[，]{style="font-family:宋体"}[RadioID]{lang="EN-US"}[为]{style="font-family:宋体"}*[RadioID]{lang="EN-US"}*[，]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，]{style="font-family:宋体"}[BSS]{lang="EN-US"}[中的]{style="font-family:宋体"}[PMF]{lang="EN-US"}[信息初始化完成。]{style="font-family:宋体"}

[[Inherited ]{lang="EN-US"}[PMF information for BSS *BSSID* from service template *STName*.]{lang="EN-US"}]{#struct_0_59269_x7909_x1341029019}

[[BSS]{lang="EN-US"}*[ BSSID]{lang="EN-US"}*]{#struct_0_59269_x7909_x1800432358}[从服务模板]{style="font-family:宋体"}*[STName]{lang="EN-US"}*[继承]{style="font-family:宋体"}[PMF]{lang="EN-US"}[信息成功。]{style="font-family:宋体"}

[[\[]{lang="EN-US"}[APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID*\] Deleted PMF information in BSS.]{lang="EN-US"}]{#struct_0_59269_x7909_225054922}

[[APID]{lang="EN-US"}]{#struct_0_59269_x7909_1579305198}[为]{style="font-family:宋体"}*[APID]{lang="EN-US"}*[，]{style="font-family:宋体"}[RadioID]{lang="EN-US"}[为]{style="font-family:宋体"}*[RadioID]{lang="EN-US"}*[，]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，]{style="font-family:宋体"}[ BSS]{lang="EN-US"}[中的]{style="font-family:宋体"}[PMF]{lang="EN-US"}[信息删除完成。]{style="font-family:宋体"}

[[\[MAC: *UserMAC*, ]{lang="EN-US"}[APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID*\] Initialized PMF information in client.]{lang="EN-US"}]{#struct_0_59269_x7909_1791138863}

[[用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_59269_x7909_1562555323}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[ ]{lang="EN-US"}[，]{style="font-family:宋体"}[APID]{lang="EN-US"}[为]{style="font-family:宋体"}*[APID]{lang="EN-US"}*[，]{style="font-family:宋体"}[RadioID]{lang="EN-US"}[为]{style="font-family:宋体"}*[RadioID]{lang="EN-US"}*[，]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，客户端中的]{style="font-family:宋体"}[PMF]{lang="EN-US"}[信息初始化完成。]{style="font-family:宋体"}

[[\[MAC: *UserMAC*, ]{lang="EN-US"}[APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID*\] Deleted PMF information in client.]{lang="EN-US"}]{#struct_0_59269_x7909_1862965809}

[[用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_59269_x7909_x937744492}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[ ]{lang="EN-US"}[，]{style="font-family:宋体"}[APID]{lang="EN-US"}[为]{style="font-family:宋体"}*[APID]{lang="EN-US"}*[，]{style="font-family:宋体"}[RadioID]{lang="EN-US"}[为]{style="font-family:宋体"}*[RadioID]{lang="EN-US"}*[，]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，客户端中的]{style="font-family:宋体"}[PMF]{lang="EN-US"}[信息删除完成。]{style="font-family:宋体"}

[[\[MAC: *UserMAC*, ]{lang="EN-US"}[APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID*\] Failed to get PMF info in client: PMF info in the client does not exist.]{lang="EN-US"}]{#struct_0_59269_x7909_x747761581}

[[用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_59269_x7909_628339449}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[ ]{lang="EN-US"}[，]{style="font-family:宋体"}[APID]{lang="EN-US"}[为]{style="font-family:宋体"}*[APID]{lang="EN-US"}*[，]{style="font-family:宋体"}[RadioID]{lang="EN-US"}[为]{style="font-family:宋体"}*[RadioID]{lang="EN-US"}*[，]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，客户端中不存在]{style="font-family:宋体"}[PMF]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\[MAC: *UserMAC*, ]{lang="EN-US"}[APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID*\] Sent SA query request.]{lang="EN-US"}]{#struct_0_59269_x7909_1694837693}

[[用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_59269_x7909_x2100543906}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[ ]{lang="EN-US"}[，]{style="font-family:宋体"}[APID]{lang="EN-US"}[为]{style="font-family:宋体"}*[APID]{lang="EN-US"}*[，]{style="font-family:宋体"}[RadioID]{lang="EN-US"}[为]{style="font-family:宋体"}*[RadioID]{lang="EN-US"}*[，]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，]{style="font-family:宋体"} [发送安全关联询问请求报文成功。]{style="font-family:宋体"}

[[\[MAC: *UserMAC*, ]{lang="EN-US"}[APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID*\] Sent SA query response.]{lang="EN-US"}]{#struct_0_59269_x7909_488484707}

[[用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_59269_x7909_x534459965}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[ ]{lang="EN-US"}[，]{style="font-family:宋体"}[APID]{lang="EN-US"}[为]{style="font-family:宋体"}*[APID]{lang="EN-US"}*[，]{style="font-family:宋体"}[RadioID]{lang="EN-US"}[为]{style="font-family:宋体"}*[RadioID]{lang="EN-US"}*[，]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，]{style="font-family:宋体"} [发送安全关联询问应答报文成功。]{style="font-family:宋体"}

[[\[MAC: *UserMAC*, ]{lang="EN-US"}[APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID*\] Sent (re)association response.]{lang="EN-US"}]{#struct_0_59269_x7909_x1044376875}

[[用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_59269_x7909_1744084696}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[ ]{lang="EN-US"}[，]{style="font-family:宋体"}[APID]{lang="EN-US"}[为]{style="font-family:宋体"}*[APID]{lang="EN-US"}*[，]{style="font-family:宋体"}[RadioID]{lang="EN-US"}[为]{style="font-family:宋体"}*[RadioID]{lang="EN-US"}*[，]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[。发送（重）关联响应成功。]{style="font-family:宋体"}

[[\[MAC: *UserMAC*, ]{lang="EN-US"}[APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID*\] Discarded (re)association request: AP is not prepared for association.]{lang="EN-US"}]{#struct_0_59269_x7909_1156346210}

[[用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_59269_x7909_x984798659}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[ ]{lang="EN-US"}[，]{style="font-family:宋体"}[APID]{lang="EN-US"}[为]{style="font-family:宋体"}*[APID]{lang="EN-US"}*[，]{style="font-family:宋体"}[RadioID]{lang="EN-US"}[为]{style="font-family:宋体"}*[RadioID]{lang="EN-US"}*[，]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[。]{style="font-family:宋体"}[AP]{lang="EN-US"}[未准备好处理与客户端的关联，所以丢弃（重）关联请求帧。]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging wlan usersec fsm]{lang="EN-US"}]{#struct_0_59269_x7909_x1319232790}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x757083759}[[字段]{style="font-family:黑体"}]{#struct_0_59269_x7909_1520493823}

[[描述]{style="font-family:黑体"}]{#struct_0_59269_x7909_x2053291391}

[[4-way handshake FSM changed state from *State1* to *State2*.]{lang="EN-US"}]{#struct_0_59269_x7909_1999113416}

[[四次握手状态机切换，]{style="font-family:宋体"}*[State1]{lang="EN-US"}*[-\>*State2*]{lang="EN-US"}]{#struct_0_59269_x7909_1129904830}[。]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[State1]{lang="EN-US"}*]{#struct_0_59269_x7909_351625292}[取值如下：]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NULL]{lang="EN-US"}]{#struct_0_59269_x7909_716444460}[：未定义状态]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IDLE]{lang="EN-US"}]{#struct_0_59269_x7909_1629490126}[：空闲状态]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WAITMSG2]{lang="EN-US"}]{#struct_0_59269_x7909_x1426836643}[：发送完]{style="font-family:KaiTi_GB2312"}[message 1]{lang="EN-US"}[等待]{style="font-family:KaiTi_GB2312"}[message 2]{lang="EN-US"}[状态]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WAITMSG4]{lang="EN-US"}]{#struct_0_59269_x7909_1250703577}[：发送完]{style="font-family:KaiTi_GB2312"}[message 3]{lang="EN-US"}[等待]{style="font-family:KaiTi_GB2312"}[message 4]{lang="EN-US"}[状态]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4WAYDONE]{lang="EN-US"}]{#struct_0_59269_x7909_2028717798}[：四次握手完成状态]{style="font-family:KaiTi_GB2312"}

[*[State2]{lang="EN-US"}*]{#struct_0_59269_x7909_x966151524}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IDLE]{lang="EN-US"}]{#struct_0_59269_x7909_285360760}[：空闲状态]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WAITMSG2]{lang="EN-US"}]{#struct_0_59269_x7909_204269717}[：发送完]{style="font-family:KaiTi_GB2312"}[message 1]{lang="EN-US"}[等待]{style="font-family:KaiTi_GB2312"}[message 2]{lang="EN-US"}[状态]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WAITMSG4]{lang="EN-US"}]{#struct_0_59269_x7909_718532755}[：发送完]{style="font-family:KaiTi_GB2312"}[message 3]{lang="EN-US"}[等待]{style="font-family:KaiTi_GB2312"}[message 4]{lang="EN-US"}[状态]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4WAYDONE]{lang="EN-US"}]{#struct_0_59269_x7909_1142471521}[：四次握手完成状态]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DONE]{lang="EN-US"}]{#struct_0_59269_x7909_x1054951441}[：密钥协商完成状态]{style="font-family:KaiTi_GB2312"}

[[Group handshake FSM changed state from *State1* to *State2*.]{lang="EN-US"}]{#struct_0_59269_x7909_x1825379010}

[[组播握手状态机切换，]{style="font-family:宋体"}*[State1]{lang="EN-US"}*[-\>*State2*]{lang="EN-US"}]{#struct_0_59269_x7909_x1232569619}[。]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[State1]{lang="EN-US"}*]{#struct_0_59269_x7909_x1658925848}[取值如下：]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NULL]{lang="EN-US"}]{#struct_0_59269_x7909_x300045574}[：未定义状态]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GKHS_IDLE]{lang="EN-US"}]{#struct_0_59269_x7909_285360761}[：空闲状态]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GKHS_WAITMSG2]{lang="EN-US"}]{#struct_0_59269_x7909_204269718}[：发送完]{style="font-family:KaiTi_GB2312"}[message 1]{lang="EN-US"}[等待]{style="font-family:KaiTi_GB2312"}[message 2]{lang="EN-US"}[状态]{style="font-family:KaiTi_GB2312"}

[*[State2]{lang="EN-US"}*]{#struct_0_59269_x7909_718532744}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GKHS_IDLE]{lang="EN-US"}]{#struct_0_59269_x7909_x813843616}[：空闲状态]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GKHS_WAITMSG2]{lang="EN-US"}]{#struct_0_59269_x7909_x1210550961}[：发送完]{style="font-family:KaiTi_GB2312"}[message 1]{lang="EN-US"}[等待]{style="font-family:KaiTi_GB2312"}[message 2]{lang="EN-US"}[状态]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GKHS_DONE]{lang="EN-US"}]{#struct_0_59269_x7909_686763974}[：组播握手完成状态]{style="font-family:KaiTi_GB2312"}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging wlan usersec packet receive]{lang="EN-US"}]{#struct_0_59269_x7909_x421657376}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x758243829}[[字段]{style="font-family:黑体"}]{#struct_0_59269_x7909_x712995584}

[[描述]{style="font-family:黑体"}]{#struct_0_59269_x7909_1570189530}

[[Received a *MsgType*.]{lang="EN-US"}]{#struct_0_59269_x7909_x2118444171}

[[接收到]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*]{#struct_0_59269_x7909_285360762}[类型报文]{style="font-family:宋体"}

[*[MsgType]{lang="EN-US"}*]{#struct_0_59269_x7909_204269715}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4-way handshake message 2]{lang="EN-US"}]{#struct_0_59269_x7909_718532757}[：四次握手]{style="font-family:KaiTi_GB2312"}[message 2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4-way handshake message 4]{lang="EN-US"}]{#struct_0_59269_x7909_1142471519}[：四次握手]{style="font-family:KaiTi_GB2312"}[message 4]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[group handshake message 2]{lang="EN-US"}]{#struct_0_59269_x7909_x1054427156}[：组播握手]{style="font-family:KaiTi_GB2312"}[message 2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MIC failure report]{lang="EN-US"}]{#struct_0_59269_x7909_1385175553}[：]{style="font-family:KaiTi_GB2312"}[MIC]{lang="EN-US"}[错误报告]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4-way handshake request]{lang="EN-US"}]{#struct_0_59269_x7909_x2135572897}[：四次握手请求]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[group handshake request]{lang="EN-US"}]{#struct_0_59269_x7909_1160422805}[：组播握手请求]{style="font-family:KaiTi_GB2312"}

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging wlan usersec packet receive verbose]{lang="EN-US"}]{#struct_0_59269_x7909_x1964622722}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x755354167}[[字段]{style="font-family:黑体"}]{#struct_0_59269_x7909_x1582664778}

[[描述]{style="font-family:黑体"}]{#struct_0_59269_x7909_x1016317721}

[[Received an EAPOL-Key frame from client *StaMacAddr* (Length=*Length*)]{lang="EN-US"}]{#struct_0_59269_x7909_1263551020}

[*[Packet context]{lang="EN-US"}*]{#struct_0_59269_x7909_285360763}

[[接收到来自客户端]{style="font-family:宋体"} *[StaMacAddr]{lang="EN-US"}*]{#struct_0_59269_x7909_204269716}[的]{style="font-family:宋体"}[EAPOL-key]{lang="EN-US"}[报文]{style="font-family:宋体"}[(]{lang="EN-US"}[报文长度：]{style="font-family:宋体"}*[Length]{lang="EN-US"}*[)]{lang="EN-US"}

[*[Packet context]{lang="EN-US"}*]{#struct_0_59269_x7909_718532754}[：报文内容]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[debugging wlan usersec packet send]{lang="EN-US"}]{#struct_0_59269_x7909_1142471520}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x756488211}[[字段]{style="font-family:黑体"}]{#struct_0_59269_x7909_x1054885905}

[[描述]{style="font-family:黑体"}]{#struct_0_59269_x7909_1798960444}

[[Failed to send a *MsgType*.]{lang="EN-US"}]{#struct_0_59269_x7909_x1003006071}

[[发送]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*]{#struct_0_59269_x7909_1988635031}[类型报文失败]{style="font-family:宋体"}

[*[MsgType]{lang="EN-US"}*]{#struct_0_59269_x7909_166706740}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4-way handshake message 1]{lang="EN-US"}]{#struct_0_59269_x7909_934183944}[：四次握手]{style="font-family:KaiTi_GB2312"}[message 1]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4-way handshake message 3]{lang="EN-US"}]{#struct_0_59269_x7909_1632205789}[：四次握手]{style="font-family:KaiTi_GB2312"}[message 3]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[group handshake message 1]{lang="EN-US"}]{#struct_0_59269_x7909_285360764}[：组播握手]{style="font-family:KaiTi_GB2312"}[message 1]{lang="EN-US"}

[[Sent a *MsgType*.]{lang="EN-US"}]{#struct_0_59269_x7909_204269721}

[[发送]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*]{#struct_0_59269_x7909_x1237782383}[类型报文成功]{style="font-family:宋体"}

[*[MsgType]{lang="EN-US"}*]{#struct_0_59269_x7909_x1226928266}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4-way handshake message 1]{lang="EN-US"}]{#struct_0_59269_x7909_x902006495}[：四次握手]{style="font-family:KaiTi_GB2312"}[message 1]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4-way handshake message 3]{lang="EN-US"}]{#struct_0_59269_x7909_406444459}[：四次握手]{style="font-family:KaiTi_GB2312"}[message 3]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[group handshake message 1]{lang="EN-US"}]{#struct_0_59269_x7909_265294258}[：组播握手]{style="font-family:KaiTi_GB2312"}[message 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[debugging wlan usersec packet send verbose]{lang="EN-US"}]{#struct_0_59269_x7909_450113032}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x761580441}[[字段]{style="font-family:黑体"}]{#struct_0_59269_x7909_2080968327}

[[描述]{style="font-family:黑体"}]{#struct_0_59269_x7909_x699284274}

[[Sent an EAPOL-Key frame to client *StaMacAddr* (Length=*Length*)]{lang="EN-US"}]{#struct_0_59269_x7909_x835913751}

[*[Packet context]{lang="EN-US"}*]{#struct_0_59269_x7909_x460105840}

[[发送]{style="font-family:宋体"}[EAPOL-key]{lang="EN-US"}]{#struct_0_59269_x7909_285360765}[报文给客户端]{style="font-family:宋体"} *[StaMacAddr]{lang="EN-US"}*[ (]{lang="EN-US"}[报文长度：]{style="font-family:宋体"}*[Length]{lang="EN-US"}*[)]{lang="EN-US"}

[*[Packet context ]{lang="EN-US"}*]{#struct_0_59269_x7909_204269722}[：报文内容]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[debugging wlan usersec timer]{lang="EN-US"}]{#struct_0_59269_x7909_x1237782386}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x762886107}[[字段]{style="font-family:黑体"}]{#struct_0_59269_x7909_x823643739}

[[描述]{style="font-family:黑体"}]{#struct_0_59269_x7909_x1647288472}

[[Created timer *TimerId* for resending *MsgType*.]{lang="EN-US"}]{#struct_0_59269_x7909_x1025859130}

[[创建]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*]{#struct_0_59269_x7909_x1365250788}[类型报文重传定时器]{style="font-family:宋体"}*[TimerId]{lang="EN-US"}*[成功]{style="font-family:宋体"}

[*[MsgType]{lang="EN-US"}*]{#struct_0_59269_x7909_2063322644}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4-way handshake message 1]{lang="EN-US"}]{#struct_0_59269_x7909_1200435162}[：四次握手]{style="font-family:KaiTi_GB2312"}[message 1]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4-way handshake message 3]{lang="EN-US"}]{#struct_0_59269_x7909_x1882559893}[：四次握手]{style="font-family:KaiTi_GB2312"}[message 3]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[group handshake message 1]{lang="EN-US"}]{#struct_0_59269_x7909_285360766}[：组播握手]{style="font-family:KaiTi_GB2312"}[message 1]{lang="EN-US"}

[[Deleted timer *TimerId* for resending *MsgType*.]{lang="EN-US"}]{#struct_0_59269_x7909_204269719}

[[删除]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*]{#struct_0_59269_x7909_718532745}[类型报文重传定时器]{style="font-family:宋体"}*[TimerId]{lang="EN-US"}*

[*[MsgType]{lang="EN-US"}*]{#struct_0_59269_x7909_x813843615}[取值如下]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4-way handshake message 1]{lang="EN-US"}]{#struct_0_59269_x7909_x1210485425}[：四次握手]{style="font-family:KaiTi_GB2312"}[message 1]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4-way handshake message 3]{lang="EN-US"}]{#struct_0_59269_x7909_2061477170}[：四次握手]{style="font-family:KaiTi_GB2312"}[message 3]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[group handshake message 1]{lang="EN-US"}]{#struct_0_59269_x7909_x1039763445}[：组播握手]{style="font-family:KaiTi_GB2312"}[message 1]{lang="EN-US"}

[[Timer TimerId for resending *MsgType* expired.]{lang="EN-US"}]{#struct_0_59269_x7909_x682858525}

[*[MsgType]{lang="EN-US"}*]{#struct_0_59269_x7909_285360767}[类型报文重传定时器]{style="font-family:宋体"}*[TimerId]{lang="EN-US"}*[超时]{style="font-family:宋体"}

[*[MsgType]{lang="EN-US"}*]{#struct_0_59269_x7909_204269720}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4-way handshake message 1]{lang="EN-US"}]{#struct_0_59269_x7909_x1237782384}[：四次握手]{style="font-family:KaiTi_GB2312"}[message 1]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4-way handshake message 3]{lang="EN-US"}]{#struct_0_59269_x7909_339155675}[：四次握手]{style="font-family:KaiTi_GB2312"}[message 3]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[group handshake message 1]{lang="EN-US"}]{#struct_0_59269_x7909_x2105591357}[：组播握手]{style="font-family:KaiTi_GB2312"}[message 1]{lang="EN-US"}

[[Failed to create a timer for resending *MsgType*.]{lang="EN-US"}]{#struct_0_59269_x7909_1887348698}

[[创建]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*]{#struct_0_59269_x7909_x1713712458}[类型报文重传定时器失败]{style="font-family:宋体"}

[*[MsgType]{lang="EN-US"}*]{#struct_0_59269_x7909_x21869344}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4-way handshake message 1]{lang="EN-US"}]{#struct_0_59269_x7909_285360768}[：四次握手]{style="font-family:KaiTi_GB2312"}[message 1]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4-way handshake message 3]{lang="EN-US"}]{#struct_0_59269_x7909_204269709}[：四次握手]{style="font-family:KaiTi_GB2312"}[message 3]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[group handshake message 1]{lang="EN-US"}]{#struct_0_59269_x7909_x1620119415}[：组播握手]{style="font-family:KaiTi_GB2312"}[message 1]{lang="EN-US"}

[[Refreshed timer *TimerId* for resending *MsgType*.]{lang="EN-US"}]{#struct_0_59269_x7909_1728223927}

[[刷新]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*]{#struct_0_59269_x7909_x898723344}[类型报文重传定时器成功]{style="font-family:宋体"}

[*[MsgType]{lang="EN-US"}*]{#struct_0_59269_x7909_x1024800653}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4-way handshake message 1]{lang="EN-US"}]{#struct_0_59269_x7909_x1717234892}[：四次握手]{style="font-family:KaiTi_GB2312"}[message 1]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4-way handshake message 3]{lang="EN-US"}]{#struct_0_59269_x7909_2033052524}[：四次握手]{style="font-family:KaiTi_GB2312"}[message 3]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[group handshake message 1]{lang="EN-US"}]{#struct_0_59269_x7909_285360769}[：组播握手]{style="font-family:KaiTi_GB2312"}[message 1]{lang="EN-US"}

[[Failed to refresh timer *TimerId* for resending *MsgType*.]{lang="EN-US"}]{#struct_0_59269_x7909_204269710}

[[刷新]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*]{#struct_0_59269_x7909_718532752}[类型报文重传定时器失败]{style="font-family:宋体"}

[*[MsgType]{lang="EN-US"}*]{#struct_0_59269_x7909_1142471514}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4-way handshake message 1]{lang="EN-US"}]{#struct_0_59269_x7909_x1055148052}[：四次握手]{style="font-family:KaiTi_GB2312"}[message 1]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4-way handshake message 3]{lang="EN-US"}]{#struct_0_59269_x7909_x2013509179}[：四次握手]{style="font-family:KaiTi_GB2312"}[message 3]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[group handshake message 1]{lang="EN-US"}]{#struct_0_59269_x7909_x1390162320}[：组播握手]{style="font-family:KaiTi_GB2312"}[message 1]{lang="EN-US"}

[[Created *TimerType* timer *TimerId* for BSS *BSSID*.]{lang="EN-US"}]{#struct_0_59269_x7909_x1670954376}

[[BSS ]{lang="EN-US"}*[BSSID]{lang="EN-US"}*]{#struct_0_59269_x7909_1435153750}[创建]{style="font-family:宋体"}*[TimerType]{lang="EN-US"}*[类型定时器]{style="font-family:宋体"}*[TimerId]{lang="EN-US"}*[成功]{style="font-family:宋体"}

[*[TimerType]{lang="EN-US"}*]{#struct_0_59269_x7909_x1240823396}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TKIP detect]{lang="EN-US"}]{#struct_0_59269_x7909_x1585874946}[：]{style="font-family:KaiTi_GB2312"}[TKIP]{lang="EN-US"}[检测]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TKIP counter measure]{lang="EN-US"}]{#struct_0_59269_x7909_x1526883171}[：]{style="font-family:KaiTi_GB2312"}[TKIP]{lang="EN-US"}[反制]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GTK life]{lang="EN-US"}]{#struct_0_59269_x7909_x1670954375}[：]{style="font-family:KaiTi_GB2312"}[GTK]{lang="EN-US"}[更新]{style="font-family:KaiTi_GB2312"}

[[Deleted *TimerType* timer *TimerId* in BSS *BSSID*.]{lang="EN-US"}]{#struct_0_59269_x7909_1838438277}

[[删除]{style="font-family:宋体"}[BSS *BSSID* ]{lang="EN-US"}]{#struct_0_59269_x7909_x1945781908}[中的]{style="font-family:宋体"}*[TimerType]{lang="EN-US"}*[定时器]{style="font-family:宋体"}*[TimerId]{lang="EN-US"}*

[*[TimerType]{lang="EN-US"}*]{#struct_0_59269_x7909_x95581504}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TKIP detect]{lang="EN-US"}]{#struct_0_59269_x7909_1040559106}[：]{style="font-family:KaiTi_GB2312"}[TKIP]{lang="EN-US"}[检测]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TKIP counter measure]{lang="EN-US"}]{#struct_0_59269_x7909_8412326}[：]{style="font-family:KaiTi_GB2312"}[TKIP]{lang="EN-US"}[反制]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GTK life]{lang="EN-US"}]{#struct_0_59269_x7909_1191698280}[：]{style="font-family:KaiTi_GB2312"}[GTK]{lang="EN-US"}[更新]{style="font-family:KaiTi_GB2312"}

[*[TimerType]{lang="EN-US"}*[ timer *TimerId* in BSS *BSSID* expired.]{lang="EN-US"}]{#struct_0_59269_x7909_x1670954374}

[[BSS ]{lang="EN-US"}*[BSSID]{lang="EN-US"}*]{#struct_0_59269_x7909_272354336}[中的]{style="font-family:宋体"}*[TimerType]{lang="EN-US"}*[定时器]{style="font-family:宋体"}*[TimerId]{lang="EN-US"}*[超时]{style="font-family:宋体"}

[*[TimerType]{lang="EN-US"}*]{#struct_0_59269_x7909_744916308}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TKIP detect]{lang="EN-US"}]{#struct_0_59269_x7909_x1937853026}[：]{style="font-family:KaiTi_GB2312"}[TKIP]{lang="EN-US"}[检测]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TKIP counter measure]{lang="EN-US"}]{#struct_0_59269_x7909_1888436076}[：]{style="font-family:KaiTi_GB2312"}[TKIP]{lang="EN-US"}[反制]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GTK life]{lang="EN-US"}]{#struct_0_59269_x7909_775643169}[：]{style="font-family:KaiTi_GB2312"}[GTK]{lang="EN-US"}[更新定时器]{style="font-family:KaiTi_GB2312"}

[[Failed to create *TimerType* timer for BSS *BSSID*.]{lang="EN-US"}]{#struct_0_59269_x7909_x1670954373}

[[BSS ]{lang="EN-US"}*[BSSID]{lang="EN-US"}*]{#struct_0_59269_x7909_675638863}[创建]{style="font-family:宋体"}*[TimerType]{lang="EN-US"}*[类型定时器失败]{style="font-family:宋体"}

[*[TimerType]{lang="EN-US"}*]{#struct_0_59269_x7909_1876601795}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TKIP detect]{lang="EN-US"}]{#struct_0_59269_x7909_1967308849}[：]{style="font-family:KaiTi_GB2312"}[TKIP]{lang="EN-US"}[检测]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TKIP counter measure]{lang="EN-US"}]{#struct_0_59269_x7909_1654304531}[：]{style="font-family:KaiTi_GB2312"}[TKIP]{lang="EN-US"}[反制]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GTK life]{lang="EN-US"}]{#struct_0_59269_x7909_x1670954372}[：]{style="font-family:KaiTi_GB2312"}[GTK]{lang="EN-US"}[更新定时器]{style="font-family:KaiTi_GB2312"}

[[Created PTK life timer *TimerId*.]{lang="EN-US"}]{#struct_0_59269_x7909_x890445078}

[[创建]{style="font-family:宋体"}[PTK]{lang="EN-US"}]{#struct_0_59269_x7909_x897154053}[更新定时器]{style="font-family:宋体"}*[TimerId]{lang="EN-US"}*[成功]{style="font-family:宋体"}

[[Deleted PTK life timer *TimerId*.]{lang="EN-US"}]{#struct_0_59269_x7909_x870909941}

[[删除]{style="font-family:宋体"}[PTK]{lang="EN-US"}]{#struct_0_59269_x7909_x1868895891}[更新定时器]{style="font-family:宋体"}*[TimerId]{lang="EN-US"}*

[[PTK life timer *TimerId* expired.]{lang="EN-US"}]{#struct_0_59269_x7909_x1670954371}

[[PTK]{lang="EN-US"}]{#struct_0_59269_x7909_x487160551}[更新定时器]{style="font-family:宋体"}*[TimerId]{lang="EN-US"}*[超时]{style="font-family:宋体"}

[[Failed to create a PTK life timer.]{lang="EN-US"}]{#struct_0_59269_x7909_211567716}

[[创建]{style="font-family:宋体"}[PTK]{lang="EN-US"}]{#struct_0_59269_x7909_x2046071421}[更新定时器失败]{style="font-family:宋体"}

[[Deleted timer *TimerId* for resending *MsgType*.]{lang="EN-US"}]{#struct_0_59269_x7909_906187301}

[[删除重传]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*]{#struct_0_59269_x7909_x1670954370}[类型报文定时器]{style="font-family:宋体"}

[*[MsgType]{lang="EN-US"}*]{#struct_0_59269_x7909_x2053244492}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4-way handshake message]{lang="EN-US"}]{#struct_0_59269_x7909_751716743}[：四次握手]{style="font-family:KaiTi_GB2312"}[message]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[group handshake message]{lang="EN-US"}]{#struct_0_59269_x7909_x470327273}[：组播握手]{style="font-family:KaiTi_GB2312"}[message]{lang="EN-US"}

[[\[MAC: *UserMAC*, ]{lang="EN-US"}[APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID*\] Deleted SA query timer.]{lang="EN-US"}]{#struct_0_59269_x7909_x984864195}

[[用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_59269_x7909_x1099687967}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[ ]{lang="EN-US"}[，]{style="font-family:宋体"}[APID]{lang="EN-US"}[为]{style="font-family:宋体"}*[APID]{lang="EN-US"}*[，]{style="font-family:宋体"}[RadioID]{lang="EN-US"}[为]{style="font-family:宋体"}*[RadioID]{lang="EN-US"}*[，]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，删除]{style="font-family:宋体"}[SA Query]{lang="EN-US"}[定时器成功。]{style="font-family:宋体"}

[[\[MAC: *UserMAC*, ]{lang="EN-US"}[APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID*\] Failed to create SA query timer.]{lang="EN-US"}]{#struct_0_59269_x7909_x1604550392}

[[用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_59269_x7909_1387723264}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[ ]{lang="EN-US"}[，]{style="font-family:宋体"}[APID]{lang="EN-US"}[为]{style="font-family:宋体"}*[APID]{lang="EN-US"}*[，]{style="font-family:宋体"}[RadioID]{lang="EN-US"}[为]{style="font-family:宋体"}*[RadioID]{lang="EN-US"}*[，]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，创建]{style="font-family:宋体"}[SA Query]{lang="EN-US"}[定时器失败。]{style="font-family:宋体"}

[[\[MAC: *UserMAC*, ]{lang="EN-US"}[APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID*\] Created SA query timer.]{lang="EN-US"}]{#struct_0_59269_x7909_127795836}

[[用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_59269_x7909_x1730703606}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[ ]{lang="EN-US"}[，]{style="font-family:宋体"}[APID]{lang="EN-US"}[为]{style="font-family:宋体"}*[APID]{lang="EN-US"}*[，]{style="font-family:宋体"}[RadioID]{lang="EN-US"}[为]{style="font-family:宋体"}*[RadioID]{lang="EN-US"}*[，]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，创建]{style="font-family:宋体"}[SA Query]{lang="EN-US"}[定时器成功。]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_59269_x7909_x1029844}

[[\# ]{lang="EN-US"}]{#struct_0_59269_x7909_873915670}[在]{style="font-family:宋体"}[RSN]{lang="EN-US"}[安全模式下，客户端上线密钥协商过程中，该客户端的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[000b-c002-9d11]{lang="EN-US"}[，]{style="font-family:宋体"}

[[其所在]{style="font-family:宋体"}[BSS]{lang="EN-US"}]{#struct_0_59269_x7909_x1670954369}[的]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[为]{style="font-family:宋体"}[000f-e202-1213]{lang="EN-US"}[，在]{style="font-family:宋体"}[AC]{lang="EN-US"}[端打开]{style="font-family:宋体"}[wlan usersec packet send]{lang="EN-US"}[开关，会有]{style="font-family:宋体"}

[[下调试信息：]{style="font-family:宋体"}]{#struct_0_59269_x7909_x130864655}

[[\<H3C\>debugging wlan usersec packet send]{lang="EN-US"}]{#struct_0_59269_x7909_1084756134}

[%Apr  4 09:18:45:965 2014 H3C STAMGR/4/PktSend: \[MAC:000b-c002-9d11, BSSID:000f-]{lang="EN-US"}

[e202-1213\]Sent 4-way handshake message1 successfully.]{lang="EN-US"}

[*[//]{lang="EN-US"}*]{#struct_0_59269_x7909_1740398666}*[成功发送四次握手]{style="font-family:宋体"}[message1]{lang="EN-US"}[消息。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_59269_x7909_1767172306}[在]{style="font-family:宋体"}[RSN]{lang="EN-US"}[安全模式下，客户端上线密钥协商过程中，在]{style="font-family:宋体"}[AC]{lang="EN-US"}[端打开]{style="font-family:宋体"}[wlan usersec packet send verbos]{lang="EN-US"}

[[开关，会有如下调试信息：]{style="font-family:宋体"}]{#struct_0_59269_x7909_x2018624286}

[[\<H3C\>debugging wlan usersec packet send verbose]{lang="EN-US"}]{#struct_0_59269_x7909_1765374041}

[\*Apr  4 09:18:45:964 2014 H3C STAMGR/4/PktSend: Sent an EAPOL-key frame to client 000b-c002-9d11 (Length: 153)]{lang="EN-US"}

[ 08 02 7f 00 00 0b c0 02 9d 11 00 0f e2 02 12 13]{lang="EN-US"}

[ 00 0f e2 02 12 13 00 00 aa aa 03 00 00 00 88 8e]{lang="EN-US"}

[ 01 03 00 75 02 00 8a 00 10 00 00 00 00 00 00 00]{lang="EN-US"}

[ 00 55 f3 62 91 d2 85 a6 9b 3f 51 32 c7 02 08 b8]{lang="EN-US"}

[ 78 f3 01 6b 83 42 31 d8 ea 41 5a 1f c2 7d 8e 93]{lang="EN-US"}

[ 34 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[ 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[ 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[ 00 00 16 dd 14 00 0f ac 04 00 00 00 00 00 00 00]{lang="EN-US"}

[ 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[*[//]{lang="EN-US"}*]{#struct_0_59269_x7909_1597449822}*[发送一个]{style="font-family:宋体"}[EAPOL-Key]{lang="EN-US"}[报文到客户端。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_59269_x7909_x1437385033}[在]{style="font-family:宋体"}[RSN]{lang="EN-US"}[安全模式下，客户端上线密钥协商过程中，在]{style="font-family:宋体"}[AC]{lang="EN-US"}[端打开]{style="font-family:宋体"}[wlan usersec packet receive]{lang="EN-US"}[开关，会有如下调试信息：]{style="font-family:宋体"}

[[\<H3C\>debugging wlan usersec packet receive]{lang="EN-US"}]{#struct_0_59269_x7909_x1670954368}

[%Apr  4 09:18:46:096 2014 H3C STAMGR/4/PktRcv: \[MAC:000b-c002-9d11, BSSID:000f-e]{lang="EN-US"}

[202-1213\]Received 4-way handshake massage2.]{lang="EN-US"}

[*[//]{lang="EN-US"}*]{#struct_0_59269_x7909_x1696948596}*[接受到四次握手]{style="font-family:宋体"}[message2]{lang="EN-US"}[消息。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_59269_x7909_889103761}[在]{style="font-family:宋体"}[RSN]{lang="EN-US"}[安全模式下，客户端上线密钥协商过程中，在]{style="font-family:宋体"}[AC]{lang="EN-US"}[端打开]{style="font-family:宋体"}[wlan usersec event]{lang="EN-US"}[开关，会有如下调试信息：]{style="font-family:宋体"}

[[\<H3C\>debugging wlan usersec event]{lang="EN-US"}]{#struct_0_59269_x7909_x1650202926}

[%Apr  4 09:18:46:110 2014 H3C STAMGR/4/Event: \[MAC:000b-c002-9d11, BSSID:000f-e2]{lang="EN-US"}

[02-1213\]Processed 4-way handshake message2 successfully.]{lang="EN-US"}

[*[//]{lang="EN-US"}*]{#struct_0_59269_x7909_x662547155}*[处理四次握手]{style="font-family:宋体"}[message2]{lang="EN-US"}[报文成功。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_59269_x7909_x1578020508}[在]{style="font-family:宋体"}[RSN]{lang="EN-US"}[安全模式下，客户端上线密钥协商过程中，在]{style="font-family:宋体"}[AC]{lang="EN-US"}[端打开]{style="font-family:宋体"}[wlan usersec timer]{lang="EN-US"}[开关，会有如下调试信息：]{style="font-family:宋体"}

[[\<H3C\>debugging wlan usersec timer]{lang="EN-US"}]{#struct_0_59269_x7909_1744340198}

[%Apr  4 09:18:45:967 2014 H3C STAMGR/4/Timer: \[MAC:000b-c002-9d11, BSSID:000f-e2]{lang="EN-US"}

[02-1213\]Created timer 1 for resending 4-way handshake message1 successfully.]{lang="EN-US"}

[*[//]{lang="EN-US"}*]{#struct_0_59269_x7909_1117996015}*[创建四次握手]{style="font-family:宋体"}[message1]{lang="EN-US"}[重传定时器成功。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_59269_x7909_1791007791}[在设备上配置支持]{style="font-family:宋体"}[802.11w]{lang="EN-US"}[的客户端上线，打开]{style="font-family:宋体"}[WPMF]{lang="EN-US"}[事件调试信息开关和定时器调试开关，打印如下调试信息：]{style="font-family:宋体"}

[[\<AC\> debugging wlan usersec event]{lang="EN-US"}]{#struct_0_59269_x7909_x828256960}

[[\*Jun 28 19:07:46:926 2014 H3C STAMGR/7/Event: \[MAC: 9cd3-6d9e-6742, APID: 2, RadioID: 2, BSSID: 000f-e2ff-0011\] Initialized wpmf information in client.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_59269_x7909_x522971270}

[*[//]{lang="EN-US"}*]{#struct_0_59269_x7909_2062579284}*[初始化]{style="font-family:宋体"}[STA]{lang="EN-US"}[信息中的]{style="font-family:宋体"}[wpmf]{lang="EN-US"}[信息成功。]{style="font-family:宋体"}*

[[\*Jun 28 19:07:47:070 2014 H3C STAMGR/7/Timer: \[MAC: 9cd3-6d9e-6742, APID: 2, RadioID: 2, BSSID: 000f-e2ff-0011\] Created SA query timer.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_59269_x7909_1615075113}

[*[//]{lang="EN-US"}*]{#struct_0_59269_x7909_x1080925450}*[创建一个安全连接询问定时器。]{style="font-family:宋体"}*
