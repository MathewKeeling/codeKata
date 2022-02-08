#  Part One: Weather Data
#  
#  In weather.dat you’ll find daily weather data for Morristown, NJ for June 2002. 
#
#  Write a program to output the day number with the smallest temperature spread 
#    Column one: Day
#    Column two: maximum temperature
#    Column three: minimum temperature
#        

#  Days:              03 04
#  Temperature (max): 07 08 09 10
#  Temperature (min): 13 14 15 16
#  Lines: 3 - 32


def getIntValue(line, firstColumn, lastColumn):
    lines = weather[line]
    value = lines[firstColumn:lastColumn]
    value = value.strip("* ")
    return int(value)


myfile = open("data_files\\weather.dat")
weather = myfile.readlines()
myfile.close()

#  would be cool to learn how to do array "broadcasting" or dynamic sizing
maximumNumber = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
minimumNumber = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
spread = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

x = 2
while x < 32:
    maximumNumber[x-2] = getIntValue(x, 6, 9)
    x = x + 1


x = 2
while x < 32:
    minimumNumber[x-2] = getIntValue(x, 12, 16)
    x = x + 1

x = 0
while x < 30:
    spread[x] = maximumNumber[x] - minimumNumber[x]
    x = x + 1

max_value = max(spread)
max_index = spread.index(max_value)
max_index_day = max_index + 1
print("\nDebug: Day with highest temperature spread: " + str(max_index_day))





#print("\nDebug: ", "Minimum Temperatures: ")
#print(min)


#print("\nDebug: ", "Maximum Temperatures: ")
#print(max)

#print("\nDebug: ", "Spread: ")
#print(spread)






