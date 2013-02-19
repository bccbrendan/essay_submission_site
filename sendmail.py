# sendmail.py
# email stacia's work email from a student
import smtplib

student_gmail = 'mslongenglishiistudent@gmail.com'
student_pw    = 'studentpassword'
teacher_gmail = 'mslongenglishii@gmail.com'

def sendmail ( subject, body ):
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.ehlo()
    session.starttls()
    session.ehlo()
    session.login( student_gmail, student_pw )
    headers = ["from: " + student_gmail,
           "subject: " + subject,
           "to: " + teacher_gmail,
           "mime-version: 1.0",
           "content-type: text/html"]
    headers = "\r\n".join(headers)
    session.sendmail(student_gmail, teacher_gmail, headers + "\r\n\r\n" + body)
    session.quit()
