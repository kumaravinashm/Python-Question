# s= input()
s = "Prof Moinuddin"
lst = s.split(" ")
for i in range(0,len(lst)):
    if i == 0:
        first = str(lst[0][0])+". "
    if len(lst)>2:
        full  = first+str(lst[1][0])+". "+ " ".join(lst[2:])
    if len(lst)==2:
        full = first + " ".join(lst[1:])
print(full)