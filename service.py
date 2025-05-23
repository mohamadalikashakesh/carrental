class Vehicle:
  
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
  
  def calculate_rental_cost(self, days):
    price = self.getPrice()
    return int(days * price)
  
  def update_price(self, updatedprice):
    self.setPrice(updatedprice)
  
class Car(Vehicle):

  def __init__(self, brand, model, year, seating_capacity):
    self.seating_capacity = seating_capacity
    super().__init__(brand, model, year)

  def display_info(self):
    parent_output = super().display_info()
    child_output = f", Seats : {self.seating_capacity}"
    return f"{parent_output}{child_output}"
  
class Bike(Vehicle):

  def __init__(self, brand, model, year, engine_capacity):
    self.engine_capacity = engine_capacity
    super().__init__(brand, model, year)

  def display_info(self):
    parent_output = super().display_info()
    child_output = f", Engine : {self.engine_capacity}"
    return f"{parent_output}{child_output}"


vehicle1 = Car("Bmw","E70","2009","5")
vehicle2 = Vehicle("Mercedes","E63","2012")
vehicle3 = Bike("Suzuki","GSXR","2012","600cc")

vehicle1.setPrice(70)
vehicle2.setPrice(100)
vehicle3.setPrice(50)

print("\n")
print(vehicle1.display_info())
print(vehicle2.display_info())
print(vehicle3.display_info())
print("\n")
print(f"Rental cost for {vehicle1.brand} {vehicle1.model} for 3 days: ${vehicle1.calculate_rental_cost(3)}")
print(f"Rental cost for {vehicle2.brand} {vehicle2.model} for 5 days: ${vehicle2.calculate_rental_cost(5)}")
print(f"Rental cost for {vehicle3.brand} {vehicle3.model} for 9 days: ${vehicle3.calculate_rental_cost(9)}")
print("\n")

vehicle1.update_price("80")
print(f"Updated rental price for {vehicle1.brand} {vehicle1.model}: ${vehicle1.getPrice()}/day")
