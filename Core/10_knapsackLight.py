# You found two items in a treasure chest! The first item weighs weight1 and is
# worth value1, and the second item weighs weight2 and is worth value2. What is
# the total maximum value of the items you can take with you, assuming that your
#  max weight capacity is maxW and you can't come back for the items later?
#
# Note that there are only two items and you can't bring more than one item of
# each type, i.e. you can't take two first items or two second items.
#
# Example
#
# For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, and maxW = 8, the output should be
# knapsackLight(value1, weight1, value2, weight2, maxW) = 10.
#
# You can only carry the first item.
#
# For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, and maxW = 9, the output should be
# knapsackLight(value1, weight1, value2, weight2, maxW) = 16.
#
# You're strong enough to take both of the items with you.
#
# For value1 = 5, weight1 = 3, value2 = 7, weight2 = 4, and maxW = 6, the output should be
# knapsackLight(value1, weight1, value2, weight2, maxW) = 7.
#
# You can't take both items, but you can take any of them.


value1= 4
weight1= 3
value2= 3
weight2= 4
maxW= 4

def knapsackLight(value1, weight1, value2, weight2, maxW):
    res = 0
    res2= 0
    if (weight1 + weight2) > maxW:
        if maxW >= weight1:
            res = value1
        if maxW >= weight2:
            res2 = value2
    else:
        res = value1 + value2

    if res > res2:
        return res
    else:
        return res2

print(knapsackLight(value1, weight1, value2, weight2, maxW))
