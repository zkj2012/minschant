import configparser
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
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


msg = MIMEMultipart()
msg['From'] = Header("上海树莓派", 'utf-8')
msg['To'] = Header("树莓派提醒", 'utf-8')
msg['Subject'] = Header("这是一个测试邮件", 'utf-8')

# 添加邮件文本
msg.attach(MIMEText('这里是邮件正文', 'plain', 'utf-8'))

# 添加邮件附件，这里是直接从本地读取一个图片
with open('/home/pi/image.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是jpg类型:
    mime = MIMEBase('image', 'jpg', filename='image.jpg')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='image.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

# server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
