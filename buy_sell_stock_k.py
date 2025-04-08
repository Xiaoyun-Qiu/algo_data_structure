# find maximum profit of a given sequence of stock prices, with limited number of transactions
# recursive approach
def f(prices, dp, ind,buy,k):
    n = len(prices)
    if ind ==n or k ==0:
        return 0

    if dp[ind][buy][k] != -1:
        return dp[ind][buy][k]

    if buy ==0:
        return max(-prices[ind]+f(prices, dp, ind+1, 1, k), f(prices, dp, ind+1, 0, k))
    if buy == 1:
        return max(prices[ind]+f(prices, dp, ind+1, 0, k-1), f(prices, dp, ind+1, 1, k))

def max_profit(prices, k):
    dp = [[[-1 for _ in range(k+1)] for _ in range(2)] for _ in range(len(prices))]
    return f(prices, dp, 0, 0, k)

def max_profit2(prices, k):
    n = len(prices)
    # notice that the dimension of dp is (n+1)*2*(k+1) now!! because the continuation value for the last date is zero
    dp = [[[0 for _ in range(k + 1)] for _ in range(2)] for _ in range(n+1)]
    for ind in range(n-1,-1,-1):
        for buy in range(2):
            for cap in range(1,k+1):
                if buy == 0:
                    dp[ind][buy][cap] = max(dp[ind+1][0][cap], -prices[ind]+dp[ind+1][1][cap])
                if buy == 1:
                    dp[ind][buy][cap] = max(dp[ind+1][1][cap], prices[ind]+dp[ind+1][0][cap-1])
    return dp[0][0][k]

def max_profit3(prices, k):
    n = len(prices)
    # notice that the dimension of dp is (n+1)*2*(k+1) now!! because the continuation value for the last date is zero
    curr = [[0]*(k+1)  for _ in range(2)]
    ahead = [[0] * (k + 1) for _ in range(2)]
    for ind in range(n-1,-1,-1):
        for buy in range(2):
            for cap in range(1,k+1):
                if buy == 0:
                    ahead[buy][cap] = max(curr[0][cap], -prices[ind]+curr[1][cap])
                if buy == 1:
                    ahead[buy][cap] = max(curr[1][cap], prices[ind]+curr[0][cap-1])
        curr = ahead.copy()
    return ahead[0][k]

if __name__ == '__main__':
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    print(max_profit(prices, 2))
    print(max_profit2(prices, 2))
    print(max_profit3(prices, 2))

