# Codesignal>Arcade>Intro #23 Problem
# This is not a good answer. But that's the answer I can give you now. 20/01/23
# When I finish all Arcade, I can give a good answer.


def boxBlur(image):
    ans = []
    ans1 = []
    ans2 = []
    for i in range(len(image)-2):
        for j in range(len(image[0])-2):
            ans1.append(int((image[i][j]+image[i][j+1]+image[i][j+2]
                      +image[i+1][j]+image[i+1][j+1]+image[i+1][j+2]
                      +image[i+2][j]+image[i+2][j+1]+image[i+2][j+2])/9))
        ans = ans + [ans1]
        ans1 = []
    return ans
            
        
