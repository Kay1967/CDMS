from Service.ClientService import *
from Repository.ClientRepository import *

class ClientView:

  def __init__(self, clientService):          
    self.clientService = clientService
    
  def GetMenu(self):
    return [
        [1, 'Amsterdam', self.clientService.selectCity], [2, 'Rotterdam', self.clientService.selectCity], \
        [3, 'Den Haag', self.clientService.selectCity], [4, 'Utrecht', self.clientService.selectCity], \
        [5, 'Zwolle', self.clientService.selectCity], [6, 'Maastricht', self.clientService.selectCity], \
        [7, 'Groningen', self.clientService.selectCity], [8, 'Arnhem', self.clientService.selectCity], \
        [9, 'Leeuwarden', self.clientService.selectCity], [10, 'Assen', self.clientService.selectCity] 
      ]

    