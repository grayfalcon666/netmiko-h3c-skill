
**License管理 \-- License管理Probe命令 \-- display system internal license buffer-data**

------------------------------------------------------------------------

**[display system internal license buffer-data**]命令用来显示内存中缓存的License数据。

【命令】

集中式设备：

**[display system internal license **]**buffer-data**

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal license **]**buffer-data** **slot** *slot-number*

分布式设备－IRF模式：

**[display system internal license **]**buffer-data** **chassis** *chassis-number* **slot** *slot-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot*** slot-number*]：显示指定单板的内存缓存的License数据。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的内存缓存的License数据。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis** *[chassis-number* **slot** *slot-number*]]：显示指定单板的内存缓存的License数据[。]*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**License管理 \-- License管理Probe命令 \-- display system internal license feature-set**

------------------------------------------------------------------------

**[display system internal license feature-set**]命令用来显示设备支持的特性集的相关信息。

【命令】

集中式设备：

**[display system internal license feature-set**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal license feature-set slot** *slot-number*]

分布式设备－IRF模式：

**[display system internal license feature-set chassis ***chassis-number* **slot** *slot-number*]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[feature-set**]：显示设备中的特性集相关信息。

**[slot*** slot-number*]：显示指定单板的设备中的特性集相关信息。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的设备中的特性集相关信息。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis** *[chassis-number* **slot** *slot-number*]]：显示指定单板的特性集相关信息[。]*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**License管理 \-- License管理Probe命令 \-- display system internal license fifo**

------------------------------------------------------------------------

**[display system internal license fifo**]命令用来显示License使用的FIFO管道信息。

【命令】

集中式设备：

**[display system internal license fifo **]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal license fifo slot*** slot-number*]

分布式设备－IRF模式：

**[display system internal license fifo chassis** *chassis-number* **slot** *slot-number*]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot*** slot-number*]：显示指定单板的FIFO管道信息。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的FIFO管道信息。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis** *[chassis-number* **slot** *slot-number*]]：显示指定单板的FIFO管道信息[。]*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**License管理 \-- License管理Probe命令 \-- display system internal license lipc**

------------------------------------------------------------------------

**[display system internal license lipc**]命令用来显示License LIPC通道信息。License LIPC用于特性模块和License模块的内部通信。

【命令】

集中式设备：

**[display system internal license lipc**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal license lipc** **slot** *slot-number*]

分布式设备－IRF模式：

**[display system internal license lipc chassis** *chassis-number* **slot** *slot-number* ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot*** slot-number*]：显示指定单板的License LIPC通道信息。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的License LIPC通道信息。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis** *[chassis-number* **slot** *slot-number*]]：显示指定单板的License LIPC通道信息[。]*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**License管理 \-- License管理Probe命令 \-- display system internal license lipc hash**

------------------------------------------------------------------------

**[display system internal license lipc hash**]命令用来显示hash链表中存储的License LIPC通道信息。

【命令】

集中式设备：

**[display system internal license lipc hash**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal license lipc hash slot ***slot-number*]

分布式设备－IRF模式：

**[display system internal license lipc hash chassis** *chassis-number* **slot** *slot-number*]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot*** slot-number*]：显示指定单板的hash链表中存储的LIPC信息。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的hash链表中存储的LIPC信息。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis** *[chassis-number* **slot** *slot-number*]]：显示指定单板的hash链表中存储的LIPC信息[。]*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**License管理 \-- License管理Probe命令 \-- display system internal license lmi-paa**

------------------------------------------------------------------------

**[display system internal license lmi-paa**]命令用来显示LMI（License Manage Item，License管理项）信息和PAA（Product Ability Aggregate，产品能力集）信息。

【命令】

集中式设备：

**[display system internal license lmi-paa**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal license lmi-paa** **slot** *slot-number*]

分布式设备－IRF模式：

**[display system internal license lmi-paa** **chassis** *chassis-number* **slot** *slot-number* ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot*** slot-number*]：显示指定单板的LMI信息和PAA能力信息。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的LMI信息和PAA能力信息。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的LMI信息和PAA能力信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**License管理 \-- License管理Probe命令 \-- license check-timer**

------------------------------------------------------------------------

**[license check-timer**]命令用来修改License的每天检查定时器的值。

【命令】

集中式设备：

**[license check-timer*** interval-value*]

分布式设备－独立运行模式/集中式IRF设备：

**[license check-timer*** interval-value* **slot** *slot-number*]

分布式设备－IRF模式：

**[license check-timer ***interval-value ***chassis** *chassis-number* **slot** *slot-number*]

【缺省情况】

License的每天检查定时器的值为864000秒（24小时）。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval-value*]：指定检查定时器的周期，单位为秒，范围为10～864000。时间过短可能造成系统繁忙，建议60秒以上。

**[slot*** slot-number*]：表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot*** slot-number*]：表示设备在IRF中的成员编号。（集中式IRF设备）

**[chassis** *[chassis-number* **slot** *slot-number*]]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

【使用指导】

License的有效期以天为单位，设备以每天检查定时器时长为周期，检查License是否过期，如果已经过期，则标识为过期；如果没有过期，则将有效期减一。

本命令不会保存到配置文件，设备重启后会恢复到缺省情况。

本命令仅用于内部测试使用，用户不要使用此命令修改时间，否则会导致License快速过期。

**License管理 \-- License管理Probe命令 \-- license file-timer**

------------------------------------------------------------------------

**[license file-timer**]命令用来修改License文件检查定时器的周期。

【命令】

集中式设备：

**[license file-timer*** interval-value*]

分布式设备－独立运行模式/集中式IRF设备：

**[license file-timer*** interval-value* **slot** *slot-number*]

分布式设备－IRF模式：

**[license file-timer*** interval-value ***chassis** *chassis-number* **slot** *slot-number*]

【缺省情况】

License文件检查定时器的周期为1800秒（30分钟）。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval-value*]：指定文件丢失检查定时器的周期，单位为秒，范围为10～864000。时间过短可能造成系统繁忙，建议60秒以上。

**[slot*** slot-number*]：修改指定单板上的文件丢失的检查周期。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot*** slot-number*]：修改指定设备上的文件丢失检查定定时器时间周期。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis** *[chassis-number* **slot** *slot-number*]]：修改指定设备指定单板的文件丢失检查定时器周期[。]*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

【使用指导】

设备启动后，会自动启动License进程，并检查License文件是否存在。如果License文件不存在，则启动License文件检查定时器，周期性检测License文件是否恢复。License文件文件恢复，License文件检查定时器会自动删除。

本命令不会保存到配置文件，设备重启后会恢复到缺省情况。
