
**Python \-- Python配置命令 \-- python**

------------------------------------------------------------------------

**[python**]命令用来进入Python shell。

【命令】

**[python**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

进入Python shell后，可以使用Python2.7版本的命令和标准API，也可以使用Comware V7的扩展API。

可输入exit()，然后回车，从Python shell退回到用户视图。

【举例】

\# 进入Python shell。

\<Sysname\> python

Python 2.7.3 (default, Dec 22 2012, 11:39:05)

GCC 4.4.1 on linux2

Type \"help\", \"copyright\", \"credits\" or \"license\" for more information.

\>\>\> 

\>\>\> exit()

\<Sysname\>

**Python \-- Python配置命令 \-- python filename**

------------------------------------------------------------------------

**[python ***filename*]命令用来执行Python脚本文件。

【命令】

**[python** *filename*]**\*[param* ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[filename*]：Python脚本文件的名称。该文件必须为设备存储介质（Flash或者CF卡）上存在的文件，文件名区分大小写，扩展名必须为".py"，扩展名不区分大小写。

*[param*]：执行Python脚本文件时指定的参数，多个参数之间以空格分隔。

【使用指导】

当系统执行脚本中的交互式指令时，系统将使用缺省值继续执行该指令。

【举例】

\# 执行Python脚本文件test.py。

\<Sysname\> python test.py 1 2

\'/flash:/test.py\', \'1\', \'2\'

