# You are given an array of integers representing coordinates of obstacles situated on a straight line.
#
# Assume that you are jumping from the point with coordinate 0 to the right.
# You are allowed only to make jumps of the same length represented by some integer.
#
# Find the minimal length of the jump enough to avoid all the obstacles.
#
# Example
#
# For inputArray = [5, 3, 6, 7, 9], the output should be
# avoidObstacles(inputArray) = 4.

def avoidObstacles(inputArray):
    srd = sorted(inputArray)
    maxim = max(inputArray)+1
    new_list = []
    val = 0

    for x in range(1,maxim+1):
        if x in srd:
            continue
        else:
            new_list.append(x)

    # for x in range(2,max(new_list)+1):
    for x in new_list:
        flg = True

        for y in srd:
            # print(x,y)
            if y<x:
                continue
            elif x > (max(srd)):
                flg = True
            elif y%x == 0:
                flg = False
            else:
                continue

        if flg == True:
            val = x
            break
    # print(new_list)
    return val

x = [2,3]
print(avoidObstacles(x))
