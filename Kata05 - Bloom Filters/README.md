# codeKata
Working through http://codekata.com/blog/archives/

#### Note 2022/02/11
* I realized that I did this problem incorrectly.
* I've only just come to grasp what a Hash Table is much less a bloom filter.
* I need to redo this and use a bitmap / bit vector that is ~330k long, and flip bits 0 and 1 to represent the words. Not store the words themselves in the hashmap.
* I'll get back to this.

#### Note 2022/02/12
* I'm revisiting this to give it another go using a bitmap

#### Note 2022/02/12
What is clear is:

The bigger the bit_vector / bitmap, the less likely you are to receive false positives.
The more hashes against which you test, the less likely you are to receive false positives.

Should implement a method to test against an iterative completely accurate method to generate a likelihood of false positivity against one factor, the other, and both.
