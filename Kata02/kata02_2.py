#  Binary chop method to find index of a given integer in an array of ints
#  Make five different methods
#
#

#  method(int, array_of_int)
#    if int exists   
#      return(index_of_int)
#    if int dne
#      return(-1)

#  attempt two
#  recursive version

def chop(low, high, array, x):
    
    if low <= high:
        mid = (low + high) // 2

        if x == array[mid]:
            return mid
        
        elif x > array[mid]:
            return chop(mid + 1, high, array, x)
        
        elif x < array[mid]:
            return chop(low, mid - 1, array, x)

    else:
        return -1



array_of_ints = [0, 1, 2, 3, 4, 5, 42, 99, 109, 209, 403]

print("The array is: ")
print("0, 1, 2, 3, 4, 5, 42, 99, 109, 209, 403")

print("Please provide a number.")
int = int(input())

result = chop(0, len(array_of_ints) - 1, array_of_ints, int)

if result != -1:
    print("The element is present at index #: ", result)

if result == -1:
    print("The integer " + str(int) + " is not present in the array.")