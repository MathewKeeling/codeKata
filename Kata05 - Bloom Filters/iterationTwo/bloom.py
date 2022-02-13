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

#  attempt 2

#---Scramble Test---
#Words:  20000
#Bit_Vector Length:  20000 (1x)
#False Positives:  13891
#False Positives Percent:  69.455

#---Scramble Test---
#Words:  20000
#Bit_Vector Length:  40000 (2x)
#False Positives:  7430
#False Positives Percent:  37.15

#---Scramble Test---
#Words:  20000
#Bit_Vector Length:  60000 (3x)
#False Positives:  4453
#False Positives Percent:  22.264999999999997

#---Scramble Test---
#Words:  20000
#Bit_Vector Length:  240000 (12x)
#Size of Bit_Vector: 1.920056 Megabytes
#False Positives:  420
#False Positives Percent:  2.1


from email.policy import default
from random import shuffle
from hashlib import md5, sha1, sha256
import sys


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
bit_vector_length = len(dictionary) * 12
bit_vector = [0] * bit_vector_length

#  populate bitmap
for word in dictionary:
    bit_vector[getMd5Hash(word) % bit_vector_length] = 1
    bit_vector[getSha1Hash(word) % bit_vector_length] = 1 


#  test for false negatives
trueWords = 0
falseNegative = 0
testString = "strange"

for word in dictionary:
    if word in dictionary:
        if bit_vector[getMd5Hash(word) % bit_vector_length] == 1:
            if bit_vector[getSha1Hash(word) % bit_vector_length] == 1:
                trueWords = trueWords + 1
            else:
                falseNegative = falseNegative + 1
        else:
            falseNegative = falseNegative + 1
    else:
        pass

print("True words: ", trueWords)
print("falseNegatives: ", falseNegative)
print("Words passed: ", trueWords)

print("\n---Scramble Test---")


falsePositive = 0

for word in dictionary:
    word = shuffle_word(word)
    if word not in dictionary:
        if bit_vector[getMd5Hash(word) % bit_vector_length] == 1:
            if bit_vector[getSha1Hash(word) % bit_vector_length] == 1:
                falsePositive = falsePositive + 1
            else:
                pass
        else:
            pass
    else:
        pass


print("Words: ", len(dictionary))
print("Bit_Vector Length: ", bit_vector_length)
print("Size of Bit_Vector:", (sys.getsizeof(bit_vector) / 1000000) ,"Megabytes")
print("False Positives: ", falsePositive)
print("False Positives Percent: ", ((falsePositive / len(dictionary) * 100) ))











