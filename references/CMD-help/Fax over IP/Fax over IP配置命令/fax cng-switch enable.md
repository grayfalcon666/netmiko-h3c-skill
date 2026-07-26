::: {#1072479413 .myid}
[]{#_Toc404794539}[]{#struct_0_61420_36717_x93818529}

**Fax over IP \-- Fax over IP配置命令 \-- fax cng-switch enable**

------------------------------------------------------------------------

[**[fax]{lang="EN-US"}**[ **cng-switch** **enable**]{lang="EN-US"}]{#struct_0_61420_36717_1041865474}[命令配置用来开启]{style="font-family:宋体"}[CNG]{lang="EN-US"}[传真切换。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **fax** **cng-switch** **enable**]{lang="EN-US"}]{#struct_0_61420_36717_x1842437608}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_61420_36717_x697874176}

[**[fax]{lang="EN-US"}**[ **cng-switch** **enable**]{lang="EN-US"}]{#struct_0_61420_36717_174651667}

[**[undo]{lang="EN-US"}**[ **fax** **cng-switch** **enable**]{lang="EN-US"}]{#struct_0_61420_36717_1003521933}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_61420_36717_x637036575}

[[CNG]{lang="EN-US"}]{#struct_0_61420_36717_1666775159}[传真切换处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_61420_36717_2091358828}

[[POTS/VoIP]{lang="EN-US"}]{#struct_0_61420_36717_x2095012173}[语音实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_61420_36717_x1496885099}

[[network-admin]{lang="EN-US"}]{#struct_0_61420_36717_x1304304010}

[[mdc-admin]{lang="EN-US"}]{#struct_0_61420_36717_x493242908}

[[【举例】]{style="font-family:黑体"}]{#struct_0_61420_36717_x943637427}

[[\# ]{lang="EN-US"}]{#struct_0_61420_36717_238930567}[开启]{style="font-family:宋体"}[CNG]{lang="EN-US"}[传真切换。]{style="font-family:宋体"}

[[\<sysname\> system-view]{lang="EN-US"}]{#struct_0_61420_36717_x79253166}

[\[sysname\] voice-setup]{lang="EN-US"}

[\[sysname-voice\] dial-program]{lang="EN-US"}

[\[sysname-voice-dial\] entity 100 pots]{lang="EN-US"}

[\[sysname-voice-dial-entity100\] fax cng-switch enable]{lang="EN-US"}
:::

::: {#552706026 .myid}
[]{#_Toc404794540}[]{#struct_0_61420_36717_x178343568}

**Fax over IP \-- Fax over IP配置命令 \-- fax ecm**

------------------------------------------------------------------------

[**[fax]{lang="EN-US"}**[ **ecm**]{lang="EN-US"}]{#struct_0_61420_36717_x1842634216}[命令用来配置传真使用]{style="font-family:宋体"}[ECM]{lang="EN-US"}[方式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **fax** **ecm**]{lang="EN-US"}]{#struct_0_61420_36717_x1633942362}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_61420_36717_599916813}

[**[fax]{lang="EN-US"}**[ **ecm**]{lang="EN-US"}]{#struct_0_61420_36717_x1207197007}

[**[undo]{lang="EN-US"}**[ **fax** **ecm**]{lang="EN-US"}]{#struct_0_61420_36717_1632090332}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_61420_36717_x1275587299}

[[不使用]{style="font-family:宋体"}[ECM]{lang="EN-US"}]{#struct_0_61420_36717_1027290414}[方式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_61420_36717_x24693727}

[[POTS/VoIP]{lang="EN-US"}]{#struct_0_61420_36717_x823342425}[语音实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_61420_36717_x1654920657}

[[network-admin]{lang="EN-US"}]{#struct_0_61420_36717_x301725627}

[[mdc-admin]{lang="EN-US"}]{#struct_0_61420_36717_258553998}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_61420_36717_1336752846}

[[实际配置传真使用]{style="font-family:宋体"}[ECM]{lang="EN-US"}]{#struct_0_61420_36717_562888180}[方式时，请确认两端传真机都支持]{style="font-family:宋体"}[ECM]{lang="EN-US"}[方式，并且在发送和接收侧设备上的]{style="font-family:宋体"}[VoIP]{lang="EN-US"}[语音实体和]{style="font-family:宋体"}[POTS]{lang="EN-US"}[语音实体下配置]{style="font-family:宋体"}[ECM]{lang="EN-US"}[方式处于开启状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_61420_36717_88249870}

[[\# ]{lang="EN-US"}]{#struct_0_61420_36717_887140440}[配置传真使用]{style="font-family:宋体"}[ECM]{lang="EN-US"}[方式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_61420_36717_x1842568680}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 4 pots]{lang="EN-US"}

[\[Sysname-voice-dial-entity4\] ]{lang="FR"}[fax ecm]{lang="EN-US"}
:::

::: {#1873209395 .myid}
[]{#_Toc404794541}[]{#struct_0_61420_36717_x743297911}[]{#_Toc345245916}[]{#_Toc346096024}[]{#_Toc345245917}[]{#_Toc346096025}[]{#_Toc345245918}[]{#_Toc346096026}[]{#_Toc345245919}[]{#_Toc346096027}[]{#_Toc345245920}[]{#_Toc346096028}[]{#_Toc345245921}[]{#_Toc346096029}[]{#_Toc345245922}[]{#_Toc346096030}[]{#_Toc345245923}[]{#_Toc346096031}[]{#_Toc345245924}[]{#_Toc346096032}[]{#_Toc345245925}[]{#_Toc346096033}[]{#_Toc345245926}[]{#_Toc346096034}[]{#_Toc345245927}[]{#_Toc346096035}[]{#_Toc345245928}[]{#_Toc346096036}[]{#_Toc345245929}[]{#_Toc346096037}[]{#_Toc345245930}[]{#_Toc346096038}[]{#_Toc345245931}[]{#_Toc346096039}[]{#_Toc345245932}[]{#_Toc346096040}[]{#_Toc345245933}[]{#_Toc346096041}[]{#_Toc345245934}[]{#_Toc346096042}[]{#_Toc345245935}[]{#_Toc346096043}[]{#_Toc345245936}[]{#_Toc346096044}[]{#_Toc345245937}[]{#_Toc346096045}[]{#_Toc345245938}[]{#_Toc346096046}[]{#_Toc345245939}[]{#_Toc346096047}[]{#_Toc345245940}[]{#_Toc346096048}[]{#_Toc345245941}[]{#_Toc346096049}[]{#_Toc345245942}[]{#_Toc346096050}[]{#_Toc345245943}[]{#_Toc346096051}[]{#_Toc345245944}[]{#_Toc346096052}[]{#_Toc345245945}[]{#_Toc346096053}[]{#_Toc345245946}[]{#_Toc346096054}[]{#_Toc345245947}[]{#_Toc346096055}[]{#_Toc345245948}[]{#_Toc346096056}[]{#_Toc345245949}[]{#_Toc346096057}[]{#_Toc345245950}[]{#_Toc346096058}[]{#_Toc345245951}[]{#_Toc346096059}[]{#_Toc345245952}[]{#_Toc346096060}[]{#_Toc345245953}[]{#_Toc346096061}[]{#_Toc345245954}[]{#_Toc346096062}[]{#_Toc345245955}[]{#_Toc346096063}[]{#_Toc345245956}[]{#_Toc346096064}[]{#_Toc345245957}[]{#_Toc346096065}[]{#_Toc345245958}[]{#_Toc346096066}[]{#_Toc345245959}[]{#_Toc346096067}[]{#_Toc345245960}[]{#_Toc346096068}[]{#_Toc345245961}[]{#_Toc346096069}[]{#_Toc345245962}[]{#_Toc346096070}[]{#_Toc345245963}[]{#_Toc346096071}[]{#_Toc345245964}[]{#_Toc346096072}[]{#_Toc345245965}[]{#_Toc346096073}[]{#_Toc345245966}[]{#_Toc346096074}[]{#_Toc345245967}[]{#_Toc346096075}[]{#_Toc345245968}[]{#_Toc346096076}[]{#_Toc345245969}[]{#_Toc346096077}[]{#_Toc296158651}[]{#_Toc296159966}[]{#_Toc296158652}[]{#_Toc296159967}[]{#_Toc296158653}[]{#_Toc296159968}[]{#_Toc296158654}[]{#_Toc296159969}[]{#_Toc296158655}[]{#_Toc296159970}[]{#_Toc296158656}[]{#_Toc296159971}[]{#_Toc296158657}[]{#_Toc296159972}[]{#_Toc296158658}[]{#_Toc296159973}[]{#_Toc296158659}[]{#_Toc296159974}[]{#_Toc296158660}[]{#_Toc296159975}[]{#_Toc296158661}[]{#_Toc296159976}[]{#_Toc296158662}[]{#_Toc296159977}[]{#_Toc296158663}[]{#_Toc296159978}[]{#_Toc296158664}[]{#_Toc296159979}[]{#_Toc296158665}[]{#_Toc296159980}[]{#_Toc296158666}[]{#_Toc296159981}[]{#_Toc296158667}[]{#_Toc296159982}[]{#_Toc296158668}[]{#_Toc296159983}[]{#_Toc296158669}[]{#_Toc296159984}[]{#_Toc296158670}[]{#_Toc296159985}[]{#_Toc296158671}[]{#_Toc296159986}[]{#_Toc296158672}[]{#_Toc296159987}[]{#_Toc296158677}[]{#_Toc296159992}[]{#_Toc296158685}[]{#_Toc296160000}[]{#_Toc296158686}[]{#_Toc296160001}[]{#_Toc296158687}[]{#_Toc296160002}[]{#_Toc296158716}[]{#_Toc296160031}[]{#_Toc296158718}[]{#_Toc296160033}[]{#_Toc296158719}[]{#_Toc296160034}[]{#_Toc296158720}[]{#_Toc296160035}[]{#_Toc296158721}[]{#_Toc296160036}[]{#_Toc296158722}[]{#_Toc296160037}[]{#_Toc296158723}[]{#_Toc296160038}[]{#_Toc296158724}[]{#_Toc296160039}[]{#_Toc296158725}[]{#_Toc296160040}[]{#_Toc296158726}[]{#_Toc296160041}[]{#_Toc296158727}[]{#_Toc296160042}[]{#_Toc296158728}[]{#_Toc296160043}[]{#_Toc296158729}[]{#_Toc296160044}[]{#_Toc296158730}[]{#_Toc296160045}[]{#_Toc296158731}[]{#_Toc296160046}[]{#_Toc296158732}[]{#_Toc296160047}[]{#_Toc296158733}[]{#_Toc296160048}[]{#_Toc296158734}[]{#_Toc296160049}[]{#_Toc296158735}[]{#_Toc296160050}[]{#_Toc296158736}[]{#_Toc296160051}[]{#_Toc296158737}[]{#_Toc296160052}[]{#_Toc296158738}[]{#_Toc296160053}[]{#_Toc296158739}[]{#_Toc296160054}[]{#_Toc296158740}[]{#_Toc296160055}[]{#_Toc296158741}[]{#_Toc296160056}[]{#_Toc296158742}[]{#_Toc296160057}[]{#_Toc296158743}[]{#_Toc296160058}[]{#_Toc296158745}[]{#_Toc296160060}[]{#_Toc296158747}[]{#_Toc296160062}[]{#_Toc296158750}[]{#_Toc296160065}[]{#_Toc296158752}[]{#_Toc296160067}[]{#_Toc296158753}[]{#_Toc296160068}[]{#_Toc296158754}[]{#_Toc296160069}[]{#_Toc296158755}[]{#_Toc296160070}[]{#_Toc296158756}[]{#_Toc296160071}[]{#_Toc296158757}[]{#_Toc296160072}[]{#_Toc296158760}[]{#_Toc296160075}[]{#_Toc296158761}[]{#_Toc296160076}[]{#_Toc296158762}[]{#_Toc296160077}[]{#_Toc296158795}[]{#_Toc296160110}[]{#_Toc137035624}[]{#_Toc137036654}[]{#_Toc137041713}[]{#_Toc137042384}[]{#_Toc87442398}[]{#_Toc87787038}[]{#_Toc87851901}[]{#_Toc87852680}[]{#_Toc87853461}[]{#_Toc87867500}[]{#_Toc87442408}[]{#_Toc87787048}[]{#_Toc87851911}[]{#_Toc87852690}[]{#_Toc87853471}[]{#_Toc87867510}[]{#_Toc87442409}[]{#_Toc87787049}[]{#_Toc87851912}[]{#_Toc87852691}[]{#_Toc87853472}[]{#_Toc87867511}[]{#_Toc87442410}[]{#_Toc87787050}[]{#_Toc87851913}[]{#_Toc87852692}[]{#_Toc87853473}[]{#_Toc87867512}[]{#_Toc87442411}[]{#_Toc87787051}[]{#_Toc87851914}[]{#_Toc87852693}[]{#_Toc87853474}[]{#_Toc87867513}[]{#_Toc87442412}[]{#_Toc87787052}[]{#_Toc87851915}[]{#_Toc87852694}[]{#_Toc87853475}[]{#_Toc87867514}[]{#_Toc87442413}[]{#_Toc87787053}[]{#_Toc87851916}[]{#_Toc87852695}[]{#_Toc87853476}[]{#_Toc87867515}[]{#_Toc87442414}[]{#_Toc87787054}[]{#_Toc87851917}[]{#_Toc87852696}[]{#_Toc87853477}[]{#_Toc87867516}[]{#_Toc87442415}[]{#_Toc87787055}[]{#_Toc87851918}[]{#_Toc87852697}[]{#_Toc87853478}[]{#_Toc87867517}[]{#_Toc87442416}[]{#_Toc87787056}[]{#_Toc87851919}[]{#_Toc87852698}[]{#_Toc87853479}[]{#_Toc87867518}[]{#_Toc87442417}[]{#_Toc87787057}[]{#_Toc87851920}[]{#_Toc87852699}[]{#_Toc87853480}[]{#_Toc87867519}[]{#_Toc87442418}[]{#_Toc87787058}[]{#_Toc87851921}[]{#_Toc87852700}[]{#_Toc87853481}[]{#_Toc87867520}[]{#_Toc87442419}[]{#_Toc87787059}[]{#_Toc87851922}[]{#_Toc87852701}[]{#_Toc87853482}[]{#_Toc87867521}[]{#_Toc87442420}[]{#_Toc87787060}[]{#_Toc87851923}[]{#_Toc87852702}[]{#_Toc87853483}[]{#_Toc87867522}[]{#_Toc87442426}[]{#_Toc87787066}[]{#_Toc87851929}[]{#_Toc87852708}[]{#_Toc87853489}[]{#_Toc87867528}[]{#_Toc35952990}[]{#_Toc35953393}[]{#_Toc35954277}[]{#_Toc35955154}[]{#_Toc296158797}[]{#_Toc296160112}[]{#_Toc296158798}[]{#_Toc296160113}[]{#_Toc296158799}[]{#_Toc296160114}[]{#_Toc296158800}[]{#_Toc296160115}[]{#_Toc296158801}[]{#_Toc296160116}[]{#_Toc296158802}[]{#_Toc296160117}[]{#_Toc296158803}[]{#_Toc296160118}[]{#_Toc296158804}[]{#_Toc296160119}[]{#_Toc296158805}[]{#_Toc296160120}[]{#_Toc296158806}[]{#_Toc296160121}[]{#_Toc296158807}[]{#_Toc296160122}[]{#_Toc296158808}[]{#_Toc296160123}[]{#_Toc296158809}[]{#_Toc296160124}[]{#_Toc296158810}[]{#_Toc296160125}[]{#_Toc296158811}[]{#_Toc296160126}[]{#_Toc296158812}[]{#_Toc296160127}[]{#_Toc296158813}[]{#_Toc296160128}[]{#_Toc296158814}[]{#_Toc296160129}[]{#_Toc296158815}[]{#_Toc296160130}[]{#_Toc296158816}[]{#_Toc296160131}[]{#_Toc296158817}[]{#_Toc296160132}[]{#_Toc296158821}[]{#_Toc296160136}[]{#_Toc296158826}[]{#_Toc296160141}[]{#_Toc296158839}[]{#_Toc296160154}[]{#_Toc296158840}[]{#_Toc296160155}[]{#_Toc296158841}[]{#_Toc296160156}[]{#_Toc296158842}[]{#_Toc296160157}[]{#_Toc296158843}[]{#_Toc296160158}[]{#_Toc296158844}[]{#_Toc296160159}[]{#_Toc296158845}[]{#_Toc296160160}[]{#_Toc296158846}[]{#_Toc296160161}[]{#_Toc296158847}[]{#_Toc296160162}[]{#_Toc296158848}[]{#_Toc296160163}[]{#_Toc296158849}[]{#_Toc296160164}[]{#_Toc296158850}[]{#_Toc296160165}[]{#_Toc296158851}[]{#_Toc296160166}[]{#_Toc296158852}[]{#_Toc296160167}[]{#_Toc296158853}[]{#_Toc296160168}[]{#_Toc296158854}[]{#_Toc296160169}[]{#_Toc296158855}[]{#_Toc296160170}[]{#_Toc296158856}[]{#_Toc296160171}[]{#_Toc296158857}[]{#_Toc296160172}[]{#_Toc296158858}[]{#_Toc296160173}[]{#_Toc296158859}[]{#_Toc296160174}[]{#_Toc296158860}[]{#_Toc296160175}[]{#_Toc296158861}[]{#_Toc296160176}[]{#_Toc296158862}[]{#_Toc296160177}[]{#_Toc296158877}[]{#_Toc296160192}[]{#_Toc296158878}[]{#_Toc296160193}[]{#_Toc296158915}[]{#_Toc296160230}[]{#_Toc296158917}[]{#_Toc296160232}[]{#_Toc296158918}[]{#_Toc296160233}[]{#_Toc296158919}[]{#_Toc296160234}[]{#_Toc296158920}[]{#_Toc296160235}[]{#_Toc296158921}[]{#_Toc296160236}[]{#_Toc296158922}[]{#_Toc296160237}[]{#_Toc296158923}[]{#_Toc296160238}[]{#_Toc296158924}[]{#_Toc296160239}[]{#_Toc296158925}[]{#_Toc296160240}[]{#_Toc296158926}[]{#_Toc296160241}[]{#_Toc296158927}[]{#_Toc296160242}[]{#_Toc296158928}[]{#_Toc296160243}[]{#_Toc296158929}[]{#_Toc296160244}[]{#_Toc296158930}[]{#_Toc296160245}[]{#_Toc296158931}[]{#_Toc296160246}[]{#_Toc296158932}[]{#_Toc296160247}[]{#_Toc296158933}[]{#_Toc296160248}[]{#_Toc296158934}[]{#_Toc296160249}[]{#_Toc296158935}[]{#_Toc296160250}[]{#_Toc296158937}[]{#_Toc296160252}[]{#_Toc296158938}[]{#_Toc296160253}[]{#_Toc296158939}[]{#_Toc296160254}[]{#_Toc296158943}[]{#_Toc296160258}[]{#_Toc296158965}[]{#_Toc296160280}[]{#_Toc296158966}[]{#_Toc296160281}[]{#_Toc296158967}[]{#_Toc296160282}[]{#_Toc296158969}[]{#_Toc296160284}[]{#_Toc296158970}[]{#_Toc296160285}[]{#_Toc296158971}[]{#_Toc296160286}[]{#_Toc296158972}[]{#_Toc296160287}[]{#_Toc296158973}[]{#_Toc296160288}[]{#_Toc296158974}[]{#_Toc296160289}[]{#_Toc296158975}[]{#_Toc296160290}[]{#_Toc296158976}[]{#_Toc296160291}[]{#_Toc296158977}[]{#_Toc296160292}[]{#_Toc296158978}[]{#_Toc296160293}[]{#_Toc296158979}[]{#_Toc296160294}[]{#_Toc296158980}[]{#_Toc296160295}[]{#_Toc296158981}[]{#_Toc296160296}[]{#_Toc296158982}[]{#_Toc296160297}[]{#_Toc296158983}[]{#_Toc296160298}[]{#_Toc296158984}[]{#_Toc296160299}[]{#_Toc296158987}[]{#_Toc296160302}[]{#_Toc296158988}[]{#_Toc296160303}[]{#_Toc296158991}[]{#_Toc296160306}[]{#_Toc296158992}[]{#_Toc296160307}[]{#_Toc296158993}[]{#_Toc296160308}[]{#_Toc296158994}[]{#_Toc296160309}[]{#_Toc296158995}[]{#_Toc296160310}[]{#_Toc296158996}[]{#_Toc296160311}[]{#_Toc296158997}[]{#_Toc296160312}[]{#_Toc296158998}[]{#_Toc296160313}[]{#_Toc296158999}[]{#_Toc296160314}[]{#_Toc296159000}[]{#_Toc296160315}[]{#_Toc296159001}[]{#_Toc296160316}[]{#_Toc296159002}[]{#_Toc296160317}[]{#_Toc296159003}[]{#_Toc296160318}[]{#_Toc296159004}[]{#_Toc296160319}[]{#_Toc296159005}[]{#_Toc296160320}[]{#_Toc296159006}[]{#_Toc296160321}[]{#_Toc296159007}[]{#_Toc296160322}[]{#_Toc296159010}[]{#_Toc296160325}[]{#_Toc296159011}[]{#_Toc296160326}[]{#_Toc296159014}[]{#_Toc296160329}[]{#_Toc296159015}[]{#_Toc296160330}[]{#_Toc296159016}[]{#_Toc296160331}[]{#_Toc296159017}[]{#_Toc296160332}[]{#_Toc296159018}[]{#_Toc296160333}[]{#_Toc296159019}[]{#_Toc296160334}[]{#_Toc296159020}[]{#_Toc296160335}[]{#_Toc296159021}[]{#_Toc296160336}[]{#_Toc296159022}[]{#_Toc296160337}[]{#_Toc296159023}[]{#_Toc296160338}[]{#_Toc296159024}[]{#_Toc296160339}[]{#_Toc296159025}[]{#_Toc296160340}[]{#_Toc296159026}[]{#_Toc296160341}[]{#_Toc296159027}[]{#_Toc296160342}[]{#_Toc296159028}[]{#_Toc296160343}[]{#_Toc296159029}[]{#_Toc296160344}[]{#_Toc296159030}[]{#_Toc296160345}[]{#_Toc296159034}[]{#_Toc296160349}[]{#_Toc296159035}[]{#_Toc296160350}[]{#_Toc296159042}[]{#_Toc296160357}[]{#_Toc354744830}[]{#_Toc354817950}[]{#_Toc354935986}[]{#_Toc355261822}[]{#_Toc355262297}[]{#_Toc355262382}[]{#_Toc354744831}[]{#_Toc354817951}[]{#_Toc354935987}[]{#_Toc355261823}[]{#_Toc355262298}[]{#_Toc355262383}[]{#_Toc354744832}[]{#_Toc354817952}[]{#_Toc354935988}[]{#_Toc355261824}[]{#_Toc355262299}[]{#_Toc355262384}[]{#_Toc354744833}[]{#_Toc354817953}[]{#_Toc354935989}[]{#_Toc355261825}[]{#_Toc355262300}[]{#_Toc355262385}[]{#_Toc354744834}[]{#_Toc354817954}[]{#_Toc354935990}[]{#_Toc355261826}[]{#_Toc355262301}[]{#_Toc355262386}[]{#_Toc354744835}[]{#_Toc354817955}[]{#_Toc354935991}[]{#_Toc355261827}[]{#_Toc355262302}[]{#_Toc355262387}[]{#_Toc354744836}[]{#_Toc354817956}[]{#_Toc354935992}[]{#_Toc355261828}[]{#_Toc355262303}[]{#_Toc355262388}[]{#_Toc354744837}[]{#_Toc354817957}[]{#_Toc354935993}[]{#_Toc355261829}[]{#_Toc355262304}[]{#_Toc355262389}[]{#_Toc354744838}[]{#_Toc354817958}[]{#_Toc354935994}[]{#_Toc355261830}[]{#_Toc355262305}[]{#_Toc355262390}[]{#_Toc354744839}[]{#_Toc354817959}[]{#_Toc354935995}[]{#_Toc355261831}[]{#_Toc355262306}[]{#_Toc355262391}[]{#_Toc354744840}[]{#_Toc354817960}[]{#_Toc354935996}[]{#_Toc355261832}[]{#_Toc355262307}[]{#_Toc355262392}[]{#_Toc354744841}[]{#_Toc354817961}[]{#_Toc354935997}[]{#_Toc355261833}[]{#_Toc355262308}[]{#_Toc355262393}[]{#_Toc354744842}[]{#_Toc354817962}[]{#_Toc354935998}[]{#_Toc355261834}[]{#_Toc355262309}[]{#_Toc355262394}[]{#_Toc354744843}[]{#_Toc354817963}[]{#_Toc354935999}[]{#_Toc355261835}[]{#_Toc355262310}[]{#_Toc355262395}[]{#_Toc354744844}[]{#_Toc354817964}[]{#_Toc354936000}[]{#_Toc355261836}[]{#_Toc355262311}[]{#_Toc355262396}[]{#_Toc354744845}[]{#_Toc354817965}[]{#_Toc354936001}[]{#_Toc355261837}[]{#_Toc355262312}[]{#_Toc355262397}

**Fax over IP \-- Fax over IP配置命令 \-- fax level**

------------------------------------------------------------------------

[**[fax]{lang="EN-US"}**[ **level**]{lang="EN-US"}]{#struct_0_61420_36717_x1017984603}[命令用来配置发送载波能量值。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **fax** **level**]{lang="EN-US"}]{#struct_0_61420_36717_1832932135}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_61420_36717_448265513}

[**[fax]{lang="EN-US"}**[ **level** *level*]{lang="EN-US"}]{#struct_0_61420_36717_801942079}

[**[undo]{lang="EN-US"}**[ **fax** **level**]{lang="EN-US"}]{#struct_0_61420_36717_215490115}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_61420_36717_126263975}

[[发送载波能量值为]{style="font-family:宋体"}[-15dBm]{lang="EN-US"}]{#struct_0_61420_36717_x1230036152}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_61420_36717_237568479}

[[POTS/VoIP]{lang="EN-US"}]{#struct_0_61420_36717_1992096557}[语音实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_61420_36717_x1967308314}

[[network-admin]{lang="EN-US"}]{#struct_0_61420_36717_282576939}

[[mdc-admin]{lang="EN-US"}]{#struct_0_61420_36717_2106212522}

[[【参数】]{style="font-family:黑体"}]{#struct_0_61420_36717_1982410223}

[*[level]{lang="EN-US"}*]{#struct_0_61420_36717_x1841716712}[：发送载波能量值，即发送电平衰减值，取值范围为]{style="font-family:宋体"}[-60]{lang="EN-US"}[～]{style="font-family:宋体"}[-3]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[dBm]{lang="EN-US"}[。能量值越大表示能量越大，能量值越小表示衰减越大。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_61420_36717_x1654975304}

[[在一般情况下，使用缺省的发送载波能量值即可。在其它配置正确的前提下，如果仍无法成功建立传真时，可尝试调整发送载波能量值。]{style="font-family:宋体"}]{#struct_0_61420_36717_x1194337030}

[[【举例】]{style="font-family:黑体"}]{#struct_0_61420_36717_x1817397763}

[[\# ]{lang="EN-US"}]{#struct_0_61420_36717_x1804645851}[配置发送载波能量值为]{style="font-family:宋体"}[-20dBm]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_61420_36717_x2037041868}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 4 pots]{lang="EN-US"}

[\[Sysname-voice-dial-entity4\] fax level -20]{lang="EN-US"}
:::

::: {#-598515647 .myid}
[]{#_Toc404794542}[]{#struct_0_61420_36717_x751298094}

**Fax over IP \-- Fax over IP配置命令 \-- fax local-train threshold**

------------------------------------------------------------------------

[**[fax]{lang="EN-US"}**[ **local-train** **threshold**]{lang="EN-US"}]{#struct_0_61420_36717_707303095}[命令用来配置本地训练阈值百分比。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **fax** **local-train** **threshold**]{lang="EN-US"}]{#struct_0_61420_36717_1384979332}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_61420_36717_x2071050739}

[**[fax]{lang="EN-US"}**[ **local-train** **threshold** *threshold*]{lang="EN-US"}]{#struct_0_61420_36717_x1978185766}

[**[undo]{lang="EN-US"}**[ **fax** **local-train** **threshold**]{lang="EN-US"}]{#struct_0_61420_36717_x54026376}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_61420_36717_1162189834}

[[本地训练阈值百分比为]{style="font-family:宋体"}[10]{lang="EN-US"}]{#struct_0_61420_36717_x508157073}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_61420_36717_x40218964}

[[POTS/VoIP]{lang="EN-US"}]{#struct_0_61420_36717_x1841651176}[语音实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_61420_36717_x1178176586}

[[network-admin]{lang="EN-US"}]{#struct_0_61420_36717_1675429541}

[[mdc-admin]{lang="EN-US"}]{#struct_0_61420_36717_443030283}

[[【参数】]{style="font-family:黑体"}]{#struct_0_61420_36717_x178984660}

[*[threshold]{lang="EN-US"}*]{#struct_0_61420_36717_x2030512822}[：本地训练阈值百分比，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_61420_36717_1838146348}

[[当训练方式为本地训练方式时，]{style="font-family:宋体"}**[fax]{lang="EN-US"}**[ **local-train** **threshold**]{lang="EN-US"}]{#struct_0_61420_36717_x1135465526}[命令配置的本地训练阈值百分比才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_61420_36717_x1450020180}

[[\# ]{lang="EN-US"}]{#struct_0_61420_36717_1772167103}[配置本地训练阈值百分比为]{style="font-family:宋体"}[20]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_61420_36717_x1674806290}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 10 pots]{lang="EN-US"}

[\[Sysname-voice-dial-entity10\] fax local-train threshold 20]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_61420_36717_1797013330}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fax]{lang="EN-US"}**[ **train**]{lang="EN-US"}]{#struct_0_61420_36717_1938029278}**[-mode]{lang="EN-US"}**
:::

::: {#1311172344 .myid}
[]{#_Toc404794543}[]{#struct_0_61420_36717_x586857123}

**Fax over IP \-- Fax over IP配置命令 \-- fax nsf**

------------------------------------------------------------------------

[**[fax]{lang="EN-US"}**[ **nsf**]{lang="EN-US"}]{#struct_0_61420_36717_x1842241003}[命令用来配置开启非标准能力协商的国家码和厂商码。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **fax** **nsf**]{lang="EN-US"}]{#struct_0_61420_36717_x907862592}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_61420_36717_1352206519}

[**[fax]{lang="EN-US"}**[ **nsf** *value*]{lang="EN-US"}]{#struct_0_61420_36717_x1805751888}

[**[undo]{lang="EN-US"}**[ **fax** **nsf**]{lang="EN-US"}]{#struct_0_61420_36717_1810313155}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_61420_36717_x292903052}

[[使用非标准能力协商的国家码和厂商码为]{style="font-family:宋体"}[264833]{lang="EN-US"}]{#struct_0_61420_36717_x453785418}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_61420_36717_941206438}

[[POTS/VoIP]{lang="EN-US"}]{#struct_0_61420_36717_1493628193}[语音实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_61420_36717_1379906458}

[[network-admin]{lang="EN-US"}]{#struct_0_61420_36717_172683143}

[[mdc-admin]{lang="EN-US"}]{#struct_0_61420_36717_x1473468555}

[[【参数】]{style="font-family:黑体"}]{#struct_0_61420_36717_1907466891}

[*[nsf]{lang="EN-US"}*]{#struct_0_61420_36717_x279507805}[：开启非标准能力协商的国家码和厂商码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[0xFFFFFF]{lang="EN-US"}[（两位国家码]{style="font-family:宋体"}[ + ]{lang="EN-US"}[四位厂商码），其中国家码的设置需要符合]{style="font-family:宋体"}[T.35]{lang="EN-US"}[标准。取值为]{style="font-family:宋体"}[000000]{lang="EN-US"}[时，表示使用标准能力协商。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_61420_36717_x51689113}

[[\# ]{lang="EN-US"}]{#struct_0_61420_36717_653745800}[配置开启非标准的能力协商的国家码和厂商码为]{style="font-family:宋体"}[264834]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_61420_36717_x1842175467}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 10 pots]{lang="EN-US"}

[\[Sysname-voice-dial-entity10\] fax nsf 264834]{lang="EN-US"}
:::

::: {#1958028232 .myid}
[]{#_Toc404794544}[]{#struct_0_61420_36717_x673994077}[]{#_Toc296159433}[]{#_Toc296160724}[]{#_Toc296159434}[]{#_Toc296160725}[]{#_Toc296159436}[]{#_Toc296160727}[]{#_Toc296159437}[]{#_Toc296160728}[]{#_Toc296159438}[]{#_Toc296160729}[]{#_Toc296159439}[]{#_Toc296160730}[]{#_Toc296159440}[]{#_Toc296160731}[]{#_Toc296159441}[]{#_Toc296160732}[]{#_Toc296159442}[]{#_Toc296160733}[]{#_Toc296159443}[]{#_Toc296160734}[]{#_Toc296159444}[]{#_Toc296160735}[]{#_Toc296159445}[]{#_Toc296160736}[]{#_Toc296159446}[]{#_Toc296160737}[]{#_Toc296159447}[]{#_Toc296160738}[]{#_Toc296159448}[]{#_Toc296160739}[]{#_Toc296159452}[]{#_Toc296160743}[]{#_Toc296159456}[]{#_Toc296160747}[]{#_Toc296159457}[]{#_Toc296160748}[]{#_Toc296159459}[]{#_Toc296160750}[]{#_Toc296159460}[]{#_Toc296160751}[]{#_Toc296159461}[]{#_Toc296160752}[]{#_Toc296159462}[]{#_Toc296160753}[]{#_Toc296159463}[]{#_Toc296160754}[]{#_Toc296159464}[]{#_Toc296160755}[]{#_Toc296159465}[]{#_Toc296160756}[]{#_Toc296159466}[]{#_Toc296160757}[]{#_Toc296159467}[]{#_Toc296160758}[]{#_Toc296159468}[]{#_Toc296160759}[]{#_Toc296159469}[]{#_Toc296160760}[]{#_Toc296159470}[]{#_Toc296160761}[]{#_Toc296159471}[]{#_Toc296160762}[]{#_Toc296159475}[]{#_Toc296160766}[]{#_Toc296159478}[]{#_Toc296160769}[]{#_Toc296159479}[]{#_Toc296160770}[]{#_Toc296159480}[]{#_Toc296160771}[]{#_Toc296159483}[]{#_Toc296160774}[]{#_Toc296159484}[]{#_Toc296160775}[]{#_Toc296159485}[]{#_Toc296160776}[]{#_Toc296159486}[]{#_Toc296160777}[]{#_Toc296159487}[]{#_Toc296160778}[]{#_Toc296159488}[]{#_Toc296160779}[]{#_Toc296159489}[]{#_Toc296160780}[]{#_Toc296159490}[]{#_Toc296160781}[]{#_Toc296159491}[]{#_Toc296160782}[]{#_Toc296159492}[]{#_Toc296160783}[]{#_Toc296159493}[]{#_Toc296160784}[]{#_Toc296159494}[]{#_Toc296160785}[]{#_Toc296159497}[]{#_Toc296160788}[]{#_Toc296159498}[]{#_Toc296160789}[]{#_Toc296159500}[]{#_Toc296160791}[]{#_Toc296159501}[]{#_Toc296160792}[]{#_Toc345245980}[]{#_Toc346096088}[]{#_Toc345245981}[]{#_Toc346096089}[]{#_Toc345245982}[]{#_Toc346096090}[]{#_Toc345245983}[]{#_Toc346096091}[]{#_Toc345245984}[]{#_Toc346096092}[]{#_Toc345245985}[]{#_Toc346096093}[]{#_Toc345245986}[]{#_Toc346096094}[]{#_Toc345245987}[]{#_Toc346096095}[]{#_Toc345245988}[]{#_Toc346096096}[]{#_Toc345245989}[]{#_Toc346096097}[]{#_Toc345245990}[]{#_Toc346096098}[]{#_Toc345245991}[]{#_Toc346096099}[]{#_Toc345245992}[]{#_Toc346096100}[]{#_Toc345245993}[]{#_Toc346096101}[]{#_Toc345245994}[]{#_Toc346096102}[]{#_Toc345245995}[]{#_Toc346096103}[]{#_Toc345245996}[]{#_Toc346096104}[]{#_Toc345245997}[]{#_Toc346096105}[]{#_Toc345245998}[]{#_Toc346096106}[]{#_Toc345245999}[]{#_Toc346096107}[]{#_Toc345246000}[]{#_Toc346096108}[]{#_Toc345246001}[]{#_Toc346096109}

**Fax over IP \-- Fax over IP配置命令 \-- fax protocol**

------------------------------------------------------------------------

[**[fax protocol]{lang="EN-US"}**]{#struct_0_61420_36717_x1451829940}[命令用来配置传真协议。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[fax protocol]{lang="EN-US"}**]{#struct_0_61420_36717_x1334304742}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_61420_36717_x51994849}

[**[fax protocol ]{lang="EN-US"}**[{ **pass-through** { **g711alaw** \| **g711ulaw** } \| **standard-t38** \[ **ls-redundancy** *number* \[ **hs-redundancy** *number* \] \] }]{lang="EN-US"}]{#struct_0_61420_36717_2045736928}

[**[undo fax protocol]{lang="EN-US"}**]{#struct_0_61420_36717_1436122006}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_61420_36717_x2142568910}

[[使用标准]{style="font-family:宋体"}[T.38]{lang="EN-US"}]{#struct_0_61420_36717_1038923385}[传真协议。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_61420_36717_x2031253353}

[[POTS/VoIP]{lang="EN-US"}]{#struct_0_61420_36717_x143362021}[语音实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_61420_36717_x1435162695}

[[network-admin]{lang="EN-US"}]{#struct_0_61420_36717_x780801583}

[[mdc-admin]{lang="EN-US"}]{#struct_0_61420_36717_1378859536}

[[【参数】]{style="font-family:黑体"}]{#struct_0_61420_36717_x548267379}

[**[pass-through]{lang="EN-US"}**]{#struct_0_61420_36717_x1842372075}[：]{style="font-family:宋体"}[开启传真透传方式。]{style="font-family:宋体"}

[**[g711alaw]{lang="PT-BR"}**]{#struct_0_61420_36717_x895565455}[：]{style="font-family:宋体"}[传真透传方式使用]{style="font-family:宋体"}[g711alaw]{lang="EN-US"}[编解码。]{style="font-family:宋体"}

[**[g711μlaw]{lang="EN-US"}**]{#struct_0_61420_36717_1182958556}[：传真透传方式使用]{style="font-family:宋体"}[g711]{lang="EN-US"}[m]{lang="EN-US" style="font-family:Symbol"}[law]{lang="EN-US"}[编解码。]{style="font-family:宋体"}

[**[standard-t38]{lang="PT-BR"}**]{#struct_0_61420_36717_x1025584776}[：]{style="font-family:宋体"}[使用标准]{style="font-family:宋体"}[T.38]{lang="EN-US"}[传真协议]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[ls-redundancy]{lang="PT-BR"}**]{#struct_0_61420_36717_x1905920743}[ *number*]{lang="PT-BR"}[：]{style="font-family:宋体"}[表示低速传输传真数据时的冗余包数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="PT-BR"}[～]{style="font-family:宋体"}[5]{lang="PT-BR"}[，]{style="font-family:宋体"}[缺省值为]{style="font-family:宋体"}[0]{lang="PT-BR"}[。]{style="font-family:宋体"}

[**[hs-redundancy]{lang="PT-BR"}**]{#struct_0_61420_36717_x2074512491}[ *number*]{lang="PT-BR"}[：]{style="font-family:宋体"}[表示高速传输传真数据时的冗余包数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="PT-BR"}[～]{style="font-family:宋体"}[2]{lang="PT-BR"}[，]{style="font-family:宋体"}[缺省值为]{style="font-family:宋体"}[0]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_61420_36717_x799683246}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置]{style="font-family:宋体"}]{#struct_0_61420_36717_1367984281}[使用标准]{style="font-family:宋体"}[T.38]{lang="EN-US"}[传真协议，在出现传真失败或断页情况时，可以通过配置传真冗余包，保证在网络环境较差的情况下传真成功。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[只要在传真发起方设备配置此命令，传真接收方会自动适配传真协议。]{style="font-family:宋体"}]{#struct_0_61420_36717_1768432921}

[[【举例】]{style="font-family:黑体"}]{#struct_0_61420_36717_96091263}

[[\# ]{lang="EN-US"}]{#struct_0_61420_36717_431160908}[配置标准]{style="font-family:宋体"}[T.38]{lang="EN-US"}[传真协议，低速传输传真数据时的冗余包数为]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_61420_36717_x1185799907}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 10 pots]{lang="EN-US"}

[\[Sysname-voice-dial-entity10\] fax protocol standard-t38 ls-redundancy 4]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_61420_36717_x248338460}[配置传真透传方式使用]{style="font-family:宋体"}[g711alaw]{lang="EN-US"}[编解码。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_61420_36717_x1842306539}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 10 pots]{lang="EN-US"}

[\[Sysname-voice-dial-entity10\] fax protocol pass-through g711alaw]{lang="EN-US"}
:::

::: {#-705947190 .myid}
[]{#_Toc404794545}[]{#struct_0_61420_36717_x577764575}

**Fax over IP \-- Fax over IP配置命令 \-- fax rate**

------------------------------------------------------------------------

[**[fax]{lang="EN-US"}**[ **rate**]{lang="EN-US"}]{#struct_0_61420_36717_238671118}[命令用来配置最高传真速率。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **fax** **rate**]{lang="EN-US"}]{#struct_0_61420_36717_x1068114075}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_61420_36717_200932198}

[]{#struct_0_61420_36717_x742880407}[]{#_Hlt20797640}**[fax]{lang="EN-US"}**[ **rate** { **2400** \| **4800** \| **7200** \| **9600** \| **12000** \| **14400** \| **disable** \| **voice** }]{lang="EN-US"}

[**[undo]{lang="EN-US"}**[ **fax** **rate**]{lang="EN-US"}]{#struct_0_61420_36717_2067206609}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_61420_36717_x1759247701}

[[根据不同的语音编解码协商允许的最高传真速率。]{style="font-family:宋体"}]{#struct_0_61420_36717_1160752572}

[[【视图】]{style="font-family:黑体"}]{#struct_0_61420_36717_1119698088}

[[POTS/VoIP]{lang="EN-US"}]{#struct_0_61420_36717_x1227707965}[语音实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_61420_36717_x1497667986}

[[network-admin]{lang="EN-US"}]{#struct_0_61420_36717_x323259009}

[[mdc-admin]{lang="EN-US"}]{#struct_0_61420_36717_x1336665559}

[[【参数】]{style="font-family:黑体"}]{#struct_0_61420_36717_x2010660954}

[**[2400]{lang="EN-US"}**]{#struct_0_61420_36717_1470880560}[：优先使用最高传真速率为]{style="font-family:宋体"}[2400bps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[4800]{lang="EN-US"}**]{#struct_0_61420_36717_x1842503147}[：优先使用]{style="font-family:宋体"}[V.27]{lang="EN-US"}[调制解调标准进行协商，最高传真速率为]{style="font-family:宋体"}[4800bps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[7200]{lang="EN-US"}**]{#struct_0_61420_36717_1229181035}[：优先使用]{style="font-family:宋体"}[V.29]{lang="EN-US"}[调制解调标准进行协商，最高传真速率为]{style="font-family:宋体"}[7200bps]{lang="EN-US"}

[**[9600]{lang="EN-US"}**]{#struct_0_61420_36717_x995705145}[：优先使用]{style="font-family:宋体"}[V.29]{lang="EN-US"}[调制解调标准进行协商，最高传真速率为]{style="font-family:宋体"}[9600bps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[12000]{lang="EN-US"}**]{#struct_0_61420_36717_x368269221}[：优先使用]{style="font-family:宋体"}[V.17]{lang="EN-US"}[调制解调标准进行协商，最高传真速率为]{style="font-family:宋体"}[12000bps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[14400]{lang="EN-US"}**]{#struct_0_61420_36717_x2118613995}[：优先使用]{style="font-family:宋体"}[V.17]{lang="EN-US"}[调制解调标准进行协商，最高传真速率为]{style="font-family:宋体"}[14400bps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[disable]{lang="EN-US"}**]{#struct_0_61420_36717_1963294583}[：禁止传真功能。]{style="font-family:宋体"}

[**[voice]{lang="EN-US"}**]{#struct_0_61420_36717_716056178}[：根据不同的语音编解码协商允许的最高传真速率。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若使用]{style="font-family:宋体"}]{#struct_0_61420_36717_x1984123322}[G.711]{lang="EN-US"}[语音编解码协议，最高传真速率为]{style="font-family:宋体"}[14400bps]{lang="EN-US"}[，对应调制解调标准为]{style="font-family:宋体"}[V.17]{lang="EN-US"}[；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若使用]{style="font-family:宋体"}]{#struct_0_61420_36717_x1355088105}[G.723.1 Annex A]{lang="EN-US"}[语音编解码协议，最高传真速率为]{style="font-family:宋体"}[4800bps]{lang="EN-US"}[，对应调制解调标准为]{style="font-family:宋体"}[V.27]{lang="EN-US"}[；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若是用]{style="font-family:宋体"}]{#struct_0_61420_36717_1816560170}[G.726]{lang="EN-US"}[语音编解码协议，最高传真速率为]{style="font-family:宋体"}[14400bps]{lang="EN-US"}[，对应调制解调标准为]{style="font-family:宋体"}[V.17]{lang="EN-US"}[；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若使用]{style="font-family:宋体"}]{#struct_0_61420_36717_90113149}[G.729]{lang="EN-US"}[语音编解码协议，最高传真速率为]{style="font-family:宋体"}[7200bps]{lang="EN-US"}[，对应调制解调标准为]{style="font-family:宋体"}[V.29]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_61420_36717_x402274113}

[[如果速率配置为除"]{style="font-family:宋体"}**[disable]{lang="EN-US"}**]{#struct_0_61420_36717_x191642837}["、"]{style="font-family:宋体"}**[voice]{lang="EN-US"}**["之外参数，则优先使用该速率对应的调制解调标准进行速率协商，如果协商不成功，就依次递减协商的速率，重新协商。这里配置的速率是允许的最高传真速率，而不是指定使用该速率进行传真。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_61420_36717_1185824046}

[[\# ]{lang="EN-US"}]{#struct_0_61420_36717_1153386714}[配置优先使用]{style="font-family:宋体"}[V.29]{lang="EN-US"}[调制解调标准进行速率协商，最高传真速率为]{style="font-family:宋体"}[9600bps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_61420_36717_x130913901}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 4 pots]{lang="EN-US"}

[\[Sysname-voice-dial-entity4\] ]{lang="FR"}[fax rate 9600]{lang="EN-US"}
:::

::: {#176841284 .myid}
[]{#_Toc404794546}[]{#struct_0_61420_36717_x496805997}

**Fax over IP \-- Fax over IP配置命令 \-- fax train-mode**

------------------------------------------------------------------------

[**[fax]{lang="FR"}**]{#struct_0_61420_36717_x1842437611}[ **train-mode**]{lang="FR"}[命令用来配置传真的训练方式。]{style="font-family:宋体"}

[**[undo]{lang="FR"}**]{#struct_0_61420_36717_x1907662221}[ **fax** **train-mode**]{lang="FR"}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_61420_36717_x644933844}

[**[fax train-mode ]{lang="PT-BR"}**]{#struct_0_61420_36717_x963470061}[{ **local** \| **ppp** }]{lang="PT-BR"}

[**[undo fax train-mode]{lang="PT-BR"}**]{#struct_0_61420_36717_x55238326}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_61420_36717_731550832}

[[使用端对端训练方式。]{style="font-family:宋体"}]{#struct_0_61420_36717_122326998}

[[【视图】]{style="font-family:黑体"}]{#struct_0_61420_36717_x709079667}

[[POTS/VoIP]{lang="PT-BR"}]{#struct_0_61420_36717_x607647250}[语音实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_61420_36717_x163295367}

[[network-admin]{lang="PT-BR"}]{#struct_0_61420_36717_1759733667}

[[mdc-admin]{lang="PT-BR"}]{#struct_0_61420_36717_1751893720}

[[【参数】]{style="font-family:黑体"}]{#struct_0_61420_36717_x1966881223}

[**[local]{lang="FR"}**]{#struct_0_61420_36717_x1374552824}[：]{style="font-family:宋体"}[表示使用本地训练方式。]{style="font-family:宋体"}

[**[ppp]{lang="FR"}**]{#struct_0_61420_36717_x266971404}[：]{style="font-family:宋体"}[表示使用端对端训练方式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_61420_36717_x1539336636}

[[\# ]{lang="EN-US"}]{#struct_0_61420_36717_x1842634219}[使用本地训练方式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_61420_36717_1901510047}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 10 pots]{lang="EN-US"}

[\[Sysname-voice-dial-entity10\] ]{lang="FR"}[fax train-mode local]{lang="EN-US"}

[]{#struct_0_61420_36717_526590787}[]{#_Toc353354246}[]{#_Toc354744858}[]{#_Toc354817999}[]{#_Toc354936062}[]{#_Toc355261898}[]{#_Toc355262373}[]{#_Toc355262458}[]{#_Toc345246004}[]{#_Toc346096112}[【相关命令】]{style="font-family:黑体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fax]{lang="EN-US"}**[ **local-train** **threshold**]{lang="EN-US"}]{#struct_0_61420_36717_174223865}
:::

::: {#-226289960 .myid}
[]{#_Toc404794547}[]{#struct_0_61420_36717_x1516050188}

**Fax over IP \-- Fax over IP配置命令 \-- modem passthrough**

------------------------------------------------------------------------

[**[modem passthrough]{lang="EN-US"}**]{#struct_0_61420_36717_x2034669428}[命令用来配置]{style="font-family:宋体"}[Modem]{lang="DA"}[透传的编解码类型和切换方式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **modem passthrough**]{lang="EN-US"}]{#struct_0_61420_36717_1309758309}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_61420_36717_x310917023}

[**[modem passthrough]{lang="EN-US"}**[ { **nse** \[ **payload-type** *number* \] \| **protocol** } **codec** { **g711alaw** \| **g711ulaw** }]{lang="EN-US"}]{#struct_0_61420_36717_x1166653541}

[**[undo modem passthrough]{lang="EN-US"}**]{#struct_0_61420_36717_x671035558}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_61420_36717_1057447784}

[[不使用]{style="font-family:宋体"}]{#struct_0_61420_36717_659289176}[Modem]{lang="DA"}[透传。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_61420_36717_x2004891754}

[[POTS/VoIP]{lang="EN-US"}]{#struct_0_61420_36717_x1211155777}[语音实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_61420_36717_202524405}

[[network-admin]{lang="EN-US"}]{#struct_0_61420_36717_x1842568683}

[[mdc-admin]{lang="EN-US"}]{#struct_0_61420_36717_x340013384}

[[【参数】]{style="font-family:黑体"}]{#struct_0_61420_36717_2053151687}

[**[nse]{lang="PT-BR"}**]{#struct_0_61420_36717_x1111120996}[：]{style="font-family:宋体"}[配置使用]{style="font-family:宋体"}[NSE]{lang="PT-BR"}[方式切换到]{style="font-family:宋体"}[Modem]{lang="PT-BR"}[透传。]{style="font-family:宋体"}

[**[payload-type ]{lang="PT-BR"}**]{#struct_0_61420_36717_x1084904072}*[number]{lang="PT-BR"}*[：]{style="font-family:宋体"}[NSE]{lang="PT-BR"}[方式切换时]{style="font-family:宋体"}[NSE]{lang="PT-BR"}[报文的]{style="font-family:宋体"}[payload]{lang="PT-BR"}[值]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[98]{lang="PT-BR"}[～]{style="font-family:宋体"}[120]{lang="PT-BR"}[，缺省值为]{style="font-family:宋体"}[100]{lang="PT-BR"}[。]{style="font-family:宋体"}

[**[protocol]{lang="PT-BR"}**]{#struct_0_61420_36717_296323017}[：]{style="font-family:宋体"}[配置使用]{style="font-family:宋体"}[SIP]{lang="PT-BR"}[标准]{style="font-family:宋体"}[方式]{style="font-family:宋体"}[切换到]{style="font-family:宋体"}[Modem]{lang="PT-BR"}[透传。]{style="font-family:宋体"}

[**[codec]{lang="PT-BR"}**]{#struct_0_61420_36717_1906657028}[：]{style="font-family:宋体"}[Modem]{lang="PT-BR"}[透传使用的编解码。]{style="font-family:宋体"}

[**[g711alaw]{lang="PT-BR"}**]{#struct_0_61420_36717_135233911}[：]{style="font-family:宋体"}[Modem]{lang="PT-BR"}[透传时使用]{style="font-family:宋体"}[g711alaw]{lang="PT-BR"}[编解码。]{style="font-family:宋体"}

[**[g711ulaw]{lang="PT-BR"}**]{#struct_0_61420_36717_65492338}[：]{style="font-family:宋体"}[Modem]{lang="PT-BR"}[透传时使用]{style="font-family:宋体"}[g711]{lang="PT-BR"}[m]{lang="EN-US" style="font-family:Symbol"}[law]{lang="PT-BR"}[编解码。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_61420_36717_x541606249}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{style="font-family:宋体"}]{#struct_0_61420_36717_368137713}[Modem]{lang="PT-BR"}[透传]{style="font-family:宋体"}[时，需要保证在主被叫设备上配置相同的编解码类型和切换方式。如果]{style="font-family:宋体"}[使用]{style="font-family:宋体"}[NSE]{lang="PT-BR"}[方式切换到]{style="font-family:宋体"}[Modem]{lang="PT-BR"}[透传，]{style="font-family:宋体"}[主被叫设备上的]{style="font-family:宋体"}[payload]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}[也需要保持一致。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_61420_36717_x365376416}[NSE]{lang="PT-BR"}[方式切换到]{style="font-family:宋体"}[Modem]{lang="PT-BR"}[透传时，静音抑制检测功能和回波抵消功能会自动关闭。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_61420_36717_x468919162}

[[\# ]{lang="EN-US"}]{#struct_0_61420_36717_137949542}[配置]{style="font-family:宋体"}[Modem]{lang="DA"}[透传的切换方式为]{style="font-family:宋体"}[SIP]{lang="EN-US"}[标准]{style="font-family:宋体"}[方式，编解码类型为]{style="font-family:宋体"}[g711alaw]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_61420_36717_x1841716715}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 550 voip]{lang="EN-US"}

[\[Sysname-voice-dial-entity550\] modem passthrough protocol codec g711alaw]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_61420_36717_x88891363}[配置]{style="font-family:宋体"}[Modem]{lang="DA"}[透传的切换方式为]{style="font-family:宋体"}[NSE]{lang="PT-BR"}[方式]{style="font-family:宋体"}[，编解码类型为]{style="font-family:宋体"}[g711alaw]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_61420_36717_35049651}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 550 voip]{lang="EN-US"}

[\[Sysname-voice-dial-entity550\] modem passthrough nse codec g711alaw]{lang="EN-US"}

[ ]{lang="EN-US"}
:::
