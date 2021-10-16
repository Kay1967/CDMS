from Repository.UserRepository import *
# every actions in the context of an advisor
class AdvisorService:
  def __init__(self, userRepository):
    self.UserRepository = userRepository

  def UpdatePasswordForAdvisor(self, username, newPassword):
    self.UserRepository.GetUser()
