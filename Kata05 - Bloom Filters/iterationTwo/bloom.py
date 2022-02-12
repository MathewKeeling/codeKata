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

from hashlib import md5, sha1, sha256
from imghdr import tests

def getData(dictionary):
    dictionaryWords = sorted(open(dictionary, "r").read().splitlines())
    return dictionaryWords

def getMd5Hash(word):
    return int(md5(word.encode()).hexdigest(), 16)

def getSha1Hash(word):
    return int(sha1(word.encode()).hexdigest(), 16)

def getSha256Hash(word):
    return int(sha256(word.encode()).hexdigest(), 16)



        
# dictionary = getData("./iterationTwo/wordlist20k.txt")
dictionary = getData("./iterationTwo/wordlist20k.txt")
bit_vector_length = len(dictionary) * 2
bit_vector = [0] * bit_vector_length



for word in dictionary:
    bit_vector[getMd5Hash(word) % bit_vector_length] = 1
    bit_vector[getSha1Hash(word) % bit_vector_length] = 1 

# print(bit_vector)

testString = "edgezz"
if bit_vector[getMd5Hash(testString) % bit_vector_length] == 1:
    if bit_vector[getSha1Hash(testString) % bit_vector_length] == 1:
        if bit_vector[getSha256Hash(testString) % bit_vector_length] == 1:
            print("3 hash test:", testString, "is present in dictionary")
        else:
            print("3 hash test:", testString, "is not present in dictionary")
    else:
        print("3 hash test:", testString, "is not present in dictionary")
else:
    print("3 hash test:", testString, "is not present in dictionary")





if bit_vector[getMd5Hash(testString) % bit_vector_length] == 1:
    print("1 hash test:", testString, "is present in dictionary")
elif bit_vector[getMd5Hash(testString) % bit_vector_length] == 0:
    print("1 hash test:", testString, "is not present in dictionary")










