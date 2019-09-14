def cinema(sam,friends):
    s = sam[1]
    n = sam[0]
    i, j = 0, n
    a = sorted(friends)
    while i + 1 < j and a[i] <= s <= a[j - 1]:
        i += 1
        j -= 1
    print(j-i)






sam = [1, 5]
friends = [4]
cinema(sam,friends)