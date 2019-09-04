def removeDuplicates(arr, n):
    if n == 0 or n == 1:
        return n
    temp = []
    j = 0
    for i in range(0, n - 1):
        if arr[i] != arr[i + 1]:
            temp.append(arr[i])
            # j += 1
    # temp[j] = arr[n - 1]
    # j += 1
    arr = temp
    return arr

arr = [2,2, 3, 4, 4, 4, 5, 5, 5, 6, 6, 777, 90, 9494, 9494, 45644]
arr1=removeDuplicates(arr,len(arr))
print(arr1)
