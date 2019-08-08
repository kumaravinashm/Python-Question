def select_sort(a):
    n = len(a)
    for i in range(0, n - 1):
        imin = i
        for j in range(i + 1, n):
            if a[imin] > a[j]:
                imin = j
        a[i], a[imin] = a[imin], a[i]
    return a


arr = [234, 34, 34, 3, 32, 3, 6, 7, 96, 77, 45, 767]
print(select_sort(arr))
