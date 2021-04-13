import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = 'type gmail address here'
EMAIL_PASSWORD = 'type gmail password here'

FILE_TITLE = 'type text title here'
FILE_PATHNAME = 'type file pathname here'
RECIPIENT_EMAIL = 'type recipient email here'

line_num = 1

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
	with open(FILE_PATHNAME) as fp:
		line = fp.readline()
		while line:

			msg = EmailMessage()
			msg['Subject'] = FILE_TITLE + ' Line ' + str(line_num)
			msg['From'] = EMAIL_ADDRESS
			msg.set_content(line)
			msg['To'] = RECIPIENT_EMAIL
			line = fp.readline()
			smtp.send_message(msg)

			line_num += 1
