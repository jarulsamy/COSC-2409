#
# demo of readLines and split
#


def printItems(line):
    items = line.split()
    for i in range(len(items)):
        print(items[i])


def printList(theList):
    for i in range(len(theList)):
        print("Line #" + str((i + 1)) + " has items:")
        printItems(theList[i])


inFile = open("data.txt", "r")
lineList = inFile.readlines()
printList(lineList)
inFile.close()
