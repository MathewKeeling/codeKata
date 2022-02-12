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
        if len(word) >= 2:
            if len(word) <= length:
                wordsOfLength.append(word)
    return wordsOfLength

def getWordComposition(word):
    x = 0
    compound = []
    while x <= len(word):
        if word[0:x+1] in fiveOrLessLetterWords:
            if word[x+1:] in fiveOrLessLetterWords:
                string = "First:", {word[0:x+1]} , "Second:", {word[x+1:]}
                compound.append(string)
                x = len(word) + 1
            else:
                x = x + 1
        else:
            x = x + 1
    return compound
    
        
        

words = getData(".\\resources\wordlist.txt")
sixLetterWords = getWordsOfLength(words, 6)
fiveOrLessLetterWords = getWordsOfLength(words, 5)

testWord = "sixteen"
test = getWordComposition(testWord)
sixLetterWordsCompositions = {}
sixLetterWordsCompositions[testWord] = getWordComposition(testWord)

print("The word is: ", testWord)
print(sixLetterWordsCompositions[testWord])

for word in sixLetterWords:
    sixLetterWordsCompositions[word] = getWordComposition(word)

