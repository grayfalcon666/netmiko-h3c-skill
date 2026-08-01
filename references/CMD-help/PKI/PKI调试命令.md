<!-- CMD-INDEX
  debugging pki                       | 用户视图             | L5
-->

**PKI \-- PKI调试命令 \-- debugging pki**

------------------------------------------------------------------------

【命令】

**[debugging pki **[{ **access-control-policy** \| **all** \| **error** \| **event** \| **request** [ **verbose** ] \| **verify** \| **retrieve**  **verbose**  }]]

**[undo debugging pki**[ { **access-control-policy** \| **all** \| **error** \| **event** \| **request** [ **verbose** ] \| **verify** \| **retrieve**  **verbose**  }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[access-control-policy**]：表示访问控制策略调试信息开关。

**[all**]：表示所有PKI调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

**[request**]：表示证书申请调试信息开关。

**[verify**]：表示证书验证调试信息开关。

**[retrieve**]：表示获取证书和获取CRL调试信息开关。

**[verbose**]：表示详细调试信息开关。

【描述】

**[debugging pki **]命令用来打开PKI调试开关。**undo debugging pki**命令用来关闭PKI调试信息开关。

缺省情况下，PKI调试信息开关处于关闭状态。

表1-1 debugging pki error命令输出信息描述表

字段

描述

Failed to get purpose of key pair.

获取密钥用途失败

The process is running. Unable to start the process.

有同样的进程正在运行，不能启动现有申请程序

The local public key and the public key in the received certificate did not match.

本地设备上的公钥和从接收到的证书中得到的公钥不匹配

Failed to get the CA certificate chain.

获取CA 证书链失败

Failed to verify local certificates. Verification result: *result-string*

验证本地证书失败。验证结果为*result-string*

SCEP: Failed to get local certificate.

获取本地证书失败

Failed to request certificate.

证书申请失败

Failed to start certificate request process.

启动申请证书程序失败

Failed to get CRLs.

获取CRL失败

Failed to get CA/RA certificates.

获取CA/RA证书失败

Failed to get local public key.

获取本地密钥对失败

Failed to create PKCS#10 certificate request.

创建PKCS#10类型的证书申请失败

Failed to get subject name from request.

从申请中获取主题名称失败

Failed to get issuer name from request.

从申请中获取颁发者名称失败

Failed to get issuer name from CA certificate.

从CA证书获取证书颁发者名称失败

Failed to get serial number from CA certificate.

从CA证书获取序列号失败

PKCS#7 envelope: Failed to create certificate stack.

建立证书栈失败

PKCS#7 develope: Failed to get ASN.1 object.

获取ASN.1格式的对象失败

PKCS#7 develope: Failed to find attribute.

查找属性失败

PKCS#7 develope: Failed to get ASN.1 string.

获取ASN.1字符串失败

PKCS#7 develope: Failed to get PKI status in reply.

在回应报文中获取PKI状态信息失败

.PKCS#7 develope: Wrong failure information in reply.

回应报文中错误的失败信息

PKCS#7 develope: Failed to get recipient nonce from reply.

从回应报文中获取服务器回应的nonce失败

PKCS#7 develope: Received nonce is inconsistent with sender nonce.

服务器回应的nonce与本地的sender nonce不一致

PKCS#7 develope: Failed to get sender nonce from reply.

在回应报文中获取不到服务器的sender nonce

PKCS#7 develope: Wrong message type *error_type*.

错误的消息类型，具体类型为*error_type*

PKCS#7 develope: Failed to get transaction ID from reply.

从回应报文中无法获取transaction ID信息

PKCS#7 develope: Transaction ID mismatched, received transaction ID is: *trans-id*.

transaction ID 信息不匹配，接收到的Transaction ID为*trans-id*

PKCS#7 develope: Reply message is not signed.

PKCS#7格式的回应报文没有被签名

PKCS#7 develope: Failed to get reply signer information.

不能获取回应报文中签名者信息

PKCS#7 develope: Failed to verify signature.

验证签名失败

PKCS#7 develope: Failed to read inner PKCS#7.

不能读取内层PKCS#7格式的消息

PKCS#7 develope: Failed to decrypt inner PKCS#7.

解密内层PKCS#7格式的消息失败

PKCS#7 develope: Illegal size of payload.

非法的载荷大小

No certificate in reply message.

在回应报文中没有证书信息

Failed to get CRLs from reply.

在回应报文中无法获取CRL列表信息

Failed to get CRL data in CRLs from reply.

无法获取到回应报文中的CRL列表里的表信息

PKCS#7 develope: Error reason: *string*.

解析回应报文失败的错误原因为*string*

Failed to wrap PKCS#7 message.

封装PKCS#7格式的消息失败

Failed to parse URL.

解析URL信息失败

Failed to create socket. Error code: *error-code.*

建立socket连接失败，错误码为*error-code*

Failed to get response payload.

获取响应载荷失败

Failed to get response type.

获取响应类型失败

Failed to read response message. Error code: *error-code*.

读取响应信息失败，错误码为*error-code*

Failed to unwrap PKCS#7 message.

解封装PKCS#7格式的消息失败

Polling counter reaches the upper limit.

轮询计数器已达到最大值

Unknown return status *status-code.*

未知的返回状态码为*status-code*

Failed to send SCEP message.

发送SCEP消息失败

SCEP: Failed to get CA/RA certificates.

获取CA/RA证书失败

Failed to initiate SCEP.

初始化SCEP失败

Failed to get options of the SCEP process.

解析命令行，获取程序运行参数失败

Unable to continue current SCEP process.

不能继续执行当前SCEP程序

Failed to initialize signal.

初始化信号失败

PKCS#7 envelope: Failed to add signed certificate to PKCS#7 request.

添加签名证书到PKCS#7格式的请求失败

PKCS#7 envelope: Failed to sign PKCS#7 request.

签名PKCS#7格式的请求失败

PKCS#7 envelope: Failed to set signature attribute.

设置签名属性失败

PKCS#7 envelope: Failed to create PKCS#7 data.

创建PKCS#7格式的数据失败

SCEP: Failed to encode data in BASE64.

将数据编码为BASE64 类型时失败

PKCS#7 develope: Failed to get attributes.

获取属性失败

PKCS#7 develope: Failed to handle signature's attributes.

处理签的名属性失败

Failed to bind port. Error code: *error-code*.

通信端口绑定错误，错误码为*error-code*

Failed to connect to the CA server. Error code: *error-code*.

与CA服务器连接失败，错误码为*error-code*

SCEP: Failed to create message.

构造消息失败

Failed to create self-signed certificate.

创建自签名证书失败

PKCS#7 develope: Wrong PKI status.

PKI状态错误

PKCS#7 develope: Failed to get failure information from reply.

从回应中获取失败信息失败

PKCS#7 develope: Wrong PKI status in reply. Status code: *status-code*.

回应报文中错误的PKI状态，状态码为*status-code*

The signing or encryption is running with general at the same time, can\'t start current enroll process.

签名或加密程序和通用程序在同一时间运行，不能启动证书申请程序

Failed to start the getCRL process.

启动获取CRL的程序失败

CRL verification result: *string*

验证CRL的结果为*string*，*string*内容可包括：

(1)ok：成功

(1)unable to get issuer certificate：不能获取签发者的证书

(2)unable to get certificate CRL：不能获取证书的CRL

(3)unable to decrypt certificate\'s signature：不能解密证书的签名

(4)unable to decrypt CRL\'s signature：不能解密CRL的签名

(5)unable to decode issuer public key：不能解码签发都的公钥

(6) certificate signature failure：证书签名失败

(7)CRL signature failure ：CRL签名失败

(8)certificate is not yet valid：证书不是有效的

(9)CRL is not yet valid CRL：不是有效的

(10)certificate has expired：证书已经到期

(11)CRL has expired CRL：已经到期

(12)format error in certificate\'s notBefore field：证书有效日期的起始时间错误

(13)format error in certificate\'s notAfter field：证书有效日期的终止时间错误

(14)format error in CRL\'s lastUpdate field：CRL的最后更新域错误

(15)format error in CRL\'s nextUpdate field：CRL的下次更新域错误

(16)out of memory：内存不足

(17)self signed certificate：自签名证书

(18)self signed certificate in certificate chain：自签名证书在证书链中

(19)unable to get local issuer certificate：不能获取本地签发者的证书

(20)unable to verify the first certificate：不能验证第一个证书

(21)certificate chain too long：证书链太长

(22)certificate revoked：证书被调销

(23)invalid CA certificate：无效的CA证书

(24)invalid non-CA certificate (has CA markings) ：无效的non-CA证书（包含CA 记号）

(25) path length constraint exceeded：路径长度限制过度

(26)proxy path length constraint exceeded：代理人路径长度限制过度

(27)proxy certificates not allowed, please set the appropriate flag：代理人证书没有被允许，请设置通行标志

(28)unsupported certificate purpose：不支持证书意图

(29)certificate not trusted：证书不可信

(30)certificate rejected：证书被拒决

(31)application verification failure：证书验证失败

(32)subject issuer mismatch：subject 名称和issuer名称不匹配

(33)authority and subject key identifier mismatch：授权和subject key标识符不匹配

(34)authority and issuer serial number mismatch：授权和签发者序列号不匹配

(35) key usage does not include certificate signing：密钥用途不包含给证书签名的用途

(36)unable to get CRL issuer certificate：不能获取CRL签发者的证书

(37)unhandled critical extension：不能处理鉴定扩展

(38) key usage does not include CRL signing密钥：用途不包含给CRL签名的用途

(39)key usage does not include digital signature：密钥用途不包含数字签名的用途

(40) unhandled critical CRL extension：不能处理鉴定CRL扩展

(41)invalid or inconsistent certificate extension：无效的或不一致的证书扩展

(42)invalid or inconsistent certificate policy extension：无效的或不一致的证书策略扩展

(43)no explicit policy：没有清楚的策略

(44)Different CRL scope：不同的CRL范围

(45)Unsupported extension feature：不支持扩展属性

(46)RFC 3779 resource not subset of parent\'s resources RFC 3779：资源没有父母资源的子集

(47)permitted subtree violation：允许违背子树集

(48)excluded subtree violation：排斥违背子树集

(49)name constraints minimum and maximum not supported：不支持最大或最小名称限限制

(50)unsupported name constraint type：不支持名称类型限制

(51)unsupported or invalid name constraint syntax：不支持或无效的名称限制语法

(52)unsupported or invalid name syntax：不支持或无效的名称语法

(53)CRL path validation error ：CRL路径确认错误

CRL retrieval failed: Certificate request URL is not configured.

获取证书的URL没有配置

CRL retrieval failed: Certificate request from is not configured.

获取证书的注册受理机构没有配置

CRL retrieval failed: No local certificate.

没有本地证书

CRL retrieval failed: No RA certificate.

没有RA证书

CRL retrieval failed: The local public key and the public key in the local certificate are mismatching.

本地证书里的公钥和本地公钥不匹配

Failed to retrieve CRLs.

获取CRL失败

CA certificate doesn't exist.

CA证书不存在

Local certificate and public key don't match.

本地证书和公钥不匹配

Failed to get data by curl.

通过curl获取数据失败

Failed to save the local certificate to the device.

存储本地证书失败

Failed to verify the peer certificates.Verification result: *result-string.*

验证对端证书失败，验证结果为*result-string*

The signature or encryption is running with general at the same time, can\'t start current enroll process.

签名或加密用途证书的申请程序不能和通用用途证书的申请程序同时启动，不能启动当前申请程序

Failed to generate the extension attributes for PKCS#10 request.

产生PKCS#10申请的扩展属性失败

Incomplete DN configuration.

DN配置不完整

Failed to save the peer certificates to the device.

保存对端证书到设备失败

Invalid PKI entity.

实体无效

Failed to get the certificate chain.

获取证书链失败

Certificate retrieval failed: The identity of the entity *entity-name* is not configured.

获取证书失败，未配置实体的*entity-name*身份信息

Failed to get the source IP address of PKI traffic.

获取PKI协议报文的源IP地址失败

Failed to verify the CA/RA certificate chain, Verification result: *result-string*

验证CA/RA证书链失败，验证结果为*result-string*

Failed to save the CA/RA certificate chain.

保存CA/RA证书链失败

Failed to get the encryption certificate.

获取加密用途的证书失败

The local cert is

:*local-cert*

本地证书的内容为：*local-cert*

Local Certificate and key is not matched.

本地证书和公钥不匹配

Failed to send SCEP message.

发送SCEP消息失败

Number of requests has reached the maximum.

正在进行的申请的数量达到最大

Failed to update debug switch.

更新debug开关失败

Updated debug switch.

更新debug开关

Failed to start SCEP application.

启动SCEP程序失败

Failed to get reply message from SCEP application.

从SCEP程序获取应答消息失败

Failed to save the CRL to the device.

在设备上保存CRL失败

CA Certificate doesn\'t exist.

CA证书不存在

表1-2 debugging pki request命令输出信息描述表

字段

描述

Failed to get purpose of key pair.

获取密钥用途失败

The process is running. Unable to start the process.

有同样的进程正在运行，不能启动现有申请程序

The local public key and the public key in the received certificate did not match.

从本地设备上的公钥和接收到的证书中得到的公钥不匹配

The local public key and the public key in the received certificate matched.

从本地设备上的公钥和接收到的证书中得到的公钥匹配

Failed to get public key.

获取公钥失败

Failed to get the CA certificate chain.

获取CA 证书链失败

Failed to verify local certificate. Verification result: *result-string*

验证本地证书失败，验证结果为*result-string*

Enrolling the local certificate, please wait a while\...\...

正在申请本地证书，请稍候

Enrolled local certificate successfully, begin to verify local certificate.

申请本地证书成功。开始验证本地证书

Verified the local certificate successfully.

Saving the local certificate to the device\...

验证本地证书成功。存储本地证书到设备中

SCEP: Failed to get local certificate.

获取本地证书失败

Request certificate successfully.

证书申请成功

Failed to request certificate.

证书申请失败

Failed to start certificate request process.

启动申请证书程序失败

Start enroll certificate process successfully.

启动申请证书程序成功

No CA/RA certificates, try to get them from server.

没有CA/RA证书，尝试从服务器获取它们

Failed to get CA/RA certificates.

获取CA/RA证书失败

Got the CA/RA certificates successfully.

获取CA/RA证书成功

Failed to get local public key.

获取本地密钥对失败

Create the PKCS#10 request successfully.

建立 PKCS#10 申请成功

Failed to create PKCS#10 certificate request.

创建PKCS#10类型的证书申请失败

Failed to get subject name from request.

从申请中获取主题名称失败

Failed to get issuer name from request.

从申请中获取颁发者名称失败

PKCS#7 envelope: Failed to create certificate stack.

建立证书栈失败

PKCS#7 envelope: Encrypted payload successfully.

加密载荷成功

PKCS#7 develope: Failed to get ASN.1 object.

获取ASN.1格式的对象失败

PKCS#7 develope: Failed to find attribute.

查找属性失败

PKCS#7 develope: Wrong ASN.1 type.

错误的ASN.1类型

PKCS#7 develope: Failed to get ASN.1 string.

获取ASN.1字符串失败

PKCS#7 develope: Wrong failure information in reply.

回应报文中错误的失败信息

PKCS#7 develope: Failed to get PKI status in reply.

在回应报文中获取PKI状态信息失败

PKCS#7 develope: Wrong PKI status.

PKI 状态信息出错

PKCS#7 develope: Wrong PKI status in reply, Error code: *state_error*.

回应报文中的PKI状态信息错误，错误码为*state_error*

PKCS#7 develope: Failed to get recipient nonce from reply.

从回应报文中获取CA服务器回应的nonce失败

PKCS#7 develope: Received nonce is inconsistent with sender nonce.

CA服务器回应的nonce与本地的sender nonce不一致

PKCS#7 develope: Failed to get sender nonce from reply.

在回应报文中获取不到CA服务器的sender nonce

PKCS#7 develope: Wrong message type *error_type*.

错误的消息类型为*error_type*

PKCS#7 develope: Failed to get transaction ID from reply.

从回应报文中无法获取 transaction ID 信息

PKCS#7 develope: Transaction ID mismatched, received transaction ID is: *trans-id*.

Transaction ID 信息不匹配，接收到的Transaction ID为*trans-id*

PKCS#7 develope: Reply message is not signed.

PKCS#7格式的回应报文没有被签名

PKCS#7 develope: Failed to get reply signer information.

不能获取回应报文中签名者信息

PKCS#7 develope: Failed to verify signature.

验证签名失败

PKCS#7 develope: Failed to read inner PKCS#7.

不能读取内层PKCS#7格式的消息

PKCS#7 develope: Failed to decrypt inner PKCS#7.

解密内层PKCS#7格式的消息失败

PKCS#7 develope: Illegal size of payload.

非法的载荷大小

No certificate in reply message.

在回应报文中没有证书信息

*[number* certificates in reply message.]

回应报文中携带*number*个证书

PKCS#7 develope: Error reason: *string*.

解析回应报文失败的错误原因为*string*

Failed to wrap PKCS#7 message.

封装PKCS#7格式的消息失败

Failed to parse URL.

解析URL信息失败

Failed to create socket. Error code: *error-code*.

建立socket连接失败，错误码为*error-code*

Failed to get response payload.

获取响应载荷失败

Reply type: *type*.

应答消息返回类型为*type*

Failed to get response type.

获取响应类型失败

Failed to read response message. Error code: *error-code*.

读取响应信息失败，错误码为*error-code*

Failed to send SCEP message.

发送SCEP消息失败

Failed to unwrap PKCS#7 message.

解封装PKCS#7格式的消息失败

Polling counter reaches the upper limit.

轮询计数器已达到最大值

Unknown return status *status-code.*

未知的返回状态码为*status-code*

Reply message status: *state*.

返回信息状态值为*state*

Failed to initiate SCEP.

初始化SCEP失败

Failed to get options of the SCEP process.

解析命令行，获取程序运行参数失败

Unable to continue current SCEP process.

不能断续执行当前SCEP程序

Failed to initialize signal.

初始化信号失败

SCEP: Host: *string*; Port: *port*; Path: *path*.

解析URL的具体信息：主机地址为*string*；端口号为*port*；路径为*path*

PKCS#7 envelope: Failed to add signed certificate to PKCS#7 request.

添加签名证书到PKCS#7格式的请求失败

PKCS#7 envelope: Failed to sign PKCS#7 request.

签名PKCS#7格式的请求失败

PKCS#7 envelope: Failed to set signature attribute.

设置签名属性失败

PKCS#7 envelope: Failed to create PKCS#7 data.

创建PKCS#7格式的数据失败

SCEP: Failed to encode data in BASE64.

将数据编码为BASE64 类型时失败

PKCS#7 develope: Failed to get attributes.

获取属性失败

PKCS#7 develope: Failed to handle signature attributes.

处理签名属性失败

Failed to bind port. Error code: *error-code*.

通信端口绑定错误，错误码为*error-code*

Failed to connect to the CA server. Error code: *error-code*.

与CA服务器连接失败，错误码为*error-code*

SCEP: De-encapsulated PKCS#7 packet successfully.

解封装PKCS#7格式的数据包成功

SCEP: Failed to create message.

构造消息失败

Failed to create self-signed certificate.

创建自签名证书失败

SCEP request message : *string*

SCEP申请信息的内容为*string*

The signing or encryption process is running with general process at the same time. Can\'t start the current enrolling process.

签名或加密程序和通用程序在同一时间运行，不能启动申请程序

The signature or encryption is running with general at the same time, can\'t start current enroll process.

签名或加密用途证书的申请程序，不能和通用用途证书的申请程序同时启动，不能启动当前申请程序

PKCS#7 develope: Failed to get failure information from reply.

从回应中获取失败信息失败

Failed to generate the extension attributes for PKCS#10 request.

产生PKCS#10申请的扩展属性失败

Incomplete DN configuration.

DN配置不完整

Invalid PKI entity.

实体无效

The local cert is

:*local-cert*

本地证书的内容为：*local-cert*

A request already exists for the same local certificate.

对于该本地证书，已经存在一个申请

The local certificate has passed verification, and is being saved to the device\...

验证本地证书成功，保存本地证书

Send message to SCEP application.

发送消息到SCEP程序

表1-3 debugging pki retrieval命令输出信息描述表

字段

描述

The process is running. Unable to start the process.

有同样的进程正在运行，不能启动现有申请程序

Got CRLs successfully.

获取CRL成功

Failed to get CRLs.

获取CRL失败

Certificate chain doesn't have a root CA.

证书没有根CA

Failed to get subject name from request.

从申请中获取主题名称失败

Failed to get issuer name from request.

从申请中获取颁发者名称失败

Failed to get issuer name from CA certificate.

从CA证书获取证书颁发者名称失败

Failed to get serial number from CA certificate.

从CA证书获取序列号失败

PKCS#7 envelope: Failed to create certificate stack.

建立证书栈失败

PKCS#7 envelope: Encrypted payload successfully.

加密载荷成功

PKCS#7 develope: Failed to get ASN.1 object.

获取ASN.1格式的对象失败

PKCS#7 develope: Failed to find attribute.

查找属性失败

PKCS#7 develope: Wrong ASN.1 type.

错误的ASN.1类型

PKCS#7 develope: Failed to get ASN.1 string.

获取ASN.1字符串失败

PKCS#7 develope: Failed to get failure information from reply.

在回应报文中获取错误信息失败

PKCS#7 develope: Wrong failure Information in reply.

回应报文中错误的失败信息

PKCS#7 develope: Failed to get PKI status in reply.

在回应报文中获取PKI状态信息失败

PKCS#7 develope: Wrong PKI status.

PKI状态出错

PKCS#7 develope: Wrong PKI status in reply, *state_error*.

回应报文中的PKI状态信息错误，错误码为*state_error*

PKCS#7 develope: Failed to get recipient nonce from reply.

从回应报文中获取CA服务器回应的nonce失败

PKCS#7 develope: Received nonce is inconsistent with sender nonce.

CA服务器回应的nonce与本地的sender nonce不一致

PKCS#7 develope: Failed to get sender nonce from reply.

在回应报文中获取不到CA服务器的sender nonce

PKCS#7 develope: Wrong message type *error_type*.

错误的消息类型为*error_type*

PKCS#7 develope: Failed to get transaction ID from reply.

从回应报文中无法获取transaction ID信息

PKCS#7 develope: Transaction ID mismatched, received transaction ID is: *trans-id*.

transaction ID 信息不匹配，接收到的Transaction ID为*trans-id*

PKCS#7 develope: Reply message is not signed.

PKCS#7格式的回应报文没有被签名

PKCS#7 develope: Failed to get reply signer information.

不能获取回应报文中签名者信息

PKCS#7 develope: Failed to verify signature.

验证签名失败

PKCS#7 develope: Failed to read inner PKCS#7.

不能读取内层PKCS#7格式的消息

PKCS#7 develope: Failed to decrypt inner PKCS#7.

解密内层PKCS#7格式的消息失败

PKCS#7 develope: Illegal size of payload.

非法的载荷大小

No certificate in reply message.

在回应报文中没有证书信息

Failed to get CRLs from reply.

在回应报文中无法获取CRL列表信息

Failed to get CRL data in CRLs from reply.

无法获取到回应报文中的CRL列表里的表信息

PKCS#7 develope: Error reason: *string*.

解析回应报文失败的错误原因为*string*

Failed to wrap PKCS#7 message.

封装PKCS#7格式的消息失败

Failed to parse URL.

解析URL信息失败

Failed to create socket. Error code: *error-code*.

建立socket连接失败，错误码为*error-code*

Failed to get response payload.

获取响应载荷失败

Reply type: *type*.

应答消息返回类型为*type*

Failed to get response type.

获取响应类型失败

Failed to read response message.

读取响应信息失败

Failed to unwrap PKCS#7 message.

解封装PKCS#7格式的消息失败

Unknown return status *status-code.*

未知的返回状态码为*status-code*

Reply message status: *state*.

返回信息状态值为*state*

Failed to send SCEP message.

发送SCEP消息失败

SCEP: No valid payload in reply message when retrieving CA/RA certificates.

在获取CA/RA证书时没有发现有效的载荷在响应信息中

SCEP: Got CA/RA certificates successfully.

获取CA/RA证书成功

SCEP: Failed to get CA/RA certificates.

获取CA/RA证书失败

Failed to initiate SCEP.

初始化SCEP失败

Failed to get options of the SCEP process.

解析命令行，获取程序运行参数失败

Unable to continue current SCEP process.

不能断续执行当前SCEP程序

Failed to initialize signal.

初始化信号失败

SCEP: Host: *string*; Port: *port*; Path: *path*.

解析URL的具体信息：主机地址为*string*；端口号为*port*；路径为*path*

PKCS#7 envelope: Failed to add signed certificate to PKCS#7 request.

添加签名证书到PKCS#7格式的请求失败

PKCS#7 envelope: Failed to sign PKCS#7 request.

签名PKCS#7格式的请求失败

PKCS#7 envelope: Failed to set signature attribute.

设置签名属性失败

PKCS#7 envelope: Failed to create PKCS#7 data.

创建PKCS#7格式的数据失败

SCEP: Failed to encode data in BASE64.

将数据编码为BASE64 类型时失败

PKCS#7 develope: Failed to get attributes.

获取属性失败

PKCS#7 develope: Failed to handle signature's attributes.

处理签名的属性失败

Failed to bind port. Error code: *error-code*.

通信端口绑定错误，错误码为*error-code*

Failed to connect to the CA server. Error code: *error-code*.

与CA服务器连接失败，错误码为*error-code*

SCEP: De-encapsulated PKCS#7 packet successfully.

解封装PKCS#7格式的数据包成功

SCEP: Failed to create message.

构造消息失败

SCEP request message: *string*

SCEP申请信息的内容为*string*

*[number* certificates in reply message.]

回应报文中携带*number*个证书

Verified the local certificate successfully.

Saving the local certificate to the device\...

验证本地证书成功。存储本地证书到设备中

Failed to start the getCRL process.

启动获取CRL的程序失败

GetCRL process started successfully.

启动获取CRL的程序成功

Verify CRLs : *string*

验证CRL：验证结果为*string*

CRL retrieval failed: Certificate request url is not configured.

获取证书的URL没有配置

CRL retrieval failed: Certificate request from is not configured.

获取证书的注册受理机构没有配置

CRL retrieval failed: No local certificate.

没有本地证书

CRL retrieval failed: No RA certificate.

没有RA证书

CRL retrieval failed: The local public key and the public key in the local certificate are mismatching.

本地证书和公钥不匹配

CRL retrieved successfully.

获取CRL成功

Failed to retrieve CRL.

获取CRL失败

CA Certificate is not exist.

CA证书不存在

Local Certificate and key is not matched.

本地证书和公钥不匹配

Failed to get data by curl.

从curl获取数据失败

Got data by curl successfully.

通过CRUL获取数据成功

Got the CA certificate chain successfully.

获取CA证书链成功

Failed to save the local certificate to the device.

存储LOCAL证书失败

Saved the peer certificate to the device successfully.

存储PEER证书成功

Failed to save the peer certificates to the device.

保存对端证书到设备失败

Verified peer certificate successfully. Saving the peer certificates to the device\...

验证PEER证书成功，正在进行存储证书

Failed to verify the peer certificates. Verification result: *result-string*

验证PEER证书失败验证结果为*result-string*

Certificate retrieval failed: The identity of the entity *entity-name* is not configured.

获取证书失败，未配置实体的*entity-name*身份信息

Got CRL from response successfully.

从响应报文中成功获取CRL

Failed to get encryption certificate.

获取加密证书失败

Failed to save the CA/RA certificate chain.

保存CA/RA证书链失败

Saved the CA/RA certificate chain successfully.

成功保存CA/RA证书链

Verified the CA/RA certificate chain successfully. Saving the CA/RA certificate chain to the device\...

CA/RA链验证成功，开始保存CA/RA证书链

Failed to verify the CA/RA certificate chain. Verification result: *result-string*

验证CA/RA证书链失败，验证结果为*result-string*

PKCS#7 develope: Wrong PKI status.

PKI状态错误

PKCS#7 develope: Failed to get failure information from reply

从回应中获取失败信息失败

The local cert is

:*local-cert*

本地证书的内容为：*local-cert*

Saved the local certificate to the device successfully.

保存本地证书到设备成功

The peer certificate has passed verification, and is being saved to the device\...

验证对端证书成功，保存对端证书

The local certificate has passed verification, and is being saved to the device\...

验证本地证书成功，保存本地证书

表1-4 debugging pki verify命令输出信息描述表

字段

描述

Failed to get the CA certificate chain.

获取CA 证书链失败

Failed to verify local certificates. Verification result: *result-string*

验证本地证书失败。验证结果为*result-string*

The local public key and the public key in the received certificate did not match.

从本地设备上的公钥和接收到的证书中得到的公钥不匹配

The local public key and the public key in the received certificate matched.

从本地设备上的公钥和接收到的证书中得到的公钥匹配

Got the CA certificate chain successfully.

获取CA证书链成功

Verified peer certificates successfully. Saving the peer certificates to the device\...

验证PEER证书成功。正在进行存储证书...

Failed to verify the peer certificates. Verification result: *result-string*

验证PEER证书失败。验证结果为*result-string*

Failed to verify the CA/RA certificate chain, Verification result: *result-string*

验证CA/RA证书链失败。验证结果为*result-string*

Verified the CA/RA certificate chain successfully. Saving the CA/RA certificate chain to the device\...

CA/RA链验证成功。开始保存CA/RA证书链

The peer certificate has passed verification, and is being saved to the device\...

验证对端证书成功，保存对端证书

表1-5 debugging pki request verbose命令输出信息描述表

字段

描述

SCEP request messages: *string*

SCEP申请消息的内容为*string*

表1-6 debugging pki retrieve verbose命令输出信息描述表

字段

描述

SCEP request messages: *string*

SCEP申请消息的内容为*string*

表1-7 debugging pki access-control-policy命令输出信息描述表

字段

描述

PKI_Certificate_ACP : No rule exists in access control policy *policy-name*. The certificate is trusted.

访问控制策略*policy-name*中没有配置任何规则。证书可被信任

PKI_Certificate_ACP : Access control policy *policy-name* doesn't exist. The certificate is trusted.

访问控制策略*policy-name*不存在。证书可被信任

PKI_Certificate_ACP : Matched rule *number*, which has the action deny, in access control policy *policy-name*. The certificate is untrusted.

与访问控制策略*policy-name*中的一个规则匹配，该规则ID为*number*，检测动作为deny。证书不可信

PKI_Certificate_ACP : Matched rule *number*, which has the action permit, in access control policy *policy-name*. The certificate is trusted.

与访问控制策略*strpolicy-nameing*中的一个规则匹配，该规则ID为*number*，检测动作为permit。证书可被信任

PKI_Certificate_ACP : Do not match rule *number* in access control policy *policy-name*. Checking the next rule.

与访问控制策略*policy-name*中规则号为*number*的规则不匹配。检查下一个规则

PKI_Certificate_ACP : Certificate doesn\'t match any rule in access control policy *policy-name*. The certificate is untrusted.

与访问控制策略*policy-name*中所有规则都不匹配。证书不可信

PKI_Certificate_ACP : Content of the attribute group *group-name* is NULL. Rule *number* matched.

编号为*number*的规则中指定的属性组*group-name*的内容为空，所以认为此规则匹配

PKI_Certificate_ACP : Attribute group *group-name* doesn't exist. Rule *number* matched.

规则号为number所对应的属性组 group-name不存在，所以认为此规则匹配

PKI_Certificate_ACP : Doesn't match the attribute *attr-id* in attribute group *group-name*.

与证书属性组*group-name*中属性号为*attr-id*的属性不匹配

PKI_Certificate_ACP : Matches the attribute *number* in attribute group *group-name*. Checking the next attribute.

与证书属性组*group-name*中属性号为*attr-id*的属性匹配。继续检查下一个属性

【举例】

\# 打开PKI错误调试信息开关。

\<Sysname\> debugging pki error

\<Sysname\> system-view

\# 申请本地证书。

Sysname pki request-certificate domain 1 password 123

Start to request general certificate \...

Sysname

\*Sep 19 16:44:54:539 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; PKCS#7 develope: Wrong PKI

 status.

*[// PKI*]*状态错误*

\*Sep 19 16:44:54:540 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; PKCS#7 develope: Error rea

son: Transaction not permitted or supported.

*// 解析回应报文失败，原因为交互不允许或不支持*

\*Sep 19 16:44:54:540 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; SCEP: Failed to get local

certificate.

*// 获取本地证书失败*

\*Sep 19 16:44:54:541 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; Failed to request certific

ate.

*// 申请证书失败*

\# 打开PKI证书申请调试信息开关。

\<Sysname\> debugging pki request

\<Sysname\> system-view

\# 申请本地证书。

Sysname pki request-certificate domain 1 password 123

Start to request general certificate \...

Sysname

\*Sep 19 16:53:38:808 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; Got the CA/RA certificates

 successfully.

*// 获取CA/RA证书成功*

\*Sep 19 16:53:38:816 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; Create the PKCS#10 request

 successfully.

*// 建立PKCS#10申请成功*

\*Sep 19 16:53:38:827 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; Enrolling the local certif

icate,please wait a while\...\...

*// 正在申请本地证书，请稍候*

\*Sep 19 16:53:38:828 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; SCEP: Host: 192.168.149.1

Port: 446

Path: 5718d094f90fe26e27351161fd679ad8f91464fe.

*// 解析URL的具体信息：主机地址为192.168.149.1；端口号为446；路径为5718d094f90fe26e27351161fd679ad8f91464fe*

\*Sep 19 16:53:38:829 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; PKCS#7 envelope: Encrypted

 payload successfully.

*// 加密载荷成功*

\*Sep 19 16:53:38:837 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; Start enroll certificate p

rocess successfully.

*// 启动申请证书程序成功*

\*Sep 19 16:53:38:840 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; SCEP request message :GET

/5718d094f90fe26e27351161fd679ad8f91464fe/pkiclient.exe?operation=PKIOperation&m

essage=MIIGSwYJKoZIhvcNAQcCoIIGPDCCBjgCAQExDjAMBggqhkiG9w0CBQUAMIICxwYJKoZIhvcNA

QcBoIICuASCArQwggKwBgkqhkiG9w0BBwOgggKhMIICnQIBADGB6TCB5gIBADBPMDsxCzAJBgNVBAYTA

mNuMQwwCgYDVQQKEwNoM2MxDzANBgNVBAsTBmgzYy14eDENMAsGA1UEAxMEODA4OAIQQjLIoORHV7bxu

yVpDyjDlTANBgkqhkiG9w0BAQEFAASBgFt3zrqqwqduF5xfOZ9AeNQQwih43F0TZLBvFCvIHwF5zeycq

ECwFzTcjuNlIJ4P2nStP3zVlDlT2jX0Qd2kmUs6wtFgTYonPr3xhTqwy8GY0c3ZKufC65VF2piHqSd0i

jVLR3g4S8EyC163o6o%2BgJDERtr11rBg6q%2BG3917I%2Bb0MIIBqgYJKoZIhvcNAQcBMBEGBSsOAwI

HBAj6ZDq1SIbocICCAYhLNeNVM%2Bnq5dHJYXu0VbVpxsMoZS40lJRNrXP3eWOdJac%2BKRpLiWR4IDb

5dQLE39k6YrgyFP4viMFvM%2BOUZjIbEvpXSrkqsdT8ljuUPhexfwA5oDpkmkT6sSbRbp/cVf4s2rFFw

SVH9an3ZaKlQVo/CUhUPZV8eJYTRe5yD/Zzu4LvjLATap5BzDAL%2BtYByabTm1MyjwNt5syPfqFsZR0

q586MFMty1eMpE4E8Inu/MKi78W5cAbntUcperA8yhphC8iRzQosBWnYszzjer42HO/8rkuZjVATR2Z5

rgjQXp6wDPuLzEEuDOvSMsy9bjEsPQcXCkKH5qNoeq9QTRiP4Qaa/3uC8qGb2Nb

*[// SCEP*]*申请信息的内容*

\*Sep 19 16:53:38:968 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; Reply type: 5.

*// 应答消息返回类型为5*

\*Sep 19 16:53:38:979 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; SCEP: De-encapsulated PKCS

#7 packet successfully.

*// 解封装PKCS#7格式的数据包成功*

\*Sep 19 16:53:38:979 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; Reply message status 0.

*// 返回信息状态值为0*

\*Sep 19 16:53:38:980 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; 2 certificates in reply me

ssage.

*// 回应报文中携带两个证书*

\*Sep 19 16:53:38:980 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; The local cert is

:Certificate:

    Data:

        Version: 3 (0x2)

        Serial Number:

            59:96:1e:b6:ad:b5:19:59:97:47:51:ff:ad:b8:3b:70

        Signature Algorithm: sha1WithRSAEncryption

        Issuer: C=cn, O=h3c, OU=h3c-xx, CN=8088

        Validity

            Not Before: Sep 19 02:26:22 2011 GMT

            Not After : Sep 18 02:26:22 2012 GMT

        Subject: CN=cc1

        Subject Public Key Info:

            Public Key Algorithm: rsaEncryption

                Public-Key: (1024 bit)

                Modulus:

                    00:c0:6f:d3:3a:af:1c:7a:7f:a4:8b:41:73:f4:46:

                    e9:b9:c7:b8:5d:f7:36:14:3c:0a:5b:9e:1d:31:7f:

                    fc:44:7f:6b:82:b1:f5:09:1c:8e:39:52:08:51:43:

                    e6:e4:05:a3:39:35:a0:3f:3a:73:5f:e7:a9:fc:9b:

                    a3:40:7d:8a:d7:9f:0d:b0:ba:09:de:4e:52:9f:dd:

                    93:df:8e:77:3e:8a:37:25:b8:82:ec:34:04:53:76:

                    2f:b7:07:a9:88:43:a

*// 本地证书的内容*

\*Sep 19 16:53:38:980 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; Enrolled local certificate

 successfully, begin to verify local certificate.

*// 申请本地证书成功，开始验证本地证书*

\*Sep 19 16:53:38:981 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; The local public key and t

he public key in the received certificate matched.

*// 本地设备上的公钥和从接收到的证书中得到的公钥不匹配*

\*Sep 19 16:53:38:982 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; Verified the local certifi

cate successfully. Saving the local certificate to the device\...

*// 验证本地证书成功，存储本地证书到设备中*

\*Sep 19 16:53:38:982 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; Request certificate succes

sfully.

*// 证书申请成功*

\# 打开PKI获取证书和获取CRL调试信息开关。

\<Sysname\> debugging pki retrieve

\<Sysname\> system-view

System View: return to User View with Ctrl+Z.

\# 获取本地证书。

Sysname  pki retrieve-certificate domain 1 local

Sysname

\*Sep 19 17:28:39:056 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; Verified the local certifi

cate successfully. Saving the local certificate to the device\...

*// 验证本地证书成功。存储本地证书到设备中*

\*Sep 19 17:28:39:057 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; Saved the local certificat

e to the device successfully.

*// 保存本地证书到设备成功*

\# 打开PKI验证证书调试开关。

\<Sysname\> debugging pki verify

\<Sysname\> system-view

System View: return to User View with Ctrl+Z.

Sysname pki request-certificate domain 1 password 123

Start to request general certificate \...

Sysname

\*Sep 19 17:32:00:800 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; The local public key and t

he public key in the received certificate matched.

*// 从本地设备上的公钥和接收到的证书中得到的公钥匹配*

\# 打开PKI申请证书的详细调试信息开关。

\<Sysname\> debugging pki request verbose

\<Sysname\> system-view

System View: return to User View with Ctrl+Z.

Sysname pki request-certificate domain 1 password 123

Start to request general certificate \...

Sysname

\*Sep 19 17:37:11:011 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; SCEP request message :GET

/5718d094f90fe26e27351161fd679ad8f91464fe/pkiclient.exe?operation=PKIOperation&m

essage=MIIGSwYJKoZIhvcNAQcCoIIGPDCCBjgCAQExDjAMBggqhkiG9w0CBQUAMIICxwYJKoZIhvcNA

QcBoIICuASCArQwggKwBgkqhkiG9w0BBwOgggKhMIICnQIBADGB6TCB5gIBADBPMDsxCzAJBgNVBAYTA

mNuMQwwCgYDVQQKEwNoM2MxDzANBgNVBAsTBmgzYy14eDENMAsGA1UEAxMEODA4OAIQQjLIoORHV7bxu

yVpDyjDlTANBgkqhkiG9w0BAQEFAASBgKpNtHOhfgKsndpXacK4EDU4PShRdEaeB5g%2Bw8PoGAKuQtd

M/YPSmJHn9W108BJGZRG8f2Ud3iljbEbSja4wPW6pyNmrEROVCovQJjeX1bJC6hYZiMImK3q35DFqbBb

HvJC9qvLMhvRISyAGw5MdbVF4vJLQAKILsisQC39NbTh9MIIBqgYJKoZIhvcNAQcBMBEGBSsOAwIHBAi

eWep9foXYjYCCAYjPKpA9TWA7c6gTV/0FdKkWAd3vuk7I5OXOPLMaePcOdoEXMdAURwb3RgYiq2OTUaC

ajj/JYG6H4ikHL%2B9txs97A7I3LybCvNOW9%2BKZ1AIg9O/XCCBWQYxaSn0bI1%2BlelBWwv1CxFUbU

m/MVHipJF4ygeHpqVjGjNNQVHxoR5Q9b%2BVXw/9Jvvg4dG6ywngWxpQvj1pHlspIx38haQ4Rw8esksh

5VBrzMDCVlYcpHsvNryeI8aS0jx13CF7VsnwPDBBSNun62mWSk6dCdDiN3XUXFNTLnYWVm3EnKJzwf0Ll

3xqeLP%2BjQEWENenrhaIQyJUcmTgyoLfmQ6BmEhI1KGRSwZcccW3wAQf0XXT1p

*[// SCEP*]*申请信息的内容*

\# 打开PKI获取证书的详细调试信息开关。

\<Sysname\> debugging pki retrieve verbose

\<Sysname\> system-view

System View: return to User View with Ctrl+Z.

\# 申请本地证书。

Sysname pki request-certificate domain 1 password 123

Start to request general certificate \...

Sysname

\*Sep 19 17:37:11:011 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; SCEP request message :GET

/5718d094f90fe26e27351161fd679ad8f91464fe/pkiclient.exe?operation=PKIOperation&m

essage=MIIGSwYJKoZIhvcNAQcCoIIGPDCCBjgCAQExDjAMBggqhkiG9w0CBQUAMIICxwYJKoZIhvcNA

QcBoIICuASCArQwggKwBgkqhkiG9w0BBwOgggKhMIICnQIBADGB6TCB5gIBADBPMDsxCzAJBgNVBAYTA

mNuMQwwCgYDVQQKEwNoM2MxDzANBgNVBAsTBmgzYy14eDENMAsGA1UEAxMEODA4OAIQQjLIoORHV7bxu

yVpDyjDlTANBgkqhkiG9w0BAQEFAASBgKpNtHOhfgKsndpXacK4EDU4PShRdEaeB5g%2Bw8PoGAKuQtd

M/YPSmJHn9W108BJGZRG8f2Ud3iljbEbSja4wPW6pyNmrEROVCovQJjeX1bJC6hYZiMImK3q35DFqbBb

HvJC9qvLMhvRISyAGw5MdbVF4vJLQAKILsisQC39NbTh9MIIBqgYJKoZIhvcNAQcBMBEGBSsOAwIHBAi

eWep9foXYjYCCAYjPKpA9TWA7c6gTV/0FdKkWAd3vuk7I5OXOPLMaePcOdoEXMdAURwb3RgYiq2OTUaC

ajj/JYG6H4ikHL%2B9txs97A7I3LybCvNOW9%2BKZ1AIg9O/XCCBWQYxaSn0bI1%2BlelBWwv1CxFUbU

m/MVHipJF4ygeHpqVjGjNNQVHxoR5Q9b%2BVXw/9Jvvg4dG6ywngWxpQvj1pHlspIx38haQ4Rw8esksh

5VBrzMDCVlYcpHsvNryeI8aS0jx13CF7VsnwPDBBSNun62mWSk6dCdDiN3XUXFNTLnYWVm3EnKJzwf0Ll

3xqeLP%2BjQEWENenrhaIQyJUcmTgyoLfmQ6BmEhI1KGRSwZcccW3wAQf0XXT1p

*[// SCEP*]*申请信息的内容*

\# 打开PKI证书访问控制策略的调试信息开关。

\<Sysname\> debugging pki access-control-policy

\<Sysname\> system-view

System View: return to User View with Ctrl+Z.

Sysname

\# 在一台支持HTTPS的设备上配置证书属性的访问控制策略，IE浏览器采用HTTPS的方式登录设备。

Sysname

\*Sep 20 13:11:36:358 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; PKI_Certificate_ACP: Doesn

\'t match the attribute 1 in attribute group \'1\'.

*// 与证书属性组1中属性号为1的属性不匹配*

\*Sep 20 13:11:36:358 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; PKI_Certificate_ACP: Do no

t match rule 1 in access control policy \'abc\'. Checking the next rule.

*// 与访问控制策略abc中规则号为1的规则不匹配。检查下一个规则*

\*Sep 20 13:11:36:358 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; PKI_Certificate_ACP: Certi

ficate doesn\'t match any rule in access control policy \'abc\'. The certificate is

 untrusted.

*// 与访问控制策略abc中所有规则都不匹配，证书不可信*

