::: {#-942228800 .myid}
[]{#_Toc404793947}[]{#struct_0_13054_x1190_x118590428}[]{#_Toc123629825}

**加密引擎 \-- 加密引擎调试命令 \-- debugging crypto-engine**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_13054_x1190_1162334844}

[**[debugging crypto-engine]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_13054_x1190_x539941289}

[**[undo debugging crypto-engine ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_13054_x1190_x172003740}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13054_x1190_359757362}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13054_x1190_x81914605}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13054_x1190_301710157}

[[network-admin]{lang="EN-US"}]{#struct_0_13054_x1190_805472240}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13054_x1190_323835233}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13054_x1190_549385581}

[**[all]{lang="EN-US"}**]{#struct_0_13054_x1190_x2140888047}[：表示加密引擎所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_13054_x1190_x573989093}[：表示加密引擎错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_13054_x1190_1654253943}[：表示加密引擎事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_13054_x1190_1520355205}[：表示加密引擎报文调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_13054_x1190_x1299589583}

[[debugging crypto-engine]{lang="EN-US"}]{#struct_0_13054_x1190_x81586925}[命令用来打开]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}[undo debugging crypto-engine]{lang="EN-US"}[命令用来关闭加密引擎调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，加密引擎的调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_13054_x1190_573375321}

[[表1-1 ]{lang="EN-US"}[debugging crypto-engine error]{lang="EN-US"}]{#struct_0_13054_x1190_x1072400041}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1188224872}[[字段]{style="font-family:黑体"}]{#struct_0_13054_x1190_1615759143}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13054_x1190_1240085756}

[[Failed to insert crypto engine, can\'t alloc driver structure.]{lang="EN-US"}]{#struct_0_13054_x1190_325182984}

[[插入加密引擎失败，无法创建驱动结构]{style="font-family:宋体"}]{#struct_0_13054_x1190_1229278048}

[[Failed to insert crypto engine, can\'t insert driver struct into driver array.]{lang="EN-US"}]{#struct_0_13054_x1190_1564268798}

[[插入加密引擎失败，无法将驱动结构插入驱动数组]{style="font-family:宋体"}]{#struct_0_13054_x1190_x81521389}

[[Failed to create new session in driver, driver ID=*driver-id*.]{lang="EN-US"}]{#struct_0_13054_x1190_1452766241}

[[驱动新建会话失败，驱动编号为]{style="font-family:宋体"}*[driver-id]{lang="EN-US"}*]{#struct_0_13054_x1190_1369336082}

[[Failed to add session to session array.]{lang="EN-US"}]{#struct_0_13054_x1190_x376631415}

[[将会话加入会话数组失败]{style="font-family:宋体"}]{#struct_0_13054_x1190_x1612870107}

[[Failed to allocate session, algorithm ID=*alg-id*.]{lang="EN-US"}]{#struct_0_13054_x1190_1852240672}

[[创建会话失败，算法]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_13054_x1190_x82111212}[为]{style="font-family:宋体"}*[alg-id]{lang="EN-US"}*

[[Failed to select crypto engine, flag=*flag-id*.]{lang="EN-US"}]{#struct_0_13054_x1190_x718870007}

[[选择加密引擎失败，加密引擎标识为]{style="font-family:宋体"}*[flag-id]{lang="EN-US"}*]{#struct_0_13054_x1190_1504498464}

[[First algorithm: algorithm ID=*alg-id*, required hash length =*hash-len*, key length=*key-len*.]{lang="EN-US"}]{#struct_0_13054_x1190_593938491}

[[第一个算法：算法]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_13054_x1190_x167169585}[为]{style="font-family:宋体"}*[alg-id]{lang="EN-US"}*[，需要的哈希长度为]{style="font-family:宋体"}*[hash-len]{lang="EN-US"}*[，密钥长度为]{style="font-family:宋体"}*[key-len]{lang="EN-US"}*

[[Second algorithm: algorithm ID=*alg-id*, required hash length=*hash-len*, key length=*key-len*.]{lang="EN-US"}]{#struct_0_13054_x1190_x749539204}

[[第二个算法：算法]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_13054_x1190_x82045676}[为]{style="font-family:宋体"}*[alg-id]{lang="EN-US"}*[，需要的哈希长度为]{style="font-family:宋体"}*[hash-len]{lang="EN-US"}*[，密钥长度为]{style="font-family:宋体"}*[key-len]{lang="EN-US"}*

[[Can\'t get session during symmetric encryption, session handle=*session-id*.]{lang="EN-US"}]{#struct_0_13054_x1190_x306833368}

[[对称加密过程中找不到会话，会话句柄为]{style="font-family:宋体"}*[session-id]{lang="EN-US"}*]{#struct_0_13054_x1190_x112689847}

[[Can\'t get driver during symmetric encryption, driver ID=*drv-id*, session handle=*session-id*.]{lang="EN-US"}]{#struct_0_13054_x1190_1192362784}

[[对称加密过程中找不到驱动，驱动]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_13054_x1190_x134778990}[为]{style="font-family:宋体"}*[drv-id]{lang="EN-US"}*[会话句柄为]{style="font-family:宋体"}*[session-id]{lang="EN-US"}*

[[Failed to reselect crypto engine, original driver ID=*drv-id*, session handle=*session-id*.]{lang="EN-US"}]{#struct_0_13054_x1190_x82242284}

[[重新选择加密引擎失败，原始驱动]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_13054_x1190_x432280942}[为]{style="font-family:宋体"}*[drv-id]{lang="EN-US"}*[会话句柄为]{style="font-family:宋体"}*[session-id]{lang="EN-US"}*

[[Failed to check symmetric Job, driver ID=*drv-id*.]{lang="EN-US"}]{#struct_0_13054_x1190_1244062189}

[[检查对称]{style="font-family:宋体"}[job]{lang="EN-US"}]{#struct_0_13054_x1190_454711960}[失败，驱动]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[drv-id]{lang="EN-US"}*

[[First describer: algorithm ID=*alg-id*, required hash length=*hash-len*, skip length=*skip-len*, process length=*process-len*, inject position=*inject-position*, flag=*flag*, key length=*key-len*.]{lang="EN-US"}]{#struct_0_13054_x1190_1914783716}

[[第一个描述符：算法]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_13054_x1190_426485492}[为]{style="font-family:宋体"}*[alg-id]{lang="EN-US"}*[，需要的哈希长度为]{style="font-family:宋体"}*[hash-len]{lang="EN-US"}*[，跳过的长度为]{style="font-family:宋体"}*[skip-len]{lang="EN-US"}*[，处理的长度为]{style="font-family:宋体"}*[process-len]{lang="EN-US"}*[，插入的位置为]{style="font-family:宋体"}*[inject-position]{lang="EN-US"}*[，标识为]{style="font-family:宋体"}*[flag]{lang="EN-US"}*[，密钥长度为]{style="font-family:宋体"}*[key-len]{lang="EN-US"}*

[[Second describer: algorithm ID=*alg-id*, required hash length=*hash-len*, skip length=*skip-len*, process length=*process-len*, inject position=*inject-position*,flag=*flag*, key length=*key-len*.]{lang="EN-US"}]{#struct_0_13054_x1190_x82176748}

[[第二个描述符：算法]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_13054_x1190_1243253992}[为]{style="font-family:宋体"}*[alg-id]{lang="EN-US"}*[，需要的哈希长度为]{style="font-family:宋体"}*[hash-len]{lang="EN-US"}*[，跳过的长度为]{style="font-family:宋体"}*[skip-len]{lang="EN-US"}*[，处理的长度为]{style="font-family:宋体"}*[process-len]{lang="EN-US"}*[，插入的位置为]{style="font-family:宋体"}*[inject-position]{lang="EN-US"}*[，标识为]{style="font-family:宋体"}*[flag]{lang="EN-US"}*[，密钥长度为]{style="font-family:宋体"}*[key-len]{lang="EN-US"}*

[[Symmetric Job: data type=*type*, input buffer length=*input-buff-len*, output buffer length=*output-buff-len*.]{lang="EN-US"}]{#struct_0_13054_x1190_1781190516}

[[对称]{style="font-family:宋体"}[Job]{lang="EN-US"}]{#struct_0_13054_x1190_x937461935}[：数据类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*[，输入缓冲区的长度]{style="font-family:宋体"}*[input-buff-len]{lang="EN-US"}*[，]{style="font-family:宋体"} [输出缓冲区的长度为]{style="font-family:宋体"}*[output-buff-len]{lang="EN-US"}*

[[Failed to insert crypto engine, invalid engine flag=*flag*, name=*drv-name*.]{lang="EN-US"}]{#struct_0_13054_x1190_x81849068}

[[插入加密引擎失败，无效的加密引擎标识为]{style="font-family:宋体"}*[flag]{lang="EN-US"}*]{#struct_0_13054_x1190_1530974885}[，加密引擎名字为]{style="font-family:宋体"}*[drv-name]{lang="EN-US"}*

[[Failed to remove crypto engine *engine-name*, invalid engine id=*engine-id*.]{lang="EN-US"}]{#struct_0_13054_x1190_427770255}

[[拔除加密引擎]{style="font-family:宋体"}*[engine-name]{lang="EN-US"}*]{#struct_0_13054_x1190_x587527774}[失败，无效的加密引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[engine-id]{lang="EN-US"}*[、]{style="font-family:宋体"}

[[Failed to register software crypto engine.]{lang="EN-US"}]{#struct_0_13054_x1190_x783506784}

[[注册软件加密引擎失败]{style="font-family:宋体"}]{#struct_0_13054_x1190_x81783532}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging crypto engine event]{lang="EN-US"}]{#struct_0_13054_x1190_x281988876}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1165968008}[[字段]{style="font-family:黑体"}]{#struct_0_13054_x1190_747544690}

[[描述]{style="font-family:黑体"}]{#struct_0_13054_x1190_571528767}

[[New session created on crypto engine(ID =*engine-id*), flag=*flag*.]{lang="EN-US"}]{#struct_0_13054_x1190_1035167992}

[[新会话已成功在加密引擎]{style="font-family:宋体"}*[engine-id]{lang="EN-US"}*]{#struct_0_13054_x1190_x1681803484}[上创建，标识为]{style="font-family:宋体"}*[flag]{lang="EN-US"}*

[[Crypto engine *engine-name* inserted, driver ID=*driver-id*.]{lang="EN-US"}]{#struct_0_13054_x1190_x1116365670}

[[加密引擎]{style="font-family:宋体"}*[engine-name]{lang="EN-US"}*]{#struct_0_13054_x1190_x81980140}[插入成功，驱动]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[driver-id]{lang="EN-US"}*

[[Crypto engine(ID =*engine-id*) is removed.]{lang="EN-US"}]{#struct_0_13054_x1190_x51028346}

[[加密引擎]{style="font-family:宋体"}*[engine-id]{lang="EN-US"}*]{#struct_0_13054_x1190_x118590429}[已被拔出]{style="font-family:宋体"}

[[First algorithm: algorithm ID=*alg-id*, required hash length=*hash-len*, key length=*key-len*.]{lang="EN-US"}]{#struct_0_13054_x1190_1162269308}

[[第一个算法：算法]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_13054_x1190_x540597295}[为]{style="font-family:宋体"}*[alg-id]{lang="EN-US"}*[，需要的哈希长度为]{style="font-family:宋体"}*[hash-len]{lang="EN-US"}*[，密钥长度为]{style="font-family:宋体"}*[key-len]{lang="EN-US"}*

[[Second algorithm: algorithm ID=*alg-id*, required hash length=*hash-len*, key length=*key-len*.]{lang="EN-US"}]{#struct_0_13054_x1190_1525860910}

[[第二个算法：算法]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_13054_x1190_x81914604}[为]{style="font-family:宋体"}*[alg-id]{lang="EN-US"}*[，需要的哈希长度为]{style="font-family:宋体"}*[hash-len]{lang="EN-US"}*[，密钥长度为]{style="font-family:宋体"}*[key-len]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging crypto engine packet]{lang="EN-US"}]{#struct_0_13054_x1190_301710156}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1162014472}[]{#struct_0_13054_x1190_805472239}[]{#_Toc277669731}[]{#_Toc277669732}[]{#_Toc277669735}[]{#_Toc277669736}[]{#_Toc277669737}[]{#_Toc277669738}[]{#_Toc277669739}[]{#_Toc277669740}[]{#_Toc277669741}[]{#_Toc277669742}[]{#_Toc277669743}[]{#_Toc277669744}[]{#_Toc277669745}[]{#_Toc277669746}[]{#_Toc277669795}[]{#_Toc277669796}[]{#_Toc277669824}[]{#_Toc277669825}[]{#_Toc277669845}[]{#_Toc277669846}[]{#_Toc277669865}[]{#_Toc277669866}[]{#_Toc277669867}[]{#_Toc277669868}[]{#_Toc277669869}[]{#_Toc277669871}[]{#_Toc277669872}[]{#_Toc277669873}[]{#_Toc277669874}[]{#_Toc277669879}[]{#_Toc277669883}[]{#_Toc277669887}[]{#_Toc277669888}[]{#_Toc277669891}[]{#_Toc277669892}[]{#_Toc277669894}[]{#_Toc277669899}[]{#_Toc277669900}[]{#_Toc277669901}[]{#_Toc277669902}[]{#_Toc277669903}[]{#_Toc277669904}[]{#_Toc277669905}[]{#_Toc277669906}[]{#_Toc277669907}[]{#_Toc277669908}[]{#_Toc277669910}[]{#_Toc277669912}[]{#_Toc277669916}[]{#_Toc277669920}[]{#_Toc277669921}[]{#_Toc277669924}[]{#_Toc277669925}[]{#_Toc277669926}[]{#_Toc277669927}[]{#_Toc277669930}[]{#_Toc277669931}[]{#_Toc277669932}[]{#_Toc277669933}[]{#_Toc277669934}[]{#_Toc277669935}[]{#_Toc277669936}[]{#_Toc277669937}[]{#_Toc277669938}[]{#_Toc277669939}[]{#_Toc277669940}[]{#_Toc277669941}[]{#_Toc277669990}[]{#_Toc277669991}[]{#_Toc277670043}[]{#_Toc277670044}[]{#_Toc277670067}[]{#_Toc277670068}[]{#_Toc277670087}[]{#_Toc277670088}[]{#_Toc277670089}[]{#_Toc277670090}[]{#_Toc277670091}[]{#_Toc277670092}[]{#_Toc277670095}[]{#_Toc277670097}[]{#_Toc277670098}[]{#_Toc277670099}[]{#_Toc277670100}[]{#_Toc277670105}[]{#_Toc277670109}[]{#_Toc277670115}[]{#_Toc277670119}[]{#_Toc277670122}[]{#_Toc277670127}[]{#_Toc277670128}[]{#_Toc277670129}[]{#_Toc277670131}[]{#_Toc277670133}[]{#_Toc277670134}[]{#_Toc277670138}[]{#_Toc277670139}[]{#_Toc277670140}[]{#_Toc277670141}[]{#_Toc277670142}[]{#_Toc277670143}[]{#_Toc277670144}[]{#_Toc277670145}[]{#_Toc277670149}[]{#_Toc277670150}[]{#_Toc277670153}[]{#_Toc277670157}[]{#_Toc277670161}[]{#_Toc277670162}[字段]{style="font-family:黑体"}

[[描述]{style="font-family:黑体"}]{#struct_0_13054_x1190_1515476312}

[[Symmetric encryption: Job doesn\'t contain key, previous crypto engine ID=*engine-id*.]{lang="EN-US"}]{#struct_0_13054_x1190_795798999}

[[对称加密：任务缺少密钥。之前使用的加密引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_13054_x1190_x1094632278}[为]{style="font-family:宋体"}*[engine-id]{lang="EN-US"}*

[[Symmetric encryption: Reselecting crypto engine failed, previous crypto engine ID=*engine-id*.]{lang="EN-US"}]{#struct_0_13054_x1190_1799316018}

[[对称加密：重新选择加密引擎失败。之前使用的加密引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_13054_x1190_x81586924}[为]{style="font-family:宋体"}*[engine-id]{lang="EN-US"}*

[[Symmetric encryption: New crypto engine failed to create session, first algorithm ID=*alg-id*, crypto engine ID=*engine-id*.]{lang="EN-US"}]{#struct_0_13054_x1190_573375322}

[[对称加密：新加密引擎创建会话失败。第一个算法]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_13054_x1190_x1072400042}[为]{style="font-family:宋体"}*[alg-id]{lang="EN-US"}*[，加密引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[engine-id]{lang="EN-US"}*

[[Symmetric encryption: Reselecting crypto engine successfully, previous crypto engine ID=*old-engine-id*, new crypto engine ID=*new-engine-id*,.]{lang="EN-US"}]{#struct_0_13054_x1190_2019043670}

[[对称加密：重新选择加密引擎成功。之前的加密引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_13054_x1190_x1338729766}[为]{style="font-family:宋体"}*[old-engine-id]{lang="EN-US"}*[，新加密引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[new-engine-id]{lang="EN-US"}*

[[Symmetric operation finished, driver return= *return-code*, driver ID=*driver-id*, driver flag =*driver-flag*.]{lang="EN-US"}]{#struct_0_13054_x1190_1396944785}

[[对称算法操作完成，驱动返回值为]{style="font-family:宋体"}[\[*return-code*]{lang="EN-US"}]{#struct_0_13054_x1190_993339898}[，驱动]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[driver-id]{lang="EN-US"}*[，驱动标识为]{style="font-family:宋体"}*[driver-flag]{lang="EN-US"}*

[[Job validity check failed, algorithm ID=*alg-id*, base length=*base-len*, mod length=*mod*, exp length=*exp-leng*, out buffer length =*outbuff-len*, flag=*flag*\].]{lang="EN-US"}]{#struct_0_13054_x1190_x81521388}

[[任务合法性检查失败：算法]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_13054_x1190_1452766242}[为]{style="font-family:宋体"}*[alg-id]{lang="EN-US"}*[，基数长度为]{style="font-family:宋体"}*[base-length]{lang="EN-US"}*[，模为]{style="font-family:宋体"}*[mod]{lang="EN-US"}*[，指数长度为]{style="font-family:宋体"}*[exp-length]{lang="EN-US"}*[，输出缓冲区长度为]{style="font-family:宋体"}*[outbuff-len]{lang="EN-US"}*[，标识为]{style="font-family:宋体"}*[flag]{lang="EN-US"}*

[[Asymmetric encryption failed: Can't select a crypto engine, algorithm ID=*alg-id*, flag=*flag*.]{lang="EN-US"}]{#struct_0_13054_x1190_1369532690}

[[非对称加密失败：无法选择加密引擎，使用算法]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_13054_x1190_1210268776}[为]{style="font-family:宋体"}*[alg]{lang="EN-US"}[，]{style="font-family:宋体"}*[标识为]{style="font-family:宋体"}*[flag]{lang="EN-US"}*

[[Asymmetric operation finished, base length=*base-len*, mod length=*mod*, exp length=*exp-len*, driver return=*return-code*.]{lang="EN-US"}]{#struct_0_13054_x1190_x2136036800}

[[非对称加密完成，基数长度为]{style="font-family:宋体"}*[base-len]{lang="EN-US"}*]{#struct_0_13054_x1190_x1173047737}[，模为]{style="font-family:宋体"}*[mod]{lang="EN-US"}*[，指数长度为]{style="font-family:宋体"}*[exp-len]{lang="EN-US"}*[，驱动返回值为]{style="font-family:宋体"}*[driver-return]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13054_x1190_x1997806374}

[[\# ]{lang="EN-US"}]{#struct_0_13054_x1190_x605400176}[在设备上插入一个硬件加密引擎，并打开加密引擎错误调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging crypto-engine error]{lang="EN-US"}]{#struct_0_13054_x1190_x1992887960}

[\* Dec 16 14:40:24:162 2012 Sysname CCF/7/Error: -MDC=1;]{lang="EN-US"}

[Failed to insert crypto engine, can\'t allocate driver structure.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13054_x1190_x1311644333}*[插入加密引擎失败，无法分配驱动结构]{style="font-family:宋体"}*

*[ ]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_13054_x1190_x231476411}[在设备上配置手工方式的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略]{style="font-family:宋体"}[mypolicy]{lang="EN-US"}[，并打开加密引擎事件调试信息开关。当将策略]{style="font-family:宋体"}[mypolicy]{lang="EN-US"}[应用于接口]{style="font-family:宋体"}[Ethernet1/2]{lang="EN-US"}[上时，会生成]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[，输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging crypto-engine event]{lang="EN-US"}]{#struct_0_13054_x1190_x816318116}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] interface ethernet 1/2]{lang="EN-US"}

[\[Sysname-Ethernet1/2\] ipsec policy mypolicy]{lang="EN-US"}

[\*Dec 16 16:44:24:162 2012 Sysname CCF/7/event: ]{lang="EN-US"}

[New session created on crypto engine(ID=00), flag=21.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13054_x1190_x1997871910}*[新会话成功在加密引擎]{style="font-family:宋体"}[0]{lang="EN-US"}[上建立，加密引擎标识为]{style="font-family:宋体"}[21]{lang="EN-US"}*

[[\*Dec 16 16:44:24:162 2012 Sysname Sysname /7/event: ]{lang="EN-US"}]{#struct_0_13054_x1190_x1404827843}

[First algorithm: algorithm ID=4, required hash length=0, key length=24.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13054_x1190_x496546240}*[第一个算法：算法]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[4]{lang="EN-US"}[，需要的哈希长度为]{style="font-family:宋体"}[0]{lang="EN-US"}[，密钥长度为]{style="font-family:宋体"}[24]{lang="EN-US"}*

[[\*Dec 16 16:44:24:162 2012 Sysname CCF/7/event: ]{lang="EN-US"}]{#struct_0_13054_x1190_1089408832}

[Second algorithm: algorithm ID=17, required hash length=12, key length=20.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13054_x1190_1072222743}*[第二个算法：算法]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[17]{lang="EN-US"}[，需要的哈希长度为]{style="font-family:宋体"}[12]{lang="EN-US"}[，密钥长度为]{style="font-family:宋体"}[20]{lang="EN-US"}*

[[\*Dec 16 16:44:24:162 2012 Sysname CCF/7/event: ]{lang="EN-US"}]{#struct_0_13054_x1190_x1000792445}

[New session created on crypto engine(ID=0), flag=21.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13054_x1190_1858514541}*[新会话成功在加密引擎]{style="font-family:宋体"}[0]{lang="EN-US"}[上建立，加密引擎标识为]{style="font-family:宋体"}[21]{lang="EN-US"}*

[[\*Dec 16 16:44:24:162 2012 Sysname CCF/7/event:]{lang="EN-US"}]{#struct_0_13054_x1190_1345540606}

[First algorithm: algorithm ID= 17, required hash length=12, key length=20.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13054_x1190_x1997937446}*[第一个算法：算法]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[17]{lang="EN-US"}[，需要的哈希长度为]{style="font-family:宋体"}[12]{lang="EN-US"}[，密钥长度为]{style="font-family:宋体"}[20]{lang="EN-US"}*

[[\*Dec 16 16:44:24:162 2012 Sysname CCF/7/event: ]{lang="EN-US"}]{#struct_0_13054_x1190_584241274}

[Second algorithm: algorithm ID=4, required hash length=0, key length=24.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13054_x1190_451955236}*[第二个算法：算法]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[4]{lang="EN-US"}[，需要的哈希长度为]{style="font-family:宋体"}[0]{lang="EN-US"}[，密钥长度为]{style="font-family:宋体"}[24]{lang="EN-US"}*

*[ ]{lang="EN-US" style="font-size:10.5pt;
font-family:\"Arial\",\"sans-serif\""}*

[[\# ]{lang="EN-US"}]{#struct_0_13054_x1190_x667089132}[在设备上配置]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道，生成]{style="font-family:宋体"}[SA]{lang="EN-US"}[并建立]{style="font-family:宋体"}[CCF]{lang="EN-US"}[会话，打开]{style="font-family:宋体"}[crypto-engine]{lang="EN-US"}[的报文调试信息开关。当从本机]{style="font-family:宋体"}[ping]{lang="EN-US"}[对端的时候，输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging crypto-engine packet]{lang="EN-US"}]{#struct_0_13054_x1190_x222760923}

[\[Sysname\] ping -c 1 -a 18.18.18.1 19.19.19.1]{lang="EN-US"}

[PING 19.19.19.1 (19.19.19.1) from 18.18.18.1: 56 data bytes, press CTRL_C to break]{lang="EN-US"}

[56 bytes from 19.19.19.1: icmp_seq=0 ttl=255 time=0.945 ms]{lang="EN-US"}

[\-\-- 19.19.19.1 ping statistics \-\--]{lang="EN-US"}

[1 packet(s) transmitted, 1 packet(s) received, 0.0% packet loss]{lang="EN-US"}

[round-trip min/avg/max/std-dev = 0.945/0.945/0.945/0.000 ms]{lang="EN-US"}

[\*Dec 22 18:59:41:199 2012 Sysname CCF/7/packet:]{lang="EN-US"}

[First describer: algorithm ID=4, required hash length=0, skip length=36, process length=88, inject position36, flag=1, key length=24. ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13054_x1190_102039933}*[第一个描述符：算法]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[4]{lang="EN-US"}[，需要的哈希长度为]{style="font-family:宋体"}[0]{lang="EN-US"}[，跳过的长度为]{style="font-family:宋体"}[36]{lang="EN-US"}[，处理的长度为]{style="font-family:宋体"}[88]{lang="EN-US"}[，插入的位置为]{style="font-family:宋体"}[36]{lang="EN-US"}[，标识为]{style="font-family:宋体"}[1]{lang="EN-US"}[，密钥长度为]{style="font-family:宋体"}[24]{lang="EN-US"}*

[[\*Dec 22 18:59:41:199 2012 Sysname CCF/7/packet:]{lang="EN-US"}]{#struct_0_13054_x1190_x1998002982}

[Second describer: algorithm ID=17, required hash length=12, skip length=20, process length=104, inject position=124, flag=0, key length=20.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13054_x1190_38419755}*[第二个描述符：算法]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[17]{lang="EN-US"}[，需要的哈希长度为]{style="font-family:宋体"}[12]{lang="EN-US"}[，跳过的长度为]{style="font-family:宋体"}[20]{lang="EN-US"}[，处理的长度]{style="font-family:宋体"}[104]{lang="EN-US"}[，插入的位置为]{style="font-family:宋体"}[124]{lang="EN-US"}[，标识为]{style="font-family:宋体"}[0]{lang="EN-US"}[，密钥长度为]{style="font-family:宋体"}[20]{lang="EN-US"}*

[[\*Dec 22 18:59:41:199 2012 Sysname CCF/7/packet:]{lang="EN-US"}]{#struct_0_13054_x1190_881251839}

[Symmetric Job: data type=MBuf, input buffer length=136, output buffer length=136.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13054_x1190_309314360}*[对称任务：数据类型为]{style="font-family:宋体"}[MBuf]{lang="EN-US"}[，输入缓冲区的长度为]{style="font-family:宋体"}[136]{lang="EN-US"}[，输出缓冲区的长度为]{style="font-family:宋体"}[136]{lang="EN-US"}*

[[\*Dec 22 18:59:41:199 2012 Sysname CCF/7/packet:]{lang="EN-US"}]{#struct_0_13054_x1190_843379259}

[Symmetric operation finished, driver return=0, driver ID=0, driver flag=21.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13054_x1190_813045710}*[对称操作完成，驱动返回值为]{style="font-family:宋体"}[0]{lang="EN-US"}[，驱动]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[，驱动标识为]{style="font-family:宋体"}[21]{lang="EN-US"}*

[[\*Dec 22 18:59:41:199 2012 Sysname CCF/7/packet:]{lang="EN-US"}]{#struct_0_13054_x1190_x1300574097}

[First describer: algorithm ID=17, required hash length=12, skip length=20, process length=104, inject position=124, flag=0, key length=20.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13054_x1190_x1124047362}*[第一个描述符：]{style="font-family:宋体"}[算法]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[17]{lang="EN-US"}[，需要的哈希长度为]{style="font-family:宋体"}[12]{lang="EN-US"}[，]{style="font-family:宋体"}[跳过的长度为]{style="font-family:宋体"}[20]{lang="EN-US"}[，处理的长度为]{style="font-family:宋体"}[104]{lang="EN-US"}[，插入的位置为]{style="font-family:宋体"}[124]{lang="EN-US"}[，标识为]{style="font-family:宋体"}[0]{lang="EN-US"}[，]{style="font-family:宋体"}[密钥长度为]{style="font-family:宋体"}[20]{lang="EN-US"}*

[[\*Dec 22 18:59:41:199 2012 Sysname CCF/7/packet:]{lang="EN-US"}]{#struct_0_13054_x1190_x1998068518}

[Second describer: algorithm ID=4, required hash length=0, skip length=36, process length=88, inject position=36, flag=0, key length=24.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13054_x1190_x952547389}*[第二个描述符：]{style="font-family:宋体"}[算法]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[4]{lang="EN-US"}[，需要的哈希长度为]{style="font-family:宋体"}[0]{lang="EN-US"}[，]{style="font-family:宋体"}[跳过的长度为]{style="font-family:宋体"}[36]{lang="EN-US"}[，处理的长度为]{style="font-family:宋体"}[88]{lang="EN-US"}[，插入的位置为]{style="font-family:宋体"}[36]{lang="EN-US"}[，标识为]{style="font-family:宋体"}[0]{lang="EN-US"}[，]{style="font-family:宋体"}[密钥长度为]{style="font-family:宋体"}[24]{lang="EN-US"}*

[[\*Dec 22 18:59:41:199 2012 Sysname CCF/7/packet:]{lang="EN-US"}]{#struct_0_13054_x1190_1538966069}

[Symmetric Job: data type=MBuf, input buffer length=136, output buffer length=136.]{lang="EN-US"}

*[// ]{lang="EN-US" style="font-size:10.5pt;
font-family:\"Arial\",\"sans-serif\""}[对称任务：数据类型为]{style="font-size:10.5pt;
font-family:宋体"}[MBuf]{lang="EN-US" style="font-size:10.5pt;
font-family:\"Arial\",\"sans-serif\""}[，输入缓冲区的长度]{style="font-size:
10.5pt;font-family:宋体"}[136]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}[，输出缓冲区的长度]{style="font-size:10.5pt;font-family:宋体"}[136]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}*

[\*Dec 22 18:59:41:199 2012 Sysname CCF/7/packet:]{lang="EN-US"}

[Symmetric operation finished, driver return=0, driver id=0, driver flag=21. ]{lang="EN-US"}

*[// ]{lang="EN-US" style="font-size:10.5pt;
font-family:\"Arial\",\"sans-serif\""}[对称操作完成，驱动返回值为]{style="font-size:10.5pt;
font-family:宋体"}[0]{lang="EN-US" style="font-size:
10.5pt;font-family:\"Arial\",\"sans-serif\""}[，驱动]{style="font-size:
10.5pt;font-family:宋体"}[ID]{lang="EN-US" style="font-size:10.5pt;
font-family:\"Arial\",\"sans-serif\""}[为]{style="font-size:10.5pt;
font-family:宋体"}[0]{lang="EN-US" style="font-size:10.5pt;
font-family:\"Arial\",\"sans-serif\""}[，驱动标识为]{style="font-size:10.5pt;
font-family:宋体"}[21]{lang="EN-US" style="font-size:10.5pt;
font-family:\"Arial\",\"sans-serif\""}*

[ ]{lang="EN-US"}
