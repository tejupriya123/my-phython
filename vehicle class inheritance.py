class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def chinni(self):
      print(f"Brand: {self.brand}, Model: {self.model}")
class bike(Vehicle):
  def _init_(self, brand, model):
    super()._init_(brand, model)
  def mouna(self):
    super().chinni()
    print(f"Seats: {self.seats}")
obj= bike("DUKE 360",2020)
obj.chinni()
