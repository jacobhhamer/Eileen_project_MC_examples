import random
import matplotlib
import matplotlib.pyplot as plt
import time

# Define variables that can be used with all functions
samplesize = 1000  # How many individual trials
startingfunds = 10000
wagersize = 100
wagercount = 100  # Length of individual trial


def rolldice():
    """ Generate a dice rolling, where you have 50/50 odds """

    roll = random.randint(1, 100)

    if roll <= 50:
        return False
    elif roll >=51:
        return True


def multiple_bettor2(funds, inital_wager, wager_count, multiple):  #, color):
    global ROI
    global multiple_busts
    global multiple_profits

    value = funds
    wager = inital_wager
    wx = []
    vy = []
    currentwager = 1
    previouswager = 'win'
    previouswageramount = inital_wager

    while currentwager <= wager_count:
        if previouswager == 'win'
            if rolldice():
                value += wager
                wx.append(currentwager)
                vy.append(value)

