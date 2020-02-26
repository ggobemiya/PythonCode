# Codesignal>Arcade>Intro #50 Problem
# This is not a good answer. But that's the answer I can give you now. 20/02/26
# When I finish all Arcade, I can give a good answer.

def chessKnight(cell):
    ans = 0
#    if ord(cell[0])-2<97 and ord(cell[1])+1 >56 :
#        ans -= 1
#    if ord(cell[0])-2<97 and ord(cell[1])-1 <49 :
#        ans -= 1
#    if ord(cell[0])-1<97 and ord(cell[1])+2 >56 :
#        ans -= 1
#    if ord(cell[0])-1<97 and ord(cell[1])-2 <49 :
#        ans -= 1                        
#    if ord(cell[0])+2>104 and ord(cell[1])+1 >56 :
#        ans -= 1
#    if ord(cell[0])+2>104 and ord(cell[1])-1 <49 :
#        ans -= 1
#    if ord(cell[0])+1>104 and ord(cell[1])+2 >56 :
#        ans -= 1
#    if ord(cell[0])+1>104 and ord(cell[1])-2 <49 :
#        ans -= 1                                
#
    k1 = [[-2, -2, -1, -1, +2, +2, +1, +1], [+1, -1, +2, -2, +1, -1, +2, -2]]
    k2 = [['a','b','c','d','e','f','g','h'],['1','2','3','4','5','6','7','8']]
    for i in range(8):
        if chr(ord(cell[0])+k1[0][i]) in k2[0] and chr(ord(cell[1])+k1[1][i]) in k2[1]:
            ans +=1
        

    return ans
