users:list= [
{"name":"Mateusz","location":"Morąg","posts":0},
{"name":"Krzysztof","location":"Białobrzegi","posts":500},
{"name":"Maja","location":"Świecie","posts":300},
{"name":"Zuzia","location":"Radzyń_Podlaski","posts":700},
]

def get_user_info(users_data:list)->None:

    for user in users_data:
        print(f"twój znajomy  {user['name']} z miejscowości {user['location']} opublikował {user['posts']} postów")


get_user_info (users)
