::: {#-840517699 .myid}
[]{#_Toc404782580}[]{#struct_0_x5885_64750_x502164296}[]{#_Toc291763611}[]{#_Toc206926275}[]{#_Toc98563071}

**文件系统管理 \-- 文件系统管理命令 \-- cd**

------------------------------------------------------------------------

[**[cd]{lang="EN-US"}**]{#struct_0_x5885_64750_1947845441}[命令用来修改当前的工作路径。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5885_64750_395044097}

[**[cd]{lang="EN-US"}**[ { *directory \|* **..** }]{lang="EN-US"}]{#struct_0_x5885_64750_1283333396}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x841509611}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5885_64750_x1422906717}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x584187299}

[[network-admin]{lang="EN-US"}]{#struct_0_x5885_64750_1239392814}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5885_64750_896990837}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1230714455}

[*[directory]{lang="EN-US"}*]{#struct_0_x5885_64750_x2131877341}[：指定目标工作路径。格式为]{style="font-family:宋体"}[\[*drive*:/\]*path*]{lang="EN-US"}[。]{style="font-family:宋体"}*[drive]{lang="EN-US"}*[和]{style="font-family:宋体"}*[path]{lang="EN-US"}*[参数的详细解释，请参见"基础配置指导"中的"文件系统管理"。如果没有给出]{style="font-family:宋体"}*[drive]{lang="EN-US"}*[信息，则表示当前路径下的文件夹。]{style="font-family:宋体"}

[**[..]{lang="EN-US"}**]{#struct_0_x5885_64750_x54763318}[：返回上一级目录。如果当前的工作路径是根目录，则执行]{style="font-family:宋体"}**[cd ..]{lang="EN-US"}**[后提示出错。该参数不支持命令行在线帮助。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x791569156}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x1984689003}[登录设备后从根目录进入]{style="font-family:宋体"}[test]{lang="EN-US"}[文件夹。]{style="font-family:宋体"}

[[\<Sysname\> cd test]{lang="EN-US"}]{#struct_0_x5885_64750_x841509612}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x1422972253}[返回上一级目录。]{style="font-family:宋体"}

[[\<Sysname\> cd ..]{lang="EN-US"}]{#struct_0_x5885_64750_1273370629}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_x5885_64750_1196111148}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x785783817}[修改当前的工作路径。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[查看备用主控板所在的槽位号。]{style="font-family:宋体"}]{#struct_0_x5885_64750_x1550659472}

[[\<Sysname\> display device]{lang="EN-US"}]{#struct_0_x5885_64750_x841509613}

[Slot No.   Brd Type     Brd Status     Subslot Num    Sft Ver          Patch Ver]{lang="EN-US"}

[ 0         LSQ1MPUA     Master         0              xx               None]{lang="EN-US"}

[ 1         LSQ1MPUA     Standby        0              xx               None]{lang="EN-US"}

[ 2         LSQ1GV48SC   Normal         0              xx               None]{lang="EN-US"}

[ 3         NONE         Absent         0              NONE             None]{lang="EN-US"}

[[通过以上显示信息可以了解到备用主控板所在的槽位号为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x5885_64750_x1423037789}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[进入备用主控板上]{style="font-family:宋体"}]{#struct_0_x5885_64750_x385701331}[Flash]{lang="EN-US"}[的根目录。]{style="font-family:宋体"}

[[\<Sysname\> cd slot1#flash:/]{lang="EN-US"}]{#struct_0_x5885_64750_x546522709}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[从备用主控板的文件系统切换回主用主控板根目录下的文件夹]{style="font-family:宋体"}]{#struct_0_x5885_64750_1524705272}[test]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> cd flash:/test]{lang="EN-US"}]{#struct_0_x5885_64750_x766650970}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[集中式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x5885_64750_x430694008}[设备]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_2141261929}[登录主设备后进入成员编号为]{style="font-family:宋体"}[2]{lang="EN-US"}[的从设备]{style="font-family:宋体"}[Flash]{lang="EN-US"}[的根目录。]{style="font-family:宋体"}

[[\<Sysname\> cd slot2#flash:/]{lang="EN-US"}]{#struct_0_x5885_64750_x1679774804}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_2678118}[从从设备的文件系统切换回主设备的根目录。]{style="font-family:宋体"}

[[\<Sysname\> cd flash:/]{lang="EN-US"}]{#struct_0_x5885_64750_x841509614}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_x5885_64750_x1422579037}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_161301915}[修改当前的工作路径。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[查看全局主用主控板和全局备用主控板所在成员设备的编号以及槽位号。]{style="font-family:宋体"}]{#struct_0_x5885_64750_964769126}

[[\<Sysname\> display irf]{lang="EN-US"}]{#struct_0_x5885_64750_x1917659696}

[ Member   Slot   Role    Priority    CPU-Mac]{lang="EN-US"}

[   2      0      Standby 20          00e0-fc0f-8c0f]{lang="EN-US"}

[   2      1      Standby 20          00e0-fc0f-8c1f]{lang="EN-US"}

[ \*+3      5      Master  20          00e0-fc0f-8c22]{lang="EN-US"}

[   3      6      Standby 20          00e0-fc0f-8c32]{lang="EN-US"}

[ ]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ \* indicates the device is the master.]{lang="EN-US"}

[ + indicates the device through which the user logs in.]{lang="EN-US"}

[ The Bridge MAC of the IRF is: 00e0-fc00-0a00]{lang="EN-US"}

[ Auto upgrade                  : yes]{lang="EN-US"}

[ Mac persistent                : 6 min]{lang="EN-US"}

[[通过以上显示信息可以了解到：成员设备]{style="font-family:宋体"}[3]{lang="EN-US"}]{#struct_0_x5885_64750_x841509615}[上的]{style="font-family:宋体"}[5]{lang="EN-US"}[号单板为全局主用主控板；成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[上的]{style="font-family:宋体"}[0]{lang="EN-US"}[、]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板和成员设备]{style="font-family:
宋体"}[3]{lang="EN-US"}[上的]{style="font-family:宋体"}[6]{lang="EN-US"}[号单板为全局备用主控板。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[登录设备后进入全局主用主控板上]{style="font-family:宋体"}]{#struct_0_x5885_64750_x1422644573}[Flash]{lang="EN-US"}[的根目录下的]{style="font-family:宋体"}[test]{lang="EN-US"}[文件夹。]{style="font-family:宋体"}

[[\<Sysname\> cd flash:/test]{lang="EN-US"}]{#struct_0_x5885_64750_x2057498617}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[登录设备后进入全局备用主控板上]{style="font-family:宋体"}]{#struct_0_x5885_64750_x564506203}[Flash]{lang="EN-US"}[的根目录。（该板所在设备的成员编号为]{style="font-family:宋体"}[2]{lang="EN-US"}[，槽位号为]{style="font-family:宋体"}[1]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> cd chassis2#slot1#flash:/]{lang="EN-US"}]{#struct_0_x5885_64750_1753865414}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[切换回全局主用主控板]{lang="EN-US" style="font-family:宋体"}[Flash]{lang="EN-US"}]{#struct_0_x5885_64750_593288450}[的根目录。]{lang="EN-US" style="font-family:宋体"}

[[\<Sysname\> cd flash:/]{lang="EN-US"}]{#struct_0_x5885_64750_298463299}
:::

::: {#4862103 .myid}
[]{#_Toc404782581}[]{#struct_0_x5885_64750_x1813151242}[]{#_Toc291763612}[]{#_Toc206926276}[]{#_Toc98563072}

**文件系统管理 \-- 文件系统管理命令 \-- copy**

------------------------------------------------------------------------

[**[copy]{lang="EN-US"}**]{#struct_0_x5885_64750_665559405}[命令用来复制文件。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x841509616}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_x5885_64750_x1422710109}[模式下：]{style="font-family:宋体"}

[**[copy ]{lang="EN-US"}***[fileurl-source fileurl-dest]{lang="EN-US"}*[ \[ **vpn-instance** *vpn-instance-name* \] \[ **source interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x5885_64750_x812074534}

[[FIPS]{lang="EN-US"}]{#struct_0_x5885_64750_1121559590}[模式下：]{style="font-family:宋体"}

[**[copy ]{lang="EN-US"}***[fileurl-source fileurl-dest]{lang="EN-US"}*]{#struct_0_x5885_64750_x286765895}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5885_64750_1894878237}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5885_64750_x694635826}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5885_64750_1490125877}

[[network-admin]{lang="EN-US"}]{#struct_0_x5885_64750_1090106978}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5885_64750_x841509617}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1422775645}

[*[fileurl]{lang="EN-US"}*[-*source*]{lang="EN-US"}]{#struct_0_x5885_64750_x1533060001}[：非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，为源文件名或者远程源文件]{style="font-family:宋体"}[URL]{lang="EN-US"}[；]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，为源文件名。若为]{style="font-family:宋体"}[URL]{lang="EN-US"}[格式，表示从远程文件服务器拷贝文件。远程源文件]{style="font-family:宋体"}[URL]{lang="EN-US"}[是否支持大小写遵循远程服务器端的规格。]{style="font-family:宋体"}

[*[fileurl-dest]{lang="EN-US"}*]{#struct_0_x5885_64750_x2123364110}[：非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，为目标文件名、目标文件夹、远程目标文件]{style="font-family:宋体"}[URL]{lang="EN-US"}[或远程目录]{style="font-family:宋体"}[URL]{lang="EN-US"}[；]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，为目标文件名或目标文件夹。若为]{style="font-family:宋体"}[URL]{lang="EN-US"}[格式，表示拷贝文件至远程的目标文件或目标文件夹。远程目标文件]{style="font-family:宋体"}[URL]{lang="EN-US"}[和远程目录]{style="font-family:宋体"}[URL]{lang="EN-US"}[是否支持大小写遵循远程服务器端规格。如果使用文件夹作为]{style="font-family:宋体"}*[fileurl]{lang="EN-US"}*[-*dest*]{lang="EN-US"}[，则系统会将文件复制到指定文件夹，使用源文件名称作为文件名。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x5885_64750_269530820}[：连接远程服务器使用的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示远程服务器位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}**[ **interface** *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x5885_64750_x67918160}[：指定连接远程服务器时使用的源接口。指定源接口后，设备将使用源接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[作为设备生成的连接报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[。不指定该参数时，则使用路由出接口作为源接口。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1462923936}

[[FIPS]{lang="EN-US"}]{#struct_0_x5885_64750_685235099}[模式下，不支持远程拷贝功能。]{style="font-family:宋体"}

[[使用]{style="font-family:宋体"}**[copy]{lang="EN-US"}**]{#struct_0_x5885_64750_1763051248}[命令：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{lang="EN-US" style="font-family:宋体"}*[fileurl-source]{lang="EN-US"}*]{#struct_0_x5885_64750_x841509618}[和]{lang="EN-US" style="font-family:
宋体"}*[fileurl-dest]{lang="EN-US"}*[均指定为本地路径时，可以实现本地文件间的拷贝。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_x5885_64750_x1422316893}*[fileurl-source]{lang="EN-US"}*[指定为远程服务器上的路径（即为]{style="font-family:宋体"}[URL]{lang="EN-US"}[格式），]{style="font-family:宋体"}*[fileurl-dest]{lang="EN-US"}*[指定为本地路径时，可以实现将远程服务器上的文件拷贝到本地。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_x5885_64750_x1342802571}*[fileurl-source]{lang="EN-US"}*[指定为本地路径，]{style="font-family:宋体"}*[fileurl-dest]{lang="EN-US"}*[指定为远程服务器上的路径（即为]{style="font-family:宋体"}[URL]{lang="EN-US"}[格式）时，可以实现将本地文件拷贝到远程服务器。]{style="font-family:宋体"}

[[当进行远程拷贝时，支持]{style="font-family:宋体"}[FTP]{lang="EN-US"}]{#struct_0_x5885_64750_x1848497704}[和]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[协议：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当采用]{lang="EN-US" style="font-family:宋体"}[FTP]{lang="EN-US"}]{#struct_0_x5885_64750_x1820267341}[协议时，]{lang="EN-US" style="font-family:宋体"}[URL]{lang="EN-US"}[采用"]{lang="EN-US" style="font-family:宋体"}[ftp]{lang="EN-US"}[://]{lang="EN-US"}[FTP]{lang="EN-US"}[用户名]{lang="EN-US" style="font-family:宋体"}[\[]{lang="EN-US"}[:]{lang="EN-US"}[密码]{lang="EN-US" style="font-family:宋体"}[\]@]{lang="EN-US"}[服务器地址]{lang="EN-US" style="font-family:宋体"}[\[:]{lang="EN-US"}[端口号]{style="font-family:宋体"}[\]]{lang="EN-US"}[/]{lang="EN-US"}[文件路径"的形式]{lang="EN-US" style="font-family:宋体"}[，其中用户名和密码必须和服务器上的配置一致，如果服务器只对用户名进行认证，则不用输入密码。例]{style="font-family:宋体"}[如]{lang="EN-US" style="font-family:宋体"}[URL]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[ftp://1:1@1.1.1.1/startup.cfg]{lang="EN-US"}[时，表示地址为]{lang="EN-US" style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器授权目录下的]{lang="EN-US" style="font-family:宋体"}[startup.cfg]{lang="EN-US"}[文件，登录用户名为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[、密码为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当采用]{style="font-family:宋体"}]{#struct_0_x5885_64750_x342706253}[TFTP]{lang="EN-US"}[协议时，]{style="font-family:宋体"}[URL]{lang="EN-US"}[采用"]{style="font-family:宋体"}[tftp://]{lang="EN-US"}[服务器地址]{style="font-family:宋体"}[\[:]{lang="EN-US"}[端口号]{style="font-family:宋体"}[\]/]{lang="EN-US"}[文件路径"的形式。]{style="font-family:宋体"}[例如]{lang="EN-US" style="font-family:
宋体"}[URL]{lang="EN-US"}[为]{lang="EN-US" style="font-family:
宋体"}[tftp://1.1.1.1/startup.cfg]{lang="EN-US"}[时表示地址为]{lang="EN-US" style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器]{lang="EN-US" style="font-family:宋体"}[工作]{style="font-family:宋体"}[目录下的]{lang="EN-US" style="font-family:宋体"}[startup.cfg]{lang="EN-US"}[文件。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当采用]{style="font-family:宋体"}]{#struct_0_x5885_64750_x5745204}[FTP]{lang="EN-US"}[或]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[协议时，服务器地址均支持]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[形式和]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[形式。当需要使用]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址时，必须用中括号"]{style="font-family:宋体"}[\[\]]{lang="EN-US"}["将]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址括起来，以便将]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址和端口号区分开来。形如]{style="font-family:宋体"}[ftp://test:test@\[2001::1\]:21/test.cfg]{lang="EN-US"}[，其中，]{style="font-family:宋体"}[2001::1]{lang="EN-US"}[为]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，]{style="font-family:宋体"}[21]{lang="EN-US"}[为服务器接收]{style="font-family:宋体"}[FTP]{lang="EN-US"}[协议报文的端口号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5885_64750_877906977}

[]{#_Toc291763613}[]{#_Toc206926277}[]{#_Toc98563073}[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x841509619}[将文件]{style="font-family:宋体"}[test.cfg]{lang="EN-US"}[在当前文件夹下复制一份，并命名为]{style="font-family:宋体"}[testbackup.cfg]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> copy test.cfg testbackup.cfg]{lang="EN-US"}]{#struct_0_x5885_64750_x1422382429}

[Copy flash:/test.cfg to flash:/testbackup.cfg? \[Y/N\]:y]{lang="EN-US"}

[Copying file flash:/test.cfg to flash:/testbackup.cfg\...Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x1084889714}[将]{style="font-family:宋体"}[Flash]{lang="EN-US"}[上文件夹]{style="font-family:宋体"}[test]{lang="EN-US"}[下的文件]{style="font-family:宋体"}[1.cfg]{lang="EN-US"}[复制到]{style="font-family:宋体"}[CF]{lang="EN-US"}[卡第一分区下的文件夹]{style="font-family:宋体"}[testbackup]{lang="EN-US"}[，并命名为]{style="font-family:宋体"}[1backup.cfg]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> copy flash:/test/1.cfg cfa0:/testbackup/1backup.cfg]{lang="EN-US"}]{#struct_0_x5885_64750_x1760883708}

[Copy flash:/test/1.cfg to cfa0:/testbackup/1backup.cfg? \[Y/N\]:y]{lang="EN-US"}

[Copying file flash:/test/1.cfg to cfa0:/testbackup/1backup.cfg\...Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_2055580676}[将]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[上的文件]{style="font-family:宋体"}[test.cfg]{lang="EN-US"}[拷贝到本地，并命名为]{style="font-family:宋体"}[testbackup.cfg]{lang="EN-US"}[，]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器的登录用户名为]{style="font-family:宋体"}[user]{lang="EN-US"}[，密码为]{style="font-family:宋体"}[private]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> copy ftp://user:private@1.1.1.1/test.cfg testbackup.cfg]{lang="EN-US"}]{#struct_0_x5885_64750_x1651697484}

[Copy ftp://user:private@1.1.1.1/test.cfg to flash:/testbackup.cfg? \[Y/N\]:y]{lang="EN-US"}

[Copying file ftp://user:private@1.1.1.1/test.cfg to flash:/testbackup.cfg\... Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_1601657664}[将文件]{style="font-family:宋体"}[test.cfg]{lang="EN-US"}[拷贝到]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[上，并命名为]{style="font-family:宋体"}[testbackup.cfg]{lang="EN-US"}[，]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器的登录用户名为]{style="font-family:宋体"}[user]{lang="EN-US"}[，密码为]{style="font-family:宋体"}[private]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> copy test.cfg ftp://user:private@1.1.1.1/testbackup.cfg]{lang="EN-US"}]{#struct_0_x5885_64750_x841509620}

[Copy flash:/test.cfg to ftp://user:private@1.1.1.1/testbackup.cfg? \[Y/N\]:y]{lang="EN-US"}

[Copying file flash:/test.cfg to ftp://user:private@1.1.1.1/testbackup.cfg\... Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x1422841184}[将]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[上的文件]{style="font-family:宋体"}[test.cfg]{lang="EN-US"}[拷贝到本地，并命名为]{style="font-family:宋体"}[testbackup.cfg]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> copy tftp://1.1.1.1/test.cfg testbackup.cfg]{lang="EN-US"}]{#struct_0_x5885_64750_795592964}

[Copy tftp://1.1.1.1/test.cfg to flash:/testbackup.cfg? \[Y/N\]:y]{lang="EN-US"}

[Copying file tftp://1.1.1.1/test.cfg to flash:/testbackup.cfg\... Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_580926637}[将文件]{style="font-family:宋体"}[test.cfg]{lang="EN-US"}[拷贝到]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[上，并命名为]{style="font-family:宋体"}[testbackup.cfg]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> copy test.cfg tftp://1.1.1.1/testbackup.cfg]{lang="EN-US"}]{#struct_0_x5885_64750_1332083799}

[Copy flash:/test.cfg to tftp://1.1.1.1/testbackup.cfg? \[Y/N\]:y]{lang="EN-US"}

[Copying file flash:/test.cfg to tftp://1.1.1.1/testbackup.cfg\... Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_764971437}[将]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[上的文件]{style="font-family:宋体"}[test.cfg]{lang="EN-US"}[拷贝到本地，并命名为]{style="font-family:宋体"}[testbackup.cfg]{lang="EN-US"}[。]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器位于]{style="font-family:宋体"}[VPN]{lang="EN-US"}[（名称为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[）中，登录用户名为]{style="font-family:宋体"}[user]{lang="EN-US"}[，密码为]{style="font-family:宋体"}[private]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> copy ]{lang="EN-US"}]{#struct_0_x5885_64750_659183387}[[ftp://user:private@1.1.1.1/test.cfg testbackup.cfg]{lang="EN-US" style="color:windowtext;text-decoration:none"}](ftp://user:private@1.1.1.1/test.cfg%20testbackup.cfg)[ vpn-instance vpn1]{lang="EN-US"}

[Copy ftp://user:private@1.1.1.1/test.cfg to flash:/testbackup.cfg? \[Y/N\]:y]{lang="EN-US"}

[Copying file ftp://user:private@1.1.1.1/test.cfg to flash:/testbackup.cfg\... Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_1497142549}[将]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[上的文件]{style="font-family:宋体"}[test.cfg]{lang="EN-US"}[拷贝到本地，并命名为]{style="font-family:宋体"}[testbackup.cfg]{lang="EN-US"}[。]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器位于]{style="font-family:宋体"}[VPN]{lang="EN-US"}[（名称为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[）中。]{style="font-family:宋体"}

[[\<Sysname\> copy tftp://1.1.1.1/test.cfg testbackup.cfg vpn-instance vpn1]{lang="EN-US"}]{#struct_0_x5885_64750_356544348}

[Copy tftp://1.1.1.1/test.cfg to flash:/testbackup.cfg? \[Y/N\]:y]{lang="EN-US"}

[Copying file tftp://1.1.1.1/test.cfg to flash:/testbackup.cfg\... Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x201217642}[将]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器]{style="font-family:宋体"}[2001::1]{lang="EN-US"}[上的文件]{style="font-family:宋体"}[test.cfg]{lang="EN-US"}[拷贝到本地，并命名为]{style="font-family:宋体"}[testbackup.cfg]{lang="EN-US"}[，登录用户名为]{style="font-family:宋体"}[user]{lang="EN-US"}[，密码为]{style="font-family:宋体"}[private]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> copy ]{lang="EN-US"}]{#struct_0_x5885_64750_x691974515}[[ftp://user:private@\[2001::1\]/test.cfg testbackup.cfg]{lang="EN-US" style="color:windowtext;text-decoration:none"}](ftp://user:private@%5B2001::1%5D/test.cfg%20testbackup.cfg)

[Copy ftp://user:private@\[2001::1\]/test.cfg to flash:/testbackup.cfg? \[Y/N\]:y]{lang="EN-US"}

[Copying file ftp://user:private@\[2001::1\]/test.cfg to flash:/testbackup.cfg\... Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x1393428236}[将]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器]{style="font-family:宋体"}[2001::1]{lang="EN-US"}[上的文件]{style="font-family:宋体"}[test.cfg]{lang="EN-US"}[拷贝到本地，并命名为]{style="font-family:宋体"}[testbackup.cfg]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> copy tftp://\[2001::1\]/test.cfg testbackup.cfg]{lang="EN-US"}]{#struct_0_x5885_64750_x2121355599}

[Copy tftp://\[2001::1\]/test.cfg to flash:/testbackup.cfg? \[Y/N\]:y]{lang="EN-US"}

[Copying file tftp://\[2001::1\]/test.cfg to flash:/testbackup.cfg\... Done.]{lang="EN-US"}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_x5885_64750_x241316890}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_1497142548}[登录设备后将主用主控板的配置文件拷贝到备用主控板的根目录下。]{style="font-family:宋体"}

[[\<Sysname\> copy test.cfg slot1#flash:/]{lang="EN-US"}]{#struct_0_x5885_64750_356609884}

[Copy flash:/test.cfg to slot1#flash:/test.cfg? \[Y/N\]:y]{lang="EN-US"}

[Copying file flash:/test.cfg to slot1#flash:/test.cfg\...Done.]{lang="EN-US"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[集中式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x5885_64750_1302439533}[设备]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x276677414}[登录设备后将主设备的配置文件拷贝到从设备（成员编号为]{style="font-family:宋体"}[2]{lang="EN-US"}[）的根目录下。]{style="font-family:宋体"}

[[\<Sysname\> copy test.cfg slot2#flash:/]{lang="EN-US"}]{#struct_0_x5885_64750_2090224071}

[Copy flash:/test.cfg to slot2#flash:/test.cfg? \[Y/N\]:y]{lang="EN-US"}

[Copying file flash:/test.cfg to slot2#flash:/test.cfg\...Done.]{lang="EN-US"}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_x5885_64750_1338973777}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_1148946578}[登录设备后将全局主用主控板的配置文件拷贝到全局备用主控板的根目录下（该板所在的成员设备的编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[，槽位号为]{style="font-family:宋体"}[1]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[\<Sysname\> copy test.cfg chassis1#slot1#flash:/]{lang="EN-US"}]{#struct_0_x5885_64750_1497142547}

[Copy flash:/test.cfg to chassis1#slot1#flash:/test.cfg? \[Y/N\]:y]{lang="EN-US"}

[Copying file flash:/test.cfg to chassis1#slot1#flash:/test.cfg\...Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_357199708}[登录设备后将全局备用主控板（该板所在的成员设备的编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[，槽位号为]{style="font-family:宋体"}[1]{lang="EN-US"}[）的配置文件拷贝到另一个全局备用主控板的根目录下（该板所在的成员设备的编号为]{style="font-family:宋体"}[2]{lang="EN-US"}[，槽位号为]{style="font-family:宋体"}[1]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[\<Sysname\> copy chassis1#slot1#flash:/test.cfg chassis2#slot1#flash:/]{lang="EN-US"}]{#struct_0_x5885_64750_937194108}

[Copy chassis1#slot1#flash:/test.cfg to chassis2#slot1#flash:/test.cfg? \[Y/N\]:y]{lang="EN-US"}

[Copying file chassis1#slot1#flash:/test.cfg to chassis2#slot1#flash:/test.cfg\...Done.]{lang="EN-US"}
:::

::: {#432758916 .myid}
[]{#_Toc404782582}[]{#struct_0_x5885_64750_1914625877}

**文件系统管理 \-- 文件系统管理命令 \-- delete**

------------------------------------------------------------------------

[**[delete]{lang="EN-US"}**]{#struct_0_x5885_64750_x348626259}[命令用来删除文件。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5885_64750_359290353}

[**[delete]{lang="EN-US"}**[ \[ **/unreserved** \] *file*-*url*]{lang="EN-US"}]{#struct_0_x5885_64750_764408143}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1824612631}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5885_64750_1497142546}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5885_64750_357265244}

[[network-admin]{lang="EN-US"}]{#struct_0_x5885_64750_85530112}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5885_64750_2011865474}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5885_64750_361321844}

[**[/unreserved]{lang="EN-US"}**]{#struct_0_x5885_64750_x1792958156}[：彻底删除该文件。]{style="font-family:宋体"}

[*[file]{lang="EN-US"}*[-*url*]{lang="EN-US"}]{#struct_0_x5885_64750_x1237232196}[：要删除的文件名。]{style="font-family:宋体"}*[file]{lang="EN-US"}*[-*url*]{lang="EN-US"}[参数支持通配符"]{style="font-family:宋体"}[\*]{lang="EN-US"}["进行匹配，比如]{style="font-family:宋体"}**[delete ]{lang="EN-US"}**[\*.txt]{lang="EN-US"}[可以删除当前目录下所有以]{style="font-family:宋体"}[txt]{lang="EN-US"}[为扩展名的文件。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1192700588}

[**[delete]{lang="EN-US"}**[ *file*-*url*]{lang="EN-US"}]{#struct_0_x5885_64750_x849130657}[命令用来暂时删除文件，被删除的文件被存放在回收站中，可以使用]{style="font-family:宋体"}**[undelete]{lang="EN-US"}**[命令恢复。]{style="font-family:宋体"}

[**[delete]{lang="EN-US"}**[ **/unreserved** *file*-*url*]{lang="EN-US"}]{#struct_0_x5885_64750_1190662344}[命令用来永久删除文件，系统会将该文件从设备上彻底删除。被删除的文件不再存在，不能恢复，请谨慎使用。]{style="font-family:宋体"}

[[请不要对回收站中的文件执行]{style="font-family:宋体"}**[delete]{lang="EN-US"}**]{#struct_0_x5885_64750_1497142545}[命令，以免影响回收站功能。若要删除回收站中的文件，请使用]{style="font-family:宋体"}**[reset recycle-bin]{lang="EN-US"}**[命令。]{style="font-family:宋体"}

[[在同一个目录下，如果先后删除了两个名称相同的文件，回收站中只保留最后一次删除的文件。不同目录下，如果先后删除了名称相同的文件，回收站中会保留这些删除的文件。]{style="font-family:宋体"}]{#struct_0_x5885_64750_357330780}

[[当存储介质空间不足时，如果执行]{style="font-family:宋体"}**[delete]{lang="EN-US"}**[ *file*-*url*]{lang="EN-US"}]{#struct_0_x5885_64750_x304909526}[命令，系统会自动转入永久删除处理流程。]{style="font-family:宋体"}

[[当缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_x5885_64750_1531448120}[的管理员执行]{style="font-family:宋体"}**[delete]{lang="EN-US"}**[ *file*-*url*]{lang="EN-US"}[命令删除非缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[存储介质上的文件时，系统会自动转入永久删除处理流程。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1208829584}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[集中式设备]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x5885_64750_1855950890}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_477242355}[删除当前目录下的文件]{style="font-family:宋体"}[1.cfg]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> delete 1.cfg]{lang="EN-US"}]{#struct_0_x5885_64750_x458255067}

[Delete flash:/1.cfg? \[Y/N\]:y]{lang="EN-US"}

[Deleting file flash:/1.cfg\...Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_1497142544}[永久删除当前目录下的文件]{style="font-family:宋体"}[1.cfg]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> delete /unreserved 1.cfg]{lang="EN-US"}]{#struct_0_x5885_64750_357396316}

[The file cannot be restored. Delete flash:/1.cfg? \[Y/N\]:y]{lang="EN-US"}

[Deleting the file permanently will take a long time. Please wait\...]{lang="EN-US"}

[Deleting file flash:/1.cfg\...Done.]{lang="EN-US"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_x5885_64750_868130834}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_48884871}[登录设备后删除主用主控板存储介质根目录下的文件]{style="font-family:宋体"}[1.cfg]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> delete 1.cfg]{lang="EN-US"}]{#struct_0_x5885_64750_663864551}

[Delete flash:/1.cfg? \[Y/N\]:y]{lang="EN-US"}

[Deleting file flash:/1.cfg\...Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x2025607321}[登录设备后永久删除主用主控板存储介质根目录下的文件]{style="font-family:宋体"}[1.cfg]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> delete /unreserved 1.cfg]{lang="EN-US"}]{#struct_0_x5885_64750_1497142543}

[The file cannot be restored. Delete flash:/1.cfg? \[Y/N\]:y]{lang="EN-US"}

[Deleting the file permanently will take a long time. Please wait\...]{lang="EN-US"}

[Deleting file flash:/1.cfg\...Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_356937564}[登录设备后删除备用主控板（所在槽位号为]{style="font-family:宋体"}[1]{lang="EN-US"}[）存储介质根目录下的文件]{style="font-family:宋体"}[1.cfg]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[方法一]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x5885_64750_682594795}

[[\<Sysname\> delete slot1#flash:/1.cfg]{lang="EN-US"}]{#struct_0_x5885_64750_x1320181142}

[Delete slot1#flash:/1.cfg? \[Y/N\]:y]{lang="EN-US"}

[Deleting file slot1#flash:/1.cfg\...Done.]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[方法二]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x5885_64750_x906586067}

[[\<Sysname\> cd slot1#flash:/]{lang="EN-US"}]{#struct_0_x5885_64750_1723849339}

[\<Sysname\> delete 1.cfg]{lang="EN-US"}

[Delete slot1#flash:/1.cfg? \[Y/N\]:y]{lang="EN-US"}

[Deleting file slot1#flash:/1.cfg\...Done.]{lang="EN-US"}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[集中式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x5885_64750_x57914291}[设备]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_1960700720}[登录设备后删除主设备存储介质根目录下的文件]{style="font-family:宋体"}[1.cfg]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> delete 1.cfg]{lang="EN-US"}]{#struct_0_x5885_64750_1497142542}

[Delete flash:/1.cfg? \[Y/N\]:y]{lang="EN-US"}

[Deleting file flash:/1.cfg\...Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_357003100}[登录设备后永久删除主设备存储介质根目录下的文件]{style="font-family:宋体"}[1.cfg]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> delete /unreserved 1.cfg]{lang="EN-US"}]{#struct_0_x5885_64750_981383145}

[The file cannot be restored. Delete flash:/1.cfg? \[Y/N\]:y]{lang="EN-US"}

[Deleting the file permanently will take a long time. Please wait\...]{lang="EN-US"}

[Deleting file flash:/1.cfg\...Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_342535965}[登录设备后删除从设备（成员编号为]{style="font-family:宋体"}[2]{lang="EN-US"}[）存储介质根目录下的文件]{style="font-family:宋体"}[1.cfg]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[方法一]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x5885_64750_151143533}

[[\<Sysname\> delete slot2#flash:/1.cfg]{lang="EN-US"}]{#struct_0_x5885_64750_x1313316236}

[Delete slot2#flash:/1.cfg? \[Y/N\]:y]{lang="EN-US"}

[Deleting file slot2#flash:/1.cfg\...Done.]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[方法二]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x5885_64750_x1156114264}

[[\<Sysname\> cd slot2#flash:/]{lang="EN-US"}]{#struct_0_x5885_64750_1497142541}

[\<Sysname\> delete 1.cfg]{lang="EN-US"}

[Delete slot2#flash:/1.cfg? \[Y/N\]:y]{lang="EN-US"}

[Deleting file slot2#flash:/1.cfg\...Done.]{lang="EN-US"}

[[(4)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_x5885_64750_357068636}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_545581166}[登录设备后删除全局主用主控板存储介质根目录下的文件]{style="font-family:宋体"}[1.cfg]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> delete 1.cfg]{lang="EN-US"}]{#struct_0_x5885_64750_x354902520}

[Delete flash:/1.cfg? \[Y/N\]:y]{lang="EN-US"}

[Deleting file flash:/1.cfg\...Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x1977546314}[登录设备后永久删除全局主用主控板存储介质根目录下的文件]{style="font-family:宋体"}[1.cfg]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> delete /unreserved 1.cfg]{lang="EN-US"}]{#struct_0_x5885_64750_x1529087601}

[The file cannot be restored. Delete flash:/1.cfg? \[Y/N\]:y]{lang="EN-US"}

[Deleting the file permanently will take a long time. Please wait\...]{lang="EN-US"}

[Deleting file flash:/1.cfg\...Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_206582668}[登录设备后删除全局备用主控板存储介质根目录下的文件]{style="font-family:宋体"}[1.cfg]{lang="EN-US"}[（该板所在的成员设备的编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[，槽位号为]{style="font-family:宋体"}[1]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[方法一]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x5885_64750_1497142540}

[[\<Sysname\> delete chassis1#slot1#flash:/1.cfg]{lang="EN-US"}]{#struct_0_x5885_64750_357134172}

[Delete chassis1#slot1#flash:/1.cfg? \[Y/N\]:y]{lang="EN-US"}

[Deleting file chassis1#slot1#flash:/1.cfg\...Done.]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[方法二]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x5885_64750_x949110902}

[[\<Sysname\> cd chassis1#slot1#flash:/]{lang="EN-US"}]{#struct_0_x5885_64750_553849035}

[\<Sysname\> delete 1.cfg]{lang="EN-US"}

[Delete chassis1#slot1#flash:/1.cfg? \[Y/N\]:y]{lang="EN-US"}

[Deleting file chassis1#slot1#flash:/1.cfg\...Done.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x978910049}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[undelete]{lang="EN-US"}**]{#struct_0_x5885_64750_1601110752}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset recycle-bin]{lang="EN-US"}**]{#struct_0_x5885_64750_1382163405}
:::

::: {#1391204812 .myid}
[]{#_Toc404782583}[]{#struct_0_x5885_64750_204268762}

**文件系统管理 \-- 文件系统管理命令 \-- dir**

------------------------------------------------------------------------

[**[dir]{lang="EN-US"}**]{#struct_0_x5885_64750_x2004619122}[命令用来显示当前文件夹或文件信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x2130254825}

[**[dir]{lang="EN-US"}**[ \[ **/all** \] \[ *file*-*url* \| **/all-filesystems** \]]{lang="EN-US"}]{#struct_0_x5885_64750_1608073924}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5885_64750_1577561936}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5885_64750_1773256649}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x112398098}

[[network-admin]{lang="EN-US"}]{#struct_0_x5885_64750_1149597469}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5885_64750_x681837530}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1139760319}

[**[/all]{lang="EN-US"}**]{#struct_0_x5885_64750_204203226}[：显示当前文件夹下所有的文件及文件夹信息，包括非隐藏文件、非隐藏文件夹、隐藏文件和隐藏文件夹。不指定该参数时，只显示非隐藏文件和非隐藏文件夹。]{style="font-family:宋体"}

[*[file]{lang="EN-US"}*[-*url*]{lang="EN-US"}]{#struct_0_x5885_64750_x1628090843}[：显示指定的文件或文件夹的信息。]{style="font-family:宋体"}*[file]{lang="EN-US"}*[-*url*]{lang="EN-US"}[参数支持通配符"]{style="font-family:宋体"}[\*]{lang="EN-US"}["，比如]{style="font-family:宋体"}**[dir ]{lang="EN-US"}**[\*.txt]{lang="EN-US"}[可以显示当前文件夹下所有以]{style="font-family:宋体"}[txt]{lang="EN-US"}[为扩展名的文件。]{style="font-family:宋体"}

[**[/all-filesystems]{lang="EN-US"}**]{#struct_0_x5885_64750_1120409589}[：显示设备上所有存储介质根目录下的文件及文件夹信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x673887017}

[[不带任何参数时，用来显示当前文件夹下所有可见文件及文件夹的信息。]{style="font-family:宋体"}]{#struct_0_x5885_64750_1270827530}

[[回收站文件夹名为"]{style="font-family:宋体"}[.trash]{lang="EN-US"}]{#struct_0_x5885_64750_2106620679}["，要查看回收站下有哪些文件，请用]{style="font-family:宋体"}**[dir /all]{lang="EN-US"}**[ .trash]{lang="EN-US"}[，或者]{style="font-family:宋体"}**[cd]{lang="EN-US"}**[ .trash]{lang="EN-US"}[进入回收站文件夹后，再用]{style="font-family:
宋体"}**[dir]{lang="EN-US"}**[命令查看。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5885_64750_1198987182}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[集中式设备]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x5885_64750_964545577}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x999423193}[显示当前文件夹下所有的文件及文件夹信息。]{style="font-family:宋体"}

[[\<Sysname\> dir /all]{lang="EN-US"}]{#struct_0_x5885_64750_204137690}

[Directory of flash:/]{lang="EN-US"}

[......略......]{style="font-family:宋体"}

[[本举例用于示意显示信息的大致形式，具体信息与设备型号以及用户配置有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x5885_64750_893483792}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x1779641895}[显示设备上所有存储介质根目录下的文件及文件夹信息。]{style="font-family:宋体"}

[[\<Sysname\> dir /all-filesystems]{lang="EN-US"}]{#struct_0_x5885_64750_232423477}

[Directory of flash:/]{lang="EN-US"}

[......略......]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[Directory of cfa0:/]{lang="EN-US"}

[......略......]{style="font-family:宋体"}

[[本举例用于示意显示信息的大致形式，具体信息与设备型号以及用户配置有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x5885_64750_x258976596}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_x5885_64750_x467847339}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x881176058}[登录设备后显示当前目录下所有的文件及文件夹信息。]{style="font-family:宋体"}

[[\<Sysname\> dir /all]{lang="EN-US"}]{#struct_0_x5885_64750_204072154}

[Directory of flash:/]{lang="EN-US"}

[......略......]{style="font-family:宋体"}

[[本举例用于示意显示信息的大致形式，具体信息与设备型号以及用户配置有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x5885_64750_x1109677099}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_700778123}[显示设备上所有存储介质根目录下的文件及文件夹信息。]{style="font-family:宋体"}

[[\<Sysname\> dir /all-filesystems]{lang="EN-US"}]{#struct_0_x5885_64750_x926974407}

[Directory of flash:/]{lang="EN-US"}

[......略......]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[Directory of cfa0:/]{lang="EN-US"}

[......略......]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[Directory of slot7#flash:/]{lang="EN-US"}

[......略......]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[Directory of slot7#cfa0:/]{lang="EN-US"}

[......略......]{style="font-family:宋体"}

[[本举例用于示意显示信息的大致形式，具体信息与设备型号以及用户配置有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x5885_64750_x1300353199}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_287564821}[登录设备后显示备用主控板（所在槽位号为]{style="font-family:宋体"}[1]{lang="EN-US"}[）存储介质中所有的文件及文件夹信息。]{style="font-family:宋体"}

[[\<Sysname\> cd slot1#flash:/]{lang="EN-US"}]{#struct_0_x5885_64750_204530906}

[\<Sysname\> dir /all]{lang="EN-US"}

[......略......]{style="font-family:宋体"}

[[本举例用于示意显示信息的大致形式，具体信息与设备型号以及用户配置有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x5885_64750_x1003532253}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[集中式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x5885_64750_x1835787574}[设备]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_1291651805}[登录设备后显示主设备存储介质中所有的文件及文件夹信息。]{style="font-family:宋体"}

[[\<Sysname\> dir /all]{lang="EN-US"}]{#struct_0_x5885_64750_x315104304}

[Directory of flash:]{lang="EN-US"}

[......略......]{style="font-family:宋体"}

[[本举例用于示意显示信息的大致形式，具体信息与设备型号以及用户配置有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x5885_64750_2095096966}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_1907635560}[显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中所有存储介质根目录下的文件及文件夹信息。]{style="font-family:宋体"}

[[\<Sysname\> dir /all-filesystems]{lang="EN-US"}]{#struct_0_x5885_64750_204465370}

[Directory of flash:/]{lang="EN-US"}

[......略......]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[Directory of slot1#flash:/]{lang="EN-US"}

[......略......]{style="font-family:宋体"}

[[本举例用于示意显示信息的大致形式，具体信息与设备型号以及用户配置有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x5885_64750_x592067844}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_2529751}[登录设备后显示从设备（成员编号为]{style="font-family:宋体"}[2]{lang="EN-US"}[）存储介质中所有的文件及文件夹信息。]{style="font-family:宋体"}

[[\<Sysname\> cd slot2#flash:/]{lang="EN-US"}]{#struct_0_x5885_64750_x39544738}

[\<Sysname\> dir /all]{lang="EN-US"}

[Directory of slot2#flash:/]{lang="EN-US"}

[......略......]{style="font-family:宋体"}

[[本举例用于示意显示信息的大致形式，具体信息与设备型号以及用户配置有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x5885_64750_762878664}

[[(4)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_x5885_64750_2110140506}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_2113665091}[登录设备后显示全局主用主控板存储介质中所有的文件及文件夹信息。]{style="font-family:宋体"}

[[\<Sysname\> dir /all]{lang="EN-US"}]{#struct_0_x5885_64750_204399834}

[Directory of flash:/]{lang="EN-US"}

[......略......]{style="font-family:宋体"}

[[本举例用于示意显示信息的大致形式，具体信息与设备型号以及用户配置有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x5885_64750_1853610720}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x208853811}[显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中所有存储介质根目录下的文件及文件夹信息。]{style="font-family:宋体"}

[[\<Sysname\> dir /all-filesystems]{lang="EN-US"}]{#struct_0_x5885_64750_x496927414}

[Directory of flash:/]{lang="EN-US"}

[......略......]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[Directory of chassis1#slot1#flash:/]{lang="EN-US"}

[......略......]{style="font-family:宋体"}

[[本举例用于示意显示信息的大致形式，具体信息与设备型号以及用户配置有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x5885_64750_x1270375642}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_664884877}[登录设备后显示全局备用主控板存储介质中所有的文件及文件夹信息（该板所在成员设备的编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[，槽位号为]{style="font-family:宋体"}[1]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[方法一]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x5885_64750_1416481841}

[[\<Sysname\> dir /all chassis1#slot1#flash:/]{lang="EN-US"}]{#struct_0_x5885_64750_204334298}

[Directory of chassis1#slot1#flash:/]{lang="EN-US"}

[......略......]{style="font-family:宋体"}

[[本举例用于示意显示信息的大致形式，具体信息与设备型号以及用户配置有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x5885_64750_x805941884}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[方法二]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x5885_64750_x1832688022}

[[\<Sysname\> cd chassis1#slot1#flash:/]{lang="EN-US"}]{#struct_0_x5885_64750_1697039863}

[\<Sysname\> dir /all]{lang="EN-US"}

[......略......]{style="font-family:宋体"}

[[本举例用于示意显示信息的大致形式，具体信息与设备型号以及用户配置有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x5885_64750_x1376370881}

[[表1-1 ]{lang="EN-US"}[dir]{lang="EN-US"}]{#struct_0_x5885_64750_x45240781}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_641734098}[[字段]{style="font-family:黑体"}]{#struct_0_x5885_64750_1016316491}
:::

[[说明]{style="font-family:黑体"}]{#struct_0_x5885_64750_x807604617}

[[Directory of]{lang="EN-US"}]{#struct_0_x5885_64750_204793050}

[[当前显示的目录]{style="font-family:宋体"}]{#struct_0_x5885_64750_1663579660}

[[0     -rwh      3144  Apr 26 2014 13:45:28  xx.xx]{lang="EN-US"}]{#struct_0_x5885_64750_1997087465}

[[文件或文件夹的信息：]{style="font-family:宋体"}]{#struct_0_x5885_64750_x1422340786}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_x5885_64750_2106503732}[表示编号，由系统自动分配]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[-rwh]{lang="EN-US"}]{#struct_0_x5885_64750_804758254}[表示属性。第一个字符如果是]{style="font-family:宋体"}[d]{lang="EN-US"}[表示文件夹，如果显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["，则表示它是文件；第二个字符是]{style="font-family:宋体"}[r]{lang="EN-US"}[，表示本文件或文件夹是可读的；第三个字符是]{style="font-family:宋体"}[w]{lang="EN-US"}[，表示本文件或文件夹是可写的；第四个字符如果是]{style="font-family:宋体"}[h]{lang="EN-US"}[，表示本文件或文件夹是隐藏的，如果显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["，则表示它是非隐藏的（请不要修改或删除隐藏文件或文件夹，以免影响对应功能）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3144]{lang="EN-US"}]{#struct_0_x5885_64750_485651424}[表示文件大小，单位为]{style="font-family:宋体"}[B]{lang="EN-US"}[。如果显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["，则表示它是文件夹]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Apr 26 2014 13:45:28]{lang="EN-US"}]{#struct_0_x5885_64750_204727514}[表示最近一次修改的时间]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[xx.xx]{lang="EN-US"}]{#struct_0_x5885_64750_x1472079554}[表示名称]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#-22216190 .myid}
[]{#_Toc404782584}[]{#struct_0_x5885_64750_2030328928}

**文件系统管理 \-- 文件系统管理命令 \-- fdisk**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](文件系统管理命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x5885_64750_1636871377}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_x5885_64750_854302590}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[支持]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_x5885_64750_277872525}[MDC]{lang="EN-US"}[的设备，本命令只在缺省]{style="font-family:\"KaiTi_GB2312\",\"serif\""}[MDC]{lang="EN-US"}[下存在。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[Flash]{lang="EN-US"}]{#struct_0_x5885_64750_x118127044}[不支持分区。]{lang="EN-US" style="font-family:\"KaiTi_GB2312\",\"serif\""}
:::

**[ ]{lang="EN-US"}**

[**[fdisk]{lang="EN-US"}**]{#struct_0_x5885_64750_388122289}[命令用来对存储介质进行分区。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5885_64750_204268763}

[**[fdisk]{lang="EN-US"}**[ *medium-name* \[ *partition-number* \]]{lang="EN-US"}]{#struct_0_x5885_64750_x2004619121}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5885_64750_1761427944}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5885_64750_1098810240}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5885_64750_34822057}

[[network-admin]{lang="EN-US"}]{#struct_0_x5885_64750_286305912}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5885_64750_185472784}

[*[medium-name]{lang="EN-US"}*]{#struct_0_x5885_64750_2067002487}[：需要分区的存储介质的名称。该参数的具体取值与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[partition-number]{lang="EN-US"}*]{#struct_0_x5885_64750_593113209}[：分区数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5885_64750_204203227}

[[如果指定分区数则将存储介质平均划分成指定数目的分区，否则，进入交互模式进行分区。]{style="font-family:宋体"}]{#struct_0_x5885_64750_x1628090842}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x5885_64750_x1608473766}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分区操作会清除]{style="font-family:宋体"}]{#struct_0_x5885_64750_x836927575}[CF]{lang="EN-US"}[卡]{style="font-family:宋体"}[/U]{lang="EN-US"}[盘中的所有数据，请务必做好文件备份。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分区完成后各分区的大小可能与用户指定的大小不一致，但误差小于]{style="font-family:宋体"}]{#struct_0_x5885_64750_982484258}[CF]{lang="EN-US"}[卡]{style="font-family:宋体"}[/U]{lang="EN-US"}[盘总容量的]{style="font-family:宋体"}[5]{lang="EN-US"}[％。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分区后，必须先卸载所有的分区才能安全的拔出]{style="font-family:宋体"}]{#struct_0_x5885_64750_168901534}[CF]{lang="EN-US"}[卡]{style="font-family:宋体"}[/U]{lang="EN-US"}[盘，否则，可能会引起]{style="font-family:宋体"}[CF]{lang="EN-US"}[卡]{style="font-family:宋体"}[/U]{lang="EN-US"}[盘上文件系统的损坏。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户对存储介质执行分区操作时，如果同时还有其他用户在访问该存储介质，系统会提示分区失败。]{style="font-family:宋体"}]{#struct_0_x5885_64750_x1726759300}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对]{style="font-family:宋体"}]{#struct_0_x5885_64750_1119425088}[U]{lang="EN-US"}[盘进行分区的时候，请确保没有对]{style="font-family:宋体"}[U]{lang="EN-US"}[盘设置写保护。否则会分区失败，需要重新挂载或者插拔]{style="font-family:宋体"}[U]{lang="EN-US"}[盘后，才能正常访问]{style="font-family:宋体"}[U]{lang="EN-US"}[盘。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令不支持对分区进行再分区。如果要修改分区大小，需要重新对整个存储设备进行分区。]{style="font-family:宋体"}]{#struct_0_x5885_64750_x1960287622}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5885_64750_204137691}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_893483791}[将设备的]{style="font-family:宋体"}[CF]{lang="EN-US"}[卡平均分为]{style="font-family:宋体"}[3]{lang="EN-US"}[个分区。]{style="font-family:宋体"}

[[\<Sysname\> fdisk cfa: 3]{lang="EN-US"}]{#struct_0_x5885_64750_204072155}

[Capacity of cfa: : 256M bytes]{lang="EN-US"}

[Cfa: will be divided into the following partitions:]{lang="EN-US"}

[DeviceName      Capacity]{lang="EN-US"}

[cfa0:            85MB]{lang="EN-US"}

[cfa1:            85MB]{lang="EN-US"}

[cfa2:            86MB]{lang="EN-US"}

[All data on cfa: will be lost, continue? \[Y/N\]:y]{lang="EN-US"}

[Partitioning cfa:\...Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x1109677100}[使用交互模式将设备的]{style="font-family:宋体"}[CF]{lang="EN-US"}[卡分为]{style="font-family:宋体"}[1]{lang="EN-US"}[个分区。]{style="font-family:宋体"}

[[\<Sysname\> fdisk cfa:]{lang="EN-US"}]{#struct_0_x5885_64750_x1221077425}

[The capacity of cfa: : 256M bytes ]{lang="EN-US"}

[Partition 1 (32MB\~224MB, 256MB. Press CTRL+C to quit or Enter to use all available space):]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x5885_64750_x1627886154}*[按]{style="font-family:宋体"}[\<Enter\>]{lang="EN-US"}[键或者输入]{style="font-family:宋体"}[256]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[cfa: will be divided into the following partition(s):]{lang="EN-US"}]{#struct_0_x5885_64750_204530907}

[DeviceName    Capacity]{lang="EN-US"}

[cfa0:          256MB]{lang="EN-US"}

[All data on cfa: will be lost, continue? \[Y/N\]:y]{lang="EN-US"}

[Partitioning cfa:\...Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x1003532254}[将]{style="font-family:宋体"}[CF]{lang="EN-US"}[卡分为]{style="font-family:宋体"}[3]{lang="EN-US"}[个分区，并分别指定]{style="font-family:宋体"}[3]{lang="EN-US"}[个分区的大小。]{style="font-family:宋体"}

[[\<Sysname\> fdisk cfa:]{lang="EN-US"}]{#struct_0_x5885_64750_536865421}

[The capacity of cfa: : 256M bytes ]{lang="EN-US"}

[Partition 1 (32MB\~224MB, 256MB, Press CTRL+C to quit or Enter to use all available space):128]{lang="EN-US"}

[[将第一个分区的大小指定为]{style="font-family:宋体"}[128MB]{lang="EN-US"}]{#struct_0_x5885_64750_1603081721}[（输入]{style="font-family:宋体"}[128]{lang="EN-US"}[后回车）。]{style="font-family:宋体"}

[[Partition 2 (32MB\~96MB, 128MB, Press CTRL+C to quit or Enter to use all available space):31]{lang="EN-US"}]{#struct_0_x5885_64750_827037830}

[[将第二个分区的大小指定为]{style="font-family:宋体"}[31MB]{lang="EN-US"}]{#struct_0_x5885_64750_1363585561}[（输入]{style="font-family:宋体"}[31]{lang="EN-US"}[后回车）。]{style="font-family:宋体"}

[[The partition size must be greater than or equal to 32MB.]{lang="EN-US"}]{#struct_0_x5885_64750_204465371}

[Partition 2 (32MB\~96MB, 128MB, Press CTRL+C to quit or Enter to use all available space):1000]{lang="EN-US"}

[[将第二个分区的大小指定为]{style="font-family:宋体"}[1000MB]{lang="EN-US"}]{#struct_0_x5885_64750_x592067843}[（输入]{style="font-family:宋体"}[1000]{lang="EN-US"}[后回车）。]{style="font-family:宋体"}

[[The partition size must be less than or equal to 128MB.]{lang="EN-US"}]{#struct_0_x5885_64750_2988503}

[Partition 2 (32MB\~96MB, 128MB, Press CTRL+C to quit or Enter to use all available space):127]{lang="EN-US"}

[[将第二个分区的大小指定为]{style="font-family:宋体"}[127MB]{lang="EN-US"}]{#struct_0_x5885_64750_1523970748}[（输入]{style="font-family:宋体"}[127]{lang="EN-US"}[后回车）。]{style="font-family:宋体"}

[[The remaining space is less than 32MB. Please enter the size of partition 2 again.]{lang="EN-US"}]{#struct_0_x5885_64750_2073506492}

[Partition 2 (32MB\~96MB, 128MB, Press CTRL+C to quit or Enter to use all available space):]{lang="EN-US"}

[[重新指定第二个分区的大小为]{style="font-family:宋体"}[56MB]{lang="EN-US"}]{#struct_0_x5885_64750_921297986}[（输入]{style="font-family:宋体"}[56]{lang="EN-US"}[后回车）。]{style="font-family:宋体"}

[[Partition 3 (32MB\~40MB, 72MB, Press CTRL+C to quit or Enter to use all available space):]{lang="EN-US"}]{#struct_0_x5885_64750_1271223381}

[[剩余的空间全部划分给第三个分区（直接回车）。]{style="font-family:宋体"}]{#struct_0_x5885_64750_1329637852}

[[cfa: will be divided into the following partition(s):]{lang="EN-US"}]{#struct_0_x5885_64750_204399835}

[DeviceName     Capacity]{lang="EN-US"}

[cfa0:            128MB]{lang="EN-US"}

[cfa1:            56MB]{lang="EN-US"}

[cfa2:            72MB]{lang="EN-US"}

[All data on cfa: will be lost, continue? \[Y/N\]:y]{lang="EN-US"}

[Partitioning cfa:\...Done.]{lang="EN-US"}
:::::

::: {#-310424435 .myid}
[]{#_Toc404782585}[]{#struct_0_x5885_64750_1853610719}

**文件系统管理 \-- 文件系统管理命令 \-- file prompt**

------------------------------------------------------------------------

[**[file prompt]{lang="EN-US"}**]{#struct_0_x5885_64750_x208263986}[命令用来设置文件和文件夹操作时是否提示。]{style="font-family:宋体"}

[**[undo file prompt]{lang="EN-US"}**]{#struct_0_x5885_64750_204334299}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x805941885}

[**[file prompt ]{lang="EN-US"}**[{ **alert** \| **quiet** }]{lang="EN-US"}]{#struct_0_x5885_64750_x1832753558}

[**[undo file prompt]{lang="EN-US"}**]{#struct_0_x5885_64750_x1600704717}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5885_64750_692338281}

[[用户对文件进行有危险性的操作时，系统会要求用户进行交互确认。]{style="font-family:宋体"}]{#struct_0_x5885_64750_163577581}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x909324879}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5885_64750_1490535284}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x2059946525}

[[network-admin]{lang="EN-US"}]{#struct_0_x5885_64750_x1911915901}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5885_64750_204793051}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5885_64750_1663579659}

[**[alert]{lang="EN-US"}**]{#struct_0_x5885_64750_1996628710}[：当用户对文件]{style="font-family:宋体"}[/]{lang="EN-US"}[文件夹进行有危险性的操作时，系统会要求用户进行交互确认。]{style="font-family:宋体"}

[**[quiet]{lang="EN-US"}**]{#struct_0_x5885_64750_x1054428270}[：用户对文件]{style="font-family:宋体"}[/]{lang="EN-US"}[文件夹进行任何操作，系统均不要求用户进行确认。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x6552774}

[[如果将文件]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x5885_64750_x59186291}[文件夹操作的提示方式设置为]{style="font-family:宋体"}**[quiet]{lang="EN-US"}**[，则系统对文件]{style="font-family:宋体"}[/]{lang="EN-US"}[文件夹操作不要求用户进行确认，这样可能会导致一些因误操作而发生的、不可恢复的、对系统造成破坏的操作产生。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1419494029}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_2034217226}[设置用户对文件进行有危险性的操作时，要求进行交互确认。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5885_64750_204727515}

[\[Sysname\] file prompt alert]{lang="EN-US"}
:::

::::: {#1929962580 .myid}
[]{#_Toc404782586}[]{#struct_0_x5885_64750_x1472079553}[]{#_Toc295910986}

**文件系统管理 \-- 文件系统管理命令 \-- fixdisk**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](文件系统管理命令.files/image001.png){#图片 2 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x5885_64750_x1505123481}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[支持]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_x5885_64750_1384720676}[MDC]{lang="EN-US"}[的设备，本命令只有缺省]{style="font-family:\"KaiTi_GB2312\",\"serif\""}[MDC]{lang="EN-US"}[支持。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}
:::

**[ ]{lang="EN-US"}**

[**[fixdisk]{lang="EN-US"}**]{#struct_0_x5885_64750_x1725532392}[命令用来恢复存储介质的空间。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5885_64750_1355672353}

[**[fixdisk ]{lang="EN-US"}***[medium-name]{lang="EN-US"}*]{#struct_0_x5885_64750_x1960166508}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x621561098}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5885_64750_x2025622054}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5885_64750_204268760}

[[network-admin]{lang="EN-US"}]{#struct_0_x5885_64750_x2004619120}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x967455411}

[*[medium-name]{lang="EN-US"}*]{#struct_0_x5885_64750_470837322}[：存储介质的名称。该参数的具体取值与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5885_64750_1383438890}

[[由于异常操作等原因，存储设备的某些空间可能不可用，或者某些空间已经不再需要使用但是没有释放，用户可以通过]{style="font-family:宋体"}**[fixdisk]{lang="EN-US"}**]{#struct_0_x5885_64750_811782685}[命令来恢复存储设备的空间。]{style="font-family:宋体"}

[[用户对存储介质执行]{style="font-family:宋体"}**[fixdisk]{lang="EN-US"}**]{#struct_0_x5885_64750_534448369}[操作时，如果同时还有其他用户在访问该存储介质，系统会提示]{style="font-family:宋体"}**[fixdisk]{lang="EN-US"}**[操作失败。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5885_64750_1000914610}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_631108912}[恢复存储介质]{style="font-family:宋体"}[Flash]{lang="EN-US"}[的空间。]{style="font-family:宋体"}

[[\<Sysname\> fixdisk flash:]{lang="EN-US"}]{#struct_0_x5885_64750_204203224}

[Restoring flash: may take some time\...]{lang="EN-US"}

[Restoring flash:\...Done.]{lang="EN-US"}
:::::

::::: {#446157247 .myid}
[]{#_Toc404782587}[]{#struct_0_x5885_64750_x1628090845}[]{#_Toc291763622}[]{#_Toc206926286}[]{#_Toc98563078}

**文件系统管理 \-- 文件系统管理命令 \-- format**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](文件系统管理命令.files/image001.png){#图片 3 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x5885_64750_1926978643}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[支持]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_x5885_64750_1764087701}[MDC]{lang="EN-US"}[的设备，本命令只在缺省]{style="font-family:\"KaiTi_GB2312\",\"serif\""}[MDC]{lang="EN-US"}[下存在。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}
:::

**[ ]{lang="EN-US"}**

[**[format]{lang="EN-US"}**]{#struct_0_x5885_64750_x1129151480}[命令用来格式化存储介质。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x2062490048}

[**[format]{lang="EN-US"}**[ *medium-name*]{lang="EN-US"}]{#struct_0_x5885_64750_74636359}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5885_64750_434670154}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5885_64750_204137688}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1062831336}

[[network-admin]{lang="EN-US"}]{#struct_0_x5885_64750_470304792}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x119771975}

[*[medium-name]{lang="EN-US"}*]{#struct_0_x5885_64750_x815047132}[：存储介质的名称。该参数的具体取值与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1337899435}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[格式化操作将导致存储设备上的所有文件丢失，并且不可恢复；尤其需要注意的是，如果存储设备上有启动配置文件，格式化该存储设备，将丢失启动配置文件。]{style="font-family:宋体"}]{#struct_0_x5885_64750_1612369305}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户对存储介质执行格式化操作时，如果同时还有其他用户在访问该存储介质，系统会提示格式化操作失败。]{style="font-family:宋体"}]{#struct_0_x5885_64750_959591812}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于支持分区的存储设备，请格式化各个分区来完成整个存储设备的格式化。比如，要格式化支持分区的]{style="font-family:宋体"}]{#struct_0_x5885_64750_1436865223}[CF]{lang="EN-US"}[卡，请逐个格式化各个分区，不能执行]{style="font-family:宋体"}**[format cf]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5885_64750_204072152}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x1109677101}[格式化]{style="font-family:宋体"}[Flash]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> format flash:]{lang="EN-US"}]{#struct_0_x5885_64750_345006516}

[All data on flash: will be lost, continue? \[Y/N\]:y]{lang="EN-US"}

[Formatting flash:\... Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_1488704898}[格式化]{style="font-family:宋体"}[CF]{lang="EN-US"}[卡上的第三个分区。（支持分区）]{style="font-family:宋体"}

[[\<Sysname\> format cfa2:]{lang="EN-US"}]{#struct_0_x5885_64750_x1609741962}

[All data on cfa2: will be lost, continue? \[Y/N\]:y]{lang="EN-US"}

[Formatting cfa2:\... Done.]{lang="EN-US"}
:::::

::: {#345917740 .myid}
[]{#_Toc291763623}[]{#_Toc206926287}[]{#_Toc98563079}[]{#_Toc324860402}[]{#_Toc404782588}[]{#struct_0_x5885_64750_x138804775}[]{#_Toc324860403}

**文件系统管理 \-- 文件系统管理命令 \-- gunzip**

------------------------------------------------------------------------

[**[gunzip]{lang="EN-US"}**]{#struct_0_x5885_64750_534188200}[命令用来解压缩指定的文件。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1861859276}

[**[gunzip ]{lang="EN-US"}***[filename]{lang="EN-US"}*]{#struct_0_x5885_64750_204530904}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1003532255}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5885_64750_x1029218520}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x644887120}

[[network-admin]{lang="EN-US"}]{#struct_0_x5885_64750_552782540}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5885_64750_x95894622}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1995294902}

[*[filename]{lang="EN-US"}*]{#struct_0_x5885_64750_1592828003}[：需要被解压缩的文件名，以]{style="font-family:宋体"}[.gz]{lang="EN-US"}[为后缀。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1561414964}

[[该命令将解压缩并替换当前指定文件。]{style="font-family:宋体"}]{#struct_0_x5885_64750_204465368}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5885_64750_1364247284}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_338986051}[解压缩]{style="font-family:宋体"}[system.bin.gz]{lang="EN-US"}[文件。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[解压缩前查看文件的相关信息。]{style="font-family:宋体"}]{#struct_0_x5885_64750_739536263}

[[\<Sysname\> dir system.\*]{lang="EN-US"}]{#struct_0_x5885_64750_x29796977}

[Directory of flash:]{lang="EN-US"}

[   1 -rw-          20 Jun 14 2012 10:18:53   system.bin.gz]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[472972 KB total (472840 KB free)]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行解压缩操作]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x5885_64750_x1820914414}[。]{style="font-family:宋体"}

[[\<Sysname\> gunzip system.bin.gz]{lang="EN-US"}]{#struct_0_x5885_64750_2020748066}

[Decompressing file flash:/system.bin.gz\..... Done.]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[解压缩后验证执行效果。]{style="font-family:宋体"}]{#struct_0_x5885_64750_204399832}

[[\<Sysname\> dir system.\*]{lang="EN-US"}]{#struct_0_x5885_64750_1853610722}

[Directory of flash:]{lang="EN-US"}

[   1 -rw-           0 May 30 2012 11:42:25   system.bin]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[472972 KB total (472844 KB free)]{lang="EN-US"}
:::

::: {#-394311162 .myid}
[]{#_Toc404782589}[]{#struct_0_x5885_64750_x208722739}

**文件系统管理 \-- 文件系统管理命令 \-- gzip**

------------------------------------------------------------------------

[**[gzip]{lang="EN-US"}**]{#struct_0_x5885_64750_745801810}[命令用来压缩指定的文件。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x291262365}

[**[gzip ]{lang="EN-US"}***[filename]{lang="EN-US"}*]{#struct_0_x5885_64750_830225479}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x639889366}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5885_64750_x2119298223}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5885_64750_204334296}

[[network-admin]{lang="EN-US"}]{#struct_0_x5885_64750_x805941894}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5885_64750_x1832688021}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5885_64750_2100324390}

[*[filename]{lang="EN-US"}*]{#struct_0_x5885_64750_x763958983}[：需要被压缩的文件名。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x921010984}

[[本命令会将]{style="font-family:宋体"}*[filename]{lang="EN-US"}*]{#struct_0_x5885_64750_671154284}[压缩并命名为]{style="font-family:宋体"}*[filename]{lang="EN-US"}*[.gz]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1799422560}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_360244136}[压缩]{style="font-family:宋体"}[system.bin]{lang="EN-US"}[文件。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[压缩前查看文件的相关信息。]{style="font-family:宋体"}]{#struct_0_x5885_64750_204793048}

[[\<Sysname\> dir system.\*]{lang="EN-US"}]{#struct_0_x5885_64750_x292735484}

[Directory of flash:]{lang="EN-US"}

[   1 -rw-           0 May 30 2012 11:42:24   system.bin]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[472972 KB total (472844 KB free)]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行压缩操作。]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x5885_64750_x2023128031}

[[\<Sysname\> gzip system.bin]{lang="EN-US"}]{#struct_0_x5885_64750_x1444669023}

[Compressing file flash:/system.bin\..... Done.]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[压缩后验证执行效果。]{style="font-family:宋体"}]{#struct_0_x5885_64750_842346060}

[[\<Sysname\> dir system.\*]{lang="EN-US"}]{#struct_0_x5885_64750_322063621}

[Directory of flash:]{lang="EN-US"}

[   1 -rw-          20 Jun 14 2012 10:18:53   system.bin.gz]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[472972 KB total (472840 KB free)]{lang="EN-US"}
:::

::: {#503928847 .myid}
[]{#_Toc404782590}[]{#struct_0_x5885_64750_621617923}

**文件系统管理 \-- 文件系统管理命令 \-- md5sum**

------------------------------------------------------------------------

[**[md5sum]{lang="EN-US"}**]{#struct_0_x5885_64750_x576514183}[命令用来使用]{style="font-family:宋体"}[MD5]{lang="EN-US"}[摘要算法计算文件的摘要值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5885_64750_582603987}

[**[md5sum ]{lang="EN-US"}***[file]{lang="EN-US"}*[-*url*]{lang="EN-US"}]{#struct_0_x5885_64750_2027764812}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x49523501}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5885_64750_x356744365}

[[【支持的缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5885_64750_1048518718}

[[network-admin]{lang="EN-US"}]{#struct_0_x5885_64750_1836640268}

[[network-operator]{lang="EN-US"}]{#struct_0_x5885_64750_x2144725805}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5885_64750_620765955}

[*[file]{lang="EN-US"}*[-*url*]{lang="EN-US"}]{#struct_0_x5885_64750_871308975}[：文件名。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5885_64750_1152470765}

[[使用指定的摘要算法对指定的文件计算摘要值，通常用于验证文件的正确性和完整性，防止文件内容被篡改。]{style="font-family:宋体"}]{#struct_0_x5885_64750_x2097798005}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x304042120}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_822085450}[计算]{style="font-family:宋体"}[system.bin]{lang="EN-US"}[文件的]{style="font-family:宋体"}[MD5]{lang="EN-US"}[摘要值。]{style="font-family:宋体"}

[[\<Sysname\> md5sum system.bin]{lang="EN-US"}]{#struct_0_x5885_64750_x1731757051}

[MD5 digest]{lang="EN-US"}[：]{style="font-family:宋体"}

[4f22b6190d151a167105df61c35f0917]{lang="EN-US"}
:::

::: {#-1196816799 .myid}
[]{#_Toc404782591}[]{#struct_0_x5885_64750_1782661737}

**文件系统管理 \-- 文件系统管理命令 \-- mkdir**

------------------------------------------------------------------------

[**[mkdir]{lang="EN-US"}**]{#struct_0_x5885_64750_204727512}[命令用来在当前路径下创建文件夹。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1472079552}

[**[mkdir]{lang="EN-US"}**[ *directory*]{lang="EN-US"}]{#struct_0_x5885_64750_1223759874}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5885_64750_1626098937}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5885_64750_695326906}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x842516599}

[[network-admin]{lang="EN-US"}]{#struct_0_x5885_64750_2040616342}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5885_64750_1650883577}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5885_64750_1719125566}

[*[directory]{lang="EN-US"}*]{#struct_0_x5885_64750_204268761}[：文件夹。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x2004619119}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果创建的文件夹与指定文件夹下的文件或者其它文件夹重名，则创建操作失败。]{style="font-family:宋体"}]{#struct_0_x5885_64750_2117723840}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在使用该命令创建文件夹之前，指定的文件夹必须已经存在。]{style="font-family:宋体"}]{#struct_0_x5885_64750_x221930824}[比如：创建文件夹]{lang="EN-US" style="font-family:宋体"}[flash:/test/mytest]{lang="EN-US"}[，这时，]{lang="EN-US" style="font-family:宋体"}[test]{lang="EN-US"}[文件夹必须已经存在，否则，创建失败。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1713831493}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x1118079415}[在当前路径创建文件夹]{style="font-family:宋体"}[test]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> mkdir test]{lang="EN-US"}]{#struct_0_x5885_64750_x1338208414}

[Creating directory flash:/test\... Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x1571321648}[在当前路径创建文件夹]{style="font-family:宋体"}[test/subtest]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\>mkdir test/subtest]{lang="EN-US"}]{#struct_0_x5885_64750_204203225}

[Creating directory flash:/test/subtest\... Done.]{lang="EN-US"}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_x5885_64750_x1628090844}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x801904712}[登录设备后在备用主控板（所在槽位号为]{style="font-family:宋体"}[1]{lang="EN-US"}[）上创建文件夹]{style="font-family:宋体"}[test]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> mkdir slot1#flash:/test]{lang="EN-US"}]{#struct_0_x5885_64750_338478132}

[Creating directory slot1#flash:/test\... Done.]{lang="EN-US"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[集中式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x5885_64750_x1733368916}[设备]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x766400976}[登录设备后在从设备（成员编号为]{style="font-family:宋体"}[2]{lang="EN-US"}[）上创建文件夹]{style="font-family:宋体"}[test]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> mkdir slot2#flash:/test]{lang="EN-US"}]{#struct_0_x5885_64750_x417914550}

[Creating directory slot2#flash:/test created.]{lang="EN-US"}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_x5885_64750_1280615787}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x479609281}[登录设备后在全局主用主控板上创建文件夹]{style="font-family:宋体"}[test]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> mkdir test]{lang="EN-US"}]{#struct_0_x5885_64750_204137689}

[Creating directory flash:/test\... Done.  ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x1062831337}[登录设备后在全局备用主控板上创建文件夹]{style="font-family:宋体"}[test]{lang="EN-US"}[（该板所在成员设备的编号为]{style="font-family:宋体"}[2]{lang="EN-US"}[，槽位号为]{style="font-family:宋体"}[1]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[\<Sysname\> mkdir chassis2#slot1#flash:/test]{lang="EN-US"}]{#struct_0_x5885_64750_2036388733}

[Creating directory chassis2#slot1#flash:/test\... Done.]{lang="EN-US"}
:::

::: {#109910483 .myid}
[]{#_Toc404782592}[]{#struct_0_x5885_64750_808955088}[]{#_Toc291763624}[]{#_Toc206926288}[]{#_Toc98563080}

**文件系统管理 \-- 文件系统管理命令 \-- more**

------------------------------------------------------------------------

[**[more]{lang="EN-US"}**]{#struct_0_x5885_64750_1418956974}[命令用来显示指定文本文件的内容。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1678316233}

[**[more]{lang="EN-US"}***[ file]{lang="EN-US"}*[-*url*]{lang="EN-US"}]{#struct_0_x5885_64750_x1340873940}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1437875258}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5885_64750_204072153}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1109677102}

[[network-admin]{lang="EN-US"}]{#struct_0_x5885_64750_1911090457}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5885_64750_1083180328}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5885_64750_322795345}

[*[file]{lang="EN-US"}*[-*url*]{lang="EN-US"}]{#struct_0_x5885_64750_x560756723}[：文件名。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1500259066}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_1580783961}[显示文件]{style="font-family:宋体"}[test.txt]{lang="EN-US"}[的内容。]{style="font-family:宋体"}

[[\<Sysname\> more test.txt]{lang="EN-US"}]{#struct_0_x5885_64750_x429587857}

[Have a nice day.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_204530905}[显示文件]{style="font-family:宋体"}[testcfg.cfg]{lang="EN-US"}[的内容。]{style="font-family:宋体"}

[[\<Sysname\> more testcfg.cfg]{lang="EN-US"}]{#struct_0_x5885_64750_x1003532256}

[ ]{lang="EN-US"}

[\#]{lang="EN-US"}

[ version 5.20, Beta 1201, Standard]{lang="EN-US"}

[\#]{lang="EN-US"}

[ sysname Sysname]{lang="EN-US"}

[\#]{lang="EN-US"}

[vlan 2]{lang="EN-US"}

[\#]{lang="EN-US"}

[return]{lang="EN-US"}

[\<Sysname\>]{lang="EN-US"}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_x5885_64750_1699664835}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_348138197}[查看备用主控板（所在槽位号为]{style="font-family:宋体"}[1]{lang="EN-US"}[）上的文件]{style="font-family:宋体"}[testcfg.cfg]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> more slot1#flash:/testcfg.cfg]{lang="EN-US"}]{#struct_0_x5885_64750_204465369}

[ ]{lang="EN-US"}

[\#]{lang="EN-US"}

[ version 5.20, Release 0000]{lang="EN-US"}

[\#]{lang="EN-US"}

[ sysname Test]{lang="EN-US"}

[\#]{lang="EN-US"}

[  \-\-\-- More \-\-\--]{lang="EN-US"}

[["]{style="font-family:宋体"}[\-\-\-- More \-\-\--]{lang="EN-US"}]{#struct_0_x5885_64750_1364247285}["表示这一屏信息已经显示完毕，会暂停显示。按]{style="font-family:宋体"}[\<Enter\>]{lang="EN-US"}[键将接着显示下一行信息；按]{style="font-family:宋体"}[\<Space\>]{lang="EN-US"}[键将接着显示下一屏信息；按]{style="font-family:宋体"}[\<Ctrl+C\>]{lang="EN-US"}[或其它任意键将退出显示。]{style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[集中式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x5885_64750_339051587}[设备]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_1022275168}[查看从设备（成员编号为]{style="font-family:宋体"}[2]{lang="EN-US"}[）上的文件]{style="font-family:宋体"}[testcfg.cfg]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> more slot2#flash:/testcfg.cfg]{lang="EN-US"}]{#struct_0_x5885_64750_x2127505837}

[ ]{lang="EN-US"}

[\#]{lang="EN-US"}

[ version 5.20, Release 0000]{lang="EN-US"}

[\#]{lang="EN-US"}

[ sysname Test]{lang="EN-US"}

[\#]{lang="EN-US"}

[  \-\-\-- More \-\-\--]{lang="EN-US"}

[["]{style="font-family:宋体"}[\-\-\-- More \-\-\--]{lang="EN-US"}]{#struct_0_x5885_64750_x354656174}["表示这一屏信息已经显示完毕，会暂停显示。按]{style="font-family:宋体"}[\<Enter\>]{lang="EN-US"}[键将接着显示下一行信息；按]{style="font-family:宋体"}[\<Space\>]{lang="EN-US"}[键将接着显示下一屏信息；按]{style="font-family:宋体"}[\<Ctrl+C\>]{lang="EN-US"}[或其它任意键将退出显示。]{style="font-family:宋体"}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_x5885_64750_x770296022}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_204399833}[查看全局主用主控板上的文件]{style="font-family:宋体"}[testcfg.cfg]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> more testcfg.cfg]{lang="EN-US"}]{#struct_0_x5885_64750_1853610721}

[ ]{lang="EN-US"}

[\#]{lang="EN-US"}

[ version 5.20, Release 0000]{lang="EN-US"}

[\#]{lang="EN-US"}

[ sysname Sysname]{lang="EN-US"}

[\#]{lang="EN-US"}

[  \-\-\-- More \-\-\--]{lang="EN-US"}

[["]{style="font-family:宋体"}[\-\-\-- More \-\-\--]{lang="EN-US"}]{#struct_0_x5885_64750_x208788275}["表示这一屏信息已经显示完毕，会暂停显示。按]{style="font-family:宋体"}[\<Enter\>]{lang="EN-US"}[键将接着显示下一行信息；按]{style="font-family:宋体"}[\<Space\>]{lang="EN-US"}[键将接着显示下一屏信息；按]{style="font-family:宋体"}[\<Ctrl+C\>]{lang="EN-US"}[或其它任意键将退出显示。]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_670013020}[查看全局备用主控板上的文件]{style="font-family:宋体"}[testcfg.cfg]{lang="EN-US"}[（该板所在设备的成员编号为]{style="font-family:宋体"}[2]{lang="EN-US"}[，槽位号为]{style="font-family:宋体"}[1]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[\<Sysname\> more chassis2#slot1#flash:/testcfg.cfg]{lang="EN-US"}]{#struct_0_x5885_64750_x1575418365}

[ ]{lang="EN-US"}

[\#]{lang="EN-US"}

[ version 5.20, Release 0000]{lang="EN-US"}

[\#]{lang="EN-US"}

[ sysname Sysname]{lang="EN-US"}

[\#]{lang="EN-US"}

[  \-\-\-- More \-\-\--]{lang="EN-US"}

[["]{style="font-family:宋体"}[\-\-\-- More \-\-\--]{lang="EN-US"}]{#struct_0_x5885_64750_193634017}["表示这一屏信息已经显示完毕，会暂停显示。按]{style="font-family:宋体"}[\<Enter\>]{lang="EN-US"}[键将接着显示下一行信息；按]{style="font-family:宋体"}[\<Space\>]{lang="EN-US"}[键将接着显示下一屏信息；按]{style="font-family:宋体"}[\<Ctrl+C\>]{lang="EN-US"}[或其它任意键将退出显示。]{style="font-family:宋体"}
:::

::::: {#2002596174 .myid}
[]{#_Toc404782593}[]{#struct_0_x5885_64750_204334297}[]{#_Toc291763625}[]{#_Toc206926289}[]{#_Toc139421633}

**文件系统管理 \-- 文件系统管理命令 \-- mount**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](文件系统管理命令.files/image001.png){#图片 4 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x5885_64750_x805941895}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_x5885_64750_x1832753557}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[支持]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_x5885_64750_1934747692}[MDC]{lang="EN-US"}[的设备，本命令只在缺省]{style="font-family:\"KaiTi_GB2312\",\"serif\""}[MDC]{lang="EN-US"}[下存在。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}
:::

**[ ]{lang="EN-US"}**

[**[mount]{lang="EN-US"}***[ medium-name]{lang="EN-US"}*]{#struct_0_x5885_64750_2076358370}[命令用来挂载支持热插拔的存储介质。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1226013944}

[**[mount]{lang="EN-US"}**[ *medium-name*]{lang="EN-US"}]{#struct_0_x5885_64750_x523063623}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x279028154}

[[存储介质连接到设备后，自动被挂载，处于挂载状态，即存储介质插入时已经处于连接状态，不需挂载就可使用。]{style="font-family:宋体"}]{#struct_0_x5885_64750_204793049}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x292735485}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5885_64750_x2023062495}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1377343707}

[[network-admin]{lang="EN-US"}]{#struct_0_x5885_64750_x382358300}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x3891279}

[*[medium-name]{lang="EN-US"}*]{#struct_0_x5885_64750_x1726626821}[：存储介质的名称。该参数的具体取值与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5885_64750_476665899}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x5885_64750_x787965267}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在执行挂载操作过程中，禁止对存储介质进行插拔操作。否则，可能会引起文件系统的损坏。（集中式设备）]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x5885_64750_x979268525}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在执行挂载操作过程中，禁止对单板或存储介质进行插拔或主备倒换操作。否则，可能会引起文件系统的损坏。（分布式设备－独立运行模式）]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x5885_64750_204727513}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在执行挂载操作过程中，禁止对存储介质进行插拔或主设备和从设备的倒换操作。否则，可能会引起文件系统的损坏。（集中式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x5885_64750_x1472079551}[设备）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在执行挂载操作过程中，禁止对单板或存储介质进行插拔或全局主用主控板和全局备用主控板的主备倒换操作。否则，可能会引起文件系统的损坏。]{style="font-family:宋体"}]{#struct_0_x5885_64750_1627044401}[（分布式设备－]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在执行挂载操作过程中，禁止执行创建]{style="font-family:宋体"}]{#struct_0_x5885_64750_1544642931}[MDC]{lang="EN-US"}[、删除]{style="font-family:宋体"}[MDC]{lang="EN-US"}[、启动]{style="font-family:宋体"}[MDC]{lang="EN-US"}[、停止]{style="font-family:宋体"}[MDC]{lang="EN-US"}[等操作。否则，可能会引起文件系统的损坏。（支持]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于支持分区的存储介质，请挂载各个分区来完成整个存储介质的挂载。比如，要挂载支持分区的]{style="font-family:宋体"}]{#struct_0_x5885_64750_x1414571428}[CF]{lang="EN-US"}[卡，请逐个挂载各个分区，不能执行]{style="font-family:宋体"}[mount cf]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[处于挂载状态的存储介质在拔出系统前，请先执行卸载操作，以免损坏存储介质。]{style="font-family:宋体"}]{#struct_0_x5885_64750_x1996202060}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5885_64750_1205937688}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[集中式设备]{style="font-family:宋体"}]{#struct_0_x5885_64750_1376878748}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x805728469}[挂载]{style="font-family:宋体"}[CF]{lang="EN-US"}[卡。]{style="font-family:宋体"}

[[\<Sysname\> mount cfa0:]{lang="EN-US"}]{#struct_0_x5885_64750_204268758}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_x5885_64750_x48303992}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_1274418123}[挂载主用主控板上的]{style="font-family:宋体"}[CF]{lang="EN-US"}[卡。]{style="font-family:宋体"}

[[\<Sysname\> mount cfa0:]{lang="EN-US"}]{#struct_0_x5885_64750_x2010280019}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x126696428}[挂载备用主控板（所在槽位号为]{style="font-family:宋体"}[1]{lang="EN-US"}[）上的]{style="font-family:宋体"}[CF]{lang="EN-US"}[卡。]{style="font-family:宋体"}

[[\<Sysname\> mount slot1#cfa0:]{lang="EN-US"}]{#struct_0_x5885_64750_x655484830}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[集中]{style="font-family:宋体"}]{#struct_0_x5885_64750_1501634591}[式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x1036519908}[挂载主设备上的]{style="font-family:宋体"}[CF]{lang="EN-US"}[卡。]{style="font-family:宋体"}

[[\<Sysname\> mount cfa0:]{lang="EN-US"}]{#struct_0_x5885_64750_204203222}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x1628090847}[挂载从设备（成员编号为]{style="font-family:宋体"}[2]{lang="EN-US"}[）上的]{style="font-family:宋体"}[CF]{lang="EN-US"}[卡。]{style="font-family:宋体"}

[[\<Sysname\> mount slot2#cfa0:]{lang="EN-US"}]{#struct_0_x5885_64750_x1205189239}

[[(4)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_x5885_64750_x96283763}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_706302470}[将]{style="font-family:宋体"}[CF]{lang="EN-US"}[卡挂载在主设备上。]{style="font-family:宋体"}

[[\<Sysname\> mount cfa0:]{lang="EN-US"}]{#struct_0_x5885_64750_21171378}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_1900374433}[将]{style="font-family:宋体"}[CF]{lang="EN-US"}[卡挂载在从设备上（成员编号为]{style="font-family:宋体"}[2]{lang="EN-US"}[，本地主用主控板的槽位号为]{style="font-family:宋体"}[1]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[\<Sysname\> mount chassis2#slot1#cfa0:]{lang="EN-US"}]{#struct_0_x5885_64750_1300756092}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5885_64750_266996920}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[umount]{lang="EN-US"}**]{#struct_0_x5885_64750_204137686}
:::::

::: {#-1859457985 .myid}
[]{#_Toc404782594}[]{#struct_0_x5885_64750_x1062831346}[]{#_Toc295910989}

**文件系统管理 \-- 文件系统管理命令 \-- move**

------------------------------------------------------------------------

[**[move]{lang="EN-US"}**]{#struct_0_x5885_64750_470632472}[命令用来移动文件。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5885_64750_1128718641}

[**[move]{lang="EN-US"}**[ *fileurl*-*source fileurl*-*dest*]{lang="EN-US"}]{#struct_0_x5885_64750_x433334181}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5885_64750_866914254}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5885_64750_x1570220371}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x624053311}

[[network-admin]{lang="EN-US"}]{#struct_0_x5885_64750_839278149}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5885_64750_204072150}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1109677103}

[*[fileurl]{lang="EN-US"}*[-*source*]{lang="EN-US"}]{#struct_0_x5885_64750_x817792898}[：源文件名。]{style="font-family:宋体"}

[*[fileurl]{lang="EN-US"}*[-*dest*]{lang="EN-US"}]{#struct_0_x5885_64750_x1063982701}[：目标文件名或者目标文件夹。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5885_64750_101500743}

[[如果使用文件夹作为]{style="font-family:宋体"}*[fileurl]{lang="EN-US"}*[-*dest*]{lang="EN-US"}]{#struct_0_x5885_64750_1273526721}[，则系统会将文件移到指定文件夹，文件名保持不变。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1938034684}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_2077211155}[将文件]{style="font-family:宋体"}[flash:/test/sample.txt]{lang="EN-US"}[移动到]{style="font-family:宋体"}[flash:/]{lang="EN-US"}[，并更名为]{style="font-family:宋体"}[1.txt]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> move test/sample.txt 1.txt]{lang="EN-US"}]{#struct_0_x5885_64750_204530902}

[Move flash:/test/sample.txt to flash:/1.txt? \[Y/N\]:y]{lang="EN-US"}

[Moving file flash:/test/sample.txt to flash:/1.txt \...Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x1003532249}[将文件]{style="font-family:宋体"}[b.cfg]{lang="EN-US"}[移动到文件夹]{style="font-family:宋体"}[test2]{lang="EN-US"}[下。]{style="font-family:宋体"}

[[\<Sysname\> move b.cfg test2]{lang="EN-US"}]{#struct_0_x5885_64750_1652676204}

[Move flash:/b.cfg to flash:/test2/b.cfg? \[Y/N\]:y]{lang="EN-US"}

[Moving file flash:/b.cfg to flash:/test2/b.cfg\... Done.]{lang="EN-US"}
:::

::: {#-1028371258 .myid}
[]{#_Toc404782595}[]{#struct_0_x5885_64750_1233021228}[]{#_Toc291763627}[]{#_Toc206926291}[]{#_Toc98563082}

**文件系统管理 \-- 文件系统管理命令 \-- pwd**

------------------------------------------------------------------------

[**[pwd]{lang="EN-US"}**]{#struct_0_x5885_64750_x1722179454}[命令用来显示当前工作路径。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5885_64750_1742299229}

[**[pwd]{lang="EN-US"}**]{#struct_0_x5885_64750_1997495688}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x640698878}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5885_64750_1565767274}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5885_64750_204465366}

[[network-admin]{lang="EN-US"}]{#struct_0_x5885_64750_1364247294}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5885_64750_338986050}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5885_64750_739536264}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x29796972}[显示当前路径。]{style="font-family:宋体"}

[[\<Sysname\> pwd]{lang="EN-US"}]{#struct_0_x5885_64750_x1820914411}

[flash:]{lang="EN-US"}
:::

::: {#-1934734509 .myid}
[]{#_Toc404782596}[]{#struct_0_x5885_64750_x1514704343}[]{#_Toc291763628}[]{#_Toc206926292}[]{#_Toc98563083}

**文件系统管理 \-- 文件系统管理命令 \-- rename**

------------------------------------------------------------------------

[**[rename]{lang="EN-US"}**]{#struct_0_x5885_64750_439635968}[命令用来重命名文件或文件夹。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5885_64750_1828792864}

[**[rename]{lang="EN-US"}**[ *fileurl*-*source fileurl*-*dest*]{lang="EN-US"}]{#struct_0_x5885_64750_204399830}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5885_64750_1853610724}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5885_64750_x209115955}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5885_64750_1445738467}

[[network-admin]{lang="EN-US"}]{#struct_0_x5885_64750_1038215251}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5885_64750_733793881}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x708009641}

[*[fileurl]{lang="EN-US"}*[-*source*]{lang="EN-US"}]{#struct_0_x5885_64750_x2138830356}[：源文件名或源文件夹。]{style="font-family:宋体"}

[*[fileurl]{lang="EN-US"}*[-*dest*]{lang="EN-US"}]{#struct_0_x5885_64750_240426936}[：目标文件名或目标文件夹。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5885_64750_204334294}

[[若目标文件名或目标文件夹与当前路径下已经存在的文件或目标文件夹重名（不区分大小写，只要字母相同就认为同名），则该操作不执行。]{style="font-family:宋体"}]{#struct_0_x5885_64750_x805941896}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1832819093}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x1898608327}[将文件]{style="font-family:宋体"}[copy.cfg]{lang="EN-US"}[重命名为]{style="font-family:宋体"}[test.cfg]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> rename copy.cfg test.cfg]{lang="EN-US"}]{#struct_0_x5885_64750_716423151}

[Rename flash:/copy.cfg as flash:/test.cfg? \[Y/N\]:y]{lang="EN-US"}

[Renaming flash:/copy.cfg as flash:/test.cfg\... Done.]{lang="EN-US"}
:::

::: {#-32568144 .myid}
[]{#_Toc404782597}[]{#struct_0_x5885_64750_469610142}[]{#_Toc295910990}

**文件系统管理 \-- 文件系统管理命令 \-- reset recycle-bin**

------------------------------------------------------------------------

[**[reset recycle-bin]{lang="EN-US"}**]{#struct_0_x5885_64750_1720503983}[命令用来彻底删除回收站中的文件。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1059548907}

[**[reset recycle-bin]{lang="EN-US"}**[ \[ **/force** \]]{lang="EN-US"}]{#struct_0_x5885_64750_x1262841511}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5885_64750_204793046}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5885_64750_x292735482}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x695840306}

[[network-admin]{lang="EN-US"}]{#struct_0_x5885_64750_495800782}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5885_64750_1491132367}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x2022734815}

[**[/force]{lang="EN-US"}**]{#struct_0_x5885_64750_x438542627}[：表示直接清空回收站，不需要用户对清空操作进行确认。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5885_64750_1616628648}

[[用]{style="font-family:宋体"}**[delete]{lang="EN-US"}**[ *file*-*url*]{lang="EN-US"}]{#struct_0_x5885_64750_x1653233226}[命令删除文件是将文件放在回收站中，但仍然占用存储空间，如果想要把回收站中的该文件删除，必须执行]{style="font-family:宋体"}**[reset recycle-bin]{lang="EN-US"}**[命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x427900416}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x290979394}[回收站中有文件]{style="font-family:宋体"}[a.cfg]{lang="EN-US"}[和]{style="font-family:宋体"}[b.cfg]{lang="EN-US"}[，清空整个回收站。]{style="font-family:宋体"}

[[\<Sysname\> reset recycle-bin]{lang="EN-US"}]{#struct_0_x5885_64750_204727510}

[Clear flash:/a.cfg? \[Y/N\]:y]{lang="EN-US"}

[Clearing file flash:/a.cfg\... Done.]{lang="EN-US"}

[Clear flash:/b.cfg? \[Y/N\]:y]{lang="EN-US"}

[Clearing file flash:/b.cfg\... Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x1472079550}[回收站中有文件]{style="font-family:宋体"}[a.cfg]{lang="EN-US"}[和]{style="font-family:宋体"}[b.cfg]{lang="EN-US"}[，删除]{style="font-family:宋体"}[b.cfg]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> reset recycle-bin]{lang="EN-US"}]{#struct_0_x5885_64750_60960460}

[Clear flash:/a.cfg? \[Y/N\]:n]{lang="EN-US"}

[Clear flash:/b.cfg? \[Y/N\]:y]{lang="EN-US"}

[Clearing file flash:/b.cfg\... Done.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5885_64750_581185857}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[delete]{lang="EN-US"}**]{#struct_0_x5885_64750_x712468594}
:::

::: {#-1201142008 .myid}
[]{#_Toc291763630}[]{#_Toc206926294}[]{#_Toc98563085}[]{#_Toc404782598}[]{#struct_0_x5885_64750_1164497908}

**文件系统管理 \-- 文件系统管理命令 \-- rmdir**

------------------------------------------------------------------------

[**[rmdir]{lang="EN-US"}**]{#struct_0_x5885_64750_1641841541}[命令用来删除文件夹。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1120159892}

[**[rmdir]{lang="EN-US"}**[ *directory*]{lang="EN-US"}]{#struct_0_x5885_64750_171363881}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5885_64750_204137687}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5885_64750_x1062831347}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5885_64750_2036716413}

[[network-admin]{lang="EN-US"}]{#struct_0_x5885_64750_879566660}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5885_64750_1993038665}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5885_64750_387888091}

[*[directory]{lang="EN-US"}*]{#struct_0_x5885_64750_1401891612}[：文件夹名称。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x2014537860}

[[在删除文件夹前，必须先永久删除或者暂时删除文件夹中的所有文件和子文件夹。如果文件只是暂时删除，那么执行]{style="font-family:宋体"}**[rmdir]{lang="EN-US"}**]{#struct_0_x5885_64750_x1124876960}[会导致这些文件从回收站中彻底删除。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5885_64750_204072151}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x1109677104}[删除文件夹]{style="font-family:宋体"}[subtest]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\>rmdir subtest/]{lang="EN-US"}]{#struct_0_x5885_64750_748291043}

[Remove directory flash:/test/subtest and the files in the recycle-bin under this directory will be deleted permanently. Continue? \[Y/N\]:y]{lang="EN-US"}

[Removing directory flash:/test/subtest\... Done.]{lang="EN-US"}
:::

::: {#59838700 .myid}
[]{#_Toc404782599}[]{#struct_0_x5885_64750_x1995999363}[]{#_Toc345335995}[]{#_Toc343522054}

**文件系统管理 \-- 文件系统管理命令 \-- sha256sum**

------------------------------------------------------------------------

[**[sha256sum]{lang="EN-US"}**]{#struct_0_x5885_64750_1658530750}[命令用来使用]{style="font-family:宋体"}[SHA-256]{lang="EN-US"}[摘要算法计算文件的摘要值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1933958040}

[**[sha256sum ]{lang="EN-US"}***[file]{lang="EN-US"}*[-*url*]{lang="EN-US"}]{#struct_0_x5885_64750_204268759}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x48303991}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5885_64750_1274418120}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x2010214483}

[[network-admin]{lang="EN-US"}]{#struct_0_x5885_64750_307648459}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5885_64750_1828388716}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1660561188}

[*[file]{lang="EN-US"}*[-*url*]{lang="EN-US"}]{#struct_0_x5885_64750_248630597}[：文件名。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x202657454}

[[使用指定的摘要算法对指定的文件计算摘要值，通常用于验证文件的正确性和完整性，防止文件内容被篡改。]{style="font-family:宋体"}]{#struct_0_x5885_64750_204203223}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1628090846}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_360894702}[计算]{style="font-family:宋体"}[system.bin]{lang="EN-US"}[文件的]{style="font-family:宋体"}[SHA-256]{lang="EN-US"}[摘要值。]{style="font-family:宋体"}

[[\<Sysname\> sha256sum system.bin]{lang="EN-US"}]{#struct_0_x5885_64750_29980719}

[SHA256 digest]{lang="EN-US"}[：]{style="font-family:宋体"}

[0851e0139f2770e87d01ee8c2995ca9e59a8f5f4062e99af14b141b1a36ca152]{lang="EN-US"}
:::

::: {#1137133929 .myid}
[]{#_Toc404782600}[]{#struct_0_x5885_64750_364742583}[]{#_Toc282529404}[]{#_Toc282529405}[]{#_Toc282529406}[]{#_Toc282529407}[]{#_Toc282529408}[]{#_Toc282529409}[]{#_Toc282529410}[]{#_Toc282529411}[]{#_Toc282529412}[]{#_Toc282529413}[]{#_Toc282529414}[]{#_Toc282529415}[]{#_Toc282529416}[]{#_Toc282529417}[]{#_Toc282529418}[]{#_Toc282529419}[]{#_Toc282529420}[]{#_Toc282529421}[]{#_Toc282529422}[]{#_Toc282529423}[]{#_Toc282529424}[]{#_Toc282529429}[]{#_Toc282529436}[]{#_Toc282529437}[]{#_Toc282529441}[]{#_Toc282529444}[]{#_Toc282529445}[]{#_Toc282529446}[]{#_Toc282529447}[]{#_Toc282529448}[]{#_Toc282529449}[]{#_Toc282529493}

**文件系统管理 \-- 文件系统管理命令 \-- tar create**

------------------------------------------------------------------------

[**[tar create]{lang="EN-US"}**]{#struct_0_x5885_64750_1982848517}[命令用来将多个文件]{style="font-family:宋体"}[/]{lang="EN-US"}[文件夹打包成一个新文件。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x521875055}

[**[tar create ]{lang="EN-US"}**[\[ **gz** \] **archive-file** *file*-*dest* \[ **verbose** \] **source** *file*-*source*&\<1-5\>]{lang="EN-US"}]{#struct_0_x5885_64750_x128932857}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1240929552}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5885_64750_1180083596}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5885_64750_626918094}

[[network-admin]{lang="EN-US"}]{#struct_0_x5885_64750_x179489302}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5885_64750_1123281164}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5885_64750_364808119}

[**[gz]{lang="EN-US"}**]{#struct_0_x5885_64750_615231479}[：表示打包后，再使用]{style="font-family:宋体"}[gzip]{lang="EN-US"}[格式压缩该打包文件。不指定该参数时，表示只打包，不压缩。]{style="font-family:宋体"}

[**[archive-file ]{lang="EN-US"}***[file]{lang="EN-US"}*[-*dest*]{lang="EN-US"}]{#struct_0_x5885_64750_x122735484}[：打包后生成的新文件的名称。当不指定]{style="font-family:宋体"}**[gz]{lang="EN-US"}**[参数时，]{style="font-family:宋体"}*[file]{lang="EN-US"}*[-*dest*]{lang="EN-US"}[的后缀必须为"]{style="font-family:宋体"}[.tar]{lang="EN-US"}["；当指定]{style="font-family:宋体"}**[gz]{lang="EN-US"}**[参数时，]{style="font-family:宋体"}*[file]{lang="EN-US"}*[-*dest*]{lang="EN-US"}[的后缀必须为"]{style="font-family:宋体"}[.tar.gz]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x5885_64750_x1132944462}[：表示在打包过程中逐个显示已经打包的文件和文件夹的名称。不指定该参数时，则不会显示。]{style="font-family:宋体"}

[**[source ]{lang="EN-US"}***[file]{lang="EN-US"}*[-*source*&\<1-5\>]{lang="EN-US"}]{#struct_0_x5885_64750_2058018110}[：表示需要打包的原文件]{style="font-family:
宋体"}[/]{lang="EN-US"}[文件夹列表。当包括文件夹时，则表示打包该文件夹下的所有文件和子文件夹。]{style="font-family:宋体"}[&\<1-5\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[5]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x6832791}

[[执行该命令后，设备会先拷贝原文件]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x5885_64750_x1615383058}[文件夹，再将它们打包成一个新文件后保存。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1109119082}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_489271182}[将文件]{style="font-family:宋体"}[1.cfg]{lang="EN-US"}[、]{style="font-family:宋体"}[2.cfg]{lang="EN-US"}[和文件夹]{style="font-family:宋体"}[test]{lang="EN-US"}[打包后保存到新文件]{style="font-family:宋体"}[a.tar]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> tar create archive-file a.tar source 1.cfg 2.cfg test]{lang="EN-US"}]{#struct_0_x5885_64750_x176959630}

[Creating archive flash:/a.tar Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x1448023696}[将文件]{style="font-family:宋体"}[1.cfg]{lang="EN-US"}[、]{style="font-family:宋体"}[2.cfg]{lang="EN-US"}[和文件夹]{style="font-family:宋体"}[test]{lang="EN-US"}[打包压缩后保存到新文件]{style="font-family:宋体"}[b.tar.gz]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> tar create gz archive-file b.tar.gz source 1.cfg 2.cfg test]{lang="EN-US"}]{#struct_0_x5885_64750_364873655}

[Creating archive flash:/b.tar.gz Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x2047967273}[将文件]{style="font-family:宋体"}[1.cfg]{lang="EN-US"}[、]{style="font-family:宋体"}[2.cfg]{lang="EN-US"}[和文件夹]{style="font-family:宋体"}[test]{lang="EN-US"}[打包压缩后保存到新文件]{style="font-family:宋体"}[c.tar.gz]{lang="EN-US"}[，并在打包过程中逐个显示已经打包的文件和文件夹的名称。]{style="font-family:宋体"}

[[\<Sysname\> tar create gz archive-file c.tar.gz verbose source 1.cfg 2.cfg test]{lang="EN-US"}]{#struct_0_x5885_64750_x120172323}

[1.cfg]{lang="EN-US"}

[2.cfg]{lang="EN-US"}

[test/]{lang="EN-US"}

[test/a.log]{lang="EN-US"}

[test/subtest/]{lang="EN-US"}

[test/subtest/aa.log]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5885_64750_2070669833}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[tar extract]{lang="EN-US"}**]{#struct_0_x5885_64750_x420868268}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[tar list]{lang="EN-US"}**]{#struct_0_x5885_64750_x1135565134}
:::

::: {#-137796397 .myid}
[]{#_Toc404782601}[]{#struct_0_x5885_64750_1675987314}

**文件系统管理 \-- 文件系统管理命令 \-- tar extract**

------------------------------------------------------------------------

[**[tar extract]{lang="EN-US"}**]{#struct_0_x5885_64750_x417760539}[命令用来解包指定文件。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1039215933}

[**[tar extract archive-file]{lang="EN-US"}***[ file]{lang="EN-US"}*[-*dest* \[ **verbose** \] \[ **screen** \| **to** *directory-name* \]]{lang="EN-US"}]{#struct_0_x5885_64750_x449095391}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5885_64750_364939191}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5885_64750_x1746554996}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5885_64750_696145576}

[[network-admin]{lang="EN-US"}]{#struct_0_x5885_64750_2003074256}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5885_64750_x1860769318}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5885_64750_1033548385}

[**[archive-file ]{lang="EN-US"}***[file]{lang="EN-US"}*[-*dest*]{lang="EN-US"}]{#struct_0_x5885_64750_x845760168}[：需要解包的文件的名称，后缀为]{style="font-family:宋体"}[.tar]{lang="EN-US"}[或]{style="font-family:宋体"}[.tar.gz]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x5885_64750_x1645145745}[：在命令行执行过程中，显示]{style="font-family:宋体"}*[file]{lang="EN-US"}*[-*dest*]{lang="EN-US"}[中包含的所有文件]{style="font-family:宋体"}[/]{lang="EN-US"}[文件夹的名称。]{style="font-family:宋体"}

[**[screen]{lang="EN-US"}**]{#struct_0_x5885_64750_227517310}[：不解包，仅将]{style="font-family:宋体"}*[file]{lang="EN-US"}*[-*dest*]{lang="EN-US"}[中包含的原文件的内容输出至登录终端。]{style="font-family:宋体"}

[**[to ]{lang="EN-US"}***[directory-name]{lang="EN-US"}*]{#struct_0_x5885_64750_1473289408}**[：]{style="font-family:宋体"}**[解包至目标路径。]{style="font-family:宋体"}*[directory-name]{lang="EN-US"}*[表示解包后文件的保存路径。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1666704426}

[[执行该命令后，设备会将]{style="font-family:宋体"}*[file]{lang="EN-US"}*[-*dest*]{lang="EN-US"}]{#struct_0_x5885_64750_x801221024}[中包含的文件]{style="font-family:宋体"}[/]{lang="EN-US"}[文件夹解包后保存到目标路径，名称保持不变。保存时会自动覆盖目标路径中已存在的同名文件]{style="font-family:宋体"}[/]{lang="EN-US"}[文件夹。]{style="font-family:宋体"}

[[不指定]{style="font-family:宋体"}**[screen]{lang="EN-US"}**]{#struct_0_x5885_64750_365004727}[和]{style="font-family:宋体"}**[to ]{lang="EN-US"}***[directory-name]{lang="EN-US"}*[参数时，目标路径为用户的当前路径。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5885_64750_1761471564}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x1638348832}[将]{style="font-family:宋体"}[a.tar]{lang="EN-US"}[解包。]{style="font-family:宋体"}

[[\<Sysname\> tar extract archive-file a.tar]{lang="EN-US"}]{#struct_0_x5885_64750_1424294391}

[Extracting archive flash:/a.tar Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x966237779}[将]{style="font-family:宋体"}[a.tar]{lang="EN-US"}[解包，并在解包过程中，显示]{style="font-family:宋体"}[a.tar]{lang="EN-US"}[中包含的所有文件]{style="font-family:宋体"}[/]{lang="EN-US"}[文件夹的名称。]{style="font-family:宋体"}

[[\<Sysname\> tar extract archive-file b.tar.gz verbose]{lang="EN-US"}]{#struct_0_x5885_64750_816402648}

[1.cfg]{lang="EN-US"}

[2.cfg]{lang="EN-US"}

[test/]{lang="EN-US"}

[test/a.log]{lang="EN-US"}

[test/subtest/]{lang="EN-US"}

[test/subtest/aa.log]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x1107351297}[将]{style="font-family:宋体"}[a.tar]{lang="EN-US"}[中包含的原文件的内容直接输出到登录终端。]{style="font-family:宋体"}

[[\<Sysname\> tar extract archive-file c.tar.gz screen]{lang="EN-US"}]{#struct_0_x5885_64750_x1545523957}

[\#]{lang="EN-US"}

[ version 7.1.055, Demo 2501008]{lang="EN-US"}

[\#]{lang="EN-US"}

[ sysname Sysname]{lang="EN-US"}

[\#]{lang="EN-US"}

[[执行以上操作会不解包，直接显示文件内容，剩余的文件内容此处省略。]{style="font-family:宋体"}]{#struct_0_x5885_64750_365070263}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5885_64750_1747661692}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[tar create]{lang="EN-US"}**]{#struct_0_x5885_64750_1401731127}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[tar ]{lang="EN-US"}**]{#struct_0_x5885_64750_336631846}**[list]{lang="EN-US"}**
:::

::: {#-1674595907 .myid}
[]{#_Toc404782602}[]{#struct_0_x5885_64750_x538466805}

**文件系统管理 \-- 文件系统管理命令 \-- tar list**

------------------------------------------------------------------------

[**[tar list]{lang="EN-US"}**]{#struct_0_x5885_64750_1761671516}[命令用来显示指定打包文件中包含的文件]{style="font-family:宋体"}[/]{lang="EN-US"}[文件夹的名称。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1638217691}

[**[tar list archive-file]{lang="EN-US"}***[ file]{lang="EN-US"}*[-*dest*]{lang="EN-US"}]{#struct_0_x5885_64750_x1199542643}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x476818722}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5885_64750_x738042323}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5885_64750_55298790}

[[network-admin]{lang="EN-US"}]{#struct_0_x5885_64750_x269337334}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5885_64750_618287395}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5885_64750_365135799}

[**[archive-file ]{lang="EN-US"}***[file]{lang="EN-US"}*[-*dest*]{lang="EN-US"}]{#struct_0_x5885_64750_x938021897}[：需要显示的打包文件的名称，后缀为]{style="font-family:宋体"}[.tar]{lang="EN-US"}[或]{style="font-family:宋体"}[.tar.gz]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5885_64750_967994635}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x1088614500}[显示]{style="font-family:宋体"}[a.tar]{lang="EN-US"}[中包含的文件]{style="font-family:宋体"}[/]{lang="EN-US"}[文件夹的名称。]{style="font-family:宋体"}

[[\<Sysname\> tar list archive-file a.tar]{lang="EN-US"}]{#struct_0_x5885_64750_1861209549}

[1.cfg]{lang="EN-US"}

[2.cfg]{lang="EN-US"}

[test/]{lang="EN-US"}

[test/a.log]{lang="EN-US"}

[test/subtest/]{lang="EN-US"}

[test/subtest/aa.log]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x843177003}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[tar create]{lang="EN-US"}**]{#struct_0_x5885_64750_x326972988}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[tar extrac]{lang="EN-US"}**]{#struct_0_x5885_64750_1592584955}
:::

::::: {#-1192574898 .myid}
[]{#_Toc404782603}[]{#struct_0_x5885_64750_1225416408}[]{#_Toc295910991}

**文件系统管理 \-- 文件系统管理命令 \-- umount**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](文件系统管理命令.files/image001.png){#图片 5 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x5885_64750_x51623386}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_x5885_64750_x60459997}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[支持]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_x5885_64750_x856945990}[MDC]{lang="EN-US"}[的设备，本命令只在缺省]{style="font-family:\"KaiTi_GB2312\",\"serif\""}[MDC]{lang="EN-US"}[下存在。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}
:::

**[ ]{lang="EN-US"}**

[**[umount]{lang="EN-US"}**]{#struct_0_x5885_64750_1535880176}[命令用来卸载支持热插拔的存储介质。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1062136807}

[**[umount]{lang="EN-US"}***[ medium-name]{lang="EN-US"}*]{#struct_0_x5885_64750_204530903}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1003532250}

[[存储介质连接到设备后，自动被挂载，处于挂载状态。]{style="font-family:宋体"}]{#struct_0_x5885_64750_x1432503047}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x339410332}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5885_64750_346284692}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x1401879166}

[[network-admin]{lang="EN-US"}]{#struct_0_x5885_64750_1478349088}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x2049500241}

[*[medium-name]{lang="EN-US"}*]{#struct_0_x5885_64750_1734814299}[：存储介质的名称。该参数的具体取值与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5885_64750_204465367}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在拔出存储介质前，请先执行卸载操作，以免损坏存储介质。]{style="font-family:宋体"}]{#struct_0_x5885_64750_1364247295}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户对存储介质执行]{style="font-family:宋体"}]{#struct_0_x5885_64750_339051586}**[umount]{lang="EN-US"}**[操作时，如果同时还有其他用户在访问该存储介质，系统会提示]{style="font-family:宋体"}**[umount]{lang="EN-US"}**[操作]{style="font-family:宋体"}[失败。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于支持分区的存储介质，请卸载各个分区来完成整个存储介质的卸载。比如，要卸载支持分区的]{style="font-family:宋体"}]{#struct_0_x5885_64750_1022275167}[CF]{lang="EN-US"}[卡，请逐个卸载各个分区，不能执行]{style="font-family:宋体"}**[umount cf]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在执行挂载操作过程中，禁止执行创建]{style="font-family:宋体"}]{#struct_0_x5885_64750_x2128357805}[MDC]{lang="EN-US"}[、删除]{style="font-family:宋体"}[MDC]{lang="EN-US"}[、启动]{style="font-family:宋体"}[MDC]{lang="EN-US"}[、停止]{style="font-family:宋体"}[MDC]{lang="EN-US"}[等操作。否则，可能会引起文件系统的损坏。（支持]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在执行卸载操作过程中，禁止对存储介质进行插拔操作。否则，可能会引起文件系统的损坏。]{style="font-family:宋体"}]{#struct_0_x5885_64750_x2121776068}[（集中式设备）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在执行卸载操作过程中，禁止对单板或存储介质进行插拔或主备倒换操作。否则，可能会引起文件系统的损坏。（分布式设备－独立运行模式）]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x5885_64750_x954303938}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在执行卸载操作过程中，禁止对存储介质进行插拔或主设备和从设备的倒换操作。否则，可能会引起文件系统的损坏。（集中式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x5885_64750_x2066770854}[设备）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在执行卸载操作过程中，禁止对单板或存储介质进行插拔或全局主用主控板和全局备用主控板的主备倒换操作。否则，可能会引起文件系统的损坏。]{style="font-family:宋体"}]{#struct_0_x5885_64750_x688642923}[（分布式设备－]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5885_64750_204399831}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[集中式设备]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x5885_64750_1853610723}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x208657203}[卸载]{style="font-family:宋体"}[CF]{lang="EN-US"}[卡。]{style="font-family:宋体"}

[[\<Sysname\> umount cfa0:]{lang="EN-US"}]{#struct_0_x5885_64750_x83144843}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_x5885_64750_1341687660}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x1837761401}[卸载主用主控板上的]{style="font-family:宋体"}[CF]{lang="EN-US"}[卡。]{style="font-family:宋体"}

[[\<Sysname\> umount cfa0:]{lang="EN-US"}]{#struct_0_x5885_64750_x255018827}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_195729023}[卸载备用主控板上的]{style="font-family:宋体"}[CF]{lang="EN-US"}[卡（备用主控板在]{style="font-family:宋体"}[5]{lang="EN-US"}[号槽）。]{style="font-family:宋体"}

[[\<Sysname\> umount slot5#cfa0:]{lang="EN-US"}]{#struct_0_x5885_64750_204334295}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[集中]{style="font-family:宋体"}]{#struct_0_x5885_64750_x805941897}[式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x1832884629}[卸载主设备上的]{style="font-family:宋体"}[CF]{lang="EN-US"}[卡。]{style="font-family:宋体"}

[[\<Sysname\> umount cfa0:]{lang="EN-US"}]{#struct_0_x5885_64750_836635896}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x485177120}[卸载从设备（成员编号为]{style="font-family:宋体"}[2]{lang="EN-US"}[）上的]{style="font-family:宋体"}[CF]{lang="EN-US"}[卡。]{style="font-family:宋体"}

[[\<Sysname\> umount slot2#cfa0:]{lang="EN-US"}]{#struct_0_x5885_64750_303211062}

[[(4)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_x5885_64750_360647804}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_197902535}[卸载主设备上的]{style="font-family:宋体"}[CF]{lang="EN-US"}[卡。]{style="font-family:宋体"}

[[\<Sysname\> umount cfa0:]{lang="EN-US"}]{#struct_0_x5885_64750_30511835}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x2125154494}[卸载从设备上的]{style="font-family:宋体"}[CF]{lang="EN-US"}[卡（该设备的成员编号为]{style="font-family:宋体"}[2]{lang="EN-US"}[，本地主用主控板的槽位号为]{style="font-family:宋体"}[5]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[\<Sysname\> umount chassis2#slot5#cfa0:]{lang="EN-US"}]{#struct_0_x5885_64750_204793047}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5885_64750_x292735483}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mount]{lang="EN-US"}**]{#struct_0_x5885_64750_x2022669279}
:::::

::: {#619327589 .myid}
[]{#_Toc404782604}[]{#struct_0_x5885_64750_x1789665758}[]{#_Toc291763632}[]{#_Toc206926296}

**文件系统管理 \-- 文件系统管理命令 \-- undelete**

------------------------------------------------------------------------

[**[undelete]{lang="EN-US"}**]{#struct_0_x5885_64750_703685258}[命令用来恢复未被彻底删除（即存放在回收站里）的文件。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5885_64750_1241048523}

[**[undelete]{lang="EN-US"}**[ *file*-*url*]{lang="EN-US"}]{#struct_0_x5885_64750_1070459056}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5885_64750_1111104267}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5885_64750_x254093452}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5885_64750_204727511}

[[network-admin]{lang="EN-US"}]{#struct_0_x5885_64750_x1472079549}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5885_64750_1983209225}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5885_64750_1041909621}

[*[file]{lang="EN-US"}*[-*url*]{lang="EN-US"}]{#struct_0_x5885_64750_x1918346208}[：要恢复的文件名。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5885_64750_1099651008}

[[如果恢复的文件名与当前存在的文件重名，系统将提示操作者是否覆盖原有文件。如果输入]{style="font-family:宋体"}[\<Y\>]{lang="EN-US"}]{#struct_0_x5885_64750_x1536891952}[，则覆盖源文件；如果输入]{style="font-family:宋体"}[\<N\>]{lang="EN-US"}[，则不再执行恢复操作。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5885_64750_312244566}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_x760623597}[恢复]{style="font-family:宋体"}[flash:]{lang="EN-US"}[下删除的文件]{style="font-family:宋体"}[copy.cfg]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\>undelete copy.cfg]{lang="EN-US"}]{#struct_0_x5885_64750_1770352703}

[Undelete flash:/copy.cfg? \[Y/N\]:y]{lang="EN-US"}

[Undeleting file flash:/copy.cfg\... Done.  ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5885_64750_1614880351}[恢复]{style="font-family:宋体"}[flash:/seclog]{lang="EN-US"}[下删除的文件]{style="font-family:宋体"}[startup.cfg]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[方法一]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x5885_64750_x1496447967}

[[\<Sysname\>undelete seclog/startup.cfg]{lang="EN-US"}]{#struct_0_x5885_64750_x1369293173}

[Undelete flash:/seclog/startup.cfg? \[Y/N\]:y]{lang="EN-US"}

[Undeleting file flash:/seclog/startup.cfg\... Done.]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[方法二]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x5885_64750_2078692339}

[[\<Sysname\> cd seclog]{lang="EN-US"}]{#struct_0_x5885_64750_118362621}

[\<Sysname\> undelete startup.cfg]{lang="EN-US"}

[Undelete flash:/seclog/startup.cfg? \[Y/N\]:y]{lang="EN-US"}

[Undeleting file flash:/seclog/startup.cfg\... Done.]{lang="EN-US"}

[ ]{lang="EN-US"}
:::
