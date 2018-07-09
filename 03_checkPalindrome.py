# For inputString = "aabaa", the output should be
# checkPalindrome(inputString) = true;
# For inputString = "abac", the output should be
# checkPalindrome(inputString) = false;
# For inputString = "a", the output should be
# checkPalindrome(inputString) = true.

def checkPalindrome(inputString):
    # verifico la longitud
    longitud = len(inputString)
    letras = []
    last = longitud -1
    first = 0

    if longitud == 1:
        return True
    else:
        for letra in inputString:
            letras.append(letra)

        while last != first and first < last:
            if letras[first] == letras[last]:
                last = last - 1
                first = first + 1
                flg = True
                continue
            else:
                flg = False
                break

    return flg

check = checkPalindrome('abarttraba')
print(check)
