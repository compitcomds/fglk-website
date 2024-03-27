from config import Config
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

def SendMail(Toemail, MSGbody, MSGsubject):
    email = Config.MAIL
    password = Config.MAIL_PASSWORD
    
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = Toemail
    msg['Subject'] = MSGsubject
    body = MSGbody
    msg.attach(MIMEText(body, 'html'))

    try:
        server = smtplib.SMTP('smtp.zoho.in', 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, Toemail, msg.as_string())
        logging.info("Email sent successfully!")
    except smtplib.SMTPAuthenticationError as e:
        logging.error("SMTP authentication error: %s", e)
    except smtplib.SMTPException as e:
        logging.error("SMTP error occurred: %s", e)
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)
    finally:
        try:
            server.quit()
        except UnboundLocalError:
            pass  # If server variable was never initialized
