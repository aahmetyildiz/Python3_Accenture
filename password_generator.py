import random

#Character groups in password
list_lowercase = "abcdefghijklmnopqrstuvwxyz"
list_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
list_number = "0123456789"
list_symbol = "._-+*&%"

#Password length
password_length = 8


#Function for append str's characters to a list.
def str_to_list(str, list):
    for i in range(len(str)):
        list.append(str[i])

    return list


#Function for generated password control. If OK return password else None.
def pass_control (password):
    #Control first character must not a symbol
    if password[0] in str_to_list(list_symbol, []):
        return None

    #Control uppercase, lowercase, number and symbol in password.
    else:
        ctrl_uppercase = 0
        ctrl_lowercase = 0
        ctrl_number = 0
        ctrl_symbol = 0

        #Count each character of password's group.
        for i in range(password_length):

            if list_uppercase.find(password[i]) >= 0:
                ctrl_uppercase += 1

            elif list_lowercase.find(password[i]) >= 0:
                ctrl_lowercase += 1

            elif list_number.find(password[i]) >= 0:
                ctrl_number += 1

            elif list_symbol.find(password[i]) >= 0:
                ctrl_symbol += 1

        #Control password character groups if OK return password else None
        if ctrl_uppercase == 0:
            return None

        elif ctrl_lowercase == 0:
            return None

        elif ctrl_number == 0:
            return None

        elif ctrl_symbol == 0:
            return None

        else:
            return password



while True:

    #Load character lists
    character_list = []
    character_list = str_to_list(list_lowercase, character_list)
    character_list = str_to_list(list_uppercase, character_list)
    character_list = str_to_list(list_number, character_list)
    character_list = str_to_list(list_symbol, character_list)

    #Generate password
    password = ""
    for i in range(password_length):
        password += random.choice(character_list)

    #Control password
    password = pass_control(password)

    if password is not None:
        print(password)
        break



