def kadane_also(a):
    maxsofar = 0
    maxendinghere = 0
    for i in range(0, len(a)):
        maxendinghere = maxendinghere + a[i]
        if maxendinghere<0
            maxendinghere = 0
        elif maxsofar<maxendinghere:
            maxsofar=maxendinghere
    return maxsofar


arr = [1, -2, -3, 0, 7, -8, -2, -2, -2, -2, 8]
suma = kadane_also(arr)
print(suma)
