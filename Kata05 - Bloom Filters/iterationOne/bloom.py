#  Kata05 - Bloom Filters
#  Starting work on this 2022/02/08 @ 18:34
# 
#  Kata05 - Bloom Hash
#  So, this kata is fairly straightforward. Implement a Bloom filter based spell
#    checker. You’ll need some kind of bitmap, some hash functions, and a simple way 
#    of reading in the dictionary and then the words to check. For the hash function, 
#    remember that you can always use something that generates a fairly long hash 
#    (such as MD5) and then take your smaller hash values by extracting sequences 
#    of bits from the result. 

#  this is done incorrectly. But that's not all bad. It is going to serve as the example
#    case for how much space can be saved by using a bloom filter compared with
#    storing the whole dictionary in memory
#  That speaks not to speed but memory requiresments.
#  This will be the very worst case, because not only is the word itself stored...
#    but also the hash is stored.

#
#  Result of test:
#    ---Scramble Test--- 4.3 seconds
#    Words:  20000
#    Bit_Vector Length: N/A
#    Size of Dictionary Array:  0.58992 Megabytes
#    False Positives:  0
#    False Positives Percent:  0.0

#  Tough to figure out what to make of this. Dictionary array is smaller in size..
#    and the false positivity rate is zero. It's also 2 seconds faster.
#    is this a better design? Or have I implemented something that is not a bloom
#      filter?

#  I have learned a lot since I last worked on this... so I am going to refactor
#    hoping that will provide greater clarity

#  PROBLEM SOLVED... after an hour or two (3) of sleuthing
#  I've discovered the problem. I've been using lists for my bitmap...
#    lists are a horribly space inefficient way to store 100s of 1000s of 0s and 1s
#    .... i've learned so much--I guess that's cool.
#    with lists as a bitmap, I erased all of the RAM savings over what I'm doing here

#  Basically: what is below is FASTER than a sequential lookup, becuase it is 
#    using a hashmap.
#  But: It is significantly larger than a bitmap bloom filter
#  While this has 100% accuracy, it has to store 589kB of data in RAM.
#  The Bloom Filter has 97% accuracy and only has to store 25kB of data in RAM
#    That is 1/20 the amount of storage in RAM.
#    Depending on need for accuracy, it can be 100s of time smaller

import hashlib
from random import shuffle
import sys

def getData(dictionary):
    dictionaryWords = sorted(open(dictionary, "r").read().splitlines())
    return dictionaryWords
def getHash(array):
    for c in array:
        hash = hashlib.md5(c.encode('utf-8')).hexdigest()
        hashTable[hash] = c
def shuffle_word(word):
    word = list(word)
    shuffle(word)
    return ''.join(word)

hashTable = {}
dictionary = getData("./iterationTwo/wordlist20k.txt")
getHash(dictionary)

falsePositive = 0
realWord = 0
for word in dictionary:
    word = shuffle_word(word)
    if word not in dictionary:
        if hashlib.md5(word.encode('utf-8')).hexdigest() in hashTable:
            falsePositive = falsePositive + 1
        else:
            pass
    else:
        if word in dictionary:
            realWord = realWord + 1

print("---scramble test---")
print("Words: ", len(dictionary))
print("Bit_Vector Length: N/A",)
print("Size of Dictionary Array: ", (sys.getsizeof(hashTable) / 1000000) ,"Megabytes")
print("False Positives: ", falsePositive)
print("False Positives Percent: ", ((falsePositive / len(dictionary) * 100) ))
print("Real Words Count: ", realWord)


