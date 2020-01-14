def giftSafety(gift):
    ans = 0
    if len(gift)==2:
        return ans
    for i in range(len(gift)-2):
        if gift[i]==gift[i+1] or gift[i+1]==gift[i+2] or gift[i]==gift[i+2]:
            ans +=1
    return ans

# Codesignal > Challenges
# This is not a good answer. But that's the answer I can give you now. 20/01/14
# When I finish all Arcade, I can give a good answer.
