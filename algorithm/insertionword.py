#this program is used to load the file and read the values and perform insertion sorting of the values

from data import main

try:
    file = open('wordlist','r')                    # opening the file
    str_ = file.read()                              # read the text and storing in object
    split_array = str_.split()                      # splitting the array to list
    main.insertion(split_array)                     # calling the method
except FileNotFoundError:
    print("FILE NOT FOUND")