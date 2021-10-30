# non-constructible change

# given an array of postive integers, find out the min number that can be created from arary

def nonConstructibleChange(coins):
    coins.sort()
    curSum = 0
    for coin in coins:
        if coin > curSum + 1:
            return curSum + 1
        curSum += coin
    return curSum + 1
