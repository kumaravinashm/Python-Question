def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist

a = "calvin klein design dress calvin dress klei dress dressn klein klein klein klein"
a = [2, 2, 3, 3, 3, 4, 4, 4, 5, 6, 5, 5, 4, 4, 43, 3, 4, 5, 7, 7, 8, 8, 9, 9, 9, 9, 9, 9, 9]
#a = ' '.join(unique_list(a.split()))
a = unique_list(a)
print(a)
