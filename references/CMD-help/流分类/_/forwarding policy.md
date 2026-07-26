
**流分类 \-- forwarding policy**

------------------------------------------------------------------------

**[forwarding policy**]命令用来配置流分类策略。

**[undo forwarding policy**]命令用来恢复缺省情况。

【命令】

**[forwarding policy **[{ **per-flow** \| **per-packet** }]]

**[undo forwarding policy**]

【缺省情况】

采用基于流处理的流分类策略。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[per-flow**]：基于流处理，同一条流被分配到同一个CPU进行处理，处理过程保证先进先出。

**[per-packet**]：基于报文处理，将报文依次发送到不同的CPU进行处理，不保证报文的处理顺序。

【举例】

\# 配置流分类策略为基于报文处理。

\<Sysname\> system-view

Sysname forwarding policy per-packet

\# 配置流分类策略为基于流处理。

\<Sysname\> system-view

Sysname forwarding policy per-flow
