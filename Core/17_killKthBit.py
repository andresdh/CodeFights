def killKthBit(n, k):
    return int(bin(n)[2:].zfill(8)[:-k]+"0"+bin(n)[2:].zfill(8)[-k+1:],2)

n=0
k=4

print(killKthBit(n,k))
