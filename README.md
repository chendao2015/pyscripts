# log.py
### 作用：检查日志文件中是否有指定的关键字
#### 第一个参数为日志文件名（必须有，相对路径、绝对路径均可）
#### 第二个参数为seek position文件的路径（可选项，若不设置则默认为/tmp/logseek文件。相对路径、绝对路径均可）
#### 第三个参数为搜索关键字，默认为 Error


# mail_send.py
### 作用：发送邮件，可在其他python程序中调用此模块
#### 第一个参数为smtp服务器的地址（必须有，可为本机亦可为其它pop3服务器）
#### 第二个参数为发件人邮箱用户名（必须有）
#### 第三个参数为发件人邮箱密码（必须有）
#### 第四个参数为邮件主题（必须有）
#### 第五个参数为邮件内容（必须有）
#### 第六个参数为收件人列表（必须有，此列表必须是字符串，多个收件人之间用逗号隔开。例如：'a@b.com, c@d.com, e@f.com'）
#### 第七个参数为抄送人列表（可选项，可为空。若不提供此参数则不能修改第八个参数的端口号。）
#### 第八个参数为smtp服务器发送邮件的端口（可选项，默认为25。）
