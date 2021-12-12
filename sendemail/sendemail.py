import configparser
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import logging
import sys

# 配置日志信息 输出到控制台
logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                stream=sys.stdout)

def getConf():
    config = configparser.ConfigParser()
    config.read('sendemail/local.conf')
    return config

def sendEmail(mail_msg,subject):
    
    config = getConf()
    strFrom = config.get("email", "sender")
    strTo = config.get("email", "receivers")
    code = config.get("email", "code")

    message = MIMEText(mail_msg, 'html', 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    message['To'] = strTo;
    message['From'] = strFrom;

    #ssl登录
    smtp = smtplib.SMTP_SSL('smtp.qq.com')
    smtp.connect('smtp.qq.com')
    smtp.login(strFrom, code)

    try:
        smtp.sendmail(strFrom,strTo,message.as_string())
    finally:
        smtp.close

def getContext():
    mail_msg = """
    <ul type='circle'>
    <li>hello python3</li>
    </ul>
    """
    subject = '测试基于python3的QQ邮件发送功能'
    return mail_msg,subject

if __name__ == '__main__':

    logging.info("begin send email")
    mail_msg,subject = getContext()
    sendEmail(mail_msg,subject)
    logging.info("end send email")

    