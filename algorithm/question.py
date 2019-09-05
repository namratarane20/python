#this program is used to find the number

from util import utility
import math
try:
    noOfTimes = int(input("How much time you want to ask the question:"))
    low = 0
    high = int(math.pow(2, noOfTimes))
    print("Think a number between(", low+1, ")to(", high, ")in range")
    print(utility.question(low, high))

except ValueError:
    print("ENTER THE INT VALUES")