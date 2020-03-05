# Codesignal>Arcade>Intro #54 Problem
# This is not a good answer. But that's the answer I can give you now. 20/03/05
# When I finish all Arcade, I can give a good answer.

import re
def sumUpNumbers(inputString):
    a = re.split('[^0-9]', inputString)
    b = []
    for i in range(len(a)):
        if len(a[i]):
            b.append(int(a[i]))
    if not len(b):
        return 0
    return sum(b)
