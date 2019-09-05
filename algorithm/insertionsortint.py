#this program is used  to do the sorting of given elements by insertion sorting


from data import main
try:
    nums = [int(x) for x in input("enter the elements ").split()]
    if len(nums) > 3:                     # condition
        main.insertion(nums)            # calls the method
    else:
        print("enter than more than 3 numbers")
except ValueError:
    print("Input only accepts decimal numbers")