import smtplib
from email.mime.text import MIMEText            #MIMRText()定义邮件正文
from email.mime.multipart import MIMEMultipart  #MIMEMulipart模块构造带附件
import os

def send_email():
    # 发送邮箱服务器
    smtpserver = 'smtp.163.com'

    # 发送邮箱用户/密码(登录邮箱操作)
    user = "xxkxydj@163.com"
    password = "wulian123"

    # 发送邮箱
    sender = "xxkxydj@163.com"

    # 接收邮箱
    receiver = "xiuke.xu@wuliangroup.com"

    # 发送主题
    subject = '物联mqtt通信自动化测试报告'

    # 发送附件
    lists = os.listdir(os.getcwd())                                    #列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn:os.path.getmtime(os.getcwd() + "\\" + fn))#按时间排序
    file_new = os.path.join(os.getcwd(),lists[-1])                     #获取最新的文件保存到file_new
    # print(file_new)
    # print(file_result)

    sendfile = open(file_new, "rb").read()

    att = MIMEText(sendfile,'plain', "utf-8")   # "base64",
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = "attachment;filename = result.html"

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = subject
    msgRoot.attach(att)
    msgRoot['From'] = 'xxkxydj@163.com'
    msgRoot['To'] = ",".join(["yangyi.gu@wuliangroup.com", "fangwen.fu@wuliangroup.com","jiandong.qiu@wuliangroup.com"])
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()

# send_email()