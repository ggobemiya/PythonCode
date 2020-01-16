def commonCharacterCount(s1, s2):
    a=[]
    [a.append(min(s1.count(i),s2.count(i))) for i in list(set(s1))]   
    return sum(a)

# Codesignal>Arcade>Intro #10 Problem
# This is not a good answer. But that's the answer I can give you now. 20/01/16
# When I finish all Arcade, I can give a good answer.
