import time

n = 5
while n > 0:
    print("Hello there!")
    time.sleep(2)


    while True:
        line = input('What will you like me to do for you? > ')
        if line == 'Nothing':
            break
        print("processing, please wait for some seconds...")
        time.sleep(5)
        print(line, "?, am sorry, I can't do that...")
        time.sleep(3)
        print(".")
        time.sleep(2)
        print("..")
        time.sleep(2)
        print("...")
        time.sleep(2)
        print('Will you like anything else?, if not...')
        time.sleep(2)
        print("Thanks for your time")
