class Phone:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def describe_phone(self):
    return f"This phone is a {self.brand} model {self.model}"

class android(Phone):
  def __init__(self, brand, model):
    Phone.__init__(self, brand, model)

phone1 = android("Nothing Phone", "2")
print(phone1.describe_phone())