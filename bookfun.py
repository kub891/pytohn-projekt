from datetime import date
import pandas as pd
def add_book():
    existing_data = pd.read_csv('./Library/book.csv')
    author = input('Podaj Autora: ')
    title = input('Podaj tytul ksiazki: ')
    pages = int(input('Podaj ilosc stron: '))
    new_data = pd.DataFrame({'ID': [int(existing_data.iloc[-1]['ID'])+1], 'AUTHOR': [author], 'TITLE': [title],'PAGES': [pages], 'CREATED': [date.today()], 'UPDATED': [date.today()]})
    updated_data = pd.concat([existing_data, new_data], ignore_index=True)
    updated_data.to_csv('./Library/book.csv', index=False)

def remove_book_id(book_id):
    try:
        existing_data = pd.read_csv('./Library/book.csv')
        if book_id not in existing_data['ID'].values:
            raise ValueError("Książka o podanym ID nie istnieje.")
        updated_data = existing_data[existing_data['ID'] != book_id]
        print(updated_data)
        updated_data.to_csv('./Library/book.csv', index=False)
        print("Ksiazka zostala pomyslnie usunieta.")
    except FileNotFoundError:
        print("Plik CSV nie został znaleziony.")
    except Exception as e:
        print("error:", e)

def remove_book_title(book_title):
    try:
        existing_data = pd.read_csv('./Library/book.csv')
        if book_title not in existing_data['TITLE'].values:
            raise ValueError("Książka o podanym tytule nie istnieje.")
        updated_data = existing_data[existing_data['ID'] != book_title]
        print(updated_data)
        updated_data.to_csv('./Library/book.csv', index=False)
        print("Książka została pomyślnie usunięta.")
    except FileNotFoundError:
        print("Plik CSV nie został znaleziony.")
    except Exception as e:
        print("error:", e)
