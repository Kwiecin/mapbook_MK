def get_user_info(users_data: list) -> None:
    for user in users_data:
        print(f"twój znajomy  {user['name']} z miejscowości {user['location']} opublikował {user['posts']} postów")
    users: list = [
        {"name": "Mateusz", "location": "Morąg", "posts": 0},

    ]
    print(users)

    def add_user(users_data: list) -> None:
        user_name = input("podaj imię nowego użytkowanika: ")
        user_location = input("podaj lokalizację nowego znajomego: ")
        user_posts = int(input("podaj liczbę postów znajomego: "))
        users_data.append({"name": user_name, "location": user_location, "posts": user_posts})

    add_user(users)

    print(users)
