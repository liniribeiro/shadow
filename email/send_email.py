import smtplib

from files import SMTP_PASS, SMTP_LOGIN, GOOGLE_SMTP, GOOGLE_SMTP_PORT

server = smtplib.SMTP_SSL(GOOGLE_SMTP, GOOGLE_SMTP_PORT)
server.login(SMTP_LOGIN, SMTP_PASS)
email_from = SMTP_LOGIN,
email_to = SMTP_LOGIN,
subject = "Sua exportação de arquivos está pronta!"
text = "Em anexo você encontra a solicitação de exportação do arquivo, realizada dis xxxxxxx hora xxxxx."

message = 'Subject: {}\n\n{}'.format(subject, text)
server.sendmail(email_from, email_to, message)
server.quit()
