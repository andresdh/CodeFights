def adjacentElementsProduct(inputArray):
    # defino last y first item
    last = len(inputArray) - 1
    first = 0
    adj = first + 1
    producto = 0
    # recorro el array
    while first < last:
        producto_new = inputArray[first] * inputArray[adj]
        if producto_new > producto or producto == 0:
            producto = producto_new
            first += 1
            adj += 1
        else:
            first += 1
            adj += 1

    return producto

prod = adjacentElementsProduct([-23, 4, -3, 8, -12])
print(prod)
