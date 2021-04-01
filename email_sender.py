import smtplib

to = input("Enter the Email of recipent:\n")
content = input("Enter the content for mail:\n")
def SendEmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('bahubalendra.barik@gmail.com', 'shreenu@143')
    server.sendmail('bahubalendra.barik@gmail.com', to , content)
    server.close()

SendEmail(to , content)