class Phone:
  def __init__(self, brand, model, price):
    self.brand = brand
    self.model = model
    self.price = price
  def display(self):
    return f"{self.brand} {self.model} - ${self.price}"
  def modify(self, model=None, price=None):
    if model:
      self.model = model
    if price:
      self.price = price

phones = []

def main_menu():
  while True:
    choice = input("1: Add phone \n2. Modify Phone \n3. Delete Phone \n4. Show Phones \n5. Exit \nChoose an option: ")
    if choice == '1':
      brand = input("Enter a brand: ")
      model = input("Enter its model: ")
      price = input("Enter its price: ")
      phones.append(Phone(brand, model, price))
    elif choice == '2':
      index = int(input("Enter phone index to modify: "))
      if 0 <= index < len(phones):
        model = input("New model (leave it blank to skip): ")
        price = input("New price (leave it black to skip): ")
        phones[index].modify(model if model else None, float(price) if price else None)
    elif choice == '3':
      index = int(input("Enter index to delete: "))
      if 0 <= index < len(phones):
        del phones[index]
    elif choice == '4':
      for i, phones in enumerate(phones):
        print(f"{i}: {phones.display()}")
    elif choice == '5':
      break

if __name__ == "__main__":
  main_menu()