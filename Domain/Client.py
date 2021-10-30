import re

class Client:
  regexEmail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

  def __init__(self, fullname, emailAddress, mobilePhoneNumber, address):
    self.fullname = fullname
    self.emailaddress =  emailAddress
    self.mobilephonenumber = mobilePhoneNumber
    address.ValidateAddress()
    
    self.address = address

  def UpdateMobilePhoneNumber(self, phonenumber):
    countryCode = "+31-6-"
    phonenumberReplace = phonenumber.replace(countryCode, "")
    if len(phonenumberReplace) != 8:
      raise ValueError("phone number must be exactly 8 digits", True)
    self.mobilephonenumber = countryCode + phonenumberReplace

  def UpdateEmailAdress(self, emailaddress):
    if not (re.fullmatch(self.regexEmail, emailaddress)):
      raise ValueError("not an valid email", True)
    self.emailaddress = emailaddress
  

    