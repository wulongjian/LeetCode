"""
编写一个函数来计算可以凑成总金额所需要的最少的硬币个数.
"""


def coinChange(coins, amount):
    dp = [amount+1]*(amount+1)
    dp[0]=0
    # 自下向上的设计思想,从0开始算起,最后的结果和上一个结果有关.
    for i in range(1, amount+1):
        for coin in coins:
            if i - coin < 0: continue
            dp[i] = min(dp[i], 1+dp[i-coin])
    return dp[amount] if dp[amount] != amount+1 else -1

coins = [1, 2, 5]
amount = 11
r = coinChange(coins, amount)
print(r)
