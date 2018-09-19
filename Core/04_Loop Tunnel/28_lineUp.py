# To prepare his students for an upcoming game, the sports coach decides to try some
# new training drills. To begin with, he lines them up and starts with the following
# warm-up exercise: when the coach says 'L', he instructs the students to turn to the left.
#  Alternatively, when he says 'R', they should turn to the right. Finally, when the coach
#   says 'A', the students should turn around.
#
# Unfortunately some students (not all of them, but at least one) can't tell left from right,
#  meaning they always turn right when they hear 'L' and left when they hear 'R'.
#   The coach wants to know how many times the students end up facing the same direction.
#
# Given the list of commands the coach has given, count the number of such commands after
#  which the students will be facing the same direction.
#
# Example
#
# For commands = "LLARL", the output should be
# lineUp(commands) = 3.
#
# Let's say that there are 4 students, and the second one can't tell left from right.
# In this case, only after the second, third and fifth commands will the students face
# the same direction.

def lineUp(commands):
    res=0
    poss_ok="N"
    poss_ko="N"
    #CIRCULAR LIST
    def position(cardinal,command):
        new_pos = ""
        cardinal_list=["N","E","S","W"]
        len_card=len(cardinal_list)
        indx = cardinal_list.index(cardinal)
        if command == "A":
            new_pos = cardinal_list[(indx+2)%len_card]
        elif command == "R":
            new_pos = cardinal_list[(indx+1)%len_card]
        elif command =="L":
            new_pos = cardinal_list[(indx-1)%len_card]
        # print(indx)
        return new_pos

    for x in commands:
        # print("command: "+x)
        if x == "A":
            poss_ok = position(poss_ok,x)
            poss_ko = position(poss_ko,x)
        elif x == "L":
            poss_ok = position(poss_ok,x)
            poss_ko = position(poss_ko,"R")
        elif x == "R":
            poss_ok = position(poss_ok,x)
            poss_ko = position(poss_ko,"L")
        # print(poss_ok,poss_ko)
        if poss_ko == poss_ok:
            res +=1

    return res

commands = "RRRRRRRRRRLLLLLLLLLRRRRLLLLLLLLLL"
print(lineUp(commands))
#
# 90  90
# 180 0
# 270 270
# 90  90
# 0   0
# 90  270
