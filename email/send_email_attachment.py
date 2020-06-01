
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from files import SMTP_PASS, SMTP_LOGIN, GOOGLE_SMTP, GOOGLE_SMTP_PORT

send_from = SMTP_LOGIN
send_to = SMTP_LOGIN
subject = "Sua exportação de arquivos está pronta!"
text = "Em anexo você encontra a solicitação de exportação do arquivo, realizada dia xxxxxxx hora xxxxx."

file_name = 'contacts.csv'


def get_body() -> MIMEMultipart:
    message = MIMEMultipart()
    message['From'] = f"Admin <{send_from}>"
    message['To'] = send_to
    message['Subject'] = subject
    message.preamble = 'preamble'

    body = MIMEText(text)
    message.attach(body)

    return message


def add_attachment(message: MIMEMultipart) -> MIMEMultipart:
    with open(file_name) as fp:
        record = MIMEText(fp.read())
        record['Content-Disposition'] = 'attachment; filename="test.csv"'
        message.attach(record)
    return message


def send_email(message: MIMEMultipart):
    server = smtplib.SMTP_SSL(GOOGLE_SMTP, GOOGLE_SMTP_PORT)
    server.login(SMTP_LOGIN, SMTP_PASS)
    server.sendmail(send_from, send_to, message.as_string())
    server.quit()


message = get_body()
message = add_attachment(message)
send_email(message)
