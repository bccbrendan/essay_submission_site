# sendmail.py
# email stacia's work email from a student
import smtplib

student_gmail = 'mslongenglishiistudent@gmail.com'
student_pw    = 'studentpassword'

def sendmail ( subject, body, recipient ):
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.ehlo()
    session.starttls()
    session.ehlo()
    session.login( student_gmail, student_pw )
    headers = ["from: " + student_gmail,
           "subject: " + subject,
           "to: " + recipient,
           "mime-version: 1.0",
           "content-type: text/html"]
    headers = "\r\n".join(headers)
    session.sendmail(student_gmail,  recipient, headers + "\r\n\r\n" + body)
    session.quit()
