def makeArrayConsecutive2(statues):
    maximo = max(statues) + 1
    minimo = min(statues)
    result = 0
    complete_list = [value for value in range(minimo,maximo)]

    for number in complete_list:
        if number not in statues:
            result = result + 1

    return result

statues = makeArrayConsecutive2([5, 4, 6])
print(statues)
