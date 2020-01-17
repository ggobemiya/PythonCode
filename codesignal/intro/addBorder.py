# Codesignal>Arcade>Intro #15 Problem
# This is not a good answer. But that's the answer I can give you now. 20/01/17
# When I finish all Arcade, I can give a good answer.

def addBorder(picture):
    a = len(picture)
    b = len(picture[0])
    for i in range(a):
        picture[i] = '*'+picture[i]+'*'
    picture.insert(a,'*'*(b+2))
    picture.insert(0,'*'*(b+2))
    return picture
