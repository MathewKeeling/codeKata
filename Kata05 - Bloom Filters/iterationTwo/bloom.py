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

from hashlib import md5, sha1
from imghdr import tests

def getData(dictionary):
    dictionaryWords = sorted(open(dictionary, "r").read().splitlines())
    print("Import completed.\n")
    return dictionaryWords

def getMd5Hash(word):
    return int(md5(word.encode()).hexdigest(), 16)

def getSha1Hash(word):
    return int(sha1(word.ecnode()).hexdigest(), 16)

def populateBitVector(array):
    bitValue = getMd5Hash(array) % len(dictionary)
    return bitValue
    
        
# dictionary = getData("./iterationTwo/wordlist20k.txt")
dictionary = getData("./iterationTwo/wordlist26.txt")
bit_vector = [0] * len(dictionary)


for word in dictionary:
    bit_vector[getMd5Hash(word) % len(dictionary)] = 1

# print(bit_vector)

testString = "ejehf"
if bit_vector[(getMd5Hash(testString) % len(dictionary))] == 1:
    print(testString, "is present in dictionary")
if bit_vector[(getMd5Hash(testString) % len(dictionary))] != 1:
    print(testString, "is not present in dictionary")

print(bit_vector)









