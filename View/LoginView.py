from Service.LoginService import *
from Repository.UserRepository import *

class LoginView:

  def __init__(self, loginService):          
    self.loginService = loginService
    
  def GetMenu(self):
    return [[1, 'login', self.loginService.login ], [0, 'Exit', self.loginService.close]]

  def GetMenuDb(self):
    return    [[1, 'show all clients', self.loginService.show_all_clients], [2, 'show all users', self.loginService.show_all_users], \
            [3, 'add new client', self.loginService.add_new_client], [4, 'add new user', self.loginService.add_new_user], \
            [5, 'make a user "admin"', self.loginService.make_a_user_admin], \
            [6, 'delete a client', self.loginService.delete_client], [7, 'delete a user', self.loginService.delete_user], \
            [8, 'change password', self.loginService.change_password], [0, 'logout', self.loginService.logout]]
    
    # [ [1, 'show all clients', self.userRepository.show_all_clients], [2, 'show all users', self.userRepository.show_all_users], \
    #         [3, 'add new client', self.userRepository.add_new_client], [4, 'add new user', self.userRepository.add_new_user], \
    #         [5, 'make a user "admin"', self.userRepository.make_a_user_admin], \
    #         [6, 'delete a client', self.userRepository.delete_client], [7, 'delete a user', self.userRepository.delete_user], \
    #         [8, 'change password', self.userRepository.change_password], [0, 'logout', self.userRepository.logout]] 
    
    
