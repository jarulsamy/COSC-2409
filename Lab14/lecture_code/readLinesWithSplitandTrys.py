#
# demo of readLines, split, and trys
#


def testItem(item):
    try:
        num = float(item)
        print(item + "   <<< is a valid number")
    except Exception as err:
        print(item + "   <<< is NOT a valid number")


def printItems(line):
    items = line.split()
    for i in range(len(items)):
        testItem(items[i])


def printList(theList):
    for i in range(len(theList)):
        print("Line #" + str((i + 1)) + " has items:")
        printItems(theList[i])


inFile = open("data.txt", "r")
lineList = inFile.readlines()
printList(lineList)
inFile.close()
