#this program is used to find the square root of the number for given epsilon value

from util import utility
try:
    number = int(input("enter the value to find the square root: "))
    utility.sqrt(number)
except ValueError:
    print("ENTER THE INT VALUES")