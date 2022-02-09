# starting points:
#  https://brilliant.org/wiki/hash-tables/
#  https://en.wikipedia.org/wiki/Hash_table 


# add value to hash map
#
#   You create a new key/value pair on a dictionary by assigning a value to that key
#   d = {'key': 'value'}
#   print(d)  # {'key': 'value'}
#   d['mynewkey'] = 'mynewvalue'
#   print(d)  # {'key': 'value', 'mynewkey': 'mynewvalue'}
#
#   If the key doesn't exist, it's added and points to that value. If it 
#       exists, the current value it points to is overwritten.


# 2022/02/08 21:17

import hashlib

def strToMD5(string):

    print()

sourceInformation = [ "alpha", "bravo", "charlie", "delta", "echo" ]

hashTable = {}

for c in sourceInformation:
    hashTable[hashlib.md5(c.encode('utf-8')).hexdigest()] = c


#  print(hashTable)

testWord = "pizza"
print("The word", testWord, "is in the dictionary: ",
    hashlib.md5(testWord.encode('utf-8')).hexdigest() in hashTable)

testWord = "echo"
print("The word", testWord, "is in the dictionary: ",
    hashlib.md5(testWord.encode('utf-8')).hexdigest() in hashTable)





