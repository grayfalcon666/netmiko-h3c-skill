::: {#1678689453 .myid}
[]{#_Toc404800752}[]{#struct_0_x2117_x1183_x392820094}[]{#_Toc347740119}

**配置文件管理 \-- 配置文件管理 Probe命令 \-- display system internal startup cache**

------------------------------------------------------------------------

[**[display system internal startup cache]{lang="EN-US"}**]{#struct_0_x2117_x1183_x1071569232}[命令用来显示设备本次启动时使用的二进制配置文件的路径，如]{style="font-family:宋体"}[flash:/startup.mdb]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2117_x1183_1937469502}

[**[display system internal startup cache]{lang="EN-US"}**]{#struct_0_x2117_x1183_1164002516}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2117_x1183_x1095353087}

[[Probe]{lang="EN-US"}]{#struct_0_x2117_x1183_328026860}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2117_x1183_355322326}

[[network-admin]{lang="EN-US"}]{#struct_0_x2117_x1183_772521593}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2117_x1183_678739017}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2117_x1183_631462224}

[[用户执行]{style="font-family:宋体"}**[save]{lang="EN-US"}**]{#struct_0_x2117_x1183_x611058368}[命令保存配置时，系统会自动生成一个字符串类型的配置文件和一个二进制类型的配置文件。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[字符串类型的配置文件是一个文本文件，文件名后缀为"]{style="font-family:宋体"}]{#struct_0_x2117_x1183_x479693170}[.cfg]{lang="EN-US"}["，可以通过]{style="font-family:宋体"}[more]{lang="EN-US"}[命令查看该文件的内容。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[二进制类型的配置文件是字符串类型的配置文件的二进制格式，文件名后缀为"]{style="font-family:宋体"}]{#struct_0_x2117_x1183_1937797182}[.mdb]{lang="EN-US"}["。在设备启动和运行时，系统软件能够解析该类配置文件，而用户却不能读取和编辑文件内容。]{style="font-family:宋体"}

[[两个文件保存的配置相同，但格式不同。设备启动的时候，会优先使用二进制类型的配置文件，以便提高加载配置的速度。如果没有找到合适的二进制类型的配置文件，才使用字符串类型的配置文件。]{style="font-family:宋体"}]{#struct_0_x2117_x1183_433305313}

[[当设备本次启动使用的是二进制类型的配置文件时，使用该命令会显示该二进制文件的路径；当设备本次启动使用的是字符串类型的配置文件时，使用该命令将显示]{style="font-family:宋体"}[None]{lang="EN-US"}]{#struct_0_x2117_x1183_1569027250}[。]{style="font-family:宋体"}

[ ]{lang="EN-US"}
:::
