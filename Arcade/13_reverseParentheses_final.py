def reverseParentheses(s):

    parentesis = s.count("(")
    lista_inicial = list(s)
    parentesis_s = 0
    lista_parentesis = []
    lista_final = []
    indice_lista_in = []
    lista_in = []

    while parentesis > 0:
        print("parentesis: "+ str(parentesis))
        print("lista_inicial: " + str(lista_inicial))
        # recorro la lista en busca de los parentesis
        for x in range(0,len(lista_inicial)):
            if lista_inicial[x] == "(":
                parentesis_s = parentesis_s + 1
                # chequeo si se trata del parentesis mas interno
                if parentesis_s == parentesis:
                    # si es igual guardo la ubicaciónote
                    lista_parentesis.append(x)
                    # guardo los valores dentro del parentesis hasta el cierre
                    x = x + 1
                    while lista_inicial[x] != ")":
                        lista_in.append(lista_inicial[x])
                        indice_lista_in.append(x)
                        x = x + 1
                    parentesis_cierre = x
                else:
                    continue
            else:
                continue

        lista_in.reverse()
        print("lista_in: " + str(lista_in))

        x = 0
        while x < len(lista_inicial):
            if x in lista_parentesis:
                x = x + 1
                continue
            elif x in indice_lista_in:
                for y in lista_in:
                    lista_final.append(y)
                    x = x + 1
            elif x == parentesis_cierre:
                x = x + 1
            else:
                lista_final.append(lista_inicial[x])
                x = x + 1

        indice_lista_in = []
        lista_in = []
        lista_parentesis = []
        lista_inicial = lista_final
        lista_final = []
        parentesis_s = 0
        parentesis = parentesis - 1

    return ''.join(str(e) for e in lista_inicial)

test = reverseParentheses("a(bcdefghijkl(mno)p)q")
print(test)
