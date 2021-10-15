#from termcolor import colored
class AdminView:

  def __init__(self, dbContext):          
    
    self.clientService = LoginService(UserRepository(dbContext))
  def GetMenuDb(self):
    return  [[1, 'show all clients', clientService.show_all_clients], [2, 'show all users', userService.show_all_users], \
            [3, 'add new client', clientService.add_new_client], [4, 'add new user', userService.add_new_user], \
            [5, 'make a user "admin"', userService.make_a_user_admin], \
            [6, 'delete a client', clientService.delete_client], [7, 'delete a user', userService.delete_user], \
            [8, 'change password', userService.change_password], [0, 'logout', loginService.logout]]
  # db_menu = [ [1, 'show all clients', dbContext.show_all_clients], [2, 'show all users', dbContext.show_all_users], \
  #           [3, 'add new client', dbContext.add_new_client], [4, 'add new user', dbContext.add_new_user], \
  #           [5, 'make a user "admin"', dbContext.make_a_user_admin], \
  #           [6, 'delete a client', dbContext.delete_client], [7, 'delete a user', dbContext.delete_user], \
  #           [8, 'change password', dbContext.change_password], [0, 'logout', dbContext.logout]] 