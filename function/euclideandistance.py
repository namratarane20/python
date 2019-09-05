#this program is used to calculate distance between two origins


from data import functional
try:
    x = int(input("enter the x value"))
    y = int(input("enter the y value"))
    functional.distance(x,y)                    # calling the method and passing the value
except ValueError:
    print("please provide inputs in int value")