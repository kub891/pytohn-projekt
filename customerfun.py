import pandas as pd
import random
from datetime import date

def add_customer():
    customer_id = str(random.sample('0123456789', k=4))
    existing_data = pd.read_csv('./Library/customer.csv')
    name = input('Podaj imie: ')
    email = input('Podaj e-maili: ')
    phone = int(input('Podaj numer telefonu: '))
    new_data = pd.DataFrame({'ID': [customer_id], 'NAME': [name], 'E-MAIL': [email],'PHONE': [phone], 'CREATED': [date.today()], 'UPDATED': [date.today()]})
    updated_data = pd.concat([existing_data, new_data], ignore_index=True)
    updated_data.to_csv('./Library/customer.csv', index=False)

    existing_data2 = pd.read_csv('./Library/address.csv')
    street = input('Podaj ulice: ')
    city = input('Podaj miasto: ')
    country = input('Podaj kraj: ')
    new_data2 = pd.DataFrame({'ID': [customer_id], 'STREET': [street], 'CITY': [city], 'COUNTRY': [country]})
    updated_data2 = pd.concat([existing_data2, new_data2], ignore_index=True)
    updated_data2.to_csv('./Library/address.csv')
    print('Poprawnie dodano uzytkownika')