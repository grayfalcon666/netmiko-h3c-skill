::: {#991488430 .myid}
[]{#_Toc404797186}[]{#struct_0_x1063_20800_x108916724}

**进程监控和维护 \-- 进程监控和维护命令 \-- display exception context**

------------------------------------------------------------------------

[**[display exception context]{lang="EN-US"}**]{#struct_0_x1063_20800_x1300440325}[命令用来显示用户态进程异常时的上下文信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x67553468}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1063_20800_x16132909}

[**[display exception context ]{lang="EN-US"}**[\[ **count** *value* \]]{lang="EN-US"}]{#struct_0_x1063_20800_1555624111}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1063_20800_653283939}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **exception context** \[ **count** *value* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_x108457972}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1063_20800_x198947016}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **exception context** \[ **count** *value* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_x1365730522}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x317296662}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1063_20800_1987427115}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1143985342}

[[network-admin]{lang="EN-US"}]{#struct_0_x1063_20800_1691739362}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1063_20800_x1370472750}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x108523508}

[**[count]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x1063_20800_x504922968}[：表示上下文信息的显示个数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x854849394}[：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_801710929}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中设备的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x412266735}[：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1063_20800_1826294159}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x430523602}

[[当用户态进程发生一次异常，系统会生成一个]{style="font-family:宋体"}[core]{lang="EN-US"}]{#struct_0_x1063_20800_1768380175}[文件，还会生成一条上下文信息，用于记录异常用户态进程的]{style="font-family:宋体"}[ID]{lang="EN-US"}[、生成]{style="font-family:宋体"}[core]{lang="EN-US"}[文件的时间、]{style="font-family:宋体"}[core]{lang="EN-US"}[文件存放的位置、栈信息和寄存器信息。一个]{style="font-family:宋体"}[core]{lang="EN-US"}[文件对应一条上下文信息，最多可记录的上下文信息数和可记录的]{style="font-family:宋体"}[core]{lang="EN-US"}[文件数目相同。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1726764015}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_x108982261}[显示在]{style="font-family:宋体"}[x86]{lang="EN-US"}[体系]{style="font-family:宋体"}[32]{lang="EN-US"}[位设备上的异常上下文信息。]{style="font-family:宋体"}

[[\<Sysname\> display exception context]{lang="EN-US"}]{#struct_0_x1063_20800_148782014}

[Index 1 of 1]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Crashed PID: 120 (routed)]{lang="EN-US"}

[Crash signal: SIGBUS]{lang="EN-US"}

[Crash time: Tue Apr  9 17:14:30 2013]{lang="EN-US"}

[Core file path:]{lang="EN-US"}

[flash:/core/node0_routed_120_7_20130409-171430_1365527670.core]{lang="EN-US"}

[#0  0xb7caba4a]{lang="EN-US"}

[#1  0x0804cb79]{lang="EN-US"}

[#2  0xb7cd77c4]{lang="EN-US"}

[#3  0x08049f45]{lang="EN-US"}

[Backtrace stopped.]{lang="EN-US"}

[                          Registers\' content]{lang="EN-US"}

[  eax:0xfffffffc   ebx:0x00000003   ecx:0xbfe244ec   edx:0x0000000a]{lang="EN-US"}

[  esp:0xbfe244b8   ebp:0xbfe244c8   esi:0xffffffff   edi:0xbfe24674]{lang="EN-US"}

[  eip:0xb7caba4a eflag:0x00000292    cs:0x00000073    ss:0x0000007b]{lang="EN-US"}

[   ds:0x0000007b    es:0x0000007b    fs:0x00000000    gs:0x00000033]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_1137888722}[显示在]{style="font-family:宋体"}[x86]{lang="EN-US"}[体系]{style="font-family:宋体"}[64]{lang="EN-US"}[位设备上的异常上下文信息。]{style="font-family:宋体"}

[[\<Sysname\> display exception context]{lang="EN-US"}]{#struct_0_x1063_20800_x1014017400}

[Index 1 of 1]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Crashed PID: 121 (routed)]{lang="EN-US"}

[Crash signal: SIGBUS]{lang="EN-US"}

[Crash time: Sun Mar 31 11:12:21 2013]{lang="EN-US"}

[Core file path:]{lang="EN-US"}

[flash:/core/node0_routed_121_7_20130331-111221_1364728341.core]{lang="EN-US"}

[#0  0x00007fae7dbad20c]{lang="EN-US"}

[#1  0x00000000004059fa]{lang="EN-US"}

[#2  0x00007fae7dbd96c0]{lang="EN-US"}

[#3  0x0000000000402b29]{lang="EN-US"}

[Backtrace stopped.]{lang="EN-US"}

[                          Registers\' content]{lang="EN-US"}

[       rax:0xfffffffffffffffc       rbx:0x00007fff88a5dd10]{lang="EN-US"}

[       rcx:0xffffffffffffffff       rdx:0x000000000000000a]{lang="EN-US"}

[       rsi:0x00007fff88a5dd10       rdi:0x0000000000000003]{lang="EN-US"}

[       rbp:0x00007fff88a5dcf0       rsp:0x00007fff88a5dcf0]{lang="EN-US"}

[        r8:0x00007fae7ea587e0        r9:0x0000000000000079]{lang="EN-US"}

[       r10:0xffffffffffffffff       r11:0x0000000000000246]{lang="EN-US"}

[       r12:0x0000000000405b18       r13:0x00007fff88a5ff7a]{lang="EN-US"}

[       r14:0x00007fff88a5de30       r15:0x0000000000000000]{lang="EN-US"}

[       rip:0x00007fae7dbad20c      flag:0x0000000000000246]{lang="EN-US"}

[        cs:0x0000000000000033        ss:0x000000000000002b]{lang="EN-US"}

[        ds:0x0000000000000000        es:0x0000000000000000]{lang="EN-US"}

[        fs:0x0000000000000000        gs:0x0000000000000000]{lang="EN-US"}

[   fs_base:0x00007fae80a5d6a0   gs_base:0x0000000000000000]{lang="EN-US"}

[   orig_ax:0x00000000000000e8]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_x1550549221}[显示在]{style="font-family:宋体"}[powerpc]{lang="EN-US"}[体系]{style="font-family:宋体"}[32]{lang="EN-US"}[位设备上的异常上下文信息。]{style="font-family:宋体"}

[[\<Sysname\> display exception context]{lang="EN-US"}]{#struct_0_x1063_20800_x1820520918}

[Index 1 of 1]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Crashed PID: 133 (routed)]{lang="EN-US"}

[Crash signal: SIGBUS]{lang="EN-US"}

[Crash time: Wed Apr 10 15:47:49 2013]{lang="EN-US"}

[Core file path:]{lang="EN-US"}

[flash:/core/node0_routed_133_7_20130410-154749_1365608869.core]{lang="EN-US"}

[#0  0x184720bc]{lang="EN-US"}

[#1  0x10006b4c]{lang="EN-US"}

[Backtrace stopped.]{lang="EN-US"}

[                          Registers\' content]{lang="EN-US"}

[grp00: 0x000000ee 0x7ffd6ad0 0x1800f440 0x00000004]{lang="EN-US"}

[grp04: 0x7ffd6af8 0x0000000a 0xffffffff 0x184720bc]{lang="EN-US"}

[grp08: 0x0002d200 0x00000003 0x00000001 0x1847209c]{lang="EN-US"}

[grp12: 0x10006b4c 0x10020534 0xd6744100 0x00000000]{lang="EN-US"}

[grp16: 0x00000000 0xa0203ff0 0xa028b12c 0xa028b13c]{lang="EN-US"}

[grp20: 0xa028b148 0xa028b168 0xa028b178 0xa028b190]{lang="EN-US"}

[grp24: 0xa028b1a8 0xa028b1b8 0x00000000 0x7ffd6c08]{lang="EN-US"}

[grp28: 0x10006cac 0x7ffd6f92 0x184c1b84 0x7ffd6ae0]{lang="EN-US"}

[ ]{lang="EN-US"}

[  nip:0x184720bc    lr:0x10006b4c    cr:0x38000022   ctr:0x1847209c]{lang="EN-US"}

[  msr:0x0002db00   xer:0x00000000   ret:0xfffffffc dsisr:0x08000000]{lang="EN-US"}

[  gr3:0x00000003    mq:0x00000000  trap:0x00000c00   dar:0x1833114c]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_852316963}[显示在]{style="font-family:宋体"}[powerpc]{lang="EN-US"}[体系]{style="font-family:宋体"}[64]{lang="EN-US"}[位设备上的异常上下文信息。]{style="font-family:宋体"}

[[\<Sysname\> display exception context]{lang="EN-US"}]{#struct_0_x1063_20800_1311646964}

[Index 1 of 1]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Crashed PID: 172 (routed)]{lang="EN-US"}

[Crash signal: SIGBUS]{lang="EN-US"}

[Crash time: Sat Sep 15 16:53:16 2007]{lang="EN-US"}

[Core file path:]{lang="EN-US"}

[cfa0:/core/node1_routed_172_7_20070915-165316_1189875196.core]{lang="EN-US"}

[#0  0x00000fff803c66b4]{lang="EN-US"}

[#1  0x0000000010009b94]{lang="EN-US"}

[#2  0x00000fff80401814]{lang="EN-US"}

[Backtrace stopped.]{lang="EN-US"}

[                          Registers\' content]{lang="EN-US"}

[     grp00: 0x00000000000000ee 0x00000fffffd04840]{lang="EN-US"}

[     grp02: 0x00000fff80425c28 0x0000000000000004]{lang="EN-US"}

[     grp04: 0x00000fffffd048c0 0x000000000000000a]{lang="EN-US"}

[     grp06: 0xffffffffffffffff 0x00000fff803c66b4]{lang="EN-US"}

[     grp08: 0x000000008002d000 0x0000000000000000]{lang="EN-US"}

[     grp10: 0x0000000000000000 0x0000000000000000]{lang="EN-US"}

[     grp12: 0x0000000000000000 0x00000fff80a096b0]{lang="EN-US"}

[     grp14: 0x000000007b964c00 0x000000007b7d0000]{lang="EN-US"}

[     grp16: 0x0000000000000001 0x000000000000000b]{lang="EN-US"}

[     grp18: 0x0000000000000031 0x0000000000a205b8]{lang="EN-US"}

[     grp20: 0x0000000000a20677 0x0000000000000000]{lang="EN-US"}

[     grp22: 0x000000007bb91014 0x0000000000000000]{lang="EN-US"}

[     grp24: 0xc0000000005ae1c8 0x0000000000000000]{lang="EN-US"}

[     grp26: 0xc0000001f00bff20 0xc0000001f00b0000]{lang="EN-US"}

[     grp28: 0x00000fffffd04a30 0x000000001001aed8]{lang="EN-US"}

[     grp30: 0x00000fffffd04fae 0x00000fffffd04840]{lang="EN-US"}

[ ]{lang="EN-US"}

[       nip:0x00000fff803c66b4        lr:0x0000000010009b94]{lang="EN-US"}

[        cr:0x0000000058000482       ctr:0x00000fff803c66ac]{lang="EN-US"}

[       msr:0x000000008002d000       xer:0x0000000000000000]{lang="EN-US"}

[       ret:0xfffffffffffffffc     dsisr:0x0000000000000000]{lang="EN-US"}

[       gr3:0x0000000000000003     softe:0x0000000000000001]{lang="EN-US"}

[      trap:0x0000000000000c00       dar:0x00000fff8059d14c]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_82016076}[显示在]{style="font-family:宋体"}[mips]{lang="EN-US"}[体系]{style="font-family:宋体"}[32]{lang="EN-US"}[位设备上的异常上下文信息。]{style="font-family:宋体"}

[[\<Sysname\> display exception context]{lang="EN-US"}]{#struct_0_x1063_20800_552132077}

[Index 1 of 1]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Crashed PID: 182 (routed)]{lang="EN-US"}

[Crash signal: SIGBUS]{lang="EN-US"}

[Crash time: Sun Jan  2 08:11:38 2013]{lang="EN-US"}

[Core file path:]{lang="EN-US"}

[flash:/core/node4_routed_182_10_20130102-081138_1293955898.core]{lang="EN-US"}

[#0  0x2af2faf4]{lang="EN-US"}

[#1  0x00406d8c]{lang="EN-US"}

[Backtrace stopped.]{lang="EN-US"}

[                          Registers\' content]{lang="EN-US"}

[ zero:0x00000000   at:0x1000dc00   v0:0x00000004   v1:0x00000003]{lang="EN-US"}

[   a0:0x00000003   a1:0x7fd267e8   a2:0x0000000a   a3:0x00000001]{lang="EN-US"}

[   t0:0x00000000   t1:0xcf08fa14   t2:0x80230510   t3:0xfffffff8]{lang="EN-US"}

[   t4:0x69766520   t5:0x00000000   t6:0x63cc6000   t7:0x44617461]{lang="EN-US"}

[   s0:0x7fd26f81   s1:0x00401948   s2:0x7fd268f8   s3:0x803e1db0]{lang="EN-US"}

[   s4:0x803e1da0   s5:0x803e1d88   s6:0x803e1d70   s7:0x803e1d60]{lang="EN-US"}

[   t8:0x00000008   t9:0x2af2fae0   k0:0x00000000   k1:0x00000000]{lang="EN-US"}

[   gp:0x2af9a3a0   sp:0x7fd267c0   s8:0x7fd267c0   ra:0x00406d8c]{lang="EN-US"}

[   sr:0x0000dc13   lo:0xef9db265   hi:0x0000003f  bad:0x2add2010]{lang="EN-US"}

[cause:0x00800020   pc:0x2af2faf4]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_117354283}[显示在]{style="font-family:宋体"}[mips]{lang="EN-US"}[体系]{style="font-family:宋体"}[64]{lang="EN-US"}[位设备上的异常上下文信息。]{style="font-family:宋体"}

[[\<Sysname\> display exception context]{lang="EN-US"}]{#struct_0_x1063_20800_x1464290558}

[Index 1 of 1]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Crashed PID: 270 (routed)]{lang="EN-US"}

[Crash signal: SIGBUS]{lang="EN-US"}

[Crash time: Wed Mar 27 12:39:12 2013]{lang="EN-US"}

[Core file path:]{lang="EN-US"}

[flash:/core/node16_routed_270_10_20130327-123912_1364387952.core]{lang="EN-US"}

[#0  0x0000005555a3bcb4]{lang="EN-US"}

[#1  0x0000000120006c1c]{lang="EN-US"}

[Backtrace stopped.]{lang="EN-US"}

[                          Registers\' content]{lang="EN-US"}

[      zero:0x0000000000000000        at:0x0000000000000014]{lang="EN-US"}

[        v0:0x0000000000000004        v1:0x0000000000000003]{lang="EN-US"}

[        a0:0x0000000000000003        a1:0x000000ffff899d90]{lang="EN-US"}

[        a2:0x000000000000000a        a3:0x0000000000000001]{lang="EN-US"}

[        a4:0x0000005555a9b4e0        a5:0x0000000000000000]{lang="EN-US"}

[        a6:0xffffffff8021349c        a7:0x20696e206368616e]{lang="EN-US"}

[        t0:0x0000000000000000        t1:0xffffffff80105068]{lang="EN-US"}

[        t2:0xffffffff80213890        t3:0x0000000000000008]{lang="EN-US"}

[        s0:0x0000005555a99c40        s1:0x000000ffff89af5f]{lang="EN-US"}

[        s2:0x0000000120007320        s3:0x0000005555a5f470]{lang="EN-US"}

[        s4:0x000000ffff899f80        s5:0xffffffff803cc6c0]{lang="EN-US"}

[        s6:0xffffffff803cc6a8        s7:0xffffffff803cc690]{lang="EN-US"}

[        t8:0x0000000000000002        t9:0x0000005555a3bc98]{lang="EN-US"}

[        k0:0x0000000000000000        k1:0x0000000000000000]{lang="EN-US"}

[        gp:0x0000000120020460        sp:0x000000ffff899d70]{lang="EN-US"}

[        s8:0x000000ffff899d80        ra:0x0000000120006c1c]{lang="EN-US"}

[        sr:0x000000000400fff3        lo:0xdf3b645a1cac08c9]{lang="EN-US"}

[        hi:0x000000000000007f       bad:0x000000555589ba84]{lang="EN-US"}

[     cause:0x0000000000800020        pc:0x0000005555a3bcb4]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display exception context]{lang="EN-US"}]{#struct_0_x1063_20800_x120082956}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_223129229}[[字段]{style="font-family:黑体"}]{#struct_0_x1063_20800_917367205}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1063_20800_x2029199406}

[[Crashed PID]{lang="EN-US"}]{#struct_0_x1063_20800_x1040952859}

[[发生异常的用户态进程]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1063_20800_578665489}

[[Crash signal]{lang="EN-US"}]{#struct_0_x1063_20800_x1338558056}

[[导致异常的信号：]{style="font-family:宋体"}]{#struct_0_x1063_20800_801807991}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SIGABRT]{lang="EN-US"}]{#struct_0_x1063_20800_x1212160206}[：异常终止（]{lang="EN-US" style="font-family:宋体"}[abort]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SIGBUS]{lang="EN-US"}]{#struct_0_x1063_20800_x1892174983}[：总线错误]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SIGFPE]{lang="EN-US"}]{#struct_0_x1063_20800_x1211308238}[：浮点异常]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SIGILL]{lang="EN-US"}]{#struct_0_x1063_20800_419778972}[：程序执行了非法指令，导致异常]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SIGQUIT]{lang="EN-US"}]{#struct_0_x1063_20800_x1900926310}[：终端退出符]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SIGSEGV]{lang="EN-US"}]{#struct_0_x1063_20800_x868215555}[：无效存储访问]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SIGSYS]{lang="EN-US"}]{#struct_0_x1063_20800_x1211242702}[：无效系统调用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SIGTRAP]{lang="EN-US"}]{#struct_0_x1063_20800_x1866947681}[：跟踪断点时发生了异常]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SIGXCPU]{lang="EN-US"}]{#struct_0_x1063_20800_1237029697}[：超过]{lang="EN-US" style="font-family:宋体"}[CPU]{lang="EN-US"}[限制（]{lang="EN-US" style="font-family:宋体"}[setrlimit]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SIGXFSZ]{lang="EN-US"}]{#struct_0_x1063_20800_x1211832529}[：超过文件长度限制（]{lang="EN-US" style="font-family:宋体"}[setrlimit]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SIGUNKNOW]{lang="EN-US"}]{#struct_0_x1063_20800_x786515145}[：未知原因]{lang="EN-US" style="font-family:宋体"}

[[Crash time]{lang="EN-US"}]{#struct_0_x1063_20800_x653635860}

[[异常发生的时间]{style="font-family:宋体"}]{#struct_0_x1063_20800_x2029396014}

[[Core file path]{lang="EN-US"}]{#struct_0_x1063_20800_x543212769}

[[core]{lang="EN-US"}]{#struct_0_x1063_20800_616376175}[文件存放的位置]{style="font-family:宋体"}

[[Backtrace stopped]{lang="EN-US"}]{#struct_0_x1063_20800_214673878}

[[表示栈信息已经显示完毕]{style="font-family:宋体"}]{#struct_0_x1063_20800_x970597370}

[[Registers' content]{lang="EN-US"}]{#struct_0_x1063_20800_x2029330478}

[[寄存器的内容]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1012637039}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1138015764}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset exception context]{lang="EN-US"}**]{#struct_0_x1063_20800_2093862426}

::: {#1326980436 .myid}
[]{#_Toc404797187}[]{#struct_0_x1063_20800_x341679632}[]{#_Toc358900719}[]{#_Toc340215438}

**进程监控和维护 \-- 进程监控和维护命令 \-- display exception filepath**

------------------------------------------------------------------------

[**[display exception filepath]{lang="EN-US"}**]{#struct_0_x1063_20800_2022255360}[命令用来显示]{style="font-family:
宋体"}[core]{lang="EN-US"}[文件的保存路径。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1741371066}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1063_20800_x2028675118}

[**[display exception filepath]{lang="EN-US"}**]{#struct_0_x1063_20800_x1894696721}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1063_20800_x1775750338}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display exception filepath]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_x1856727052}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1063_20800_2078370648}[模式：]{style="font-family:宋体"}

[**[display exception filepath]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_151463903}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1574816482}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1063_20800_138047176}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1280830343}

[[network-admin]{lang="EN-US"}]{#struct_0_x1063_20800_x2029264943}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1063_20800_593973542}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1428405689}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x455092845}[：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x1483208597}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_1154941610}[：：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x902130443}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1835552944}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_230514008}[显示主控板上]{style="font-family:宋体"}[core]{lang="EN-US"}[文件的保存路径。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display exception filepath]{lang="EN-US"}]{#struct_0_x1063_20800_x2029199407}

[The exception filepath is flash:.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_1687930496}[显示主用主控板上]{style="font-family:宋体"}[core]{lang="EN-US"}[文件的保存路径。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display exception filepath]{lang="EN-US"}]{#struct_0_x1063_20800_x1889044911}

[The exception filepath on slot 0 is flash:.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_1398158746}[显示备用主控板上]{style="font-family:宋体"}[core]{lang="EN-US"}[文件的保存路径。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display exception filepath slot 1]{lang="EN-US"}]{#struct_0_x1063_20800_904508346}

[The exception filepath on slot 1 is NULL.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_x1775178551}[显示全局主用主控板上]{style="font-family:宋体"}[core]{lang="EN-US"}[文件的保存路径。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display exception filepath]{lang="EN-US"}]{#struct_0_x1063_20800_x832800845}

[The exception filepath on chassis 0 slot 1 is flash:.]{lang="EN-US"}
:::

::: {#1665512562 .myid}
[]{#_Toc404797188}[]{#struct_0_x1063_20800_x959873937}

**进程监控和维护 \-- 进程监控和维护命令 \-- display kernel deadloop**

------------------------------------------------------------------------

[**[display kernel deadloop]{lang="EN-US"}**]{#struct_0_x1063_20800_618068899}[命令用来显示内核线程死循环信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x2063354904}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1498205207}

[**[display kernel deadloop ]{lang="EN-US"}***[show-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ *offset* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x1063_20800_x1296563316}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1063_20800_1262466140}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display kernel deadloop ]{lang="EN-US"}***[show-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ *offset* \] \[ **verbose** \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_260378342}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1063_20800_x1906531664}[模式：]{style="font-family:宋体"}

[**[display kernel deadloop ]{lang="EN-US"}***[show-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ *offset* \] \[ **verbose** \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_2115025365}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x487172485}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1063_20800_618003363}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x2077891243}

[[network-admin]{lang="EN-US"}]{#struct_0_x1063_20800_1062347797}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1063_20800_x2029396015}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1550089179}

[*[show-number]{lang="EN-US"}*]{#struct_0_x1063_20800_x745512315}[：需要显示的死循环信息的数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[offset]{lang="EN-US"}*]{#struct_0_x1063_20800_741156855}[：需要显示的起始条目距最近条目的偏移，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1063_20800_x1488875559}[：表示显示详细信息。不指定该参数时，显示概要信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x101788470}[：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x396978596}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中设备的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x2080931397}[：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x902261515}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1063_20800_617937827}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_1903653388}[显示最近一条内核线程死循环的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display kernel deadloop 1]{lang="EN-US"}]{#struct_0_x1063_20800_x367939819}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- Deadloop record 1 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Description          : BUG: soft lockup - CPU#0 stuck for 61! \[comsh: 16306\]]{lang="EN-US"}

[Recorded at          : 2013-05-01  11:16:00.823018]{lang="EN-US"}

[Occurred at          : 2013-05-01  11:16:00.823018]{lang="EN-US"}

[Instruction address  : 0x4004158c]{lang="EN-US"}

[Thread               : comsh (TID: 16306)]{lang="EN-US"}

[Context              : thread context]{lang="EN-US"}

[Chassis              : 0]{lang="EN-US"}

[Slot                 : 0]{lang="EN-US"}

[CPU ID               : 0]{lang="EN-US"}

[Kernel module info   : module name (mrpnc) module address (0xe332a000)]{lang="EN-US"}

[                       module name (12500) module address (0xe00bd000)]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_x560795283}[显示最近一条内核线程死循环的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display kernel deadloop 1 verbose]{lang="EN-US"}]{#struct_0_x1063_20800_617675683}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- Deadloop record 1 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Description          : BUG: soft lockup - CPU#0 stuck for 61! \[comsh: 16306\]]{lang="EN-US"}

[Recorded at          : 2013-05-01  11:16:00.823018]{lang="EN-US"}

[Occurred at          : 2013-05-01  11:16:00.823018]{lang="EN-US"}

[Instruction address  : 0x4004158c]{lang="EN-US"}

[Thread               : comsh (TID: 16306)]{lang="EN-US"}

[Context              : thread context]{lang="EN-US"}

[Chassis              : 0]{lang="EN-US"}

[Slot                 : 0]{lang="EN-US"}

[CPU ID               : 0]{lang="EN-US"}

[Kernel module info   : module name (mrpnc) module address (0xe332a000)]{lang="EN-US"}

[                       module name (12500) module address (0xe00bd000)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Last 5 thread switches : migration/0 (11:16:00.823018)\--\> ]{lang="EN-US"}

[                         swapper (11:16:00.833018)\--\> ]{lang="EN-US"}

[                         kthreadd (11:16:00.833518)\--\> ]{lang="EN-US"}

[                         swapper (11:16:00.833550)\--\> ]{lang="EN-US"}

[                         disk (11:16:00.833560)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Register content:]{lang="EN-US"}

[Reg:       r0, Val = 0x00000000 ; Reg:       r1, Val = 0xe2be5ea0 ;]{lang="EN-US"}

[Reg:       r2, Val = 0x00000000 ; Reg:       r3, Val = 0x77777777 ;]{lang="EN-US"}

[Reg:       r4, Val = 0x00000000 ; Reg:       r5, Val = 0x00001492 ;]{lang="EN-US"}

[Reg:       r6, Val = 0x00000000 ; Reg:       r7, Val = 0x0000ffff ;]{lang="EN-US"}

[Reg:       r8, Val = 0x77777777 ; Reg:       r9, Val = 0x00000000 ;]{lang="EN-US"}

[Reg:      r10, Val = 0x00000001 ; Reg:      r11, Val = 0x0000002c ;]{lang="EN-US"}

[Reg:      r12, Val = 0x057d9484 ; Reg:      r13, Val = 0x00000000 ;]{lang="EN-US"}

[Reg:      r14, Val = 0x00000000 ; Reg:      r15, Val = 0x02000000 ;]{lang="EN-US"}

[Reg:      r16, Val = 0xe2be5f00 ; Reg:      r17, Val = 0x00000000 ;]{lang="EN-US"}

[Reg:      r18, Val = 0x00000000 ; Reg:      r19, Val = 0x00000000 ;]{lang="EN-US"}

[Reg:      r20, Val = 0x024c10f8 ; Reg:      r21, Val = 0x057d9244 ;]{lang="EN-US"}

[Reg:      r22, Val = 0x00002000 ; Reg:      r23, Val = 0x0000002c ;]{lang="EN-US"}

[Reg:      r24, Val = 0x00000002 ; Reg:      r25, Val = 0x24000024 ;]{lang="EN-US"}

[Reg:      r26, Val = 0x00000000 ; Reg:      r27, Val = 0x057d9484 ;]{lang="EN-US"}

[Reg:      r28, Val = 0x0000002c ; Reg:      r29, Val = 0x00000000 ;]{lang="EN-US"}

[Reg:      r30, Val = 0x0000002c ; Reg:      r31, Val = 0x00000000 ;]{lang="EN-US"}

[Reg:       cr, Val = 0x84000028 ; Reg:      nip, Val = 0x057d9550 ;]{lang="EN-US"}

[Reg:      xer, Val = 0x00000000 ; Reg:       lr, Val = 0x0186eff0 ;]{lang="EN-US"}

[Reg:      ctr, Val = 0x682f7344 ; Reg:      msr, Val = 0x00784b5c ;]{lang="EN-US"}

[Reg:     trap, Val = 0x0000b030 ; Reg:      dar, Val = 0x77777777 ;]{lang="EN-US"}

[Reg:    dsisr, Val = 0x40000000 ; Reg:   result, Val = 0x00020300 ;]{lang="EN-US"}

[ ]{lang="EN-US"}

[Dump stack (total 1024 bytes, 16 bytes/line):]{lang="EN-US"}

[0xe2be5ea0: 02 be 5e c0 24 00 00 24 00 00 00 00 05 7d 94 84]{lang="EN-US"}

[0xe2be5eb0: 00 00 00 04 00 00 00 00 00 00 00 28 05 8d 34 c4]{lang="EN-US"}

[0xe2be5ec0: 02 be 60 a0 01 86 ef f0 00 00 00 00 00 00 00 00]{lang="EN-US"}

[0xe2be5ed0: 02 04 05 b4 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[0xe2be5ee0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[0xe2be5ef0: 95 47 73 35 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[0xe2be5f00: a0 e1 64 21 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[0xe2be5f10: 00 00 00 00 00 00 00 00 00 00 00 00 01 e9 00 00]{lang="EN-US"}

[0xe2be5f20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[0xe2be5f30: 00 00 00 00 00 00 00 00 02 be 66 c0 02 be 66 d0]{lang="EN-US"}

[0xe2be5f40: 02 be 61 e0 00 00 00 02 00 00 00 00 02 44 b3 a4]{lang="EN-US"}

[0xe2be5f50: 02 be 5f 90 00 00 00 08 02 be 5f e0 00 00 00 08]{lang="EN-US"}

[0xe2be5f60: 02 be 5f 80 00 ac 1b 14 00 00 00 00 00 00 00 00]{lang="EN-US"}

[0xe2be5f70: 05 b4 5f 90 02 be 5f e0 00 00 00 30 02 be 5f e0]{lang="EN-US"}

[0xe2be5f80: 02 be 5f c0 00 ac 1b f4 00 00 00 00 02 45 00 00]{lang="EN-US"}

[0xe2be5f90: 00 03 00 00 00 00 00 00 02 be 5f e0 00 00 00 30]{lang="EN-US"}

[0xe2be5fa0: 02 be 5f c0 00 ac 1b 14 61 f1 2e ae 02 45 00 00]{lang="EN-US"}

[0xe2be5fb0: 02 44 b3 74 02 be 5f d0 00 00 00 30 02 be 5f e0]{lang="EN-US"}

[0xe2be5fc0: 02 be 60 60 01 74 ff f8 00 00 00 00 00 00 08 00]{lang="EN-US"}

[0xe2be5fd0: 02 be 5f f0 00 e8 93 7e 02 be 5f f8 02 be 5f fc]{lang="EN-US"}

[0xe2be5fe0: 00 00 00 00 00 00 00 00 00 00 00 00 02 be 60 18]{lang="EN-US"}

[0xe2be5ff0: 02 be 60 10 00 e9 65 98 00 00 00 58 00 00 2a 4f]{lang="EN-US"}

[0xe2be6000: 02 be 60 10 00 00 00 00 00 00 00 00 02 be 60 68]{lang="EN-US"}

[0xe2be6010: 02 be 60 40 00 e8 c6 a0 00 00 11 17 00 00 00 00]{lang="EN-US"}

[0xe2be6020: 02 be 60 40 00 00 00 00 00 00 00 00 02 be 60 98]{lang="EN-US"}

[0xe2be6030: 02 27 00 00 00 00 00 00 00 00 00 00 02 be 60 68]{lang="EN-US"}

[0xe2be6040: 02 be 60 60 00 00 00 01 00 00 b0 30 02 be 60 98]{lang="EN-US"}

[0xe2be6050: 00 00 00 04 02 21 00 00 00 00 00 00 01 e9 00 00]{lang="EN-US"}

[0xe2be6060: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[0xe2be6070: 00 00 00 00 00 00 00 00 02 be 66 c0 02 be 66 d0]{lang="EN-US"}

[0xe2be6080: 02 be 61 e0 00 00 00 02 00 00 00 00 02 be 61 70]{lang="EN-US"}

[0xe2be6090: 00 00 00 00 02 21 00 00 05 8d 34 c4 05 7d 92 44]{lang="EN-US"}

[ ]{lang="EN-US"}

[Call trace:]{lang="EN-US"}

[Function Address = 0x8012a4b4]{lang="EN-US"}

[Function Address = 0x8017989c]{lang="EN-US"}

[Function Address = 0x80179b30]{lang="EN-US"}

[Function Address = 0x80127438]{lang="EN-US"}

[Function Address = 0x8012d734]{lang="EN-US"}

[Function Address = 0x80100a00]{lang="EN-US"}

[Function Address = 0xe0071004]{lang="EN-US"}

[Function Address = 0x8016ce0c]{lang="EN-US"}

[Function Address = 0x801223a0]{lang="EN-US"}

[   ]{lang="EN-US"}

[Instruction dump:]{lang="EN-US"}

[41a2fe9c 812300ec 800200ec 7f890000 409efe8c 80010014 540b07b9 40a2fe80]{lang="EN-US"}

[4bfffe6c 80780290 7f64db78 4804ea35 \<807f002c\> 38800000 38a00080 3863000c]{lang="EN-US"}

[]{#struct_0_x1063_20800_x1844784610}[[表1-2 ]{lang="EN-US"}[display kernel deadloop]{lang="EN-US"}]{#_Ref318724271}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2068419571}[[字段]{style="font-family:黑体"}]{#struct_0_x1063_20800_x934617751}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1063_20800_128681223}

[[Description]{lang="EN-US"}]{#struct_0_x1063_20800_1887931701}

[[发生死循环的内核线程的描述信息，包括死循环内核线程所在的]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_x1063_20800_x958076186}[的编号、内核线程连续运行的时间、内核线程的名称和编号]{style="font-family:宋体"}

[[Recorded at]{lang="EN-US"}]{#struct_0_x1063_20800_618658723}

[[内核线程死循环被记录到主控板上的时间点，精确到微秒]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1734035722}

[[Occurred at]{lang="EN-US"}]{#struct_0_x1063_20800_1338633030}

[[内核线程发生死循环的时间，精确到微秒]{style="font-family:宋体"}]{#struct_0_x1063_20800_x51672719}

[[Instruction address]{lang="EN-US"}]{#struct_0_x1063_20800_1840334689}

[[内核线程被检测到发生死循环时对应的指令信息]{style="font-family:宋体"}]{#struct_0_x1063_20800_210334085}

[[Thread]{lang="EN-US"}]{#struct_0_x1063_20800_618593187}

[[发生死循环的内核线程的名称和编号]{style="font-family:宋体"}]{#struct_0_x1063_20800_22138672}

[[Context]{lang="EN-US"}]{#struct_0_x1063_20800_x545035878}

[[内核线程被检测到发生死循环时所在的上下文环境]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1413369193}

[[Chassis]{lang="EN-US"}]{#struct_0_x1063_20800_720514540}

[[运行该内核线程的设备的成员编号（仅]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1063_20800_2143768908}[模式支持）]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_x1063_20800_618134432}

[[运行该内核线程的主控板所在的槽位号（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1063_20800_x1354486856}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[运行该内核线程的设备的成员编号（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1063_20800_x470032351}[设备）]{style="font-family:宋体"}

[[为固定值]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x1063_20800_x1556092212}[，无特殊意义（集中式设备）]{style="font-family:宋体"}

[[CPU ID]{lang="EN-US"}]{#struct_0_x1063_20800_577706876}

[[运行该内核线程的]{style="font-family:宋体"}]{#struct_0_x1063_20800_618068896}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}

[[Kernel module info]{lang="EN-US"}]{#struct_0_x1063_20800_x2063354903}

[[内核线程被检测到发生死循环时，系统中已加载的内核模块信息。包括内核模块名和内核模块加载的内存地址]{style="font-family:宋体"}]{#struct_0_x1063_20800_874447788}

[[Last 5 thread switches]{lang="EN-US"}]{#struct_0_x1063_20800_775296491}

[[内核线程被检测到发生死循环时，记录死循环发生的]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_x1063_20800_618003360}[上、最近五次的内核线程切换轨迹。包括内核线程的名称和内核线程切换时间点，时间精确到微秒]{style="font-family:宋体"}

[[Register content]{lang="EN-US"}]{#struct_0_x1063_20800_x2077891246}

[[内核线程被检测到发生死循环时现场的寄存器信息。]{style="font-family:宋体"}[Reg]{lang="EN-US"}]{#struct_0_x1063_20800_1465632324}[表示寄存器名称，]{style="font-family:宋体"}[Val]{lang="EN-US"}[表示寄存器中保存的值]{style="font-family:宋体"}

[[Dump stack]{lang="EN-US"}]{#struct_0_x1063_20800_x1158464322}

[[内核线程被检测到发生死循环时现场的堆栈信息]{style="font-family:宋体"}]{#struct_0_x1063_20800_x933816966}

[[Call trace]{lang="EN-US"}]{#struct_0_x1063_20800_617937824}

[[内核线程被检测到发生死循环时现场的函数调用栈信息，即每级调用函数的指令地址]{style="font-family:宋体"}]{#struct_0_x1063_20800_1903653387}

[[Instruction dump]{lang="EN-US"}]{#struct_0_x1063_20800_x367612139}

[[内核线程被检测到发生死循环时对应的指令码。非法指令用]{style="font-family:宋体"}[ffffffff]{lang="EN-US"}]{#struct_0_x1063_20800_x1339356487}[表示]{style="font-family:宋体"}

[[No information to display]{lang="EN-US"}]{#struct_0_x1063_20800_617872288}

[[表示系统中没有内核线程死循环记录]{style="font-family:宋体"}]{#struct_0_x1063_20800_x498466903}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_873926491}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ]{lang="EN-US"}**]{#struct_0_x1063_20800_x1127392136}**[kernel ]{lang="EN-US"}[deadloop]{lang="EN-US"}**

::: {#-1414755061 .myid}
[]{#_Toc404797189}[]{#struct_0_x1063_20800_375790777}

**进程监控和维护 \-- 进程监控和维护命令 \-- display kernel deadloop configuration**

------------------------------------------------------------------------

[**[display kernel deadloop configuration]{lang="EN-US"}**]{#struct_0_x1063_20800_27061059}[命令用来显示内核线程死循环监控参数配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_617806752}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1063_20800_x865771893}

[**[display kernel deadloop configuration]{lang="EN-US"}**]{#struct_0_x1063_20800_1617532427}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1063_20800_x7070899}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display kernel deadloop configuration ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_x1398526956}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1063_20800_x789074021}[模式：]{style="font-family:宋体"}

[**[display kernel deadloop configuration ]{lang="EN-US"}**[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_1569527411}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1459782500}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1063_20800_2099067770}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1063_20800_617741216}

[[network-admin]{lang="EN-US"}]{#struct_0_x1063_20800_107937850}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1063_20800_x2029199408}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1376546734}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_1572485226}[：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x360869291}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中设备的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_249754002}[：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x902589195}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1063_20800_325143629}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_2027381096}[显示内核线程死循环监控参数配置。]{style="font-family:宋体"}

[[\<Sysname\> display kernel deadloop configuration]{lang="EN-US"}]{#struct_0_x1063_20800_617675680}

[Thread dead loop detection: Enabled]{lang="EN-US"}

[Dead loop timer (in seconds): 60]{lang="EN-US"}

[Threads excluded from monitoring: 1]{lang="EN-US"}

[  TID:     15   Name: co0    ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display kernel deadloop configuration]{lang="EN-US"}]{#struct_0_x1063_20800_x1844784611}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2067122163}[[字段]{style="font-family:黑体"}]{#struct_0_x1063_20800_631466190}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1063_20800_x976850465}

[[Thread dead loop detection: Enabled]{lang="EN-US"}]{#struct_0_x1063_20800_1760363265}

[[内核线程死循环检测功能处于开启状态]{style="font-family:宋体"}]{#struct_0_x1063_20800_1459466689}

[[Thread dead loop detection: Disabled]{lang="EN-US"}]{#struct_0_x1063_20800_x1773180685}

[[内核线程死循环检测功能处于关闭状态]{style="font-family:宋体"}]{#struct_0_x1063_20800_618658720}

[[Dead loop timer (in seconds): *n*]{lang="EN-US"}]{#struct_0_x1063_20800_x1734035719}

[[内核线程死循环判定周期（单位为秒），即内核线程连续运行时间大于]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_x1063_20800_1385883805}[秒时，则判定为死循环]{style="font-family:宋体"}

[[Threads excluded from monitoring]{lang="EN-US"}]{#struct_0_x1063_20800_x1299381809}

[[不进行死循环检测的内核线程列表，配置]{style="font-family:宋体"}**[monitor kernel deadloop exclude-thread]{lang="EN-US"}**]{#struct_0_x1063_20800_x1790651365}[命令后才会显示该信息]{style="font-family:宋体"}

[[Name]{lang="EN-US"}]{#struct_0_x1063_20800_x1578776041}

[[不进行死循环检测的内核线程的名称]{style="font-family:宋体"}]{#struct_0_x1063_20800_618593184}

[[TID]{lang="EN-US"}]{#struct_0_x1063_20800_22138675}

[[不进行死循环检测的内核线程的编号]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1736676966}

[[No thread is excluded from monitoring]{lang="EN-US"}]{#struct_0_x1063_20800_1804749442}

[[对所有内核线程都进行死循环检查]{style="font-family:宋体"}]{#struct_0_x1063_20800_33701120}

[ ]{lang="EN-US"}

::: {#-1757077756 .myid}
[]{#_Toc404797190}[]{#struct_0_x1063_20800_618134433}[]{#_Toc318724798}[]{#_Toc318724799}[]{#_Toc318724800}[]{#_Toc318724801}

**进程监控和维护 \-- 进程监控和维护命令 \-- display kernel exception**

------------------------------------------------------------------------

[**[display kernel exception]{lang="EN-US"}**]{#struct_0_x1063_20800_x1354486857}[命令用来显示内核线程的异常信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1096051590}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1063_20800_184869897}

[**[display kernel exception ]{lang="EN-US"}***[show-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ *offset* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x1063_20800_738650213}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1063_20800_x662670314}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display kernel exception ]{lang="EN-US"}***[show-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ *offset* \] \[ **verbose** \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_1178804614}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1063_20800_x2012936598}[模式：]{style="font-family:宋体"}

[**[display kernel exception ]{lang="EN-US"}***[show-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ *offset* \] \[ **verbose** \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_x910204535}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1063_20800_618068897}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1063_20800_x2063354902}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x691636153}

[[network-admin]{lang="EN-US"}]{#struct_0_x1063_20800_x1799811167}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1063_20800_x2029330480}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1833933034}

[*[show-number]{lang="EN-US"}*]{#struct_0_x1063_20800_x2023220301}[：需要显示的异常信息的数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[offset]{lang="EN-US"}*]{#struct_0_x1063_20800_1785600420}[：开始显示的条目距最近条目的偏移，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1063_20800_x839944403}[：显示详细信息。不指定该参数时，显示概要信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_60035212}[：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_618003361}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中设备的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x2077891245}[：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x902523659}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x100451617}

[[当内核线程在运行过程中发生异常时，系统会自动记录异常信息，以便设备维护人员定位问题。]{style="font-family:宋体"}]{#struct_0_x1063_20800_811427324}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1095614747}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_1469197011}[显示最近一条内核线程异常的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display kernel exception 1]{lang="EN-US"}]{#struct_0_x1063_20800_617937825}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- Exception record 1 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Description          : Oops\[#0\]]{lang="EN-US"}

[Recorded at          : 2013-05-01  11:16:00.823018]{lang="EN-US"}

[Occurred at          : 2013-05-01  11:16:00.823018]{lang="EN-US"}

[Instruction address  : 0x4004158c]{lang="EN-US"}

[Thread               : comsh (TID: 16306)]{lang="EN-US"}

[Context              : thread context]{lang="EN-US"}

[Chassis              : 0]{lang="EN-US"}

[Slot                 : 0]{lang="EN-US"}

[CPU ID               : 0]{lang="EN-US"}

[Kernel module info   : module name (mrpnc) module address (0xe332a000)]{lang="EN-US"}

[                       module name (disk) module address (0xe00bd000)]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_1903653386}[显示最近一条内核线程异常的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display kernel exception 1 verbose]{lang="EN-US"}]{#struct_0_x1063_20800_617741217}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- Exception record 1 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Description          : Oops\[#0\]]{lang="EN-US"}

[Recorded at          : 2013-05-01  11:16:00.823018]{lang="EN-US"}

[Occurred at          : 2013-05-01  11:16:00.823018]{lang="EN-US"}

[Instruction address  : 0x4004158c]{lang="EN-US"}

[Thread               : comsh (TID: 16306)]{lang="EN-US"}

[Context              : thread context]{lang="EN-US"}

[Chassis              : 0]{lang="EN-US"}

[Slot                 : 0]{lang="EN-US"}

[CPU ID               : 0]{lang="EN-US"}

[Kernel module info   : module name (mrpnc) module address (0xe332a000)]{lang="EN-US"}

[                       module name (12500) module address (0xe00bd000)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Last 5 thread switches : migration/0 (11:16:00.823018)\--\> ]{lang="EN-US"}

[                         swapper (11:16:00.833018)\--\> ]{lang="EN-US"}

[                         kthreadd (11:16:00.833518)\--\> ]{lang="EN-US"}

[                         swapper (11:16:00.833550)\--\> ]{lang="EN-US"}

[                         disk (11:16:00.833560)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Register content:]{lang="EN-US"}

[Reg:       r0, Val = 0x00000000 ; Reg:       r1, Val = 0xe2be5ea0 ;]{lang="EN-US"}

[Reg:       r2, Val = 0x00000000 ; Reg:       r3, Val = 0x77777777 ;]{lang="EN-US"}

[Reg:       r4, Val = 0x00000000 ; Reg:       r5, Val = 0x00001492 ;]{lang="EN-US"}

[Reg:       r6, Val = 0x00000000 ; Reg:       r7, Val = 0x0000ffff ;]{lang="EN-US"}

[Reg:       r8, Val = 0x77777777 ; Reg:       r9, Val = 0x00000000 ;]{lang="EN-US"}

[Reg:      r10, Val = 0x00000001 ; Reg:      r11, Val = 0x0000002c ;]{lang="EN-US"}

[Reg:      r12, Val = 0x057d9484 ; Reg:      r13, Val = 0x00000000 ;]{lang="EN-US"}

[Reg:      r14, Val = 0x00000000 ; Reg:      r15, Val = 0x02000000 ;]{lang="EN-US"}

[Reg:      r16, Val = 0xe2be5f00 ; Reg:      r17, Val = 0x00000000 ;]{lang="EN-US"}

[Reg:      r18, Val = 0x00000000 ; Reg:      r19, Val = 0x00000000 ;]{lang="EN-US"}

[Reg:      r20, Val = 0x024c10f8 ; Reg:      r21, Val = 0x057d9244 ;]{lang="EN-US"}

[Reg:      r22, Val = 0x00002000 ; Reg:      r23, Val = 0x0000002c ;]{lang="EN-US"}

[Reg:      r24, Val = 0x00000002 ; Reg:      r25, Val = 0x24000024 ;]{lang="EN-US"}

[Reg:      r26, Val = 0x00000000 ; Reg:      r27, Val = 0x057d9484 ;]{lang="EN-US"}

[Reg:      r28, Val = 0x0000002c ; Reg:      r29, Val = 0x00000000 ;]{lang="EN-US"}

[Reg:      r30, Val = 0x0000002c ; Reg:      r31, Val = 0x00000000 ;]{lang="EN-US"}

[Reg:       cr, Val = 0x84000028 ; Reg:      nip, Val = 0x057d9550 ;]{lang="EN-US"}

[Reg:      xer, Val = 0x00000000 ; Reg:       lr, Val = 0x0186eff0 ;]{lang="EN-US"}

[Reg:      ctr, Val = 0x682f7344 ; Reg:      msr, Val = 0x00784b5c ;]{lang="EN-US"}

[Reg:     trap, Val = 0x0000b030 ; Reg:      dar, Val = 0x77777777 ;]{lang="EN-US"}

[Reg:    dsisr, Val = 0x40000000 ; Reg:   result, Val = 0x00020300 ;]{lang="EN-US"}

[ ]{lang="EN-US"}

[Dump stack (total 1024 bytes, 16 bytes/line):]{lang="EN-US"}

[0xe2be5ea0: 02 be 5e c0 24 00 00 24 00 00 00 00 05 7d 94 84]{lang="EN-US"}

[0xe2be5eb0: 00 00 00 04 00 00 00 00 00 00 00 28 05 8d 34 c4]{lang="EN-US"}

[0xe2be5ec0: 02 be 60 a0 01 86 ef f0 00 00 00 00 00 00 00 00]{lang="EN-US"}

[0xe2be5ed0: 02 04 05 b4 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[0xe2be5ee0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[0xe2be5ef0: 95 47 73 35 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[0xe2be5f00: a0 e1 64 21 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[0xe2be5f10: 00 00 00 00 00 00 00 00 00 00 00 00 01 e9 00 00]{lang="EN-US"}

[0xe2be5f20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[0xe2be5f30: 00 00 00 00 00 00 00 00 02 be 66 c0 02 be 66 d0]{lang="EN-US"}

[0xe2be5f40: 02 be 61 e0 00 00 00 02 00 00 00 00 02 44 b3 a4]{lang="EN-US"}

[0xe2be5f50: 02 be 5f 90 00 00 00 08 02 be 5f e0 00 00 00 08]{lang="EN-US"}

[0xe2be5f60: 02 be 5f 80 00 ac 1b 14 00 00 00 00 00 00 00 00]{lang="EN-US"}

[0xe2be5f70: 05 b4 5f 90 02 be 5f e0 00 00 00 30 02 be 5f e0]{lang="EN-US"}

[0xe2be5f80: 02 be 5f c0 00 ac 1b f4 00 00 00 00 02 45 00 00]{lang="EN-US"}

[0xe2be5f90: 00 03 00 00 00 00 00 00 02 be 5f e0 00 00 00 30]{lang="EN-US"}

[0xe2be5fa0: 02 be 5f c0 00 ac 1b 14 61 f1 2e ae 02 45 00 00]{lang="EN-US"}

[0xe2be5fb0: 02 44 b3 74 02 be 5f d0 00 00 00 30 02 be 5f e0]{lang="EN-US"}

[0xe2be5fc0: 02 be 60 60 01 74 ff f8 00 00 00 00 00 00 08 00]{lang="EN-US"}

[0xe2be5fd0: 02 be 5f f0 00 e8 93 7e 02 be 5f f8 02 be 5f fc]{lang="EN-US"}

[0xe2be5fe0: 00 00 00 00 00 00 00 00 00 00 00 00 02 be 60 18]{lang="EN-US"}

[0xe2be5ff0: 02 be 60 10 00 e9 65 98 00 00 00 58 00 00 2a 4f]{lang="EN-US"}

[0xe2be6000: 02 be 60 10 00 00 00 00 00 00 00 00 02 be 60 68]{lang="EN-US"}

[0xe2be6010: 02 be 60 40 00 e8 c6 a0 00 00 11 17 00 00 00 00]{lang="EN-US"}

[0xe2be6020: 02 be 60 40 00 00 00 00 00 00 00 00 02 be 60 98]{lang="EN-US"}

[0xe2be6030: 02 27 00 00 00 00 00 00 00 00 00 00 02 be 60 68]{lang="EN-US"}

[0xe2be6040: 02 be 60 60 00 00 00 01 00 00 b0 30 02 be 60 98]{lang="EN-US"}

[0xe2be6050: 00 00 00 04 02 21 00 00 00 00 00 00 01 e9 00 00]{lang="EN-US"}

[0xe2be6060: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[0xe2be6070: 00 00 00 00 00 00 00 00 02 be 66 c0 02 be 66 d0]{lang="EN-US"}

[0xe2be6080: 02 be 61 e0 00 00 00 02 00 00 00 00 02 be 61 70]{lang="EN-US"}

[0xe2be6090: 00 00 00 00 02 21 00 00 05 8d 34 c4 05 7d 92 44]{lang="EN-US"}

[ ]{lang="EN-US"}

[Call trace:]{lang="EN-US"}

[Function Address = 0x8012a4b4]{lang="EN-US"}

[Function Address = 0x8017989c]{lang="EN-US"}

[Function Address = 0x80179b30]{lang="EN-US"}

[Function Address = 0x80127438]{lang="EN-US"}

[Function Address = 0x8012d734]{lang="EN-US"}

[Function Address = 0x80100a00]{lang="EN-US"}

[Function Address = 0xe0071004]{lang="EN-US"}

[Function Address = 0x8016ce0c]{lang="EN-US"}

[Function Address = 0x801223a0]{lang="EN-US"}

[   ]{lang="EN-US"}

[Instruction dump:]{lang="EN-US"}

[41a2fe9c 812300ec 800200ec 7f890000 409efe8c 80010014 540b07b9 40a2fe80]{lang="EN-US"}

[4bfffe6c 80780290 7f64db78 4804ea35 \<807f002c\> 38800000 38a00080 3863000c]{lang="EN-US"}

[[本命令显示信息的详细描述请参见]{style="font-family:宋体"}]{#struct_0_x1063_20800_107937851}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-2]{lang="EN-US"}](?1665512562#_Ref318724271)[。]{style="font-family:宋体"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1376546733}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ]{lang="EN-US"}**]{#struct_0_x1063_20800_x1962967183}**[kernel ]{lang="EN-US"}[exception]{lang="EN-US"}**
:::

::: {#513714458 .myid}
[]{#_Toc404797191}[]{#struct_0_x1063_20800_1600424703}

**进程监控和维护 \-- 进程监控和维护命令 \-- display kernel reboot**

------------------------------------------------------------------------

[**[display kernel reboot]{lang="EN-US"}**]{#struct_0_x1063_20800_617675681}[命令用来显示内核线程的重启信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1844784612}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1063_20800_228181663}

[**[display kernel reboot ]{lang="EN-US"}***[show-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ *offset* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x1063_20800_x865447134}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1063_20800_x568958}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display kernel reboot ]{lang="EN-US"}***[show-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ *offset* \] \[ **verbose** \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_471768500}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1063_20800_1318735544}[模式：]{style="font-family:宋体"}

[**[display kernel reboot ]{lang="EN-US"}***[show-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ *offset* \] \[ **verbose** \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_x1327799655}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1248513435}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1063_20800_618658721}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1734035720}

[[network-admin]{lang="EN-US"}]{#struct_0_x1063_20800_175833616}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1063_20800_x2029264945}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x202085997}

[*[show-number]{lang="EN-US"}*]{#struct_0_x1063_20800_1131427708}[：需要显示的重启信息的数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[offset]{lang="EN-US"}*]{#struct_0_x1063_20800_x1263487290}[：需要显示的起始条目距最近条目的偏移，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1063_20800_266738557}[：表示显示详细信息。不指定该参数时，显示概要信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_1697418669}[：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x1327778994}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中设备的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_618593185}[：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x902130442}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1063_20800_22138674}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_601975194}[显示最近一条内核线程重启的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display kernel reboot 1]{lang="EN-US"}]{#struct_0_x1063_20800_x603885062}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- Reboot record 1 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Recorded at          : 2013-05-01  11:16:00.823018]{lang="EN-US"}

[Occurred at          : 2013-05-01  11:16:00.823018]{lang="EN-US"}

[Reason               : 0x31]{lang="EN-US"}

[Thread               : comsh (TID: 16306)]{lang="EN-US"}

[Context              : thread context]{lang="EN-US"}

[Chassis              : 0]{lang="EN-US"}

[Slot                 : 0]{lang="EN-US"}

[CPU ID               : 0]{lang="EN-US"}

[Kernel module info   : module name (mrpnc) module address (0xe332a000)]{lang="EN-US"}

[                       module name (12500) module address (0xe00bd000)]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_814168298}[显示最近一条内核线程重启的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display kernel reboot 1 verbose]{lang="EN-US"}]{#struct_0_x1063_20800_x2110879991}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- Reboot record 1 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Recorded at          : 2013-05-01  11:16:00.823018]{lang="EN-US"}

[Occurred at          : 2013-05-01  11:16:00.823018]{lang="EN-US"}

[Reason               : 0x31]{lang="EN-US"}

[Thread               : comsh (TID: 16306)]{lang="EN-US"}

[Context              : thread context]{lang="EN-US"}

[Chassis              : 0]{lang="EN-US"}

[Slot                 : 0]{lang="EN-US"}

[CPU ID               : 0]{lang="EN-US"}

[Kernel module info   : module name (mrpnc) module address (0xe332a000)]{lang="EN-US"}

[                       module name (12500) module address (0xe00bd000)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Last 5 thread switches : migration/0 (11:16:00.823018)\--\> ]{lang="EN-US"}

[                         swapper (11:16:00.833018)\--\> ]{lang="EN-US"}

[                         kthreadd (11:16:00.833518)\--\> ]{lang="EN-US"}

[                         swapper (11:16:00.833550)\--\> ]{lang="EN-US"}

[                         disk (11:16:00.833560)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Dump stack (total 1024 bytes, 16 bytes/line):]{lang="EN-US"}

[0xe2be5ea0: 02 be 5e c0 24 00 00 24 00 00 00 00 05 7d 94 84]{lang="EN-US"}

[0xe2be5eb0: 00 00 00 04 00 00 00 00 00 00 00 28 05 8d 34 c4]{lang="EN-US"}

[0xe2be5ec0: 02 be 60 a0 01 86 ef f0 00 00 00 00 00 00 00 00]{lang="EN-US"}

[0xe2be5ed0: 02 04 05 b4 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[0xe2be5ee0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[0xe2be5ef0: 95 47 73 35 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[0xe2be5f00: a0 e1 64 21 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[0xe2be5f10: 00 00 00 00 00 00 00 00 00 00 00 00 01 e9 00 00]{lang="EN-US"}

[0xe2be5f20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[0xe2be5f30: 00 00 00 00 00 00 00 00 02 be 66 c0 02 be 66 d0]{lang="EN-US"}

[0xe2be5f40: 02 be 61 e0 00 00 00 02 00 00 00 00 02 44 b3 a4]{lang="EN-US"}

[0xe2be5f50: 02 be 5f 90 00 00 00 08 02 be 5f e0 00 00 00 08]{lang="EN-US"}

[0xe2be5f60: 02 be 5f 80 00 ac 1b 14 00 00 00 00 00 00 00 00]{lang="EN-US"}

[0xe2be5f70: 05 b4 5f 90 02 be 5f e0 00 00 00 30 02 be 5f e0]{lang="EN-US"}

[0xe2be5f80: 02 be 5f c0 00 ac 1b f4 00 00 00 00 02 45 00 00]{lang="EN-US"}

[0xe2be5f90: 00 03 00 00 00 00 00 00 02 be 5f e0 00 00 00 30]{lang="EN-US"}

[0xe2be5fa0: 02 be 5f c0 00 ac 1b 14 61 f1 2e ae 02 45 00 00]{lang="EN-US"}

[0xe2be5fb0: 02 44 b3 74 02 be 5f d0 00 00 00 30 02 be 5f e0]{lang="EN-US"}

[0xe2be5fc0: 02 be 60 60 01 74 ff f8 00 00 00 00 00 00 08 00]{lang="EN-US"}

[0xe2be5fd0: 02 be 5f f0 00 e8 93 7e 02 be 5f f8 02 be 5f fc]{lang="EN-US"}

[0xe2be5fe0: 00 00 00 00 00 00 00 00 00 00 00 00 02 be 60 18]{lang="EN-US"}

[0xe2be5ff0: 02 be 60 10 00 e9 65 98 00 00 00 58 00 00 2a 4f]{lang="EN-US"}

[0xe2be6000: 02 be 60 10 00 00 00 00 00 00 00 00 02 be 60 68]{lang="EN-US"}

[0xe2be6010: 02 be 60 40 00 e8 c6 a0 00 00 11 17 00 00 00 00]{lang="EN-US"}

[0xe2be6020: 02 be 60 40 00 00 00 00 00 00 00 00 02 be 60 98]{lang="EN-US"}

[0xe2be6030: 02 27 00 00 00 00 00 00 00 00 00 00 02 be 60 68]{lang="EN-US"}

[0xe2be6040: 02 be 60 60 00 00 00 01 00 00 b0 30 02 be 60 98]{lang="EN-US"}

[0xe2be6050: 00 00 00 04 02 21 00 00 00 00 00 00 01 e9 00 00]{lang="EN-US"}

[0xe2be6060: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[0xe2be6070: 00 00 00 00 00 00 00 00 02 be 66 c0 02 be 66 d0]{lang="EN-US"}

[0xe2be6080: 02 be 61 e0 00 00 00 02 00 00 00 00 02 be 61 70]{lang="EN-US"}

[0xe2be6090: 00 00 00 00 02 21 00 00 05 8d 34 c4 05 7d 92 44]{lang="EN-US"}

[ ]{lang="EN-US"}

[Call trace:]{lang="EN-US"}

[Function Address = 0x8012a4b4]{lang="EN-US"}

[Function Address = 0x8017989c]{lang="EN-US"}

[Function Address = 0x80179b30]{lang="EN-US"}

[Function Address = 0x80127438]{lang="EN-US"}

[Function Address = 0x8012d734]{lang="EN-US"}

[Function Address = 0x80100a00]{lang="EN-US"}

[Function Address = 0xe0071004]{lang="EN-US"}

[Function Address = 0x8016ce0c]{lang="EN-US"}

[Function Address = 0x801223a0]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display kernel reboot]{lang="EN-US"}]{#struct_0_x1063_20800_1037525089}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2094491315}[[字段]{style="font-family:宋体"}]{#struct_0_x1063_20800_1299107193}
:::

[描述]{style="font-family:宋体"}

[[Recorded at]{lang="EN-US"}]{#struct_0_x1063_20800_1450757410}

[[内核线程重启记录到主控板上的时间点，精确到微秒]{style="font-family:宋体"}]{#struct_0_x1063_20800_1522988148}

[[Occurred at]{lang="EN-US"}]{#struct_0_x1063_20800_1615517588}

[[内核线程重启的时间，精确到微秒]{style="font-family:宋体"}]{#struct_0_x1063_20800_x2110945527}

[[Reason]{lang="EN-US"}]{#struct_0_x1063_20800_x448388094}

[[内核线程重启的原因]{style="font-family:宋体"}]{#struct_0_x1063_20800_338212302}

[[Thread]{lang="EN-US"}]{#struct_0_x1063_20800_x812320200}

[[重启的内核线程的名称和编号]{style="font-family:宋体"}]{#struct_0_x1063_20800_1899745852}

[[Context]{lang="EN-US"}]{#struct_0_x1063_20800_x1476938206}

[[内核线程重启时所在的上下文环境]{style="font-family:宋体"}]{#struct_0_x1063_20800_x2111011063}

[[Chassis]{lang="EN-US"}]{#struct_0_x1063_20800_1428765195}

[[运行该内核线程的设备的成员编号（仅]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1063_20800_x1260333657}[模式支持）]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_x1063_20800_x1476668342}

[[运行该内核线程的主控板所在的槽位号（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1063_20800_x1623201235}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[运行该内核线程的设备的成员编号（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1063_20800_x2111076599}[设备）]{style="font-family:宋体"}

[[为固定值]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x1063_20800_472778144}[，无特殊意义（集中式设备）]{style="font-family:宋体"}

[[CPU ID]{lang="EN-US"}]{#struct_0_x1063_20800_2099942368}

[[重启发生时当前]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_x1063_20800_x1924046425}[的编号]{style="font-family:宋体"}

[[Kernel module info]{lang="EN-US"}]{#struct_0_x1063_20800_1649211757}

[[重启发生时，系统中已加载的内核模块信息。包括内核模块名和内核模块加载的内存地址]{style="font-family:宋体"}]{#struct_0_x1063_20800_x2111142135}

[[Last 5 thread switches]{lang="EN-US"}]{#struct_0_x1063_20800_x205451873}

[[系统重启时，记录重启的]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_x1063_20800_1820157442}[上、最近五次的内核线程切换轨迹。包括内核线程的名称和内核线程切换时间点，时间精确到微秒]{style="font-family:宋体"}

[[Dump stack]{lang="EN-US"}]{#struct_0_x1063_20800_466927402}

[[内核线程重启时现场的堆栈信息]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1592585868}

[[Call trace]{lang="EN-US"}]{#struct_0_x1063_20800_x2111207671}

[[内核线程重启时现场的函数调用栈信息，即每级调用函数的指令地址]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1290462400}

[[No information to display]{lang="EN-US"}]{#struct_0_x1063_20800_x1997169557}

[[表示系统中没有内核线程重启记录]{style="font-family:宋体"}]{#struct_0_x1063_20800_741200585}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1194964621}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ]{lang="EN-US"}**]{#struct_0_x1063_20800_x2110224631}**[kernel reboot]{lang="EN-US"}**

::: {#1641310426 .myid}
[]{#_Toc404797192}[]{#struct_0_x1063_20800_x874509587}

**进程监控和维护 \-- 进程监控和维护命令 \-- display kernel starvation**

------------------------------------------------------------------------

[**[display kernel starvation]{lang="EN-US"}**]{#struct_0_x1063_20800_960817397}[命令用来显示内核线程饿死信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1578880316}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1544932353}

[**[display kernel starvation ]{lang="EN-US"}***[show-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ *offset* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x1063_20800_x1633913447}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1063_20800_x1854045064}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display kernel starvation ]{lang="EN-US"}***[show-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ *offset* \] \[ **verbose** \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_1248194766}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1063_20800_x1004572339}[模式：]{style="font-family:宋体"}

[**[display kernel starvation ]{lang="EN-US"}***[show-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ *offset* \] \[ **verbose** \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_x2110290167}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1063_20800_2139006741}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1431888024}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1063_20800_744458208}

[[network-admin]{lang="EN-US"}]{#struct_0_x1063_20800_x2043264897}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1063_20800_x2028740657}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1738178035}

[*[show-number]{lang="EN-US"}*]{#struct_0_x1063_20800_1578285524}[：需要显示的饿死信息的数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[offset]{lang="EN-US"}*]{#struct_0_x1063_20800_1964544791}[：需要显示的起始条目距最近条目的偏移，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1063_20800_173942174}[：表示显示详细信息。不指定该参数时，显示概要信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x2110748918}[：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_13508949}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中设备的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x1736162592}[：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x902392586}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1063_20800_394777697}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_756842456}[显示最近一条内核线程饿死的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display kernel starvation 1]{lang="EN-US"}]{#struct_0_x1063_20800_x880473145}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- Starvation record 1 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Description          : INFO: task comsh: 16306 blocked for more than 10 seconds.]{lang="EN-US"}

[Recorded at          : 2013-05-01  11:16:00.823018]{lang="EN-US"}

[Occurred at          : 2013-05-01  11:16:00.823018]{lang="EN-US"}

[Instruction address  : 0x4004158c]{lang="EN-US"}

[Thread               : comsh (TID: 16306)]{lang="EN-US"}

[Context              : thread context]{lang="EN-US"}

[Chassis              : 0]{lang="EN-US"}

[Slot                 : 0]{lang="EN-US"}

[CPU ID               : 0]{lang="EN-US"}

[Kernel module info   : module name (mrpnc) module address (0xe332a000)]{lang="EN-US"}

[                       module name (12500) module address (0xe00bd000)]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_x2110814454}[显示最近一条内核线程饿死的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display kernel starvation 1 verbose]{lang="EN-US"}]{#struct_0_x1063_20800_x2111011062}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- Starvation record 1 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Description          : INFO: task comsh: 16306 blocked for more than 10 seconds.]{lang="EN-US"}

[Recorded at          : 2013-05-01  11:16:00.823018]{lang="EN-US"}

[Occurred at          : 2013-05-01  11:16:00.823018]{lang="EN-US"}

[Instruction address  : 0x4004158c]{lang="EN-US"}

[Thread               : comsh (TID: 16306)]{lang="EN-US"}

[Context              : thread context]{lang="EN-US"}

[Chassis              : 0]{lang="EN-US"}

[Slot                 : 0]{lang="EN-US"}

[CPU ID               : 0]{lang="EN-US"}

[Kernel module info   : module name (mrpnc) module address (0xe332a000)]{lang="EN-US"}

[                       module name (12500) module address (0xe00bd000)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Last 5 thread switches : migration/0 (11:16:00.823018)\--\> ]{lang="EN-US"}

[                         swapper (11:16:00.833018)\--\> ]{lang="EN-US"}

[                         kthreadd (11:16:00.833518)\--\> ]{lang="EN-US"}

[                         swapper (11:16:00.833550)\--\> ]{lang="EN-US"}

[                         disk (11:16:00.833560)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Register content:]{lang="EN-US"}

[Reg:       r0, Val = 0x00000000 ; Reg:       r1, Val = 0xe2be5ea0 ;]{lang="EN-US"}

[Reg:       r2, Val = 0x00000000 ; Reg:       r3, Val = 0x77777777 ;]{lang="EN-US"}

[Reg:       r4, Val = 0x00000000 ; Reg:       r5, Val = 0x00001492 ;]{lang="EN-US"}

[Reg:       r6, Val = 0x00000000 ; Reg:       r7, Val = 0x0000ffff ;]{lang="EN-US"}

[Reg:       r8, Val = 0x77777777 ; Reg:       r9, Val = 0x00000000 ;]{lang="EN-US"}

[Reg:      r10, Val = 0x00000001 ; Reg:      r11, Val = 0x0000002c ;]{lang="EN-US"}

[Reg:      r12, Val = 0x057d9484 ; Reg:      r13, Val = 0x00000000 ;]{lang="EN-US"}

[Reg:      r14, Val = 0x00000000 ; Reg:      r15, Val = 0x02000000 ;]{lang="EN-US"}

[Reg:      r16, Val = 0xe2be5f00 ; Reg:      r17, Val = 0x00000000 ;]{lang="EN-US"}

[Reg:      r18, Val = 0x00000000 ; Reg:      r19, Val = 0x00000000 ;]{lang="EN-US"}

[Reg:      r20, Val = 0x024c10f8 ; Reg:      r21, Val = 0x057d9244 ;]{lang="EN-US"}

[Reg:      r22, Val = 0x00002000 ; Reg:      r23, Val = 0x0000002c ;]{lang="EN-US"}

[Reg:      r24, Val = 0x00000002 ; Reg:      r25, Val = 0x24000024 ;]{lang="EN-US"}

[Reg:      r26, Val = 0x00000000 ; Reg:      r27, Val = 0x057d9484 ;]{lang="EN-US"}

[Reg:      r28, Val = 0x0000002c ; Reg:      r29, Val = 0x00000000 ;]{lang="EN-US"}

[Reg:      r30, Val = 0x0000002c ; Reg:      r31, Val = 0x00000000 ;]{lang="EN-US"}

[Reg:       cr, Val = 0x84000028 ; Reg:      nip, Val = 0x057d9550 ;]{lang="EN-US"}

[Reg:      xer, Val = 0x00000000 ; Reg:       lr, Val = 0x0186eff0 ;]{lang="EN-US"}

[Reg:      ctr, Val = 0x682f7344 ; Reg:      msr, Val = 0x00784b5c ;]{lang="EN-US"}

[Reg:     trap, Val = 0x0000b030 ; Reg:      dar, Val = 0x77777777 ;]{lang="EN-US"}

[Reg:    dsisr, Val = 0x40000000 ; Reg:   result, Val = 0x00020300 ;]{lang="EN-US"}

[ ]{lang="EN-US"}

[Dump stack (total 1024 bytes, 16 bytes/line):]{lang="EN-US"}

[0xe2be5ea0: 02 be 5e c0 24 00 00 24 00 00 00 00 05 7d 94 84]{lang="EN-US"}

[0xe2be5eb0: 00 00 00 04 00 00 00 00 00 00 00 28 05 8d 34 c4]{lang="EN-US"}

[0xe2be5ec0: 02 be 60 a0 01 86 ef f0 00 00 00 00 00 00 00 00]{lang="EN-US"}

[0xe2be5ed0: 02 04 05 b4 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[0xe2be5ee0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[0xe2be5ef0: 95 47 73 35 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[0xe2be5f00: a0 e1 64 21 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[0xe2be5f10: 00 00 00 00 00 00 00 00 00 00 00 00 01 e9 00 00]{lang="EN-US"}

[0xe2be5f20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[0xe2be5f30: 00 00 00 00 00 00 00 00 02 be 66 c0 02 be 66 d0]{lang="EN-US"}

[0xe2be5f40: 02 be 61 e0 00 00 00 02 00 00 00 00 02 44 b3 a4]{lang="EN-US"}

[0xe2be5f50: 02 be 5f 90 00 00 00 08 02 be 5f e0 00 00 00 08]{lang="EN-US"}

[0xe2be5f60: 02 be 5f 80 00 ac 1b 14 00 00 00 00 00 00 00 00]{lang="EN-US"}

[0xe2be5f70: 05 b4 5f 90 02 be 5f e0 00 00 00 30 02 be 5f e0]{lang="EN-US"}

[0xe2be5f80: 02 be 5f c0 00 ac 1b f4 00 00 00 00 02 45 00 00]{lang="EN-US"}

[0xe2be5f90: 00 03 00 00 00 00 00 00 02 be 5f e0 00 00 00 30]{lang="EN-US"}

[0xe2be5fa0: 02 be 5f c0 00 ac 1b 14 61 f1 2e ae 02 45 00 00]{lang="EN-US"}

[0xe2be5fb0: 02 44 b3 74 02 be 5f d0 00 00 00 30 02 be 5f e0]{lang="EN-US"}

[0xe2be5fc0: 02 be 60 60 01 74 ff f8 00 00 00 00 00 00 08 00]{lang="EN-US"}

[0xe2be5fd0: 02 be 5f f0 00 e8 93 7e 02 be 5f f8 02 be 5f fc]{lang="EN-US"}

[0xe2be5fe0: 00 00 00 00 00 00 00 00 00 00 00 00 02 be 60 18]{lang="EN-US"}

[0xe2be5ff0: 02 be 60 10 00 e9 65 98 00 00 00 58 00 00 2a 4f]{lang="EN-US"}

[0xe2be6000: 02 be 60 10 00 00 00 00 00 00 00 00 02 be 60 68]{lang="EN-US"}

[0xe2be6010: 02 be 60 40 00 e8 c6 a0 00 00 11 17 00 00 00 00]{lang="EN-US"}

[0xe2be6020: 02 be 60 40 00 00 00 00 00 00 00 00 02 be 60 98]{lang="EN-US"}

[0xe2be6030: 02 27 00 00 00 00 00 00 00 00 00 00 02 be 60 68]{lang="EN-US"}

[0xe2be6040: 02 be 60 60 00 00 00 01 00 00 b0 30 02 be 60 98]{lang="EN-US"}

[0xe2be6050: 00 00 00 04 02 21 00 00 00 00 00 00 01 e9 00 00]{lang="EN-US"}

[0xe2be6060: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[0xe2be6070: 00 00 00 00 00 00 00 00 02 be 66 c0 02 be 66 d0]{lang="EN-US"}

[0xe2be6080: 02 be 61 e0 00 00 00 02 00 00 00 00 02 be 61 70]{lang="EN-US"}

[0xe2be6090: 00 00 00 00 02 21 00 00 05 8d 34 c4 05 7d 92 44]{lang="EN-US"}

[ ]{lang="EN-US"}

[Call trace:]{lang="EN-US"}

[Function Address = 0x8012a4b4]{lang="EN-US"}

[Function Address = 0x8017989c]{lang="EN-US"}

[Function Address = 0x80179b30]{lang="EN-US"}

[Function Address = 0x80127438]{lang="EN-US"}

[Function Address = 0x8012d734]{lang="EN-US"}

[Function Address = 0x80100a00]{lang="EN-US"}

[Function Address = 0xe0071004]{lang="EN-US"}

[Function Address = 0x8016ce0c]{lang="EN-US"}

[Function Address = 0x801223a0]{lang="EN-US"}

[   ]{lang="EN-US"}

[Instruction dump:]{lang="EN-US"}

[41a2fe9c 812300ec 800200ec 7f890000 409efe8c 80010014 540b07b9 40a2fe80]{lang="EN-US"}

[4bfffe6c 80780290 7f64db78 4804ea35 \<807f002c\> 38800000 38a00080 3863000c]{lang="EN-US"}

[[本命令显示信息的详细描述请参见]{style="font-family:宋体"}]{#struct_0_x1063_20800_x137318746}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-2]{lang="EN-US"}](?1665512562#_Ref318724271)[。]{style="font-family:宋体"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1281652978}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ]{lang="EN-US"}**]{#struct_0_x1063_20800_1787977830}**[kernel ]{lang="EN-US"}[starvation]{lang="EN-US"}**
:::

::: {#-1305193890 .myid}
[]{#_Toc404797193}[]{#struct_0_x1063_20800_x228010980}

**进程监控和维护 \-- 进程监控和维护命令 \-- display kernel starvation configuration**

------------------------------------------------------------------------

[**[display kernel starvation configuration]{lang="EN-US"}**]{#struct_0_x1063_20800_1900652}[命令用来显示内核线程的饿死监控参数的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1606626037}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1063_20800_996347100}

[**[display kernel starvation configuration]{lang="EN-US"}**]{#struct_0_x1063_20800_x2111076598}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1063_20800_x1093305797}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display kernel starvation configuration ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_x206159768}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1063_20800_x1914172852}[模式：]{style="font-family:宋体"}

[**[display kernel starvation configuration ]{lang="EN-US"}**[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_x1960501789}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1694334953}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1063_20800_1069520082}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1063_20800_788812593}

[[network-admin]{lang="EN-US"}]{#struct_0_x1063_20800_x57957161}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1063_20800_x2029133874}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x2111142134}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_1360632068}[：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x592298822}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中设备的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_1178239144}[：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x901999373}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1063_20800_354950106}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_x989155243}[显示内核线程饿死监控参数配置。]{style="font-family:宋体"}

[[\<Sysname\> display kernel starvation configuration]{lang="EN-US"}]{#struct_0_x1063_20800_1322290026}

[Thread starvation detection: Enabled]{lang="EN-US"}

[Starvation timer (in seconds): 10]{lang="EN-US"}

[Threads excluded from monitoring: 1]{lang="EN-US"}

[  TID:    123   Name: co0]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display kernel starvation configuration]{lang="EN-US"}]{#struct_0_x1063_20800_x934464480}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2090615251}[[字段]{style="font-family:黑体"}]{#struct_0_x1063_20800_x2111207670}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1063_20800_275621541}

[[Thread starvation detection: Enabled]{lang="EN-US"}]{#struct_0_x1063_20800_359059781}

[[内核线程饿死检测功能处于开启状态]{style="font-family:宋体"}]{#struct_0_x1063_20800_x300563159}

[[Thread starvation detection: Disabled]{lang="EN-US"}]{#struct_0_x1063_20800_x1284342611}

[[内核线程饿死检测功能处于关闭状态]{style="font-family:宋体"}]{#struct_0_x1063_20800_290920648}

[[Starvation timer (in seconds): *n*]{lang="EN-US"}]{#struct_0_x1063_20800_x2110224630}

[[内核线程饿死判定周期（单位为秒）。即如果内核线程在]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_x1063_20800_691574354}[秒内一直不能运行，则判定为饿死]{style="font-family:宋体"}

[[Threads excluded from monitoring]{lang="EN-US"}]{#struct_0_x1063_20800_1187547332}

[[不进行饿死检测的内核线程列表]{style="font-family:宋体"}]{#struct_0_x1063_20800_253285535}

[[Name]{lang="EN-US"}]{#struct_0_x1063_20800_x2081439707}

[[不进行饿死检测的内核线程的名称]{style="font-family:宋体"}]{#struct_0_x1063_20800_2031765557}

[[TID]{lang="EN-US"}]{#struct_0_x1063_20800_x2110290166}

[[不进行饿死检测的内核线程的编号]{style="font-family:宋体"}]{#struct_0_x1063_20800_572922800}

[ ]{lang="EN-US"}

[]{#_Toc174519876}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1068419061}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[monitor kernel]{lang="EN-US"}[ starvation]{lang="EN-US"}**]{#struct_0_x1063_20800_x1915280631}**[ enable]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[monitor kernel]{lang="EN-US"}[ starvation]{lang="EN-US"}**]{#struct_0_x1063_20800_2034981500}**[ exclude-thread]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[monitor kernel]{lang="EN-US"}[ starvation]{lang="EN-US"}**]{#struct_0_x1063_20800_1368887990}**[ time]{lang="EN-US"}**

::: {#1968242870 .myid}
[]{#_Toc404797194}[]{#struct_0_x1063_20800_1134527240}[]{#_Toc316392149}[]{#_Toc329093578}[]{#_Toc329098973}[]{#_Toc329093579}[]{#_Toc329098974}[]{#_Toc329093580}[]{#_Toc329098975}[]{#_Toc329093581}[]{#_Toc329098976}[]{#_Toc329093582}[]{#_Toc329098977}[]{#_Toc329093583}[]{#_Toc329098978}[]{#_Toc329093584}[]{#_Toc329098979}[]{#_Toc329093585}[]{#_Toc329098980}[]{#_Toc329093586}[]{#_Toc329098981}[]{#_Toc329093587}[]{#_Toc329098982}[]{#_Toc329093588}[]{#_Toc329098983}[]{#_Toc329093589}[]{#_Toc329098984}[]{#_Toc329093590}[]{#_Toc329098985}[]{#_Toc329093591}[]{#_Toc329098986}[]{#_Toc329093592}[]{#_Toc329098987}[]{#_Toc329093593}[]{#_Toc329098988}[]{#_Toc329093594}[]{#_Toc329098989}[]{#_Toc329093595}[]{#_Toc329098990}[]{#_Toc329093596}[]{#_Toc329098991}[]{#_Toc329093597}[]{#_Toc329098992}[]{#_Toc329093598}[]{#_Toc329098993}[]{#_Toc329093599}[]{#_Toc329098994}[]{#_Toc329093600}[]{#_Toc329098995}[]{#_Toc329093601}[]{#_Toc329098996}[]{#_Toc329093602}[]{#_Toc329098997}[]{#_Toc329093603}[]{#_Toc329098998}[]{#_Toc329093604}[]{#_Toc329098999}[]{#_Toc329093605}[]{#_Toc329099000}[]{#_Toc329093606}[]{#_Toc329099001}[]{#_Toc329093607}[]{#_Toc329099002}[]{#_Toc329093653}[]{#_Toc329099048}

**进程监控和维护 \-- 进程监控和维护命令 \-- display process**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **process**]{lang="EN-US"}]{#struct_0_x1063_20800_827242147}[命令用来显示进程的状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x2110748921}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1196279096}

[**[display]{lang="EN-US"}**[ **process** \[ **all** \| **job** *job-id* \| **name** *process-name* \]]{lang="EN-US"}]{#struct_0_x1063_20800_1386683017}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1063_20800_x286129516}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **process** \[ **all** \| **job** *job-id* \| **name** *process-name* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_x440134613}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1063_20800_x579649952}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **process** \[ **all** \| **job** *job-id* \| **name** *process-name* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_2010769746}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x435607354}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1063_20800_x43023097}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1063_20800_994697706}

[[network-admin]{lang="EN-US"}]{#struct_0_x1063_20800_x2110814457}

[[network-operator]{lang="EN-US"}]{#struct_0_x1063_20800_x512661702}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1063_20800_x228434365}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1063_20800_63713010}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1848487879}

[**[all]{lang="EN-US"}**]{#struct_0_x1063_20800_1573321800}[：显示所有进程的状态信息。指定]{style="font-family:宋体"}**[all]{lang="EN-US"}**[参数和不指定任何可选参数时，命令行的执行效果相同。]{style="font-family:宋体"}

[**[job ]{lang="EN-US"}***[job-id]{lang="EN-US"}*]{#struct_0_x1063_20800_509132942}[：任务编号，用于唯一标识一个进程，该编号不会随着进程的重启而改变，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}***[ process-name]{lang="EN-US"}*]{#struct_0_x1063_20800_239480411}[：进程名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，不区分大小写，不能包含问号和空格。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x433054319}[：表示单板所在的槽位号，不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x2110879993}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x2011911985}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x125274325}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x2011846449}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x902130445}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1063_20800_284044872}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_927718579}[显示进程]{style="font-family:宋体"}[scmd]{lang="EN-US"}[的状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display process name scmd]{lang="EN-US"}]{#struct_0_x1063_20800_x2110945529}

[                             Job ID: 1]{lang="EN-US"}

[                                PID: 1]{lang="EN-US"}

[                         Parent JID: 0]{lang="EN-US"}

[                         Parent PID: 0]{lang="EN-US"}

[                    Executable path: -]{lang="EN-US"}

[                           Instance: 0]{lang="EN-US"}

[                            Respawn: OFF]{lang="EN-US"}

[                      Respawn count: 1]{lang="EN-US"}

[             Max. spawns per minute: 0]{lang="EN-US"}

[                       Last started: Wed Jun  1 14:45:46 2013]{lang="EN-US"}

[                      Process state: sleeping]{lang="EN-US"}

[                          Max. core: 0]{lang="EN-US"}

[                               ARGS: -]{lang="EN-US"}

[    TID  LAST_CPU    Stack      PRI    State   HH:MM:SS:MESC  Name]{lang="EN-US"}

[      1      0          0K      120      S     0:0:5:220      scmd]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display process name]{lang="EN-US"}]{#struct_0_x1063_20800_x1967417868}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2092647155}[[字段]{style="font-family:黑体"}]{#struct_0_x1063_20800_1822934793}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1063_20800_x431857578}

[[Job ID]{lang="EN-US"}]{#struct_0_x1063_20800_x1719237309}

[[任务编号，用于唯一标识一个进程，该编号不会随着进程的重启而改变]{style="font-family:宋体"}]{#struct_0_x1063_20800_1946675452}

[[PID]{lang="EN-US"}]{#struct_0_x1063_20800_1146545598}

[[进程编号，用于标识一个进程，但该编号可能会随着进程的重启而改变]{style="font-family:宋体"}]{#struct_0_x1063_20800_x2111011065}

[[Parent JID]{lang="EN-US"}]{#struct_0_x1063_20800_x2059633047}

[[父进程的任务编号]{style="font-family:宋体"}]{#struct_0_x1063_20800_1971836039}

[[Parent PID]{lang="EN-US"}]{#struct_0_x1063_20800_181464994}

[[父进程的进程编号]{style="font-family:宋体"}]{#struct_0_x1063_20800_220673308}

[[Executable path]{lang="EN-US"}]{#struct_0_x1063_20800_1684578983}

[[进程执行路径（内核线程执行路径显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_x1063_20800_x2111076601}["）]{style="font-family:宋体"}

[[Instance]{lang="EN-US"}]{#struct_0_x1063_20800_117137605}

[[进程的实例号（一个进程根据需要在软件实现时决定了它是否会运行多个实例）]{style="font-family:宋体"}]{#struct_0_x1063_20800_x330436407}

[[Respawn]{lang="EN-US"}]{#struct_0_x1063_20800_x1814693539}

[[运行出错时，该进程是否会自动重启：]{style="font-family:宋体"}]{#struct_0_x1063_20800_x823404524}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ON]{lang="EN-US"}]{#struct_0_x1063_20800_1115107054}[表示自动重启]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OFF]{lang="EN-US"}]{#struct_0_x1063_20800_x2111142137}[表示不自动重启]{style="font-family:宋体"}

[[Respawn count]{lang="EN-US"}]{#struct_0_x1063_20800_x1368251287}

[[进程重启的次数（初始值为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x1063_20800_x1155680957}[）]{style="font-family:宋体"}

[[Max. spawns per minute]{lang="EN-US"}]{#struct_0_x1063_20800_x30594226}

[[进程一分钟内允许异常重启的最大次数（如果进程在一分钟内异常重启次数超过该值，则系统会自动关闭该进程）]{style="font-family:宋体"}]{#struct_0_x1063_20800_x353367925}

[[Last started]{lang="EN-US"}]{#struct_0_x1063_20800_x2111207673}

[[进程最近一次启动的日期和时间]{style="font-family:宋体"}]{#struct_0_x1063_20800_1841705482}

[[Process state]{lang="EN-US"}]{#struct_0_x1063_20800_x192158308}

[[进程状态，可能的取值为：]{style="font-family:宋体"}]{#struct_0_x1063_20800_1426030794}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[running]{lang="EN-US"}]{#struct_0_x1063_20800_x1125829673}[：运行状态或正在队列中等待调度]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sleeping]{lang="EN-US"}]{#struct_0_x1063_20800_x2110224633}[：]{style="font-family:宋体"}[可中断睡眠状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[traced or stopped]{lang="EN-US"}]{#struct_0_x1063_20800_288289827}[：]{style="font-family:宋体"}[暂停状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[uninterruptible sleep]{lang="EN-US"}]{#struct_0_x1063_20800_x1474247400}[：]{style="font-family:宋体"}[不可中断睡眠状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[zombie]{lang="EN-US"}]{#struct_0_x1063_20800_x1051586382}[：]{style="font-family:宋体"}[僵死状态]{lang="EN-US" style="font-family:宋体"}[（僵死状态指的是进程已经退出，但是仍然占用部分资源的状态）]{style="font-family:宋体"}

[[Max. core]{lang="EN-US"}]{#struct_0_x1063_20800_x2110290169}

[[进程最多可以生成的]{style="font-family:宋体"}[core]{lang="EN-US"}]{#struct_0_x1063_20800_x1349391501}[文件的数量，如果为]{style="font-family:宋体"}[0]{lang="EN-US"}[表示不生成]{style="font-family:宋体"}[core]{lang="EN-US"}[文件（进程异常重启一次，会产生一个]{style="font-family:宋体"}[core]{lang="EN-US"}[文件。如果生成的]{style="font-family:宋体"}[core]{lang="EN-US"}[文件的数目达到最大值，则不再生成]{style="font-family:宋体"}[core]{lang="EN-US"}[文件。软件开发和维护人员能够根据]{style="font-family:宋体"}[core]{lang="EN-US"}[文件的内容来定位异常的原因和异常的位置）]{style="font-family:宋体"}

[[ARGS]{lang="EN-US"}]{#struct_0_x1063_20800_x1536188344}

[[进程启动时携带的参数。如果进程不带参数，显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_x1063_20800_836866365}["]{style="font-family:宋体"}

[[TID]{lang="EN-US"}]{#struct_0_x1063_20800_x2110748920}

[[线程编号]{style="font-family:宋体"}]{#struct_0_x1063_20800_369804845}

[[LAST_CPU]{lang="EN-US"}]{#struct_0_x1063_20800_x1124422833}

[[进程最近一次被调度时，所在的]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_x1063_20800_x450562799}

[[Stack]{lang="EN-US"}]{#struct_0_x1063_20800_x2110814456}

[[堆栈大小]{style="font-family:宋体"}]{#struct_0_x1063_20800_x2078745643}

[[PRI]{lang="EN-US"}]{#struct_0_x1063_20800_627621633}

[[线程优先级]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1809394975}

[[State]{lang="EN-US"}]{#struct_0_x1063_20800_x2110879992}

[[线程状态，可能的取值为：]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1691358266}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[R]{lang="EN-US"}]{#struct_0_x1063_20800_x322158311}[：]{style="font-family:宋体"}[running]{lang="EN-US"}[，运行状态或正在队列中等待调度]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S]{lang="EN-US"}]{#struct_0_x1063_20800_x2110945528}[：]{lang="EN-US" style="font-family:宋体"}[sleeping]{lang="EN-US"}[，可中断睡眠状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_x1063_20800_x401333927}[：]{lang="EN-US" style="font-family:宋体"}[traced or stopped]{lang="EN-US"}[，暂停状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_x1063_20800_1939438696}[：]{lang="EN-US" style="font-family:宋体"}[uninterruptible sleep]{lang="EN-US"}[，不可中断睡眠状态]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Z]{lang="EN-US"}]{#struct_0_x1063_20800_x1367295626}[：]{lang="EN-US" style="font-family:宋体"}[zombie]{lang="EN-US"}[，僵死状态]{lang="EN-US" style="font-family:宋体"}

[[HH:MM:SS:MESC]{lang="EN-US"}]{#struct_0_x1063_20800_x2111011064}

[[进程最近一次启动后的运行时间]{style="font-family:宋体"}]{#struct_0_x1063_20800_669250308}

[[Name]{lang="EN-US"}]{#struct_0_x1063_20800_x742531959}

[[进程名称]{style="font-family:宋体"}]{#struct_0_x1063_20800_x2111076600}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_x1448946336}[显示所有进程的状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display process all]{lang="EN-US"}]{#struct_0_x1063_20800_x2111142136}

[    JID    PID %CPU %MEM STAT PRI     TTY HH:MM:SS COMMAND]{lang="EN-US"}

[      1      1  0.0  0.0   S  120      -  00:00:04 scmd]{lang="EN-US"}

[      2      2  0.0  0.0   S  115      -  00:00:00 \[kthreadd\]]{lang="EN-US"}

[      3      3  0.0  0.0   S   99      -  00:00:00 \[migration/0\]]{lang="EN-US"}

[      4      4  0.0  0.0   S  115      -  00:00:05 \[ksoftirqd/0\]]{lang="EN-US"}

[      5      5  0.0  0.0   S   99      -  00:00:00 \[watchdog/0\]]{lang="EN-US"}

[      6      6  0.0  0.0   S  115      -  00:00:00 \[events/0\]]{lang="EN-US"}

[      7      7  0.0  0.0   S  115      -  00:00:00 \[khelper\]]{lang="EN-US"}

[      8      8  0.0  0.0   S  115      -  00:00:00 \[kblockd/0\]]{lang="EN-US"}

[      9      9  0.0  0.0   S  115      -  00:00:00 \[ata/0\]]{lang="EN-US"}

[     10     10  0.0  0.0   S  115      -  00:00:00 \[ata_aux\]]{lang="EN-US"}

[     11     11  0.0  0.0   S  115      -  00:00:00 \[kseriod\]]{lang="EN-US"}

[     12     12  0.0  0.0   S  120      -  00:00:00 \[vzmond\]]{lang="EN-US"}

[     13     13  0.0  0.0   S  120      -  00:00:00 \[pdflush\]]{lang="EN-US"}

[     14     14  0.0  0.0   S  120      -  00:00:00 \[pdflush\]]{lang="EN-US"}

[     15     15  0.0  0.0   S  115      -  00:00:00 \[kswapd0\]]{lang="EN-US"}

[     16     16  0.0  0.0   S  115      -  00:00:00 \[aio/0\]]{lang="EN-US"}

[     17     17  0.0  0.0   S  115      -  00:00:00 \[scsi_eh_0\]]{lang="EN-US"}

[     18     18  0.0  0.0   S  115      -  00:00:00 \[scsi_eh_1\]]{lang="EN-US"}

[     19     19  0.0  0.0   S  115      -  00:00:00 \[scsi_eh_2\]]{lang="EN-US"}

[     35     35  0.0  0.0   D  100      -  00:00:00 \[lipc_topology\]]{lang="EN-US"}

[\-\-\-- More \-\-\--               ]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display process all]{lang="EN-US"}]{#struct_0_x1063_20800_197832654}[命令显示信息描述]{style="font-family:黑体"}

[]{#table_struct_0_2081831091}[[字段]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1921453880}

[[描述]{style="font-family:黑体"}]{#struct_0_x1063_20800_1798538012}

[[JID]{lang="EN-US"}]{#struct_0_x1063_20800_x585583824}

[[任务编号，用于唯一标识一个进程，该编号不会随着进程的重启而改变]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1449013199}

[[PID]{lang="EN-US"}]{#struct_0_x1063_20800_x421152029}

[[进程编号]{style="font-family:宋体"}]{#struct_0_x1063_20800_839707145}

[[%CPU]{lang="EN-US"}]{#struct_0_x1063_20800_x2111207672}

[[CPU]{lang="EN-US"}]{#struct_0_x1063_20800_x887177873}[使用率（用百分比表示）]{style="font-family:宋体"}

[[%MEM]{lang="EN-US"}]{#struct_0_x1063_20800_918069811}

[[内存使用率（用百分比表示）]{style="font-family:宋体"}]{#struct_0_x1063_20800_x536154113}

[[STAT]{lang="EN-US"}]{#struct_0_x1063_20800_799674274}

[[进程状态，可能的取值为：]{style="font-family:宋体"}]{#struct_0_x1063_20800_x2110224632}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[R]{lang="EN-US"}]{#struct_0_x1063_20800_1854373768}[：]{style="font-family:宋体"}[running]{lang="EN-US"}[，运行状态或处于运行队列]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S]{lang="EN-US"}]{#struct_0_x1063_20800_49137505}[：]{lang="EN-US" style="font-family:宋体"}[sleeping]{lang="EN-US"}[，可中断睡眠状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_x1063_20800_x157616950}[：]{lang="EN-US" style="font-family:宋体"}[traced or stopped]{lang="EN-US"}[，暂停状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_x1063_20800_1562326828}[：]{lang="EN-US" style="font-family:宋体"}[uninterruptible sleep]{lang="EN-US"}[，不可中断睡眠状态]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Z]{lang="EN-US"}]{#struct_0_x1063_20800_342953870}[：]{lang="EN-US" style="font-family:宋体"}[zombie]{lang="EN-US"}[，僵死状态]{lang="EN-US" style="font-family:宋体"}

[[PRI]{lang="EN-US"}]{#struct_0_x1063_20800_x2110290168}

[[进程优先级（优先级在进程调度时发挥作用，优先级高的会优先得到调度）]{style="font-family:宋体"}]{#struct_0_x1063_20800_1379491854}

[[TTY]{lang="EN-US"}]{#struct_0_x1063_20800_523091939}

[[进程使用的终端（在非缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_x1063_20800_x83872954}[内该项总显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["）]{style="font-family:宋体"}

[[HH:MM:SS]{lang="EN-US"}]{#struct_0_x1063_20800_1573196527}

[[进程最近一次启动后的运行时间]{style="font-family:宋体"}]{#struct_0_x1063_20800_x2110748923}

[[COMMAND]{lang="EN-US"}]{#struct_0_x1063_20800_1935888786}

[[进程名称以及进程运行的参数（如果进程名称带有"]{style="font-family:宋体"}[\[ \]]{lang="EN-US"}]{#struct_0_x1063_20800_1263450355}["标记，则表示内核线程）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#550853952 .myid}
[]{#_Toc404797195}[]{#struct_0_x1063_20800_1079726915}[]{#_Toc316392150}

**进程监控和维护 \-- 进程监控和维护命令 \-- display process cpu**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **process cpu**]{lang="EN-US"}]{#struct_0_x1063_20800_476966985}[命令用来显示所有进程的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[使用率信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x254079148}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1063_20800_545792478}

[**[display]{lang="EN-US"}**[ **process** **cpu**]{lang="EN-US"}]{#struct_0_x1063_20800_x2110814459}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1063_20800_1006368072}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **process** **cpu** \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_601278692}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1063_20800_x1317023791}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **process** **cpu** \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_1387936407}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x664117375}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1703653126}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1063_20800_882333183}

[[network-admin]{lang="EN-US"}]{#struct_0_x1063_20800_1919992418}

[[network-operator]{lang="EN-US"}]{#struct_0_x1063_20800_x2110879995}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1063_20800_x1288073739}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1063_20800_x190519806}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1517482861}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x348507304}[：表示单板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x1929958685}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x2011715384}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_834140766}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x1823599122}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x902589197}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1441930793}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_1223571469}[显示所有进程]{style="font-family:宋体"}[CPU]{lang="EN-US"}[使用率信息。]{style="font-family:宋体"}

[[\<Sysname\> display process cpu]{lang="EN-US"}]{#struct_0_x1063_20800_x2110945531}

[CPU utilization in 5 secs: 16.8%; 1 min: 4.7%; 5 mins: 4.7%]{lang="EN-US"}

[    JID      5Sec      1Min      5Min    Name]{lang="EN-US"}

[      1      0.0%      0.0%      0.0%    scmd]{lang="EN-US"}

[      2      0.0%      0.0%      0.0%    \[kthreadd\]]{lang="EN-US"}

[      3      0.1%      0.0%      0.0%    \[ksoftirqd/0\]]{lang="EN-US"}

[      4      0.0%      0.0%      0.0%    \[watchdog/0\]]{lang="EN-US"}

[      5      0.0%      0.0%      0.0%    \[events/0\]]{lang="EN-US"}

[      6      0.0%      0.0%      0.0%    \[khelper\]]{lang="EN-US"}

[     29      0.0%      0.0%      0.0%    \[kblockd/0\]]{lang="EN-US"}

[     49      0.0%      0.0%      0.0%    \[vzmond\]]{lang="EN-US"}

[     52      0.0%      0.0%      0.0%    \[pdflush\]]{lang="EN-US"}

[     53      0.0%      0.0%      0.0%    \[pdflush\]]{lang="EN-US"}

[     54      0.0%      0.0%      0.0%    \[kswapd0\]]{lang="EN-US"}

[    110      0.0%      0.0%      0.0%    \[aio/0\]]{lang="EN-US"}

[    712      0.0%      0.0%      0.0%    \[mtdblockd\]]{lang="EN-US"}

[    719      0.0%      0.0%      0.0%    \[TNetJob\]]{lang="EN-US"}

[    720      0.0%      0.0%      0.0%    \[TMTH\]]{lang="EN-US"}

[    727      0.0%      0.0%      0.0%    \[CF\]]{lang="EN-US"}

[    730      0.0%      0.0%      0.0%    \[DIBC\]]{lang="EN-US"}

[    752      0.0%      0.0%      0.0%    \[lipc_topology\]]{lang="EN-US"}

[    762      0.0%      0.0%      0.0%    \[MNET\]]{lang="EN-US"}

[    763      0.0%      0.0%      0.0%    \[SYSM\]]{lang="EN-US"}

[\-\-\-- More \-\-\--]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display process cpu ]{lang="EN-US"}]{#struct_0_x1063_20800_x1611121972}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2082834739}[[字段]{style="font-family:黑体"}]{#struct_0_x1063_20800_x2111011067}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1063_20800_x896833633}

[[CPU utilization in 5 secs: 16.8%; 1 min: 4.7%; 5 mins: 4.7%]{lang="EN-US"}]{#struct_0_x1063_20800_1868810457}

[[系统最近]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_x1063_20800_x253930809}[秒]{style="font-family:宋体"}[CPU]{lang="EN-US"}[使用率；最近]{style="font-family:宋体"}[1]{lang="EN-US"}[分钟]{style="font-family:宋体"}[CPU]{lang="EN-US"}[使用率；最近]{style="font-family:宋体"}[5]{lang="EN-US"}[分钟]{style="font-family:宋体"}[CPU]{lang="EN-US"}[使用率]{style="font-family:宋体"}

[[JID]{lang="EN-US"}]{#struct_0_x1063_20800_x424611090}

[[任务编号（用于唯一标识一个进程，该编号不会随着进程的重启而改变）]{style="font-family:宋体"}]{#struct_0_x1063_20800_x2145814980}

[[5Sec]{lang="EN-US"}]{#struct_0_x1063_20800_x2111076603}

[[最近]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_x1063_20800_x1045661809}[秒钟内进程的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[使用率]{style="font-family:宋体"}

[[1Min]{lang="EN-US"}]{#struct_0_x1063_20800_1614405295}

[[最近]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x1063_20800_79913594}[分钟内进程的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[使用率]{style="font-family:宋体"}

[[5Min]{lang="EN-US"}]{#struct_0_x1063_20800_x146985290}

[[最近]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_x1063_20800_251769835}[分钟内进程的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[使用率]{style="font-family:宋体"}

[[Name]{lang="EN-US"}]{#struct_0_x1063_20800_x2111142139}

[[进程名称（如果进程名称带有"]{style="font-family:宋体"}[\[ \]]{lang="EN-US"}]{#struct_0_x1063_20800_1407686235}["标记，则表示该进程为内核线程）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1322505631 .myid}
[]{#_Toc174519877}[]{#_Toc404797196}[]{#struct_0_x1063_20800_1512967387}[]{#_Toc316392151}

**进程监控和维护 \-- 进程监控和维护命令 \-- display process log**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **process log**]{lang="EN-US"}]{#struct_0_x1063_20800_1698855072}[命令用来显示所有用户态进程的日志信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x405817988}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1063_20800_509759423}

[**[display]{lang="EN-US"}**[ **process** **log**]{lang="EN-US"}]{#struct_0_x1063_20800_x1764877703}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1063_20800_x1975284068}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **process** **log** \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_x2111207675}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1063_20800_678906068}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **process** **log** \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_x1137223180}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1063_20800_737122140}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1063_20800_1136961188}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1063_20800_674668385}

[[network-admin]{lang="EN-US"}]{#struct_0_x1063_20800_x893865846}

[[network-operator]{lang="EN-US"}]{#struct_0_x1063_20800_x1378646922}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1063_20800_776664148}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1063_20800_x2110224635}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1094858881}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_1952101077}[：表示单板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x1982111308}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x2010928952}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x39869318}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x1508980578}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x902064908}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1838067298}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_1860077791}[显示所有用户态进程的日志信息。]{style="font-family:宋体"}

[[\<Sysname\> display process log]{lang="EN-US"}]{#struct_0_x1063_20800_x2110290171}

[Name          JID    PID    Abort Core Start-time          End-time]{lang="EN-US"}

[mdcd          135    135    N     N    2013-06-11 09:31:00 2013-06-11 09:31:00]{lang="EN-US"}

[knotify       156    156    N     N    2013-06-11 09:31:02 2013-06-11 09:31:02]{lang="EN-US"}

[knotify       158    158    N     N    2013-06-11 09:31:02 2013-06-11 09:31:02]{lang="EN-US"}

[knotify       195    195    N     N    2013-06-11 09:31:03 2013-06-11 09:31:03]{lang="EN-US"}

[pkg_update    203    203    N     N    2013-06-11 09:31:06 2013-06-11 09:31:06]{lang="EN-US"}

[autocfgd      219    219    N     N    2013-06-11 09:31:13 2013-06-11 09:31:13]{lang="EN-US"}

[comsh         202    202    N     N    2013-06-11 09:31:05 2013-06-11 09:31:13]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display process log]{lang="EN-US"}]{#struct_0_x1063_20800_x993226677}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2110199795}[[字段]{style="font-family:黑体"}]{#struct_0_x1063_20800_1904610994}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1063_20800_1087382447}

[[Name]{lang="EN-US"}]{#struct_0_x1063_20800_1651412571}

[[用户态进程名]{style="font-family:宋体"}]{#struct_0_x1063_20800_576535381}

[[JID]{lang="EN-US"}]{#struct_0_x1063_20800_1637523642}

[[用户态进程任务编号]{style="font-family:宋体"}]{#struct_0_x1063_20800_x2110748922}

[[PID]{lang="EN-US"}]{#struct_0_x1063_20800_x792994569}

[[用户态进程编号]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1737492237}

[[Abort]{lang="EN-US"}]{#struct_0_x1063_20800_682239741}

[[是否异常退出：]{style="font-family:宋体"}]{#struct_0_x1063_20800_759472412}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Y]{lang="EN-US"}]{#struct_0_x1063_20800_x571469617}[表示]{lang="EN-US" style="font-family:宋体"}[异常]{style="font-family:宋体"}[退出]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N]{lang="EN-US"}]{#struct_0_x1063_20800_x2110814458}[表示]{lang="EN-US" style="font-family:宋体"}[正常]{style="font-family:宋体"}[退出]{lang="EN-US" style="font-family:宋体"}

[[Core]{lang="EN-US"}]{#struct_0_x1063_20800_x559715869}

[[是否产生]{style="font-family:宋体"}[core]{lang="EN-US"}]{#struct_0_x1063_20800_x1647006810}[文件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Y]{lang="EN-US"}]{#struct_0_x1063_20800_1959512800}[表示产生]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N]{lang="EN-US"}]{#struct_0_x1063_20800_x1261421768}[表示未产生]{lang="EN-US" style="font-family:宋体"}

[[Start-time]{lang="EN-US"}]{#struct_0_x1063_20800_x2110879994}

[[用户态进程创建时间]{style="font-family:宋体"}]{#struct_0_x1063_20800_1440809616}

[[End-time]{lang="EN-US"}]{#struct_0_x1063_20800_542137408}

[[用户态进程结束时间]{style="font-family:宋体"}]{#struct_0_x1063_20800_1643466891}

[ ]{lang="EN-US"}

::: {#-1080320674 .myid}
[]{#_Toc404797197}[]{#struct_0_x1063_20800_x1196390472}[]{#_Toc316392152}

**进程监控和维护 \-- 进程监控和维护命令 \-- display process memory**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **process memory**]{lang="EN-US"}]{#struct_0_x1063_20800_1827336007}[命令用来显示所有用户态进程的代码段、数据段以及堆栈等的内存使用信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_94456525}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1063_20800_x2110945530}

[**[display]{lang="EN-US"}**[ **process** **memory**]{lang="EN-US"}]{#struct_0_x1063_20800_x45038031}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1063_20800_1844245033}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **process** **memory** \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_317449796}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1063_20800_1783526418}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **process** **memory** \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_51273731}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1903591795}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1063_20800_1584109547}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1065203943}

[[network-admin]{lang="EN-US"}]{#struct_0_x1063_20800_x2111011066}

[[network-operator]{lang="EN-US"}]{#struct_0_x1063_20800_1832049722}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1063_20800_816399706}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1063_20800_1349295807}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1661540793}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x94734683}[：表示单板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_612446640}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x2011649847}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_1183778043}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x2011584311}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x902130444}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x907596639}

[[用户态进程启动时，会向系统申请]{style="font-family:宋体"}[Text]{lang="EN-US"}]{#struct_0_x1063_20800_1362090616}[、]{style="font-family:宋体"}[Data]{lang="EN-US"}[、]{style="font-family:宋体"}[Stack]{lang="EN-US"}[和]{style="font-family:宋体"}[Dynamic]{lang="EN-US"}[类型的内存。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Text]{lang="EN-US"}]{#struct_0_x1063_20800_x2111076602}[类型的内存用来存放用户态进程的代码。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Data]{lang="EN-US"}]{#struct_0_x1063_20800_1683221546}[类型的内存用来存放用户态进程的数据。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stack]{lang="EN-US"}]{#struct_0_x1063_20800_x503780270}[内存指的是栈内存，一般存放临时数据。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Dynamic]{lang="EN-US"}]{#struct_0_x1063_20800_x394858107}[类型的内存指的是堆内存（]{lang="EN-US" style="font-family:宋体"}[heap]{lang="EN-US"}[），由系统根据用户态进程运行需要进行动态分配（]{lang="EN-US" style="font-family:宋体"}[malloc]{lang="EN-US"}[）和释放（]{lang="EN-US" style="font-family:宋体"}[free]{lang="EN-US"}[），可使用]{lang="EN-US" style="font-family:宋体"}**[display process memory heap]{lang="EN-US"}**[命令显示]{lang="EN-US" style="font-family:宋体"}[Dynamic]{lang="EN-US"}[类型内存的详细信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1185579473}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_1950041741}[显示所有用户态进程的内存使用信息。]{style="font-family:宋体"}

[[\<Sysname\> display process memory]{lang="EN-US"}]{#struct_0_x1063_20800_x2111142138}

[   JID       Text      Data      Stack    Dynamic    Name]{lang="EN-US"}

[     1        384      1800         16         36    scmd]{lang="EN-US"}

[     2          0         0          0          0    \[kthreadd\]]{lang="EN-US"}

[     3          0         0          0          0    \[ksoftirqd/0\]]{lang="EN-US"}

[     4          0         0          0          0    \[watchdog/0\]]{lang="EN-US"}

[     5          0         0          0          0    \[events/0\]]{lang="EN-US"}

[     6          0         0          0          0    \[khelper\]]{lang="EN-US"}

[    29          0         0          0          0    \[kblockd/0\]]{lang="EN-US"}

[    49          0         0          0          0    \[vzmond\]]{lang="EN-US"}

[    52          0         0          0          0    \[pdflush\]]{lang="EN-US"}

[\-\-\-- More \-\-\--]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[display process memory]{lang="EN-US"}]{#struct_0_x1063_20800_x1321197120}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2112855955}[[字段]{style="font-family:黑体"}]{#struct_0_x1063_20800_1209471999}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1063_20800_x884959224}

[[JID]{lang="EN-US"}]{#struct_0_x1063_20800_733091088}

[[任务编号。用于唯一标识一个用户态进程，该编号不会随着用户态进程的重启而改变]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1410990986}

[[Text]{lang="EN-US"}]{#struct_0_x1063_20800_x2111207674}

[[用户态进程占用的代码段大小，单位为]{style="font-family:宋体"}[KB]{lang="EN-US"}]{#struct_0_x1063_20800_x2049977287}[（内核线程该项大小为]{style="font-family:宋体"}[0]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Data]{lang="EN-US"}]{#struct_0_x1063_20800_x187101724}

[[用户态进程占用的数据段大小，单位为]{style="font-family:宋体"}[KB]{lang="EN-US"}]{#struct_0_x1063_20800_x1665156864}[（内核线程该项大小为]{style="font-family:宋体"}[0]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Stack]{lang="EN-US"}]{#struct_0_x1063_20800_x1151611668}

[[用户态进程占用的堆栈大小，单位为]{style="font-family:宋体"}[KB]{lang="EN-US"}]{#struct_0_x1063_20800_x2087723299}[（内核线程该项大小为]{style="font-family:宋体"}[0]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Dynamic]{lang="EN-US"}]{#struct_0_x1063_20800_x2110224634}

[[用户态进程动态申请内存大小，单位为]{style="font-family:宋体"}[KB]{lang="EN-US"}]{#struct_0_x1063_20800_x1634024474}[（内核线程该项大小为]{style="font-family:宋体"}[0]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Name]{lang="EN-US"}]{#struct_0_x1063_20800_x1060435901}

[[用户态进程名称（如果用户态进程名称带有"]{style="font-family:宋体"}[\[ \]]{lang="EN-US"}]{#struct_0_x1063_20800_x1622623125}["标记，则表示该进程为内核线程）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_532714241}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display process memory heap]{lang="EN-US"}**]{#struct_0_x1063_20800_810683380}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display process memory heap address]{lang="EN-US"}**]{#struct_0_x1063_20800_83872224}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display process memory heap size]{lang="EN-US"}**]{#struct_0_x1063_20800_x2110290170}

::: {#-1633354861 .myid}
[]{#_Toc404797198}[]{#struct_0_x1063_20800_1735656678}[]{#_Toc316392153}

**进程监控和维护 \-- 进程监控和维护命令 \-- display process memory heap**

------------------------------------------------------------------------

[**[display process memory heap]{lang="EN-US"}**]{#struct_0_x1063_20800_1128541085}[命令用来显示指定用户态进程的堆内存统计信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1211062304}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1063_20800_978569827}

[**[display process memory heap job ]{lang="EN-US"}***[job-id]{lang="EN-US"}*[ \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x1063_20800_x1566511110}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1063_20800_262887483}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display process memory heap job ]{lang="EN-US"}***[job-id ]{lang="EN-US"}*[\[ **verbose** \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_x638823545}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1063_20800_1461278637}[模式：]{style="font-family:宋体"}

[**[display process memory heap job ]{lang="EN-US"}***[job-id ]{lang="EN-US"}*[\[ **verbose** \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_x188434618}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1063_20800_81467221}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1063_20800_460409769}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x477336386}

[[network-admin]{lang="EN-US"}]{#struct_0_x1063_20800_1974058440}

[[network-operator]{lang="EN-US"}]{#struct_0_x1063_20800_1136693299}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1063_20800_x137197189}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1063_20800_x104823753}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x223052474}

[**[job ]{lang="EN-US"}***[job-id]{lang="EN-US"}*]{#struct_0_x1063_20800_x188500154}[：任务编号，用于唯一标识一个用户态进程，该编号不会随着用户态进程的重启而改变。取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1063_20800_1244349648}**[：]{style="font-family:宋体"}**[显示内存详细统计信息。不指定该参数时，显示内存概要统计信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x1552917144}[：表示单板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x658669060}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x2011846455}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x2010994487}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_1125106999}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x902458124}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1192615159}

[[系统的堆内存由固定大小（比如]{style="font-family:宋体"}[size=16]{lang="EN-US"}]{#struct_0_x1063_20800_88601997}[字节、]{style="font-family:宋体"}[size=64]{lang="EN-US"}[字节等）的内存块构成，用于存放用户态进程运行过程中需要用到的数据或者中间变量。当用户态进程启动时，系统会根据用户态进程运行需要，给用户态进程动态分配堆内存。用户态进程的堆内存信息可使用]{style="font-family:宋体"}**[display process memory heap]{lang="EN-US"}**[命令显示。]{style="font-family:宋体"}

[[每个内存块都有地址，该地址用十六进制数表示，可通过]{style="font-family:宋体"}**[display process memory heap size]{lang="EN-US"}**]{#struct_0_x1063_20800_1785205914}[命令显示。用户使用内存块的地址可以访问内存块，获取内存块的内容，内存块的内容可通过]{style="font-family:宋体"}**[display process memory heap address]{lang="EN-US"}**[命令显示。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x418398533}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_x188565690}[显示]{style="font-family:宋体"}[job 148]{lang="EN-US"}[的堆内存概要统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display process memory heap job 148]{lang="EN-US"}]{#struct_0_x1063_20800_x1486386213}

[Total virtual memory heap space(in bytes) :  2228224]{lang="EN-US"}

[Total physical memory heap space(in bytes) :  262144]{lang="EN-US"}

[Total allocated memory(in bytes)          :  161576]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_x451663150}[显示]{style="font-family:宋体"}[job 148]{lang="EN-US"}[的堆内存详细统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display process memory heap job 148 verbose]{lang="EN-US"}]{#struct_0_x1063_20800_x188631226}

[Heap usage:]{lang="EN-US"}

[Size       Free      Used     Total     Free Ratio]{lang="EN-US"}

[16         8         52       60        13%]{lang="EN-US"}

[64         3         1262     1265      0.2%]{lang="EN-US"}

[128        2         207      209       1%]{lang="EN-US"}

[512        3         55       58        5.1%]{lang="EN-US"}

[4096       3         297      300       1%]{lang="EN-US"}

[8192       1         19       20        5%]{lang="EN-US"}

[81920      0         1        1         0%]{lang="EN-US"}

[Summary:]{lang="EN-US"}

[Total virtual memory heap space (in bytes)  :  2293760]{lang="EN-US"}

[Total physical memory heap space (in bytes) :  58368]{lang="EN-US"}

[Total allocated memory (in bytes)           :  42368]{lang="EN-US"}

[[以上显示信息表明：]{style="font-family:宋体"}[job 148]{lang="EN-US"}]{#struct_0_x1063_20800_1250081221}[分得]{style="font-family:宋体"}[size]{lang="EN-US"}[大小]{style="font-family:宋体"}[16]{lang="EN-US"}[字节的内存块]{style="font-family:宋体"}[60]{lang="EN-US"}[个（已用]{style="font-family:宋体"}[52]{lang="EN-US"}[个，还有]{style="font-family:宋体"}[8]{lang="EN-US"}[个未使用），]{style="font-family:宋体"}[size]{lang="EN-US"}[大小为]{style="font-family:宋体"}[64]{lang="EN-US"}[字节的内存块]{style="font-family:宋体"}[1265]{lang="EN-US"}[个（已用]{style="font-family:宋体"}[1262]{lang="EN-US"}[个，还有]{style="font-family:宋体"}[3]{lang="EN-US"}[个未使用），以此类推。]{style="font-family:宋体"}

[[表1-11 ]{lang="EN-US"}[display process memory heap]{lang="EN-US"}]{#struct_0_x1063_20800_1217507448}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2106356499}[[命令字]{style="font-family:黑体"}]{#struct_0_x1063_20800_x128157415}
:::

[[功能描述]{style="font-family:黑体"}]{#struct_0_x1063_20800_1149930555}

[[Total virtual memory heap space(in bytes)]{lang="EN-US"}]{#struct_0_x1063_20800_2055357108}

[[虚拟堆内存总大小，单位为字节]{style="font-family:宋体"}]{#struct_0_x1063_20800_1536223152}

[[Total physical memory heap space(in bytes)]{lang="EN-US"}]{#struct_0_x1063_20800_1561299452}

[[物理堆内存总大小，单位为字节]{style="font-family:宋体"}]{#struct_0_x1063_20800_x188696762}

[[Total allocated memory(in bytes)]{lang="EN-US"}]{#struct_0_x1063_20800_1236348516}

[[任务已使用的堆内存大小，单位为字节]{style="font-family:宋体"}]{#struct_0_x1063_20800_292600343}

[[Size]{lang="EN-US"}]{#struct_0_x1063_20800_625771827}

[[内存块大小，单位为字节]{style="font-family:宋体"}]{#struct_0_x1063_20800_1611377498}

[[Free]{lang="EN-US"}]{#struct_0_x1063_20800_x1206027815}

[[空闲的内存块个数]{style="font-family:宋体"}]{#struct_0_x1063_20800_x188762298}

[[Used]{lang="EN-US"}]{#struct_0_x1063_20800_1650416608}

[[已使用的内存块个数]{style="font-family:宋体"}]{#struct_0_x1063_20800_x576296726}

[[Total]{lang="EN-US"}]{#struct_0_x1063_20800_x1417953924}

[[指定大小内存块总个数，为]{style="font-family:宋体"}[Free]{lang="EN-US"}]{#struct_0_x1063_20800_x941819762}[和]{style="font-family:宋体"}[Used]{lang="EN-US"}[之和]{style="font-family:宋体"}

[[Free Ratio]{lang="EN-US"}]{#struct_0_x1063_20800_x188827834}

[[Free]{lang="EN-US"}]{#struct_0_x1063_20800_35562304}[与]{style="font-family:宋体"}[Total]{lang="EN-US"}[的比率，可以反映这种大小内存块的碎片情况]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1344476432}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display process memory]{lang="EN-US"}**]{#struct_0_x1063_20800_642287537}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display process memory heap address]{lang="EN-US"}**]{#struct_0_x1063_20800_x2012825199}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display process memory heap size]{lang="EN-US"}**]{#struct_0_x1063_20800_x1649230281}

::: {#-2138533078 .myid}
[]{#_Toc404797199}[]{#struct_0_x1063_20800_x188893370}[]{#_Toc316392154}

**进程监控和维护 \-- 进程监控和维护命令 \-- display process memory heap address**

------------------------------------------------------------------------

[**[display process memory heap address]{lang="EN-US"}**]{#struct_0_x1063_20800_x1890791216}[命令用来显示从指定地址开始的内存空间的内容。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_456458778}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1024233696}

[**[display process memory heap]{lang="EN-US"}**[ **job** *job-id* **address** *starting-address* **length** *memory-length*]{lang="EN-US"}]{#struct_0_x1063_20800_1296225320}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1063_20800_2000402110}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display process memory heap]{lang="EN-US"}**[ **job** *job-id* **address** *starting-address* **length** *memory-length* \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_630402744}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1063_20800_x8494030}[模式：]{style="font-family:宋体"}

[**[display process memory heap]{lang="EN-US"}**[ **job** *job-id* **address** *starting-address* **length** *memory-length* \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_x2040807946}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x187910330}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1063_20800_658982222}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1375309380}

[[network-admin]{lang="EN-US"}]{#struct_0_x1063_20800_1605249631}

[[network-operator]{lang="EN-US"}]{#struct_0_x1063_20800_291650973}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1063_20800_x1331287807}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1063_20800_x34218098}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x405991229}

[**[job ]{lang="EN-US"}***[job-id]{lang="EN-US"}*]{#struct_0_x1063_20800_x713857440}[：任务编号，用于唯一标识一个用户态进程，该编号不会随着用户态进程的重启而改变，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[address ]{lang="EN-US"}***[starting-address]{lang="EN-US"}*]{#struct_0_x1063_20800_x187975866}[：内存块的起始地址。]{style="font-family:宋体"}

[**[length]{lang="EN-US"}***[ memory-length]{lang="EN-US"}*]{#struct_0_x1063_20800_1369148496}[：内存的长度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x671895858}[：表示单板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_1529035376}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x445500367}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x2032791247}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_982959483}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x902523660}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x693053931}

[[当用户态进程运行异常时，使用该命令可以帮助设备维护人员诊断和定位问题。]{style="font-family:宋体"}]{#struct_0_x1063_20800_478267250}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1063_20800_2031450622}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_x188434617}[显示]{style="font-family:宋体"}[job 1]{lang="EN-US"}[从地址]{style="font-family:宋体"}[0xb7e30580]{lang="EN-US"}[开始，长度为]{style="font-family:宋体"}[128]{lang="EN-US"}[字节的内存空间的内容。]{style="font-family:宋体"}

[[\<Sysname\> display process memory heap job 1 address b7e30580 length 128]{lang="EN-US"}]{#struct_0_x1063_20800_82057045}

[B7E30580:  14 00 EF FF 00 00 00 00 E4 39 E2 B7 7C 05 E3 B7  \...\...\...9..\|\...    ]{lang="EN-US"}

[B7E30590:  14 00 EF FF 2F 73 62 69 6E 2F 73 6C 62 67 64 00  \..../sbin/slbgd.    ]{lang="EN-US"}

[B7E305A0:  14 00 EF FF 00 00 00 00 44 3B E2 B7 8C 05 E3 B7  \...\.....D;\...\...    ]{lang="EN-US"}

[B7E305B0:  14 00 EF FF 2F 73 62 69 6E 2F 6F 73 70 66 64 00  \..../sbin/ospfd.    ]{lang="EN-US"}

[B7E305C0:  14 00 EF FF 00 00 00 00 A4 3C E2 B7 AC 05 E3 B7  \...\...\...\<\...\...    ]{lang="EN-US"}

[B7E305D0:  14 00 EF FF 2F 73 62 69 6E 2F 6D 73 74 70 64 00  \..../sbin/mstpd.    ]{lang="EN-US"}

[B7E305E0:  14 00 EF FF 00 00 00 00 04 3E E2 B7 CC 05 E3 B7  \...\...\...\>\...\...    ]{lang="EN-US"}

[B7E305F0:  14 00 EF FF 2F 73 62 69 6E 2F 6E 74 70 64 00 00  \..../sbin/ntpd..]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1118955359}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display process memory heap]{lang="EN-US"}**]{#struct_0_x1063_20800_x806329900}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display process memory heap size]{lang="EN-US"}**]{#struct_0_x1063_20800_348457588}
:::

::: {#1579624061 .myid}
[]{#_Toc404797200}[]{#struct_0_x1063_20800_1492366932}[]{#_Toc316392155}[]{#_Toc295398814}

**进程监控和维护 \-- 进程监控和维护命令 \-- display process memory heap size**

------------------------------------------------------------------------

[**[display process memory heap size]{lang="EN-US"}**]{#struct_0_x1063_20800_976634377}[命令用来显示指定大小已使用内存块的地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x188500153}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1063_20800_1244021968}

[**[display process memory heap job]{lang="EN-US"}**[ *job-id* **size** *memory-size* \[ **offset** *offset-size* \]]{lang="EN-US"}]{#struct_0_x1063_20800_x1470252937}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1063_20800_x934474177}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display process memory heap]{lang="EN-US"}**[ **job** *job-id* **size** *memory-size* \[ **offset** *offset-size* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_1309806636}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1063_20800_2068319257}[模式：]{style="font-family:宋体"}

[**[display process memory heap]{lang="EN-US"}**[ **job** *job-id* **size** *memory-size* \[ **offset** *offset-size* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_1997215334}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1063_20800_2063775421}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1063_20800_x188565689}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1486844966}

[[network-admin]{lang="EN-US"}]{#struct_0_x1063_20800_1382920998}

[[network-operator]{lang="EN-US"}]{#struct_0_x1063_20800_x1565428140}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1063_20800_x1234622175}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1063_20800_x1180230897}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1063_20800_413477292}

[**[job ]{lang="EN-US"}***[job-id]{lang="EN-US"}*]{#struct_0_x1063_20800_x1530533455}[：任务编号，用于唯一标识一个用户态进程，该编号不会随着用户态进程的重启而改变，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[size]{lang="EN-US"}**[ memory-size]{lang="EN-US"}]{#struct_0_x1063_20800_1495894906}[：内存块大小，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[offset]{lang="EN-US"}***[ offset-size]{lang="EN-US"}*]{#struct_0_x1063_20800_x188631225}[：要查询的内存块的偏移，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[128]{lang="EN-US"}[。比如，系统给]{style="font-family:宋体"}[job 1]{lang="EN-US"}[分配了]{style="font-family:宋体"}[size]{lang="EN-US"}[为]{style="font-family:宋体"}[16]{lang="EN-US"}[字节的内存块]{style="font-family:宋体"}[100]{lang="EN-US"}[个，用户态进程当前已用了]{style="font-family:宋体"}[66]{lang="EN-US"}[个，如果执行命令]{style="font-family:宋体"}**[display process memory heap]{lang="EN-US"}**[ **job** *1* **size** *16* **offset** *50*]{lang="EN-US"}[，则会显示该用户态进程第]{style="font-family:宋体"}[51]{lang="EN-US"}[到第]{style="font-family:宋体"}[66]{lang="EN-US"}[个]{style="font-family:宋体"}[size]{lang="EN-US"}[为]{style="font-family:宋体"}[16]{lang="EN-US"}[字节的内存块的地址。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_1250146757}[：表示单板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_826685403}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x445762511}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_1486432316}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x216887881}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x901999375}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1584152776}

[[该命令显示的地址为十六进制格式，使用该地址，通过]{style="font-family:宋体"}**[display process memory heap address]{lang="EN-US"}**]{#struct_0_x1063_20800_x685011423}[命令可以显示该地址内存的具体内容。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1063_20800_2096609442}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_1795502847}[显示]{style="font-family:宋体"}[job 1]{lang="EN-US"}[已使用的]{style="font-family:宋体"}[size]{lang="EN-US"}[大小为]{style="font-family:宋体"}[16]{lang="EN-US"}[字节的内存块的地址。]{style="font-family:宋体"}

[[\<Sysname\> display process memory heap job 1 size 16]{lang="EN-US"}]{#struct_0_x1063_20800_x188696761}

[0xb7e300c0  0xb7e300d0  0xb7e300e0  0xb7e300f0]{lang="EN-US"}

[0xb7e30100  0xb7e30110  0xb7e30120  0xb7e30130]{lang="EN-US"}

[0xb7e30140  0xb7e30150  0xb7e30160  0xb7e30170]{lang="EN-US"}

[0xb7e30180  0xb7e30190  0xb7e301a0  0xb7e301b0]{lang="EN-US"}

[0xb7e301c0  0xb7e301d0  0xb7e301e0  0xb7e301f0]{lang="EN-US"}

[0xb7e30200  0xb7e30210  0xb7e30220  0xb7e30230]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_1236151908}[显示]{style="font-family:宋体"}[job 1]{lang="EN-US"}[已使用的]{style="font-family:宋体"}[size]{lang="EN-US"}[大小为]{style="font-family:宋体"}[16]{lang="EN-US"}[字节的内存块的地址，从第]{style="font-family:宋体"}[5]{lang="EN-US"}[个已使用内存块开始显示。]{style="font-family:宋体"}

[[\<Sysname\> display process memory heap job 1 size 16 offset 4]{lang="EN-US"}]{#struct_0_x1063_20800_x792944543}

[0xb7e30100  0xb7e30110  0xb7e30120  0xb7e30130]{lang="EN-US"}

[0xb7e30140  0xb7e30150  0xb7e30160  0xb7e30170]{lang="EN-US"}

[0xb7e30180  0xb7e30190  0xb7e301a0  0xb7e301b0]{lang="EN-US"}

[0xb7e301c0  0xb7e301d0  0xb7e301e0  0xb7e301f0]{lang="EN-US"}

[0xb7e30200  0xb7e30210  0xb7e30220  0xb7e30230]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1756301071}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display process memory heap]{lang="EN-US"}**]{#struct_0_x1063_20800_x1752312942}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display process memory heap address]{lang="EN-US"}**]{#struct_0_x1063_20800_433934139}[]{#_Toc358900887}[]{#_Toc340215437}
:::

::: {#1146935664 .myid}
[]{#_Toc404797201}[]{#struct_0_x1063_20800_x462984395}

**进程监控和维护 \-- 进程监控和维护命令 \-- exception filepath**

------------------------------------------------------------------------

[**[exception filepath]{lang="EN-US"}**]{#struct_0_x1063_20800_x462656715}[命令用来设置]{style="font-family:宋体"}[core]{lang="EN-US"}[文件的保存路径。]{style="font-family:宋体"}

[**[undo exception filepath]{lang="EN-US"}**]{#struct_0_x1063_20800_x253960921}[命令用来将]{style="font-family:宋体"}[core]{lang="EN-US"}[文件的保存路径设置为空。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1525478124}

[**[exception filepath ]{lang="EN-US"}***[directory]{lang="EN-US"}*]{#struct_0_x1063_20800_x462591179}

[**[undo exception filepath]{lang="EN-US"}**[ *directory*]{lang="EN-US"}]{#struct_0_x1063_20800_x656304701}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x463181004}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1063_20800_2078905692}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x237468411}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1063_20800_x463115468}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1063_20800_895510466}

[[network-admin]{lang="EN-US"}]{#struct_0_x1063_20800_623668307}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1063_20800_x449746170}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x463312076}

[*[directory]{lang="EN-US"}*]{#struct_0_x1063_20800_535038496}[：表示]{style="font-family:宋体"}[core]{lang="EN-US"}[文件的保存路径，只能为存储介质的根目录。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1695399478}

[[本命令配置成功后，设备会将生成的]{style="font-family:宋体"}[core]{lang="EN-US"}]{#struct_0_x1063_20800_x463246540}[文件存放到当前主用主控板上、指定存储介质根目录下的]{style="font-family:宋体"}[core]{lang="EN-US"}[文件夹下。如果存储介质根目录下没有]{style="font-family:宋体"}[core]{lang="EN-US"}[文件夹，则会先创建]{style="font-family:宋体"}[core]{lang="EN-US"}[文件夹，再保存]{style="font-family:宋体"}[core]{lang="EN-US"}[文件。]{style="font-family:宋体"}

[[当主控板上有多块存储介质的时候，可使用该命令修改]{style="font-family:宋体"}[core]{lang="EN-US"}]{#struct_0_x1063_20800_x364714190}[文件的保存路径。]{style="font-family:宋体"}

[[需要注意的是，当]{style="font-family:宋体"}[core]{lang="EN-US"}]{#struct_0_x1063_20800_x303648074}[文件的保存路径为空或无法正常访问时，系统将无法保存]{style="font-family:宋体"}[core]{lang="EN-US"}[文件。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x462918860}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_997227723}[设置]{style="font-family:宋体"}[core]{lang="EN-US"}[文件的保存路径。]{style="font-family:宋体"}

[[\<Sysname\> exception filepath flash:/]{lang="EN-US"}]{#struct_0_x1063_20800_1603508693}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x462853324}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display exception filepath]{lang="EN-US"}**]{#struct_0_x1063_20800_913932187}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[process core]{lang="EN-US"}**]{#struct_0_x1063_20800_1253490346}
:::

::: {#726285448 .myid}
[]{#_Toc404797202}[]{#struct_0_x1063_20800_1924369253}

**进程监控和维护 \-- 进程监控和维护命令 \-- monitor kernel deadloop enable**

------------------------------------------------------------------------

[**[monitor kernel deadloop enable]{lang="EN-US"}**]{#struct_0_x1063_20800_x188762297}[命令用来开启内核线程死循环检测功能。]{style="font-family:
宋体"}

[**[undo monitor kernel deadloop enable]{lang="EN-US"}**]{#struct_0_x1063_20800_1651399648}[命令用来关闭内核线程死循环检测功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_2071876980}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1063_20800_300933928}

[**[monitor kernel deadloop enable]{lang="EN-US"}**]{#struct_0_x1063_20800_807154818}

[**[undo monitor kernel deadloop enable]{lang="EN-US"}**]{#struct_0_x1063_20800_x2011125397}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1063_20800_x828308812}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[monitor kernel deadloop enable]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_x1340430896}

[**[undo monitor kernel deadloop enable]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_1360961365}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1063_20800_x188827833}[模式：]{style="font-family:宋体"}

[**[monitor kernel deadloop enable ]{lang="EN-US"}**[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_36021056}

[**[undo monitor kernel deadloop enable ]{lang="EN-US"}**[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_x315925773}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1063_20800_126234830}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1063_20800_1085583127}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1756429774}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1063_20800_x567245384}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1063_20800_2042062752}

[[network-admin]{lang="EN-US"}]{#struct_0_x1063_20800_x61649372}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x188893369}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x1890332463}[：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x1993192599}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中设备的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_1537730340}[：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x902327055}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1154739019}

[[在内核态空间中，所有资源都是共享的，多个内核线程之间通过任务调度协调工作。如果某个内核线程长时间一直占用]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_x1063_20800_1987789835}[，就会导致其它内核线程获取不到运行机会，整个系统挂死，我们称这种现象为死循环。]{style="font-family:宋体"}

[[开启内核线程死循环检测功能后，如果系统发现某内核线程在指定时间内一直占用]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_x1063_20800_x788511017}[，则判定该内核线程为死循环。系统会记录一条死循环信息供管理员查询，并自动重启整个系统来解除死循环。]{style="font-family:宋体"}

[[开机后，系统会自动检测内核线程是否发生了死循环，建议用户不要随意配置该命令。如果确实需要配置，请在]{style="font-family:宋体"}[H3C]{lang="EN-US"}]{#struct_0_x1063_20800_1199815012}[工程师的指导下进行，以免引起系统异常。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1063_20800_583906677}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_x187910329}[开启内核线程死循环检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1063_20800_658392397}

[\[Sysname\] monitor kernel deadloop enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_264562171}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display kernel]{lang="EN-US"}**]{#struct_0_x1063_20800_1319676976}**[ ]{lang="EN-US"}[deadloop]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display kernel]{lang="EN-US"}**]{#struct_0_x1063_20800_x1351684590}**[ ]{lang="EN-US"}[deadloop configuration]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[monitor kernel deadloop exclude-thread]{lang="EN-US"}**]{#struct_0_x1063_20800_608379889}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[monitor kernel deadloop time]{lang="EN-US"}**]{#struct_0_x1063_20800_1156690949}
:::

::: {#1488864331 .myid}
[]{#_Toc404797203}[]{#struct_0_x1063_20800_1573528779}

**进程监控和维护 \-- 进程监控和维护命令 \-- monitor kernel deadloop exclude-thread**

------------------------------------------------------------------------

[**[monitor kernel deadloop exclude-thread]{lang="EN-US"}**]{#struct_0_x1063_20800_x187975865}[命令用来配置不检测指定内核线程是否发生了死循环。]{style="font-family:宋体"}

[**[undo monitor kernel deadloop exclude-thread]{lang="EN-US"}**]{#struct_0_x1063_20800_1369214032}[命令用来恢复对指定内核线程是否发生了死循环进行检测。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1535367561}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1063_20800_2035812665}

[**[monitor kernel deadloop exclude-thread]{lang="EN-US"}***[ tid]{lang="EN-US"}*]{#struct_0_x1063_20800_x191631154}

[**[undo monitor kernel deadloop exclude-thread]{lang="EN-US"}***[ ]{lang="EN-US"}*[\[ *tid* \]]{lang="EN-US"}]{#struct_0_x1063_20800_x1182354993}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1063_20800_95574479}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[monitor kernel deadloop exclude-thread]{lang="EN-US"}***[ tid]{lang="EN-US"}*[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_x1367611909}

[**[undo monitor kernel deadloop exclude-thread]{lang="EN-US"}***[ ]{lang="EN-US"}*[\[ *tid* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_x921888461}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1063_20800_x188434620}[模式：]{style="font-family:宋体"}

[**[monitor kernel deadloop exclude-thread]{lang="EN-US"}***[ tid]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_81991512}

[**[undo monitor kernel deadloop exclude-thread]{lang="EN-US"}***[ ]{lang="EN-US"}*[\[ *tid* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_x1552493283}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x862679245}

[[开启内核线程死循环检测功能后，系统会监控所有内核线程是否发生了死循环。]{style="font-family:宋体"}]{#struct_0_x1063_20800_2121068877}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1430533058}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1063_20800_1535784200}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x666353075}

[[network-admin]{lang="EN-US"}]{#struct_0_x1063_20800_x1413644596}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x188500156}

[*[tid]{lang="EN-US"}*]{#struct_0_x1063_20800_1244218576}[：表示内核线程编号，用于唯一标识一个内核线程，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[。不指定该参数时，表示恢复到缺省情况。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x1554585359}[：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_1927242603}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中设备的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_1054416216}[：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x902392591}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1151494378}

[[缺省情况下，系统会检测所有内核线程是否发生了死循环。多次执行该命令，可以配置对多个内核线程不进行检测，最多可以配置]{style="font-family:宋体"}[128]{lang="EN-US"}]{#struct_0_x1063_20800_758010398}[个。]{style="font-family:宋体"}

[[开机后，系统会自动检测内核线程是否发生了死循环，建议用户不要随意配置该命令。如果确实需要配置，请在]{style="font-family:宋体"}[H3C]{lang="EN-US"}]{#struct_0_x1063_20800_x409212615}[工程师的指导下进行，以免引起系统异常。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x192346231}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_x188565692}[对编号为]{style="font-family:宋体"}[15]{lang="EN-US"}[的内核线程不进行死循环检测。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1063_20800_x1486255141}

[\[Sysname\]monitor kernel deadloop exclude-thread 15]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x719306838}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}**]{#struct_0_x1063_20800_703642510}**[kernel ]{lang="EN-US"}[deadloop configuration]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**]{#struct_0_x1063_20800_x1443777622}**[ kernel ]{lang="EN-US"}[deadloop]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[monitor ]{lang="EN-US"}**]{#struct_0_x1063_20800_x1329945677}**[kernel]{lang="EN-US"}[ deadloop]{lang="EN-US"}[ enable]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[monitor ]{lang="EN-US"}**]{#struct_0_x1063_20800_1729175996}**[kernel]{lang="EN-US"}[ deadloop]{lang="EN-US"}[ time]{lang="EN-US"}**
:::

::: {#-1619579924 .myid}
[]{#_Toc404797204}[]{#struct_0_x1063_20800_296277478}

**进程监控和维护 \-- 进程监控和维护命令 \-- monitor kernel deadloop time**

------------------------------------------------------------------------

[**[monitor kernel deadloop time]{lang="EN-US"}**]{#struct_0_x1063_20800_x188631228}[命令用来配置判定内核线程是否死循环的时长。]{style="font-family:
宋体"}

[**[undo monitor kernel deadloop time]{lang="EN-US"}**]{#struct_0_x1063_20800_1249425861}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1425480321}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1179958980}

[**[monitor kernel deadloop time]{lang="EN-US"}***[ interval]{lang="EN-US"}*]{#struct_0_x1063_20800_308959976}

[**[undo monitor kernel deadloop time]{lang="EN-US"}**]{#struct_0_x1063_20800_x467386602}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1063_20800_x2067866491}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[monitor kernel deadloop time ]{lang="EN-US"}***[interval]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_486774750}

[**[undo monitor kernel deadloop time]{lang="EN-US"}***[ ]{lang="EN-US"}*[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_x496144533}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1063_20800_x188696764}[模式：]{style="font-family:宋体"}

[**[monitor kernel deadloop time ]{lang="EN-US"}***[interval]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_1236479588}

[**[undo monitor kernel deadloop time]{lang="EN-US"}***[ ]{lang="EN-US"}*[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_1860584668}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1063_20800_298395023}

[[当某内核线程连续运行超过]{style="font-family:宋体"}[8]{lang="EN-US"}]{#struct_0_x1063_20800_x1338742363}[秒钟，则判定为死循环。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x259394482}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1063_20800_x873193532}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1657506154}

[[network-admin]{lang="EN-US"}]{#struct_0_x1063_20800_1914268936}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x188762300}

[**[time]{lang="EN-US"}***[ interval]{lang="EN-US"}*]{#struct_0_x1063_20800_x305374249}[：表示内核线程死循环判定时长，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x1168063631}[：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x243550298}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中设备的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x593555144}[：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x902195982}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1129874394}

[[开启内核线程检测功能后，如果某内核线程持续运行指定时间，则认为该内核线程已经死循环，系统将记录一条死循环信息并重启。]{style="font-family:宋体"}]{#struct_0_x1063_20800_1149984883}

[[开机后，系统会自动检测内核线程是否发生了死循环，建议用户不要随意配置该命令。如果确实需要配置，请在]{style="font-family:宋体"}[H3C]{lang="EN-US"}]{#struct_0_x1063_20800_51933259}[工程师的指导下进行，以免引起系统异常。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x188827836}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_35693376}[配置当某内核线程连续运行超过]{style="font-family:宋体"}[8]{lang="EN-US"}[秒钟，则判定为死循环。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1063_20800_1915581449}

[\[Sysname\] monitor kernel deadloop time 8]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_416387043}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}**]{#struct_0_x1063_20800_204619104}**[kernel ]{lang="EN-US"}[deadloop configuration]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}**]{#struct_0_x1063_20800_x1891128437}**[kernel ]{lang="EN-US"}[deadloop]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[monitor ]{lang="EN-US"}**]{#struct_0_x1063_20800_x972717735}**[kernel]{lang="EN-US"}[ deadloop ]{lang="EN-US"}[enable]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[monitor ]{lang="EN-US"}**]{#struct_0_x1063_20800_x1111930452}**[kernel]{lang="EN-US"}[ deadloop exclude-thread]{lang="EN-US"}**
:::

::: {#-173307042 .myid}
[]{#_Toc404797205}[]{#struct_0_x1063_20800_1889586240}

**进程监控和维护 \-- 进程监控和维护命令 \-- monitor kernel starvation enable**

------------------------------------------------------------------------

[**[monitor kernel starvation enable]{lang="EN-US"}**]{#struct_0_x1063_20800_x188893372}[命令用来开启内核线程饿死检测功能。]{style="font-family:宋体"}

[**[undo monitor kernel starvation enable]{lang="EN-US"}**]{#struct_0_x1063_20800_x1890660144}[命令用来关闭内核线程饿死检测功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1223534112}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1063_20800_923075172}

[**[monitor kernel starvation enable]{lang="EN-US"}**]{#struct_0_x1063_20800_x1213415895}

[**[undo monitor kernel starvation enable]{lang="EN-US"}**]{#struct_0_x1063_20800_x1170726222}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1063_20800_1214510119}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[monitor kernel starvation enable ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_x807467901}

[**[undo monitor kernel starvation enable ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_313806643}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1063_20800_x187910332}[模式：]{style="font-family:宋体"}

[**[monitor kernel starvation enable ]{lang="EN-US"}**[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_659113294}

[**[undo monitor kernel starvation enable ]{lang="EN-US"}**[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_x1430302316}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x2026211650}

[[内核线程饿死检测功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1782788718}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1220622247}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1063_20800_x185656112}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1927818849}

[[network-admin]{lang="EN-US"}]{#struct_0_x1063_20800_x1361651788}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x187975868}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_1370066000}[：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x1243221847}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中设备的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x266796051}[：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x902261518}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1557668602}

[[如果内核线程本身的触发条件没有达到，会导致该内核线程在一段时间内一直得不到调度，我们称这种现象为饿死。]{style="font-family:宋体"}]{#struct_0_x1063_20800_353039018}

[[开启内核线程饿死检测功能后，当系统检测到某内核线程饿死时，会记录一条饿死信息供管理员查询。]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1997992897}

[[内核线程饿死并不会影响整个系统的运行，当触发条件达到，处于饿死状态的内核线程会自动执行。]{style="font-family:宋体"}]{#struct_0_x1063_20800_2447773}

[[开机后，系统会自动检测内核线程是否发生了饿死，建议用户不要随意配置该命令。如果确实需要配置，请在]{style="font-family:宋体"}[H3C]{lang="EN-US"}]{#struct_0_x1063_20800_396148510}[工程师的指导下进行，以免引起系统异常。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x188434619}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_81401685}[开启内核线程饿死检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1063_20800_411163065}

[\[Sysname\] monitor kernel starvation enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_949416165}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}**]{#struct_0_x1063_20800_1217462784}**[kernel ]{lang="EN-US"}[starvation configuration]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}**]{#struct_0_x1063_20800_1845042035}**[kernel]{lang="EN-US"}[ starvation]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[monitor ]{lang="EN-US"}**]{#struct_0_x1063_20800_x464758111}**[kernel]{lang="EN-US"}[ starvation time]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[monitor ]{lang="EN-US"}**]{#struct_0_x1063_20800_846757008}**[kernel]{lang="EN-US"}[ starvation exclude-thread]{lang="EN-US"}**
:::

::: {#-1287846675 .myid}
[]{#_Toc282002495}[]{#_Toc280620237}[]{#_Toc273190425}[]{#_Toc404797206}[]{#struct_0_x1063_20800_x188500155}[]{#_Toc294703873}[]{#_Toc294703885}[]{#_Toc294703886}[]{#_Toc294703915}[]{#_Toc294703916}[]{#_Toc294703918}[]{#_Toc294703920}[]{#_Toc294703921}[]{#_Toc294703922}[]{#_Toc294703923}[]{#_Toc294703924}[]{#_Toc294703925}[]{#_Toc294703926}[]{#_Toc294703927}[]{#_Toc294703928}[]{#_Toc294703929}[]{#_Toc294703930}[]{#_Toc294703931}[]{#_Toc294703932}[]{#_Toc294703933}[]{#_Toc294703934}[]{#_Toc294703935}[]{#_Toc294703936}[]{#_Toc294703938}[]{#_Toc294703939}[]{#_Toc294703940}[]{#_Toc294703941}[]{#_Toc294703942}[]{#_Toc294703943}[]{#_Toc294703965}[]{#_Toc294703966}[]{#_Toc294703990}[]{#_Toc294703991}[]{#_Toc294704013}

**进程监控和维护 \-- 进程监控和维护命令 \-- monitor kernel starvation exclude-thread**

------------------------------------------------------------------------

[**[monitor kernel starvation exclude-thread]{lang="EN-US"}**]{#struct_0_x1063_20800_1244415184}[命令用来配置不检测指定内核线程是否发生了饿死。]{style="font-family:宋体"}

[**[undo monitor kernel starvation exclude-thread]{lang="EN-US"}**]{#struct_0_x1063_20800_2022892937}[命令用来恢复对指定内核线程是否发生了饿死进行检测。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1392709520}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1063_20800_1716862683}

[**[monitor kernel starvation exclude-thread]{lang="EN-US"}***[ tid]{lang="EN-US"}*]{#struct_0_x1063_20800_888740590}

[**[undo monitor kernel starvation exclude-thread]{lang="EN-US"}***[ ]{lang="EN-US"}*[\[ *tid* \]]{lang="EN-US"}]{#struct_0_x1063_20800_x250030178}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1063_20800_x1903431262}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[monitor kernel starvation exclude-thread]{lang="EN-US"}***[ tid]{lang="EN-US"}*[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_x1367278192}

[**[undo monitor kernel starvation exclude-thread]{lang="EN-US"}***[ ]{lang="EN-US"}*[\[ *tid* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_x188565691}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1063_20800_x1486320677}[模式：]{style="font-family:宋体"}

[**[monitor kernel starvation exclude-thread]{lang="EN-US"}***[ tid ]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_x179274736}

[**[undo monitor kernel starvation exclude-thread]{lang="EN-US"}***[ ]{lang="EN-US"}*[\[ *tid* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_1480709190}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1063_20800_2139637453}

[[开启内核线程死循环检测功能后，会监控所有内核线程是否发生了饿死。]{style="font-family:宋体"}]{#struct_0_x1063_20800_2088217360}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1063_20800_666224762}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1063_20800_x7379389}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x188631227}

[[network-admin]{lang="EN-US"}]{#struct_0_x1063_20800_1250015685}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1857102334}

[*[tid]{lang="EN-US"}*]{#struct_0_x1063_20800_x1285963888}[：表示内核线程编号，用于唯一标识一个内核线程，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[。不指定该参数时，表示恢复到缺省情况。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x1356185068}[：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_1097320849}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中设备的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_2129549516}[：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1063_20800_664019034}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1120616692}

[[缺省情况下，系统会检测所有内核线程是否发生了饿死。多次执行该命令，可以配置对多个内核线程不进行检测，最多可以配置]{style="font-family:宋体"}[128]{lang="EN-US"}]{#struct_0_x1063_20800_941378159}[个。]{style="font-family:宋体"}

[[开机后，系统会自动检测内核线程是否发生了饿死，建议用户不要随意配置该命令。如果确实需要配置，请在]{style="font-family:宋体"}[H3C]{lang="EN-US"}]{#struct_0_x1063_20800_x188696763}[工程师的指导下进行，以免引起系统异常。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1236282980}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_x1203372405}[对编号为]{style="font-family:宋体"}[15]{lang="EN-US"}[的内核线程不进行饿死检测。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1063_20800_x1742705184}

[\[Sysname\] monitor kernel starvation exclude-thread 15]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x696909759}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display kernel]{lang="EN-US"}**]{#struct_0_x1063_20800_x206107375}**[ ]{lang="EN-US"}[starvation]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display kernel]{lang="EN-US"}**]{#struct_0_x1063_20800_x1861923157}**[ ]{lang="EN-US"}[starvation configuration]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[monitor kernel starvation]{lang="EN-US"}**]{#struct_0_x1063_20800_x1413608253}**[ time]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[monitor kernel starvation]{lang="EN-US"}**]{#struct_0_x1063_20800_2063872059}**[ enable]{lang="EN-US"}**
:::

::: {#-1320667249 .myid}
[]{#_Toc404797207}[]{#struct_0_x1063_20800_x188762299}

**进程监控和维护 \-- 进程监控和维护命令 \-- monitor kernel starvation time**

------------------------------------------------------------------------

[**[monitor kernel starvation time]{lang="EN-US"}**]{#struct_0_x1063_20800_1650482144}[命令用来配置判定内核线程是否饿死的时长。]{style="font-family:
宋体"}

[**[undo monitor kernel starvation time]{lang="EN-US"}**]{#struct_0_x1063_20800_917650258}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_473119674}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1063_20800_1045370492}

[**[monitor kernel starvation]{lang="EN-US"}**[ **time** *interval* ]{lang="EN-US"}]{#struct_0_x1063_20800_959005682}

[**[undo monitor kernel starvation time]{lang="EN-US"}**]{#struct_0_x1063_20800_x1840685204}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1063_20800_907282965}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[monitor kernel starvation time]{lang="EN-US"}***[ interval]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_999373351}

[**[undo monitor kernel starvation time ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_x188827835}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1063_20800_35627840}[模式：]{style="font-family:宋体"}

[**[monitor kernel starvation time]{lang="EN-US"}***[ interval]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_782964284}

[**[undo monitor kernel starvation time]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_244777574}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1407703401}

[[当某内核线程在]{style="font-family:宋体"}[120]{lang="EN-US"}]{#struct_0_x1063_20800_1557769966}[秒内一直没有运行，则认为该内核线程被饿死。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1883155226}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1063_20800_x2136312871}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x188893371}

[[network-admin]{lang="EN-US"}]{#struct_0_x1063_20800_x1890856752}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x209149723}

[**[time ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_x1063_20800_1852770896}[：表示内核线程饿死判定时长，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x577166167}[：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x2128691813}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中设备的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_171277042}[：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1063_20800_663822426}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x394656575}

[[开机后，系统会自动检测内核线程是否发生了饿死，建议用户不要随意配置该命令。如果确实需要配置，请在]{style="font-family:宋体"}[H3C]{lang="EN-US"}]{#struct_0_x1063_20800_x825552994}[工程师的指导下进行，以免引起系统异常。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x187910331}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_658916686}[配置当内核线程在]{style="font-family:宋体"}[120]{lang="EN-US"}[秒内一直没有运行，则认为该内核线程被饿死。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1063_20800_2105950915}

[\[Sysname\] monitor kernel starvation time 120]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_975967775}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display kernel]{lang="EN-US"}**]{#struct_0_x1063_20800_1374687798}**[ ]{lang="EN-US"}[starvation]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display kernel]{lang="EN-US"}**]{#struct_0_x1063_20800_x736658477}**[ ]{lang="EN-US"}[starvation configuration]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[monitor kernel starvation]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1063_20800_1749059503}**[enable]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[monitor kernel starvation]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1063_20800_406019400}**[exclude-thread]{lang="EN-US"}**
:::

::: {#-1251975530 .myid}
[]{#_Toc404797208}[]{#struct_0_x1063_20800_914886868}[]{#_Toc316392156}

**进程监控和维护 \-- 进程监控和维护命令 \-- monitor process**

------------------------------------------------------------------------

[**[monitor process]{lang="EN-US"}**]{#struct_0_x1063_20800_x187975867}[命令用来显示进程的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1369082960}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1063_20800_776682760}

[**[monitor process]{lang="EN-US"}**[ \[ **dumbtty** \] \[ **iteration** *number* \]]{lang="EN-US"}]{#struct_0_x1063_20800_1834773386}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1063_20800_1892518221}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[monitor]{lang="EN-US"}**[ **process** \[ **dumbtty** \] \[ **iteration** *number* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_x186469584}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1063_20800_x515697483}[模式：]{style="font-family:宋体"}

[**[monitor]{lang="EN-US"}**[ **process** \[ **dumbtty** \] \[ **iteration** *number* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_759908225}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x92973579}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1063_20800_x188434622}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1063_20800_81860440}

[[network-admin]{lang="EN-US"}]{#struct_0_x1063_20800_433666794}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1063_20800_2140775177}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1410914666}

[**[dumbtty]{lang="EN-US"}**]{#struct_0_x1063_20800_1649989228}[：以哑终端方式显示进程统计信息（即屏幕不支持定时刷新统计信息）。指定该参数时，全部进程的统计信息以]{style="font-family:宋体"}[CPU]{lang="EN-US"}[使用率降序排列输出到屏幕上；不指定该参数时，统计信息以交互模式显示，缺省情况下按]{style="font-family:宋体"}[CPU]{lang="EN-US"}[占用率降序显示前]{style="font-family:宋体"}[10]{lang="EN-US"}[个进程的统计信息，且每隔]{style="font-family:宋体"}[5]{lang="EN-US"}[秒刷新一次。]{style="font-family:宋体"}

[**[iteration]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_x1063_20800_x204514269}[：表示进程统计信息的显示次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。指定]{style="font-family:宋体"}**[dumbtty]{lang="EN-US"}**[参数时，]{style="font-family:宋体"}*[number]{lang="EN-US"}*[的缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[；不指定]{style="font-family:宋体"}**[dumbtty]{lang="EN-US"}**[且不配置]{style="font-family:宋体"}*[number]{lang="EN-US"}*[参数时，表示显示次数没有限制，统计信息会每隔]{style="font-family:宋体"}[5]{lang="EN-US"}[秒刷新一次，一直显示。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_1788134321}[：表示单板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x188500158}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x445565900}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_758559582}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_2040636525}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1063_20800_663560282}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1243563216}

[[不指定]{style="font-family:宋体"}**[dumbtty]{lang="EN-US"}**]{#struct_0_x1063_20800_977981081}[参数的情况下，统计信息以交互模式显示。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交互模式下，系统会自动计算可显示的进程个数，超过屏幕范围的不显示。]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1311943785}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交互模式下，用户可通过输入]{style="font-family:宋体"}]{#struct_0_x1063_20800_x113363041}[[[表]{style="font-family:宋体"}1-12]{lang="EN-US"}](?-1251975530#_Ref282593064)[中指定的交互命令字来执行相应的操作。]{style="font-family:宋体"}

[]{#struct_0_x1063_20800_1999533167}[[表1-12 ]{lang="EN-US"}[monitor process]{lang="EN-US"}]{#_Ref282593064}[命令支持的交互命令字描述表]{style="font-family:黑体"}

[]{#table_struct_0_2102549779}[[命令字]{style="font-family:黑体"}]{#struct_0_x1063_20800_x440075725}
:::

[[功能描述]{style="font-family:黑体"}]{#struct_0_x1063_20800_201962139}

[[?]{lang="EN-US"}]{#struct_0_x1063_20800_x188565694}[或]{style="font-family:宋体"}[h]{lang="EN-US"}

[[帮助信息，显示可用的交互式命令字]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1486124069}

[[1]{lang="EN-US"}]{#struct_0_x1063_20800_x2064187414}

[[各物理]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_x1063_20800_x2064121878}[状态的显示开关。比如：]{style="font-family:宋体"}

[[(1)[    ]{style="font:7.0pt "}]{lang="EN-US"}[输入]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x1063_20800_x1464028414}[，分别显示各物理]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的参数值]{style="font-family:宋体"}

[[(2)[    ]{style="font:7.0pt "}]{lang="EN-US"}[再次输入]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x1063_20800_1018884884}[，显示所有]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的参数的平均值]{style="font-family:宋体"}

[[(3)[    ]{style="font:7.0pt "}]{lang="EN-US"}[第三次输入]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x1063_20800_1702876817}[，又分别显示各物理]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的参数值]{style="font-family:宋体"}

[[(4)[    ]{style="font:7.0pt "}]{lang="EN-US"}[如此循环]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1299641320}

[[缺省情况下，显示所有]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_x1063_20800_x656172657}[的参数的平均值]{style="font-family:宋体"}

[[c]{lang="EN-US"}]{#struct_0_x1063_20800_x98050936}

[[按]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_x1063_20800_x1963387760}[占用率降序排列，缺省情况下采用降序排列]{style="font-family:宋体"}

[[d]{lang="EN-US"}]{#struct_0_x1063_20800_1729321535}

[[设置统计信息的更新时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x1063_20800_341223578}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[秒，缺省值为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒]{style="font-family:宋体"}

[[f]{lang="EN-US"}]{#struct_0_x1063_20800_x188631230}

[[按进程打开的文件句柄数降序排列]{style="font-family:宋体"}]{#struct_0_x1063_20800_1249950148}

[[k]{lang="EN-US"}]{#struct_0_x1063_20800_x1416215885}

[[终止一个任务，此命令会影响系统运行，请谨慎使用]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1885654517}

[[l]{lang="EN-US"}]{#struct_0_x1063_20800_728426681}

[[刷新屏幕]{style="font-family:宋体"}]{#struct_0_x1063_20800_2027570911}

[[m]{lang="EN-US"}]{#struct_0_x1063_20800_x188696766}

[[按进程使用内存大小降序排列]{style="font-family:宋体"}]{#struct_0_x1063_20800_1236610660}

[[n]{lang="EN-US"}]{#struct_0_x1063_20800_x2013195053}

[[改变显示的进程个数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x1063_20800_x693266390}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[（缺省值为]{style="font-family:宋体"}[10]{lang="EN-US"}[个，]{style="font-family:宋体"}[0]{lang="EN-US"}[表示不作限制）；超过屏幕范围时，仍只显示一屏内可容纳的进程个数]{style="font-family:宋体"}

[[q]{lang="EN-US"}]{#struct_0_x1063_20800_x1903882575}

[[退出交互模式]{style="font-family:宋体"}]{#struct_0_x1063_20800_x188762302}

[[t]{lang="EN-US"}]{#struct_0_x1063_20800_x305243177}

[[按进程最近一次启动后的运行时间降序排列]{style="font-family:宋体"}]{#struct_0_x1063_20800_x342393826}

[[\<]{lang="EN-US"}]{#struct_0_x1063_20800_x1180066732}[ ]{lang="EN-US"}

[[排序项向左移动一列]{style="font-family:宋体"}]{#struct_0_x1063_20800_386113395}

[[\>]{lang="EN-US"}]{#struct_0_x1063_20800_x188827838}[ ]{lang="EN-US"}

[[排序项向右移动一列]{style="font-family:宋体"}]{#struct_0_x1063_20800_35300160}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1104143386}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_425242705}[以哑终端方式显示进程统计信息。（使用该方式显示时，系统会一次显示所有进程的统计信息，并且不支持定时刷新，显示完毕后，会退回到命令视图）]{style="font-family:宋体"}

[[\<Sysname\> monitor process dumbtty]{lang="EN-US"}]{#struct_0_x1063_20800_x188893374}

[ 76 processes; 103 threads; 687 fds]{lang="EN-US"}

[Thread states: 1 running, 102 sleeping, 0 stopped, 0 zombie]{lang="EN-US"}

[CPU states: 77.16% idle, 0.00% user, 14.96% kernel, 7.87% interrupt]{lang="EN-US"}

[Memory: 496M total, 341M available, page size 4K]{lang="EN-US"}

[    JID    PID  PRI  State  FDs    MEM  HH:MM:SS    CPU   Name]{lang="EN-US"}

[   1047   1047  120    R     9   1420K  00:02:23  13.53%  diagd]{lang="EN-US"}

[      1      1  120    S    17   1092K  00:00:20   7.61%  scmd]{lang="EN-US"}

[   1000   1000  115    S     0      0K  00:00:09   0.84%  \[sock/1\]]{lang="EN-US"}

[   1026   1026  120    S    20  26044K  00:00:05   0.84%  syslogd]{lang="EN-US"}

[      2      2  115    S     0      0K  00:00:00   0.00%  \[kthreadd\]]{lang="EN-US"}

[      3      3   99    S     0      0K  00:00:00   0.00%  \[migration/0\]]{lang="EN-US"}

[      4      4  115    S     0      0K  00:00:06   0.00%  \[ksoftirqd/0\]]{lang="EN-US"}

[      5      5   99    S     0      0K  00:00:00   0.00%  \[watchdog/0\]]{lang="EN-US"}

[      6      6  115    S     0      0K  00:00:01   0.00%  \[events/0\]]{lang="EN-US"}

[      7      7  115    S     0      0K  00:00:00   0.00%  \[khelper\]]{lang="EN-US"}

[   4797   4797  120    S     8  28832K  00:00:02   0.00%  comsh]{lang="EN-US"}

[   5117   5117  120    S     8   1496K  00:00:00   0.00%  top]{lang="EN-US"}

[ ]{lang="EN-US"}

[\<Sysname\>]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_x1890529072}[以哑终端方式显示进程统计信息，并且执行一次命令显示两次统计结果。]{style="font-family:宋体"}

[[\<Sysname\> monitor process dumbtty iteration 2]{lang="EN-US"}]{#struct_0_x1063_20800_x187910334}

[76 processes; 103 threads; 687 fds]{lang="EN-US"}

[Thread states: 1 running, 102 sleeping, 0 stopped, 0 zombie]{lang="EN-US"}

[CPU states: 44.84% idle, 0.51% user, 39.17% kernel, 15.46% interrupt]{lang="EN-US"}

[Memory: 496M total, 341M available, page size 4K]{lang="EN-US"}

[    JID    PID  PRI  State  FDs    MEM  HH:MM:SS    CPU   Name]{lang="EN-US"}

[   1047   1047  120    R     9   1420K  00:02:30  37.11%  diagd]{lang="EN-US"}

[      1      1  120    S    17   1092K  00:00:21  11.34%  scmd]{lang="EN-US"}

[   1000   1000  115    S     0      0K  00:00:09   2.06%  \[sock/1\]]{lang="EN-US"}

[   1026   1026  120    S    20  26044K  00:00:05   1.54%  syslogd]{lang="EN-US"}

[   1027   1027  120    S    12   9280K  00:01:12   1.03%  devd]{lang="EN-US"}

[      4      4  115    S     0      0K  00:00:06   0.51%  \[ksoftirqd/0\]]{lang="EN-US"}

[   1009   1009  115    S     0      0K  00:00:08   0.51%  \[karp/1\]]{lang="EN-US"}

[   1010   1010  115    S     0      0K  00:00:13   0.51%  \[kND/1\]]{lang="EN-US"}

[   5373   5373  120    S     8   1496K  00:00:00   0.51%  top]{lang="EN-US"}

[      2      2  115    S     0      0K  00:00:00   0.00%  \[kthreadd\]]{lang="EN-US"}

[      3      3   99    S     0      0K  00:00:00   0.00%  \[migration/0\]]{lang="EN-US"}

[      5      5   99    S     0      0K  00:00:00   0.00%  \[watchdog/0\]]{lang="EN-US"}

[      6      6  115    S     0      0K  00:00:01   0.00%  \[events/0\]]{lang="EN-US"}

[      7      7  115    S     0      0K  00:00:00   0.00%  \[khelper\]]{lang="EN-US"}

[   4796   4796  120    S    11   2744K  00:00:00   0.00%  login]{lang="EN-US"}

[   4797   4797  120    S     8  28832K  00:00:03   0.00%  comsh]{lang="EN-US"}

[[// 5]{lang="EN-US"}]{#struct_0_x1063_20800_659244366}[秒钟后，系统会自动统计一次，并显示统计信息如下。（相当于执行了两次]{style="font-family:宋体"}**[monitor process dumbtty]{lang="EN-US"}**[，两次执行的时间间隔为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒）]{style="font-family:宋体"}

[[76 processes; 103 threads; 687 fds]{lang="EN-US"}]{#struct_0_x1063_20800_x187975870}

[Thread states: 1 running, 102 sleeping, 0 stopped, 0 zombie]{lang="EN-US"}

[CPU states: 78.71% idle, 0.16% user, 14.86% kernel, 6.25% interrupt]{lang="EN-US"}

[Memory: 496M total, 341M available, page size 4K]{lang="EN-US"}

[    JID    PID  PRI  State  FDs    MEM  HH:MM:SS    CPU   Name]{lang="EN-US"}

[   1047   1047  120    R     9   1420K  00:02:31  14.25%  diagd]{lang="EN-US"}

[      1      1  120    S    17   1092K  00:00:21   4.25%  scmd]{lang="EN-US"}

[   1027   1027  120    S    12   9280K  00:01:12   1.29%  devd]{lang="EN-US"}

[   1000   1000  115    S     0      0K  00:00:09   0.37%  \[sock/1\]]{lang="EN-US"}

[   5373   5373  120    S     8   1500K  00:00:00   0.37%  top]{lang="EN-US"}

[      6      6  115    S     0      0K  00:00:01   0.18%  \[events/0\]]{lang="EN-US"}

[   1009   1009  115    S     0      0K  00:00:08   0.18%  \[karp/1\]]{lang="EN-US"}

[   1010   1010  115    S     0      0K  00:00:13   0.18%  \[kND/1\]]{lang="EN-US"}

[   4795   4795  120    S    11   2372K  00:00:01   0.18%  telnetd]{lang="EN-US"}

[      2      2  115    S     0      0K  00:00:00   0.00%  \[kthreadd\]]{lang="EN-US"}

[      3      3   99    S     0      0K  00:00:00   0.00%  \[migration/0\]]{lang="EN-US"}

[      4      4  115    S     0      0K  00:00:06   0.00%  \[ksoftirqd/0\]]{lang="EN-US"}

[      5      5   99    S     0      0K  00:00:00   0.00%  \[watchdog/0\]]{lang="EN-US"}

[      7      7  115    S     0      0K  00:00:00   0.00%  \[khelper\]]{lang="EN-US"}

[   4796   4796  120    S    11   2744K  00:00:00   0.00%  login]{lang="EN-US"}

[   4797   4797  120    S     8  28832K  00:00:03   0.00%  comsh]{lang="EN-US"}

[ ]{lang="EN-US"}

[\<Sysname\>]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_1369541713}[以交互方式显示进程统计信息。]{style="font-family:宋体"}

[[\<Sysname\> monitor process]{lang="EN-US"}]{#struct_0_x1063_20800_x188434621}

[76 processes; 103 threads; 687 fds]{lang="EN-US"}

[Thread states: 1 running, 102 sleeping, 0 stopped, 0 zombie]{lang="EN-US"}

[CPU states: 78.98% idle, 0.16% user, 14.57% kernel, 6.27% interrupt]{lang="EN-US"}

[Memory: 496M total, 341M available, page size 4K]{lang="EN-US"}

[    JID    PID  PRI  State  FDs    MEM  HH:MM:SS    CPU   Name]{lang="EN-US"}

[   1047   1047  120    R     9   1420K  00:02:39  14.13%  diagd]{lang="EN-US"}

[      1      1  120    S    17   1092K  00:00:23   3.98%  scmd]{lang="EN-US"}

[   1027   1027  120    S    12   9280K  00:01:13   1.44%  devd]{lang="EN-US"}

[   1000   1000  115    S     0      0K  00:00:09   0.36%  \[sock/1\]]{lang="EN-US"}

[   1009   1009  115    S     0      0K  00:00:09   0.36%  \[karp/1\]]{lang="EN-US"}

[      4      4  115    S     0      0K  00:00:06   0.18%  \[ksoftirqd/0\]]{lang="EN-US"}

[   1010   1010  115    S     0      0K  00:00:13   0.18%  \[kND/1\]]{lang="EN-US"}

[   4795   4795  120    S    11   2372K  00:00:01   0.18%  telnetd]{lang="EN-US"}

[   5491   5491  120    S     8   1500K  00:00:00   0.18%  top]{lang="EN-US"}

[      2      2  115    S     0      0K  00:00:00   0.00%  \[kthreadd\]]{lang="EN-US"}

[[以上信息会每隔]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_x1063_20800_81925976}[秒刷新一次。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[输入"]{style="font-family:宋体"}]{#struct_0_x1063_20800_1222688335}[h]{lang="EN-US"}["或"]{style="font-family:宋体"}[?]{lang="EN-US"}["，将显示如下帮助信息。]{style="font-family:宋体"}

[[Help for interactive commands:]{lang="EN-US"}]{#struct_0_x1063_20800_x1937581965}

[      ?,h    Show the available interactive commands]{lang="EN-US"}

[        1    Toggle SMP view: \'1\' single/separate states]{lang="EN-US"}

[        c    Sort by the CPU field(default)]{lang="EN-US"}

[        d    Set the delay interval between screen updates]{lang="EN-US"}

[        f    Sort by number of open files]{lang="EN-US"}

[        k    Kill a job]{lang="EN-US"}

[        l    Refresh the screen]{lang="EN-US"}

[        m    Sort by memory used]{lang="EN-US"}

[        n    Set the maximum number of processes to display]{lang="EN-US"}

[        q    Quit the interactive display]{lang="EN-US"}

[        t    Sort by run time of processes since last restart]{lang="EN-US"}

[        \<    Move sort field to the next left column]{lang="EN-US"}

[        \>    Move sort field to the next right column]{lang="EN-US"}

[Press any key to continue]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[输入"]{style="font-family:宋体"}]{#struct_0_x1063_20800_70420569}[d]{lang="EN-US"}["后，根据出现的提示如果输入"]{style="font-family:宋体"}[3]{lang="EN-US"}["，则统计信息将会每隔]{style="font-family:宋体"}[3]{lang="EN-US"}[秒更新一次。]{style="font-family:宋体"}

[[Enter the delay interval between updates(1\~2147483647)]{lang="EN-US"}]{#struct_0_x1063_20800_x188500157}[：]{style="font-family:宋体"}[3]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[输入"]{style="font-family:宋体"}]{#struct_0_x1063_20800_1244284112}[n]{lang="EN-US"}["后，根据出现的提示如果输入"]{style="font-family:宋体"}[5]{lang="EN-US"}["，则显示的进程数目将会变为]{style="font-family:宋体"}[5]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[Enter the max number of procs to display(0 is unlimited)]{lang="EN-US"}]{#struct_0_x1063_20800_x721391189}[：]{style="font-family:宋体"}[5]{lang="EN-US"}

[87 processes; 113 threads; 735 fds]{lang="EN-US"}

[Thread states: 2 running, 111 sleeping, 0 stopped, 0 zombie]{lang="EN-US"}

[CPU states: 86.57% idle, 0.83% user, 11.74% kernel, 0.83% interrupt]{lang="EN-US"}

[Memory: 755M total, 414M available, page size 4K]{lang="EN-US"}

[    JID    PID  PRI  State  FDs    MEM  HH:MM:SS    CPU   Name]{lang="EN-US"}

[    864    864  120    S    24  27020K  00:00:43   8.95%  syslogd]{lang="EN-US"}

[   1173   1173  120    R    24   2664K  00:00:01   2.37%  top]{lang="EN-US"}

[    866    866  120    S    18  10276K  00:00:09   0.69%  devd]{lang="EN-US"}

[      1      1  120    S    16   1968K  00:00:04   0.41%  scmd]{lang="EN-US"}

[    881    881  120    S     8   2420K  00:00:07   0.41%  diagd]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[输入"]{style="font-family:宋体"}]{#struct_0_x1063_20800_x281184855}[f]{lang="EN-US"}["，统计信息将以打开的文件句柄数降序输出（]{style="font-family:宋体"}[c]{lang="EN-US"}[、]{style="font-family:宋体"}[m]{lang="EN-US"}[、]{style="font-family:
宋体"}[t]{lang="EN-US"}[命令字类似）。]{style="font-family:宋体"}

[[87 processes; 113 threads; 735 fds]{lang="EN-US"}]{#struct_0_x1063_20800_x188565693}

[Thread states: 1 running, 112 sleeping, 0 stopped, 0 zombie]{lang="EN-US"}

[CPU states: 90.66% idle, 0.88% user, 5.77% kernel, 2.66% interrupt]{lang="EN-US"}

[Memory: 755M total, 414M available, page size 4K]{lang="EN-US"}

[    JID    PID  PRI  State  FDs    MEM  HH:MM:SS    CPU   Name]{lang="EN-US"}

[    862    862  120    S    61   5384K  00:00:01   0.00%  dbmd]{lang="EN-US"}

[    905    905  120    S    35   2464K  00:00:02   0.00%  ipbased]{lang="EN-US"}

[    863    863  120    S    31   1956K  00:00:00   0.00%  had]{lang="EN-US"}

[    884    884  120    S    31  30600K  00:00:00   0.00%  lsmd]{lang="EN-US"}

[    889    889  120    S    29  61592K  00:00:00   0.00%  routed ]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[输入"]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1486189605}[k]{lang="EN-US"}["后，根据出现的提示如果输入]{style="font-family:宋体"}[884]{lang="EN-US"}[，将会终止此]{style="font-family:宋体"}[JID]{lang="EN-US"}[对应的任务"]{style="font-family:宋体"}[lsmd]{lang="EN-US"}["。]{style="font-family:宋体"}

[[Enter the JID to kill: 884]{lang="EN-US"}]{#struct_0_x1063_20800_x1301474292}

[84 processes; 107 threads; 683 fds]{lang="EN-US"}

[Thread states: 1 running, 106 sleeping, 0 stopped, 0 zombie]{lang="EN-US"}

[CPU states: 59.03% idle, 1.92% user, 37.88% kernel, 1.15% interrupt]{lang="EN-US"}

[Memory: 755M total, 419M available, page size 4K]{lang="EN-US"}

[    JID    PID  PRI  State  FDs    MEM  HH:MM:SS    CPU   Name]{lang="EN-US"}

[    862    862  120    S    56   5384K  00:00:01   0.00%  dbmd]{lang="EN-US"}

[    905    905  120    S    35   2464K  00:00:02   0.00%  ipbased]{lang="EN-US"}

[    863    863  120    S    30   1956K  00:00:00   0.00%  had]{lang="EN-US"}

[    889    889  120    S    29  61592K  00:00:00   0.00%  routed]{lang="EN-US"}

[   1160   1160  120    S    28  23096K  00:00:01   0.19%  sshd]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[输入"]{style="font-family:宋体"}]{#struct_0_x1063_20800_x358044316}[q]{lang="EN-US"}["，将退出交互模式。]{style="font-family:宋体"}

[[表1-13 ]{lang="EN-US"}[monitor process]{lang="EN-US"}]{#struct_0_x1063_20800_881991480}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2103724851}[[字段]{style="font-family:黑体"}]{#struct_0_x1063_20800_x188631229}

[[描述]{style="font-family:黑体"}]{#struct_0_x1063_20800_1249360325}

[[84 processes; 107 threads; 683 fds]{lang="EN-US"}]{#struct_0_x1063_20800_x1028373509}

[[系统的进程总数，线程总数，文件句柄总数]{style="font-family:宋体"}]{#struct_0_x1063_20800_x33837690}

[[Thread states: 1 running, 102 sleeping, 0 stopped, 0 zombie]{lang="EN-US"}]{#struct_0_x1063_20800_x65668868}

[[线程状态：处于]{style="font-family:宋体"}[running]{lang="EN-US"}]{#struct_0_x1063_20800_2051774378}[状态的线程数，处于]{style="font-family:宋体"}[sleeping]{lang="EN-US"}[（包括]{style="font-family:宋体"}[interruptible sleep]{lang="EN-US"}[和]{style="font-family:宋体"}[uninterruptible sleep]{lang="EN-US"}[）状态的线程数，处于]{style="font-family:宋体"}[stopped]{lang="EN-US"}[状态的线程数，处于]{style="font-family:宋体"}[zombie]{lang="EN-US"}[状态的线程数]{style="font-family:宋体"}

[[CPU states]{lang="EN-US"}]{#struct_0_x1063_20800_976438794}

[[CPU]{lang="EN-US"}]{#struct_0_x1063_20800_x188696765}[状态：空闲率，用户态占用率，内核态占用率，中断占用率]{style="font-family:宋体"}

[[Memory]{lang="EN-US"}]{#struct_0_x1063_20800_1236414052}

[[内存状态：总量，可用内存数，]{style="font-family:宋体"}[page]{lang="EN-US"}]{#struct_0_x1063_20800_x1190968794}[大小，单位为]{style="font-family:宋体"}[KB]{lang="EN-US"}

[[JID]{lang="EN-US"}]{#struct_0_x1063_20800_x246249303}

[[任务编号（用于唯一标识一个进程，该编号不会随着进程的重启而改变）]{style="font-family:宋体"}]{#struct_0_x1063_20800_1053043231}

[[PID]{lang="EN-US"}]{#struct_0_x1063_20800_1257883457}

[[进程编号]{style="font-family:宋体"}]{#struct_0_x1063_20800_x188762301}

[[PRI]{lang="EN-US"}]{#struct_0_x1063_20800_x305308713}

[[进程优先级]{style="font-family:宋体"}]{#struct_0_x1063_20800_x413624870}

[[State]{lang="EN-US"}]{#struct_0_x1063_20800_x1978227380}

[[进程状态，可能的取值为：]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1430025472}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[R]{lang="EN-US"}]{#struct_0_x1063_20800_x188827837}[：]{style="font-family:宋体"}[running]{lang="EN-US"}[，运行状态或处于运行队列]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S]{lang="EN-US"}]{#struct_0_x1063_20800_35758912}[：]{lang="EN-US" style="font-family:宋体"}[sleeping]{lang="EN-US"}[，可中断睡眠状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_x1063_20800_x1533497243}[：]{lang="EN-US" style="font-family:宋体"}[traced or stopped]{lang="EN-US"}[，暂停状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_x1063_20800_1618609171}[：]{lang="EN-US" style="font-family:宋体"}[uninterruptible sleep]{lang="EN-US"}[，不可中断睡眠状态]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Z]{lang="EN-US"}]{#struct_0_x1063_20800_1697658138}[：]{lang="EN-US" style="font-family:宋体"}[zombie]{lang="EN-US"}[，僵死状态]{lang="EN-US" style="font-family:宋体"}

[[FDs]{lang="EN-US"}]{#struct_0_x1063_20800_x188893373}

[[file descriptions]{lang="EN-US"}]{#struct_0_x1063_20800_x1890725680}[，进程打开的文件句柄数]{style="font-family:宋体"}

[[MEM]{lang="EN-US"}]{#struct_0_x1063_20800_x1964897185}

[[进程所使用的内存大小（内核线程该项显示为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x1063_20800_x590950900}[）]{style="font-family:宋体"}

[[HH:MM:SS]{lang="EN-US"}]{#struct_0_x1063_20800_x665901431}

[[进程自最近一次启动以来的运行时间]{style="font-family:宋体"}]{#struct_0_x1063_20800_x187910333}

[[CPU]{lang="EN-US"}]{#struct_0_x1063_20800_659047758}

[[进程]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_x1063_20800_x1461932330}[使用率]{style="font-family:宋体"}

[[Name]{lang="EN-US"}]{#struct_0_x1063_20800_39407323}

[[进程名称（如果进程名称带有"]{style="font-family:宋体"}[\[ \]]{lang="EN-US"}]{#struct_0_x1063_20800_x710128988}["标记，则表示该进程为内核线程）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1366243004 .myid}
[]{#_Toc404797209}[]{#struct_0_x1063_20800_x187975869}[]{#_Toc316392157}[]{#_Toc282002496}[]{#_Toc280620238}

**进程监控和维护 \-- 进程监控和维护命令 \-- monitor thread**

------------------------------------------------------------------------

[**[monitor thread]{lang="EN-US"}**]{#struct_0_x1063_20800_1370000464}[命令用来显示线程的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1205390067}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1063_20800_967096474}

[**[monitor thread]{lang="EN-US"}**[ \[ **dumbtty** \] \[ **iteration** *number* \]]{lang="EN-US"}]{#struct_0_x1063_20800_x1284561305}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1063_20800_1563383373}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[monitor]{lang="EN-US"}**[ **thread** \[ **dumbtty** \] \[ **iteration** *number* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_311144896}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1063_20800_2104140289}[模式：]{style="font-family:宋体"}

[**[monitor]{lang="EN-US"}**[ **thread** \[ **dumbtty** \] \[ **iteration** *number* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_x610068720}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1377649323}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1063_20800_x355919024}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1218370775}

[[network-admin]{lang="EN-US"}]{#struct_0_x1063_20800_x1907986754}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1063_20800_1948390324}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1742060549}

[**[dumbtty]{lang="EN-US"}**]{#struct_0_x1063_20800_231527966}[：以哑终端方式显示线程统计信息（即屏幕不支持定时刷新统计信息）。指定该参数时，全部线程的统计信息以]{style="font-family:宋体"}[CPU]{lang="EN-US"}[使用率降序排列输出到屏幕上。不指定该参数时，统计信息以交互模式显示，缺省情况下按]{style="font-family:宋体"}[CPU]{lang="EN-US"}[占用率降序显示前]{style="font-family:宋体"}[10]{lang="EN-US"}[个线程的统计信息，且每隔]{style="font-family:宋体"}[5]{lang="EN-US"}[秒更新一次。]{style="font-family:宋体"}

[**[iteration]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_x1063_20800_498935961}[：进程统计信息的显示次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。指定]{style="font-family:宋体"}**[dumbtty]{lang="EN-US"}**[参数时]{style="font-family:宋体"}*[number]{lang="EN-US"}*[的缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[；不指定]{style="font-family:宋体"}**[dumbtty]{lang="EN-US"}**[且不配置]{style="font-family:宋体"}*[number]{lang="EN-US"}*[参数时*，*表示显示次数没有限制，统计信息会一直显示。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x2127416814}[：表示单板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_372746503}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x445631443}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x883849681}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_2009404729}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1063_20800_663625819}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1063_20800_508743183}

[[不指定]{style="font-family:宋体"}**[dumbtty]{lang="EN-US"}**]{#struct_0_x1063_20800_x740893810}[参数的情况下，统计信息以交互模式显示。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交互模式下，系统会自动计算可显示的线程个数，超过屏幕范围的不作显示。]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1700422345}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交互模式下，用户可通过输入]{style="font-family:宋体"}]{#struct_0_x1063_20800_x2100460398}[[[表]{style="font-family:宋体"}1-14]{lang="EN-US"}](?-1366243004#_Ref282593016)[中指定的交互命令字来执行相应的操作。]{style="font-family:宋体"}

[]{#struct_0_x1063_20800_x879619735}[[表1-14 ]{lang="EN-US"}[monitor thread]{lang="EN-US"}]{#_Ref282593016}[命令支持的交互命令字描述表]{style="font-family:黑体"}

[]{#table_struct_0_2101044371}[[命令字]{style="font-family:黑体"}]{#struct_0_x1063_20800_1087433035}
:::

[[功能描述]{style="font-family:黑体"}]{#struct_0_x1063_20800_1377518251}

[[?]{lang="EN-US"}]{#struct_0_x1063_20800_401379209}[或]{style="font-family:宋体"}[h]{lang="EN-US"}

[[帮助信息，显示可用的交互式命令字]{style="font-family:宋体"}]{#struct_0_x1063_20800_629213000}

[[d]{lang="EN-US"}]{#struct_0_x1063_20800_x853853497}

[[设置统计信息的更新时间间隔，缺省值为]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_x1063_20800_x1387752125}[秒]{style="font-family:宋体"}

[[k]{lang="EN-US"}]{#struct_0_x1063_20800_1384911538}

[[终止一个任务（进程），此命令会影响系统运行，请谨慎使用]{style="font-family:宋体"}]{#struct_0_x1063_20800_1377452715}

[[l]{lang="EN-US"}]{#struct_0_x1063_20800_x1174004296}

[[刷新屏幕]{style="font-family:宋体"}]{#struct_0_x1063_20800_318529577}

[[n]{lang="EN-US"}]{#struct_0_x1063_20800_x1631144526}

[[改变显示的线程个数，取值为]{style="font-family:宋体"}[0\~2147483647]{lang="EN-US"}]{#struct_0_x1063_20800_1782984313}[（缺省值为]{style="font-family:宋体"}[10]{lang="EN-US"}[个，]{style="font-family:宋体"}[0]{lang="EN-US"}[表示不作限制）；超过屏幕范围时，仍只显示一屏内可容纳的线程个数]{style="font-family:宋体"}

[[q]{lang="EN-US"}]{#struct_0_x1063_20800_x1887287115}

[[退出交互模式]{style="font-family:宋体"}]{#struct_0_x1063_20800_1377387179}

[[\<]{lang="EN-US"}]{#struct_0_x1063_20800_x449479632}[ ]{lang="EN-US"}

[[排序项向左移动一列]{style="font-family:宋体"}]{#struct_0_x1063_20800_x800183614}

[[\>]{lang="EN-US"}]{#struct_0_x1063_20800_386628677}[ ]{lang="EN-US"}

[[排序项向右移动一列]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1689057625}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1411134110}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_1377321643}[以哑终端方式显示线程统计信息。]{style="font-family:宋体"}

[[\<Sysname\> monitor thread dumbtty]{lang="EN-US"}]{#struct_0_x1063_20800_1561051275}

[84 processes; 107 threads]{lang="EN-US"}

[Thread states: 1 running, 106 sleeping, 0 stopped, 0 zombie]{lang="EN-US"}

[CPU states: 83.19% idle, 1.68% user, 10.08% kernel, 5.04% interrupt]{lang="EN-US"}

[Memory: 755M total, 417M available, page size 4K]{lang="EN-US"}

[    JID    TID  LAST_CPU  PRI  State  HH:MM:SS   MAX    CPU    Name]{lang="EN-US"}

[   1175   1175      0     120    R    00:00:00     1  10.75%   top]{lang="EN-US"}

[      1      1      0     120    S    00:00:06     1   2.68%   scmd]{lang="EN-US"}

[    881    881      0     120    S    00:00:09     1   2.01%   diagd]{lang="EN-US"}

[    776    776      0     120    S    00:00:01     0   0.67%   \[DEVD\]]{lang="EN-US"}

[    866    866      0     120    S    00:00:11     1   0.67%   devd]{lang="EN-US"}

[      2      2      0     115    S    00:00:00     0   0.00%   \[kthreadd\]]{lang="EN-US"}

[      3      3      0     115    S    00:00:01     0   0.00%   \[ksoftirqd/0\]]{lang="EN-US"}

[      4      4      0      99    S    00:00:00     1   0.00%   \[watchdog/0\]]{lang="EN-US"}

[      5      5      0     115    S    00:00:00     0   0.00%   \[events/0\]]{lang="EN-US"}

[      6      6      0     115    S    00:00:00     0   0.00%   \[khelper\]]{lang="EN-US"}

[    796    796      0     115    S    00:00:00     0   0.00%   \[kip6fs/1\]]{lang="EN-US"}

[ ]{lang="EN-US"}

[\<Sysname\>]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_2010040429}[以交互模式显示线程统计信息。]{style="font-family:宋体"}

[[\<Sysname\> monitor thread]{lang="EN-US"}]{#struct_0_x1063_20800_1377256107}

[84 processes; 107 threads]{lang="EN-US"}

[Thread states: 1 running, 106 sleeping, 0 stopped, 0 zombie]{lang="EN-US"}

[CPU states: 94.43% idle, 0.76% user, 3.64% kernel, 1.15% interrupt]{lang="EN-US"}

[Memory: 755M total, 417M available, page size 4K]{lang="EN-US"}

[    JID    TID  LAST_CPU  PRI  State  HH:MM:SS   MAX    CPU    Name]{lang="EN-US"}

[   1176   1176      0     120    R    00:00:01     1   3.42%   top]{lang="EN-US"}

[    866    866      0     120    S    00:00:12     1   0.85%   devd]{lang="EN-US"}

[    881    881      0     120    S    00:00:09     1   0.64%   diagd]{lang="EN-US"}

[      1      1      0     120    S    00:00:06     1   0.42%   scmd]{lang="EN-US"}

[   1160   1160      0     120    S    00:00:01     1   0.21%   sshd]{lang="EN-US"}

[      2      2      0     115    S    00:00:00     0   0.00%   \[kthreadd\]]{lang="EN-US"}

[      3      3      0     115    S    00:00:01     0   0.00%   \[ksoftirqd/0\]]{lang="EN-US"}

[      4      4      0      99    S    00:00:00     1   0.00%   \[watchdog/0\]]{lang="EN-US"}

[      5      5      0     115    S    00:00:00     0   0.00%   \[events/0\]]{lang="EN-US"}

[      6      6      0     115    S    00:00:00     0   0.00%   \[khelper\]]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[输入"]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1996492565}[h]{lang="EN-US"}["或"]{style="font-family:宋体"}[?]{lang="EN-US"}["，帮助信息显示如下：]{style="font-family:宋体"}

[[Help for interactive commands]{lang="EN-US"}]{#struct_0_x1063_20800_1377190571}[：]{style="font-family:
宋体"}

[        ?,h      Show the available interactive commands]{lang="EN-US"}

[          c      Sort by the CPU field(default)]{lang="EN-US"}

[          d      Set the delay interval between screen updates]{lang="EN-US"}

[          k      Kill a job]{lang="EN-US"}

[          l      Refresh the screen]{lang="EN-US"}

[          n      Set the maximum number of threads to display]{lang="EN-US"}

[          q      Quit the interactive display]{lang="EN-US"}

[          t      Sort by run time of threads since last restart]{lang="EN-US"}

[          \<      Move sort field to the next left column]{lang="EN-US"}

[          \>      Move sort field to the next right column]{lang="EN-US"}

[Press any key to continue]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[输入"]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1978583829}[d]{lang="EN-US"}["后，根据出现的提示如果输入"]{style="font-family:宋体"}[3]{lang="EN-US"}["，统计信息将会每隔]{style="font-family:宋体"}[3]{lang="EN-US"}[秒更新一次。]{style="font-family:宋体"}

[[Enter the delay interval between screen updates]{lang="EN-US"}]{#struct_0_x1063_20800_785025890}[（]{style="font-family:宋体"}[1\~2147483647]{lang="EN-US"}[）：]{style="font-family:宋体"}[3]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[输入"]{style="font-family:宋体"}]{#struct_0_x1063_20800_1851502625}[n]{lang="EN-US"}["后，根据出现的提示如果输入"]{style="font-family:宋体"}[5]{lang="EN-US"}["，显示的线程数目将会变为]{style="font-family:宋体"}[5]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[Enter the max number of threads to display(0 means unlimited)]{lang="EN-US"}]{#struct_0_x1063_20800_1378173611}[：]{style="font-family:宋体"}[5]{lang="EN-US"}

[84 processes; 107 threads]{lang="EN-US"}

[Thread states: 1 running, 106 sleeping, 0 stopped, 0 zombie]{lang="EN-US"}

[CPU states: 93.26% idle, 0.99% user, 4.23% kernel, 1.49% interrupt]{lang="EN-US"}

[Memory: 755M total, 417M available, page size 4K]{lang="EN-US"}

[    JID    TID  LAST_CPU  PRI  State  HH:MM:SS   MAX    CPU    Name]{lang="EN-US"}

[   1176   1176      0     120    R    00:00:02     1   3.71%   top]{lang="EN-US"}

[      1      1      0     120    S    00:00:06     1   0.92%   scmd]{lang="EN-US"}

[    866    866      0     120    S    00:00:13     1   0.69%   devd]{lang="EN-US"}

[    881    881      0     120    S    00:00:10     1   0.69%   diagd]{lang="EN-US"}

[    720    720      0     115    D    00:00:01     0   0.23%   \[TMTH\]]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[输入"]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1754748540}[k]{lang="EN-US"}["后，根据出现的提示输入]{style="font-family:宋体"}[881]{lang="EN-US"}[，将会终止此]{style="font-family:宋体"}[JID]{lang="EN-US"}[对应的任务]{style="font-family:宋体"}[diagd]{lang="EN-US"}[。]{style="font-family:宋体"}

[[Enter the JID to kill]{lang="EN-US"}]{#struct_0_x1063_20800_1319969274}[：]{style="font-family:宋体"}[881]{lang="EN-US"}

[83 processes; 106 threads]{lang="EN-US"}

[Thread states: 1 running, 105 sleeping, 0 stopped, 0 zombie]{lang="EN-US"}

[CPU states: 96.26% idle, 0.54% user, 2.63% kernel, 0.54% interrupt]{lang="EN-US"}

[Memory: 755M total, 418M available, page size 4K]{lang="EN-US"}

[    JID    TID  LAST_CPU  PRI  State  HH:MM:SS   MAX    CPU    Name]{lang="EN-US"}

[   1176   1176      0     120    R    00:00:04     1   1.86%   top]{lang="EN-US"}

[    866    866      0     120    S    00:00:14     1   0.87%   devd]{lang="EN-US"}

[      1      1      0     120    S    00:00:07     1   0.49%   scmd]{lang="EN-US"}

[    730    730      0       0    S    00:00:04     1   0.12%   \[DIBC\]]{lang="EN-US"}

[    762    762      0     120    S    00:00:22     1   0.12%   \[MNET\]]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[输入"]{style="font-family:宋体"}]{#struct_0_x1063_20800_605697086}[q]{lang="EN-US"}["，将退出交互模式。]{style="font-family:宋体"}

[[表1-15 ]{lang="EN-US"}[monitor thread]{lang="EN-US"}]{#struct_0_x1063_20800_x546109387}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2126769203}[[显示项]{style="font-family:黑体"}]{#struct_0_x1063_20800_708782645}

[[内容描述]{style="font-family:黑体"}]{#struct_0_x1063_20800_1378108075}

[[84 processes; 107 threads]{lang="EN-US"}]{#struct_0_x1063_20800_604540947}

[[系统的进程总数，线程总数]{style="font-family:宋体"}]{#struct_0_x1063_20800_x238862521}

[[Thread states]{lang="EN-US"}]{#struct_0_x1063_20800_172280911}

[[线程状态：处于]{style="font-family:宋体"}[running]{lang="EN-US"}]{#struct_0_x1063_20800_x72332213}[状态的线程数，处于]{style="font-family:宋体"}[sleeping]{lang="EN-US"}[（包括]{style="font-family:宋体"}[interruptible sleep]{lang="EN-US"}[和]{style="font-family:宋体"}[uninterruptible sleep]{lang="EN-US"}[）状态的线程数，处于]{style="font-family:宋体"}[stopped]{lang="EN-US"}[状态的线程数，处于]{style="font-family:宋体"}[zombie]{lang="EN-US"}[状态的线程数]{style="font-family:宋体"}

[[CPU states]{lang="EN-US"}]{#struct_0_x1063_20800_x1597314487}

[[CPU]{lang="EN-US"}]{#struct_0_x1063_20800_1377649324}[状态：空闲率，用户态占用率，内核态占用率，中断占用率]{style="font-family:宋体"}

[[Memory]{lang="EN-US"}]{#struct_0_x1063_20800_x356377776}

[[内存状态：总量，可用内存数，]{style="font-family:宋体"}[page]{lang="EN-US"}]{#struct_0_x1063_20800_x2088582670}[大小]{style="font-family:宋体"}

[[JID]{lang="EN-US"}]{#struct_0_x1063_20800_2110775021}

[[任务编号，用于唯一标识一个进程，该编号不会随着进程的重启而改变]{style="font-family:宋体"}]{#struct_0_x1063_20800_134698584}

[[TID]{lang="EN-US"}]{#struct_0_x1063_20800_1377583788}

[[线程编号]{style="font-family:宋体"}]{#struct_0_x1063_20800_372812039}

[[LAST_CPU]{lang="EN-US"}]{#struct_0_x1063_20800_1884498757}

[[线程最近一次被调度所在的]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_x1063_20800_1133171217}[的编号]{style="font-family:宋体"}

[[PRI]{lang="EN-US"}]{#struct_0_x1063_20800_x1804165022}

[[线程优先级]{style="font-family:宋体"}]{#struct_0_x1063_20800_1234060283}

[[State]{lang="EN-US"}]{#struct_0_x1063_20800_1377518252}

[[进程状态，可能的取值为：]{style="font-family:宋体"}]{#struct_0_x1063_20800_401313673}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[R]{lang="EN-US"}]{#struct_0_x1063_20800_1011472632}[：]{style="font-family:宋体"}[running]{lang="EN-US"}[，运行状态或处于运行队列]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S]{lang="EN-US"}]{#struct_0_x1063_20800_x17753236}[：]{lang="EN-US" style="font-family:宋体"}[sleeping]{lang="EN-US"}[，可中断睡眠状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_x1063_20800_x270079080}[：]{lang="EN-US" style="font-family:宋体"}[traced or stopped]{lang="EN-US"}[，暂停状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_x1063_20800_1377452716}[：]{lang="EN-US" style="font-family:宋体"}[uninterruptible sleep]{lang="EN-US"}[，不可中断睡眠状态]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Z]{lang="EN-US"}]{#struct_0_x1063_20800_x1174069832}[：]{lang="EN-US" style="font-family:宋体"}[zombie]{lang="EN-US"}[，僵死状态]{lang="EN-US" style="font-family:宋体"}

[[HH:MM:SS]{lang="EN-US"}]{#struct_0_x1063_20800_x1079962371}

[[线程自最近一次启动以来的运行时间]{style="font-family:宋体"}]{#struct_0_x1063_20800_1586796579}

[[MAX]{lang="EN-US"}]{#struct_0_x1063_20800_1377387180}

[[线程单次调度占用]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_x1063_20800_x450069463}[的最长时间，以毫秒为单位]{style="font-family:宋体"}

[[CPU]{lang="EN-US"}]{#struct_0_x1063_20800_1070408160}

[[线程]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_x1063_20800_1893961641}[使用率]{style="font-family:宋体"}

[[Name]{lang="EN-US"}]{#struct_0_x1063_20800_1377321644}

[[线程名称（如果线程名称带有"]{style="font-family:宋体"}[\[ \]]{lang="EN-US"}]{#struct_0_x1063_20800_1560854667}["标记，则表示该线程为内核线程）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1363718947 .myid}
[]{#_Toc404797210}[]{#struct_0_x1063_20800_1102968475}[]{#_Toc358901100}[]{#_Toc340215436}

**进程监控和维护 \-- 进程监控和维护命令 \-- process core**

------------------------------------------------------------------------

[**[process]{lang="EN-US"}**[ **core**]{lang="EN-US"}]{#struct_0_x1063_20800_1102771867}[命令用来开启]{style="font-family:宋体"}[/]{lang="EN-US"}[关闭用户态进程异常时的生成]{style="font-family:宋体"}[core]{lang="EN-US"}[文件的功能，以及配置能生成的]{style="font-family:宋体"}[core]{lang="EN-US"}[文件的最大个数。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_700946474}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1063_20800_1228463080}

[**[process]{lang="EN-US"}**[ **core** { **maxcore** *value* \| **off** } { **job** *job-id \|* **name** *process-name* }]{lang="EN-US"}]{#struct_0_x1063_20800_1102837403}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1063_20800_x1657634637}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[process]{lang="EN-US"}**[ **core** { **maxcore** *value* \| **off** } { **job** *job-id* \| **name** *process-name* } \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_727928293}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1063_20800_1103165083}[模式：]{style="font-family:宋体"}

[**[process]{lang="EN-US"}**[ **core** { **maxcore** *value* \| **off** } { **job** *job-id* \| **name** *process-name* } \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_1051945674}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x172892954}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1063_20800_1103230619}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1063_20800_676275243}

[[同一用户态进程在首次异常时会生成]{style="font-family:宋体"}[core]{lang="EN-US"}]{#struct_0_x1063_20800_x1378476424}[文件，后续异常不再生成]{style="font-family:宋体"}[core]{lang="EN-US"}[文件。即]{style="font-family:宋体"}**[maxcore]{lang="EN-US"}**[的最大数值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x7641246}

[[network-admin]{lang="EN-US"}]{#struct_0_x1063_20800_1103034011}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1063_20800_x1674906027}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x938685771}

[**[off]{lang="EN-US"}**]{#struct_0_x1063_20800_1103099547}[：表示关闭用户态进程异常时生成]{style="font-family:宋体"}[core]{lang="EN-US"}[文件的功能。]{style="font-family:宋体"}

[**[maxcore]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x1063_20800_1784364385}[：表示开启用户态进程的]{style="font-family:宋体"}[core]{lang="EN-US"}[文件生成功能，并配置能生成的]{style="font-family:宋体"}[core]{lang="EN-US"}[文件的最大个数。]{style="font-family:宋体"}*[value]{lang="EN-US"}*[表示用户态进程能生成的]{style="font-family:宋体"}[core]{lang="EN-US"}[文件的最大个数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}**[ *process-name*]{lang="EN-US"}]{#struct_0_x1063_20800_1873824248}[：用户态进程的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}**[process core]{lang="EN-US"}**[命令的配置对用户态进程下的所有实例有效。]{style="font-family:宋体"}

[**[job]{lang="EN-US"}***[ job-id]{lang="EN-US"}*]{#struct_0_x1063_20800_1103427227}[：任务]{style="font-family:宋体"}[ID]{lang="EN-US"}[，用于唯一标识一个进程，该]{style="font-family:宋体"}[ID]{lang="EN-US"}[不会随着进程的重启而改变，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x484802247}[：表示单板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_1103492763}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x445762514}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_1486759996}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_1420117709}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1063_20800_664084568}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1448819246}

[[开启用户态进程的]{style="font-family:宋体"}[core]{lang="EN-US"}]{#struct_0_x1063_20800_1102902938}[文件生成功能，并配置能生成的]{style="font-family:宋体"}[core]{lang="EN-US"}[文件的最大个数后，用户态进程异常重启一次，就会产生一个]{style="font-family:宋体"}[core]{lang="EN-US"}[文件并记录用户态进程的异常信息。如果生成的]{style="font-family:宋体"}[core]{lang="EN-US"}[文件的数目达到最大值，则不再生成新的]{style="font-family:宋体"}[core]{lang="EN-US"}[文件。软件开发和维护人员能够根据]{style="font-family:宋体"}[core]{lang="EN-US"}[文件的内容来定位异常的原因和异常的位置。]{style="font-family:宋体"}

[[因为生成的]{style="font-family:宋体"}[core]{lang="EN-US"}]{#struct_0_x1063_20800_x841467508}[文件会占用系统存储资源，如果用户对某些用户态进程的异常退出不关心，可以关闭这些用户态进程的]{style="font-family:宋体"}[core]{lang="EN-US"}[文件记录功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1063_20800_590072391}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_1102968474}[关闭用户态进程]{style="font-family:宋体"}[routed]{lang="EN-US"}[的]{style="font-family:宋体"}[core]{lang="EN-US"}[文件生成功能。]{style="font-family:宋体"}

[[\<Sysname\> process core off name routed]{lang="EN-US"}]{#struct_0_x1063_20800_x899954786}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_1301346558}[开启用户态进程]{style="font-family:宋体"}[routed]{lang="EN-US"}[的]{style="font-family:宋体"}[core]{lang="EN-US"}[文件生成功能，并且最多可生成]{style="font-family:宋体"}[5]{lang="EN-US"}[个]{style="font-family:宋体"}[core]{lang="EN-US"}[文件。]{style="font-family:宋体"}

[[\<Sysname\> process core maxcore 5 name routed]{lang="EN-US"}]{#struct_0_x1063_20800_1102771866}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_701012010}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}**]{#struct_0_x1063_20800_x1205277824}**[exception ]{lang="EN-US"}[context]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[exception filepath]{lang="EN-US"}**]{#struct_0_x1063_20800_1102837402}
:::

::: {#1428207943 .myid}
[]{#_Toc404797211}[]{#struct_0_x1063_20800_x1657569101}[]{#_Toc358901101}[]{#_Toc340215440}

**进程监控和维护 \-- 进程监控和维护命令 \-- reset exception context**

------------------------------------------------------------------------

[**[reset exception context]{lang="EN-US"}**]{#struct_0_x1063_20800_x479683055}[命令用来清除用户态进程异常时记录的上下文信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1103165082}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1063_20800_1051880138}

[**[reset exception context]{lang="EN-US"}**]{#struct_0_x1063_20800_x1377557494}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1063_20800_1103230618}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset]{lang="EN-US"}**[ **exception context** \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_676340779}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1063_20800_x1015781994}[模式：]{style="font-family:宋体"}

[**[reset exception context]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_1103034010}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1674840491}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1157263877}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1103099546}

[[network-admin]{lang="EN-US"}]{#struct_0_x1063_20800_1784429921}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1063_20800_789071538}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1103427226}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x484867783}[：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_285975367}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中设备的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_1103492762}[：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1063_20800_663756888}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1448884782}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_x1151831958}[清除用户态进程异常记录。]{style="font-family:宋体"}

[[\<Sysname\> reset exception context]{lang="EN-US"}]{#struct_0_x1063_20800_1102902937}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x840746612}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display exception context]{lang="EN-US"}**]{#struct_0_x1063_20800_x961784368}
:::

::: {#-324115247 .myid}
[]{#_Toc404797212}[]{#struct_0_x1063_20800_x706468555}[]{#_Toc329093669}[]{#_Toc329099064}[]{#_Toc329093670}[]{#_Toc329099065}[]{#_Toc329093671}[]{#_Toc329099066}[]{#_Toc329093672}[]{#_Toc329099067}[]{#_Toc329093673}[]{#_Toc329099068}[]{#_Toc329093674}[]{#_Toc329099069}[]{#_Toc329093675}[]{#_Toc329099070}[]{#_Toc329093676}[]{#_Toc329099071}[]{#_Toc329093677}[]{#_Toc329099072}[]{#_Toc329093678}[]{#_Toc329099073}[]{#_Toc329093679}[]{#_Toc329099074}[]{#_Toc329093680}[]{#_Toc329099075}[]{#_Toc329093681}[]{#_Toc329099076}[]{#_Toc329093682}[]{#_Toc329099077}[]{#_Toc329093683}[]{#_Toc329099078}[]{#_Toc329093684}[]{#_Toc329099079}[]{#_Toc329093685}[]{#_Toc329099080}[]{#_Toc329093686}[]{#_Toc329099081}[]{#_Toc329093687}[]{#_Toc329099082}[]{#_Toc329093688}[]{#_Toc329099083}[]{#_Toc329093689}[]{#_Toc329099084}[]{#_Toc329093690}[]{#_Toc329099085}[]{#_Toc329093691}[]{#_Toc329099086}[]{#_Toc329093692}[]{#_Toc329099087}[]{#_Toc329093693}[]{#_Toc329099088}[]{#_Toc329093694}[]{#_Toc329099089}[]{#_Toc329093695}[]{#_Toc329099090}[]{#_Toc329093696}[]{#_Toc329099091}[]{#_Toc329093697}[]{#_Toc329099092}[]{#_Toc329093698}[]{#_Toc329099093}[]{#_Toc329093699}[]{#_Toc329099094}[]{#_Toc329093700}[]{#_Toc329099095}[]{#_Toc329093701}[]{#_Toc329099096}[]{#_Toc329093702}[]{#_Toc329099097}[]{#_Toc329093703}[]{#_Toc329099098}[]{#_Toc329093704}[]{#_Toc329099099}[]{#_Toc329093705}[]{#_Toc329099100}[]{#_Toc329093706}[]{#_Toc329099101}[]{#_Toc329093707}[]{#_Toc329099102}[]{#_Toc329093708}[]{#_Toc329099103}[]{#_Toc329093709}[]{#_Toc329099104}[]{#_Toc329093710}[]{#_Toc329099105}[]{#_Toc329093711}[]{#_Toc329099106}[]{#_Toc329093712}[]{#_Toc329099107}[]{#_Toc329093713}[]{#_Toc329099108}[]{#_Toc329093714}[]{#_Toc329099109}[]{#_Toc329093715}[]{#_Toc329099110}[]{#_Toc329093716}[]{#_Toc329099111}[]{#_Toc329093717}[]{#_Toc329099112}[]{#_Toc329093718}[]{#_Toc329099113}

**进程监控和维护 \-- 进程监控和维护命令 \-- reset kernel deadloop**

------------------------------------------------------------------------

[**[reset kernel deadloop]{lang="EN-US"}**]{#struct_0_x1063_20800_x1234987458}[命令用来清除内核线程死循环信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1893550157}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1775478777}

[**[reset kernel deadloop]{lang="EN-US"}**]{#struct_0_x1063_20800_327180519}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1063_20800_2102692069}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset kernel deadloop ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_1377256108}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1063_20800_x1997082389}[模式：]{style="font-family:宋体"}

[**[reset kernel deadloop ]{lang="EN-US"}**[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_1120665495}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1402939948}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1063_20800_1714042177}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1823742965}

[[network-admin]{lang="EN-US"}]{#struct_0_x1063_20800_x1992614725}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1467306133}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x1899709405}[：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_1377190572}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中设备的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x1978649365}[：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1063_20800_663625816}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1692433069}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_1199429767}[清除内核线程死循环信息。]{style="font-family:宋体"}

[[\<Sysname\> reset kernel deadloop]{lang="EN-US"}]{#struct_0_x1063_20800_x513458508}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_99055476}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display kernel]{lang="EN-US"}**]{#struct_0_x1063_20800_1123971811}**[ ]{lang="EN-US"}[deadloop]{lang="EN-US"}**
:::

::: {#-845802021 .myid}
[]{#_Toc404797213}[]{#struct_0_x1063_20800_1203021653}

**进程监控和维护 \-- 进程监控和维护命令 \-- reset kernel exception**

------------------------------------------------------------------------

[**[reset kernel exception]{lang="EN-US"}**]{#struct_0_x1063_20800_1378173612}[命令用来清除内核线程的异常信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1754551932}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1167139719}

[**[reset kernel exception]{lang="EN-US"}**]{#struct_0_x1063_20800_1868710957}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1063_20800_83776368}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset kernel exception ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_1808327091}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1063_20800_943751639}[模式：]{style="font-family:宋体"}

[**[reset kernel exception ]{lang="EN-US"}**[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_x2106701469}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1582579481}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1063_20800_1378108076}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1063_20800_604606483}

[[network-admin]{lang="EN-US"}]{#struct_0_x1063_20800_117134312}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1063_20800_864201159}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x1263611392}[：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_1799371127}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中设备的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x224795598}[：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1063_20800_663560280}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1242127437}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_x544930912}[清除内核线程的异常信息。]{style="font-family:宋体"}

[[\<Sysname\> reset kernel exception]{lang="EN-US"}]{#struct_0_x1063_20800_1377649321}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x356050096}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**]{#struct_0_x1063_20800_647098780}**[ kernel]{lang="EN-US"}[ exception]{lang="EN-US"}**
:::

::: {#-1422962547 .myid}
[]{#_Toc404797214}[]{#struct_0_x1063_20800_x1164222672}

**进程监控和维护 \-- 进程监控和维护命令 \-- reset kernel reboot**

------------------------------------------------------------------------

[**[reset kernel reboot]{lang="EN-US"}**]{#struct_0_x1063_20800_56030479}[命令用来清除内核线程重启信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_114848122}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1887324177}

[**[reset kernel reboot]{lang="EN-US"}**]{#struct_0_x1063_20800_535855620}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1063_20800_1670338768}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset kernel reboot ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_1377583785}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1063_20800_372615431}[模式：]{style="font-family:宋体"}

[**[reset kernel reboot ]{lang="EN-US"}**[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_x280995631}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1459260501}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1063_20800_x1005247149}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1063_20800_937731310}

[[network-admin]{lang="EN-US"}]{#struct_0_x1063_20800_1531299789}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x55884399}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_1377518249}[：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_401903496}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中设备的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_159957640}[：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1063_20800_663953497}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1113735487}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_1959944845}[清除内核线程重启信息。]{style="font-family:宋体"}

[[\<Sysname\> reset kernel reboot]{lang="EN-US"}]{#struct_0_x1063_20800_1861964162}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x136764141}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}**]{#struct_0_x1063_20800_1078530118}**[kernel reboot]{lang="EN-US"}**
:::

::: {#204190232 .myid}
[]{#_Toc404797215}[]{#struct_0_x1063_20800_x650234779}

**进程监控和维护 \-- 进程监控和维护命令 \-- reset kernel starvation**

------------------------------------------------------------------------

[**[reset kernel starvation]{lang="EN-US"}**]{#struct_0_x1063_20800_1377452713}[命令用来清除内核线程饿死信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x1174397512}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1063_20800_610898227}

[**[reset kernel starvation]{lang="EN-US"}**]{#struct_0_x1063_20800_x919396905}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1063_20800_x692339854}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset kernel starvation ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_x1459614613}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1063_20800_x232455709}[模式：]{style="font-family:宋体"}

[**[reset kernel starvation ]{lang="EN-US"}**[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1063_20800_1787927436}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1785975836}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1063_20800_1377387177}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x449610704}

[[network-admin]{lang="EN-US"}]{#struct_0_x1063_20800_x1932914288}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x909553249}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x426017620}[：表示主控板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_x1893823525}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中设备的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1063_20800_1116170938}[：表示指定成员设备上的指定主控板。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1063_20800_663625817}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1063_20800_x2143746811}

[[\# ]{lang="EN-US"}]{#struct_0_x1063_20800_x2144060580}[清除内核线程饿死信息。]{style="font-family:宋体"}

[[\<Sysname\> reset kernel starvation]{lang="EN-US"}]{#struct_0_x1063_20800_1377321641}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1063_20800_1561182347}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}**]{#struct_0_x1063_20800_x1921106714}**[kernel ]{lang="EN-US"}[starvation]{lang="EN-US"}**
:::
