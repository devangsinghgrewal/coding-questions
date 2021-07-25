# Non Constructible Change
# The function returns the minimum amount of change you cannot create
# coins = [1,1,2,6]
# Logic : The current coin value should be less than change + 1
def nonConstructibleChange(coins):
    coins.sort()
    change = 0 
    for coin in coins:
        if coin > change + 1:
            return change + 1
        change += coin
    return change + 1