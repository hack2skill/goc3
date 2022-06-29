import os
import time

def history(num1 , num2, calc):
    my_file = open("history.txt", "a")
    my_file = my_file.write(str(num1) + " " + user_input + " " + str(num2) + " = " + calc + "\n")

def timer():
    time.sleep(1)
    print("")
    print("--------------------------------------------------------------------------")

while True:
    print("enter '+' for addition:")
    print("enter '-' for subtraction:")
    print("enter '*' for multiplication:")
    print("enter '/' for division:")
    print("Enter 'h' to check history:")
    print("enter 'quit' to end the program:")
    user_input = input("-->")

    if user_input == 'quit':
        break

    elif user_input =='+':
        print("")
        num1 = float(input("enter first number:"))
        num2 = float(input("enter first number:"))
        sum = str(num1+num2)
        print("")
        print("The sum is " + sum)

        history(num1, num2, sum)
        timer()

    elif user_input =='-':
        print("")
        num1 = float(input("enter first number:"))
        num2 = float(input("enter first number:"))
        diff = str(num1 - num2)
        print("")
        print("The difference is " + diff)

        history(num1,num2,diff)
        timer()

    elif user_input=='*':
        print("")
        num1 = float(input("enter first number:"))
        num2 = float(input("enter first number:"))
        product = str(num1 * num2)
        print("")
        print("The product is " + product)

        history(num1,num2,product)
        timer()

    elif user_input=='/':
        print("")
        num1 = float(input("enter first number:"))
        num2 = float(input("enter first number:"))
        div = str(num1 / num2)
        print("")
        print("The division is " + div)

        history(num1,num2,div)
        timer()

    elif user_input=='h':
        my_file = open("history.txt", "r")
        print("")
        print(my_file.read())
        timer()

    else:
        print("Unknown input!")
