def reverseParentheses(s):
    lista_in = []
    lista_s = list(s)
    count = 0
    lista_final = []
    lista_idx = []
    count_open = 0
    count_close = 0
    x = 0

    # Contar cuantos "(" hay
    parentesis = s.count("(")

    # Defino los caracteres dentro de los parentesis
    for x in range(0,len(lista_s)):
        print(lista_in)
        if lista_s[x] == "(" and count_open == 0:
            count_open = count_open + 1
            lista_idx.append(x+1)
            x = x + 1
            if parentesis > 1:
                while count_close < 2:
                    if lista_s[x] == ")":
                        count_close = count_close + 1
                        if count_close == 2:
                            lista_idx.append(x)
                            continue
                    lista_in.append(lista_s[x])
                    x = x + 1
            else:
                 while lista_s[x] != ")":
                    lista_in.append(lista_s[x])
                    x = x + 1
        else:
            continue

    if parentesis > 1:
        count_open = 0
        count_close = 0
        x = 0
        lista_in2 = []

        if lista_in[x] == "(" and count_open == 0:
            count_open = count_open + 1
            x = x + 1
             while lista_s[x] != ")":
                lista_in2.append(lista_s[x])
                x = x + 1
        else:
            continue

    # Ordeno desendente la lista dentro del parentesis
    lista_in.reverse()
    # print(lista_in)

    print(lista_idx)

    # Creo la lista final
    for x in range(0,len(lista_s)):
        if lista_s[x] == "(" or lista_s[x] == ")":
            continue
        elif x in lista_idx:
            lista_final.append(lista_in[count])
            count = count + 1
        else:
            lista_final.append(lista_s[x])





    respuesta = ''.join(str(e) for e in lista_final)

    return respuesta




result = reverseParentheses("co(de(fight)s)")
print(result)
