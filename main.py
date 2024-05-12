import bookfun
import login
import customerfun
import borrow_fun

def main():
    while(True):
        logged = login.login()
        if(logged == 'admin'):
            break
        
    while(True):
        print('Co chcesz zrobic?\n1) Dodaj Ksiazke do bazy\n2) Usun ksiazke z bazy (ID/Nazwa)\n3) Dodaj nowego klienta do bazy \n4) Usun klienta z bazy (ID/Imie)\n5) Wypozycz ksiazki ID\n6) Zwroc ksiazki \n8) Wyjdz')
        selection = int(input('Wybierz numer odpowiadajacy danej funkcji: '))
        if(selection == 1):
            bookfun.add_book()
        elif(selection == 2):
            bookfun.remove_book()
        elif(selection == 3):
            customerfun.add_customer(customerfun.random_id)
        elif(selection == 4):
            identifier = input('Podaj ID lub imie klienta: ')
            customerfun.remove_customer(identifier)
        elif(selection == 5):
            customer_id = input("Podaj ID klienta: ")
            book_ids = input("Podaj ID ksiazek (oddzielone przecinkami): ").split(",")
            borrow_fun.borrow_books(customer_id, book_ids)
        elif(selection == 6):
            customer_id = input("Podaj ID klienta: ")
            returned_book_ids = input("Podaj ID zwracanych ksiazek (oddzielone przecinkami): ").split(",")
            borrow_fun.return_books(customer_id, returned_book_ids)
        elif(selection == 8):
            break
        else:
            print('Niepoprawny numer funkcji')

if __name__ == '__main__':
    main()
