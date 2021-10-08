# 导入smtplib模块，用于发送邮件
import smtplib
# 带多个部分的邮件
from email.mime.multipart import MIMEMultipart
# MIMEText用于在邮件内的放置文本内容
from email.mime.text import MIMEText
# MIMEImage用于在邮件内放置图片附件
from email.mime.image import MIMEImage
# MIMEApplication用于在邮件内放置附件内容
from email.mime.application import MIMEApplication
# Header用于构建邮件头
from email.header import Header

# 指定发件人邮箱
from_addr = 'hbx9610232021@163.com'
# 授权码
password = 'PZKWAOLDSMTPBIJR'
# 指定收件人邮箱，有多少，放多少
to_addrs = ['2431320433@qq.com']
# cc_reciver = ['邮箱3', '邮箱4']
# 指定发送服务器为腾讯邮箱服务器
smtp_server = 'smtp.163.com'
smtplib.SMTP_SSL(host='smtp.163.com').connect(host='smtp.163.com')
# 登录发送邮件的邮箱
server = smtplib.SMTP()
server.connect(smtp_server)
server.login(from_addr, password)
# 创建一个多部分的邮件对象
# 这一步很重要，后面的文本，图片和pdf都是不断添加到msg中的。
msg = MIMEMultipart('alternative')
# 在邮件中加入文本内容
contents = ' '
# plain是字体，utf-8是编码方式
msgtext = MIMEText(contents, 'plain', 'utf-8')
# 将文本内容加载到msg中
msg.attach(msgtext)
# 将一个附件放入邮件中
filepath = r"/python基础/day11/计算器测试报告.html"
filename = "计算器测试报告.html"
with open(filepath, 'rb') as f:
    # 读取pdf文件赋值一个对象
    attachfile = MIMEApplication(f.read())
    # 为对象拓展标题字段和值
attachfile.add_header('Content-Disposition', 'attachment', filename=filename)
# 将pdf添加到msg
msg.attach(attachfile)
# 邮件标题
msg['Subject'] = Header('主题')
# 标明邮件发送人名称
msg['From'] = Header('发件人，似乎定义了没生效')
# 标明收件人
msg['To'] = Header(','.join(to_addrs))
# 定义抄送人
# msg['CC'] = Header(','.join(cc_reciver))
# 指定邮件的发送邮箱，接收邮箱，发送内容
server.sendmail(from_addr, to_addrs, msg.as_string())
# 结束邮件发送，关闭服务器
server.quit()
