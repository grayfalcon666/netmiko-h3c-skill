<!-- CMD-INDEX
  apply classification policy         | VSD视图            | L73
  apply countermeasure policy         | VSD视图            | L117
  apply detect policy                 | VSD视图            | L161
  ap-rate-limit                       | 攻击检测策略视图         | L205
  ap-spoofing                         | 攻击检测策略视图         | L253
  ap-timer                            | 攻击检测策略视图         | L301
  block mac-address                   | 分类策略视图           | L351
  classification policy               | WIPS视图           | L397
  client-rate-limit                   | 攻击检测策略视图         | L439
  client-spoofing                     | 攻击检测策略视图         | L487
  client-timer                        | 攻击检测策略视图         | L535
  countermeasure external-ap          | 反制策略视图           | L585
  countermeasure misassociation-client | 反制策略视图           | L625
  countermeasure misconfigured-ap     | 反制策略视图           | L665
  countermeasure policy               | WIPS视图           | L705
  countermeasure potential-authorized-ap | 反制策略视图           | L749
  countermeasure potential-external-ap | 反制策略视图           | L789
  countermeasure potential-rogue-ap   | 反制策略视图           | L829
  countermeasure rogue-ap             | 反制策略视图           | L869
  countermeasure unauthorized-client  | 反制策略视图           | L909
  countermeasure uncategorized-ap     | 反制策略视图           | L949
  countermeasure uncategorized-client | 反制策略视图           | L989
  detect policy                       | WIPS视图           | L1029
  display wips sensor                 | 任意视图             | L1073
  display wips statistics receive     | 任意视图             | L1139
  display wips virtual-security-domain | 任意视图             | L1407
  display wips virtual-security-domain countermeasure record | 任意视图             | L1771
  flood association-request           | 攻击检测策略视图         | L1867
  flood authentication                | 攻击检测策略视图         | L1915
  flood beacon                        | 攻击检测策略视图         | L1963
  flood block-ack                     | 攻击检测策略视图         | L2011
  flood cts                           | 攻击检测策略视图         | L2059
  flood deauthentication              | 攻击检测策略视图         | L2107
  flood disassociation                | 攻击检测策略视图         | L2155
  flood eapol-start                   | 攻击检测策略视图         | L2203
  flood null-data                     | 攻击检测策略视图         | L2251
  flood probe-request                 | 攻击检测策略视图         | L2299
  flood reassociation-request         | 攻击检测策略视图         | L2347
  flood rts                           | 攻击检测策略视图         | L2395
  import oui                          | WIPS视图           | L2443
  invalid-oui-classify illegal        | 分类策略视图           | L2495
  malformed duplicated-ie             | 攻击检测策略视图         | L2539
  malformed fata-jack                 | 攻击检测策略视图         | L2587
  malformed illegal-ibss-ess          | 攻击检测策略视图         | L2635
  malformed invalid-address-combination | 攻击检测策略视图         | L2683
  malformed invalid-assoc-req         | 攻击检测策略视图         | L2731
  malformed invalid-auth              | 攻击检测策略视图         | L2779
  malformed invalid-deauth-code       | 攻击检测策略视图         | L2833
  malformed invalid-disassoc-code     | 攻击检测策略视图         | L2881
  malformed invalid-ht-ie             | 攻击检测策略视图         | L2929
  malformed invalid-ie-length         | 攻击检测策略视图         | L2981
  malformed invalid-pkt-length        | 攻击检测策略视图         | L3029
  malformed large-duration            | 攻击检测策略视图         | L3077
  malformed null-probe-resp           | 攻击检测策略视图         | L3127
  malformed overflow-eapol-key        | 攻击检测策略视图         | L3175
  malformed overflow-ssid             | 攻击检测策略视图         | L3223
  malformed redundant-ie              | 攻击检测策略视图         | L3271
  manual-classify mac-address         | 分类策略视图           | L3319
  reset wips statistics               | 用户视图             | L3373
  reset wips virtual-security-domain  | ]                | L3403
  reset wips virtual-security-domain countermeasure record | 用户视图             | L3453
  trust mac-address                   | 分类策略视图           | L3487
  trust oui                           | 分类策略视图           | L3533
  trust ssid                          | 分类策略视图           | L3581
  virtual-security-domain             | WIPS视图           | L3627
  weak-iv                             | 攻击检测策略视图         | L3671
  wips                                | 系统视图             | L3719
  wips enable                         | Radio视图          | L3757
  wips virtual-security-domain        | AP视图             | L3797
-->

**WIPS \-- WIPS配置命令 \-- apply classification policy**

------------------------------------------------------------------------

**[apply classification policy**]命令用来在VSD上应用分类策略。

**[undo apply classification policy**]命令用来取消应用的分类策略。

【命令】

**[apply classification policy **]*policy-name*

**[undo apply classification policy**]* policy-name*

【缺省情况】

没有在VSD上应用分类策略。

【视图】

VSD视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：分类策略名称，为1～63个字符的字符串，区分大小写。

【举例】

\# 在VSD上应用分类策略policy1。

\<Sysname\> system-view

Sysname wips

Sysname-wips virtual-security-domain home

Sysname-wips-vsd-home apply classification policy policy1

**WIPS \-- WIPS配置命令 \-- apply countermeasure policy**

------------------------------------------------------------------------

**[apply countermeasure policy**]命令用来在VSD上应用反制策略。

**[undo apply countermeasure policy**]命令用来取消应用的攻击检测策略。

【命令】

**[apply countermeasure policy **]*policy-name*

**[undo apply countermeasure policy**]* policy-name*

【缺省情况】

没有在VSD上应用反制策略。

【视图】

VSD视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：反制策略名称，为1～63个字符的字符串，区分大小写。

【举例】

\# 在VSD上应用反制策略policy2。

\<Sysname\> system-view

Sysname wips

Sysname-wips virtual-security-domain home

Sysname-wips-vsd-home apply countermeasure policy policy2

**WIPS \-- WIPS配置命令 \-- apply detect policy**

------------------------------------------------------------------------

**[apply detect policy**]命令用来在VSD上应用攻击检测策略。

**[undo apply detect policy**]命令用来取消应用的攻击检测策略。

【命令】

**[apply detect policy **]*policy-name*

**[undo apply detect policy**]* policy-name*

【缺省情况】

没有在VSD上应用攻击检测策略。

【视图】

VSD视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：攻击检测策略名称，为1～63个字符的字符串，区分大小写。

【举例】

\# 在VSD上应用攻击检测策略policy2。

\<Sysname\> system-view

Sysname wips

Sysname-wips virtual-security-domain home

Sysname-wips-vsd-home apply detect policy policy2

**WIPS \-- WIPS配置命令 \-- ap-rate-limit**

------------------------------------------------------------------------

**[ap-rate-limit**]命令用来控制AP表项学习的速率。

**[undo** **ap-rate-limit**]命令用来恢复缺省情况。

【命令】

**[ap-rate-limit** [ **interval** ]*interval-value*****[\| **quiet** ]*quiet-value *[\| **threshold** ]*number * \*]

**[undo ap-rate-limit**]

【缺省情况】

学习AP表项的统计周期为60秒，发送告警日志后的静默时间为1200，AP表项的阈值为64。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interval*** interval-value*]：学习AP表项的统计周期，取值范围为1～3600，单位为秒。

**[quiet**]* quiet-value*：发送告警日志后的静默时间，取值范围为1200～3600，单位为秒。在静默期间，设备在统计周期内学习到的AP表项即使达到触发告警阈值，设备也不会发送告警日志，并在此时间内不学习新的AP表项。

**[threshold**]* number*：AP表项的阈值，取值范围为1～4096。当设备学习AP表项达到触发阈值，设备会发送告警日志。

【举例】

\# 配置控制AP表项学习的速率。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home ap-rate-limit interval 60 threshold 100 quiet 1600

**WIPS \-- WIPS配置命令 \-- ap-spoofing**

------------------------------------------------------------------------

**[ap-spoofing**]命令用来开启AP地址仿冒检测功能。

**[undo** **ap-spoofing**]命令用来关闭AP地址仿冒检测功能。

【命令】

**[ap-spoofing** [ **quiet** *quiet-value* ]]

**[undo ap-spoofing**]

【缺省情况】

不检测AP地址仿冒。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[quiet**]* quiet-value*：发送告警日志后的静默时间，取值范围为5～604800，单位为秒，缺省值为600秒。在静默期间，设备再次检测到AP地址仿冒也不会发送告警日志。

【使用指导】

设备检测到AP地址仿冒后会发送告警日志。

【举例】

\# 开启AP地址仿冒检测功能，静默时间为360秒。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home ap-spoofing quiet 360

**WIPS \-- WIPS配置命令 \-- ap-timer**

------------------------------------------------------------------------

**[ap-timer**]命令用来配置AP表项的时间参数。

**[undo** **ap-timer**]命令用来恢复缺省情况。

【命令】

**[ap-timer** [ **inactive** ]*inactive-value*** aging ***aging-value*****]

**[undo ap-timer**]

【缺省情况】

AP表项的非活跃时间为300秒，老化时间为600秒。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[inactive **]*inactive-value*：从创建AP表项转换到非活跃状态的时间，取值范围为60～1200，单位为秒。

**[aging **]*aging-value*：从创建AP表项转换到删除AP表项的老化时间，取值范围为120～86400，单位为秒。

【使用指导】

配置的老化时间必须大于非活跃时间。

【举例】

\# 配置AP表项的时间参数。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home ap-timer inactive 120 aging 360

**WIPS \-- WIPS配置命令 \-- block mac-address**

------------------------------------------------------------------------

**[block mac-address**]命令用来将指定的MAC地址添加到静态禁用列表中。

**[undo block mac-address**]命令用来删除静态禁用列表中的MAC地址。

【命令】

**[block mac-address **]*mac-address*

**[undo block mac-address ***mac-address*[ \| **all** }]

【缺省情况】]

静态禁用列表中不存在MAC地址。

【视图】

分类策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mac-address*]：AP或客户端的MAC地址，格式为H-H-H。

**[all**]：所有MAC地址。

【举例】

\# 将MAC地址78AC-C0AF-944F添加到静态禁用列表中。

\<Sysname\> system-view

Sysname wips

Sysname-wips classification policy home

Sysname-wips-cls-home block mac-address 78AC-C0AF-944F

**WIPS \-- WIPS配置命令 \-- classification policy**

------------------------------------------------------------------------

**[classification policy**]命令用来创建分类策略，并进入分类策略视图。

**[undo classification policy**]命令用来删除分类策略。

【命令】

**[c**]**lassification policy ***policy-name*

**[undo classification policy **]*policy-name*

【缺省情况】

没有创建分类策略。

【视图】

WIPS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：分类策略名称，为1～63个字符的字符串，区分大小写。

【举例】

\# 创建名字为home的分类策略，并进入分类策略视图。

\<Sysname\> system-view

Sysname wips

Sysname-wips classification policy home

**WIPS \-- WIPS配置命令 \-- client-rate-limit**

------------------------------------------------------------------------

**[client-rate-limit**]命令用来控制客户端表项学习的速率。

**[undo** **client -rate-limit**]命令用来恢复缺省情况。

【命令】

**[client-rate-limit** [ **interval** ]*interval-value*[\| **quiet** ]*quiet-value *[\| **threshold** ]*number* \*]

**[undo client-rate-limit**]

【缺省情况】

学习客户端表项的统计周期为60秒，发送告警日志后的静默时间为1200秒，客户端表项的阈值为512。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interval*** interval-value*]：学习客户端表项的统计周期，取值范围为1～3600，单位为秒。

**[quiet**]* quiet-value*：发送告警日志后的静默时间，取值范围为1200～3600，单位为秒。在静默期间，设备在统计周期内学习到的客户端表项即使达到触发告警阈值，设备也不会发送告警日志，并在此时间内不学习新的客户端表项。

**[threshold**]* number*：客户端表项的阈值，取值范围为1～4096。当设备学习客户端表项达到触发阈值，设备会发送告警日志。

【举例】

\# 配置控制客户端表项学习的速率。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home client-rate-limit interval 60 threshold 100 quiet 1600

**WIPS \-- WIPS配置命令 \-- client-spoofing**

------------------------------------------------------------------------

**[client-spoofing**]命令用来开启客户端地址仿冒检测功能。

**[undo** **client-spoofing**]命令用来关闭客户端地址仿冒检测功能。

【命令】

**[client-spoofing** [ **quiet** *quiet-value* ]]

**[undo client-spoofing**]

【缺省情况】

客户端地址仿冒检测功能处于关闭状态。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[quiet**]* quiet-value*：发送告警日志后的静默时间，取值范围为5～604800，单位为秒，缺省值为600秒。在静默期间，设备再次检测到客户端地址仿冒也不会发送告警日志。

【使用指导】

设备检测到客户端地址仿冒后会发送告警日志。

【举例】

\# 开启客户端地址仿冒检测功能。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home client-spoofing quiet 360

**WIPS \-- WIPS配置命令 \-- client-timer**

------------------------------------------------------------------------

**[client-timer**]命令用来配置客户端表项的时间参数。

**[undo** **client-timer**]命令用来恢复缺省情况。

【命令】

**[client-timer** [ **inactive** ]*inactive-value*** aging ***aging-value*]

**[undo client-timer**]

【缺省情况】

客户端表项的非活跃时间为300秒，老化时间为600秒。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[inactive **]*inactive-value*：从创建客户端表项到非活跃状态的非活跃时间，取值范围为60～1200，单位为秒。

**[aging **]*aging-value*：从创建客户端表项到删除客户端表项的老化时间，取值范围为120～86400，单位为秒。

【使用指导】

配置的老化时间必须大于非活跃时间。

【举例】

\# 配置客户端表项的时间参数，从创建客户端表项到非活跃状态的非活跃时间为120秒，从创建客户端表项到删除客户端表项的老化时间为360秒。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home client-timer inactive 120 aging 360

**WIPS \-- WIPS配置命令 \-- countermeasure external-ap**

------------------------------------------------------------------------

**[countermeasure external-ap**]命令对外部AP进行反制。

**[undo **]**countermeasure external-ap**命令用来恢复缺省情况。

【命令】

**[countermeasure external-ap**]

**[undo countermeasure external-ap**]

【缺省情况】

不对外部AP进行反制。

【视图】

反制策略视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 对外部AP进行反制。

\<Sysname\> system-view

Sysname wips

Sysname-wips countermeasure policy home

Sysname-wips-cms-home countermeasure external-ap

**WIPS \-- WIPS配置命令 \-- countermeasure misassociation-client**

------------------------------------------------------------------------

**[countermeasure misassociation-client**]命令对关联错误的客户端进行反制。

**[undo **]**countermeasure misassociation-client**令用来恢复缺省情况。

【命令】

**[countermeasure misassociation-client**]

**[undo countermeasure misassociation-client**]

【缺省情况】

不对关联错误的客户端进行反制。

【视图】

反制策略视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 对关联错误的客户端进行反制。

\<Sysname\> system-view

Sysname wips

Sysname-wips countermeasure policy home

Sysname-wips-cms-home countermeasure misassociation-client

**WIPS \-- WIPS配置命令 \-- countermeasure misconfigured-ap**

------------------------------------------------------------------------

**[countermeasure misconfigured-ap**]命令对配置错误的AP进行反制。

**[undo **]**countermeasure misconfigured-ap**命令用来恢复缺省情况。

【命令】

**[countermeasure misconfigured-ap**]

**[undo countermeasure misconfigured-ap**]

【缺省情况】

不对配置错误的AP进行反制。

【视图】

反制策略视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 对配置错误的AP进行反制。

\<Sysname\> system-view

Sysname wips

Sysname-wips countermeasure policy home

Sysname-wips-cms-home countermeasure misconfigured-ap

**WIPS \-- WIPS配置命令 \-- countermeasure policy**

------------------------------------------------------------------------

**[countermeasure policy**]命令用来创建反制策略，并进入反制策略视图。

**[undo **]**countermeasure policy**命令用来删除反制策略。

【命令】

**[countermeasure policy **]*policy-name*

**[undo countermeasure policy **]*policy-name*

【缺省情况】

没有创建反制策略。

【视图】

WIPS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：反制策略的名称，为1～63个字符的字符串，区分大小写。

【举例】

\# 创建名为home的反制策略，并进入反制策略视图。

\<Sysname\> system-view

Sysname wips

Sysname-wips countermeasure policy home

Sysname-wips-cms-home

**WIPS \-- WIPS配置命令 \-- countermeasure potential-authorized-ap**

------------------------------------------------------------------------

**[countermeasure potential-authorized-ap**]命令对潜在授权AP进行反制。

**[undo **]**countermeasure potential-authorized-ap**命令用来恢复缺省情况。

【命令】

**[countermeasure potential-authorized-ap**]

**[undo countermeasure potential-authorized-ap**]

【缺省情况】

不对潜在授权AP进行反制。

【视图】

反制策略视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 对潜在授权AP进行反制。

\<Sysname\> system-view

Sysname wips

Sysname-wips countermeasure policy home

Sysname-wips-cms-home countermeasure potential-authorized-ap

**WIPS \-- WIPS配置命令 \-- countermeasure potential-external-ap**

------------------------------------------------------------------------

**[countermeasure potential-external-ap**]命令对潜在外部AP进行反制。

**[undo **]**countermeasure potential-external-ap**命令用来恢复缺省情况。

【命令】

**[countermeasure potential-external-ap**]

**[undo countermeasure potential-external-ap**]

【缺省情况】

不对潜在外部AP进行反制。

【视图】

反制策略视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 对潜在外部AP进行反制。

\<Sysname\> system-view

Sysname wips

Sysname-wips countermeasure policy home

Sysname-wips-cms-home countermeasure potential-external-ap

**WIPS \-- WIPS配置命令 \-- countermeasure potential-rogue-ap**

------------------------------------------------------------------------

**[countermeasure potential-rogue-ap**]命令对潜在Rogue AP进行反制。

**[undo **]**countermeasure potential-rogue-ap**命令用来恢复缺省情况。

【命令】

**[countermeasure potential-rogue-ap**]

**[undo countermeasure potential-rogue-ap**]

【缺省情况】

不对潜在Rogue AP进行反制。

【视图】

反制策略视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 对潜在Rogue AP进行反制。

\<Sysname\> system-view

Sysname wips

Sysname-wips countermeasure policy home

Sysname-wips-cms-home countermeasure potential-rogue-ap

**WIPS \-- WIPS配置命令 \-- countermeasure rogue-ap**

------------------------------------------------------------------------

**[countermeasure rogue-ap**]命令对Rogue AP进行反制。

**[undo **]**countermeasure rogue-ap**命令用来恢复缺省情况。

【命令】

**[countermeasure rogue-ap**]

**[undo countermeasure rogue-ap**]

【缺省情况】

不对Rogue AP进行反制。

【视图】

反制策略视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 对Rogue AP进行反制。

\<Sysname\> system-view

Sysname wips

Sysname-wips countermeasure policy home

Sysname-wips-cms-home countermeasure rogue-ap

**WIPS \-- WIPS配置命令 \-- countermeasure unauthorized-client**

------------------------------------------------------------------------

**[countermeasure unauthorized-client**]命令对未授权的客户端进行反制。

**[undo **]**countermeasure unauthorized-client**命令用来恢复缺省情况。

【命令】

**[countermeasure unauthorized-client**]

**[undo countermeasure unauthorized-client**]

【缺省情况】

不对未授权的客户端进行反制。

【视图】

反制策略视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 对未授权的客户端进行反制。

\<Sysname\> system-view

Sysname wips

Sysname-wips countermeasure policy home

Sysname-wips-cms-home countermeasure unauthorized-client

**WIPS \-- WIPS配置命令 \-- countermeasure uncategorized-ap**

------------------------------------------------------------------------

**[countermeasure uncategorized-ap**]命令对未确定分类的AP进行反制。

**[undo **]**countermeasure uncategorized-ap**命令用来恢复缺省情况。

【命令】

**[countermeasure uncategorized-ap**]

**[undo countermeasure uncategorized-ap**]

【缺省情况】

不对未确定分类的AP进行反制。

【视图】

反制策略视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 对未确定分类的AP进行反制。

\<Sysname\> system-view

Sysname wips

Sysname-wips countermeasure policy home

Sysname-wips-cms-home countermeasure uncategorized-ap

**WIPS \-- WIPS配置命令 \-- countermeasure uncategorized-client**

------------------------------------------------------------------------

**[countermeasure uncategorized-client**]命令对未确定分类的客户端进行反制。

**[undo **]**countermeasure uncategorized-client**命令用来恢复缺省情况。

【命令】

**[countermeasure uncategorized-client**]

**[undo countermeasure uncategorized-client**]

【缺省情况】

不对未确定分类的客户端进行反制。

【视图】

反制策略视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 对未确定分类的客户端进行反制。

\<Sysname\> system-view

Sysname wips

Sysname-wips countermeasure policy home

Sysname-wips-cms-home countermeasure uncategorized-client

**WIPS \-- WIPS配置命令 \-- detect policy**

------------------------------------------------------------------------

**[detect policy**]命令用来创建攻击检测策略，并进入攻击检测策略视图。

**[undo **]**detect policy**命令用来删除攻击检测策略。

【命令】

**[detect policy **]*policy-name*

**[undo detect policy **]*policy-name*

【缺省情况】

不存在攻击检测策略。

【视图】

WIPS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：攻击检测策略的名称，为1～63个字符的字符串，区分大小写。

【举例】

\# 创建名为home的攻击检测策略，并进入攻击检测策略视图。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home

**WIPS \-- WIPS配置命令 \-- display wips sensor**

------------------------------------------------------------------------

**[display** **wips sensor**]命令用来显示所有Sensor的信息。

【命令】

**[display** **wips sensor**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示所有Sensor的信息。

\<Sysname\> display wips sensor

Total number of sensors: 1

AP ID    Sensor name                VSD name               Radio ID   Status

3        ap1               aaa                    1          Active

表1-1 display wips sensor命令显示信息描述表

字段

描述

AP ID

AP设备的ID

Sensor name

AP设备名字

VSD name

AP所在的虚拟安全域

Radio ID

开启WIPS的Radio ID

Status

Sensor的状态：

·Active：已运行WIPS功能的Sensor

·Inactive：未运行WIPS功能的Sensor

**WIPS \-- WIPS配置命令 \-- display wips statistics receive**

------------------------------------------------------------------------

**[display** **wips statistics receive**]命令用来显示所有虚拟安全域中AC收到Sensor上报的攻击检测信息。

【命令】

**[display** **wips statistics receive**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示所有的虚拟安全域中的AC收到Sensor上报的攻击检测信息。

\<Sysname\> display wips statistics receive

Information from sensor 3

 Information about attack statistics:

   Detected association-request flood messages: 0

   Detected authentication flood messages: 0

   Detected beacon flood messages: 0

   Detected block-ack flood messages: 0

   Detected cts flood messages: 0

   Detected deauthentication flood messages: 0

   Detected disassociation flood messages: 0

   Detected eapol-start flood messages: 0

   Detected null-data flood messages: 0

   Detected probe-request flood messages: 0

   Detected reassociation-request flood messages: 0

   Detected rts flood messages: 0

   Detected duplicated-ie messages: 0

   Detected fata-jack messages: 0

   Detected illegal-ibss-ess messages: 0

   Detected invalid-address-combination messages: 0

   Detected invalid-assoc-req messages: 0

   Detected invalid-auth messages: 0

   Detected invalid-deauth-code messages: 0

   Detected invalid-disassoc-code messages: 0

   Detected invalid-ht-ie messages: 0

   Detected invalid-ie-length messages: 0

   Detected invalid-pkt-length messages: 0

   Detected large-duration messages: 0

   Detected null-probe-resp messages: 0

   Detected overflow-eapol-key messages: 0

   Detected overflow-ssid messages: 0

   Detected redundant-ie messages: 0

   Detected AP spoof AP messages: 0

   Detected AP spoof client messages: 0

   Detected AP spoof ad-hoc messages: 0

   Detected ad-hoc spoof AP messages: 0

   Detected client spoof AP messages: 0

   Detected weak IV messages: 0

   Detected excess AP messages: 0

   Detected excess client messages: 0

表1-2 display wips statistics receive命令显示信息描述表

字段

描述

Information from sensor n

Sensor n发送的消息，n表示sensor ID

Information about attack statistics

关于攻击信息统计

Detected association-request flood messages

检测到关联请求帧的泛洪攻击消息的计数

Detected authentication flood messages

检测到鉴权帧的泛洪攻击消息的计数

Detected beacon flood messages

检测到Beacon帧的泛洪攻击消息的计数

Detected block-ack flood messages

检测到批量确认帧的泛洪攻击消息的计数

Detected cts flood messages

检测到允许发送帧的泛洪攻击消息的计数

Detected deauthentication flood messages

检测到解鉴权帧的泛洪攻击消息的计数

Detected disassociation flood messages

检测到解关联帧的泛洪攻击消息的计数

Detected eapol-start flood messages

检测到握手开始帧的泛洪攻击消息的计数

Detected null-data flood messages

检测到空数据帧的泛洪攻击消息的计数

Detected probe-request flood messages

检测到探查请求帧的泛洪攻击消息的计数

Detected reassociation-request flood messages

检测到重关联请求帧的泛洪攻击消息的计数

Detected rts flood messages

检测到请求发送帧的泛洪攻击消息的计数

Detected duplicated-ie messages

检测到重复的IE畸形消息的计数

Detected fata-jack messages

检测到认证算法错畸形消息的计数

Detected illegal-ibss-ess messages

检测到无效IBSS-ESS畸形消息的计数

Detected invalid-address-combination messages

检测到无效联合地址畸形消息的计数

Detected invalid-assoc-req messages

检测到无效关联请求畸形消息的计数

Detected invalid-auth messages

检测到无效鉴权畸形消息的计数

Detected invalid-deauth-code messages

检测到无效解鉴权码畸形消息的计数

Detected invalid-disassoc-code messages

检测到无效解关联码畸形消息的计数

Detected invalid-ht-ie messages

检测到无效HT IE畸形消息的计数

Detected invalid-ie-length messages

检测到无效IE长度畸形消息的计数

Detected invalid-pkt-length messages

检测到无效报文长度畸形消息的计数

Detected large-duration messages

检测到超大持续时间畸形消息的计数

Detected null-probe-resp messages

检测到空探查回应畸形消息的计数

Detected overflow-eapol-key messages

检测到eapol-key溢出畸形消息的计数

Detected overflow-ssid messages

检测到SSID溢出畸形消息的计数

Detected redundant-ie messages

检测到冗余的IE畸形消息的计数

Detected AP spoof AP messages

检测到AP仿冒AP消息的计数

Detected AP spoof client messages

检测到AP仿冒client消息的计数

Detected AP spoof ad-hoc messages

检测到AP仿冒ad-hoc消息的计数

Detected ad-hoc spoof AP messages

检测到ad-hoc 仿冒AP消息的计数

Detected client spoof AP messages

检测到client仿冒AP消息的计数

Detected weak IV messages

检测到弱向量消息的计数

Detected excess AP messages

检测到AP设备表项超过规格消息的计数

Detected excess client messages

检测到客户端设备表项超过规格消息的计数

【相关命令】

·**reset wips statistic****s**

**WIPS \-- WIPS配置命令 \-- display wips virtual-security-domain**

------------------------------------------------------------------------

**[display wips virtual-security-domain device**]命令用来显示在指定虚拟安全域中检测到的无线设备的信息。

【命令】

**[display wips virtual-security-domain**[ *vsd-name* **device** [ **ap** [ **ad-hoc** \| **authorized** \| **external** \| **misconfigured** \| **potential-authorized** \| **potential-external** \| **potential-rogue** \| **rogue** \| **uncategorized** ] \| **client** [ **authorized** \| **misassociation** \| **unauthorized** \| **uncategorized** ] \| **mac-address** *mac-address* ]  **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[vsd-name*]：虚拟安全域的名称，为1～63个字符的字符串，区分大小写。

**[device**]：显示所有设备的信息。

**[ap**]：显示检测到AP的信息。

**[ad-hoc**]：显示AP用于Ad hoc时的信息。

**[authorized**]：显示授权AP的信息。

**[external**]：显示外部AP的信息。

**[misconfigured**]：显示配置错误的AP的信息。

**[potential-authorized**]：显示潜在授权AP的信息。

**[potential-rogue**]：显示潜在Rogue AP的信息。

**[potential-external**]：显示潜在外部AP的信息。

**[rogue**]：显示Rogue AP的信息。

**[uncategorized**]：显示无法确定类别的AP的信息。

**[client**]：显示客户端的信息。

**[authorized**]：显示授权客户端的信息。

**[misassociation**]：显示误关联客户端的信息。

**[unauthorized**]：显示未授权客户端的信息。

**[uncategorized**]：显示无法确定类别的客户端的信息。

**[mac-address** *mac-address*]：显示指定MAC地址的无线设备的信息。

**[verbose**]：显示检测到设备的详细信息。

【举例】

\#显示在虚拟安全域office中的检测到的所有无线设备信息。

\<Sysname\> display wips virtual-security-domain office device

Total 200 detected devices in virtual-security-domain a

Class: Auth - authorization; Ext - extern; Mis - mistake;

       Unauth - unauthorized; Uncate - uncategorized;

       (A) - associate; (C) - config; (P) - potential

MAC address    Type   Class    Duration    Sensors Channel Status

1000-0000-0000 AP     Ext(P)   00h 10m 46s 1       11      Active

1000-0000-0001 AP     Ext(P)   00h 10m 46s 1       6       Active

1000-0000-0002 AP     Ext(P)   00h 10m 46s 1       1       Active

表1-3 display wips virtual-security-domain device命令显示信息描述表

字段

描述

MAC Address

检测到的无线设备的MAC地址

Type

无线设备的类型：

·AP：AP设备

·Client：无线客户端

Class

无线设备的分类类别

Duration

无线设备的当前状态的持续时间

Sensors

检测到该无线设备的Sensor的数量

Channel

最后一次检测到该无线设备的信道

Status

AP或客户端表项的状态：

·Active：AP或客户端表项处于激活状态

·Inactive：AP或客户端表项处于非激活状态

\<Sysname\> display wips virtual-security-domain office device verbose

Total 1 detected devices in virtual-security-domain a

 AP: 1000-0000-0000

   Classification: Mis(C)

   Status: Active

   Status duration: 00h 27m 57s

   Vendor: Not found

   SSID:service

   Radio type: 802.11g

   Countermeasuring: No

   Security: None

   Encrypt method: None

   Authentication method: None

   Broadcast SSID: No

   Qos supported: No

   Ad-hoc: No

   Beacon interval: 0 millisecond

   Up duration: 00h 27m 57s

   Total number of reported sensors: 1

     Sensor 1:

       Sensor ID: 3

       Sensor name: 1

       Radio ID: 1

       RSSI: 15

       Channel: 6

       First reported time: 2014-06-03/09:05:51

       Last reported time: 2014-06-03/09:05:51

   Total number of associated clients: 10

     01: 2000-0000-0000

     02: 2000-0000-0001

     03: 2000-0000-0002

     04: 2000-0000-0003

     05: 2000-0000-0004

     06: 2000-0000-0005

     07: 2000-0000-0006

     08: 2000-0000-0007

     09: 2000-0000-0008

     10: 2000-0000-0009

表1-4 display wips virtual-security-domain device verbose命令显示信息描述表

字段

描述

Total *number* detected devices in virtual-security-domain *name*

在指定虚拟安全域中检测到无线设备的总数

AP

检测到AP的MAC地址

Classification

AP或无线客户端的分类：

·对于AP设备有以下几种分类类别：

¡ad_hoc、authorized、rogue、misconfigured、external、potential-authorized、potential-rogue、potential-external、uncategorized

·对于无线客户端有以下几种分类类别：

¡authorized、unauthorized、misassociated、uncategorized

Status

AP或客户端表项的状态：

·Active：AP或客户端表项处于激活状态

·Inactive：AP或客户端表项处于非激活状态

Status duration

设备当前状态的持续时间

Vendor

如果该设备的OUI能够匹配**import oui**命令导入配置文件中的OUI，则显示设备厂商，没有配置或者没有匹配到显示为Not found

SSID

AP提供的SSID

Radio Type

无线设备使用的射频模式

Countermeasuring

·No：没有被反制或是已经被通知反制过

·Yes：正在被反制

Security

无线服务使用的安全方式：

·None：未配置安全方式

·WEP：WEP（Wired Equivalent Privacy，有线等效加密）方式

·WPA：WPA（Wi-Fi Protected Access，WIFI保护访问）方式

·WPA2：WPA第二版方式

Encrypt method

无线数据的加密方式：

·TKIP：TKIP（Temporal Key Integrity Protocol，`临时密钥完整性协议`）加密

·CCMP：CCMP（Counter mode with CBC-MAC Protocol，`[计数器模式搭配密码块链接－消息验证码协议`]）加密

·WEP：WEP（Wired Equivalent Privacy，有线等效加密）加密

·None：无加密方式

Authentication method

AP提供的接入无线网络的认证方式：

·None：无认证方式

·PSK： 采用PSK认证方式

·802.1X：采用802.1X认证方式

·Others：采用除PSK和802.1X之外的认证方式

Broadcast SSID

设备是否是广播SSID，如果AP不广播SSID，显示信息的SSID显示为空

Qos supported

是否支持QoS

Ad-hoc

是否是ad hoc

Beacon interval

信标间隔，单位为毫秒

Up duration

AP设备从启动到当前的持续时间

Total number of reported sensors

发现该设备的Sensor的数量

Sensor *n*

发现该设备的Sensor，*n*为系统自动的编号

Sensor ID

Sensor的ID，即Sensor的APID

Sensor name

检测到该无线设备的Sensor的名字

Radio ID

发现该设备的Sensor上的RadioID

RSSI

Sensor的信号强度

Channel

该Sensor最近一次探测到该设备的信道

First reported time

该Sensor第一次检测到该AP或无线客户端的时间

Last reported time

该Sensor最近一次检测到该AP或无线客户端的时间

Total number of associated clients

关联该设备的Client的数量

n

AP上关联的无线客户端的MAC地址，*n*为系统自动的编号

【相关命令】

·**reset wips virtual-security-domain device**

**WIPS \-- WIPS配置命令 \-- display wips virtual-security-domain countermeasure record**

------------------------------------------------------------------------

**[display**]** wips virtual-security-domain******countermeasure record**命令用来显示被反制过设备的信息。

【命令】

**[display**]** wips virtual-security-domain ***vsd-name*** countermeasure record**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[vsd-name*]：虚拟安全域的名称，为1～63个字符的字符串，区分大小写。

【举例】

\# 显示被反制过设备的信息。

\<Sysname\> display wips virtual-security-domain office countermeasure record

Total 3 times countermeasure, current 3 countermeasure record in virtual-

security-domain a

Class: Auth - authorization; Ext - extern; Mis - mistake;

       Unauth - unauthorized; Uncate - uncategorized;

       (A) - associate; (C) - config; (P) - potential

MAC address    Type   Class    Sensor name            Radio ID   Time

1000-0000-00e3 AP     Mis(C)   ap1                    1          2014-06-03/09:32:01

1000-0000-00e4 AP     Mis(C)   ap2                    1          2014-06-03/09:32:11

2000-0000-f282 Client Uncate   ap3                    1          2014-06-03/09:31:56

表1-5 display wips virtual-security-domain countermeasure record命令显示信息描述表

字段

描述

Total 3 times countermeasure, current 1024 countermeasure record in virtual-

security-domain a

累计成功通知反制次数，当前成功通知反制次数，最多可以显示1024条反制记录

MAC Address

检测到的无线设备的MAC地址

Type

无线设备的类型：

·AP：AP设备

·Client：客户端

Class

无线设备的分类类别

Sensor name

发起反制设备的Sensor名字

Radio ID

发起反制设备的Sensor的Radio ID

Time

通知反制的时间

【相关命令】

·**reset wips virtual-security-domain countermeasure record**

**WIPS \-- WIPS配置命令 \-- flood association-request**

------------------------------------------------------------------------

**[flood association-request**]命令用来配置检测关联请求帧泛洪攻击。

**[undo** **flood association-request**]命令用来恢复缺省情况。

【命令】

**[flood association-request** [ **interval** ]*interval-value*****[\| **quiet** ]*quiet-value *[\| **threshold** ]*number * \*]

**[undo flood association-request**]

【缺省情况】

不对关联请求帧泛洪攻击进行检测。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interval*** interval-value*]：检测关联请求帧的统计周期，取值范围为1～3600，单位为秒，缺省值为60秒。

**[quiet**]* quiet-value*：发送告警日志后的静默时间，取值范围为5～604800，单位为秒，缺省值为600秒。在静默期间，设备在统计周期内收到的关联请求帧即使达到触发告警阈值，设备也不会发送告警日志。

**[threshold**]* number*：检测关联请求帧达到触发阈值，取值范围为1～100000，缺省值为50。当设备检测到的关联请求帧达到触发阈值，即判定设备受到关联请求帧泛洪攻击，设备会发送告警日志。

【举例】

\# 配置检测关联请求帧泛洪攻击，统计周期为100秒，触发告警阈值为100，静默时间为360秒。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home flood association-request interval 100 threshold 100 quiet 360

**WIPS \-- WIPS配置命令 \-- flood authentication**

------------------------------------------------------------------------

**[flood authentication**]命令用来配置检测认证请求帧泛洪攻击。

**[undo** **flood authentication**]命令用来恢复缺省情况。

【命令】

**[flood authentication** [ **interval** ]*interval-value*****[\| **quiet** ]*quiet-value *[\| **threshold** ]*number * \*]

**[undo flood authentication**]

【缺省情况】

不对认证请求帧泛洪攻击进行检测。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interval*** interval-value*]：检测认证请求帧的统计周期，取值范围为1～3600，单位为秒，缺省值为60秒。

**[quiet**]* quiet-value*：发送告警日志后的静默时间，取值范围为5～604800，单位为秒，缺省值为600秒。在静默期间，设备在统计周期内收到的认证请求帧即使达到触发告警阈值，设备也不会发送告警日志。

**[threshold**]* number*：检测认证请求帧达到触发阈值，取值范围为1～100000，缺省值为50。当设备检测到的认证请求帧达到触发阈值，即判定设备受到认证请求帧泛洪攻击，设备会发送告警日志。

【举例】

\# 配置检测认证请求帧泛洪攻击，统计周期为100秒，触发告警阈值为100，静默时间为360秒。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home flood authentication interval 100 threshold 100 quiet 360

**WIPS \-- WIPS配置命令 \-- flood beacon**

------------------------------------------------------------------------

**[flood beacon**]命令用来配置检测Beacon帧泛洪攻击。

**[undo** **flood beacon**]命令用来恢复缺省情况。

【命令】

**[flood beacon** [ **interval** ]*interval-value*****[\| **quiet** ]*quiet-value *[\| **threshold** ]*number * \*]

**[undo flood beacon**]

【缺省情况】

不对Beacon帧泛洪攻击进行检测。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interval*** interval-value*]：检测Beacon帧的统计周期，取值范围为1～3600，单位为秒，缺省值为60秒。

**[quiet**]* quiet-value*：发送告警日志后的静默时间，取值范围为5～604800，单位为秒，缺省值为600秒。在静默期间，设备在统计周期内收到的Beacon帧即使达到触发告警阈值，设备也不会发送告警日志。

**[threshold**]* number*：检测Beacon帧达到触发阈值，取值范围为1～100000，缺省值为50。当设备检测到的Beacon帧达到触发阈值，即判定设备受到Beacon帧泛洪攻击，设备会发送告警日志。

【举例】

\# 配置检测Beacon帧泛洪攻击，统计周期为100秒，触发告警阈值为100，静默时间为360秒。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home flood beacon interval 100 threshold 100 quiet 360

**WIPS \-- WIPS配置命令 \-- flood block-ack**

------------------------------------------------------------------------

**[flood block-ack**]命令用来配置检测Block ACK帧泛洪攻击。

**[undo** **flood block-ack**]命令用来恢复缺省情况。

【命令】

**[flood block-ack** [ **interval** ]*interval-value*****[\| **quiet** ]*quiet-value *[\| **threshold** ]*number * \*]

**[undo flood block-ack**]

【缺省情况】

不对Block ACK帧泛洪攻击进行检测。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interval*** interval-value*]：检测Block ACK帧的统计周期，取值范围为1～3600，单位为秒，缺省值为60秒。

**[quiet**]* quiet-value*：发送告警日志后的静默时间，取值范围为5～604800，单位为秒，缺省值为600秒。在静默期间，设备在统计周期内收到的Block ACK帧即使达到触发告警阈值，设备也不会发送告警日志。

**[threshold**]* number*：检测Block ACK帧达到触发阈值，取值范围为1～100000，缺省值为50。当设备检测到的Block ACK帧达到触发阈值，即判定设备受到Block ACK帧泛洪攻击，设备会发送告警日志。

【举例】

\# 配置检测Block ACK帧泛洪攻击，统计周期为100秒，触发告警阈值为100，静默时间为360秒。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home flood block-ack interval 100 threshold 100 quiet 360

**WIPS \-- WIPS配置命令 \-- flood cts**

------------------------------------------------------------------------

**[flood cts**]命令用来配置检测CTS帧泛洪攻击。

**[undo** **flood cts**]命令用来恢复缺省情况。

【命令】

**[flood cts** [ **interval** ]*interval-value*****[\| **quiet** ]*quiet-value *[\| **threshold** ]*number * \*]

**[undo flood cts**]

【缺省情况】

不对CTS帧泛洪攻击进行检测。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interval*** interval-value*]：检测CTS帧的统计周期，取值范围为1～3600，单位为秒，缺省值为60秒。

**[quiet**]* quiet-value*：发送告警日志后的静默时间，取值范围为5～604800，单位为秒，缺省值为600秒。在静默期间，设备在统计周期内收到的CTS帧即使达到触发告警阈值，设备也不会发送告警日志。

**[threshold**]* number*：检测CTS帧达到触发阈值，取值范围为1～100000，缺省值为50。当设备检测到的CTS帧达到触发阈值，即判定设备受到CTS帧泛洪攻击，设备会发送告警日志。

【举例】

\# 配置检测CTS帧泛洪攻击，统计周期为100秒，触发告警阈值为100，静默时间为360秒。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home flood cts interval 100 threshold 100 quiet 360

**WIPS \-- WIPS配置命令 \-- flood deauthentication**

------------------------------------------------------------------------

**[flood deauthentication**]命令用来配置检测解认证帧（单播、广播）泛洪攻击。

**[undo** **flood deauthentication**]命令用来恢复缺省情况。

【命令】

**[flood deauthentication** [ **interval** ]*interval-value*****[\| **quiet** ]*quiet-value *[\| **threshold** ]*number * \*]

**[undo flood deauthentication**]

【缺省情况】

不对解认证帧泛洪攻击进行检测。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interval*** interval-value*]：检测解认证帧的统计周期，取值范围为1～3600，单位为秒，缺省值为60秒。

**[quiet**]* quiet-value*：发送告警日志后的静默时间，取值范围为5～604800，单位为秒，缺省值为600秒。在静默期间，设备在统计周期内收到的解认证帧即使达到触发告警阈值，设备也不会发送告警日志。

**[threshold**]* number*：检测解认证帧达到触发阈值，取值范围为1～100000，缺省值为50。当设备检测到的解认证帧达到触发阈值，即判定设备受到解认证帧泛洪攻击，设备会发送告警日志。

【举例】

\# 配置检测解认证帧泛洪攻击，统计周期为100秒，触发告警阈值为100，静默时间为360秒。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home flood deauthentication interval 100 threshold 100 quiet 360

**WIPS \-- WIPS配置命令 \-- flood disassociation**

------------------------------------------------------------------------

**[flood disassociation**]命令用来配置检测解关联帧泛洪攻击。

**[undo** **flood disassociation**]命令用来恢复缺省情况。

【命令】

**[flood disassociation** [ **interval** ]*interval-value*****[\| **quiet** ]*quiet-value *[\| **threshold** ]*number * \*]

**[undo flood disassociation**]

【缺省情况】

不对解关联帧泛洪攻击进行检测。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interval*** interval-value*]：检测解关联帧的统计周期，取值范围为1～3600，单位为秒，缺省值为60秒。

**[quiet**]* quiet-value*：发送告警日志后的静默时间，取值范围为5～604800，单位为秒，缺省值为600秒。在静默期间，设备在统计周期内收到的解关联帧即使达到触发告警阈值，设备也不会发送告警日志。

**[threshold**]* number*：检测解关联帧达到触发阈值，取值范围为1～100000，缺省值为50。当设备检测到的解关联帧达到触发阈值，即判定设备受到解关联帧泛洪攻击，设备会发送告警日志。

【举例】

\# 配置检测解关联帧泛洪攻击，统计周期为100秒，触发告警阈值为100，静默时间为360秒。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home flood disassociation interval 100 threshold 100 quiet 360

**WIPS \-- WIPS配置命令 \-- flood eapol-start**

------------------------------------------------------------------------

**[flood eapol-start**]命令用来配置检测EAPOL-Start帧泛洪攻击。

**[undo** **flood eapol-start**]命令用来恢复缺省情况。

【命令】

**[flood eapol-start** [ **interval** ]*interval-value*****[\| **quiet** ]*quiet-value *[\| **threshold** ]*number * \*]

**[undo flood eapol-start**]

【缺省情况】

不对EAPOL-Start帧泛洪攻击进行检测。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interval*** interval-value*]：检测EAPOL-Start帧的统计周期，取值范围为1～3600，单位为秒，缺省值为60秒。

**[quiet**]* quiet-value*：发送告警日志后的静默时间，取值范围为5～604800，单位为秒，缺省值为600秒。在静默期间，设备在统计周期内收到的EAPOL-Start帧即使达到触发告警阈值，设备也不会发送告警日志。

**[threshold**]* number*：检测EAPOL-Start帧达到触发阈值，取值范围为1～100000，缺省值为50。当设备检测到的EAPOL-Start帧达到触发阈值，即判定设备受到EAPOL-Start帧泛洪攻击，设备会发送告警日志。

【举例】

\# 配置检测EAPOL-Start帧泛洪攻击，统计周期为100秒，触发告警阈值为100，静默时间为360秒。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home flood eapol-start interval 100 threshold 100 quiet 360

**WIPS \-- WIPS配置命令 \-- flood null-data**

------------------------------------------------------------------------

**[flood null-data**]命令用来配置检测Null data帧泛洪攻击。

**[undo** **flood null-data**]命令用来恢复缺省情况。

【命令】

**[flood null-data** [ **interval** ]*interval-value*****[\| **quiet** ]*quiet-value *[\| **threshold** ]*number * \*]

**[undo flood null-data**]

【缺省情况】

不对Null data帧泛洪攻击进行检测。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interval*** interval-value*]：检测Null data帧的统计周期，取值范围为1～3600，单位为秒，缺省值为60秒。

**[quiet**]* quiet-value*：发送告警日志后的静默时间，取值范围为5～604800，单位为秒，缺省值为600秒。在静默期间，设备在统计周期内收到的Null data帧即使达到触发告警阈值，设备也不会发送告警日志。

**[threshold**]* number*：检测Null data帧达到触发阈值，取值范围为1～100000，缺省值为50。当设备检测到的Null data帧达到触发阈值，即判定设备受到Null data帧泛洪攻击，设备会发送告警日志。

【举例】

\# 配置检测Null data帧泛洪攻击，统计周期为100秒，触发告警阈值为100，静默时间为360秒。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home flood null-data interval 100 threshold 100 quiet 360

**WIPS \-- WIPS配置命令 \-- flood probe-request**

------------------------------------------------------------------------

**[flood probe-request**]命令用来配置探查请求帧泛洪攻击。

**[undo** **flood probe-request**]命令用来恢复缺省情况。

【命令】

**[flood probe-request** [ **interval** ]*interval-value*****[\| **quiet** ]*quiet-value *[\| **threshold** ]*number * \*]

**[undo flood probe-request**]

【缺省情况】

不对探查请求帧泛洪攻击进行检测。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interval*** interval-value*]：检测探查请求帧的统计周期，取值范围为1～3600，单位为秒，缺省值为60秒。

**[quiet**]* quiet-value*：发送告警日志后的静默时间，取值范围为5～604800，单位为秒，缺省值为600秒。在静默期间，设备在统计周期内收到的探查请求帧即使达到触发告警阈值，设备也不会发送告警日志。

**[threshold**]* number*：检测探查请求帧达到触发阈值，取值范围为1～100000，缺省值为50。当设备检测到的探查请求帧达到触发阈值，即判定设备受到探查请求帧泛洪攻击，设备会发送告警日志。

【举例】

\# 配置检测探查请求帧泛洪攻击，统计周期为100秒，触发告警阈值为100，静默时间为360秒。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home flood probe-request interval 100 threshold 100 quiet 360

**WIPS \-- WIPS配置命令 \-- flood reassociation-request**

------------------------------------------------------------------------

**[flood reassociation-request**]命令用来配置检测重关联帧泛洪攻击。

**[undo** **flood reassociation-request**]命令用来恢复缺省情况。

【命令】

**[flood reassociation-request** [ **interval** ]*interval-value*****[\| **quiet** ]*quiet-value *[\| **threshold** ]*number * \*]

**[undo flood reassociation-request**]

【缺省情况】

不对重关联帧泛洪攻击进行检测。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interval*** interval-value*]：检测重关联帧的统计周期，取值范围为1～3600，单位为秒，缺省值为60秒。

**[quiet**]* quiet-value*：发送告警日志后的静默时间，取值范围为5～604800，单位为秒，缺省值为600秒。在静默期间，设备在统计周期内收到的重关联帧即使达到触发告警阈值，设备也不会发送告警日志。

**[threshold**]* number*：检测重关联帧达到触发阈值，取值范围为1～100000，缺省值为50。当设备检测到的重关联帧达到触发阈值，即判定设备受到重关联帧泛洪攻击，设备会发送告警日志。

【举例】

\# 配置检测重关联帧泛洪攻击，统计周期为100秒，触发告警阈值为100，静默时间为360秒。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home flood reassociation-request interval 100 threshold 100 quiet 360

**WIPS \-- WIPS配置命令 \-- flood rts**

------------------------------------------------------------------------

**[flood rts**]命令用来配置检测RTS帧泛洪攻击。

**[undo** **flood rts**]命令用来恢复缺省情况。

【命令】

**[flood rts** [ **interval** ]*interval-value*****[\| **quiet** ]*quiet-value *[\| **threshold** ]*number * \*]

**[undo flood rts**]

【缺省情况】

不对RTS帧泛洪攻击进行检测。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interval*** interval-value*]：检测RTS帧的统计周期，取值范围为1～3600，单位为秒，缺省值为60秒。

**[quiet**]* quiet-value*：发送告警日志后的静默时间，取值范围为5～604800，单位为秒，缺省值为600秒。在静默期间，设备在统计周期内收到的RTS帧即使达到触发告警阈值，设备也不会发送告警日志。

**[threshold**]* number*：检测RTS帧达到触发阈值，取值范围为1～100000，缺省值为50。当设备检测到的RTS帧达到触发阈值，即判定设备受到RTS帧泛洪攻击，设备会发送告警日志。

【举例】

\# 配置检测RTS帧泛洪攻击，统计周期为100秒，触发告警阈值为100，静默时间为360秒。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home flood rts interval 100 threshold 100 quiet 360

**WIPS \-- WIPS配置命令 \-- import oui**

------------------------------------------------------------------------

**[import oui**]命令用来导入配置文件中的OUI信息。

**[undo import oui**]命令用来删除已导入的OUI信息。

【命令】

**[import oui **]*file-name*

**[undo import oui**]

【缺省情况】

没有导入配置文件的OUI信息。

【视图】

WIPS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[oui*]：导入配置文件名称，1～255个字符的字符串，不区分大小写，且文件名不能包含如下字符：[\\ / : \* ? " \< \> \|]。

【使用指导】

·该配置文件可以从IEEE网站下载。

·最多只能导入一个配置文件。

【举例】

\# 导入配置文件中的OUI信息。

\<Sysname\> system-view

Sysname wips

Sysname-wips import oui oui_import_cfg

【相关命令】

·**invalid-oui-classify illegal**

**WIPS \-- WIPS配置命令 \-- invalid-oui-classify illegal**

------------------------------------------------------------------------

**[invalid-oui-classify illegal**]命令用来配置对非法OUI的设备进行分类。

**[undo **]**invalid-oui-classify**命令用来恢复缺省情况。

【命令】

**[invalid-oui-classify illegal**]

**[undo invalid-oui-classify**]

【缺省情况】

不对非法OUI的设备进行分类。

【视图】

分类策略视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 配置对非法OUI的设备进行分类。

\<Sysname\> system-view

Sysname wips

Sysname-wips classification policy home

Sysname-wips-cls-home invalid-oui-classify illegal

【相关命令】

·**import oui**

**WIPS \-- WIPS配置命令 \-- malformed duplicated-ie**

------------------------------------------------------------------------

**[malformed duplicated-ie**]命令用来配置检测IE重复的畸形报文。

**[undo** **malformed duplicated-ie**]命令用来恢复缺省情况。

【命令】

**[malformed duplicated-ie** [ **quiet** *quiet-value*]**]

**[undo malformed duplicated-ie**]

【缺省情况】

不检测IE重复的畸形报文。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[quiet**]* quiet-value*：发送告警日志后的静默时间，取值范围为5～604800，单位为秒，缺省值为600秒。在静默期间，即使设备检测到IE重复的畸形报文，也不会发送告警日志。

【使用指导】

该检测是针对所有管理帧的检测。当解析某报文时，该报文所包含的某IE重复出现时，则检测该报文为重复IE畸形报文。因为厂商自定义IE是允许重复的，所以检测IE重复时，不需要考虑厂商自定义IE。

【举例】

\# 配置检测IE重复的畸形报文，静默时间为360秒。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home malformed duplicated-ie quiet 360

**WIPS \-- WIPS配置命令 \-- malformed fata-jack**

------------------------------------------------------------------------

**[malformed fata-jack**]命令用来配置检测Fata-Jack畸形报文。

**[undo** **malformed fata-jack**]命令用来恢复缺省情况。

【命令】

**[malformed fata-jack** [ **quiet** *quiet-value*]**]

**[undo malformed fata-jack**]

【缺省情况】

不检测Fata-Jack畸形报文。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[quiet**]* quiet-value*：发送告警日志后的静默时间，取值范围为5～604800，单位为秒，缺省值为600秒。在静默期间，即使设备检测到Fata-Jack畸形报文，也不会发送告警日志。

【使用指导】

该检测是针对认证帧的检测。Fata-jack畸形类型规定，当身份认证算法编号即Authentication algorithm number的值等于2时，则判定该帧为Fata-jack畸形报文。

【举例】

\# 配置检测Fata-Jack畸形报文，静默时间为360秒。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home malformed fata-jack quiet 360

**WIPS \-- WIPS配置命令 \-- malformed illegal-ibss-ess**

------------------------------------------------------------------------

**[malformed illegal-ibss-ess**]命令用来配置检测IBSS和ESS置位异常的畸形报文。

**[undo** **malformed illegal-ibss-ess**]命令用来恢复缺省情况。

【命令】

**[malformed illegal-ibss-ess** [ **quiet** *quiet-value*]**]

**[undo malformed illegal-ibss-ess**]

【缺省情况】

不检测IBSS和ESS置位异常的畸形报文。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[quiet**]* quiet-value*：发送告警日志后的静默时间，取值范围为5～604800，单位为秒，缺省值为600秒。在静默期间，即使设备检测到IBSS和ESS置位异常的畸形报文，也不会发送告警日志。

【使用指导】

该检测是针对Beacon帧和探查响应帧进行的检测。当报文中的IBSS和ESS都置位为1时，由于此种情况在协议中没有定义，所以这类报文被判定为IBSS和ESS置位异常的畸形报文。

【举例】

\# 配置检测IBSS和ESS置位异常的畸形报文，静默时间为360秒。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home malformed fata-jack quiet 360

**WIPS \-- WIPS配置命令 \-- malformed invalid-address-combination**

------------------------------------------------------------------------

**[malformed invalid-address-combination**]命令用来配置检测源地址为广播或者组播的认证和关联畸形报文。

**[undo** **malformed invalid-address-combination**]命令用来恢复缺省情况。

【命令】

**[malformed invalid-address-combination** [ **quiet** *quiet-value*]**]

**[undo malformed invalid-address-combination**]

【缺省情况】

不检测源地址为广播或者组播的认证和关联畸形报文。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[quiet**]* quiet-value*：发送告警日志后的静默时间，取值范围为5～604800，单位为秒，缺省值为600秒。在静默期间，即使设备检测到报文长度非法的畸形报文，也不会发送告警日志。

【使用指导】

该检测是针对所有管理帧的检测。当检测到该帧的TO DS等于1时，表明该帧为客户端发给AP的，如果同时又检测到该帧的源MAC地址为广播或组播，则该帧被判定为Invalid-source-address畸形报文。

【举例】

\# 配置检测源地址为广播或者组播的认证和关联畸形报文，静默时间为360秒。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home malformed invalid-address-combination quiet 360

**WIPS \-- WIPS配置命令 \-- malformed invalid-assoc-req**

------------------------------------------------------------------------

**[malformed invalid-assoc-req**]命令用来配置检测畸形关联请求报文。

**[undo** **malformed invalid-assoc-req**]命令用来恢复缺省情况。

【命令】

**[malformed invalid-assoc-req** [ **quiet** *quiet-value*]**]

**[undo malformed invalid-assoc-req**]

【缺省情况】

不检测畸形关联请求报文。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[quiet**]* quiet-value*：发送告警日志后的静默时间，取值范围为5～604800，单位为秒，缺省值为600秒。在静默期间，即使设备检测到畸形关联请求报文，也不会发送告警日志。

【使用指导】

该检测是针对认证请求帧的检测。当收到认证请求帧中的SSID长度等于零时，判定该报文为畸形关联请求报文。

【举例】

\# 配置检测畸形关联请求报文，静默时间为360秒。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home malformed invalid-assoc-req quiet 360

**WIPS \-- WIPS配置命令 \-- malformed invalid-auth**

------------------------------------------------------------------------

**[malformed invalid-auth**]命令用来配置检测畸形认证请求报文。

**[undo** **malformed invalid-auth**]命令用来恢复缺省情况。

【命令】

**[malformed invalid-auth** [ **quiet** *quiet-value*]**]

**[undo malformed invalid-auth**]

【缺省情况】

不检测畸形认证请求报文。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[quiet**]* quiet-value*：发送告警日志后的静默时间，取值范围为5～604800，单位为秒，缺省值为600秒。在静默期间，即使设备检测到畸形认证请求报文，也不会发送告警日志。

【使用指导】

该检测是针对认证帧的检测。当检测到以下情况时请求认证过程失败，会被判断判定为认证畸形报文。

·当对认证帧的身份认证算法编号（Authentication algorithm number）的值不符合协议规定，并且其值大于3时；

·当标记客户端和AP之间的身份认证的进度的Authentication Transaction Sequence Number 的值等于1，且状态代码status code不为零时；

·当Authentication Transaction Sequence Number的值大于4时。

【举例】

\# 配置检测畸形认证请求报文，静默时间为360秒。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home malformed invalid-auth quiet 360

**WIPS \-- WIPS配置命令 \-- malformed invalid-deauth-code**

------------------------------------------------------------------------

**[malformed invalid-deauth-code**]命令用来配置检测含有无效原因值的解认证畸形报文。

**[undo** **malformed invalid-deauth-code**]命令用来恢复缺省情况。

【命令】

**[malformed invalid-deauth-code** [ **quiet** *quiet-value*]**]

**[undo malformed invalid-deauth-code**]

【缺省情况】

不检测含有无效原因值的解认证畸形报文。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[quiet**]* quiet-value*：发送告警日志后的静默时间，取值范围为5～604800，单位为秒，缺省值为600秒。在静默期间，即使设备检测到含有无效原因值的解认证畸形报文，也不会发送告警日志。

【使用指导】

该检测是针对解认证畸形帧的检测。当解认证畸形帧携带的Reason code的值属于集合0，67～65535时，则属于协议中的保留值，此时判定该帧为含有无效原因值的解认证畸形报文。

【举例】

\# 配置检测含有无效原因值的解认证畸形报文，静默时间为360秒。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home malformed invalid-deauth-code quiet 360

**WIPS \-- WIPS配置命令 \-- malformed invalid-disassoc-code**

------------------------------------------------------------------------

**[malformed invalid-disassoc-code**]命令用来配置检测含有无效原因值的解关联畸形报文。

**[undo** **malformed invalid-disassoc-code**]命令用来恢复缺省情况。

【命令】

**[malformed invalid-disassoc-code** [ **quiet** *quiet-value*]**]

**[undo malformed invalid-disassoc-code**]

【缺省情况】

不检测含有无效原因值的解关联畸形报文。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[quiet**]* quiet-value*：发送告警日志后的静默时间，取值范围为5～604800，单位为秒，缺省值为600秒。在静默期间，即使设备检测到含有无效原因值的解关联畸形报文，也不会发送告警日志。

【使用指导】

该检测是针对解关联帧的检测。当解关联帧携带的Reason code的值属于集合0，67～65535时，则属于协议中的保留值，此时判定该帧为含有无效原因值的解关联畸形报文。

【举例】

\# 配置检测含有无效原因值的解关联畸形报文，静默时间为360秒。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home malformed invalid-disassoc-code quiet 360

**WIPS \-- WIPS配置命令 \-- malformed invalid-ht-ie**

------------------------------------------------------------------------

**[malformed invalid-ht-ie**]命令用来配置检测畸形HT IE报文。

**[undo** **malformed invalid-ht-ie**]命令用来恢复缺省情况。

【命令】

**[malformed invalid-ht-ie** [ **quiet** *quiet-value*]**]

**[undo malformed invalid-ht-ie**]

【缺省情况】

不检测畸形HT IE报文。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[quiet**]* quiet-value*：发送告警日志后的静默时间，取值范围为5～604800，单位为秒，缺省值为600秒。在静默期间，即使设备检测到畸形HT IE报文，也不会发送告警日志。

【使用指导】

该检测是针对Beacon、探查响应帧、关联响应帧、重关联响应帧的检测。当检测到以下情况时，判定为HT IE的畸形报文，发出告警，在静默时间内不再告警。

·解析出HT Capabilities IE的SM Power Save值为2时；

·解析出HT Operation IE 的Secondary Channel Offset值等于2时。

【举例】

\# 配置检测畸形HT IE报文，静默时间为360秒。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home malformed invalid-ht-ie quiet 360

**WIPS \-- WIPS配置命令 \-- malformed invalid-ie-length**

------------------------------------------------------------------------

**[malformed invalid-ie-length**]命令用来配置检测IE长度非法的畸形报文。

**[undo** **malformed invalid-ie-length**]命令用来恢复缺省情况。

【命令】

**[malformed invalid-ie-length** [ **quiet** *quiet-value*]**]

**[undo malformed invalid-ie-length**]

【缺省情况】

不检测IE长度非法的畸形报文。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[quiet**]* quiet-value*：发送告警日志后的静默时间，取值范围为5～604800，单位为秒，缺省值为600秒。在静默期间，即使设备检测到IE长度非法的畸形报文，也不会发送告警日志。

【使用指导】

该检测是针对所有管理帧的检测。信息元素（Information Element，简称IE）是管理帧的组成元件，其长度不定。信息元素通常包含一个元素识别码位（Element ID）、一个长度位（Length）以及一个长度不定的位。每种类型的管理帧包含特定的几种IE，IE的长度的取值范围应遵守最新802.11协议的规定。报文解析过程中，当检测到该报文包含的某个IE的长度为非法时，该报文被判定为IE长度非法的畸形报文。

【举例】

\# 配置检测IE长度非法的畸形报文，静默时间为360秒。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home malformed invalid-ie-length quiet 360

**WIPS \-- WIPS配置命令 \-- malformed invalid-pkt-length**

------------------------------------------------------------------------

**[malformed invalid-pkt-length**]命令用来配置检测报文长度非法的畸形报文。

**[undo** **malformed invalid-pkt-length**]命令用来恢复缺省情况。

【命令】

**[malformed invalid-pkt-length** [ **quiet** *quiet-value*]**]

**[undo malformed invalid-pkt-length**]

【缺省情况】

不检测报文长度非法的畸形报文。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[quiet**]* quiet-value*：发送告警日志后的静默时间，取值范围为5～604800，单位为秒，缺省值为600秒。在静默期间，即使设备检测到报文长度非法的畸形报文，也不会发送告警日志。

【使用指导】

该检测是针对所有管理帧的检测。当解析完报文主体后，IE的剩余长度不等于零时，则该报文被判定为报文长度非法畸形报文。

【举例】

\# 配置检测报文长度非法的畸形报文，静默时间为360秒。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home malformed invalid-pkt-length quiet 360

**WIPS \-- WIPS配置命令 \-- malformed large-duration**

------------------------------------------------------------------------

**[malformed large-duration**]命令用来配置检测Duration字段超大的畸形报文。

**[undo** **malformed large-duration**]命令用来恢复缺省情况。

【命令】

**[malformed large-duration**[ [ **quiet** *quiet-value* \| ]]****threshold ***value *]

**[undo malformed large-duration**]

【缺省情况】

不检测Duration字段超大的畸形报文。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[quiet**]* quiet-value*：发送告警日志后的静默时间，取值范围为5～604800，单位为秒，缺省值为600秒。在静默期间，即使设备检测到Duration字段超大的畸形报文，也不会发送告警日志。

**[threshold**]*value*：检测报文中Duration字段超大的触发阈值，取值范围为1～32767，缺省值为5000。当设备检测报文的Duration字段达到触发阈值，即判定设备受到Duration字段超大的畸形报文，设备会发送告警日志。

【使用指导】

该检测是针对单播管理帧、单播数据帧以及RTS、CTS、ACK帧的检测。如果报文解析结果中该报文的Duration值大于指定的门限值，则为Duration超大的畸形报文。

【举例】

\# 配置检测Duration字段超大的畸形报文，静默时间为360秒。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home malformed large-duration quiet 360

**WIPS \-- WIPS配置命令 \-- malformed null-probe-resp**

------------------------------------------------------------------------

**[malformed null-probe-resp**]命令用来配置检测无效探查响应报文。

**[undo** **malformed null-probe-resp**]命令用来恢复缺省情况。

【命令】

**[malformed null-probe-resp** [ **quiet** *quiet-value*]**]

**[undo malformed null-probe-resp**]

【缺省情况】

不检测无效探查响应报文。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[quiet**]* quiet-value*：发送告警日志后的静默时间，取值范围为5～604800，单位为秒，缺省值为600秒。在静默期间，即使设备检测到无效探查响应报文，也不会发送告警日志。

【使用指导】

该检测是针对探查响应报文。当检测到该帧为非Mesh帧，但同时该帧的SSID Length等于零，这种情况不符合协议（协议规定SSID等于零的情况是Mesh帧），则判定为无效探查响应报文。

【举例】

\# 配置检测无效探查响应报文，静默时间为360秒。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home malformed null-probe-resp quiet 360

**WIPS \-- WIPS配置命令 \-- malformed overflow-eapol-key**

------------------------------------------------------------------------

**[malformed overflow-eapol-key**]命令用来配置检测key长度超长的EAPOL报文。

**[undo** **malformed overflow-eapol-key**]命令用来恢复缺省情况。

【命令】

**[malformed overflow-eapol-key** [ **quiet** *quiet-value*]**]

**[undo malformed overflow-eapol-key**]

【缺省情况】

不检测key长度超长的EAPOL报文。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[quiet**]* quiet-value*：发送告警日志后的静默时间，取值范围为5～604800，单位为秒，缺省值为600秒。在静默期间，即使设备检测到key长度超长的EAPOL报文，也不会发送告警日志。

【使用指导】

该检测是针对EAPOL-Key帧的检测。当检测到该帧的TO DS等于1且其Key Length大于零时，则判定该帧为key长度超长的EAPOL报文。Key length长度异常的恶意的EAPOL-Key帧可能会导致DOS攻击。

【举例】

\# 配置检测key长度超长的EAPOL报文，静默时间为360秒。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home malformed overflow-eapol-key quiet 360

**WIPS \-- WIPS配置命令 \-- malformed overflow-ssid**

------------------------------------------------------------------------

**[malformed overflow-ssid**]命令用来配置检测SSID长度超长的畸形报文。

**[undo** **malformed overflow-ssid**]命令用来恢复缺省情况。

【命令】

**[malformed overflow-ssid** [ **quiet** *quiet-value*]**]

**[undo malformed overflow-ssid**]

【缺省情况】

不检测SSID长度超长的畸形报文。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[quiet**]* quiet-value*：发送告警日志后的静默时间，取值范围为5～604800，单位为秒，缺省值为600秒。在静默期间，即使设备检测到SSID长度超长的畸形报文，也不会发送告警日志。

【使用指导】

该检测是针对Beacon、探查请求、探查响应、关联请求帧的检测。当解析报文的SSID length大于32字节时，不符合协议规定的0～32字节的范围，则判定该帧为SSID超长的畸形报文。

【举例】

\# 配置检测SSID长度超长的畸形报文，静默时间为360秒。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home malformed overflow-ssid quiet 360

**WIPS \-- WIPS配置命令 \-- malformed redundant-ie**

------------------------------------------------------------------------

**[malformed redundant-ie**]命令用来配置检测多余IE畸形报文。

**[undo** **malformed redundant-ie**]命令用来恢复缺省情况。

【命令】

**[malformed redundant-ie** [ **quiet** *quiet-value*]**]

**[undo malformed redundant-ie**]

【缺省情况】

不检测多余IE畸形报文。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[quiet**]* quiet-value*：发送告警日志后的静默时间，取值范围为5～604800，单位为秒，缺省值为600秒。在静默期间，即使设备检测到多余IE畸形报文，也不会发送告警日志。

【使用指导】

该检测是针对所有管理帧的检测。报文解析过程中，当遇到既不属于报文应包含的IE，也不属于reserved IE时，判断该IE为多余IE，则该报文被判定为多余IE畸形报文。

【举例】

\# 配置检测多余IE畸形报文，静默时间为360秒。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home malformed redundant-ie quiet 360

**WIPS \-- WIPS配置命令 \-- manual-classify mac-address**

------------------------------------------------------------------------

**[manual-classify mac-address**]命令用来配置手工AP分类。

**[undo manual-classify mac-address**]命令用来删除手动AP分类。

【命令】

**[manual-classify mac-address**[ *mac*-*address* { **authorized-ap** \| **external-ap** \| **misconfigured-ap** \| **rogue-ap** }]]

**[undo manual-classify mac-address**[ { *mac*-*address* \| **all** }]]

【缺省情况】

没有对AP进行手工分类。

【视图】

分类策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mac*]-*address*：AP的MAC地址，格式为H-H-H。

**[authorized-ap**]：将指定AP设置为授权AP。

**[external-ap**]：将指定AP设置为外部AP。

**[misconfigured-ap**]：将指定AP设置为配置错误的AP。

**[rogue-ap**]：将指定AP设置为Rogue AP。

**[all**]：所有AP。

【举例】

\# 将MAC地址为000f-00e2-0001的AP配置为授权AP。

\<Sysname\> system-view

Sysname wips

Sysname-wips classification policy home

Sysname-wips-cls-home manual-classify mac-address 000f-00e2-0001 authorized-ap

**WIPS \-- WIPS配置命令 \-- reset wips statistics**

------------------------------------------------------------------------

**[reset wips statistics**]命令用来清除所有Sensor上报的信息。

【命令】

**[reset wips statistics**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 清除所有Sensor上报的信息。

\<Sysname\> reset wips statistics

【相关命令】

·**display wips statistic****s receive**

**WIPS \-- WIPS配置命令 \-- reset wips virtual-security-domain**

------------------------------------------------------------------------

**[reset wips virtual-security-domain**]命令用来清除VSD内学习到的AP表项和客户端表项。

【命令】

**[reset wips virtual-security-domain ***vsd-name* **device** ** **all**[ \| **mac-address**]*****mac-address *[} \|[ **client**] **[ \| ]]**mac-address***mac-address*[ } \| **[all]** }]

【视图】]

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vsd-name*]：虚拟安全域的名称，为1～63个字符的字符串，区分大小写。

**[device**]：虚拟安全域中检测到的设备。

**[ap**]：虚拟安全域中检测到的AP。

**[all**]：虚拟安全域中检测到的所有AP。

**[mac-address**]*****mac-address*：指定AP的MAC地址。

**[client**]：虚拟安全域中检测到的客户端。

**[all**]：虚拟安全域中检测到的所有客户端。

**[mac-address**]*****mac-address*：指定客户端的MAC地址。

**[all**]：虚拟安全域中检测到的所有AP和客户端。

【举例】

\# 清除VSD aaa内学习到的AP表项和客户端表项。

\<Sysname\> reset wips virtual-security-domain aaa device all

【相关命令】

·**display wips virtual-security-domain device**

**WIPS \-- WIPS配置命令 \-- reset wips virtual-security-domain countermeasure record**

------------------------------------------------------------------------

**[reset wips virtual-security-domain countermeasure record**]命令用来清除指定VSD内所有被反制过的设备信息。

【命令】

**[reset wips virtual-security-domain ***vsd-name*** countermeasure record**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vsd-name*]：虚拟安全域的名称，为1～63个字符的字符串，区分大小写。

【举例】

\# 清除指定VSD内所有被反制过的设备信息。

\<Sysname\> reset wips virtual-security-domain aaa countermeasure record

【相关命令】

·**display wips virtual-security-domain countermeasure record**

**WIPS \-- WIPS配置命令 \-- trust mac-address**

------------------------------------------------------------------------

**[trust mac-address**]命令用来将指定的MAC地址添加到静态信任列表中。

**[undo trust mac-address**]命令用来删除静态信任列表中的MAC地址。

【命令】

**[trust mac-address**]*mac-address*

**[undo trust mac-address***mac-address*[ \| **all** }]

【缺省情况】]

静态信任列表中不存在MAC地址。

【视图】

分类策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mac-address*]：AP或客户端的MAC地址。

**[all**]：所有MAC地址。

【举例】

\# 将MAC地址78AC-C0AF-944F添加到静态信任列表中。

\<Sysname\> system-view

Sysname wips

Sysname-wips classification policy home

Sysname-wips-cls-home trust mac-address 78AC-C0AF-944F

**WIPS \-- WIPS配置命令 \-- trust oui**

------------------------------------------------------------------------

**[trust oui**]命令用来将指定的OUI添加到静态信任列表中。

**[undo trust oui**]命令用来删除静态信任列表中的OUI。

【命令】

**[trust oui***oui*]

**[undo trust**]**oui**[{ *oui* \| **all** }]

【缺省情况】

静态信任列表中不存在OUI。

【视图】

分类策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[oui*]：OUI名称，为6个字符的字符串，不区分大小写。

**[all**]：所有OUI。

【举例】

\# 将名为000fe4、000fe5的OUI添加到静态信任列表中。

\<Sysname\> system-view

Sysname wips

Sysname-wips classification policy home

Sysname-wips-cls-home trust oui 000fe4

Sysname-wips-cls-home trust oui 000fe5

**WIPS \-- WIPS配置命令 \-- trust ssid**

------------------------------------------------------------------------

**[trust ssid**]命令用来将指定的SSID添加到静态信任列表中。

**[undo trust ssid**]命令用来删除静态信任列表中的SSID。

【命令】

**[trust ssid **]*ssid-name*

**[undo trust**]**ssid***[ssid-name*[ \| **all** }]

【缺省情况】]

静态信任列表中不存在SSID。

【视图】

分类策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ssid-name*]：SSID的名称，为1～32个字符的字符串，区分大小写。

**[all**]：所有SSID。

【举例】

\# 将名为flood1的SSID添加到静态信任列表中。

\<Sysname\> system-view

Sysname wips

Sysname-wips classification policy home

Sysname-wips-cls-home trust ssid flood1

**WIPS \-- WIPS配置命令 \-- virtual-security-domain**

------------------------------------------------------------------------

**[virtual-security-domain**]命令用来创建VSD（Virtual Security Domain，虚拟安全域），并进入VSD视图。

**[undo virtual-security-domain**]命令用来删除已创建的VSD。

【命令】

**[virtual-security-domain**]* vsd-name*

**[undo virtual-security-domain**] *vsd-name*

【缺省情况】

不存在VSD。

【视图】

WIPS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vsd-name*]：虚拟安全域的名称，为1～63个字符的字符串，区分大小写。

【举例】

\# 创建名为office的VSD，并进入VSD视图。

\<Sysname\> system-view

Sysname wips

Sysname-wips virtual-security-domain office

Sysname-wips-vsd-office

**WIPS \-- WIPS配置命令 \-- weak-iv**

------------------------------------------------------------------------

**[weak-iv**]命令用来检测弱初始化向量。

**[undo** **weak-iv**]命令用来恢复缺省情况。

【命令】

**[weak-iv** [ **quiet** *quiet-value* ]]

**[undo weak-iv**]

【缺省情况】

不检测弱初始化向量。

【视图】

攻击检测策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[quiet**]* quiet-value*：发送告警日志后的静默时间，取值范围为5～604800，单位为秒，缺省值为600秒。在静默期间，设备再次检测到初始化向量也不会发送告警日志。

【使用指导】

设备检测到弱初始化向量后会发送告警日志。

【举例】

\# 配置检测弱初始化向量。

\<Sysname\> system-view

Sysname wips

Sysname-wips detect policy home

Sysname-wips-dtc-home weak-iv

**WIPS \-- WIPS配置命令 \-- wips**

------------------------------------------------------------------------

**[wips**]命令用来进入WIPS视图。

**[undo **]**wips**命令用来删除WIPS视图下所有配置。

【命令】

**[wips**]

**[undo wips**]

【缺省情况】

没有配置WIPS视图。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 进入WIPS视图。

\<Sysname\> system-view

Sysname wips

Sysname-wips

**WIPS \-- WIPS配置命令 \-- wips enable**

------------------------------------------------------------------------

**[wips enable**]命令用来开启WIPS功能。

**[undo** **wips enable**]命令用来恢复缺省情况。

【命令】

**[wips enable**]

**[undo wips enable**]

【缺省情况】

WIPS功能处于关闭状态。

【视图】

Radio视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 开启WIPS功能。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA2620i-AGN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 wips enable

**WIPS \-- WIPS配置命令 \-- wips virtual-security-domain**

------------------------------------------------------------------------

**[wips virtual-security-domain**]命令用来将AP加入到指定的VSD中。

**[undo wips virtual-security-domain**]命令用来删除已加入VSD的AP。

【命令】

**[wips virtual-security-domain **]*vsd-name*

**[undo wips virtual-security-domain**]

【缺省情况】

没有将AP加入到指定的VSD中。

【视图】

AP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vsd-name*]：虚拟安全域的名称，为1～63个字符的字符串，区分大小写。

【举例】

\# 将ap1加入到名为office的VSD中。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA2620i-AGN

Sysname-wlan-ap-ap1 wips virtual-security-domain office

