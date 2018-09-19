# We want to turn the given integer into a number that has only one non-zero
# digit using a tail rounding approach. This means that at each step we take the
# last non 0 digit of the number and round it to 0 or to 10. If it's less than 5
#  we round it to 0 if it's larger than or equal to 5 we round it to 10 (rounding
#   to 10 means increasing the next significant digit by 1). The process stops
#   immediately once there is only one non-zero digit left.
#
# Example
#
# For n = 15, the output should be
# rounders(n) = 20;
#
# For n = 1234, the output should be
# rounders(n) = 1000.
#
# 1234 -> 1230 -> 1200 -> 1000.
#
# For n = 1445, the output should be
# rounders(n) = 2000.
#
# 1445 -> 1450 -> 1500 -> 2000.


def rounders(n):
    number = str(n)[::-1]
    no_ceros = len(number)-number.count("0",0,len(number))
    res = ""
    resto = 0

    for x in number:
        if x == "0":
            res += "0"
        elif no_ceros == 1:
            res += str(resto+int(x))[::-1]
        elif (int(x)+resto) >= 5:
            res += "0"
            resto = 1
            no_ceros -= 1
        else:
            res += "0"
            no_ceros -= 1
            resto = 0
    return int(res[::-1])

n=14999
print(rounders(n))
