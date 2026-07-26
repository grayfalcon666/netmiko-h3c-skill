
**AAA \-- ISP域中实现AAA配置命令 \-- aaa nas-id profile**

------------------------------------------------------------------------

**[aaa nas-id profile**]命令用来创建NAS-ID Profile，并进入NAS-ID-Profile视图。

**[undo aaa nas-id profile**]命令用来删除指定的NAS-ID Profile。

【命令】

**[aaa nas-id profile***profile-name*]

**[undo aaa nas-id profile***profile-name*]

【缺省情况】

不存在NAS-ID Profile。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[profile-name*]：Profile名称，为1～31个字符的字符串，不区分大小写。该Profile用于保存NAS-ID与VLAN的绑定关系。

【使用指导】

在某些应用环境中，网络运营商需要使用接入设备发送给RADIUS服务器的NAS-Identifier属性值来获知用户的接入位置，而用户的接入VLAN可标识用户的接入位置，因此接入设备上可通过建立用户接入VLAN与指定的NAS-ID之间的绑定关系来实现接入位置信息的映射。NAS-ID Profile用于保存NAS-ID和VLAN的绑定关系。这样，当用户上线时，设备会将与用户接入VLAN匹配的NAS-ID填充在RADIUS请求报文中的NAS-Identifier属性中发送给RADIUS服务器。

【举例】

\# 创建一个名字为aaa的NAS-ID Profile。

\<Sysname\> system-view

Sysname aaa nas-id profile aaa

Sysname-nas-id-prof-aaa

【相关命令】

·**portal nas-id-profile**（安全命令参考/Portal）

·**port-security nas-id-profile**（安全命令参考/端口安全）

·**nas-id bind vlan**

**AAA \-- ISP域中实现AAA配置命令 \-- aaa session-limit**

------------------------------------------------------------------------

**[aaa session-limit**]命令用来配置同时在线的最大用户连接数，即采用指定登录方式登录设备并同时在线的用户数。

**[undo aaa session-limit**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[aaa session-limit **[{ **ftp** \| **http** \| **https** \| **ssh** \| **telnet** } *max-sessions*]]

**[undo aaa session-limit **[{ **ftp** \| **http** \| **https** \| **ssh** \| **telnet** }]]

FIPS模式下：

**[aaa session-limit **[{ **https** \| **ssh** } *max-sessions*]]

**[undo aaa session-limit **[{ **https** \| **ssh** }]]

【缺省情况】

缺省的最大用户连接数为32。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ftp**]：表示FTP用户。

**[http**]：表示HTTP用户。

**[https**]：表示HTTPS用户。

**[ssh**]：表示SSH用户。

**[telnet**]：表示Telnet用户。

*[max-sessions*]：允许同时在线的最大用户连接数，取值范围以各产品实际情况为准。

【使用指导】

配置本命令后，当指定类型的接入用户的用户数超过当前配置的最大连接数后，新的接入请求将被拒绝。

【举例】

\# 设置同时在线的最大FTP用户连接数为4。

\<Sysname\> system-view

Sysname aaa session-limit ftp 4

**AAA \-- ISP域中实现AAA配置命令 \-- accounting advpn**

------------------------------------------------------------------------

![说明](AAA命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[accounting advpn**]命令用来为ADVPN用户配置计费方法。

**[undo accounting advpn**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[accounting advpn** { **local** [ **none**  \| **none** \| **radius-scheme** *radius-scheme-name*  **local**   **none**  }]]

**[undo accounting advpn**]

FIPS模式下：

**[accounting advpn**[ { **local** \| **radius-scheme** *radius-scheme-name* [ **local** ] }]]

**[undo accounting advpn**]

【缺省情况】

ADVPN用户采用当前ISP域的缺省计费方法。

【视图】

ISP域视图

【支持的缺省用户角色】

network-admin

mdc-admin

【参数】

**[local**]：本地计费。

**[none**]：不计费。

**[radius-scheme*** radius-scheme-name*]：指定RADIUS方案。其中，*radius-scheme-name*表示RADIUS方案名，为1～32个字符的字符串，不区分大小写。

【使用指导】

可以指定一个或多个备选的计费方法，在当前的计费方法无效时按照配置顺序尝试使用备选的方法完成计费。例如，**radius-scheme** *radius-scheme-name* **local** **none**表示，先进行RADIUS计费，若RADIUS计费无效则进行本地计费，若本地计费也无效则不进行计费。

【举例】

\# 在ISP域test下，为ADVPN用户配置计费方法为**local**。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test accounting advpn local

\# 在ISP域test下，配置ADVPN用户使用RADIUS方案rd进行计费，并且使用**local**作为备选计费方法。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test accounting advpn radius-scheme rd local

【相关命令】

·**accounting default**

·**local-user**

·**radius scheme**

**AAA \-- ISP域中实现AAA配置命令 \-- accounting command**

------------------------------------------------------------------------

**[accounting command**]命令用来配置命令行计费方法。

**[undo accounting command**]命令用来恢复缺省情况。

【命令】

**[accounting command hwtacacs-scheme** *hwtacacs-scheme-name*]

**[undo accounting command**]

【缺省情况】

命令行计费采用当前ISP域的缺省计费方法。

【视图】

ISP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[hwtacacs-scheme*** hwtacacs-scheme-name*]：指定HWTACACS方案。其中，*hwtacacs-scheme-name*表示HWTACACS方案名，为1～32个字符的字符串，不区分大小写。

【使用指导】

命令行计费是指，用户执行过的所有命令或被成功授权执行的命令，会被计费服务器进行记录。

目前，仅支持使用远程HWTACACS服务器完成命令行计费功能。

【举例】

\# 在ISP域test下，配置使用HWTACACS计费方案hwtac进行命令行计费。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test accounting command hwtacacs-scheme hwtac

【相关命令】

·**accounting default**

·**command accounting**（基础命令参考/登录设备）

·**hwtacacs scheme**

**AAA \-- ISP域中实现AAA配置命令 \-- accounting default**

------------------------------------------------------------------------

**[accounting default**]命令用来为当前ISP域配置缺省的计费方法。

**[undo accounting default**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[accounting default** { **hwtacacs-scheme** *hwtacacs-scheme-name* [ **radius-scheme** *radius-scheme-name*   **local**   **none**  \| **local**  **none**  \| **none** \| **radius-scheme** *radius-scheme-name*  **hwtacacs-scheme** *hwtacacs-scheme-name*   **local**   **none**  }]]

**[undo accounting default**]

FIPS模式下：

**[accounting default** { **hwtacacs-scheme** *hwtacacs-scheme-name* [ **radius-scheme** *radius-scheme-name*   **local**  \| **local** \| **radius-scheme** *radius-scheme-name*  **hwtacacs-scheme** *hwtacacs-scheme-name*   **local**  }]]

**[undo accounting default**]

【缺省情况】

当前ISP域的缺省计费方法为**local**。

【视图】

ISP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[hwtacacs-scheme*** hwtacacs-scheme-name*]：指定HWTACACS方案。其中，*hwtacacs-scheme-name*表示HWTACACS方案名，为1～32个字符的字符串，不区分大小写。

**[local**]：本地计费。

**[none**]：不计费。

**[radius-scheme*** radius-scheme-name*]：指定RADIUS方案。其中，*radius-scheme-name*表示RADIUS方案名，为1～32个字符的字符串，不区分大小写。

【使用指导】

当前ISP域的缺省计费方法对于该域中未指定具体计费方法的所有接入用户都起作用，但是如果某类型的用户不支持指定的计费方法，则该计费方法对于这类用户不能生效。

本地计费只是为了支持本地用户的连接数管理，没有实际的计费相关的统计功能。

可以指定一个或多个备选的计费方法，在当前的计费方法无效时按照配置顺序尝试使用备选的方法完成计费。例如，**radius-scheme** *radius-scheme-name* **local** **none**表示，先进行RADIUS计费，若RADIUS计费无效则进行本地计费，若本地计费也无效则不进行计费。

【举例】

\# 在ISP域test下，配置缺省计费方法为使用RADIUS方案rd进行计费，并且使用**local**作为备选计费方法。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test accounting default radius-scheme rd local

【相关命令】

·**hwtacacs scheme**

·**local-user**

·**radius scheme**

**AAA \-- ISP域中实现AAA配置命令 \-- accounting ipoe**

------------------------------------------------------------------------

**[accounting ipoe**]命令用来为IPoE用户配置计费方法。

**[undo accounting ipoe**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[accounting ipoe****broadcast****radius-scheme** *radius-scheme-name1* **radius-scheme** *radius-scheme-name2* \**[local**  \**none**  \| ]**local** \**[none**  \| ]**none**[ \| ]**radius-scheme** *radius-scheme-name* \**[local**  \**none**  }]

**[undo accounting ipoe**]

FIPS]模式下：

**[accounting ipoe****broadcast****radius-scheme** *radius-scheme-name1* **radius-scheme** *radius-scheme-name2* \**[local**  \| ]**local**[ \| ]**radius-scheme** *radius-scheme-name* \**[local**  }]

**[undo accounting ipoe**]

【缺省情况】]

IPoE用户采用当前ISP域的缺省计费方法。

【视图】

ISP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[broadcast**]：指定广播RADIUS方案，即同时向指定的两个RADIUS方案中的计费服务器发送计费请求。

**[radius-scheme **]*radius-scheme-name1*：表示主送计费RADIUS方案名，为1～32个字符的字符串，不区分大小写；

**[radius-scheme**]*radius-scheme-name2*：表示抄送计费RADIUS方案名，为1～32个字符的字符串，不区分大小写。

**[local**]：本地计费。

**[none**]：不计费。

**[radius-scheme**]* radius-scheme-name*：指定RADIUS方案。其中，*radius-scheme-name*表示RADIUS方案名，为1～32个字符的字符串，不区分大小写。

【使用指导】

可以指定一个或多个备选的计费方法，在当前的计费方法无效时按照配置顺序尝试使用备选的方法完成计费。例如，**radius-scheme** *radius-scheme-name* **local****none**表示，先进行RADIUS计费，若RADIUS计费无效则进行本地计费，若本地计费也无效则不进行计费。

当指定**broadcast**关键字时，将同时向指定的两个RADIUS方案里的主计费服务器发送计费请求，若主计费服务器不可达，再依次向RADIUS方案里的从计费服务器发送计费请求。主送计费方案计费成功时，表示用户计费成功；抄送计费方案的计费结果对用户无影响。

【举例】

\# 在ISP域test下，为IPoE用户配置计费方法为**local**。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test accounting ipoe local

\# 在ISP域test下，配置IPoE用户使用RADIUS方案rd进行计费，并且使用**local**作为备选计费方法。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test accounting ipoe radius-scheme rd local

\# 在ISP域test下，配置IPoE用户使用RADIUS方案rd1和rd2进行广播计费，并且使用**local**作为备选计费方法。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test accounting ipoe broadcast radius-scheme rd1 radius-scheme rd2 local

【相关命令】

·**accounting default**

·**local-user**

·**radius scheme**

**AAA \-- ISP域中实现AAA配置命令 \-- accounting lan-access**

------------------------------------------------------------------------

![说明](AAA命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[accounting lan-access**]命令用来为lan-access用户配置计费方法。

**[undo accounting lan-access**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[accounting lan-access****broadcast radius-scheme ***radius-scheme-name1*** radius-scheme***radius-scheme-name2 * \**[ local ** \** none ** \| **local**  **none**  \| **none** \| **radius-scheme** *radius-scheme-name*  **local**   **none**  }]

**[undo accounting lan-access**]

FIPS]模式下：

**[accounting lan-access****broadcast radius-scheme ***radius-scheme-name1*** radius-scheme***radius-scheme-name2 *\**[ local ** \** none ** \|]**local **[\| **radius-scheme** *radius-scheme-name* [ **local** ] }]

**[undo accounting lan-access**]

【缺省情况】]

lan-access用户采用当前ISP域的缺省计费方法。

【视图】

ISP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[broadcast**]：指定广播RADIUS方案，即同时向指定的两个RADIUS方案中的计费服务器发送计费请求。

**[radius-scheme **]*radius-scheme-name1*：表示主送计费RADIUS方案名，为1～32个字符的字符串，不区分大小写；

**[radius-scheme**]*radius-scheme-name2*：表示抄送计费RADIUS方案名，为1～32个字符的字符串，不区分大小写。

**[local**]：本地计费。

**[none**]：不计费。

**[radius-scheme**]* radius-scheme-name*：指定RADIUS方案。其中，*radius-scheme-name*表示RADIUS方案名，为1～32个字符的字符串，不区分大小写。

【使用指导】

可以指定一个或多个备选的计费方法，在当前的计费方法无效时按照配置顺序尝试使用备选的方法完成计费。例如，**radius-scheme** *radius-scheme-name* **local** **none**表示，先进行RADIUS计费，若RADIUS计费无效则进行本地计费，若本地计费也无效则不进行计费。

当指定**broadcast**关键字时，将同时向指定的两个RADIUS方案里的主计费服务器发送计费请求，若主计费服务器不可达，再依次向RADIUS方案里的从计费服务器发送计费请求。主送计费方案计费成功时，表示用户计费成功；抄送计费方案的计费结果对用户无影响。

【举例】

\# 在ISP域test下，为lan-access用户配置计费方法为**local**。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test accounting lan-access local

\# 在ISP域test下，配置lan-access用户使用RADIUS方案rd进行计费，并且使用**local**作为备选计费方法。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test accounting lan-access radius-scheme rd local

\# 在ISP域test下，配置lan-access用户使用RADIUS方案rd1和rd2进行广播计费，并且使用**local**作为备选计费方法。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test accounting lan-access broadcast radius-scheme rd1 radius-scheme rd2 local

【相关命令】

·**accounting default**

·**local-user**

·**radius scheme**

**AAA \-- ISP域中实现AAA配置命令 \-- accounting login**

------------------------------------------------------------------------

**[accounting login**]命令用来为login用户配置计费方法。

**[undo accounting login**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[accounting login** { **hwtacacs-scheme** *hwtacacs-scheme-name* [ **radius-scheme** *radius-scheme-name*   **local**   **none**  \| **local**  **none**  \| **none** \| **radius-scheme** *radius-scheme-name*  **hwtacacs-scheme** *hwtacacs-scheme-name*   **local**   **none**  }]]

**[undo accounting login**]

FIPS模式下：

**[accounting login** { **hwtacacs-scheme** *hwtacacs-scheme-name* [ **radius-scheme** *radius-scheme-name*   **local**  \| **local** \| **radius-scheme** *radius-scheme-name*  **hwtacacs-scheme** *hwtacacs-scheme-name*   **local**  }]]

**[undo accounting login**]

【缺省情况】

login用户采用当前ISP域的缺省计费方法。

【视图】

ISP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[hwtacacs-scheme*** hwtacacs-scheme-name*]：指定HWTACACS方案。其中，*hwtacacs-scheme-name*表示HWTACACS方案名，为1～32个字符的字符串，不区分大小写。

**[local**]：本地计费。

**[none**]：不计费。

**[radius-scheme*** radius-scheme-name*]：指定RADIUS方案。其中，*radius-scheme-name*表示RADIUS方案名，为1～32个字符的字符串，不区分大小写。

【使用指导】

不支持对FTP类型的login用户进行计费。

可以指定一个或多个备选的计费方法，在当前的计费方法无效时按照配置顺序尝试使用备选的方法完成计费。例如，**radius-scheme** *radius-scheme-name* **local** **none**表示，先进行RADIUS计费，若RADIUS计费无效则进行本地计费，若本地计费也无效则不进行计费。

【举例】

\# 在ISP域test下，为login用户配置计费方法为**local**。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test accounting login local

\# 在ISP域test下，配置login用户使用RADIUS方案rd进行计费，并且使用**local**作为备选计费方法。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test accounting login radius-scheme rd local

【相关命令】

·**accounting default**

·**hwtacacs scheme**

·**local-user**

·**radius scheme**

**AAA \-- ISP域中实现AAA配置命令 \-- accounting portal**

------------------------------------------------------------------------

**[accounting portal**]命令用来为Portal用户配置计费方法。

**[undo accounting portal**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[accounting portal ****broadcast radius-scheme ***radius-scheme-name1*** radius-scheme***radius-scheme-name2 * \**[ local ** \** none ** \| **local**  **none**  \| **none** \| **radius-scheme** *radius-scheme-name*  **local**   **none**  }]

**[undo accounting portal**]

FIPS]模式下：

**[accounting portal ****broadcast radius-scheme ***radius-scheme-name1 ***radius-scheme***radius-scheme-name2* \**[ local ** \| **local** \| **radius-scheme** *radius-scheme-name*  **local**  }]

**[undo accounting portal**]

【缺省情况】]

Portal用户采用当前ISP域的缺省计费方法。

【视图】

ISP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[broadcast**]：指定广播RADIUS方案，即同时向指定的两个RADIUS方案中的计费服务器发送计费请求。

**[radius-scheme **]*radius-scheme-name1*：表示主送计费RADIUS方案名，为1～32个字符的字符串，不区分大小写；

**[radius-scheme**]*radius-scheme-name2*：表示抄送计费RADIUS方案名，为1～32个字符的字符串，不区分大小写。

**[local**]：本地计费。

**[none**]：不计费。

**[radius-scheme**]* radius-scheme-name*：指定RADIUS方案。其中，*radius-scheme-name*表示RADIUS方案名，为1～32个字符的字符串，不区分大小写。

【使用指导】

可以指定一个或多个备选的计费方法，在当前的计费方法无效时按照配置顺序尝试使用备选的方法完成计费。例如，**radius-scheme** *radius-scheme-name* **local** **none**表示，先进行RADIUS计费，若RADIUS计费无效则进行本地计费，若本地计费也无效则不进行计费。

当指定**broadcast**关键字时，将同时向指定的两个RADIUS方案里的主计费服务器发送计费请求，若主计费服务器不可达，再依次向RADIUS方案里的从计费服务器发送计费请求。主送计费方案计费成功时，表示用户计费成功；抄送计费方案的计费结果对用户无影响。

【举例】

\# 在ISP域test下，为Portal用户配置计费方法为**local**。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test accounting portal local

\# 在ISP域test下，配置Portal用户使用RADIUS方案rd进行计费，并且使用**local**作为备选计费方法。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test accounting portal radius-scheme rd local

\# 在ISP域test下，配置portal用户使用RADIUS方案rd1和rd2进行广播计费，并且使用**local**作为备选计费方法。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test accounting portal broadcast radius-scheme rd1 radius-scheme rd2 local

【相关命令】

·**accounting default**

·**local-user**

·**radius scheme**

**AAA \-- ISP域中实现AAA配置命令 \-- accounting ppp**

------------------------------------------------------------------------

![说明](AAA命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[accounting ppp**]命令用来为PPP用户配置计费方法。

**[undo accounting ppp**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[accounting ppp****broadcast radius-scheme ***radius-scheme-name1*** radius-scheme***radius-scheme-name2 *\**[hwtacacs-scheme***hwtacacs-scheme-name*  \** local ** \** none ** \| **hwtacacs-scheme** *hwtacacs-scheme-name*  **radius-scheme** *radius-scheme-name*   **local**   **none**  \| **local**  **none**  \| **none** \| **radius-scheme** *radius-scheme-name*  **hwtacacs-scheme** *hwtacacs-scheme-name*   **local**   **none**  }]

**[undo accounting ppp**]

FIPS]模式下：

**[accounting ppp****broadcast radius-scheme ***radius-scheme-name1*** radius-scheme***radius-scheme-name2 *\**[hwtacacs-scheme***hwtacacs-scheme-name*  \** local ** \** none ** \| **hwtacacs-scheme** *hwtacacs-scheme-name*  **radius-scheme** *radius-scheme-name*   **local**  \| **local** \| **radius-scheme** *radius-scheme-name*  **hwtacacs-scheme** *hwtacacs-scheme-name*   **local**  }]

**[undo accounting ppp**]

【缺省情况】]

PPP用户采用当前ISP域的缺省计费方法。

【视图】

ISP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[broadcast**]：指定广播RADIUS方案，即同时向指定的两个RADIUS方案中的计费服务器发送计费请求。

**[radius-scheme **]*radius-scheme-name1*：表示主送计费RADIUS方案名，为1～32个字符的字符串，不区分大小写；

**[radius-scheme**]*radius-scheme-name2*：表示抄送计费RADIUS方案名，为1～32个字符的字符串，不区分大小写。

**[hwtacacs-scheme ***hwtacacs-scheme-name*]：指定HWTACACS方案。其中*hwtacacs-scheme-name*表示HWTACACS方案名，为1～32个字符的字符串，不区分大小写。

**[local**]：本地计费。

**[none**]：不计费。

**[radius-scheme*** radius-scheme-name*]：指定RADIUS方案。其中，*radius-scheme-name*表示RADIUS方案名，为1～32个字符的字符串，不区分大小写。

【使用指导】

可以指定一个或多个备选的计费方法，在当前的计费方法无效时按照配置顺序尝试使用备选的方法完成计费。例如，**radius-scheme** *radius-scheme-name* **local** **none**表示，先进行RADIUS计费，若RADIUS计费无效则进行本地计费，若本地计费也无效则不进行计费。

当指定**broadcast**关键字时，将同时向指定的两个RADIUS方案里的主计费服务器发送计费请求，若主计费服务器不可达，再依次向RADIUS方案里的从计费服务器发送计费请求。主送计费方案计费成功时，表示用户计费成功；抄送计费方案的计费结果对用户无影响。

【举例】

\# 在ISP域test下，为PPP用户配置计费方法为**local**。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test accounting ppp local

\# 在ISP域test下，配置PPP用户使用RADIUS方案rd进行计费，并且使用**local**作为备选计费方法。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test accounting ppp radius-scheme rd local

\# 在ISP域test下，配置ppp用户使用RADIUS方案rd1和rd2进行广播计费，并且使用**local**作为备选计费方法。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test accounting ppp broadcast radius-scheme rd1 radius-scheme rd2 local

【相关命令】

·**accounting default**

·**hwtacacs scheme**

·**local-user**

·**radius scheme**

**AAA \-- ISP域中实现AAA配置命令 \-- accounting quota-out**

------------------------------------------------------------------------

![说明](AAA命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[accounting quota-out**]命令用来配置用户计费流量配额耗尽策略。

**[undo accounting quota-out**]命令用来恢复缺省情况。

【命令】

**[accounting quota-out **[{ **offline** \| **online** }]]

**[undo accounting quota-out**]

【缺省情况】

用户的计费流量配额耗尽后将被强制下线。

【视图】

ISP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[offline**]：当用户的整体流量配额耗尽后，强制用户下线。

**[online**]：当用户的整体流量配额耗尽后，允许用户保持在线状态。

【举例】

\# 在ISP域test下，配置用户计费流量配额耗尽策略为：当流量配额耗尽后用户仍能保持在线状态。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-domain-test accounting quota-out online

**AAA \-- ISP域中实现AAA配置命令 \-- accounting sslvpn**

------------------------------------------------------------------------

**[accounting sslvpn**]命令用来为SSL VPN用户配置计费方法。

**[undo accounting sslvpn**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[accounting sslvpn** { **local** [ **none**  \| **none** \| **radius-scheme** *radius-scheme-name*  **local**   **none**  }]]

**[undo accounting sslvpn**]

FIPS模式下：

**[accounting sslvpn**[ { **local** \| **radius-scheme** *radius-scheme-name* [ **local** ] }]]

**[undo accounting sslvpn**]

【缺省情况】

SSL VPN用户采用当前ISP域的缺省计费方法。

【视图】

ISP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[local**]：本地计费。

**[none**]：不计费。

**[radius-scheme ***radius-scheme-name*]：指定RADIUS方案。其中，radius-scheme-name表示RADIUS方案名，为1～32个字符的字符串，不区分大小写。

【使用指导】

可以指定一个或多个备选的计费方法，在当前的计费方法无效时按照配置顺序尝试使用备选的方法完成计费。例如，**radius-scheme** *radius-scheme-name* **local** **none**表示，先进行RADIUS计费，若RADIUS计费无效则进行本地计费，若本地计费也无效则不进行计费。

【举例】

\# 在ISP域test下，为SSL VPN用户配置计费方法为**local**。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test accounting sslvpn local

\# 在ISP域test下，配置SSL VPN用户使用RADIUS方案rd进行计费，并且使用**local**作为备选计费方法。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test accounting sslvpn radius-scheme rd local

【相关命令】

·**accounting default**

·**local-user**

·**radius scheme**

**AAA \-- ISP域中实现AAA配置命令 \-- accounting start-fail**

------------------------------------------------------------------------

![说明](AAA命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[accounting start-fail**]命令用来配置用户计费开始失败策略，即设备向计费服务器发送计费开始请求失败后，是否允许用户接入网络。

**[undo accounting start-fail**]命令用来恢复默认情况。

【命令】

**[accounting start-fail **[{ **offline** \| **online** }]]

**[undo accounting start-fail**]

【缺省情况】

如果用户计费开始失败，允许用户保持在线状态。

【视图】

ISP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[offline**]：强制用户下线。

**[online**]：允许用户保持在线状态。

【举例】

\# 在ISP域test下，配置计费开始失败策略为：用户计费开始失败时允许用户保持在线状态。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-domain-test accounting start-fail online

**AAA \-- ISP域中实现AAA配置命令 \-- accounting update-fail**

------------------------------------------------------------------------

![说明](AAA命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[accounting update-fail**]命令用来配置用户计费更新失败策略，即设备向计费服务器发送用户的计费更新报文失败时，是否允许用户接入网络。

**[undo accounting update-fail**]命令用来恢复缺省情况。

【命令】

**[accounting update-fail** { [ **max-times** *times*  **offline** \| **online** }]]

**[undo accounting update-fail**]

【缺省情况】

如果用户计费更新失败，允许用户保持在线状态。

【视图】

ISP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[max-times ***times*]：允许用户连续计费更新失败的次数，取值范围1～255，缺省值为1。

**[offline**]：如果用户连续计费更新失败的次数达到了指定的次数，则强制用户下线。

**[online**]：如果用户计费更新失败，允许用户保持在线状态。

【举例】

\# 在ISP域test下，配置计费开始失败策略为：用户计费更新失败时允许用户保持在线状态。

\<Sysname\> system-view

Sysname domain isp1

Sysname-isp-domain-isp1 accounting update-fail online

**AAA \-- ISP域中实现AAA配置命令 \-- authentication advpn**

------------------------------------------------------------------------

![说明](AAA命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[authentication advpn**]命令用来为ADVPN用户配置认证方法。

**[undo authentication advpn**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[authentication advpn** { **local** [ **none**  \| **none** \| **radius-scheme** *radius-scheme-name*  **local**   **none**  }]]

**[undo authentication advpn**]

FIPS模式下：

**[authentication advpn**[ { **local** \| **radius-scheme** *radius-scheme-name* [ **local** ] }]]

**[undo authentication advpn**]

【缺省情况】

ADVPN用户采用当前ISP域的缺省认证方法。

【视图】

ISP域视图

【支持的缺省用户角色】

network-admin

mdc-admin

【参数】

**[local**]：本地计费。

**[none**]：不计费。

**[radius-scheme*** radius-scheme-name*]：指定RADIUS方案。其中，*radius-scheme-name*表示RADIUS方案名，为1～32个字符的字符串，不区分大小写。

【使用指导】

可以指定一个或多个备选的认证方法，在当前的认证方法无效时按照配置顺序尝试使用备选的方法完成认证。例如，**radius-scheme** *radius-scheme-name* **local** **none**表示，先进行RADIUS认证，若RADIUS认证无效则进行本地认证，若本地认证也无效则不进行认证。

【举例】

\# 在ISP域test下，为ADVPN用户配置认证方法为**local**。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test authentication advpn local

\# 在ISP域test下，配置ADVPN用户使用RADIUS方案rd进行认证，并且使用**local**作为备选认证方法。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test authentication advpn radius-scheme rd local

【相关命令】

·**authentication default**

·**local-user**

·**radius scheme**

**AAA \-- ISP域中实现AAA配置命令 \-- authentication default**

------------------------------------------------------------------------

**[authentication default**]命令用来为当前ISP域配置缺省的认证方法。

**[undo authentication default**]命令用来为恢复缺省情况。

【命令】

非FIPS模式下：

**[authentication default** { **hwtacacs-scheme** *hwtacacs-scheme-name* [ **radius-scheme** *radius-scheme-name*   **local**   **none**  \| **ldap-scheme** *ldap-scheme-name*  **local**   **none**  \| **local**  **none**  \| **none** \| **radius-scheme** *radius-scheme-name*  **hwtacacs-scheme** *hwtacacs-scheme-name*   **local**   **none**  }]]

**[undo authentication default**]

FIPS模式下：

**[authentication default** { **hwtacacs-scheme** *hwtacacs-scheme-name* [ **radius-scheme** *radius-scheme-name*   **local**  \| **ldap-scheme** *ldap-scheme-name*  **local**  \| **local** \| **radius-scheme** *radius-scheme-name*  **hwtacacs-scheme** *hwtacacs-scheme-name*   **local**  }]]

**[undo authentication default**]

【缺省情况】

当前ISP域的缺省认证方法为**local**。

【视图】

ISP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[hwtacacs-scheme*** hwtacacs-scheme-name*]：指定HWTACACS方案。其中，*hwtacacs-scheme-name*表示HWTACACS方案名，为1～32个字符的字符串，不区分大小写。

**[ldap-scheme** *ldap-scheme-name*]：指定LDAP方案。其中*ldap-scheme-name*表示LDAP方案名，为1～32个字符的字符串，不区分大小写。

**[local**]：本地认证。

**[none**]：不进行认证。

**[radius-scheme**]* radius-scheme-name*：指定RADIUS方案。其中，*radius-scheme-name*表示RADIUS方案名，为1～32个字符的字符串，不区分大小写。

【使用指导】

当前ISP域的缺省的认证方法对于该域中未指定具体认证方法的所有接入用户都起作用，但是如果某类型的用户不支持指定的认证方法，则该认证方法对于这类用户不能生效。

可以指定一个或多个备选的认证方法，在当前的认证方法无效时按照配置顺序尝试使用备选的方法完成认证。例如，**radius-scheme** *radius-scheme-name* **local** **none**表示，先进行RADIUS认证，若RADIUS认证无效则进行本地认证，若本地认证也无效则不进行认证。

【举例】

\# 在ISP域test下，配置缺省认证方法为使用RADIUS方案rd进行认证，并且使用**local**作为备选认证方法。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test authentication default radius-scheme rd local

【相关命令】

·**hwtacacs scheme**

·**ldap scheme**

·**local-user**

·**radius scheme**

**AAA \-- ISP域中实现AAA配置命令 \-- authentication ipoe**

------------------------------------------------------------------------

**[authentication ipoe**]命令用来为IPoE用户配置认证方法。

**[undo authentication ipoe**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[authentication ipoe****local **\**[ none ** \|]** none **[\|]** radius-scheme***radius-scheme-name* \**[ local ** \** none **]****}

**[undo authentication ipoe**]

FIPS]模式下：

**[authentication ipoe****local **[\|]** radius-scheme***radius-scheme-name* \**[ local ** }]

**[undo authentication ipoe**]

【缺省情况】]

IPoE用户采用当前ISP域的缺省认证方法。

【视图】

ISP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[local**]：本地认证。

**[none**]：不认证。

**[radius-scheme**]* radius-scheme-name*：指定RADIUS方案。其中，*radius-scheme-name*表示RADIUS方案名，为1～32个字符的字符串，不区分大小写。

【使用指导】

可以指定一个或多个备选的认证方法，在当前的认证方法无效时按照配置顺序尝试使用备选的方法完成认证。例如，**radius-scheme***radius-scheme-name***local****none**表示，先进行RADIUS认证，若RADIUS认证无效则进行本地认证，若本地认证也无效则不进行认证。

【举例】

\# 在ISP域test下，为IPoE用户配置认证方法为**local**。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test authentication ipoe local

\# 在ISP域test下，配置IPoE用户使用RADIUS方案rd进行认证，并且使用**local**作为备选认证方法。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test authentication ipoe radius-scheme rd local

【相关命令】

·**authentication default**

·**local-user**

·**radius scheme**

**AAA \-- ISP域中实现AAA配置命令 \-- authentication lan-access**

------------------------------------------------------------------------

![说明](AAA命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[authentication lan-access**]命令用来为lan-access用户配置认证方法。

**[undo authentication lan-access**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[authentication lan-access****ldap-scheme ***ldap-scheme-name*****[ **local**   **none**  \| **local**  **none**  \| **none** \| **radius-scheme** *radius-scheme-name*  **local**   **none**  }]

**[undo authentication lan-access**]

FIPS]模式下：

**[authentication lan-access****ldap-scheme ***ldap-scheme-name*****[ **local**  \| **local** \| **radius-scheme** *radius-scheme-name*  **local**  }]

**[undo authentication lan-access**]

【缺省情况】]

lan-access用户采用当前ISP域的缺省认证方法。

【视图】

ISP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ldap-scheme ***ldap-scheme-name*]：指定LDAP方案。其中*ldap-scheme-name*表示LDAP方案名，为1～32个字符的字符串，不区分大小写。

**[local**]：本地认证。

**[none**]：不进行认证。

**[radius-scheme**] *radius-scheme-name*：指定RADIUS方案。其中，*radius-scheme-name*表示RADIUS方案名，为1～32个字符的字符串，不区分大小写。

【使用指导】

可以指定一个或多个备选的认证方法，在当前的认证方法无效时按照配置顺序尝试使用备选的方法完成认证。例如，**radius-scheme** *radius-scheme-name* **local** **none**表示，先进行RADIUS认证，若RADIUS认证无效则进行本地认证，若本地认证也无效则不进行认证。

【举例】

\# 在ISP域test下，为lan-access用户配置认证方法为**local**。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test authentication lan-access local

\# 在ISP域test下，配置lan-access用户使用RADIUS方案rd进行认证，并且使用**local**作为备选认证方法。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test authentication lan-access radius-scheme rd local

【相关命令】

·**authentication default**

·**hwtacacs scheme**

·**ldap scheme**

·**local-user**

·**radius scheme**

**AAA \-- ISP域中实现AAA配置命令 \-- authentication login**

------------------------------------------------------------------------

**[authentication login**]命令用来为login用户配置认证方法。

**[undo authentication login**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[authentication login** { **hwtacacs-scheme** *hwtacacs-scheme-name* [ **radius-scheme** *radius-scheme-name*   **local**   **none**  \| **ldap-scheme** *ldap-scheme-name*  **local**   **none**  \| **local**  **none**  \| **none** \| **radius-scheme** *radius-scheme-name*  **hwtacacs-scheme** *hwtacacs-scheme-name*   **local**   **none**  }]]

**[undo authentication login**]

FIPS模式下：

**[authentication login** { **hwtacacs-scheme** *hwtacacs-scheme-name* [ **radius-scheme** *radius-scheme-name*   **local**  \| **ldap-scheme** *ldap-scheme-name*  **local**  \| **local** \| **radius-scheme** *radius-scheme-name*  **hwtacacs-scheme** *hwtacacs-scheme-name*   **local**  }]]

**[undo authentication login**]

【缺省情况】

login用户采用当前ISP域的缺省认证方法。

【视图】

ISP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[hwtacacs-scheme*** hwtacacs-scheme-name*]：指定HWTACACS方案。其中，*hwtacacs-scheme-name*表示HWTACACS方案名，为1～32个字符的字符串，不区分大小写。

**[ldap-scheme** *ldap-scheme-name*]：指定LDAP方案。其中*ldap-scheme-name*表示LDAP方案名，为1～32个字符的字符串，不区分大小写。

**[local**]：本地认证。

**[none**]：不进行认证。

**[radius-scheme**] *radius-scheme-name*：指定RADIUS方案。其中，*radius-scheme-name*表示RADIUS方案名，为1～32个字符的字符串，不区分大小写。

【使用指导】

可以指定一个或多个备选的认证方法，在当前的认证方法无效时按照配置顺序尝试使用备选的方法完成认证。例如，**radius-scheme** *radius-scheme-name* **local** **none**表示，先进行RADIUS认证，若RADIUS认证无效则进行本地认证，若本地认证也无效则不进行认证。

【举例】

\# 在ISP域test下，为login用户配置认证方法为**local**。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test authentication login local

\# 在ISP域test下，配置login用户使用RADIUS方案rd进行认证，并且使用**local**作为备选认证方法。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test authentication login radius-scheme rd local

【相关命令】

·**authentication default**

·**hwtacacs scheme**

·**ldap scheme**

·**local-user**

·**radius scheme**

**AAA \-- ISP域中实现AAA配置命令 \-- authentication portal**

------------------------------------------------------------------------

**[authentication portal**]命令用来为Portal用户配置认证方法。

**[undo authentication portal**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[authentication portal **{ **ldap-scheme** *ldap-scheme-name* [ **local**   **none**  \| **local**  **none**  \| **none** \| **radius-scheme** *radius-scheme-name*  **local**   **none**  }]]

**[undo authentication portal**]

FIPS模式下：

**[authentication portal **{ **ldap-scheme** *ldap-scheme-name* [ **local**  \| **local** \| **radius-scheme** *radius-scheme-name*  **local**  }]]

**[undo authentication portal**]

【缺省情况】

Portal用户采用当前ISP域的缺省认证方法。

【视图】

ISP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ldap-scheme** *ldap-scheme-name*]：指定LDAP方案。其中*ldap-scheme-name*表示LDAP方案名，为1～32个字符的字符串，不区分大小写。

**[local**]：本地认证。

**[none**]：不进行认证。

**[radius-scheme**] *radius-scheme-name*：指定RADIUS方案。其中，*radius-scheme-name*表示RADIUS方案名，为1～32个字符的字符串，不区分大小写。

【使用指导】

可以指定一个或多个备选的认证方法，在当前的认证方法无效时按照配置顺序尝试使用备选的方法完成认证。例如，**radius-scheme** *radius-scheme-name* **local** **none**表示，先进行RADIUS认证，若RADIUS认证无效则进行本地认证，若本地认证也无效则不进行认证。

【举例】

\# 在ISP域test下，为Portal用户配置认证方法为**local**。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test authentication portal local

\# 在ISP域test下，配置Portal用户使用RADIUS方案rd进行认证，并且使用**local**作为备选认证方法。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test authentication portal radius-scheme rd local

【相关命令】

·**authentication default**

·**ldap scheme**

·**local-user**

·**radius scheme**

**AAA \-- ISP域中实现AAA配置命令 \-- authentication ppp**

------------------------------------------------------------------------

![说明](AAA命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[authentication ppp**]命令用来为PPP用户配置认证方法。

**[undo authentication ppp**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[authentication ppp****hwtacacs-scheme ***hwtacacs-scheme-name***** **radius-scheme** *radius-scheme-name* ]  **local**   **none**  [\| **local** [ **none** ] \| **none** \| **radius-scheme** *radius-scheme-name* ] **hwtacacs-scheme** *hwtacacs-scheme-name*   **local**   **none**  }

**[undo authentication ppp**]

FIPS模式下：

**[authentication ppp****hwtacacs-scheme ***hwtacacs-scheme-name***** **radius-scheme** *radius-scheme-name* ]  **local**  [\| **local** \| **radius-scheme** *radius-scheme-name* ] **hwtacacs-scheme** *hwtacacs-scheme-name*   **local**  }

**[undo authentication ppp**]

【缺省情况】

PPP用户采用当前ISP域的缺省认证方法。

【视图】

ISP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[hwtacacs-scheme ***hwtacacs-scheme-name*]：指定HWTACACS方案。其中*hwtacacs-scheme-name*表示HWTACACS方案名，为1～32个字符的字符串，不区分大小写。

**[local**]：本地认证。

**[none**]：不进行认证。

**[radius-scheme**] *radius-scheme-name*：指定RADIUS方案。其中，*radius-scheme-name*表示RADIUS方案名，为1～32个字符的字符串，不区分大小写。

【使用指导】

可以指定一个或多个备选的认证方法，在当前的认证方法无效时按照配置顺序尝试使用备选的方法完成认证。例如，**radius-scheme** *radius-scheme-name* **local** **none**表示，先进行RADIUS认证，若RADIUS认证无效则进行本地认证，若本地认证也无效则不进行认证。

【举例】

\# 在ISP域test下，为PPP用户配置认证方法为**local**。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test authentication ppp local

\# 在ISP域test下，配置PPP用户使用RADIUS方案rd进行认证，并且使用**local**作为备选认证方法。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test authentication ppp radius-scheme rd local

【相关命令】

·**authentication default**

·**hwtacacs scheme**

·**local-user**

·**radius scheme**

**AAA \-- ISP域中实现AAA配置命令 \-- authentication sslvpn**

------------------------------------------------------------------------

**[authentication sslvpn**]命令用来为SSL VPN用户配置认证方法。

**[undo authentication sslvpn**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[authentication sslvpn **{ **ldap-scheme** *ldap-scheme-name* [ **local**   **none**  \| **local**  **none**  \| **none** \| **radius-scheme** *radius-scheme-name*  **local**   **none**  }]]

**[undo authentication sslvpn**]

FIPS模式下：

**[authentication sslvpn **{ **ldap-scheme** *ldap-scheme-name* [ **local**  \| **local** \| **radius-scheme** *radius-scheme-name*  **local**  }]]

**[undo authentication sslvpn**]

【缺省情况】

SSL VPN用户采用当前ISP域的缺省认证方法。

【视图】

ISP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ldap-scheme ***ldap-scheme-name*]：指定LDAP方案。其中，*ldap-scheme-name*表示LDAP方案名，为1～32个字符的字符串，不区分大小写。

**[local**]：本地认证。

**[none**]：不进行认证。

**[radius-scheme ***radius-scheme-name*]：指定RADIUS方案。其中，radius-scheme-name表示RADIUS方案名，为1～32个字符的字符串，不区分大小写。

【使用指导】

可以指定一个或多个备选的认证方法，在当前的认证方法无效时按照配置顺序尝试使用备选的方法完成认证。例如，**radius-scheme** *radius-scheme-name* **local** **none**表示，先进行RADIUS认证，若RADIUS认证无效则进行本地认证，若本地认证也无效则不进行认证。

【举例】

\# 在ISP域test下，为SSL VPN用户配置认证方法为**local**。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test authentication sslvpn local

\# 在ISP域test下，配置SSL VPN用户使用LDAP方案ldp进行认证，并且使用**local**作为备选认证方法。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test authentication sslvpn ldap-scheme ldp local

【相关命令】

·**authentication default**

·**ldap scheme**

·**local-user**

·**radius scheme**

**AAA \-- ISP域中实现AAA配置命令 \-- authentication super**

------------------------------------------------------------------------

**[authentication super**]命令用来配置用户角色切换认证方法。

**[undo authentication super**]命令用来恢复缺省情况。

【命令】

**[authentication super**[ { **hwtacacs-scheme** *hwtacacs-scheme-name* \| **radius-scheme** *radius-scheme-name* } \*]]

**[undo authentication super **]

【缺省情况】

用户角色切换认证采用当前ISP域的缺省认证方法。

【视图】

ISP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[hwtacacs-scheme** *hwtacacs-scheme-name*]：指定HWTACACS方案。其中，*hwtacacs-scheme-name*表示HWTACACS方案名，为1～32个字符的字符串，不区分大小写。

**[radius-scheme **]*radius-scheme-name*：指定RADIUS方案。其中，*radius-scheme-name*表示RADIUS方案名，为1～32个字符的字符串，不区分大小写。

【使用指导】

可以指定一个备选的认证方法，在当前的认证方法无效时尝试使用备选的方法完成认证。

目前，远程方案只能支持对名称为level-*n*的用户角色之间的切换进行认证。

·当使用HWTACACS方案进行用户角色切换认证时，系统使用用户输入的用户角色切换用户名进行角色切换认证，HWTACACS服务器上也必须存在相应的用户名，该用户名代表了能够切换到的最大级别。例如，用户希望切换到用户角色level-3，输入的用户名为"test"，在要求携带域名认证的情况下，系统使用用户名"test@*domain-name*"进行用户角色切换认证；在要求不携带域名认证的情况下使用"test"进行用户角色切换认证。

·当使用RADIUS方案进行用户角色切换认证时，系统使用"\$enab*n*\$"形式的用户名进行用户角色切换认证，其中*n*为用户希望切换到的用户角色level-*n*中的*n*，RADIUS服务器上也必须存在相同形式的用户名。例如，用户希望切换到用户角色level-3，输入任意用户名，系统忽略用户输入的用户名，使用"\$enab3\$@*domain-name*"或"\$enab3\$"形式的用户名进行用户角色切换认证（是否携带域名由**user-name-format**命令决定）。

【举例】

\# 在ISP域test下，配置使用HWTACACS方案tac进行用户角色切换认证。

\<Sysname\> system-view

Sysname super authentication-mode scheme

Sysname domain test

Sysname-domain-test authentication super hwtacacs-scheme tac

【相关命令】

·**authentication default**

·**hwtacacs scheme**

·**radius scheme**

**AAA \-- ISP域中实现AAA配置命令 \-- authorization advpn**

------------------------------------------------------------------------

![说明](AAA命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[authorization advpn**]命令用来为ADVPN用户配置授权方法。

**[undo authorization advpn**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[authorization advpn** { **local** [ **none**  \| **none** \| **radius-scheme** *radius-scheme-name*  **local**   **none**  }]]

**[undo authorization advpn**]

FIPS模式下：

**[authorization advpn**[ { **local** \| **radius-scheme** *radius-scheme-name* [ **local** ] }]]

**[undo authorization advpn**]

【缺省情况】

ADVPN用户采用当前ISP域的缺省授权方法。

【视图】

ISP域视图

【支持的缺省用户角色】

network-admin

mdc-admin

【参数】

**[local**]：本地计费。

**[none**]：不计费。

**[radius-scheme*** radius-scheme-name*]：指定RADIUS方案。其中，*radius-scheme-name*表示RADIUS方案名，为1～32个字符的字符串，不区分大小写。

【使用指导】

在一个ISP域中，只有配置的认证和授权方法中引用了相同的RADIUS方案时，RADIUS授权过程才能生效。

可以指定一个或多个备选的授权方法，在当前的授权方法无效时按照配置顺序尝试使用备选的方法完成授权。例如，**radius-scheme** *radius-scheme-name* **local** **none**表示，先进行RADIUS授权，若RADIUS授权无效则进行本地授权，若本地授权也无效则不进行授权。

【举例】

\# 在ISP域test下，为ADVPN用户配置授权方法为**local**。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test authorization advpn local

\# 在ISP域test下，配置ADVPN用户使用RADIUS方案rd进行计费，并且使用**local**作为备选计费方法。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test authorization advpn radius-scheme rd local

【相关命令】

·**authorization default**

·**local-user**

·**radius scheme**

**AAA \-- ISP域中实现AAA配置命令 \-- authorization command**

------------------------------------------------------------------------

**[authorization command**]命令用来配置命令行授权方法。

**[undo authorization command**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[authorization command** { **hwtacacs-scheme** *hwtacacs-scheme-name* [ **local**   **none**  \| **local**  **none**  \| **none** }]]

**[undo authorization command**]

FIPS模式下：

**[authorization command** { **hwtacacs-scheme** *hwtacacs-scheme-name* [ **local**  \| **local** }]]

**[undo authorization command**]

【缺省情况】

命令行授权采用当前ISP域的缺省授权方法。

【视图】

ISP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[hwtacacs-scheme*** hwtacacs-scheme-name*]：指定HWTACACS方案。其中，*hwtacacs-scheme-name*表示HWTACACS方案名，为1～32个字符的字符串，不区分大小写。

**[local**]：本地授权。

**[none**]：不授权。用户执行角色所允许的命令时，无须接受授权服务器的检查。

【使用指导】

命令行授权是指，用户执行的每一条命令都需要接受授权服务器的检查，只有授权成功的命令才被允许执行。用户登录后可以执行的命令受登录授权的用户角色和命令行授权的用户角色的双重限制，即，仅登录授权的用户角色和命令行授权的用户角色均允许执行的命令行，才能被执行。需要注意的是，命令行授权功能只利用角色中的权限规则对命令行执行权限检查，不进行其它方面的权限检查，例如资源控制策略等。

对用户采用本地命令行授权时，设备将根据用户登录设备时输入的用户名对应的本地用户配置来对用户输入的命令进行检查，只有本地用户中配置的授权用户角色所允许的命令才被允许执行。

可以指定一个或多个备选的命令行授权方法，在当前的授权方法无效时按照配置顺序尝试使用备选的方法完成命令授权。例如，**hwtacacs-scheme*** hwtacacs-scheme-name* **local** **none**表示，先进行HWTACACS授权，若HWTACACS授权无效则进行本地授权，若本地授权也无效则不进行授权。

【举例】

\# 在ISP域test下，配置命令行授权方法为**local**。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test authorization command local

\# 在ISP域test下，配置使用HWTACACS方案hwtac进行命令行授权，并且使用**local**作为备选授权方法。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test authorization command hwtacacs-scheme hwtac local

【相关命令】

·**authorization accounting**（基础命令参考/登录设备）

·**hwtacacs scheme**

·**local-user**

**AAA \-- ISP域中实现AAA配置命令 \-- authorization default**

------------------------------------------------------------------------

**[authorization default**]命令用来为当前ISP域配置缺省的授权方法。

**[undo authorization default**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[authorization default** { **hwtacacs-scheme** *hwtacacs-scheme-name* [ **radius-scheme** *radius-scheme-name*   **local**   **none**  \| **local**  **none**  \| **none** \| **radius-scheme** *radius-scheme-name*  **hwtacacs-scheme** *hwtacacs-scheme-name*   **local**   **none**  }]]

**[undo authorization default**]

FIPS模式下：

**[authorization default** { **hwtacacs-scheme** *hwtacacs-scheme-name* [ **radius-scheme** *radius-scheme-name*   **local**  \| **local** \| **radius-scheme** *radius-scheme-name*  **hwtacacs-scheme** *hwtacacs-scheme-name*   **local**  }]]

**[undo authorization default**]

【缺省情况】

当前ISP域的缺省授权方法为**local**。

【视图】

ISP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[hwtacacs-scheme*** hwtacacs-scheme-name*]：指定HWTACACS方案。其中，*hwtacacs-scheme-name*表示HWTACACS方案名，为1～32个字符的字符串，不区分大小写。

**[local**]：本地授权。

**[none**]：不授权。接入设备不请求授权信息，不对用户可以使用的操作以及用户允许使用的网络服务进行授权。此时，认证通过的Login用户（通过Console/AUX/异步串口或者Telnet、FTP/SFTP/SCP访问设备的用户）只有系统所给予的缺省用户角色，其中FTP/SFTP/SCP用户的工作目录是设备的根目录，但并无访问权限；认证通过的非Login用户可直接访问网络。关于缺省用户角色的详细介绍请参见"基础配置指导"中的"RBAC"。

**[radius-scheme**]* radius-scheme-name*：指定RADIUS方案。其中，*radius-scheme-name*表示RADIUS方案名，为1～32个字符的字符串，不区分大小写。

【使用指导】

当前ISP域的缺省的授权方法对于该域中未指定具体授权方法的所有接入用户都起作用，但是如果某类型的用户不支持指定的授权方法，则该授权方法对于这类用户不能生效。

在一个ISP域中，只有配置的认证和授权方法中引用了相同的RADIUS方案时，RADIUS授权过程才能生效。

可以指定一个或多个备选的授权方法，在当前的授权方法无效时按照配置顺序尝试使用备选的方法完成授权。例如，**radius-scheme** *radius-scheme-name* **local** **none**表示，先进行RADIUS授权，若RADIUS授权无效则进行本地授权，若本地授权也无效则不进行授权。

【举例】

\# 在ISP域test下，配置缺省授权方法为使用RADIUS方案rd进行授权，并且使用**local**作为备选授权方法。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test authorization default radius-scheme rd local

【相关命令】

·**hwtacacs scheme**

·**local-user**

·**radius scheme**

**AAA \-- ISP域中实现AAA配置命令 \-- authorization ipoe**

------------------------------------------------------------------------

**[authorization ipoe**]命令用来为IPoE用户配置授权方法。

**[undo authorization ipoe**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[authorization ipoe****local **\**[ none ** \|]** none **[\|]** radius-scheme***radius-scheme-name* \**[ local ** \** none **]****}

**[undo authorization ipoe**]

FIPS]模式下：

**[authorization ipoe****local **[\|]** radius-scheme***radius-scheme-name* \**[ local ** }]

**[undo authorization ipoe**]

【缺省情况】]

IPoE用户采用当前ISP域的缺省授权方法。

【视图】

ISP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[local**]：本地授权。

**[none**]：不授权。

**[radius-scheme**]* radius-scheme-name*：指定RADIUS方案。其中，*radius-scheme-name*表示RADIUS方案名，为1～32个字符的字符串，不区分大小写。

【使用指导】

在一个ISP域中，只有配置的认证和授权方法中引用了相同的RADIUS方案时，RADIUS授权过程才能生效。

可以指定一个或多个备选的授权方法，在当前的授权方法无效时按照配置顺序尝试使用备选的方法完成授权。例如，**radius-scheme***radius-scheme-name***local****none**表示，先进行RADIUS授权，若RADIUS授权无效则进行本地授权，若本地授权也无效则不进行授权。

【举例】

\# 在ISP域test下，为IPoE用户配置授权方法为**local**。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test authorization ipoe local

\# 在ISP域test下，配置IPoE用户使用RADIUS方案rd进行授权，并且使用**local**作为备选授权方法。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test authorization ipoe radius-scheme rd local

【相关命令】

·**authorization default**

·**local-user**

·**radius scheme**

**AAA \-- ISP域中实现AAA配置命令 \-- authorization lan-access**

------------------------------------------------------------------------

![说明](AAA命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[authorization lan-access**]命令用来为lan-access用户配置授权方法。

**[undo authorization lan-access**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[authorization lan-access** { **local** [ **none**  \| **none** \| **radius-scheme** *radius-scheme-name*  **local**   **none**  }]]

**[undo authorization lan-access**]

FIPS模式下：

**[authorization lan-access**[ { **local** \| **radius-scheme** *radius-scheme-name* [ **local** ] }]]

**[undo authorization lan-access**]

【缺省情况】

lan-access用户采用当前ISP域的缺省授权方法。

【视图】

ISP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[local**]：本地授权。

**[none**]：不授权。接入设备不请求授权信息，不对用户可以使用的操作以及用户允许使用的网络服务进行授权，认证通过的lan-access用户可直接访问网络。

**[radius-scheme**]* radius-scheme-name*：指定RADIUS方案。其中，*radius-scheme-name*表示RADIUS方案名，为1～32个字符的字符串，不区分大小写。

【使用指导】

在一个ISP域中，只有配置的认证和授权方法中引用了相同的RADIUS方案时，RADIUS授权过程才能生效。

可以指定一个或多个备选的授权方法，在当前的授权方法无效时按照配置顺序尝试使用备选的方法完成授权。例如，**radius-scheme** *radius-scheme-name* **local** **none**表示，先进行RADIUS授权，若RADIUS授权无效则进行本地授权，若本地授权也无效则不进行授权。

【举例】

\# 在ISP域test下，为lan-access用户配置授权方法为**local**。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test authorization lan-access local

\# 在ISP域test下，配置lan-access用户使用RADIUS方案rd进行授权，并且使用**local**作为备选授权方法。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test authorization lan-access radius-scheme rd local

【相关命令】

·**authorization default**

·**local-user**

·**radius scheme**

**AAA \-- ISP域中实现AAA配置命令 \-- authorization login**

------------------------------------------------------------------------

**[authorization login**]命令用来为login用户配置授权方法。

**[undo authorization login**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[authorization login** { **hwtacacs-scheme** *hwtacacs-scheme-name* [ **radius-scheme** *radius-scheme-name*   **local**   **none**  \| **local**  **none**  \| **none** \| **radius-scheme** *radius-scheme-name*  **hwtacacs-scheme** *hwtacacs-scheme-name*   **local**   **none**  }]]

**[undo authorization login**]

FIPS模式下：

**[authorization login** { **hwtacacs-scheme** *hwtacacs-scheme-name* [ **radius-scheme** *radius-scheme-name*   **local**  \| **local** \| **radius-scheme** *radius-scheme-name*  **hwtacacs-scheme** *hwtacacs-scheme-name*   **local**  }]]

**[undo authorization login**]

【缺省情况】

login用户采用当前ISP域的缺省授权方法。

【视图】

ISP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[hwtacacs-scheme*** hwtacacs-scheme-name*]：指定HWTACACS方案。其中，*hwtacacs-scheme-name*表示HWTACACS方案名，为1～32个字符的字符串，不区分大小写。

**[local**]：本地授权。

**[none**]：不授权。接入设备不请求授权信息，不对用户可以使用的操作以及用户允许使用的网络服务进行授权。此时，认证通过的Login用户（通过Console/AUX/异步串口或者Telnet、FTP/SFTP/SCP访问设备的用户）只有系统所给予的缺省用户角色，其中FTP/SFTP/SCP用户的工作目录是设备的根目录，但并无访问权限。关于缺省用户角色的详细介绍请参见"基础配置指导"中的"RBAC"。

**[radius-scheme**]* radius-scheme-name*：指定RADIUS方案。其中，*radius-scheme-name*表示RADIUS方案名，为1～32个字符的字符串，不区分大小写。

【使用指导】

在一个ISP域中，只有配置的认证和授权方法中引用了相同的RADIUS方案时，RADIUS授权过程才能生效。

可以指定一个或多个备选的授权方法，在当前的授权方法无效时按照配置顺序尝试使用备选的方法完成授权。例如，**radius-scheme** *radius-scheme-name* **local** **none**表示，先进行RADIUS授权，若RADIUS授权无效则进行本地授权，若本地授权也无效则不进行授权。

【举例】

\# 在ISP域test下，为login用户配置授权方法为**local**。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test authorization login local

\# 在ISP域test下，配置login用户使用RADIUS方案rd进行授权，并且使用**local**作为备选授权方法。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test authorization login radius-scheme rd local

【相关命令】

·**authorization default**

·**hwtacacs scheme**

·**local-user**

·**radius scheme**

**AAA \-- ISP域中实现AAA配置命令 \-- authorization portal**

------------------------------------------------------------------------

**[authorization portal**]命令用来为Portal用户配置授权方法。

**[undo authorization portal**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[authorization portal **{ **local** [ **none**  \| **none** \| **radius-scheme** *radius-scheme-name*  **local**   **none**  }]]

**[undo authorization portal**]

FIPS模式下：

**[authorization portal **[{ **local** \| **radius-scheme** *radius-scheme-name* [ **local** ] }]]

**[undo authorization portal**]

【缺省情况】

Portal用户采用当前ISP域的缺省授权方法。

【视图】

ISP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[local**]：本地授权。

**[none**]：不授权。接入设备不请求授权信息，不对用户可以使用的操作以及用户允许使用的网络服务进行授权，认证通过的Portal用户可直接访问网络。

**[radius-scheme**]* radius-scheme-name*：指定RADIUS方案。其中，*radius-scheme-name*表示RADIUS方案名，为1～32个字符的字符串，不区分大小写。

【使用指导】

在一个ISP域中，只有配置的认证和授权方法中引用了相同的RADIUS方案时，RADIUS授权过程才能生效。

可以指定一个或多个备选的授权方法，在当前的授权方法无效时按照配置顺序尝试使用备选的方法完成授权。例如，**radius-scheme** *radius-scheme-name* **local** **none**表示，先进行RADIUS授权，若RADIUS授权无效则进行本地授权，若本地授权也无效则不进行授权。

【举例】

\# 在ISP域test下，为Portal用户配置授权方法为**local**。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test authorization portal local

\# 在ISP域test下，配置Portal用户使用RADIUS方案rd进行授权，并且使用**local**作为备选授权方法。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test authorization portal radius-scheme rd local

【相关命令】

·**authorization default**

·**local-user**

·**radius scheme**

**AAA \-- ISP域中实现AAA配置命令 \-- authorization ppp**

------------------------------------------------------------------------

![说明](AAA命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[authorization ppp**]命令用来为PPP用户配置授权方法。

**[undo authorization ppp**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[authorization ppp****hwtacacs-scheme ***hwtacacs-scheme-name***** **radius-scheme** *radius-scheme-name* ]  **local**   **none**  [\| **local** [ **none** ] \| **none** \| **radius-scheme** *radius-scheme-name* ] **hwtacacs-scheme** *hwtacacs-scheme-name*   **local**   **none**  }

**[undo authorization ppp**]

FIPS模式下：

**[authorization ppp****hwtacacs-scheme ***hwtacacs-scheme-name***** **radius-scheme** *radius-scheme-name* ]  **local**  [\| **local** \| **radius-scheme** *radius-scheme-name* ] **hwtacacs-scheme** *hwtacacs-scheme-name*   **local**  }

**[undo authorization ppp**]

【缺省情况】

PPP用户采用当前ISP域的缺省授权方法。

【视图】

ISP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[hwtacacs-scheme ***hwtacacs-scheme-name*]：指定HWTACACS方案。其中*hwtacacs-scheme-name*表示HWTACACS方案名，为1～32个字符的字符串，不区分大小写。

**[local**]：本地授权。

**[none**]：不授权。接入设备不请求授权信息，不对用户可以使用的操作以及用户允许使用的网络服务进行授权。

**[radius-scheme**]* radius-scheme-name*：指定RADIUS方案。其中，*radius-scheme-name*表示RADIUS方案名，为1～32个字符的字符串，不区分大小写。

【使用指导】

在一个ISP域中，只有配置的认证和授权方法中引用了相同的RADIUS方案时，RADIUS授权过程才能生效。

可以指定一个或多个备选的授权方法，在当前的授权方法无效时按照配置顺序尝试使用备选的方法完成授权。例如，**radius-scheme** *radius-scheme-name* **local** **none**表示，先进行RADIUS授权，若RADIUS授权无效则进行本地授权，若本地授权也无效则不进行授权。

【举例】

\# 在ISP域test下，为PPP用户配置授权方法为**local**。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test authorization ppp local

\# 在ISP域test下，配置PPP用户使用RADIUS方案rd进行授权，并且使用**local**作为备选授权方法。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test authorization ppp radius-scheme rd local

【相关命令】

·**authorization default**

·**hwtacacs scheme**

·**local-user**

·**radius scheme**

**AAA \-- ISP域中实现AAA配置命令 \-- authorization sslvpn**

------------------------------------------------------------------------

**[authorization sslvpn**]命令用来为SSL VPN用户配置授权方法。

**[undo authorization sslvpn**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[authorization sslvpn **{ **ldap-scheme** *ldap-scheme-name* [ **local**   **none**  \| **local**  **none**  \| **none** \| **radius-scheme** *radius-scheme-name*  **local**   **none**  }]]

**[undo authorization sslvpn**]

FIPS模式下：

**[authorization sslvpn **{ **ldap-scheme** *ldap-scheme-name* [ **local**  \| **local** \| **radius-scheme** *radius-scheme-name*  **local**  }]]

**[undo authorization sslvpn**]

【缺省情况】

SSL VPN用户采用当前ISP域缺省授权方法。

【视图】

ISP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ldap-scheme ***ldap-scheme-name*]：指定LDAP方案。其中，*ldap-scheme-name*表示LDAP方案名，为1～32个字符的字符串，不区分大小写。

**[local**]：本地授权。

**[none**]：不授权。接入设备不请求授权信息，不对用户可以使用的操作以及用户允许使用的网络服务进行授权，认证通过的SSL VPN用户可以直接访问网络。

**[radius-scheme ***radius-scheme-name*]：指定RADIUS方案。其中，radius-scheme-name表示RADIUS方案名，为1～32个字符的字符串，不区分大小写。

【使用指导】

可以指定一个或多个备选的授权方法，在当前的授权方法无效时按照配置顺序尝试使用备选的方法完成授权。例如，**radius-scheme** *radius-scheme-name* **local** **none**表示，先进行RADIUS授权，若RADIUS授权无效则进行本地授权，若本地授权也无效则不进行授权。

【举例】

\# 在ISP域test下，为SSL VPN用户配置授权方法为**local**。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test authorization sslvpn local

\# 在ISP域test下，配置SSL VPN用户使用LDAP方案ldp进行授权，并且使用**local**作为备选授权方法。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test authorization sslvpn ldap-scheme ldp local

【相关命令】

·**authorization default**

·**ldap scheme**

·**local-user**

·**radius scheme**

**AAA \-- ISP域中实现AAA配置命令 \-- authorization-attribute（ISP domain view）**

------------------------------------------------------------------------

**[authorization-attribute**]命令用来设置当前ISP域下的用户授权属性。

**[undo** **authorization-attribute**]命令用来删除配置的授权属性，恢复用户具有的缺省访问权限。

【命令】

**[authorization-attribute ******[\| **mld max-access-number** *number* \| { **primary-dns** \| **secondary-dns** } { **ip** *ipv4-address* \| **ipv6** *ipv6-address* } \| **session-group-profile** *session-group-profile-name* \| **url** *url-string* \| **user-group** *user-group-name* \| **user-profile** *profile-name* \| **vpn-instance** *vpn-instance-name* }]

**[undo authorization-attribute **[{ **acl** \| **car** \| **idle-cut** \| **igmp** \| **ip-pool** \| **ipv6-pool** \| **ipv6-prefix** \| **mld** \| **primary-dns** \| **secondary-dns** \| **session-group-profile** \| **url** \| **user-group** \| **user-profile** \| **vpn-instance** }]]

【缺省情况】]

未对当前ISP域下的用户设置任何授权属性，其中用户闲置切换功能处于关闭状态。

【视图】

ISP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[acl ***acl-number*]：指定用于匹配用户流量的ACL。其中*acl-number*表示ACL编号，取值范围2000～5999。IPv4/IPv6用户认证成功后，将仅被授权访问指定的IPv4/IPv6 ACL网络资源。IPv4/IPv6 Portal用户在认证前，若被授权认证域，则将被授权访问指定的IPv4/IPv6 ACL网络资源。

**[car**]：指定授权用户的流量监管动作。Portal用户在认证前，若被授权认证域，则其流量将受到指定的流量监管动作控制。

**[inbound**]：表示用户的上传速率。

**[outbound**]：表示用户的下载速率。

**[cir** *committed-information-rate*]：承诺信息速率，取值范围为1～4194303，单位为kbps。

**[pir ***peak-information-rate*]：峰值速率，取值范围为1～4194303，单位为kbps。若不指定该参数，则表示不对峰值速率进行限制。

**[idle-cut ***minute*]：指定用户的闲置切断时间。其中，*minute*的取值范围为1～600，单位为分钟。

*[flow*]：用户在闲置切断时间内产生的数据流量，取值范围1～10240000，单位为字节，缺省值为10240。

**[igmp max-access-number** *number*]：指定IPv4用户可以同时点播的最大节目数。其中，*number*的取值范围为1～64。此属性只对PPP、Portal和IPoE用户生效。

**[ip-pool ***pool-name*]：指定为用户分配IP地址的地址池。其中，*pool-name*表示地址池名称，为1～31个字符的字符串，不区分大小写。此属性只对PPP、Portal和IPoE用户生效。

**[ipv6-pool** *ipv6-pool-name*]：指定为用户分配IPv6地址的地址池。其中，*ipv6-pool-name*表示地址池名称，为1～63个字符的字符串，不区分大小写。此属性只对PPP、Portal和IPoE用户生效。

**[ipv6-prefix** *ipv6-prefix prefix-length*]：指定为用户分配的IPv6前缀。其中，*ipv6-prefix prefix-length*为前缀地址和前缀长度，前缀长度取值范围是1～128。此属性只对PPP、IPoE用户生效。

**[mld max-access-number** *number*]：指定IPv6用户可以同时点播的最大节目数。其中，*number*的取值范围为1～64。此属性只对PPP、Portal和IPoE用户生效。

**[primary-dns ip** *ipv4-address*]：指定用户的主DNS服务器IPv4地址。此属性只对PPP用户生效。

**[primary-dns ipv6** *ipv6-address*]：指定用户的主DNS服务器IPv6地址。此属性只对PPP用户生效。

**[secondary-dns ip** *ip-address*]：指定用户的从DNS服务器IPv4地址。此属性只对PPP用户生效。

**[secondary-dns ipv6** *ipv6-address*]：指定用户的从DNS服务器IPv6地址。此属性只对PPP用户生效。

**[session-group-profile ***session-group-profile-name*]：指定用户的授权Session Group Profile。其中，*session-group-profile-name*为Session Group Profile名称，为1～31个字符的字符串，区分大小写。Portal用户在认证前，若被授权认证域，则其访问行为将受到该域中的Session Group Profile配置的限制。

**[url ***url-string*]：指定用户的强制URL，为1～255个字符的字符串，区分大小写。用户认证成功后，此URL将被推送至PPP客户端。此属性只对PPP用户生效。

**[user-group ***user-group-name*]：表示用户所属用户组。其中，*user-group-name*表示用户组名，为1～32个字符的字符串，不区分大小写。用户认证成功后，将继承该用户组中的所有属性。

**[user-profile ***profile-name*]：指定用户的授权User Profile。其中，*profile-name*为User Profile名称，为1～31个字符的字符串，区分大小写。Portal用户在认证前，若被授权认证域，则其访问行为将受到该域中的User Profile配置的限制。

**[vpn-instance** *vpn-instance-nam*e]：指定用户所属的VPN。其中，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。用户认证成功后，将被授权允许访问指定VPN中的网络资源。此属性只对PPP和IPoE用户生效。

【使用指导】

用户上线后，设备会周期性检测用户的流量，若域内某用户在指定的闲置检测时间内产生的流量小于本命令中指定的数据流量，则会被强制下线。需要注意的是，服务器上也可以配置最大空闲时间实现对用户的闲置切断功能，具体为当用户在指定的闲置检测时间内产生的流量小于10240个字节（服务器上该阈值为固定值，不可配置）时，会被强制下线。但是，只有在设备上的闲置切断功能处于关闭状态时，服务器才会根据自身的配置来控制用户的闲置切断。

如果当前ISP域的用户认证成功，但认证服务器（包括本地认证下的接入设备）未对该ISP域下发授权属性，则系统使用当前ISP下指定的授权属性为用户授权。

需要注意的是，可通过多次执行本命令配置多个授权属性，但对于相同授权属性，新配置会覆盖原有的配置。

【举例】

\# 指定ISP域test下的用户闲置切断时间为30分钟，闲置切断时间内产生的流量为10240字节。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test authorization-attribute idle-cut 30 10240

【相关命令】

·**display domain**

**AAA \-- ISP域中实现AAA配置命令 \-- display domain**

------------------------------------------------------------------------

**[display domain**]命令用来显示所有或指定ISP域的配置信息。

【命令】

**[display domain** [ *isp-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[isp-name*]：指定ISP域名，为1～24个字符的字符串，不区分大小写。

【使用指导】

如果不指定ISP域，则显示系统中所有ISP域的配置信息。

【举例】

\# 显示系统中所有ISP域的配置信息。

\<Sysname\> display domain

Total 2 domains

Domain: system

  State: Active

  Default authentication scheme:  Local

  Default authorization  scheme:  Local

  Default accounting     scheme:  Local

  Accounting start failure action: Online

  Accounting update failure action: Online

  Accounting quota out action: Offline

  Service type: HSI

  Session time: Exclude idle time

  Authorization attributes :

    Idle-cut: Disabled

    IGMP access number: 4

    MLD access number:  4

Domain: dm

  State: Active

  Login   authentication scheme:  RADIUS=rad

  Login   authorization  scheme:  HWTACACS=hw

  Super   authentication scheme:  RADIUS=rad

  PPP     accounting     scheme:  RADIUS=r1, (RADIUS=r2), HWTACACS=tc, Local

  Command authorization  scheme:  HWTACACS=hw

  LAN access authentication scheme:  RADIUS=r4

  Portal  authentication scheme:  LDAP=ldp

  IPoE    authentication scheme:  RADIUS=rad, Local, None

  SSL VPN authentication scheme:  LDAP=ldp, Local, None

  SSL VPN authorization  scheme:  LDAP=ldp, Local

  SSL VPN accounting     scheme:  None

  Default authentication scheme:  ldap=rad, Local, None

  Default authorization  scheme:  Local

  Default accounting     scheme:  None

  Accounting start failure action: Online

  Accounting update failure action: Online

  Accounting quota out action: Offline

  ITA service poilcy: ita1

  Service type: HIS

  Session time: Include idle time

  Authorization attributes :

    Idle-cut : Enabled

      Idle timeout: 2 minutes

      Flow: 10240 bytes

    IP pool: appy

    User profile: test

    Session group profile: abc

    Inbound CAR: CIR 64000 bps PIR 640000 bps

    Outbound CAR: CIR 64000 bps PIR 640000 bps

    ACL number：3000

    User group: ugg

    IPv6 prefix: 1::1/34

    IPv6 pool: ipv6pool

    Primary DNS server: 6.6.6.6

    Secondary DNS server: 3.6.2.3

    URL: http://portal

    VPN instance: vpn1

    IGMP access number: 12

    MLD access number: 35

Default domain name: system

表1-1 display domain命令显示信息描述表

字段

描述

Total 2 domains

总计2个ISP域

Domain

ISP域名

State

ISP域的状态

Default authentication scheme

缺省的认证方案

Default authorization scheme

缺省的授权方案

Default accounting scheme

缺省的计费方案

Accounting start failure action

用户计费开始失败的动作，包括以下取值：

·Online：如果用户计费开始失败，则保持用户在线

·Offline：如果用户计费开始失败，则强制用户下线

该字段的支持情况与设备的型号有关，请以设备的实际情况为准

Accounting update failure max-times

允许用户连续计费更新失败的次数

Accounting update failure action

用户计费更新失败的动作，包括以下取值：

·Online：如果用户计费更新失败，则保持用户在线

·Offline：如果用户计费更新失败，则强制用户下线

该字段的支持情况与设备的型号有关，请以设备的实际情况为准

Accounting quota out action

用户计费流量配额耗尽策略，包括以下取值：

·Online：如果用户计费流量配额耗尽，则保持用户在线

·Offline：如果用户计费流量配额耗尽，则强制用户下线

该字段的支持情况与设备的型号有关，请以设备的实际情况为准

ITA service poilcy

采用的ITA业务策略

该字段的支持情况与设备的型号有关，请以设备的实际情况为准

Service type

ISP域的业务类型，取值为HIS，STB和VoIP

Session time

设备上传到服务器的用户在线时间，有以下两种情况：

·Include idle time：保留闲置切断时间

·Exclude idle time：扣除闲置切断时间

ADVPN authentication scheme

ADVPN用户认证方案

ADVPN authorization scheme

ADVPN用户授权方案

ADVPN accounting scheme

ADVPN用户计费方案

Login authentication scheme

Login用户认证方案

Login authorization scheme

Login用户授权方案

Login accounting scheme

Login用户计费方案

Authorization attributes

ISP的用户授权属性

Idle-cut

用户闲置切断功能，包括以下取值：

·Enabled：处于使能状态，表示当ISP域中的用户在指定的最大闲置切断时间内产生的流量小于指定的最小数据流量时，会被强制下线。

·Disabled：处于关闭状态，表示不对用户进行闲置切断控制，它为缺省状态

Idle timeout

用户闲置切断时间（单位为分钟）

Flow

用户数据流量阈值（单位为字节）

IP pool

授权IPv4地址池的名称

User profile

授权User Profile的名称

Session group profile

授权Session Group Profile的名称

Inbound CAR

授权的入方向CAR（CIR：平均速率，单位为bps；PIR：峰值速率，单位为bps）

Outbound CAR

授权的出方向CAR（CIR：平均速率，单位为bps；PIR：峰值速率，单位为bps）

ACL number

授权ACL编号

User group

授权User group的名称

IPv6 prefix

授权IPv6前缀

IPv6 pool

授权IPv6地址池的名称

Primary DNS server

授权主DNS服务器地址

Secondary DNS server

授权从DNS服务器地址

URL

授权强制URL

VPN instance

授权VPN实例名称

IGMP max access number

授权IPv4用户可以同时点播的最大节目数

MLD max access number

授权IPv6用户可以同时点播的最大节目数

RADIUS

RADIUS方案

HWTACACS

HWTACACS方案

ldap

LDAP方案

local

本地方案

none

不认证、不授权和不计费

Super authentication scheme

用户角色切换认证方案

PPP authentication scheme

PPP用户的认证方案

PPP authorization scheme

PPP用户的授权方案

PPP accounting scheme

PPP用户的计费方案

Command authorization scheme

命令行授权方案

Command accounting scheme

命令行计费方案

LAN access authentication scheme

lan-access用户认证方案

LAN access authorization scheme

lan-access用户授权方案

LAN access accounting scheme

lan-access用户计费方案

Portal authentication scheme

Portal用户认证方案

Portal authorization scheme

Portal用户授权方案

Portal accounting scheme

Portal用户计费方案

IPoE authentication scheme

IPoE用户认证方案

IPoE authorization scheme

IPoE用户授权方案

IPoE accounting scheme

IPoE用户计费方案

SSL VPN authentication scheme

SSL VPN用户认证方案

SSL VPN authorization scheme

SSL VPN用户授权方案

SSL VPN accounting scheme

SSL VPN用户计费方案

Default Domain Name

缺省ISP域名

**AAA \-- ISP域中实现AAA配置命令 \-- domain**

------------------------------------------------------------------------

**[domain**]命令用来创建ISP域并进入其视图。

**[undo domain**]命令用来删除指定的ISP域。

【命令】

**[domain** *isp-name*]

**[undo domain** *isp-name*]

【缺省情况】

系统存在一个名称为system的ISP域。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[isp-name*]：ISP域名，为1～255个字符的字符串，不区分大小写，不能包括"/"、"\"、"[\|]"、"""、":"、"\*"、"?"、"\<"、"\>"以及"@"字符，且不能为字符串"d"、"de"、"def"、"defa"、"defau"、"defaul"、"default"、"i"、"if"、"if-"、"if-u"、"if-un"、"if-unk"、"if-unkn"、"if-unkno"、"if-unknow"和"if-unknown"。

【使用指导】

需要注意的是：

·所有的ISP域在创建后即处于**active**状态。

·不能删除系统中预定义的ISP域system，只能修改该域的配置。

·不能删除系统缺省的ISP域，除非先恢复要删除的域为非缺省域，系统缺省的ISP域的配置请参考**domain** **default** **enable**命令。

·不能删除为未知域名的用户指定的ISP域，除非首先使用命令**undo domain if-unknown**将其恢复为缺省情况。

【举例】

\# 创建一个新的ISP域test，并进入其视图。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test

【相关命令】

·**display domain**

·**domain** **default** **enable**

·**domain if-unkn****own**

·**state**

**AAA \-- ISP域中实现AAA配置命令 \-- domain default enable**

------------------------------------------------------------------------

**[domain default enable**]命令用来配置系统缺省的ISP域，所有在登录时没有提供ISP域名的用户都属于这个域。

**[undo domain default enable**]命令用来恢复缺省情况。

【命令】

**[domain** **default** **enable** *isp-name*]

**[undo domain default enable**]

【缺省情况】

系统缺省的ISP域为system。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[isp-name*]：ISP域名，为1～255个字符的字符串，不区分大小写。

【使用指导】

需要注意的是：

·缺省的ISP域有且只有一个。

·指定的缺省ISP域必须已经存在。

·配置为缺省的ISP域不能被删除，除非先恢复要删除的域为非缺省域。

【举例】

\# 创建一个新的ISP域test，并设置为系统缺省的ISP域。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test quit

Sysname domain default enable test

【相关命令】

·**display domain**

·**domain**

**AAA \-- ISP域中实现AAA配置命令 \-- domain if-unknown**

------------------------------------------------------------------------

**[domain if-unknown**]命令用来为未知域名的用户指定ISP域。

**[undo domain if-unknown**]命令用来恢复缺省情况。

【命令】

**[domain if-unknown** *isp-domain-name*]

**[undo domain if-unknown**]

【缺省情况】

没有为未知域名的用户指定ISP域。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[isp-domain-name*]：ISP域名。为1～24个字符的字符串，不区分大小写，不能包括"/"、"\"、"[\|]" 、"""、":"、"\*"、"?"、"\<"、"\>"以及"@"字符，且不能为字符串"d"、"de"、"def"、"defa"、"defau"、"defaul"、"default"、"i"、"if"、"if-"、"if-u"、"if-un"、"if-unk"、"if-unkn"、"if-unkno"、"if-unknow"和"if-unknown"。

【使用指导】

设备将按照如下先后顺序选择认证域：接入模块指定的认证域\--\>用户名中指定的ISP域\--\>系统缺省的ISP域。其中，仅部分接入模块支持指定认证域，例如802.1X、Portal、MAC地址认证。

如果根据以上原则决定的认证域在设备上不存在，但设备上为未知域名的用户指定了ISP域，则最终使用该指定的ISP域认证，否则，用户将无法认证。

【举例】

\# 为未知域名的用户指定ISP域为test。

\<Sysname\> system-view

Sysname domain if-unknown test

【相关命令】

·**display domain**

**AAA \-- ISP域中实现AAA配置命令 \-- ita-policy**

------------------------------------------------------------------------

![说明](AAA命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ita-policy**]命令用来指定当前ISP域采用的ITA业务策略。

**[undo ita-policy**]命令用来删除当前ISP域采用的ITA业务策略。

【命令】

**[ita-policy ***policy-name*]

**[undo ita-policy**]

【缺省情况】

当前ISP域中未指定ITA业务策略。

【视图】

ISP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[service-policy-name*]：ITA业务策略名称，由1～31个字符组成，不区分大小写。

【使用指导】

当RADIUS服务器为当前用户动态授权了ITA业务策略时，将使用RADIUS服务器授权的ITA业务策略，否则使用用户认证域中指定的ITA业务策略。

若RADIUS服务器为当前用户授权了ITA业务策略，但该策略在设备上不存在，则即使认证域中指定了ITA业务策略且存在，设备也不会对该用户进行ITA业务计费。

【举例】

\# 在ISP域test中，指定采用ITA业务策略ita1。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-domain-test ita-policy ita1

【相关命令】

·**ita policy**

**AAA \-- ISP域中实现AAA配置命令 \-- nas-id bind vlan**

------------------------------------------------------------------------

**[nas-id bind vlan**]命令用来设置NAS-ID与VLAN的绑定关系。

**[undo nas-id bind vlan**]命令用来删除指定的NAS-ID和VLAN的绑定关系。

【命令】

**[nas-id ***nas-identifier*** bind vlan ***vlan-id*]

**[undo nas-id ***nas-identifier*** bind vlan ***vlan-id*]

【缺省情况】

未设置任何绑定关系。

【视图】

NAS-ID Profile视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[nas-identifier*]：NAS-ID名称，为1～31个字符的字符串，区分大小写。

*[vlan-id*]：与NAS-ID绑定的VLAN ID，取值范围为1～4094。

【使用指导】

一个NAS-ID Profile视图下，可以指定多个NAS-ID与VLAN的绑定关系。

一个NAS-ID可以与多个VLAN绑定，但是一个VLAN只能与一个NAS-ID绑定。若多次将一个VLAN与不同的NAS-ID进行绑定，则最后的绑定关系生效。

【举例】

\#在名称为aaa的NAS-ID Profile视图下，配置NAS-ID 222与VLAN 2的绑定关系。

\<Sysname\> system-view

Sysname aaa nas-id profile aaa

Sysname-nas-id-prof-aaa nas-id 222 bind vlan 2

【相关命令】

·**aaa nas-id profile**

**AAA \-- ISP域中实现AAA配置命令 \-- service-type（ISP domain view）**

------------------------------------------------------------------------

**[service-type**]命令用来设置当前ISP域的业务类型。

**[undo**]**service-type**命令用来恢复缺省情况。

【命令】

**[service-type****hsi**[ \| ]**stb**[ \| ]**voip** }

**[undo service-type**]

【缺省情况】]

当前ISP域的业务类型为**hsi**。

【视图】

ISP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[hsi**]：表示高速上网业务。

**[stb**]：表示数字机顶盒接入业务。

**[voip**]：表示VoIP业务。

【使用指导】

本命令用来配置当前认证域的用户使用的业务类型，用来决定接入模块是否开启组播功能。

·HSI（High Speed Internet，高速上网）业务：主要指使用PPP、802.1X、IPoE专线方式接入网络的用户业务。用户使用该业务类型的ISP域接入时，接入模块不会开启组播功能，可节省系统资源。

·STB（Set Top Box，机顶盒）接入业务：专指使用数字机顶盒接入网络的用户业务。用户使用该业务类型的ISP域接入时，接入模块会开启组播功能，可提高系统处理组播业务的性能。

·VoIP（Voice over IP，IP电话）业务：指使用IP电话的用户业务。用户使用该业务类型的ISP域接入时，QoS功能会开启保证用户语音数据的低延迟传送。

对于IPoE三层专线用户、PPP用户、802.1X用户，ISP域中配置的业务类型无效，系统强制使用HSI业务类型。

【举例】

\# 设置域test下用户业务类型为STB终端业务。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test service-type stb

**AAA \-- ISP域中实现AAA配置命令 \-- session-time include-idle-time**

------------------------------------------------------------------------

**[session-time include-idle-time**]命令用来配置设备上传到服务器的用户在线时间中保留闲置切断时间。

**[undo session-time include-idle-time**]命令用来恢复缺省情况。

【命令】

**[session-time include-idle-time**]

**[undo session-time** **include-idle-time**]

【缺省情况】

设备上传到服务器的用户在线时间中扣除闲置切断时间。

【视图】

ISP域视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当用户正常下线时，设备上传到服务器上的用户在线时间为实际在线时间。当用户异常下线时，若配置为保留闲置切断时间，则上传到服务器上的用户在线时间中包含了一定的闲置切断检测间隔或用户在线探测间隔（该在线探测机制目前仅Portal认证支持），此时服务器上记录的用户时长将大于用户实际在线时长。若配置为扣除闲置切断时间，则上传到服务器上的用户在线时间为，闲置切断检测机制（或用户在线探测机制）计算出的用户已在线时长扣除掉一个闲置切断检测间隔（或一个用户在线探测间隔），此时服务器上记录的用户时长将小于用户实际在线时长。

请根据实际的计费策略决定是否在用户在线时间中保留该闲置切换时间。

【举例】

\#在ISP域test下， 配置设备上传到服务器的用户在线时间中保留闲置切断时间。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-testsession-time include-idle-time

【相关命令】

·**display domain**

**AAA \-- ISP域中实现AAA配置命令 \-- state（ISP domain view）**

------------------------------------------------------------------------

**[state**]命令用来设置当前ISP域的状态。

**[undo state**]命令用来恢复缺省情况。

【命令】

**[state**[ { **active** \| **block** }]]

**[undo state**]

【缺省情况】

当一个ISP域被创建以后，其状态为**active**。

【视图】

ISP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[active**]：指定当前ISP域处于活动状态，即系统允许该域下的用户请求网络服务。

**[block**]：指定当前ISP域处于"阻塞"状态，即系统不允许该域下的用户请求网络服务。

【使用指导】

当指定某个ISP域处于**block**状态时，不允许该域下的用户请求网络服务，但是不影响已经在线的用户。

【举例】

\# 设置当前ISP域test处于"阻塞"状态，域下的接入用户不能再请求网络服务。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test state block

【相关命令】

·**display domain**

**AAA \-- ISP域中实现AAA配置命令 \-- user-address-type**

------------------------------------------------------------------------

**[user-address-type**]命令用来设置当前ISP域的用户地址类型。

**[undo user-address-type**]命令用来恢复缺省情况。

【命令】

**[user-address-type**[ { **ds-lite** \| **ipv6** \| **nat64** \| **private-ds** \| **private-ipv4** \| **public-ds** \| **public-ipv4** }]]

**[undo user-address-type**]

【缺省情况】

未指定当前ISP域的用户地址类型。

【视图】

ISP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ds-lite**]：表示当前用户的地址类型为轻量级双栈地址。

**[ipv6**]：表示当前用户的地址类型为IPv6地址。

**[nat64**]：表示当前用户的地址类型为NAT64地址。

**[private-ds**]：表示当前用户的地址类型为私网双栈地址。

**[private-ipv4**]：表示当前用户的地址类型为私网IPv4地址。

**[public-ds**]：表示当前用户的地址类型为公网双栈地址。

**[public-ipv4**]：表示当前用户的地址类型为公网IPv4地址。

【使用指导】

当更改当前ISP域的用户地址类型时，不影响已经在线的用户。

【举例】

\# 设置当前ISP域用户地址类型为私网双栈地址。

\<Sysname\> system-view

Sysname domain test

Sysname-isp-test user-address-type private-ds

【相关命令】

·**display domain**

**AAA \-- 本地用户配置命令 \-- access-limit**

------------------------------------------------------------------------

**[access-limit**]命令用来设置使用当前本地用户名接入设备的最大用户数。

**[undo access-limit**]命令用来恢复缺省情况。

【命令】

**[access-limit ***max-user-number*]

**[undo access-limit**]

【缺省情况】

不限制使用当前本地用户名接入的用户数。

【视图】

本地用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[max-user-number*]：表示使用当前本地用户名接入设备的最大用户数，取值范围为1～1024。

【使用指导】

本地用户视图下的**access-limit**命令只在该用户采用了本地计费方法的情况下生效。

由于FTP/SFTP/SCP用户不支持计费，因此FTP/SFTP/SCP用户不受此属性限制。

【举例】

\# 允许同时以本地用户名abc在线的用户数为5。

\<Sysname\> system-view

Sysname local-user abc

Sysname-luser-manage-abc access-limit 5

【相关命令】

·**display local-user**

**AAA \-- 本地用户配置命令 \-- authorization-attribute（Local user view/user group view）**

------------------------------------------------------------------------

**[authorization-attribute**]命令用来设置本地用户或用户组的授权属性，该属性在本地用户认证通过之后，由设备下发给用户。

**[undo authorization-attribute**]命令用来删除配置的授权属性，恢复用户具有的缺省访问权限。

【命令】

**[authorization-attribute**[ { **acl** *acl-number* \| **callback-number** *callback-number* \| **idle-cut** *minute* \| **ip** *ipv4-address* \| **ipv6** *ipv6-address* \| **ipv6-pool** *ipv6-pool-name* \| **ipv6-prefix** *ipv6-prefix prefix-length* \| { **primary-dns** \| **secondary-dns** } { **ip** *ip-address* \| **ipv6** *ipv6-address* } \| **sslvpn-policy-group** *group-name* \| **url** *url-string* \| **user-profile** *profile-name* \| **user-role** *role-name* \| **vlan** *vlan-id* \| **vpn-instance** *vpn-instance-name* \| **work-directory** *directory-name* } \*]]

**[undo**[ **authorization-attribute** { **acl** \| **callback-number** \| **idle-cut** \| **ip** \| **ipv6** \| **ipv6-pool** \| **ipv6-prefix** \| **primary-dns** \| **secondary-dns** \| **sslvpn-policy-group** \| **url** \| **user-profile** \| **user-role** *role-name* \| **vlan** \| **vpn-instance** \| **work-directory** } \*]]

【缺省情况】

授权FTP/SFTP/SCP用户可以访问的目录为设备的根目录，但无访问权限。由用户角色为network-admin或level-15的用户创建的本地用户被授权用户角色network-operator。（不支持MDC、Context的设备）

授权FTP/SFTP/SCP用户可以访问的目录为设备的根目录，但无访问权限。在缺省MDC中由用户角色为network-admin或者level-15的用户创建的本地用户被授权用户角色network-operator；在非缺省MDC中由用户角色为mdc-admin或者level-15的用户创建的本地用户被授权用户角色mdc-operator（支持MDC的设备）

授权FTP/SFTP/SCP用户可以访问的目录为设备的根目录，但无访问权限。在缺省Context中由用户角色为network-admin或者level-15的用户创建的本地用户被授权用户角色network-operator；在非缺省Context中由用户角色为context-admin或者level-15的用户创建的本地用户被授权用户角色context-operator（支持Context的设备）

【视图】

本地用户视图/用户组视图（该视图的支持情况与设备的型号有关，请以设备的实际情况为准）

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[acl ***acl-number*]：指定本地用户的授权ACL。其中，*acl-number*为授权ACL的编号，取值范围为2000～5999。本地用户认证成功后，将被授权仅可以访问符合指定ACL规则的网络资源。

**[callback-number** *callback-number*]：指定本地用户的授权PPP回呼号码。其中，*callback-number*为1～64个字符的字符串，区分大小写。本地用户认证成功后，设备将可以使用该用户的授权PPP回呼号码向PPP协商的对端设备发起回呼。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[idle-cut** *minute*]：设置本地用户的闲置切断时间。其中，*minute*为设定的闲置切断时间，取值范围为1～120，单位为分钟。如果用户在线后连续闲置的时长超过该值，设备会强制该用户下线。

**[ip ***ipv4-address*]：指定本地用户的静态IP地址。本地用户认证成功后，将允许使用该IP地址。此属性只对PPP、Portal、IPoE用户生效。

**[ipv6 ***ipv6-address*]：指定本地用户的静态IPv6地址。本地用户认证成功后，将允许使用该IPv6地址。此属性只对PPP、Portal、IPoE用户生效。

**[ipv6-pool** *ipv6-pool-name*]：指定本地用户的IPv6地址池信息。本地用户认证成功后，将允许使用该IPv6地址池分配地址。其中，*ipv6-pool-name*表示地址池名称，为1～63个字符的字符串，不区分大小写。此属性只对PPP、Portal、IPoE用户生效。

**[ipv6-prefix** *ipv6-prefix prefix-length*]：指定本地用户的IPv6前缀信息。*ipv6-prefix prefix-length*为前缀地址和前缀长度，前缀长度取值范围是1～128。本地用户认证成功后，将允许使用该IPv6前缀。此属性只对PPP、IPoE用户生效。

**[primary-dns ip** *ip-address*]：指定本地用户的首选DNS服务器IP地址。本地用户认证成功后，将被授权使用该主DNS服务器。此属性只对PPP用户生效。

**[primary-dns ipv6** *ipv6-address*]：指定本地用户的首选DNS服务器IPv6地址。本地用户认证成功后，将被授权使用该主DNS服务器。此属性只对PPP用户生效。

**[secondary-dns ip** *ip-address*]：指定本地用户的备用DNS服务器IP地址。本地用户认证成功后，将被授权使用该从DNS服务器。此属性只对PPP用户生效。

**[secondary-dns ipv6** *ipv6-address*]：指定本地用户的备用DNS服务器IPv6地址。本地用户认证成功后，将被授权使用该从DNS服务器。此属性只对PPP用户生效。

**[sslvpn-policy-group*** group-name*]：指定本地用户所引用的SSL VPN策略组名，其中，*group-name*为1～31个字符的字符串，不区分大小写。此属性只对SSL VPN用户生效。关于SSL VPN策略组的详细介绍请参见"安全配置指导"中的"SSL VPN"。

**[url ***url-string*]：指定本地用户的强制URL，为1～255个字符的字符串，区分大小写。用户认证成功后，此URL将被推送至PPP客户端。此属性只对PPP用户生效。

**[user-profile*** profile-name*]：指定本地用户的授权User Profile。其中，*profile-name*表示User Profile名称，为1～31个字符的字符串，只能包含英文字母、数字、下划线，区分大小写。当用户认证成功后，其访问行为将受到User Profile中的预设配置的限制。关于User Profile的详细介绍请参见"安全配置指导"中的"User Profile"。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[user-role ***role-name*]：指定本地用户的授权用户角色。其中，*role-name*为1～63个字符的字符串，区分大小写。可以为每个用户最多指定64个用户角色。本地用户角色的相关命令请参见"基础命令参考"中的"RBAC"。该授权属性只能在本地用户视图下配置，不能在本地用户组视图下配置。

**[vlan*** vlan-id*]：指定本地用户的授权VLAN。其中，*vlan-id*为VLAN编号，取值范围为1～4094。本地用户认证成功后，将被授权仅可以访问指定VLAN内的网络资源。

**[vpn-instance** *vpn-instance-name*]：指定本地用户所在的VPN实例。其中，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，不区分大小写。本地用户认证成功后，将允许访问指定VPN中的网络资源。此属性只对PPP用户和IPoE用户生效。

**[work-directory*** directory-name*]：授权FTP/SFTP/SCP用户可以访问的目录。其中，*directory-name*表示FTP/SFTP/SCP用户可以访问的目录，为1～255个字符的字符串，不区分大小写，且该目录必须已经存在。缺省情况下，FTP/SFTP/SCP用户可访问设备的根目录，可通过本参数来修改用户可以访问的目录。

【使用指导】

可配置的授权属性都有其明确的使用环境和用途，请针对用户的服务类型配置对应的授权属性：

·对于ppp用户，仅授权属性**callback-number**、**idle-cut**、**user-profile**、**ip**、**ipv6**、**ipv6-prefix**、**ipv6-pool**、**primary-dns**、**secondary-dns**、**url**和**vpn-instance**有效；

·对于IPoE用户，仅授权属性**idle-cut**、**user-profile**、**ip**、**ipv6**、**ipv6-prefix**、**ipv6-pool**和**vpn-instance**有效；

·对于portal用户，仅授权属性**acl**、**idle-cut**、**user-profile**、**ip**、**ipv6**和**vlan**有效；

·对于lan-access用户，仅授权属性**acl**、**user-profile**和**vlan**有效；

·对于http、https、telnet、terminal用户，仅授权属性**user-role**有效；

·对于ssh、ftp用户，仅授权属性**user-role**和**work-directory**有效；

·对于SSL VPN用户，仅授权属性**sslvpn-policy-group**有效；

·对于其它类型的本地用户，所有授权属性均无效。

需要注意的是：

·用户组的授权属性对于组内的所有本地用户生效，因此具有相同属性的用户可通过加入相同的用户组来统一配置和管理。

·本地用户视图下未配置的授权属性继承所属用户组的授权属性配置，但是如果本地用户视图与所属的用户组视图下都配置了某授权属性，则本地用户视图下的授权属性生效。

·为了避免设备上进行主备倒换后FTP/SFTP/SCP用户无法正常登录，建议用户在指定工作目录时不要携带槽位信息。主备倒换特性以及FTP/SFTP/SCP类型用户的支持情况与设备的型号有关，请以设备的实际情况为准。

·如果希望本地用户仅使用本命令授权的用户角色，建议使用**undo authorization-attribute user-role**命令删除该用户已有的缺省用户角色。

·被授权安全日志管理员的本地用户登录设备后，仅可执行安全日志文件管理相关的命令以及安全日志文件操作相关的命令，具体命令可通过**display role name security-audit**命令查看。安全日志文件管理相关命令的介绍，请参见"网络管理与监控"中的"信息中心"。文件系统管理相关命令的介绍，请参见"基础配置命令参考"中的"文件系统管理"。

·为一个用户授权安全日志管理员角色时，经过界面的交互式确认后，系统会自动删除当前用户的所有其它他用户角色；如果已经授权当前用户安全日志管理员角色，再授权其它的用户角色时，经过界面的交互式确认后，系统会自动删除当前用户的安全日志管理员角色。

·系统中的最后一个安全日志管理员角色的本地用户不可被删除。

【举例】

\# 配置网络接入类本地用户abc的授权VLAN为VLAN 2。

\<Sysname\> system-view

Sysname local-user abc class network

Sysname-luser-network-abc authorization-attribute vlan 2

\# 配置用户组abc的授权VLAN为VLAN 3。

\<Sysname\> system-view

Sysname user-group abc

Sysname-ugroup-abc authorization-attribute vlan 3

\# 配置设备管理类本地用户xyz的授权用户角色为security-audit（安全日志管理员）。

\<Sysname\> system-view

Sysname local-user xyz class manage

Sysname-luser-manage-xyzauthorization-attribute user-role security-audit

This operation will delete all other roles of the user. Are you sure? [Y/N:y]

【相关命令】

·**display local-user**

·**display user-group**

**AAA \-- 本地用户配置命令 \-- bind-attribute**

------------------------------------------------------------------------

**[bind-attribute**]命令用来设置用户的绑定属性。

**[undo bind-attribute**]命令用来删除配置的用户绑定属性。

【命令】

**[bind-attribute **{ **call-number** *call-number* [ **:** *subcall-number*  \| **ip** *ip-address* \| **location** **interface** *interface-type* *interface-number* \| **mac** *mac-address* \| **vlan** *vlan-id* } \*]]

**[undo bind-attribute **[{ **call-number** \| **ip** \| **location** \| **mac** \| **vlan** } \*]]

【缺省情况】

未设置用户的任何绑定属性。

【视图】

本地用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[call-number** *call-number*]：指定PPP用户认证的主叫号码。其中*call-number*为1～64个字符的字符串。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[subcall-number*]：指定子主叫号码。如果配置了子主叫号码，则主叫号码与子主叫号码的总长度不能大于62个字符。

**[ip ***ip-address*]：指定用户的IP地址。

**[location interface ***interface-type interface-number*]：指定用户绑定的接口。其中*interface-type interface-number*表示接口类型和接口编号。如果用户接入的接口与此处绑定的接口不一致，则认证失败。

**[mac ***mac-address*]：指定用户的MAC地址。其中，*mac-address*为H-H-H格式。

**[vlan ***vlan-id*]：指定用户所属于的VLAN。其中，*vlan-id*为VLAN编号，取值范围为1～4094。

【使用指导】

需要注意的是，当对本地用户进行认证时，如果配置了绑定属性，则会检查用户的实际属性与配置的绑定属性是否一致，如果不一致或用户未携带该绑定属性则认证失败。而且，由于认证检测时不区分用户的接入服务类型，即会对所有类型的用户都进行已配置绑定属性的认证检测，因此在配置绑定属性时要考虑某类型的用户是否需要绑定某些属性。例如，只有支持IP地址上传功能的802.1X认证用户才可以配置绑定IP地址；对于不支持IP地址上传功能的MAC地址认证用户，如果配置了绑定IP地址，则会导致该用户的本地认证失败。

·绑定属性**call-number**仅适用于PPP用户；

·绑定属性**ip**仅适用于lan-access类型中的802.1X用户；

·绑定属性**location**、**mac**和**vlan**仅适用于lan-access、PPP、IPoE、Portal类型的用户。

在绑定接口属性时要考虑绑定接口类型是否合理。例如对802.1X认证用户绑定接口需要绑定物理接口，如果绑定VLAN接口等虚接口，则会导致该用户的本地认证失败。

【举例】

\# 配置网络接入类本地用户abc的绑定IP为3.3.3.3。

\<Sysname\> system-view

Sysname local-user abc class network

Sysname-luser-network-abc bind-attribute ip 3.3.3.3

【相关命令】

·**display local-user**

**AAA \-- 本地用户配置命令 \-- display local-user**

------------------------------------------------------------------------

**[display local-user**]命令用来显示本地用户的配置信息和在线用户数的统计信息。

【命令】

**[display local-user **[[ **class** { **manage** \| **network** } \| **idle-cut** { **disable** \| **enable** } \| **service-type** ]**ipoe**[ \| **lan-access** \| **pad** \| **portal** \| **ppp** \| **ssh** \| **sslvpn** \| **telnet** \| **terminal** } \| **state** { **active** \| **block** } \| **user-name** *user-name* \| **vlan** *vlan-id* ]]

【视图】]

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[class**]：显示指定用户类别的本地用户信息。

·**manage**：设备管理类用户。

·**network**：网络接入类用户。

**[idle-cut**[ { **disable** \| **enable** }]]：显示使能或未使能闲置切断功能的本地用户信息。其中，**disable**表示未启用闲置切断功能的本地用户；**enable**表示启用了闲置切断功能并配置了闲置切断时间的本地用户。

**[service-type**]：显示指定用户类型的本地用户信息。各用户类型的支持情况与设备的型号有关，请以设备的实际情况为准。

·**advpn**：ADVPN隧道用户。

·**ftp**：FTP用户。

·**http**：HTTP用户。

·**https**：HTTPS用户。

·**ipoe**：IPoE用户（主要指IP接入用户，比如二/三层专线用户，数字机顶盒接入用户）。

·**lan-access**：lan-access类型用户（主要指以太网接入用户，比如802.1X用户）。

·**pad**：X.25 PAD用户。

·**portal**：Portal用户。

·**ppp**：PPP用户。

·**ssh**：SSH用户。

·**[sslvpn**]{.ItemStepChar}：SSL VPN用户。

·**telnet**：Telnet用户。

·**terminal**：从CON口、AUX口、Asyn口登录的终端用户。不同型号的设备支持的用户登录接口类型不同，请以设备的实际情况为准

**[state**[ { **active** \| **block** }]]：显示处于指定状态的本地用户信息。其中，**active**表示用户处于活动状态，即系统允许该用户请求网络服务；**block**表示用户处于阻塞状态，即系统不允许用户请求网络服务。

**[user-name** *user-name*]：显示指定用户名的本地用户信息。其中，*user-name*表示本地用户名，为1～55个字符的字符串，区分大小写，不能携带域名。

**[vlan** *vlan-id*]：显示指定VLAN内的所有本地用户信息。其中，*vlan-id*为VLAN编号，取值范围为1～4094。

【使用指导】

如果不指定任何参数，则显示所有本地用户信息。

【举例】

\# 显示所有本地用户的相关信息。

\<Sysname\> display local-user

Total 2 local users matched.

Device management user root:

 State:                    Active

 Service type:             SSH/Telnet/Terminal

 Access limit:             Enabled           Max access number: 3

 Current access number:    1

 User group:               system

 Bind attributes:

 Authorization attributes:

  Work directory:          flash:

  User role list:          network-admin

 Password control configurations:

  Password aging:          Enabled (3 days)

Network access user jj:

 State:                    Active

 Service type:             Lan-access

 User group:               system

 Bind attributes:

  IP address:              2.2.2.2

  Location bound:          GigabitEthernet1/0/1

  MAC address:             0001-0001-0001

  VLAN ID:                 2

  Calling number:          2:2

 Authorization attributes:

  Idle timeOut:            33 (min)

  Work directory:          flash:

  ACL number:              2000

  User profile:            pp

  User role list:          network-operator, level-0, level-3

  SSL VPN policy group:    spg

表1-2 display local-user命令显示信息描述表

字段

描述

Total 2 local users matched.

总计有2个本地用户匹配

State

本地用户状态

·Active：活动状态

·Block：阻塞状态

Service type

本地用户使用的服务类型，取值包括ADVPN、FTP、HTTP、HTTPS、Lan-access、PAD、Portal、PPP、SSH、Telnet、Terminal和SSL VPN{.TableTextChar}

Access limit

是否对使用该用户名的接入用户数进行限制

Max access number

最大接入用户数

Current access number

使用该用户名的当前接入用户数

User group

本地用户所属的用户组

Bind attributes

本地用户的绑定属性

IP address

本地用户的IP地址

Location bound

本地用户绑定的端口

MAC address

本地用户的MAC地址

VLAN ID

本地用户绑定的VLAN

Calling number

ISDN用户的主叫号码

Authorization attributes

本地用户的授权属性

Idle timeOut

本地用户闲置切断时间（单位为分钟）

Callback number

本地用户的授权PPP回呼号码

Work directory

FTP/SFTP/SCP用户可以访问的目录

ACL number

本地用户授权ACL

VLAN ID

本地用户授权VLAN

User profile

本地用户授权User Profile

该字段的支持情况与设备的型号有关，请以设备的实际情况为准

User role list

本地用户的授权用户角色列表

SSL VPN policy group

本地用户的授权SSL VPN策略组

IP address

本地用户的授权IPv4地址

IPv6 address

本地用户的授权IPv6地址

IPv6 prefix

本地用户的授权IPv6前缀

IPv6 pool

本地用户的授权IPv6地址池

Primary DNS server

本地用户的授权首选DNS服务器IP地址

Secondary DNS server

本地用户的授权备用DNS服务器IP地址

URL

本地用户的授权强制URL

VPN instance

本地用户的授权VPN实例

Password control configurations

本地用户的密码控制属性

Password aging

密码老化功能的开启状态（密码的老化时间）

Password length

密码最小长度功能的开启状态（密码的最小长度）

Password composition

密码组合策略的开启状态（密码元素的组合类型、至少要包含每种元素的个数）

Password complexity

密码复杂度检查功能的开启状态（检查是否包含用户名或者颠倒的用户名；检查是否包含三个或以上相同字符）

Maximum login attempts

用户最大登录尝试次数

Action for exceeding login attempts

登录尝试次数达到设定次数后的用户帐户锁定行为

**AAA \-- 本地用户配置命令 \-- display user-group**

------------------------------------------------------------------------

![说明](AAA命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display user-group**]命令用来显示用户组的相关配置。

【命令】

**[display user-group** [ *group-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[group-name*]：显示指定用户组的配置。*group-name*表示用户组名称，为1～32个字符的字符串，不区分大小写。

【使用指导】

若不指定用户组名称，则显示所有用户组的相关配置。

【举例】

\# 显示所有用户组的相关配置。

\<Sysname\> display user-group

Total 2 user groups matched.

The contents of user group system:

 Authorization attributes:

  Work directory:          flash:

The contents of user group jj:

 Authorization attributes:

  Idle timeOut:            2 (min)

  Callback number:         2:2

  Work directory:          flash:/

ACL number:              2000

  VLAN ID:                 2

  User profile:            pp

SSL VPN policy group:    policygroup1

Password control configurations:

  Password aging:          Enabled (2 days)

表1-3 display user-group命令显示信息描述表

字段

描述

Total 2 user groups matched.

总计有2个用户组匹配

Idle timeOut

闲置切断时间（单位：分钟）

Callback number

PPP回呼号码

Work directory

FTP/SFTP/SCP用户可以访问的目录

ACL number

授权ACL号

VLAN ID

授权VLAN ID

User profile

授权User Profile名称

SSL VPN policy group

授权SSL VPN策略组名称

IPv6 prefix

授权IPv6前缀

IPv6 pool

授权IPv6地址池

Primary DNS server

授权首选DNS服务器IP地址

Secondary DNS server

授权备用DNS服务器IP地址

URL

授权强制URL

VPN instance

授权VPN实例

Password control configurations

用户组的密码控制属性

Password aging

密码老化功能的开启状态（密码的老化时间）

Password length

密码最小长度功能的开启状态（密码的最小长度）

Password composition

密码组合策略的开启状态（密码元素的组合类型、至少要包含每种元素的个数）

Password complexity

密码复杂度检查功能的开启状态（检查是否包含用户名或者颠倒的用户名；检查是否包含三个或以上相同字符）

Maximum login attempts

用户最大登录尝试次数

Action for exceeding login attempts

登录尝试次数达到设定次数后的用户帐户锁定行为

**AAA \-- 本地用户配置命令 \-- group**

------------------------------------------------------------------------

**[group**]命令用来设置本地用户所属的用户组。

**[undo group**]命令用来恢复缺省配置。

【命令】

**[group** *group-name*]

**[undo group**]

【缺省情况】

用户属于系统默认创建的用户组system。

【视图】

本地用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-name*]：用户组名称，为1～32个字符的字符串，不区分大小写。

【举例】

\# 设置设备管理类本地用户111所属的用户组为abc。

\<Sysname\> system-view

Sysname local-user 111 class manage

Sysname-luser-manage-111 group abc

【相关命令】

·**display local-user**

**AAA \-- 本地用户配置命令 \-- local-user**

------------------------------------------------------------------------

**[local-user**]命令用来添加本地用户，并进入本地用户视图。

**[undo local-user**]命令用来删除指定的本地用户。

【命令】

**[local-user ***user-name *[[ **class** { **manage** \| **network** } ]]]

**[undo local-user **[{ *user-name* **class** { **manage** \| **network** } \| **all** [ **service-type** { **advpn** \| **ftp** \| **http** \| **https** \| **ipoe** \| **lan-access** \| **pad** \| **portal** \| **ppp** \| **ssh** \| **sslvpn** \| **telnet** \| **terminal** } \| **class** { **manage** \| **network** } ] }]]

【缺省情况】

不存在本地用户。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[user-name*]：表示本地用户名，为1～55个字符的字符串，区分大小写。用户名不能携带域名，不能包括符号"\"、"[\|]"、"/"、":"、"\*"、"?"、"\<"、"\>"和"@"，且不能为"a"、"al"或"all"。

**[class**]：指定本地用户的类别。若不指定本参数，则表示设备管理类用户。

·**manage**：设备管理类用户，用于登录设备，对设备进行配置和监控。此类用户可以提供**ftp**、**http**、**https**、**telnet**、**ssh**、**terminal**和**pad**服务。

·**network**：网络接入类用户，用于通过设备接入网络，访问网络资源。此类用户可以提供**advpn**、**lan-access**、**portal**、**ppp**和**sslvpn**服务。

**[all**]：所有的用户。

**[service-type**]：指定用户的类型。各用户类型的支持情况与设备的型号有关，请以设备的实际情况为准。

·**advpn**：ADVPN隧道用户。

·**ftp**：表示FTP类型用户。

·**http**：表示HTTP类型用户。

·**http****s**：表示HTTPS类型用户。

·**ipoe**：表示IPoE类型用户（主要指以IP接入用户，比如二三层专线，数字机顶盒接入的用户）。

·**lan-access**：表示lan-access类型用户（主要指以太网接入用户，比如802.1X用户）。

·**pad**：X.25 PAD用户。

·**portal**：表示Portal用户。

·**ppp**：PPP用户。

·**ssh**：表示SSH用户。

·**[sslvpn**]{.ItemStepChar}：表示SSL VPN用户。

·**telnet**：表示Telnet用户。

·**terminal**：表示从Console口、AUX口、Asyn口登录的终端用户。不同型号的设备支持的接口类型不同，请以设备的实际情况为准。

【举例】

\# 添加名称为user1的设备管理类本地用户。

\<Sysname\> system-view

Sysname local-user user1 class manage

Sysname-luser-manage-user1

\# 添加名称为user2的网络接入类本地用户。

\<Sysname\> system-view

Sysname local-user user2 class network

Sysname-luser-network-user2

【相关命令】

·**display local-user**

·**service-type**

**AAA \-- 本地用户配置命令 \-- password**

------------------------------------------------------------------------

**[password**]命令用来设置本地用户的密码。

**[undo password**]命令用来删除本地用户的密码。

【命令】

非FIPS模式下：

**[password**[ [ { **cipher** \| **hash** \| **simple** } *password* ]]]

**[undo password**]

FIPS模式下：

**[password**]

【缺省情况】

非FIPS模式下：

不存在本地用户密码，即本地用户认证时无需输入密码，只要用户名有效且其它属性验证通过即可认证成功。

FIPS模式下：

不存在本地用户密码，但本地用户认证时不能成功。

【视图】

本地用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cipher**]：表示以密文方式设置用户密码。

**[hash**]：表示以哈希方式设置用户密码。

**[simple**]：表示以明文方式设置用户密码。

*[password*]：设置的明文密码或密文密码，区分大小写。非FIPS模式下，明文密码为1～63个字符的字符串；哈希密码为1～110个字符的字符串；密文密码为1～117个字符的字符串；FIPS模式下，明文密码为15～63个字符的字符串，密码元素的最少组合类型为4（必须包括数字、大写字母、小写字母以及特殊字符）。

【使用指导】

如果不指定任何参数，则表示以交互式方式设置本地用户密码，涵义与指定**simple**关键字相同。若不设置本地用户密码，则本地用户认证时无需输入密码，只要用户名有效且其它属性验证通过即可认证成功。因此为提高用户帐户的安全性，建议设置本地用户密码。

需要注意的是：

·对于设备管理类本地用户，可以使用交互式方式、明文或哈希方式设置用户密码，设置的明文密码将以哈希计算后生成的密文形式保存在配置文件中，设置的哈希密码将以设置的原始形式保存在配置文件中。FIPS模式下，只支持交互式方式设置本地用户密码，且必须设置本地用户密码，否则用户的本地认证不能成功。

·对于网络接入类本地用户，可以使用明文或密文方式设置用户密码，设置的明文密码将以加密后生成的密文形式保存在配置文件中，设置的密文密码将以设置的原始形式保存在配置文件中。

【举例】

\# 设置设备管理类本地用户user1的密码为明文123456TESTplat&!。

\<Sysname\> system-view

Sysname local-user user1 class manage

Sysname-luser-manage-user1 password simple 123456TESTplat&!

\# 以交互式方式设置设备管理类本地用户test的密码。

\<Sysname\> system-view

Sysname local-user test class manage

Sysname-luser-manage-test password

Password:

Confirm :

\# 设置网络接入类本地用户user2的密码为明文123456TESTuser&!。

\<Sysname\> system-view

Sysname local-user user1 class network

Sysname-luser-network-user1 password simple 123456TESTuser&!

【相关命令】

·**display local-user**

**AAA \-- 本地用户配置命令 \-- service-type**

------------------------------------------------------------------------

**[service-type**]命令用来设置用户可以使用的服务类型。

**[undo service-type**]命令用来删除用户可以使用的服务类型。

【命令】

非FIPS模式下：

**[service-type **[{ **advpn** \| **ftp** \| **ipoe** \| **lan-access** \| { **http** \| **https** \| **pad** \| **ssh** \| **telnet** \| **terminal** } \* \| **portal** \| **ppp** \| **sslvpn** }]]

**[undo service-type **[{ **dvpn** \| **ftp** \| **ipoe** \| **lan-access** \| { **http** \| **https** \| **pad** \| **ssh** \| **telnet** \| **terminal** } \* \| **portal** \| **ppp** \| **sslvpn** }]]

FIPS模式下：

**[service-type **[{ **dvpn** \| **ipoe** \| **lan-access** \| { **https** \| **pad** \| **ssh** \| **terminal** } \* \| **portal** \| **ppp** \| **sslvpn** }]]

**[undo service-type **[{ **dvpn** \| **ipoe** \| **lan-access** \| { **https** \| **pad** \| **ssh** \| **terminal** } \* \| **portal** \| **ppp** \| **sslvpn** }]]

【缺省情况】

系统不对用户授权任何服务，即用户不能使用任何服务。

【视图】

本地用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[advpn**]：指定用户可以使用ADVPN服务。该参数支持情况与设备的型号有关，请以设备的实际情况为准。

**[ftp**]：指定用户可以使用FTP服务。若授权FTP服务，缺省授权FTP用户可访问设备的根目录，授权目录可以通过**authorization-attribute work-directory**命令来修改。

**[http**]：指定用户可以使用HTTP服务。该参数支持情况与设备的型号有关，请以设备的实际情况为准。

**[https**]：指定用户可以使用HTTPS服务。该参数支持情况与设备的型号有关，请以设备的实际情况为准。

**[ipoe**]：指定用户可以使用IPoE服务。该参数支持情况与设备的型号有关，请以设备的实际情况为准。

**[lan-access**]：指定用户可以使用lan-access服务。主要指以太网接入，比如用户可以通过802.1X认证接入。该参数支持情况与设备的型号有关，请以设备的实际情况为准。

**[pad**]：指定用户可以使用X.25 PAD服务。该参数支持情况与设备的型号有关，请以设备的实际情况为准。

**[ssh**]：指定用户可以使用SSH服务。该参数支持情况与设备的型号有关，请以设备的实际情况为准。

**[telnet**]：指定用户可以使用Telnet服务。

**[terminal**]：指定用户可以使用terminal服务（即从Console口、AUX口、Asyn口登录）。不同型号的设备支持的用户登录接口类型不同，请以设备的实际情况为准。

**[portal**]：指定用户可以使用Portal服务。该参数支持情况与设备的型号有关，请以设备的实际情况为准。

**[ppp**]：指定用户可以使用PPP服务。该参数支持情况与设备的型号有关，请以设备的实际情况为准。

**[sslvpn**]：指定用户可以使用SSL VPN服务。该参数支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

可以通过多次执行本命令，设置用户可以使用多种服务类型。

【举例】

\# 指定设备管理类用户可以使用Telnet服务和FTP服务。

\<Sysname\> system-view

Sysname local-user user1 class manage

Sysname-luser-manage-user1 service-type telnet

Sysname-luser-manage-user1 service-type ftp

【相关命令】

·**display local-user**

**AAA \-- 本地用户配置命令 \-- state（Local user view）**

------------------------------------------------------------------------

**[state**]命令用来设置当前本地用户的状态。

**[undo state**]命令用来恢复缺省情况。

【命令】

**[state**[ { **active** \| **block** }]]

**[undo state**]

【缺省情况】

当一个本地用户被创建以后，其状态为**active**。

【视图】

本地用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[active**]：指定当前本地用户处于活动状态，即系统允许当前本地用户请求网络服务。

**[block**]：指定当前本地用户处于"阻塞"状态，即系统不允许当前本地用户请求网络服务。

【使用指导】

本命令仅对当前用户生效，不影响其它用户。

【举例】

\# 设置设备管理类本地用户user1处于"阻塞"状态。

\<Sysname\> system-view

Sysname local-user user1 class manage

Sysname-luser-manage-user1 state block

【相关命令】

·**display local-user**

**AAA \-- 本地用户配置命令 \-- user-group**

------------------------------------------------------------------------

![说明](AAA命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[user-group**]命令用来创建用户组，并进入其视图。

**[undo user-group**]命令用来删除指定的用户组。

【命令】

**[user-group** *group-name*]

**[undo user-group ***group-name*]

【缺省情况】

存在一个名称为system的用户组。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-name*]：用户组名称，为1～32个字符的字符串，不区分大小写。

【使用指导】

用户组是一个本地用户的集合，某些需要集中管理的属性可在用户组中统一配置和管理。目前，用户组中可配置的内容为本地用户的授权属性。

需要注意的是：

·当用户组中有本地用户时，不允许使用**undo user-group**删除该用户组。

·不能删除系统中存在的默认用户组system，但可以修改该用户组的配置。

【举例】

\# 创建名称为abc的用户组并进入其视图。

\<Sysname\> system-view

Sysname user-group abc

Sysname-ugroup-abc

【相关命令】

·**display user-group**

**AAA \-- RADIUS配置命令 \-- accounting-on enable**

------------------------------------------------------------------------

**[accounting-on enable**]命令用来配置accounting-on功能。

**[undo accounting-on enable**]命令用来恢复缺省情况。

【命令】

**[accounting-on enable **[[ **interval** *seconds* \| **send** *send-times* ] \*]]

**[undo accounting-on enable**]

【缺省情况】

accounting-on功能处于关闭状态。

【视图】

RADIUS方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interval** *seconds*]：指定accounting-on报文重发时间间隔，取值范围为1～15，单位为秒，缺省值为3。

**[send** *send-times*]：指定accounting-on报文的最大发送次数，取值范围为1～255，缺省值为50。

【使用指导】

在accounting-on功能处于使能的情况下，若设备重启，则设备会在重启之后发送accounting-on报文通知该方案所使用的RADIUS计费服务器，要求RADIUS服务器停止计费且强制该设备的用户下线。

需要注意的是：

·执行完该命令后，请执行**save**操作，以保证设备重启后accounting-on功能生效。

·在执行accounting-on功能的过程中，使用该命令重新设置的报文重发间隔时间以及报文最大发送次数会立即生效。

【举例】

\# 使能RADIUS认证方案radius1的accounting-on功能，并配置accounting-on报文重发时间间隔为5秒、accounting-on报文的最大发送次数为15次。

\<Sysname\> system-view

Sysname radius scheme radius1

Sysname-radius-radius1 accounting-on enable interval 5 send 15

【相关命令】

·**display radius scheme**

**AAA \-- RADIUS配置命令 \-- attribute 15 check-mode**

------------------------------------------------------------------------

**[attribute 15 check-mode**]命令用来配置RADIUS Attribute 15的检查方式。

**[undo attribute 15 check-mode**]命令用来恢复缺省情况。

【命令】

**[attribute 15 check-mode **[{ **loose** \| **strict** }]]

**[undo attribute 15 check-mode**]

【缺省情况】

RADIUS Attribute 15的检查方式为**strict**方式。

【视图】

RADIUS方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[loose**]：松散检查方式。设备使用RADIUS Attribute 15的标准属性值对用户业务类型进行检查，对于SSH、FTP、Terminal用户，在RADIUS服务器下发的Login-Service属性值为0（表示用户业务类型为Telnet）时才，这类用户才能够通过认证。

**[strict**]：严格检查方式。设备使用RADIUS Attribute 15的标准属性值以及扩展属性值对用户业务类型进行检查，对于SSH、FTP、Terminal用户，当RADIUS服务器下发的Login-Service属性值为对应的扩展取值时，这类用户才能够通过认证。

【使用指导】

由于某些RADIUS服务器不支持自定义的属性，无法下发扩展的Login-Service属性，若要使用这类RADIUS服务器对SSH、FTP、Terminal用户进行认证，建议设备上对RADIUS 15号属性值采用松散检查方式。

【举例】

\# 在RADIUS方案视图radius1下，配置RADIUS Attribute 15的检查方式为loose方式。

\<Sysname\> system-view

Sysname radius scheme radius1

Sysname-radius-radius1 attribute 15 check-mode loose

【相关命令】

·**display radius scheme**

**AAA \-- RADIUS配置命令 \-- attribute 25 car**

------------------------------------------------------------------------

**[attribute 25 car**]命令用来开启RADIUS Attribute 25的CAR参数解析功能。

**[undo attribute 25 car**]命令用来恢复缺省情况。

【命令】

**[attribute 25 car**]

**[undo attribute 25 car**]

【缺省情况】

RADIUS Attribute 25的CAR参数解析功能处于关闭状态。

【视图】

RADIUS方案视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

RADIUS的25号属性为class属性，该属性由RADIUS服务器下发给设备，但RFC中并未定义具体的用途，仅规定了设备需要将服务器下发的class属性再原封不动地携带在计费请求报文中发送给服务器即可，同时RFC并未要求设备必须对该属性进行解析。目前，某些RADIUS服务器利用class属性来对用户下发CAR参数，为了支持这种应用，可以通过本特性来控制设备是否将RADIUS 25号属性解析为CAR参数，解析出的CAR参数可被用来进行基于用户的流量监管控制。

【举例】

\# 在RADIUS方案视图test下，开启RADIUS Attribute 25的CAR参数解析功能。

\<Sysname\> system-view

Sysnameradius scheme test

Sysname-radius-test attribute 25 car

【相关命令】

·**display radius scheme**

**AAA \-- RADIUS配置命令 \-- attribute remanent-volume**

------------------------------------------------------------------------

**[attribute remanent-volume**]命令用来配置RADIUS Remanent-Volume属性的流量单位。

**[undo attribute remanent-volume**]命令用来恢复缺省情况。

【命令】

**[attribute remanent-volume unit **[{ **byte** \| **giga-byte** \| **kilo-byte** \| **mega-byte** }]]

**[undo attribute remanent-volume unit**]

【缺省情况】

Remanent-Volume属性的流量单位是千字节。

【视图】

RADIUS方案视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[byte**]：表示流量单位为字节。

**[giga-byte**]：表示流量单位为千兆字节。

**[kilo-byte**]：表示流量单位为千字节。

**[mega-byte**]：表示流量单位为兆字节。

【使用指导】

Remanent-Volume属性为H3C自定义RADIUS属性，携带在RADIUS服务器发送给接入设备的认证响应或实时计费响应报文中，用于向接入设备通知在线用户的剩余流量值。设备管理员通过本命令设置的流量单位应与RADIUS服务器上统计用户流量的单位保持一致，否则设备无法正确使用Remanent-Volume属性值对用户进行计费。

【举例】

\# 在RADIUS方案radius1中，设置RADIUS服务器下发的Remanent-Volume属性的流量单位为千字节。

\<Sysname\> system-view

Sysname radius scheme radius1

Sysname-radius-radius1 attribute remanent-volume unit kilo-byte

【相关命令】

·**display radius scheme**

**AAA \-- RADIUS配置命令 \-- client**

------------------------------------------------------------------------

**[client**]命令用来指定RADIUS DAE客户端。

**[undo client**]命令用来删除指定的RADIUS DAE客户端。

【命令】

**[client **[{ **ip** *ipv4-address* \| **ipv6** *ipv6-address* } [ **key** { **cipher** \| **simple** } *string* \| **vpn-instance** *vpn-instance-name* ] \*]]

**[undo client **[{ **ip** *ipv4-address* \| **ipv6** *ipv6-address* } [ **vpn-instance** *vpn-instance-name* ]]]

【缺省情况】

未指定RADIUS DAE客户端。

【视图】

RADIUS DAE服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip*** ipv4-address*]：RADIUS DAE客户端IPv4地址。

**[ipv6*** ipv6-address*]：RADIUS DAE客户端IPv6地址。

**[key **[{ **cipher** \| **simple** } *string*]]：与RADIUS DAE客户端交互DAE报文时使用的共享密钥。此共享密钥的设置必须与RADIUS DAE客户端的共享密钥设置保持一致。如果此处未指定本参数，则对应的RADIUS DAE客户端上也必须未指定。

·**cipher ***string*：以密文方式设置共享密钥。非FIPS模式下，*string*为1～117个字符的密文字符串，区分大小写；FIPS模式下，*string*为15～117个字符的密文字符串，区分大小写。

·**simple ***string*：以明文方式设置共享密钥。非FIPS模式下，*string*为1～64个字符的明文字符串，区分大小写；FIPS模式下，*string*为15～64个字符的明文字符串，区分大小写，密钥元素的最少组合类型为4（必须包括数字、大写字母、小写字母以及特殊字符）。

**[vpn-instance** *vpn-instance-name*]：RADIUS DAE客户端所属的VPN。vpn-instance-name表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示RADIUS DAE客户端位于公网中。该参数支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

使能RADIUS DAE服务之后，设备会监听并处理指定的RADIUS DAE客户端发起的DAE请求消息（用于动态授权修改或断开连接），并向其发送应答消息。对于非指定的RADIUS DAE客户端的DAE报文进行丢弃处理。

可通过多次执行本命令指定多个RADIUS DAE客户端。

【举例】

\# 设置RADIUS DAE客户端的IP地址为10.110.1.2，与RADIUS DAE客户端交互DAE报文时使用的共享密钥为明文123456，MPLS L3VPN实例名称为abc。

\<Sysname\> system-view

Sysnameradius dynamic-author server

Sysname-radius-da-serverclient ip 10.110.1.2 key simple 123456 vpn-instance abc

【相关命令】

·**radius dynamic-author server**

·**port**

**AAA \-- RADIUS配置命令 \-- data-flow-format (RADIUS scheme view)**

------------------------------------------------------------------------

**[data-flow-format**]命令用来配置发送到RADIUS服务器的数据流及数据包的单位。

**[undo data-flow-format**]命令用来恢复缺省情况。

【命令】

**[data-flow-format **[{ **data** { **byte** \| **giga-byte** \| **kilo-byte** \| **mega-byte** } \| **packet** { **giga-packet** \| **kilo-packet** \| **mega-packet** \| **one-packet** } } \*]]

**[undo data-flow-format **[{ **data** \| **packet** }]]

【缺省情况】

数据流的单位为**byte**，数据包的单位为**one-packet**。

【视图】

RADIUS方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[data**]：设置数据流的单位。

·**byte**：数据流的单位为字节。

·**giga-byte**：数据流的单位千兆字节。

·**kilo-byte**：数据流的单位为千字节。

·**mega-byte**：数据流的单位为兆字节。

**[packet**]：设置数据包的单位。

·**giga-packet**：数据包的单位为千兆包。

·**kilo-packet**：数据包的单位为千包。

·**mega-packet**：数据包的单位为兆包。

·**one-packet**：数据包的单位为包。

【使用指导】

设备上配置的发送给RADIUS服务器的数据流单位及数据包单位应与RADUIS服务器上的流量统计单位保持一致，否则无法正确计费。

【举例】

\# 在RADIUS方案radius1中，设置发往RADIUS服务器的数据流单位为千字节、数据包单位为千包。

\<Sysname\> system-view

Sysname radius scheme radius1

Sysname-radius-radius1 data-flow-format data kilo-byte packet kilo-packet

【相关命令】

·**display radius scheme**

**AAA \-- RADIUS配置命令 \-- display radius scheme**

------------------------------------------------------------------------

**[display radius scheme**]命令用来显示所有或指定RADIUS方案的配置信息。

【命令】

**[display radius scheme** [ *radius-scheme-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[radius-scheme-name*]：显示指定的RADIUS方案的配置信息。*radius-scheme-name*为RADIUS方案名，为1～32个字符的字符串，不区分大小写。

【使用指导】

如果不指定RADIUS方案名，则显示所有RADIUS方案的配置信息。

【举例】

\# 显示所有RADIUS方案的配置信息。

\<Sysname\> display radius scheme

Total 1 RADIUS schemes

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

RADIUS scheme name  : radius1

  Index : 0

  Primary authentication server:

    IP   : 2.2.2.2                                  Port: 1812

    VPN  : vpn1

    State: Active

    Test profile: 132

      Probe username: test

      Probe interval: 60 minutes

  Primary accounting server:

    IP : 1.1.1.1                                    Port: 1813

    VPN : Not configured

    State: Active

  Second authentication server:

    IP: Not configured                             Port: 1812

    VPN : Not configured

    State: Block

    Test profile: Not configured

  Second accounting server:

    IP : 3.3.3.3                                    Port: 1813

    State: Block (Mandatory)

    VPN : Not configured

  Security policy server:

    Server: 0     IP: 2.2.2.2         VPN: Not configured

    Server: 1     IP: 3.3.3.3         VPN: 2

  Accounting-On function                     : Enabled

    retransmission times                     : 5

    retransmission interval(seconds)         : 2

  Timeout Interval(seconds)                  : 3

  Retransmission Times                       : 3

  Retransmission Times for Accounting Update : 5

  Server Quiet Period(minutes)               : 5

  Realtime Accounting Interval(minutes)      : 22 

  NAS IP Address                             : 1.1.1.1

  VPN                                        : Not configured

  User Name Format                           : with-domain

  Data flow unit                             : Megabyte

  Packet unit                                : One

  Attribute 15 check-mode                    : Strict

  Attribute 25                               : CAR

  Attribute Remanent-Volume unit             : Mega

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

表1-4 display radius scheme命令显示信息描述表

字段

描述

Total 1 RADIUS schemes.

共计1个RADIUS方案

RADIUS scheme name

RADIUS方案的名称

Index

RADIUS方案的索引号

Primary authentication server

主RADIUS认证服务器

Primary accounting server

主RADIUS计费服务器

Second authentication server

从RADIUS认证服务器

Second accounting server

从RADIUS计费服务器

IP

RADIUS认证/计费服务器IP地址

未配置时，显示为Not configured

Port

RADIUS认证/计费服务器接入端口号

未配置时，显示缺省值

State

RADIUS认证/计费服务器目前状态

·Active：激活状态

·Block：自动转换的静默状态

·Block(Mandatory)：手工配置的静默状态

VPN

RADIUS认证/计费服务器所在的VPN

未配置时，显示为Not configured

Security policy server

安全策略服务器

Server: *n*

安全策略服务器编号

IP

安全策略服务器的IP地址

VPN

安全策略服务器所在的VPN

未配置时，显示为Not configured

Test profile

探测服务器状态使用的模版名称

Probe username

探测服务器状态使用的用户名

Probe interval

探测服务器状态的周期（单位为分钟）

Accounting-On function

accounting-on功能的使能情况

accounting-on功能的显示信息的支持情况与设备的型号有关，请以设备的实际情况为准

retransmission times

accounting-on报文的发送尝试次数

retransmission interval(seconds)

accounting-on报文的重发间隔（单位为秒）

Timeout Interval(seconds)

RADIUS服务器超时时间（单位为秒）

Retransmission Times

发送RADIUS报文的最大尝试次数

Retransmission Times for Accounting Update

实时计费更新报文的最大尝试次数

Server Quiet Period(minutes)

RADIUS服务器恢复激活状态的时间（单位为分钟）

Realtime Accounting Interval(minutes)

实时计费更新报文的发送间隔（单位为分钟）

NAS IP Address

发送RADIUS报文的源IP地址

VPN

RADIUS方案所属的VPN名称

未配置时，显示为Not configured

User Name Format

发送给RADIUS服务器的用户名格式

·with-domain：携带域名

·without-domain：不携带域名

·keep-original：与用户输入保持一致

Data flow unit

数据流的单位

Packet unit

数据包的单位

Attribute 15 check-mode

对RADIUS  Attribute 15的检查方式，包括以下两种取值：

·Strict：表示使用RADIUS标准属性值和私有扩展的属性值进行检查

·Loose：表示使用RADIUS标准属性值进行检查

Attribute 25

对RADIUS Attribute 25的处理，包括以下两种取值：

·Standard：表示不对RADIUS Attribute 25进行解析

·CAR：表示将RADIUS 25号属性解析为CAR参数

Attribute Remanent-Volume unit

RADIUS Remanent-Volume属性的流量单位

**AAA \-- RADIUS配置命令 \-- display radius statistics**

------------------------------------------------------------------------

**[display radius statistics**]命令用来显示RADIUS报文的统计信息。

【命令】

**[display radius statistics**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示RADIUS报文的统计信息。

\<Sysname\> display radius statistics

                                 Auth.         Acct.       SessCtrl.

          Request Packet:          0             0             0

            Retry Packet:          0             0             -

          Timeout Packet:          0             0             -

        Access Challenge:          0             -             -

           Account Start:          -             0             -

          Account Update:          -             0             -

            Account Stop:          -             0             -

       Terminate Request:          -             -             0

              Set Policy:          -             -             0

    Packet With Response:          0             0             0

 Packet Without Response:          0             0             -

          Access Rejects:          0             -             -

          Dropped Packet:          0             0             0

          Check Failures:          0             0             0

表1-5 display radius statistics命令显示信息描述表

字段

描述

Auth.

认证报文

Acct.

计费报文

SessCtrl.

Session-control报文

Request Packet

发送的请求报文总数

Retry Packet

重传的请求报文总数

Timeout Packet

超时的请求报文总数

Access Challenge

Access challenge报文数

Account Start

计费开始报文的数目

Account Update

计费更新报文的数目

Account Stop

计费结束报文的数目

Terminate Request

服务器强制下线报文的数目

Set Policy

更新用户授权信息报文的数目

Packet With Response

有回应信息的报文数

Packet Without Response

无回应信息的报文数

Access Rejects

认证拒绝报文的数目

Dropped Packet

丢弃的报文数

Check Failures

报文校验错误的报文数目

【相关命令】

·**reset radius statistics**

**AAA \-- RADIUS配置命令 \-- key (RADIUS scheme view)**

------------------------------------------------------------------------

**[key**]命令用来配置RADIUS报文的共享密钥。

**[undo key**]命令用来删除RADIUS报文的共享密钥。

【命令】

**[key**[ { **accounting** \| **authentication** } { **cipher** \| **simple** } *string*]]

**[undo key**[ { **accounting** \| **authentication** }]]

【缺省情况】

无共享密钥。

【视图】

RADIUS方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[accounting**]：指定RADIUS计费报文的共享密钥。

**[authentication**]：指定RADIUS认证报文的共享密钥。

**[cipher**]：表示以密文方式设置共享密钥。

**[simple**]：表示以明文方式设置共享密钥。

*[string*]：设置的明文密钥或密文密钥，区分大小写。非FIPS模式下，明文密钥为1～64个字符的字符串；密文密钥为1～117个字符的字符串；FIPS模式下，明文密钥为15～64个字符的字符串，密钥元素的最少组合类型为4（必须包括数字、大写字母、小写字母以及特殊字符）；密文密钥为15～117个字符的字符串。

【使用指导】

需要注意的是：

·设备优先采用配置RADIUS认证/计费服务器时指定的报文共享密钥，本配置中指定的报文共享密钥仅在配置RADIUS认证/计费服务器时未指定相应密钥的情况下使用。

·必须保证设备上设置的共享密钥与RADIUS服务器上的完全一致。

·以明文或密文方式设置的共享密钥，均以密文的方式保存在配置文件中。

【举例】

\# 将RADIUS方案radius1的计费报文的共享密钥设置为明文ok。

\<Sysname\> system-view

Sysname radius scheme radius1

Sysname-radius-radius1 key accounting simple ok

【相关命令】

·**display radius scheme**

**AAA \-- RADIUS配置命令 \-- nas-ip (RADIUS scheme view)**

------------------------------------------------------------------------

**[nas-ip**]命令用来设置设备发送RADIUS报文使用的源IP地址。

**[undo nas-ip**]命令用来删除指定的源IP地址。

【命令】

**[nas-ip **]*[ipv6-address* }

**[undo nas-ip **] **ipv6** ]

【缺省情况】

使用系统视图下由命令**radius nas-ip**指定的源地址，若系统视图下未指定源地址，则使用发送RADIUS报文的接口的主IP地址。

【视图】

RADIUS方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv4-address*]：指定的源IPv4地址，应该为本机的地址，禁止配置全0地址、全1地址、D类地址、E类地址和环回地址。

**[ipv6** *ipv6-address*]：指定的源IPv6地址，应该为本机的地址，必须是单播地址，不能为环回地址与本地链路地址。

【使用指导】

RADIUS服务器上通过IP地址来标识接入设备，并根据收到的RADIUS报文的源IP地址是否与服务器所管理的接入设备的IP地址匹配，来决定是否处理来自该接入设备的认证或计费请求。因此，为保证认证和计费报文可被服务器正常接收并处理，接入设备上发送RADIUS报文使用的源地址必须与RADIUS服务器上指定的接入设备的IP地址保持一致。

需要注意的是：

·RADIUS方案视图下的命令**nas-ip**只对本RADIUS方案有效，系统视图下的命令**radius nas-ip**对所有RADIUS方案有效。RADIUS方案视图下的设置具有更高的优先级。

·指定发送RADIUS报文使用的源地址，可以避免物理接口故障时从服务器返回的报文不可达。一般推荐使用Loopback接口地址。

·如果重复执行此命令，新配置的IPv4/IPv6源地址会覆盖原有的IPv4/IPv6源地址。

【举例】

\# 配置设备发送RADIUS报文使用的源IP地址为10.1.1.1。

\<Sysname\> system-view

Sysname radius scheme radius1

Sysname-radius-radius1 nas-ip 10.1.1.1

【相关命令】

·**display radius scheme**

·**radius nas-ip**

**AAA \-- RADIUS配置命令 \-- port**

------------------------------------------------------------------------

**[port**]命令用来指定RADIUS DAE服务端口。

**[undo port**]命令用来恢复缺省情况。

【命令】

**[port ***port-number*]

**[undo port**]

【缺省情况】

RADIUS DAE服务端口为3799。

【视图】

RADIUS DAE服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-number*]：DAE服务器接收DAE请求消息的UDP端口，取值范围为1～65535。

【使用指导】

通常RADIUS DAE客户端使用UDP 3799作为发送DAE报文的目的端口，因此不需要修改设备上的RADIUS DAE服务端口。若要修改，必须保证设备上的RADIUS DAE服务端口与RADIUS DAE客户端发送DAE报文的目的UDP端口一致。

【举例】

\# 使能RADIUS DAE服务后，指定DAE服务端口为3790。

\<Sysname\> system-view

Sysname radius dynamic-author server

Sysname-radius-da-server port 3790

【相关命令】

·**client**

·**radius dynamic-author server**

**AAA \-- RADIUS配置命令 \-- primary accounting (RADIUS scheme view)**

------------------------------------------------------------------------

**[primary accounting**]命令用来配置主RADIUS计费服务器。

**[undo primary accounting**]命令用来删除设置的主RADIUS计费服务器。

【命令】

**[primary accounting ***ipv4-address*[\| **ipv6** *ipv6-address* } [ *port-number* *\|* **key** { **cipher** \| **simple** } *string* \| **vpn-instance** *vpn-instance-name* ] \*]

**[undo primary accounting**]

【缺省情况】]

未配置主RADIUS计费服务器。

【视图】

RADIUS方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv4-address*]：主RADIUS计费服务器的IPv4地址。

**[ipv6*** ipv6-address*]：主RADIUS计费服务器的IPv6地址。

*[port-number*]：主RADIUS计费服务器的UDP端口号，缺省为1813，取值范围为1～65535。此端口号必须与服务器提供计费服务的端口号保持一致。

**[key**[ { **cipher** \| **simple** } *string*]]：与主RADIUS计费服务器交互的计费报文的共享密钥。此共享密钥必须与服务器上配置的共享密钥保持一致。

·**cipher ***string*：以密文方式设置共享密钥。非FIPS模式下，*string*为1～117个字符的密文字符串，区分大小写；FIPS模式下，*string*为15～117个字符的密文字符串，区分大小写。

·**simple ***string*：以明文方式设置共享密钥。非FIPS模式下，*string*为1～64个字符的明文字符串，区分大小写；FIPS模式下，*string*为15～64个字符的明文字符串，区分大小写，密钥元素的最少组合类型为4（必须包括数字、大写字母、小写字母以及特殊字符）。

**[vpn-instance ***vpn-instance-name*]：主RADIUS计费服务器所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示主RADIUS计费服务器位于公网中。该参数支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

在同一个方案中指定的主计费服务器和从计费服务器的IP地址、端口号和VPN参数不能完全相同。

设备与主计费服务器通信时优先使用本命令设置的共享密钥，如果此处未设置，则使用**key** **accounting**命令设置的共享密钥。

若服务器位于MPLS VPN私网中，为保证RADIUS报文被发送到指定的私网服务器，必须指定服务器所属的VPN实例名称。本命令指定的服务器所属的VPN实例比RADIUS方案所属的VPN实例具有更高的优先级。

如果计费开始请求过程中使用本命令修改或删除了正在使用的主计费服务器，则设备在与当前服务器通信超时后，将会重新按照优先级顺序开始依次查找状态为**active**的服务器进行通信。

如果在线用户正在使用的计费服务器被删除，则设备将无法发送用户的实时计费请求和停止计费请求，且停止计费报文不会被缓存到本地，这将造成对用户计费的不准确。

以明文或密文方式设置的共享密钥，均以密文的方式保存在配置文件中。

【举例】

\# 设置RADIUS方案radius1的主计费服务器的IP地址为10.110.1.2，使用UDP端口1813提供RADIUS计费服务，计费报文的共享密钥为明文123456TESTacct&!。

\<Sysname\> system-view

Sysname radius scheme radius1

Sysname-radius-radius1 primary accounting 10.110.1.2 1813 key simple 123456TESTacct&!

【相关命令】

·**display radius scheme**

·**key **(RADIUS scheme view)

·**secondary accounting**

·**vpn-instance **(RADIUS scheme view)

**AAA \-- RADIUS配置命令 \-- primary authentication (RADIUS scheme view)**

------------------------------------------------------------------------

**[primary authentication**]命令用来配置主RADIUS认证服务器。

**[undo primary authentication**]命令用来删除设置的主RADIUS认证服务器。

【命令】

**[primary authentication ***ipv4-address*[\| **ipv6** *ipv6-address* } [ *port-number* \| **key** { **cipher** \| **simple** } *string* \| **test-profile** *profile-name* \| **vpn-instance** *vpn-instance-name* ] \*]

**[undo primary authentication**]

【缺省情况】]

未配置RADIUS主认证服务器。

【视图】

RADIUS方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv4-address*]：主RADIUS认证服务器的IPv4地址。

**[ipv6*** ipv6-address*]：主RADIUS认证服务器的IPv6地址。

*[port-number*]：主RADIUS认证服务器的UDP端口号，取值范围为1～65535,缺省为1812。此端口号必须与服务器提供认证服务的端口号保持一致。

**[key**[ { **cipher** \| **simple** } *string*]]：与主RADIUS认证服务器交互的认证报文的共享密钥。此共享密钥必须与服务器上配置的共享密钥保持一致。

·**cipher ***string*：以密文方式设置共享密钥。非FIPS模式下，*string*为1～117个字符的密文字符串，区分大小写； FIPS模式下，*string*为15～117个字符的密文字符串，区分大小写。

·**simple ***string*：以明文方式设置共享密钥。非FIPS模式下，*string*为1～64个字符的明文字符串，区分大小写；FIPS模式下，*string*为15～64个字符的明文字符串，区分大小写，密钥元素的最少组合类型为4（必须包括数字、大写字母、小写字母以及特殊字符）。

**[test-profile*** profile-name*]：RADIUS服务器探测模版名称，为1～31个字符的字符串，区分大小写。

**[vpn-instance ***vpn-instance-name*]：主RADIUS认证服务器所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示主RADIUS认证服务器位于公网中。该参数支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

在同一个方案中指定的主认证服务器和从认证服务器的IP地址、端口号和VPN参数不能完全相同。

设备与主认证服务器通信时优先使用本命令设置的共享密钥，如果本命令中未设置，则使用**key** **authenticaiton**命令设置的共享密钥。

RADIUS认证服务器引用了存在的服务器探测模版后，将会触发对该服务器的探测功能。RADIUS服务器探测功能是指，设备周期性发送探测报文探测RADIUS服务器是否可达：如果服务器不可达，则置服务器状态为**block**，如果服务器可达，则置服务器状态为**active**。

若服务器位于MPLS VPN私网中，为保证RADIUS报文被发送到指定的私网服务器，必须指定服务器所属的VPN实例名称。本命令指定的服务器所属的VPN比RADIUS方案所属的VPN优先级高。

如果在认证过程中使用本命令修改或删除了正在使用的主认证服务器，则设备在与当前服务器通信超时后，将会重新按照优先级顺序开始依次查找状态为**active**的服务器进行通信。

以明文或密文方式设置的共享密钥，均以密文的方式保存在配置文件中。

【举例】

\# 设置RADIUS方案radius1的主认证服务器的IP地址为10.110.1.1，使用UDP端口1812提供RADIUS认证/授权服务，认证报文的共享密钥为明文123456TESTauth&!。

\<Sysname\> system-view

Sysname radius scheme radius1

Sysname-radius-radius1 primary authentication 10.110.1.1 1812 key simple 123456TESTauth&!

【相关命令】

·**display radius scheme**

·**key **(RADIUS scheme view)

·**radius-server test-profile**

·**secondary authentication**

·**vpn-instance **(RADIUS scheme view)

**AAA \-- RADIUS配置命令 \-- radius-server test-profile**

------------------------------------------------------------------------

**[radius-server test-profile**]命令用来配置RADIUS服务器探测模版。

**[undo radius-server test-profile**]命令用来删除指定的RADIUS服务器探测模版。

【命令】

**[radius-server test-profile** *profile-name* **username** *name* [ **interval** *interval* ]]

**[undo radius-server test-profile ***profile-name*]

【缺省情况】

无RADIUS服务器探测模版。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[profile-name*]：探测模版名称，为1～31个字符的字符串，区分大小写

**[username ***name*]：探测报文中的用户名，为1～253个字符的字符串，区分大小写。

**[interval** *interval*]：发送探测报文的周期，取值范围为1～3600，单位为分钟，缺省值为60。

【使用指导】

RADIUS服务器探测模版用于配置探测用户名以及探测周期，并且可以被RADIUS方案视图下的RADIUS认证/授权服务器配置引用。只有一个RADIUS服务器配置中成功引用了一个已经存在的服务器探测模版，且该服务器状态为**active**时，设备才会启动对该RADIUS服务器的探测功能。

RADIUS服务器探测报文是一种模拟的认证请求报文，服务器探测模版中配置的探测用户名即为该探测报文中的认证用户名。设备会在配置的探测周期内选择随机时间点向引用了服务器探测模版的RADIUS服务器发送探测报文，且每次收到的探测应答消息仅能说明当前探测周期内该RADIUS服务器可达。如果服务器不可达，则置服务器状态为**block**，如果服务器可达，则置服务器状态为**active**。

服务器探测功能启动后，周期性的探测过程会一直执行，直到相关的配置发生变化才会停止。这些配置包括：删除该RADIUS服务器配置、取消对服务器探测模版的引用、删除对应的服务器探测模版、将该RADIUS服务器的状态手工置为**block**、删除当前RADIUS方案。

系统支持配置多个RADIUS服务器探测模版。

需要注意的是：

·RADIUS方案视图下的RADIUS服务器配置成功引用了某探测模板后，若被引用的探测模板不存在，则暂不启动探测功能。之后，当该探测模板被成功配置时，针对该服务器的探测过程将会立即开始。

·一个RADIUS服务器探测模版可被多个RADIUS方案引用，用于对不同的RADIUS服务器进行探测。

·删除一个RADIUS服务器探测模版时，引用该探测模版的所有RADIUS方案中的RADIUS服务器的探测功能也会被关闭。

【举例】

\# 配置RADIUS服务器探测模版abc，探测报文中携带的用户名为admin，探测报文的发送间隔为10分钟。

\<Sysname\> system-view

Sysname radius-server test-profile abc username admin interval 10

【相关命令】

·**primary authentication** (RADIUS scheme view)

·**secondary authentication** (RADIUS scheme view)

**AAA \-- RADIUS配置命令 \-- radius dynamic-author server**

------------------------------------------------------------------------

**[radius dynamic-author server**]命令用来使能RADIUS DAE服务，并进入RADIUS DAE服务器视图。

**[undo radius dynamic-author server**]用来恢复缺省情况。

【命令】

**[radius dynamic-author server**]

**[undo radius dynamic-author server**]

【缺省情况】

RADIUS DAE服务处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

使能RADIUS DAE服务后，设备将默认开启UDP端口3799，并能够接收指定的RADIUS DAE客户端发送的DAE请求消息，然后根据请求消息进行用户授权信息的修改或断开用户连接请求。

【举例】

\# 使能RADIUS DAE服务，并进入RADIUS DAE服务器视图。

\<Sysname\> system-view

Sysname radius dynamic-author server

Sysname -radius-da-server

【相关命令】

·**client**

·**port**

**AAA \-- RADIUS配置命令 \-- radius dscp**

------------------------------------------------------------------------

**[radius dscp**]命令用来配置RADIUS协议报文的DSCP优先级。

**[undo radius dscp**]命令用来恢复缺省情况。

【命令】

**[radius** [ **ipv6**  **dscp** *dscp-value*]]

**[undo radius** [ **ipv6**  **dscp**]]

【缺省情况】

RADIUS报文的DSCP优先级为0。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv6**]：表示设置IPv6 RADIUS报文。若不指定该参数，则表示设置IPv4 RADIUS报文。

*[dscp-value*]：RADIUS报文的DSCP优先级，取值范围为0～63。取值越大，优先级越高。

【使用指导】

DSCP携带在IP报文中的ToS字段，用来体现报文自身的优先等级，决定报文传输的优先程度。通过本命令可以指定设备发送的RADIUS报文携带的DSCP优先级的取值。

【举例】

\# 配置IPv4 RADIUS报文的DSCP优先级为10。

\<Sysname\> system-view

Sysname radius dscp 10

**AAA \-- RADIUS配置命令 \-- radius nas-ip**

------------------------------------------------------------------------

**[radius nas-ip**]命令用来指定设备发送RADIUS报文使用的源地址。

**[undo radius nas-ip**]命令用来删除指定的源地址。

【命令】

**[radius nas-ip**[ { *ipv4-address* \| **ipv6** *ipv6-address* } [ **vpn-instance** *vpn-instance-name* ]]]

**[undo radius nas-ip** { *ipv4-address* \| **ipv6** *ipv6-address* }  **vpn-instance** *vpn-instance-name* ]

【缺省情况】

不指定源地址，即以发送报文的接口的主IP地址作为源地址。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv4-address*]：指定的源IPv4地址，应该为本机的地址，不能为全0地址、全1地址、D类地址、E类地址和环回地址。

**[ipv6** *ipv6-address*]：指定的源IPv6地址，应该为本机的地址，必须是单播地址，不能为环回地址与本地链路地址。

**[vpn-instance ***vpn-instance-name*]：指定私网源IPv4/IPv6地址所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。若不指定该参数，则表示配置的是公网源地址。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

RADIUS服务器上通过IP地址来标识接入设备，并根据收到的RADIUS报文的源IP地址是否与服务器所管理的接入设备的IP地址匹配，来决定是否处理来自该接入设备的认证或计费请求。指定发送RADIUS报文使用的源地址，可以避免物理接口故障时从服务器返回的报文不可达。

需要注意的是：

·系统最多允许指定16个源地址，其中，最多包括一个IPv4公网源地址和一个IPv6公网源地址，其余为IPv4或IPv6私网源地址。新配置的IPv4/IPv6公网源地址会覆盖原有的IPv4/IPv6公网源地址。而且，对于同一个VPN，最多只能指定一个IPv4私网源地址和一个IPv6私网源地址。

·为保证认证和计费报文可被服务器正常接收并处理，接入设备上发送RADIUS报文使用的源地址必须与RADIUS服务器上指定的接入设备的IP地址保持一致。

·RADIUS方案视图下的命令**nas-ip**只对本RADIUS方案有效，系统视图下的命令**radius nas-ip**对所有RADIUS方案有效。RADIUS方案视图下的设置具有更高的优先级。

【举例】

\# 配置设备发送RADIUS报文使用的源地址为129.10.10.1。

\<Sysname\> system-view

Sysname radius nas-ip 129.10.10.1

【相关命令】

·**nas-ip **(RADIUS scheme view)

**AAA \-- RADIUS配置命令 \-- radius scheme**

------------------------------------------------------------------------

**[radius scheme**]命令用来创建RADIUS方案，并进入RADIUS方案视图。

**[undo radius scheme**]命令用来删除指定的RADIUS方案。

【命令】

**[radius scheme**] *radius-scheme-name*

**[undo radius scheme**] *radius-scheme-name*

【缺省情况】

不存在任何RADIUS方案。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[radius-scheme-name*]：RADIUS方案名，为1～32个字符的字符串，不区分大小写。

【使用指导】

一个RADIUS方案可以同时被多个ISP域引用。

系统最多支持配置16个RADIUS方案。

【举例】

\# 创建名为radius1的RADIUS方案并进入其视图。

\<Sysname\> system-view

Sysname radius scheme radius1

Sysname-radius-radius1

【相关命令】

·**display radius scheme**

**AAA \-- RADIUS配置命令 \-- radius session-control enable**

------------------------------------------------------------------------

**[radius session-control enable**]命令用来使能RADIUS session control功能，即打开知名UDP端口1812。

**[undo radius session-control enable**]命令恢复缺省情况。

【命令】

**[radius session-control enable**]

**[undo radius session-control enable**]

【缺省情况】

RADIUS session control功能处于关闭状态，即知名UDP端口1812处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【使用指导】

H3C的IMC RADIUS服务器使用session control报文向设备发送授权信息的动态修改请求以及断开连接请求。使能RADIUS session control功能后，设备会打开知名UDP端口1812来监听并接收RADIUS服务器发送的session control报文。

需要注意的是，该功能仅能和H3C IMC的RADIUS服务器配合使用。

【举例】

\# 使能RADIUS session control功能。

\<Sysname\> system-view

Sysname radius session-control enable

**AAA \-- RADIUS配置命令 \-- reset radius statistics**

------------------------------------------------------------------------

**[reset radius statistics**]命令用来清除RADIUS协议的统计信息。

【命令】

**[reset radius statistics**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 清除RADIUS协议的统计信息。

\<Sysname\> reset radius statistics

【相关命令】

·**display radius statistics**

**AAA \-- RADIUS配置命令 \-- retry**

------------------------------------------------------------------------

**[retry**]命令用来设置发送RADIUS报文的最大尝试次数，即如果某RADIUS服务器在指定的时间内未响应或未及时响应设备发送的RAIUDS报文，设备尝试向该服务器发送RADIUS报文的最大次数。

**[undo retry**]命令用来恢复缺省情况。

【命令】

**[retry** *retry-times*]

**[undo retry**]

【缺省情况】

发送RADIUS报文的最大尝试次数为3次。

【视图】

RADIUS方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[retry-times*]：发送RAIUDS报文的最大尝试次数，取值范围为1～20。

【使用指导】

由于RADIUS协议采用UDP报文来承载数据，因此其通信过程是不可靠的。如果设备在应答超时定时器规定的时长内（由**timer response-timeout**命令配置）没有收到RADIUS服务器的响应，则设备有必要向RADIUS服务器重传RADIUS请求报文。如果累计的传送次数已达到最大传送次数而RADIUS服务器仍旧没有响应，则设备将认为本次请求失败。

发送RADIUS报文的最大尝试次数与RADIUS服务器应答超时时间的乘积不能超过300秒。

【举例】

\# 设置在RADIUS方案radius1下，发送RAIUDS报文的最大尝试次数为5次。

\<Sysname\> system-view

Sysname radius scheme radius1

Sysname-radius-radius1 retry 5

【相关命令】

·**radius scheme**

·**timer response-timeout**

**AAA \-- RADIUS配置命令 \-- retry realtime-accounting**

------------------------------------------------------------------------

**[retry realtime-accounting**]命令用来设置允许发起实时计费请求的最大尝试次数。

**[undo** **retry realtime-accounting**]命令用来恢复缺省情况。

【命令】

**[retry realtime-accounting** *retry-times*]

**[undo retry realtime-accounting**]

【缺省情况】

设备最多允许5次实时计费请求无响应，之后将切断用户连接。

【视图】

RADIUS方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[retry-times*]：允许发起实时计费请求的最大尝试次数，取值范围为1～255。

【使用指导】

RADIUS服务器通常通过连接超时定时器来判断用户是否在线。如果RADIUS服务器在连接超时时间之内一直收不到设备传来的实时计费报文，它会认为线路或设备故障并停止对用户记帐。为了配合RADIUS服务器的这种特性，有必要在不可预见的故障条件下，尽量保持设备端与RADIUS服务器同步切断用户连接。设备提供对实时计费请求连续无响应次数限制的设置，保证设备尽可能得在RADIUS服务器的连接超时时长内向RADIUS服务器尝试发出实时计费请求。如果设备没有收到响应的次数超过了设定的限度，才会切断用户连接。

假设RADIUS服务器的应答超时时长（**timer response-timeout**命令设置）为3秒，发送RADIUS报文的最大尝试次数（**retry**命令设置）为3，设备的实时计费间隔（**timer realtime-accounting**命令设置）为12分钟，设备允许实时计费无响应的最大次数为5次（**retry realtime-accounting**命令设置），则其含义为：设备每隔12分钟发起一次计费请求，如果3秒钟得不到回应就重新发起一次请求，如果3次发送都没有得到回应就认为该次实时计费失败，然后每隔12分钟再发送一次，5次均失败以后，设备将切断用户连接。

【举例】

\# 设置RADIUS方案radius1最多允许10次实时计费请求无响应。

\<Sysname\> system-view

Sysname radius scheme radius1

Sysname-radius-radius1 retry realtime-accounting 10

【相关命令】

·**retry**

·**timer realtime-accounting**

·**timer response-timeout**

**AAA \-- RADIUS配置命令 \-- secondary accounting (RADIUS scheme view)**

------------------------------------------------------------------------

**[secondary accounting**]命令用来配置从RADIUS计费服务器。

**[undo secondary accounting**]命令用来删除指定的从RADIUS计费服务器。

【命令】

**[secondary accounting ***ipv4-address*[\| **ipv6** *ipv6-address* } [ *port-number* \| **key** { **cipher** \| **simple** } *string* \| **vpn-instance** *vpn-instance-name* ] \*]

**[undo secondary accounting **\*[ipv4-address*[\| **ipv6** *ipv6-address* } [ *port-number* \| **vpn-instance** *vpn-instance-name* ] \* ]]

【缺省情况】]

未配置从]RADIUS计费服务器

【视图】

RADIUS方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv4-address*]：从RADIUS计费服务器的IPv4地址。

**[ipv6*** ipv6-address*]：从RADIUS计费服务器的IPv6地址。

*[port-number*]：从RADIUS计费服务器的UDP端口号，缺省为1813，取值范围为1～65535。此端口号必须与服务器提供计费服务的端口号保持一致。

**[key**[ { **cipher** \| **simple** } *string*]]：与从RADIUS计费服务器交互的计费报文的共享密钥。此共享密钥必须与服务器上配置的共享密钥保持一致。

·**cipher ***string*：以密文方式设置共享密钥。非FIPS模式下，*string*为1～117个字符的密文字符串，区分大小写；FIPS模式下，*string*为15～117个字符的密文字符串，区分大小写。

·**simple ***string*：以明文方式设置共享密钥。非FIPS模式下，*string*为1～64个字符的明文字符串，区分大小写；FIPS模式下，*string*为15～64个字符的明文字符串，区分大小写，密钥元素的最少组合类型为4（必须包括数字、大写字母、小写字母以及特殊字符）。

**[vpn-instance ***vpn-instance-name*]：从RADIUS计费服务器所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示从RADIUS计费服务器位于公网中。该参数支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

可通过多次执行本命令，配置多个从RADIUS计费服务器。当主服务器不可达时，设备根据从服务器的配置顺序由先到后查找状态为**active**的从服务器并与之交互。每个RADIUS方案中最多支持配置16个从RADIUS计费服务器。

需要注意的是：

·在同一个方案中指定的主计费服务器和从计费服务器的IP地址、端口号和VPN参数不能完全相同，并且各从计费服务器的IP地址、端口号和VPN参数也不能完全相同。

·设备与从计费服务器通信时优先使用本命令设置的共享密钥，如果此处未设置，则使用命令**key** **accounting**命令设置的共享密钥。

·若服务器位于MPLS VPN私网中，为保证RADIUS报文被发送到指定的私网服务器，必须指定服务器所属的VPN实例名称。本命令指定的服务器所属的VPN比RADIUS方案所属的VPN优先级高。

·如果在发送计费开始请求过程中使用本命令删除了正在使用的从服务器，则设备在与当前服务器通信超时后，将会重新按照优先级顺序开始依次查找状态为**active**的服务器进行通信。

·如果在线用户正在使用的计费服务器被删除，则设备将无法发送用户的实时计费请求和停止计费请求，且停止计费报文不会被缓存到本地。

·以明文或密文方式设置的共享密钥，均以密文的方式保存在配置文件中。

【举例】

\# 设置RADIUS方案radius1的从计费服务器的IP地址为10.110.1.1，使用UDP端口1813提供RADIUS计费服务。

\<Sysname\> system-view

Sysname radius scheme radius1

Sysname-radius-radius1 secondary accounting 10.110.1.1 1813

\# 设置RADIUS方案radius2的从计费服务器：IP地址分别为10.110.1.1，10.110.1.2，均使用UDP端口1813提供RADIUS计费服务。

\<Sysname\> system-view

Sysname radius scheme radius2

Sysname-radius-radius2 secondary accounting 10.110.1.1 1813

Sysname-radius-radius2 secondary accounting 10.110.1.2 1813

【相关命令】

·**display radius scheme**

·**key **(RADIUS scheme view)

·**primary accounting**

·**vpn-instance **(RADIUS scheme view)

**AAA \-- RADIUS配置命令 \-- secondary authentication (RADIUS scheme view)**

------------------------------------------------------------------------

**[secondary authentication**]命令用来配置从RADIUS认证服务器。

**[undo secondary authentication**]命令用来删除指定的从RADIUS认证服务器。

【命令】

**[secondary authentication ***ipv4-address*[\| **ipv6** *ipv6-address* } [ *port-number* \| **key** { **cipher** \| **simple** } *string* \| **test-profile** *profile-name* \| **vpn-instance** *vpn-instance-name* ] \*]

**[undo secondary authentication **\*[ipv4-address*[\| **ipv6** *ipv6-address* } [ *port-number* \| **vpn-instance** *vpn-instance-name* ] \* ]]

【缺省情况】]

未配置从]RADIUS认证服务器。

【视图】

RADIUS方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv4-address*]：从RADIUS认证服务器的IPv4地址。

**[ipv6**]*ipv6-address*：从RADIUS认证服务器的IPv6地址。

*[port-number*]：从RADIUS认证服务器的UDP端口号，取值范围为1～65535，缺省为1812。此端口号必须与服务器提供认证服务的端口号保持一致。

**[key**  { **cipher** \| **simple** } *string*]：与从RADIUS认证服务器交互的认证报文的共享密钥。此共享密钥必须与服务器上配置的共享密钥保持一致。

·**cipher ***string*：以密文方式设置共享密钥。非FIPS模式下，*string*为1～117个字符的密文字符串，区分大小写；FIPS模式下，*string*为15～117个字符的密文字符串，区分大小写。

·**simple ***string*：以明文方式设置共享密钥。非FIPS模式下，*string*为1～64个字符的明文字符串，区分大小写；FIPS模式下，*string*为15～64个字符的明文字符串，区分大小写，密钥元素的最少组合类型为4（必须包括数字、大写字母、小写字母以及特殊字符）。

**[test-profile*** profile-name*]：RADIUS服务器探测模版名称，为1～31个字符的字符串，区分大小写。

**[vpn-instance ***vpn-instance-name*]：从RADIUS认证服务器所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示从RADIUS认证服务器位于公网中。该参数支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

可通过多次执行本命令，配置多个从RADIUS认证服务器。当主服务器不可达时，设备根据从服务器的配置顺序由先到后查找状态为**active**的从服务器并与之交互。每个RADIUS方案中最多支持配置16个从RADIUS认证服务器。

RADIUS认证服务器引用了存在的服务器探测模版后，将会触发对该服务器的探测功能。RADIUS服务器探测功能是指，设备周期性发送探测报文探测RADIUS服务器是否可达：如果服务器不可达，则置服务器状态为**block**，如果服务器可达，则置服务器状态为**active**。

需要注意的是：

·在同一个方案中指定的主认证服务器和从认证服务器的IP地址、端口号和VPN参数不能完全相同，并且各从认证服务器的IP地址、端口号和VPN参数也不能完全相同。

·设备与从认证服务器通信时优先使用本命令设置的共享密钥，如果此处未设置，则使用命令**key** **authentication**命令设置的共享密钥。

·若服务器位于MPLS VPN私网中，为保证RADIUS报文被发送到指定的私网服务器，必须指定服务器所属的VPN实例名称。本命令指定的服务器所属的VPN比RADIUS方案所属的VPN优先级高。

·如果在认证过程中使用本命令删除了正在使用的从服务器，则设备在与当前服务器通信超时后，将会重新按照优先级顺序开始依次查找状态为**active**的服务器进行通信。

·以明文或密文方式设置的共享密钥，均以密文的方式保存在配置文件中。

【举例】

\# 设置RADIUS方案radius1的从认证服务器的IP地址为10.110.1.2，使用UDP端口1812提供RADIUS认证/授权服务。

\<Sysname\> system-view

Sysname radius scheme radius1

Sysname-radius-radius1 secondary authentication 10.110.1.2 1812

\# 设置RADIUS方案radius2的从认证服务器：IP地址分别为10.110.1.1，10.110.1.2，均使用UDP端口1812提供RADIUS认证/授权服务。

\<Sysname\> system-view

Sysname radius scheme radius2

Sysname-radius-radius2 secondary authentication 10.110.1.1 1812

Sysname-radius-radius2 secondary authentication 10.110.1.2 1812

【相关命令】

·**display radius scheme**

·**key **(RADIUS scheme view)

·**primary authentication**

·**radius-server test-profile**

·**vpn-instance **(RADIUS scheme view)

**AAA \-- RADIUS配置命令 \-- security-policy-server**

------------------------------------------------------------------------

**[security-policy-server**]命令用来指定安全策略服务器。

**[undo security-policy-server**]命令用来删除指定的安全策略服务器。

【命令】

**[security-policy-server **[*[ipv4-address \| ]***ipv6*** ipv6-address *}** **vpn-instance** *vpn-instance-name* ]]

**[undo security-policy-server **[{ { *ipv4-address \| * **ipv6** *ipv6-address* } [ **vpn-instance** *vpn-instance-name* ] \| **all** }]]

【缺省情况】

未指定安全策略服务器。

【视图】

RADIUS方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv4-address*]：安全策略服务器IPv4地址。

**[ipv6*** ipv6-address*]：安全策略服务器的IPv6地址。

**[vpn-instance** *vpn-instance-name*]：安全策略服务器所属的VPN的实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则表示安全策略服务器属于公网。

**[all**]：所有安全策略服务器。

【使用指导】

一个RADIUS方案中最多可以指定8个安全策略服务器。

【举例】

\# 指定RADIUS方案radius1的安全策略服务器IP地址为10.110.1.2。

\<Sysname\> system-view

Sysname radius scheme radius1

Sysname-radius-radius1 security-policy-server 10.110.1.2

【相关命令】

·**display radius scheme**

**AAA \-- RADIUS配置命令 \-- snmp-agent trap enable radius**

------------------------------------------------------------------------

**[snmp-agent trap enable radius**]命令用来开启RADIUS告警功能。

**[undo snmp-agent trap enable radius**]命令用来关闭指定的RADIUS告警功能。

【命令】

**[snmp-agent trap enable radius **[[ **accounting-server-down** \| **accounting-server-up** \| **authentication-error-threshold** \| **authentication-server-down** \|  **authentication-server-up** ] \*]]

**[undo snmp-agent trap enable radius **[[ **accounting-server-down** \| **accounting-server-up** \| **authentication-error-threshold** \| **authentication-server-down \| authentication-server-up** ] \*]]

【缺省情况】

所有类型的RADIUS告警功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[accounting-server-down**]：表示RADIUS计费服务器可达状态变为down时发送告警信息。

**[accounting-server-up**]：表示RADIUS计费服务器可达状态变为up时发送告警信息。

**[authentication-error-threshold**]：表示认证失败次数超过阈值时发送告警信息。该阈值为认证失败次数占认证请求总数的百分比数值，目前仅能通过MIB方式配置，取值范围为1～100，缺省为30。

**[authentication-server-down**]：表示RADIUS认证服务器可达状态变为down时发送告警信息。

**[authentication-server-up**]：表示RADIUS认证服务器可达状态变为up时发送告警信息。

【使用指导】

不指定可选参数时，表示开启/关闭所有类型的RADIUS告警功能。

开启RADIUS服务器可达状态改变时的告警功能后，告警信息的发送包括以下两种情况：

·当NAS向RADIUS服务器发送计费或认证请求没有收到响应时，会重传请求，当重传次数达到最大传送次数时仍然没有收到响应时，NAS认为该服务器不可达，并发送表示RADIUS服务器不可达的告警信息。

·当**timer quiet**定时器设定的时间到达后，NAS将服务器的状态置为激活状态并发送表示RADIUS服务器可达的告警信息。

·当NAS发现认证失败次数与认证请求总数的百分比超过阈值时，会发送表示认证失败次数超过阈值的告警信息。

开启认证失败次数超过阈值时的告警功能后，当NAS发现认证失败次数与认证请求总数的百分比超过阈值时，会发送表示认证失败次数超过阈值的告警信息。

【举例】

\# 开启RADIUS计费服务器可达状态变为down时的告警功能。

\<Sysname\> system-view

Sysname snmp-agent trap enable radius accounting-server-down

**AAA \-- RADIUS配置命令 \-- state primary**

------------------------------------------------------------------------

**[state primary**]命令用来设置主RADIUS服务器的状态。

【命令】

**[state**[ **primary** { **accounting** \| **authentication** } { **active** \| **block** }]]

【缺省情况】

RADIUS方案中配置了IP地址的主RADIUS服务器状态为**active**。

【视图】

RADIUS方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[accounting**]：设置主RADIUS计费服务器的状态。

**[authentication**]：设置主RADIUS认证服务器的状态。

**[active**]：设置主RADIUS服务器的状态为**active**，即处于正常工作状态。

**[block**]：设置主RADIUS服务器的状态为**block**，即处于通信中断状态。

【使用指导】

每次用户发起认证或计费，如果主服务器状态为**active**，则设备都会首先尝试与主服务器进行通信，如果主服务器不可达，则将主服务器的状态置为**block**，同时启动主服务器的**timer quiet**定时器，然后设备会严格按照从服务器的配置先后顺序依次查找状态为**active**的从服务器。在**timer quiet**定时器设定的时间到达之后，主服务器状态将由**block**恢复为**active**。若该定时器超时之前，通过本命令将主服务器的状态手工设置为**block**，则定时器超时之后主服务器状态不会自动恢复为**active**，除非通过本命令手工将其设置为**active**。

如果主服务器与所有从服务器状态都是**block**，则认证或计费失败。

认证服务器的状态会影响设备对该服务器可达性探测功能的开启。当指定的服务器状态为**active**，且该服务器通过**radius-server test-profile**命令成功引用了一个已存在的服务器探测模版时，则设备会开启对该服务器的可达性探测功能。当手工将该服务器状态置为**block**时，会关闭对该服务器的可达性探测功能。

【举例】

\# 将RADIUS方案radius1的主认证服务器的状态设置为**block**。

\<Sysname\> system-view

Sysname radius scheme radius1

Sysname-radius-radius1 state primary authentication block

【相关命令】

·**display** **radius scheme**

·**radius-server test-profile**

·**state** **secondary**

**AAA \-- RADIUS配置命令 \-- state secondary**

------------------------------------------------------------------------

**[state secondary**]命令用来设置从RADIUS服务器的状态。

【命令】

**[state**[ **secondary** { **accounting** \| **authentication** } \*[v4]-address*[ \| **ipv6** *ipv6-address* } [ *port-number* \| **vpn-instance** *vpn-instance-name* ] \* ] { **active** \| **block** }]

【缺省情况】]

RADIUS方案中配置了IP地址的各从RADIUS服务器状态为**active**。

【视图】

RADIUS方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[accounting**]：设置从RADIUS计费服务器的状态。

**[authentication**]：设置从RADIUS认证服务器的状态。

*[ip*]*v4-address*：指定从RADIUS服务器的IPv4地址。

**[ipv6**]*ipv6-address*：指定从RADIUS服务器的IPv6地址。

*[port-number*]：指定从RADIUS服务器的UDP端口号，取值范围为1～65535，从RADIUS计费服务器的缺省UDP端口号为1813，从RADIUS认证服务器的缺省UDP端口号为1812。

**[vpn-instance ***vpn-instance-name*]：从RADIUS服务器所属的VPN。*vpn-instance-name*表示MPLS L3VPN实例名称，为1～31个字符的字符串，区分大小写。

**[active**]：设置从RADIUS服务器的状态为**active**，即处于正常工作状态。

**[block**]：设置从RADIUS服务器的状态为**block**，即处于通信中断状态。

【使用指导】

如果不指定从服务器IP地址，那么本命令将会修改所有已配置的从认证服务器或从计费服务器的状态。

如果设备查找到的状态为**active**的从服务器不可达，则设备会将该从服务器的状态置为**block**，同时启动该服务器的**timer quiet**定时器，并继续查找下一个状态为**active**的从服务器。在**timer quiet**定时器设定的时间到达之后，从服务器状态将由**block**恢复为**active**。若该定时器超时之前，通过本命令将从服务器的状态手工设置为**block**，则定时器超时之后从服务器状态不会自动恢复为**active**，除非通过本命令手工将其设置为**active**。如果所有已配置的从服务器都不可达，则本次认证或计费失败。

认证服务器的状态会影响设备对该服务器可达性探测功能的开启。当指定的服务器状态为**active**，且该服务器通过**radius-server test-profile**命令成功引用了一个已存在的服务器探测模版时，则设备会开启对该服务器的可达性探测功能。当手工将该服务器状态置为**block**时，会关闭对该服务器的可达性探测功能。

【举例】

\# 将RADIUS方案radius1的从认证服务器的状态设置为**block**。

\<Sysname\> system-view

Sysname radius scheme radius1

Sysname-radius-radius1 state secondary authentication block

【相关命令】

·**display** **radius scheme**

·**radius-server test-profile**

·**state** **primary**

**AAA \-- RADIUS配置命令 \-- timer quiet (RADIUS scheme view)**

------------------------------------------------------------------------

**[timer quiet**]命令用来设置服务器恢复激活状态的时间。

**[undo timer quiet**]命令用来恢复缺省情况。

【命令】

**[timer quiet ***minutes*]

**[undo timer quiet**]

【缺省情况】

服务器恢复激活状态的时间为5分钟。

【视图】

RADIUS方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[minutes*]：恢复激活状态的时间，取值范围为1～255，单位为分钟。

【使用指导】

建议根据配置的从服务器数量合理设置服务器恢复激活状态的时间。如果服务器恢复激活状态时间设置的过短，就会出现设备反复尝试与状态**active**但实际不可达的服务器通信而导致的认证或计费频繁失败的问题。

【举例】

\# 设置服务器恢复激活状态的时间为10分钟。

\<Sysname\> system-view

Sysname radius scheme radius1

Sysname-radius-radius1 timer quiet 10

【相关命令】

·**display radius scheme**

**AAA \-- RADIUS配置命令 \-- timer realtime-accounting (RADIUS scheme view)**

------------------------------------------------------------------------

**[timer realtime-accounting**]命令用来设置实时计费的时间间隔。

**[undo timer realtime-accounting**]命令用来恢复缺省情况。

【命令】

**[timer realtime-accounting** *interval* [ **second** ]]

**[undo timer realtime-accounting**]

【缺省情况】

实时计费的时间间隔为12分钟。

【视图】

RADIUS方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：实时计费的时间间隔，取值范围为0～71582。

**[second**]：表示实时计费的时间间隔以秒为单位，缺省以分钟为单位。

【使用指导】

为了对用户实施实时计费，有必要设置实时计费的时间间隔。不同的取值的处理有所不同：

·若实时计费间隔不为0，则每隔设定的时间，设备会向RADIUS服务器发送一次在线用户的计费信息。

·若实时计费间隔设置为0，且服务器上配置了实时计费间隔，则设备按照服务器上配置的实时计费间隔向RADIUS服务器发送在线用户的计费信息；如果服务器上没有配置该值，则设备不向RADIUS服务器发送在线用户的计费信息。

实时计费间隔的取值与RADIUS服务器的性能和用户的数目有一定关系。取值小，会增加网络中的数据流量，对设备和RADIUS服务器的性能要求就高；取值大，会影响计费的准确性。因此要结合网络的实际情况合理设置计费间隔。一般情况下，建议当用户量比较大（大于等于1000）时，尽量把该间隔的值设置得大一些。以下是实时计费间隔与用户量之间的推荐比例关系。

表1-6 实时计费间隔与用户量之间的推荐比例关系

用户数

实时计费间隔（分钟）

1～99

3

100～499

6

500～999

12

大于等于1000

大于等于15

****

【举例】

\# 将RADIUS方案radius1的实时计费的时间间隔设置为51分钟。

\<Sysname\> system-view

Sysname radius scheme radius1

Sysname-radius-radius1 timer realtime-accounting 51

【相关命令】

·**retry realtime-accounting**

**AAA \-- RADIUS配置命令 \-- timer response-timeout (RADIUS scheme view)**

------------------------------------------------------------------------

**[timer response-timeout**]命令用来设置RADIUS服务器响应超时时间。

**[undo timer response-timeout**]命令用来恢复缺省情况。

【命令】

**[timer response-timeout***seconds*]

**[undo timer response-timeout**]

【缺省情况】

RADIUS服务器响应超时时间为3秒。

【视图】

RADIUS方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：RADIUS服务器响应超时时间，取值范围为1～10，单位为秒。

【使用指导】

如果在RADIUS请求报文传送出去一段时间后，设备还没有得到RADIUS服务器的响应，则有必要重传RADIUS请求报文，以保证用户尽可能地获得RADIUS服务，这段时间被称为RADIUS服务器响应超时时间，本命令用于调整这个时间。

需要注意的是，发送RADIUS报文的最大尝试次数与RADIUS服务器响应超时时间的乘积不能超过300秒。

【举例】

\# 将RADIUS方案radius1的服务器响应超时时间设置为5秒。

\<Sysname\> system-view

Sysname radius scheme radius1

Sysname-radius-radius1 timer response-timeout 5

【相关命令】

·**display radius scheme**

·**retry**

**AAA \-- RADIUS配置命令 \-- user-name-format (RADIUS scheme view)**

------------------------------------------------------------------------

**[user-name-format**]命令用来设置发送给RADIUS服务器的用户名格式。

**[undo user-name-format**]命令用来恢复缺省情况。

【命令】

**[user-name-format**[ { **keep-original** \| **with-domain** \| **without-domain** }]]

**[undo user-name-format**]

【缺省情况】

设备发送给RADIUS服务器的用户名携带有ISP域名。

【视图】

RADIUS方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[keep-original**]：发送给RADIUS服务器的用户名与用户的输入保持一致。

**[with-domain**]：发送给RADIUS服务器的用户名带ISP域名。

**[without-domain**]：发送给RADIUS服务器的用户名不带ISP域名。

【使用指导】

接入用户通常以"*userid@isp-name*"的格式命名，"*@*"后面的部分为ISP域名，设备就是通过该域名来决定将用户归于哪个ISP域的。但是，有些较早期的RADIUS服务器不能接受携带有ISP域名的用户名，在这种情况下，有必要将用户名中携带的域名去除后再传送给RADIUS服务器。因此，设备提供此命令以指定发送给RADIUS服务器的用户名是否携带有ISP域名。

需要注意的是：

·如果指定某个RADIUS方案不允许用户名中携带有ISP域名，那么请不要在两个或两个以上的ISP域中同时设置使用该RADIUS方案。否则，会出现虽然实际用户不同（在不同的ISP域中），但RADIUS服务器认为用户相同（因为传送到它的用户名相同）的错误。

·在802.1X用户采用EAP认证方式的情况下，RADIUS方案中配置的**user-name-format**命令无效，客户端传送给RADIUS服务器的用户名与用户输入的用户名保持一致。

·若接入用户为需要漫游的无线用户，建议接入设备上将发送给RADIUS服务器的用户名格式配置为**keep-original**类型，否则可能导致这类用户认证失败。

【举例】

\# 指定发送给RADIUS方案radius1中RADIUS服务器的用户名不得携带域名。

\<Sysname\> system-view

Sysname radius scheme radius1

Sysname-radius-radius1 user-name-format without-domain

【相关命令】

·**display radius scheme**

**AAA \-- RADIUS配置命令 \-- vpn-instance (RADIUS scheme view)**

------------------------------------------------------------------------

![说明](AAA命令.files/image001.png)

本命令的支持请与设备的型号有关，请以设备的实际情况为准。

**[vpn-instance**]命令用来配置RADIUS方案所属的VPN。

**[undo vpn-instance**]命令用来恢复缺省情况。

【命令】

**[vpn-instance ***vpn-instance-name*]

**[undo vpn-instance**]

【缺省情况】

RADIUS方案属于公网。

【视图】

RADIUS方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vpn-instance-name*]：MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。

【使用指导】

本命令配置的VPN对于该方案下的所有RADIUS认证/计费服务器生效，但设备优先使用配置RADIUS认证/计费服务器时为各服务器单独指定的VPN。

【举例】

\# 配置RADIUS方案radius1所属的VPN为test。

\<Sysname\> system-view

Sysname radius scheme radius1

Sysname-radius-radius1 vpn-instance test

【相关命令】

·**display radius scheme**

**AAA \-- HWTACACS配置命令 \-- data-flow-format (HWTACACS scheme view)**

------------------------------------------------------------------------

**[data-flow-format**]命令用来配置发送到HWTACACS服务器的数据流的单位。

**[undo data-flow-format**]命令用来恢复缺省情况。

【命令】

**[data-flow-format **[{ **data** { **byte** \| **giga-byte** \| **kilo-byte** \| **mega-byte** } \| **packet** { **giga-packet** \| **kilo-packet** \| **mega-packet** \| **one-packet** } } \*]]

**[undo data-flow-format **[{ **data** \| **packet** }]]

【缺省情况】

数据流的单位为**byte**，数据包的单位为**one-packet**。

【视图】

HWTACACS方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[data**]：设置数据流的单位。

·**byte**：数据流的单位为字节。

·**giga-byte**：数据流的单位千兆字节。

·**kilo-byte**：数据流的单位为千字节。

·**mega-byte**：数据流的单位为兆字节。

**[packet**]：设置数据包的单位。

·**giga-packet**：数据包的单位为千兆包。

·**kilo-packet**：数据包的单位为千包。

·**mega-packet**：数据包的单位为兆包。

·**one-packet**：数据包的单位为包。

【使用指导】

设备上配置的发送给HWTACACS服务器的数据流单位及数据包单位应与HWTACACS服务器上的流量统计单位保持一致，否则无法正确计费。

【举例】

\# 在HWTACACS方案radius1中，设置发往HWTACACS服务器的数据流的数据单位为**kilo-byte**、数据包的单位为**kilo-packet**。

\<Sysname\> system-view

Sysname hwtacacs scheme hwt1

Sysname-hwtacacs-hwt1 data-flow-format data kilo-byte packet kilo-packet

【相关命令】

·**display hwtacacs scheme**

**AAA \-- HWTACACS配置命令 \-- display hwtacacs scheme**

------------------------------------------------------------------------

**[display hwtacacs scheme**]命令用来查看HWTACACS方案的配置信息或HWTACACS服务相关的统计信息。

【命令】

**[display hwtacacs scheme ** *hwtacacs-scheme-name*  **statistics**  ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[hwtacacs-scheme-name*]：显示指定的HWTACACS的配置或统计信息。*hwtacacs-scheme-name*为HWTACACS方案名，为1～32个字符的字符串，不区分大小写。

**[statistics**]：显示HWTACACS服务相关的统计信息。不指定该参数，则显示HWTACACS方案的配置信息。

【使用指导】

如果不指定HWTACACS方案名，则显示所有HWTACACS方案的配置信息。

【举例】

\# 查看所有HWTACACS方案的配置情况。

\<Sysname\> display hwtacacs scheme

Total 1 TACACS schemes

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

HWTACACS Scheme Name  : hwtac

  Index : 0

  Primary Auth Server:

    IP  : 2.2.2.2         Port: 49     State: Active

    VPN Instance: 2

    Single-connection: Enabled

  Primary Author Server:

    IP  : 2.2.2.2         Port: 49     State: Active

    VPN Instance: 2

    Single-connection: Disabled

  Primary Acct Server:

    IP  : Not Configured  Port: 49     State: Block

    VPN Instance: Not configured

    Single-connection: Disabled

  VPN Instance                          : 2

  NAS IP Address                        : 2.2.2.3

  Server Quiet Period(minutes)          : 5

  Realtime Accounting Interval(minutes) : 12

  Response Timeout Interval(seconds)    : 5

  Username Format                       : with-domain

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

表1-7 display hwtacacs scheme命令显示信息描述表

字段

描述

Total 1 TACACS schemes

共计1个HWTACACS方案

HWTACACS Scheme Name

HWTACACS方案的名称

Index

HWTACACS方案的索引号

Primary Auth Server

主HWTACACS认证服务器

Primary Author Server

主HWTACACS授权服务器

Primary Acct Server

主HWTACACS计费服务器

Secondary Auth Server

从HWTACACS认证服务器

Secondary Author Server

从HWTACACS授权服务器

Secondary Acct Server

从HWTACACS计费服务器

IP

HWTACACS服务器的IP地址

未配置时，显示为Not configured

Port

HWTACACS服务器的端口号

未配置时，显示缺省值

Single-connection

单连接状态

·Enabled：使用一条TCP连接与服务器通信

·Disabled：每次新建TCP连接与服务器通信

State

HWTACACS服务器目前状态

·Active：激活状态

·Block：静默状态

VPN Instance

HWTACACS服务器所在的VPN

未配置时，显示为Not configured

VPN Instance

HWTACACS方案所属的VPN名称

未配置时，显示为Not configured

NAS IP Address

发送HWTACACS报文的源IP地址

Server Quiet Period

主HWTACACS服务器恢复激活状态的时间（分钟）

Realtime Accounting Interval(minutes)

实时HWTACACS计费更新报文的发送间隔（分钟）

Response Timeout Interval

HWTACACS服务器超时时间（秒）

Username Format

用户名格式

·with-domain：携带域名

·without-domain：不携带域名

·keep-original：与用户输入保持一致

【相关命令】

·**reset hwtacacs statistics**

**AAA \-- HWTACACS配置命令 \-- hwtacacs nas-ip**

------------------------------------------------------------------------

**[hwtacacs nas-ip**]命令用来指定设备发送HWTACACS报文使用的源地址。

**[undo hwtacacs nas-ip**]命令用来删除指定的源地址。

【命令】

**[hwtacacs nas-ip****[{ *ipv4-address* \| **ipv6** *ipv6-address* } [ **vpn-instance** *vpn-instance-name* ]]]

**[undo hwtacacs nas-ip **[{ *ipv4-address* \| **ipv6** *ipv6-address* } [ **vpn-instance** *vpn-instance-name* ]]]

【缺省情况】

未指定源地址，即以发送报文的接口的主IP地址作为源地址。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv4-address*]：指定的源IPv4地址，应该为本机的地址，不能为全0地址、全1地址、D类地址、E类地址和环回地址。

**[ipv6** *ipv6-address*]：指定的源IPv6地址，应该为本机的地址，必须是单播地址，不能为环回地址与本地链路地址。

**[vpn-instance ***vpn-instance-name*]：指定私网源IP地址所属的VPN。MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。若不指定该参数，则表示配置的是公网源地址。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

HWTACACS服务器上通过IP地址来标识接入设备，并根据收到的HWTACACS报文的源IP地址是否与服务器所管理的接入设备的IP地址匹配，来决定是否处理来自该接入设备的认证或计费请求。因此，为保证认证、授权和计费报文可被服务器正常接收并处理，接入设备上发送HWTACACS报文使用的源地址必须与HWTACACS服务器上指定的接入设备的IP地址保持一致。

需要注意的是：

·系统最多允许指定16个源地址，其中，最多包括一个IPv4公网源地址和一个IPv6公网源地址，其余为IPv4或IPv6私网源地址。新配置的IPv4/IPv6公网源地址会覆盖原有的IPv4/IPv6公网源地址。而且，对于同一个VPN，最多只能指定一个IPv4私网源地址和一个IPv6私网源地址，新配置会覆盖原有配置。

·HWTACACS方案视图下的命令**nas-ip**只对本HWTACACS方案有效，系统视图下的命令**hwtacacs nas-ip**对所有HWTACACS方案有效。HWTACACS方案视图下的设置具有更高的优先级。

【举例】

\# 配置设备发送HWTACACS报文使用的源地址为129.10.10.1。

\<Sysname\> system-view

Sysname hwtacacs nas-ip 129.10.10.1

【相关命令】

·**nas-ip**

**AAA \-- HWTACACS配置命令 \-- hwtacacs scheme**

------------------------------------------------------------------------

**[hwtacacs scheme**]命令用来创建HWTACACS方案，并进入HWTACACS方案视图。

**[undo hwtacacs scheme**]命令用来删除指定的HWTACACS方案。

【命令】

**[hwtacacs scheme** *hwtacacs-scheme-name*]

**[undo hwtacacs scheme** *hwtacacs-scheme-name*]

【缺省情况】

不存在任何HWTACACS方案。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[hwtacacs-scheme-name*]：HWTACACS方案名称，为1～32个字符的字符串，不区分大小写。

【使用指导】

一个HWTACACS方案可以同时被多个ISP域引用。

最多可以配置16个HWTACACS方案。

【举例】

\# 创建名为hwt1的HWTACACS方案并进入相应的HWTACACS视图。

\<Sysname\> system-view

Sysname hwtacacs scheme hwt1

Sysname-hwtacacs-hwt1

【相关命令】

·**display hwtacacs scheme**

**AAA \-- HWTACACS配置命令 \-- key (HWTACACS scheme view)**

------------------------------------------------------------------------

**[key**]命令用来配置HWTACACS认证、授权、计费报文的共享密钥。

**[undo key**]命令用来删除配置。

【命令】

**[key **[{ **accounting** \| **authentication** \| **authorization** } { **cipher** \| **simple** } *string*]]

**[undo key **[{ **accounting** \| **authentication** \| **authorization** }]]

【缺省情况】

无共享密钥。

【视图】

HWTACACS方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[accounting**]：指定HWTACACS计费报文的共享密钥。

**[authentication**]：指定HWTACACS认证报文的共享密钥。

**[authorization**]：指定HWTACACS授权报文的共享密钥。

**[cipher**]：表示以密文方式设置共享密钥。

**[simple**]：表示以明文方式设置共享密钥。

*[key*]：设置的明文密钥或密文密钥，区分大小写。非FIPS模式下，明文密钥为1～255个字符的字符串；密文密钥为1～373个字符的字符串；FIPS模式下，明文密钥为15～255个字符的字符串，密钥元素的最少组合类型为4（必须包括数字、大写字母、小写字母以及特殊字符）；密文密钥为15～373个字符的字符串。

【使用指导】

必须保证设备上设置的共享密钥与HWTACACS服务器上的完全一致。

以明文或密文方式设置的共享密钥，均以密文的方式保存在配置文件中。

【举例】

\# 配置HWTACACS认证报文共享密钥为明文123456TESTauth&!。

\<Sysname\> system-view

Sysname hwtacacs scheme hwt1

Sysname-hwtacacs-hwt1 key authentication simple 123456TESTauth&!

\# 配置HWTACACS授权报文共享密钥为明文123456TESTautr&!。

Sysname-hwtacacs-hwt1 key authorization simple 123456TESTautr&!

\# 配置HWTACACS计费报文共享密钥为明文123456TESTacct&!。

Sysname-hwtacacs-hwt1 key accounting simple 123456TESTacct&!

【相关命令】

·**display hwtacacs scheme**

**AAA \-- HWTACACS配置命令 \-- nas-ip (HWTACACS scheme view)**

------------------------------------------------------------------------

**[nas-ip**]命令用来指定设备发送HWTACACS报文使用的源IP地址。

**[undo nas-ip**]命令用来删除指定的源IP地址。

【命令】

**[nas-ip**] *[ipv6-address* }

**[undo nas-ip **] **ipv6** ]

【缺省情况】

使用系统视图下由命令**hwtacacs nas-ip**指定的源地址，若系统视图下未指定源地址，则使用发送HWTACACS报文的接口的主IP地址。

【视图】

HWTACACS方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv4-address*]：指定的源IPv4地址，应该为本机的地址，不能为全0地址、全1地址、D类地址、E类地址和环回地址。

**[ipv6** *ipv6-address*]：指定的源IPv6地址，应该为本机的地址，必须是单播地址，不能为环回地址与本地链路地址。

【使用指导】

HWTACACS服务器上通过IP地址来标识接入设备，并根据收到的HWTACACS报文的源IP地址是否与服务器所管理的接入设备的IP地址匹配，来决定是否处理来自该接入设备的认证、授权、计费请求。

需要注意的是：

·为保证认证和计费报文可被服务器正常接收并处理，接入设备上发送HWTACACS报文使用的源地址必须与HWTACACS服务器上指定的接入设备的IP地址保持一致。

·HWTACACS方案视图下的命令**nas-ip**只对本HWTACACS方案有效，系统视图下的命令**hwtacacs nas-ip**对所有HWTACACS方案有效。HWTACACS方案视图下的设置具有更高的优先级。

·如果重复执行此命令，新配置的IPv4/IPv6源地址会覆盖原有的IPv4/IPv6源地址。

【举例】

\# 为HWTACACS方案hwt1配置设备发送HWTACACS报文使用的源IP地址为10.1.1.1。

\<Sysname\> system-view

Sysname hwtacacs scheme hwt1

Sysname-hwtacacs-hwt1 nas-ip 10.1.1.1

【相关命令】

·**hwtacacs nas-ip**

**AAA \-- HWTACACS配置命令 \-- primary accounting (HWTACACS scheme view)**

------------------------------------------------------------------------

**[primary accounting**]命令用来配置主HWTACACS计费服务器。

**[undo primary accounting**]命令用来删除配置的主HWTACACS计费服务器。

【命令】

**[primary accounting ***ipv4-address*[\| **ipv6** *ipv6-address* } [ *port-number* \| **key** { **cipher** \| **simple** } *string* \| **single-connection** \| **vpn-instance** *vpn-instance-name* ] **\***]

**[undo primary accounting**]

【缺省情况】]

未配置HWTACACS主计费服务器。

【视图】

HWTACACS方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv4-address*]：主HWTACACS计费服务器的IPv4地址。

**[ipv6*** ipv6-address*]：主HWTACACS计费服务器的IPv6地址。

*[port-number*]：主HWTACACS计费服务器的TCP端口号，取值范围为1～65535，缺省值为49。此端口号必须与服务器提供计费服务的端口号保持一致。

**[key**[ { **cipher** \| **simple** } *string*]]：与主HWTACACS计费服务器交互的计费报文的共享密钥。此共享密钥必须与服务器上配置的共享密钥保持一致。

·**cipher ***string*：以密文方式设置共享密钥。非FIPS模式下，*string*为1～373个字符的密文字符串，区分大小写；FIPS模式下，*string*为15～373个字符的密文字符串，区分大小写。

·**simple ***string*：以明文方式设置共享密钥。非FIPS模式下，*string*为1～255个字符的明文字符串，区分大小写；FIPS模式下，*string*为15～255个字符的明文字符串，区分大小写，密钥元素的最少组合类型为4（必须包括数字、大写字母、小写字母以及特殊字符）。

**[single-connection**]：所有与主HWTACACS计费服务器交互的计费报文使用同一个TCP连接。如果未指定本参数，则表示每次计费都会使用一个新的TCP连接。

**[vpn-instance ***vpn-instance-name*]：主HWTACACS计费服务器所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示主HWTACACS计费服务器位于公网中。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

在同一个方案中指定的主计费服务器和从计费服务器的IP地址、端口号和VPN参数不能完全相同。

若服务器位于MPLS VPN私网中，为保证HWTACACS报文被发送到指定的私网服务器，必须指定服务器所属的VPN实例名称。本命令指定的服务器所属的VPN比HWTACACS方案所属的VPN优先级高。

只有在设备与计费服务器没有报文交互时，才允许删除该服务器。计费服务器删除后，只对之后的计费过程有影响。

以明文或密文方式设置的共享密钥，均以密文的方式保存在配置文件中。

配置**single-connection**参数后可节省TCP连接资源，但有些TACACS服务器不支持这种方式，需要根据服务器支持情况进行配置。在服务器支持这种方式的情况下，建议配置**single-connection**参数，以提高性能和效率。

【举例】

\# 配置主HWTACACS计费服务器的IP地址为10.163.155.12，使用TCP端口49与HWTACACS计费服务器通信，计费报文的共享密钥为明文123456TESTacct&!。

\<Sysname\> system-view

Sysname hwtacacs scheme test1

Sysname-hwtacacs-test1 primary accounting 10.163.155.12 49 key simple 123456TESTacct&!

【相关命令】

·**display hwtacacs scheme**

·**key **(HWTACACS scheme view)

·**secondary accounting**

·**vpn-instance **(HWTACACS scheme view)

**AAA \-- HWTACACS配置命令 \-- primary authentication (HWTACACS scheme view)**

------------------------------------------------------------------------

**[primary authentication**]命令用来配置主HWTACACS认证服务器。

**[undo primary authentication**]命令用来删除配置的主HWTACACS认证服务器

【命令】

**[primary authentication***ipv4-address*[\| **ipv6** *ipv6-address* } [ *port-number* \| **key** { **cipher** \| **simple** } *string* \| **single-connection** \| **vpn-instance** *vpn-instance-name* ] \*]

**[undo primary authentication**]

【缺省情况】]

未配置主HWTACACS认证服务器。

【视图】

HWTACACS方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv4-address*]：主HWTACACS认证服务器的IPv4地址。

**[ipv6*** ipv6-address*]：主HWTACACS认证服务器的IPv6地址。

*[port-number*]：主HWTACACS认证服务器的TCP端口号，取值范围为1～65535，缺省值为49。此端口号必须与服务器提供认证服务的端口号保持一致。

**[key **[{ **cipher** \| **simple** } *string*]]：与主HWTACACS认证服务器交互的认证报文的共享密钥。此共享密钥必须与服务器上配置的共享密钥保持一致。

·**cipher ***string*：以密文方式设置共享密钥。非FIPS模式下，*string*为1～373个字符的密文字符串，区分大小写；FIPS模式下，*string*为15～373个字符的密文字符串，区分大小写。

·**simple ***string*：以明文方式设置共享密钥。非FIPS模式下，*string*为1～255个字符的明文字符串，区分大小写；FIPS模式下，*string*为15～255个字符的明文字符串，区分大小写，密钥元素的最少组合类型为4（必须包括数字、大写字母、小写字母以及特殊字符）。

**[single-connection**]：所有与主HWTACACS认证服务器交互的计费报文使用同一个TCP连接。如果未指定本参数，则表示向主HWTACACS计费服务器发送计费报文都会使用一个新的TCP连接。

**[vpn-instance ***vpn-instance-name*]：主HWTACACS认证服务器所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。如果未指定本参数，则表示主HWTACACS认证服务器位于公网中。

【使用指导】

在同一个方案中指定的主认证服务器和从认证服务器的IP地址、端口号和VPN参数不能完全相同。

若服务器位于MPLS VPN私网中，为保证HWTACACS报文被发送到指定的私网服务器，必须指定服务器所属的VPN实例名称。本命令指定的服务器所属的VPN比HWTACACS方案所属的VPN优先级高。

只有在设备与认证服务器没有报文交互时，才允许删除该服务器。认证服务器删除后，只对之后的认证过程有影响。

以明文或密文方式设置的共享密钥，均以密文的方式保存在配置文件中。

配置**single-connection**参数后可节省TCP连接资源，但有些TACACS服务器不支持这种方式，需要根据服务器支持情况进行配置。在服务器支持这种方式的情况下，建议配置**single-connection**参数，以提高性能和效率。

【举例】

\# 配置主HWTACACS认证服务器的IP地址为10.163.155.13，使用TCP端口49与HWTACACS认证服务器通信，认证报文的共享密钥为明文123456TESTauth&!。

\<Sysname\> system-view

Sysname hwtacacs scheme hwt1

Sysname-hwtacacs-hwt1 primary authentication 10.163.155.13 49 key simple 123456TESTauth&!

【相关命令】

·**display hwtacacs scheme**

·**key **(HWTACACS scheme view)

·**secondary authentication**

·**vpn-instance **(HWTACACS scheme view)

**AAA \-- HWTACACS配置命令 \-- primary authorization**

------------------------------------------------------------------------

**[primary authorization**]命令用来配置主HWTACACS授权服务器。

**[undo primary authorization**]命令用来删除配置的主HWTACACS授权服务器。

【命令】

**[primary authorization*****ipv4-address*[\| **ipv6** *ipv6-address* } [ *port-number* \| **key** { **cipher** \| **simple** } *string* \| **single-connection** \| **vpn-instance** *vpn-instance-name* ] \*]

**[undo primary authorization**]

【缺省情况】]

未配置主HWTACACS授权服务器。

【视图】

HWTACACS方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv4-address*]：主HWTACACS授权服务器的IPv4地址。

**[ipv6*** ipv6-address*]：主HWTACACS授权服务器的IPv6地址。

*[port-number*]：主HWTACACS授权服务器的TCP端口号，取值范围为1～65535，缺省值为49。此端口号必须与服务器提供授权服务的端口号保持一致。

**[key**[ { **cipher** \| **simple** } *string*]]：与主HWTACACS授权服务器交互的授权报文的共享密钥。此共享密钥必须与服务器上配置的共享密钥保持一致。

·**cipher ***string*：以密文方式设置共享密钥。非FIPS模式下，*string*为1～373个字符的密文字符串，区分大小写；FIPS模式下，*string*为15～373个字符的密文字符串，区分大小写。

·**simple ***string*：以明文方式设置共享密钥。非FIPS模式下，*string*为1～255个字符的明文字符串，区分大小写； FIPS模式下，*string*为15～255个字符的明文字符串，区分大小写，密钥元素的最少组合类型为4（必须包括数字、大写字母、小写字母以及特殊字符）。

**[single-connection**]：所有与主HWTACACS授权服务器交互的授权报文使用同一个TCP连接。如果未指定本参数，则表示每次授权都会使用一个新的TCP连接。

**[vpn-instance ***vpn-instance-name*]：主HWTACACS授权服务器所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。如果未指定本参数，则表示主HWTACACS授权服务器位于公网中。

【使用指导】

在同一个方案中指定的主授权服务器和从授权服务器的IP地址、端口号和VPN参数不能完全相同。

若服务器位于MPLS VPN私网中，为保证HWTACACS报文被发送到指定的私网服务器，必须指定服务器所属的VPN实例名称。本命令指定的服务器所属的VPN比HWTACACS方案所属的VPN优先级高。

只有在设备与授权服务器没有报文交互时，才允许删除该服务器。授权服务器删除后，只对之后的授权过程有影响。

以明文或密文方式设置的共享密钥，均以密文的方式保存在配置文件中。

配置**single-connection**参数后可节省TCP连接资源，但有些TACACS服务器不支持这种方式，需要根据服务器支持情况进行配置。在服务器支持这种方式的情况下，建议配置**single-connection**参数，以提高性能和效率。

【举例】

\# 配置主HWTACACS授权服务器的IP地址为10.163.155.13，使用TCP端口49与HWTACACS授权服务器通信，授权报文的共享密钥为明文123456TESTautr&!。

\<Sysname\> system-view

Sysname hwtacacs scheme hwt1

Sysname-hwtacacs-hwt1 primary authorization 10.163.155.13 49 key simple 123456TESTautr&!

【相关命令】

·**display hwtacacs scheme**

·**key **(HWTACACS scheme view)

·**secondary authorization**

·**vpn-instance **(HWTACACS scheme view)

**AAA \-- HWTACACS配置命令 \-- reset hwtacacs statistics**

------------------------------------------------------------------------

**[reset hwtacacs statistics**]命令用来清除HWTACACS协议的统计信息。

【命令】

**[reset hwtacacs statistics **[{ **accounting** \| **all** \| **authentication** \| **authorization** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[accounting**]：清除HWTACACS协议关于计费的统计信息。

**[all**]：清除HWTACACS的所有统计信息。

**[authentication**]：清除HWTACACS协议关于认证的统计信息。

**[authorization**]：清除HWTACACS协议关于授权的统计信息。

【举例】

\# 清除HWTACACS协议的所有统计信息。

\<Sysname\> reset hwtacacs statistics all

【相关命令】

·**display hwtacacs scheme**

**AAA \-- HWTACACS配置命令 \-- secondary accounting (HWTACACS scheme view)**

------------------------------------------------------------------------

**[secondary accounting**]命令用来配置从HWTACACS计费服务器。

**[undo secondary accounting**]命令用来删除指定的从HWTACACS计费服务器。

【命令】

**[secondary accounting***ipv4-address*[\| **ipv6** *ipv6-address* } [ *port-number* \| **key** { **cipher** \| **simple** } *string* \| **single-connection** \| **vpn-instance** *vpn-instance-name* ] \*]

**[undo secondary accounting **\*[ipv4-address*[\| **ipv6** *ipv6-address* } [ *port-number* \| **vpn-instance** *vpn-instance-name* ] \* ]]

【缺省情况】]

未配置从]HWTACACS计费服务器。

【视图】

HWTACACS方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv4-address*]：从HWTACACS计费服务器的IPv4地址。

**[ipv6*** ipv6-address*]：从HWTACACS计费服务器的IPv6地址

*[port-number*]：从HWTACACS计费服务器的端口号，取值范围为1～65535，缺省值为49。此端口号必须与服务器提供计费服务的端口号保持一致。

**[key**[ { **cipher** \| **simple** } *string*]]：与从HWTACACS计费服务器交互的计费报文的共享密钥。此共享密钥必须与服务器上配置的共享密钥保持一致。

·**cipher ***string*：以密文方式设置共享密钥。非FIPS模式下，*string*为1～373个字符的密文字符串，区分大小写；FIPS模式下，*string*为15～373个字符的密文字符串，区分大小写。

·**simple ***string*：以明文方式设置共享密钥。非FIPS模式下，*string*为1～255个字符的明文字符串，区分大小写；FIPS模式下，*string*为15～255个字符的明文字符串，区分大小写，密钥元素的最少组合类型为4（必须包括数字、大写字母、小写字母以及特殊字符）。

**[single-connection**]：所有与从HWTACACS计费服务器交互的计费报文使用同一个TCP连接。如果未指定本参数，则表示每次计费都会使用一个新的TCP连接。

**[vpn-instance ***vpn-instance-name*]：从HWTACACS计费服务器所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。如果未指定本参数，则表示从HWTACACS计费服务器位于公网中。

【使用指导】

可通过多次执行本命令，配置多个从HWTACACS计费服务器。当主服务器不可达时，设备根据从服务器的配置顺序由先到后查找状态为**active**的从服务器并与之交互。每个HWTACACS方案中最多支持配置16个从HWTACACS计费服务器。

需要注意的是：

·如果不指定任何参数，则**undo**命令将删除所有从计费服务器。

·在同一个方案中指定的主计费服务器和从计费服务器的IP地址、端口号和VPN参数不能完全相同，并且各从计费服务器的IP地址、端口号和VPN参数也不能完全相同。

·若服务器位于MPLS VPN私网中，为保证HWTACACS报文被发送到指定的私网服务器，必须指定服务器所属的VPN实例名称。本命令指定的服务器所属的VPN比HWTACACS方案所属的VPN优先级高。

·只有在设备与计费服务器没有报文交互时，才允许删除该服务器。计费服务器删除后，只对之后的计费过程有影响。

·以明文或密文方式设置的共享密钥，均以密文的方式保存在配置文件中。

·配置**single-connection**参数后可节省TCP连接资源，但有些TACACS服务器不支持这种方式，需要根据服务器支持情况进行配置。在服务器支持这种方式的情况下，建议配置**single-connection**参数，以提高性能和效率。

【举例】

\# 配置从HWTACACS计费服务器的IP地址为10.163.155.12，使用TCP端口49与HWTACACS计费服务器通信，计费报文的共享密钥为明文123456TESTacct&!。

\<Sysname\> system-view

Sysname hwtacacs scheme hwt1

Sysname-hwtacacs-hwt1 secondary accounting 10.163.155.12 49 key simple 123456TESTacct&!

【相关命令】

·**display hwtacacs scheme**

·**key **(HWTACACS scheme view)

·**primary accounting**

·**vpn-instance **(HWTACACS scheme view)

**AAA \-- HWTACACS配置命令 \-- secondary authentication (HWTACACS scheme view)**

------------------------------------------------------------------------

**[secondary authentication**]命令用来配置从HWTACACS认证服务器。

**[undo secondary authentication**]命令用来删除指定的从HWTACACS认证服务器。

【命令】

**[secondary authentication***ipv4-address*[\| **ipv6** *ipv6-address* } [ *port-number* I **key** { **cipher** \| **simple** } *string* \| **single-connection** \| **vpn-instance** *vpn-instance-name* ] \*]

**[undo secondary authentication **\*[ipv4-address*[\| **ipv6** *ipv6-address* } [ *port-number* \| **vpn-instance** *vpn-instance-name* ]\* ]]

【缺省情况】]

未配置从]HWTACACS认证服务器。

【视图】

HWTACACS方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv4-address*]：从HWTACACS认证服务器的IPv4地址。

**[ipv6*** ipv6-address*]：从HWTACACS认证服务器的IPv6地址。

*[port-number*]：从HWTACACS认证服务器的TCP端口号，取值范围为1～65535，缺省值为49。此端口号必须与服务器提供认证服务的端口号保持一致。

**[key**[  { **cipher** \| **simple** } *string*]]：与从HWTACACS认证服务器交互的认证报文的共享密钥。此共享密钥必须与服务器上配置的共享密钥保持一致。

·**cipher ***string*：以密文方式设置共享密钥。非FIPS模式下，*string*为1～373个字符的密文字符串，区分大小写；FIPS模式下，*string*为15～373个字符的密文字符串，区分大小写。

·**simple ***string*：以明文方式设置共享密钥。非FIPS模式下，*string*为1～255个字符的明文字符串，区分大小写；FIPS模式下，*string*为15～255个字符的明文字符串，区分大小写，密钥元素的最少组合类型为4（必须包括数字、大写字母、小写字母以及特殊字符）。

**[single-connection**]：所有与从HWTACACS认证服务器交互的认证报文使用同一个TCP连接。如果未指定本参数，则表示每次认证都会使用一个新的TCP连接。

**[vpn-instance ***vpn-instance-name*]：从HWTACACS认证服务器所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。如果未指定本参数，则表示从HWTACACS服务器位于公网中。

【使用指导】

可通过多次执行本命令，配置多个从HWTACACS认证服务器。当主服务器不可达时，设备根据从服务器的配置顺序由先到后查找状态为**active**的从服务器并与之交互。每个HWTACACS方案中最多支持配置16个从HWTACACS认证服务器。

需要注意的是：

·如果不指定任何参数，则**undo**命令命令将删除所有从认证服务器。

·在同一个方案中指定的主认证服务器和从认证服务器的IP地址、端口号和VPN参数不能完全相同，并且各从认证服务器的IP地址、端口号和VPN参数也不能完全相同。

·若服务器位于MPLS VPN私网中，为保证HWTACACS报文被发送到指定的私网服务器，必须指定服务器所属的VPN实例名称。本命令指定的服务器所属的VPN比HWTACACS方案所属的VPN优先级高。

·只有在设备与认证服务器没有报文交互时，才允许删除该服务器。认证服务器删除后，只对之后的认证过程有影响。

·以明文或密文方式设置的共享密钥，均以密文的方式保存在配置文件中。

·配置**single-connection**参数后可节省TCP连接资源，但有些TACACS服务器不支持这种方式，需要根据服务器支持情况进行配置。在服务器支持这种方式的情况下，建议配置**single-connection**参数，以提高性能和效率。

【举例】

\# 配置从HWTACACS认证服务器的IP地址为10.163.155.13，使用TCP端口49与HWTACACS认证服务器通信，认证报文的共享密钥为明文123456TESTauth&!。

\<Sysname\> system-view

Sysname hwtacacs scheme hwt1

Sysname-hwtacacs-hwt1 secondary authentication 10.163.155.13 49 key simple 123456TESTauth&!

【相关命令】

·**display hwtacacs scheme**

·**key **(HWTACACS scheme view)

·**primary authentication**

·**vpn-instance **(HWTACACS scheme view)

**AAA \-- HWTACACS配置命令 \-- secondary authorization**

------------------------------------------------------------------------

**[secondary authorization**]命令用来配置从HWTACACS授权服务器。

**[undo secondary authorization**]命令用来删除指定的从HWTACACS授权服务器。

【命令】

**[secondary authorization*****ipv4-address*[\| **ipv6** *ipv6-address* } [ *port-number* I **key** { **cipher** \| **simple** } *string* \| **single-connection** \| **vpn-instance** *vpn-instance-name* ] \*]

**[undo secondary authorization **\*[ipv4-address*[\| **ipv6** *ipv6-address* } [ *port-number* \| **vpn-instance** *vpn-instance-name* ]\* ]]

【缺省情况】]

未配置从]HWTACACS授权服务器。

【视图】

HWTACACS方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv4-address*]：从HWTACACS授权服务器的IPv4地址。

**[ipv6**]*ipv6-address*：从HWTACACS授权服务器的IPv6地址。

*[port-number*]：从HWTACACS授权服务器的TCP端口号，取值范围为1～65535，缺省为49。此端口号必须与服务器提供授权服务的端口号保持一致。

**[key**  { **cipher** \| **simple** } *string*]：与从HWTACACS授权服务器交互的授权报文的共享密钥。此共享密钥必须与服务器上配置的共享密钥保持一致。

·**cipher ***string*：以密文方式设置共享密钥。非FIPS模式下，为1～373个字符的密文字符串，区分大小写； FIPS模式下，*string*为15～373个字符的密文字符串，区分大小写。

·**simple ***string*：以明文方式设置共享密钥。非FIPS模式下，为1～255个字符的明文字符串，区分大小写， FIPS模式下，*string*为15～255个字符的明文字符串，区分大小写，密钥元素的最少组合类型为4（必须包括数字、大写字母、小写字母以及特殊字符）。

**[single-connection**]：所有与从HWTACACS授权服务器交互的授权报文使用同一个TCP连接。如果未指定本参数，则表示每次授权都会使用一个新的TCP连接。

**[vpn-instance ***vpn-instance-name*]：从HWTACACS授权服务器所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。如果未指定本参数，则表示从HWTACACS授权服务器位于公网中。

【使用指导】

可通过多次执行本命令，配置多个从HWTACACS授权服务器。当主服务器不可达时，设备根据从服务器的配置顺序由先到后查找状态为**active**的从服务器并与之交互。每个HWTACACS方案中最多支持配置16个从HWTACACS授权服务器。

需要注意的是：

·如果不指定任何参数，则**undo**命令将删除所有从授权服务器。

·在同一个方案中指定的主授权服务器和从授权服务器的IP地址、端口号和VPN参数不能完全相同，并且各从授权服务器的IP地址、端口号和VPN参数也不能完全相同。

·若服务器位于MPLS VPN私网中，为保证HWTACACS报文被发送到指定的私网服务器，必须指定服务器所属的VPN实例名称。本命令指定的服务器所属的VPN比HWTACACS方案所属的VPN优先级高。

·只有在设备与授权服务器没有报文交互时，才允许删除该服务器。授权服务器删除后，只对之后的授权过程有影响。

·以明文或密文方式设置的共享密钥，均以密文的方式保存在配置文件中。

·配置**single-connection**参数后可节省TCP连接资源，但有些TACACS服务器不支持这种方式，需要根据服务器支持情况进行配置。在服务器支持这种方式的情况下，建议配置**single-connection**参数，以提高性能和效率。

【举例】

\# 配置从HWTACACS授权服务器的IP地址为10.163.155.13，使用TCP端口49与HWTACACS授权服务器通信，授权报文的共享密钥为明文123456TESTautr&!。

\<Sysname\> system-view

Sysname hwtacacs scheme hwt1

Sysname-hwtacacs-hwt1 secondary authorization 10.163.155.13 49 key simple 123456TESTautr&!

【相关命令】

·**display hwtacacs scheme**

·**key **(HWTACACS scheme view)

·**primary authorization**

·**vpn-instance **(HWTACACS scheme view)

**AAA \-- HWTACACS配置命令 \-- timer quiet (HWTACACS scheme view)**

------------------------------------------------------------------------

**[timer quiet**]命令用来设置服务器恢复激活状态的时间。

**[undo timer quiet**]命令用来恢复缺省情况。

【命令】

**[timer quiet ***minutes*]

**[undo timer quiet**]

【缺省情况】

服务器恢复激活状态的时间为5分钟。

【视图】

HWTACACS方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[minutes*]：恢复激活状态的时间，取值范围为1～255，单位为分钟。

【举例】

\# 设置服务器恢复激活状态的时间为10分钟。

\<Sysname\> system-view

Sysname hwtacacs scheme hwt1

Sysname-hwtacacs-hwt1 timer quiet 10

【相关命令】

·**display hwtacacs scheme**

**AAA \-- HWTACACS配置命令 \-- timer realtime-accounting (HWTACACS scheme view)**

------------------------------------------------------------------------

**[timer realtime-accounting**]命令用来设置实时计费的时间间隔。

**[undo timer realtime-accounting**]命令用来恢复缺省情况。

【命令】

**[timer realtime-accounting ***minutes*]

**[undo timer realtime-accounting**]

【缺省情况】

实时计费的时间间隔为12分钟。

【视图】

HWTACACS方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[minutes*]：实时计费的时间间隔，取值范围为0～60，单位为分钟。0表示设备不向HWTACACS服务器发送在线用户的计费信息。

【使用指导】

为了对用户实施实时计费，有必要设置实时计费的时间间隔。在设置了该属性以后，每隔设定的时间，设备会向HWTACACS服务器发送一次在线用户的计费信息。

实时计费间隔的取值与HWTACACS服务器的性能和用户的数目有一定的关系。取值越小，对设备和HWTACACS服务器的性能要求越高。建议当用户量比较大（大于等于1000）时，尽量把该间隔的值设置得大一些。以下是实时计费间隔与用户量之间的推荐比例关系。

表1-8 实时计费间隔与用户量之间的推荐比例关系

用户数

实时计费间隔（分钟）

1～99

3

100～499

6

500～999

12

大于等于1000

大于等于15

****

【举例】

\# 将HWTACACS方案hwt1的实时计费的时间间隔设置为51分钟。

\<Sysname\> system-view

Sysname hwtacacs scheme hwt1

Sysname-hwtacacs-hwt1 timer realtime-accounting 51

【相关命令】

·**display hwtacacs scheme**

**AAA \-- HWTACACS配置命令 \-- timer response-timeout (HWTACACS scheme view)**

------------------------------------------------------------------------

**[timer response-timeout**]命令用来设置HWTACACS服务器响应超时时间。

**[undo timer response-timeout**]命令用来恢复缺省情况。

【命令】

**[timer response-timeout ***seconds*]

**[undo timer response-timeout**]

【缺省情况】

HWTACACS服务器响应超时时间为5秒。

【视图】

HWTACACS方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：HWTACACS服务器响应超时时间，取值范围为1～300，单位为秒。

【使用指导】

由于HWTACACS是基于TCP实现的，因此，服务器响应超时或TCP超时都可能导致与HWTACACS服务器的连接断开。

【举例】

\# 配置HWTACACS服务器响应超时时间为30秒。

\<Sysname\> system-view

Sysname hwtacacs scheme hwt1

Sysname-hwtacacs-hwt1 timer response-timeout 30

【相关命令】

·**display hwtacacs scheme**

**AAA \-- HWTACACS配置命令 \-- user-name-format (HWTACACS scheme view)**

------------------------------------------------------------------------

**[user-name-format**]命令用来设置发送给HWTACACS服务器的用户名格式。

**[undo user-name-format**]命令用来恢复缺省情况。

【命令】

**[user-name-format**[ { **keep-original** \| **with-domain** \| **without-domain** }]]

**[undo user-name-format**]

【缺省情况】

设备发送给HWTACACS服务器的用户名携带有ISP域名。

【视图】

HWTACACS方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[keep-original**]：发送给HWTACACS服务器的用户名与用户输入的保持一致。

**[with-domain**]：发送给HWTACACS服务器的用户名带ISP域名。

**[without-domain**]：发送给HWTACACS服务器的用户名不带ISP域名。

【使用指导】

接入用户通常以"*userid@isp-name*"的格式命名，"*@*"后面的部分为ISP域名，设备就是通过该域名来决定将用户归于哪个ISP域的。但是，有些HWTACACS服务器不能接受携带有ISP域名的用户名，在这种情况下，有必要将用户名中携带的域名去除后再传送给HWTACACS服务器。因此，设备提供此命令以指定发送给HWTACACS服务器的用户名是否携带有ISP域名。

需要注意的是：

·如果指定某个HWTACACS方案不允许用户名中携带有ISP域名，那么请不要在两个乃至两个以上的ISP域中同时设置使用该HWTACACS方案。否则，会出现虽然实际用户不同（在不同的ISP域中），但HWTACACS服务器认为用户相同（因为传送到它的用户名相同）的错误。

·若接入用户为需要漫游的无线用户，接入设备上将发送给HWTACACS服务器的用户名格式配置为**keep-original**类型，否则可能导致这类用户认证失败。

【举例】

\# 指定发送给HWTACACS方案hwt1的用户不带ISP域名。

\<Sysname\> system-view

Sysname hwtacacs scheme hwt1

Sysname-hwtacacs-hwt1 user-name-format without-domain

【相关命令】

·**display hwtacacs scheme**

**AAA \-- HWTACACS配置命令 \-- vpn-instance (HWTACACS scheme view)**

------------------------------------------------------------------------

![说明](AAA命令.files/image001.png)

本命令的支持请与设备的型号有关，请以设备的实际情况为准。

****

**[vpn-instance**]命令用来配置HWTACACS方案所属的VPN。

**[undo vpn-instance**]命令用来恢复缺省情况。

【命令】

**[vpn-instance ***vpn-instance-name*]

**[undo vpn-instance**]

【缺省情况】

HWTACACS方案属于公网。

【视图】

HWTACACS方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vpn-instance-name*]：MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。

【使用指导】

本命令配置的VPN对于该方案下的所有HWTACACS认证/授权/计费服务器生效，但设备优先使用配置认证/授权/计费服务器时指定的各服务器所属的VPN。

【举例】

\# 配置HWTACACS方案hw1所属的VPN为test。

\<Sysname\> system-view

Sysname hwtacacs scheme hwt1

Sysname-hwtacacs-hwt1 vpn-instance test

【相关命令】

·**display hwtacacs scheme**

**AAA \-- LDAP配置命令 \-- attribute-map**

------------------------------------------------------------------------

**[attribute-map**]命令用来在LDAP方案中引用LDAP属性映射表。

**[undo attribute-map**]命令用来删除引用的指定LDAP属性映射表。

【命令】

**attribute-map**{.ItemListCharChar} *map-name*

**undo attribute-map**{.ItemListCharChar}

【缺省情况】

未引用任何LDAP属性映射表。

【视图】

LDAP方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[map-name*]：表示LDAP属性映射表名，为1～31个字符的字符串，不区分大小写。

【使用指导】

在使用LDAP授权方案的情况下，可以通过在LDAP方案中引用LDAP属性映射表，将LDAP授权服务器下发给用户的LDAP属性映射为AAA模块可以解析的某类属性。

一个LDAP方案视图中只能引用一个LDAP属性映射表，后配置的生效。

如果在LDAP授权过程中修改了引用的LDAP属性映射表，或者修改了引用的LDAP属性映射表的内容，则该修改对当前的授权过程不会生效，只对修改后新的LDAP授权过程生效。

【举例】

\# 在LDAP方案test中引用名称为map1的LDAP属性映射表。

\<Sysname\> system-view

Sysname ldap scheme test

Sysname-ldap-test attribute-map map1

【相关命令】

·**display ldap-scheme**

·**ldap attribute-map**

**AAA \-- LDAP配置命令 \-- authentication-server**

------------------------------------------------------------------------

**[authentication-server**]命令用来指定LDAP认证服务器。

**[undo authentication-server**]命令用来删除指定的LDAP认证服务器。

【命令】

**[authentication-server ***server-name*]

**[undo authentication-server**]

【缺省情况】

未指定LDAP认证服务器。

【视图】

LDAP方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[server-name*]：LDAP服务器的名称，为1～64个字符的字符串，不区分大小写。该服务器必须已经存在。

【使用指导】

一个LDAP方案视图下仅能指定一个LDAP认证服务器，如果重复执行此命令，新的配置将覆盖原来的配置。

【举例】

\# 指定LDAP认证服务器为ccc。

\<Sysname\> system-view

Sysname ldap scheme ldap1

Sysname-ldap-ldap1 authentication-server ccc

【相关命令】

·**display ldap scheme**

·**ldap server**

**AAA \-- LDAP配置命令 \-- authorization-server**

------------------------------------------------------------------------

**[authorization-server**]命令用来指定LDAP授权服务器。

**[undo authorization-server**]命令用来删除指定的LDAP授权服务器。

【命令】

**[authorization-server ***server-name*]

**[undo authorization-server**]

【缺省情况】

未指定LDAP授权服务器。

【视图】

LDAP方案视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[server-name*]：LDAP服务器的名称，为1～64个字符的字符串，不区分大小写。该服务器必须已经存在。

【使用指导】

一个LDAP方案视图下仅能指定一个LDAP授权服务器，如果重复执行此命令，新的配置将覆盖原来的配置。

【举例】

\# 指定LDAP授权服务器为ccc。

\<Sysname\> system-view

Sysname ldap scheme ldap1

Sysname-ldap-ldap1 authorization-server ccc

【相关命令】

·**display ldap scheme**

·**ldap server**

**AAA \-- LDAP配置命令 \-- display ldap scheme**

------------------------------------------------------------------------

**[display ldap scheme**]命令用来查看LDAP方案的配置信息。

【命令】

**[display ldap scheme** [ *scheme-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[scheme-name*]：指定LDAP方案名，为1～32个字符的字符串，不区分大小写。

【使用指导】

如果不指定LDAP方案名，则显示所有LDAP方案的配置信息。

【举例】

\# 查看所有LDAP方案的配置信息。

\<Sysname\> display ldap scheme

Total 1 LDAP schemes

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

LDAP scheme name             : aaa

  Authentication server      : aaa

    IP                       : 1.1.1.1

    Port                     : 111

    VPN instance             : Not configured

    LDAP protocol version    : LDAPv3

    Server timeout interval  : 10 seconds

    Login account DN         : Not configured

    Base DN                  : Not configured

    Search scope             : all-level

    User searching parameters:

      User object class      : Not configured

      Username attribute     : cn

      Username format        : with-domain

  Authorization server       : aaa

    IP                       : 1.1.1.1

    Port                     : 111

    VPN instance             : Not configured

    LDAP protocol version    : LDAPv3

    Server timeout interval  : 10 seconds

    Login account DN         : Not configured

    Base DN                  : Not configured

    Search scope             : all-level

    User searching parameters:

      User object class      : Not configured

      Username attribute     : cn

      Username format        : with-domain

  Attribute map              : map1

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

表1-9 display ldap scheme命令显示信息描述表

字段

描述

Total 1 LDAP schemes

总共有1个LDAP方案

LDAP Scheme Name

LDAP方案名称

Authentication Server

LDAP认证服务器名称

未配置时，显示为Not configured

Authorization server

LDAP授权服务器名字

未配置时，显示为Not configured

IP

LDAP认证服务器的IP地址

未配置认证服务器IP时，IP地址显示为Not configured

Port

LDAP认证服务器的端口号

未配置认证服务器IP时，端口号显示为缺省值

VPN Instance

VPN实例名称

未配置时，显示为Not configured

LDAP Protocol Version

LDAP协议的版本号（LDAPv2、LDAPv3）

Server Timeout Interval

LDAP服务器连接超时时间（单位为秒）

Login Account DN

管理员用户的DN

Base DN

用户DN查询的起始DN

Search Scope

用户DN查询的范围（all-level：所有子目录查询，single-level：下级目录查询）

User Searching Parameters

用户查询参数

User Object Class

查询用户DN时使用的用户对象类型

未配置时，显示为Not configured

Username Attribute

用户登录帐号的属性类型

Username Format

发送给服务器的用户名格式

Attribute map

引用的LDAP属性映射表名称

未配置时，显示为Not configured

**AAA \-- LDAP配置命令 \-- ip**

------------------------------------------------------------------------

**[ip**]命令用来配置LDAP服务器的IP地址。

**[undo ip**]命令用来删除配置的LDAP服务器IP地址。

【命令】

**[ip ***ip-address***** **port** *port-number* ]  **vpn-instance** *vpn-instance-name*

**[undo ip**]

【缺省情况】

未配置LDAP服务器的IP地址。

【视图】

LDAP服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：LDAP服务器的IP地址。

**[port ***port-number*]：LDAP服务器所使用的TCP端口号，取值范围为1～65535，缺省值为389。

**[vpn-instance*** vpn-instance-name*]：LDAP服务器所属的VPN。*vpn-instance-name*表示MPLS L3VPN实例的名称，为1～31个字符的字符串，区分大小写。不指定该参数时，表示LDAP服务器属于公网。

【使用指导】

需要注意的是：

·需保证设备上的LDAP服务端口与LDAP服务器上使用的端口设置一致。

·更改后的服务器IP地址和端口号，只对更改之后进行的LDAP认证生效。

【举例】

\# 配置LDAP服务器的IP地址为192.168.0.10，端口号为4300。

\<Sysname\> system-view

Sysname ldap server ccc

Sysname-ldap-server-ccc ip 192.168.0.10 port 4300

【相关命令】

·**ldap server**

**AAA \-- LDAP配置命令 \-- ipv6**

------------------------------------------------------------------------

**[ipv6**]命令用来配置LDAP服务器的IPv6地址。

**[undo ipv6**]命令用来删除配置的LDAP服务器IPv6地址。

【命令】

**[ipv6 ***ipv6-address* [ **port** *port-number*   **vpn-instance** *vpn-instance-name* ]]

**[undo ipv6**]

【缺省情况】

缺省情况下，未配置LDAP服务器的IP地址。

【视图】

LDAP服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：LDAP服务器的IPv6地址。

**[port ***port-number*]：LDAP服务器所使用的TCP端口号，取值范围为1～65535，缺省值为389。

**[vpn-instance*** vpn-instance-name*]：LDAP服务器所属的VPN。*vpn-instance-name*表示MPLS L3VPN实例的名称，为1～31个字符的字符串，区分大小写。不指定该参数时，表示LDAP服务器属于公网。

【使用指导】

需保证设备上的LDAP服务端口与LDAP服务器上使用的端口设置一致。

更改后的服务器IP地址和端口号，只对更改之后的LDAP认证生效。

【举例】

\# 配置LDAP服务器的IPv6地址为1:2::3:4，端口号为4300。

\<Sysname\> system-view

Sysname ldap server ccc

Sysname-ldap-server-ccc ipv6 1:2::3:4 port 4300

【相关命令】

·**ldap server**

**AAA \-- LDAP配置命令 \-- ldap attribute-map**

------------------------------------------------------------------------

**[ldap attribute-map**]命令用来创建LDAP的属性映射表，并进入属性映射表视图。

**[undo ldap attribute-map**]命令用来删除指定的LDAP属性映射表。

【命令】

**ldap attribute-map**{.ItemListCharChar} *map-name*

**undo ldap attribute-map**{.ItemListCharChar}* map-name*

【缺省情况】

不存在LDAP属性映射表。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[map-name*]：表示LDAP属性映射表的名称，为1～31个字符的字符串，不区分大小写。

【使用指导】

一个LDAP的属性映射表中可以添加多个LDAP属性映射表项，每个表项表示一个LDAP 属性和一个AAA属性的映射关系。

可以通过多次执行本命令配置多个LDAP的属性映射表。

【举例】

\# 添加名称为map1的LDAP属性映射表。

\<Sysname\> system-view

Sysname ldap attribute-map map1

Sysname-ldap-map-map1

【相关命令】

·**attribute-map**

·**ldap scheme**

·**map**

**AAA \-- LDAP配置命令 \-- ldap scheme**

------------------------------------------------------------------------

**[ldap scheme**]命令用来创建LDAP方案，并进入LDAP方案视图。

**[undo ldap scheme**]命令用来删除指定的LDAP方案。

【命令】

**[ldap scheme**] *ldap-scheme-name*

**[undo ldap scheme**] *ldap-scheme-name*

【缺省情况】

未定义LDAP方案。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ldap-scheme-name*]：LDAP方案名，为1～32个字符的字符串，不区分大小写。

【使用指导】

一个LDAP方案可以同时被多个ISP域引用。

系统最多支持配置16个LDAP方案。

【举例】

\# 创建名为ldap1的LDAP方案并进入其视图。

\<Sysname\> system-view

Sysname ldap scheme ldap1

Sysname-ldap-ldap1

【相关命令】

·**display ldap scheme**

**AAA \-- LDAP配置命令 \-- ldap server**

------------------------------------------------------------------------

**[ldap server**]用来创建LDAP服务器并进入LDAP服务器视图。

**[undo ldap server**]命令用来删除配置的LDAP服务器。

【命令】

**[ldap server ***server-name*]

**[undo ldap server ***server-name*]

【缺省情况】

不存在LDAP服务器。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[server-name*]：LDAP服务器的名称，为1～64个字符的字符串，不区分大小写。

【举例】

\# 创建LDAP服务器ccc并进入其视图。

\<Sysname\> system-view

Sysname ldap server ccc

Sysname-ldap-server-ccc

【相关命令】

·**display ldap scheme**

**AAA \-- LDAP配置命令 \-- login-dn**

------------------------------------------------------------------------

**[login-dn**]命令用来配置具有管理员权限的用户DN。

**[undo login-dn**]命令用来删除已配置的具有管理员权限的用户DN。

【命令】

**[login-dn ***dn-string*]

**[undo login-dn**]

【缺省情况】

未配置具有管理员权限的用户DN。

【视图】

LDAP服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dn-string*]：具有管理员权限的用户DN，是绑定服务器时使用的用户标识名，为1～255个字符的字符串，不区分大小写。

【使用指导】

需要注意的是：

·设备上的管理员DN必须与服务器上管理员的DN一致。

·更改后的管理员DN，只对更改之后的LDAP认证生效。

【举例】

\# 配置管理员权限的用户DN为uid=test, ou=people, o=example, c=city。

\<Sysname\> system-view

Sysname ldap server ldap1

Sysname-ldap-server-ldap1 login-dn uid=test,ou=people,o=example,c=city

【相关命令】

·**display ldap scheme**

**AAA \-- LDAP配置命令 \-- login-password**

------------------------------------------------------------------------

**[login-password**]命令用来配置LDAP认证中，绑定服务器时所使用的具有管理员权限的用户密码。

**[undo login-password**]命令用来恢复缺省情况。

【命令】

**[login-password**[ { **cipher** *\|* **simple** } *password*]]

**[undo login-password**]

【缺省情况】

未配置具有管理权限的用户密码。

【视图】

LDAP服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cipher**]：表示以密文方式设置用户密码。

**[simple**]：表示以明文方式设置用户密码。

*[string*]：设置的明文密码或密文密码，区分大小写。明文密码为1～128个字符的字符串；密文密码为1～201个字符的字符串。

【使用指导】

该命令只有在配置了**login-dn**的情况下生效。当未配置**login-dn**时，该命令不生效。

以明文或密文方式设置的用户密码，均以密文的方式保存在配置文件中。

【举例】

\# 配置具有管理员权限的用户密码为明文abcdefg。

\<Sysname\> system-view

Sysname ldap server ccc

Sysname-ldap-server-ccc login-password simple abcdefg

【相关命令】

·**display ldap scheme**

·**login-dn**

**AAA \-- LDAP配置命令 \-- map**

------------------------------------------------------------------------

**[map**]命令用来配置LDAP属性映射表项，即将一个LDAP服务器的属性映射为一个AAA的属性。

**[undo map**]命令用来删除指定的LDAP属性映射表项。

【命令】

**[map ldap-attribute ***ldap-attribute-name* [ **prefix** *prefix-value* **delimiter** *delimiter-value*  **aaa-attribute** { **user-group** \| **user-profile** }]]

**[undo map** [ **ldap-attribute** *ldap-**attribute-name* ]]

【缺省情况】

未指定LDAP属性映射关系。

【视图】

LDAP属性映射表视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ldap-attribute ***ldap-attribute-name*]：表示要映射的LDAP属性。其中，*ldap-attribute-name*表示LDAP属性名称，为1～63个字符的字符串，不区分大小写。

**[prefix** *prefix-value* **delimiter** *delimiter-value*]：表示按照一定的格式提取LDAP属性字符串中的内容映射为AAA属性。其中，*prefix-value*表示LDAP属性字符串中的某内容前缀（例如cn=），为1～7个字符的字符串，不区分大小写；*delimiter-value*表示LDAP属性字符串中的内容分隔符（例如逗号）。若不指定该可选参数，则表示要将一个完整的LDAP属性字符串映射为指定的AAA属性。

**[aaa-attribute** *aaa-attribute-name*]：表示要映射为的AAA属性。其中，*aaa-attribute-name*表示AAA属性名称，为1～63个字符的字符串，不区分大小写。

**[user-group**]：表示User group类型的AAA属性。

**[user-profile**]：表示User Profile类型的AAA属性。

【使用指导】

在用户的LDAP授权过程中，设备会通过查询操作得到用户的授权信息，该授权信息由LDAP服务器通过若干LDAP属性下发给设备。若设备从LDAP服务器查询得到某LDAP属性，则该属性只有在被设备的AAA模块解析之后才能实际生效。如果某LDAP服务器下发给用户的属性不能被AAA模块解析，则该属性将被忽略。因此，需要通过本命令指定要获取哪些LDAP属性，以及LDAP服务器下发的这些属性将被AAA模块解析为什么类型的AAA属性，具体映射为

哪种类型的AAA属性由实际应用需求决定。

一个LDAP服务器属性只能映射为一个AAA属性，但不同的LDAP服务器属性可映射为同一个AAA属性。

【举例】

\# 配置将LDAP服务器属性memberof按照前缀为cn=、分隔符为逗号（,）的格式提取出的内容映射成AAA属性User group。

\<Sysname\> system-view

Sysname ldap attribute-map ccc

Sysname-ldap-map-ccc map ldap-attribute memberof prefix cn= delimiter ; aaa-attribute user-group

【相关命令】

·**ldap attribute-map**

·**user-group**

·**user-profile**（安全命令参考/User Profile）

**AAA \-- LDAP配置命令 \-- protocol-version**

------------------------------------------------------------------------

**[protocol-version**]命令用来配置LDAP认证中所支持的LDAP协议的版本号。

**[undo protocol-version**]命令用来恢复缺省情况。

【命令】

**[protocol-version**  { **v2** \| **v3** }]

**[undo protocol-version**]

【缺省情况】

LDAP版本号为LDAPv3。

【视图】

LDAP服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[v2**]：表示LDAP协议版本号为LDAPv2。

**[v3**]：表示LDAP协议版本号为LDAPv3。

【使用指导】

为保证LDAP认证成功，请保证设备上的LDAP版本号与LDAP服务器上使用的版本号一致。

更改后的服务器版本号，只对更改之后的LDAP认证生效。

Microsoft的LDAP服务器只支持LDAPv3，配置LDAP版本为v2时无效。

【举例】

\# 配置LDAP协议版本号为LDAPv2。

\<Sysname\> system-view

Sysname ldap server ccc

Sysname-ldap-server-ccc protocol-version v2

【相关命令】

·**display ldap scheme**

**AAA \-- LDAP配置命令 \-- search-base-dn**

------------------------------------------------------------------------

**[search-base-dn**]命令用来配置用户查询的起始DN。

**[undo search-base-dn**]命令用来恢复缺省情况。

【命令】

**[search-base-dn ***base-dn*]

**[undo search-base-dn**]

【缺省情况】

未指定用户查询的起始DN。

【视图】

LDAP服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[base-dn*]：表示查询待认证用户的起始DN。*base-dn*表示起始DN的值，为1～255个字符的字符串，不区分大小写。

【举例】

\# 配置用户查询的起始DN为dc=ldap,dc=com。

\<Sysname\> system-view

Sysname ldap server ccc

Sysname-ldap-server-ccc search-base-dn dc=ldap,dc=com

【相关命令】

·**display ldap scheme**

·**ldap server**

**AAA \-- LDAP配置命令 \-- search-scope**

------------------------------------------------------------------------

**[search-scope**]命令用来配置用户查询的范围。

**[undo search-scope**]命令用来恢复缺省情况。

【命令】

**[search-scope **[{ **all-level** \| **single-level** }]]

**[undo search-scope**]

【缺省情况】

用户查询的范围为**all-level**。

【视图】

LDAP服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all-level**]：表示在起始DN的所有子目录下进行查询。

**[single-level**]：表示只在起始DN的下一级子目录下进行查询。

【举例】

\# 配置在起始DN的所有子目录下查询LDAP认证用户。

\<Sysname\> system-view

Sysname ldap server ccc

Sysname-ldap-server-ccc search-scope all-level

【相关命令】

·**display ldap scheme**

·**ldap server**

**AAA \-- LDAP配置命令 \-- server-timeout**

------------------------------------------------------------------------

**[server-timeout**]命令用来配置LDAP服务器连接超时时间，即认证、授权时等待LDAP服务器回应的最大时间。

**[undo server-timeout**]命令用来恢复缺省情况。

【命令】

**[server-timeout** *time-interval*]

**[undo server-timeout**]

【缺省情况】

LDAP服务器连接超时时间为10秒。

【视图】

LDAP服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time-interval*]：LDAP服务器连接超时时间，取值范围为5～20，单位为秒。

【使用指导】

更改后的连接超时时间，只对更改之后的LDAP认证生效。

【举例】

\# 配置LDAP服务器连接超时时间为15秒。

\<Sysname\> system-view

Sysname ldap server ccc

Sysname-ldap-server-ccc server-timeout 15

【相关命令】

·**display ldap scheme**

**AAA \-- LDAP配置命令 \-- user-parameters**

------------------------------------------------------------------------

**[user-parameters**]命令用来配置LDAP用户查询的属性参数，包括用户名属性、用户名格式和自定义用户对象类型。

**[undo user-parameters**]命令用来恢复缺省情况。

【命令】

**[user-parameters **[{ **user-name-attribute** { *name-attribute* \| **cn** \| **uid** } \| **user-name-format** { **with-domain** \| **without-domain** } \| **user-object-class** *object-class-name* }]]

**[undo user-parameters **[{ **user-name-attribute** \| **user-name-format** \| **user-object-class** }]]

【缺省情况】

**[user-name-attribute**]为**cn**；**user-name-format**为**without-domain**；未指定自定义**user-object-class**，根据使用的LDAP服务器的类型使用各服务器缺省的用户对象类型。

【视图】

LDAP服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[user-name-attribute **[{ *name-attribute* \| **cn** \| **uid** }]]：表示用户名的属性类型。其中，*name-attribute*表示属性类型值，为1～64个字符的字符串，不区分大小写；**cn**表示用户登录帐号的属性为cn（Common Name）；**uid**表示用户登录帐号的属性为uid（User ID）。

**[user-name-format**[ { **with-domain** \| **without-domain** }]]：表示发送给服务器的用户名格式。其中，**with-domain**表示发送给服务器的用户名带ISP域名；**without-domain**表示发送给服务器的用户名不带ISP域名。

**[user-object-class ***object-class-name*]：表示查询用户DN时使用的用户对象类型。其中，*object-class-name*表示对象类型值，为1～64个字符的字符串，不区分大小写。

【使用指导】

如果LDAP服务器上的用户名不包含域名，必须配置**user-name-format**为**without-domain**，将用户名的域名去除后再传送给LDAP服务器；如果包含域名则需配置**user-name-format**为**with-domain**。

【举例】

\# 配置用户对象类型为person。

\<Sysname\> system-view

Sysname ldap server ccc

Sysname-ldap-server-ccc user-parameters user-object-class person

【相关命令】

·**display ldap scheme**

·**login-dn**

**AAA \-- 本地话单缓存配置命令 \-- display local-bill**

------------------------------------------------------------------------

**[display local-bill**]命令用来显示缓存中指定的具体话单信息或者缓存中话单资源的使用情况。

【命令】

**[display local-bill **[{ **cache-usage** \| **verbose** *start-number* **count** *count* }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[cache-usage**]：查看本地缓存中话单资源的使用情况。

**[verbose**]：查看本地缓存中的具体话单信息。

*[start-number*]：指定显示话单的起始位置，取值范围为1～50000。

**[count*** count*]：连续显示的话单总数目，取值范围为1～100。

【使用指导】

查看本地缓存中的具体话单信息时，需要指定开始显示话单的位置*start-number*，即从第几个话单开始显示，以及从这个位置开始总共连续显示多少个话单数目。

【举例】

\# 从本地缓存的第一个话单开始显示连续2个话单的详细信息。

\<Sysname\> display local-bill verbose 1 count 2

Bill 1 details:

  Session ID  : 000000012013-05-21:18:04:02-12345678011

  User name   : user1@h3c

  Start time  : 2013-05-21 18:04:10

  Stop time   : 2013-05-21 18:05:35    Duration   : 0:01:35

  IP address  : 111.8.10.125           MAC address: 0016-ecb7-a879

  IPv6 address: N/A

  Service type: PPP                    Access type: PPP

  Interface   : Ethernet 1/1

  VLAN ID     : N/A

  Status      : Offline                Reason code: 6  Ref: 98

  User traffic:

    Received: 0            bytes, 0            packets

    Sent    : 0            bytes, 0            packets

Bill 2 details:

Session ID  : 000000012013-05-21:18:14:07-12341234011

User name   : user2

Start time  : 2013-05-21 18:14:15

Stop time   : 2013-05-21 18:15:35    Duration   : 0:01:20

IP address  : 111.8.10.124           MAC address: 0016-ec89-a8e9

IPv6 address: N/A

Service type: PPP                    Access type: PPP

Interface   : Ethernet 1/2

VLAN ID     : 100

Status      : Offline                Reason code: 6  Ref: 98

User traffic:

    Received: 0            bytes, 0            packets

    Sent    : 0            bytes, 0            packets

Total bills: 2.

表1-10 display local-bill verbose命令显示信息描述表

字段

描述

Bill 1 details

第n个话单的详细内容

Session ID

会话ID，用户的唯一标识

User name

用户名称

Start time

开始计费时间

Stop time

停止计费时间

Duration

用户在线时长

IP address

用户IP地址

MAC address

用户MAC地址

IPv6 address

用户IPv6地址

Service type

用户使用的服务类型

Access type

用户使用的接入类型

Interface

用户接入到设备的端口号

VLAN ID

用户接入的VLAN

Status

话单类型。目前只支持本地话单缓存，是在用户下线后才产生的话单

·Invalid：无效

·Realtime：实时计费话单

·Offline：下线话单

·CRC Failed：错误话单，即CRC校验错误的话单

Code

设备外部的下线原因代码。为按照RFC 2866远端计费提供的标准下线原因，具体请参考RFC 2866

Ref

设备内部的下线原因代码，作为外部下线原因的补充，提供更加详细的原因，一般无需使用

User traffic

用户流量统计信息，包括上行字节数、上行包数、下行字节数、下行包数

Received

下行流量，即用户收到报文的流量

Sent

上行流量，即用户发送出去的流量

Total bills

当前显示的话单总数

\#显示本地缓存中的话单资源的使用情况。

\<Sysname\> display local-bill cache-usage

Cache usage:

  Existing bills: 0         Available bills      : 50000

  Max bills     : 50000     Auto export threshold: 4000

  Bytes per bill: 448

表1-11 display local-bill cache-usage命令显示信息描述表

字段

描述

Cache usage

缓存的使用情况

Existing bills

当前缓存中已保存的话单数目

Available bills

当前缓存中还可以保存的话单数目

Max bills

当前缓存中可保存的话单总数

Auto export threshold

自动上传阈值，取值为触发自动上传的话单数

Bytes per bill

缓存中每个话单的存储空间大小 （单位：字节）

【相关命令】

·**local-bill enable**

·**local-bill export**

·**local-bill export-interval**

·**local-bill export-url**

**AAA \-- 本地话单缓存配置命令 \-- local-bill enable**

------------------------------------------------------------------------

**[local-bill enable**]命令用来使能本地话单缓存功能。

**[undo local-bill enable**]用来恢复缺省情况。

【命令】

**[local-bill enable**]

**[undo local-bill enable**]

【缺省情况】

本地话单缓存功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

使能本地话单缓存功能后，当AAA服务器不能提供计费服务时（例如计费服务器不可达时），接入设备将用户计费停止时产生的话单保存在本地。本地话单缓存功能处于使能状态的情况下，可以通过配置指定本地自动定期将缓存的话单上传到指定的服务器上，或手动上传到指定服务器上。

本功能可以支持对lan-access、Portal、PPP、和IPoE用户进行本地话单缓存。

【举例】

\# 使能本地话单缓存功能。

\<Sysname\> system-view

Sysname local-bill enable

【相关命令】

·**local-bill export-url**

·**local-bill export-interval**

·**local-bill export**

**AAA \-- 本地话单缓存配置命令 \-- local-bill export**

------------------------------------------------------------------------

**[local-bill export**]命令用来执行话单手动上传。

【命令】

**[local-bill export ** *url* ]  **clear-cache**

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[url*]：手动上传话单的URL，为1～256个字符的字符串。若不指定该参数，则会将本地缓存的话单上传到**local-bill export-url**命令指定的路径上。

**[clear-cache**]：手动上传话单后，清除本地缓存的话单信息。若不指定该参数，则表示手动上传话单后，不清除本地缓存的话单信息。

【使用指导】

本地话单缓存功能处于使能状态的情况下，通过本命令可立即将本地缓存的话单上传到指定的路径上，该路径可以是本命令中通过*url*参数指定，如果本命令中未指定*url*参数，则使用**local-bill export-url**命令指定的*url*参数。

具体上传URL格式要求如下：

·TFTP协议URL格式：tftp://*path*，例如tftp://1.1.1.1/lbill。

·FTP协议URL格式：

¡携带用户名和密码的格式为ftp://*username*:*password*@*server*/*path*，例如ftp://1:1@1.1.1.1/lbill。其中，*username*为FTP用户名，*password*为FTP认证密码*，**server*为FTP服务器IP地址或主机名。如果FTP用户名中携带域名，则该域名会被设备忽略，例如ftp://1@abc:1@1.1.1.1/lbill将被当作ftp://1:1@1.1.1.1/lbill处理。

¡不需要携带用户名和密码的格式为ftp://*path*，例如ftp://1.1.1.1/lbill。

本命令为一次性执行命令，所有参数仅对本次手动上传有效。

通常情况下，使用话单自动上传功能即可，在自动上传路径不可达（例如存储话单的服务器故障）、有临时审计、数据分析等需求的情况下，可通过本命令进行手工上传话单，为避免**local-bill export-url**命令指定的上传URL不可达造成话单上传失败问题，可通过*url*参数指定一个其它的上传URL。

在上传的话单用于计费或审计等用途的情况下，建议执行话单手动上传的同时，指定**clear-cache**参数清除本地缓存的话单信息；在上传的话单用于数据分析、故障排除等用途的情况下，建议执行话单手工上传的同时，不要指定**clear-cache**参数，保留本地缓存的话单信息用于正常的话单上传。

手动上传操作仅能同时在一个用户线上执行。某用户线上的用户执行了该操作后，系统需要一定的时间进行上传，在此期间，该用户线上的用户必须等待上传结果，不能执行命令行操作，且正在进行的自动上传也会暂停等待。同时，其它用户线上的用户执行手动上传话单命令时，系统会提示当前正在处理手动上传话单不能执行本次命令。

【举例】

\# 将本地缓存话单手动上传到URL为tftp://10.10.10.10/tftp的服务器上，并在上传后清除缓存的话单信息。

\<Sysname\> system-view

Sysname local-bill export tftp://10.10.10.10/tftp clear-cache

【相关命令】

·**local-bill enable**

·**local-bill export-interval**

·**local-bill export-url**

**AAA \-- 本地话单缓存配置命令 \-- local-bill export-interval**

------------------------------------------------------------------------

**[local-bill export-interval**]命令用来配置话单自动上传的周期。

**[undo local-bill export-interval**]命令用来恢复缺省情况。

【命令】

**[local-bill export-interval ***interval*]

**[undo local-bill export-interval**]

【缺省情况】

自动上传话单的周期为1440分钟。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：话单自动上传的周期，单位为分钟，取值范围为1～65535。

【使用指导】

本地话单缓存功能处于使能状态的情况下，系统将以本命令指定的周期向指定路径上进行话单上传。

【举例】

\# 配置本地缓存话单自动上传的周期为100分钟。

\<Sysname\> system-view

Sysname local-bill export-interval 100

【相关命令】

·**local-bill enable**

·**local-bill export-url**

·**local-bill export**

**AAA \-- 本地话单缓存配置命令 \-- local-bill export-url**

------------------------------------------------------------------------

**[local-bill export-url**]命令用来配置对本地缓存话单进行上传的URL 。

**[undo local-bill export-url**]命令用来恢复缺省情况。

【命令】

**[local-bill export-url ***url*]

**[undo local-bill export-url**]

【缺省情况】

未指定对话单上传的URL，对缓存话单的自动上传会失败。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[url*]：对本地缓存话单进行上传的URL，为1～256个字符的字符串。该路径必须是可存储文件的路径。

【使用指导】

本地话单缓存功能处于使能状态的情况下，指定合法的上传话单的URL后，系统将定期向该指定路径上进行话单上传，或当本地缓存话单数目达到系统设定的阈值时，系统也会自动向该指定路径上进行话单上传。上传的话单将以文本格式保存在指定路径中供计费、审校或分析。上传方式包括TFTP和FTP。每次话单信息上传完成之后，系统将自动清除当前本地话单缓存中的所有话单信息。

具体上传URL格式要求如下：

·TFTP协议URL格式：tftp://*path*，例如tftp://1.1.1.1/lbill。

·FTP协议URL格式：

¡携带用户名和密码的格式为ftp://*username*:*password*@*server*/*path*，例如ftp://1:1@1.1.1.1/lbill。其中，*username*为FTP用户名，*password*为FTP认证密码*，**server*为FTP服务器IP地址或主机名。如果FTP用户名中携带域名，则该域名会被设备忽略，例如ftp://1@abc:1@1.1.1.1/lbill将被当作ftp://1:1@1.1.1.1/lbill处理。

¡不需要携带用户名和密码的格式为ftp://*path*，例如ftp://1.1.1.1/lbill。

【举例】

\# 配置本地缓存话单的上传URL为tftp://10.10.10.10/tftp。

\<Sysname\> system-view

Sysname local-bill export-url tftp://10.10.10.10/tftp

【相关命令】

·**local-bill enable**

·**local-bill export-interval**

**AAA \-- 本地话单缓存配置命令 \-- snmp-agent trap enable local-bill**

------------------------------------------------------------------------

**[snmp-agent trap enable local-bill**]命令用来开启本地话单缓存告警功能。

**[undo snmp-agent trap enable local-bill**]用来关闭本地话单缓存告警功能。

【命令】

**[snmp-agent  trap enable local-bill **]

**[undo snmp-agent trap enable local-bill**]

【缺省情况】

本地话单缓存告警功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

使能本地话单上传缓存告警功能后，当系统定时自动上传或超过阈值时自动上传本地缓存的话单到服务器失败时，会发送表示本地话单上传失败的告警信息。

发送告警信息的最小时间间隔为10秒。当出现上传话单失败而需要发送告警信息时，如果距离上次上传失败发送告警信息间隔不足10秒，则本次不会发送告警信息。

【举例】

\# 使能本地话单缓存告警功能。

\<Sysname\> system-view

Sysname snmp-agent trap enable local-bill

【相关命令】

·**local-bill export-url**

·**local-bill export-interval**

**AAA \-- ITA业务策略配置命令 \-- accounting-level**

------------------------------------------------------------------------

![说明](AAA命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[accounting-level**]命令用来指定需要进行计费的流量计费级别。

**[undo accounting-level**]命令用来删除需要进行计费的计费级别。

【命令】

**[accounting-level ***level*****[{ **ipv4** \| **ipv6** }]]

**[undo accounting-level ** *level* ]

【缺省情况】

未指定需要计费的流量计费级别。

【视图】

ITA业务策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[accounting-level ***level*]：流量计费级别，取值范围为1～8。

**[ipv4**]：指定该级别的流量按照IPv4流量进行计费。

**[Ipv6**]：指定该级别的流量按照IPv6流量进行计费。

【使用指导】

流量计费级别是指运营商对用户访问不同目的的流量收取不同等级的费用，例如在校园网环境中，用户访问校园网或教育网内资源只需交纳一定的费用（通常较低）；如果访问Internet则需要交纳相对较高的费用。

可以通过多次执行本命令为ITA业务策略指定多个需要计费的流量计费级别。

执行**undo accounting-level**命令时，如果不指定级别，则表示删除本ITA业务策略内所有的流量计费级别。

【举例】

\# 在ITA业务策略ita1中，指定需要计费的流量计费级别为2和5，其中2级作为IPv4流量计费，5级作为IPv6流量计费。

\<Sysname\> system-view

Sysname ita policy ita1

Sysname-ita-policy-ita1 accounting-level 2 ipv4

Sysname-ita-policy-ita1 accounting-level 5 ipv6

【相关命令】

·**ita policy**

**AAA \-- ITA业务策略配置命令 \-- accounting-merge enable**

------------------------------------------------------------------------

![说明](AAA命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[accounting-merge enable**]命令用来开启统一计费功能。

**[undo accounting-merge enable**]命令用来关闭统一计费功能。

【命令】

**[accounting-merge enable**]

**[undo accounting-merge enable**]

【缺省情况】

统一计费功能处于关闭状态。

【视图】

ITA业务策略视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启ITA业务策略的统一计费功能后，系统会将策略下所有级别的流量进行合并，并以该策略中配置的最低的流量计费级别上报给计费服务器。

【举例】

\# 在ITA业务策略ita1中使能统一计费功能。

\<Sysname\> system-view

Sysname ita policy ita1

Sysname-ita-policy-ita1 accounting-merge enable

【相关命令】

·**ita policy**

**AAA \-- ITA业务策略配置命令 \-- accounting-method**

------------------------------------------------------------------------

![说明](AAA命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[accounting-method**]命令用来指定ITA业务策略采用的计费方案。

**[undo accounting-method**]命令用来恢复ITA缺省情况。

【命令】

**[accounting-method **[{ **none** \| **radius-scheme** *radius-scheme-name* [ **none** ] }]]

**[undo accounting**]

【缺省情况】

ITA业务策略使用的计费方案为**none**。

【视图】

ITA业务策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[none**]：不计费。

**[radius-scheme*** radius-scheme-name*]：指定RADIUS方案。其中，*radius-scheme-name*表示RADIUS方案名，为1～32个字符的字符串，不区分大小写。

【使用指导】

可以对ITA业务流量采用独立的计费方案，与对非ITA业务流量采用的计费方案不同。

可以指定备选计费方法，在当前的计费方法无效时尝试使用备选的方法完成计费。例如，**radius-scheme** *radius-scheme-name* **none**表示，先进行RADIUS计费，若RADIUS计费无效则不进行计费。

【举例】

\# 在ITA业务策略ita1中指定采用的计费方案为radius1。

\<Sysname\> system-view

Sysname ita policy ita1

Sysname-ita-policy-ita1 accounting radius-scheme radius1

【相关命令】

·**radius scheme**

·**ita policy**

**AAA \-- ITA业务策略配置命令 \-- ita policy**

------------------------------------------------------------------------

![说明](AAA命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ita policy**]命令用来创建ITA业务策略。

**[undo ita policy**]命令用来删除指定的ITA业务策略。

【命令】

**[ita policy ***policy-name*]

**[undo ita policy ***policy-name*]

【缺省情况】

无ITA业务策略。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：ITA业务策略名称，由1～31个字符组成，不区分大小写。

【使用指导】

ITA业务策略用来配置智能靶向计费功能相关控制参数，包括选用的计费方案、需要进行计费的流量计费级别、用户流量配额耗尽后采用的接入策略等。

【举例】

\# 创建一个名称为ita1的ITA业务策略。

\<Sysname\> system-view

Sysname ita policy ita1

Sysname-ita-policy-ita1

**AAA \-- ITA业务策略配置命令 \-- traffic-quota-out**

------------------------------------------------------------------------

![说明](AAA命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[traffic-quota-out**]命令用来配置流量配额耗尽策略。

**[undo traffic-quota-out**]命令用来恢复缺省情况。

【命令】

**[traffic-quota-out **[{ **offline** \| **online** }]]

**[undo traffic-quota-out**]

【缺省情况】

流量配额耗尽后用户不能访问授权的目的IP地址段。

【视图】

ITA业务策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[offline**]：当用户的指定级别的流量配额耗尽后，用户不能访问授权的目的IP地址段。

**[online**]：当用户的指定级别的流量配额耗尽后，用户仍能访问授权的目的IP地址段。

【举例】

\# 在ITA业务策略ita1中配置流量配额耗尽策略为流量耗尽后不能访问授权的目前IP地址段。

\<Sysname\> system-view

Sysname ita policy ita1

Sysname-ita-policy-ita1 traffic-quota-out offline

【相关命令】

·**ita policy**

**AAA \-- ITA业务策略配置命令 \-- traffic-seperate**

------------------------------------------------------------------------

![说明](AAA命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[traffic-separate enable**]命令用来开启ITA业务流量与用户总计费流量分离功能。

**[undo traffic-separate enable**]命令用来恢复缺省情况。

【命令】

**[traffic-separate enable**]

**[undo traffic-separate enable**]

【缺省情况】

ITA业务流量与用户总计费流量分离功能处于关闭状态。

【视图】

ITA业务策略视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

缺省情况下，设备上报给计费服务器的用户总计费流量为ITA业务流量和非ITA业务流量之和。开启ITA业务流量与用户总计费流量分离功能后，设备上报给计费服务器的用户总计费流量中将不包含ITA业务流量。

【举例】

\# 在ITA业务策略ita1中开启ITA业务流量与用户总计费流量分离功能。

\<Sysname\> system-view

Sysname ita policy ita1

Sysname-ita-policy-ita1 traffic-separate enable

【相关命令】

·**ita policy**

