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

#  after running a test, I am now convinced that I am not sure what this 
#    program is even doing. The array containing the hashes and words is smaller
#    in size than even the bitvector of 12x dictionary length of iterationTwo
#    something is wrong... need to do more digging
#
#  if this were a pure "does x = x?" while x is stored in memory, the false positive
#    rate would not be as high as it is:
#
#  Result of test:
#    Words:  20000
#    Bit_Vector Length: N/A
#    Size of Dictionary Array:  0.000232 Megabytes
#    False Positives:  18657
#    False Positives Percent:  93.285
#
#  ...It's tough to tell for my ignorance.
#    but I am guessing that in its current implementation it is actually working
#      as a bloom filter


import hashlib
from random import shuffle
from hashlib import md5, sha1, sha256
import sys


def getData(dictionary):
    dictionaryWords = []
    f = open(dictionary, "r")
    file_contents = f.read()
    dictionaryWords = file_contents.splitlines()
    print("Import completed.\n")
    return dictionaryWords

def getHash(array):
    for c in array:
        hash = hashlib.md5(c.encode('utf-8')).hexdigest()
        hash = hash[0:hashReduction]
        hashTable[hash] = c

def shuffle_word(word):
    word = list(word)
    shuffle(word)
    return ''.join(word)


hashReduction = 0
dictionary = getData("./iterationTwo/wordlist20k.txt")
hashTable = {}

getHash(dictionary)


#  check to see if the word is present
print("Lenth of Dictionary: " + str(len(dictionary)))
print("Length of Bloom Filter: " + str(len(hashTable)))
print("Number of collisions: " + str(len(dictionary) - len(hashTable)))

word = input("Please supply a word: ")
hashedWord = hashlib.md5(word.encode('utf-8')).hexdigest()
hashedWord = hashedWord[0:hashReduction]

if hashedWord in hashTable:
    print(word + " is a correctly spelled word.")
elif hashedWord not in hashTable:
    print(word + " is not a correctly spelled word.")



falsePositive = 0

for word in dictionary:
    word = shuffle_word(word)
    if word not in dictionary:
        if hashedWord in hashTable:
            falsePositive = falsePositive + 1
        else:
            pass
    else:
        pass


print("Words: ", len(dictionary))
print("Bit_Vector Length: N/A",)
print("Size of Dictionary Array: ", (sys.getsizeof(hashTable) / 1000000) ,"Megabytes")
print("False Positives: ", falsePositive)
print("False Positives Percent: ", ((falsePositive / len(dictionary) * 100) ))

