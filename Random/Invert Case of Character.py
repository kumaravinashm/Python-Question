def invert(s, n):
    l = []
    for i in range(0, len(n)):
        n[i] = int(n[i])
    n[:] = [x - 1 for x in n]
    for i in range(len(s)):
        if i in n:
            if s[i]=="@":
                l.append("@")
            elif s[i].isupper():
                l.append(s[i].lower())
            elif s[i].islower():
                l.append(s[i].upper())
        else:
            l.append(s[i])
    return "".join(l)

s = "IEEE Ch@irperson"
n = [3,8]
print(invert(s,n))
