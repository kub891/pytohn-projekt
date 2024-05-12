def login():
    correct_username = "admin"
    correct_password = "admin"
    
    username = input("Podaj login: ")
    password = input("Podaj haslo: ")
    
    if username == correct_username and password == correct_password:
        print("Zalogowano pomyslnie!")
        return username
    else:
        print("Niepoprawny login lub haslo. Sprobuj ponownie.")
