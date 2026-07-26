::: {#470793729 .myid}
[]{#_Toc404783001}[]{#struct_0_x2019_84149_x1659254846}[]{#_Toc340740812}

**Python \-- Python配置命令 \-- python**

------------------------------------------------------------------------

[**[python]{lang="EN-US"}**]{#struct_0_x2019_84149_144619174}[命令用来进入]{style="font-family:宋体"}[Python shell]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2019_84149_1309063254}

[**[python]{lang="EN-US"}**]{#struct_0_x2019_84149_x1054494894}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2019_84149_1654107997}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2019_84149_x811993941}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2019_84149_x1403030227}

[[network-admin]{lang="EN-US"}]{#struct_0_x2019_84149_x1216345438}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2019_84149_582759035}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2019_84149_1766486077}

[[进入]{style="font-family:宋体"}[Python shell]{lang="EN-US"}]{#struct_0_x2019_84149_x2016407832}[后，可以使用]{style="font-family:宋体"}[Python2.7]{lang="EN-US"}[版本的命令和标准]{style="font-family:宋体"}[API]{lang="EN-US"}[，也可以使用]{style="font-family:宋体"}[Comware V7]{lang="EN-US"}[的扩展]{style="font-family:宋体"}[API]{lang="EN-US"}[。]{style="font-family:宋体"}

[[可输入]{style="font-family:宋体"}[exit()]{lang="EN-US"}]{#struct_0_x2019_84149_1344374803}[，然后回车，从]{style="font-family:宋体"}[Python shell]{lang="EN-US"}[退回到用户视图。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2019_84149_x489000563}

[[\# ]{lang="EN-US"}]{#struct_0_x2019_84149_805192708}[进入]{style="font-family:宋体"}[Python shell]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> python]{lang="EN-US"}]{#struct_0_x2019_84149_x951906436}

[Python 2.7.3 (default, Dec 22 2012, 11:39:05)]{lang="EN-US"}

[\[GCC 4.4.1\] on linux2]{lang="EN-US"}

[Type \"help\", \"copyright\", \"credits\" or \"license\" for more information.]{lang="EN-US"}

[\>\>\> ]{lang="EN-US"}

[\>\>\> exit()]{lang="EN-US"}

[\<Sysname\>]{lang="EN-US"}
:::

::: {#-36793359 .myid}
[]{#_Toc404783002}[]{#struct_0_x2019_84149_1305556811}

**Python \-- Python配置命令 \-- python filename**

------------------------------------------------------------------------

[**[python ]{lang="EN-US"}***[filename]{lang="EN-US"}*]{#struct_0_x2019_84149_57281662}[命令用来执行]{style="font-family:
宋体"}[Python]{lang="EN-US"}[脚本文件]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2019_84149_1766027326}

[**[python]{lang="EN-US"}**[ *filename*]{lang="EN-US"}]{#struct_0_x2019_84149_x882932726}*[ ]{lang="EN-US"}*[\[ ]{lang="EN-US"}*[param]{lang="EN-US"}*[ \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2019_84149_x727294953}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2019_84149_1292381766}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2019_84149_x1646664653}

[[network-admin]{lang="EN-US"}]{#struct_0_x2019_84149_x745592426}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2019_84149_x815585286}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2019_84149_x1724960681}

[*[filename]{lang="EN-US"}*]{#struct_0_x2019_84149_x394907149}[：]{style="font-family:宋体"}[Python]{lang="EN-US"}[脚本文件的名称。该文件必须为设备存储介质（]{style="font-family:宋体"}[Flash]{lang="EN-US"}[或者]{style="font-family:宋体"}[CF]{lang="EN-US"}[卡）上存]{style="font-family:宋体"}[在的文件，]{style="font-family:宋体"}[文件名区分大小写，扩展名必须为"]{style="font-family:宋体"}[.py]{lang="EN-US"}["，扩展名不区分大小写]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[*[param]{lang="EN-US"}*]{#struct_0_x2019_84149_x27092191}[：执]{style="font-family:宋体"}[行]{style="font-family:宋体"}[Python]{lang="EN-US"}[脚本文]{style="font-family:宋体"}[件时指定的参数，多个参数之间以空格分隔。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2019_84149_1765961790}

[[当系统执行脚本中的交互式指令时，系统将使用缺省值继续执行该指令。]{style="font-family:宋体"}]{#struct_0_x2019_84149_27269863}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2019_84149_1112488579}

[[\# ]{lang="EN-US"}]{#struct_0_x2019_84149_x1564956298}[执行]{style="font-family:宋体"}[Python]{lang="EN-US"}[脚本文件]{style="font-family:宋体"}[test.py]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> python test.py 1 2]{lang="EN-US"}]{#struct_0_x2019_84149_506191080}

[\[\'/flash:/test.py\', \'1\', \'2\'\]]{lang="EN-US"}

[ ]{lang="EN-US"}
:::
