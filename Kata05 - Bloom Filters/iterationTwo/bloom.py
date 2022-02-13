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

#---Scramble Test---
#Words:  20000
#Bit_Vector Length:  20000 (1x)
#Size of Bit_Vector: 0.00258 Megabytes
#False Positives:  13972
#False Positives Percent:  69.86
#Real Positives:  4704
#Real Words Skipped:  1324

#---Scramble Test---
#Words:  20000
#Bit_Vector Length:  200000
#Size of Bit_Vector: 0.02508 Megabytes
#False Positives:  626
#False Positives Percent:  3.1300000000000003
#Real Positives:  18009
#Real Words Skipped:  1365

from email.policy import default
from random import shuffle
from hashlib import md5, sha1
import sys
from bitarray import bitarray

def getData(dictionary):
    dictionaryWords = sorted(open(dictionary, "r").read().splitlines())
    return dictionaryWords
def getMd5Hash(word):
    return int(md5(word.encode()).hexdigest(), 16)
def getSha1Hash(word):
    return int(sha1(word.encode()).hexdigest(), 16)
def shuffle_word(word):
    word = list(word)
    shuffle(word)
    return ''.join(word)

# dictionary = getData("./iterationTwo/wordlist20k.txt")
dictionary = getData("./iterationTwo/wordlist20k.txt")
bit_vector_length = len(dictionary) * 10
bit_vector = bitarray(bit_vector_length)
bit_vector.setall(0)


#  populate bitmap
for word in dictionary:
    bit_vector[getMd5Hash(word) % bit_vector_length] = 1
    bit_vector[getSha1Hash(word) % bit_vector_length] = 1 

realWord = 0
skippedWord = 0
falsePositive = 0

for word in dictionary:
    word = shuffle_word(word)
    if word not in dictionary:
        if bit_vector[getMd5Hash(word) % bit_vector_length] == 1:
            if bit_vector[getSha1Hash(word) % bit_vector_length] == 1:
                falsePositive = falsePositive + 1
            else:
                skippedWord = skippedWord + 1
        else:
            skippedWord = skippedWord + 1
    else:
        realWord = realWord + 1
    
print("\n---Scramble Test---")
print("Words: ", len(dictionary))
print("Bit_Vector Length: ", bit_vector_length)
print("Size of Bit_Vector:", ((sys.getsizeof(bit_vector) / 1000000)) ,"Megabytes")
print("False Positives: ", falsePositive)
print("False Positives Percent: ", ((falsePositive / len(dictionary) * 100) ))
print("Real Positives: ", skippedWord)
print("Real Words Skipped: ", realWord)







