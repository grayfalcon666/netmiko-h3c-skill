<!-- CMD-INDEX
  archive configuration               | 用户视图             | L21
  archive configuration interval      | 系统视图             | L75
  archive configuration location      | 系统视图             | L141
  archive configuration max           | 系统视图             | L211
  backup startup-configuration        | 用户视图             | L271
  configuration encrypt               | 系统视图             | L313
  configuration replace file          | 系统视图             | L359
  display archive configuration       | 任意视图             | L403
  display current-configuration       | 任意视图             | L513
  display default-configuration       | 任意视图             | L591
  display saved-configuration         | 任意视图             | L627
  display startup                     | 任意视图             | L709
  display this                        | 任意视图             | L881
  reset saved-configuration           | 用户视图             | L969
  restore startup-configuration       | 用户视图             | L1091
  save                                |                  | L1171
  startup saved-configuration         | 用户视图             | L1397
-->

**配置文件管理 \-- 配置文件管理命令 \-- archive configuration**

------------------------------------------------------------------------

**[archive configuration**]命令用来手工备份当前配置。

【命令】

**[archive configuration**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

设备支持手工和自动两种方式来备份当前配置。执行该命令后，系统会将当前的配置以指定的文件名保存到指定的路径。

需要注意的是：

·执行**archive configuration**命令前必须先执行**archive configuration location**命令来设置备份配置文件的保存路径和文件名前缀。

·执行该命令后，只有主用主控板会备份当前配置，备用主控板不进行备份操作。（分布式设备－独立运行模式）

·执行该命令后，只有主设备会备份当前配置，从设备不进行备份操作。（集中式IRF设备）

·执行该命令后，只有全局主用主控板会备份当前配置，IRF中的其它主控板不进行备份操作。（分布式设备－IRF模式）

【举例】

\# 手工备份当前配置。

\<Sysname\> archive configuration

Save the running configuration to an archive file. Continue? [Y/N: Y]

The archive configuration file myarchive_1.cfg is saved.

【相关命令】

·**archive configuration interval**

·**archive configuration location**

·**archive configuration max**

·**display archive configuration**

**配置文件管理 \-- 配置文件管理命令 \-- archive configuration interval**

------------------------------------------------------------------------

**[archive configuration interval**]命令用来使能自动备份当前配置功能，并设置自动备份的时间间隔。

**[undo archive configuration interval**]用来恢复缺省情况。

【命令】

**[archive configuration interval ***minutes*]

**[undo archive configuration interval**]

【缺省情况】

系统不会自动备份当前配置。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[minutes*]：表示自动备份当前配置的时间间隔，取值范围为10～525600，单位为分钟。（525600分钟相当于365天）

【使用指导】

设备支持手工和自动两种方式来备份当前配置。成功执行本命令后，每隔指定时间（由*minutes*值决定）系统会把当前配置以指定文件名自动保存到指定路径，保存完毕后，重新开始计时，进入下一个周期。

需要注意的是：

·执行**archive configuration interval**命令前必须先执行**archive configuration location**命令来设置备份文件的前缀和保存路径。

·执行该命令后，只有主用主控板会备份当前配置，备用主控板不进行备份操作。（分布式设备－独立运行模式）

·执行该命令后，只有主设备会备份当前配置，从设备不进行备份操作。（集中式IRF设备）

·执行该命令后，只有全局主用主控板会备份当前配置，全局备用主控板不进行备份操作。（分布式设备－IRF模式）

【举例】

\# 设置每隔一小时自动备份当前配置。

\<Sysname\> system-view

Sysname archive configuration interval 60

Archive files will be saved every 60 minutes.

【相关命令】

·**archive configuration**

·**archive configuration location**

·**archive configuration max**

·**display archive configuration**

**配置文件管理 \-- 配置文件管理命令 \-- archive configuration location**

------------------------------------------------------------------------

**[archive configuration location**]命令用来设置备份配置文件的保存路径和文件名前缀。

**[undo archive configuration location**]命令用来恢复缺省情况。

【命令】

**[archive configuration location*** directory* **filename-prefix** *filename-prefix*]

**[undo archive configuration location**]

【缺省情况】

系统没有设置备份配置文件的保存路径和文件名前缀。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[directory*]：表示保存备份配置文件的文件夹的路径，为1～63个字符的字符串，格式为存储介质名:/[文件夹名/]子文件夹名。

*[filename-prefix*]：表示备份配置文件的文件名前缀，为1～30个字符的字符串，只能包含字母、数字、"\_"和"-"。

【使用指导】

自动或手动备份当前配置前必须使用该命令设置备份配置文件的保存路径和文件名前缀。

需要注意的是：

·*directory*必须是主用主控板上已存在的路径，且参数中不能包含槽位号。（分布式设备－独立运行模式）

·*directory*必须是主设备上已存在的路径，且参数中不能包含成员编号。（集中式IRF设备）

·*directory*必须是全局主用主控板上已存在的路径，且参数中不能包含成员编号和槽位号。（分布式设备－IRF模式）

·执行**undo archive configuration location**命令后，用户将不能手工备份当前配置，系统也不再自动备份当前配置，**archive configuration interval**和**archive configuration max**的配置也会恢复到缺省情况，**display archive configuration**的显示信息也会被清除。

【举例】

\# 在flash:/archive/目录下备份配置文件，文件名前缀为my_archive。

\<Sysname\> mkdir flash:/archive

Creating directory flash:/archive\... Done.

\<Sysname\> system-view

Sysname archive configuration location flash:/archive filename-prefix my_archive

【相关命令】

·**archive configuration**

·**archive configuration location**

·**archive configuration max**

·**display archive configuration**

**配置文件管理 \-- 配置文件管理命令 \-- archive configuration max**

------------------------------------------------------------------------

**[archive configuration max**]命令用来设置系统允许保存的备份配置文件的最大数。

**[undo archive configuration max**]用来恢复缺省情况。

【命令】

**[archive configuration max ***file-number*]

**[undo archive configuration max**]

【缺省情况】

系统最多允许保存5个备份配置文件。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[file-number*]：表示可保存的备份配置文件数目上限，取值范围为1～10。该参数的具体数值应根据设备存储介质的空间大小来决定。对于存储空间较小的设备，建议设置*file-number*为较小值。

【使用指导】

备份配置文件数目过多会占用系统内存空间，通过该命令可以控制备份配置文件的数目。当备份配置文件数目到达上限后，下次备份配置文件（包括自动和手动两种触发方式）时，将删除保存时间最早的备份文件，以保存新的备份配置文件。修改备份配置文件数上限时并不删除多余文件，如果当前已有的备份配置文件数大于或等于新设置的上限值，则在备份新的配置时，系统将自动删除生成时间最早的n（n=当前已有备份配置文件数-新设置的上限值+1）个备份配置文件。比如，当前已有备份配置文件数为7，新设置的上限值为4，当有配置需要备份时，系统会先删除"7-4+1=4"个生成时间最早的备份配置文件。

需要注意的是：

·在使用该命令前，必须先执行**archive configuration location**命令设置保存路径和文件名前缀，否则，本命令执行失败。

·执行**undo** **archive configuration location**，系统最多允许保存的备份配置文件数目也会恢复到缺省情况。

【举例】

\# 设置系统最大允许保存10个备份配置文件。

\<Sysname\> system-view

Sysname archive configuration max 10

【相关命令】

·**archive configuration**

·**archive configuration location**

·**archive configuration interval**

·**display archive configuration**

**配置文件管理 \-- 配置文件管理命令 \-- backup startup-configuration**

------------------------------------------------------------------------

**[backup startup-configuration**]命令用于将设备的主用下次启动配置文件备份到指定的TFTP服务器。

【命令】

**[backup startup-configuration to** *tftp-server* [ *dest-filename* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[tftp-server*]：TFTP服务器的IPv4地址或主机名。其中，主机名为1～253个字符的字符串，不区分大小写，字符串仅可包含字母、数字、"-"、"\_"或"."。

*[dest-filename*]：目的文件名，后缀必须为".cfg"。在服务器上将以该文件名保存设备的启动配置文件。不指定该参数时，使用原文件名备份。

【使用指导】

FIPS模式下，不支持本命令。

【举例】

\# 将设备的下次启动配置文件备份到IP地址为2.2.2.2的TFTP服务器上，文件名为192-168-1-26.cfg。

\<Sysname\> backup startup-configuration to 2.2.2.2 192-168-1-26.cfg

Backup next startup-configuration file to 2.2.2.2, please wait...finished。

【相关命令】

·**restore startup-configuration**

**配置文件管理 \-- 配置文件管理命令 \-- configuration encrypt**

------------------------------------------------------------------------

**[configuration encrypt**]命令用来使能配置文件加密功能。

**[undo configuration encrypt**]命令用来关闭配置文件加密功能。

【命令】

**[configuration encrypt**[ { **private-key** \| **public-key** }]]

**[undo configuration encrypt**]

【缺省情况】

配置文件加密功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[private-key**]：使用私钥进行加密。所有运行Comware V7平台软件的H3C设备拥有相同的私钥。

**[public-key**]：使用公钥进行加密。所有运行Comware V7平台软件的H3C设备拥有相同的公钥。

【使用指导】

使能该功能后，每次执行**save**操作，都会先将当前的生效的配置进行加密，再保存。

【举例】

\# 设置保存配置文件时使用公钥进行加密。

\<Sysname\> system-view

Sysname configuration encrypt public-key

**配置文件管理 \-- 配置文件管理命令 \-- configuration replace file**

------------------------------------------------------------------------

**[configuration replace file**]命令用来进行配置回滚。

【命令】

**[configuration replace file** *filename*]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[filename*]：指定用来回滚配置的配置文件名。

【使用指导】

配置回滚是在不重启设备的情况下，将当前的配置回退到指定配置文件中的配置状态。该配置文件必须是有效的.cfg文件，它可以使用手工/自动备份功能或者**save**命令生成，也可以是别的设备的可兼容配置文件，推荐使用手工/自动备份功能生成。如果使用的配置文件不是由**save**命令、自动备份或手工备份生成的完整文件，或是不同类型设备的配置文件，配置回滚可能不能完全恢复至配置文件中的配置状态。因此，需要用户确保回滚配置文件中配置的正确性和与当前设备的兼容性。

本命令中指定的配置文件只能是明文配置文件，不能是被加密的配置文件。否则，不能回滚。

【举例】

\# 将当前配置回滚到配置文件my_archive_1.cfg中的配置状态。

\<Sysname\> system-view

Sysname configuration replace file my_archive_1.cfg

Current configuration will be lost, save current configuration? [Y/N:n]

Now replacing the current configuration. Please wait\...

Succeeded in replacing current configuration with the file my_archive_1.cfg.

**配置文件管理 \-- 配置文件管理命令 \-- display archive configuration**

------------------------------------------------------------------------

**[display archive configuration**]命令用来显示备份配置文件的相关信息。

【命令】

**[display archive configuration**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示备份配置文件的相关信息。

\<Sysname\> display archive configuration

Location: flash:/archive

Filename prefix: my_archive

Archive interval in minutes: 120

Maximum number of archive files: 10

Saved archive files:

  No. TimeStamp                  FileName

  1   Wed Dec 15 14:20:18 2010   my_archive_1.cfg

  2   Wed Dec 15 14:33:10 2010   my_archive_2.cfg

\# 3   Wed Dec 15 14:49:37 2010   my_archive_3.cfg

'#' indicates the most recent archive file.

Next archive file to be saved: my_archive_4.cfg

表1-1 display archive configuration命令显示信息描述表

字段

描述

Location

保存备份配置文件的文件夹的绝对路径

Filename prefix

备份配置文件的文件名前缀

Archive interval in minutes

自动备份配置文件的时间间隔，以分钟为单位

若不自动备份配置文件，不显示此项

Maximum number of archive files

设备可保存的最大备份配置文件数目

Saved archive files

当前已保存的备份配置文件信息

No.

显示已保存的备份配置文件信息的行号

TimeStamp

备份配置文件的保存时间

FileName

备份配置文件名，不包含路径

'#' indicates the most recent archive file.

"\#"表示该行描述的备份配置文件是最近一次备份的

Next archive file to be saved

下次保存备份配置文件将使用的文件名

【相关命令】

·**archive configuration**

·**archive configuration interval**

·**archive configuration location**

·**archive configuration max**

**配置文件管理 \-- 配置文件管理命令 \-- display current-configuration**

------------------------------------------------------------------------

**[display current-configuration**]命令用来显示设备当前生效的配置。

【命令】

**[display current-configuration **[ **configuration** [ *module-name*  \| **interface**  *interface-type* [ *interface-number*  ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[configuration** [ *module-name* ]]：显示具体功能模块的配置信息，*module-name*参数的取值与设备的型号有关，请以设备的实际情况为准。

**[interface** [ *interface-type* [ *interface-number*  ]]]：显示接口的配置。*interface-type*表示接口类型，*interface-number*表示接口编号。

【使用指导】

当用户完成一组配置之后，需要验证是否配置正确，则可以执行**display current-configuration**命令来查看当前生效的参数。对于某些当前配置的参数，如果与缺省参数相同，则不显示。对于某些参数，由于硬件或者规格限制，实际生效值和用户配置值不一致，则显示实际生效值。

【举例】

\# 查看当前设备上本地用户的相关配置。

\<Sysname\> display current-configuration configuration local-user

\#

local-user ftp

 password simple 123

 service-type ftp

 authorization-attribute user-role network-operator

\#

local-user root

 password simple admin

 service-type ssh telnet terminal

 authorization-attribute user-role network-admin

\#

return

\# 查看当前设备上以太网接口的相关配置。

\<Sysname\> display current-configuration interface gigabitethernet

\#

interface GigabitEthernet1/0/1

 port link-mode route

\#

return

**配置文件管理 \-- 配置文件管理命令 \-- display default-configuration**

------------------------------------------------------------------------

**[display default-configuration**]命令用来显示设备的出厂配置。

【命令】

**[display default-configuration**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

设备在出厂时，通常会带有一些基本的配置，称为出厂配置。它用来保证设备在没有配置文件或者配置文件损坏的情况下，能够正常启动、运行。

出厂配置可能与命令行的缺省情况不一致，不同型号的设备会根据需要定制各自的出厂配置。

【举例】

\# 显示设备的出厂配置（不同型号的设备出厂配置不同，请以设备的实际情况为准，具体显示信息略）。

\<Sysname\> display default-configuration

**配置文件管理 \-- 配置文件管理命令 \-- display saved-configuration**

------------------------------------------------------------------------

**[display saved-configuration**]命令用来查看下次启动配置文件的内容。

【命令】

**[display saved-configuration**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

可以在管理/维护设备时使用该命令确认重要的配置是否已经保存到下次启动配置文件。

·如果主用下次启动配置文件存在，执行该命令会显示主用下次启动配置文件的内容；

·如果主用下次启动配置文件不存在，但备用下次启动配置文件存在，执行该命令会显示备用下次启动配置文件的内容；

·如果主用和备用下次启动配置文件均不存在，执行该命令，则不显示任何信息。

【举例】

\# 显示主用下次启动配置文件的内容。

\<Sysname\> display saved-configuration

\#

 version 1.00, Alpha 2009

\#

 sysname Sysname

\#

mdc Admin id 1

\#

 ftp server enable

\#

 telnet server enable

\#

 domain default enable system

\#

vlan 1

\#

domain system

\#

......略......

【相关命令】

·**save**

·**reset saved-configuration**

**配置文件管理 \-- 配置文件管理命令 \-- display startup**

------------------------------------------------------------------------

**[display startup**]命令用来显示用于本次及下次启动的配置文件的名称。

【命令】

**[display startup**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

分布式设备－独立运行模式：

·因为备用主控板是根据主用主控板的当前配置启动和运行的，所以主用主控板和备用主控板显示的当前启动配置文件始终是相同的。

·当主备倒换后，主用主控板和备用主控板的角色交换，新的主用主控板没有从配置文件重启而是沿用当前的配置继续运行，使用**display startup**查看时，所有主控板的当前启动配置文件均会显示为NULL。

集中式IRF设备：

·因为从设备是根据主设备的当前配置启动和运行的，所以IRF中所有成员设备显示的当前启动配置文件始终是相同的。

·当主设备角色变更后，新的主设备没有从配置文件重启而是沿用当前的配置继续运行，使用**display startup**查看时，所有成员设备的当前启动配置文件均会显示为NULL。

【举例】

(1)集中式设备

\# 显示本次及下次启动的配置文件名。

\<Sysname\> display startup

 Current startup saved-configuration file: flash:/startup.cfg

 Next main startup saved-configuration file: flash:/startup.cfg

 Next backup startup saved-configuration file: NULL

表1-2 display startup命令显示信息描述表

字段

描述

Current Startup saved-configuration file

当前启动使用的配置文件

Next main startup saved-configuration file

下一次启动时使用的主用配置文件

Next backup startup saved-configuration file

下一次启动时使用的备用配置文件

(2)分布式设备－独立运行模式/集中式IRF设备

\# 显示本次及下次启动的配置文件名。

\<Sysname\> display startup

MainBoard:

 Current startup saved-configuration file: flash:/startup.cfg

 Next main startup saved-configuration file: flash:/startup.cfg

 Next backup startup saved-configuration file: NULL

Slot 1:

 Current startup saved-configuration file: flash:/startup.cfg

 Next main startup saved-configuration file: flash:/startup.cfg

 Next backup startup saved-configuration file: NULL

表1-3 display startup命令显示信息描述表

字段

描述

MainBoard

主用主控板使用的本次及下次启动的配置文件名

Current startup saved-configuration file

当前启动使用的配置文件

Next startup saved-configuration file

下一次启动时使用的配置文件

Slot *n*

备用主控板（所在槽位号为*n*）使用的本次及下次启动的配置文件名

(3)分布式设备－IRF模式

\# 显示本次及下次启动的配置文件名。

\<Sysname\> display startup

MainBoard:

 Current startup saved-configuration file: NULL

 Next main startup saved-configuration file: flash:/startup.cfg

 Next backup startup saved-configuration file: flash:/startup2.cfg

Chassis 2 Slot 0:

 Current startup saved-configuration file: NULL

 Next main startup saved-configuration file: flash:/startup.cfg

 Next backup startup saved-configuration file: flash:/startup2.cfg

表1-4 display startup命令显示信息描述表

字段

描述

MainBoard

主设备使用的本次及下次启动的配置文件名

Current startup saved-configuration file

当前启动使用的配置文件

Next main startup saved-configuration file

下一次启动时使用的主用配置文件

Next backup startup saved-configuration file

下一次启动时使用的备用配置文件

(This file does not exist.)

表示配置文件不存在

如果用户在配置完下次启动配置文件后又将该文件删除了，这种情况下会在文件名后显示该信息

Chassis 2 Slot 2

成员设备2上的2号单板使用的本次及下次启动的配置文件名

【相关命令】

·**startup saved-configuration**

**配置文件管理 \-- 配置文件管理命令 \-- display this**

------------------------------------------------------------------------

**[display this**]命令用来显示当前视图下生效的配置。

【命令】

**[display** **this**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

当用户在某一视图下完成一组配置之后，需要验证是否配置成功，则可以执行**display this**命令来查看当前生效的配置。

需要注意的是：

·有些已经生效的配置如果与缺省情况相同，则不显示。

·对于某些参数，虽然用户已经配置，但如果这些参数所在的功能没有生效，则不显示。

·在任意一个用户界面视图下执行此命令，将会显示所有用户界面下生效的配置。

【举例】

\# 显示接口GigabitEthernet1/0/1下生效的配置（该显示信息与设备当前的配置有关）。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 display this

\#

interface GigabitEthernet1/0/1

 port link-mode route

\#

return

\# 显示所有用户界面下生效的配置（该显示信息与设备当前的配置有关）。

\<Sysname\> system-view

Sysname line vty 0

Sysname-line-vty0 display this

\#

line aux 0

 user-role network-operator

\#

line con 0

 user-role network-admin

\#

line vty 0 4

 authentication-mode none

 user-role network-admin

\#

return

**配置文件管理 \-- 配置文件管理命令 \-- reset saved-configuration**

------------------------------------------------------------------------

**[reset saved-configuration**]命令用来删除设备存储介质中保存的下次启动配置文件。

【命令】

**[reset saved-configuration **[[ **backup** \| **main** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[backup**]：删除备用下次启动配置文件。

**[main**]：删除主用下次启动配置文件。

【使用指导】

·删除操作会将配置文件从设备上彻底删除，所以请慎用该命令。（集中式设备/分布式设备－独立运行模式）

·删除操作会将配置文件从所有成员设备上彻底删除，所以请慎用该命令。（集中式IRF设备/分布式设备－IRF模式）

·对于支持主备用下次启动配置文件的设备，如果当前设备的主备用下次启动配置文件相同，仅执行一次删除操作（假设指定了**backup**参数），系统只会将相应的下次启动配置文件设置为NULL，不会删除该文件，需要再执行一次删除操作（指定**main**参数），才能将这个配置文件彻底删除。

·不指定**backup**和**main**参数时，缺省使用**main**。

【举例】

(1)集中式设备

\# 删除主用下次启动配置文件。

\<Sysname\> reset saved-configuration

The saved configuration file will be erased. Are you sure? [Y/N:y]

Configuration file in flash: is being cleared.

Please wait \...\...\.....

Configuration file is cleared.

(2)分布式设备－独立运行模式

\# 删除主用下次启动配置文件。

\<Sysname\> reset saved-configuration

The saved configuration file will be erased. Are you sure? [Y/N:y]

Configuration file in flash: is being cleared.

Please wait \...

..

MainBoard:

Configuration file is cleared.

Slot 1:

Erase next configuration file successfully

(3)集中式IRF设备

\# 删除备用下次启动配置文件。

\<Sysname\> reset saved-configuration backup

The saved configuration file will be erased. Are you sure? [Y/N:y]

Configuration file in flash: is being cleared.

Please wait \...

..

MainBoard:

Configuration file is cleared.

Slot 2:

Erase next configuration file successfully

(4)分布式设备－IRF模式

\# 删除备用下次启动配置文件。

\<Sysname\> reset saved-configuration backup

The saved configuration file will be erased. Are you sure? [Y/N:y]

Configuration file in flash: is being cleared.

Please wait \...

..

MainBoard:

Configuration file is cleared.

Chassis 2 Slot 2:

Erase next configuration file successfully

【相关命令】

·**display saved-configuration**

**配置文件管理 \-- 配置文件管理命令 \-- restore startup-configuration**

------------------------------------------------------------------------

**[restore startup-configuration**]命令用于从指定TFTP服务器上下载配置文件并设置为设备的主用下次启动配置文件。

【命令】

**[restore startup-configuration from** *tftp-server src-filename*]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[tftp-server*]：TFTP服务器的IPv4地址或主机名。其中，主机名为1～253个字符的字符串，不区分大小写，字符串仅可包含字母、数字、"-"、"\_"或"."。

*[src-filename*]：源文件名，TFTP服务器上将要下载的文件的文件名。

【使用指导】

·FIPS模式下，不支持本命令。

·执行该命令会将指定配置文件下载到主用主控板和备用主控板存储介质的根目录下（对于支持存储设备分区的设备，该目录为存储设备的第一个分区），并设置为主用主控板和备用主控板的下次启动配置文件。对于主用主控板和备用主控板使用不同存储介质的情况（如，主用主控板使用Flash，而备用主控板使用CF卡），备份操作失败。（分布式设备－独立运行模式）

·执行该命令会将指定配置文件下载到所有成员设备存储介质的根目录下（对于支持存储设备分区的设备，该目录为存储设备的第一个分区），并设置为所有成员设备的主用下次启动配置文件。对于成员设备使用不同存储介质的情况（如，主设备使用Flash，而从设备使用CF卡），备份操作失败。（集中式IRF设备）

·执行该命令会将指定配置文件下载到所有主控板存储介质的根目录下（对于支持存储设备分区的设备，该目录为存储设备的第一个分区），并设置为所有主控板的主用下次启动配置文件。对于主控板使用不同存储介质的情况（如，有些主控板使用Flash，而有些主控板使用CF卡），备份操作失败。（分布式设备－IRF模式）

【举例】

(1)集中式设备

\# 从IP地址为2.2.2.2的TFTP服务器上下载test.cfg文件作为设备的下次启动配置文件。

\<Sysname\> restore startup-configuration from 2.2.2.2 test.cfg

Restoring the next startup-configuration file from 2.2.2.2. Please wait\...finished。

(2)分布式设备－独立运行模式

\# 从IP地址为2.2.2.2的TFTP服务器上下载config.cfg文件作为设备的主用下次启动配置文件。

\<Sysname\> restore startup-configuration from 2.2.2.2 config.cfg

Restoring the next startup-configuration file from 2.2.2.2. Please wait\...finished.

Now restoring the next startup-configuration file from main board to backup board. Please wait\...finished。

(3)集中式IRF设备

\# 从IP地址为2.2.2.2的TFTP服务器上下载config.cfg文件作为设备的主用下次启动配置文件。

\<Sysname\> restore startup-configuration from 2.2.2.2 config.cfg

Restoring the next startup-configuration file from 2.2.2.2. Please wait\...finished.

Now restoring the next startup-configuration file from main board to backup board. Please wait\...finished.

(4)分布式设备－IRF模式

\# 从IP地址为2.2.2.2的TFTP服务器上下载config.cfg文件作为设备的主用下次启动配置文件。

\<Sysname\> restore startup-configuration from 2.2.2.2 config.cfg

Restoring the next startup-configuration file from 2.2.2.2. Please wait\...finished.

Now restoring the next startup-configuration file from main board to backup board. Please wait\...finished.

【相关命令】

·**backup startup-configuration**

**配置文件管理 \-- 配置文件管理命令 \-- save**

------------------------------------------------------------------------

·集中式设备

**[save** *file-url*]命令用来将设备的当前配置保存到指定文件，但不会将该文件设置为下次启动配置文件。

**[save** [ **safely**  [ **backup** \| **main** ]  **force** ]]命令用来将设备的当前配置保存到存储介质的根目录，并将该文件设置为下次启动配置文件。（不支持MDC的设备）

**[save** [ **safely**  [ **backup** \| **main** ]  **force**   **mdc-all** ]]命令用来将MDC的当前配置保存到存储介质的根目录，并将该文件设置为下次启动配置文件。（支持MDC的设备）

·分布式设备－独立运行模式

**[save**[ *file-url* [ **all** \| **slot** *slot-number* ]]]命令用来将设备的当前配置保存到指定文件，但不会将该文件设置为下次启动配置文件。

**[save** [ **safely**  [ **backup** \| **main** ]  **force** ]]命令用来将设备的当前配置保存到主用主控板和备用主控板存储介质的根目录，并将该文件设置为下次启动配置文件。（不支持MDC的设备）

**[save** [ **safely**  [ **backup** \| **main** ]  **force**   **mdc-all** ]]命令用来将MDC的当前配置保存到主用主控板和备用主控板存储介质的根目录，并将该文件设置为下次启动配置文件。（支持MDC的设备）

·集中式IRF设备

**[save**[ *file-url* [ **all** \| **slot** *slot-number* ]]]命令用来将设备的当前配置保存到指定文件，但不会将该文件设置为下次启动配置文件。

**[save** [ **safely**  [ **backup** \| **main** ]  **force** ]]命令用来将设备的当前配置保存到所有成员设备存储介质的根目录，并将该文件设置为下次启动配置文件。（不支持MDC的设备）

**[save** [ **safely**  [ **backup** \| **main** ]  **force**   **mdc-all** ]]命令用来将MDC的当前配置保存到主用主控板和备用主控板存储介质的根目录，并将该文件设置为下次启动配置文件。（支持MDC的设备）

·分布式设备－IRF模式

**[save*** file-url*[ [ **all** \| **chassis** *chassis-number* **slot** *slot-number* ]]]命令用来将设备的当前配置保存到指定文件，但不会将该文件设置为下次启动配置文件。

**[save** [ **safely**  [ **backup** \| **main** ]  **force** ]]命令用来将设备的当前配置保存到所有主控板存储介质的根目录，并将该文件设置为下次启动配置文件。（不支持MDC的设备）

**[save** [ **safely**  [ **backup** \| **main** ]  **force**   **mdc-all** ]]命令用来将MDC的当前配置保存到主用主控板和备用主控板存储介质的根目录，并将该文件设置为下次启动配置文件。（支持MDC的设备）

【命令】

集中式设备：

**[save** *file-url*]

**[save** [ **safely**  [ **backup** \| **main** ]  **force**   **mdc-all** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[save**[ *file-url* [ **all** \| **slot** *slot-number* ]]]

**[save** [ **safely**  [ **backup** \| **main** ]  **force**   **mdc-all** ]]

分布式设备－IRF模式：

**[save**[ *file-url* [ **all** \| **chassis** *chassis-number* **slot** *slot-number* ]]]

**[save** [ **safely**  [ **backup** \| **main** ]  **force**   **mdc-all** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[file-url*]：文件路径，文件名部分必须以".cfg"为后缀。（集中式设备）

*[file-url*]：文件路径，文件名部分必须以".cfg"为后缀。当本参数和关键字**all**或者**slot**一起使用时，本参数不能包含槽位号；如果路径中包含了文件夹，则必须先在相应的主控板上创建该文件夹，否则该主控板上的保存操作将失败。（分布式设备－独立运行模式）

*[file-url*]：文件路径，必须以".cfg"为后缀。当本参数和关键字**all**或者**slot**一起使用时，本参数不能包含成员编号，如果路径中包含了文件夹，则必须先在相应的成员设备上创建该文件夹，否则本成员设备上的保存操作将失败。（集中式IRF设备）

*[file-url*]：文件路径，文件名部分必须以".cfg"为后缀。当本参数和关键字**all**或者**chassis**一起使用时，本参数不能包含成员编号和槽位号；如果路径中包含了文件夹，则必须先在相应的主控板上创建该文件夹，否则该主控板上的保存操作将失败。（分布式设备－IRF模式）

**[all**]：将当前配置以指定的名称保存到所有主控板。不指定**all**或**slot**参数，则保存到主用主控板上。（分布式设备－独立运行模式）

**[all**]**：**将当前配置以指定的名称保存到所有成员设备。不指定**all**和**slot**参数，则保存到Master上。（集中式IRF设备）

**[all**]**：**将当前配置以指定的名称保存到所有主控板。不指定**all**和**chassis*** chassis-number* **slot** *slot-number*参数，则保存到全局主用主控板上（分布式设备－IRF模式）

**[slot ***slot-number*]：将当前配置以指定的名称保存到备用主控板。*slot-number*表示单板所在的槽位号。不指定**all**或**slot**参数，则保存到主用主控板上。（分布式设备－独立运行模式）

**[slot ***slot-number*]：将当前配置以指定的名称保存到指定从设备。*slot-number*表示设备在IRF中的成员编号。不指定**all**和**slot**参数，则保存到Master上。（集中式IRF设备）

**[chassis** *chassis-number* **slot** *slot-number*]：将当前配置以指定的名称保存到指定主控板。*chassis-numbe*r表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定**all**和**chassis*** chassis-number* **slot** *slot-number*参数，则保存到全局主用主控板上（分布式设备－IRF模式）

**[safely**]：以安全模式保存配置文件。如果不指定该参数，表示以快速保存方式保存配置文件。

**[backup**]：将该文件设置为备用下次启动配置文件。当不指定**backup**和**main**时，系统缺省使用**main**。

**[main**]：将该文件设置为主用下次启动配置文件。当不指定**backup**和**main**时，系统缺省使用**main**。

**[force**]：表示直接将当前配置保存到主用下次启动配置文件，系统不再输出交互信息。缺省情况下，用户执行**save**命令，系统要求用户输入\<Y\>或\<N\>等参数来确认本次操作，如果在30秒内没有确认，系统会自动退出本次操作。如果在执行**save**操作时使用了**force**参数，则系统会直接保存当前配置，不再需要用户输入任何信息。

**[mdc-all**]：保存设备上所有MDC内的配置。不指定该参数时，只保存用户当前登录的MDC的当前配置。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

当执行**save**命令时，如果指定的文件名不存在，则系统会先创建该文件，再执行保存操作。如果指定的文件名存在，则会提示用户是否覆盖该文件，如果用户选择不覆盖，则不会继续执行**save**命令。

[当执行**save** [ **safely**  [ **backup** \| **main** ]  **force**   **mdc-all** ]]命令输入的文件名和设备上已存在的文件同名时，

·如果使用了**safely**参数，则系统会先将当前配置保存到一个临时文件，保存成功后，再用这个临时文件替换原同名文件。因此，即使在保存过程中出现设备重启、断电等问题导致配置保存失败，仍然能够以原同名的配置文件启动设备。

·如果没有使用**safely**参数，则会直接覆盖原同名文件。在保存过程中如果出现设备重启、断电、内存不足等问题，结果是当前配置保存失败，原同名文件已删除，下次启动文件为空。

因此，为了安全起见，在需要将当前配置保存到下次启动配置文件的时候，建议选用**safely**参数。

【举例】

\# 将当前配置文件保存到指定配置文件backup.cfg，但不将该文件设置为下次启动配置文件。

\<Sysname\> save backup.cfg

The current configuration will be saved to flash:/backup.cfg. Continue? [Y/N:y]

Now saving current configuration to the device.

Saving configuration

flash:/backup.cfg. Please wait\...

Configuration is saved to flash successfully.

\# 直接将当前配置保存到主用下次启动配置文件，不再进行信息确认。

\<Sysname\> save force

Validating file. Please wait\....

Configuration is saved to device successfully.

\# 将当前配置保存到存储介质的根目录，并将该文件设置为下次启动配置文件。（集中式设备）

\<Sysname\> save

The current configuration will be written to the device. Are you sure? [Y/N:y]

Please input the file name(\*.cfg)[flash:/backup.cfg]

(To leave the existing filename unchanged, press the enter key):test.cfg

 Validating file. Please wait\...\...\...\...

 Configuration is saved to device successfully.

\# 将当前配置保存到存储介质的根目录，并将该文件设置为下次启动配置文件。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> save

The current configuration will be written to the device. Are you sure? [Y/N:y]

Please input the file name(\*.cfg)[flash:/startup.cfg]

(To leave the existing filename unchanged, press the enter key):

Validating file. Please wait\...

Saved the current configuration to mainboard device successfully.

Slot 1:

Save next configuration file successfully.

\# 将当前配置保存到存储介质的根目录，并将该文件设置为下次启动配置文件。（分布式设备－IRF模式）

\<Sysname\> save

The current configuration will be written to the device. Are you sure? [Y/N:y]

Please input the file name(\*.cfg)[flash:/startup.cfg]

(To leave the existing filename unchanged, press the enter key):

Validating file. Please wait\...

Saved the current configuration to mainboard device successfully.

Chassis 1 Slot 1:

Save next configuration file successfully.

\# 保存所有MDC内的配置，并将该文件设置为下次启动配置文件。（支持MDC的设备）

\<Sysname\> save mdc-all

Save current configuration in MDC Admin? [Y/N:y]

Please input the file name(\*.cfg)[flash:/1.cfg]

(To leave the existing filename unchanged, press the enter key):

flash:/1.cfg exists, overwrite? [Y/N:y]

Validating file. Please wait\...

Saved the current configuration to mainboard device successfully.

Chassis 1 Slot 1:

Save next configuration file successfully.

Save current configuration in MDC mdc1? [Y/N:y]

Please input the file name(\*.cfg)[flash:/mdc1.cfg]

(To leave the existing filename unchanged, press the enter key):

flash:/mdc1.cfg exists, overwrite? [Y/N:y]

Validating file. Please wait\...

Saved the current configuration to mainboard device successfully.

Chassis 1 Slot 1:

Save next configuration file successfully.

【相关命令】

·**display current-configuration**

·**display saved-configuration**

**配置文件管理 \-- 配置文件管理命令 \-- startup saved-configuration**

------------------------------------------------------------------------

**[startup** **saved-configuration**]命令用来配置下次启动配置文件（系统下次启动时使用的配置文件）。

**[undo** **startup saved-configuration**]命令用来设置设备以出厂配置启动。

【命令】

**[startup**[ **saved-configuration** *cfgfile* [ **backup** \| **main** ]]]

**[undo startup saved-configuration**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[cfgfile*]：配置文件的名称，该文件必须是存储介质根目录下、后缀为.cfg的文件。

**[backup**]：将配置文件设置为备用下次启动配置文件。

**[main**]：将配置文件设置为主用下次启动配置文件。

【使用指导】

主用主控板和备用主控板的下次启动配置文件必须是相同的文件，因此，使用本命令前，请确保指定的配置文件已经保存在主用主控板和备用主控板相同类型存储介质的根目录下，否则，操作失败。（分布式设备－独立运行模式）

所有成员设备的下次启动配置文件必须是相同的文件，因此，使用本命令前，请确保指定的配置文件已经保存在所有成员设备相同类型存储介质的根目录下，否则，操作失败。（集中式IRF设备）

所有成员设备上主控板的下次启动配置文件必须是相同的文件，因此，使用本命令前，请确保指定的配置文件已经保存在IRF中所有主控板相同类型存储介质的根目录下，否则，操作失败。（分布式设备－IRF模式）

使用该命令设置配置文件时：

·不指定**main**和**back**参数时，缺省使用**main**。

·主用下次启动配置文件和备用下次启动配置文件可以设置为同一文件，但为了更可靠，建议设置为不同的文件，或者将一份配置保存在两个不同名的文件中，一个设置为主用，一个设置为备用。

·在执行**undo** **startup saved-configuration**命令之后，系统会将主用/备用下次启动配置文件均设置为NULL，但不会删除该文件。

需要注意的是，执行**undo** **startup saved-configuration**命令并重启IRF或IRF中的成员设备时，会导致IRF分裂，请谨慎使用。（集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 配置下次启动配置文件。

\<Sysname\> startup saved-configuration testcfg.cfg

Please wait \....

\... Done!

【相关命令】

·**display startup**
