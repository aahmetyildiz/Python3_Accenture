#Class for random PC choice
import random


#Define variables for score
user_score = 0
pc_score = 0
values = ['r','p','s']

#Function for control user input
def input_control (user_input):
    if user_input in values :
        if user_input == 'r':
            print('You choose "Rock"')

        elif user_input == 'p':
            print('You choose "Paper"')

        else:
            print('You choose "Scissors"')
        #If user choose valid value write choice and return input
        return user_input

    else:
        print('Please write valid character. Write "r" for Rock, "p" for Paper, "s" for Scissors.')
        # If user choose invalid value return fail
        return 'fail!'


#Function for random pc choice
def pc_choice():
    pc_rnd = random.choice(values)
    return pc_rnd


#Function for match choices
def match(user, pc):
    if  user == "r" and pc == "s":
        print("Rock smashes Scissors. You win!")
        return "user"

    elif  user == "s" and pc == "r":
        print("Rock smashes Scissors. PC win!")
        return "pc"

    elif user == "s" and pc == "p":
        print("Scissors cut Paper. You win!")
        return "user"

    elif user == "p" and pc == "s":
        print("Scissors cut Paper. PC win!")
        return "pc"

    elif user == "p" and pc == "r":
        print("Paper wraps Rock. You win!")
        return "user"

    elif user == "r" and pc == "p":
        print("Paper wraps Rock. PC win!")
        return "pc"

    else:
        print("Equality")
        return "eq"


#Game continue in a loop since user exit.
while True:

    # Print a blank row for separate rounds.
    print("")

    #Define user input and control its validity with input_control() function defined before. user_value define as result of control
    user_input = input('What\'s your choice? Write "r" for Rock, "p" for Paper, "s" for Scissors:')
    user_value = input_control(user_input)

    #user input not valid error message write at input_control function and loop go to start again.
    if user_value == 'fail!':
        continue

    else:

        #If user input is valid first random pc choice generated.
        pc_value = pc_choice()

        if pc_value == 'r':
            print('PC choose "Rock"')

        elif pc_value == 'p':
            print('PC choose "Paper"')

        else:
            print('PC choose "Scissors"')

        #User and PC choices compare with match() function. It return the winner (user, pc, eq)
        winner = match(user_value, pc_value)


        #Score board change with return value of match
        if winner == "pc":
            pc_score += 1

        elif winner == "user":
            user_score += 1

        else:
            pc_score += 0
            user_score += 0

        print("Score, You: "+str(user_score)+" - PC: "+str(pc_score))













