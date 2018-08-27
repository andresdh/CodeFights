def reverseParentheses(s):

    lista_inicial = list(s)
    lista_index = []
    lista_pie = []
    lista_cabeza = []
    lista_final = []
    count_car = 0
    parentesis = s.count("(")
    count_in = 0
    count_out = 0

    for x in range(0,len(lista_inicial)):
        if lista_inicial[x] == "(":
            if count_in == 0:
                lista_index.append(x+1)
            x = x + 1
            if parentesis > 1:
                while count_in == 0:
                    if lista_inicial[x] == "(":
                        x = x + 1
                        count_in = 1
                        continue
                    else:
                        lista_pie.insert(0,lista_inicial[x])
                        count_car = count_car + 1
                        x = x + 1
                        continue
            else:
                while lista_inicial[x] != ")":
                    lista_in.append(lista_inicial[x])
                    x = x + 1
        elif lista_inicial[x] == ")" and count_out == 0 and parentesis > 1:
            # x = x + 1
            while lista_inicial[x] != ")":
                lista_cabeza.insert(0,lista_inicial[x])
                count_out = count_out + 1
        else:
            continue
    x = 0
    while x < len(lista_inicial):
        if lista_inicial[x] == "(":
            x = x + 1
            continue
        elif x in lista_index:
            for i in lista_pie:
                x = x + 1
                lista_final.append(i)
        else:
            lista_final.append(lista_inicial[x])
            x = x + 1


    print("lista final: " + str(lista_final))
    print("lista cabeza: " + str(lista_cabeza))
    print("lista index: " + str(lista_index))
    print(lista_pie)
    print(lista_inicial)
    print(count_car)



result = reverseParentheses("co(de(fight)s)")
print(result)
