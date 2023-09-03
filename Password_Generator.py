import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%&*")


def pass_gen():
    pass_len = int(input("Enter the length of password : "))
    random.shuffle(characters)
    password = []
    for i in range(pass_len):
        password.append(random.choice(characters))

    random.shuffle(password)
    password = "".join(password)
    print("Your generated password : ", password)

option = input("Do you want to generate the password (Y/N) : ")

if option == 'Y' or option == 'y':
    pass_gen()
elif option == 'N' or option == 'n':
    print("You are going to exits from this program")
    quit()
else:
    print("Wrong choice, please choose the valid choice")
    option = input("Do you want to generate the password (Y/N) : ")
