<!-- CMD-INDEX
  cd                                  | 用户视图             | L29
  copy                                | 用户视图             | L147
  delete                              | 用户视图             | L323
  dir                                 | 用户视图             | L511
  fdisk                               | 用户视图             | L727
  file prompt                         | 系统视图             | L871
  fixdisk                             | 用户视图             | L917
  format                              | 用户视图             | L961
  gunzip                              | 用户视图             | L1015
  gzip                                | 用户视图             | L1073
  md5sum                              | 用户视图             | L1131
  mkdir                               | 用户视图             | L1169
  more                                | 用户视图             | L1243
  mount                               | 用户视图             | L1375
  move                                | 用户视图             | L1469
  pwd                                 | 用户视图             | L1517
  rename                              | 用户视图             | L1545
  reset recycle-bin                   | 用户视图             | L1585
  rmdir                               | 用户视图             | L1641
  sha256sum                           | 用户视图             | L1679
  tar create                          | 用户视图             | L1717
  tar extract                         | 用户视图             | L1787
  tar list                            | 用户视图             | L1869
  umount                              | 用户视图             | L1917
  undelete                            | 用户视图             | L2011
-->

**文件系统管理 \-- 文件系统管理命令 \-- cd**

------------------------------------------------------------------------

**[cd**]命令用来修改当前的工作路径。

【命令】

**[cd**[ { *directory \|* **..** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[directory*]：指定目标工作路径。格式为*drive*:/*path*。*drive*和*path*参数的详细解释，请参见"基础配置指导"中的"文件系统管理"。如果没有给出*drive*信息，则表示当前路径下的文件夹。

**[..**]：返回上一级目录。如果当前的工作路径是根目录，则执行**cd ..**后提示出错。该参数不支持命令行在线帮助。

【举例】

\# 登录设备后从根目录进入test文件夹。

\<Sysname\> cd test

\# 返回上一级目录。

\<Sysname\> cd ..

(1)分布式设备－独立运行模式

\# 修改当前的工作路径。

·查看备用主控板所在的槽位号。

\<Sysname\> display device

Slot No.   Brd Type     Brd Status     Subslot Num    Sft Ver          Patch Ver

 0         LSQ1MPUA     Master         0              xx               None

 1         LSQ1MPUA     Standby        0              xx               None

 2         LSQ1GV48SC   Normal         0              xx               None

 3         NONE         Absent         0              NONE             None

通过以上显示信息可以了解到备用主控板所在的槽位号为1。

·进入备用主控板上Flash的根目录。

\<Sysname\> cd slot1#flash:/

·从备用主控板的文件系统切换回主用主控板根目录下的文件夹test。

\<Sysname\> cd flash:/test

(2)集中式IRF设备

\# 登录主设备后进入成员编号为2的从设备Flash的根目录。

\<Sysname\> cd slot2#flash:/

\# 从从设备的文件系统切换回主设备的根目录。

\<Sysname\> cd flash:/

(3)分布式设备－IRF模式

\# 修改当前的工作路径。

·查看全局主用主控板和全局备用主控板所在成员设备的编号以及槽位号。

\<Sysname\> display irf

 Member   Slot   Role    Priority    CPU-Mac

   2      0      Standby 20          00e0-fc0f-8c0f

   2      1      Standby 20          00e0-fc0f-8c1f

 \*+3      5      Master  20          00e0-fc0f-8c22

   3      6      Standby 20          00e0-fc0f-8c32

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 \* indicates the device is the master.

 + indicates the device through which the user logs in.

 The Bridge MAC of the IRF is: 00e0-fc00-0a00

 Auto upgrade                  : yes

 Mac persistent                : 6 min

通过以上显示信息可以了解到：成员设备3上的5号单板为全局主用主控板；成员设备2上的0、1号单板和成员设备3上的6号单板为全局备用主控板。

·登录设备后进入全局主用主控板上Flash的根目录下的test文件夹。

\<Sysname\> cd flash:/test

·登录设备后进入全局备用主控板上Flash的根目录。（该板所在设备的成员编号为2，槽位号为1）

\<Sysname\> cd chassis2#slot1#flash:/

·切换回全局主用主控板Flash的根目录。

\<Sysname\> cd flash:/

**文件系统管理 \-- 文件系统管理命令 \-- copy**

------------------------------------------------------------------------

**[copy**]命令用来复制文件。

【命令】

非FIPS模式下：

**[copy ***fileurl-source fileurl-dest* [ **vpn-instance** *vpn-instance-name*   **source interface** *interface-type interface-number* ]]

FIPS模式下：

**[copy ***fileurl-source fileurl-dest*]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[fileurl*-*source*]：非FIPS模式下，为源文件名或者远程源文件URL；FIPS模式下，为源文件名。若为URL格式，表示从远程文件服务器拷贝文件。远程源文件URL是否支持大小写遵循远程服务器端的规格。

*[fileurl-dest*]：非FIPS模式下，为目标文件名、目标文件夹、远程目标文件URL或远程目录URL；FIPS模式下，为目标文件名或目标文件夹。若为URL格式，表示拷贝文件至远程的目标文件或目标文件夹。远程目标文件URL和远程目录URL是否支持大小写遵循远程服务器端规格。如果使用文件夹作为*fileurl*-*dest*，则系统会将文件复制到指定文件夹，使用源文件名称作为文件名。

**[vpn-instance** *vpn-instance-name*]：连接远程服务器使用的VPN实例名。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示远程服务器位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[source** **interface** *interface-type interface-number*]：指定连接远程服务器时使用的源接口。指定源接口后，设备将使用源接口的主IP作为设备生成的连接报文的源IP。不指定该参数时，则使用路由出接口作为源接口。

【使用指导】

FIPS模式下，不支持远程拷贝功能。

使用**copy**命令：

·当*fileurl-source*和*fileurl-dest*均指定为本地路径时，可以实现本地文件间的拷贝。

·当*fileurl-source*指定为远程服务器上的路径（即为URL格式），*fileurl-dest*指定为本地路径时，可以实现将远程服务器上的文件拷贝到本地。

·当*fileurl-source*指定为本地路径，*fileurl-dest*指定为远程服务器上的路径（即为URL格式）时，可以实现将本地文件拷贝到远程服务器。

当进行远程拷贝时，支持FTP和TFTP协议：

·当采用FTP协议时，URL采用"ftp://FTP用户名:密码@服务器地址:端口号/文件路径"的形式，其中用户名和密码必须和服务器上的配置一致，如果服务器只对用户名进行认证，则不用输入密码。例如URL为ftp://1:1@1.1.1.1/startup.cfg时，表示地址为1.1.1.1的FTP服务器授权目录下的startup.cfg文件，登录用户名为1、密码为1。

·当采用TFTP协议时，URL采用"tftp://服务器地址:端口号/文件路径"的形式。例如URL为tftp://1.1.1.1/startup.cfg时表示地址为1.1.1.1的TFTP服务器工作目录下的startup.cfg文件。

·当采用FTP或TFTP协议时，服务器地址均支持IPv4形式和IPv6形式。当需要使用IPv6地址时，必须用中括号""将IPv6地址括起来，以便将IPv6地址和端口号区分开来。形如ftp://test:test@[2001::1:21/test.cfg]，其中，2001::1为FTP服务器的IPv6地址，21为服务器接收FTP协议报文的端口号。

【举例】

\# 将文件test.cfg在当前文件夹下复制一份，并命名为testbackup.cfg。

\<Sysname\> copy test.cfg testbackup.cfg

Copy flash:/test.cfg to flash:/testbackup.cfg? [Y/N:y]

Copying file flash:/test.cfg to flash:/testbackup.cfg\...Done.

\# 将Flash上文件夹test下的文件1.cfg复制到CF卡第一分区下的文件夹testbackup，并命名为1backup.cfg。

\<Sysname\> copy flash:/test/1.cfg cfa0:/testbackup/1backup.cfg

Copy flash:/test/1.cfg to cfa0:/testbackup/1backup.cfg? [Y/N:y]

Copying file flash:/test/1.cfg to cfa0:/testbackup/1backup.cfg\...Done.

\# 将FTP服务器1.1.1.1上的文件test.cfg拷贝到本地，并命名为testbackup.cfg，FTP服务器的登录用户名为user，密码为private。

\<Sysname\> copy ftp://user:private@1.1.1.1/test.cfg testbackup.cfg

Copy ftp://user:private@1.1.1.1/test.cfg to flash:/testbackup.cfg? [Y/N:y]

Copying file ftp://user:private@1.1.1.1/test.cfg to flash:/testbackup.cfg\... Done.

\# 将文件test.cfg拷贝到FTP服务器1.1.1.1上，并命名为testbackup.cfg，FTP服务器的登录用户名为user，密码为private。

\<Sysname\> copy test.cfg ftp://user:private@1.1.1.1/testbackup.cfg

Copy flash:/test.cfg to ftp://user:private@1.1.1.1/testbackup.cfg? [Y/N:y]

Copying file flash:/test.cfg to ftp://user:private@1.1.1.1/testbackup.cfg\... Done.

\# 将TFTP服务器1.1.1.1上的文件test.cfg拷贝到本地，并命名为testbackup.cfg。

\<Sysname\> copy tftp://1.1.1.1/test.cfg testbackup.cfg

Copy tftp://1.1.1.1/test.cfg to flash:/testbackup.cfg? [Y/N:y]

Copying file tftp://1.1.1.1/test.cfg to flash:/testbackup.cfg\... Done.

\# 将文件test.cfg拷贝到TFTP服务器1.1.1.1上，并命名为testbackup.cfg。

\<Sysname\> copy test.cfg tftp://1.1.1.1/testbackup.cfg

Copy flash:/test.cfg to tftp://1.1.1.1/testbackup.cfg? [Y/N:y]

Copying file flash:/test.cfg to tftp://1.1.1.1/testbackup.cfg\... Done.

\# 将FTP服务器1.1.1.1上的文件test.cfg拷贝到本地，并命名为testbackup.cfg。FTP服务器位于VPN（名称为vpn1）中，登录用户名为user，密码为private。

\<Sysname\> copy ftp://user:private@1.1.1.1/test.cfg testbackup.cfg(ftp://user:private@1.1.1.1/test.cfg%20testbackup.cfg) vpn-instance vpn1

Copy ftp://user:private@1.1.1.1/test.cfg to flash:/testbackup.cfg? [Y/N:y]

Copying file ftp://user:private@1.1.1.1/test.cfg to flash:/testbackup.cfg\... Done.

\# 将TFTP服务器1.1.1.1上的文件test.cfg拷贝到本地，并命名为testbackup.cfg。TFTP服务器位于VPN（名称为vpn1）中。

\<Sysname\> copy tftp://1.1.1.1/test.cfg testbackup.cfg vpn-instance vpn1

Copy tftp://1.1.1.1/test.cfg to flash:/testbackup.cfg? [Y/N:y]

Copying file tftp://1.1.1.1/test.cfg to flash:/testbackup.cfg\... Done.

\# 将FTP服务器2001::1上的文件test.cfg拷贝到本地，并命名为testbackup.cfg，登录用户名为user，密码为private。

\<Sysname\> copy ftp://user:private@2001::1/test.cfg testbackup.cfg(ftp://user:private@%5B2001::1%5D/test.cfg%20testbackup.cfg)

Copy ftp://user:private@[2001::1/test.cfg to flash:/testbackup.cfg? Y/N:y]

Copying file ftp://user:private@[2001::1/test.cfg to flash:/testbackup.cfg\... Done.]

\# 将TFTP服务器2001::1上的文件test.cfg拷贝到本地，并命名为testbackup.cfg。

\<Sysname\> copy tftp://2001::1/test.cfg testbackup.cfg

Copy tftp://[2001::1/test.cfg to flash:/testbackup.cfg? Y/N:y]

Copying file tftp://[2001::1/test.cfg to flash:/testbackup.cfg\... Done.]

(1)分布式设备－独立运行模式

\# 登录设备后将主用主控板的配置文件拷贝到备用主控板的根目录下。

\<Sysname\> copy test.cfg slot1#flash:/

Copy flash:/test.cfg to slot1#flash:/test.cfg? [Y/N:y]

Copying file flash:/test.cfg to slot1#flash:/test.cfg\...Done.

(2)集中式IRF设备

\# 登录设备后将主设备的配置文件拷贝到从设备（成员编号为2）的根目录下。

\<Sysname\> copy test.cfg slot2#flash:/

Copy flash:/test.cfg to slot2#flash:/test.cfg? [Y/N:y]

Copying file flash:/test.cfg to slot2#flash:/test.cfg\...Done.

(3)分布式设备－IRF模式

\# 登录设备后将全局主用主控板的配置文件拷贝到全局备用主控板的根目录下（该板所在的成员设备的编号为1，槽位号为1）。

\<Sysname\> copy test.cfg chassis1#slot1#flash:/

Copy flash:/test.cfg to chassis1#slot1#flash:/test.cfg? [Y/N:y]

Copying file flash:/test.cfg to chassis1#slot1#flash:/test.cfg\...Done.

\# 登录设备后将全局备用主控板（该板所在的成员设备的编号为1，槽位号为1）的配置文件拷贝到另一个全局备用主控板的根目录下（该板所在的成员设备的编号为2，槽位号为1）。

\<Sysname\> copy chassis1#slot1#flash:/test.cfg chassis2#slot1#flash:/

Copy chassis1#slot1#flash:/test.cfg to chassis2#slot1#flash:/test.cfg? [Y/N:y]

Copying file chassis1#slot1#flash:/test.cfg to chassis2#slot1#flash:/test.cfg\...Done.

**文件系统管理 \-- 文件系统管理命令 \-- delete**

------------------------------------------------------------------------

**[delete**]命令用来删除文件。

【命令】

**[delete** [ **/unreserved**  *file*-*url*]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[/unreserved**]：彻底删除该文件。

*[file*-*url*]：要删除的文件名。*file*-*url*参数支持通配符"\*"进行匹配，比如**delete **\*.txt可以删除当前目录下所有以txt为扩展名的文件。

【使用指导】

**[delete** *file*-*url*]命令用来暂时删除文件，被删除的文件被存放在回收站中，可以使用**undelete**命令恢复。

**[delete** **/unreserved** *file*-*url*]命令用来永久删除文件，系统会将该文件从设备上彻底删除。被删除的文件不再存在，不能恢复，请谨慎使用。

请不要对回收站中的文件执行**delete**命令，以免影响回收站功能。若要删除回收站中的文件，请使用**reset recycle-bin**命令。

在同一个目录下，如果先后删除了两个名称相同的文件，回收站中只保留最后一次删除的文件。不同目录下，如果先后删除了名称相同的文件，回收站中会保留这些删除的文件。

当存储介质空间不足时，如果执行**delete** *file*-*url*命令，系统会自动转入永久删除处理流程。

当缺省MDC的管理员执行**delete** *file*-*url*命令删除非缺省MDC存储介质上的文件时，系统会自动转入永久删除处理流程。

【举例】

(1)集中式设备

\# 删除当前目录下的文件1.cfg。

\<Sysname\> delete 1.cfg

Delete flash:/1.cfg? [Y/N:y]

Deleting file flash:/1.cfg\...Done.

\# 永久删除当前目录下的文件1.cfg。

\<Sysname\> delete /unreserved 1.cfg

The file cannot be restored. Delete flash:/1.cfg? [Y/N:y]

Deleting the file permanently will take a long time. Please wait\...

Deleting file flash:/1.cfg\...Done.

(2)分布式设备－独立运行模式

\# 登录设备后删除主用主控板存储介质根目录下的文件1.cfg。

\<Sysname\> delete 1.cfg

Delete flash:/1.cfg? [Y/N:y]

Deleting file flash:/1.cfg\...Done.

\# 登录设备后永久删除主用主控板存储介质根目录下的文件1.cfg。

\<Sysname\> delete /unreserved 1.cfg

The file cannot be restored. Delete flash:/1.cfg? [Y/N:y]

Deleting the file permanently will take a long time. Please wait\...

Deleting file flash:/1.cfg\...Done.

\# 登录设备后删除备用主控板（所在槽位号为1）存储介质根目录下的文件1.cfg。

·方法一

\<Sysname\> delete slot1#flash:/1.cfg

Delete slot1#flash:/1.cfg? [Y/N:y]

Deleting file slot1#flash:/1.cfg\...Done.

·方法二

\<Sysname\> cd slot1#flash:/

\<Sysname\> delete 1.cfg

Delete slot1#flash:/1.cfg? [Y/N:y]

Deleting file slot1#flash:/1.cfg\...Done.

(3)集中式IRF设备

\# 登录设备后删除主设备存储介质根目录下的文件1.cfg。

\<Sysname\> delete 1.cfg

Delete flash:/1.cfg? [Y/N:y]

Deleting file flash:/1.cfg\...Done.

\# 登录设备后永久删除主设备存储介质根目录下的文件1.cfg。

\<Sysname\> delete /unreserved 1.cfg

The file cannot be restored. Delete flash:/1.cfg? [Y/N:y]

Deleting the file permanently will take a long time. Please wait\...

Deleting file flash:/1.cfg\...Done.

\# 登录设备后删除从设备（成员编号为2）存储介质根目录下的文件1.cfg。

·方法一

\<Sysname\> delete slot2#flash:/1.cfg

Delete slot2#flash:/1.cfg? [Y/N:y]

Deleting file slot2#flash:/1.cfg\...Done.

·方法二

\<Sysname\> cd slot2#flash:/

\<Sysname\> delete 1.cfg

Delete slot2#flash:/1.cfg? [Y/N:y]

Deleting file slot2#flash:/1.cfg\...Done.

(4)分布式设备－IRF模式

\# 登录设备后删除全局主用主控板存储介质根目录下的文件1.cfg。

\<Sysname\> delete 1.cfg

Delete flash:/1.cfg? [Y/N:y]

Deleting file flash:/1.cfg\...Done.

\# 登录设备后永久删除全局主用主控板存储介质根目录下的文件1.cfg。

\<Sysname\> delete /unreserved 1.cfg

The file cannot be restored. Delete flash:/1.cfg? [Y/N:y]

Deleting the file permanently will take a long time. Please wait\...

Deleting file flash:/1.cfg\...Done.

\# 登录设备后删除全局备用主控板存储介质根目录下的文件1.cfg（该板所在的成员设备的编号为1，槽位号为1）。

·方法一

\<Sysname\> delete chassis1#slot1#flash:/1.cfg

Delete chassis1#slot1#flash:/1.cfg? [Y/N:y]

Deleting file chassis1#slot1#flash:/1.cfg\...Done.

·方法二

\<Sysname\> cd chassis1#slot1#flash:/

\<Sysname\> delete 1.cfg

Delete chassis1#slot1#flash:/1.cfg? [Y/N:y]

Deleting file chassis1#slot1#flash:/1.cfg\...Done.

【相关命令】

·**undelete**

·**reset recycle-bin**

**文件系统管理 \-- 文件系统管理命令 \-- dir**

------------------------------------------------------------------------

**[dir**]命令用来显示当前文件夹或文件信息。

【命令】

**[dir** [ **/all**  [ *file*-*url* \| **/all-filesystems** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[/all**]：显示当前文件夹下所有的文件及文件夹信息，包括非隐藏文件、非隐藏文件夹、隐藏文件和隐藏文件夹。不指定该参数时，只显示非隐藏文件和非隐藏文件夹。

*[file*-*url*]：显示指定的文件或文件夹的信息。*file*-*url*参数支持通配符"\*"，比如**dir **\*.txt可以显示当前文件夹下所有以txt为扩展名的文件。

**[/all-filesystems**]：显示设备上所有存储介质根目录下的文件及文件夹信息。

【使用指导】

不带任何参数时，用来显示当前文件夹下所有可见文件及文件夹的信息。

回收站文件夹名为".trash"，要查看回收站下有哪些文件，请用**dir /all** .trash，或者**cd** .trash进入回收站文件夹后，再用**dir**命令查看。

【举例】

(1)集中式设备

\# 显示当前文件夹下所有的文件及文件夹信息。

\<Sysname\> dir /all

Directory of flash:/

......略......

本举例用于示意显示信息的大致形式，具体信息与设备型号以及用户配置有关，请以设备的实际情况为准。

\# 显示设备上所有存储介质根目录下的文件及文件夹信息。

\<Sysname\> dir /all-filesystems

Directory of flash:/

......略......

Directory of cfa0:/

......略......

本举例用于示意显示信息的大致形式，具体信息与设备型号以及用户配置有关，请以设备的实际情况为准。

(2)分布式设备－独立运行模式

\# 登录设备后显示当前目录下所有的文件及文件夹信息。

\<Sysname\> dir /all

Directory of flash:/

......略......

本举例用于示意显示信息的大致形式，具体信息与设备型号以及用户配置有关，请以设备的实际情况为准。

\# 显示设备上所有存储介质根目录下的文件及文件夹信息。

\<Sysname\> dir /all-filesystems

Directory of flash:/

......略......

Directory of cfa0:/

......略......

Directory of slot7#flash:/

......略......

Directory of slot7#cfa0:/

......略......

本举例用于示意显示信息的大致形式，具体信息与设备型号以及用户配置有关，请以设备的实际情况为准。

\# 登录设备后显示备用主控板（所在槽位号为1）存储介质中所有的文件及文件夹信息。

\<Sysname\> cd slot1#flash:/

\<Sysname\> dir /all

......略......

本举例用于示意显示信息的大致形式，具体信息与设备型号以及用户配置有关，请以设备的实际情况为准。

(3)集中式IRF设备

\# 登录设备后显示主设备存储介质中所有的文件及文件夹信息。

\<Sysname\> dir /all

Directory of flash:

......略......

本举例用于示意显示信息的大致形式，具体信息与设备型号以及用户配置有关，请以设备的实际情况为准。

\# 显示IRF中所有存储介质根目录下的文件及文件夹信息。

\<Sysname\> dir /all-filesystems

Directory of flash:/

......略......

Directory of slot1#flash:/

......略......

本举例用于示意显示信息的大致形式，具体信息与设备型号以及用户配置有关，请以设备的实际情况为准。

\# 登录设备后显示从设备（成员编号为2）存储介质中所有的文件及文件夹信息。

\<Sysname\> cd slot2#flash:/

\<Sysname\> dir /all

Directory of slot2#flash:/

......略......

本举例用于示意显示信息的大致形式，具体信息与设备型号以及用户配置有关，请以设备的实际情况为准。

(4)分布式设备－IRF模式

\# 登录设备后显示全局主用主控板存储介质中所有的文件及文件夹信息。

\<Sysname\> dir /all

Directory of flash:/

......略......

本举例用于示意显示信息的大致形式，具体信息与设备型号以及用户配置有关，请以设备的实际情况为准。

\# 显示IRF中所有存储介质根目录下的文件及文件夹信息。

\<Sysname\> dir /all-filesystems

Directory of flash:/

......略......

Directory of chassis1#slot1#flash:/

......略......

本举例用于示意显示信息的大致形式，具体信息与设备型号以及用户配置有关，请以设备的实际情况为准。

\# 登录设备后显示全局备用主控板存储介质中所有的文件及文件夹信息（该板所在成员设备的编号为1，槽位号为1）。

·方法一

\<Sysname\> dir /all chassis1#slot1#flash:/

Directory of chassis1#slot1#flash:/

......略......

本举例用于示意显示信息的大致形式，具体信息与设备型号以及用户配置有关，请以设备的实际情况为准。

·方法二

\<Sysname\> cd chassis1#slot1#flash:/

\<Sysname\> dir /all

......略......

本举例用于示意显示信息的大致形式，具体信息与设备型号以及用户配置有关，请以设备的实际情况为准。

表1-1 dir命令显示信息描述表

字段

说明

Directory of

当前显示的目录

0     -rwh      3144  Apr 26 2014 13:45:28  xx.xx

文件或文件夹的信息：

·0表示编号，由系统自动分配

·-rwh表示属性。第一个字符如果是d表示文件夹，如果显示为"-"，则表示它是文件；第二个字符是r，表示本文件或文件夹是可读的；第三个字符是w，表示本文件或文件夹是可写的；第四个字符如果是h，表示本文件或文件夹是隐藏的，如果显示为"-"，则表示它是非隐藏的（请不要修改或删除隐藏文件或文件夹，以免影响对应功能）

·3144表示文件大小，单位为B。如果显示为"-"，则表示它是文件夹

·Apr 26 2014 13:45:28表示最近一次修改的时间

·xx.xx表示名称

**文件系统管理 \-- 文件系统管理命令 \-- fdisk**

------------------------------------------------------------------------

![说明](文件系统管理命令.files/image001.png)

·本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

·支持MDC的设备，本命令只在缺省MDC下存在。

·Flash不支持分区。

****

**[fdisk**]命令用来对存储介质进行分区。

【命令】

**[fdisk** *medium-name* [ *partition-number* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

*[medium-name*]：需要分区的存储介质的名称。该参数的具体取值与设备型号有关，请以设备的实际情况为准。

*[partition-number*]：分区数，取值范围为1～4。

【使用指导】

如果指定分区数则将存储介质平均划分成指定数目的分区，否则，进入交互模式进行分区。

需要注意的是：

·分区操作会清除CF卡/U盘中的所有数据，请务必做好文件备份。

·分区完成后各分区的大小可能与用户指定的大小不一致，但误差小于CF卡/U盘总容量的5％。

·分区后，必须先卸载所有的分区才能安全的拔出CF卡/U盘，否则，可能会引起CF卡/U盘上文件系统的损坏。

·用户对存储介质执行分区操作时，如果同时还有其他用户在访问该存储介质，系统会提示分区失败。

·对U盘进行分区的时候，请确保没有对U盘设置写保护。否则会分区失败，需要重新挂载或者插拔U盘后，才能正常访问U盘。

·本命令不支持对分区进行再分区。如果要修改分区大小，需要重新对整个存储设备进行分区。

【举例】

\# 将设备的CF卡平均分为3个分区。

\<Sysname\> fdisk cfa: 3

Capacity of cfa: : 256M bytes

Cfa: will be divided into the following partitions:

DeviceName      Capacity

cfa0:            85MB

cfa1:            85MB

cfa2:            86MB

All data on cfa: will be lost, continue? [Y/N:y]

Partitioning cfa:\...Done.

\# 使用交互模式将设备的CF卡分为1个分区。

\<Sysname\> fdisk cfa:

The capacity of cfa: : 256M bytes

Partition 1 (32MB\~224MB, 256MB. Press CTRL+C to quit or Enter to use all available space):

*// 按\<Enter\>键或者输入256。*

cfa: will be divided into the following partition(s):

DeviceName    Capacity

cfa0:          256MB

All data on cfa: will be lost, continue? [Y/N:y]

Partitioning cfa:\...Done.

\# 将CF卡分为3个分区，并分别指定3个分区的大小。

\<Sysname\> fdisk cfa:

The capacity of cfa: : 256M bytes

Partition 1 (32MB\~224MB, 256MB, Press CTRL+C to quit or Enter to use all available space):128

将第一个分区的大小指定为128MB（输入128后回车）。

Partition 2 (32MB\~96MB, 128MB, Press CTRL+C to quit or Enter to use all available space):31

将第二个分区的大小指定为31MB（输入31后回车）。

The partition size must be greater than or equal to 32MB.

Partition 2 (32MB\~96MB, 128MB, Press CTRL+C to quit or Enter to use all available space):1000

将第二个分区的大小指定为1000MB（输入1000后回车）。

The partition size must be less than or equal to 128MB.

Partition 2 (32MB\~96MB, 128MB, Press CTRL+C to quit or Enter to use all available space):127

将第二个分区的大小指定为127MB（输入127后回车）。

The remaining space is less than 32MB. Please enter the size of partition 2 again.

Partition 2 (32MB\~96MB, 128MB, Press CTRL+C to quit or Enter to use all available space):

重新指定第二个分区的大小为56MB（输入56后回车）。

Partition 3 (32MB\~40MB, 72MB, Press CTRL+C to quit or Enter to use all available space):

剩余的空间全部划分给第三个分区（直接回车）。

cfa: will be divided into the following partition(s):

DeviceName     Capacity

cfa0:            128MB

cfa1:            56MB

cfa2:            72MB

All data on cfa: will be lost, continue? [Y/N:y]

Partitioning cfa:\...Done.

**文件系统管理 \-- 文件系统管理命令 \-- file prompt**

------------------------------------------------------------------------

**[file prompt**]命令用来设置文件和文件夹操作时是否提示。

**[undo file prompt**]命令用来恢复缺省情况。

【命令】

**[file prompt **[{ **alert** \| **quiet** }]]

**[undo file prompt**]

【缺省情况】

用户对文件进行有危险性的操作时，系统会要求用户进行交互确认。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[alert**]：当用户对文件/文件夹进行有危险性的操作时，系统会要求用户进行交互确认。

**[quiet**]：用户对文件/文件夹进行任何操作，系统均不要求用户进行确认。

【使用指导】

如果将文件/文件夹操作的提示方式设置为**quiet**，则系统对文件/文件夹操作不要求用户进行确认，这样可能会导致一些因误操作而发生的、不可恢复的、对系统造成破坏的操作产生。

【举例】

\# 设置用户对文件进行有危险性的操作时，要求进行交互确认。

\<Sysname\> system-view

Sysname file prompt alert

**文件系统管理 \-- 文件系统管理命令 \-- fixdisk**

------------------------------------------------------------------------

![说明](文件系统管理命令.files/image001.png)

支持MDC的设备，本命令只有缺省MDC支持。

****

**[fixdisk**]命令用来恢复存储介质的空间。

【命令】

**[fixdisk ***medium-name*]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

*[medium-name*]：存储介质的名称。该参数的具体取值与设备型号有关，请以设备的实际情况为准。

【使用指导】

由于异常操作等原因，存储设备的某些空间可能不可用，或者某些空间已经不再需要使用但是没有释放，用户可以通过**fixdisk**命令来恢复存储设备的空间。

用户对存储介质执行**fixdisk**操作时，如果同时还有其他用户在访问该存储介质，系统会提示**fixdisk**操作失败。

【举例】

\# 恢复存储介质Flash的空间。

\<Sysname\> fixdisk flash:

Restoring flash: may take some time\...

Restoring flash:\...Done.

**文件系统管理 \-- 文件系统管理命令 \-- format**

------------------------------------------------------------------------

![说明](文件系统管理命令.files/image001.png)

支持MDC的设备，本命令只在缺省MDC下存在。

****

**[format**]命令用来格式化存储介质。

【命令】

**[format** *medium-name*]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

*[medium-name*]：存储介质的名称。该参数的具体取值与设备型号有关，请以设备的实际情况为准。

【使用指导】

·格式化操作将导致存储设备上的所有文件丢失，并且不可恢复；尤其需要注意的是，如果存储设备上有启动配置文件，格式化该存储设备，将丢失启动配置文件。

·用户对存储介质执行格式化操作时，如果同时还有其他用户在访问该存储介质，系统会提示格式化操作失败。

·对于支持分区的存储设备，请格式化各个分区来完成整个存储设备的格式化。比如，要格式化支持分区的CF卡，请逐个格式化各个分区，不能执行**format cf**。

【举例】

\# 格式化Flash。

\<Sysname\> format flash:

All data on flash: will be lost, continue? [Y/N:y]

Formatting flash:\... Done.

\# 格式化CF卡上的第三个分区。（支持分区）

\<Sysname\> format cfa2:

All data on cfa2: will be lost, continue? [Y/N:y]

Formatting cfa2:\... Done.

**文件系统管理 \-- 文件系统管理命令 \-- gunzip**

------------------------------------------------------------------------

**[gunzip**]命令用来解压缩指定的文件。

【命令】

**[gunzip ***filename*]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[filename*]：需要被解压缩的文件名，以.gz为后缀。

【使用指导】

该命令将解压缩并替换当前指定文件。

【举例】

\# 解压缩system.bin.gz文件。

·解压缩前查看文件的相关信息。

\<Sysname\> dir system.\*

Directory of flash:

   1 -rw-          20 Jun 14 2012 10:18:53   system.bin.gz

472972 KB total (472840 KB free)

·执行解压缩操作。

\<Sysname\> gunzip system.bin.gz

Decompressing file flash:/system.bin.gz\..... Done.

·解压缩后验证执行效果。

\<Sysname\> dir system.\*

Directory of flash:

   1 -rw-           0 May 30 2012 11:42:25   system.bin

472972 KB total (472844 KB free)

**文件系统管理 \-- 文件系统管理命令 \-- gzip**

------------------------------------------------------------------------

**[gzip**]命令用来压缩指定的文件。

【命令】

**[gzip ***filename*]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[filename*]：需要被压缩的文件名。

【使用指导】

本命令会将*filename*压缩并命名为*filename*.gz。

【举例】

\# 压缩system.bin文件。

·压缩前查看文件的相关信息。

\<Sysname\> dir system.\*

Directory of flash:

   1 -rw-           0 May 30 2012 11:42:24   system.bin

472972 KB total (472844 KB free)

·执行压缩操作。

\<Sysname\> gzip system.bin

Compressing file flash:/system.bin\..... Done.

·压缩后验证执行效果。

\<Sysname\> dir system.\*

Directory of flash:

   1 -rw-          20 Jun 14 2012 10:18:53   system.bin.gz

472972 KB total (472840 KB free)

**文件系统管理 \-- 文件系统管理命令 \-- md5sum**

------------------------------------------------------------------------

**[md5sum**]命令用来使用MD5摘要算法计算文件的摘要值。

【命令】

**[md5sum ***file*-*url*]

【视图】

用户视图

【支持的缺省用户角色】

network-admin

network-operator

【参数】

*[file*-*url*]：文件名。

【使用指导】

使用指定的摘要算法对指定的文件计算摘要值，通常用于验证文件的正确性和完整性，防止文件内容被篡改。

【举例】

\# 计算system.bin文件的MD5摘要值。

\<Sysname\> md5sum system.bin

MD5 digest：

4f22b6190d151a167105df61c35f0917

**文件系统管理 \-- 文件系统管理命令 \-- mkdir**

------------------------------------------------------------------------

**[mkdir**]命令用来在当前路径下创建文件夹。

【命令】

**[mkdir** *directory*]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[directory*]：文件夹。

【使用指导】

·如果创建的文件夹与指定文件夹下的文件或者其它文件夹重名，则创建操作失败。

·在使用该命令创建文件夹之前，指定的文件夹必须已经存在。比如：创建文件夹flash:/test/mytest，这时，test文件夹必须已经存在，否则，创建失败。

【举例】

\# 在当前路径创建文件夹test。

\<Sysname\> mkdir test

Creating directory flash:/test\... Done.

\# 在当前路径创建文件夹test/subtest。

\<Sysname\>mkdir test/subtest

Creating directory flash:/test/subtest\... Done.

(1)分布式设备－独立运行模式

\# 登录设备后在备用主控板（所在槽位号为1）上创建文件夹test。

\<Sysname\> mkdir slot1#flash:/test

Creating directory slot1#flash:/test\... Done.

(2)集中式IRF设备

\# 登录设备后在从设备（成员编号为2）上创建文件夹test。

\<Sysname\> mkdir slot2#flash:/test

Creating directory slot2#flash:/test created.

(3)分布式设备－IRF模式

\# 登录设备后在全局主用主控板上创建文件夹test。

\<Sysname\> mkdir test

Creating directory flash:/test\... Done. 

\# 登录设备后在全局备用主控板上创建文件夹test（该板所在成员设备的编号为2，槽位号为1）。

\<Sysname\> mkdir chassis2#slot1#flash:/test

Creating directory chassis2#slot1#flash:/test\... Done.

**文件系统管理 \-- 文件系统管理命令 \-- more**

------------------------------------------------------------------------

**[more**]命令用来显示指定文本文件的内容。

【命令】

**[more*** file*-*url*]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[file*-*url*]：文件名。

【举例】

\# 显示文件test.txt的内容。

\<Sysname\> more test.txt

Have a nice day.

\# 显示文件testcfg.cfg的内容。

\<Sysname\> more testcfg.cfg

\#

 version 5.20, Beta 1201, Standard

\#

 sysname Sysname

\#

vlan 2

\#

return

\<Sysname\>

(1)分布式设备－独立运行模式

\# 查看备用主控板（所在槽位号为1）上的文件testcfg.cfg。

\<Sysname\> more slot1#flash:/testcfg.cfg

\#

 version 5.20, Release 0000

\#

 sysname Test

\#

  \-\-\-- More \-\-\--

"\-\-\-- More \-\-\--"表示这一屏信息已经显示完毕，会暂停显示。按\<Enter\>键将接着显示下一行信息；按\<Space\>键将接着显示下一屏信息；按\<Ctrl+C\>或其它任意键将退出显示。

(2)集中式IRF设备

\# 查看从设备（成员编号为2）上的文件testcfg.cfg。

\<Sysname\> more slot2#flash:/testcfg.cfg

\#

 version 5.20, Release 0000

\#

 sysname Test

\#

  \-\-\-- More \-\-\--

"\-\-\-- More \-\-\--"表示这一屏信息已经显示完毕，会暂停显示。按\<Enter\>键将接着显示下一行信息；按\<Space\>键将接着显示下一屏信息；按\<Ctrl+C\>或其它任意键将退出显示。

(3)分布式设备－IRF模式

\# 查看全局主用主控板上的文件testcfg.cfg。

\<Sysname\> more testcfg.cfg

\#

 version 5.20, Release 0000

\#

 sysname Sysname

\#

  \-\-\-- More \-\-\--

"\-\-\-- More \-\-\--"表示这一屏信息已经显示完毕，会暂停显示。按\<Enter\>键将接着显示下一行信息；按\<Space\>键将接着显示下一屏信息；按\<Ctrl+C\>或其它任意键将退出显示。

\# 查看全局备用主控板上的文件testcfg.cfg（该板所在设备的成员编号为2，槽位号为1）。

\<Sysname\> more chassis2#slot1#flash:/testcfg.cfg

\#

 version 5.20, Release 0000

\#

 sysname Sysname

\#

  \-\-\-- More \-\-\--

"\-\-\-- More \-\-\--"表示这一屏信息已经显示完毕，会暂停显示。按\<Enter\>键将接着显示下一行信息；按\<Space\>键将接着显示下一屏信息；按\<Ctrl+C\>或其它任意键将退出显示。

**文件系统管理 \-- 文件系统管理命令 \-- mount**

------------------------------------------------------------------------

![说明](文件系统管理命令.files/image001.png)

·本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

·支持MDC的设备，本命令只在缺省MDC下存在。

****

**[mount*** medium-name*]命令用来挂载支持热插拔的存储介质。

【命令】

**[mount** *medium-name*]

【缺省情况】

存储介质连接到设备后，自动被挂载，处于挂载状态，即存储介质插入时已经处于连接状态，不需挂载就可使用。

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

*[medium-name*]：存储介质的名称。该参数的具体取值与设备型号有关，请以设备的实际情况为准。

【使用指导】

需要注意的是：

·在执行挂载操作过程中，禁止对存储介质进行插拔操作。否则，可能会引起文件系统的损坏。（集中式设备）

·在执行挂载操作过程中，禁止对单板或存储介质进行插拔或主备倒换操作。否则，可能会引起文件系统的损坏。（分布式设备－独立运行模式）

·在执行挂载操作过程中，禁止对存储介质进行插拔或主设备和从设备的倒换操作。否则，可能会引起文件系统的损坏。（集中式IRF设备）

·在执行挂载操作过程中，禁止对单板或存储介质进行插拔或全局主用主控板和全局备用主控板的主备倒换操作。否则，可能会引起文件系统的损坏。（分布式设备－IRF模式）

·在执行挂载操作过程中，禁止执行创建MDC、删除MDC、启动MDC、停止MDC等操作。否则，可能会引起文件系统的损坏。（支持MDC的设备）

·对于支持分区的存储介质，请挂载各个分区来完成整个存储介质的挂载。比如，要挂载支持分区的CF卡，请逐个挂载各个分区，不能执行mount cf。

·处于挂载状态的存储介质在拔出系统前，请先执行卸载操作，以免损坏存储介质。

【举例】

(1)集中式设备

\# 挂载CF卡。

\<Sysname\> mount cfa0:

(2)分布式设备－独立运行模式

\# 挂载主用主控板上的CF卡。

\<Sysname\> mount cfa0:

\# 挂载备用主控板（所在槽位号为1）上的CF卡。

\<Sysname\> mount slot1#cfa0:

(3)集中式IRF设备

\# 挂载主设备上的CF卡。

\<Sysname\> mount cfa0:

\# 挂载从设备（成员编号为2）上的CF卡。

\<Sysname\> mount slot2#cfa0:

(4)分布式设备－IRF模式

\# 将CF卡挂载在主设备上。

\<Sysname\> mount cfa0:

\# 将CF卡挂载在从设备上（成员编号为2，本地主用主控板的槽位号为1）。

\<Sysname\> mount chassis2#slot1#cfa0:

【相关命令】

·**umount**

**文件系统管理 \-- 文件系统管理命令 \-- move**

------------------------------------------------------------------------

**[move**]命令用来移动文件。

【命令】

**[move** *fileurl*-*source fileurl*-*dest*]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[fileurl*-*source*]：源文件名。

*[fileurl*-*dest*]：目标文件名或者目标文件夹。

【使用指导】

如果使用文件夹作为*fileurl*-*dest*，则系统会将文件移到指定文件夹，文件名保持不变。

【举例】

\# 将文件flash:/test/sample.txt移动到flash:/，并更名为1.txt。

\<Sysname\> move test/sample.txt 1.txt

Move flash:/test/sample.txt to flash:/1.txt? [Y/N:y]

Moving file flash:/test/sample.txt to flash:/1.txt \...Done.

\# 将文件b.cfg移动到文件夹test2下。

\<Sysname\> move b.cfg test2

Move flash:/b.cfg to flash:/test2/b.cfg? [Y/N:y]

Moving file flash:/b.cfg to flash:/test2/b.cfg\... Done.

**文件系统管理 \-- 文件系统管理命令 \-- pwd**

------------------------------------------------------------------------

**[pwd**]命令用来显示当前工作路径。

【命令】

**[pwd**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 显示当前路径。

\<Sysname\> pwd

flash:

**文件系统管理 \-- 文件系统管理命令 \-- rename**

------------------------------------------------------------------------

**[rename**]命令用来重命名文件或文件夹。

【命令】

**[rename** *fileurl*-*source fileurl*-*dest*]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[fileurl*-*source*]：源文件名或源文件夹。

*[fileurl*-*dest*]：目标文件名或目标文件夹。

【使用指导】

若目标文件名或目标文件夹与当前路径下已经存在的文件或目标文件夹重名（不区分大小写，只要字母相同就认为同名），则该操作不执行。

【举例】

\# 将文件copy.cfg重命名为test.cfg。

\<Sysname\> rename copy.cfg test.cfg

Rename flash:/copy.cfg as flash:/test.cfg? [Y/N:y]

Renaming flash:/copy.cfg as flash:/test.cfg\... Done.

**文件系统管理 \-- 文件系统管理命令 \-- reset recycle-bin**

------------------------------------------------------------------------

**[reset recycle-bin**]命令用来彻底删除回收站中的文件。

【命令】

**[reset recycle-bin** [ **/force** ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[/force**]：表示直接清空回收站，不需要用户对清空操作进行确认。

【使用指导】

用**delete** *file*-*url*命令删除文件是将文件放在回收站中，但仍然占用存储空间，如果想要把回收站中的该文件删除，必须执行**reset recycle-bin**命令。

【举例】

\# 回收站中有文件a.cfg和b.cfg，清空整个回收站。

\<Sysname\> reset recycle-bin

Clear flash:/a.cfg? [Y/N:y]

Clearing file flash:/a.cfg\... Done.

Clear flash:/b.cfg? [Y/N:y]

Clearing file flash:/b.cfg\... Done.

\# 回收站中有文件a.cfg和b.cfg，删除b.cfg。

\<Sysname\> reset recycle-bin

Clear flash:/a.cfg? [Y/N:n]

Clear flash:/b.cfg? [Y/N:y]

Clearing file flash:/b.cfg\... Done.

【相关命令】

·**delete**

**文件系统管理 \-- 文件系统管理命令 \-- rmdir**

------------------------------------------------------------------------

**[rmdir**]命令用来删除文件夹。

【命令】

**[rmdir** *directory*]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[directory*]：文件夹名称。

【使用指导】

在删除文件夹前，必须先永久删除或者暂时删除文件夹中的所有文件和子文件夹。如果文件只是暂时删除，那么执行**rmdir**会导致这些文件从回收站中彻底删除。

【举例】

\# 删除文件夹subtest。

\<Sysname\>rmdir subtest/

Remove directory flash:/test/subtest and the files in the recycle-bin under this directory will be deleted permanently. Continue? [Y/N:y]

Removing directory flash:/test/subtest\... Done.

**文件系统管理 \-- 文件系统管理命令 \-- sha256sum**

------------------------------------------------------------------------

**[sha256sum**]命令用来使用SHA-256摘要算法计算文件的摘要值。

【命令】

**[sha256sum ***file*-*url*]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[file*-*url*]：文件名。

【使用指导】

使用指定的摘要算法对指定的文件计算摘要值，通常用于验证文件的正确性和完整性，防止文件内容被篡改。

【举例】

\# 计算system.bin文件的SHA-256摘要值。

\<Sysname\> sha256sum system.bin

SHA256 digest：

0851e0139f2770e87d01ee8c2995ca9e59a8f5f4062e99af14b141b1a36ca152

**文件系统管理 \-- 文件系统管理命令 \-- tar create**

------------------------------------------------------------------------

**[tar create**]命令用来将多个文件/文件夹打包成一个新文件。

【命令】

**[tar create ** **gz** ] **archive-file** *file*-*dest*  **verbose**  **source** *file*-*source*&\<1-5\>

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[gz**]：表示打包后，再使用gzip格式压缩该打包文件。不指定该参数时，表示只打包，不压缩。

**[archive-file ***file*-*dest*]：打包后生成的新文件的名称。当不指定**gz**参数时，*file*-*dest*的后缀必须为".tar"；当指定**gz**参数时，*file*-*dest*的后缀必须为".tar.gz"。

**[verbose**]：表示在打包过程中逐个显示已经打包的文件和文件夹的名称。不指定该参数时，则不会显示。

**[source ***file*-*source*&\<1-5\>]：表示需要打包的原文件/文件夹列表。当包括文件夹时，则表示打包该文件夹下的所有文件和子文件夹。&\<1-5\>表示前面的参数最多可以输入5次。

【使用指导】

执行该命令后，设备会先拷贝原文件/文件夹，再将它们打包成一个新文件后保存。

【举例】

\# 将文件1.cfg、2.cfg和文件夹test打包后保存到新文件a.tar。

\<Sysname\> tar create archive-file a.tar source 1.cfg 2.cfg test

Creating archive flash:/a.tar Done.

\# 将文件1.cfg、2.cfg和文件夹test打包压缩后保存到新文件b.tar.gz。

\<Sysname\> tar create gz archive-file b.tar.gz source 1.cfg 2.cfg test

Creating archive flash:/b.tar.gz Done.

\# 将文件1.cfg、2.cfg和文件夹test打包压缩后保存到新文件c.tar.gz，并在打包过程中逐个显示已经打包的文件和文件夹的名称。

\<Sysname\> tar create gz archive-file c.tar.gz verbose source 1.cfg 2.cfg test

1.cfg

2.cfg

test/

test/a.log

test/subtest/

test/subtest/aa.log

【相关命令】

·**tar extract**

·**tar list**

**文件系统管理 \-- 文件系统管理命令 \-- tar extract**

------------------------------------------------------------------------

**[tar extract**]命令用来解包指定文件。

【命令】

**[tar extract archive-file*** file*-*dest* [ **verbose**  [ **screen** \| **to** *directory-name* ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[archive-file ***file*-*dest*]：需要解包的文件的名称，后缀为.tar或.tar.gz。

**[verbose**]：在命令行执行过程中，显示*file*-*dest*中包含的所有文件/文件夹的名称。

**[screen**]：不解包，仅将*file*-*dest*中包含的原文件的内容输出至登录终端。

**[to ***directory-name*]**：**解包至目标路径。*directory-name*表示解包后文件的保存路径。

【使用指导】

执行该命令后，设备会将*file*-*dest*中包含的文件/文件夹解包后保存到目标路径，名称保持不变。保存时会自动覆盖目标路径中已存在的同名文件/文件夹。

不指定**screen**和**to ***directory-name*参数时，目标路径为用户的当前路径。

【举例】

\# 将a.tar解包。

\<Sysname\> tar extract archive-file a.tar

Extracting archive flash:/a.tar Done.

\# 将a.tar解包，并在解包过程中，显示a.tar中包含的所有文件/文件夹的名称。

\<Sysname\> tar extract archive-file b.tar.gz verbose

1.cfg

2.cfg

test/

test/a.log

test/subtest/

test/subtest/aa.log

\# 将a.tar中包含的原文件的内容直接输出到登录终端。

\<Sysname\> tar extract archive-file c.tar.gz screen

\#

 version 7.1.055, Demo 2501008

\#

 sysname Sysname

\#

执行以上操作会不解包，直接显示文件内容，剩余的文件内容此处省略。

【相关命令】

·**tar create**

·**tar ****list**

**文件系统管理 \-- 文件系统管理命令 \-- tar list**

------------------------------------------------------------------------

**[tar list**]命令用来显示指定打包文件中包含的文件/文件夹的名称。

【命令】

**[tar list archive-file*** file*-*dest*]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[archive-file ***file*-*dest*]：需要显示的打包文件的名称，后缀为.tar或.tar.gz。

【举例】

\# 显示a.tar中包含的文件/文件夹的名称。

\<Sysname\> tar list archive-file a.tar

1.cfg

2.cfg

test/

test/a.log

test/subtest/

test/subtest/aa.log

【相关命令】

·**tar create**

·**tar extrac**

**文件系统管理 \-- 文件系统管理命令 \-- umount**

------------------------------------------------------------------------

![说明](文件系统管理命令.files/image001.png)

·本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

·支持MDC的设备，本命令只在缺省MDC下存在。

****

**[umount**]命令用来卸载支持热插拔的存储介质。

【命令】

**[umount*** medium-name*]

【缺省情况】

存储介质连接到设备后，自动被挂载，处于挂载状态。

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

*[medium-name*]：存储介质的名称。该参数的具体取值与设备型号有关，请以设备的实际情况为准。

【使用指导】

·在拔出存储介质前，请先执行卸载操作，以免损坏存储介质。

·用户对存储介质执行**umount**操作时，如果同时还有其他用户在访问该存储介质，系统会提示**umount**操作失败。

·对于支持分区的存储介质，请卸载各个分区来完成整个存储介质的卸载。比如，要卸载支持分区的CF卡，请逐个卸载各个分区，不能执行**umount cf**。

·在执行挂载操作过程中，禁止执行创建MDC、删除MDC、启动MDC、停止MDC等操作。否则，可能会引起文件系统的损坏。（支持MDC的设备）

·在执行卸载操作过程中，禁止对存储介质进行插拔操作。否则，可能会引起文件系统的损坏。（集中式设备）

·在执行卸载操作过程中，禁止对单板或存储介质进行插拔或主备倒换操作。否则，可能会引起文件系统的损坏。（分布式设备－独立运行模式）

·在执行卸载操作过程中，禁止对存储介质进行插拔或主设备和从设备的倒换操作。否则，可能会引起文件系统的损坏。（集中式IRF设备）

·在执行卸载操作过程中，禁止对单板或存储介质进行插拔或全局主用主控板和全局备用主控板的主备倒换操作。否则，可能会引起文件系统的损坏。（分布式设备－IRF模式）

【举例】

(1)集中式设备

\# 卸载CF卡。

\<Sysname\> umount cfa0:

(2)分布式设备－独立运行模式

\# 卸载主用主控板上的CF卡。

\<Sysname\> umount cfa0:

\# 卸载备用主控板上的CF卡（备用主控板在5号槽）。

\<Sysname\> umount slot5#cfa0:

(3)集中式IRF设备

\# 卸载主设备上的CF卡。

\<Sysname\> umount cfa0:

\# 卸载从设备（成员编号为2）上的CF卡。

\<Sysname\> umount slot2#cfa0:

(4)分布式设备－IRF模式

\# 卸载主设备上的CF卡。

\<Sysname\> umount cfa0:

\# 卸载从设备上的CF卡（该设备的成员编号为2，本地主用主控板的槽位号为5）。

\<Sysname\> umount chassis2#slot5#cfa0:

【相关命令】

·**mount**

**文件系统管理 \-- 文件系统管理命令 \-- undelete**

------------------------------------------------------------------------

**[undelete**]命令用来恢复未被彻底删除（即存放在回收站里）的文件。

【命令】

**[undelete** *file*-*url*]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[file*-*url*]：要恢复的文件名。

【使用指导】

如果恢复的文件名与当前存在的文件重名，系统将提示操作者是否覆盖原有文件。如果输入\<Y\>，则覆盖源文件；如果输入\<N\>，则不再执行恢复操作。

【举例】

\# 恢复flash:下删除的文件copy.cfg。

\<Sysname\>undelete copy.cfg

Undelete flash:/copy.cfg? [Y/N:y]

Undeleting file flash:/copy.cfg\... Done. 

\# 恢复flash:/seclog下删除的文件startup.cfg。

·方法一

\<Sysname\>undelete seclog/startup.cfg

Undelete flash:/seclog/startup.cfg? [Y/N:y]

Undeleting file flash:/seclog/startup.cfg\... Done.

·方法二

\<Sysname\> cd seclog

\<Sysname\> undelete startup.cfg

Undelete flash:/seclog/startup.cfg? [Y/N:y]

Undeleting file flash:/seclog/startup.cfg\... Done.

