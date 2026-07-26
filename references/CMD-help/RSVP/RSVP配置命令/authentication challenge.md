::: {#-1547490737 .myid}
[]{#_Toc404791045}[]{#struct_0_16315_x4274_1496350459}[]{#_Toc333936368}[]{#_Toc328505087}

**RSVP \-- RSVP配置命令 \-- authentication challenge**

------------------------------------------------------------------------

[**[authentication challenge]{lang="EN-US"}**]{#struct_0_16315_x4274_306469069}[命令用来全局或为指定]{style="font-family:
宋体"}[RSVP]{lang="EN-US"}[邻居开启]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[认证的]{style="font-family:宋体"}[challenge-response]{lang="EN-US"}[握手功能。]{style="font-family:宋体"}

[**[undo authentication challenge]{lang="EN-US"}**]{#struct_0_16315_x4274_x823633547}[命令用来全局或为指定]{style="font-family:
宋体"}[RSVP]{lang="EN-US"}[邻居关闭]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[认证的]{style="font-family:宋体"}[challenge-response]{lang="EN-US"}[握手功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1255579793}

[**[authentication challenge]{lang="EN-US"}**]{#struct_0_16315_x4274_x1788026180}

[**[undo authentication challenge]{lang="EN-US"}**]{#struct_0_16315_x4274_1337451465}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1780047878}

[[认证的]{style="font-family:宋体"}[challenge-response]{lang="EN-US"}]{#struct_0_16315_x4274_1257984328}[握手功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16315_x4274_870076796}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x793535686}[视图]{style="font-family:宋体"}[/RSVP]{lang="EN-US"}[邻居视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x599686178}

[[network-admin]{lang="EN-US"}]{#struct_0_16315_x4274_x492040289}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16315_x4274_x824223370}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1751932544}

[[为了避免报文的重放（]{style="font-family:宋体"}[Replay]{lang="EN-US"}]{#struct_0_16315_x4274_358300343}[）攻击，]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[接收认证消息时要求认证消息的序列号依次增加，]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[在接收]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[（]{style="font-family:宋体"}[Security Association]{lang="EN-US"}[，安全联盟）中保存最后一次收到的消息的序列号，用于判断后续消息是否符合要求。但是，在新创建接收]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[的时候，无法获取发送端的序列号，因此缺省情况下，创建接收]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[时将接收序列号填写为零，这样对端发送任意序列号的消息就都能接收。这就增加了重放攻击的风险。为了避免这种风险，可以执行]{style="font-family:宋体"}**[authentication challenge]{lang="ES"}**[命令，使得在新建接收]{style="font-family:宋体"}[RSVP SA]{lang="ES"}[时]{style="font-family:宋体"}[执行]{style="font-family:宋体"}[challenge-response]{lang="ES"}[握手过程，]{style="font-family:宋体"}[获取发送端的序列号。]{style="font-family:宋体"}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_597949011}[认证的]{style="font-family:宋体"}[challenge-response]{lang="EN-US"}[握手功能可以在如下视图配置：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_1870770750}[视图：该视图下的配置对所有]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_1594111147}[邻居视图：该视图下的配置只对与指定]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居之间的]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口视图：该视图下的配置只对根据指定接口下的配置生成的]{style="font-family:宋体"}]{#struct_0_16315_x4274_1870705214}[RSVP SA]{lang="EN-US"}[生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x686411319}

[[\# ]{lang="ES"}]{#struct_0_16315_x4274_x757614203}[在]{style="font-family:宋体"}[RSVP]{lang="ES"}[视图]{style="font-family:
宋体"}[下全局开启]{style="font-family:宋体"}[RSVP]{lang="ES"}[认证的]{style="font-family:宋体"}[challenge-response]{lang="ES"}[握手功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="ES"}]{#struct_0_16315_x4274_x824157834}

[\[Sysname\] rsvp]{lang="ES"}

[\[Sysname-rsvp\] authentication challenge]{lang="ES"}

[[\# ]{lang="ES"}]{#struct_0_16315_x4274_237931577}[在]{style="font-family:宋体"}[RSVP]{lang="ES"}[邻居视图]{style="font-family:
宋体"}[下开启本地设备与]{style="font-family:宋体"}[RSVP]{lang="ES"}[邻居]{style="font-family:宋体"}[1.1.1.9]{lang="ES"}[之间]{style="font-family:宋体"}[RSVP]{lang="ES"}[认证的]{style="font-family:宋体"}[challenge-response]{lang="ES"}[握手功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="ES"}]{#struct_0_16315_x4274_x1385134671}

[\[Sysname\] rsvp]{lang="ES"}

[\[Sysname-rsvp\] peer 1.1.1.9]{lang="ES"}

[\[Sysname-rsvp-peer-1.1.1.9\] authentication challenge]{lang="ES"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1515098137}

[[·[              ]{style="font:7.0pt "}]{lang="ES" style="font-size:10.0pt;font-family:Symbol"}**[authentication key]{lang="ES"}**]{#struct_0_16315_x4274_616289984}

[[·[              ]{style="font:7.0pt "}]{lang="ES" style="font-size:10.0pt;font-family:Symbol"}**[authentication lifetime]{lang="ES"}**]{#struct_0_16315_x4274_x513734898}

[[·[              ]{style="font:7.0pt "}]{lang="ES" style="font-size:10.0pt;font-family:Symbol"}**[authentication window-size]{lang="ES"}**]{#struct_0_16315_x4274_2109777202}

[[·[              ]{style="font:7.0pt "}]{lang="ES" style="font-size:10.0pt;font-family:Symbol"}**[display rsvp authentication]{lang="ES"}**]{#struct_0_16315_x4274_1398437147}

[[·[              ]{style="font:7.0pt "}]{lang="ES" style="font-size:10.0pt;font-family:Symbol"}**[reset ]{lang="ES"}**]{#struct_0_16315_x4274_828361920}**[rsvp authentication]{lang="ES"}**

[[·[              ]{style="font:7.0pt "}]{lang="ES" style="font-size:10.0pt;font-family:Symbol"}**[rsvp authentication challenge]{lang="ES"}**]{#struct_0_16315_x4274_x824354442}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp authentication key]{lang="EN-US"}**]{#struct_0_16315_x4274_x1359860081}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp authentication lifetime]{lang="EN-US"}**]{#struct_0_16315_x4274_x165108141}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp authentication window-size]{lang="EN-US"}**]{#struct_0_16315_x4274_1317501925}
:::

::: {#1053000967 .myid}
[]{#_Toc404791046}[]{#struct_0_16315_x4274_x1544515611}[]{#_Toc333936369}[]{#_Toc328505088}[]{#_Toc324951715}[]{#_Toc329607561}[]{#_Toc329607675}[]{#_Toc330307094}[]{#_Toc329607562}[]{#_Toc329607676}[]{#_Toc330307095}[]{#_Toc329607563}[]{#_Toc329607677}[]{#_Toc330307096}

**RSVP \-- RSVP配置命令 \-- authentication key**

------------------------------------------------------------------------

[**[authentication key]{lang="EN-US"}**]{#struct_0_16315_x4274_x1682280758}[命令用来全局或为指定]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居开启]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[认证功能，并配置认证密钥。]{style="font-family:宋体"}

[**[undo authentication key]{lang="EN-US"}**]{#struct_0_16315_x4274_x2069418228}[命令用来全局或为指定]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居关闭]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[认证功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1307056348}

[**[authentication key ]{lang="EN-US"}**[{ **cipher** \| **plain** } *auth-key*]{lang="EN-US"}]{#struct_0_16315_x4274_x606185029}

[**[undo authentication key]{lang="EN-US"}**]{#struct_0_16315_x4274_565000167}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x824288906}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_1386194318}[认证功能处于关闭状态，即不进行]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1105835584}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_1388939343}[视图]{style="font-family:宋体"}[/RSVP]{lang="EN-US"}[邻居视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1213905390}

[[network-admin]{lang="EN-US"}]{#struct_0_16315_x4274_x359093013}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16315_x4274_x1886678061}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1758400535}

[**[cipher]{lang="EN-US"}**]{#struct_0_16315_x4274_76415331}[：表示以密文形式设置密钥。]{style="font-family:宋体"}

[**[plain]{lang="EN-US"}**]{#struct_0_16315_x4274_x823961226}[：表示以明文形式设置密钥。]{style="font-family:宋体"}

[*[auth-key]{lang="EN-US"}*]{#struct_0_16315_x4274_x1239976362}[：认证密钥，区分大小写。如果采用明文（]{style="font-family:宋体"}**[plain]{lang="EN-US"}**[）形式，则为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[个字符的明文字符串；如果采用密文（]{style="font-family:宋体"}**[cipher]{lang="EN-US"}**[）形式，则为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[53]{lang="EN-US"}[个字符的密文字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16315_x4274_778625852}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_612284627}[认证功能可以用来确保]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息不会被篡改，]{style="font-family:宋体"}[防止伪造的资源预留请求非法占用网络资源。]{style="font-family:宋体"}

[[配置]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x1562038740}[认证功能后，发送]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息时会使用]{style="font-family:宋体"}[MD5]{lang="EN-US"}[算法对]{style="font-family:宋体"}[认证密钥和消息内容计算出消息摘要，并将消息摘要添加到发送的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息中。对端接收到]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息后，也进行同样地计算，并将计算结果和消息中的摘要进行比较。如果一致，则认证通过，接收该消息；否则认证失败，丢弃该消息。]{style="font-family:宋体"}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_1765558107}[认证功能可以在如下视图配置：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_1871491646}[视图：该视图下的配置对所有]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x1896693788}[邻居视图：该视图下的配置只对与指定]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居之间的]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口视图：该视图下的配置只对根据指定接口下的配置生成的]{style="font-family:宋体"}]{#struct_0_16315_x4274_1871426110}[RSVP SA]{lang="EN-US"}[生效。]{style="font-family:宋体"}

[[如果在多个视图下配置了认证密钥，则认证密钥的使用优先级顺序从高到低依次为：]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_1061302239}[邻居视图、接口视图、]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[视图。例如，如果在]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居视图和]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[视图都开启了与特定邻居的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[认证功能，并配置了不同的认证密钥，则采用]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居视图下配置的密钥认证本地设备和该邻居之间的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[[如果已经采用某个视图下配置的认证密钥建立了]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}]{#struct_0_16315_x4274_x823895690}[，则只有先删除当前视图下配置的认证密钥或执行]{style="font-family:宋体"}**[reset rsvp authentication]{lang="EN-US"}**[命令删除该]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[，才会按照上述优先级顺序重新查找新的认证密钥并建立]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_16315_x4274_1528734738}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本地设备上开启]{style="font-family:宋体"}]{#struct_0_16315_x4274_x1057070833}[RSVP]{lang="EN-US"}[认证功能后，在相应的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居上也需要开启]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[认证功能，并配置相同的认证密钥。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以明文或密文形式设置的密钥，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_16315_x4274_x490813787}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16315_x4274_325634272}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_x1129434378}[在]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[视图下全局开启]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[认证功能，并指定认证密钥为明文]{style="font-family:宋体"}[abcdefgh]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16315_x4274_x191931591}

[\[Sysname\] rsvp ]{lang="EN-US"}

[\[Sysname-rsvp\] authentication key plain abcdefgh]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_x1947356680}[在]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居视图下开启本地设备与邻居]{style="font-family:宋体"}[1.1.1.9]{lang="EN-US"}[之间的认证功能，并指定认证密钥为明文]{style="font-family:宋体"}[abcdefgh]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16315_x4274_x824092298}

[\[Sysname\] rsvp]{lang="EN-US"}

[\[Sysname-rsvp\] peer 1.1.1.9]{lang="EN-US"}

[\[Sysname-rsvp-peer-1.1.1.9\] authentication key plain abcdefgh]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1006823841}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication challenge]{lang="EN-US"}**]{#struct_0_16315_x4274_290238027}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication lifetime]{lang="EN-US"}**]{#struct_0_16315_x4274_410785475}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication window-size]{lang="EN-US"}**]{#struct_0_16315_x4274_x341909528}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display rsvp authentication]{lang="EN-US"}**]{#struct_0_16315_x4274_x697357532}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ]{lang="EN-US"}[rsvp authentication]{lang="EN-US"}**]{#struct_0_16315_x4274_x191063429}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp authentication challenge]{lang="EN-US"}**]{#struct_0_16315_x4274_x774191246}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp authentication key]{lang="EN-US"}**]{#struct_0_16315_x4274_1003916636}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp authentication lifetime]{lang="EN-US"}**]{#struct_0_16315_x4274_2049313784}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp authentication window-size]{lang="EN-US"}**]{#struct_0_16315_x4274_x824026762}
:::

::: {#515937491 .myid}
[]{#_Toc404791047}[]{#struct_0_16315_x4274_1757222716}[]{#_Toc333936370}[]{#_Toc328505089}[]{#_Toc324951716}[]{#_Toc252960451}[]{#_Toc252962387}[]{#_Toc252962501}[]{#_Toc252973225}

**RSVP \-- RSVP配置命令 \-- authentication lifetime**

------------------------------------------------------------------------

[**[authentication lifetime]{lang="EN-US"}**]{#struct_0_16315_x4274_785529885}[命令用来全局或为指定]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居配置]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[的空闲老化时间。]{style="font-family:宋体"}

[**[undo ]{lang="ES"}[authentication lifetime]{lang="EN-US"}**]{#struct_0_16315_x4274_858370084}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1032818931}

[**[authentication lifetime ]{lang="EN-US"}***[life-time]{lang="EN-US"}*]{#struct_0_16315_x4274_1907538156}

[**[undo ]{lang="ES"}[authentication lifetime]{lang="EN-US"}**]{#struct_0_16315_x4274_x648361956}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x2116844126}

[[RSVP SA]{lang="EN-US"}]{#struct_0_16315_x4274_986099857}[的空闲老化时间为]{style="font-family:宋体"}[1800]{lang="EN-US"}[秒（]{style="font-family:宋体"}[30]{lang="EN-US"}[分钟）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x823699082}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x466609387}[视图]{style="font-family:宋体"}[/RSVP]{lang="EN-US"}[邻居视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x76353199}

[[network-admin]{lang="EN-US"}]{#struct_0_16315_x4274_x2127391290}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16315_x4274_1743586800}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1401780336}

[*[life-time]{lang="EN-US"}*]{#struct_0_16315_x4274_493449493}[：]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[的空闲老化时间，取值范围为]{style="font-family:宋体"}[30]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x200593873}

[[开启了]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x670860117}[认证功能后，设备收发]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息时会动态建立]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[，以记录消息的序列号、方便对]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息进行认证处理。]{style="font-family:宋体"}

[[为了在不需要]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}]{#struct_0_16315_x4274_x823633546}[的时候，能够及时删除该]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[，回收内存资源，每个]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[都有其老化时间。当]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[的空闲时间到达老化时间时，将删除该]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[。设备发送和接收]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[认证消息时，会更新对应]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[的空闲时间，避免其被老化删除。]{style="font-family:宋体"}

[[RSVP SA]{lang="EN-US"}]{#struct_0_16315_x4274_x1255645329}[的空闲老化时间可以在如下视图配置：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_1166089035}[视图：该视图下的配置对所有]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_1556816784}[邻居视图：该视图下的配置只对与指定]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居之间的]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口视图：该视图下的配置只对根据指定接口下的配置生成的]{style="font-family:宋体"}]{#struct_0_16315_x4274_492595310}[RSVP SA]{lang="EN-US"}[生效。]{style="font-family:宋体"}

[[采用某个视图下配置的认证密钥建立]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}]{#struct_0_16315_x4274_x1972143259}[后，该]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[的空闲老化时间为该视图下配置的老化时间。]{style="font-family:宋体"}

[[修改]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}]{#struct_0_16315_x4274_1969837718}[的空闲老化时间后，只会对新建立的]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[生效。要想使得修改后的空闲老化时间对已建立的]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[生效，则需要执行]{style="font-family:宋体"}**[reset rsvp authentication]{lang="EN-US"}**[命令来删除并重新建立]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16315_x4274_286884608}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_x307625491}[在]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[视图下全局配置]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[的空闲老化时间为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16315_x4274_x824223373}

[\[Sysname\] rsvp]{lang="EN-US"}

[\[Sysname-rsvp\] authentication lifetime 100]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_1751998080}[在]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居视图下配置本地设备与]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居]{style="font-family:宋体"}[1.1.1.9]{lang="EN-US"}[之间]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[的空闲老化时间为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16315_x4274_707053769}

[\[Sysname\] rsvp]{lang="EN-US"}

[\[Sysname-rsvp\] peer 1.1.1.9]{lang="EN-US"}

[\[Sysname-rsvp-peer-1.1.1.9\] authentication lifetime 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x481271314}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication challenge]{lang="EN-US"}**]{#struct_0_16315_x4274_x1012549406}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication key]{lang="EN-US"}**]{#struct_0_16315_x4274_x459769477}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication window-size]{lang="EN-US"}**]{#struct_0_16315_x4274_x1038867736}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display rsvp authentication]{lang="EN-US"}**]{#struct_0_16315_x4274_341242728}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ]{lang="EN-US"}[rsvp authentication]{lang="EN-US"}**]{#struct_0_16315_x4274_x824157837}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp authentication challenge]{lang="EN-US"}**]{#struct_0_16315_x4274_238128185}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp authentication key]{lang="EN-US"}**]{#struct_0_16315_x4274_x675619001}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp authentication lifetime]{lang="EN-US"}**]{#struct_0_16315_x4274_2010769741}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp authentication window-size]{lang="EN-US"}**]{#struct_0_16315_x4274_x435541818}
:::

::: {#213714050 .myid}
[]{#_Toc404791048}[]{#struct_0_16315_x4274_1555131866}[]{#_Toc333936371}[]{#_Toc328505090}[]{#_Toc324951717}

**RSVP \-- RSVP配置命令 \-- authentication window-size**

------------------------------------------------------------------------

[**[authentication window-size]{lang="ES"}**]{#struct_0_16315_x4274_1052487772}[命令用来全局或为指定]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居配置对于带有认证信息的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息，最大可允许的乱序消息数量。]{style="font-family:宋体"}

[**[undo authentication window-size]{lang="ES"}**]{#struct_0_16315_x4274_478213197}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_872142503}

[**[authentication window-size ]{lang="ES"}***[numbe]{lang="EN-US"}*]{#struct_0_16315_x4274_x824354445}

[**[undo authentication window-size]{lang="ES"}**]{#struct_0_16315_x4274_x1359663473}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1448887015}

[[对于带有认证信息的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_982324300}[消息，最大可允许的乱序消息数量为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16315_x4274_310685563}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_1940676868}[视图]{style="font-family:宋体"}[/RSVP]{lang="EN-US"}[邻居视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1547925524}

[[network-admin]{lang="EN-US"}]{#struct_0_16315_x4274_655066928}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16315_x4274_1248409242}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1443472191}

[*[number]{lang="EN-US"}*]{#struct_0_16315_x4274_x824288909}[：最大可允许的乱序消息数量，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1385473422}

[[为了防止报文重放攻击，]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_1009713749}[在带有认证信息的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息中携带唯一的序列号。每发送一个消息，序列号依次增加。如果接收到的消息序列号在允许的范围内，则接受该消息；否则，丢弃该消息。]{style="font-family:宋体"}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_482586354}[判断报文序列号是否在允许范围内的方法为：]{style="font-family:宋体"}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[在设备上记录最后一次接收到的]{lang="EN-US" style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x999851198}[报文的序列号。]{lang="EN-US" style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[设备接收到新的]{lang="EN-US" style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_711242261}[报文时，将该报文的序列号与记录的序列号进行比较：]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果大于记录的序列号，则将记录的序列号更新为该报文的序列号。]{style="font-family:宋体"}]{#struct_0_16315_x4274_x727449212}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果等于记录的序列号，则认为是重放攻击，丢弃该报文。]{style="font-family:宋体"}]{#struct_0_16315_x4274_x1479140661}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果小于记录的序列号、大于（记录的序列号---本命令配置的]{style="font-family:宋体"}]{#struct_0_16315_x4274_729777576}[window-size]{lang="EN-US"}[），且未收到过该序列号的报文，则接收该报文；若已经收到过该序列号的报文，则认为是重放攻击，丢弃该报文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果小于等于（记录的序列号---本命令配置的]{style="font-family:宋体"}]{#struct_0_16315_x4274_x823961229}[window-size]{lang="EN-US"}[），则认为报文序列号不合法，丢弃该报文。]{style="font-family:宋体"}

[[缺省情况下，最大可允许的乱序消息数量为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_16315_x4274_x1240435114}[，即]{style="font-family:宋体"}[如果新收到的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息的序列号小于最后收到的消息序列号，则认为该消息是重放攻击，丢弃该消息。但是，如果在短时间内发送了多个]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息，那么这些消息到达邻居时可能会产生乱序。若采用缺省情况，则会导致这些乱序消息被丢弃。此时，可以通过本命令配置较大的]{style="font-family:宋体"}[window-size]{lang="EN-US"}[解决此问题。]{style="font-family:宋体"}

[[采用某个视图下配置的认证密钥建立]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}]{#struct_0_16315_x4274_x835207807}[后，该]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[的最大可允许乱序消息数量为该视图下配置的值。]{style="font-family:宋体"}

[[修改最大可允许的乱序消息数量后，只会对新建立的]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}]{#struct_0_16315_x4274_1165198368}[生效。要想使得修改后的最大可允许乱序消息数量对已建立的]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[生效，则需要执行]{style="font-family:宋体"}**[reset rsvp authentication]{lang="EN-US"}**[命令来删除并重新建立]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1676652247}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_1838620150}[在]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[视图下全局配置对于带有认证信息的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息，最大可允许的乱序消息数量为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16315_x4274_412423380}

[\[Sysname\] rsvp]{lang="EN-US"}

[\[Sysname-rsvp\] authentication window-size 10]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_1859353840}[在]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居视图下配置本地设备和]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居]{style="font-family:宋体"}[1.1.1.9]{lang="EN-US"}[之间对于带有认证信息的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息，最大可允许的乱序消息数量为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16315_x4274_x823895693}

[\[Sysname\] rsvp]{lang="EN-US"}

[\[Sysname-rsvp\] peer 1.1.1.9]{lang="EN-US"}

[\[Sysname-rsvp-peer-1.1.1.9\] authentication window-size 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1528931346}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication challenge]{lang="EN-US"}**]{#struct_0_16315_x4274_466200407}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication key]{lang="EN-US"}**]{#struct_0_16315_x4274_769593649}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication lifetime]{lang="EN-US"}**]{#struct_0_16315_x4274_1839933756}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display rsvp authentication]{lang="EN-US"}**]{#struct_0_16315_x4274_x1127839596}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ]{lang="EN-US"}[rsvp authentication]{lang="EN-US"}**]{#struct_0_16315_x4274_1008574291}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp authentication challenge]{lang="EN-US"}**]{#struct_0_16315_x4274_x1510672964}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp authentication key]{lang="EN-US"}**]{#struct_0_16315_x4274_x54164228}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp authentication lifetime]{lang="EN-US"}**]{#struct_0_16315_x4274_x824092301}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp authentication window-size]{lang="EN-US"}**]{#struct_0_16315_x4274_x948901462}
:::

::: {#-1204101853 .myid}
[]{#_Toc404791049}[]{#struct_0_16315_x4274_x1753905592}[]{#_Toc333936379}[]{#_Toc328505091}[]{#_Toc324951718}

**RSVP \-- RSVP配置命令 \-- display rsvp**

------------------------------------------------------------------------

[**[display rsvp]{lang="EN-US"}**]{#struct_0_16315_x4274_1582575813}[命令用来显示]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1017888212}

[**[display rsvp ]{lang="EN-US"}**[\[ **interface** \[ *interface-type interface-number* \] \]]{lang="EN-US"}]{#struct_0_16315_x4274_x1992644364}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1957788631}

[[任意视图]{style="font-family:宋体"}]{#struct_0_16315_x4274_855434783}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1082986172}

[[network-admin]{lang="EN-US"}]{#struct_0_16315_x4274_x824026765}

[[network-operator]{lang="EN-US"}]{#struct_0_16315_x4274_1757288252}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16315_x4274_1134545455}

[[mdc-operator]{lang="EN-US"}]{#struct_0_16315_x4274_798281070}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16315_x4274_224550644}

[**[interface]{lang="EN-US"}**]{#struct_0_16315_x4274_1634827226}[：显示接口的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_16315_x4274_608417347}[：显示指定接口的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型及接口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16315_x4274_566158578}

[[执行]{style="font-family:宋体"}**[display]{lang="EN-US"}**[ **rsvp**]{lang="EN-US"}]{#struct_0_16315_x4274_1276414507}[命令时：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{lang="EN-US" style="font-family:宋体"}**[interface]{lang="EN-US"}**]{#struct_0_16315_x4274_x823699085}[参数，则显示全局的]{lang="EN-US" style="font-family:宋体"}[RSVP]{lang="EN-US"}[信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果只指定]{lang="EN-US" style="font-family:宋体"}**[interface]{lang="EN-US"}**]{#struct_0_16315_x4274_x466937067}[参数，不指定]{lang="EN-US" style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[参数，则显示所有接口的]{lang="EN-US" style="font-family:宋体"}[RSVP]{lang="EN-US"}[信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[interface]{lang="EN-US"}**[ interface-type interface-number]{lang="EN-US"}]{#struct_0_16315_x4274_1041060320}[参数，则显示指定接口的]{lang="EN-US" style="font-family:宋体"}[RSVP]{lang="EN-US"}[信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1999586264}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_x1243397830}[显示全局的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[]{#struct_0_16315_x4274_x823633549}[[\<Sysname\> display rsvp]{lang="EN-US"}]{#_Toc38708889}

[LSR ID: 50.0.0.1                       Fast Reroute time: 300 sec]{lang="EN-US"}

[Refresh interval: 30 sec               Keep multiplier: 3]{lang="EN-US"}

[Hello interval: 3 sec                  Hello lost: 4]{lang="EN-US"}

[Graceful Restart: Disabled             DSCP value: 48]{lang="EN-US"}

[Authentication: Enabled]{lang="EN-US"}

[  Lifetime: 300 sec]{lang="EN-US"}

[  Window size: 64]{lang="EN-US"}

[  Challenge: Enabled]{lang="EN-US"}

[Statistics:]{lang="EN-US"}

[  PSB number: 5                        RSB number: 5]{lang="EN-US"}

[  LSP number: 5                        Request number: 5]{lang="EN-US"}

[  Peer number: 5                       SA number: 5]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display rsvp]{lang="EN-US"}]{#struct_0_16315_x4274_x1255186577}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x435257617}[[字段]{style="font-family:黑体"}]{#struct_0_16315_x4274_x2114368513}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16315_x4274_257430776}

[[LSR ID]{lang="EN-US"}]{#struct_0_16315_x4274_x865767705}

[[标签交换路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_16315_x4274_1142051236}

[[Fast Reroute time]{lang="EN-US"}]{#struct_0_16315_x4274_2043983986}

[[为决定一条]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_16315_x4274_x824223372}[是否应使用新的、更好的备份隧道而进行扫描的时间间隔，单位为秒]{style="font-family:宋体"}

[[Refresh interval]{lang="EN-US"}]{#struct_0_16315_x4274_1752063616}

[[路径和预留消息的刷新时间间隔，单位为秒]{style="font-family:宋体"}]{#struct_0_16315_x4274_x175061184}

[[Keep multiplier]{lang="EN-US"}]{#struct_0_16315_x4274_244681976}

[[PSB]{lang="EN-US"}]{#struct_0_16315_x4274_1682591686}[和]{style="font-family:宋体"}[RSB]{lang="EN-US"}[的超时倍数]{style="font-family:宋体"}

[[Hello interval]{lang="EN-US"}]{#struct_0_16315_x4274_x117707919}

[[Hello Request]{lang="EN-US"}]{#struct_0_16315_x4274_x239777956}[消息的发送时间间隔，单位为秒]{style="font-family:宋体"}

[[Hello lost]{lang="EN-US"}]{#struct_0_16315_x4274_x824157836}

[[最多可以接受的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_16315_x4274_238062649}[消息连续丢失次数]{style="font-family:宋体"}

[[Graceful Restart]{lang="EN-US"}]{#struct_0_16315_x4274_2046907490}

[[是否开启]{style="font-family:宋体"}[Graceful Restart]{lang="EN-US"}]{#struct_0_16315_x4274_x301601028}[能力，取值包括]{style="font-family:宋体"}[Enabled]{lang="EN-US"}[和]{style="font-family:宋体"}[Disabled]{lang="EN-US"}

[[DSCP value]{lang="EN-US"}]{#struct_0_16315_x4274_558395186}

[[发送的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x526788097}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级]{style="font-family:宋体"}

[[Authentication]{lang="EN-US"}]{#struct_0_16315_x4274_x1680579011}

[[是否开启]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x824354444}[认证功能，取值包括]{style="font-family:宋体"}[Enabled]{lang="EN-US"}[和]{style="font-family:宋体"}[Disabled]{lang="EN-US"}

[[Lifetime]{lang="EN-US"}]{#struct_0_16315_x4274_x1359729009}

[[RSVP SA]{lang="EN-US"}]{#struct_0_16315_x4274_125116775}[的空闲老化时间，单位为秒]{style="font-family:宋体"}

[[Window size]{lang="EN-US"}]{#struct_0_16315_x4274_479327418}

[[最大可允许的乱序消息数量]{style="font-family:宋体"}]{#struct_0_16315_x4274_x599779745}

[[Challenge]{lang="EN-US"}]{#struct_0_16315_x4274_x796390184}

[[是否开启认证的]{style="font-family:宋体"}[challenge-response]{lang="EN-US"}]{#struct_0_16315_x4274_x824288908}[握手功能，取值包括]{style="font-family:宋体"}[Enabled]{lang="EN-US"}[和]{style="font-family:宋体"}[Disabled]{lang="EN-US"}

[[Statistics]{lang="EN-US"}]{#struct_0_16315_x4274_1385538958}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x1258565132}[统计信息]{style="font-family:宋体"}

[[PSB number]{lang="EN-US"}]{#struct_0_16315_x4274_920070459}

[[PSB]{lang="EN-US"}]{#struct_0_16315_x4274_x1086712826}[总数]{style="font-family:宋体"}

[[RSB number]{lang="EN-US"}]{#struct_0_16315_x4274_x823961228}

[[RSB]{lang="EN-US"}]{#struct_0_16315_x4274_x1240369578}[总数]{style="font-family:宋体"}

[[LSP number]{lang="EN-US"}]{#struct_0_16315_x4274_959660354}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x1465640899}[协议建立的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[总数]{style="font-family:宋体"}

[[Request number]{lang="EN-US"}]{#struct_0_16315_x4274_x823895692}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_1528865810}[请求信息数据块总数]{style="font-family:宋体"}

[[Peer number]{lang="EN-US"}]{#struct_0_16315_x4274_2024002823}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x658960233}[协议动态生成的邻居的总数]{style="font-family:宋体"}

[[SA number]{lang="EN-US"}]{#struct_0_16315_x4274_797504238}

[[RSVP SA]{lang="EN-US"}]{#struct_0_16315_x4274_x824092300}[的总数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_x948966998}[显示所有接口的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display rsvp interface]{lang="EN-US"}]{#struct_0_16315_x4274_x824026764}

[Interface: GE1/0/1                      Logical interface handle: 0x3]{lang="EN-US"}

[State: Up                              IP address: 50.1.0.1]{lang="EN-US"}

[MPLS TE: Enabled                       RSVP: Enabled]{lang="EN-US"}

[Hello: Enabled                         BFD: Enabled]{lang="EN-US"}

[Summary refresh: Enabled               Reliability: Disabled]{lang="EN-US"}

[Retransmit interval: 500 ms            Retransmit increment: 1]{lang="EN-US"}

[Authentication: Enabled]{lang="EN-US"}

[  Lifetime: 300 sec]{lang="EN-US"}

[  Window size: 64]{lang="EN-US"}

[  Challenge: Enabled]{lang="EN-US"}

[Bypass tunnels: Tunnel0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface: GE1/0/2                      Logical interface handle: 0x67]{lang="EN-US"}

[State: Up                              IP address: 50.2.0.1]{lang="EN-US"}

[MPLS TE: Enabled                       RSVP: Enabled]{lang="EN-US"}

[Hello: Enabled                         BFD: Enabled]{lang="EN-US"}

[Summary refresh: Disabled              Reliability: Disabled]{lang="EN-US"}

[Retransmit interval: 500 ms            Retransmit increment: 1]{lang="EN-US"}

[Authentication: Enabled]{lang="EN-US"}

[  Lifetime: 300 sec]{lang="EN-US"}

[  Window size: 64]{lang="EN-US"}

[  Challenge: Enabled]{lang="EN-US"}

[Bypass tunnels: Tunnel0, Tunnel1, Tunnel2]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display rsvp interface]{lang="EN-US"}]{#struct_0_16315_x4274_1757353788}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x402690483}[[字段]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1952594086}

[[描述]{style="font-family:黑体"}]{#struct_0_16315_x4274_71921562}

[[Interface]{lang="EN-US"}]{#struct_0_16315_x4274_421540193}

[[接口的名称]{style="font-family:宋体"}]{#struct_0_16315_x4274_x369722358}

[[Logical interface handle]{lang="EN-US"}]{#struct_0_16315_x4274_x356840806}

[[接口的逻辑接口索引]{style="font-family:宋体"}]{#struct_0_16315_x4274_x823699084}

[[State]{lang="EN-US"}]{#struct_0_16315_x4274_x467002603}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x74970730}[所记录的接口状态，取值包括]{style="font-family:宋体"}[Up]{lang="EN-US"}[和]{style="font-family:宋体"}[Down]{lang="EN-US"}

[[IP address]{lang="EN-US"}]{#struct_0_16315_x4274_2013317737}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x1714197347}[当前所用的接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[MPLS TE]{lang="EN-US"}]{#struct_0_16315_x4274_571942617}

[[接口上是否开启]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}]{#struct_0_16315_x4274_x823633548}[能力，取值包括]{style="font-family:宋体"}[Enabled]{lang="EN-US"}[和]{style="font-family:宋体"}[Disabled]{lang="EN-US"}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x1255252113}

[[接口上是否开启]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x633952976}[能力，取值包括]{style="font-family:宋体"}[Enabled]{lang="EN-US"}[和]{style="font-family:宋体"}[Disabled]{lang="EN-US"}

[[Hello]{lang="EN-US"}]{#struct_0_16315_x4274_x1598698454}

[[接口上是否开启]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_16315_x4274_x961518909}[扩展功能，取值包括]{style="font-family:宋体"}[Enabled]{lang="EN-US"}[和]{style="font-family:宋体"}[Disabled]{lang="EN-US"}

[[BFD]{lang="EN-US"}]{#struct_0_16315_x4274_x824223375}

[[接口上是否开启]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_16315_x4274_1752129152}[检测功能，取值包括]{style="font-family:宋体"}[Enabled]{lang="EN-US"}[和]{style="font-family:宋体"}[Disabled]{lang="EN-US"}

[[Summary refresh]{lang="EN-US"}]{#struct_0_16315_x4274_x214805199}

[[接口上是否开启摘要刷新功能，取值包括]{style="font-family:宋体"}[Enabled]{lang="EN-US"}]{#struct_0_16315_x4274_x1208864519}[和]{style="font-family:宋体"}[Disabled]{lang="EN-US"}

[[Reliability]{lang="EN-US"}]{#struct_0_16315_x4274_1615187471}

[[接口上是否开启]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x824157839}[消息的可靠传递功能，取值包括]{style="font-family:宋体"}[Enabled]{lang="EN-US"}[和]{style="font-family:宋体"}[Disabled]{lang="EN-US"}

[[Retransmit interval]{lang="EN-US"}]{#struct_0_16315_x4274_238259257}

[[初始的重传时间间隔，单位为毫秒]{style="font-family:宋体"}]{#struct_0_16315_x4274_x1982365217}

[[Retransmit increment]{lang="EN-US"}]{#struct_0_16315_x4274_1981731333}

[[重传时间增量]{style="font-family:宋体"}]{#struct_0_16315_x4274_x437785681}

[[Authentication]{lang="EN-US"}]{#struct_0_16315_x4274_x824354447}

[[接口上是否开启]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x1359532401}[认证功能，取值包括]{style="font-family:宋体"}[Enabled]{lang="EN-US"}[和]{style="font-family:宋体"}[Disabled]{lang="EN-US"}

[[Lifetime]{lang="EN-US"}]{#struct_0_16315_x4274_x1136931274}

[[RSVP SA]{lang="EN-US"}]{#struct_0_16315_x4274_1463847081}[的空闲老化时间，单位为秒]{style="font-family:宋体"}

[[Window size]{lang="EN-US"}]{#struct_0_16315_x4274_1304789769}

[[最大可允许的乱序消息数量]{style="font-family:宋体"}]{#struct_0_16315_x4274_x824288911}

[[Challenge]{lang="EN-US"}]{#struct_0_16315_x4274_1385997709}

[[接口是否开启认证的]{style="font-family:宋体"}[challenge-response]{lang="EN-US"}]{#struct_0_16315_x4274_1358746652}[握手功能，取值包括]{style="font-family:宋体"}[Enabled]{lang="EN-US"}[和]{style="font-family:宋体"}[Disabled]{lang="EN-US"}

[[Bypass tunnels]{lang="EN-US"}]{#struct_0_16315_x4274_911108371}

[[接口下配置的用于快速重路由的旁路隧道。如果没有配置任何旁路隧道，则显示为]{style="font-family:宋体"}[None]{lang="EN-US"}]{#struct_0_16315_x4274_x823961231}

[ ]{lang="EN-US"}

::: {#2087967775 .myid}
[]{#_Toc404791050}[]{#struct_0_16315_x4274_x1239910825}[]{#_Toc333936380}[]{#_Toc328505092}[]{#_Toc324951719}

**RSVP \-- RSVP配置命令 \-- display rsvp authentication**

------------------------------------------------------------------------

[**[display rsvp authentication]{lang="EN-US"}**]{#struct_0_16315_x4274_x1608834184}[命令用来显示本地设备与]{style="font-family:
宋体"}[RSVP]{lang="EN-US"}[邻居建立的]{style="font-family:
宋体"}[RSVP SA]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1941817475}

[**[display rsvp authentication]{lang="EN-US"}**[ \[ **from** *ip-address* \] \[ **to** *ip-address* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_16315_x4274_x1028542579}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16315_x4274_228042123}

[[任意视图]{style="font-family:宋体"}]{#struct_0_16315_x4274_x81207277}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x823895695}

[[network-admin]{lang="EN-US"}]{#struct_0_16315_x4274_1528538130}

[[network-operator]{lang="EN-US"}]{#struct_0_16315_x4274_x1523722219}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16315_x4274_869762056}

[[mdc-operator]{lang="EN-US"}]{#struct_0_16315_x4274_1369731597}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16315_x4274_55166975}

[**[from]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_16315_x4274_x1613928059}[：显示认证]{style="font-family:宋体"}[发起节点]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为指定地址的]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为认证发起节点的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[to ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*]{#struct_0_16315_x4274_x483737385}[：显示认证目的节点]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为指定地址的]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[认证目的节点的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_16315_x4274_x355753242}[：]{style="font-family:宋体"}[显示]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[的详细信息。如果没有指定本参数，则显示]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[的简要信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x824092303}

[[开启了]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x948770390}[认证功能后，设备收发]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息时会动态建立]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[。]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[中包含如下信息：]{style="font-family:宋体"}[认证发起节点的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、认证目的节点的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、认证方向、认证类型、认证密钥、认证空闲老化的剩余时间等。其中，认证发起节点和认证目的节点的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址从]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文头或]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息对象中获取，具体获取方法如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-3]{lang="EN-US"}](?2087967775#_Ref330996818)[所示。]{style="font-family:宋体"}

[]{#struct_0_16315_x4274_x1761865350}[[表1-3 ]{lang="EN-US"}[认证发起节点和目的节点]{style="font-family:
黑体"}[IP]{lang="EN-US"}]{#_Ref330996818}[地址]{style="font-family:
黑体"}[的获取方法]{style="font-family:黑体"}

[]{#table_struct_0_x408186259}[[接收或发送的消息类型]{style="font-family:黑体"}]{#struct_0_16315_x4274_x564579991}
:::

[[认证发起节点的]{style="font-family:黑体"}[IP]{lang="EN-US"}]{#struct_0_16315_x4274_1836380398}[地址]{style="font-family:黑体"}

[[认证目的节点的]{style="font-family:黑体"}[IP]{lang="EN-US"}]{#struct_0_16315_x4274_217781559}[地址]{style="font-family:黑体"}

[[Path]{lang="EN-US"}]{#struct_0_16315_x4274_2072151384}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_161002386}[消息]{style="font-family:宋体"}[HOP]{lang="EN-US"}[对象中的地址]{style="font-family:宋体"}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x824026767}[消息]{style="font-family:宋体"}[SESSION]{lang="EN-US"}[对象中的目的地址]{style="font-family:宋体"}

[[PathTear]{lang="EN-US"}]{#struct_0_16315_x4274_1757419324}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_338449611}[消息]{style="font-family:宋体"}[HOP]{lang="EN-US"}[对象中的地址]{style="font-family:宋体"}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_1375688873}[消息]{style="font-family:宋体"}[SESSION]{lang="EN-US"}[对象中的目的地址]{style="font-family:宋体"}

[[PathError]{lang="EN-US"}]{#struct_0_16315_x4274_x1024094234}

[[IP]{lang="EN-US"}]{#struct_0_16315_x4274_x344900932}[报文头中的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[IP]{lang="EN-US"}]{#struct_0_16315_x4274_x117632590}[报文头中的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Resv]{lang="EN-US"}]{#struct_0_16315_x4274_x823699087}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x466805995}[消息]{style="font-family:宋体"}[HOP]{lang="EN-US"}[对象中的地址]{style="font-family:宋体"}

[[IP]{lang="EN-US"}]{#struct_0_16315_x4274_693922006}[报文头中的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[ResvTear]{lang="EN-US"}]{#struct_0_16315_x4274_x1340213418}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x1342539623}[消息]{style="font-family:宋体"}[HOP]{lang="EN-US"}[对象中的地址]{style="font-family:宋体"}

[[IP]{lang="EN-US"}]{#struct_0_16315_x4274_x823633551}[报文头中的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[ResvError]{lang="EN-US"}]{#struct_0_16315_x4274_x1255710866}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x186774486}[消息]{style="font-family:宋体"}[HOP]{lang="EN-US"}[对象中的地址]{style="font-family:宋体"}

[[IP]{lang="EN-US"}]{#struct_0_16315_x4274_1386551169}[报文头中的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[ResvConfirm]{lang="EN-US"}]{#struct_0_16315_x4274_x1061098652}

[[IP]{lang="EN-US"}]{#struct_0_16315_x4274_281384962}[报文头中的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x824223374}[消息]{style="font-family:宋体"}[CONFIRM]{lang="EN-US"}[对象中的地址]{style="font-family:宋体"}

[[ACK]{lang="EN-US"}]{#struct_0_16315_x4274_1752194688}

[[IP]{lang="EN-US"}]{#struct_0_16315_x4274_1421103741}[报文头中的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[IP]{lang="EN-US"}]{#struct_0_16315_x4274_841388438}[报文头中的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Srefresh]{lang="EN-US"}]{#struct_0_16315_x4274_1108996634}

[[IP]{lang="EN-US"}]{#struct_0_16315_x4274_x824157838}[报文头中的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[IP]{lang="EN-US"}]{#struct_0_16315_x4274_238193721}[报文头中的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Hello]{lang="EN-US"}]{#struct_0_16315_x4274_x1885288584}

[[IP]{lang="EN-US"}]{#struct_0_16315_x4274_x977597731}[报文头中的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[IP]{lang="EN-US"}]{#struct_0_16315_x4274_x824354446}[报文头中的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[需要注意的是，执行]{style="font-family:宋体"}**[display rsvp authentication]{lang="EN-US"}**]{#struct_0_16315_x4274_x1359597937}[命令时，如果没有指定]{style="font-family:宋体"}**[from]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*[和]{style="font-family:宋体"}**[to ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*[参数，则显示本地设备与所有邻居建立的]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x322034073}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_1046228485}[显示本地设备与所有邻居建立的]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display rsvp authentication]{lang="EN-US"}]{#struct_0_16315_x4274_810019048}

[From            To              Mode    Type      Key-ID       Expiration]{lang="EN-US"}

[57.10.10.1      57.10.10.2      Receive Interface 000103000000 280s]{lang="EN-US"}

[57.10.10.2      57.10.10.1      Send    Interface 000103000000 280s]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display rsvp authentication]{lang="EN-US"}]{#struct_0_16315_x4274_x1542505062}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x412817019}[[字段]{style="font-family:黑体"}]{#struct_0_16315_x4274_1187699394}

[[描述]{style="font-family:黑体"}]{#struct_0_16315_x4274_x824288910}

[[From]{lang="EN-US"}]{#struct_0_16315_x4274_1386063245}

[[认证发起节点的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_16315_x4274_117703387}[地址]{style="font-family:宋体"}

[[To]{lang="EN-US"}]{#struct_0_16315_x4274_1251387815}

[[认证目的节点的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_16315_x4274_1661334776}[地址]{style="font-family:宋体"}

[[Mode]{lang="EN-US"}]{#struct_0_16315_x4274_x1429330341}

[[认证方向，取值包括：]{style="font-family:宋体"}]{#struct_0_16315_x4274_x164606013}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Receive]{lang="EN-US"}]{#struct_0_16315_x4274_x823961230}[：接收]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[，用来对]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居发送给本地的消息进行认证处理]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Send]{lang="EN-US"}]{#struct_0_16315_x4274_x1239845289}[：发送]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[，用来对本地发送给]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居的消息进行认证处理]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_16315_x4274_1309982205}

[[认证类型，取值包括：]{style="font-family:宋体"}]{#struct_0_16315_x4274_490027405}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Peer]{lang="EN-US"}]{#struct_0_16315_x4274_2062475674}[：表示根据]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居视图下的配置建立的]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_16315_x4274_x762736939}[：表示根据接口视图下的配置建立的]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Global]{lang="EN-US"}]{#struct_0_16315_x4274_x823895694}[：表示根据]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[视图下的配置建立的]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}

[[Key-ID]{lang="EN-US"}]{#struct_0_16315_x4274_1528472594}

[[RSVP SA]{lang="EN-US"}]{#struct_0_16315_x4274_x1472914278}[的密钥]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若为发送]{style="font-family:宋体"}]{#struct_0_16315_x4274_306887129}[RSVP SA]{lang="EN-US"}[，则显示本地的密钥]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若为接收]{style="font-family:宋体"}]{#struct_0_16315_x4274_x1953382796}[RSVP SA]{lang="EN-US"}[，则显示对端发来的密钥]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Expiration]{lang="EN-US"}]{#struct_0_16315_x4274_x824092302}

[[RSVP SA]{lang="EN-US"}]{#struct_0_16315_x4274_x948835926}[空闲老化的剩余时间，单位为秒]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_559789059}[显示所有]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display rsvp authentication verbose]{lang="EN-US"}]{#struct_0_16315_x4274_x824026766}

[From: 20.1.1.1                            To: 4.4.4.9]{lang="EN-US"}

[Mode: Send                                Type: Interface]{lang="EN-US"}

[Challenge: Supported                      Peer: 20.1.1.2]{lang="EN-US"}

[Local key ID: 0x000104000000              Peer key ID: 0x0]{lang="EN-US"}

[Lifetime: 1800 sec                        Expiration time: 1781 sec]{lang="EN-US"}

[Window size: 1]{lang="EN-US"}

[Last sent sequence number:]{lang="EN-US"}

[  5781735195480686593]{lang="EN-US"}

[ ]{lang="EN-US"}

[From: 20.1.1.2                            To: 20.1.1.1]{lang="EN-US"}

[Mode: Receive                             Type: Interface]{lang="EN-US"}

[Challenge: Not configured                 Peer: 20.1.1.2]{lang="EN-US"}

[Local key ID: 0x0                         Peer key ID: 0x000104000000]{lang="EN-US"}

[Lifetime: 1800 sec                        Expiration time: 1798 sec]{lang="EN-US"}

[Window size: 1]{lang="EN-US"}

[Received sequence numbers:]{lang="EN-US"}

[  5781742445385482241]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display rsvp authentication verbose]{lang="EN-US"}]{#struct_0_16315_x4274_1757484860}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x418867690}[[字段]{style="font-family:黑体"}]{#struct_0_16315_x4274_364270110}

[[描述]{style="font-family:黑体"}]{#struct_0_16315_x4274_x501108719}

[[From]{lang="EN-US"}]{#struct_0_16315_x4274_1674089909}

[[认证发起节点的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_16315_x4274_2013862803}[地址]{style="font-family:宋体"}

[[To]{lang="EN-US"}]{#struct_0_16315_x4274_x823699086}

[[认证目的节点的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_16315_x4274_x466871531}[地址]{style="font-family:宋体"}

[[Mode]{lang="EN-US"}]{#struct_0_16315_x4274_665032292}

[[认证方向，取值包括：]{style="font-family:宋体"}]{#struct_0_16315_x4274_x586670668}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Receive]{lang="EN-US"}]{#struct_0_16315_x4274_x825014995}[：接收]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[，用来对]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居发送给本地的消息进行认证处理]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Send]{lang="EN-US"}]{#struct_0_16315_x4274_x905236993}[：发送]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[，]{style="font-family:宋体"} [用来对本地发送给]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居的消息进行认证处理]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_16315_x4274_x1639261715}

[[认证类型，取值包括：]{style="font-family:宋体"}]{#struct_0_16315_x4274_x823633550}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Peer]{lang="EN-US"}]{#struct_0_16315_x4274_x1255776402}[：表示根据]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居视图下的配置建立的]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_16315_x4274_x1063626920}[：表示根据接口视图下的配置建立的]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Global]{lang="EN-US"}]{#struct_0_16315_x4274_x1731853600}[：表示根据]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[视图下的配置建立的]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}

[[Challenge]{lang="EN-US"}]{#struct_0_16315_x4274_679678328}

[[认证的]{style="font-family:宋体"}[challenge-response]{lang="EN-US"}]{#struct_0_16315_x4274_1098090930}[握手状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not configured]{lang="EN-US"}]{#struct_0_16315_x4274_x27109202}[：用于接收]{lang="EN-US" style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[，表示本地没有开启]{lang="EN-US" style="font-family:宋体"}[challenge-response]{lang="EN-US"}[握手功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Configured]{lang="EN-US"}]{#struct_0_16315_x4274_1697311443}[：用于接收]{lang="EN-US" style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[，表示本地开启]{lang="EN-US" style="font-family:宋体"}[了]{style="font-family:宋体"}[challenge-response]{lang="EN-US"}[握手功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[In progress]{lang="EN-US"}]{#struct_0_16315_x4274_976217144}[：本地开启]{lang="EN-US" style="font-family:宋体"}[challenge-response]{lang="EN-US"}[握手功能，向对端发送]{lang="EN-US" style="font-family:宋体"}[Integrity Challenge]{lang="EN-US"}[消息后，正在等待对端回应的]{lang="EN-US" style="font-family:
  宋体"}[Integrity Response]{lang="EN-US"}[消息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Completed]{lang="EN-US"}]{#struct_0_16315_x4274_183297619}[：本地开启]{lang="EN-US" style="font-family:宋体"}[challenge-response]{lang="EN-US"}[握手功能，向对端发送]{lang="EN-US" style="font-family:宋体"}[Integrity Challenge]{lang="EN-US"}[消息后，收到对端回应的]{lang="EN-US" style="font-family:
  宋体"}[Integrity Response]{lang="EN-US"}[消息，并通过认证检查]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed]{lang="EN-US"}]{#struct_0_16315_x4274_1098156466}[：本地开启]{lang="EN-US" style="font-family:宋体"}[challenge-response]{lang="EN-US"}[握手功能，向对端发送]{lang="EN-US" style="font-family:宋体"}[Integrity Challenge]{lang="EN-US"}[消息后，收到对端回应的]{lang="EN-US" style="font-family:
  宋体"}[Integrity Response]{lang="EN-US"}[消息，但未通过认证检查；或本地重复向对端发送三次]{lang="EN-US" style="font-family:宋体"}[Integrity Challenge]{lang="EN-US"}[消息后，仍然没有收到对端回应的合法]{lang="EN-US" style="font-family:
  宋体"}[Integrity Response]{lang="EN-US"}[消息；或对端未开启]{lang="EN-US" style="font-family:宋体"}[challenge-response]{lang="EN-US"}[握手功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Supported]{lang="EN-US"}]{#struct_0_16315_x4274_807027142}[：用于发送]{lang="EN-US" style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[，表示本端]{lang="EN-US" style="font-family:宋体"}[支持]{style="font-family:宋体"}[challenge-response]{lang="EN-US"}[握手功能]{lang="EN-US" style="font-family:宋体"}

[[Peer]{lang="EN-US"}]{#struct_0_16315_x4274_698997305}

[[认证邻居的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_16315_x4274_1747641852}[地址，表示是和哪个邻居建立的]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}

[[Local key ID]{lang="EN-US"}]{#struct_0_16315_x4274_x205998037}

[[本地的]{style="font-family:宋体"}[Key-ID]{lang="EN-US"}]{#struct_0_16315_x4274_1097959858}[，用于发送]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}

[[Peer key ID]{lang="EN-US"}]{#struct_0_16315_x4274_x961855976}

[[对端的]{style="font-family:宋体"}[Key-ID]{lang="EN-US"}]{#struct_0_16315_x4274_859072716}[，用于接收]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}

[[Lifetime]{lang="EN-US"}]{#struct_0_16315_x4274_x703732025}

[[RSVP SA]{lang="EN-US"}]{#struct_0_16315_x4274_1098025394}[的空闲老化时间，单位为秒]{style="font-family:宋体"}

[[Expiration time]{lang="EN-US"}]{#struct_0_16315_x4274_1968158325}

[[RSVP SA]{lang="EN-US"}]{#struct_0_16315_x4274_1889906387}[空闲老化的剩余时间，单位为秒]{style="font-family:宋体"}

[[Window size]{lang="EN-US"}]{#struct_0_16315_x4274_x398762103}

[[最大可允许的乱序消息数量]{style="font-family:宋体"}]{#struct_0_16315_x4274_1098353074}

[[Received sequence numbers]{lang="EN-US"}]{#struct_0_16315_x4274_812055294}

[[收到的消息的序列号，最多可显示]{style="font-family:宋体"}[Window-size]{lang="EN-US"}]{#struct_0_16315_x4274_920598102}[数量的序列号]{style="font-family:宋体"}

[[Last sent sequence number]{lang="EN-US"}]{#struct_0_16315_x4274_x955140236}

[[最后发送的消息的序列号]{style="font-family:宋体"}]{#struct_0_16315_x4274_1098418610}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1086082224}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication challenge]{lang="EN-US"}**]{#struct_0_16315_x4274_x270988225}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication key]{lang="EN-US"}**]{#struct_0_16315_x4274_x986882550}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication lifetime]{lang="EN-US"}**]{#struct_0_16315_x4274_760634419}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication window-size]{lang="EN-US"}**]{#struct_0_16315_x4274_204463221}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ]{lang="EN-US"}[rsvp authentication]{lang="EN-US"}**]{#struct_0_16315_x4274_x2124984734}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp authentication challenge]{lang="EN-US"}**]{#struct_0_16315_x4274_1370166431}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp authentication key]{lang="EN-US"}**]{#struct_0_16315_x4274_x2007830391}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp authentication lifetime]{lang="EN-US"}**]{#struct_0_16315_x4274_1098222002}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp authentication window-size]{lang="EN-US"}**]{#struct_0_16315_x4274_x747802695}

::: {#-1124721692 .myid}
[]{#_Toc404791051}[]{#struct_0_16315_x4274_1824204964}[]{#_Toc333936381}[]{#_Toc328505093}[]{#_Toc324951720}[]{#_Toc329607594}[]{#_Toc329607708}[]{#_Toc330307127}[]{#_Toc329607595}[]{#_Toc329607709}[]{#_Toc330307128}

**RSVP \-- RSVP配置命令 \-- display rsvp lsp**

------------------------------------------------------------------------

[**[display rsvp lsp]{lang="EN-US"}**]{#struct_0_16315_x4274_x1312792136}[命令用来显示]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[建立的]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1465342012}

[**[display rsvp lsp]{lang="EN-US"}**[ \[ **destination** *ip-address* \] \[ **source** *ip-address* \] \[ **tunnel-id** *tunnel-id* \] \[ **lsp-id** *lsp-id* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_16315_x4274_812989734}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16315_x4274_735042010}

[[任意视图]{style="font-family:宋体"}]{#struct_0_16315_x4274_x2122446169}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16315_x4274_2080937530}

[[network-admin]{lang="EN-US"}]{#struct_0_16315_x4274_1098287538}

[[network-operator]{lang="EN-US"}]{#struct_0_16315_x4274_410307975}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16315_x4274_1415718999}

[[mdc-operator]{lang="EN-US"}]{#struct_0_16315_x4274_x1721652843}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16315_x4274_324318117}

[**[destination]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_16315_x4274_168734679}[：显示隧道目的地为指定值的]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为隧道的目的地址。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_16315_x4274_850550977}[：显示隧道源地址为指定值的]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[隧道的源地址，即]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息中]{style="font-family:宋体"}[Session]{lang="EN-US"}[对象的扩展]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[tunnel-id]{lang="EN-US"}**[ *tunnel-id*]{lang="EN-US"}]{#struct_0_16315_x4274_x2125769057}[：显示隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}[为指定值的]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[lsp-id]{lang="EN-US"}**[ *lsp-id*]{lang="EN-US"}]{#struct_0_16315_x4274_x1709840574}[：显示]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为指定值的]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[的]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_16315_x4274_1098615218}**[：]{style="font-family:宋体"}**[显示]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[的详细信息。如果没有指定本参数，则显示]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[的简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x368986565}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_406904133}[显示]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[建立的所有]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display rsvp lsp]{lang="EN-US"}]{#struct_0_16315_x4274_1553773411}

[Destination     Source          Tunnel-ID LSP-ID Direction  Tunnel-name]{lang="EN-US"}

[50.0.0.1        50.0.0.3        0         1      Uni        Sysname_t0]{lang="EN-US"}

[50.0.0.1        50.0.0.3        1         2      Bi-Down    Sysname_t1]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display rsvp lsp ]{lang="EN-US"}]{#struct_0_16315_x4274_1924908765}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x119582865}[[字段]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1223960685}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1361291791}

[[Destination]{lang="EN-US"}]{#struct_0_16315_x4274_1098680754}

[[隧道目的地址]{style="font-family:宋体"}]{#struct_0_16315_x4274_1593792614}

[[Source]{lang="EN-US"}]{#struct_0_16315_x4274_x1227985132}

[[隧道的源地址]{style="font-family:宋体"}]{#struct_0_16315_x4274_1519977487}

[[Tunnel-ID]{lang="EN-US"}]{#struct_0_16315_x4274_124614816}

[[隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_16315_x4274_x2061375343}

[[LSP-ID]{lang="EN-US"}]{#struct_0_16315_x4274_1098090931}

[[LSP ID]{lang="EN-US"}]{#struct_0_16315_x4274_x27043666}

[[Direction]{lang="EN-US"}]{#struct_0_16315_x4274_2113519143}

[[隧道方向，取值包括：]{style="font-family:宋体"}]{#struct_0_16315_x4274_1177889032}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Uni]{lang="EN-US"}]{#struct_0_16315_x4274_x1813439859}[：]{lang="EN-US" style="font-family:宋体"}[Unidirectional CR-LSP]{lang="EN-US"}[，表示单向隧道]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Bi-Down]{lang="EN-US"}]{#struct_0_16315_x4274_x1048658454}[：]{lang="EN-US" style="font-family:宋体"}[Bidirectional downstream CR-LSP]{lang="EN-US"}[，表示双向隧道的正向]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Bi-Up]{lang="EN-US"}]{#struct_0_16315_x4274_1098156467}[：]{lang="EN-US" style="font-family:宋体"}[Bidirectional upstream CR-LSP]{lang="EN-US"}[，表示双向隧道的反向]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}

[[Tunnel-name]{lang="EN-US"}]{#struct_0_16315_x4274_807092678}

[[隧道名称，取值为]{style="font-family:宋体"}*[Sysname]{lang="EN-US"}*[\_t*tunnel-ID*]{lang="EN-US"}]{#struct_0_16315_x4274_289147729}[。其中，]{style="font-family:宋体"}*[Sysname]{lang="EN-US"}*[为设备的名称，可以通过系统视图下的]{style="font-family:宋体"}**[sysname]{lang="EN-US"}**[命令配置；]{style="font-family:宋体"}*[tunnel-ID]{lang="EN-US"}*[为隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[本字段最长为]{style="font-family:宋体"}[80]{lang="EN-US"}]{#struct_0_16315_x4274_x857457244}[个字符，如果隧道名称超过]{style="font-family:宋体"}[80]{lang="EN-US"}[个字符，则超过]{style="font-family:宋体"}[77]{lang="EN-US"}[个字符的部分以"]{style="font-family:宋体"}[\...]{lang="EN-US"}["代替]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_x894189244}[显示]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[建立的所有]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display rsvp lsp verbose]{lang="EN-US"}]{#struct_0_16315_x4274_1098025395}

[Tunnel name: Sysname_t1]{lang="EN-US"}

[Destination: 3.3.3.9                      Source: 1.1.1.9]{lang="EN-US"}

[Tunnel ID: 1                              LSP ID: 5]{lang="EN-US"}

[LSR type: Transit                         Direction: Unidirectional]{lang="EN-US"}

[Setup priority: 7                         Holding priority: 7]{lang="EN-US"}

[In-Label: 1146                            Out-Label: 3]{lang="EN-US"}

[In-Interface: GE1/0/2                    Out-Interface: GE1/0/4]{lang="EN-US"}

[Nexthop: 57.20.20.1                       Exclude-any: 0]{lang="EN-US"}

[Include-Any: 0                            Include-all: 0]{lang="EN-US"}

[Mean rate (CIR): 0.00 kbps                Mean burst size (CBS): 1000.00 bytes]{lang="EN-US"}

[Path MTU: 1500                            Class type: CT0]{lang="EN-US"}

[RRO number: 8]{lang="EN-US"}

[  57.10.10.1/32      Flag: 0x00 (No FRR)]{lang="EN-US"}

[  57.10.10.2/32      Flag: 0x40 (No FRR/In-Int)]{lang="EN-US"}

[  1146               Flag: 0x01 (Global label)]{lang="EN-US"}

[  2.2.2.9/32         Flag: 0x20 (No FRR/Node-ID)]{lang="EN-US"}

[  57.20.20.2/32      Flag: 0x00 (No FRR)]{lang="EN-US"}

[  57.20.20.1/32      Flag: 0x40 (No FRR/In-Int)]{lang="EN-US"}

[  3                  Flag: 0x01 (Global label)]{lang="EN-US"}

[  3.3.3.9/32         Flag: 0x20 (No FRR/Node-ID)]{lang="EN-US"}

[Fast Reroute protection: Ready]{lang="EN-US"}

[  FRR inner label: 3           Bypass tunnel: Tunnel253]{lang="EN-US"}

[ ]{lang="EN-US"}

[Tunnel name: Sysname_t253]{lang="EN-US"}

[Destination: 3.3.3.9                      Source: 2.2.2.9]{lang="EN-US"}

[Tunnel ID: 253                            LSP ID: 17767]{lang="EN-US"}

[LSR type: Ingress                         Direction: Bidirectional, Downstream]{lang="EN-US"}

[Setup priority: 7                         Holding priority: 7]{lang="EN-US"}

[In-Label: -                               Out-Label: 1025]{lang="EN-US"}

[In-Interface: -                           Out-Interface: GE1/0/6]{lang="EN-US"}

[Nexthop: 10.11.112.135                    Exclude-any: 0]{lang="EN-US"}

[Include-Any: 0                            Include-all: 0]{lang="EN-US"}

[Mean rate (CIR): 125.00 kbps              Mean burst size (CBS): 0.00 bytes]{lang="EN-US"}

[Path MTU: 0                               Class type: CT0]{lang="EN-US"}

[RRO number: 8]{lang="EN-US"}

[  10.11.112.140/32   Flag: 0x00 (No FRR)]{lang="EN-US"}

[  10.11.112.135/32   Flag: 0x40 (No FRR/In-Int)]{lang="EN-US"}

[  1025               Flag: 0x01 (Global label)]{lang="EN-US"}

[  5.5.5.9/32         Flag: 0x20 (No FRR/Node-ID)]{lang="EN-US"}

[  57.40.40.3/32      Flag: 0x00 (No FRR)]{lang="EN-US"}

[  57.40.40.1/32      Flag: 0x40 (No FRR/In-Int)]{lang="EN-US"}

[  3                  Flag: 0x01 (Global label)]{lang="EN-US"}

[  3.3.3.9/32         Flag: 0x20 ((No FRR/Node-ID)]{lang="EN-US"}

[Fast Reroute protection: None]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display rsvp lsp verbose]{lang="EN-US"}]{#struct_0_16315_x4274_1968092789}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x117693669}[[字段]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1627112198}

[[描述]{style="font-family:黑体"}]{#struct_0_16315_x4274_x236825412}

[[Tunnel name]{lang="EN-US"}]{#struct_0_16315_x4274_1146133519}

[[隧道名称，取值为]{style="font-family:宋体"}*[Sysname]{lang="EN-US"}*[\_t*tunnel-ID*]{lang="EN-US"}]{#struct_0_16315_x4274_x144716003}[。其中，]{style="font-family:宋体"}*[Sysname]{lang="EN-US"}*[为设备的名称，可以通过系统视图下的]{style="font-family:宋体"}**[sysname]{lang="EN-US"}**[命令配置；]{style="font-family:宋体"}*[tunnel-ID]{lang="EN-US"}*[为隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Destination]{lang="EN-US"}]{#struct_0_16315_x4274_1098353075}

[[隧道目的地址]{style="font-family:宋体"}]{#struct_0_16315_x4274_812120830}

[[Source]{lang="EN-US"}]{#struct_0_16315_x4274_x1856769405}

[[隧道的源地址]{style="font-family:宋体"}]{#struct_0_16315_x4274_1560303033}

[[Tunnel ID]{lang="EN-US"}]{#struct_0_16315_x4274_2003939772}

[[隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_16315_x4274_1628647308}

[[LSP ID]{lang="EN-US"}]{#struct_0_16315_x4274_1098418611}

[[LSP ID]{lang="EN-US"}]{#struct_0_16315_x4274_x1086016688}

[[LSR type]{lang="EN-US"}]{#struct_0_16315_x4274_x1805946262}

[[标签交换路由器类型，取值包括]{style="font-family:宋体"}[Ingress]{lang="EN-US"}]{#struct_0_16315_x4274_x2057923876}[、]{style="font-family:宋体"}[Transit]{lang="EN-US"}[和]{style="font-family:宋体"}[Egress]{lang="EN-US"}

[[Direction]{lang="EN-US"}]{#struct_0_16315_x4274_1977489965}

[[隧道方向，取值包括：]{style="font-family:宋体"}]{#struct_0_16315_x4274_1098222003}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unidirectional]{lang="EN-US"}]{#struct_0_16315_x4274_x747868231}[：表示单向隧道]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Bidirectional, Downstream]{lang="EN-US"}]{#struct_0_16315_x4274_x206063956}[：表示双向隧道的正向]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Bidirectional, Upstream]{lang="EN-US"}]{#struct_0_16315_x4274_x1809155106}[：表示双向隧道的反向]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}

[[Setup priority]{lang="EN-US"}]{#struct_0_16315_x4274_x1138723682}

[[隧道的建立优先级]{style="font-family:宋体"}]{#struct_0_16315_x4274_1098287539}

[[Holding priority]{lang="EN-US"}]{#struct_0_16315_x4274_410242439}

[[隧道的保持优先级]{style="font-family:宋体"}]{#struct_0_16315_x4274_265347536}

[[In-Label]{lang="EN-US"}]{#struct_0_16315_x4274_1643893262}

[[隧道的入标签]{style="font-family:宋体"}]{#struct_0_16315_x4274_679857720}

[[Out-Label]{lang="EN-US"}]{#struct_0_16315_x4274_1098615219}

[[隧道的出标签]{style="font-family:宋体"}]{#struct_0_16315_x4274_x368921029}

[[In-Interface]{lang="EN-US"}]{#struct_0_16315_x4274_x1913350590}

[[隧道的入接口]{style="font-family:宋体"}]{#struct_0_16315_x4274_2061337419}

[[Out-Interface]{lang="EN-US"}]{#struct_0_16315_x4274_1098680755}

[[隧道的出接口]{style="font-family:宋体"}]{#struct_0_16315_x4274_1593727078}

[[Nexthop]{lang="EN-US"}]{#struct_0_16315_x4274_x1987982113}

[[隧道的下一跳地址]{style="font-family:宋体"}]{#struct_0_16315_x4274_11563399}

[[Exclude-any]{lang="EN-US"}]{#struct_0_16315_x4274_x974895724}

[[不接受的亲和属性，即如果链路属性与任意的]{style="font-family:宋体"}[Exclude-any]{lang="EN-US"}]{#struct_0_16315_x4274_1098090928}[亲和属性相同，则不能使用该链路]{style="font-family:宋体"}

[[Include-any]{lang="EN-US"}]{#struct_0_16315_x4274_x26584913}

[[接受的亲和属性，即如果链路属性与任意的]{style="font-family:宋体"}[Include-any]{lang="EN-US"}]{#struct_0_16315_x4274_x193400436}[亲和属性相同，则可以使用该链路]{style="font-family:宋体"}

[[Include-all]{lang="EN-US"}]{#struct_0_16315_x4274_624567846}

[[接受的所有亲和属性，即只有链路属性与所有的]{style="font-family:宋体"}[Include-all]{lang="EN-US"}]{#struct_0_16315_x4274_1098156464}[亲和属性相同时，才能使用该链路]{style="font-family:宋体"}

[[Mean rate (CIR)]{lang="EN-US"}]{#struct_0_16315_x4274_806896070}

[[平均速率，单位为]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}]{#struct_0_16315_x4274_1184525948}

[[Mean burst size (CBS)]{lang="EN-US"}]{#struct_0_16315_x4274_x387793454}

[[平均峰值速率，单位为]{style="font-family:宋体"}[byte/s]{lang="EN-US"}]{#struct_0_16315_x4274_1097959856}

[[Path MTU]{lang="EN-US"}]{#struct_0_16315_x4274_x960938472}

[[路径的最大传输单元]{style="font-family:宋体"}]{#struct_0_16315_x4274_2073525452}

[[Class type]{lang="EN-US"}]{#struct_0_16315_x4274_1098025392}

[[LSP]{lang="EN-US"}]{#struct_0_16315_x4274_1968027253}[流量所属的服务类型]{style="font-family:宋体"}

[[RRO number]{lang="EN-US"}]{#struct_0_16315_x4274_1839170572}

[[RRO]{lang="EN-US"}]{#struct_0_16315_x4274_49091839}[（]{style="font-family:宋体"}[Record Route Object]{lang="EN-US"}[，记录路由对象）的个数]{style="font-family:宋体"}

[[如果]{style="font-family:宋体"}[RRO]{lang="EN-US"}]{#struct_0_16315_x4274_1098353072}[的个数不为零，则接下来显示]{style="font-family:宋体"}[RRO]{lang="EN-US"}[对象中所记录的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址或标签信息]{style="font-family:宋体"}

[[只有]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}]{#struct_0_16315_x4274_811924222}[接口上配置了路由记录功能后，才会显示]{style="font-family:宋体"}[RRO]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Flag]{lang="EN-US"}]{#struct_0_16315_x4274_1941910972}

[[RRO]{lang="EN-US"}]{#struct_0_16315_x4274_388711090}[对象中标记的值及其含义，标记含义的取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No FRR]{lang="EN-US"}]{#struct_0_16315_x4274_1098418608}[：表示没有配置]{lang="EN-US" style="font-family:宋体"}[FRR]{lang="EN-US"}[保护]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FRR Avail]{lang="EN-US"}]{#struct_0_16315_x4274_x1086606511}[：表示]{lang="EN-US" style="font-family:宋体"}[FRR]{lang="EN-US"}[保护可用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[In use]{lang="EN-US"}]{#struct_0_16315_x4274_986458685}[：表示已经发生]{lang="EN-US" style="font-family:宋体"}[FRR]{lang="EN-US"}[切换]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BW]{lang="EN-US"}]{#struct_0_16315_x4274_1098222000}[：表示带宽保护]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Node-Prot]{lang="EN-US"}]{#struct_0_16315_x4274_x747933767}[：表示节点保护]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Node-ID]{lang="EN-US"}]{#struct_0_16315_x4274_x2090689259}[：表示]{lang="EN-US" style="font-family:宋体"}[RRO]{lang="EN-US"}[对象中的地址为节点的]{lang="EN-US" style="font-family:宋体"}[LSR ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[In-Int]{lang="EN-US"}]{#struct_0_16315_x4274_1098287536}[：表示]{lang="EN-US" style="font-family:宋体"}[RRO]{lang="EN-US"}[对象中的地址为入接口的地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Global label]{lang="EN-US"}]{#struct_0_16315_x4274_409914759}[：表示全局标签空间]{lang="EN-US" style="font-family:宋体"}

[[Fast Reroute protection]{lang="EN-US"}]{#struct_0_16315_x4274_816953323}

[[是否绑定了快速重路由的旁路隧道，取值包括：]{style="font-family:宋体"}]{#struct_0_16315_x4274_1098615216}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[None]{lang="EN-US"}]{#struct_0_16315_x4274_x368593349}[：没有绑定快速重路由的旁路隧道]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ready]{lang="EN-US"}]{#struct_0_16315_x4274_1187348218}[：绑定了快速重路由的旁路隧道，此时未进行切换]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_16315_x4274_x1655319874}[：绑定了快速重路由的旁路隧道，此时已进行切换]{lang="EN-US" style="font-family:宋体"}

[[FRR]{lang="EN-US"}]{#struct_0_16315_x4274_1098680752}[[ i]{lang="EN-US" style="font-size:10.5pt"}]{.MsoCommentReference}[nner label]{lang="EN-US"}

[[快速重路由旁路隧道的入口标签，只有绑定了旁路隧道才会显示此字段]{style="font-family:宋体"}]{#struct_0_16315_x4274_1593399398}

[[Bypass tunnel]{lang="EN-US"}]{#struct_0_16315_x4274_x1958920365}

[[旁路隧道的名称，只有绑定了旁路隧道才会显示此字段]{style="font-family:宋体"}]{#struct_0_16315_x4274_1098090929}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x26519377}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display rsvp request]{lang="EN-US"}**]{#struct_0_16315_x4274_x1828815219}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display rsvp reservation]{lang="EN-US"}**]{#struct_0_16315_x4274_x1998336321}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display rsvp sender]{lang="EN-US"}**]{#struct_0_16315_x4274_874869519}

::: {#-2117178311 .myid}
[]{#_Toc404791052}[]{#struct_0_16315_x4274_x1887699102}[]{#_Toc333936382}[]{#_Toc328505094}[]{#_Toc324951721}[]{#_Toc329607597}[]{#_Toc329607711}[]{#_Toc330307130}[]{#_Toc329607598}[]{#_Toc329607712}[]{#_Toc330307131}

**RSVP \-- RSVP配置命令 \-- display rsvp peer**

------------------------------------------------------------------------

[**[display rsvp peer]{lang="EN-US"}**]{#struct_0_16315_x4274_1098156465}[命令用来显示]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_806961606}

[**[display rsvp peer]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \] \[ **ip** *ip-address* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_16315_x4274_x14538565}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1529525025}

[[任意视图]{style="font-family:宋体"}]{#struct_0_16315_x4274_1270338925}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16315_x4274_223973460}

[[network-admin]{lang="EN-US"}]{#struct_0_16315_x4274_x185715185}

[[network-operator]{lang="EN-US"}]{#struct_0_16315_x4274_1533250588}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16315_x4274_x539486892}

[[mdc-operator]{lang="EN-US"}]{#struct_0_16315_x4274_1097959857}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x960872936}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_16315_x4274_864750335}[：显示通过指定接口连接的邻居的信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为]{style="font-family:
宋体"}[接口类型和接口编号。]{style="font-family:宋体"}

[**[ip]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_16315_x4274_x1109006213}[：显示指定]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居的信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为邻居的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_16315_x4274_2069574390}[：显示]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居的详细信息。如果不指定本参数，则显示]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[的简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1147279825}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_575954313}[显示所有]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display rsvp peer]{lang="EN-US"}]{#struct_0_16315_x4274_x205867359}

[Peer             Interface                State    Type     Summary refresh]{lang="EN-US"}

[57.10.10.1       GE1/0/1                  Idle     Active   Enabled]{lang="EN-US"}

[57.20.20.1       GE1/0/2                  Init     Passive  Disabled]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display rsvp peer]{lang="EN-US"}]{#struct_0_16315_x4274_1098025393}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x129848064}[[字段]{style="font-family:黑体"}]{#struct_0_16315_x4274_1967961717}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16315_x4274_x280049855}

[[Peer]{lang="EN-US"}]{#struct_0_16315_x4274_x1594616892}

[[邻居地址]{style="font-family:宋体"}]{#struct_0_16315_x4274_1768017053}

[[Interface]{lang="EN-US"}]{#struct_0_16315_x4274_1286767629}

[[邻居所对应的接口名称]{style="font-family:宋体"}]{#struct_0_16315_x4274_x885730076}

[[State]{lang="EN-US"}]{#struct_0_16315_x4274_1098353073}

[[本地的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_16315_x4274_811989758}[状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Idle]{lang="EN-US"}]{#struct_0_16315_x4274_x1957850039}[：本地未开启]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[扩展功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Init]{lang="EN-US"}]{#struct_0_16315_x4274_x235728424}[：本地开启]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[扩展功能，与邻居进行]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[消息交互未成功或正在进行消息交互]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_16315_x4274_x1516468336}[：本地开启]{style="font-family:宋体"}[Hello]{lang="EN-US"}[扩展功能，与邻居进行]{style="font-family:宋体"}[Hello]{lang="EN-US"}[消息交互成功]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_16315_x4274_x904483903}

[[本端设备在邻居关系中的角色，取值包括：]{style="font-family:宋体"}]{#struct_0_16315_x4274_1098418609}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_16315_x4274_x1086540975}[：表示本端是主动方，主动向邻居发送]{lang="EN-US" style="font-family:宋体"}[Hello Request]{lang="EN-US"}[消息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Passive]{lang="EN-US"}]{#struct_0_16315_x4274_1933122713}[：表示本端是被动方，被动接收邻居发来的]{lang="EN-US" style="font-family:宋体"}[Hello Request]{lang="EN-US"}[消息并回应]{lang="EN-US" style="font-family:宋体"}[Hello Ack]{lang="EN-US"}[消息]{lang="EN-US" style="font-family:宋体"}

[[Summary refresh]{lang="EN-US"}]{#struct_0_16315_x4274_1024654899}

[[邻居是否开启摘要刷新功能，取值包括]{style="font-family:宋体"}[Enabled]{lang="EN-US"}]{#struct_0_16315_x4274_136667449}[和]{style="font-family:宋体"}[Disabled]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_1098222001}[显示所有]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display rsvp peer verbose]{lang="EN-US"}]{#struct_0_16315_x4274_x747999303}

[Peer: 57.10.10.1                          Interface: GE1/0/2]{lang="EN-US"}

[Hello state: Idle                         Hello type: Active]{lang="EN-US"}

[PSB count: 1                              RSB count: 0]{lang="EN-US"}

[Src instance: 0x32e                       Dst instance: 0x0]{lang="EN-US"}

[Summary refresh: Enabled                  Graceful Restart state: Invalid]{lang="EN-US"}

[Peer GR restart time: 0 ms                Peer GR recovery time: 0 ms]{lang="EN-US"}

[ ]{lang="EN-US"}

[Peer: 57.20.20.1                          Interface: GE1/0/4]{lang="EN-US"}

[Hello state: Init                         Hello type: Active]{lang="EN-US"}

[PSB count: 0                              RSB count: 1]{lang="EN-US"}

[Src instance: 0x32e                       Dst instance: 0x0]{lang="EN-US"}

[Summary refresh: Disabled                 Graceful Restart state: Ready]{lang="EN-US"}

[Peer GR restart time: 0 ms                Peer GR recovery time: 0 ms]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display rsvp peer verbose]{lang="EN-US"}]{#struct_0_16315_x4274_214117157}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x127816109}[[字段]{style="font-family:黑体"}]{#struct_0_16315_x4274_x919950456}

[[描述]{style="font-family:黑体"}]{#struct_0_16315_x4274_1098287537}

[[Peer]{lang="EN-US"}]{#struct_0_16315_x4274_409849223}

[[邻居地址]{style="font-family:宋体"}]{#struct_0_16315_x4274_x1144235273}

[[Interface]{lang="EN-US"}]{#struct_0_16315_x4274_x1089841106}

[[邻居所对应的接口名称]{style="font-family:宋体"}]{#struct_0_16315_x4274_1393851015}

[[Hello state]{lang="EN-US"}]{#struct_0_16315_x4274_1285612297}

[[本地的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_16315_x4274_x1891660287}[状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Idle]{lang="EN-US"}]{#struct_0_16315_x4274_1098615217}[：本地未开启]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[扩展功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Init]{lang="EN-US"}]{#struct_0_16315_x4274_x368527813}[：本地开启]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[扩展功能，与邻居进行]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[消息交互未成功或正在进行消息交互]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_16315_x4274_x1191227037}[：本地开启]{style="font-family:宋体"}[Hello]{lang="EN-US"}[扩展功能，与邻居进行]{style="font-family:宋体"}[Hello]{lang="EN-US"}[消息交互成功]{style="font-family:宋体"}

[[Hello type]{lang="EN-US"}]{#struct_0_16315_x4274_1059398170}

[[本端设备在邻居关系中的角色，取值包括：]{style="font-family:宋体"}]{#struct_0_16315_x4274_377539083}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_16315_x4274_1098680753}[：表示本端是主动方，主动向邻居发送]{lang="EN-US" style="font-family:宋体"}[Hello Request]{lang="EN-US"}[消息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Passive]{lang="EN-US"}]{#struct_0_16315_x4274_1593333862}[：表示本端是被动方，被动接收邻居发来的]{lang="EN-US" style="font-family:宋体"}[Hello Request]{lang="EN-US"}[消息并回应]{lang="EN-US" style="font-family:宋体"}[Hello Ack]{lang="EN-US"}[消息]{lang="EN-US" style="font-family:宋体"}

[[PSB count]{lang="EN-US"}]{#struct_0_16315_x4274_x1553925376}

[[邻居对应的路径状态块的数量]{style="font-family:宋体"}]{#struct_0_16315_x4274_622191747}

[[RSB count]{lang="EN-US"}]{#struct_0_16315_x4274_613917288}

[[邻居对应的预留状态块的数量]{style="font-family:宋体"}]{#struct_0_16315_x4274_1098090926}

[[Src instance]{lang="EN-US"}]{#struct_0_16315_x4274_x27240273}

[[发送给邻居的]{style="font-family:宋体"}]{#struct_0_16315_x4274_x1142428746}[Hello]{lang="FR"}[消息中携带]{style="font-family:宋体"}[的]{style="font-family:宋体"}[Src ]{lang="EN-US"}[instance]{lang="FR"}[，即本地设备的]{style="font-family:
  宋体"}[instance]{lang="FR"}

[[Dst instance]{lang="EN-US"}]{#struct_0_16315_x4274_375434585}

[[最后一次接收到邻居发来的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_16315_x4274_2085737761}[消息中的]{style="font-family:宋体"}[Src Instance]{lang="EN-US"}[，即邻居的]{style="font-family:宋体"}[instance]{lang="EN-US"}

[[Summary refresh]{lang="EN-US"}]{#struct_0_16315_x4274_1098156462}

[[邻居是否开启摘要刷新功能，取值包括]{style="font-family:宋体"}[Enabled]{lang="EN-US"}]{#struct_0_16315_x4274_806764998}[和]{style="font-family:宋体"}[Disabled]{lang="EN-US"}

[[Graceful Restart state]{lang="EN-US"}]{#struct_0_16315_x4274_1746484446}

[[邻居的]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_16315_x4274_1806463201}[状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid]{lang="EN-US"}]{#struct_0_16315_x4274_x1604145461}[：邻居没有]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力，或本地没有开启]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ready]{lang="EN-US"}]{#struct_0_16315_x4274_1097959854}[：邻居具有]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[能力]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Restarting]{lang="EN-US"}]{#struct_0_16315_x4274_x961069544}[：邻居正在重启]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Recovering]{lang="EN-US"}]{#struct_0_16315_x4274_x1057492961}[：邻居正在恢复]{lang="EN-US" style="font-family:宋体"}

[[Peer GR restart time]{lang="EN-US"}]{#struct_0_16315_x4274_1517620562}

[[邻居的]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_16315_x4274_1098025390}[重启时间间隔，单位为毫秒]{style="font-family:宋体"}

[[Peer GR recovery time]{lang="EN-US"}]{#struct_0_16315_x4274_1967896181}

[[邻居的]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_16315_x4274_1649610350}[恢复时间间隔，单位为毫秒]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1354732780 .myid}
[]{#_Toc404791053}[]{#struct_0_16315_x4274_x1311226992}[]{#_Toc333936383}[]{#_Toc328505095}[]{#_Toc324951722}[]{#_Toc329607600}[]{#_Toc329607714}[]{#_Toc330307133}[]{#_Toc329607601}[]{#_Toc329607715}[]{#_Toc330307134}[]{#_Toc329607602}[]{#_Toc329607716}[]{#_Toc330307135}

**RSVP \-- RSVP配置命令 \-- display rsvp request**

------------------------------------------------------------------------

[**[display rsvp request]{lang="EN-US"}**]{#struct_0_16315_x4274_x2097751014}[命令用来显示向上游设备发送的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[资源预留请求的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x906969143}

[**[display rsvp request ]{lang="EN-US"}**[\[ **destination** *ip-address* \] \[ **source** *ip-address* \] \[ **tunnel-id** *tunnel-id* \] \[ **prevhop** *ip-address* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_16315_x4274_1098353070}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16315_x4274_811793150}

[[任意视图]{style="font-family:宋体"}]{#struct_0_16315_x4274_597863226}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1910567423}

[[network-admin]{lang="EN-US"}]{#struct_0_16315_x4274_743505749}

[[network-operator]{lang="EN-US"}]{#struct_0_16315_x4274_x1609065013}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16315_x4274_x297915977}

[[mdc-operator]{lang="EN-US"}]{#struct_0_16315_x4274_x752057258}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1729773212}

[**[destination]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_16315_x4274_x763987920}[：显示隧道目的地址为指定值的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[资源预留请求信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[隧道的目的地。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_16315_x4274_1098418606}[：显示隧道源地址为指定值的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[资源预留请求信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[隧道的源地址，即]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息中]{style="font-family:宋体"}[Session]{lang="EN-US"}[对象的扩展]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[tunnel-id]{lang="EN-US"}**[ *tunnel-id*]{lang="EN-US"}]{#struct_0_16315_x4274_x1086213295}[：显示隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}[为指定值的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[资源预留请求信息。]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*[为隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[prevhop]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_16315_x4274_1871015869}[：显示向指定上游设备发送的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[资源预留请求信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[资源预留请求信息的目的设备的地址，即隧道的前一跳地址。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_16315_x4274_x734686498}[：显示向上游设备发送的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[资源预留请求的详细信息。如果不指定本参数，则显示向上游设备发送的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[资源预留请求的简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x7603801}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_524960390}[显示所有向上游设备发送的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[资源预留请求的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display rsvp request]{lang="EN-US"}]{#struct_0_16315_x4274_1686224637}

[Destination     Source          Tunnel-ID Previous-hop      Style]{lang="EN-US"}

[3.3.3.9         1.1.1.9         1         57.10.10.1        SE]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[display rsvp request]{lang="EN-US"}]{#struct_0_16315_x4274_1565411870}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x130357941}[[字段]{style="font-family:黑体"}]{#struct_0_16315_x4274_1098221998}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16315_x4274_1553458251}

[[Destination]{lang="EN-US"}]{#struct_0_16315_x4274_726518113}

[[隧道目的地址]{style="font-family:宋体"}]{#struct_0_16315_x4274_154185413}

[[Source]{lang="EN-US"}]{#struct_0_16315_x4274_x1187286940}

[[隧道的源地址]{style="font-family:宋体"}]{#struct_0_16315_x4274_x1619531982}

[[Tunnel-ID]{lang="EN-US"}]{#struct_0_16315_x4274_1098287534}

[[隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_16315_x4274_410045831}

[[Previous-hop]{lang="EN-US"}]{#struct_0_16315_x4274_1543353412}

[[前一跳地址]{style="font-family:宋体"}]{#struct_0_16315_x4274_1779617628}

[[Style]{lang="EN-US"}]{#struct_0_16315_x4274_1830321097}

[[资源预留风格，取值包括：]{style="font-family:宋体"}]{#struct_0_16315_x4274_x1761238884}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SE]{lang="EN-US"}]{#struct_0_16315_x4274_1098615214}[：共享显式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FF]{lang="EN-US"}]{#struct_0_16315_x4274_x368724421}[：固定过滤器]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_1213133781}[显示所有向上游设备发送的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[资源预留请求的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display rsvp request verbose]{lang="EN-US"}]{#struct_0_16315_x4274_116893485}

[Destination: 3.3.3.9                      Source: 1.1.1.9]{lang="EN-US"}

[Tunnel ID: 1                              Style: SE]{lang="EN-US"}

[Previous hop: 57.10.10.1                  Previous hop LIH: 0xf0008]{lang="EN-US"}

[Sent message epoch: 0                     Sent message ID: 0]{lang="EN-US"}

[Out-Interface: GE1/0/2                    Refresh interval: 30000 ms]{lang="EN-US"}

[Unknown object number: 0]{lang="EN-US"}

[Flow descriptor 1:]{lang="EN-US"}

[  Flow specification:]{lang="EN-US"}

[    Mean rate (CIR): 50.00 kbps           Mean burst size (CBS): 1000.00 bytes]{lang="EN-US"}

[    Path MTU: 1500                        QoS service: Controlled-Load]{lang="EN-US"}

[  Filter specification 1:]{lang="EN-US"}

[    Sender address: 1.1.1.9               LSP ID: 23]{lang="EN-US"}

[    Label: 1110]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[display rsvp request verbose]{lang="EN-US"}]{#struct_0_16315_x4274_x641784554}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x103160170}[[字段]{style="font-family:黑体"}]{#struct_0_16315_x4274_1098680750}

[[描述]{style="font-family:黑体"}]{#struct_0_16315_x4274_1593530470}

[[Destination]{lang="EN-US"}]{#struct_0_16315_x4274_336943110}

[[隧道目的地址]{style="font-family:宋体"}]{#struct_0_16315_x4274_821084265}

[[Source]{lang="EN-US"}]{#struct_0_16315_x4274_x1705822587}

[[隧道的源地址]{style="font-family:宋体"}]{#struct_0_16315_x4274_1023843365}

[[Tunnel ID]{lang="EN-US"}]{#struct_0_16315_x4274_1098090927}

[[隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_16315_x4274_x27174737}

[[Style]{lang="EN-US"}]{#struct_0_16315_x4274_x655799896}

[[资源预留风格，取值包括：]{style="font-family:宋体"}]{#struct_0_16315_x4274_1460544239}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SE]{lang="EN-US"}]{#struct_0_16315_x4274_273425812}[：共享显式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FF]{lang="EN-US"}]{#struct_0_16315_x4274_x1240289999}[：固定过滤器]{lang="EN-US" style="font-family:宋体"}

[[Previous hop]{lang="EN-US"}]{#struct_0_16315_x4274_1098156463}

[[前一跳地址]{style="font-family:宋体"}]{#struct_0_16315_x4274_806830534}

[[Previous hop LIH]{lang="EN-US"}]{#struct_0_16315_x4274_x1573276479}

[[前一跳设备的逻辑接口索引]{style="font-family:宋体"}]{#struct_0_16315_x4274_959004974}

[[Sent message epoch]{lang="EN-US"}]{#struct_0_16315_x4274_929520837}

[[发送消息携带的]{style="font-family:宋体"}[Message ID Object]{lang="EN-US"}]{#struct_0_16315_x4274_x2121084512}[中]{style="font-family:宋体"}[Epoch]{lang="EN-US"}[字段的值]{style="font-family:宋体"}

[[Sent message ID]{lang="EN-US"}]{#struct_0_16315_x4274_1097959855}

[[发送消息中的]{style="font-family:宋体"}[Message ID]{lang="EN-US"}]{#struct_0_16315_x4274_x961004008}

[[Out-Interface]{lang="EN-US"}]{#struct_0_16315_x4274_2003366604}

[[消息的出接口名称]{style="font-family:宋体"}]{#struct_0_16315_x4274_2038235132}

[[Refresh interval]{lang="EN-US"}]{#struct_0_16315_x4274_1098025391}

[[路径和预留消息的刷新时间间隔，单位为毫秒]{style="font-family:宋体"}]{#struct_0_16315_x4274_1967830645}

[[Unknown object number]{lang="EN-US"}]{#struct_0_16315_x4274_x659860792}

[[无法识别的]{style="font-family:宋体"}[Object]{lang="EN-US"}]{#struct_0_16315_x4274_x757075179}[的个数]{style="font-family:宋体"}

[[Flow descriptor]{lang="EN-US"}]{#struct_0_16315_x4274_x1972786532}

[[流量信息描述]{style="font-family:宋体"}]{#struct_0_16315_x4274_1098353071}

[[Flow specification]{lang="EN-US"}]{#struct_0_16315_x4274_811858686}

[[流量规格信息]{style="font-family:宋体"}]{#struct_0_16315_x4274_326895517}

[[Mean rate (CIR)]{lang="EN-US"}]{#struct_0_16315_x4274_x1340174031}

[[平均速率，单位为]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}]{#struct_0_16315_x4274_x530493644}

[[Mean burst size (CBS)]{lang="EN-US"}]{#struct_0_16315_x4274_1098418607}

[[平均峰值速率，单位为]{style="font-family:宋体"}[byte/s]{lang="EN-US"}]{#struct_0_16315_x4274_x1086147759}

[[Path MTU]{lang="EN-US"}]{#struct_0_16315_x4274_x70212273}

[[路径的最大传输单元]{style="font-family:宋体"}]{#struct_0_16315_x4274_x129628247}

[[QoS service]{lang="EN-US"}]{#struct_0_16315_x4274_1098221999}

[[QoS]{lang="EN-US"}]{#struct_0_16315_x4274_1553392715}[业务类型，取值包括]{style="font-family:宋体"}[Controlled-Load]{lang="EN-US"}[和]{style="font-family:宋体"}[Guaranteed]{lang="EN-US"}

[[Filter specification]{lang="EN-US"}]{#struct_0_16315_x4274_1904360444}

[[过滤规格信息]{style="font-family:宋体"}]{#struct_0_16315_x4274_1036395529}

[[Sender address]{lang="EN-US"}]{#struct_0_16315_x4274_1098287535}

[[发送者地址，用来标识隧道的源端]{style="font-family:宋体"}]{#struct_0_16315_x4274_409980295}

[[LSP ID]{lang="EN-US"}]{#struct_0_16315_x4274_x772056823}

[[LSP ID]{lang="EN-US"}]{#struct_0_16315_x4274_1098615215}

[[Label]{lang="EN-US"}]{#struct_0_16315_x4274_x368658885}

[[正向]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_16315_x4274_832076982}[的入标签]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_376661719}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display rsvp lsp]{lang="EN-US"}**]{#struct_0_16315_x4274_x1266385983}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display rsvp reservation]{lang="EN-US"}**]{#struct_0_16315_x4274_136739318}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display rsvp sender]{lang="EN-US"}**]{#struct_0_16315_x4274_1098680751}

::: {#1752354919 .myid}
[]{#_Toc240171970}[]{#_Toc404791054}[]{#struct_0_16315_x4274_1593464934}[]{#_Toc333936384}[]{#_Toc328505096}[]{#_Toc324951723}[]{#_Toc329607604}[]{#_Toc329607718}[]{#_Toc330307137}[]{#_Toc329607605}[]{#_Toc329607719}[]{#_Toc330307138}

**RSVP \-- RSVP配置命令 \-- display rsvp reservation**

------------------------------------------------------------------------

[**[display rsvp reservation]{lang="EN-US"}**]{#struct_0_16315_x4274_x1955386729}[命令用来显示]{style="font-family:
宋体"}[RSVP]{lang="EN-US"}[资源预留状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x654079302}

[**[display rsvp reservation]{lang="EN-US"}**[ \[ **destination** *ip-address* \] \[ **source** *ip-address* \] \[ **tunnel-id** *tunnel-id* \] \[ **nexthop** *ip-address* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_16315_x4274_x104062495}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x621803713}

[[任意视图]{style="font-family:宋体"}]{#struct_0_16315_x4274_698769325}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16315_x4274_788849705}

[[network-admin]{lang="EN-US"}]{#struct_0_16315_x4274_x770000172}

[[network-operator]{lang="EN-US"}]{#struct_0_16315_x4274_x1630792425}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16315_x4274_x2008851745}

[[mdc-operator]{lang="EN-US"}]{#struct_0_16315_x4274_x1856293694}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1291346193}

[**[destination]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_16315_x4274_x1525399041}[：显示隧道目的地址为指定值的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[资源预留状态信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[隧道的目的地。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_16315_x4274_1431640861}[：显示隧道源地址为指定值的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[资源预留状态信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[隧道的源地址，即]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息中]{style="font-family:宋体"}[Session]{lang="EN-US"}[对象的扩展]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[tunnel-id]{lang="EN-US"}**[ *tunnel-id*]{lang="EN-US"}]{#struct_0_16315_x4274_x546040621}[：显示隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}[为指定值的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[资源预留状态信息。]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[nexthop]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_16315_x4274_353701995}[：显示根据从指定下游设备接收到的]{style="font-family:宋体"}[Resv]{lang="EN-US"}[消息创建的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[资源预留状态信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[发送资源预留状态信息设备的地址，即隧道下一跳地址。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_16315_x4274_x1618985774}[：显示]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[资源预留状态的详细信息。如果不指定本参数，则显示]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[资源预留状态的简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1630726889}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_x1562525620}[显示所有]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[资源预留状态的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display rsvp reservation]{lang="EN-US"}]{#struct_0_16315_x4274_1313810583}

[Destination     Source          Tunnel-ID Nexthop           Style]{lang="EN-US"}

[3.3.3.9         1.1.1.9         1         57.20.20.1        SE]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[display rsvp reservation]{lang="EN-US"}]{#struct_0_16315_x4274_x122747867}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x105759015}[[字段]{style="font-family:黑体"}]{#struct_0_16315_x4274_x742028066}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1128286913}

[[Destination]{lang="EN-US"}]{#struct_0_16315_x4274_655848182}

[[隧道目的地址]{style="font-family:宋体"}]{#struct_0_16315_x4274_x1630923497}

[[Source]{lang="EN-US"}]{#struct_0_16315_x4274_x1712686094}

[[隧道的源地址]{style="font-family:宋体"}]{#struct_0_16315_x4274_983810154}

[[Tunnel-ID]{lang="EN-US"}]{#struct_0_16315_x4274_1221312109}

[[隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_16315_x4274_x1364845255}

[[Nexthop]{lang="EN-US"}]{#struct_0_16315_x4274_1561314190}

[[下一跳地址]{style="font-family:宋体"}]{#struct_0_16315_x4274_x1630857961}

[[Style]{lang="EN-US"}]{#struct_0_16315_x4274_1084815786}

[[资源预留风格，取值包括：]{style="font-family:宋体"}]{#struct_0_16315_x4274_1727708537}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SE]{lang="EN-US"}]{#struct_0_16315_x4274_1669388371}[：共享显式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FF]{lang="EN-US"}]{#struct_0_16315_x4274_x1971409129}[：固定过滤器]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_1905426556}[显示所有]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[资源预留状态的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display rsvp reservation verbose]{lang="EN-US"}]{#struct_0_16315_x4274_x1630530281}

[Destination: 3.3.3.9                      Source: 1.1.1.9]{lang="EN-US"}

[Tunnel ID: 1                              Style: SE]{lang="EN-US"}

[Nexthop: 57.20.20.1                       Nexthop LIH: 0x35]{lang="EN-US"}

[Received message epoch: 0                 Received message ID: 0]{lang="EN-US"}

[In-Interface: GE1/0/4                     Unknown object number: 0]{lang="EN-US"}

[Flow descriptor 1:]{lang="EN-US"}

[  Flow specification:]{lang="EN-US"}

[    Mean rate (CIR): 50.00 kbps           Mean burst size (CBS): 1000.00 bytes]{lang="EN-US"}

[    Path MTU: 1500                        QoS service: Controlled-Load]{lang="EN-US"}

[  Filter specification 1:]{lang="EN-US"}

[    Sender address: 1.1.1.9               LSP ID: 23]{lang="EN-US"}

[    Label: 3]{lang="EN-US"}

[    RRO number: 3]{lang="EN-US"}

[      57.20.20.1/32      Flag: 0x40 (No FRR/In-Int)]{lang="EN-US"}

[      3                  Flag: 0x01 (Global label)]{lang="EN-US"}

[      3.3.3.9/32         Flag: 0x20 (No FRR/Node-ID)]{lang="EN-US"}

[[表1-13 ]{lang="EN-US"}[display rsvp reservation verbose]{lang="EN-US"}]{#struct_0_16315_x4274_x1366328033}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x105999803}[[字段]{style="font-family:黑体"}]{#struct_0_16315_x4274_x662512410}

[[描述]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1156773287}

[[Destination]{lang="EN-US"}]{#struct_0_16315_x4274_x1630464745}

[[隧道目的地址]{style="font-family:宋体"}]{#struct_0_16315_x4274_267915681}

[[Source]{lang="EN-US"}]{#struct_0_16315_x4274_x1895767097}

[[隧道的源地址]{style="font-family:宋体"}]{#struct_0_16315_x4274_x424739627}

[[Tunnel ID]{lang="EN-US"}]{#struct_0_16315_x4274_x1411900688}

[[隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_16315_x4274_x2111498594}

[[Style]{lang="EN-US"}]{#struct_0_16315_x4274_x1630661353}

[[资源预留风格，取值包括：]{style="font-family:宋体"}]{#struct_0_16315_x4274_x220518289}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SE]{lang="EN-US"}]{#struct_0_16315_x4274_x999119335}[：共享显式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FF]{lang="EN-US"}]{#struct_0_16315_x4274_744623150}[：固定过滤器]{style="font-family:宋体"}

[[Nexthop]{lang="EN-US"}]{#struct_0_16315_x4274_939695785}

[[下一跳地址]{style="font-family:宋体"}]{#struct_0_16315_x4274_x1630595817}

[[Nexthop LIH]{lang="EN-US"}]{#struct_0_16315_x4274_x1519762415}

[[与下一跳对应的本地出接口的逻辑接口索引]{style="font-family:宋体"}]{#struct_0_16315_x4274_x679332024}

[[Received message epoch]{lang="EN-US"}]{#struct_0_16315_x4274_x1460868239}

[[接收消息携带的]{style="font-family:宋体"}[Message ID Object]{lang="EN-US"}]{#struct_0_16315_x4274_x1969350327}[中]{style="font-family:宋体"}[Epoch]{lang="EN-US"}[字段的值]{style="font-family:宋体"}

[[Received message ID]{lang="EN-US"}]{#struct_0_16315_x4274_x1630268137}

[[接收消息中的]{style="font-family:宋体"}[Message ID]{lang="EN-US"}]{#struct_0_16315_x4274_x1244136743}

[[In-Interface]{lang="EN-US"}]{#struct_0_16315_x4274_x1190561948}

[[消息的入接口名称]{style="font-family:宋体"}]{#struct_0_16315_x4274_x1715138209}

[[Unknown object number]{lang="EN-US"}]{#struct_0_16315_x4274_x1689524105}

[[无法识别的]{style="font-family:宋体"}[Object]{lang="EN-US"}]{#struct_0_16315_x4274_x1630202601}[的个数]{style="font-family:宋体"}

[[Flow descriptor]{lang="EN-US"}]{#struct_0_16315_x4274_x373926604}

[[流量信息描述]{style="font-family:宋体"}]{#struct_0_16315_x4274_181976710}

[[Flow specification]{lang="EN-US"}]{#struct_0_16315_x4274_x475170465}

[[流量规格信息]{style="font-family:宋体"}]{#struct_0_16315_x4274_x1630792424}

[[Mean rate (CIR)]{lang="EN-US"}]{#struct_0_16315_x4274_x442767804}

[[平均速率，单位为]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}]{#struct_0_16315_x4274_882887274}

[[Mean burst size (CBS)]{lang="EN-US"}]{#struct_0_16315_x4274_x879085653}

[[平均峰值速率，单位为]{style="font-family:宋体"}[byte/s]{lang="EN-US"}]{#struct_0_16315_x4274_x1630726888}

[[Path MTU]{lang="EN-US"}]{#struct_0_16315_x4274_1166357735}

[[路径的最大传输单元]{style="font-family:宋体"}]{#struct_0_16315_x4274_298812463}

[[QoS service]{lang="EN-US"}]{#struct_0_16315_x4274_586956025}

[[QoS]{lang="EN-US"}]{#struct_0_16315_x4274_x1630923496}[业务类型，取值包括]{style="font-family:宋体"}[Controlled-Load]{lang="EN-US"}[和]{style="font-family:宋体"}[Guaranteed]{lang="EN-US"}

[[Filter specification]{lang="EN-US"}]{#struct_0_16315_x4274_1016197261}

[[过滤规格信息]{style="font-family:宋体"}]{#struct_0_16315_x4274_358840739}

[[Sender address]{lang="EN-US"}]{#struct_0_16315_x4274_169856317}

[[发送者地址，用来标识隧道的源端]{style="font-family:宋体"}]{#struct_0_16315_x4274_x1630857960}

[[LSP ID]{lang="EN-US"}]{#struct_0_16315_x4274_x1644067569}

[[LSP ID]{lang="EN-US"}]{#struct_0_16315_x4274_x1414142729}

[[Label]{lang="EN-US"}]{#struct_0_16315_x4274_480824405}

[[正向]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_16315_x4274_x1630530280}[的出标签]{style="font-family:宋体"}

[[RRO number]{lang="EN-US"}]{#struct_0_16315_x4274_199755908}

[[RRO]{lang="EN-US"}]{#struct_0_16315_x4274_2092973727}[（]{style="font-family:宋体"}[Record Route Object]{lang="EN-US"}[，记录路由对象）的个数]{style="font-family:宋体"}

[[如果]{style="font-family:宋体"}[RRO]{lang="EN-US"}]{#struct_0_16315_x4274_x1630464744}[的个数不为零，则接下来显示]{style="font-family:宋体"}[RRO]{lang="EN-US"}[对象中所记录的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址或标签信息]{style="font-family:宋体"}

[[只有]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}]{#struct_0_16315_x4274_x1298168260}[接口上配置了路由记录功能后，才会显示]{style="font-family:宋体"}[RRO]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Flag]{lang="EN-US"}]{#struct_0_16315_x4274_1497144793}

[[RRO]{lang="EN-US"}]{#struct_0_16315_x4274_x831968525}[对象中标记的值及其含义，标记含义的取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No FRR]{lang="EN-US"}]{#struct_0_16315_x4274_x1630661352}[：表示没有配置]{lang="EN-US" style="font-family:宋体"}[FRR]{lang="EN-US"}[保护]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FRR Avail]{lang="EN-US"}]{#struct_0_16315_x4274_x1786602230}[：表示]{lang="EN-US" style="font-family:宋体"}[FRR]{lang="EN-US"}[保护可用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[In use]{lang="EN-US"}]{#struct_0_16315_x4274_1080611728}[：表示已经发生]{lang="EN-US" style="font-family:宋体"}[FRR]{lang="EN-US"}[切换]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BW]{lang="EN-US"}]{#struct_0_16315_x4274_x1630595816}[：表示带宽保护]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Node-Prot]{lang="EN-US"}]{#struct_0_16315_x4274_46321526}[：表示节点保护]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Node-ID]{lang="EN-US"}]{#struct_0_16315_x4274_1109323248}[：表示]{lang="EN-US" style="font-family:宋体"}[RRO]{lang="EN-US"}[对象中的地址为节点的]{lang="EN-US" style="font-family:宋体"}[LSR ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[In-Int]{lang="EN-US"}]{#struct_0_16315_x4274_x912543890}[：表示]{lang="EN-US" style="font-family:宋体"}[RRO]{lang="EN-US"}[对象中的地址为入接口的地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Global label]{lang="EN-US"}]{#struct_0_16315_x4274_x1630268136}[：表示全局标签空间]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1484746612}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display rsvp lsp]{lang="EN-US"}**]{#struct_0_16315_x4274_x482451384}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display rsvp request]{lang="EN-US"}**]{#struct_0_16315_x4274_x1142638195}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display rsvp sender]{lang="EN-US"}**]{#struct_0_16315_x4274_x164883669}

::: {#-984807050 .myid}
[]{#_Toc404791055}[]{#struct_0_16315_x4274_x1104314473}[]{#_Toc333936385}[]{#_Toc328505097}[]{#_Toc324951724}

**RSVP \-- RSVP配置命令 \-- display rsvp sender**

------------------------------------------------------------------------

[**[display rsvp sender]{lang="EN-US"}**]{#struct_0_16315_x4274_1658600082}[命令用来显示]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[路径状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1630202600}

[**[display rsvp sender]{lang="EN-US"}**[ \[ **destination** *ip-address* \] \[ **source** *ip-address* \] \[ **tunnel-id** *tunnel-id* \] \[ **lsp-id** *lsp-id* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_16315_x4274_x1940010545}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x609505493}

[[任意视图]{style="font-family:宋体"}]{#struct_0_16315_x4274_1206663248}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16315_x4274_2059775753}

[[network-admin]{lang="EN-US"}]{#struct_0_16315_x4274_x1116286611}

[[network-operator]{lang="EN-US"}]{#struct_0_16315_x4274_1674271717}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16315_x4274_21872814}

[[mdc-operator]{lang="EN-US"}]{#struct_0_16315_x4274_856021997}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1630792427}

[**[destination]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_16315_x4274_x846052331}[：显示隧道目的地址为指定值的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[路径状态信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[隧道的目的地。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_16315_x4274_1744643893}[：显示隧道源地址为指定值的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[路径状态信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[隧道的源地址，即]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息中]{style="font-family:宋体"}[Session]{lang="EN-US"}[对象的扩展]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[tunnel-id]{lang="EN-US"}**[ *tunnel-id*]{lang="EN-US"}]{#struct_0_16315_x4274_x1184248063}[：显示隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}[为指定值的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[路径状态信息。]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[lsp-id]{lang="EN-US"}**[ *lsp-id*]{lang="EN-US"}]{#struct_0_16315_x4274_x1363127681}[：显示]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为指定值的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[路径状态信息。]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[的]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_16315_x4274_x1512716929}[：显示]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[路径状态的详细信息。如果不指定本参数，则显示]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[路径状态的简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1488205503}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_302592281}[显示所有]{style="font-family:宋体"}[RSVP ]{lang="EN-US"}[路径状态的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display rsvp sender]{lang="EN-US"}]{#struct_0_16315_x4274_x1630726891}

[Destination     Source          Tunnel-ID LSP-ID  Style     Bitrate]{lang="EN-US"}

[3.3.3.9         1.1.1.9         1         5       SE        0.00]{lang="EN-US"}

[3.3.3.9         2.2.2.9         253       17767   SE        125.00]{lang="EN-US"}

[[表1-14 ]{lang="EN-US"}[display rsvp sender]{lang="EN-US"}]{#struct_0_16315_x4274_x1206360796}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x113959822}[[字段]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1990871968}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1760992948}

[[Destination]{lang="EN-US"}]{#struct_0_16315_x4274_879413955}

[[隧道目的地址]{style="font-family:宋体"}]{#struct_0_16315_x4274_x1076078362}

[[Source]{lang="EN-US"}]{#struct_0_16315_x4274_1413954388}

[[隧道的源地址]{style="font-family:宋体"}]{#struct_0_16315_x4274_x1630923499}

[[Tunnel-ID]{lang="EN-US"}]{#struct_0_16315_x4274_x906117040}

[[隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_16315_x4274_142298796}

[[LSP-ID]{lang="EN-US"}]{#struct_0_16315_x4274_1509473824}

[[LSP ID]{lang="EN-US"}]{#struct_0_16315_x4274_x47927604}

[[Style]{lang="EN-US"}]{#struct_0_16315_x4274_x1630857963}

[[资源预留风格，取值包括：]{style="font-family:宋体"}]{#struct_0_16315_x4274_x2047352096}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SE]{lang="EN-US"}]{#struct_0_16315_x4274_x538847597}[：共享显式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FF]{lang="EN-US"}]{#struct_0_16315_x4274_x926513842}[：固定过滤器]{style="font-family:宋体"}

[[Bitrate]{lang="EN-US"}]{#struct_0_16315_x4274_x1669243122}

[[隧道带宽，单位为]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}]{#struct_0_16315_x4274_1088684792}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_x1630530283}[显示所有]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[路径状态的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display rsvp sender verbose]{lang="EN-US"}]{#struct_0_16315_x4274_x1630661355}

[Destination: 3.3.3.9                      Source: 1.1.1.9]{lang="EN-US"}

[Tunnel ID: 1                              Style: SE]{lang="EN-US"}

[Sender address: 1.1.1.9                   LSP ID: 5]{lang="EN-US"}

[Setup priority: 7                         Holding priority: 7]{lang="EN-US"}

[FRR desired: Yes                          BW protection desired: Yes]{lang="EN-US"}

[Received upstream label: 1051             Sent upstream label: 1051]{lang="EN-US"}

[Previous hop: 57.10.10.1                  Previous hop LIH: 0xf0008]{lang="EN-US"}

[Mean rate (CIR): 0.00 kbps                Mean burst size (CBS): 1000.00 bytes]{lang="EN-US"}

[MTU: 1500                                 Qos service: Controlled-Load]{lang="EN-US"}

[Received message epoch: 0                 Received message ID: 0]{lang="EN-US"}

[Sent message epoch: 0                     Sent message ID: 0]{lang="EN-US"}

[In-Interface: GE1/0/2                    Local LIH: 0x35]{lang="EN-US"}

[Local address: 57.20.20.2                 Refresh interval: 30000 ms]{lang="EN-US"}

[Out-Interface: GE1/0/4                    Nexthop: 57.20.20.1]{lang="EN-US"}

[Unknown object number: 0]{lang="EN-US"}

[Received ERO number: 2]{lang="EN-US"}

[  57.10.10.2/32      Strict]{lang="EN-US"}

[  57.20.20.1/32      Loose]{lang="EN-US"}

[Sent ERO number: 1]{lang="EN-US"}

[  57.20.20.1/32      Loose]{lang="EN-US"}

[XRO number: 2]{lang="EN-US"}

[  67.10.10.1/32]{lang="EN-US"}

[  67.20.20.1/32]{lang="EN-US"}

[RRO number: 1]{lang="EN-US"}

[  57.10.10.1/32      Flag: 0x00 (No FRR)]{lang="EN-US"}

[Fast Reroute PLR: Active]{lang="EN-US"}

[  FRR inner label: 3                      Bypass tunnel: Tunnel253]{lang="EN-US"}

[  Sender Template:]{lang="EN-US"}

[    Sender address: 10.11.112.140         LSP ID: 5]{lang="EN-US"}

[  FRR ERO number: 1]{lang="EN-US"}

[    3.3.3.9/32         Strict]{lang="EN-US"}

[Fast Reroute MP: None]{lang="EN-US"}

[ ]{lang="EN-US"}

[Destination: 3.3.3.9                      Source: 2.2.2.9]{lang="EN-US"}

[Tunnel ID: 253                            Style: SE]{lang="EN-US"}

[Sender address: 2.2.2.9                   LSP ID: 17767]{lang="EN-US"}

[Setup priority: 7                         Holding priority: 7]{lang="EN-US"}

[FRR desired: Yes                          BW protection desired: Yes]{lang="EN-US"}

[Received upstream label: 1115             Sent upstream label: 1115]{lang="EN-US"}

[Previous hop: 57.10.10.1                  Previous hop LIH: 0xf0008]{lang="EN-US"}

[Mean rate (CIR): 125.00 kbps              Mean burst size (CBS): 0.00 bytes]{lang="EN-US"}

[MTU: 1500                                 Qos service: Controlled-Load]{lang="EN-US"}

[Received message epoch: 0                 Received message ID: 0]{lang="EN-US"}

[Sent message epoch: 0                     Sent message ID: 0]{lang="EN-US"}

[In-Interface: GE1/0/2                    Local LIH: 0x67]{lang="EN-US"}

[Local address: 10.11.112.140              Refresh interval: 30000 ms]{lang="EN-US"}

[Out-Interface: GE1/0/6                   Nexthop: 10.11.112.135]{lang="EN-US"}

[Unknown object number: 0]{lang="EN-US"}

[Received ERO number: 5]{lang="EN-US"}

[  2.2.2.9/32         Strict]{lang="EN-US"}

[  10.11.112.140/32   Strict]{lang="EN-US"}

[  10.11.112.135/32   Strict]{lang="EN-US"}

[  57.40.40.3/32      Strict]{lang="EN-US"}

[  57.40.40.1/32      Strict]{lang="EN-US"}

[Sent ERO number: 3]{lang="EN-US"}

[  10.11.112.135/32   Strict]{lang="EN-US"}

[  57.40.40.3/32      Strict]{lang="EN-US"}

[  57.40.40.1/32      Strict]{lang="EN-US"}

[XRO number: 1]{lang="EN-US"}

[  67.40.40.1/32]{lang="EN-US"}

[RRO number: 0]{lang="EN-US"}

[Fast Reroute PLR: None]{lang="EN-US"}

[Fast Reroute MP: Active]{lang="EN-US"}

[  In-Interface: GE1/0/2]{lang="EN-US"}

[  Sender Template:]{lang="EN-US"}

[    Sender address: 10.11.112.140         LSP ID: 5]{lang="EN-US"}

[[表1-15 ]{lang="EN-US"}[display rsvp sender verbose]{lang="EN-US"}]{#struct_0_16315_x4274_942281125}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x86590660}[[字段]{style="font-family:黑体"}]{#struct_0_16315_x4274_x2030188786}

[[描述]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1188236210}

[[Destination]{lang="EN-US"}]{#struct_0_16315_x4274_x1511541117}

[[隧道目的地址]{style="font-family:宋体"}]{#struct_0_16315_x4274_x1630595819}

[[Source]{lang="EN-US"}]{#struct_0_16315_x4274_x732641}

[[隧道源端设备的]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}]{#struct_0_16315_x4274_1301843773}

[[Tunnel ID]{lang="EN-US"}]{#struct_0_16315_x4274_x1260016052}

[[隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_16315_x4274_1135032561}

[[Style]{lang="EN-US"}]{#struct_0_16315_x4274_1172700759}

[[资源预留风格，取值包括：]{style="font-family:宋体"}]{#struct_0_16315_x4274_x1630268139}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SE]{lang="EN-US"}]{#struct_0_16315_x4274_x81337329}[：共享显式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FF]{lang="EN-US"}]{#struct_0_16315_x4274_x1975946124}[：固定过滤器]{style="font-family:宋体"}

[[Sender address]{lang="EN-US"}]{#struct_0_16315_x4274_x1537541813}

[[发送者地址，用来标识隧道的源端]{style="font-family:宋体"}]{#struct_0_16315_x4274_845295678}

[[LSP ID]{lang="EN-US"}]{#struct_0_16315_x4274_x1630202603}

[[LSP ID]{lang="EN-US"}]{#struct_0_16315_x4274_x1536726018}

[[Setup priority]{lang="EN-US"}]{#struct_0_16315_x4274_x1756688370}

[[隧道建立优先级]{style="font-family:宋体"}]{#struct_0_16315_x4274_x1253767086}

[[Holding priority]{lang="EN-US"}]{#struct_0_16315_x4274_x1668524565}

[[隧道保持优先级]{style="font-family:宋体"}]{#struct_0_16315_x4274_x1630792426}

[[FRR desired]{lang="EN-US"}]{#struct_0_16315_x4274_720031610}

[[是否需要]{style="font-family:宋体"}[FRR]{lang="EN-US"}]{#struct_0_16315_x4274_x1482689735}[保护标记，取值包括]{style="font-family:宋体"}[Yes ]{lang="EN-US"}[和]{style="font-family:宋体"}[No]{lang="EN-US"}

[[BW protection desired]{lang="EN-US"}]{#struct_0_16315_x4274_707905797}

[[是否需要带宽保护标记，取值包括]{style="font-family:宋体"}[Yes ]{lang="EN-US"}]{#struct_0_16315_x4274_707840261}[和]{style="font-family:宋体"}[No]{lang="EN-US"}

[[Received upstream label]{lang="EN-US"}]{#struct_0_16315_x4274_x1299246305}

[[从上游收到的反向]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_16315_x4274_x1630726890}[标签]{style="font-family:宋体"}

[[Sent upstream label]{lang="EN-US"}]{#struct_0_16315_x4274_708036868}

[[发送给下游的反向]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_16315_x4274_707971332}[标签]{style="font-family:宋体"}

[[Previous hop]{lang="EN-US"}]{#struct_0_16315_x4274_1522522559}

[[前一跳地址]{style="font-family:宋体"}]{#struct_0_16315_x4274_1685396589}

[[Previous hop LIH]{lang="EN-US"}]{#struct_0_16315_x4274_x1823711038}

[[前一跳设备的逻辑接口索引]{style="font-family:宋体"}]{#struct_0_16315_x4274_x961455811}

[[Mean rate (CIR)]{lang="EN-US"}]{#struct_0_16315_x4274_x1630923498}

[[平均速率，单位为]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}]{#struct_0_16315_x4274_1822766315}

[[Mean burst size (CBS)]{lang="EN-US"}]{#struct_0_16315_x4274_1482443338}

[[平均峰值速率，单位为]{style="font-family:宋体"}[byte/s]{lang="EN-US"}]{#struct_0_16315_x4274_1991311956}

[[Path MTU]{lang="EN-US"}]{#struct_0_16315_x4274_x1630857962}

[[路径的最大传输单元]{style="font-family:宋体"}]{#struct_0_16315_x4274_x481268155}

[[QoS service]{lang="EN-US"}]{#struct_0_16315_x4274_x183066773}

[[QoS]{lang="EN-US"}]{#struct_0_16315_x4274_x1630530282}[业务类型，取值包括]{style="font-family:宋体"}[Controlled_Load]{lang="EN-US"}[和]{style="font-family:宋体"}[Guaranteed]{lang="EN-US"}

[[Received message Epoch]{lang="EN-US"}]{#struct_0_16315_x4274_x963043506}

[[接收消息携带的]{style="font-family:宋体"}[Message ID Object]{lang="EN-US"}]{#struct_0_16315_x4274_x2039185871}[中]{style="font-family:宋体"}[Epoch]{lang="EN-US"}[字段的值]{style="font-family:宋体"}

[[Received message ID]{lang="EN-US"}]{#struct_0_16315_x4274_68577853}

[[接收消息中的]{style="font-family:宋体"}[Message ID]{lang="EN-US"}]{#struct_0_16315_x4274_x1630464746}

[[Sent message epoch]{lang="EN-US"}]{#struct_0_16315_x4274_x135368846}

[[发送消息携带的]{style="font-family:宋体"}[Message ID Object]{lang="EN-US"}]{#struct_0_16315_x4274_408913678}[中]{style="font-family:宋体"}[Epoch]{lang="EN-US"}[字段的值]{style="font-family:宋体"}

[[Sent message ID]{lang="EN-US"}]{#struct_0_16315_x4274_x1664267444}

[[发送消息中的]{style="font-family:宋体"}[Message ID]{lang="EN-US"}]{#struct_0_16315_x4274_x1630661354}

[[In-Interface]{lang="EN-US"}]{#struct_0_16315_x4274_x623802816}

[[消息的入接口名称]{style="font-family:宋体"}]{#struct_0_16315_x4274_x570889454}

[[Local LIH]{lang="EN-US"}]{#struct_0_16315_x4274_x1630595818}

[[本地的逻辑接口索引]{style="font-family:宋体"}]{#struct_0_16315_x4274_1565351300}

[[Local address]{lang="EN-US"}]{#struct_0_16315_x4274_206751881}

[[Path]{lang="EN-US"}]{#struct_0_16315_x4274_x1630268138}[消息的出接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Refresh interval]{lang="EN-US"}]{#struct_0_16315_x4274_x1647421270}

[[路径和预留消息的刷新时间间隔，单位为毫秒]{style="font-family:宋体"}]{#struct_0_16315_x4274_1802033872}

[[Out-Interface]{lang="EN-US"}]{#struct_0_16315_x4274_256421716}

[[消息的出接口名称]{style="font-family:宋体"}]{#struct_0_16315_x4274_x1630202602}

[[Nexthop]{lang="EN-US"}]{#struct_0_16315_x4274_1192157337}

[[下一跳地址]{style="font-family:宋体"}]{#struct_0_16315_x4274_215469352}

[[Unknown object number]{lang="EN-US"}]{#struct_0_16315_x4274_x1630792429}

[[无法识别的]{style="font-family:宋体"}[Object]{lang="EN-US"}]{#struct_0_16315_x4274_672977443}[的个数]{style="font-family:宋体"}

[[Received ERO number]{lang="EN-US"}]{#struct_0_16315_x4274_1906066154}

[[接收的]{style="font-family:宋体"}[ERO]{lang="EN-US"}]{#struct_0_16315_x4274_x1630726893}[（]{style="font-family:宋体"}[Explicit Route Object]{lang="EN-US"}[，显式路由对象）的个数及其信息]{style="font-family:宋体"}

[[ERO]{lang="EN-US"}]{#struct_0_16315_x4274_x43561382}[信息包括显式路径经过的节点的地址、该节点为松散下一跳（]{style="font-family:宋体"}[Loose]{lang="EN-US"}[）或严格下一跳（]{style="font-family:宋体"}[Strict]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Sent ERO number]{lang="EN-US"}]{#struct_0_16315_x4274_x1586145426}

[[发送的]{style="font-family:宋体"}[ERO]{lang="EN-US"}]{#struct_0_16315_x4274_x1630923501}[的个数及其信息]{style="font-family:宋体"}

[[ERO]{lang="EN-US"}]{#struct_0_16315_x4274_x550345433}[信息包括显式路径经过的节点的地址、该节点为松散下一跳（]{style="font-family:宋体"}[Loose]{lang="EN-US"}[）或严格下一跳（]{style="font-family:宋体"}[Strict]{lang="EN-US"}[）]{style="font-family:宋体"}

[[XRO number]{lang="EN-US"}]{#struct_0_16315_x4274_962007390}

[[XRO]{lang="EN-US"}]{#struct_0_16315_x4274_962072926}[（]{style="font-family:宋体"}[Exclude Route Object]{lang="EN-US"}[，排除路由对象）的个数]{style="font-family:宋体"}

[[如果]{style="font-family:宋体"}[XRO]{lang="EN-US"}]{#struct_0_16315_x4274_961614174}[的个数不为零，则接下来显示]{style="font-family:宋体"}[XRO]{lang="EN-US"}[对象中的地址，该地址为不希望路由经过的接口地址或节点]{style="font-family:宋体"}[LSR-ID]{lang="EN-US"}[，即]{style="font-family:宋体"}[XRO]{lang="EN-US"}[中的地址不会出现在路由经过的地址列表中。]{style="font-family:宋体"}[XRO]{lang="EN-US"}[中的地址信息没有先后顺序要求]{style="font-family:宋体"}

[[RRO number]{lang="EN-US"}]{#struct_0_16315_x4274_x1817007299}

[[RRO]{lang="EN-US"}]{#struct_0_16315_x4274_x1630857965}[（]{style="font-family:宋体"}[Record Route Object]{lang="EN-US"}[，记录路由对象）的个数]{style="font-family:宋体"}

[[如果]{style="font-family:宋体"}[RRO]{lang="EN-US"}]{#struct_0_16315_x4274_x884552682}[的个数不为零，则接下来显示]{style="font-family:宋体"}[RRO]{lang="EN-US"}[对象中所记录的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址或标签信息]{style="font-family:宋体"}

[[只有]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}]{#struct_0_16315_x4274_x2037818467}[接口上配置了路由记录功能后，才会显示]{style="font-family:宋体"}[RRO]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Flag]{lang="EN-US"}]{#struct_0_16315_x4274_x1630530285}

[[RRO]{lang="EN-US"}]{#struct_0_16315_x4274_603040435}[对象中标记的值及其含义，标记含义的取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No FRR]{lang="EN-US"}]{#struct_0_16315_x4274_103752875}[：表示没有配置]{lang="EN-US" style="font-family:宋体"}[FRR]{lang="EN-US"}[保护]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FRR Avail]{lang="EN-US"}]{#struct_0_16315_x4274_x1630464749}[：表示]{lang="EN-US" style="font-family:宋体"}[FRR]{lang="EN-US"}[保护可用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[In use]{lang="EN-US"}]{#struct_0_16315_x4274_x1701452787}[：表示已经发生]{lang="EN-US" style="font-family:宋体"}[FRR]{lang="EN-US"}[切换]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BW]{lang="EN-US"}]{#struct_0_16315_x4274_x1716592324}[：表示带宽保护]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Node-Prot]{lang="EN-US"}]{#struct_0_16315_x4274_x1630661357}[：表示节点保护]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Node-ID]{lang="EN-US"}]{#struct_0_16315_x4274_2105080539}[：表示]{lang="EN-US" style="font-family:宋体"}[RRO]{lang="EN-US"}[对象中的地址为节点的]{lang="EN-US" style="font-family:宋体"}[LSR ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[In-Int]{lang="EN-US"}]{#struct_0_16315_x4274_x1026353300}[：表示]{lang="EN-US" style="font-family:宋体"}[RRO]{lang="EN-US"}[对象中的地址为入接口的地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Global label]{lang="EN-US"}]{#struct_0_16315_x4274_x1630595821}[：表示全局标签空间]{lang="EN-US" style="font-family:宋体"}

[[Fast Reroute PLR]{lang="EN-US"}]{#struct_0_16315_x4274_x356766393}

[[PLR]{lang="EN-US"}]{#struct_0_16315_x4274_x118474989}[（]{style="font-family:宋体"}[Point of Local Repair]{lang="EN-US"}[，本地修复节点）信息，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[None]{lang="EN-US"}]{#struct_0_16315_x4274_x1630268141}[：没有绑定快速重路由的旁路隧道]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ready]{lang="EN-US"}]{#struct_0_16315_x4274_x438026441}[：绑定快速重路由的旁路隧道，此时未进行切换]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_16315_x4274_x1630202605}[：绑定快速重路由的旁路隧道，此时已进行切换]{lang="EN-US" style="font-family:宋体"}

[[FRR]{lang="EN-US"}]{#struct_0_16315_x4274_1951672224}[[ i]{lang="EN-US" style="font-size:10.5pt"}]{.MsoCommentReference}[nner label]{lang="EN-US"}

[[快速重路由旁路隧道的入口标签，只有为]{style="font-family:宋体"}[PLR]{lang="EN-US"}]{#struct_0_16315_x4274_482622359}[节点才会显示此字段]{style="font-family:宋体"}

[[Bypass tunnel]{lang="EN-US"}]{#struct_0_16315_x4274_x1630792428}

[[旁路隧道的隧道名称，只有为]{style="font-family:宋体"}[PLR]{lang="EN-US"}]{#struct_0_16315_x4274_x2055905912}[节点才会显示此字段]{style="font-family:宋体"}

[[Sender Template]{lang="EN-US"}]{#struct_0_16315_x4274_x1630726892}

[[发送者模板]{style="font-family:宋体"}]{#struct_0_16315_x4274_x1609645323}

[[Sender address]{lang="EN-US"}]{#struct_0_16315_x4274_1969720628}

[[FRR]{lang="EN-US"}]{#struct_0_16315_x4274_x1630923500}[切换后，]{style="font-family:宋体"}[Path]{lang="EN-US"}[消息的发送者地址，取值为]{style="font-family:宋体"}[PLR]{lang="EN-US"}[节点上旁路隧道的出接口地址]{style="font-family:宋体"}

[[LSP ID]{lang="EN-US"}]{#struct_0_16315_x4274_x2116429374}

[[FRR]{lang="EN-US"}]{#struct_0_16315_x4274_x1630857964}[切换后，]{style="font-family:宋体"}[Path]{lang="EN-US"}[消息所携带的]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}

[[Fast Reroute MP]{lang="EN-US"}]{#struct_0_16315_x4274_681531259}

[[MP]{lang="EN-US"}]{#struct_0_16315_x4274_x1630530284}[（]{style="font-family:宋体"}[Merge Point]{lang="EN-US"}[，汇聚点）信息，取值包括：]{style="font-family:宋体"}

[[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
  Symbol"}]{.TableTextChar}[Active]{lang="EN-US"}]{#struct_0_16315_x4274_x2125842920}[：]{lang="EN-US" style="font-family:宋体"}[[为]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[MP]{lang="EN-US"}[节点，且已进行]{lang="EN-US" style="font-family:宋体"}[FRR]{lang="EN-US"}[切换]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[None]{lang="EN-US"}]{#struct_0_16315_x4274_x835664124}[：不是]{style="font-family:宋体"}[MP]{lang="EN-US"}[节点，或虽然是]{style="font-family:宋体"}[MP]{lang="EN-US"}[节点但没有发生]{style="font-family:宋体"}[FRR]{lang="EN-US"}[切换]{style="font-family:宋体"}

[[In-Interface]{lang="EN-US"}]{#struct_0_16315_x4274_x1630464748}

[[消息的入接口名称]{style="font-family:宋体"}]{#struct_0_16315_x4274_1027430568}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1944335194}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display rsvp lsp]{lang="EN-US"}**]{#struct_0_16315_x4274_x1835276767}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display rsvp request]{lang="EN-US"}**]{#struct_0_16315_x4274_x1630661356}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display rsvp reservation]{lang="EN-US"}**]{#struct_0_16315_x4274_538996598}

::: {#-800614567 .myid}
[]{#_Toc404791056}[]{#struct_0_16315_x4274_x501896090}[]{#_Toc333936386}[]{#_Toc328505098}[]{#_Toc324951725}

**RSVP \-- RSVP配置命令 \-- display rsvp statistics**

------------------------------------------------------------------------

[**[display rsvp]{lang="EN-US"}**[ **statistics**]{lang="EN-US"}]{#struct_0_16315_x4274_884529956}[命令用来显示]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x2056292590}

[**[display rsvp]{lang="EN-US"}**[ **statistics** \[ **interface** \[ *interface-type* *interface-number* \] \]]{lang="EN-US"}]{#struct_0_16315_x4274_31359494}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x221301422}

[[任意视图]{style="font-family:宋体"}]{#struct_0_16315_x4274_1777825172}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1630595820}

[[network-admin]{lang="EN-US"}]{#struct_0_16315_x4274_1209317548}

[[network-operator]{lang="EN-US"}]{#struct_0_16315_x4274_x2011921958}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16315_x4274_541930219}

[[mdc-operator]{lang="EN-US"}]{#struct_0_16315_x4274_x846132473}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x207476848}

[**[interface]{lang="EN-US"}**]{#struct_0_16315_x4274_x710550884}[：显示接口的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_16315_x4274_x1422011771}[：显示指定接口的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型及接口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x578855252}

[[执行]{style="font-family:宋体"}**[display]{lang="EN-US"}**[ **rsvp statistics**]{lang="EN-US"}]{#struct_0_16315_x4274_x1630268140}[命令时：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{style="font-family:宋体"}]{#struct_0_16315_x4274_x2004110382}**[interface]{lang="EN-US"}**[参数，则显示全局的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果只指定]{lang="EN-US" style="font-family:宋体"}**[interface]{lang="EN-US"}**]{#struct_0_16315_x4274_1229382681}[参数，不指定]{lang="EN-US" style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[参数，则显示所有开启了]{lang="EN-US" style="font-family:宋体"}[RSVP]{lang="EN-US"}[能力的接口的]{lang="EN-US" style="font-family:宋体"}[RSVP]{lang="EN-US"}[统计信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_16315_x4274_1978015025}[参数，则显示指定接口的]{lang="EN-US" style="font-family:宋体"}[RSVP]{lang="EN-US"}[统计信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1197576922}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_738017598}[显示全局的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display rsvp statistics]{lang="EN-US"}]{#struct_0_16315_x4274_x1630202604}

[Object                 Added            Deleted]{lang="EN-US"}

[  PSB                  3                1]{lang="EN-US"}

[  RSB                  3                1]{lang="EN-US"}

[  LSP                  3                1]{lang="EN-US"}

[ ]{lang="EN-US"}

[Packet                 Received         Sent]{lang="EN-US"}

[  Path                 5                5]{lang="EN-US"}

[  Resv                 5                5]{lang="EN-US"}

[  PathError            0                0]{lang="EN-US"}

[  ResvError            0                0]{lang="EN-US"}

[  PathTear             0                0]{lang="EN-US"}

[  ResvTear             0                0]{lang="EN-US"}

[  ResvConf             0                0]{lang="EN-US"}

[  Bundle               0                0]{lang="EN-US"}

[  Ack                  0                0]{lang="EN-US"}

[  Srefresh             0                0]{lang="EN-US"}

[  Hello                0                0]{lang="EN-US"}

[  Challenge            0                0]{lang="EN-US"}

[  Response             0                0]{lang="EN-US"}

[  Error                0                0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_385588283}[显示接口的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display rsvp statistics interface]{lang="EN-US"}]{#struct_0_16315_x4274_748479706}

[GE1/0/2:]{lang="EN-US"}

[Packet                 Received         Sent]{lang="EN-US"}

[  Path                 2                2]{lang="EN-US"}

[  Resv                 2                2]{lang="EN-US"}

[  PathError            0                0]{lang="EN-US"}

[  ResvError            0                0]{lang="EN-US"}

[  PathTear             0                0]{lang="EN-US"}

[  ResvTear             0                0]{lang="EN-US"}

[  ResvConf             0                0]{lang="EN-US"}

[  Bundle               0                0]{lang="EN-US"}

[  Ack                  0                0]{lang="EN-US"}

[  Srefresh             0                0]{lang="EN-US"}

[  Hello                0                0]{lang="EN-US"}

[  Challenge            0                0]{lang="EN-US"}

[  Response             0                0]{lang="EN-US"}

[  Error                0                0]{lang="EN-US"}

[ ]{lang="EN-US"}

[GE1/0/4:]{lang="EN-US"}

[Packet                 Received         Sent]{lang="EN-US"}

[  Path                 3                3]{lang="EN-US"}

[  Resv                 3                3]{lang="EN-US"}

[  PathError            0                0]{lang="EN-US"}

[  ResvError            0                0]{lang="EN-US"}

[  PathTear             0                0]{lang="EN-US"}

[  ResvTear             0                0]{lang="EN-US"}

[  ResvConf             0                0]{lang="EN-US"}

[  Bundle               0                0]{lang="EN-US"}

[  Ack                  0                0]{lang="EN-US"}

[  Srefresh             0                0]{lang="EN-US"}

[  Hello                0                0]{lang="EN-US"}

[  Challenge            0                0]{lang="EN-US"}

[  Response             0                0]{lang="EN-US"}

[  Error                0                0]{lang="EN-US"}

[[表1-16 ]{lang="EN-US"}[display rsvp statistics]{lang="EN-US"}]{#struct_0_16315_x4274_1837284082}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x93069662}[[字段]{style="font-family:黑体"}]{#struct_0_16315_x4274_250561257}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16315_x4274_748414170}

[[PSB]{lang="EN-US"}]{#struct_0_16315_x4274_x875703704}

[[添加]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_16315_x4274_x1030916291}[删除]{style="font-family:宋体"}[PSB]{lang="EN-US"}[的次数]{style="font-family:宋体"}

[[RSB]{lang="EN-US"}]{#struct_0_16315_x4274_819872007}

[[添加]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_16315_x4274_210596396}[删除]{style="font-family:宋体"}[RSB]{lang="EN-US"}[的次数]{style="font-family:宋体"}

[[LSP]{lang="EN-US"}]{#struct_0_16315_x4274_x1745051265}

[[添加]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_16315_x4274_748348634}[删除]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的次数]{style="font-family:宋体"}

[[Path]{lang="EN-US"}]{#struct_0_16315_x4274_1196443194}

[[接收]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_16315_x4274_x1950614945}[发送的]{style="font-family:宋体"}[Path]{lang="EN-US"}[消息数量]{style="font-family:宋体"}

[[Resv]{lang="EN-US"}]{#struct_0_16315_x4274_x1450242824}

[[接收]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_16315_x4274_x533906090}[发送的]{style="font-family:宋体"}[Resv]{lang="EN-US"}[消息数量]{style="font-family:宋体"}

[[PathError]{lang="EN-US"}]{#struct_0_16315_x4274_x130090552}

[[接收]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_16315_x4274_748283098}[发送的]{style="font-family:宋体"}[Path Error]{lang="EN-US"}[消息数量]{style="font-family:宋体"}

[[ResvError]{lang="EN-US"}]{#struct_0_16315_x4274_x1499898132}

[[接收]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_16315_x4274_x531714462}[发送的]{style="font-family:宋体"}[Resv Error]{lang="EN-US"}[消息数量]{style="font-family:宋体"}

[[PathTear]{lang="EN-US"}]{#struct_0_16315_x4274_1963397195}

[[接收]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_16315_x4274_x451771355}[发送的]{style="font-family:宋体"}[Path Tear]{lang="EN-US"}[消息数量]{style="font-family:宋体"}

[[ResvTear]{lang="EN-US"}]{#struct_0_16315_x4274_748217562}

[[接收]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_16315_x4274_x1923373866}[发送的]{style="font-family:宋体"}[Resv Tear]{lang="EN-US"}[消息数量]{style="font-family:宋体"}

[[ResvConf]{lang="EN-US"}]{#struct_0_16315_x4274_23612182}

[[接收]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_16315_x4274_x995516716}[发送的]{style="font-family:宋体"}[Resv Conf]{lang="EN-US"}[消息数量]{style="font-family:宋体"}

[[Bundle]{lang="EN-US"}]{#struct_0_16315_x4274_748152026}

[[接收]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_16315_x4274_x1412801201}[发送的]{style="font-family:宋体"}[Bundle]{lang="EN-US"}[消息数量]{style="font-family:宋体"}

[[Ack]{lang="EN-US"}]{#struct_0_16315_x4274_x49461568}

[[接收]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_16315_x4274_x754088896}[发送的]{style="font-family:宋体"}[Ack]{lang="EN-US"}[消息数量]{style="font-family:宋体"}

[[Srefresh]{lang="EN-US"}]{#struct_0_16315_x4274_x1064528267}

[[接收]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_16315_x4274_748086490}[发送的]{style="font-family:宋体"}[Srefresh]{lang="EN-US"}[消息数量]{style="font-family:宋体"}

[[Hello]{lang="EN-US"}]{#struct_0_16315_x4274_564408672}

[[接收]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_16315_x4274_x1790609615}[发送的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[消息数量]{style="font-family:宋体"}

[[Challenge]{lang="EN-US"}]{#struct_0_16315_x4274_381187225}

[[接收]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_16315_x4274_748020954}[发送的]{style="font-family:宋体"}[Integrity Challenge]{lang="EN-US"}[消息数量]{style="font-family:宋体"}

[[Response]{lang="EN-US"}]{#struct_0_16315_x4274_1371811185}

[[接收]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_16315_x4274_x436224148}[发送的]{style="font-family:宋体"}[Integrity Response]{lang="EN-US"}[消息数量]{style="font-family:宋体"}

[[Error]{lang="EN-US"}]{#struct_0_16315_x4274_1003294593}

[[接收]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_16315_x4274_749003994}[发送的错误消息数量]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_746137016}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset]{lang="EN-US"}**[ **rsvp** **statistics**]{lang="EN-US"}]{#struct_0_16315_x4274_1065761255}

::: {#1124128791 .myid}
[]{#_Toc404791057}[]{#struct_0_16315_x4274_962400605}[]{#_Toc358212191}[]{#_Toc356823295}

**RSVP \-- RSVP配置命令 \-- dscp**

------------------------------------------------------------------------

[**[dscp]{lang="EN-US"}**]{#struct_0_16315_x4274_x1886361546}[命令用来配置]{style="font-family:宋体"}[发送的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[**[undo dscp]{lang="EN-US"}**]{#struct_0_16315_x4274_962466141}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1511995935}

[**[dscp ]{lang="EN-US"}***[dscp-value]{lang="EN-US"}*]{#struct_0_16315_x4274_x604207619}

[**[undo dscp]{lang="EN-US"}**]{#struct_0_16315_x4274_x458600815}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1456147766}

[[发送的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x604142083}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[48]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1592195168}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x1192283124}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x604076547}

[[network-admin]{lang="EN-US"}]{#struct_0_16315_x4274_x456074833}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16315_x4274_1153965882}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x604011011}

[*[dscp-value]{lang="EN-US"}*]{#struct_0_16315_x4274_x2006162151}[：发送的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1235892783}

[[DSCP]{lang="EN-US"}]{#struct_0_16315_x4274_x604469763}[（]{style="font-family:宋体"}[Differentiated Services Code point]{lang="EN-US"}[，差分服务编码点）携带在]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[字段，用来体现报文自身的优先等级，决定报文传输的优先程度。通过本命令可以指定发送的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[报文中携带的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级的取值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1085803226}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_981926353}[配置发送的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[56]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="FR"}]{#struct_0_16315_x4274_x604404227}

[\[Sysname\] rsvp]{lang="FR"}

[\[Sysname-rsvp\] dscp 56]{lang="FR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1504953295}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display rsvp]{lang="EN-US"}**]{#struct_0_16315_x4274_681094702}
:::

::: {#-235989138 .myid}
[]{#_Toc404791058}[]{#struct_0_16315_x4274_x1269905397}[]{#_Toc333936392}[]{#_Toc328505100}[]{#_Toc324951727}

**RSVP \-- RSVP配置命令 \-- graceful-restart enable**

------------------------------------------------------------------------

[**[graceful-restart enable]{lang="EN-US"}**]{#struct_0_16315_x4274_x703769979}[命令用来开启]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[（]{style="font-family:宋体"}[Graceful Restart]{lang="EN-US"}[，平滑重启）功能。]{style="font-family:宋体"}

[**[undo graceful-restart enable]{lang="EN-US"}**]{#struct_0_16315_x4274_x934278408}[命令用来关闭]{style="font-family:
宋体"}[RSVP]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1877375287}

[**[graceful-restart enable]{lang="EN-US"}**]{#struct_0_16315_x4274_748938458}

[**[undo graceful-restart enable]{lang="EN-US"}**]{#struct_0_16315_x4274_x1184419841}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16315_x4274_2045530464}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_968046458}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1195009785}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_146095922}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16315_x4274_320086630}

[[network-admin]{lang="EN-US"}]{#struct_0_16315_x4274_x1871510730}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16315_x4274_748479707}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1837284083}

[[目前]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_250495721}[仅支持]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[方功能，即协助邻居设备进行]{style="font-family:宋体"}[GR]{lang="EN-US"}[重启，而自身不能进行]{style="font-family:宋体"}[GR]{lang="EN-US"}[重启。本地设备的]{style="font-family:宋体"}[NSF]{lang="EN-US"}[（]{style="font-family:宋体"}[Nonstop Forwarding]{lang="EN-US"}[，不间断转发）只能通过主备进程之间的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[（]{style="font-family:宋体"}[Nonstop Routing]{lang="EN-US"}[，不间断路由）功能实现。]{style="font-family:宋体"}

[[只有在接口视图下通过]{style="font-family:宋体"}**[rsvp hello enable]{lang="EN-US"}**]{#struct_0_16315_x4274_x1287425039}[命令开启了]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[扩展功能后，本地设备才能作为]{style="font-family:宋体"}[GR helper]{lang="EN-US"}[协助该接口所连接的邻居设备进行]{style="font-family:宋体"}[GR]{lang="EN-US"}[重启。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x785013777}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_x1236480151}[全局开启]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16315_x4274_x330598201}

[\[Sysname\] rsvp]{lang="EN-US"}

[\[Sysname-rsvp\] ]{lang="NO-BOK"}[graceful-restart enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_748414171}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp hello enable]{lang="EN-US"}**]{#struct_0_16315_x4274_x875703703}
:::

::: {#-1241019893 .myid}
[]{#_Toc404791059}[]{#struct_0_16315_x4274_x1031375043}[]{#_Toc333936393}[]{#_Toc328505102}[]{#_Toc324951729}

**RSVP \-- RSVP配置命令 \-- hello interval**

------------------------------------------------------------------------

[**[hello interval]{lang="EN-US"}**]{#struct_0_16315_x4274_1587886738}[命令用来配置]{style="font-family:宋体"}[Hello Request]{lang="EN-US"}[消息的发送时间间隔。]{style="font-family:宋体"}

[**[undo hello]{lang="EN-US"}**[ **interval**]{lang="EN-US"}]{#struct_0_16315_x4274_753885090}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_958725276}

[**[hello ]{lang="DA"}**]{#struct_0_16315_x4274_x1544246265}**[interval]{lang="NO-BOK"}***[ ]{lang="NO-BOK"}[interval]{lang="DA"}*

[**[undo hello ]{lang="DA"}**]{#struct_0_16315_x4274_x555530529}**[interval]{lang="NO-BOK"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x557387157}

[[Hello Request]{lang="NO-BOK"}]{#struct_0_16315_x4274_748348635}[消息的发送时间间隔为]{style="font-family:宋体"}[5]{lang="NO-BOK"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1196443193}

[[RSVP]{lang="NO-BOK"}]{#struct_0_16315_x4274_x1950418337}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1011014708}

[[network-admin]{lang="NO-BOK"}]{#struct_0_16315_x4274_x973049442}

[[mdc-admin]{lang="NO-BOK"}]{#struct_0_16315_x4274_x1078138844}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1516019693}

[*[interval]{lang="NO-BOK"}*]{#struct_0_16315_x4274_978409534}[：]{style="font-family:宋体"}[Hello Request]{lang="NO-BOK"}[消息的发送时间间隔]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="NO-BOK"}[～]{style="font-family:宋体"}[60]{lang="NO-BOK"}[，]{style="font-family:宋体"}[单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16315_x4274_748283099}

[[在本命令指定的时间内]{style="font-family:宋体"}]{#struct_0_16315_x4274_x1499898133}[，]{style="font-family:宋体"}[如果没有收到邻居发送的]{style="font-family:宋体"}[Hello Request]{lang="NO-BOK"}[消息]{style="font-family:宋体"}[，]{style="font-family:宋体"}[则主动向邻居发送]{style="font-family:宋体"}[Hello Request]{lang="NO-BOK"}[消息]{style="font-family:宋体"}[；]{style="font-family:宋体"}[如果收到了邻居发送的]{style="font-family:宋体"}[Hello Request]{lang="NO-BOK"}[消息]{style="font-family:宋体"}[，]{style="font-family:宋体"}[则立即向邻居回应]{style="font-family:宋体"}[Hello Ack]{lang="NO-BOK"}[消息。]{style="font-family:宋体"}

[[只有在接口视图下通过]{style="font-family:宋体"}]{#struct_0_16315_x4274_x2097798403}**[rsvp hello enable]{lang="NO-BOK"}**[命令开启了]{style="font-family:宋体"}[RSVP]{lang="NO-BOK"}[的]{style="font-family:宋体"}[Hello]{lang="NO-BOK"}[扩展功能后]{style="font-family:宋体"}[，]{style="font-family:宋体"}[设备才会通过该接口发送]{style="font-family:宋体"}[Hello]{lang="NO-BOK"}[消息]{style="font-family:宋体"}[，]{style="font-family:宋体"}[本命令才会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16315_x4274_858757290}

[[\# ]{lang="NO-BOK"}]{#struct_0_16315_x4274_1136437119}[配置]{style="font-family:宋体"}[Hello Request]{lang="NO-BOK"}[消息的发送时间间隔为]{style="font-family:宋体"}[10]{lang="NO-BOK"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NO-BOK"}]{#struct_0_16315_x4274_x485902651}

[\[Sysname\] rsvp]{lang="NO-BOK"}

[\[Sysname-rsvp\] hello interval 10]{lang="NO-BOK"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1267966954}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hello lost]{lang="EN-US"}**]{#struct_0_16315_x4274_x508543058}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp hello enable]{lang="EN-US"}**]{#struct_0_16315_x4274_1934916778}
:::

::: {#-119070267 .myid}
[]{#_Toc67196092}[]{#_Toc67145917}[]{#_Toc59929618}[]{#_Toc50284044}[]{#_Toc404791060}[]{#struct_0_16315_x4274_748217563}[]{#_Toc333936394}[]{#_Toc328505101}[]{#_Toc324951728}

**RSVP \-- RSVP配置命令 \-- hello lost**

------------------------------------------------------------------------

[**[hello lost]{lang="EN-US"}**]{#struct_0_16315_x4274_x1923373865}[命令用来配置]{style="font-family:宋体"}[Hello]{lang="EN-US"}[消息连续丢失或错误的最大次数。]{style="font-family:宋体"}

[**[undo hello lost]{lang="EN-US"}**]{#struct_0_16315_x4274_x1542471759}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_62710545}

[**[hello lost]{lang="EN-US"}**[ *times*]{lang="EN-US"}]{#struct_0_16315_x4274_x489163055}

[**[undo hello lost]{lang="EN-US"}**]{#struct_0_16315_x4274_1184354249}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x31700483}

[[Hello]{lang="EN-US"}]{#struct_0_16315_x4274_1550165030}[消息连续丢失或错误的最大次数为]{style="font-family:宋体"}[4]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16315_x4274_748152027}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x1412801200}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1615545509}

[[network-admin]{lang="EN-US"}]{#struct_0_16315_x4274_x1159278316}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16315_x4274_1707673226}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1570287370}

[*[times]{lang="EN-US"}*]{#struct_0_16315_x4274_2108521554}[：]{style="font-family:宋体"}[Hello]{lang="EN-US"}[消息连续丢失或错误的最大次数，取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16315_x4274_658148394}

[[当连续未收到]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_16315_x4274_x24845207}[消息或收到错误的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[消息的次数达到本命令配置的次数时，认为邻居设备发生故障。如果配置了]{style="font-family:宋体"}[GR]{lang="EN-US"}[功能，则本地设备作为]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[协助邻居进行]{style="font-family:宋体"}[GR]{lang="EN-US"}[重启；如果没有配置]{style="font-family:宋体"}[GR]{lang="EN-US"}[功能，但配置了]{style="font-family:宋体"}[FRR]{lang="EN-US"}[功能，则进行]{style="font-family:宋体"}[FRR]{lang="EN-US"}[切换。]{style="font-family:宋体"}

[[Hello]{lang="EN-US"}]{#struct_0_16315_x4274_748086491}[消息连续丢失或错误的最大次数过大会导致不能快速检测到邻居的故障，过小则可能会导致错误地认为邻居出现故障。请根据实际组网和应用需求选择合适的值。]{style="font-family:宋体"}

[[只有通过]{style="font-family:宋体"}**[rsvp hello enable]{lang="EN-US"}**]{#struct_0_16315_x4274_564408671}[命令开启]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[扩展功能后，本命令才会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1790609616}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_x1184896716}[配置]{style="font-family:宋体"}[Hello]{lang="EN-US"}[消息连续丢失或错误的最大次数为]{style="font-family:宋体"}[6]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16315_x4274_187374746}

[\[Sysname\] rsvp]{lang="EN-US"}

[\[Sysname-rsvp\] hello lost 6]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1317504077}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hello ]{lang="DA"}**]{#struct_0_16315_x4274_1518396996}**[interval]{lang="NO-BOK"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp hello enable]{lang="EN-US"}**]{#struct_0_16315_x4274_x1916146060}
:::

::: {#-1992029901 .myid}
[]{#_Toc404791061}[]{#struct_0_16315_x4274_748020955}[]{#_Toc333936395}[]{#_Toc328505103}[]{#_Toc324951730}[]{#_Toc329607621}[]{#_Toc329607735}[]{#_Toc330307154}[]{#_Toc329607622}[]{#_Toc329607736}[]{#_Toc330307155}

**RSVP \-- RSVP配置命令 \-- keep-multiplier**

------------------------------------------------------------------------

[**[keep-multiplier]{lang="EN-US"}**]{#struct_0_16315_x4274_1371811184}[命令用来配置]{style="font-family:宋体"}[PSB]{lang="EN-US"}[和]{style="font-family:宋体"}[RSB]{lang="EN-US"}[的老化超时倍数。]{style="font-family:宋体"}

[**[undo keep-multiplier]{lang="EN-US"}**]{#struct_0_16315_x4274_x436158612}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1790933271}

[**[keep-multiplier]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_16315_x4274_741969038}

[**[undo keep-multiplier]{lang="EN-US"}**]{#struct_0_16315_x4274_683862641}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16315_x4274_444403003}

[[PSB]{lang="EN-US"}]{#struct_0_16315_x4274_x865325358}[和]{style="font-family:宋体"}[RSB]{lang="EN-US"}[的老化超时倍数为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x778016785}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_749003995}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16315_x4274_746137015}

[[network-admin]{lang="EN-US"}]{#struct_0_16315_x4274_1065761258}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16315_x4274_x1269053429}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1434558127}

[*[number]{lang="EN-US"}*]{#struct_0_16315_x4274_2084733894}[：]{style="font-family:宋体"}[PSB]{lang="EN-US"}[和]{style="font-family:宋体"}[RSB]{lang="EN-US"}[的老化超时倍数，取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1719994834}

[[PSB]{lang="EN-US"}]{#struct_0_16315_x4274_285050134}[和]{style="font-family:宋体"}[RSB]{lang="EN-US"}[老化时间的计算方法为：]{style="font-family:宋体"}[Expired_Time]{lang="EN-US"}[＝（]{style="font-family:宋体"}[keep-multiplier]{lang="EN-US"}[＋]{style="font-family:宋体"}[0.5]{lang="EN-US"}[）]{style="font-family:宋体"}[×1.5×refresh-time]{lang="EN-US"}[。其中，]{style="font-family:宋体"}[refresh-time]{lang="EN-US"}[为对端设备向本端通告的路径和预留消息刷新时间间隔。]{style="font-family:宋体"}

[[为了避免设备上保存过多的]{style="font-family:宋体"}[PSB]{lang="EN-US"}]{#struct_0_16315_x4274_x80108516}[和]{style="font-family:宋体"}[RSB]{lang="EN-US"}[，占用系统资源，]{style="font-family:宋体"}[如果老化时间内没有收到]{style="font-family:宋体"}[Path]{lang="EN-US"}[或]{style="font-family:宋体"}[Resv]{lang="EN-US"}[刷新信息，相应的]{style="font-family:宋体"}[PSB]{lang="EN-US"}[或]{style="font-family:宋体"}[RSB]{lang="EN-US"}[将会被删除。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16315_x4274_748938459}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_x1184419840}[配置]{style="font-family:宋体"}[PSB]{lang="EN-US"}[和]{style="font-family:宋体"}[RSB]{lang="EN-US"}[的老化超时倍数为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16315_x4274_479446523}

[\[Sysname\] rsvp]{lang="EN-US"}

[\[Sysname-rsvp\] keep-multiplier 5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1886412289}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[refresh interval]{lang="EN-US"}**]{#struct_0_16315_x4274_927321721}
:::

::: {#1903411553 .myid}
[]{#_Toc404791062}[]{#struct_0_16315_x4274_1196792279}[]{#_Toc333936432}[]{#_Toc328505104}[]{#_Toc324951731}

**RSVP \-- RSVP配置命令 \-- peer**

------------------------------------------------------------------------

[**[pee]{lang="EN-US"}**]{#struct_0_16315_x4274_x1192333539}**[r]{lang="ES"}**[命令用来创建]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[认证邻居，并进入]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居视图。在该视图下可以配置邻居的认证信息。]{style="font-family:宋体"}

[**[undo peer]{lang="EN-US"}**]{#struct_0_16315_x4274_x430643821}[命令用来删除指定的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[认证邻居。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_748479704}

[**[pee]{lang="EN-US"}**]{#struct_0_16315_x4274_1837284084}**[r ]{lang="ES"}***[ip-address]{lang="EN-US"}*

[**[undo pee]{lang="EN-US"}**]{#struct_0_16315_x4274_250954473}**[r ]{lang="ES"}***[ip-address]{lang="EN-US"}*

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16315_x4274_754838006}

[[设备上不存在任何]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x224384524}[认证邻居。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16315_x4274_325725837}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x735919838}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1544885045}

[[network-admin]{lang="EN-US"}]{#struct_0_16315_x4274_x690297600}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16315_x4274_748414168}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1080611440}

[*[ip-address]{lang="EN-US"}*]{#struct_0_16315_x4274_x324015161}[：]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[认证邻居的地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16315_x4274_2090771105}

[[通过本命令创建]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x1387669646}[认证邻居后，可以在]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居视图下为特定的邻居配置特定的认证信息（如认证密钥、]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[的空闲老化时间等）。]{style="font-family:宋体"}

[[设备接收到带认证对象的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x2144605587}[消息后，根据消息（]{style="font-family:宋体"}[Path]{lang="EN-US"}[，]{style="font-family:宋体"}[Path Tear]{lang="EN-US"}[消息）]{style="font-family:宋体"}[PHOP]{lang="EN-US"}[中的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址或消息（]{style="font-family:宋体"}[Path Error]{lang="EN-US"}[，]{style="font-family:宋体"}[Resv]{lang="EN-US"}[，]{style="font-family:宋体"}[Resv Error]{lang="EN-US"}[等除]{style="font-family:宋体"}[Path]{lang="EN-US"}[，]{style="font-family:宋体"}[Path Tear]{lang="EN-US"}[外的其它消息）的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址来检查设备上是否存在与之匹配的认证邻居。如果存在且为该认证邻居配置了认证密钥，则根据认证邻居的密钥来检查消息是否合法；否则，根据接口视图或全局视图下配置的认证密钥来检查消息是否合法。如果三个视图下都没有配置认证密钥，则忽略消息中的认证对象，直接接收该消息。]{style="font-family:宋体"}

[[设备发送]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x1172021206}[消息时，根据消息目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址所对应的下一跳地址来检查设备上是否存在与之匹配的认证邻居。如果存在且为该认证邻居配置了认证密钥，则根据认证邻居的密钥来设置认证对象；否则，根据接口视图或全局视图下配置的认证密钥来设置认证对象。如果三个视图下都没有配置认证密钥，则不在发送的消息中携带认证对象。]{style="font-family:宋体"}

[[如果发生了]{style="font-family:宋体"}[FRR]{lang="EN-US"}]{#struct_0_16315_x4274_x1769725447}[切换，则]{style="font-family:宋体"}[PLR]{lang="EN-US"}[节点所对应的下游认证邻居为旁路隧道的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，]{style="font-family:宋体"}[MP]{lang="EN-US"}[节点所对应的上游认证邻居为]{style="font-family:宋体"}[PLR]{lang="EN-US"}[节点旁路隧道的物理出接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1896011771}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_748348632}[创建]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[认证邻居]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，进入]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居视图，并配置此邻居的认证密钥为明文]{style="font-family:宋体"}[abcdfegh]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16315_x4274_1196443196}

[\[Sysname\] rsvp ]{lang="EN-US"}

[\[Sysname-rsvp\] peer 1.1.1.1]{lang="EN-US"}

[\[Sysname-rsvp-peer-1.1.1.1\] authentication key plain abcdfegh]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1950746017}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication challenge]{lang="EN-US"}**]{#struct_0_16315_x4274_1320000180}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication key]{lang="EN-US"}**]{#struct_0_16315_x4274_1158362072}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication lifetime]{lang="EN-US"}**]{#struct_0_16315_x4274_218512381}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication window-size]{lang="EN-US"}**]{#struct_0_16315_x4274_x1138493964}
:::

::: {#-1184885453 .myid}
[]{#_Toc404791063}[]{#struct_0_16315_x4274_x21941270}[]{#_Toc333936433}[]{#_Toc328505105}[]{#_Toc324951732}

**RSVP \-- RSVP配置命令 \-- refresh interval**

------------------------------------------------------------------------

[**[refresh interval]{lang="EN-US"}**]{#struct_0_16315_x4274_748283096}[命令用来配置路径消息和预留消息的刷新时间间隔。]{style="font-family:宋体"}

[**[undo refresh interval]{lang="EN-US"}**]{#struct_0_16315_x4274_x1499898122}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x531779998}

[**[refresh]{lang="EN-US"}**[ **interval** *interval*]{lang="EN-US"}]{#struct_0_16315_x4274_x1174662407}

[**[undo refresh ]{lang="PT-BR"}**]{#struct_0_16315_x4274_x282496310}**[interval]{lang="NO-BOK"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1703292447}

[[路径消息和预留消息的刷新时间间隔为]{style="font-family:宋体"}[30]{lang="EN-US"}]{#struct_0_16315_x4274_x518767879}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1640449883}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_26172620}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16315_x4274_748217560}

[[network-admin]{lang="EN-US"}]{#struct_0_16315_x4274_x1923373868}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16315_x4274_x1139187232}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1912012339}

[*[interval]{lang="EN-US"}*]{#struct_0_16315_x4274_x1422320656}[：路径消息和预留消息的刷新时间间隔，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x500699201}

[[本]{style="font-family:宋体"}]{#struct_0_16315_x4274_1640434454}[命令具有如下作用：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[决定发送的路径消息和预留消息的刷新时间间隔。]{style="font-family:宋体"}]{#struct_0_16315_x4274_x331058974}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在路径消息和预留消息中携带本地配置的刷新时间间隔，以便对端设备根据该值计算]{style="font-family:宋体"}]{#struct_0_16315_x4274_1693419140}[PSB]{lang="EN-US"}[和]{style="font-family:宋体"}[RSB]{lang="EN-US"}[的老化时间。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16315_x4274_748152024}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_x1412801203}[配置路径和预留消息的刷新时间间隔为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16315_x4274_1113337846}

[\[Sysname\] rsvp]{lang="EN-US"}

[\[Sysname-rsvp\] refresh interval 60]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1496811041}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[keep-multiplier]{lang="EN-US"}**]{#struct_0_16315_x4274_x1470406761}
:::

::: {#-2117886718 .myid}
[]{#_Toc404791064}[]{#struct_0_16315_x4274_965387342}[]{#_Toc333936435}[]{#_Toc328505106}[]{#_Toc324951733}

**RSVP \-- RSVP配置命令 \-- reset rsvp authentication**

------------------------------------------------------------------------

[**[reset rsvp authentication]{lang="ES"}**]{#struct_0_16315_x4274_1997399505}[命令用来手工清除]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x983154851}

[**[reset rsvp authentication ]{lang="ES"}**[\[ ]{lang="EN-US"}]{#struct_0_16315_x4274_748086488}**[from]{lang="ES"}***[ ]{lang="ES"}[ip-address ]{lang="EN-US"}***[to ]{lang="ES"}***[ip-address ]{lang="EN-US"}*[\]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1774243496}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16315_x4274_105569693}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1566283478}

[[network-admin]{lang="EN-US"}]{#struct_0_16315_x4274_525129803}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16315_x4274_1173076260}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x446041937}

[**[from]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_16315_x4274_x1340308218}[：清除认证发起节点]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为指定地址的]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为认证发起节点的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[to ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*]{#struct_0_16315_x4274_179703850}[：清除认证目的节点]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为指定地址的]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[认证目的节点的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16315_x4274_748020952}

[[执行]{style="font-family:宋体"}]{#struct_0_16315_x4274_1371811183}**[reset ]{lang="ES"}[rsvp authentication]{lang="EN-US"}**[命令时，如果没有指定]{style="font-family:宋体"}**[from]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*[和]{style="font-family:宋体"}**[to ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*[参数，则清除本地设备与所有邻居建立的]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x436093076}

[[\# ]{lang="ES"}]{#struct_0_16315_x4274_x590981561}[清除所有的]{style="font-family:宋体"}[RSVP SA]{lang="ES"}[。]{style="font-family:宋体"}

[[\<Sysname\> reset rsvp authentication]{lang="ES"}]{#struct_0_16315_x4274_1639035372}

[[\# ]{lang="ES"}]{#struct_0_16315_x4274_x479998438}[清除认证发起节点]{style="font-family:宋体"}[IP]{lang="ES"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="ES"}[、认证目的节点]{style="font-family:宋体"}[IP]{lang="ES"}[地址为]{style="font-family:宋体"}[2.2.2.2]{lang="ES"}[的]{style="font-family:宋体"}[RSVP SA]{lang="ES"}[。]{style="font-family:宋体"}

[[\<Sysname\> reset rsvp authentication from 1.1.1.1 to 2.2.2.2]{lang="EN-US"}]{#struct_0_16315_x4274_671768075}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1763645836}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[rsvp authentication]{lang="EN-US"}**]{#struct_0_16315_x4274_x1075978944}
:::

::: {#1798009966 .myid}
[]{#_Toc404791065}[]{#struct_0_16315_x4274_749003992}[]{#_Toc333936436}[]{#_Toc328505107}[]{#_Toc324951734}

**RSVP \-- RSVP配置命令 \-- reset rsvp statistics**

------------------------------------------------------------------------

[**[reset]{lang="EN-US"}**[ **rsvp** **statistics**]{lang="EN-US"}]{#struct_0_16315_x4274_746137010}[命令用来清除]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1065761253}

[**[reset]{lang="EN-US"}**[ **rsvp** **statistics** \[ **interface** \[ *interface-type* *interface-number* \] \]]{lang="EN-US"}]{#struct_0_16315_x4274_x1269512181}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16315_x4274_2059066474}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16315_x4274_x1887019787}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16315_x4274_624932753}

[[network-admin]{lang="EN-US"}]{#struct_0_16315_x4274_1365892776}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16315_x4274_x476169217}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16315_x4274_748938456}

[**[interface]{lang="EN-US"}**]{#struct_0_16315_x4274_x1184419847}[：清除接口的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_16315_x4274_882731050}[：清除指定接口的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型及接口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1842983478}

[[执行]{style="font-family:宋体"}**[reset]{lang="EN-US"}**[ **rsvp statistics**]{lang="EN-US"}]{#struct_0_16315_x4274_78479765}[命令时：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{style="font-family:宋体"}]{#struct_0_16315_x4274_2087876538}**[interface]{lang="EN-US"}**[参数，则清除全局的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[如果只指定]{style="font-family:宋体"}**[interface]{lang="EN-US"}**]{#struct_0_16315_x4274_1641108258}[参数，不指定]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[参数，则清除所有开启了]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[能力的接口的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[如果指定]{style="font-family:宋体"}**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_16315_x4274_x15210351}[参数，则清除指定接口的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16315_x4274_748479705}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_1837284085}[清除全局的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset rsvp statistics]{lang="EN-US"}]{#struct_0_16315_x4274_250888937}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_1086730092}[清除所有开启了]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[能力的接口的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset rsvp statistics interface]{lang="EN-US"}]{#struct_0_16315_x4274_x1489340662}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1106737752}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display rsvp]{lang="EN-US"}**[ **statistics**]{lang="EN-US"}]{#struct_0_16315_x4274_x1825911542}
:::

::: {#8383562 .myid}
[]{#_Toc404791066}[]{#struct_0_16315_x4274_x1780542170}[]{#_Toc333936437}[]{#_Toc328505108}[]{#_Toc324951735}

**RSVP \-- RSVP配置命令 \-- rsvp**

------------------------------------------------------------------------

[**[rsvp]{lang="EN-US"}**]{#struct_0_16315_x4274_484682871}[命令用来全局开启]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[能力，并进入]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo rsvp]{lang="EN-US"}**]{#struct_0_16315_x4274_748414169}[命令用来全局关闭]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1080611441}

[**[rsvp]{lang="EN-US"}**]{#struct_0_16315_x4274_x323949625}

[**[undo rsvp]{lang="EN-US"}**]{#struct_0_16315_x4274_x947578066}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1118549513}

[[全局]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_1142764736}[能力处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1425313524}

[[系统视图]{style="font-family:宋体"}]{#struct_0_16315_x4274_x1252279028}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1816075041}

[[network-admin]{lang="EN-US"}]{#struct_0_16315_x4274_748348633}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16315_x4274_1196443195}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1950549409}

[[全局开启]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x1777445294}[能力时，需要同时通过]{style="font-family:宋体"}**[mpls te]{lang="EN-US"}**[命令全局开启]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x801377144}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_x2012721450}[全局开启]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[能力，并进入]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16315_x4274_198675959}

[\[Sysname\] rsvp]{lang="EN-US"}

[\[Sysname-rsvp\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x23836979}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mpls te]{lang="EN-US"}**]{#struct_0_16315_x4274_748283097}[（]{style="font-family:
宋体"}[MPLS]{lang="EN-US"}[命令参考]{style="font-family:宋体"}[/MPLS TE]{lang="EN-US"}[）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp enable]{lang="EN-US"}**]{#struct_0_16315_x4274_x1499898123}
:::

::: {#1201977996 .myid}
[]{#_Toc404791067}[]{#struct_0_16315_x4274_x2097863939}[]{#_Toc333936438}[]{#_Toc328505109}[]{#_Toc324951736}

**RSVP \-- RSVP配置命令 \-- rsvp authentication challenge**

------------------------------------------------------------------------

[**[rsvp authentication challenge]{lang="ES"}**]{#struct_0_16315_x4274_279633650}[命令用来在接口下开启]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[认证的]{style="font-family:宋体"}[challenge-response]{lang="EN-US"}[握手功能。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_16315_x4274_x855362370}**[rsvp authentication challenge]{lang="ES"}**[命令用来在接口下关闭]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[认证的]{style="font-family:宋体"}[challenge-response]{lang="EN-US"}[握手功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1121122055}

[**[rsvp authentication challenge]{lang="ES"}**]{#struct_0_16315_x4274_358562020}

[**[undo rsvp authentication challenge]{lang="ES"}**]{#struct_0_16315_x4274_x1078366415}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16315_x4274_174221995}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_748217561}[认证的]{style="font-family:宋体"}[challenge-response]{lang="EN-US"}[握手功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1923373867}

[[接口视图]{style="font-family:宋体"}]{#struct_0_16315_x4274_1589696123}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1793367965}

[[network-admin]{lang="EN-US"}]{#struct_0_16315_x4274_1211499521}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16315_x4274_199505120}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1731206126}

[[为了避免报文的重放（]{style="font-family:宋体"}[Replay]{lang="EN-US"}]{#struct_0_16315_x4274_737798552}[）攻击，]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[接收认证消息时要求认证消息的序列号依次增加，]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[在接收]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[中保存最后一次收到的消息的序列号，用于判断后续消息是否符合要求。但是，在新创建接收]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[的时候，无法获取发送端的序列号，因此缺省情况下，创建接收]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[时将接收序列号填写为零，这样对端发送任意序列号的消息就都能接收。这就增加了重放攻击的风险。为了避免这种风险，可以执行]{style="font-family:宋体"}**[authentication challenge]{lang="ES"}**[命令，使得在新建接收]{style="font-family:宋体"}[RSVP SA]{lang="ES"}[时]{style="font-family:宋体"}[执行]{style="font-family:宋体"}[challenge-response]{lang="ES"}[握手过程，]{style="font-family:宋体"}[获取发送端的序列号。]{style="font-family:宋体"}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_1914272317}[认证的]{style="font-family:宋体"}[challenge-response]{lang="EN-US"}[握手功能可以在如下视图配置：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x98466646}[视图：该视图下的配置对所有]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x98532182}[邻居视图：该视图下的配置只对与指定]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居之间的]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口视图：该视图下的配置只对根据指定接口下的配置生成的]{style="font-family:宋体"}]{#struct_0_16315_x4274_x98597718}[RSVP SA]{lang="EN-US"}[生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16315_x4274_991573779}

[[·[              ]{style="font:7.0pt "}]{lang="ES" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_16315_x4274_x388655248}

[[\# ]{lang="ES"}]{#struct_0_16315_x4274_x858354633}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="ES"}[上开启]{style="font-family:宋体"}[RSVP]{lang="ES"}[认证的]{style="font-family:宋体"}[challenge-response]{lang="ES"}[握手功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="ES"}]{#struct_0_16315_x4274_x1383981121}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="ES"}

[\[Sysname-GigabitEthernet1/0/1\] rsvp authentication challenge]{lang="ES"}

[[·[              ]{style="font:7.0pt "}]{lang="ES" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_16315_x4274_x602463209}

[[\# ]{lang="ES"}]{#struct_0_16315_x4274_1254915270}[在接口]{style="font-family:宋体"}[Vlan-interface10]{lang="ES"}[上开启]{style="font-family:宋体"}[RSVP]{lang="ES"}[认证的]{style="font-family:宋体"}[challenge-response]{lang="ES"}[握手功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="ES"}]{#struct_0_16315_x4274_748086489}

[\[Sysname\] interface vlan-interface 10]{lang="ES"}

[\[Sysname-Vlan-interface10\] rsvp authentication challenge]{lang="ES"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1774243497}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication challenge]{lang="EN-US"}**]{#struct_0_16315_x4274_1671653634}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication key]{lang="EN-US"}**]{#struct_0_16315_x4274_x1674204834}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication lifetime]{lang="EN-US"}**]{#struct_0_16315_x4274_x775131924}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication window-size]{lang="EN-US"}**]{#struct_0_16315_x4274_x1719235230}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display rsvp authentication]{lang="EN-US"}**]{#struct_0_16315_x4274_1004798574}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ]{lang="EN-US"}[rsvp authentication]{lang="EN-US"}**]{#struct_0_16315_x4274_x864892824}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp authentication key]{lang="EN-US"}**]{#struct_0_16315_x4274_748020953}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp authentication lifetime]{lang="EN-US"}**]{#struct_0_16315_x4274_1371811182}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp authentication window-size]{lang="EN-US"}**]{#struct_0_16315_x4274_x436027540}
:::

::: {#1621276223 .myid}
[]{#_Toc404791068}[]{#struct_0_16315_x4274_201360346}[]{#_Toc333936439}[]{#_Toc328505110}[]{#_Toc324951737}

**RSVP \-- RSVP配置命令 \-- rsvp authentication key**

------------------------------------------------------------------------

[**[rsvp authentication key]{lang="EN-US"}**]{#struct_0_16315_x4274_x1319855337}[命令用来在接口下开启]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[认证功能，并配置认证密钥。]{style="font-family:宋体"}

[**[undo rsvp authentication key]{lang="EN-US"}**]{#struct_0_16315_x4274_1717381564}[命令用来在接口下关闭]{style="font-family:
宋体"}[RSVP]{lang="EN-US"}[认证功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_187666606}

[**[rsvp authentication key ]{lang="EN-US"}**[{ **cipher** \| **plain** } *auth-key*]{lang="EN-US"}]{#struct_0_16315_x4274_393932897}

[**[undo rsvp authentication key]{lang="EN-US"}**]{#struct_0_16315_x4274_x1793281781}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16315_x4274_749003993}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_746137009}[认证功能处于关闭状态，即不进行]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x890553874}

[[接口视图]{style="font-family:宋体"} ]{#struct_0_16315_x4274_x1614886856}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16315_x4274_83981339}

[[network-admin]{lang="EN-US"}]{#struct_0_16315_x4274_x17830937}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16315_x4274_x28776270}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1202562089}

[**[cipher]{lang="EN-US"}**]{#struct_0_16315_x4274_1350159598}[：表示以密文形式设置密钥。]{style="font-family:宋体"}

[**[plain]{lang="EN-US"}**]{#struct_0_16315_x4274_748938457}[：表示以明文形式设置密钥。]{style="font-family:宋体"}

[*[auth-key]{lang="EN-US"}*]{#struct_0_16315_x4274_x1184419846}[：认证密钥，区分大小写。如果采用明文（]{style="font-family:宋体"}**[plain]{lang="EN-US"}**[）形式，则为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[个字符的明文字符串；如果采用密文（]{style="font-family:宋体"}**[cipher]{lang="EN-US"}**[）形式，则为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[53]{lang="EN-US"}[个字符的密文字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x683352891}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x53126295}[认证功能可以用来确保]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息不会被篡改，]{style="font-family:宋体"}[防止伪造的资源预留请求非法占用网络资源。]{style="font-family:宋体"}

[[配置]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x1930441949}[认证功能后，发送]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息时会使用]{style="font-family:宋体"}[MD5]{lang="EN-US"}[算法对]{style="font-family:宋体"}[认证密钥和消息内容计算出消息摘要，并将消息摘要添加到发送的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息中。对端接收到]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息后，也进行同样地计算，并将计算结果和消息中的摘要进行比较。如果一致，则认证通过，接收该消息；否则认证失败，丢弃该消息。]{style="font-family:宋体"}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x360396056}[认证功能可以在如下视图配置：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x97876822}[视图：该视图下的配置对所有]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x97942358}[邻居视图：该视图下的配置只对与指定]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居之间的]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口视图：该视图下的配置只对根据指定接口下的配置生成的]{style="font-family:宋体"}]{#struct_0_16315_x4274_2015655714}[RSVP SA]{lang="EN-US"}[生效。]{style="font-family:宋体"}

[[如果在多个视图下配置了认证密钥，则认证密钥的使用优先级顺序从高到低依次为：]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_748479702}[邻居视图、接口视图、]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[视图。例如，如果在]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居视图和]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[视图都开启了与特定邻居的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[认证功能，并配置了不同的认证密钥，则采用]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居视图下配置的密钥认证本地设备和该邻居之间的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[[如果已经采用某个视图下配置的认证密钥建立了]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}]{#struct_0_16315_x4274_1837284086}[，则只有先删除当前视图下配置的认证密钥或执行]{style="font-family:宋体"}**[reset rsvp authentication]{lang="EN-US"}**[命令删除该]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[，才会按照上述优先级顺序重新查找新的认证密钥并建立]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_16315_x4274_250823401}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本地设备上开启]{style="font-family:宋体"}]{#struct_0_16315_x4274_x1609635439}[RSVP]{lang="EN-US"}[认证功能后，在相应的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居上也需要开启]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[认证功能，并配置相同的认证密钥。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以明文或密文形式设置的密钥，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_16315_x4274_x1659774582}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x508157511}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_16315_x4274_1533628078}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_1392753067}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上开启]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[认证功能，并配置认证密钥为]{style="font-family:宋体"}[abcdefgh]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16315_x4274_748414166}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] rsvp authentication key plain abcdefgh]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_16315_x4274_1080611430}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_x324015160}[在接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上开启]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[认证功能，并配置认证密钥为]{style="font-family:宋体"}[abcdefgh]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16315_x4274_2090836641}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] rsvp authentication key plain abcdefgh]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x972737442}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication challenge]{lang="EN-US"}**]{#struct_0_16315_x4274_466045349}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication key]{lang="EN-US"}**]{#struct_0_16315_x4274_1314037012}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication lifetime]{lang="EN-US"}**]{#struct_0_16315_x4274_x635078209}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication window-size]{lang="EN-US"}**]{#struct_0_16315_x4274_748348630}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display rsvp authentication]{lang="EN-US"}**]{#struct_0_16315_x4274_1196443198}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ]{lang="EN-US"}[rsvp authentication]{lang="EN-US"}**]{#struct_0_16315_x4274_x1949828513}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp authentication challenge]{lang="EN-US"}**]{#struct_0_16315_x4274_x503614445}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp authentication lifetime]{lang="EN-US"}**]{#struct_0_16315_x4274_x1200307181}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp authentication window-size]{lang="EN-US"}**]{#struct_0_16315_x4274_1125201865}
:::

::: {#689419488 .myid}
[]{#_Toc404791069}[]{#struct_0_16315_x4274_1481877695}[]{#_Toc333936440}[]{#_Toc328505111}[]{#_Toc324951738}

**RSVP \-- RSVP配置命令 \-- rsvp authentication lifetime**

------------------------------------------------------------------------

[**[rsvp authentication lifetime]{lang="EN-US"}**]{#struct_0_16315_x4274_1724306498}[命令用来在接口下配置]{style="font-family:
宋体"}[RSVP SA]{lang="EN-US"}[的空闲老化时间。]{style="font-family:
宋体"}

[**[undo rsvp]{lang="EN-US"}**[ **authentication lifetime**]{lang="EN-US"}]{#struct_0_16315_x4274_x1327805757}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_748283094}

[**[rsvp authentication lifetime ]{lang="EN-US"}***[life-time]{lang="EN-US"}*]{#struct_0_16315_x4274_x1499898120}

[**[undo rsvp ]{lang="ES"}[authentication lifetime]{lang="EN-US"}**]{#struct_0_16315_x4274_631019416}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16315_x4274_752662957}

[[RSVP SA]{lang="EN-US"}]{#struct_0_16315_x4274_1374958245}[的空闲老化时间为]{style="font-family:宋体"}[1800]{lang="EN-US"}[秒（]{style="font-family:宋体"}[30]{lang="EN-US"}[分钟）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x641495284}

[[接口视图]{style="font-family:宋体"}]{#struct_0_16315_x4274_13808516}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1117266872}

[[network-admin]{lang="EN-US"}]{#struct_0_16315_x4274_955031685}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16315_x4274_748217558}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16315_x4274_32941276}

[*[life-time]{lang="EN-US"}*]{#struct_0_16315_x4274_x2037072566}[：]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[的空闲老化时间，取值范围为]{style="font-family:宋体"}[30]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1923258630}

[[开启了]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_1243732215}[认证功能后，设备收发]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息时会动态建立]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[，以记录消息的序列号、方便对]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息进行认证处理。]{style="font-family:宋体"}

[[为了在不需要]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}]{#struct_0_16315_x4274_x1744086464}[的时候，能够及时删除该]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[，回收内存资源，每个]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[都有其老化时间。当]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[的空闲时间到达老化时间时，将删除该]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[。设备发送和接收]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[认证消息时，会更新对应]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[的空闲时间，避免其被老化删除。]{style="font-family:宋体"}

[[RSVP SA]{lang="EN-US"}]{#struct_0_16315_x4274_844349712}[的空闲老化时间可以在如下视图配置：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_834737650}[视图：该视图下的配置对所有]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_2121966110}[邻居视图：该视图下的配置只对与指定]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居之间的]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口视图：该视图下的配置只对根据指定接口下的配置生成的]{style="font-family:宋体"}]{#struct_0_16315_x4274_748152022}[RSVP SA]{lang="EN-US"}[生效。]{style="font-family:宋体"}

[[采用某个视图下配置的认证密钥建立]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}]{#struct_0_16315_x4274_x1412801205}[后，该]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[的空闲老化时间为该视图下配置的老化时间。]{style="font-family:宋体"}

[[修改]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}]{#struct_0_16315_x4274_x2018830036}[的空闲老化时间后，只会对新建立的]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[生效。要想使得修改后的空闲老化时间对已建立的]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[生效，则需要执行]{style="font-family:宋体"}**[reset rsvp authentication]{lang="EN-US"}**[命令来删除并重新建立]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1599460518}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_16315_x4274_1912035369}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_x658480388}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[的空闲老化时间为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16315_x4274_x1195707760}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] rsvp authentication lifetime 100]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_16315_x4274_x804608238}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_748086486}[在接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上配置]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[的空闲老化时间为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16315_x4274_x1774243486}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] rsvp authentication lifetime 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_105504157}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication challenge]{lang="EN-US"}**]{#struct_0_16315_x4274_1493741691}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication key]{lang="EN-US"}**]{#struct_0_16315_x4274_1741087658}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication lifetime]{lang="EN-US"}**]{#struct_0_16315_x4274_x2089157421}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication window-size]{lang="EN-US"}**]{#struct_0_16315_x4274_x66428362}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display rsvp authentication]{lang="EN-US"}**]{#struct_0_16315_x4274_x1326481808}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ]{lang="EN-US"}[rsvp authentication]{lang="EN-US"}**]{#struct_0_16315_x4274_748020950}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp authentication challenge]{lang="EN-US"}**]{#struct_0_16315_x4274_1371811181}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp authentication key]{lang="EN-US"}**]{#struct_0_16315_x4274_x435962004}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp authentication window-size]{lang="EN-US"}**]{#struct_0_16315_x4274_x1617310674}
:::

::: {#-1457438101 .myid}
[]{#_Toc404791070}[]{#struct_0_16315_x4274_x2077808859}[]{#_Toc333936441}[]{#_Toc328505112}[]{#_Toc324951739}

**RSVP \-- RSVP配置命令 \-- rsvp authentication window-size**

------------------------------------------------------------------------

[**[rsvp authentication window-size]{lang="EN-US"}**]{#struct_0_16315_x4274_959720652}[命令用来在接口下配置对于带有认证信息的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息，最大可允许的乱序消息数量。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rsvp authentication window-size**]{lang="EN-US"}]{#struct_0_16315_x4274_x1833803862}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x114686440}

[**[rsvp authentication window-size ]{lang="ES"}***[number]{lang="EN-US"}*]{#struct_0_16315_x4274_x1300513767}

[**[undo rsvp authentication window-size]{lang="ES"}**]{#struct_0_16315_x4274_749003990}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16315_x4274_746137012}

[[对于带有认证信息的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_1065761251}[消息，最大可允许的乱序消息数量为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1269643253}

[[接口视图]{style="font-family:宋体"}]{#struct_0_16315_x4274_2117230636}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16315_x4274_987166817}

[[network-admin]{lang="EN-US"}]{#struct_0_16315_x4274_x1513706098}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16315_x4274_x1749737631}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1875545551}

[*[number]{lang="EN-US"}*]{#struct_0_16315_x4274_748938454}[：最大可允许的乱序消息数量，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1184419845}

[[为了防止报文重放攻击，]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x280068364}[在带有认证信息的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息中携带唯一的序列号。每发送一个消息，序列号依次增加。如果接收到的消息序列号在允许的范围内，则接受该消息；否则，丢弃该消息。]{style="font-family:宋体"}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x833446100}[判断报文序列号是否在允许范围内的方法为：]{style="font-family:宋体"}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[在设备上记录最后一次接收到的]{style="font-family:宋体"}]{#struct_0_16315_x4274_x1484588707}[RSVP]{lang="EN-US"}[报文的序列号。]{style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[设备接收到新的]{style="font-family:宋体"}]{#struct_0_16315_x4274_x13435645}[RSVP]{lang="EN-US"}[报文时，将该报文的序列号与记录的序列号进行比较：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果大于记录的序列号，则将记录的序列号更新为该报文的序列号。]{style="font-family:宋体"}]{#struct_0_16315_x4274_389871873}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果等于记录的序列号，则认为是重放攻击，丢弃该报文。]{style="font-family:宋体"}]{#struct_0_16315_x4274_1755360117}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果小于记录的序列号、大于（记录的序列号---本命令配置的]{style="font-family:宋体"}]{#struct_0_16315_x4274_x1482808014}[window-size]{lang="EN-US"}[），且未收到过该序列号的报文，则接收该报文；若已经收到过该序列号的报文，则认为是重放攻击，丢弃该报文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果小于等于（记录的序列号---本命令配置的]{style="font-family:宋体"}]{#struct_0_16315_x4274_748479703}[window-size]{lang="EN-US"}[），则认为报文序列号不合法，丢弃该报文。]{style="font-family:宋体"}

[[缺省情况下，最大可允许的乱序消息数量为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_16315_x4274_1837284087}[，即]{style="font-family:宋体"}[如果新收到的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息的序列号小于最后收到的消息序列号，则认为该消息是重放攻击，丢弃该消息。但是，如果在短时间内发送了多个]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息，那么这些消息到达邻居时可能会产生乱序。若采用缺省情况，则会导致这些乱序消息被丢弃。此时，可以通过本命令配置较大的]{style="font-family:宋体"}[window-size]{lang="EN-US"}[解决此问题。]{style="font-family:宋体"}

[[采用某个视图下配置的认证密钥建立]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}]{#struct_0_16315_x4274_250757865}[后，该]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[的最大可允许乱序消息数量为该视图下配置的值。]{style="font-family:宋体"}

[[修改最大可允许的乱序消息数量后，只会对新建立的]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}]{#struct_0_16315_x4274_x236471192}[生效。要想使得修改后的最大可允许乱序消息数量对已建立的]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[生效，则需要执行]{style="font-family:宋体"}**[reset rsvp authentication]{lang="EN-US"}**[命令来删除并重新建立]{style="font-family:宋体"}[RSVP SA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16315_x4274_740322815}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_16315_x4274_x1769033987}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_x1758973939}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置对于带有认证信息的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息，最大可允许的乱序消息数量为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16315_x4274_196418864}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] rsvp authentication window-size 10]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_16315_x4274_748414167}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_1080611431}[在接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上配置对于带有认证信息的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息，最大可允许的乱序消息数量为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16315_x4274_x323949624}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] rsvp authentication window-size 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x947643602}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication challenge]{lang="EN-US"}**]{#struct_0_16315_x4274_1175297269}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication key]{lang="EN-US"}**]{#struct_0_16315_x4274_2139978834}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication lifetime]{lang="EN-US"}**]{#struct_0_16315_x4274_31501350}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication window-size]{lang="EN-US"}**]{#struct_0_16315_x4274_x974402036}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display rsvp authentication]{lang="EN-US"}**]{#struct_0_16315_x4274_1895689142}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ]{lang="EN-US"}[rsvp authentication]{lang="EN-US"}**]{#struct_0_16315_x4274_748348631}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp authentication challenge]{lang="EN-US"}**]{#struct_0_16315_x4274_1196443197}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp authentication key]{lang="EN-US"}**]{#struct_0_16315_x4274_x1950680481}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp authentication lifetime]{lang="EN-US"}**]{#struct_0_16315_x4274_x209656554}
:::

::: {#-1306000727 .myid}
[]{#_Toc404791071}[]{#struct_0_16315_x4274_x454239523}[]{#_Toc333936442}[]{#_Toc328505113}[]{#_Toc324951740}

**RSVP \-- RSVP配置命令 \-- rsvp bfd enable**

------------------------------------------------------------------------

[**[rsvp bfd enable]{lang="EN-US"}**]{#struct_0_16315_x4274_1168187938}[命令用来配置通过]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测本地设备和]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居之间链路的状态。]{style="font-family:宋体"}

[**[undo rsvp bfd enable]{lang="EN-US"}**]{#struct_0_16315_x4274_1277789161}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_209984313}

[**[rsvp bfd enable]{lang="ES"}**]{#struct_0_16315_x4274_x743969450}

[**[undo rsvp bfd enable]{lang="ES"}**]{#struct_0_16315_x4274_748283095}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1499898121}

[[不会通过]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_16315_x4274_x935064525}[检测本地设备和]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居之间链路的状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1822159035}

[[接口视图]{style="font-family:宋体"}]{#struct_0_16315_x4274_x759574169}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1354178563}

[[network-admin]{lang="EN-US"}]{#struct_0_16315_x4274_x460469812}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16315_x4274_x830148346}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1017739548}

[[通常情况下，]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_748217559}[通过]{style="font-family:宋体"}[Hello]{lang="EN-US"}[消息检测邻居的状态，]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[无法及时感知邻居的故障。执行本命令后，设备上会建立]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话，通过]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话来检测本地设备和]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居之间链路的状态。当]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居出现故障时，]{style="font-family:宋体"}[BFD]{lang="EN-US"}[能够快速检测到该故障，并通知]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[进行相应的处理（例如，配置了]{style="font-family:宋体"}[FRR]{lang="EN-US"}[保护时，会进行]{style="font-family:宋体"}[FRR]{lang="EN-US"}[切换）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16315_x4274_32941277}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_16315_x4274_301579594}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_2083478171}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置通过]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测本地设备和]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居之间链路的状态。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16315_x4274_350733980}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] rsvp bfd enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_16315_x4274_865154169}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_1738918322}[在接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上配置通过]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测本地设备和]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居之间链路的状态。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16315_x4274_748152023}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] rsvp bfd enable]{lang="EN-US"}
:::

::: {#-1819692363 .myid}
[]{#_Toc404791072}[]{#struct_0_16315_x4274_x1412801204}[]{#_Toc333936443}[]{#_Toc328505114}[]{#_Toc324951741}

**RSVP \-- RSVP配置命令 \-- rsvp enable**

------------------------------------------------------------------------

[**[rsvp enable]{lang="EN-US"}**]{#struct_0_16315_x4274_710053319}[命令用来开启接口的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[**[undo rsvp enable]{lang="EN-US"}**]{#struct_0_16315_x4274_x1146448593}[命令用来关闭接口的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x2036772156}

[**[rsvp enable]{lang="EN-US"}**]{#struct_0_16315_x4274_1916836135}

[**[undo rsvp enable]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_16315_x4274_1060564308}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1417927275}

[[接口的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x1830984409}[能力处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16315_x4274_748086487}

[[接口视图]{style="font-family:宋体"}]{#struct_0_16315_x4274_x1774243487}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1671588098}

[[network-admin]{lang="EN-US"}]{#struct_0_16315_x4274_x113012846}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16315_x4274_x1097602945}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1987336120}

[[必须先在系统视图下通过]{style="font-family:宋体"}**[rsvp]{lang="EN-US"}**]{#struct_0_16315_x4274_x1582669619}[命令全局开启]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[能力，才能开启接口的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x28398205}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_16315_x4274_1734564886}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_748020951}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上开启]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16315_x4274_1371811180}

[\[Sysname\] rsvp]{lang="EN-US"}

[\[Sysname-rsvp\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] rsvp enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_16315_x4274_x435896468}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_1093335519}[在接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上开启]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16315_x4274_x1914521950}

[\[Sysname\] rsvp]{lang="EN-US"}

[\[Sysname-rsvp\] quit]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] rsvp enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1426844185}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp]{lang="EN-US"}**]{#struct_0_16315_x4274_x1263839923}
:::

::: {#176082248 .myid}
[]{#_Toc404791073}[]{#struct_0_16315_x4274_749003991}[]{#_Toc333936445}[]{#_Toc328505116}[]{#_Toc324951743}

**RSVP \-- RSVP配置命令 \-- rsvp hello enable**

------------------------------------------------------------------------

[**[rsvp hello enable]{lang="EN-US"}**]{#struct_0_16315_x4274_746137011}[命令用来开启]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[扩展功能。]{style="font-family:宋体"}

[**[undo rsvp hello enable]{lang="EN-US"}**]{#struct_0_16315_x4274_1065761254}[命令用来关闭]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[扩展功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1269839861}

[**[rsvp hello enable]{lang="EN-US"}**]{#struct_0_16315_x4274_x1315902361}

[**[undo rsvp hello enable]{lang="EN-US"}**]{#struct_0_16315_x4274_1513564767}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1697240811}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_1714837743}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[扩展功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1800370363}

[[接口视图]{style="font-family:宋体"}]{#struct_0_16315_x4274_748938455}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1184419844}

[[network-admin]{lang="EN-US"}]{#struct_0_16315_x4274_x1846152305}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16315_x4274_x1182281144}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x587394057}

[[在接口视图下开启]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_1109726991}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[扩展功能后，设备会通过该接口发送和接收]{style="font-family:宋体"}[Hello]{lang="EN-US"}[消息，通过]{style="font-family:宋体"}[Hello]{lang="EN-US"}[消息检测邻居的状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1788087480}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_16315_x4274_1621546298}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_x1244313075}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上开启]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[扩展功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16315_x4274_x1980403649}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] rsvp hello enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_16315_x4274_x430246733}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_227997880}[在接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上开启]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[扩展功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16315_x4274_x1172929947}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] rsvp hello enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1298158249}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hello lost]{lang="EN-US"}**]{#struct_0_16315_x4274_x1016801775}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hello interval]{lang="EN-US"}**]{#struct_0_16315_x4274_x921282609}
:::

::: {#-358072250 .myid}
[]{#_Toc404791074}[]{#struct_0_16315_x4274_1039198700}[]{#_Toc333936446}[]{#_Toc328505117}[]{#_Toc324951744}

**RSVP \-- RSVP配置命令 \-- rsvp reduction retransmit increment**

------------------------------------------------------------------------

[**[rsvp]{lang="EN-US"}**[ **reduction retransmit** **increment**]{lang="EN-US"}]{#struct_0_16315_x4274_x1980469185}[命令用来配置]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息可靠传递功能的重传增量。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rsvp** **reduction retransmit** **increment**]{lang="EN-US"}]{#struct_0_16315_x4274_x793778034}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x942177940}

[**[rsvp reduction retransmit]{lang="EN-US"}**[ **increment** *increment-value*]{lang="EN-US"}]{#struct_0_16315_x4274_x507065920}[]{#_Toc312767118}

[**[undo ]{lang="EN-US"}**]{#struct_0_16315_x4274_509818758}[]{#_Toc312767119}**[rsvp reduction retransmit]{lang="EN-US"}**[ **increment**]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16315_x4274_406633517}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x1791195734}[消息可靠传递功能的重传增量为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x561478623}

[[接口视图]{style="font-family:宋体"}]{#struct_0_16315_x4274_x1835828115}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1980534721}

[[network-admin]{lang="EN-US"}]{#struct_0_16315_x4274_1027502499}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16315_x4274_1157110908}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16315_x4274_755246322}

[*[increment-value]{lang="EN-US"}*]{#struct_0_16315_x4274_761834707}[：重传增量，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}[]{#_Toc312767125}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16315_x4274_171139037}

[[通过]{style="font-family:宋体"}**[rsvp reduction srefresh]{lang="EN-US"}**[ **reliability**]{lang="EN-US"}]{#struct_0_16315_x4274_x1039792824}[命令]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息的可靠传递功能后，重传增量和重传时间间隔共同决定了下一次重传消息的时间，详细介绍请参见"]{style="font-family:宋体"}[[1.1.32  ]{lang="EN-US"}](?-1914564316#_Ref327966342)[[rsvp reduction srefresh]{lang="EN-US"}](?-1914564316#_Ref327966357)["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x520996057}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_16315_x4274_1787369601}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_x1980600257}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息可靠传递功能的重传增量为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16315_x4274_603577837}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] rsvp reduction retransmit increment 2]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_16315_x4274_181705572}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_x1050975496}[在接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上配置]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息可靠传递功能的重传增量为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16315_x4274_x156103527}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] rsvp reduction retransmit increment 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:
黑体"}]{#struct_0_16315_x4274_x748493}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp reduction retransmit interval]{lang="EN-US"}**]{#struct_0_16315_x4274_x1622622730}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp reduction srefresh]{lang="EN-US"}**]{#struct_0_16315_x4274_x1980665793}
:::

::: {#383966402 .myid}
[]{#_Toc404791075}[]{#struct_0_16315_x4274_x346554538}[]{#_Toc333936447}[]{#_Toc328505118}[]{#_Toc324951745}

**RSVP \-- RSVP配置命令 \-- rsvp reduction retransmit interval**

------------------------------------------------------------------------

[**[rsvp]{lang="EN-US"}**[ **reduction retransmit** **interval**]{lang="EN-US"}]{#struct_0_16315_x4274_120209090}[命令用来配置]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息可靠传递功能的重传时间间隔。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rsvp** **reduction retransmit** **interval**]{lang="EN-US"}]{#struct_0_16315_x4274_370615274}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1928802830}

[**[rsvp reduction retransmit]{lang="EN-US"}**[ **interval** *retrans-timer-value*]{lang="EN-US"}]{#struct_0_16315_x4274_x743498737}

[**[undo rsvp reduction retransmit]{lang="EN-US"}**[ **interval**]{lang="EN-US"}]{#struct_0_16315_x4274_2009577000}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1221686621}

[[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x1749005722}[消息可靠传递功能的重传时间间隔为]{style="font-family:宋体"}[500]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1980731329}

[[接口视图]{style="font-family:宋体"}]{#struct_0_16315_x4274_5885135}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1830703559}

[[network-admin]{lang="EN-US"}]{#struct_0_16315_x4274_x61472033}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16315_x4274_x1471622468}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1927117637}

[*[retrans-timer-value]{lang="EN-US"}*]{#struct_0_16315_x4274_1466679077}[：重传时间间隔，取值范围为]{style="font-family:宋体"}[500]{lang="EN-US"}[～]{style="font-family:宋体"}[3000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1500586822}

[[通过]{style="font-family:宋体"}**[rsvp reduction srefresh]{lang="EN-US"}**[ **reliability**]{lang="EN-US"}]{#struct_0_16315_x4274_x1430975362}[命令]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息的可靠传递功能后，重传增量和重传时间间隔共同决定了下一次重传消息的时间，详细介绍请参见"]{style="font-family:宋体"}[[1.1.32  ]{lang="EN-US"}](?-1914564316#_Ref327966342)[[rsvp reduction srefresh]{lang="EN-US"}](?-1914564316#_Ref327966357)["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1980796865}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_16315_x4274_x179540144}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_x460389788}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息可靠传递功能的重传时间间隔为]{style="font-family:宋体"}[1000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16315_x4274_1862267054}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] rsvp reduction retransmit interval 1000]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_16315_x4274_1281983566}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_1095893426}[在接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上配置]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息可靠传递功能的重传时间间隔为]{style="font-family:宋体"}[1000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16315_x4274_1485830614}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] rsvp reduction retransmit interval 1000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x111708567}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp reduction retransmit increment]{lang="EN-US"}**]{#struct_0_16315_x4274_x1980862401}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp reduction srefresh]{lang="EN-US"}**]{#struct_0_16315_x4274_x1655761377}
:::

::: {#-1914564316 .myid}
[]{#_Toc404791076}[]{#struct_0_16315_x4274_x384137469}[]{#_Toc333936448}[]{#_Toc328505119}[]{#_Ref327966357}[]{#_Ref327966342}[]{#_Toc324951746}

**RSVP \-- RSVP配置命令 \-- rsvp reduction srefresh**

------------------------------------------------------------------------

[**[rsvp reduction srefresh]{lang="EN-US"}**]{#struct_0_16315_x4274_x1751997902}[命令用来开启摘要刷新（]{style="font-family:宋体"}[Summary Refresh]{lang="EN-US"}[）功能和]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息的可靠传递功能。]{style="font-family:宋体"}

[**[undo rsvp]{lang="EN-US"}**[ **reduction srefresh**]{lang="EN-US"}]{#struct_0_16315_x4274_1139675012}[命令用来关闭摘要刷新功能和]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息的可靠传递功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1681509841}

[**[rsvp reduction srefresh]{lang="EN-US"}**]{#struct_0_16315_x4274_x1087158643}[]{#_Toc312767144}[ \[ **reliability** \]]{lang="EN-US"}

[**[undo rsvp reduction srefresh]{lang="EN-US"}**]{#struct_0_16315_x4274_1254193344}[]{#_Toc312767145}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1979879361}

[[摘要刷新功能和]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x999858869}[消息的可靠传递功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1638104625}

[[接口视图]{style="font-family:宋体"}]{#struct_0_16315_x4274_1137781000}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x892428257}

[[network-admin]{lang="EN-US"}]{#struct_0_16315_x4274_x196902576}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16315_x4274_1551973711}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1828534761}

[**[reliability]{lang="EN-US"}**]{#struct_0_16315_x4274_x1223793764}[：开启]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息的可靠传递功能。如果不指定本参数，则只开启摘要刷新功能。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1979944897}

[[通常情况下，]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_x1401709563}[发送]{style="font-family:宋体"}[Path]{lang="EN-US"}[和]{style="font-family:宋体"}[Resv]{lang="EN-US"}[消息后，会周期性地（由]{style="font-family:宋体"}**[refresh interval]{lang="EN-US"}**[命令配置）发送带有同样状态、对象等信息的]{style="font-family:宋体"}[Path]{lang="EN-US"}[和]{style="font-family:宋体"}[Resv]{lang="EN-US"}[消息来维护路径和预留状态，该消息统称为]{style="font-family:宋体"}[Refresh]{lang="EN-US"}[消息。]{style="font-family:宋体"}[Refresh]{lang="EN-US"}[消息不仅用于在]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[邻居节点进行状态同步，也用于恢复丢失的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[[由于]{style="font-family:宋体"}[Refresh]{lang="EN-US"}]{#struct_0_16315_x4274_1820471316}[消息是周期性发送的，当网络中的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[会话比较多时，]{style="font-family:宋体"}[Refresh]{lang="EN-US"}[消息会加重网络负载，此时]{style="font-family:宋体"}**[refresh interval]{lang="EN-US"}**[命令配置的刷新时间间隔不宜过小；对于时延敏感的应用，当]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息丢失时，希望能够尽快通过]{style="font-family:宋体"}[Refresh]{lang="EN-US"}[消息恢复丢失的消息，此时]{style="font-family:宋体"}**[refresh interval]{lang="EN-US"}**[命令配置的刷新时间间隔不宜过大。简单地调整刷新时间间隔无法同时解决这两类问题。]{style="font-family:宋体"}

[[摘要刷新和]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_16315_x4274_52996086}[消息的可靠传递功能可以很好地解决上述问题。]{style="font-family:宋体"}

[[摘要刷新功能的工作机制为：发送]{style="font-family:宋体"}[Path]{lang="EN-US"}]{#struct_0_16315_x4274_57844634}[和]{style="font-family:宋体"}[Resv]{lang="EN-US"}[消息时，在消息中携带]{style="font-family:宋体"}[Message ID]{lang="EN-US"}[，用来唯一标识一个消息；]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[通过发送携带待刷新消息的]{style="font-family:宋体"}[Message ID]{lang="EN-US"}[的]{style="font-family:宋体"}[Srefresh]{lang="EN-US"}[消息，来刷新对应的]{style="font-family:宋体"}[Path]{lang="EN-US"}[和]{style="font-family:宋体"}[Resv]{lang="EN-US"}[消息。采用摘要刷新功能后，不必传送标准的]{style="font-family:宋体"}[Path]{lang="EN-US"}[和]{style="font-family:宋体"}[Resv]{lang="EN-US"}[消息，只需传递携带]{style="font-family:宋体"}[Path]{lang="EN-US"}[和]{style="font-family:宋体"}[Resv]{lang="EN-US"}[消息摘要的]{style="font-family:宋体"}[Srefresh]{lang="EN-US"}[消息，即可实现对]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[路径和预留状态进行刷新，减少了网络上的]{style="font-family:宋体"}[Refresh]{lang="EN-US"}[消息流量，并加快了节点对刷新消息的处理速度。]{style="font-family:宋体"}

[]{#struct_0_16315_x4274_157938330}[]{#_Toc312767156}[RSVP]{lang="EN-US"}[消息的可靠传递功能是指对端设备需要应答本端发送的]{style="font-family:
宋体"}[RSVP]{lang="EN-US"}[消息，否则将会重传此消息。其工作机制为：节点发送了携带]{style="font-family:宋体"}[Message_ID]{lang="EN-US"}[对象的消息，且]{style="font-family:宋体"}[Message_ID]{lang="EN-US"}[对象的]{style="font-family:宋体"}[ACK_Desired]{lang="EN-US"}[标识（是否需要应答标识）置位后，如果在重传时间]{style="font-family:宋体"}[Rf]{lang="EN-US"}[内没有收到携带对应]{style="font-family:宋体"}[Message_ID_ACK]{lang="EN-US"}[对象的消息，则重传时间]{style="font-family:宋体"}[Rf]{lang="EN-US"}[超时后重传此消息，并将重传时间置为（]{style="font-family:宋体"}[1]{lang="EN-US"}[＋]{style="font-family:宋体"}[Delta]{lang="EN-US"}[）×]{style="font-family:宋体"}[Rf]{lang="EN-US"}[。节点持续按照上述方法重传此消息，直到节点在重传时间超时前接收到对应的应答消息，或消息传送次数达到]{style="font-family:宋体"}[3]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[其中，重传时间]{style="font-family:宋体"}[Rf]{lang="EN-US"}]{#struct_0_16315_x4274_x1941132860}[的初始值为]{style="font-family:宋体"}**[rsvp reduction retransmit]{lang="EN-US"}**[ **interval**]{lang="EN-US"}[命令配置的值；]{style="font-family:宋体"}[Delta]{lang="EN-US"}[的值为]{style="font-family:宋体"}**[rsvp reduction retransmit]{lang="EN-US"}**[ **increment**]{lang="EN-US"}[命令配置的值。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_16315_x4274_693888666}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[开启摘要刷新功能后，将不会周期性发送]{style="font-family:宋体"}]{#struct_0_16315_x4274_x126087322}[Refresh]{lang="EN-US"}[消息维护路径和预留状态。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Srefresh]{lang="EN-US"}]{#struct_0_16315_x4274_x1980403648}[消息的发送周期由]{lang="EN-US" style="font-family:宋体"}**[refresh interval]{lang="EN-US"}**[命令决定。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16315_x4274_1135837208}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_16315_x4274_x1925925310}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_x1023076928}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上开启摘要刷新功能和]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息的可靠传递功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16315_x4274_x2091370476}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] rsvp reduction srefresh reliability]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_16315_x4274_412784735}

[[\# ]{lang="EN-US"}]{#struct_0_16315_x4274_x616912681}[在接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上开启摘要刷新功能和]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息的可靠传递功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16315_x4274_1115875795}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] rsvp reduction srefresh []{#_Toc312767167}reliability]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16315_x4274_x1980469184}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[refresh interval]{lang="EN-US"}**]{#struct_0_16315_x4274_772305907}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp reduction retransmit increment]{lang="EN-US"}**]{#struct_0_16315_x4274_x1637796913}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsvp reduction retransmit interval]{lang="EN-US"}**]{#struct_0_16315_x4274_944052117}

[ ]{lang="EN-US"}
:::
