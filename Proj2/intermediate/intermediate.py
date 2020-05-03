# Joshua Arulsamy
# Project 2 - Intermediate
# 05/03/2020
# COSC 2049 500

in_file = open("Scan.txt", "r")
out_file = open("IPLog.txt", "w")
line_count = 0
lineList = in_file.readlines()


def logIPs(lineList: list):
    for line in lineList:
        checkLine(line)


def clean_ip(ip: str):
    if ip[0] == "(":
        return ip[1:-1]
    return ip


def checkLine(line: str):
    items = line.split()

    if len(items) > 4 and items[0].lower() == "nmap":
        # If an extra column exists for hostname, increment index by 1
        if len(items) == 6:
            ip = clean_ip(items[5])
        else:
            ip = clean_ip(items[4])

        out_file.write(ip + "\n")

        global line_count
        line_count += 1


logIPs(lineList)

print(f"Line count: {line_count}")

in_file.close()
out_file.close()
