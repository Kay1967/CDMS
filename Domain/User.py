import string
import random
from Enum.Permission import Permission
from Helper.EncryptionHelper import EncryptionHelper

class User:
    specialCharactersPassword = [ '~','!','@','#','$','%','^','&','*','_','-','+','=','`','|',"\\", '(',',',')',"{","}",'[',']',':','<','>',',','.','?','/', "'" ]
    whiteListPasswordCharacters = set.union(set(string.ascii_lowercase + string.ascii_uppercase + string.digits), 
                                            set(specialCharactersPassword))
    specialCharactersUsername = [ '-','_',"'", "." ]
    whiteListUsernameCharacters = set.union(set(string.ascii_lowercase + string.digits), 
                                            set(specialCharactersUsername))

    def __init__(self, username, password, fullname, admin):
      self.username = username
      self.password = password
      self.fullname = fullname
      self.admin = admin
      self.hasPermissions = []
    
    def HasPermission(self, permission):
      # If user has Manage permission, return all permissions starting with permission number as true
      try: 
        managePermission = Permission(int(str(permission.value)[0])) 
        hasManagePermission = managePermission in self.hasPermissions
      except: hasManagePermission = False

      hasPermission = permission in self.hasPermissions
      return hasManagePermission or hasPermission

    def UpdatePassword(self, newPassword):
      self.ValidateNewPassword(newPassword)
      self.password = newPassword

    def GenerateAndUpdatePassword(self):
      newPassword = [ f'{random.choice(string.ascii_lowercase)}', 
                      f'{random.choice(string.ascii_lowercase)}',
                      f'{random.choice(string.ascii_lowercase)}', 
                      f'{random.choice(string.ascii_lowercase)}', 
                      f'{random.choice(string.ascii_lowercase)}',  
                      f'{random.choice(string.ascii_uppercase)}', 
                      f'{random.choice(string.digits)}',
                      f'{random.choice(self.specialCharactersPassword)}']

      # Shuffle characters and create string
      random.shuffle(newPassword)
      newPassword = ''.join(newPassword)
      self.UpdatePassword(newPassword)

    def ValidateNewPassword(self, newPassword):
      if newPassword == self.password:
        raise ValueError("New password cannot be the same as old password")
      if len(newPassword) < 8 or len(newPassword) >= 30:
        raise ValueError("Password must be between 7 and 31 characters")
      if set(newPassword).issubset(self.whiteListPasswordCharacters) == False:
        raise ValueError("Password contains invalid characters")
      if not any(ch.isupper() for ch in newPassword) :
        raise ValueError("Password should contain at least one uppercase character")
      if not any(ch.islower() for ch in newPassword):
        raise ValueError("Password should contain at least one lowercase character")
      if not any(ch.isdigit() for ch in newPassword):
        raise ValueError("Password should contain at least one digit character")
      if not any(ch in self.specialCharactersPassword for ch in newPassword):
        specialCharactersToString = "".join(self.specialCharactersPassword)
        raise ValueError(f"Password should contain at least one of the following special characters: {specialCharactersToString}")

    def ValidateUsername(self, username):
      # Check if validation should be in place for all lower case or force username to .lower() on creation
      if username[0].isalpha() == False:
        raise ValueError("Username must start with a letter")
      if len(username) < 5 or len(username) >= 20:
        raise ValueError("Username must be between 4 and 21 characters")
      if set(username).issubset(self.whiteListUsernameCharacters) == False:
        raise ValueError("Username contains invalid characters. No uppercase letters can be used")
      