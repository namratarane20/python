#this program is used to find the percentage of head and tail by generating random numbers


from data import functional

try:
    no = int(input("enter the no of times coin to flip :"))         # input
    if no > 0:
        functional.flipcoin(no)                                 # if the input is more than 0 than method will run
    else:
        print("enter more than 0")                              # if the input is less than 0 it will show the message
except ValueError:
    print("Input only accepts decimal numbers")   # if the input is not in numerical it will throw the error message