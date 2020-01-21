def excelSheetColumnNumber(s):
    s1 = s[::-1]
    k = []
    for i in range(len(s1)):
        c = ord(s1[i])-64
        k.append(26**i*c)
    return sum(k)
