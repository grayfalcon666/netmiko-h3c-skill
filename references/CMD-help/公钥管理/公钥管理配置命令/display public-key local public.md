::: {#311746211 .myid}
[]{#_Toc404792928}[]{#struct_0_x1871_x1914_x171083972}[]{#_Toc195409915}[]{#_Toc149979593}[]{#_Toc144810329}[]{#_Toc144782890}

**公钥管理 \-- 公钥管理配置命令 \-- display public-key local public**

------------------------------------------------------------------------

[**[display public-key local public]{lang="EN-US"}**]{#struct_0_x1871_x1914_x670796237}[命令用来显示本地非对称密钥对中的公钥信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_x1723154880}

[**[display public-key local ]{lang="EN-US"}**[{ **dsa** \| **ecdsa** \| **rsa** } **public** \[ **name** *key-name* \]]{lang="EN-US"}]{#struct_0_x1871_x1914_721555880}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_752586708}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1871_x1914_206199158}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_x1001145707}

[[network-admin]{lang="EN-US"}]{#struct_0_x1871_x1914_209192190}

[[network-operator]{lang="EN-US"}]{#struct_0_x1871_x1914_1787352648}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1871_x1914_634883682}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1871_x1914_x2029884487}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_x274366213}

[**[dsa]{lang="EN-US"}**]{#struct_0_x1871_x1914_x889078335}[：显示本地]{style="font-family:宋体"}[DSA]{lang="EN-US"}[密钥对中的公钥信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ecdsa]{lang="EN-US"}**]{#struct_0_x1871_x1914_x1922588881}[：显示本地]{style="font-family:宋体"}[ECDSA]{lang="EN-US"}[密钥对中的公钥信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[rsa]{lang="EN-US"}**]{#struct_0_x1871_x1914_206133622}[：显示本地]{style="font-family:宋体"}[RSA]{lang="EN-US"}[密钥对中的公钥信息。]{style="font-family:宋体"}

[**[name ]{lang="EN-US"}***[key-name]{lang="EN-US"}*]{#struct_0_x1871_x1914_x1037958580}[：显示指定的本地非对称密钥对的公钥信息。]{style="font-family:宋体"}*[key-name]{lang="EN-US"}*[为本地非对称密钥对的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，不区分大小写，字符串中可以包含字母、数字及"]{style="font-family:宋体"}[-]{lang="EN-US"}["。如果不指定本参数，则显示指定类型的所有本地非对称密钥对的公钥信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_x1134695078}

[[如果通过手工配置方式将本地的主机公钥保存到远端设备上，则需要事先在本地设备上执行本命令显示主机公钥信息，并记录该信息。]{style="font-family:宋体"}]{#struct_0_x1871_x1914_1149264115}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_492269995}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_x656590573}[显示所有本地]{style="font-family:宋体"}[RSA]{lang="EN-US"}[密钥对中的公钥信息。]{style="font-family:宋体"}

[[\<Sysname\> display public-key local rsa public]{lang="EN-US"}]{#struct_0_x1871_x1914_206068086}

[ ]{lang="EN-US"}

[=============================================]{lang="EN-US"}

[Key name: hostkey (default)]{lang="EN-US"}

[Key type: RSA]{lang="EN-US"}

[Time when key pair created: 15:40:48 2011/05/12]{lang="EN-US"}

[Key code:]{lang="EN-US"}

[   30819F300D06092A864886F70D010101050003818D0030818902818100DAA4AAFEFE04C2C9]{lang="EN-US"}

[   667269BB8226E26331E30F41A8FF922C7338208097E84332610632B49F75DABF6D871B80CE]{lang="EN-US"}

[   C1BA2B75020077C74745C933E2F390DC0B39D35B88283D700A163BB309B19F8F87216A44AB]{lang="EN-US"}

[   FBF6A3D64DEB33E5CEBF2BCF26296778A26A84F4F4C5DBF8B656ACFA62CD96863474899BC1]{lang="EN-US"}

[   2DA4C04EF5AE0835090203010001]{lang="EN-US"}

[=============================================]{lang="EN-US"}

[Key name: serverkey (default)]{lang="EN-US"}

[Key type: RSA]{lang="EN-US"}

[Time when key pair created: 15:40:48 2011/05/12]{lang="EN-US"}

[Key code:]{lang="IT"}

[   307C300D06092A864886F70D0101010500036B003068026100CAB4CACCA16442AD5F453442]{lang="IT"}

[   762F03897E0D494FEDE69224F5C051A441D290976733A278C9F0C0F5A198E66143EAB54A64]{lang="IT"}

[   DB608269CAE844B1E7CC64AD7E808972E7CF887F3B657F056E7930FC84FBF1AD83A01CC47E]{lang="IT"}

[   9D85C13413996ECD093B0203010001]{lang="IT"}

[=============================================]{lang="EN-US"}

[Key name: rsa1]{lang="EN-US"}

[Key type: RSA]{lang="EN-US"}

[Time when key pair created: 15:42:26 2011/05/12]{lang="EN-US"}

[Key code:]{lang="EN-US"}

[   30819F300D06092A864886F70D010101050003818D0030818902818100DEBC46F217DDF11D]{lang="EN-US"}

[   426E7095AA45CD6BF1F87343D952569AC223A01365E0D8C91D49D347C143C5D8FAADA896AA]{lang="EN-US"}

[   1A827E580F2502F1926F52197230E1DE391A64015C43DD79DC4E9E171BAEA1DEB4C71DAED7]{lang="EN-US"}

[   9A6EDFD460D8945D27D39B7C9822D56AEA5B7C2CCFF1B6BC524AD498C3B87D4BD6EB36AF03]{lang="EN-US"}

[   92D8C6D940890BF4290203010001]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_1352746895}[显示所有本地]{style="font-family:宋体"}[DSA]{lang="EN-US"}[密钥对中的公钥信息。]{style="font-family:宋体"}

[[\<Sysname\> display public-key local dsa public]{lang="EN-US"}]{#struct_0_x1871_x1914_206461302}

[ ]{lang="EN-US"}

[=============================================]{lang="EN-US"}

[Key name: dsakey (default)]{lang="EN-US"}

[Key type: DSA]{lang="EN-US"}

[Time when key pair created: 15:41:37 2011/05/12]{lang="EN-US"}

[Key code:]{lang="EN-US"}

[   308201B73082012C06072A8648CE3804013082011F02818100D757262C4584C44C211F18BD]{lang="EN-US"}

[   96E5F061C4F0A423F7FE6B6B85B34CEF72CE14A0D3A5222FE08CECE65BE6C265854889DC1E]{lang="EN-US"}

[   DBD13EC8B274DA9F75BA26CCB987723602787E922BA84421F22C3C89CB9B06FD60FE01941D]{lang="EN-US"}

[   DD77FE6B12893DA76EEBC1D128D97F0678D7722B5341C8506F358214B16A2FAC4B36895038]{lang="EN-US"}

[   7811C7DA33021500C773218C737EC8EE993B4F2DED30F48EDACE915F0281810082269009E1]{lang="EN-US"}

[   4EC474BAF2932E69D3B1F18517AD9594184CCDFCEAE96EC4D5EF93133E84B47093C52B20CD]{lang="EN-US"}

[   35D02492B3959EC6499625BC4FA5082E22C5B374E16DD00132CE71B020217091AC717B6123]{lang="EN-US"}

[   91C76C1FB2E88317C1BD8171D41ECB83E210C03CC9B32E810561C21621C73D6DAAC028F4B1]{lang="EN-US"}

[   585DA7F42519718CC9B09EEF0381840002818041912CE34D12BCD2157E7AB1C2F03B3EF395]{lang="EN-US"}

[   100F3DB4A9E2FDFE860C1BD663D676438F7DA40A9406D61CA9079AF13E330489F1C76785DE]{lang="EN-US"}

[   52DA649AC8BC04B6D39CD7C52CD0A14F75F7491A91D31D6AC22340B5981B27A915CDEC4F09]{lang="EN-US"}

[   887E541EC1E5302D500F68E7AC29A084463C60F9EE266985A502FC92193E1CF4D265C4BA]{lang="EN-US"}

[=============================================]{lang="EN-US"}

[Key name: dsa1]{lang="EN-US"}

[Key type: DSA]{lang="EN-US"}

[Time when key pair created: 15:35:42 2011/05/12]{lang="EN-US"}

[Key code:]{lang="EN-US"}

[   308201B83082012C06072A8648CE3804013082011F02818100D757262C4584C44C211F18BD]{lang="EN-US"}

[   96E5F061C4F0A423F7FE6B6B85B34CEF72CE14A0D3A5222FE08CECE65BE6C265854889DC1E]{lang="EN-US"}

[   DBD13EC8B274DA9F75BA26CCB987723602787E922BA84421F22C3C89CB9B06FD60FE01941D]{lang="EN-US"}

[   DD77FE6B12893DA76EEBC1D128D97F0678D7722B5341C8506F358214B16A2FAC4B36895038]{lang="EN-US"}

[   7811C7DA33021500C773218C737EC8EE993B4F2DED30F48EDACE915F0281810082269009E1]{lang="EN-US"}

[   4EC474BAF2932E69D3B1F18517AD9594184CCDFCEAE96EC4D5EF93133E84B47093C52B20CD]{lang="EN-US"}

[   35D02492B3959EC6499625BC4FA5082E22C5B374E16DD00132CE71B020217091AC717B6123]{lang="EN-US"}

[   91C76C1FB2E88317C1BD8171D41ECB83E210C03CC9B32E810561C21621C73D6DAAC028F4B1]{lang="EN-US"}

[   585DA7F42519718CC9B09EEF0381850002818100A1E456C8DA2AD1BB83B1BDF2A1A6B5A6E8]{lang="EN-US"}

[   3642B460402445DA7E4036715F468F76655E114D460B7112F57143EE020AEF4A5BFAD07B74]{lang="EN-US"}

[   0FBCB1C64DA8A2BCE619283421445EEC77D3CF0D11866E9656AD6511F4926F8376967B0AB7]{lang="EN-US"}

[   15F9FB7B514BC1174155DD6E073B1FCB3A2749E6C5FEA81003E16729497D0EAD9105E3E76A]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_x1261132452}[显示所有本地]{style="font-family:宋体"}[ECDSA]{lang="EN-US"}[密钥对中的公钥信息。]{style="font-family:宋体"}

[[\<Sysname\> display public-key local ecdsa public]{lang="EN-US"}]{#struct_0_x1871_x1914_206395766}

[ ]{lang="EN-US"}

[=============================================]{lang="EN-US"}

[Key name: ecdsakey (default)]{lang="EN-US"}

[Key type: ECDSA]{lang="EN-US"}

[Time when key pair created: 15:42:04 2011/05/12]{lang="EN-US"}

[Key code:]{lang="EN-US"}

[   3049301306072A8648CE3D020106082A8648CE3D03010103320004C10CF7CE42193F7FC2AF]{lang="EN-US"}

[   68F5DC877835A43009DB6135558A7FB8316C361B0690B4FD84A14C0779C76DD6145BF9362B]{lang="EN-US"}

[   1D]{lang="EN-US"}

[=============================================]{lang="EN-US"}

[Key name: ecdsa1]{lang="EN-US"}

[Key type: ECDSA]{lang="EN-US"}

[Time when key pair created: 15:43:33 2011/05/12]{lang="EN-US"}

[Key code:]{lang="EN-US"}

[   3049301306072A8648CE3D020106082A8648CE3D03010103320004A1FB84D92315B8DB72D1]{lang="EN-US"}

[   AE672C7CFA5135D5F5B02377F2F092F182EC83B5819795BC94CCBD3EBA7D4F0F2B2EB20C58]{lang="EN-US"}

[   4D]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_1954379321}[显示名称为]{style="font-family:宋体"}[rsa1]{lang="EN-US"}[的本地]{style="font-family:宋体"}[RSA]{lang="EN-US"}[密钥对中的公钥信息。]{style="font-family:宋体"}

[[\<Sysname\> display public-key local rsa public name rsa1]{lang="EN-US"}]{#struct_0_x1871_x1914_598496627}

[ ]{lang="EN-US"}

[=============================================]{lang="EN-US"}

[Key name: rsa1]{lang="EN-US"}

[Key type: RSA]{lang="EN-US"}

[Time when key pair created: 15:42:26 2011/05/12]{lang="EN-US"}

[Key code:]{lang="EN-US"}

[   30819F300D06092A864886F70D010101050003818D0030818902818100DEBC46F217DDF11D]{lang="EN-US"}

[   426E7095AA45CD6BF1F87343D952569AC223A01365E0D8C91D49D347C143C5D8FAADA896AA]{lang="EN-US"}

[   1A827E580F2502F1926F52197230E1DE391A64015C43DD79DC4E9E171BAEA1DEB4C71DAED7]{lang="EN-US"}

[   9A6EDFD460D8945D27D39B7C9822D56AEA5B7C2CCFF1B6BC524AD498C3B87D4BD6EB36AF03]{lang="EN-US"}

[   92D8C6D940890BF4290203010001]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_x685683048}[显示名称为]{style="font-family:宋体"}[dsa1]{lang="EN-US"}[的本地]{style="font-family:宋体"}[DSA]{lang="EN-US"}[密钥对中的公钥信息。]{style="font-family:宋体"}

[[\<Sysname\> display public-key local dsa public name dsa1]{lang="EN-US"}]{#struct_0_x1871_x1914_206330230}

[ ]{lang="EN-US"}

[=============================================]{lang="EN-US"}

[Key name: dsa1]{lang="EN-US"}

[Key type: DSA]{lang="EN-US"}

[Time when key pair created: 15:35:42 2011/05/12]{lang="EN-US"}

[Key code:]{lang="EN-US"}

[   308201B83082012C06072A8648CE3804013082011F02818100D757262C4584C44C211F18BD]{lang="EN-US"}

[   96E5F061C4F0A423F7FE6B6B85B34CEF72CE14A0D3A5222FE08CECE65BE6C265854889DC1E]{lang="EN-US"}

[   DBD13EC8B274DA9F75BA26CCB987723602787E922BA84421F22C3C89CB9B06FD60FE01941D]{lang="EN-US"}

[   DD77FE6B12893DA76EEBC1D128D97F0678D7722B5341C8506F358214B16A2FAC4B36895038]{lang="EN-US"}

[   7811C7DA33021500C773218C737EC8EE993B4F2DED30F48EDACE915F0281810082269009E1]{lang="EN-US"}

[   4EC474BAF2932E69D3B1F18517AD9594184CCDFCEAE96EC4D5EF93133E84B47093C52B20CD]{lang="EN-US"}

[   35D02492B3959EC6499625BC4FA5082E22C5B374E16DD00132CE71B020217091AC717B6123]{lang="EN-US"}

[   91C76C1FB2E88317C1BD8171D41ECB83E210C03CC9B32E810561C21621C73D6DAAC028F4B1]{lang="EN-US"}

[   585DA7F42519718CC9B09EEF0381850002818100A1E456C8DA2AD1BB83B1BDF2A1A6B5A6E8]{lang="EN-US"}

[   3642B460402445DA7E4036715F468F76655E114D460B7112F57143EE020AEF4A5BFAD07B74]{lang="EN-US"}

[   0FBCB1C64DA8A2BCE619283421445EEC77D3CF0D11866E9656AD6511F4926F8376967B0AB7]{lang="EN-US"}

[   15F9FB7B514BC1174155DD6E073B1FCB3A2749E6C5FEA81003E16729497D0EAD9105E3E76A]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_x1901973538}[显示名称为]{style="font-family:宋体"}[ecdsa1]{lang="EN-US"}[的本地]{style="font-family:宋体"}[ECDSA]{lang="EN-US"}[密钥对中的公钥信息。]{style="font-family:宋体"}

[[\<Sysname\> display public-key local ecdsa public name ecdsa1]{lang="EN-US"}]{#struct_0_x1871_x1914_x872128077}

[ ]{lang="EN-US"}

[=============================================]{lang="EN-US"}

[Key name: ecdsa1]{lang="EN-US"}

[Key type: ECDSA]{lang="EN-US"}

[Time when key pair created: 15:43:33 2011/05/12]{lang="EN-US"}

[Key code:]{lang="EN-US"}

[   3049301306072A8648CE3D020106082A8648CE3D03010103320004A1FB84D92315B8DB72D1]{lang="EN-US"}

[   AE672C7CFA5135D5F5B02377F2F092F182EC83B5819795BC94CCBD3EBA7D4F0F2B2EB20C58]{lang="EN-US"}

[   4D]{lang="EN-US"}

[]{#struct_0_x1871_x1914_206264694}[[表1-1 ]{lang="EN-US"}[display public-key local public]{lang="EN-US"}]{#_Toc138241147}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1916951917}[[字段]{style="font-family:黑体"}]{#struct_0_x1871_x1914_x1133706445}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1871_x1914_173885696}

[[Key name]{lang="EN-US"}]{#struct_0_x1871_x1914_x364107038}

[[本地非对称密钥对的名称]{style="font-family:宋体"}]{#struct_0_x1871_x1914_712397053}

[[default]{lang="EN-US"}]{#struct_0_x1871_x1914_x1569383610}[表示该名称为密钥对的默认名称，即执行]{style="font-family:宋体"}**[public-key local create]{lang="EN-US"}**[命令没有指定密钥名称时，生成的密钥对的名称]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[hostkey]{lang="EN-US"}]{#struct_0_x1871_x1914_162542476}[：]{style="font-family:宋体"}[RSA]{lang="EN-US"}[主机密钥对的默认名称]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[serverkey]{lang="EN-US"}]{#struct_0_x1871_x1914_206723446}[：]{style="font-family:宋体"}[RSA]{lang="EN-US"}[服务器密钥对的默认名称。只有密钥类型为]{style="font-family:宋体"}[RSA]{lang="EN-US"}[时，才会存在服务器密钥对]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[dsakey]{lang="EN-US"}]{#struct_0_x1871_x1914_1750538607}[：]{style="font-family:宋体"}[DSA]{lang="EN-US"}[主机密钥对的默认名称]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ecdsakey]{lang="EN-US"}]{#struct_0_x1871_x1914_x1245263547}[：]{style="font-family:宋体"}[ECDSA]{lang="EN-US"}[主机密钥对的默认名称]{style="font-family:宋体"}

[[Key type]{lang="EN-US"}]{#struct_0_x1871_x1914_209403752}

[[密钥类型，取值包括：]{style="font-family:宋体"}]{#struct_0_x1871_x1914_1085259977}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RSA]{lang="EN-US"}]{#struct_0_x1871_x1914_1822771064}[：密钥类型为]{style="font-family:宋体"}[RSA]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DSA]{lang="EN-US"}]{#struct_0_x1871_x1914_206657910}[：密钥类型为]{style="font-family:宋体"}[DSA]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ECDSA]{lang="EN-US"}]{#struct_0_x1871_x1914_x186706127}[：密钥类型为]{style="font-family:宋体"}[ECDSA]{lang="EN-US"}

[[Time when key pair created]{lang="EN-US"}]{#struct_0_x1871_x1914_1809002053}

[[本地非对称密钥对产生的时间]{style="font-family:宋体"}]{#struct_0_x1871_x1914_972438199}

[[Key code]{lang="EN-US"}]{#struct_0_x1871_x1914_x1672821076}

[[本地非对称密钥对的公钥数据]{style="font-family:宋体"}]{#struct_0_x1871_x1914_1651413762}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_206199155}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[public-key local create]{lang="EN-US"}**]{#struct_0_x1871_x1914_x1001145704}

::: {#-1743557713 .myid}
[]{#_Toc404792929}[]{#struct_0_x1871_x1914_1775276131}[]{#_Toc195409916}[]{#_Toc149979594}[]{#_Toc144810330}[]{#_Toc144782891}[]{#_Toc29974898}[]{#_Toc25576894}[]{#_Toc292983989}[]{#_Toc292986726}[]{#_Toc292986752}

**公钥管理 \-- 公钥管理配置命令 \-- display public-key peer**

------------------------------------------------------------------------

[**[display public-key peer]{lang="EN-US"}**]{#struct_0_x1871_x1914_1725559017}[命令用来显示保存在本地的远端主机的公钥信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_x1369420626}

[**[display public-key peer]{lang="EN-US"}**[ \[ **brief** \| **name** *publickey-name* \]]{lang="EN-US"}]{#struct_0_x1871_x1914_x980671478}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_x37045816}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1871_x1914_1544773037}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_206133619}

[[network-admin]{lang="EN-US"}]{#struct_0_x1871_x1914_536019537}

[[network-operator]{lang="EN-US"}]{#struct_0_x1871_x1914_948275627}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1871_x1914_x751075754}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1871_x1914_1136831130}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_677486457}

[**[brief]{lang="EN-US"}**]{#struct_0_x1871_x1914_926935798}[：显示保存在本地的所有远端主机公钥的简要信息。]{style="font-family:宋体"}

[**[name ]{lang="EN-US"}***[publickey-name]{lang="EN-US"}*]{#struct_0_x1871_x1914_1753653820}[：显示保存在本地的指定远端主机公钥的详细信息，]{style="font-family:宋体"}*[publickey-name]{lang="EN-US"}*[为远端主机公钥的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_x531314949}

[[如果没有指定任何参数，则显示所有保存在本地的远端主机公钥的详细信息。]{style="font-family:宋体"}]{#struct_0_x1871_x1914_206068083}

[[可以通过]{style="font-family:宋体"}**[public-key peer]{lang="EN-US"}**]{#struct_0_x1871_x1914_1352746892}[命令或]{style="font-family:宋体"}**[public-key peer import sshkey]{lang="EN-US"}**[命令将远端主机的公钥配置到本地。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_x604870393}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_1529344494}[显示保存在本地的公钥名称为]{style="font-family:宋体"}[idrsa]{lang="EN-US"}[的远端主机公钥的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display public-key peer name idrsa]{lang="EN-US"}]{#struct_0_x1871_x1914_2076008845}

[ ]{lang="EN-US"}

[=============================================]{lang="EN-US"}

[Key name: idrsa]{lang="EN-US"}

[Key type: RSA]{lang="EN-US"}

[Key modulus: 1024]{lang="EN-US"}

[Key code:]{lang="EN-US"}

[   30819F300D06092A864886F70D010101050003818D0030818902818100C5971581A78B5388]{lang="EN-US"}

[   B3C9063EC6B53D395A6704D9752B6F9B7B1F734EEB5DD509F0B050662C46FFB8D27F797E37]{lang="EN-US"}

[   918F6270C5793F1FC63638970A0E4D51A3CEF7CFF6E92BFAFD73F530E0BDE27056E81F2525]{lang="EN-US"}

[   6D0883836FD8E68031B2C272FE2EA75C87734A7B8F85B8EBEB3BD51CC26916AF3B3FDC32C3]{lang="EN-US"}

[   42C142D41BB4884FEB0203010001]{lang="EN-US"}

[]{#struct_0_x1871_x1914_x1170504782}[[表1-2 ]{lang="EN-US"}[display public-key peer name]{lang="EN-US"}]{#_Toc138241148}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1923308582}[[字段]{style="font-family:黑体"}]{#struct_0_x1871_x1914_206002547}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1871_x1914_x1405055399}

[[Key name]{lang="EN-US"}]{#struct_0_x1871_x1914_630121505}

[[远端主机公钥的名称]{style="font-family:宋体"}]{#struct_0_x1871_x1914_640240943}

[[Key type]{lang="EN-US"}]{#struct_0_x1871_x1914_1754144599}

[[密钥类型，取值包括]{style="font-family:宋体"}[RSA]{lang="EN-US"}]{#struct_0_x1871_x1914_861098620}[、]{style="font-family:宋体"}[DSA]{lang="EN-US"}[和]{style="font-family:宋体"}[ECDSA]{lang="EN-US"}

[[Key modulus]{lang="EN-US"}]{#struct_0_x1871_x1914_1090324746}

[[密钥模数的长度，单位为比特]{style="font-family:宋体"}]{#struct_0_x1871_x1914_206461299}

[[Key code]{lang="EN-US"}]{#struct_0_x1871_x1914_1114255548}

[[公钥数据]{style="font-family:宋体"}]{#struct_0_x1871_x1914_x525114564}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_385298022}[显示保存在本地的所有远端主机公钥的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display public-key peer brief]{lang="EN-US"}]{#struct_0_x1871_x1914_1359879018}

[Type  Modulus  Name]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[RSA   1024    idrsa]{lang="EN-US"}

[DSA   1024    10.1.1.1]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display public-key peer brief]{lang="EN-US"}]{#struct_0_x1871_x1914_x348433339}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1921582629}[[字段]{style="font-family:黑体"}]{#struct_0_x1871_x1914_206395763}

[[描述]{style="font-family:黑体"}]{#struct_0_x1871_x1914_1954379324}

[[Type]{lang="EN-US"}]{#struct_0_x1871_x1914_598300019}

[[密钥类型，取值包括]{style="font-family:宋体"}[RSA]{lang="EN-US"}]{#struct_0_x1871_x1914_1010722421}[、]{style="font-family:宋体"}[DSA]{lang="EN-US"}[和]{style="font-family:宋体"}[ECDSA]{lang="EN-US"}

[[Modulus]{lang="EN-US"}]{#struct_0_x1871_x1914_x1173349488}

[[密钥模数的长度，单位为比特]{style="font-family:宋体"}]{#struct_0_x1871_x1914_1411159680}

[[Name]{lang="EN-US"}]{#struct_0_x1871_x1914_x1491323589}

[[远端主机公钥的名称]{style="font-family:宋体"}]{#struct_0_x1871_x1914_206330227}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_436678619}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[public-key peer]{lang="EN-US"}**]{#struct_0_x1871_x1914_570030791}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[public-key peer]{lang="EN-US"}***[ ]{lang="EN-US"}***[import]{lang="EN-US"}**[ **sshkey**]{lang="EN-US"}]{#struct_0_x1871_x1914_x780570408}

::: {#-1178680169 .myid}
[]{#_Toc404792930}[]{#struct_0_x1871_x1914_588334282}[]{#_Toc195409922}

**公钥管理 \-- 公钥管理配置命令 \-- peer-public-key end**

------------------------------------------------------------------------

[**[peer-public-key]{lang="SV"}**]{#struct_0_x1871_x1914_858357085}[ **end**]{lang="SV"}[命令用来从公钥视图退回到系统视图]{style="font-family:宋体"}[，]{style="font-family:宋体"}[并保存用户输入的公钥。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_1043632306}

[**[peer-public-key end]{lang="SV"}**]{#struct_0_x1871_x1914_346643038}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_1841122246}

[[公钥视图]{style="font-family:宋体"}]{#struct_0_x1871_x1914_206264691}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_x1133706448}

[[network-admin]{lang="SV"}]{#struct_0_x1871_x1914_126831529}

[[mdc-admin]{lang="SV"}]{#struct_0_x1871_x1914_242457327}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_x1359968940}

[[本命令用于通过手工配置方式将远端主机的公钥保存到本地设备上。手工配置方式是指：]{style="font-family:宋体"}]{#struct_0_x1871_x1914_x666690825}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[执行]{lang="EN-US" style="font-family:宋体"}**[public-key peer]{lang="EN-US"}**]{#struct_0_x1871_x1914_1730879875}[命令进入公钥视图。]{lang="EN-US" style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[在公钥视图手工输入远端主机的公钥。]{style="font-family:宋体"}]{#struct_0_x1871_x1914_213599318}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[执行]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1871_x1914_1953594340}**[peer-public-key]{lang="SV"}**[ **end**]{lang="SV"}[命令退出公钥视图，并保存输入的公钥。]{lang="EN-US" style="font-family:宋体"}

[[输入的公钥数据必须满足一定的格式要求。在保存公钥之前，设备会进行公钥合法性的检测：]{style="font-family:宋体"}]{#struct_0_x1871_x1914_206723443}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果用户配置的公钥字符串不满足格式要求，那么将会显示相关提示信息，用户配置的公钥将被丢弃，本次配置失败；]{style="font-family:宋体"}]{#struct_0_x1871_x1914_1750538612}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果用户配置的公钥字符串合法，例如输入的公钥数据为通过]{lang="EN-US" style="font-family:宋体"}**[display public-key local public]{lang="EN-US"}**]{#struct_0_x1871_x1914_x1245460156}[命令显示的公钥，则保存该公钥。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_x1503480833}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_x1345631842}[退出公钥视图，并保存用户输入的公钥。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1871_x1914_x1094529602}

[\[Sysname\] public-key peer key1]{lang="EN-US"}

[Enter public key view. Return to system view with \"peer-public-key end\" command.]{lang="EN-US"}

[\[Sysname-pkey-public-key-key1\]30819F300D06092A864886F70D010101050003818D0030818902818100C0EC8014F82515F6335A0A]{lang="EN-US"}

[\[Sysname-pkey-public-key-key1\]EF8F999C01EC94E5760A079BD73E4F4D97F3500EDB308C29481B77E719D1643135877E13B1C531B4]{lang="EN-US"}

[\[Sysname-pkey-public-key-key1\]FF1877A5E2E7B1FA4710DB0744F66F6600EEFE166F1B854E2371D5B952ADF6B80EB5F52698FCF3D6]{lang="EN-US"}

[\[Sysname-pkey-public-key-key1\]1F0C2EAAD9813ECB16C5C7DC09812D4EE3E9A0B074276FFD4AF2050BD4A9B1DDE675AC30CB020301]{lang="EN-US"}

[\[Sysname-pkey-public-key-key1\]0001]{lang="EN-US"}

[\[Sysname-pkey-public-key-key1\] peer-public-key end]{lang="EN-US"}

[\[Sysname\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_1185981805}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display public-key local public]{lang="EN-US"}**]{#struct_0_x1871_x1914_206657907}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display public-key peer]{lang="EN-US"}**]{#struct_0_x1871_x1914_1769609010}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[public-key peer]{lang="EN-US"}**]{#struct_0_x1871_x1914_x1767300275}
:::

::: {#-203730704 .myid}
[]{#_Toc404792931}[]{#struct_0_x1871_x1914_227541257}[]{#_Toc195409925}[]{#_Toc149979604}[]{#_Toc144810340}[]{#_Toc144782901}[]{#_Toc165086104}[]{#_Toc165086609}[]{#_Toc165086106}[]{#_Toc165086611}[]{#_Toc165086107}[]{#_Toc165086612}[]{#_Toc165086108}[]{#_Toc165086613}[]{#_Toc165086109}[]{#_Toc165086614}[]{#_Toc165086110}[]{#_Toc165086615}[]{#_Toc165086111}[]{#_Toc165086616}[]{#_Toc165086112}[]{#_Toc165086617}[]{#_Toc165086113}[]{#_Toc165086618}[]{#_Toc165086114}[]{#_Toc165086619}[]{#_Toc165086115}[]{#_Toc165086620}[]{#_Toc165086116}[]{#_Toc165086621}[]{#_Toc165086117}[]{#_Toc165086622}[]{#_Toc165086118}[]{#_Toc165086623}[]{#_Toc165086119}[]{#_Toc165086624}[]{#_Toc165086120}[]{#_Toc165086625}[]{#_Toc165086121}[]{#_Toc165086626}[]{#_Toc165086122}[]{#_Toc165086627}[]{#_Toc165086123}[]{#_Toc165086628}[]{#_Toc271791106}[]{#_Toc271791108}[]{#_Toc271791109}[]{#_Toc271791110}[]{#_Toc271791111}[]{#_Toc271791112}[]{#_Toc271791113}[]{#_Toc271791114}[]{#_Toc271791115}[]{#_Toc271791116}[]{#_Toc271791117}[]{#_Toc271791118}[]{#_Toc271791119}[]{#_Toc271791120}[]{#_Toc271791121}[]{#_Toc271791122}[]{#_Toc271791124}[]{#_Toc271791130}[]{#_Toc271791131}[]{#_Toc271791132}[]{#_Toc271791134}[]{#_Toc271791135}[]{#_Toc271791136}[]{#_Toc271791137}[]{#_Toc271791138}[]{#_Toc271791139}[]{#_Toc271791140}[]{#_Toc271791141}[]{#_Toc271791142}[]{#_Toc271791143}[]{#_Toc271791144}[]{#_Toc271791145}[]{#_Toc271791146}[]{#_Toc271791147}[]{#_Toc271791149}[]{#_Toc271791155}

**公钥管理 \-- 公钥管理配置命令 \-- public-key local create**

------------------------------------------------------------------------

[**[public-key local create]{lang="EN-US"}**]{#struct_0_x1871_x1914_676205119}[命令用来生成本地非对称密钥对。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_x1004033304}

[**[public-key local create]{lang="EN-US"}**[ { **dsa** \| **ecdsa** \| **rsa** } \[ **name** *key-name* \]]{lang="EN-US"}]{#struct_0_x1871_x1914_418310893}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_x1376600777}

[[设备上不存在任何本地非对称密钥对。]{style="font-family:宋体"}]{#struct_0_x1871_x1914_206199156}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_x1001145705}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1871_x1914_x953607224}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_x773078388}

[[network-admin]{lang="EN-US"}]{#struct_0_x1871_x1914_1525308602}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1871_x1914_1499650266}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_1306548325}

[**[dsa]{lang="EN-US"}**]{#struct_0_x1871_x1914_x1303918563}[：本地密钥对类型为]{style="font-family:宋体"}[DSA]{lang="EN-US"}[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ecdsa]{lang="EN-US"}**]{#struct_0_x1871_x1914_x879528324}[：本地密钥对类型为]{style="font-family:宋体"}[ECDSA]{lang="EN-US"}[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[rsa]{lang="EN-US"}**]{#struct_0_x1871_x1914_206133620}[：本地密钥对类型为]{style="font-family:宋体"}[RSA]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[name ]{lang="EN-US"}***[key-name]{lang="EN-US"}*]{#struct_0_x1871_x1914_x1037958582}[：生成指定名称的本地非对称密钥对。]{style="font-family:宋体"}*[key-name]{lang="EN-US"}*[为本地非对称密钥对的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，不区分大小写，字符串中可以包含字母、数字及"]{style="font-family:宋体"}[-]{lang="EN-US"}["。如果不指定本参数，则生成的]{style="font-family:宋体"}[RSA]{lang="EN-US"}[主机密钥对的默认名称为]{style="font-family:宋体"}[hostkey]{lang="EN-US"}[，]{style="font-family:宋体"}[RSA]{lang="EN-US"}[服务器密钥对的默认名称为]{style="font-family:宋体"}[serverkey]{lang="EN-US"}[，]{style="font-family:宋体"}[DSA]{lang="EN-US"}[密钥对的默认名称为]{style="font-family:宋体"}[dsakey]{lang="EN-US"}[，]{style="font-family:宋体"}[ECDSA]{lang="EN-US"}[密钥对的默认名称为]{style="font-family:宋体"}[ecdsakey]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_1997472804}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在非]{style="font-family:宋体"}]{#struct_0_x1871_x1914_1256877811}[FIPS]{lang="EN-US"}[模式下，生成默认名称的本地]{style="font-family:宋体"}[RSA]{lang="EN-US"}[密钥对时，将同时生成两个密钥对------服务器密钥对和主机密钥对，二者都包括一个公钥和一个私钥；生成非默认名称的本地]{style="font-family:宋体"}[RSA]{lang="EN-US"}[密钥对时，只生成一个主机密钥对。]{style="font-family:宋体"}[RSA]{lang="EN-US"}[密钥模数的最小长度为]{style="font-family:宋体"}[512]{lang="EN-US"}[比特，最大长度为]{style="font-family:宋体"}[2048]{lang="EN-US"}[比特，缺省长度为]{style="font-family:宋体"}[1024]{lang="EN-US"}[比特。密钥模数越长，安全性越好，但是生成密钥的时间越长。生成]{style="font-family:宋体"}[RSA]{lang="EN-US"}[密钥对时会提示用户输入密钥模数的长度，建议密钥模数的长度大于或等于]{style="font-family:宋体"}[768]{lang="EN-US"}[比特，以提高安全性。目前，只有]{style="font-family:宋体"}[SSH1.5]{lang="EN-US"}[中应用了]{style="font-family:宋体"}[RSA]{lang="EN-US"}[服务器密钥对。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x1871_x1914_1691481035}[FIPS]{lang="EN-US"}[模式下，生成默认名称的本地]{style="font-family:宋体"}[RSA]{lang="EN-US"}[密钥对时，将生成]{style="font-family:宋体"}[1]{lang="EN-US"}[个密钥对------主机密钥对，包括一个公钥和一个私钥；]{style="font-family:宋体"}[RSA]{lang="EN-US"}[密钥模数的长度为]{style="font-family:宋体"}[2048]{lang="EN-US"}[比特。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在非]{style="font-family:宋体"}]{#struct_0_x1871_x1914_915727248}[FIPS]{lang="EN-US"}[模式下，生成本地]{style="font-family:宋体"}[DSA]{lang="EN-US"}[密钥对时，只生成一个主机密钥对。]{style="font-family:宋体"}[DSA]{lang="EN-US"}[主机密钥模数的最小长度为]{style="font-family:宋体"}[512]{lang="EN-US"}[比特，最大长度为]{style="font-family:宋体"}[2048]{lang="EN-US"}[比特，缺]{style="font-family:宋体"}[省长度为]{style="font-family:宋体"}[1024]{lang="EN-US"}[比特。密钥模数越长，安全性越好，但是生成密钥的时间越长。生成]{style="font-family:宋体"}[DSA]{lang="EN-US"}[密钥对时会提示用户输入密钥模数的长度，建议密钥模数的长度大于或等于]{style="font-family:宋体"}[768]{lang="EN-US"}[比特，以提高安全性。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x1871_x1914_x365667923}[FIPS]{lang="EN-US"}[模式下，生成本地]{style="font-family:宋体"}[DSA]{lang="EN-US"}[密钥对时，只生成一个主机密钥对。]{style="font-family:宋体"}[DSA]{lang="EN-US"}[密钥模数的长度为]{style="font-family:宋体"}[2048]{lang="EN-US"}[比特。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[生成本地]{style="font-family:宋体"}]{#struct_0_x1871_x1914_1928155585}[ECDSA]{lang="EN-US"}[密钥对时，只生成一个主机密钥对。]{style="font-family:宋体"}[ECDSA]{lang="EN-US"}[主机密钥的长度为]{style="font-family:宋体"}[192]{lang="EN-US"}[比特。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[生成密钥对时，通过]{style="font-family:宋体"}]{#struct_0_x1871_x1914_x1463233048}**[name ]{lang="EN-US"}***[key-name]{lang="EN-US"}*[参数指定的密钥对名称可以与密钥对的默认名称相同，该密钥对与不指定]{style="font-family:宋体"}**[name ]{lang="EN-US"}***[key-name]{lang="EN-US"}*[参数生成的默认名称的密钥对被视为两个不同的密钥对，可以在设备上同时存在这两个密钥对。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[非默认名称密钥对的密钥类型和名称不能完全相同，否则需要用户确认是否覆盖原有的密钥对。不同类型的密钥，名称可以相同。]{style="font-family:宋体"}]{#struct_0_x1871_x1914_206068084}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行此命令后，生成的密钥对将保存在设备中，设备重启后密钥不会丢失。]{style="font-family:宋体"}]{#struct_0_x1871_x1914_1352746897}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_x605067001}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_x44478898}[生成默认名称的本地]{style="font-family:宋体"}[RSA]{lang="EN-US"}[非对称密钥对。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1871_x1914_285062737}

[\[Sysname\] public-key local create rsa]{lang="EN-US"}

[The range of public key modulus is (512 \~ 2048).]{lang="EN-US"}

[If the key modulus is greater than 512, it will take a few minutes.]{lang="EN-US"}

[Press CTRL+C to abort.]{lang="EN-US"}

[Input the modulus length \[default = 1024\]:]{lang="EN-US"}

[Generating Keys\...]{lang="EN-US"}

[\...++++++]{lang="EN-US"}

[.++++++]{lang="EN-US"}

[..++++++++]{lang="EN-US"}

[\....++++++++]{lang="EN-US"}

[Create the key pair successfully.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_722135192}[生成默认名称的本地]{style="font-family:宋体"}[DSA]{lang="EN-US"}[非对称密钥对。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1871_x1914_206002548}

[\[Sysname\] public-key local create dsa]{lang="EN-US"}

[The range of public key modulus is (512 \~ 2048).]{lang="EN-US"}

[If the key modulus is greater than 512, it will take a few minutes.]{lang="EN-US"}

[Press CTRL+C to abort.]{lang="EN-US"}

[Input the modulus length \[default = 1024\]:]{lang="EN-US"}

[Generating Keys\...]{lang="EN-US"}

[.++++++++++++++++++++++++++++++++++++++++++++++++++\*]{lang="EN-US"}

[\...\.....+\...\...+\.....+\...\...\...\...\...\...\...\...\...\...\...\.....+..+\...\...\...\...\....]{lang="EN-US"}

[\...\....+\...\...\....+\...\...\...\.....+\...\...\...\....+\...+\.....+\...\...\...\...\...+..+\...]{lang="EN-US"}

[\...+\...\...\...\...\.....+\...\...\....+\...+\....+\...\....+\.....+\...\...\...\...+\...\...\...+.]{lang="EN-US"}

[\...\...\...\...\...\...\...\...+\...\.....+\...\...\....+\...\...\...\.....+\.....+\...+\...\...\....]{lang="EN-US"}

[\...\...\...\.....+\...\...\...+\...\...\....+\...\...\.....+\...\.....+\....+\...\...\...\...\...\...]{lang="EN-US"}

[\.....+++++++++++++++++++++++++++++++++++++++++++++++++++\*]{lang="EN-US"}

[Create the key pair successfully.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_x1405055414}[生成默认名称的本地]{style="font-family:宋体"}[ECDSA]{lang="EN-US"}[非对称密钥对。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1871_x1914_x485099449}

[\[Sysname\] public-key local create ecdsa]{lang="EN-US"}

[Generating Keys\...]{lang="EN-US"}

[Create the key pair successfully.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_1866470341}[生成名称为]{style="font-family:宋体"}[rsa1]{lang="EN-US"}[的本地]{style="font-family:宋体"}[RSA]{lang="EN-US"}[非对称密钥对。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1871_x1914_206461300}

[\[Sysname\] public-key local create rsa name rsa1]{lang="EN-US"}

[The range of public key modulus is (512 \~ 2048).]{lang="EN-US"}

[If the key modulus is greater than 512, it will take a few minutes.]{lang="EN-US"}

[Press CTRL+C to abort.]{lang="EN-US"}

[Input the modulus length \[default = 1024\]:]{lang="EN-US"}

[Generating Keys\...]{lang="EN-US"}

[\...++++++]{lang="EN-US"}

[\...\...\...\...\...\...\...\...\...\....++++++]{lang="EN-US"}

[Create the key pair successfully.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_x1261132450}[生成名称为]{style="font-family:宋体"}[dsa1]{lang="EN-US"}[的本地]{style="font-family:宋体"}[DSA]{lang="EN-US"}[非对称密钥对。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1871_x1914_206395764}

[\[Sysname\] public-key local create dsa name dsa1]{lang="EN-US"}

[The range of public key modulus is (512 \~ 2048).]{lang="EN-US"}

[If the key modulus is greater than 512, it will take a few minutes.]{lang="EN-US"}

[Press CTRL+C to abort.]{lang="EN-US"}

[Input the modulus length \[default = 1024\]:]{lang="EN-US"}

[Generating Keys\...]{lang="EN-US"}

[.++++++++++++++++++++++++++++++++++++++++++++++++++\*]{lang="EN-US"}

[\...\.....+\...\...+\.....+\...\...\...\...\...\...\...\...\...\...\...\.....+..+\...\...\...\...\....]{lang="EN-US"}

[\...\....+\...\...\....+\...\...\...\.....+\...\...\...\....+\...+\.....+\...\...\...\...\...+..+\...]{lang="EN-US"}

[\...+\...\...\...\...\.....+\...\...\....+\...+\....+\...\....+\.....+\...\...\...\...+\...\...\...+.]{lang="EN-US"}

[\...\...\...\...\...\...\...\...+\...\.....+\...\...\....+\...\...\...\.....+\.....+\...+\...\...\....]{lang="EN-US"}

[\...\...\...\.....+\...\...\...+\...\...\....+\...\...\.....+\...\.....+\....+\...\...\...\...\...\...]{lang="EN-US"}

[\.....+++++++++++++++++++++++++++++++++++++++++++++++++++\*]{lang="EN-US"}

[Create the key pair successfully.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_1954379323}[生成名称为]{style="font-family:宋体"}[ecdsa1]{lang="EN-US"}[的本地]{style="font-family:宋体"}[ECDSA]{lang="EN-US"}[非对称密钥对。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1871_x1914_598365555}

[\[Sysname\] public-key local create ecdsa name ecdsa1]{lang="EN-US"}

[Generating Keys\...]{lang="EN-US"}

[Create the key pair successfully.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_x1770869186}[在]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下生成默认名称的本地]{style="font-family:宋体"}[RSA]{lang="EN-US"}[非对称密钥对。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1871_x1914_206330228}

[\[Sysname\] public-key local create rsa]{lang="EN-US"}

[The range of public key modulus is (2048 \~ 2048).]{lang="EN-US"}

[It will take a few minutes.Press CTRL+C to abort.]{lang="EN-US"}

[Input the modulus length \[default = 2024\]:]{lang="EN-US"}

[Generating Keys\...]{lang="EN-US"}

[\...++++++]{lang="EN-US"}

[.++++++]{lang="EN-US"}

[..++++++++]{lang="EN-US"}

[\....++++++++]{lang="EN-US"}

[Create the key pair successfully.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_436678630}[在]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下生成默认名称的本地]{style="font-family:宋体"}[DSA]{lang="EN-US"}[非对称密钥对。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1871_x1914_952367824}

[\[Sysname\] public-key local create dsa]{lang="EN-US"}

[The range of public key modulus is (2048 \~ 2048).]{lang="EN-US"}

[It will take a few minutes.Press CTRL+C to abort.]{lang="EN-US"}

[Input the modulus length \[default = 2024\]:]{lang="EN-US"}

[.++++++++++++++++++++++++++++++++++++++++++++++++++\*]{lang="EN-US"}

[\...\.....+\...\...+\.....+\...\...\...\...\...\...\...\...\...\...\...\.....+..+\...\...\...\...\....]{lang="EN-US"}

[\...\....+\...\...\....+\...\...\...\.....+\...\...\...\....+\...+\.....+\...\...\...\...\...+..+\...]{lang="EN-US"}

[\...+\...\...\...\...\.....+\...\...\....+\...+\....+\...\....+\.....+\...\...\...\...+\...\...\...+.]{lang="EN-US"}

[\...\...\...\...\...\...\...\...+\...\.....+\...\...\....+\...\...\...\.....+\.....+\...+\...\...\....]{lang="EN-US"}

[\...\...\...\.....+\...\...\...+\...\...\....+\...\...\.....+\...\.....+\....+\...\...\...\...\...\...]{lang="EN-US"}

[\.....+++++++++++++++++++++++++++++++++++++++++++++++++++\*]{lang="EN-US"}

[Create the key pair successfully.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_x289671655}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
Symbol"}]{.TerminalDisplayChar}**[display public-key local public]{lang="EN-US"}**]{#struct_0_x1871_x1914_2097002954}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[public-key local destroy]{lang="EN-US"}**]{#struct_0_x1871_x1914_x1366727941}
:::

::: {#1258178250 .myid}
[]{#_Toc404792932}[]{#struct_0_x1871_x1914_206264692}[]{#_Toc195409926}[]{#_Toc149979605}[]{#_Toc144810341}[]{#_Toc144782902}

**公钥管理 \-- 公钥管理配置命令 \-- public-key local destroy**

------------------------------------------------------------------------

[**[public-key local destroy]{lang="EN-US"}**]{#struct_0_x1871_x1914_x1133706451}[命令用来销毁本地非对称密钥对。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_x1795548308}

[**[public-key local destroy]{lang="EN-US"}**[ { **dsa** \| **ecdsa** \| **rsa** } \[ **name** *key-name* \]]{lang="EN-US"}]{#struct_0_x1871_x1914_x395357676}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_x431842714}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1871_x1914_x574567348}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_x1614853782}

[[network-admin]{lang="EN-US"}]{#struct_0_x1871_x1914_x727683273}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1871_x1914_x646553747}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_206723444}

[**[dsa]{lang="EN-US"}**]{#struct_0_x1871_x1914_1750538609}[：本地密钥对类型为]{style="font-family:宋体"}[DSA]{lang="EN-US"}[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ecdsa]{lang="EN-US"}**]{#struct_0_x1871_x1914_x1245132475}[：本地密钥对类型为]{style="font-family:宋体"}[ECDSA]{lang="EN-US"}[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[rsa]{lang="EN-US"}**]{#struct_0_x1871_x1914_x1461505306}[：本地密钥对类型为]{style="font-family:宋体"}[RSA]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[name ]{lang="EN-US"}***[key-name]{lang="EN-US"}*]{#struct_0_x1871_x1914_2113083724}[：销毁指定名称的本地非对称密钥对。]{style="font-family:宋体"}*[key-name]{lang="EN-US"}*[为本地非对称密钥对名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，不区分大小写，字符串中可以包含字母、数字及"]{style="font-family:宋体"}[-]{lang="EN-US"}["。如果不指定本参数，则销毁指定类型默认名称的本地非对称密钥对。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_30448341}

[[在如下几种情况下，建议用户销毁旧的非对称密钥对，并生成新的密钥对：]{style="font-family:宋体"}]{#struct_0_x1871_x1914_x964009629}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本地设备的私钥泄露。这种情况下，非法用户可能会冒充本地设备访问网络。]{style="font-family:宋体"}]{#struct_0_x1871_x1914_x2110590939}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[保存密钥对的存储设备出现故障，导致设备上没有公钥对应的私钥，无法再利用旧的非对称密钥对进行加解密和数字签名。]{style="font-family:宋体"}]{#struct_0_x1871_x1914_x1364595861}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[密钥对使用了较长时间，可能存在密钥泄露或破译的风险。]{style="font-family:宋体"}]{#struct_0_x1871_x1914_206657908}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本地证书到达有效期，需要删除对应的本地密钥对。本地证书的详细介绍，请参见"安全配置指导"中的"]{style="font-family:宋体"}]{#struct_0_x1871_x1914_1769609001}[PKI]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_x1767234740}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_x1128761656}[销毁默认名称的本地]{style="font-family:宋体"}[RSA]{lang="EN-US"}[非对称密钥对。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1871_x1914_x1286900920}

[\[Sysname\] public-key local destroy rsa]{lang="EN-US"}

[Confirm to destroy the key pair? \[Y/N\]:y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_x2129023598}[销毁默认名称的本地]{style="font-family:宋体"}[DSA]{lang="EN-US"}[非对称密钥对。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1871_x1914_250231922}

[\[Sysname\] public-key local destroy dsa]{lang="EN-US"}

[Confirm to destroy the key pair? \[Y/N\] :y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_x1605750726}[销毁默认名称的本地]{style="font-family:宋体"}[ECDSA]{lang="EN-US"}[非对称密钥对。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1871_x1914_206199153}

[\[Sysname\] public-key local destroy ecdsa]{lang="EN-US"}

[Confirm to destroy the key pair? \[Y/N\]:y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_x1001145702}[销毁名称为]{style="font-family:宋体"}[rsa1]{lang="EN-US"}[的本地]{style="font-family:宋体"}[RSA]{lang="EN-US"}[非对称密钥对。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1871_x1914_612476717}

[\[Sysname\] public-key local destroy rsa name rsa1]{lang="EN-US"}

[Confirm to destroy the key pair? \[Y/N\]:y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_x899702602}[销毁名称为]{style="font-family:宋体"}[dsa1]{lang="EN-US"}[的本地]{style="font-family:宋体"}[DSA]{lang="EN-US"}[非对称密钥对。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1871_x1914_153369874}

[\[Sysname\] public-key local destroy dsa name dsa1]{lang="EN-US"}

[Confirm to destroy the key pair? \[Y/N\] :y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_x589973076}[销毁名称为]{style="font-family:宋体"}[ecdsa1]{lang="EN-US"}[的本地]{style="font-family:宋体"}[ECDSA]{lang="EN-US"}[非对称密钥对。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1871_x1914_206133617}

[\[Sysname\] public-key local destroy ecdsa name ecdsa1]{lang="EN-US"}

[Confirm to destroy the key pair? \[Y/N\]:y]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_536019527}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[public-key local create]{lang="EN-US"}**]{#struct_0_x1871_x1914_x1390376533}
:::

::::: {#1644788797 .myid}
[]{#_Toc195409927}[]{#_Toc149979606}[]{#_Toc144810342}[]{#_Toc133380268}[]{#_Toc144782903}[]{#_Toc404792933}[]{#struct_0_x1871_x1914_50804837}

**公钥管理 \-- 公钥管理配置命令 \-- public-key local export dsa**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](公钥管理命令.files/image002.png){#图片 16 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1871_x1914_68547226}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1871_x1914_x438424782}
:::

[ ]{lang="EN-US"}

[**[public-key local export dsa]{lang="EN-US"}**]{#struct_0_x1871_x1914_453972015}[命令用来根据指定格式显示本地]{style="font-family:
宋体"}[DSA]{lang="EN-US"}[主机公钥或将其导出到指定文件。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_x171114367}

[**[public-key local export dsa ]{lang="EN-US"}**[\[ **name** *key-name* \] { **openssh** \| **ssh2** } \[ *filename* \]]{lang="EN-US"}]{#struct_0_x1871_x1914_849007714}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_206068081}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1871_x1914_1352746894}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_x605263609}

[[network-admin]{lang="EN-US"}]{#struct_0_x1871_x1914_x1223590876}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1871_x1914_x1528282171}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_x190827600}

[**[name ]{lang="EN-US"}***[key-name]{lang="EN-US"}*]{#struct_0_x1871_x1914_394173252}[：显示或导出指定本地]{style="font-family:宋体"}[DSA]{lang="EN-US"}[密钥对的主机公钥。]{style="font-family:宋体"}*[key-name]{lang="EN-US"}*[为本地密钥对的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，不区分大小写，字符串中可以包含字母、数字及"]{style="font-family:宋体"}[-]{lang="EN-US"}["。如果不指定本参数，则显示或导出默认名称的本地]{style="font-family:宋体"}[DSA]{lang="EN-US"}[密钥对的主机公钥。]{style="font-family:宋体"}

[**[openssh]{lang="EN-US"}**]{#struct_0_x1871_x1914_x6270401}[：主机公钥格式为]{style="font-family:宋体"}[OpenSSH]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ssh2]{lang="EN-US"}**]{#struct_0_x1871_x1914_x1994251625}[：主机公钥格式为]{style="font-family:宋体"}[SSH2.0]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[filename]{lang="EN-US"}*]{#struct_0_x1871_x1914_206002545}[：指定存储导出公钥的文件的名称，不区分大小写，取值不能为"]{style="font-family:宋体"}[hostkey]{lang="EN-US"}["，"]{style="font-family:宋体"}[serverkey]{lang="EN-US"}["，"]{style="font-family:宋体"}[dsakey]{lang="EN-US"}["和"]{style="font-family:宋体"}[ecdsakey]{lang="EN-US"}["，不能全部为"]{style="font-family:宋体"}[.]{lang="EN-US"}["，并且第一个字符不能为"]{style="font-family:宋体"}[/]{lang="EN-US"}["，不能包含字符"]{style="font-family:宋体"}[./]{lang="EN-US"}["和"]{style="font-family:宋体"}[../]{lang="EN-US"}["。不同型号的设备支持的文件名长度不同，请以设备的实际情况为准。文件名的详细介绍，请参见"基础配置指导"中的"文件系统管理"。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_x1405055401}

[[如果执行本命令时没有指定文件名，则按照指定格式显示本地]{style="font-family:宋体"}[DSA]{lang="EN-US"}]{#struct_0_x1871_x1914_274349902}[主机公钥；如果指定了文件名，则将本地]{style="font-family:宋体"}[DSA]{lang="EN-US"}[主机公钥导出到指定文件并保存。需要注意的是，不能将主机公钥导出到工作路径]{style="font-family:宋体"}[pkey]{lang="EN-US"}[目录以及]{style="font-family:宋体"}[pkey]{lang="EN-US"}[的子目录中。]{style="font-family:宋体"}

[[本命令用于采用从公钥文件中导入的方式将本地的主机公钥保存到远端设备上：]{style="font-family:宋体"}]{#struct_0_x1871_x1914_x1894166199}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在本地设备上执行]{lang="EN-US" style="font-family:宋体"}**[public-key local export]{lang="EN-US"}**]{#struct_0_x1871_x1914_x1718152259}[命令按照指定格式显示本地主机公钥（执行命令时不指定]{lang="EN-US" style="font-family:宋体"}*[filename]{lang="EN-US"}*[参数），通过拷贝粘贴等方式将显示的主机公钥保存到文件中，并将该文件上传到远端主机上。在远端主机上，执行]{lang="EN-US" style="font-family:宋体"}**[public-key peer]{lang="EN-US"}***[ ]{lang="EN-US"}***[import]{lang="EN-US"}**[ **sshkey**]{lang="EN-US"}[命令将本地的主机公钥保存到远端设备上。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在本地设备上执行]{lang="EN-US" style="font-family:宋体"}**[public-key local export]{lang="EN-US"}**]{#struct_0_x1871_x1914_984414484}[命令按照指定格式将本地主机公钥导出到指定文件（执行命令时指定]{lang="EN-US" style="font-family:宋体"}*[filename]{lang="EN-US"}*[参数），并将该文件上传到远端主机上。在远端主机上，执行]{lang="EN-US" style="font-family:宋体"}**[public-key peer]{lang="EN-US"}***[ ]{lang="EN-US"}***[import]{lang="EN-US"}**[ **sshkey**]{lang="EN-US"}[命令将本地的主机公钥保存到远端设备上。]{lang="EN-US" style="font-family:宋体"}

[[SSH2.0]{lang="EN-US"}]{#struct_0_x1871_x1914_355438423}[和]{style="font-family:宋体"}[OpenSSH]{lang="EN-US"}[是两种不同类型的公钥格式，用户需要根据服务器端支持的对端公钥格式，来选择导出的主机公钥格式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_1800751554}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_x44132311}[以]{style="font-family:宋体"}[OpenSSH]{lang="EN-US"}[格式导出默认名称的本地]{style="font-family:宋体"}[DSA]{lang="EN-US"}[密钥对的主机公钥，文件名为]{style="font-family:宋体"}[key.pub]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1871_x1914_206461297}

[\[Sysname\] public-key local export dsa openssh key.pub]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_1114255558}[以]{style="font-family:宋体"}[SSH2.0]{lang="EN-US"}[格式显示默认名称的本地]{style="font-family:宋体"}[DSA]{lang="EN-US"}[密钥对的主机公钥。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1871_x1914_x525114565}

[\[Sysname\] public-key local export dsa ssh2]{lang="EN-US"}

[\-\-\-- BEGIN SSH2 PUBLIC KEY \-\-\--]{lang="EN-US"}

[Comment: \"dsa-key-2011/05/12\"]{lang="EN-US"}

[AAAAB3NzaC1kc3MAAACBANdXJixFhMRMIR8YvZbl8GHE8KQj9/5ra4WzTO9yzhSg06UiL+CM7OZb5sJlhUiJ3B7b0T7IsnTan3W6Jsy5h3I2Anh+kiuoRCHyLDyJy5sG/WD+AZQd3Xf+axKJPadu68HRKNl/BnjXcitTQchQbzWCFLFqL6xLNolQOHgRx9ozAAAAFQDHcyGMc37I7pk7Ty3tMPSO2s6RXwAAAIEAgiaQCeFOxHS68pMuadOx8YUXrZWUGEzN/OrpbsTV75MTPoS0cJPFKyDNNdAkkrOVnsZJliW8T6UILiLFs3ThbdABMs5xsCAhcJGscXthI5HHbB+y6IMXwb2BcdQey4PiEMA8ybMugQVhwhYhxz1tqsAo9LFYXaf0JRlxjMmwnu8AAACAQZEs400SvNIVfnqxwvA7PvOVEA89tKni/f6GDBvWY9Z2Q499pAqUBtYcqQea8T4zBInxx2eF3lLaZJrIvAS205zXxSzQoU9190kakdMdasIjQLWYGyepFc3sTwmIflQeweUwLVAPaOesKaCERjxg+e4maYWlAvySGT4c9NJlxLo=]{lang="EN-US"}

[\-\-\-- END SSH2 PUBLIC KEY \-\-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_385232486}[以]{style="font-family:宋体"}[OpenSSH]{lang="EN-US"}[格式显示默认名称的本地]{style="font-family:宋体"}[DSA]{lang="EN-US"}[密钥对的主机公钥。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1871_x1914_1395935676}

[\[Sysname\] public-key local export dsa openssh]{lang="EN-US"}

[ssh-dss AAAAB3NzaC1kc3MAAACBANdXJixFhMRMIR8YvZbl8GHE8KQj9/5ra4WzTO9yzhSg06UiL+CM7OZb5sJlhUiJ3B7b0T7IsnTan3W6Jsy5h3I2Anh+kiuoRCHyLDyJy5sG/WD+AZQd3Xf+axKJPadu68HRKNl/BnjXcitTQchQbzWCFLFqL6xLNolQOHgRx9ozAAAAFQDHcyGMc37I7pk7Ty3tMPSO2s6RXwAAAIEAgiaQCeFOxHS68pMuadOx8YUXrZWUGEzN/OrpbsTV75MTPoS0cJPFKyDNNdAkkrOVnsZJliW8T6UILiLFs3ThbdABMs5xsCAhcJGscXthI5HHbB+y6IMXwb2BcdQey4PiEMA8ybMugQVhwhYhxz1tqsAo9LFYXaf0JRlxjMmwnu8AAACAQZEs400SvNIVfnqxwvA7PvOVEA89tKni/f6GDBvWY9Z2Q499pAqUBtYcqQea8T4zBInxx2eF3lLaZJrIvAS205zXxSzQoU9190kakdMdasIjQLWYGyepFc3sTwmIflQeweUwLVAPaOesKaCERjxg+e4maYWlAvySGT4c9NJlxLo= dsa-key]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_717731162}[以]{style="font-family:宋体"}[OpenSSH]{lang="EN-US"}[格式导出名称为]{style="font-family:宋体"}[dsa1]{lang="EN-US"}[的本地]{style="font-family:宋体"}[DSA]{lang="EN-US"}[密钥对的主机公钥，文件名为]{style="font-family:宋体"}[dsa1.pub]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1871_x1914_206395761}

[\[Sysname\] public-key local export dsa name dsa1 openssh dsa1.pub]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_1954379326}[以]{style="font-family:宋体"}[SSH2.0]{lang="EN-US"}[格式显示名称为]{style="font-family:宋体"}[dsa1]{lang="EN-US"}[的本地]{style="font-family:宋体"}[DSA]{lang="EN-US"}[密钥对的主机公钥。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1871_x1914_598168947}

[\[Sysname\] public-key local export dsa name dsa1 ssh2]{lang="EN-US"}

[\-\-\-- BEGIN SSH2 PUBLIC KEY \-\-\--]{lang="EN-US"}

[Comment: \"dsa-key-2011/05/12\"]{lang="EN-US"}

[AAAAB3NzaC1kc3MAAACBANdXJixFhMRMIR8YvZbl8GHE8KQj9/5ra4WzTO9yzhSg06UiL+CM7OZb5sJlhUiJ3B7b0T7IsnTan3W6Jsy5h3I2Anh+kiuoRCHyLDyJy5sG/WD+AZQd3Xf+axKJPadu68HRKNl/BnjXcitTQchQbzWCFLFqL6xLNolQOHgRx9ozAAAAFQDHcyGMc37I7pk7Ty3tMPSO2s6RXwAAAIEAgiaQCeFOxHS68pMuadOx8YUXrZWUGEzN/OrpbsTV75MTPoS0cJPFKyDNNdAkkrOVnsZJliW8T6UILiLFs3ThbdABMs5xsCAhcJGscXthI5HHbB+y6IMXwb2BcdQey4PiEMA8ybMugQVhwhYhxz1tqsAo9LFYXaf0JRlxjMmwnu8AAACBAKHkVsjaKtG7g7G98qGmtaboNkK0YEAkRdp+QDZxX0aPdmVeEU1GC3ES9XFD7gIK70pb+tB7dA+8scZNqKK85hkoNCFEXux3088NEYZullatZRH0km+DdpZ7CrcV+ft7UUvBF0FV3W4HOx/LOidJ5sX+qBAD4WcpSX0OrZEF4+dq]{lang="EN-US"}

[\-\-\-- END SSH2 PUBLIC KEY \-\-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_411907832}[以]{style="font-family:宋体"}[OpenSSH]{lang="EN-US"}[格式显示名称为]{style="font-family:宋体"}[dsa1]{lang="EN-US"}[的本地]{style="font-family:宋体"}[DSA]{lang="EN-US"}[密钥对的主机公钥。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1871_x1914_1124439288}

[\[Sysname\] public-key local export dsa name dsa1 openssh]{lang="EN-US"}

[ssh-dss AAAAB3NzaC1kc3MAAACBANdXJixFhMRMIR8YvZbl8GHE8KQj9/5ra4WzTO9yzhSg06UiL+CM7OZb5sJlhUiJ3B7b0T7IsnTan3W6Jsy5h3I2Anh+kiuoRCHyLDyJy5sG/WD+AZQd3Xf+axKJPadu68HRKNl/BnjXcitTQchQbzWCFLFqL6xLNolQOHgRx9ozAAAAFQDHcyGMc37I7pk7Ty3tMPSO2s6RXwAAAIEAgiaQCeFOxHS68pMuadOx8YUXrZWUGEzN/OrpbsTV75MTPoS0cJPFKyDNNdAkkrOVnsZJliW8T6UILiLFs3ThbdABMs5xsCAhcJGscXthI5HHbB+y6IMXwb2BcdQey4PiEMA8ybMugQVhwhYhxz1tqsAo9LFYXaf0JRlxjMmwnu8AAACBAKHkVsjaKtG7g7G98qGmtaboNkK0YEAkRdp+QDZxX0aPdmVeEU1GC3ES9XFD7gIK70pb+tB7dA+8scZNqKK85hkoNCFEXux3088NEYZullatZRH0km+DdpZ7CrcV+ft7UUvBF0FV3W4HOx/LOidJ5sX+qBAD4WcpSX0OrZEF4+dq dsa-key]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_x2096739113}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[public-key local create]{lang="EN-US"}**]{#struct_0_x1871_x1914_206330225}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[public-key peer]{lang="EN-US"}***[ ]{lang="EN-US"}***[import]{lang="EN-US"}**[ **sshkey**]{lang="EN-US"}]{#struct_0_x1871_x1914_436678617}
:::::

::: {#1644788807 .myid}
[]{#_Toc404792934}[]{#struct_0_x1871_x1914_570030801}

**公钥管理 \-- 公钥管理配置命令 \-- public-key local export rsa**

------------------------------------------------------------------------

[**[public-key local export rsa]{lang="EN-US"}**]{#struct_0_x1871_x1914_x830359585}[命令用来根据指定格式显示本地]{style="font-family:
宋体"}[RSA]{lang="EN-US"}[主机公钥或将其导出到指定文件。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_170988151}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_x1871_x1914_641701757}[模式下：]{style="font-family:宋体"}

[**[public-key local export rsa]{lang="EN-US"}**[ \[ **name** *key-name* \] { **openssh** \| **ssh1** \| **ssh2** } \[ *filename* \]]{lang="EN-US"}]{#struct_0_x1871_x1914_1684954170}

[[FIPS]{lang="EN-US"}]{#struct_0_x1871_x1914_x1802942277}[模式下：]{style="font-family:宋体"}

[**[public-key local export rsa]{lang="EN-US"}**[ \[ **name** *key-name* \] { **openssh** \| **ssh2** } \[ *filename* \]]{lang="EN-US"}]{#struct_0_x1871_x1914_1298133034}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_681769660}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1871_x1914_206264689}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_822608680}

[[network-admin]{lang="EN-US"}]{#struct_0_x1871_x1914_1415210035}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1871_x1914_1790903652}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_1931147703}

[**[name ]{lang="EN-US"}***[key-name]{lang="EN-US"}*]{#struct_0_x1871_x1914_x778455253}[：显示或导出指定本地]{style="font-family:宋体"}[RSA]{lang="EN-US"}[密钥对的主机公钥。]{style="font-family:宋体"}*[key-name]{lang="EN-US"}*[为本地密钥对的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，不区分大小写，字符串中可以包含字母、数字及"]{style="font-family:宋体"}[-]{lang="EN-US"}["。如果不指定本参数，则显示或导出默认名称的本地]{style="font-family:宋体"}[RSA]{lang="EN-US"}[密钥对的主机公钥。]{style="font-family:宋体"}

[**[openssh]{lang="EN-US"}**]{#struct_0_x1871_x1914_x123772844}[：主机公钥格式为]{style="font-family:宋体"}[OpenSSH]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ssh1]{lang="EN-US"}**]{#struct_0_x1871_x1914_x363271507}[：主机公钥格式为]{style="font-family:宋体"}[SSH1.5]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ssh2]{lang="EN-US"}**]{#struct_0_x1871_x1914_460035389}[：主机公钥格式为]{style="font-family:宋体"}[SSH2.0]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[filename]{lang="EN-US"}*]{#struct_0_x1871_x1914_206723441}[：指定存储导出公钥的文件的名称，不区分大小写，取值不能为"]{style="font-family:宋体"}[hostkey]{lang="EN-US"}["，"]{style="font-family:宋体"}[serverkey]{lang="EN-US"}["，"]{style="font-family:宋体"}[dsakey]{lang="EN-US"}["和"]{style="font-family:宋体"}[ecdsakey]{lang="EN-US"}["，不能全部为"]{style="font-family:宋体"}[.]{lang="EN-US"}["，并且第一个字符不能为"]{style="font-family:宋体"}[/]{lang="EN-US"}["，不能包含字符"]{style="font-family:宋体"}[./]{lang="EN-US"}["和"]{style="font-family:宋体"}[../]{lang="EN-US"}["。不同型号的设备支持的文件名长度不同，请以设备的实际情况为准。文件名的详细介绍，请参见"基础配置指导"中的"文件系统管理"。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_1750538614}

[[如果执行本命令时没有指定文件名，则显示本地]{style="font-family:宋体"}[RSA]{lang="EN-US"}]{#struct_0_x1871_x1914_x1245329084}[主机公钥；如果指定了文件名，则将本地]{style="font-family:宋体"}[RSA]{lang="EN-US"}[主机公钥导出到指定文件并保存。需要注意的是，不能将主机公钥导出到工作路径]{style="font-family:宋体"}[pkey]{lang="EN-US"}[目录以及]{style="font-family:宋体"}[pkey]{lang="EN-US"}[的子目录中。]{style="font-family:宋体"}

[[本命令用于采用从公钥文件中导入的方式将本地的主机公钥保存到远端设备上：]{style="font-family:宋体"}]{#struct_0_x1871_x1914_x1931178100}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在本地设备上执行]{lang="EN-US" style="font-family:宋体"}**[public-key local export]{lang="EN-US"}**]{#struct_0_x1871_x1914_787809935}[命令按照指定格式显示本地主机公钥（执行命令时不指定]{lang="EN-US" style="font-family:宋体"}*[filename]{lang="EN-US"}*[参数），将显示的主机公钥保存到文件中，并将该文件上传到远端主机上。在远端主机上，执行]{lang="EN-US" style="font-family:宋体"}**[public-key peer]{lang="EN-US"}***[ ]{lang="EN-US"}***[import]{lang="EN-US"}**[ **sshkey**]{lang="EN-US"}[命令将本地的主机公钥保存到远端设备上。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在本地设备上执行]{lang="EN-US" style="font-family:宋体"}**[public-key local export]{lang="EN-US"}**]{#struct_0_x1871_x1914_702218769}[命令按照指定格式将本地主机公钥导出到指定文件（执行命令时指定]{lang="EN-US" style="font-family:宋体"}*[filename]{lang="EN-US"}*[参数），并将该文件上传到远端主机上。在远端主机上，执行]{lang="EN-US" style="font-family:宋体"}**[public-key peer]{lang="EN-US"}***[ ]{lang="EN-US"}***[import]{lang="EN-US"}**[ **sshkey**]{lang="EN-US"}[命令将本地的主机公钥保存到远端设备上。]{lang="EN-US" style="font-family:宋体"}

[[SSH1.5]{lang="EN-US"}]{#struct_0_x1871_x1914_603301289}[、]{style="font-family:宋体"}[SSH2.0]{lang="EN-US"}[和]{style="font-family:宋体"}[OpenSSH]{lang="EN-US"}[是三种不同类型的公钥格式，用户需要根据服务器端支持的对端公钥格式，来选择导出的主机公钥格式。]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下只支持]{style="font-family:宋体"}[SSH2.0]{lang="EN-US"}[和]{style="font-family:宋体"}[OpenSSH]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_1160437973}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_1127187330}[以]{style="font-family:宋体"}[OpenSSH]{lang="EN-US"}[格式导出默认名称的本地]{style="font-family:宋体"}[RSA]{lang="EN-US"}[密钥对的主机公钥，文件名为]{style="font-family:宋体"}[key.pub]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1871_x1914_206657905}

[\[Sysname\] public-key local export rsa openssh key.pub]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_1769609012}[以]{style="font-family:宋体"}[SSH2.0]{lang="EN-US"}[格式显示默认名称的本地]{style="font-family:宋体"}[RSA]{lang="EN-US"}[密钥对的主机公钥。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1871_x1914_x1767169203}

[\[Sysname\] public-key local export rsa ssh2]{lang="EN-US"}

[\-\-\-- BEGIN SSH2 PUBLIC KEY \-\-\--]{lang="EN-US"}

[Comment: \"rsa-key-2011/05/12\"]{lang="EN-US"}

[AAAAB3NzaC1yc2EAAAADAQABAAAAgQDapKr+/gTCyWZyabuCJuJjMeMPQaj/kixzOCCAl+hDMmEGMrSfddq/bYcbgM7Buit1AgB3x0dFyTPi85DcCznTW4goPXAKFjuzCbGfj4chakSr+/aj1k3rM+XOvyvPJilneKJqhPT0xdv4tlas+mLNloY0dImbwS2kwE71rgg1CQ==]{lang="EN-US"}

[\-\-\-- END SSH2 PUBLIC KEY \-\-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_1456002113}[以]{style="font-family:宋体"}[OpenSSH]{lang="EN-US"}[格式显示默认名称的本地]{style="font-family:宋体"}[RSA]{lang="EN-US"}[密钥对的主机公钥。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1871_x1914_1887386586}

[\[Sysname\] public-key local export rsa openssh]{lang="EN-US"}

[ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQDapKr+/gTCyWZyabuCJuJjMeMPQaj/kixzOCCAl+hDMmEGMrSfddq/bYcbgM7Buit1AgB3x0dFyTPi85DcCznTW4goPXAKFjuzCbGfj4chakSr+/aj1k3rM+XOvyvPJilneKJqhPT0xdv4tlas+mLNloY0dImbwS2kwE71rgg1CQ== rsa-key]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_x2126487357}[以]{style="font-family:宋体"}[OpenSSH]{lang="EN-US"}[格式导出名称为]{style="font-family:宋体"}[rsa1]{lang="EN-US"}[的本地]{style="font-family:宋体"}[RSA]{lang="EN-US"}[密钥对的主机公钥，文件名为]{style="font-family:宋体"}[rsa1.pub]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1871_x1914_206199154}

[\[Sysname\] public-key local export rsa name rsa1 openssh rsa1.pub]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_x1001145703}[以]{style="font-family:宋体"}[SSH2.0]{lang="EN-US"}[格式显示名称为]{style="font-family:宋体"}[rsa1]{lang="EN-US"}[的本地]{style="font-family:宋体"}[RSA]{lang="EN-US"}[密钥对的主机公钥。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1871_x1914_x2116406638}

[\[Sysname\] public-key local export rsa name rsa1 ssh2]{lang="EN-US"}

[\-\-\-- BEGIN SSH2 PUBLIC KEY \-\-\--]{lang="EN-US"}

[Comment: \"rsa-key-2011/05/12\"]{lang="EN-US"}

[AAAAB3NzaC1yc2EAAAADAQABAAAAgQDevEbyF93xHUJucJWqRc1r8fhzQ9lSVprCI6ATZeDYyR1J00fBQ8XY+q2olqoagn5YDyUC8ZJvUhlyMOHeORpkAVxD3XncTp4XG66h3rTHHa7Xmm7f1GDYlF0n05t8mCLVaupbfCzP8ba8UkrUmMO4fUvW6zavA5LYxtlAiQv0KQ==]{lang="EN-US"}

[\-\-\-- END SSH2 PUBLIC KEY \-\-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_484985930}[以]{style="font-family:宋体"}[OpenSSH]{lang="EN-US"}[格式显示名称为]{style="font-family:宋体"}[rsa1]{lang="EN-US"}[的本地]{style="font-family:宋体"}[RSA]{lang="EN-US"}[密钥对的主机公钥。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1871_x1914_x1598732578}

[\[Sysname\] public-key local export rsa name rsa1 openssh]{lang="EN-US"}

[ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQDevEbyF93xHUJucJWqRc1r8fhzQ9lSVprCI6ATZeDYyR1J00fBQ8XY+q2olqoagn5YDyUC8ZJvUhlyMOHeORpkAVxD3XncTp4XG66h3rTHHa7Xmm7f1GDYlF0n05t8mCLVaupbfCzP8ba8UkrUmMO4fUvW6zavA5LYxtlAiQv0KQ== rsa-key]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_701855936}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[public-key local create]{lang="EN-US"}**]{#struct_0_x1871_x1914_1733958463}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[public-key peer]{lang="EN-US"}***[ ]{lang="EN-US"}***[import]{lang="EN-US"}**[ **sshkey**]{lang="EN-US"}]{#struct_0_x1871_x1914_206133618}
:::

::: {#787258782 .myid}
[]{#_Toc404792935}[]{#struct_0_x1871_x1914_536019538}[]{#_Toc195409929}[]{#_Toc149979608}[]{#_Toc144810344}[]{#_Toc287539394}[]{#_Toc211842743}[]{#_Toc213475567}[]{#_Toc211842744}[]{#_Toc213475568}[]{#_Toc211842745}[]{#_Toc213475569}[]{#_Toc211842746}[]{#_Toc213475570}[]{#_Toc211842747}[]{#_Toc213475571}[]{#_Toc211842748}[]{#_Toc213475572}[]{#_Toc211842749}[]{#_Toc213475573}[]{#_Toc211842750}[]{#_Toc213475574}[]{#_Toc211842751}[]{#_Toc213475575}[]{#_Toc211842752}[]{#_Toc213475576}[]{#_Toc211842753}[]{#_Toc213475577}[]{#_Toc211842754}[]{#_Toc213475578}[]{#_Toc211842755}[]{#_Toc213475579}[]{#_Toc211842756}[]{#_Toc213475580}[]{#_Toc211842757}[]{#_Toc213475581}[]{#_Toc211842758}[]{#_Toc213475582}[]{#_Toc211842759}[]{#_Toc213475583}[]{#_Toc211842760}[]{#_Toc213475584}[]{#_Toc211842761}[]{#_Toc213475585}[]{#_Toc211842762}[]{#_Toc213475586}[]{#_Toc211842763}[]{#_Toc213475587}[]{#_Toc211842764}[]{#_Toc213475588}[]{#_Toc211842765}[]{#_Toc213475589}[]{#_Toc211842766}[]{#_Toc213475590}[]{#_Toc211842767}[]{#_Toc213475591}[]{#_Toc211842771}[]{#_Toc213475595}[]{#_Toc211842772}[]{#_Toc213475596}[]{#_Toc211842773}[]{#_Toc213475597}[]{#_Toc211842774}[]{#_Toc213475598}[]{#_Toc211842775}[]{#_Toc213475599}

**公钥管理 \-- 公钥管理配置命令 \-- public-key peer**

------------------------------------------------------------------------

[**[public-key peer]{lang="EN-US"}**]{#struct_0_x1871_x1914_948275640}[命令用来指定远端主机公钥的名称，并进入公钥视图。]{style="font-family:宋体"}

[**[undo public-key peer]{lang="EN-US"}**]{#struct_0_x1871_x1914_x1898086833}[命令用来删除指定的远端主机公钥。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_1219383946}

[**[public-key peer ]{lang="EN-US"}***[keyname]{lang="EN-US"}*]{#struct_0_x1871_x1914_x1916688525}

[**[undo public-key peer]{lang="EN-US"}**[ *keyname*]{lang="EN-US"}]{#struct_0_x1871_x1914_771786866}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_900960640}

[[设备上不存在任何远端主机公钥。]{style="font-family:宋体"}]{#struct_0_x1871_x1914_2034969222}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_206068082}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1871_x1914_1352746891}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_x604935929}

[[network-admin]{lang="EN-US"}]{#struct_0_x1871_x1914_1132542159}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1871_x1914_x267387477}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_1192841511}

[*[keyname]{lang="EN-US"}*]{#struct_0_x1871_x1914_x2087722231}[：远端主机公钥的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_798366247}

[[进入公钥视图后，可以开始输入公钥数据。在输入公钥数据时，字符之间可以有空格，也可以按回车键继续输入数据。保存公钥数据时，将删除空格和回车符。]{style="font-family:宋体"}]{#struct_0_x1871_x1914_x1348045939}

[[通过手工配置方式创建远端主机公钥时，用户需要事先获取并记录远端主机十六进制形式的公钥，并在本地设备上执行以下操作：]{style="font-family:宋体"}]{#struct_0_x1871_x1914_206002546}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[执行本命令进入公钥视图。]{style="font-family:宋体"}]{#struct_0_x1871_x1914_x1405055400}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[在公钥视图，手工输入远端主机的公钥。]{style="font-family:宋体"}]{#struct_0_x1871_x1914_1840433843}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[执行]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1871_x1914_x575942989}**[peer-public-key]{lang="SV"}**[ **end**]{lang="SV"}[命令，保存输入的远端主机公钥，并从公钥视图退回到系统视图。]{lang="EN-US" style="font-family:宋体"}

[[需要注意的是，输入的公钥数据必须满足一定的格式要求。通过]{style="font-family:宋体"}**[display public-key local public]{lang="EN-US"}**]{#struct_0_x1871_x1914_x1961169887}[命令显示的公钥可以作为输入的公钥数据。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_1521769859}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_1029262572}[指定远端主机公钥名称为]{style="font-family:宋体"}[key1]{lang="EN-US"}[，并进入公钥视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1871_x1914_x595714727}

[\[Sysname\] public-key peer key1]{lang="EN-US"}

[\[Sysname-pkey-public-key-key1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_969472177}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display public-key local public]{lang="EN-US"}**]{#struct_0_x1871_x1914_206461298}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display public-key peer]{lang="EN-US"}**]{#struct_0_x1871_x1914_1114255547}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer-public-key]{lang="SV"}**]{#struct_0_x1871_x1914_x525835460}[ **end**]{lang="SV"}
:::

::: {#245361319 .myid}
[]{#_Toc404792936}[]{#struct_0_x1871_x1914_1162454024}[]{#_Toc195409930}

**公钥管理 \-- 公钥管理配置命令 \-- public-key peer import sshkey**

------------------------------------------------------------------------

[**[public-key peer]{lang="EN-US"}***[ ]{lang="EN-US"}***[import]{lang="EN-US"}**[ **sshkey**]{lang="EN-US"}]{#struct_0_x1871_x1914_975906230}[命令用来配置从公钥文件中导入远端主机的公钥。]{style="font-family:宋体"}

[**[undo public-key peer]{lang="EN-US"}**]{#struct_0_x1871_x1914_x1393927838}[命令用来删除指定的远端主机公钥。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_2112495785}

[**[public-key peer ]{lang="EN-US"}***[keyname ]{lang="EN-US"}***[import]{lang="EN-US"}**[ **sshkey** *filename*]{lang="EN-US"}]{#struct_0_x1871_x1914_x1948887311}

[**[undo public-key peer ]{lang="EN-US"}***[keyname]{lang="EN-US"}*]{#struct_0_x1871_x1914_2002737950}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_206395762}

[[设备上不存在任何远端主机公钥。]{style="font-family:宋体"}]{#struct_0_x1871_x1914_1954379325}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_598234483}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1871_x1914_x941999872}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_1534798625}

[[network-admin]{lang="EN-US"}]{#struct_0_x1871_x1914_1233172879}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1871_x1914_1011875381}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_x832019978}

[*[keyname]{lang="EN-US"}*]{#struct_0_x1871_x1914_x317058583}[：远端主机公钥的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[*[filename]{lang="EN-US"}*]{#struct_0_x1871_x1914_206330226}[：指定导入公钥数据的文件名，不区分大小写，取值不能为"]{style="font-family:宋体"}[hostkey]{lang="EN-US"}["，"]{style="font-family:宋体"}[serverkey]{lang="EN-US"}["，"]{style="font-family:宋体"}[dsakey]{lang="EN-US"}["和"]{style="font-family:宋体"}[ecdsakey]{lang="EN-US"}["，不能全部为"]{style="font-family:宋体"}[.]{lang="EN-US"}["，并且第一个字符不能为"]{style="font-family:宋体"}[/]{lang="EN-US"}["，不能包含字符"]{style="font-family:宋体"}[./]{lang="EN-US"}["和"]{style="font-family:宋体"}[../]{lang="EN-US"}["。不同型号的设备支持的文件名长度不同，请以设备的实际情况为准。文件名的详细介绍，请参见"基础配置指导"中的"文件系统管理"。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_436678620}

[[执行本命令后，系统会对指定公钥文件中的公钥进行格式转换，将其转换为]{style="font-family:宋体"}[PKCS]{lang="EN-US"}]{#struct_0_x1871_x1914_x1386284336}[标准编码格式，并将该远端主机的公钥保存到本地设备。]{style="font-family:宋体"}

[[从公钥文件中导入远端主机的公钥前，需要远端主机将其公钥保存到公钥文件中，并将该公钥文件上传到本地设备。例如，在远端主机上执行]{style="font-family:宋体"}**[public-key local export]{lang="EN-US"}**]{#struct_0_x1871_x1914_854551485}[命令将其公钥导出到公钥文件中，并通过]{style="font-family:宋体"}[FTP]{lang="EN-US"}[或]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[，以二进制方式将该公钥文件保存到本地设备。]{style="font-family:宋体"}

[[目前，非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_x1871_x1914_148933290}[模式下，设备支持的公钥格式为]{style="font-family:宋体"}[SSH1.5]{lang="EN-US"}[、]{style="font-family:宋体"}[SSH2.0]{lang="EN-US"}[和]{style="font-family:宋体"}[OpenSSH]{lang="EN-US"}[；]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，设备支持的格式为]{style="font-family:宋体"}[SSH2.0]{lang="EN-US"}[和]{style="font-family:宋体"}[OpenSSH]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_1931316831}

[[\# ]{lang="EN-US"}]{#struct_0_x1871_x1914_x1144312821}[配置从公钥文件]{style="font-family:宋体"}[key.pub]{lang="EN-US"}[中导入远端主机的公钥，公钥名称为]{style="font-family:宋体"}[key2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1871_x1914_721441120}

[\[Sysname\] public-key peer key2 import sshkey key.pub]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1871_x1914_x1960872416}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display public-key peer]{lang="EN-US"}**]{#struct_0_x1871_x1914_206264690}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[public-key local export dsa]{lang="EN-US"}**]{#struct_0_x1871_x1914_x1133706449}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[public-key local export rsa]{lang="EN-US"}**]{#struct_0_x1871_x1914_x1439252412}
:::
