import random
import matplotlib
import matplotlib.pyplot as plt

import time
import smallcodes as sc

"""Chirp"""

# Globally define some variables to be used with multiple bettor strategies
samplesize = 1000  # How many individual trials
startingFunds = 10000
wagerSize = 100
wagerCount = 100  # Length of individual trial

# Values to beat to be better than dbl_bettor in bust and profit
lower_bust = 31.235
higher_profit = 63.208


def rollDice():
    """
    Function to represent rolling the dice. House wins if roll 100 or 1-50. You win if roll between 51 and 99.
    """

    roll = random.randint(1, 100)

    if roll == 100:
        return False
    elif roll <= 50:
        return False
    elif 100 > roll > 50:
        return True


def multiple_bettor(funds, initial_wager, wager_count):
    """
    A bettor of a different multiple than 2. Used to determine which combination of betting is better.
    """
    global multiple_busts
    global multiple_profits
    value = funds
    wager = initial_wager
    wX = []
    vY = []
    currentWager = 1
    previousWager = 'win'
    previousWagerAmount = initial_wager

    while currentWager <= wager_count:
        if previousWager == 'win':
            if rollDice():  # rollDice returned True
                value += wager
                wX.append(currentWager)
                vY.append(value)
            else:  # rollDice returned False
                value -= wager
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value <= 0:
                    multiple_busts += 1
                    break
        elif previousWager == 'loss':
            if rollDice():
                wager = previousWagerAmount * random_multiple

                if (value - wager) < 0:
                    wager = value

                value += wager
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount * random_multiple
                if (value - wager) < 0:  # Making it so we bet all that was left. Can't go negative.
                    wager = value
                value -= wager
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value <= 0:
                    multiple_busts += 1
                    break

        currentWager += 1

    # print(value)
    #plt.plot(wX, vY, color)
    if value > funds:
        multiple_profits += 1



def dbl_bettor(funds, initial_wager, wager_count, color):
    """
    Making a more complicated bettor (Martingale Strategy). Double your wager when you lose and go back to original
    wager when you win again.
    """

    global dbl_busts  # Adding to see which method make more money/loses more
    global dbl_profits
    value = funds
    wager = initial_wager
    wX = []
    vY = []
    currentWager = 1
    previousWager = 'win'  # We are betting on the previous outcome. Assume start with a win.
    previousWagerAmount = initial_wager

    while currentWager <= wager_count:
        if previousWager == 'win':
            if rollDice():  # rollDice returned True
                value += wager
                wX.append(currentWager)
                vY.append(value)
            else:  # rollDice returned False
                value -= wager
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value <= 0:
                    dbl_busts += 1
                    break
        elif previousWager == 'loss':
            # print('We lost last one, so we will be smart and dbl!')
            if rollDice():
                wager = previousWagerAmount * 2

                if (value - wager) < 0:
                    wager = value

                value += wager
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount * 2
                # print('We lost', wager)
                if (value - wager) < 0:  # Making it so we bet all that was left. Can't go negative.
                    wager = value
                value -= wager
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value <= 0:
                    dbl_busts += 1
                    break

        currentWager += 1

    # print(value)
    #plt.plot(wX, vY, color)
    if value > funds:
        dbl_profits += 1



def simple_bettor(funds, initial_wager, wager_count, color):
    """
    Simple Bettor, betting the same amount each time. The while loop rolls the dice wager_count times and adds or subtracts
    from the bettor's funds.
    """

    global simple_busts
    global simple_profits
    value = funds
    wager = initial_wager
    wX = []  # wager X
    vY = []  # value y
    currentWager = 1  # wager count starting at one

    while currentWager <= wager_count:  # Run while currentWager is less than wagerCount (defined with global variables)
        if rollDice():
            value += wager  # If you win, add to funds
            wX.append(currentWager)
            vY.append(value)
            # print(value)
        else:
            value -= wager  # lose subtract bet from funds
            wX.append(currentWager)
            vY.append(value)
            # print(value)

            if value <= 0:
                simple_busts += 1
                break


        currentWager += 1

    plt.plot(wX, vY, color)
    if value > funds:
        simple_profits += 1



''' Determine which multiple gives a better result for both higher_profit and lower_bust out of 100,000 samples. The MC
is what gives us the final multiple. You need to visually determine the answer from the output. MC keeps going in either
direction. Does not look closer to the so far best value.'''
x = 0

while x < 10000:

    multiple_busts = 0.0
    multiple_profits = 0.0
    multiple_sampleSize = 1000
    currentSample = 1

    random_multiple = random.uniform(0.1, 10.0)

    while currentSample <= multiple_sampleSize:
        multiple_bettor(startingFunds, wagerSize, wagerCount)
        currentSample += 1

    if ((multiple_busts/multiple_sampleSize)*100.00 < lower_bust) and ((multiple_profits/multiple_sampleSize)*100.00 > higher_profit):
        # try and make one number J = win- bust and then export that output to a list and plot J vs random number use
        # the .append to add those values to the new array. i.e


        '''winner = random_multiple
        bust_rate = (multiple_busts/multiple_sampleSize)*100.00
        profit_rate = (multiple_profits/multiple_sampleSize)*100.00
        winner_bust = bust_rate
        winner_profit = profit_rate'''

        print("###############")
        print("Found a winner, the multiple was:", random_multiple)
        print('Lower bust to beat', lower_bust)
        print('Higher profit rate to beat:', higher_profit)
        print('Bust rate:',(multiple_busts/multiple_sampleSize)*100.00)
        print('Profit rate:', (multiple_profits/multiple_sampleSize)*100.00)
        print('###############')
        '''if winner:                                                       #Trying to figure out how to make it narrow
            random_multiple += random.uniform(0.01,0.05)                        the range once you know a good value.
            print("###############")
            print("Found a winner, the multiple was:", random_multiple)
            print('Lower bust to beat', lower_bust)
            print('Higher profit rate to beat:', higher_profit)
            print('Bust rate:', (multiple_busts / multiple_sampleSize) * 100.00)
            print('Profit rate:', (multiple_profits / multiple_sampleSize) * 100.00)
            print('###############')
        else:
            pass'''
    else:
        pass
        '''print("###############")
        print("Found a loser, the multiple was:", random_multiple)
        print('Lower bust to beat', lower_bust)
        print('Higher profit rate to beat:', higher_profit)
        print('Bust rate:',(multiple_busts/multiple_sampleSize)*100.00)
        print('Profit rate:', (multiple_profits/multiple_sampleSize)*100.00)
        print('###############')'''

    x += 1



# ------------ NOT USING ANYMORE --------------
# ---------------------- Previously -----------------------------------------
''' Adding some more statistics to track losses v wins '''

'''
xx = 0
broke_count = 0   # this is no longer in the code, replaced by dbl_bust and simple_busts
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


# ------------------------------ Previously in  section -----------------------
''' Giving it a go for simple_bettor. Roll the dice wager_count times (third entry). Being in the while loop says to
show me the results for 100 trials. '''

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
'''


# ---------------- From Analyzing Monte Carlo results section ------------------------
'''Now run with both bettors to compare which is better.'''

'''
x = 0
simple_busts = 0.0
dbl_busts = 0.0
simple_profits = 0.0
dbl_profits = 0.0
while x < samplesize:
    simple_bettor(startingFunds, wagerSize, wagerCount, 'k')  # K is black for matplotlib
    #simple_bettor(startingFunds, wagerSize * 2, wagerCount, 'g')
    dbl_bettor(startingFunds, wagerSize,wagerCount, 'b')
    x += 1
print('Simple Bettor Bust Chances:', (simple_busts/samplesize)*100.00)
print('Double Bettor Bust Chances:', (dbl_busts/samplesize)*100.00)
print('Simple Bettor Profit Chances:', (simple_profits/samplesize)*100.00)
print('Double Bettor Profit Chances:', (dbl_profits/samplesize)*100.00)
plt.axhline(0, color='r')
plt.ylabel('Account value')
plt.xlabel('Wager Count')
plt.show()
'''
