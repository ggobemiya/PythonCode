def adjacentElementsProduct(inputArray):
    b=[]
    for i in range(len(inputArray)-1):
        k=inputArray[i]*inputArray[i+1]
        b.append(k)
    return max(b)
