number = 7

while True:
    guess = int(input("Guess a number between 1 and 10 : "))

    if guess == number:
        print('you guesses it')
        break
