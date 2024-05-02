import pandas as pd
import random
import string
from datetime import date
def random_id(existing_data):
    while(True):
        customer_id = ''.join(random.choices(string.digits, k=4))
        if customer_id not in existing_data['ID'].values:
            return customer_id
            

def add_customer(random_id_func):
    existing_data = pd.read_csv('./Library/customer.csv')
    customer_id = random_id_func(existing_data)
    name = input('Podaj imie: ')
    email = input('Podaj e-maili: ')
    phone = input('Podaj numer telefonu: ')
    new_data = pd.DataFrame({'ID': [customer_id], 'NAME': [name], 'E-MAIL': [email],'PHONE': [phone], 'CREATED': [date.today()], 'UPDATED': [date.today()]})
    updated_data = pd.concat([existing_data, new_data], ignore_index=True)
    updated_data.to_csv('./Library/customer.csv', index=False)

    existing_data2 = pd.read_csv('./Library/address.csv')
    street = input('Podaj ulice: ')
    city = input('Podaj miasto: ')
    country = input('Podaj kraj: ')
    new_data2 = pd.DataFrame({'ID': [customer_id], 'STREET': [street], 'CITY': [city], 'COUNTRY': [country]})
    updated_data2 = pd.concat([existing_data2, new_data2], ignore_index=True)
    updated_data2.to_csv('./Library/address.csv', index = False)
    print('Poprawnie dodano uzytkownika')

def remove_customer(customer_id):
    try:
        existing_data = pd.read_csv('./Library/customer.csv')
        existing_data2 = pd.read_csv('./Library/address.csv')
        if customer_id not in existing_data['ID'].values:
            raise ValueError("Klient o podanym ID nie istnieje.")
        if customer_id not in existing_data2['ID'].values:
            raise ValueError("Klient o podanym ID nie istnieje.")
        updated_data = existing_data[existing_data['ID'] != customer_id]
        updated_data2 = existing_data2[existing_data2['ID'] != customer_id]
        updated_data.to_csv('./Library/customer.csv', index=False)
        updated_data2.to_csv('./Library/address.csv')
        print("Klient zostal pomyslnie usuniety.")
    except FileNotFoundError:
        print("Plik CSV nie został znaleziony.")
    except Exception as e:
        print("error:", e)

def remove_customer_name(customer_name):
    try:
        existing_data = pd.read_csv('./Library/customer.csv')
        existing_data2 = pd.read_csv('./Library/address.csv')
        if customer_name not in existing_data['NAME'].values:
            raise ValueError("Klient o podanym imieniu nie istnieje.")
        matching_customer = existing_data[existing_data['NAME'] == customer_name]

        updated_data = existing_data[existing_data['NAME'] != customer_name]
        updated_data2 = existing_data2[existing_data2['ID'] != matching_customer['ID'].iloc[0]]
        updated_data.to_csv('./Library/customer.csv', index=False)
        updated_data2.to_csv('./Library/address.csv')
        print("Klient zostal pomyslnie usuniety.")
    except FileNotFoundError:
        print("Plik CSV nie został znaleziony.")
    except Exception as e:
        print("error:", e)
