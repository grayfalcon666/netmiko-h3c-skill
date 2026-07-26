::: {#-1515877738 .myid}
[]{#_Toc404800691}[]{#struct_0_x1662_x1996_60576933}[]{#_Toc340215442}

**诊断 \-- 诊断Probe命令 \-- display system internal kernel memory dump**

------------------------------------------------------------------------

[**[display system internal kernel memory dump]{lang="EN-US"}**]{#struct_0_x1662_x1996_x939411816}[命令用来查看指定内核内存地址的内容。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1662_x1996_1750167031}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1662_x1996_1909322933}

[**[display system internal kernel memory dump address]{lang="EN-US"}**[ *address-hex* **length** *memory-length*]{lang="EN-US"}]{#struct_0_x1662_x1996_x41927974}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1662_x1996_1863123508}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal kernel memory dump address]{lang="EN-US"}**[ *address-hex* **length** *memory-length* \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1662_x1996_x2012378705}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1662_x1996_x247192670}[模式：]{style="font-family:宋体"}

[**[display system internal kernel memory dump address]{lang="EN-US"}**[ *address-hex* **length** *memory-length* \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1662_x1996_x1994643568}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1662_x1996_x301639875}

[[Probe]{lang="EN-US"}]{#struct_0_x1662_x1996_1430784792}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1662_x1996_x966966713}

[[network-admin]{lang="EN-US"}]{#struct_0_x1662_x1996_x1923424948}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1662_x1996_x1230606160}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1662_x1996_x1030247324}

[**[address ]{lang="EN-US"}***[address-hex]{lang="EN-US"}*]{#struct_0_x1662_x1996_x2012444241}[：表示内存起始地址。]{style="font-family:宋体"}

[**[length]{lang="EN-US"}**[ *memory-length*]{lang="EN-US"}]{#struct_0_x1662_x1996_1316571456}[：表示要查看的内存大小，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1662_x1996_x756510748}[：表示单板所在的槽位号，不指定表示主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1662_x1996_x455937427}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，不指定表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1662_x1996_1524556893}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号，不指定表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1662_x1996_63619759}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号，不指定表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1662_x1996_817711629}[：]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1662_x1996_x1461211910}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#18678236 .myid}
[]{#_Toc404800692}[]{#struct_0_x1662_x1996_1197488489}[]{#_Toc340215441}[]{#_Toc360006125}[]{#_Toc360005879}[]{#_Toc360006126}[]{#_Toc360005880}[]{#_Toc360006127}[]{#_Toc360005881}[]{#_Toc360006128}[]{#_Toc360005882}[]{#_Toc360006129}[]{#_Toc360005883}[]{#_Toc360006130}[]{#_Toc360005884}[]{#_Toc360006131}[]{#_Toc360005885}[]{#_Toc360006132}[]{#_Toc360005886}[]{#_Toc360006133}[]{#_Toc360005887}[]{#_Toc360006134}[]{#_Toc360005888}[]{#_Toc360006135}[]{#_Toc360005889}[]{#_Toc360006136}[]{#_Toc360005890}[]{#_Toc360006137}[]{#_Toc360005891}[]{#_Toc350522621}[]{#_Toc350523572}[]{#_Toc350522622}[]{#_Toc350523573}[]{#_Toc350522623}[]{#_Toc350523574}[]{#_Toc350522624}[]{#_Toc350523575}[]{#_Toc350522625}[]{#_Toc350523576}[]{#_Toc350522626}[]{#_Toc350523577}[]{#_Toc350522627}[]{#_Toc350523578}[]{#_Toc350522628}[]{#_Toc350523579}[]{#_Toc350522629}[]{#_Toc350523580}[]{#_Toc350522630}[]{#_Toc350523581}[]{#_Toc350522631}[]{#_Toc350523582}[]{#_Toc350522632}[]{#_Toc350523583}[]{#_Toc350522633}[]{#_Toc350523584}[]{#_Toc350522634}[]{#_Toc350523585}[]{#_Toc350522635}[]{#_Toc350523586}[]{#_Toc350522636}[]{#_Toc350523587}[]{#_Toc350522637}[]{#_Toc350523588}[]{#_Toc350522638}[]{#_Toc350523589}[]{#_Toc350522639}[]{#_Toc350523590}[]{#_Toc350522640}[]{#_Toc350523591}[]{#_Toc350522641}[]{#_Toc350523592}[]{#_Toc350522642}[]{#_Toc350523593}[]{#_Toc350522643}[]{#_Toc350523594}[]{#_Toc350522644}[]{#_Toc350523595}

**诊断 \-- 诊断Probe命令 \-- display system internal kernel memory pool**

------------------------------------------------------------------------

[**[display system internal kernel memory pool]{lang="EN-US"}**]{#struct_0_x1662_x1996_x742280359}[命令用来显示内核态正在使用的内存池的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1662_x1996_1257509032}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1662_x1996_x734047062}

[**[display system internal kernel memory pool ]{lang="EN-US"}**[\[ **name** *name-string* \]]{lang="EN-US"}]{#struct_0_x1662_x1996_768508891}

[**[display system internal kernel memory pool tag]{lang="EN-US"}**[ \[ *tag-value* \]]{lang="EN-US"}]{#struct_0_x1662_x1996_x1344554732}

[**[display system internal kernel memory pool name]{lang="EN-US"}**[ *name-string* **tag** *tag-value*]{lang="EN-US"}]{#struct_0_x1662_x1996_1309264780}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1662_x1996_896398992}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal kernel memory pool ]{lang="EN-US"}**[\[ **name** *name-string* \] \[ **slot** *slot-number* \[**cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1662_x1996_x1529856447}

[**[display system internal kernel memory pool tag]{lang="EN-US"}**[ \[ *tag-value* \] \[ **slot** *slot-number* \[**cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1662_x1996_x1591974397}

[**[display system internal kernel memory pool name]{lang="EN-US"}**[ *name-string* **tag** *tag-value* \[ **slot** *slot-number* \[**cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1662_x1996_x2011526737}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1662_x1996_x1238236496}[模式：]{style="font-family:宋体"}

[**[display system internal kernel memory pool]{lang="EN-US"}**[ \[ **name** name-string \] \[ **chassis** *chassis-number* **slot** *slot-number* \[**cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1662_x1996_x1728260688}

[**[display system internal kernel memory pool tag ]{lang="EN-US"}**[\[ *tag-value* \] \[ **chassis** *chassis-num*ber **slot** *slot-number* \[**cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1662_x1996_1554342572}

[**[display system internal kernel memory pool name]{lang="EN-US"}**[ *name-string* **tag** *tag-value* \[ **chassis** *chassis-number* **slot** *slot-number* \[**cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1662_x1996_x2111751170}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1662_x1996_x1871059619}

[[Probe]{lang="EN-US"}]{#struct_0_x1662_x1996_1860054865}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1662_x1996_x102685122}

[[network-admin]{lang="EN-US"}]{#struct_0_x1662_x1996_x1701693271}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1662_x1996_x958841571}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1662_x1996_x445901545}

[**[name]{lang="EN-US"}**[ *name-string*]{lang="EN-US"}]{#struct_0_x1662_x1996_1078560330}[：表示内存池的名字。]{style="font-family:宋体"}

[**[tag]{lang="EN-US"}**[ *tag-value*]{lang="EN-US"}]{#struct_0_x1662_x1996_x1038666653}[：指定内存池使用者的标识。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1662_x1996_x182562502}[：表示单板所在的槽位号，不指定表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1662_x1996_x1821221995}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，不指定表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1662_x1996_1974895587}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号，不指定表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1662_x1996_x2015401332}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号，不指定表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1662_x1996_408811646}[：]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1662_x1996_x1461211897}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1662_x1996_1076594601}

[[不指定]{style="font-family:宋体"}**[name]{lang="EN-US"}**]{#struct_0_x1662_x1996_x126744880}[和]{style="font-family:宋体"}**[tag]{lang="EN-US"}**[参数时，显示系统内存池使用情况的概要信息。]{style="font-family:宋体"}

[[仅指定]{style="font-family:宋体"}**[name]{lang="EN-US"}**[ *name-string*]{lang="EN-US"}]{#struct_0_x1662_x1996_197144343}[时，显示指定内存池使用情况的概要信息；]{style="font-family:宋体"}

[[仅指定]{style="font-family:宋体"}**[tag]{lang="EN-US"}**]{#struct_0_x1662_x1996_x1355044577}[时，显示所有内存池使用情况的概要信息，以]{style="font-family:宋体"}[tag]{lang="EN-US"}[为关键字进行显示；]{style="font-family:宋体"}

[[仅指定]{style="font-family:宋体"}**[tag ]{lang="EN-US"}***[tag-value]{lang="EN-US"}*]{#struct_0_x1662_x1996_x445967081}[时，显示指定]{style="font-family:宋体"}[tag]{lang="EN-US"}[使用的内存池概要信息；]{style="font-family:宋体"}

[[指定]{style="font-family:宋体"}**[name]{lang="EN-US"}**[ *name-string* **tag** *tag-value*]{lang="EN-US"}]{#struct_0_x1662_x1996_x831272268}[时，显示指定]{style="font-family:宋体"}[tag]{lang="EN-US"}[和内存池中内存对象的使用信息。]{style="font-family:宋体"}
:::

::: {#8675279 .myid}
[]{#_Toc404800693}[]{#struct_0_x1662_x1996_714681932}[]{#_Toc340215446}[]{#_Toc360006139}[]{#_Toc360005893}[]{#_Toc360006140}[]{#_Toc360005894}[]{#_Toc360006141}[]{#_Toc360005895}[]{#_Toc360006142}[]{#_Toc360005896}[]{#_Toc360006143}[]{#_Toc360005897}[]{#_Toc360006144}[]{#_Toc360005898}[]{#_Toc360006145}[]{#_Toc360005899}[]{#_Toc360006146}[]{#_Toc360005900}[]{#_Toc360006147}[]{#_Toc360005901}[]{#_Toc360006148}[]{#_Toc360005902}[]{#_Toc360006149}[]{#_Toc360005903}[]{#_Toc360006150}[]{#_Toc360005904}[]{#_Toc360006151}[]{#_Toc360005905}[]{#_Toc360006152}[]{#_Toc360005906}[]{#_Toc360006153}[]{#_Toc360005907}[]{#_Toc360006154}[]{#_Toc360005908}[]{#_Toc360006155}[]{#_Toc360005909}[]{#_Toc360006156}[]{#_Toc360005910}[]{#_Toc360006157}[]{#_Toc360005911}[]{#_Toc360006158}[]{#_Toc360005912}[]{#_Toc360006159}[]{#_Toc360005913}[]{#_Toc360006160}[]{#_Toc360005914}[]{#_Toc360006161}[]{#_Toc360005915}[]{#_Toc360006162}[]{#_Toc360005916}[]{#_Toc360006163}[]{#_Toc360005917}[]{#_Toc360006164}[]{#_Toc360005918}[]{#_Toc360006165}[]{#_Toc360005919}[]{#_Toc360006166}[]{#_Toc360005920}[]{#_Toc360006167}[]{#_Toc360005921}[]{#_Toc360006168}[]{#_Toc360005922}[]{#_Toc360006199}[]{#_Toc360005953}[]{#_Toc360006200}[]{#_Toc360005954}[]{#_Toc360006201}[]{#_Toc360005955}[]{#_Toc360006202}[]{#_Toc360005956}[]{#_Toc360006203}[]{#_Toc360005957}[]{#_Toc360006204}[]{#_Toc360005958}[]{#_Toc360006205}[]{#_Toc360005959}[]{#_Toc360006206}[]{#_Toc360005960}[]{#_Toc360006207}[]{#_Toc360005961}[]{#_Toc360006208}[]{#_Toc360005962}[]{#_Toc360006209}[]{#_Toc360005963}[]{#_Toc360006210}[]{#_Toc360005964}[]{#_Toc360006211}[]{#_Toc360005965}[]{#_Toc360006212}[]{#_Toc360005966}[]{#_Toc360006225}[]{#_Toc360005979}[]{#_Toc360006226}[]{#_Toc360005980}[]{#_Toc360006227}[]{#_Toc360005981}[]{#_Toc360006228}[]{#_Toc360005982}[]{#_Toc360006229}[]{#_Toc360005983}[]{#_Toc360006230}[]{#_Toc360005984}[]{#_Toc360006231}[]{#_Toc360005985}[]{#_Toc360006232}[]{#_Toc360005986}[]{#_Toc360006233}[]{#_Toc360005987}[]{#_Toc360006234}[]{#_Toc360005988}[]{#_Toc360006235}[]{#_Toc360005989}[]{#_Toc360006236}[]{#_Toc360005990}[]{#_Toc360006237}[]{#_Toc360005991}[]{#_Toc360006238}[]{#_Toc360005992}[]{#_Toc360006239}[]{#_Toc360005993}[]{#_Toc360006240}[]{#_Toc360005994}[]{#_Toc360006241}[]{#_Toc360005995}[]{#_Toc360006242}[]{#_Toc360005996}[]{#_Toc360006243}[]{#_Toc360005997}[]{#_Toc360006244}[]{#_Toc360005998}[]{#_Toc360006245}[]{#_Toc360005999}[]{#_Toc360006246}[]{#_Toc360006000}[]{#_Toc360006247}[]{#_Toc360006001}[]{#_Toc360006248}[]{#_Toc360006002}[]{#_Toc360006249}[]{#_Toc360006003}[]{#_Toc360006250}[]{#_Toc360006004}[]{#_Toc360006251}[]{#_Toc360006005}[]{#_Toc360006252}[]{#_Toc360006006}[]{#_Toc360006253}[]{#_Toc360006007}[]{#_Toc360006254}[]{#_Toc360006008}[]{#_Toc360006255}[]{#_Toc360006009}[]{#_Toc360006256}[]{#_Toc360006010}[]{#_Toc360006257}[]{#_Toc360006011}[]{#_Toc360006258}[]{#_Toc360006012}[]{#_Toc360006259}[]{#_Toc360006013}[]{#_Toc360006260}[]{#_Toc360006014}[]{#_Toc360006261}[]{#_Toc360006015}[]{#_Toc360006262}[]{#_Toc360006016}[]{#_Toc360006263}[]{#_Toc360006017}[]{#_Toc360006264}[]{#_Toc360006018}[]{#_Toc360006265}[]{#_Toc360006019}[]{#_Toc360006290}[]{#_Toc360006044}[]{#_Toc360006291}[]{#_Toc360006045}[]{#_Toc360006292}[]{#_Toc360006046}[]{#_Toc360006293}[]{#_Toc360006047}[]{#_Toc360006294}[]{#_Toc360006048}[]{#_Toc360006295}[]{#_Toc360006049}[]{#_Toc360006296}[]{#_Toc360006050}[]{#_Toc360006297}[]{#_Toc360006051}[]{#_Toc360006298}[]{#_Toc360006052}[]{#_Toc360006299}[]{#_Toc360006053}[]{#_Toc360006300}[]{#_Toc360006054}[]{#_Toc360006307}[]{#_Toc360006061}[]{#_Toc350522646}[]{#_Toc350523597}[]{#_Toc350522647}[]{#_Toc350523598}[]{#_Toc350522648}[]{#_Toc350523599}[]{#_Toc350522649}[]{#_Toc350523600}[]{#_Toc350522650}[]{#_Toc350523601}[]{#_Toc350522651}[]{#_Toc350523602}[]{#_Toc350522652}[]{#_Toc350523603}[]{#_Toc350522653}[]{#_Toc350523604}[]{#_Toc350522654}[]{#_Toc350523605}[]{#_Toc350522655}[]{#_Toc350523606}[]{#_Toc350522656}[]{#_Toc350523607}[]{#_Toc350522657}[]{#_Toc350523608}[]{#_Toc350522658}[]{#_Toc350523609}[]{#_Toc350522659}[]{#_Toc350523610}[]{#_Toc350522660}[]{#_Toc350523611}[]{#_Toc350522661}[]{#_Toc350523612}[]{#_Toc350522662}[]{#_Toc350523613}[]{#_Toc350522663}[]{#_Toc350523614}[]{#_Toc350522664}[]{#_Toc350523615}[]{#_Toc350522665}[]{#_Toc350523616}[]{#_Toc350522666}[]{#_Toc350523617}[]{#_Toc350522667}[]{#_Toc350523618}[]{#_Toc350522668}[]{#_Toc350523619}[]{#_Toc350522669}[]{#_Toc350523620}[]{#_Toc350522670}[]{#_Toc350523621}[]{#_Toc350522671}[]{#_Toc350523622}[]{#_Toc350522672}[]{#_Toc350523623}[]{#_Toc350522673}[]{#_Toc350523624}[]{#_Toc350522674}[]{#_Toc350523625}[]{#_Toc350522675}[]{#_Toc350523626}

**诊断 \-- 诊断Probe命令 \-- follow**

------------------------------------------------------------------------

[**[follow]{lang="EN-US"}**]{#struct_0_x1662_x1996_989283529}[命令用来通过跟踪栈信息来调试指定的进程或者线程。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1662_x1996_x446032616}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1662_x1996_x614783181}

[**[follow]{lang="EN-US"}**[ { **job** *job-id* \| **process** *pid* } \[ **thread** *thread-id* \] \[ **delay** *seconds* \] \[ **iteration** *count* \]]{lang="EN-US"}]{#struct_0_x1662_x1996_x710839050}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1662_x1996_2032141146}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[follow]{lang="EN-US"}**[ { **job** *job-id* \| **process** *pid* } \[ **thread** *thread-id* \] \[ **delay** *seconds* \] \[ **iteration** *count* \] \[ **slot** *slot-number* \[**cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1662_x1996_344691610}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1662_x1996_x1742963061}[模式：]{style="font-family:宋体"}

[**[follow]{lang="EN-US"}**[ { **job** *job-id* \| **process** *pid* } \[ **thread** *thread-id* \] \[ **delay** *seconds* \] \[ **iteration** *count* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[**cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1662_x1996_x14339765}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1662_x1996_x667891221}

[[Probe]{lang="EN-US"}]{#struct_0_x1662_x1996_2096076388}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1662_x1996_x446098152}

[[network-admin]{lang="EN-US"}]{#struct_0_x1662_x1996_2083435837}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1662_x1996_x2010402177}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1662_x1996_x84852771}

[**[job]{lang="EN-US"}***[ job-id]{lang="EN-US"}*]{#struct_0_x1662_x1996_1217710633}[：任务]{style="font-family:宋体"}[ID]{lang="EN-US"}[，用于唯一标识一个进程，该]{style="font-family:宋体"}[ID]{lang="EN-US"}[不会随着进程的重启而改变，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[process]{lang="EN-US"}**[ *pid*]{lang="EN-US"}]{#struct_0_x1662_x1996_1054016711}[：进程]{style="font-family:宋体"}[ID]{lang="EN-US"}[，该]{style="font-family:宋体"}[ID]{lang="EN-US"}[可能会随着进程的重启而改变，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[thread ]{lang="EN-US"}***[thread-id]{lang="EN-US"}*]{#struct_0_x1662_x1996_x39949970}[：线程]{style="font-family:宋体"}[ID]{lang="EN-US"}[，用于指定进程内某一指定线程，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[delay]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}]{#struct_0_x1662_x1996_x683078478}[：指定每次跟踪操作的间隔时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[秒，缺省为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[**[iteration]{lang="EN-US"}**[ *count*]{lang="EN-US"}]{#struct_0_x1662_x1996_x1243766996}[：指定跟踪调试的次数的次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[次，缺省为]{style="font-family:宋体"}[5]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1662_x1996_x1772637243}[：表示单板所在的槽位号，不指定表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1662_x1996_2004418919}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，不指定表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1662_x1996_765107542}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号，不指定表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1662_x1996_x446163688}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号，不指定表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1662_x1996_x962542463}[：]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1662_x1996_x271733505}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1662_x1996_2124651560}

[[对于用户态进程，]{style="font-family:宋体"}**[follow]{lang="EN-US"}**]{#struct_0_x1662_x1996_1020238910}[命令会分别显示当前进程的内核态堆栈和用户态堆栈信息，并以]{style="font-family:宋体"}[user stack/kernel stack]{lang="EN-US"}[提示符加以区分；对于内核态进程，则只显示内核态堆栈信息。]{style="font-family:宋体"}

[[不指定]{style="font-family:宋体"}[thread]{lang="EN-US"}]{#struct_0_x1662_x1996_331405561}[参数时，默认显示指定进程内所有线程。]{style="font-family:宋体"}
:::

::: {#-252258674 .myid}
[]{#_Toc404800694}[]{#struct_0_x1662_x1996_1492763249}[]{#_Toc340215443}[]{#_Toc360006309}[]{#_Toc360006063}[]{#_Toc360006310}[]{#_Toc360006064}[]{#_Toc360006311}[]{#_Toc360006065}[]{#_Toc360006312}[]{#_Toc360006066}[]{#_Toc360006313}[]{#_Toc360006067}[]{#_Toc360006314}[]{#_Toc360006068}[]{#_Toc360006315}[]{#_Toc360006069}[]{#_Toc360006316}[]{#_Toc360006070}[]{#_Toc360006317}[]{#_Toc360006071}[]{#_Toc360006318}[]{#_Toc360006072}[]{#_Toc360006319}[]{#_Toc360006073}[]{#_Toc360006320}[]{#_Toc360006074}[]{#_Toc360006321}[]{#_Toc360006075}[]{#_Toc360006322}[]{#_Toc360006076}[]{#_Toc360006323}[]{#_Toc360006077}[]{#_Toc360006324}[]{#_Toc360006078}[]{#_Toc360006325}[]{#_Toc360006079}[]{#_Toc360006326}[]{#_Toc360006080}[]{#_Toc360006327}[]{#_Toc360006081}[]{#_Toc360006328}[]{#_Toc360006082}[]{#_Toc360006329}[]{#_Toc360006083}[]{#_Toc360006330}[]{#_Toc360006084}[]{#_Toc360006331}[]{#_Toc360006085}[]{#_Toc360006332}[]{#_Toc360006086}[]{#_Toc360006333}[]{#_Toc360006087}[]{#_Toc360006334}[]{#_Toc360006088}[]{#_Toc360006335}[]{#_Toc360006089}[]{#_Toc360006336}[]{#_Toc360006090}[]{#_Toc360006337}[]{#_Toc360006091}[]{#_Toc360006338}[]{#_Toc360006092}[]{#_Toc360006339}[]{#_Toc360006093}[]{#_Toc360006340}[]{#_Toc360006094}[]{#_Toc360006341}[]{#_Toc360006095}[]{#_Toc360006342}[]{#_Toc360006096}[]{#_Toc360006343}[]{#_Toc360006097}[]{#_Toc360006344}[]{#_Toc360006098}[]{#_Toc350522770}[]{#_Toc350523721}[]{#_Toc350522771}[]{#_Toc350523722}[]{#_Toc350522772}[]{#_Toc350523723}[]{#_Toc350522773}[]{#_Toc350523724}[]{#_Toc350522774}[]{#_Toc350523725}[]{#_Toc350522775}[]{#_Toc350523726}[]{#_Toc350522776}[]{#_Toc350523727}[]{#_Toc350522777}[]{#_Toc350523728}[]{#_Toc350522778}[]{#_Toc350523729}[]{#_Toc350522779}[]{#_Toc350523730}[]{#_Toc350522780}[]{#_Toc350523731}[]{#_Toc350522781}[]{#_Toc350523732}[]{#_Toc350522782}[]{#_Toc350523733}[]{#_Toc350522783}[]{#_Toc350523734}[]{#_Toc350522784}[]{#_Toc350523735}[]{#_Toc350522785}[]{#_Toc350523736}[]{#_Toc350522786}[]{#_Toc350523737}[]{#_Toc350522787}[]{#_Toc350523738}[]{#_Toc350522788}[]{#_Toc350523739}[]{#_Toc350522789}[]{#_Toc350523740}[]{#_Toc350522790}[]{#_Toc350523741}[]{#_Toc350522791}[]{#_Toc350523742}[]{#_Toc350522792}[]{#_Toc350523743}[]{#_Toc350522793}[]{#_Toc350523744}[]{#_Toc350522794}[]{#_Toc350523745}[]{#_Toc350522795}[]{#_Toc350523746}[]{#_Toc350522796}[]{#_Toc350523747}[]{#_Toc350522797}[]{#_Toc350523748}[]{#_Toc350522798}[]{#_Toc350523749}[]{#_Toc350522799}[]{#_Toc350523750}[]{#_Toc350522800}[]{#_Toc350523751}[]{#_Toc350522801}[]{#_Toc350523752}[]{#_Toc350522802}[]{#_Toc350523753}[]{#_Toc350522803}[]{#_Toc350523754}[]{#_Toc350522804}[]{#_Toc350523755}[]{#_Toc350522805}[]{#_Toc350523756}[]{#_Toc350522806}[]{#_Toc350523757}[]{#_Toc350522807}[]{#_Toc350523758}[]{#_Toc350522808}[]{#_Toc350523759}[]{#_Toc350522809}[]{#_Toc350523760}[]{#_Toc350522810}[]{#_Toc350523761}[]{#_Toc350522811}[]{#_Toc350523762}[]{#_Toc350522812}[]{#_Toc350523763}[]{#_Toc350522813}[]{#_Toc350523764}[]{#_Toc350522814}[]{#_Toc350523765}[]{#_Toc350522815}[]{#_Toc350523766}[]{#_Toc350522816}[]{#_Toc350523767}[]{#_Toc350522817}[]{#_Toc350523768}[]{#_Toc350522818}[]{#_Toc350523769}[]{#_Toc350522819}[]{#_Toc350523770}[]{#_Toc350522820}[]{#_Toc350523771}[]{#_Toc350522821}[]{#_Toc350523772}[]{#_Toc350522822}[]{#_Toc350523773}[]{#_Toc350522823}[]{#_Toc350523774}[]{#_Toc350522824}[]{#_Toc350523775}[]{#_Toc350522825}[]{#_Toc350523776}[]{#_Toc350522826}[]{#_Toc350523777}[]{#_Toc350522827}[]{#_Toc350523778}[]{#_Toc350522828}[]{#_Toc350523779}[]{#_Toc350522829}[]{#_Toc350523780}[]{#_Toc350522830}[]{#_Toc350523781}[]{#_Toc350522831}[]{#_Toc350523782}[]{#_Toc350522832}[]{#_Toc350523783}[]{#_Toc350522833}[]{#_Toc350523784}[]{#_Toc350522834}[]{#_Toc350523785}[]{#_Toc350522835}[]{#_Toc350523786}[]{#_Toc350522836}[]{#_Toc350523787}[]{#_Toc350522837}[]{#_Toc350523788}[]{#_Toc350522838}[]{#_Toc350523789}[]{#_Toc350522839}[]{#_Toc350523790}[]{#_Toc350522840}[]{#_Toc350523791}[]{#_Toc350522841}[]{#_Toc350523792}[]{#_Toc350522842}[]{#_Toc350523793}[]{#_Toc350522843}[]{#_Toc350523794}[]{#_Toc350522844}[]{#_Toc350523795}[]{#_Toc350522845}[]{#_Toc350523796}[]{#_Toc350522846}[]{#_Toc350523797}[]{#_Toc350522847}[]{#_Toc350523798}[]{#_Toc350522848}[]{#_Toc350523799}[]{#_Toc350522849}[]{#_Toc350523800}[]{#_Toc350522850}[]{#_Toc350523801}[]{#_Toc350522851}[]{#_Toc350523802}[]{#_Toc350522852}[]{#_Toc350523803}[]{#_Toc350522853}[]{#_Toc350523804}[]{#_Toc350522854}[]{#_Toc350523805}[]{#_Toc350522855}[]{#_Toc350523806}[]{#_Toc350522856}[]{#_Toc350523807}[]{#_Toc350522857}[]{#_Toc350523808}[]{#_Toc350522859}[]{#_Toc350523810}[]{#_Toc350522860}[]{#_Toc350523811}[]{#_Toc350522861}[]{#_Toc350523812}[]{#_Toc350522862}[]{#_Toc350523813}[]{#_Toc350522863}[]{#_Toc350523814}[]{#_Toc350522864}[]{#_Toc350523815}[]{#_Toc350522865}[]{#_Toc350523816}[]{#_Toc350522866}[]{#_Toc350523817}[]{#_Toc350522867}[]{#_Toc350523818}[]{#_Toc350522868}[]{#_Toc350523819}[]{#_Toc350522869}[]{#_Toc350523820}[]{#_Toc350522870}[]{#_Toc350523821}[]{#_Toc350522871}[]{#_Toc350523822}[]{#_Toc350522872}[]{#_Toc350523823}[]{#_Toc350522873}[]{#_Toc350523824}[]{#_Toc350522874}[]{#_Toc350523825}[]{#_Toc350522875}[]{#_Toc350523826}[]{#_Toc350522876}[]{#_Toc350523827}[]{#_Toc350522877}[]{#_Toc350523828}[]{#_Toc350522878}[]{#_Toc350523829}[]{#_Toc350522879}[]{#_Toc350523830}[]{#_Toc350522880}[]{#_Toc350523831}[]{#_Toc350522881}[]{#_Toc350523832}[]{#_Toc350522882}[]{#_Toc350523833}[]{#_Toc350522883}[]{#_Toc350523834}[]{#_Toc282090086}[]{#_Toc282090088}[]{#_Toc282090089}[]{#_Toc350522884}[]{#_Toc350523835}[]{#_Toc350522885}[]{#_Toc350523836}[]{#_Toc350522887}[]{#_Toc350523838}[]{#_Toc350522888}[]{#_Toc350523839}[]{#_Toc350522889}[]{#_Toc350523840}[]{#_Toc350522890}[]{#_Toc350523841}[]{#_Toc350522891}[]{#_Toc350523842}[]{#_Toc350522892}[]{#_Toc350523843}[]{#_Toc350522893}[]{#_Toc350523844}[]{#_Toc350522894}[]{#_Toc350523845}[]{#_Toc350522895}[]{#_Toc350523846}[]{#_Toc350522896}[]{#_Toc350523847}[]{#_Toc350522897}[]{#_Toc350523848}[]{#_Toc350522898}[]{#_Toc350523849}[]{#_Toc350522899}[]{#_Toc350523850}[]{#_Toc350522900}[]{#_Toc350523851}[]{#_Toc350522901}[]{#_Toc350523852}[]{#_Toc350522902}[]{#_Toc350523853}[]{#_Toc350522903}[]{#_Toc350523854}[]{#_Toc350522904}[]{#_Toc350523855}[]{#_Toc350522905}[]{#_Toc350523856}[]{#_Toc350522906}[]{#_Toc350523857}[]{#_Toc350522907}[]{#_Toc350523858}[]{#_Toc350522908}[]{#_Toc350523859}[]{#_Toc350522909}[]{#_Toc350523860}[]{#_Toc350522911}[]{#_Toc350523862}[]{#_Toc350522912}[]{#_Toc350523863}[]{#_Toc350522913}[]{#_Toc350523864}[]{#_Toc350522914}[]{#_Toc350523865}[]{#_Toc350522915}[]{#_Toc350523866}[]{#_Toc350522916}[]{#_Toc350523867}[]{#_Toc350522917}[]{#_Toc350523868}[]{#_Toc350522918}[]{#_Toc350523869}[]{#_Toc350522919}[]{#_Toc350523870}[]{#_Toc350522920}[]{#_Toc350523871}[]{#_Toc350522921}[]{#_Toc350523872}[]{#_Toc350522922}[]{#_Toc350523873}[]{#_Toc350522923}[]{#_Toc350523874}[]{#_Toc350522924}[]{#_Toc350523875}[]{#_Toc350522925}[]{#_Toc350523876}[]{#_Toc350522926}[]{#_Toc350523877}[]{#_Toc350522927}[]{#_Toc350523878}[]{#_Toc350522928}[]{#_Toc350523879}[]{#_Toc350522929}[]{#_Toc350523880}[]{#_Toc350522930}[]{#_Toc350523881}[]{#_Toc350522931}[]{#_Toc350523882}[]{#_Toc350522932}[]{#_Toc350523883}[]{#_Toc350522933}[]{#_Toc350523884}[]{#_Toc350522934}[]{#_Toc350523885}[]{#_Toc350522935}[]{#_Toc350523886}[]{#_Toc350522936}[]{#_Toc350523887}[]{#_Toc350522937}[]{#_Toc350523888}[]{#_Toc343779362}[]{#_Toc350522939}[]{#_Toc350523890}[]{#_Toc350522940}[]{#_Toc350523891}[]{#_Toc350522941}[]{#_Toc350523892}[]{#_Toc350522942}[]{#_Toc350523893}[]{#_Toc350522943}[]{#_Toc350523894}[]{#_Toc350522944}[]{#_Toc350523895}[]{#_Toc350522945}[]{#_Toc350523896}[]{#_Toc350522946}[]{#_Toc350523897}[]{#_Toc350522947}[]{#_Toc350523898}[]{#_Toc350522948}[]{#_Toc350523899}[]{#_Toc350522949}[]{#_Toc350523900}[]{#_Toc350522950}[]{#_Toc350523901}[]{#_Toc350522951}[]{#_Toc350523902}[]{#_Toc350522952}[]{#_Toc350523903}[]{#_Toc350522953}[]{#_Toc350523904}[]{#_Toc350522954}[]{#_Toc350523905}[]{#_Toc350522955}[]{#_Toc350523906}[]{#_Toc350522956}[]{#_Toc350523907}[]{#_Toc350522957}[]{#_Toc350523908}[]{#_Toc350522958}[]{#_Toc350523909}[]{#_Toc350522960}[]{#_Toc350523911}[]{#_Toc350522961}[]{#_Toc350523912}[]{#_Toc350522962}[]{#_Toc350523913}[]{#_Toc350522963}[]{#_Toc350523914}[]{#_Toc350522964}[]{#_Toc350523915}[]{#_Toc350522965}[]{#_Toc350523916}[]{#_Toc350522966}[]{#_Toc350523917}[]{#_Toc350522967}[]{#_Toc350523918}[]{#_Toc350522968}[]{#_Toc350523919}[]{#_Toc350522969}[]{#_Toc350523920}[]{#_Toc350522970}[]{#_Toc350523921}[]{#_Toc350522971}[]{#_Toc350523922}[]{#_Toc350522972}[]{#_Toc350523923}[]{#_Toc350522973}[]{#_Toc350523924}[]{#_Toc350522974}[]{#_Toc350523925}[]{#_Toc350522975}[]{#_Toc350523926}[]{#_Toc350522976}[]{#_Toc350523927}[]{#_Toc350522977}[]{#_Toc350523928}[]{#_Toc350522978}[]{#_Toc350523929}[]{#_Toc350522979}[]{#_Toc350523930}[]{#_Toc343779365}[]{#_Toc350522981}[]{#_Toc350523932}[]{#_Toc350522982}[]{#_Toc350523933}[]{#_Toc350522983}[]{#_Toc350523934}[]{#_Toc350522984}[]{#_Toc350523935}[]{#_Toc350522985}[]{#_Toc350523936}[]{#_Toc350522986}[]{#_Toc350523937}[]{#_Toc350522987}[]{#_Toc350523938}[]{#_Toc350522988}[]{#_Toc350523939}[]{#_Toc350522989}[]{#_Toc350523940}[]{#_Toc350522990}[]{#_Toc350523941}[]{#_Toc350522991}[]{#_Toc350523942}[]{#_Toc350522992}[]{#_Toc350523943}[]{#_Toc350522993}[]{#_Toc350523944}[]{#_Toc350522994}[]{#_Toc350523945}[]{#_Toc350522995}[]{#_Toc350523946}[]{#_Toc350522996}[]{#_Toc350523947}[]{#_Toc350522997}[]{#_Toc350523948}[]{#_Toc350522998}[]{#_Toc350523949}[]{#_Toc350522999}[]{#_Toc350523950}[]{#_Toc343779367}[]{#_Toc360006363}[]{#_Toc360006117}[]{#_Toc350522677}[]{#_Toc350523628}[]{#_Toc350522678}[]{#_Toc350523629}[]{#_Toc350522679}[]{#_Toc350523630}[]{#_Toc350522680}[]{#_Toc350523631}[]{#_Toc350522681}[]{#_Toc350523632}[]{#_Toc350522682}[]{#_Toc350523633}[]{#_Toc350522683}[]{#_Toc350523634}[]{#_Toc350522684}[]{#_Toc350523635}[]{#_Toc350522685}[]{#_Toc350523636}[]{#_Toc350522686}[]{#_Toc350523637}[]{#_Toc350522687}[]{#_Toc350523638}[]{#_Toc350522688}[]{#_Toc350523639}[]{#_Toc350522689}[]{#_Toc350523640}[]{#_Toc350522690}[]{#_Toc350523641}[]{#_Toc350522691}[]{#_Toc350523642}[]{#_Toc350522692}[]{#_Toc350523643}[]{#_Toc350522693}[]{#_Toc350523644}[]{#_Toc350522694}[]{#_Toc350523645}[]{#_Toc350522695}[]{#_Toc350523646}

**诊断 \-- 诊断Probe命令 \-- memory boundary-check enable**

------------------------------------------------------------------------

[**[memory boundary-check enable]{lang="EN-US"}**]{#struct_0_x1662_x1996_x210568577}[命令用来开启内存越界检查功能。]{style="font-family:
宋体"}

[**[undo memory boundary-check enable]{lang="EN-US"}**]{#struct_0_x1662_x1996_x1753778343}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1662_x1996_x104952263}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1662_x1996_x1779758965}

[**[memory boundary-check]{lang="EN-US"}***[ ]{lang="EN-US"}***[enable job ]{lang="EN-US"}***[job-id]{lang="EN-US"}*]{#struct_0_x1662_x1996_1770207921}

[**[undo memory boundary-check enable job ]{lang="EN-US"}***[job-id]{lang="EN-US"}*]{#struct_0_x1662_x1996_x445377256}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1662_x1996_x450770453}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[memory boundary-check enable job ]{lang="EN-US"}***[job-id]{lang="EN-US"}*[ \[ **slot** *slot-number* \[**cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1662_x1996_x854068567}

[**[undo memory boundary-check]{lang="EN-US"}**[ **enable** **job** *job-id* \[ **slot** *slot-number* \[**cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1662_x1996_378377851}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1662_x1996_474073657}[模式：]{style="font-family:宋体"}

[**[memory boundary-check]{lang="EN-US"}**[ **enable job** *job-id* \[ **chassis** *chassis-number* **slot** *slot-number* \[**cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1662_x1996_622818200}

[**[undo memory boundary-check]{lang="EN-US"}**[ **enable job** *job-id* \[ **chassis** *chassis-number* **slot** *slot-number* \[**cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1662_x1996_1573257008}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1662_x1996_1229356111}

[[内存越界检查功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x1662_x1996_x445442792}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1662_x1996_1873029151}

[[Probe]{lang="EN-US"}]{#struct_0_x1662_x1996_325589911}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1662_x1996_936069987}

[[network-admin]{lang="EN-US"}]{#struct_0_x1662_x1996_x924237586}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1662_x1996_374377491}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1662_x1996_1681746185}

[**[job ]{lang="EN-US"}***[job-id]{lang="EN-US"}*]{#struct_0_x1662_x1996_1197563982}[：任务]{style="font-family:宋体"}[ID]{lang="EN-US"}[，用于唯一标识一个进程，该]{style="font-family:宋体"}[ID]{lang="EN-US"}[不会随着进程的重启而改变，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1662_x1996_x14878143}[：表示单板所在的槽位号，不指定表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1662_x1996_2025293327}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，不指定表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1662_x1996_361823015}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号，不指定表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1662_x1996_x445901547}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号，不指定表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1662_x1996_x221250467}[：]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1662_x1996_x271733504}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1662_x1996_1078429258}

[[开启指定进程的内存越界检查功能后，该进程每次释放内存前都会进行内存越界检查，以便确保申请和释放操作的正确性。如果发生内存越界，将内存越界信息记录到内存文件中（所有进程的越界信息都会记录到一个文件中）。]{style="font-family:宋体"}]{#struct_0_x1662_x1996_2135628555}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1662_x1996_x1979024464}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[memory boundary-check scan]{lang="EN-US"}**]{#struct_0_x1662_x1996_134002800}
:::

::: {#-1588135916 .myid}
[]{#_Toc404800695}[]{#struct_0_x1662_x1996_x1113855826}[]{#_Toc350522697}[]{#_Toc350523648}[]{#_Toc350522698}[]{#_Toc350523649}[]{#_Toc350522699}[]{#_Toc350523650}[]{#_Toc350522700}[]{#_Toc350523651}[]{#_Toc350522701}[]{#_Toc350523652}[]{#_Toc350522702}[]{#_Toc350523653}[]{#_Toc350522703}[]{#_Toc350523654}[]{#_Toc350522704}[]{#_Toc350523655}[]{#_Toc350522705}[]{#_Toc350523656}[]{#_Toc350522706}[]{#_Toc350523657}[]{#_Toc350522707}[]{#_Toc350523658}[]{#_Toc350522708}[]{#_Toc350523659}[]{#_Toc350522709}[]{#_Toc350523660}[]{#_Toc350522710}[]{#_Toc350523661}[]{#_Toc350522711}[]{#_Toc350523662}[]{#_Toc350522712}[]{#_Toc350523663}[]{#_Toc350522713}[]{#_Toc350523664}[]{#_Toc350522714}[]{#_Toc350523665}[]{#_Toc350522716}[]{#_Toc350523667}[]{#_Toc350522717}[]{#_Toc350523668}[]{#_Toc350522718}[]{#_Toc350523669}[]{#_Toc350522719}[]{#_Toc350523670}[]{#_Toc350522720}[]{#_Toc350523671}[]{#_Toc350522721}[]{#_Toc350523672}[]{#_Toc350522722}[]{#_Toc350523673}[]{#_Toc350522723}[]{#_Toc350523674}[]{#_Toc350522724}[]{#_Toc350523675}[]{#_Toc350522725}[]{#_Toc350523676}[]{#_Toc350522726}[]{#_Toc350523677}[]{#_Toc350522727}[]{#_Toc350523678}[]{#_Toc350522728}[]{#_Toc350523679}[]{#_Toc350522729}[]{#_Toc350523680}[]{#_Toc350522730}[]{#_Toc350523681}[]{#_Toc350522731}[]{#_Toc350523682}[]{#_Toc350522733}[]{#_Toc350523684}[]{#_Toc350522734}[]{#_Toc350523685}[]{#_Toc350522735}[]{#_Toc350523686}[]{#_Toc350522736}[]{#_Toc350523687}[]{#_Toc350522737}[]{#_Toc350523688}[]{#_Toc350522738}[]{#_Toc350523689}[]{#_Toc350522739}[]{#_Toc350523690}[]{#_Toc350522740}[]{#_Toc350523691}[]{#_Toc350522741}[]{#_Toc350523692}[]{#_Toc350522742}[]{#_Toc350523693}[]{#_Toc350522743}[]{#_Toc350523694}[]{#_Toc350522744}[]{#_Toc350523695}[]{#_Toc350522745}[]{#_Toc350523696}[]{#_Toc350522746}[]{#_Toc350523697}[]{#_Toc350522747}[]{#_Toc350523698}[]{#_Toc350522748}[]{#_Toc350523699}[]{#_Toc350522749}[]{#_Toc350523700}[]{#_Toc350522751}[]{#_Toc350523702}[]{#_Toc350522752}[]{#_Toc350523703}[]{#_Toc350522753}[]{#_Toc350523704}[]{#_Toc350522754}[]{#_Toc350523705}[]{#_Toc350522755}[]{#_Toc350523706}[]{#_Toc350522756}[]{#_Toc350523707}[]{#_Toc350522757}[]{#_Toc350523708}[]{#_Toc350522758}[]{#_Toc350523709}[]{#_Toc350522759}[]{#_Toc350523710}[]{#_Toc350522760}[]{#_Toc350523711}[]{#_Toc350522761}[]{#_Toc350523712}[]{#_Toc350522762}[]{#_Toc350523713}[]{#_Toc350522763}[]{#_Toc350523714}[]{#_Toc350522764}[]{#_Toc350523715}[]{#_Toc350522765}[]{#_Toc350523716}[]{#_Toc350522766}[]{#_Toc350523717}[]{#_Toc350522767}[]{#_Toc350523718}[]{#_Toc350522768}[]{#_Toc350523719}

**诊断 \-- 诊断Probe命令 \-- memory boundary-check scan**

------------------------------------------------------------------------

[**[memory boundary-check scan]{lang="EN-US"}**]{#struct_0_x1662_x1996_2074321192}[命令用来触发一次内存越界检查，并显示检查的结果。若有内存被写越界，则打印出该出错处地址往前偏移]{style="font-family:
宋体"}[16]{lang="EN-US"}[字节，一共]{style="font-family:宋体"}[128]{lang="EN-US"}[字节的内存内容。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1662_x1996_x445967083}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1662_x1996_x831141196}

[**[memory boundary-check scan job ]{lang="EN-US"}***[job-id]{lang="EN-US"}*]{#struct_0_x1662_x1996_976121198}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1662_x1996_1904141880}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[memory boundary-check scan]{lang="EN-US"}**[ **job** *job-id* \[ **slot** *slot-number* \[**cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1662_x1996_1468766302}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1662_x1996_877727501}[模式：]{style="font-family:宋体"}

[**[memory boundary-check scan]{lang="EN-US"}**[ **job** *job-id* \[ **chassis** *chassis-number* **slot** *slot-number* \[**cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1662_x1996_439332001}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1662_x1996_x290438262}

[[Probe]{lang="EN-US"}]{#struct_0_x1662_x1996_x1861123757}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1662_x1996_x1396306755}

[[network-admin]{lang="EN-US"}]{#struct_0_x1662_x1996_x446032619}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1662_x1996_x613800141}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1662_x1996_x956640484}

[**[job ]{lang="EN-US"}***[job-id]{lang="EN-US"}*]{#struct_0_x1662_x1996_2040722131}[：任务]{style="font-family:宋体"}[ID]{lang="EN-US"}[，用于唯一标识一个进程，该]{style="font-family:宋体"}[ID]{lang="EN-US"}[不会随着进程的重启而改变，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1662_x1996_61361665}[：表示单板所在的槽位号，不指定表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1662_x1996_x1483859134}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，不指定表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1662_x1996_1524622429}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号，不指定表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1662_x1996_1188034562}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号，不指定表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1662_x1996_1143872721}[：]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1662_x1996_x271733510}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1662_x1996_x1492104732}

[[使用前必须使能内存越界检测功能，否则使用该命令检查，无效果。]{style="font-family:宋体"}]{#struct_0_x1662_x1996_x1037785972}

[[执行该命令后，系统会从出错处地址往前偏移]{style="font-family:宋体"}[16]{lang="EN-US"}]{#struct_0_x1662_x1996_x446098155}[字节，一共显示]{style="font-family:宋体"}[128]{lang="EN-US"}[字节的内存内容；当系统中存在多处内存越界时，只记录并显示地址最小的一条检查结果。]{style="font-family:宋体"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1662_x1996_x1859654313}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[memory boundary-check enable]{lang="EN-US"}**]{#struct_0_x1662_x1996_491561520}
:::
