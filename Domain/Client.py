from Domain.Address import Address

class Client:
  
  def __init__(self, fullname, emailAddress, mobilePhoneNumber, address):
    self.fullname = fullname
    self.UpdateEmailAdress(emailAddress)
    self.UpdateMobilePhoneNumber(mobilePhoneNumber)
    self.mobilePhoneNumber = mobilePhoneNumber
    address.ValidateAddress()
    
    self.address = address
    
  def UpdateMobilePhoneNumber(self, phonenumber):
    countryCode = "+31-6-"
    phonenumberReplace = phonenumber.replace(countryCode, "")
    if len(phonenumberReplace) != 8:
      raise ValueError("phone number must be exactly 8 digits")
    self.mobilephonenumber = countryCode + phonenumberReplace

  def UpdateEmailAdress(self, emailaddress):
    self.emailaddress = emailaddress
  

    