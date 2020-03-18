import random

list_lovercase = "abcdefghijklmnopqrstuvwxyz"
list_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
list_number = "0123456789"
list_symbol = "._-+*&%"
password_length = 8



def str_to_list(str, list):
    for i in range(len(str)):
        list.append(str[i])

    return list



def pass_control (password):
    ctrl = 0

    #First character must not symbol
    if password[0] in str_to_list(list_symbol, ""):
        return None

    else:

        return password



while True:
    character_list = []
    character_list = str_to_list(list_lovercase, character_list)
    character_list = str_to_list(list_uppercase, character_list)
    character_list = str_to_list(list_number, character_list)
    character_list = str_to_list(list_symbol, character_list)

    password = ""
    for i in range(password_length):
        password += random.choice(character_list)


    if password is not None:
        print(password)
        break