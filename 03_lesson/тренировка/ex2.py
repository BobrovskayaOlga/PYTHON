from book import Book

library = [
    Book("Властелин колец", "Толкиен"),
    Book("Гордость и предубеждение", "Джейн Остен"),
    Book("Джейн Эйр", "Шарлота Бронте")
]

for book in library:
    print(f"{book.title} - {book.Author}" )