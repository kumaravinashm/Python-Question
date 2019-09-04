def maxproducta(a):
    maxi = a[0]
    mini = a[0]
    cur_max = a[0]
    ans = a[0]
    for i in range(0, len(a)):
        cur_max = max(mini * a[i], maxi * a[i], a[i])
        cur_min = min(mini * a[i], maxi * a[i], a[i])
        maxi = cur_max
        mini = cur_min
        ans  = max(cur_max,ans)

    return ans

arr = [1, -2, -3, 0, 7, -8, -2]
print (maxproducta(arr))
