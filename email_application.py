from email.mime.text import MIMEText
import smtplib


#email body
msg = MIMEText("testing my email application...")
msg['Subject']='TEST python EMAIL application'
msg['From']='sender_id@example.com'
msg['To']='reciever_id@example.com'



#email envelop
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('sender_id@example.com', 'password')
s.sendmail('sender_id@example.com','reciever_id@example.com',msg.as_string())

print("message sent")
