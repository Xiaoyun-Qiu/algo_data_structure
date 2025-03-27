def dutch_flag(pivot,seq):
    # equal counts how many elements in the list equals to the pivot
    # bottom group: seq[:smaller]
    # equal group: seq[smaller:smaller+equal]
    # unclassified group: seq[smaller+equal:larger]
    # top group: seq[larger:]
    smaller,equal, larger = 0,0,len(seq)-1

    while smaller + equal <= larger:
        if seq[smaller+equal] < pivot:
            seq[smaller], seq[smaller+equal] = seq[smaller+equal], seq[smaller]
            smaller += 1
        elif seq[smaller+equal] == pivot:
            equal +=1
        else:
            seq[smaller+equal], seq[larger] = seq[larger], seq[smaller+equal]
            larger -=1
    return seq, smaller, equal

def dutch_flag2(seq):
    # suppose seq can only take 3 distinct values, group same values together
    # equal counts how many elements in the list equals to the pivot
    # bottom group: seq[:smaller]
    # equal group: seq[smaller:smaller+equal]
    # unclassified group: seq[smaller+equal:larger]
    # top group: seq[larger:]
    smaller,equal, larger = 0,0,len(seq)-1

    # find the correct pivot
    s  =list(set(seq))
    if len(s)<3:
        pivot = s[0]
    else:
        s.remove(max(s))
        pivot = max(s)

    while smaller + equal <= larger:
        if seq[smaller+equal] < pivot:
            seq[smaller], seq[smaller+equal] = seq[smaller+equal], seq[smaller]
            smaller += 1
        elif seq[smaller+equal] == pivot:
            equal +=1
        else:
            seq[smaller+equal], seq[larger] = seq[larger], seq[smaller+equal]
            larger -=1
    return seq

def dutch_flag3(seq):
    # suppose seq can only take 4 distinct values, group same values together
    # equal counts how many elements in the list equals to the pivot
    # bottom group: seq[:smaller]
    # equal1 group: seq[smaller:smaller+equal1]
    # equal2 group: seq[smaller+equal1: smaller+equal1+equal2]
    # unclassified group: seq[smaller+equal1+equal2:larger]
    # top group: seq[larger:]

    # find the correct pivot
    s = list(set(seq))
    if len(s) < 3:
        pivot = s[0]
        seq,smaller, equal = dutch_flag(pivot, seq)
    elif len(s)==3:
        s.remove(max(s))
        pivot = max(s)
        seq,smaller, equal= dutch_flag(pivot, seq)
    else:
        s.remove(max(s))
        s.remove(min(s))
        pivot1 = min(s)
        pivot2 = max(s)
        seq, smaller, equal = dutch_flag(pivot1, seq)
        seq[smaller+equal:],smaller1,equal2 = dutch_flag(pivot2, seq[smaller+equal:])
    return seq