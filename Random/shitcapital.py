def cap(a):
    n = len(a)
    l = []
    if len(a) == 1:
        return a
    for i in range(0, n):
        if a[i].isupper():
            l.append(a[i].lower())
        elif a[i].islower():
            if i > 0 and a[i - 1].isupper():
                l.append(a[i].upper())
            else:
                l.append(a[i])
    s = "".join(l)
    if a[n - 1] and a[n - 1].isupper():
       s = s[0].upper()+s[1:]
    return s


a = "MorgaNstAnleY"
b = cap(a)
print(b)
