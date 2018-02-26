#!/usr/bin/env python3
# -*-encoding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def mail():
    ret = True
    try:
        msg = MIMEText(mail_context,'plain','utf-8')
        msg['From'] = formataddr(['发件人昵称',my_sender])
        msg['To'] = recv_user
        msg['Cc'] = cc_user
        msg['Subject'] = mail_subject

        server = smtplib.SMTP(smtp_server,smtp_server_port)
        server.login(my_sender,my_pass)
        server.sendmail(my_sender,recv_user.split(',')+cc_user.split(','),msg.as_string())
        server.quit()
    except Exception:
        ret = False
    return ret

if __name__ == '__main__':
    smtp_server = 'smtp.126.com'
    smtp_server_port = 25
    my_sender = 'abc@126.com'   #发件人邮箱
    my_pass = 'xxooxxoo'    #发件人邮箱密码
    recv_user = 'a@b.com,c@d.com,'   #收件人
    cc_user = 'e@f.com,g@j.com,'

    mail_subject = '邮箱主题写在这里'    #邮箱主题

    mail_context = '''
这是一个段落
有没有换行？
This is a test page.
haha
How are you?
How old are you?
    '''    #邮箱内容

    ret = mail()
    if ret:
        print('邮件发送成功')
    else:
        print('邮件发送失败')
