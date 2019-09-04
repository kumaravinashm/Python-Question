def rev_sen(sen):
    lst = sen.split(" ")
    temp = []
    for i in lst:
        temp.insert(0,i)
    sen1 = " ".join(temp)
    return sen1


s = "kwek wkedkne dk2edk edk2 wdkj edk3 edkj ekjd kje dkj edkj"
t = rev_sen(s)
print(t)
