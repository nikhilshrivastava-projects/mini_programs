import random

# Simple program to play rock, scissor and page game
# The program is using infinite while loop hence it will keep running indefinately until the user closes it or exits

while(True):
    print('\nEnter: \n')
    print('1 - For Rock\n')
    print('2 - For Paper\n')
    print('3 - For Scissor\n')

    choice = int(input("Enter 1, 2  or 3 : "))
    selection = ''
    if choice == 1:
        selection = 'Rock'
    elif choice == 2:
        selection = 'Paper'
    else:
        selection = 'Scissor'

    print('You have selected {}'.format(selection))
    computer_choice = random.randint(1, 3)
    if computer_choice == 1:
        selection = 'Rock'
    elif computer_choice == 2:
        selection = 'Paper'
    else:
        computer_choice = 'Scissor'
    print('Computer has selected {}'.format(selection))

    if choice == computer_choice:
        print("Draw")
    elif choice == 1:
        if computer_choice == 2:
            print("Computer Won - It selected Paper")
        else:
            print("You Won - - You selected  Scissor")
    elif choice == 2:
        if computer_choice == 1:
            print("You Won, - You selected Rock")
        else:
            print("Computer Won - It selected Scissor")
    elif choice == 3:
        if computer_choice == 1:
            print("Computer Won, - It selected Rock")
        else:
            print("You Won, - You selected Paper")