class Book:
    def __init__(self, title, Author):
        self.title = title
        self.Author = Author

    def get_name(self):
        return self.title
    
    def get_Author(self):
        return self.Author
    
    def get_Book_info(self):
        return "f Book {self.title}, Author {self.Author}"