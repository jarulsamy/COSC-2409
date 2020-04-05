def hello(num):
    print("Number " + str(num))
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.\n')

count = 1
times = int(input("How many greetings do you wish? "))
while count <= times:
    hello(count)
    count += 1
