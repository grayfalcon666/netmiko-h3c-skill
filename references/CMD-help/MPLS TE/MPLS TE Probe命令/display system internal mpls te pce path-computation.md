
**MPLS TE \-- MPLS TE Probe命令 \-- display system internal mpls te pce path-computation**

------------------------------------------------------------------------

**[display system internal mpls te pce path-computation**]命令用来显示PCE路径计算过程的相关信息。

【命令】

**[display system internal mpls te pce path-computation ** **source**]*****ip-address ***destination ***ip-address*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[source***ip-ddress*]：指定计算路径的源IP地址。

**[destination ***ip-address*]：指定计算路径的目的IP地址。

**MPLS TE \-- MPLS TE Probe命令 \-- mpls te path-calculation**

------------------------------------------------------------------------

**[mpls te path-calculation**]命令用来根据指定的约束条件进行CSPF计算并返回计算结果。

【命令】

**[mpls te path-calculation**[ { **destination** *address* \| **tunnel-interface** **tunnel** *number* [ **destination** *address* ] } [ **bandwidth** [ **ct0** \| **ct1** \| **ct2** \| **ct3** ] *bandwidth-value* ]  **priority** *setup-priority* [ *hold-priority*  ]  **affinity** *attribute-value* [ **mask** *mask-value*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[destination**]* address*：指定CSPF计算的目的地址。

**[tunnel-interface tunnel**]* number*：从指定Tunnel接口获取CSPF计算使用的约束条件。*number*为Tunnel接口的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[bandwidth**  [ **ct0** \| **ct1** \| **ct2** \| **ct3** ] *bandwidth-value*]：指定CSPF计算需要满足的带宽条件。如果没有指定任何CT，则隧道流量属于CT 0。

·**ct0**：指定隧道流量属于CT 0。

·**ct1**：指定隧道流量属于CT 1。

·**ct2**：指定隧道流量属于CT 2。

·**ct3**：指定隧道流量属于CT 3。

·*bandwidth-value*：MPLS TE隧道所需的带宽，取值范围为1～4294967295，单位为kbps。

**[priority**] *setup-priority* [ *hold-priority* ]：指定CSPF计算的建立优先级和保持优先级。*setup-priority*为建立优先级，取值范围为0～7；*hold-priority*为保持优先级，取值范围为0～7。数值越小优先级越高。如果不指定*hold-priority*参数，则保持优先级与建立优先级相同。

**[affinity** *attribute-value* [ **mask** *mask-value* ]]：指定CSPF计算的亲和属性及其掩码。

·*attribute-value*为亲和属性，取值范围为0x00000000～0xFFFFFFFF，即为32位的二进制数。亲和属性中的每一位二进制数代表一种属性，属性值为0或1。

·*mask-value*为亲和属性掩码，取值范围为0x00000000～0xFFFFFFFF，即为32位的二进制数。掩码中的每一位二进制数都表示是否检查该位的链路属性。掩码为1，表示需要检查该位的链路属性，只有该位的链路属性满足一定条件时，才可以使用该链路；掩码为0，表示不检查该位的链路属性，不管该位的链路属性与隧道的亲和属性是否相同，都可以使用该链路。

【使用指导】

通过本命令可以指定的CSPF计算约束条件包括隧道所需带宽、优先级和亲和属性。约束条件可以通过以下两种方式指定：

·指定**tunnel*** number*参数，采用该Tunnel接口下配置的约束条件进行CSPF计算。

·通过指定**destination**、**bandwidth**、**priority**或**affinity**参数，手工指定CSPF计算的约束条件。

手工指定的约束条件优先级高于通过Tunnel接口获取的约束条件，即如果在指定**tunnel*** number*参数的同时，指定了**destination**、**bandwidth**、**priority**或**affinity**参数，则采用手工指定的约束条件进行CSPF计算。
