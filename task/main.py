COINS = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount):
    result = {}
    for coin in COINS:
        if amount >= coin:
            num_coins = amount // coin
            result[coin] = num_coins
            amount -= num_coins * coin
    return result

def find_min_coins(amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    coin_used = [-1] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in COINS:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin
    
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    
    return result