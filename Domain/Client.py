class Client:
  
  def __init__(self, client_data, address):
    self.fullname = client_data[0]
    self.UpdateEmailAdress(client_data[1])
    self.UpdateMobilePhoneNumber(client_data[2])
    address.ValidateAddress()
    self.address = address
    
  def UpdateMobilePhoneNumber(self, phonenumber):
    countryCode = "+31-6-"
    if len(self.phonenumber) < 8 or len(self.phoneNumber) > 8:
      raise ValueError("phone number must be excatly 8 digits")
    self.mobilephonenumber = countryCode + phonenumber

  def UpdateEmailAdress(self, emailaddress):
    self.emailaddress = emailaddress
  
  
  
    

 
  
  # def menuDisplayCity(self):
  #  # default_menu = [[1, 'option 1', None], [2, 'option 2', None], [3, 'option 2', None], [0, 'Exit', None]]
  #   cities = ['Amsterdam', 'Rotterdam', 'Den Haag', 'Utrecht', 'Zwolle', 'Maastricht', 'Groningen', 'Arnhem', 'Leeuwarden', 'Assen']
  #   print('Select a city')
  #   print('_________________________________\n')
  #   for index, option in enumerate(cities, start = 1):
  #       print('[' + str(index) + ']' + ' ' + option)
  #   self.selectCity()

  # def selectCity(self):
  #   chooseOption = int(input('Choose a number from the menu: '))
  #   for index, option in enumerate(cities, start = 1):
  #     try:
  #       if chooseOption == index:
  #         option = cities.index(chooseOption)
  #     except:
  #       print("invalid option")
  #     self.menuDisplayCity()

  
    
    

  def GetItemsToUpdate(self):
    # ItemToUpdate = 

    for item in ItemToUpdate:
          if ItemToUpdate[1] == streetname:
            NewStreetName = input("please enter a new streetname: ")
            self.clientRepository.Updateclient(NewStreetName)
          if ItemToUpdate[2] == housenumber:
            NewHouseNumber = input("please enter a new housenumber: ")
            self.tenant.Updateclient(NewHouseNumber)
          if ItemToUpdate[3] == zipcode:
            NewZipCode = input("please enter a new zipcode: ")
            self.tenant.Updateclient(NewZipCode)
          if ItemToUpdate[4] == city:
            NewCity = input("please enter a new city: ")
            self.tenant.Updateclient(NewCity)
          if ItemToUpdate[5] ==  emailaddress:
            NewEmailAddress = input("please enter a new emailaddress: ")
            self.tenant.Updateclient(NewEmailAddress)
          if ItemToUpdate[6] == mobilephone:
            NewMobilePhone = input("please enter a new mobilephone: ")
            self.tenant.Updateclient(NewMobilePhone)  
    