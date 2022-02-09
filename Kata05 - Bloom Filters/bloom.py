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

#  it would be cool to implement some sort of grafana thing where the data is graphed
#    sort of like the way that one commenter did...

import hashlib
import os


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
        # hashTable[hashlib.md5(c.encode('utf-8')).hexdigest()] = c


hashReduction = 10

dictionary = getData("wordlist.txt")
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

