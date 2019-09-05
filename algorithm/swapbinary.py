#this program is used to find the binary number and swap the binary number by using padding


from util import utility

try:
    num = int(input("enter the number :"))
    utility.swap(num)           # calls the method
except ValueError:
    print("ENTER THE INT VALUE")