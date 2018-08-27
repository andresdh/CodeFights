a = ["172.16.254.1",".2.222.111","11..32.33","331.321.33.2","12,12,.32"]

def isIPv4Address(inputString):
    intlist = [0,1,2,3,4,5,6,7,8,9]
    num = ""
    numlist = []
    flg = True
    if inputString.count(".") == 3 and inputString[0] != ".":
        for x in inputString:
            if x != ".":
                if x in str(intlist):
                    num += x
                else:
                    flg = False
                    break
            else:
                if num == "":
                    break
                    flg = False
                else:
                    numlist.append(int(num))
                    num = ""

        if num != "" and flg == True:
            numlist.append(int(num))
            for x in numlist:
                if x >= 0 and x <= 255:
                    flg = True
                else:
                    flg = False
                    break
        else:
            flg = False
    else:
        flg = False

    return flg

for x in a:
    print(str(x)+" --> "+ str(isIPv4Address(x)))
