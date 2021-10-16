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