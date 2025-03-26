# erasing the lowest bit in a word
def erase_lowest_bit(x):
    return x & (x - 1)

# right propagate the rightmost set bit in x
def right_propagate(x):
    return x| (x-1)

# isolate the lowest bit that is 1 in x
x = 2
print(x& ~(x-1))
# test if x is an even number (equivalent to see whether the last bit is 0)
def iseven(x):
    # Idea: we check whether the rightmost bit of x is 0
    return x& ~(x-1) !=1

# test if x is a  power of 2 (equivalent to see whether the word has a form of (100000)_2)
def ispower2(x):
    # Idea: we erase the lowest bit of x once. If it becomes 0 then x is a power of 2.
    return not (x&(x-1))

# compute x mod a power of two, eg returns 13 for 77 mod 64
# step 1: given any x = (1xxxxx)_2, turn it into y = (10000000)_2
# step 2: return x^y
def mod_power2(x): # slow method
    count = 0
    while not ispower2(x):  # stop when x becomes a power of 2
        count+=x & ~(x-1)   # everytime collect the lowest bit of x
        x&=(x-1)            # remove the lowest bit of x
    return count
