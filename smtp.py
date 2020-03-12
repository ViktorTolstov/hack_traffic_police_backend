pwd = "v1343412"
import smtplib

server = smtplib.SMTP('smtp.mail.ru')
server.ehlo()
server.starttls()
server.login("viktor.tolstov.tsu@mail.ru",pwd)

msg = "Test test"
server.sendmail("viktor.tolstov.tsu@mail.ru", "viktor.tolstov.tsu@gmail.com", msg)
server.quit()

# TO = "viktor.tolstov.tsu@mail.ru"