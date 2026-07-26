::: {#2002597514 .myid}
[]{#_Toc404792942}[]{#struct_0_x1261_x1417_1609379996}[]{#_Toc130718952}[]{#_Toc87257691}

**PKI \-- PKI调试命令 \-- debugging pki**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1261_x1417_x796574346}

[**[debugging pki ]{lang="EN-US"}**[{ **access-control-policy** \| **all** \| **error** \| **event** \| **request** \[ **verbose** \] \| **verify** \| **retrieve** \[ **verbose** \] }]{lang="EN-US"}]{#struct_0_x1261_x1417_x82642827}

[**[undo debugging pki]{lang="EN-US"}**[ { **access-control-policy** \| **all** \| **error** \| **event** \| **request** \[ **verbose** \] \| **verify** \| **retrieve** \[ **verbose** \] }]{lang="EN-US"}]{#struct_0_x1261_x1417_1208395317}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1261_x1417_x885036267}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1261_x1417_2128972210}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1261_x1417_1133645643}

[[network-admin]{lang="EN-US"}]{#struct_0_x1261_x1417_932302286}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1261_x1417_x502515036}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1261_x1417_x19908534}

[**[access-control-p]{lang="EN-US"}[olicy]{lang="EN-US"}**]{#struct_0_x1261_x1417_x1386642674}[：表示]{style="font-family:宋体"}[访问控制策略调试信息开关。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x1261_x1417_773506000}[：表示所有]{style="font-family:宋体"}[PKI]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1261_x1417_1141635988}[：表示错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1261_x1417_291825099}[：表示事件调试信息开关。]{style="font-family:宋体"}

[**[request]{lang="EN-US"}**]{#struct_0_x1261_x1417_2128513459}[：表示证书申请调试信息开关。]{style="font-family:宋体"}

[**[verify]{lang="EN-US"}**]{#struct_0_x1261_x1417_x811039402}[：表示证书验证调试信息开关。]{style="font-family:宋体"}

[**[retrieve]{lang="EN-US"}**]{#struct_0_x1261_x1417_x1097465354}[：表示获取证书和获取]{style="font-family:宋体"}[CRL]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1261_x1417_1071373379}[：表示详细调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1261_x1417_1453697476}

[**[debugging pki ]{lang="EN-US"}**]{#struct_0_x1261_x1417_x216402805}[命令用来打开]{style="font-family:宋体"}[PKI]{lang="EN-US"}[调试开关。]{style="font-family:宋体"}**[undo debugging pki]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[PKI]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_x1261_x1417_x1272845977}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[]{#struct_0_x1261_x1417_952077490}[[表1-1 ]{lang="EN-US"}[debugging pki error]{lang="EN-US"}]{#_Toc130718926}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1419301577}[[字段]{style="font-family:黑体;
   color:black"}]{#struct_0_x1261_x1417_1463320378}
:::

[[描述]{style="font-family:黑体;color:black"}]{#struct_0_x1261_x1417_2128447923}

[[Failed to get purpose of key pair.]{lang="EN-US"}]{#struct_0_x1261_x1417_1494266698}

[[获取密钥用途失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_816792092}

[[The process is running. Unable to start the process.]{lang="EN-US"}]{#struct_0_x1261_x1417_x822972802}

[[有同样的进程正在运行，不能启动现有申请程序]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x435754253}

[[The local public key and the public key in the received certificate did not match.]{lang="EN-US"}]{#struct_0_x1261_x1417_x426176441}

[[本地设备上的公钥和从接收到的证书中得到的公钥不匹配]{style="font-family:宋体"}]{#struct_0_x1261_x1417_2128382387}

[[Failed to get the CA certificate chain.]{lang="EN-US"}]{#struct_0_x1261_x1417_x829091846}

[[获取]{style="font-family:宋体"}[CA ]{lang="EN-US"}]{#struct_0_x1261_x1417_1839887627}[证书链失败]{style="font-family:宋体"}

[[Failed to verify local certificates. Verification result: *result-string*]{lang="EN-US"}]{#struct_0_x1261_x1417_x1099581884}

[[验证本地证书失败。验证结果为]{style="font-family:宋体"}*[result-string]{lang="EN-US"}*]{#struct_0_x1261_x1417_x316797844}

[[SCEP: Failed to get local certificate.]{lang="EN-US"}]{#struct_0_x1261_x1417_2128316851}

[[获取本地证书失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_723991937}

[[Failed to request certificate.]{lang="EN-US"}]{#struct_0_x1261_x1417_x1811075910}

[[证书申请失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x1642562942}

[[Failed to start certificate request process.]{lang="EN-US"}]{#struct_0_x1261_x1417_x1519608510}

[[启动申请证书程序失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x584203012}

[[Failed to get CRLs.]{lang="EN-US"}]{#struct_0_x1261_x1417_2128775603}

[[获取]{style="font-family:宋体"}[CRL]{lang="EN-US"}]{#struct_0_x1261_x1417_x390739601}[失败]{style="font-family:宋体"}

[[Failed to get CA/RA certificates.]{lang="EN-US"}]{#struct_0_x1261_x1417_x1282667307}

[[获取]{style="font-family:宋体"}[CA/RA]{lang="EN-US"}]{#struct_0_x1261_x1417_x754762019}[证书失败]{style="font-family:宋体"}

[[Failed to get local public key.]{lang="EN-US"}]{#struct_0_x1261_x1417_x1091106444}

[[获取本地密钥对失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_2128710067}

[[Failed to create PKCS#10 certificate request.]{lang="EN-US"}]{#struct_0_x1261_x1417_357836614}

[[创建]{style="font-family:宋体"}[PKCS#10]{lang="EN-US"}]{#struct_0_x1261_x1417_x1935349823}[类型的证书申请失败]{style="font-family:宋体"}

[[Failed to get subject name from request.]{lang="EN-US"}]{#struct_0_x1261_x1417_x801555024}

[[从申请中获取主题名称失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_2128644531}

[[Failed to get issuer name from request.]{lang="EN-US"}]{#struct_0_x1261_x1417_x396339916}

[[从申请中获取颁发者名称失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_1476922450}

[[Failed to get issuer name from CA certificate.]{lang="EN-US"}]{#struct_0_x1261_x1417_x1942414053}

[[从]{style="font-family:宋体"}[CA]{lang="EN-US"}]{#struct_0_x1261_x1417_x1960744172}[证书获取证书颁发者名称失败]{style="font-family:宋体"}

[[Failed to get serial number from CA certificate.]{lang="EN-US"}]{#struct_0_x1261_x1417_2128578995}

[[从]{style="font-family:宋体"}[CA]{lang="EN-US"}]{#struct_0_x1261_x1417_282119249}[证书获取序列号失败]{style="font-family:宋体"}

[[PKCS#7 envelope: Failed to create certificate stack.]{lang="EN-US"}]{#struct_0_x1261_x1417_872419387}

[[建立证书栈失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_1444129631}

[[PKCS#7 develope: Failed to get ASN.1 object.]{lang="EN-US"}]{#struct_0_x1261_x1417_2129037747}

[[获取]{style="font-family:宋体"}[ASN.1]{lang="EN-US"}]{#struct_0_x1261_x1417_x8998200}[格式的对象失败]{style="font-family:宋体"}

[[PKCS#7 develope: Failed to find attribute.]{lang="EN-US"}]{#struct_0_x1261_x1417_815810412}

[[查找属性失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_1395420239}

[[PKCS#7 develope: Failed to get ASN.1 string.]{lang="EN-US"}]{#struct_0_x1261_x1417_2128972211}

[[获取]{style="font-family:宋体"}[ASN.1]{lang="EN-US"}]{#struct_0_x1261_x1417_1133580107}[字符串失败]{style="font-family:宋体"}

[[PKCS#7 develope: Failed to get PKI status in reply.]{lang="EN-US"}]{#struct_0_x1261_x1417_x1037560712}

[[在回应报文中获取]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_x1261_x1417_2128513456}[状态信息失败]{style="font-family:宋体"}

[[.PKCS#7 develope: Wrong failure information in reply.]{lang="EN-US"}]{#struct_0_x1261_x1417_x810056362}

[[回应报文中错误的失败信息]{style="font-family:宋体"}]{#struct_0_x1261_x1417_75938541}

[[PKCS#7 develope: Failed to get recipient nonce from reply.]{lang="EN-US"}]{#struct_0_x1261_x1417_x360768866}

[[从回应报文中获取服务器回应的]{style="font-family:宋体"}[nonce]{lang="EN-US"}]{#struct_0_x1261_x1417_2128447920}[失败]{style="font-family:宋体"}

[[PKCS#7 develope: Received nonce is inconsistent with sender nonce.]{lang="EN-US"}]{#struct_0_x1261_x1417_1494332234}

[[服务器回应的]{style="font-family:宋体"}[nonce]{lang="EN-US"}]{#struct_0_x1261_x1417_2011066269}[与本地的]{style="font-family:宋体"}[sender nonce]{lang="EN-US"}[不一致]{style="font-family:宋体"}

[[PKCS#7 develope: Failed to get sender nonce from reply.]{lang="EN-US"}]{#struct_0_x1261_x1417_2128382384}

[[在回应报文中获取不到服务器的]{style="font-family:宋体"}[sender nonce]{lang="EN-US"}]{#struct_0_x1261_x1417_x829026310}

[[PKCS#7 develope: Wrong message type *error_type*.]{lang="EN-US"}]{#struct_0_x1261_x1417_x1270343875}

[[错误的消息类型，具体类型为]{style="font-family:宋体"}*[error_type]{lang="EN-US"}*]{#struct_0_x1261_x1417_x463363269}

[[PKCS#7 develope: Failed to get transaction ID from reply.]{lang="EN-US"}]{#struct_0_x1261_x1417_2128316848}

[[从回应报文中无法获取]{style="font-family:宋体"}[transaction ID]{lang="EN-US"}]{#struct_0_x1261_x1417_723533186}[信息]{style="font-family:宋体"}

[[PKCS#7 develope: Transaction ID mismatched, received transaction ID is: *trans-id*.]{lang="EN-US"}]{#struct_0_x1261_x1417_1693091483}

[[transaction ID ]{lang="EN-US"}]{#struct_0_x1261_x1417_2128775600}[信息不匹配，接收到的]{style="font-family:宋体"}[Transaction ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[trans-id]{lang="EN-US"}*

[[PKCS#7 develope: Reply message is not signed.]{lang="EN-US"}]{#struct_0_x1261_x1417_x390542993}

[[PKCS#7]{lang="EN-US"}]{#struct_0_x1261_x1417_x1679409959}[格式的回应报文没有被签名]{style="font-family:宋体"}

[[PKCS#7 develope: Failed to get reply signer information.]{lang="EN-US"}]{#struct_0_x1261_x1417_2128710064}

[[不能获取回应报文中签名者信息]{style="font-family:宋体"}]{#struct_0_x1261_x1417_357771078}

[[PKCS#7 develope: Failed to verify signature.]{lang="EN-US"}]{#struct_0_x1261_x1417_1807625375}

[[验证签名失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_2128644528}

[[PKCS#7 develope: Failed to read inner PKCS#7.]{lang="EN-US"}]{#struct_0_x1261_x1417_x395881165}

[[不能读取内层]{style="font-family:宋体"}[PKCS#7]{lang="EN-US"}]{#struct_0_x1261_x1417_x804736500}[格式的消息]{style="font-family:宋体"}

[[PKCS#7 develope: Failed to decrypt inner PKCS#7.]{lang="EN-US"}]{#struct_0_x1261_x1417_2128578992}

[[解密内层]{style="font-family:宋体"}[PKCS#7]{lang="EN-US"}]{#struct_0_x1261_x1417_282315857}[格式的消息失败]{style="font-family:宋体"}

[[PKCS#7 develope: Illegal size of payload.]{lang="EN-US"}]{#struct_0_x1261_x1417_x501625905}

[[非法的载荷大小]{style="font-family:宋体"}]{#struct_0_x1261_x1417_2129037744}

[[No certificate in reply message.]{lang="EN-US"}]{#struct_0_x1261_x1417_x8801592}

[[在回应报文中没有证书信息]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x683330067}

[[Failed to get CRLs from reply.]{lang="EN-US"}]{#struct_0_x1261_x1417_2128972208}

[[在回应报文中无法获取]{style="font-family:宋体"}[CRL]{lang="EN-US"}]{#struct_0_x1261_x1417_1134169932}[列表信息]{style="font-family:宋体"}

[[Failed to get CRL data in CRLs from reply.]{lang="EN-US"}]{#struct_0_x1261_x1417_2128513457}

[[无法获取到回应报文中的]{style="font-family:宋体"}[CRL]{lang="EN-US"}]{#struct_0_x1261_x1417_x810121898}[列表里的表信息]{style="font-family:宋体"}

[[PKCS#7 develope: Error reason: *string*.]{lang="EN-US"}]{#struct_0_x1261_x1417_1286888824}

[[解析回应报文失败的错误原因为]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_x1261_x1417_2128447921}

[[Failed to wrap PKCS#7 message.]{lang="EN-US"}]{#struct_0_x1261_x1417_1494397770}

[[封装]{style="font-family:宋体"}[PKCS#7]{lang="EN-US"}]{#struct_0_x1261_x1417_403426666}[格式的消息失败]{style="font-family:宋体"}

[[Failed to parse URL.]{lang="EN-US"}]{#struct_0_x1261_x1417_2128382385}

[[解析]{style="font-family:宋体"}[URL]{lang="EN-US"}]{#struct_0_x1261_x1417_x828960774}[信息失败]{style="font-family:宋体"}

[[Failed to create socket. Error code: *error-code.*]{lang="EN-US"}]{#struct_0_x1261_x1417_2128316849}

[[建立]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x1261_x1417_723467650}[连接失败，错误码为]{style="font-family:宋体"}*[error-code]{lang="EN-US"}*

[[Failed to get response payload.]{lang="EN-US"}]{#struct_0_x1261_x1417_x1490742983}

[[获取响应载荷失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_2128775601}

[[Failed to get response type.]{lang="EN-US"}]{#struct_0_x1261_x1417_x390608529}

[[获取响应类型失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_2128710065}

[[Failed to read response message. Error code: *error-code*.]{lang="EN-US"}]{#struct_0_x1261_x1417_357705542}

[[读取响应信息失败，错误码为]{style="font-family:宋体"}*[error-code]{lang="EN-US"}*]{#struct_0_x1261_x1417_x160986541}

[[Failed to unwrap PKCS#7 message.]{lang="EN-US"}]{#struct_0_x1261_x1417_2128644529}

[[解封装]{style="font-family:宋体"}[PKCS#7]{lang="EN-US"}]{#struct_0_x1261_x1417_x395815629}[格式的消息失败]{style="font-family:宋体"}

[[Polling counter reaches the upper limit.]{lang="EN-US"}]{#struct_0_x1261_x1417_2128578993}

[[轮询计数器已达到最大值]{style="font-family:宋体"}]{#struct_0_x1261_x1417_282250321}

[[Unknown return status *status-code.*]{lang="EN-US"}]{#struct_0_x1261_x1417_2129037745}

[[未知的返回状态码为]{style="font-family:宋体"}*[status-code]{lang="EN-US"}*]{#struct_0_x1261_x1417_x8867128}

[[Failed to send SCEP message.]{lang="EN-US"}]{#struct_0_x1261_x1417_x267223814}

[[发送]{style="font-family:宋体"}[SCEP]{lang="EN-US"}]{#struct_0_x1261_x1417_2128972209}[消息失败]{style="font-family:宋体"}

[[SCEP: Failed to get CA/RA certificates.]{lang="EN-US"}]{#struct_0_x1261_x1417_1134104396}

[[获取]{style="font-family:宋体"}[CA/RA]{lang="EN-US"}]{#struct_0_x1261_x1417_2128513454}[证书失败]{style="font-family:宋体"}

[[Failed to initiate SCEP.]{lang="EN-US"}]{#struct_0_x1261_x1417_x810187434}

[[初始化]{style="font-family:宋体"}[SCEP]{lang="EN-US"}]{#struct_0_x1261_x1417_2128447918}[失败]{style="font-family:宋体"}

[[Failed to get options of the SCEP process.]{lang="EN-US"}]{#struct_0_x1261_x1417_1494856521}

[[解析命令行，获取程序运行参数失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x754302755}

[[Unable to continue current SCEP process.]{lang="EN-US"}]{#struct_0_x1261_x1417_2128382382}

[[不能继续执行当前]{style="font-family:宋体"}[SCEP]{lang="EN-US"}]{#struct_0_x1261_x1417_x829419526}[程序]{style="font-family:宋体"}

[[Failed to initialize signal.]{lang="EN-US"}]{#struct_0_x1261_x1417_2128316846}

[[初始化信号失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_724450690}

[[PKCS#7 envelope: Failed to add signed certificate to PKCS#7 request.]{lang="EN-US"}]{#struct_0_x1261_x1417_2128775598}

[[添加签名证书到]{style="font-family:宋体"}[PKCS#7]{lang="EN-US"}]{#struct_0_x1261_x1417_x1963996826}[格式的请求失败]{style="font-family:宋体"}

[[PKCS#7 envelope: Failed to sign PKCS#7 request.]{lang="EN-US"}]{#struct_0_x1261_x1417_2128710062}

[[签名]{style="font-family:宋体"}[PKCS#7]{lang="EN-US"}]{#struct_0_x1261_x1417_357640006}[格式的请求失败]{style="font-family:宋体"}

[[PKCS#7 envelope: Failed to set signature attribute.]{lang="EN-US"}]{#struct_0_x1261_x1417_2128644526}

[[设置签名属性失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x396798669}

[[PKCS#7 envelope: Failed to create PKCS#7 data.]{lang="EN-US"}]{#struct_0_x1261_x1417_2128578990}

[[创建]{style="font-family:宋体"}[PKCS#7]{lang="EN-US"}]{#struct_0_x1261_x1417_282446929}[格式的数据失败]{style="font-family:宋体"}

[[SCEP: Failed to encode data in BASE64.]{lang="EN-US"}]{#struct_0_x1261_x1417_2129037742}

[[将数据编码为]{style="font-family:宋体"}[BASE64 ]{lang="EN-US"}]{#struct_0_x1261_x1417_x9194808}[类型时失败]{style="font-family:宋体"}

[[PKCS#7 develope: Failed to get attributes. ]{lang="EN-US"}]{#struct_0_x1261_x1417_2128972206}

[[获取属性失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_1133252428}

[[PKCS#7 develope: Failed to handle signature's attributes.]{lang="EN-US"}]{#struct_0_x1261_x1417_2128513455}

[[处理签的名属性失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x810252970}

[[Failed to bind port. Error code: *error-code*.]{lang="EN-US"}]{#struct_0_x1261_x1417_2128447919}

[[通信端口绑定错误，错误码为]{style="font-family:宋体"}*[error-code]{lang="EN-US"}*]{#struct_0_x1261_x1417_1494922057}

[[Failed to connect to the CA server. Error code: *error-code*.]{lang="EN-US"}]{#struct_0_x1261_x1417_2128382383}

[[与]{style="font-family:宋体"}[CA]{lang="EN-US"}]{#struct_0_x1261_x1417_x829353990}[服务器连接失败，错误码为]{style="font-family:宋体"}*[error-code]{lang="EN-US"}*

[[SCEP: Failed to create message.]{lang="EN-US"}]{#struct_0_x1261_x1417_2128316847}

[[构造消息失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_724385154}

[[Failed to create self-signed certificate.]{lang="EN-US"}]{#struct_0_x1261_x1417_2128775599}

[[创建自签名证书失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x1964062362}

[[PKCS#7 develope: Wrong PKI status.]{lang="EN-US"}]{#struct_0_x1261_x1417_2128710063}

[[PKI]{lang="EN-US"}]{#struct_0_x1261_x1417_2128644527}[状态错误]{style="font-family:宋体"}

[[PKCS#7 develope: Failed to get failure information from reply.]{lang="EN-US"}]{#struct_0_x1261_x1417_x396733133}

[[从回应中获取失败信息失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_2128578991}

[[PKCS#7 develope: Wrong PKI status in reply. Status code: *status-code*.]{lang="EN-US"}]{#struct_0_x1261_x1417_282381393}

[[回应报文中错误的]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_x1261_x1417_2129037743}[状态，状态码为]{style="font-family:宋体"}*[status-code]{lang="EN-US"}*

[[The signing or encryption is running with general at the same time, can\'t start current enroll process.]{lang="EN-US"}]{#struct_0_x1261_x1417_x9260344}

[[签名或加密程序和通用程序在同一时间运行，不能启动证书申请程序]{style="font-family:宋体"}]{#struct_0_x1261_x1417_2128972207}

[[Failed to start the getCRL process.]{lang="EN-US"}]{#struct_0_x1261_x1417_x600369897}

[[启动获取]{style="font-family:宋体"}[CRL]{lang="EN-US"}]{#struct_0_x1261_x1417_595135114}[的程序失败]{style="font-family:宋体"}

[[CRL verification result: *string*]{lang="EN-US"}]{#struct_0_x1261_x1417_x600435433}

[[验证]{style="font-family:宋体"}[CRL]{lang="EN-US"}]{#struct_0_x1261_x1417_x976340885}[的结果为]{style="font-family:宋体"}*[string]{lang="EN-US"}*[，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[内容可包括：]{style="font-family:宋体"}

[[(1)[    ]{style="font:7.0pt "}]{lang="EN-US"}[ok]{lang="EN-US"}]{#struct_0_x1261_x1417_x600500969}[：成功]{style="font-family:宋体"}

[[(1)[    ]{style="font:7.0pt "}]{lang="EN-US"}[unable to get issuer certificate]{lang="EN-US"}]{#struct_0_x1261_x1417_x600566505}[：不能获取签发者的证书]{style="font-family:
  宋体"}

[[(2)[    ]{style="font:7.0pt "}]{lang="EN-US"}[unable to get certificate CRL]{lang="EN-US"}]{#struct_0_x1261_x1417_1776278136}[：不能获取证书的]{style="font-family:
  宋体"}[CRL]{lang="EN-US"}

[[(3)[    ]{style="font:7.0pt "}]{lang="EN-US"}[unable to decrypt certificate\'s signature]{lang="EN-US"}]{#struct_0_x1261_x1417_x600107753}[：不能解密证书的签名]{style="font-family:宋体"}

[[(4)[    ]{style="font:7.0pt "}]{lang="EN-US"}[unable to decrypt CRL\'s signature]{lang="EN-US"}]{#struct_0_x1261_x1417_x185250134}[：不能解密]{style="font-family:宋体"}[CRL]{lang="EN-US"}[的签名]{style="font-family:宋体"}

[[(5)[    ]{style="font:7.0pt "}]{lang="EN-US"}[unable to decode issuer public key]{lang="EN-US"}]{#struct_0_x1261_x1417_x600173289}[：不能解码签发都的公钥]{style="font-family:宋体"}

[[(6)[    ]{style="font:7.0pt "}]{lang="EN-US"}[ certificate signature failure]{lang="EN-US"}]{#struct_0_x1261_x1417_x600238825}[：证书签名失败]{style="font-family:
  宋体"}

[[(7)[    ]{style="font:7.0pt "}]{lang="EN-US"}[CRL signature failure ]{lang="EN-US"}]{#struct_0_x1261_x1417_x2144168555}[：]{style="font-family:宋体"}[CRL]{lang="EN-US"}[签名失败]{style="font-family:宋体"}

[[(8)[    ]{style="font:7.0pt "}]{lang="EN-US"}[certificate is not yet valid]{lang="EN-US"}]{#struct_0_x1261_x1417_x600304361}[：证书不是有效的]{style="font-family:
  宋体"}

[[(9)[    ]{style="font:7.0pt "}]{lang="EN-US"}[CRL is not yet valid CRL]{lang="EN-US"}]{#struct_0_x1261_x1417_x986791034}[：不是有效的]{style="font-family:宋体"}

[[(10)[  ]{style="font:7.0pt "}]{lang="EN-US"}[certificate has expired]{lang="EN-US"}]{#struct_0_x1261_x1417_x599845609}[：证书已经到期]{style="font-family:宋体"}

[[(11)[  ]{style="font:7.0pt "}]{lang="EN-US"}[CRL has expired CRL]{lang="EN-US"}]{#struct_0_x1261_x1417_x599911145}[：已经到期]{style="font-family:宋体"}

[[(12)[  ]{style="font:7.0pt "}]{lang="EN-US"}[format error in certificate\'s notBefore field]{lang="EN-US"}]{#struct_0_x1261_x1417_x71323158}[：证书有效日期的起始时间错误]{style="font-family:宋体"}

[[(13)[  ]{style="font:7.0pt "}]{lang="EN-US"}[format error in certificate\'s notAfter field]{lang="EN-US"}]{#struct_0_x1261_x1417_x600369896}[：证书有效日期的终止时间错误]{style="font-family:宋体"}

[[(14)[  ]{style="font:7.0pt "}]{lang="EN-US"}[format error in CRL\'s lastUpdate field]{lang="EN-US"}]{#struct_0_x1261_x1417_x600435432}[：]{style="font-family:宋体"}[CRL]{lang="EN-US"}[的最后更新域错误]{style="font-family:宋体"}

[[(15)[  ]{style="font:7.0pt "}]{lang="EN-US"}[format error in CRL\'s nextUpdate field]{lang="EN-US"}]{#struct_0_x1261_x1417_x976406421}[：]{style="font-family:宋体"}[CRL]{lang="EN-US"}[的下次更新域错误]{style="font-family:宋体"}

[[(16)[  ]{style="font:7.0pt "}]{lang="EN-US"}[out of memory]{lang="EN-US"}]{#struct_0_x1261_x1417_x600500968}[：内存不足]{style="font-family:宋体"}

[[(17)[  ]{style="font:7.0pt "}]{lang="EN-US"}[self signed certificate]{lang="EN-US"}]{#struct_0_x1261_x1417_x600566504}[：自签名证书]{style="font-family:宋体"}

[[(18)[  ]{style="font:7.0pt "}]{lang="EN-US"}[self signed certificate in certificate chain]{lang="EN-US"}]{#struct_0_x1261_x1417_1776343672}[：自签名证书在证书链中]{style="font-family:宋体"}

[[(19)[  ]{style="font:7.0pt "}]{lang="EN-US"}[unable to get local issuer certificate]{lang="EN-US"}]{#struct_0_x1261_x1417_x600107752}[：不能获取本地签发者的证书]{style="font-family:宋体"}

[[(20)[  ]{style="font:7.0pt "}]{lang="EN-US"}[unable to verify the first certificate]{lang="EN-US"}]{#struct_0_x1261_x1417_x600173288}[：不能验证第一个证书]{style="font-family:宋体"}

[[(21)[  ]{style="font:7.0pt "}]{lang="EN-US"}[certificate chain too long]{lang="EN-US"}]{#struct_0_x1261_x1417_220494907}[：证书链太长]{style="font-family:
  宋体"}

[[(22)[  ]{style="font:7.0pt "}]{lang="EN-US"}[certificate revoked]{lang="EN-US"}]{#struct_0_x1261_x1417_x600238824}[：证书被调销]{style="font-family:宋体"}

[[(23)[  ]{style="font:7.0pt "}]{lang="EN-US"}[invalid CA certificate]{lang="EN-US"}]{#struct_0_x1261_x1417_x600304360}[：无效的]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书]{style="font-family:宋体"}

[[(24)[  ]{style="font:7.0pt "}]{lang="EN-US"}[invalid non-CA certificate (has CA markings) ]{lang="EN-US"}]{#struct_0_x1261_x1417_x986725498}[：无效的]{style="font-family:宋体"}[non-CA]{lang="EN-US"}[证书（包含]{style="font-family:宋体"}[CA ]{lang="EN-US"}[记号）]{style="font-family:宋体"}

[[(25)[  ]{style="font:7.0pt "}]{lang="EN-US"}[ path length constraint exceeded]{lang="EN-US"}]{#struct_0_x1261_x1417_x599845608}[：路径长度限制过度]{style="font-family:
  宋体"}

[[(26)[  ]{style="font:7.0pt "}]{lang="EN-US"}[proxy path length constraint exceeded]{lang="EN-US"}]{#struct_0_x1261_x1417_x599911144}[：代理人路径长度限制过度]{style="font-family:宋体"}

[[(27)[  ]{style="font:7.0pt "}]{lang="EN-US"}[proxy certificates not allowed, please set the appropriate flag]{lang="EN-US"}]{#struct_0_x1261_x1417_x71257622}[：代理人证书没有被允许，请设置通行标志]{style="font-family:宋体"}

[[(28)[  ]{style="font:7.0pt "}]{lang="EN-US"}[unsupported certificate purpose]{lang="EN-US"}]{#struct_0_x1261_x1417_x600369899}[：不支持证书意图]{style="font-family:
  宋体"}

[[(29)[  ]{style="font:7.0pt "}]{lang="EN-US"}[certificate not trusted]{lang="EN-US"}]{#struct_0_x1261_x1417_x600435435}[：证书不可信]{style="font-family:宋体"}

[[(30)[  ]{style="font:7.0pt "}]{lang="EN-US"}[certificate rejected]{lang="EN-US"}]{#struct_0_x1261_x1417_x976209813}[：证书被拒决]{style="font-family:宋体"}

[[(31)[  ]{style="font:7.0pt "}]{lang="EN-US"}[application verification failure]{lang="EN-US"}]{#struct_0_x1261_x1417_x600500971}[：证书验证失败]{style="font-family:
  宋体"}

[[(32)[  ]{style="font:7.0pt "}]{lang="EN-US"}[subject issuer mismatch]{lang="EN-US"}]{#struct_0_x1261_x1417_x600566507}[：]{style="font-family:宋体"}[subject ]{lang="EN-US"}[名称和]{style="font-family:宋体"}[issuer]{lang="EN-US"}[名称不匹配]{style="font-family:宋体"}

[[(33)[  ]{style="font:7.0pt "}]{lang="EN-US"}[authority and subject key identifier mismatch]{lang="EN-US"}]{#struct_0_x1261_x1417_1776147064}[：授权和]{style="font-family:宋体"}[subject key]{lang="EN-US"}[标识符不匹配]{style="font-family:宋体"}

[[(34)[  ]{style="font:7.0pt "}]{lang="EN-US"}[authority and issuer serial number mismatch]{lang="EN-US"}]{#struct_0_x1261_x1417_x600107755}[：授权和签发者序列号不匹配]{style="font-family:宋体"}

[[(35)[  ]{style="font:7.0pt "}]{lang="EN-US"}[ key usage does not include certificate signing]{lang="EN-US"}]{#struct_0_x1261_x1417_x600173291}[：密钥用途不包含给证书签名的用途]{style="font-family:宋体"}

[[(36)[  ]{style="font:7.0pt "}]{lang="EN-US"}[unable to get CRL issuer certificate]{lang="EN-US"}]{#struct_0_x1261_x1417_x600238827}[：不能获取]{style="font-family:宋体"}[CRL]{lang="EN-US"}[签发者的证书]{style="font-family:宋体"}

[[(37)[  ]{style="font:7.0pt "}]{lang="EN-US"}[unhandled critical extension]{lang="EN-US"}]{#struct_0_x1261_x1417_x2144037483}[：不能处理鉴定扩展]{style="font-family:
  宋体"}

[[(38)[  ]{style="font:7.0pt "}]{lang="EN-US"}[ key usage does not include CRL signing]{lang="EN-US"}]{#struct_0_x1261_x1417_x600304363}[密钥：用途不包含给]{style="font-family:宋体"}[CRL]{lang="EN-US"}[签名的用途]{style="font-family:宋体"}

[[(39)[  ]{style="font:7.0pt "}]{lang="EN-US"}[key usage does not include digital signature]{lang="EN-US"}]{#struct_0_x1261_x1417_x599845611}[：密钥用途不包含数字签名的用途]{style="font-family:宋体"}

[[(40)[  ]{style="font:7.0pt "}]{lang="EN-US"}[ unhandled critical CRL extension]{lang="EN-US"}]{#struct_0_x1261_x1417_x68975494}[：不能处理鉴定]{style="font-family:宋体"}[CRL]{lang="EN-US"}[扩展]{style="font-family:宋体"}

[[(41)[  ]{style="font:7.0pt "}]{lang="EN-US"}[invalid or inconsistent certificate extension]{lang="EN-US"}]{#struct_0_x1261_x1417_x599911147}[：无效的或不一致的证书扩展]{style="font-family:宋体"}

[[(42)[  ]{style="font:7.0pt "}]{lang="EN-US"}[invalid or inconsistent certificate policy extension]{lang="EN-US"}]{#struct_0_x1261_x1417_x600369898}[：无效的或不一致的证书策略扩展]{style="font-family:宋体"}

[[(43)[  ]{style="font:7.0pt "}]{lang="EN-US"}[no explicit policy]{lang="EN-US"}]{#struct_0_x1261_x1417_594545290}[：没有清楚的策略]{style="font-family:宋体"}

[[(44)[  ]{style="font:7.0pt "}]{lang="EN-US"}[Different CRL scope]{lang="EN-US"}]{#struct_0_x1261_x1417_x600435434}[：不同的]{style="font-family:宋体"}[CRL]{lang="EN-US"}[范围]{style="font-family:宋体"}

[[(45)[  ]{style="font:7.0pt "}]{lang="EN-US"}[Unsupported extension feature]{lang="EN-US"}]{#struct_0_x1261_x1417_x600500970}[：不支持扩展属性]{style="font-family:
  宋体"}

[[(46)[  ]{style="font:7.0pt "}]{lang="EN-US"}[RFC 3779 resource not subset of parent\'s resources RFC 3779]{lang="EN-US"}]{#struct_0_x1261_x1417_x600566506}[：资源没有父母资源的子集]{style="font-family:宋体"}

[[(47)[  ]{style="font:7.0pt "}]{lang="EN-US"}[permitted subtree violation]{lang="EN-US"}]{#struct_0_x1261_x1417_1776212600}[：允许违背子树集]{style="font-family:
  宋体"}

[[(48)[  ]{style="font:7.0pt "}]{lang="EN-US"}[excluded subtree violation]{lang="EN-US"}]{#struct_0_x1261_x1417_x600107754}[：排斥违背子树集]{style="font-family:
  宋体"}

[[(49)[  ]{style="font:7.0pt "}]{lang="EN-US"}[name constraints minimum and maximum not supported]{lang="EN-US"}]{#struct_0_x1261_x1417_x600173290}[：不支持最大或最小名称限限制]{style="font-family:宋体"}

[[(50)[  ]{style="font:7.0pt "}]{lang="EN-US"}[unsupported name constraint type]{lang="EN-US"}]{#struct_0_x1261_x1417_x600238826}[：不支持名称类型限制]{style="font-family:
  宋体"}

[[(51)[  ]{style="font:7.0pt "}]{lang="EN-US"}[unsupported or invalid name constraint syntax]{lang="EN-US"}]{#struct_0_x1261_x1417_x2144103019}[：不支持或无效的名称限制语法]{style="font-family:宋体"}

[[(52)[  ]{style="font:7.0pt "}]{lang="EN-US"}[unsupported or invalid name syntax]{lang="EN-US"}]{#struct_0_x1261_x1417_x600304362}[：不支持或无效的名称语法]{style="font-family:宋体"}

[[(53)[  ]{style="font:7.0pt "}]{lang="EN-US"}[CRL path validation error ]{lang="EN-US"}]{#struct_0_x1261_x1417_x599845610}[：]{style="font-family:
  宋体"}[CRL]{lang="EN-US"}[路径确认错误]{style="font-family:宋体"}

[[CRL retrieval failed: Certificate request URL is not configured.]{lang="EN-US"}]{#struct_0_x1261_x1417_x69041030}

[[获取证书的]{style="font-family:宋体"}[URL]{lang="EN-US"}]{#struct_0_x1261_x1417_x599911146}[没有配置]{style="font-family:宋体"}

[[CRL retrieval failed: Certificate request from is not configured.]{lang="EN-US"}]{#struct_0_x1261_x1417_x600369901}

[[获取证书的注册受理机构没有配置]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x600435437}

[[CRL retrieval failed: No local certificate.]{lang="EN-US"}]{#struct_0_x1261_x1417_x976078741}

[[没有本地证书]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x600500973}

[[CRL retrieval failed: No RA certificate.]{lang="EN-US"}]{#struct_0_x1261_x1417_x600566509}

[[没有]{style="font-family:宋体"}[RA]{lang="EN-US"}]{#struct_0_x1261_x1417_x600107757}[证书]{style="font-family:宋体"}

[[CRL retrieval failed: The local public key and the public key in the local certificate are mismatching.]{lang="EN-US"}]{#struct_0_x1261_x1417_x600173293}

[[本地证书里的公钥和本地公钥不匹配]{style="font-family:宋体"}]{#struct_0_x1261_x1417_221215802}

[[Failed to retrieve CRLs.]{lang="EN-US"}]{#struct_0_x1261_x1417_x600238829}

[[获取]{style="font-family:宋体"}[CRL]{lang="EN-US"}]{#struct_0_x1261_x1417_x600304365}[失败]{style="font-family:宋体"}

[[CA certificate doesn't exist.]{lang="EN-US"}]{#struct_0_x1261_x1417_x599845613}

[[CA]{lang="EN-US"}]{#struct_0_x1261_x1417_x69106566}[证书不存在]{style="font-family:宋体"}

[[Local certificate and public key don't match.]{lang="EN-US"}]{#struct_0_x1261_x1417_x599911149}

[[本地证书和公钥不匹配]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x600369900}

[[Failed to get data by curl.]{lang="EN-US"}]{#struct_0_x1261_x1417_x600435436}

[[通过]{style="font-family:宋体"}[curl]{lang="EN-US"}]{#struct_0_x1261_x1417_x600500972}[获取数据失败]{style="font-family:宋体"}

[[Failed to save the local certificate to the device.]{lang="EN-US"}]{#struct_0_x1261_x1417_x164236985}

[[存储本地证书失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x600566508}

[[Failed to verify the peer certificates.[ ]{style="color:red"}Verification result: *result-string.*]{lang="EN-US"}]{#struct_0_x1261_x1417_x600107756}

[[验证对端证书失败，验证结果为]{style="font-family:宋体"}*[result-string]{lang="EN-US"}*]{#struct_0_x1261_x1417_x600173292}

[[The signature or encryption is running with general at the same time, can\'t start current enroll process.]{lang="EN-US"}]{#struct_0_x1261_x1417_x600238828}

[[签名或加密用途证书的申请程序不能和通用用途证书的申请程序同时启动，不能启动当前申请程序]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x600304364}

[[Failed to generate the extension attributes for PKCS#10 request.]{lang="EN-US"}]{#struct_0_x1261_x1417_x986987642}

[[产生]{style="font-family:宋体"}[PKCS#10]{lang="EN-US"}]{#struct_0_x1261_x1417_x599845612}[申请的扩展属性失败]{style="font-family:宋体"}

[[Incomplete DN configuration.]{lang="EN-US"}]{#struct_0_x1261_x1417_x599911148}

[[DN]{lang="EN-US"}]{#struct_0_x1261_x1417_1778640090}[配置不完整]{style="font-family:宋体"}

[[Failed to save the peer certificates to the device.]{lang="EN-US"}]{#struct_0_x1261_x1417_1778705626}

[[保存对端证书到设备失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x875457932}

[[Invalid PKI entity.]{lang="EN-US"}]{#struct_0_x1261_x1417_1778771162}

[[实体无效]{style="font-family:宋体"}]{#struct_0_x1261_x1417_1778836698}

[[Failed to get the certificate chain.]{lang="EN-US"}]{#struct_0_x1261_x1417_1778377946}

[[获取证书链失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_1778443482}

[[Certificate retrieval failed: The identity of the entity *entity-name* is not configured.]{lang="EN-US"}]{#struct_0_x1261_x1417_1778509018}

[[获取证书失败，未配置实体的]{style="font-family:宋体"}*[entity-name]{lang="EN-US"}*]{#struct_0_x1261_x1417_1778574554}[身份信息]{style="font-family:宋体"}

[[Failed to get the source IP address of PKI traffic.]{lang="EN-US"}]{#struct_0_x1261_x1417_262080202}

[[获取]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_x1261_x1417_1779164378}[协议报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址失败]{style="font-family:宋体"}

[[Failed to verify the CA/RA certificate chain, Verification result: *result-string*]{lang="EN-US"}]{#struct_0_x1261_x1417_1779229914}

[[验证]{style="font-family:宋体"}[CA/RA]{lang="EN-US"}]{#struct_0_x1261_x1417_1778640091}[证书链失败，验证结果为]{style="font-family:宋体"}*[result-string]{lang="EN-US"}*

[[Failed to save the CA/RA certificate chain.]{lang="EN-US"}]{#struct_0_x1261_x1417_1778705627}

[[保存]{style="font-family:宋体"}[CA/RA]{lang="EN-US"}]{#struct_0_x1261_x1417_1778771163}[证书链失败]{style="font-family:宋体"}

[[Failed to get the encryption certificate.]{lang="EN-US"}]{#struct_0_x1261_x1417_1778836699}

[[获取加密用途的证书失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x1288835159}

[[The local cert is]{lang="EN-US"}]{#struct_0_x1261_x1417_1778377947}

[[:*local-cert*]{lang="EN-US"}]{#struct_0_x1261_x1417_1778443483}

[[本地证书的内容为：]{style="font-family:宋体"}*[local-cert]{lang="EN-US"}*]{#struct_0_x1261_x1417_1778509019}

[[Local Certificate and key is not matched.]{lang="EN-US"}]{#struct_0_x1261_x1417_1778574555}

[[本地证书和公钥不匹配]{style="font-family:宋体"}]{#struct_0_x1261_x1417_1779164379}

[[Failed to send SCEP message.]{lang="EN-US"}]{#struct_0_x1261_x1417_1779229915}

[[发送]{style="font-family:宋体"}[SCEP]{lang="EN-US"}]{#struct_0_x1261_x1417_1778640088}[消息失败]{style="font-family:宋体"}

[[Number of requests has reached the maximum.]{lang="EN-US"}]{#struct_0_x1261_x1417_666842316}

[[正在进行的申请的数量达到最大]{style="font-family:宋体"}]{#struct_0_x1261_x1417_1778705624}

[[Failed to update debug switch.]{lang="EN-US"}]{#struct_0_x1261_x1417_1778771160}

[[更新]{style="font-family:宋体"}[debug]{lang="EN-US"}]{#struct_0_x1261_x1417_1778836696}[开关失败]{style="font-family:宋体"}

[[Updated debug switch.]{lang="EN-US"}]{#struct_0_x1261_x1417_1778377944}

[[更新]{style="font-family:宋体"}[debug]{lang="EN-US"}]{#struct_0_x1261_x1417_1778443480}[开关]{style="font-family:宋体"}

[[Failed to start SCEP application.]{lang="EN-US"}]{#struct_0_x1261_x1417_1778509016}

[[启动]{style="font-family:宋体"}[SCEP]{lang="EN-US"}]{#struct_0_x1261_x1417_1778574552}[程序失败]{style="font-family:宋体"}

[[Failed to get reply message from SCEP application.]{lang="EN-US"}]{#struct_0_x1261_x1417_1779164376}

[[从]{style="font-family:宋体"}[SCEP]{lang="EN-US"}]{#struct_0_x1261_x1417_1779229912}[程序获取应答消息失败]{style="font-family:宋体"}

[[Failed to save the CRL to the device.]{lang="EN-US"}]{#struct_0_x1261_x1417_1778640089}

[[在设备上保存]{style="font-family:宋体"}[CRL]{lang="EN-US"}]{#struct_0_x1261_x1417_1778705625}[失败]{style="font-family:宋体"}

[[CA Certificate doesn\'t exist.]{lang="EN-US"}]{#struct_0_x1261_x1417_1778771161}

[[CA]{lang="EN-US"}]{#struct_0_x1261_x1417_267436036}[证书不存在]{style="font-family:宋体"}

[[ ]{lang="EN-US"}]{#_Toc130718927}

[[表1-2 ]{lang="EN-US"}[debugging pki request]{lang="EN-US"}]{#struct_0_x1261_x1417_1778836697}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1380368619}[[字段]{style="font-family:黑体"}]{#struct_0_x1261_x1417_x1288966231}

[[描述]{style="font-family:黑体"}]{#struct_0_x1261_x1417_522660158}

[[Failed to get purpose of key pair.]{lang="EN-US"}]{#struct_0_x1261_x1417_1366923317}

[[获取密钥用途失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_1371451511}

[[The process is running. Unable to start the process.]{lang="EN-US"}]{#struct_0_x1261_x1417_x1191985177}

[[有同样的进程正在运行，不能启动现有申请程序]{style="font-family:宋体"}]{#struct_0_x1261_x1417_1857068925}

[[The local public key and the public key in the received certificate did not match.]{lang="EN-US"}]{#struct_0_x1261_x1417_1778377945}

[[从本地设备上的公钥和接收到的证书中得到的公钥不匹配]{style="font-family:宋体"}]{#struct_0_x1261_x1417_989953076}

[[The local public key and the public key in the received certificate matched.]{lang="EN-US"}]{#struct_0_x1261_x1417_x1021348308}

[[从本地设备上的公钥和接收到的证书中得到的公钥匹配]{style="font-family:宋体"}]{#struct_0_x1261_x1417_14031139}

[[Failed to get public key.]{lang="EN-US"}]{#struct_0_x1261_x1417_2088345491}

[[获取公钥失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_1778443481}

[[Failed to get the CA certificate chain.]{lang="EN-US"}]{#struct_0_x1261_x1417_x1664374491}

[[获取]{style="font-family:宋体"}[CA ]{lang="EN-US"}]{#struct_0_x1261_x1417_x1922329098}[证书链失败]{style="font-family:宋体"}

[[Failed to verify local certificate. Verification result: *result-string*]{lang="EN-US"}]{#struct_0_x1261_x1417_x822644634}

[[验证本地证书失败，验证结果为]{style="font-family:宋体"}*[result-string]{lang="EN-US"}*]{#struct_0_x1261_x1417_1515663147}

[[Enrolling the local certificate, please wait a while\...\...]{lang="EN-US"}]{#struct_0_x1261_x1417_1778509017}

[[正在申请本地证书，请稍候]{style="font-family:宋体;
  color:black"}]{#struct_0_x1261_x1417_1884756719}

[[Enrolled local certificate successfully, begin to verify local certificate.]{lang="EN-US"}]{#struct_0_x1261_x1417_x1668063160}

[[申请本地证书成功。开始验证本地证书]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x360764971}

[[Verified the local certificate successfully.]{lang="EN-US"}]{#struct_0_x1261_x1417_1394340818}

[[Saving the local certificate to the device\...]{lang="EN-US"}]{#struct_0_x1261_x1417_1778574553}

[[验证本地证书成功。存储本地证书到设备中]{style="font-family:宋体"}]{#struct_0_x1261_x1417_262407882}

[[SCEP: Failed to get local certificate.]{lang="EN-US"}]{#struct_0_x1261_x1417_x1881551820}

[[获取本地证书失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_451644023}

[[Request certificate successfully.]{lang="EN-US"}]{#struct_0_x1261_x1417_1454436518}

[[证书申请成功]{style="font-family:宋体;
  color:black"}]{#struct_0_x1261_x1417_1779164377}

[[Failed to request certificate.]{lang="EN-US"}]{#struct_0_x1261_x1417_1808664408}

[[证书申请失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x1394018796}

[[Failed to start certificate request process.]{lang="EN-US"}]{#struct_0_x1261_x1417_804002060}

[[启动申请证书程序失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_1779229913}

[[Start enroll certificate process successfully.]{lang="EN-US"}]{#struct_0_x1261_x1417_1855134678}

[[启动申请证书程序成功]{style="font-family:宋体;color:black"}]{#struct_0_x1261_x1417_832852617}

[[No CA/RA certificates, try to get them from server.]{lang="EN-US"}]{#struct_0_x1261_x1417_1389519851}

[[没有]{style="font-family:宋体;
  color:black"}[CA/RA]{lang="EN-US" style="color:black"}]{#struct_0_x1261_x1417_1778640086}[证书，尝试从服务器获取它们]{style="font-family:宋体;color:black"}

[[Failed to get CA/RA certificates.]{lang="EN-US"}]{#struct_0_x1261_x1417_666711244}

[[获取]{style="font-family:宋体"}[CA/RA]{lang="EN-US"}]{#struct_0_x1261_x1417_163847967}[证书失败]{style="font-family:宋体"}

[[Got the CA/RA certificates successfully.]{lang="EN-US"}]{#struct_0_x1261_x1417_x2058271534}

[[获取]{style="font-family:宋体;
  color:black"}[CA/RA]{lang="EN-US" style="color:black"}]{#struct_0_x1261_x1417_1778705622}[证书成功]{style="font-family:宋体;color:black"}

[[Failed to get local public key.]{lang="EN-US"}]{#struct_0_x1261_x1417_x875195788}

[[获取本地密钥对失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_154755013}

[[Create the PKCS#10 request successfully.]{lang="EN-US" style="color:black"}]{#struct_0_x1261_x1417_1941652275}

[[建立]{style="font-family:宋体;
  color:black"}[ PKCS#10 ]{lang="EN-US" style="color:black"}]{#struct_0_x1261_x1417_1778771158}[申请成功]{style="font-family:宋体;color:black"}

[[Failed to create PKCS#10 certificate request.]{lang="EN-US"}]{#struct_0_x1261_x1417_266977285}

[[创建]{style="font-family:宋体"}[PKCS#10]{lang="EN-US"}]{#struct_0_x1261_x1417_x1226035098}[类型的证书申请失败]{style="font-family:宋体"}

[[Failed to get subject name from request.]{lang="EN-US"}]{#struct_0_x1261_x1417_1778836694}

[[从申请中获取主题名称失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x1289031767}

[[Failed to get issuer name from request.]{lang="EN-US"}]{#struct_0_x1261_x1417_x216184277}

[[从申请中获取颁发者名称失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x184900479}

[[PKCS#7 envelope: Failed to create certificate stack.]{lang="EN-US"}]{#struct_0_x1261_x1417_1778377942}

[[建立证书栈失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_990411828}

[[PKCS#7 envelope: Encrypted payload successfully.]{lang="EN-US"}]{#struct_0_x1261_x1417_250668723}

[[加密载荷成功]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x278760068}

[[PKCS#7 develope: Failed to get ASN.1 object.]{lang="EN-US"}]{#struct_0_x1261_x1417_1778443478}

[[获取]{style="font-family:宋体"}[ASN.1]{lang="EN-US"}]{#struct_0_x1261_x1417_x1663915748}[格式的对象失败]{style="font-family:宋体"}

[[PKCS#7 develope: Failed to find attribute.]{lang="EN-US"}]{#struct_0_x1261_x1417_x1727412007}

[[查找属性失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_1778509014}

[[PKCS#7 develope: Wrong ASN.1 type.]{lang="EN-US"}]{#struct_0_x1261_x1417_1884560111}

[[错误的]{style="font-family:宋体"}[ASN.1]{lang="EN-US"}]{#struct_0_x1261_x1417_1072527056}[类型]{style="font-family:宋体"}

[[PKCS#7 develope: Failed to get ASN.1 string.]{lang="EN-US"}]{#struct_0_x1261_x1417_1778574550}

[[获取]{style="font-family:宋体"}[ASN.1]{lang="EN-US"}]{#struct_0_x1261_x1417_262342346}[字符串失败]{style="font-family:宋体"}

[[PKCS#7 develope: Wrong failure information in reply.]{lang="EN-US"}]{#struct_0_x1261_x1417_158369205}

[[回应报文中错误的失败信息]{style="font-family:宋体"}]{#struct_0_x1261_x1417_1779164374}

[[PKCS#7 develope: Failed to get PKI status in reply.]{lang="EN-US"}]{#struct_0_x1261_x1417_1808729944}

[[在回应报文中获取]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_x1261_x1417_x289456896}[状态信息失败]{style="font-family:宋体"}

[[PKCS#7 develope: Wrong PKI status.]{lang="EN-US"}]{#struct_0_x1261_x1417_1779229910}

[[PKI ]{lang="EN-US"}]{#struct_0_x1261_x1417_1855200214}[状态信息出错]{style="font-family:宋体"}

[[PKCS#7 develope: Wrong PKI status in reply, Error code: *state_error*.]{lang="EN-US"}]{#struct_0_x1261_x1417_x1903483566}

[[回应报文中的]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_x1261_x1417_1778640087}[状态信息错误，错误码为]{style="font-family:宋体"}*[state_error]{lang="EN-US"}*

[[PKCS#7 develope: Failed to get recipient nonce from reply.]{lang="EN-US"}]{#struct_0_x1261_x1417_666776780}

[[从回应报文中获取]{style="font-family:宋体"}[CA]{lang="EN-US"}]{#struct_0_x1261_x1417_x1066769028}[服务器回应的]{style="font-family:宋体"}[nonce]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[PKCS#7 develope: Received nonce is inconsistent with sender nonce.]{lang="EN-US"}]{#struct_0_x1261_x1417_1778705623}

[[CA]{lang="EN-US"}]{#struct_0_x1261_x1417_x875130252}[服务器回应的]{style="font-family:宋体"}[nonce]{lang="EN-US"}[与本地的]{style="font-family:宋体"}[sender nonce]{lang="EN-US"}[不一致]{style="font-family:宋体"}

[[PKCS#7 develope: Failed to get sender nonce from reply.]{lang="EN-US"}]{#struct_0_x1261_x1417_1778771159}

[[在回应报文中获取不到]{style="font-family:宋体"}[CA]{lang="EN-US"}]{#struct_0_x1261_x1417_266911749}[服务器的]{style="font-family:宋体"}[sender nonce]{lang="EN-US"}

[[PKCS#7 develope: Wrong message type *error_type*.]{lang="EN-US"}]{#struct_0_x1261_x1417_1521448751}

[[错误的消息类型为]{style="font-family:宋体"}*[error_type]{lang="EN-US"}*]{#struct_0_x1261_x1417_1778836695}

[[PKCS#7 develope: Failed to get transaction ID from reply.]{lang="EN-US"}]{#struct_0_x1261_x1417_x1289097303}

[[从回应报文中无法获取]{style="font-family:宋体"}[ transaction ID ]{lang="EN-US"}]{#struct_0_x1261_x1417_x1684871503}[信息]{style="font-family:宋体"}

[[PKCS#7 develope: Transaction ID mismatched, received transaction ID is: *trans-id*.]{lang="EN-US"}]{#struct_0_x1261_x1417_1778377943}

[[Transaction ID ]{lang="EN-US"}]{#struct_0_x1261_x1417_990346292}[信息不匹配，接收到的]{style="font-family:宋体"}[Transaction ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[trans-id]{lang="EN-US"}*

[[PKCS#7 develope: Reply message is not signed.]{lang="EN-US"}]{#struct_0_x1261_x1417_1778443479}

[[PKCS#7]{lang="EN-US"}]{#struct_0_x1261_x1417_x1663850212}[格式的回应报文没有被签名]{style="font-family:宋体"}

[[PKCS#7 develope: Failed to get reply signer information.]{lang="EN-US"}]{#struct_0_x1261_x1417_x1522343058}

[[不能获取回应报文中签名者信息]{style="font-family:宋体"}]{#struct_0_x1261_x1417_1778509015}

[[PKCS#7 develope: Failed to verify signature.]{lang="EN-US"}]{#struct_0_x1261_x1417_1884625647}

[[验证签名失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_1778574551}

[[PKCS#7 develope: Failed to read inner PKCS#7.]{lang="EN-US"}]{#struct_0_x1261_x1417_262276810}

[[不能读取内层]{style="font-family:宋体"}[PKCS#7]{lang="EN-US"}]{#struct_0_x1261_x1417_1779164375}[格式的消息]{style="font-family:宋体"}

[[PKCS#7 develope: Failed to decrypt inner PKCS#7.]{lang="EN-US"}]{#struct_0_x1261_x1417_1808795480}

[[解密内层]{style="font-family:宋体"}[PKCS#7]{lang="EN-US"}]{#struct_0_x1261_x1417_1369926280}[格式的消息失败]{style="font-family:宋体"}

[[PKCS#7 develope: Illegal size of payload.]{lang="EN-US"}]{#struct_0_x1261_x1417_1779229911}

[[非法的载荷大小]{style="font-family:宋体"}]{#struct_0_x1261_x1417_1855265750}

[[No certificate in reply message.]{lang="EN-US"}]{#struct_0_x1261_x1417_x950243265}

[[在回应报文中没有证书信息]{style="font-family:宋体"}]{#struct_0_x1261_x1417_493720592}

[*[number]{lang="EN-US"}*[ certificates in reply message.]{lang="EN-US"}]{#struct_0_x1261_x1417_x950177729}

[[回应报文中携带]{style="font-family:宋体"}*[number]{lang="EN-US"}*]{#struct_0_x1261_x1417_x251936313}[个证书]{style="font-family:宋体"}

[[PKCS#7 develope: Error reason: *string*.]{lang="EN-US"}]{#struct_0_x1261_x1417_x312133811}

[[解析回应报文失败的错误原因为]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_x1261_x1417_x950112193}

[[Failed to wrap PKCS#7 message.]{lang="EN-US"}]{#struct_0_x1261_x1417_1657473225}

[[封装]{style="font-family:宋体"}[PKCS#7]{lang="EN-US"}]{#struct_0_x1261_x1417_x950046657}[格式的消息失败]{style="font-family:宋体"}

[[Failed to parse URL.]{lang="EN-US"}]{#struct_0_x1261_x1417_132199934}

[[解析]{style="font-family:宋体"}[URL]{lang="EN-US"}]{#struct_0_x1261_x1417_x950505409}[信息失败]{style="font-family:宋体"}

[[Failed to create socket. Error code: *error-code*.]{lang="EN-US"}]{#struct_0_x1261_x1417_x1044075677}

[[建立]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x1261_x1417_x950439873}[连接失败，错误码为]{style="font-family:宋体"}*[error-code]{lang="EN-US"}*

[[Failed to get response payload.]{lang="EN-US"}]{#struct_0_x1261_x1417_878650059}

[[获取响应载荷失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x950374337}

[[Reply type: *type*.]{lang="EN-US"}]{#struct_0_x1261_x1417_109584319}

[[应答消息返回类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*]{#struct_0_x1261_x1417_x950308801}

[[Failed to get response type.]{lang="EN-US"}]{#struct_0_x1261_x1417_x693528832}

[[获取响应类型失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x949718977}

[[Failed to read response message. Error code: *error-code*.]{lang="EN-US"}]{#struct_0_x1261_x1417_910276168}

[[读取响应信息失败，错误码为]{style="font-family:宋体"}*[error-code]{lang="EN-US"}*]{#struct_0_x1261_x1417_1851635252}

[[Failed to send SCEP message.]{lang="EN-US"}]{#struct_0_x1261_x1417_x949653441}

[[发送]{style="font-family:宋体"}[SCEP]{lang="EN-US"}]{#struct_0_x1261_x1417_x2137154311}[消息失败]{style="font-family:宋体"}

[[Failed to unwrap PKCS#7 message.]{lang="EN-US"}]{#struct_0_x1261_x1417_x950243264}

[[解封装]{style="font-family:宋体"}[PKCS#7]{lang="EN-US"}]{#struct_0_x1261_x1417_493655056}[格式的消息失败]{style="font-family:宋体"}

[[Polling counter reaches the upper limit.]{lang="EN-US"}]{#struct_0_x1261_x1417_x950177728}

[[轮询计数器已达到最大值]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x251870777}

[[Unknown return status *status-code.*]{lang="EN-US"}]{#struct_0_x1261_x1417_x950112192}

[[未知的返回状态码为]{style="font-family:宋体"}*[status-code]{lang="EN-US"}*]{#struct_0_x1261_x1417_x950046656}

[[Reply message status: *state*.]{lang="EN-US"}]{#struct_0_x1261_x1417_132134398}

[[返回信息状态值为]{style="font-family:宋体"}*[state]{lang="EN-US"}*]{#struct_0_x1261_x1417_x950505408}

[[Failed to initiate SCEP.]{lang="EN-US"}]{#struct_0_x1261_x1417_x1044141213}

[[初始化]{style="font-family:宋体"}[SCEP]{lang="EN-US"}]{#struct_0_x1261_x1417_x950439872}[失败]{style="font-family:宋体"}

[[Failed to get options of the SCEP process.]{lang="EN-US"}]{#struct_0_x1261_x1417_878715595}

[[解析命令行，获取程序运行参数失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x950374336}

[[Unable to continue current SCEP process.]{lang="EN-US"}]{#struct_0_x1261_x1417_109649855}

[[不能断续执行当前]{style="font-family:宋体"}[SCEP]{lang="EN-US"}]{#struct_0_x1261_x1417_x950308800}[程序]{style="font-family:宋体"}

[[Failed to initialize signal.]{lang="EN-US"}]{#struct_0_x1261_x1417_x693594368}

[[初始化信号失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x949718976}

[[SCEP: Host: *string*; Port: *port*; Path: *path*.]{lang="EN-US"}]{#struct_0_x1261_x1417_x949653440}

[[解析]{style="font-family:宋体"}[URL]{lang="EN-US"}]{#struct_0_x1261_x1417_x2137088775}[的具体信息：主机地址为]{style="font-family:宋体"}*[string]{lang="EN-US"}*[；端口号为]{style="font-family:宋体"}*[port]{lang="EN-US"}*[；路径为]{style="font-family:宋体"}*[path]{lang="EN-US"}*

[[PKCS#7 envelope: Failed to add signed certificate to PKCS#7 request.]{lang="EN-US"}]{#struct_0_x1261_x1417_x950243267}

[[添加签名证书到]{style="font-family:宋体"}[PKCS#7]{lang="EN-US"}]{#struct_0_x1261_x1417_493589520}[格式的请求失败]{style="font-family:宋体"}

[[PKCS#7 envelope: Failed to sign PKCS#7 request.]{lang="EN-US"}]{#struct_0_x1261_x1417_x950177731}

[[签名]{style="font-family:宋体"}[PKCS#7]{lang="EN-US"}]{#struct_0_x1261_x1417_x251412024}[格式的请求失败]{style="font-family:宋体"}

[[PKCS#7 envelope: Failed to set signature attribute.]{lang="EN-US"}]{#struct_0_x1261_x1417_x950112195}

[[设置签名属性失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_1657604297}

[[PKCS#7 envelope: Failed to create PKCS#7 data.]{lang="EN-US"}]{#struct_0_x1261_x1417_x950046659}

[[创建]{style="font-family:宋体"}[PKCS#7]{lang="EN-US"}]{#struct_0_x1261_x1417_x950505411}[格式的数据失败]{style="font-family:宋体"}

[[SCEP: Failed to encode data in BASE64.]{lang="EN-US"}]{#struct_0_x1261_x1417_x1044599964}

[[将数据编码为]{style="font-family:宋体"}[BASE64 ]{lang="EN-US"}]{#struct_0_x1261_x1417_x950439875}[类型时失败]{style="font-family:宋体"}

[[PKCS#7 develope: Failed to get attributes. ]{lang="EN-US"}]{#struct_0_x1261_x1417_879043275}

[[获取属性失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x950374339}

[[PKCS#7 develope: Failed to handle signature attributes.]{lang="EN-US"}]{#struct_0_x1261_x1417_x950308803}

[[处理签名属性失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x693659904}

[[Failed to bind port. Error code: *error-code*.]{lang="EN-US"}]{#struct_0_x1261_x1417_x949718979}

[[通信端口绑定错误，错误码为]{style="font-family:宋体"}*[error-code]{lang="EN-US"}*]{#struct_0_x1261_x1417_910407240}

[[Failed to connect to the CA server. Error code: *error-code*.]{lang="EN-US"}]{#struct_0_x1261_x1417_x949653443}

[[与]{style="font-family:宋体"}[CA]{lang="EN-US"}]{#struct_0_x1261_x1417_x950243266}[服务器连接失败，错误码为]{style="font-family:宋体"}*[error-code]{lang="EN-US"}*

[[SCEP: De-encapsulated PKCS#7 packet successfully.]{lang="EN-US"}]{#struct_0_x1261_x1417_493523984}

[[解封装]{style="font-family:宋体"}[PKCS#7]{lang="EN-US"}]{#struct_0_x1261_x1417_x950177730}[格式的数据包成功]{style="font-family:宋体"}

[[SCEP: Failed to create message.]{lang="EN-US"}]{#struct_0_x1261_x1417_x251346488}

[[构造消息失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x950112194}

[[Failed to create self-signed certificate.]{lang="EN-US"}]{#struct_0_x1261_x1417_x950046658}

[[创建自签名证书失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_132003326}

[[SCEP request message : *string*]{lang="EN-US"}]{#struct_0_x1261_x1417_x950505410}

[[SCEP]{lang="EN-US"}]{#struct_0_x1261_x1417_x950439874}[申请信息的内容为]{style="font-family:宋体"}*[string]{lang="EN-US"}*

[[The signing or encryption process is running with general process at the same time. Can\'t start the current enrolling process.]{lang="EN-US"}]{#struct_0_x1261_x1417_879108811}

[[签名或加密程序和通用程序在同一时间运行，不能启动申请程序]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x950374338}

[[The signature or encryption is running with general at the same time, can\'t start current enroll process.]{lang="EN-US"}]{#struct_0_x1261_x1417_x950308802}

[[签名或加密用途证书的申请程序，不能和通用用途证书的申请程序同时启动，不能启动当前申请程序]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x693725440}

[[PKCS#7 develope: Failed to get failure information from reply.]{lang="EN-US"}]{#struct_0_x1261_x1417_x949718978}

[[从回应中获取失败信息失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_910472776}

[[Failed to generate the extension attributes for PKCS#10 request.]{lang="EN-US"}]{#struct_0_x1261_x1417_x949653442}

[[产生]{style="font-family:宋体"}[PKCS#10]{lang="EN-US"}]{#struct_0_x1261_x1417_x950243269}[申请的扩展属性失败]{style="font-family:宋体"}

[[Incomplete DN configuration.]{lang="EN-US"}]{#struct_0_x1261_x1417_493458448}

[[DN]{lang="EN-US"}]{#struct_0_x1261_x1417_x950177733}[配置不完整]{style="font-family:宋体"}

[[Invalid PKI entity.]{lang="EN-US"}]{#struct_0_x1261_x1417_x950112197}

[[实体无效]{style="font-family:宋体"}]{#struct_0_x1261_x1417_1657735369}

[[The local cert is]{lang="EN-US"}]{#struct_0_x1261_x1417_x950046661}

[[:*local-cert*]{lang="EN-US"}]{#struct_0_x1261_x1417_x950505413}

[[本地证书的内容为：]{style="font-family:宋体"}*[local-cert]{lang="EN-US"}*]{#struct_0_x1261_x1417_x1044731036}

[[A request already exists for the same local certificate.]{lang="EN-US"}]{#struct_0_x1261_x1417_x950439877}

[[对于该本地证书，已经存在一个申请]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x950374341}

[[The local certificate has passed verification, and is being saved to the device\...]{lang="EN-US"}]{#struct_0_x1261_x1417_x950308805}

[[验证本地证书成功，保存本地证书]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x693266688}

[[Send message to SCEP application.]{lang="EN-US"}]{#struct_0_x1261_x1417_x949718981}

[[发送消息到]{style="font-family:宋体"}[SCEP]{lang="EN-US"}]{#struct_0_x1261_x1417_x949653445}[程序]{style="font-family:宋体"}

[[ ]{lang="EN-US"}]{#_Toc130718928}

[[表1-3 ]{lang="EN-US"}[debugging pki retrieval]{lang="EN-US"}]{#struct_0_x1261_x1417_x2137416455}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1373174674}[[字段]{style="font-family:黑体;
   color:black"}]{#struct_0_x1261_x1417_2071101195}

[[描述]{style="font-family:黑体;color:black"}]{#struct_0_x1261_x1417_x76827759}

[[The process is running. Unable to start the process.]{lang="EN-US"}]{#struct_0_x1261_x1417_x1445965609}

[[有同样的进程正在运行，不能启动现有申请程序]{style="font-family:宋体"}]{#struct_0_x1261_x1417_735231037}

[[Got CRLs successfully.]{lang="EN-US" style="color:black"}]{#struct_0_x1261_x1417_x950243268}

[[获取]{style="font-family:宋体;color:black"}[CRL]{lang="EN-US" style="color:black"}]{#struct_0_x1261_x1417_493392912}[成功]{style="font-family:宋体;
  color:black"}

[[Failed to get CRLs.]{lang="EN-US"}]{#struct_0_x1261_x1417_1404776206}

[[获取]{style="font-family:宋体"}[CRL]{lang="EN-US"}]{#struct_0_x1261_x1417_487525567}[失败]{style="font-family:宋体"}

[[Certificate chain doesn't have a root CA.]{lang="EN-US" style="color:black"}]{#struct_0_x1261_x1417_x1828028898}

[[证书没有根]{style="font-family:宋体;
  color:black"}[CA]{lang="EN-US" style="color:black"}]{#struct_0_x1261_x1417_x950177732}

[[Failed to get subject name from request.]{lang="EN-US"}]{#struct_0_x1261_x1417_x251477560}

[[从申请中获取主题名称失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_98091602}

[[Failed to get issuer name from request.]{lang="EN-US"}]{#struct_0_x1261_x1417_1634669846}

[[从申请中获取颁发者名称失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_989611281}

[[Failed to get issuer name from CA certificate.]{lang="EN-US"}]{#struct_0_x1261_x1417_1924697441}

[[从]{style="font-family:宋体"}[CA]{lang="EN-US"}]{#struct_0_x1261_x1417_x950112196}[证书获取证书颁发者名称失败]{style="font-family:宋体"}

[[Failed to get serial number from CA certificate.]{lang="EN-US"}]{#struct_0_x1261_x1417_1657800905}

[[从]{style="font-family:宋体"}[CA]{lang="EN-US"}]{#struct_0_x1261_x1417_543368200}[证书获取序列号失败]{style="font-family:宋体"}

[[PKCS#7 envelope: Failed to create certificate stack.]{lang="EN-US"}]{#struct_0_x1261_x1417_x1910116845}

[[建立证书栈失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x739266776}

[[PKCS#7 envelope: Encrypted payload successfully.]{lang="EN-US"}]{#struct_0_x1261_x1417_x950046660}

[[加密载荷成功]{style="font-family:宋体"}]{#struct_0_x1261_x1417_132527617}

[[PKCS#7 develope: Failed to get ASN.1 object.]{lang="EN-US"}]{#struct_0_x1261_x1417_931810029}

[[获取]{style="font-family:宋体"}[ASN.1]{lang="EN-US"}]{#struct_0_x1261_x1417_1421943575}[格式的对象失败]{style="font-family:宋体"}

[[PKCS#7 develope: Failed to find attribute.]{lang="EN-US"}]{#struct_0_x1261_x1417_x950505412}

[[查找属性失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x1044796572}

[[PKCS#7 develope: Wrong ASN.1 type.]{lang="EN-US"}]{#struct_0_x1261_x1417_250291187}

[[错误的]{style="font-family:宋体"}[ASN.1]{lang="EN-US"}]{#struct_0_x1261_x1417_421300917}[类型]{style="font-family:宋体"}

[[PKCS#7 develope: Failed to get ASN.1 string.]{lang="EN-US"}]{#struct_0_x1261_x1417_1248075866}

[[获取]{style="font-family:宋体"}[ASN.1]{lang="EN-US"}]{#struct_0_x1261_x1417_x950439876}[字符串失败]{style="font-family:宋体"}

[[PKCS#7 develope: Failed to get failure information from reply.]{lang="EN-US"}]{#struct_0_x1261_x1417_878977739}

[[在回应报文中获取错误信息失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_1178332865}

[[PKCS#7 develope: Wrong failure Information in reply.]{lang="EN-US"}]{#struct_0_x1261_x1417_x501473698}

[[回应报文中错误的失败信息]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x950374340}

[[PKCS#7 develope: Failed to get PKI status in reply.]{lang="EN-US"}]{#struct_0_x1261_x1417_110043072}

[[在回应报文中获取]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_x1261_x1417_435430248}[状态信息失败]{style="font-family:宋体"}

[[PKCS#7 develope: Wrong PKI status.]{lang="EN-US"}]{#struct_0_x1261_x1417_x24369471}

[[PKI]{lang="EN-US"}]{#struct_0_x1261_x1417_x950308804}[状态出错]{style="font-family:宋体"}

[[PKCS#7 develope: Wrong PKI status in reply, *state_error*.]{lang="EN-US"}]{#struct_0_x1261_x1417_x693332224}

[[回应报文中的]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_x1261_x1417_x1901249365}[状态信息错误，错误码为]{style="font-family:宋体"}*[state_error]{lang="EN-US"}*

[[PKCS#7 develope: Failed to get recipient nonce from reply.]{lang="EN-US"}]{#struct_0_x1261_x1417_x949718980}

[[从回应报文中获取]{style="font-family:宋体"}[CA]{lang="EN-US"}]{#struct_0_x1261_x1417_909948497}[服务器回应的]{style="font-family:宋体"}[nonce]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[PKCS#7 develope: Received nonce is inconsistent with sender nonce.]{lang="EN-US"}]{#struct_0_x1261_x1417_x1595914182}

[[CA]{lang="EN-US"}]{#struct_0_x1261_x1417_2017447031}[服务器回应的]{style="font-family:宋体"}[nonce]{lang="EN-US"}[与本地的]{style="font-family:宋体"}[sender nonce]{lang="EN-US"}[不一致]{style="font-family:宋体"}

[[PKCS#7 develope: Failed to get sender nonce from reply.]{lang="EN-US"}]{#struct_0_x1261_x1417_x949653444}

[[在回应报文中获取不到]{style="font-family:宋体"}[CA]{lang="EN-US"}]{#struct_0_x1261_x1417_x2137350919}[服务器的]{style="font-family:宋体"}[sender nonce]{lang="EN-US"}

[[PKCS#7 develope: Wrong message type *error_type*.]{lang="EN-US"}]{#struct_0_x1261_x1417_x540029800}

[[错误的消息类型为]{style="font-family:宋体"}*[error_type]{lang="EN-US"}*]{#struct_0_x1261_x1417_615840676}

[[PKCS#7 develope: Failed to get transaction ID from reply.]{lang="EN-US"}]{#struct_0_x1261_x1417_x914404500}

[[从回应报文中无法获取]{style="font-family:宋体"}[transaction ID]{lang="EN-US"}]{#struct_0_x1261_x1417_x1581275895}[信息]{style="font-family:宋体"}

[[PKCS#7 develope: Transaction ID mismatched, received transaction ID is: *trans-id*.]{lang="EN-US"}]{#struct_0_x1261_x1417_1089016003}

[[transaction ID ]{lang="EN-US"}]{#struct_0_x1261_x1417_615906212}[信息不匹配，接收到的]{style="font-family:宋体"}[Transaction ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[trans-id]{lang="EN-US"}*

[[PKCS#7 develope: Reply message is not signed.]{lang="EN-US"}]{#struct_0_x1261_x1417_x1339417000}

[[PKCS#7]{lang="EN-US"}]{#struct_0_x1261_x1417_x2123967218}[格式的回应报文没有被签名]{style="font-family:宋体"}

[[PKCS#7 develope: Failed to get reply signer information.]{lang="EN-US"}]{#struct_0_x1261_x1417_615971748}

[[不能获取回应报文中签名者信息]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x522791360}

[[PKCS#7 develope: Failed to verify signature.]{lang="EN-US"}]{#struct_0_x1261_x1417_78083607}

[[验证签名失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_616037284}

[[PKCS#7 develope: Failed to read inner PKCS#7.]{lang="EN-US"}]{#struct_0_x1261_x1417_x1978392866}

[[不能读取内层]{style="font-family:宋体"}[PKCS#7]{lang="EN-US"}]{#struct_0_x1261_x1417_1134653640}[格式的消息]{style="font-family:宋体"}

[[PKCS#7 develope: Failed to decrypt inner PKCS#7.]{lang="EN-US"}]{#struct_0_x1261_x1417_615578532}

[[解密内层]{style="font-family:宋体"}[PKCS#7]{lang="EN-US"}]{#struct_0_x1261_x1417_x1432633472}[格式的消息失败]{style="font-family:宋体"}

[[PKCS#7 develope: Illegal size of payload.]{lang="EN-US"}]{#struct_0_x1261_x1417_x1228684460}

[[非法的载荷大小]{style="font-family:宋体"}]{#struct_0_x1261_x1417_615644068}

[[No certificate in reply message.]{lang="EN-US"}]{#struct_0_x1261_x1417_1922631440}

[[在回应报文中没有证书信息]{style="font-family:宋体"}]{#struct_0_x1261_x1417_615709604}

[[Failed to get CRLs from reply.]{lang="EN-US"}]{#struct_0_x1261_x1417_x1939584026}

[[在回应报文中无法获取]{style="font-family:宋体"}[CRL]{lang="EN-US"}]{#struct_0_x1261_x1417_x195482943}[列表信息]{style="font-family:宋体"}

[[Failed to get CRL data in CRLs from reply.]{lang="EN-US"}]{#struct_0_x1261_x1417_615775140}

[[无法获取到回应报文中的]{style="font-family:宋体"}[CRL]{lang="EN-US"}]{#struct_0_x1261_x1417_x1936092694}[列表里的表信息]{style="font-family:宋体"}

[[PKCS#7 develope: Error reason: *string*.]{lang="EN-US"}]{#struct_0_x1261_x1417_x923605733}

[[解析回应报文失败的错误原因为]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_x1261_x1417_616364964}

[[Failed to wrap PKCS#7 message.]{lang="EN-US"}]{#struct_0_x1261_x1417_x2102197024}

[[封装]{style="font-family:宋体"}[PKCS#7]{lang="EN-US"}]{#struct_0_x1261_x1417_x29478211}[格式的消息失败]{style="font-family:宋体"}

[[Failed to parse URL.]{lang="EN-US"}]{#struct_0_x1261_x1417_616430500}

[[解析]{style="font-family:宋体"}[URL]{lang="EN-US"}]{#struct_0_x1261_x1417_x310281045}[信息失败]{style="font-family:宋体"}

[[Failed to create socket. Error code: *error-code*.]{lang="EN-US"}]{#struct_0_x1261_x1417_615840677}

[[建立]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x1261_x1417_x914404499}[连接失败，错误码为]{style="font-family:宋体"}*[error-code]{lang="EN-US"}*

[[Failed to get response payload.]{lang="EN-US"}]{#struct_0_x1261_x1417_375629072}

[[获取响应载荷失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_615906213}

[[Reply type: *type*.]{lang="EN-US"}]{#struct_0_x1261_x1417_x1339416999}

[[应答消息返回类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*]{#struct_0_x1261_x1417_615971749}

[[Failed to get response type.]{lang="EN-US"}]{#struct_0_x1261_x1417_x522791361}

[[获取响应类型失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_78018071}

[[Failed to read response message. ]{lang="EN-US"}]{#struct_0_x1261_x1417_616037285}

[[读取响应信息失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x1978392867}

[[Failed to unwrap PKCS#7 message.]{lang="EN-US"}]{#struct_0_x1261_x1417_615578533}

[[解封装]{style="font-family:宋体"}[PKCS#7]{lang="EN-US"}]{#struct_0_x1261_x1417_x1432633473}[格式的消息失败]{style="font-family:宋体"}

[[Unknown return status *status-code.*]{lang="EN-US"}]{#struct_0_x1261_x1417_615644069}

[[未知的返回状态码为]{style="font-family:宋体"}*[status-code]{lang="EN-US"}*]{#struct_0_x1261_x1417_1922631441}

[[Reply message status: *state*.]{lang="EN-US"}]{#struct_0_x1261_x1417_1696180277}

[[返回信息状态值为]{style="font-family:宋体"}*[state]{lang="EN-US"}*]{#struct_0_x1261_x1417_615709605}

[[Failed to send SCEP message.]{lang="EN-US"}]{#struct_0_x1261_x1417_x1939584025}

[[发送]{style="font-family:宋体"}[SCEP]{lang="EN-US"}]{#struct_0_x1261_x1417_615775141}[消息失败]{style="font-family:宋体"}

[[SCEP: No valid payload in reply message when retrieving CA/RA certificates.]{lang="EN-US"}]{#struct_0_x1261_x1417_x1936092695}

[[在获取]{style="font-family:宋体"}[CA/RA]{lang="EN-US"}]{#struct_0_x1261_x1417_616364965}[证书时没有发现有效的载荷在响应信息中]{style="font-family:宋体"}

[[SCEP: Got CA/RA certificates successfully.]{lang="EN-US"}]{#struct_0_x1261_x1417_x2102197023}

[[获取]{style="font-family:宋体"}[CA/RA]{lang="EN-US"}]{#struct_0_x1261_x1417_730036676}[证书成功]{style="font-family:宋体"}

[[SCEP: Failed to get CA/RA certificates.]{lang="EN-US"}]{#struct_0_x1261_x1417_616430501}

[[获取]{style="font-family:宋体"}[CA/RA]{lang="EN-US"}]{#struct_0_x1261_x1417_x310281046}[证书失败]{style="font-family:宋体"}

[[Failed to initiate SCEP.]{lang="EN-US"}]{#struct_0_x1261_x1417_615840674}

[[初始化]{style="font-family:宋体"}[SCEP]{lang="EN-US"}]{#struct_0_x1261_x1417_x914404502}[失败]{style="font-family:宋体"}

[[Failed to get options of the SCEP process.]{lang="EN-US"}]{#struct_0_x1261_x1417_615906210}

[[解析命令行，获取程序运行参数失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x1339417002}

[[Unable to continue current SCEP process.]{lang="EN-US"}]{#struct_0_x1261_x1417_615971746}

[[不能断续执行当前]{style="font-family:宋体"}[SCEP]{lang="EN-US"}]{#struct_0_x1261_x1417_x522791354}[程序]{style="font-family:宋体"}

[[Failed to initialize signal.]{lang="EN-US"}]{#struct_0_x1261_x1417_616037282}

[[初始化信号失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x1978392868}

[[SCEP: Host: *string*; Port: *port*; Path: *path*.]{lang="EN-US"}]{#struct_0_x1261_x1417_615578530}

[[解析]{style="font-family:宋体"}[URL]{lang="EN-US"}]{#struct_0_x1261_x1417_x1432633474}[的具体信息：主机地址为]{style="font-family:宋体"}*[string]{lang="EN-US"}*[；端口号为]{style="font-family:宋体"}*[port]{lang="EN-US"}*[；路径为]{style="font-family:宋体"}*[path]{lang="EN-US"}*

[[PKCS#7 envelope: Failed to add signed certificate to PKCS#7 request.]{lang="EN-US"}]{#struct_0_x1261_x1417_615644066}

[[添加签名证书到]{style="font-family:宋体"}[PKCS#7]{lang="EN-US"}]{#struct_0_x1261_x1417_1922631438}[格式的请求失败]{style="font-family:宋体"}

[[PKCS#7 envelope: Failed to sign PKCS#7 request.]{lang="EN-US"}]{#struct_0_x1261_x1417_615709602}

[[签名]{style="font-family:宋体"}[PKCS#7]{lang="EN-US"}]{#struct_0_x1261_x1417_x1939584020}[格式的请求失败]{style="font-family:宋体"}

[[PKCS#7 envelope: Failed to set signature attribute.]{lang="EN-US"}]{#struct_0_x1261_x1417_615775138}

[[设置签名属性失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_402559458}

[[PKCS#7 envelope: Failed to create PKCS#7 data.]{lang="EN-US"}]{#struct_0_x1261_x1417_616364962}

[[创建]{style="font-family:宋体"}[PKCS#7]{lang="EN-US"}]{#struct_0_x1261_x1417_x2102197022}[格式的数据失败]{style="font-family:宋体"}

[[SCEP: Failed to encode data in BASE64.]{lang="EN-US"}]{#struct_0_x1261_x1417_616430498}

[[将数据编码为]{style="font-family:宋体"}[BASE64 ]{lang="EN-US"}]{#struct_0_x1261_x1417_2065106968}[类型时失败]{style="font-family:宋体"}

[[PKCS#7 develope: Failed to get attributes. ]{lang="EN-US"}]{#struct_0_x1261_x1417_615840675}

[[获取属性失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x914404501}

[[PKCS#7 develope: Failed to handle signature's attributes.]{lang="EN-US"}]{#struct_0_x1261_x1417_615906211}

[[处理签名的属性失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x1339417001}

[[Failed to bind port. Error code: *error-code*.]{lang="EN-US"}]{#struct_0_x1261_x1417_615971747}

[[通信端口绑定错误，错误码为]{style="font-family:宋体"}*[error-code]{lang="EN-US"}*]{#struct_0_x1261_x1417_x522791355}

[[Failed to connect to the CA server. Error code: *error-code*.]{lang="EN-US"}]{#struct_0_x1261_x1417_616037283}

[[与]{style="font-family:宋体"}[CA]{lang="EN-US"}]{#struct_0_x1261_x1417_615578531}[服务器连接失败，错误码为]{style="font-family:宋体"}*[error-code]{lang="EN-US"}*

[[SCEP: De-encapsulated PKCS#7 packet successfully.]{lang="EN-US"}]{#struct_0_x1261_x1417_x1432633475}

[[解封装]{style="font-family:宋体"}[PKCS#7]{lang="EN-US"}]{#struct_0_x1261_x1417_615644067}[格式的数据包成功]{style="font-family:宋体"}

[[SCEP: Failed to create message.]{lang="EN-US"}]{#struct_0_x1261_x1417_1922631439}

[[构造消息失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_615709603}

[[SCEP request message: *string*]{lang="EN-US"}]{#struct_0_x1261_x1417_x1939584019}

[[SCEP]{lang="EN-US"}]{#struct_0_x1261_x1417_615775139}[申请信息的内容为]{style="font-family:宋体"}*[string]{lang="EN-US"}*

[*[number]{lang="EN-US"}*[ certificates in reply message.]{lang="EN-US"}]{#struct_0_x1261_x1417_616364963}

[[回应报文中携带]{style="font-family:宋体"}*[number]{lang="EN-US"}*]{#struct_0_x1261_x1417_x2102197021}[个证书]{style="font-family:宋体"}

[[Verified the local certificate successfully.]{lang="EN-US"}]{#struct_0_x1261_x1417_616430499}

[[Saving the local certificate to the device\...]{lang="EN-US"}]{#struct_0_x1261_x1417_2065106967}

[[验证本地证书成功。存储本地证书到设备中]{style="font-family:宋体"}]{#struct_0_x1261_x1417_615840672}

[[Failed to start the getCRL process.]{lang="EN-US"}]{#struct_0_x1261_x1417_x914404504}

[[启动获取]{style="font-family:宋体"}[CRL]{lang="EN-US"}]{#struct_0_x1261_x1417_615906208}[的程序失败]{style="font-family:宋体"}

[[GetCRL process started successfully.]{lang="EN-US" style="color:black"}]{#struct_0_x1261_x1417_615971744}

[[启动获取]{style="font-family:宋体;
  color:black"}[CRL]{lang="EN-US" style="color:black"}]{#struct_0_x1261_x1417_x522791356}[的程序成功]{style="font-family:宋体;color:black"}

[[Verify CRLs : *string*]{lang="EN-US"}]{#struct_0_x1261_x1417_616037280}

[[验证]{style="font-family:宋体"}[CRL]{lang="EN-US"}]{#struct_0_x1261_x1417_x1978392870}[：验证结果为]{style="font-family:宋体"}*[string]{lang="EN-US"}*

[[CRL retrieval failed: Certificate request url is not configured.]{lang="EN-US"}]{#struct_0_x1261_x1417_615578528}

[[获取证书的]{style="font-family:宋体"}[URL]{lang="EN-US"}]{#struct_0_x1261_x1417_615644064}[没有配置]{style="font-family:宋体"}

[[CRL retrieval failed: Certificate request from is not configured.]{lang="EN-US"}]{#struct_0_x1261_x1417_1922631436}

[[获取证书的注册受理机构没有配置]{style="font-family:宋体"}]{#struct_0_x1261_x1417_615709600}

[[CRL retrieval failed: No local certificate.]{lang="EN-US"}]{#struct_0_x1261_x1417_x1939584022}

[[没有本地证书]{style="font-family:宋体"}]{#struct_0_x1261_x1417_615775136}

[[CRL retrieval failed: No RA certificate.]{lang="EN-US"}]{#struct_0_x1261_x1417_616364960}

[[没有]{style="font-family:宋体"}[RA]{lang="EN-US"}]{#struct_0_x1261_x1417_x2102197020}[证书]{style="font-family:宋体"}

[[CRL retrieval failed: The local public key and the public key in the local certificate are mismatching.]{lang="EN-US"}]{#struct_0_x1261_x1417_616430496}

[[本地证书和公钥不匹配]{style="font-family:宋体"}]{#struct_0_x1261_x1417_615840673}

[[CRL retrieved successfully.]{lang="EN-US" style="color:black"}]{#struct_0_x1261_x1417_x914404503}

[[获取]{style="font-family:宋体;color:black"}[CRL]{lang="EN-US" style="color:black"}]{#struct_0_x1261_x1417_615906209}[成功]{style="font-family:宋体;
  color:black"}

[[Failed to retrieve CRL.]{lang="EN-US"}]{#struct_0_x1261_x1417_999235167}

[[获取]{style="font-family:宋体"}[CRL]{lang="EN-US"}]{#struct_0_x1261_x1417_615971745}[失败]{style="font-family:宋体"}

[[CA Certificate is not exist.]{lang="EN-US"}]{#struct_0_x1261_x1417_616037281}

[[CA]{lang="EN-US"}]{#struct_0_x1261_x1417_x1978392871}[证书不存在]{style="font-family:宋体"}

[[Local Certificate and key is not matched.]{lang="EN-US"}]{#struct_0_x1261_x1417_615578529}

[[本地证书和公钥不匹配]{style="font-family:宋体"}]{#struct_0_x1261_x1417_615644065}

[[Failed to get data by curl.]{lang="EN-US"}]{#struct_0_x1261_x1417_1922631437}

[[从]{style="font-family:宋体"}[curl]{lang="EN-US"}]{#struct_0_x1261_x1417_615709601}[获取数据失败]{style="font-family:宋体"}

[[Got data by curl successfully.]{lang="EN-US"}]{#struct_0_x1261_x1417_615775137}

[[通过]{style="font-family:宋体"}[CRUL]{lang="EN-US"}]{#struct_0_x1261_x1417_402559463}[获取数据成功]{style="font-family:宋体"}

[[Got the CA certificate chain successfully.]{lang="EN-US"}]{#struct_0_x1261_x1417_616364961}

[[获取]{style="font-family:宋体"}[CA]{lang="EN-US"}]{#struct_0_x1261_x1417_616430497}[证书链成功]{style="font-family:宋体"}

[[Failed to save the local certificate to the device.]{lang="EN-US"}]{#struct_0_x1261_x1417_2065106965}

[[存储]{style="font-family:宋体"}[LOCAL]{lang="EN-US"}]{#struct_0_x1261_x1417_x2113042679}[证书失败]{style="font-family:宋体"}

[[Saved the peer certificate to the device successfully.]{lang="EN-US"}]{#struct_0_x1261_x1417_x2112977143}

[[存储]{style="font-family:宋体"}[PEER]{lang="EN-US"}]{#struct_0_x1261_x1417_x930842763}[证书成功]{style="font-family:宋体"}

[[Failed to save the peer certificates to the device.]{lang="EN-US"}]{#struct_0_x1261_x1417_x2112911607}

[[保存对端证书到设备失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x2112846071}

[[Verified peer certificate successfully. Saving the peer certificates to the device\...]{lang="EN-US"}]{#struct_0_x1261_x1417_x2010367213}

[[验证]{style="font-family:宋体"}[PEER]{lang="EN-US"}]{#struct_0_x1261_x1417_x2113304823}[证书成功，正在进行存储证书]{style="font-family:宋体"}

[[Failed to verify the peer certificates. Verification result: *result-string*]{lang="EN-US"}]{#struct_0_x1261_x1417_x2113239287}

[[验证]{style="font-family:宋体"}[PEER]{lang="EN-US"}]{#struct_0_x1261_x1417_x2113173751}[证书失败验证结果为]{style="font-family:宋体"}*[result-string]{lang="EN-US"}*

[[Certificate retrieval failed: The identity of the entity *entity-name* is not configured.]{lang="EN-US"}]{#struct_0_x1261_x1417_x286236428}

[[获取证书失败，未配置实体的]{style="font-family:宋体"}*[entity-name]{lang="EN-US"}*]{#struct_0_x1261_x1417_x2113108215}[身份信息]{style="font-family:宋体"}

[[Got CRL from response successfully.]{lang="EN-US"}]{#struct_0_x1261_x1417_x2112518391}

[[从响应报文中成功获取]{style="font-family:宋体"}[CRL]{lang="EN-US"}]{#struct_0_x1261_x1417_1192710323}

[[Failed to get encryption certificate.]{lang="EN-US"}]{#struct_0_x1261_x1417_x2112452855}

[[获取加密证书失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x2113042678}

[[Failed to save the CA/RA certificate chain.]{lang="EN-US"}]{#struct_0_x1261_x1417_x2112977142}

[[保存]{style="font-family:宋体"}[CA/RA]{lang="EN-US"}]{#struct_0_x1261_x1417_1798040592}[证书链失败]{style="font-family:宋体"}

[[Saved the CA/RA certificate chain successfully.]{lang="EN-US"}]{#struct_0_x1261_x1417_x2112911606}

[[成功保存]{style="font-family:宋体"}[CA/RA]{lang="EN-US"}]{#struct_0_x1261_x1417_x2112846070}[证书链]{style="font-family:宋体"}

[[Verified the CA/RA certificate chain successfully. Saving the CA/RA certificate chain to the device\...]{lang="EN-US"}]{#struct_0_x1261_x1417_x2113304822}

[[CA/RA]{lang="EN-US"}]{#struct_0_x1261_x1417_x755253857}[链验证成功，开始保存]{style="font-family:宋体"}[CA/RA]{lang="EN-US"}[证书链]{style="font-family:宋体"}

[[Failed to verify the CA/RA certificate chain. Verification result: *result-string*]{lang="EN-US"}]{#struct_0_x1261_x1417_x2113239286}

[[验证]{style="font-family:宋体"}[CA/RA]{lang="EN-US"}]{#struct_0_x1261_x1417_x2113173750}[证书链失败，验证结果为]{style="font-family:宋体"}*[result-string]{lang="EN-US"}*

[[PKCS#7 develope: Wrong PKI status.]{lang="EN-US"}]{#struct_0_x1261_x1417_x2113108214}

[[PKI]{lang="EN-US"}]{#struct_0_x1261_x1417_x1386883997}[状态错误]{style="font-family:宋体"}

[[PKCS#7 develope: Failed to get failure information from reply]{lang="EN-US"}]{#struct_0_x1261_x1417_x2112518390}

[[从回应中获取失败信息失败]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x2112452854}

[[The local cert is]{lang="EN-US"}]{#struct_0_x1261_x1417_x2113042681}

[[:*local-cert*]{lang="EN-US"}]{#struct_0_x1261_x1417_x2112977145}

[[本地证书的内容为：]{style="font-family:宋体"}*[local-cert]{lang="EN-US"}*]{#struct_0_x1261_x1417_x2093642177}

[[Saved the local certificate to the device successfully.]{lang="EN-US"}]{#struct_0_x1261_x1417_x2112911609}

[[保存本地证书到设备成功]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x2112846073}

[[The peer certificate has passed verification, and is being saved to the device\...]{lang="EN-US"}]{#struct_0_x1261_x1417_x2113304825}

[[验证对端证书成功，保存对端证书]{style="font-family:宋体"}]{#struct_0_x1261_x1417_810830084}

[[The local certificate has passed verification, and is being saved to the device\...]{lang="EN-US"}]{#struct_0_x1261_x1417_x2113239289}

[[验证本地证书成功，保存本地证书]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x2113173753}

[[ ]{lang="EN-US"}]{#_Toc130718929}

[[表1-4 ]{lang="EN-US"}[debugging pki verify]{lang="EN-US"}]{#struct_0_x1261_x1417_x1449035842}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1606182007}[[字段]{style="font-family:黑体;
   color:black"}]{#struct_0_x1261_x1417_2143667303}

[[描述]{style="font-family:黑体;color:black"}]{#struct_0_x1261_x1417_542240912}

[[Failed to get the CA certificate chain.]{lang="EN-US"}]{#struct_0_x1261_x1417_x2113108217}

[[获取]{style="font-family:宋体"}[CA ]{lang="EN-US"}]{#struct_0_x1261_x1417_179199944}[证书链失败]{style="font-family:宋体"}

[[Failed to verify local certificates. Verification result: *result-string*]{lang="EN-US"}]{#struct_0_x1261_x1417_x379044330}

[[验证本地证书失败。验证结果为]{style="font-family:宋体"}*[result-string]{lang="EN-US"}*]{#struct_0_x1261_x1417_2122372104}

[[The local public key and the public key in the received certificate did not match.]{lang="EN-US"}]{#struct_0_x1261_x1417_x1574236174}

[[从本地设备上的公钥和接收到的证书中得到的公钥不匹配]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x365159825}

[[The local public key and the public key in the received certificate matched.]{lang="EN-US"}]{#struct_0_x1261_x1417_x2112518393}

[[从本地设备上的公钥和接收到的证书中得到的公钥匹配]{style="font-family:宋体"}]{#struct_0_x1261_x1417_x1939457559}

[[Got the CA certificate chain successfully.]{lang="EN-US"}]{#struct_0_x1261_x1417_x204622778}

[[获取]{style="font-family:宋体"}[CA]{lang="EN-US"}]{#struct_0_x1261_x1417_1409353839}[证书链成功]{style="font-family:宋体"}

[[Verified peer certificates successfully. Saving the peer certificates to the device\...]{lang="EN-US"}]{#struct_0_x1261_x1417_161132405}

[[验证]{style="font-family:宋体"}[PEER]{lang="EN-US"}]{#struct_0_x1261_x1417_x2112452857}[证书成功。正在进行存储证书]{style="font-family:宋体"}[...]{lang="EN-US"}

[[Failed to verify the peer certificates. Verification result: *result-string*]{lang="EN-US"}]{#struct_0_x1261_x1417_x1516295108}

[[验证]{style="font-family:宋体"}[PEER]{lang="EN-US"}]{#struct_0_x1261_x1417_x184273680}[证书失败。验证结果为]{style="font-family:宋体"}*[result-string]{lang="EN-US"}*

[[Failed to verify the CA/RA certificate chain, Verification result: *result-string*]{lang="EN-US"}]{#struct_0_x1261_x1417_x22687835}

[[验证]{style="font-family:宋体"}[CA/RA]{lang="EN-US"}]{#struct_0_x1261_x1417_x1390238033}[证书链失败。验证结果为]{style="font-family:宋体"}*[result-string]{lang="EN-US"}*

[[Verified the CA/RA certificate chain successfully. Saving the CA/RA certificate chain to the device\...]{lang="EN-US"}]{#struct_0_x1261_x1417_x2113042680}

[[CA/RA]{lang="EN-US"}]{#struct_0_x1261_x1417_x963393857}[链验证成功。开始保存]{style="font-family:宋体"}[CA/RA]{lang="EN-US"}[证书链]{style="font-family:宋体"}

[[The peer certificate has passed verification, and is being saved to the device\...]{lang="EN-US"}]{#struct_0_x1261_x1417_x1967948103}

[[验证对端证书成功，保存对端证书]{style="font-family:宋体"}]{#struct_0_x1261_x1417_1000327504}

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging pki request verbose]{lang="EN-US"}]{#struct_0_x1261_x1417_621183454}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1609201176}[[字段]{style="font-family:黑体;
   color:black"}]{#struct_0_x1261_x1417_625392400}

[[描述]{style="font-family:黑体;color:black"}]{#struct_0_x1261_x1417_x2112977144}

[[SCEP request messages: *string*]{lang="EN-US"}]{#struct_0_x1261_x1417_635241178}

[[SCEP]{lang="EN-US"}]{#struct_0_x1261_x1417_x668757387}[申请消息的内容为]{style="font-family:宋体"}*[string]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[debugging pki retrieve verbose]{lang="EN-US"}]{#struct_0_x1261_x1417_x828747349}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1610196635}[[字段]{style="font-family:黑体;
   color:black"}]{#struct_0_x1261_x1417_289377500}

[[描述]{style="font-family:黑体;color:black"}]{#struct_0_x1261_x1417_154053086}

[[SCEP request messages: *string*]{lang="EN-US"}]{#struct_0_x1261_x1417_x2112911608}

[[SCEP]{lang="EN-US"}]{#struct_0_x1261_x1417_x963614173}[申请消息的内容为]{style="font-family:宋体"}*[string]{lang="EN-US"}*

[ ]{lang="PT-BR"}

[[表1-7 ]{lang="PT-BR"}[debugging pki access-control-policy]{lang="EN-US"}]{#struct_0_x1261_x1417_x65932301}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1607169229}[[字段]{style="font-family:黑体;
   color:black"}]{#struct_0_x1261_x1417_x1939434379}

[[描述]{style="font-family:黑体;color:black"}]{#struct_0_x1261_x1417_953011734}

[[PKI_Certificate_ACP : No rule exists in access control policy *policy-name*. The certificate is trusted.]{lang="EN-US"}]{#struct_0_x1261_x1417_x2112846072}

[[访问控制策略]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*]{#struct_0_x1261_x1417_x1607082686}[中没有配置任何规则。证书可被信任]{style="font-family:宋体"}

[[PKI_Certificate_ACP : Access control policy *policy-name* doesn't exist. The certificate is trusted.]{lang="EN-US"}]{#struct_0_x1261_x1417_x2001868}

[[访问控制策略]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*]{#struct_0_x1261_x1417_x1319306280}[不存在。证书可被信任]{style="font-family:宋体"}

[[PKI_Certificate_ACP : Matched rule *number*, which has the action deny, in access control policy *policy-name*. The certificate is untrusted.]{lang="EN-US"}]{#struct_0_x1261_x1417_x659048889}

[[与访问控制策略]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*]{#struct_0_x1261_x1417_x450259340}[中的一个规则匹配，该规则]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[number]{lang="EN-US"}*[，检测动作为]{style="font-family:宋体"}[deny]{lang="EN-US"}[。证书不可信]{style="font-family:宋体"}

[[PKI_Certificate_ACP : Matched rule *number*, which has the action permit, in access control policy *policy-name*. The certificate is trusted.]{lang="EN-US"}]{#struct_0_x1261_x1417_x2113304824}

[[与访问控制策略]{style="font-family:宋体"}*[strpolicy-nameing]{lang="EN-US"}*]{#struct_0_x1261_x1417_x1918053271}[中的一个规则匹配，该规则]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[number]{lang="EN-US"}*[，检测动作为]{style="font-family:宋体"}[permit]{lang="EN-US"}[。证书可被信任]{style="font-family:宋体"}

[[PKI_Certificate_ACP : Do not match rule *number* in access control policy *policy-name*. Checking the next rule.]{lang="EN-US"}]{#struct_0_x1261_x1417_x798617710}

[[与访问控制策略]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*]{#struct_0_x1261_x1417_x599614718}[中规则号为]{style="font-family:宋体"}*[number]{lang="EN-US"}*[的规则不匹配。检查下一个规则]{style="font-family:宋体"}

[[PKI_Certificate_ACP : Certificate doesn\'t match any rule in access control policy *policy-name*. The certificate is untrusted.]{lang="EN-US"}]{#struct_0_x1261_x1417_306706643}

[[与访问控制策略]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*]{#struct_0_x1261_x1417_x2113239288}[中所有规则都不匹配。证书不可信]{style="font-family:宋体"}

[[PKI_Certificate_ACP : Content of the attribute group *group-name* is NULL. Rule *number* matched.]{lang="EN-US"}]{#struct_0_x1261_x1417_412965494}

[[编号为]{style="font-family:宋体"}*[number]{lang="EN-US"}*]{#struct_0_x1261_x1417_x2000990925}[的规则中指定的属性组]{style="font-family:宋体"}*[group-name]{lang="EN-US"}*[的内容为空，所以认为此规则匹配]{style="font-family:宋体"}

[[PKI_Certificate_ACP : Attribute group *group-name* doesn't exist. Rule *number* matched.]{lang="EN-US"}]{#struct_0_x1261_x1417_1649258088}

[[规则号为]{style="font-family:宋体"}[number]{lang="EN-US"}]{#struct_0_x1261_x1417_1009445095}[所对应的属性组]{style="font-family:宋体"}[ group-name]{lang="EN-US"}[不存在，所以认为此规则匹配]{style="font-family:宋体"}

[[PKI_Certificate_ACP : Doesn't match the attribute *attr-id* in attribute group *group-name*.]{lang="EN-US"}]{#struct_0_x1261_x1417_x2113173752}

[[与证书属性组]{style="font-family:宋体"}*[group-name]{lang="EN-US"}*]{#struct_0_x1261_x1417_1279847513}[中属性号为]{style="font-family:宋体"}*[attr-id]{lang="EN-US"}*[的属性不匹配]{style="font-family:宋体"}

[[PKI_Certificate_ACP : Matches the attribute *number* in attribute group *group-name*. Checking the next attribute.]{lang="EN-US"}]{#struct_0_x1261_x1417_x398165243}

[[与证书属性组]{style="font-family:宋体"}*[group-name]{lang="EN-US"}*]{#struct_0_x1261_x1417_x714701969}[中属性号为]{style="font-family:宋体"}*[attr-id]{lang="EN-US"}*[的属性匹配。继续检查下一个属性]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1261_x1417_x1262920154}

[[\# ]{lang="EN-US"}]{#struct_0_x1261_x1417_x2113108216}[打开]{style="font-family:宋体"}[PKI]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging pki error]{lang="EN-US"}]{#struct_0_x1261_x1417_1745283885}

[\<Sysname\> system-view]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1261_x1417_x374681740}[申请本地证书。]{style="font-family:宋体"}

[[\[Sysname\] pki request-certificate domain 1 password 123]{lang="EN-US"}]{#struct_0_x1261_x1417_69373482}

[Start to request general certificate \...]{lang="EN-US"}

[\[Sysname\]]{lang="EN-US"}

[\*Sep 19 16:44:54:539 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; PKCS#7 develope: Wrong PKI]{lang="EN-US"}

[ status.]{lang="EN-US"}

[*[// PKI]{lang="EN-US"}*]{#struct_0_x1261_x1417_1643555150}*[状态错误]{style="font-family:宋体"}*

[[\*Sep 19 16:44:54:540 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; PKCS#7 develope: Error rea]{lang="EN-US"}]{#struct_0_x1261_x1417_1879696732}

[son: Transaction not permitted or supported.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1261_x1417_x2112518392}*[解析回应报文失败，原因为交互不允许或不支持]{style="font-family:宋体"}*

[[\*Sep 19 16:44:54:540 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; SCEP: Failed to get local]{lang="EN-US"}]{#struct_0_x1261_x1417_789425796}

[certificate.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1261_x1417_x711347322}*[获取本地证书失败]{style="font-family:宋体"}*

[[\*Sep 19 16:44:54:541 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; Failed to request certific]{lang="EN-US"}]{#struct_0_x1261_x1417_1668564724}

[ate.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1261_x1417_x1183701610}*[申请证书失败]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1261_x1417_x1442273581}[打开]{style="font-family:宋体"}[PKI]{lang="EN-US"}[证书申请调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging pki request]{lang="EN-US"}]{#struct_0_x1261_x1417_x2112452856}

[\<Sysname\> system-view]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1261_x1417_1212588247}[申请本地证书。]{style="font-family:宋体"}

[[\[Sysname\] pki request-certificate domain 1 password 123]{lang="EN-US"}]{#struct_0_x1261_x1417_1605151062}

[Start to request general certificate \...]{lang="EN-US"}

[[\[Sysname\]]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x1261_x1417_x1213687701}

[[\*Sep 19 16:53:38:808 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; Got the CA/RA certificates]{lang="EN-US"}]{#struct_0_x1261_x1417_x171214804}

[ successfully.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1261_x1417_1275909193}*[获取]{style="font-family:宋体"}[CA/RA]{lang="EN-US"}[证书成功]{style="font-family:宋体"}*

[[\*Sep 19 16:53:38:816 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; Create the PKCS#10 request]{lang="EN-US"}]{#struct_0_x1261_x1417_x40363402}

[ successfully.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1261_x1417_x1753824242}*[建立]{style="font-family:宋体"}[PKCS#10]{lang="EN-US"}[申请成功]{style="font-family:宋体"}*

[[\*Sep 19 16:53:38:827 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; Enrolling the local certif]{lang="EN-US"}]{#struct_0_x1261_x1417_x2113042683}

[icate,please wait a while\...\...]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1261_x1417_602690084}*[正在申请本地证书，请稍候]{style="font-family:宋体"}*

[[\*Sep 19 16:53:38:828 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; SCEP: Host: 192.168.149.1]{lang="EN-US"}]{#struct_0_x1261_x1417_x1556932858}

[Port: 446]{lang="EN-US"}

[Path: 5718d094f90fe26e27351161fd679ad8f91464fe.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1261_x1417_x97672330}*[解析]{style="font-family:宋体"}[URL]{lang="EN-US"}[的具体信息：主机地址为]{style="font-family:宋体"}[192.168.149.1]{lang="EN-US"}[；端口号为]{style="font-family:宋体"}[446]{lang="EN-US"}[；路径为]{style="font-family:宋体"}[5718d094f90fe26e27351161fd679ad8f91464fe]{lang="EN-US"}*

[[\*Sep 19 16:53:38:829 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; PKCS#7 envelope: Encrypted]{lang="EN-US"}]{#struct_0_x1261_x1417_x2132052163}

[ payload successfully.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1261_x1417_1244813783}*[加密载荷成功]{style="font-family:宋体"}*

[[\*Sep 19 16:53:38:837 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; Start enroll certificate p]{lang="EN-US"}]{#struct_0_x1261_x1417_x2112977147}

[rocess successfully.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1261_x1417_1038525705}*[启动申请证书程序成功]{style="font-family:宋体"}*

[[\*Sep 19 16:53:38:840 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; SCEP request message :GET]{lang="EN-US"}]{#struct_0_x1261_x1417_x1989358223}

[/5718d094f90fe26e27351161fd679ad8f91464fe/pkiclient.exe?operation=PKIOperation&m]{lang="EN-US"}

[essage=MIIGSwYJKoZIhvcNAQcCoIIGPDCCBjgCAQExDjAMBggqhkiG9w0CBQUAMIICxwYJKoZIhvcNA]{lang="EN-US"}

[QcBoIICuASCArQwggKwBgkqhkiG9w0BBwOgggKhMIICnQIBADGB6TCB5gIBADBPMDsxCzAJBgNVBAYTA]{lang="EN-US"}

[mNuMQwwCgYDVQQKEwNoM2MxDzANBgNVBAsTBmgzYy14eDENMAsGA1UEAxMEODA4OAIQQjLIoORHV7bxu]{lang="EN-US"}

[yVpDyjDlTANBgkqhkiG9w0BAQEFAASBgFt3zrqqwqduF5xfOZ9AeNQQwih43F0TZLBvFCvIHwF5zeycq]{lang="EN-US"}

[ECwFzTcjuNlIJ4P2nStP3zVlDlT2jX0Qd2kmUs6wtFgTYonPr3xhTqwy8GY0c3ZKufC65VF2piHqSd0i]{lang="EN-US"}

[jVLR3g4S8EyC163o6o%2BgJDERtr11rBg6q%2BG3917I%2Bb0MIIBqgYJKoZIhvcNAQcBMBEGBSsOAwI]{lang="EN-US"}

[HBAj6ZDq1SIbocICCAYhLNeNVM%2Bnq5dHJYXu0VbVpxsMoZS40lJRNrXP3eWOdJac%2BKRpLiWR4IDb]{lang="EN-US"}

[5dQLE39k6YrgyFP4viMFvM%2BOUZjIbEvpXSrkqsdT8ljuUPhexfwA5oDpkmkT6sSbRbp/cVf4s2rFFw]{lang="EN-US"}

[SVH9an3ZaKlQVo/CUhUPZV8eJYTRe5yD/Zzu4LvjLATap5BzDAL%2BtYByabTm1MyjwNt5syPfqFsZR0]{lang="EN-US"}

[q586MFMty1eMpE4E8Inu/MKi78W5cAbntUcperA8yhphC8iRzQosBWnYszzjer42HO/8rkuZjVATR2Z5]{lang="EN-US"}

[rgjQXp6wDPuLzEEuDOvSMsy9bjEsPQcXCkKH5qNoeq9QTRiP4Qaa/3uC8qGb2Nb]{lang="EN-US"}

[*[// SCEP]{lang="EN-US"}*]{#struct_0_x1261_x1417_x1675560795}*[申请信息的内容]{style="font-family:宋体"}*

[[\*Sep 19 16:53:38:968 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; Reply type: 5.]{lang="EN-US"}]{#struct_0_x1261_x1417_888172605}

[*[// ]{lang="EN-US"}*]{#struct_0_x1261_x1417_x2112911611}*[应答消息返回类型为]{style="font-family:宋体"}[5]{lang="EN-US"}*

[[\*Sep 19 16:53:38:979 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; SCEP: De-encapsulated PKCS]{lang="EN-US"}]{#struct_0_x1261_x1417_246304944}

[#7 packet successfully.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1261_x1417_x1778247918}*[解封装]{style="font-family:宋体"}[PKCS#7]{lang="EN-US"}[格式的数据包成功]{style="font-family:宋体"}*

[[\*Sep 19 16:53:38:979 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; Reply message status 0.]{lang="EN-US"}]{#struct_0_x1261_x1417_1804453722}

[*[// ]{lang="EN-US"}*]{#struct_0_x1261_x1417_475508429}*[返回信息状态值为]{style="font-family:宋体"}[0]{lang="EN-US"}*

[[\*Sep 19 16:53:38:980 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; 2 certificates in reply me]{lang="EN-US"}]{#struct_0_x1261_x1417_x1053672024}

[ssage.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1261_x1417_x1166007318}*[回应报文中携带两个证书]{style="font-family:宋体"}*

[[\*Sep 19 16:53:38:980 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; The local cert is]{lang="EN-US"}]{#struct_0_x1261_x1417_x2112846075}

[:Certificate:]{lang="EN-US"}

[    Data:]{lang="EN-US"}

[        Version: 3 (0x2)]{lang="EN-US"}

[        Serial Number:]{lang="EN-US"}

[            59:96:1e:b6:ad:b5:19:59:97:47:51:ff:ad:b8:3b:70]{lang="EN-US"}

[        Signature Algorithm: sha1WithRSAEncryption]{lang="EN-US"}

[        Issuer: C=cn, O=h3c, OU=h3c-xx, CN=8088]{lang="EN-US"}

[        Validity]{lang="EN-US"}

[            Not Before: Sep 19 02:26:22 2011 GMT]{lang="EN-US"}

[            Not After : Sep 18 02:26:22 2012 GMT]{lang="EN-US"}

[        Subject: CN=cc1]{lang="EN-US"}

[        Subject Public Key Info:]{lang="EN-US"}

[            Public Key Algorithm: rsaEncryption]{lang="EN-US"}

[                Public-Key: (1024 bit)]{lang="EN-US"}

[                Modulus:]{lang="EN-US"}

[                    00:c0:6f:d3:3a:af:1c:7a:7f:a4:8b:41:73:f4:46:]{lang="EN-US"}

[                    e9:b9:c7:b8:5d:f7:36:14:3c:0a:5b:9e:1d:31:7f:]{lang="EN-US"}

[                    fc:44:7f:6b:82:b1:f5:09:1c:8e:39:52:08:51:43:]{lang="EN-US"}

[                    e6:e4:05:a3:39:35:a0:3f:3a:73:5f:e7:a9:fc:9b:]{lang="EN-US"}

[                    a3:40:7d:8a:d7:9f:0d:b0:ba:09:de:4e:52:9f:dd:]{lang="EN-US"}

[                    93:df:8e:77:3e:8a:37:25:b8:82:ec:34:04:53:76:]{lang="EN-US"}

[                    2f:b7:07:a9:88:43:a]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1261_x1417_315231615}*[本地证书的内容]{style="font-family:宋体"}*

[[\*Sep 19 16:53:38:980 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; Enrolled local certificate]{lang="EN-US"}]{#struct_0_x1261_x1417_x2113304827}

[ successfully, begin to verify local certificate.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1261_x1417_x351969330}*[申请本地证书成功，开始验证本地证书]{style="font-family:宋体"}*

[[\*Sep 19 16:53:38:981 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; The local public key and t]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x1261_x1417_595665706}

[[he public key in the received certificate matched.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x1261_x1417_x647109480}

[*[// ]{lang="EN-US"}*]{#struct_0_x1261_x1417_x1925502411}*[本地设备上的公钥和从接收到的证书中得到的公钥不匹配]{style="font-family:宋体"}*

[[\*Sep 19 16:53:38:982 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; Verified the local certifi]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x1261_x1417_762681942}

[[cate successfully. Saving the local certificate to the device\...]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x1261_x1417_x898812718}

[*[// ]{lang="EN-US"}*]{#struct_0_x1261_x1417_950353266}*[验证本地证书成功，存储本地证书到设备中]{style="font-family:宋体"}*

[[\*Sep 19 16:53:38:982 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; Request certificate succes]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x1261_x1417_x2113239291}

[[sfully.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x1261_x1417_1622753539}

[*[// ]{lang="EN-US" style="color:black"}*]{#struct_0_x1261_x1417_188649804}*[证书申请成功]{style="font-family:
宋体;color:black"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1261_x1417_x1321020910}[打开]{style="font-family:宋体"}[PKI]{lang="EN-US"}[获取证书和获取]{style="font-family:宋体"}[CRL]{lang="EN-US"}[调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> debugging pki retrieve]{lang="EN-US"}]{#struct_0_x1261_x1417_x1062156976}

[\<Sysname\> system-view]{lang="EN-US"}

[System View: return to User View with Ctrl+Z.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1261_x1417_1290816096}[获取本地证书。]{style="font-family:宋体"}

[[\[Sysname \] pki retrieve-certificate domain 1 local]{lang="EN-US"}]{#struct_0_x1261_x1417_35930338}

[\[Sysname\]]{lang="EN-US"}

[\*Sep 19 17:28:39:056 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; Verified the local certifi]{lang="EN-US"}

[cate successfully. Saving the local certificate to the device\...]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1261_x1417_x2113173755}*[验证本地证书成功。存储本地证书到设备中]{style="font-family:宋体"}*

[[\*Sep 19 17:28:39:057 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; Saved the local certificat]{lang="EN-US"}]{#struct_0_x1261_x1417_1683132040}

[e to the device successfully.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1261_x1417_1471843872}*[保存本地证书到设备成功]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1261_x1417_1618127007}[打开]{style="font-family:宋体"}[PKI]{lang="EN-US"}[验证证书调试开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging pki verify]{lang="EN-US"}]{#struct_0_x1261_x1417_169507232}

[\<Sysname\> system-view]{lang="EN-US"}

[System View: return to User View with Ctrl+Z.]{lang="EN-US"}

[\[Sysname\] pki request-certificate domain 1 password 123]{lang="EN-US"}

[Start to request general certificate \...]{lang="EN-US"}

[\[Sysname\]]{lang="EN-US"}

[\*Sep 19 17:32:00:800 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; The local public key and t]{lang="EN-US"}

[he public key in the received certificate matched.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1261_x1417_1096970104}*[从本地设备上的公钥和接收到的证书中得到的公钥匹配]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1261_x1417_x2113108219}[打开]{style="font-family:宋体"}[PKI]{lang="EN-US"}[申请证书的详细调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging pki request verbose]{lang="EN-US"}]{#struct_0_x1261_x1417_x271138750}

[\<Sysname\> system-view]{lang="EN-US"}

[System View: return to User View with Ctrl+Z.]{lang="EN-US"}

[\[Sysname\] pki request-certificate domain 1 password 123]{lang="EN-US"}

[Start to request general certificate \...]{lang="EN-US"}

[\[Sysname\]]{lang="EN-US"}

[\*Sep 19 17:37:11:011 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; SCEP request message :GET]{lang="EN-US"}

[/5718d094f90fe26e27351161fd679ad8f91464fe/pkiclient.exe?operation=PKIOperation&m]{lang="EN-US"}

[essage=MIIGSwYJKoZIhvcNAQcCoIIGPDCCBjgCAQExDjAMBggqhkiG9w0CBQUAMIICxwYJKoZIhvcNA]{lang="EN-US"}

[QcBoIICuASCArQwggKwBgkqhkiG9w0BBwOgggKhMIICnQIBADGB6TCB5gIBADBPMDsxCzAJBgNVBAYTA]{lang="EN-US"}

[mNuMQwwCgYDVQQKEwNoM2MxDzANBgNVBAsTBmgzYy14eDENMAsGA1UEAxMEODA4OAIQQjLIoORHV7bxu]{lang="EN-US"}

[yVpDyjDlTANBgkqhkiG9w0BAQEFAASBgKpNtHOhfgKsndpXacK4EDU4PShRdEaeB5g%2Bw8PoGAKuQtd]{lang="EN-US"}

[M/YPSmJHn9W108BJGZRG8f2Ud3iljbEbSja4wPW6pyNmrEROVCovQJjeX1bJC6hYZiMImK3q35DFqbBb]{lang="EN-US"}

[HvJC9qvLMhvRISyAGw5MdbVF4vJLQAKILsisQC39NbTh9MIIBqgYJKoZIhvcNAQcBMBEGBSsOAwIHBAi]{lang="EN-US"}

[eWep9foXYjYCCAYjPKpA9TWA7c6gTV/0FdKkWAd3vuk7I5OXOPLMaePcOdoEXMdAURwb3RgYiq2OTUaC]{lang="EN-US"}

[ajj/JYG6H4ikHL%2B9txs97A7I3LybCvNOW9%2BKZ1AIg9O/XCCBWQYxaSn0bI1%2BlelBWwv1CxFUbU]{lang="EN-US"}

[m/MVHipJF4ygeHpqVjGjNNQVHxoR5Q9b%2BVXw/9Jvvg4dG6ywngWxpQvj1pHlspIx38haQ4Rw8esksh]{lang="EN-US"}

[5VBrzMDCVlYcpHsvNryeI8aS0jx13CF7VsnwPDBBSNun62mWSk6dCdDiN3XUXFNTLnYWVm3EnKJzwf0Ll]{lang="EN-US"}

[3xqeLP%2BjQEWENenrhaIQyJUcmTgyoLfmQ6BmEhI1KGRSwZcccW3wAQf0XXT1p]{lang="EN-US"}

[*[// SCEP]{lang="EN-US"}*]{#struct_0_x1261_x1417_1772838177}*[申请信息的内容]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1261_x1417_x2112518395}[打开]{style="font-family:宋体"}[PKI]{lang="EN-US"}[获取证书的详细调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging pki retrieve verbose]{lang="EN-US"}]{#struct_0_x1261_x1417_x1132888505}

[\<Sysname\> system-view]{lang="EN-US"}

[System View: return to User View with Ctrl+Z.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1261_x1417_377129102}[申请本地证书。]{style="font-family:宋体"}

[[\[Sysname\] pki request-certificate domain 1 password 123]{lang="EN-US"}]{#struct_0_x1261_x1417_x2112452859}

[Start to request general certificate \...]{lang="EN-US"}

[\[Sysname\]]{lang="EN-US"}

[\*Sep 19 17:37:11:011 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; SCEP request message :GET]{lang="EN-US"}

[/5718d094f90fe26e27351161fd679ad8f91464fe/pkiclient.exe?operation=PKIOperation&m]{lang="EN-US"}

[essage=MIIGSwYJKoZIhvcNAQcCoIIGPDCCBjgCAQExDjAMBggqhkiG9w0CBQUAMIICxwYJKoZIhvcNA]{lang="EN-US"}

[QcBoIICuASCArQwggKwBgkqhkiG9w0BBwOgggKhMIICnQIBADGB6TCB5gIBADBPMDsxCzAJBgNVBAYTA]{lang="EN-US"}

[mNuMQwwCgYDVQQKEwNoM2MxDzANBgNVBAsTBmgzYy14eDENMAsGA1UEAxMEODA4OAIQQjLIoORHV7bxu]{lang="EN-US"}

[yVpDyjDlTANBgkqhkiG9w0BAQEFAASBgKpNtHOhfgKsndpXacK4EDU4PShRdEaeB5g%2Bw8PoGAKuQtd]{lang="EN-US"}

[M/YPSmJHn9W108BJGZRG8f2Ud3iljbEbSja4wPW6pyNmrEROVCovQJjeX1bJC6hYZiMImK3q35DFqbBb]{lang="EN-US"}

[HvJC9qvLMhvRISyAGw5MdbVF4vJLQAKILsisQC39NbTh9MIIBqgYJKoZIhvcNAQcBMBEGBSsOAwIHBAi]{lang="EN-US"}

[eWep9foXYjYCCAYjPKpA9TWA7c6gTV/0FdKkWAd3vuk7I5OXOPLMaePcOdoEXMdAURwb3RgYiq2OTUaC]{lang="EN-US"}

[ajj/JYG6H4ikHL%2B9txs97A7I3LybCvNOW9%2BKZ1AIg9O/XCCBWQYxaSn0bI1%2BlelBWwv1CxFUbU]{lang="EN-US"}

[m/MVHipJF4ygeHpqVjGjNNQVHxoR5Q9b%2BVXw/9Jvvg4dG6ywngWxpQvj1pHlspIx38haQ4Rw8esksh]{lang="EN-US"}

[5VBrzMDCVlYcpHsvNryeI8aS0jx13CF7VsnwPDBBSNun62mWSk6dCdDiN3XUXFNTLnYWVm3EnKJzwf0Ll]{lang="EN-US"}

[3xqeLP%2BjQEWENenrhaIQyJUcmTgyoLfmQ6BmEhI1KGRSwZcccW3wAQf0XXT1p]{lang="EN-US"}

[*[// SCEP]{lang="EN-US"}*]{#struct_0_x1261_x1417_x1065956414}*[申请信息的内容]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1261_x1417_x1859046362}[打开]{style="font-family:宋体"}[PKI]{lang="EN-US"}[证书访问控制策略的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging pki access-control-policy]{lang="EN-US"}]{#struct_0_x1261_x1417_1653093776}

[\<Sysname\> system-view]{lang="EN-US"}

[System View: return to User View with Ctrl+Z.]{lang="EN-US"}

[\[Sysname\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1261_x1417_x753219770}[在一台支持]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[的设备上配置证书属性的访问控制策略，]{style="font-family:宋体"}[IE]{lang="EN-US"}[浏览器采用]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[的方式登录设备。]{style="font-family:宋体"}

[[\[Sysname\]]{lang="EN-US"}]{#struct_0_x1261_x1417_567288350}

[\*Sep 20 13:11:36:358 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; PKI_Certificate_ACP: Doesn]{lang="EN-US"}

[\'t match the attribute 1 in attribute group \'1\'.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1261_x1417_x261449931}*[与证书属性组]{style="font-family:宋体"}[1]{lang="EN-US"}[中属性号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的属性不匹配]{style="font-family:宋体"}*

[[\*Sep 20 13:11:36:358 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; PKI_Certificate_ACP: Do no]{lang="EN-US"}]{#struct_0_x1261_x1417_x2113042682}

[t match rule 1 in access control policy \'abc\'. Checking the next rule.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1261_x1417_x2126193271}*[与访问控制策略]{style="font-family:宋体"}[abc]{lang="EN-US"}[中规则号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的规则不匹配。检查下一个规则]{style="font-family:宋体"}*

[[\*Sep 20 13:11:36:358 2011 Sysname PKI/7/PKI_DEBUG: -MDC=1; PKI_Certificate_ACP: Certi]{lang="EN-US"}]{#struct_0_x1261_x1417_x1256746640}

[ficate doesn\'t match any rule in access control policy \'abc\'. The certificate is]{lang="EN-US"}

[ untrusted.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1261_x1417_1967522364}*[与访问控制策略]{style="font-family:宋体"}[abc]{lang="EN-US"}[中所有规则都不匹配，证书不可信]{style="font-family:宋体"}*

[ ]{lang="EN-US"}
