import random

end = False
user_points = 0
computer_points = 0

# while end == False:
while not end:
    options = ["rock", "paper", "scissors"]
    user_input = input("Enter the rock , paper ,scissors , or exit : ")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("Game Over")
        print("your total points " + str(user_points) + " and the computer points is " + str(computer_points))
        end = True

    if user_input == "rock":
        if computer_input == "rock":
            print("->It's Tie")
            print("Your input is " + str(user_input) + " and the computer is " + str(computer_input))
        elif computer_input == "paper":
            print("->Computer Win")
            print("Your input is " + str(user_input) + " and the computer is " + str(computer_input))
            computer_points += 1
        elif computer_input == "scissors":
            print("->You Win")
            print("Your input is " + str(user_input) + " and the computer is " + str(computer_input))
            user_points += 1
    elif user_input == "paper":
        if computer_input == "rock":
            print("->You Win")
            print("Your input is " + str(user_input) + " and the computer is " + str(computer_input))
            user_points += 1
        elif computer_input == "paper":
            print("->It's Tie")
            print("Your input is " + str(user_input) + " and the computer is " + str(computer_input))
        elif computer_input == "scissors":
            print("->Computer Win")
            print("Your input is " + str(user_input) + " and the computer is " + str(computer_input))
            computer_points += 1
    elif user_input == "scissors":
        if computer_input == "rock":
            print("->Computer Win")
            print("Your input is " + str(user_input) + " and the computer is " + str(computer_input))
            computer_points += 1
        elif computer_input == "paper":
            print("->You Win")
            print("Your input is " + str(user_input) + " and the computer is " + str(computer_input))
            user_points += 1
        elif computer_input == "scissors":
            print("->It's Tie")
            print("Your input is " + str(user_input) + " and the computer is " + str(computer_input))

    # elif user_input != "rock" or user_input != "paper" or user_input != "scissors" or user_input != "exit":
    #     print("invalid input")
