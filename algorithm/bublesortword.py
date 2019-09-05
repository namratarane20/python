#this program is used load the file and do sorting using buble sort


from data import main
try:
    file = open('number', 'r')                # opening the file
    str_ = file.read()                         # reading the text and storing it into the object
    split_array = str_.split()     # splitting the words to store the elements in array using sorted inbuilt function
    main.buble_sort(split_array)            # calling the method
except FileNotFoundError:
    print("FILE NOT FOUND")