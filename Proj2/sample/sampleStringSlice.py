#
# Demo of String slices and indexing
#
# Strings may be indexed and sliced like lists. Read the section
# about this in chapter 6
#
# if a variable called stuff is a string, it has indecies from 0 to len - 1
#
# so, if word = 'Hello'
#    len(word) is 5
#    word[0] is 'H'
#    word[1] is 'e'
#    word[2] is 'l'
#    word[3] is 'l'
#    word[4] is 'o'
#    word[5] is an error (index out of range)
#
#    a slice is a substring starting at the first index, and stopping before the last
#
#    word[2:4] is 'll'
#

word = "Hello"
print("Length: " + str(len(word)))
print("first: " + word[0])
print("last: " + word[len(word) - 1])
print("Slice: " + word[2:4])
