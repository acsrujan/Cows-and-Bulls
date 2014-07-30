from random import randint


def Stats(number, guess):
    numList = map(int, str(number))
    guessList = map(int, str(guess))
    n_bulls = []

    for i in range(0, 4):
        n_bulls.append(numList[i] - guessList[i])

    Bull = n_bulls.count(0)
    Cow = len([i for i in numList if i in guessList]) - Bull

    return '%dB,%dC' % (Bull, Cow)

def NoDup(num):
    if len(num) == len(set(num)) and num[0] is not '0':
        return int(num)

def Rand_num():
    while True:
        randNum = NoDup(str(randint(1023, 9876)))
        if randNum is not None:
            break
    return randNum

def enter_num():
    while True:
        userNumber = NoDup(raw_input('Your Guess: '))
        if userNumber is not None and str(userNumber).isdigit() and len(str(userNumber)) == 4:
            break
    return userNumber

def start_game():
    print "I chose my number."
    return Rand_num()


def main():
    randNum = start_game()
    output = '0'

    while output[0] is not '4':
        guess = enter_num()
        output = Stats(randNum, guess)
        print output

    print "You won, Congrats!"

main()
