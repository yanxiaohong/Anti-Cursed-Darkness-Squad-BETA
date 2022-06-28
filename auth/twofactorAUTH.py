import pyotp

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
        
SECRETKEY_AT_LOAD = PinAuthorization.GenerateSecretKey()
