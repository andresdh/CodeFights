# Define an integer's roundness as the number of trailing zeroes in it.
#
# Given an integer n, check if it's possible to increase n's roundness by swapping some
#  pair of its digits.
#
# Example
#
# For n = 902200100, the output should be
# increaseNumberRoundness(n) = true.
#
# One of the possible ways to increase roundness of n is to swap digit 1 with digit 0
#  preceding it: roundness of 902201000 is 3, and roundness of n is 2.
#
# For instance, one may swap the leftmost 0 with 1.
#
# For n = 11000, the output should be
# increaseNumberRoundness(n) = false.
#
# Roundness of n is 3, and there is no way to increase it.


def increaseNumberRoundness(n):
    flg = False
    number = str(n)[::-1]
    i_c = ceros = number.count("0",0,len(number))
    i_nc = no_ceros = len(number)-ceros
    if ceros == 0:
        flg = False
    else:
        for x in enumerate(number):
            if x[1] == "0":
                ceros -= 1
            else:
                no_ceros -= 1
            if ceros == 0 and no_ceros > 0:
                break
            elif ceros > 0 and no_ceros < i_nc:
                flg = True
                break
    return flg

n = 103456789
print(increaseNumberRoundness(n))
