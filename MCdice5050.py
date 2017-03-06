import random
import matplotlib
import matplotlib.pyplot as plt
import time

# Define variables that can be used with all functions
samplesize = 1000  # How many individual trials
startingfunds = 100000
wagersize = 100
wagercount = 1000  # Length of individual trial


def rolldice():
    """ Generate a dice rolling, where you have 50/50 odds """

    roll = random.randint(1, 100)

    if roll <= 50:
        return False
    elif roll >= 51:
        return True


def dAlembert(funds, initial_wager, wager_count):
    """D'Alembert Strategy- for 50/50 odds. If start with $100 and lose then bet $200. If lose again bet $300. If then
    win bet $200, win bet $100, lose $200, etc.   """

    global ret
    global da_busts
    global da_profits
    value = funds
    wager = initial_wager
    currentwager = 1
    previouswager = 'win'
    previouswageramount = initial_wager

    while currentwager <= wager_count:
        if previouswager == 'win':              # Defining what your wager is
            if wager == initial_wager:
                pass
            else:
                wager -= initial_wager

            #print('current wager:', wager, 'value:', value)

            if rolldice():                      # If you win add to your funds
                value += wager
                #print('we won, current value:', value)
                previouswageramount = wager
            else:                               # If you lose subtract from funds
                value -= wager
                previouswager = 'loss'
                #print('we lost. current value:', value)
                previouswageramount = wager

                if value <= 0:                 # If you lose all your money, you broke!
                    da_busts += 1
                    break

        elif previouswager == 'loss':           # If you lost, add to wager by adding initial_wager (i.e. +100 to bet)
            wager = previouswageramount + initial_wager
            if (value - wager) <= 0:            # If you go negative by doing that just bet what you have left.
                wager = value

            #print('lost the last wager, current wager:', wager, 'value:', value)

            if rolldice():
                value += wager
                #print('we won, current value:', value)
                previouswageramount = wager
                previouswager = 'win'

            else:
                value -= wager
                #print('we lost, curren value:', value)
                previouswageramount = wager

                if value <= 0:
                    da_busts += 1
                    break

        currentwager += 1

    if value > funds:
        da_profits += 1

    #print(value)

    ret += value


ret = 0.0
da_busts = 0.0
da_profits = 0.0
dasampsize = 1000
counter = 1

while counter <= dasampsize:
    dAlembert(startingfunds, wagersize, wagercount)
    counter += 1

print('Total Invested:', dasampsize * startingfunds)
print('Total return:', ret)
print('ROI:', ret - (dasampsize * startingfunds))
print('Bust rate:', (da_busts/dasampsize) * 100.00)
print('Profit rate:', (da_profits/dasampsize) * 100.00)



''' Initally shown in the 50/50 odds section as the code, but was never used in that video or the next one. Not Sure if/
when it will actually be used. '''

# def multiple_bettor2(funds, inital_wager, wager_count, multiple):  #, color):
#     global ROI
#     global multiple_busts
#     global multiple_profits
#
#     value = funds
#     wager = inital_wager
#     wx = []
#     vy = []
#     currentwager = 1
#     previouswager = 'win'
#     previouswageramount = inital_wager
#
#     while currentwager <= wager_count:
#         if previouswager == 'win':
#             if rolldice():                # Somehow this knows to use rolldice before evaluating for the if or else
#                 value += wager              # if statements only execute true statements
#                 wx.append(currentwager)
#                 vy.append(value)
#             else:
#                 value -= wager
#                 previouswager = 'loss'
#                 previouswageramount = wager
#                 wx.append(currentwager)
#                 vy.append(value)
#                 if value <= 0:
#                     multiple_busts += 1
#                     break
#         elif previouswager == 'loss':
#             if rolldice():
#                 wager = previouswageramount * multiple
#                 if (value - wager) <= 0:
#                     wager = value
#
#                 value += wager
#                 wager = inital_wager
#                 previouswager = 'win'
#                 wx.append(currentwager)
#                 vy.append(value)
#             else:
#                 wager = previouswageramount * multiple
#                 if (value - wager) <= 0:
#                     wager = value
#                 value -= wager
#                 previouswager = 'loss'
#
#                 if value <= 0:
#                     multiple_busts += 1
#                     break
#
#         currentwager += 1
#     #print('ending value:', value)
#     ROI += value
#
#     plt.plot(wx,vy)
#
#     if value > funds:
#         multiple_profits += 1
#
#
# multiplesamplesize = 1000000
# multiple_busts = 0.0
# multiple_profits = 0.0
# ROI = 0
#
# counter2 = 1
# while counter2 <= multiplesamplesize:
#     multiple_bettor2(startingfunds, wagersize, wagercount, 1.75)
#     counter2 += 1

