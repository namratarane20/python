#this program is used to find prime number within the given range of numbers from user


from util import utility
try:
    start = int(input("enter from where you want to find prime number :"))
    stop = int(input("enter till where you want to find prime number :"))
    if start > -1 and stop < 1002:              # condition
        utility.prime(start, stop)           # calls the method
    else:
        print("enter number between 0-1000")
except ValueError:
    print("ENTER THE NUMBERS")
