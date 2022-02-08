#  the task described in this portion of the kata is to refactor the code into
#    two smaller programs and "shared functionality."
# 
#  Using creative license, I am interpeting "shared functionality" as a third program
#    capable of solving either problem given either data set.
#
#  the only thing this implementation lacks is a switching capability to choose
#    whether you are using the football formatted .dat or the weather formatted .dat
#
#  I don't think that's within the scope of the goal of this kata... short of me learning
#    how data architecture works... to the degree that I could make a model of the 
#    data and really dig into all that...
#      I am going to do all of that... just not now.

#  anyway: here are the methods from the last program that are greatly improved as 
#    compared to how they existed when I initially solved both part 1 and part 2


#  TL;DR, my work was done for me by the time I got here, so here are the resultant
#    methods from my work. One minor modification: changed 'scores' variable to 'array'

import numpy
import os

def getValue(line, firstColumn, lastColumn):
    lineSelected = array[line]
    if lineSelected[3] == "-":
        return -1
    elif lineSelected[3] != "-":
        value = lineSelected[firstColumn:lastColumn]
        value = value.strip("* -")
    return value

def getMaxValue(arrayOne, arrayTwo):
    scoredDifference = numpy.subtract(arrayOne,arrayTwo)
    scoredDifference = scoredDifference.tolist()
    max_value = max(scoredDifference)
    max_index = scoredDifference.index(max_value)
    return max_index


array = []
