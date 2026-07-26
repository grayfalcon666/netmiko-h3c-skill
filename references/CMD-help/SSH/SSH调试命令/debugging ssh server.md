::: {#42942862 .myid}
[]{#_Toc404793162}[]{#_Toc395010546}[]{#struct_0_28483_x1134_1737402229}[]{#_Toc167939232}[]{#_Toc138241185}

**SSH \-- SSH调试命令 \-- debugging ssh server**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_28483_x1134_x2123266295}

[**[debugging ssh server]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **message** }]{lang="EN-US"}]{#struct_0_28483_x1134_762641868}

[**[undo debugging ssh server]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **message** }]{lang="EN-US"}]{#struct_0_28483_x1134_1049607749}

[[【视图】]{style="font-family:黑体"}]{#struct_0_28483_x1134_1889205385}

[[用户视图]{style="font-family:宋体"}]{#struct_0_28483_x1134_x801915213}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_28483_x1134_1882405071}

[[network-admin]{lang="EN-US"}]{#struct_0_28483_x1134_x763511310}

[[mdc-admin]{lang="EN-US"}]{#struct_0_28483_x1134_x977103426}

[[【参数】]{style="font-family:黑体"}]{#struct_0_28483_x1134_x546081131}

[**[all]{lang="EN-US"}**]{#struct_0_28483_x1134_x2123725046}[：所有类型的调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_28483_x1134_x470962783}[：错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_28483_x1134_1984883746}[：事件调试信息开关。]{style="font-family:宋体"}

[**[message]{lang="EN-US"}**]{#struct_0_28483_x1134_x1455423021}[：消息调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_28483_x1134_63935776}

[**[debugging ssh server]{lang="EN-US"}**]{#struct_0_28483_x1134_x1527268191}[命令用来打开]{style="font-family:宋体"}[SSH]{lang="EN-US"}[服务器的调试信息开关。]{style="font-family:宋体"}**[undo debugging ssh server]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[SSH]{lang="EN-US"}[服务器的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[SSH]{lang="EN-US"}]{#struct_0_28483_x1134_x1150809737}[服务器调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging ssh server error]{lang="EN-US"}]{#struct_0_28483_x1134_x2004620635}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1112236682}[[字段]{style="font-family:黑体"}]{#struct_0_28483_x1134_x439423884}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_28483_x1134_x2123790582}

[[Failed to get challenge]{lang="EN-US"}]{#struct_0_28483_x1134_x1263407451}

[[获取挑战字失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x150628830}

[[PAM authentication context not initialized]{lang="EN-US"}]{#struct_0_28483_x1134_x1184720992}

[[PAM]{lang="EN-US"}]{#struct_0_28483_x1134_137265269}[认证上下文未初始化]{style="font-family:宋体"}

[[Failed to set real user ID:]{lang="EN-US"}]{#struct_0_28483_x1134_610606594}

[[设置]{style="font-family:宋体"}[real user id]{lang="EN-US"}]{#struct_0_28483_x1134_x2123593974}[失败]{style="font-family:宋体"}

[[Failed to set effective user ID:]{lang="EN-US"}]{#struct_0_28483_x1134_x862637305}

[[设置]{style="font-family:宋体"}[effective user id]{lang="EN-US"}]{#struct_0_28483_x1134_x278507069}[失败]{style="font-family:宋体"}

[[Too many environment variables, expected \<= 1024.]{lang="EN-US"}]{#struct_0_28483_x1134_1929136489}

[[环境变量太多，应该不大于]{style="font-family:宋体"}[1024]{lang="EN-US"}]{#struct_0_28483_x1134_x277329277}

[[Internal error: PAM authentication succeeded when it should have failed]{lang="EN-US"}]{#struct_0_28483_x1134_x2123659510}

[[内部错误，]{style="font-family:宋体"}[PAM]{lang="EN-US"}]{#struct_0_28483_x1134_x921836157}[认证成功，原本应该失败]{style="font-family:宋体"}

[[PAM: Initialization requested when PAM is disabled.]{lang="EN-US"}]{#struct_0_28483_x1134_1041832097}

[[PAM]{lang="EN-US"}]{#struct_0_28483_x1134_x1495049825}[未使能的情况下初始化]{style="font-family:宋体"}[PAM]{lang="EN-US"}

[[PAM: Initialization failed]{lang="EN-US"}]{#struct_0_28483_x1134_432887029}

[[PAM]{lang="EN-US"}]{#struct_0_28483_x1134_x2123462902}[初始化失败]{style="font-family:宋体"}

[[PAM: Failed to set PAM_TTY:]{lang="EN-US"}]{#struct_0_28483_x1134_617979906}

[[设置]{style="font-family:宋体"}[PAM_TTY]{lang="EN-US"}]{#struct_0_28483_x1134_x1220543226}[失败]{style="font-family:宋体"}

[[PAM: PAM disabled or failed to initialize]{lang="EN-US"}]{#struct_0_28483_x1134_449934769}

[[PAM]{lang="EN-US"}]{#struct_0_28483_x1134_x1025198035}[未使能或者初始化失败]{style="font-family:宋体"}

[[PAM: Failed to set PAM_CONV:]{lang="EN-US"}]{#struct_0_28483_x1134_x2123528438}

[[设置]{style="font-family:宋体"}[PAM_CONV]{lang="EN-US"}]{#struct_0_28483_x1134_1712864179}[失败]{style="font-family:宋体"}

[[Failed to generate RSA authentication challenge.]{lang="EN-US"}]{#struct_0_28483_x1134_737859215}

[[生成]{style="font-family:宋体"}[RSA]{lang="EN-US"}]{#struct_0_28483_x1134_144311321}[认证挑战字失败]{style="font-family:宋体"}

[[Failed to verify the RSA authentication response: bad challenge length *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x2123331830}

[[验证]{style="font-family:宋体"}[RSA]{lang="EN-US"}]{#struct_0_28483_x1134_x1139100252}[认证应答报文失败：错误的挑战字长度]{style="font-family:宋体"}*[xx]{lang="EN-US"}*

[[Failed to perform the RSA authentication challenge-response dialog]{lang="EN-US"}]{#struct_0_28483_x1134_x1119633829}

[[准备]{style="font-family:宋体"}[RSA]{lang="EN-US"}]{#struct_0_28483_x1134_565110439}[认证挑战交换环境失败]{style="font-family:宋体"}

[[Failed to create new BN.]{lang="EN-US"}]{#struct_0_28483_x1134_559563144}

[[创建]{style="font-family:宋体"}[BIGNUM]{lang="EN-US"}]{#struct_0_28483_x1134_x2123397366}[失败]{style="font-family:宋体"}

[[INTERNAL ERROR: authenticated invalid user *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_848895031}

[[内部错误，非法认证用户]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_793743905}

[[Access denied for user *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x18142487}

[[拒绝用户]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x2123200758}[接入]{style="font-family:宋体"}

[[No authentication context]{lang="EN-US"}]{#struct_0_28483_x1134_374688684}

[[没有认证上下文]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1653375419}

[[Keyboard interface error]{lang="EN-US"}]{#struct_0_28483_x1134_x2123266294}

[[keyboard]{lang="EN-US"}]{#struct_0_28483_x1134_x1966241487}[接口错误]{style="font-family:宋体"}

[[Wrong number of replies]{lang="EN-US"}]{#struct_0_28483_x1134_x2146591778}

[[应答报文数目错误]{style="font-family:宋体"}]{#struct_0_28483_x1134_1621319990}

[[Access denied for user *xx* by PAM account configuration.]{lang="EN-US"}]{#struct_0_28483_x1134_x2123725049}

[[PAM]{lang="EN-US"}]{#struct_0_28483_x1134_x518016950}[计费配置拒绝用户]{style="font-family:宋体"}*[xx]{lang="EN-US"}*[登录]{style="font-family:宋体"}

[[Failed to sign server host key]{lang="EN-US"}]{#struct_0_28483_x1134_x1900823829}

[[对服务器主机密钥进行签名失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_841278647}

[[protocol error during kex, no DH_GEX_REQUEST:]{lang="PT-BR"}]{#struct_0_28483_x1134_x2123790585}

[[密钥计算过程中协议错误，没有收到]{style="font-family:宋体"}[DH_GEX_REQUEST]{lang="EN-US"}]{#struct_0_28483_x1134_1109245544}[请求]{style="font-family:宋体"}

[[DH_GEX_REQUEST, bad parameters:]{lang="EN-US"}]{#struct_0_28483_x1134_x922522825}

[[DH_GEX_REQUEST]{lang="EN-US"}]{#struct_0_28483_x1134_x636753299}[请求中发现参数错误]{style="font-family:宋体"}

[[Bad IP address or host name:]{lang="EN-US"}]{#struct_0_28483_x1134_x2123593977}

[[错误的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_28483_x1134_1866246050}[地址或主机名]{style="font-family:宋体"}

[[No user or invalid user]{lang="PT-BR"}]{#struct_0_28483_x1134_x906752077}

[[无用户名或非法用户名]{style="font-family:宋体"}]{#struct_0_28483_x1134_x2123659513}

[[No session]{lang="EN-US"}]{#struct_0_28483_x1134_1807047198}

[[无会话]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1211661902}

[[Failed to set environment: too many environment vars]{lang="EN-US"}]{#struct_0_28483_x1134_569345535}

[[设置环境变量失败：太多的环境变量]{style="font-family:宋体"}]{#struct_0_28483_x1134_x2123462905}

[[Too many lines in environment file *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_214695379}

[[环境变量文件]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_226279784}[的行数太多]{style="font-family:宋体"}

[[Insane session id *xx* (max *mm* allocated *nn*)]{lang="EN-US"}]{#struct_0_28483_x1134_x2123528441}

[[错误的通道号]{style="font-family:宋体"}[xx]{lang="EN-US"}]{#struct_0_28483_x1134_x209646730}[（最大值]{style="font-family:宋体"}*[mm]{lang="EN-US"}*[，]{style="font-family:宋体"}[已分配]{style="font-family:宋体"}*[nn]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Insane first unused session id *xx* (max *mm*, allocated *nn*).]{lang="EN-US"}]{#struct_0_28483_x1134_x69608745}

[[错误的第一个未使用通道号]{style="font-family:宋体"}]{#struct_0_28483_x1134_x2123331833}*[xx]{lang="EN-US"}*[（最大值]{style="font-family:宋体"}*[mm]{lang="EN-US"}*[，]{style="font-family:宋体"}[已分配]{style="font-family:宋体"}*[nn]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Failed to allocate new session]{lang="EN-US"}]{#struct_0_28483_x1134_x735815725}

[[分配新会话失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x799564783}

[[No user for session *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x2123397369}

[[会话]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1073419270}*[xx]{lang="EN-US"}*[没有用户]{style="font-family:宋体"}

[[No channel for session *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_658260362}

[[会话]{style="font-family:宋体"}]{#struct_0_28483_x1134_x2123200761}*[xx]{lang="EN-US"}*[没有通道]{style="font-family:宋体"}

[[Session ]{lang="IT"}]{#struct_0_28483_x1134_x1547691153}*[xx]{lang="IT"}*[: no channel *yy*]{lang="IT"}

[[会话]{style="font-family:宋体"}]{#struct_0_28483_x1134_x2123266297}*[xx]{lang="IT"}*[没有通道]{style="font-family:宋体"}*[yy]{lang="IT"}*

[[Bad IP address or host name:]{lang="EN-US"}]{#struct_0_28483_x1134_1925441282}

[[错误的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_28483_x1134_x412964865}[地址或主机名]{style="font-family:宋体"}

[[No user or invalid user]{lang="PT-BR"}]{#struct_0_28483_x1134_x2123725048}

[[无用户名或非法用户名]{style="font-family:宋体"}]{#struct_0_28483_x1134_1048066991}

[[No session]{lang="EN-US"}]{#struct_0_28483_x1134_x2123790584}

[[无会话]{style="font-family:宋体"}]{#struct_0_28483_x1134_x456838397}

[[Failed to allocate new session]{lang="EN-US"}]{#struct_0_28483_x1134_x2123528440}

[[分配新通道号失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_1356437211}

[[TCP wrapper failed]{lang="EN-US"}]{#struct_0_28483_x1134_18392788}

[[TCP wrapper]{lang="EN-US"}]{#struct_0_28483_x1134_x2123266296}[失败]{style="font-family:宋体"}

[[Do connection:]{lang="EN-US"}]{#struct_0_28483_x1134_x803442073}

[[发起连接失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x2123725051}

[[Failed to get host key]{lang="EN-US"}]{#struct_0_28483_x1134_x874181774}

[[获取主机密码失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_952208732}

[[Failed to get server key]{lang="EN-US"}]{#struct_0_28483_x1134_x2123790587}

[[获取服务器密码失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x2022922338}

[[TTY name is null.]{lang="EN-US"}]{#struct_0_28483_x1134_x2123593979}

[[TTY]{lang="EN-US"}]{#struct_0_28483_x1134_x1622152192}[名字为空]{style="font-family:宋体"}

[[Failed to change owner]{lang="EN-US"}]{#struct_0_28483_x1134_x2123659515}

[[改变]{style="font-family:宋体"}[owner]{lang="EN-US"}]{#struct_0_28483_x1134_x1325120684}[失败]{style="font-family:宋体"}

[[Failed to change mode]{lang="EN-US"}]{#struct_0_28483_x1134_x2123462907}

[[改变]{style="font-family:宋体"}[mode]{lang="EN-US"}]{#struct_0_28483_x1134_1377494793}[失败]{style="font-family:宋体"}

[[Authentication response too long:]{lang="EN-US"}]{#struct_0_28483_x1134_x2123528443}

[[认证应答报文长度过长]{style="font-family:宋体"}]{#struct_0_28483_x1134_953152684}

[[Bad authentication reply message type:]{lang="EN-US"}]{#struct_0_28483_x1134_x2123331835}

[[错误的认证应答消息类型]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1542384779}

[[Too many identities in authentication reply:]{lang="EN-US"}]{#struct_0_28483_x1134_x2123397371}

[[认证应答中存在太多的标识]{style="font-family:宋体"}]{#struct_0_28483_x1134_x717123374}

[[Bad authentication response:]{lang="EN-US"}]{#struct_0_28483_x1134_x2123200763}

[[错误的认证应答]{style="font-family:宋体"}]{#struct_0_28483_x1134_1584476729}

[[Bad response from authentication agent:]{lang="EN-US"}]{#struct_0_28483_x1134_x2123266299}

[[从认证代理接收到错误的应答]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1919187320}

[[Failed to get data from buffer]{lang="EN-US"}]{#struct_0_28483_x1134_x2123725050}

[[从]{style="font-family:宋体"}]{#struct_0_28483_x1134_691902167}[buffer]{lang="EN-US"}[中获取数据失败]{style="font-family:宋体"}

[[Bad string length *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x2123790586}

[[错误的字符串长度]{style="font-family:宋体"}]{#struct_0_28483_x1134_705961017}*[xx]{lang="EN-US"}*

[[Failed to put null string to buffer]{lang="EN-US"}]{#struct_0_28483_x1134_x2123593978}

[[向]{style="font-family:宋体"}]{#struct_0_28483_x1134_x2123659514}[buffer]{lang="EN-US"}[中存入空串失败]{style="font-family:宋体"}

[[Failed to put BIGNUM to the buffer.]{lang="EN-US"}]{#struct_0_28483_x1134_1403762671}

[[向]{style="font-family:宋体"}]{#struct_0_28483_x1134_x2123462906}[buffer]{lang="EN-US"}[中存入]{style="font-family:宋体"}[BIGNUM]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to get BIGNUM from the buffer.]{lang="EN-US"}]{#struct_0_28483_x1134_x1351388562}

[[从]{style="font-family:宋体"}]{#struct_0_28483_x1134_x2123528442}[buffer]{lang="EN-US"}[中获取]{style="font-family:宋体"}[BIGNUM]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to write BIGNUM to the buffer in SSH2 format.]{lang="EN-US"}]{#struct_0_28483_x1134_x1775730671}

[[向]{style="font-family:宋体"}]{#struct_0_28483_x1134_x2123331834}[buffer]{lang="EN-US"}[中以]{style="font-family:宋体"}[ssh2]{lang="EN-US"}[协议格式写入]{style="font-family:宋体"}[BIGNUM]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to get BIGNUM from the buffer in SSH2 format.]{lang="EN-US"}]{#struct_0_28483_x1134_1186498576}

[[从]{style="font-family:宋体"}]{#struct_0_28483_x1134_x2123397370}[buffer]{lang="EN-US"}[中以]{style="font-family:宋体"}[ssh2]{lang="EN-US"}[协议格式获取]{style="font-family:宋体"}[BIGNUM]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to append space to the buffer:]{lang="EN-US"}]{#struct_0_28483_x1134_2011759981}

[[在]{style="font-family:宋体"}]{#struct_0_28483_x1134_x2123200762}[buffer]{lang="EN-US"}[后追加空间失败]{style="font-family:宋体"}

[[Failed to append buffer space:]{lang="EN-US"}]{#struct_0_28483_x1134_x2123266298}

[[在]{style="font-family:宋体"}]{#struct_0_28483_x1134_x353103379}[buffer]{lang="EN-US"}[后追加空间失败]{style="font-family:宋体"}

[[Failed to consume data from the beginning of the buffer.]{lang="EN-US"}]{#struct_0_28483_x1134_x201410746}

[[从]{style="font-family:宋体"}]{#struct_0_28483_x1134_1667887462}[buffer]{lang="EN-US"}[头删除数据失败]{style="font-family:宋体"}

[[Failed to consume data from the end of the buffer.]{lang="EN-US"}]{#struct_0_28483_x1134_x201476282}

[[从]{style="font-family:宋体"}]{#struct_0_28483_x1134_1634720416}[buffer]{lang="EN-US"}[尾删除数据失败]{style="font-family:宋体"}

[[Failed to get remote hostname.]{lang="EN-US"}]{#struct_0_28483_x1134_x201279674}

[[获取对端主机名失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x201345210}

[[Connection from *x.x.x.x* with IP options: *yy*]{lang="EN-US"}]{#struct_0_28483_x1134_1229010953}

[[从]{style="font-family:宋体"}]{#struct_0_28483_x1134_x201148602}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}*[x.x.x.x]{lang="EN-US"}*[发起的连接，携带]{style="font-family:宋体"}[IP]{lang="EN-US"}[选项为]{style="font-family:宋体"}*[yy]{lang="EN-US"}*

[[Failed to allocate new channel:]{lang="EN-US"}]{#struct_0_28483_x1134_61183415}

[[channel]{lang="EN-US"}]{#struct_0_28483_x1134_x201214138}[分配失败]{style="font-family:宋体"}

[[Cannot happen: SSH_CHANNEL_LARVAL]{lang="EN-US"}]{#struct_0_28483_x1134_x201017530}

[[SSH_CHANNEL_LARVAL]{lang="EN-US"}]{#struct_0_28483_x1134_882134608}[类型的]{style="font-family:宋体"}[channel]{lang="EN-US"}[在不兼容]{style="font-family:宋体"}[2.0]{lang="EN-US"}[版本的情况下不应该出现]{style="font-family:宋体"}

[[Cannot happen: OUT_DRAIN]{lang="EN-US"}]{#struct_0_28483_x1134_x201083066}

[[SSH_CHANNEL_OUTPUT_DRAINING]{lang="EN-US"}]{#struct_0_28483_x1134_1644985313}[类型的]{style="font-family:宋体"}[channel]{lang="EN-US"}[在不兼容]{style="font-family:宋体"}[1.3]{lang="EN-US"}[版本的情况下不应该出现]{style="font-family:宋体"}

[[Bad channel type *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x200886458}

[[错误的]{style="font-family:宋体"}]{#struct_0_28483_x1134_x200951994}[channel]{lang="EN-US"}[类型]{style="font-family:宋体"}*[xx]{lang="EN-US"}*

[[Bad channel id *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x1455921557}

[[错误的]{style="font-family:宋体"}]{#struct_0_28483_x1134_x201410745}[channel ID *xx*]{lang="EN-US"}

[[Non-larval channel]{lang="EN-US"}]{#struct_0_28483_x1134_x201476281}

[[channel]{lang="EN-US"}]{#struct_0_28483_x1134_1634654880}[为空或者非]{style="font-family:宋体"}[SSH_CHANNEL_LARVAL]{lang="EN-US"}[类型的]{style="font-family:宋体"}[channel]{lang="EN-US"}

[[Channel xx: decode socks4: len *mm* \> have *nn*]{lang="EN-US"}]{#struct_0_28483_x1134_x201279673}

[[channel ID *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x1502541268}[：]{style="font-family:宋体"}[socks4]{lang="EN-US"}[解码时，]{style="font-family:宋体"}[buffer]{lang="EN-US"}[长度]{style="font-family:宋体"}*[mm]{lang="EN-US"}*[大于实际串长度]{style="font-family:宋体"}*[nn]{lang="EN-US"}*

[[Channel xx: decode socks4a: len *mm* \> have *nn*]{lang="EN-US"}]{#struct_0_28483_x1134_x201345209}

[[channel ID *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x201148601}[：]{style="font-family:宋体"}[socks4a]{lang="EN-US"}[解码时，]{style="font-family:宋体"}[buffer]{lang="EN-US"}[长度]{style="font-family:宋体"}*[mm]{lang="EN-US"}*[大于实际串长度]{style="font-family:宋体"}*[nn]{lang="EN-US"}*

[[Unexpected data on control fd]{lang="EN-US"}]{#struct_0_28483_x1134_x201214137}

[[在控制文件描述符上获取到异常数据]{style="font-family:宋体"}]{#struct_0_28483_x1134_80921385}

[[Failed to prepare select:]{lang="EN-US"}]{#struct_0_28483_x1134_x201017529}

[[select]{lang="EN-US"}]{#struct_0_28483_x1134_x201083065}[准备失败]{style="font-family:宋体"}

[[Cannot happen: input state INPUT_WAIT_DRAIN for proto 1.3]{lang="EN-US"}]{#struct_0_28483_x1134_1644788705}

[[在]{style="font-family:宋体"}[1.3]{lang="EN-US"}]{#struct_0_28483_x1134_x200886457}[协议中不应该出现输入状态]{style="font-family:宋体"}[ INPUT_WAIT_DRAIN]{lang="EN-US"}

[[Too many forwards]{lang="EN-US"}]{#struct_0_28483_x1134_x307045609}

[[太多的]{style="font-family:宋体"}[TCP/IP]{lang="EN-US"}]{#struct_0_28483_x1134_x200951993}[端口转发]{style="font-family:宋体"}

[[Failed to set socket to non-block]{lang="EN-US"}]{#struct_0_28483_x1134_x201410748}

[[设置]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_28483_x1134_x201476284}[为非阻塞时失败]{style="font-family:宋体"}

[[x11_request_forwarding:]{lang="EN-US"}]{#struct_0_28483_x1134_1634851488}

[[在]{style="font-family:宋体"}[x11]{lang="EN-US"}]{#struct_0_28483_x1134_x201279676}[转发请求处理中收到错误的认证数据]{style="font-family:宋体"}

[[Bad 3DES IV length: *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x201345212}

[[错误的]{style="font-family:宋体"}[3DES IV]{lang="EN-US"}]{#struct_0_28483_x1134_1229142025}[长度]{style="font-family:宋体"}*[xx]{lang="EN-US"}*

[[No 3DES context.]{lang="EN-US"}]{#struct_0_28483_x1134_x201148604}

[[没有]{style="font-family:宋体"}[3DES]{lang="EN-US"}]{#struct_0_28483_x1134_x201214140}[上下文信息]{style="font-family:宋体"}

[[No AES context.]{lang="EN-US"}]{#struct_0_28483_x1134_80724776}

[[没有]{style="font-family:宋体"}[AES]{lang="EN-US"}]{#struct_0_28483_x1134_x201017532}[上下文信息]{style="font-family:宋体"}

[[Failed to initialize cipher:]{lang="EN-US"}]{#struct_0_28483_x1134_x201083068}

[[初始化加密套件失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_1645116385}

[[Failed to initialize cipher *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x200886460}

[[初始化加密套件]{style="font-family:宋体"}[xx]{lang="EN-US"}]{#struct_0_28483_x1134_x200951996}[失败]{style="font-family:宋体"}

[[Cipher encrypt failed:]{lang="EN-US"}]{#struct_0_28483_x1134_x201410747}

[[加密失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_1667952998}

[[Wrong IV length *xx* != *yy*]{lang="EN-US"}]{#struct_0_28483_x1134_x201476283}

[[IV]{lang="EN-US"}]{#struct_0_28483_x1134_x201279675}[长度错误]{style="font-family:宋体"}

[[Bad cipher *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x1502410196}

[[错误的加密套件编号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x201345211}

[[No available ciphers found]{lang="EN-US"}]{#struct_0_28483_x1134_x201148603}

[[没有可用的加密套件]{style="font-family:宋体"}]{#struct_0_28483_x1134_x201214139}

[[Bad compression level *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_80266025}

[[错误的压缩等级]{style="font-family:宋体"}]{#struct_0_28483_x1134_x201017531}*[xx]{lang="EN-US"}*

[[Buffer compress failed:]{lang="EN-US"}]{#struct_0_28483_x1134_x201083067}

[[Buffer]{lang="EN-US"}]{#struct_0_28483_x1134_x200886459}[压缩失败]{style="font-family:宋体"}

[[Buffer uncompress failed:]{lang="EN-US"}]{#struct_0_28483_x1134_x306914537}

[[Buffer]{lang="EN-US"}]{#struct_0_28483_x1134_x200951995}[解压缩失败]{style="font-family:宋体"}

[[Detect attack:]{lang="EN-US"}]{#struct_0_28483_x1134_x201410750}

[[检测到]{style="font-family:宋体"}[CRC32 ]{lang="EN-US"}]{#struct_0_28483_x1134_x201476286}[压缩攻击]{style="font-family:宋体"}

[[Failed to generate DH_key:]{lang="EN-US"}]{#struct_0_28483_x1134_1634982560}

[[生成]{style="font-family:宋体"}[DH]{lang="EN-US"}]{#struct_0_28483_x1134_x201279678}[密钥失败]{style="font-family:宋体"}

[[Failed to create BN.]{lang="EN-US"}]{#struct_0_28483_x1134_x201345214}

[[创建]{style="font-family:宋体"}[BN]{lang="EN-US"}]{#struct_0_28483_x1134_x201148606}[失败]{style="font-family:宋体"}

[[Failed to generate DH_private_key]{lang="EN-US"}]{#struct_0_28483_x1134_x201214142}

[[生成]{style="font-family:宋体"}[DH]{lang="EN-US"}]{#struct_0_28483_x1134_80593704}[私钥失败]{style="font-family:宋体"}

[[Failed to generate DH_key]{lang="EN-US"}]{#struct_0_28483_x1134_x201017534}

[[生成]{style="font-family:宋体"}[DH]{lang="EN-US"}]{#struct_0_28483_x1134_x201083070}[密钥失败]{style="font-family:宋体"}

[[Failed to generate DH_key:]{lang="EN-US"}]{#struct_0_28483_x1134_x200886462}

[[生成]{style="font-family:宋体"}[DH]{lang="EN-US"}]{#struct_0_28483_x1134_x307242214}[密钥失败]{style="font-family:宋体"}

[[Failed to generate DH public key.]{lang="EN-US"}]{#struct_0_28483_x1134_x200951998}

[[生成]{style="font-family:宋体"}[DH]{lang="EN-US"}]{#struct_0_28483_x1134_x201410749}[公钥失败]{style="font-family:宋体"}

[[Protocol error.]{lang="EN-US"}]{#struct_0_28483_x1134_x201476285}

[[协议错误]{style="font-family:宋体"}]{#struct_0_28483_x1134_x201279677}

[[Failed to seed PRNG.]{lang="EN-US"}]{#struct_0_28483_x1134_x1502279124}

[[设置]{style="font-family:宋体"}[PRNG]{lang="EN-US"}]{#struct_0_28483_x1134_x201345213}[的种子失败]{style="font-family:宋体"}

[[Failed to send SSH2_MSG_KEXINIT:]{lang="EN-US"}]{#struct_0_28483_x1134_x201148605}

[[发送]{style="font-family:宋体"}[SSH2_MSG_KEXINIT]{lang="EN-US"}]{#struct_0_28483_x1134_x201214141}[消息失败]{style="font-family:宋体"}

[[Received SSH2_MSG_KEXINIT:]{lang="EN-US"}]{#struct_0_28483_x1134_x201017533}

[[发送]{style="font-family:宋体"}[SSH2_MSG_KEXINIT]{lang="EN-US"}]{#struct_0_28483_x1134_x201083069}[消息失败：空的交换上下文]{style="font-family:宋体"}

[[Unsupported key exchange:]{lang="EN-US"}]{#struct_0_28483_x1134_1645050849}

[[不支持的密钥交换类型]{style="font-family:宋体"}]{#struct_0_28483_x1134_x200886461}

[[No matching cipher found:]{lang="EN-US"}]{#struct_0_28483_x1134_x200951997}

[[没有匹配的加密算法]{style="font-family:宋体"}]{#struct_0_28483_x1134_1364673195}

[[Matching cipher is not supported:]{lang="EN-US"}]{#struct_0_28483_x1134_1364607659}

[[匹配的加密算法不支持]{style="font-family:宋体"}]{#struct_0_28483_x1134_1094812610}

[[No matching mac found:]{lang="EN-US"}]{#struct_0_28483_x1134_1364804267}

[[没有匹配的摘要算法]{style="font-family:宋体"}]{#struct_0_28483_x1134_1364738731}

[[Unsupported mac *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_1364935339}

[[不支持的摘要算法]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1364869803}

[[No matching compress found:]{lang="EN-US"}]{#struct_0_28483_x1134_1365066411}

[[没有匹配的压缩算法]{style="font-family:宋体"}]{#struct_0_28483_x1134_1365000875}

[[Unsupported compress:]{lang="EN-US"}]{#struct_0_28483_x1134_1365197483}

[[不支持的压缩算法]{style="font-family:宋体"}]{#struct_0_28483_x1134_1365131947}

[[Failed to negotiate a key exchange method.]{lang="EN-US"}]{#struct_0_28483_x1134_x1575368628}

[[密钥交换算法协商失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_1364673196}

[[Bad kex algorithm:]{lang="EN-US"}]{#struct_0_28483_x1134_1364607660}

[[错误的密钥交换算法]{style="font-family:宋体"}]{#struct_0_28483_x1134_1364804268}

[[No host_key algorithm]{lang="EN-US"}]{#struct_0_28483_x1134_1364738732}

[[没有主机公钥算法]{style="font-family:宋体"}]{#struct_0_28483_x1134_1364935340}

[[Bad host_key algorithm:]{lang="EN-US"}]{#struct_0_28483_x1134_1364869804}

[[错误的主机公钥算法]{style="font-family:宋体"}]{#struct_0_28483_x1134_1365066412}

[[Bad kex md size *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x463073427}

[[错误的密钥交换模数大小]{style="font-family:宋体"}]{#struct_0_28483_x1134_1365000876}*[xx]{lang="EN-US"}*

[[Bad host modulus (len *xx*)]{lang="EN-US"}]{#struct_0_28483_x1134_1365197484}

[[错误的主机模数（长度]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1365131948}[）]{style="font-family:宋体"}

[[Bad server modulus (len *xx*)]{lang="EN-US"}]{#struct_0_28483_x1134_1364673193}

[[错误的服务器模数（长度]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1364607657}[）]{style="font-family:宋体"}

[[Unexpected KEX type *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_1364804265}

[[错误的密钥交换算法类型]{style="font-family:宋体"}]{#struct_0_28483_x1134_1364738729}*[xx]{lang="EN-US"}*

[[Failed to compute DH key]{lang="EN-US"}]{#struct_0_28483_x1134_1364935337}

[[计算]{style="font-family:宋体"}[DH]{lang="EN-US"}]{#struct_0_28483_x1134_1364869801}[密钥失败]{style="font-family:宋体"}

[[Failed to compute BN]{lang="EN-US"}]{#struct_0_28483_x1134_1365066409}

[[计算]{style="font-family:宋体"}[BN]{lang="EN-US"}]{#struct_0_28483_x1134_x463401106}[失败]{style="font-family:宋体"}

[[Cannot load hostkey]{lang="EN-US"}]{#struct_0_28483_x1134_1365000873}

[[加载主机密钥失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_1365197481}

[[Unsupported hostkey type *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_1365131945}

[[不支持的主机密钥类型]{style="font-family:宋体"}]{#struct_0_28483_x1134_1364673194}*[xx]{lang="EN-US"}*

[[Failed to create RSA key]{lang="EN-US"}]{#struct_0_28483_x1134_1364607658}

[[创建]{style="font-family:宋体"}[RSA]{lang="EN-US"}]{#struct_0_28483_x1134_1364804266}[密钥失败]{style="font-family:宋体"}

[[Failed to create DSA key]{lang="EN-US"}]{#struct_0_28483_x1134_1364738730}

[[创建]{style="font-family:宋体"}[DSA]{lang="EN-US"}]{#struct_0_28483_x1134_1364935338}[密钥失败]{style="font-family:宋体"}

[[Failed to create key: ]{lang="EN-US"}]{#struct_0_28483_x1134_1364869802}

[[创建密钥失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_1365066410}

[[Failed to free key:]{lang="EN-US"}]{#struct_0_28483_x1134_1365000874}

[[释放]{style="font-family:宋体"}[key]{lang="EN-US"}]{#struct_0_28483_x1134_1365197482}[失败]{style="font-family:宋体"}

[[Failed to compare key:]{lang="EN-US"}]{#struct_0_28483_x1134_1365131946}

[[密钥比较失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_1364673191}

[[Failed to print key finger:]{lang="EN-US"}]{#struct_0_28483_x1134_1364607655}

[[打印密钥指纹失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_1364804263}

[[Failed to generate rsa_private_key.]{lang="EN-US"}]{#struct_0_28483_x1134_1364738727}

[[生成]{style="font-family:宋体"}[RSA]{lang="EN-US"}]{#struct_0_28483_x1134_1364935335}[私有失败]{style="font-family:宋体"}

[[Failed to generate dsa_private_key.]{lang="EN-US"}]{#struct_0_28483_x1134_1364869799}

[[生成]{style="font-family:宋体"}[DSA]{lang="EN-US"}]{#struct_0_28483_x1134_1365066407}[私有失败]{style="font-family:宋体"}

[[Failed to generate key:]{lang="EN-US"}]{#struct_0_28483_x1134_1365000871}

[[密钥生成失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_1365197479}

[[Failed to setup MAC *xx*, length *yy*.]{lang="EN-US"}]{#struct_0_28483_x1134_1365131943}

[[设置摘要算法]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1364673192}[失败，长度为]{style="font-family:宋体"}*[yy]{lang="EN-US"}*

[[Failed to initial MAC]{lang="EN-US"}]{#struct_0_28483_x1134_1364607656}

[[初始化摘要算法失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_1364804264}

[[Failed to compute MAC:]{lang="EN-US"}]{#struct_0_28483_x1134_1364738728}

[[计算摘要失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_1364935336}

[[Failed to add arguments:]{lang="EN-US"}]{#struct_0_28483_x1134_1364869800}

[[增加参数失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_1365066408}

[[Failed to replace argument:]{lang="EN-US"}]{#struct_0_28483_x1134_1365000872}

[[替换参数失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_1365197480}

[[Failed to expend keys:]{lang="EN-US"}]{#struct_0_28483_x1134_1365131944}

[[扩展密钥失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1364210160}

[[Bad channel input state:]{lang="EN-US"}]{#struct_0_28483_x1134_x1364275696}

[[错误的通道输入状态]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1364079088}

[[Bad channel output state:]{lang="EN-US"}]{#struct_0_28483_x1134_x1364144624}

[[错误的通道输出状态]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1363948016}

[[Failed to load cipher \'none\']{lang="EN-US"}]{#struct_0_28483_x1134_x1364013552}

[[载入]{style="font-family:宋体"}[none]{lang="EN-US"}]{#struct_0_28483_x1134_x1363816944}[加密套件失败]{style="font-family:宋体"}

[[Compression already enabled]{lang="EN-US"}]{#struct_0_28483_x1134_x1363882480}

[[已经使能了压缩]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1363685872}

[[Failed to set encrypt key:]{lang="EN-US"}]{#struct_0_28483_x1134_x1363751408}

[[设置加密密钥失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1364210159}

[[No keys for mode *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x1364275695}

[[模式]{style="font-family:宋体"}[xx]{lang="EN-US"}]{#struct_0_28483_x1134_x1364079087}[没有密钥]{style="font-family:宋体"}

[[Too many packets with same key]{lang="EN-US"}]{#struct_0_28483_x1134_x1364144623}

[[使用同一个密钥发送的包个数太多]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1364013551}

[[Read failed:]{lang="EN-US"}]{#struct_0_28483_x1134_x1363816943}

[[读数据失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1363882479}

[[Too large packet size:]{lang="EN-US"}]{#struct_0_28483_x1134_x1363685871}

[[包过大]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1363751407}

[[Disconnect recursively]{lang="EN-US"}]{#struct_0_28483_x1134_x1364210162}

[[重复断连]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1364275698}

[[Write failed:]{lang="EN-US"}]{#struct_0_28483_x1134_x1364079090}

[[写数据失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1363948018}

[[Write connection closed]{lang="EN-US"}]{#struct_0_28483_x1134_x1364013554}

[[连接的写方向已关闭]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1363816946}

[[Failed to ask password:]{lang="EN-US"}]{#struct_0_28483_x1134_x1363882482}

[[获取密码失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1363685874}

[[Failed to encrypt RSA public key, exponent too small or not odd.]{lang="EN-US"}]{#struct_0_28483_x1134_x1363751410}

[[RSA]{lang="EN-US"}]{#struct_0_28483_x1134_x1364210161}[公钥加密失败，指数太小或非偶数]{style="font-family:宋体"}

[[Failed to encrypt RSA public key]{lang="EN-US"}]{#struct_0_28483_x1134_x1364275697}

[[RSA]{lang="EN-US"}]{#struct_0_28483_x1134_x1364079089}[公钥加密失败]{style="font-family:宋体"}

[[Failed to decrypt RSA private key]{lang="EN-US"}]{#struct_0_28483_x1134_x1363948017}

[[RSA]{lang="EN-US"}]{#struct_0_28483_x1134_x1364013553}[私钥解密失败]{style="font-family:宋体"}

[[Failed to generate RSA additional parameters]{lang="EN-US"}]{#struct_0_28483_x1134_x1363816945}

[[生成]{style="font-family:宋体"}[RSA]{lang="EN-US"}]{#struct_0_28483_x1134_x1363882481}[附加参数失败]{style="font-family:宋体"}

[[Bad signature blob length:]{lang="EN-US"}]{#struct_0_28483_x1134_x1363685873}

[[错误的签名]{style="font-family:宋体"}[blob]{lang="EN-US"}]{#struct_0_28483_x1134_x1363751409}[长度]{style="font-family:宋体"}

[[Failed to verify DSA signature]{lang="EN-US"}]{#struct_0_28483_x1134_x1364210164}

[[验证]{style="font-family:宋体"}[DSA]{lang="EN-US"}]{#struct_0_28483_x1134_x1364275700}[签名失败]{style="font-family:宋体"}

[[Failed to set resource limits:]{lang="EN-US"}]{#struct_0_28483_x1134_x1364144628}

[[设置资源限制失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1363948020}

[[Failed to malloc memory: ]{lang="EN-US"}]{#struct_0_28483_x1134_x1364013556}

[[分配内存失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1363816948}

[[Failed to free memory]{lang="EN-US"}]{#struct_0_28483_x1134_x1363882484}

[[释放内存失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1363685876}

[[Failed to allocate memory]{lang="EN-US"}]{#struct_0_28483_x1134_x1363751412}

[[分配内存失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1364275699}

[[Protocol major versions differ for *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x1364079091}

[[客户端]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1364144627}*[xx]{lang="EN-US"}*[的协议主版本号不同]{style="font-family:宋体"}

[[Bad protocol version identification \'*yy*\' from *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x1363948019}

[[客户端]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1364013555}*[xx]{lang="EN-US"}*[的错误协议版本串]{style="font-family:宋体"}*[yy]{lang="EN-US"}*

[[Did not receive identification string from *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x1363882483}

[[没有从]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1363685875}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}*[xx]{lang="EN-US"}*[收到标识串]{style="font-family:宋体"}

[[Failed to write identification string to ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x1363751411}

[[向地址]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_201873781}[写入标识串失败]{style="font-family:宋体"}

[[PAM: conversation function passed a null context]{lang="EN-US"}]{#struct_0_28483_x1134_201808245}

[[交互接口为空]{style="font-family:宋体"}]{#struct_0_28483_x1134_201939317}

[[PAM: Failed to set TZ environment:]{lang="EN-US"}]{#struct_0_28483_x1134_202135925}

[[设置]{style="font-family:宋体"}[TZ]{lang="EN-US"}]{#struct_0_28483_x1134_202070389}[环境变量失败]{style="font-family:宋体"}

[[PAM: initialization failed]{lang="EN-US"}]{#struct_0_28483_x1134_202266997}

[[PAM]{lang="EN-US"}]{#struct_0_28483_x1134_202201461}[初始化失败]{style="font-family:宋体"}

[[PAM: Failed to set pam item *XX*.]{lang="EN-US"}]{#struct_0_28483_x1134_202332533}

[[设置]{style="font-family:宋体"}[PAM]{lang="EN-US"}]{#struct_0_28483_x1134_201873782}[的]{style="font-family:宋体"}*[XX]{lang="EN-US"}*[项错误]{style="font-family:宋体"}

[[Failed to verify the RSA authentication response:]{lang="EN-US"}]{#struct_0_28483_x1134_201808246}

[[验证]{style="font-family:宋体"}[RSA]{lang="EN-US"}]{#struct_0_28483_x1134_202004854}[认证应答失败]{style="font-family:宋体"}

[[Unknown message during authentication:]{lang="EN-US"}]{#struct_0_28483_x1134_202135926}

[[认证过程中收到未知消息]{style="font-family:宋体"}]{#struct_0_28483_x1134_202070390}

[*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_202266998}[ authentication disabled]{lang="EN-US"}

[[不支持认证方法]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_202201462}

[[Unsupported public key algorithm:]{lang="EN-US"}]{#struct_0_28483_x1134_202398070}

[[不支持的公钥算法]{style="font-family:宋体"}]{#struct_0_28483_x1134_201873779}

[[Unrecognized authentication method name:]{lang="EN-US"}]{#struct_0_28483_x1134_201808243}

[[未知的认证方法名]{style="font-family:宋体"}]{#struct_0_28483_x1134_202004851}

[[Read error from remote host *xx*:]{lang="EN-US"}]{#struct_0_28483_x1134_201939315}

[[从远端主机]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_202135923}[读取数据失败]{style="font-family:宋体"}

[[Wait returned pid *xx*, expected *yy*]{lang="EN-US"}]{#struct_0_28483_x1134_202266995}

[[返回的]{style="font-family:宋体"}[PID]{lang="EN-US"}]{#struct_0_28483_x1134_202201459}[值]{style="font-family:宋体"}*[xx]{lang="EN-US"}*[不是期望的]{style="font-family:宋体"}*[yy]{lang="EN-US"}*

[[Stelnet server is disabled or service type is not supported]{lang="EN-US"}]{#struct_0_28483_x1134_202398067}

[[Stelnet]{lang="EN-US"}]{#struct_0_28483_x1134_202332531}[服务器未使能或者服务器类型不支持]{style="font-family:宋体"}

[[No more sessions]{lang="EN-US"}]{#struct_0_28483_x1134_201808244}

[[没有更多的会话]{style="font-family:宋体"}]{#struct_0_28483_x1134_202004852}

[[Unknown packet type received after authentication:]{lang="EN-US"}]{#struct_0_28483_x1134_201939316}

[[认证通过后收到未知类型的包]{style="font-family:宋体"}]{#struct_0_28483_x1134_202135924}

[[Failed to close PTY:]{lang="EN-US"}]{#struct_0_28483_x1134_202070388}

[[关闭]{style="font-family:宋体"}[PTY]{lang="EN-US"}]{#struct_0_28483_x1134_202201460}[失败]{style="font-family:宋体"}

[[No user for session *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_202398068}

[[会话（]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_28483_x1134_202332532}[为]{style="font-family:宋体"}*[xx]{lang="EN-US"}*[）中没有用户]{style="font-family:宋体"}

[[Free space insufficient:]{lang="EN-US"}]{#struct_0_28483_x1134_201873777}

[[无剩余磁盘空间]{style="font-family:宋体"}]{#struct_0_28483_x1134_202004849}

[[Failed to get device free space]{lang="EN-US"}]{#struct_0_28483_x1134_201939313}

[[获取设备剩余磁盘空间失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_202135921}

[[Bad message from *xx* local user ]{lang="EN-US"}*[yy]{lang="EN-US"}*]{#struct_0_28483_x1134_202266993}

[[接收到本地用户]{style="font-family:宋体"}*[yy]{lang="EN-US"}*]{#struct_0_28483_x1134_202201457}[从地址]{style="font-family:宋体"}*[xx]{lang="EN-US"}*[发来的错误消息]{style="font-family:宋体"}

[[Unknown message *XX*]{lang="EN-US"}]{#struct_0_28483_x1134_202398065}

[[未知消息类型]{style="font-family:宋体"}]{#struct_0_28483_x1134_201873778}*[XX]{lang="EN-US"}*

[[Incoming queue grew unexpectedly]{lang="EN-US"}]{#struct_0_28483_x1134_201808242}

[[输入队列增长异常]{style="font-family:宋体"}]{#struct_0_28483_x1134_202004850}

[[Abnormal message length *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_201939314}

[[消息长度]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_202070386}[异常]{style="font-family:宋体"}

[[Read:]{lang="EN-US"}]{#struct_0_28483_x1134_202266994}

[[读操作]{style="font-family:宋体"}]{#struct_0_28483_x1134_202201458}

[[Write:]{lang="EN-US"}]{#struct_0_28483_x1134_202332530}

[[写操作]{style="font-family:宋体"}]{#struct_0_28483_x1134_2124188082}

[[Failed to set socket option SO_REUSEPORT:]{lang="EN-US"}]{#struct_0_28483_x1134_2124122546}

[[设置]{style="font-family:宋体"}[Socket]{lang="EN-US"}]{#struct_0_28483_x1134_2124253618}[选项]{style="font-family:宋体"}[SO_REUSEPORT]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to bind any address]{lang="EN-US"}]{#struct_0_28483_x1134_2124450226}

[[无法绑定任何地址]{style="font-family:宋体"}]{#struct_0_28483_x1134_2124384690}

[[Failed to run in a new session:]{lang="EN-US"}]{#struct_0_28483_x1134_2124515762}

[[无法在新的会话中运行]{style="font-family:宋体"}]{#struct_0_28483_x1134_2124712370}

[[All session info slots are busy now!]{lang="EN-US"}]{#struct_0_28483_x1134_2124188083}

[[会话信息满]{style="font-family:宋体"}]{#struct_0_28483_x1134_2124122547}

[[Failed to start new child:]{lang="EN-US"}]{#struct_0_28483_x1134_2124319155}

[[启动新的子进程失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_2124450227}

[[Failed to open config server]{lang="EN-US"}]{#struct_0_28483_x1134_2124384691}

[[无法打开配置服务]{style="font-family:宋体"}]{#struct_0_28483_x1134_2124581299}

[[User *xx* doesn\'t exist!]{lang="EN-US"}]{#struct_0_28483_x1134_2124515763}

[[用户]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_2124646835}[不存在]{style="font-family:宋体"}

[[Failed to disconnect from controlling tty]{lang="EN-US"}]{#struct_0_28483_x1134_2124188080}

[[从控制]{style="font-family:宋体"}[TTY]{lang="EN-US"}]{#struct_0_28483_x1134_2124319152}[断开连接失败]{style="font-family:宋体"}

[[Failed to open /dev/tty:]{lang="EN-US"}]{#struct_0_28483_x1134_2124253616}

[[打开]{style="font-family:宋体"}[/dev/tty]{lang="EN-US"}]{#struct_0_28483_x1134_2124450224}[失败]{style="font-family:宋体"}

[[Decodes terminal modes:]{lang="EN-US"}]{#struct_0_28483_x1134_2124581296}

[[解析终端模式]{style="font-family:宋体"}]{#struct_0_28483_x1134_2124515760}

[[Setting tty modes failed:]{lang="EN-US"}]{#struct_0_28483_x1134_2124712368}

[[设置]{style="font-family:宋体"}[TTY]{lang="EN-US"}]{#struct_0_28483_x1134_2124188081}[模式失败]{style="font-family:宋体"}

[[Failed to write authentication data]{lang="EN-US"}]{#struct_0_28483_x1134_2124122545}

[[写认证数据失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_2124319153}

[[Failed to read authentication response length]{lang="EN-US"}]{#struct_0_28483_x1134_2124450225}

[[读认证应答长度失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_2124384689}

[[Failed to read authentication response]{lang="EN-US"}]{#struct_0_28483_x1134_2124581297}

[[读认证应答失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_2124712369}

[[Bad string length *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_2124646833}

[[错误的串长度]{style="font-family:宋体"}]{#struct_0_28483_x1134_2124188078}*[xx]{lang="EN-US"}*

[[Failed to get peer name:]{lang="EN-US"}]{#struct_0_28483_x1134_2124319150}

[[获取对端主机名失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_2124253614}

[[Non-public channel ]{lang="FR"}]{#struct_0_28483_x1134_2124450222}*[xx]{lang="FR"}*[, type ]{lang="FR"}*[yy]{lang="FR"}*

[[非公用通道号]{style="font-family:宋体"}]{#struct_0_28483_x1134_2124581294}*[xx]{lang="FR"}*[，类型]{style="font-family:宋体"}*[yy]{lang="FR"}*

[[Failed to set socket options SO_REUSEADDR]{lang="EN-US"}]{#struct_0_28483_x1134_2124515758}

[[设置]{style="font-family:宋体"}[Socket]{lang="EN-US"}]{#struct_0_28483_x1134_2124646830}[选项]{style="font-family:宋体"}[SO_REUSEADDR]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Channel *xx*: connection failed:]{lang="EN-US"}]{#struct_0_28483_x1134_2124188079}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_2124319151}[：连接失败]{style="font-family:宋体"}

[[Use of DES is strongly discouraged due to cryptographic weaknesses]{lang="EN-US"}]{#struct_0_28483_x1134_2124253615}

[[不推荐使用]{style="font-family:宋体"}[DES]{lang="EN-US"}]{#struct_0_28483_x1134_2124384687}[算法，因为加密强度弱]{style="font-family:宋体"}

[[Kex protocol error:]{lang="EN-US"}]{#struct_0_28483_x1134_2124581295}

[[密钥交换协议错误]{style="font-family:宋体"}]{#struct_0_28483_x1134_2124712367}

[[Failed to get key type from name: ]{lang="EN-US"}]{#struct_0_28483_x1134_2124646831}

[[依据密钥名称获取密钥类型失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x604695273}

[[Failed to get key:]{lang="EN-US"}]{#struct_0_28483_x1134_x604564201}

[[获取密钥失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x604629737}

[[Unsupported key type ]{lang="EN-US"}]{#struct_0_28483_x1134_x604498665}*[xx]{lang="FR"}*

[[不支持的密钥类型]{style="font-family:宋体"}]{#struct_0_28483_x1134_x604367593}*[xx]{lang="FR"}*

[[Failed to sign key:]{lang="EN-US"}]{#struct_0_28483_x1134_x604170985}

[[密钥签名失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x604695272}

[[Failed to verify key:]{lang="EN-US"}]{#struct_0_28483_x1134_x604760808}

[[密钥验证失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x604564200}

[[Failed to get key by name \'*xx*\']{lang="EN-US"}]{#struct_0_28483_x1134_x604433128}

[[从密钥名字]{style="font-family:宋体"}]{#struct_0_28483_x1134_x604498664}*[xx]{lang="EN-US"}*[获取密钥实体失败]{style="font-family:宋体"}

[[Failed to get evpkey:]{lang="EN-US"}]{#struct_0_28483_x1134_x604367592}

[[获取]{style="font-family:宋体"}[EVP]{lang="EN-US"}]{#struct_0_28483_x1134_x604236520}[密钥失败]{style="font-family:宋体"}

[[Failed to read the file descriptor flags(*xx*):]{lang="EN-US"}]{#struct_0_28483_x1134_x604695275}

[[读取文件描述符标识]{style="font-family:宋体"}]{#struct_0_28483_x1134_x604760811}*[xx]{lang="EN-US"}*[失败]{style="font-family:宋体"}

[[Failed to set the file descriptor flags(*xx*):]{lang="EN-US"}]{#struct_0_28483_x1134_x604629739}

[[设置文件描述符标识]{style="font-family:宋体"}]{#struct_0_28483_x1134_x604433131}*[xx]{lang="EN-US"}*[失败]{style="font-family:宋体"}

[[Failed to get socket option TCP_NODELAY:]{lang="EN-US"}]{#struct_0_28483_x1134_x604302059}

[[设置]{style="font-family:宋体"}[Socket]{lang="EN-US"}]{#struct_0_28483_x1134_x604367595}[选项]{style="font-family:宋体"}[TCP_NODELAY]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to send message]{lang="EN-US"}]{#struct_0_28483_x1134_x604170987}

[[发送消息失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x604695274}

[[Failed to receive message header]{lang="EN-US"}]{#struct_0_28483_x1134_x604760810}

[[接收消息头失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x604629738}

[[Failed to receive message:]{lang="EN-US"}]{#struct_0_28483_x1134_x604433130}

[[接收消息失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x604302058}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x604367594}[: protocol error for unexpected state *yy*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x604236522}[：错误的状态]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[导致协议错误]{style="font-family:宋体"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x604695277}[: read failed for unexpected input state *yy*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x604564205}[：错误的输入状态]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[导致]{style="font-family:宋体"}[读失败]{style="font-family:宋体"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x604629741}[: protocol error for unexpected output state *yy*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x604498669}[：错误的输出状态]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[导致]{style="font-family:宋体"}[协议错误]{style="font-family:宋体"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x604302061}[: write failed]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x604170989}[：写错误]{style="font-family:宋体"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x604236525}[: write failed for unexpected output state *yy*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x604760812}[：错误的输出状态]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[导致]{style="font-family:宋体"}[写错误]{style="font-family:宋体"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x604629740}[: no empty buffer]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x604433132}[：无缓存空间]{style="font-family:宋体"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x604302060}[: internal error for unexpected output state *yy*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x604367596}[：错误的输出状态]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[导致]{style="font-family:宋体"}[内部错误]{style="font-family:宋体"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x604236524}[: cannot send IEOF for unexpected state *yy*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1774380250}[：错误的状态]{style="font-family:宋体"}*[y]{lang="EN-US"}[y]{lang="EN-US"}*[导致]{style="font-family:宋体"}[无法发送]{style="font-family:宋体"}[IEOF]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1774183642}[: cannot send SSH_MSG_CHANNEL_OUTPUT_CLOSE for unexpected state ]{lang="EN-US"}*[y]{lang="EN-US"}[y]{lang="EN-US"}*

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1774576858}[：错误的状态]{style="font-family:宋体"}*[y]{lang="EN-US"}[y]{lang="EN-US"}*[导致无法发送消息]{style="font-family:宋体"}[SSH_MSG_CHANNEL_OUTPUT_CLOSE]{lang="EN-US"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1774445786}[: SSH2_MSG_CHANNEL_CLOSE received twice]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1774511322}[：重复接收到]{style="font-family:宋体"}[SSH2_MSG_CHANNEL_CLOSE]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1774904538}[: write failed for unexpected output state *yy*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1774314715}[：错误的输出状态]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[导致]{style="font-family:宋体"}[写失败]{style="font-family:宋体"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1774183643}[: cannot send EOF for unexpected input state *yy*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1774576859}[：错误的输入状态]{style="font-family:宋体"}*[y]{lang="EN-US"}[y]{lang="EN-US"}*[导致]{style="font-family:宋体"}[无法发送]{style="font-family:宋体"}[EOF]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1774642395}[: cannot send CLOSE for input state/output state *yy*/*zz*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1774511323}[：错误的输入状态]{style="font-family:宋体"}*[xx]{lang="EN-US"}*[/]{lang="EN-US"}[输出]{style="font-family:
  宋体"}[状态]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[导致]{style="font-family:宋体"}[无法发送关闭消息]{style="font-family:宋体"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1774904539}[: already sent CLOSE]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1774314712}[：已经发送关闭消息]{style="font-family:宋体"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1774183640}[: failed to shutdown write:]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1774576856}[：]{style="font-family:宋体"}[shutdown]{lang="EN-US"}[写失败]{style="font-family:宋体"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1774642392}[: failed to close write:]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1774511320}[：关闭写失败]{style="font-family:宋体"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1774904536}[: failed to shutdown read:]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1774314713}[：]{style="font-family:宋体"}[shutdown]{lang="EN-US"}[读失败]{style="font-family:宋体"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1774183641}[: failed to close read:]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1774576857}[：关闭读失败]{style="font-family:宋体"}

[[Bad packet length ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1774445785}

[[错误的包长度]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1774511321}

[[Failed to set socket option IP_TOS ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1774904537}[:]{lang="EN-US"}

[[设置]{style="font-family:宋体"}[Socket]{lang="EN-US"}]{#struct_0_28483_x1134_1774380246}[选项]{style="font-family:宋体"}[IP_TOS]{lang="EN-US"}[值]{style="font-family:宋体"}*[xx]{lang="EN-US"}*[失败]{style="font-family:宋体"}

[[Bad max packet size ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1774183638}

[[错误的最大包大小]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1774576854}

[[Failed to ask password:]{lang="EN-US"}]{#struct_0_28483_x1134_1774445782}

[[获取密码失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_1774838998}

[[Failed to decrypt RSA private key]{lang="EN-US"}]{#struct_0_28483_x1134_1774904534}

[[解密]{style="font-family:宋体"}]{#struct_0_28483_x1134_1774380247}[RSA]{lang="EN-US"}[私钥失败]{style="font-family:宋体"}

[[RSA sign failed:]{lang="EN-US"}]{#struct_0_28483_x1134_1774249175}

[[RSA]{lang="EN-US"}]{#struct_0_28483_x1134_1774576855}[签名失败]{style="font-family:宋体"}

[[Failed to verify RSA:]{lang="EN-US"}]{#struct_0_28483_x1134_1774445783}

[[RSA]{lang="EN-US"}]{#struct_0_28483_x1134_1774838999}[验证失败]{style="font-family:宋体"}

[[Bad hash length]{lang="EN-US"}]{#struct_0_28483_x1134_x954568641}

[[错误的哈希长度]{style="font-family:宋体"}]{#struct_0_28483_x1134_x954503105}

[[Bad signature length]{lang="EN-US"}]{#struct_0_28483_x1134_x954634177}

[[错误的签名长度]{style="font-family:宋体"}]{#struct_0_28483_x1134_x954240961}

[[Failed to decrypt RSA public key:]{lang="EN-US"}]{#struct_0_28483_x1134_x954372033}

[[解密]{style="font-family:宋体"}]{#struct_0_28483_x1134_x954044353}[RSA]{lang="EN-US"}[公钥失败]{style="font-family:宋体"}

[[Bad decrypted length ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x954568640}

[[错误的解密长度]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x954699712}

[[Hash mismatch]{lang="EN-US"}]{#struct_0_28483_x1134_x954306496}

[[哈希不匹配]{style="font-family:宋体"}]{#struct_0_28483_x1134_x954240960}

[[Failed to get remote hostname]{lang="EN-US"}]{#struct_0_28483_x1134_x954372032}

[[获取远端主机名失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x953978816}

[[Failed to set socket option SO_KEEPALIVE:]{lang="EN-US"}]{#struct_0_28483_x1134_x954503107}

[[设置]{style="font-family:宋体"}[Socket]{lang="EN-US"}]{#struct_0_28483_x1134_x954634179}[选项]{style="font-family:宋体"}[SO_KEEPALIVE]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to initialize the INOTIFY]{lang="EN-US"}]{#struct_0_28483_x1134_x954306499}

[[初始化]{style="font-family:宋体"}]{#struct_0_28483_x1134_x954437571}[INOTIFY]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to get name info:]{lang="EN-US"}]{#struct_0_28483_x1134_x954044355}

[[获取名称信息失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x954568642}

[[Failed to set socket option:]{lang="EN-US"}]{#struct_0_28483_x1134_x954503106}

[[设置]{style="font-family:宋体"}[Socket]{lang="EN-US"}]{#struct_0_28483_x1134_x954634178}[选项失败]{style="font-family:宋体"}

[[Failed to change owner *xx* (0 0):]{lang="EN-US"}]{#struct_0_28483_x1134_x954240962}

[[改变]{style="font-family:宋体"}]{#struct_0_28483_x1134_x954372034}[owner]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to change mode *xx* (0666):]{lang="EN-US"}]{#struct_0_28483_x1134_x953978818}

[[改变]{style="font-family:宋体"}]{#struct_0_28483_x1134_x954568645}[mode]{lang="EN-US"}[失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[]{#struct_0_28483_x1134_x954503109}[[表1-2 ]{lang="EN-US"}[debugging ssh server event]{lang="EN-US"}]{#_Toc138241145}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1322991178}[[字段]{style="font-family:黑体"}]{#struct_0_28483_x1134_x537357159}

[[描述]{style="font-family:黑体"}]{#struct_0_28483_x1134_x365394821}

[[PAM: cleanup]{lang="EN-US"}]{#struct_0_28483_x1134_349238097}

[[清除]{style="font-family:宋体"}[PAM]{lang="EN-US"}]{#struct_0_28483_x1134_x211071035}[相关资源]{style="font-family:宋体"}

[[PAM: initializing for \\\"*xx*\\\", service: *yy*]{lang="EN-US"}]{#struct_0_28483_x1134_x1335141089}

[[为用户]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x954699717}[初始化]{style="font-family:宋体"}[PAM]{lang="EN-US"}[资源，服务类型为]{style="font-family:宋体"}*[yy]{lang="EN-US"}*

[[PAM: password authentication accepted for *xx*, level: *yy*, workdir: *zz*]{lang="EN-US"}]{#struct_0_28483_x1134_1383080711}

[*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_734492529}[用户]{style="font-family:宋体"}[PAM]{lang="EN-US"}[密码认证通过，级别为]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[，工作路径为]{style="font-family:宋体"}*[zz]{lang="EN-US"}*

[[PAM: password authentication failed for *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x913584799}

[*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x1812880141}[用户]{style="font-family:宋体"}[PAM]{lang="EN-US"}[密码认证失败]{style="font-family:宋体"}

[[Get default work dir: *xx*, return: *yy*]{lang="EN-US"}]{#struct_0_28483_x1134_769550373}

[[获取用户的默认工作路径]{style="font-family:宋体"}]{#struct_0_28483_x1134_x954634181}*[xx]{lang="EN-US"}*[，]{style="font-family:宋体"}[返回值]{style="font-family:宋体"}*[yy]{lang="EN-US"}*

[[Sending challenge \'*xx*\']{lang="EN-US"}]{#struct_0_28483_x1134_1034428519}

[[发送认证挑战字]{style="font-family:宋体"}]{#struct_0_28483_x1134_171424110}*[xx]{lang="EN-US"}*

[[Do authentication: invalid user *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_254054603}

[[认证进行中，非法用户]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x793281580}

[[Init keyboard interactive device:]{lang="EN-US"}]{#struct_0_28483_x1134_x954306501}

[[初始化键盘交互设备]{style="font-family:宋体"}]{#struct_0_28483_x1134_630077062}

[[SSH2 authentication challenge:]{lang="EN-US"}]{#struct_0_28483_x1134_x2045967008}

[[SSH2]{lang="EN-US"}]{#struct_0_28483_x1134_x167423166}[认证挑战信息]{style="font-family:宋体"}

[[Start SSH2 authentication challenge:]{lang="EN-US"}]{#struct_0_28483_x1134_x954240965}

[[开始]{style="font-family:宋体"}[SSH2]{lang="EN-US"}]{#struct_0_28483_x1134_1817637345}[认证挑战]{style="font-family:宋体"}[:]{lang="EN-US"}

[[Received *XX*]{lang="EN-US"}]{#struct_0_28483_x1134_x1443399302}

[[接收到消息]{style="font-family:宋体"}[XX]{lang="EN-US"}]{#struct_0_28483_x1134_x1414091362}[，消息类型可包括：]{style="font-family:宋体"}[SSH2_MSG_USERAUTH_INFO_RESPONSE]{lang="EN-US"}[、]{style="font-family:
  宋体"}[SSH2_MSG_SERVICE_REQUEST]{lang="EN-US"}[、]{style="font-family:宋体"}[SSH2_MSG_USERAUTH_REQUEST]{lang="EN-US"}[、]{style="font-family:宋体"}[SSH2_MSG_KEXINIT]{lang="EN-US"}[、]{style="font-family:宋体"}[SSH2_MSG_KEX_DH_GEX_REQUEST]{lang="EN-US"}[、]{style="font-family:宋体"}[SSH2_MSG_KEX_DH_GEX_REQUEST_OLD]{lang="EN-US"}[、]{style="font-family:宋体"}[SSH_CMSG_EOF]{lang="EN-US"}[、]{style="font-family:宋体"}[SSH_CMSG_WINDOW_SIZE]{lang="EN-US"}

[[Publickey authentication]{lang="EN-US"}]{#struct_0_28483_x1134_1688514045}

[[公钥认证]{style="font-family:宋体"}]{#struct_0_28483_x1134_x954437573}

[[Authentication result: *xx*, authentication algorithm: *yy*]{lang="EN-US"}]{#struct_0_28483_x1134_x2092711343}

[[认证结果]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1101637618}*[xx]{lang="EN-US"}*[（]{style="font-family:宋体"}[0]{lang="EN-US"}[或]{style="font-family:宋体"}[1]{lang="EN-US"}[）]{style="font-family:宋体"}[，认证算法]{style="font-family:宋体"}*[yy]{lang="EN-US"}*

[[Username: *xx*, service: *yy*, method: *zz*]{lang="EN-US"}]{#struct_0_28483_x1134_x300131764}

[[用户名]{style="font-family:宋体"}]{#struct_0_28483_x1134_x954372037}*[xx]{lang="EN-US"}*[，]{style="font-family:宋体"}[服务类型]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[，认证方法]{style="font-family:宋体"}*[zz]{lang="EN-US"}*

[[Try method *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x148371211}

[[尝试认证方法]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x1877637751}

[[Get authentication methods:]{lang="EN-US"}]{#struct_0_28483_x1134_1351151266}

[[获取到认证方法]{style="font-family:宋体"}]{#struct_0_28483_x1134_x954044357}

[[Connection closed by *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_638918452}

[[连接被关闭，对方]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_28483_x1134_x1251464202}[地址为]{style="font-family:宋体"}*[xx]{lang="EN-US"}*

[[Exited with status %d]{lang="EN-US"}]{#struct_0_28483_x1134_x953978821}

[[退出，状态为]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_357930948}

[[Received exit confirmation]{lang="EN-US"}]{#struct_0_28483_x1134_2043744952}

[[接收到退出确认]{style="font-family:宋体"}]{#struct_0_28483_x1134_x954568644}

[[Received SIGCHLD]{lang="EN-US"}]{#struct_0_28483_x1134_1749587782}

[[接收到]{style="font-family:宋体"}]{#struct_0_28483_x1134_1269234739}[SIGCHLD]{lang="EN-US"}[信号]{style="font-family:宋体"}

[[Entering interactive session for SSH2]{lang="EN-US"}]{#struct_0_28483_x1134_256714359}

[[进入]{style="font-family:宋体"}[SSH2]{lang="EN-US"}]{#struct_0_28483_x1134_x954503108}[交互会话阶段]{style="font-family:宋体"}

[[Need rekeying]{lang="EN-US"}]{#struct_0_28483_x1134_x537422695}

[[需要重新密钥协商]{style="font-family:宋体"}]{#struct_0_28483_x1134_1588710353}

[[Received session request]{lang="EN-US"}]{#struct_0_28483_x1134_x954699716}

[[收到会话请求]{style="font-family:宋体"}]{#struct_0_28483_x1134_1383146247}

[[Failed to open session, free channel *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x797876083}

[[打开会话失败，释放通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1112739814}

[[Received SSH2_MSG_CHANNEL_OPEN:]{lang="EN-US"}]{#struct_0_28483_x1134_x954634180}

[[接收到消息]{style="font-family:宋体"}]{#struct_0_28483_x1134_1034494055}[MSG_CHANNEL_OPEN]{lang="EN-US"}

[[Received SSH2_MSG_GLOBAL_REQUEST:]{lang="EN-US"}]{#struct_0_28483_x1134_x1333378522}

[[接收到消息]{style="font-family:宋体"}]{#struct_0_28483_x1134_x954306500}[SSH2_MSG_GLOBAL_REQUEST]{lang="EN-US"}

[[Received SSH2_MSG_CHANNEL_REQUEST:]{lang="EN-US"}]{#struct_0_28483_x1134_630011526}

[[接收到消息]{style="font-family:宋体"}]{#struct_0_28483_x1134_x526103283}[SSH2_MSG_GLOBAL_REQUEST]{lang="EN-US"}

[[Initiate server message dispatch, compatibility: *xx*/*yy*]{lang="EN-US"}]{#struct_0_28483_x1134_x954240964}

[[初始化服务器消息分发机制，兼容性：]{style="font-family:宋体"}]{#struct_0_28483_x1134_1817571809}*[xx]{lang="EN-US"}*[/*yy*]{lang="EN-US"}[，其中]{style="font-family:宋体"}*[xx]{lang="EN-US"}*[表示是否兼容]{style="font-family:宋体"}[2.0]{lang="EN-US"}[，]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[表示是否兼容]{style="font-family:宋体"}[1.3)]{lang="EN-US"}

[[Compression disabled]{lang="EN-US"}]{#struct_0_28483_x1134_1636798439}

[[取消压缩]{style="font-family:宋体"}]{#struct_0_28483_x1134_x954437572}

[[Received unsupported request:]{lang="EN-US"}]{#struct_0_28483_x1134_x2092645807}

[[接收到不支持的请求]{style="font-family:宋体"}]{#struct_0_28483_x1134_x349240100}

[[Exec command \'*xx*\']{lang="EN-US"}]{#struct_0_28483_x1134_x954372036}

[[执行命令]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x148305675}

[[Setup environment: user=*xx*, work directory=*yy*, level=*zz*]{lang="EN-US"}]{#struct_0_28483_x1134_x954044356}

[[设置环境变量：用户]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_638852916}[，工作路径]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[，权限级别]{style="font-family:宋体"}*[zz]{lang="EN-US"}*

[[Session id *xx* unused.]{lang="EN-US"}]{#struct_0_28483_x1134_x828430107}

[[会话]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x953978820}[设置为未使用]{style="font-family:宋体"}

[[Session info: used *xx*, next_unused *yy*, session_id *zz*, channel_id *mm*, pid *nn*]{lang="EN-US"}]{#struct_0_28483_x1134_357996484}

[[会话信息：是否被使用]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1171520997}[，下一个未使用]{style="font-family:宋体"}[session ID *yy* ]{lang="EN-US"}[，会话]{style="font-family:宋体"}[ID zz]{lang="EN-US"}[，通道号]{style="font-family:宋体"}*[mm]{lang="EN-US"}*[，进程]{style="font-family:宋体"}[ID *nn*]{lang="EN-US"}

[[Session opened: session *xx*, link with channel *yy*]{lang="EN-US"}]{#struct_0_28483_x1134_611515300}

[[会话打开成功，会话]{style="font-family:宋体"}[ID *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x2037347986}[，关联通道]{style="font-family:宋体"}*[yy]{lang="EN-US"}*

[[Channel request: user *xx*, service type *yy*]{lang="EN-US"}]{#struct_0_28483_x1134_x1468040627}

[[通道请求：用户]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_611580836}[，服务类型]{style="font-family:宋体"}*[yy]{lang="EN-US"}*

[[Release channel *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_265063806}

[[释放通道，通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_611384228}

[[Close session: session *xx*, pid *yy*]{lang="EN-US"}]{#struct_0_28483_x1134_43581290}

[[关闭会话，会话]{style="font-family:宋体"}[ID *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x1190640403}[，进程]{style="font-family:宋体"}[ID *yy*]{lang="EN-US"}

[[Request *xx*: sent status *yy*]{lang="EN-US"}]{#struct_0_28483_x1134_611449764}

[[请求序列号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x122070085}[，发送状态]{style="font-family:宋体"}*[yy]{lang="EN-US"}*

[[Failed to get full file name from \\\"*xx*\\\"]{lang="EN-US"}]{#struct_0_28483_x1134_611777444}

[[从]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x607602431}[获取全路径文件名失败]{style="font-family:宋体"}

[[Received client version *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x1313863572}

[[接收到客户端版本]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_611842980}

[[Nothing at all written]{lang="EN-US"}]{#struct_0_28483_x1134_1108023129}

[[未写入任何数据]{style="font-family:宋体"}]{#struct_0_28483_x1134_611646372}

[[Old state mode *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_938576205}

[[旧的状态码]{style="font-family:宋体"}]{#struct_0_28483_x1134_611711908}*[xx]{lang="EN-US"}*

[[New state mode *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x241887356}

[[新的状态码]{style="font-family:宋体"}]{#struct_0_28483_x1134_1093388998}*[xx]{lang="EN-US"}*

[[Read EOF]{lang="EN-US"}]{#struct_0_28483_x1134_612039588}

[[读]{style="font-family:宋体"}[EOF]{lang="EN-US"}]{#struct_0_28483_x1134_2108733423}

[[RSA key re-generation complete, return *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_612105124}

[[重新生成]{style="font-family:宋体"}[RSA]{lang="EN-US"}]{#struct_0_28483_x1134_x1451259150}[密钥，返回值]{style="font-family:宋体"}*[xx]{lang="EN-US"}*

[[Client protocol version *x.y*, client software version *zz*]{lang="EN-US"}]{#struct_0_28483_x1134_611515301}

[[客户端协议版本]{style="font-family:宋体"}*[x.y]{lang="EN-US"}*]{#struct_0_28483_x1134_x2037347987}[，客户端软件版本]{style="font-family:宋体"}*[zz]{lang="EN-US"}*

[[Hostkey string]{lang="EN-US"}]{#struct_0_28483_x1134_611580837}

[[主机密钥串]{style="font-family:宋体"}]{#struct_0_28483_x1134_265063807}

[[Server listening on *xx* port *yy*]{lang="EN-US"}]{#struct_0_28483_x1134_125222318}

[[服务器启动监听]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_28483_x1134_611384229}[地址]{style="font-family:宋体"}*[xx]{lang="EN-US"}*[、端口]{style="font-family:宋体"}*[yy]{lang="EN-US"}*

[[Failed to get remote port]{lang="EN-US"}]{#struct_0_28483_x1134_43581291}

[[获取远端端口号失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_611449765}

[[Drop connection *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x122070084}

[[丢弃连接，其中]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_611777445}[为文件描述句柄号]{style="font-family:宋体"}

[[Start new child *xx*.]{lang="EN-US"}]{#struct_0_28483_x1134_611842981}

[[启动新的子进程，其中]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1108023130}[为进程]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[SSH1 key exchange]{lang="EN-US"}]{#struct_0_28483_x1134_260288336}

[[SSH1]{lang="EN-US"}]{#struct_0_28483_x1134_611646373}[协议密钥交换]{style="font-family:宋体"}

[[Sent *xx* bit server key and yy bit host key]{lang="EN-US"}]{#struct_0_28483_x1134_938576206}

[[发送]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_611711909}[位的服务器密钥和]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[位的主机密钥]{style="font-family:宋体"}

[[Encryption type:]{lang="EN-US"}]{#struct_0_28483_x1134_x241887357}

[[加密套件]{style="font-family:宋体"}]{#struct_0_28483_x1134_612039589}

[[Received session key, encryption turned on]{lang="EN-US"}]{#struct_0_28483_x1134_612105125}

[[接收到会话密钥，启动加密]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1451259149}

[[KEX done]{lang="EN-US"}]{#struct_0_28483_x1134_611515298}

[[密钥交换结束]{style="font-family:宋体"}]{#struct_0_28483_x1134_1118502417}

[[Failed to send data to pid *xx*, return *yy*]{lang="EN-US"}]{#struct_0_28483_x1134_611580834}

[[发送数据到进程]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_265063804}[失败，返回值]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[ ]{lang="EN-US"}[（]{style="font-family:
  宋体"}[-1]{lang="EN-US"}[或成功发送的字节数值）]{style="font-family:宋体"}

[[Failed to get session info by user pid *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_611384226}

[[依据用户进程]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_43581296}[获取会话信息失败]{style="font-family:宋体"}

[[Failed to send session info to SSHD, return *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_611449762}

[[向]{style="font-family:宋体"}[SSHD]{lang="EN-US"}]{#struct_0_28483_x1134_x122070087}[守护进程发送会话信息失败，返回值]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[（]{style="font-family:宋体"}[-1]{lang="EN-US"}[或成功发送的字节数值）]{style="font-family:宋体"}

[[Delete user *xx* successfully]{lang="EN-US"}]{#struct_0_28483_x1134_611777442}[！]{style="font-family:宋体"}

[[成功删除用户]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x607602425}

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_611842978}[read_fd *yy* is a TTY]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_770316129}[：读连接]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[是]{style="font-family:宋体"}[TTY]{lang="EN-US"}

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_611646370}[big output buffer *yy* \> *zz*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_611711906}[：较大的输出缓存，实际值]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[\>]{lang="EN-US"}[最大值]{style="font-family:
  宋体"}*[zz]{lang="EN-US"}*

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_x241887362}[request *yy* confirm *zz*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_612039586}[：请求]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[、确认]{style="font-family:宋体"}*[zz]{lang="EN-US"}*

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_2108733421}[closing]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_612105122}[：关闭中]{style="font-family:宋体"}

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_x1451259144}[connected to *yy* port *zz*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_611515299}[：连接到]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[、端口]{style="font-family:宋体"}*[zz]{lang="EN-US"}*

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_611580835}[not open]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_265063805}[：未打开]{style="font-family:宋体"}

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_611384227}[input draining]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_43581297}[：输出关闭中]{style="font-family:宋体"}

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_611449763}[Failed to filter]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_611777443}[：停止过滤]{style="font-family:宋体"}

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_x607602426}[window *yy* sent adjust *zz*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_611842979}[：窗口]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[发送调整量]{style="font-family:宋体"}*[zz]{lang="EN-US"}*

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_770316130}[garbage collecting]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_611646371}[：资源回收中]{style="font-family:宋体"}

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_611711907}[sent extended data *yy*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x241887363}[：发送扩展数据]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[字节]{style="font-family:宋体"}

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_612039587}[accepting extended_data after EOF]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_2108733420}[：]{style="font-family:宋体"}[EOF]{lang="EN-US"}[状态后收到了扩展数据]{style="font-family:宋体"}

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_612105123}[received too much extended data *yy* bytes, window_size *zz*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_611515296}[：接收太多的扩展数据]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[，窗口大小]{style="font-family:宋体"}*[zz]{lang="EN-US"}*

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_1118502411}[received extended data *yy* bytes]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_611580832}[：接收扩展数据]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[字节]{style="font-family:宋体"}

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_611384224}[FORCE input drain]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_43581294}[：输入强行关闭]{style="font-family:宋体"}

[[Bad cipher *xx* \[*yy*\]]{lang="EN-US"}]{#struct_0_28483_x1134_611449760}

[[错误的加密套件]{style="font-family:宋体"}[xx \[]{lang="EN-US"}]{#struct_0_28483_x1134_611777440}[收到的完整的加密套件串列表]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[\]]{lang="EN-US"}

[[Enabling compatibility mode for protocol 2.0]{lang="EN-US"}]{#struct_0_28483_x1134_x607602427}

[[使能兼容]{style="font-family:宋体"}[2.0]{lang="EN-US"}]{#struct_0_28483_x1134_611842976}[版本]{style="font-family:宋体"}

[[Enabling compatibility mode for protocol 1.3]{lang="EN-US"}]{#struct_0_28483_x1134_770316127}

[[使能兼容]{style="font-family:宋体"}[1.3]{lang="EN-US"}]{#struct_0_28483_x1134_611646368}[版本]{style="font-family:宋体"}

[[Enabling compression at level *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_611711904}

[[使能]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x241887360}[等级的压缩算法]{style="font-family:宋体"}

[[Compress outgoing: raw data *xx* bytes, compressed *yy* bytes, factor *zz*]{lang="EN-US"}]{#struct_0_28483_x1134_612039584}

[[压缩输出：原始数据]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_612105120}[字节，压缩后为]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[字节，比例为]{style="font-family:宋体"}*[zz]{lang="EN-US"}*

[[Compress incoming: raw data *xx* bytes, compressed *yy* bytes, factor *zz*]{lang="EN-US"}]{#struct_0_28483_x1134_x1451259146}

[[压缩输入：原始数据]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_611515297}[字节，压缩后为]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[字节，比例为]{style="font-family:宋体"}*[zz]{lang="EN-US"}*

[[Installing CRC compensation attack detector]{lang="EN-US"}]{#struct_0_28483_x1134_611580833}

[[安装]{style="font-family:宋体"}[CRC]{lang="EN-US"}]{#struct_0_28483_x1134_265063811}[补偿攻击探测器]{style="font-family:宋体"}

[[Kex strings(*xx*):]{lang="EN-US"}]{#struct_0_28483_x1134_611384225}

[[密钥交互串信息，]{style="font-family:宋体"}[xx]{lang="EN-US"}]{#struct_0_28483_x1134_611449761}[取值代表如下涵义：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_28483_x1134_611777441}[：密钥交换算法串；]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_28483_x1134_x607602428}[：服务器端支持的主机公钥算法串；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_28483_x1134_611842977}[：客户端到服务器端的加密算法串；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_28483_x1134_611646369}[：服务器端到客户端的加密算法串；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_28483_x1134_x1400075948}[：客户端到服务器端的]{style="font-family:宋体"}[HMAC]{lang="EN-US"}[算法串；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5]{lang="EN-US"}]{#struct_0_28483_x1134_611711905}[：服务器端到客户端的]{style="font-family:宋体"}[HMAC]{lang="EN-US"}[算法串；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6]{lang="EN-US"}]{#struct_0_28483_x1134_612039585}[：客户端到服务器端的压缩算法串；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[7]{lang="EN-US"}]{#struct_0_28483_x1134_612105121}[：服务器端到客户端的压缩算法串；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[8]{lang="EN-US"}]{#struct_0_28483_x1134_x1451259145}[：客户端到服务器端的语言选择串；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[9]{lang="EN-US"}]{#struct_0_28483_x1134_x2117368055}[：服务器端到客户端的语言选择串]{style="font-family:宋体"}

[[Proposal mismatch:]{lang="EN-US"}]{#struct_0_28483_x1134_x2117302519}

[[密钥交互串匹配失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x2117499127}

[[My proposal kex:]{lang="EN-US"}]{#struct_0_28483_x1134_x963925986}

[[我的密钥交互串]{style="font-family:宋体"}]{#struct_0_28483_x1134_x2117433591}

[[Peer proposal kex:]{lang="EN-US"}]{#struct_0_28483_x1134_x2117105911}

[[对方的密钥交互串]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1029039115}

[[Kex: *xx*, Encrypt: *yy*, HMAC: *zz*, Compress: *mm*]{lang="EN-US"}]{#struct_0_28483_x1134_x2117040375}

[[密钥交换算法]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x2117236983}[，加密算法]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[，摘要算法]{style="font-family:宋体"}*[zz]{lang="EN-US"}*[，压缩算法]{style="font-family:宋体"}*[mm]{lang="EN-US"}*

[[Bad HAMC *xx* \[*yy*\]]{lang="EN-US"}]{#struct_0_28483_x1134_x2117171447}

[[错误的摘要算法]{style="font-family:宋体"}*[xx]{lang="EN-US"}*[\[]{lang="EN-US"}]{#struct_0_28483_x1134_788047307}[摘要算法串]{style="font-family:
  宋体"}*[yy]{lang="EN-US"}*[\]]{lang="EN-US"}

[[Send message: type *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x2116843767}

[[发送消息：消息类型]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x2116778231}

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_x2117368054}[input state: *xx* -\> *yy*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x1308915277}[：输入状态由]{style="font-family:宋体"}*[xx]{lang="EN-US"}*[状态切换到]{style="font-family:宋体"}*[yy]{lang="EN-US"}*

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_x2117302518}[output state: *xx* -\> *yy*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x2117499126}[：输出状态由]{style="font-family:宋体"}*[xx]{lang="EN-US"}*[状态切换到]{style="font-family:宋体"}*[yy]{lang="EN-US"}*

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_x2117433590}[received *XX*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x2117105910}[：接收到消息]{style="font-family:宋体"}*[XX]{lang="EN-US"}*

[[Channel *xx*: read failed]{lang="EN-US"}]{#struct_0_28483_x1134_537044826}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x2117040374}[：读数据失败]{style="font-family:宋体"}

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_x2117236982}[send *XX*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x2117171446}[：发送消息]{style="font-family:宋体"}*[XX]{lang="EN-US"}*

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_x2116843766}[write failed]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_316911763}[：写失败]{style="font-family:宋体"}

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_x2116778230}[mode=*yy*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x2117368057}[：新的模式]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[（]{style="font-family:宋体"}[0]{lang="EN-US"}[和]{style="font-family:宋体"}[1]{lang="EN-US"}[，分别对应]{style="font-family:宋体"}[MODE_IN]{lang="EN-US"}[或者]{style="font-family:宋体"}[MODE_OUT]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Expecting packet type ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x2117302521}

[[期望收到包类型]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x1961878551}

[[Remote message:]{lang="EN-US"}]{#struct_0_28483_x1134_x2117499129}

[[远端发来的信息]{style="font-family:宋体"}]{#struct_0_28483_x1134_x2117433593}

[[Set max packet size to ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x2117105913}

[[设置最大包大小为]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x2117040377}

[[Read passphrase:]{lang="EN-US"}]{#struct_0_28483_x1134_x2117236985}

[[读取密码]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1283779590}

[[Sent message: type ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x2117171449}[, ID ]{lang="EN-US"}*[yy]{lang="EN-US"}*

[[发送消息：类型为]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x2116843769}[，消息]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[yy]{lang="EN-US"}*

[[DSA verify:]{lang="EN-US"}]{#struct_0_28483_x1134_x2116778233}

[[DSA]{lang="EN-US"}]{#struct_0_28483_x1134_x2117368056}[验证]{style="font-family:宋体"}

[[RSA verify]{lang="EN-US"}]{#struct_0_28483_x1134_x2117302520}

[[RSA]{lang="EN-US"}]{#struct_0_28483_x1134_x395794610}[验证]{style="font-family:宋体"}

[[Ignoring unsupported tty mode, opcode *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x2117499128}

[[忽略不支持的]{style="font-family:宋体"}[TTY]{lang="EN-US"}]{#struct_0_28483_x1134_x2117433592}[模式，操作码为]{style="font-family:宋体"}*[xx]{lang="EN-US"}*

[[Found matching *xx* key, key finger is *yy*]{lang="EN-US"}]{#struct_0_28483_x1134_x2117105912}

[[找到匹配的]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x2117040376}[类型的密钥，密钥指纹串为]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[。其中，可能是]{style="font-family:宋体"}[RSA]{lang="EN-US"}[、]{style="font-family:宋体"}[RSA]{lang="EN-US"}[、]{style="font-family:宋体"}[DSA]{lang="EN-US"}

[[Failed to get domain from 'xx']{lang="EN-US"}]{#struct_0_28483_x1134_x1898889824}

[[从用户名]{style="font-family:宋体"}[xx]{lang="EN-US"}]{#struct_0_28483_x1134_x1898955360}[中获取]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域名失败]{style="font-family:宋体"}

[[Failed *mm* for xx from yy port zzz ssh2]{lang="EN-US"}]{#struct_0_28483_x1134_x1898496608}

[[用户使用]{style="font-family:宋体"}*[mm]{lang="EN-US"}*]{#struct_0_28483_x1134_x1898562144}[认证方式认证失败，用户名为]{style="font-family:宋体"}[xx]{lang="EN-US"}[，用户]{style="font-family:宋体"}[IP]{lang="EN-US"}[为]{style="font-family:宋体"}[yy]{lang="EN-US"}[，源端口号为]{style="font-family:宋体"}[zz]{lang="EN-US"}[。]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging ssh server message]{lang="EN-US"}]{#struct_0_28483_x1134_468037750}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1284197418}[[字段]{style="font-family:黑体"}]{#struct_0_28483_x1134_x1531723744}

[[描述]{style="font-family:黑体"}]{#struct_0_28483_x1134_1594394248}

[[Prepare packet\[*xx*\]]{lang="DE"}]{#struct_0_28483_x1134_x2117236984}

[[准备消息]{style="font-family:宋体"}[\[]{lang="EN-US"}]{#struct_0_28483_x1134_1445103765}[消息类型]{style="font-family:宋体"}*[xx]{lang="EN-US"}*[\]]{lang="EN-US"}

[[Compression: raw_len *xx*, compressed_len *yy*]{lang="DE"}]{#struct_0_28483_x1134_298110750}

[[数据压缩：原始数据大小为]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x425015199}[，压缩后数据大小为]{style="font-family:宋体"}*[yy]{lang="EN-US"}*

[[Input: Length before de-compress *xx*, length after de-compress *yy*]{lang="EN-US"}]{#struct_0_28483_x1134_x1731550566}

[[输入：解压前数据长度为]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x2117171448}[，解压后数据长度为]{style="font-family:宋体"}*[yy]{lang="EN-US"}*

[[Received packet type *xx*]{lang="DE"}]{#struct_0_28483_x1134_x1228375328}

[[接收到消息]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x1409191573}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_28483_x1134_x253943047}

[[\# ]{lang="EN-US"}]{#struct_0_28483_x1134_1497339161}[打开]{style="font-family:宋体"}[SSH]{lang="EN-US"}[服务器端的错误调试信息开关。远端用户]{style="font-family:宋体"}[abc]{lang="EN-US"}[从]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.0.59]{lang="EN-US"}[的客户端上登录本设备，第一次输入密码错误。]{style="font-family:宋体"}

[[\<Sysname\> debugging ssh server error]{lang="EN-US"}]{#struct_0_28483_x1134_x815448229}

[%Dec 31 17:50:35:219 2009 Sysname SSHS/6/SSHLOG: Failed password for abc from 192.168.0.59 port 2628 ssh2]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x990021769}*[来自]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[192.168.0.59]{lang="EN-US"}[、端口]{style="font-family:宋体"}[2628]{lang="EN-US"}[的用户]{style="font-family:宋体"}[abc]{lang="EN-US"}[登录设备，密码认证失败（日志信息）]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_28483_x1134_x2116843768}[远端用户第二次输入正确的密码，成功登录本设备。]{style="font-family:宋体"}

[[%Dec 31 17:50:48:996 2009 Sysname SSHS/6/SSHLOG: Accepted password for abc from 192.1]{lang="EN-US"}]{#struct_0_28483_x1134_x1202118011}[68.0.59 port 2628 ssh2]{lang="PT-BR"}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_1099517949}*[来自]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[192.168.0.59]{lang="EN-US"}[、端口]{style="font-family:宋体"}[2628]{lang="EN-US"}[的用户]{style="font-family:宋体"}[abc]{lang="EN-US"}[登录设备，密码认证成功（日志信息）]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_28483_x1134_x1174680415}[远端用户执行]{style="font-family:宋体"}[quit]{lang="EN-US"}[命令退出。]{style="font-family:宋体"}

[[%Dec 31 17:50:51:874 2009 Sysname SSHS/6/SSHLOG: Protocol dispatch error: type 24, seq 15.]{lang="PT-BR"}]{#struct_0_28483_x1134_1378751646}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_1381941263}*[协议消息分发处理失败，消息类型]{style="font-family:宋体"}[24]{lang="EN-US"}[，请求序号]{style="font-family:宋体"}[15]{lang="EN-US"}[（日志信息）]{style="font-family:宋体"}*

[[\*Dec 31 17:50:51:879 2009 Sysname SSHS/3/ERROR: Read error from remote host 192.168.0.59: Connection reset by peer]{lang="EN-US"}]{#struct_0_28483_x1134_1265363688}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x2116778232}*[从远端主机]{style="font-family:宋体"}[192.168.0.59]{lang="EN-US"}[上读取数据错误，对端已关闭连接（调试信息）]{style="font-family:宋体"}*

[[%Dec 31 17:50:51:897 2009 Sysname SSHS/6/SSHLOG: Received signal SIGCHLD! pid = 167.]{lang="EN-US"}]{#struct_0_28483_x1134_x1814565645}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_1998513712}*[接收到]{style="font-family:宋体"}[SIGCHLD]{lang="EN-US"}[信号，]{style="font-family:宋体"}[PID]{lang="EN-US"}[为]{style="font-family:宋体"}[167]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_28483_x1134_x1993016774}[打开]{style="font-family:宋体"}[SSH]{lang="EN-US"}[服务器端的事件调试信息开关。远端用户从]{style="font-family:宋体"}[192.168.0.58]{lang="EN-US"}[上通过]{style="font-family:宋体"}[putty]{lang="EN-US"}[客户端登录本设备，用户名为]{style="font-family:宋体"}[abc]{lang="EN-US"}[、密码为]{style="font-family:宋体"}[abc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> debugging ssh server event]{lang="EN-US"}]{#struct_0_28483_x1134_998188117}

[\*Dec 31 17:58:29:819 2009 Sysname SSHS/7/EVENT: Start new child 135.]{lang="EN-US"}

[\*Dec 31 17:58:29:841 2009 Sysname SSHS/6/EVENT: Connection from 192.168.0.58 port 1476]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x805827934}*[用户从]{style="font-family:宋体"}[192.168.0.58]{lang="EN-US"}[的]{style="font-family:宋体"}[1476]{lang="EN-US"}[端口发起连接请求，用户进程]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[135]{lang="EN-US"}*

[[\*Dec 31 17:58:29:873 2009 Sysname SSHS/7/EVENT: Client protocol version 2.0, client software version PuTTY_Release_0.60]{lang="EN-US"}]{#struct_0_28483_x1134_1289179064}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_2123056920}*[客户端]{style="font-family:宋体"}[SSH]{lang="EN-US"}[协议版本号]{style="font-family:宋体"}[2.0]{lang="EN-US"}[，客户端软件版本信息为]{style="font-family:宋体"}[PuTTY_Release_0.60]{lang="EN-US"}*

[[\*Dec 31 17:58:29:888 2009 Sysname SSHS/7/EVENT: Enabling compatibility mode for protocol 2.0]{lang="EN-US"}]{#struct_0_28483_x1134_x2117368059}

[\*Dec 31 17:58:29:897 2009 Sysname SSHS/7/EVENT: Local version string SSH-2.0-Comware-7]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x1261861110}*[发给客户端的服务器端版本串信息（版本中的]{style="font-family:宋体"}[Comware-7]{lang="EN-US"}[与产品型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}*

[[\*Dec 31 17:58:29:947 2009 Sysname SSHS/7/EVENT: Hostkey string is : ssh-dss,ssh-rsa]{lang="EN-US"}]{#struct_0_28483_x1134_x1802235540}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x19206695}*[主机公钥串为]{style="font-family:宋体"}[ssh-dss]{lang="EN-US"}[、]{style="font-family:宋体"}[ssh-rsa]{lang="EN-US"}[，即支持]{style="font-family:宋体"}[DSA]{lang="EN-US"}[和]{style="font-family:宋体"}[RSA]{lang="EN-US"}[公钥算法]{style="font-family:宋体"}*

[[\*Dec 31 17:58:29:988 2009 Sysname SSHS/7/EVENT: Received SSH2_MSG_KEXINIT.]{lang="EN-US"}]{#struct_0_28483_x1134_1040387698}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_1261567211}*[收到]{style="font-family:宋体"}[SSH2_MSG_KEXINIT]{lang="EN-US"}[消息]{style="font-family:宋体"}*

[[\*Dec 31 17:58:29:993 2009 Sysname SSHS/7/EVENT: My proposal kex:]{lang="EN-US"}]{#struct_0_28483_x1134_1549108071}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x2117302523}*[服务器端的版本协商算法串信息如下]{style="font-family:宋体"}*

[[\*Dec 31 17:58:30:29 2009 Sysname SSHS/7/EVENT: Kex strings(0): diffie-hellman-group-exchange-sha1,diffie-hellman-group14-sha1,diffie-hellman-group1-sha1]{lang="EN-US"}]{#struct_0_28483_x1134_1170289331}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x1444275245}*[密钥交换算法串]{style="font-family:宋体"}*

[[\*Dec 31 17:58:30:35 2009 Sysname SSHS/7/EVENT: Kex strings(1): ssh-dss,ssh-rsa]{lang="EN-US"}]{#struct_0_28483_x1134_1952603401}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_385992446}*[服务器端支持的主机公钥算法串]{style="font-family:宋体"}*

[[\*Dec 31 17:58:30:43 2009 Sysname SSHS/7/EVENT: Kex strings(2): aes128-cbc,3des-cbc,des-cbc]{lang="EN-US"}]{#struct_0_28483_x1134_x216708862}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_246118294}*[客户端到服务器端的加密算法串]{style="font-family:宋体"}*

[[\*Dec 31 17:58:30:48 2009 Sysname SSHS/7/EVENT: Kex strings(3): aes128-cbc,3des-cbc,des-cbc]{lang="EN-US"}]{#struct_0_28483_x1134_x2117499131}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_198807892}*[服务器端到客户端的加密算法串]{style="font-family:宋体"}*

[[\*Dec 31 17:58:30:59 2009 Sysname SSHS/7/EVENT: Kex strings(4): hmac-sha1,hmac-sha1-96,hmac-md5,hmac-md5-96]{lang="EN-US"}]{#struct_0_28483_x1134_x1385639268}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x880918618}*[客户端到服务器端的]{style="font-family:宋体"}[HMAC]{lang="EN-US"}[算法串]{style="font-family:宋体"}*

[[\*Dec 31 17:58:30:67 2009 Sysname SSHS/7/EVENT: Kex strings(5): hmac-sha1,hmac-sha1-96,hmac-md5,hmac-md5-96]{lang="EN-US"}]{#struct_0_28483_x1134_1007853688}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_1449766479}*[服务器端到客户端的]{style="font-family:宋体"}[HMAC]{lang="EN-US"}[算法串]{style="font-family:宋体"}*

[[\*Dec 31 17:58:30:76 2009 Sysname SSHS/7/EVENT: Kex strings(6): none,zlib,zlib@openssh.com]{lang="EN-US"}]{#struct_0_28483_x1134_835487706}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x1546383513}*[客户端到服务器端的压缩算法串]{style="font-family:宋体"}*

[[\*Dec 31 17:58:30:82 2009 Sysname SSHS/7/EVENT: Kex strings(7): none,zlib,zlib@openssh.com]{lang="EN-US"}]{#struct_0_28483_x1134_x2117433595}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x1697442834}*[服务器端到客户端的压缩算法串]{style="font-family:宋体"}*

[[\*Dec 31 17:58:30:91 2009 Sysname SSHS/7/EVENT: Kex strings(8):]{lang="EN-US"}]{#struct_0_28483_x1134_1966544992}

[\*Dec 31 17:58:30:96 2009 Sysname SSHS/7/EVENT: Kex strings(9):]{lang="EN-US"}

*[ ]{lang="EN-US"}*

[\*Dec 31 17:58:30:104 2009 Sysname SSHS/7/EVENT: Peer proposal kex:]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x1470159458}*[客户端的版本协商算法串信息如下]{style="font-family:宋体"}*

[[\*Dec 31 17:58:30:111 2009 Sysname SSHS/7/EVENT: Kex strings(0): diffie-hellman-group-exchange-sha256,diffie-hellman-group-exchange-sha1,diffie-hellman-group14-sha1,diffie-hellman-group1-sha1]{lang="EN-US"}]{#struct_0_28483_x1134_128377689}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x1749000128}*[密钥交换算法串]{style="font-family:宋体"}*

[[\*Dec 31 17:58:30:147 2009 Sysname SSHS/7/EVENT: Kex strings(1): ssh-rsa,ssh-dss]{lang="EN-US"}]{#struct_0_28483_x1134_1951936222}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x1836292026}*[服务器端支持的主机公钥算法串]{style="font-family:宋体"}*

[[\*Dec 31 17:58:30:153 2009 Sysname SSHS/7/EVENT: Kex strings(2): aes256-ctr,aes256-cbc,rijndael-cbc@lysator.liu.se,aes192-ctr,aes192-cbc,aes128-ctr,aes128-cbc,blowfish-ctr,blowfish-cbc,3des-ctr,3des-cbc,arcfour256,arcfour128]{lang="EN-US"}]{#struct_0_28483_x1134_x2117105915}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_940329353}*[服务器端支持的加密算法串]{style="font-family:宋体"}*

[[\*Dec 31 17:58:30:162 2009 Sysname SSHS/7/EVENT: Kex strings(3): aes256-ctr,aes256-cbc,rijndael-cbc@lysator.liu.se,aes192-ctr,aes192-cbc,aes128-ctr,aes128-cbc,blowfish-ctr,blowfish-cbc,3des-ctr,3des-cbc,arcfour256,arcfour128]{lang="EN-US"}]{#struct_0_28483_x1134_194694422}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x1969852351}*[服务器端到客户端的加密算法串]{style="font-family:宋体"}*

[[\*Dec 31 17:58:30:170 2009 Sysname SSHS/7/EVENT: Kex strings(4): hmac-sha1,hmac-sha1-96,hmac-md5]{lang="EN-US"}]{#struct_0_28483_x1134_x714969791}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_985203525}*[客户端到服务器端的]{style="font-family:宋体"}[HMAC]{lang="EN-US"}[算法串]{style="font-family:宋体"}*

[[\*Dec 31 17:58:30:171 2009 Sysname SSHS/7/EVENT: Kex strings(5): hmac-sha1,hmac-sha1-96,hmac-md5]{lang="EN-US"}]{#struct_0_28483_x1134_580909973}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x2117040379}*[服务器端到客户端的]{style="font-family:宋体"}[HMAC]{lang="EN-US"}[算法串]{style="font-family:宋体"}*

[[\*Dec 31 17:58:30:172 2009 Sysname SSHS/7/EVENT: Kex strings(6): none,zlib]{lang="EN-US"}]{#struct_0_28483_x1134_1677891331}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x101400730}*[客户端到服务器端的压缩算法]{style="font-family:宋体"}*

[[\*Dec 31 17:58:30:173 2009 Sysname SSHS/7/EVENT: Kex strings(7): none,zlib]{lang="EN-US"}]{#struct_0_28483_x1134_1602744675}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_1246229997}*[客户端到服务器端的压缩算法]{style="font-family:宋体"}*

[[\*Dec 31 17:58:30:174 2009 Sysname SSHS/7/EVENT: Kex strings(8):]{lang="EN-US"}]{#struct_0_28483_x1134_x845652606}

[\*Dec 31 17:58:30:243 2009 Sysname SSHS/7/EVENT: Kex strings(9):]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Dec 31 17:58:30:248 2009 Sysname SSHS/7/EVENT: Kex: client-\>server, Encrypt: aes128-cbc, HMAC: hmac-sha1, Compress: none]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_687220826}*[协商出来的客户端到服务器端的加密算法、]{style="font-family:宋体"}[HMAC]{lang="EN-US"}[算法和压缩算法]{style="font-family:宋体"}*

[[\*Dec 31 17:58:30:253 2009 Sysname SSHS/7/EVENT: Kex: server-\>client, Encrypt: aes128-cbc, HMAC: hmac-sha1, Compress: none]{lang="EN-US"}]{#struct_0_28483_x1134_x2117236987}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_1848388292}*[协商出来的服务器端到客户端的加密算法、]{style="font-family:宋体"}[HMAC]{lang="EN-US"}[算法和压缩算法]{style="font-family:宋体"}*

[[\*Dec 31 17:58:30:287 2009 Sysname SSHS/7/EVENT: Received SSH2_MSG_KEX_DH_GEX_REQUEST_OLD.]{lang="EN-US"}]{#struct_0_28483_x1134_777840842}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x449088062}*[接收到]{style="font-family:宋体"}[SSH2_MSG_KEX_DH_GEX_REQUEST_OLD]{lang="EN-US"}[消息]{style="font-family:
宋体"}*

[[\*Dec 31 17:58:31:142 2009 Sysname SSHS/7/EVENT: Expecting packet type 32.]{lang="EN-US"}]{#struct_0_28483_x1134_1122350400}

[\*Dec 31 17:58:33:45 2009 Sysname SSHS/7/EVENT: Set new keys: mode=1]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x1549454333}*[设置协商出来的新的算法（]{style="font-family:宋体"}[mode=1]{lang="EN-US"}[表示输出方向）]{style="font-family:宋体"}*

[[\*Dec 31 17:58:33:62 2009 Sysname SSHS/7/EVENT: Expecting packet type 21.]{lang="EN-US"}]{#struct_0_28483_x1134_185415794}

[\*Dec 31 17:58:33:466 2009 Sysname SSHS/7/EVENT: Set new keys: mode=0]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_108524729}*[设置协商出来的新的算法（]{style="font-family:宋体"}[mode=0]{lang="EN-US"}[标识输入方向）]{style="font-family:宋体"}*

[[\*Dec 31 17:58:33:471 2009 Sysname SSHS/7/EVENT: KEX done.]{lang="EN-US"}]{#struct_0_28483_x1134_x2117171451}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x18456211}*[密钥交换结束]{style="font-family:宋体"}*

[[\*Dec 31 17:58:33:479 2009 Sysname SSHS/7/EVENT: Received SSH2_MSG_SERVICE_REQUEST.]{lang="EN-US"}]{#struct_0_28483_x1134_x792044650}

[\*Dec 31 17:58:34:459 2009 Sysname SSHS/7/EVENT: Received SSH2_MSG_USERAUTH_REQUEST.]{lang="EN-US"}

[\*Dec 31 17:58:34:464 2009 Sysname SSHS/7/EVENT: Username: abc, service: ssh-connection, method: none]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_582154153}*[接收到用户认证请求消息，消息中的用户名为]{style="font-family:宋体"}[abc]{lang="EN-US"}[，服务请求串为]{style="font-family:宋体"}[ssh-connection]{lang="EN-US"}[，认证方法为]{style="font-family:宋体"}[none]{lang="EN-US"}[（]{style="font-family:宋体"}[向对方请求对方支持的认证方法列表串）]{style="font-family:宋体"}*

[[\*Dec 31 17:58:34:470 2009 Sysname SSHS/7/EVENT: PAM: initializing for \"abc\", service:login, pure user name:abc, domain:]{lang="EN-US"}]{#struct_0_28483_x1134_71735259}

[*[// PAM]{lang="EN-US"}*]{#struct_0_28483_x1134_578323026}*[初始化，]{style="font-family:宋体"}[PAM]{lang="EN-US"}[服务类型为]{style="font-family:宋体"}[login]{lang="EN-US"}[，纯用户名为]{style="font-family:宋体"}[abc]{lang="EN-US"}[，域名为空]{style="font-family:宋体"}*

[[\*Dec 31 17:58:34:509 2009 Sysname SSHS/7/EVENT: Try authentication method none.]{lang="EN-US"}]{#struct_0_28483_x1134_2030593705}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x2116843771}*[尝试]{style="font-family:宋体"}[none]{lang="EN-US"}[认证类型]{style="font-family:宋体"}*

[[\*Dec 31 17:58:34:520 2009 Sysname SSHS/6/EVENT: Failed none for abc from 192.168.0.58 port 1476 ssh2]{lang="EN-US"}]{#struct_0_28483_x1134_1882930168}

[*[// none]{lang="EN-US"}*]{#struct_0_28483_x1134_818247245}*[认证尝试失败]{style="font-family:宋体"}*

[[\*Dec 31 17:58:34:525 2009 Sysname SSHS/7/EVENT: Get authentication methods: password]{lang="EN-US"}]{#struct_0_28483_x1134_129673054}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x1509926832}*[用户还可挑战的认证方法为]{style="font-family:宋体"}[password]{lang="EN-US"}[认证方法]{style="font-family:宋体"}*

[[\*Dec 31 17:58:35:673 2009 Sysname SSHS/7/EVENT: Received SSH2_MSG_USERAUTH_REQUEST.]{lang="EN-US"}]{#struct_0_28483_x1134_471375431}

[\*Dec 31 17:58:35:679 2009 Sysname SSHS/7/EVENT: Username: abc, service: ssh-connection, method: password]{lang="EN-US"}

[\*Dec 31 17:58:35:687 2009 Sysname SSHS/7/EVENT: Try authentication method password.]{lang="EN-US"}

[\*Dec 31 17:58:36:86 2009 Sysname SSHS/7/EVENT: PAM: password authentication accepted for abc, level: 15, workdir:flash:.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_762954483}*[用户]{style="font-family:宋体"}[password]{lang="EN-US"}[认证挑战成功，授权用户角色]{style="font-family:宋体"}[level-15]{lang="EN-US"}[，授权工作路径为]{style="font-family:宋体"}[flash:]{lang="EN-US"}*

[[%Dec 31 17:58:36:109 2009 Sysname SSHS/6/SSHLOG: Accepted password for abc from 192.168.0.58 port 1476 ssh2]{lang="EN-US"}]{#struct_0_28483_x1134_x2116778235}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x1411281118}*[用户]{style="font-family:宋体"}[abc]{lang="EN-US"}[从]{style="font-family:宋体"}[192.168.0.58]{lang="EN-US"}[端口]{style="font-family:宋体"}[1467]{lang="EN-US"}[发起连接请求，]{style="font-family:宋体"}[password]{lang="EN-US"}[认证通过]{style="font-family:宋体"}*

[[\*Dec 31 17:58:36:139 2009 Sysname SSHS/7/EVENT: Entering interactive session for SSH2.]{lang="EN-US"}]{#struct_0_28483_x1134_1907841613}

[\*Dec 31 17:58:36:147 2009 Sysname SSHS/7/EVENT: Initiate server message dispatch, compatibility:1/0]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x1392142468}*[初始化消息分发处理，兼容]{style="font-family:宋体"}[2.0]{lang="EN-US"}[版本，不兼容]{style="font-family:宋体"}[1.3]{lang="EN-US"}[版本]{style="font-family:宋体"}*

[[\*Dec 31 17:58:36:158 2009 Sysname SSHS/7/EVENT: Received SSH2_MSG_CHANNEL_OPEN: ctype session, rchan 256, win 16384, max 16384]{lang="EN-US"}]{#struct_0_28483_x1134_x1274856918}

[\*Dec 31 17:58:36:173 2009 Sysname SSHS/7/EVENT: Received session request.]{lang="EN-US"}

[\*Dec 31 17:58:36:185 2009 Sysname SSHS/7/EVENT: Channel 0: new \[server-session\]]{lang="EN-US"}

[\*Dec 31 17:58:36:191 2009 Sysname SSHS/7/EVENT: Session id 0 unused.]{lang="EN-US"}

[\*Dec 31 17:58:36:199 2009 Sysname SSHS/7/EVENT: Session opened: session 0, link with channel 0]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x1710303854}*[接收到]{style="font-family:宋体"}[SSH2_MSG_CHANNEL_OPEN]{lang="EN-US"}[消息，分配通道号为]{style="font-family:宋体"}[0]{lang="EN-US"}[，会话]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}*

[[\*Dec 31 17:58:36:212 2009 Sysname SSHS/7/EVENT: Received SSH2_MSG_CHANNEL_REQUEST: channel 0, request pty-req, reply 1]{lang="EN-US"}]{#struct_0_28483_x1134_x2117368058}

[\*Dec 31 17:58:36:225 2009 Sysname SSHS/7/EVENT: Channel request: user abc, service type 1]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_304222831}*[用户]{style="font-family:宋体"}[abc]{lang="EN-US"}[的配置支持服务类型为]{style="font-family:宋体"}[1]{lang="EN-US"}[（]{style="font-family:宋体"}[1]{lang="EN-US"}[表示同时支持]{style="font-family:宋体"}[Stelnet]{lang="EN-US"}[和]{style="font-family:宋体"}[SFTP]{lang="EN-US"}[服务；]{style="font-family:宋体"}[2]{lang="EN-US"}[表示支持]{style="font-family:宋体"}[Stelnet]{lang="EN-US"}[服务，]{style="font-family:宋体"}[3]{lang="EN-US"}[表示支持]{style="font-family:宋体"}[SFTP]{lang="EN-US"}[服务）]{style="font-family:宋体"}*

[[\*Dec 31 17:58:36:288 2009 Sysname SSHS/7/EVENT: Received SSH2_MSG_CHANNEL_REQUEST: channel 0, request shell, reply 1]{lang="EN-US"}]{#struct_0_28483_x1134_x2067537943}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x662853958}*[接收到类型为]{style="font-family:宋体"}[shell]{lang="EN-US"}[的通道请求消息]{style="font-family:宋体"}*

[[\*Dec 31 17:58:36:298 2009 Sysname SSHS/7/EVENT: Channel request: user abc, service type 1]{lang="EN-US"}]{#struct_0_28483_x1134_x1140752491}

[\*Dec 31 17:58:36:327 2009 Sysname SSHS/7/EVENT: Channel 0: read_fd 33 is a TTY.]{lang="EN-US"}

[\*Dec 31 17:58:36:337 2009 Sysname SSHS/7/EVENT: Setup environment: user=abc, work directory=flash:, level=15]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_148729948}*[设置用户]{style="font-family:宋体"}[abc]{lang="EN-US"}[的环境变量：工作路径为]{style="font-family:宋体"}[flash:]{lang="EN-US"}[，授权等级为]{style="font-family:宋体"}[15]{lang="EN-US"}*

[[\*Dec 31 17:58:36:349 2009 Sysname SSHS/7/EVENT: Get default work dir: /mnt/flash:, return:0]{lang="EN-US"}]{#struct_0_28483_x1134_x2117302522}

[\*Dec 31 17:58:40:87 2009 Sysname SSHS/7/EVENT: Received SIGCHLD.]{lang="EN-US"}

[\*Dec 31 17:58:40:93 2009 Sysname SSHS/7/EVENT: Channel 0: request exit-status confirm 0]{lang="EN-US"}

[\*Dec 31 17:58:40:102 2009 Sysname SSHS/7/EVENT: Release channel 0]{lang="EN-US"}

[\*Dec 31 17:58:40:107 2009 Sysname SSHS/7/EVENT: Channel 0: write failed]{lang="EN-US"}

[\*Dec 31 17:58:40:111 2009 Sysname SSHS/7/EVENT: Channel 0: send EOW]{lang="EN-US"}

[\*Dec 31 17:58:40:115 2009 Sysname SSHS/7/EVENT: Channel 0: output state changed (open -\> closed)]{lang="EN-US"}

[\*Dec 31 17:58:40:125 2009 Sysname SSHS/7/EVENT: Channel 0: read failed]{lang="EN-US"}

[\*Dec 31 17:58:40:129 2009 Sysname SSHS/7/EVENT: Channel 0: input state changed (open -\> drain)]{lang="EN-US"}

[\*Dec 31 17:58:40:134 2009 Sysname SSHS/7/EVENT: Channel 0: send EOF]{lang="EN-US"}

[\*Dec 31 17:58:40:138 2009 Sysname SSHS/7/EVENT: Channel 0: input state changed (drain -\> closed)]{lang="EN-US"}

[\*Dec 31 17:58:40:143 2009 Sysname SSHS/7/EVENT: Channel 0: send SSH2_MSG_CHANNEL_CLOSE]{lang="EN-US"}

[\*Dec 31 17:58:40:173 2009 Sysname SSHS/7/EVENT: Channel 0: received SSH2_MSG_CHANNEL_CLOSE]{lang="EN-US"}

[\*Dec 31 17:58:40:180 2009 Sysname SSHS/7/EVENT: Close session: session 0, pid 0]{lang="EN-US"}

[\*Dec 31 17:58:40:185 2009 Sysname SSHS/7/EVENT: Session id 0 unused.]{lang="EN-US"}

[\*Dec 31 17:58:40:187 2009 Sysname SSHS/7/EVENT: Channel 0: garbage collecting]{lang="EN-US"}

[\*Dec 31 17:58:40:198 2009 Sysname SSHS/7/EVENT: Connection closed by 192.168.0.58]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x1558594024}*[从]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[192.168.0.58]{lang="EN-US"}[发起的连接被主动关闭]{style="font-family:宋体"}*

[[\*Dec 31 17:58:40:203 2009 Sysname SSHS/7/EVENT: PAM: cleanup]{lang="EN-US"}]{#struct_0_28483_x1134_x511584414}

[\*Dec 31 17:58:40:205 2009 Sysname SSHS/6/EVENT: Transferred: sent 1928 bytes, received 1624 bytes]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x1710643992}*[传输完成，发送]{style="font-family:宋体"}[1928]{lang="EN-US"}[字节，接收]{style="font-family:宋体"}[1624]{lang="EN-US"}[字节]{style="font-family:宋体"}*

[[\*Dec 31 17:58:40:207 2009 Sysname SSHS/6/EVENT: Closing connection to 192.168.0.58 port 1476]{lang="EN-US"}]{#struct_0_28483_x1134_x2117499130}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x1367276049}*[关闭与]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[192.168.0.58]{lang="EN-US"}[、端口]{style="font-family:宋体"}[1476]{lang="EN-US"}[之间的连接]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_28483_x1134_x588164380}[打开]{style="font-family:宋体"}[SSH]{lang="EN-US"}[服务器端的消息调试信息开关。用户从]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.0.59]{lang="EN-US"}[的客户端上登录本设备。登录成功后，用户首先执行了]{style="font-family:宋体"}**[dir]{lang="EN-US"}**[命令，然后执行]{style="font-family:宋体"}**[quit]{lang="EN-US"}**[命令退出。]{style="font-family:宋体"}

[[\<Sysname\> debugging ssh server message]{lang="EN-US"}]{#struct_0_28483_x1134_x1380116790}

[\*Dec 31 16:07:05:723 2009 Sysname SSHS/7/MESSAGE: Prepare packet\[20\].]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_1762972610}*[准备消息，消息类型为]{style="font-family:宋体"}[20]{lang="EN-US"}[（以下各消息涵义类似，解释略）]{style="font-family:宋体"}*

[[\*Dec 31 16:07:05:779 2009 Sysname SSHS/7/MESSAGE: Received packet type 20.]{lang="EN-US"}]{#struct_0_28483_x1134_x999408679}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_750879058}*[接收到消息，消息类型为]{style="font-family:宋体"}[20]{lang="EN-US"}[（以下各消息涵义类似，解释略）]{style="font-family:宋体"}*

[[\*Dec 31 16:07:05:886 2009 Sysname SSHS/7/MESSAGE: Received packet type 34.]{lang="EN-US"}]{#struct_0_28483_x1134_x2117105914}

[\*Dec 31 16:07:05:887 2009 Sysname SSHS/7/MESSAGE: Prepare packet\[31\].]{lang="EN-US"}

[\*Dec 31 16:07:07:444 2009 Sysname SSHS/7/MESSAGE: Received packet type 32.]{lang="EN-US"}

[\*Dec 31 16:07:09:294 2009 Sysname SSHS/7/MESSAGE: Prepare packet\[33\].]{lang="EN-US"}

[\*Dec 31 16:07:09:301 2009 Sysname SSHS/7/MESSAGE: Prepare packet\[21\].]{lang="EN-US"}

[\*Dec 31 16:07:11:627 2009 Sysname SSHS/7/MESSAGE: Received packet type 21.]{lang="EN-US"}

[\*Dec 31 16:07:11:738 2009 Sysname SSHS/7/MESSAGE: Received packet type 5.]{lang="EN-US"}

[\*Dec 31 16:07:11:741 2009 Sysname SSHS/7/MESSAGE: Prepare packet\[6\].]{lang="EN-US"}

[\*Dec 31 16:07:11:840 2009 Sysname SSHS/7/MESSAGE: Received packet type 50.]{lang="EN-US"}

[\*Dec 31 16:07:11:846 2009 Sysname SSHS/7/MESSAGE: Prepare packet\[51\].]{lang="EN-US"}

[\*Dec 31 16:07:12:673 2009 Sysname SSHS/7/MESSAGE: Received packet type 50.]{lang="EN-US"}

[\*Dec 31 16:07:12:803 2009 Sysname SSHS/7/MESSAGE: Prepare packet\[52\].]{lang="EN-US"}

[\*Dec 31 16:07:12:885 2009 Sysname SSHS/7/MESSAGE: Received packet type 90.]{lang="EN-US"}

[\*Dec 31 16:07:12:887 2009 Sysname SSHS/7/MESSAGE: Prepare packet\[91\]. ]{lang="EN-US"}

[\*Dec 31 16:07:12:986 2009 Sysname SSHS/7/MESSAGE: Received packet type 98.]{lang="EN-US"}

[\*Dec 31 16:07:12:996 2009 Sysname SSHS/7/MESSAGE:P repare packet\[99\].]{lang="EN-US"}

[\*Dec 31 16:07:13:86 2009 Sysname SSHS/7/MESSAGE: Received packet type 98.]{lang="EN-US"}

[\*Dec 31 16:07:13:97 2009 Sysname SSHS/7/MESSAGE: Prepare packet\[93\].]{lang="EN-US"}

[\*Dec 31 16:07:13:99 2009 Sysname SSHS/7/MESSAGE: Prepare packet\[99\].]{lang="EN-US"}

[\*Dec 31 16:07:14:62 2009 Sysname SSHS/7/MESSAGE: Received packet type 94.]{lang="EN-US"}

[\*Dec 31 16:07:14:268 2009 Sysname SSHS/7/MESSAGE: Received packet type 94.]{lang="EN-US"}

[\*Dec 31 16:07:14:695 2009 Sysname SSHS/7/MESSAGE: Received packet type 94.]{lang="EN-US"}

[\*Dec 31 16:07:14:902 2009 Sysname SSHS/7/MESSAGE: Received packet type 94.]{lang="EN-US"}

[\*Dec 31 16:07:17:99 2009 Sysname SSHS/7/MESSAGE: Received packet type 94.]{lang="EN-US"}

[\*Dec 31 16:07:17:205 2009 Sysname SSHS/7/MESSAGE: Received packet type 94.]{lang="EN-US"}

[\*Dec 31 16:07:17:306 2009 Sysname SSHS/7/MESSAGE: Received packet type 94.]{lang="EN-US"}

[\*Dec 31 16:07:17:508 2009 Sysname SSHS/7/MESSAGE: Received packet type 94.]{lang="EN-US"}

[\*Dec 31 16:07:17:520 2009 Sysname SSHS/7/MESSAGE: Prepare packet\[98\].]{lang="EN-US"}

[\*Dec 31 16:07:17:523 2009 Sysname SSHS/7/MESSAGE: Prepare packet\[96\].]{lang="EN-US"}

[\*Dec 31 16:07:17:525 2009 Sysname SSHS/7/MESSAGE: Prepare packet\[97\].]{lang="EN-US"}

[\*Dec 31 16:07:17:719 2009 Sysname SSHS/7/MESSAGE: Received packet type 24.]{lang="EN-US"}

[\*Dec 31 16:07:17:722 2009 Sysname SSHS/7/MESSAGE: Prepare packet\[3\].]{lang="EN-US"}

::: {#342661084 .myid}
[]{#_Toc404793163}[]{#_Toc395010547}[]{#struct_0_28483_x1134_x1788554002}[]{#_Toc167939233}[]{#_Toc138241186}[]{#_Toc133380254}

**SSH \-- SSH调试命令 \-- debugging ssh client**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_28483_x1134_x1693898417}

[**[debugging ssh client]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **message** }]{lang="EN-US"}]{#struct_0_28483_x1134_859063456}

[**[undo debugging ssh client]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **message** }]{lang="EN-US"}]{#struct_0_28483_x1134_x1873853319}

[[【视图】]{style="font-family:黑体"}]{#struct_0_28483_x1134_x1113313412}

[[用户视图]{style="font-family:宋体"}]{#struct_0_28483_x1134_x474632500}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_28483_x1134_126413815}

[[network-admin]{lang="EN-US"}]{#struct_0_28483_x1134_x2117040378}

[[mdc-admin]{lang="EN-US"}]{#struct_0_28483_x1134_x1050992024}

[[【参数】]{style="font-family:黑体"}]{#struct_0_28483_x1134_1906421361}

[**[all]{lang="EN-US"}**]{#struct_0_28483_x1134_1702860799}[：所有类型的调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_28483_x1134_1020928746}[：错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_28483_x1134_716167061}[：事件调试信息开关。]{style="font-family:宋体"}

[**[message]{lang="EN-US"}**]{#struct_0_28483_x1134_x1210173153}[：消息调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_28483_x1134_x883272050}

[**[debugging ssh client]{lang="EN-US"}**]{#struct_0_28483_x1134_x2117236986}[命令用来打开]{style="font-family:宋体"}[SSH]{lang="EN-US"}[客户端调试信息开关。]{style="font-family:宋体"}**[undo debugging ssh client]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[SSH]{lang="EN-US"}[客户端调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[SSH]{lang="EN-US"}]{#struct_0_28483_x1134_282304351}[客户端调试信息开关处于关闭状态。]{style="font-family:宋体"}

[]{#struct_0_28483_x1134_x1263303375}[[表1-4 ]{lang="EN-US"}[debugging ssh client error]{lang="EN-US"}]{#_Toc138241146}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1284740074}[[字段]{style="font-family:黑体"}]{#struct_0_28483_x1134_x1577555827}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_28483_x1134_973992242}

[[The count of global confirm register too much:]{lang="EN-US"}]{#struct_0_28483_x1134_x1880679101}

[[全局确认计数太大]{style="font-family:宋体"}]{#struct_0_28483_x1134_x2117171450}

[[Killed by signal *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x1584540152}

[[由于收到信号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_930265975}[，进程终止]{style="font-family:宋体"}

[[Failed to setup session: unknown channel *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_119626430}

[[建立会话失败，未知通道号]{style="font-family:宋体"}]{#struct_0_28483_x1134_355478363}*[xx]{lang="EN-US"}*

[[Cannot decode server_public_key_blob]{lang="EN-US"}]{#struct_0_28483_x1134_x2116843770}

[[无法解码服务器公钥]{style="font-family:宋体"}]{#struct_0_28483_x1134_x845953187}

[[Type mismatch for decoded server_public_key_blob]{lang="EN-US"}]{#struct_0_28483_x1134_x69493472}

[[服务器公钥类型不匹配]{style="font-family:宋体"}]{#struct_0_28483_x1134_x119932681}

[[Failed to save server public key]{lang="EN-US"}]{#struct_0_28483_x1134_x2116778234}

[[保存服务器公钥失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_1317602237}

[[Failed to verify server host key]{lang="EN-US"}]{#struct_0_28483_x1134_448666538}

[[验证服务器主机密钥失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_1713351220}

[[Failed to authenticate server public key]{lang="EN-US"}]{#struct_0_28483_x1134_x1951821654}

[[认证服务器公钥失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x195053754}

[[DH_GEX group out of range:]{lang="EN-US"}]{#struct_0_28483_x1134_x676083861}

[[DH]{lang="EN-US"}]{#struct_0_28483_x1134_1462531635}[密钥交换算法的]{style="font-family:宋体"}[group]{lang="EN-US"}[参数超出范围]{style="font-family:宋体"}

[[Cannot decode server_host_key_blob]{lang="EN-US"}]{#struct_0_28483_x1134_929875907}

[[无法解码服务器主机密钥]{style="font-family:宋体"}]{#struct_0_28483_x1134_x194988218}

[[Type mismatch for decoded server_host_key_blob]{lang="EN-US"}]{#struct_0_28483_x1134_x1411808845}

[[服务器主机密钥类型不匹配]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1081337531}

[[Outbound message too long *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_713437549}

[[要发的消息太长]{style="font-family:宋体"}]{#struct_0_28483_x1134_x195184826}

[[Couldn\'t send packet:]{lang="EN-US"}]{#struct_0_28483_x1134_906622988}

[[无法发送包]{style="font-family:宋体"}]{#struct_0_28483_x1134_246759777}

[[Connection closed]{lang="EN-US"}]{#struct_0_28483_x1134_x195119290}

[[连接已被关闭]{style="font-family:宋体"}]{#struct_0_28483_x1134_1713376296}

[[Failed to read packet:]{lang="EN-US"}]{#struct_0_28483_x1134_1935404660}

[[读取数据包失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_902840873}

[[Received message too long *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x194791610}

[[接收到的消息太长]{style="font-family:宋体"}]{#struct_0_28483_x1134_1268298158}

[[ID mismatch (*xx* != *yy*)]{lang="EN-US"}]{#struct_0_28483_x1134_1829875513}[＝]{style="font-family:宋体"}[)]{lang="EN-US"}

[[ID]{lang="EN-US"}]{#struct_0_28483_x1134_x851520250}[不匹配]{style="font-family:宋体"}[(]{lang="EN-US"}[当前]{style="font-family:宋体"}[ID *xx* ]{lang="EN-US"}[不等于期望]{style="font-family:宋体"}[ID *yy*)]{lang="EN-US"}

[[Expected *XX* packet, got *YY*]{lang="EN-US"}]{#struct_0_28483_x1134_x194726074}

[[期望接收到消息]{style="font-family:宋体"}]{#struct_0_28483_x1134_510398333}*[XX]{lang="EN-US"}*[，却接收到]{style="font-family:宋体"}*[YY]{lang="EN-US"}*

[[Got multiple names (*xx*) from SSH_FXP_REALPATH]{lang="EN-US"}]{#struct_0_28483_x1134_x878797501}

[[从]{style="font-family:宋体"}[SSH_FXP_REALPATH]{lang="EN-US"}]{#struct_0_28483_x1134_x194922682}[消息中获取到多个文件名]{style="font-family:宋体"}*[xx]{lang="EN-US"}*

[[Unexpected reply *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x1432470180}

[[接收到非期望的包序列]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_2062203445}

[[Received more data than asked for *xx* \> *yy*]{lang="EN-US"}]{#struct_0_28483_x1134_x194857146}

[[接收到过多数据]{style="font-family:宋体"}]{#struct_0_28483_x1134_100965184}

[[Transfer complete, but fail sanity check]{lang="EN-US"}]{#struct_0_28483_x1134_1593612351}

[[传送完成，完整性检查失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x194529466}

[[Couldn\'t read from \\\"*xx*\\\":]{lang="EN-US"}]{#struct_0_28483_x1134_1322257557}

[[无法从文件]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x2065055862}[中读取数据]{style="font-family:宋体"}

[[Unexpected ACK *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x194463930}

[[非期望的]{style="font-family:宋体"}[ACK *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_551798869}

[[Couldn\'t find request for ID *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_1039374312}

[[无法找到]{style="font-family:宋体"}[ID ]{lang="EN-US"}]{#struct_0_28483_x1134_x195053753}*[xx]{lang="EN-US"}*[对应的请求]{style="font-family:宋体"}

[[Too many data]{lang="EN-US"}]{#struct_0_28483_x1134_x675756181}

[[数据太多]{style="font-family:宋体"}]{#struct_0_28483_x1134_1959312971}

[[Unknown ls sort type]{lang="EN-US"}]{#struct_0_28483_x1134_x194988217}

[[不认识的]{style="font-family:宋体"}[ls ]{lang="EN-US"}]{#struct_0_28483_x1134_x1412136525}[排序类型]{style="font-family:宋体"}

[*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x2015026908}[ is not implemented]{lang="EN-US"}

[*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x195184825}[命令未实现]{style="font-family:宋体"}

[[Couldn\'t initialize connection to server]{lang="EN-US"}]{#struct_0_28483_x1134_906819596}

[[无法初始化到]{style="font-family:宋体"}[server]{lang="EN-US"}]{#struct_0_28483_x1134_323270846}[的连接]{style="font-family:宋体"}

[[Failed to get current working directory]{lang="EN-US"}]{#struct_0_28483_x1134_x195119289}

[[获取当前工作路径失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_1712786471}

[[Couldn\'t wait for ssh process:]{lang="EN-US"}]{#struct_0_28483_x1134_x194791609}

[[无法等到]{style="font-family:宋体"}[SSH]{lang="EN-US"}]{#struct_0_28483_x1134_1268756909}[进程]{style="font-family:宋体"}

[[No host]{lang="EN-US"}]{#struct_0_28483_x1134_x1377366259}

[[未输入目标主机名或]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_28483_x1134_x194726073}[地址]{style="font-family:宋体"}

[[The public key does not exist]{lang="EN-US"}]{#struct_0_28483_x1134_510857085}

[[指定的公钥不存在]{style="font-family:宋体"}]{#struct_0_28483_x1134_x2129063088}

[[Failed to get host name:]{lang="EN-US"}]{#struct_0_28483_x1134_x194922681}

[[获取主机名失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1432535716}

[[Remote port forwarding failed for listen port *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x194857145}

[[监听端口]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_100768576}[的端口转发失败]{style="font-family:宋体"}

[[Couldn\'t request local forwarding]{lang="EN-US"}]{#struct_0_28483_x1134_x194529465}

[[无法请求本地转发]{style="font-family:宋体"}]{#struct_0_28483_x1134_1322192021}

[[Compression level must be from 1 (fast) to 9 (slow, best)]{lang="EN-US"}]{#struct_0_28483_x1134_228662517}

[[压缩等级只能从]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_28483_x1134_x194463929}[到]{style="font-family:宋体"}[9]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_28483_x1134_551340118}[：压缩速度最快]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[9]{lang="EN-US"}]{#struct_0_28483_x1134_x195053756}[：压缩速度最慢，性能最好]{style="font-family:宋体"}

[[Failed to select, return (*xx*).]{lang="EN-US"}]{#struct_0_28483_x1134_x675952789}

[[select]{lang="EN-US"}]{#struct_0_28483_x1134_780200993}[失败，返回值]{style="font-family:宋体"}[(*xx*)]{lang="EN-US"}

[[Couldn\'t resolve hostname *xx*:]{lang="EN-US"}]{#struct_0_28483_x1134_x194988220}

[[无法解析主机名]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x1412333136}

[[Connection timed out during banner exchange]{lang="EN-US"}]{#struct_0_28483_x1134_x195184828}

[[banner]{lang="EN-US"}]{#struct_0_28483_x1134_907016204}[交换过程中连接超时]{style="font-family:宋体"}

[[SSH exchange identification: ]{lang="EN-US"}]{#struct_0_28483_x1134_x195119292}

[[交换标识]{style="font-family:宋体"}]{#struct_0_28483_x1134_1713507368}

[[Bad remote protocol version identification:]{lang="EN-US"}]{#struct_0_28483_x1134_1180727578}

[[远端版本标识错误]{style="font-family:宋体"}]{#struct_0_28483_x1134_x194791612}

[[Protocol major versions differ:]{lang="EN-US"}]{#struct_0_28483_x1134_1268429230}

[[主版本号不同]{style="font-family:宋体"}]{#struct_0_28483_x1134_x194726076}

[[Couldn\'t wait for child:]{lang="EN-US"}]{#struct_0_28483_x1134_510529405}

[[等待子进程错误]{style="font-family:宋体"}]{#struct_0_28483_x1134_x194922684}

[[Server denied authentication request:]{lang="EN-US"}]{#struct_0_28483_x1134_x1432863396}

[[服务器拒绝认证请求]{style="font-family:宋体"}]{#struct_0_28483_x1134_x194857148}

[[Failed to setup authentication context:]{lang="EN-US"}]{#struct_0_28483_x1134_101620544}

[[设置认证上下文失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x194529468}

[[Permission denied (xx).]{lang="EN-US"}]{#struct_0_28483_x1134_1321864341}

[[访问拒绝]{style="font-family:宋体"}]{#struct_0_28483_x1134_x194463932}

[[Bad message during authentication:]{lang="EN-US"}]{#struct_0_28483_x1134_551929941}

[[认证过程中接收到错误的消息]{style="font-family:宋体"}]{#struct_0_28483_x1134_x711252832}

[[No authentication context]{lang="EN-US"}]{#struct_0_28483_x1134_x195053755}

[[No authentication context.]{lang="EN-US"}]{#struct_0_28483_x1134_x194988219}

[[Server returned different OID from expected]{lang="EN-US"}]{#struct_0_28483_x1134_x1411743309}

[[服务器返回不同的]{style="font-family:宋体"}[OID]{lang="EN-US"}]{#struct_0_28483_x1134_x195184827}

[[Failed to sign and send public_key]{lang="EN-US"}]{#struct_0_28483_x1134_906688524}

[[公钥签名和发送失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x195119291}

[[Authentication response too long:]{lang="EN-US"}]{#struct_0_28483_x1134_1713310760}

[[认证应答报文长度过长]{style="font-family:宋体"}]{#struct_0_28483_x1134_x194791611}

[[Bad authentication reply message type:]{lang="EN-US"}]{#struct_0_28483_x1134_1268232622}

[[错误的认证应答消息类型]{style="font-family:宋体"}]{#struct_0_28483_x1134_x194726075}

[[Too many identities in authentication reply:]{lang="EN-US"}]{#struct_0_28483_x1134_510463869}

[[认证应答中存在太多的标识]{style="font-family:宋体"}]{#struct_0_28483_x1134_x194922683}

[[Bad authentication response:]{lang="EN-US"}]{#struct_0_28483_x1134_x1432404644}

[[错误的认证应答]{style="font-family:宋体"}]{#struct_0_28483_x1134_x194857147}

[[Bad response from authentication agent:]{lang="EN-US"}]{#struct_0_28483_x1134_100899648}

[[从认证代理接收到错误的应答]{style="font-family:宋体"}]{#struct_0_28483_x1134_x194529467}

[[Failed to get data from buffer]{lang="EN-US"}]{#struct_0_28483_x1134_1322323093}

[[从]{style="font-family:宋体"}]{#struct_0_28483_x1134_x194463931}[buffer]{lang="EN-US"}[中获取数据失败]{style="font-family:宋体"}

[[Bad string length *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_551864405}

[[错误的字符串长度]{style="font-family:宋体"}]{#struct_0_28483_x1134_x195053758}*[xx]{lang="EN-US"}*

[[Failed to put null string to buffer]{lang="EN-US"}]{#struct_0_28483_x1134_x194988222}

[[向]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1412464208}[buffer]{lang="EN-US"}[中存入空串失败]{style="font-family:宋体"}

[[Failed to put BIGNUM to the buffer.]{lang="EN-US"}]{#struct_0_28483_x1134_x195184830}

[[向]{style="font-family:宋体"}]{#struct_0_28483_x1134_906491917}[buffer]{lang="EN-US"}[中存入]{style="font-family:宋体"}[BIGNUM]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to get BIGNUM from the buffer.]{lang="EN-US"}]{#struct_0_28483_x1134_x195119294}

[[从]{style="font-family:宋体"}]{#struct_0_28483_x1134_1713638440}[buffer]{lang="EN-US"}[中获取]{style="font-family:宋体"}[BIGNUM]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to write BIGNUM to the buffer in SSH2 format.]{lang="EN-US"}]{#struct_0_28483_x1134_x194791614}

[[向]{style="font-family:宋体"}]{#struct_0_28483_x1134_1268560302}[buffer]{lang="EN-US"}[中以]{style="font-family:宋体"}[ssh2]{lang="EN-US"}[协议格式写入]{style="font-family:宋体"}[BIGNUM]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to get BIGNUM from the buffer in SSH2 format.]{lang="EN-US"}]{#struct_0_28483_x1134_x194726078}

[[从]{style="font-family:宋体"}]{#struct_0_28483_x1134_x194922686}[buffer]{lang="EN-US"}[中以]{style="font-family:宋体"}[ssh2]{lang="EN-US"}[协议格式获取]{style="font-family:宋体"}[BIGNUM]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to append space to the buffer:]{lang="EN-US"}]{#struct_0_28483_x1134_x1432732324}

[[在]{style="font-family:宋体"}]{#struct_0_28483_x1134_x194857150}[buffer]{lang="EN-US"}[后追加空间失败]{style="font-family:宋体"}

[[Failed to append buffer space:]{lang="EN-US"}]{#struct_0_28483_x1134_101096255}

[[在]{style="font-family:宋体"}]{#struct_0_28483_x1134_x194529470}[buffer]{lang="EN-US"}[后追加空间失败]{style="font-family:宋体"}

[[Failed to consume data from the beginning of the buffer.]{lang="EN-US"}]{#struct_0_28483_x1134_x194463934}

[[从]{style="font-family:宋体"}]{#struct_0_28483_x1134_552061013}[buffer]{lang="EN-US"}[头删除数据失败]{style="font-family:宋体"}

[[Failed to consume data from the end of the buffer.]{lang="EN-US"}]{#struct_0_28483_x1134_x195053757}

[[从]{style="font-family:宋体"}]{#struct_0_28483_x1134_x676018325}[buffer]{lang="EN-US"}[尾删除数据失败]{style="font-family:宋体"}

[[Failed to get remote hostname.]{lang="EN-US"}]{#struct_0_28483_x1134_x194988221}

[[获取对端主机名失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x195184829}

[[Connection from *x.x.x.x* with IP options: *yy*]{lang="EN-US"}]{#struct_0_28483_x1134_907081740}

[[从]{style="font-family:宋体"}]{#struct_0_28483_x1134_x195119293}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}*[x.x.x.x]{lang="EN-US"}*[发起的连接，携带]{style="font-family:宋体"}[IP]{lang="EN-US"}[选项为]{style="font-family:宋体"}*[yy]{lang="EN-US"}*

[[Failed to allocate new channel:]{lang="EN-US"}]{#struct_0_28483_x1134_x194791613}

[[channel]{lang="EN-US"}]{#struct_0_28483_x1134_1268363694}[分配失败]{style="font-family:宋体"}

[[Cannot happen: SSH_CHANNEL_LARVAL]{lang="EN-US"}]{#struct_0_28483_x1134_x194726077}

[[SSH_CHANNEL_LARVAL]{lang="EN-US"}]{#struct_0_28483_x1134_510594941}[类型的]{style="font-family:宋体"}[channel]{lang="EN-US"}[在不兼容]{style="font-family:宋体"}[2.0]{lang="EN-US"}[版本的情况下不应该出现]{style="font-family:宋体"}

[[Cannot happen: OUT_DRAIN]{lang="EN-US"}]{#struct_0_28483_x1134_x194922685}

[[SSH_CHANNEL_OUTPUT_DRAINING]{lang="EN-US"}]{#struct_0_28483_x1134_x194857149}[类型的]{style="font-family:宋体"}[channel]{lang="EN-US"}[在不兼容]{style="font-family:宋体"}[1.3]{lang="EN-US"}[版本的情况下不应该出现]{style="font-family:宋体"}

[[Bad channel type *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_101555008}

[[错误的]{style="font-family:宋体"}]{#struct_0_28483_x1134_x194529469}[channel]{lang="EN-US"}[类型]{style="font-family:宋体"}*[xx]{lang="EN-US"}*

[[Bad channel id *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x194463933}

[[错误的]{style="font-family:宋体"}]{#struct_0_28483_x1134_551995477}[channel ID *xx*]{lang="EN-US"}

[[Non-larval channel]{lang="EN-US"}]{#struct_0_28483_x1134_1371030187}

[[channel]{lang="EN-US"}]{#struct_0_28483_x1134_1371095723}[为空或者非]{style="font-family:宋体"}[SSH_CHANNEL_LARVAL]{lang="EN-US"}[类型的]{style="font-family:宋体"}[channel]{lang="EN-US"}

[[Channel xx: decode socks4: len *mm* \> have *nn*]{lang="EN-US"}]{#struct_0_28483_x1134_1491964634}

[[channel ID *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_1370899115}[：]{style="font-family:宋体"}[socks4]{lang="EN-US"}[解码时，]{style="font-family:宋体"}[buffer]{lang="EN-US"}[长度]{style="font-family:宋体"}*[mm]{lang="EN-US"}*[大于实际串长度]{style="font-family:宋体"}*[nn]{lang="EN-US"}*

[[Channel xx: decode socks4a: len *mm* \> have *nn*]{lang="EN-US"}]{#struct_0_28483_x1134_1370964651}

[[channel ID *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_742000209}[：]{style="font-family:宋体"}[socks4a]{lang="EN-US"}[解码时，]{style="font-family:宋体"}[buffer]{lang="EN-US"}[长度]{style="font-family:宋体"}*[mm]{lang="EN-US"}*[大于实际串长度]{style="font-family:宋体"}*[nn]{lang="EN-US"}*

[[Unexpected data on control fd]{lang="EN-US"}]{#struct_0_28483_x1134_1371292331}

[[在控制文件描述符上获取到异常数据]{style="font-family:宋体"}]{#struct_0_28483_x1134_1371357867}

[[Failed to prepare select:]{lang="EN-US"}]{#struct_0_28483_x1134_x424444881}

[[select]{lang="EN-US"}]{#struct_0_28483_x1134_1371161259}[准备失败]{style="font-family:宋体"}

[[Cannot happen: input state INPUT_WAIT_DRAIN for proto 1.3]{lang="EN-US"}]{#struct_0_28483_x1134_1371226795}

[[在]{style="font-family:宋体"}[1.3]{lang="EN-US"}]{#struct_0_28483_x1134_1105916130}[协议中不应该出现输入状态]{style="font-family:宋体"}[ INPUT_WAIT_DRAIN]{lang="EN-US"}

[[Too many forwards]{lang="EN-US"}]{#struct_0_28483_x1134_1371554475}

[[太多的]{style="font-family:宋体"}[TCP/IP]{lang="EN-US"}]{#struct_0_28483_x1134_1371620011}[端口转发]{style="font-family:宋体"}

[[Failed to set socket to non-block]{lang="EN-US"}]{#struct_0_28483_x1134_338769092}

[[设置]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_28483_x1134_1371030188}[为非阻塞时失败]{style="font-family:宋体"}

[[x11_request_forwarding:]{lang="EN-US"}]{#struct_0_28483_x1134_1371095724}

[[在]{style="font-family:宋体"}[x11]{lang="EN-US"}]{#struct_0_28483_x1134_1370899116}[转发请求处理中收到错误的认证数据]{style="font-family:宋体"}

[[Bad 3DES IV length: *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x1209394549}

[[错误的]{style="font-family:宋体"}[3des IV]{lang="EN-US"}]{#struct_0_28483_x1134_1370964652}[长度]{style="font-family:宋体"}*[xx]{lang="EN-US"}*

[[No 3DES context.]{lang="EN-US"}]{#struct_0_28483_x1134_1371292332}

[[没有]{style="font-family:宋体"}[3des]{lang="EN-US"}]{#struct_0_28483_x1134_x472179076}[上下文信息]{style="font-family:宋体"}

[[No AES context.]{lang="EN-US"}]{#struct_0_28483_x1134_1371357868}

[[没有]{style="font-family:宋体"}[AES]{lang="EN-US"}]{#struct_0_28483_x1134_1371161260}[上下文信息]{style="font-family:宋体"}

[[Failed to initialize cipher:]{lang="EN-US"}]{#struct_0_28483_x1134_1371226796}

[[初始化加密套件失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_1105719522}

[[Failed to initialize cipher *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_1371554476}

[[初始化加密套件]{style="font-family:宋体"}[xx]{lang="EN-US"}]{#struct_0_28483_x1134_1371620012}[失败]{style="font-family:宋体"}

[[Cipher encrypt failed:]{lang="EN-US"}]{#struct_0_28483_x1134_338572484}

[[加密失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_1371030185}

[[Wrong IV length *xx* != *yy*]{lang="EN-US"}]{#struct_0_28483_x1134_1371095721}

[[IV]{lang="EN-US"}]{#struct_0_28483_x1134_1370899113}[长度错误]{style="font-family:宋体"}

[[Bad cipher *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x1209197941}

[[错误的加密套件编号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1370964649}

[[No available ciphers found]{lang="EN-US"}]{#struct_0_28483_x1134_1371292329}

[[没有可用的加密套件]{style="font-family:宋体"}]{#struct_0_28483_x1134_1371357865}

[[Bad compression level *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_1371161257}

[[错误的压缩等级]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1998995374}*[xx]{lang="EN-US"}*

[[Buffer compress failed:]{lang="EN-US"}]{#struct_0_28483_x1134_1371226793}

[[Buffer]{lang="EN-US"}]{#struct_0_28483_x1134_1371554473}[压缩失败]{style="font-family:宋体"}

[[Buffer uncompress failed:]{lang="EN-US"}]{#struct_0_28483_x1134_1371620009}

[[Buffer]{lang="EN-US"}]{#struct_0_28483_x1134_1371030186}[解压缩失败]{style="font-family:宋体"}

[[Detect attack:]{lang="EN-US"}]{#struct_0_28483_x1134_x2006436609}

[[检测到]{style="font-family:宋体"}[CRC32 ]{lang="EN-US"}]{#struct_0_28483_x1134_1371095722}[压缩攻击]{style="font-family:宋体"}

[[Failed to generate DH_key:]{lang="EN-US"}]{#struct_0_28483_x1134_1370899114}

[[生成]{style="font-family:宋体"}[DH]{lang="EN-US"}]{#struct_0_28483_x1134_1370964650}[密钥失败]{style="font-family:宋体"}

[[Failed to create BN.]{lang="EN-US"}]{#struct_0_28483_x1134_1371292330}

[[创建]{style="font-family:宋体"}[BN]{lang="EN-US"}]{#struct_0_28483_x1134_x472048004}[失败]{style="font-family:宋体"}

[[Failed to generate DH_private_key]{lang="EN-US"}]{#struct_0_28483_x1134_1371357866}

[[生成]{style="font-family:宋体"}[DH]{lang="EN-US"}]{#struct_0_28483_x1134_1371161258}[私钥失败]{style="font-family:宋体"}

[[Failed to generate DH_key]{lang="EN-US"}]{#struct_0_28483_x1134_1371226794}

[[生成]{style="font-family:宋体"}[DH]{lang="EN-US"}]{#struct_0_28483_x1134_1371554474}[密钥失败]{style="font-family:宋体"}

[[Failed to generate DH_key:]{lang="EN-US"}]{#struct_0_28483_x1134_1906509515}

[[生成]{style="font-family:宋体"}[DH]{lang="EN-US"}]{#struct_0_28483_x1134_1371620010}[密钥失败]{style="font-family:宋体"}

[[Failed to generate DH public key.]{lang="EN-US"}]{#struct_0_28483_x1134_1371030183}

[[生成]{style="font-family:宋体"}[DH]{lang="EN-US"}]{#struct_0_28483_x1134_1371095719}[公钥失败]{style="font-family:宋体"}

[[Protocol error.]{lang="EN-US"}]{#struct_0_28483_x1134_1370899111}

[[协议错误]{style="font-family:宋体"}]{#struct_0_28483_x1134_1370964647}

[[Failed to seed PRNG.]{lang="EN-US"}]{#struct_0_28483_x1134_1371292327}

[[设置]{style="font-family:宋体"}[PRNG]{lang="EN-US"}]{#struct_0_28483_x1134_1371357863}[的种子失败]{style="font-family:宋体"}

[[Failed to send SSH2_MSG_KEXINIT:]{lang="EN-US"}]{#struct_0_28483_x1134_x424707025}

[[发送]{style="font-family:宋体"}[SSH2_MSG_KEXINIT]{lang="EN-US"}]{#struct_0_28483_x1134_1371161255}[消息失败]{style="font-family:宋体"}

[[Received SSH2_MSG_KEXINIT:]{lang="EN-US"}]{#struct_0_28483_x1134_1371226791}

[[发送]{style="font-family:宋体"}[SSH2_MSG_KEXINIT]{lang="EN-US"}]{#struct_0_28483_x1134_1371554471}[消息失败：空的交换上下文]{style="font-family:宋体"}

[[Unsupported key exchange:]{lang="EN-US"}]{#struct_0_28483_x1134_1371620007}

[[不支持的密钥交换类型]{style="font-family:宋体"}]{#struct_0_28483_x1134_1371030184}

[[No matching cipher found:]{lang="EN-US"}]{#struct_0_28483_x1134_1371095720}

[[没有匹配的加密算法]{style="font-family:宋体"}]{#struct_0_28483_x1134_1492161242}

[[Matching cipher is not supported:]{lang="EN-US"}]{#struct_0_28483_x1134_1370899112}

[[匹配的加密算法不支持]{style="font-family:宋体"}]{#struct_0_28483_x1134_1370964648}

[[No matching mac found:]{lang="EN-US"}]{#struct_0_28483_x1134_1371292328}

[[没有匹配的摘要算法]{style="font-family:宋体"}]{#struct_0_28483_x1134_1371357864}

[[Unsupported mac *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_1371161256}

[[不支持的摘要算法]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1371226792}

[[No matching compress found:]{lang="EN-US"}]{#struct_0_28483_x1134_1105981666}

[[没有匹配的压缩算法]{style="font-family:宋体"}]{#struct_0_28483_x1134_1371554472}

[[Unsupported compress:]{lang="EN-US"}]{#struct_0_28483_x1134_1371620008}

[[不支持的压缩算法]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1357853168}

[[Failed to negotiate a key exchange method.]{lang="EN-US"}]{#struct_0_28483_x1134_x1357787632}

[[密钥交换算法协商失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1357984240}

[[Bad kex algorithm:]{lang="EN-US"}]{#struct_0_28483_x1134_x1357918704}

[[错误的密钥交换算法]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1357591024}

[[No host_key algorithm]{lang="EN-US"}]{#struct_0_28483_x1134_884656203}

[[没有主机公钥算法]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1357525488}

[[Bad host_key algorithm:]{lang="EN-US"}]{#struct_0_28483_x1134_x1357722096}

[[错误的主机公钥算法]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1357656560}

[[Bad kex md size *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x1357328880}

[[错误的密钥交换模数大小]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1357263344}*[xx]{lang="EN-US"}*

[[Bad host modulus (len *xx*)]{lang="EN-US"}]{#struct_0_28483_x1134_x1357853167}

[[错误的主机模数（长度]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x1357787631}[）]{style="font-family:宋体"}

[[Bad server modulus (len *xx*)]{lang="EN-US"}]{#struct_0_28483_x1134_x1357984239}

[[错误的服务器模数（长度]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x1357918703}[）]{style="font-family:宋体"}

[[Unexpected KEX type *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x1357591023}

[[错误的密钥交换算法类型]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1357525487}*[xx]{lang="EN-US"}*

[[Failed to compute DH key]{lang="EN-US"}]{#struct_0_28483_x1134_33664815}

[[计算]{style="font-family:宋体"}[DH]{lang="EN-US"}]{#struct_0_28483_x1134_x1357722095}[密钥失败]{style="font-family:宋体"}

[[Failed to compute BN]{lang="EN-US"}]{#struct_0_28483_x1134_x1357656559}

[[计算]{style="font-family:宋体"}[BN]{lang="EN-US"}]{#struct_0_28483_x1134_x1357328879}[失败]{style="font-family:宋体"}

[[Cannot load hostkey]{lang="EN-US"}]{#struct_0_28483_x1134_x1357263343}

[[加载主机密钥失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1357853170}

[[Unsupported hostkey type *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x1357787634}

[[不支持的主机密钥类型]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1357984242}*[xx]{lang="EN-US"}*

[[Failed to create RSA key]{lang="EN-US"}]{#struct_0_28483_x1134_x1357918706}

[[创建]{style="font-family:宋体"}[RSA]{lang="EN-US"}]{#struct_0_28483_x1134_x1357591026}[密钥失败]{style="font-family:宋体"}

[[Failed to create DSA key]{lang="EN-US"}]{#struct_0_28483_x1134_x1357525490}

[[创建]{style="font-family:宋体"}[DSA]{lang="EN-US"}]{#struct_0_28483_x1134_x1357722098}[密钥失败]{style="font-family:宋体"}

[[Failed to create key: ]{lang="EN-US"}]{#struct_0_28483_x1134_x1357656562}

[[创建密钥失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1357328882}

[[Failed to free key:]{lang="EN-US"}]{#struct_0_28483_x1134_x1357263346}

[[释放]{style="font-family:宋体"}[key]{lang="EN-US"}]{#struct_0_28483_x1134_x1357853169}[失败]{style="font-family:宋体"}

[[Failed to compare key:]{lang="EN-US"}]{#struct_0_28483_x1134_x1357787633}

[[密钥比较失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1357984241}

[[Failed to print key finger:]{lang="EN-US"}]{#struct_0_28483_x1134_x1357918705}

[[打印密钥指纹失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1357591025}

[[Failed to generate rsa_private_key.]{lang="EN-US"}]{#struct_0_28483_x1134_x1357525489}

[[生成]{style="font-family:宋体"}[RSA]{lang="EN-US"}]{#struct_0_28483_x1134_x1357722097}[私有失败]{style="font-family:宋体"}

[[Failed to generate dsa_private_key.]{lang="EN-US"}]{#struct_0_28483_x1134_x1357656561}

[[生成]{style="font-family:宋体"}[DSA]{lang="EN-US"}]{#struct_0_28483_x1134_x1357328881}[私有失败]{style="font-family:宋体"}

[[Failed to generate key:]{lang="EN-US"}]{#struct_0_28483_x1134_x1357263345}

[[密钥生成失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1357853172}

[[Failed to setup MAC *xx*, length *yy*.]{lang="EN-US"}]{#struct_0_28483_x1134_x1357787636}

[[设置摘要算法]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x1357984244}[失败，长度为]{style="font-family:宋体"}*[yy]{lang="EN-US"}*

[[Failed to initial MAC]{lang="EN-US"}]{#struct_0_28483_x1134_x1357918708}

[[初始化摘要算法失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1357591028}

[[Failed to compute MAC:]{lang="EN-US"}]{#struct_0_28483_x1134_x1357525492}

[[计算摘要失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1357722100}

[[Failed to add arguments:]{lang="EN-US"}]{#struct_0_28483_x1134_x1357656564}

[[增加参数失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1357328884}

[[Failed to replace argument:]{lang="EN-US"}]{#struct_0_28483_x1134_x1357853171}

[[替换参数失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1357787635}

[[Failed to expend keys:]{lang="EN-US"}]{#struct_0_28483_x1134_x1357984243}

[[扩展密钥失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1357918707}

[[Bad channel input state:]{lang="EN-US"}]{#struct_0_28483_x1134_x1357591027}

[[错误的通道输入状态]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1357525491}

[[Bad channel output state:]{lang="EN-US"}]{#struct_0_28483_x1134_x1357722099}

[[错误的通道输出状态]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1357656563}

[[Failed to load cipher \'none\']{lang="EN-US"}]{#struct_0_28483_x1134_x1357328883}

[[载入]{style="font-family:宋体"}[none]{lang="EN-US"}]{#struct_0_28483_x1134_x1357263347}[加密套件失败]{style="font-family:宋体"}

[[Compression already enabled]{lang="EN-US"}]{#struct_0_28483_x1134_208230773}

[[已经使能了压缩]{style="font-family:宋体"}]{#struct_0_28483_x1134_208296309}

[[Failed to set encrypt key:]{lang="EN-US"}]{#struct_0_28483_x1134_208099701}

[[设置加密密钥失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_208165237}

[[No keys for mode *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_208558453}

[[模式]{style="font-family:宋体"}[xx]{lang="EN-US"}]{#struct_0_28483_x1134_208361845}[没有密钥]{style="font-family:宋体"}

[[Too many packets with same key]{lang="EN-US"}]{#struct_0_28483_x1134_208427381}

[[使用同一个密钥发送的包个数太多]{style="font-family:宋体"}]{#struct_0_28483_x1134_208755061}

[[Read failed:]{lang="EN-US"}]{#struct_0_28483_x1134_208820597}

[[读数据失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_208230774}

[[Too large packet size:]{lang="EN-US"}]{#struct_0_28483_x1134_208296310}

[[包过大]{style="font-family:宋体"}]{#struct_0_28483_x1134_208099702}

[[Disconnect recursively]{lang="EN-US"}]{#struct_0_28483_x1134_208165238}

[[重复断连]{style="font-family:宋体"}]{#struct_0_28483_x1134_208558454}

[[Write failed:]{lang="EN-US"}]{#struct_0_28483_x1134_208361846}

[[写数据失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_208427382}

[[Write connection closed]{lang="EN-US"}]{#struct_0_28483_x1134_208755062}

[[连接的写方向已关闭]{style="font-family:宋体"}]{#struct_0_28483_x1134_208820598}

[[Failed to ask password:]{lang="EN-US"}]{#struct_0_28483_x1134_208230771}

[[获取密码失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_208296307}

[[Failed to encrypt RSA public key, exponent too small or not odd.]{lang="EN-US"}]{#struct_0_28483_x1134_208165235}

[[RSA]{lang="EN-US"}]{#struct_0_28483_x1134_208492915}[公钥加密失败，指数太小或非偶数]{style="font-family:宋体"}

[[Failed to encrypt RSA public key]{lang="EN-US"}]{#struct_0_28483_x1134_208558451}

[[RSA]{lang="EN-US"}]{#struct_0_28483_x1134_208361843}[公钥加密失败]{style="font-family:宋体"}

[[Failed to decrypt RSA private key]{lang="EN-US"}]{#struct_0_28483_x1134_208427379}

[[RSA]{lang="EN-US"}]{#struct_0_28483_x1134_208755059}[私钥解密失败]{style="font-family:宋体"}

[[Failed to generate RSA additional parameters]{lang="EN-US"}]{#struct_0_28483_x1134_208820595}

[[生成]{style="font-family:宋体"}[RSA]{lang="EN-US"}]{#struct_0_28483_x1134_208296308}[附加参数失败]{style="font-family:宋体"}

[[Bad signature blob length:]{lang="EN-US"}]{#struct_0_28483_x1134_208099700}

[[错误的签名]{style="font-family:宋体"}[blob]{lang="EN-US"}]{#struct_0_28483_x1134_208165236}[长度]{style="font-family:宋体"}

[[Failed to verify DSA signature]{lang="EN-US"}]{#struct_0_28483_x1134_208492916}

[[验证]{style="font-family:宋体"}[DSA]{lang="EN-US"}]{#struct_0_28483_x1134_208558452}[签名失败]{style="font-family:宋体"}

[[Failed to set resource limits:]{lang="EN-US"}]{#struct_0_28483_x1134_208427380}

[[设置资源限制失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_208755060}

[[Failed to malloc memory: ]{lang="EN-US"}]{#struct_0_28483_x1134_208820596}

[[分配内存失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_208230769}

[[Failed to free memory]{lang="EN-US"}]{#struct_0_28483_x1134_208296305}

[[释放内存失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_208099697}

[[Failed to allocate memory]{lang="EN-US"}]{#struct_0_28483_x1134_208165233}

[[分配内存失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_208558449}

[[Failed to connect to *xx* port *yy*:]{lang="EN-US"}]{#struct_0_28483_x1134_208361841}

[[向地址]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_208427377}[端口]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[发起连接失败]{style="font-family:宋体"}

[[Failed to setup untrusted X11 forwarding:]{lang="EN-US"}]{#struct_0_28483_x1134_208755057}

[[无法建立非信任的]{style="font-family:宋体"}[X11]{lang="EN-US"}]{#struct_0_28483_x1134_208820593}[转发]{style="font-family:宋体"}

[[Not supported]{lang="EN-US"}]{#struct_0_28483_x1134_208296306}

[[该命令不支持]{style="font-family:宋体"}]{#struct_0_28483_x1134_208099698}

[[Not supported for SSH protocol version 1]{lang="EN-US"}]{#struct_0_28483_x1134_208165234}

[[SSH]{lang="EN-US"}]{#struct_0_28483_x1134_208492914}[协议版本]{style="font-family:宋体"}[1]{lang="EN-US"}[不支持]{style="font-family:宋体"}

[[Server does not support re-keying]{lang="EN-US"}]{#struct_0_28483_x1134_208558450}

[[服务器不支持重新密钥协商]{style="font-family:宋体"}]{#struct_0_28483_x1134_208427378}

[[Write failed]{lang="EN-US"}]{#struct_0_28483_x1134_208755058}

[[写错误]{style="font-family:宋体"}]{#struct_0_28483_x1134_208820594}

[[Channel *xx*: unknown channel.]{lang="EN-US"}]{#struct_0_28483_x1134_2130545074}

[[通道号]{style="font-family:宋体"}]{#struct_0_28483_x1134_2130414002}*[xx]{lang="EN-US"}*[：未知通道]{style="font-family:宋体"}

[[Unexpected channel *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_2130479538}

[[非期望的通道号]{style="font-family:宋体"}]{#struct_0_28483_x1134_2130807218}*[xx]{lang="EN-US"}*

[[Couldn\'t get handle:]{lang="EN-US"}]{#struct_0_28483_x1134_2130872754}

[[无法获取到句柄]{style="font-family:宋体"}]{#struct_0_28483_x1134_2130676146}

[[Failed to close file:]{lang="EN-US"}]{#struct_0_28483_x1134_2131069362}

[[关闭文件失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_2131134898}

[[Couldn\'t read directory:]{lang="EN-US"}]{#struct_0_28483_x1134_2130545075}

[[读文件目录错误]{style="font-family:宋体"}]{#struct_0_28483_x1134_2130414003}

[[No such file or directory]{lang="EN-US"}]{#struct_0_28483_x1134_2130479539}

[[在执行]{style="font-family:宋体"}[remove]{lang="EN-US"}]{#struct_0_28483_x1134_2130807219}[、]{style="font-family:宋体"}[get]{lang="EN-US"}[、]{style="font-family:宋体"}[put]{lang="EN-US"}[、]{style="font-family:宋体"}[ls]{lang="EN-US"}[、]{style="font-family:宋体"}[rename]{lang="EN-US"}[等操作时，发现不存在该文件，类似的错误信息还包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[End of file]{lang="EN-US"}]{#struct_0_28483_x1134_2130872755}[：文件末尾；]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Permission denied]{lang="EN-US"}]{#struct_0_28483_x1134_2130676147}[：拒绝访问；]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Bad message]{lang="EN-US"}]{#struct_0_28483_x1134_2131069363}[：错误消息；]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No connection]{lang="EN-US"}]{#struct_0_28483_x1134_2131134899}[：连接未建立]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Connection lost]{lang="EN-US"}]{#struct_0_28483_x1134_2130545072}[：连接已关闭；]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Operation unsupported]{lang="EN-US"}]{#struct_0_28483_x1134_2130610608}[：不支持的操作]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown status]{lang="EN-US"}]{#struct_0_28483_x1134_2130479536}[：未知状态；]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failure]{lang="EN-US"}]{#struct_0_28483_x1134_2130807216}[：操作失败]{lang="EN-US" style="font-family:宋体"}

[[Couldn\'t set state on \\\"*xx*\\\":]{lang="EN-US"}]{#struct_0_28483_x1134_2130872752}

[[设置状态错误，文件名]{style="font-family:宋体"}]{#struct_0_28483_x1134_2130741680}*[xx]{lang="EN-US"}*[ ]{lang="EN-US"}

[[Process SSH_FXP_REALPATH error:]{lang="EN-US"}]{#struct_0_28483_x1134_2131069360}

[[处理]{style="font-family:宋体"}[SSH_FXP_REALPATH]{lang="EN-US"}]{#struct_0_28483_x1134_2131134896}[消息出错]{style="font-family:宋体"}

[[Couldn\'t rename file \\\"*xx*\\\" to \\\"*yy*\\\"]{lang="EN-US"}]{#struct_0_28483_x1134_2130545073}

[[文件重命名错误，旧文件名为]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_2130414001}[，新文件名为]{style="font-family:宋体"}*[yy]{lang="EN-US"}*

[[Not support symlink operation]{lang="EN-US"}]{#struct_0_28483_x1134_2130479537}

[[不支持符号连接操作]{style="font-family:宋体"}]{#struct_0_28483_x1134_2130807217}

[[Couldn\'t symlink file \\\"*xx*\\\" to \\\"*yy*\\\"]{lang="EN-US"}]{#struct_0_28483_x1134_2130676145}

[[符号连接错误，旧文件名为]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_2130741681}[，新文件名为]{style="font-family:宋体"}*[yy]{lang="EN-US"}*

[[Couldn\'t download non-regular file:]{lang="EN-US"}]{#struct_0_28483_x1134_2131069361}

[[无法下载非正则文件：]{style="font-family:宋体"}]{#struct_0_28483_x1134_2130545070}

[[Couldn\'t open local file \\\"*xx*\\\" for writing:]{lang="EN-US"}]{#struct_0_28483_x1134_2130610606}

[[无法打开本地文件]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_2130413998}[去写数据]{style="font-family:宋体"}

[[Couldn\'t read from remote file \\\"*xx*\\\":]{lang="EN-US"}]{#struct_0_28483_x1134_2130807214}

[[无法从远端文件]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_2130872750}[中读数据]{style="font-family:宋体"}

[[Couldn\'t write to \\\"*xx*\\\":]{lang="EN-US"}]{#struct_0_28483_x1134_2130676142}

[[无法向本地文件]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_2131069358}[中写数据]{style="font-family:宋体"}

[[Couldn\'t set mode on \\\"*xx*\\\":]{lang="EN-US"}]{#struct_0_28483_x1134_2131134894}

[[设置文件]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_2130545071}[的模式失败]{style="font-family:宋体"}

[[Can\'t set times on \\\"*xx*\\\":]{lang="EN-US"}]{#struct_0_28483_x1134_2130413999}

[[设置文件]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_2130479535}[的时间错误]{style="font-family:宋体"}

[[\"Couldn\'t open local file \\\"*xx*\\\" for reading:]{lang="EN-US"}]{#struct_0_28483_x1134_2130807215}

[[无法打开本地文件]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_2130676143}[去读数据]{style="font-family:宋体"}

[[Couldn\'t get state for local file \\\"*xx*\\\":]{lang="EN-US"}]{#struct_0_28483_x1134_2130741679}

[[无法获取本地文件]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_2131069359}[的状态]{style="font-family:宋体"}

[*[xx ]{lang="EN-US"}*]{#struct_0_28483_x1134_x598338281}[is not a regular file]{lang="EN-US"}

[[文件]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x598272745}[不是正则文件]{style="font-family:宋体"}

[[Couldn\'t write to remote file \\\"*xx*\\\":]{lang="EN-US"}]{#struct_0_28483_x1134_x598403817}

[[无法向远端文件]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x598076137}[写数据]{style="font-family:宋体"}

[[Couldn\'t close local file \\\"*xx*\\\":]{lang="EN-US"}]{#struct_0_28483_x1134_x598010601}

[[无法关闭本地文件]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x598141673}

[[Invalid path.]{lang="EN-US"}]{#struct_0_28483_x1134_x597813993}

[[路径无效]{style="font-family:宋体"}]{#struct_0_28483_x1134_x598338280}

[[Invalid flag --*xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x598272744}

[[无效标识]{style="font-family:宋体"}]{#struct_0_28483_x1134_x598403816}

[[File \\\"*xx*\\\" not found]{lang="EN-US"}]{#struct_0_28483_x1134_x598076136}

[[未找到文件]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x598010600}

[[Multiple files match, but \\\"*xx*\\\" is not a directory.]{lang="EN-US"}]{#struct_0_28483_x1134_x598141672}

[[匹配到多个文件，但]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x597813992}[不是一个目录]{style="font-family:宋体"}

[[Failed to get the file status ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x598338283}[:]{lang="EN-US"}

[[获取]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x598272747}[文件信息失败]{style="font-family:宋体"}

[[Skipping non-regular file ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x598403819}[.]{lang="EN-US"}

[[跳过非正则文件]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x598076139}

[[You must specify at least one path after a *xx* command.]{lang="EN-US"}]{#struct_0_28483_x1134_x598010603}

[*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x598141675}[命令之后，必须至少指定一个路径]{style="font-family:宋体"}

[[You must specify two paths after a *xx* command.]{lang="EN-US"}]{#struct_0_28483_x1134_x597813995}

[*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x598338282}[命令之后，必须至少指定两个路径]{style="font-family:宋体"}

[[You must specify a path after a *xx* command.]{lang="EN-US"}]{#struct_0_28483_x1134_x598272746}

[*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x598403818}[命令之后，必须指定一个路径]{style="font-family:宋体"}

[[Failed to connect to host *xx* port *yy*]{lang="EN-US"}]{#struct_0_28483_x1134_x598076138}

[[连接到主机]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x598207210}[端口]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[失败]{style="font-family:宋体"}

[[Permission denied, please try again.]{lang="EN-US"}]{#struct_0_28483_x1134_x598141674}

[[拒绝登录，请重试]{style="font-family:宋体"}]{#struct_0_28483_x1134_x597748458}

[[Failed to sign and send public key:]{lang="EN-US"}]{#struct_0_28483_x1134_x598338285}

[[签名和发送公钥失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x598469357}

[[Failed to send and test public key:]{lang="EN-US"}]{#struct_0_28483_x1134_x598403821}

[[发送和测试公钥失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x598010605}

[[Unrecognized authentication method name:]{lang="EN-US"}]{#struct_0_28483_x1134_x598207213}

[[无法识别的认证方法名]{style="font-family:宋体"}]{#struct_0_28483_x1134_x597813997}

[[Setting tty modes failed:]{lang="EN-US"}]{#struct_0_28483_x1134_x597748461}

[[设置]{style="font-family:宋体"}[TTY]{lang="EN-US"}]{#struct_0_28483_x1134_x598272748}[模式失败]{style="font-family:宋体"}

[[Failed to write authentication data]{lang="EN-US"}]{#struct_0_28483_x1134_x598469356}

[[写认证数据失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x598076140}

[[Failed to read authentication response length]{lang="EN-US"}]{#struct_0_28483_x1134_x598010604}

[[读认证应答长度失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x598141676}

[[Failed to read authentication response]{lang="EN-US"}]{#struct_0_28483_x1134_x597813996}

[[读认证应答失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_1780933850}

[[Bad string length *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_1780868314}

[[错误的串长度]{style="font-family:宋体"}]{#struct_0_28483_x1134_1780737242}*[xx]{lang="EN-US"}*

[[Failed to get peer name:]{lang="EN-US"}]{#struct_0_28483_x1134_1780606170}

[[获取对端主机名失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_1780540634}

[[Non-public channel ]{lang="FR"}]{#struct_0_28483_x1134_1781458138}*[xx]{lang="FR"}*[, type ]{lang="FR"}*[yy]{lang="FR"}*

[[非公用通道号]{style="font-family:宋体"}]{#struct_0_28483_x1134_1781392602}*[xx]{lang="FR"}*[，类型]{style="font-family:宋体"}*[yy]{lang="FR"}*

[[Failed to set socket options SO_REUSEADDR]{lang="EN-US"}]{#struct_0_28483_x1134_1780868315}

[[设置]{style="font-family:宋体"}[Socket]{lang="EN-US"}]{#struct_0_28483_x1134_1780802779}[选项]{style="font-family:宋体"}[SO_REUSEADDR]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Channel *xx*: connection failed:]{lang="EN-US"}]{#struct_0_28483_x1134_1780671707}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1780606171}[：连接失败]{style="font-family:宋体"}

[[Use of DES is strongly discouraged due to cryptographic weaknesses]{lang="EN-US"}]{#struct_0_28483_x1134_1780475099}

[[不推荐使用]{style="font-family:宋体"}[DES]{lang="EN-US"}]{#struct_0_28483_x1134_1781458139}[算法，因为加密强度弱]{style="font-family:宋体"}

[[Kex protocol error:]{lang="EN-US"}]{#struct_0_28483_x1134_1780933848}

[[密钥交换协议错误]{style="font-family:宋体"}]{#struct_0_28483_x1134_1780802776}

[[Failed to get key type from name: ]{lang="EN-US"}]{#struct_0_28483_x1134_1780737240}

[[依据密钥名称获取密钥类型失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_1780606168}

[[Failed to get key:]{lang="EN-US"}]{#struct_0_28483_x1134_1780540632}

[[获取密钥失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_1781458136}

[[Unsupported key type ]{lang="EN-US"}]{#struct_0_28483_x1134_1781392600}*[xx]{lang="FR"}*

[[不支持的密钥类型]{style="font-family:宋体"}]{#struct_0_28483_x1134_1780868313}*[xx]{lang="FR"}*

[[Failed to sign key:]{lang="EN-US"}]{#struct_0_28483_x1134_1780802777}

[[密钥签名失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_1780671705}

[[Failed to verify key:]{lang="EN-US"}]{#struct_0_28483_x1134_1780540633}

[[密钥验证失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_1780475097}

[[Failed to get key by name \'*xx*\']{lang="EN-US"}]{#struct_0_28483_x1134_1781392601}

[[从密钥名字]{style="font-family:宋体"}]{#struct_0_28483_x1134_1780933846}*[xx]{lang="EN-US"}*[获取密钥实体失败]{style="font-family:宋体"}

[[Failed to get evpkey:]{lang="EN-US"}]{#struct_0_28483_x1134_1780802774}

[[获取]{style="font-family:宋体"}[EVP]{lang="EN-US"}]{#struct_0_28483_x1134_1780671702}[密钥失败]{style="font-family:宋体"}

[[Failed to read the file descriptor flags(*xx*):]{lang="EN-US"}]{#struct_0_28483_x1134_1780606166}

[[读取文件描述符标识]{style="font-family:宋体"}]{#struct_0_28483_x1134_1780475094}*[xx]{lang="EN-US"}*[失败]{style="font-family:宋体"}

[[Failed to set the file descriptor flags(*xx*):]{lang="EN-US"}]{#struct_0_28483_x1134_1781458134}

[[设置文件描述符标识]{style="font-family:宋体"}]{#struct_0_28483_x1134_1780933847}*[xx]{lang="EN-US"}*[失败]{style="font-family:宋体"}

[[Failed to get socket option TCP_NODELAY:]{lang="EN-US"}]{#struct_0_28483_x1134_1780868311}

[[设置]{style="font-family:宋体"}[Socket]{lang="EN-US"}]{#struct_0_28483_x1134_1780737239}[选项]{style="font-family:宋体"}[TCP_NODELAY]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to send message]{lang="EN-US"}]{#struct_0_28483_x1134_1780671703}

[[发送消息失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_1780540631}

[[Failed to receive message header]{lang="EN-US"}]{#struct_0_28483_x1134_1780475095}

[[接收消息头失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_1781392599}

[[Failed to receive message:]{lang="EN-US"}]{#struct_0_28483_x1134_x947949505}

[[接收消息失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x948080577}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x948146113}[: protocol error for unexpected state *yy*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x948277185}[：错误的状态]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[导致协议错误]{style="font-family:宋体"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x948342721}[: read failed for unexpected input state *yy*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x947425217}[：错误的输入状态]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[导致]{style="font-family:宋体"}[读失败]{style="font-family:宋体"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x947949504}[: protocol error for unexpected output state *yy*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x948015040}[：错误的输出状态]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[导致]{style="font-family:宋体"}[协议错误]{style="font-family:宋体"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x948146112}[: write failed]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x948277184}[：写错误]{style="font-family:宋体"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x948342720}[: write failed for unexpected output state *yy*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x947425216}[：错误的输出状态]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[导致]{style="font-family:宋体"}[写错误]{style="font-family:宋体"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x947490752}[: no empty buffer]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x948015043}[：无缓存]{style="font-family:宋体"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x948146115}[: internal error for unexpected output state *yy*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x948211651}[：错误的输出状态]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[导致]{style="font-family:宋体"}[内部错误]{style="font-family:宋体"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x948342723}[: cannot send IEOF for unexpected state *yy*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x947425219}[：错误的状态]{style="font-family:宋体"}*[y]{lang="EN-US"}[y]{lang="EN-US"}*[导致]{style="font-family:宋体"}[无法发送]{style="font-family:宋体"}[IEOF]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x947490755}[: cannot send SSH_MSG_CHANNEL_OUTPUT_CLOSE for unexpected state ]{lang="EN-US"}*[y]{lang="EN-US"}[y]{lang="EN-US"}*

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x948015042}[：错误的状态]{style="font-family:宋体"}*[y]{lang="EN-US"}[y]{lang="EN-US"}*[导致无法发送消息]{style="font-family:宋体"}[SSH_MSG_CHANNEL_OUTPUT_CLOSE]{lang="EN-US"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x948080578}[: SSH2_MSG_CHANNEL_CLOSE received twice]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x948211650}[：重复接收到]{style="font-family:宋体"}[SSH2_MSG_CHANNEL_CLOSE]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x948342722}[: write failed for unexpected output state *yy*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x948408258}[：错误的输出状态]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[导致]{style="font-family:宋体"}[写失败]{style="font-family:宋体"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x947490754}[: cannot send EOF for unexpected input state *yy*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x947949509}[：错误的输入状态]{style="font-family:宋体"}*[y]{lang="EN-US"}[y]{lang="EN-US"}*[导致]{style="font-family:宋体"}[无法发送]{style="font-family:宋体"}[EOF]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x948080581}[: cannot send CLOSE for input state/output state *yy*/*zz*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x948146117}[：错误的输入状态]{style="font-family:宋体"}*[xx]{lang="EN-US"}*[/]{lang="EN-US"}[输出]{style="font-family:
  宋体"}[状态]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[导致]{style="font-family:宋体"}[无法发送关闭消息]{style="font-family:宋体"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x948277189}[: already sent CLOSE]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x948408261}[：已经发送关闭消息]{style="font-family:宋体"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x947425221}[: failed to shutdown write:]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x947949508}[：]{style="font-family:宋体"}[shutdown]{lang="EN-US"}[写失败]{style="font-family:宋体"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x948080580}[: failed to close write:]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x948146116}[：关闭写失败]{style="font-family:宋体"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x948277188}[: failed to shutdown read:]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x948408260}[：]{style="font-family:宋体"}[shutdown]{lang="EN-US"}[读失败]{style="font-family:宋体"}

[[Channel ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x947425220}[: failed to close read:]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_618134436}[：关闭读失败]{style="font-family:宋体"}

[[Bad packet length ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_618003364}

[[错误的包长度]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_617937828}

[[Failed to set socket option IP_TOS ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_617806756}[:]{lang="EN-US"}

[[设置]{style="font-family:宋体"}[Socket]{lang="EN-US"}]{#struct_0_28483_x1134_617675684}[选项]{style="font-family:宋体"}[IP_TOS]{lang="EN-US"}[值]{style="font-family:宋体"}*[xx]{lang="EN-US"}*[失败]{style="font-family:宋体"}

[[Bad max packet size ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_618593188}

[[错误的最大包大小]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_618068901}

[[Failed to ask password:]{lang="EN-US"}]{#struct_0_28483_x1134_618003365}

[[获取密码失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_617872293}

[[Failed to decrypt RSA private key]{lang="EN-US"}]{#struct_0_28483_x1134_617741221}

[[解密]{style="font-family:宋体"}]{#struct_0_28483_x1134_617675685}[RSA]{lang="EN-US"}[私钥失败]{style="font-family:宋体"}

[[RSA sign failed:]{lang="EN-US"}]{#struct_0_28483_x1134_618593189}

[[RSA]{lang="EN-US"}]{#struct_0_28483_x1134_618134434}[签名失败]{style="font-family:宋体"}

[[Failed to verify RSA:]{lang="EN-US"}]{#struct_0_28483_x1134_618003362}

[[RSA]{lang="EN-US"}]{#struct_0_28483_x1134_617872290}[验证失败]{style="font-family:宋体"}

[[Bad hash length]{lang="EN-US"}]{#struct_0_28483_x1134_617806754}

[[错误的哈希长度]{style="font-family:宋体"}]{#struct_0_28483_x1134_617675682}

[[Bad signature length]{lang="EN-US"}]{#struct_0_28483_x1134_618593186}

[[错误的签名长度]{style="font-family:宋体"}]{#struct_0_28483_x1134_618068899}

[[Failed to decrypt RSA public key:]{lang="EN-US"}]{#struct_0_28483_x1134_617937827}

[[解密]{style="font-family:宋体"}]{#struct_0_28483_x1134_617806755}[RSA]{lang="EN-US"}[公钥失败]{style="font-family:宋体"}

[[Bad decrypted length ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_617741219}

[[错误的解密长度]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_618658723}

[[Hash mismatch]{lang="EN-US"}]{#struct_0_28483_x1134_618134432}

[[哈希不匹配]{style="font-family:宋体"}]{#struct_0_28483_x1134_618003360}

[[Failed to get remote hostname]{lang="EN-US"}]{#struct_0_28483_x1134_617872288}

[[获取远端主机名失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_617741216}

[[Failed to set socket option SO_KEEPALIVE:]{lang="EN-US"}]{#struct_0_28483_x1134_618658720}

[[设置]{style="font-family:宋体"}[Socket]{lang="EN-US"}]{#struct_0_28483_x1134_618593184}[选项]{style="font-family:宋体"}[SO_KEEPALIVE]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to initialize the INOTIFY]{lang="EN-US"}]{#struct_0_28483_x1134_618068897}

[[初始化]{style="font-family:宋体"}]{#struct_0_28483_x1134_617937825}[INOTIFY]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to get name info:]{lang="EN-US"}]{#struct_0_28483_x1134_617806753}

[[获取名称信息失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_617675681}

[[Failed to set socket option:]{lang="EN-US"}]{#struct_0_28483_x1134_618593185}

[[设置]{style="font-family:宋体"}[Socket]{lang="EN-US"}]{#struct_0_28483_x1134_x2110814455}[选项失败]{style="font-family:宋体"}

[[Failed to change owner *xx* (0 0):]{lang="EN-US"}]{#struct_0_28483_x1134_x2110945527}

[[改变]{style="font-family:宋体"}]{#struct_0_28483_x1134_x2111011063}[owner]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to change mode *xx* (0666):]{lang="EN-US"}]{#struct_0_28483_x1134_x2111142135}

[[改变]{style="font-family:宋体"}]{#struct_0_28483_x1134_x2110224631}[mode]{lang="EN-US"}[失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging ssh client event]{lang="EN-US"}]{#struct_0_28483_x1134_x2110290167}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x929712266}[[字段]{style="font-family:黑体"}]{#struct_0_28483_x1134_2139006741}

[[描述]{style="font-family:黑体"}]{#struct_0_28483_x1134_x1431888024}

[[No x11 authenticate context]{lang="EN-US"}]{#struct_0_28483_x1134_744458208}

[[无]{style="font-family:宋体"}[x11]{lang="EN-US"}]{#struct_0_28483_x1134_x2043264897}[认证上下文]{style="font-family:宋体"}

[*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x2110748918}[ request accepted on channel *yy*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[yy]{lang="EN-US"}*]{#struct_0_28483_x1134_13508949}[上接受]{style="font-family:宋体"}*[xx]{lang="EN-US"}*[请求]{style="font-family:宋体"}

[[Forwarding port]{lang="EN-US"}]{#struct_0_28483_x1134_x1736162592}

[[端口转发]{style="font-family:宋体"}]{#struct_0_28483_x1134_394777697}

[[Entering interactive session.]{lang="EN-US"}]{#struct_0_28483_x1134_x2110814454}

[[进入会话交互阶段]{style="font-family:宋体"}]{#struct_0_28483_x1134_1053422239}

[[Rekeying in progress]{lang="EN-US"}]{#struct_0_28483_x1134_x304399528}

[[rekey]{lang="EN-US"}]{#struct_0_28483_x1134_1508969078}[进行中]{style="font-family:宋体"}

[[Transfer complete: sent *xx* bytes, received *yy* bytes, in *zz* seconds]{lang="EN-US"}]{#struct_0_28483_x1134_x836682694}

[[传输完成：在]{style="font-family:宋体"}*[zz]{lang="EN-US"}*]{#struct_0_28483_x1134_x2110879990}[秒内，发送]{style="font-family:宋体"}*[xx]{lang="EN-US"}*[字节，接收]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[字节]{style="font-family:宋体"}

[[Bytes per second: sent *xx*, received *yy*]{lang="EN-US"}]{#struct_0_28483_x1134_x528558852}

[[每秒发送]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1966384659}[字节，接收]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[字节]{style="font-family:宋体"}

[[Requesting tunnel unit *xx* in mode *yy*]{lang="EN-US"}]{#struct_0_28483_x1134_x1108924840}

[[以]{style="font-family:宋体"}*[yy]{lang="EN-US"}*]{#struct_0_28483_x1134_x2110945526}[模式请求隧道单元]{style="font-family:宋体"}*[xx]{lang="EN-US"}*

[[request_type *xx*, want_reply *yy*]{lang="EN-US"}]{#struct_0_28483_x1134_1117695847}

[[请求类型]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x1056152912}[，是否要求应答]{style="font-family:宋体"}*[yy]{lang="EN-US"}*

[[Client key exchange]{lang="EN-US"}]{#struct_0_28483_x1134_x2111011062}

[[客户端密钥交换]{style="font-family:宋体"}]{#struct_0_28483_x1134_x137318746}

[[Couldn\'t get remote file\'s state:]{lang="EN-US"}]{#struct_0_28483_x1134_x1281652978}

[[无法获取远端文件的状态]{style="font-family:宋体"}[,]{lang="EN-US"}]{#struct_0_28483_x1134_1787977830}

[[Remote version:]{lang="EN-US"}]{#struct_0_28483_x1134_x2111076598}

[[对方版本串]{style="font-family:宋体"}]{#struct_0_28483_x1134_x1093305797}

[[Server supports extension \\\"*xx*\\\" revision *yy*]{lang="EN-US"}]{#struct_0_28483_x1134_x206159768}

[[服务器支持扩展]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x1914172852}[、修订]{style="font-family:宋体"}*[yy]{lang="EN-US"}*

[[Unrecognised server extension \\\"*xx*\\\"]{lang="EN-US"}]{#struct_0_28483_x1134_x2111142134}

[[无法识别的服务器扩展]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1360632068}

[[Sent message *XX*:]{lang="EN-US"}]{#struct_0_28483_x1134_x592298822}

[[发送消息]{style="font-family:宋体"}*[XX]{lang="EN-US"}*]{#struct_0_28483_x1134_x2111207670}

[[Received reply: type *xx*, ID *yy*]{lang="EN-US"}]{#struct_0_28483_x1134_275621541}

[[接收到应答：类型为]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_359059781}[，消息]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[yy]{lang="EN-US"}*

[[Received *XX*:]{lang="EN-US"}]{#struct_0_28483_x1134_x300563159}

[[接收到消息]{style="font-family:宋体"}]{#struct_0_28483_x1134_x2110224630}*[X]{lang="EN-US"}*[X]{lang="EN-US"}[，可能包括：]{style="font-family:
  宋体"}

[[SSH2_FXP_STATUS]{lang="EN-US"}]{#struct_0_28483_x1134_691574354}[、]{style="font-family:宋体"}[SSH2_MSG_USERAUTH_BANNER]{lang="EN-US"}[、]{style="font-family:宋体"}[SSH2_MSG_USERAUTH_SUCCESS]{lang="EN-US"}[、]{style="font-family:宋体"}[SSH2_MSG_USERAUTH_PK_OK]{lang="EN-US"}[、]{style="font-family:宋体"}[SSH2_MSG_USERAUTH_PASSWD_CHANGEREQ]{lang="EN-US"}

[[Received *xx* SSH2_FXP_NAME responses]{lang="EN-US"}]{#struct_0_28483_x1134_1187547332}

[[接收到]{style="font-family:宋体"}[x]{lang="EN-US"}]{#struct_0_28483_x1134_x2110290166}[个]{style="font-family:宋体"}[SSH2_FXP_NAME]{lang="EN-US"}[消息应答]{style="font-family:宋体"}

[[Sending SSH2_FXP_REMOVE \\\"*xx*\\\"]{lang="EN-US"}]{#struct_0_28483_x1134_572922800}

[[发送消息]{style="font-family:宋体"}]{#struct_0_28483_x1134_1068419061}[SSH2_FXP_REMOVE]{lang="EN-US"}[，路径为]{style="font-family:宋体"}*[xx]{lang="EN-US"}*

[[Server version does not support lstat operation]{lang="EN-US"}]{#struct_0_28483_x1134_x2110748921}

[[服务器版本不支持]{style="font-family:宋体"}[lstat]{lang="EN-US"}]{#struct_0_28483_x1134_x1196279096}[操作]{style="font-family:宋体"}

[[Process SSH_FXP_REALPATH: filename *xx* -\> *yy*]{lang="EN-US"}]{#struct_0_28483_x1134_1386683017}

[[处理消息]{style="font-family:宋体"}[SSH_FXP_REALPATH]{lang="EN-US"}]{#struct_0_28483_x1134_x2110814457}[，原来文件名]{style="font-family:宋体"}[xx-\>]{lang="EN-US"}[真实文件名]{style="font-family:宋体"}[yy]{lang="EN-US"}

[[Sent message *xx*:]{lang="EN-US"}]{#struct_0_28483_x1134_x512661702}

[[发送消息]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x228434365}

[[Request data: offset *xx* -\> *yy*]{lang="EN-US"}]{#struct_0_28483_x1134_x2110879993}

[[请求偏移]{style="font-family:宋体"}]{#struct_0_28483_x1134_x125274325}*[xx]{lang="EN-US"}*[ -\> *yy*]{lang="EN-US"}[的数据（]{style="font-family:宋体"}*[xx]{lang="EN-US"}*[为当前序号，]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[为最大序号）]{style="font-family:宋体"}

[[Received reply: Type *xx*, ID *yy*, Max_req *zz*]{lang="EN-US"}]{#struct_0_28483_x1134_284044872}

[[接收到应答：消息类型为]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x2110945529}[，消息]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[，]{style="font-family:宋体"} [最大序列号]{style="font-family:宋体"}*[zz]{lang="EN-US"}*

[[Received data: offset *xx* -\> *yy*]{lang="EN-US"}]{#struct_0_28483_x1134_x1967417868}

[[接收到数据偏移]{style="font-family:宋体"}]{#struct_0_28483_x1134_1822934793}*[xx]{lang="EN-US"}*[ -\> *yy*]{lang="EN-US"}[的数据（]{style="font-family:宋体"}*[xx]{lang="EN-US"}*[为当前序号，]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[为最大序号）]{style="font-family:宋体"}

[[Requesting compression at level *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x2111011065}

[[请求压缩等级]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x2059633047}

[[Remote host refused compression]{lang="EN-US"}]{#struct_0_28483_x1134_x2111076601}

[[对方不支持压缩]{style="font-family:宋体"}]{#struct_0_28483_x1134_117137605}

[[Requesting PTY]{lang="EN-US"}]{#struct_0_28483_x1134_x330436407}

[[请求]{style="font-family:宋体"}[PTY]{lang="EN-US"}]{#struct_0_28483_x1134_x2111142137}

[[Remote host failed or refused to allocate a pseudo tty]{lang="EN-US"}]{#struct_0_28483_x1134_x1368251287}

[[对方分配虚拟]{style="font-family:宋体"}[TTY]{lang="EN-US"}]{#struct_0_28483_x1134_x1155680957}[失败或拒绝分配]{style="font-family:宋体"}

[[Remote host denied X11 forwarding]{lang="EN-US"}]{#struct_0_28483_x1134_x2111207673}

[[对方拒绝]{style="font-family:宋体"}[x11]{lang="EN-US"}]{#struct_0_28483_x1134_1841705482}[转发]{style="font-family:宋体"}

[[Remote host denied authentication agent forwarding]{lang="EN-US"}]{#struct_0_28483_x1134_x2110224633}

[[对方拒绝认证代理转发]{style="font-family:宋体"}]{#struct_0_28483_x1134_288289827}

[[Sending command:]{lang="EN-US"}]{#struct_0_28483_x1134_x1474247400}

[[发送命令]{style="font-family:宋体"}]{#struct_0_28483_x1134_x2110290169}

[[Open new channel:]{lang="EN-US"}]{#struct_0_28483_x1134_x1349391501}

[[打开新的通道]{style="font-family:宋体"}]{#struct_0_28483_x1134_x2110748920}

[[Connecting to *xx* port *yy*]{lang="EN-US"}]{#struct_0_28483_x1134_369804845}

[[连接到]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_28483_x1134_x1124422833}[地址]{style="font-family:宋体"}*[xx]{lang="EN-US"}[、]{style="font-family:宋体"}*[端口号]{style="font-family:宋体"}*[yy]{lang="EN-US"}*

[[Connection established]{lang="EN-US"}]{#struct_0_28483_x1134_x2110814456}

[[连接建立]{style="font-family:宋体"}]{#struct_0_28483_x1134_x2078745643}

[[Remote protocol version ]{lang="EN-US"}*[x.y]{lang="EN-US"}*]{#struct_0_28483_x1134_x2110879992}[, remote software version *zz*]{lang="EN-US"}

[[对方协议版本号]{style="font-family:宋体"}*[x.y]{lang="EN-US"}*[,]{lang="EN-US"}]{#struct_0_28483_x1134_x1691358266}[对方软件版本号]{style="font-family:
  宋体"}*[zz]{lang="EN-US"}*

[[Get self version string *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x322158311}

[[获取到本端版本串]{style="font-family:宋体"}]{#struct_0_28483_x1134_x2110945528}*[xx]{lang="EN-US"}*

[[Local version string *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x401333927}

[[本端版本串]{style="font-family:宋体"}]{#struct_0_28483_x1134_x2111011064}*[xx]{lang="EN-US"}*

[[Service accepted:]{lang="EN-US"}]{#struct_0_28483_x1134_669250308}

[[服务器接受服务]{style="font-family:宋体"}]{#struct_0_28483_x1134_x2111076600}

[[Authentication succeeded (*xx*)]{lang="EN-US"}]{#struct_0_28483_x1134_x1448946336}

[[认证成功（认证方法名串为]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_2064495458}[）]{style="font-family:宋体"}

[[Try authentication method *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x2111142136}

[[尝试认证方法]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_197832654}

[[Passed a different authentication method list *xx*, preferred *yy*.]{lang="EN-US"}]{#struct_0_28483_x1134_x2111207672}

[[服务端给出不同的认证方法列表]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x887177873}[，首选]{style="font-family:宋体"}*[yy]{lang="EN-US"}*

[[No more authentication methods to try]{lang="EN-US"}]{#struct_0_28483_x1134_x2110224632}

[[无其它可尝试的认证方法]{style="font-family:宋体"}]{#struct_0_28483_x1134_1854373768}

[[Authentication method *xx* is enabled]{lang="EN-US"}]{#struct_0_28483_x1134_x2110290168}

[[使能认证方法]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1379491854}

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_x2110748923}[request *yy* confirm *zz*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1935888786}[：请求]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[、确认]{style="font-family:宋体"}*[zz]{lang="EN-US"}*

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_x2110814459}[closing]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1006368072}[：关闭中]{style="font-family:宋体"}

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_601278692}[connected to *yy* port *zz*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x2110879995}[：连接到]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[、端口]{style="font-family:宋体"}*[zz]{lang="EN-US"}*

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_x1288073739}[not open]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x2110945531}[：未打开]{style="font-family:宋体"}

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_x1611121972}[input draining]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x2111011067}[：输出关闭中]{style="font-family:宋体"}

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_x896833633}[Failed to filter]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x2111076603}[：停止过滤]{style="font-family:宋体"}

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_x1045661809}[window *yy* sent adjust *zz*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x2111142139}[：窗口]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[发送调整量]{style="font-family:宋体"}*[zz]{lang="EN-US"}*

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_1407686235}[garbage collecting]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x2111207675}[：资源回收中]{style="font-family:宋体"}

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_678906068}[sent extended data *yy*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x2110224635}[：发送扩展数据]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[字节]{style="font-family:宋体"}

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_1094858881}[accepting extended_data after EOF]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x2110290171}[：]{style="font-family:宋体"}[EOF]{lang="EN-US"}[状态后收到了扩展数据]{style="font-family:宋体"}

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_x2110748922}[received too much extended data *yy* bytes, window_size *zz*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x792994569}[：接收太多的扩展数据]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[，窗口大小]{style="font-family:宋体"}*[zz]{lang="EN-US"}*

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_x2110814458}[received extended data *yy* bytes]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x559715869}[：接收扩展数据]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[字节]{style="font-family:宋体"}

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_x2110879994}[FORCE input drain]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1440809616}[：输入强行关闭]{style="font-family:宋体"}

[[Bad cipher *xx* \[*yy*\]]{lang="EN-US"}]{#struct_0_28483_x1134_x2110945530}

[[错误的加密套件]{style="font-family:宋体"}[xx \[]{lang="EN-US"}]{#struct_0_28483_x1134_x45038031}[收到的完整的加密套件串列表]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[\]]{lang="EN-US"}

[[Enabling compatibility mode for protocol 2.0]{lang="EN-US"}]{#struct_0_28483_x1134_x2111011066}

[[使能兼容]{style="font-family:宋体"}[2.0]{lang="EN-US"}]{#struct_0_28483_x1134_1832049722}[版本]{style="font-family:宋体"}

[[Enabling compatibility mode for protocol 1.3]{lang="EN-US"}]{#struct_0_28483_x1134_x2111076602}

[[使能兼容]{style="font-family:宋体"}[1.3]{lang="EN-US"}]{#struct_0_28483_x1134_1683221546}[版本]{style="font-family:宋体"}

[[Enabling compression at level *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x2111142138}

[[使能]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x2111207674}[等级的压缩算法]{style="font-family:宋体"}

[[Compress outgoing: raw data *xx* bytes, compressed *yy* bytes, factor *zz*]{lang="EN-US"}]{#struct_0_28483_x1134_x2049977287}

[[压缩输出：原始数据]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x2110224634}[字节，压缩后为]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[字节，比例为]{style="font-family:宋体"}*[zz]{lang="EN-US"}*

[[Compress incoming: raw data *xx* bytes, compressed *yy* bytes, factor *zz*]{lang="EN-US"}]{#struct_0_28483_x1134_x1634024474}

[[压缩输入：原始数据]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x2110290170}[字节，压缩后为]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[字节，比例为]{style="font-family:宋体"}*[zz]{lang="EN-US"}*

[[Installing CRC compensation attack detector]{lang="EN-US"}]{#struct_0_28483_x1134_x188434618}

[[安装]{style="font-family:宋体"}[CRC]{lang="EN-US"}]{#struct_0_28483_x1134_81467221}[补偿攻击探测器]{style="font-family:宋体"}

[[Kex strings(*xx*):]{lang="EN-US"}]{#struct_0_28483_x1134_x188500154}

[[密钥交互串信息，]{style="font-family:宋体"}[xx]{lang="EN-US"}]{#struct_0_28483_x1134_1244349648}[取值代表如下涵义：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_28483_x1134_x188565690}[：密钥交换算法串；]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_28483_x1134_x188631226}[：服务器端支持的主机公钥算法串；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_28483_x1134_1250081221}[：客户端到服务器端的加密算法串；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_28483_x1134_x188696762}[：服务器端到客户端的加密算法串；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_28483_x1134_1236348516}[：客户端到服务器端的]{style="font-family:宋体"}[HMAC]{lang="EN-US"}[算法串；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5]{lang="EN-US"}]{#struct_0_28483_x1134_x188762298}[：服务器端到客户端的]{style="font-family:宋体"}[HMAC]{lang="EN-US"}[算法串；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6]{lang="EN-US"}]{#struct_0_28483_x1134_x188827834}[：客户端到服务器端的压缩算法串；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[7]{lang="EN-US"}]{#struct_0_28483_x1134_35562304}[：服务器端到客户端的压缩算法串；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[8]{lang="EN-US"}]{#struct_0_28483_x1134_x188893370}[：客户端到服务器端的语言选择串；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[9]{lang="EN-US"}]{#struct_0_28483_x1134_x187910330}[：服务器端到客户端的语言选择串]{style="font-family:宋体"}

[[Proposal mismatch:]{lang="EN-US"}]{#struct_0_28483_x1134_658982222}

[[密钥交互串匹配失败]{style="font-family:宋体"}]{#struct_0_28483_x1134_x187975866}

[[My proposal kex:]{lang="EN-US"}]{#struct_0_28483_x1134_1369148496}

[[我的密钥交互串]{style="font-family:宋体"}]{#struct_0_28483_x1134_x188434617}

[[Peer proposal kex:]{lang="EN-US"}]{#struct_0_28483_x1134_x188500153}

[[对方的密钥交互串]{style="font-family:宋体"}]{#struct_0_28483_x1134_1244021968}

[[Kex: *xx*, Encrypt: *yy*, HMAC: *zz*, Compress: *mm*]{lang="EN-US"}]{#struct_0_28483_x1134_x188565689}

[[密钥交换算法]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x188631225}[，加密算法]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[，摘要算法]{style="font-family:宋体"}*[zz]{lang="EN-US"}*[，压缩算法]{style="font-family:宋体"}*[mm]{lang="EN-US"}*

[[Bad HAMC *xx* \[*yy*\]]{lang="EN-US"}]{#struct_0_28483_x1134_1250146757}

[[错误的摘要算法]{style="font-family:宋体"}*[xx]{lang="EN-US"}*[\[]{lang="EN-US"}]{#struct_0_28483_x1134_x188696761}[摘要算法串]{style="font-family:
  宋体"}*[yy]{lang="EN-US"}*[\]]{lang="EN-US"}

[[Send message: type *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x188762297}

[[发送消息：消息类型]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1651399648}

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_x188827833}[input state: *xx* -\> *yy*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x188893369}[：输入状态由]{style="font-family:宋体"}*[xx]{lang="EN-US"}*[状态切换到]{style="font-family:宋体"}*[yy]{lang="EN-US"}*

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_x1890332463}[output state: *xx* -\> *yy*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x187910329}[：输出状态由]{style="font-family:宋体"}*[xx]{lang="EN-US"}*[状态切换到]{style="font-family:宋体"}*[yy]{lang="EN-US"}*

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_x187975865}[received *XX*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1369214032}[：接收到消息]{style="font-family:宋体"}*[XX]{lang="EN-US"}*

[[Channel *xx*: read failed]{lang="EN-US"}]{#struct_0_28483_x1134_x188434620}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x188500156}[：读数据失败]{style="font-family:宋体"}

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_1244218576}[send *XX*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x188565692}[：发送消息]{style="font-family:宋体"}*[XX]{lang="EN-US"}*

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_x188631228}[write failed]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1249425861}[：写失败]{style="font-family:宋体"}

[[Channel *xx*:]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_28483_x1134_x188696764}[mode=*yy*]{lang="EN-US"}

[[通道号]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x188762300}[：新的模式]{style="font-family:宋体"}*[yy]{lang="EN-US"}*[（]{style="font-family:宋体"}[0]{lang="EN-US"}[和]{style="font-family:宋体"}[1]{lang="EN-US"}[，分别对应]{style="font-family:宋体"}[MODE_IN]{lang="EN-US"}[或者]{style="font-family:宋体"}[MODE_OUT]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Expecting packet type ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x188827836}

[[期望收到包类型]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_35693376}

[[Remote message:]{lang="EN-US"}]{#struct_0_28483_x1134_x188893372}

[[远端发来的信息]{style="font-family:宋体"}]{#struct_0_28483_x1134_x187910332}

[[Set max packet size to ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_659113294}

[[设置最大包大小为]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x187975868}

[[Read passphrase:]{lang="EN-US"}]{#struct_0_28483_x1134_x188434619}

[[读取密码]{style="font-family:宋体"}]{#struct_0_28483_x1134_x188500155}

[[Sent message: type ]{lang="EN-US"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1244415184}[, ID ]{lang="EN-US"}*[yy]{lang="EN-US"}*

[[发送消息：类型为]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_x188565691}[，消息]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[yy]{lang="EN-US"}*

[[DSA verify:]{lang="EN-US"}]{#struct_0_28483_x1134_x188631227}

[[DSA]{lang="EN-US"}]{#struct_0_28483_x1134_x188696763}[验证]{style="font-family:宋体"}

[[RSA verify]{lang="EN-US"}]{#struct_0_28483_x1134_1236282980}

[[RSA]{lang="EN-US"}]{#struct_0_28483_x1134_x188762299}[验证]{style="font-family:宋体"}

[[Ignoring unsupported tty mode, opcode *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x188827835}

[[忽略不支持的]{style="font-family:宋体"}[TTY]{lang="EN-US"}]{#struct_0_28483_x1134_x188893371}[模式，操作码为]{style="font-family:宋体"}*[xx]{lang="EN-US"}*

[[Processed SSH2_MSG_USERAUTH_PK_OK message successfully, key finger is *xx*]{lang="EN-US"}]{#struct_0_28483_x1134_x1890856752}

[[处理]{style="font-family:宋体"}]{#struct_0_28483_x1134_x187910331}[SSH2_MSG_USERAUTH_PK]{lang="EN-US"}[消息成功，密钥指纹串为]{style="font-family:宋体"}*[xx]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[debugging ssh client message]{lang="EN-US"}]{#struct_0_28483_x1134_658916686}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x914819690}[[字段]{style="font-family:黑体"}]{#struct_0_28483_x1134_2105950915}

[[描述]{style="font-family:黑体"}]{#struct_0_28483_x1134_x187975867}

[[Prepare packet\[*xx*\]]{lang="DE"}]{#struct_0_28483_x1134_1369082960}

[[准备消息]{style="font-family:宋体"}[\[]{lang="EN-US"}]{#struct_0_28483_x1134_776682760}[消息类型]{style="font-family:宋体"}*[xx]{lang="EN-US"}*[\]]{lang="EN-US"}

[[Compression: raw_len *xx*, compressed_len *yy*]{lang="DE"}]{#struct_0_28483_x1134_1834773386}

[[数据压缩：原始数据大小为]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_1892518221}[，压缩后数据大小为]{style="font-family:宋体"}*[yy]{lang="EN-US"}*

[[Input: Length before de-compress *xx*, length after de-compress *yy*]{lang="EN-US"}]{#struct_0_28483_x1134_x188434622}

[[输入：解压前数据长度为]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_81860440}[，解压后数据长度为]{style="font-family:宋体"}*[yy]{lang="EN-US"}*

[[Received packet type *xx*]{lang="DE"}]{#struct_0_28483_x1134_433666794}

[[接收到消息]{style="font-family:宋体"}*[xx]{lang="EN-US"}*]{#struct_0_28483_x1134_2140775177}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_28483_x1134_x188500158}

[[\# ]{lang="EN-US"}]{#struct_0_28483_x1134_1243563216}[打开]{style="font-family:宋体"}[SSH]{lang="EN-US"}[客户端的错误调试信息开关。设备作为]{style="font-family:宋体"}[SFTP]{lang="EN-US"}[客户端（]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.0.55]{lang="EN-US"}[）登录远端]{style="font-family:宋体"}[SFTP]{lang="EN-US"}[服务器（]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.0.59]{lang="EN-US"}[），用户名为]{style="font-family:宋体"}[abc]{lang="EN-US"}[、密码为]{style="font-family:宋体"}[abc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> debugging ssh client error]{lang="EN-US"}]{#struct_0_28483_x1134_977981081}

[\<Sysname\> sftp 192.168.0.59]{lang="EN-US"}

[Username: abc]{lang="EN-US"}

[Connecting to 192.168.0.59 port 22.]{lang="EN-US"}

[The server is not authenticated. Continue? \[Y/N\]:y]{lang="EN-US"}

[Do you want to save the server public key? \[Y/N\]:n]{lang="EN-US"}

[abc@192.168.0.59\'s password:]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_28483_x1134_x1311943785}[将本地]{style="font-family:宋体;color:black"}[temp.c]{lang="EN-US" style="color:black"}[文件上传到远程]{style="font-family:宋体;color:black"}[SFTP]{lang="EN-US" style="color:black"}[服务器。]{style="font-family:宋体;
color:black"}

[[sftp\> put temp.c]{lang="EN-US"}]{#struct_0_28483_x1134_x113363041}

[Failed to put file.]{lang="EN-US"}

[sftp\>]{lang="EN-US"}

[\*Dec 31 18:15:06:374 2009 Sysname SSHC/3/ERROR: Failed to get the file status temp.c: No such file or directory]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_1999533167}*[获取文件状态失败；无法找到文件]{style="font-family:宋体"}[temp.c]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_28483_x1134_x188565694}[以列表的形式显示]{style="font-family:宋体;color:black"}[/abcdefg]{lang="EN-US" style="color:black"}[目录下的文件及文件夹的详细信息。]{style="font-family:宋体;
color:black"}

[[sftp\> dir abcdefg]{lang="EN-US"}]{#struct_0_28483_x1134_x1486124069}

[Failed to list files, \"/abcdefg\" not found.]{lang="EN-US"}

[sftp\>]{lang="EN-US"}

[\*Dec 31 18:15:24:786 2009 Sysname SSHC/3/ERROR: Couldn\'t get remote file status: No such file or directory]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x98050936}*[获取文件状态失败；无法找到指定文件或目录]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_28483_x1134_x1963387760}[打开]{style="font-family:宋体"}[SSH]{lang="EN-US"}[客户端的事件调试信息开关。设备作为]{style="font-family:宋体"}[SFTP]{lang="EN-US"}[客户端（]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.0.55]{lang="EN-US"}[）登录远端]{style="font-family:宋体"}[SFTP]{lang="EN-US"}[服务器（]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.0.59]{lang="EN-US"}[），用户名为]{style="font-family:宋体"}[abc]{lang="EN-US"}[、密码为]{style="font-family:宋体"}[abc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> debugging ssh client event]{lang="EN-US"}]{#struct_0_28483_x1134_1729321535}

[\<Sysname\> ssh 192.168.0.59]{lang="EN-US"}

[ ]{lang="EN-US"}

[Username: abc]{lang="EN-US"}

[\*Dec 31 20:46:58:178 2009 Sysname SSHC/7/EVENT: Connecting to 192.168.0.59 port 22.]{lang="EN-US"}

[\*Dec 31 20:46:58:191 2009 Sysname SSHC/7/EVENT: Connection established.]{lang="EN-US"}

[\*Dec 31 20:46:58:242 2009 Sysname SSHC/7/EVENT: Remote protocol version 1.99, remote software version Comware-5.20]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x188631230}*[对端协议版本号为]{style="font-family:宋体"}[1.99]{lang="EN-US"}[（即兼容]{style="font-family:宋体"}[SSH1]{lang="EN-US"}[和]{style="font-family:宋体"}[SSH2]{lang="EN-US"}[），对端软件版本串为]{style="font-family:宋体"}[Comware-5.20]{lang="EN-US"}[（版本串内容与实际的对端产品型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}*

[[\*Dec 31 20:46:58:248 2009 Sysname SSHC/7/EVENT: Enabling compatibility mode for protocol 2.0]{lang="EN-US"}]{#struct_0_28483_x1134_1249950148}

[\*Dec 31 20:46:58:262 2009 Sysname SSHC/7/EVENT: Get self version string Comware-7]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x1416215885}*[获取到本端软件版本串为]{style="font-family:宋体"}[Comware-7]{lang="EN-US"}[（版本串内容与实际的对端产品型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}*

[[\*Dec 31 20:46:58:278 2009 Sysname SSHC/7/EVENT: Local version string SSH-2.0-Comware-7]{lang="EN-US"}]{#struct_0_28483_x1134_x1885654517}

[\*Dec 31 20:46:58:314 2009 Sysname SSHC/7/EVENT: Received SSH2_MSG_KEXINIT.]{lang="EN-US"}

[\*Dec 31 20:46:58:322 2009 Sysname SSHC/7/EVENT: My proposal kex:]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_728426681}*[客户端的版本协商算法串信息如下]{style="font-family:宋体"}*

[[\*Dec 31 20:46:58:331 2009 Sysname SSHC/7/EVENT: Kex strings(0): diffie-hellman-group-exchange-sha1,diffie-hellman-group14-sha1,diffie-hellman-group1-sha1]{lang="EN-US"}]{#struct_0_28483_x1134_2027570911}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x64673919}*[密钥交换算法串]{style="font-family:宋体"}*

[[\*Dec 31 20:46:58:338 2009 Sysname SSHC/7/EVENT: Kex strings(1): ssh-dss,ssh-rsa]{lang="EN-US"}]{#struct_0_28483_x1134_x188696766}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_1236610660}*[服务器端支持的主机公钥算法串]{style="font-family:宋体"}*

[[\*Dec 31 20:46:58:358 2009 Sysname SSHC/7/EVENT: Kex strings(2): aes128-cbc,3des-cbc,des-cbc]{lang="EN-US"}]{#struct_0_28483_x1134_x2013195053}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x693266390}*[客户端到服务器端的加密算法串]{style="font-family:宋体"}*

[[\*Dec 31 20:46:58:369 2009 Sysname SSHC/7/EVENT: Kex strings(3): aes128-cbc,3des-cbc,des-cbc]{lang="EN-US"}]{#struct_0_28483_x1134_x1903882575}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x146896943}*[服务器端到客户端的加密算法串]{style="font-family:宋体"}*

[[\*Dec 31 20:46:58:394 2009 Sysname SSHC/7/EVENT: Kex strings(4): hmac-sha1,hmac-sha1-96,hmac-md5,hmac-md5-96]{lang="EN-US"}]{#struct_0_28483_x1134_1075729964}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x188762302}*[客户端到服务器端的]{style="font-family:宋体"}[HMAC]{lang="EN-US"}[算法串]{style="font-family:宋体"}*

[[\*Dec 31 20:46:58:404 2009 Sysname SSHC/7/EVENT: Kex strings(5): hmac-sha1,hmac-sha1-96,hmac-md5,hmac-md5-96]{lang="EN-US"}]{#struct_0_28483_x1134_x305243177}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x342393826}*[服务器端到客户端的]{style="font-family:宋体"}[HMAC]{lang="EN-US"}[算法串]{style="font-family:宋体"}*

[[\*Dec 31 20:46:58:421 19692009 Sysname SSHC/7/EVENT: Kex strings(6): none,zlib,zlib@openssh.com]{lang="EN-US"}]{#struct_0_28483_x1134_x1180066732}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_386113395}*[客户端到服务器端的压缩算法串]{style="font-family:宋体"}*

[[\*Dec 31 20:46:58:426 2009 Sysname SSHC/7/EVENT: Kex strings(7): none,zlib,zlib@openssh.com]{lang="EN-US"}]{#struct_0_28483_x1134_x88299263}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_1249467416}*[服务器端到客户端的压缩算法串]{style="font-family:宋体"}*

[[\*Dec 31 20:46:58:440 2009 Sysname SSHC/7/EVENT: Kex strings(8):]{lang="EN-US"}]{#struct_0_28483_x1134_x188827838}

[\*Dec 31 20:46:58:446 2009 Sysname SSHC/7/EVENT: Kex strings(9):]{lang="EN-US"}

[\*Dec 31 20:46:58:452 2009 Sysname SSHC/7/EVENT: Peer proposal kex:]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_35300160}*[服务器端的版本协商算法串信息如下]{style="font-family:宋体"}*

[[\*Dec 31 20:46:58:460 2009 Sysname SSHC/7/EVENT: Kex strings(0): diffie-hellman-group-exchange-sha1,diffie-hellman-group14-sha1,diffie-hellman-group1-sha1]{lang="EN-US"}]{#struct_0_28483_x1134_x1104143386}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_425242705}*[密钥交换算法串]{style="font-family:宋体"}*

[[\*Dec 31 20:46:58:463 2009 Sysname SSHC/7/EVENT: Kex strings(1): ssh-dss,ssh-rsa]{lang="EN-US"}]{#struct_0_28483_x1134_x1602232230}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_137300162}*[服务器端支持的主机公钥算法串]{style="font-family:宋体"}*

[[\*Dec 31 20:46:58:468 2009 Sysname SSHC/7/EVENT: Kex strings(2): aes128-cbc,3des-cbc,des-cbc]{lang="EN-US"}]{#struct_0_28483_x1134_x1738882962}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_411663673}*[客户端到服务器端的加密算法串]{style="font-family:宋体"}*

[[\*Dec 31 20:46:58:475 2009 Sysname SSHC/7/EVENT: Kex strings(3): aes128-cbc,3des-cbc,des-cbc]{lang="EN-US"}]{#struct_0_28483_x1134_x188893374}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x1890529072}*[服务器端到客户端的加密算法串]{style="font-family:宋体"}*

[[\*Dec 31 20:46:58:477 2009 Sysname SSHC/7/EVENT: Kex strings(4): hmac-sha1,hmac-sha1-96,hmac-md5,hmac-md5-96]{lang="EN-US"}]{#struct_0_28483_x1134_x444456149}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x2003610192}*[客户端到服务器端的]{style="font-family:宋体"}[HMAC]{lang="EN-US"}[算法串]{style="font-family:宋体"}*

[[\*Dec 31 20:46:58:480 2009 Sysname SSHC/7/EVENT: Kex strings(5): hmac-sha1,hmac-sha1-96,hmac-md5,hmac-md5-96]{lang="EN-US"}]{#struct_0_28483_x1134_1228071864}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_388081793}*[服务器端到客户端的]{style="font-family:宋体"}[HMAC]{lang="EN-US"}[算法串]{style="font-family:宋体"}*

[[\*Dec 31 20:46:58:484 2009 Sysname SSHC/7/EVENT: Kex strings(6): none]{lang="EN-US"}]{#struct_0_28483_x1134_x1379415210}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x187910334}*[客户端到服务器端的压缩算法串]{style="font-family:宋体"}*

[[\*Dec 31 20:46:58:486 2009 Sysname SSHC/7/EVENT: Kex strings(7): none]{lang="EN-US"}]{#struct_0_28483_x1134_659244366}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x1183261588}*[服务器端到客户端的压缩算法串]{style="font-family:宋体"}*

[[\*Dec 31 20:46:58:494 2009 Sysname SSHC/7/EVENT: Kex strings(8):]{lang="EN-US"}]{#struct_0_28483_x1134_x2066279952}

[\*Dec 31 20:46:58:497 2009 Sysname SSHC/7/EVENT: Kex strings(9):]{lang="EN-US"}

[\*Dec 31 20:46:58:499 2009 Sysname SSHC/7/EVENT: Kex: server-\>client, Encrypt: aes128-cbc, HMAC: hmac-sha1, Compress: none]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x903660706}*[协商出来的服务器端到客户端的加密算法、]{style="font-family:宋体"}[HMAC]{lang="EN-US"}[算法和压缩算法]{style="font-family:宋体"}*

[[\*Dec 31 20:46:58:502 2009 Sysname SSHC/7/EVENT: Kex: client-\>server, Encrypt: aes128-cbc, HMAC: hmac-sha1, Compress: none]{lang="EN-US"}]{#struct_0_28483_x1134_x1168248412}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x1777511681}*[协商出来的客户端到服务器端的加密算法、]{style="font-family:宋体"}[HMAC]{lang="EN-US"}[算法和压缩算法]{style="font-family:宋体"}*

[[\*Dec 31 20:46:58:504 2009 Sysname SSHC/7/EVENT: Expecting packet type 31.]{lang="EN-US"}]{#struct_0_28483_x1134_x187975870}

[\*Dec 31 20:47:01:576 2009 Sysname SSHC/7/EVENT: Expecting packet type 33.]{lang="EN-US"}

[The server is not authenticated. Continue? \[Y/N\]:y]{lang="EN-US"}

[Do you want to save the server public key? \[Y/N\]:n]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Dec 31 20:47:07:612 2009 Sysname SSHC/7/EVENT: DSA verify: signature correct]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_1369541713}*[进行]{style="font-family:宋体"}[DSA]{lang="EN-US"}[认证，签名正确]{style="font-family:宋体"}*

[[\*Dec 31 20:47:07:634 2009 Sysname SSHC/7/EVENT: Set new keys: mode=1]{lang="EN-US"}]{#struct_0_28483_x1134_457230277}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x1494939371}*[设置协商出来的新的算法（]{style="font-family:宋体"}[mode=1]{lang="EN-US"}[表示输出方向）]{style="font-family:宋体"}*

[[\*Dec 31 20:47:07:643 2009 Sysname SSHC/7/EVENT: Expecting packet type 21.]{lang="EN-US"}]{#struct_0_28483_x1134_2029473632}

[\*Dec 31 20:47:07:649 2009 Sysname SSHC/7/EVENT: Set new keys: mode=0]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_556893623}*[设置协商出来的新的算法（]{style="font-family:宋体"}[mode=0]{lang="EN-US"}[表示输入方向）]{style="font-family:宋体"}*

[[\*Dec 31 20:47:07:831 2009 Sysname SSHC/7/EVENT: Service accepted: reply ssh-userauth]{lang="EN-US"}]{#struct_0_28483_x1134_x188434621}

[\*Dec 31 20:47:07:859 2009 Sysname SSHC/7/EVENT: Received SSH2_MSG_USERAUTH_FAILURE.]{lang="EN-US"}

[\*Dec 31 20:47:07:866 2009 Sysname SSHC/7/EVENT: Authentication methods that can continue to try: password]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_81925976}*[认证失败，可以继续尝试的认证方法为]{style="font-family:宋体"}[password]{lang="EN-US"}[认证]{style="font-family:宋体"}*

[[\*Dec 31 20:47:07:871 2009 Sysname SSHC/7/EVENT: Passed a different authentication method list password, preferred publickey,password.]{lang="EN-US"}]{#struct_0_28483_x1134_1222688335}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x1937581965}*[传入了一个不同的认证方法列表]{style="font-family:宋体"}[password]{lang="EN-US"}[，但支持的认证方法是]{style="font-family:宋体"}[publickey]{lang="EN-US"}[、]{style="font-family:宋体"}[password]{lang="EN-US"}*

[[\*Dec 31 20:47:07:877 2009 Sysname SSHC/7/EVENT: Authentication method password is enabled.]{lang="EN-US"}]{#struct_0_28483_x1134_70420569}

[*[// Password]{lang="EN-US"}*]{#struct_0_28483_x1134_370898865}*[认证被使能]{style="font-family:宋体"}*

[[abc@192.168.0.59\'s password:]{lang="EN-US"}]{#struct_0_28483_x1134_x558645453}

[ ]{lang="EN-US"}

[\*Dec 31 20:47:09:166 2009 Sysname SSHC/7/EVENT: Try authentication method password.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x188500157}*[尝试]{style="font-family:宋体"}[Password]{lang="EN-US"}[认证]{style="font-family:宋体"}*

[[\*Dec 31 20:47:09:181 2009 Sysname SSHC/7/EVENT: Received SSH2_MSG_USERAUTH_SUCCESS.]{lang="EN-US"}]{#struct_0_28483_x1134_1244284112}

[\*Dec 31 20:47:09:185 2009 Sysname SSHC/7/EVENT: Authentication succeeded (password).]{lang="EN-US"}

[\*Dec 31 20:47:09:194 2009 Sysname SSHC/7/EVENT: Channel 0: new \[client-session\]]{lang="EN-US"}

[\*Dec 31 20:47:09:196 2009 Sysname SSHC/7/EVENT: Open new channel: 0.]{lang="EN-US"}

[\*Dec 31 20:47:09:203 2009 Sysname SSHC/7/EVENT: Entering interactive session.]{lang="EN-US"}

[\*Dec 31 20:47:09:249 2009 Sysname SSHC/7/EVENT: Channel 0: request pty-req confirm 1]{lang="EN-US"}

[\*Dec 31 20:47:09:254 2009 Sysname SSHC/7/EVENT: Channel 0: request shell confirm 1]{lang="EN-US"}

[\*Dec 31 20:47:09:272 2009 Sysname SSHC/7/EVENT: PTY allocation request accepted on channel 0]{lang="EN-US"}

[\*Dec 31 20:47:09:377 2009 Sysname SSHC/7/EVENT: shell request accepted on channel 0]{lang="EN-US"}

[*[// Password]{lang="EN-US"}*]{#struct_0_28483_x1134_x721391189}*[认证成功，]{style="font-family:宋体"}[shell]{lang="EN-US"}[请求被接受，分配通道号为]{style="font-family:宋体"}[0]{lang="EN-US"}*

[[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*]{lang="EN-US"}]{#struct_0_28483_x1134_x281184855}

[\* Copyright (c) 2004-2010 Hangzhou Sysname Tech. Co., Ltd. All rights reserved.  \*]{lang="EN-US"}

[\* Without the owner\'s prior written consent,                                 \*]{lang="EN-US"}

[\* no decompiling or reverse-engineering shall be allowed.                    \*]{lang="EN-US"}

[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*]{lang="EN-US"}

[ ]{lang="EN-US"}

[\<Sysname\>]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x188565693}*[用户]{style="font-family:宋体"}[abc]{lang="EN-US"}[成功登录设备]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_28483_x1134_x1486189605}[打开]{style="font-family:宋体"}[SSH]{lang="EN-US"}[客户端的消息调试信息开关。设备作为]{style="font-family:宋体"}[SFTP]{lang="EN-US"}[客户端（]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.0.55]{lang="EN-US"}[）登录远端]{style="font-family:宋体"}[SFTP]{lang="EN-US"}[服务器（]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.0.59]{lang="EN-US"}[），用户名为]{style="font-family:宋体"}[abc]{lang="EN-US"}[、密码为]{style="font-family:宋体"}[abc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> debugging ssh client message]{lang="EN-US"}]{#struct_0_28483_x1134_x1301474292}

[\<Sysname\> sftp 192.168.0.59]{lang="EN-US"}

[Username: abc]{lang="EN-US"}

[Connecting to 192.168.0.59 port 22.]{lang="EN-US"}

[\*Dec 31 16:11:03:507 2009 Sysname SSHC/7/MESSAGE: Prepare packet\[20\].]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x358044316}*[准备消息，消息类型为]{style="font-family:宋体"}[20]{lang="EN-US"}[（以下各消息涵义类似，解释略）]{style="font-family:宋体"}*

[[\*Dec 31 16:11:03:510 2009 Sysname SSHC/7/MESSAGE: Received packet type 20.]{lang="EN-US"}]{#struct_0_28483_x1134_881991480}

[*[// ]{lang="EN-US"}*]{#struct_0_28483_x1134_x1290276287}*[接收到消息，消息类型为]{style="font-family:宋体"}[20]{lang="EN-US"}[（以下各消息涵义类似，解释略）]{style="font-family:宋体"}*

[[\*Dec 31 16:11:03:518 2009 Sysname SSHC/7/MESSAGE:Prepare packet\[34\].]{lang="EN-US"}]{#struct_0_28483_x1134_x188631229}

[\*Dec 31 16:11:03:625 2009 Sysname SSHC/7/MESSAGE: Received packet type 31.]{lang="EN-US"}

[\*Dec 31 16:11:05:218 2009 Sysname SSHC/7/MESSAGE: Prepare packet\[32\].]{lang="EN-US"}

[\*Dec 31 16:11:05:466 2009 Sysname SSHC/7/MESSAGE: Received packet type 33.]{lang="EN-US"}

[The server is not authenticated. Continue? \[Y/N\]:y]{lang="EN-US"}

[Do you want to save the server public key? \[Y/N\]:n]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Dec 31 16:11:09:252 2009 Sysname SSHC/7/MESSAGE: Prepare packet\[21\].]{lang="EN-US"}

[\*Dec 31 16:11:09:255 2009 Sysname SSHC/7/MESSAGE: Received packet type 21.]{lang="EN-US"}

[\*Dec 31 16:11:09:256 2009 Sysname SSHC/7/MESSAGE: Prepare packet\[5\].]{lang="EN-US"}

[\*Dec 31 16:11:09:266 2009 Sysname SSHC/7/MESSAGE: Received packet type 6.]{lang="EN-US"}

[\*Dec 31 16:11:09:282 2009 Sysname SSHC/7/MESSAGE: Prepare packet\[50\].]{lang="EN-US"}

[\*Dec 31 16:11:09:287 2009 Sysname SSHC/7/MESSAGE: Received packet type 51.]{lang="EN-US"}

[abc@192.168.0.59\'s password:]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Dec 31 16:11:11:184 2009 Sysname SSHC/7/MESSAGE: Prepare packet\[50\].]{lang="EN-US"}

[\*Dec 31 16:11:11:193 2009 Sysname SSHC/7/MESSAGE: Received packet type 52.]{lang="EN-US"}

[\*Dec 31 16:11:11:194 2009 Sysname SSHC/7/MESSAGE: Prepare packet\[90\].]{lang="EN-US"}

[\*Dec 31 16:11:11:197 2009 Sysname SSHC/7/MESSAGE: Received packet type 91.]{lang="EN-US"}

[\*Dec 31 16:11:11:201 2009 Sysname SSHC/7/MESSAGE: Prepare packet\[98\].]{lang="EN-US"}

[\*Dec 31 16:11:11:205 2009 Sysname SSHC/7/MESSAGE: Received packet type 99.]{lang="EN-US"}

[\*Dec 31 16:11:11:209 2009 Sysname SSHC/7/MESSAGE: Received packet type 94.sftp\>]{lang="EN-US"}

[\*Dec 31 16:11:11:219 2009 Sysname SSHC/7/MESSAGE: Received packet type 94.]{lang="EN-US"}

[sftp\>]{lang="EN-US"}

[ ]{lang="EN-US"}
