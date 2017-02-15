import random

#Function to represent rolling the dice.
def rollDice():
    roll = random.randint(1, 100)

    if roll == 100:
        print(roll, 'roll was 100, you lose. What are the odds?! Play again!')
        return False
    elif roll <= 50:
        print(roll, 'roll was 1-50, you lose.')
        return False
    elif 100 > roll >= 50:
        print(roll, 'roll was 51-99, you win! *flashing lights! play more*')
        return True


'''
Simple Bettor, betting the same amount each time.
'''
def simple_bettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager

    currentWager = 0

    while currentWager < wager_count: #Run while current wager is less than wager_count(here it is 100)=>run only 100 times
        if rollDice():
            value += wager #Win add to funds
        else:
            value -= wager #lose subtract bet from funds


        currentWager += 1
        print('Funds:', value)

# testing the dice
#x = 0
#while x < 100:
#    result = rollDice()
#    print(result)
#    x += 1

simple_bettor(10000,100,100)