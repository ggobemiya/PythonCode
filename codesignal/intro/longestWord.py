# Codesignal>Arcade>Intro #52 Problem
# This is not a good answer. But that's the answer I can give you now. 20/03/03
# When I finish all Arcade, I can give a good answer.

import re

def longestWord(text):
    return max(re.split('[^a-zA-Z]', text), key=len)
    
