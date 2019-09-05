import math
import random

# program for anagram

def anag(l, l1):
    if sorted(l) == sorted(l1):     # sorting the elements because to compare the elements
                                    # for anagram have to sort and check the elements
        print("it is anagram")
    else:
        print("it is not anagram")


# program for prime number
arr = []  # to store prime numbers in int
arr1 = []  # to store the prime number in string


def prime(start, stop):
    for num in range(start, stop + 1):      # outer loop
        isboolean = True                    # boolean value
        for i in range(2, num):             # inner loop
            if (num % i) == 0:
                isboolean = False
                break                       # if boolean value is false it will break the loop

        if isboolean:
            arr.append(num)                 # if it is prime than the number will be added to list(arr[])

    arr1 = [str(i) for i in arr]            # list comprehension converting the arry to string
    print("prime numbers", arr1)
    kir(arr1)  # calling the method


def palin(arr):
    array_palindrome = []
    for i in range(2, len(arr), 1):              # LOOP
        rev = temp = number = 0                  # initialization
        number = arr[i]                          # storing the value from list one by one
        temp = number                            # storing the number to temp ,to compare.
        while number > 0:                        # loop
            last = number % 10
            rev = rev * 10 + last
            number = number // 10
        if temp == rev:                             # condition
            array_palindrome.append(temp)
    print("palindrome numbers", array_palindrome)


def arr_(arr1):
    arr2 = []                                        # empty list to store the anagram elements
    for i in range(len(arr1)):                      # outer loop
        for j in range(i + 1, len(arr1), 1):        # innerloop
            if sorted(arr1[i]) == sorted(arr1[j]):
                arr2.append(arr1[i])                # adding the anagram element to list
                arr2.append(arr1[j])                # adding the anagram element to list
            else:
                pass
    print("anagram number", arr2)

    palin(arr)


def question(low, high):
    if (high - low) == 1:
        return low
    mid = int(high + low) // 2
    print('Is your number less than', mid, '?. press 1 to YES or 0 to NO:')
    a = int(input())
    if a == 1:
        return question(low, mid)
    elif a == 0:
        return question(mid, high)
    else:
        print("Invalid input.. ")
        return 0

# merge sort


def merge_sort(lst):
    if len(lst) <= 1:                   # if length size is 0 or 1 it will return the value
        return lst

    mid = int(len(lst) / 2)              # dividing the list and seperating
    left = merge_sort(lst[:mid])         # adding the values to left
    right = merge_sort(lst[mid:])        # adding the values to right
    return merge(left, right)            # passing the values to the method


def merge(left, right):
    result = []                                     # empty list to store  elements
    i, j = 0, 0                                     # initialization
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result

# vending machine


def vending(notes, money):
    rem = 0
    total = 0                                           # initialization
    while money > 0:                                    # condition
        for i in range(0, len(notes), 1):               # loop
            if money >= notes[i]:
                number = money // notes[i]
                rem = money % notes[i]
                money = rem
                total += int(number)
                print(notes[i], "Notes------->", number)
        vending(notes, money)
        print("Total number of notes is", total)


# day of week


def day(d, m, y):
    y0 = y - (14 - m) // 12
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = m + 12 * ((14 - m) // 12) - 2
    day1 = (d + x + 31 * m0 // 12) % 7          # calculation
    if day1 == 0:
        print("its sunday")
    elif day1 == 1:
        print("its monday")
    elif day1 == 2:
        print("its tuesday")
    elif day1 == 3:
        print("its wednesday")
    elif day1 == 4:
        print("its thursday")
    elif day1 == 5:
        print("its friday")
    elif day1 == 6:
        print("its saturday")
    else:
        print("invalid")


def monthly_payment(principal,year,roi):
    n = 12*year
    r = roi/(12*100)
    numerator = principal*r
    denominator = 1-pow((1+r),(-n))
    payment = numerator/denominator       # calculation
    print(payment)


def fahreheit(value):
    fah=(value*9 / 5)+32                # calculation
    print(fah)


def celsius(value):
    cel=(value-32)*5/9                  # calculation
    print(cel)


def sqrt(num):
    temp = num
    epsilon = 1e-15
    while math.fabs(temp - num / temp) > epsilon * temp:
        temp = ((num / temp + temp) / 2)        # calculation
    print("SquareRoot is:", temp)


def bin_ary(num):
    array=[]
    while num > 0:
        temp = num % 2                              # storing remainder
        num = num//2                              # getting quotient value
        array.append(temp)                      # adding remainder values to list
    array.reverse()                             # reversing the list
    print("binary number is", array)
    for n in range(len(array), 8):               # padding
        array.append(0)
    print(array)


def swap(num):
    array=[]
    result=[]
    while num > 0:
        temp = num % 2                              # storing the remainder
        num = num//2                              # getting quotient value
        array.append(temp)
    array.reverse()
    print("binary number",array)

    up = 0
    last = len(array)
    mid = up+last//2
    left = array[:mid]                # divided list merged to left
    right = array[mid:]               # divided list merged to right
    print("divided array1", left)
    print("divided array2", right)
    total=right+left                # adding the list
    print("swapped array is",total)


def coupan(n):
    arr = []
    count = 0
    while(len(arr)) < n:
        x=random.randint(1, n)           # generating the random numbers from 1 to 9
        count += 1                        # increment
        if x not in arr:                # to skip the duplicate values
            arr.append(x)               # adding the values to arr->list
    print(sorted(arr))
    print("distinct counts",count)


board = [1, 2, 3, 4, 5, 6, 7, 8, 9]                   # slots for board

win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
# win combinations in board


def draw():
    # this method is used to print the board
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])
    print()


def p1():
    # this method is used to give the input from user
    n = choose_number()                             # calls the method
    if board[n] == "X" or board[n] == "O":          # checks the slot whether the input is give before
        print("\nYou can't go there. Try again")
        p1()                                        # if input is given before it again calls the method
    else:
        board[n] = "X"                              # input is given to particular slot from user


def p2():
    n = random.randint(0, 8)                         # random number is generated from user
    if board[n] == "X" or board[n] == "O":          # checks the slot whether the input is give before
        print("\nYou can't go there. Try again")
        p2()                                        # if input is given before it again calls the method
    else:
        board[n] = "O"                             # input is given to particular slot generated from random number


def choose_number():
    while True:
        a = input()     # takes the input
        try:
            a = int(a)
            a -= 1           # decrements the value by 1 because list starts from index number 0
            if a in range(0, 9):
                return a
            else:
                print("\nThat's not on the board. Try again")
                continue
        except ValueError:
            print("\nThat's not a number. Try again")
            continue


def check_board():
    # this method is used to check the winning combinations
    count = 0
    for i in win_combinations:
        if board[i[0]] == board[i[1]] == board[i[2]] == "X":    # checks the winning combination
            print("Player 1 Wins!\n")
            print("Congratulations!\n")
            return True

        if board[i[0]] == board[i[1]] == board[i[2]] == "O":    # checks the winning combination
            print("Player 2 Wins!\n")
            print("Congratulations!\n")
            return True
    for a in range(9):
        if board[a] == "X" or board[a] == "O":
            count += 1
        if count == 9:                                         # if board is full it will exit by returning the value
            print("The game ends in a Tie\n")
            return True
            
