# Codesignal>Arcade>Intro #48 Problem
# This is not a good answer. But that's the answer I can give you now. 20/02/26
# When I finish all Arcade, I can give a good answer.

def lineEncoding(s):
    g=[]
    a=0
    for i in range(len(s)-1):
        if ord(s[i])!=ord(s[i+1]):
            g.append(s[a:i+1])
            a=i+1
        if i == len(s)-2:
            g.append(s[a:])
    a=''
    for i in range(len(g)):
        if len(g[i])>1:
            a+= str(len(g[i]))+g[i][:1]
        else:
            a+= g[i]
    return a
