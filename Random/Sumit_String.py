def sumit(a):
    for i in range(0, len(a)-1):
        if a[i + 1] == chr(ord(a[i]) + 1) or a[i + 1] == a[i] or a[i + 1] == chr(ord(a[i]) - 1):
            flag = 1
        else:
            flag = 0
            break
    if flag == 1:
        return "YES"
    else:
        return "NO"


s = "zazabcdefghgfgfededededcdefghghijkjihihgfe"
print(sumit(s))
