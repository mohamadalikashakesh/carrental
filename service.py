class Vehicle:
  
  rental_days=0
  
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year
    self.__pricepd = 0

  def getPrice(self):
    return self.__pricepd
  
  def setPrice(self, newPrice):
    self.__pricepd = newPrice

  def display_info(self):
    return f"{self.brand} {self.model}, Year: {self.year}, Rental Price: {self.__pricepd}$/day"

# class calculate_rental_cost(Vehicle):
#     def __init__(self, brand, model, year, rentingdays):
#         super().__init__(brand, model,year)  # Call parent constructor
#         self.rentingdays = rentingdays  # New attribute

#     def rental_days(self):
#         return {self.rentingdays}
    

vehicle1 = Vehicle("Bmw","E70","2009")
vehicle2 = Vehicle("Mercedes","E63","2012")
vehicle1.setPrice(70)
vehicle2.setPrice(100)
print(vehicle1.display_info())
print(vehicle2.display_info())