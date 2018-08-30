# If you played the first Teenage Mutant Ninja Turtles game on the Nintendo
 # Entertainment System, you might have some unpleasant memories of a very
 # difficult and frustrating level where you have to swim around the Hudson
  # River, disarming bombs and avoiding deadly obstacles.
#
# TMNT dam level
#
# Your friend is working on a romhack of the game that's just based on this
 # one horrific level. She's a big fan of the GDQ events, so she's designing
  # the game as a speedrunning challenge.
#
# This version of the game is quite simple - you just need to swim through a
 # long corridor as fast as possible, while avoiding being shocked by the
  # electric gates. Each gate has its own period of activation based on a
   # global timer that begins at the start of the level; for example, if the
    # period is 5 then the gate deactivates every 5 seconds (for 1 second at
     # a time), so it can only be passed through at times 5, 10, 15, etc.
      # However, if you have enough energy remaining, it's also possible to
       # "damage boost" by passing through the gate while it's still active.
#
# Given an array gates, containing 2-element arrays of the form
 # [location, period] for each gate, and an integer energy, your task is
  # to find the fastest time (in seconds) that the level can be completed.
#
# NOTES:
#
# It takes 1 second to move 1 tile horizontally
# To move past an electric gate, the total time must be a multiple of the gate's period
# Going through the gate when it's still active will deal 1 point of damage
# The game ends if your energy drops below 1
# The level is considered successfully completed the moment you swim through the final gate
# You always start at position 0
# Example
#
# For gates = [[1, 2], [3, 5]] and energy = 1, the output should be waterLevel(gates, energy) = 5
#
# example 1
#
# Since you only have 1 energy, you'll have to wait for both gates to deactivate. You arrive at the first gate after 1 second, so you'll have to wait another second, since the period of this gate is 2. After that, you make it to the second gate after 4 seconds, so you'll need to wait another second to pass through. So after 5 seconds total, you've completed the level.
#
# For gates = [[1, 2], [3, 5]] and energy = 2, the output should be waterLevel(gates, energy) = 4
#
# example 2
#
# Since you have 2 energy, you have one to spare, so you can pass through one
 # of the gates while it's still active. If you were to damage boost through
  # the first one, you'd make it to the second gate after 3 seconds, so you'd
  # still need to wait 2 more seconds to pass (since it has a period of 5).
#
# So the better choice is to wait for the first gate, then damage boost through
 # the second gate. The level is complete after 4 seconds.
#
# For gates = [[1, 2], [3, 5]] and energy = 3, the output should be waterLevel(gates,
 # energy) = 3
#
# example 3
#
# You have enough energy to damage boost through both gates, so you can just sprint
 # to the finish without waiting. Since you need to make it to position 3, it'll
  # take 3 seconds total.
#
# Input / Output
#
# [execution time limit] 4 seconds (py3)
#
# [input] array.array.integer gates
#
# An array of 2-element arrays of the form [location, period], sorted in
 # ascending order of location. All gates are guaranteed to have a unique
  # location (no gates overlap).
#
# Guaranteed constraints:
# 1 ≤ gates.length ≤ 200
# gates[i].length = 2
# 1 ≤ gates[i][0] ≤ 108
# 2 ≤ gates[i][1] ≤ 105
#
# [input] integer energy
#
# An integer representing how much energy you start with.
#
# Guaranteed constraints:
# 1 ≤ energy ≤ 50
#
# [output] integer
#
# The fastest possible time (in seconds) that the level could be completed in.

def waterLevel(gates, energy):
    time = 0
    maxtime = gates[-1][0]
    for [x][y] in gates:
        print(x)
        print(y)

    print(maxtime)

    return time


gates=[[1, 2], [3, 5]]
energy=1
print(waterLevel(gates,energy))
