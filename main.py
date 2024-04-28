import bookfun

def main():
    print('Co chcesz zrobic?\n1) Dodaj Ksiazke do bazy\n2) Usun ksiazke z bazy po numerze ID\n3) Usun ksiazke z bazy po tytule')
    selection = int(input('Wybierz numer odpowiadajacy danej funkcji: '))
    if(selection == 1):
        bookfun.add_book()
    elif(selection == 2):
        book_id = int(input('Podaj ID ksiazki: '))
        bookfun.remove_book_id(book_id)
    elif(selection == 3):
        book_title = input('Podaj tytul ksiazki: ')
        bookfun.remove_book_title(book_title)


if __name__ == '__main__':
    main()
