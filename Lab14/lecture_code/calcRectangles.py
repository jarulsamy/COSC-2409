#
# demo of readLines, split, and trys
#
def getData(l, w):
    return (l * w), (l + w) * 2


def testItem(item):
    try:
        num = float(item)
        return True
    except Exception as err:
        return False


def checkItems(line):
    items = line.split()
    if len(items) == 2:
        if not testItem(items[0]) or not testItem(items[1]):
            print(line + " has an invalid item")
        else:
            area, perimeter = getData(float(items[0]), float(items[1]))
            print(line + "   Area: " + str(area) + "   Perimeter: " + str(perimeter))
    else:
        print(line + " does not have two items")


def calcList(theList):
    for i in range(len(theList)):
        checkItems(theList[i])


#
# start of main program
#
inFile = open("rectangles.txt", "r")
print("Calculating information on rectangles\n********************\n")
recList = inFile.readlines()
calcList(recList)
inFile.close()
