from Domain.SuperAdmin import SuperAdmin
from Domain.SysAdmin import SysAdmin
from Enum.Permission import Permission


class SysAdminService:  

  def __init__(self, tenant, userRepository, loggingRepository):
    self.tenant = tenant
    self.userRepository = userRepository
    self.loggingRepository = loggingRepository
    
  def CreateSysAdmin(self):
    if not self.tenant.HasPermission(Permission.ManageSysAdmin):
      print("Unauthorized")
      return

    try:
      username = input("please enter username: ")
      fullname = input("please enter fullname: ")
      sysadmin = SysAdmin(username, None, fullname, True)
      sysadmin.GenerateAndUpdatePassword()
    except ValueError as error: print(error); return

    self.userRepository.CreateUser(sysadmin.username, sysadmin.password, sysadmin.fullname, "1")  
    self.loggingRepository.CreateLog(self.tenant.username, f"New SysAdmin added: {sysadmin.username}", "Success", 0)
    print(f"Created new admin: {sysadmin.username}\nPassword : {sysadmin.password}") 
  
  def UpdatePasswordForSysAdmin(self):
    # if self.tenant is not Advisor and self.tenant is not SysAdmin and self.tenant is not SuperAdmin:
    # Haspermission is a method that gives back a boolean based on if the tenant has the permission UpdateAdvisorPassword
    if not self.tenant.HasPermission(Permission.UpdateSysAdminPassword):
      print("Unauthorized")
      return

    if type(self.tenant) is SysAdmin:
      sysadmin = self.tenant
      print("Password criteria:\nCannot be the same as old password\nBetween 7 and 31 characters\nWith atleast one uppercase, one lowercase and one special\n")
      newPassword = input("please enter a new password: ")
      try: self.tenant.UpdatePassword(newPassword)
      except ValueError as error: print(error); return
    else:
      try:
        sysadmin = self.GetAndValidateSysAdmin()
        sysadmin.GenerateAndUpdatePassword() 
      except ValueError as error: print(error); return    

    self.userRepository.UpdatePassword(sysadmin.username, sysadmin.password)  
    self.loggingRepository.CreateLog(self.tenant.username, f"Updated Password For admin: {sysadmin.username}", "Success", 0)
    print("New Password for " + sysadmin.username + ". Password: " + sysadmin.password)

  def DeleteSysAdmin(self):
    if not self.tenant.HasPermission(Permission.ManageSysAdmin):
      print("Unauthorized")
      return
    
    try: sysadmin = self.GetAndValidateSysAdmin()
    except ValueError as error: print(error); return    

    self.userRepository.DeleteUser(sysadmin.username)
    self.loggingRepository.CreateLog(self.tenant.username, f"Deleted admin: {sysadmin.username}", "Success", 0)
    print(f"Deleted SysAdmin: {sysadmin.username}") 

  # helpers
  def GetAndValidateSysAdmin(self):
    username = input("please enter username: ").lower()
    user = self.userRepository.GetUser(username)
    if type(user) is not SysAdmin:
      raise ValueError("User is not a sysadmin")

    return user