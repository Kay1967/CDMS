class Address:
  cities = {1 : 'Amsterdam', 
            2: 'Rotterdam',
            3: 'Den Haag',
            4: 'Utrecht',
            5: 'Zwolle',
            6: 'Maastricht',
            7: 'Groningen',
            8: 'Arnhem',
            9: 'Leeuwarden',
            10: 'Assen'}

  def UpdateStreetName(self, streetname):
    self.streetname = streetname 
  
  def UpdateHouseNumber(self, housenumber):
    self.housenumber = housenumber

  def UpdateZipCode(self, zipcode):
    if len(zipcode) != 6:
      raise ValueError("zipcode must be excatly 6 characters")
    if not any(ch.isdigit() for ch in zipcode[0:5]):
        raise ValueError("zipcode must start with exactly 4 digits")
    if not any(ch.isalpha() for ch in zipcode[5:7]):
        raise ValueError("zipcode must end with excatly 2 characters")
    self.zipcode = zipcode 

  def UpdateCity(self, cityKey):
    if cityKey not in self.cities:
      raise ValueError("city does not exist")
    self.city = self.cities.get(cityKey)

  def ValidateAddress(self):
    try:
      self.city 
      self.zipcode
      self.housenumber
      self.streetname
    except:
      raise ValueError("address not complete")

  
   