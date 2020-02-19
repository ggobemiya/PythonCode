# Codesignal>Arcade>Intro #46 Problem
# This is not a good answer. But that's the answer I can give you now. 20/02/19
# When I finish all Arcade, I can give a good answer.

def electionsWinners(votes, k):
    ans = 0
    M = max(votes)
    if k == 0 and votes.count(M) == 1:
        ans = 1
    for i in votes:
#        v = list(votes)
#        v[i] += k
        if i+k>M:
            ans +=1
    return ans
