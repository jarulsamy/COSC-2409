#
#
# use of parallel lists and the index method
#
# read chapter 4, "Finding a Value in a List with the index() Method"
#
# We can create two lists that relate in parallel with each other.
# In other words, the ith item in one list is related to the ith item in the other
#
# in this script, I will have the user enter words. I will use one list to keep
# track of the words (no duplicates) and another to count the times words were entered
#
# you must use try-except blocks with the index method or it will cause an error
#
#
# first, create the two lists
words = []
counts = []
newWord = "go"  # just to get things rolling
while newWord != "stop":
    newWord = input('Enter a word ("stop" to end): ')
    try:  # must use a try to search for the new word, it bombs if not found
        i = words.index(newWord)  # returns the index of the newWord in words
        counts[i] += 1  # the word is there, so we up the count. This will
        # not be executed if not found
    except Exception as err:  # if the newWord is not found, we will add it
        words.append(newWord)  # same as words = words + [newWord]
        counts.append(1)  # adds a 1 onto the end of counts for this newWord

# outside the while loop, lets print the results
#
for i in range(len(words)):
    print(words[i] + " was entered " + str(counts[i]) + " times")
