import time
tStart = time.time()

# Coin sum: solve by recursion backtracking somehow
# How many different ways can you arrive at 2 pounds = 200?
# there's a 2 pound coin, so start with 1 obvious way and leave out from coins

coins = [100, 50, 20, 10, 5, 2, 1]


def get_coins(diff, max_coin):
    if diff == 0:
        return 1
    if diff < 0:
        return 0
    result = 0
    for coin in coins:
        if coin <= max_coin and coin <= diff:
            result += get_coins(diff - coin, coin)
    return result

# Adding one b/c of the 2 pound coin
# coins[0] is the largest coin of the set
print get_coins(200, coins[0]) + 1



print "Run Time = {} seconds".format(time.time() - tStart)