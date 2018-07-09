def shapeArea(n):
    shape_squares = []
    for number in range(1,n+1):
        shape_squares.append(number)

    shape_area = sum(shape_squares)
    cuadrado = n ** 2
    unshape_area = (cuadrado - shape_area) * 4

    shape_area = (n + (n - 1)) ** 2 - unshape_area
    return shape_area

n = shapeArea(5)
print(n)
