from termcolor import colored

class MainView:
  def __init__(self, loginService, advisorService, userService):
    self.loginService = loginService
    self.advisorService = advisorService
    self.userService = userService

  def GetMenu(self):
   return [ 
            [1, 'update password for advisor', self.advisorService.UpdatePasswordForAdvisor],
            [2, 'view all users', self.userService.GetAllUsers],
            [0, 'Exit', self.loginService.close]
    
          ]
  #          [3, 'add new client', clientService.add_new_client], [4, 'add new user', userService.add_new_user], \
  #           [5, 'make a user "admin"', userService.make_a_user_admin], \
  #           [6, 'delete a client', clientService.delete_client], [7, 'delete a user', userService.delete_user], \
  #           [8, 'change password', userService.change_password], [0, 'logout', loginService.logout]]
