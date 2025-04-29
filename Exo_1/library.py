class Person:
    """To implement"""
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return self.__str__()

class Book:
    """To implement"""
    def __init__(self, title: str, author: Person):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} ({self.author})"

    def __repr__(self):
        return self.__str__()



class LibraryError(Exception):
    """Base class for Library errors"""
    pass
class Library:
    """To implement."""

    def __init__(self, name: str):
        self.name = name
        self._books = []  # liste des livres de la bibliothèque
        self._members = set()  # ensemble des membres inscrits
        self._borrowed_books = {}  # dictionnaire : {livre: personne qui l'a emprunté}

    def add_new_book(self, book: Book):
        """Ajoute un nouveau livre au catalogue"""
        if book in self._books:
            raise LibraryError(f"{book} is already in the library")
        self._books.append(book)

    def add_new_member(self, person: Person):
        """Ajoute une personne comme membre de la bibliothèque"""
        self._members.add(person)

    def is_book_available(self, book: Book) -> bool:
        """Retourne True si le livre est dans le catalogue et pas encore emprunté"""
        if book not in self._books:
            raise LibraryError(f"{book} doesn't exist in the library")
        return book not in self._borrowed_books

    def borrow_book(self, book: Book, person: Person):
        """Permet à une personne d'emprunter un livre, si toutes les conditions sont réunies"""
        if book not in self._books:
            raise LibraryError(f"{book} doesn't exist in the library")
        if person not in self._members:
            raise LibraryError(f"{person} is not a member of the library")
        if book in self._borrowed_books:
            raise LibraryError(f"{book} is already borrowed by {self._borrowed_books[book]}")
        self._borrowed_books[book] = person

    def return_book(self, book: Book):
        """Permet de rendre un livre emprunté"""
        if book not in self._borrowed_books:
            raise LibraryError(f"{book} is not part of the borrowed books")
        del self._borrowed_books[book]

    def print_status(self):
        """Affiche l'état actuel de la bibliothèque (livres, membres, emprunts...)"""
        print(f"{self.name} status:")
        print(f"Books catalogue: {self._books}")
        print(f"Members: {{{', '.join(str(m) for m in self._members)}}}")
        available_books = [book for book in self._books if book not in self._borrowed_books]
        print(f"Available books: {available_books}")
        borrowed_books_str = ", ".join(f"{book}: {person}" for book, person in self._borrowed_books.items())
        print(f"Borrowed books: {{{borrowed_books_str}}}")
        print("-----")

def main():
    """Test your code here"""
antoine = Person("Antoine", "Dupont")
print(antoine)

julia = Person("Julia", "Roberts")
print(julia)

rugby_book = Book("Jouer au rugby pour les nuls", Person("Louis", "BB"))
print(rugby_book)

novel_book = Book("Vingt mille lieues sous les mers", Person("Jules", "Verne"))
print(novel_book)

library = Library("Public library")
library.print_status()

library.add_new_book(rugby_book)
library.add_new_book(novel_book)
library.add_new_member(antoine)
library.add_new_member(julia)
library.print_status()

print(f"Is {rugby_book} available? {library.is_book_available(rugby_book)}")
library.borrow_book(rugby_book, antoine)
library.print_status()

try:
    library.borrow_book(rugby_book, julia)
except LibraryError as error:
    print(error)

try:
    library.borrow_book(Book("Roméo et Juliette", Person("William", "Shakespeare")), julia)
except LibraryError as error:
    print(error)

try:
    library.borrow_book(novel_book, Person("Simone", "Veil"))
except LibraryError as error:
    print(error)

try:
    library.return_book(novel_book)
except LibraryError as error:
    print(error)

library.return_book(rugby_book)
library.borrow_book(novel_book, julia)
library.print_status()

library.borrow_book(rugby_book, julia)
library.print_status()
if __name__ == "__main__":
    main()