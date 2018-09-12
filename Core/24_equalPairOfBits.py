def equalPairOfBits(n, m):
    return 2**[x for x in range(0,32) if bin(n)[2:].zfill(32)[::-1][x] == bin(m)[2:].zfill(32)[::-1][x]][0]



n = 0
m = 0

print(equalPairOfBits(n,m))
