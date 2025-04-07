# find maximum profit of a given sequence of stock prices, with unlimited number of transactions
def max_profit(seq):
    current_price = seq[0]
    profit = 0
    for i in range(1,len(seq)):
        next_price = seq[i]
        profit += max(next_price - current_price,0)
        current_price = next_price
    return profit


if __name__ == '__main__':
    print(max_profit([1, 2, 3, 2, 5, 6, 7, 8, 9, 10]))
    print(max_profit([7,17,13,19,5]))
    print(max_profit([5,4,3,2,1]))

