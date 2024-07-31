import smtplib
from email.message import EmailMessage

def sendmail(to, subject='It is test API mail', body='It is successful'):
    print("Starting email send process...")
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    print("Connected to the SMTP server.")

    server.login('abdullahabeeb9786@gmail.com', 'adjr mjwz kdca eoby')
    print("Logged in to the SMTP server.")

    msg = EmailMessage()
    msg['From'] = 'abdullahabeeb9786@gmail.com'
    msg['To'] = to
    msg['Subject'] = subject
    msg.set_content(body)

    server.send_message(msg)
    print("Email sent successfully.")
    server.quit()
    print("Connection closed.")

# Example usage
sendmail('20211a1281@bvrit.ac.in')