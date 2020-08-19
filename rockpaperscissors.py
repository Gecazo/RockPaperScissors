import random
countD = 0 # Counter - Draw, Loose, Win
countL = 0
countW = 0
l = ['k','n','b'] # Random item - rock, scissors, paper
  
def inp(): # Number of turns
    global n
    while True:
        try:
            n = int(input('Enter an amount of games n '))
            return n
        except ValueError:
            print("It's not a number!")
  
  
def logic(x, y): # game logic
    global countD, countW, countL
        if x == y:
            print('Draw')
            countD += 1
        elif (x == 'k' and y == 'n') or (x == 'n' and y == 'b') or (x == 'b' and y == 'k'):
            print('Win')
            countW += 1
        else:
            print('Lose')
            countL += 1
        return countD, countL, countW
  
# start
inp()
while n != 0:
    while True:
        x = input('Rock (r), Scissors (s), Paper (p)')
        if x not in l:
            print('Enter r, s, p')
        else: break
  
    y = random.choice(l)
    logic(x, y)
    n -= 1
else:
    print('Wins - {0}\nLoses - {1}\nDraws- {2}'.format(countW, countL, countD))