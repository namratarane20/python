#this program is used to find the day by using gregorian calender formula


from util import  utility
try:

    d = int(input("enter the date :"))
    m = int(input("enter the month :"))
    y = int(input("enter the year :"))
    if d < 32 and m < 13 and y > 0:                   # condition for day ,month and year
        utility.day(d, m, y)                # calling the method
    else:
        print("please give the correct date and month")
except ValueError:
    print("ENTER IN INT VALUES")