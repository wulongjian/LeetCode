def maxProfit(prices):
    # result = []
    # for i, buy in enumerate(prices):
    #     for sold in prices[i+1:]:
    #         result.append(sold-buy)
    # return max(result)
    '''
    确实, 关键的一点就是dp[i] 函数/数组的定义
    dp[i]代表的到底是 i天买入的最大收益
        还是卖出的最大收益?
    确定了这个就思路清晰了.
    :param prices:
    :return:
    '''
    dp = []
    minist = prices[0]
    dp.append(0)
    for i in range(1, len(prices)):
        minist = min(minist, prices[i])
        dp.append(max(0, prices[i] - minist))
    return max(dp)


x = [7, 1, 5, 3, 6, 4]
y = maxProfit(x)
print(y)
