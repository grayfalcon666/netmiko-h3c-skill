
**EVB \-- EVB Probe命令 \-- display system internal evb global-info**

------------------------------------------------------------------------

**[display** **system** **internal** **evb** **global-info**]命令用来显示EVB子线程的信息。

【命令】

**[display** **system** **internal** **evb** **global-info**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**EVB \-- EVB Probe命令 \-- display system internal evb kernel**

------------------------------------------------------------------------

**[display** **system** **internal** **evb** **kernel**]命令用来显示EVB内核的数据信息。

【命令】

集中式设备：

**[display** **system** **internal** **evb** **kernel** **interface** ]**s-channel** *[channel-id[ \| interface-number]*:*channel-id*.*vsi-local-id* } [ **section** *section-number* ]

分布式设备－独立运行模式]/集中式IRF设备：

**[display** **system** **internal** **evb** **kernel** **slot** *slot-number* **interface** ]**s-channel** *[channel-id[ \| interface-number]*:*channel-id*.*vsi-local-id* } [ **section** *section-number* ]

分布式设备－]IRF模式：

**[display** **system** **internal** **evb** **kernel** **chassis** *chassis-number* **slot** *slot-number* **interface** ]**s-channel** *[channel-id[ \| interface-number]*:*channel-id*.*vsi-local-id* } [ **section** *section-number* ]

【视图】]

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[interface**]**s-channel** *channel-id[ \| interface-number]*:*channel-id*.*vsi-local-id* }：显示指定S通道接口或VSI接口上的信息。其中，*interface-number*为S通道所在端口的编号；*channel-id*为S通道的编号，取值范围为已创建S通道的编号；*vsi-local-id*为VSI本地编号，取值范围为已创建的VSI本地编号。

**[section** *section-number*]：显示VSI接口下指定段的过滤信息（每个段包含60条VSI过滤信息），*section-number*表示段的编号，取值范围为1～65535。如果未指定本参数，将只显示第一段的过滤信息。当VSI接口下的过滤信息较多时，可使用本参数进行分段显示，比如当*section-number*为1时显示第1～60条过滤信息，*section-number*为2时显示第61～120条过滤信息，......以此类推。

