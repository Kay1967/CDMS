from datetime import datetime as dt
from Component.UserInterface import *
from Domain.SuperAdmin import SuperAdmin



class LoginService:
  loggedin = False
  def __init__ (self, userRepository):
    self.userRepository = userRepository

  def login(self):
    username = input("please enter username: ").lower()
    password = input("please enter password: ")
    if username == 'superadmin' and password == 'Admin!23':
      self.tenant = SuperAdmin(username, password)
      self.loggedin = True
      return  
    
    user = self.userRepository.GetUser(username)
    if user == None or user.password != password:  # An empty result evaluates to False.
        print("Login failed")
    else:
        self.loggedin = True
        self.tenant = user
        today =  dt.now()
        date = today.strftime("%d-%m-%Y")
        self.userRepository.UpdateLastLogin(date, self.tenant.username)

  def show_all_clients(self):
    self.not_implemented(self.show_all_clients)
  def add_new_client(self):
    self.not_implemented(self.add_new_client)
    
  def delete_client(self):
    self.not_implemented(self.delete_client)  
  
  def show_all_users(self):
    self.not_implemented(self.show_all_users)

  def add_new_user(self, userName, Password):
      self.dbContext.append(username, password)
      self.dbContext.save()

  def make_a_user_admin(self):
    self.not_implemented(self.make_a_user_admin)

  def delete_user(self):
    self.not_implemented(self.delete_user)

  def change_password(self):
    self.not_implemented(self.change_password)

  def close():
    pass

  def logout(self):
    self.loggedin = 0
    self.loggedin_user = None
    self.admin_is_loggedin = 0 


  def close(self):
    self.userRepository.close()

