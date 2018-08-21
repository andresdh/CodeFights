def arrayMaximalAdjacentDifference(inputArray):
    i = inputArray
    num = 0
    maxim = []
    def dif(a,b):
        maximo = max(a,b)
        minimo = min(a,b)
        dif = maximo-minimo
        return dif

    for x in range(0,len(i)-1):
        maxim.append(dif(i[x],i[x+1]))

    num = max(maxim)

    return num
