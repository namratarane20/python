# code for binary search


def binary(list, item):
    first = 0
    last = len(list) - 1
    found = False  # initialization
    while first <= last and not found:
        mid = (first + last) // 2  # dividing the list in two and searching the element
        # if mid value is equal to item it will return true here itself
        if item == list[mid]:
            found = True
        else:
            if item > list[mid]:  # if item is more than the middle value in the list than make
                # first element as next to the mid element(+1) and last element as last
                first = mid + 1
            else:
                last = mid - 1  # if item is less than mid element than the
                # last element is updated to the less than mid element

    return found


def buble_sort(array):
    for i in range(len(array)-1,0,-1):  # for outer loop
        for j in range(i):  # for inner loop
            if array[j] > array[j + 1]:
                temp = array[j]  # swapping of elements0
                array[j] = array[j + 1]
                array[j + 1] = temp
    print("sorted array ", array)  # printing the sorted array


# code for the insertion sort


def insertion(nlist):
    for i in range(1, len(nlist)):

        currentvalue = nlist[i]
        position = i

        while position>0 and nlist[position-1]>currentvalue:
            nlist[position]=nlist[position-1]
            position = position-1

            nlist[position]=currentvalue
        print(nlist)