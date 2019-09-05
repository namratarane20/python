from data import functional

try:
    stack = int(input("enter the stack amount :"))
    goal = int(input("enter the goal amount :"))
    number = int(input("enter how many times you want to play :"))
    if number > 0 and stack > 0:                        # condition
        functional.gambler(stack, goal, number)       # calling the method and passing the value of stack,goal,number
    else:
        print("enter more than 0")
except ValueError:
    print("enter the proper input")