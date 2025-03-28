def int2str(x):
    isnegative = (x<0)
    if isnegative:
        x = -x
    s=[]
    while x!= 0:
        s.append(chr(ord('0')+x%10))
        x = x//10
    return ('-' if isnegative else '')+''.join(reversed(s))

import functools
import string
def str2int(s):
    return (-1 if s[0]=='-' else 1)* functools.reduce(lambda x,y:x*10+string.digits.index(y),s[s[0] in '-+':],0)

def convert_base(s,b1,b2):
    num10 = 0
    for ch in s:
        if ch=='A':
            num10 = num10*b1 +10
        elif ch=='B':
            num10 = num10 * b1 + 11
        elif ch=='C':
            num10 = num10 * b1 + 12
        elif ch=='D':
            num10 = num10 * b1 + 13
        elif ch=='E':
            num10 = num10 * b1 + 14
        elif ch=='F':
            num10 = num10 * b1 + 15
        else:
            num10 = num10 * b1 + string.digits.index(ch)
    converteds = []
    while num10!= 0:
        c = num10%b2
        if c==10:
            converteds.append('A')
        elif c==11:
            converteds.append('B')
        elif c==12:
            converteds.append('C')
        elif c==13:
            converteds.append('D')
        elif c==14:
            converteds.append('E')
        elif c==15:
            converteds.append('F')
        else:
            converteds.append(chr(ord('0')+c))
        num10 = num10//b2
    return ''.join(reversed(converteds))



