
**信息中心 \-- 信息中心Probe命令 \-- display system internal customlog host**

------------------------------------------------------------------------

![说明](信息中心Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display system internal customlog host**]命令用来显示指定日志主机当前运行状态下的内核数据信息。

【命令】

集中式设备：

**[display system internal customlog host ***index*****[{ **cmccPortA** \| **cmccPortF** \| **cmccPortW \|  cmccSessionA** \| **cmccSessionW** \| **portA** \| **portW** \| **sessionA** \| **sessionW** \| **sessionbasedA \| sessionbasedW** \| **userbasedA** \| **userbasedF** \| **userbasedW** }]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal customlog host ***index*****[{ **cmccPortA** \| **cmccPortF** \| **cmccPortW \|  cmccSessionA** \| **cmccSessionW** \| **portA** \| **portW** \| **sessionA** \| **sessionW** \| **sessionbasedA \| sessionbasedW** \| **userbasedA** \| **userbasedF** \| **userbasedW** } [ **slot** *slot-number* [ **cpu** *cpu-number* ] ]]]

分布式设备－IRF模式：

**[display system internal customlog host ***index*****[{ **cmccPortA** \| **cmccPortF** \| **cmccPortW \|  cmccSessionA** \| **cmccSessionW** \| **portA** \| **portW** \| **sessionA** \| **sessionW** \| **sessionbasedA \| sessionbasedW** \| **userbasedA** \| **userbasedF** \| **userbasedW** } [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ] ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[index*]：表示指定日志主机的索引号。*index*取值范围为0～3。

**[cmccPortA**]**：**指定中国移动公司的端口创建日志类型，并显示日志对应的内核数据信息。

**[cmccPortF**]**：**指定中国移动公司的端口资源不足日志类型，并显示日志对应的内核数据信息。

**[cmccPortW**]**：**指定中国移动公司的端口删除日志类型，并显示日志对应的内核数据信息。

**[cmccSessionA**]**：**指定中国移动公司的session创建日志类型，并显示日志对应的内核数据信息。

**[cmccSessionW**]**：**指定中国移动公司的session删除日志类型，并显示日志对应的内核数据信息。

**[portA**]**：**指定中国联通公司的端口创建日志类型，并显示日志对应的内核数据信息。

**[portW**]**：**指定中国联通公司的端口删除日志类型，并显示日志对应的内核数据信息。

**[sessionA**]**：**指定中国联通公司的session创建日志类型，并显示日志对应的内核数据信息。

**[sessionW**]**：**指定中国联通公司的session删除日志类型，并显示日志对应的内核数据信息。

**[sessionbasedA**]**：**指定中国电信公司的session创建日志类型，并显示日志对应的内核数据信息。

**[sessionbasedW **]**：**指定中国电信公司的session删除日志类型，并显示日志对应的内核数据信息。

**[userbasedA**]**：**指定中国电信公司的端口创建日志，并显示日志对应的内核数据信息。

**[userbasedF**]**：**指定中国电信公司的端口资源不足日志类型，并显示日志对应的内核数据信息。

**[userbasedW**]**：**指定中国电信公司的端口删除日志，并显示日志对应的内核数据信息。

**[slot** *slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在槽位号。如未指定该参数，则显示当前日志主机主控板运行状态下的内核数据信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的内核数据信息，*slot-number*表示设备在IRF中的成员编号。如未指定该参数，则显示当前日志主机主控板运行状态下的内核数据信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上的内核数据信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如未指定该参数，则显示当前日志主机主控板运行状态下的内核数据信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备和单板上的内核数据信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如未指定该参数，则显示当前日志主机全局主用主控板运行状态下的内核数据信息。[（分布式设备－]IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的内核数据信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号[，]*slot-number*表示单板或PEX所[在的槽位号。如未指定该参数，则显示当前日志主机全局主用主控板运行状态下的内核数据信息。（分布式设备－]IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：指定需要显示信息的成员设备所在[的]CPU。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]

**信息中心 \-- 信息中心Probe命令 \-- display system internal customlog mbuf dump**

------------------------------------------------------------------------

![说明](信息中心Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display system internal customlog mbuf dump**]命令用来显示指定个数的CUSTOMLOG报文的详细信息。

【命令】

集中式设备

**[display system internal customlog mbuf dump count ***number*]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal customlog mbuf dump count ***number* [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display system internal customlog mbuf dump count ***number* [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：指定需要显示的日志个数。*number*取值范围为1～100。

**[slot** *slot-number*]：显示指定单板上CUSTOMLOG报文的详细信息，*slot-number*表示单板所在槽位号。如未指定该参数，则显示当前日志主机主控板上日志报文的详细信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上CUSTOMLOG报文的详细信息，*slot-number*表示设备在IRF中的成员编号。如未指定该参数，则显示当前日志主机主控板上日志报文的详细信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上CUSTOMLOG报文的详细信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如未指定该参数，则显示当前日志主机主控板上日志报文的详细信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备和单板的CUSTOMLOG报文的详细信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如未指定该参数，则显示当前日志主机主控板上日志报文的详细信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的CUSTOMLOG报文的详细信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如未指定该参数，则显示当前日志主机主控板上日志报文的详细信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：指定需要显示信息的成员设备所在的CPU。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**信息中心 \-- 信息中心Probe命令 \-- display system internal customlog mbuf usage**

------------------------------------------------------------------------

![说明](信息中心Probe命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display system internal customlog mbuf usage**]命令用来显示指定日志主机上每个CPU内MBUF池的使用情况信息。

【命令】

集中式设备

**[display system internal customlog mbuf usage ***index*****[{ **cmccPortA** \| **cmccPortF** \| **cmccPortW** \| **cmccSessionA** \| **cmccSessionW** \| **portA** \| **portW** \| **sessionA** \| **sessionW** \| **sessionbasedA \| sessionbasedW** \| **userbasedA** \| **userbasedF** \| **userbasedW** }]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal customlog mbuf usage ***index*****[{ **cmccPortA** \| **cmccPortF** \| **cmccPortW** \| **cmccSessionA** \| **cmccSessionW** \| **portA** \| **portW** \| **sessionA** \| **sessionW** \| **sessionbasedA \| sessionbasedW** \| **userbasedA** \| **userbasedF** \| **userbasedW** } [ **slot** *slot-number* [ **cpu** *cpu-number* ] ]]]

分布式设备－IRF模式：

**[display system internal customlog mbuf usage ***index*****[{ **cmccPortA** \| **cmccPortF** \| **cmccPortW** \| **cmccSessionA \| cmccSessionW** \| **portA** \| **portW** \| **sessionA** \| **sessionW** \| **sessionbasedA** \| **sessionbasedW  **\| **userbasedA \| userbasedF** \| **userbasedW** } [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ] ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[index*]：指定需要查看数据的日志主机索引号。*index*取值范围为0～3。

**[cmccPortA**]**：**指定中国移动公司的端口创建日志类型，并显示日志对应的MBUF池使用情况信息。

**[cmccPortF**]**：**指定中国移动公司的端口资源不足日志类型，并显示日志对应的MBUF池使用情况信息。

**[cmccPortW**]**：**指定中国移动公司的端口删除日志类型，并显示日志对应的MBUF池使用情况信息。

**[cmccSessionA**]**：**指定中国移动公司的session创建日志类型，并显示日志对应的MBUF池使用情况信息。

**[cmccSessionW**]**：**指定中国移动公司的session删除日志类型，并显示日志对应的MBUF池使用情况信息。

**[portA**]**：**指定中国联通公司的端口创建日志类型，并显示日志对应的MBUF池使用情况信息。

**[portW**]**：**指定中国联通公司的端口删除日志类型，并显示日志对应的MBUF池使用情况信息。

**[sessionA**]**：**指定中国联通公司的session创建日志类型，并显示日志对应的MBUF池使用情况信息。

**[sessionW**]**：**指定中国联通公司的session删除日志类型，并显示日志对应的MBUF池使用情况信息。

**[sessionbasedA**]**：**指定中国电信公司的session创建日志类型，并显示日志对应的MBUF池使用情况信息。

**[sessionbasedW **]**：**指定中国电信公司的session删除日志类型，并显示日志对应的MBUF池使用情况信息。

**[userbasedA**]**：**指定中国电信公司的端口创建日志，并显示日志对应的MBUF池使用情况信息。

**[userbasedF**]**：**指定中国电信公司的端口资源不足日志类型，并显示日志对应的MBUF池使用情况信息。

**[userbasedW**]**：**指定中国电信公司的端口删除日志，并显示日志对应的MBUF池使用情况信息。

**[slot** *slot-number*]：显示指定单板上的CPU内MBUF池的使用情况信息，*slot-number*表示单板所在槽位号。如未指定该参数，则显示当前日志主机主控板上CPU内MBUF使用情况。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的CPU内MBUF池的使用情况信息，*slot-number*表示设备在IRF中的成员编号。如未指定该参数，则显示当前日志主控板上CPU内MBUF使用情况。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上的CPU内MBUF池的使用情况信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如未指定该参数，则显示当前日志主控板上CPU内MBUF使用情况。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备和单板上的CPU内MBUF池的使用情况信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如未指定该参数，则显示当前日志主机主控板上CPU内MBUF使用情况。[（分布式设备－]IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的CPU内MBUF池的使用情况信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号[，]*slot-number*表示单板或PEX所在的槽位号。如未指定该参数，则显示当前日志主机主控板上CPU内MBUF使用情况。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：指定需要显示信息的成员设备所在[的]CPU。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]

**信息中心 \-- 信息中心Probe命令 \-- display system internal customlog test**

------------------------------------------------------------------------

![说明](信息中心Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display system internal customlog test**]命令用来发送指定数目CUSTOMLOG测试的报文，并显示日志发送结果信息。

【命令】

集中式设备

**[display system internal customlog test count ***number *[{ **cmccPortA** \| **cmccPortF** \| **cmccPortW** \| **cmccSessionA** \| **cmccSessionW** \| **portA** \| **portW** \| **sessionA** \| **sessionW** \| **sessionbasedA \| sessionbasedW** \| **userbasedA** \| **userbasedF** \| **userbasedW** }]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal customlog test count ***number*[ { **cmccPortA** \| **cmccPortF** \| **cmccPortW** \| **cmccSessionA** \| **cmccSessionW** \| **portA** \| **portW** \| **sessionA** \| **sessionW** \| **sessionbasedA \| sessionbasedW** \| **userbasedA** \| **userbasedF** \| **userbasedW** } [ **slot** *slot-number* [ **cpu** *cpu-number* ] ]]]

分布式设备－IRF模式：

**[display system internal customlog test count ***number*[ { **cmccPortA** \| **cmccPortF** \| **cmccPortW** \| **cmccSessionA** \| **cmccSessionW** \| **portA** \| **portW** \| **sessionA** \| **sessionW** \| **sessionbasedA \| sessionbasedW** \| **userbasedA** \| **userbasedF** \| **userbasedW** } [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ] ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：指定需要参与测试的CUSTOMLOG数目。*number*取值范围为1～100。

**[cmccPortA**]**：**指定中国移动公司的端口创建日志类型，并显示日志对应的测试日志发送结果信息。

**[cmccPortF**]**：**指定中国移动公司的端口资源不足日志类型，并显示日志对应的测试日志发送结果信息。

**[cmccPortW**]**：**指定中国移动公司的端口删除日志类型，并显示日志对应的测试日志发送结果信息。

**[cmccSessionA**]**：**指定中国移动公司的session创建日志类型，并显示日志对应的测试日志发送结果信息。

**[cmccSessionW**]**：**指定中国移动公司的session删除日志类型，并显示日志对应的测试日志发送结果信息。

**[portA**]**：**指定中国联通公司的端口创建日志类型，并显示日志对应的测试日志发送结果信息。

**[portW**]**：**指定中国联通公司的端口删除日志类型，并显示日志对应的测试日志发送结果信息。

**[sessionA**]**：**指定中国联通公司的session创建日志类型，并显示日志对应的测试日志发送结果信息。

**[sessionW**]**：**指定中国联通公司的session删除日志类型，并显示日志对应的测试日志发送结果信息。

**[sessionbasedA**]**：**指定中国电信公司的session创建日志类型，并显示日志对应的测试日志发送结果信息。

**[sessionbasedW **]**：**指定中国电信公司的session删除日志类型，并显示日志对应的测试日志发送结果信息。

**[userbasedA**]**：**指定中国电信公司的端口创建日志，并显示日志对应的测试日志发送结果信息。

**[userbasedF**]**：**指定中国电信公司的端口资源不足日志类型，并显示日志对应的测试日志发送结果信息。

**[userbasedW**]**：**指定中国电信公司的端口删除日志，并显示日志对应的测试日志发送结果信息。

**[slot** *slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在槽位号。如未指定该参数，则显示当前日志主机主控板上日志报文的发送结果信息。[（分布式设备－独立运行模式）]

**[slot** *slot-number*]：显示指定成员设备上的日志发送结果信息，*slot-number*表示设备在IRF中的成员编号。如未指定该参数，则显示当前日志主机主控板上日志报文的发送结果信息。[（集中式]IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上的日志发送结果信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号[。如未指定该参数，则显示当前日志主机主控板上日志报文的发送结果信息。（集中式]IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备和单板上的日志发送结果信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如未指定该参数，则显示当前日志主机主控板上日志报文的发送结果信息。[（分布式设备－]IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的日志发送结果信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号[，]*slot-number*表示单板或PEX所在的槽位号。如未指定该参数，则显示当前日志主机主控板上日志报文的发送结果信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：指定需要显示信息的成员设备所在[的]CPU。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]

