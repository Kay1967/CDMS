from termcolor import colored
from Component.UserInterface import *
from Domain.User import User
from Domain.Advisor import Advisor
from Domain.SuperAdmin import SuperAdmin
from Domain.SysAdmin import SysAdmin
from View.LoginView import LoginView
import sqlite3



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
    print(user)
    if user == None or user.password != password:  # An empty result evaluates to False.
        print("Login failed")
    else:
        self.loggedin = True
        self.tenant = loggedin_user
        # self.loggedin_user = username
        # self.admin_is_loggedin = loggedin_user[3]
        # user_type = 'Admin' if self.admin_is_loggedin == 1 else 'Not Admin'
        # print('\n\n\n\nWelcome')
        # print( '▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄'  + '\n'   + \
        #           '▍ '                                           + '\n'   + \
        #           '▍ Username: ' + colored(self.loggedin_user, 'red')   + '\n'   + \
        #           '▍ '                                           + '\n'   + \
        #           '▍ User type: ' + colored(user_type, 'red')    + '\n'   + \
        #           '▍ '                                           + '\n'   + \
        #           '▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀'  + '\n'   + \
        #           'User Menu')
        # db_menu = [ [1, 'show all clients', self.userRepository.show_all_clients], [2, 'show all users', self.userRepository.show_all_users], \
        #     [3, 'add new client', self.userRepository.add_new_client], [4, 'add new user', self.userRepository.add_new_user], \
        #     [5, 'make a user "admin"', self.userRepository.make_a_user_admin], \
        #     [6, 'delete a client', self.userRepository.delete_client], [7, 'delete a user', self.userRepository.delete_user], \
        #     [8, 'change password', self.userRepository.change_password], [0, 'logout', self.userRepository.logout]] 
        
        
        # db_interface = user_interface(heading, db_menu = LoginView(dbContext).GetMenuDb())
        # db_interface.run()
        # del db_interface
        

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
    self.conn.close()

  def logout(self):
    self.loggedin = 0
    self.loggedin_user = None
    self.admin_is_loggedin = 0 


  def close(self):
    self.userRepository.close()

