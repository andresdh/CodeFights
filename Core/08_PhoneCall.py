def phoneCall(min1, min2_10, min11, s):
    res = 0
    if s >= min1:
        res += 1
        s -= min1
    for x in range(0,9):
        if s >= min2_10:
            res += 1
            s -= min2_10
        else:
            break
    if res == 10:
        for x in range(0,s):
            if s >= min11:
                res += 1
                s -= min11
    return res

min1 = 3
min2_10= 1
min11 = 2
s = 20

print (phoneCall(min1, min2_10, min11, s))
