def bubble_sort(a):
    n = len(a)
    for i in range(0, n - 1):
        swap = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swap = True
        if swap is False:
            break


arr = [345, 457, 23, 45, 568, 5, 435, 34, 4, 5, 65, 65, 34, 3464, 57, 54, 23, 42, 436, 4, 74, 57, 457, 4, 64, 57]
print(bubble_sort(arr))
