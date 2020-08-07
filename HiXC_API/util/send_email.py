# coding:utf-8
import smtplib
from email.mime.text import MIMEText


class SendEmail:
    def send_mail(self, user_list, sub, content):
        email_host = "smtp.163.com"#邮箱服务器的地址
        send_user = "自己的邮箱"
        password = "自己的密码"
        user = "nian0099" + "<" + send_user + ">"
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)
        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user, password)
        server.sendmail(user, user_list, message.as_string())
        server.close()

    def send_main(self, pass_list, fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num + fail_num
        # 90%
        pass_result = "%.2f%%" % (pass_num / count_num * 100)
        fail_result = "%.2f%%" % (fail_num / count_num * 100)

        user_list = ['nian110nian@qq.com']
        sub = "接口自动化报告"
        content = "此次一共运行接口个数为%s个，通过个数为%s个，失败个数为%s,通过率为%s,失败率为%s" % (
            count_num, pass_num, fail_num, pass_result, fail_result)
        self.send_mail(user_list, sub, content)


if __name__ == '__main__':
    sen = SendEmail()
