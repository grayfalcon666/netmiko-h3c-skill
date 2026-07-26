::: {#-1740567205 .myid}
[]{#_Toc404794030}[]{#struct_0_x1322_x1237_x1927204411}[]{#_Toc343590064}[]{#_Toc343590013}

**FIPS \-- FIPS配置命令 \-- dispaly fips status**

------------------------------------------------------------------------

[**[display fips status]{lang="EN-US"}**]{#struct_0_x1322_x1237_1585486480}[命令用来显示当前的]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}[       ]{lang="EN-US"}]{#struct_0_x1322_x1237_441999403}

[**[display fips status]{lang="EN-US"}**]{#struct_0_x1322_x1237_2143652271}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1322_x1237_x1828303260}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1322_x1237_2126978497}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1322_x1237_875547365}

[[network-admin]{lang="EN-US"}]{#struct_0_x1322_x1237_x1887510433}

[[network-operator]{lang="EN-US"}]{#struct_0_x1322_x1237_x153843206}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1322_x1237_1047762236}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1322_x1237_x1080993214}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1322_x1237_x2014758440}

[[\# ]{lang="EN-US"}]{#struct_0_x1322_x1237_2143717807}[显示当前的]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式状态。]{style="font-family:宋体"}

[[\<Sysname\> display fips status]{lang="EN-US"}]{#struct_0_x1322_x1237_1731981359}

[FIPS mode is enabled.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1322_x1237_248815451}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fips mode enable]{lang="EN-US"}**]{#struct_0_x1322_x1237_x1557971717}
:::

::: {#2141346042 .myid}
[]{#_Toc404794031}[]{#struct_0_x1322_x1237_x1504267361}[]{#_Toc343590062}[]{#_Toc343590011}

**FIPS \-- FIPS配置命令 \-- fips mode enable**

------------------------------------------------------------------------

[**[fips mode enable]{lang="EN-US"}**]{#struct_0_x1322_x1237_x1798960812}[命令用来使能]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[**[undo fips mode enable]{lang="EN-US"}**]{#struct_0_x1322_x1237_x1134308184}[命令用来关闭]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1322_x1237_x1207708479}

[**[fips mode enable]{lang="EN-US"}**]{#struct_0_x1322_x1237_1874517413}

[**[undo fips mode enable]{lang="EN-US"}**]{#struct_0_x1322_x1237_x1821672596}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1322_x1237_2143783343}

[[FIPS]{lang="EN-US"}]{#struct_0_x1322_x1237_x1440365921}[模式处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1322_x1237_400496277}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1322_x1237_1532175461}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1322_x1237_x1268920838}

[[network-admin]{lang="EN-US"}]{#struct_0_x1322_x1237_1699384718}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1322_x1237_355478330}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1322_x1237_x1721647392}

[[使能]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_x1322_x1237_x1526426098}[模式并重启设备之后，设备会运行于支持]{style="font-family:宋体"}[FIPS 140-2]{lang="EN-US"}[标准的工作模式下。在该工作模式下，系统将具有更为严格的安全性要求，并会对密码模块进行相应的自检处理，以确认其处于正常运行状态。]{style="font-family:宋体"}

[[用户执行了]{style="font-family:宋体"}**[fips mode enable]{lang="EN-US"}**]{#struct_0_x1322_x1237_2143848879}[命令后，系统提供以下两种启动方式来进入]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[自动重启方式]{style="font-family:宋体"}]{#struct_0_x1322_x1237_x1449272532}

[[该方式下，系统自动创建一个]{style="font-family:宋体"}]{#struct_0_x1322_x1237_x645159824}[FIPS]{lang="EN-US"}[缺省配置文件（]{style="font-family:宋体"}[[名称为]{style="font-family:宋体"}]{.MsoCommentReference}[fips-startup.cfg]{lang="EN-US"}[），同时将其指定为下次启动配置文件，并且要求用户手工配置设备重启后登录设备的用户名和密码。如果用户在输入过程中想退出配置流程，]{style="font-family:宋体"}[可以使用]{style="font-family:宋体"}[\<Ctrl+C\>]{lang="EN-US"}[组合键中断配置流程]{style="font-family:宋体"}[，配置流程中断后，当前的]{style="font-family:宋体"}**[fips mode enable]{lang="EN-US"}**[命令设置也相应失败。]{style="font-family:宋体"}

[[用户成功设置安全管理员用户名和登录密码之后，系统将自动使用指定的启动配置文件重启。]{style="font-family:宋体"}]{#struct_0_x1322_x1237_1343892031}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[手动重启方式]{style="font-family:宋体"}]{#struct_0_x1322_x1237_x1595254375}

[[该方式下，系统不自动创建进入]{style="font-family:宋体"}]{#struct_0_x1322_x1237_687176780}[FIPS]{lang="EN-US"}[模式的下次启动配置文件。需要用户手工完成进入]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式所需的所有必要配置，主要包括：]{style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[使能全局]{lang="EN-US" style="font-family:宋体"}[Password Control]{lang="EN-US"}]{#struct_0_x1322_x1237_411327874}[功能。]{lang="EN-US" style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[设置全局]{lang="EN-US" style="font-family:宋体"}[Password Control]{lang="EN-US"}]{#struct_0_x1322_x1237_x9202368}[密码组合类型的个数为]{lang="EN-US" style="font-family:宋体"}[4]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[每种类型至少]{style="font-family:宋体"}[1]{lang="EN-US"}[个字符]{style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[设置全局]{lang="EN-US" style="font-family:宋体"}[Password Control]{lang="EN-US"}]{#struct_0_x1322_x1237_2143914415}[的密码最小长度为]{lang="EN-US" style="font-family:宋体"}[15]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[添加设备管理类本地用户，设置密码、用户角色和服务类型。本地用户的密码需要符合以上]{style="font-family:宋体"}]{#struct_0_x1322_x1237_x1835179105}[Password Control]{lang="EN-US"}[配置的限制，用户角色必须是]{style="font-family:宋体"}[network-admin]{lang="EN-US"}[或者]{style="font-family:宋体"}[mdc-admin]{lang="EN-US"}[，服务类型为]{style="font-family:宋体"}[terminal]{lang="EN-US"}[。]{style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[删除不符合]{style="font-family:宋体"}]{#struct_0_x1322_x1237_x107101707}[FIPS]{lang="EN-US"}[标准的本地用户服务类型（]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[、]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[和]{style="font-family:宋体"}[FTP]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[然后手工保存当前配置文件为下次启动配置文件，并将二进制类型的下次启动配置文件删除后重启设备。]{style="font-family:宋体"}]{#struct_0_x1322_x1237_75523450}

[[执行]{style="font-family:宋体"}**[fips mode enable]{lang="EN-US"}**]{#struct_0_x1322_x1237_x715076218}[命令之后，系统会提示用户选择启动方式，若用户未在]{style="font-family:宋体"}[30]{lang="EN-US"}[秒内作出选择，则系统默认用户采用了手动启动方式。]{style="font-family:宋体"}

[[用户执行了]{style="font-family:宋体"}**[undo fips mode enable]{lang="EN-US"}**]{#struct_0_x1322_x1237_x1327514897}[命令后，系统提供以下两种启动选择来退出]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[自动重启方式：系统自动创建一个非]{style="font-family:宋体"}]{#struct_0_x1322_x1237_809804951}[FIPS]{lang="EN-US"}[缺省配置文件（]{style="font-family:宋体"}[[名称为]{style="font-family:宋体"}]{.MsoCommentReference}[[non-fips-startup.cfg]{lang="EN-US"}]{.FigureChar}[），同时将其指定为下次启动配置文件，之后自动使用非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[缺省配置文件重启。重启之后，当前登录用户不需要输入任何信息即可直接登录到非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式的系统。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[手动重启方式：系统不自动创建进入非]{style="font-family:宋体"}]{#struct_0_x1322_x1237_2143979951}[FIPS]{lang="EN-US"}[模式的下次启动配置文件，需要用户手工完成进入非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式所需的所有必要配置之后，手工重启设备。重启之后，当前登录用户需要根据配置的登录认证方式输入相应的用户信息登录到非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式的系统。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1322_x1237_x1061728390}

[[\# ]{lang="EN-US"}]{#struct_0_x1322_x1237_136577716}[使能]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式，并选择自动重启方式进入]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1322_x1237_x842693714}

[\[Sysname\] fips mode enable]{lang="EN-US"}

[FIPS mode change requires a device reboot. Continue? \[Y/N\]:y]{lang="EN-US"}

[Reboot the device automatically? \[Y/N\]:y]{lang="EN-US"}

[The system will create a new startup configuration file for FIPS mode. After you set the login username and password for FIPS mode, the device will reboot automatically.]{lang="EN-US"}

[Enter username(1-55 characters): root]{lang="EN-US"}

[Enter password(15-63 characters):]{lang="EN-US"}

[Confirm password:]{lang="EN-US"}

[Waiting for reboot\... After reboot, the device will enter FIPS mode.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1322_x1237_x1096049420}[使能]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式，并选择手动重启方式进入]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1322_x1237_2142996911}

[\[Sysname\] fips mode enable]{lang="EN-US"}

[FIPS mode change requires a device reboot. Continue? \[Y/N\]:y]{lang="EN-US"}

[Reboot the device automatically? \[Y/N\]:n]{lang="EN-US"}

[Change the configuration to meet FIPS mode requirements, save the configuration to the next-startup configuration file, and then reboot to enter FIPS mode.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1322_x1237_540047977}[关闭]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式，并选择自动重启方式进入非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\[Sysname\] undo fips mode enable]{lang="EN-US"}]{#struct_0_x1322_x1237_x845796126}

[FIPS mode change requires a device reboot. Continue? \[Y/N\]:y]{lang="EN-US"}

[The system will create a new startup configuration file for non-FIPS mode and then reboot automatically. Continue? \[Y/N\]:y]{lang="EN-US"}

[Waiting for reboot\... After reboot, the device will enter non-FIPS mode.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1322_x1237_x803645999}[关闭]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式，并选择手动重启方式进入非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\[Sysname\] undo fips mode enable]{lang="EN-US"}]{#struct_0_x1322_x1237_x2113849166}

[FIPS mode change requires a device reboot. Continue? \[Y/N\]:y]{lang="EN-US"}

[The system will create a new startup configuration file for non-FIPS mode, and then reboot automatically. Continue? \[Y/N\]:n]{lang="EN-US"}

[Change the configuration to meet non-FIPS mode requirements, save the configuration to the next-startup configuration file, and then reboot to enter non-FIPS mode.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1322_x1237_1655812080}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display fips status]{lang="EN-US"}**]{#struct_0_x1322_x1237_x79611174}
:::

::: {#-917766234 .myid}
[]{#_Toc404794032}[]{#struct_0_x1322_x1237_2143062447}[]{#_Toc343590063}[]{#_Toc343590012}[]{#_Toc345082775}[]{#_Toc345082776}[]{#_Toc345082777}

**FIPS \-- FIPS配置命令 \-- fips self-test**

------------------------------------------------------------------------

[**[fips self-test]{lang="EN-US"}**]{#struct_0_x1322_x1237_x670085597}[命令用来手工触发密码算法自检。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1322_x1237_630218596}

[**[fips self-test]{lang="EN-US"}**]{#struct_0_x1322_x1237_918179085}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1322_x1237_1031050526}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1322_x1237_x1853418211}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1322_x1237_951320087}

[[network-admin]{lang="EN-US"}]{#struct_0_x1322_x1237_x217439503}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1322_x1237_1024590554}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1322_x1237_x585362153}

[[当管理员需要确认当前处于]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_x1322_x1237_x655205523}[模式的系统中的密码算法模块是否正常工作时，可以执行本命令触发密码算法自检。手工触发的密码算法自检内容与设备启动时自动进行的启动自检内容相同。]{style="font-family:宋体"}

[[只有所有密码算法自检都通过了，整个密码算法自检才算成功。密码算法自检失败后，设备会自动重启。]{style="font-family:宋体"}]{#struct_0_x1322_x1237_x1248220451}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1322_x1237_673728804}

[[\# ]{lang="EN-US"}]{#struct_0_x1322_x1237_1795922991}[手工触发密码算法自检。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1322_x1237_x585296617}

[\[Sysname\] fips self-test]{lang="EN-US"}

[FIPS Known-Answer Tests are running \...]{lang="EN-US"}

[ ]{lang="EN-US"}

[CPU 1 of slot 1 in chassis 1:]{lang="EN-US"}

[Starting Known-Answer tests in the user space.]{lang="EN-US"}

[Known-answer test for SHA1 passed.]{lang="EN-US"}

[Known-answer test for SHA224 passed.]{lang="EN-US"}

[Known-answer test for SHA256 passed.]{lang="EN-US"}

[Known-answer test for SHA384 passed.]{lang="EN-US"}

[Known-answer test for SHA512 passed.]{lang="EN-US"}

[Known-answer test for HMAC-SHA1 passed.]{lang="EN-US"}

[Known-answer test for HMAC-SHA224 passed.]{lang="EN-US"}

[Known-answer test for HMAC-SHA256 passed.]{lang="EN-US"}

[Known-answer test for HMAC-SHA384 passed.]{lang="EN-US"}

[Known-answer test for HMAC-SHA512 passed.]{lang="EN-US"}

[Known-answer test for AES passed.]{lang="EN-US"}

[Known-answer test for RSA(signature/verification) passed.]{lang="EN-US"}

[Known-answer test for RSA(encrypt/decrypt) passed.]{lang="EN-US"}

[Known-answer test for DSA(signature/verification) passed.]{lang="EN-US"}

[Known-answer test for random number generator passed.]{lang="EN-US"}

[Known-Answer tests in the user space passed.]{lang="EN-US"}

[Starting Known-Answer tests in the kernel.]{lang="EN-US"}

[Known-answer test for SHA1 passed.]{lang="EN-US"}

[Known-answer test for HMAC-SHA1 passed.]{lang="EN-US"}

[Known-answer test for AES passed.]{lang="EN-US"}

[Known-answer test for random number generator passed.]{lang="EN-US"}

[Known-Answer tests in the kernel passed.]{lang="EN-US"}

[CPU 1 of slot 2 in chassis 1:]{lang="EN-US"}

[Starting Known-Answer tests in the user space.]{lang="EN-US"}

[Known-answer test for SHA1 passed.]{lang="EN-US"}

[Known-answer test for SHA224 passed.]{lang="EN-US"}

[Known-answer test for SHA256 passed.]{lang="EN-US"}

[Known-answer test for SHA384 passed.]{lang="EN-US"}

[Known-answer test for SHA512 passed.]{lang="EN-US"}

[Known-answer test for HMAC-SHA1 passed.]{lang="EN-US"}

[Known-answer test for HMAC-SHA224 passed.]{lang="EN-US"}

[Known-answer test for HMAC-SHA256 passed.]{lang="EN-US"}

[Known-answer test for HMAC-SHA384 passed.]{lang="EN-US"}

[Known-answer test for HMAC-SHA512 passed.]{lang="EN-US"}

[Known-answer test for AES passed.]{lang="EN-US"}

[Known-answer test for RSA(signature/verification) passed.]{lang="EN-US"}

[Known-answer test for RSA(encrypt/decrypt) passed.]{lang="EN-US"}

[Known-answer test for DSA(signature/verification) passed.]{lang="EN-US"}

[Known-answer test for random number generator passed.]{lang="EN-US"}

[Known-Answer tests in the user-space passed.]{lang="EN-US"}

[Starting Known-Answer tests in the kernel.]{lang="EN-US"}

[Known-answer test for SHA1 passed.]{lang="EN-US"}

[Known-answer test for HMAC-SHA1 passed.]{lang="EN-US"}

[Known-answer test for AES passed.]{lang="EN-US"}

[Known-answer test for SHA1 passed.]{lang="EN-US"}

[Known-Answer tests in the kernel passed.]{lang="EN-US"}

[CPU 1 of slot 0 in chassis 2:]{lang="EN-US"}

[Starting Known-Answer tests in the user space.]{lang="EN-US"}

[Known-answer test for SHA1 passed.]{lang="EN-US"}

[Known-answer test for SHA224 passed.]{lang="EN-US"}

[Known-answer test for SHA256 passed.]{lang="EN-US"}

[Known-answer test for SHA384 passed.]{lang="EN-US"}

[Known-answer test for SHA512 passed.]{lang="EN-US"}

[Known-answer test for HMAC-SHA1 passed.]{lang="EN-US"}

[Known-answer test for HMAC-SHA224 passed.]{lang="EN-US"}

[Known-answer test for HMAC-SHA256 passed.]{lang="EN-US"}

[Known-answer test for HMAC-SHA384 passed.]{lang="EN-US"}

[Known-answer test for HMAC-SHA512 passed.]{lang="EN-US"}

[Known-answer test for AES passed.]{lang="EN-US"}

[Known-answer test for RSA(signature/verification) passed.]{lang="EN-US"}

[Known-answer test for RSA(encrypt/decrypt) passed.]{lang="EN-US"}

[Known-answer test for DSA(signature/verification) passed.]{lang="EN-US"}

[Known-answer test for random number generator passed.]{lang="EN-US"}

[Known-Answer tests in the user-space passed.]{lang="EN-US"}

[Starting Known-Answer tests in the kernel.]{lang="EN-US"}

[Known-answer test for SHA1 passed.]{lang="EN-US"}

[Known-answer test for HMAC-SHA1 passed.]{lang="EN-US"}

[Known-answer test for AES passed.]{lang="EN-US"}

[Known-answer test for SHA1 passed.]{lang="EN-US"}

[Known-answer test for HMAC-SHA1 crypto engine passed.]{lang="EN-US"}

[Known-answer test for AES crypto engine passed.]{lang="EN-US"}

[Known-answer test for random number generator crypto engine passed.]{lang="EN-US"}

[Known-answer test for RSA(signature/verification) crypto engine passed.]{lang="EN-US"}

[Known-answer test for RSA(encrypt/decrypt) crypto engine passed.]{lang="EN-US"}

[Known-answer test for DSA(signature/verification) crypto engine passed.]{lang="EN-US"}

[Known-Answer tests in the kernel passed.]{lang="EN-US"}

[CPU 1 of slot 1 in chassis 2:]{lang="EN-US"}

[Starting Known-Answer tests in the user space.]{lang="EN-US"}

[Known-answer test for SHA1 passed.]{lang="EN-US"}

[Known-answer test for SHA224 passed.]{lang="EN-US"}

[Known-answer test for SHA256 passed.]{lang="EN-US"}

[Known-answer test for SHA384 passed.]{lang="EN-US"}

[Known-answer test for SHA512 passed.]{lang="EN-US"}

[Known-answer test for HMAC-SHA1 passed.]{lang="EN-US"}

[Known-answer test for HMAC-SHA224 passed.]{lang="EN-US"}

[Known-answer test for HMAC-SHA256 passed.]{lang="EN-US"}

[Known-answer test for HMAC-SHA384 passed.]{lang="EN-US"}

[Known-answer test for HMAC-SHA512 passed.]{lang="EN-US"}

[Known-answer test for AES passed.]{lang="EN-US"}

[Known-answer test for RSA(signature/verification) passed.]{lang="EN-US"}

[Known-answer test for RSA(encrypt/decrypt) passed.]{lang="EN-US"}

[Known-answer test for DSA(signature/verification) passed.]{lang="EN-US"}

[Known-answer test for random number generator passed.]{lang="EN-US"}

[Known-Answer tests in the user-space passed.]{lang="EN-US"}

[Starting Known-Answer tests in the kernel.]{lang="EN-US"}

[Known-answer test for SHA1 passed.]{lang="EN-US"}

[Known-answer test for HMAC-SHA1 passed.]{lang="EN-US"}

[Known-answer test for AES passed.]{lang="EN-US"}

[Known-answer test for SHA1 passed.]{lang="EN-US"}

[Known-Answer tests in the kernel passed.]{lang="EN-US"}

[FIPS Known-Answer Tests passed.]{lang="EN-US"}
:::
