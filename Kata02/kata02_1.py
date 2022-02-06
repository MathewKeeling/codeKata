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
    length = len(array)
    low = array[0]
    mid = array[floor(length/2)]
    high = array[-1]

    




array_of_ints = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 42]

chop(66, array_of_ints)