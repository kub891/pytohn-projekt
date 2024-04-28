import csv
import pandas as pd
import os
def add_book():
    file_path = os.path.abspath('Library/book.csv')
    with open(file_path, 'r') as file:
    # Odczytanie zawartości pliku
     zawartosc = file.read()

# Wyświetlenie zawartości pliku
    print(zawartosc)

# Dodanie nowych danych do istniejących danych
#nowa_ramka_danych = pd.concat([existing_data, nowe_dane], ignore_index=True)