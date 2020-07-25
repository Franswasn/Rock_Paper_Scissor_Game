import random
di = {"r": "Rock", "p": "Paper", "s": "Scissor"}


def main ():
    num_of_chances = 1
    human_point = 0
    computer_point = 0
    print("****** Welcome to Rock Paper Scissor game ******")
    print('\nPress "q" to exit the game\n')

    chances = int(input ('How many guesess you want to make?: '))

    for key, value in di.items():
        print('press "',key,'" for', value)

    while num_of_chances <= chances:

        computer = random.choice(list(di.keys()))
        player = input('\nEnter your choice: ').lower()

        if player == "q" or player == "Q":
            exit()
        elif player == "r" or player == "p" or player == "s":

            print('                                             Your choice: ', di[player])
            print('                                             Computer choice: ', di[computer])

            if player == computer:
                print('\n                                               **Draw**')
            elif player == "r" and computer == "p":
                print("\n                                               **Computer wins**")
                computer_point = computer_point + 1
            elif player == "r" and computer == "s":
                print("\n                                               **Player wins**")
                human_point = human_point + 1
            elif player == "p" and computer == "s":
                print("\n                                               **Computer wins**")
                computer_point = computer_point + 1
            elif player == "p" and computer == "r":
                print("\n                                               **Player wins**")
                human_point = human_point + 1
            elif player == "s" and computer == "r":
                print("\n                                               **Computer wins**")
                computer_point = computer_point + 1
            elif player == "s" and computer == "p":
                print("\n                                               **Player wins**")
                human_point = human_point + 1
            print("\nChances left: ", chances - num_of_chances)
            num_of_chances += 1
        else:
            print('Invalid input. Try again')

    print("\nComputer point: ", computer_point,"  Human point: ", human_point)

    if computer_point > human_point:
        print("\n                                         ******************* COMPUTER WINS THE GAME ***************")
    if computer_point < human_point:
        print("\n                                          ********************* YOU WINS THE GAME *****************")
    if computer_point == human_point:
        print("\n                                          ************************THE GAME IS DRAW *****************")
    again = input('Play again ? "y" or "n": ')
    if again == "y":
        num_of_chances  = 1
    elif again == "n":
        exit()


    main()


main()

