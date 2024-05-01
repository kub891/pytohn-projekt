def login():
    correct_username = "admin"
    correct_password = "admin"
    
    username = input("Podaj login: ")
    password = input("Podaj hasło: ")
    
    if username == correct_username and password == correct_password:
        print("Zalogowano pomyślnie!")
        return username
    else:
        print("Niepoprawny login lub hasło. Spróbuj ponownie.")
