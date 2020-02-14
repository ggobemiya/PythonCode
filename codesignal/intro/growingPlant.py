# Codesignal>Arcade>Intro #38 Problem
# This is not a good answer. But that's the answer I can give you now. 20/02/14
# When I finish all Arcade, I can give a good answer.

import math
def growingPlant(upSpeed, downSpeed, desiredHeight):
    ans = math.ceil((desiredHeight-downSpeed)/(upSpeed-downSpeed))
    if ans <0:
        ans = 1
    return ans
