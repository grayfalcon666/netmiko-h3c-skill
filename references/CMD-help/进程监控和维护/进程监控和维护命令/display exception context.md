
**进程监控和维护 \-- 进程监控和维护命令 \-- display exception context**

------------------------------------------------------------------------

**[display exception context**]命令用来显示用户态进程异常时的上下文信息。

【命令】

集中式设备：

**[display exception context ** **count** *value* ]

分布式设备－独立运行模式/集中式IRF设备：

**[display** **exception context** [ **count** *value*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display** **exception context** [ **count** *value*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[count** *value*]：表示上下文信息的显示个数，取值范围为1～20，缺省值为1。

**[slot** *slot-number*]：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示IRF中设备的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）

**[chassis*** chassis-number ***slot** *slot-number*]：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

当用户态进程发生一次异常，系统会生成一个core文件，还会生成一条上下文信息，用于记录异常用户态进程的ID、生成core文件的时间、core文件存放的位置、栈信息和寄存器信息。一个core文件对应一条上下文信息，最多可记录的上下文信息数和可记录的core文件数目相同。

【举例】

\# 显示在x86体系32位设备上的异常上下文信息。

\<Sysname\> display exception context

Index 1 of 1

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Crashed PID: 120 (routed)

Crash signal: SIGBUS

Crash time: Tue Apr  9 17:14:30 2013

Core file path:

flash:/core/node0_routed_120_7_20130409-171430_1365527670.core

#0  0xb7caba4a

#1  0x0804cb79

#2  0xb7cd77c4

#3  0x08049f45

Backtrace stopped.

                          Registers\' content

  eax:0xfffffffc   ebx:0x00000003   ecx:0xbfe244ec   edx:0x0000000a

  esp:0xbfe244b8   ebp:0xbfe244c8   esi:0xffffffff   edi:0xbfe24674

  eip:0xb7caba4a eflag:0x00000292    cs:0x00000073    ss:0x0000007b

   ds:0x0000007b    es:0x0000007b    fs:0x00000000    gs:0x00000033

\# 显示在x86体系64位设备上的异常上下文信息。

\<Sysname\> display exception context

Index 1 of 1

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Crashed PID: 121 (routed)

Crash signal: SIGBUS

Crash time: Sun Mar 31 11:12:21 2013

Core file path:

flash:/core/node0_routed_121_7_20130331-111221_1364728341.core

#0  0x00007fae7dbad20c

#1  0x00000000004059fa

#2  0x00007fae7dbd96c0

#3  0x0000000000402b29

Backtrace stopped.

                          Registers\' content

       rax:0xfffffffffffffffc       rbx:0x00007fff88a5dd10

       rcx:0xffffffffffffffff       rdx:0x000000000000000a

       rsi:0x00007fff88a5dd10       rdi:0x0000000000000003

       rbp:0x00007fff88a5dcf0       rsp:0x00007fff88a5dcf0

        r8:0x00007fae7ea587e0        r9:0x0000000000000079

       r10:0xffffffffffffffff       r11:0x0000000000000246

       r12:0x0000000000405b18       r13:0x00007fff88a5ff7a

       r14:0x00007fff88a5de30       r15:0x0000000000000000

       rip:0x00007fae7dbad20c      flag:0x0000000000000246

        cs:0x0000000000000033        ss:0x000000000000002b

        ds:0x0000000000000000        es:0x0000000000000000

        fs:0x0000000000000000        gs:0x0000000000000000

   fs_base:0x00007fae80a5d6a0   gs_base:0x0000000000000000

   orig_ax:0x00000000000000e8

\# 显示在powerpc体系32位设备上的异常上下文信息。

\<Sysname\> display exception context

Index 1 of 1

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Crashed PID: 133 (routed)

Crash signal: SIGBUS

Crash time: Wed Apr 10 15:47:49 2013

Core file path:

flash:/core/node0_routed_133_7_20130410-154749_1365608869.core

#0  0x184720bc

#1  0x10006b4c

Backtrace stopped.

                          Registers\' content

grp00: 0x000000ee 0x7ffd6ad0 0x1800f440 0x00000004

grp04: 0x7ffd6af8 0x0000000a 0xffffffff 0x184720bc

grp08: 0x0002d200 0x00000003 0x00000001 0x1847209c

grp12: 0x10006b4c 0x10020534 0xd6744100 0x00000000

grp16: 0x00000000 0xa0203ff0 0xa028b12c 0xa028b13c

grp20: 0xa028b148 0xa028b168 0xa028b178 0xa028b190

grp24: 0xa028b1a8 0xa028b1b8 0x00000000 0x7ffd6c08

grp28: 0x10006cac 0x7ffd6f92 0x184c1b84 0x7ffd6ae0

  nip:0x184720bc    lr:0x10006b4c    cr:0x38000022   ctr:0x1847209c

  msr:0x0002db00   xer:0x00000000   ret:0xfffffffc dsisr:0x08000000

  gr3:0x00000003    mq:0x00000000  trap:0x00000c00   dar:0x1833114c

\# 显示在powerpc体系64位设备上的异常上下文信息。

\<Sysname\> display exception context

Index 1 of 1

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Crashed PID: 172 (routed)

Crash signal: SIGBUS

Crash time: Sat Sep 15 16:53:16 2007

Core file path:

cfa0:/core/node1_routed_172_7_20070915-165316_1189875196.core

#0  0x00000fff803c66b4

#1  0x0000000010009b94

#2  0x00000fff80401814

Backtrace stopped.

                          Registers\' content

     grp00: 0x00000000000000ee 0x00000fffffd04840

     grp02: 0x00000fff80425c28 0x0000000000000004

     grp04: 0x00000fffffd048c0 0x000000000000000a

     grp06: 0xffffffffffffffff 0x00000fff803c66b4

     grp08: 0x000000008002d000 0x0000000000000000

     grp10: 0x0000000000000000 0x0000000000000000

     grp12: 0x0000000000000000 0x00000fff80a096b0

     grp14: 0x000000007b964c00 0x000000007b7d0000

     grp16: 0x0000000000000001 0x000000000000000b

     grp18: 0x0000000000000031 0x0000000000a205b8

     grp20: 0x0000000000a20677 0x0000000000000000

     grp22: 0x000000007bb91014 0x0000000000000000

     grp24: 0xc0000000005ae1c8 0x0000000000000000

     grp26: 0xc0000001f00bff20 0xc0000001f00b0000

     grp28: 0x00000fffffd04a30 0x000000001001aed8

     grp30: 0x00000fffffd04fae 0x00000fffffd04840

       nip:0x00000fff803c66b4        lr:0x0000000010009b94

        cr:0x0000000058000482       ctr:0x00000fff803c66ac

       msr:0x000000008002d000       xer:0x0000000000000000

       ret:0xfffffffffffffffc     dsisr:0x0000000000000000

       gr3:0x0000000000000003     softe:0x0000000000000001

      trap:0x0000000000000c00       dar:0x00000fff8059d14c

\# 显示在mips体系32位设备上的异常上下文信息。

\<Sysname\> display exception context

Index 1 of 1

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Crashed PID: 182 (routed)

Crash signal: SIGBUS

Crash time: Sun Jan  2 08:11:38 2013

Core file path:

flash:/core/node4_routed_182_10_20130102-081138_1293955898.core

#0  0x2af2faf4

#1  0x00406d8c

Backtrace stopped.

                          Registers\' content

 zero:0x00000000   at:0x1000dc00   v0:0x00000004   v1:0x00000003

   a0:0x00000003   a1:0x7fd267e8   a2:0x0000000a   a3:0x00000001

   t0:0x00000000   t1:0xcf08fa14   t2:0x80230510   t3:0xfffffff8

   t4:0x69766520   t5:0x00000000   t6:0x63cc6000   t7:0x44617461

   s0:0x7fd26f81   s1:0x00401948   s2:0x7fd268f8   s3:0x803e1db0

   s4:0x803e1da0   s5:0x803e1d88   s6:0x803e1d70   s7:0x803e1d60

   t8:0x00000008   t9:0x2af2fae0   k0:0x00000000   k1:0x00000000

   gp:0x2af9a3a0   sp:0x7fd267c0   s8:0x7fd267c0   ra:0x00406d8c

   sr:0x0000dc13   lo:0xef9db265   hi:0x0000003f  bad:0x2add2010

cause:0x00800020   pc:0x2af2faf4

\# 显示在mips体系64位设备上的异常上下文信息。

\<Sysname\> display exception context

Index 1 of 1

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Crashed PID: 270 (routed)

Crash signal: SIGBUS

Crash time: Wed Mar 27 12:39:12 2013

Core file path:

flash:/core/node16_routed_270_10_20130327-123912_1364387952.core

#0  0x0000005555a3bcb4

#1  0x0000000120006c1c

Backtrace stopped.

                          Registers\' content

      zero:0x0000000000000000        at:0x0000000000000014

        v0:0x0000000000000004        v1:0x0000000000000003

        a0:0x0000000000000003        a1:0x000000ffff899d90

        a2:0x000000000000000a        a3:0x0000000000000001

        a4:0x0000005555a9b4e0        a5:0x0000000000000000

        a6:0xffffffff8021349c        a7:0x20696e206368616e

        t0:0x0000000000000000        t1:0xffffffff80105068

        t2:0xffffffff80213890        t3:0x0000000000000008

        s0:0x0000005555a99c40        s1:0x000000ffff89af5f

        s2:0x0000000120007320        s3:0x0000005555a5f470

        s4:0x000000ffff899f80        s5:0xffffffff803cc6c0

        s6:0xffffffff803cc6a8        s7:0xffffffff803cc690

        t8:0x0000000000000002        t9:0x0000005555a3bc98

        k0:0x0000000000000000        k1:0x0000000000000000

        gp:0x0000000120020460        sp:0x000000ffff899d70

        s8:0x000000ffff899d80        ra:0x0000000120006c1c

        sr:0x000000000400fff3        lo:0xdf3b645a1cac08c9

        hi:0x000000000000007f       bad:0x000000555589ba84

     cause:0x0000000000800020        pc:0x0000005555a3bcb4

表1-1 display exception context命令输出信息描述表

字段

描述

Crashed PID

发生异常的用户态进程ID

Crash signal

导致异常的信号：

·SIGABRT：异常终止（abort）

·SIGBUS：总线错误

·SIGFPE：浮点异常

·SIGILL：程序执行了非法指令，导致异常

·SIGQUIT：终端退出符

·SIGSEGV：无效存储访问

·SIGSYS：无效系统调用

·SIGTRAP：跟踪断点时发生了异常

·SIGXCPU：超过CPU限制（setrlimit）

·SIGXFSZ：超过文件长度限制（setrlimit）

·SIGUNKNOW：未知原因

Crash time

异常发生的时间

Core file path

core文件存放的位置

Backtrace stopped

表示栈信息已经显示完毕

Registers' content

寄存器的内容

【相关命令】

·**reset exception context**

**进程监控和维护 \-- 进程监控和维护命令 \-- display exception filepath**

------------------------------------------------------------------------

**[display exception filepath**]命令用来显示core文件的保存路径。

【命令】

集中式设备：

**[display exception filepath**]

分布式设备－独立运行模式/集中式IRF设备：

**[display exception filepath** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display exception filepath** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）

**[chassis*** chassis-number ***slot** *slot-number*]：：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示主控板上core文件的保存路径。（集中式设备）

\<Sysname\> display exception filepath

The exception filepath is flash:.

\# 显示主用主控板上core文件的保存路径。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display exception filepath

The exception filepath on slot 0 is flash:.

\# 显示备用主控板上core文件的保存路径。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display exception filepath slot 1

The exception filepath on slot 1 is NULL.

\# 显示全局主用主控板上core文件的保存路径。（分布式设备－IRF模式）

\<Sysname\> display exception filepath

The exception filepath on chassis 0 slot 1 is flash:.

**进程监控和维护 \-- 进程监控和维护命令 \-- display kernel deadloop**

------------------------------------------------------------------------

**[display kernel deadloop**]命令用来显示内核线程死循环信息。

【命令】

集中式设备：

**[display kernel deadloop ***show-number***** *offset* ]  **verbose**

分布式设备－独立运行模式/集中式IRF设备：

**[display kernel deadloop ***show-number***** *offset* ]  **verbose**   **slot** *slot-number* [ **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display kernel deadloop ***show-number***** *offset* ]  **verbose**   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[show-number*]：需要显示的死循环信息的数目，取值范围为1～20。

*[offset*]：需要显示的起始条目距最近条目的偏移，取值范围为0～19，缺省值为0。

**[verbose**]：表示显示详细信息。不指定该参数时，显示概要信息。

**[slot** *slot-number*]：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示IRF中设备的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）

**[chassis*** chassis-number ***slot** *slot-number*]：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示最近一条内核线程死循环的概要信息。

\<Sysname\> display kernel deadloop 1

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- Deadloop record 1 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Description          : BUG: soft lockup - CPU#0 stuck for 61! [comsh: 16306]

Recorded at          : 2013-05-01  11:16:00.823018

Occurred at          : 2013-05-01  11:16:00.823018

Instruction address  : 0x4004158c

Thread               : comsh (TID: 16306)

Context              : thread context

Chassis              : 0

Slot                 : 0

CPU ID               : 0

Kernel module info   : module name (mrpnc) module address (0xe332a000)

                       module name (12500) module address (0xe00bd000)

\# 显示最近一条内核线程死循环的详细信息。

\<Sysname\> display kernel deadloop 1 verbose

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- Deadloop record 1 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Description          : BUG: soft lockup - CPU#0 stuck for 61! [comsh: 16306]

Recorded at          : 2013-05-01  11:16:00.823018

Occurred at          : 2013-05-01  11:16:00.823018

Instruction address  : 0x4004158c

Thread               : comsh (TID: 16306)

Context              : thread context

Chassis              : 0

Slot                 : 0

CPU ID               : 0

Kernel module info   : module name (mrpnc) module address (0xe332a000)

                       module name (12500) module address (0xe00bd000)

Last 5 thread switches : migration/0 (11:16:00.823018)\--\>

                         swapper (11:16:00.833018)\--\>

                         kthreadd (11:16:00.833518)\--\>

                         swapper (11:16:00.833550)\--\>

                         disk (11:16:00.833560)

Register content:

Reg:       r0, Val = 0x00000000 ; Reg:       r1, Val = 0xe2be5ea0 ;

Reg:       r2, Val = 0x00000000 ; Reg:       r3, Val = 0x77777777 ;

Reg:       r4, Val = 0x00000000 ; Reg:       r5, Val = 0x00001492 ;

Reg:       r6, Val = 0x00000000 ; Reg:       r7, Val = 0x0000ffff ;

Reg:       r8, Val = 0x77777777 ; Reg:       r9, Val = 0x00000000 ;

Reg:      r10, Val = 0x00000001 ; Reg:      r11, Val = 0x0000002c ;

Reg:      r12, Val = 0x057d9484 ; Reg:      r13, Val = 0x00000000 ;

Reg:      r14, Val = 0x00000000 ; Reg:      r15, Val = 0x02000000 ;

Reg:      r16, Val = 0xe2be5f00 ; Reg:      r17, Val = 0x00000000 ;

Reg:      r18, Val = 0x00000000 ; Reg:      r19, Val = 0x00000000 ;

Reg:      r20, Val = 0x024c10f8 ; Reg:      r21, Val = 0x057d9244 ;

Reg:      r22, Val = 0x00002000 ; Reg:      r23, Val = 0x0000002c ;

Reg:      r24, Val = 0x00000002 ; Reg:      r25, Val = 0x24000024 ;

Reg:      r26, Val = 0x00000000 ; Reg:      r27, Val = 0x057d9484 ;

Reg:      r28, Val = 0x0000002c ; Reg:      r29, Val = 0x00000000 ;

Reg:      r30, Val = 0x0000002c ; Reg:      r31, Val = 0x00000000 ;

Reg:       cr, Val = 0x84000028 ; Reg:      nip, Val = 0x057d9550 ;

Reg:      xer, Val = 0x00000000 ; Reg:       lr, Val = 0x0186eff0 ;

Reg:      ctr, Val = 0x682f7344 ; Reg:      msr, Val = 0x00784b5c ;

Reg:     trap, Val = 0x0000b030 ; Reg:      dar, Val = 0x77777777 ;

Reg:    dsisr, Val = 0x40000000 ; Reg:   result, Val = 0x00020300 ;

Dump stack (total 1024 bytes, 16 bytes/line):

0xe2be5ea0: 02 be 5e c0 24 00 00 24 00 00 00 00 05 7d 94 84

0xe2be5eb0: 00 00 00 04 00 00 00 00 00 00 00 28 05 8d 34 c4

0xe2be5ec0: 02 be 60 a0 01 86 ef f0 00 00 00 00 00 00 00 00

0xe2be5ed0: 02 04 05 b4 00 00 00 00 00 00 00 00 00 00 00 00

0xe2be5ee0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

0xe2be5ef0: 95 47 73 35 00 00 00 00 00 00 00 00 00 00 00 00

0xe2be5f00: a0 e1 64 21 00 00 00 00 00 00 00 00 00 00 00 00

0xe2be5f10: 00 00 00 00 00 00 00 00 00 00 00 00 01 e9 00 00

0xe2be5f20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

0xe2be5f30: 00 00 00 00 00 00 00 00 02 be 66 c0 02 be 66 d0

0xe2be5f40: 02 be 61 e0 00 00 00 02 00 00 00 00 02 44 b3 a4

0xe2be5f50: 02 be 5f 90 00 00 00 08 02 be 5f e0 00 00 00 08

0xe2be5f60: 02 be 5f 80 00 ac 1b 14 00 00 00 00 00 00 00 00

0xe2be5f70: 05 b4 5f 90 02 be 5f e0 00 00 00 30 02 be 5f e0

0xe2be5f80: 02 be 5f c0 00 ac 1b f4 00 00 00 00 02 45 00 00

0xe2be5f90: 00 03 00 00 00 00 00 00 02 be 5f e0 00 00 00 30

0xe2be5fa0: 02 be 5f c0 00 ac 1b 14 61 f1 2e ae 02 45 00 00

0xe2be5fb0: 02 44 b3 74 02 be 5f d0 00 00 00 30 02 be 5f e0

0xe2be5fc0: 02 be 60 60 01 74 ff f8 00 00 00 00 00 00 08 00

0xe2be5fd0: 02 be 5f f0 00 e8 93 7e 02 be 5f f8 02 be 5f fc

0xe2be5fe0: 00 00 00 00 00 00 00 00 00 00 00 00 02 be 60 18

0xe2be5ff0: 02 be 60 10 00 e9 65 98 00 00 00 58 00 00 2a 4f

0xe2be6000: 02 be 60 10 00 00 00 00 00 00 00 00 02 be 60 68

0xe2be6010: 02 be 60 40 00 e8 c6 a0 00 00 11 17 00 00 00 00

0xe2be6020: 02 be 60 40 00 00 00 00 00 00 00 00 02 be 60 98

0xe2be6030: 02 27 00 00 00 00 00 00 00 00 00 00 02 be 60 68

0xe2be6040: 02 be 60 60 00 00 00 01 00 00 b0 30 02 be 60 98

0xe2be6050: 00 00 00 04 02 21 00 00 00 00 00 00 01 e9 00 00

0xe2be6060: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

0xe2be6070: 00 00 00 00 00 00 00 00 02 be 66 c0 02 be 66 d0

0xe2be6080: 02 be 61 e0 00 00 00 02 00 00 00 00 02 be 61 70

0xe2be6090: 00 00 00 00 02 21 00 00 05 8d 34 c4 05 7d 92 44

Call trace:

Function Address = 0x8012a4b4

Function Address = 0x8017989c

Function Address = 0x80179b30

Function Address = 0x80127438

Function Address = 0x8012d734

Function Address = 0x80100a00

Function Address = 0xe0071004

Function Address = 0x8016ce0c

Function Address = 0x801223a0

Instruction dump:

41a2fe9c 812300ec 800200ec 7f890000 409efe8c 80010014 540b07b9 40a2fe80

4bfffe6c 80780290 7f64db78 4804ea35 \<807f002c\> 38800000 38a00080 3863000c

表1-2 display kernel deadloop命令显示信息描述表

字段

描述

Description

发生死循环的内核线程的描述信息，包括死循环内核线程所在的CPU的编号、内核线程连续运行的时间、内核线程的名称和编号

Recorded at

内核线程死循环被记录到主控板上的时间点，精确到微秒

Occurred at

内核线程发生死循环的时间，精确到微秒

Instruction address

内核线程被检测到发生死循环时对应的指令信息

Thread

发生死循环的内核线程的名称和编号

Context

内核线程被检测到发生死循环时所在的上下文环境

Chassis

运行该内核线程的设备的成员编号（仅IRF模式支持）

Slot

运行该内核线程的主控板所在的槽位号（分布式设备－独立运行模式/分布式设备－IRF模式）

运行该内核线程的设备的成员编号（集中式IRF设备）

为固定值0，无特殊意义（集中式设备）

CPU ID

运行该内核线程的CPU的编号

Kernel module info

内核线程被检测到发生死循环时，系统中已加载的内核模块信息。包括内核模块名和内核模块加载的内存地址

Last 5 thread switches

内核线程被检测到发生死循环时，记录死循环发生的CPU上、最近五次的内核线程切换轨迹。包括内核线程的名称和内核线程切换时间点，时间精确到微秒

Register content

内核线程被检测到发生死循环时现场的寄存器信息。Reg表示寄存器名称，Val表示寄存器中保存的值

Dump stack

内核线程被检测到发生死循环时现场的堆栈信息

Call trace

内核线程被检测到发生死循环时现场的函数调用栈信息，即每级调用函数的指令地址

Instruction dump

内核线程被检测到发生死循环时对应的指令码。非法指令用ffffffff表示

No information to display

表示系统中没有内核线程死循环记录

【相关命令】

·**reset ****kernel deadloop**

**进程监控和维护 \-- 进程监控和维护命令 \-- display kernel deadloop configuration**

------------------------------------------------------------------------

**[display kernel deadloop configuration**]命令用来显示内核线程死循环监控参数配置。

【命令】

集中式设备：

**[display kernel deadloop configuration**]

分布式设备－独立运行模式/集中式IRF设备：

**[display kernel deadloop configuration ** **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display kernel deadloop configuration ** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示IRF中设备的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）

**[chassis*** chassis-number ***slot** *slot-number*]：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示内核线程死循环监控参数配置。

\<Sysname\> display kernel deadloop configuration

Thread dead loop detection: Enabled

Dead loop timer (in seconds): 60

Threads excluded from monitoring: 1

  TID:     15   Name: co0   

表1-3 display kernel deadloop configuration命令显示信息描述表

字段

描述

Thread dead loop detection: Enabled

内核线程死循环检测功能处于开启状态

Thread dead loop detection: Disabled

内核线程死循环检测功能处于关闭状态

Dead loop timer (in seconds): *n*

内核线程死循环判定周期（单位为秒），即内核线程连续运行时间大于*n*秒时，则判定为死循环

Threads excluded from monitoring

不进行死循环检测的内核线程列表，配置**monitor kernel deadloop exclude-thread**命令后才会显示该信息

Name

不进行死循环检测的内核线程的名称

TID

不进行死循环检测的内核线程的编号

No thread is excluded from monitoring

对所有内核线程都进行死循环检查

**进程监控和维护 \-- 进程监控和维护命令 \-- display kernel exception**

------------------------------------------------------------------------

**[display kernel exception**]命令用来显示内核线程的异常信息。

【命令】

集中式设备：

**[display kernel exception ***show-number***** *offset* ]  **verbose**

分布式设备－独立运行模式/集中式IRF设备：

**[display kernel exception ***show-number***** *offset* ]  **verbose**   **slot** *slot-number* [ **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display kernel exception ***show-number***** *offset* ]  **verbose**   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[show-number*]：需要显示的异常信息的数目，取值范围为1～20。

*[offset*]：开始显示的条目距最近条目的偏移，取值范围为0～19，缺省值为0。

**[verbose**]：显示详细信息。不指定该参数时，显示概要信息。

**[slot** *slot-number*]：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示IRF中设备的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）

**[chassis*** chassis-number ***slot** *slot-number*]：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

当内核线程在运行过程中发生异常时，系统会自动记录异常信息，以便设备维护人员定位问题。

【举例】

\# 显示最近一条内核线程异常的概要信息。

\<Sysname\> display kernel exception 1

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- Exception record 1 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Description          : Oops[#0]

Recorded at          : 2013-05-01  11:16:00.823018

Occurred at          : 2013-05-01  11:16:00.823018

Instruction address  : 0x4004158c

Thread               : comsh (TID: 16306)

Context              : thread context

Chassis              : 0

Slot                 : 0

CPU ID               : 0

Kernel module info   : module name (mrpnc) module address (0xe332a000)

                       module name (disk) module address (0xe00bd000)

\# 显示最近一条内核线程异常的详细信息。

\<Sysname\> display kernel exception 1 verbose

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- Exception record 1 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Description          : Oops[#0]

Recorded at          : 2013-05-01  11:16:00.823018

Occurred at          : 2013-05-01  11:16:00.823018

Instruction address  : 0x4004158c

Thread               : comsh (TID: 16306)

Context              : thread context

Chassis              : 0

Slot                 : 0

CPU ID               : 0

Kernel module info   : module name (mrpnc) module address (0xe332a000)

                       module name (12500) module address (0xe00bd000)

Last 5 thread switches : migration/0 (11:16:00.823018)\--\>

                         swapper (11:16:00.833018)\--\>

                         kthreadd (11:16:00.833518)\--\>

                         swapper (11:16:00.833550)\--\>

                         disk (11:16:00.833560)

Register content:

Reg:       r0, Val = 0x00000000 ; Reg:       r1, Val = 0xe2be5ea0 ;

Reg:       r2, Val = 0x00000000 ; Reg:       r3, Val = 0x77777777 ;

Reg:       r4, Val = 0x00000000 ; Reg:       r5, Val = 0x00001492 ;

Reg:       r6, Val = 0x00000000 ; Reg:       r7, Val = 0x0000ffff ;

Reg:       r8, Val = 0x77777777 ; Reg:       r9, Val = 0x00000000 ;

Reg:      r10, Val = 0x00000001 ; Reg:      r11, Val = 0x0000002c ;

Reg:      r12, Val = 0x057d9484 ; Reg:      r13, Val = 0x00000000 ;

Reg:      r14, Val = 0x00000000 ; Reg:      r15, Val = 0x02000000 ;

Reg:      r16, Val = 0xe2be5f00 ; Reg:      r17, Val = 0x00000000 ;

Reg:      r18, Val = 0x00000000 ; Reg:      r19, Val = 0x00000000 ;

Reg:      r20, Val = 0x024c10f8 ; Reg:      r21, Val = 0x057d9244 ;

Reg:      r22, Val = 0x00002000 ; Reg:      r23, Val = 0x0000002c ;

Reg:      r24, Val = 0x00000002 ; Reg:      r25, Val = 0x24000024 ;

Reg:      r26, Val = 0x00000000 ; Reg:      r27, Val = 0x057d9484 ;

Reg:      r28, Val = 0x0000002c ; Reg:      r29, Val = 0x00000000 ;

Reg:      r30, Val = 0x0000002c ; Reg:      r31, Val = 0x00000000 ;

Reg:       cr, Val = 0x84000028 ; Reg:      nip, Val = 0x057d9550 ;

Reg:      xer, Val = 0x00000000 ; Reg:       lr, Val = 0x0186eff0 ;

Reg:      ctr, Val = 0x682f7344 ; Reg:      msr, Val = 0x00784b5c ;

Reg:     trap, Val = 0x0000b030 ; Reg:      dar, Val = 0x77777777 ;

Reg:    dsisr, Val = 0x40000000 ; Reg:   result, Val = 0x00020300 ;

Dump stack (total 1024 bytes, 16 bytes/line):

0xe2be5ea0: 02 be 5e c0 24 00 00 24 00 00 00 00 05 7d 94 84

0xe2be5eb0: 00 00 00 04 00 00 00 00 00 00 00 28 05 8d 34 c4

0xe2be5ec0: 02 be 60 a0 01 86 ef f0 00 00 00 00 00 00 00 00

0xe2be5ed0: 02 04 05 b4 00 00 00 00 00 00 00 00 00 00 00 00

0xe2be5ee0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

0xe2be5ef0: 95 47 73 35 00 00 00 00 00 00 00 00 00 00 00 00

0xe2be5f00: a0 e1 64 21 00 00 00 00 00 00 00 00 00 00 00 00

0xe2be5f10: 00 00 00 00 00 00 00 00 00 00 00 00 01 e9 00 00

0xe2be5f20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

0xe2be5f30: 00 00 00 00 00 00 00 00 02 be 66 c0 02 be 66 d0

0xe2be5f40: 02 be 61 e0 00 00 00 02 00 00 00 00 02 44 b3 a4

0xe2be5f50: 02 be 5f 90 00 00 00 08 02 be 5f e0 00 00 00 08

0xe2be5f60: 02 be 5f 80 00 ac 1b 14 00 00 00 00 00 00 00 00

0xe2be5f70: 05 b4 5f 90 02 be 5f e0 00 00 00 30 02 be 5f e0

0xe2be5f80: 02 be 5f c0 00 ac 1b f4 00 00 00 00 02 45 00 00

0xe2be5f90: 00 03 00 00 00 00 00 00 02 be 5f e0 00 00 00 30

0xe2be5fa0: 02 be 5f c0 00 ac 1b 14 61 f1 2e ae 02 45 00 00

0xe2be5fb0: 02 44 b3 74 02 be 5f d0 00 00 00 30 02 be 5f e0

0xe2be5fc0: 02 be 60 60 01 74 ff f8 00 00 00 00 00 00 08 00

0xe2be5fd0: 02 be 5f f0 00 e8 93 7e 02 be 5f f8 02 be 5f fc

0xe2be5fe0: 00 00 00 00 00 00 00 00 00 00 00 00 02 be 60 18

0xe2be5ff0: 02 be 60 10 00 e9 65 98 00 00 00 58 00 00 2a 4f

0xe2be6000: 02 be 60 10 00 00 00 00 00 00 00 00 02 be 60 68

0xe2be6010: 02 be 60 40 00 e8 c6 a0 00 00 11 17 00 00 00 00

0xe2be6020: 02 be 60 40 00 00 00 00 00 00 00 00 02 be 60 98

0xe2be6030: 02 27 00 00 00 00 00 00 00 00 00 00 02 be 60 68

0xe2be6040: 02 be 60 60 00 00 00 01 00 00 b0 30 02 be 60 98

0xe2be6050: 00 00 00 04 02 21 00 00 00 00 00 00 01 e9 00 00

0xe2be6060: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

0xe2be6070: 00 00 00 00 00 00 00 00 02 be 66 c0 02 be 66 d0

0xe2be6080: 02 be 61 e0 00 00 00 02 00 00 00 00 02 be 61 70

0xe2be6090: 00 00 00 00 02 21 00 00 05 8d 34 c4 05 7d 92 44

Call trace:

Function Address = 0x8012a4b4

Function Address = 0x8017989c

Function Address = 0x80179b30

Function Address = 0x80127438

Function Address = 0x8012d734

Function Address = 0x80100a00

Function Address = 0xe0071004

Function Address = 0x8016ce0c

Function Address = 0x801223a0

Instruction dump:

41a2fe9c 812300ec 800200ec 7f890000 409efe8c 80010014 540b07b9 40a2fe80

4bfffe6c 80780290 7f64db78 4804ea35 \<807f002c\> 38800000 38a00080 3863000c

本命令显示信息的详细描述请参见 表1-2(?1665512562#_Ref318724271)。

【相关命令】

·**reset ****kernel exception**

**进程监控和维护 \-- 进程监控和维护命令 \-- display kernel reboot**

------------------------------------------------------------------------

**[display kernel reboot**]命令用来显示内核线程的重启信息。

【命令】

集中式设备：

**[display kernel reboot ***show-number***** *offset* ]  **verbose**

分布式设备－独立运行模式/集中式IRF设备：

**[display kernel reboot ***show-number***** *offset* ]  **verbose**   **slot** *slot-number* [ **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display kernel reboot ***show-number***** *offset* ]  **verbose**   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[show-number*]：需要显示的重启信息的数目，取值范围为1～20。

*[offset*]：需要显示的起始条目距最近条目的偏移，取值范围为0～19，缺省值为0。

**[verbose**]：表示显示详细信息。不指定该参数时，显示概要信息。

**[slot** *slot-number*]：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示IRF中设备的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）

**[chassis*** chassis-number ***slot** *slot-number*]：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示最近一条内核线程重启的概要信息。

\<Sysname\> display kernel reboot 1

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- Reboot record 1 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Recorded at          : 2013-05-01  11:16:00.823018

Occurred at          : 2013-05-01  11:16:00.823018

Reason               : 0x31

Thread               : comsh (TID: 16306)

Context              : thread context

Chassis              : 0

Slot                 : 0

CPU ID               : 0

Kernel module info   : module name (mrpnc) module address (0xe332a000)

                       module name (12500) module address (0xe00bd000)

\# 显示最近一条内核线程重启的详细信息。

\<Sysname\> display kernel reboot 1 verbose

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- Reboot record 1 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Recorded at          : 2013-05-01  11:16:00.823018

Occurred at          : 2013-05-01  11:16:00.823018

Reason               : 0x31

Thread               : comsh (TID: 16306)

Context              : thread context

Chassis              : 0

Slot                 : 0

CPU ID               : 0

Kernel module info   : module name (mrpnc) module address (0xe332a000)

                       module name (12500) module address (0xe00bd000)

Last 5 thread switches : migration/0 (11:16:00.823018)\--\>

                         swapper (11:16:00.833018)\--\>

                         kthreadd (11:16:00.833518)\--\>

                         swapper (11:16:00.833550)\--\>

                         disk (11:16:00.833560)

Dump stack (total 1024 bytes, 16 bytes/line):

0xe2be5ea0: 02 be 5e c0 24 00 00 24 00 00 00 00 05 7d 94 84

0xe2be5eb0: 00 00 00 04 00 00 00 00 00 00 00 28 05 8d 34 c4

0xe2be5ec0: 02 be 60 a0 01 86 ef f0 00 00 00 00 00 00 00 00

0xe2be5ed0: 02 04 05 b4 00 00 00 00 00 00 00 00 00 00 00 00

0xe2be5ee0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

0xe2be5ef0: 95 47 73 35 00 00 00 00 00 00 00 00 00 00 00 00

0xe2be5f00: a0 e1 64 21 00 00 00 00 00 00 00 00 00 00 00 00

0xe2be5f10: 00 00 00 00 00 00 00 00 00 00 00 00 01 e9 00 00

0xe2be5f20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

0xe2be5f30: 00 00 00 00 00 00 00 00 02 be 66 c0 02 be 66 d0

0xe2be5f40: 02 be 61 e0 00 00 00 02 00 00 00 00 02 44 b3 a4

0xe2be5f50: 02 be 5f 90 00 00 00 08 02 be 5f e0 00 00 00 08

0xe2be5f60: 02 be 5f 80 00 ac 1b 14 00 00 00 00 00 00 00 00

0xe2be5f70: 05 b4 5f 90 02 be 5f e0 00 00 00 30 02 be 5f e0

0xe2be5f80: 02 be 5f c0 00 ac 1b f4 00 00 00 00 02 45 00 00

0xe2be5f90: 00 03 00 00 00 00 00 00 02 be 5f e0 00 00 00 30

0xe2be5fa0: 02 be 5f c0 00 ac 1b 14 61 f1 2e ae 02 45 00 00

0xe2be5fb0: 02 44 b3 74 02 be 5f d0 00 00 00 30 02 be 5f e0

0xe2be5fc0: 02 be 60 60 01 74 ff f8 00 00 00 00 00 00 08 00

0xe2be5fd0: 02 be 5f f0 00 e8 93 7e 02 be 5f f8 02 be 5f fc

0xe2be5fe0: 00 00 00 00 00 00 00 00 00 00 00 00 02 be 60 18

0xe2be5ff0: 02 be 60 10 00 e9 65 98 00 00 00 58 00 00 2a 4f

0xe2be6000: 02 be 60 10 00 00 00 00 00 00 00 00 02 be 60 68

0xe2be6010: 02 be 60 40 00 e8 c6 a0 00 00 11 17 00 00 00 00

0xe2be6020: 02 be 60 40 00 00 00 00 00 00 00 00 02 be 60 98

0xe2be6030: 02 27 00 00 00 00 00 00 00 00 00 00 02 be 60 68

0xe2be6040: 02 be 60 60 00 00 00 01 00 00 b0 30 02 be 60 98

0xe2be6050: 00 00 00 04 02 21 00 00 00 00 00 00 01 e9 00 00

0xe2be6060: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

0xe2be6070: 00 00 00 00 00 00 00 00 02 be 66 c0 02 be 66 d0

0xe2be6080: 02 be 61 e0 00 00 00 02 00 00 00 00 02 be 61 70

0xe2be6090: 00 00 00 00 02 21 00 00 05 8d 34 c4 05 7d 92 44

Call trace:

Function Address = 0x8012a4b4

Function Address = 0x8017989c

Function Address = 0x80179b30

Function Address = 0x80127438

Function Address = 0x8012d734

Function Address = 0x80100a00

Function Address = 0xe0071004

Function Address = 0x8016ce0c

Function Address = 0x801223a0

表1-4 display kernel reboot命令显示信息描述表

字段

描述

Recorded at

内核线程重启记录到主控板上的时间点，精确到微秒

Occurred at

内核线程重启的时间，精确到微秒

Reason

内核线程重启的原因

Thread

重启的内核线程的名称和编号

Context

内核线程重启时所在的上下文环境

Chassis

运行该内核线程的设备的成员编号（仅IRF模式支持）

Slot

运行该内核线程的主控板所在的槽位号（分布式设备－独立运行模式/分布式设备－IRF模式）

运行该内核线程的设备的成员编号（集中式IRF设备）

为固定值0，无特殊意义（集中式设备）

CPU ID

重启发生时当前CPU的编号

Kernel module info

重启发生时，系统中已加载的内核模块信息。包括内核模块名和内核模块加载的内存地址

Last 5 thread switches

系统重启时，记录重启的CPU上、最近五次的内核线程切换轨迹。包括内核线程的名称和内核线程切换时间点，时间精确到微秒

Dump stack

内核线程重启时现场的堆栈信息

Call trace

内核线程重启时现场的函数调用栈信息，即每级调用函数的指令地址

No information to display

表示系统中没有内核线程重启记录

【相关命令】

·**reset ****kernel reboot**

**进程监控和维护 \-- 进程监控和维护命令 \-- display kernel starvation**

------------------------------------------------------------------------

**[display kernel starvation**]命令用来显示内核线程饿死信息。

【命令】

集中式设备：

**[display kernel starvation ***show-number***** *offset* ]  **verbose**

分布式设备－独立运行模式/集中式IRF设备：

**[display kernel starvation ***show-number***** *offset* ]  **verbose**   **slot** *slot-number* [ **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display kernel starvation ***show-number***** *offset* ]  **verbose**   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[show-number*]：需要显示的饿死信息的数目，取值范围为1～20。

*[offset*]：需要显示的起始条目距最近条目的偏移，取值范围为0～19，缺省值为0。

**[verbose**]：表示显示详细信息。不指定该参数时，显示概要信息。

**[slot** *slot-number*]：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示IRF中设备的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）

**[chassis*** chassis-number ***slot** *slot-number*]：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示最近一条内核线程饿死的概要信息。

\<Sysname\> display kernel starvation 1

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- Starvation record 1 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Description          : INFO: task comsh: 16306 blocked for more than 10 seconds.

Recorded at          : 2013-05-01  11:16:00.823018

Occurred at          : 2013-05-01  11:16:00.823018

Instruction address  : 0x4004158c

Thread               : comsh (TID: 16306)

Context              : thread context

Chassis              : 0

Slot                 : 0

CPU ID               : 0

Kernel module info   : module name (mrpnc) module address (0xe332a000)

                       module name (12500) module address (0xe00bd000)

\# 显示最近一条内核线程饿死的详细信息。

\<Sysname\> display kernel starvation 1 verbose

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- Starvation record 1 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Description          : INFO: task comsh: 16306 blocked for more than 10 seconds.

Recorded at          : 2013-05-01  11:16:00.823018

Occurred at          : 2013-05-01  11:16:00.823018

Instruction address  : 0x4004158c

Thread               : comsh (TID: 16306)

Context              : thread context

Chassis              : 0

Slot                 : 0

CPU ID               : 0

Kernel module info   : module name (mrpnc) module address (0xe332a000)

                       module name (12500) module address (0xe00bd000)

Last 5 thread switches : migration/0 (11:16:00.823018)\--\>

                         swapper (11:16:00.833018)\--\>

                         kthreadd (11:16:00.833518)\--\>

                         swapper (11:16:00.833550)\--\>

                         disk (11:16:00.833560)

Register content:

Reg:       r0, Val = 0x00000000 ; Reg:       r1, Val = 0xe2be5ea0 ;

Reg:       r2, Val = 0x00000000 ; Reg:       r3, Val = 0x77777777 ;

Reg:       r4, Val = 0x00000000 ; Reg:       r5, Val = 0x00001492 ;

Reg:       r6, Val = 0x00000000 ; Reg:       r7, Val = 0x0000ffff ;

Reg:       r8, Val = 0x77777777 ; Reg:       r9, Val = 0x00000000 ;

Reg:      r10, Val = 0x00000001 ; Reg:      r11, Val = 0x0000002c ;

Reg:      r12, Val = 0x057d9484 ; Reg:      r13, Val = 0x00000000 ;

Reg:      r14, Val = 0x00000000 ; Reg:      r15, Val = 0x02000000 ;

Reg:      r16, Val = 0xe2be5f00 ; Reg:      r17, Val = 0x00000000 ;

Reg:      r18, Val = 0x00000000 ; Reg:      r19, Val = 0x00000000 ;

Reg:      r20, Val = 0x024c10f8 ; Reg:      r21, Val = 0x057d9244 ;

Reg:      r22, Val = 0x00002000 ; Reg:      r23, Val = 0x0000002c ;

Reg:      r24, Val = 0x00000002 ; Reg:      r25, Val = 0x24000024 ;

Reg:      r26, Val = 0x00000000 ; Reg:      r27, Val = 0x057d9484 ;

Reg:      r28, Val = 0x0000002c ; Reg:      r29, Val = 0x00000000 ;

Reg:      r30, Val = 0x0000002c ; Reg:      r31, Val = 0x00000000 ;

Reg:       cr, Val = 0x84000028 ; Reg:      nip, Val = 0x057d9550 ;

Reg:      xer, Val = 0x00000000 ; Reg:       lr, Val = 0x0186eff0 ;

Reg:      ctr, Val = 0x682f7344 ; Reg:      msr, Val = 0x00784b5c ;

Reg:     trap, Val = 0x0000b030 ; Reg:      dar, Val = 0x77777777 ;

Reg:    dsisr, Val = 0x40000000 ; Reg:   result, Val = 0x00020300 ;

Dump stack (total 1024 bytes, 16 bytes/line):

0xe2be5ea0: 02 be 5e c0 24 00 00 24 00 00 00 00 05 7d 94 84

0xe2be5eb0: 00 00 00 04 00 00 00 00 00 00 00 28 05 8d 34 c4

0xe2be5ec0: 02 be 60 a0 01 86 ef f0 00 00 00 00 00 00 00 00

0xe2be5ed0: 02 04 05 b4 00 00 00 00 00 00 00 00 00 00 00 00

0xe2be5ee0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

0xe2be5ef0: 95 47 73 35 00 00 00 00 00 00 00 00 00 00 00 00

0xe2be5f00: a0 e1 64 21 00 00 00 00 00 00 00 00 00 00 00 00

0xe2be5f10: 00 00 00 00 00 00 00 00 00 00 00 00 01 e9 00 00

0xe2be5f20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

0xe2be5f30: 00 00 00 00 00 00 00 00 02 be 66 c0 02 be 66 d0

0xe2be5f40: 02 be 61 e0 00 00 00 02 00 00 00 00 02 44 b3 a4

0xe2be5f50: 02 be 5f 90 00 00 00 08 02 be 5f e0 00 00 00 08

0xe2be5f60: 02 be 5f 80 00 ac 1b 14 00 00 00 00 00 00 00 00

0xe2be5f70: 05 b4 5f 90 02 be 5f e0 00 00 00 30 02 be 5f e0

0xe2be5f80: 02 be 5f c0 00 ac 1b f4 00 00 00 00 02 45 00 00

0xe2be5f90: 00 03 00 00 00 00 00 00 02 be 5f e0 00 00 00 30

0xe2be5fa0: 02 be 5f c0 00 ac 1b 14 61 f1 2e ae 02 45 00 00

0xe2be5fb0: 02 44 b3 74 02 be 5f d0 00 00 00 30 02 be 5f e0

0xe2be5fc0: 02 be 60 60 01 74 ff f8 00 00 00 00 00 00 08 00

0xe2be5fd0: 02 be 5f f0 00 e8 93 7e 02 be 5f f8 02 be 5f fc

0xe2be5fe0: 00 00 00 00 00 00 00 00 00 00 00 00 02 be 60 18

0xe2be5ff0: 02 be 60 10 00 e9 65 98 00 00 00 58 00 00 2a 4f

0xe2be6000: 02 be 60 10 00 00 00 00 00 00 00 00 02 be 60 68

0xe2be6010: 02 be 60 40 00 e8 c6 a0 00 00 11 17 00 00 00 00

0xe2be6020: 02 be 60 40 00 00 00 00 00 00 00 00 02 be 60 98

0xe2be6030: 02 27 00 00 00 00 00 00 00 00 00 00 02 be 60 68

0xe2be6040: 02 be 60 60 00 00 00 01 00 00 b0 30 02 be 60 98

0xe2be6050: 00 00 00 04 02 21 00 00 00 00 00 00 01 e9 00 00

0xe2be6060: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

0xe2be6070: 00 00 00 00 00 00 00 00 02 be 66 c0 02 be 66 d0

0xe2be6080: 02 be 61 e0 00 00 00 02 00 00 00 00 02 be 61 70

0xe2be6090: 00 00 00 00 02 21 00 00 05 8d 34 c4 05 7d 92 44

Call trace:

Function Address = 0x8012a4b4

Function Address = 0x8017989c

Function Address = 0x80179b30

Function Address = 0x80127438

Function Address = 0x8012d734

Function Address = 0x80100a00

Function Address = 0xe0071004

Function Address = 0x8016ce0c

Function Address = 0x801223a0

Instruction dump:

41a2fe9c 812300ec 800200ec 7f890000 409efe8c 80010014 540b07b9 40a2fe80

4bfffe6c 80780290 7f64db78 4804ea35 \<807f002c\> 38800000 38a00080 3863000c

本命令显示信息的详细描述请参见 表1-2(?1665512562#_Ref318724271)。

【相关命令】

·**reset ****kernel starvation**

**进程监控和维护 \-- 进程监控和维护命令 \-- display kernel starvation configuration**

------------------------------------------------------------------------

**[display kernel starvation configuration**]命令用来显示内核线程的饿死监控参数的配置。

【命令】

集中式设备：

**[display kernel starvation configuration**]

分布式设备－独立运行模式/集中式IRF设备：

**[display kernel starvation configuration ** **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display kernel starvation configuration ** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示IRF中设备的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）

**[chassis*** chassis-number ***slot** *slot-number*]：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示内核线程饿死监控参数配置。

\<Sysname\> display kernel starvation configuration

Thread starvation detection: Enabled

Starvation timer (in seconds): 10

Threads excluded from monitoring: 1

  TID:    123   Name: co0

表1-5 display kernel starvation configuration命令显示信息描述表

字段

描述

Thread starvation detection: Enabled

内核线程饿死检测功能处于开启状态

Thread starvation detection: Disabled

内核线程饿死检测功能处于关闭状态

Starvation timer (in seconds): *n*

内核线程饿死判定周期（单位为秒）。即如果内核线程在*n*秒内一直不能运行，则判定为饿死

Threads excluded from monitoring

不进行饿死检测的内核线程列表

Name

不进行饿死检测的内核线程的名称

TID

不进行饿死检测的内核线程的编号

【相关命令】

·**monitor kernel starvation**** enable**

·**monitor kernel starvation**** exclude-thread**

·**monitor kernel starvation**** time**

**进程监控和维护 \-- 进程监控和维护命令 \-- display process**

------------------------------------------------------------------------

**[display** **process**]命令用来显示进程的状态信息。

【命令】

集中式设备：

**[display**[ **process** [ **all** \| **job** *job-id* \| **name** *process-name* ]]]

分布式设备－独立运行模式/集中式IRF设备：

**[display**[ **process** [ **all** \| **job** *job-id* \| **name** *process-name* ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display**[ **process** [ **all** \| **job** *job-id* \| **name** *process-name* ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[all**]：显示所有进程的状态信息。指定**all**参数和不指定任何可选参数时，命令行的执行效果相同。

**[job ***job-id*]：任务编号，用于唯一标识一个进程，该编号不会随着进程的重启而改变，取值范围为1～2147483647。

**[name*** process-name*]：进程名称，为1～15个字符的字符串，不区分大小写，不能包含问号和空格。

**[slot** *slot-number*]：表示单板所在的槽位号，不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，表示主设备。（集中式IRF设备）（支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示进程scmd的状态信息。

\<Sysname\> display process name scmd

                             Job ID: 1

                                PID: 1

                         Parent JID: 0

                         Parent PID: 0

                    Executable path: -

                           Instance: 0

                            Respawn: OFF

                      Respawn count: 1

             Max. spawns per minute: 0

                       Last started: Wed Jun  1 14:45:46 2013

                      Process state: sleeping

                          Max. core: 0

                               ARGS: -

    TID  LAST_CPU    Stack      PRI    State   HH:MM:SS:MESC  Name

      1      0          0K      120      S     0:0:5:220      scmd

表1-6 display process name命令显示信息描述表

字段

描述

Job ID

任务编号，用于唯一标识一个进程，该编号不会随着进程的重启而改变

PID

进程编号，用于标识一个进程，但该编号可能会随着进程的重启而改变

Parent JID

父进程的任务编号

Parent PID

父进程的进程编号

Executable path

进程执行路径（内核线程执行路径显示为"-"）

Instance

进程的实例号（一个进程根据需要在软件实现时决定了它是否会运行多个实例）

Respawn

运行出错时，该进程是否会自动重启：

·ON表示自动重启

·OFF表示不自动重启

Respawn count

进程重启的次数（初始值为1）

Max. spawns per minute

进程一分钟内允许异常重启的最大次数（如果进程在一分钟内异常重启次数超过该值，则系统会自动关闭该进程）

Last started

进程最近一次启动的日期和时间

Process state

进程状态，可能的取值为：

·running：运行状态或正在队列中等待调度

·sleeping：可中断睡眠状态

·traced or stopped：暂停状态

·uninterruptible sleep：不可中断睡眠状态

·zombie：僵死状态（僵死状态指的是进程已经退出，但是仍然占用部分资源的状态）

Max. core

进程最多可以生成的core文件的数量，如果为0表示不生成core文件（进程异常重启一次，会产生一个core文件。如果生成的core文件的数目达到最大值，则不再生成core文件。软件开发和维护人员能够根据core文件的内容来定位异常的原因和异常的位置）

ARGS

进程启动时携带的参数。如果进程不带参数，显示为"-"

TID

线程编号

LAST_CPU

进程最近一次被调度时，所在的CPU

Stack

堆栈大小

PRI

线程优先级

State

线程状态，可能的取值为：

·R：running，运行状态或正在队列中等待调度

·S：sleeping，可中断睡眠状态

·T：traced or stopped，暂停状态

·D：uninterruptible sleep，不可中断睡眠状态

·Z：zombie，僵死状态

HH:MM:SS:MESC

进程最近一次启动后的运行时间

Name

进程名称

\# 显示所有进程的状态信息。

\<Sysname\> display process all

    JID    PID %CPU %MEM STAT PRI     TTY HH:MM:SS COMMAND

      1      1  0.0  0.0   S  120      -  00:00:04 scmd

      2      2  0.0  0.0   S  115      -  00:00:00 [kthreadd]

      3      3  0.0  0.0   S   99      -  00:00:00 [migration/0]

      4      4  0.0  0.0   S  115      -  00:00:05 [ksoftirqd/0]

      5      5  0.0  0.0   S   99      -  00:00:00 [watchdog/0]

      6      6  0.0  0.0   S  115      -  00:00:00 [events/0]

      7      7  0.0  0.0   S  115      -  00:00:00 [khelper]

      8      8  0.0  0.0   S  115      -  00:00:00 [kblockd/0]

      9      9  0.0  0.0   S  115      -  00:00:00 [ata/0]

     10     10  0.0  0.0   S  115      -  00:00:00 [ata_aux]

     11     11  0.0  0.0   S  115      -  00:00:00 [kseriod]

     12     12  0.0  0.0   S  120      -  00:00:00 [vzmond]

     13     13  0.0  0.0   S  120      -  00:00:00 [pdflush]

     14     14  0.0  0.0   S  120      -  00:00:00 [pdflush]

     15     15  0.0  0.0   S  115      -  00:00:00 [kswapd0]

     16     16  0.0  0.0   S  115      -  00:00:00 [aio/0]

     17     17  0.0  0.0   S  115      -  00:00:00 [scsi_eh_0]

     18     18  0.0  0.0   S  115      -  00:00:00 [scsi_eh_1]

     19     19  0.0  0.0   S  115      -  00:00:00 [scsi_eh_2]

     35     35  0.0  0.0   D  100      -  00:00:00 [lipc_topology]

\-\-\-- More \-\-\--              

表1-7 display process all命令显示信息描述

字段

描述

JID

任务编号，用于唯一标识一个进程，该编号不会随着进程的重启而改变

PID

进程编号

%CPU

CPU使用率（用百分比表示）

%MEM

内存使用率（用百分比表示）

STAT

进程状态，可能的取值为：

·R：running，运行状态或处于运行队列

·S：sleeping，可中断睡眠状态

·T：traced or stopped，暂停状态

·D：uninterruptible sleep，不可中断睡眠状态

·Z：zombie，僵死状态

PRI

进程优先级（优先级在进程调度时发挥作用，优先级高的会优先得到调度）

TTY

进程使用的终端（在非缺省MDC内该项总显示为"-"）

HH:MM:SS

进程最近一次启动后的运行时间

COMMAND

进程名称以及进程运行的参数（如果进程名称带有"  "标记，则表示内核线程）

**进程监控和维护 \-- 进程监控和维护命令 \-- display process cpu**

------------------------------------------------------------------------

**[display** **process cpu**]命令用来显示所有进程的CPU使用率信息。

【命令】

集中式设备：

**[display** **process** **cpu**]

分布式设备－独立运行模式/集中式IRF设备：

**[display** **process** **cpu** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display** **process** **cpu** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot** *slot-number*]：表示单板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，表示主设备。（集中式IRF设备）（支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示所有进程CPU使用率信息。

\<Sysname\> display process cpu

CPU utilization in 5 secs: 16.8%; 1 min: 4.7%; 5 mins: 4.7%

    JID      5Sec      1Min      5Min    Name

      1      0.0%      0.0%      0.0%    scmd

      2      0.0%      0.0%      0.0%    [kthreadd]

      3      0.1%      0.0%      0.0%    [ksoftirqd/0]

      4      0.0%      0.0%      0.0%    [watchdog/0]

      5      0.0%      0.0%      0.0%    [events/0]

      6      0.0%      0.0%      0.0%    [khelper]

     29      0.0%      0.0%      0.0%    [kblockd/0]

     49      0.0%      0.0%      0.0%    [vzmond]

     52      0.0%      0.0%      0.0%    [pdflush]

     53      0.0%      0.0%      0.0%    [pdflush]

     54      0.0%      0.0%      0.0%    [kswapd0]

    110      0.0%      0.0%      0.0%    [aio/0]

    712      0.0%      0.0%      0.0%    [mtdblockd]

    719      0.0%      0.0%      0.0%    [TNetJob]

    720      0.0%      0.0%      0.0%    [TMTH]

    727      0.0%      0.0%      0.0%    [CF]

    730      0.0%      0.0%      0.0%    [DIBC]

    752      0.0%      0.0%      0.0%    [lipc_topology]

    762      0.0%      0.0%      0.0%    [MNET]

    763      0.0%      0.0%      0.0%    [SYSM]

\-\-\-- More \-\-\--

表1-8 display process cpu 命令显示信息描述表

字段

描述

CPU utilization in 5 secs: 16.8%; 1 min: 4.7%; 5 mins: 4.7%

系统最近5秒CPU使用率；最近1分钟CPU使用率；最近5分钟CPU使用率

JID

任务编号（用于唯一标识一个进程，该编号不会随着进程的重启而改变）

5Sec

最近5秒钟内进程的CPU使用率

1Min

最近1分钟内进程的CPU使用率

5Min

最近5分钟内进程的CPU使用率

Name

进程名称（如果进程名称带有"  "标记，则表示该进程为内核线程）

**进程监控和维护 \-- 进程监控和维护命令 \-- display process log**

------------------------------------------------------------------------

**[display** **process log**]命令用来显示所有用户态进程的日志信息。

【命令】

集中式设备：

**[display** **process** **log**]

分布式设备－独立运行模式/集中式IRF设备：

**[display** **process** **log** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display** **process** **log** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot** *slot-number*]：表示单板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，表示主设备。（集中式IRF设备）（支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示所有用户态进程的日志信息。

\<Sysname\> display process log

Name          JID    PID    Abort Core Start-time          End-time

mdcd          135    135    N     N    2013-06-11 09:31:00 2013-06-11 09:31:00

knotify       156    156    N     N    2013-06-11 09:31:02 2013-06-11 09:31:02

knotify       158    158    N     N    2013-06-11 09:31:02 2013-06-11 09:31:02

knotify       195    195    N     N    2013-06-11 09:31:03 2013-06-11 09:31:03

pkg_update    203    203    N     N    2013-06-11 09:31:06 2013-06-11 09:31:06

autocfgd      219    219    N     N    2013-06-11 09:31:13 2013-06-11 09:31:13

comsh         202    202    N     N    2013-06-11 09:31:05 2013-06-11 09:31:13

表1-9 display process log命令显示信息描述表

字段

描述

Name

用户态进程名

JID

用户态进程任务编号

PID

用户态进程编号

Abort

是否异常退出：

·Y表示异常退出

·N表示正常退出

Core

是否产生core文件

·Y表示产生

·N表示未产生

Start-time

用户态进程创建时间

End-time

用户态进程结束时间

**进程监控和维护 \-- 进程监控和维护命令 \-- display process memory**

------------------------------------------------------------------------

**[display** **process memory**]命令用来显示所有用户态进程的代码段、数据段以及堆栈等的内存使用信息。

【命令】

集中式设备：

**[display** **process** **memory**]

分布式设备－独立运行模式/集中式IRF设备：

**[display** **process** **memory** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display** **process** **memory** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot** *slot-number*]：表示单板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，表示主设备。（集中式IRF设备）（支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

用户态进程启动时，会向系统申请Text、Data、Stack和Dynamic类型的内存。

·Text类型的内存用来存放用户态进程的代码。

·Data类型的内存用来存放用户态进程的数据。

·Stack内存指的是栈内存，一般存放临时数据。

·Dynamic类型的内存指的是堆内存（heap），由系统根据用户态进程运行需要进行动态分配（malloc）和释放（free），可使用**display process memory heap**命令显示Dynamic类型内存的详细信息。

【举例】

\# 显示所有用户态进程的内存使用信息。

\<Sysname\> display process memory

   JID       Text      Data      Stack    Dynamic    Name

     1        384      1800         16         36    scmd

     2          0         0          0          0    [kthreadd]

     3          0         0          0          0    [ksoftirqd/0]

     4          0         0          0          0    [watchdog/0]

     5          0         0          0          0    [events/0]

     6          0         0          0          0    [khelper]

    29          0         0          0          0    [kblockd/0]

    49          0         0          0          0    [vzmond]

    52          0         0          0          0    [pdflush]

\-\-\-- More \-\-\--

表1-10 display process memory命令显示信息描述表

字段

描述

JID

任务编号。用于唯一标识一个用户态进程，该编号不会随着用户态进程的重启而改变

Text

用户态进程占用的代码段大小，单位为KB（内核线程该项大小为0）

Data

用户态进程占用的数据段大小，单位为KB（内核线程该项大小为0）

Stack

用户态进程占用的堆栈大小，单位为KB（内核线程该项大小为0）

Dynamic

用户态进程动态申请内存大小，单位为KB（内核线程该项大小为0）

Name

用户态进程名称（如果用户态进程名称带有"  "标记，则表示该进程为内核线程）

【相关命令】

·**display process memory heap**

·**display process memory heap address**

·**display process memory heap size**

**进程监控和维护 \-- 进程监控和维护命令 \-- display process memory heap**

------------------------------------------------------------------------

**[display process memory heap**]命令用来显示指定用户态进程的堆内存统计信息。

【命令】

集中式设备：

**[display process memory heap job ***job-id* [ **verbose** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display process memory heap job ***job-id * **verbose** ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display process memory heap job ***job-id * **verbose** ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[job ***job-id*]：任务编号，用于唯一标识一个用户态进程，该编号不会随着用户态进程的重启而改变。取值范围为1～2147483647。

**[verbose**]**：**显示内存详细统计信息。不指定该参数时，显示内存概要统计信息。

**[slot** *slot-number*]：表示单板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，表示主设备。（集中式IRF设备）（支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

系统的堆内存由固定大小（比如size=16字节、size=64字节等）的内存块构成，用于存放用户态进程运行过程中需要用到的数据或者中间变量。当用户态进程启动时，系统会根据用户态进程运行需要，给用户态进程动态分配堆内存。用户态进程的堆内存信息可使用**display process memory heap**命令显示。

每个内存块都有地址，该地址用十六进制数表示，可通过**display process memory heap size**命令显示。用户使用内存块的地址可以访问内存块，获取内存块的内容，内存块的内容可通过**display process memory heap address**命令显示。

【举例】

\# 显示job 148的堆内存概要统计信息。

\<Sysname\> display process memory heap job 148

Total virtual memory heap space(in bytes) :  2228224

Total physical memory heap space(in bytes) :  262144

Total allocated memory(in bytes)          :  161576

\# 显示job 148的堆内存详细统计信息。

\<Sysname\> display process memory heap job 148 verbose

Heap usage:

Size       Free      Used     Total     Free Ratio

16         8         52       60        13%

64         3         1262     1265      0.2%

128        2         207      209       1%

512        3         55       58        5.1%

4096       3         297      300       1%

8192       1         19       20        5%

81920      0         1        1         0%

Summary:

Total virtual memory heap space (in bytes)  :  2293760

Total physical memory heap space (in bytes) :  58368

Total allocated memory (in bytes)           :  42368

以上显示信息表明：job 148分得size大小16字节的内存块60个（已用52个，还有8个未使用），size大小为64字节的内存块1265个（已用1262个，还有3个未使用），以此类推。

表1-11 display process memory heap命令显示信息描述表

命令字

功能描述

Total virtual memory heap space(in bytes)

虚拟堆内存总大小，单位为字节

Total physical memory heap space(in bytes)

物理堆内存总大小，单位为字节

Total allocated memory(in bytes)

任务已使用的堆内存大小，单位为字节

Size

内存块大小，单位为字节

Free

空闲的内存块个数

Used

已使用的内存块个数

Total

指定大小内存块总个数，为Free和Used之和

Free Ratio

Free与Total的比率，可以反映这种大小内存块的碎片情况

【相关命令】

·**display process memory**

·**display process memory heap address**

·**display process memory heap size**

**进程监控和维护 \-- 进程监控和维护命令 \-- display process memory heap address**

------------------------------------------------------------------------

**[display process memory heap address**]命令用来显示从指定地址开始的内存空间的内容。

【命令】

集中式设备：

**[display process memory heap** **job** *job-id* **address** *starting-address* **length** *memory-length*]

分布式设备－独立运行模式/集中式IRF设备：

**[display process memory heap** **job** *job-id* **address** *starting-address* **length** *memory-length* [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display process memory heap** **job** *job-id* **address** *starting-address* **length** *memory-length* [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[job ***job-id*]：任务编号，用于唯一标识一个用户态进程，该编号不会随着用户态进程的重启而改变，取值范围为1～2147483647。

**[address ***starting-address*]：内存块的起始地址。

**[length*** memory-length*]：内存的长度，取值范围为1～1024，单位为字节。

**[slot** *slot-number*]：表示单板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，表示主设备。（集中式IRF设备）（支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

当用户态进程运行异常时，使用该命令可以帮助设备维护人员诊断和定位问题。

【举例】

\# 显示job 1从地址0xb7e30580开始，长度为128字节的内存空间的内容。

\<Sysname\> display process memory heap job 1 address b7e30580 length 128

[B7E30580:  14 00 EF FF 00 00 00 00 E4 39 E2 B7 7C 05 E3 B7  \...\...\...9..\|\...    ]

B7E30590:  14 00 EF FF 2F 73 62 69 6E 2F 73 6C 62 67 64 00  \..../sbin/slbgd.   

B7E305A0:  14 00 EF FF 00 00 00 00 44 3B E2 B7 8C 05 E3 B7  \...\.....D;\...\...   

B7E305B0:  14 00 EF FF 2F 73 62 69 6E 2F 6F 73 70 66 64 00  \..../sbin/ospfd.   

B7E305C0:  14 00 EF FF 00 00 00 00 A4 3C E2 B7 AC 05 E3 B7  \...\...\...\<\...\...   

B7E305D0:  14 00 EF FF 2F 73 62 69 6E 2F 6D 73 74 70 64 00  \..../sbin/mstpd.   

B7E305E0:  14 00 EF FF 00 00 00 00 04 3E E2 B7 CC 05 E3 B7  \...\...\...\>\...\...   

B7E305F0:  14 00 EF FF 2F 73 62 69 6E 2F 6E 74 70 64 00 00  \..../sbin/ntpd..

【相关命令】

·**display process memory heap**

·**display process memory heap size**

**进程监控和维护 \-- 进程监控和维护命令 \-- display process memory heap size**

------------------------------------------------------------------------

**[display process memory heap size**]命令用来显示指定大小已使用内存块的地址。

【命令】

集中式设备：

**[display process memory heap job** *job-id* **size** *memory-size* [ **offset** *offset-size* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display process memory heap** **job** *job-id* **size** *memory-size* [ **offset** *offset-size*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display process memory heap** **job** *job-id* **size** *memory-size* [ **offset** *offset-size*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[job ***job-id*]：任务编号，用于唯一标识一个用户态进程，该编号不会随着用户态进程的重启而改变，取值范围为1～2147483647。

**[size** memory-size]：内存块大小，取值范围为1～4294967295。

**[offset*** offset-size*]：要查询的内存块的偏移，取值范围为0～4294967295，缺省值为128。比如，系统给job 1分配了size为16字节的内存块100个，用户态进程当前已用了66个，如果执行命令**display process memory heap** **job** *1* **size** *16* **offset** *50*，则会显示该用户态进程第51到第66个size为16字节的内存块的地址。

**[slot** *slot-number*]：表示单板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，表示主设备。（集中式IRF设备）（支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

该命令显示的地址为十六进制格式，使用该地址，通过**display process memory heap address**命令可以显示该地址内存的具体内容。

【举例】

\# 显示job 1已使用的size大小为16字节的内存块的地址。

\<Sysname\> display process memory heap job 1 size 16

0xb7e300c0  0xb7e300d0  0xb7e300e0  0xb7e300f0

0xb7e30100  0xb7e30110  0xb7e30120  0xb7e30130

0xb7e30140  0xb7e30150  0xb7e30160  0xb7e30170

0xb7e30180  0xb7e30190  0xb7e301a0  0xb7e301b0

0xb7e301c0  0xb7e301d0  0xb7e301e0  0xb7e301f0

0xb7e30200  0xb7e30210  0xb7e30220  0xb7e30230

\# 显示job 1已使用的size大小为16字节的内存块的地址，从第5个已使用内存块开始显示。

\<Sysname\> display process memory heap job 1 size 16 offset 4

0xb7e30100  0xb7e30110  0xb7e30120  0xb7e30130

0xb7e30140  0xb7e30150  0xb7e30160  0xb7e30170

0xb7e30180  0xb7e30190  0xb7e301a0  0xb7e301b0

0xb7e301c0  0xb7e301d0  0xb7e301e0  0xb7e301f0

0xb7e30200  0xb7e30210  0xb7e30220  0xb7e30230

【相关命令】

·**display process memory heap**

·**display process memory heap address**

**进程监控和维护 \-- 进程监控和维护命令 \-- exception filepath**

------------------------------------------------------------------------

**[exception filepath**]命令用来设置core文件的保存路径。

**[undo exception filepath**]命令用来将core文件的保存路径设置为空。

【命令】

**[exception filepath ***directory*]

**[undo exception filepath** *directory*]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[directory*]：表示core文件的保存路径，只能为存储介质的根目录。

【使用指导】

本命令配置成功后，设备会将生成的core文件存放到当前主用主控板上、指定存储介质根目录下的core文件夹下。如果存储介质根目录下没有core文件夹，则会先创建core文件夹，再保存core文件。

当主控板上有多块存储介质的时候，可使用该命令修改core文件的保存路径。

需要注意的是，当core文件的保存路径为空或无法正常访问时，系统将无法保存core文件。

【举例】

\# 设置core文件的保存路径。

\<Sysname\> exception filepath flash:/

【相关命令】

·**display exception filepath**

·**process core**

**进程监控和维护 \-- 进程监控和维护命令 \-- monitor kernel deadloop enable**

------------------------------------------------------------------------

**[monitor kernel deadloop enable**]命令用来开启内核线程死循环检测功能。

**[undo monitor kernel deadloop enable**]命令用来关闭内核线程死循环检测功能。

【命令】

集中式设备：

**[monitor kernel deadloop enable**]

**[undo monitor kernel deadloop enable**]

分布式设备－独立运行模式/集中式IRF设备：

**[monitor kernel deadloop enable** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[undo monitor kernel deadloop enable** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[monitor kernel deadloop enable ** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

**[undo monitor kernel deadloop enable ** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

【参数】

**[slot** *slot-number*]：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示IRF中设备的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）

**[chassis*** chassis-number ***slot** *slot-number*]：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

在内核态空间中，所有资源都是共享的，多个内核线程之间通过任务调度协调工作。如果某个内核线程长时间一直占用CPU，就会导致其它内核线程获取不到运行机会，整个系统挂死，我们称这种现象为死循环。

开启内核线程死循环检测功能后，如果系统发现某内核线程在指定时间内一直占用CPU，则判定该内核线程为死循环。系统会记录一条死循环信息供管理员查询，并自动重启整个系统来解除死循环。

开机后，系统会自动检测内核线程是否发生了死循环，建议用户不要随意配置该命令。如果确实需要配置，请在H3C工程师的指导下进行，以免引起系统异常。

【举例】

\# 开启内核线程死循环检测功能。

\<Sysname\> system-view

Sysname monitor kernel deadloop enable

【相关命令】

·**display kernel****deadloop**

·**display kernel****deadloop configuration**

·**monitor kernel deadloop exclude-thread**

·**monitor kernel deadloop time**

**进程监控和维护 \-- 进程监控和维护命令 \-- monitor kernel deadloop exclude-thread**

------------------------------------------------------------------------

**[monitor kernel deadloop exclude-thread**]命令用来配置不检测指定内核线程是否发生了死循环。

**[undo monitor kernel deadloop exclude-thread**]命令用来恢复对指定内核线程是否发生了死循环进行检测。

【命令】

集中式设备：

**[monitor kernel deadloop exclude-thread*** tid*]

**[undo monitor kernel deadloop exclude-thread**** *tid* ]

分布式设备－独立运行模式/集中式IRF设备：

**[monitor kernel deadloop exclude-thread*** tid* [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[undo monitor kernel deadloop exclude-thread**** *tid* ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[monitor kernel deadloop exclude-thread*** tid***** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

**[undo monitor kernel deadloop exclude-thread**** *tid* ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]

【缺省情况】

开启内核线程死循环检测功能后，系统会监控所有内核线程是否发生了死循环。

【视图】

系统视图

【缺省用户角色】

network-admin

【参数】

*[tid*]：表示内核线程编号，用于唯一标识一个内核线程，取值范围为1～2147483647。不指定该参数时，表示恢复到缺省情况。

**[slot** *slot-number*]：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示IRF中设备的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）

**[chassis*** chassis-number ***slot** *slot-number*]：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

缺省情况下，系统会检测所有内核线程是否发生了死循环。多次执行该命令，可以配置对多个内核线程不进行检测，最多可以配置128个。

开机后，系统会自动检测内核线程是否发生了死循环，建议用户不要随意配置该命令。如果确实需要配置，请在H3C工程师的指导下进行，以免引起系统异常。

【举例】

\# 对编号为15的内核线程不进行死循环检测。

\<Sysname\> system-view

Sysnamemonitor kernel deadloop exclude-thread 15

【相关命令】

·**display ****kernel deadloop configuration**

·**display**** kernel deadloop**

·**monitor ****kernel deadloop enable**

·**monitor ****kernel deadloop time**

**进程监控和维护 \-- 进程监控和维护命令 \-- monitor kernel deadloop time**

------------------------------------------------------------------------

**[monitor kernel deadloop time**]命令用来配置判定内核线程是否死循环的时长。

**[undo monitor kernel deadloop time**]命令用来恢复缺省情况。

【命令】

集中式设备：

**[monitor kernel deadloop time*** interval*]

**[undo monitor kernel deadloop time**]

分布式设备－独立运行模式/集中式IRF设备：

**[monitor kernel deadloop time ***interval***** **slot** *slot-number*  **cpu** *cpu-number*  ]

**[undo monitor kernel deadloop time**** **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[monitor kernel deadloop time ***interval***** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

**[undo monitor kernel deadloop time**** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

【缺省情况】

当某内核线程连续运行超过8秒钟，则判定为死循环。

【视图】

系统视图

【缺省用户角色】

network-admin

【参数】

**[time*** interval*]：表示内核线程死循环判定时长，取值范围为1～65535，单位为秒。

**[slot** *slot-number*]：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示IRF中设备的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）

**[chassis*** chassis-number ***slot** *slot-number*]：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

开启内核线程检测功能后，如果某内核线程持续运行指定时间，则认为该内核线程已经死循环，系统将记录一条死循环信息并重启。

开机后，系统会自动检测内核线程是否发生了死循环，建议用户不要随意配置该命令。如果确实需要配置，请在H3C工程师的指导下进行，以免引起系统异常。

【举例】

\# 配置当某内核线程连续运行超过8秒钟，则判定为死循环。

\<Sysname\> system-view

Sysname monitor kernel deadloop time 8

【相关命令】

·**display ****kernel deadloop configuration**

·**display ****kernel deadloop**

·**monitor ****kernel deadloop enable**

·**monitor ****kernel deadloop exclude-thread**

**进程监控和维护 \-- 进程监控和维护命令 \-- monitor kernel starvation enable**

------------------------------------------------------------------------

**[monitor kernel starvation enable**]命令用来开启内核线程饿死检测功能。

**[undo monitor kernel starvation enable**]命令用来关闭内核线程饿死检测功能。

【命令】

集中式设备：

**[monitor kernel starvation enable**]

**[undo monitor kernel starvation enable**]

分布式设备－独立运行模式/集中式IRF设备：

**[monitor kernel starvation enable ** **slot** *slot-number*  **cpu** *cpu-number*  ]

**[undo monitor kernel starvation enable ** **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[monitor kernel starvation enable ** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

**[undo monitor kernel starvation enable ** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

【缺省情况】

内核线程饿死检测功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

【参数】

**[slot** *slot-number*]：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示IRF中设备的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）

**[chassis*** chassis-number ***slot** *slot-number*]：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

如果内核线程本身的触发条件没有达到，会导致该内核线程在一段时间内一直得不到调度，我们称这种现象为饿死。

开启内核线程饿死检测功能后，当系统检测到某内核线程饿死时，会记录一条饿死信息供管理员查询。

内核线程饿死并不会影响整个系统的运行，当触发条件达到，处于饿死状态的内核线程会自动执行。

开机后，系统会自动检测内核线程是否发生了饿死，建议用户不要随意配置该命令。如果确实需要配置，请在H3C工程师的指导下进行，以免引起系统异常。

【举例】

\# 开启内核线程饿死检测功能。

\<Sysname\> system-view

Sysname monitor kernel starvation enable

【相关命令】

·**display ****kernel starvation configuration**

·**display ****kernel starvation**

·**monitor ****kernel starvation time**

·**monitor ****kernel starvation exclude-thread**

**进程监控和维护 \-- 进程监控和维护命令 \-- monitor kernel starvation exclude-thread**

------------------------------------------------------------------------

**[monitor kernel starvation exclude-thread**]命令用来配置不检测指定内核线程是否发生了饿死。

**[undo monitor kernel starvation exclude-thread**]命令用来恢复对指定内核线程是否发生了饿死进行检测。

【命令】

集中式设备：

**[monitor kernel starvation exclude-thread*** tid*]

**[undo monitor kernel starvation exclude-thread**** *tid* ]

分布式设备－独立运行模式/集中式IRF设备：

**[monitor kernel starvation exclude-thread*** tid* [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[undo monitor kernel starvation exclude-thread**** *tid* ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[monitor kernel starvation exclude-thread*** tid ***** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

**[undo monitor kernel starvation exclude-thread**** *tid* ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]

【缺省情况】

开启内核线程死循环检测功能后，会监控所有内核线程是否发生了饿死。

【视图】

系统视图

【缺省用户角色】

network-admin

【参数】

*[tid*]：表示内核线程编号，用于唯一标识一个内核线程，取值范围为1～2147483647。不指定该参数时，表示恢复到缺省情况。

**[slot** *slot-number*]：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示IRF中设备的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）

**[chassis*** chassis-number ***slot** *slot-number*]：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

缺省情况下，系统会检测所有内核线程是否发生了饿死。多次执行该命令，可以配置对多个内核线程不进行检测，最多可以配置128个。

开机后，系统会自动检测内核线程是否发生了饿死，建议用户不要随意配置该命令。如果确实需要配置，请在H3C工程师的指导下进行，以免引起系统异常。

【举例】

\# 对编号为15的内核线程不进行饿死检测。

\<Sysname\> system-view

Sysname monitor kernel starvation exclude-thread 15

【相关命令】

·**display kernel****starvation**

·**display kernel****starvation configuration**

·**monitor kernel starvation**** time**

·**monitor kernel starvation**** enable**

**进程监控和维护 \-- 进程监控和维护命令 \-- monitor kernel starvation time**

------------------------------------------------------------------------

**[monitor kernel starvation time**]命令用来配置判定内核线程是否饿死的时长。

**[undo monitor kernel starvation time**]命令用来恢复缺省情况。

【命令】

集中式设备：

**[monitor kernel starvation** **time** *interval* ]

**[undo monitor kernel starvation time**]

分布式设备－独立运行模式/集中式IRF设备：

**[monitor kernel starvation time*** interval***** **slot** *slot-number*  **cpu** *cpu-number*  ]

**[undo monitor kernel starvation time ** **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[monitor kernel starvation time*** interval***** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

**[undo monitor kernel starvation time** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【缺省情况】

当某内核线程在120秒内一直没有运行，则认为该内核线程被饿死。

【视图】

系统视图

【缺省用户角色】

network-admin

【参数】

**[time ***interval*]：表示内核线程饿死判定时长，取值范围为1～65535，单位为秒。

**[slot** *slot-number*]：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示IRF中设备的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）

**[chassis*** chassis-number ***slot** *slot-number*]：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

开机后，系统会自动检测内核线程是否发生了饿死，建议用户不要随意配置该命令。如果确实需要配置，请在H3C工程师的指导下进行，以免引起系统异常。

【举例】

\# 配置当内核线程在120秒内一直没有运行，则认为该内核线程被饿死。

\<Sysname\> system-view

Sysname monitor kernel starvation time 120

【相关命令】

·**display kernel****starvation**

·**display kernel****starvation configuration**

·**monitor kernel starvation****enable**

·**monitor kernel starvation****exclude-thread**

**进程监控和维护 \-- 进程监控和维护命令 \-- monitor process**

------------------------------------------------------------------------

**[monitor process**]命令用来显示进程的统计信息。

【命令】

集中式设备：

**[monitor process** [ **dumbtty**   **iteration** *number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[monitor** **process** [ **dumbtty**   **iteration** *number*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[monitor** **process** [ **dumbtty**   **iteration** *number*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[dumbtty**]：以哑终端方式显示进程统计信息（即屏幕不支持定时刷新统计信息）。指定该参数时，全部进程的统计信息以CPU使用率降序排列输出到屏幕上；不指定该参数时，统计信息以交互模式显示，缺省情况下按CPU占用率降序显示前10个进程的统计信息，且每隔5秒刷新一次。

**[iteration** *number*]：表示进程统计信息的显示次数，取值范围为1～4294967295。指定**dumbtty**参数时，*number*的缺省值为1；不指定**dumbtty**且不配置*number*参数时，表示显示次数没有限制，统计信息会每隔5秒刷新一次，一直显示。

**[slot** *slot-number*]：表示单板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，表示主设备。（集中式IRF设备）（支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

不指定**dumbtty**参数的情况下，统计信息以交互模式显示。

·交互模式下，系统会自动计算可显示的进程个数，超过屏幕范围的不显示。

·交互模式下，用户可通过输入表1-12(?-1251975530#_Ref282593064)中指定的交互命令字来执行相应的操作。

表1-12 monitor process命令支持的交互命令字描述表

命令字

功能描述

?或h

帮助信息，显示可用的交互式命令字

1

各物理CPU状态的显示开关。比如：

(1)输入1，分别显示各物理CPU的参数值

(2)再次输入1，显示所有CPU的参数的平均值

(3)第三次输入1，又分别显示各物理CPU的参数值

(4)如此循环

缺省情况下，显示所有CPU的参数的平均值

c

按CPU占用率降序排列，缺省情况下采用降序排列

d

设置统计信息的更新时间间隔，取值范围为1～2147483647秒，缺省值为5秒

f

按进程打开的文件句柄数降序排列

k

终止一个任务，此命令会影响系统运行，请谨慎使用

l

刷新屏幕

m

按进程使用内存大小降序排列

n

改变显示的进程个数，取值范围为0～2147483647（缺省值为10个，0表示不作限制）；超过屏幕范围时，仍只显示一屏内可容纳的进程个数

q

退出交互模式

t

按进程最近一次启动后的运行时间降序排列

\<

排序项向左移动一列

\>

排序项向右移动一列

【举例】

\# 以哑终端方式显示进程统计信息。（使用该方式显示时，系统会一次显示所有进程的统计信息，并且不支持定时刷新，显示完毕后，会退回到命令视图）

\<Sysname\> monitor process dumbtty

 76 processes; 103 threads; 687 fds

Thread states: 1 running, 102 sleeping, 0 stopped, 0 zombie

CPU states: 77.16% idle, 0.00% user, 14.96% kernel, 7.87% interrupt

Memory: 496M total, 341M available, page size 4K

    JID    PID  PRI  State  FDs    MEM  HH:MM:SS    CPU   Name

   1047   1047  120    R     9   1420K  00:02:23  13.53%  diagd

      1      1  120    S    17   1092K  00:00:20   7.61%  scmd

   1000   1000  115    S     0      0K  00:00:09   0.84%  [sock/1]

   1026   1026  120    S    20  26044K  00:00:05   0.84%  syslogd

      2      2  115    S     0      0K  00:00:00   0.00%  [kthreadd]

      3      3   99    S     0      0K  00:00:00   0.00%  [migration/0]

      4      4  115    S     0      0K  00:00:06   0.00%  [ksoftirqd/0]

      5      5   99    S     0      0K  00:00:00   0.00%  [watchdog/0]

      6      6  115    S     0      0K  00:00:01   0.00%  [events/0]

      7      7  115    S     0      0K  00:00:00   0.00%  [khelper]

   4797   4797  120    S     8  28832K  00:00:02   0.00%  comsh

   5117   5117  120    S     8   1496K  00:00:00   0.00%  top

\<Sysname\>

\# 以哑终端方式显示进程统计信息，并且执行一次命令显示两次统计结果。

\<Sysname\> monitor process dumbtty iteration 2

76 processes; 103 threads; 687 fds

Thread states: 1 running, 102 sleeping, 0 stopped, 0 zombie

CPU states: 44.84% idle, 0.51% user, 39.17% kernel, 15.46% interrupt

Memory: 496M total, 341M available, page size 4K

    JID    PID  PRI  State  FDs    MEM  HH:MM:SS    CPU   Name

   1047   1047  120    R     9   1420K  00:02:30  37.11%  diagd

      1      1  120    S    17   1092K  00:00:21  11.34%  scmd

   1000   1000  115    S     0      0K  00:00:09   2.06%  [sock/1]

   1026   1026  120    S    20  26044K  00:00:05   1.54%  syslogd

   1027   1027  120    S    12   9280K  00:01:12   1.03%  devd

      4      4  115    S     0      0K  00:00:06   0.51%  [ksoftirqd/0]

   1009   1009  115    S     0      0K  00:00:08   0.51%  [karp/1]

   1010   1010  115    S     0      0K  00:00:13   0.51%  [kND/1]

   5373   5373  120    S     8   1496K  00:00:00   0.51%  top

      2      2  115    S     0      0K  00:00:00   0.00%  [kthreadd]

      3      3   99    S     0      0K  00:00:00   0.00%  [migration/0]

      5      5   99    S     0      0K  00:00:00   0.00%  [watchdog/0]

      6      6  115    S     0      0K  00:00:01   0.00%  [events/0]

      7      7  115    S     0      0K  00:00:00   0.00%  [khelper]

   4796   4796  120    S    11   2744K  00:00:00   0.00%  login

   4797   4797  120    S     8  28832K  00:00:03   0.00%  comsh

// 5秒钟后，系统会自动统计一次，并显示统计信息如下。（相当于执行了两次**monitor process dumbtty**，两次执行的时间间隔为5秒）

76 processes; 103 threads; 687 fds

Thread states: 1 running, 102 sleeping, 0 stopped, 0 zombie

CPU states: 78.71% idle, 0.16% user, 14.86% kernel, 6.25% interrupt

Memory: 496M total, 341M available, page size 4K

    JID    PID  PRI  State  FDs    MEM  HH:MM:SS    CPU   Name

   1047   1047  120    R     9   1420K  00:02:31  14.25%  diagd

      1      1  120    S    17   1092K  00:00:21   4.25%  scmd

   1027   1027  120    S    12   9280K  00:01:12   1.29%  devd

   1000   1000  115    S     0      0K  00:00:09   0.37%  [sock/1]

   5373   5373  120    S     8   1500K  00:00:00   0.37%  top

      6      6  115    S     0      0K  00:00:01   0.18%  [events/0]

   1009   1009  115    S     0      0K  00:00:08   0.18%  [karp/1]

   1010   1010  115    S     0      0K  00:00:13   0.18%  [kND/1]

   4795   4795  120    S    11   2372K  00:00:01   0.18%  telnetd

      2      2  115    S     0      0K  00:00:00   0.00%  [kthreadd]

      3      3   99    S     0      0K  00:00:00   0.00%  [migration/0]

      4      4  115    S     0      0K  00:00:06   0.00%  [ksoftirqd/0]

      5      5   99    S     0      0K  00:00:00   0.00%  [watchdog/0]

      7      7  115    S     0      0K  00:00:00   0.00%  [khelper]

   4796   4796  120    S    11   2744K  00:00:00   0.00%  login

   4797   4797  120    S     8  28832K  00:00:03   0.00%  comsh

\<Sysname\>

\# 以交互方式显示进程统计信息。

\<Sysname\> monitor process

76 processes; 103 threads; 687 fds

Thread states: 1 running, 102 sleeping, 0 stopped, 0 zombie

CPU states: 78.98% idle, 0.16% user, 14.57% kernel, 6.27% interrupt

Memory: 496M total, 341M available, page size 4K

    JID    PID  PRI  State  FDs    MEM  HH:MM:SS    CPU   Name

   1047   1047  120    R     9   1420K  00:02:39  14.13%  diagd

      1      1  120    S    17   1092K  00:00:23   3.98%  scmd

   1027   1027  120    S    12   9280K  00:01:13   1.44%  devd

   1000   1000  115    S     0      0K  00:00:09   0.36%  [sock/1]

   1009   1009  115    S     0      0K  00:00:09   0.36%  [karp/1]

      4      4  115    S     0      0K  00:00:06   0.18%  [ksoftirqd/0]

   1010   1010  115    S     0      0K  00:00:13   0.18%  [kND/1]

   4795   4795  120    S    11   2372K  00:00:01   0.18%  telnetd

   5491   5491  120    S     8   1500K  00:00:00   0.18%  top

      2      2  115    S     0      0K  00:00:00   0.00%  [kthreadd]

以上信息会每隔5秒刷新一次。

·输入"h"或"?"，将显示如下帮助信息。

Help for interactive commands:

      ?,h    Show the available interactive commands

        1    Toggle SMP view: \'1\' single/separate states

        c    Sort by the CPU field(default)

        d    Set the delay interval between screen updates

        f    Sort by number of open files

        k    Kill a job

        l    Refresh the screen

        m    Sort by memory used

        n    Set the maximum number of processes to display

        q    Quit the interactive display

        t    Sort by run time of processes since last restart

        \<    Move sort field to the next left column

        \>    Move sort field to the next right column

Press any key to continue

·输入"d"后，根据出现的提示如果输入"3"，则统计信息将会每隔3秒更新一次。

Enter the delay interval between updates(1\~2147483647)：3

·输入"n"后，根据出现的提示如果输入"5"，则显示的进程数目将会变为5个。

Enter the max number of procs to display(0 is unlimited)：5

87 processes; 113 threads; 735 fds

Thread states: 2 running, 111 sleeping, 0 stopped, 0 zombie

CPU states: 86.57% idle, 0.83% user, 11.74% kernel, 0.83% interrupt

Memory: 755M total, 414M available, page size 4K

    JID    PID  PRI  State  FDs    MEM  HH:MM:SS    CPU   Name

    864    864  120    S    24  27020K  00:00:43   8.95%  syslogd

   1173   1173  120    R    24   2664K  00:00:01   2.37%  top

    866    866  120    S    18  10276K  00:00:09   0.69%  devd

      1      1  120    S    16   1968K  00:00:04   0.41%  scmd

    881    881  120    S     8   2420K  00:00:07   0.41%  diagd

·输入"f"，统计信息将以打开的文件句柄数降序输出（c、m、t命令字类似）。

87 processes; 113 threads; 735 fds

Thread states: 1 running, 112 sleeping, 0 stopped, 0 zombie

CPU states: 90.66% idle, 0.88% user, 5.77% kernel, 2.66% interrupt

Memory: 755M total, 414M available, page size 4K

    JID    PID  PRI  State  FDs    MEM  HH:MM:SS    CPU   Name

    862    862  120    S    61   5384K  00:00:01   0.00%  dbmd

    905    905  120    S    35   2464K  00:00:02   0.00%  ipbased

    863    863  120    S    31   1956K  00:00:00   0.00%  had

    884    884  120    S    31  30600K  00:00:00   0.00%  lsmd

    889    889  120    S    29  61592K  00:00:00   0.00%  routed

·输入"k"后，根据出现的提示如果输入884，将会终止此JID对应的任务"lsmd"。

Enter the JID to kill: 884

84 processes; 107 threads; 683 fds

Thread states: 1 running, 106 sleeping, 0 stopped, 0 zombie

CPU states: 59.03% idle, 1.92% user, 37.88% kernel, 1.15% interrupt

Memory: 755M total, 419M available, page size 4K

    JID    PID  PRI  State  FDs    MEM  HH:MM:SS    CPU   Name

    862    862  120    S    56   5384K  00:00:01   0.00%  dbmd

    905    905  120    S    35   2464K  00:00:02   0.00%  ipbased

    863    863  120    S    30   1956K  00:00:00   0.00%  had

    889    889  120    S    29  61592K  00:00:00   0.00%  routed

   1160   1160  120    S    28  23096K  00:00:01   0.19%  sshd

·输入"q"，将退出交互模式。

表1-13 monitor process命令显示信息描述表

字段

描述

84 processes; 107 threads; 683 fds

系统的进程总数，线程总数，文件句柄总数

Thread states: 1 running, 102 sleeping, 0 stopped, 0 zombie

线程状态：处于running状态的线程数，处于sleeping（包括interruptible sleep和uninterruptible sleep）状态的线程数，处于stopped状态的线程数，处于zombie状态的线程数

CPU states

CPU状态：空闲率，用户态占用率，内核态占用率，中断占用率

Memory

内存状态：总量，可用内存数，page大小，单位为KB

JID

任务编号（用于唯一标识一个进程，该编号不会随着进程的重启而改变）

PID

进程编号

PRI

进程优先级

State

进程状态，可能的取值为：

·R：running，运行状态或处于运行队列

·S：sleeping，可中断睡眠状态

·T：traced or stopped，暂停状态

·D：uninterruptible sleep，不可中断睡眠状态

·Z：zombie，僵死状态

FDs

file descriptions，进程打开的文件句柄数

MEM

进程所使用的内存大小（内核线程该项显示为0）

HH:MM:SS

进程自最近一次启动以来的运行时间

CPU

进程CPU使用率

Name

进程名称（如果进程名称带有"  "标记，则表示该进程为内核线程）

**进程监控和维护 \-- 进程监控和维护命令 \-- monitor thread**

------------------------------------------------------------------------

**[monitor thread**]命令用来显示线程的统计信息。

【命令】

集中式设备：

**[monitor thread** [ **dumbtty**   **iteration** *number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[monitor** **thread** [ **dumbtty**   **iteration** *number*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[monitor** **thread** [ **dumbtty**   **iteration** *number*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[dumbtty**]：以哑终端方式显示线程统计信息（即屏幕不支持定时刷新统计信息）。指定该参数时，全部线程的统计信息以CPU使用率降序排列输出到屏幕上。不指定该参数时，统计信息以交互模式显示，缺省情况下按CPU占用率降序显示前10个线程的统计信息，且每隔5秒更新一次。

**[iteration** *number*]：进程统计信息的显示次数，取值范围为1～4294967295。指定**dumbtty**参数时*number*的缺省值为1；不指定**dumbtty**且不配置*number*参数时*，*表示显示次数没有限制，统计信息会一直显示。

**[slot** *slot-number*]：表示单板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，表示主设备。（集中式IRF设备）（支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

不指定**dumbtty**参数的情况下，统计信息以交互模式显示。

·交互模式下，系统会自动计算可显示的线程个数，超过屏幕范围的不作显示。

·交互模式下，用户可通过输入表1-14(?-1366243004#_Ref282593016)中指定的交互命令字来执行相应的操作。

表1-14 monitor thread命令支持的交互命令字描述表

命令字

功能描述

?或h

帮助信息，显示可用的交互式命令字

d

设置统计信息的更新时间间隔，缺省值为5秒

k

终止一个任务（进程），此命令会影响系统运行，请谨慎使用

l

刷新屏幕

n

改变显示的线程个数，取值为0\~2147483647（缺省值为10个，0表示不作限制）；超过屏幕范围时，仍只显示一屏内可容纳的线程个数

q

退出交互模式

\<

排序项向左移动一列

\>

排序项向右移动一列

【举例】

\# 以哑终端方式显示线程统计信息。

\<Sysname\> monitor thread dumbtty

84 processes; 107 threads

Thread states: 1 running, 106 sleeping, 0 stopped, 0 zombie

CPU states: 83.19% idle, 1.68% user, 10.08% kernel, 5.04% interrupt

Memory: 755M total, 417M available, page size 4K

    JID    TID  LAST_CPU  PRI  State  HH:MM:SS   MAX    CPU    Name

   1175   1175      0     120    R    00:00:00     1  10.75%   top

      1      1      0     120    S    00:00:06     1   2.68%   scmd

    881    881      0     120    S    00:00:09     1   2.01%   diagd

    776    776      0     120    S    00:00:01     0   0.67%   [DEVD]

    866    866      0     120    S    00:00:11     1   0.67%   devd

      2      2      0     115    S    00:00:00     0   0.00%   [kthreadd]

      3      3      0     115    S    00:00:01     0   0.00%   [ksoftirqd/0]

      4      4      0      99    S    00:00:00     1   0.00%   [watchdog/0]

      5      5      0     115    S    00:00:00     0   0.00%   [events/0]

      6      6      0     115    S    00:00:00     0   0.00%   [khelper]

    796    796      0     115    S    00:00:00     0   0.00%   [kip6fs/1]

\<Sysname\>

\# 以交互模式显示线程统计信息。

\<Sysname\> monitor thread

84 processes; 107 threads

Thread states: 1 running, 106 sleeping, 0 stopped, 0 zombie

CPU states: 94.43% idle, 0.76% user, 3.64% kernel, 1.15% interrupt

Memory: 755M total, 417M available, page size 4K

    JID    TID  LAST_CPU  PRI  State  HH:MM:SS   MAX    CPU    Name

   1176   1176      0     120    R    00:00:01     1   3.42%   top

    866    866      0     120    S    00:00:12     1   0.85%   devd

    881    881      0     120    S    00:00:09     1   0.64%   diagd

      1      1      0     120    S    00:00:06     1   0.42%   scmd

   1160   1160      0     120    S    00:00:01     1   0.21%   sshd

      2      2      0     115    S    00:00:00     0   0.00%   [kthreadd]

      3      3      0     115    S    00:00:01     0   0.00%   [ksoftirqd/0]

      4      4      0      99    S    00:00:00     1   0.00%   [watchdog/0]

      5      5      0     115    S    00:00:00     0   0.00%   [events/0]

      6      6      0     115    S    00:00:00     0   0.00%   [khelper]

·输入"h"或"?"，帮助信息显示如下：

Help for interactive commands：

        ?,h      Show the available interactive commands

          c      Sort by the CPU field(default)

          d      Set the delay interval between screen updates

          k      Kill a job

          l      Refresh the screen

          n      Set the maximum number of threads to display

          q      Quit the interactive display

          t      Sort by run time of threads since last restart

          \<      Move sort field to the next left column

          \>      Move sort field to the next right column

Press any key to continue

·输入"d"后，根据出现的提示如果输入"3"，统计信息将会每隔3秒更新一次。

Enter the delay interval between screen updates（1\~2147483647）：3

·输入"n"后，根据出现的提示如果输入"5"，显示的线程数目将会变为5个。

Enter the max number of threads to display(0 means unlimited)：5

84 processes; 107 threads

Thread states: 1 running, 106 sleeping, 0 stopped, 0 zombie

CPU states: 93.26% idle, 0.99% user, 4.23% kernel, 1.49% interrupt

Memory: 755M total, 417M available, page size 4K

    JID    TID  LAST_CPU  PRI  State  HH:MM:SS   MAX    CPU    Name

   1176   1176      0     120    R    00:00:02     1   3.71%   top

      1      1      0     120    S    00:00:06     1   0.92%   scmd

    866    866      0     120    S    00:00:13     1   0.69%   devd

    881    881      0     120    S    00:00:10     1   0.69%   diagd

    720    720      0     115    D    00:00:01     0   0.23%   [TMTH]

·输入"k"后，根据出现的提示输入881，将会终止此JID对应的任务diagd。

Enter the JID to kill：881

83 processes; 106 threads

Thread states: 1 running, 105 sleeping, 0 stopped, 0 zombie

CPU states: 96.26% idle, 0.54% user, 2.63% kernel, 0.54% interrupt

Memory: 755M total, 418M available, page size 4K

    JID    TID  LAST_CPU  PRI  State  HH:MM:SS   MAX    CPU    Name

   1176   1176      0     120    R    00:00:04     1   1.86%   top

    866    866      0     120    S    00:00:14     1   0.87%   devd

      1      1      0     120    S    00:00:07     1   0.49%   scmd

    730    730      0       0    S    00:00:04     1   0.12%   [DIBC]

    762    762      0     120    S    00:00:22     1   0.12%   [MNET]

·输入"q"，将退出交互模式。

表1-15 monitor thread命令显示信息描述表

显示项

内容描述

84 processes; 107 threads

系统的进程总数，线程总数

Thread states

线程状态：处于running状态的线程数，处于sleeping（包括interruptible sleep和uninterruptible sleep）状态的线程数，处于stopped状态的线程数，处于zombie状态的线程数

CPU states

CPU状态：空闲率，用户态占用率，内核态占用率，中断占用率

Memory

内存状态：总量，可用内存数，page大小

JID

任务编号，用于唯一标识一个进程，该编号不会随着进程的重启而改变

TID

线程编号

LAST_CPU

线程最近一次被调度所在的CPU的编号

PRI

线程优先级

State

进程状态，可能的取值为：

·R：running，运行状态或处于运行队列

·S：sleeping，可中断睡眠状态

·T：traced or stopped，暂停状态

·D：uninterruptible sleep，不可中断睡眠状态

·Z：zombie，僵死状态

HH:MM:SS

线程自最近一次启动以来的运行时间

MAX

线程单次调度占用CPU的最长时间，以毫秒为单位

CPU

线程CPU使用率

Name

线程名称（如果线程名称带有"  "标记，则表示该线程为内核线程）

**进程监控和维护 \-- 进程监控和维护命令 \-- process core**

------------------------------------------------------------------------

**[process** **core**]命令用来开启/关闭用户态进程异常时的生成core文件的功能，以及配置能生成的core文件的最大个数。

【命令】

集中式设备：

**[process**[ **core** { **maxcore** *value* \| **off** } { **job** *job-id \|* **name** *process-name* }]]

分布式设备－独立运行模式/集中式IRF设备：

**[process**[ **core** { **maxcore** *value* \| **off** } { **job** *job-id* \| **name** *process-name* } [ **slot** *slot-number* [ **cpu** *cpu-number* ] ]]]

分布式设备－IRF模式：

**[process**[ **core** { **maxcore** *value* \| **off** } { **job** *job-id* \| **name** *process-name* } [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ] ]]]

【视图】

用户视图

【缺省情况】

同一用户态进程在首次异常时会生成core文件，后续异常不再生成core文件。即**maxcore**的最大数值为1。

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[off**]：表示关闭用户态进程异常时生成core文件的功能。

**[maxcore** *value*]：表示开启用户态进程的core文件生成功能，并配置能生成的core文件的最大个数。*value*表示用户态进程能生成的core文件的最大个数，取值范围为1～10，缺省值为1。

**[name** *process-name*]：用户态进程的名称，为1～15个字符的字符串，不区分大小写。**process core**命令的配置对用户态进程下的所有实例有效。

**[job*** job-id*]：任务ID，用于唯一标识一个进程，该ID不会随着进程的重启而改变，取值范围为1～2147483647。

**[slot** *slot-number*]：表示单板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，表示主设备。（集中式IRF设备）（支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

开启用户态进程的core文件生成功能，并配置能生成的core文件的最大个数后，用户态进程异常重启一次，就会产生一个core文件并记录用户态进程的异常信息。如果生成的core文件的数目达到最大值，则不再生成新的core文件。软件开发和维护人员能够根据core文件的内容来定位异常的原因和异常的位置。

因为生成的core文件会占用系统存储资源，如果用户对某些用户态进程的异常退出不关心，可以关闭这些用户态进程的core文件记录功能。

【举例】

\# 关闭用户态进程routed的core文件生成功能。

\<Sysname\> process core off name routed

\# 开启用户态进程routed的core文件生成功能，并且最多可生成5个core文件。

\<Sysname\> process core maxcore 5 name routed

【相关命令】

·**display ****exception context**

·**exception filepath**

**进程监控和维护 \-- 进程监控和维护命令 \-- reset exception context**

------------------------------------------------------------------------

**[reset exception context**]命令用来清除用户态进程异常时记录的上下文信息。

【命令】

集中式设备：

**[reset exception context**]

分布式设备－独立运行模式/集中式IRF设备：

**[reset** **exception context** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[reset exception context** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示IRF中设备的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）

**[chassis*** chassis-number ***slot** *slot-number*]：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 清除用户态进程异常记录。

\<Sysname\> reset exception context

【相关命令】

·**display exception context**

**进程监控和维护 \-- 进程监控和维护命令 \-- reset kernel deadloop**

------------------------------------------------------------------------

**[reset kernel deadloop**]命令用来清除内核线程死循环信息。

【命令】

集中式设备：

**[reset kernel deadloop**]

分布式设备－独立运行模式/集中式IRF设备：

**[reset kernel deadloop ** **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[reset kernel deadloop ** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

**[slot** *slot-number*]：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示IRF中设备的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）

**[chassis*** chassis-number ***slot** *slot-number*]：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 清除内核线程死循环信息。

\<Sysname\> reset kernel deadloop

【相关命令】

·**display kernel****deadloop**

**进程监控和维护 \-- 进程监控和维护命令 \-- reset kernel exception**

------------------------------------------------------------------------

**[reset kernel exception**]命令用来清除内核线程的异常信息。

【命令】

集中式设备：

**[reset kernel exception**]

分布式设备－独立运行模式/集中式IRF设备：

**[reset kernel exception ** **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[reset kernel exception ** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

**[slot** *slot-number*]：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示IRF中设备的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）

**[chassis*** chassis-number ***slot** *slot-number*]：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 清除内核线程的异常信息。

\<Sysname\> reset kernel exception

【相关命令】

·**display**** kernel exception**

**进程监控和维护 \-- 进程监控和维护命令 \-- reset kernel reboot**

------------------------------------------------------------------------

**[reset kernel reboot**]命令用来清除内核线程重启信息。

【命令】

集中式设备：

**[reset kernel reboot**]

分布式设备－独立运行模式/集中式IRF设备：

**[reset kernel reboot ** **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[reset kernel reboot ** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

**[slot** *slot-number*]：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示IRF中设备的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）

**[chassis*** chassis-number ***slot** *slot-number*]：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 清除内核线程重启信息。

\<Sysname\> reset kernel reboot

【相关命令】

·**display ****kernel reboot**

**进程监控和维护 \-- 进程监控和维护命令 \-- reset kernel starvation**

------------------------------------------------------------------------

**[reset kernel starvation**]命令用来清除内核线程饿死信息。

【命令】

集中式设备：

**[reset kernel starvation**]

分布式设备－独立运行模式/集中式IRF设备：

**[reset kernel starvation ** **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[reset kernel starvation ** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

**[slot** *slot-number*]：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示IRF中设备的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）

**[chassis*** chassis-number ***slot** *slot-number*]：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 清除内核线程饿死信息。

\<Sysname\> reset kernel starvation

【相关命令】

·**display ****kernel starvation**
