dataFile = open("ftemps.txt", "r")
resultFile = open("ctemps.txt", "w")
lines = dataFile.readlines()
for i in range(len(lines)):
    f = float(lines[i])
    c = (f - 32) * (5.0 / 9.0)
    resultFile.write(str(c) + "\n")

dataFile.close()
resultFile.close()
