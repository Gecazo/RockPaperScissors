import random

count_draws = 0  # Counter - Draw, Loose, Win
count_loses = 0
count_wins = 0
TYPE_LIST = ('rock', 'scissors', 'paper')  # Items - rock, scissors, paper


def inp():  # Number of turns
    global n
    while True:
        try:
            n = int(input('Enter an amount of games n '))
            return n
        except ValueError:
            print("It's not a number!")


def logic(x, y):  # Game logic
    global count_draws, count_wins, count_loses
    if x == y:
        print('Draw')
        count_draws += 1
    elif (x == 'rock' and y == 'scissors') or (x == 'scissors' and y == 'paper') or (x == 'paper' and y == 'rock'):
        print('Win')
        count_wins += 1
    else:
        print('Lose')
        count_loses += 1
    return count_draws, count_loses, count_wins


# Start
inp()
while n != 0:
    while True:
        x = input('Choose your item: rock , scissors , paper ')
        if x not in TYPE_LIST:
            print('Enter rock, scissors, paper')
        else:
            break

    y = random.choice(TYPE_LIST)
    logic(x, y)
    n -= 1
else:
    print('Wins - {0}\nLoses - {1}\nDraws- {2}'.format(count_wins, count_loses, count_draws))
