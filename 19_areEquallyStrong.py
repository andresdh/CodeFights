def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    your = yourLeft + yourRight
    friend = friendsLeft + friendsRight
    maxYour = max(yourLeft,yourRight)
    maxFriend = max(friendsLeft,friendsRight)
    flg = False

    if your == friend:
        if maxYour == maxFriend:
            flg = True

    return flg

res = areEquallyStrong(15,10,15,9)
print(res)
