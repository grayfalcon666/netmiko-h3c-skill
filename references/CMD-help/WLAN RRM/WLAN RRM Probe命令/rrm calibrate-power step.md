
**WLAN RRM \-- WLAN RRM Probe命令 \-- rrm calibrate-power step**

------------------------------------------------------------------------

**[rrm calibrate-power step**]命令用来设置功率调整步长。

**[undo rrm calibrate-power step**]命令用来恢复缺省情况。

【命令】

**[rrm calibrate-power step **[{ **down** \| **up** } ]*value*]

**[undo rrm calibrate-power step **[{ **down** \| **up** }]]

【缺省情况】

增加功率或减小功率的调整步长为3。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[down**]：减小功率的步长。

**[up**]：增加功率的步长。

*[value*]：功调调整步长，取值范围为1～8，单位为dBm。

