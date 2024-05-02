import bookfun
import login
import customerfun

def main():
    while(True):
        logged = login.login()
        if(logged == 'admin'):
            break
        
    while(True):
        print('Co chcesz zrobic?\n1) Dodaj Ksiazke do bazy\n2) Usun ksiazke z bazy po numerze ID\n3) Usun ksiazke z bazy po tytule\n4) Dodaj nowego klienta do bazy\n5) Usun klienta z bazy po ID\n6) Usun klienta z bazy po imieniu\n8) Wyjdz')
        selection = int(input('Wybierz numer odpowiadajacy danej funkcji: '))
        if(selection == 1):
            bookfun.add_book()
        elif(selection == 2):
            book_id = int(input('Podaj ID ksiazki: '))
            bookfun.remove_book_id(book_id)
        elif(selection == 3):
            bookfun.remove_book()
        elif(selection == 4):
            customerfun.add_customer(customerfun.random_id)
        elif(selection == 5):
            customer_id = int(input('Podaj ID klienta: '))
            customerfun.remove_customer(customer_id)
        elif(selection == 6):
            customer_name = input('Podaj imie klienta: ')
            customerfun.remove_customer_name(customer_name)
        elif(selection == 8):
            break
        else:
            print('Niepoprawny numer funkcji')

if __name__ == '__main__':
    main()
