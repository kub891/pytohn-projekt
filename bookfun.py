"""
Modul do zarzadzania ksiazkami w bibliotece.

Ten modul zawiera funkcje umozliwiajace dodawanie nowych ksiazek do biblioteki
oraz usuwanie istniejacych ksiazek z biblioteki.

Funkcje:
    - add_book(): Pozwala uzytkownikowi dodac nowa ksiazke do biblioteki.
    - remove_book(): Pozwala uzytkownikowi usunac istniejaca ksiazke z biblioteki,
                     przy uzyciu ID ksiazki lub tytulu ksiazki.

Przyklady uzycia:
    import bookfun

    Aby dodac nowa ksiazke, nalezy wywolac funkcje add_book(). Zostaniesz poproszony
    o podanie autora, tytulu i liczby stron ksiazki.

    bookfun.add_book()
    
    Aby usunac ksiazke, nalezy wywolac funkcje remove_book(). Nastepnie zostaniesz poproszony
    o podanie ID ksiazki lub tytulu ksiazki, ktora chcesz usunac.

    bookfun.remove_book()

Wymagane moduly:
    datetime
    pandas
"""








from datetime import date
import pandas as pd
def add_book():
    existing_data = pd.read_csv('./Library/book.csv')
    author = input('Podaj Autora: ')
    title = input('Podaj tytul ksiazki: ')
    while True:
        pages = input('Podaj ilosc stron: ')
        if(str(pages).isdigit()):
            if(int(pages) > 0):
                break
        print('Ilosc stron musi byc liczba wieksza od 0')

    new_data = pd.DataFrame({'ID': [int(existing_data.iloc[-1]['ID'])+1], 'AUTHOR': [author], 'TITLE': [title],'PAGES': [pages], 'CREATED': [date.today()], 'UPDATED': [date.today()]})
    updated_data = pd.concat([existing_data, new_data], ignore_index=True)
    updated_data.to_csv('./Library/book.csv', index=False)

def remove_book():
    try:
        existing_data = pd.read_csv('./Library/book.csv')
        
        user_input = input("Wprowadz ID ksiazki lub tytul ksiazki, ktora chcesz usunac: ")
        try:
            book_id = int(user_input)
            if book_id in existing_data['ID'].values:
                updated_data = existing_data[existing_data['ID'] != book_id]
                updated_data.to_csv('./Library/book.csv', index=False)
                print("Ksiazka zostala pomyslnie usunieta.")
            else:
                raise ValueError("Ksiazka o podanym ID nie istnieje.")
        except ValueError:
            book_title = user_input
            if book_title not in existing_data['TITLE'].values:
                raise ValueError("Ksiazka o podanym tytule nie istnieje.")
            updated_data = existing_data[existing_data['TITLE'] != book_title]
            updated_data.to_csv('./Library/book.csv', index=False)
            print("Ksiazka zostala pomyslnie usunieta.")
    
    except FileNotFoundError:
        print("Plik CSV nie zostal znaleziony.")
    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("Error:", e)
    
