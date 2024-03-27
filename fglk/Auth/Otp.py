import bcrypt
import random
import string
from .Mail import SendMail

def generate_otp(email,num_digits=6):
    """
    Generate a random OTP (One Time Password) consisting of digits and letters.
    :param num_digits: Number of digits in the OTP (default is 6)
    :return: OTP in bcrypt format
    """
    
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
    """
    Check if the provided OTP matches the given bcrypt hash.
    :param otp: The OTP provided by the user
    :param bcrypt_hash: The bcrypt hash of the correct OTP
    :return: True if the OTP matches the bcrypt hash, False otherwise
    """
    otp_bytes = otp.encode('utf-8')
    return bcrypt.checkpw(otp_bytes, bcrypt_hash.encode('utf-8'))
        

