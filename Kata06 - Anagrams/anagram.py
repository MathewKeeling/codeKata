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


def print_anagrams(words):
    d = get_anagrams(wordlist)
    for key, anagrams in d.items():
        if len(anagrams) > 1:
            print(key, anagrams)

wordlist = getWords("./resources/wordlist.txt")





