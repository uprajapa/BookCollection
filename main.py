import mongoengine as db
from mongoengine import Document

database_name = "database1"
database_password = "Urvish"
DB_URI = "mongodb+srv://urvish1:{}@cluster0.g7r2j.mongodb.net/{}?retryWrites=true&w=majority".format(database_password, database_name)

db.connect(host=DB_URI)

class Book(Document):
    book_id = db.IntField()
    name = db.StringField()
    author = db.StringField()
    def to_json(self):
        return {
            "book_id" : self.book_id,
            "name" : self.name,
            "author" : self.author
        }
    
print("\n Create a book")
book = Book(
    book_id=1,
    name=" Sherlock H. ",
    author=" XXX "
)
book.save()

print("\n Fetch a book \n")
book = Book.objects(book_id=1).first()
print(book.to_json())

book.update(name="GOT", author="ABC")
print(book.to_json())   #updating same book


