def centuryFromYear(year):
    if year%100 > 0 and year%100 < 50 :
        return round(year/100) + 1
    elif year == 50 :
        return 1
    elif year%100 >= 50:
        return round(year/100)
    else :
        return round(year/100)
