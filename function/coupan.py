#this program is used  to find the distinct counts  to generate the random numbers within


from util import utility

try:

    a = int(input("enter how many coupon numbers you want to generate :"))
    if a > 0:
        utility.coupan_revised(a)                  # calling the method and passing the value
    else:
        print("enter positive number")
except ValueError:
    print("ENTER THE INT VALUE")