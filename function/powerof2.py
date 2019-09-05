#this program is used  to print the square table


from data import functional
try:
    number = int(input("enter the number "))
    if 0 <= number < 31:               # condition check
        functional.power(number)    # calls the method and pass the value
    else:
        print("enter the number between 0 to 31")
except Exception as e:
    print(e)