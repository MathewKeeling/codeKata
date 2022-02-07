#  Binary chop method to find index of a given integer in an array of ints
#  Make five different methods
#
#

#  method(int, array_of_int)
#    if int exists   
#      return(index_of_int)
#    if int dne
#      return(-1)

#  attempt one

from array import array
from math import floor


def chop(int, array):
    low = 0
    high = len(array) -1
    mid = 0

    while low <= high: 
        mid = (high + low) // 2

        if array[mid] < int:
            low = mid + 1
        
        elif array[mid] > int:
            high = mid -1
        
        else:
            return mid
        
    return -1


array_of_ints = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 42]

result = chop(6, array_of_ints)

print(result)