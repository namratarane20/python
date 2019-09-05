#this program is used check the given input year is leap or not


from data import functional

try:
    year = int(input("enter the year :"))
    if year > 0:
        functional.leap(year)           # calling the method and passing the value
    else:
        print("please enter the proper year")
except ValueError:
    print("enter the values in int")