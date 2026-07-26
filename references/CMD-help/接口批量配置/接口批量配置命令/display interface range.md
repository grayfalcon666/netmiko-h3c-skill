
**接口批量配置 \-- 接口批量配置命令 \-- display interface range**

------------------------------------------------------------------------

**[display interface range**]命令用来显示通过**interface range name**命令创建的批量接口的信息。

【命令】

**[display interface range ** **name** ]*name*

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name ***name*]：设备上已创建的批量接口的别名，为1～32个字符的字符串，区分大小写。不指定该参数时，显示当前设备中所有已创建的批量接口的信息。

【举例】

\# 显示当前设备中所有通过**interface range name**命令创建的批量接口的信息。

\<Sysname\> display interface range

Interface range name t2 gigabitethernet 1/0/1 gigabitethernet 1/0/2

Interface range name test gigabitethernet 1/0/11 gigabitethernet 1/0/12

以上显示信息表明：批量接口t2下绑定了接口GigabitEthernet1/0/1和GigabitEthernet1/0/2，批量接口test下绑定了接口GigabitEthernet1/0/11和GigabitEthernet1/0/12。

【相关命令】

·**interface range name**

**接口批量配置 \-- 接口批量配置命令 \-- interface range**

------------------------------------------------------------------------

**[interface range**]命令用来绑定一组接口，并进入接口批量配置视图。

【命令】

**[interface range*** interface-list*]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-list*]：接口列表，表示方式为*interface-list*＝ { *interface-type interface-number* [ **to** *interface-type interface-number*  }&\<1-5\>]。其中*interface-type interface-number*表示接口类型和接口编号。&\<1-5\>表示前面的参数最多可以输入5次。当使用**to**关键字指定接口范围时（形如*interface-type interface-number1* **to** *interface-type interface-number2*），则**to**关键字左边[的接口（起始接口）和]**to**关键字右边的接口（结束接口）必须位于同一接口卡或子卡上，并且起始接口编号中最后一维的值必须小于等于结束接口的编号中最后一维的值，其它维的值必须相等。

【使用指导】

当多个接口需要配置某功能（比如shutdown）时，需要逐个进入接口视图，在每个接口执行一遍命令，比较繁琐。**interface range**命令提供了一种批量配置方式。使用该命令可以将不同类型的接口进行绑定，并进入接口批量配置视图。

·在接口批量配置视图下，只能执行接口列表中第一个接口支持的命令，不能执行第一个接口不支持但其它成员接口支持的命令。（接口列表中的第一个接口指的是执行**interf[ace range]**命令时指定的第一个接口）。在接口批量配置视图下，输入问号并回车，将显示该视图下支持的所有命令。

·在接口批量配置视图下执行命令，会在绑定的所有接口下执行该命令：

¡当命令执行完成后，系统提示配置失败并保持在接口批量配置视图，如果配置失败的接口是接口列表的第一个接口，则表示列表中的所有接口都没有配置该命令；如果配置失败的接口是其它接口，则表示除了提示失败的接口外，其它接口都已经配置成功。

¡如果命令执行完成后，退回到系统视图，则表示这条命令在接口视图和系统视图下都支持，并且在列表中的某个接口上配置失败，在系统视图下配置成功，列表中位于这个接口后面的接口不再执行该命令。此时，可到列表中各接口的视图下使用**display this**命令验证配置效果，同时如果不需要在系统视图下配置该命令的话，请使用相应的**undo**命令取消该配置。

·在接口批量配置视图下，执行**display this**命令，将显示接口列表中第一个接口当前生效的配置。

需要注意的是：

[·无法通过**interface ***interface-type*[ { *interface-number* \| *interface-number.subnumber* }]]命令进入接口视图的接口（比如BRI1/1/1:1等），不能被设置为接口列表的第一个接口。

·聚合口加入[批量接口时，建议不要将该聚合口的成员接口也加入，否则在批量接口配置视图下执行某些配置命令时，可能会导致聚合分裂]。

·批量接口包含的接口数量没有上限，仅受系统资源限制。[接口数量较多时，在批量接口配置视图下执行命令等待的时间将较长。]

【举例】

\# 关闭接口GigabitEthernet1/0/1到GigabitEthernet1/0/24、VLAN接口2、Serial2/1/1到Serial2/1/7。

\<Sysname\> system-view

Sysname interface range gigabitethernet 1/0/1 to gigabitethernet 1/0/24 vlan-interafce 2 serial 2/1/1 to serial 2/1/7

Sysname-if-range shutdown

**接口批量配置 \-- 接口批量配置命令 \-- interface range name**

------------------------------------------------------------------------

**[interface range** **name** *name* **interface** *interface-list*]命令用来绑定一组接口，为这组接口指定一个别名，并使用该别名进入接口批量配置视图。

**[interface range name ***name*]（不带**interface**参数时）命令用来使用别名进入接口批量配置视图。

**[undo interface range name**]命令用来取消接口绑定，删除接口别名。

【命令】

**[interface range** **name** *name*  **interface***interface-list* ]

**[undo interface range name** *name*]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[name*]：批量接口的别名，为1～32个字符的字符串，区分大小写。

*[interface-list*]：接口列表，表示方式为*interface-list* = { *interface-type interface-number* [ **to** *interface-type interface-number*  }&\<1-5\>]。其中*interface-type interface-number*表示接口类型和接口编号。&\<1-5\>表示前面的参数最多可以输入5次。当使用**to**关键字指定接口范围时（形如*interface-type interface-number1* **to** *interface-type interface-number2*），则**to**关键字左边[的接口（起始接口）和]**to**关键字右边的接口（结束接口）必须位于同一接口卡或子卡上，并且起始接口编号中最后一维的值必须小于等于结束接口的编号中最后一维的值，其它维的值必须相等。

【使用指导】

当多个接口需要配置某功能（比如shutdown）时，需要逐个进入接口视图，在每个接口执行一遍命令，比较繁琐。**interface range name**命令提供了一种批量配置方式。使用该命令可以将不同类型的接口进行绑定，并进入接口批量配置视图。在接口批量配置视图下执行的配置命令，对绑定的所有成员接口生效。

**[interface range** **name**]和**interface range**命令都能提供接口[批量配置功能，它们的差别在于：]**interface range** **name**命令在绑定接口的时候可以定义一个别名，可以进行多次绑定，给不同的绑定定义不同的别名，以示区别，方便记忆。并且，后续可以使用别名直接进入接口批量配置视图，不再需要输出一长串的接口列表，配置起来更简便。用户可以使用**display [interface range]**命令来查看绑定了哪些接口。

·在接口批量配置视图下，只能执行接口列表中第一个接口支持的命令，不能执行第一个接口不支持但其它成员接口支持的命令。（接口列表中的第一个接口指的是执行**interf[ace range]**命令时指定的第一个接口）。在接口批量配置视图下，输入问号并回车，将显示该视图下支持的所有命令。

·在接口批量配置视图下执行命令，会在绑定的所有接口下执行该命令：

¡当命令执行完成后，系统提示配置失败并保持在接口批量配置视图，如果配置失败的接口是接口列表的第一个接口，则表示列表中的所有接口都没有配置该命令；如果配置失败的接口是其它接口，则表示除了提示失败的接口外，其它接口都已经配置成功。

¡如果命令执行完成后，退回到系统视图，则表示这条命令在接口视图和系统视图下都支持，并且在列表中的某个接口上配置失败，在系统视图下配置成功，列表中位于这个接口后面的接口不再执行该命令。此时，可到列表中各接口的视图下使用**display this**命令验证配置效果，同时如果不需要在系统视图下配置该命令的话，请使用相应的**undo**命令取消该配置。

·在接口批量配置视图下，执行**display this**命令，将显示接口列表中第一个接口当前生效的配置。

需要注意的是：

[·无法通过**interface ***interface-type*[ { *interface-number* \| *interface-number.subnumber* }]]命令进入接口视图的接口（比如BRI1/1/1:1等），不能被设置为接口列表的第一个接口。

·聚合口加入[批量接口时，建议不要将该聚合口的成员接口也加入，否则在批量接口配置视图下执行某些配置命令时，可能会导致聚合分裂]。

·批量接口包含的接口数量没有上限，仅受系统资源限制。[接口数量较多时，在批量接口配置视图下执行命令等待的时间将较长。]

·系统中支持的批量接口别名的个数没有上限，仅受系统资源限制。推荐用户配置1000个以下，配置数量过多，可能引起该特性执行效率降低。

【举例】

\# 将12个以太网接口GigabitEthernet1/0/1～GigabitEthernet1/0/12定义为myEthPort，并进入批量接口视图。

\<Sysname\> system-view

Sysname interface range name myEthPort interface gigabitethernet 1/0/1 to gigabitethernet 1/0/12

Sysname-if-range-myEthPort

\# 进入myEthPort别名对应的批量接口配置视图。

\<Sysname\> system-view

Sysname interface range name myEthPort

Sysname-if-range-myEthPort

【相关命令】

·**display interface range**

