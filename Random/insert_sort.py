def insert_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j = j-1
        a[j + 1] = key
    return a


a = [234, 35, 235, 234, 234, 23]
print(insert_sort(a))
