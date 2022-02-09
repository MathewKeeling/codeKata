import array
from collections import defaultdict

# trash

def sortWords(toBeSorted):
    x = 0
    while x < len(toBeSorted):
        toBeSorted[x] = ''.join(sorted(toBeSorted[x]))
        x = x + 1
    return toBeSorted

# /trash

#   get all the words
#   sort all words by characters
#       apply all sorted words to a dictionary where the sorted word is the key
#       and the word itself is appended to the key value
#   provide a word
#   sort the word
#   return the key value(s) for the word


def getWords(wordlist):
    file = open(wordlist, "r")
    words = file.read().splitlines()
    print("Import Completed.\n")
    return words


def get_anagrams(words):
    d = defaultdict(list)
    for word in words:
        key = "".join(sorted(word))
        d[key].append(word)
    return d


wordlist = getWords("./resources/wordlist.txt")
anagramsDict = get_anagrams(wordlist)

# print(anagramsDict)

searchTerm = "".join(sorted("potato"))
print(anagramsDict[searchTerm])




