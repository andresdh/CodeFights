def isLucky(n):
    resultado = False
    longitud = int(len(str(n))/2)
    count = 0
    sum1 = []
    sum2 = []
    lista_n = list(str(n))

    # Creo 2 listas con los numeros de cada mitad
    for x in lista_n:
        if count < longitud:
            sum1.append(x)
            count = count + 1
        else:
            sum2.append(x)
            count += count

    # Convierto a Int y sumo
    sum1 = sum(int(x) for x in sum1)
    sum2 = sum(int(x) for x in sum2)

    # Resultado final
    if sum1 == sum2:
        return True
    else:
        return False

result = isLucky(123123)
print(result)
