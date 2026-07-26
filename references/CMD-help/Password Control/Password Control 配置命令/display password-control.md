
**Password Control \-- Password Control 配置命令 \-- display password-control**

------------------------------------------------------------------------

**[display password-control**]命令用来显示密码管理的配置信息。

【命令】

**[display password-control ** **super** ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[super**]：显示super密码管理的配置信息。如果不指定该参数，将显示全局密码管理的配置信息。

【举例】

\# 显示全局密码管理的配置信息。

\<Sysname\> display password-control

 Global password control configurations:

 Password control:                     Disabled

 Password aging:                       Enabled (90 days)

 Password length:                      Enabled (10 characters)

 Password composition:                 Enabled (1 types, 1 characters per type)

 Password history:                     Enabled (max history records:4)

 Early notice on password expiration:  7 days

 Maximum login attempts:               3

 Action for exceeding login attempts:  Lock user for 1 minutes

 Minimum interval between two updates: 24 hours

 User account idle time:               90 days

 Logins with aged password:            3 times in 30 days

 Password complexity:                  Disabled (username checking)

                                       Disabled (repeated characters checking)

\# 显示super密码管理的配置信息。

\<Sysname\> display password-control super

 Super password control configurations:

 Password aging:                       Enabled (90 days)

 Password length:                      Enabled (10 characters)

 Password composition:                 Enabled (1 types, 1 characters per type)

表1-1 display password-control命令显示信息描述表

字段

描述

Global password control configurations

全局密码管理配置

Super password control configurations

Super密码管理配置

Password control

全局密码管理功能的开启状态

Password aging

密码老化功能的开启状态（密码的老化时间）

Password length

密码最小长度功能的开启状态（密码的最小长度）

Password composition

密码组合策略的开启状态（密码元素的组合类型、至少要包含每种元素的个数）

Password history

密码历史记录功能的开启状态（密码历史记录的最大条数）

Early notice on password expiration

密码过期前的提醒时间

Maximum login attempts

用户最大登录尝试次数

Action for exceeding login attempts

登录尝试次数达到设定次数后的用户帐户锁定行为

Minimum interval between two updates

密码更新的最小时间间隔

User account idle time

用户帐号闲置时间

Login with aged password

密码过期后允许用户登录的次数和时间

Password complexity

密码复杂度检查功能的开启状态（检查是否包含用户名或者颠倒的用户名；检查是否包含三个或以上相同字符）

**Password Control \-- Password Control 配置命令 \-- display password-control blacklist**

------------------------------------------------------------------------

**[display password-control blacklist**]命令用来显示用户认证失败后，被加入密码管理黑名单中的用户信息。

【命令】

**[display password-control blacklist **[[ **user-name** *name* \| **ip** *ipv4-address* \| **ipv6** *ipv6-address* ] ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[user-name*** name*]：显示密码管理黑名单中指定用户名的用户信息。其中，*name*表示本地用户名，为1～55个字符的字符串，区分大小写。

**[ip ***ipv4-address*]：显示密码管理黑名单中指定IPv4地址的用户信息。

**[ipv6 ***ipv6-address*]：显示密码管理黑名单中指定IPv6地址的用户信息。

【使用指导】

如果不指定任何参数，则显示密码管理黑名单中的所有用户信息。

FTP用户和通过VTY方式访问设备的用户在认证失败后，会被加入密码管理的黑名单，可通过本命令查看；Web用户认证失败不会加入密码管理黑名单；通过Console口或AUX口连接到设备的用户，由于系统无法获得其IP地址，且通过这两种方式访问设备的用户已经具备了一定的权限和安全性，所以认证失败后也不会被加入密码管理的黑名单。

【举例】

\# 显示用户认证失败后，被加入密码管理黑名单中的用户信息。

\<Sysname\> display password-control blacklist

 Blacklist items matched: 2.

 Username: test

    IP: 192.168.44.1        Login failures: 1      Lock flag: unlock

 Username: jj

    IP: 192.168.44.3        Login failures: 3      Lock flag: lock

表1-2 display password-control blacklist命令显示信息描述表

字段

描述

Blacklist items matched

匹配的黑名单表项数目

Username

用户名

IP

用户的IP地址

Login failures

用户登录失败的次数

Lock flag

该用户是否被锁定

·unlock：表示未锁定，允许用户再次尝试登录

·lock：表示锁定，暂时或永久禁止用户尝试登录（具体由**password-control login-attempt**命令的配置情况决定）

**Password Control \-- Password Control 配置命令 \-- password-control { aging \| composition \| history \| length } enable**

------------------------------------------------------------------------

**[password-control **[{ **aging** \| **composition** \| **history** \| **length** } **enable**]]命令用来使能指定的密码管理功能。

**[undo password-control **[{ **aging** \| **composition** \| **history** \| **length** } **enable**]]命令用来关闭指定的密码管理功能。

【命令】

**[password-control **[{ **aging** \| **composition** \| **history** \| **length** } **enable**]]

**[undo password-control **[{ **aging** \| **composition** \| **history** \| **length** } **enable**]]

【缺省情况】

各密码管理功能均处于使能状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[aging**]：使能密码老化管理功能。

**[composition**]：使能密码的组合检测管理功能。

**[history**]：使能密码历史记录管理功能。

**[length**]：使能密码最小长度管理功能。

【使用指导】

要使指定的密码管理功能生效，首先必须保证全局密码管理功能处于使能状态，其次要保证对应的密码管理功能处于使能状态。例如，若全局密码管理功能或密码最小长度管理功能处于未使能状态，则**password-control length**命令配置的具体长度限制就不会生效。

密码历史记录管理功能关闭后，系统将不再记录历史密码，但之前已经存在的密码历史记录依然保存。

需要注意的是，使能了全局密码管理功能，未使能密码最小长度管理功能时，密码的最小长度为4个字符，且至少要有四个字符不同。

【举例】

\# 使能全局密码管理功能。

\<Sysname\> system-view

Sysname password-control enable

\# 使能密码组合检测管理功能。

Sysname password-control composition enable

\# 使能密码老化功能。

Sysname password-control aging enable

\# 使能密码最小长度功能。

Sysname password-control length enable

\# 使能密码历史记录功能。

Sysname password-control history enable

【相关命令】

·**display password-control**

·**password-control enable**

**Password Control \-- Password Control 配置命令 \-- password-control aging**

------------------------------------------------------------------------

**[password-control aging**]命令用来配置密码的老化时间。

**[undo password-control aging**]命令用来恢复缺省情况。

【命令】

**[password-control aging ***aging-time*]

**[undo password-control aging**]

【缺省情况】

全局的密码老化时间为90天；用户组的密码老化时间为全局配置的密码老化时间；本地用户的密码老化时间为所属用户组的密码老化时间。

【视图】

系统视图/用户组视图/本地用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[aging-time*]：密码的老化时间，取值范围为1～365，单位为天。

【使用指导】

·系统视图下配置具有全局性，对所有用户组有效，用户组视图下的配置对用户组内所有本地用户有效，本地用户视图下的配置只对当前本地用户有效。

·该配置的生效优先级顺序由高到低依次为本地用户视图、用户组视图、全局视图。即，系统优先采用本地用户视图下的配置，若本地用户视图下未配置，则采用用户组视图下的配置，若用户组视图下也未配置，则采用全局视图下的配置。

【举例】

\# 配置全局的密码老化时间为80天。

\<Sysname\> system-view

Sysname password-control aging 80

\# 配置用户组test的密码老化时间为90天。

Sysname user-group test

Sysname-ugroup-test password-control aging 90

Sysname-ugroup-test quit

\# 配置设备管理类本地用户abc的密码老化时间为100天。

Sysname local-user abc class manage

Sysname-luser-manage-abc password-control aging 100

【相关命令】

·**display local-user**（安全命令参考/AAA）

·**display password-control**

·**display user-group**（安全命令参考/AAA）

·**password-control aging enable**

**Password Control \-- Password Control 配置命令 \-- password-control alert-before-expire**

------------------------------------------------------------------------

**[password-control alert-before-expire**]命令用来配置密码过期前的提醒时间。

**[undo password-control alert-before-expire**]命令用来恢复缺省情况。

【命令】

**[password-control alert-before-expire*** alert-time*]

**[undo password-control alert-before-expire**]

【缺省情况】

密码过期前的提醒时间为7天，表示在密码过期之前7天内，系统会在用户登录时提醒其密码即将过期。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[alert-time*]：密码过期前的提醒时间，取值范围为1～30，单位为天。

【使用指导】

不允许FTP用户更改密码，只能由管理员修改FTP用户的密码，因此本命令配置的过期提醒时间仅对非FTP类型的Login用户有效。

【举例】

\# 设定密码过期前的提醒时间为10天。

\<Sysname\> system-view

Sysname password-control alert-before-expire 10

【相关命令】

·**display password-control**

**Password Control \-- Password Control 配置命令 \-- password-control complexity**

------------------------------------------------------------------------

**[password-control complexity**]命令用来配置用户密码的复杂度检查策略。

**[undo password-control complexity**]命令用来取消指定的密码复杂度检查策略。

【命令】

**[password-control complexity **[{ **same-character** \| **user-name** } **check**]]

**[undo password-control complexity **[{ **same-character** \| **user-name** } **check**]]

【缺省情况】

全局的密码复杂度检查策略为：不对用户密码进行复杂度检查，允许密码中包含用户名或者字符顺序颠倒的用户名，也允许包含连续三个或以上的相同字符；用户组的密码复杂度检查策略为全局的的密码复杂度检查策略；本地用户的密码复杂度检查策略为所属用户组的密码复杂度检查策略。

【视图】

系统视图/用户组视图/本地用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[same-character**]：指定检查密码中是否包含连续三个或以上相同的字符。例如，密码aaabc就不符合该项复杂度检查。

**[user-name**]：指定检查密码中是否包含用户名或者字符顺序颠倒的用户名。例如，用户名为123，则密码abc123、321df就不符合该项复杂度检查。

【使用指导】

·系统视图下配置具有全局性，对所有用户组有效，用户组视图下的配置对用户组内所有本地用户有效，本地用户视图下的配置只对当前本地用户有效。

·该配置的生效优先级顺序由高到低依次为本地用户视图、用户组视图、全局视图。即，系统优先采用本地用户视图下的配置，若本地用户视图下未配置，则采用用户组视图下的配置，若用户组视图下也未配置，则采用全局视图下的配置。

·可以通过多次执行本命令同时打开用户名检查以及连续字符检查功能。

【举例】

\# 配置密码复杂度检测策略为，检查配置的密码中是否包含用户名或者字符顺序颠倒的用户名。

\<Sysname\> system-view

Sysname password-control complexity user-name check

【相关命令】

·**display local-user**（安全命令参考/AAA）

·**display password-control**

·**display user-group**（安全命令参考/AAA）

**Password Control \-- Password Control 配置命令 \-- password-control composition**

------------------------------------------------------------------------

**[password-control composition**]命令用来配置用户密码的组合策略。

**[undo password-control composition**]命令用来恢复缺省情况。

【命令】

**[password-control composition type-number ***type-number* [ **type-length** *type-length* ]]

**[undo password-control composition**]

【缺省情况】

非FIPS模式下：

全局的密码元素的最少组合类型为1种，至少要包含每种元素的个数为1个；用户组的密码组合策略为全局配置的密码组合策略；本地用户的密码组合策略为所属用户组的密码组合策略。

FIPS模式下：

全局的密码元素的最少组合类型为4种，至少要包含每种元素的个数为1个；用户组的密码组合策略为全局配置的密码组合策略；本地用户的密码组合策略为所属用户组的密码组合策略。

【视图】

系统视图/用户组视图/本地用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[type-number*** type-number*]：密码元素的最少组合类型。其中，*type-number*表示组合类型的个数，非FIPS模式下，取值范围为1～4；FIPS模式下，取值为4。

**[type-length*** type-length*]：密码中至少要包含每种元素的个数。其中，*type-length*表示元素个数，非FIPS模式下，取值范围为1～63；FIPS模式下，取值范围为1～15。

【使用指导】

系统视图下配置具有全局性，对所有用户组有效，用户组视图下的配置对用户组内所有本地用户有效，本地用户视图下的配置只对当前本地用户有效。

该配置的生效优先级顺序由高到低依次为本地用户视图、用户组视图、全局视图。即，系统优先采用本地用户视图下的配置，若本地用户视图下未配置，则采用用户组视图下的配置，若用户组视图下也未配置，则采用全局视图下的配置。

密码元素的最少组合类型数以及每种元素的最小个数的乘积应该小于允许的最大密码长度。

【举例】

\# 配置全局的密码元素的最少组合类型为4种，至少要包含每种元素的个数为5个。

\<Sysname\> system-view

Sysname password-control composition type-number 4 type-length 5

\# 配置用户组test的密码元素的最少组合类型为4种，至少要包含每种元素的个数为5个。

Sysname user-group test

Sysname-ugroup-test password-control composition type-number 4 type-length 5

Sysname-ugroup-test quit

\# 配置设备管理类本地用户abc的密码元素的最少组合类型为4种，至少要包含每种元素的个数为5个。

Sysname local-user abc class manage

Sysname-luser-manage-abc password-control composition type-number 4 type-length 5

【相关命令】

·**display local-user**（安全命令参考/AAA）

·**display password-control**

·**display user-group**（安全命令参考/AAA）

·**password-control composition enable**

**Password Control \-- Password Control 配置命令 \-- password-control enable**

------------------------------------------------------------------------

**[password-control enable**]命令用来使能全局密码管理功能。

**[undo password-control enable**]命令用来关闭全局密码管理功能。

【命令】

**[password-control enable**]

 **undo password-control enable**

【缺省情况】

非{.ItemStepChar}FIPS{.ItemStepChar}模式下：{.ItemStepChar}

全局密码管理功能处于关闭状态{.ItemStepChar}。

FIPS模式下：

全局密码管理功能处于开启状态，切不能关闭。{.ItemStepChar}

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有在使能了全局密码管理功能的情况下，其它指定的密码管理功能才能生效。

需要注意的是，使能全局密码管理功能后：

·设备管理类本地用户密码以及super密码的配置将不被显示，即无法通过相应的**display**命令查看到设备管理类本地用户密码以及super密码的配置。网络接入类本地用户密码不受密码管理功能控制，其配置显示也不受影响。

·首次设置的设备管理类本地用户密码必须至少由四个不同的字符组成。

·FIPS模式下，不能关闭全局Password Control功能，即**undo password control enable**命令执行后不生效。

【举例】

\# 使能全局密码管理功能。

\<Sysname\> system-view

Sysname password-control enable

【相关命令】

·**display password-control**

[·**password-control **[{ **aging** \| **composition** \| **history** \| **length** } **enable**]]

**Password Control \-- Password Control 配置命令 \-- password-control expired-user-login**

------------------------------------------------------------------------

**[password-control expired-user-login**]命令用来配置密码过期后允许用户登录的时间和次数。

**[undo password-control expired-user-login**]命令用来恢复缺省情况。

【命令】

**[password-control expired-user-login delay ***delay*** times ***times*]

 **undo password-control expired-user-login**

【缺省情况】

密码过期后允许登录的时间为30天，允许登录的次数为3次，即密码过期后系统还允许用户在30天内登录3次。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[delay ***delay*]：密码过期后允许用户登录的时长，取值范围为1～90，单位为天。

**[times ***times*]：密码过期后允许用户登录的最大次数，取值范围为0～10。0表示密码过期后不允许用户登录。

【使用指导】

该配置仅对非FTP类型的Login用户生效。对于FTP用户，密码过期后，系统不允许其继续登录。

【举例】

\# 设定允许用户在密码过期之后的60天内登录5次。

\<Sysname\> system-view

Sysname password-control expired-user-login delay 60 times 5

【相关命令】

·**display password-control**

**Password Control \-- Password Control 配置命令 \-- password-control history**

------------------------------------------------------------------------

**[password-control history**]命令用来配置每个用户密码历史记录的最大条数。

**[undo password-control history**]命令用来恢复缺省情况。

【命令】

**[password-control history ***max-record-num*]

**[undo password-control history**]

【缺省情况】

每个用户密码历史记录的最大条数为4条。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[max-record-num*]：每个用户密码历史记录的最大条数，取值范围为2～15。

【使用指导】

当记录的某用户的历史密码条数达到最大值后，该用户的后续新密码历史记录将覆盖最老的一条密码历史记录。

密码历史记录管理功能关闭后，系统将不再记录历史密码，但之前已经存在的密码历史记录依然保存。只有当关闭全局密码管理功能（**undo password-control enable**）或手动清除历史密码记录时（**reset password-control history-record**），历史密码记录才会被清除掉。

【举例】

\# 配置每个用户密码历史记录的最大条数为10条。

\<Sysname\> system-view

Sysname password-control history 10

【相关命令】

·**display password-control**

·**password-control history enable**

·**reset password-control blacklist**

**Password Control \-- Password Control 配置命令 \-- password-control length**

------------------------------------------------------------------------

**[password-control length**]命令用来配置密码的最小长度。

**[undo password-control length**]命令用来恢复缺省情况。

【命令】

**[password-control length ***length*]

**[undo password-control length**]

【缺省情况】

非FIPS模式下：

全局的密码最小长度为10个字符；用户组的密码最小长度为全局配置的密码最小长度；本地用户的密码最小长度为所属用户组的密码最小长度。

FIPS模式下：

全局的密码最小长度为15个字符；用户组的密码最小长度为全局配置的密码最小长度；本地用户的密码最小长度为所属用户组的密码最小长度。

【视图】

系统视图/用户组视图/本地用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[length*]：密码的最小长度，非FIPS模式下，取值范围为4～32；FIPS模式下，取值范围为15～32。

【使用指导】

系统视图下配置具有全局性，对所有用户组有效，用户组视图下的配置对用户组内所有本地用户有效，本地用户视图下的配置只对当前本地用户有效。

该配置的生效优先级顺序由高到低依次为本地用户视图、用户组视图、全局视图。即，系统优先采用本地用户视图下的配置，若本地用户视图下未配置，则采用用户组视图下的配置，若用户组视图下也未配置，则采用全局视图下的配置。

【举例】

\# 配置全局的密码最小长度为16个字符。

\<Sysname\> system-view

Sysname password-control length 16

\# 配置用户组test的密码最小长度为16个字符。

Sysname user-group test

Sysname-ugroup-test password-control length 16

Sysname-ugroup-test quit

\# 配置设备管理类本地用户abc的密码最小长度为16个字符。

Sysname local-user abc class manage

Sysname-luser-manage-abc password-control length 16

【相关命令】

·**display local-user**（安全命令参考/AAA）

·**display password-control**

·**display user-group**（安全命令参考/AAA）

·**password-control length enable**

**Password Control \-- Password Control 配置命令 \-- password-control login idle-time**

------------------------------------------------------------------------

**[password-control login idle-time**]命令用来配置用户帐号的闲置时间。

**[undo password-control login idle-time**]命令用来恢复缺省情况。

【命令】

**[password-control login idle-time ***idle-time*]

**[undo password-control login idle-time**]

【缺省情况】

用户帐号的闲置时间为90天。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[idle-time*]：用户帐号的闲置时间，取值范围为0～365，单位为天。0表示对用户帐号闲置时间无限制。

【使用指导】

如果用户自最后一次成功登录后，在指定的闲置时间内再未成功登录过设备，那么该用户帐号将会失效。

【举例】

\# 设定用户帐号的闲置时间为30天，表示自最后一次成功登录后，若用户在30天内再未成功登录过设备，那么该用户帐号将会失效。

\<Sysname\> system-view

Sysname password-control login idle-time 30

【相关命令】

·**display password-control**

**Password Control \-- Password Control 配置命令 \-- password-control login-attempt**

------------------------------------------------------------------------

**[password-control login-attempt**]命令用来配置允许用户登录的最大尝试次数以及登录尝试失败后的处理措施。

**[undo password-control login-attempt**]命令用来恢复缺省情况

【命令】

**[password-control login-attempt*** login-times*****[[ **exceed** { **lock** \| **lock-time** *time* \| **unlock** } ]]]

 **undo password-control login-attempt**

【缺省情况】

全局的用户登录尝试次数限制策略为：用户登录尝试的最大次数为3次。如果某用户登录尝试失败，则1分钟后再允许该用户重新登录；用户组的用户登录尝试次数限制策略为全局配置的用户登录尝试次数限制策略；本地用户的登录尝试次数限制策略为所属用户组的用户登录尝试次数限制策略。

【视图】

系统视图/用户组视图/本地用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[login-times*]：用户登录尝试的最大次数，取值范围为2～10。

**[exceed**]：对登录尝试失败次数超过最大值的用户所采取的处理措施。

**[lock**]：表示永久禁止该用户登录。

**[lock-time ***time*]：表示禁止该用户一段时间后，再允许该用户重新登录。其中，*time*为禁止该用户的时间，取值范围为1～360，单位为分钟。

**[unlock**]：表示不禁止该用户，允许其继续登录。

【使用指导】

系统视图下配置具有全局性，对所有用户组有效，用户组视图下的配置对用户组内所有本地用户有效，本地用户视图下的配置只对当前本地用户有效。

该配置的生效优先级顺序由高到低依次为本地用户视图、用户组视图、全局视图。即，系统优先采用本地用户视图下的配置，若本地用户视图下未配置，则采用用户组视图下的配置，若用户组视图下也未配置，则采用全局视图下的配置。

用户登录认证失败后，系统会将其加入密码管理的黑名单，当登录失败次数超过指定值后，系统将会根据此处配置的处理措施对其之后的登录行为进行相应的限制，并且该用户只能在满足相应的条件后才可重新登录：

·对于被永久禁止登录的用户，只有管理员使用**reset password-control blacklist**命令把该用户从密码管理的黑名单中删除后，该用户才能重新登录。

·对于被禁止一段时间内登录的用户，当配置的禁止时间超时或者管理员使用**reset password-control blacklist**命令将其从密码管理的黑名单中删除，该用户才可以重新登录。

·对于不禁止登录的用户，只要用户登录成功后，该用户就会从该黑名单中删除。

本命令生效后，会立即影响密码管理黑名单中当前用户的锁定状态以及这些用户后续的登录。

【举例】

\# 管理员设定用户登录尝试次数为4次，并且永久禁止该用户登录。

\<Sysname\> system-view

Sysname password-control login-attempt 4 exceed lock

之后，若有用户连续尝试认证的失败累加次数达到4次，管理员可通过命令查看到被加入密码管理黑名单中的用户锁定状态由之前的**unlock**切换为**lock**，且该用户无法再次成功登录。

Sysname display password-control blacklist

 Username: test

    IP: 192.168.44.1        Login failures: 4      [Lock flag: lock]{.TerminalDisplayshading}

 Blacklist items matched: 1.

\# 管理员设定用户登录尝试次数为2次，并且限制该用户在3分钟后才能重新登录。

\<Sysname\> system-view

Sysname password-control login-attempt 2 exceed lock-time 3

之后，若有用户连续尝试认证的失败累加次数达到2次，管理员可通过命令查看到被加入密码管理黑名单中的用户锁定状态由之前的**unlock**切换为**lock**。

Sysname display password-control blacklist

 Username: test

    IP: 192.168.44.1        Login failures: 2      [Lock flag: lock]{.TerminalDisplayshading}

 Blacklist items matched: 1.

用户被禁止登录3分钟后，将被从密码管理黑名单中删除，且可以重新登录。

【相关命令】

·**display local-user**（安全命令参考/AAA）

·**display password-control**

·**display password-control blacklist**

·**display user-group**（安全命令参考/AAA）

·**reset password-control blacklist**

**Password Control \-- Password Control 配置命令 \-- password-control super aging**

------------------------------------------------------------------------

**[password-control super aging**]命令用来配置super密码的老化时间。

**[undo password-control super aging**]命令用来恢复缺省情况。

【命令】

**[password-control super aging ***aging-time*]

 **undo password-control super aging**

【缺省情况】

密码的老化时间为90天。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[aging-time*]：super密码的老化时间，取值范围为1～365，单位为天。

【举例】

\# 设定super密码的老化时间为10天。

\<Sysname\> system-view

Sysname password-control super aging 10

【相关命令】

·**display password-control**

·**password-control aging**

**Password Control \-- Password Control 配置命令 \-- password-control super composition**

------------------------------------------------------------------------

**[password-control super composition**]命令用来配置super密码的组合策略。

**[undo password-control super composition**]命令用来恢复缺省情况。

【命令】

**[password-control super composition type-number ***type-number***** **type-length** *type-length* ]

 **undo password-control super composition**

【缺省情况】

非FIPS模式下：

super密码的最少组合类型为1种，每种类型至少包含1个字符。

FIPS模式下：

super密码的最少组合类型为4种，每种类型至少包含1个字符。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[type-number*** type-number*]：super密码的最少组合类型。其中，*type-number*表示组合类型，非FIPS模式下，取值范围为1～4；FIPS模式下，取值为4。

**[type-length*** type-length*]：super密码中每种类型的最少字符个数。其中，*type-length*表示字符个数，非FIPS模式下，取值范围为1～63；FIPS模式下，取值范围为1～15。

【使用指导】

密码元素的最少组合类型数以及每种元素的最小个数的乘积应该小于密码允许的最大长度。

【举例】

\# 配置super密码的最少组合类型为4种，每种类型的最少字符个数为5个。

\<Sysname\> system-view

Sysname password-control super composition type-number 4 type-length 5

【相关命令】

·**display password-control**

·**password-control composition**

**Password Control \-- Password Control 配置命令 \-- password-control super length**

------------------------------------------------------------------------

**[password-control super length**]命令用来配置super密码的最小长度。

**[undo password-control super length**]命令用来恢复缺省情况。

【命令】

**[password-control super length ***length*]

 **undo password-control super length**

【缺省情况】

非FIPS模式下：

super密码的最小长度为10个字符。

FIPS模式下：

super密码的最小长度为15个字符。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[length*]：super密码的最小字符长度，非FIPS模式下，取值范围为4～63；FIPS模式下，取值范围为15～63。

【举例】

\# 设定super密码的最小长度为16个字符。

\<Sysname\> system-view

Sysname password-control super length 16

【相关命令】

·**display password-control**

·**password-control length**

**Password Control \-- Password Control 配置命令 \-- password-control update-interval**

------------------------------------------------------------------------

**[password-control update-interval**]命令用来配置密码更新的最小时间间隔。

**[undo password-control update-interval**]命令用来恢复缺省情况。

【命令】

**[password-control update-interval ***interval*]

 **undo password-control update-interval**

【缺省情况】

密码更新的最小时间间隔为24小时。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：密码更新的最小时间间隔，取值范围为0～168，单位为小时。0表示对密码更新的时间间隔无限制。

【使用指导】

有两种情况下的密码更新并不受该功能的约束：用户首次登录设备时系统要求用户修改密码；密码老化后系统要求用户修改密码。

【举例】

\# 设定密码更新的最小时间间隔为36小时。

\<Sysname\> system-view

Sysname password-control update-interval 36

【相关命令】

·**display password-control**

**Password Control \-- Password Control 配置命令 \-- reset password-control blacklist**

------------------------------------------------------------------------

**[reset password-control blacklist**]命令用来清除密码管理黑名单中的用户。

【命令】

**[reset password-control blacklist ** **user-name** *name* ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[user-name*** name*]：清除密码管理黑名单中指定的用户。其中，*name*表示用户名，为1～55个字符的字符串，区分大小写。

【使用指导】

对于因为登录认证时密码尝试的失败次数超过最大值而被禁止登录的用户，管理员可以使用本命令将其从黑名单中删除，使其可以重新登录。

【举例】

\# 清除密码管理黑名单中的用户test。

\<Sysname\> reset password-control blacklist user-name test

Are you sure to delete the specified user in blacklist? [Y/N:]

【相关命令】

·**display password-control blacklist**

**Password Control \-- Password Control 配置命令 \-- reset password-control history-record**

------------------------------------------------------------------------

**[reset password-control history-record**]命令用来清除用户的密码历史记录。

【命令】

**[reset password-control history-record **[ **super** [ **role** *role-name*  \| **user-name** *name* ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[super**]：删除super密码的历史记录。

**[role ***role-name*]：删除指定用户角色的用户密码历史记录。其中，*role-name*表示用户角色，为1～63个字符的字符串，区分大小写。

**[user-name*** name*]：删除指定用户名的密码历史记录。其中，*name*表示用户名，为1～55个字符的字符串，区分大小写。

【使用指导】

·如果不指定任何参数，将删除所有本地用户的密码历史记录。

·如果不指定参数*role-name*，将删除所有super密码的历史记录。

【举例】

\# 清除所有本地用户的密码历史记录。当用户输入Y，系统将删除所有本地用户的密码历史记录。

\<Sysname\> reset password-control history-record

Are you sure to delete all local user's history records? [Y/N:y]

【相关命令】

·**password-control history**
