# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# You're given two integers, n and m. Find position of the rightmost bit in which they differ
#  in their binary representations (it is guaranteed that such a bit exists), counting from right to left.
#
# Return the value of 2position_of_the_found_bit (0-based).
#
# Example
#
# For n = 11 and m = 13, the output should be
# differentRightmostBit(n, m) = 2.
#
# 1110 = 10112, 1310 = 11012, the rightmost bit in which they differ is the bit at position
#  1 (0-based) from the right in the binary representations.
# So the answer is 21 = 2.
#
# For n = 7 and m = 23, the output should be
# differentRightmostBit(n, m) = 16.
#
# 710 = 1112, 2310 = 101112, i.e.
#
# 00111
# 10111
# So the answer is 24 = 16.

def differentRightmostBit(n, m):
    # print(bin(n)[2:].zfill(8))
    # print(bin(n)[2:].zfill(8)[::-1][x])

    # return True
    return 2**[x for x in range(0,32) if bin(n)[2:].zfill(32)[::-1][x] != bin(m)[2:].zfill(32)[::-1][x]][0]


n = 11
m = 13

print(differentRightmostBit(n,m))
