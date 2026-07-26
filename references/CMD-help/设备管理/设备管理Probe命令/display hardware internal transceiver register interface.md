
**设备管理 \-- 设备管理Probe命令 \-- display hardware internal transceiver register interface**

------------------------------------------------------------------------

![说明](设备管理Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[d**]**isplay hardware internal transceiver register interface**命令用来显示可插拔光模块上指定寄存器区域的内容，用十六进制数表示。

【命令】

**[d**]**isplay hardware internal transceiver register interface ***interface-type interface-number*** device ***device-index*** address ***start-address*** length ***region-length*

【视图】

Probe视图

【缺省用户角色】

network-admin

【参数】

**[interface**] *interface-type interface-number*：显示接口上插入的可插拔光模块上的寄存器信息。*interface-type interface-number*表示接口类型和接口编号。

**[device** device-index]：表示指定接口上光模块内部寄存器的索引号，用十六进制数表示，取值范围为0～FF。

**[address **]*start-address*：起始地址，即需要显示的寄存器区域的起始点的偏移地址。用十六进制数表示，取值范围为0～FFFF。

**[length **]*region-length*：寄存器区域的长度，即需要显示的寄存器区域的字节数。用十进制数表示，取值范围为1～256。

**设备管理 \-- 设备管理Probe命令 \-- display system internal dbm**

------------------------------------------------------------------------

**[display system internal dbm**]命令用来显示数据库信息。

【命令】

集中式设备：

**[display system internal dbm**]**[all**[ \| **name** *dbname* ]\**[key** *keyname*  }]

分布式设备－独立运行模式/集中式]IRF设备[:]

**[display system internal dbm**]**[all**[\|] **name** *dbname* \**[key** *keyname*  } **slot** *slot-number* }

分布]式设备－IRF模式：

**[display system internal dbm**  **all** [\|] **name** *dbname* [ **key** *keyname*  } **chassis** *chassis-number* **slot** *slot-number* }

【视图】]

Probe]视图

【缺省用户角色】]

network-admin

mdc-admin

【参数】

**[all**]：表示所有数据库。

**[name**] *dbname*：指定数据库名。

**[key**] *keyname*：指定key的名称，在数据库中以key名称标识一项数据。

**[slot**] *slot-number*：表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**] *slot-number*：表示设备在IRF中的成员编号。（集中式IRF设备）

**[chassis**] *chassis-number* **slot** *slot-number*：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**设备管理 \-- 设备管理Probe命令 \-- display transceiver information interface**

------------------------------------------------------------------------

**[display transceiver information interface**]命令用来显示光模块的详细信息。

【命令】

**[display transceiver information interface** [ *interface-type interface-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type interface-number*]：显示接口上插入的可插拔光模块的详细信息。*interface-type interface-number*表示接口类型和接口编号，如果不指定该参数，表示所有接口。

