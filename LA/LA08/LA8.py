class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

book1 = Book("Harry Potter: The Prisoner of Azkaban", "JK Rowlings")
print(book1.title, book1.author)

del book1.author
print(book1.author)

book2 = Book("Harry Potter: Order of the Phoenix", "Jk Rowlings")
print(book2.title, book2.author)