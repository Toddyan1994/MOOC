from email.header import Header
from email.mime.text import MIMEText
import smtplib

# smtplib 用于邮件的发信动作

# 发信方的信息：发信邮箱，QQ邮箱授权码
from_addr = '2040691005@qq.com'
password = 'bewxbyskdvpigedg'

# 收信方邮箱
to_addrs = ['2040691005@qq.com','249424797@qq.com','yta11801@gmail.com']

# 发信服务器
smtp_server = 'smtp.qq.com'

# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
text = '''这是用python发送的一封邮件
​希望学习Python对你不是一件困难的事情！

人生苦短，我用Python

Best, Todd
May 10, 2020 1:00 AM
'''
msg = MIMEText(text, 'plain', 'utf-8')

# 邮箱开头内容
msg['From'] = Header(from_addr)
msg['To'] = Header(','.join(to_addrs))
msg['Subject'] = Header('python test')

# 开启发信服务，这里使用的是加密传输

server = smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server, 465)

# 登录发信邮箱
server.login(from_addr, password)
# 发送邮件
server.sendmail(from_addr, to_addrs, msg.as_string())
# 关闭服务器
server.quit()
