#this program is used to do the sorting of values by merge sort

from util import utility
try:
    lst = [int(x) for x in input("enter the number with space ").split()]
    print(utility.merge_sort(lst))              # calls the method nad prints the output
except ValueError:
    print("ENTER THE INT VALUES")