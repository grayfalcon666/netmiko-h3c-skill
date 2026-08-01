<!-- CMD-INDEX
  display system internal kernel memory dump | Probe视图          | L9
  display system internal kernel memory pool |                  | L57
  follow                              | Probe视图          | L129
  memory boundary-check enable        |                  | L189
  memory boundary-check scan          | Probe视图          | L255
-->

**诊断 \-- 诊断Probe命令 \-- display system internal kernel memory dump**

------------------------------------------------------------------------

**[display system internal kernel memory dump**]命令用来查看指定内核内存地址的内容。

【命令】

集中式设备：

**[display system internal kernel memory dump address** *address-hex* **length** *memory-length*]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal kernel memory dump address** *address-hex* **length** *memory-length* [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display system internal kernel memory dump address** *address-hex* **length** *memory-length* [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[address ***address-hex*]：表示内存起始地址。

**[length** *memory-length*]：表示要查看的内存大小，取值范围为1～1024，单位为字节。

**[slot** *slot-number*]：表示单板所在的槽位号，不指定表示主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示设备在IRF中的成员编号，不指定表示主设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号，不指定表示主设备。（集中式IRF设备）（支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号，不指定表示全局主用主控板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定表示全局主用主控板。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**诊断 \-- 诊断Probe命令 \-- display system internal kernel memory pool**

------------------------------------------------------------------------

**[display system internal kernel memory pool**]命令用来显示内核态正在使用的内存池的统计信息。

【命令】

集中式设备：

**[display system internal kernel memory pool ** **name** *name-string* ]

**[display system internal kernel memory pool tag** [ *tag-value* ]]

**[display system internal kernel memory pool name** *name-string* **tag** *tag-value*]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal kernel memory pool ** **name** *name-string* ]  **slot** *slot-number* [**cpu** *cpu-number*  ]

**[display system internal kernel memory pool tag** [ *tag-value*   **slot** *slot-number* [**cpu** *cpu-number*  ]]]

**[display system internal kernel memory pool name** *name-string* **tag** *tag-value* [ **slot** *slot-number* [**cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display system internal kernel memory pool** [ **name** name-string   **chassis** *chassis-number* **slot** *slot-number* [**cpu** *cpu-number*  ]]]

**[display system internal kernel memory pool tag ** *tag-value* ]  **chassis** *chassis-num*ber **slot** *slot-number* [**cpu** *cpu-number*  ]

**[display system internal kernel memory pool name** *name-string* **tag** *tag-value* [ **chassis** *chassis-number* **slot** *slot-number* [**cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[name** *name-string*]：表示内存池的名字。

**[tag** *tag-value*]：指定内存池使用者的标识。

**[slot** *slot-number*]：表示单板所在的槽位号，不指定表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示设备在IRF中的成员编号，不指定表示主设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号，不指定表示主设备。（集中式IRF设备）（支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号，不指定表示全局主用主控板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定表示全局主用主控板。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

不指定**name**和**tag**参数时，显示系统内存池使用情况的概要信息。

仅指定**name** *name-string*时，显示指定内存池使用情况的概要信息；

仅指定**tag**时，显示所有内存池使用情况的概要信息，以tag为关键字进行显示；

仅指定**tag ***tag-value*时，显示指定tag使用的内存池概要信息；

指定**name** *name-string* **tag** *tag-value*时，显示指定tag和内存池中内存对象的使用信息。

**诊断 \-- 诊断Probe命令 \-- follow**

------------------------------------------------------------------------

**[follow**]命令用来通过跟踪栈信息来调试指定的进程或者线程。

【命令】

集中式设备：

**[follow**[ { **job** *job-id* \| **process** *pid* } [ **thread** *thread-id* ]  **delay** *seconds*   **iteration** *count* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[follow**[ { **job** *job-id* \| **process** *pid* } [ **thread** *thread-id* ]  **delay** *seconds*   **iteration** *count*   **slot** *slot-number* [**cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[follow**[ { **job** *job-id* \| **process** *pid* } [ **thread** *thread-id* ]  **delay** *seconds*   **iteration** *count*   **chassis** *chassis-number* **slot** *slot-number* [**cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[job*** job-id*]：任务ID，用于唯一标识一个进程，该ID不会随着进程的重启而改变，取值范围为1～2147483647。

**[process** *pid*]：进程ID，该ID可能会随着进程的重启而改变，取值范围为1～2147483647。

**[thread ***thread-id*]：线程ID，用于指定进程内某一指定线程，取值范围为1～2147483647。

**[delay** *seconds*]：指定每次跟踪操作的间隔时间，取值范围为0～255秒，缺省为5秒。

**[iteration** *count*]：指定跟踪调试的次数的次数，取值范围为1～255次，缺省为5次。

**[slot** *slot-number*]：表示单板所在的槽位号，不指定表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示设备在IRF中的成员编号，不指定表示主设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号，不指定表示主设备。（集中式IRF设备）（支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号，不指定表示全局主用主控板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定表示全局主用主控板。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

对于用户态进程，**follow**命令会分别显示当前进程的内核态堆栈和用户态堆栈信息，并以user stack/kernel stack提示符加以区分；对于内核态进程，则只显示内核态堆栈信息。

不指定thread参数时，默认显示指定进程内所有线程。

**诊断 \-- 诊断Probe命令 \-- memory boundary-check enable**

------------------------------------------------------------------------

**[memory boundary-check enable**]命令用来开启内存越界检查功能。

**[undo memory boundary-check enable**]命令用来恢复缺省情况。

【命令】

集中式设备：

**[memory boundary-check******enable job ***job-id*]

**[undo memory boundary-check enable job ***job-id*]

分布式设备－独立运行模式/集中式IRF设备：

**[memory boundary-check enable job ***job-id* [ **slot** *slot-number* [**cpu** *cpu-number*  ]]]

**[undo memory boundary-check** **enable** **job** *job-id* [ **slot** *slot-number* [**cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[memory boundary-check** **enable job** *job-id* [ **chassis** *chassis-number* **slot** *slot-number* [**cpu** *cpu-number*  ]]]

**[undo memory boundary-check** **enable job** *job-id* [ **chassis** *chassis-number* **slot** *slot-number* [**cpu** *cpu-number*  ]]]

【缺省情况】

内存越界检查功能处于关闭状态。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[job ***job-id*]：任务ID，用于唯一标识一个进程，该ID不会随着进程的重启而改变，取值范围为1～2147483647。

**[slot** *slot-number*]：表示单板所在的槽位号，不指定表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示设备在IRF中的成员编号，不指定表示主设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号，不指定表示主设备。（集中式IRF设备）（支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号，不指定表示全局主用主控板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定表示全局主用主控板。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

开启指定进程的内存越界检查功能后，该进程每次释放内存前都会进行内存越界检查，以便确保申请和释放操作的正确性。如果发生内存越界，将内存越界信息记录到内存文件中（所有进程的越界信息都会记录到一个文件中）。

【相关命令】

·**memory boundary-check scan**

**诊断 \-- 诊断Probe命令 \-- memory boundary-check scan**

------------------------------------------------------------------------

**[memory boundary-check scan**]命令用来触发一次内存越界检查，并显示检查的结果。若有内存被写越界，则打印出该出错处地址往前偏移16字节，一共128字节的内存内容。

【命令】

集中式设备：

**[memory boundary-check scan job ***job-id*]

分布式设备－独立运行模式/集中式IRF设备：

**[memory boundary-check scan** **job** *job-id* [ **slot** *slot-number* [**cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[memory boundary-check scan** **job** *job-id* [ **chassis** *chassis-number* **slot** *slot-number* [**cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[job ***job-id*]：任务ID，用于唯一标识一个进程，该ID不会随着进程的重启而改变，取值范围为1～2147483647。

**[slot** *slot-number*]：表示单板所在的槽位号，不指定表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示设备在IRF中的成员编号，不指定表示主设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号，不指定表示主设备。（集中式IRF设备）（支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号，不指定表示全局主用主控板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定表示全局主用主控板。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

使用前必须使能内存越界检测功能，否则使用该命令检查，无效果。

执行该命令后，系统会从出错处地址往前偏移16字节，一共显示128字节的内存内容；当系统中存在多处内存越界时，只记录并显示地址最小的一条检查结果。

【相关命令】

·**memory boundary-check enable**
