# Our program is going do process the dictionary we used in previous kata, 
# this time looking for all six letter words which are composed of two 
# concatenated smaller words.
#
#    The first time, make program as readable as you can make it.

def getData(dictionary):
    file = open(dictionary, "r")
    fileContents = file.read()
    dictionaryWords = fileContents.splitlines()
    print("Import completed.\n")
    return dictionaryWords

def getWordsOfLength(words, length):
    wordsOfLength = []
    for word in words:
        if len(word) <= length:
            wordsOfLength.append(word)
    return wordsOfLength

words = getData(".\\resources\wordlist.txt")


sixLetterWords = getWordsOfLength(words, 6)
fiveOrLessLetterWords = getWordsOfLength(words, 5)

print("The Last Ten Six Letter Words: ")
print(sixLetterWords[-10:])

print("The Last Ten Five Or Less Letter Words: ")
print(fiveOrLessLetterWords[-10:])


    