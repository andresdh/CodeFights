def commonCharacterCount(s1, s2):
    list_repetidos = []
    list_result = []
    countS1 = 0
    countS2 = 0

    # Verifico que caracteres estan repedidos
    for x in s1:
        for y in s2:
            if x == y:
                list_repetidos.append(x)
                break
            else:
                continue

    # Identifico los caracteres únicos
    list_repetidos = set(list_repetidos)

    # Busco en que string se repite menos

    for i in list_repetidos:
        # Para S1
        for js1 in s1:
            if i == js1:
                countS1 = countS1 + 1
            else:
                countS1
        # Para S2
        for js2 in s2:
            if i == js2:
                countS2 = countS2 + 1
            else:
                countS2

        # Verifico cual es menor
        if countS1 <= countS2:
            list_result.append(countS1)
            countS1 = 0
            countS2 = 0
        else:
            list_result.append(countS2)
            countS1 = 0
            countS2 = 0

    # Return con la suma del resultado        
    return sum(list_result)



result = commonCharacterCount("aabcc","adcaa")
print(result)
