a = [2, 3, 1, 2, 1]
b = [2, 3, 1, 2, 1]

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

a1,b1 = distintos(a,b)
a1_len = len(a1)
b1_len = len(b1)

print (a1)








# print (a)
# # r = []
# for x in range(0,len(a)):
#     for y in range(1,len(a)):
#         if y <= x:
#             continue
#         else:
#             # r=[x,y]
#             # print(r)
#             resultado = []
#             for i in range(0,len(a)):
#                     if i == y:
#                         resultado.append(a[x])
#                     elif i == x:
#                         resultado.append(a[y])
#                     else:
#                         resultado.append(a[i])
#             print(resultado)
#             resultado=[]
#             # r=[]
#             # print(str(x)+","+str(y))
