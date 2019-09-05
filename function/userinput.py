#this program is used replace the string with the given string

from data import functional

name = input("enter the username:")               # input for username
if len(name) < 3:                                 # if user name is less than 3 character it will give show the message
    print("enter more than 3 characters")
else:
    functional.username(name)                   # if user name has more than 3 character it will run the method
