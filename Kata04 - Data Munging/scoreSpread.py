# The file football.dat contains the results from the English Premier League 
# for 2001/2. The columns labeled ‘F’ and ‘A’ contain the total number of goals 
# scored for and against each team in that season (so Arsenal scored 79 goals against 
# opponents, and had 36 goals scored against them). Write a program to print the 
# name of the team with the smallest difference in ‘for’ and ‘against’ goals.

#  Columns F and A
#  Total number of goals scored for and against each team in the season.
#  Write a program to print the name of the team w/ the smallest difference
#    between for and against goals.

#  Name: Columns 08 - 23 (index 07 - 22)
#  For:  Columns 44 - 45 (index 43 - 44)
#  Against: Columns 51 - 52 (index 50 - 51)



import numpy
import os

def getValue(line, firstColumn, lastColumn):
    lineSelected = scores[line]
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

os.system('cls' if os.name == 'nt' else 'clear')

myfile = open("data_files\\football.dat")
scores = myfile.readlines()
myfile.close()

teamNames = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
scoredFor = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
scoredAgainst = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


x = 1
while x < 21:
    result = getValue(x, 44, 45)
    if result == -1:
        scoredFor[x-1] = -1
        scoredAgainst[x-1] = -1
        teamNames[x-1] = -1
        x = x + 1
    else:
        scoredFor[x-1] = int(getValue(x, 43, 45))
        scoredAgainst[x-1] = int(getValue(x, 50, 52))
        teamNames[x-1] = str(getValue(x, 7, 23))
        x = x + 1

print("The team with the greatest spread is: " + teamNames[getMaxValue(scoredFor, scoredAgainst)])

#  debug lines
#  print("Debug: scoredFor: ")
#  print(scoredFor)
#  print("Debug: scoredAgainst: ")
#  print(scoredAgainst)
#  print("Debug: teamNames: ")
#  print(teamNames)

#  print("Debug: Spread: ")
#  scoredDifference = numpy.subtract(scoredFor,scoredAgainst)
#  scoredDifference = scoredDifference.tolist()
#  print(scoredDifference)
