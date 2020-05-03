# Joshua Arulsamy
# Project 2 - Basic
# 05/03/2020
# COSC 2049 500

in_file = open("Scan.txt", "r")
out_file = open("IPLog.txt", "w")
line_count = 0
lineList = in_file.readlines()


def logIPs(lineList: list):
    for line in lineList:
        checkLine(line)


def checkLine(line: str):
    items = line.split()
    if len(items) > 0:
        if items[0].lower() == "nmap":
            out_file.write(line)
            # Global is kinda hacky.
            # A better way would be to use returns.
            global line_count
            line_count += 1


logIPs(lineList)

print(f"Line count: {line_count}")

in_file.close()
out_file.close()
