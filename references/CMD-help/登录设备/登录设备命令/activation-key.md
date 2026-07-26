::: {#707542718 .myid}
[]{#_Toc100291504}[]{#_Toc15375227}[]{#_Toc404782450}[]{#struct_0_18173_18228_x1333436234}[]{#_Toc263186389}[]{#_Toc139341865}[]{#_Toc121584942}[]{#_Toc385435348}

**登录设备 \-- 登录设备命令 \-- activation-key**

------------------------------------------------------------------------

[**[activation-key]{lang="EN-US"}**]{#struct_0_18173_18228_x214649172}[命令用来配置启动终端会话的快捷键。]{style="font-family:宋体"}

[**[undo activation-key]{lang="EN-US"}**]{#struct_0_18173_18228_1108804381}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_633206102}

[**[activation-key]{lang="EN-US"}**[ *key-string*]{lang="EN-US"}]{#struct_0_18173_18228_x87649007}

[**[undo activation-key]{lang="EN-US"}**]{#struct_0_18173_18228_1232929412}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_1763066930}

[[按]{style="font-family:宋体"}[\<Enter\>]{lang="EN-US"}]{#struct_0_18173_18228_x1377497232}[键启动终端会话。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_778166039}

[[用户线视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18173_18228_182344894}[用户线类视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_1497159728}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1950073063}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_736773433}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_x87649008}

[*[key-string]{lang="EN-US"}*]{#struct_0_18173_18228_1232929415}[：定义启动终端会话的快捷键，可以是区分大小写的单个字符，也可以是单个字符或组合键对应的]{style="font-family:宋体"}[ACSII]{lang="EN-US"}[码（]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[）。比如设置]{style="font-family:宋体"}[activation-key 65]{lang="EN-US"}[，此时生效快捷键为]{style="font-family:宋体"}[A]{lang="EN-US"}[；如果设置]{style="font-family:宋体"}[activation-key a]{lang="EN-US"}[，生效的快捷键为]{style="font-family:宋体"}[a]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_1763394610}

[[如果使用]{style="font-family:宋体"}**[activation-key]{lang="EN-US"}**]{#struct_0_18173_18228_1740252761}[命令设置了别的快捷键，则新的快捷键将代替]{style="font-family:宋体"}[\<Enter\>]{lang="EN-US"}[键来启动终端会话，新设置的快捷键可以使用]{style="font-family:宋体"}**[display current-configuration \| include activation-key]{lang="EN-US"}**[命令查看。]{style="font-family:宋体"}

[[如果用户线视图下配置]{style="font-family:宋体"}**[activation-key]{lang="EN-US"}**]{#struct_0_18173_18228_x1732224285}[为缺省值，并且此时用户线类视图下配置了]{style="font-family:宋体"}**[activation-key]{lang="EN-US"}**[，那么用户线视图下的生效配置值为用户线类视图下的配置；如果用户线类视图下未配置，则生效的为缺省值。]{style="font-family:宋体"}

[[VTY]{lang="EN-US"}]{#struct_0_18173_18228_1753122001}[用户线视图]{style="font-family:宋体"}[/VTY]{lang="EN-US"}[用户线类视图不支持该命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x559400005}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_1883828872}[指定启动]{style="font-family:宋体"}[Console]{lang="EN-US"}[口终端会话的快捷键为]{style="font-family:宋体"}[\<s\>]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_x87649009}

[\[Sysname\] line console 0]{lang="EN-US"}

[\[Sysname-line-console0\] activation-key s]{lang="EN-US"}

[[验证过程如下：]{style="font-family:宋体"}]{#struct_0_18173_18228_1232929414}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[退出]{lang="EN-US" style="font-family:宋体"}[Console]{lang="EN-US"}]{#struct_0_18173_18228_1763460146}[口终端会话。]{lang="EN-US" style="font-family:宋体"}

[[\[Sysname-line-console0\] return]{lang="EN-US"}]{#struct_0_18173_18228_958026563}

[\<Sysname\> quit]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重新使用]{style="font-family:宋体"}]{#struct_0_18173_18228_1135860801}[Console]{lang="EN-US"}[口登录设备，能看到如下显示信息。]{style="font-family:宋体"}

[[Press ENTER to get started.]{lang="EN-US"}]{#struct_0_18173_18228_52368403}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[此时，]{style="font-family:宋体"}]{#struct_0_18173_18228_x701496110}[\<Enter\>]{lang="EN-US"}[键失效，需要按]{style="font-family:宋体"}[\<s\>]{lang="EN-US"}[键才能出现用户视图提示符，启动]{style="font-family:宋体"}[Console]{lang="EN-US"}[口终端会话。]{style="font-family:宋体"}

[[\<Sysname\>]{lang="EN-US"}]{#struct_0_18173_18228_x87649010}
:::

::: {#-947553691 .myid}
[]{#_Toc404782451}[]{#struct_0_18173_18228_x723385729}[]{#_Toc263186391}[]{#_Toc139341867}

**登录设备 \-- 登录设备命令 \-- authentication-mode**

------------------------------------------------------------------------

[**[authentication-mode]{lang="EN-US"}**]{#struct_0_18173_18228_x1950178493}[命令用来设置用户使用当前用户线登录设备时的认证方式。]{style="font-family:宋体"}

[**[undo authentication-mode]{lang="EN-US"}**]{#struct_0_18173_18228_1934705973}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_1347145146}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_18173_18228_x1802115606}[模式下：]{style="font-family:宋体"}

[**[authentication-mode]{lang="EN-US"}**[ { **none** \| **password** \| **scheme** }]{lang="EN-US"}]{#struct_0_18173_18228_494617132}

[**[undo authentication-mode]{lang="EN-US"}**]{#struct_0_18173_18228_1130472207}

[[FIPS]{lang="EN-US"}]{#struct_0_18173_18228_1035730381}[模式下：]{style="font-family:宋体"}

[**[authentication-mode]{lang="EN-US"}**[ **scheme**]{lang="EN-US"}]{#struct_0_18173_18228_x87649011}

[**[undo authentication-mode]{lang="EN-US"}**]{#struct_0_18173_18228_x723385730}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1949719742}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_18173_18228_x2056134479}[模式下：使用]{style="font-family:宋体"}[VTY]{lang="EN-US"}[、]{style="font-family:宋体"}[AUX]{lang="EN-US"}[用户线登录的用户的认证方式为]{style="font-family:宋体"}[password]{lang="EN-US"}[，使用]{style="font-family:宋体"}[Console]{lang="EN-US"}[、]{style="font-family:宋体"}[TTY]{lang="EN-US"}[用户线登录的用户不需要认证。如果设备上只有一个]{style="font-family:宋体"}[AUX]{lang="EN-US"}[口，而没有]{style="font-family:宋体"}[Console]{lang="EN-US"}[口（]{style="font-family:宋体"}[Console]{lang="EN-US"}[口与]{style="font-family:宋体"}[AUX]{lang="EN-US"}[口共用），则使用]{style="font-family:宋体"}[AUX]{lang="EN-US"}[用户线登录的用户不需要认证。]{style="font-family:宋体"}

[[FIPS]{lang="EN-US"}]{#struct_0_18173_18228_x1203019146}[模式下：使用当前用户线登录设备时的认证方式为]{style="font-family:宋体"}[scheme]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_1731827526}

[[用户线视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18173_18228_x2082032061}[用户线类视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_381432145}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x175863900}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_x87649012}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_x723385727}

[**[none]{lang="EN-US"}**]{#struct_0_18173_18228_x1949785277}[：指定不进行认证。]{style="font-family:宋体"}

[**[password]{lang="EN-US"}**]{#struct_0_18173_18228_x1747345574}[：指定进行密码认证方式。]{style="font-family:宋体"}

[**[scheme]{lang="EN-US"}**]{#struct_0_18173_18228_x917340184}[：指定进行]{style="font-family:宋体"}[AAA]{lang="EN-US"}[认证方式。]{style="font-family:宋体"}[AAA]{lang="EN-US"}[的相关内容请参见"安全配置指导"中的"]{style="font-family:宋体"}[]{#_Toc138065690}[]{#_Ref138064787}[]{#_Ref138064785}[]{#_Ref107300551}[]{#_Ref107300544}[]{#_Toc69803983}[]{#_Ref65657240}[]{#_Ref65657237}[]{#_Ref17794740}[]{#_Ref17794737}[]{#_Ref13651826}[]{#_Ref13651824}[[AAA]{lang="EN-US"}]{#_Toc13649100}["。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_286052932}

[[当认证方式设置为]{style="font-family:宋体"}[none]{lang="EN-US"}]{#struct_0_18173_18228_x864151761}[时，用户不需要输入用户名和密码，就可以使用该用户线登录设备，存在安全隐患，请谨慎配置。]{style="font-family:宋体"}

[[用户线视图下，对]{style="font-family:宋体"}**[authentication-mode]{lang="EN-US"}**]{#struct_0_18173_18228_791254358}[和]{style="font-family:宋体"}**[protocol inbound]{lang="EN-US"}**[进行关联绑定。]{style="font-family:宋体"}

[[当这两条命令均配置为缺省值，此时该用户线视图下的这两条命令配置值均取该类用户线类视图下的相应的配置；若该类用户线类视图下没有进行相应的配置，则均取缺省值。]{style="font-family:宋体"}]{#struct_0_18173_18228_x2043964139}

[[当两条命令中的任意一条配置了非缺省值，那么另外一条取缺省值。当两条命令都配置成非缺省值，则均取用户线下的配置值。]{style="font-family:宋体"}]{#struct_0_18173_18228_1264705126}

[[需要注意的是，在用户线视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18173_18228_1134677697}[用户线类视图下，该命令的配置结果将在下次登录设备时生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_2098961012}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_1972426311}[设置用户使用]{style="font-family:宋体"}[VTY 0]{lang="EN-US"}[用户线登录设备时，不需要认证。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_x1911164892}

[\[Sysname\] line vty 0]{lang="EN-US"}

[\[Sysname-line-vty0\] authentication-mode none]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x1843557609}[设置用户使用]{style="font-family:宋体"}[VTY 0]{lang="EN-US"}[用户线登录设备时，需要密码认证，认证密码为]{style="font-family:宋体"}[321]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_x2043964140}

[\[Sysname\] line vty 0]{lang="EN-US"}

[\[Sysname-line-vty0\] authentication-mode password]{lang="EN-US"}

[\[Sysname-line-vty0\] set authentication password simple 321]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x657281495}[设置用户使用]{style="font-family:宋体"}[VTY 0]{lang="EN-US"}[用户线，采用]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[方式登录设备时采用本地]{style="font-family:宋体"}[AAA]{lang="EN-US"}[认证，用户名为]{style="font-family:宋体"}[123]{lang="EN-US"}[，认证密码为]{style="font-family:宋体"}[321]{lang="EN-US"}[，用户角色为]{style="font-family:宋体"}[network-admin]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_2130476356}

[\[Sysname\] line vty 0]{lang="EN-US"}

[\[Sysname-line-vty0\] authentication-mode scheme]{lang="EN-US"}

[\[Sysname-line-vty0\] quit]{lang="EN-US"}

[\[Sysname\] local-user 123]{lang="EN-US"}

[\[Sysname-luser-manage-123\] password simple 321]{lang="EN-US"}

[\[Sysname-luser-manage-123\] service-type telnet]{lang="EN-US"}

[\[Sysname-luser-manage-123\] authorization-attribute user-role network-admin]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_1048846309}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[set authentication password]{lang="EN-US"}**]{#struct_0_18173_18228_x1248950484}
:::

::: {#-2053474462 .myid}
[]{#_Toc263186394}[]{#_Toc139341868}[]{#_Toc100291505}[]{#_Toc15375229}[]{#_Toc404782452}[]{#struct_0_18173_18228_310438444}[]{#_Toc297210643}[]{#_Toc296689413}[]{#_Toc139341866}[]{#_Toc301508026}

**登录设备 \-- 登录设备命令 \-- auto-execute command**

------------------------------------------------------------------------

[**[auto-execute command]{lang="EN-US"}**]{#struct_0_18173_18228_x1444811409}[命令用来设置自动执行命令。]{style="font-family:宋体"}

[**[undo auto-execute command]{lang="EN-US"}**]{#struct_0_18173_18228_x2043964141}[命令用来取消自动执行命令。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_908802446}

[**[auto-execute command ]{lang="EN-US"}***[command]{lang="EN-US"}*]{#struct_0_18173_18228_668690284}

[**[undo auto-execute command]{lang="EN-US"}**]{#struct_0_18173_18228_x311398047}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_1524201240}

[[未设定自动执行命令。]{style="font-family:宋体"}]{#struct_0_18173_18228_1559079104}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_1474581837}

[[用户线视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18173_18228_174309320}[用户线类视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_x2043964142}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1820080909}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_1287195827}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_1428143704}

[*[command]{lang="EN-US"}*]{#struct_0_18173_18228_1085444498}[：需要自动执行的某条命令。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_2115520865}

[[用户在登录时设备会自动执行]{style="font-family:宋体"}**[auto-execute command]{lang="EN-US"}**]{#struct_0_18173_18228_343079113}[配置好的命令，执行完命令后，自动断开用户连接。]{style="font-family:宋体"}

[[该命令通常的用法是：配置]{style="font-family:宋体"}**[auto-execute command telnet X.X.X.X]{lang="EN-US"}**]{#struct_0_18173_18228_x217802720}[，使用户通过该用户线登录设备时能自动连接到指定的主机。用户断开与指定主机的连接后，用户与该设备的连接才会自动断开。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_18173_18228_1849616877}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Console]{lang="EN-US"}]{#struct_0_18173_18228_x2043964143}[用户线视图]{style="font-family:宋体"}[/Console]{lang="EN-US"}[用户线类视图不支持该命令。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果设备上只有一个]{style="font-family:宋体"}]{#struct_0_18173_18228_x253996968}[AUX]{lang="EN-US"}[口，没有]{style="font-family:宋体"}[Console]{lang="EN-US"}[口（]{style="font-family:宋体"}[Console]{lang="EN-US"}[口和]{style="font-family:宋体"}[AUX]{lang="EN-US"}[口共用），则]{style="font-family:宋体"}[AUX]{lang="EN-US"}[用户线视图]{style="font-family:宋体"}[/AUX]{lang="EN-US"}[用户线类视图不支持该命令。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置]{lang="EN-US" style="font-family:宋体"}**[auto-execute command]{lang="EN-US"}**]{#struct_0_18173_18228_x1977338042}[命令之前，请确保可以通过其它用户线（比如]{lang="EN-US" style="font-family:宋体"}[Console]{lang="EN-US"}[用户线）登录系统，以便出现问题后，能删除该配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}**[auto-execute command]{lang="EN-US"}**]{#struct_0_18173_18228_x694860519}[命令后，可能导致用户不能通过该终端线对本系统进行配置，需谨慎使用。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18173_18228_x2054150487}[用户线视图下配置]{style="font-family:宋体"}**[ a]{lang="EN-US"}[uto-execute command]{lang="EN-US"}**[为]{style="font-family:宋体"}[缺省值，]{lang="EN-US" style="font-family:宋体"}[并且此时用户线类视图下配置了]{style="font-family:宋体"}**[auto-execute command]{lang="EN-US"}**[，那么用户线视图下的生效配置值为用户线类视图下的配置]{style="font-family:宋体"}[；如果用户线类视图下未配置，则生效的为缺省值]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[需要注意的是，在用户线视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18173_18228_1135005377}[用户线类视图下，使用该命令设置的自动执行命令将在下次登录设备时生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x708585868}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x1771358129}[配置用户从]{style="font-family:宋体"}[VTY0]{lang="EN-US"}[登录本设备（]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.1.40]{lang="EN-US"}[）后，自动]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[到]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.1.41]{lang="EN-US"}[的设备。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_x2043964144}

[\[Sysname\] line vty 0]{lang="EN-US"}

[\[Sysname-line-vty0\] auto-execute command telnet 192.168.1.41]{lang="EN-US"}

[This action will lead to configuration failure through line-vty0. Are you sure?]{lang="EN-US"}

[\[Y/N\]:y]{lang="EN-US"}

[\[Sysname-line-vty0\]]{lang="EN-US"}

[[结果验证：]{style="font-family:宋体"}]{#struct_0_18173_18228_1312086973}

[[重新]{style="font-family:宋体"}[Telnet]{lang="EN-US"}]{#struct_0_18173_18228_x1666191776}[登录到本设备，设备会自动执行]{style="font-family:宋体"}[telnet 192.168.1.41]{lang="EN-US"}[命令，在]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[客户端会看到以下显示信息。]{style="font-family:宋体"}

[[C:\\\> telnet 192.168.1.40]{lang="EN-US"}]{#struct_0_18173_18228_x2043964145}

[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*]{lang="EN-US"}

[\* Copyright (c) 2004-2010 Hangzhou H3C Tech. Co., Ltd. All rights reserved.  \*]{lang="EN-US"}

[\* Without the owner\'s prior written consent,                                 \*]{lang="EN-US"}

[\* no decompiling or reverse-engineering shall be allowed.                    \*]{lang="EN-US"}

[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*]{lang="EN-US"}

[ ]{lang="EN-US"}

[\<Sysname\>]{lang="EN-US"}

[Trying 192.168.1.41 \...]{lang="EN-US"}

[Press CTRL+K to abort]{lang="EN-US"}

[Connected to 192.168.1.41 \...]{lang="EN-US"}

[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*]{lang="EN-US"}

[\* Copyright (c) 2004-2014 Hangzhou H3C Tech. Co., Ltd. All rights reserved.  \*]{lang="EN-US"}

[\* Without the owner\'s prior written consent,                                 \*]{lang="EN-US"}

[\* no decompiling or reverse-engineering shall be allowed.                    \*]{lang="EN-US"}

[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*]{lang="EN-US"}

[\<Sysname.41\>]{lang="EN-US"}

[[此时相当于用户直接登录了]{style="font-family:宋体"}[192.168.1.41]{lang="EN-US"}]{#struct_0_18173_18228_x1416796382}[设备。如果用户断开与]{style="font-family:宋体"}[192.168.1.41]{lang="EN-US"}[的]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[连接，用户与]{style="font-family:宋体"}[192.168.1.40]{lang="EN-US"}[设备的]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[连接也会同时自动断开。]{style="font-family:宋体"}
:::

::: {#1330474620 .myid}
[]{#_Toc404782453}[]{#struct_0_18173_18228_1812115003}[]{#_Toc309144859}[]{#_Toc301187182}[]{#_Toc263186392}[]{#_Toc223507082}

**登录设备 \-- 登录设备命令 \-- command accounting**

------------------------------------------------------------------------

[**[command accounting]{lang="EN-US"}**]{#struct_0_18173_18228_1125016279}[命令用来使能命令行计费功能。]{style="font-family:宋体"}

[**[undo command accounting]{lang="EN-US"}**]{#struct_0_18173_18228_x505394513}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_1008976779}

[**[command accounting]{lang="EN-US"}**]{#struct_0_18173_18228_x1098970116}

[**[undo command accounting]{lang="EN-US"}**]{#struct_0_18173_18228_319789417}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_359670056}

[[没有使能命令行计费功能，即计费服务器不会记录用户执行的命令行。]{style="font-family:宋体"}]{#struct_0_18173_18228_x2043964146}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_149287559}

[[用户线视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18173_18228_174110077}[用户线类视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_606749627}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1012272788}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_1527592899}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1360651143}

[[使能命令行计费功能后，如果没有配置命令行授权功能，则当前用户执行的每一条合法命令都会发送到]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}]{#struct_0_18173_18228_1162053188}[服务器上做记录；如果配置了命令行授权功能，则当前用户执行的并且授权成功的命令都会发送到]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[服务器上做记录。]{style="font-family:宋体"}

[[如果在用户线类视图下使用]{style="font-family:宋体"}**[command accounting]{lang="EN-US"}**]{#struct_0_18173_18228_x2043964147}[命令使能了命令行计费功能，则该类型用户线视图都使能命令行计费功能，且用户线视图下无法使用]{style="font-family:宋体"}**[undo command accounting]{lang="EN-US"}**[恢复缺省情况。]{style="font-family:宋体"}

[[需要注意的是，在用户线视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18173_18228_1134874305}[用户线类视图下，该命令的配置结果将在下次登录设备时生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_1715371500}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_1414959276}[设置用户使用]{style="font-family:宋体"}[VTY 0]{lang="EN-US"}[用户线登录设备时，执行的命令需要在]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[服务器上做记录。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_x1739901890}

[\[Sysname\] line vty 0]{lang="EN-US"}

[\[Sysname-line-vty0\] command [accounting]{.TerminalDisplayChar}]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x2020355139}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}**[command authorization]{lang="EN-US"}**]{#struct_0_18173_18228_558742552}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}**[accounting command]{lang="EN-US"}**]{#struct_0_18173_18228_758230522}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/AAA]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#1025915770 .myid}
[]{#_Toc404782454}[]{#struct_0_18173_18228_x1374968685}[]{#_Toc309144860}[]{#_Toc301187183}[]{#_Toc263186393}[]{#_Toc223507083}

**登录设备 \-- 登录设备命令 \-- command authorization**

------------------------------------------------------------------------

[**[command authorization]{lang="EN-US"}**]{#struct_0_18173_18228_x2043964148}[命令用来使能命令行授权功能。]{style="font-family:宋体"}

[**[undo command authorization]{lang="EN-US"}**]{#struct_0_18173_18228_x301051135}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_278750490}

[**[command authorization]{lang="EN-US"}**]{#struct_0_18173_18228_176307583}

[**[undo command authorization]{lang="EN-US"}**]{#struct_0_18173_18228_x1766745387}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_484075837}

[[没有使能命令行授权功能，即用户登录后执行命令行不需要服务器授权。]{style="font-family:宋体"}]{#struct_0_18173_18228_1694553105}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_1874000440}

[[用户线视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18173_18228_1707226379}[用户线类视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_294688021}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_381695566}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1497278125}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_162422059}

[[使能命令行授权功能后，使用该用户线登录的用户只能执行服务器授权的命令，服务器没有授权的命令不能执行。]{style="font-family:宋体"}]{#struct_0_18173_18228_x1910885350}

[[如果在用户线类视图下使用]{style="font-family:宋体"}**[command authorization]{lang="EN-US"}**]{#struct_0_18173_18228_x45947621}[命令使能了命令行授权功能，则该类型用户线视图都使能命令行授权功能，且用户线视图下无法使用]{style="font-family:宋体"}**[undo command authorization]{lang="EN-US"}**[恢复缺省情况。]{style="font-family:宋体"}

[[需要注意的是，在用户线视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18173_18228_1135267521}[用户线类视图下该命令的配置结果将在下次登录设备时生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1008912666}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x916188626}[设置用户使用]{style="font-family:宋体"}[VTY 0]{lang="EN-US"}[用户线登录设备时，需要服务器授权才能执行命令。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_294688020}

[\[Sysname\] line vty 0]{lang="EN-US"}

[\[Sysname-line-vty0\] command [authorization]{.TerminalDisplayChar}]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_381695565}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}**[command accounting]{lang="EN-US"}**]{#struct_0_18173_18228_x1497278126}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}**[authorization command]{lang="EN-US"}**]{#struct_0_18173_18228_x1403661882}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/AAA]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#318849580 .myid}
[]{#_Toc404782455}[]{#struct_0_18173_18228_2005836430}

**登录设备 \-- 登录设备命令 \-- databits**

------------------------------------------------------------------------

[**[databits]{lang="EN-US"}**]{#struct_0_18173_18228_x1599733862}[命令用来设置数据位的个数。]{style="font-family:宋体"}

[**[undo databits]{lang="EN-US"}**]{#struct_0_18173_18228_x683218272}[命令用来恢复缺省的数据位。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_1891606378}

[**[databits ]{lang="EN-US"}**[{ **5** \| **6** \| **7** \| **8** }]{lang="EN-US"}]{#struct_0_18173_18228_294688019}

[**[undo databits]{lang="EN-US"}**]{#struct_0_18173_18228_x1956956586}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_1327817149}

[[用户线的数据位为]{style="font-family:宋体"}[8]{lang="EN-US"}]{#struct_0_18173_18228_x371409343}[位。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_x403248880}

[[用户线视图]{style="font-family:宋体"}]{#struct_0_18173_18228_x943614576}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_625164069}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_440993375}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_194287870}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_294688018}

[**[5]{lang="EN-US"}**]{#struct_0_18173_18228_x1956956587}[：数据位为]{style="font-family:宋体"}[5]{lang="EN-US"}[位，即使用]{style="font-family:宋体"}[5]{lang="EN-US"}[比特来表示一个字符。]{style="font-family:宋体"}

[**[6]{lang="EN-US"}**]{#struct_0_18173_18228_x238266792}[：数据位为]{style="font-family:宋体"}[6]{lang="EN-US"}[位，即使用]{style="font-family:宋体"}[6]{lang="EN-US"}[比特来表示一个字符。]{style="font-family:宋体"}

[**[7]{lang="EN-US"}**]{#struct_0_18173_18228_1759246514}[：数据位为]{style="font-family:宋体"}[7]{lang="EN-US"}[位，即使用]{style="font-family:宋体"}[7]{lang="EN-US"}[比特来表示一个字符。]{style="font-family:宋体"}

[**[8]{lang="EN-US"}**]{#struct_0_18173_18228_x563844687}[：数据位为]{style="font-family:宋体"}[8]{lang="EN-US"}[位，即使用]{style="font-family:宋体"}[8]{lang="EN-US"}[比特来表示一个字符。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_1880880187}

[[访问终端和设备相应用户线下数据位的设置必须一致，双方才能正常通信。]{style="font-family:宋体"}]{#struct_0_18173_18228_565278322}

[[VTY]{lang="EN-US"}]{#struct_0_18173_18228_798602976}[用户线类视图不支持该命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_373632433}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_294688017}[设置数据位为]{style="font-family:宋体"}[5]{lang="EN-US"}[位。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_x1956956588}

[\[Sysname\] line aux 0]{lang="EN-US"}

[\[Sysname-line-aux0\] databits 5]{lang="EN-US"}
:::

::: {#1601541110 .myid}
[]{#_Toc404782456}[]{#struct_0_18173_18228_1038566751}[]{#_Toc356977366}[]{#_Toc185927308}[]{#_Toc123026768}

**登录设备 \-- 登录设备命令 \-- display ip http**

------------------------------------------------------------------------

[**[display ip http]{lang="EN-US"}**]{#struct_0_18173_18228_1038566752}[命令用来显示]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[的状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_1893608255}

[**[display ip http]{lang="EN-US"}**]{#struct_0_18173_18228_x173362290}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_1529670493}

[[任意视图]{style="font-family:宋体"}]{#struct_0_18173_18228_104149926}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1171891005}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_1038566749}

[[network-operator]{lang="EN-US"}]{#struct_0_18173_18228_1893935934}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_590984534}

[[mdc-operator]{lang="EN-US"}]{#struct_0_18173_18228_723343489}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_1828595772}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x1607150233}[显示]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[的状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display ip http]{lang="EN-US"}]{#struct_0_18173_18228_1038566750}

[HTTP port: 80]{lang="EN-US"}

[Basic ACL: 2222]{lang="EN-US"}

[HTTP status: Enabled]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display ip http]{lang="EN-US"}]{#struct_0_18173_18228_1893477183}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1698559360}[[字段]{style="font-family:黑体"}]{#struct_0_18173_18228_950652108}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_18173_18228_x1802258943}

[[HTTP port]{lang="EN-US"}]{#struct_0_18173_18228_1038566763}

[[HTTP]{lang="EN-US"}]{#struct_0_18173_18228_1893542716}[服务使用的端口号]{style="font-family:宋体"}

[[Basic ACL]{lang="EN-US"}]{#struct_0_18173_18228_1733914325}

[[与]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_18173_18228_1038566764}[服务关联的基本访问控制列表号，]{style="font-family:宋体"}[Not configured]{lang="EN-US"}[表示没有配置]{style="font-family:宋体"}

[[HTTP status]{lang="EN-US"}]{#struct_0_18173_18228_1893215036}

[[HTTP]{lang="EN-US"}]{#struct_0_18173_18228_167950013}[服务是否开启：]{style="font-family:宋体"}

[[Enabled]{lang="EN-US"}]{#struct_0_18173_18228_x673041308}[：表示]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[服务处于开启状态]{style="font-family:宋体"}

[[Disabled]{lang="EN-US"}]{#struct_0_18173_18228_x917748381}[：表示]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[服务处于关闭状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_260274080}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip http ]{lang="EN-US"}**]{#struct_0_18173_18228_2065241929}**[port]{lang="FR"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip http acl]{lang="EN-US"}**]{#struct_0_18173_18228_x1220166750}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip http enable]{lang="EN-US"}**]{#struct_0_18173_18228_x317023124}

::: {#766940150 .myid}
[]{#_Toc404782457}[]{#struct_0_18173_18228_x917748380}[]{#_Toc356977368}

**登录设备 \-- 登录设备命令 \-- display ip https**

------------------------------------------------------------------------

[**[display ip https]{lang="EN-US"}**]{#struct_0_18173_18228_260208544}[命令用来显示]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[的状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x731488661}

[**[display ip https]{lang="EN-US"}**]{#struct_0_18173_18228_613451632}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_1590168985}

[[任意视图]{style="font-family:宋体"}]{#struct_0_18173_18228_x1011633235}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_x917748383}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_260143008}

[[network-operator]{lang="EN-US"}]{#struct_0_18173_18228_x186312732}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_623991638}

[[mdc-operator]{lang="EN-US"}]{#struct_0_18173_18228_x601223425}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_615742498}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x917748382}[显示]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[的状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display ip https]{lang="EN-US"}]{#struct_0_18173_18228_260077472}

[HTTPS port: 443]{lang="EN-US"}

[SSL server policy: test]{lang="EN-US"}

[Certificate access control policy: Not configured]{lang="EN-US"}

[Basic ACL: 2222]{lang="EN-US"}

[HTTPS status: Enabled]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display ip https]{lang="EN-US"}]{#struct_0_18173_18228_x1739396681}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1700044280}[[字段]{style="font-family:黑体"}]{#struct_0_18173_18228_x1009959423}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_18173_18228_x917748385}

[[HTTPS port]{lang="EN-US"}]{#struct_0_18173_18228_260011936}

[[HTTPS]{lang="EN-US"}]{#struct_0_18173_18228_x228183948}[服务使用的端口号]{style="font-family:宋体"}

[[SSL server policy]{lang="EN-US"}]{#struct_0_18173_18228_x416129374}

[[与]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}]{#struct_0_18173_18228_x917748384}[服务关联的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略，]{style="font-family:宋体"}[Not configured]{lang="EN-US"}[表示没有配置]{style="font-family:宋体"}

[[Certificate access-control-policy]{lang="EN-US"}]{#struct_0_18173_18228_259946400}

[[与]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}]{#struct_0_18173_18228_x1251598565}[服务关联的证书属性访问控制策略]{style="font-family:宋体"}[,Not configured]{lang="EN-US"}[表示没有配置]{style="font-family:宋体"}

[[Basic ACL]{lang="EN-US"}]{#struct_0_18173_18228_x917748387}

[[与]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}]{#struct_0_18173_18228_259880864}[服务关联的基本访问控制列表号，]{style="font-family:宋体"}[Not configured]{lang="EN-US"}[表示没有配置]{style="font-family:宋体"}

[[HTTPS status]{lang="EN-US"}]{#struct_0_18173_18228_x1582455321}

[[HTTPS]{lang="EN-US"}]{#struct_0_18173_18228_x1531556301}[服务是否开启：]{style="font-family:宋体"}

[[Enabled]{lang="EN-US"}]{#struct_0_18173_18228_x917748386}[[：表示]{style="font-family:宋体"}]{.TableTextChar}[HTTPS]{lang="EN-US"}[[服务处于开启状态]{style="font-family:宋体"}]{.TableTextChar}

[[Disabled]{lang="EN-US"}]{#struct_0_18173_18228_259815328}[[：表示]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}]{.TableTextChar}[[服务处于关闭状态]{style="font-family:宋体"}]{.TableTextChar}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x51778047}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip http]{lang="EN-US"}**]{#struct_0_18173_18228_1065472704}**[s]{lang="EN-US"}[ ]{lang="EN-US"}[port]{lang="FR"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip https acl]{lang="EN-US"}**]{#struct_0_18173_18228_x917748373}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip https enable]{lang="EN-US"}**]{#struct_0_18173_18228_260142999}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip https ssl-server-policy]{lang="EN-US"}**]{#struct_0_18173_18228_x971361962}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip https certificate access-control-policy]{lang="EN-US"}**]{#struct_0_18173_18228_x1324905079}

::: {#-508460551 .myid}
[]{#_Toc100291508}[]{#_Toc263186397}[]{#_Toc139341870}[]{#_Toc98416308}[]{#_Toc93828722}[]{#_Toc404782458}[]{#struct_0_18173_18228_1318595452}[]{#_Toc135191669}[]{#_Toc135479340}[]{#_Toc135191670}[]{#_Toc135479341}[]{#_Toc135191671}[]{#_Toc135479342}[]{#_Toc135191672}[]{#_Toc135479343}[]{#_Toc135191673}[]{#_Toc135479344}[]{#_Toc135191674}[]{#_Toc135479345}[]{#_Toc135191675}[]{#_Toc135479346}[]{#_Toc135191676}[]{#_Toc135479347}[]{#_Toc135191677}[]{#_Toc135479348}[]{#_Toc135191678}[]{#_Toc135479349}[]{#_Toc135191679}[]{#_Toc135479350}[]{#_Toc135191680}[]{#_Toc135479351}[]{#_Toc135191681}[]{#_Toc135479352}[]{#_Toc135191682}[]{#_Toc135479353}

**登录设备 \-- 登录设备命令 \-- display line**

------------------------------------------------------------------------

[**[display line]{lang="EN-US"}**]{#struct_0_18173_18228_617767504}[命令用来显示用户线的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_876180521}

[**[display line]{lang="EN-US"}**[ \[ *number1* \| { **aux** \| **console** \| **tty** \| **vty** } *number2* \] \[ **summary** \]]{lang="EN-US"}]{#struct_0_18173_18228_x107694750}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_294688014}

[[任意视图]{style="font-family:宋体"}]{#struct_0_18173_18228_x1956956591}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1401131742}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x2115714190}

[[network-operator]{lang="EN-US"}]{#struct_0_18173_18228_x905656875}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_688380635}

[[mdc-operator]{lang="EN-US"}]{#struct_0_18173_18228_2000962600}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_1426730218}

[*[number1]{lang="EN-US"}*]{#struct_0_18173_18228_294688013}[：用户线的编号（绝对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准，一般从]{style="font-family:宋体"}[0]{lang="EN-US"}[开始。]{style="font-family:宋体"}

[**[aux]{lang="EN-US"}**]{#struct_0_18173_18228_x1956956592}[：]{style="font-family:宋体"}[AUX]{lang="EN-US"}[用户线。]{style="font-family:宋体"}

[**[console]{lang="EN-US"}**]{#struct_0_18173_18228_x997847215}[：]{style="font-family:宋体"}[Console]{lang="EN-US"}[用户线。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[tty]{lang="EN-US"}**]{#struct_0_18173_18228_x1064395965}[：]{style="font-family:宋体"}[TTY]{lang="EN-US"}[用户线。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vty]{lang="EN-US"}**]{#struct_0_18173_18228_x1058129215}[：]{style="font-family:宋体"}[VTY]{lang="EN-US"}[用户线。]{style="font-family:宋体"}

[*[number2]{lang="EN-US"}*]{#struct_0_18173_18228_533177837}[：用户线的编号（相对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[summary]{lang="EN-US"}**]{#struct_0_18173_18228_x693393003}[：显示用户线的摘要信息。不使用该参数时，将显示用户线类型、绝对]{style="font-family:宋体"}[/]{lang="EN-US"}[相对编号、传输速率、]{style="font-family:宋体"}[Modem]{lang="EN-US"}[属性、认证方式及接入接口；使用该参数时，将显示正在使用和未使用的用户线数目和类型。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_27314194}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_294688012}[显示用户线]{style="font-family:宋体"}[0]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display line 0]{lang="EN-US"}]{#struct_0_18173_18228_x1956956593}

[  Idx  Type     Tx/Rx      Modem Auth  Int         Location]{lang="EN-US"}

[  0    CON 0    9600       -     N     -           0/0]{lang="EN-US"}

[ ]{lang="EN-US"}

[  +    : Line is active.]{lang="EN-US"}

[  F    : Line is active and in async mode.]{lang="EN-US"}

[  Idx  : Absolute index of line.]{lang="EN-US"}

[  Type : Type and relative index of line.]{lang="EN-US"}

[  Auth : Login authentication mode.]{lang="EN-US"}

[  Int  : Physical port of the line.]{lang="EN-US"}

[  A    : Authentication use AAA.]{lang="EN-US"}

[  N    : No authentication is required.]{lang="EN-US"}

[  P    : Password authentication.]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display line]{lang="EN-US"}]{#struct_0_18173_18228_1731036140}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1842387635}[[字段]{style="font-family:黑体"}]{#struct_0_18173_18228_1405037544}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_18173_18228_x1495236161}

[[+]{lang="EN-US"}]{#struct_0_18173_18228_x1661627115}

[[表示当前正在使用的用户线]{style="font-family:宋体"}]{#struct_0_18173_18228_87421171}

[[F]{lang="EN-US"}]{#struct_0_18173_18228_314961370}

[[表示当前正在使用的用户线，且工作在异步方式]{style="font-family:宋体"}]{#struct_0_18173_18228_x294664453}

[[Idx]{lang="EN-US"}]{#struct_0_18173_18228_x1798637354}

[[用户线的绝对编号]{style="font-family:宋体"}]{#struct_0_18173_18228_1700147236}

[[Type]{lang="EN-US"}]{#struct_0_18173_18228_x1661627116}

[[用户线的类型及相对编号]{style="font-family:宋体"}]{#struct_0_18173_18228_490705698}

[[Tx/Rx]{lang="EN-US"}]{#struct_0_18173_18228_1673394213}

[[用户线的速率]{style="font-family:宋体"}]{#struct_0_18173_18228_x1833891948}

[[Modem]{lang="EN-US"}]{#struct_0_18173_18228_1244357406}

[[Modem]{lang="EN-US"}]{#struct_0_18173_18228_x723190542}[的呼入]{style="font-family:宋体"}[/]{lang="EN-US"}[呼出开关，取值有]{style="font-family:宋体"}[in]{lang="EN-US"}[（允许呼入）、]{style="font-family:宋体"}[out]{lang="EN-US"}[（允许呼出）、]{style="font-family:宋体"}[inout]{lang="EN-US"}[（允许呼入呼出），缺省显示"]{style="font-family:宋体"}[-]{lang="EN-US"}["（表示没有配置）]{style="font-family:宋体"}

[[Auth]{lang="EN-US"}]{#struct_0_18173_18228_x1661627117}

[[使用该用户线登录的用户的认证方式，取值有]{style="font-family:宋体"}[A]{lang="EN-US"}]{#struct_0_18173_18228_x1075378243}[、]{style="font-family:宋体"}[L]{lang="EN-US"}[、]{style="font-family:宋体"}[N]{lang="EN-US"}[和]{style="font-family:宋体"}[P]{lang="EN-US"}[四种方式]{style="font-family:宋体"}

[[Int]{lang="EN-US"}]{#struct_0_18173_18228_x1316829607}

[[用户线对应的物理接口的简称表示（没有对应接口的用户线均显示"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_18173_18228_x422173713}["，但]{style="font-family:宋体"}[console]{lang="EN-US"}[口除外，即使]{style="font-family:宋体"}[console]{lang="EN-US"}[口有对应的物理接口，此处仍显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["）]{style="font-family:宋体"}

[[Location]{lang="EN-US"}]{#struct_0_18173_18228_x396390156}

[[用户线的物理位置：]{style="font-family:宋体"}]{#struct_0_18173_18228_1785275849}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式设备：显示为"槽位号]{style="font-family:宋体"}]{#struct_0_18173_18228_x396455692}[/CPU]{lang="EN-US"}[编号"]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备---独立运行模式：显示为"槽位号]{style="font-family:宋体"}]{#struct_0_18173_18228_214467581}[/CPU]{lang="EN-US"}[编号"]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备---]{style="font-family:宋体"}]{#struct_0_18173_18228_x1920017977}[IRF]{lang="EN-US"}[模式：显示为"设备成员编号]{style="font-family:宋体"}[/]{lang="EN-US"}[槽位号]{style="font-family:宋体"}[/CPU]{lang="EN-US"}[编号"]{style="font-family:宋体"}

[[A]{lang="EN-US"}]{#struct_0_18173_18228_709779111}

[[表示使用]{style="font-family:宋体"}[AAA]{lang="EN-US"}]{#struct_0_18173_18228_x1661627118}[认证方式，对应的]{style="font-family:宋体"}**[authentication-mode]{lang="EN-US"}**[为]{style="font-family:宋体"}**[scheme]{lang="EN-US"}**

[[N]{lang="EN-US"}]{#struct_0_18173_18228_x672093716}

[[表示无需认证，对应的]{style="font-family:宋体"}**[authentication-mode]{lang="EN-US"}**]{#struct_0_18173_18228_123696694}[为]{style="font-family:宋体"}**[none]{lang="EN-US"}**

[[P]{lang="EN-US"}]{#struct_0_18173_18228_775826114}

[[表示使用当前用户线的密码进行认证，对应的]{style="font-family:宋体"}**[authentication-mode]{lang="EN-US"}**]{#struct_0_18173_18228_550934193}[为]{style="font-family:宋体"}**[password]{lang="EN-US"}**

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x1661627119}[显示所有用户线的摘要信息。]{style="font-family:宋体"}

[[\<Sysname\> display line summary]{lang="EN-US"}]{#struct_0_18173_18228_2056789639}

[  Line type : \[CON\]]{lang="EN-US"}

[           0:U]{lang="EN-US"}

[  Line type : \[AUX\]]{lang="EN-US"}

[           1:X]{lang="EN-US"}

[  Line type : \[VTY\]]{lang="EN-US"}

[           2:UXXX X]{lang="EN-US"}

[ ]{lang="EN-US"}

[   2 lines used.      (U)]{lang="EN-US"}

[   5 lines not used.  (X)]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display line summary]{lang="EN-US"}]{#struct_0_18173_18228_x245282641}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1838393237}[[字段]{style="font-family:黑体"}]{#struct_0_18173_18228_33564530}

[[描述]{style="font-family:黑体"}]{#struct_0_18173_18228_987543365}

[[Line type]{lang="EN-US"}]{#struct_0_18173_18228_x1661627120}

[[用户线类型（]{style="font-family:宋体"}[CON/TTY/AUX/VTY]{lang="EN-US"}]{#struct_0_18173_18228_x315797820}[）]{style="font-family:宋体"}

[[0:X]{lang="EN-US"}]{#struct_0_18173_18228_x1391442083}

[[0]{lang="EN-US"}]{#struct_0_18173_18228_x2036534458}[表示用户线的绝对编号，]{style="font-family:宋体"}[X]{lang="EN-US"}[表示当前没有用户使用该用户线（]{style="font-family:宋体"}[U]{lang="EN-US"}[表示当前有用户使用该用户线）。比如"]{style="font-family:宋体"}[2:UXXX X]{lang="EN-US"}["表示该行第一个用户线的绝对编号是]{style="font-family:宋体"}[2]{lang="EN-US"}[，有用户使用；第]{style="font-family:宋体"}[3]{lang="EN-US"}[、]{style="font-family:宋体"}[4]{lang="EN-US"}[、]{style="font-family:宋体"}[5]{lang="EN-US"}[、]{style="font-family:宋体"}[6]{lang="EN-US"}[号用户线，没有用户使用]{style="font-family:宋体"}

[[lines used.      (U)]{lang="EN-US"}]{#struct_0_18173_18228_x1458871690}

[[当前正在使用的用户线的数目（即]{style="font-family:宋体"}[U]{lang="EN-US"}]{#struct_0_18173_18228_868233205}[字符的个数）]{style="font-family:宋体"}

[[lines not used.  (X)]{lang="EN-US"}]{#struct_0_18173_18228_x1661627121}

[[当前未使用的用户线的数目（即]{style="font-family:宋体"}[X]{lang="EN-US"}]{#struct_0_18173_18228_x1881881761}[字符的个数）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#820383044 .myid}
[]{#_Toc404782459}[]{#struct_0_18173_18228_943939676}

**登录设备 \-- 登录设备命令 \-- display telnet client**

------------------------------------------------------------------------

[**[display telnet client]{lang="EN-US"}**]{#struct_0_18173_18228_x1525921266}[命令用来显示设备作为]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[客户端的相关配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_2106880037}

[**[display telnet client]{lang="EN-US"}**]{#struct_0_18173_18228_31004260}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_208665893}

[[任意视图]{style="font-family:宋体"}]{#struct_0_18173_18228_x622144265}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_1372335718}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_1369674492}

[[network-operator]{lang="EN-US"}]{#struct_0_18173_18228_1999513085}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_1894382145}

[[mdc-operator]{lang="EN-US"}]{#struct_0_18173_18228_1242132374}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_575167108}

[[目前该命令显示的是]{style="font-family:宋体"}[Telnet]{lang="EN-US"}]{#struct_0_18173_18228_1887674415}[客户端源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址或源接口的配置信息。用户可以使用]{style="font-family:宋体"}**[telnet client source]{lang="EN-US"}**[命令指定]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[客户端源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址或源接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_1352812955}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_2106739090}[显示设备作为]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[客户端的相关配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display telnet client]{lang="EN-US"}]{#struct_0_18173_18228_x1163775820}

[ The source IP address is 1.1.1.1.]{lang="EN-US"}

[[以上显示信息表示设备作为]{style="font-family:宋体"}[Telnet]{lang="EN-US"}]{#struct_0_18173_18228_902842923}[客户端时，发送]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1026004360}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[telnet client source]{lang="EN-US"}**]{#struct_0_18173_18228_401514194}
:::

::: {#1751930072 .myid}
[]{#_Toc404782460}[]{#struct_0_18173_18228_x464623552}

**登录设备 \-- 登录设备命令 \-- display user-interface**

------------------------------------------------------------------------

[**[display user-interface]{lang="EN-US"}**]{#struct_0_18173_18228_1553497946}[命令用来显示用户线的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x766643125}

[**[display user-interface]{lang="EN-US"}**[ \[ *number1* \| { **aux** \| **console** \| **tty** \| **vty** } *number2* \] \[ **summary** \]]{lang="EN-US"}]{#struct_0_18173_18228_699957076}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1235469731}

[[任意视图]{style="font-family:宋体"}]{#struct_0_18173_18228_x2008799076}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1661627122}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1478597234}

[[network-operator]{lang="EN-US"}]{#struct_0_18173_18228_844553919}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_665155204}

[[mdc-operator]{lang="EN-US"}]{#struct_0_18173_18228_x605479540}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_1867975384}

[*[number1]{lang="EN-US"}*]{#struct_0_18173_18228_x1275881036}[：用户线的编号（绝对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准，一般从]{style="font-family:宋体"}[0]{lang="EN-US"}[开始。]{style="font-family:宋体"}

[**[aux]{lang="EN-US"}**]{#struct_0_18173_18228_624416607}[：]{style="font-family:宋体"}[AUX]{lang="EN-US"}[用户线。]{style="font-family:宋体"}

[**[console]{lang="EN-US"}**]{#struct_0_18173_18228_81816143}[：]{style="font-family:宋体"}[Console]{lang="EN-US"}[用户线。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[tty]{lang="EN-US"}**]{#struct_0_18173_18228_x1661627123}[：]{style="font-family:宋体"}[TTY]{lang="EN-US"}[用户线。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vty]{lang="EN-US"}**]{#struct_0_18173_18228_1250286121}[：]{style="font-family:宋体"}[VTY]{lang="EN-US"}[用户线。]{style="font-family:宋体"}

[*[number2]{lang="EN-US"}*]{#struct_0_18173_18228_x1115985489}[：用户线的编号（相对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[summary]{lang="EN-US"}**]{#struct_0_18173_18228_1692186286}[：显示用户线的摘要信息。不使用该参数时，将显示用户线类型、绝对]{style="font-family:宋体"}[/]{lang="EN-US"}[相对编号、传输速率、]{style="font-family:宋体"}[Modem]{lang="EN-US"}[属性、认证方式及接入接口；使用该参数时，将显示正在使用和未使用的用户线数目和类型。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_378749371}

[[该命令实现与]{style="font-family:宋体"}**[display line]{lang="EN-US"}**]{#struct_0_18173_18228_1050540761}[一致，仅为与旧版本兼容保留，请使用]{style="font-family:宋体"}**[display line]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_1376789608}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x1592517837}[显示用户线]{style="font-family:宋体"}[0]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display user-interface 0]{lang="EN-US"}]{#struct_0_18173_18228_x1661627124}

[  Idx  Type     Tx/Rx      Modem Auth  Int        Location]{lang="EN-US"}

[  0    CON 0    9600       -     N     -         0/0]{lang="EN-US"}

[ ]{lang="EN-US"}

[  +    : Line is active.]{lang="EN-US"}

[  F    : Line is active and in async mode.]{lang="EN-US"}

[  Idx  : Absolute index of line.]{lang="EN-US"}

[  Type : Type and relative index of line.]{lang="EN-US"}

[  Auth : Login authentication mode.]{lang="EN-US"}

[  Int  : Physical port of the line.]{lang="EN-US"}

[  A    : Authentication use AAA.]{lang="EN-US"}

[  N    : No authentication is required.]{lang="EN-US"}

[  P    : Password authentication.]{lang="EN-US"}

[]{#struct_0_18173_18228_1653570648}[]{#_Toc138230985}[]{#_Toc98236444}[[表1-5 ]{lang="EN-US"}[display user-interface]{lang="EN-US"}]{#_Toc98233658}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1840509795}[[字段]{style="font-family:黑体"}]{#struct_0_18173_18228_1210197097}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_18173_18228_x969442918}

[[+]{lang="EN-US"}]{#struct_0_18173_18228_x852323051}

[[表示当前正在使用的用户线]{style="font-family:宋体"}]{#struct_0_18173_18228_1355977820}

[[F]{lang="EN-US"}]{#struct_0_18173_18228_2002187179}

[[表示当前正在使用的用户线，且工作在异步方式]{style="font-family:宋体"}]{#struct_0_18173_18228_1640854738}

[[Idx]{lang="EN-US"}]{#struct_0_18173_18228_1628794980}

[[用户线的绝对编号]{style="font-family:宋体"}]{#struct_0_18173_18228_1670603034}

[[Type]{lang="EN-US"}]{#struct_0_18173_18228_x2083018402}

[[用户线的类型及相对编号]{style="font-family:宋体"}]{#struct_0_18173_18228_x852323052}

[[Tx/Rx]{lang="EN-US"}]{#struct_0_18173_18228_1356174428}

[[用户线的速率]{style="font-family:宋体"}]{#struct_0_18173_18228_x918793596}

[[Modem]{lang="EN-US"}]{#struct_0_18173_18228_147617016}

[[Modem]{lang="EN-US"}]{#struct_0_18173_18228_x1523567382}[的呼入]{style="font-family:宋体"}[/]{lang="EN-US"}[呼出开关，取值有]{style="font-family:宋体"}[in]{lang="EN-US"}[（允许呼入）、]{style="font-family:宋体"}[out]{lang="EN-US"}[（允许呼出）、]{style="font-family:宋体"}[inout]{lang="EN-US"}[（允许呼入呼出），缺省显示"]{style="font-family:宋体"}[-]{lang="EN-US"}["（表示没有配置）]{style="font-family:宋体"}

[[Auth]{lang="EN-US"}]{#struct_0_18173_18228_x852323053}

[[使用该用户线登录的用户的认证方式，取值有]{style="font-family:宋体"}[A]{lang="EN-US"}]{#struct_0_18173_18228_1356108892}[、]{style="font-family:宋体"}[L]{lang="EN-US"}[、]{style="font-family:宋体"}[N]{lang="EN-US"}[和]{style="font-family:宋体"}[P]{lang="EN-US"}[四种方式]{style="font-family:宋体"}

[[Int]{lang="EN-US"}]{#struct_0_18173_18228_x528299581}

[[用户线对应的物理接口的简称表示（没有对应接口的用户线均显示"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_18173_18228_420878880}["）]{style="font-family:宋体"}

[[Location]{lang="EN-US"}]{#struct_0_18173_18228_x396324621}

[[用户线的物理位置：]{style="font-family:宋体"}]{#struct_0_18173_18228_x396390157}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式设备：显示为"槽位号]{style="font-family:宋体"}]{#struct_0_18173_18228_1785210313}[/CPU]{lang="EN-US"}[编号"]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备---独立运行模式：显示为"槽位号]{style="font-family:宋体"}]{#struct_0_18173_18228_x396455693}[/CPU]{lang="EN-US"}[编号"]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备---]{style="font-family:宋体"}]{#struct_0_18173_18228_214402045}[IRF]{lang="EN-US"}[模式：显示为"设备成员编号]{style="font-family:宋体"}[/]{lang="EN-US"}[槽位号]{style="font-family:宋体"}[/CPU]{lang="EN-US"}[编号"]{style="font-family:宋体"}

[[A]{lang="EN-US"}]{#struct_0_18173_18228_x1716603868}

[[表示使用]{style="font-family:宋体"}[AAA]{lang="EN-US"}]{#struct_0_18173_18228_x852323054}[认证方式，对应的]{style="font-family:宋体"}**[authentication-mode]{lang="EN-US"}**[为]{style="font-family:宋体"}**[scheme]{lang="EN-US"}**

[[N]{lang="EN-US"}]{#struct_0_18173_18228_1356305500}

[[表示无需认证，对应的]{style="font-family:宋体"}**[authentication-mode]{lang="EN-US"}**]{#struct_0_18173_18228_x1306468819}[为]{style="font-family:宋体"}**[none]{lang="EN-US"}**

[[P]{lang="EN-US"}]{#struct_0_18173_18228_x891699285}

[[表示使用当前用户线的密码进行认证，对应的]{style="font-family:宋体"}**[authentication-mode]{lang="EN-US"}**]{#struct_0_18173_18228_1912868092}[为]{style="font-family:宋体"}**[password]{lang="EN-US"}**

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x852323055}[显示所有用户线的摘要信息。]{style="font-family:宋体"}

[[\<Sysname\> display user-interface summary]{lang="EN-US"}]{#struct_0_18173_18228_1356239964}

[  Line type : \[CON\]]{lang="EN-US"}

[           0:U]{lang="EN-US"}

[  Line type : \[AUX\]]{lang="EN-US"}

[           1:X]{lang="EN-US"}

[  Line type : \[VTY\]]{lang="EN-US"}

[           2:UXXX X]{lang="EN-US"}

[ ]{lang="EN-US"}

[   2 lines used.      (U)]{lang="EN-US"}

[   5 lines not used.  (X)]{lang="EN-US"}

[]{#struct_0_18173_18228_x929606254}[]{#_Toc138230986}[]{#_Toc98236445}[[表1-6 ]{lang="EN-US"}[display user-interface summary]{lang="EN-US"}]{#_Toc98233659}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1833897779}[[字段]{style="font-family:黑体"}]{#struct_0_18173_18228_863115367}

[[描述]{style="font-family:黑体"}]{#struct_0_18173_18228_x1108761756}

[[Line type]{lang="EN-US"}]{#struct_0_18173_18228_x852323056}

[[用户线类型（]{style="font-family:宋体"}[CON/TTY/AUX/VTY]{lang="EN-US"}]{#struct_0_18173_18228_1356436572}[）]{style="font-family:宋体"}

[[0:X]{lang="EN-US"}]{#struct_0_18173_18228_249063656}

[[0]{lang="EN-US"}]{#struct_0_18173_18228_1463760294}[表示用户线的绝对编号，]{style="font-family:宋体"}[X]{lang="EN-US"}[表示当前没有用户使用该用户线（]{style="font-family:宋体"}[U]{lang="EN-US"}[表示当前有用户使用该用户线）。比如"]{style="font-family:宋体"}[2:UXXX X]{lang="EN-US"}["表示该行第一个用户线的绝对编号是]{style="font-family:宋体"}[2]{lang="EN-US"}[，有用户使用；第]{style="font-family:宋体"}[3]{lang="EN-US"}[、]{style="font-family:宋体"}[4]{lang="EN-US"}[、]{style="font-family:宋体"}[5]{lang="EN-US"}[、]{style="font-family:宋体"}[6]{lang="EN-US"}[号用户线，没有用户使用]{style="font-family:宋体"}

[[lines used.      (U)]{lang="EN-US"}]{#struct_0_18173_18228_x1003859100}

[[当前正在使用的用户线的数目（即]{style="font-family:宋体"}[U]{lang="EN-US"}]{#struct_0_18173_18228_x1611993894}[字符的个数）]{style="font-family:宋体"}

[[lines not used.  (X)]{lang="EN-US"}]{#struct_0_18173_18228_x852323057}

[[当前未使用的用户线的数目（即]{style="font-family:宋体"}[X]{lang="EN-US"}]{#struct_0_18173_18228_1356371036}[字符的个数）]{style="font-family:宋体"}

[]{#_Toc139341875}[]{#_Toc139341874}[ ]{lang="EN-US"}

::: {#-442880117 .myid}
[]{#_Toc404782461}[]{#struct_0_18173_18228_x2085834596}[]{#_Toc263186398}

**登录设备 \-- 登录设备命令 \-- display users**

------------------------------------------------------------------------

[**[display users]{lang="EN-US"}**]{#struct_0_18173_18228_1035260936}[命令用来显示当前正在使用的用户线以及用户的相关信息。]{style="font-family:宋体"}

[**[display users all]{lang="EN-US"}**]{#struct_0_18173_18228_x2085350054}[命令用来显示设备支持所有用户线以及用户的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1134903417}

[**[display users]{lang="EN-US"}**[ \[ **all** \]]{lang="EN-US"}]{#struct_0_18173_18228_x332242901}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1922708697}

[[任意视图]{style="font-family:宋体"}]{#struct_0_18173_18228_x852323058}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_1356567644}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x126028755}

[[network-operator]{lang="EN-US"}]{#struct_0_18173_18228_x683170489}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_x887471010}

[[mdc-operator]{lang="EN-US"}]{#struct_0_18173_18228_x1774012028}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_x301088296}

[**[all]{lang="EN-US"}**]{#struct_0_18173_18228_607688013}[：显示设备支持的所有用户线以及用户的相关信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1261889395}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x852323059}[显示当前正在使用的用户线以及用户的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display users]{lang="EN-US"}]{#struct_0_18173_18228_1356502108}

[  Idx  Line     Idle       Time              Pid     Type]{lang="EN-US"}

[  10   VTY 0    00:10:49   Jun 11 11:27:32   320     TEL]{lang="EN-US"}

[+ 11   VTY 1    00:00:00   Jun 11 11:39:40   334     TEL]{lang="EN-US"}

[ ]{lang="EN-US"}

[Following are more details.]{lang="EN-US"}

[VTY 0   :]{lang="EN-US"}

[        Location: 192.168.1.12]{lang="EN-US"}

[VTY 1   :]{lang="EN-US"}

[        Location: 192.168.1.26]{lang="EN-US"}

[ +    : Current operation user.]{lang="EN-US"}

[ F    : Current operation user works in async mode.]{lang="EN-US"}

[[以上显示信息表明，当前有两个用户已经登录设备，用户自己使用的是]{style="font-family:宋体"}[VTY 1]{lang="EN-US"}]{#struct_0_18173_18228_1820015416}[用户线，用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.1.26]{lang="EN-US"}[；另一个用户使用的是]{style="font-family:宋体"}[VTY 0]{lang="EN-US"}[用户线。]{style="font-family:宋体"}

[]{#struct_0_18173_18228_x687483378}[[表1-7 ]{lang="EN-US"}[display users]{lang="EN-US"}]{#_Toc138230987}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1836014217}[[字段]{style="font-family:黑体"}]{#struct_0_18173_18228_1988874325}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_18173_18228_x852323060}

[[Idx]{lang="EN-US"}]{#struct_0_18173_18228_1356043357}

[[用户线的绝对编号]{style="font-family:宋体"}]{#struct_0_18173_18228_x517421245}

[[Line]{lang="EN-US"}]{#struct_0_18173_18228_x1255973371}

[[用户线的相对编号，第一列（比如]{style="font-family:宋体"}[VTY]{lang="EN-US"}]{#struct_0_18173_18228_x1972909074}[）表示用户线的类型，第二列（比如]{style="font-family:宋体"}[0]{lang="EN-US"}[）表示用户线的相对编号]{style="font-family:宋体"}

[[Idle]{lang="EN-US"}]{#struct_0_18173_18228_x1644574877}

[[空闲时间，表明用户和设备没有报文交互的时间长度，格式为]{style="font-family:宋体"}[hh:mm:ss]{lang="EN-US"}]{#struct_0_18173_18228_1486329109}[。当空闲时间大于等于]{style="font-family:宋体"}[24]{lang="EN-US"}[小时时，显示为]{style="font-family:宋体"}[old]{lang="EN-US"}

[[Time]{lang="EN-US"}]{#struct_0_18173_18228_x1355856040}

[[用户本次登录的时间]{style="font-family:宋体"}]{#struct_0_18173_18228_738535737}

[[Pid]{lang="EN-US"}]{#struct_0_18173_18228_619559775}

[[用户对应的进程]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_18173_18228_1642180345}[（]{style="font-family:宋体"}[CLI]{lang="EN-US"}[用户登录时，系统会自动运行一个用户登录进程来监控用户的操作）]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_18173_18228_1426539450}

[[显示用户的登录类型，如]{style="font-family:宋体"}[Telnet]{lang="EN-US"}]{#struct_0_18173_18228_1486329108}[、]{style="font-family:宋体"}[SSH]{lang="EN-US"}[、]{style="font-family:宋体"}[PAD]{lang="EN-US"}

[[+]{lang="EN-US"}]{#struct_0_18173_18228_x1355790504}

[[当前操作用户]{style="font-family:宋体"}]{#struct_0_18173_18228_754960398}

[[Location]{lang="EN-US"}]{#struct_0_18173_18228_1333703814}

[[使用该用户线登录的用户的位置信息（即用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_18173_18228_x1919710890}[地址）]{style="font-family:宋体"}

[[F]{lang="EN-US"}]{#struct_0_18173_18228_1486329107}

[[当前操作用户工作在异步模式]{style="font-family:宋体"}]{#struct_0_18173_18228_x1356511400}

[]{#_Toc100291509}[[ ]{lang="EN-US"}]{#_Toc15375232}

::::: {#399016337 .myid}
[]{#_Toc404782462}[]{#struct_0_18173_18228_1113147786}

**登录设备 \-- 登录设备命令 \-- display web menu**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](登录设备命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_18173_18228_x1930921575}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_18173_18228_x784746714}
:::

**[ ]{lang="EN-US"}**

[**[display web menu]{lang="EN-US"}**]{#struct_0_18173_18228_1486761537}[命令用来显示]{style="font-family:宋体"}[Web]{lang="EN-US"}[的页面菜单树。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x226432081}

[**[display web menu]{lang="EN-US"}**]{#struct_0_18173_18228_1486329106}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1356445864}

[[任意视图]{style="font-family:宋体"}]{#struct_0_18173_18228_126564465}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1049745935}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1535632194}

[[network-operator]{lang="EN-US"}]{#struct_0_18173_18228_x193527585}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_1018796713}

[[mdc-operator]{lang="EN-US"}]{#struct_0_18173_18228_200273403}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_1486329105}

[[当用户需要配置角色对应的]{style="font-family:宋体"}[web]{lang="EN-US"}]{#struct_0_18173_18228_x1356642472}[菜单项时，可使用这个命令来查看系统支持的全部菜单树。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x540937201}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_1545652907}[显示全部]{style="font-family:宋体"}[web]{lang="EN-US"}[菜单信息。]{style="font-family:宋体"}

[[\<Sysname\> display web menu]{lang="EN-US"}]{#struct_0_18173_18228_1486329104}

[  .]{lang="EN-US"}

[    \`\--Device: ID = m_device]{lang="EN-US"}

[         \|\--Summary: ID = m_panel]{lang="EN-US"}

[         \|    \|\--System Information: ID = i_main]{lang="EN-US"}

[         \|    \`\--Device Information: ID = i_panel]{lang="EN-US"}

[         \|\--Basic Settings: ID = m_device_basic]{lang="EN-US"}

[         \|    \|\--Device Name: ID = i_device_sysname]{lang="EN-US"}

[         \|    \`\--Web Idle Timeout: ID = i_device_webidle]{lang="EN-US"}

[         \|\--Device Maintenance: ID = m_maintains]{lang="EN-US"}

[         \|    \`\--Reboot: ID = i_reboot]{lang="EN-US"}

[         \|\--System Time: ID = m_datetime]{lang="EN-US"}

[         \|    \|\--UTC Time: ID = i_systime]{lang="EN-US"}

[         \|    \`\--Time Zone: ID = i_timezone]{lang="EN-US"}

[         \|\--System Log: ID = m_log]{lang="EN-US"}

[         \|    \|\--Log List: ID = i_syslog]{lang="EN-US"}

[         \|    \|\--Log Host: ID = i_loghost]{lang="EN-US"}

[         \|    \`\--Log Setup: ID = i_logsetup]{lang="EN-US"}

[         \|\--Port Management: ID = m_port]{lang="EN-US"}

[         \|    \|\--Summary: ID = i_portsummary]{lang="EN-US"}

[         \|    \`\--Setup: ID = i_portsetup]{lang="EN-US"}

[         \|\--Interface Statistics: ID = m_int_statistic]{lang="EN-US"}

[         \|    \`\--Interface Statistics: ID = i_statistic_summary]{lang="EN-US"}

[         \`\--Configuration: ID = m_config]{lang="EN-US"}

[              \|\--Save: ID = i_save]{lang="EN-US"}

[              \|\--Backup: ID = i_backup]{lang="EN-US"}

[              \|\--Restore: ID = i_restore]{lang="EN-US"}

[              \|\--Import: ID = i_import]{lang="EN-US"}

[              \`\--Export: ID = i_export]{lang="EN-US"}
:::::

::::: {#73509292 .myid}
[]{#_Toc404782463}[]{#struct_0_18173_18228_x1356576936}[]{#_Toc319416211}

**登录设备 \-- 登录设备命令 \-- display web users**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](登录设备命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_18173_18228_1264877045}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_18173_18228_1486329103}
:::

**[ ]{lang="EN-US"}**

[**[display web users]{lang="EN-US"}**]{#struct_0_18173_18228_x1356249256}[命令用来显示当前]{style="font-family:宋体"}[Web]{lang="EN-US"}[用户的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1385750115}

[**[display web users]{lang="EN-US"}**]{#struct_0_18173_18228_1117196912}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1828917699}

[[任意视图]{style="font-family:宋体"}]{#struct_0_18173_18228_2022887099}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_989245893}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_230740218}

[[network-operator]{lang="EN-US"}]{#struct_0_18173_18228_1479749295}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_1486329102}

[[mdc-operator]{lang="EN-US"}]{#struct_0_18173_18228_x1356183720}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_1008608442}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_447400060}[显示当前]{style="font-family:宋体"}[Web]{lang="EN-US"}[用户的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display web users]{lang="EN-US"}]{#struct_0_18173_18228_540811268}

[UserID          Name            Type   Language JobCount LoginTime LastOperation]{lang="EN-US"}

[AB2039483271293 Administrator   HTTP   Chinese     3     12:00:23  14:10:05]{lang="EN-US"}

[F09382BA2014AC8 user            HTTPS  English     1     13:05:00  14:11:00]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display web users]{lang="EN-US"}]{#struct_0_18173_18228_x1740297831}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1831027927}[[字段]{style="font-family:黑体"}]{#struct_0_18173_18228_x992396106}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_18173_18228_1486329101}

[[UserID]{lang="EN-US"}]{#struct_0_18173_18228_x1356380328}

[[Web]{lang="EN-US"}]{#struct_0_18173_18228_1502792078}[用户的]{style="font-family:宋体"}[ID]{lang="EN-US"}[号，用来唯一标识一个登录用户]{style="font-family:宋体"}

[[Name]{lang="EN-US"}]{#struct_0_18173_18228_x1957807541}

[[Web]{lang="EN-US"}]{#struct_0_18173_18228_x2020596234}[用户的登录用户名]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_18173_18228_x556320296}

[[Web]{lang="EN-US"}]{#struct_0_18173_18228_1486329100}[用户登录使用的协议类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HTTP]{lang="EN-US"}]{#struct_0_18173_18228_x1356314792}[表示]{lang="EN-US" style="font-family:宋体"}[Hypertext Transfer Protocol]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HTTPS]{lang="EN-US"}]{#struct_0_18173_18228_1618883261}[表示基于安全套接字的]{lang="EN-US" style="font-family:宋体"}[Hypertext Transfer Protocol]{lang="EN-US"}

[[Language]{lang="EN-US"}]{#struct_0_18173_18228_1729013329}

[[Web]{lang="EN-US"}]{#struct_0_18173_18228_x1645833806}[用户登录时使用的语言：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Chinese]{lang="EN-US"}]{#struct_0_18173_18228_1281772973}[表示中文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[English]{lang="EN-US"}]{#struct_0_18173_18228_1908051426}[表示英文]{lang="EN-US" style="font-family:宋体"}

[[JobCount]{lang="EN-US"}]{#struct_0_18173_18228_x85486315}

[[Web]{lang="EN-US"}]{#struct_0_18173_18228_x337996489}[用户建立的连接数量]{style="font-family:宋体"}

[[LoginTime]{lang="EN-US"}]{#struct_0_18173_18228_x238618166}

[[Web]{lang="EN-US"}]{#struct_0_18173_18228_132876207}[用户的登录时间]{style="font-family:宋体"}

[[LastOperation]{lang="EN-US"}]{#struct_0_18173_18228_1385110716}

[[Web]{lang="EN-US"}]{#struct_0_18173_18228_x85486316}[用户的最后操作时间]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#965544710 .myid}
[]{#_Toc404782464}[]{#struct_0_18173_18228_x337996486}[]{#_Toc297210644}[]{#_Toc296689414}[]{#_Toc296419362}[]{#_Toc141003647}[]{#_Toc141005236}[]{#_Toc141591293}[]{#_Toc191788225}[]{#_Toc192407681}[]{#_Toc192495949}[]{#_Toc191788226}[]{#_Toc192407682}[]{#_Toc192495950}[]{#_Toc191788227}[]{#_Toc192407683}[]{#_Toc192495951}[]{#_Toc191788228}[]{#_Toc192407684}[]{#_Toc192495952}[]{#_Toc191788229}[]{#_Toc192407685}[]{#_Toc192495953}[]{#_Toc191788230}[]{#_Toc192407686}[]{#_Toc192495954}[]{#_Toc191788231}[]{#_Toc192407687}[]{#_Toc192495955}[]{#_Toc191788232}[]{#_Toc192407688}[]{#_Toc192495956}[]{#_Toc191788233}[]{#_Toc192407689}[]{#_Toc192495957}[]{#_Toc191788234}[]{#_Toc192407690}[]{#_Toc192495958}[]{#_Toc191788235}[]{#_Toc192407691}[]{#_Toc192495959}[]{#_Toc191788236}[]{#_Toc192407692}[]{#_Toc192495960}[]{#_Toc191788237}[]{#_Toc192407693}[]{#_Toc192495961}[]{#_Toc191788238}[]{#_Toc192407694}[]{#_Toc192495962}[]{#_Toc191788239}[]{#_Toc192407695}[]{#_Toc192495963}[]{#_Toc191788240}[]{#_Toc192407696}[]{#_Toc192495964}[]{#_Toc191788241}[]{#_Toc192407697}[]{#_Toc192495965}[]{#_Toc191788242}[]{#_Toc192407698}[]{#_Toc192495966}[]{#_Toc191788243}[]{#_Toc192407699}[]{#_Toc192495967}[]{#_Toc191788244}[]{#_Toc192407700}[]{#_Toc192495968}[]{#_Toc191788246}[]{#_Toc192407702}[]{#_Toc192495970}[]{#_Toc56565319}[]{#_Toc56565320}[]{#_Toc191788248}[]{#_Toc192407704}[]{#_Toc192495972}[]{#_Toc191788249}[]{#_Toc192407705}[]{#_Toc192495973}[]{#_Toc191788250}[]{#_Toc192407706}[]{#_Toc192495974}[]{#_Toc191788251}[]{#_Toc192407707}[]{#_Toc192495975}[]{#_Toc191788252}[]{#_Toc192407708}[]{#_Toc192495976}[]{#_Toc191788253}[]{#_Toc192407709}[]{#_Toc192495977}[]{#_Toc191788254}[]{#_Toc192407710}[]{#_Toc192495978}[]{#_Toc191788255}[]{#_Toc192407711}[]{#_Toc192495979}[]{#_Toc191788256}[]{#_Toc192407712}[]{#_Toc192495980}[]{#_Toc191788257}[]{#_Toc192407713}[]{#_Toc192495981}[]{#_Toc191788258}[]{#_Toc192407714}[]{#_Toc192495982}[]{#_Toc191788259}[]{#_Toc192407715}[]{#_Toc192495983}[]{#_Toc191788260}[]{#_Toc192407716}[]{#_Toc192495984}[]{#_Toc191788261}[]{#_Toc192407717}[]{#_Toc192495985}[]{#_Toc191788262}[]{#_Toc192407718}[]{#_Toc192495986}[]{#_Toc191788263}[]{#_Toc192407719}[]{#_Toc192495987}[]{#_Toc191788264}[]{#_Toc192407720}[]{#_Toc192495988}[]{#_Toc191788269}[]{#_Toc192407725}[]{#_Toc192495993}[]{#_Toc191788270}[]{#_Toc192407726}[]{#_Toc192495994}[]{#_Toc191788271}[]{#_Toc192407727}[]{#_Toc192495995}[]{#_Toc191788272}[]{#_Toc192407728}[]{#_Toc192495996}[]{#_Toc191788273}[]{#_Toc192407729}[]{#_Toc192495997}[]{#_Toc191788274}[]{#_Toc192407730}[]{#_Toc192495998}[]{#_Toc191788275}[]{#_Toc192407731}[]{#_Toc192495999}[]{#_Toc191788276}[]{#_Toc192407732}[]{#_Toc192496000}[]{#_Toc191788277}[]{#_Toc192407733}[]{#_Toc192496001}[]{#_Toc191788278}[]{#_Toc192407734}[]{#_Toc192496002}[]{#_Toc191788279}[]{#_Toc192407735}[]{#_Toc192496003}[]{#_Toc191788280}[]{#_Toc192407736}[]{#_Toc192496004}[]{#_Toc191788281}[]{#_Toc192407737}[]{#_Toc192496005}[]{#_Toc191788282}[]{#_Toc192407738}[]{#_Toc192496006}[]{#_Toc191788283}[]{#_Toc192407739}[]{#_Toc192496007}[]{#_Toc191788284}[]{#_Toc192407740}[]{#_Toc192496008}[]{#_Toc191788285}[]{#_Toc192407741}[]{#_Toc192496009}[]{#_Toc56565323}[]{#_Toc56565324}

**登录设备 \-- 登录设备命令 \-- escape-key**

------------------------------------------------------------------------

[**[escape-key]{lang="EN-US"}**]{#struct_0_18173_18228_x238421558}[命令用来配置终止当前运行任务（比如]{style="font-family:宋体"}**[ping]{lang="EN-US"}**[命令等）的快捷键。]{style="font-family:宋体"}

[**[undo escape-key]{lang="EN-US"}**]{#struct_0_18173_18228_583757307}[命令用来取消快捷键的配置，包括缺省快捷键。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_985233690}

[**[escape-key]{lang="EN-US"}**[ { *key-string* \| **default** }]{lang="EN-US"}]{#struct_0_18173_18228_x1721006182}

[**[undo escape-key]{lang="EN-US"}**]{#struct_0_18173_18228_x803423228}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_x2113241911}

[[按]{style="font-family:宋体"}[\<Ctrl+C\>]{lang="EN-US"}]{#struct_0_18173_18228_x85486317}[组合键终止当前运行的任务。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_x337996487}

[[用户线视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18173_18228_x238487094}[用户线类视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_2121106633}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1798750779}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_249493775}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_417447801}

[*[key-string]{lang="EN-US"}*]{#struct_0_18173_18228_x128549967}[：定义终止当前运行任务的快捷键，可以是区分大小写的单个字符，也可以是单个字符或组合键对应的]{style="font-family:宋体"}[ACSII]{lang="EN-US"}[码（]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[）。比如设置]{style="font-family:宋体"}**[escape-key]{lang="EN-US"}**[ 65]{lang="EN-US"}[，此时生效快捷键为]{style="font-family:宋体"}[A]{lang="EN-US"}[；如果设置]{style="font-family:宋体"}**[escape-key ]{lang="EN-US"}**[a]{lang="EN-US"}[，生效的快捷键为]{style="font-family:宋体"}[a]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[default]{lang="EN-US"}**]{#struct_0_18173_18228_x1281942866}[：恢复为缺省的快捷键]{style="font-family:宋体"}[\<Ctrl+C\>]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_x85486318}

[[有些命令行执行时间比较长，比如]{style="font-family:宋体"}[ping]{lang="EN-US"}]{#struct_0_18173_18228_x337996476}[时指定发送]{style="font-family:宋体"}[1000]{lang="EN-US"}[个包、]{style="font-family:宋体"}[tracert]{lang="EN-US"}[时目的地址不可达，系统执行这些命令时，在当前用户线下用户无法输入其他命令。此时，用户可以按]{style="font-family:宋体"}[\<Ctrl+C\>]{lang="EN-US"}[组合键来终止]{style="font-family:宋体"}[ping]{lang="EN-US"}[或者]{style="font-family:宋体"}[tracert]{lang="EN-US"}[任务，以便输入新的命令。如果配置了]{style="font-family:宋体"}**[escape-key]{lang="EN-US"}**[，则用户可以用新配置的快捷键来代替]{style="font-family:宋体"}[\<Ctrl+C\>]{lang="EN-US"}[。命令行是否支持]{style="font-family:宋体"}[\<Ctrl+C\>]{lang="EN-US"}[终止与功能模块的软件实现有关，请参见相关命令行的描述。]{style="font-family:宋体"}

[[如果设置的快捷键为单个字符，且当前有任务可终止，则输入快捷键会终止命令的执行；如果当前没有任务可终止，则输入的快捷键会作为普通的编辑字符。如果在某用户线下设置了]{style="font-family:宋体"}*[key-string]{lang="EN-US"}*]{#struct_0_18173_18228_x238421571}[，当使用该用户线登录到设备，又通过该设备]{style="font-family:宋体"}[telnet]{lang="EN-US"}[到别的设备，这时的]{style="font-family:宋体"}*[key-string]{lang="EN-US"}*[将被视为控制字符，只能用来中止当前的任务，不能作为编辑字符输入。比如，在]{style="font-family:宋体"}[Device A]{lang="EN-US"}[的]{style="font-family:宋体"}[VTY 0]{lang="EN-US"}[用户线下指定]{style="font-family:宋体"}*[key-string]{lang="EN-US"}*[为]{style="font-family:宋体"}[e]{lang="EN-US"}[，此时，]{style="font-family:宋体"}[PC]{lang="EN-US"}[（超级终端）使用]{style="font-family:宋体"}[VTY 0]{lang="EN-US"}[用户线登录设备，在]{style="font-family:宋体"}[PC]{lang="EN-US"}[上]{style="font-family:宋体"}[e]{lang="EN-US"}[可以作为编辑字符输入，也可以用]{style="font-family:
宋体"}[e]{lang="EN-US"}[来中止]{style="font-family:
宋体"}[Device A]{lang="EN-US"}[上正在运行的任务。如果通过]{style="font-family:宋体"}[Device A]{lang="EN-US"}[再]{style="font-family:宋体"}[telnet]{lang="EN-US"}[到]{style="font-family:宋体"}[Device B]{lang="EN-US"}[，则此时，]{style="font-family:宋体"}[PC]{lang="EN-US"}[上只能使用]{style="font-family:宋体"}[e]{lang="EN-US"}[来中止]{style="font-family:宋体"}[Device B]{lang="EN-US"}[上正在运行的任务，不能作为编辑字符输入。所以，建议用户尽量将]{style="font-family:宋体"}*[key-string]{lang="EN-US"}*[配置为组合键。]{style="font-family:宋体"}

[[多次执行该命令配置不同的快捷键时，最新的配置生效。新设置的快捷键可以使用]{style="font-family:宋体"}**[display current-configuration]{lang="EN-US"}**]{#struct_0_18173_18228_584216061}[命令来查看。]{style="font-family:
宋体"}

[[如果用户线视图下配置]{style="font-family:宋体"}**[escape-key]{lang="EN-US"}**]{#struct_0_18173_18228_x739036492}[为缺省值，并且此时用户线类视图下配置了]{style="font-family:宋体"}**[escape-key]{lang="EN-US"}**[，那么用户线视图下的生效配置值为用户线类视图下的配置；如果用户线类视图下未配置，则生效的为缺省值。]{style="font-family:宋体"}

[[需要注意的是，用户线视图下使用本命令配置的快捷键立即生效；用户线类视图下配置的快捷键将在下次登录时生效。]{style="font-family:宋体"}]{#struct_0_18173_18228_763707191}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_85588081}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x422266115}[配置终止当前运行任务的快捷键为]{style="font-family:宋体"}[a]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_x85486319}

[\[Sysname\] line console 0]{lang="EN-US"}

[\[Sysname-line-console0\] escape-key a]{lang="EN-US"}

[[验证过程如下：]{style="font-family:宋体"}]{#struct_0_18173_18228_x337996477}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_18173_18228_x238487107}**[ping]{lang="EN-US"}**[命令检查]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.1.49]{lang="EN-US"}[的设备是否可达，并用]{style="font-family:宋体"}**[-c]{lang="EN-US"}**[参数指定发送]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[回显请求报文的数目为]{style="font-family:宋体"}[20]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> ping -c 20 192.168.1.49]{lang="EN-US"}]{#struct_0_18173_18228_164857026}

[  PING 192.168.1.49: 56  data bytes, press a to break]{lang="EN-US"}

[    Reply from 192.168.1.49: bytes=56 Sequence=1 ttl=255 time=3 ms]{lang="EN-US"}

[    Reply from 192.168.1.49: bytes=56 Sequence=2 ttl=255 time=3 ms]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[键入]{style="font-family:宋体"}]{#struct_0_18173_18228_x507231440}[a]{lang="EN-US"}[，任务立即终止，并返回到当前视图。]{style="font-family:宋体"}

[[  \-\-- 192.168.1.49 ping statistics \-\--]{lang="EN-US"}]{#struct_0_18173_18228_x85486320}

[    2 packet(s) transmitted]{lang="EN-US"}

[    2 packet(s) received]{lang="EN-US"}

[    0.00% packet loss]{lang="EN-US"}

[    round-trip min/avg/max = 3/3/3 ms]{lang="EN-US"}

[\<Sysname\>]{lang="EN-US"}
:::

::: {#956270952 .myid}
[]{#_Toc139341877}[]{#_Toc404782465}[]{#struct_0_18173_18228_1235981628}[]{#_Toc263186400}

**登录设备 \-- 登录设备命令 \-- flow-control**

------------------------------------------------------------------------

[**[flow-control]{lang="EN-US"}**]{#struct_0_18173_18228_54370135}[命令用来配置流量控制方式。]{style="font-family:宋体"}

[**[undo flow-control]{lang="EN-US"}**]{#struct_0_18173_18228_1278048629}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x341209039}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[不支持]{lang="EN-US" style="font-family:宋体"}*[direction1]{lang="EN-US"}*]{#struct_0_18173_18228_x1888933348}[、]{lang="EN-US" style="font-family:宋体"}*[direction2]{lang="EN-US"}*[参数的设备：]{lang="EN-US" style="font-family:宋体"}

[**[flow-control ]{lang="EN-US"}**[{ **hardware** \| **none** \| **software** }]{lang="EN-US"}]{#struct_0_18173_18228_x85486321}

[**[undo flow-control]{lang="EN-US"}**]{#struct_0_18173_18228_1235981627}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[支持]{lang="EN-US" style="font-family:宋体"}*[direction1]{lang="EN-US"}*]{#struct_0_18173_18228_54173527}[、]{lang="EN-US" style="font-family:宋体"}*[direction2]{lang="EN-US"}*[参数的设备：]{lang="EN-US" style="font-family:宋体"}

[**[flow-control ]{lang="EN-US"}**[{ **hardware** \| **none** \| **software** }]{lang="EN-US"}]{#struct_0_18173_18228_1581583281}

[**[flow-control hardware]{lang="EN-US"}**[ *direction1* \[ **software** *direction2* \]]{lang="EN-US"}]{#struct_0_18173_18228_x85486322}

[**[flow-control software]{lang="EN-US"}**[ *direction1* \[ **hardware** *direction2* \]]{lang="EN-US"}]{#struct_0_18173_18228_1235981630}

[**[undo flow-control]{lang="EN-US"}**]{#struct_0_18173_18228_53845848}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_x85486323}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_18173_18228_1235981629}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_54304599}

[[用户线视图]{style="font-family:宋体"}]{#struct_0_18173_18228_x1497942757}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_x2053161372}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x271447044}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_1303398794}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1468086050}

[**[hardware]{lang="EN-US"}**]{#struct_0_18173_18228_x85486324}[：进行硬件方式的流量控制。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_18173_18228_1235981624}[：不进行流量控制。]{style="font-family:宋体"}

[**[software]{lang="EN-US"}**]{#struct_0_18173_18228_54107991}[：进行软件方式的流量控制。]{style="font-family:宋体"}

[*[direction1]{lang="EN-US"}*]{#struct_0_18173_18228_x2041801451}[、]{style="font-family:宋体"}*[direction2]{lang="EN-US"}*[：表示流量控制的方向，取值为]{style="font-family:宋体"}**[in]{lang="EN-US"}**[或]{style="font-family:宋体"}**[out]{lang="EN-US"}**[，]{style="font-family:宋体"}**[in]{lang="EN-US"}**[表示入方向，即本设备接受远端设备流量控制；]{style="font-family:宋体"}**[out]{lang="EN-US"}**[表示出方向，即本设备流量控制远端设备。]{style="font-family:宋体"}*[direction1]{lang="EN-US"}*[和]{style="font-family:宋体"}*[direction2]{lang="EN-US"}*[参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_1594763633}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[不支持]{lang="EN-US" style="font-family:宋体"}*[direction1]{lang="EN-US"}*]{#struct_0_18173_18228_x2041801452}[、]{lang="EN-US" style="font-family:宋体"}*[direction2]{lang="EN-US"}*[参数的设备：]{lang="EN-US" style="font-family:宋体"}

[[流量控制分为入方向和出方向，入方向表示本设备能够接受远端设备的流量控制，出方向表示本设备能够对远端设备进行流量控制。配置该命令后，指定的流量控制方式对入方向和出方向都生效。]{style="font-family:宋体"}]{#struct_0_18173_18228_1191479106}

[[要使流量控制生效，双方才能正常通信，对端设备也要配置相同的流量控制方式。]{style="font-family:宋体"}]{#struct_0_18173_18228_x1547878730}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[支持]{lang="EN-US" style="font-family:宋体"}*[direction1]{lang="EN-US"}*]{#struct_0_18173_18228_x2041801453}[、]{lang="EN-US" style="font-family:宋体"}*[direction2]{lang="EN-US"}*[参数的设备：]{lang="EN-US" style="font-family:宋体"}

[[流量控制分为]{style="font-family:宋体"}**[in]{lang="EN-US"}**]{#struct_0_18173_18228_x1537404249}[和]{style="font-family:宋体"}**[out]{lang="EN-US"}**[两个方向，]{style="font-family:宋体"}**[in]{lang="EN-US"}**[表示本设备能够接受远端设备流量控制，]{style="font-family:宋体"}**[out]{lang="EN-US"}**[表示本设备能够流量控制远端设备。流量控制方式又分为]{style="font-family:宋体"}**[hardware]{lang="EN-US"}**[、]{style="font-family:宋体"}**[software]{lang="EN-US"}**[和]{style="font-family:宋体"}**[none]{lang="EN-US"}**[三种，同一个方向，只能配置一种流量控制方式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果要给]{lang="EN-US" style="font-family:宋体"}**[in]{lang="EN-US"}**]{#struct_0_18173_18228_423924866}[和]{lang="EN-US" style="font-family:宋体"}**[out]{lang="EN-US"}**[方向配置相同的流量控制方式，请使用命令]{lang="EN-US" style="font-family:宋体"}**[flow-control]{lang="EN-US"}**[ { **hardware** \| **software** \| **none** }]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果要给]{lang="EN-US" style="font-family:宋体"}**[in]{lang="EN-US"}**]{#struct_0_18173_18228_x2041801454}[和]{lang="EN-US" style="font-family:宋体"}**[out]{lang="EN-US"}**[方向配置不同的流量控制方式，请使用命令]{lang="EN-US" style="font-family:宋体"}**[flow-control hardware]{lang="EN-US"}**[ *direction1* \[ **software** *direction2* \]]{lang="EN-US"}[或]{lang="EN-US" style="font-family:
宋体"}**[flow-control software]{lang="EN-US"}**[ *direction1* \[ **hardware** *direction2* \]]{lang="EN-US"}[。当不指定可选参数时，表示另一个方向的流量控制方式为]{lang="EN-US" style="font-family:宋体"}**[none]{lang="EN-US"}**[（比如配置]{lang="EN-US" style="font-family:宋体"}**[flow-control hardware in]{lang="EN-US"}**[，则系统会自动将]{lang="EN-US" style="font-family:宋体"}**[out]{lang="EN-US"}**[方向配置为无流量控制）。]{lang="EN-US" style="font-family:宋体"}

[[要使流量控制生效，本设备上]{style="font-family:宋体"}**[in]{lang="EN-US"}**]{#struct_0_18173_18228_1998048160}[（]{style="font-family:宋体"}**[out]{lang="EN-US"}**[）方向配置的流量控制方式和对端设备上]{style="font-family:宋体"}**[out]{lang="EN-US"}**[（]{style="font-family:宋体"}**[in]{lang="EN-US"}**[）方向配置]{style="font-family:宋体"}

[[的流量控制方式必须相同。]{style="font-family:宋体"}]{#struct_0_18173_18228_x1614236709}

[[VTY]{lang="EN-US"}]{#struct_0_18173_18228_x2041801455}[用户线视图不支持该命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x730835195}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_1406835736}[配置]{style="font-family:宋体"}[Console 0]{lang="EN-US"}[用户线视图下，入方向和出方向都采用软件流量控制方式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_x84121110}

[\[Sysname\] line console 0]{lang="EN-US"}

[\[Sysname-line-console0\] flow-control software]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x2041801456}[配置]{style="font-family:宋体"}[Console 0]{lang="EN-US"}[用户线视图下，入方向采用硬件流量控制方式，出方向不进行流量控制。（支持]{style="font-family:宋体"}*[direction1]{lang="EN-US"}*[、]{style="font-family:宋体"}*[direction2]{lang="EN-US"}*[参数的设备才支持该举例）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_x1134119722}

[\[Sysname\] line console 0]{lang="EN-US"}

[\[Sysname-line-console0\] flow-control hardware in]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x2041801457}[配置]{style="font-family:宋体"}[Console 0]{lang="EN-US"}[用户线视图下，入方向采用硬件流量控制方式，出方向采用软件流量控制方式。（支持]{style="font-family:宋体"}*[direction1]{lang="EN-US"}*[、]{style="font-family:宋体"}*[direction2]{lang="EN-US"}*[参数的设备才支持该举例）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_431964219}

[\[Sysname\] line console 0]{lang="EN-US"}

[\[Sysname-line-console0\] flow-control hardware in software out]{lang="EN-US"}
:::

::: {#1365385653 .myid}
[]{#_Toc263186401}[]{#_Toc139341878}[]{#_Toc100291510}[]{#struct_0_18173_18228_x904525909}[]{#_Toc141003657}[]{#_Toc141005246}[]{#_Toc141591303}[]{#_Toc141003658}[]{#_Toc141005247}[]{#_Toc141591304}[]{#_Toc141003659}[]{#_Toc141005248}[]{#_Toc141591305}[]{#_Toc141003660}[]{#_Toc141005249}[]{#_Toc141591306}[]{#_Toc141003661}[]{#_Toc141005250}[]{#_Toc141591307}[]{#_Toc141003662}[]{#_Toc141005251}[]{#_Toc141591308}[]{#_Toc141003663}[]{#_Toc141005252}[]{#_Toc141591309}[]{#_Toc141003664}[]{#_Toc141005253}[]{#_Toc141591310}[]{#_Toc141003665}[]{#_Toc141005254}[]{#_Toc141591311}[]{#_Toc141003666}[]{#_Toc141005255}[]{#_Toc141591312}[]{#_Toc141003667}[]{#_Toc141005256}[]{#_Toc141591313}[]{#_Toc141003668}[]{#_Toc141005257}[]{#_Toc141591314}[]{#_Toc141003669}[]{#_Toc141005258}[]{#_Toc141591315}[]{#_Toc141003670}[]{#_Toc141005259}[]{#_Toc141591316}[]{#_Toc141003671}[]{#_Toc141005260}[]{#_Toc141591317}[]{#_Toc141003672}[]{#_Toc141005261}[]{#_Toc141591318}[]{#_Toc141003674}[]{#_Toc141005263}[]{#_Toc141591320}[]{#_Toc141003683}[]{#_Toc141005272}[]{#_Toc141591329}[]{#_Toc141003684}[]{#_Toc141005273}[]{#_Toc141591330}[]{#_Toc141003685}[]{#_Toc141005274}[]{#_Toc141591331}[]{#_Toc141003686}[]{#_Toc141005275}[]{#_Toc141591332}[]{#_Toc141003687}[]{#_Toc141005276}[]{#_Toc141591333}[]{#_Toc141003688}[]{#_Toc141005277}[]{#_Toc141591334}[]{#_Toc141003689}[]{#_Toc141005278}[]{#_Toc141591335}[]{#_Toc141003690}[]{#_Toc141005279}[]{#_Toc141591336}[]{#_Toc141003691}[]{#_Toc141005280}[]{#_Toc141591337}[]{#_Toc141003692}[]{#_Toc141005281}[]{#_Toc141591338}[]{#_Toc141003693}[]{#_Toc141005282}[]{#_Toc141591339}[]{#_Toc141003697}[]{#_Toc141005286}[]{#_Toc141591343}[]{#_Toc404782466}

**登录设备 \-- 登录设备命令 \-- free line**

------------------------------------------------------------------------

[**[free line]{lang="EN-US"}**]{#struct_0_18173_18228_1849505866}[命令用来释放指定用户线上建立的连接。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x791419556}

[**[free line]{lang="EN-US"}***[ ]{lang="EN-US"}*[{ *number1* \| { **aux** \| **console** \| **tty** \| **vty** } *number2* }]{lang="EN-US"}]{#struct_0_18173_18228_x2041801458}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_384910052}

[[用户视图]{style="font-family:宋体"}]{#struct_0_18173_18228_x1529398473}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1566833453}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x127752677}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_550365872}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1585661823}

[*[number1]{lang="EN-US"}*]{#struct_0_18173_18228_1849356914}[：用户线的编号（绝对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准，一般从]{style="font-family:宋体"}[0]{lang="EN-US"}[开始。]{style="font-family:宋体"}

[**[aux]{lang="EN-US"}**]{#struct_0_18173_18228_x2041801459}[：]{style="font-family:宋体"}[AUX]{lang="EN-US"}[用户线。]{style="font-family:宋体"}

[**[console]{lang="EN-US"}**]{#struct_0_18173_18228_1950993993}[：]{style="font-family:宋体"}[Console]{lang="EN-US"}[用户线。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[tty]{lang="EN-US"}**]{#struct_0_18173_18228_1711523362}[：]{style="font-family:宋体"}[TTY]{lang="EN-US"}[用户线。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vty]{lang="EN-US"}**]{#struct_0_18173_18228_x652958034}[：]{style="font-family:宋体"}[VTY]{lang="EN-US"}[用户线。]{style="font-family:宋体"}

[*[number2]{lang="EN-US"}*]{#struct_0_18173_18228_396531654}[：用户线的编号（相对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_2128217735}

[[用户不能使用该命令释放自己的连接。]{style="font-family:宋体"}]{#struct_0_18173_18228_x1179536767}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_309507677}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x2041801460}[释放用户线上]{style="font-family:宋体"}[VTY 1]{lang="EN-US"}[建立的连接。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[查看当前有哪些用户正在操作设备。]{style="font-family:宋体"}]{#struct_0_18173_18228_28876300}

[[\<Sysname\> display users]{lang="EN-US"}]{#struct_0_18173_18228_x1086167210}

[  Idx  Line     Idle       Time              Pid     Type]{lang="EN-US"}

[  10   VTY 0    00:10:49   Jun 11 11:27:32   320     TEL]{lang="EN-US"}

[+ 11   VTY 1    00:00:00   Jun 11 11:39:40   334     TEL]{lang="EN-US"}

[ ]{lang="EN-US"}

[Following are more details.]{lang="EN-US"}

[VTY 0   :]{lang="EN-US"}

[        Location: 192.168.1.12]{lang="EN-US"}

[VTY 1   :]{lang="EN-US"}

[        Location: 192.168.1.26]{lang="EN-US"}

[ +    : Current operation user.]{lang="EN-US"}

[ F    : Current operation user works in async mode.]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[假设]{style="font-family:宋体"}]{#struct_0_18173_18228_x998002999}[VTY 1]{lang="EN-US"}[用户的操作影响到网络管理员当前的操作，将他强制下线。]{style="font-family:宋体"}

[[\<Sysname\> free line vty 1]{lang="EN-US"}]{#struct_0_18173_18228_x884327422}

[Are you sure to free line vty1? \[Y/N\]:y]{lang="EN-US"}

[ \[OK\]]{lang="EN-US"}
:::

::: {#1444903476 .myid}
[]{#_Toc404782467}[]{#struct_0_18173_18228_296850709}

**登录设备 \-- 登录设备命令 \-- free user-interface**

------------------------------------------------------------------------

[**[free user-interface]{lang="EN-US"}**]{#struct_0_18173_18228_x2074839134}[命令用来释放指定用户线上建立的连接。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1326227578}

[**[free user-interface]{lang="EN-US"}***[ ]{lang="EN-US"}*[{ *number1* \| { **aux** \| **console** \| **tty** \| **vty** } *number2* }]{lang="EN-US"}]{#struct_0_18173_18228_x1280302777}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_532970533}

[[用户视图]{style="font-family:宋体"}]{#struct_0_18173_18228_x551041611}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_1675066634}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_1156575403}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_781704551}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_296850708}

[*[number1]{lang="EN-US"}*]{#struct_0_18173_18228_x2074839133}[：用户线的编号（绝对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准，一般从]{style="font-family:宋体"}[0]{lang="EN-US"}[开始。]{style="font-family:宋体"}

[**[aux]{lang="EN-US"}**]{#struct_0_18173_18228_x566712691}[：]{style="font-family:宋体"}[AUX]{lang="EN-US"}[用户线。]{style="font-family:宋体"}

[**[console]{lang="EN-US"}**]{#struct_0_18173_18228_1219037859}[：]{style="font-family:宋体"}[Console]{lang="EN-US"}[用户线。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[tty]{lang="EN-US"}**]{#struct_0_18173_18228_x1528661565}[：]{style="font-family:宋体"}[TTY]{lang="EN-US"}[用户线。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vty]{lang="EN-US"}**]{#struct_0_18173_18228_x394250394}[：]{style="font-family:宋体"}[VTY]{lang="EN-US"}[用户线。]{style="font-family:宋体"}

[*[number2]{lang="EN-US"}*]{#struct_0_18173_18228_1159669114}[：用户线的编号（相对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_1749112075}

[[用户不能使用该命令释放自己的连接。]{style="font-family:宋体"}]{#struct_0_18173_18228_x731620731}

[[该命令实现与]{style="font-family:宋体"}**[free line]{lang="EN-US"}**]{#struct_0_18173_18228_296850707}[一致，仅为与旧版本兼容保留，请使用]{style="font-family:宋体"}**[free line]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x2074839124}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x1326162042}[释放用户线上]{style="font-family:宋体"}[VTY 1]{lang="EN-US"}[建立的连接。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[查看当前有哪些用户正在操作设备。]{style="font-family:宋体"}]{#struct_0_18173_18228_x1934246662}

[[\<Sysname\> display users]{lang="EN-US"}]{#struct_0_18173_18228_x701904590}

[  Idx  LINE     Idle       Time              Pid     Type]{lang="EN-US"}

[  10   VTY 0    00:10:49   Jun 11 11:27:32   320     TEL]{lang="EN-US"}

[+ 11   VTY 1    00:00:00   Jun 11 11:39:40   334     TEL]{lang="EN-US"}

[ ]{lang="EN-US"}

[Following are more details.]{lang="EN-US"}

[VTY 0   :]{lang="EN-US"}

[        Location: 192.168.1.12]{lang="EN-US"}

[VTY 1   :]{lang="EN-US"}

[        Location: 192.168.1.26]{lang="EN-US"}

[ +    : Current operation user.]{lang="EN-US"}

[ F    : Current operation user works in async mode.]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[假设]{style="font-family:宋体"}]{#struct_0_18173_18228_296850706}[VTY 1]{lang="EN-US"}[用户的操作影响到网络管理员当前的操作，将他强制下线。]{style="font-family:宋体"}

[[\<Sysname\> free user-interface vty 1]{lang="EN-US"}]{#struct_0_18173_18228_x2074839123}

[Are you sure to free line vty1? \[Y/N\]:y]{lang="EN-US"}

[ \[OK\]]{lang="EN-US"}
:::

::::: {#314430370 .myid}
[]{#_Toc404782468}[]{#struct_0_18173_18228_x566647155}[]{#_Toc319416212}[]{#_Toc297293890}[]{#_Toc301508037}[]{#_Toc301508038}[]{#_Toc301508039}[]{#_Toc301508040}[]{#_Toc301508041}[]{#_Toc301508042}[]{#_Toc301508043}[]{#_Toc301508044}[]{#_Toc301508045}[]{#_Toc301508047}[]{#_Toc301508048}[]{#_Toc301508049}[]{#_Toc301508050}[]{#_Toc301508051}[]{#_Toc301508052}[]{#_Toc301508053}[]{#_Toc301508071}

**登录设备 \-- 登录设备命令 \-- free web users**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](登录设备命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_18173_18228_x1109372473}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_18173_18228_x1217103751}
:::

[ ]{lang="EN-US"}

[**[free web users]{lang="EN-US"}**]{#struct_0_18173_18228_420690128}[命令用来强制在线]{style="font-family:宋体"}[Web]{lang="EN-US"}[用户下线。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1071742415}

[**[free web users]{lang="EN-US"}**[ { **all** \| **user-id** *user-id* \| **user-name** *user-name* }]{lang="EN-US"}]{#struct_0_18173_18228_x652314214}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_296850705}

[[用户视图]{style="font-family:宋体"}]{#struct_0_18173_18228_x2074839122}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_x2132731096}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_384605841}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_1306255403}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_1431661363}

[**[all]{lang="EN-US"}**]{#struct_0_18173_18228_588881976}[：所有]{style="font-family:宋体"}[Web]{lang="EN-US"}[用户。]{style="font-family:宋体"}

[*[user-id]{lang="EN-US"}*]{#struct_0_18173_18228_x1114688313}[：]{style="font-family:宋体"}[Web]{lang="EN-US"}[用户的]{style="font-family:宋体"}[ID]{lang="EN-US"}[号，为]{style="font-family:宋体"}[15]{lang="EN-US"}[位十六进制数。系统会自动为每位成功登录的]{style="font-family:宋体"}[Web]{lang="EN-US"}[用户分配一个用户]{style="font-family:宋体"}[ID]{lang="EN-US"}[，用户]{style="font-family:宋体"}[ID]{lang="EN-US"}[用于唯一标识]{style="font-family:宋体"}[Web]{lang="EN-US"}[用户。]{style="font-family:宋体"}

[**[user-name]{lang="EN-US"}**[ *user-name*]{lang="EN-US"}]{#struct_0_18173_18228_296850704}[：]{style="font-family:宋体"}[Web]{lang="EN-US"}[用户的用户名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_x2074839121}

[[管理员在管理需要时，可以使用该命令强制下线部分或全部的]{style="font-family:宋体"}]{#struct_0_18173_18228_x1729446569}[Web]{lang="EN-US"}[用户。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_525518641}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x1373480883}[强制所有在线]{style="font-family:宋体"}[Web]{lang="EN-US"}[用户下线。]{style="font-family:宋体"}

[[\<Sysname\> free web users all]{lang="EN-US"}]{#struct_0_18173_18228_x178677575}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x869316151}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display web users]{lang="EN-US"}**]{#struct_0_18173_18228_x1850352502}
:::::

::: {#1825817370 .myid}
[]{#_Toc404782469}[]{#struct_0_18173_18228_x804514434}[]{#_Toc297210645}[]{#_Toc296689415}[]{#_Toc296419366}

**登录设备 \-- 登录设备命令 \-- history-command max-size**

------------------------------------------------------------------------

[**[history-command max-size]{lang="EN-US"}**]{#struct_0_18173_18228_296850703}[命令用来设置可以存储的当前用户线下历史命令的条数。]{style="font-family:
宋体"}

[**[undo history-command max-size]{lang="EN-US"}**]{#struct_0_18173_18228_x2074839128}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_1355667146}

[**[history-command max-size ]{lang="EN-US"}***[size-value]{lang="EN-US"}*]{#struct_0_18173_18228_1199371406}

[**[undo history-command max-size]{lang="EN-US"}**]{#struct_0_18173_18228_1783751733}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1112937560}

[[历史命令缓冲区可存储]{style="font-family:宋体"}[10]{lang="EN-US"}]{#struct_0_18173_18228_x840714922}[条历史命令。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_x2124464377}

[[用户线视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18173_18228_x2114328734}[用户线类视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_296850702}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x2074839127}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_1402721313}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_587503653}

[*[size-value]{lang="EN-US"}*]{#struct_0_18173_18228_x653008986}[：可存储的历史命令的条数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_1600493172}

[[每个用户线对应一个历史命令缓冲区，缓冲区里保存了当前用户最近执行成功的命令，缓冲区的容量决定了可以保存的历史命令的数目。用户使用]{style="font-family:宋体"}**[display history-command]{lang="EN-US"}**]{#struct_0_18173_18228_x1381257527}[命令、上光标键↑或下光标键↓可以随时了解近期成功执行了哪些操作（]{style="font-family:宋体"}**[display history-command]{lang="EN-US"}**[命令的详细介绍请参见"基础配置命令参考"中的"]{style="font-family:宋体"}[CLI]{lang="EN-US"}["）。同时登录设备的不同用户拥有不同的历史命令缓冲区，互不影响。]{style="font-family:宋体"}

[[用户退出当前会话时，系统会自动清除相应历史命令缓冲区内保存的历史命令。]{style="font-family:宋体"}]{#struct_0_18173_18228_639051986}

[[如果用户线视图下配置]{style="font-family:宋体"}**[history-command max-size]{lang="EN-US"}**]{#struct_0_18173_18228_296850701}[为缺省值，并且此时用户线类视图下配置了]{style="font-family:宋体"}**[history-command max-size]{lang="EN-US"}**[，那么用户线视图下的生效配置值为用户线类视图下的配置；如果用户线类视图下未配置，则生效的为缺省值。]{style="font-family:宋体"}

[[需要注意的是，在用户线视图下使用本命令配置的当前用户线下可存储的历史命令条数立即生效；用户线类视图下配置的可存储的历史命令条数将在下次登录时生效。]{style="font-family:宋体"}]{#struct_0_18173_18228_x1965241700}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x2074839126}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x163362628}[设置]{style="font-family:宋体"}[Console]{lang="EN-US"}[用户线下历史命令缓冲区最多可以存储]{style="font-family:宋体"}[20]{lang="EN-US"}[条历史命令。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_989858331}

[\[Sysname\] line console 0]{lang="EN-US"}

[\[Sysname-line-console0\] history-command max-size 20]{lang="EN-US"}
:::

::: {#-1526888109 .myid}
[]{#_Toc100291521}[]{#_Toc404782470}[]{#struct_0_18173_18228_x1000269726}[]{#_Toc297210646}[]{#_Toc296689416}[]{#_Toc15375231}

**登录设备 \-- 登录设备命令 \-- idle-timeout**

------------------------------------------------------------------------

[**[idle-timeout]{lang="EN-US"}**]{#struct_0_18173_18228_1084944896}[命令用来设置用户连接的超时时间。]{style="font-family:宋体"}

[**[undo idle-timeout]{lang="EN-US"}**]{#struct_0_18173_18228_x963426112}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_1099226341}

[**[idle-timeout ]{lang="EN-US"}***[minutes ]{lang="EN-US"}*[\[ *seconds* \]]{lang="EN-US"}]{#struct_0_18173_18228_296850700}

[**[undo idle-timeout]{lang="EN-US"}**]{#struct_0_18173_18228_x2074839125}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_239921899}

[[超时时间为]{style="font-family:宋体"}[10]{lang="EN-US"}]{#struct_0_18173_18228_x320166117}[分钟。]{style="font-family:宋体"}

[[【视图】]{style="font-family:
黑体"}]{#struct_0_18173_18228_71584}

[[用户线视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18173_18228_1010192460}[用户线类视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1188291630}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_434701901}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1659464427}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1051228284}

[*[minutes]{lang="EN-US"}*]{#struct_0_18173_18228_1975595079}[：指定超时时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[35791]{lang="EN-US"}[，单位为分钟。]{style="font-family:宋体"}

[*[seconds]{lang="EN-US"}*]{#struct_0_18173_18228_1132237360}[：指定超时时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[59]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_x638535794}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户登录后，如果在超时时间内设备和用户间没有消息交互，则超时时间到达时设备会自动断开用户连接。]{style="font-family:宋体"}]{#struct_0_18173_18228_1884068723}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当超时时间设置为]{style="font-family:宋体"}]{#struct_0_18173_18228_1098764956}[0]{lang="EN-US"}[时，表示设备不会因为超时自动断开用户连接。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果用户线视图下配置]{style="font-family:宋体"}]{#struct_0_18173_18228_x1990251843}**[idle-timeout]{lang="EN-US"}**[为缺省值，并且此时用户线类视图下配置了]{style="font-family:宋体"}**[idle-timeout]{lang="EN-US"}**[，那么用户线视图下的生效配置值为用户线类视图下的配置；如果用户线类视图下未配置，则生效的为缺省值。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户线视图下使用本命令配置的连接超时时间立即生效；用户线类视图下配置的连接超时时间将在下次登录时生效。]{style="font-family:宋体"}]{#struct_0_18173_18228_1879386902}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x361892010}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x1659464428}[设置]{style="font-family:宋体"}[Console]{lang="EN-US"}[用户线下用户连接超时时间为]{style="font-family:宋体"}[1]{lang="EN-US"}[分钟]{style="font-family:宋体"}[30]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_x291713397}

[\[Sysname\] line console 0]{lang="EN-US"}

[\[Sysname-line-console0\] idle-timeout 1 30]{lang="EN-US"}
:::

::: {#-1764206188 .myid}
[]{#_Toc404782471}[]{#struct_0_18173_18228_x1718386519}[]{#_Toc361076170}

**登录设备 \-- 登录设备命令 \-- ip alias**

------------------------------------------------------------------------

[**[ip alias]{lang="EN-US"}**]{#struct_0_18173_18228_2102242666}[命令用来建立]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[重定向监听端口与]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的对应关系。]{style="font-family:宋体"}

[**[undo ip alias]{lang="EN-US"}**]{#struct_0_18173_18228_x2041631253}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1666114908}

[**[ip alias ]{lang="EN-US"}**]{#struct_0_18173_18228_x1576482436}*[ip-address port-number]{lang="EN-US"}*

[**[undo ip alias ]{lang="EN-US"}**]{#struct_0_18173_18228_x1718452055}*[ip-address]{lang="EN-US"}*

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_x987640962}

[[Telnet]{lang="EN-US"}]{#struct_0_18173_18228_x1229175506}[重定向监听端口与]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址没有对应关系。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_x963047218}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18173_18228_x1718255447}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1200299452}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_1150841034}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1718320983}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1096650954}

[*[ip-address]{lang="EN-US"}*]{#struct_0_18173_18228_x1105608721}[：与]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[重定向监听端口对应的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。该地址不能为设备上接口的地址，但可以和接口地址同一网段。]{style="font-family:宋体"}

[*[port-number]{lang="EN-US"}*]{#struct_0_18173_18228_x799073363}[：]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[重定向的监听端口，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[50000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1718124375}

[[用户和设备]{style="font-family:宋体"}[A]{lang="EN-US"}]{#struct_0_18173_18228_x1727363590}[相连，能够]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[登录到设备]{style="font-family:宋体"}[A]{lang="EN-US"}[，设备]{style="font-family:宋体"}[A]{lang="EN-US"}[通过]{style="font-family:宋体"}[AUX]{lang="EN-US"}[口]{style="font-family:宋体"}[/]{lang="EN-US"}[异步串口和设备]{style="font-family:
宋体"}[B]{lang="EN-US"}[相连。在设备]{style="font-family:宋体"}[A]{lang="EN-US"}[上配置]{style="font-family:宋体"}**[redirect enable]{lang="EN-US"}**[和]{style="font-family:宋体"}**[redirect listen-port ]{lang="EN-US"}***[port-number]{lang="EN-US"}*[后，用户就可以使用"]{style="font-family:宋体"}[telnet ]{lang="EN-US"}[设备]{style="font-family:宋体"}[A]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"} *[port-number]{lang="EN-US"}*["来登录设备]{style="font-family:宋体"}[B]{lang="EN-US"}[，相当于用户直接]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[登录设备]{style="font-family:宋体"}[B]{lang="EN-US"}[。如果再使用]{style="font-family:宋体"}**[ip alias ]{lang="EN-US"}***[ip-address port-number]{lang="EN-US"}*[建立]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[重定向监听端口与]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的对应关系后，用户就可以直接执行"]{style="font-family:宋体"}**[telnet]{lang="EN-US"}**[ ]{lang="EN-US"}*[ip-address]{lang="EN-US"}*["来登录设备]{style="font-family:宋体"}[B]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_790019442}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_1319427251}[配置]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[重定向监听端口]{style="font-family:宋体"}[2000]{lang="EN-US"}[对应的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_x1718189911}

[\[Sysname\] ip alias 1.1.1.1 2000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1616050018}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[redirect enable]{lang="EN-US"}**]{#struct_0_18173_18228_x1383519466}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[redirect listen-port]{lang="EN-US"}**]{#struct_0_18173_18228_x1717993303}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display tcp]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18173_18228_1988187282}[（请参考三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}[业务）]{lang="EN-US" style="font-family:宋体"}
:::

::::: {#-664306067 .myid}
[]{#_Toc404782472}[]{#struct_0_18173_18228_x1895839616}[]{#_Toc319416215}[]{#_Toc297293893}

**登录设备 \-- 登录设备命令 \-- ip http acl**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](登录设备命令.files/image001.png){#图片 2 width="62" height="25"}]{lang="EN-US"}]{#struct_0_18173_18228_857474349}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_18173_18228_x844053728}
:::

[ ]{lang="EN-US"}

[**[ip http acl]{lang="EN-US"}**]{#struct_0_18173_18228_x88761391}[命令用来配置]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[服务与]{style="font-family:宋体"}[ACL]{lang="EN-US"}[关联。]{style="font-family:宋体"}

[**[undo ip http acl]{lang="EN-US"}**]{#struct_0_18173_18228_558682256}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x36406323}

[**[ip http acl ]{lang="EN-US"}**[{ *acl-number* \| **name** *acl-name* }]{lang="EN-US"}]{#struct_0_18173_18228_x1659464429}

[**[undo ip http acl]{lang="EN-US"}**]{#struct_0_18173_18228_x1857797338}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_x872097737}

[[HTTP]{lang="EN-US"}]{#struct_0_18173_18228_x880785245}[服务没有与任何]{style="font-family:宋体"}[ACL]{lang="EN-US"}[关联。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1396077552}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18173_18228_x1378832850}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_1209555398}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_290286167}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1659464430}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_x647878221}

[*[acl-number]{lang="EN-US"}*]{#struct_0_18173_18228_33928875}[：]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[（基本]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}[）。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}***[ acl]{lang="EN-US"}*[-name]{lang="EN-US"}]{#struct_0_18173_18228_x431151390}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称。]{style="font-family:宋体"}*[acl-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写，必须以英文字母]{style="font-family:宋体"}[a\~z]{lang="EN-US"}[或]{style="font-family:宋体"}[A\~Z]{lang="EN-US"}[开头。为避免混淆，]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称不允许使用英文单词]{style="font-family:宋体"}[all]{lang="EN-US"}[。仅当指定名称的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[存在且为基本]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}[时生效。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1120223935}

[[FIPS]{lang="EN-US"}]{#struct_0_18173_18228_235354234}[模式下，不支持本命令。]{style="font-family:宋体"}

[[配置]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_18173_18228_1309814657}[服务与]{style="font-family:宋体"}[ACL]{lang="EN-US"}[关联后，只有]{style="font-family:宋体"}[ACL]{lang="EN-US"}[允许通过的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端能够通过]{style="font-family:宋体"}[Web]{lang="EN-US"}[方式登录设备。不匹配]{style="font-family:宋体"}[ACL]{lang="EN-US"}[或]{style="font-family:宋体"}[ACL]{lang="EN-US"}[拒绝通过的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端将不能通过]{style="font-family:宋体"}[Web]{lang="EN-US"}[方式登录设备。]{style="font-family:宋体"}

[[多次执行该命令最新配置生效。]{style="font-family:宋体"}]{#struct_0_18173_18228_x1071057583}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1915157634}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_489969142}[配置]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[服务与]{style="font-family:宋体"}[ACL 2001]{lang="EN-US"}[关联，只允许]{style="font-family:宋体"}[10.10.0.0/16]{lang="EN-US"}[网段的客户端通过]{style="font-family:宋体"}[Web]{lang="EN-US"}[访问设备。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_x1659464431}

[\[Sysname\] acl basic 2001]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2001\] rule permit source 10.10.0.0 0.0.255.255]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2001\] quit]{lang="EN-US"}

[\[Sysname\] ip http acl 2001]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_2081005134}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[acl]{lang="EN-US"}**]{#struct_0_18173_18228_1213903355}[（]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[QoS]{lang="EN-US"}[命令参考]{lang="EN-US" style="font-family:宋体"}[/ACL]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}
:::::

::::: {#232647239 .myid}
[]{#_Toc404782473}[]{#struct_0_18173_18228_x649943502}[]{#_Toc319416216}[]{#_Toc297293894}

**登录设备 \-- 登录设备命令 \-- ip http enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](登录设备命令.files/image001.png){#图片 3 width="62" height="25"}]{lang="EN-US"}]{#struct_0_18173_18228_x881353449}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_18173_18228_x207040526}
:::

[ ]{lang="EN-US"}

[**[ip http enable]{lang="EN-US"}**]{#struct_0_18173_18228_2082009216}[命令用来使能]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[服务。]{style="font-family:宋体"}

[**[undo ip http enable]{lang="EN-US"}**]{#struct_0_18173_18228_x1659464432}[命令用来关闭]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[服务。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1810677635}

[**[ip http enable]{lang="EN-US"}**]{#struct_0_18173_18228_x1155022547}

[**[undo ip http enable]{lang="EN-US"}**]{#struct_0_18173_18228_x851857944}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_x24067380}

[[HTTP]{lang="EN-US"}]{#struct_0_18173_18228_x1221419787}[服务处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_404163513}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18173_18228_2028196299}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_x990233137}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1659464433}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_918205720}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_2031874763}

[[FIPS]{lang="EN-US"}]{#struct_0_18173_18228_493499692}[模式下，不支持本命令。]{style="font-family:宋体"}

[[使能]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_18173_18228_962205083}[服务后，用户才能通过]{style="font-family:宋体"}[Web]{lang="EN-US"}[使用]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[方式登录设备。]{style="font-family:宋体"}

[[使用]{style="font-family:宋体"}[Web]{lang="EN-US"}]{#struct_0_18173_18228_1785090410}[方式登录设备，用户输入的用户名和密码属于敏感信息，]{style="font-family:宋体"}[Web]{lang="EN-US"}[登录请求采用]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[方式发送到]{style="font-family:宋体"}[Web]{lang="EN-US"}[服务器。所以，即使用户希望使用]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[方式访问]{style="font-family:宋体"}[Web]{lang="EN-US"}[，也必须先开启设备的]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[服务才能成功的登录。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x828999822}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_1412373294}[使能]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[服务。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_x1659464434}

[\[Sysname\] ip http enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_1036404062}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip https enable]{lang="EN-US"}**]{#struct_0_18173_18228_x1046199767}
:::::

::::: {#-1586503978 .myid}
[]{#_Toc263186435}[]{#_Toc139341904}[]{#_Toc100291525}[]{#_Toc15375252}[]{#_Toc536418349}[]{#_Toc404782474}[]{#struct_0_18173_18228_1677720607}[]{#_Toc319416214}[]{#_Toc297293892}[]{#_Hlt13304852}[]{#_Hlt13304871}[]{#_Hlt13304903}[]{#_Hlt13304908}

**登录设备 \-- 登录设备命令 \-- ip http port**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](登录设备命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_18173_18228_x72469339}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_18173_18228_634806131}
:::

[ ]{lang="EN-US"}

[**[ip http port]{lang="EN-US"}**]{#struct_0_18173_18228_330210029}[命令用来配置]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[服务的端口号。]{style="font-family:宋体"}

[**[undo ip http port]{lang="EN-US"}**]{#struct_0_18173_18228_x250995902}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_81439719}

[**[ip http ]{lang="EN-US"}**]{#struct_0_18173_18228_x1606440572}**[port ]{lang="FR"}***[port-number]{lang="FR"}*

[**[undo ip http ]{lang="EN-US"}**]{#struct_0_18173_18228_x2817616}**[port]{lang="FR"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1659464435}

[[HTTP]{lang="EN-US"}]{#struct_0_18173_18228_111636666}[服务的端口号为]{style="font-family:宋体"}[80]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_x640553348}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18173_18228_1990171799}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_2060379116}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x991488406}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1016037043}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1583867029}

[*[port-number]{lang="EN-US"}*]{#struct_0_18173_18228_x1659464436}[：]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[服务的端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_514921193}

[[FIPS]{lang="EN-US"}]{#struct_0_18173_18228_x1515149396}[模式下，不支持本命令。]{style="font-family:宋体"}

[[如果修改端口号前]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_18173_18228_918218988}[服务是开启的，则修改端口号后系统会自动重启]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[服务，正在访问的用户将被断开，用户需要在浏览器的地址栏中重新输入新的地址后才可以继续访问。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1405328090}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x483742742}[配置]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[服务的端口号为]{style="font-family:宋体"}[80]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_x335520813}

[\[Sysname\] ip http port 80]{lang="EN-US"}
:::::

::::: {#-1168760613 .myid}
[]{#_Toc404782475}[]{#struct_0_18173_18228_x90512779}[]{#_Toc319416220}[]{#_Toc297293898}[]{#_Toc290553364}

**登录设备 \-- 登录设备命令 \-- ip https acl**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](登录设备命令.files/image001.png){#图片 6 width="62" height="25"}]{lang="EN-US"}]{#struct_0_18173_18228_x850160363}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_18173_18228_x1660161536}
:::

[ ]{lang="EN-US"}

[**[ip https acl]{lang="EN-US"}**]{#struct_0_18173_18228_1063391647}[命令用来配置]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[服务与]{style="font-family:宋体"}[ACL]{lang="EN-US"}[关联。]{style="font-family:宋体"}

[**[undo ip https ac]{lang="EN-US"}[l]{lang="EN-US"}**]{#struct_0_18173_18228_x1543780218}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x2063899893}

[**[ip https acl ]{lang="EN-US"}**[{]{lang="EN-US"}*[acl-number ]{lang="EN-US"}*[\| **name** *acl-name* }]{lang="EN-US"}]{#struct_0_18173_18228_1763451799}

[**[undo ip https acl]{lang="EN-US"}**]{#struct_0_18173_18228_x219559957}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_x391773504}

[[HTTPS]{lang="EN-US"}]{#struct_0_18173_18228_1042401399}[服务没有与任何]{style="font-family:宋体"}[ACL]{lang="EN-US"}[关联。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_x850160364}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18173_18228_x1660489216}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_1803097440}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_1386840511}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_1276671593}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_940425265}

[*[acl-number]{lang="EN-US"}*]{#struct_0_18173_18228_x1068148607}[：]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[（基本]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}[）。]{style="font-family:宋体"}

[**[name ]{lang="EN-US"}***[acl]{lang="EN-US"}*[-name]{lang="EN-US"}]{#struct_0_18173_18228_1134998087}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称。]{style="font-family:宋体"}*[acl-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写，必须以英文字母]{style="font-family:宋体"}[a\~z]{lang="EN-US"}[或]{style="font-family:宋体"}[A\~Z]{lang="EN-US"}[开头。为避免混淆，]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称不允许使用英文单词]{style="font-family:宋体"}[all]{lang="EN-US"}[。仅当指定名称的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[存在且为基本]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}[时生效。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1109814931}

[[配置]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}]{#struct_0_18173_18228_480399814}[服务与]{style="font-family:宋体"}[ACL]{lang="EN-US"}[关联后，只有]{style="font-family:宋体"}[ACL]{lang="EN-US"}[允许通过的]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[客户端能够通过]{style="font-family:宋体"}[Web]{lang="EN-US"}[方式登录设备。不匹配]{style="font-family:宋体"}[ACL]{lang="EN-US"}[或]{style="font-family:宋体"}[ACL]{lang="EN-US"}[拒绝通过的]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[客户端将不能通过]{style="font-family:宋体"}[Web]{lang="EN-US"}[方式登录设备。]{style="font-family:宋体"}

[[需要注意的是，]{style="font-family:宋体"}[Web]{lang="EN-US"}]{#struct_0_18173_18228_1538282614}[登录时用户输入的用户名和密码属于敏感信息，]{style="font-family:宋体"}[Web]{lang="EN-US"}[登录请求采用]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[方式发送到]{style="font-family:宋体"}[Web]{lang="EN-US"}[服务器。所以，如果本命令中的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则拒绝客户端通过]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[服务访问]{style="font-family:宋体"}[Web]{lang="EN-US"}[页面，那么该客户端也无法通过]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[服务访问]{style="font-family:宋体"}[Web]{lang="EN-US"}[页面。]{style="font-family:宋体"}

[[多次执行该命令最新配置生效。]{style="font-family:宋体"}]{#struct_0_18173_18228_x850160365}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1660554752}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x2056002842}[配置]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[服务与]{style="font-family:宋体"}[ACL 2001]{lang="EN-US"}[关联，只允许]{style="font-family:宋体"}[10.10.0.0/16]{lang="EN-US"}[网段的客户端通过]{style="font-family:宋体"}[Web]{lang="EN-US"}[访问设备。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_1580673602}

[\[Sysname\] acl basic 2001]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2001\] rule permit source 10.10.0.0 0.0.255.255]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2001\] quit]{lang="EN-US"}

[\[Sysname\] ip https acl 2001]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_1939079828}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[acl]{lang="EN-US"}**]{#struct_0_18173_18228_2103264602}[（]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[QoS]{lang="EN-US"}[命令参考]{lang="EN-US" style="font-family:宋体"}[/ACL]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}
:::::

::::: {#327278671 .myid}
[]{#_Toc404782476}[]{#struct_0_18173_18228_x1294669421}[]{#_Toc319416218}[]{#_Toc297293896}[]{#_Toc297792890}[]{#_Toc297792891}

**登录设备 \-- 登录设备命令 \-- ip https certificate access-control-policy**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](登录设备命令.files/image001.png){#图片 4 width="62" height="25"}]{lang="EN-US"}]{#struct_0_18173_18228_x850160366}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_18173_18228_x1660358144}
:::

[ ]{lang="EN-US"}

[**[ip https certificate access-control-policy]{lang="EN-US"}**]{#struct_0_18173_18228_727043102}[命令用来配置]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[服务与证书属性访问控制策略关联。]{style="font-family:宋体"}

[**[undo ip https certificate access-control-policy]{lang="EN-US"}**]{#struct_0_18173_18228_1338222080}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1611399541}

[**[ip https certificate access-control-policy ]{lang="EN-US"}***[policy-name]{lang="EN-US"}*]{#struct_0_18173_18228_1016212909}

[**[undo ip https certificate access-control-policy]{lang="EN-US"}**]{#struct_0_18173_18228_1205869617}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_563756116}

[[HTTPS]{lang="EN-US"}]{#struct_0_18173_18228_872583142}[服务没有与任何证书属性访问控制策略关联。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_x850160367}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18173_18228_x1660423680}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_215830112}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_992125780}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_270982415}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_981461095}

[*[policy-name]{lang="EN-US"}*]{#struct_0_18173_18228_x1690819962}[：证书属性访问控制策略名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_x539565639}

[[通过将]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}]{#struct_0_18173_18228_x850160368}[服务与已配置的客户端证书属性访问控制策略关联，可以实现对客户端的访问权限进行控制。证书属性访问控制策略的相关介绍请参见"安全配置指导"中"]{style="font-family:宋体"}[PKI]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1660751360}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_1482095028}[设置]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[服务使用的证书属性访问控制策略为]{style="font-family:宋体"}[myacl]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_x1563181445}

[\[Sysname\] ip https certificate access-control-policy myacl]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_23040161}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pki certificate access-control-policy]{lang="EN-US"}**]{#struct_0_18173_18228_x1216611070}[（]{lang="EN-US" style="font-family:宋体"}[PKI]{lang="EN-US"}[命令参考]{lang="EN-US" style="font-family:宋体"}[/PKI]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}
:::::

::::: {#-1149159034 .myid}
[]{#_Toc404782477}[]{#struct_0_18173_18228_1833360454}[]{#_Toc319416221}[]{#_Toc297293899}

**登录设备 \-- 登录设备命令 \-- ip https enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](登录设备命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_18173_18228_x1518004933}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_18173_18228_x850160369}
:::

[ ]{lang="EN-US"}

[**[ip https enable]{lang="EN-US"}**]{#struct_0_18173_18228_x1660816896}[命令用来使能]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[服务。]{style="font-family:宋体"}

[**[undo ip https enable]{lang="EN-US"}**]{#struct_0_18173_18228_1633780713}[命令用来关闭]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[服务。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x880077640}

[**[ip https enable]{lang="EN-US"}**]{#struct_0_18173_18228_949395923}

[**[undo ip https enable]{lang="EN-US"}**]{#struct_0_18173_18228_619273770}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_x534991172}

[[HTTPS]{lang="EN-US"}]{#struct_0_18173_18228_104820313}[服务处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_x102051974}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18173_18228_x850160370}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1660227071}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1873427715}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1120197707}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1955551469}

[[只有使能该功能后，用户才能通过]{style="font-family:宋体"}[Web]{lang="EN-US"}]{#struct_0_18173_18228_x99610214}[方式使用]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[登录设备。]{style="font-family:宋体"}

[[需要注意的是，使能]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}]{#struct_0_18173_18228_1285766248}[服务，会触发]{style="font-family:宋体"}[SSL]{lang="EN-US"}[的握手协商过程。在]{style="font-family:宋体"}[SSL]{lang="EN-US"}[握手协商过程中，如果设备的本地证书已经存在，则]{style="font-family:宋体"}[SSL]{lang="EN-US"}[协商可以成功，]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[服务可以正常启动；如果设备的本地证书不存在，则]{style="font-family:宋体"}[SSL]{lang="EN-US"}[协商过程会触发证书申请流程。由于证书申请需要较长的时间，会导致]{style="font-family:宋体"}[SSL]{lang="EN-US"}[协商不成功，从而无法正常启动]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[服务。因此，在这种情况下，需要多次执行]{style="font-family:宋体"}**[ip https enable]{lang="EN-US"}**[命令，这样]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[服务才能正常启动。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_431972427}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_996918004}[使能]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[服务。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_x850160371}

[\[Sysname\] ip https enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1660292607}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip https ssl-server-policy]{lang="EN-US"}**]{#struct_0_18173_18228_590794620}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip https certificate access-control-policy]{lang="EN-US"}**]{#struct_0_18173_18228_2102524693}
:::::

::::: {#1792716644 .myid}
[]{#_Toc404782478}[]{#struct_0_18173_18228_1460333039}[]{#_Toc319416222}

**登录设备 \-- 登录设备命令 \-- ip https port**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](登录设备命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_18173_18228_x2086948413}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_18173_18228_x237816992}
:::

[ ]{lang="EN-US"}

[**[ip https port]{lang="EN-US"}**]{#struct_0_18173_18228_x53478936}[命令用来配置]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[服务的端口号。]{style="font-family:宋体"}

[**[undo ip https port]{lang="EN-US"}**]{#struct_0_18173_18228_x850160372}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1660095999}

[**[ip https ]{lang="EN-US"}**]{#struct_0_18173_18228_1703370115}**[port]{lang="FR"}**[ *port-number*]{lang="FR"}

[**[undo ip https ]{lang="EN-US"}**]{#struct_0_18173_18228_1807098891}**[port]{lang="FR"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_x848312135}

[[HTTPS]{lang="EN-US"}]{#struct_0_18173_18228_1968777146}[服务的端口号为]{style="font-family:宋体"}[443]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_260080556}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18173_18228_1356684545}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_1488491797}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1563563120}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_2146240755}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1334692080}

[*[port-number]{lang="EN-US"}*]{#struct_0_18173_18228_1447171201}[：]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[服务的端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1754285998}

[[如果修改端口号前]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}]{#struct_0_18173_18228_1932373234}[服务是开启的，则修改端口号后系统会自动重启]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[服务，正在访问的用户将被断开，用户需要在浏览器的地址栏中重新输入新的地址后才可以继续访问。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x154564132}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_528490493}[配置]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[服务的端口号为]{style="font-family:宋体"}[8080]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_1488491796}

[\[Sysname\] ip https port 8080]{lang="EN-US"}
:::::

::::: {#-683515403 .myid}
[]{#_Toc404782479}[]{#struct_0_18173_18228_x1563628656}[]{#_Toc319416219}[]{#_Toc297293897}

**登录设备 \-- 登录设备命令 \-- ip https ssl-server-policy**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](登录设备命令.files/image001.png){#图片 5 width="62" height="25"}]{lang="EN-US"}]{#struct_0_18173_18228_x2036276090}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_18173_18228_x2097357434}
:::

[ ]{lang="EN-US"}

[**[ip https ssl-server-policy]{lang="EN-US"}**]{#struct_0_18173_18228_x630407227}[命令用来配置]{style="font-family:
宋体"}[HTTPS]{lang="EN-US"}[服务与]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略关联。]{style="font-family:宋体"}

[**[undo ip https ssl-server-policy]{lang="EN-US"}**]{#struct_0_18173_18228_68715715}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1229279291}

[**[ip https ssl-server-policy ]{lang="EN-US"}***[policy-name]{lang="EN-US"}*]{#struct_0_18173_18228_1505050892}

[**[undo ip https ssl-server-policy]{lang="EN-US"}**]{#struct_0_18173_18228_1488491795}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1563694192}

[[HTTPS]{lang="EN-US"}]{#struct_0_18173_18228_449452764}[服务没有与任何]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略关联，]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[使用自签名证书。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1923368852}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18173_18228_x1158509751}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_1485809583}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x453622219}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_x588838508}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_1488491794}

[*[policy-name]{lang="EN-US"}*]{#struct_0_18173_18228_x1563759728}[：]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_x2035819380}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[关闭]{style="font-family:宋体"}]{#struct_0_18173_18228_x362754770}[HTTPS]{lang="EN-US"}[服务后，系统将自动取消]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[服务与]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略的关联。再次使能]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[服务之前，需要重新配置]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[服务与]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略关联。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HTTPS]{lang="EN-US"}]{#struct_0_18173_18228_654067044}[服务处于使能状态时，对与其关联的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略进行的修改不会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1487932462}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_1566032921}[设置]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[服务使用的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略为]{style="font-family:宋体"}[myssl]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_885669123}

[\[Sysname\] ip https ssl-server-policy myssl]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x831272512}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ssl server-policy]{lang="EN-US"}**]{#struct_0_18173_18228_x189543642}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/SSL]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}
:::::

::: {#-1502834408 .myid}
[]{#_Toc301187206}[]{#_Toc263186412}[]{#_Toc404782480}[]{#struct_0_18173_18228_1488491793}

**登录设备 \-- 登录设备命令 \-- line**

------------------------------------------------------------------------

[**[line]{lang="EN-US"}**]{#struct_0_18173_18228_x1563825264}[命令用来进入一个或多个用户线视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x657851572}

[**[line]{lang="EN-US"}**[ { *first-number1* \[ *last-number1* \] \| { **aux** \| **console** \| **tty** \| **vty** } *first-number2* \[ *last-number2* \] }]{lang="EN-US"}]{#struct_0_18173_18228_1488491792}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1563890800}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18173_18228_2135295001}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_1488491791}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1563956336}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_956136462}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_1488491790}

[*[first-number1]{lang="EN-US"}*]{#struct_0_18173_18228_x1564021872}[：第一个用户线的编号（绝对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准，一般从]{style="font-family:宋体"}[0]{lang="EN-US"}[开始。]{style="font-family:宋体"}

[*[last-number1]{lang="EN-US"}*]{#struct_0_18173_18228_x1267723651}[：最后一个用户线的编号（绝对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准，一般从]{style="font-family:宋体"}[0]{lang="EN-US"}[开始，但不能小于]{style="font-family:宋体"}*[first-number1]{lang="EN-US"}*[。]{style="font-family:宋体"}

[**[aux]{lang="EN-US"}**]{#struct_0_18173_18228_1488491789}[：]{style="font-family:宋体"}[AUX]{lang="EN-US"}[用户线。]{style="font-family:宋体"}

[**[console]{lang="EN-US"}**]{#struct_0_18173_18228_x1563432047}[：]{style="font-family:宋体"}[Console]{lang="EN-US"}[用户线。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[tty]{lang="EN-US"}**]{#struct_0_18173_18228_x1955170336}[：]{style="font-family:宋体"}[TTY]{lang="EN-US"}[用户线。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vty]{lang="EN-US"}**]{#struct_0_18173_18228_460956622}[：]{style="font-family:宋体"}[VTY]{lang="EN-US"}[用户线。]{style="font-family:宋体"}

[*[first-number2]{lang="EN-US"}*]{#struct_0_18173_18228_1488491788}[：第一个用户线的编号（相对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[last-number2]{lang="EN-US"}*]{#struct_0_18173_18228_x1563497583}[：最后一个用户线的编号（相对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准，但不能小于]{style="font-family:宋体"}*[first-number2]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1521643653}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[进入一个用户线视图进行配置后，该配置只对该用户视图有效。]{style="font-family:宋体"}]{#struct_0_18173_18228_x91974379}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[进入多个用户线视图进行配置后，该配置对这些用户视图均有效。]{style="font-family:宋体"}]{#struct_0_18173_18228_906392824}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1086665239}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x91974380}[进入]{style="font-family:宋体"}[Console 0]{lang="EN-US"}[用户线视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_861762799}

[\[Sysname\] line console 0]{lang="EN-US"}

[\[Sysname-line-console0\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x456551651}[进入]{style="font-family:宋体"}[VTY 0]{lang="EN-US"}[～]{style="font-family:宋体"}[4]{lang="EN-US"}[用户线视图。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_x91974381}

[\[Sysname\] line vty 0 4]{lang="EN-US"}

[\[Sysname-line-vty0-4\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_861762800}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[line class]{lang="EN-US"}**]{#struct_0_18173_18228_x2019900573}
:::

::: {#1997417724 .myid}
[]{#_Toc404782481}[]{#struct_0_18173_18228_x91974382}

**登录设备 \-- 登录设备命令 \-- line class**

------------------------------------------------------------------------

[**[line class]{lang="EN-US"}**]{#struct_0_18173_18228_861762801}[命令用来进入指定用户线类视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x2019900574}

[**[line class ]{lang="EN-US"}**[{ **aux** \| **console** \| **tty** \| **vty** }]{lang="EN-US"}]{#struct_0_18173_18228_x91974383}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_861762802}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18173_18228_x2019900575}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_x990160914}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x91974384}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_861762795}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_x456551647}

[**[aux]{lang="EN-US"}**]{#struct_0_18173_18228_x91974385}[：]{style="font-family:宋体"}[AUX]{lang="EN-US"}[用户线类。]{style="font-family:宋体"}

[**[console]{lang="EN-US"}**]{#struct_0_18173_18228_861762796}[：]{style="font-family:宋体"}[Console]{lang="EN-US"}[用户线类。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[tty]{lang="EN-US"}**]{#struct_0_18173_18228_x456551648}[：]{style="font-family:宋体"}[TTY]{lang="EN-US"}[用户线类。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vty]{lang="EN-US"}**]{#struct_0_18173_18228_x91974386}[：]{style="font-family:宋体"}[VTY]{lang="EN-US"}[用户线类。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_861762797}

[**[line class]{lang="EN-US"}**]{#struct_0_18173_18228_x456551649}[命令用来进入指定用户线类视图，]{style="font-family:宋体"}**[line]{lang="EN-US"}**[命令用来进入一个或多个用户线视图。对于同时支持这两种视图的命令：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户线视图下的配置优先于用户线类视图下的配置。]{style="font-family:宋体"}]{#struct_0_18173_18228_x1718386522}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户线视图下的配置只对该用户线生效。]{style="font-family:宋体"}]{#struct_0_18173_18228_179862829}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户线类视图下的配置修改不会立即生效，当用户下次登录后所修改的配置值才会生效。]{style="font-family:宋体"}]{#struct_0_18173_18228_x964840549}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户线视图下的属性配置为缺省值时，将采用用户线类视图下配置的值。如果用户线类视图下的属性配置也为缺省值时，则直接采用该属性的缺省值。]{style="font-family:宋体"}]{#struct_0_18173_18228_x1718452058}

[[用户]{style="font-family:宋体"}]{#struct_0_18173_18228_x863535660}[线类视图下支持的命令有：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[activation-key]{lang="EN-US"}**]{#struct_0_18173_18228_x91974388}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[auto-execute command]{lang="EN-US"}**]{#struct_0_18173_18228_861762807}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication-mode]{lang="EN-US"}**]{#struct_0_18173_18228_x2019900580}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[command accounting]{lang="EN-US"}**]{#struct_0_18173_18228_x2048289515}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[command authorization]{lang="EN-US"}**]{#struct_0_18173_18228_x767649821}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[escape-key]{lang="EN-US"}**]{#struct_0_18173_18228_x844631738}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[history-command max-size]{lang="EN-US"}**]{#struct_0_18173_18228_x2048289516}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[idle-timeout]{lang="EN-US"}**]{#struct_0_18173_18228_x1170934348}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[protocol inbound]{lang="EN-US"}**]{#struct_0_18173_18228_x1176383859}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[screen-length]{lang="EN-US"}**]{#struct_0_18173_18228_x2048289517}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[set authentication password]{lang="EN-US"}**]{#struct_0_18173_18228_395149593}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[shell]{lang="EN-US"}**]{#struct_0_18173_18228_949278217}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[terminal type]{lang="EN-US"}**]{#struct_0_18173_18228_155487525}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[user-role]{lang="EN-US"}**]{#struct_0_18173_18228_x2048289518}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x364365294}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x827627533}[将]{style="font-family:宋体"}[VTY]{lang="EN-US"}[用户线参数------用户连接的超时时间的缺省值设置为]{style="font-family:宋体"}[15]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_x2048289519}

[\[Sysname\] line class vty]{lang="EN-US"}

[\[Sysname-line-class-vty\] idle-timeout 15]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_1201718647}[在]{style="font-family:宋体"}[console]{lang="EN-US"}[用户线类视图下，将启动]{style="font-family:宋体"}[Console]{lang="EN-US"}[口终端会话的快捷键设置为]{style="font-family:宋体"}[\<s\>]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_x2048289520}

[\[Sysname\] line class console]{lang="EN-US"}

[\[Sysname-line-class-console\] activation-key s]{lang="EN-US"}

[\[Sysname-line-class-console\] quit]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{lang="EN-US" style="font-family:宋体"}[console]{lang="EN-US"}]{#struct_0_18173_18228_x8200470}[用户线视图下，将启动]{lang="EN-US" style="font-family:宋体"}[Console]{lang="EN-US"}[口终端会话的快捷键设置为缺省值]{lang="EN-US" style="font-family:宋体"}[（]{style="font-family:
宋体"}[可以使用]{lang="EN-US" style="font-family:宋体"}[undo activation-key]{lang="EN-US"}[或者直接使用]{lang="EN-US" style="font-family:宋体"}[activation-key 13]{lang="EN-US"}[进行配置]{lang="EN-US" style="font-family:宋体"}[）]{style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[\[Sysname\] line console 0]{lang="EN-US"}]{#struct_0_18173_18228_350793212}

[\[Sysname-line-console0\] undo activation-key]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[此时生效的快捷键为用户线类视图下的配置，验证过程如下：]{style="font-family:宋体"}]{#struct_0_18173_18228_1339175208}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[退出]{lang="EN-US" style="font-family:宋体"}[Console]{lang="EN-US"}]{#struct_0_18173_18228_x2048289521}[口终端会话。]{lang="EN-US" style="font-family:宋体"}

[[\[Sysname-line-console0\] return]{lang="EN-US"}]{#struct_0_18173_18228_1557883471}

[\<Sysname\> quit]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重新使用]{style="font-family:宋体"}]{#struct_0_18173_18228_901039678}[Console]{lang="EN-US"}[口登录设备，能看到如下显示信息。]{style="font-family:宋体"}

[[Press ENTER to get started.]{lang="EN-US"}]{#struct_0_18173_18228_x2048289522}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[此时，]{style="font-family:宋体"}]{#struct_0_18173_18228_1154598944}[\<Enter\>]{lang="EN-US"}[键失效，需要按]{style="font-family:宋体"}[\<s\>]{lang="EN-US"}[键才能出现用户视图提示符，启动]{style="font-family:宋体"}[Console]{lang="EN-US"}[口终端会话。]{style="font-family:宋体"}

[[\<Sysname\>]{lang="EN-US"}]{#struct_0_18173_18228_1661782338}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x2048289523}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[line]{lang="EN-US"}**]{#struct_0_18173_18228_x1574284411}
:::

::: {#1167972383 .myid}
[]{#_Toc404782482}[]{#struct_0_18173_18228_x1520189802}

**登录设备 \-- 登录设备命令 \-- lock**

------------------------------------------------------------------------

[**[lock]{lang="EN-US"}**]{#struct_0_18173_18228_1406850160}[命令用来锁住当前用户线，防止未授权的用户操作该用户线。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1977277720}

[**[lock]{lang="EN-US"}**]{#struct_0_18173_18228_x1832654738}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_x2048289524}

[[系统不会自动锁住当前用户线。]{style="font-family:宋体"}]{#struct_0_18173_18228_1961167998}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_2022736867}

[[用户视图]{style="font-family:宋体"}]{#struct_0_18173_18228_1036664336}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_1661813354}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_896446617}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_959719566}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1463036820}

[[FIPS]{lang="EN-US"}]{#struct_0_18173_18228_x472690938}[模式下，不支持本命令。]{style="font-family:宋体"}

[[用户输入]{style="font-family:宋体"}**[lock]{lang="EN-US"}**]{#struct_0_18173_18228_290362645}[命令后，系统提示输入密码（密码最大长度为]{style="font-family:宋体"}[16]{lang="EN-US"}[个字符），并提示再次输入密码，只有两次输入的密码相同，]{style="font-family:宋体"}[Lock]{lang="EN-US"}[操作才能成功。之后，如果用户要再进入系统，需要按回车键，并输入刚才配置的密码后，才能结束锁定，进入系统。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1568014106}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_1039090099}[锁住当前用户线然后解锁。]{style="font-family:宋体"}

[[\<Sysname\> lock]{lang="EN-US"}]{#struct_0_18173_18228_x1652091630}

[Please input password\<1 to 16\> to lock current line:]{lang="EN-US"}

[Password:]{lang="EN-US"}

[Again:]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[                   locked !]{lang="EN-US"}

[[此时，命令行用户线被锁定。键入回车，并输入正确的密码后，可以解锁。]{style="font-family:宋体"}]{#struct_0_18173_18228_440413579}

[[Password:]{lang="EN-US"}]{#struct_0_18173_18228_x1115138668}

[\<Sysname\>]{lang="EN-US"}
:::

::: {#1214567650 .myid}
[]{#_Toc404782483}[]{#struct_0_18173_18228_202267320}

**登录设备 \-- 登录设备命令 \-- parity**

------------------------------------------------------------------------

[**[parity]{lang="EN-US"}**]{#struct_0_18173_18228_290362644}[命令用来设置校验位的解析和生成方式。]{style="font-family:宋体"}

[**[undo parity]{lang="EN-US"}**]{#struct_0_18173_18228_x1568014107}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x526993842}

[**[parity]{lang="EN-US"}**[ { **even** \| **mark** \| **none** \| **odd** \| **space** }]{lang="EN-US"}]{#struct_0_18173_18228_1821204361}

[**[undo parity]{lang="EN-US"}**]{#struct_0_18173_18228_464675256}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_1213220355}

[[设备校验位的校验方式为]{style="font-family:宋体"}**[none]{lang="EN-US"}**]{#struct_0_18173_18228_x1048902294}[，即不进行校验。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1968386899}

[[用户线视图]{style="font-family:宋体"}]{#struct_0_18173_18228_x510162078}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_290362643}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1568014112}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1286443193}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1011732531}

[**[even]{lang="EN-US"}**]{#struct_0_18173_18228_867709293}[：进行偶校验。]{style="font-family:宋体"}

[**[mark]{lang="EN-US"}**]{#struct_0_18173_18228_1405892550}[：进行标记校验。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_18173_18228_2027501999}[：无校验。]{style="font-family:宋体"}

[**[odd]{lang="EN-US"}**]{#struct_0_18173_18228_x1616405484}[：进行奇校验。]{style="font-family:宋体"}

[**[space]{lang="EN-US"}**]{#struct_0_18173_18228_290362642}[：进行空格校验。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1568014113}

[[访问终端和设备相应用户线下校验位的设置必须一致，双方才能正常通信。]{style="font-family:宋体"}]{#struct_0_18173_18228_1442440162}

[[VTY]{lang="EN-US"}]{#struct_0_18173_18228_1219380048}[用户线视图不支持该命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1510537916}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x1479534886}[将]{style="font-family:宋体"}[AUX]{lang="EN-US"}[口传输校验位设为奇校验。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_147721070}

[\[Sysname\] line aux 0]{lang="EN-US"}

[\[Sysname-line-aux0\] parity odd]{lang="EN-US"}
:::

::: {#-1631387965 .myid}
[]{#_Toc404782484}[]{#struct_0_18173_18228_x1997104259}

**登录设备 \-- 登录设备命令 \-- protocol inbound**

------------------------------------------------------------------------

[**[protocol inbound]{lang="EN-US"}**]{#struct_0_18173_18228_76608958}[命令用来指定所在用户线支持的协议。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **protocol inbound**]{lang="EN-US"}]{#struct_0_18173_18228_1716816472}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1950050092}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_18173_18228_x171766232}[模式下：]{style="font-family:宋体"}

[**[protocol inbound]{lang="EN-US"}**[ { **all** \| **pad** \| **ssh** \| **telnet** }]{lang="EN-US"}]{#struct_0_18173_18228_57327175}

[**[undo]{lang="EN-US"}**[ **protocol inbound**]{lang="EN-US"}]{#struct_0_18173_18228_x1995593968}

[[FIPS]{lang="EN-US"}]{#struct_0_18173_18228_97344517}[模式下：]{style="font-family:宋体"}

[**[protocol inbound]{lang="EN-US"}**[ **ssh**]{lang="EN-US"}]{#struct_0_18173_18228_581734823}

[**[undo]{lang="EN-US"}**[ **protocol inbound**]{lang="EN-US"}]{#struct_0_18173_18228_x1485268705}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_839576018}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_18173_18228_1942319659}[模式下：系统支持所有协议。]{style="font-family:宋体"}

[[FIPS]{lang="EN-US"}]{#struct_0_18173_18228_x2146345623}[模式下：系统支持]{style="font-family:宋体"}[SSH]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_778833263}

[[VTY]{lang="EN-US"}]{#struct_0_18173_18228_452752469}[用户线视图]{style="font-family:宋体"}[/VTY]{lang="EN-US"}[用户线类视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_1087851660}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_872344331}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_744925908}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_x412335223}

[**[all]{lang="EN-US"}**]{#struct_0_18173_18228_713437199}[：支持所有的协议，包括]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[、]{style="font-family:宋体"}[SSH]{lang="EN-US"}[和]{style="font-family:宋体"}[PAD]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[pad]{lang="EN-US"}**]{#struct_0_18173_18228_x1127250270}[：支持]{style="font-family:宋体"}[PAD]{lang="EN-US"}[协议。该参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ssh]{lang="EN-US"}**]{#struct_0_18173_18228_x1917458940}[：支持]{style="font-family:宋体"}[SSH]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[**[telnet]{lang="EN-US"}**]{#struct_0_18173_18228_x1168800813}[：支持]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_x739524988}

[[如果要配置用户线支持]{style="font-family:宋体"}[SSH]{lang="EN-US"}]{#struct_0_18173_18228_x1728037460}[协议，必须先将该用户的认证方式配置为]{style="font-family:宋体"}**[scheme]{lang="EN-US"}**[，否则]{style="font-family:宋体"}**[protocol inbound ssh]{lang="EN-US"}**[命令会执行]{style="font-family:宋体"}[失败。相关配置可参考命令]{style="font-family:宋体"}**[authentication-mode]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[用户线视图下，该命令的配置结果将在下次登录时生效。]{style="font-family:宋体"}]{#struct_0_18173_18228_609223307}

[[用户线视图下，对]{style="font-family:宋体"}**[authentication-mode]{lang="EN-US"}**]{#struct_0_18173_18228_x316482280}[和]{style="font-family:宋体"}**[protocol inbound]{lang="EN-US"}**[进行关联绑定。]{style="font-family:宋体"}

[[当这两条命令均配置为缺省值，此时该用户线视图下的这两条命令配置值均取该类用户线类视图下的相应的配置；若该类用户线类视图下没有进行相应的配置，则均取缺省值。]{style="font-family:宋体"}]{#struct_0_18173_18228_411560303}

[[当两条命令中的任意一条配置了非缺省值，那么另外一条取缺省值。当两条命令都配置成非缺省值，则均取用户线下的配置值。]{style="font-family:宋体"}]{#struct_0_18173_18228_x2026532070}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1649885798}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x1268371435}[设置用户线]{style="font-family:宋体"}[VTY 0]{lang="EN-US"}[到]{style="font-family:宋体"}[VTY 4]{lang="EN-US"}[只支持]{style="font-family:宋体"}[SSH]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_161937954}

[\[Sysname\] line vty 0 4]{lang="EN-US"}

[\[Sysname-line-vty0-4\] authentication-mode scheme]{lang="EN-US"}

[\[Sysname-line-vty0-4\] protocol inbound ssh]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_1346712968}[设置]{style="font-family:宋体"}[VTY]{lang="EN-US"}[用户线类支持]{style="font-family:宋体"}[SSH]{lang="EN-US"}[协议，认证方式为]{style="font-family:宋体"}[scheme]{lang="EN-US"}[。同时设置用户线]{style="font-family:宋体"}[VTY 0]{lang="EN-US"}[到]{style="font-family:宋体"}[VTY 4]{lang="EN-US"}[不进行登陆认证，支持所有的协议。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_1000845895}

[\[Sysname\] line class vty]{lang="EN-US"}

[\[Sysname-line-class-vty\] authentication-mode scheme]{lang="EN-US"}

[\[Sysname-line-class-vty\] protocol inbound ssh]{lang="EN-US"}

[\[Sysname-line-class-vty\] line vty 0 4]{lang="EN-US"}

[\[Sysname-line-vty0-4\] authentication-mode none]{lang="EN-US"}

[[验证过程如下：]{style="font-family:宋体"}]{#struct_0_18173_18228_x1324258832}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_18173_18228_x1606366321}[Telnet]{lang="EN-US"}[方式登陆，无需认证即可成功登陆。]{style="font-family:宋体"}

[[\<Client\> telnet 192.168.1.241]{lang="EN-US"}]{#struct_0_18173_18228_x1061273509}

[Trying 192.168.1.241 \...]{lang="EN-US"}

[Press CTRL+K to abort]{lang="EN-US"}

[Connected to 192.168.1.241 \...]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ]{lang="EN-US"}

[\* Copyright (c) 2004-2013 Hangzhou H3C Tech. Co., Ltd. All rights reserved.  \*]{lang="EN-US"}

[\* Without the owner\'s prior written consent,                                 \*]{lang="EN-US"}

[\* no decompiling or reverse-engineering shall be allowed.                    \*]{lang="EN-US"}

[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ]{lang="EN-US"}

[ ]{lang="EN-US"}

[\<Server\>]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[查看当前正在使用的用户线以及用户的相关信息，用户线为]{style="font-family:宋体"}]{#struct_0_18173_18228_2032220134}[line 0]{lang="EN-US"}[，则证明该配置下用户线下配置生效。]{style="font-family:宋体"}

[[\<Server\> display users]{lang="EN-US"}]{#struct_0_18173_18228_x1216411561}

[  Idx  Line     Idle       Time              Pid     Type]{lang="EN-US"}

[+ 50   VTY 0    00:00:00   Jan 17 15:29:27   189     TEL]{lang="EN-US"}

[ ]{lang="EN-US"}

[Following are more details.]{lang="EN-US"}

[VTY 0   :]{lang="EN-US"}

[        Location: 192.168.1.186]{lang="EN-US"}

[ +    : Current operation user.]{lang="EN-US"}

[ F    : Current operation user works in async mode.]{lang="EN-US"}
:::

::: {#934886966 .myid}
[]{#_Toc404782485}[]{#struct_0_18173_18228_x1717927770}[]{#_Toc361076169}

**登录设备 \-- 登录设备命令 \-- redirect disconnect**

------------------------------------------------------------------------

[**[redirect disconnect]{lang="EN-US"}**]{#struct_0_18173_18228_2013127528}[命令用来强制断开已经建立的]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[重定向连接。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1334612772}

[**[redirect disconnect]{lang="EN-US"}**]{#struct_0_18173_18228_x152302576}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_663161081}

[[AUX/TTY]{lang="EN-US"}]{#struct_0_18173_18228_x698354066}[用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_x152368112}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1352427775}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_934188957}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x152171504}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x913998485}[强制断开已经建立的]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[重定向连接。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_x1058572318}

[\[Sysname\] line tty 1]{lang="EN-US"}

[\[Sysname-line-tty1\] redirect disconnect]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_436252044}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[redirect enable]{lang="EN-US"}**]{#struct_0_18173_18228_x152237040}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display tcp]{lang="EN-US"}**]{#struct_0_18173_18228_x1672494682}
:::

::: {#-189148690 .myid}
[]{#_Toc404782486}[]{#struct_0_18173_18228_x2051336511}[]{#_Toc361076165}

**登录设备 \-- 登录设备命令 \-- redirect enable**

------------------------------------------------------------------------

[**[redirect enable]{lang="EN-US"}**]{#struct_0_18173_18228_x152040432}[命令用来使能当前用户线的]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[重定向功能。]{style="font-family:宋体"}

[**[undo redirect enable]{lang="EN-US"}**]{#struct_0_18173_18228_x521604698}[命令用来用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_1048522550}

[**[redirect enable]{lang="EN-US"}**]{#struct_0_18173_18228_698178042}

[**[undo redirect enable]{lang="EN-US"}**]{#struct_0_18173_18228_x152105968}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_301116153}

[[当前用户线的重定向功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_18173_18228_x10844180}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_x151909360}

[[AUX/TTY]{lang="EN-US"}]{#struct_0_18173_18228_734077733}[用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_x266804605}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1553992652}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_x151974896}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_1197023371}

[[用户和设备]{style="font-family:宋体"}[A]{lang="EN-US"}]{#struct_0_18173_18228_x1917977887}[相连，能够]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[登录到设备]{style="font-family:宋体"}[A]{lang="EN-US"}[；设备]{style="font-family:宋体"}[A]{lang="EN-US"}[通过]{style="font-family:宋体"}[AUX]{lang="EN-US"}[口]{style="font-family:宋体"}[/]{lang="EN-US"}[异步串口和设备]{style="font-family:
宋体"}[B]{lang="EN-US"}[相连，如果设备]{style="font-family:宋体"}[B]{lang="EN-US"}[要给用户提供]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[服务，但又不方便告知用户]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址时，可以在设备]{style="font-family:宋体"}[A]{lang="EN-US"}[上配置]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[重定向功能，则用户执行"]{style="font-family:宋体"}[telnet ]{lang="EN-US"}[设备]{style="font-family:宋体"}[A]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"} [特定端口号"（该端口号由]{style="font-family:宋体"}**[redirect listen-port]{lang="EN-US"}**[命令决定）能够登录设备]{style="font-family:宋体"}[B]{lang="EN-US"}[，相当于用户直接]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[登录设备]{style="font-family:宋体"}[B]{lang="EN-US"}[。]{style="font-family:宋体"}

[[重定向服务器与目的设备相连端口对应的用户线的传输速率和停止位的设置必须相同，否则重定向将失败。]{style="font-family:宋体"}]{#struct_0_18173_18228_x151778288}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[传输速率可以通过]{style="font-family:宋体"}]{#struct_0_18173_18228_1496487820}**[speed]{lang="EN-US"}**[命令进行设置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[传输速率的设置，请先使用]{style="font-family:宋体"}]{#struct_0_18173_18228_711576774}**[stopbit-error intolerance]{lang="EN-US"}**[命令检测重定向设备与目的设备的停止位设置是否相同。如不相同，可以通过]{style="font-family:宋体"}**[stopbits]{lang="EN-US"}**[命令进行设置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x896901263}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x151843824}[使能]{style="font-family:宋体"}[TTY 7]{lang="EN-US"}[用户线的]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[重定向功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_x366897858}

[\[Sysname\] line tty 7]{lang="EN-US"}

[\[Sysname-line-tty7\] redirect enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x570732032}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[telnet]{lang="EN-US"}**]{#struct_0_18173_18228_x152302577}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display tcp]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18173_18228_663226617}[（请参考三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}[业务）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#-1258346484 .myid}
[]{#_Toc404782487}[]{#struct_0_18173_18228_1501433378}[]{#_Toc361076166}[]{#_Toc301187211}[]{#_Toc263186417}[]{#_Toc139341890}[]{#_Toc95306377}

**登录设备 \-- 登录设备命令 \-- redirect listen-port**

------------------------------------------------------------------------

[**[redirect listen-port]{lang="EN-US"}**]{#struct_0_18173_18228_x152368113}[命令用来设置]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[重定向的监听端口。]{style="font-family:宋体"}

[**[undo redirect listen-port]{lang="EN-US"}**]{#struct_0_18173_18228_x1352362239}[命令用来恢复缺省的监听端口。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x62109150}

[**[redirect listen-port ]{lang="EN-US"}***[port-number]{lang="EN-US"}*]{#struct_0_18173_18228_x152171505}

[**[undo redirect listen-port]{lang="EN-US"}**]{#struct_0_18173_18228_x914064021}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_x393894873}

[[Telnet]{lang="EN-US"}]{#struct_0_18173_18228_x152237041}[重定向的监听端口号为用户线的绝对编号加]{style="font-family:宋体"}[2000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1672560218}

[[AUX/TTY]{lang="EN-US"}]{#struct_0_18173_18228_484363654}[用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_x329288717}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x152040433}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_x521539162}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_205265585}

[*[port-number]{lang="EN-US"}*]{#struct_0_18173_18228_x152105969}[：监听端口号，取值范围为]{lang="EN-US" style="font-family:宋体"}[2000]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[50000]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_301181689}

[[设备只对从该监听端口收到的数据进行重定向。]{style="font-family:宋体"}]{#struct_0_18173_18228_1174987880}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x151909361}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_734143269}[设置]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[重定向的监听端口号为]{style="font-family:宋体"}[3000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_2061582381}

[\[Sysname\] line tty 1]{lang="EN-US"}

[\[Sysname-line-tty1\] redirect listen-port 3000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x151974897}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[redirect enable]{lang="EN-US"}**]{#struct_0_18173_18228_1196957835}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display tcp]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18173_18228_795528224}[（请参考三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}[业务）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#202292221 .myid}
[]{#struct_0_18173_18228_1860375749}[]{#_Toc404782488}

**登录设备 \-- 登录设备命令 \-- redirect passthrough**

------------------------------------------------------------------------

[**[redirect]{lang="EN-US"}**[ **passthrough**]{lang="EN-US"}]{#struct_0_18173_18228_1049205490}[命令用来设置在]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[重定向时对数据不进行任何处理直接转发。]{style="font-family:宋体"}

[**[undo redirect]{lang="EN-US"}**[ **passthrough**]{lang="EN-US"}]{#struct_0_18173_18228_713942590}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_884192170}

[**[redirect]{lang="EN-US"}**[ **passthrough**]{lang="EN-US"}]{#struct_0_18173_18228_176083745}

[**[undo]{lang="EN-US"}**[ **redirect** **passthrough**]{lang="EN-US"}]{#struct_0_18173_18228_x882408699}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_1860441285}

[[在建立]{style="font-family:宋体"}[Telnet]{lang="EN-US"}]{#struct_0_18173_18228_1442695147}[重定向连接后，将对数据按照]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[协议规定处理。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_1595270591}

[[AUX/TTY]{lang="EN-US"}]{#struct_0_18173_18228_x1725343513}[用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_669584147}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x2049587307}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_x958693122}

[[配置该命令后，对经过]{style="font-family:宋体"}[Telnet]{lang="EN-US"}]{#struct_0_18173_18228_347378936}[重定向设备的数据不进行任何处理直接转发。某些情况下，]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[重定向服务器连接的用户和目的设备之间的报文传输是不遵循]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[标准协议的，因此只需要用户与目的设备能够解析双方交互的数据报文即可完成登录过程。在此情况下，]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[重定向服务器需要配置]{style="font-family:宋体"}**[redirect passthrough]{lang="EN-US"}**[命令保证对这些交互报文仅仅是转发而不进行任何处理，否则将导致用户和目的设备之间的数据解析错误。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_1860506821}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_1062014665}[设置在建立]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[重定向时对数据不进行任何处理直接转发。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_816391742}

[\[Sysname\] line tty 1]{lang="EN-US"}

[\[Sysname-line-tty1\] redirect passthrough]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_2131271355}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[redirect]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_18173_18228_649171898}
:::

::: {#197743845 .myid}
[]{#_Toc404782489}[]{#struct_0_18173_18228_x151778289}[]{#_Toc361076167}[]{#_Toc301187212}[]{#_Toc263186418}[]{#_Toc139341891}[]{#_Toc121585045}

**登录设备 \-- 登录设备命令 \-- redirect refuse-negotiation**

------------------------------------------------------------------------

[**[redirect refuse-negotiation]{lang="EN-US"}**]{#struct_0_18173_18228_1496422284}[命令用来强制设置在建立]{style="font-family:
宋体"}[Telnet]{lang="EN-US"}[重定向连接时不进行]{style="font-family:
宋体"}[Telnet]{lang="EN-US"}[选项协商。]{style="font-family:
宋体"}

[**[undo redirect refuse-negotiation]{lang="EN-US"}**]{#struct_0_18173_18228_x1126975070}[命令用来设置在建立]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[重定向连接时进行]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[选项协商。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1249415429}

[**[redirect refuse-negotiation]{lang="EN-US"}**]{#struct_0_18173_18228_x151843825}

[**[undo redirect refuse-negotiation]{lang="EN-US"}**]{#struct_0_18173_18228_x366832322}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1363342592}

[[在建立]{style="font-family:宋体"}[Telnet]{lang="EN-US"}]{#struct_0_18173_18228_x395316371}[重定向连接时，将进行]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[选项协商。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_x152302578}

[[AUX/TTY]{lang="EN-US"}]{#struct_0_18173_18228_662505721}[用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_2019664318}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x152368114}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1352296703}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_1532711652}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x152171506}[设置在建立]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[重定向连接时不进行]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[选项协商。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_x914129557}

[\[Sysname\] line tty 1]{lang="EN-US"}

[\[Sysname-line-tty1\] redirect refuse-negotiation]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1980300716}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[redirect enable]{lang="EN-US"}**]{#struct_0_18173_18228_x152237042}
:::

::: {#-1886560562 .myid}
[]{#_Toc404782490}[]{#struct_0_18173_18228_x1672625754}[]{#_Toc361076168}[]{#_Toc301187216}[]{#_Toc263186422}[]{#_Toc139341894}[]{#_Toc121585042}

**登录设备 \-- 登录设备命令 \-- redirect timeout**

------------------------------------------------------------------------

[**[redirect timeout]{lang="EN-US"}**]{#struct_0_18173_18228_x932086735}[命令用来设置]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[重定向的空闲超时时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **redirect timeout**]{lang="EN-US"}]{#struct_0_18173_18228_x152040434}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x521735770}

[**[redirect timeout ]{lang="EN-US"}***[time]{lang="EN-US"}*]{#struct_0_18173_18228_1436197802}

[**[undo redirect timeout]{lang="EN-US"}**]{#struct_0_18173_18228_x151210197}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_x152105970}

[[设备]{style="font-family:宋体"}[Telnet]{lang="EN-US"}]{#struct_0_18173_18228_301640442}[重定向的空闲超时时间为]{style="font-family:宋体"}[360]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_354013073}

[[AUX/TTY]{lang="EN-US"}]{#struct_0_18173_18228_x151909362}[用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_733946661}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_765137274}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_x151974898}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_1197940875}

[*[time]{lang="EN-US"}*]{#struct_0_18173_18228_1915836297}[：超时时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}[0]{lang="EN-US"}[表示永不超时。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_x151778290}

[[如果在指定的时间内没有从]{style="font-family:宋体"}[Telnet]{lang="EN-US"}]{#struct_0_18173_18228_1495963533}[客户端接收到数据，则断开]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[重定向连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1114441292}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x1799103002}[设置]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[重定向的空闲超时时间为]{style="font-family:宋体"}[200]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_x151843826}

[\[Sysname\] line tty 1]{lang="EN-US"}

[\[Sysname-line-tty1\] redirect timeout 200]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x367028930}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[redirect enable]{lang="EN-US"}**]{#struct_0_18173_18228_x152302579}
:::

::: {#1553018043 .myid}
[]{#_Toc404782491}[]{#struct_0_18173_18228_x758710044}[]{#_Toc297210648}[]{#_Toc296689418}[]{#_Toc401307853}[]{#_Toc401565592}[]{#_Toc401737598}[]{#_Toc401307854}[]{#_Toc401565593}[]{#_Toc401737599}[]{#_Toc401307855}[]{#_Toc401565594}[]{#_Toc401737600}[]{#_Toc401307856}[]{#_Toc401565595}[]{#_Toc401737601}[]{#_Toc401307857}[]{#_Toc401565596}[]{#_Toc401737602}[]{#_Toc401307858}[]{#_Toc401565597}[]{#_Toc401737603}[]{#_Toc401307859}[]{#_Toc401565598}[]{#_Toc401737604}[]{#_Toc401307860}[]{#_Toc401565599}[]{#_Toc401737605}[]{#_Toc401307861}[]{#_Toc401565600}[]{#_Toc401737606}[]{#_Toc401307862}[]{#_Toc401565601}[]{#_Toc401737607}[]{#_Toc401307863}[]{#_Toc401565602}[]{#_Toc401737608}[]{#_Toc401307864}[]{#_Toc401565603}[]{#_Toc401737609}[]{#_Toc401307865}[]{#_Toc401565604}[]{#_Toc401737610}[]{#_Toc401307866}[]{#_Toc401565605}[]{#_Toc401737611}[]{#_Toc401307867}[]{#_Toc401565606}[]{#_Toc401737612}[]{#_Toc401307868}[]{#_Toc401565607}[]{#_Toc401737613}[]{#_Toc401307869}[]{#_Toc401565608}[]{#_Toc401737614}[]{#_Toc401307870}[]{#_Toc401565609}[]{#_Toc401737615}[]{#_Toc401307871}[]{#_Toc401565610}[]{#_Toc401737616}[]{#_Toc401307872}[]{#_Toc401565611}[]{#_Toc401737617}[]{#_Toc401307873}[]{#_Toc401565612}[]{#_Toc401737618}[]{#_Toc401307874}[]{#_Toc401565613}[]{#_Toc401737619}[]{#_Toc401307875}[]{#_Toc401565614}[]{#_Toc401737620}[]{#_Toc401307876}[]{#_Toc401565615}[]{#_Toc401737621}[]{#_Toc401307877}[]{#_Toc401565616}[]{#_Toc401737622}[]{#_Toc401307878}[]{#_Toc401565617}[]{#_Toc401737623}[]{#_Toc401307879}[]{#_Toc401565618}[]{#_Toc401737624}[]{#_Toc401307880}[]{#_Toc401565619}[]{#_Toc401737625}[]{#_Toc401307881}[]{#_Toc401565620}[]{#_Toc401737626}[]{#_Toc401307882}[]{#_Toc401565621}[]{#_Toc401737627}[]{#_Toc401307883}[]{#_Toc401565622}[]{#_Toc401737628}[]{#_Toc401307884}[]{#_Toc401565623}[]{#_Toc401737629}[]{#_Toc401307885}[]{#_Toc401565624}[]{#_Toc401737630}[]{#_Toc401307886}[]{#_Toc401565625}[]{#_Toc401737631}[]{#_Toc401307887}[]{#_Toc401565626}[]{#_Toc401737632}[]{#_Toc401307888}[]{#_Toc401565627}[]{#_Toc401737633}[]{#_Toc401307889}[]{#_Toc401565628}[]{#_Toc401737634}[]{#_Toc401307890}[]{#_Toc401565629}[]{#_Toc401737635}[]{#_Toc401307891}[]{#_Toc401565630}[]{#_Toc401737636}[]{#_Toc401307892}[]{#_Toc401565631}[]{#_Toc401737637}[]{#_Toc401307893}[]{#_Toc401565632}[]{#_Toc401737638}[]{#_Toc401307894}[]{#_Toc401565633}[]{#_Toc401737639}[]{#_Toc401307895}[]{#_Toc401565634}[]{#_Toc401737640}[]{#_Toc401307896}[]{#_Toc401565635}[]{#_Toc401737641}[]{#_Toc401307897}[]{#_Toc401565636}[]{#_Toc401737642}[]{#_Toc401307898}[]{#_Toc401565637}[]{#_Toc401737643}[]{#_Toc401307899}[]{#_Toc401565638}[]{#_Toc401737644}[]{#_Toc401307900}[]{#_Toc401565639}[]{#_Toc401737645}[]{#_Toc401307901}[]{#_Toc401565640}[]{#_Toc401737646}[]{#_Toc401307902}[]{#_Toc401565641}[]{#_Toc401737647}[]{#_Toc401307903}[]{#_Toc401565642}[]{#_Toc401737648}[]{#_Toc401307904}[]{#_Toc401565643}[]{#_Toc401737649}[]{#_Toc401307905}[]{#_Toc401565644}[]{#_Toc401737650}[]{#_Toc401307906}[]{#_Toc401565645}[]{#_Toc401737651}[]{#_Toc401307907}[]{#_Toc401565646}[]{#_Toc401737652}[]{#_Toc401307908}[]{#_Toc401565647}[]{#_Toc401737653}[]{#_Toc401307909}[]{#_Toc401565648}[]{#_Toc401737654}[]{#_Toc401307910}[]{#_Toc401565649}[]{#_Toc401737655}[]{#_Toc401307911}[]{#_Toc401565650}[]{#_Toc401737656}[]{#_Toc401307912}[]{#_Toc401565651}[]{#_Toc401737657}[]{#_Toc401307913}[]{#_Toc401565652}[]{#_Toc401737658}[]{#_Toc401307914}[]{#_Toc401565653}[]{#_Toc401737659}[]{#_Toc401307915}[]{#_Toc401565654}[]{#_Toc401737660}[]{#_Toc401307916}[]{#_Toc401565655}[]{#_Toc401737661}[]{#_Toc401307917}[]{#_Toc401565656}[]{#_Toc401737662}[]{#_Toc401307918}[]{#_Toc401565657}[]{#_Toc401737663}

**登录设备 \-- 登录设备命令 \-- screen-length**

------------------------------------------------------------------------

[**[screen-length]{lang="EN-US"}**]{#struct_0_18173_18228_951186095}[命令用来设置分屏显示时，每屏所显示的行数。]{style="font-family:宋体"}

[**[undo screen-length]{lang="EN-US"}**]{#struct_0_18173_18228_1484071865}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x833950701}

[**[screen-length]{lang="EN-US"}**[ *screen-length*]{lang="EN-US"}]{#struct_0_18173_18228_64873208}

[**[undo screen-length]{lang="EN-US"}**]{#struct_0_18173_18228_419260109}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_638701518}

[[每屏显示]{style="font-family:宋体"}[24]{lang="EN-US"}]{#struct_0_18173_18228_1659150588}[行数据。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_290362636}

[[用户线视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18173_18228_x758710045}[用户线类视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_951120559}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_1832485064}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_497470862}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_762018703}

[*[screen-length]{lang="EN-US"}*]{#struct_0_18173_18228_289645980}[：指定每屏所显示的行数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[512]{lang="EN-US"}[。]{style="font-family:宋体"}[0]{lang="EN-US"}[表示一次性显示全部信息，即不进行分屏显示。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_x6278339}

[[设备支持分屏显示信息，在暂停显示时按空格键，能继续显示下一屏信息。该命令设置的是每一屏所显示的行数，但显示终端实际显示的行数由终端的规格决定。比如，设置]{style="font-family:宋体"}*[screen-length]{lang="EN-US"}*]{#struct_0_18173_18228_x868253584}[的值为]{style="font-family:宋体"}[40]{lang="EN-US"}[，但显示终端的规格为]{style="font-family:宋体"}[24]{lang="EN-US"}[行，当暂停显示按空格键时，设备发送给显示终端的信息为]{style="font-family:宋体"}[40]{lang="EN-US"}[行，但当前屏幕显示的是第]{style="font-family:宋体"}[18]{lang="EN-US"}[～第]{style="font-family:宋体"}[40]{lang="EN-US"}[行的信息，前面的]{style="font-family:宋体"}[17]{lang="EN-US"}[行信息，需要通过]{style="font-family:宋体"}[\<Page Up\>/\<Page Down\>]{lang="EN-US"}[键来翻看。]{style="font-family:宋体"}

[[缺省情况下，分屏显示功能处于开启状态。配置]{style="font-family:宋体"}**[screen-length 0]{lang="EN-US"}**]{#struct_0_18173_18228_x1665952491}[或]{style="font-family:宋体"}**[screen-length disable]{lang="EN-US"}**[可关闭分屏显示功能。]{style="font-family:宋体"}

[[如果用户线视图下配置]{style="font-family:宋体"}**[screen-length]{lang="EN-US"}**]{#struct_0_18173_18228_x1392802335}[为缺省值，并且此时用户线类视图下配置了]{style="font-family:宋体"}**[screen-length]{lang="EN-US"}**[，那么用户线视图下的生效配置值为用户线类视图下的配置；如果用户线类视图下未配置，则生效的为缺省值。]{style="font-family:宋体"}

[[需要注意的是，用户线视图下使用本命令配置的分屏显示信息行数立即生效；在用户线类视图下配置的分屏显示信息行数将在下次登录时生效。]{style="font-family:宋体"}]{#struct_0_18173_18228_1879124758}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1447625658}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x1375842046}[设置]{style="font-family:宋体"}[Console]{lang="EN-US"}[用户线分屏显示时，每屏显示]{style="font-family:宋体"}[30]{lang="EN-US"}[行数据。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_x2097340098}

[\[Sysname\] line console 0]{lang="EN-US"}

[\[Sysname-line-console0\] screen-length 30]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x2128274998}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[screen-length disable]{lang="EN-US"}**]{#struct_0_18173_18228_x676824244}[（基础配置指导]{lang="EN-US" style="font-family:宋体"}[/CLI]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#835031329 .myid}
[]{#_Toc404782492}[]{#struct_0_18173_18228_x1296312982}[]{#_Toc263186424}[]{#_Toc139341897}[]{#_Toc95306325}[]{#_Toc15375244}[]{#_Toc313524792}[]{#_Toc313524793}[]{#_Toc313524794}[]{#_Toc313524795}[]{#_Toc313524796}[]{#_Toc313524797}[]{#_Toc313524798}[]{#_Toc313524799}[]{#_Toc313524800}[]{#_Toc313524801}[]{#_Toc313524802}[]{#_Toc313524803}[]{#_Toc313524804}[]{#_Toc313524805}[]{#_Toc313524806}[]{#_Toc313524807}[]{#_Toc313524808}[]{#_Toc313524809}[]{#_Toc313524810}[]{#_Toc313524811}[]{#_Toc313524812}[]{#_Toc313524813}[]{#_Toc313524814}[]{#_Toc313524815}

**登录设备 \-- 登录设备命令 \-- send**

------------------------------------------------------------------------

[**[send]{lang="EN-US"}**]{#struct_0_18173_18228_x1665952492}[命令用来向指定的用户线发送消息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1796086862}

[**[send]{lang="EN-US"}**[ { **all** \| *number1* \| { **aux** \| **console** \| **tty** \| **vty** } *number2* }]{lang="EN-US"}]{#struct_0_18173_18228_x815563528}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_1391424683}

[[用户视图]{style="font-family:宋体"}]{#struct_0_18173_18228_1388128925}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_x2025008519}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1368731978}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_355054829}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_x321994302}

[**[all]{lang="EN-US"}**]{#struct_0_18173_18228_x1665952493}[：所有的用户线。]{style="font-family:宋体"}

[*[number1]{lang="EN-US"}*]{#struct_0_18173_18228_x230002921}[：用户线的编号（绝对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准，一般从]{style="font-family:宋体"}[0]{lang="EN-US"}[开始。]{style="font-family:宋体"}

[**[aux]{lang="EN-US"}**]{#struct_0_18173_18228_x1989489945}[：]{style="font-family:宋体"}[AUX]{lang="EN-US"}[用户线。]{style="font-family:宋体"}

[**[console]{lang="EN-US"}**]{#struct_0_18173_18228_1685751963}[：]{style="font-family:宋体"}[Console]{lang="EN-US"}[用户线。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[tty]{lang="EN-US"}**]{#struct_0_18173_18228_1767566245}[：]{style="font-family:宋体"}[TTY]{lang="EN-US"}[用户线。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vty]{lang="EN-US"}**]{#struct_0_18173_18228_x1651437882}[：]{style="font-family:宋体"}[VTY]{lang="EN-US"}[用户线。]{style="font-family:宋体"}

[*[number2]{lang="EN-US"}*]{#struct_0_18173_18228_1349555264}[：用户线的编号（相对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_1510991196}

[[输入本命令后回车，系统会提示您可以输入消息内容了。在输入消息内容时，按]{style="font-family:宋体"}[\<Enter\>]{lang="EN-US"}]{#struct_0_18173_18228_x148664471}[键结束输入，按]{style="font-family:宋体"}[\<Ctrl+C\>]{lang="EN-US"}[组合键取消此次操作。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1665952494}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x633287448}[使用]{style="font-family:宋体"}[VTY 0]{lang="EN-US"}[用户线上线的用户想重启设备，于是发信息"]{style="font-family:宋体"}[Note please, I will reboot the system in 3 minutes.]{lang="EN-US"}["来提醒]{style="font-family:宋体"}[VTY 1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> send vty 1]{lang="EN-US"}]{#struct_0_18173_18228_x2051374053}

[Input message, end with Enter; abort with CTRL+C:]{lang="EN-US"}

[Note please, I will reboot the system in 3 minutes.]{lang="EN-US"}

[Send message? \[Y/N\]:y]{lang="EN-US"}

[[使用]{style="font-family:宋体"}[VTY 1]{lang="EN-US"}]{#struct_0_18173_18228_x957168137}[用户线登录的用户将收到如下消息：]{style="font-family:宋体"}

[[\[Sysname\]]{lang="EN-US"}]{#struct_0_18173_18228_80582365}

[ ]{lang="EN-US"}

[\*\*\*]{lang="EN-US"}

[\*\*\*]{lang="EN-US"}

[\*\*\*Message from vty0 to vty1]{lang="EN-US"}

[\*\*\*]{lang="EN-US"}

[Note please, I will reboot the system in 3 minutes.]{lang="EN-US"}
:::

::: {#-972616514 .myid}
[]{#_Toc404782493}[]{#struct_0_18173_18228_x721659267}[]{#_Toc263186425}[]{#_Toc139341898}[]{#_Toc95306326}

**登录设备 \-- 登录设备命令 \-- set authentication password**

------------------------------------------------------------------------

[**[set authentication password]{lang="EN-US"}**]{#struct_0_18173_18228_x1665952495}[命令用来设置认证密码。]{style="font-family:
宋体"}

[**[undo set authentication password]{lang="EN-US"}**]{#struct_0_18173_18228_932796493}[命令用来取消认证密码。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_1568309348}

[**[set authentication password]{lang="EN-US"}**[ { **hash** \| **simple** } *password*]{lang="EN-US"}]{#struct_0_18173_18228_x451730507}

[**[undo set authentication password]{lang="EN-US"}**]{#struct_0_18173_18228_1877340844}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_x778095322}

[[没有设置认证密码。]{style="font-family:宋体"}]{#struct_0_18173_18228_x2056167571}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_491296772}

[[用户线视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18173_18228_1701012342}[用户线类视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1665952496}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_529511966}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1744490991}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_x603308631}

[**[hash]{lang="EN-US"}**]{#struct_0_18173_18228_816616949}[：表示以哈希方式设置认证密码。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_18173_18228_x1963967170}[：表示以明文方式设置认证密码。]{style="font-family:宋体"}

[*[password]{lang="EN-US"}*]{#struct_0_18173_18228_x1128655193}[：设置的明文密码或哈希密码，区分大小写。明文密码的长度范围是]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[；哈希密码的长度范围是]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[110]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_1204050685}

[[FIPS]{lang="EN-US"}]{#struct_0_18173_18228_218833890}[模式下，不支持本命令。]{style="font-family:宋体"}

[[以明文或哈希方式设置的密码，均以哈希计算后的密文形式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_18173_18228_x1665952497}

[[如果用户线视图下配置]{style="font-family:宋体"}**[set authentication password]{lang="EN-US"}**]{#struct_0_18173_18228_2095595907}[为缺省值，并且此时用户线类视图下配置了]{style="font-family:宋体"}**[set authentication password]{lang="EN-US"}**[，那么用户线视图下的生效的认证密码为用户线类视图下的配置；如果用户线类视图下未配置，则生效的为缺省值。]{style="font-family:宋体"}

[[需要注意的是，在用户线视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18173_18228_x797729150}[用户线类视图下，使用该命令设置的认证密码将在下次登录设备时生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_341617184}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_1316456429}[设置用户线]{style="font-family:宋体"}[Console 0]{lang="EN-US"}[的认证密码为]{style="font-family:宋体"}[hello]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_x1156452903}

[\[Sysname\] line console 0]{lang="EN-US"}

[\[Sysname-line-console0\] authentication-mode password]{lang="EN-US"}

[\[Sysname-line-console0\] set authentication password simple hello]{lang="EN-US"}

[[设置完后如果退出系统，则只有在密码提示信息后输入]{style="font-family:宋体"}[hello]{lang="EN-US"}]{#struct_0_18173_18228_x1848908248}[字符串才能再进入系统。]{style="font-family:宋体"}

[[【相关配置】]{style="font-family:黑体"}]{#struct_0_18173_18228_x826115863}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication-mode]{lang="EN-US"}**]{#struct_0_18173_18228_x1665952498}
:::

::: {#-1182434384 .myid}
[]{#_Toc404782494}[]{#struct_0_18173_18228_1692311380}[]{#_Toc263186426}[]{#_Toc139341899}

**登录设备 \-- 登录设备命令 \-- shell**

------------------------------------------------------------------------

[**[shell]{lang="EN-US"}**]{#struct_0_18173_18228_x1152588756}[命令用来在当前用户线上启动终端服务。]{style="font-family:宋体"}

[**[undo shell]{lang="EN-US"}**]{#struct_0_18173_18228_x536895658}[命令用来在当前用户线上禁止终端服务。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_1149672460}

[**[shell]{lang="EN-US"}**]{#struct_0_18173_18228_x1072604584}

[**[undo shell]{lang="EN-US"}**]{#struct_0_18173_18228_1395867675}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_x429601723}

[[系统在所有的用户线上启动终端服务。]{style="font-family:宋体"}]{#struct_0_18173_18228_1079866931}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1665952499}

[[用户线视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18173_18228_x1036571975}[用户线类视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1022155628}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_2049066938}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_1060142006}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_x238666525}

[**[undo shell]{lang="EN-US"}**]{#struct_0_18173_18228_2141387165}[命令有以下几点限制：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Console]{lang="EN-US"}]{#struct_0_18173_18228_643952553}[用户线视图]{style="font-family:宋体"}[/Console]{lang="EN-US"}[用户线类视图不支持该命令。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果设备上只有一个]{style="font-family:宋体"}]{#struct_0_18173_18228_x1494175801}[AUX]{lang="EN-US"}[口，没有]{style="font-family:宋体"}[Console]{lang="EN-US"}[口（]{style="font-family:宋体"}[Console]{lang="EN-US"}[口和]{style="font-family:宋体"}[AUX]{lang="EN-US"}[口共用），则]{style="font-family:宋体"}[AUX]{lang="EN-US"}[用户线视图]{style="font-family:宋体"}[/AUX]{lang="EN-US"}[用户线类视图也不支持该命令。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户不能在自己登录的用户线上使用该命令。]{style="font-family:宋体"}]{#struct_0_18173_18228_x1665952500}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当设备作为]{lang="EN-US" style="font-family:宋体"}[Telnet/SSH]{lang="EN-US"}]{#struct_0_18173_18228_1335622269}[服务器的时候，不能配置]{lang="EN-US" style="font-family:宋体"}**[undo shell]{lang="EN-US"}**[命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在用户线类视图下使用]{style="font-family:宋体"}]{#struct_0_18173_18228_x1310327287}**[undo shell]{lang="EN-US"}**[命令禁止了终端服务，那么用户线视图下无法使用]{style="font-family:宋体"}**[shell]{lang="EN-US"}**[启动终端服务。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当设备作为重定向服务器时，如果使用本命令在用户线上禁止了终端服务，则该用户线只能用于重定向服务功能，其它设备无法通过该用户线登录到本设备；如果未禁止终端服务，则该用户线既能用于重定向服务，也能用于终端服务使其它设备通过该用户线登录到本设备，但需要注意的是两者不能同时占用该用户线。]{style="font-family:宋体"}]{#struct_0_18173_18228_x1727906388}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1210768695}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x421636762}[在]{style="font-family:宋体"}[VTY0]{lang="EN-US"}[到]{style="font-family:宋体"}[VTY4]{lang="EN-US"}[上终止终端服务（用户将不能通过]{style="font-family:宋体"}[VTY0-4]{lang="EN-US"}[登录设备）。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_75438182}

[\[Sysname\] line vty 0 4]{lang="EN-US"}

[\[Sysname-line-vty0-4\] undo shell]{lang="EN-US"}

[Disable line-vty0-4 , are you sure? ]{lang="EN-US"}[\[Y/N\]:y]{lang="FR"}

[\[Sysname-line-vty0-4\]]{lang="FR"}
:::

::: {#-738165832 .myid}
[]{#_Toc404782495}[]{#struct_0_18173_18228_x501950413}[]{#_Toc263186427}[]{#_Toc139341900}[]{#_Toc100291522}[]{#_Toc15375249}

**登录设备 \-- 登录设备命令 \-- speed**

------------------------------------------------------------------------

[**[speed]{lang="EN-US"}**]{#struct_0_18173_18228_x1019022907}[命令用来设置用户线的传输速率。]{style="font-family:宋体"}

[**[undo speed]{lang="EN-US"}**]{#struct_0_18173_18228_x856648427}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1688430687}

[**[speed ]{lang="EN-US"}***[speed-value]{lang="EN-US"}*]{#struct_0_18173_18228_x1900363039}

[**[undo speed]{lang="EN-US"}**]{#struct_0_18173_18228_x420627717}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_1639943422}

[[用户线的传输速率为]{style="font-family:宋体"}[9600bps]{lang="EN-US"}]{#struct_0_18173_18228_x88569712}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_1104454395}

[[用户线视图]{style="font-family:宋体"}]{#struct_0_18173_18228_x248056359}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1393601341}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x856648428}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1688496223}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_670177263}

[*[speed-value]{lang="EN-US"}*]{#struct_0_18173_18228_x1962861526}[：传输速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[。异步串口的传输速率有：]{style="font-family:宋体"}[300bps]{lang="EN-US"}[、]{style="font-family:宋体"}[600bps]{lang="EN-US"}[、]{style="font-family:宋体"}[1200bps]{lang="EN-US"}[、]{style="font-family:宋体"}[2400bps]{lang="EN-US"}[、]{style="font-family:宋体"}[4800bps]{lang="EN-US"}[、]{style="font-family:宋体"}[9600bps]{lang="EN-US"}[、]{style="font-family:宋体"}[19200bps]{lang="EN-US"}[、]{style="font-family:宋体"}[38400bps]{lang="EN-US"}[、]{style="font-family:宋体"}[57600bps]{lang="EN-US"}[和]{style="font-family:宋体"}[115200bps]{lang="EN-US"}[。设备对以上速率的支持由产品和配置时的网络环境决定。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1125985790}

[[访问终端和设备相应用户线下传输速率的设置必须一致，双方才能正常通信。]{style="font-family:宋体"}]{#struct_0_18173_18228_x803936534}

[[VTY]{lang="EN-US"}]{#struct_0_18173_18228_592894716}[用户线视图不支持该命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_463580468}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_185805883}[将用户线]{style="font-family:宋体"}[AUX 0]{lang="EN-US"}[的传输速率设置为]{style="font-family:宋体"}[19200bps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_x856648429}

[\[Sysname\] line aux 0]{lang="EN-US"}

[\[Sysname-line-aux0\] speed 19200]{lang="EN-US"}
:::

::::: {#484904218 .myid}
[]{#_Toc404782496}[]{#struct_0_18173_18228_x1688561759}[]{#_Toc263186428}

**登录设备 \-- 登录设备命令 \-- stopbit-error intolerance**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](登录设备命令.files/image002.png){#图片 7 width="63" height="25"}]{lang="EN-US"}]{#struct_0_18173_18228_1641801077}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备型号相关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_18173_18228_1974384495}
:::

**[ ]{lang="EN-US"}**

[**[stopbit-error]{lang="EN-US"}**[ **intolerance**]{lang="EN-US"}]{#struct_0_18173_18228_x454293617}[命令用来检测停止位。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **stopbit-error** **intolerance**]{lang="EN-US"}]{#struct_0_18173_18228_1210684437}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x2135238836}

[**[stopbit-error intolerance]{lang="EN-US"}**]{#struct_0_18173_18228_x856648430}

[**[undo stopbit-error intolerance]{lang="EN-US"}**]{#struct_0_18173_18228_x1687971936}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_x2116976812}

[[不检测停止位。]{style="font-family:宋体"}]{#struct_0_18173_18228_1663954173}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_x775346923}

[[用户线视图]{style="font-family:宋体"}]{#struct_0_18173_18228_205045213}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_1360080865}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_1003705298}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_882993801}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_x856648431}

[[VTY]{lang="EN-US"}]{#struct_0_18173_18228_x1688037472}[用户线视图不支持该命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1625874256}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x196378873}[设置对用户线]{style="font-family:宋体"}[AUX 0]{lang="EN-US"}[检测停止位。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_2009825523}

[\[Sysname\] line aux 0]{lang="EN-US"}

[\[Sysname-line-aux0\] stopbit-error intolerance]{lang="EN-US"}
:::::

::: {#1031263194 .myid}
[]{#_Toc404782497}[]{#struct_0_18173_18228_x708092566}[]{#_Toc263186429}

**登录设备 \-- 登录设备命令 \-- stopbits**

------------------------------------------------------------------------

[**[stopbits]{lang="EN-US"}**]{#struct_0_18173_18228_640223045}[命令用来设置停止位的个数。]{style="font-family:宋体"}

[**[undo stopbits]{lang="EN-US"}**]{#struct_0_18173_18228_x856648432}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1688103008}

[**[stopbits ]{lang="EN-US"}**[{ **1** \| **1.5** \| **2** }]{lang="EN-US"}]{#struct_0_18173_18228_507192929}

[**[undo stopbits]{lang="EN-US"}**]{#struct_0_18173_18228_x2014705278}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_808272749}

[[停止位为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_18173_18228_1101131456}[比特。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_1991088235}

[[用户线视图]{style="font-family:宋体"}]{#struct_0_18173_18228_131183574}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1943903758}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x856648433}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1688168544}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_1117095842}

[**[1]{lang="EN-US"}**]{#struct_0_18173_18228_x1056349446}[：停止位为]{style="font-family:宋体"}[1]{lang="EN-US"}[比特。]{style="font-family:宋体"}

[**[1.5]{lang="EN-US"}**]{#struct_0_18173_18228_450370710}[：停止位为]{style="font-family:宋体"}[1.5]{lang="EN-US"}[比特。目前，设备不支持该参数，配置后实际生效的是命令行]{style="font-family:宋体"}**[stopbits 2]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[2]{lang="EN-US"}**]{#struct_0_18173_18228_1560964380}[：停止位为]{style="font-family:宋体"}[2]{lang="EN-US"}[比特。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1887754984}

[[访问终端和设备相应用户线下停止位的设置必须一致，双方才能正常通信。]{style="font-family:宋体"}]{#struct_0_18173_18228_x843555430}

[[VTY]{lang="EN-US"}]{#struct_0_18173_18228_1602794333}[用户线视图不支持该命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x856648434}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x1688234080}[设置]{style="font-family:宋体"}[AUX]{lang="EN-US"}[用户线的停止位为]{style="font-family:宋体"}[1]{lang="EN-US"}[比特。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_x593360406}

[\[Sysname\] line aux 0]{lang="EN-US"}

[\[Sysname-line-aux0\] stopbits 1]{lang="EN-US"}
:::

::: {#-377527709 .myid}
[]{#_Toc404782498}[]{#struct_0_18173_18228_351806947}[]{#_Toc290553363}

**登录设备 \-- 登录设备命令 \-- telnet**

------------------------------------------------------------------------

[**[telnet]{lang="EN-US"}**]{#struct_0_18173_18228_x1462817574}[命令用于]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[登录到远端设备，以便进行远程管理。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_1419718938}

[**[telnet]{lang="EN-US"}**[ *remote-host* \[ *service-port* \] \[ **vpn-instance** *vpn-instance-name* \] \[ **source** { **interface**  *interface-type interface-number* \| **ip** *ip-address* } \] \[ **dscp** *dscp-value* \]]{lang="EN-US"}]{#struct_0_18173_18228_x2092127841}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_1039079768}

[[用户视图]{style="font-family:宋体"}]{#struct_0_18173_18228_x856648435}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1688299616}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x2084515612}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_625271838}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_x899830955}

[*[remote-host]{lang="EN-US"}*]{#struct_0_18173_18228_891692708}[：远端设备的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址或主机名。其中，主机名为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[253]{lang="EN-US"}[个字符的字符串，不区分大小写，字符串仅可包含字母、数字、"]{style="font-family:宋体"}[-]{lang="EN-US"}["、"]{style="font-family:宋体"}[\_]{lang="EN-US"}["或"]{style="font-family:宋体"}[.]{lang="EN-US"}["。]{style="font-family:宋体"}

[*[service-port]{lang="EN-US"}*]{#struct_0_18173_18228_288920680}[：远端设备提供]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[服务的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[23]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_18173_18228_x1204988955}[：指定远端设备所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示远端设备位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}**]{#struct_0_18173_18228_x856648436}[：指定]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[报文的源接口或源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。如果未指定本参数，则使用路由出接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址作为设备发送的]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_18173_18228_x1688365152}[：指定源接口，发送的]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址为该接口的地址。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。]{style="font-family:
宋体"}

[**[ip]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_18173_18228_1431346800}[：指定]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[dscp-value]{lang="EN-US"}*]{#struct_0_18173_18228_x1708774392}[：]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[客户端向服务器端发送]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[48]{lang="EN-US"}[。]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[携带在]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[字段，用来体现报文自身的优先等级，决定报文传输的优先程度。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_x73041838}

[[FIPS]{lang="EN-US"}]{#struct_0_18173_18228_2145421170}[模式下，不支持本命令。]{style="font-family:宋体"}

[[用户可以使用]{style="font-family:宋体"}[\<Ctrl+K\>]{lang="EN-US"}]{#struct_0_18173_18228_394243187}[组合键或]{style="font-family:宋体"}**[quit]{lang="EN-US"}**[命令来中断本次]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[登录。]{style="font-family:宋体"}

[[需要注意的是，本命令指定的源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_18173_18228_648196212}[地址或源接口只对当前]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[连接有效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x992972452}

[[\# Telnet]{lang="EN-US"}]{#struct_0_18173_18228_1482003733}[登录到远程主机（]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.2]{lang="EN-US"}[），并指定发送]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> telnet 1.1.1.2 source ip 1.1.1.1]{lang="EN-US"}]{#struct_0_18173_18228_1218314968}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x381691982}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[telnet client source]{lang="EN-US"}**]{#struct_0_18173_18228_1279441359}
:::

::: {#1539921408 .myid}
[]{#_Toc404782499}[]{#struct_0_18173_18228_1555808227}[]{#_Toc290553365}[]{#_Toc243714813}

**登录设备 \-- 登录设备命令 \-- telnet client source**

------------------------------------------------------------------------

[**[telnet client source]{lang="EN-US"}**]{#struct_0_18173_18228_1756416226}[命令用来指定设备作为]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[客户端时，发送]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址或源接口。]{style="font-family:宋体"}

[**[undo telnet client source]{lang="EN-US"}**]{#struct_0_18173_18228_1541892332}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_333076890}

[**[telnet client source ]{lang="EN-US"}**[{ **interface** *interface-type interface-number* \| **ip** *ip-address* }]{lang="EN-US"}]{#struct_0_18173_18228_1290383764}

[**[undo telnet client source]{lang="EN-US"}**]{#struct_0_18173_18228_1482003732}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_1218380504}

[[没有指定发送]{style="font-family:宋体"}[Telnet]{lang="EN-US"}]{#struct_0_18173_18228_x720829112}[报文的源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址和源接口，使用报文路由出接口的主]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址作为]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[报文的源地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_x341435569}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18173_18228_906081155}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1385502982}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x608329980}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1204745589}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_1482003731}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_18173_18228_1218446040}[：指定源接口，发送的]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址为该接口的地址。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。]{style="font-family:
宋体"}

[**[ip]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_18173_18228_x1123619373}[：指定发送]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1989789136}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FIPS]{lang="EN-US"}]{#struct_0_18173_18228_2087070402}[模式下，不支持本命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令指定的源]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_18173_18228_x1478661391}[地址或源接口对所有]{lang="EN-US" style="font-family:宋体"}[Telnet]{lang="EN-US"}[连接有效。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若同时使用本命令和]{lang="EN-US" style="font-family:宋体"}**[telnet]{lang="EN-US"}**]{#struct_0_18173_18228_1147172312}[命令指定源]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址或源接口，则以]{lang="EN-US" style="font-family:宋体"}**[telnet]{lang="EN-US"}**[命令指定的源]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址或源接口为准。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_667835010}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x1063905570}[设备作为]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[客户端时，指定发送的]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_1482003730}

[\[Sysname\] telnet client source ip 1.1.1.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_1218511576}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display telnet client configuration]{lang="EN-US"}**]{#struct_0_18173_18228_860393442}
:::

::: {#-732842463 .myid}
[]{#_Toc404782500}[]{#struct_0_18173_18228_x1123217145}[]{#_Toc290553366}

**登录设备 \-- 登录设备命令 \-- telnet ipv6**

------------------------------------------------------------------------

[**[telnet ipv6]{lang="EN-US"}**]{#struct_0_18173_18228_x1978630516}[命令用于]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组网环境下，]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[登录到远程主机，以便进行远程管理。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1951829239}

[**[telnet]{lang="EN-US"}**[ **ipv6** *remote-host* \[ **-i** *interface-type* *interface-number* \] \[ *port-number* \] \[ **vpn-instance** *vpn-instance-name* \] \[ **source** { **interface** *interface-type* *interface-number* \| **ipv6** *ipv6-address* } \] \[ **dscp** *dscp-value* \]]{lang="EN-US"}]{#struct_0_18173_18228_x220368765}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_572696021}

[[用户视图]{style="font-family:宋体"}]{#struct_0_18173_18228_1482003729}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_1218970329}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x328268804}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_2111284622}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1036399924}

[*[remote-host]{lang="EN-US"}*]{#struct_0_18173_18228_424884995}[：远端设备的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址或主机名。其中，主机名为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[253]{lang="EN-US"}[个字符的字符串，不区分大小写，字符串仅可包含字母、数字、"]{style="font-family:宋体"}[-]{lang="EN-US"}["、"]{style="font-family:宋体"}[\_]{lang="EN-US"}["或"]{style="font-family:宋体"}[.]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[-i]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_18173_18228_x1500035365}[：指定]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[报文的出接口。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。当]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[指定的服务端]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址是全球单播地址时，则不能指定该参数；当指定的服务端]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为链路本地地址时，必须指定该参数。]{style="font-family:宋体"}

[*[port-number]{lang="EN-US"}*]{#struct_0_18173_18228_1162120063}[：远端设备提供]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[服务的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[23]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_18173_18228_x1329900625}[：指定远端设备所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示远端设备位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[source]{lang="EN-US" style="color:black"}**]{#struct_0_18173_18228_1012027856}[：指定]{style="font-family:
宋体;color:black"}[Telnet]{lang="EN-US" style="color:black"}[报文的源接口或源]{style="font-family:宋体;color:black"}[IPv6]{lang="EN-US" style="color:black"}[地址。如果未指定本参数，则使用路由出接口的主]{style="font-family:宋体;color:black"}[IPv6]{lang="EN-US" style="color:black"}[地址作为]{style="font-family:宋体;
color:black"}[Telnet]{lang="EN-US" style="color:black"}[报文的源]{style="font-family:宋体;color:black"}[IPv6]{lang="EN-US" style="color:black"}[地址。]{style="font-family:宋体;color:black"}

[**[interface]{lang="EN-US" style="color:black"}**[[ ]{lang="EN-US" style="color:black"}]{.apple-converted-space}*[interface-type interface-number]{lang="EN-US" style="color:black"}*]{#struct_0_18173_18228_x2073069117}[：指定源接口，发送的]{style="font-family:宋体;color:black"}[Telnet]{lang="EN-US" style="color:black"}[报文的源]{style="font-family:宋体;color:black"}[IPv6]{lang="EN-US" style="color:black"}[地址为该接口的主地址。]{style="font-family:宋体;
color:black"}*[interface-type interface-number]{lang="EN-US" style="color:black"}*[为接口类型和接口编号。]{style="font-family:宋体;color:black"}

[**[ipv6]{lang="EN-US" style="color:black"}**[ *ipv6-address*]{lang="EN-US" style="color:black"}]{#struct_0_18173_18228_x334474495}[：指定]{style="font-family:
宋体;color:black"}[Telnet]{lang="EN-US" style="color:black"}[报文的源]{style="font-family:宋体;color:black"}[IPv6]{lang="EN-US" style="color:black"}[地址。]{style="font-family:宋体;color:black"}

[*[dscp-value]{lang="EN-US"}*]{#struct_0_18173_18228_1482003728}[：]{style="font-family:宋体"}[IPv6 Telnet]{lang="EN-US"}[客户端向服务器端发送]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[48]{lang="EN-US"}[。]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[携带在]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[Traffic class]{lang="EN-US"}[字段，用来体现报文自身的优先等级，决定报文传输的优先程度。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_1219035865}

[[FIPS]{lang="EN-US"}]{#struct_0_18173_18228_x365600004}[模式下，不支持本命令。]{style="font-family:宋体"}

[[用户可以使用]{style="font-family:宋体"}[\<Ctrl+K\>]{lang="EN-US"}]{#struct_0_18173_18228_x425123450}[组合键或]{style="font-family:宋体"}**[quit]{lang="EN-US"}**[命令来中断本次]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[登录。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_563371683}

[[\# Telnet]{lang="EN-US"}]{#struct_0_18173_18228_x1593369724}[登录到远程主机，]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[5000::1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> telnet ipv6 5000::1]{lang="EN-US"}]{#struct_0_18173_18228_x771833358}

[[\# Telnet]{lang="EN-US" style="color:black"}]{#struct_0_18173_18228_629690832}[登录到远程主机，]{style="font-family:宋体;color:black"}[IPv6]{lang="EN-US" style="color:black"}[地址为]{style="font-family:宋体;
color:black"}[2000::1]{lang="EN-US" style="color:black"}[，并指定]{style="font-family:宋体;color:black"}[Telnet]{lang="EN-US" style="color:black"}[报文的源]{style="font-family:宋体;color:black"}[IPv6]{lang="EN-US" style="color:black"}[地址为]{style="font-family:宋体;
color:black"}[1000::1]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;color:black"}

[[\<Sysname\> telnet ipv6 2000::1 source ipv6 1000::1]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\";color:black"}]{#struct_0_18173_18228_x1326624304}
:::

::: {#-1424633872 .myid}
[]{#_Toc404782501}[]{#struct_0_18173_18228_819951514}[]{#_Toc290553368}

**登录设备 \-- 登录设备命令 \-- telnet server acl**

------------------------------------------------------------------------

[**[telnet server acl]{lang="EN-US"}**]{#struct_0_18173_18228_x1753821250}[命令用来使用]{style="font-family:宋体"}[ACL]{lang="EN-US"}[（]{style="font-family:宋体"}[Access Controle List]{lang="EN-US"}[，访问控制列表）限制哪些]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[客户端可以访问设备。]{style="font-family:宋体"}

[**[undo telnet server acl]{lang="EN-US"}**]{#struct_0_18173_18228_1482003727}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_1218052825}

[**[telnet server acl ]{lang="EN-US"}***[acl-number]{lang="EN-US"}*]{#struct_0_18173_18228_x1922098191}

[**[undo telnet server acl]{lang="EN-US"}**]{#struct_0_18173_18228_x625982971}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_1629678319}

[[没有使用]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_18173_18228_x660154250}[限制]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[客户端。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_129233703}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18173_18228_1875037550}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_1482003726}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_1218118361}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_32811488}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_500155036}

[*[acl-number]{lang="EN-US"}*]{#struct_0_18173_18228_x1727392947}[：]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围及其代表的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2000]{lang="EN-US"}]{#struct_0_18173_18228_51193604}[～]{lang="EN-US" style="font-family:宋体"}[2999]{lang="EN-US"}[：表示]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3000]{lang="EN-US"}]{#struct_0_18173_18228_1770321127}[～]{lang="EN-US" style="font-family:宋体"}[3999]{lang="EN-US"}[：表示]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[高级]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4000]{lang="EN-US"}]{#struct_0_18173_18228_x1120812916}[～]{lang="EN-US" style="font-family:宋体"}[4999]{lang="EN-US"}[：表示二层]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_1490082768}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当未引用]{style="font-family:宋体"}]{#struct_0_18173_18228_1482003725}[ACL]{lang="EN-US"}[、或者引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在、或者引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[为空时，允许所有登录用户访问设备；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当引用的]{style="font-family:宋体"}]{#struct_0_18173_18228_1218183897}[ACL]{lang="EN-US"}[非空时，则只有]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中]{style="font-family:宋体"}[permit]{lang="EN-US"}[的用户才能访问设备，其它用户不允许访问设备，以免非法用户使用]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[访问设备。]{style="font-family:宋体"}

[[关于]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_18173_18228_x362109138}[的详细描述和介绍请参见"]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{style="font-family:宋体"}[QoS]{lang="EN-US"}[配置指导"中的"]{style="font-family:宋体"}[ACL]{lang="EN-US"}["。]{style="font-family:宋体"}

[[该配置只过滤新建立的]{style="font-family:宋体"}[Telnet]{lang="EN-US"}]{#struct_0_18173_18228_x1061359485}[连接，不会对已建立的]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[连接和操作造成影响。]{style="font-family:宋体"}

[[如果多次使用该命令配置]{style="font-family:宋体"}[Telnet]{lang="EN-US"}]{#struct_0_18173_18228_1468776223}[服务与]{style="font-family:宋体"}[ACL]{lang="EN-US"}[关联，最新配置生效。]{style="font-family:宋体"}

[[FIPS]{lang="EN-US"}]{#struct_0_18173_18228_x1463152881}[模式下，不支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_1904527989}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_686719264}[仅允许地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[的用户通过]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[访问本设备。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_1482003724}

[\[Sysname\] acl basic 2001]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2001\] rule permit source 1.1.1.1 0]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2001\] quit]{lang="EN-US"}

[\[Sysname\] telnet server acl 2001]{lang="EN-US"}
:::

::: {#873498860 .myid}
[]{#_Toc404782502}[]{#struct_0_18173_18228_1218249433}[]{#_Toc337719105}

**登录设备 \-- 登录设备命令 \-- telnet server dscp**

------------------------------------------------------------------------

[**[telnet server dscp]{lang="EN-US"}**]{#struct_0_18173_18228_x1128712799}[命令用来配置]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[服务器发送]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[**[undo telnet server dscp]{lang="EN-US"}**]{#struct_0_18173_18228_287241905}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_1889931156}

[**[telnet server dscp ]{lang="EN-US"}***[dscp-value]{lang="EN-US"}*]{#struct_0_18173_18228_787081963}

[**[undo telnet server dscp]{lang="EN-US"}**]{#struct_0_18173_18228_475136787}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_1167056812}

[[Telnet]{lang="EN-US"}]{#struct_0_18173_18228_693047149}[服务器发送]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[48]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_x89811691}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18173_18228_1655770841}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_x433118037}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_1597146855}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1483980346}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_x516787909}

[*[dscp-value]{lang="EN-US"}*]{#struct_0_18173_18228_285755226}[：]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[。]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[携带在]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[字段，用来体现报文自身的优先等级，决定报文传输的优先程度。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_728182655}

[[FIPS]{lang="EN-US"}]{#struct_0_18173_18228_710690861}[模式下不支持该命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x89811692}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_1655770838}[配置]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[服务器发送报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_x433707860}

[\[Sysname\] telnet server dscp 30]{lang="EN-US"}
:::

::: {#-1509288542 .myid}
[]{#_Toc404782503}[]{#struct_0_18173_18228_116425955}[]{#_Toc290553367}[]{#_Toc263186432}[]{#_Toc252354511}

**登录设备 \-- 登录设备命令 \-- telnet server enable**

------------------------------------------------------------------------

[**[telnet server enable]{lang="EN-US"}**]{#struct_0_18173_18228_100410324}[命令用来使能]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[服务。]{style="font-family:宋体"}

[**[undo telnet server enable]{lang="EN-US"}**]{#struct_0_18173_18228_1170714420}[命令用来关闭]{style="font-family:
宋体"}[Telnet]{lang="EN-US"}[服务。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_1256326932}

[**[telnet server enable]{lang="EN-US"}**]{#struct_0_18173_18228_x1820431979}

[**[undo telnet server enable]{lang="EN-US"}**]{#struct_0_18173_18228_x89811693}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_1655770839}

[[Telnet]{lang="EN-US"}]{#struct_0_18173_18228_x433642324}[服务处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_x306787319}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18173_18228_x2088612009}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_450619205}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1422777012}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1041128596}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1673038003}

[[FIPS]{lang="EN-US"}]{#struct_0_18173_18228_x89811694}[模式下，不支持本命令。]{style="font-family:宋体"}

[[只有使能]{style="font-family:宋体"}[Telnet]{lang="EN-US"}]{#struct_0_18173_18228_1655770836}[服务后，才允许网络管理员通过]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[协议登录设备。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x433314644}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x702541878}[使能]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[服务。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_275736034}

[\[Sysname\] telnet server enable]{lang="EN-US"}
:::

::: {#-542144234 .myid}
[]{#_Toc404782504}[]{#struct_0_18173_18228_x1593894936}

**登录设备 \-- 登录设备命令 \-- telnet server ipv6 acl**

------------------------------------------------------------------------

[**[telnet server ]{lang="EN-US"}[ipv6 acl]{lang="EN-US"}**]{#struct_0_18173_18228_1794591521}[命令用来使用]{style="font-family:宋体"}[ACL]{lang="EN-US"}[限制哪些]{style="font-family:宋体"}[IPv6 Telnet]{lang="EN-US"}[客户端可以访问设备。]{style="font-family:宋体"}

[**[undo telnet server ]{lang="EN-US"}[ipv6 acl]{lang="EN-US"}**]{#struct_0_18173_18228_x699341968}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x89811695}

[**[telnet server ipv6 acl ]{lang="EN-US"}**[\[ **ipv6** \] *acl-number*]{lang="EN-US"}]{#struct_0_18173_18228_1655770837}

[**[undo telnet server ipv6 acl]{lang="EN-US"}**]{#struct_0_18173_18228_x433249108}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_834277934}

[[没有使用]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_18173_18228_315324107}[限制]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[客户端。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1704810577}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18173_18228_x1072470349}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1771882553}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_905477160}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_x89811696}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_1655770834}

[*[acl-number]{lang="EN-US"}*]{#struct_0_18173_18228_x433445716}[：]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围及其代表的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2000]{lang="EN-US"}]{#struct_0_18173_18228_x1464558709}[～]{lang="EN-US" style="font-family:宋体"}[2999]{lang="EN-US"}[：需指定]{lang="EN-US" style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[关键字，表示]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3000]{lang="EN-US"}]{#struct_0_18173_18228_x703434837}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[：需指定]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[关键字，表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4000]{lang="EN-US"}]{#struct_0_18173_18228_654230480}[～]{lang="EN-US" style="font-family:宋体"}[4999]{lang="EN-US"}[：表示二层]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_x900705471}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当未引用]{style="font-family:宋体"}]{#struct_0_18173_18228_x264882037}[ACL]{lang="EN-US"}[、或者引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在、或者引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[为空时，允许所有登录用户访问设备；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当引用的]{style="font-family:宋体"}]{#struct_0_18173_18228_146213631}[ACL]{lang="EN-US"}[非空时，则只有]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中]{style="font-family:宋体"}[permit]{lang="EN-US"}[的用户才能访问设备，其它用户不允许访问设备，以免非法用户使用]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[访问设备。]{style="font-family:宋体"}

[[关于]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_18173_18228_x89811697}[的详细描述和介绍请参见"]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{style="font-family:宋体"}[QoS]{lang="EN-US"}[配置指导"中的"]{style="font-family:宋体"}[ACL]{lang="EN-US"}["。]{style="font-family:宋体"}

[[该配置只过滤新建立的]{style="font-family:宋体"}[Telnet]{lang="EN-US"}]{#struct_0_18173_18228_1655770835}[连接，不会对已建立的]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[连接和操作造成影响。]{style="font-family:宋体"}

[[如果多次使用该命令配置]{style="font-family:宋体"}[Telnet]{lang="EN-US"}]{#struct_0_18173_18228_x433380180}[服务与]{style="font-family:宋体"}[ACL]{lang="EN-US"}[关联，最新配置生效。]{style="font-family:宋体"}

[[FIPS]{lang="EN-US"}]{#struct_0_18173_18228_x1119755718}[模式下，不支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1763622553}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_838203828}[仅允许地址为]{style="font-family:宋体"}[2000::1]{lang="EN-US"}[的用户通过]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[访问本设备。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_x89811698}

[\[Sysname\] acl ipv6 basic 2001]{lang="EN-US"}

[\[Sysname-acl6-ipv6-basic-2001\] rule permit source 2000::1 128]{lang="EN-US"}

[\[Sysname-acl6-ipv6-basic-2001\] quit]{lang="EN-US"}

[\[Sysname\] telnet server ipv6 acl ipv6 2001]{lang="EN-US"}
:::

::: {#893870237 .myid}
[]{#_Toc404782505}[]{#struct_0_18173_18228_1655770832}[]{#_Toc337719106}

**登录设备 \-- 登录设备命令 \-- telnet server ipv6 dscp**

------------------------------------------------------------------------

[**[telnet server ipv6 dscp]{lang="EN-US"}**]{#struct_0_18173_18228_x433052500}[命令用来配置]{style="font-family:宋体"}[IPv6 Telnet]{lang="EN-US"}[服务器发送报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **telnet server ipv6 dscp**]{lang="EN-US"}]{#struct_0_18173_18228_837929701}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1813604902}

[**[telnet server ipv6 dscp ]{lang="EN-US"}***[dscp-value]{lang="EN-US"}*]{#struct_0_18173_18228_x214759911}

[**[undo telnet server ipv6 dscp]{lang="EN-US"}**]{#struct_0_18173_18228_x422640898}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_1928266145}

[[IPv6 Telnet]{lang="EN-US"}]{#struct_0_18173_18228_2031176432}[服务器发送]{style="font-family:宋体"}[IPv6 Telnet]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[48]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_x89811699}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18173_18228_1655770833}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_x432986964}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_81131964}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_x966598810}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_2125298766}

[*[dscp-value]{lang="EN-US"}*]{#struct_0_18173_18228_x576664593}[：]{style="font-family:宋体"}[IPv6 Telnet]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[。]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[携带在]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[Traffic class]{lang="EN-US"}[字段，用来体现报文自身的优先等级，决定报文传输的优先程度。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_1366742325}

[[FIPS]{lang="EN-US"}]{#struct_0_18173_18228_x1344324445}[模式下不支持该命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x593228571}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x89811700}[配置]{style="font-family:宋体"}[IPv6 Telnet]{lang="EN-US"}[服务器发送的报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_x646145475}

[\[Sysname\] telnet server ipv6 dscp 30]{lang="EN-US"}
:::

::: {#579348375 .myid}
[]{#_Toc404782506}[]{#struct_0_18173_18228_441823990}

**登录设备 \-- 登录设备命令 \-- terminal type**

------------------------------------------------------------------------

[**[terminal type]{lang="EN-US"}**]{#struct_0_18173_18228_x930471775}[命令用来设置当前用户线下的终端显示类型。]{style="font-family:宋体"}

[**[undo terminal type]{lang="EN-US"}**]{#struct_0_18173_18228_x775918083}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_230317587}

[**[terminal type]{lang="EN-US"}**[ { **ansi** \| **vt100** }]{lang="EN-US"}]{#struct_0_18173_18228_x616997368}

[**[undo terminal type]{lang="EN-US"}**]{#struct_0_18173_18228_x2024192102}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_x2046126827}

[[终端显示类型为]{style="font-family:宋体"}[ANSI]{lang="EN-US"}]{#struct_0_18173_18228_x1374026878}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1584949851}

[[用户线视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18173_18228_x686155439}[用户线类视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_x380728466}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_530620467}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_x920132211}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_244640268}

[**[ansi]{lang="EN-US"}**]{#struct_0_18173_18228_x611168613}[：终端显示类型为]{style="font-family:宋体"}[ANSI]{lang="EN-US"}[类型。]{style="font-family:宋体"}

[**[vt100]{lang="EN-US"}**]{#struct_0_18173_18228_x2046126828}[：终端显示类型为]{style="font-family:宋体"}[VT100]{lang="EN-US"}[类型。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_548287423}

[[设备支持]{style="font-family:宋体"}[ANSI]{lang="EN-US"}]{#struct_0_18173_18228_407385971}[和]{style="font-family:宋体"}[VT100]{lang="EN-US"}[两种终端显示类型。当设备的终端类型与客户端（如超级终端或者]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[客户端等）的终端类型不一致，或者均设置为]{style="font-family:宋体"}[ANSI]{lang="EN-US"}[时，并且当前编辑行的总字符数超过]{style="font-family:宋体"}[80]{lang="EN-US"}[个字符时，客户端会出现光标错位、终端屏幕不能正常显示的现象。建议两端都设置为]{style="font-family:宋体"}[VT100]{lang="EN-US"}[类型。]{style="font-family:宋体"}

[[需要注意的是，用户线视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18173_18228_761961736}[用户线类视图下配置的终端显示类型都在下次登录时生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_207226154}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x991710299}[设置终端显示类型为]{style="font-family:宋体"}[VT100]{lang="EN-US"}[类型。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_472262225}

[\[Sysname\] line vty 0]{lang="EN-US"}

[[\[Sysname-line-vty0\] terminal type vt100]{lang="EN-US"}]{#struct_0_18173_18228_x2046126830}
:::

::: {#634700465 .myid}
[]{#_Toc404782507}[]{#struct_0_18173_18228_192122599}

**登录设备 \-- 登录设备命令 \-- user-interface**

------------------------------------------------------------------------

[**[user-interface]{lang="EN-US"}**]{#struct_0_18173_18228_1079629384}[命令用来进入一个或多个用户线视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x2046126831}

[**[user-interface]{lang="EN-US"}**[ { *first-number1* \[ *last-number1* \] \| { **aux** \| **console** \| **tty** \| **vty** } *first-number2* \[ *last-number2* \] }]{lang="EN-US"}]{#struct_0_18173_18228_1758206540}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_x957126220}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18173_18228_x1799539102}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_x456332377}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x2031744775}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1474094136}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_x705039102}

[*[first-number1]{lang="EN-US"}*]{#struct_0_18173_18228_872024560}[：第一个用户线的编号（绝对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准，一般从]{style="font-family:宋体"}[0]{lang="EN-US"}[开始。]{style="font-family:宋体"}

[*[last-number1]{lang="EN-US"}*]{#struct_0_18173_18228_x2046126832}[：最后一个用户线的编号（绝对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准，一般从]{style="font-family:宋体"}[0]{lang="EN-US"}[开始，但不能小于]{style="font-family:宋体"}*[first-number1]{lang="EN-US"}*[。]{style="font-family:宋体"}

[**[aux]{lang="EN-US"}**]{#struct_0_18173_18228_x970676815}[：]{style="font-family:宋体"}[AUX]{lang="EN-US"}[用户线。]{style="font-family:宋体"}

[**[console]{lang="EN-US"}**]{#struct_0_18173_18228_x2139242910}[：]{style="font-family:宋体"}[Console]{lang="EN-US"}[用户线。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[tty]{lang="EN-US"}**]{#struct_0_18173_18228_x176240760}[：]{style="font-family:宋体"}[TTY]{lang="EN-US"}[用户线。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vty]{lang="EN-US"}**]{#struct_0_18173_18228_x312868393}[：]{style="font-family:宋体"}[VTY]{lang="EN-US"}[用户线。]{style="font-family:宋体"}

[*[first-number2]{lang="EN-US"}*]{#struct_0_18173_18228_x539723776}[：第一个用户线的编号（相对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[last-number2]{lang="EN-US"}*]{#struct_0_18173_18228_x2116004015}[：最后一个用户线的编号（相对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准，但不能小于]{style="font-family:宋体"}*[first-number2]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_808339871}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[进入一个用户线视图进行配置后，该配置只对该用户视图有效。]{style="font-family:宋体"}]{#struct_0_18173_18228_729738371}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[进入多个用户线视图进行配置后，该配置对这些用户视图均有效。]{style="font-family:宋体"}]{#struct_0_18173_18228_x2046126833}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令实现与]{style="font-family:宋体"}]{#struct_0_18173_18228_595407126}**[line]{lang="EN-US"}**[一致，仅为与旧版本兼容保留，请使用]{style="font-family:宋体"}**[line]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x2099470480}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_1208999333}[进入]{style="font-family:宋体"}[Console 0]{lang="EN-US"}[用户线视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_1440300085}

[\[Sysname\] user-interface console 0]{lang="EN-US"}

[\[Sysname-line-console0\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x1395899407}[进入]{style="font-family:宋体"}[VTY 0]{lang="EN-US"}[～]{style="font-family:宋体"}[4]{lang="EN-US"}[用户线视图。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_1357833257}

[\[Sysname\] user-interface vty 0 4]{lang="EN-US"}

[\[Sysname-line-vty0-4\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x2046126834}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[user-interface class]{lang="EN-US"}**]{#struct_0_18173_18228_x2046126836}
:::

::: {#1985466109 .myid}
[]{#_Toc273364318}[]{#_Toc259625765}[]{#_Toc139341903}[]{#_Toc100291524}[]{#_Toc15375243}[]{#_Toc404782508}[]{#struct_0_18173_18228_1354922013}

**登录设备 \-- 登录设备命令 \-- user-interface class**

------------------------------------------------------------------------

[**[user-interface class]{lang="EN-US"}**]{#struct_0_18173_18228_x790283595}[命令用来进入指定用户线类视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_374130602}

[**[user-interface class ]{lang="EN-US"}**[{ **aux** \| **console** \| **tty** \| **vty** }]{lang="EN-US"}]{#struct_0_18173_18228_x160661678}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_292525333}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18173_18228_x1589803795}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1874523135}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1662114802}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_x57452905}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_1162864879}

[**[aux]{lang="EN-US"}**]{#struct_0_18173_18228_x542956235}[：]{style="font-family:宋体"}[AUX]{lang="EN-US"}[用户线类。]{style="font-family:宋体"}

[**[console]{lang="EN-US"}**]{#struct_0_18173_18228_x146188783}[：]{style="font-family:宋体"}[Console]{lang="EN-US"}[用户线类。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[tty]{lang="EN-US"}**]{#struct_0_18173_18228_x986991205}[：]{style="font-family:宋体"}[TTY]{lang="EN-US"}[用户线类。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vty]{lang="EN-US"}**]{#struct_0_18173_18228_1933556202}[：]{style="font-family:宋体"}[VTY]{lang="EN-US"}[用户线类。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_292525332}

[**[user-interface class]{lang="EN-US"}**]{#struct_0_18173_18228_x1589803796}[命令用来进入指定用户线类视图，]{style="font-family:宋体"}**[user-interface]{lang="EN-US"}**[命令用来进入一个或多个用户线视图。对于同时支持这两种视图的命令：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户线视图下的配置优先于用户线类视图下的配置。]{style="font-family:宋体"}]{#struct_0_18173_18228_x2064196654}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户线视图下的配置只对该用户线生效。]{style="font-family:宋体"}]{#struct_0_18173_18228_x2064131118}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户线类视图下的配置修改不会立即生效，当用户下次登录后所修改的配置值才会生效。]{style="font-family:宋体"}]{#struct_0_18173_18228_2071779018}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户线视图下的属性配置为缺省值时，将采用用户线类视图下配置的值。如果用户线类视图下的属性配置也为缺省值时，则直接采用该属性的缺省值。]{style="font-family:宋体"}]{#struct_0_18173_18228_1890914035}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令实现与]{lang="EN-US" style="font-family:宋体"}**[line class]{lang="EN-US"}**]{#struct_0_18173_18228_758922349}[一致，仅为与旧版本兼容保留，请使用]{lang="EN-US" style="font-family:宋体"}**[line class]{lang="EN-US"}**[。]{lang="EN-US" style="font-family:宋体"}

[[用户线类视图下]{style="font-family:宋体"}]{#struct_0_18173_18228_206563607}[支持的命令有：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[activation-key]{lang="EN-US"}**]{#struct_0_18173_18228_x884735182}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[auto-execute command]{lang="EN-US"}**]{#struct_0_18173_18228_1844874268}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication-mode]{lang="EN-US"}**]{#struct_0_18173_18228_292525331}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[command accounting]{lang="EN-US"}**]{#struct_0_18173_18228_x1589803793}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[command authorization]{lang="EN-US"}**]{#struct_0_18173_18228_x1067954081}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[escape-key]{lang="EN-US"}**]{#struct_0_18173_18228_1944776029}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[history-command max-size]{lang="EN-US"}**]{#struct_0_18173_18228_516917205}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[idle-timeout]{lang="EN-US"}**]{#struct_0_18173_18228_1736387548}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[protocol inbound]{lang="EN-US"}**]{#struct_0_18173_18228_x130042000}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[screen-length]{lang="EN-US"}**]{#struct_0_18173_18228_1420544741}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[set authentication password]{lang="EN-US"}**]{#struct_0_18173_18228_2056347853}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[shell]{lang="EN-US"}**]{#struct_0_18173_18228_292525330}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[terminal type]{lang="EN-US"}**]{#struct_0_18173_18228_x1589803794}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[user-role]{lang="EN-US"}**]{#struct_0_18173_18228_x308439194}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_1621297884}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x452739202}[将]{style="font-family:宋体"}[VTY]{lang="EN-US"}[用户线参数------用户连接的超时时间的缺省值设置为]{style="font-family:宋体"}[15]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_x1820646679}

[\[Sysname\] user-interface class vty]{lang="EN-US"}

[\[Sysname-line-class-vty\] idle-timeout 15]{lang="EN-US"}

[[\#]{lang="EN-US"}]{#struct_0_18173_18228_x1567762146}[在]{style="font-family:宋体"}[console]{lang="EN-US"}[用户线类视图下，将启动]{style="font-family:宋体"}[Console]{lang="EN-US"}[口终端会话的快捷键设置为]{style="font-family:宋体"}[\<s\>]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_292525329}

[\[Sysname\] user-interface class console]{lang="EN-US"}

[\[Sysname-line-class-console\] activation-key s]{lang="EN-US"}

[\[Sysname-line-class-console\] quit]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{lang="EN-US" style="font-family:宋体"}[console]{lang="EN-US"}]{#struct_0_18173_18228_748848375}[用户线视图下，将启动]{lang="EN-US" style="font-family:宋体"}[Console]{lang="EN-US"}[口终端会话的快捷键设置为缺省值]{lang="EN-US" style="font-family:宋体"}[（]{style="font-family:
宋体"}[可以使用]{lang="EN-US" style="font-family:宋体"}[undo activation-key]{lang="EN-US"}[或者直接使用]{lang="EN-US" style="font-family:宋体"}[activation-key 13]{lang="EN-US"}[进行配置]{lang="EN-US" style="font-family:宋体"}[）]{style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[\[Sysname\] line console 0]{lang="EN-US"}]{#struct_0_18173_18228_1567025256}

[\[Sysname-line-console0\] undo activation-key]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[此时生效的快捷键为用户线类视图下的配置，验证过程如下：]{style="font-family:宋体"}]{#struct_0_18173_18228_81566423}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[退出]{lang="EN-US" style="font-family:宋体"}[Console]{lang="EN-US"}]{#struct_0_18173_18228_2146315493}[口终端会话。]{lang="EN-US" style="font-family:宋体"}

[[\[Sysname-line-console0\] return]{lang="EN-US"}]{#struct_0_18173_18228_645126376}

[\<Sysname\> quit]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重新使用]{style="font-family:宋体"}]{#struct_0_18173_18228_x1624135301}[Console]{lang="EN-US"}[口登录设备，能看到如下显示信息。]{style="font-family:宋体"}

[[Press ENTER to get started.]{lang="EN-US"}]{#struct_0_18173_18228_x1058963966}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[此时，]{style="font-family:宋体"}]{#struct_0_18173_18228_1697898321}[\<Enter\>]{lang="EN-US"}[键失效，需要按]{style="font-family:宋体"}[\<s\>]{lang="EN-US"}[键才能出现用户视图提示符，启动]{style="font-family:宋体"}[Console]{lang="EN-US"}[口终端会话。]{style="font-family:宋体"}

[[\<Sysname\>]{lang="EN-US"}]{#struct_0_18173_18228_292525328}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_748848374}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[user-interface]{lang="EN-US"}**]{#struct_0_18173_18228_1567025257}
:::

::: {#1580969545 .myid}
[]{#_Toc404782509}[]{#struct_0_18173_18228_81631959}

**登录设备 \-- 登录设备命令 \-- user-role**

------------------------------------------------------------------------

[**[user-role]{lang="EN-US"}**]{#struct_0_18173_18228_436440030}[命令用来配置从当前用户线登录系统的用户角色。]{style="font-family:宋体"}

[**[undo user-role]{lang="EN-US"}**]{#struct_0_18173_18228_743784269}[命令用来删除指定的用户角色配置或者恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_1799349706}

[**[user-role]{lang="EN-US"}**[ *role-name*]{lang="EN-US"}]{#struct_0_18173_18228_x954187940}

[**[undo]{lang="EN-US"}**[ **user-role** \[ *role-name* \]]{lang="EN-US"}]{#struct_0_18173_18228_292525327}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_748848361}

[[通过]{style="font-family:宋体"}[Console]{lang="EN-US"}]{#struct_0_18173_18228_x771626900}[口登录系统的用户角色为]{style="font-family:宋体"}[network-admin]{lang="EN-US"}[，通过其它接口登录系统的用户角色为]{style="font-family:宋体"}[network-operator]{lang="EN-US"}[。（不支持]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[对于缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_18173_18228_x326386078}[，通过]{style="font-family:宋体"}[Console]{lang="EN-US"}[口登录系统的用户角色为]{style="font-family:宋体"}[network-admin]{lang="EN-US"}[，通过其它接口登录系统的用户角色为]{style="font-family:宋体"}[network-operator]{lang="EN-US"}[。对于非缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[，通过]{style="font-family:宋体"}**[switchto mdc]{lang="EN-US"}**[命令登录用户的缺省角色为]{style="font-family:宋体"}[mdc-admin]{lang="EN-US"}[，其它登录用户的缺省角色均为]{style="font-family:宋体"}[mdc-operator]{lang="EN-US"}[（支持]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1556539448}

[[用户线视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18173_18228_1383310194}[用户线类视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_362772366}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1217754793}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1904928245}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_292525326}

[*[role-name]{lang="EN-US"}*]{#struct_0_18173_18228_748848360}[：用户角色名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。可以是系统预定义的角色名称，包括]{style="font-family:宋体"}[network-admin]{lang="EN-US"}[、]{style="font-family:宋体"}[network-operator]{lang="EN-US"}[、]{style="font-family:宋体"}[mdc-admin]{lang="EN-US"}[、]{style="font-family:宋体"}[mdc-operator]{lang="EN-US"}[、]{style="font-family:宋体"}[level-0]{lang="EN-US"}[～]{style="font-family:宋体"}[level-15]{lang="EN-US"}[，也可以是自定义的用户角色名称。不指定该参数时，表示恢复到缺省情况。由于系统预定义角色]{style="font-family:宋体"}[security-audit]{lang="EN-US"}[只能在]{style="font-family:宋体"}[local-user]{lang="EN-US"}[视图下进行配置，所以该参数不能指定为]{style="font-family:宋体"}[security-audit]{lang="EN-US"}[角色，否则会弹出错误提示信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_x771626899}

[[FIPS]{lang="EN-US"}]{#struct_0_18173_18228_2012855915}[模式下，不支持本命令。]{style="font-family:宋体"}

[[可通过多次执行本命令，配置多个用户角色，最多可配置]{style="font-family:宋体"}[64]{lang="EN-US"}]{#struct_0_18173_18228_1421956462}[个。用户登录后具有的权限是这些角色权限的集合。]{style="font-family:宋体"}

[[在用户线视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18173_18228_x797860223}[用户线类视图下使用该命令设置的用户角色将在下次登录设备时生效。]{style="font-family:宋体"}

[[关于用户角色的详细介绍请参见"基础配置指导"中的"]{style="font-family:宋体"}[RBAC]{lang="EN-US"}]{#struct_0_18173_18228_2045004165}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x159619857}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_1320166155}[设置从]{style="font-family:宋体"}[AUX]{lang="EN-US"}[用户线登录系统的用户角色为]{style="font-family:宋体"}[network-admin]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_292525325}

[\[Sysname\] line aux 0]{lang="EN-US"}

[\[Sysname-line-aux0\] user-role ]{lang="FR"}[network-admin]{lang="EN-US"}
:::

::::: {#-494832065 .myid}
[]{#_Toc347480797}[]{#_Toc404782510}[]{#struct_0_18173_18228_748848363}

**登录设备 \-- 登录设备命令 \-- web captcha**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](登录设备命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_18173_18228_x771626902}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_18173_18228_292525324}
:::

[ ]{lang="EN-US"}

[**[web captcha]{lang="EN-US"}**]{#struct_0_18173_18228_748848362}[命令用来配置用户访问]{style="font-family:宋体"}[Web]{lang="EN-US"}[的固定校验码。]{style="font-family:宋体"}

[**[undo web captcha]{lang="EN-US"}**]{#struct_0_18173_18228_x1663789803}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1734451984}

[**[web captcha]{lang="EN-US"}**[ *verification-code*]{lang="EN-US"}]{#struct_0_18173_18228_x1904525412}

[**[undo web captcha]{lang="EN-US"}**]{#struct_0_18173_18228_x1663789804}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_638201011}

[[用户只能使用]{style="font-family:宋体"}[Web]{lang="EN-US"}]{#struct_0_18173_18228_x1663789805}[页面显示的校验码访问]{style="font-family:宋体"}[Web]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_x927882930}

[[用户视图]{style="font-family:宋体"}]{#struct_0_18173_18228_x1663789806}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_1801000425}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x30465044}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1663789807}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_234916484}

[*[verification-code]{lang="EN-US"}*]{#struct_0_18173_18228_x1663789808}[：访问]{style="font-family:宋体"}[Web]{lang="EN-US"}[的固定校验码，为]{style="font-family:宋体"}[4]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_18173_18228_x974937097}

[[配置该命令后，不管]{style="font-family:宋体"}[Web]{lang="EN-US"}]{#struct_0_18173_18228_1498696180}[登录页面显示的校验码是什么，用户只要输入该固定的校验码，即可访问设备。本命令主要用于测试环境，当需要对设备的]{style="font-family:宋体"}[Web]{lang="EN-US"}[功能进行测试时，可以配置一个固定的校验码，使用脚本即可登录设备，以免每次测试都要手工输入变化的校验码，影响测试效率。]{style="font-family:宋体"}

[[设备在网络中正常使用的时候，建议不要配置该命令，以免降低]{style="font-family:宋体"}[Web]{lang="EN-US"}]{#struct_0_18173_18228_x1663789809}[访问的安全性。]{style="font-family:宋体"}

[[多次配置该命令，最新配置生效。]{style="font-family:宋体"}]{#struct_0_18173_18228_1753946258}

[[该命令不能保存到配置文件，设备重启后失效。]{style="font-family:宋体"}]{#struct_0_18173_18228_x1663789810}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1331232993}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x1663789811}[设置访问]{style="font-family:宋体"}[Web]{lang="EN-US"}[的固定校验码为]{style="font-family:宋体"}[test]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> web captcha test]{lang="EN-US"}]{#struct_0_18173_18228_1397650362}
:::::

::: {#-912002969 .myid}
[]{#_Toc404782511}[]{#struct_0_18173_18228_1828739173}

**登录设备 \-- 登录设备命令 \-- web https-authorization mode**

------------------------------------------------------------------------

[**[web https-authorization mode]{lang="EN-US"}**]{#struct_0_18173_18228_x2095100679}[命令用来设置使用]{style="font-family:
宋体"}[HTTPS]{lang="EN-US"}[登录设备的认证模式。]{style="font-family:宋体"}

[**[undo web https-authorization mode]{lang="EN-US"}**]{#struct_0_18173_18228_711249587}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1138734971}

[**[web]{lang="EN-US"}**[ **https-authorization mode** { **auto** \| **manual** }]{lang="EN-US"}]{#struct_0_18173_18228_x1663789812}

[**[undo]{lang="EN-US"}**[ **web** **https-authorization** **mode**]{lang="EN-US"}]{#struct_0_18173_18228_x168433579}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_967278362}

[[使用]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}]{#struct_0_18173_18228_2077214566}[登录设备的认证模式为]{style="font-family:宋体"}[manual]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_718994090}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18173_18228_x1131651371}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_x123178816}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1169971794}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_x543351472}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_x854485739}

[**[auto]{lang="EN-US"}**]{#struct_0_18173_18228_x1091916925}**[：]{style="font-family:宋体"}**[表示用户通过]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[登录设备时，使用客户端的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[证书自动认证登录。]{style="font-family:宋体"}

[**[manual]{lang="EN-US"}**]{#struct_0_18173_18228_2079944435}**[：]{style="font-family:宋体"}**[表示用户通过]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[登录设备时，设备给出登录页面，用户必须输入合法的用户名和密码后才能登录。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_x646055514}

[[当选用]{style="font-family:宋体"}]{#struct_0_18173_18228_x1516457319}**[auto]{lang="EN-US"}**[认证模式时，设备客户端的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[证书自动认证登录：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当用户侧的证书正确且未超期，则读取证书中的]{style="font-family:宋体"}]{#struct_0_18173_18228_x74976273}[CN]{lang="EN-US"}[字段作为用户名，进行]{style="font-family:宋体"}[AAA]{lang="EN-US"}[认证。如果认证成功，则自动进入设备的]{style="font-family:宋体"}[Web]{lang="EN-US"}[界面；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当用户侧的证书有效且未超期，但]{style="font-family:宋体"}]{#struct_0_18173_18228_832383031}[AAA]{lang="EN-US"}[认证失败，则回到登录界面（如果此时用户输入合法的用户名和密码仍然能够登录）；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当用户侧的证书错误或超期，则断开]{style="font-family:宋体"}]{#struct_0_18173_18228_1435848306}[HTTPS]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x81020693}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x854485740}[设置]{style="font-family:宋体"}[Web]{lang="EN-US"}[的]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[认证模式为]{style="font-family:宋体"}[auto]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_x1091327098}

[\[Sysname\] web https-authorization mode auto]{lang="EN-US"}
:::

::::: {#-1890397601 .myid}
[]{#_Toc404782512}[]{#_Toc319416210}[]{#struct_0_18173_18228_x238669070}

**登录设备 \-- 登录设备命令 \-- web idle-timeout**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](登录设备命令.files/image003.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_18173_18228_x642116845}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_18173_18228_x1995549404}
:::

**[ ]{lang="EN-US"}**

[**[web idle-timeout]{lang="EN-US"}**]{#struct_0_18173_18228_x854485741}[命令用来设置]{style="font-family:宋体"}[Web]{lang="EN-US"}[闲置超时时间。]{style="font-family:宋体"}

[**[undo web idle-timeout]{lang="EN-US"}**]{#struct_0_18173_18228_x1091392634}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_2002467377}

[**[web]{lang="EN-US"}**[ **idle-timeout** *idle-time*]{lang="EN-US"}]{#struct_0_18173_18228_2026862013}

[**[undo]{lang="EN-US"}**[ **web** **idle-timeout**]{lang="EN-US"}]{#struct_0_18173_18228_1125453710}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1327918804}

[[Web]{lang="EN-US"}]{#struct_0_18173_18228_932971112}[闲置超时时间为]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_1390069284}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18173_18228_x502644942}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1924479981}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x854485742}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1091458170}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18173_18228_x212341576}

[*[idle-time]{lang="EN-US"}*]{#struct_0_18173_18228_x280142424}[：]{style="font-family:宋体"}[Web]{lang="EN-US"}[闲置超时时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[999]{lang="EN-US"}[，单位为分钟。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_x70362321}

[[当某]{style="font-family:宋体"}[Web]{lang="EN-US"}]{#struct_0_18173_18228_1044610313}[用户在指定时间（]{style="font-family:宋体"}*[idle-time]{lang="EN-US"}*[）内一直没有操作]{style="font-family:宋体"}[Web]{lang="EN-US"}[页面，包括点击鼠标或键盘操作（只是移动鼠标，不会延长用户的下线时间），则系统会强制断开该用户的]{style="font-family:宋体"}[Web]{lang="EN-US"}[链接，使该用户下线。从而尽量避免在用户离开登录终端期间，非法用户对设备进行配置。]{style="font-family:宋体"}

[[需要注意的是，修改]{style="font-family:宋体"}[Web]{lang="EN-US"}]{#struct_0_18173_18228_1379943315}[线的闲置超时时间，会影响正在访问的用户。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_x1769494404}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x2055449395}[设置]{style="font-family:宋体"}[Web]{lang="EN-US"}[闲置超时时间为]{style="font-family:宋体"}[100]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_x854485743}

[\[Sysname\] web idle-timeout 100]{lang="EN-US"}
:::::

::: {#-1661944146 .myid}
[]{#_Toc404782513}[]{#struct_0_18173_18228_x1091523706}[]{#_Toc354582633}

**登录设备 \-- 登录设备命令 \-- webui log**

------------------------------------------------------------------------

[**[webui log enable]{lang="EN-US"}**]{#struct_0_18173_18228_767896041}[命令用来开启]{style="font-family:宋体"}[Web]{lang="EN-US"}[操作日志输出功能。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[webui log enable]{lang="EN-US"}**]{#struct_0_18173_18228_129899624}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18173_18228_x854485744}

[**[webui log enable]{lang="EN-US"}**]{#struct_0_18173_18228_x1091064954}

[**[undo ]{lang="EN-US"}[webui log enable]{lang="EN-US"}**]{#struct_0_18173_18228_946658195}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18173_18228_x854485745}

[[Web]{lang="EN-US"}]{#struct_0_18173_18228_x1091130490}[操作日志输出功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18173_18228_x854485746}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18173_18228_x1091196026}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18173_18228_x854485747}

[[network-admin]{lang="EN-US"}]{#struct_0_18173_18228_x1091261562}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18173_18228_1711654093}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18173_18228_x854485748}

[[开启]{style="font-family:宋体"}[Web]{lang="EN-US"}]{#struct_0_18173_18228_x1091851386}[操作日志输出功能，比较关键的]{style="font-family:宋体"}[Web]{lang="EN-US"}[操作（比如修改系统时间）会产生对应的]{style="font-family:宋体"}[Web]{lang="EN-US"}[操作日志，输出到信息中心。通过设置信息中心的参数，最终决定]{style="font-family:宋体"}[Web]{lang="EN-US"}[操作日志的输出规则（即是否允许输出以及输出方向）]{style="font-family:宋体"}

[[能够触发]{style="font-family:宋体"}[Web]{lang="EN-US"}]{#struct_0_18173_18228_1484166421}[操作日志的]{style="font-family:宋体"}[Web]{lang="EN-US"}[操作动作和设备相关，请以实际设备情况为准。]{style="font-family:宋体"}

[[Web]{lang="EN-US"}]{#struct_0_18173_18228_x104374137}[操作日志，采用固定的模块名]{style="font-family:宋体"}["WEB"]{lang="EN-US"}[；]{style="font-family:宋体"}[日志助记符有统一的前缀]{style="font-family:宋体"}["WEBOPT\_"]{lang="EN-US"}[；同时]{style="font-family:宋体"}[Web]{lang="EN-US"}[操作日志还包含]{style="font-family:宋体"}[Web]{lang="EN-US"}[用户信息：]{style="font-family:宋体"}[Web]{lang="EN-US"}[客户端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和]{style="font-family:宋体"}[Web]{lang="EN-US"}[用户名。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18173_18228_1484166420}

[[\# ]{lang="EN-US"}]{#struct_0_18173_18228_x104308601}[开启]{style="font-family:宋体"}[Web]{lang="EN-US"}[操作日志输出功能，]{style="font-family:宋体"}[Web]{lang="EN-US"}[用户执行修改系统时间的操作。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18173_18228_518952409}

[\[Sysname\] webui log enable]{lang="EN-US"}

[[当]{style="font-family:宋体"}[Web]{lang="EN-US"}]{#struct_0_18173_18228_x1304410782}[用户执行修改系统时间的操作时，设备上将输出如下日志：]{style="font-family:宋体"}

[[%Mar 25 14:32:38:802 2013 H3C WEB/6/WEBOPT_SET_TIME: -HostIP=192.168.100.235-User=Admin; Set the system date and time to 2013-05-27T10:00:00.]{lang="EN-US"}]{#struct_0_18173_18228_793373560}
:::
