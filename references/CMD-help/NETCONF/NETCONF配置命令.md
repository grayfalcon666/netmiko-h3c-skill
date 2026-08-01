<!-- CMD-INDEX
  xml                                 | 用户视图             | L9
  netconf soap http enable            | 系统视图             | L69
  netconf soap https enable           | 系统视图             | L109
  netconf ssh server enable           | 系统视图             | L147
  netconf ssh server port             | 系统视图             | L189
-->

**NETCONF \-- NETCONF配置命令 \-- xml**

------------------------------------------------------------------------

**[xml**]命令用来进入XML视图。

【命令】

**[xml**]

【视图】

用户视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

进入XML视图后可以输入NETCONF指令来配置或者获取系统数据。用户登录时使用的角色不同，可执行的NETCONF操作也不同：

·network-admin和mdc-admin可执行全部操作。

·network-operator和mdc-operator可执行get、get-bulk、get-config、get-bulk-config、get-sessions、close-session操作。

需要注意的是：

·用户输入的NETCONF指令必须符合XML语言格式要求和《NETCONF XML API 手册》中的语法、语义要求。建议使用第三方软件来协助生成NETCONF指令，命令行手工输入方式通常用于研发和测试环境。

·退出XML视图时需要使用相关的NETCONF指令，不能使用**quit**。

·在XML模式下终止当前任务的快捷键有重置缓存的功能，快捷键之前的内容都会被清除掉。如果在用户线/用户线类视图下使用**escape-key**命令配置了终止当前任务的快捷键（默认为Ctrl+C），可能会影响XML视图下相关配置。例如：在用户线视图下配置了**escape-key **a，当NETCONF指令中含有字符'a'时，其实只有NETCONF指令最后一个'a'之后的内容能够得到处理；当NETCONF指令中不含有字符'a'时，则对XML视图下的配置没有影响。

【举例】

\# 进入XML视图。

\<Sysname\> xml

\<?xml version=\"1.0\" encoding=\"UTF-8\"?\>\<hello xmlns=\"urn:ietf:params:xml:ns:netconf:base:1.0\"\>\<capabilities\>\<capability\>urn:ietf:params:netconf:base:1.1\</capability\>\<capability\>urn:ietf:params:netconf:writable-running\</capability\>\<capability\>urn:ietf:params:netconf:capability:notification:1.0\</capability\>\<capability\>urn:ietf:params:netconf:capability:validate:1.1\</capability\>\<capability\>urn:ietf:params:netconf:capability:interleave:1.0\</capability\>\<capability\>urn:h3c:params:netconf:capability:h3c-netconf-ext:1.0\</capability\>\</capabilities\>\<session-id\>1\</session-id\>\</hello\>\>\>

\# 退出XML视图。

\<rpc message-id=\"101\" xmlns=\"urn:ietf:params:xml:ns:netconf:base:1.0\"\>

  \<close-session\>

  \</close-session\>

\</rpc\>\>\>

\<Sysname\>

**NETCONF \-- NETCONF配置命令 \-- netconf soap http enable**

------------------------------------------------------------------------

**[netconf soap http enable**]命令用来开启基于HTTP的SOAP功能。

【命令】

**[netconf soap http enable**]

**[undo netconf soap http enable**]

【缺省情况】

基于HTTP的SOAP功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

FIPS模式下，不支持本命令。

配置该命令后，表示设备能够解析这样的HTTP报文，报文中的数据为SOAP封装过的NETCONF指令。

【举例】

\# 开启基于HTTP的SOAP功能。

\<Sysname\> system-view

Sysname netconf soap http enable

**NETCONF \-- NETCONF配置命令 \-- netconf soap https enable**

------------------------------------------------------------------------

**[netconf soap https enable**]命令用来开启基于HTTPS的SOAP功能。

【命令】

**[netconf soap https enable**]

**[undo netconf soap https enable**]

【缺省情况】

基于HTTPS的SOAP功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

配置该命令后，表示设备能够解析这样的HTTPS报文，报文中的数据为SOAP封装过的NETCONF指令。

【举例】

\# 开启基于HTTPS的SOAP功能。

\<Sysname\> system-view

Sysname netconf soap https enable

**NETCONF \-- NETCONF配置命令 \-- netconf ssh server enable**

------------------------------------------------------------------------

**[netconf** **ssh** **server** **enable**]命令用来开启NETCONF Over SSH的接入方式。

**[undo** **netconf** **ssh** **server** **enable**]命令用来关闭NETCONF Over SSH的接入方式。

【命令】

**[netconf** **ssh** **server** **enable**]

**[undo** **netconf** **ssh** **server** **enable**]

【缺省情况】

未开启NETCONF Over SSH的接入方式。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

用户配置该命令后，可以利用SSH客户端通过SSH子系统的方式接入设备的NETCONF系统，然后直接进入NETCONF配置模式，而不用手工输入XML命令。

使能该命令前必须在设备上把SSH连接终端的认证方式设置为scheme，支持NETCONF over SSH的客户端才能连接到NETCONF系统，目前只支持用urn:ietf:params:netconf:base:1.0（设备与终端共同支持的能力集）连接系统。

【举例】

\# 开启NETCONF Over SSH的接入方式。

\<Sysname\> system

Sysname netconf ssh server enable

**NETCONF \-- NETCONF配置命令 \-- netconf ssh server port**

------------------------------------------------------------------------

**[netconf** **ssh** **server port**]命令用来设置 NETCONF Over SSH接入方式的监听端口号。

**[undo** **netconf** **ssh** **server** **port**]命令用来把端口号恢复成默认的830。

【命令】

**[netconf** **ssh** **server** **port** *port-number*]

**[undo** **netconf ssh** **server** **port**]

【缺省情况】

基于NETCONF Over SSH的接入方式的监听端口是830。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-number*]：基于NETCONF Over SSH的接入方式的监听端口，取值范围为1～65535，缺省值为830。

【使用指导】

用户可以在必要时使用此命令来重新配置一个端口作为NETCONF子系统的监听端口，但由于SSH服务使用共享端口的方式来分配监听端口，为了正常使用，必须保证分配的端口不和其他使用的端口冲突。

【举例】

\# 把基于NETCONF Over SSH的接入方式的监听端口设置为800。

\<sysname\> system

sysname netconf ssh server port 800

