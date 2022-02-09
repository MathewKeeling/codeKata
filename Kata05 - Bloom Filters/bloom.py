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