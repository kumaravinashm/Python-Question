def sort(a):
    lo = 0
    hi = len(a)-1
    mid = 0
    while mid <= hi:
        if a[mid] == 0:
            a[lo], a[mid] = a[mid], a[lo]
            lo=lo+1
            mid=mid+1
        elif a[mid]==1:
            mid=mid+1
        else:
            a[hi], a[mid] = a[mid], a[hi]
            hi = hi -1




arr = [1, 1, 1, 1, 2, 0, 0, 0, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0]
sort(arr)
print(arr)
