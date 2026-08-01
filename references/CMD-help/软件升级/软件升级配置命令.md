<!-- CMD-INDEX
  boot-loader file                    | ]                | L21
  boot-loader blade file              | 用户视图             | L245
  boot-loader pex file                | 用户视图             | L409
  boot-loader update                  | 用户视图             | L609
  bootrom backup                      | 用户视图             | L759
  bootrom read                        | 用户视图             | L837
  bootrom restore                     | 用户视图             | L911
  bootrom update                      | 用户视图             | L983
  bootrom-update security-check enable | 系统视图             | L1061
  display boot-loader                 | 任意视图             | L1103
  display boot-loader blade           | 任意视图             | L1373
  display boot-loader pex             | 任意视图             | L1435
  firmware update                     | 用户视图             | L1485
  reset boot-loader blade             | 用户视图             | L1587
  reset boot-loader pex               | 用户视图             | L1633
  version auto-update enable          | 系统视图             | L1679
  version check ignore                | 系统视图             | L1727
-->

**软件升级 \-- 软件升级配置命令 \-- boot-loader file**

------------------------------------------------------------------------

**[boot-loader file**]命令用来指定设备下次启动时使用的软件包/IPE文件（以下简称下次启动软件包/IPE文件）。

【命令】

集中式设备：

**[boot-loader file boot ***boot-package ***system** *system-package* [ **feature** *feature-package*&\<1-30\>  { **backup** \| **main** }]]

**[boot-loader file*** ipe-filename *[{ **backup** \| **main** }]]

分布式设备－独立运行模式/集中式IRF设备：

**[boot-loader file boot ***boot-package ***system** *system-package* [ **feature** *feature-package*&\<1-30\>  ]]**[all**[ \| **slot** *slot-number* \**[cpu]** *cpu-number*  } { **backup** \| **main** }]

**[boot-loader file*** ipe-filename *]**[all**[ \| **slot** *slot-number* \**[cpu]** *cpu-number*  } { **backup** \| **main** }]

分布式设备－]IRF模式：

**[boot-loader file boot ***boot-package ***system** *system-package* [ **feature** *feature-package*&\<1-30\>  ]]**[all**[ \| **chassis** *chassis-number* **slot** *slot-number* \**[cpu]** *cpu-number*  } { **backup** \| **main** }]

**[boot-loader file*** ipe-filename*****]**[all**[ \| **chassis** *chassis-number* **slot** *slot-number* \**[cpu]** *cpu-number*  } { **backup** \| **main** }]

【视图】]

用户视图]

【缺省用户角色】]

network-admin

【参数】

**[boot ***boot-package*]：Boot包的名称，以.bin作为后缀名，从flash、cf、usb开始最多可输入63个字符，不区分大小写。

**[system** *system-package*]：System包的名称，以.bin作为后缀名，从flash、cf、usb开始最多可输入63个字符，不区分大小写。

**[feature** *feature-package*]：Feature包的名称，以.bin作为后缀名，从flash、cf、usb开始最多可输入63个字符，不区分大小写。*feature-package*&\<1-30\>表示前面的参数最多可以输入30次。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[ipe-filename*]：表示IPE（Image Package Envelope，复合软件包套件）文件的名称，以.ipe作为后缀名，从flash、cf、usb开始最多可输入63个字符，不区分大小写。

**[all**]：用来升级整个系统。当用户获取的IPE包中包含IRF系统升级需要的所有软件包时，使用这样的IPE包，并指定**all**参数，执行一次**boot-loader file**命令，就能指定系统中所有硬件下次启动时使用的软件包/IPE文件。

**[slot ***slot-number*]：表示待升级的主控板所在的槽位号。（分布式设备－独立运行模式）（不支持IRF3的设备）

**[slot ***slot-number*]：表示待升级的主控板所在的槽位号，或者待升级的本地有存储介质的PEX设备的虚拟槽位号。（分布式设备－独立运行模式）（支持IRF3的设备）

**[slot ***slot-number*]：表示待升级的成员设备的编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：表示待升级的成员设备的编号，或者待升级的本地有存储介质的PEX设备的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[cpu**] *cpu-number*：表示待升级的安全引擎的CPU编号。本参数专用于升级防火墙插卡上的安全引擎，其它单板以及防火墙插卡上其它CPU升级时，不需要指定该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/分布式设备－IRF模式）

**[chassis ***chassis-number ***slot ***slot-number*]：表示待升级的成员设备上的指定主控板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：表示待升级的成员设备上的指定主控板的槽位号，或者待升级的本地有存储介质的PEX设备的虚拟槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[backup**]：指定该软件包为备用启动软件包，并将该软件包的名称添加到备用启动软件包列表。备用启动软件包用于主用启动软件包不可用或异常情况时，引导设备启动。

**[main**]：指定该软件包为主用启动软件包，并将该软件包的名称添加到主用启动软件包列表。主用启动软件包用于引导设备启动。

【使用指导】

(1)集中式设备

请先查看软件包版本发布说明书，如果软件包需要License才能运行，且设备当前没有对应的有效的License时，需安装对应的License，再执行该命令。否则：

[·对于**boot-loader file boot ***boot-package ***system** *system-package* [ **feature** *feature-package*&\<1-30\>  { **backup** \| **main** }]]命令，只要指定某个的软件包当前没有有效的License，就会导致整条命令配置失败。

[·对于**boot-loader file*** ipe-filename *[{ **backup** \| **main** }]]命令，只有当前没有有效的License的软件包配置失败，其它软件包会配置成功。

当配置该命令时，命令中指定的软件包/IPE文件必须放在设备存储介质主分区的根目录下，文件名中必须包含存储介质的名称，形如flash:/xx.bin（flash:/xx.ipe）。

成功执行该命令后，系统会用命令中指定的软件包替换现有的软件包列表。如果命令行中没有指定Feature包，则更新后的软件包列表中不会有Feature包。

(2)分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式

·对于PEX设备，只有本地有存储介质的PEX设备才能使用该命令来配置下次启动软件包。对于本地无存储介质的PEX设备，则不能通过该命令来升级PEX设备，请使用**boot-loader pex file**命令。对于本地有存储介质的PEX设备，如果同时配置了**boot-loader file**和**boot-loader pex**命令，则PEX设备启动时优先使用下次启动软件包。在启动过程中，如果发现下次启动软件包和父设备的版本不兼容，再使用加载软件包。

·对于防火墙插卡上的安全引擎，如果同时配置了**boot-loader file**和**boot-loader blade**命令，则安全引擎启动时优先使用下次启动软件包。在启动过程中，如果发现下次启动软件包和主用主控板的版本不兼容，再使用加载软件包。（分布式设备－独立运行模式）

·请先查看软件包版本发布说明书，如果软件包需要License才能运行，且设备当前没有对应的有效的License时，需安装对应的License，再执行该命令。否则，当使用软件包配置该命令时，只要指定的某个软件包当前没有有效的License，则会导致整条命令配置失败；当使用IPE文件配置该命令时，只有当前没有有效的License的软件包配置失败，其它软件包会配置成功。

·当配置该命令时，命令中指定的软件包/IPE文件必须放在存储介质主分区的根目录下，文件名中必须包含存储介质的名称。

·系统会自动检查指定单板上对应路径下是否存在同名文件，如果不存在，则直接从指定路径拷贝一份并设置为下次启动软件包；如果存在，则提示用户是否从指定路径拷贝一份并设置为下次启动软件包。

·成功执行该命令后，系统会用命令中指定的软件包替换现有的软件包列表。如果命令行中没有指定Feature包，则更新后的软件包列表中不会有Feature包。

【举例】

\# 指定设备下次启动时所用的主用启动文件为flash:/all.ipe。（集中式设备）

\<Sysname\> boot-loader file flash:/all.ipe main

Verifying the IPE file and the images\...\...\...\...Done.

Images in IPE:

  boot.bin

  system.bin

This command will set the main startup software images. Continue? [Y/N:Y]

Add images to the device.

File flash:/boot.bin already exists on the device.

File flash:/system.bin already exists on the device.

Overwrite the existing files? [Y/N:Y]

Decompressing file boot.bin to flash:/boot.bin\...\...\...\...\...\...\...\...Done.

Decompressing file system.bin to flash:/system.bin\...\...\...\...\...\...\...\...\...\....Done.

The images that have passed all examinations will be used as the main startup software images at the next reboot on the device..

\# 指定设备下次启动时所用的主用启动文件为flash:/boot.bin和flash:/system.bin。（集中式设备）

\<Sysname\> boot-loader file boot flash:/boot.bin system flash:/system.bin main

This command will set the main startup software images. Continue? [Y/N:y]

The images that have passed all examinations will be used as the main startup

software images at the next reboot on the device.

\# 指定0号板下次启动时所用的主用启动文件为flash:/all.ipe。（分布式设备－独立运行模式）

\<Sysname\> boot-loader file flash:/all.ipe slot 0 main

Verifying the IPE file and the images\...\...\...\...Done.

Images in IPE:

  boot.bin

  system.bin

This command will set the main startup software images. Continue? [Y/N:Y]

Add images to target slot.

File flash:/boot.bin already exists on slot 0.

File flash:/system.bin already exists on slot 0.

Overwrite the existing files? [Y/N:Y]

Decompressing file boot.bin to flash:/boot.bin\...\...\...\...\...\...\...\...Done.

Decompressing file system.bin to flash:/system.bin\...\...\...\...\...\...\...\...\...\....Done.

The images that have passed all examinations will be used as the main startup software images at the next reboot on slot 0.

\# 指定成员设备1下次启动时所用的主用启动文件为flash:/all.ipe。（集中式IRF设备）

\<Sysname\> boot-loader file flash:/all.ipe slot 1 main

Verifying the IPE file and the images\...\...\...\...Done.

Images in IPE:

  boot.bin

  system.bin

This command will set the main startup software images. Continue? [Y/N:Y]

Add images to target slot.

File flash:/boot.bin already exists on slot 1.

File flash:/system.bin already exists on slot 1.

Overwrite the existing files? [Y/N:Y]

Decompressing file boot.bin to flash:/boot.bin\...\...\...\...\...\...\...\...Done.

Decompressing file system.bin to flash:/system.bin\...\...\...\...\...\...\...\...\...\....Done.

The images that have passed all examinations will be used as the main startup software images at the next reboot on slot 1.

\# 指定成员设备1的0号单板下次启动时所用的主用启动文件为flash:/all.ipe。（分布式设备－IRF模式）

\<Sysname\> boot-loader file flash:/all.ipe chassis 1 slot 0 main

Verifying the IPE file and the images\...\...\...\...Done.

Images in IPE:

  boot.bin

  system.bin

This command will set the main startup software images. Continue? [Y/N:Y]

Add images to target slot.

File flash:/boot.bin already exists on chassis 1 slot 0.

File flash:/system.bin already exists on chassis 1 slot 0.

Overwrite the existing files? [Y/N:Y]

Decompressing file boot.bin to flash:/boot.bin\...\...\...\...\...\...\...\...Done.

Decompressing file system.bin to flash:/system.bin\...\...\...\...\...\...\...\...\...\....Done.

The images that have passed all examinations will be used as the main startup software images at the next reboot on chassis 1 slot 0.

【相关命令】

·**boot-loader blade**** file**

·**boot-loader pex**** file**

·**display boot-loader**

**软件升级 \-- 软件升级配置命令 \-- boot-loader blade file**

------------------------------------------------------------------------

![说明](软件升级命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[boot-loader blade file**]命令用来配置安全引擎的加载软件包/IPE文件。

【命令】

分布式设备－独立运行模式/分布式设备－IRF模式：

**[boot-loader blade ***blade-model*** file boot ***boot-package ***system** *system-package* [ **feature** *feature-package*&\<1-30\> ]]

**[boot-loader blade ***blade-model*** file ipe ***ipe-filename*]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

**[blade ***blade-model*]：设备支持的安全引擎的型号，该参数必须完整输入，不区分大小写。可输入**boot-loader blade ？**，来获取该参数的取值。

**[boot ***boot-package*]：安全引擎加载的Boot包的名称，以.bin作为后缀名，从flash、cf、usb开始最多可输入63个字符，不区分大小写。

**[system** *system-package*]：安全引擎加载的System包的名称，以.bin作为后缀名，从flash、cf、usb开始最多可输入63个字符，不区分大小写。

**[feature** *feature-package*]：安全引擎加载的Feature包的名称，以.bin作为后缀名，从flash、cf、usb开始最多可输入63个字符，不区分大小写。{ *feature-package* }&\<1-30\>表示前面的参数最多可以输入30次。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ipe ***ipe-filename*]：表示加载的IPE（Image Package Envelope，复合软件包套件）文件名，以.ipe作为后缀名，从flash、cf、usb开始最多可输入63个字符，不区分大小写。

【使用指导】

请在设备启动完成、稳定运行后再配置该命令。如果配置该命令后，加入新的主控板，需要重新配置该命令，以免新加入的主控板上没有加载软件包，影响安全引擎启动。

配置该命令后，系统会将指定软件包备份到所有主控板。安全引擎只使用当前主用主控板上的软件包作为加载软件包。（分布式设备－独立运行模式）

成功执行该命令后，系统会用命令中指定的软件包替换命令行中指定型号的安全引擎现有的加载软件包列表。如果命令行中没有指定Feature包，则更新后的加载软件包列表中不会有Feature包。

当配置该命令时，命令中指定的软件包/IPE文件必须放在存储介质主分区的根目录下，文件名中必须包含存储介质的名称。

关于加载软件包的详细介绍以及下次启动软件包/IPE文件和加载软件包/IPE文件的关系，请参见"基础配置指导"中的"软件升级"。

【举例】

\# 指定型号为Blade-m9k的安全引擎向主控板加载时所用的加载文件为slot2.1#flash:/m9000_fw.ipe。（分布式设备---独立运行模式）

\<Sysname\> boot-loader blade Blade-m9k file ipe slot2.1#cfa0:/m9000_fw.ipe

Verifying the IPE file and the images\...\...\...\...\...\...\...\...\....Done.

File flash:/blade3fwm9k-cmw710-boot-a0002.bin already exists on slot 5.

File flash:/blade3fwm9k-cmw710-system-a0002.bin already exists on slot 5.

Overwrite the existing files? [Y/N:Y]

Decompressing file blade3fwm9k-cmw710-boot-a0002.bin to flash:/blade3fwm9k-cmw710-boot-a0002.bin\...\...\...\...\...\.....Done.

Decompressing file blade3fwm9k-cmw710-system-a0002.bin to flash:/blade3fwm9k-cmw710-system-a0002.bin\...\...\...\...\...\...\...\...\...\...Done.

File flash:/blade3fwm9k-cmw710-boot-a0002.bin already exists on slot 4.

File flash:/blade3fwm9k-cmw710-system-a0002.bin already exists on slot 4.

Overwrite the existing files? [Y/N:Y]

Copying file flash:/blade3fwm9k-cmw710-boot-a0002.bin to slot4#flash:/blade3fwm9k-cmw710-boot-a0002.bin\...\...\...\...\...\...\...\...\...\...\....Done.

Copying file flash:/blade3fwm9k-cmw710-system-a0002.bin to slot4#flash:/blade3fwm9k-cmw710-system-a0002.bin\...\...\...\...\...\...\...\...\...\.....Done.

\# 指定型号为Blade-m9k的安全引擎向主控板加载时所用的文件为slot2.1#flash:/blade3fwm9k-cmw710-boot-a0002.bin和slot2.1#flash:/blade3fwm9k-cmw710-system-a0002.bin。（分布式设备---独立运行模式）

\<Sysname\> boot-loader blade Blade-m9k file boot slot2.1#cfa0:/blade3fwm9k-cmw710-boot-a0002.bin system slot2.1#cfa0:/blade3fwm9k-cmw710-system-a0002.bin

File flash:/blade3fwm9k-cmw710-boot-a0002.bin already exists on slot 4.

File flash:/blade3fwm9k-cmw710-system-a0002.bin already exists on slot 4.

Overwrite the existing files? [Y/N:]

File flash:/blade3fwm9k-cmw710-boot-a0002.bin already exists on slot 5.

File flash:/blade3fwm9k-cmw710-system-a0002.bin already exists on slot 5.

Overwrite the existing files? [Y/N:]

\<maintest\>boot-loader blade Blade-m9k file boot slot2.1#cfa0:/blade3fwm9k-cmw710-boot-a0002.bin system slot2.1#cfa0:/blade3fwm9k-cmw710-system-a0002.bin

File flash:/blade3fwm9k-cmw710-boot-a0002.bin already exists on chassis 1 slot 4.

File flash:/blade3fwm9k-cmw710-system-a0002.bin already exists on chassis 1 slot 4.

Overwrite the existing files? [Y/N:Y]

Copying file cfa0:/blade3fwm9k-cmw710-boot-a0002.bin to slot4#flash:/blade3fwm9k-cmw710-boot-a0002.bin\...\...\...\...\...\...Done.

Copying file cfa0:/blade3fwm9k-cmw710-system-a0002.bin to slot4#flash:/blade3fwm9k-cmw710-system-a0002.bin\...\...\...\...\...\...\...\....Done.

File flash:/blade3fwm9k-cmw710-boot-a0002.bin already exists on slot 5.

File flash:/blade3fwm9k-cmw710-system-a0002.bin already exists on slot 5.

Overwrite the existing files? [Y/N:Y]

Copying file cfa0:/blade3fwm9k-cmw710-boot-a0002.bin to flash:/blade3fwm9k-cmw710-boot-a0002.bin\...\...\...\...\.....Done.

Copying file cfa0:/blade3fwm9k-cmw710-system-a0002.bin to flash:/blade3fwm9k-cmw710-system-a0002.bin\...\...\...\...\...\...\...\...\....Done.

\# 指定型号为Blade-m9k的安全引擎向主控板加载时所用的文件为flash:/m9000_fw.ipe。（分布式设备---IRF模式）

\<Sysname\> boot-loader blade Blade-m9k file ipe flash:/m9000_fw.ipe

Verifying the IPE file and the images\...\...\...\...\...\....Done.

File flash:/blade3fwm9k-cmw710-boot-a0002.bin already exists on chassis 1 slot 5.

File flash:/blade3fwm9k-cmw710-system-a0002.bin already exists on chassis 1 slot 5.

File flash:/blade3fwm9k-cmw710-devkit-a0002.bin already exists on chassis 1 slot 5.

Overwrite the existing files? [Y/N:N]

File flash:/blade3fwm9k-cmw710-boot-a0002.bin already exists on chassis 1 slot 4.

File flash:/blade3fwm9k-cmw710-system-a0002.bin already exists on chassis 1 slot 4.

File flash:/blade3fwm9k-cmw710-devkit-a0002.bin already exists on chassis 1 slot 4.

Overwrite the existing files? [Y/N:Y]

Copying file flash:/blade3fwm9k-cmw710-boot-a0002.bin to chassis1#slot4#flash:/blade3fwm9k-cmw710-boot-a0002.bin\...\...\...\...\...\...\...\...\....Done.

Copying file flash:/blade3fwm9k-cmw710-system-a0002.bin to chassis1#slot4#flash:/blade3fwm9k-cmw710-system-a0002.bin\...\...\...\...\...\.....Done.

Copying file flash:/blade3fwm9k-cmw710-devkit-a0002.bin to chassis1#slot4#flash:/blade3fwm9k-cmw710-devkit-a0002.bin\...\...\...\...\...\....Done.

\# 指定型号为Blade-m9k的安全引擎向主控板加载时所用的文件为flash:/ blade3fwm9k-cmw710-boot-a0002.bin和flash:/ blade3fwm9k-cmw710-system-a0002.bin。（分布式设备---IRF模式）

\<Sysname\> boot-loader blade Blade-m9k file boot flash:/blade3fwm9k-cmw710-boot-a0002.bin system flash:/blade3fwm9k-cmw710-system-a0002.bin

File flash:/blade3fwm9k-cmw710-boot-a0002.bin already exists on chassis 1 slot 4.

File flash:/blade3fwm9k-cmw710-system-a0002.bin already exists on chassis 1 slot 4.

Overwrite the existing files? [Y/N:Y]

Copying file flash:/blade3fwm9k-cmw710-boot-a0002.bin to chassis1#slot4#flash:/blade3fwm9k-cmw710-boot-a0002.bin\...\...\...\...\...\...\...\...Done.

Copying file flash:/blade3fwm9k-cmw710-system-a0002.bin to chassis1#slot4#flash:/blade3fwm9k-cmw710-system-a0002.bin\...\...\...\...\...\...\....Done.

【相关命令】

·**display boot-loader ****blade**

**软件升级 \-- 软件升级配置命令 \-- boot-loader pex file**

------------------------------------------------------------------------

![说明](软件升级命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[boot-loader pex file**]命令用来配置PEX设备的加载软件包/IPE文件。

【命令】

分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式：

**[boot-loader pex ***pex-model*** file boot ***boot-package ***system** *system-package* [ **feature** *feature-package*&\<1-30\> ]]

**[boot-loader pex ***pex-model*** file******ipe ***ipe-filename*]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

**[pex ***pex-model*]：设备支持的PEX设备的型号，该参数必须完整输入，不区分大小写。可输入**boot-loader pex ？**，回车，来获取该参数的取值。

**[boot ***boot-package*]：PEX设备将加载的Boot包的名称，以.bin作为后缀名，从flash、cf、usb开始最多可输入63个字符，不区分大小写。

**[system** *system-package*]：PEX设备将加载的System包的名称，以.bin作为后缀名，从flash、cf、usb开始最多可输入63个字符，不区分大小写。

**[feature** *feature-package*]：PEX设备将加载的feature包的名称，以.bin作为后缀名，从flash、cf、usb开始最多可输入63个字符，不区分大小写。*feature-package*&\<1-30\>表示前面的参数最多可以输入30次。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ipe ***ipe-filename*]：表示PEX设备将加载的IPE（Image Package Envelope，复合软件包套件）文件的名称，以.ipe作为后缀名，从flash、cf、usb开始最多可输入63个字符，不区分大小写。

【使用指导】

如果配置该命令后，加入新的主控板，需要重新配置该命令，以免主备倒换后，影响PEX设备启动。

配置该命令后，系统会将指定软件包备份到所有主控板。PEX设备只使用当前主用主控板上的软件包作为加载软件包。（分布式设备－独立运行模式）

成功执行该命令后，系统会用命令中指定的软件包替换命令行中指定型号的PEX设备现有的加载软件包列表。如果命令行中没有指定Feature包，则更新后的加载软件包列表中不会有Feature包。

关于该命令请注意，当配置该命令时，命令中指定的软件包（IPE文件）必须放在存储介质主分区的根目录下，文件名中必须包含存储介质的名称。

关于加载软件包的详细介绍以及下次启动软件包/IPE文件和加载软件包/IPE文件的关系，请参见"基础配置指导"中的"软件升级"。

【举例】

\# 将型号为PEX-S5120HI的PEX设备的加载软件包配置为flash:/all.ipe。（分布式设备---独立运行模式）

\<Sysname\> boot-loader pex PEX-S5120HI file ipe flash:/all.ipe

Verifying the IPE file and the images\...\...\...\...Done.

File flash:/rpu-s5120hi-boot.bin already exists on slot 0.

File flash:/rpu-s5120hi-system.bin already exists on slot 0.

Overwrite the existing files? [Y/N:Y]

Decompressing file rpu-s5120hi-boot.bin to flash:/rpu-s5120hi-boot.bin\...\...\...\...\...\...\...Done.

Decompressing file rpu-s5120hi-system.bin to flash:/rpu-s5120hi-system.bin\...\...\...\...\...\...\...\...\...\...\...\... Done.

File flash:/rpu-s5120hi-boot.bin already exists on slot 1.

File flash:/rpu-s5120hi-system.bin already exists on slot 1.

Overwrite the existing files? [Y/N:Y]

Copying file flash:/rpu-s5120hi-boot.bin to slot1#flash:/rpu-s5120hi-boot.bin\...\...\...\...\...\...\...\....Done.

Copying file flash:/rpu-s5120hi-system.bin to slot1#flash:/rpu-s5120hi-system.bin\...\...\...\...\...\...\...\...\...\...\...\...\...\.....Done.

\# 将型号为PEX-S5120HI的PEX设备的加载软件包配置为flash:/boot.bin和flash:/system.bin。（分布式设备---独立运行模式）

\<Sysname\> boot-loader pex PEX-S5120HI file boot flash:/boot.bin system flash:/system.bin

File flash:/boot.bin already exists on slot 1.

File flash:/system.bin already exists on slot 1.

Overwrite the existing files? [Y/N:y]

Copying file flash:/boot.bin to slot1#flash:/boot.bin\...\...\...\...\...\...\...\....Done.

Copying file flash:/system.bin to slot1#flash:/system.bin\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...Done.

\# 将型号为PEX-S5120HI的PEX设备的加载软件包配置为flash:/all.ipe。（集中式IRF设备）

\<Sysname\> boot-loader pex PEX-S5120HI file ipe flash:/all.ipe

Verifying the IPE file and the images\...\...\...\...Done.

File flash:/rpu-s5120hi-boot.bin already exists on slot 1.

File flash:/rpu-s5120hi-system.bin already exists on slot 1.

Overwrite the existing files? [Y/N:Y]

Decompressing file rpu-s5120hi-boot.bin to flash:/rpu-s5120hi-boot.bin\...\...\...\...\...\...\...Done.

Decompressing file rpu-s5120hi-system.bin to flash:/rpu-s5120hi-system.bin\...\...\...\...\...\...\...\...\...\...\...\...\...\..... Done.

File flash:/rpu-s5120hi-boot.bin already exists on slot 2.

File flash:/rpu-s5120hi-system.bin already exists on slot 2.

Overwrite the existing files? [Y/N:Y]

Copying file flash:/rpu-s5120hi-boot.bin to slot2#flash:/rpu-s5120hi-boot.bin\...\...\...\...\...\...\...\....Done.

Copying file flash:/rpu-s5120hi-system.bin to slot2#flash:/rpu-s5120hi-system.bin\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....Done.

\# 将型号为PEX-S5120HI的PEX设备的加载软件包配置为flash:/boot.bin和flash:/system.bin。（集中式IRF设备）

\<Sysname\> boot-loader pex PEX-S5120HI file boot flash:/boot.bin system flash:/system.bin

File flash:/boot.bin already exists on slot 2.

File flash:/system.bin already exists on slot 2.

Overwrite the existing files? [Y/N:Y]

Copying file flash:/boot.bin to slot2#flash:/boot.bin\...\...\...\...\...\...\...\....Done.

Copying file flash:/system.bin to slot2#flash:/system.bin\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....Done.

\# 将型号为PEX-S5120HI的PEX设备的加载软件包配置为flash:/all.ipe。（分布式设备---IRF模式）

\<Sysname\> boot-loader pex PEX-S5120HI file ipe flash:/all.ipe

Verifying the IPE file and the images\...\...\...\...Done.

File flash:/rpu-s5120hi-boot.bin already exists on chassis 1 slot 1.

File flash:/rpu-s5120hi-system.bin already exists on chassis 1 slot 1.

Overwrite the existing files? [Y/N:Y]

Decompressing file rpu-s5120hi-boot.bin to flash:/rpu-s5120hi-boot.bin\...\...\...\...\...\...\...Done.

Decompressing file rpu-s5120hi-system.bin to flash:/rpu-s5120hi-system.bin\...\...\...\...\...\...\...\...\...\...\...\...\...\..... Done.

File flash:/rpu-s5120hi-boot.bin already exists on chassis 1 slot 2.

File flash:/rpu-s5120hi-system.bin already exists on chassis 1 slot 2.

Overwrite the existing files? [Y/N:Y]

Copying file flash:/rpu-s5120hi-boot.bin to chassis1#slot2#flash:/rpu-s5120hi-boot.bin\...\...\...\...\...\...\...\....Done.

Copying file flash:/rpu-s5120hi-system.bin to chassis1#slot2#flash:/rpu-s5120hi-system.bin\...\...\...\...\...\...\...\...\...\...\...\...\...Done.

File flash:/rpu-s5120hi-boot.bin already exists on chassis 2 slot 2.

File flash:/rpu-s5120hi-system.bin already exists on chassis 2 slot 2.

Overwrite the existing files? [Y/N:Y]

Copying file flash:/rpu-s5120hi-boot.bin to chassis2#slot2#flash:/rpu-s5120hi-boot.bin\...\...\...\...\...\...\...\....Done.

Copying file flash:/rpu-s5120hi-system.bin to chassis2#slot2#flash:/rpu-s5120hi-system.bin\...\...\...\...\...\...\...\...\...\...\...\...Done.

\# 将型号为PEX-S5120HI的PEX设备的加载软件包配置为flash:/boot.bin和flash:/system.bin。（分布式设备---IRF模式）

\<Sysname\> boot-loader pex PEX-S5120HI file boot flash:/boot.bin system flash:/system.bin

File flash:/boot.bin already exists on chassis 1 slot 2.

File flash:/system.bin already exists on chassis 1 slot 2.

Overwrite the existing files? [Y/N:Y]

Copying file flash:/boot.bin to chassis1#slot2#flash:/boot.bin\...\...\...\...\...\...\...\....Done.

Copying file flash:/system.bin to chassis1#slot2#flash:/system.bin\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...Done.

File flash:/boot.bin already exists chassis 2 slot 2.

File flash:/system.bin already exists chassis 2 slot 2.

Overwrite the existing files? [Y/N:Y]

Copying file flash:/boot.bin to chassis2#slot2#flash:/boot.bin\...\...\...\...\...\...\...\....Done.

Copying file flash:/system.bin to chassis2#slot2#flash:/system.bin\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\....Done.

【相关命令】

·**boot-loader ****file**

·**display boot-loader**** pex**

**软件升级 \-- 软件升级配置命令 \-- boot-loader update**

------------------------------------------------------------------------

[**[![说明](软件升级命令.files/image001.png)]**]

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[boot-loader update**]命令用来将备用主控板的软件版本与主用主控板的当前软件版本进行同步。（分布式设备－独立运行模式）

**[boot-loader update**]命令用来将从设备的软件版本与主设备的当前软件版本进行同步。（集中式IRF设备）

**[boot-loader update**]命令用来将全局备用主控板的软件版本与全局主用主控板的当前软件版本进行同步。（分布式设备－IRF模式）

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[boot-loader update**[ { **all** \| **slot** *slot-number* }]]

分布式设备－IRF模式：

**[boot-loader update**[ { **all** \| **chassis** *chassis-number* **slot** *slot-number* }]]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

**[all**]：表示同步升级所有备用主控板。（分布式设备－独立运行模式）

**[all**]：表示同步升级所有备设备。（集中式IRF设备）

**[all**]：表示同步升级所有全局备用主控板。（分布式设备－IRF模式）

**[slot ***slot-number*]：表示待升级的备用主控板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：表示待升级的成员设备的编号。（集中式IRF设备）

**[chassis ***chassis-number ***slot ***slot-number*]：表示待升级的全局备用主控板所在位置。*chassis-number*表示设备的成员编号，*slot-number*表示全局备用主控板所在的槽位号。（分布式设备－IRF模式）

【使用指导】

本命令用于备用主控板和主用主控板软件版本不一致时，刷新备用主控板的软件版本，使其和主用主控板的软件版本相同。

(1)分布式设备－独立运行模式

请先查看软件包版本发布说明书，如果软件包需要License才能运行，且设备当前没有对应的有效的License时，需安装对应的License，再执行该命令。否则，会导致命令执行失败。

通过该命令指定备用主控板的下次启动软件包时，系统会进行如下处理：

·如果主用主控板当前是使用主用启动软件包列表启动的，则将其主用下次启动软件包列表中的软件包拷贝到备用主控板的对应目录下，并设置为备用主控板的主用下次启动软件包。如果这些软件包中有任一软件包不存在或者不可用，则命令执行失败。

·如果主用主控板当前是使用备用启动软件包列表启动的，则将其备用下次启动软件包列表中的软件包拷贝到备用主控板的对应目录下，并设置为备用主控板的主用下次启动软件包。如果这些软件包中有任一软件包不存在或者不可用，则命令执行失败。

如果主用主控板刚安装了补丁或者进行了ISSU升级，在执行**boot-loader update**命令前，请执行**install commit**命令刷新主用主控板的下次启动软件包列表。否则，可能导致备用主控板升级后与主用主控板的版本不一致。

(2)集中式IRF设备

请先查看软件包版本发布说明书，如果软件包需要License才能运行，且设备当前没有对应的有效的License时，需安装对应的License，再执行该命令。否则，会导致命令执行失败。

通过该命令指定从设备的下次启动软件包时，系统会进行如下处理：

·如果主设备当前是使用主用启动软件包列表启动的，则将其主用下次启动软件包列表中的软件包拷贝到从设备的对应目录下，并设置为从设备的主用下次启动软件包。如果这些软件包中有任一软件包不存在或者不可用，则命令执行失败。

·如果主设备当前是使用备用启动软件包列表启动的，则将其备用下次启动软件包列表中的软件包拷贝到从设备的对应目录下，并设置为从设备的主用下次启动软件包。如果这些软件包中有任一软件包不存在或者不可用，则命令执行失败。

如果主用主控板刚安装了补丁或者进行了ISSU升级，在执行**boot-loader update**命令前，请执行**install commit**命令刷新主用主控板的下次启动软件包列表。否则，可能导致备用主控板升级后与主用主控板的版本不一致。

(3)分布式设备－IRF模式

请先查看软件包版本发布说明书，如果软件包需要License才能运行，且设备当前没有对应的有效的License时，需安装对应的License，再执行该命令。否则，会导致命令执行失败。

通过该命令指定全局备用主控板的下次启动软件包时，系统会进行如下处理：

·如果全局主用主控板当前是使用主用启动软件包列表启动的，则将其主用下次启动软件包列表中的软件包拷贝到全局备用主控板的对应目录下，并设置为全局备用主控板的主用下次启动软件包。如果这些软件包中有任一软件包不存在或者不可用，则命令执行失败。

·如果全局主用主控板当前是使用备用启动软件包列表启动的，则将其备用下次启动软件包列表中的软件包拷贝到全局备用主控板的对应目录下，并设置为全局备用主控板的主用下次启动软件包。如果这些软件包中有任一软件包不存在或者不可用，则命令执行失败。

如果主用主控板刚安装了补丁或者进行了ISSU升级，在执行**boot-loader update**命令前，请执行**install commit**命令刷新主用主控板的下次启动软件包列表。否则，可能导致备用主控板升级后与主用主控板的版本不一致。

【举例】

\# 将1号槽位的备用主控板上的软件版本与主用主控板的软件版本同步。（分布式设备－独立运行模式）

\<Sysname\> boot-loader update slot 1

This command will update the specified standby MPU. Continue? [Y/N:y]

Updating. Please wait\...

Copying main startup software images to slot 1. Please wait\...

Done.

Setting copied images as main startup software images for slot 1\...

Done.

Successfully updated the startup software images of slot 1.

\# 将成员设备2上的软件版本与主设备的软件版本同步。（集中式IRF设备）

\<Sysname\> boot-loader update slot 2

This command will update the specified standby MPU. Continue? [Y/N:y]

Updating. Please wait\...

Copying main startup software images to slot 2. Please wait\...

Done.

Setting copied images as main startup software images for slot 2\...

Done.

Successfully updated the startup software images of slot 2.

\# 将成员设备1的1号单板上的软件版本与全局主用主控板同步。（分布式设备－IRF模式）

\<Sysname\> boot-loader update chassis 1 slot 1

This command will update the specified standby MPU. Continue? [Y/N:y]

Updating. Please wait\...

Copying main startup software images to chassis 1 slot 1. Please wait\...

Done.

Setting copied images as main startup software images for chassis 1 slot 1\...

Done.

Successfully updated the startup software images of chassis 1 slot 1.

【相关命令】

·**display boot-loader**

·**install commit**（基本配置命令参考/ISSU）

**软件升级 \-- 软件升级配置命令 \-- bootrom backup**

------------------------------------------------------------------------

![说明](软件升级命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[bootrom backup**]命令用来将Boot ROM程序从Boot ROM的Normal区备份到Backup区。

【命令】

集中式设备：

**[bootrom backup **\**[cpu***cpu-number *   **subslot** *subslot-number-list*  [ **all** \| **part** ]]]

分布式设备－独立运行模式/集中式IRF设备：

**[bootrom backup** **slot** *slot-number-list* [ **cpu** *cpu-number*   **subslot** *subslot-number-list*  [ **all** \| **part** ]]]

分布式设备－IRF模式：

**[bootrom backup** **chassis** *chassis-number* **slot** *slot-number-list* [ **cpu** *cpu-number*   **subslot** *subslot-number-list*  [ **all** \| **part** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

**[slot ***slot-number-list*]：槽位号列表，表示同时备份多个单板的Boot ROM程序。表示方式为*slot-number-list* *=* { *slot-number* [ **to** *slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要备份的单板所在的槽位号。&\<1-7\>表示前面的参数最多可以输入7次。（分布式设备－独立运行模式）

**[slot ***slot-number-list*]：成员编号列表，表示同时备份多个成员设备的Boot ROM程序。表示方式为*slot-number-list* *=* { *slot-number* [ **to** *slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要备份的设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number-list*]：成员编号/PEX虚拟槽位号列表，表示同时备份多个成员设备/PEX的Boot ROM程序。表示方式为*slot-number-list* *=* { *slot-number* [ **to** *slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要备份的设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number*]：表示需要备份Boot ROM程序的设备在IRF中的成员编号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number*]：表示需要备份Boot ROM程序的设备在IRF中的成员编号或者PEX对应的虚拟框号。（分布式设备－IRF模式）（支持IRF3的设备）

**[slot ***slot-number-list*]：槽位号列表，表示同时备份多个单板的Boot ROM程序。表示方式为*slot-number-list* *=* { *slot-number* [ **to** *slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要备份的单板所在的槽位号。&\<1-7\>表示前面的参数最多可以输入7次。（分布式设备－IRF模式）（不支持IRF3的设备）

**[slot ***slot-number-list*]：槽位号列表，表示同时备份多个单板/PEX的Boot ROM程序。表示方式为*slot-number-list* *=* { *slot-number* [ **to** *slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要备份的单板/PEX所在的槽位号。&\<1-7\>表示前面的参数最多可以输入7次。（分布式设备－IRF模式）（支持IRF3的设备）

**[subslot ***subslot-number-list*]：子槽位号列表，表示同时备份多个子卡的Boot ROM程序。表示方式为*subslot-number-list* *=* { *subslot-number* [ **to** *subslot-number*  }&\<1-7\>]。其中，*subslot-number*表示需要备份的子卡所在的子槽位号。&\<1-7\>表示前面的参数最多可以输入7次。不使用该参数时，表示备份的是单板的Boot ROM程序。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[all**]：操作Boot ROM程序的全部内容。不指定**all**和**part**参数时，默认使用**all**。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[part**]：只操作Boot ROM程序的扩展段（Boot ROM程序分为两部分：基本段和扩展段，基本段提供Boot ROM菜单的基本操作项，扩展段提供更多的Boot ROM菜单操作项）。不指定**all**和**part**参数时，默认使用**all**。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[cpu***cpu-number*]：备份指定CPU的Boot ROM程序。*cpu-number*表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

Boot ROM分为Normal区和Backup区。

·Normal区用于存放Boot ROM程序。设备启动时，会自动读取Normal区的Boot ROM程序。如果Normal区的Boot ROM程序不可用，再自动读取Backup区的Boot ROM程序。

·Backup区用于存放Boot ROM程序的副本。如果在设备运行过程中，Normal区的Boot ROM程序被损坏或者需要版本回退，可以使用**bootrom restore**命令将Boot ROM程序从Backup区恢复到Normal区。

【举例】

\# 将Boot ROM程序从Boot ROM的Normal区备份到Backup区。

\<Sysname\> bootrom backup all

Now backing up the Boot ROM, please wait\...

\...\...Done.

【相关命令】

·**bootrom restore**

**软件升级 \-- 软件升级配置命令 \-- bootrom read**

------------------------------------------------------------------------

![说明](软件升级命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[bootrom read**]命令用来将Boot ROM程序从Boot ROM的Normal区读取到Flash中。

【命令】

集中式设备：

**[bootrom read****\**[cpu***cpu-number *   **subslot** *subslot-number-list*  [ **all** \| **part** ]]]

分布式设备－独立运行模式/集中式IRF设备：

**[bootrom read******slot ***slot-number-list *\**[cpu***cpu-number *   **subslot** *subslot-number-list*  [ **all** \| **part** ]]]

分布式设备－IRF模式：

**[bootrom read** **chassis** *chassis-number* **slot** *slot-number-list* [ **cpu** *cpu-number*   **subslot** *subslot-number-list*  [ **all** \| **part** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

**[slot ***slot-number-list*]：槽位号列表，表示同时读取多个单板的Boot ROM程序。表示方式为*slot-number-list* *=* { *slot-number* [ **to** *slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要读取的单板所在的槽位号。&\<1-7\>表示前面的参数最多可以输入7次。（分布式设备－独立运行模式）

**[slot ***slot-number-list*]：成员编号列表，表示同时读取多个成员设备的Boot ROM程序。表示方式为*slot-number-list* *=* { *slot-number* [ **to** *slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要读取的设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number-list*]：成员编号/PEX虚拟槽位号列表，表示同时读取多个成员设备/PEX的Boot ROM程序。表示方式为*slot-number-list* *=* { *slot-number* [ **to** *slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要读取的设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number*]：表示需要读取Boot ROM程序的设备在IRF中的成员编号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number*]：表示需要读取Boot ROM程序的设备在IRF中的成员编号或者PEX对应的虚拟框号。（分布式设备－IRF模式）（支持IRF3的设备）

**[slot ***slot-number-list*]：槽位号列表，表示同时读取多个单板的Boot ROM程序。表示方式为*slot-number-list* *=* { *slot-number* [ **to** *slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要读取的单板所在的槽位号。&\<1-7\>表示前面的参数最多可以输入7次。（分布式设备－IRF模式）（不支持IRF3的设备）

**[slot ***slot-number-list*]：槽位号列表，表示同时读取多个单板/PEX的Boot ROM程序。表示方式为*slot-number-list* *=* { *slot-number* [ **to** *slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要备份的单板/PEX所在的槽位号。&\<1-7\>表示前面的参数最多可以输入7次。（分布式设备－IRF模式）（支持IRF3的设备）

**[subslot ***subslot-number-list*]：子槽位号列表，表示同时读取多个子卡的Boot ROM程序。表示方式为*subslot-number-list* *=* { *subslot-number* [ **to** *subslot-number*  }&\<1-7\>]。其中，*subslot-number*表示需要读取的子卡所在的子槽位号。&\<1-7\>表示前面的参数最多可以输入7次。不使用该参数时，表示读取的是单板的Boot ROM程序。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[all**]：操作Boot ROM程序的全部内容。不指定**all**和**part**参数时，默认使用**all**。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[part**]：只操作Boot ROM程序的扩展段。不指定**all**和**part**参数时，默认使用**all**。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[cpu***cpu-number*]：读取指定CPU的Boot ROM程序。*cpu-number*表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

成功执行**bootrom read**命令后，系统会自动生成basicbtm.bin和extendbtm.bin文件并保存到Flash中。其中，basicbtm.bin存储了Boot ROM程序的基本段，extendbtm.bin存储了Boot ROM程序的扩展段。如果在设备运行过程中，Normal区的Boot ROM程序被损坏或者需要版本回退，可以使用**bootrom update**命令重新加载之前生成的basicbtm.bin和extendbtm.bin。

【举例】

\# 读取Boot ROM程序。

\<Sysname\> bootrom read all

  Now reading the Boot ROM, please wait\...

\...\...\...Done.

【相关命令】

·**bootrom ****update**

**软件升级 \-- 软件升级配置命令 \-- bootrom restore**

------------------------------------------------------------------------

![说明](软件升级命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[bootrom restore**]命令用来将Boot ROM程序从Boot ROM的Backup区恢复到Normal区。。

【命令】

集中式设备：

**[bootrom** **restore** [ **cpu** *cpu-number*   **subslot** *subslot-number-list*  [ **all** \| **part** ]]]

分布式设备－独立运行模式/集中式IRF设备：

**[bootrom** **restore** **slot** *slot-number-list* [ **cpu** *cpu-number*   **subslot** *subslot-number-list*  [ **all** \| **part** ]]]

分布式设备－IRF模式：

**[bootrom restore** **chassis** *chassis-number* **slot** *slot-number-list* [ **cpu** *cpu-number*   **subslot** *subslot-number-list*  [ **all** \| **part** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

**[slot ***slot-number-list*]：槽位号列表，表示同时恢复多个单板的Boot ROM程序。表示方式为*slot-number-list* *=* { *slot-number* [ **to** *slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要恢复的单板所在的槽位号。&\<1-7\>表示前面的参数最多可以输入7次。（分布式设备－独立运行模式）

**[slot ***slot-number-list*]：成员编号列表，表示同时恢复多个成员设备的Boot ROM程序。表示方式为*slot-number-list* *=* { *slot-number* [ **to** *slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要恢复的设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number-list*]：成员编号/PEX虚拟槽位号列表，表示同时恢复多个成员设备/PEX的Boot ROM程序。表示方式为*slot-number-list* *=* { *slot-number* [ **to** *slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要恢复的设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number*]：表示需要恢复Boot ROM程序的设备在IRF中的成员编号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number*]：表示需要恢复Boot ROM程序的设备在IRF中的成员编号或者PEX对应的虚拟框号。（分布式设备－IRF模式）（支持IRF3的设备）

**[slot ***slot-number-list*]：槽位号列表，表示同时恢复多个单板的Boot ROM程序。表示方式为*slot-number-list* *=* { *slot-number* [ **to** *slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要恢复的单板所在的槽位号。&\<1-7\>表示前面的参数最多可以输入7次。（分布式设备－IRF模式）（不支持IRF3的设备）

**[slot ***slot-number-list*]：槽位号列表，表示同时恢复多个单板/PEX的Boot ROM程序。表示方式为*slot-number-list* *=* { *slot-number* [ **to** *slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要恢复的单板/PEX所在的槽位号。&\<1-7\>表示前面的参数最多可以输入7次。（分布式设备－IRF模式）（支持IRF3的设备）

**[subslot ***subslot-number-list*]：子槽位号列表，表示同时恢复多个子卡的Boot ROM程序。表示方式为*subslot-number-list* *=* { *subslot-number* [ **to** *subslot-number*  }&\<1-7\>]。其中，*subslot-number*表示需要恢复的子卡所在的子槽位号。&\<1-7\>表示前面的参数最多可以输入7次。不使用该参数时，表示不恢复子卡。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[all**]：操作Boot ROM程序的全部内容。不指定**all**和**part**参数时，默认使用**all**。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[part**]：只操作Boot ROM程序的扩展段。不指定**all**和**part**参数时，默认使用**all**。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[cpu***cpu-number*]：恢复指定CPU的Boot ROM程序。*cpu-number*表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 恢复Boot ROM程序。

\<Sysname\> bootrom restore all

  This command will restore the Boot ROM file, Continue? [Y/N:y]

  Now restoring the Boot ROM, please wait\...

\...\...Done.

【相关命令】

·**bootrom backup**

**软件升级 \-- 软件升级配置命令 \-- bootrom update**

------------------------------------------------------------------------

**[bootrom update**]命令用来加载Boot ROM程序。

【命令】

集中式设备：

**[bootrom update** **file** *file-url* [ **cpu** *cpu-number*   **subslot** *subslot-number-list*  [ **all** \| **part** ]]]

分布式设备－独立运行模式/集中式IRF设备：

**[bootrom update** **file** *file-url* **slot** *slot-number-list* [ **cpu** *cpu-number*   **subslot** *subslot-number-list*  [ **all** \| **part** ]]]

分布式设备－IRF模式：

**[bootrom update** **file** *file-url* **chassis** *chassis-number* **slot** *slot-number-list* [ **cpu** *cpu-number*   **subslot** *subslot-number-list*  [ **all** \| **part** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

**[file** *file-url*]：Flash中包含Boot ROM程序的文件，*file-url*表示用于Boot ROM程序升级的文件的名称，为1～63个字符的字符串。

**[slot ***slot-number-list*]：槽位号列表，表示同时升级多个单板的Boot ROM程序。表示方式为*slot-number-list* *=* { *slot-number* [ **to** *slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要升级的单板所在的槽位号。&\<1-7\>表示前面的参数最多可以输入7次。（分布式设备－独立运行模式）

**[slot ***slot-number-list*]：成员编号列表，表示同时升级多个成员设备的Boot ROM程序。表示方式为*slot-number-list* *=* { *slot-number* [ **to** *slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要升级的设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number-list*]：成员编号/PEX虚拟槽位号列表，表示同时升级多个成员设备/PEX的Boot ROM程序。表示方式为*slot-number-list* *=* { *slot-number* [ **to** *slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要升级的设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number*]：表示需要升级Boot ROM程序的设备在IRF中的成员编号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number*]：表示需要升级Boot ROM程序的设备在IRF中的成员编号或者PEX对应的虚拟框号。（分布式设备－IRF模式）（支持IRF3的设备）

**[slot ***slot-number-list*]：槽位号列表，表示同时升级多个单板的Boot ROM程序。表示方式为*slot-number-list* *=* { *slot-number* [ **to** *slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要升级的单板所在的槽位号。&\<1-7\>表示前面的参数最多可以输入7次。（分布式设备－IRF模式）（不支持IRF3的设备）

**[slot ***slot-number-list*]：槽位号列表，表示同时升级多个单板/PEX的Boot ROM程序。表示方式为*slot-number-list* *=* { *slot-number* [ **to** *slot-number*  }&\<1-7\>]。其中，*slot-number*表示需要升级的单板/PEX所在的槽位号。&\<1-7\>表示前面的参数最多可以输入7次。（分布式设备－IRF模式）（支持IRF3的设备）

**[subslot ***subslot-number-list*]：子槽位号列表，表示同时升级多个子卡的Boot ROM程序。表示方式为*subslot-number-list* *=* { *subslot-number* [ **to** *subslot-number*  }&\<1-7\>]。其中，*subslot-number*表示需要升级的子卡所在的子槽位号。&\<1-7\>表示前面的参数最多可以输入7次。不使用该参数时，表示不升级子卡。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[all**]：操作Boot ROM程序的全部内容。不指定**all**和**part**参数时，默认使用**all**。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[part**]：只操作Boot ROM程序的扩展段。不指定**all**和**part**参数时，默认使用**all**。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[cpu***cpu-number*]：更新指定CPU的Boot ROM程序。*cpu-number*表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

Boot ROM程序通过Boot包（\*.bin）发布，产品会将需要升级的单板的Boot ROM程序集成到Boot包中。此时，可是使用**bootrom update**命令，将升级文件指定为Boot包，系统会根据单板的型号自动将相应的Boot ROM程序加载到Boot ROM中；也可以在升级Boot包的同时完成Boot ROM程序的加载。

执行该命令后，设备会将Flash中的Boot ROM程序加载到Boot ROM的Normal区。设备启动时，会直接使用Normal区的Boot ROM程序。因此，如果Flash空间不足，Boot ROM程序加载完成之后，Boot ROM文件可以删除。

加载后，要使新的Boot ROM程序生效，需要重启设备。

【举例】

\# 使用a.bin文件升级设备的Boot ROM程序。

\<Sysname\> bootrom update file a.bin

   This command will update the Boot ROM file on the specified board(s), Continue? [Y/N:y]

   Now updating the Boot ROM, please wait\...

\...\...\...\....Done.

【相关命令】

·**boot-loader file**

**软件升级 \-- 软件升级配置命令 \-- bootrom-update security-check enable**

------------------------------------------------------------------------

![说明](软件升级命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[bootrom-update security-check enable**]命令用来开启Boot ROM程序合法性检查功能。

**[undo bootrom-update security-check enable**]命令用来关闭Boot ROM程序合法性检查功能。

【命令】

**[bootrom-update security-check enable**]

**[undo bootrom-update security-check enable**]

【缺省情况】

Boot ROM程序合法性检查功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

【使用指导】

如果使能了该功能，则在升级Boot ROM程序时，设备会先检查Boot ROM文件的合法性：包括Boot ROM文件是否有效以及是否和硬件匹配等。检查通过后，才会升级。

【举例】

\# 启动Boot ROM升级时的合法性检查功能。

\<Sysname\> system-view

Sysname bootrom-update security-check enable

**软件升级 \-- 软件升级配置命令 \-- display boot-loader**

------------------------------------------------------------------------

**[display boot-loader**]命令用来显示本次启动和下次启动所采用的启动软件包的名称。

【命令】

集中式设备：

**[display boot-loader**]

分布式设备－独立运行模式/集中式IRF设备：

**[display boot-loader ** **slot** *slot-number* ]**cpu** *cpu-number*

分布式设备－IRF模式：

**[display boot-loader ** **chassis** *chassis-number*  **slot** *slot-number* **cpu** *cpu-number*  ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

【参数】

**[slot ***slot-number*]：表示主控板所在的槽位号。不指定该参数时，表示设备上的所有主控板。（分布式设备－独立运行模式）

**[slot ***slot-number*]：表示成员设备的编号。不指定该参数时，表示IRF中的所有成员设备。（集中式IRF设备）

**[chassis ***chassis-number ***slot ***slot-number*]：表示指定成员设备上的指定主控板。**chassis ***chassis-number*表示设备在IRF中的成员编号，**slot ***slot-number*表示主控板所在的槽位号。不指定该参数时，表示IRF中的所有主控板。（分布式设备－IRF模式）

**[cpu**] *cpu-number*：表示安全引擎的CPU编号。本参数专用于显示安全引擎本次启动和下次启动所采用的启动软件包的名称。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/分布式设备－IRF模式）

【使用指导】

使用该命令可显示父设备、PEX设备和安全引擎本次启动和下次启动所采用的启动软件包的名称。

·对于本地有存储介质的PEX设备，会显示本次启动和下次启动所采用的启动软件包的名称。

·对于本地无存储介质的PEX设备，只显示本次启动软件包的名称。

·对于安全引擎，会显示本次启动和下次启动所采用的启动软件包的名称。

【举例】

\# 显示本次启动和下次启动所采用的启动软件包的名称（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（集中式设备）

\<Sysname\> display boot-loader

Software images on the device:

Current software images:

  flash:/simware-cmw710-boot-a1701.bin

  flash:/simware-cmw710-system-a1701.bin

Main startup software images:

  flash:/simware-cmw710-boot-a1701.bin

  flash:/simware-cmw710-system-a1701.bin

  flash:/simware-cmw710-ssh-a1701.bin

Backup startup software images:

  flash:/simware-cmw710-boot-a1701.bin

  flash:/simware-cmw710-system-a1701.bin

\# 显示本次启动和下次启动所采用的启动软件包的名称（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display boot-loader

Software images on slot 0:

Current software images:

  flash:/simware-cmw710-boot-a1701.bin

  flash:/simware-cmw710-system-a1701.bin

Main startup software images:

  flash:/simware-cmw710-boot-a1701.bin

  flash:/simware-cmw710-system-a1701.bin

  flash:/simware-cmw710-ssh-a1701.bin

Backup startup software images:

  flash:/simware-cmw710-boot-a1701.bin

  flash:/simware-cmw710-system-a1701.bin

\# 显示本次启动和下次启动所采用的启动软件包的名称（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（分布式设备－IRF模式）

\<Sysname\> display boot-loader

Software images on chassis 0 slot 1:

Current software images:

  flash:/simware-cmw710-boot-a1701.bin

  flash:/simware-cmw710-system-a1701.bin

Main startup software images:

  flash:/simware-cmw710-boot-a1701.bin

  flash:/simware-cmw710-system-a1701.bin

  flash:/simware-cmw710-ssh-a1701.bin

Backup startup software images:

  flash:/simware-cmw710-boot-a1701.bin

  flash:/simware-cmw710-system-a1701.bin

\# 显示本次启动和下次启动所采用的启动软件包的名称（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（支持IRF3的设备）（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display boot-loader

Software images on slot 1:

Current software images:

  flash:/s5820v2_5830v2-cmw710-boot-d2402.bin

  flash:/s5820v2_5830v2-cmw710-systemt-d2402.bin

Main startup software images:

  flash:/s5820v2_5830v2-cmw710-boot-d2402.bin

  flash:/s5820v2_5830v2-cmw710-systemt-d2402.bin

Backup startup software images:

  flash:/s5820v2_5830v2-cmw710-boot-d2402.bin

  flash:/s5820v2_5830v2-cmw710-systemt-d2402.bin

Software images on slot 101:

Current software images:

  flash:/rpu-s5800-boot-d2402.bin

  flash:/rpu-s5800-boot-systemt-d2402.bin

Main startup software images:

  flash:/rpu-s5800-boot-boot-d2402.bin

  flash:/rpu-s5800-boot-systemt-d2402.bin

Backup startup software images:

  flash:/rpu-s5800-boot-boot-d2402.bin

  flash:/rpu-s5800-boot-systemt-d2402.bin

Software images on slot 105:

Current software images:

  flash:/rpu-s5120hi-boot.bin

  flash:/rpu-s5120hi-system.bin

\# 显示本次启动和下次启动所采用的启动软件包的名称（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（支持IRF3的设备）（分布式设备－IRF模式）

\<Sysname\> display boot-loader

Software images on chassis 0 slot 1:

Current software images:

  flash:/s10500-cmw710-boot-a0046.bin

  flash:/s10500-cmw710-system-a0046.bin

Main startup software images:

  flash:/s10500-cmw710-boot-a0046.bin

  flash:/s10500-cmw710-system-a0046.bin

Backup startup software images:

  flash:/s10500-cmw710-boot-a0046.bin

  flash:/s10500-cmw710-system-a0046.bin

Software images on chassis 5 slot 1:

Current software images:

  flash:/rpu-s5800-boot-d2402.bin

  flash:/rpu-s5800-systemt-d2402.bin

Main startup software images:

  flash:/rpu-s5800-boot-d2402.bin

  flash:/rpu-s5800-systemt-d2402.bin

Backup startup software images:

  flash:/rpu-s5800-boot-d2402.bin

  flash:/rpu-s5800-systemt-d2402.bin

Software images on chassis 5 slot 10:

Current software images:

  flash:/rpu-s5120hi-boot.bin

  flash:/rpu-s5120hi-systemt.bin

表1-1 display boot-loader命令显示信息描述表

字段

描述

Software images on the device

启动软件包的相关信息（集中式设备）

Software images on slot *n*

位于槽位*n*上的某主控板的启动软件包的相关信息（分布式设备－独立运行模式）

成员编号为*n*的某成员设备的启动软件包的相关信息（集中式IRF设备）

Software images on chassis *m* slot *n*

某主控板的启动软件包的相关信息，该主控板位于成员设备*m*的*n*号槽位上（分布式设备－IRF模式）

Current software images

最近一次启动使用的启动软件包列表

Main startup software images

主用下次启动软件包列表

Backup startup software images

备用下次启动软件包列表

【相关命令】

·**boot-loader file**

**软件升级 \-- 软件升级配置命令 \-- display boot-loader blade**

------------------------------------------------------------------------

![说明](软件升级命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display** **boot-loader blade**]命令用来显示安全引擎的加载软件包列表。

【命令】

分布式设备－独立运行模式/分布式设备－IRF模式：

**[display boot-loader blade ** *blade-model* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

【参数】

*[blade-model*]：设备支持的安全引擎的型号，该参数必须完整输入，不区分大小写。可输入**boot-loader blade ？**，来获取该参数的取值。不指定该参数时，表示设备支持的所有型号的安全引擎。

【使用指导】

加载软件包列表中记录了加载软件包存储的位置、安全引擎的型号、加载启动软件包的名称。当安全引擎需要使用加载软件包启动时，就会根据该列表去当前主用主控板加载这些软件包。

【举例】

\# 查看所有安全引擎在所有主控板上的加载软件包列表。

\<Sysname\> display boot-loader blade Blade-m9k

Startup software image files for BLADEs to load from the parent device:

Blade model: Blade-m9k

  flash:/blade3fwm9k-cmw710-boot-a0002.bin

  flash:/blade3fwm9k-cmw710-system-a0002.bin

表1-2 display boot-loader blade命令显示信息描述表

字段

描述

Startup software image files for BLADEs to load from the parent device

安全引擎的加载软件包列表

Blade model

安全引擎的型号

**软件升级 \-- 软件升级配置命令 \-- display boot-loader pex**

------------------------------------------------------------------------

**[display** **boot-loader pex**]命令用来显示PEX设备的加载软件包列表。

【命令】

分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式：

**[display boot-loader pex** [ *pex-model* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

【参数】

*[pex-model*]：设备支持的PEX设备的型号，该参数必须完整输入，不区分大小写。可输入**boot-loader pex ？**，回车，来获取该参数的取值。不指定该参数时，表示所有型号的PEX设备。

【使用指导】

加载软件包列表中记录了加载软件包存储的位置、PEX设备的型号、加载启动软件包的名称。当PEX设备需要使用加载软件包启动时，就会根据该列表去当前主用主控板加载这些软件包。

【举例】

\# 查看所有PEX设备在所有主控板上的加载软件包列表。

\<Sysname\> display boot-loader pex

Startup software image files for PEXs to load from the parent device:

PEX model: PEX-S5120HI

  flash:/rpu-s5120hi-boot.bin

  flash:/rpu-s5120hi-system.bin

PEX model: PEX-S5820

  flash:/boot.bin

  flash:/system.bin

**软件升级 \-- 软件升级配置命令 \-- firmware update**

------------------------------------------------------------------------

![说明](软件升级命令.files/image001.png)

本命令的支持情况与设备型号有关，请以设备的实际情况为准。

**[firmware update**]命令用来升级CPLD、FPGA等固件。

【命令】

集中式设备：

**[firmware update** [ **subslot** *subslot-number*  { **cpld** *cpld-number* \| **cpu** *cpu-number* \| **fpga** *fpga-number* \| **module** *module-number* } **file** *filename*]]

分布式设备－独立运行模式/集中式IRF设备：

**[firmware update slot** *slot-number* [ **subslot** *subslot-number*  { **cpld** *cpld-number* \| **cpu** *cpu-number* \| **fpga** *fpga-number* \| **module** *module-number* } **file** *filename*]]

分布式设备－IRF模式：

**[firmware update chassis ***chass-number* **slot** *slot-number* [ **subslot** *subslot-number*  { **cpld** *cpld-number* \| **cpu** *cpu-number* \| **fpga** *fpga-number* \| **module** *module-number* } **file** *filename*]]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

**[chassis ***chass-number* **slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chass-number* **slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[slot** *slot-number*]：表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[subslot** *subslot-number*]：子卡所在的子槽位号。不指定该参数时，表示单板上的所有子卡。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[cpld** *cpld-number*]：表示需要升级CPLD（Complex Programmable Logical Device 复杂可编程逻辑器件），*cpld-number*表示固件的编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[fpga** *fpga-number*]：表示需要升级FPGA（Field Programmable Gate Array 现场可编程门阵列），*fpga-number*表示固件的编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[cpu** *cpu-number*]：表示需要升级CPU，*cpu-number*表示CPU的编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[module** *module-number*]：表示需要升级指定模块（如3G Modem模块等），*module-number*表示模块的编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[file** *filename*]：升级文件的名称。不同固件升级文件的后缀可能不同，文件名从flash、cf、usb开始最多可输入63个字符，不区分大小写。

【使用指导】

固件升级后需要对其所在的板卡进行下电后重新上电才能生效，对板卡下电的方式有：切断外部电源、插拔板卡、使用**power-supply off**和**power-supply** **on**命令等方式，请根据板卡的实际支持情况，选择下电方式。

【举例】

\# 升级1号CPLD。（集中式设备）

\<Sysname\> firmware update cpld 1 file package.bin

Updating firmware for CPLD on the specified card or subcard. Continue?Y/N:y

Updating the firmware...

Please power cycle the card or subcard to activate the firmware.

\# 升级位于1号槽位的1号CPLD。（分布式设备－独立运行模式）

\<Sysname\> firmware update slot 1 cpld 1 file package.bin

Updating firmware for CPLD on the specified card or subcard. Continue?Y/N:y

Updating the firmware...

Please power cycle the card or subcard to activate the firmware.

\# 升级位于成员设备1上的1号CPLD。（集中式IRF设备）

\<Sysname\> firmware update slot 1 cpld 1 file package.bin

Updating firmware for CPLD on the specified card or subcard. Continue?Y/N:y

Updating the firmware...

Please power cycle the card or subcard to activate the firmware.

\# 升级位于成员设备1上1号槽位的1号CPLD。（分布式设备－IRF模式）

\<Sysname\> firmware update chassis 1 slot 1 cpld 1 file package.bin

Updating firmware for CPLD on the specified card or subcard. Continue?Y/N:y

Updating the firmware...

Please power cycle the card or subcard to activate the firmware.

**软件升级 \-- 软件升级配置命令 \-- reset boot-loader blade**

------------------------------------------------------------------------

![说明](软件升级命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[reset boot-loader blade**]命令用来清除安全引擎的加载软件包配置。

【命令】

分布式设备－独立运行模式/分布式设备－IRF模式：

**[reset boot-loader blade ***blade-model*]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

*[blade-model*]：设备支持的安全引擎的型号，该参数必须完整输入，不区分大小写。可输入**reset boot-loader blade ？**，来获取该参数的取值。

【使用指导】

请在设备启动完成、稳定运行后再配置该命令。

执行该命令后，设备会清空对应的加载软件包列表，不会将加载软件包从设备上删除。

【举例】

\# 清除指定型号为Blade-m9k的安全引擎的加载软件包配置。

\<Sysname\> reset boot-loader blade Blade-m9k

【相关命令】

·**boot-loader blade file**

·**display boot-loader blade**

**软件升级 \-- 软件升级配置命令 \-- reset boot-loader pex**

------------------------------------------------------------------------

![说明](软件升级命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[reset boot-loader pex**]命令用来清除PEX设备的加载软件包配置。

【命令】

分布式设备－独立运行模式/分布式设备－IRF模式：

**[reset boot-loader pex** *pex-model*]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

*[pex-model*]：设备支持的PEX设备的型号，该参数必须完整输入，不区分大小写。可输入**boot-loader pex ？**，回车，来获取该参数的取值。

【使用指导】

请在设备启动完成、稳定运行后再配置该命令。

执行该命令后，设备会清空对应的加载软件包列表，不会将加载软件包从设备上删除。

【举例】

\# 清除指定型号为PEX-S5820V2的PEX的加载软件包配置。

\<Sysname\> reset boot-loader pex PEX-S5820V2

【相关命令】

·**boot-loader pex file**

·**display boot-loader pex**

**软件升级 \-- 软件升级配置命令 \-- version auto-update enable**

------------------------------------------------------------------------

![说明](软件升级命令.files/image002.png)

该命令只在分布式设备－独立运行模式下支持。

****

**[version auto-update enable**]命令用来使能备用主控板自动加载主用主控板当前启动软件包的功能。

**[undo version auto-update enable**]命令用来[取消备用主控板自动加载主用主控板启动软件的功能。]

【命令】

**[version auto-update enable**]

**[undo version auto-update enable**]

【缺省情况】

当启动过程中，当备用主控板发现自己版本和主用主控板版本不一致时，会自动加载主用主控板的当前启动软件包。

【视图】

系统视图

【缺省用户角色】

network-admin

【使用指导】

配置**undo version check ignore**和**version auto-update enable**命令后，在设备启动过程中，当[备用主控板发现自己当前启动软件包版本和主用主控板的当前启动软件包版本不一致时，会自动拷贝主用主控板的当前启动软件包列表中的所有软件包，设置为自己的主用下次启动软件包，并自动重启。这样，能够使得备用主控板启动后，和主用主控板启动软件包的版本一致。]

【举例】

\# 使能备用主控板自动加载主用主控板当前启动软件包的功能。

\<Sysname\> system-view

Sysname version auto-update enable

【相关命令】

·**version check ignore**

**软件升级 \-- 软件升级配置命令 \-- version check ignore**

------------------------------------------------------------------------

![说明](软件升级命令.files/image002.png)

该命令只在分布式设备－独立运行模式下支持。

****

**[version check ignore**]命令用来忽略对备用主控板进行启动软件包版本一致性检查，即不检查备用主控板的版本是否与主用主控板的启动软件包版本一致。

**[undo version check ignore**]命令用来使能对备用主控板进行启动软件包版本一致性检查。

需要注意的是，系统运行时，如果备用主控板的启动软件包版本和主用主控板的启动软件包版本不一致，可能会造成系统故障。

【命令】

**[version check ignore**]

**[undo version check ignore**]

【缺省情况】

备用主控板启动软件包版本一致性检查功能处于使能状态。

【视图】

系统视图

【缺省用户角色】

network-admin

【使用指导】

·如果[忽略对备用主控板进行启动软件包版本一致性检查，当备用主控板和主用主控板启动软件包版本不一致时，备用主控板仍然使用不一致的版本启动，可能会造成设备功能问题。]

·如果[使能对备用主控板进行启动软件包版本一致性检查，当备用主控板和主用主控板启动软件包版本不一致时，备用主控板会停留在启动阶段，不能正常启动。]

建议用户不要忽略启动软件包版本一致性检查。

【举例】

\# 使能对备用主控板进行版本一致性检查。

\<Sysname\> system-view

Sysname undo version check ignore

【相关命令】

·**version auto-update enable**
