def possibleSameCharFreqByOneRemoval(s):
    all_freq = {}
    for i in s:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    lst = [int(i) for i in all_freq.values()]
    maxi = max(lst)
    if all(x == lst[0] for x in lst):
        return maxi
    else:
        lst = [x-1 for x in lst]
        if 0 in lst and lst.count(0)==1:
            lst.remove(0)
            if all(x == lst[0] for x in lst):
                return maxi


if __name__ == "__main__":
    str1 = "aaaaaaaaaaggggggggggrrrrrrrrrrllllllllllbbbbbbbbbbe.........."
    if (possibleSameCharFreqByOneRemoval(str1)):
        print(possibleSameCharFreqByOneRemoval(str1))
    else:
        print(0)
