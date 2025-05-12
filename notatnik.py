users: list = [
    {"name": "Mateusz", "location": "Morąg", "posts": 0},

]
print(users)

def update_user(users_data: list)-> None:


    user_name=input("podaj imie uzytkownika którego dane chcesz zaktualizować: ")
    for user in users_data:
        if user["name"] == user_name:
            user["name"]= input("podaj nowe imię użytkownika: ")
            user["location"]= input("podaj nową lokalizację użytkownika: ")
            user["posts"]= int(input("podaj nową liczbę postów użytkownika użytkownika: "))



update_user(users)

print(users)