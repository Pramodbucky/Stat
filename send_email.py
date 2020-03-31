from config import *
import smtplib
'''port for SMTP = 587 and SMTP_SSL = 465'''
def send_email(text):
    conn = smtplib.SMTP('smtp.outlook.com', 587)    # connection process
    conn.ehlo()
    conn.starttls()    # start connection
    conn.login(useremail, userpassword)
    message = text
    body = 'SUBJECT: Corona Stat \n\n Hi there, \n\n\n' + message + '\n\n Pramod'
    conn.sendmail(sender, receiver, body)
    conn.quit()

