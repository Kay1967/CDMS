class Client:
  
  def __init__(self, client_data):
    self.fullname = client_data[0]
    self.streetname = client_data[1]
    self.housenumber = client_data[2]
    #self.zipcode = client_data[3]
    self.UpdatezipCode(client_data[3])
    self.city = client_data[4]
    self.emailaddress = client_data[5]
    #self.mobilephonenumber = client_data[6]
    self.UpdateMobilePhoneNumber(client_data[6])

 
  def UpdateMobilePhoneNumber(self, phonenumber):
    countryCode = "+31-6-"
    if len(self.phonenumber) < 8 or len(self.phoneNumber) > 8:
      raise ValueError("phone number must be excatly 8 digits")
    self.mobilephonenumber = countryCode + phonenumber
  
  def UpdatezipCode(self, zipcode):
    if len(zipcode) != 6:
      raise ValueError("zipcode must be excatly 6 characters")
    #districtNumber, districtLetter = input("please enter zipcode: ").split()
    if not any(ch.isdigit() for ch in zipcode[0:5]):
        raise ValueError("zipcode must start with exactly 4 digits")
    if not any(ch.isalpha() and ch.isupper() for ch in zipcode[5:7]):
        raise ValueError("zipcode must end with excatly 2 characters")

    

 
  
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
    