import random
import numpy as np
import math
import time


def username(name):
    print("hello", name, "how are you")  # printing the username

#  --------------------------------------------------------------------------------------------------------

# flip of coin


def flipcoin(no):
    heads = 0
    tails = 0                         # intialization
    for x in range(no):
        x = random.random()           # taking random variable for random value to flip a coin
        if x < 0.5:                  # if the x is less than 0.5 than its tails
            tails += 1
        else:                       # if x is more than 0.5 than its heads
            heads += 1
    totalnoheads = heads
    totalnotails = tails
    print("total no of heads",totalnoheads)
    print("total no of tails",totalnotails)
    print("percentage of heads",(totalnoheads/no)*100)
    print("percentage of tails",(totalnotails/no)*100)

#  ------------------------------------------------------------------------------------------------------------# -
# program to print the leap year


def leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:  # condition check leap year
        print("it is leap year")
    else:
        print("it is not leap year")
#  ---------------------------------------------------------------------------------------------------------------
# program to print power of 2


def power(number):
    i = 0
    while i <= number:                    # it will iterate the loop till i<=number
        print(i, "-", pow(2, i))
        i += 1
#  ---------------------------------------------------------------------------------------------------------------
#harmonic

def harmonic(value):
    sum_ = 0
    for i in range(1, value, 1):          # USING LOOP TO ITERATE THE VALUES
        sum_ = sum_+1/i
    print(sum_)
# -----------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------
# gambler


def gambler(stack, goal, no_of_times):
    bets = 0
    wins = 0
    loss=0                                      # Initialization

    for i in range(no_of_times):

        while 0 < stack < goal:                # checks cash is greater than 0 and less than goal amount
            bets += 1                           # Increment bets
            if random.random() < 0.5:            # if value of random function less than 0.5
                stack += 1                       # Increment cash by 1
            else:
                stack -= 1                       # decrement cash by 1
    if stack == goal:
        wins += 1                                 # If cash== goal increment wins by 1
    else:
        loss += 1

    print(wins, " wins of ", no_of_times)
    print(loss,"loss of", no_of_times)
    print("Percent of games won =", 100.0 * wins / no_of_times)               # print wining in percent
    print("percent of games loss =", 100.0 * loss/ no_of_times)
#  --------------------------------------------------------------------------------------------------------------
#   coupan number


def count(array_):
    count = 0
    while (len(array_) >0):              # loop
        x=random.randint(1,9)           # generating random numbers from 1 to 9
        count += 1                        # incrementing the count
        if x in array_:                  # condition
            array_.remove(x)             # if x value is present in array it will remove that value
            print(array_)

    print("total random number to have all distinct codes", count)
#  --------------------------------------------------------------------------------------------------------------------
#  2d array


def array(row, column):
    arr = [[0 for i in range(row)] for j in range(column)]
    for i in range(column):
        for j in range(row):
            arr[i][j] = int(input("entered elements:"))     # int element
            array_ = np.array(arr)
    print(array_)
# ---------------------------------------------------------------------------------------------------------
# triplets


def triple( array_ ):
    n=len(array_)
    count =0
    for i in range(0, n-2, 1):                # from 1st element to last third element
        for j in range(i+1, n-1,1):          # from 2nd element to last second element
            for k in range(j+1, n, 1):        # from 3rd element to last element
                if (array[i] +array[j] + array[k]==0):
                    count+=1                 # increment
                print(array[i], " ", array[j], " ", array[k], " ")
    print("number of triplets found in the above list   is", count)
    if count == 0:
        print("no triplets found")
# --------------------------------------------------------------------------------------------------------------
#euclidean distance

def distance(x, y):
    z=math.sqrt(x*x+y*y)    # using math number of mathematical operations can be performed
    print("euclidean distance value of", x, "and", y, "is", z)
#  ---------------------------------------------------------------------------------------------------
#  start and stop program


def start_time():
    t0=time.time()                          # taking the time1
    t1=time.time()                          # taking the time2
    print("start time is", t0)
    print("stopped time is ", t1)
    t2=t1-t0                                # calculating the difference between two times
    print("elapsed time is ", t2)
#  -------------------------------------------------------------------------------------------------------------
#  quadratic function


def quadraticFunctions (a, b, c):
    print("Given quadratic equation is:", a, "x^2 +", b, "x + ", c)
    d = (b * b) - (4 * a * c)
    if d > 0:                             # if d is more than 0 than 2 roots are present
        print("Roots are real and unequal")
        root1 = (-b + math.sqrt(d)) / (2 * a)
        root2 = (-b - math.sqrt(d)) / (2 * a)
        print("First Root ", root1)
        print("Second Root ", root2)

    elif d == 0:                          # if d is equal to 0 than only one root is present
        print("Roots are real and equal")
        root1 = (-b + math.sqrt(d)) / (2 * a)
        print("First Root ", root1)

    else:
        print("Root are imaginary")
# -----------------------------------------------------------------------------------------------------------
# windchill


def wind(t,v):
    w = (355.74 + 0.6215 * t + (.4275 * t - 35.75)) * pow(v, 0.16)      # calculation
    print(w)
#  ---------------------------------------------------------------------------------------------------------
#temperature

def fahreheit(value):
    fah=(value*9 / 5)+32            # calculation
    print(fah)


def celsius(value):
    cel=(value-32)*5/9              # calculation

#  ------------------------------------------------------------------------------------------------------------
#factors

def fact(n):
    p = 2                 # because factorisation starts from 2
    while n > p:
        if n % p == 0:
            print(p)
            n = n//p      # storing the  quotient value
        else:
            p += 1
    print(n)
