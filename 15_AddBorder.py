# Given a rectangular matrix of characters, add a border of asterisks(*) to it.
#
# Example
# For
# picture = ["abc",
#            "ded"]
# the output should be
#
# addBorder(picture) = ["*****",
#                       "*abc*",
#                       "*ded*",
#                       "*****"]

def addBorder(picture):
    # defino la base y la altura
    base = len(picture[0])
    altura = len(picture)
    marco = "*" * (base+2)
    result = []

    # agrego el marco
    result.append(marco)
    for x in picture:
        result.append("*"+x+"*")
    result.append(marco)

    return result

x = addBorder(["abc","ded"])
print(x)
