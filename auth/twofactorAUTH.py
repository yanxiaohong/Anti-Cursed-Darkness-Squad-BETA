import pyotp
import rsa 

class PinAuthorization():
    def __init__(self, pincodeInput,secret):
        self.pincodeInput = pincodeInput
        self.secret =secret

    @staticmethod
    def GenerateSecretKey():
        return pyotp.random_base32()
    
    def Validate(self):
        pincode = self.pincodeInput

        totp = pyotp.TOTP(self.secret)
        return totp.verify(pincode)
        
pub,priv= rsa.newkeys(600)
SECRETKEY_AT_LOAD = rsa.encrypt(PinAuthorization.GenerateSecretKey().encode('utf-8'),pub)

def Decrypt(secret):
    return rsa.decrypt(secret, priv).decode('utf-8')
