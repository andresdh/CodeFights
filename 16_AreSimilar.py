def areSimilar(a, b):
    # verifico y devuelvo las diferencias
    def distintos(a,b):
        a1=[]
        b1=[]
        for x in range(0,len(a)):
            if a[x] == b [x]:
                continue
            else:
                a1.append(a[x])
                b1.append(b[x])
        return a1,b1

    def forceBrute(a,b):
        for x in range(0,len(a)):
            for y in range(1,len(a)):
                if y <= x:
                    continue
                else:
                    resultado = []
                    for i in range(0,len(a)):
                        if i == y:
                            resultado.append(a[x])
                        elif i == x:
                            resultado.append(a[y])
                        else:
                            resultado.append(a[i])
                    # print(resultado)

                    if resultado == b:
                        return True
                    else:
                        resultado = []
        return False

    flg = False
    if a == b:
        flg = True
    else:
        a1,b1 = distintos(a,b)
        if len(a1)>2:
            flg = False
        else:
            flg = forceBrute(a1,b1)
    return flg

a= [2, 3, 1]
b= [3, 2, 1]
# a= [2, 1, 2, 1, 1, 1, 2]
# b= [1, 1, 2, 1, 2, 1, 2]
# a= [832, 998, 148, 570, 533, 561, 894, 147, 455, 279,561, 894, 147, 455, 279,561, 894, 147, 455, 279,561, 894, 147, 455, 279,561, 894, 147, 455, 279,561, 894, 147, 455, 279,561, 894, 147, 455, 279,561, 894, 147, 455, 279]
# b= [832, 998, 148, 570, 533, 561, 455, 147, 894, 279,561, 894, 147, 455, 279,561, 894, 147, 455, 279,561, 894, 147, 455, 279,561, 894, 147, 455, 279,561, 894, 147, 455, 279,561, 894, 147, 455, 279,561, 894, 147, 455, 279]

x=  areSimilar(a,b)
print(x)
