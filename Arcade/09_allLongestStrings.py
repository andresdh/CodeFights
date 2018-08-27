def allLongestStrings(inputArray):
    mayor = 0
    final_array = []
    # Busco el item mayor
    for x in inputArray:
        if len(x) > mayor:
            mayor = len(x)
        else:
            continue
    # Armo el array con los mayores
    for y in inputArray:
        if len(y) == mayor:
            final_array.append(y)
        else:
            continue

    return final_array

result = allLongestStrings(["asdf","asdf","asd","ff"])
print(result)
