#this program is used to give the fewest notes in return for the amount entered by the user

from util import utility

try:

    notes = [1000, 500, 100, 50, 20, 10, 5, 2, 1]                 # values
    money = int(input("enter the amount to withdraw: "))
    utility.vending(notes, money)                        # calling the method
except ValueError:
    print("Input only accepts decimal numbers")