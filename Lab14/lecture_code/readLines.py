#
# demo of readLines
#
def printList(theList):
    for i in range(len(theList)):
        print(theList[i])


inFile = open("data.txt", "r")
lineList = inFile.readlines()
printList(lineList)
inFile.close()
