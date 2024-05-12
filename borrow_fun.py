"""
Modul do zarzadzania wypozyczeniami i zwrotami ksiazek w bibliotece.

Ten modul zawiera funkcje umozliwiajace wypozyczanie oraz zwracanie ksiazek przez klientow
biblioteki.

Funkcje:
    - borrow_books(customer_id, book_ids): Pozwala klientowi wypozyczyc jedna lub wiecej ksiazek
      z biblioteki na podstawie ich identyfikatorow.
    - return_books(customer_id, returned_book_ids): Pozwala klientowi zwrocic jedna lub wiecej ksiazek
      do biblioteki na podstawie ich identyfikatorow. Ta funkcja jest dekorowana
      przez dekorator return_books_decorator, ktory umozliwia zwracanie wielu ksiazek jednoczesnie.

Dekorator:
    - return_books_decorator: Dekorator uzywany w funkcji return_books do obslugi zwracania wielu ksiazek.
      Dekorator ten umozliwia sprawdzenie poprawnosci zwrotu ksiazek i zwraca liste zwroconych ksiazek.

Przyklady uzycia:
    import borrow_fun

    Aby wypozyczyc ksiazki, nalezy wywolac funkcje borrow_books(customer_id, book_ids),
    podajac ID klienta i liste identyfikatorow ksiazek do wypozyczenia.

    borrow_fun.borrow_books('123')

    Aby zwrocic ksiazki, nalezy wywolac funkcje return_books(customer_id, returned_book_ids),
    podajac ID klienta i liste identyfikatorow ksiazek do zwrotu.

    borrow_fun.return_books('123')

Wymagane moduly:
    os
    pandas
    datetime
"""





import os
import pandas as pd
from datetime import date
#Funkcja wielu zmiennych
def borrow_books(customer_id, book_ids):
    try:
        customers_data = pd.read_csv('./Library/customer.csv')
        if int(customer_id) not in customers_data['ID'].values:
            print("Klient o podanym ID nie istnieje.")
            return
        books_data = pd.read_csv('./Library/book.csv')
        missing_books = [book_id for book_id in book_ids if int(book_id) not in books_data['ID'].values]
        if missing_books:
            print(f"Ksiazki o podanych ID nie istnieja: {missing_books}")
            return
        customer_file = "./DATABASE/" + customer_id + ".txt"
        if not os.path.exists(customer_file):
            with open(customer_file, 'w') as f:
                f.write(f"Wypozyczone ksiazki przez klienta o ID {customer_id}:\n")
        with open(customer_file, 'a') as f:
            for book_id in book_ids:
                f.write(f"ID ksiazki: {book_id}, Data wypozyczenia: {date.today()}\n")
        print("Ksiazki zostały pomyslnie wypozyczone przez klienta.")

    except FileNotFoundError:
        print("Brak pliku customers.csv lub book.csv.")
    except Exception as e:
        print("Wystapil blad podczas wypozyczania ksiazek:", e)

def return_books(customer_id, returned_book_id):
    try:
        customer_file = "./DATABASE/" + customer_id + ".txt"
        if not os.path.exists(customer_file):
            print("Klient o podanym ID nie ma wypozyczonych ksiazek.")
            return
        with open(customer_file, 'r') as f:
            lines = f.readlines()   
        with open(customer_file, 'w') as f:
            for line in lines:
                book_id = line.split(', ')[0].split(': ')[1].strip()
                if book_id != returned_book_id:
                    f.write(line)
        print("Ksiazki zostaly pomyslnie zwrocone.")
    except FileNotFoundError:
        print("Brak pliku klienta o podanym ID.")
    except Exception as e:
        print("Wystapil blad podczas zwracania ksiazek:", e)

#dekorator
def return_books_decorator(func):
    def return_books(customer_id, returned_book_ids):
        try:
            customer_file = "./DATABASE/" + customer_id + ".txt"
            returned_books = []
            if not os.path.exists(customer_file):
                print("Klient o podanym ID nie ma wypozyczonych ksiazek.")
                return returned_books
            with open(customer_file, 'r') as f:
                lines = f.readlines()
            with open(customer_file, 'w') as f:
                for line in lines:
                    book_id = line.split(', ')[0].split(': ')[1].strip()
                    if book_id not in returned_book_ids:
                        f.write(line)
                    else:
                        returned_books.append(book_id)
            print("Ksiazki zostaly zwrocone pomyslnie.")
            return returned_books
        except FileNotFoundError:
            print("Brak pliku klienta o podanym ID.")
            return returned_books
        except Exception as e:
            print("Wystapil blad podczas zwracania ksiazek:", e)
            return returned_books
    return return_books

@return_books_decorator
def return_books(customer_id, returned_book_ids):
    return