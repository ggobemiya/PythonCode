def centuryFromYear(year):
    if year%100 > 0 and year%100 < 50 :
        return round(year/100) + 1
    elif year == 50 :
        return 1
    elif year%100 >= 50:
        return round(year/100)
    else :
        return round(year/100)

# Codesignal>Arcade>Intro #2 Problem
# This is not a good answer. But that's the answer I can give you now. 20/01/10
# When I finish all Arcade, I can give a good answer.
