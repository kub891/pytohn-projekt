import bookfun
import login
import customerfun

def main():
    while(True):
        logged = login.login()
        if(logged == 'admin'):
            break
        
    while(True):
        print('Co chcesz zrobic?\n1) Dodaj Ksiazke do bazy\n2) Usun ksiazke z bazy po numerze ID\n3) Usun ksiazke z bazy po tytule\n4)Dodaj nowego uzytkownika do bazy\n8)Wyjdz')
        selection = int(input('Wybierz numer odpowiadajacy danej funkcji: '))
        if(selection == 1):
            bookfun.add_book()
        elif(selection == 2):
            book_id = int(input('Podaj ID ksiazki: '))
            bookfun.remove_book_id(book_id)
        elif(selection == 3):
            book_title = input('Podaj tytul ksiazki: ')
            bookfun.remove_book_title(book_title)
        elif(selection == 4):
            customerfun.add_customer()
        elif(selection == 8):
            break
        else:
            print('Niepoprawny numer funkcji')

if __name__ == '__main__':
    main()
