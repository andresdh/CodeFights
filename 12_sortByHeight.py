def sortByHeight(a):
    lista_final = []
    lista_sin_trees = []
    count = 0
    # Calculo de la lista sin los arboles
    for x in a:
        if x == -1:
            continue
        else:
            lista_sin_trees.append(x)

    # Ordeno la lista sin los arboles
    lista_sin_trees = sorted(lista_sin_trees)
    # Longitud de la lista para el for
    longitud = len(lista_sin_trees)-1

    # Calculo la lista final
    for x in a:
        if x == -1:
            lista_final.append(x)
        else:
            lista_final.append(lista_sin_trees[count])
            count = count + 1

    return lista_final

result = sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180])
print(result)
