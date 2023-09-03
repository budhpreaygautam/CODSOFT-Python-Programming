def add(a, b):
    ans = a + b
    print(str(a) + " + " + str(b) + " = " + str(ans))


def sub(a, b):
    ans = a - b
    print(str(a) + " - " + str(b) + " = " + str(ans))


def mul(a, b):
    ans = a * b
    print(str(a) + " * " + str(b) + " = " + str(ans))


def div(a, b):
    ans = a / b
    print(str(a) + " / " + str(b) + " = " + str(ans))


while True:
    print("\n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Exit")
    choice = int(input("Enter the choice : "))

    if choice == 1:
        print("Your choice is Addition")
        a = int(input("Enter the Ist no. : "))
        b = int(input("Enter the IInd no. : "))
        add(a, b)

    elif choice == 2:
        print("Your choice is Subtractions")
        a = int(input("Enter the Ist no. : "))
        b = int(input("Enter the IInd no. : "))
        sub(a, b)

    elif choice == 3:
        print("Your choice is Multiplication")
        a = int(input("Enter the Ist no. : "))
        b = int(input("Enter the IInd no. : "))
        mul(a, b)

    elif choice == 4:
        print("Your choice is Division")
        a = int(input("Enter the Ist no. : "))
        b = int(input("Enter the IInd no. : "))
        div(a, b)
    elif choice == 5:
        exit()
    else:
        print("Enter the valid choice")
