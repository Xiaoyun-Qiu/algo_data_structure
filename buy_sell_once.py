def max_profit(seq):
    profit = 0
    cmin = float('inf')
    for price in seq:
        profit = max(profit,price-cmin)
        cmin = min(price,cmin)
    return profit

def longest_subarray(seq):
    maxlength, count, num = 1, 1, seq[0]
    for i in range(1,len(seq)):
        if seq[i] == num:
            count += 1
            maxlength = max(maxlength, count)
        else:
            count = 1
            num = seq[i]
    return maxlength

# a more concise version
def longest_subarray2(seq):
    maxlength, count, num= 1, 1, seq[0]
    for item in seq[1:]:
        count = count*(item == num) + 1
        num = item
        maxlength = max(maxlength, count)
    return maxlength