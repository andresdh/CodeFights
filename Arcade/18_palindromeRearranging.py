def palindromeRearranging(inputString):
    long = len(inputString)
    flg = True
    odd = 0
    unicos = []
    cont = []

    for x in inputString:
        if x in unicos:
            continue
        else:
            unicos.append(x)

    for x in unicos:
        cont.append(inputString.count(x))
#caso par
    if long%2 == 0:
        for x in cont:
            if x%2 == 0:
                continue
            else:
                flg = False
#caso impar
    else:
        for x in cont:
            if x == 1 or x%2 != 0:
                odd = odd + 1
            else:
                continue
        if odd > 1:
            flg = False

    return flg



inputString = "aabbcd"
print(palindromeRearranging(inputString))
