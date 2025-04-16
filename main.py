from utils.model import users
from utils.controller import  get_user_info


def main():
    while True:
        print("============MENU==============")
        print("0 - zakończ program")
        print("1 - pokaż co u znajomych")
        print("==============================")
        choice= input("wybierz opcję menu: ")
        if choice == "0":break
        if choice == "1": get_user_info



