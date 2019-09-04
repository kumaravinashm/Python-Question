def first_occur(s):
    l = []
    for i in range(0,len(s)):
        if s[i] not in l:
            l.append(s[i])
    return "".join(l)

s = "aljjbqwlkweflkhwef"
print(first_occur(s))