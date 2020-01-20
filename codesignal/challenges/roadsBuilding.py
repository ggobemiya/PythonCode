def roadsBuilding(cities, roads):
    b = []
    for i in range(0,cities):
        for j in range(0,cities):
            if j>i:
                b.append([i,j])
    c = []
    r = roads[:]
    for i in range(len(roads)):
        r.append(roads[i][::-1])
    for element in b:
        if element not in r:
            c.append(element)
    return c
