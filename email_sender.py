# Youtube video reference : https://www.youtube.com/watch?v=BsVQ_cBmEwg
# Go to gmail settings of the sender gmail and turn ON 'Less secure app access'

import smtplib

server = smtplib.SMTP('smtp.gmail.com', 567)

server.starttls()

server.login('','') # email in first single quotes AND password in second single quotes

server.sendmail('','Mail sent from python') # receiver email in quotes

print('Mail sent')