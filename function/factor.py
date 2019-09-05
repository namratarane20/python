#this program is used to find the factors of the given number

from data import functional
try:
    number = int(input("enter the number :"))
    functional.fact(number)          # calling the method and passing the value
except ValueError:
    print("Input only accepts decimal numbers")