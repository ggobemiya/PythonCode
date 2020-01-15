def numbersGrouping(a):
    b=[]
    for i in range(len(a)):
        b.append(int((a[i]-1)/10000))
    c= sorted(set(b))
    return len(a)+len(c)
