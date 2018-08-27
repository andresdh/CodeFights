# Two arrays are called similar if one can be obtained from another by swapping at
# most one pair of elements in one of the arrays.
# Given two arrays a and b, check whether they are similar.
# Example
#
# For a = [1, 2, 3] and b = [1, 2, 3], the output should be
# areSimilar(a, b) = true.
# The arrays are equal, no need to swap any elements.
#
# For a = [1, 2, 3] and b = [2, 1, 3], the output should be
# areSimilar(a, b) = true.
# We can obtain b from a by swapping 2 and 1 in b.
#
# For a = [1, 2, 2] and b = [2, 1, 1], the output should be
# areSimilar(a, b) = false.
# Any swap of any two elements either in a or in b won't make a and b equal.

def areSimilar(a, b):
    flg = False
    count_a = 0
    count_b = 0
    print("a: "+str(a))
    print("b: "+str(b))
    def comparar (a,b):
        x = 0
        val = 0
        val_2 = 0
        resultado = []
        count = 0
        while count == 0:
            if a[x] == b[x]:
                resultado.append(a[x])
                x = x + 1
            else:
                val = a[x]
                val_2 = b[x]
                count = 1
                resultado.append(val)
                x = x + 1
                for z in range(x,len(b)):
                    if b[z] == val and count < 2:
                        resultado.append(val_2)
                        count += count
                    else:
                        resultado.append(b[z])
        print("r: "+str(resultado))
        return resultado
#
# FALLA PORQUE NO UBICA EL LUGAR PRECISO DONDE ESTA EL VALOR QUE SE SUSTITUYE
#
    if a == b:
        flg = True
    else:
        if (comparar(a,b)) == a:
           flg = True
        else:
            if (comparar(b,a)) == b:
                flg = True
            else:
                flg = False

    return flg
a= [2, 1, 2, 1, 1, 1, 2]
b= [1, 1, 2, 1, 2, 1, 2]
x=  areSimilar(a,b)
print(x)
