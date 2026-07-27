import smtplib
import os

from email.message import EmailMessage

def sendMail(receiver, logPath, body):
  mail = EmailMessage()

  mail["From"] = "yashsatarkar64@gmail.com"
  mail["To"] = receiver
  mail["Subject"] = "Testing Assignment 33"

  mail.set_content(body)

  try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("yashsatarkar64@gmail.com", "nqyl uhfa bkpx wref")

    afobj = open(logPath, "rb")
    data = afobj.read()
    mail.add_attachment(data,maintype="text", subtype= "plain", filename=str(os.path.basename(logPath)))
    server.send_message(mail)
    afobj.close()
  except Exception as e:
    with open(logPath, "a") as log:
       log.write(f"\nEmail Error: {e} \n")
    return False
  finally:
      server.quit()

  return True


