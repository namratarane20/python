#this program is used to sort the given values by buble sort

from data import main
try:
    array = [int(x) for x in input("enter the elements: ").split()]
    if len(array) > 3:
        main.buble_sort(array)          # calling the method
    else:
        print("enter than more than 3 characters")

except ValueError:
    print("Input only accepts decimal numbers")