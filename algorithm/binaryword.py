#this program is used  load a file and search a value by   using binary search

from data import main
try:
    item = input("enter the word which you want to find ")  # taking input which word to find
    open_file = open('wordlist', 'r')                        # command to open file
    read_file = open_file.read()                            # command to read the file
    splited_list = read_file.split()                        # splitting the word ang taking the words in list
    list_ = sorted(splited_list)                             # sorting the list to do binary search
    print(list_)                                           # printing the sorted list
    print(main.binary(list_, item))                          # calling the method
except FileNotFoundError:
    print("FILE NOT FOUND")