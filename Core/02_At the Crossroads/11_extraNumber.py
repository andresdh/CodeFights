# You're given three integers, a, b and c. It is guaranteed that two of these
# integers are equal to each other. What is the value of the third integer?
#
# Example
#
# For a = 2, b = 7, and c = 2, the output should be
# extraNumber(a, b, c) = 7.
#
# The two equal numbers are a and c. The third number (b) equals 7,
#  which is the answer.

a=2
b=7
c=2

def extraNumber(a, b, c):
    extra = 0

    if a == b:
        extra = c
    elif a == c:
        extra = b
    else:
        extra = a

    return extra

print(extraNumber(a,b,c))
