choice = 1
while choice == 1:

    try:
        num = float(input("Enter a number: "))
        print("The number you entered is: " + str(num))
    except Exception as err:
        print("The number you entered is NOT a number! ")

    choice = int(input("Enter 1 to do it again, 0 to stop: "))
