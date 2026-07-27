<!-- CMD-INDEX
  display system internal l2vpn ldp   | 任意视图             | L5
-->

**VPLS \-- VPLS Probe命令 \-- display system internal l2vpn ldp**

------------------------------------------------------------------------

**[display system internal l2vpn ldp**]命令用来显示LDP协议备进程的PW标签相关信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal l2vpn ldp **[[ **peer** *ip-address* [ **pw-id** *pw-id* \| **vpls-id** *vpls-id* ] ]  **verbose** ]  **standby slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal l2vpn ldp **[[ **peer** *ip-address* [ **pw-id** *pw-id* \| **vpls-id** *vpls-id* ] ]  **verbose** ] **standby chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[peer*** ip-address*]：显示指定远端PE通过LDP通告的PW标签相关信息。*ip-address*为远端PE的LSR ID。如果没有指定本参数，则显示所有远端PE通过LDP通告的PW标签相关信息。

**[pw-id ***pw-id*]：显示指定FEC 128方式的PW标签相关信息。*pw-id*为PW的PW ID，取值范围为1～4294967295。本参数和**peer**参数配合使用，如果只指定了**peer*** ip-address*参数，则显示指定远端PE通过LDP通告的所有PW标签相关信息。

**[vpls-id ***vpls-id*]：显示指定FEC 129方式的PW标签相关信息。*vpls-id*表示VPLS ID，即VPLS实例标识符，为3～21个字符的字符串，VPLS ID有三种格式：

·16位自治系统号:32位用户自定义数，例如：101:3。

·32位IP地址:16位用户自定义数，例如：192.168.122.15:1。

·32位自治系统号:16位用户自定义数字，其中的自治系统号最小值为65536。例如：65536:1。

**[verbose**]：显示详细信息。如果不指定本参数，则显示简要信息。

**[standby**]**：**显示指定LDP备进程的信息。

**[slot**]* slot-number*：指定备进程所在的主控板。*slot-number*为主控板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：指定备进程所在的成员设备。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis **]*chassis-number* **slot** *slot-number*：指定备进程所在的成员设备和主控板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示主控板所在的槽位号。（分布式设备－IRF模式）

**[cpu ***cpu-number*]：指定备进程所在的CPU。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

LDP可以通过如下两种方式通告PW标签：

·执行**peer**命令手工指定远端PE后，LDP通告FEC 128和PW标签的绑定关系。

·采用BGP协议自动发现远端PE后，LDP通告FEC 129和PW标签的绑定关系。

本命令可以用来显示通过上述两种方式通告的PW标签。

执行本命令时，如果指定了**pw-id ***pw-id*参数，则显示指定FEC 128方式的PW标签相关信息；如果指定了**vpls-id ***vpls-id*参数，则显示指定FEC 129方式的PW标签相关信息；如果没有指定**pw-id ***pw-id*和**vpls-id ***vpls-id*参数，则同时显示FEC 128方式和FEC 129方式的PW标签相关信息。

执行本命令时，本设备接收到的LDP PW标签映射信息都会显示；而本设备通告的PW标签映射只有成功通告给远端PE后才会显示。

