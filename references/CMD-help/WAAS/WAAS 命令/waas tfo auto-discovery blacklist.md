
**WAAS \-- WAAS 命令 \-- waas tfo auto-discovery blacklist**

------------------------------------------------------------------------

**[waas tfo auto-discovery blacklist**]命令用来添加指定黑名单表项。

**[undo waas tfo auto-discovery blacklist**]命令用来删除指定黑名单表项。

【命令】

**[waas tfo auto-discovery blacklist **[{ **ip-address** *ip-address* \| **ipv6-address** *ipv6-address* } **port** *port-num*]]

**[undo waas tfo auto-discovery blacklist **[{ **ip-address** *ipv4-address* \| **ipv6-address** *ipv6-address* } **port** *port-num*]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip-address ***ip-address*]：指定黑名单表项的IPv4地址。

**[ipv6-address ***ipv6-address*]：指定黑名单表项的IPv6地址。

**[port ***port-num*]：指定黑名单表项的端口号，取值范围为1～65535。

