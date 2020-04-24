myFile = open("Text.txt")
lines = myFile.readlines()
myFile.close()
for i in range(len(lines)):
    print(str(i) + ": " + lines[i])
