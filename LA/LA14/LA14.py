class Spiderman:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def describeSpiderman(self):
    print(f"Name: {self.name} Age: {self.age}")

class Tobey(Spiderman):
  def __init__(self, name, age, movie_title):
    super().__init__(name, age)
    self.movie_title = movie_title

class Andrew(Spiderman):
  def __init__(self, name, age, movie_title):
    super().__init__(name, age)
    self.movie_title = movie_title

class Tom(Spiderman):
  def __init__(self, name, age, movie_title):
    super().__init__(name, age)
    self.movie_title = movie_title

tobey = Tobey("tobey maguire", 49, "Spiderman Trilogy")
andrew = Andrew("andrew garfield", 41, "The Amazing Spiderman")
tom = Tom("tom holland", 28, "Spiderman: Home Coming")

print(f"""
{tobey.name.upper()} {tobey.movie_title}
{andrew.name.upper()} {andrew.movie_title}
{tom.name.upper()} {tom.movie_title}
""")  