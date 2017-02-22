import random
import matplotlib
import matplotlib.pyplot as plt

import time
import smallcodes as sc

'''
Function to represent rolling the dice.
'''
def rollDice():
    roll = random.randint(1, 100)

    if roll == 100:
        #print(roll, 'roll was 100, you lose. What are the odds?! Play again!')
        return False
    elif roll <= 50:
        #print(roll, 'roll was 1-50, you lose.')
        return False
    elif 100 > roll > 50:
        #print(roll, 'roll was 51-99, you win! *flashing lights! play more*')
        return True


'''
Making a more complicated bettor (Martingale Strategy)
'''

def dbl_bettor(funds,inital_wager,wager_count):
    global broke_count
    value = funds
    wager = inital_wager
    wX = []
    vY = []
    currentWager = 1

    # We will be betting on the previous outcome therefore, #
    previousWager = 'win'
    previousWagerAmount = inital_wager

    while currentWager <= wager_count:
        if previousWager == 'win':
            if rollDice():  #rollDice returned True
                value += wager
                wX.append(currentWager)
                vY.append(value)
            else:   #rollDice returned False
                value -= wager
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value < 0:
                    broke_count += 1
                    break
        elif previousWager == 'loss':
            #print('We lost last one, so we will be smart and dbl!')
            if rollDice():
                wager = previousWagerAmount * 2
                value += wager
                wager = inital_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount * 2
                #print('We lost', wager)
                value -= wager
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value < 0:
                    #print('We broke. Went broke after',currentWager,'bets')
                    broke_count += 1
                    break


        currentWager += 1

    #print(value)
    plt.plot(wX,vY)

'''
Adding some more statistics
'''
'''
xx = 0
broke_count = 0

while xx < 10:
    dbl_bettor(10000,100,1000)
    xx += 1

print('death rate:',(broke_count/float(xx)) * 100)
print('survival rate',100 - ((broke_count/float(xx)) * 100))

#dbl_bettor(10000,100,100)
plt.title('Double Up Results')
plt.xlabel('bets')
plt.ylabel('amount')
plt.axhline(0, color = 'r')
plt.show()
sc.stop() #stops code from here on out. Not interactive like IDL.

#time.sleep(555) #pauses code for set amount of seconds.
'''

'''
Simple Bettor, betting the same amount each time. The while loop rolls the dice wager_count times and adds or subtracts
from the bettor's funds.
'''
def simple_bettor(funds, initial_wager, wager_count):
    global broke_count
    value = funds
    wager = initial_wager

    wX = [] # wager X
    vY = [] # value y
    currentWager = 1  #wager count starting at one

    while currentWager <= wager_count: #Run while current wager is less than wager_count(here it is 100)=>run only 100 times
        if rollDice():
            value += wager  #If you win, add to funds
            wX.append(currentWager)
            vY.append(value)
            #print(value)
        else:
            value -= wager  #lose subtract bet from funds
            wX.append(currentWager)
            vY.append(value)
            #print(value)

            if value < 0:
                currentWager += 10000000000000
                broke_count += 1

        currentWager += 1

    plt.plot(wX, vY)

    #if value < 0:
    #   value = 'Broke!'
    #print('Funds:', value)

'''
Giving it a go. Roll the dice wager_count times (third entry). Being in the while loop says to show me the results for
100 trials.
'''
x = 0
broke_count = 0

while x < 1000:
    simple_bettor(10000, 100, 1000)
    x += 1
print(('death rate:', (broke_count/float(x)) * 100))
print(('survival rate:', 100 -(broke_count/float(x)) * 100))
plt.axhline(0,color = 'r')
plt.ylabel("Account Value")
plt.xlabel('Wager Count')
plt.title('MC Dice: 100 trials of length 1000')
plt.show()
