import configparser
from email.header import Header
from email.mime.text import MIMEText
import smtplib


config = configparser.ConfigParser()
config.read('/home/pi/minschantGit/nogit/mail_conf.ini')


# 输入Email地址和口令:
from_addr = config.get('address', 'me')
password = config.get('key', 'me')
# 输入SMTP服务器地址:
smtp_server = 'smtp.qq.com'
# 输入收件人地址:
# to_addr = input('To: ')
to_addr = config.get('address', 'me')
# SMTP协议默认端口是25
server = smtplib.SMTP(smtp_server, 25) 


msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = Header("上海树莓派", 'utf-8')
msg['To'] = Header("树莓派提醒", 'utf-8')
msg['Subject'] = Header("这是一个测试邮件", 'utf-8')

server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
