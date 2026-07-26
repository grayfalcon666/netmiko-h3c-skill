::: {#-313111210 .myid}
[]{#_Toc404796885}[]{#struct_0_x1089_x8390_x2044020787}[]{#_Toc331772676}[]{#_Toc130718952}[]{#_Toc87257691}

**RMON \-- RMON调试命令 \-- debugging rmon**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1089_x8390_x1104608451}

[**[debugging rmon]{lang="EN-US"}**[ { **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_x1089_x8390_x798876723}

[**[undo debugging rmon ]{lang="EN-US"}**[{ **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_x1089_x8390_2118455264}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1089_x8390_1149261559}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1089_x8390_486324406}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1089_x8390_1733152270}

[[network-admin]{lang="EN-US"}]{#struct_0_x1089_x8390_1657536054}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1089_x8390_x2132842298}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1089_x8390_x553573986}

[**[all]{lang="EN-US"}**]{#struct_0_x1089_x8390_1587385504}[：表示]{style="font-family:宋体"}[RMON]{lang="EN-US"}[所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1089_x8390_733200027}[：表示]{style="font-family:宋体"}[RMON]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1089_x8390_770636694}[：表示]{style="font-family:宋体"}[RMON]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1089_x8390_1575875388}

[**[debugging rmon]{lang="EN-US"}**]{#struct_0_x1089_x8390_x1617653289}[命令用来打开]{style="font-family:宋体"}[RMON]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging rmon]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[RMON]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[RMON]{lang="EN-US"}]{#struct_0_x1089_x8390_1206558612}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging rmon error]{lang="EN-US"}]{#struct_0_x1089_x8390_1733217806}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x845275707}[[字段]{style="font-family:黑体"}]{#struct_0_x1089_x8390_x242305141}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1089_x8390_1756803872}

[*[modulename]{lang="EN-US"}*[ entry *index*: failed to create aging timer]{lang="EN-US"}]{#struct_0_x1089_x8390_x766720450}

[[模块创建表项的老化定时器失败]{style="font-family:宋体"}]{#struct_0_x1089_x8390_x466738839}

[*[modulename]{lang="EN-US"}*]{#struct_0_x1089_x8390_1529052306}[：模块名，可取]{style="font-family:宋体"}[Hist]{lang="EN-US"}[、]{style="font-family:宋体"}[Event]{lang="EN-US"}[、]{style="font-family:宋体"}[Prialarm]{lang="EN-US"}[、]{style="font-family:宋体"}[Usrhist]{lang="EN-US"}[、]{style="font-family:宋体"}[Stats]{lang="EN-US"}

[*[index]{lang="EN-US"}*]{#struct_0_x1089_x8390_71572757}[：表项索引]{style="font-family:宋体"}

[*[modulename]{lang="EN-US"}*[ entry *index*: failed to sample on slot *slotid*]{lang="EN-US"}]{#struct_0_x1089_x8390_1733283342}

[[模块采样失败]{style="font-family:宋体"}]{#struct_0_x1089_x8390_915311099}

[*[modulename]{lang="EN-US"}*]{#struct_0_x1089_x8390_1457537795}[：模块名，可取]{style="font-family:宋体"}[Hist]{lang="EN-US"}[、]{style="font-family:宋体"}[Stats]{lang="EN-US"}

[*[index]{lang="EN-US"}*]{#struct_0_x1089_x8390_376173626}[：表项的索引]{style="font-family:宋体"}

[*[slotid]{lang="EN-US"}*]{#struct_0_x1089_x8390_x1680275692}[：采样所在槽号]{style="font-family:宋体"}

[*[modulename]{lang="EN-US"}*[ module: failed to init]{lang="EN-US"}]{#struct_0_x1089_x8390_415411158}

[[模块初始化失败]{style="font-family:宋体"}]{#struct_0_x1089_x8390_1733348878}

[*[modulename]{lang="EN-US"}*]{#struct_0_x1089_x8390_x291259882}[：模块名，可取]{style="font-family:宋体"}[Alarm]{lang="EN-US"}[、]{style="font-family:宋体"}[Stats]{lang="EN-US"}[、]{style="font-family:宋体"}[Usrhist]{lang="EN-US"}[、]{style="font-family:宋体"}[Event]{lang="EN-US"}[、]{style="font-family:宋体"}[Hist]{lang="EN-US"}[、]{style="font-family:宋体"}[Prialarm]{lang="EN-US"}[、]{style="font-family:宋体"}[Dbm]{lang="EN-US"}[、]{style="font-family:宋体"}[Epoll]{lang="EN-US"}[、]{style="font-family:宋体"}[Timer]{lang="EN-US"}

[*[modulename]{lang="EN-US"}*[ module: failed to recover]{lang="EN-US"}]{#struct_0_x1089_x8390_x671282168}

[[模块配置恢复失败]{style="font-family:宋体"}]{#struct_0_x1089_x8390_x932648180}

[*[modulename]{lang="EN-US"}*]{#struct_0_x1089_x8390_x577009739}[：模块名，可取]{style="font-family:宋体"}[Alarm]{lang="EN-US"}[、]{style="font-family:宋体"}[Event]{lang="EN-US"}[、]{style="font-family:宋体"}[Stats]{lang="EN-US"}[、]{style="font-family:宋体"}[Hist]{lang="EN-US"}[、]{style="font-family:宋体"}[Prialarm]{lang="EN-US"}[、]{style="font-family:宋体"}[Usrhist]{lang="EN-US"}

[*[modulename]{lang="EN-US"}*[ entry *index*: calloc failed]{lang="EN-US"}]{#struct_0_x1089_x8390_x1271601110}

[[模块创建表项时分配内存失败]{style="font-family:宋体"}]{#struct_0_x1089_x8390_1733414414}

[*[modulename]{lang="EN-US"}*]{#struct_0_x1089_x8390_x677035477}[：模块名，可取]{style="font-family:宋体"}[Event]{lang="EN-US"}[、]{style="font-family:宋体"}[Stats]{lang="EN-US"}[、]{style="font-family:宋体"}[Hist]{lang="EN-US"}[、]{style="font-family:宋体"}[Prialarm]{lang="EN-US"}[、]{style="font-family:宋体"}[Alarm]{lang="EN-US"}[、]{style="font-family:宋体"}[Usrhist]{lang="EN-US"}

[*[index]{lang="EN-US"}*]{#struct_0_x1089_x8390_x94544022}[：表项索引]{style="font-family:宋体"}

[*[modulename]{lang="EN-US"}*[ entry *index*: failed to create sampling timer]{lang="EN-US"}]{#struct_0_x1089_x8390_871960912}

[[模块创建表项的采样定时器失败]{style="font-family:宋体"}]{#struct_0_x1089_x8390_1886473926}

[*[modulename]{lang="EN-US"}*]{#struct_0_x1089_x8390_1733479950}[：模块名，可取]{style="font-family:宋体"}[Hist]{lang="EN-US"}[、]{style="font-family:宋体"}[Prialarm]{lang="EN-US"}[、]{style="font-family:宋体"}[Alarm]{lang="EN-US"}[、]{style="font-family:宋体"}[Usrhist]{lang="EN-US"}

[*[index]{lang="EN-US"}*]{#struct_0_x1089_x8390_x1072937776}[：表项的索引]{style="font-family:宋体"}

[*[modulename]{lang="EN-US"}*[ sample entry *index*- *sampleindex*: calloc failed]{lang="EN-US"}]{#struct_0_x1089_x8390_1637894164}

[[模块创建采样数据表项时分配内存失败]{style="font-family:宋体"}]{#struct_0_x1089_x8390_1248543148}

[*[modulename]{lang="EN-US"}*]{#struct_0_x1089_x8390_x249770348}[：模块名，可取]{style="font-family:宋体"}[Hist]{lang="EN-US"}

[*[index]{lang="EN-US"}*]{#struct_0_x1089_x8390_1733545486}[：表项的索引]{style="font-family:宋体"}

[*[sampleindex]{lang="EN-US"}*]{#struct_0_x1089_x8390_886885752}[：采样索引]{style="font-family:宋体"}

[*[modulename]{lang="EN-US"}*[ entry *index*: sampling failed]{lang="EN-US"}]{#struct_0_x1089_x8390_x297558376}

[[表项定时采样失败]{style="font-family:宋体"}]{#struct_0_x1089_x8390_1669038385}

[*[Modulename]{lang="EN-US"}*]{#struct_0_x1089_x8390_x1945129237}[：模块名，可取]{style="font-family:宋体"}[Alarm]{lang="EN-US"}[、]{style="font-family:宋体"}[Prialarm]{lang="EN-US"}

[*[Index]{lang="EN-US"}*]{#struct_0_x1089_x8390_1733611022}[：表项索引]{style="font-family:宋体"}

[*[modulename ]{lang="EN-US"}*[module: illegal OID type ]{lang="EN-US"}]{#struct_0_x1089_x8390_x1845387205}

[[模块创建或修改表项时]{style="font-family:宋体"}[OID]{lang="EN-US"}]{#struct_0_x1089_x8390_x1551526341}[类型非法]{style="font-family:宋体"}

[*[modulename]{lang="EN-US"}*]{#struct_0_x1089_x8390_x1693731808}[：模块名，可取]{style="font-family:宋体"}[Alarm]{lang="EN-US"}[、]{style="font-family:宋体"}[Prialarm]{lang="EN-US"}

[[Prialarm module: failed to process *state-name* parse state]{lang="EN-US"}]{#struct_0_x1089_x8390_1732627982}

[[扩展告警表解析表达式时处理状态失败]{style="font-family:宋体"}]{#struct_0_x1089_x8390_1314109199}

[*[state-name]{lang="EN-US"}*]{#struct_0_x1089_x8390_907097404}[：状态名称，可以取]{style="font-family:宋体"}[OID]{lang="EN-US"}[、]{style="font-family:宋体"}[INIT]{lang="EN-US"}[、]{style="font-family:宋体"}[NUM]{lang="EN-US"}[、]{style="font-family:宋体"}[SCAN]{lang="EN-US"}[、]{style="font-family:宋体"}[OPERATOR]{lang="EN-US"}[、]{style="font-family:宋体"}[FINISH]{lang="EN-US"}

[[Prialarm module: failed to calloc OID memory]{lang="EN-US"}]{#struct_0_x1089_x8390_x2071779736}

[[扩展告警表解析表达式时分配]{style="font-family:宋体"}[oid]{lang="EN-US"}]{#struct_0_x1089_x8390_1732693518}[内存失败]{style="font-family:宋体"}

[*[modulename]{lang="EN-US"}*[ module: illegal NUM characters]{lang="EN-US"}]{#struct_0_x1089_x8390_124291444}

[[表达式中含有非法格式的数字字符]{style="font-family:宋体"}]{#struct_0_x1089_x8390_218656839}

[*[Modulename]{lang="EN-US"}*]{#struct_0_x1089_x8390_664651315}[：模块名，可取]{style="font-family:宋体"}[Prialarm]{lang="EN-US"}

[[Prialarm module: illegal bracket]{lang="EN-US"}]{#struct_0_x1089_x8390_1733152271}

[[扩展告警表的表达式含有非法的括号]{style="font-family:宋体"}]{#struct_0_x1089_x8390_1657470518}

[[Prialarm module: zero divider]{lang="EN-US"}]{#struct_0_x1089_x8390_x1739905907}

[[用户将]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x1089_x8390_x990290141}[作为除数下发给扩展告警表的表达式]{style="font-family:宋体"}

[[Prialarm module: fail to calloc exp-stack]{lang="EN-US"}]{#struct_0_x1089_x8390_1733217807}

[[扩展告警表创建表达式栈失败]{style="font-family:宋体"}]{#struct_0_x1089_x8390_x242370677}

[[Prialarm module: exp-stack overflow]{lang="EN-US"}]{#struct_0_x1089_x8390_x1373302540}

[[扩展告警表表达式栈溢出]{style="font-family:宋体"}]{#struct_0_x1089_x8390_1733283343}

[[Log entry *index --logIndex*: calloc failed]{lang="EN-US"}]{#struct_0_x1089_x8390_915376635}

[[创建事件日志表项时分配内存失败]{style="font-family:宋体"}]{#struct_0_x1089_x8390_x886012133}

[*[index]{lang="EN-US"}*]{#struct_0_x1089_x8390_194992849}[：事件表项的索引]{style="font-family:宋体"}

[*[logindex]{lang="EN-US"}*]{#struct_0_x1089_x8390_1733348879}[：日志表项的索引]{style="font-family:宋体"}

[[Usrhist entry *index*: failed to calloc OID]{lang="EN-US"}]{#struct_0_x1089_x8390_x291194346}

[[用户历史控制表项采样时获取采样]{style="font-family:宋体"}[OID]{lang="EN-US"}]{#struct_0_x1089_x8390_9107466}[时分配内存失败]{style="font-family:宋体"}

[*[index]{lang="EN-US"}*]{#struct_0_x1089_x8390_1733414415}[：用户历史控制表项的索引]{style="font-family:宋体"}

[[Object entry *index-objectindex*: *calloc failed*]{lang="EN-US"}]{#struct_0_x1089_x8390_x677101013}

[[创建索引为]{style="font-family:宋体"}*[index]{lang="EN-US"}*]{#struct_0_x1089_x8390_x1658155681}[的用户历史控制表项的第]{style="font-family:宋体"}*[objectindex]{lang="EN-US"}*[个用户历史对象表项时分配内存失败]{style="font-family:宋体"}

[*[index]{lang="EN-US"}*]{#struct_0_x1089_x8390_1733479951}[：用户历史控制表项的索引]{style="font-family:宋体"}

[*[objectindex]{lang="EN-US"}*]{#struct_0_x1089_x8390_x1073003312}[：用户历史对象表项的索引]{style="font-family:宋体"}

[[Usrhist sample *entry index-sampleindex-objectindex*: calloc failed]{lang="EN-US"}]{#struct_0_x1089_x8390_x1865274982}

[[创建索引为]{style="font-family:宋体"}*[index]{lang="EN-US"}*]{#struct_0_x1089_x8390_1685838023}[的用户历史控制表项的第]{style="font-family:宋体"}*[objectindex]{lang="EN-US"}*[个用户历史对象表项的第]{style="font-family:宋体"}*[sampleindex]{lang="EN-US"}*[个用户历史数据表项时分配内存失败]{style="font-family:宋体"}

[*[index]{lang="EN-US"}*]{#struct_0_x1089_x8390_1733545487}[：用户历史控制表项的索引]{style="font-family:宋体"}

[*[sampleindex]{lang="EN-US"}*]{#struct_0_x1089_x8390_886951288}[：用户历史数据表采样次数]{style="font-family:宋体"}

[*[objectindex]{lang="EN-US"}*]{#struct_0_x1089_x8390_x309045698}[：用户历史对象表项的索引]{style="font-family:宋体"}

[[Sync module: failed to get global slot]{lang="EN-US"}]{#struct_0_x1089_x8390_1733611023}

[[获取全局槽号失败]{style="font-family:宋体"}]{#struct_0_x1089_x8390_x1845452741}

[[Sync module: failed to register epoll]{lang="EN-US"}]{#struct_0_x1089_x8390_784531329}

[[Sync]{lang="EN-US"}]{#struct_0_x1089_x8390_1732627983}[模块注册]{style="font-family:宋体"}[epoll]{lang="EN-US"}[失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging rmon event]{lang="EN-US"}]{#struct_0_x1089_x8390_1314174735}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x847257819}[[字段]{style="font-family:黑体"}]{#struct_0_x1089_x8390_1691342705}

[[描述]{style="font-family:黑体"}]{#struct_0_x1089_x8390_x206409831}

[*[modulename]{lang="EN-US"}*[ entry *index*: set same configuration]{lang="EN-US"}]{#struct_0_x1089_x8390_1670843094}

[[对表项下发了相同配置]{style="font-family:宋体"}]{#struct_0_x1089_x8390_1732693519}

[*[modulename]{lang="EN-US"}*]{#struct_0_x1089_x8390_124225908}[：模块名，可取]{style="font-family:宋体"}[Alarm]{lang="EN-US"}[、]{style="font-family:宋体"}[Event]{lang="EN-US"}[、]{style="font-family:宋体"}[Stats]{lang="EN-US"}[、]{style="font-family:宋体"}[Hist]{lang="EN-US"}[、]{style="font-family:宋体"}[Prialarm]{lang="EN-US"}[、]{style="font-family:宋体"}[Usrhist]{lang="EN-US"}

[*[index]{lang="EN-US"}*]{#struct_0_x1089_x8390_2090425731}[：表项索引]{style="font-family:宋体"}

[*[modulename]{lang="EN-US"}*[ entry *index*: aging timer started]{lang="EN-US"}]{#struct_0_x1089_x8390_x198268284}

[[表项开始老化]{style="font-family:宋体"}]{#struct_0_x1089_x8390_x533233501}

[*[modulename]{lang="EN-US"}*]{#struct_0_x1089_x8390_x2109450613}[：]{style="font-family:宋体"} [统计表模块名，可取]{style="font-family:宋体"}[Event]{lang="EN-US"}[、]{style="font-family:宋体"}[Stats]{lang="EN-US"}[、]{style="font-family:宋体"}[Hist]{lang="EN-US"}[、]{style="font-family:宋体"}[Prialarm]{lang="EN-US"}[、]{style="font-family:宋体"}[Usrhist]{lang="EN-US"}

[*[index]{lang="EN-US"}*]{#struct_0_x1089_x8390_618683097}[：统计表项索引]{style="font-family:宋体"}

[*[modulename]{lang="EN-US"}*[ entry *index*: the entry has been valid]{lang="EN-US"}]{#struct_0_x1089_x8390_1733152268}

[[表项已经处于激活状态]{style="font-family:宋体"}]{#struct_0_x1089_x8390_1657011767}

[*[modulename]{lang="EN-US"}*]{#struct_0_x1089_x8390_x568938373}[：模块名，可取]{style="font-family:宋体"}[Alarm]{lang="EN-US"}[、]{style="font-family:宋体"}[Event]{lang="EN-US"}[、]{style="font-family:宋体"}[Stats]{lang="EN-US"}[、]{style="font-family:宋体"}[Hist]{lang="EN-US"}[、]{style="font-family:宋体"}[Prialarm]{lang="EN-US"}[、]{style="font-family:宋体"}[Usrhist]{lang="EN-US"}

[*[index]{lang="EN-US"}*]{#struct_0_x1089_x8390_1111588045}[：表项索引]{style="font-family:宋体"}

[*[modulename]{lang="EN-US"}*[ entry *index*: start sampling ]{lang="EN-US"}]{#struct_0_x1089_x8390_1671997782}

[[表项触发采样]{style="font-family:宋体"}]{#struct_0_x1089_x8390_1733217804}

[*[modulename]{lang="EN-US"}*]{#struct_0_x1089_x8390_x242174069}[：模块名，可取]{style="font-family:宋体"}[Alarm]{lang="EN-US"}[、]{style="font-family:宋体"}[Hist]{lang="EN-US"}[、]{style="font-family:宋体"}[Prialarm]{lang="EN-US"}[、]{style="font-family:宋体"}[Usrhist]{lang="EN-US"}

[*[index]{lang="EN-US"}*]{#struct_0_x1089_x8390_977485401}[：表项索引]{style="font-family:宋体"}

[*[modulename]{lang="EN-US"}*[ entry *index*: the entry does not exist or different sample-id]{lang="EN-US"}]{#struct_0_x1089_x8390_2120754691}

[[表项不存在或采样标记]{style="font-family:宋体"}[sample Id]{lang="EN-US"}]{#struct_0_x1089_x8390_x230271797}[不一致]{style="font-family:宋体"}

[*[modulename]{lang="EN-US"}*]{#struct_0_x1089_x8390_x1209701043}[：]{style="font-family:宋体"} [模块名，可取]{style="font-family:宋体"}[Alarm]{lang="EN-US"}[、]{style="font-family:宋体"}[Hist]{lang="EN-US"}[、]{style="font-family:宋体"}[Prialarm]{lang="EN-US"}[、]{style="font-family:宋体"}[Usrhist]{lang="EN-US"}

[*[index]{lang="EN-US"}*]{#struct_0_x1089_x8390_1733283340}[：表项索引]{style="font-family:宋体"}

[*[modulename]{lang="EN-US"}*[ entry *index*: created no-loop timer-id *timerid*]{lang="EN-US"}]{#struct_0_x1089_x8390_915180027}

[[模块创建一个非循环定时器]{style="font-family:宋体"}]{#struct_0_x1089_x8390_1147290534}

[*[modulename]{lang="EN-US"}*]{#struct_0_x1089_x8390_1435714581}[：模块名，可取]{style="font-family:宋体"}[Alarm]{lang="EN-US"}[、]{style="font-family:宋体"}[Hist]{lang="EN-US"}[、]{style="font-family:宋体"}[Prialarm]{lang="EN-US"}[、]{style="font-family:宋体"}[Usrhist]{lang="EN-US"}

[*[timerid]{lang="EN-US"}*]{#struct_0_x1089_x8390_1903706694}[：非循环定时器]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Alarm entry *index*: sample reverse or first sample]{lang="EN-US"}]{#struct_0_x1089_x8390_1733348876}

[[索引为]{style="font-family:宋体"}*[index]{lang="EN-US"}*]{#struct_0_x1089_x8390_x291390954}[的告警表项采样翻转或第一次采样]{style="font-family:宋体"}

[*[index]{lang="EN-US"}*]{#struct_0_x1089_x8390_66921929}[：告警表项索引]{style="font-family:宋体"}

[*[modulename]{lang="EN-US"}*[ entry *index*: set to valid]{lang="EN-US"}]{#struct_0_x1089_x8390_x1483841836}

[[表项被配置为生效状态]{style="font-family:宋体"}]{#struct_0_x1089_x8390_1733414412}

[*[modulename]{lang="EN-US"}*]{#struct_0_x1089_x8390_x677428693}[：模块名，可取]{style="font-family:宋体"}[Alarm]{lang="EN-US"}[、]{style="font-family:宋体"}[Prialarm]{lang="EN-US"}

[*[index]{lang="EN-US"}*]{#struct_0_x1089_x8390_x428450385}[：表项的索引]{style="font-family:宋体"}

[[Usrhist sample entry *index-sampleindex-objectindex*: sample reverse]{lang="EN-US"}]{#struct_0_x1089_x8390_x2044067488}

[[用户历史表采样数据发生反转]{style="font-family:宋体"}]{#struct_0_x1089_x8390_x148614299}

[*[Index]{lang="EN-US"}*]{#struct_0_x1089_x8390_1733479948}[：用户历史控制表项索引]{style="font-family:宋体"}

[*[Sampleindex]{lang="EN-US"}*]{#struct_0_x1089_x8390_x1073462065}[：用户历史数据表采样次数]{style="font-family:宋体"}

[*[Objectindex]{lang="EN-US"}*]{#struct_0_x1089_x8390_x368285238}[：用户历史对象表项索引]{style="font-family:宋体"}

[[Failed to start daemon in chass-id *chassid* slot-id *slotid* ]{lang="EN-US"}]{#struct_0_x1089_x8390_16869286}

[[启动框号为]{style="font-family:宋体"}*[chassid]{lang="EN-US"}*]{#struct_0_x1089_x8390_1733545484}[槽号为]{style="font-family:宋体"}*[slotid]{lang="EN-US"}*[上的]{style="font-family:宋体"}[rmon]{lang="EN-US"}[进程失败]{style="font-family:宋体"}

[*[chassid]{lang="EN-US"}*]{#struct_0_x1089_x8390_886754680}[：框号]{style="font-family:宋体"}

[*[slotid]{lang="EN-US"}*]{#struct_0_x1089_x8390_1407658162}[：槽号]{style="font-family:宋体"}

[[Interface *interfacename* activated]{lang="EN-US"}]{#struct_0_x1089_x8390_x1219245958}

[*[interfacename]{lang="EN-US"}*]{#struct_0_x1089_x8390_1733611020}[的接口激活]{style="font-family:宋体"}

[[Interface *interfacename* deactivated]{lang="EN-US"}]{#struct_0_x1089_x8390_x1845256133}

[*[interfacename]{lang="EN-US"}*]{#struct_0_x1089_x8390_x900393399}[的接口去激活]{style="font-family:宋体"}

[[Interface *interfacename* deleted]{lang="EN-US"}]{#struct_0_x1089_x8390_1732627980}

[*[interfacename]{lang="EN-US"}*]{#struct_0_x1089_x8390_1314240271}[的接口删除]{style="font-family:宋体"}

[[Timer id is invalid]{lang="EN-US"}]{#struct_0_x1089_x8390_567936360}

[[删除一个无效的定时器]{style="font-family:宋体"}]{#struct_0_x1089_x8390_x269838144}

[*[timerType]{lang="EN-US"}*[ timer has *timerCount* timer instances]{lang="EN-US"}]{#struct_0_x1089_x8390_1732693516}

[[拥有]{style="font-family:宋体"}*[timerCount]{lang="EN-US"}*]{#struct_0_x1089_x8390_124946804}[个]{style="font-family:宋体"}*[timetype]{lang="EN-US"}*[类型的定时器]{style="font-family:宋体"}

[*[Timetype]{lang="EN-US"}*]{#struct_0_x1089_x8390_1281353766}[：老化定时器]{style="font-family:宋体"}[(0)]{lang="EN-US"}[，]{style="font-family:宋体"}[OID]{lang="EN-US"}[采样定时器]{style="font-family:宋体"}[(1)]{lang="EN-US"}[，驱动采样定时器]{style="font-family:宋体"}[(2)]{lang="EN-US"}

[*[timerCount]{lang="EN-US"}*]{#struct_0_x1089_x8390_1484063480}[：定时器个数]{style="font-family:宋体"}

[[SYNC module accepted new connection(GSlot=*gSlotNo*,Slot=*SlotNo*,Socket=*socketId*)]{lang="EN-US"}]{#struct_0_x1089_x8390_1733152269}

[[LLIPC]{lang="EN-US"}]{#struct_0_x1089_x8390_1656946231}[模块接受来自全局槽号为]{style="font-family:宋体"}*[gSlotNo]{lang="EN-US"}*[，局部槽号为]{style="font-family:宋体"}*[SlotNo]{lang="EN-US"}*[的]{style="font-family:宋体"}*[socketId]{lang="EN-US"}*[的连接请求]{style="font-family:宋体"}

[*[gSlotNo]{lang="EN-US"}*]{#struct_0_x1089_x8390_1766484040}[：全局槽号]{style="font-family:宋体"}

[*[SlotNo]{lang="EN-US"}*]{#struct_0_x1089_x8390_1733217805}[：局部槽号]{style="font-family:宋体"}

[*[socketId]{lang="EN-US"}*]{#struct_0_x1089_x8390_x242239605}[：连接的]{style="font-family:宋体"}[socket id]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1089_x8390_1719806495}

[[\# ]{lang="EN-US"}]{#struct_0_x1089_x8390_x1591087781}[打开]{style="font-family:宋体"}[RMON]{lang="EN-US"}[事件调试信息开关，配置历史组。]{style="font-family:宋体"}

[[\<Sysname\> debugging rmon event]{lang="EN-US"}]{#struct_0_x1089_x8390_x668257627}

[*[//]{lang="EN-US"}*]{#struct_0_x1089_x8390_362893532}*[新创建历史表项，系统输出相应调试信息]{style="font-family:宋体"}*

[[\[Sysname\] rmon alarm 1 1.3.6.1.2.1.6.3.0 5 absolute rising-threshold 100 1 falling-threshold 20 1]{lang="EN-US"}]{#struct_0_x1089_x8390_1733283341}

[\*Jun 30 16:53:29:403 2012 H3C RMON/7/EVENT: Alarm entry index 1: set to valid]{lang="EN-US"}

[*[//]{lang="EN-US"}*]{#struct_0_x1089_x8390_915245563}*[新创建历史控制表项后，对监控接口进行开始第一次采样，输出相应调试信息]{style="font-family:宋体"}*

[[\[Sysname-Ethernet1/0/2\] rmon history 1 buckets 5 interval 5 owner h3c]{lang="EN-US"}]{#struct_0_x1089_x8390_x903939281}

[\*Jun 30 16:53:29:403 2012 H3C RMON/7/EVENT:Hist entry index 1: start sampling]{lang="EN-US"}

[ ]{lang="EN-US"}
