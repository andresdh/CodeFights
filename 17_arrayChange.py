a = [1,1,1]

def arrayChange(inputArray):
    count = 0
    dif = 0
    a = inputArray
    new = a
    for x in range(1,len(a)):
        if a[x] > new[x-1]:
            new[x]=(a[x])
            continue
        elif a[x] < new[x-1]:
            dif = new[x-1] - a[x] + 1
            count = count + dif
            new[x]=(dif + a[x])
        elif a[x] == new[x-1]:
            dif = 1
            count = count + dif
            new[x]=(dif + a[x])

    return count

x = arrayChange(a)
print(x)
