import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def connect(smtp_server,user,password,smtp_server_port=25):
    server = smtplib.SMTP(smtp_server,smtp_server_port)
    server.login(user,password)
    return server

def send(smtp_server,user,password,subject,context,recv_user='',cc_user='',smtp_server_port=25):
    '''
recv_user argument must be string, comma interval, like 'fuxing.cheng@126.com, a@b.com'
cc_user argument must be string, comma interval, like 'fuxing.cheng@126.com, a@b.com'
    '''
    if not recv_user:
        return 'Error, Please enter a recipient mailbox address.'

    mail_subject = subject
    mail_context = context

    msg = MIMEText(mail_context,'plain','utf-8')
    msg['From'] = formataddr(['发件人昵称',user])
    msg['To'] = recv_user
    msg['Cc'] = cc_user
    msg['Subject'] = mail_subject

    server = connect(smtp_server,user,password)
    if not cc_user:
        server.sendmail(user,recv_user.split(','),msg.as_string())
    else:
        server.sendmail(user,recv_user.split(',')+cc_user.split(','),msg.as_string())
    server.quit()

    return 'Mail delivery success'
