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

def getWordsOfMaxLength(words, length):
    wordsOfLength = []
    for word in words:
        if len(word) >= 2:
            if len(word) <= length:
                wordsOfLength.append(word)
    return wordsOfLength

def getWordsExactLength(words, length):
    wordsExactLength = []
    for word in words:
        if len(word) == length:
            wordsExactLength.append(word)
    return wordsExactLength

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
    

words = sorted(getData(".\\resources\wordlist20k.txt"))
sixLetterWords = getWordsExactLength(words, 6)
fiveOrLessLetterWords = getWordsOfMaxLength(words, 5)


testWord = "sixteen"
test = getWordComposition(testWord)
sixLetterWordsCompositions = {}
sixLetterWordsCompositions[testWord] = getWordComposition(testWord)

print("The word is: ", testWord)
print(sixLetterWordsCompositions[testWord])

print(sixLetterWords)

for word in sixLetterWords:
    
    sixLetterWordsCompositions[word] = getWordComposition(word)
    if sixLetterWordsCompositions[word] == []:
        pass
    else:
        print(word)
        print(sixLetterWordsCompositions[word])

