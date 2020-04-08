import smtplib
from email.message import Message

s = smtplib.SMTP_SSL(host='smtp.mail.ru', port=465)
with open('roma.gol') as f: passwd = f.redline().strip()
s.login("roma.gol12@mail.ru", passwd)

msg = EmailMessage()
msg.set_content("JOJO my live")

msg.add_header('From','roma.gol12@mail.ru')
msg.add_header('To','teodorit.evlampiev@yandex.ru')
msg.add_header('Subject','Test message')

s.send_message(msg)
s.quit()
