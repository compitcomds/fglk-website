import bcrypt
import random
import string
from .Mail import SendMail

def generate_otp(email,num_digits=6):
    otp = ''.join(random.choices(string.ascii_letters + string.digits, k=num_digits))
    otp_bytes = otp.encode('utf-8')
    bcrypt_hash = bcrypt.hashpw(otp_bytes, bcrypt.gensalt())
    MSGSubject="this is forgot password"
    MSGBody=f"""
        <h2>FG LawKit</h2>
        <p>This is a testing mail for thanking the customer.</p>
        <hr>
        <i>Please provide a valid email format for sending messages to the customer.{otp}</i>
    """
    SendMail(email,MSGBody,MSGSubject)
    return bcrypt_hash.decode('utf-8')


def check_otp(otp, bcrypt_hash):
    otp_bytes = otp.encode('utf-8')
    return bcrypt.checkpw(otp_bytes, bcrypt_hash.encode('utf-8'))
        

