
# Given an array of positive integers, return the min
# amount of change that you cannot create

def nonConstructibleChange(coins):
    # Write your code here.
    coins.sort()
    curSum = 0
    for coin in coins:
        if coin > curSum + 1:
            return curSum + 1
        curSum += coin
    return curSum + 1
